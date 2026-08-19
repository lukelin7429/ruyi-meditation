# -*- coding: utf-8 -*-
"""Theragatha — Verses of the Senior Monks. Organized into books by the
number of verses attributed to each elder (Book of the Ones, Twos...)."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Theragatha — Verses of the Senior Monks"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Theragatha selections")
TAIL = ("./", "Theragatha selections")
INDEX_EXTRA = []

PAGES = []


def page(book, num, pali, title, **kw):
    """Shared scaffolding for a single elder's verses in the Theragatha.

    Like the Saṃyutta Nikāya, this collection spans several independently
    numbered books (Book of the Ones, Book of the Twos...), so both the book
    and the poem number are required. Unlike SN, bilara-data keeps every
    file flat (no per-book subfolder) -- see thag_build.py's load_source.
    """
    d = {
        "slug": "thag-%d.%d" % (book, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "thag%d.%d" % (book, num),
        "crumb": "Thag %d.%d" % (book, num),
        "number_line": "Theragatha &middot; %d.%d" % (book, num),
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
