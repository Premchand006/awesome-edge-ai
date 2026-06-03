# Sample Projects

Hands-on, **verified, easy-to-run** projects ordered by difficulty. Start with the zero-hardware classifier (it runs on any laptop), then move to real-time on-device vision. Every project lists its hardware, level, and the [roadmap](../roadmap/README.md) phases it exercises.

## Project index
| Project | Level | Hardware | What you build | Roadmap |
|---|---|---|---|---|
| [Zero-hardware image classification](onnxruntime-image-classification.md) | Beginner | Any laptop/PC | CPU image classifier with ONNX Runtime (+ self-test) | 2 → 4 |
| [Raspberry Pi + Hailo live detection](pi5-hailo-live-detection.md) | Beginner→Intermediate | Pi 5 + Hailo AI HAT | real-time object detection pipeline | 2 → 4 → 5 |
| [Jetson + YOLO detection](jetson-yolo-detection.md) | Intermediate | NVIDIA Jetson | high-FPS detection via TensorRT | 3 → 4 → 5 |

## Our bar for "verified and easy"
- **Runs as written** — the flagship project ships with a `--selftest` that checks your environment offline; its helper functions are unit-tested.
- **Copy-paste setup** — one `pip install` line, exact model-download commands, expected output shown.
- **Heavily commented** — the code explains *why*, not just *what*, so you learn the pattern, not just the recipe.
- **Portable** — the same flow (load → preprocess → run → post-process) carries across CPU, GPU, and NPU by changing the runtime/Execution Provider.

## Recommended order
1. **[Zero-hardware classifier](onnxruntime-image-classification.md)** — learn the inference flow with no hardware to buy or configure.
2. **[Raspberry Pi + Hailo](pi5-hailo-live-detection.md)** — your first *real-time, on-device* pipeline on affordable hardware.
3. **[Jetson + YOLO](jetson-yolo-detection.md)** — squeeze maximum throughput with TensorRT and scale to multiple streams.

From here, turn a project into a product with [deployment & MLOps](../deployment-and-mlops/README.md), or browse industry [PoCs & use cases](../poc-and-use-cases/README.md).

> **Contributing a project?** Keep the bar: runnable as written, one-command install, commented code, and a clear hardware/level header. See [CONTRIBUTING.md](../CONTRIBUTING.md).
