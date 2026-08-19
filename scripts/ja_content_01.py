# -*- coding: utf-8 -*-
"""Jataka -- selected verses from the birth stories.

IMPORTANT SCOPE NOTE (per Luke's explicit decision 2026-08-19): the
traditional Jataka collection has 547 numbered birth stories, but bilara-data
contains Sujato CC0 translations for only 82 of them, scattered
non-sequentially (ja1, ja2... ja67, ja466...), and even those 82 are bare
verse excerpts -- the prose narrative framework that gives each Jataka tale
its story is post-canonical commentary, not part of the CC0 canonical text,
and is not available to build from. This collection can therefore never be
"complete" the way Dhammapada/Udana/Itivuttaka/Sutta-Nipata/Khuddakapatha
can. Every page in this module, and this collection's own index.html, must
say so explicitly and never imply full coverage of the traditional 547.
"""

SC = "https://suttacentral.net"

INDEX_HEADING = "Jataka — Selected Verses"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Jataka selections")
TAIL = ("./", "Jataka selections")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single Jataka verse excerpt.

    num is the traditional Jataka number (not sequential in this project --
    only the 82 numbers with a Sujato CC0 file exist at all; see this
    module's docstring). Every page built from this helper must include,
    in its own "why"/glance text, an honest note that this is a bare verse
    excerpt from a partial selection, not the traditional story in full.
    """
    d = {
        "slug": "ja-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "ja%d" % num,
        "crumb": "Ja %d" % num,
        "number_line": "Jataka &middot; No. %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
