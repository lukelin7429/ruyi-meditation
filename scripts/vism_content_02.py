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

# --------------------------------------------------------------------------- #
# Chapter 4 -- Pathavīkasiṇaniddesa
# --------------------------------------------------------------------------- #
page(
    4, "Pathavīkasiṇaniddesa", "The Earth Kasina",
    part=PART_2,
    meta_title="Visuddhimagga Ch. 4 — The Earth Kasina | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 4 of the Visuddhimagga (The Path of "
        "Purification) — preparing an earth-disk device, the three progressively "
        "refined mental signs it produces, the five hindrances and five jhāna "
        "factors, and the absorption this first meditation subject can reach. No "
        "translated text reproduced; links to the full free translation and the "
        "Pali original. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter moves directly from Chapter "
                    "3's overview into the first of the forty meditation subjects "
                    "treated in full"),
        ("Speaker", "Buddhaghosa, now giving sustained practical instruction rather "
                    "than a preview list"),
        ("Form", "The most detailed method chapter so far: physical preparation of a "
                 "device, a staged account of the mental images that arise from "
                 "working with it, the obstacles to be set aside, and the depths of "
                 "concentration that result"),
        ("Length", "one of the longest chapters in the whole work; it functions as a "
                   "template the following chapters refer back to rather than repeat"),
        ("Northern parallel", "Object-based calm-abiding methods using a fixed visual "
                              "support appear across many contemplative traditions; "
                              "this guide does not assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; introduces several "
                       "technical terms (the three signs, the five hindrances, the "
                       "five jhāna factors) that recur through the rest of Part II"),
    ],
    why=(
        "Chapter 3 previewed forty meditation subjects at a distance. Chapter 4 is "
        "where the method becomes concrete for the first time, treating the earth "
        "kasina &mdash; a simple prepared disk used as a visual support for "
        "attention &mdash; in full detail: how the device itself is prepared, what "
        "happens to the mind's image of it as concentration develops, which "
        "obstacles have to recede, and how deep that concentration can go. Because so "
        "much of this account applies equally to many of the other thirty-nine "
        "subjects, this chapter earns its length by becoming the reference point the "
        "rest of Part II leans on."),
    guide=[
        ("Preparing the physical disk", [
            "The chapter opens with practical instructions for making an earth "
            "kasina: a patch of a suitable, evenly colored clay smoothed onto a "
            "portable disk or a prepared patch of ground, set up where it can be "
            "viewed steadily and without strain. The emphasis throughout is "
            "practical &mdash; an uneven surface or an inconsistent color is treated "
            "as a real obstacle to the stages that follow, not a minor detail."]),
        ("From the object itself to a preliminary sign", [
            "Sitting before the disk with eyes alternately open and closed, a "
            "practitioner works until the image can be recalled with the eyes shut "
            "just as clearly as with them open. Buddhaghosa calls this recalled "
            "image the preliminary sign, the first of three progressively refined "
            "mental images the chapter tracks."]),
        ("The learning sign and the counterpart sign", [
            "With further practice, the preliminary sign gives way to a learning "
            "sign &mdash; a mental image reproducible without looking at the disk at "
            "all, though it still carries the physical object's particular flaws and "
            "features. Beyond that lies a third image, the counterpart sign: a "
            "purified, idealized version of the disk, free of its physical "
            "irregularities, and it is this third sign that concentration proper is "
            "built on."]),
        ("Suppressing the five hindrances", [
            "As the counterpart sign stabilizes, the chapter describes five "
            "obstacles receding in tandem: sensual desire, ill will, dullness and "
            "drowsiness, restlessness and worry, and doubt. Their withdrawal is "
            "treated as both a sign of progress and a condition for it &mdash; "
            "concentration and the hindrances are described as mutually exclusive in "
            "the mind at any given moment."]),
        ("Five factors of absorption", [
            "In their place, the chapter identifies five qualities that come to "
            "characterize the deepening state: applied thought directed at the sign, "
            "sustained thought that stays with it, a rapture that accompanies "
            "success, a settled happiness, and a one-pointedness of mind. Each is "
            "treated as opposing one or more of the five hindrances, so that their "
            "presence and the hindrances' absence are two descriptions of the same "
            "shift."]),
        ("The absorption the earth kasina can reach", [
            "Worked through fully, the chapter treats the earth kasina as capable of "
            "producing full absorption (<em>jhāna</em>), with the five factors "
            "dropping away in stages as concentration deepens further &mdash; a "
            "progression the chapter describes here for the first time and assumes "
            "as known background from this point on."]),
        ("A template for the rest of Part II", [
            "Because the sequence of signs, the role of the five hindrances, and the "
            "five jhāna factors apply well beyond this one device, later chapters on "
            "the remaining kasinas and many further subjects refer back to this "
            "chapter's account rather than restating it in full."]),
        ("What follows", [
            "Chapter 5 covers the nine remaining kasinas &mdash; water, fire, air, "
            "and several colors, among others &mdash; more briefly, as variations on "
            "the method this chapter has already laid out in detail."]),
    ],
    terms=[
        ("parikammanimitta, uggahanimitta, paṭibhāganimitta",
         "the preliminary sign, the learning sign, and the counterpart sign &mdash; "
         "three progressively refined mental images this chapter tracks as "
         "concentration on the kasina deepens."),
        ("nīvaraṇa",
         "the five hindrances &mdash; sensual desire, ill will, dullness and "
         "drowsiness, restlessness and worry, and doubt &mdash; described here as "
         "receding as the counterpart sign stabilizes."),
        ("jhānaṅga",
         "the jhāna factors &mdash; applied thought, sustained thought, rapture, "
         "happiness, and one-pointedness &mdash; the five qualities said to "
         "characterize deepening absorption."),
        ("jhāna",
         "absorption &mdash; the depth of concentration the chapter describes the "
         "earth kasina as capable of producing when worked through fully."),
        ("kasiṇa",
         "&ldquo;kasina&rdquo; &mdash; the class of ten visual-object meditation "
         "devices this chapter's earth disk belongs to, the first of the forty "
         "subjects previewed in Chapter 3."),
    ],
    quiz=[
        {"q": "What is the earth kasina, in general terms?",
         "opts": [
             "A prepared, evenly colored earth disk used as a visual support for concentration",
             "A chant recited silently while walking",
             "A formal monastic ordination ceremony",
             "A style of alms-round practiced only in certain regions"],
         "correct": 0,
         "expl": "The first of the ten kasinas among the forty meditation subjects previewed in Chapter 3."},
        {"q": "What sequence of mental images does this chapter track as concentration on the disk deepens?",
         "opts": [
             "The preliminary sign, the learning sign, and the counterpart sign",
             "A single fixed image that never changes",
             "Ten unrelated images, one per kasina",
             "No image at all; the method is entirely non-visual"],
         "correct": 0,
         "expl": "Each image is more refined than the last, with the counterpart sign purified of the object's physical flaws."},
        {"q": "What must recede for concentration on the kasina to strengthen, according to this chapter?",
         "opts": [
             "The five hindrances",
             "The five aggregates",
             "The four noble truths",
             "The three trainings"],
         "correct": 0,
         "expl": "Concentration and the hindrances are described as mutually exclusive in the mind at any given moment."},
        {"q": "Which five obstacles make up the hindrances this chapter names?",
         "opts": [
             "Sensual desire, ill will, dullness and drowsiness, restlessness and worry, and doubt",
             "Greed, hate, delusion, pride, and wrong view",
             "Hunger, thirst, fatigue, cold, and heat",
             "Fear, anger, sorrow, envy, and shame"],
         "correct": 0,
         "expl": "Their withdrawal is treated as both a sign of progress and a condition for it."},
        {"q": "What five qualities does the chapter identify as characterizing deepening absorption?",
         "opts": [
             "Applied thought, sustained thought, rapture, happiness, and one-pointedness",
             "Faith, energy, mindfulness, concentration, and wisdom",
             "Generosity, virtue, patience, effort, and insight",
             "Sight, hearing, smell, taste, and touch"],
         "correct": 0,
         "expl": "Each factor is treated as opposing one or more of the five hindrances."},
        {"q": "What can the earth kasina, worked through fully, be used to produce?",
         "opts": [
             "Full absorption (jhāna)",
             "Supernormal powers only, with no deeper concentration",
             "Only access concentration, never absorption",
             "Nothing beyond ordinary calm"],
         "correct": 0,
         "expl": "The jhāna factors are described as dropping away in further stages as concentration deepens still further."},
        {"q": "Why does this chapter function as a template for later chapters in Part II?",
         "opts": [
             "Because the sequence of signs, hindrances, and jhāna factors it describes applies well beyond this one device",
             "Because it is the shortest chapter in the entire work",
             "Because none of its content applies to any other meditation subject",
             "Because later chapters are required to quote it verbatim"],
         "correct": 0,
         "expl": "Later chapters on the remaining kasinas and other subjects refer back to this account rather than repeating it."},
        {"q": "What does Chapter 5 cover next?",
         "opts": [
             "The nine remaining kasinas, treated more briefly as variations on this chapter's method",
             "The thirteen ascetic practices",
             "The four divine abidings",
             "The five aggregates"],
         "correct": 0,
         "expl": "Water, fire, air, several colors, and others, building on the detailed method Chapter 4 establishes."},
        {"q": "What does this chapter say matters about the kasina disk's physical preparation?",
         "opts": [
             "An even color and a smooth, undistracting surface, since flaws in the object are treated as real obstacles",
             "The disk must be made of a rare or expensive material",
             "The disk's exact size is irrelevant and never discussed",
             "Only a living teacher may ever prepare the disk"],
         "correct": 0,
         "expl": "Practical care in preparing the device is treated as directly relevant to the stages that follow."},
        {"q": "Where can a reader go for Chapter 4's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("A method made concrete", [
            "earth kasina &mdash; this",
            "section's template chapter",
        ]),
        ("Three signs", [
            "preliminary, learning,",
            "and counterpart",
        ]),
        ("Hindrances and factors", [
            "five recede,",
            "five characterize absorption",
        ]),
        ("Toward absorption", [
            "jhāna &mdash; the depth",
            "the kasina can reach",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/anguttara-nikaya/an-8.65.html">AN 8.65 &mdash; '
        "Dimensions of Mastery</a> &mdash; the bases of mastery over form built "
        "directly on kasina practice, including the color kasinas.",
        '<a href="../discourses/majjhima-nikaya/mn-016.html">MN 16 &mdash; Emotional '
        "Barrenness</a> &mdash; a related but distinct fivefold list of obstacles to "
        "practice, useful for comparison with this chapter's five hindrances.",
    ],
)
