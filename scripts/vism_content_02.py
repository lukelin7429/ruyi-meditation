# -*- coding: utf-8 -*-
"""Visuddhimagga -- Part II: Samādhi (Concentration), Chapters 3-13.

Same no-verbatim-text policy as vism_content_01.py -- see vism_build.py's
docstring. This module opens with Chapter 3 and grows one chapter at a
time; HEAD points back at the last page of Part I (vism-2.html), TAIL
stays at the collection page until a Part III module exists to hand off
to.
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

INDEX_HEADING = "Part II: Samādhi — Concentration (Chapters 3&ndash;13)"
HEAD = ("vism-2.html", "The Description of the Ascetic Practices")
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


PART_2 = "Part II: Samādhi (Concentration)"

# --------------------------------------------------------------------------- #
# Chapter 3 -- Kammaṭṭhānaggahananiddesa
# --------------------------------------------------------------------------- #
page(
    3, "Kammaṭṭhānaggahananiddesa", "Taking a Meditation Subject",
    part=PART_2,
    meta_title="Visuddhimagga Ch. 3 — Taking a Meditation Subject | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 3 of the Visuddhimagga (The Path of "
        "Purification) — choosing a dwelling, cutting off the ten impediments, "
        "approaching a teacher, the six temperaments, and a preview of the forty "
        "meditation subjects that open Part II. No translated text reproduced; links "
        "to the full free translation and the Pali original. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter opens Part II with practical "
                    "groundwork rather than a framing story"),
        ("Speaker", "Buddhaghosa, continuing the same systematic voice, now turned "
                    "toward concentration practice"),
        ("Form", "Procedural rather than purely definitional: dwelling selection, a "
                 "list of impediments to clear away, the role of a teacher, a "
                 "sixfold typing of temperament, and a preview list of forty "
                 "meditation subjects"),
        ("Length", "moderate; mostly enumerable lists rather than sustained "
                   "argument"),
        ("Northern parallel", "Temperament-matched meditation-subject schemes and "
                              "lists of obstacles to retreat appear in other "
                              "Buddhist meditation manuals; this guide does not "
                              "assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; several lists to "
                       "hold in mind (impediments, temperaments, the forty "
                       "subjects), but each item is straightforward on its own"),
    ],
    why=(
        "Part I established virtue as the ground the whole path stands on. Chapter 3 "
        "makes the turn from that ground to actual practice: before concentration "
        "can be developed, a practitioner needs a workable place to live, freedom "
        "from the entanglements that would pull attention away, and a qualified "
        "teacher who can match a meditation subject to that particular person. Only "
        "once these practical conditions are in place does the chapter step back and "
        "preview the forty meditation subjects the rest of Part II will work through "
        "one at a time."),
    guide=[
        ("Where a meditator should live", [
            "The chapter opens by weighing what makes a dwelling workable for serious "
            "practice: near enough to a village for alms but not so near that noise "
            "and traffic intrude, with access to water and suitable company, free of "
            "the kind of disturbances that make sustained attention difficult. This is "
            "treated as a real practical question, not a formality, since the wrong "
            "setting can undermine training before it starts."]),
        ("Cutting off the impediments", [
            "Before taking up a meditation subject in earnest, the chapter lists ten "
            "kinds of worldly entanglement a serious student is expected to set "
            "aside: a troublesome dwelling, family concerns, gain and reputation, an "
            "unfinished building project, travel obligations, demanding relatives, "
            "illness, formal study, and even supernormal powers already gained "
            "elsewhere, when any of these still occupies the mind. Not every "
            "impediment applies to every person; the point is to recognize which of "
            "the ten are still live concerns and resolve or set them down first."]),
        ("Approaching a good friend", [
            "Rather than choosing a meditation subject on one's own, the chapter "
            "presents this as something learned from a qualified teacher, called a "
            "&lsquo;good friend&rsquo; (<em>kalyāṇamitta</em>), who can read a "
            "student's temperament and assign a subject genuinely suited to them, "
            "rather than one the student happens to find appealing."]),
        ("Six temperaments", [
            "The chapter sets out six personality types &mdash; the greedy, the "
            "hating, the deluded, the faithful, the intelligent, and the speculative "
            "(prone to restless thinking) &mdash; and treats matching a person's "
            "temperament to a compatible meditation subject as central to a "
            "teacher's role, since a subject well suited to one temperament can sit "
            "poorly with another."]),
        ("Forty subjects, previewed", [
            "Having covered the practical setup, the chapter closes with an overview "
            "list of forty meditation subjects (<em>kammaṭṭhāna</em>), grouped into "
            "categories: ten kasinas (devices such as a colored disk or an earth "
            "surface used as a visual focus), ten kinds of foulness (corpse "
            "contemplations), ten recollections, four divine abidings, four "
            "immaterial states, one perception of food's unattractiveness, and one "
            "analytical defining of the four elements. This list is a map for what "
            "Chapters 4 through 11 will each take up in turn, not a treatment of any "
            "one subject in detail."]),
        ("Access and absorption", [
            "The chapter also distinguishes two depths of concentration that "
            "practice with these subjects can reach: a preliminary steadiness called "
            "access concentration, and the fuller absorption that some &mdash; but "
            "not all &mdash; of the forty subjects are capable of producing. Which "
            "depth a given subject can reach becomes relevant again as each one is "
            "treated individually in the following chapters."]),
        ("What follows", [
            "Chapter 4 begins the detailed treatment with the first and most "
            "extensively discussed of the forty subjects: the earth kasina, taken as "
            "the template for how the other kasinas will later be handled more "
            "briefly."]),
    ],
    terms=[
        ("kammaṭṭhāna",
         "&ldquo;meditation subject&rdquo; &mdash; any of the forty objects of "
         "concentration this chapter previews and Chapters 4&ndash;11 treat in turn."),
        ("kalyāṇamitta",
         "&ldquo;good friend&rdquo; &mdash; the qualified teacher a student "
         "approaches to be assigned a meditation subject, rather than choosing one "
         "unaided."),
        ("palibodha",
         "&ldquo;impediment&rdquo; &mdash; any of ten kinds of worldly entanglement "
         "the chapter says should be cleared away before serious training begins."),
        ("carita",
         "&ldquo;temperament&rdquo; &mdash; the sixfold typing (greedy, hating, "
         "deluded, faithful, intelligent, speculative) used to match a person to a "
         "suitable subject."),
        ("upacāra, appanā",
         "access (concentration) and absorption &mdash; the two depths of "
         "concentration the forty subjects lead to in differing measure."),
    ],
    quiz=[
        {"q": "What does Part II of the Visuddhimagga, opened by this chapter, cover?",
         "opts": [
             "Concentration (samādhi), across eleven chapters",
             "Virtue (sīla), across two chapters",
             "Understanding (paññā), across ten chapters",
             "The Vinaya rules for monastics"],
         "correct": 0,
         "expl": "Chapter 3 opens the concentration section that runs through Chapter 13."},
        {"q": "What two practical concerns does the chapter address before any meditation subject is taken up?",
         "opts": [
             "A workable dwelling and freedom from the ten impediments",
             "A specific diet and a fixed daily schedule",
             "Ordination status and seniority",
             "Financial support from lay donors"],
         "correct": 0,
         "expl": "Setting and entanglements are cleared away before training begins in earnest."},
        {"q": "What are the ten palibodha the chapter lists?",
         "opts": [
             "Ten kinds of worldly entanglement, such as family concerns, gain and reputation, and unfinished projects",
             "Ten meditation subjects reserved for advanced practitioners only",
             "Ten monastic offenses requiring formal confession",
             "Ten types of dwelling ranked from best to worst"],
         "correct": 0,
         "expl": "Not every impediment applies to every person; the point is to recognize and resolve the live ones."},
        {"q": "What role does the kalyāṇamitta play in this chapter?",
         "opts": [
             "A qualified teacher who reads a student's temperament and assigns a suitable meditation subject",
             "A fellow meditator of exactly equal experience",
             "A lay donor who supplies robes and food",
             "A historical figure no longer consulted directly"],
         "correct": 0,
         "expl": "Choosing a subject is presented as something learned from a teacher, not self-taught."},
        {"q": "How many temperaments does the chapter describe, and what is their purpose?",
         "opts": [
             "Six, used to match a person to a compatible meditation subject",
             "Two, simply pleasant and unpleasant",
             "Four, matching the four elements",
             "None; temperament is treated as irrelevant to practice"],
         "correct": 0,
         "expl": "Greedy, hating, deluded, faithful, intelligent, and speculative."},
        {"q": "How many meditation subjects does the chapter preview in total?",
         "opts": [
             "Forty",
             "Eight",
             "Thirteen",
             "One hundred and eight"],
         "correct": 0,
         "expl": "Grouped into kasinas, kinds of foulness, recollections, divine abidings, immaterial states, and two further single subjects."},
        {"q": "Which categories make up the forty meditation subjects previewed here?",
         "opts": [
             "Ten kasinas, ten kinds of foulness, ten recollections, four divine abidings, four immaterial states, plus two further subjects",
             "Forty individually unrelated exercises with no grouping",
             "Ten precepts repeated across four categories",
             "Thirteen ascetic practices plus twenty-seven others"],
         "correct": 0,
         "expl": "This list is the map Chapters 4 through 11 will work through one at a time."},
        {"q": "What two depths of concentration does the chapter distinguish?",
         "opts": [
             "Access concentration and absorption",
             "Waking concentration and dream concentration",
             "Monastic concentration and lay concentration",
             "Momentary concentration and permanent concentration"],
         "correct": 0,
         "expl": "Not all forty subjects are capable of producing full absorption."},
        {"q": "Which meditation subject does Chapter 4 take up first?",
         "opts": [
             "The earth kasina, used as the template for how the other kasinas are later treated",
             "The recollection of death",
             "The divine abiding of loving-kindness",
             "The perception of the body's foulness"],
         "correct": 0,
         "expl": "The most extensively discussed of the forty subjects, treated first and most fully."},
        {"q": "Where can a reader go for Chapter 3's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Opening Part II", [
            "samādhi &mdash; concentration,",
            "eleven chapters ahead",
        ]),
        ("Ten impediments", [
            "worldly entanglements",
            "cleared before training",
        ]),
        ("Six temperaments", [
            "matched to a",
            "compatible subject",
        ]),
        ("Forty subjects previewed", [
            "kasinas, foulness, recollections,",
            "divine abidings, and more",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/anguttara-nikaya/an-10.17.html">AN 10.17 &mdash; A '
        "Protector (1st)</a> &mdash; on the qualities, including good friendship, "
        "that support a mendicant's own practice.",
        '<a href="../discourses/anguttara-nikaya/an-8.65.html">AN 8.65 &mdash; '
        "Dimensions of Mastery</a> &mdash; on the bases of mastery closely related "
        "to the kasina practices this chapter previews.",
    ],
)
