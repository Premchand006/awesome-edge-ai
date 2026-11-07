# Changelog

All notable changes to this repository are documented here (dates `YYYY-MM-DD`). Follows [Keep a Changelog](https://keepachangelog.com/) loosely.

## [Unreleased]
### Added
- Project website (GitHub Pages, MkDocs Material) with search, sitemap, and per-page titles.
- `CITATION.cff` so the guide can be cited ("Cite this repository").
- Social-preview image.

### Changed
- The **renames-and-deprecations page** is no longer maintained in this repo; it now lives canonically in the flagship [awesome-embedded-ai-stack](https://github.com/Premchand006/awesome-embedded-ai-stack/blob/main/renames-and-deprecations.md) repo and is linked cross-repo. This repo keeps a short quick-reference table only.
- ROS 2 guidance: Lyrical Luth (LTS, May 2026) is now the recommended release; Kilted Kaiju reaches EOL Nov 2026.
- README banner uses a relative path with descriptive alt text; Discussions enabled and linked.
- Link checker: longer timeout and more retries for slow-but-valid hosts (e.g. docs.ros.org).

### Planned
- Add OpenVINO-NPU and RKNN (RK3588) sample projects.
- Expand PoCs with more reference implementations per industry.

## [0.1.0] - 2026-06-03
### Added
- Initial release: an 8-phase beginner-to-advanced edge-AI **roadmap**.
- Phase pages: foundations, model structures, model optimization, runtimes and frameworks, pipelines, and deployment/MLOps.
- **PoCs, real-time use cases, and applications** by industry, each mapped to roadmap phases and starting projects.
- **Verified sample projects:** a zero-hardware ONNX Runtime CPU classifier (with offline self-test and unit-tested helpers), plus Raspberry Pi + Hailo and Jetson + YOLO pipelines.
- Curated, annotated courses/books/docs; a curated awesome list; a renames-and-deprecations page.
- CI (awesome-lint + lychee) and contribution scaffolding with a strict sample-project quality bar.

[Unreleased]: https://github.com/Premchand006/awesome-edge-ai/commits/main
[0.1.0]: https://github.com/Premchand006/awesome-edge-ai/tree/v0.1.0
