#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit how completely each text's Chinese source is aligned beside its English.

For every text directory under sutras/, abhidharma/ and anthology/ this script
pulls the Chinese out of the pages' `class="source"` blocks, fingerprints it
against the CBETA canon in the Obsidian vault to identify which Taisho text it
came from, and reports what fraction of that text is actually on the site.

    python3 scripts/align_audit.py                 # full report
    python3 scripts/align_audit.py --below 88      # only texts under 88%
    python3 scripts/align_audit.py --json out.json

Two traps this script exists to avoid, both of which produced wrong answers
when the same question was asked by hand:

  1. A naive regex for `class="source"` that stops at the first `</` captures
     only the block's label ("Chinese Source") and reports zero Chinese on a
     page that is fully aligned. The extractor here walks the element properly.

  2. An HTML parser that increments nesting depth on void tags (<br>, <img>)
     never closes the block, and silently drops every page whose source block
     contains a line break. VOID below is the fix.

Coverage is a ratio against the WHOLE canonical file, so a text that is one
chapter of a larger work (Samantabhadra's Vows inside the forty-fascicle
Avatamsaka, the Gandavyuha inside the sixty-fascicle one) reports a low figure
that is an artifact of the denominator, not a gap. Those are flagged PARTIAL-OF
rather than counted as missing.
"""
import os, re, io, sys, json, argparse, collections
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT = os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/第二大腦/知識庫/佛法")
SCAN = ("sutras", "abhidharma", "anthology")
CJK = re.compile(r"[一-鿿]")
VOID = {"br", "img", "meta", "link", "input", "hr", "wbr", "source",
        "area", "base", "col", "embed", "track", "param"}

# Texts that are a chapter or book of a larger canonical file: comparing their
# length against the whole file is meaningless, so we say so instead.
PARTIAL_OF = {
    "sutras/samantabhadra-vows": "fascicle 40 of the forty-fascicle Avatamsaka",
    "sutras/gandavyuha": "the final book of the Avatamsaka",
    "sutras/pure-conduct-chapter": "one chapter of the Avatamsaka",
}


class SrcExtract(HTMLParser):
    """Collect the text inside every element whose class list contains `source`."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.buf = []
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:                      # never changes nesting depth
            if self.depth:
                self.buf.append("\n")
            return
        if self.depth:
            self.depth += 1
        elif "source" in (dict(attrs).get("class", "") or "").split():
            self.depth = 1
            self.buf = []

    def handle_startendtag(self, tag, attrs):
        if self.depth:
            self.buf.append("\n")

    def handle_endtag(self, tag):
        if tag in VOID or not self.depth:
            return
        self.depth -= 1
        if self.depth == 0:
            self.out.append("".join(self.buf))

    def handle_data(self, data):
        if self.depth:
            self.buf.append(data)


def page_chinese(html):
    html = re.sub(r"<(script|style).*?</\1>", "", html, flags=re.S)
    e = SrcExtract()
    try:
        e.feed(html)
        e.close()
    except Exception:
        pass
    return "".join(CJK.findall("".join(e.out)))


def load_canon():
    canon = {}
    if not os.path.isdir(VAULT):
        sys.exit("Canon not found at %s — is the Obsidian vault mounted?" % VAULT)
    for root, _, files in os.walk(VAULT):
        for f in files:
            m = re.match(r"([TX]\d{4})_", f)
            if not m or not f.endswith(".md"):
                continue
            h = io.open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()
            body = h[h.find("\n---", 4) + 4:]
            body = re.sub(r"^\s*>.*$", "", body, flags=re.M)   # CBETA apparatus
            body = re.sub(r"^#.*$", "", body, flags=re.M)      # headings
            canon[m.group(1)] = ("".join(CJK.findall(body)), f[:-3])
    return canon


def collect_site():
    site = collections.defaultdict(list)
    for root, _, files in os.walk(ROOT):
        rel = os.path.relpath(root, ROOT)
        if rel.startswith(("_site", ".git")):
            continue
        parts = rel.split(os.sep)
        if not parts or parts[0] not in SCAN:
            continue
        key = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
        for f in files:
            if not f.endswith(".html") or f == "index.html":
                continue
            h = io.open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()
            cn = page_chinese(h)
            if cn:
                site[key].append(cn)
    return site


def identify(chunks, canon):
    """Fingerprint the longest passages against the canon; majority vote wins."""
    votes = collections.Counter()
    for probe in [c[10:50] for c in sorted(chunks, key=len, reverse=True)[:3] if len(c) > 60]:
        for tid, (text, _) in canon.items():
            if probe in text:
                votes[tid] += 1
    return votes.most_common(1)[0][0] if votes else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--below", type=float, default=None,
                    help="only show texts under this coverage percentage")
    ap.add_argument("--json", metavar="PATH", help="also write the report as JSON")
    args = ap.parse_args()

    canon = load_canon()
    sys.stderr.write("canon: %d texts loaded\n" % len(canon))
    site = collect_site()

    rows = []
    for key, chunks in sorted(site.items()):
        total = sum(len(c) for c in chunks)
        if total < 2000:
            continue
        tid = identify(chunks, canon)
        row = {"text": key, "chars": total, "pages": len(chunks),
               "taisho": tid, "canon_chars": 0, "canon_name": None,
               "coverage": None, "note": PARTIAL_OF.get(key)}
        if tid:
            row["canon_chars"] = len(canon[tid][0])
            row["canon_name"] = canon[tid][1]
            row["coverage"] = round(total / row["canon_chars"] * 100, 1)
        rows.append(row)

    rows.sort(key=lambda r: (r["coverage"] is None, r["coverage"] or 0))

    print("%-38s %10s %6s %8s  %s" % ("text", "chars", "pages", "coverage", "canonical source"))
    print("-" * 104)
    gaps = 0
    for r in rows:
        if args.below is not None and (r["coverage"] is None or r["coverage"] >= args.below):
            continue
        if r["coverage"] is None:
            cov = "     ?"
        elif r["note"]:
            cov = "  n/a "
        else:
            cov = "%5.0f%%" % r["coverage"]
            if r["coverage"] < 88:
                gaps += 1
        src = ("%s %s" % (r["taisho"], (r["canon_name"] or "")[6:34])) if r["taisho"] else "unmatched"
        print("%-38s %10s %6d %8s  %s%s" % (
            r["text"], "{:,}".format(r["chars"]), r["pages"], cov, src,
            ("  [%s]" % r["note"]) if r["note"] else ""))

    print("-" * 104)
    print("%d texts matched, %d below 88%% coverage (chapter-of-a-larger-work excluded)"
          % (len([r for r in rows if r["coverage"] is not None]), gaps))

    if args.json:
        json.dump(rows, io.open(args.json, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("wrote %s" % args.json)


if __name__ == "__main__":
    main()
