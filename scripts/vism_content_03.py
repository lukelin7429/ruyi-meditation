# -*- coding: utf-8 -*-
"""Visuddhimagga -- Part III: Paññā (Understanding), Chapters 14-23.

Same no-verbatim-text policy as vism_content_01.py/02.py -- see
vism_build.py's docstring. This module opens with Chapter 14; HEAD points
back at the last page of Part II (vism-13.html), TAIL stays at the
collection page since this is the work's final part.
"""

PDF_LINK = ('<a href="https://www.accesstoinsight.org/lib/authors/nanamoli/'
            'PathofPurification2011.pdf" target="_blank" rel="noopener">Bhikkhu '
            'Ñāṇamoli&rsquo;s full translation (PDF, Access to Insight)</a> '
            '&mdash; the complete English text, distributed free by the Buddhist '
            'Publication Society; not reproduced here as it remains under '
            'copyright.')
SC_LINK = ('<a href="https://suttacentral.net/vism/pli/ms" target="_blank" '
           'rel="noopener">The Pali root text on SuttaCentral</a> &mdash; '
           'Buddhaghosa&rsquo;s original composition, public domain.')

INDEX_HEADING = "Part III: Paññā — Understanding (Chapters 14&ndash;23)"
HEAD = ("vism-13.html", "The Other Direct-Knowledges")
TAIL = ("./", "Visuddhimagga guide")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single Visuddhimagga chapter guide."""
    d = {
        "slug": "vism-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "crumb": "Chapter %d" % num,
        "number_line": "Visuddhimagga &middot; Chapter %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("part") if "part" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


PART_3 = "Part III: Paññā (Understanding)"

# --------------------------------------------------------------------------- #
# Chapter 14 -- Khandhaniddesa
# --------------------------------------------------------------------------- #
page(
    14, "Khandhaniddesa", "The Aggregates",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 14 — The Aggregates | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 14 of the Visuddhimagga (The Path of "
        "Purification) — the five aggregates, why each is called an "
        "&lsquo;aggregate&rsquo;, an elevenfold cross-section applied to each, and "
        "why this analysis marks the real beginning of insight. No translated text "
        "reproduced; links to the full free translation and the Pali original. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter opens Part III with the same "
                    "systematic method Part I used for virtue, now turned toward "
                    "analysis rather than practical training"),
        ("Speaker", "Buddhaghosa, opening the ten-chapter section on understanding"),
        ("Form", "Five categories analyzed in turn, each run through a defining "
                 "framework and then a recurring elevenfold classification"),
        ("Length", "substantial, given the systematic detail applied to each of the "
                   "five categories in turn"),
        ("Northern parallel", "Analysis of a person into five aggregates is one of "
                              "the most widely shared frameworks across Buddhist "
                              "traditions; this guide does not assert a specific "
                              "matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the most "
                       "abstract material the series has covered so far, opening "
                       "the doctrinally dense final third of the work"),
    ],
    why=(
        "Parts I and II built the practical foundation (virtue) and the meditative "
        "skill (concentration) the whole path depends on. Part III turns to what "
        "all of that has been in service of: seeing clearly. Chapter 14 opens this "
        "work with the most basic analytical move the rest of the section builds "
        "on &mdash; breaking down what is ordinarily experienced as a single, "
        "unified person into five aggregates, none of which, examined "
        "individually, amounts to anything fixed."),
    guide=[
        ("A different kind of chapter", [
            "Where Parts I and II were organized around practical training "
            "&mdash; conduct to take up, subjects to develop &mdash; Part III works "
            "by taking apart what ordinarily looks unified. Chapter 14 is where "
            "that analytical project begins."]),
        ("Five aggregates", [
            "The chapter treats five categories in turn: form, covering material "
            "and physical phenomena; feeling, the pleasant, unpleasant, or neutral "
            "quality of experience; perception, the factor that recognizes and "
            "labels; formations, a broad and notably heterogeneous category "
            "covering the mind's remaining volitional and constructing activity; "
            "and consciousness, bare cognizing awareness, itself further divided "
            "by which of the six sense doors it arises through."]),
        ("Why &lsquo;aggregate&rsquo;", [
            "The chapter explains the term khandha as reflecting that each of the "
            "five is itself a grouping rather than a single thing &mdash; form "
            "alone covers many distinct material phenomena bundled under one "
            "heading, and the same holds for each of the other four."]),
        ("An elevenfold cross-section", [
            "Rather than offering one flat definition, the chapter applies a "
            "recurring elevenfold classification to each of the five aggregates in "
            "turn: past, future, and present; internal and external; gross and "
            "subtle; inferior and superior; far and near &mdash; producing a "
            "systematic cross-section of each category rather than a single "
            "summary statement."]),
        ("Five aggregates, no fixed self", [
            "The chapter's underlying point is made explicit through this "
            "analysis: what is conventionally experienced and spoken of as a "
            "single &lsquo;person&rsquo; or &lsquo;self&rsquo; resolves, on "
            "examination, into five distinct, constantly varying categories, none "
            "of which by itself constitutes anything fixed or unified."]),
        ("The actual start of insight", [
            "This kind of analytical seeing, rather than concentration itself, is "
            "what the tradition calls insight (<em>vipassanā</em>), and this "
            "chapter marks its real beginning within the Visuddhimagga's own "
            "structure, distinct from everything Part II covered."]),
        ("What follows", [
            "Chapter 15 continues the same analytical project with two further "
            "classification schemes: the sense bases and the elements."]),
    ],
    terms=[
        ("khandha",
         "&ldquo;aggregate&rdquo; &mdash; this chapter's general term and "
         "organizing concept, reflecting that each category is a grouping of many "
         "instances."),
        ("rūpa",
         "form &mdash; the first aggregate, covering material and physical "
         "phenomena."),
        ("vedanā, saññā",
         "feeling and perception &mdash; the second and third aggregates."),
        ("saṅkhāra",
         "(mental) formations &mdash; the fourth and most heterogeneous "
         "aggregate, covering the mind's remaining volitional activity."),
        ("viññāṇa",
         "consciousness &mdash; the fifth aggregate, itself divided by the six "
         "sense doors it arises through."),
    ],
    quiz=[
        {"q": "What shift does Chapter 14 mark within the Visuddhimagga's overall structure?",
         "opts": [
             "From Parts I and II's practical training to Part III's analytical project",
             "A return to the practical training already covered in Part I",
             "The end of the entire work",
             "A repeat of Chapter 3's preview of meditation subjects"],
         "correct": 0,
         "expl": "Part III works by taking apart what ordinarily looks unified."},
        {"q": "What five categories does this chapter analyze?",
         "opts": [
             "Form, feeling, perception, formations, and consciousness",
             "Virtue, concentration, understanding, liberation, and knowledge",
             "The four elements and space",
             "The ten kasinas"],
         "correct": 0,
         "expl": "The traditional five aggregates, each treated in turn."},
        {"q": "What does the aggregate of form cover?",
         "opts": [
             "Material and physical phenomena",
             "Only thoughts and ideas",
             "Only pleasant sensations",
             "Only sounds and smells"],
         "correct": 0,
         "expl": "The first of the five aggregates the chapter treats."},
        {"q": "What does the aggregate of feeling cover?",
         "opts": [
             "The pleasant, unpleasant, or neutral quality of experience",
             "Physical strength and endurance",
             "Memory of past events specifically",
             "Visual perception exclusively"],
         "correct": 0,
         "expl": "Distinct from perception, which is treated as a separate, third aggregate."},
        {"q": "Why is the aggregate of formations (saṅkhāra) described as especially heterogeneous?",
         "opts": [
             "It is a broad category covering the mind's remaining volitional and constructing activity beyond feeling and perception",
             "It contains only a single, simple mental factor",
             "It refers only to physical formations like rock and clay",
             "It is identical in content to the aggregate of consciousness"],
         "correct": 0,
         "expl": "Everything mental not already classed as feeling or perception falls here."},
        {"q": "How is the aggregate of consciousness further subdivided?",
         "opts": [
             "By which of the six sense doors it arises through",
             "By the practitioner's age at the time it arises",
             "By whether it occurs during the day or at night",
             "It cannot be subdivided at all"],
         "correct": 0,
         "expl": "Eye-, ear-, nose-, tongue-, body-, and mind-consciousness."},
        {"q": "Why does the chapter use the term &lsquo;aggregate&rsquo; (khandha) for each of the five categories?",
         "opts": [
             "Because each is itself a grouping of many instances, not a single thing",
             "Because the term simply means &lsquo;important&rsquo; in Pali",
             "Because there are exactly five physical objects each aggregate refers to",
             "Because the term was invented specifically for this chapter and used nowhere else"],
         "correct": 0,
         "expl": "Form alone, for instance, covers many distinct material phenomena bundled under one heading."},
        {"q": "What elevenfold classification does the chapter apply to each of the five aggregates?",
         "opts": [
             "Past/future/present, internal/external, gross/subtle, inferior/superior, far/near",
             "A ranking from most to least important",
             "A count of how many times each aggregate is mentioned in the canon",
             "A geographic classification by region"],
         "correct": 0,
         "expl": "Producing a systematic cross-section of each aggregate rather than one flat definition."},
        {"q": "What is the chapter's underlying point about the conventional sense of a unified &lsquo;self&rsquo;?",
         "opts": [
             "It resolves into five distinct, constantly varying categories, none fixed or unified on its own",
             "It is confirmed and reinforced by this analysis",
             "It exists independently of all five aggregates",
             "The chapter reaches no conclusion on this question"],
         "correct": 0,
         "expl": "The analytical move this chapter opens Part III with."},
        {"q": "Where can a reader go for Chapter 14's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("A different kind of chapter", [
            "Part III begins &mdash;",
            "understanding, not concentration",
        ]),
        ("Five aggregates", [
            "form, feeling, perception,",
            "formations, consciousness",
        ]),
        ("An elevenfold cross-section", [
            "past/future/present, internal/external,",
            "gross/subtle, inferior/superior, far/near",
        ]),
        ("No fixed self", [
            "five varying categories,",
            "none of them unified",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/sn-22.59.html">SN 22.59 &mdash; The '
        "Characteristic of Not-Self</a> &mdash; the foundational discourse "
        "analyzing the five aggregates this chapter treats in systematic detail.",
        '<a href="../discourses/samyutta-nikaya/sn-22.1.html">SN 22.1 &mdash; '
        "Nakula's Father</a> &mdash; a further discourse from the same collection "
        "devoted to the five aggregates.",
    ],
)
