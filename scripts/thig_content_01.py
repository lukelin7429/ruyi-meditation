# -*- coding: utf-8 -*-
"""Therigatha — Verses of the Senior Nuns. Organized into books by the
number of verses attributed to each elder (Book of the Ones, Twos...)."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Therigatha — Verses of the Senior Nuns"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Therigatha selections")
TAIL = ("./", "Therigatha selections")
INDEX_EXTRA = []

PAGES = []


def page(book, num, pali, title, **kw):
    """Shared scaffolding for a single elder's verses in the Therigatha.

    Same two-level addressing as thag_content_01.py's page() -- see that
    file's docstring for the rationale.
    """
    d = {
        "slug": "thig-%d.%d" % (book, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "thig%d.%d" % (book, num),
        "crumb": "Thig %d.%d" % (book, num),
        "number_line": "Therigatha &middot; %d.%d" % (book, num),
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
