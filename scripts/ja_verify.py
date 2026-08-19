#!/usr/bin/env python3
"""
Structural + textual acceptance check for Jātaka (selected verses) study pages.

Identical checks to an_verify.py/sn_verify.py -- see those files for the
full list. Kept as its own file for the same reason ja_build.py is.

Usage:
    python3 scripts/ja_verify.py ja_content_01
"""
import html
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ja_build  # noqa: E402

ROOT = ja_build.ROOT
OUT_DIR = ja_build.OUT_DIR

failures = []
checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        failures.append(msg)


def verify(page):
    slug = page["slug"]
    path = os.path.join(OUT_DIR, slug + ".html")
    check(os.path.exists(path), "%s: file missing" % slug)
    if not os.path.exists(path):
        return
    doc = open(path, encoding="utf-8").read()

    panels = re.findall(r'data-panel="(\w+)"', doc)
    check(panels.count("guide") == 2, "%s: expected 2 guide panels, got %d"
          % (slug, panels.count("guide")))
    for name in ("text", "quiz"):
        check(panels.count(name) == 1,
              "%s: expected 1 %s panel, got %d" % (slug, name, panels.count(name)))
    tabs = re.findall(r'data-tab="(\w+)"', doc)
    check(sorted(tabs) == sorted(["guide", "text", "quiz"] * 2),
          "%s: tab buttons wrong: %s" % (slug, tabs))

    qs = re.findall(r'<div class="q" data-correct="(\d+)">(.*?)\n      </div>',
                    doc, re.S)
    n = len(qs)
    check(n == len(page["quiz"]),
          "%s: %d questions rendered, %d in source" % (slug, n, len(page["quiz"])))
    for i, (correct, body) in enumerate(qs, 1):
        check(0 <= int(correct) <= 3,
              "%s q%d: data-correct=%s out of range" % (slug, i, correct))
        opts = body.count('<button class="opt">')
        check(opts == 4, "%s q%d: %d options" % (slug, i, opts))
        check('class="expl"' in body, "%s q%d: no explanation" % (slug, i))
        check("Question %d of %d" % (i, n) in body,
              "%s q%d: wrong question label" % (slug, i))
    bar = re.search(r'Answered <strong id="answered-count">0</strong> of (\d+)', doc)
    check(bar and int(bar.group(1)) == n,
          "%s: score-bar says %s, quiz has %d"
          % (slug, bar.group(1) if bar else "?", n))

    check(doc.count('<div class="term">') == 5,
          "%s: %d key terms, expected 5" % (slug, doc.count('<div class="term">')))
    check(doc.count('<div class="marginalia-block">') == 4,
          "%s: %d marginalia blocks, expected 4"
          % (slug, doc.count('<div class="marginalia-block">')))
    check(doc.count('<div class="ending-mark">') == 1, "%s: no ending mark" % slug)
    check("A series at <a href=\"../../\">Ru-Yi Meditation Center</a>" in doc,
          "%s: footer line 1 changed" % slug)
    check("English translation &copy; Bhikkhu Sujato, released CC0." in doc,
          "%s: footer line 2 changed" % slug)
    check("Translation: Bhikkhu Sujato (CC0, SuttaCentral)." in doc,
          "%s: text-intro attribution missing" % slug)

    for href in re.findall(r'href="([^"]+)"', doc):
        if href.startswith(("http://", "https://", "#", "mailto:")):
            continue
        base = href.split("#")[0]
        if not base:
            continue
        target = (os.path.join(ROOT, base.lstrip("/")) if base.startswith("/")
                  else os.path.normpath(os.path.join(OUT_DIR, base)))
        if base.endswith("/"):
            ok = (os.path.isfile(os.path.join(target, "index.html"))
                  or os.path.isfile(target.rstrip("/") + ".html"))
        else:
            ok = os.path.exists(target)
        check(ok, "%s: dead link %s" % (slug, href))

    src = ja_build.load_source(page["source"])
    expected = [ja_build.joined(src, ja_build.segments(src, spec))
                for kind, _, spec in
                [i for i in page["text"] if i[0] == "p"]]
    block = re.search(r'<div class="text-block">(.*?)</div>\s*</section>', doc, re.S)
    check(bool(block), "%s: no text-block" % slug)
    if block:
        got = re.findall(r"<p>(.*?)</p>", block.group(1), re.S)
        got = [re.sub(r'<span class="segno">.*?</span>', "", g) for g in got]
        got = [html.unescape(re.sub(r"<[^>]+>", "", g)) for g in got]
        check(len(got) == len(expected),
              "%s: %d text paragraphs, expected %d" % (slug, len(got), len(expected)))
        for i, (a, b) in enumerate(zip(got, expected), 1):
            check(a == b, "%s: paragraph %d does not match bilara-data\n"
                          "   got: %r\n   exp: %r" % (slug, i, a[:120], b[:120]))
        heads = [(k, v.strip()) for k, v in src.items()
                 if ja_build.is_structural(k, v) and v.strip()]
        for i, para in enumerate(got, 1):
            for key, head in heads:
                if not para.startswith(head):
                    continue
                rest = para[len(head):].lstrip()
                leaked = not rest or rest[0] in "\u201c\u2018\"'" or rest[0].isupper()
                check(not leaked,
                      "%s: paragraph %d opens with heading %s (%r)"
                      % (slug, i, key, head[:60]))


def main():
    module = sys.argv[1] if len(sys.argv) > 1 else "ja_content_01"
    pages = ja_build.chain(importlib.import_module(module))
    for page in pages:
        verify(page)
    print("%d checks over %d pages" % (checks, len(pages)))
    if failures:
        print("\nFAILURES (%d):" % len(failures))
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("all clear")


if __name__ == "__main__":
    main()
