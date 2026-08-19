#!/usr/bin/env python3
"""
Structural acceptance check for Visuddhimagga chapter guide pages.

Checks, per page:
  * both tab panels are present (guide x2 -- reading guide + terms -- and quiz)
  * the sidebar and the mobile tab bar both offer exactly these two tabs
  * quiz question count == the number printed in .score-bar == the "N of N" labels
  * every .q has exactly 4 .opt and a data-correct in 0..3
  * five .term entries, four .marginalia-block entries
  * every internal link resolves to a file that exists
  * NO text-block exists at all (this series carries no translated text)
  * the "further reading" section links to the legitimate free PDF and/or
    the Pali original, since every page must point readers to real text
    somewhere, having none of its own

Usage:
    python3 scripts/vism_verify.py vism_content_01
"""
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vism_build  # noqa: E402

ROOT = vism_build.ROOT
OUT_DIR = vism_build.OUT_DIR

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
    check(panels.count("quiz") == 1, "%s: expected 1 quiz panel, got %d"
          % (slug, panels.count("quiz")))
    check("text" not in panels, "%s: unexpected text panel present" % slug)
    tabs = re.findall(r'data-tab="(\w+)"', doc)
    check(sorted(tabs) == sorted(["guide", "quiz"] * 2),
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
    check('<div class="text-block">' not in doc,
          "%s: unexpected text-block found -- this series must carry no "
          "translated text" % slug)
    check("A series at <a href=\"../\">Ru-Yi Meditation Center</a>" in doc,
          "%s: footer line 1 changed" % slug)
    check("No translated text is reproduced on this page" in doc,
          "%s: footer's no-text-reproduced disclosure missing" % slug)

    # Every page must point somewhere real for the actual text, since it has
    # none of its own.
    check("accesstoinsight.org" in doc or "pathofpurification" in doc.lower()
          or "suttacentral.net" in doc,
          "%s: further reading does not link to a real source for the full "
          "text (free PDF or Pali original)" % slug)

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


def main():
    module = sys.argv[1] if len(sys.argv) > 1 else "vism_content_01"
    pages = vism_build.chain(importlib.import_module(module))
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
