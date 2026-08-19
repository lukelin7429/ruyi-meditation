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

# --------------------------------------------------------------------------- #
# Chapter 5 -- Sesakasiṇaniddesa
# --------------------------------------------------------------------------- #
page(
    5, "Sesakasiṇaniddesa", "The Remaining Kasinas",
    part=PART_2,
    meta_title="Visuddhimagga Ch. 5 — The Remaining Kasinas | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 5 of the Visuddhimagga (The Path of "
        "Purification) — the nine kasinas beyond earth: water, fire, air, four "
        "colors, light, and bounded space, each a variation on Chapter 4's method. "
        "No translated text reproduced; links to the full free translation and the "
        "Pali original. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter continues directly from "
                    "Chapter 4's detailed treatment of the earth kasina"),
        ("Speaker", "Buddhaghosa, applying Chapter 4's method to nine further "
                    "devices in a much more compressed form"),
        ("Form", "Nine short entries, one per remaining kasina, each noting only "
                 "what differs from the earth kasina rather than restating the full "
                 "method"),
        ("Length", "considerably shorter than Chapter 4, since the underlying "
                   "account of signs, hindrances, and jhāna factors is assumed "
                   "rather than repeated"),
        ("Northern parallel", "Other traditions likewise use varied physical objects "
                              "(colored disks, light, bounded space) as concentration "
                              "supports; this guide does not assert a specific "
                              "matching passage"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; mostly a "
                       "practical survey, easy to follow once Chapter 4's method is "
                       "in hand"),
    ],
    why=(
        "Chapter 4 gave the full method through a single device, the earth kasina. "
        "Chapter 5 completes the set of ten by working through the remaining nine "
        "&mdash; water, fire, air, four colors, light, and a bounded area of space "
        "&mdash; but treats each briefly, noting only how its physical preparation "
        "and characteristic quality differ from the earth kasina already covered. "
        "The chapter's underlying claim is that all ten reach the same destination "
        "by the same method; what changes from one kasina to the next is only the "
        "object placed in front of that method."),
    guide=[
        ("Nine variations on one method", [
            "Rather than repeating Chapter 4's full account of the three signs, the "
            "five hindrances, and the five jhāna factors, this chapter assumes that "
            "account as known and describes, for each of the remaining nine kasinas, "
            "only what is specific to preparing and attending to that particular "
            "device."]),
        ("The kasina list completed", [
            "Together with the earth kasina from Chapter 4, this chapter brings the "
            "traditional list of ten kasinas to completion: earth, water, fire, and "
            "air; four colors (blue, yellow, red, and white); light; and a bounded "
            "area of space."]),
        ("Water, fire, and air", [
            "The water kasina is prepared by viewing clear water held in a vessel. "
            "The fire kasina is traditionally attended to through a small opening in "
            "a screen rather than by looking at an open flame directly. The air "
            "kasina is approached indirectly as well, since moving air has no "
            "visible form of its own &mdash; attention rests instead on something "
            "stirred by it, such as the swaying tips of grass or the movement of a "
            "banner."]),
        ("The four color kasinas", [
            "Blue, yellow, red, and white are each prepared much as the earth "
            "kasina was: as an evenly colored disk, or by using a naturally suited "
            "colored object such as a flower or cloth of the right hue, then worked "
            "through the same sequence of signs described in Chapter 4."]),
        ("Light and bounded space", [
            "The light kasina takes a patch of steady light &mdash; such as light "
            "falling through a small gap &mdash; as its object. The space kasina is "
            "unusual among the ten in taking an absence rather than a colored "
            "surface as its object: a gap or opening of a fixed, defined size, "
            "attended to as a bounded area rather than as a visible thing."]),
        ("All ten, one destination", [
            "The chapter's recurring point across all nine entries is that none of "
            "them requires a different method from the one Chapter 4 already gave "
            "in full: any of the ten kasinas, worked through its own three signs, "
            "can be brought to the same depth of absorption. What differs between "
            "them is preparation and characteristic feel, not the underlying "
            "process."]),
        ("Which kasina to begin with", [
            "The earth kasina is generally treated as the easiest starting point, "
            "given the stability and universal familiarity of its object, though "
            "the chapter also connects the choice back to the six temperaments "
            "introduced in Chapter 3, since some of the ten may suit a particular "
            "temperament better than others."]),
        ("What follows", [
            "Chapter 6 leaves the kasinas behind entirely and turns to an "
            "altogether different class of object: foulness, meaning sustained "
            "contemplation of a corpse in its stages of decay, the next of the forty "
            "meditation subjects."]),
    ],
    terms=[
        ("āpokasiṇa",
         "the water kasina &mdash; prepared by viewing clear water held in a "
         "vessel."),
        ("tejokasiṇa",
         "the fire kasina &mdash; traditionally viewed through a small opening in a "
         "screen rather than looking at an open flame directly."),
        ("vāyokasiṇa",
         "the air (wind) kasina &mdash; attended to indirectly, through something "
         "moved by the wind, since air itself has no visible form."),
        ("nīla, pīta, lohita, odāta kasiṇa",
         "the four color kasinas &mdash; blue, yellow, red, and white &mdash; each "
         "prepared as an evenly colored disk or a suitably colored object."),
        ("āloka, ākāsa kasiṇa",
         "the light kasina and the (bounded) space kasina &mdash; the final two of "
         "the ten, taking a patch of light and a fixed-size gap respectively as "
         "their objects."),
    ],
    quiz=[
        {"q": "How many kasinas does the traditional list total, once this chapter's nine are added to Chapter 4's earth kasina?",
         "opts": [
             "Ten",
             "Four",
             "Thirteen",
             "Forty"],
         "correct": 0,
         "expl": "Earth, water, fire, air, four colors, light, and bounded space."},
        {"q": "Does this chapter repeat Chapter 4's full account of the three signs, the hindrances, and the jhāna factors for each new kasina?",
         "opts": [
             "No &mdash; it assumes that account and describes only what differs for each device",
             "Yes, in full, for all nine remaining kasinas individually",
             "No, because none of the other nine can reach absorption at all",
             "Yes, but only for the water and fire kasinas"],
         "correct": 0,
         "expl": "Chapter 5 is deliberately compressed compared to Chapter 4's full template treatment."},
        {"q": "How is the water kasina prepared?",
         "opts": [
             "By viewing clear water held in a vessel",
             "By listening to the sound of flowing water",
             "By submerging the whole body in a river",
             "By boiling water and observing the steam"],
         "correct": 0,
         "expl": "A visual object, like the other kasinas, not an auditory or tactile one."},
        {"q": "Why is the air (wind) kasina attended to indirectly, through something like swaying grass or a banner?",
         "opts": [
             "Because moving air has no visible form of its own",
             "Because looking directly at air causes eye strain",
             "Because air is considered too dangerous a subject for beginners",
             "Because the earlier chapters forbid attending to invisible things"],
         "correct": 0,
         "expl": "Attention rests on something moved by the wind rather than the wind itself."},
        {"q": "Which four colors make up the color kasinas this chapter covers?",
         "opts": [
             "Blue, yellow, red, and white",
             "Black, gray, brown, and gold",
             "Green, purple, orange, and pink",
             "Only blue and white"],
         "correct": 0,
         "expl": "Each prepared much as the earth kasina was, as an evenly colored disk or suited object."},
        {"q": "What is unusual about the space kasina's object compared to the other nine?",
         "opts": [
             "It takes an absence &mdash; a bounded gap of fixed size &mdash; rather than a colored surface",
             "It is the only kasina that changes color over time",
             "It requires no physical preparation of any kind",
             "It is the only kasina that cannot be practiced indoors"],
         "correct": 0,
         "expl": "Attended to as a bounded area rather than as a visible thing."},
        {"q": "What does the chapter say all ten kasinas share, despite their different objects?",
         "opts": [
             "All can be brought to the same depth of absorption by the same underlying method",
             "Only the earth kasina can ever reach full absorption",
             "Each kasina requires an entirely separate, unrelated method",
             "None of the ten can be practiced without a teacher present at every session"],
         "correct": 0,
         "expl": "What differs between them is preparation and characteristic feel, not the underlying process."},
        {"q": "Which kasina is generally treated as the easiest starting point, and why?",
         "opts": [
             "The earth kasina, for the stability and universal familiarity of its object",
             "The space kasina, because it requires no physical object at all",
             "The fire kasina, because it produces results fastest",
             "The light kasina, because it requires no prior training"],
         "correct": 0,
         "expl": "The chapter also connects the choice back to the six temperaments from Chapter 3."},
        {"q": "What does Chapter 6 turn to next?",
         "opts": [
             "Foulness &mdash; sustained contemplation of a corpse in its stages of decay",
             "The four divine abidings",
             "The immaterial states",
             "The supernormal powers"],
         "correct": 0,
         "expl": "An entirely different class of meditation subject from the ten kasinas."},
        {"q": "Where can a reader go for Chapter 5's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Nine more kasinas", [
            "completing the set",
            "of ten total",
        ]),
        ("Same method,", [
            "different preparation",
        ]),
        ("Water, fire, air,", [
            "four colors, light, space",
        ]),
        ("One destination", [
            "all ten can reach",
            "full absorption",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/anguttara-nikaya/an-8.65.html">AN 8.65 &mdash; '
        "Dimensions of Mastery</a> &mdash; the bases of mastery over form, closely "
        "tied to the color kasinas this chapter covers.",
        '<a href="../discourses/anguttara-nikaya/an-10.29.html">AN 10.29 &mdash; '
        "Kosala (1st)</a> &mdash; an ascending cosmological survey that names the "
        "kasinas directly among its later stages.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 6 -- Asubhakammaṭṭhānaniddesa
# --------------------------------------------------------------------------- #
page(
    6, "Asubhakammaṭṭhānaniddesa", "Foulness as a Meditation Subject",
    part=PART_2,
    meta_title="Visuddhimagga Ch. 6 — Foulness as a Meditation Subject | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 6 of the Visuddhimagga (The Path of "
        "Purification) — the ten stages of a decaying corpse as meditation subjects, "
        "their use as an antidote to the greedy temperament, practical cautions "
        "about charnel grounds, and a lower ceiling on absorption than the kasinas. "
        "No translated text reproduced; links to the full free translation and the "
        "Pali original. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter turns from the ten kasinas "
                    "just completed to an entirely different class of object"),
        ("Speaker", "Buddhaghosa, continuing the systematic survey of the forty "
                    "meditation subjects previewed in Chapter 3"),
        ("Form", "Ten distinct objects introduced together, paired with practical "
                 "guidance on obtaining and safely approaching such a sight, and a "
                 "note on the level of concentration this subject can reach"),
        ("Length", "moderate; shorter than Chapter 4, but includes practical and "
                   "safety guidance not present in the kasina chapters"),
        ("Northern parallel", "Contemplation of the body's impurity or decay appears "
                              "widely elsewhere in Buddhist meditation literature as "
                              "an antidote to bodily attachment; this guide does not "
                              "assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the subject "
                       "matter is vivid, though the chapter itself treats it in a "
                       "clinical, structured way"),
    ],
    why=(
        "Chapter 3 established that different meditation subjects suit different "
        "temperaments, and having just spent two chapters on the ten kasinas, "
        "Chapter 6 turns to a subject fitted to a specific situation those kasinas "
        "do not directly address: strong attachment to the body's apparent "
        "attractiveness. Ten stages of a corpse's visible decay are presented as a "
        "direct counterweight to that attachment, continuing the forty-subject "
        "survey into its next category while putting the temperament principle from "
        "Chapter 3 into concrete use."),
    guide=[
        ("Ten stages of decay", [
            "The chapter introduces foulness as ten separate meditation subjects, "
            "each a distinct stage of a corpse's visible decay: the bloated, the "
            "discolored, the festering, the cut-up, the gnawed, the scattered, the "
            "hacked-and-scattered, the bleeding, the worm-infested, and finally the "
            "bare skeleton. Each of the ten counts as its own entry among the forty "
            "subjects previewed in Chapter 3, not as variations of a single "
            "practice."]),
        ("An antidote for a specific temperament", [
            "The chapter connects this subject directly back to the sixfold typing "
            "of temperament from Chapter 3, presenting sustained, unflinching "
            "awareness of decay as a deliberate counterweight for a person whose "
            "attachment centers on the body's beauty. It is framed less as a "
            "universal prescription than as a targeted remedy for one particular "
            "kind of difficulty."]),
        ("Obtaining the sign", [
            "Unlike a kasina disk, which can simply be prepared at will, a subject "
            "like this depends on an actual opportunity to observe such a sight, "
            "traditionally at a charnel ground or similar site. The chapter treats "
            "this dependence on circumstance as a real practical difference from the "
            "kasinas, not a minor detail."]),
        ("Cautions and safeguards", [
            "The chapter is notably practical about the genuine dangers and "
            "disturbances such a setting can involve, addressing composure, caution, "
            "and safety as seriously as it addresses the meditative instruction "
            "itself &mdash; a level of real-world concern not called for by the "
            "kasinas."]),
        ("A different ceiling on absorption", [
            "Where Chapters 4 and 5 described all ten kasinas as capable of "
            "reaching full absorption, this chapter treats foulness differently: "
            "the vivid, repulsive nature of the object requires a degree of "
            "sustained applied thought that does not fully fall away the way it "
            "does with a kasina's counterpart sign, so foulness meditation is said "
            "to reach only the first level of jhāna, not the deeper levels the "
            "kasinas can produce."]),
        ("What follows", [
            "Chapter 7 turns to gentler ground: the first group of six "
            "recollections, beginning with recollection of the Buddha, the Dhamma, "
            "and the Sangha."]),
    ],
    terms=[
        ("asubha",
         "&ldquo;foulness&rdquo; &mdash; this chapter's subject, both the general "
         "meditation category and, individually, each of its ten forms."),
        ("uddhumātaka",
         "the bloated &mdash; the first of the ten stages of foulness."),
        ("aṭṭhika",
         "the skeleton &mdash; the tenth and final stage of foulness."),
        ("rāgacarita",
         "the greedy or lustful temperament, one of the six from Chapter 3, for "
         "which foulness is prescribed here as a direct antidote."),
        ("sīvathikā",
         "cemetery or charnel ground &mdash; the traditional setting in which such "
         "sights were directly observed."),
    ],
    quiz=[
        {"q": "Which temperament from Chapter 3 is foulness meditation specifically prescribed to counter?",
         "opts": [
             "The greedy or lustful temperament",
             "The hating temperament",
             "The deluded temperament",
             "The faithful temperament"],
         "correct": 0,
         "expl": "Presented as a direct counterweight to attachment centered on the body's apparent attractiveness."},
        {"q": "How many stages of foulness does this chapter describe?",
         "opts": [
             "Ten",
             "Four",
             "Six",
             "Forty"],
         "correct": 0,
         "expl": "Each stage counts as its own separate entry among the forty meditation subjects."},
        {"q": "What is the first of the ten stages of foulness?",
         "opts": [
             "The bloated",
             "The skeleton",
             "The worm-infested",
             "The bleeding"],
         "correct": 0,
         "expl": "Uddhumātaka, the earliest visible stage of decay in the chapter's sequence."},
        {"q": "What is the tenth and final stage of foulness?",
         "opts": [
             "The skeleton",
             "The bloated",
             "The festering",
             "The cut-up"],
         "correct": 0,
         "expl": "Aṭṭhika, the last of the ten stages the chapter describes."},
        {"q": "Where would a practitioner traditionally go to observe such a sight directly?",
         "opts": [
             "A charnel ground or cemetery",
             "A monastery's main shrine hall",
             "A riverbank at dawn",
             "Any private residence"],
         "correct": 0,
         "expl": "Unlike a kasina disk, this subject depends on an actual opportunity rather than a device prepared at will."},
        {"q": "What practical concern does the chapter address alongside the meditative instruction itself?",
         "opts": [
             "The genuine dangers and disturbances of approaching such a site, requiring composure and caution",
             "The cost of hiring assistants to prepare the site",
             "Obtaining formal government permission",
             "The chapter raises no practical concerns at all"],
         "correct": 0,
         "expl": "A level of real-world concern not called for by the kasinas."},
        {"q": "How does the ceiling on absorption for foulness meditation compare to that of the kasinas?",
         "opts": [
             "Foulness reaches only the first level of jhāna, while the kasinas can reach full, deeper absorption",
             "Foulness and the kasinas reach exactly the same depth of absorption",
             "Foulness reaches deeper absorption than any of the kasinas",
             "Neither foulness nor the kasinas can reach any level of jhāna"],
         "correct": 0,
         "expl": "The vivid, repulsive nature of the object keeps a degree of applied thought from fully dropping away."},
        {"q": "Why, per this chapter, can foulness meditation not proceed beyond the first jhāna?",
         "opts": [
             "The object's vivid, repulsive nature requires sustained applied thought that does not fully fall away",
             "The practice is considered too dangerous to continue past that point",
             "No teacher has ever demonstrated it going further",
             "The corpse itself decays too quickly for further practice"],
         "correct": 0,
         "expl": "Contrasted directly with the kasina's counterpart sign, where that same factor can fall away."},
        {"q": "What does Chapter 7 turn to next?",
         "opts": [
             "The first group of six recollections, including the Buddha, the Dhamma, and the Sangha",
             "The immaterial states",
             "The remaining kasinas",
             "The supernormal powers"],
         "correct": 0,
         "expl": "A gentler set of subjects following the vivid material of Chapter 6."},
        {"q": "Where can a reader go for Chapter 6's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("A different antidote", [
            "asubha &mdash; foulness,",
            "for the greedy temperament",
        ]),
        ("Ten stages of decay", [
            "from the bloated",
            "to the bare skeleton",
        ]),
        ("Real cautions", [
            "charnel-ground dangers",
            "addressed directly",
        ]),
        ("A lower ceiling", [
            "only the first jhāna,",
            "unlike the kasinas",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/majjhima-nikaya/mn-010.html">MN 10 &mdash; '
        "Mindfulness Meditation</a> &mdash; the canon's most comprehensive source "
        "on contemplative training, including charnel-ground observation.",
        '<a href="../discourses/majjhima-nikaya/mn-119.html">MN 119</a> &mdash; a '
        "discourse centered on mindfulness of the body, closely related in theme to "
        "this chapter's subject.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 7 -- Chaanussatiniddesa
# --------------------------------------------------------------------------- #
page(
    7, "Chaanussatiniddesa", "Six Recollections",
    part=PART_2,
    meta_title="Visuddhimagga Ch. 7 — Six Recollections | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 7 of the Visuddhimagga (The Path of "
        "Purification) — recollection of the Buddha, the Dhamma, the Sangha, one's "
        "own virtue, one's own generosity, and the qualities of deities, and why "
        "these six reach confidence rather than full absorption. No translated text "
        "reproduced; links to the full free translation and the Pali original. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter turns from the vivid material "
                    "of Chapter 6 to a structurally different group of subjects"),
        ("Speaker", "Buddhaghosa, continuing the survey of the forty meditation "
                    "subjects previewed in Chapter 3"),
        ("Form", "Six related recollections treated in turn, each built on a set of "
                 "qualities to be called to mind rather than a fixed visual object"),
        ("Length", "substantial; the recollections of the Buddha, the Dhamma, and "
                   "the Sangha each carry an extended traditional formula of "
                   "qualities explored individually"),
        ("Northern parallel", "Recollection of the Three Jewels appears widely "
                              "across Buddhist traditions in some form, though "
                              "specific formulas and expansions differ; this guide "
                              "does not assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; conceptually "
                       "accessible, though the catalogued qualities of the Buddha "
                       "and the Dhamma are numerous"),
    ],
    why=(
        "Chapters 4 through 6 covered subjects built on a single object &mdash; a "
        "kasina disk, a corpse's visible decay. Chapter 7 introduces something "
        "structurally different: recollections built on calling to mind a set of "
        "qualities rather than fixing attention on one simple sign. These particular "
        "six are grouped together because each works by recalling something worthy "
        "of confidence &mdash; the Buddha, the Dhamma, the Sangha, one's own virtue, "
        "one's own generosity, or the qualities that account for a deity's state "
        "&mdash; and each is presented as especially suited to a person of faithful "
        "or devoted temperament."),
    guide=[
        ("A different kind of object", [
            "Where a kasina rests attention on a single visual sign, each of these "
            "six recollections works by calling to mind a whole set of qualities in "
            "turn. This difference in structure matters later in the chapter, when "
            "it becomes the reason given for why these six reach a different depth "
            "of concentration than several of the kasinas."]),
        ("Recollection of the Buddha", [
            "The first recollection has a practitioner call to mind a traditional "
            "formula of the Buddha's qualities &mdash; among them being worthy, "
            "fully self-awakened, and accomplished in both knowledge and conduct "
            "&mdash; reflecting on each in turn as grounds for settled confidence."]),
        ("Recollection of the Dhamma", [
            "The second recollection turns to qualities traditionally attributed to "
            "the teaching itself: that it is well-expounded, visible in the present, "
            "not delayed in its results, inviting inspection, and to be experienced "
            "individually by the wise."]),
        ("Recollection of the Sangha", [
            "The third recollection reflects on qualities of the community of "
            "accomplished practitioners &mdash; that they practice the good way, "
            "are worthy of hospitality and offerings, and constitute what the "
            "tradition calls an unsurpassed field for cultivating merit."]),
        ("Recollection of one's own virtue and generosity", [
            "The fourth and fifth recollections turn the same reflective method "
            "inward: recalling one's own unbroken and unblemished conduct, and "
            "recalling one's own history of giving, each as grounds for confidence "
            "rather than self-congratulation."]),
        ("Recollection of deities", [
            "The sixth recollection reflects on the qualities said to account for a "
            "deity's favorable state &mdash; faith, virtue, learning, generosity, "
            "and wisdom &mdash; but the chapter frames its actual purpose as using "
            "that reflection as a kind of mirror, checking whether one possesses "
            "those same qualities oneself, rather than as devotion to deities as "
            "such."]),
        ("Confidence, not absorption", [
            "Because each of these six objects is a set of qualities rather than a "
            "single simple sign, the chapter treats all six as capable of bringing "
            "the mind to a settled confidence and access concentration, but not to "
            "the fuller absorption several of the kasinas were said to reach in "
            "Chapters 4 and 5."]),
        ("What follows", [
            "Chapter 8 completes the set of ten recollections with four more: "
            "death, the body, the breath, and peace &mdash; broadening the range of "
            "objects this same reflective approach can be applied to."]),
    ],
    terms=[
        ("anussati",
         "&ldquo;recollection&rdquo; &mdash; the class of ten subjects this chapter "
         "and the next cover; Chapter 7 treats the first six."),
        ("Buddhānussati",
         "recollection of the Buddha &mdash; reflecting on a traditional formula of "
         "his qualities."),
        ("Dhammānussati",
         "recollection of the Dhamma &mdash; reflecting on qualities traditionally "
         "attributed to the teaching itself."),
        ("Saṅghānussati",
         "recollection of the Sangha &mdash; reflecting on qualities of the "
         "community of accomplished practitioners."),
        ("sīlānussati, cāgānussati, devatānussati",
         "recollection of one's own virtue, one's own generosity, and the qualities "
         "of deities &mdash; the chapter's remaining three recollections."),
    ],
    quiz=[
        {"q": "How do the six recollections in this chapter differ structurally from a kasina?",
         "opts": [
             "They rest on a set of qualities called to mind, rather than a single fixed visual sign",
             "They require no mental effort of any kind",
             "They can only be practiced in a charnel ground",
             "They are identical in structure to a kasina, only differently colored"],
         "correct": 0,
         "expl": "This difference becomes the chapter's reason for their different ceiling on concentration."},
        {"q": "Which temperament from Chapter 3 do these six recollections particularly suit?",
         "opts": [
             "The faithful or devoted temperament",
             "The hating temperament",
             "The deluded temperament",
             "The speculative temperament"],
         "correct": 0,
         "expl": "Each works by calling to mind something worthy of confidence."},
        {"q": "What is recollection of the Buddha built on?",
         "opts": [
             "A traditional formula of the Buddha's qualities, such as being worthy and fully self-awakened",
             "A single visual image of the Buddha only",
             "A physical relic that must be present",
             "Silent repetition of the Buddha's name alone"],
         "correct": 0,
         "expl": "Each quality is reflected on in turn as grounds for settled confidence."},
        {"q": "What is recollection of the Dhamma built on?",
         "opts": [
             "Qualities traditionally attributed to the teaching, such as being well-expounded and visible in the present",
             "Memorizing every discourse word for word",
             "A vow never to question the teaching",
             "The physical books the teaching is written in"],
         "correct": 0,
         "expl": "Including that it invites inspection and is to be experienced individually by the wise."},
        {"q": "What do recollection of virtue and recollection of generosity turn attention toward?",
         "opts": [
             "One's own unbroken conduct and one's own history of giving",
             "The virtue and generosity of a specific named teacher only",
             "Rules one has not yet learned",
             "Wealth one hopes to acquire in the future"],
         "correct": 0,
         "expl": "Each is treated as grounds for confidence rather than self-congratulation."},
        {"q": "What does the chapter say recollection of deities is actually for?",
         "opts": [
             "Using deities' qualities as a mirror to check whether one possesses the same qualities oneself",
             "Securing direct favors and protection from deities",
             "Proving that deities do not really exist",
             "Preparing to be reborn as a deity as quickly as possible"],
         "correct": 0,
         "expl": "Framed as a check on one's own faith, virtue, learning, generosity, and wisdom, not devotion to devas as such."},
        {"q": "What depth of concentration does the chapter say all six recollections here can reach?",
         "opts": [
             "Access concentration and settled confidence, but not full absorption",
             "Full absorption through all four jhānas, exactly like the kasinas",
             "No concentration at all; they are purely intellectual exercises",
             "A depth beyond even the kasinas'"],
         "correct": 0,
         "expl": "Contrasted with several of the kasinas from Chapters 4 and 5."},
        {"q": "Why can't these six recollections reach full absorption, per the chapter's account?",
         "opts": [
             "Each object is a set of multiple qualities rather than one single, simple sign",
             "They are considered too easy to require full absorption",
             "The Buddha explicitly forbade absorption on these subjects",
             "They can only be practiced for a few minutes at a time"],
         "correct": 0,
         "expl": "The same structural difference noted early in the chapter becomes the reason given here."},
        {"q": "What does Chapter 8 add to complete the set of ten recollections?",
         "opts": [
             "Death, the body, the breath, and peace",
             "Four more kasinas",
             "Four more stages of foulness",
             "The four divine abidings"],
         "correct": 0,
         "expl": "Broadening the range of objects the same reflective approach can be applied to."},
        {"q": "Where can a reader go for Chapter 7's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("A different kind of object", [
            "qualities reflected on,",
            "not a visual sign",
        ]),
        ("The Triple Gem", [
            "Buddha, Dhamma,",
            "and Sangha",
        ]),
        ("Turning inward, and beyond", [
            "virtue, generosity,",
            "and the qualities of deities",
        ]),
        ("Confidence, not absorption", [
            "access concentration only,",
            "unlike several kasinas",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/anguttara-nikaya/an-6.10.html">AN 6.10 &mdash; With '
        "Mahānāma</a> &mdash; the Buddha's own full expansion of the six "
        "recollections this chapter treats.",
        '<a href="../discourses/anguttara-nikaya/an-6.25.html">AN 6.25 &mdash; '
        "Topics for Recollection</a> &mdash; a further discourse on the same six "
        "recollections, closing on how they purify a mind of greed.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 8 -- Anussatikammaṭṭhānaniddesa (dutiya)
# --------------------------------------------------------------------------- #
page(
    8, "Anussatikammaṭṭhānaniddesa", "Other Recollections",
    part=PART_2,
    meta_title="Visuddhimagga Ch. 8 — Other Recollections | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 8 of the Visuddhimagga (The Path of "
        "Purification) — recollection of death, mindfulness occupied with the body, "
        "mindfulness of breathing, and recollection of peace, and why breathing "
        "alone among them reaches full absorption. No translated text reproduced; "
        "links to the full free translation and the Pali original. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter completes the ten "
                    "recollections begun in Chapter 7"),
        ("Speaker", "Buddhaghosa, continuing the survey of the forty meditation "
                    "subjects previewed in Chapter 3"),
        ("Form", "Four subjects treated in sequence, markedly different in "
                 "character from one another despite belonging to the same "
                 "traditional category"),
        ("Length", "one of the longest chapters in the work, since mindfulness of "
                   "breathing and mindfulness occupied with the body each receive "
                   "extended, detailed treatment"),
        ("Northern parallel", "Recollection of death, contemplation of the body's "
                              "parts, and mindfulness of breathing all appear widely "
                              "across Buddhist meditation literature; this guide "
                              "does not assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; four fairly "
                       "distinct subjects covered in one chapter, with breathing's "
                       "detailed step scheme the most technical material so far"),
    ],
    why=(
        "Chapter 7 covered six of the traditional ten recollections; this chapter "
        "completes the set with the remaining four &mdash; death, the body, "
        "breathing, and peace. Despite sharing the recollection label, these four "
        "differ from each other more than the six in Chapter 7 did from one "
        "another, and one of them, mindfulness of breathing, breaks the pattern set "
        "in the previous chapter entirely by reaching all the way to full "
        "absorption. The chapter is worth reading as much for that contrast as for "
        "the four techniques themselves."),
    guide=[
        ("Four subjects, one chapter", [
            "The chapter groups recollection of death, mindfulness occupied with "
            "the body, mindfulness of breathing, and recollection of peace together "
            "because, along with Chapter 7's six, they complete the traditional "
            "list of ten recollections &mdash; not because the four themselves are "
            "especially alike. Their character, difficulty, and depth of "
            "concentration all differ considerably."]),
        ("Recollection of death", [
            "This recollection has a practitioner reflect on death's certainty and "
            "its unpredictable timing, using any of several traditional approaches "
            "&mdash; among them, reflecting on how death spares no one regardless of "
            "status or achievement, and reflecting on the body's fragility. The "
            "intended effect is a sense of spiritual urgency rather than morbid "
            "fear, and like most of Chapter 7's recollections, this one is said to "
            "reach only access concentration, given the weight of its object."]),
        ("Mindfulness occupied with the body", [
            "This subject has a practitioner mentally divide the body into some "
            "thirty-two anatomical parts &mdash; hair, nails, teeth, skin, sinews, "
            "bones, and so on &mdash; reflecting on each in turn. Its purpose runs "
            "parallel to Chapter 6's foulness meditation: undermining an "
            "unexamined sense of the body as attractive or as a single, unified "
            "self, but applied to the living body rather than to a corpse's visible "
            "decay."]),
        ("Mindfulness of breathing", [
            "Traditionally regarded as the most highly praised of all forty "
            "subjects, this recollection is set out through a detailed sixteen-step "
            "scheme organized into four groups of four: attending first to the "
            "breath itself (its length, the whole body of breathing, its "
            "calming), then to rapture and happiness arising with it, then to the "
            "state of mind itself, and finally to impermanence and letting go as "
            "objects of contemplation built on that same steady attention to "
            "breathing."]),
        ("Why breathing stands apart", [
            "Unlike the six recollections of Chapter 7 and the death and peace "
            "recollections here, mindfulness of breathing is described as capable "
            "of reaching full absorption through all four levels of jhāna, on par "
            "with the kasinas. The chapter attributes this to breathing's nature as "
            "a single, continuously present physical process, rather than a "
            "complex set of qualities to be called to mind in sequence."]),
        ("Recollection of peace", [
            "The final recollection reflects on the qualities of Nibbāna itself as "
            "the cessation of suffering. Like most of this chapter's other "
            "subjects, it is said to reach only access concentration, its object "
            "being too profound for full absorption to be reached by reflecting on "
            "it indirectly, prior to its direct realization."]),
        ("What follows", [
            "Chapter 9 turns to the four divine abidings &mdash; loving-kindness, "
            "compassion, appreciative joy, and equanimity &mdash; each capable, like "
            "several of the kasinas and mindfulness of breathing, of reaching a "
            "deep level of absorption."]),
    ],
    terms=[
        ("maraṇānussati",
         "recollection of death &mdash; reflecting on death's certainty and "
         "unpredictable timing, meant to cultivate a sense of urgency."),
        ("kāyagatāsati",
         "mindfulness occupied with the body &mdash; reflecting in turn on some "
         "thirty-two anatomical parts, undermining the body's apparent "
         "attractiveness."),
        ("ānāpānassati",
         "mindfulness of breathing &mdash; traditionally the most highly praised of "
         "the forty subjects, and the only recollection in this chapter capable of "
         "reaching full absorption."),
        ("upasamānussati",
         "recollection of peace &mdash; reflecting on the qualities of Nibbāna as "
         "the cessation of suffering."),
        ("saṃvega",
         "a sense of spiritual urgency &mdash; the quality recollection of death is "
         "meant to cultivate, distinct from ordinary fear."),
    ],
    quiz=[
        {"q": "What four subjects does this chapter cover?",
         "opts": [
             "Death, the body, breathing, and peace",
             "The four kasinas of color",
             "The four divine abidings",
             "The four immaterial states"],
         "correct": 0,
         "expl": "Completing the traditional list of ten recollections begun in Chapter 7."},
        {"q": "What is recollection of death meant to cultivate?",
         "opts": [
             "Saṃvega, a sense of spiritual urgency, rather than morbid fear",
             "Complete indifference to all future events",
             "A detailed prediction of one's own death date",
             "Anger at the inevitability of death"],
         "correct": 0,
         "expl": "Reflecting on death's certainty and unpredictable timing."},
        {"q": "What technique does mindfulness occupied with the body use?",
         "opts": [
             "Mentally dividing the body into some thirty-two anatomical parts, reflected on in turn",
             "Observing the body's reflection in a mirror",
             "Fasting until the body's structure becomes visible",
             "Measuring the body's exact weight and height"],
         "correct": 0,
         "expl": "Hair, nails, teeth, skin, sinews, bones, and so on."},
        {"q": "What is mindfulness occupied with the body meant to undermine?",
         "opts": [
             "An unexamined sense of the body as attractive or as a single, unified self",
             "The ability to walk and move normally",
             "Trust in one's teacher",
             "The five hindrances specifically, and nothing else"],
         "correct": 0,
         "expl": "Its purpose runs parallel to Chapter 6's foulness meditation, applied to the living body."},
        {"q": "How is mindfulness of breathing traditionally regarded among the forty meditation subjects?",
         "opts": [
             "As the most highly praised of all forty",
             "As the least effective of all forty",
             "As forbidden for beginners",
             "As identical in every respect to the earth kasina"],
         "correct": 0,
         "expl": "Set out through a detailed sixteen-step scheme in this chapter."},
        {"q": "How is mindfulness of breathing's method organized?",
         "opts": [
             "A sixteen-step scheme organized into four groups of four",
             "A single step repeated sixteen times identically",
             "Two steps only: inhaling and exhaling",
             "Forty steps, one for each meditation subject"],
         "correct": 0,
         "expl": "Moving from the breath itself, through rapture and happiness, to the mind, and finally to impermanence and letting go."},
        {"q": "What makes mindfulness of breathing unique among this chapter's four subjects?",
         "opts": [
             "It alone is described as capable of reaching full absorption through all four jhānas",
             "It alone requires no sustained attention",
             "It alone cannot be practiced by monastics",
             "It alone was added to the canon after Buddhaghosa's time"],
         "correct": 0,
         "expl": "Attributed to breathing's nature as a single, continuously present physical process."},
        {"q": "What does recollection of peace reflect on, and what is its ceiling on concentration?",
         "opts": [
             "The qualities of Nibbāna as the cessation of suffering; access concentration only",
             "The qualities of a peaceful afternoon; full absorption",
             "The absence of any object whatsoever; no concentration at all",
             "The qualities of a specific historical peace treaty"],
         "correct": 0,
         "expl": "Its object is described as too profound for full absorption to be reached indirectly."},
        {"q": "What does Chapter 9 turn to next?",
         "opts": [
             "The four divine abidings: loving-kindness, compassion, appreciative joy, and equanimity",
             "The immaterial states",
             "The supernormal powers",
             "The remaining kasinas"],
         "correct": 0,
         "expl": "Several of which are also capable, like mindfulness of breathing, of reaching deep absorption."},
        {"q": "Where can a reader go for Chapter 8's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Four different subjects", [
            "death, the body,",
            "breathing, and peace",
        ]),
        ("Completing the ten", [
            "with Chapter 7's six,",
            "the full recollection set",
        ]),
        ("Thirty-two parts", [
            "undermining the body's",
            "apparent attractiveness",
        ]),
        ("Breathing stands apart", [
            "the one recollection here",
            "reaching full absorption",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/majjhima-nikaya/mn-118.html">MN 118 &mdash; '
        "Mindfulness of Breathing</a> &mdash; the canonical source discourse for "
        "the sixteen-step scheme this chapter details.",
        '<a href="../discourses/majjhima-nikaya/mn-119.html">MN 119</a> &mdash; a '
        "discourse centered on mindfulness of the body, directly relevant to this "
        "chapter's thirty-two-parts technique.",
    ],
)
