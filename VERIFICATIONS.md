# Verifications ledger

Two kinds of "verified" live in this repo, and they mean different things:

- 🟢 **CI-verified** — a GitHub Actions job installs the pinned dependencies on a clean
  Ubuntu runner and runs the project's offline `--selftest` on every push and weekly.
  This is automatic and proves the code *runs as written on CPU*. Status:
  [![Verified by CI](https://img.shields.io/github/actions/workflow/status/Premchand006/awesome-edge-ai/selftest.yml?label=verified%20by%20CI)](https://github.com/Premchand006/awesome-edge-ai/actions/workflows/selftest.yml)
- 🔵 **Community-verified** — a human ran a project on *real hardware* (Jetson, Pi + Hailo, …)
  and reported the result. These are collected below. CI can't prove on-device behavior,
  so this ledger is how hardware claims earn trust.

## How to add a report

Open a [**Hardware verification report**](https://github.com/Premchand006/awesome-edge-ai/issues/new?template=verification.yml)
issue (or send a PR appending a row here). Include your hardware, OS/driver/JetPack version,
pass/fail, and measured FPS or latency. The maintainer moves accepted reports into the table.

## Community reports

| Project | Hardware | OS / driver / JetPack | Date | Result | FPS / latency | Reporter | Evidence |
|---|---|---|---|---|---|---|---|
| _No community reports yet — [be the first »](https://github.com/Premchand006/awesome-edge-ai/issues/new?template=verification.yml)_ | | | | | | | |

<!--
Row template (copy, fill, keep newest at top):
| [Jetson + YOLO](sample-projects/jetson-yolo-detection.md) | Jetson Orin Nano Super 8GB | JetPack 6.2 | 2026-07-09 | ✅ pass | 62 FPS (yolo11n, 640) | @handle | link to log/screenshot |
-->

## CI-verified projects

| Project | Check | Where |
|---|---|---|
| [Zero-hardware image classification](sample-projects/onnxruntime-image-classification.md) | `python classify.py --selftest` on Python 3.11 & 3.12 | [selftest.yml](.github/workflows/selftest.yml) |
