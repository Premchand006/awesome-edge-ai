"""MkDocs hooks: render GitHub-flavoured Markdown extras that MkDocs lacks.

- GitHub alerts (> [!TIP], > [!NOTE], ...) become Material admonitions.
- Links to repo files that are not site pages (code, LICENSE, ...) point to GitHub.
- GitHub-style anchors for emoji headings (#-the-roadmap) match MkDocs slugs.
- <div align="center"> blocks are parsed as Markdown.
- Each page gets its own meta description from its first paragraph.
"""
import re

REPO = "https://github.com/Premchand006/awesome-edge-ai/blob/main/"
ALERT = re.compile(r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\n((?:>.*\n?)+)", re.M)
KIND = {"NOTE": "note", "TIP": "tip", "IMPORTANT": "info", "WARNING": "warning", "CAUTION": "danger"}
# Relative links to non-Markdown files in the repo (e.g. classify.py, LICENSE).
FILE_LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+?\.(?:py|txt|yml|yaml|cff)|[^)\s]*LICENSE)\)")
LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")


def on_page_markdown(markdown, page, **_):
    markdown = ALERT.sub(_alert, markdown)

    src = page.file.src_uri
    base = src.rsplit("/", 1)[0] + "/" if "/" in src else ""

    def file_link(m):
        parts = []
        for seg in (base + m.group(1)).split("/"):
            if seg == "..":
                if parts:
                    parts.pop()
            elif seg not in ("", "."):
                parts.append(seg)
        return "](" + REPO + "/".join(parts) + ")"

    markdown = FILE_LINK.sub(file_link, markdown)
    markdown = markdown.replace("](#-", "](#")
    markdown = markdown.replace('<div align="center">', '<div align="center" markdown="1">')

    if "description" not in page.meta:
        desc = first_paragraph(markdown)
        if desc:
            page.meta["description"] = desc
    return markdown


def _alert(m):
    lines = m.group(2).rstrip("\n").split("\n")
    body = "\n".join("    " + re.sub(r"^> ?", "", line) for line in lines)
    return "!!! " + KIND[m.group(1)] + "\n" + body + "\n"


def first_paragraph(markdown, limit=155):
    """Plain text of the first prose paragraph, trimmed to about `limit` chars."""
    in_fence = False
    for block in re.split(r"\n\s*\n", markdown):
        text = block.strip()
        if text.count("```") % 2 == 1:
            in_fence = not in_fence
            continue
        if in_fence or text.startswith("```") or not text or text[0] in "#<|>!" or text.startswith(("- ", "* ", "1. ", "[![")):
            continue
        text = LINK.sub(r"\1", text)
        text = re.sub(r"[*_`]", "", re.sub(r"\s+", " ", text)).strip()
        if len(text) < 60:
            continue
        if len(text) > limit:
            text = text[:limit].rsplit(" ", 1)[0].rstrip(",;:—-") + "…"
        return text
    return None
