# Phase 4: Inference Runtimes & Frameworks

A runtime takes your optimized model and executes it efficiently on a specific target — CPU, GPU, NPU, or MCU. Picking the right one is mostly about **what hardware you're deploying to**.

## Selection matrix
| Runtime | Best for | Hardware | Notes |
|---|---|---|---|
| **ONNX Runtime** | portability across many targets | CPU, GPU, NPU (via EPs) | start here if unsure; one model, many backends |
| **LiteRT** (was TF Lite) | mobile & embedded; MCUs | Arm CPU, GPU, NPU, MCU | renamed from TensorFlow Lite (Sept 2024); `.tflite` unchanged |
| **TensorRT** | maximum NVIDIA performance | NVIDIA GPU / Jetson | compiles an optimized engine per GPU |
| **OpenVINO** | Intel CPU/iGPU/NPU/Arc | Intel | great on x86 edge and AI PCs |
| **Apache TVM** | custom/niche hardware; research | many | compiler approach; powers some vendor SDKs |
| **RKNN (rknn-toolkit2)** | Rockchip RK3588 NPU | Rockchip | converts ONNX → `.rknn` for the on-SoC NPU |

## ONNX Runtime — the portable default
**[ONNX Runtime](https://onnxruntime.ai/)** runs models in the open **ONNX** format and dispatches work to **Execution Providers (EPs)**: CPU (default), CUDA/TensorRT (NVIDIA), OpenVINO (Intel), QNN (Qualcomm), and more. Train in any framework → export to ONNX → run almost anywhere. This is why the flagship [sample project](../sample-projects/README.md) uses it: it runs on *any* machine with no special hardware.

> ⚠️ The **ArmNN Execution Provider was removed in ONNX Runtime 1.26** — use the CPU EP (with KleidiAI on Arm) or QNN for Qualcomm. See [renames-and-deprecations.md](../renames-and-deprecations.md).

## LiteRT — mobile, embedded, and microcontrollers
**[LiteRT](https://ai.google.dev/edge/litert)** (formerly TensorFlow Lite) is Google's on-device runtime. **LiteRT for Microcontrollers** runs in kilobytes on Cortex-M and similar — the TinyML target from [Phase 1](../foundations/README.md). The rebrand did not change the `.tflite` format.

## TensorRT — NVIDIA performance
**[TensorRT](https://developer.nvidia.com/tensorrt)** compiles a model into a hardware-specific engine (layer fusion, precision calibration, kernel autotuning). On Jetson it's the path to maximum FPS. Engines are GPU-specific — build on the target. Pairs with **DeepStream** for video ([pipelines](../pipelines/README.md)).

## OpenVINO — Intel everywhere
**[OpenVINO](https://docs.openvino.ai)** accelerates inference across Intel CPU, integrated GPU, the Core Ultra **NPU**, and Arc GPUs, with an `AUTO` device that picks the best target. **OpenVINO GenAI** handles on-device LLMs/VLMs. (Note the removed Model Optimizer / Open Model Zoo — use **OVC** and `optimum-intel`.)

## Apache TVM & RKNN — specialized targets
- **[Apache TVM](https://tvm.apache.org/)** is a compiler stack that optimizes models for arbitrary hardware; it underpins some vendor SDKs (e.g., Axelera Voyager).
- **RKNN** converts ONNX models to run on the **Rockchip RK3588** NPU (popular, affordable 6 TOPS SBCs).

## How to choose, in one line
> **Deploying to NVIDIA?** TensorRT. **Intel?** OpenVINO. **A phone/MCU?** LiteRT. **Rockchip?** RKNN. **Not sure / many targets?** ONNX Runtime.

➡️ Next: feed real data through your model with [pipelines](../pipelines/README.md).
