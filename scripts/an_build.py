#!/usr/bin/env python3
"""
Build Aṅguttara Nikāya study pages.

The page shell (head, site header, tab/quiz script) is sliced at runtime out of
discourses/anguttara-nikaya/an-3.65.html, which is the sole format authority.
Everything between the shell halves is assembled here from a per-page dict.

Discourse text is never typed by hand: paragraphs name segment keys and the
text is pulled straight from bilara-data (Bhikkhu Sujato, CC0).

Usage:
    python3 scripts/an_build.py an_content_01
"""
import importlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "discourses", "anguttara-nikaya")
REFERENCE = os.path.join(OUT_DIR, "an-3.65.html")
BILARA = os.path.expanduser("~/Documents/Claude/repos/bilara-data")
TRANS = os.path.join(BILARA, "translation/en/sujato/sutta/an")

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
# source text
# --------------------------------------------------------------------------- #
def load_source(rel):
    """rel is like 'an1/an1.1-10'."""
    nipata = rel.split("/")[0]
    name = rel.split("/")[1]
    path = os.path.join(TRANS, nipata, name + "_translation-en-sujato.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def is_structural(key, value):
    """Headings are navigation furniture, not discourse text.

    In bilara-data a segment whose sub-key ends in `.0` is a heading: `0.x` is
    the file heading, and `N.0` is the label of a division within it — a bare
    number in the Ones, a numbered title from the Twos on. Across the whole of
    AN no such segment runs longer than a dozen words. The segno carries the
    number, and the guide supplies its own section headings."""
    sub = key.split(":")[1]
    return sub.startswith("0.") or sub.endswith(".0")


def heading(src, uid):
    """The heading the source gives a discourse, minus its leading number."""
    for key, value in src.items():
        if key.split(":")[0] == uid and key.split(":")[1] == "1.0":
            return re.sub(r"^[\d–-]+\.\s*", "", value.strip())
    return ""


def segments(src, spec):
    """Which source segments a text paragraph is made of.

    spec may be a uid ('an1.1') for the whole discourse, a sub-key range
    within one ('an3.1:1.1-2.3', inclusive, in document order), or an
    explicit list of segment keys. Headings are skipped either way.
    """
    if isinstance(spec, str) and ":" in spec:
        uid, span = spec.split(":", 1)
        first, last = span.split("-", 1)
        order = [k for k in src if k.split(":")[0] == uid]
        try:
            lo = order.index("%s:%s" % (uid, first))
            hi = order.index("%s:%s" % (uid, last))
        except ValueError:
            raise KeyError("no such range %s" % spec)
        keys = [k for k in order[lo:hi + 1] if not is_structural(k, src[k])]
        if not keys:
            raise KeyError("range %s is all headings" % spec)
        return keys
    if isinstance(spec, str):
        keys = [k for k in src if k.split(":")[0] == spec
                and not is_structural(k, src[k])]
        if not keys:
            raise KeyError("no segments for %s" % spec)
        return keys
    for k in spec:
        if k not in src:
            raise KeyError(k)
    return list(spec)


ENTITIES = [
    ("&", "&amp;"), ("<", "&lt;"), (">", "&gt;"),
    ("“", "&ldquo;"), ("”", "&rdquo;"),
    ("‘", "&lsquo;"), ("’", "&rsquo;"),
    ("—", "&mdash;"), ("–", "&ndash;"),
    ("…", "&hellip;"),
]


def esc(s):
    for a, b in ENTITIES:
        s = s.replace(a, b)
    return s


def joined(src, keys):
    """Concatenate segments, dropping SuttaCentral's <j> verse-break hints.

    From the Fours onward the verse segments carry a bare `<j>` where the line
    is broken for display. It is markup, not text; left in it would print
    literally. Stripping it here keeps the build and the verifier in step,
    since both read the text through this function."""
    return "".join(src[k] for k in keys).replace("<j>", "").strip()


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


def text_block(page, src):
    out = ['  <section data-panel="text">',
           "    <h2>The text</h2>",
           '    <div class="text-intro">',
           "      %s" % page["text_intro"],
           "    </div>",
           "",
           '    <div class="text-block">',
           ""]
    for item in page["text"]:
        if item[0] == "h3":
            out.append("      <h3>%s</h3>\n" % item[1])
        elif item[0] == "p":
            _, label, spec = item
            body = esc(joined(src, segments(src, spec)))
            mark = '<span class="segno">%s</span>' % label if label else ""
            out.append("      <p>%s%s</p>\n" % (mark, body))
        else:
            raise ValueError(item[0])
    out.append('      <div class="ending-mark">&middot; &middot; &middot;</div>')
    out.append("")
    out.append("    </div>")
    out.append("  </section>")
    return "\n".join(out)


NUMWORD = {8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve"}


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
        opts = "\n".join('        <button class="opt">%s</button>' % o
                         for o in q["opts"])
        out.append('      <div class="q" data-correct="%d">\n'
                   '        <span class="q-num">Question %d of %d</span>\n'
                   '        <div class="q-text">%s</div>\n'
                   "%s\n"
                   '        <div class="expl"><strong>Correct: %s.</strong> %s</div>\n'
                   "      </div>\n"
                   % (q["correct"], i, n, q["q"], opts,
                      "ABCD"[q["correct"]], q["expl"]))
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
        '    <p>A series at <a href="../../">Ru-Yi Meditation Center</a></p>\n'
        '    <p style="margin-top:6px;">English translation &copy; Bhikkhu Sujato, '
        "released CC0. Reading guide written for Ru-Yi Meditation Center.</p>\n"
        "  </footer>\n"
        "  </div>\n"
        % (res, prev_href, prev_class, prev_lbl, prev_label,
           next_href, next_lbl, next_label))


SIDEBAR = """
  <aside class="pv-sidebar">
    <div class="side-tabs">
      <button class="side-tab tab active" type="button" data-tab="guide" role="tab" aria-selected="true">
        <span class="side-tab-num">01</span>
        <span class="side-tab-label">Reading Guide</span>
      </button>
      <button class="side-tab tab" type="button" data-tab="text" role="tab" aria-selected="false">
        <span class="side-tab-num">02</span>
        <span class="side-tab-label">The Text</span>
      </button>
      <button class="side-tab tab" type="button" data-tab="quiz" role="tab" aria-selected="false">
        <span class="side-tab-num">03</span>
        <span class="side-tab-label">Self-Check</span>
      </button>
    </div>
  </aside>
"""

TABS = """  <div class="tabs" role="tablist">
    <button class="tab active" type="button" data-tab="guide" role="tab" aria-selected="true">
      <span class="tab-num">01</span>
      <span class="tab-label">Reading Guide</span>
      <span class="tab-sub">Structured commentary &amp; key terms</span>
    </button>
    <button class="tab" type="button" data-tab="text" role="tab" aria-selected="false">
      <span class="tab-num">02</span>
      <span class="tab-label">The Text</span>
      <span class="tab-sub">Full translation</span>
    </button>
    <button class="tab" type="button" data-tab="quiz" role="tab" aria-selected="false">
      <span class="tab-num">03</span>
      <span class="tab-label">Self-Check</span>
      <span class="tab-sub">10-question quiz, instant feedback</span>
    </button>
  </div>
"""


def build(page, shell):
    head, tail = shell
    src = load_source(page["source"])

    header = (
        '\n  <div class="pv-header">\n\n'
        '  <nav class="crumb">\n'
        '    <a href="../../">Ru-Yi Meditation Center</a><span>&rsaquo;</span>'
        '<a href="../">The Discourses</a><span>&rsaquo;</span>'
        '<a href="./">Aṅguttara Nikāya</a><span>&rsaquo;</span>%s\n'
        "  </nav>\n\n"
        '  <div class="sutta-number">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="subtitle">%s</p>\n\n'
        "%s\n\n"
        "  <section>\n"
        "    <h2>Why this discourse</h2>\n"
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
        text_block(page, src),
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
    """Fill in prev/next from the module's page order.

    The first page links back to the collection index; the last hands off to
    whatever mod.TAIL names (the next already-published page in the series).
    An explicit prev/next on a page always wins.
    """
    pages = mod.PAGES
    head = getattr(mod, "HEAD", ("./", "Aṅguttara Nikāya selections"))
    tail = getattr(mod, "TAIL", ("./", "Aṅguttara Nikāya selections"))
    for i, page in enumerate(pages):
        label = lambda p: (p["slug"].replace("an-", "AN ").replace("-", "&ndash;")
                           + " &middot; " + p["nav_title"])
        page.setdefault("prev", head if i == 0 else
                        (pages[i - 1]["slug"] + ".html", label(pages[i - 1])))
        page.setdefault("next", tail if i == len(pages) - 1 else
                        (pages[i + 1]["slug"] + ".html", label(pages[i + 1])))
    return pages


def main():
    module = sys.argv[1] if len(sys.argv) > 1 else "an_content_01"
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
