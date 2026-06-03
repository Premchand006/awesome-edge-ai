# Curated Courses, Books & Docs

Hand-vetted learning resources, mapped to the [roadmap](../roadmap/README.md), with **level**, **cost**, and an honest note on each. Free and authoritative resources are prioritized; paid/supplementary ones are labeled.

## Courses — by roadmap phase
| Resource | Level | Cost | Phase | Note |
|---|---|---|---|---|
| [Edge Impulse — Edge AI Fundamentals](https://docs.edgeimpulse.com/) | Beginner | Free | 0–1 | Concepts + free certificate; the cleanest starting point. |
| [Qualcomm Academy — AI Upskilling, Technical Foundations](https://academy.qualcomm.com/course-catalog/AI-Upskilling-Certificate-Technical-Foundations) | Beginner→Technical | Free | 0 | ~5 h, Credly badge; partly product-oriented. |
| [DeepLearning.AI — Introduction to On-Device AI](https://www.deeplearning.ai/courses/introduction-to-on-device-ai/) | Beginner | Free | 3–4 | ~1–2 h with Qualcomm; conversion, quantization, NPU deployment. |
| [Coursera — Edge AI for Microcontrollers (Edge Impulse)](https://www.coursera.org/specializations/edge-ai-mcu) | Beginner→Intermediate | Subscription / aid | 1 | Hands-on TinyML; strong and practical. |
| [Coursera — Edge AI Fundamentals](https://www.coursera.org/learn/edge-ai-fundamentals) | Beginner | Paid cert (free content on Edge Impulse) | 0 | Same material is free on Edge Impulse docs. |
| [MIT 6.5940 — TinyML & Efficient Deep Learning Computing](https://efficientml.ai/) | Advanced | Free | 3 | **The academic anchor** for optimization (Song Han). Lectures on YouTube. |
| [Microsoft — edgeai-for-beginners](https://github.com/microsoft/edgeai-for-beginners) | Intermediate | Free (MIT) | 3–6 | 8 modules, 50+ samples; Microsoft-ecosystem-centric but comprehensive. |

> **On paid Udemy items** ("Edge AI & TinyML" practice tests; "Mastering GPU Parallel Programming with CUDA"): treat as **supplementary**. The practice tests are exam prep, not core learning. Prefer the free, authoritative options above first.

## Books
### Efficient deep learning / TinyML
- **Course materials for MIT 6.5940** (Song Han) — the closest thing to a modern textbook on quantization, pruning, NAS, and distillation; free.

### CUDA / GPU programming
From the community list [alternbits/awesome-cuda-books](https://github.com/alternbits/awesome-cuda-books) (note: that list has only one commit — low maintenance — but the titles are canonical):
- **Programming Massively Parallel Processors, 3rd ed.** — Kirk & Hwu (the canonical GPU text).
- **CUDA by Example** — Sanders & Kandrot (gentle introduction).
- **The CUDA Handbook** — Nicholas Wilt (reference depth).
- **Professional CUDA C Programming** — Cheng, Grossman & McKercher.
- **Hands-On GPU Programming with Python and CUDA** — Tuomanen.

## Official documentation (cite these, not blog reposts)
- [ONNX Runtime docs](https://onnxruntime.ai/docs/) · [LiteRT docs](https://ai.google.dev/edge/litert) · [TensorRT docs](https://docs.nvidia.com/deeplearning/tensorrt/) · [OpenVINO docs](https://docs.openvino.ai/) · [Apache TVM docs](https://tvm.apache.org/docs/) · [ROS 2 docs](https://docs.ros.org/).

## Canonical papers
- **OpenVLA** — [arXiv 2406.09246](https://arxiv.org/abs/2406.09246) (open vision-language-action model).
- **NVIDIA Cosmos** — [arXiv 2501.03575](https://arxiv.org/abs/2501.03575) (world foundation models).

## Existing awesome lists worth mining
- [qijianpeng/awesome-edge-computing](https://github.com/qijianpeng/awesome-edge-computing) — actively maintained; frameworks, simulators, tools.
- [crespum/edge-ai](https://github.com/crespum/edge-ai) — moderately maintained; already reflects the TFLite→LiteRT rebrand.

➡️ Back to the [roadmap](../roadmap/README.md) or jump to [sample-projects](../sample-projects/README.md).
