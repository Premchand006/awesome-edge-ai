# Project: Zero-Hardware Image Classification (ONNX Runtime, CPU)

> **Level:** absolute beginner · **Hardware:** any laptop/PC (no GPU/NPU) · **Time:** ~15 minutes · **Roadmap:** [Phase 2](../model-structures/README.md) → [Phase 4](../runtimes-and-frameworks/README.md)

The best first edge-AI project: classify images on your **CPU** with **ONNX Runtime**. It runs on any machine, teaches the exact load → preprocess → run → post-process flow every edge model uses, and the *same code* later moves to a Jetson, Pi, or Intel box by changing one line (the Execution Provider).

The full, commented program is in **[`onnxruntime-classify/classify.py`](onnxruntime-classify/classify.py)** and ships with a built-in `--selftest` that verifies your install with no downloads.

## Why start here
- **No special hardware** — removes the biggest beginner blocker.
- **Portable** — ONNX is the universal model format; ONNX Runtime runs it everywhere.
- **Transferable** — swap `CPUExecutionProvider` for `CUDAExecutionProvider`/`TensorrtExecutionProvider` (NVIDIA) or `OpenVINOExecutionProvider` (Intel) and the rest is unchanged.

## Step 1 — Install (one command)
```bash
pip install numpy onnxruntime Pillow
```

## Step 2 — Verify your environment (no model needed)
```bash
python classify.py --selftest
```
Expected output:
```text
ONNX Runtime OK — bundled model ran on input shape [[3, 2]]
Numeric helpers OK — softmax/top_k verified.

Environment is ready. Download a real image model to classify photos.
```
The selftest runs a tiny model bundled inside ONNX Runtime, so a green result proves your install works before you download anything.

## Step 3 — Get a model and labels
Grab a small, standard ImageNet classifier from the [ONNX Model Zoo](https://github.com/onnx/models) (SqueezeNet is only ~5 MB). Model-zoo paths occasionally move — if a link 404s, browse the zoo's vision/classification section.
```bash
# A small, well-known classifier (SqueezeNet 1.1) and the ImageNet labels:
curl -L -o squeezenet1.1-7.onnx \
  https://github.com/onnx/models/raw/main/validated/vision/classification/squeezenet/model/squeezenet1.1-7.onnx
curl -L -o imagenet_classes.txt \
  https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
```

## Step 4 — Classify an image
```bash
python classify.py --model squeezenet1.1-7.onnx --image your_photo.jpg --labels imagenet_classes.txt
```
Example output:
```text
Top 5 predictions for your_photo.jpg:
  1. tabby cat                       62.10%
  2. tiger cat                       18.44%
  3. Egyptian cat                     7.05%
  4. lynx                             2.18%
  5. tabby                            1.30%
```

## How the code works (the four steps)
The same four steps appear in every edge deployment:

```python
# 1. LOAD — CPU runs anywhere; change the provider list to use a GPU/NPU.
session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])

# 2. PRE-PROCESS — resize, scale to 0..1, normalize, HWC->CHW, add batch dim -> (1,3,224,224)
x = preprocess_image(image_path, size=size)

# 3. RUN — ask the model its input name instead of hard-coding it.
outputs = session.run(None, {session.get_inputs()[0].name: x})

# 4. POST-PROCESS — softmax to probabilities, then take the top-k labels.
probs = softmax(np.asarray(outputs[0]).reshape(-1))
print(top_k(probs, labels, k=5))
```
Read the fully-commented version in [`onnxruntime-classify/classify.py`](onnxruntime-classify/classify.py); every line has an explanation.

## Common pitfalls
- **Wrong input size:** some models expect 224, others 227/256. Pass `--size`.
- **Normalization mismatch:** this script uses standard ImageNet mean/std; a model trained differently will give odd results.
- **Output shape:** classifiers may emit `(1, 1000)` or `(1, 1000, 1, 1)` — `reshape(-1)` handles both.

## Take it to the edge (next steps)
1. **Quantize** the model to INT8 ([Phase 3](../model-optimization/README.md)) and compare size/latency.
2. **Switch provider** to TensorRT or OpenVINO ([Phase 4](../runtimes-and-frameworks/README.md)).
3. **Make it real-time** by feeding webcam frames through a [pipeline](../pipelines/README.md).
4. Try the on-device hardware projects: [Raspberry Pi + Hailo](pi5-hailo-live-detection.md) and [Jetson + YOLO](jetson-yolo-detection.md).

➡️ Back to all [sample projects](README.md) or the [PoC & use-cases](../poc-and-use-cases/README.md) page.
