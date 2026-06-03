#!/usr/bin/env python3
"""
classify.py — Image classification on the CPU with ONNX Runtime.

Why this exists
---------------
This is the "runs anywhere" edge-AI starter. It needs **no GPU and no NPU** —
just Python, ONNX Runtime, and Pillow — so you can learn the full inference
flow (load -> preprocess -> run -> post-process) on the laptop you already own,
then move the *same* code to a Jetson, a Raspberry Pi, or an Intel box by
swapping the ONNX Runtime Execution Provider.

The flow (every edge model looks like this)
-------------------------------------------
    1. Load a model            -> ort.InferenceSession(...)
    2. Pre-process the input   -> resize, to float, normalize, NCHW layout
    3. Run inference           -> session.run(...)
    4. Post-process the output -> softmax -> top-k labels

Usage
-----
    python classify.py --model mobilenetv2-7.onnx --image cat.jpg --labels imagenet_classes.txt

    # Quick environment check (no image/model needed) — proves ONNX Runtime works:
    python classify.py --selftest

See the companion README (onnxruntime-image-classification.md) for exact,
copy-paste commands to download a known-good model and labels.
"""

import argparse
import sys

import numpy as np
import onnxruntime as ort

# Standard ImageNet normalization. Most pretrained classification models
# (MobileNet, ResNet, SqueezeNet, EfficientNet) expect inputs normalized
# with these per-channel means/stds after scaling pixels to the 0..1 range.
IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)


def load_labels(path):
    """Read a labels file (one class name per line) into a list.

    Returns None if no path is given, in which case we print raw class indices.
    """
    if not path:
        return None
    with open(path, "r", encoding="utf-8") as f:
        # strip() drops trailing newlines/spaces; keep order = class index order
        return [line.strip() for line in f if line.strip()]


def preprocess_image(image_path, size=224):
    """Turn an image file into the (1, 3, H, W) float32 tensor models expect.

    Steps: open -> RGB -> resize -> 0..1 floats -> normalize -> HWC->CHW -> add batch dim.
    Pillow is imported here so `--selftest` works even without an image library quirk.
    """
    from PIL import Image  # local import keeps the selftest path dependency-light

    img = Image.open(image_path).convert("RGB")  # force 3 channels (drops alpha/grayscale)
    img = img.resize((size, size))               # square resize to the model's input size
    x = np.asarray(img, dtype=np.float32) / 255.0  # HWC, pixels now in [0, 1]
    x = (x - IMAGENET_MEAN) / IMAGENET_STD          # per-channel normalize
    x = np.transpose(x, (2, 0, 1))                  # HWC -> CHW (channels first)
    x = np.expand_dims(x, axis=0)                   # add batch dim -> (1, 3, H, W)
    return x.astype(np.float32)


def softmax(logits):
    """Numerically stable softmax over a 1-D array of logits -> probabilities."""
    logits = logits.astype(np.float32)
    z = logits - np.max(logits)      # subtract max for numerical stability
    e = np.exp(z)
    return e / np.sum(e)


def top_k(probs, labels=None, k=5):
    """Return the top-k (label, probability) pairs, highest first."""
    k = min(k, probs.shape[0])
    idx = np.argsort(probs)[::-1][:k]   # indices of the k largest probabilities
    out = []
    for i in idx:
        name = labels[i] if labels and i < len(labels) else f"class_{i}"
        out.append((name, float(probs[i])))
    return out


def classify(model_path, image_path, labels_path=None, size=224, k=5):
    """Full pipeline: load model, preprocess image, run, post-process, return top-k."""
    # CPUExecutionProvider runs on any machine. On a Jetson you'd add
    # "CUDAExecutionProvider"/"TensorrtExecutionProvider"; on Intel, "OpenVINOExecutionProvider".
    session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])

    input_name = session.get_inputs()[0].name   # don't hard-code; ask the model its input name
    x = preprocess_image(image_path, size=size)

    outputs = session.run(None, {input_name: x})  # None = return all outputs
    logits = np.asarray(outputs[0]).reshape(-1)    # flatten (handles (1,1000) and (1,1000,1,1))

    probs = softmax(logits)
    labels = load_labels(labels_path)
    return top_k(probs, labels=labels, k=k)


def selftest():
    """Prove the environment works without needing a downloaded model or image.

    Exercises (a) the numeric helpers and (b) the real ONNX Runtime run path
    using a tiny model that ships inside the onnxruntime package.
    """
    # (a) numeric helpers
    logits = np.array([2.0, 1.0, 0.1], dtype=np.float32)
    p = softmax(logits)
    assert abs(float(p.sum()) - 1.0) < 1e-5, "softmax must sum to 1"
    assert int(np.argmax(p)) == 0, "largest logit must map to largest prob"
    tk = top_k(p, labels=["a", "b", "c"], k=2)
    assert tk[0][0] == "a" and len(tk) == 2, "top_k ordering/length wrong"

    # (b) real ONNX Runtime inference on a bundled tiny model (no network needed).
    # We read each input's declared shape/type from the model itself and build a
    # matching tensor, so the check works regardless of the exact bundled model.
    import os

    ds = os.path.join(os.path.dirname(ort.__file__), "datasets", "logreg_iris.onnx")
    sess = ort.InferenceSession(ds, providers=["CPUExecutionProvider"])

    type_map = {"tensor(float)": np.float32, "tensor(double)": np.float64,
                "tensor(int64)": np.int64, "tensor(int32)": np.int32}
    feed = {}
    for inp in sess.get_inputs():
        # replace symbolic/None dimensions (e.g. dynamic batch) with 1
        shape = [d if isinstance(d, int) and d > 0 else 1 for d in inp.shape]
        dtype = type_map.get(inp.type, np.float32)
        feed[inp.name] = np.ones(shape, dtype=dtype)
    result = sess.run(None, feed)
    print("ONNX Runtime OK — bundled model ran on input shape",
          [list(np.shape(v)) for v in feed.values()])
    print("Numeric helpers OK — softmax/top_k verified.")
    print("\nEnvironment is ready. Download a real image model to classify photos.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="CPU image classification with ONNX Runtime.")
    parser.add_argument("--model", help="Path to an .onnx classification model")
    parser.add_argument("--image", help="Path to an image file to classify")
    parser.add_argument("--labels", help="Optional path to a labels .txt (one per line)")
    parser.add_argument("--size", type=int, default=224, help="Model input size (default 224)")
    parser.add_argument("--topk", type=int, default=5, help="How many predictions to show")
    parser.add_argument("--selftest", action="store_true", help="Verify the environment and exit")
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    if not args.model or not args.image:
        parser.error("--model and --image are required (or use --selftest)")

    results = classify(args.model, args.image, labels_path=args.labels, size=args.size, k=args.topk)
    print(f"\nTop {len(results)} predictions for {args.image}:")
    for rank, (name, prob) in enumerate(results, start=1):
        print(f"  {rank}. {name:<30} {prob * 100:5.2f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
