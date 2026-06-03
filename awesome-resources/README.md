# Awesome Edge AI Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vendor-neutral list of high-signal resources for learning and shipping edge AI - courses, runtimes, optimization tools, docs, papers, and other awesome lists.

Only authoritative or genuinely useful, currently-maintained resources are listed, with free options prioritized. See the [contribution guide](../CONTRIBUTING.md) for the quality bar, and [courses-and-books](../courses-and-books/README.md) for the annotated, roadmap-mapped version.

## Contents
- [Courses](#courses)
- [Runtimes and frameworks](#runtimes-and-frameworks)
- [Optimization tools](#optimization-tools)
- [Documentation](#documentation)
- [Papers](#papers)
- [Other awesome lists](#other-awesome-lists)
- [Suggested GitHub topics](#suggested-github-topics)

## Courses
- [MIT 6.5940 TinyML and Efficient Deep Learning](https://efficientml.ai) - Free, advanced course on quantization, pruning, NAS, and distillation.
- [Microsoft edgeai-for-beginners](https://github.com/microsoft/edgeai-for-beginners) - Free 8-module MIT-licensed curriculum with 50+ samples.
- [DeepLearning.AI Introduction to On-Device AI](https://www.deeplearning.ai/courses/introduction-to-on-device-ai) - Free short course on conversion, quantization, and NPU deployment.
- [Edge Impulse Edge AI Fundamentals](https://docs.edgeimpulse.com) - Free conceptual foundation with a certificate.
- [Qualcomm Academy AI Upskilling Technical Foundations](https://academy.qualcomm.com/course-catalog/AI-Upskilling-Certificate-Technical-Foundations) - Free technical grounding with a Credly badge.
- [Coursera Edge AI for Microcontrollers](https://www.coursera.org/specializations/edge-ai-mcu) - Hands-on TinyML specialization from Edge Impulse.

## Runtimes and frameworks
- [ONNX Runtime](https://onnxruntime.ai) - Portable inference across CPU, GPU, and NPU via Execution Providers.
- [LiteRT](https://ai.google.dev/edge/litert) - Google's on-device runtime, formerly TensorFlow Lite.
- [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt) - Maximum-performance inference on NVIDIA GPUs and Jetson.
- [Intel OpenVINO](https://docs.openvino.ai) - Inference across Intel CPU, NPU, and GPU.
- [Apache TVM](https://tvm.apache.org) - Compiler stack for deploying models to arbitrary hardware.

## Optimization tools
- [Neural Network Compression Framework (NNCF)](https://github.com/openvinotoolkit/nncf) - Quantization and pruning for OpenVINO targets.
- [ONNX Runtime quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) - Framework-agnostic post-training INT8 quantization.
- [TensorRT Model Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer) - Quantization and sparsity for NVIDIA deployment.

## Documentation
- [ROS 2 documentation](https://docs.ros.org) - The robotics middleware used for perception pipelines.
- [GStreamer documentation](https://gstreamer.freedesktop.org/documentation) - The multimedia framework under most edge-vision stacks.
- [NVIDIA DeepStream](https://developer.nvidia.com/deepstream-sdk) - GStreamer-based multi-stream video analytics SDK.

## Papers
- [OpenVLA (arXiv 2406.09246)](https://arxiv.org/abs/2406.09246) - Open vision-language-action model for robots.
- [Cosmos World Foundation Models (arXiv 2501.03575)](https://arxiv.org/abs/2501.03575) - World models for Physical AI.

## Other awesome lists
- [qijianpeng/awesome-edge-computing](https://github.com/qijianpeng/awesome-edge-computing) - Actively maintained list of frameworks, simulators, and tools.
- [crespum/edge-ai](https://github.com/crespum/edge-ai) - Embedded-AI resources, already reflecting the LiteRT rebrand.
- [alternbits/awesome-cuda-books](https://github.com/alternbits/awesome-cuda-books) - Curated CUDA book list (low maintenance, but canonical titles).

## Suggested GitHub topics
Add these in Settings then Topics so the repo is discoverable:

```
awesome  edge-ai  tinyml  on-device-ai  embedded-ai
quantization  onnx  onnxruntime  tensorrt  openvino
litert  computer-vision  mlops  roadmap  edge-computing
```

---

*Found a great resource or a dead link? [Open a PR](../CONTRIBUTING.md).*
