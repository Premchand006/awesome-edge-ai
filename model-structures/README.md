# Phase 2: Model Structures

You can't optimize what you don't understand. This phase covers the neural-network architectures you'll actually deploy at the edge and *why* some fit a constrained device while others don't.

## What decides if a model fits the edge?
Three numbers, not just accuracy:
- **Parameters** — how much memory the weights need.
- **FLOPs / MACs** — how much compute per inference (affects latency and power).
- **Memory-access pattern** — how much data moves per operation (the real bottleneck on most edge silicon).

A model that is accurate but parameter-heavy (e.g., a large ViT) may be impractical on a 2.5 W NPU, while an efficient CNN runs comfortably.

## Convolutional Neural Networks (CNNs)
The workhorse of edge vision. Convolutions exploit spatial locality and weight sharing, making them efficient and hardware-friendly.
- **ResNet** — the canonical deep CNN; residual connections enable very deep networks.
- Still the backbone of most production detection/segmentation models on the edge.

## Vision Transformers (ViT)
Transformers applied to image patches. Often more accurate at scale, but typically heavier in memory and attention compute — increasingly viable on edge GenAI parts (Hailo-10H, SiMa Modalix) but still demanding.

## Efficient architectures (built for constrained devices)
| Family | Idea | Typical use |
|---|---|---|
| **MobileNet** (v1–v4) | depthwise-separable convolutions | mobile/embedded classification & backbones |
| **EfficientNet** | compound scaling of depth/width/resolution | accuracy-per-FLOP |
| **YOLO** (v5 → v11+) | single-shot real-time object detection | the default edge detector |
| **MobileViT / EdgeNeXt** | hybrid CNN + transformer | efficient ViT-style accuracy |

## Object detection, the edge's killer app
Most edge-vision PoCs are detection. The **YOLO** line (Ultralytics YOLO11, etc.) dominates because it's fast, accurate, and exports cleanly to TensorRT/ONNX/edge NPUs. You'll use it in [sample-projects](../sample-projects/README.md).

## Generative models at the edge (the new frontier)
Small **LLMs/VLMs** now run on-device (e.g., on Hailo-10H, Jetson, RK3588 via rkllm). Efficient transformer variants and aggressive [quantization](../model-optimization/README.md) (INT4) make this possible. This is where edge AI meets [Physical AI](../poc-and-use-cases/README.md).

## How this connects
You'll take one of these architectures, **optimize** it ([Phase 3](../model-optimization/README.md)), run it on a **runtime** ([Phase 4](../runtimes-and-frameworks/README.md)), and wire it into a **pipeline** ([Phase 5](../pipelines/README.md)).

➡️ Next: [model-optimization](../model-optimization/README.md).
