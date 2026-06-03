# Renames & Deprecations (2024–2026)

Edge AI moves fast, and tutorials rot. This page is the cheat-sheet of what was renamed, deprecated, or abandoned recently, so you don't waste a weekend on dead tooling. Verify against the linked source before relying on any single line.

## Renamed (same thing, new name)
- **TensorFlow Lite → LiteRT** (Google, Sept 4, 2024). The `.tflite` format is unchanged; `tf.lite` was decoupled into a standalone LiteRT repo (TF 2.20, Aug 2025). See [runtimes-and-frameworks](runtimes-and-frameworks/README.md).
- **TensorFlow Lite Micro → LiteRT for Microcontrollers** — the TinyML runtime from [foundations](foundations/README.md).

## Deprecated within an active product
- **OpenVINO:** the legacy **Model Optimizer**, the **`openvino-dev`** package, and the **Open Model Zoo** are removed. Use **OVC** + `optimum-intel`; for compression use `nncf.quantize()` (the old `create_compressed_model()` is deprecated). See [model-optimization](model-optimization/README.md).
- **ONNX Runtime:** the **ArmNN Execution Provider** was removed in **1.26** — use the CPU EP (with KleidiAI on Arm) or QNN for Qualcomm.

## Discontinued / abandoned
- **Google Coral / Edge TPU — effectively abandoned** (community consensus, not an official Google EOL). No updates 2021–2025; the Gasket PCIe driver won't build on Linux ≥ 6.4; `google/gasket-driver` was archived April 2026. Prefer **Hailo**, **MemryX**, or an **RK3588** NPU instead.
- **Raspberry Pi AI Kit — out of production.** Replaced by the **AI HAT+** (Hailo-8/8L) and the **AI HAT+ 2** (Hailo-10H, 40 TOPS INT4, GenAI on Pi 5; Jan 15, 2026, $130).

## ROS 2 release status (pick an LTS for production)
- Current release **Kilted Kaiju** (May 23, 2025) is **non-LTS** (EOL Nov 2026).
- **Lyrical Luth** is the scheduled next **LTS** (~May 2026, 5-year support); ship status as of mid-2026 is ambiguous.
- Most recent shipped **LTS** is **Jazzy Jalisco** (May 2024, EOL 2029). See [pipelines](pipelines/README.md).

## Industry context (affects which tutorials/specs are current)
- **Groq → "NVIDIA Groq"** — LPU architecture licensed and team acqui-hired by NVIDIA (Dec 2025; framing contested).
- **Blaize** is now public (NASDAQ: BZAI, Jan 2025).

## Quick "if a tutorial says X, do Y"
| Tutorial says… | Do instead |
|---|---|
| `import tensorflow.lite` for deployment | use **LiteRT** (`.tflite` still works) |
| "install the Coral Edge TPU" | use **Hailo / MemryX / RK3588** |
| "Raspberry Pi AI Kit" | **AI HAT+ / AI HAT+ 2** |
| "OpenVINO Model Optimizer (`mo`)" | **OVC** + `optimum-intel` |
| "NNCF `create_compressed_model()`" | `nncf.quantize()` |
| "ONNX Runtime ArmNN EP" | CPU EP (KleidiAI) or QNN |

*Spot something stale? [Open a PR](CONTRIBUTING.md) — keeping this current is one of the most valuable contributions here.*
