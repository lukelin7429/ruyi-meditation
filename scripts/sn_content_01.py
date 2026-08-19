# -*- coding: utf-8 -*-
"""Sagāthāvagga — The Book with Verses (SN 1–11). One discourse per page."""

SC = "https://suttacentral.net"

INDEX_HEADING = "I. Sagāthāvagga — The Book with Verses"
# SN 1.1, SN 3.25, and SN 6.1 were published before this series began working
# in order, in the earlier twenty-page selection; they are listed in the
# index by INDEX_EXTRA and are not generated here. Systematic coverage of
# this book starts at SN 1.2, the first discourse not already published.
# HEAD is "./" (this is the first module of the whole Saṃyutta Nikāya). TAIL
# points at the nearest already-published page beyond this book -- SN 12.1,
# from the same earlier selection -- until a sn_content_02 module exists for
# the Nidānavagga and TAIL can move to its own first page.
HEAD = ("./", "Saṃyutta Nikāya selections")
TAIL = ("sn-12.1.html", "SN 12.1 &middot; Dependent Origination")
INDEX_EXTRA = [
    ("sn-1.1", "Oghataraṇa", "Crossing the Flood"),
    ("sn-3.25", "Pabbatūpama", "The Simile of the Mountain"),
    ("sn-6.1", "Āyācana", "The Appeal of the Divinity"),
]

PAGES = []


def page(samyutta, num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Sagāthāvagga.

    Unlike the Aṅguttara content modules, one Saṃyutta Nikāya book spans
    several independently numbered saṃyuttas (SN 1.1..., SN 2.1..., SN
    3.1..., not one flat number space), so both the saṃyutta and the
    discourse number are required.
    """
    d = {
        "slug": "sn-%d.%d" % (samyutta, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "sn%d/sn%d.%d" % (samyutta, samyutta, num),
        "crumb": "SN %d.%d" % (samyutta, num),
        "number_line": "Saṃyutta Nikāya &middot; Discourse %d.%d" % (samyutta, num),
        "title": title,
        "subtitle": "<em>%ssutta</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# SN 1.2 — Nimokkhasutta
# --------------------------------------------------------------------------- #
page(
    1, 2, "Nimokkha", "Liberation",
    meta_title="SN 1.2 — Liberation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nimokkhasutta — a "
        "deity's question about liberation, answered in a compact three-line verse naming "
        "the end of relish for rebirth, the finishing of perception and consciousness, and "
        "the stilling of feeling. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove, late at night; the same "
                    "circumstances as SN 1.1"),
        ("Speakers", "The Buddha and an unnamed, radiant deity"),
        ("Form", "A three-part riddle-and-answer exchange in prose, closed with a compact "
                 "verse naming three causes"),
        ("Length", "~1.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the Chinese Saṃyukta-āgama "
                              "(T99), though this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, but the closing "
                       "verse compresses three separate technical claims into three lines"),
    ],
    why=(
        "A deity asks the Buddha, twice over, whether he knows the liberation, emancipation, "
        "and seclusion of sentient beings &mdash; first whether he knows it at all, then how "
        "he knows it. The answer, given in verse, names three specific causes: the ending of "
        "relish for rebirth, the finishing of perception and consciousness, and the cessation "
        "and stilling of feelings. Three of the five aggregates &mdash; perception, "
        "consciousness, and feeling &mdash; already appear here, in the second discourse of "
        "the entire collection, well before any discourse devoted to the aggregates as a "
        "topic in their own right."),
    guide=[
        ("A question asked twice, then answered once", [
            "The deity's exchange follows a three-step pattern already used at SN 1.1: a "
            "first question asking simply whether the Buddha knows a thing, a second "
            "confirming that he does, and a third asking how &mdash; which the Buddha answers "
            "directly, in verse, without further prompting."]),
        ("Three technical terms, closely related", [
            "<em>Nimokkha</em>, <em>pamokkha</em>, and <em>viveka</em> &mdash; liberation, "
            "emancipation, and seclusion &mdash; are named together as a set, without being "
            "distinguished from one another in this discourse. The verse answer addresses "
            "all three at once, as a single achievement rather than three separate ones."]),
        ("Three causes, three aggregates", [
            "The verse names three specific causes: the ending of relish for continued "
            "existence (<em>nandībhavaparikkhaya</em>), the finishing of perception and "
            "consciousness (<em>saññāviññāṇasaṅkhaya</em>), and the cessation and stilling of "
            "feelings (<em>vedanānaṁ nirodhā upasamā</em>). Perception, consciousness, and "
            "feeling are three of the five aggregates (<em>khandha</em>) that later become "
            "this collection's own dedicated subject in its third book, the Khandhavagga."]),
        ("A verse, not further prose explanation", [
            "Unlike a discourse that might unpack each of these three causes in prose, this "
            "one simply states them, compressed into four lines of verse, and ends. Nothing "
            "in the text explains what &lsquo;finishing perception and consciousness&rsquo; "
            "or &lsquo;stilling feelings&rsquo; concretely involves; the deity asks no further "
            "question, and none is offered unprompted."]),
        ("A shape this book's opening chapter repeats", [
            "This same short question-and-answer shape, closed by a compact verse, recurs "
            "across the Naḷavagga, the first sub-chapter of the Devatāsaṃyutta this discourse "
            "belongs to &mdash; the same &lsquo;deity approaches, asks, is answered&rsquo; "
            "frame already met at SN 1.1, now applied to a different subject."]),
    ],
    terms=[
        ("nimokkha, pamokkha, viveka",
         "liberation, emancipation, and seclusion &mdash; three closely related terms named "
         "together as a single achievement in this discourse's question."),
        ("nandībhavaparikkhaya",
         "&ldquo;the ending of relish for rebirth&rdquo; &mdash; the first of the verse's "
         "three named causes."),
        ("saññāviññāṇasaṅkhaya",
         "&ldquo;the finishing of perception and consciousness&rdquo; &mdash; the second "
         "cause, naming two of the five aggregates directly."),
        ("vedanānaṁ nirodhā upasamā",
         "&ldquo;the cessation and stilling of feelings&rdquo; &mdash; the third cause, "
         "naming a third aggregate."),
        ("khandha",
         "&ldquo;aggregate&rdquo; &mdash; perception, consciousness, and feeling, three of "
         "the five aggregates, appear here well before this collection's own dedicated book "
         "on the subject."),
    ],
    text_intro=(
        "The discourse in full: a deity's question, asked twice, answered once in verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.2:1.1-1.2"),
        ("p", "&sect;2", "sn1.2:2.1-2.1"),
        ("p", "&sect;3", "sn1.2:3.1-3.1"),
        ("p", "&sect;4", "sn1.2:4.1-4.1"),
        ("p", "&sect;5", "sn1.2:5.1-5.5"),
    ],
    quiz=[
        {"q": "What three things does the deity ask the Buddha about?",
         "opts": [
             "Liberation, emancipation, and seclusion of sentient beings",
             "The five aggregates",
             "The four noble truths",
             "The eightfold path"],
         "correct": 0,
         "expl": "Nimokkha, pamokkha, viveka &mdash; named together as a single question."},
        {"q": "What pattern does this exchange follow, already used at SN 1.1?",
         "opts": [
             "A question asking whether the Buddha knows a thing, confirmation that he does, then a question asking how",
             "A long philosophical debate spanning many exchanges",
             "A silent gesture with no words exchanged",
             "A question the Buddha refuses to answer"],
         "correct": 0,
         "expl": "The same three-step shape recurs across this sub-chapter."},
        {"q": "What three causes does the closing verse name?",
         "opts": [
             "Ending relish for rebirth, finishing perception and consciousness, and stilling feelings",
             "The five precepts",
             "The four right efforts",
             "Faith, energy, mindfulness, immersion, and wisdom"],
         "correct": 0,
         "expl": "Three separate technical claims compressed into four lines of verse."},
        {"q": "How many of the five aggregates (khandha) does this verse name directly?",
         "opts": [
             "Three: perception, consciousness, and feeling",
             "All five",
             "None; the aggregates are not mentioned at all",
             "Only one"],
         "correct": 0,
         "expl": "Well before this collection's own dedicated book on the aggregates."},
        {"q": "Does this discourse explain in prose what 'finishing perception and consciousness' concretely involves?",
         "opts": [
             "No &mdash; the verse simply states the three causes and the discourse ends",
             "Yes, in extensive detail across several paragraphs",
             "Yes, but only in a footnote",
             "The discourse asks a follow-up question to clarify this itself"],
         "correct": 0,
         "expl": "No further question is asked, and none is offered unprompted."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove, late at night &mdash; the same circumstances as SN 1.1",
             "On a mountaintop at dawn",
             "In a different city entirely from SN 1.1",
             "No setting is given"],
         "correct": 0,
         "expl": "Identical circumstances to the discourse immediately preceding it."},
        {"q": "Who are the two speakers in this discourse?",
         "opts": [
             "The Buddha and an unnamed, radiant deity",
             "Two named mendicants",
             "The Buddha and a king",
             "A deity speaking alone, with no reply from the Buddha"],
         "correct": 0,
         "expl": "The deity asks; the Buddha answers, twice."},
        {"q": "What sub-chapter of the Devatāsaṃyutta does this discourse belong to?",
         "opts": [
             "The Naḷavagga",
             "The Nidānavagga",
             "The Khandhavagga",
             "This discourse belongs to no sub-chapter"],
         "correct": 0,
         "expl": "Named directly in the Pali source's own heading."},
        {"q": "What does 'khandha' mean?",
         "opts": [
             "'Aggregate' &mdash; the topic this collection later devotes an entire book to",
             "'Liberation'",
             "'A deity'",
             "'Verse'"],
         "correct": 0,
         "expl": "Three of the five aggregates appear by name in this discourse's closing verse."},
        {"q": "What form does the Buddha's final answer take?",
         "opts": [
             "A compact four-line verse",
             "A long prose explanation",
             "A single-word answer",
             "A refusal to answer"],
         "correct": 0,
         "expl": "Compressing three separate causes into four lines."},
    ],
    marginalia=[
        ("Three terms, one question", [
            "nimokkha, pamokkha,",
            "viveka &mdash; asked as one",
        ]),
        ("Three causes, in verse", [
            "ending relish for rebirth,",
            "finishing perception &amp; consciousness,",
        ]),
        ("Aggregates, early", [
            "perception, consciousness, feeling",
            "&mdash; three of the five khandha",
        ]),
        ("A pattern repeating", [
            "the same question-shape",
            "as SN 1.1, this sub-chapter",
        ]),
    ],
    further=[
        '<a href="%s/sn1.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; the previous '
        "discourse in this collection, and this same question-and-answer shape&rsquo;s first "
        "appearance.",
        '<a href="sn-22.1.html">SN 22.1 &middot; Nakula&rsquo;s Father</a> &mdash; this '
        "collection&rsquo;s own book devoted to the five aggregates this verse names three "
        "of.",
        '<a href="sn-3.25.html">SN 3.25 &middot; The Simile of the Mountain</a> &mdash; the '
        "next discourse in this book&rsquo;s currently published selection.",
    ],
)
