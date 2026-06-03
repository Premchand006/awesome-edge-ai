# Contributing to awesome-edge-ai

Thanks for helping build the clearest learning path in edge AI. This guide covers **what we accept** and the **quality bar** — especially for sample projects, where "it runs as written" is non-negotiable.

## What this repo is
A structured **roadmap** (beginner → advanced) plus **verified sample projects**, **PoCs and real-time use cases**, and a **curated resource list**. It teaches the *pattern* of edge AI, not just recipes.

## Great contributions
- 🧪 **A new sample project** that runs as written (see the project bar below).
- 🛠️ **Fixes/improvements** to an existing project (clearer comments, a bug, a faster path).
- 🗺️ **Roadmap or explainer improvements** (a clearer analogy, a missing step).
- 📚 **A high-signal resource** (course, doc, paper, tool) with level/cost noted.
- 🔁 **A rename/deprecation update** (this field rots fast — see [renames-and-deprecations.md](renames-and-deprecations.md)).

## Quality bar for resources
1. **Authoritative or genuinely useful**, and currently maintained. Prefer official docs/papers over blog reposts.
2. **Annotate** level and cost; mark paid/supplementary clearly. Free, high-quality resources come first.
3. **List items:** `- [Name](url) - Capitalized description.` — regular hyphen separator, no trailing slash in URLs.

<a id="quick-win-template"></a>
## Quality bar for sample projects (strict)
A project is only merged if it:
1. **Runs exactly as written** on the stated hardware — no missing steps.
2. Has a **one-line/one-block install** and **exact commands** to fetch any model/data.
3. Includes **expected output** so a learner knows it worked.
4. Is **heavily commented** — explain *why*, not just *what*.
5. Has a header stating **level, hardware, time, and roadmap phases**.
6. Where possible, ships a **self-test** or trivially verifiable step (the ONNX Runtime project is the reference example).

Use this as the template for the project's header and structure; mirror [`sample-projects/onnxruntime-image-classification.md`](sample-projects/onnxruntime-image-classification.md).

## Submit
1. Fork, branch (`add/<short-name>`), keep the PR focused.
2. Run checks locally if you can:
   ```bash
   npx awesome-lint awesome-resources/README.md
   python -m py_compile sample-projects/**/**.py   # if you added code
   lychee --offline . || lychee .
   ```
3. Use a [Conventional Commits](https://www.conventionalcommits.org/) message, e.g. `feat: add OpenVINO NPU classification project`.
4. Open a PR; CI runs `awesome-lint` and a link checker.

## License of contributions
Prose: **CC BY 4.0**; code: **MIT**. By contributing you agree to these terms. See [LICENSE](LICENSE) and the [Code of Conduct](CODE_OF_CONDUCT.md).
