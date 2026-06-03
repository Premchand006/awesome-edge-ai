# Phase 0–1: Foundations & Embedded Basics

Before you optimize or deploy anything, you need three things: comfort on Linux, enough programming to read real samples, and a working mental model of neural networks. Then you meet the device.

## Linux & tooling
You will spend most of your time on a headless Linux board over SSH. Get fluent with:
- The shell (navigation, pipes, `grep`), package managers (`apt`, `pip`), and file permissions.
- `systemd` services (to autostart an inference app), and the **serial console** (`screen`, `minicom`) for boards with no display.
- Checking hardware: `v4l2-ctl --list-devices` (cameras), `lsusb`/`lspci` (accelerators).

## Programming: Python + a little C/C++
- **Python** is the glue for most ML workflows and is enough for ONNX Runtime, LiteRT, and Ultralytics.
- **C/C++** matters because the highest-performance samples (DeepStream, TensorRT, LiteRT for Microcontrollers) are written in it. You need to *read* it even if you write Python.

## ML basics (the minimum)
- **Tensors** and the shape of data flowing through a network.
- **CNNs vs transformers**; **classification vs object detection vs segmentation**.
- **Training vs inference** — at the edge you almost always do *inference* on a model trained elsewhere.
- **Precision**: FP32 → FP16 → INT8 → INT4, and why lower precision is faster and smaller (covered in [model-optimization](../model-optimization/README.md)).

## Meet the device (Phase 1)
| Class | Examples | When to use |
|---|---|---|
| **Linux SoC** | Jetson, Raspberry Pi 5, RK3588 boards | vision, robotics, multiple models |
| **Microcontroller (MCU)** | ESP32, Arm Cortex-M | always-on sensors, milliwatts, TinyML |
| **Discrete NPU** | Hailo, MemryX (M.2) | add acceleration to an existing host |

Key embedded concepts: cross-compilation, flashing an OS image, CSI vs USB cameras, and I²C/SPI sensors.

## TinyML (your first embedded model)
On a microcontroller you run **LiteRT for Microcontrollers** (formerly TensorFlow Lite Micro) — kilobytes of memory, often battery-powered. Classic first projects: keyword spotting and gesture recognition. The smoothest on-ramp is **Edge Impulse** (data collection → training → deployment), paired with the **DeepLearning.AI / Qualcomm** and **Edge Impulse** courses in [courses-and-books](../courses-and-books/README.md).

## Recommended starting resources
- **Edge Impulse "Edge AI Fundamentals"** (free) — conceptual foundation.
- **Qualcomm Academy "AI Upskilling — Technical Foundations"** (free) — technical grounding.
- **DeepLearning.AI "Introduction to On-Device AI"** (free, ~1–2 h) — conversion + quantization + deployment.

➡️ Next: [model-structures](../model-structures/README.md), then your first [sample project](../sample-projects/README.md).
