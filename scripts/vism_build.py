#!/usr/bin/env python3
"""
Build Visuddhimagga (The Path of Purification) chapter guide pages.

Unlike every other series this toolchain generates, there is no CC0 English
translation of the Visuddhimagga to pull verbatim text from: the only
complete English translation, Bhikkhu Ñāṇamoli's "The Path of Purification"
(BPS, copyright 1975/1991/2010, all rights reserved), is still under active
copyright and is not available for republication or excerpting here. This
project therefore does NOT reproduce any translated text. Every page is an
original reading guide in Ru-Yi's own words, with key terms and a
self-check quiz -- no "text" panel, no verbatim quotation. Readers who want
the full translated text are pointed to the legitimate free-distribution
PDF and the public-domain Pali original via the "further reading" section
every page carries.

The page shell (head, site header, script boilerplate) is sliced at runtime
out of discourses/samyutta-nikaya/sn-12.1.html, the sole format authority
for the whole site, exactly as an_build.py/sn_build.py do. Because this
series has no text panel, the tab bar and sidebar here render only two tabs
(Reading Guide, Self-Check) instead of the usual three, via an inline
grid-template-columns override -- the shared shell CSS itself is not
touched.

Usage:
    python3 scripts/vism_build.py vism_content_01
"""
import hashlib
import importlib
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "discourses", "..", "visuddhimagga")
OUT_DIR = os.path.normpath(OUT_DIR)
REFERENCE = os.path.join(ROOT, "discourses", "samyutta-nikaya", "sn-12.1.html")

CONTAINER = '<div class="container">'
SCRIPT_MARK = "<script>\n(function() {"


# --------------------------------------------------------------------------- #
# shell
# --------------------------------------------------------------------------- #
def load_shell():
    with open(REFERENCE, encoding="utf-8") as fh:
        ref = fh.read()
    i = ref.index(CONTAINER) + len(CONTAINER)
    j = ref.index(SCRIPT_MARK)
    head, tail = ref[:i], ref[j:]
    assert "<title>" in head and "</html>" in tail
    # REFERENCE lives two directories below the site root
    # (discourses/samyutta-nikaya/...); visuddhimagga/ is only one level
    # down, so every "../../assets/..." in the sliced head must become
    # "../assets/...".
    head = head.replace('href="../../assets/', 'href="../assets/')
    return head, tail


def make_head(head, page):
    head = re.sub(r"<title>.*?</title>",
                  lambda m: "<title>%s</title>" % page["meta_title"],
                  head, count=1, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")(.*?)(">)',
                  lambda m: m.group(1) + page["meta_desc"] + m.group(3),
                  head, count=1, flags=re.S)
    return head


# --------------------------------------------------------------------------- #
# blocks
# --------------------------------------------------------------------------- #
def glance_block(page):
    rows = "\n".join("      <dt>%s</dt><dd>%s</dd>" % (dt, dd)
                     for dt, dd in page["glance"])
    return '  <div class="glance">\n    <dl>\n%s\n    </dl>\n  </div>' % rows


def guide_block(page):
    out = ['  <section data-panel="guide" class="active">',
           "    <h2>Reading guide</h2>"]
    for heading, paras in page["guide"]:
        out.append("\n    <h3>%s</h3>" % heading)
        for p in paras:
            out.append("    <p>\n      %s\n    </p>" % p)
    out.append("  </section>")
    return "\n".join(out)


def terms_block(page):
    items = []
    for word, body in page["terms"]:
        items.append('      <div class="term">\n'
                     '        <span class="pali-word">%s</span> &mdash; %s\n'
                     "      </div>" % (word, body))
    return ('  <section data-panel="guide" class="active">\n'
            "    <h2>Key terms</h2>\n"
            '    <div class="terms">\n%s\n    </div>\n'
            "  </section>" % "\n".join(items))


NUMWORD = {8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve"}


def _shuffled_opts(slug, i, q):
    """Deterministically shuffle a question's four options so the correct
    answer's position isn't always index 0 (as authored) -- otherwise every
    quiz in the series is gameable by always picking the first, or always
    the longest, option. Seeded per (slug, question index, question text)
    so rebuilds are reproducible and don't churn the diff."""
    seed = int(hashlib.sha256(("%s|%d|%s" % (slug, i, q["q"])).encode("utf-8")).hexdigest(), 16)
    perm = list(range(4))
    random.Random(seed).shuffle(perm)
    opts = [q["opts"][j] for j in perm]
    correct = perm.index(q["correct"])
    return opts, correct


def quiz_block(page):
    qs = page["quiz"]
    n = len(qs)
    out = ['  <section data-panel="quiz">',
           "    <h2>Self-check quiz</h2>",
           '    <p style="font-size:15px; color:#6b6b6b; margin-bottom:20px;">'
           "%s questions. Click an answer to see immediate feedback. "
           "No score is recorded &mdash; this is for your own checking.</p>" % NUMWORD.get(n, str(n)),
           "",
           '    <div class="quiz" id="quiz">',
           ""]
    for i, q in enumerate(qs, 1):
        assert len(q["opts"]) == 4, "question %d needs 4 options" % i
        assert 0 <= q["correct"] <= 3, "question %d correct out of range" % i
        shown_opts, shown_correct = _shuffled_opts(page["slug"], i, q)
        opts = "\n".join('        <button class="opt">%s</button>' % o
                         for o in shown_opts)
        out.append('      <div class="q" data-correct="%d">\n'
                   '        <span class="q-num">Question %d of %d</span>\n'
                   '        <div class="q-text">%s</div>\n'
                   "%s\n"
                   '        <div class="expl"><strong>Correct: %s.</strong> %s</div>\n'
                   "      </div>\n"
                   % (shown_correct, i, n, q["q"], opts,
                      "ABCD"[shown_correct], q["expl"]))
    out.append('      <div class="score-bar" id="score-bar">Answered '
               '<strong id="answered-count">0</strong> of %d &middot; Correct '
               '<strong id="correct-count">0</strong></div>' % n)
    out.append("    </div>")
    out.append("  </section>")
    return "\n".join(out)


def marginalia_block(page):
    blocks = []
    for label, items in page["marginalia"]:
        lis = "\n".join("        <li>%s</li>" % it for it in items)
        blocks.append('    <div class="marginalia-block">\n'
                      '      <div class="m-label">%s</div>\n'
                      "      <ul>\n%s\n      </ul>\n"
                      "    </div>" % (label, lis))
    return '  <aside class="pv-marginalia">\n%s\n  </aside>' % "\n".join(blocks)


def footer_block(page):
    res = "\n".join("      <li>%s</li>" % r for r in page["further"])
    prev_href, prev_label = page["prev"]
    next_href, next_label = page["next"]
    prev_class = ' class="prev"' if prev_href == "./" else ""
    prev_lbl = "Collection" if prev_href == "./" else "&larr; Previous"
    next_lbl = "Collection" if next_href == "./" else "Next &rarr;"
    return (
        '  <div class="pv-footer">\n'
        "  <section>\n"
        "    <h2>Further reading</h2>\n"
        '    <ul class="resources">\n%s\n    </ul>\n'
        "  </section>\n\n"
        '  <div class="nav-prev-next">\n'
        '    <a href="%s"%s><span class="label">%s</span>%s</a>\n'
        '    <a href="%s" class="next"><span class="label">%s</span>%s</a>\n'
        "  </div>\n\n"
        "  <footer>\n"
        '    <p>A series at <a href="../">Ru-Yi Meditation Center</a></p>\n'
        '    <p style="margin-top:6px;">Reading guide written for Ru-Yi Meditation Center. '
        "No translated text is reproduced on this page &mdash; see &ldquo;Further "
        "reading&rdquo; for the full translation and the Pali original.</p>\n"
        "  </footer>\n"
        "  </div>\n"
        % (res, prev_href, prev_class, prev_lbl, prev_label,
           next_href, next_lbl, next_label))


# Two tabs, not three -- this series has no text panel. The inline style
# overrides the shared shell's 3-column .tabs/.side-tabs grid without
# touching that shared CSS.
SIDEBAR = """
  <aside class="pv-sidebar">
    <div class="side-tabs" style="grid-template-columns: 1fr;">
      <button class="side-tab tab active" type="button" data-tab="guide" role="tab" aria-selected="true">
        <span class="side-tab-num">01</span>
        <span class="side-tab-label">Reading Guide</span>
      </button>
      <button class="side-tab tab" type="button" data-tab="quiz" role="tab" aria-selected="false">
        <span class="side-tab-num">02</span>
        <span class="side-tab-label">Self-Check</span>
      </button>
    </div>
  </aside>
"""

TABS = """  <div class="tabs" role="tablist" style="grid-template-columns: 1fr 1fr;">
    <button class="tab active" type="button" data-tab="guide" role="tab" aria-selected="true">
      <span class="tab-num">01</span>
      <span class="tab-label">Reading Guide</span>
      <span class="tab-sub">Original commentary &amp; key terms &mdash; no translated text reproduced</span>
    </button>
    <button class="tab" type="button" data-tab="quiz" role="tab" aria-selected="false">
      <span class="tab-num">02</span>
      <span class="tab-label">Self-Check</span>
      <span class="tab-sub">10-question quiz, instant feedback</span>
    </button>
  </div>
"""


def build(page, shell):
    head, tail = shell

    header = (
        '\n  <div class="pv-header">\n\n'
        '  <nav class="crumb">\n'
        '    <a href="../">Ru-Yi Meditation Center</a><span>&rsaquo;</span>'
        '<a href="./">Visuddhimagga</a><span>&rsaquo;</span>%s\n'
        "  </nav>\n\n"
        '  <div class="sutta-number">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="subtitle">%s</p>\n\n'
        "%s\n\n"
        "  <section>\n"
        "    <h2>Why this chapter</h2>\n"
        '    <p class="lede">\n      %s\n    </p>\n'
        "  </section>\n\n"
        "  </div>\n"
        % (page["crumb"], page["number_line"], page["title"],
           page["subtitle"], glance_block(page), page["why"])
    )

    body = "\n".join([
        header,
        SIDEBAR,
        '  <main class="pv-main">',
        TABS,
        guide_block(page),
        "",
        terms_block(page),
        "",
        quiz_block(page),
        "",
        "  </main>",
        "",
        marginalia_block(page),
        "",
        footer_block(page),
        "",
        "</div>",
        "",
    ])

    return make_head(head, page) + body + tail


def chain(mod):
    pages = mod.PAGES
    head = getattr(mod, "HEAD", ("./", "Visuddhimagga guide"))
    tail = getattr(mod, "TAIL", ("./", "Visuddhimagga guide"))
    for i, page in enumerate(pages):
        label = lambda p: p["nav_title"]
        page.setdefault("prev", head if i == 0 else
                        (pages[i - 1]["slug"] + ".html", label(pages[i - 1])))
        page.setdefault("next", tail if i == len(pages) - 1 else
                        (pages[i + 1]["slug"] + ".html", label(pages[i + 1])))
    return pages


def main():
    module = sys.argv[1] if len(sys.argv) > 1 else "vism_content_01"
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    pages = chain(importlib.import_module(module))
    shell = load_shell()
    for page in pages:
        out = os.path.join(OUT_DIR, page["slug"] + ".html")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(build(page, shell))
        print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
