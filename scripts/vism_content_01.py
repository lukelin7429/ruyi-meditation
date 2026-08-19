# -*- coding: utf-8 -*-
"""Visuddhimagga (The Path of Purification) — original chapter-by-chapter
reading guides, no translated text reproduced. See vism_build.py's
docstring for why.

Roadmap, the traditional 23 chapters in their three-part division (this
project's own outline, for planning purposes -- not copied from any single
edition's table of contents):

  I. Sīla (Virtue) -- 2 chapters
    1. The Description of Virtue
    2. The Description of the Ascetic Practices

  II. Samādhi (Concentration) -- 11 chapters
    3. Taking a Meditation Subject
    4. The Earth Kasina
    5. The Remaining Kasinas
    6. Foulness as a Meditation Subject
    7. Six Recollections (Buddha, Dhamma, Sangha, Virtue, Generosity, Deities)
    8. Other Recollections (death, the body, breathing, peace)
    9. The Divine Abidings
    10. The Immaterial States
    11. Concentration: the remaining subjects (nutriment, the four elements)
    12. The Supernormal Powers
    13. The Other Direct-Knowledges

  III. Paññā (Understanding) -- 10 chapters
    14. The Aggregates
    15. The Bases and Elements
    16. The Faculties and Truths
    17. The Soil of Understanding (dependent origination)
    18. Purification of View
    19. Purification by Overcoming Doubt
    20. Purification by Knowledge and Vision of What Is and Is Not the Path
    21. Purification by Knowledge and Vision of the Way
    22. Purification by Knowledge and Vision
    23. The Benefits in Developing Understanding

This module currently holds only Chapter 1, as an end-to-end test of the
toolchain built for this series.
"""

# Every page's further-reading section must offer these two resources, since
# this series carries no text of its own. PDF is the legitimate free
# "for-free-distribution" edition on Access to Insight (Bhikkhu Ñāṇamoli's
# translation, copyright Buddhist Publication Society -- distributed free
# but not open-licensed, hence never quoted here); SC is the public-domain
# Pali root text on SuttaCentral.
PDF_LINK = ('<a href="https://www.accesstoinsight.org/lib/authors/nanamoli/'
            'PathofPurification2011.pdf" target="_blank" rel="noopener">Bhikkhu '
            'Ñāṇamoli&rsquo;s full translation (PDF, Access to Insight)</a> '
            '&mdash; the complete English text, distributed free by the Buddhist '
            'Publication Society; not reproduced here as it remains under '
            'copyright.')
SC_LINK = ('<a href="https://suttacentral.net/vism/pli/ms" target="_blank" '
           'rel="noopener">The Pali root text on SuttaCentral</a> &mdash; '
           'Buddhaghosa&rsquo;s original composition, public domain.')

INDEX_HEADING = "Part I: Sīla — Virtue (Chapters 1&ndash;2)"
HEAD = ("./", "Visuddhimagga guide")
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


PART_1 = "Part I: Sīla (Virtue)"

# --------------------------------------------------------------------------- #
# Chapter 1 — Sīlaniddesa
# --------------------------------------------------------------------------- #
page(
    1, "Sīlaniddesa", "The Description of Virtue",
    part=PART_1,
    meta_title="Visuddhimagga Ch. 1 — The Description of Virtue | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 1 of the Visuddhimagga (The Path of "
        "Purification) — what virtue is, its four defining aspects, its many "
        "classifications, and why the whole path opens here. No translated text "
        "reproduced; links to the full free translation and the Pali original. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; Buddhaghosa opens with a verse announcing "
                    "his intention to expound the path of purification, in response to "
                    "a question about a verse from the Saṃyutta Nikāya"),
        ("Speaker", "Buddhaghosa, 5th-century commentator, writing in his own analytical "
                    "voice rather than narrating a discourse"),
        ("Form", "Systematic analysis: a definition, then four defining aspects "
                 "(characteristic, function, manifestation, proximate cause), then "
                 "roughly a dozen ways of classifying virtue by number and kind"),
        ("Length", "the longest opening chapter in this series so far; a full reading "
                   "of the original runs well over an hour"),
        ("Northern parallel", "Comparable systematic treatments of śīla open several "
                              "Sarvāstivāda and Mahāyāna abhidharma works; this guide "
                              "does not assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; conceptually "
                       "straightforward, but the sheer number of classification schemes "
                       "rewards a second pass"),
    ],
    why=(
        "The Visuddhimagga opens exactly where its own title points: virtue "
        "(<em>sīla</em>) is the ground everything else in the path stands on, so the "
        "very first chapter is devoted entirely to defining it with the same rigor "
        "later chapters bring to concentration and understanding. Buddhaghosa does not "
        "simply describe virtue in a sentence and move on; he pins it down through four "
        "distinct analytical categories, then works through more than a dozen different "
        "ways of counting and classifying its varieties, treating the concept with the "
        "same systematic thoroughness an entomologist might bring to a single species."),
    guide=[
        ("Why the whole path opens on virtue", [
            "The Visuddhimagga is structured around the three trainings &mdash; virtue, "
            "concentration, and understanding &mdash; in that order, and the book's own "
            "structure follows suit: two chapters on virtue, eleven on concentration, "
            "ten on understanding. Starting here is not arbitrary; the text treats "
            "virtue as the precondition that makes serious meditative development "
            "possible at all, not merely a preliminary courtesy before the &lsquo;real&rsquo; "
            "practice begins."]),
        ("Four angles on one concept", [
            "Rather than offering a single definition, Buddhaghosa analyzes virtue "
            "through four questions applied throughout the whole text to nearly every "
            "important term: what is its characteristic (defining mark), its function "
            "(what it does), its manifestation (how it shows up in experience), and its "
            "proximate cause (what most immediately gives rise to it). This fourfold "
            "analytical grid is one of the Visuddhimagga's signature methods, reused "
            "for concentration, understanding, and dozens of other concepts across the "
            "whole work."]),
        ("Virtue as restraint, and virtue as quality", [
            "The chapter distinguishes virtue understood as the act of restraining "
            "unwholesome bodily and verbal conduct from virtue understood as the "
            "resulting wholesome quality of character itself &mdash; two related but "
            "distinguishable senses of the same word, both explored before the "
            "classification schemes begin."]),
        ("A cascade of classifications", [
            "Having established what virtue is, the chapter spends most of its length "
            "walking through how it can be counted and sorted: as a single undivided "
            "quality; as two (restraint and non-transgression, or the negative "
            "abstaining-from and the positive fulfilling-of); as three, four, and on "
            "upward through increasingly fine-grained schemes tied to different "
            "practical contexts &mdash; monastic versus lay virtue, virtue bound up "
            "with craving versus not, and more. The effect is less a single tidy "
            "definition than a multi-faceted map of everything the word can mean."]),
        ("Defilement, cleansing, and the chapter's close", [
            "The chapter also addresses what corrupts virtue (breaches through greed, "
            "hate, delusion, and fear) and what purifies it, before closing with a "
            "statement of virtue's benefits &mdash; freedom from remorse, a foundation "
            "for concentration, and a protective quality often compared in the "
            "tradition to a shield or an ornament."]),
        ("What follows", [
            "Chapter 2 turns from virtue in general to the thirteen optional ascetic "
            "practices (<em>dhutaṅga</em>) &mdash; voluntary austerities like eating "
            "only from the almsbowl or dwelling at the foot of a tree &mdash; closing "
            "out the book's first part before Chapter 3 opens the eleven-chapter "
            "section on concentration."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;virtue&rdquo; or &ldquo;ethical conduct&rdquo; &mdash; this chapter's "
         "subject, and the first of the path's three trainings."),
        ("lakkhaṇa, rasa, paccupaṭṭhāna, padaṭṭhāna",
         "characteristic, function, manifestation, and proximate cause &mdash; the "
         "fourfold analytical grid Buddhaghosa applies to virtue here, and reuses "
         "throughout the entire Visuddhimagga."),
        ("vāritta, cāritta",
         "restraint (abstaining from what should not be done) and performance "
         "(fulfilling what should be done) &mdash; one of the chapter's core twofold "
         "divisions of virtue."),
        ("Visuddhimagga",
         "&ldquo;The Path of Purification&rdquo; &mdash; this work's own title, and the "
         "organizing image for its entire three-part structure."),
        ("Buddhaghosa",
         "the 5th-century commentator traditionally credited as this work's author, "
         "writing in Pali, working primarily from earlier Sinhala commentarial "
         "material."),
    ],
    quiz=[
        {"q": "What are the three trainings the Visuddhimagga's whole structure is built around?",
         "opts": [
             "Virtue, concentration, and understanding",
             "Generosity, patience, and wisdom",
             "Faith, energy, and mindfulness",
             "The four noble truths"],
         "correct": 0,
         "expl": "Two chapters on virtue, eleven on concentration, ten on understanding."},
        {"q": "What four questions does Buddhaghosa apply to virtue in this chapter?",
         "opts": [
             "Characteristic, function, manifestation, and proximate cause",
             "Origin, development, cessation, and path",
             "Who, what, when, and where",
             "Cause, condition, result, and consequence"],
         "correct": 0,
         "expl": "A recurring fourfold analytical grid used throughout the whole work."},
        {"q": "What two senses of 'virtue' does the chapter distinguish?",
         "opts": [
             "Virtue as the act of restraint, and virtue as the resulting wholesome quality of character",
             "Monastic virtue and lay virtue only",
             "Virtue in this life and virtue in a future life",
             "No distinction is drawn; the chapter uses a single sense throughout"],
         "correct": 0,
         "expl": "Related but distinguishable senses of the same word."},
        {"q": "What does most of this chapter's length consist of?",
         "opts": [
             "A cascade of classification schemes, counting and sorting virtue in increasingly fine-grained ways",
             "A single narrative story illustrating virtue",
             "A verbatim reproduction of the monastic training rules",
             "A debate between two named monks"],
         "correct": 0,
         "expl": "From a single undivided quality up through many multi-part schemes."},
        {"q": "What does the chapter identify as corrupting virtue?",
         "opts": [
             "Breaches through greed, hate, delusion, and fear",
             "Only physical injury to another being",
             "Nothing; the chapter treats virtue as incorruptible",
             "Disagreement with a teacher's instructions"],
         "correct": 0,
         "expl": "Discussed alongside what purifies virtue, before the chapter's closing statement of its benefits."},
        {"q": "What benefits does the chapter attribute to virtue?",
         "opts": [
             "Freedom from remorse, a foundation for concentration, and a protective quality",
             "Immediate full awakening, with no further practice required",
             "Wealth and social status in this life alone",
             "No benefits are named; the chapter is purely definitional"],
         "correct": 0,
         "expl": "Often compared in the tradition to a shield or an ornament."},
        {"q": "What does Chapter 2 turn to next?",
         "opts": [
             "The thirteen optional ascetic practices (dhutaṅga)",
             "The forty meditation subjects",
             "The five aggregates",
             "The four noble truths"],
         "correct": 0,
         "expl": "Closing out Part I (Virtue) before Chapter 3 opens Part II (Concentration)."},
        {"q": "How many total chapters does the Visuddhimagga have, and how are they divided?",
         "opts": [
             "23 chapters: 2 on virtue, 11 on concentration, 10 on understanding",
             "10 chapters, one per perfection",
             "108 chapters, one per defilement",
             "3 chapters, one per training"],
         "correct": 0,
         "expl": "This chapter opens the first of the three parts."},
        {"q": "Why does this reading guide not include the chapter's translated text?",
         "opts": [
             "Bhikkhu Ñāṇamoli's English translation remains under active copyright and is not available for reproduction here",
             "The chapter has never been translated into English",
             "The original Pali no longer survives",
             "This site has a policy against ever discussing commentarial literature"],
         "correct": 0,
         "expl": "The Pali original is public domain, but the only complete English translation is not."},
        {"q": "Where can a reader go for the chapter's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only by purchasing a specific edition with no free alternative",
             "This page's own quiz section contains the full text"],
         "correct": 0,
         "expl": "Every page in this series links to both, since none reproduces the text itself."},
    ],
    marginalia=[
        ("Where the path begins", [
            "sīla &mdash; virtue,",
            "the first of three trainings",
        ]),
        ("Four questions, one method", [
            "characteristic, function,",
            "manifestation, proximate cause",
        ]),
        ("Two senses of one word", [
            "restraint (vāritta)",
            "and performance (cāritta)",
        ]),
        ("23 chapters, three parts", [
            "virtue (2), concentration (11),",
            "understanding (10)",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/">Saṃyutta Nikāya</a> &mdash; the verse '
        "this whole work traditionally opens by responding to a question about.",
        '<a href="../discourses/dhammapada/">Dhammapada</a> &mdash; a much shorter, '
        "already-complete verse collection on this site, for comparison in scale.",
    ],
)
