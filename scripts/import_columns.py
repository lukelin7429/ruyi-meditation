#!/usr/bin/env python3
"""
Import columns from Luke's Obsidian vault to the Jekyll _columns collection.

Source: /Users/hayashikisshou/Library/Mobile Documents/iCloud~md~obsidian/Documents/第二個大腦/組織事務/Ru-Yi Meditation Center/Columns/
Target: ./_columns/

Transformations:
- Strip Obsidian wiki links [[term]] -> term and [[term|display]] -> display
- Convert filename to URL slug (lowercase, dashes, no special chars)
- Inject Jekyll-friendly frontmatter (preserve title/author/original_date/source)
- Drop the trailing "**Author:** / **Original publish date:** / **Source:**" block
  (the column layout already shows these)

Idempotent: re-running overwrites existing _columns/*.md.
"""

from __future__ import annotations
import re
import sys
import unicodedata
from pathlib import Path

VAULT_COLUMNS = Path(
    "/Users/hayashikisshou/Library/Mobile Documents/iCloud~md~obsidian/Documents/第二個大腦/組織事務/Ru-Yi Meditation Center/Columns"
)
REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET = REPO_ROOT / "_columns"

WIKI_LINK_PIPED = re.compile(r"\[\[([^\[\]|]+)\|([^\[\]]+)\]\]")
WIKI_LINK_PLAIN = re.compile(r"\[\[([^\[\]|]+)\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TRAILING_META_RE = re.compile(
    r"\n---\s*\n\*\*Author:\*\*.*?(?=\n\n|\Z)", re.DOTALL
)


def slugify(name: str) -> str:
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name


def strip_wiki_links(text: str) -> str:
    # [[english|中文]] -> "english" (keep the article's original English prose,
    # not the bilingual annotation that was added for vault navigation)
    text = WIKI_LINK_PIPED.sub(r"\1", text)
    text = WIKI_LINK_PLAIN.sub(r"\1", text)
    return text


def parse_frontmatter(raw: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return {}, raw
    front_text = m.group(1)
    body = raw[m.end():]
    front = {}
    for line in front_text.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
        elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1].replace('\\"', '"').replace("\\'", "'")
        front[key] = val
    return front, body


def strip_trailing_meta_block(body: str) -> str:
    return TRAILING_META_RE.sub("", body).rstrip() + "\n"


def render_frontmatter(front: dict) -> str:
    lines = ["---"]
    for key in ["title", "author", "original_date", "tags", "source", "slug"]:
        if key not in front or front[key] in (None, "", []):
            continue
        val = front[key]
        if isinstance(val, list):
            inner = ", ".join(val)
            lines.append(f"{key}: [{inner}]")
        else:
            if any(c in str(val) for c in ":#&*!|>%@`"):
                escaped = str(val).replace('"', '\\"')
                lines.append(f'{key}: "{escaped}"')
            else:
                lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def convert(file: Path) -> tuple[str, str]:
    raw = file.read_text(encoding="utf-8")
    front, body = parse_frontmatter(raw)

    if not front.get("title"):
        front["title"] = file.stem.replace(" - ", ": ")
    if not front.get("author"):
        front["author"] = "Luke Lin"

    slug = slugify(file.stem)
    front["slug"] = slug

    body = strip_wiki_links(body)
    body = strip_trailing_meta_block(body)
    body = body.lstrip("\n")

    return slug, render_frontmatter(front) + "\n" + body


def main() -> int:
    if not VAULT_COLUMNS.is_dir():
        print(f"ERROR: vault columns directory not found: {VAULT_COLUMNS}", file=sys.stderr)
        return 1

    TARGET.mkdir(parents=True, exist_ok=True)
    sources = sorted(VAULT_COLUMNS.glob("*.md"))
    if not sources:
        print(f"ERROR: no .md files found in {VAULT_COLUMNS}", file=sys.stderr)
        return 1

    written = 0
    for src in sources:
        slug, content = convert(src)
        dest = TARGET / f"{slug}.md"
        dest.write_text(content, encoding="utf-8")
        written += 1

    print(f"✓ Imported {written} columns from {VAULT_COLUMNS} → {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
