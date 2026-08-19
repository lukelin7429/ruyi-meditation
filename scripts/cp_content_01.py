# -*- coding: utf-8 -*-
"""Cariyapitaka — The Basket of Conduct. 35 past-life verse stories, one per page."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Cariyapitaka — The Basket of Conduct"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Cariyapitaka selections")
TAIL = ("./", "Cariyapitaka selections")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single past-life story of the Cariyapitaka."""
    d = {
        "slug": "cp-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "cp%d" % num,
        "crumb": "Cp %d" % num,
        "number_line": "Cariyapitaka &middot; Story %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
