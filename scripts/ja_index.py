#!/usr/bin/env python3
"""
Keep the Jātaka (selected verses) index and the chain hand-off in step with a content module.

Identical logic to an_index.py/sn_index.py -- see those files for the full
rationale. Kept as its own file for the same reason ja_build.py is.

Usage:
    python3 scripts/ja_index.py ja_content_01
"""
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ja_build  # noqa: E402

INDEX = os.path.join(ja_build.OUT_DIR, "index.html")

ROW = ('        <li class="sutta-row linked"><a href="{slug}.html">'
       '<span class="sutta-num">{num}</span><span class="sutta-titles">'
       '<span class="pali">{pali}</span> \u00b7 <span class="en">{en}</span></span>'
       '<span class="sutta-status">live</span></a></li>')


def rewrite_block(doc, heading, rows):
    start = doc.index(heading)
    ul_open = doc.index('<ul class="sutta-list">', start)
    ul_close = doc.index("</ul>", ul_open)
    body = '<ul class="sutta-list">\n' + "\n".join(rows) + "\n      "
    return doc[:ul_open] + body + doc[ul_close:]


def main():
    mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1
                                  else "ja_content_01")
    pages = ja_build.chain(mod)
    doc = open(INDEX, encoding="utf-8").read()

    entries = [(p["slug"], p["index_pali"], p["nav_title"]) for p in pages]
    entries += list(getattr(mod, "INDEX_EXTRA", []))
    entries.sort(key=lambda e: [int(n) for n in
                                re.findall(r"\d+", e[0].split("-", 1)[1])][:2])
    rows = [ROW.format(slug=slug,
                       num=slug.replace("ja-", "Ja ").replace("-", "\u2013"),
                       pali=pali, en=en) for slug, pali, en in entries]
    doc = rewrite_block(doc, mod.INDEX_HEADING, rows)

    live = len(re.findall(r'class="sutta-row linked"', doc))
    doc = re.sub(r"<dd>\d+ pages live,", "<dd>%d pages live," % live, doc, count=1)
    open(INDEX, "w", encoding="utf-8").write(doc)
    print("index: %d rows in %s, %d live overall"
          % (len(rows), mod.INDEX_HEADING, live))

    tail_href, _ = mod.TAIL
    if tail_href.endswith(".html"):
        path = os.path.join(ja_build.OUT_DIR, tail_href)
        doc = open(path, encoding="utf-8").read()
        last = pages[-1]
        new = ('<a href="%s.html"><span class="label">&larr; Previous</span>%s'
               " &middot; %s</a>"
               % (last["slug"],
                  last["slug"].replace("ja-", "Ja ").replace("-", "&ndash;"),
                  last["nav_title"]))
        doc2 = re.sub(r'<a href="[^"]*"(?: class="prev")?>'
                      r'<span class="label">(?:&larr; Previous|Collection)</span>[^<]*</a>',
                      lambda m: new, doc, count=1)
        if doc2 != doc:
            open(path, "w", encoding="utf-8").write(doc2)
            print("hand-off: %s previous -> %s" % (tail_href, last["slug"]))
        else:
            print("hand-off: %s already current" % tail_href)


if __name__ == "__main__":
    main()
