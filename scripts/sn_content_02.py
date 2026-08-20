# -*- coding: utf-8 -*-
"""Nidānavagga — The Book of Causation (SN 12–21). One discourse per page,
with merged pages for the heaviest peyyāla (formula-repetition) ranges."""

SC = "https://suttacentral.net"

INDEX_HEADING = "II. Nidānavagga — The Book of Causation"
# SN 12.1, 12.2, 12.15, 12.61, and 12.65 (Nidānasaṃyutta) and SN 15.3
# (Anamataggasaṃyutta) were published before this series began working in
# order, in the earlier twenty-page selection; they are listed in the index
# by INDEX_EXTRA and are not generated here. Systematic coverage of this
# book starts at SN 12.3, the first discourse of Buddhavagga not already
# published. HEAD is the nearest already-published page immediately before
# this module's first new page (SN 12.2). TAIL points at the nearest
# already-published page beyond whatever this module currently covers --
# moved forward as later vaggas are completed, exactly as sn_content_01.py's
# TAIL was moved across the course of Book I.
HEAD = ("sn-12.2.html", "SN 12.2 &middot; Analysis")
TAIL = ("sn-12.61.html", "SN 12.61 &middot; Unlearned")
# SN 12.15 (Kaccānagotta) is a pre-existing page sitting between this
# module's SN 12.14 and SN 12.16 (confirmed by Āhāravagga's own closing
# uddāna, which lists it fifth of ten); it is not itself in PAGES, so
# sn_build.py's auto-chain naturally skips over it when linking 12.14 to
# 12.16. As with sn_content_01.py's INDEX_EXTRA nav-link fragility, the
# three-way junction at 12.14/12.15/12.16 needs a one-time manual nav fix
# after each build that touches this stretch.
INDEX_EXTRA = [
    ("sn-12.1", "Paṭiccasamuppāda", "Dependent Origination"),
    ("sn-12.2", "Vibhaṅga", "Analysis"),
    ("sn-12.15", "Kaccānagotta", "Kaccānagotta"),
    ("sn-12.61", "Assutavā", "Unlearned"),
    ("sn-12.65", "Nagara", "The City"),
    ("sn-15.3", "Assu", "Tears"),
]

PAGES = []


def page(samyutta, num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Nidānavagga.

    Same two-parameter signature as sn_content_01.py's page() (samyutta,
    then discourse number), since this book spans several independently
    numbered saṃyuttas (SN 12, 13, 14...) just as Book I did.
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


def page_range(samyutta, lo, hi, pali, title, **kw):
    """Scaffolding for a single page covering a merged range of discourse
    numbers (a peyyāla block bilara-data itself stores as one file, e.g.
    'sn12.72-81'). Mirrors AN's an-1.1-10-style merged pages."""
    d = {
        "slug": "sn-%d.%d-%d" % (samyutta, lo, hi),
        "index_pali": pali,
        "nav_title": title,
        "source": "sn%d/sn%d.%d-%d" % (samyutta, samyutta, lo, hi),
        "crumb": "SN %d.%d&ndash;%d" % (samyutta, lo, hi),
        "number_line": "Saṃyutta Nikāya &middot; Discourses %d.%d&ndash;%d" % (samyutta, lo, hi),
        "title": title,
        "subtitle": "<em>%ssutta</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
# --------------------------------------------------------------------------- #
# SN 12.3 — Paṭipadāsutta
# --------------------------------------------------------------------------- #
page(
    12, 3, "Paṭipadā", "Practice",
    meta_title="SN 12.3 — Practice | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭipadāsutta — dependent origination in forward order "
        "named as the wrong practice, and in reverse order as the "
        "right practice. Opens Buddhavagga's third discourse. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A short, direct teaching restating the same "
                 "twelve-link formula already given in SN 12.1 and "
                 "SN 12.2, now given ethical names"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but assumes familiarity with the "
                       "twelve-link chain from SN 12.1&ndash;2"),
    ],
    why=(
        "Having already laid out the twelve-link chain of dependent "
        "origination in SN 12.1 and analyzed each of its links in SN "
        "12.2, this discourse does something different: it gives the "
        "chain's two directions ethical names. Running the chain "
        "forward &mdash; ignorance conditioning choices, choices "
        "conditioning consciousness, and onward to the arising of "
        "the whole mass of suffering &mdash; is called the wrong "
        "practice. Running it in reverse, so that each link's "
        "cessation brings about the next link's cessation, is called "
        "the right practice. A teaching that could otherwise read as "
        "abstract metaphysics is reframed here as a direct, personal "
        "choice between two ways of living."),
    guide=[
        ("A restatement, not a new formula", [
            "This discourse doesn't introduce new content; it assumes "
            "the reader already knows the twelve-link chain from SN "
            "12.1 and SN 12.2, and the middle of the chain is elided "
            "here exactly as the source elides it, trusting that "
            "context."]),
        ("Two directions, two ethical labels", [
            "Rather than simply describing arising and cessation as "
            "neutral processes, the discourse names them directly "
            "&mdash; the forward direction is called wrong practice, "
            "the reverse direction right practice &mdash; turning a "
            "descriptive formula into a normative one."]),
        ("Complete cessation, not mere absence", [
            "The description of the right practice doesn't simply say "
            "ignorance ends; it specifies that ignorance fades away "
            "and ceases with no residue left behind, a stronger claim "
            "than temporary absence or suppression."]),
        ("A whole mass, not a single event", [
            "Both directions of the formula close on the same phrase "
            "&mdash; this entire mass of suffering &mdash; framing "
            "suffering not as an isolated occurrence but as something "
            "built up link by link, and capable of being dismantled "
            "the same way."]),
        ("A compact bridge within a longer chapter", [
            "Positioned between SN 12.2's detailed analysis and SN "
            "12.4's extended narrative of past Buddhas rediscovering "
            "the same chain, this short discourse functions as a "
            "hinge, restating the formula's stakes before the chapter "
            "moves into its longer material."]),
    ],
    terms=[
        ("micchāpaṭipadā",
         "&ldquo;wrong practice&rdquo; &mdash; the ethical name given "
         "to running the chain forward, from ignorance to suffering."),
        ("sammāpaṭipadā",
         "&ldquo;right practice&rdquo; &mdash; the ethical name given "
         "to running the chain in reverse, from ignorance's cessation "
         "to suffering's cessation."),
        ("avijjāpaccayā saṅkhārā",
         "&ldquo;ignorance is a requirement for choices&rdquo; "
         "&mdash; the chain's first link, standing in here for the "
         "full formula already given in SN 12.1&ndash;2."),
        ("asesavirāganirodhā",
         "&ldquo;fades away and ceases with no residue left "
         "behind&rdquo; &mdash; specifying complete cessation, not "
         "temporary absence."),
        ("kevalassa dukkhakkhandhassa",
         "&ldquo;this entire mass of suffering&rdquo; &mdash; the "
         "recurring closing phrase for both directions, framing "
         "suffering as something built up and capable of being "
         "dismantled."),
    ],
    text_intro=(
        "The discourse in full. The middle of the twelve-link chain "
        "is elided in the source, exactly as bilara-data preserves "
        "it, trusting the reader's familiarity with SN 12.1&ndash;2. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.3:1.1-1.5"),
        ("p", "&sect;2", "sn12.3:2.1-2.5"),
        ("p", "&sect;3", "sn12.3:3.1-3.5"),
    ],
    quiz=[
        {"q": "What does this discourse do with the twelve-link chain already given in SN 12.1 and SN 12.2?",
         "opts": [
             "It gives the chain's two directions ethical names — wrong practice and right practice",
             "It introduces an entirely new thirteenth link",
             "It reverses the order of the links permanently",
             "It rejects the chain as inaccurate"],
         "correct": 0,
         "expl": "A restatement reframed as a normative, ethical choice."},
        {"q": "What is the forward direction of the chain called?",
         "opts": [
             "The wrong practice",
             "The right practice",
             "The middle way",
             "The noble path"],
         "correct": 0,
         "expl": "Ignorance conditioning choices, onward to suffering's arising."},
        {"q": "What is the reverse direction of the chain called?",
         "opts": [
             "The right practice",
             "The wrong practice",
             "The forward path",
             "The origination"],
         "correct": 0,
         "expl": "Each link's cessation bringing about the next link's cessation."},
        {"q": "How does the discourse describe ignorance's cessation in the right practice?",
         "opts": [
             "Fading away and ceasing with no residue left behind",
             "Temporarily suppressed but likely to return",
             "Replaced by a different form of ignorance",
             "Impossible to achieve in this lifetime"],
         "correct": 0,
         "expl": "A stronger claim than mere temporary absence."},
        {"q": "What phrase closes the description of both directions?",
         "opts": [
             "This entire mass of suffering",
             "The eternal wheel of existence",
             "The realm of the gods",
             "The path to liberation alone"],
         "correct": 0,
         "expl": "Framing suffering as something built up link by link."},
        {"q": "Does this discourse introduce new content beyond SN 12.1 and SN 12.2?",
         "opts": [
             "No — it assumes familiarity with the chain and restates it with ethical labels",
             "Yes, it introduces several entirely new links",
             "Yes, it reverses the entire teaching of the earlier discourses",
             "Yes, it introduces a different chain altogether"],
         "correct": 0,
         "expl": "A restatement, not new doctrinal content."},
        {"q": "How is the middle of the twelve-link chain presented in this discourse's source text?",
         "opts": [
             "Elided, trusting the reader's familiarity from SN 12.1 and SN 12.2",
             "Spelled out in full detail",
             "Replaced with an entirely different formula",
             "Omitted along with the first and last links"],
         "correct": 0,
         "expl": "Preserved exactly as bilara-data elides it."},
        {"q": "What role does this discourse play within Buddhavagga's structure?",
         "opts": [
             "A compact bridge between SN 12.2's analysis and SN 12.4's extended narrative",
             "The chapter's final and longest discourse",
             "An unrelated digression with no connection to nearby discourses",
             "The chapter's opening discourse"],
         "correct": 0,
         "expl": "Positioned as a hinge restating the formula's stakes."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Sakka, addressing the gods",
             "A group of unnamed monks",
             "Ānanda, on the Buddha's behalf"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for this opening chapter of Nidānavagga."},
    ],
    marginalia=[
        ("Old content, new names", [
            "the same chain, ethically labeled &mdash;",
            "descriptive formula turned normative",
        ]),
        ("Two directions, opposite verdicts", [
            "forward: wrong practice &mdash;",
            "reverse: the right one",
        ]),
        ("No residue left behind", [
            "not mere suppression &mdash;",
            "complete cessation claimed outright",
        ]),
        ("A hinge, not a standalone teaching", [
            "assuming SN 12.1&ndash;2 already read &mdash;",
            "bridging to what comes next",
        ]),
    ],
    further=[
        '<a href="%s/sn12.3/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.2.html">SN 12.2 &middot; Analysis</a> '
        "&mdash; the discourse immediately before this one, analyzing "
        "each link of the chain this discourse names.",
        '<a href="sn-12.4.html">SN 12.4 &middot; About Vipassī</a> '
        "&mdash; the next discourse, an extended narrative of a past "
        "Buddha rediscovering this same chain.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.4 — Vipassīsutta
# --------------------------------------------------------------------------- #
page(
    12, 4, "Vipassī", "About Vipassī",
    meta_title="SN 12.4 — About Vipassī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Vipassīsutta — before his own awakening, the past "
        "Buddha Vipassī reasons backward link by link through "
        "dependent origination, the template for six more Buddhas' "
        "identical discovery. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove — the Buddha narrating "
                    "the past Buddha Vipassī's own pre-awakening "
                    "reasoning"),
        ("Speakers", "The Buddha, addressing the mendicants; within "
                     "the account, Vipassī's own unspoken reflection"),
        ("Form", "An extended first-hand account of backward "
                 "reasoning, one question and one insight per link, "
                 "run twice &mdash; once for arising, once for "
                 "cessation"),
        ("Length", "~8 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "long and repetitive by design, the template "
                       "for six more discourses to come"),
    ],
    why=(
        "Before Vipassī &mdash; one of the six Buddhas said to have "
        "preceded Gotama &mdash; reached his own awakening, he faced "
        "the same trouble every unawakened being faces: birth, aging, "
        "and death, with no visible way out. Rather than receiving "
        "the twelve-link chain as a finished teaching, this discourse "
        "shows him deriving it himself, one question at a time, "
        "working backward from old age and death to find what each "
        "link actually depends on, then working the same sequence in "
        "reverse to see how each link's ending brings about the "
        "next's. This is the discourse the following five borrow "
        "their entire structure from, changing only the Buddha's "
        "name."),
    guide=[
        ("A discovery narrated, not a doctrine announced", [
            "Rather than stating the twelve-link chain as settled "
            "fact, the discourse walks through Vipassī's actual "
            "reasoning process before his awakening, letting readers "
            "watch the derivation happen rather than simply receiving "
            "its conclusion."]),
        ("One question repeated, working backward through every link", [
            "The entire chain emerges from asking the same question "
            "twelve times in sequence &mdash; when what exists is "
            "there this next thing? &mdash; each answer producing the "
            "next question, all the way back to ignorance itself."]),
        ("A named moment for each breakthrough, not treated as automatic", [
            "Each insight is marked with the same formula &mdash; "
            "through rational application of mind, wisdom penetrated "
            "&mdash; framing the discovery of each link as an actual "
            "event of understanding rather than a foregone conclusion."]),
        ("The identical method run twice, forward then reversed", [
            "Having derived how each link conditions the next in the "
            "direction of suffering's arising, Vipassī then reruns "
            "the same backward-questioning method to derive how each "
            "link's cessation produces the next link's cessation "
            "&mdash; the same tool used to build the chain is used to "
            "dismantle it."]),
        ("A template, explicitly marked as such by the source itself", [
            "The discourse closes with the source's own editorial "
            "note stating that this same account should be told in "
            "full for all seven Buddhas &mdash; making explicit what "
            "the text itself intends: this is a pattern to be "
            "repeated, not a story unique to Vipassī alone."]),
    ],
    terms=[
        ("bodhisatta",
         "&ldquo;the one intent on awakening&rdquo; &mdash; how "
         "Vipassī is described throughout, before his own "
         "enlightenment."),
        ("yoniso manasikārā ahu paññāya abhisamayo",
         "&ldquo;through rational application of mind, [he] "
         "penetrated with wisdom&rdquo; &mdash; the recurring formula "
         "marking each breakthrough insight."),
        ("kimhi nu kho sati X hoti, kiṁpaccayā X",
         "&ldquo;when what exists is there X? What is a requirement "
         "for X?&rdquo; &mdash; the single repeated question driving "
         "the entire backward derivation."),
        ("cakkhuṁ udapādi, ñāṇaṁ udapādi&hellip; āloko udapādi",
         "&ldquo;vision arose, knowledge arose&hellip; light "
         "arose&rdquo; &mdash; the fivefold description marking the "
         "completed breakthrough, given once for origination and "
         "once for cessation."),
        ("sattannampi buddhānaṁ evaṁ vitthāretabbo",
         "&ldquo;this should be elaborated in full for all seven "
         "Buddhas&rdquo; &mdash; the source's own explicit note "
         "identifying this discourse as the shared template for the "
         "five that follow."),
    ],
    text_intro=(
        "The discourse in full, given here as the extended template "
        "the following five discourses each abbreviate down to a "
        "single elided line. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "The trouble that prompted the search"),
        ("p", "&sect;1", "sn12.4:1.1-1.5"),
        ("h3", "Discovering how suffering arises"),
        ("p", "&sect;2", "sn12.4:2.1-13.4"),
        ("h3", "Discovering how suffering ceases"),
        ("p", "&sect;3", "sn12.4:14.1-25.4"),
    ],
    quiz=[
        {"q": "Who is Vipassī, as this discourse identifies him?",
         "opts": [
             "One of the Buddhas said to have preceded Gotama",
             "A contemporary disciple of the historical Buddha",
             "A titan lord",
             "A brahmin ascetic never connected to Buddhism"],
         "correct": 0,
         "expl": "One of the six past Buddhas this chapter covers in turn."},
        {"q": "How is the twelve-link chain presented in this discourse?",
         "opts": [
             "As something Vipassī derives himself through backward reasoning, not received as finished doctrine",
             "As a teaching Vipassī simply memorizes from an earlier Buddha",
             "As a chain Vipassī rejects after examination",
             "As a teaching given to Vipassī by Sakka"],
         "correct": 0,
         "expl": "A discovery narrated step by step, not announced as settled fact."},
        {"q": "What single question drives the entire backward derivation?",
         "opts": [
             "When what exists is there this next thing? What is a requirement for it?",
             "What is the meaning of suffering itself?",
             "How can suffering be avoided through ritual?",
             "Who created the chain of existence?"],
         "correct": 0,
         "expl": "The same question repeated at each of the twelve links."},
        {"q": "What formula marks each of Vipassī's breakthrough insights?",
         "opts": [
             "Through rational application of mind, wisdom penetrated",
             "A god appeared and revealed the answer",
             "The answer came through dreamless sleep",
             "No formula marks the insights; they are simply stated"],
         "correct": 0,
         "expl": "Framing each discovery as an actual event of understanding."},
        {"q": "How many times is the backward-questioning method applied across the whole discourse?",
         "opts": [
             "Twice — once to derive arising, once to derive cessation",
             "Only once, covering arising alone",
             "Three times, covering three separate topics",
             "The method is described but never actually applied"],
         "correct": 0,
         "expl": "The identical tool used to build the chain and to dismantle it."},
        {"q": "What formula marks the completed breakthrough, given once for origination and once for cessation?",
         "opts": [
             "Vision arose, knowledge arose, wisdom arose, realization arose, light arose",
             "A single word: \"enlightenment\"",
             "A physical transformation described in detail",
             "No closing formula is given"],
         "correct": 0,
         "expl": "The fivefold description of the moment of full understanding."},
        {"q": "What editorial note does the source text itself include at the discourse's end?",
         "opts": [
             "That this same account should be told in full for all seven Buddhas",
             "That this discourse should never be repeated",
             "That Vipassī's account differs entirely from Gotama's own",
             "No editorial note is given"],
         "correct": 0,
         "expl": "Explicitly marking this as the shared template for the discourses to follow."},
        {"q": "What is the first link identified working backward from old age and death?",
         "opts": [
             "Rebirth (jāti)",
             "Ignorance (avijjā)",
             "Consciousness (viññāṇa)",
             "Craving (taṇhā)"],
         "correct": 0,
         "expl": "The first step in the backward chain, closest to old age and death."},
        {"q": "What is the final link reached at the end of the backward chain?",
         "opts": [
             "Ignorance (avijjā)",
             "Rebirth (jāti)",
             "Feeling (vedanā)",
             "Contact (phassa)"],
         "correct": 0,
         "expl": "The root condition the whole backward derivation eventually reaches."},
        {"q": "Where does the Buddha narrate this account to the monks?",
         "opts": [
             "Sāvatthī, Jeta's Grove",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("Derived, not simply announced", [
            "the chain built step by step &mdash;",
            "readers watching the reasoning unfold",
        ]),
        ("One question, twelve times", [
            "\"when what exists, is there this?\" &mdash;",
            "each answer producing the next question",
        ]),
        ("The same tool, run in reverse", [
            "building the chain, then dismantling it &mdash;",
            "one method serving both directions",
        ]),
        ("A template, marked as such", [
            "\"tell this for all seven Buddhas\" &mdash;",
            "the source naming its own pattern",
        ]),
    ],
    further=[
        '<a href="%s/sn12.4/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.3.html">SN 12.3 &middot; Practice</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.5-9.html">SN 12.5&ndash;9 &middot; Five More Buddhas</a> '
        "&mdash; the next discourses, applying this exact template to "
        "five further past Buddhas in turn.",
    ],
)



# --------------------------------------------------------------------------- #
# SN 12.5–9 — Sikhī, Vessabhū, Kakusandha, Koṇāgamana, Kassapa
# --------------------------------------------------------------------------- #
page_range(
    12, 5, 9,
    "Sikhī, Vessabhū, Kakusandha, Koṇāgamana, Kassapa",
    "Five More Buddhas",
    sources=[
        "sn12/sn12.5", "sn12/sn12.6", "sn12/sn12.7",
        "sn12/sn12.8", "sn12/sn12.9",
    ],
    meta_title="SN 12.5–9 — Five More Buddhas | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "SN 12.5 through 12.9 — five discourses, each preserved in "
        "the source as a single elided line applying SN 12.4's "
        "Vipassī template to a further past Buddha in turn. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove &mdash; the same setting "
                    "named once at the head of this set of five"),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "Five separate discourses, each preserved in the "
                 "source as a single elided line naming a different "
                 "past Buddha"),
        ("Length", "~1.5 minutes to read"),
        ("Northern parallel", "The Chinese Dīrgha-āgama and other "
                              "sources preserve fuller accounts of "
                              "these same seven Buddhas, though this "
                              "reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the content is minimal by design; the "
                       "interest lies in what the repetition itself "
                       "signals"),
    ],
    why=(
        "SN 12.4 gave, in full, the account of how the past Buddha "
        "Vipassī reasoned his own way to the twelve-link chain of "
        "dependent origination before his awakening. That same "
        "discourse closed with an explicit editorial note: tell this "
        "in full for all seven Buddhas. Rather than actually writing "
        "out five more complete versions, the source preserves each "
        "of the next five &mdash; Sikhī, Vessabhū, Kakusandha, "
        "Koṇāgamana, and Kassapa &mdash; as a single elided line, "
        "naming the Buddha and trusting the reader to supply "
        "Vipassī's full account underneath. This reading guide treats "
        "all five together rather than manufacturing five nearly "
        "identical full-length guides for content the source itself "
        "declines to spell out."),
    guide=[
        ("An instruction followed to the letter, not embellished", [
            "SN 12.4's closing note said this account should be told "
            "in full for all seven Buddhas; the source honors that "
            "instruction's letter by preserving five more discourse "
            "numbers, but honors its spirit by eliding each one down "
            "to a single line rather than repeating pages of "
            "identical prose five times over."]),
        ("Five real discourses, not a single merged one", [
            "Despite their near-total brevity, each of these five "
            "carries its own discourse number and its own place in "
            "the collection; this guide treats them together for "
            "readability, not because bilara-data itself merges them "
            "into one file."]),
        ("A traditional lineage of seven, this book's second and third", [
            "Vipassī, Sikhī, Vessabhū, Kakusandha, Koṇāgamana, "
            "Kassapa, and Gotama are traditionally enumerated "
            "together as the Buddhas of the current age; fuller "
            "biographical accounts of each exist elsewhere in the "
            "canon (the Mahāpadāna Sutta, DN 14, most notably), and "
            "this reading guide points there rather than inventing "
            "biographical detail this discourse set doesn't itself "
            "supply."]),
        ("Content this guide declines to manufacture", [
            "Because the source gives essentially no distinguishing "
            "content between these five beyond the substituted name, "
            "this guide does not pretend to find five separate "
            "teachings here; the single teaching is Vipassī's, "
            "applied five more times."]),
        ("A structural signal about how the chapter itself is built", [
            "Reading these five stubs alongside SN 12.4's full "
            "version reveals something about how Buddhavagga is "
            "constructed: one template given in full, then applied "
            "by name-substitution alone &mdash; the same technique "
            "seen at smaller scale elsewhere in this collection, "
            "here used across an entire chapter's structure."]),
    ],
    terms=[
        ("sikhissa&hellip; bhagavato arahato sammāsambuddhassa",
         "&ldquo;for Sikhī, the Blessed One, the perfected one, the "
         "fully awakened Buddha&rdquo; &mdash; the fixed opening "
         "formula shared by all five stubs, varying only the name."),
        ("vessabhū",
         "&ldquo;Vessabhū&rdquo; &mdash; the third of the seven "
         "Buddhas in this traditional lineage, named in SN 12.6."),
        ("kakusandha",
         "&ldquo;Kakusandha&rdquo; &mdash; the fourth of the seven, "
         "traditionally regarded as the first Buddha of the current "
         "aeon, named in SN 12.7."),
        ("koṇāgamana",
         "&ldquo;Koṇāgamana&rdquo; &mdash; the fifth of the seven, "
         "named in SN 12.8."),
        ("kassapa",
         "&ldquo;Kassapa&rdquo; &mdash; the sixth of the seven, "
         "immediately preceding Gotama himself, named in SN 12.9."),
    ],
    text_intro=(
        "All five discourses in full &mdash; each is preserved in the "
        "source as exactly this one elided line, with no further "
        "text beyond the Buddha's name. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1 &middot; SN 12.5", "sn12.5:1.1"),
        ("p", "&sect;2 &middot; SN 12.6", "sn12.6:1.1"),
        ("p", "&sect;3 &middot; SN 12.7", "sn12.7:1.1"),
        ("p", "&sect;4 &middot; SN 12.8", "sn12.8:1.1"),
        ("p", "&sect;5 &middot; SN 12.9", "sn12.9:1.1"),
    ],
    quiz=[
        {"q": "What does each of these five discourses consist of in the source text?",
         "opts": [
             "A single elided line naming a Buddha, referring back to SN 12.4's full account",
             "A complete, independently written account for each Buddha",
             "A verse composed specifically for each Buddha",
             "A dialogue between two of the Buddhas"],
         "correct": 0,
         "expl": "The instruction to tell the account in full was honored by elision, not repetition."},
        {"q": "Which discourse gives the full account these five stubs each refer back to?",
         "opts": [
             "SN 12.4, About Vipassī",
             "SN 12.1, Dependent Origination",
             "SN 12.10, About Gotama",
             "SN 12.3, Practice"],
         "correct": 0,
         "expl": "The template all five apply with only the name changed."},
        {"q": "How many separate discourse numbers do these five stubs actually carry?",
         "opts": [
             "Five — each is its own discourse despite the shared brevity",
             "One merged discourse number covering all five",
             "Two, since some are combined in the source",
             "None; they exist only as part of SN 12.4"],
         "correct": 0,
         "expl": "Treated together here for readability, not because the source merges them."},
        {"q": "What does this reading guide do regarding invented biographical detail for each Buddha?",
         "opts": [
             "It declines to manufacture content the source doesn't supply, pointing instead to DN 14",
             "It provides extensive invented biographical detail for each",
             "It claims all five Buddhas are identical in every respect",
             "It asserts these five Buddhas never actually existed"],
         "correct": 0,
         "expl": "Honesty about what the source does and doesn't say."},
        {"q": "What is the traditional name for the fuller account of these seven Buddhas' lives?",
         "opts": [
             "The Mahāpadāna Sutta (DN 14)",
             "The Dhammapada",
             "The Vinaya Piṭaka",
             "No such fuller account exists anywhere in the canon"],
         "correct": 0,
         "expl": "A separate discourse this reading guide points to rather than duplicating."},
        {"q": "Which Buddha is traditionally regarded as the first of the current aeon?",
         "opts": [
             "Kakusandha",
             "Vipassī",
             "Gotama",
             "Sikhī"],
         "correct": 0,
         "expl": "The fourth of the traditional seven, named in SN 12.7."},
        {"q": "Which Buddha immediately precedes Gotama in this traditional lineage of seven?",
         "opts": [
             "Kassapa",
             "Koṇāgamana",
             "Vessabhū",
             "Sikhī"],
         "correct": 0,
         "expl": "The sixth of the seven, named in SN 12.9, directly before Gotama's own account in SN 12.10."},
        {"q": "What does the repetition across these five stubs reveal about Buddhavagga's own construction?",
         "opts": [
             "A template given in full once, then applied by name-substitution alone across the chapter",
             "That each Buddha taught an entirely different doctrine",
             "That the chapter's structure is random with no discernible pattern",
             "That only Gotama's teaching is considered authoritative"],
         "correct": 0,
         "expl": "A structural technique visible at chapter scale here."},
        {"q": "What formula opens each of the five stub discourses, varying only the name?",
         "opts": [
             "\"For [name], the Blessed One, the perfected one, the fully awakened Buddha\"",
             "\"Once upon a time, a battle was fought\"",
             "\"Thus have I heard\"",
             "No shared formula opens these discourses"],
         "correct": 0,
         "expl": "The fixed template shared across all five names."},
        {"q": "Where is this set of five discourses set, as named once at their head?",
         "opts": [
             "Sāvatthī, Jeta's Grove",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting shared with the rest of Buddhavagga."},
    ],
    marginalia=[
        ("An instruction honored by elision", [
            "\"tell this in full for all seven\" &mdash;",
            "answered with a single line each",
        ]),
        ("Five discourses, one teaching", [
            "only the name changes &mdash;",
            "Vipassī's account, applied five times",
        ]),
        ("A lineage named, not invented", [
            "Sikhī, Vessabhū, Kakusandha&hellip; &mdash;",
            "fuller accounts pointed to, not fabricated",
        ]),
        ("A chapter's structure, visible at scale", [
            "one template, substituted by name &mdash;",
            "the same technique, seen chapter-wide",
        ]),
    ],
    further=[
        '<a href="%s/sn12.5/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation of SN 12.5 on SuttaCentral</a> &mdash; "
        "and similarly for 12.6&ndash;9, each following the same URL "
        "pattern."
        % SC,
        '<a href="sn-12.4.html">SN 12.4 &middot; About Vipassī</a> '
        "&mdash; the full template all five of these discourses "
        "apply.",
        '<a href="sn-12.10.html">SN 12.10 &middot; About Gotama</a> '
        "&mdash; the seventh and final discourse in this set, the "
        "historical Buddha's own first-person account, closing "
        "Buddhavagga.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.10 — Gotamasutta
# --------------------------------------------------------------------------- #
page(
    12, 10, "Gotama", "About Gotama",
    meta_title="SN 12.10 — About Gotama | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Gotamasutta — the historical Buddha tells, in his own "
        "voice, the same backward-questioning discovery of dependent "
        "origination already given for Vipassī, closing Buddhavagga. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove"),
        ("Speakers", "The Buddha alone, recounting his own "
                     "pre-awakening reasoning in the first person"),
        ("Form", "The same extended backward-questioning account "
                 "given in full for Vipassī in SN 12.4, now told by "
                 "Gotama of himself"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "identical in structure to SN 12.4, its "
                       "interest lying in the shift to first person"),
    ],
    why=(
        "Having given Vipassī's discovery of dependent origination in "
        "full, and five more past Buddhas' identical discoveries in a "
        "single elided line each, this closing discourse of "
        "Buddhavagga does something neither approach could: the "
        "Buddha tells his own story, in his own voice. Every step of "
        "the reasoning is the same &mdash; the same backward question "
        "asked twelve times, the same formula marking each "
        "breakthrough, the same reversal from arising to cessation "
        "&mdash; but where Vipassī's account was narrated in the "
        "third person, one Buddha addressing his monks about another, "
        "Gotama speaks here directly of what happened before his own "
        "awakening."),
    guide=[
        ("The same content, a different grammatical person", [
            "Structurally, this discourse changes almost nothing from "
            "SN 12.4; every question, every insight, and every "
            "closing formula reappears in the same order, with "
            "\"Vipassī thought\" replaced throughout by \"it occurred "
            "to me.\""]),
        ("A seventh application of the pattern, not a new discovery", [
            "Like the five discourses before it, this account applies "
            "the same reasoning process to a seventh Buddha in "
            "sequence; what distinguishes it isn't new content but "
            "who is doing the telling."]),
        ("A shift that changes how the account lands, without changing its content", [
            "Reading six accounts of past Buddhas independently "
            "discovering the identical chain, then finally hearing "
            "the same discovery in the speaker's own first-person "
            "voice, gives the pattern a different weight &mdash; this "
            "isn't only a claim about legendary predecessors, but "
            "about the teacher currently addressing the room."]),
        ("A closing that completes the chapter's own structure", [
            "This discourse ends Buddhavagga, and the source's own "
            "closing summary verse lists all ten discourse titles in "
            "sequence &mdash; the general teaching, the analysis, the "
            "naming of practice, and then the seven Buddhas in "
            "order, Vipassī through Gotama."]),
        ("A chapter that grounds an abstract formula in specific tellers", [
            "Read across its full ten discourses, Buddhavagga doesn't "
            "simply state the twelve-link chain once and move on; it "
            "insists on attaching the discovery to particular "
            "individuals, seven times over, closing with the one "
            "individual actually present to say it himself."]),
    ],
    terms=[
        ("pubbeva me&hellip; anabhisambuddhassa bodhisattasseva sato",
         "&ldquo;before my awakening&hellip; when I was still "
         "unawakened but intent on awakening&rdquo; &mdash; the "
         "first-person framing distinguishing this account from the "
         "third-person Vipassī narrative."),
        ("tassa mayhaṁ&hellip; etadahosi",
         "&ldquo;then it occurred to me&rdquo; &mdash; the recurring "
         "first-person marker replacing Vipassī's third-person "
         "formula throughout."),
        ("kimhi nu kho sati X hoti, kiṁpaccayā X",
         "&ldquo;when what exists is there X? What is a requirement "
         "for X?&rdquo; &mdash; the identical backward question "
         "already seen in SN 12.4, now asked by Gotama of himself."),
        ("cakkhuṁ udapādi, ñāṇaṁ udapādi&hellip; āloko udapādi",
         "&ldquo;vision arose, knowledge arose&hellip; light "
         "arose&rdquo; &mdash; the same fivefold breakthrough "
         "formula, now describing what arose in the speaker himself."),
        ("buddhavaggo paṭhamo",
         "&ldquo;the first chapter, on the Buddhas&rdquo; &mdash; the "
         "untranslated closing marker naming the chapter this "
         "discourse completes."),
    ],
    text_intro=(
        "The discourse in full, closing Buddhavagga. The chapter's "
        "closing summary verse, listing all ten discourse titles, is "
        "a structural index and is not reproduced as running prose "
        "here. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The trouble that prompted the search"),
        ("p", "&sect;1", "sn12.10:1.1-1.4"),
        ("h3", "Discovering how suffering arises"),
        ("p", "&sect;2", "sn12.10:2.1-4.4"),
        ("h3", "Discovering how suffering ceases"),
        ("p", "&sect;3", "sn12.10:5.1-7.4"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to SN 12.4's account of Vipassī?",
         "opts": [
             "Structurally identical, with third-person narration replaced by first person",
             "Completely different content and reasoning",
             "Much shorter, omitting most of the backward-questioning steps",
             "Focused on a different topic entirely"],
         "correct": 0,
         "expl": "The same questions, insights, and formulas, told from the speaker's own perspective."},
        {"q": "Who is the speaker of this account?",
         "opts": [
             "The Buddha, recounting his own pre-awakening reasoning",
             "Vipassī, recounting Gotama's future awakening",
             "Sakka, recounting a story about the Buddha",
             "Ānanda, recounting what he heard secondhand"],
         "correct": 0,
         "expl": "A first-person account, distinct from the third-person narration of SN 12.4."},
        {"q": "What phrase replaces Vipassī's third-person \"etadahosi\" formula throughout?",
         "opts": [
             "\"It occurred to me\"",
             "\"It occurred to Vipassī\"",
             "\"The gods declared\"",
             "No replacement phrase is used"],
         "correct": 0,
         "expl": "The consistent first-person marker running through the whole account."},
        {"q": "What position does this discourse's Buddha occupy in the traditional lineage of seven?",
         "opts": [
             "The seventh and most recent, following Kassapa",
             "The first, preceding all the others",
             "The fourth, in the middle of the sequence",
             "This discourse does not specify a position"],
         "correct": 0,
         "expl": "Coming immediately after Kassapa's brief stub in SN 12.9."},
        {"q": "What does this discourse close, structurally, within Nidānavagga?",
         "opts": [
             "Buddhavagga, this book's first chapter of ten discourses",
             "The entire Nidānavagga book",
             "Only a minor sub-section with no larger significance",
             "Nothing; more discourses in this chapter follow"],
         "correct": 0,
         "expl": "Confirmed by the chapter's closing summary verse listing all ten titles."},
        {"q": "What effect does the shift to first person have on the chapter's overall pattern?",
         "opts": [
             "It grounds the abstract, repeated discovery in the teacher actually present to tell it",
             "It contradicts everything said in the previous six discourses",
             "It has no effect; the shift is purely grammatical with no significance",
             "It reveals the previous six accounts were mistaken"],
         "correct": 0,
         "expl": "A different weight given to the same repeated content."},
        {"q": "What is the first link identified working backward from old age and death, matching SN 12.4?",
         "opts": [
             "Rebirth (jāti)",
             "Ignorance (avijjā)",
             "Consciousness (viññāṇa)",
             "Feeling (vedanā)"],
         "correct": 0,
         "expl": "The identical first step in the backward chain, unchanged from Vipassī's account."},
        {"q": "How many times total does the pattern established in SN 12.4 get applied across Buddhavagga?",
         "opts": [
             "Seven times, once for each of the seven Buddhas including Gotama",
             "Only twice, for Vipassī and Gotama alone",
             "Three times, for Vipassī, Kassapa, and Gotama",
             "The pattern is applied only once, in SN 12.4 itself"],
         "correct": 0,
         "expl": "Vipassī in full, five more in elided stubs, and Gotama closing the set."},
        {"q": "What formula marks each completed breakthrough insight in this account?",
         "opts": [
             "Vision arose, knowledge arose, wisdom arose, realization arose, light arose",
             "A physical sign appeared in the sky",
             "The earth shook six times",
             "No formula marks the breakthroughs"],
         "correct": 0,
         "expl": "The same fivefold formula already seen in SN 12.4, now describing the speaker's own experience."},
        {"q": "Where does the Buddha deliver this account to the monks?",
         "opts": [
             "Sāvatthī, Jeta's Grove",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across Buddhavagga."},
    ],
    marginalia=[
        ("The same account, a different voice", [
            "\"Vipassī thought\" becomes \"it occurred to me\" &mdash;",
            "structure unchanged, person shifted",
        ]),
        ("A seventh telling, not a new teaching", [
            "the identical chain, applied once more &mdash;",
            "distinguished by who speaks it",
        ]),
        ("A pattern grounded in the present speaker", [
            "not only about legendary predecessors &mdash;",
            "about the teacher now addressing the room",
        ]),
        ("A chapter completed, seven Buddhas named", [
            "Vipassī through Gotama, in order &mdash;",
            "Buddhavagga's own structure made explicit",
        ]),
    ],
    further=[
        '<a href="%s/sn12.10/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.5-9.html">SN 12.5&ndash;9 &middot; Five More Buddhas</a> '
        "&mdash; the discourses immediately before this one.",
        '<a href="sn-12.4.html">SN 12.4 &middot; About Vipassī</a> '
        "&mdash; the full third-person template this discourse "
        "retells in the first person.",
        '<a href="sn-12.15.html">SN 12.15 &middot; Kaccānagotta</a> '
        "&mdash; a later discourse in this book, already published, "
        "on the middle way between existence and non-existence.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.11 — Āhārasutta
# --------------------------------------------------------------------------- #
page(
    12, 11, "Āhāra", "Fuel",
    meta_title="SN 12.11 — Fuel | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Āhārasutta — opening Āhāravagga, the four fuels that "
        "sustain living beings are traced back through craving into "
        "the same familiar twelve-link chain. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A direct teaching naming four fuels, then tracing "
                 "each back to its source through a repeated "
                 "four-part question"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "introduces a genuinely new framework, not "
                       "just a restatement of Buddhavagga"),
    ],
    why=(
        "Rather than opening Āhāravagga with another retelling of the "
        "twelve-link chain, this discourse approaches the same "
        "territory from an entirely different angle: what sustains a "
        "living being at all? The answer names four fuels &mdash; "
        "edible food, contact, mental intention, and consciousness "
        "&mdash; a framework distinct from anything given in "
        "Buddhavagga. But the discourse doesn't stop at naming them; "
        "it asks what sustains the fuels themselves, and the answer "
        "&mdash; craving, then feeling, then contact, and onward "
        "&mdash; leads straight back into the familiar chain, showing "
        "two different doctrinal frameworks converging on the same "
        "underlying structure."),
    guide=[
        ("A new entry point, not a repeated formula", [
            "This discourse doesn't begin from old age and death, as "
            "every account in Buddhavagga did; it begins from an "
            "entirely different question &mdash; what sustains a "
            "living being &mdash; opening a new chapter with genuinely "
            "new content rather than another variation on the same "
            "starting point."]),
        ("Four fuels, only one of them literally food", [
            "The list moves quickly past the most obvious sense of "
            "sustenance &mdash; edible food &mdash; to name three more "
            "abstract fuels: contact, mental intention, and "
            "consciousness itself, each maintaining beings in a "
            "different sense than nutrition does."]),
        ("A question repeated four times to trace each fuel to its source", [
            "Having named the four fuels, the discourse doesn't leave "
            "them unexplained; it asks, in a fixed fourfold "
            "formula, what the source, origin, birthplace, and "
            "inception of these fuels actually is."]),
        ("Two frameworks meeting at the same point", [
            "The answer to what sustains the four fuels turns out to "
            "be craving, and tracing craving's own source leads "
            "through feeling, contact, the six senses, and onward "
            "&mdash; the same twelve-link chain from Buddhavagga, now "
            "reached from an entirely different starting question."]),
        ("A chapter title earned by its opening discourse", [
            "Āhāravagga takes its name directly from this discourse's "
            "central term; unlike some chapters named for an "
            "incidental detail in their closing discourse, this one is "
            "named for the concept its very first discourse "
            "introduces."]),
    ],
    terms=[
        ("cattāro āhārā",
         "&ldquo;four fuels&rdquo; &mdash; the fourfold framework "
         "opening this chapter, distinct from anything named in "
         "Buddhavagga."),
        ("kabaḷīkāro āhāro oḷāriko vā sukhumo vā",
         "&ldquo;edible food, whether solid or subtle&rdquo; "
         "&mdash; the first and most literal of the four fuels."),
        ("manosañcetanā",
         "&ldquo;mental intention&rdquo; &mdash; the third fuel, "
         "naming the sustaining role of volitional activity itself."),
        ("kiṁnidānā kiṁsamudayā kiṁjātikā kiṁpabhavā",
         "&ldquo;what is the source, origin, birthplace, and "
         "inception&rdquo; &mdash; the fixed fourfold question used "
         "to trace each fuel back to its condition."),
        ("taṇhānidānā",
         "&ldquo;craving is [their] source&rdquo; &mdash; the "
         "pivotal answer connecting the four fuels back into the "
         "familiar twelve-link chain."),
    ],
    text_intro=(
        "The discourse in full, opening Āhāravagga. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.11:1.3-1.6"),
        ("p", "&sect;2", "sn12.11:2.1-2.16"),
        ("p", "&sect;3", "sn12.11:3.1-3.6"),
    ],
    quiz=[
        {"q": "How does this discourse open Āhāravagga, compared to Buddhavagga's approach?",
         "opts": [
             "With an entirely new framework — four fuels sustaining beings — rather than repeating the chain from old age and death",
             "By repeating SN 12.4's account word for word",
             "By rejecting the twelve-link chain outright",
             "By introducing a battle between gods and titans"],
         "correct": 0,
         "expl": "A genuinely new entry point into the same underlying territory."},
        {"q": "What are the four fuels this discourse names?",
         "opts": [
             "Edible food, contact, mental intention, and consciousness",
             "Water, earth, fire, and air",
             "Faith, ethics, generosity, and wisdom",
             "Sight, sound, smell, and taste"],
         "correct": 0,
         "expl": "A framework distinct from anything given in Buddhavagga."},
        {"q": "How is edible food further specified in the list?",
         "opts": [
             "As whether solid or subtle",
             "As only ever solid",
             "As only ever liquid",
             "The text gives no further specification"],
         "correct": 0,
         "expl": "The most literal of the four fuels, given a qualifying detail."},
        {"q": "What question does the discourse ask about the four fuels themselves?",
         "opts": [
             "What is their source, origin, birthplace, and inception",
             "How many beings depend on them",
             "Whether they can be avoided entirely",
             "Which fuel is most important"],
         "correct": 0,
         "expl": "A fixed fourfold formula tracing each fuel to its condition."},
        {"q": "What is identified as the source of the four fuels?",
         "opts": [
             "Craving",
             "Ignorance directly",
             "The six sense fields",
             "Consciousness alone"],
         "correct": 0,
         "expl": "The pivotal answer connecting this new framework back to the familiar chain."},
        {"q": "After craving, what chain of conditions does the discourse trace backward?",
         "opts": [
             "Feeling, contact, the six sense fields, name and form, consciousness, choices, ignorance",
             "An entirely new chain unrelated to Buddhavagga",
             "A chain of only two additional links",
             "No further chain is traced; the discourse stops at craving"],
         "correct": 0,
         "expl": "The same twelve-link chain from Buddhavagga, reached by a new route."},
        {"q": "Why is this chapter named Āhāravagga?",
         "opts": [
             "Because its very first discourse introduces the concept of fuel (āhāra) as its central term",
             "Because of an incidental detail in its closing discourse",
             "The name has no connection to any discourse in the chapter",
             "Because it was named after a place called Āhāra"],
         "correct": 0,
         "expl": "A chapter named directly for its opening discourse's central concept."},
        {"q": "What kind of fuel is mental intention, distinct from edible food?",
         "opts": [
             "An abstract fuel sustaining beings through volitional activity, not literal nutrition",
             "A form of edible food eaten only by ascetics",
             "A fuel available only to enlightened beings",
             "A fuel that has no relationship to sustaining existence"],
         "correct": 0,
         "expl": "One of three more abstract fuels beyond literal food."},
        {"q": "Does this discourse's twelve-link chain, reached via the fuels, differ in content from Buddhavagga's chain?",
         "opts": [
             "No — it is the same chain, reached from a different starting question",
             "Yes, it reverses the direction entirely",
             "Yes, it omits several links present in Buddhavagga",
             "Yes, it adds several new links not in Buddhavagga"],
         "correct": 0,
         "expl": "Two frameworks converging on the identical underlying structure."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for this opening chapter of Āhāravagga."},
    ],
    marginalia=[
        ("A new door into the same house", [
            "not old age and death this time &mdash;",
            "what sustains a being at all",
        ]),
        ("Four fuels, only one of them food", [
            "contact, intention, consciousness too &mdash;",
            "sustenance beyond nutrition",
        ]),
        ("Traced back, not left unexplained", [
            "source, origin, birthplace, inception &mdash;",
            "the same question, asked of each fuel",
        ]),
        ("Two roads, one destination", [
            "fuel leads to craving, craving to the chain &mdash;",
            "Buddhavagga's structure, reached anew",
        ]),
    ],
    further=[
        '<a href="%s/sn12.11/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.10.html">SN 12.10 &middot; About Gotama</a> '
        "&mdash; the discourse closing Buddhavagga, immediately "
        "before this one.",
        '<a href="sn-12.12.html">SN 12.12 &middot; Phagguna of the Top-Knot</a> '
        "&mdash; the next discourse, directly challenging the idea "
        "of a self standing behind these very fuels.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.12 — Moḷiyaphaggunasutta
# --------------------------------------------------------------------------- #
page(
    12, 12, "Moḷiyaphagguna", "Phagguna of the Top-Knot",
    meta_title="SN 12.12 — Phagguna of the Top-Knot | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Moḷiyaphaggunasutta — a monk asks who consumes "
        "consciousness as fuel, and the Buddha systematically "
        "rejects the question's hidden assumption of a self behind "
        "each link. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove"),
        ("Speakers", "The Buddha and the monk Phagguna of the "
                     "Top-Knot"),
        ("Form", "A five-part question-and-correction sequence, each "
                 "round following an identical pattern"),
        ("Length", "~4.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "one of this collection's most philosophically "
                       "demanding discourses"),
    ],
    why=(
        "Following directly on SN 12.11's account of the four fuels, "
        "the monk Phagguna asks a question that seems entirely "
        "reasonable: who consumes consciousness as fuel? The Buddha's "
        "answer is startling &mdash; that's not a cogent question at "
        "all, because it assumes a self who does the consuming, a "
        "self the teaching never posits. Rather than simply refusing "
        "to answer, the Buddha explains exactly what a cogent "
        "question would look like instead, and this exchange repeats "
        "four more times &mdash; who contacts, who feels, who craves, "
        "who grasps &mdash; each time the same agent-implying question "
        "corrected into a question about conditions rather than "
        "actors."),
    guide=[
        ("A reasonable-sounding question, firmly refused", [
            "Phagguna's question isn't presented as obviously "
            "mistaken; it's the kind of question almost anyone might "
            "ask after hearing SN 12.11's talk of fuel, which makes "
            "the Buddha's flat rejection &mdash; that's not a cogent "
            "question &mdash; land with real force."]),
        ("The problem named precisely, not left vague", [
            "The Buddha doesn't simply say the question is wrong; he "
            "explains exactly why &mdash; he doesn't speak of one who "
            "consumes at all, so asking who does the consuming has no "
            "target to land on."]),
        ("A corrected question offered, not just a rejected one", [
            "Rather than leaving Phagguna with nothing, the Buddha "
            "supplies the question that would actually be cogent "
            "&mdash; not who consumes, but what consciousness as fuel "
            "is a condition for &mdash; redirecting the inquiry "
            "toward relationships between conditions rather than "
            "toward an agent."]),
        ("The same correction applied five times over", [
            "This isn't a single exchange; the identical pattern "
            "repeats for four more verbs &mdash; contacting, feeling, "
            "craving, grasping &mdash; systematically closing off "
            "every place a hidden self might otherwise be smuggled "
            "into the chain."]),
        ("A philosophical stance embedded in the chain's own grammar", [
            "By the discourse's end, the twelve-link chain has been "
            "shown to describe conditions producing conditions, with "
            "no experiencer standing behind any of them &mdash; not a "
            "separate teaching about not-self, but the same "
            "conclusion built directly into how the chain itself is "
            "meant to be spoken of."]),
    ],
    terms=[
        ("ko nu kho, bhante, viññāṇāhāraṁ āhāretī",
         "&ldquo;who consumes consciousness as fuel?&rdquo; "
         "&mdash; Phagguna's opening question, assuming an agent "
         "behind the process."),
        ("no kallo pañho",
         "&ldquo;that's not a cogent question&rdquo; &mdash; the "
         "Buddha's firm, repeated rejection formula, used five times "
         "across the discourse."),
        ("āhāretīti ahaṁ na vadāmi",
         "&ldquo;I don't speak of one who consumes&rdquo; &mdash; "
         "the Buddha's explicit statement that he posits no agent "
         "behind the fuels or the chain."),
        ("kissa nu kho, bhante, viññāṇāhāro",
         "&ldquo;for what is consciousness the fuel?&rdquo; &mdash; "
         "the corrected, impersonal question the Buddha supplies in "
         "place of Phagguna's original."),
        ("ko nu kho, bhante, phusati&hellip; vedayati&hellip; tasati&hellip; upādiyati",
         "&ldquo;who contacts&hellip; who feels&hellip; who "
         "craves&hellip; who grasps&rdquo; &mdash; the sequence of "
         "further agent-implying questions, each corrected in turn."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.12:1.2-1.5"),
        ("p", "&sect;2", "sn12.12:2.1-2.11"),
        ("p", "&sect;3", "sn12.12:3.1-3.10"),
        ("p", "&sect;4", "sn12.12:4.1-4.10"),
        ("p", "&sect;5", "sn12.12:5.1-5.10"),
        ("p", "&sect;6", "sn12.12:6.1-6.12"),
        ("p", "&sect;7", "sn12.12:7.1-7.8"),
    ],
    quiz=[
        {"q": "What question does Phagguna ask the Buddha at the discourse's opening?",
         "opts": [
             "Who consumes consciousness as fuel?",
             "How many fuels sustain a being?",
             "What is the meaning of suffering?",
             "Where do the four fuels come from?"],
         "correct": 0,
         "expl": "A reasonable-sounding question that turns out to hide an assumption."},
        {"q": "How does the Buddha respond to this question?",
         "opts": [
             "He rejects it outright as not a cogent question",
             "He answers it directly by naming a specific consumer",
             "He refuses to respond at all",
             "He asks Phagguna to answer his own question"],
         "correct": 0,
         "expl": "A firm rejection, repeated as a formula across the discourse."},
        {"q": "Why does the Buddha say the question isn't cogent?",
         "opts": [
             "Because he doesn't speak of one who consumes at all, so the question has no target",
             "Because the answer is a secret reserved for advanced monks",
             "Because Phagguna asked it disrespectfully",
             "Because consciousness doesn't actually require fuel"],
         "correct": 0,
         "expl": "The problem is named precisely, not left vague."},
        {"q": "What corrected question does the Buddha offer in place of Phagguna's original?",
         "opts": [
             "For what is consciousness the fuel?",
             "Who created consciousness?",
             "How long does consciousness last?",
             "No corrected question is offered"],
         "correct": 0,
         "expl": "Redirecting inquiry toward conditions rather than an agent."},
        {"q": "How many times does this same question-and-correction pattern repeat across the discourse?",
         "opts": [
             "Five times in total, covering consuming, contacting, feeling, craving, and grasping",
             "Only once, covering consuming alone",
             "Exactly three times",
             "Ten times, covering every link in the chain"],
         "correct": 0,
         "expl": "Systematically closing off every place a hidden self might be smuggled in."},
        {"q": "What does the Buddha say about a self behind the process of feeling?",
         "opts": [
             "He doesn't speak of one who feels; the cogent question concerns what feeling is a condition for",
             "He confirms a self does the feeling",
             "He says feeling happens without any cause",
             "He declines to discuss feeling at all"],
         "correct": 0,
         "expl": "The identical correction applied to the third of the five verbs."},
        {"q": "What philosophical position does this discourse embed directly into the chain's structure?",
         "opts": [
             "That the chain describes conditions producing conditions, with no experiencer standing behind them",
             "That a permanent self exists behind every experience",
             "That consciousness alone is exempt from conditioning",
             "That the chain is purely metaphorical with no real content"],
         "correct": 0,
         "expl": "Not-self built into how the chain is meant to be spoken of, not argued separately."},
        {"q": "What does the discourse trace as the condition for grasping?",
         "opts": [
             "Craving",
             "Feeling directly, bypassing craving",
             "Ignorance directly, bypassing all intermediate links",
             "No condition is given for grasping"],
         "correct": 0,
         "expl": "Matching the standard sequence already seen in Buddhavagga and SN 12.11."},
        {"q": "How does the discourse close, regarding cessation?",
         "opts": [
             "By tracing how the fading of the six fields of contact leads to the cessation of the whole chain",
             "Without addressing cessation at all",
             "By declaring cessation impossible",
             "By introducing an entirely new topic unrelated to cessation"],
         "correct": 0,
         "expl": "The same reverse-order cessation sequence familiar from Buddhavagga."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "Sāvatthī, Jeta's Grove",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A question that sounds reasonable", [
            "\"who consumes?\" &mdash; almost anyone would ask it &mdash;",
            "the rejection landing with real force",
        ]),
        ("No agent posited, none to find", [
            "\"I don't speak of one who consumes\" &mdash;",
            "the question has nothing to land on",
        ]),
        ("Corrected, not simply dismissed", [
            "a cogent question supplied in its place &mdash;",
            "conditions, not an actor",
        ]),
        ("The same move, five times over", [
            "consuming, contacting, feeling, craving, grasping &mdash;",
            "every hiding place for a self, closed off",
        ]),
    ],
    further=[
        '<a href="%s/sn12.12/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.11.html">SN 12.11 &middot; Fuel</a> '
        "&mdash; the discourse immediately before this one, "
        "introducing the four fuels this exchange interrogates.",
        '<a href="sn-12.13.html">SN 12.13 &middot; Ascetics and Brahmins</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.13 — Samaṇabrāhmaṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 13, "Samaṇabrāhmaṇa", "Ascetics and Brahmins",
    meta_title="SN 12.13 — Ascetics and Brahmins | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Samaṇabrāhmaṇasutta — genuine ascetic or brahmin status "
        "is redefined around a fourfold understanding of each of the "
        "twelve links, not formal title or external status. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A direct teaching applying a fourfold analytical "
                 "template to each of the twelve links in turn, then "
                 "delivering a pointed verdict"),
        ("Length", "~3.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a new analytical structure applied across "
                       "the whole chain, not just a restatement"),
    ],
    why=(
        "This discourse takes the twelve-link chain and puts it to a "
        "sharply pointed use: redefining what actually counts as a "
        "genuine ascetic or brahmin. Rather than accepting formal "
        "title, robes, or social recognition as sufficient, the "
        "Buddha applies a fourfold test to every single link in "
        "turn &mdash; do you understand this link, its origin, its "
        "cessation, and the practice leading to its cessation? "
        "Whoever fails this test on even one link isn't deemed a true "
        "ascetic or brahmin at all, regardless of external "
        "recognition; "
        "whoever passes it on every link is deemed genuine, having "
        "realized the goal with their own insight rather than merely "
        "claiming it."),
    guide=[
        ("A fourfold template, not a single question", [
            "Rather than simply asking whether someone understands "
            "dependent origination in general, the discourse breaks "
            "the test into four specific components applied to each "
            "link &mdash; the thing itself, its origin, its "
            "cessation, and the path to its cessation."]),
        ("Applied to every link, not just the whole chain", [
            "This fourfold test isn't run once against the chain as "
            "a totality; it's applied individually to each of the "
            "twelve links in sequence, meaning genuine understanding "
            "can't be claimed by grasping the chain's general shape "
            "while missing any single piece."]),
        ("A verdict on identity, not merely on knowledge", [
            "Failing this test doesn't just mean someone lacks a "
            "particular piece of information; the Buddha states "
            "directly that he doesn't deem such people true ascetics "
            "or brahmins at all, regardless of their formal claim to "
            "that status."]),
        ("Realization, not mere claim, as the actual standard", [
            "The discourse specifies exactly what distinguishes "
            "genuine attainment from empty title: realizing the goal "
            "of ascetic or brahmin life with one's own insight, in "
            "this very life, rather than simply asserting the "
            "identity."]),
        ("A single teaching mirrored in two opposite verdicts", [
            "The discourse doesn't only describe failure; it states "
            "the positive case in exactly parallel language, giving "
            "the same weight to genuine attainment as to its absence, "
            "rather than framing the teaching purely as a rebuke."]),
    ],
    terms=[
        ("jarāmaraṇaṁ, jarāmaraṇasamudayaṁ, jarāmaraṇanirodhaṁ, jarāmaraṇanirodhagāminiṁ paṭipadaṁ",
         "&ldquo;old age and death, their origin, their cessation, "
         "and the practice leading to their cessation&rdquo; &mdash; "
         "the fourfold analytical template, applied first to "
         "illustrate the pattern."),
        ("na me te&hellip; samaṇā vā brāhmaṇā vā samaṇesu vā samaṇasammatā",
         "&ldquo;I don't deem them as true ascetics and "
         "brahmins&rdquo; &mdash; the discourse's central, pointed "
         "verdict on failure."),
        ("sāmaññatthaṁ vā brahmaññatthaṁ&hellip; sayaṁ abhiññā sacchikatvā",
         "&ldquo;the goal of life as an ascetic or brahmin&hellip; "
         "realized with their own insight&rdquo; &mdash; specifying "
         "personal realization, not external status, as what's "
         "actually at stake."),
        ("saṅkhāre nappajānanti, saṅkhārasamudayaṁ nappajānanti",
         "&ldquo;they don't understand choices, their origin&rdquo; "
         "&mdash; the twelfth and final link in the enumeration, "
         "closing the full checklist."),
        ("te kho me&hellip; samaṇasammatā",
         "&ldquo;I deem them as true ascetics and brahmins&rdquo; "
         "&mdash; the positive counterpart verdict, mirroring the "
         "negative one in exactly parallel language."),
    ],
    text_intro=(
        "The discourse in full. The middle links are elided in the "
        "source exactly as bilara-data preserves them, following the "
        "same pattern established for old age and death. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.13:1.2-1.13"),
        ("p", "&sect;2", "sn12.13:2.1-2.12"),
    ],
    quiz=[
        {"q": "What fourfold template does this discourse apply to each of the twelve links?",
         "opts": [
             "The thing itself, its origin, its cessation, and the practice leading to its cessation",
             "The thing's color, taste, texture, and sound",
             "Its origin only, with no further analysis",
             "A comparison to each of the four noble truths as a single unit"],
         "correct": 0,
         "expl": "A specific fourfold test, not a single general question."},
        {"q": "How many times is this fourfold test actually applied across the discourse?",
         "opts": [
             "Individually to each of the twelve links in sequence",
             "Only once, applied to the chain as a single whole",
             "Twice, once for arising and once for cessation as wholes",
             "Never; the discourse only describes the test without applying it"],
         "correct": 0,
         "expl": "Understanding can't be claimed by grasping the chain's general shape alone."},
        {"q": "What does the Buddha say about someone who fails this test on even one link?",
         "opts": [
             "That he doesn't deem them a true ascetic or brahmin at all",
             "That they are merely mistaken but still genuine",
             "That failure on one link is acceptable if the rest are understood",
             "That the discourse offers no verdict either way"],
         "correct": 0,
         "expl": "A verdict on identity, not merely on a gap in knowledge."},
        {"q": "What does the discourse specify as the actual standard for genuine attainment?",
         "opts": [
             "Realizing the goal with one's own insight, not merely claiming the title",
             "Wearing the correct robes and following ritual forms",
             "Being formally ordained by a recognized teacher",
             "Achieving social recognition from the wider community"],
         "correct": 0,
         "expl": "Personal realization distinguished from external status or claim."},
        {"q": "Does the discourse only describe failure, or also success?",
         "opts": [
             "Both — it states the positive case in exactly parallel language to the negative",
             "Only failure; no positive case is given",
             "Only success; failure is never mentioned",
             "Neither; the discourse remains purely descriptive"],
         "correct": 0,
         "expl": "A single teaching mirrored in two opposite verdicts."},
        {"q": "What is the first link the fourfold template is applied to, illustrating the pattern?",
         "opts": [
             "Old age and death",
             "Ignorance",
             "Consciousness",
             "Craving"],
         "correct": 0,
         "expl": "The starting point before the pattern extends through all twelve links."},
        {"q": "What is the twelfth and final link closing the enumeration?",
         "opts": [
             "Choices (saṅkhārā)",
             "Ignorance (avijjā)",
             "Rebirth (jāti)",
             "Feeling (vedanā)"],
         "correct": 0,
         "expl": "The closing link in the standard backward sequence."},
        {"q": "According to this discourse, is formal title alone sufficient for genuine ascetic or brahmin status?",
         "opts": [
             "No — genuine status requires the fourfold understanding regardless of formal claim",
             "Yes, formal title alone is entirely sufficient",
             "The discourse takes no position on this question",
             "Only royal recognition can confer genuine status"],
         "correct": 0,
         "expl": "The central redefinition driving the whole discourse."},
        {"q": "How does this discourse relate to the twelve-link chain already given in Buddhavagga?",
         "opts": [
             "It applies a new analytical use to the same familiar chain, rather than restating it plainly",
             "It rejects the chain entirely",
             "It introduces an unrelated new chain with different links",
             "It only discusses the chain's first link"],
         "correct": 0,
         "expl": "A pointed redefinition of spiritual identity, built on already-established content."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A test, not a general question", [
            "thing, origin, cessation, path &mdash;",
            "applied link by link, not once for all",
        ]),
        ("Failure named plainly", [
            "\"I don't deem them true\" &mdash;",
            "a verdict on identity, not just knowledge",
        ]),
        ("Realized, not merely claimed", [
            "insight of one's own, in this very life &mdash;",
            "title alone falling short",
        ]),
        ("Two verdicts, equal weight", [
            "failure and success both stated in full &mdash;",
            "not framed as rebuke alone",
        ]),
    ],
    further=[
        '<a href="%s/sn12.13/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.12.html">SN 12.12 &middot; Phagguna of the Top-Knot</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.14.html">SN 12.14 &middot; Ascetics and Brahmins (2nd)</a> '
        "&mdash; the next discourse, restating this same teaching "
        "with an added rhetorical question.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.14 — Dutiyasamaṇabrāhmaṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 14, "Dutiyasamaṇabrāhmaṇa", "Ascetics and Brahmins (2nd)",
    meta_title="SN 12.14 — Ascetics and Brahmins (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasamaṇabrāhmaṇasutta — SN 12.13's same fourfold "
        "test for genuine ascetic or brahmin status, restated with "
        "an added rhetorical question framing each half. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same fourfold test as SN 12.13, now introduced "
                 "with an explicit rhetorical question before each "
                 "half"),
        ("Length", "~3.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "nearly identical content to SN 12.13, worth "
                       "reading for the added pedagogical framing"),
    ],
    why=(
        "This discourse teaches exactly what SN 12.13 already "
        "taught &mdash; the same fourfold test of each of the twelve "
        "links, the same pointed verdict on genuine versus merely "
        "titled ascetics and brahmins &mdash; but restructures the "
        "presentation with an explicit rhetorical question inserted "
        "before each half: what things don't they understand? What "
        "things do they understand? Where SN 12.13 moved straight "
        "into the list, this version pauses first to name the "
        "question the list is about to answer, a small but "
        "genuine shift in how the same content is taught."),
    guide=[
        ("Identical content, a different pedagogical shape", [
            "Every substantive claim in this discourse matches SN "
            "12.13 exactly; what changes is the presentation, not the "
            "teaching itself."]),
        ("A question inserted before the answer, not left implicit", [
            "SN 12.13 moves directly from stating that some ascetics "
            "and brahmins fail the test into listing what they fail "
            "to understand; this version pauses to ask explicitly "
            "what things they don't understand, before answering its "
            "own question."]),
        ("A generic pointer, specified afterward", [
            "The discourse first refers to \"these things\" in "
            "general terms, then only afterward spells out exactly "
            "which things &mdash; old age and death, rebirth, and so "
            "on through the full twelve links &mdash; a structure "
            "that builds anticipation before delivering the list SN "
            "12.13 gives immediately."]),
        ("The same two-part symmetry preserved", [
            "Like its companion, this discourse gives equal, "
            "parallel treatment to both failure and success, now each "
            "half opened by its own explicit question rather than "
            "moving straight into the answer."]),
        ("A minor variation worth noticing, not overreading", [
            "The difference here is genuinely small &mdash; a "
            "restructured presentation of identical content &mdash; "
            "and this reading guide treats it as exactly that, rather "
            "than searching for a doctrinal distinction the source "
            "itself doesn't actually draw."]),
    ],
    terms=[
        ("ime dhamme nappajānanti, imesaṁ dhammānaṁ samudayaṁ nappajānanti",
         "&ldquo;they don't understand these things, their "
         "origin&rdquo; &mdash; the same fourfold formula, now "
         "introduced with a generic pointer before being spelled "
         "out."),
        ("katame dhamme nappajānanti",
         "&ldquo;what things don't they understand?&rdquo; &mdash; "
         "the added rhetorical question distinguishing this version's "
         "structure from SN 12.13's."),
        ("katamesaṁ dhammānaṁ samudayaṁ&hellip; nirodhaṁ&hellip; nirodhagāminiṁ paṭipadaṁ",
         "&ldquo;what things' origin&hellip; cessation&hellip; "
         "practice leading to cessation&rdquo; &mdash; the question "
         "expanded into its full fourfold form."),
        ("na me te&hellip; samaṇā vā brāhmaṇā vā samaṇasammatā",
         "&ldquo;I don't deem them as true ascetics and "
         "brahmins&rdquo; &mdash; the identical verdict already given "
         "in SN 12.13."),
        ("te kho me&hellip; samaṇasammatā",
         "&ldquo;I deem them as true ascetics and brahmins&rdquo; "
         "&mdash; the identical positive verdict, closing this "
         "version exactly as SN 12.13 closes."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.14:1.2-2.13"),
        ("p", "&sect;2", "sn12.14:3.1-4.13"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to SN 12.13's?",
         "opts": [
             "Identical in every substantive claim, differing only in presentation",
             "Completely different teaching with no overlap",
             "A direct contradiction of SN 12.13's verdict",
             "Focused on an entirely unrelated topic"],
         "correct": 0,
         "expl": "The same teaching, restructured rather than replaced."},
        {"q": "What does this version add before listing what some ascetics and brahmins fail to understand?",
         "opts": [
             "An explicit rhetorical question: what things don't they understand?",
             "A story about a specific named ascetic",
             "A verse in praise of understanding",
             "Nothing is added; the structure is identical to SN 12.13"],
         "correct": 0,
         "expl": "A pause before the answer, distinguishing this version's structure."},
        {"q": "How does this discourse first refer to the twelve links, before spelling them out?",
         "opts": [
             "With a generic pointer, \"these things,\" specified only afterward",
             "By naming all twelve immediately with no generic pointer",
             "By omitting several of the twelve entirely",
             "By referring to them as \"those distant matters\""],
         "correct": 0,
         "expl": "Building anticipation before delivering the full list."},
        {"q": "Does this discourse preserve the same two-part symmetry (failure and success) as SN 12.13?",
         "opts": [
             "Yes — both halves are given equal, parallel treatment, each opened by its own question",
             "No — only the failure case is given here",
             "No — only the success case is given here",
             "The symmetry is present but reversed in order"],
         "correct": 0,
         "expl": "The same balanced structure, now with explicit questions framing each half."},
        {"q": "How does this reading guide characterize the difference between SN 12.13 and SN 12.14?",
         "opts": [
             "A genuinely small restructuring, not a doctrinal distinction",
             "A major theological disagreement between the two discourses",
             "Evidence that one of the two discourses is corrupted",
             "A difference so large the two should be treated as unrelated"],
         "correct": 0,
         "expl": "Honest treatment of a minor variation without overreading it."},
        {"q": "What verdict does the Buddha give for those who fail the fourfold test in this version?",
         "opts": [
             "That he doesn't deem them true ascetics or brahmins, identical to SN 12.13",
             "A softer verdict than SN 12.13's",
             "A harsher verdict than SN 12.13's",
             "No verdict is given in this version"],
         "correct": 0,
         "expl": "The identical conclusion, unchanged from the companion discourse."},
        {"q": "What is the first link discussed once the list is spelled out?",
         "opts": [
             "Old age and death",
             "Ignorance",
             "Consciousness",
             "Craving"],
         "correct": 0,
         "expl": "Matching SN 12.13's own starting point in the enumeration."},
        {"q": "What is the standard this discourse gives for genuine ascetic or brahmin status?",
         "opts": [
             "Realizing the goal with one's own insight, matching SN 12.13 exactly",
             "A different, more lenient standard than SN 12.13's",
             "A different, stricter standard than SN 12.13's",
             "No standard is specified in this version"],
         "correct": 0,
         "expl": "Identical substantive content across both discourses."},
        {"q": "What is the numbering convention for this discourse's Pali title?",
         "opts": [
             "Dutiyasamaṇabrāhmaṇasutta, \"the second ascetics-and-brahmins discourse\"",
             "Tatiyasamaṇabrāhmaṇasutta, \"the third\"",
             "The Pali title bears no relation to SN 12.13's",
             "This discourse has no distinct Pali title"],
         "correct": 0,
         "expl": "Explicitly marked as the second in a pair with SN 12.13."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting shared with SN 12.13."},
    ],
    marginalia=[
        ("Same teaching, new shape", [
            "every claim unchanged from SN 12.13 &mdash;",
            "only the presentation differs",
        ]),
        ("A question paused on, not skipped", [
            "\"what things don't they understand?\" &mdash;",
            "asked before being answered",
        ]),
        ("Named generally, then specified", [
            "\"these things\" first, the list after &mdash;",
            "anticipation built before delivery",
        ]),
        ("A minor variation, honestly sized", [
            "not a doctrinal split &mdash;",
            "just a different way of teaching it",
        ]),
    ],
    further=[
        '<a href="%s/sn12.14/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.13.html">SN 12.13 &middot; Ascetics and Brahmins</a> '
        "&mdash; the discourse immediately before this one, teaching "
        "the same content without the added rhetorical question.",
        '<a href="sn-12.16.html">SN 12.16 &middot; A Dhamma Speaker</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.16 — Dhammakathikasutta
# --------------------------------------------------------------------------- #
page(
    12, 16, "Dhammakathika", "A Dhamma Speaker",
    meta_title="SN 12.16 — A Dhamma Speaker | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dhammakathikasutta — a monk asks how a genuine Dhamma "
        "speaker is defined, and the Buddha answers with a threefold "
        "hierarchy running from speaking to practicing to full "
        "realization. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "An unnamed mendicant and the Buddha"),
        ("Form", "A question answered with a threefold hierarchy, "
                 "applied to each of the twelve links in turn"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a compact but precise distinction worth "
                       "reading slowly"),
    ],
    why=(
        "A monk asks a question that sounds almost administrative: "
        "how is a &ldquo;Dhamma speaker&rdquo; actually defined? The "
        "Buddha's answer refuses to settle for a simple yes-or-no "
        "test. Instead, for each of the twelve links, he distinguishes "
        "three separate levels of engagement: teaching about that "
        "link's disillusionment, dispassion, and cessation qualifies "
        "someone to be called a Dhamma speaker; actually practicing "
        "toward that same disillusionment qualifies them as one who "
        "practices in line with the teaching; and being genuinely "
        "freed through it qualifies them as one who has attained "
        "extinguishment in this very life. Talking about the "
        "teaching, living by it, and realizing it are treated as "
        "three distinct achievements, not stages of the same title."),
    guide=[
        ("A question about status, answered with a hierarchy", [
            "Rather than giving a single definition of what makes "
            "someone a Dhamma speaker, the Buddha distinguishes three "
            "separate titles, each earned by a different kind of "
            "engagement with the same content."]),
        ("Teaching as the first, most modest threshold", [
            "Simply teaching Dhamma aimed at disillusionment, "
            "dispassion, and cessation regarding a given link is "
            "enough to earn the title of Dhamma speaker &mdash; a "
            "real but limited qualification, not requiring personal "
            "attainment."]),
        ("Practicing as a distinct, higher threshold", [
            "A second, more demanding title belongs to those who "
            "actually practice toward that same disillusionment, "
            "dispassion, and cessation &mdash; not merely speaking "
            "about the goal but working toward it."]),
        ("Freedom as the highest and most specific threshold", [
            "The third title is reserved for those freed by "
            "non-grasping through disillusionment, dispassion, and "
            "cessation &mdash; full realization, described precisely "
            "as attainment of extinguishment in this very life, not a "
            "future promise."]),
        ("The same three-tier test applied to every link", [
            "This threefold distinction isn't made once for the chain "
            "as a whole; it's applied individually to each of the "
            "twelve links, from old age and death through to "
            "ignorance, meaning genuine speaking, practicing, or "
            "attainment can be assessed link by link."]),
    ],
    terms=[
        ("dhammakathiko",
         "&ldquo;a Dhamma speaker&rdquo; &mdash; the term the "
         "questioning monk asks the Buddha to define."),
        ("nibbidāya virāgāya nirodhāya dhammaṁ deseti",
         "&ldquo;teaches Dhamma for disillusionment, dispassion, and "
         "cessation&rdquo; &mdash; the first, most modest threshold, "
         "qualifying someone as a Dhamma speaker."),
        ("dhammānudhammappaṭipanno",
         "&ldquo;one who practices in line with the teaching&rdquo; "
         "&mdash; the second, higher threshold, requiring actual "
         "practice rather than only teaching."),
        ("anupādāvimutto&hellip; diṭṭhadhammanibbānappatto",
         "&ldquo;freed by not grasping&hellip; attained "
         "extinguishment in this very life&rdquo; &mdash; the third "
         "and highest threshold, full realization."),
        ("jarāmaraṇassa&hellip; avijjāya",
         "&ldquo;old age and death&hellip; ignorance&rdquo; &mdash; "
         "the first and last links bracketing the full twelve-link "
         "application of this threefold test."),
    ],
    text_intro=(
        "The discourse in full. The middle links are elided in the "
        "source, following the same pattern already seen throughout "
        "this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.16:1.2-1.4"),
        ("p", "&sect;2", "sn12.16:2.1-2.3"),
        ("p", "&sect;3", "sn12.16:3.11-3.13"),
    ],
    quiz=[
        {"q": "What question does the monk ask the Buddha at the discourse's opening?",
         "opts": [
             "How a \"Dhamma speaker\" is actually defined",
             "How many links make up the chain of dependent origination",
             "Whether ordination is required to teach the Dhamma",
             "What the proper etiquette is for addressing the Buddha"],
         "correct": 0,
         "expl": "A question that sounds administrative but receives a precise answer."},
        {"q": "What qualifies someone to be called a Dhamma speaker, the first threshold?",
         "opts": [
             "Teaching Dhamma aimed at disillusionment, dispassion, and cessation regarding a link",
             "Achieving full liberation regarding that link",
             "Simply being formally ordained",
             "Having memorized the entire twelve-link chain"],
         "correct": 0,
         "expl": "A real but limited qualification, not requiring personal attainment."},
        {"q": "What is the second, higher threshold the discourse names?",
         "opts": [
             "One who practices in line with the teaching",
             "One who has taught for at least ten years",
             "One who has converted the most followers",
             "There is no second threshold; only two levels are named"],
         "correct": 0,
         "expl": "Actual practice toward the goal, distinct from merely speaking about it."},
        {"q": "What is the third and highest threshold?",
         "opts": [
             "Being freed by not grasping, attaining extinguishment in this very life",
             "Being recognized as a Dhamma speaker by the wider community",
             "Being able to teach all twelve links without hesitation",
             "There is no third threshold named in this discourse"],
         "correct": 0,
         "expl": "Full realization, described precisely rather than left vague."},
        {"q": "How many times is this threefold test actually applied across the discourse?",
         "opts": [
             "Individually to each of the twelve links in turn",
             "Only once, applied to the whole chain as a unit",
             "Only to the first link, old age and death",
             "The test is described but never actually applied"],
         "correct": 0,
         "expl": "Genuine speaking, practicing, or attainment assessed link by link."},
        {"q": "Does simply teaching the Dhamma require personal liberation, according to this discourse?",
         "opts": [
             "No — teaching alone qualifies someone as a Dhamma speaker, a distinct and lesser threshold",
             "Yes — only fully liberated beings may teach at all",
             "The discourse doesn't address teaching separately from liberation",
             "Teaching is explicitly forbidden without full liberation"],
         "correct": 0,
         "expl": "The three titles are distinct achievements, not stages of a single one."},
        {"q": "What is the first link the threefold test is applied to, illustrating the pattern?",
         "opts": [
             "Old age and death",
             "Ignorance",
             "Craving",
             "Consciousness"],
         "correct": 0,
         "expl": "The starting point before the pattern extends through all twelve links."},
        {"q": "What is the last link, closing the full application?",
         "opts": [
             "Ignorance",
             "Rebirth",
             "Feeling",
             "Grasping"],
         "correct": 0,
         "expl": "The closing link matching Buddhavagga's own backward sequence."},
        {"q": "How is full attainment described in this discourse's third threshold?",
         "opts": [
             "As extinguishment attained in this very life, not a future promise",
             "As a state achievable only after death",
             "As a permanent state requiring no further practice to maintain",
             "As identical to simply being ordained"],
         "correct": 0,
         "expl": "A precise, present-tense description of full realization."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across most of this chapter."},
    ],
    marginalia=[
        ("A question sounding administrative", [
            "\"how is a Dhamma speaker defined?\" &mdash;",
            "answered with real precision",
        ]),
        ("Speaking, the most modest threshold", [
            "no attainment required &mdash;",
            "a real but limited title",
        ]),
        ("Practicing, a distinct step higher", [
            "not merely talking about the goal &mdash;",
            "actually working toward it",
        ]),
        ("Freedom, named precisely", [
            "extinguishment in this very life &mdash;",
            "not a promise deferred",
        ]),
    ],
    further=[
        '<a href="%s/sn12.16/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.14.html">SN 12.14 &middot; Ascetics and Brahmins (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.17.html">SN 12.17 &middot; With Kassapa, the Naked Ascetic</a> '
        "&mdash; the next discourse, connecting dependent origination "
        "directly to the rejection of both eternalism and "
        "annihilationism.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.17 — Acelakassapasutta
# --------------------------------------------------------------------------- #
page(
    12, 17, "Acelakassapa", "With Kassapa, the Naked Ascetic",
    meta_title="SN 12.17 — With Kassapa, the Naked Ascetic | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Acelakassapasutta — a wandering ascetic presses the "
        "Buddha on whether suffering is self-made or other-made, and "
        "dependent origination is named as the middle way avoiding "
        "both eternalism and annihilationism. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Rājagaha, the Bamboo Grove, on the Buddha's "
                    "own alms round through the streets"),
        ("Speakers", "The Buddha and Kassapa, a naked ascetic from "
                     "another tradition"),
        ("Form", "A persistent philosophical challenge, a direct "
                 "teaching in response, and a conversion narrative "
                 "closing in ordination and awakening"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "one of this saṃyutta's philosophically "
                       "richest and most consequential discourses"),
    ],
    why=(
        "Catching the Buddha mid-almsround, the naked ascetic Kassapa "
        "presses a classic question in four parts: is suffering made "
        "by oneself, by another, by both, or by neither? To every "
        "version the Buddha answers only &ldquo;not so, "
        "Kassapa&rdquo; &mdash; while still insisting suffering is "
        "entirely real and that he knows and sees it clearly. Pushed "
        "to explain what looks like evasion, the Buddha reveals the "
        "hidden cost of each rejected position: saying suffering is "
        "self-made assumes a single unchanging self persisting "
        "through the act and its result, which amounts to "
        "eternalism; saying it's other-made assumes the doer and the "
        "one who experiences the result are entirely separate, which "
        "amounts to annihilationism. Avoiding both extremes, he "
        "teaches the middle way: dependent origination itself."),
    guide=[
        ("A question refused three times before it's even asked", [
            "Before Kassapa can pose his actual question, the Buddha "
            "twice declines to answer &mdash; not because the "
            "question is unwelcome, but because he is mid-almsround "
            "in an inhabited area, a detail that grounds this "
            "philosophically dense discourse in an entirely ordinary "
            "moment."]),
        ("Four positions offered, all four rejected", [
            "Kassapa's tetralemma covers what looks like every "
            "logical possibility &mdash; self-made, other-made, both, "
            "or neither &mdash; and the Buddha declines every single "
            "one, a pattern that could easily read as evasion if the "
            "discourse stopped there."]),
        ("Suffering affirmed as real, even as every explanation is refused", [
            "The Buddha doesn't use his fourfold rejection to deny "
            "suffering exists or claim ignorance of it; he states "
            "plainly that suffering is real and that he knows and "
            "sees it &mdash; making Kassapa's confusion, and his "
            "demand for an actual answer, entirely reasonable."]),
        ("Each rejected position diagnosed, not just dismissed", [
            "Rather than leaving the four rejections unexplained, the "
            "Buddha names exactly what each one smuggles in: "
            "self-made suffering assumes one continuous self doing "
            "and experiencing, implying eternalism; other-made "
            "suffering assumes doer and experiencer are entirely "
            "separate, implying annihilationism."]),
        ("A conversion completed, not merely argued", [
            "The discourse doesn't end with Kassapa intellectually "
            "satisfied; he goes for refuge, requests ordination, "
            "volunteers four years of probation when only four months "
            "was required of a former ascetic from another tradition, "
            "and attains full awakening not long after &mdash; "
            "philosophy followed all the way through to a completed "
            "life."]),
    ],
    terms=[
        ("sayaṅkataṁ dukkhaṁ&hellip; paraṅkataṁ dukkhaṁ",
         "&ldquo;suffering made by oneself&hellip; made by "
         "another&rdquo; &mdash; the two central horns of Kassapa's "
         "fourfold question."),
        ("mā hevaṁ, kassapa",
         "&ldquo;not so, Kassapa&rdquo; &mdash; the Buddha's "
         "repeated rejection of every one of the four proposed "
         "positions."),
        ("so karoti so paṭisaṁvedayati&hellip; sassataṁ etaṁ pareti",
         "&ldquo;he who does the deed and he who experiences the "
         "result are one and the same&hellip; this implies "
         "eternalism&rdquo; &mdash; the hidden assumption diagnosed "
         "behind the self-made position."),
        ("añño karoti añño paṭisaṁvedayati&hellip; ucchedaṁ etaṁ pareti",
         "&ldquo;he who does the deed is one, and he who experiences "
         "is another&hellip; this implies annihilationism&rdquo; "
         "&mdash; the hidden assumption diagnosed behind the "
         "other-made position."),
        ("ete te ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the pivotal line "
         "connecting dependent origination directly to the rejection "
         "of both eternalism and annihilationism."),
    ],
    text_intro=(
        "The discourse in full, one of this saṃyutta's philosophically "
        "richest. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.17:1.2-1.9"),
        ("p", "&sect;2", "sn12.17:2.1-2.9"),
        ("p", "&sect;3", "sn12.17:3.1-3.15"),
        ("p", "&sect;4", "sn12.17:4.9-4.10"),
        ("p", "&sect;5", "sn12.17:5.1-5.9"),
        ("p", "&sect;6", "sn12.17:6.1-6.5"),
        ("p", "&sect;7", "sn12.17:7.1-9.4"),
    ],
    quiz=[
        {"q": "Why does the Buddha decline to answer Kassapa's question the first two times it's raised?",
         "opts": [
             "It's the wrong time, since he's mid-almsround in an inhabited area",
             "He considers the question unworthy of an answer",
             "He doesn't recognize Kassapa",
             "Kassapa hasn't yet formally introduced himself"],
         "correct": 0,
         "expl": "A practical, not philosophical, reason grounding the discourse in an ordinary moment."},
        {"q": "What four positions does Kassapa's question about suffering cover?",
         "opts": [
             "Self-made, other-made, made by both, or arising uncaused by either",
             "Only two positions: caused or uncaused",
             "Five positions including a position about the gods",
             "The question doesn't actually offer multiple positions"],
         "correct": 0,
         "expl": "A classic fourfold structure covering what looks like every logical possibility."},
        {"q": "How does the Buddha respond to each of the four positions?",
         "opts": [
             "He rejects each one with \"not so, Kassapa\"",
             "He affirms the first position and rejects the rest",
             "He affirms all four as equally valid",
             "He refuses to respond to any of them"],
         "correct": 0,
         "expl": "A uniform rejection across all four proposed explanations."},
        {"q": "Does the Buddha deny that suffering exists, given his rejection of all four positions?",
         "opts": [
             "No — he affirms suffering is real and that he knows and sees it clearly",
             "Yes, he denies suffering exists at all",
             "He remains ambiguous on whether suffering exists",
             "He says suffering exists only for some beings"],
         "correct": 0,
         "expl": "Making Kassapa's confusion and demand for an actual answer entirely reasonable."},
        {"q": "What hidden assumption does the Buddha identify behind the \"self-made\" position?",
         "opts": [
             "That the doer and the one who experiences the result are one continuous self, implying eternalism",
             "That suffering is purely imaginary",
             "That suffering comes only from external forces",
             "No hidden assumption is identified"],
         "correct": 0,
         "expl": "A diagnosis, not merely a dismissal, of what the position smuggles in."},
        {"q": "What hidden assumption does the Buddha identify behind the \"other-made\" position?",
         "opts": [
             "That the doer and the one who experiences are entirely separate, implying annihilationism",
             "That suffering only affects enlightened beings",
             "That suffering is caused by karma from a past life alone",
             "No hidden assumption is identified"],
         "correct": 0,
         "expl": "The second diagnosed extreme, mirroring the first."},
        {"q": "What does the Buddha teach as the middle way avoiding both extremes?",
         "opts": [
             "Dependent origination, the twelve-link chain",
             "A doctrine of a permanent, unchanging soul",
             "The complete non-existence of cause and effect",
             "A teaching unrelated to the twelve-link chain"],
         "correct": 0,
         "expl": "Connecting this famous philosophical exchange directly to the chain covered throughout this book."},
        {"q": "How does Kassapa respond to the Buddha's explanation?",
         "opts": [
             "He goes for refuge and requests ordination",
             "He rejects the explanation and departs unconvinced",
             "He challenges the Buddha to further debate",
             "He remains silent with no recorded response"],
         "correct": 0,
         "expl": "A conversion completed, not merely an argument won."},
        {"q": "What unusual commitment does Kassapa make regarding his ordination probation?",
         "opts": [
             "He volunteers four years of probation when only four months was required",
             "He refuses any probation period at all",
             "He requests immediate ordination with no conditions",
             "He asks to skip ordination entirely"],
         "correct": 0,
         "expl": "A display of eagerness exceeding what standard procedure actually demanded."},
        {"q": "What is the outcome of Kassapa's ordination, according to the discourse's closing lines?",
         "opts": [
             "He attains full awakening not long afterward, becoming one of the perfected",
             "He abandons the monastic life shortly after ordination",
             "He remains a probationary monk indefinitely",
             "The discourse doesn't record any outcome"],
         "correct": 0,
         "expl": "Philosophy followed all the way through to a completed spiritual life."},
    ],
    marginalia=[
        ("A question delayed by ordinary circumstance", [
            "mid-almsround, not the time &mdash;",
            "grounding a dense discourse in the everyday",
        ]),
        ("Four positions, all four refused", [
            "self-made, other-made, both, neither &mdash;",
            "yet suffering still affirmed as real",
        ]),
        ("Each refusal, its hidden cost named", [
            "one position smuggles in eternalism &mdash;",
            "the other, annihilation",
        ]),
        ("An argument that ends in a life changed", [
            "refuge, ordination, four years volunteered &mdash;",
            "and full awakening not long after",
        ]),
    ],
    further=[
        '<a href="%s/sn12.17/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.16.html">SN 12.16 &middot; A Dhamma Speaker</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.18.html">SN 12.18 &middot; With Timbaruka</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.18 — Timbarukasutta
# --------------------------------------------------------------------------- #
page(
    12, 18, "Timbaruka", "With Timbaruka",
    meta_title="SN 12.18 — With Timbaruka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Timbarukasutta — a close companion to SN 12.17, asking "
        "the same fourfold question about pleasure and pain rather "
        "than suffering, ending in lifelong lay refuge rather than "
        "ordination. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and Timbaruka, a wanderer from "
                     "another tradition"),
        ("Form", "The same fourfold question-and-rejection sequence "
                 "as SN 12.17, closely paralleling its structure"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "familiar structure from SN 12.17, worth "
                       "reading for exactly what differs"),
    ],
    why=(
        "This discourse retells nearly the same exchange as SN 12.17 "
        "&mdash; the same fourfold question, the same repeated "
        "&ldquo;not so&rdquo; rejections, the same diagnosis of "
        "eternalism and annihilationism hiding inside the rejected "
        "positions, the same middle way named as dependent "
        "origination &mdash; but with two genuine differences worth "
        "reading for. The wanderer Timbaruka asks about pleasure and "
        "pain specifically, not suffering in general, and the "
        "Buddha's diagnosis is phrased in terms of feeling and the "
        "one who feels it, rather than the doer of a deed and the "
        "one who experiences its result. And where Kassapa sought "
        "ordination, Timbaruka asks only to be remembered as a "
        "lay follower, going for refuge for life."),
    guide=[
        ("A close companion, not a duplicate", [
            "This discourse follows SN 12.17's structure closely "
            "enough that reading them side by side is more useful "
            "than reading either alone; the value here lies in "
            "noticing precisely where the two diverge, not in "
            "treating this as unrelated new content."]),
        ("Pleasure and pain, not suffering, as the topic", [
            "Timbaruka's fourfold question concerns sukhadukkha "
            "&mdash; pleasure and pain together &mdash; a broader "
            "framing than Kassapa's question about suffering alone, "
            "encompassing pleasant experience as much as painful."]),
        ("The same diagnosis, phrased around feeling rather than deeds", [
            "Where SN 12.17 diagnosed the self-made position as "
            "assuming one continuous self doing a deed and "
            "experiencing its result, this discourse diagnoses it in "
            "terms of the feeling itself and the one who feels it "
            "&mdash; a smaller shift in vocabulary carrying the same "
            "underlying logic."]),
        ("An identical middle way, reached by a parallel route", [
            "Despite these differences in framing, the conclusion is "
            "exactly the same: avoiding both extremes, the Realized "
            "One teaches dependent origination, word for word matching "
            "SN 12.17's own formula."]),
        ("A different outcome, worth noticing without overreading it", [
            "Where Kassapa requested ordination and underwent a "
            "probationary period before becoming a monk, Timbaruka "
            "asks only to be remembered as a lay follower who has "
            "gone for refuge for life &mdash; a genuinely different "
            "resolution, though the text gives no explanation for "
            "why one wanderer sought ordination and the other did "
            "not."]),
    ],
    terms=[
        ("sayaṅkataṁ sukhadukkhaṁ",
         "&ldquo;pleasure and pain made by oneself&rdquo; &mdash; "
         "Timbaruka's version of the fourfold question, broader than "
         "SN 12.17's focus on suffering alone."),
        ("mā hevaṁ, timbaruka",
         "&ldquo;not so, Timbaruka&rdquo; &mdash; the same rejection "
         "formula from SN 12.17, personalized to this interlocutor."),
        ("sā vedanā, so vedayati&hellip; na vadāmi",
         "&ldquo;the feeling and the one who feels it are one and "
         "the same&hellip; I don't say this&rdquo; &mdash; the same "
         "diagnosis as SN 12.17, now phrased around feeling rather "
         "than deeds."),
        ("ete te ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the identical "
         "pivot line closing both discourses' philosophical content."),
        ("upāsakaṁ maṁ bhavaṁ gotamo dhāretu&hellip; pāṇupetaṁ saraṇaṁ gataṁ",
         "&ldquo;may the worthy Gotama remember me as a lay follower "
         "who has gone for refuge for life&rdquo; &mdash; Timbaruka's "
         "conversion outcome, remaining lay rather than seeking "
         "ordination."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.18:1.2-1.3"),
        ("p", "&sect;2", "sn12.18:2.1-2.15"),
        ("p", "&sect;3", "sn12.18:3.10-3.11"),
        ("p", "&sect;4", "sn12.18:4.1-4.9"),
        ("p", "&sect;5", "sn12.18:5.1-5.4"),
    ],
    quiz=[
        {"q": "How does this discourse's structure compare to SN 12.17's?",
         "opts": [
             "Closely parallel, following nearly the same fourfold question-and-rejection sequence",
             "Completely unrelated with no structural overlap",
             "A direct contradiction of SN 12.17's conclusions",
             "Told entirely in verse, unlike SN 12.17's prose"],
         "correct": 0,
         "expl": "A close companion discourse, best read alongside SN 12.17."},
        {"q": "What does Timbaruka's fourfold question concern, broader than SN 12.17's topic?",
         "opts": [
             "Pleasure and pain together, not suffering alone",
             "Wealth and poverty",
             "Life and death specifically",
             "The existence of the gods"],
         "correct": 0,
         "expl": "Encompassing pleasant experience as much as painful, unlike Kassapa's narrower question."},
        {"q": "How is the Buddha's diagnosis of the \"self-made\" position phrased differently here than in SN 12.17?",
         "opts": [
             "Around feeling and the one who feels it, rather than a deed and its result",
             "It is phrased identically with no difference at all",
             "It rejects the diagnosis given in SN 12.17 entirely",
             "It introduces an entirely new diagnostic framework unrelated to SN 12.17"],
         "correct": 0,
         "expl": "A smaller shift in vocabulary carrying the same underlying logic."},
        {"q": "Does the conclusion — the middle way taught — differ from SN 12.17's?",
         "opts": [
             "No — it is identical, dependent origination, word for word",
             "Yes, it teaches a completely different doctrine",
             "Yes, it reverses SN 12.17's conclusion",
             "The discourse reaches no conclusion at all"],
         "correct": 0,
         "expl": "The same middle way, reached by a parallel but distinct route."},
        {"q": "How does Timbaruka's outcome differ from Kassapa's in SN 12.17?",
         "opts": [
             "He asks to be remembered as a lay follower, rather than seeking ordination",
             "He rejects the Buddha's teaching entirely",
             "He seeks ordination exactly as Kassapa did",
             "The discourse gives no outcome for Timbaruka"],
         "correct": 0,
         "expl": "A genuinely different resolution, left unexplained by the text itself."},
        {"q": "Does the source explain why Timbaruka's outcome differs from Kassapa's?",
         "opts": [
             "No — the text gives no explanation for the difference",
             "Yes, it explains Timbaruka was too old to ordain",
             "Yes, it explains Timbaruka's tradition forbade ordination",
             "Yes, it explains the Buddha refused to ordain Timbaruka"],
         "correct": 0,
         "expl": "A difference this reading guide notes honestly without inventing a cause."},
        {"q": "How many times does the Buddha reject a proposed position in this discourse's fourfold question?",
         "opts": [
             "Four times",
             "Only once",
             "Twice",
             "He accepts all four positions"],
         "correct": 0,
         "expl": "Matching SN 12.17's identical pattern of fourfold rejection."},
        {"q": "Does the Buddha deny that pleasure and pain exist, given his rejection of all four positions?",
         "opts": [
             "No — he affirms they are real and that he knows and sees them",
             "Yes, he denies they exist at all",
             "He remains ambiguous on the question",
             "He says they exist only for unenlightened beings"],
         "correct": 0,
         "expl": "The same affirmation of reality already seen in SN 12.17."},
        {"q": "What relationship does this discourse have to Buddhavagga's twelve-link chain?",
         "opts": [
             "It connects directly to the same chain via the middle-way teaching",
             "It rejects the twelve-link chain entirely",
             "It has no connection to the chain whatsoever",
             "It introduces a thirteenth link"],
         "correct": 0,
         "expl": "The identical formula closing both this discourse and SN 12.17."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across most of this chapter."},
    ],
    marginalia=[
        ("A companion, not a duplicate", [
            "read alongside SN 12.17 &mdash;",
            "value in what differs, not what repeats",
        ]),
        ("Pleasure and pain, the broader question", [
            "not suffering alone this time &mdash;",
            "the pleasant included too",
        ]),
        ("The same logic, a different vocabulary", [
            "feeling and the one who feels &mdash;",
            "not the deed and its result",
        ]),
        ("A different ending, left unexplained", [
            "lay refuge, not ordination &mdash;",
            "the text offers no reason why",
        ]),
    ],
    further=[
        '<a href="%s/sn12.18/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.17.html">SN 12.17 &middot; With Kassapa, the Naked Ascetic</a> '
        "&mdash; the closely related discourse this one closely "
        "parallels.",
        '<a href="sn-12.19.html">SN 12.19 &middot; The Astute and the Foolish</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.19 — Bālapaṇḍitasutta
# --------------------------------------------------------------------------- #
page(
    12, 19, "Bālapaṇḍita", "The Astute and the Foolish",
    meta_title="SN 12.19 — The Astute and the Foolish | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bālapaṇḍitasutta — fool and sage share the exact same "
        "starting mechanism of body and experience, diverging only "
        "on whether ignorance and craving are actually resolved. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha, addressing the mendicants, with a "
                     "brief request from the monks for clarification"),
        ("Form", "A parallel description of fool and sage, followed "
                 "by a direct answer to the monks' own question about "
                 "the difference between them"),
        ("Length", "~4.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a precise, structurally elegant teaching on "
                       "what actually distinguishes wisdom"),
    ],
    why=(
        "This discourse opens by describing the fool and the astute "
        "person in identical terms: both have a body produced through "
        "ignorance and craving, both experience pleasure and pain "
        "through contact at the six sense fields, in exactly the same "
        "way. Having laid out this parallel so precisely that the "
        "monks themselves ask what the actual difference is, the "
        "Buddha answers with equal precision: the fool has not given "
        "up ignorance or finished craving, so continues to another "
        "body after death; the astute person has, and does not. The "
        "difference isn't in how experience arises &mdash; that "
        "mechanism is shared &mdash; but in whether the underlying "
        "conditions have actually been resolved."),
    guide=[
        ("Fool and sage described in identical terms, deliberately", [
            "The discourse's opening two sections are constructed to "
            "mirror each other almost word for word, describing the "
            "fool and the astute person's body, contact, and "
            "experience of pleasure and pain in exactly parallel "
            "language."]),
        ("A question the monks themselves are moved to ask", [
            "Rather than the Buddha immediately explaining the "
            "distinction, the parallel description is precise enough "
            "that the monks themselves request clarification, "
            "genuinely uncertain what could possibly differ between "
            "two people described so identically."]),
        ("The difference located in resolution, not in mechanism", [
            "The Buddha's answer doesn't locate the difference in how "
            "experience arises for each person, since that mechanism "
            "has already been shown to be shared; it locates the "
            "difference in whether ignorance has actually been given "
            "up and craving actually finished."]),
        ("A consequence stated in terms of rebirth, not merely character", [
            "The practical difference isn't framed as one person "
            "simply behaving better than the other; it's framed in "
            "terms of an entirely different fate at death &mdash; "
            "continuing to another body, or not."]),
        ("A single sentence naming the entire distinction", [
            "The discourse closes by naming, in one line, exactly "
            "what the difference between fool and sage comes down to: "
            "leading the spiritual life &mdash; not talent, not "
            "circumstance, but sustained practice toward the ending "
            "of ignorance and craving."]),
    ],
    terms=[
        ("avijjānīvaraṇassa&hellip; taṇhāya sampayuttassa&hellip; kāyo samudāgato",
         "&ldquo;shrouded by ignorance and coupled to craving, this "
         "body has been produced&rdquo; &mdash; the shared starting "
         "condition described identically for both fool and sage."),
        ("ayañceva kāyo bahiddhā ca nāmarūpaṁ",
         "&ldquo;this body and external name and form&rdquo; "
         "&mdash; the basic duality producing contact and "
         "experience, identical for both."),
        ("bālo&hellip; avijjā appahīnā&hellip; taṇhā aparikkhīṇā",
         "&ldquo;the fool&hellip; has not given up ignorance&hellip; "
         "has not finished craving&rdquo; &mdash; what specifically "
         "distinguishes the fool once the question is finally "
         "answered."),
        ("paṇḍito&hellip; avijjā pahīnā&hellip; taṇhā parikkhīṇā",
         "&ldquo;the astute person&hellip; has given up "
         "ignorance&hellip; has finished craving&rdquo; &mdash; the "
         "exact mirror distinguishing the wise."),
        ("kāyūpago&hellip; na parimuccati / akāyūpago&hellip; parimuccati",
         "&ldquo;proceeds to another body&hellip; not freed&rdquo; "
         "versus &ldquo;doesn't proceed to another body&hellip; "
         "freed&rdquo; &mdash; the actual consequence distinguishing "
         "rebirth from liberation."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.19:1.2-1.3"),
        ("p", "&sect;2", "sn12.19:2.1-2.2"),
        ("p", "&sect;3", "sn12.19:3.1-4.3"),
        ("p", "&sect;4", "sn12.19:5.1-5.6"),
        ("p", "&sect;5", "sn12.19:6.1-6.7"),
    ],
    quiz=[
        {"q": "How does this discourse initially describe the fool and the astute person?",
         "opts": [
             "In identical terms, deliberately mirroring each other",
             "As already entirely different in every respect",
             "It describes only the fool, omitting the astute person",
             "It describes only the astute person, omitting the fool"],
         "correct": 0,
         "expl": "A precise parallel construction opening the discourse."},
        {"q": "What shared condition does the discourse attribute to both fool and sage?",
         "opts": [
             "A body produced through ignorance and craving, experiencing pleasure and pain through contact",
             "Both are already fully liberated",
             "Both lack any body at all",
             "Neither experiences pleasure or pain"],
         "correct": 0,
         "expl": "The identical starting mechanism shared by both."},
        {"q": "What prompts the Buddha to explain the difference between fool and sage?",
         "opts": [
             "The monks themselves ask, genuinely uncertain given the identical description",
             "The Buddha volunteers the explanation unprompted",
             "A visiting deity demands an answer",
             "No explanation is ever given in this discourse"],
         "correct": 0,
         "expl": "A question arising naturally from how precisely parallel the description was."},
        {"q": "Where does the Buddha locate the actual difference between fool and sage?",
         "opts": [
             "In whether ignorance has been given up and craving finished, not in how experience arises",
             "In physical strength",
             "In social status at birth",
             "In the mechanism of experience itself, which differs between them"],
         "correct": 0,
         "expl": "The mechanism is shared; the resolution of ignorance and craving is not."},
        {"q": "What happens to the fool at death, according to this discourse?",
         "opts": [
             "They proceed to another body, not freed from suffering",
             "They are immediately freed from all suffering",
             "They cease to exist entirely with no further consequence",
             "The discourse doesn't address what happens at death"],
         "correct": 0,
         "expl": "A consequence framed in terms of continued rebirth, not merely character."},
        {"q": "What happens to the astute person at death, by contrast?",
         "opts": [
             "They do not proceed to another body, and are freed from suffering",
             "They proceed to another body just as the fool does",
             "They are punished for their wisdom",
             "The discourse gives an identical outcome for both"],
         "correct": 0,
         "expl": "The exact mirror of the fool's fate, in terms of rebirth and freedom."},
        {"q": "What single phrase does the discourse use to name the entire difference between fool and sage?",
         "opts": [
             "Leading the spiritual life",
             "Being born into a wealthy family",
             "Having a naturally sharper intellect",
             "Living in a particular geographic region"],
         "correct": 0,
         "expl": "Sustained practice, not talent or circumstance, named as the actual distinction."},
        {"q": "Why do the monks say they want the Buddha himself to explain this, rather than working it out themselves?",
         "opts": [
             "Because their teachings are rooted in the Buddha, who is their guide and refuge",
             "Because they are forbidden from speculating on this topic",
             "Because the question has no correct answer",
             "Because Sāriputta has already forbidden discussion of it"],
         "correct": 0,
         "expl": "A statement of trust in the Buddha as the source of clarification."},
        {"q": "Does the discourse frame the fool's failure as a lack of information?",
         "opts": [
             "No — it frames it as a failure to actually give up ignorance and finish craving, through practice",
             "Yes — the fool simply lacks facts the sage possesses",
             "The discourse takes no position on the nature of the fool's failure",
             "It frames the failure as entirely outside the fool's control"],
         "correct": 0,
         "expl": "A distinction of resolved versus unresolved practice, not mere knowledge."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across most of this chapter."},
    ],
    marginalia=[
        ("Described as identical, on purpose", [
            "fool and sage, mirrored word for word &mdash;",
            "the same body, the same mechanism",
        ]),
        ("A question the monks can't help but ask", [
            "if described alike, what differs? &mdash;",
            "genuine uncertainty, not rhetoric",
        ]),
        ("Not the mechanism, but its resolution", [
            "ignorance given up, or not &mdash;",
            "craving finished, or not",
        ]),
        ("A fate, not just a character trait", [
            "another body, or none &mdash;",
            "the actual stakes of the difference",
        ]),
    ],
    further=[
        '<a href="%s/sn12.19/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.18.html">SN 12.18 &middot; With Timbaruka</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.20.html">SN 12.20 &middot; Conditions</a> '
        "&mdash; the next discourse, closing Āhāravagga with a "
        "precise statement of dependent origination as a discovered "
        "natural law.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.20 — Paccayasutta
# --------------------------------------------------------------------------- #
page(
    12, 20, "Paccaya", "Conditions",
    meta_title="SN 12.20 — Conditions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paccayasutta — closing Āhāravagga, dependent origination "
        "is distinguished from the phenomena it governs and named a "
        "discovered natural law, with clear vision of it closing off "
        "speculation about self across all three times. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A precise doctrinal teaching distinguishing two "
                 "related but separate concepts, closed with a "
                 "practical payoff"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "one of this chapter's most philosophically "
                       "precise discourses, closing it fittingly"),
    ],
    why=(
        "Closing Āhāravagga, this discourse makes a distinction easy "
        "to miss: dependent origination itself &mdash; the "
        "principle, the lawful regularity that rebirth conditions "
        "old age and death, and so through every link &mdash; is not "
        "the same thing as the dependently originated phenomena, the "
        "twelve links themselves. The principle is described as "
        "persisting whether or not any Buddha ever arises to discover "
        "it, a fixed regularity of nature the Buddha awakens to and "
        "then reveals; the phenomena it governs are each described as "
        "impermanent, conditioned, liable to end. And clear vision of "
        "both together, the discourse closes by saying, makes a whole "
        "category of speculative questions about the self across "
        "past, future, and present simply stop arising."),
    guide=[
        ("Two related concepts, kept carefully distinct", [
            "The discourse doesn't treat &ldquo;dependent "
            "origination&rdquo; and &ldquo;the twelve links&rdquo; as "
            "interchangeable terms for the same thing; it defines "
            "each separately, devoting a full section to each in "
            "turn."]),
        ("A principle described as discovered, not invented", [
            "The lawful regularity connecting each link to the next "
            "is said to persist whether or not any Realized One ever "
            "arises &mdash; the Buddha's role is to awaken to this "
            "regularity and reveal it, not to originate it."]),
        ("The phenomena themselves, characterized by their instability", [
            "Where the principle is described as a fixed regularity, "
            "each individual link &mdash; old age and death, "
            "rebirth, and onward through to ignorance &mdash; is "
            "instead characterized as impermanent, conditioned, and "
            "liable to end, a deliberate contrast between the "
            "unchanging rule and its ever-changing instances."]),
        ("A precise, technical vocabulary for both", [
            "The discourse doesn't settle for vague description; it "
            "gives dependent origination itself a precise technical "
            "definition &mdash; reality, non-falseness, "
            "non-otherness, specific conditionality &mdash; and gives "
            "the phenomena an equally precise fourfold characterization "
            "of their instability."]),
        ("A practical payoff closing the chapter", [
            "The discourse doesn't end as pure theory; it states that "
            "a noble disciple who has clearly seen both the principle "
            "and the phenomena finds it simply impossible to fall "
            "into speculation about their own existence across past, "
            "future, or present &mdash; not because such speculation "
            "is forbidden, but because clear seeing makes it cease to "
            "arise as a live question at all."]),
    ],
    terms=[
        ("paṭiccasamuppādo",
         "&ldquo;dependent origination&rdquo; itself &mdash; defined "
         "here specifically as the underlying principle, kept "
         "distinct from the links it governs."),
        ("uppādā vā tathāgatānaṁ anuppādā vā tathāgatānaṁ, ṭhitāva sā dhātu",
         "&ldquo;whether Realized Ones arise or not, this law of "
         "nature persists&rdquo; &mdash; the famous statement that "
         "this principle is discovered, not invented by any Buddha."),
        ("paṭiccasamuppannā dhammā",
         "&ldquo;dependently originated phenomena&rdquo; &mdash; the "
         "twelve links themselves, distinguished from the principle "
         "governing them."),
        ("aniccaṁ saṅkhataṁ paṭiccasamuppannaṁ khayadhammaṁ vayadhammaṁ virāgadhammaṁ nirodhadhammaṁ",
         "&ldquo;impermanent, conditioned, dependently originated, "
         "liable to end, vanish, fade away, and cease&rdquo; "
         "&mdash; the fourfold characterization applied to each "
         "individual link."),
        ("netaṁ ṭhānaṁ vijjati",
         "&ldquo;this is not possible&rdquo; &mdash; the discourse's "
         "practical payoff, stating that clear vision makes "
         "speculative self-questions simply stop arising."),
    ],
    text_intro=(
        "The discourse in full, closing Āhāravagga. The chapter's "
        "closing summary verse, listing all ten discourse titles, is "
        "a structural index and is not reproduced as running prose "
        "here. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Dependent origination: the principle"),
        ("p", "&sect;1", "sn12.20:1.2-1.5"),
        ("p", "&sect;2", "sn12.20:2.1-2.7"),
        ("p", "&sect;3", "sn12.20:3.1-3.17"),
        ("h3", "The dependently originated phenomena"),
        ("p", "&sect;4", "sn12.20:4.1-4.14"),
        ("h3", "The payoff of seeing both clearly"),
        ("p", "&sect;5", "sn12.20:5.1-5.9"),
    ],
    quiz=[
        {"q": "What distinction does this discourse carefully maintain?",
         "opts": [
             "Between dependent origination as a principle and the twelve links it governs as phenomena",
             "Between monks and lay followers",
             "Between the past and the present alone",
             "No distinction is drawn; the terms are treated as identical"],
         "correct": 0,
         "expl": "Two related but separate concepts, each given its own definition."},
        {"q": "How does the discourse describe the status of dependent origination as a principle?",
         "opts": [
             "As persisting whether or not any Realized One arises to discover it",
             "As invented by Gotama specifically",
             "As something that changes with each new Buddha",
             "As applicable only during the Buddha's own lifetime"],
         "correct": 0,
         "expl": "A discovered regularity of nature, not an original invention."},
        {"q": "What role does the Buddha play regarding this principle, according to the discourse?",
         "opts": [
             "He awakens to it and comprehends it, then explains and reveals it",
             "He creates the principle from nothing",
             "He has no relationship to the principle at all",
             "He alone is exempt from the principle"],
         "correct": 0,
         "expl": "Discovery and revelation, not origination."},
        {"q": "How are the dependently originated phenomena (the twelve links) characterized?",
         "opts": [
             "As impermanent, conditioned, and liable to end, vanish, fade away, and cease",
             "As permanent and unchanging",
             "As entirely independent of any conditions",
             "As identical in nature to the principle governing them"],
         "correct": 0,
         "expl": "A deliberate contrast between the fixed rule and its ever-changing instances."},
        {"q": "What does clear vision of both the principle and the phenomena make impossible, according to the discourse's close?",
         "opts": [
             "Falling into speculation about one's own existence across past, future, or present",
             "Practicing meditation at all",
             "Teaching the Dhamma to others",
             "Achieving any further spiritual progress"],
         "correct": 0,
         "expl": "The discourse's practical payoff, closing the chapter."},
        {"q": "Why does speculation about self become impossible, according to the discourse?",
         "opts": [
             "Not because it's forbidden, but because clear seeing makes it cease to arise as a live question",
             "Because the Buddha personally prohibits such questions",
             "Because such questions are considered blasphemous",
             "Because monks are forbidden from thinking about the past or future"],
         "correct": 0,
         "expl": "A psychological and epistemic outcome, not an external rule."},
        {"q": "What example of a speculative question about the past does the discourse name?",
         "opts": [
             "\"Did I exist in the past? What was I in the past?\"",
             "\"What color was the Buddha's robe?\"",
             "\"How many monks attended this teaching?\"",
             "No example questions are given"],
         "correct": 0,
         "expl": "One of a cluster of questions the discourse names as no longer arising."},
        {"q": "What term describes dependent origination's precise, technical characterization in this discourse?",
         "opts": [
             "Reality, non-falseness, non-otherness, specific conditionality",
             "A poetic metaphor with no technical content",
             "An entirely mysterious, undefinable concept",
             "A term borrowed directly from another religious tradition"],
         "correct": 0,
         "expl": "A precise vocabulary, not vague description."},
        {"q": "What does this discourse close, structurally, within Nidānavagga?",
         "opts": [
             "Āhāravagga, this book's second chapter of ten discourses",
             "The entire Nidānavagga book",
             "Only a minor sub-section with no larger significance",
             "Nothing; more discourses in this chapter follow"],
         "correct": 0,
         "expl": "Confirmed by the chapter's closing summary verse listing all ten titles."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for the opening of this chapter."},
    ],
    marginalia=[
        ("A principle, kept distinct from its instances", [
            "the rule, and what the rule governs &mdash;",
            "not the same thing, carefully separated",
        ]),
        ("Discovered, not invented", [
            "persisting whether Buddhas arise or not &mdash;",
            "awakened to, then revealed",
        ]),
        ("Fixed regularity, unstable instances", [
            "the law unchanging, the links impermanent &mdash;",
            "a deliberate contrast",
        ]),
        ("Speculation, simply stopping", [
            "not forbidden, but no longer arising &mdash;",
            "clear seeing closing the question",
        ]),
    ],
    further=[
        '<a href="%s/sn12.20/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.19.html">SN 12.19 &middot; The Astute and the Foolish</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.21.html">SN 12.21 &middot; The Ten Powers</a> '
        "&mdash; opening Dasabalavagga, this book's third chapter.",
    ],
)
