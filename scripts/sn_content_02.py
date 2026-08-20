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
# 12.16. As with sn_content_01.py's sn-4.1/sn-5.10/sn-6.2 fragility, this
# is a STABLE, RECURRING regression, confirmed to reset on every full
# build of this module (not just the first time 12.16 was added) --
# 12.14's next and 12.16's prev must be manually re-patched to route
# through 12.15 after every single sn_build.py run.
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


# --------------------------------------------------------------------------- #
# SN 12.21 — Dasabalasutta
# --------------------------------------------------------------------------- #
page(
    12, 21, "Dasabala", "The Ten Powers",
    meta_title="SN 12.21 — The Ten Powers | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dasabalasutta — opening Dasabalavagga, the Buddha's own "
        "authority to teach is grounded in mastery of the five "
        "aggregates' arising and ending, generalized into the "
        "twelve-link chain. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A declaration of authority followed by an "
                 "analytical statement applied first to the five "
                 "aggregates, then generalized into the familiar "
                 "twelve-link chain"),
        ("Length", "~2.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "connects dependent origination directly to "
                       "the five aggregates for the first time in "
                       "this book"),
    ],
    why=(
        "Opening a new chapter, this discourse doesn't simply repeat "
        "the twelve-link chain; it first grounds the Buddha's "
        "authority to teach it at all &mdash; ten powers, four kinds "
        "of self-assurance, the confidence to roar a lion's roar in "
        "any assembly &mdash; and then applies a causal template not "
        "to old age and death first, but to each of the five "
        "aggregates in turn: such is form, such is its origin, such "
        "is its ending, and so through feeling, perception, choices, "
        "and consciousness. Only after this does the discourse state "
        "the abstract principle of conditionality in general terms "
        "and then give the familiar twelve-link chain as its concrete "
        "instance, connecting dependent origination explicitly to the "
        "aggregates for the first time in this book."),
    guide=[
        ("Authority established before content is taught", [
            "The discourse doesn't move directly into doctrine; it "
            "first names what grounds the Buddha's confidence to "
            "teach it at all &mdash; ten powers and four kinds of "
            "self-assurance, framed in the vivid imagery of a bull's "
            "place, a lion's roar, and a turning wheel."]),
        ("The aggregates addressed before old age and death", [
            "Rather than opening with the twelve-link chain's usual "
            "starting point, this discourse first applies its causal "
            "template to the five aggregates individually, a "
            "connection not made explicitly anywhere earlier in this "
            "book."]),
        ("The same threefold formula, run five times", [
            "Each aggregate receives an identical treatment &mdash; "
            "what it is, what its origin is, what its ending is "
            "&mdash; applied in turn to form, feeling, perception, "
            "choices, and consciousness, before the discourse moves "
            "on to anything else."]),
        ("An abstract principle stated before its concrete case", [
            "Rather than moving straight from the aggregates into the "
            "twelve-link chain, the discourse pauses to state "
            "conditionality in its most general, abstract form "
            "&mdash; when this exists, this comes to be &mdash; "
            "before showing the familiar chain as one specific "
            "instance of that general principle."]),
        ("Two frameworks united in a single discourse", [
            "By its close, this discourse has connected three "
            "distinct teachings &mdash; the aggregates, the abstract "
            "principle of conditionality, and the specific twelve-link "
            "chain &mdash; showing they describe the same underlying "
            "structure from three different angles."]),
    ],
    terms=[
        ("dasabalasamannāgato&hellip; catūhi ca vesārajjehi",
         "&ldquo;endowed with ten powers and four kinds of "
         "self-assurance&rdquo; &mdash; what grounds the Buddha's "
         "authority to teach what follows."),
        ("āsabhaṁ ṭhānaṁ paṭijānāti, parisāsu sīhanādaṁ nadati, brahmacakkaṁ pavatteti",
         "&ldquo;claims the bull's place, roars his lion's roar in "
         "the assemblies, and turns the divine wheel&rdquo; &mdash; "
         "the vivid triple image of proclaimed authority opening the "
         "discourse."),
        ("iti rūpaṁ iti rūpassa samudayo iti rūpassa atthaṅgamo",
         "&ldquo;such is form, such is the origin of form, such is "
         "the ending of form&rdquo; &mdash; the causal template "
         "applied to each of the five aggregates in turn."),
        ("imasmiṁ sati idaṁ hoti, imassuppādā idaṁ uppajjati",
         "&ldquo;when this exists, this comes to be; due to the "
         "arising of this, this arises&rdquo; &mdash; the abstract, "
         "general statement of conditionality preceding its specific "
         "instance."),
        ("yadidaṁ avijjāpaccayā saṅkhārā",
         "&ldquo;that is: ignorance is a requirement for "
         "choices&rdquo; &mdash; the familiar twelve-link chain given "
         "as the concrete case of the abstract principle just stated."),
    ],
    text_intro=(
        "The discourse in full, opening Dasabalavagga. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.21:1.2-1.7"),
        ("p", "&sect;2", "sn12.21:1.8-1.15"),
    ],
    quiz=[
        {"q": "What does this discourse establish before teaching any specific content?",
         "opts": [
             "The Buddha's own authority to teach, grounded in ten powers and four kinds of self-assurance",
             "A list of monastic rules",
             "The names of all his chief disciples",
             "A history of previous Buddhas"],
         "correct": 0,
         "expl": "Authority established before content follows."},
        {"q": "What imagery does the discourse use to describe this authority?",
         "opts": [
             "A bull's place, a lion's roar, and a turning wheel",
             "A blazing fire and a flowing river",
             "A ship crossing the ocean",
             "A tree growing from a seed"],
         "correct": 0,
         "expl": "A vivid triple image opening the discourse."},
        {"q": "What does this discourse apply its causal template to before reaching old age and death?",
         "opts": [
             "The five aggregates — form, feeling, perception, choices, consciousness",
             "The four great elements",
             "The six sense fields alone",
             "Nothing; it begins directly with old age and death"],
         "correct": 0,
         "expl": "A connection to the aggregates not made explicitly elsewhere in this book."},
        {"q": "What threefold formula is applied to each aggregate?",
         "opts": [
             "What it is, what its origin is, what its ending is",
             "Its color, its weight, its location",
             "Its name in three different languages",
             "No formula is applied; each aggregate is simply named"],
         "correct": 0,
         "expl": "An identical treatment run five times, once per aggregate."},
        {"q": "What does the discourse state before giving the twelve-link chain as a specific case?",
         "opts": [
             "The abstract, general principle of conditionality",
             "A list of the Buddha's past lives",
             "A description of the monastic robe",
             "Nothing; the chain is given with no preceding principle"],
         "correct": 0,
         "expl": "The general principle stated before its concrete instance."},
        {"q": "How many distinct frameworks does this discourse connect together?",
         "opts": [
             "Three — the aggregates, the abstract principle, and the specific twelve-link chain",
             "Only one, repeated three times with no variation",
             "Five, one for each aggregate treated as fully separate",
             "None; the frameworks remain entirely disconnected"],
         "correct": 0,
         "expl": "Showing they describe the same underlying structure from different angles."},
        {"q": "What is the first aggregate addressed in the discourse's fivefold treatment?",
         "opts": [
             "Form",
             "Consciousness",
             "Feeling",
             "Choices"],
         "correct": 0,
         "expl": "The first of five aggregates given identical causal treatment."},
        {"q": "What is the final aggregate addressed?",
         "opts": [
             "Consciousness",
             "Form",
             "Perception",
             "Craving"],
         "correct": 0,
         "expl": "Closing the fivefold sequence before the abstract principle is stated."},
        {"q": "What phrase closes this discourse, matching the standard chain formula?",
         "opts": [
             "That is how this entire mass of suffering ceases",
             "That is how the four great elements combine",
             "That is how the monastic robe should be worn",
             "No closing formula is given"],
         "correct": 0,
         "expl": "The standard cessation-sequence closing already familiar from Buddhavagga."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The setting opening this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("Authority named before doctrine taught", [
            "ten powers, four assurances &mdash;",
            "the ground for what follows",
        ]),
        ("The aggregates, addressed first", [
            "form, feeling, perception, choices, consciousness &mdash;",
            "a connection new to this book",
        ]),
        ("One formula, run five times", [
            "what it is, its origin, its ending &mdash;",
            "identical treatment for each",
        ]),
        ("Principle before instance", [
            "the abstract rule, stated first &mdash;",
            "the familiar chain as one concrete case",
        ]),
    ],
    further=[
        '<a href="%s/sn12.21/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.20.html">SN 12.20 &middot; Conditions</a> '
        "&mdash; the discourse closing Āhāravagga, immediately "
        "before this one.",
        '<a href="sn-12.22.html">SN 12.22 &middot; The Ten Powers (2nd)</a> '
        "&mdash; the next discourse, repeating this same content "
        "before adding a famous exhortation to vigorous effort.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.22 — Dutiyadasabalasutta
# --------------------------------------------------------------------------- #
page(
    12, 22, "Dutiyadasabala", "The Ten Powers (2nd)",
    meta_title="SN 12.22 — The Ten Powers (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyadasabalasutta — SN 12.21's teaching repeated, then "
        "followed by the famous vow to let only skin, sinews, and "
        "tendons remain rather than give up before the goal is "
        "reached. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 12.21's content repeated in full, followed by an "
                 "extended exhortation to vigorous effort"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the added exhortation is one of this "
                       "collection's most vivid calls to effort"),
    ],
    why=(
        "This discourse opens by repeating SN 12.21 word for word "
        "&mdash; the ten powers, the fivefold treatment of the "
        "aggregates, the twelve-link chain &mdash; but doesn't stop "
        "there. Having declared the teaching fully clarified, "
        "revealed, and illuminated, the Buddha issues one of this "
        "collection's most vivid calls to effort: let only skin, "
        "sinews, and tendons remain, let flesh and blood waste away, "
        "rather than stop trying before what's humanly achievable is "
        "achieved. What follows is a tightly reasoned case for "
        "diligence &mdash; the lazy live in suffering, the energetic "
        "live happily, and the best is reached only by the best "
        "effort, not by half measures."),
    guide=[
        ("Repetition establishing the ground for what follows", [
            "The discourse's first half isn't padding; repeating SN "
            "12.21's content in full establishes that what follows "
            "is a response to a fully explained teaching, not an "
            "exhortation issued in a vacuum."]),
        ("A teaching declared complete before the call to action", [
            "Before urging effort, the Buddha explicitly states that "
            "the teaching has been clarified, revealed, illuminated, "
            "and stripped of patchwork &mdash; there's nothing left "
            "unexplained standing between the listener and practice."]),
        ("A vow stated in the most extreme possible terms", [
            "The famous image of letting only skin, sinews, and "
            "tendons remain while flesh and blood waste away doesn't "
            "describe a moderate commitment; it names the most "
            "extreme level of persistence imaginable, refusing to "
            "stop short of what's humanly possible."]),
        ("A maxim connecting quality of effort to quality of outcome", [
            "The discourse doesn't simply praise effort in general; "
            "it states a specific principle &mdash; the best isn't "
            "reached by the worst, the best is reached by the best "
            "&mdash; making a direct link between the caliber of "
            "one's effort and what that effort can actually achieve."]),
        ("Diligence justified three separate ways", [
            "Rather than giving a single reason to practice "
            "diligently, the discourse closes with three distinct "
            "justifications &mdash; one's own good, others' good, and "
            "both together &mdash; any one of which the Buddha says "
            "is sufficient on its own."]),
    ],
    terms=[
        ("evaṁ svākkhāto&hellip; uttāno vivaṭo pakāsito chinnapilotiko",
         "&ldquo;well-explained&hellip; clarified, revealed, "
         "illuminated, and stripped of patchwork&rdquo; &mdash; "
         "marking the teaching as complete before the call to effort "
         "begins."),
        ("kāmaṁ taco ca nhāru ca aṭṭhi ca avasissatu",
         "&ldquo;gladly, let only skin, sinews, and tendons "
         "remain&rdquo; &mdash; the famous, extreme vow of total "
         "effort."),
        ("na hīnena aggassa patti hoti. aggena ca kho aggassa patti hoti",
         "&ldquo;the best isn't reached by the worst; the best is "
         "reached by the best&rdquo; &mdash; the maxim linking the "
         "quality of effort to the quality of its outcome."),
        ("maṇḍapeyyamidaṁ brahmacariyaṁ, satthā sammukhībhūto",
         "&ldquo;this spiritual life is the cream&hellip; the "
         "Teacher is before you&rdquo; &mdash; naming the rare value "
         "of the present opportunity."),
        ("attatthaṁ vā&hellip; paratthaṁ vā&hellip; ubhayatthaṁ vā",
         "&ldquo;for one's own good&hellip; for others' good&hellip; "
         "for both&rdquo; &mdash; the threefold justification "
         "closing the discourse, any one sufficient on its own."),
    ],
    text_intro=(
        "The discourse in full. The opening content, repeating SN "
        "12.21, is given here again in full as the source itself "
        "repeats it. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.22:1.2-1.9"),
        ("p", "&sect;2", "sn12.22:1.10-1.15"),
        ("p", "&sect;3", "sn12.22:2.1-2.3"),
        ("p", "&sect;4", "sn12.22:3.1-3.12"),
    ],
    quiz=[
        {"q": "How does this discourse's opening compare to SN 12.21's content?",
         "opts": [
             "It repeats SN 12.21 word for word before adding new material",
             "It contradicts SN 12.21 entirely",
             "It shares no content at all with SN 12.21",
             "It only briefly summarizes SN 12.21 in one sentence"],
         "correct": 0,
         "expl": "Full repetition establishing the ground for what follows."},
        {"q": "What does the Buddha declare about the teaching before issuing his call to effort?",
         "opts": [
             "That it has been clarified, revealed, illuminated, and stripped of patchwork",
             "That it remains partially unexplained",
             "That only advanced monks can understand it",
             "That it will be explained further in a future discourse"],
         "correct": 0,
         "expl": "Nothing left unexplained standing between the listener and practice."},
        {"q": "What famous image does the Buddha use to describe total effort?",
         "opts": [
             "Letting only skin, sinews, and tendons remain while flesh and blood waste away",
             "Climbing to the top of a mountain",
             "Crossing an ocean in a small boat",
             "Planting a single seed and waiting patiently"],
         "correct": 0,
         "expl": "One of this collection's most vivid and extreme calls to persistence."},
        {"q": "What maxim connects the quality of effort to the quality of outcome?",
         "opts": [
             "The best isn't reached by the worst; the best is reached by the best",
             "Any effort at all, regardless of quality, guarantees success",
             "Effort is irrelevant to the outcome achieved",
             "Only inherited talent determines the outcome"],
         "correct": 0,
         "expl": "A direct link between caliber of effort and what it can achieve."},
        {"q": "How does the discourse describe the spiritual life, using a vivid image?",
         "opts": [
             "As \"the cream,\" with the Teacher present before the listener",
             "As a burden to be endured reluctantly",
             "As identical to ordinary lay life",
             "As something to be postponed until later in life"],
         "correct": 0,
         "expl": "Naming the rare value of the present opportunity."},
        {"q": "How does a lazy person live, according to this discourse?",
         "opts": [
             "In suffering, mixed up with bad, unskillful qualities",
             "In perfect happiness with no drawbacks",
             "Exactly the same as an energetic person",
             "The discourse doesn't address laziness at all"],
         "correct": 0,
         "expl": "Contrasted directly with the energetic person's happy, secluded life."},
        {"q": "How many separate justifications for diligence does the discourse give at its close?",
         "opts": [
             "Three — one's own good, others' good, and both together",
             "Only one, with no alternatives given",
             "Five separate justifications",
             "None; diligence is commanded without justification"],
         "correct": 0,
         "expl": "Any one of the three said to be sufficient on its own."},
        {"q": "What does the discourse say about the fruitfulness of one's going-forth if diligence is maintained?",
         "opts": [
             "That it will not be barren, but fruitful and fertile",
             "That fruitfulness is impossible to achieve",
             "That only ordained monks can achieve fruitfulness",
             "The discourse doesn't address fruitfulness"],
         "correct": 0,
         "expl": "Connected directly to the benefit received by those who support the monastic community."},
        {"q": "What five aggregates does this discourse's opening half address, matching SN 12.21?",
         "opts": [
             "Form, feeling, perception, choices, and consciousness",
             "Earth, water, fire, and air",
             "Sight, sound, smell, taste, and touch",
             "Faith, ethics, learning, generosity, and wisdom"],
         "correct": 0,
         "expl": "The identical fivefold treatment repeated from SN 12.21."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting shared with SN 12.21."},
    ],
    marginalia=[
        ("The same teaching, repeated in full", [
            "not a summary, but the whole content again &mdash;",
            "grounding what follows in something explained",
        ]),
        ("A vow at the furthest extreme", [
            "skin, sinews, tendons alone &mdash;",
            "flesh and blood allowed to waste away",
        ]),
        ("Effort matched to outcome", [
            "the best reached only by the best &mdash;",
            "not by half measures",
        ]),
        ("Three reasons, any one enough", [
            "one's own good, others', or both &mdash;",
            "no single justification required alone",
        ]),
    ],
    further=[
        '<a href="%s/sn12.22/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.21.html">SN 12.21 &middot; The Ten Powers</a> '
        "&mdash; the discourse immediately before this one, whose "
        "content this one repeats in full before adding the "
        "exhortation to effort.",
        '<a href="sn-12.23.html">SN 12.23 &middot; Vital Conditions</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.23 — Upanisasutta
# --------------------------------------------------------------------------- #
page(
    12, 23, "Upanisa", "Vital Conditions",
    meta_title="SN 12.23 — Vital Conditions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upanisasutta — the standard chain of suffering continues "
        "past its own arising into an ascending chain from faith "
        "through joy, immersion, and disillusionment all the way to "
        "final freedom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A backward-questioning chain extending well beyond "
                 "the familiar twelve links, illustrated by a "
                 "cascading simile"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "one of the most doctrinally significant "
                       "discourses in the entire collection"),
    ],
    why=(
        "Every earlier account of dependent origination in this book "
        "has stopped at the same point: suffering. This discourse "
        "doesn't stop there. Using the identical backward-questioning "
        "method already familiar from Buddhavagga, it asks what "
        "suffering itself is a vital condition for &mdash; and the "
        "answer opens an entirely new ascending sequence: faith, "
        "then joy, rapture, tranquility, bliss, immersion, true "
        "knowledge and vision, disillusionment, dispassion, freedom, "
        "and finally the knowledge of the ending of defilements "
        "itself. The familiar chain of suffering turns out to be only "
        "half the picture; suffering rightly met becomes the very "
        "condition that makes liberation possible."),
    guide=[
        ("A question extended past its usual stopping point", [
            "Every prior discourse in this book treats suffering, or "
            "old age and death, as the chain's natural endpoint; this "
            "discourse keeps asking the same backward question one "
            "step further, revealing that suffering itself has "
            "something depending on it."]),
        ("The same rigor applied to the path as to the problem", [
            "The discourse doesn't shift into vague inspirational "
            "language once it reaches faith and joy; it maintains "
            "the identical, precise conditional formula &mdash; this "
            "has a vital condition, it doesn't lack a vital condition "
            "&mdash; all the way through to final freedom."]),
        ("Suffering as a genuine turning point, not merely an endpoint", [
            "Rather than treating suffering as purely negative, the "
            "discourse names it as the specific condition for faith "
            "&mdash; suggesting that suffering, properly recognized, "
            "is what actually turns a person toward the path rather "
            "than away from it."]),
        ("An unbroken chain from ignorance to liberation", [
            "By the discourse's end, the entire sequence &mdash; from "
            "ignorance at one extreme to the knowledge of ending at "
            "the other &mdash; is stated as a single, continuous "
            "chain, with no gap or discontinuity where the familiar "
            "twelve links stop and the new sequence begins."]),
        ("A cascading simile making the whole shape visible at once", [
            "The discourse closes with an image of heavy rain on a "
            "mountaintop, filling crevices, then pools, then lakes, "
            "streams, rivers, and finally the ocean itself &mdash; "
            "each stage overflowing into the next until the whole "
            "cascade reaches its natural conclusion."]),
    ],
    terms=[
        ("jānato&hellip; passato āsavānaṁ khayaṁ vadāmi",
         "&ldquo;for one who knows and sees&hellip; I say the ending "
         "of defilements&rdquo; &mdash; grounding liberation in "
         "genuine knowledge, not blind faith alone."),
        ("saupanisaṁ&hellip; no anupanisaṁ",
         "&ldquo;has a vital condition&hellip; does not lack a vital "
         "condition&rdquo; &mdash; the recurring formula insisting "
         "nothing in the sequence, not even liberation's own "
         "approach, arises groundlessly."),
        ("dukkhūpanisā saddhā",
         "&ldquo;suffering is the vital condition for faith&rdquo; "
         "&mdash; the pivotal turn where the familiar chain of "
         "suffering becomes the spur for the ascending sequence."),
        ("saddhūpanisaṁ pāmojjaṁ&hellip; virāgūpanisā vimutti",
         "&ldquo;faith is the vital condition for joy&hellip; "
         "dispassion is the vital condition for freedom&rdquo; "
         "&mdash; the ascending chain itself, faith through freedom, "
         "in unbroken sequence."),
        ("uparipabbate thullaphusitake deve vassante&hellip; mahāsamuddaṁ paripūrenti",
         "&ldquo;when the heavens rain heavily on a mountain "
         "top&hellip; fill up the ocean&rdquo; &mdash; the cascading "
         "simile closing the discourse, each stage overflowing into "
         "the next."),
    ],
    text_intro=(
        "The discourse in full, one of the most doctrinally "
        "significant in this entire collection. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Knowing and seeing the ending of defilements"),
        ("p", "&sect;1", "sn12.23:1.2-1.9"),
        ("h3", "The ascending chain, questioned backward"),
        ("p", "&sect;2", "sn12.23:2.1-2.16"),
        ("p", "&sect;3", "sn12.23:3.1-3.15"),
        ("p", "&sect;4", "sn12.23:4.1-4.15"),
        ("p", "&sect;5", "sn12.23:5.1-5.10"),
        ("h3", "The full chain, stated in sequence"),
        ("p", "&sect;6", "sn12.23:6.1-6.22"),
        ("h3", "The cascading simile"),
        ("p", "&sect;7", "sn12.23:7.1-8.1"),
    ],
    quiz=[
        {"q": "Where do most earlier discourses in this book treat the twelve-link chain as ending?",
         "opts": [
             "At suffering, or old age and death",
             "At the six sense fields",
             "At consciousness",
             "There is no consistent stopping point in earlier discourses"],
         "correct": 0,
         "expl": "The point every prior account in this book has stopped at."},
        {"q": "What does this discourse ask, extending past that usual stopping point?",
         "opts": [
             "What suffering itself is a vital condition for",
             "Whether suffering can be avoided entirely",
             "How many kinds of suffering exist",
             "Whether suffering is real at all"],
         "correct": 0,
         "expl": "The same backward-questioning method pushed one step further."},
        {"q": "What does the discourse name as the vital condition arising from suffering?",
         "opts": [
             "Faith",
             "Ignorance",
             "Craving",
             "Consciousness"],
         "correct": 0,
         "expl": "The pivotal turn opening the ascending sequence."},
        {"q": "What formula does the discourse maintain consistently, even once it reaches faith and joy?",
         "opts": [
             "That each stage has a vital condition, not lacking one",
             "A shift into purely poetic, non-technical language",
             "A claim that these stages require no further explanation",
             "A denial that these stages are actually conditioned at all"],
         "correct": 0,
         "expl": "The identical precision applied to the path as to the problem."},
        {"q": "What is the final term in the ascending chain?",
         "opts": [
             "The knowledge of the ending of defilements",
             "Faith",
             "Rapture",
             "Ignorance"],
         "correct": 0,
         "expl": "The chain's ultimate destination, full liberation itself."},
        {"q": "What comes immediately after immersion (samādhi) in the ascending sequence?",
         "opts": [
             "True knowledge and vision",
             "Rapture",
             "Faith",
             "Grasping"],
         "correct": 0,
         "expl": "One step in the precise, ordered ascending chain."},
        {"q": "What simile closes the discourse?",
         "opts": [
             "Rain on a mountaintop cascading through pools, lakes, streams, and rivers into the ocean",
             "A lamp lit in a dark room",
             "A tree growing from a small seed",
             "A chariot assembled from many parts"],
         "correct": 0,
         "expl": "Each stage overflowing into the next, reaching the ocean at last."},
        {"q": "Does the discourse treat suffering as purely negative?",
         "opts": [
             "No — it names suffering as the specific condition for faith",
             "Yes — suffering is described as having no further consequence",
             "Yes — the discourse recommends avoiding suffering entirely",
             "The discourse takes no position on the nature of suffering"],
         "correct": 0,
         "expl": "Suffering rightly met becomes a genuine turning point, not merely an endpoint."},
        {"q": "How is the entire sequence from ignorance to liberation described by the discourse's close?",
         "opts": [
             "As a single, continuous, unbroken chain",
             "As two entirely separate and unrelated chains",
             "As a chain with several unexplained gaps",
             "As a sequence that resets partway through"],
         "correct": 0,
         "expl": "No discontinuity between the familiar twelve links and the ascending sequence."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("Past the usual stopping point", [
            "suffering, questioned one step further &mdash;",
            "not the chain's actual end after all",
        ]),
        ("The same rigor, applied upward", [
            "faith and joy, no less conditioned &mdash;",
            "than ignorance and craving",
        ]),
        ("Suffering as a turning, not a dead end", [
            "the specific condition for faith &mdash;",
            "properly met, not merely endured",
        ]),
        ("One unbroken chain, start to finish", [
            "ignorance to final freedom &mdash;",
            "no gap, no separate sequence",
        ]),
    ],
    further=[
        '<a href="%s/sn12.23/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.22.html">SN 12.22 &middot; The Ten Powers (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.24.html">SN 12.24 &middot; Followers of Other Religions</a> '
        "&mdash; the next discourse, where Sāriputta reduces an "
        "entire philosophical debate to a single word: contact.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.24 — Aññatitthiyasutta
# --------------------------------------------------------------------------- #
page(
    12, 24, "Aññatitthiya", "Followers of Other Religions",
    meta_title="SN 12.24 — Followers of Other Religions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aññatitthiyasutta — Sāriputta reduces a four-way "
        "philosophical debate about suffering to a single dependent "
        "condition, contact, confirmed by the Buddha and matched by "
        "Ānanda's own mastery. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, the Bamboo Grove &mdash; opening at a "
                    "monastery of wanderers from other traditions"),
        ("Speakers", "Sāriputta, wanderers of other religions, "
                     "Ānanda, and finally the Buddha himself"),
        ("Form", "A philosophical challenge answered twice over "
                 "&mdash; once by Sāriputta, once confirmed and "
                 "retold by the Buddha &mdash; closing with Ānanda's "
                 "own demonstration"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "an elegant philosophical move worth reading "
                       "carefully"),
    ],
    why=(
        "Wanderers of other traditions press Sāriputta with the same "
        "four-way question already seen from Kassapa and Timbaruka: "
        "is suffering self-made, other-made, both, or neither? "
        "Rather than picking a side, Sāriputta reframes the entire "
        "debate around a single word: suffering, the Buddha teaches, "
        "is dependent on contact. And crucially, every one of the "
        "four positions the wanderers name still depends on contact "
        "to be experienced at all &mdash; none of them can claim to "
        "feel what they're theorizing about apart from it. The "
        "Buddha confirms Sāriputta's answer as exactly right, then "
        "invites Ānanda to demonstrate the same understanding in "
        "fuller detail, which he does by walking the entire chain "
        "himself."),
    guide=[
        ("A question posed to a disciple, not to the Buddha directly", [
            "Unlike SN 12.17 and SN 12.18, where the same tetralemma "
            "was put directly to the Buddha, here it's addressed to "
            "Sāriputta, testing whether his understanding matches his "
            "teacher's without the Buddha present to answer it "
            "himself."]),
        ("A single word answering a four-way debate", [
            "Rather than engaging with each of the four positions in "
            "turn, Sāriputta collapses the whole question into one "
            "phrase &mdash; suffering is dependent on contact &mdash; "
            "sidestepping the debate's own terms entirely."]),
        ("Every position shown to share the same hidden dependency", [
            "The elegance of the answer lies in what it does to all "
            "four positions at once: whether someone claims suffering "
            "is self-made, other-made, both, or neither, none of them "
            "could actually experience what they're describing apart "
            "from contact &mdash; the debate itself rests on ground "
            "none of the debaters have examined."]),
        ("An answer confirmed, not merely accepted", [
            "The Buddha doesn't simply approve of Sāriputta's answer "
            "in passing; he explicitly recounts facing the identical "
            "question from the same wanderers and giving the "
            "identical reply, making the confirmation personal and "
            "specific rather than generic praise."]),
        ("A second demonstration, freely offered rather than tested", [
            "When Ānanda marvels that so much could be captured in a "
            "single word, the Buddha doesn't simply explain further "
            "himself; he invites Ānanda to clarify the matter in his "
            "own words, and Ānanda proves equal to the task, walking "
            "the full chain from old age and death back to the six "
            "sense fields and forward again through its cessation."]),
    ],
    terms=[
        ("sayaṅkataṁ dukkhaṁ&hellip; paraṅkataṁ dukkhaṁ",
         "&ldquo;suffering made by oneself&hellip; made by "
         "another&rdquo; &mdash; the same fourfold question already "
         "seen from Kassapa and Timbaruka, now posed to Sāriputta."),
        ("paṭiccasamuppannaṁ kho dukkhaṁ vuttaṁ bhagavatā. kiṁ paṭicca? phassaṁ paṭicca",
         "&ldquo;the Buddha has said that suffering is dependently "
         "originated. Dependent on what? Dependent on contact&rdquo; "
         "&mdash; Sāriputta's single-phrase reframing of the entire "
         "debate."),
        ("te vata aññatra phassā paṭisaṁvedissantīti netaṁ ṭhānaṁ vijjati",
         "&ldquo;it's impossible that they will experience that "
         "without contact&rdquo; &mdash; the point that all four "
         "philosophical positions equally depend on contact to be "
         "experienced at all."),
        ("sādhu sādhu, ānanda&hellip; yathā taṁ sāriputto sammā byākaramāno byākareyya",
         "&ldquo;good, good, Ānanda!&hellip; it's just as Sāriputta "
         "has so rightly explained&rdquo; &mdash; the Buddha's "
         "specific, personal confirmation, matched by his own "
         "identical account facing the same question."),
        ("taññevettha paṭibhātu",
         "&ldquo;clarify this matter yourself&rdquo; &mdash; the "
         "Buddha inviting Ānanda to demonstrate his own understanding "
         "rather than explaining it for him."),
    ],
    text_intro=(
        "The discourse in full. Several passages repeating earlier "
        "content are elided in the source exactly as bilara-data "
        "preserves them. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.24:1.2-2.2"),
        ("p", "&sect;2", "sn12.24:3.1-3.6"),
        ("p", "&sect;3", "sn12.24:4.1-6.4"),
        ("p", "&sect;4", "sn12.24:7.1-8.5"),
        ("p", "&sect;5", "sn12.24:17.1-17.3"),
        ("p", "&sect;6", "sn12.24:18.1-18.6"),
        ("p", "&sect;7", "sn12.24:19.1-19.5"),
        ("p", "&sect;8", "sn12.24:20.1-20.5"),
        ("p", "&sect;9", "sn12.24:21.1-21.17"),
    ],
    quiz=[
        {"q": "Who do the wanderers of other religions initially address their fourfold question to?",
         "opts": [
             "Sāriputta, rather than the Buddha directly",
             "The Buddha himself, in person",
             "Ānanda alone",
             "A group of unnamed junior monks"],
         "correct": 0,
         "expl": "Testing whether a disciple's understanding matches the teacher's."},
        {"q": "How does Sāriputta answer the four-way question about suffering?",
         "opts": [
             "By reframing it entirely: suffering is dependent on contact",
             "By picking the first of the four positions as correct",
             "By refusing to answer at all",
             "By claiming the question is entirely meaningless"],
         "correct": 0,
         "expl": "Sidestepping the debate's own terms with a single reframing word."},
        {"q": "What does Sāriputta point out that all four positions share?",
         "opts": [
             "None of them could be experienced apart from contact",
             "All four are equally correct simultaneously",
             "All four were invented by the same teacher",
             "None of the four positions actually mention suffering"],
         "correct": 0,
         "expl": "A hidden dependency none of the four debaters have examined."},
        {"q": "How does the Buddha respond when he learns of Sāriputta's answer?",
         "opts": [
             "He confirms it specifically, recounting having given the identical answer himself",
             "He corrects Sāriputta's answer as mistaken",
             "He declines to comment on the exchange",
             "He punishes Sāriputta for speaking without permission"],
         "correct": 0,
         "expl": "A personal, specific confirmation rather than generic praise."},
        {"q": "Who first reports the exchange between Sāriputta and the wanderers to the Buddha?",
         "opts": [
             "Ānanda, who overheard the discussion",
             "Sāriputta himself, immediately afterward",
             "One of the wanderers, dissatisfied with the answer",
             "No one reports it; the Buddha already knew"],
         "correct": 0,
         "expl": "Ānanda's overhearing sets up the discourse's second half."},
        {"q": "What does Ānanda marvel at regarding Sāriputta's answer?",
         "opts": [
             "That so much could be captured in a single word",
             "That the wanderers accepted the answer without argument",
             "That the Buddha had never taught this before",
             "That Sāriputta spoke without being asked"],
         "correct": 0,
         "expl": "The elegance of the single-word reframing."},
        {"q": "How does the Buddha respond to Ānanda's request for a fuller explanation?",
         "opts": [
             "He invites Ānanda to clarify the matter himself",
             "He refuses to allow any further explanation",
             "He explains it fully himself without involving Ānanda",
             "He tells Ānanda the question cannot be answered further"],
         "correct": 0,
         "expl": "A demonstration freely offered to Ānanda, not simply given by the Buddha."},
        {"q": "What does Ānanda do when asked to clarify the matter?",
         "opts": [
             "He walks the full twelve-link chain from old age and death back to the six sense fields",
             "He declines, saying he is unable to explain further",
             "He repeats only the single word \"contact\" without elaboration",
             "He asks a different monk to answer in his place"],
         "correct": 0,
         "expl": "Proving equal to the task the Buddha set for him."},
        {"q": "What triggers Sāriputta's decision to visit the monastery of other wanderers in the first place?",
         "opts": [
             "It being too early to wander for alms in Rājagaha",
             "A formal invitation from the wanderers",
             "An order from the Buddha to investigate their teachings",
             "A dispute that needed mediating"],
         "correct": 0,
         "expl": "An ordinary, practical reason opening the discourse."},
        {"q": "Where does this discourse take place?",
         "opts": [
             "Near Rājagaha, in the Bamboo Grove",
             "At Sāvatthī",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "A setting distinct from most of this chapter's Sāvatthī backdrop."},
    ],
    marginalia=[
        ("A question tested on a disciple", [
            "not put to the Buddha directly &mdash;",
            "does the student's answer match?",
        ]),
        ("One word, answering four positions", [
            "\"dependent on contact\" &mdash;",
            "sidestepping the debate's own terms",
        ]),
        ("A shared blind spot, named", [
            "none of the four escape contact &mdash;",
            "the ground none of them examined",
        ]),
        ("Confirmed twice, then demonstrated a third time", [
            "Sāriputta, then the Buddha, then Ānanda &mdash;",
            "the same understanding, independently shown",
        ]),
    ],
    further=[
        '<a href="%s/sn12.24/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.23.html">SN 12.23 &middot; Vital Conditions</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.25.html">SN 12.25 &middot; With Bhūmija</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.25 — Bhūmijasutta
# --------------------------------------------------------------------------- #
page(
    12, 25, "Bhūmija", "With Bhūmija",
    meta_title="SN 12.25 — With Bhūmija | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bhūmijasutta — the same reduction of a philosophical "
        "debate to contact, now extended into a detailed taxonomy of "
        "how pleasure and pain actually arise through body, speech, "
        "and mind. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "Bhūmija, Sāriputta, Ānanda, and finally the "
                     "Buddha himself"),
        ("Form", "The same pattern as SN 12.24, extended with a "
                 "detailed taxonomy of bodily, verbal, and mental "
                 "action"),
        ("Length", "~5.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "repeats SN 12.24's structure before extending "
                       "it into genuinely new material"),
    ],
    why=(
        "This discourse opens by retracing SN 12.24's exact pattern "
        "&mdash; a monk poses the same fourfold question, this time "
        "about pleasure and pain rather than suffering alone, "
        "Sāriputta reduces it to a single word, contact, Ānanda "
        "overhears and reports it, and the Buddha confirms the "
        "answer as his own. But this discourse doesn't stop where SN "
        "12.24 did. The Buddha goes on to break down exactly how "
        "pleasure and pain actually arise: through bodily, verbal, "
        "and mental action, each of which can be self-instigated or "
        "instigated by others, done with deliberation or without "
        "&mdash; and every single one of these channels, the "
        "discourse insists, still has ignorance fallen into it, "
        "unless that ignorance has genuinely ceased."),
    guide=[
        ("A familiar pattern retraced before new ground is broken", [
            "The discourse's first half is a close repetition of SN "
            "12.24's structure &mdash; the fourfold question, "
            "Sāriputta's reduction to contact, Ānanda's report, the "
            "Buddha's confirmation &mdash; establishing continuity "
            "before the discourse moves into genuinely new territory."]),
        ("Three channels named, not left as one general category", [
            "Rather than speaking of action in general, the Buddha "
            "distinguishes bodily, verbal, and mental action "
            "specifically, each identified as its own distinct "
            "channel through which pleasure and pain can arise "
            "internally."]),
        ("A further distinction within each channel", [
            "Each of the three channels is further split by two "
            "additional questions: was the action self-instigated or "
            "instigated by another, and was it done with deliberation "
            "or without &mdash; producing a genuinely detailed map of "
            "how experience actually comes about."]),
        ("Ignorance found in every branch of the map", [
            "No matter which combination of channel, source, and "
            "deliberation is in play, the discourse states plainly "
            "that ignorance is included in all of them &mdash; even "
            "self-instigated, carefully deliberated action remains "
            "conditioned by ignorance unless that ignorance has "
            "actually ceased."]),
        ("A conclusion stated in terms of absence, not just presence", [
            "The discourse doesn't only describe how pleasure and "
            "pain arise while ignorance persists; it closes by "
            "describing what happens when ignorance fully fades away "
            "&mdash; the entire basis for such arising simply ceases "
            "to exist, described fourfold as no field, no ground, no "
            "basis, no foundation remaining."]),
    ],
    terms=[
        ("sayaṅkataṁ sukhadukkhaṁ",
         "&ldquo;pleasure and pain made by oneself&rdquo; &mdash; "
         "the same fourfold question already seen in SN 12.17, SN "
         "12.18, and SN 12.24, now posed to Sāriputta by Bhūmija."),
        ("phassaṁ paṭicca",
         "&ldquo;dependent on contact&rdquo; &mdash; Sāriputta's "
         "identical reduction of the debate, confirmed again by the "
         "Buddha."),
        ("kāyasañcetanāhetu&hellip; vacīsañcetanāhetu&hellip; manosañcetanāhetu",
         "&ldquo;the intention that gives rise to bodily&hellip; "
         "verbal&hellip; mental action&rdquo; &mdash; the threefold "
         "breakdown of channels through which pleasure and pain "
         "actually arise, genuinely new content beyond SN 12.24."),
        ("sāmaṁ vā&hellip; pare vā&hellip; sampajāno vā&hellip; asampajāno vā",
         "&ldquo;by oneself&hellip; or by others&hellip; with "
         "deliberation&hellip; or without deliberation&rdquo; "
         "&mdash; the further fourfold matrix applied to each of the "
         "three channels."),
        ("imesu dhammesu avijjā anupatitā",
         "&ldquo;ignorance is included in all these things&rdquo; "
         "&mdash; the point that even self-instigated, deliberate "
         "action remains conditioned by underlying ignorance."),
    ],
    text_intro=(
        "The discourse in full. Several passages repeating earlier "
        "content are elided in the source exactly as bilara-data "
        "preserves them. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.25:1.2-2.6"),
        ("p", "&sect;2", "sn12.25:3.1-5.4"),
        ("p", "&sect;3", "sn12.25:6.1-7.5"),
        ("p", "&sect;4", "sn12.25:10.1-10.3"),
        ("p", "&sect;5", "sn12.25:11.1-11.4"),
        ("p", "&sect;6", "sn12.25:14.1-14.3"),
    ],
    quiz=[
        {"q": "How does this discourse's first half compare to SN 12.24's structure?",
         "opts": [
             "It closely retraces the same pattern, now concerning pleasure and pain rather than suffering alone",
             "It shares no similarity with SN 12.24 at all",
             "It directly contradicts SN 12.24's conclusion",
             "It is told entirely in verse, unlike SN 12.24's prose"],
         "correct": 0,
         "expl": "Continuity established before the discourse moves into new territory."},
        {"q": "Who poses the fourfold question to Sāriputta in this discourse?",
         "opts": [
             "Bhūmija",
             "Ānanda",
             "The Buddha himself",
             "Timbaruka"],
         "correct": 0,
         "expl": "A different questioner than SN 12.24's wanderers, though the pattern matches."},
        {"q": "What three channels does the Buddha distinguish for how pleasure and pain arise?",
         "opts": [
             "Bodily, verbal, and mental action",
             "Sight, sound, and smell",
             "Past, present, and future",
             "Only one channel is named, not three"],
         "correct": 0,
         "expl": "Genuinely new content extending beyond SN 12.24's single-word reduction."},
        {"q": "What further distinction is applied to each of these three channels?",
         "opts": [
             "Whether self-instigated or instigated by another, and whether deliberate or not",
             "Whether performed in daylight or at night",
             "Whether performed by a monk or a layperson",
             "No further distinction is applied"],
         "correct": 0,
         "expl": "A detailed map of how experience actually comes about."},
        {"q": "What does the discourse say is present in every combination of channel, source, and deliberation?",
         "opts": [
             "Ignorance",
             "Craving alone, with no role for ignorance",
             "Nothing; each combination is entirely independent",
             "Wisdom, in every single case"],
         "correct": 0,
         "expl": "Even self-instigated, deliberate action remains conditioned by ignorance."},
        {"q": "What happens to the basis for pleasure and pain's arising when ignorance fully ceases?",
         "opts": [
             "It ceases entirely — no field, ground, basis, or foundation for it remains",
             "It continues exactly as before",
             "It only partially diminishes",
             "The discourse doesn't address what happens when ignorance ceases"],
         "correct": 0,
         "expl": "A conclusion stated in terms of complete absence, not partial reduction."},
        {"q": "How does the Buddha respond when he learns of Sāriputta's answer to Bhūmija?",
         "opts": [
             "He confirms it, matching his own confirmation in SN 12.24",
             "He corrects Sāriputta's answer as mistaken",
             "He declines to comment",
             "He punishes Sāriputta for answering without permission"],
         "correct": 0,
         "expl": "The same pattern of confirmation seen in SN 12.24."},
        {"q": "Who reports the exchange between Sāriputta and Bhūmija to the Buddha?",
         "opts": [
             "Ānanda, who overheard the discussion",
             "Bhūmija himself",
             "Sāriputta immediately afterward",
             "No one reports it"],
         "correct": 0,
         "expl": "Matching the identical structural role Ānanda plays in SN 12.24."},
        {"q": "Does this discourse address pleasure and pain together, or suffering alone?",
         "opts": [
             "Pleasure and pain together, broader than SN 12.24's focus on suffering",
             "Only suffering, identical to SN 12.24's scope",
             "Only pleasure, with no mention of pain",
             "Neither; the topic is unrelated to feeling"],
         "correct": 0,
         "expl": "A broader framing than SN 12.24's narrower topic."},
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
        ("A familiar pattern, then new ground", [
            "the same reduction to contact &mdash;",
            "before the discourse goes further",
        ]),
        ("Three channels, not one general category", [
            "body, speech, and mind, each distinct &mdash;",
            "a detailed map, not a single word",
        ]),
        ("A further split within each channel", [
            "self or other, deliberate or not &mdash;",
            "the map growing more precise",
        ]),
        ("Ignorance found in every branch", [
            "even deliberate, self-chosen action &mdash;",
            "still conditioned, until it ceases entirely",
        ]),
    ],
    further=[
        '<a href="%s/sn12.25/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.24.html">SN 12.24 &middot; Followers of Other Religions</a> '
        "&mdash; the discourse whose pattern this one retraces before "
        "extending it.",
        '<a href="sn-12.26.html">SN 12.26 &middot; With Upavāṇa</a> '
        "&mdash; the next discourse, a third and more compact "
        "iteration of the same reduction to contact.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.26 — Upavāṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 26, "Upavāṇa", "With Upavāṇa",
    meta_title="SN 12.26 — With Upavāṇa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upavāṇasutta — a third, most compact iteration of the "
        "reduction of a philosophical debate about suffering to a "
        "single dependent condition, asked this time directly of the "
        "Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and the monk Upavāṇa"),
        ("Form", "The same fourfold question and single-word "
                 "reduction as SN 12.24, asked directly rather than "
                 "mediated through Sāriputta"),
        ("Length", "~2.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the most compact of three closely related "
                       "discourses, worth reading for its economy"),
    ],
    why=(
        "This is the third time in close succession that this "
        "collection reduces the same fourfold debate about suffering "
        "to a single word: contact. Where SN 12.24 staged the "
        "question through Sāriputta and a group of wanderers, "
        "confirmed later by the Buddha, and SN 12.25 extended the "
        "same pattern into a detailed taxonomy of action, this "
        "discourse strips the exchange down to its simplest form "
        "&mdash; the monk Upavāṇa asks the Buddha directly, and "
        "receives the identical answer with none of the surrounding "
        "narrative framing."),
    guide=[
        ("The third iteration of a now-familiar pattern", [
            "By this point in the chapter, the fourfold question and "
            "its reduction to contact has appeared in close succession "
            "across several discourses; this reading guide treats "
            "this repetition honestly rather than searching for a "
            "distinction the text itself doesn't draw."]),
        ("Asked directly, without a relayed conversation", [
            "Unlike SN 12.24 and SN 12.25, where the question first "
            "passes through Sāriputta and is only later confirmed by "
            "the Buddha via Ānanda's report, here Upavāṇa poses the "
            "question directly to the Buddha, with no intermediary "
            "narrative at all."]),
        ("Suffering specifically, not the broader pleasure and pain", [
            "This discourse returns to SN 12.24's narrower topic of "
            "suffering alone, rather than SN 12.25's broader framing "
            "around pleasure and pain together."]),
        ("No extended taxonomy this time", [
            "Where SN 12.25 went on to distinguish bodily, verbal, "
            "and mental channels of action, this discourse ends "
            "immediately after the core reduction, without extending "
            "into that further analysis."]),
        ("Economy itself as the point worth noticing", [
            "Read after its two companions, this discourse's real "
            "interest lies in its brevity: the same insight, "
            "stripped down to its barest form, still lands with the "
            "same force."]),
    ],
    terms=[
        ("sayaṅkataṁ dukkhaṁ",
         "&ldquo;suffering made by oneself&rdquo; &mdash; the same "
         "fourfold question, here posed directly to the Buddha."),
        ("phassaṁ paṭicca",
         "&ldquo;dependent on contact&rdquo; &mdash; the identical "
         "single-word reduction given in SN 12.24 and SN 12.25."),
        ("te vata aññatra phassā paṭisaṁvedissantīti netaṁ ṭhānaṁ vijjati",
         "&ldquo;it's impossible that they will experience that "
         "without contact&rdquo; &mdash; the same point about all "
         "four positions sharing a hidden dependency."),
        ("upavāṇa",
         "&ldquo;Upavāṇa&rdquo; &mdash; the monk who poses this "
         "question directly, without the mediating role Sāriputta "
         "plays in SN 12.24 and SN 12.25."),
        ("na ca bhagavantaṁ abhūtena abbhācikkheyya",
         "&ldquo;and not misrepresent him with an untruth&rdquo; "
         "&mdash; Upavāṇa's own stated concern for accuracy, echoing "
         "the wanderers' and Bhūmija's identical wording."),
    ],
    text_intro=(
        "The discourse in full, the most compact of three closely "
        "related discourses. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.26:1.2-2.5"),
        ("p", "&sect;2", "sn12.26:3.1-3.4"),
        ("p", "&sect;3", "sn12.26:4.1-5.4"),
    ],
    quiz=[
        {"q": "How many times in close succession does this reduction of suffering to contact now appear in this chapter?",
         "opts": [
             "Three times, across SN 12.24, SN 12.25, and this discourse",
             "Only once, in this discourse alone",
             "Five separate times with major variations each time",
             "This is the first appearance of the pattern"],
         "correct": 0,
         "expl": "A now-familiar pattern this reading guide treats honestly as repetition."},
        {"q": "How does Upavāṇa pose his question, unlike SN 12.24 and SN 12.25?",
         "opts": [
             "Directly to the Buddha, with no intermediary narrative",
             "Through a formal written petition",
             "Through Sāriputta, exactly as in the companion discourses",
             "He does not pose a question at all"],
         "correct": 0,
         "expl": "No relayed conversation through Sāriputta and Ānanda this time."},
        {"q": "What topic does this discourse address, matching SN 12.24 rather than SN 12.25?",
         "opts": [
             "Suffering specifically, not the broader pleasure and pain",
             "Pleasure and pain together",
             "An entirely unrelated topic",
             "The topic is left unspecified"],
         "correct": 0,
         "expl": "A return to SN 12.24's narrower framing."},
        {"q": "Does this discourse extend into the taxonomy of bodily, verbal, and mental action seen in SN 12.25?",
         "opts": [
             "No — it ends immediately after the core reduction",
             "Yes, in even greater detail than SN 12.25",
             "Yes, but only for bodily action",
             "The discourse addresses only mental action"],
         "correct": 0,
         "expl": "A more compact discourse without the extended analysis."},
        {"q": "What does the Buddha name as suffering's dependent condition?",
         "opts": [
             "Contact",
             "Ignorance directly, bypassing contact",
             "Craving directly",
             "No condition is named"],
         "correct": 0,
         "expl": "The identical single-word answer given across all three related discourses."},
        {"q": "What do all four of the wanderers' positions share, according to the Buddha's explanation?",
         "opts": [
             "None of them could be experienced apart from contact",
             "All four are equally endorsed by the Buddha",
             "None of the four positions mention suffering at all",
             "They share nothing in common"],
         "correct": 0,
         "expl": "The same underlying point already established in SN 12.24 and SN 12.25."},
        {"q": "What is worth noticing about this discourse's brevity, according to this reading guide?",
         "opts": [
             "That the same insight, stripped to its barest form, still lands with the same force",
             "That brevity indicates the teaching is less important",
             "That the discourse is incomplete and missing content",
             "That brevity makes the teaching harder to understand"],
         "correct": 0,
         "expl": "Economy itself treated as worth noticing, not as a deficiency."},
        {"q": "How does Upavāṇa frame his concern about the answer he receives?",
         "opts": [
             "Wanting to avoid misrepresenting the Buddha with an untruth",
             "Wanting to win a public debate",
             "Wanting to challenge the Buddha's authority",
             "No such concern is expressed"],
         "correct": 0,
         "expl": "Echoing the same concern for accuracy already voiced in the companion discourses."},
        {"q": "Who is the sole interlocutor addressing the Buddha in this discourse?",
         "opts": [
             "Upavāṇa",
             "Sāriputta",
             "Ānanda",
             "Bhūmija"],
         "correct": 0,
         "expl": "A different, direct questioner from the companion discourses."},
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
        ("A third telling, honestly named as such", [
            "the same reduction, once more &mdash;",
            "not searching for a difference not there",
        ]),
        ("No relay this time", [
            "asked straight to the Buddha &mdash;",
            "no Sāriputta, no Ānanda between",
        ]),
        ("Back to suffering alone", [
            "not the broader pleasure and pain &mdash;",
            "matching SN 12.24's narrower scope",
        ]),
        ("Brevity as the actual point", [
            "stripped to its barest form &mdash;",
            "still landing with the same force",
        ]),
    ],
    further=[
        '<a href="%s/sn12.26/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.25.html">SN 12.25 &middot; With Bhūmija</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.27.html">SN 12.27 &middot; Dependency</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.27 — Paccayasutta
# --------------------------------------------------------------------------- #
page(
    12, 27, "Paccaya", "Dependency",
    meta_title="SN 12.27 — Dependency | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paccayasutta — each link of the chain given a precise "
        "definition and, for the first time, explicitly connected to "
        "the noble eightfold path as the specific practice for its "
        "cessation. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A detailed definitional treatment of each link, "
                 "closing on a string of honorific titles"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the first discourse in this book to name the "
                       "eightfold path explicitly as the chain's own "
                       "practice"),
    ],
    why=(
        "This discourse doesn't just name the twelve links; it "
        "defines each one precisely, in language vivid enough that "
        "old age becomes broken teeth, grey hair, and failing "
        "faculties, and death becomes the breaking up of the "
        "aggregates and the laying to rest of the corpse. But its "
        "real significance lies elsewhere: for the first time in this "
        "book, the practice leading to each link's cessation is "
        "named explicitly &mdash; not left as a vague reference to "
        "spiritual effort, but identified specifically as the noble "
        "eightfold path, spelled out in full. Understanding the "
        "chain this way, the discourse closes, earns a noble "
        "disciple nine distinct honorific titles, ending on a "
        "striking image: standing pressed against the door to "
        "freedom from death."),
    guide=[
        ("Definitions given, not merely names listed", [
            "Rather than simply naming old age and death as the "
            "chain's starting point, the discourse defines each "
            "precisely and vividly &mdash; broken teeth, grey hair, "
            "wrinkled skin, and failing faculties for old age; "
            "passing away, disintegration, and the laying to rest of "
            "the corpse for death."]),
        ("The eightfold path named explicitly, for the first time", [
            "Every prior discourse in this book that addresses a "
            "link's cessation leaves the practice leading to it "
            "unspecified or generic; this discourse names it directly "
            "as the noble eightfold path, spelled out component by "
            "component."]),
        ("The same fourfold structure applied to choices specifically", [
            "Choices, like every other link, receive their own "
            "precise definition &mdash; three kinds, by way of body, "
            "speech, and mind &mdash; before the same origin, "
            "cessation, and eightfold-path treatment already given to "
            "old age and death."]),
        ("Nine titles, not one, for genuine understanding", [
            "The discourse doesn't settle for a single label to "
            "describe the noble disciple who understands the chain "
            "this way; it offers nine distinct honorific titles in "
            "sequence, each naming a different facet of the same "
            "accomplishment."]),
        ("A closing image of physical proximity to liberation", [
            "The final title doesn't describe understanding in "
            "abstract terms; it pictures the disciple standing "
            "pressed directly against the door to freedom from death "
            "&mdash; liberation described as immediately, physically "
            "close, not a distant future prospect."]),
    ],
    terms=[
        ("khaṇḍiccaṁ pāliccaṁ valittacatā",
         "&ldquo;broken teeth, grey hair, wrinkly skin&rdquo; "
         "&mdash; the vivid physical definition given for old age."),
        ("cuti cavanatā bhedo&hellip; kaḷevarassa nikkhepo",
         "&ldquo;passing away, disintegration&hellip; laying to rest "
         "of the corpse&rdquo; &mdash; the equally vivid definition "
         "given for death."),
        ("ayameva ariyo aṭṭhaṅgiko maggo&hellip; nirodhagāminī paṭipadā",
         "&ldquo;this noble eightfold path&hellip; the practice "
         "leading to cessation&rdquo; &mdash; the first explicit "
         "naming of the eightfold path as the specific practice for "
         "each link's cessation."),
        ("kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro",
         "&ldquo;choices by way of body, speech, and mind&rdquo; "
         "&mdash; the threefold definition given specifically for "
         "choices."),
        ("amatadvāraṁ āhacca tiṭṭhati",
         "&ldquo;stands pressing against the door to freedom from "
         "death&rdquo; &mdash; the final, vivid epithet closing the "
         "string of nine honorific titles."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.27:1.2-1.4"),
        ("p", "&sect;2", "sn12.27:2.1-2.11"),
        ("p", "&sect;3", "sn12.27:4.1-4.8"),
        ("p", "&sect;4", "sn12.27:5.1-5.2"),
    ],
    quiz=[
        {"q": "How does this discourse treat old age, compared to simply naming it?",
         "opts": [
             "It defines it precisely — broken teeth, grey hair, wrinkled skin, failing faculties",
             "It leaves old age entirely undefined",
             "It defines old age only in relation to animals, not humans",
             "It denies that old age is a real phenomenon"],
         "correct": 0,
         "expl": "A vivid, precise definition, not merely a name."},
        {"q": "What is named for the first time in this book as the practice leading to a link's cessation?",
         "opts": [
             "The noble eightfold path, spelled out component by component",
             "A vow of complete silence",
             "A specific mantra to be recited",
             "No practice is named at all"],
         "correct": 0,
         "expl": "Previously left generic or unspecified in earlier discourses."},
        {"q": "How many components make up the eightfold path as named here?",
         "opts": [
             "Eight — right view, purpose, speech, action, livelihood, effort, mindfulness, and immersion",
             "Four, matching the four noble truths alone",
             "Twelve, matching the twelve links",
             "The path is mentioned but not enumerated"],
         "correct": 0,
         "expl": "Spelled out in full rather than left as a vague reference."},
        {"q": "How are choices specifically defined in this discourse?",
         "opts": [
             "As three kinds: by way of body, speech, and mind",
             "As a single, undifferentiated category",
             "As five kinds, matching the five aggregates",
             "Choices are not defined in this discourse"],
         "correct": 0,
         "expl": "Given the same precise, fourfold treatment as old age and death."},
        {"q": "How many honorific titles does the discourse give for the noble disciple who understands the chain this way?",
         "opts": [
             "Nine distinct titles",
             "Only one title",
             "Three titles",
             "No titles are given"],
         "correct": 0,
         "expl": "Each naming a different facet of the same accomplishment."},
        {"q": "What is the final, closing image among these titles?",
         "opts": [
             "Standing pressed against the door to freedom from death",
             "Sitting quietly in a forest hut",
             "Walking slowly through a marketplace",
             "No closing image is given"],
         "correct": 0,
         "expl": "Liberation pictured as immediately, physically close."},
        {"q": "What is named as the origin of old age and death?",
         "opts": [
             "Rebirth",
             "Craving directly, bypassing rebirth",
             "Ignorance directly, bypassing all intermediate links",
             "No origin is given"],
         "correct": 0,
         "expl": "Matching the standard chain already familiar from Buddhavagga."},
        {"q": "What is named as the origin of choices specifically?",
         "opts": [
             "Ignorance",
             "Craving",
             "Consciousness",
             "Old age and death"],
         "correct": 0,
         "expl": "The chain's final link, closing the backward sequence."},
        {"q": "Does the discourse's definition of death mention the breaking up of the aggregates?",
         "opts": [
             "Yes, explicitly, alongside the laying to rest of the corpse",
             "No, the aggregates are never mentioned in this discourse",
             "Only implicitly, with no direct reference",
             "The discourse avoids describing death at all"],
         "correct": 0,
         "expl": "Part of the vivid, precise definition given for death."},
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
        ("Defined, not merely named", [
            "broken teeth, grey hair, failing faculties &mdash;",
            "old age given precise, vivid content",
        ]),
        ("The path, finally spelled out", [
            "not vague effort, but eight named steps &mdash;",
            "the first explicit naming in this book",
        ]),
        ("Choices, defined threefold", [
            "body, speech, mind &mdash;",
            "the same rigor applied throughout",
        ]),
        ("Nine titles, one closing image", [
            "pressed against the door to death's end &mdash;",
            "liberation pictured as immediately close",
        ]),
    ],
    further=[
        '<a href="%s/sn12.27/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.26.html">SN 12.26 &middot; With Upavāṇa</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.28.html">SN 12.28 &middot; A Mendicant</a> '
        "&mdash; the next discourse, restating this same content "
        "reframed around a mendicant's own direct comprehension.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.28 — Bhikkhusutta
# --------------------------------------------------------------------------- #
page(
    12, 28, "Bhikkhu", "A Mendicant",
    meta_title="SN 12.28 — A Mendicant | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bhikkhusutta — SN 12.27's definitions and eightfold-path "
        "connection restated, reframed around a mendicant's own "
        "direct comprehension of each link individually. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 12.27's content restated, reframed around a "
                 "single mendicant's direct comprehension of each "
                 "link"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a close companion to SN 12.27, worth reading "
                       "for the shift in framing"),
    ],
    why=(
        "This discourse gives the identical definitions, the "
        "identical connection to the eightfold path, and the "
        "identical string of nine honorific titles already given in "
        "SN 12.27. What changes is the frame: rather than describing "
        "a generic noble disciple who understands dependency as an "
        "abstract whole, this discourse opens by describing a "
        "mendicant who understands each of the twelve links "
        "individually, one by one, before the same detailed "
        "definitions follow. A small shift in emphasis, from the "
        "general principle to the practitioner's own direct, "
        "itemized comprehension."),
    guide=[
        ("Identical content, a different opening frame", [
            "Every definition, every connection to the eightfold "
            "path, and every closing title in this discourse matches "
            "SN 12.27 precisely; only the discourse's opening framing "
            "differs."]),
        ("A mendicant's comprehension, itemized link by link", [
            "Where SN 12.27 opens by naming dependency as a single "
            "concept to be understood, this discourse opens by "
            "listing each of the twelve links individually as "
            "something the mendicant comes to understand one at a "
            "time."]),
        ("The same fourfold formula, still intact", [
            "Despite this shift in opening frame, the fourfold "
            "pattern &mdash; understanding a thing, its origin, its "
            "cessation, and the practice leading to cessation "
            "&mdash; remains exactly as SN 12.27 gives it, applied to "
            "every link in turn."]),
        ("A closing that names the practitioner directly", [
            "Where SN 12.27 closes describing a noble disciple in "
            "general terms, this discourse closes naming this "
            "mendicant specifically, with the identical nine titles "
            "attached to the individual practitioner rather than to "
            "the category of noble disciple."]),
        ("A pairing worth reading together, not separately", [
            "Given how closely these two discourses match in "
            "substance, this reading guide treats them as a pair best "
            "understood together, with SN 12.27 supplying the fuller "
            "context for what this discourse restates in a more "
            "itemized form."]),
    ],
    terms=[
        ("bhikkhu jarāmaraṇaṁ pajānāti",
         "&ldquo;a mendicant understands old age and death&rdquo; "
         "&mdash; the discourse's opening frame, naming a specific "
         "practitioner rather than a general category."),
        ("jātiṁ pajānāti&hellip; saṅkhāre pajānāti",
         "&ldquo;they understand rebirth&hellip; they understand "
         "choices&rdquo; &mdash; each link named individually as "
         "something to be understood one at a time."),
        ("khaṇḍiccaṁ pāliccaṁ valittacatā",
         "&ldquo;broken teeth, grey hair, wrinkly skin&rdquo; "
         "&mdash; the identical vivid definition of old age already "
         "given in SN 12.27."),
        ("ayameva ariyo aṭṭhaṅgiko maggo",
         "&ldquo;this noble eightfold path&rdquo; &mdash; the "
         "identical connection to the path's cessation-practice, "
         "unchanged from SN 12.27."),
        ("ayaṁ vuccati, bhikkhave, bhikkhu diṭṭhisampanno itipi&hellip;",
         "&ldquo;this mendicant is called: &lsquo;one accomplished "
         "in view&rsquo;&hellip;&rdquo; &mdash; the identical string "
         "of nine titles, now attached to this individual "
         "practitioner rather than to noble disciples in general."),
    ],
    text_intro=(
        "The discourse in full. The middle links are elided in the "
        "source exactly as bilara-data preserves them, following "
        "patterns already established throughout this chapter. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.28:1.3-1.12"),
        ("p", "&sect;2", "sn12.28:2.1-2.11"),
        ("p", "&sect;3", "sn12.28:4.1-4.8"),
        ("p", "&sect;4", "sn12.28:5.14"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to SN 12.27's?",
         "opts": [
             "Identical definitions, eightfold-path connection, and closing titles",
             "Completely different content with no overlap",
             "A direct contradiction of SN 12.27's teaching",
             "Focused on an entirely unrelated topic"],
         "correct": 0,
         "expl": "The same substantive teaching, differently framed."},
        {"q": "How does this discourse's opening differ from SN 12.27's?",
         "opts": [
             "It describes a mendicant understanding each link individually, one by one",
             "It opens with an entirely new topic unrelated to the twelve links",
             "It omits the twelve links entirely",
             "It opens with a narrated story rather than direct teaching"],
         "correct": 0,
         "expl": "A shift from dependency as a single concept to itemized comprehension."},
        {"q": "Does the fourfold formula (thing, origin, cessation, path) remain intact in this discourse?",
         "opts": [
             "Yes — applied to every link exactly as in SN 12.27",
             "No — only the origin is addressed, not cessation or path",
             "No — the formula is reduced to twofold",
             "No — an entirely new fivefold formula replaces it"],
         "correct": 0,
         "expl": "Unchanged despite the shift in opening frame."},
        {"q": "How does this discourse's closing differ from SN 12.27's?",
         "opts": [
             "The titles are attached to this specific mendicant, rather than to noble disciples in general",
             "No closing titles are given at all",
             "A completely different set of titles is given",
             "The closing is identical in every respect, including framing"],
         "correct": 0,
         "expl": "A subtle shift from general category to individual practitioner."},
        {"q": "How many honorific titles does this discourse give, matching SN 12.27?",
         "opts": [
             "Nine",
             "Only one",
             "Three",
             "Twelve, matching the number of links"],
         "correct": 0,
         "expl": "The identical string of titles already seen in SN 12.27."},
        {"q": "How is old age defined in this discourse?",
         "opts": [
             "Identically to SN 12.27 — broken teeth, grey hair, wrinkled skin, failing faculties",
             "With an entirely different definition than SN 12.27",
             "Old age is left undefined in this version",
             "Only death is defined, not old age"],
         "correct": 0,
         "expl": "The identical vivid definition carried over unchanged."},
        {"q": "What is named as the practice leading to each link's cessation?",
         "opts": [
             "The noble eightfold path, matching SN 12.27 exactly",
             "A vow of silence",
             "A different practice than SN 12.27's",
             "No practice is named in this version"],
         "correct": 0,
         "expl": "Unchanged from SN 12.27's explicit naming."},
        {"q": "How does this reading guide recommend approaching these two discourses?",
         "opts": [
             "As a pair best read together, with SN 12.27 supplying fuller context",
             "As entirely unrelated and best read separately",
             "As contradictory teachings requiring reconciliation",
             "Only this discourse should be read; SN 12.27 is redundant"],
         "correct": 0,
         "expl": "Given how closely the two discourses match in substance."},
        {"q": "How are choices defined in this discourse?",
         "opts": [
             "As three kinds: by way of body, speech, and mind",
             "As a single undifferentiated category",
             "As five kinds",
             "Choices are not addressed in this discourse"],
         "correct": 0,
         "expl": "Matching SN 12.27's identical threefold definition."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting shared with SN 12.27."},
    ],
    marginalia=[
        ("Same content, a different opening", [
            "not dependency as a concept &mdash;",
            "a mendicant's own itemized comprehension",
        ]),
        ("The fourfold formula, unchanged", [
            "thing, origin, cessation, path &mdash;",
            "carried over intact",
        ]),
        ("Titles, now individually attached", [
            "not noble disciples in general &mdash;",
            "this specific practitioner, named",
        ]),
        ("Best read as a pair", [
            "SN 12.27's fuller context alongside &mdash;",
            "not two separate teachings",
        ]),
    ],
    further=[
        '<a href="%s/sn12.28/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.27.html">SN 12.27 &middot; Dependency</a> '
        "&mdash; the discourse immediately before this one, sharing "
        "identical content in a different frame.",
        '<a href="sn-12.29.html">SN 12.29 &middot; Ascetics and Brahmins</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.29 — Samaṇabrāhmaṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 29, "Samaṇabrāhmaṇa", "Ascetics and Brahmins",
    meta_title="SN 12.29 — Ascetics and Brahmins | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Samaṇabrāhmaṇasutta — SN 12.13's test for genuine "
        "ascetic or brahmin status returns with a single intensified "
        "verb, complete rather than ordinary understanding. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same fourfold test as SN 12.13 and SN 12.14, "
                 "reprised with a single intensified verb"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a small verbal shift on already-familiar "
                       "content, worth noting rather than overreading"),
    ],
    why=(
        "This discourse returns to territory this chapter has already "
        "covered twice: the same fourfold test of each link, the same "
        "verdict distinguishing true ascetics and brahmins from those "
        "in name only. What's different this time is a single word "
        "&mdash; where SN 12.13 and SN 12.14 asked whether someone "
        "understands (pajānāti) each link, this discourse asks "
        "whether they completely understand (parijānāti) it, a "
        "slightly intensified standard for the same underlying test."),
    guide=[
        ("A third pass over already-familiar ground", [
            "Rather than treating this discourse as introducing new "
            "content, this reading guide names it honestly as a third "
            "iteration of the same test already given in SN 12.13 and "
            "SN 12.14, distinguished by a single verbal shift rather "
            "than substantive new teaching."]),
        ("A single intensified verb carrying the whole difference", [
            "Where the earlier pair used pajānāti, a general term for "
            "understanding, this discourse consistently uses "
            "parijānāti, suggesting a fuller, more complete grasp "
            "&mdash; the only substantive change from the earlier "
            "discourses' wording."]),
        ("The same verdict, the same stakes", [
            "Despite this verbal shift, the discourse's conclusion "
            "matches its predecessors precisely: failing this test on "
            "any link means the Buddha doesn't deem someone a true "
            "ascetic or brahmin, regardless of title."]),
        ("The same two-part symmetry preserved once more", [
            "As in SN 12.13 and SN 12.14, this discourse gives equal, "
            "parallel treatment to both failure and success, closing "
            "with the identical positive verdict for those who meet "
            "the standard."]),
        ("A reprise placed deliberately near this chapter's close", [
            "Returning to this theme so close to Dasabalavagga's end "
            "suggests a deliberate echo rather than coincidence, "
            "tying this chapter's closing material back to a question "
            "already raised early in Āhāravagga."]),
    ],
    terms=[
        ("na parijānanti",
         "&ldquo;don't completely understand&rdquo; &mdash; the "
         "intensified verb distinguishing this discourse's wording "
         "from SN 12.13's plainer pajānāti."),
        ("jarāmaraṇaṁ na parijānanti, jarāmaraṇasamudayaṁ na parijānanti",
         "&ldquo;don't completely understand old age and death, "
         "their origin&rdquo; &mdash; the fourfold test's first "
         "application, matching SN 12.13's structure exactly."),
        ("na mete&hellip; samaṇā vā brāhmaṇā vā samaṇesu vā samaṇasammatā",
         "&ldquo;I don't deem them as true ascetics and "
         "brahmins&rdquo; &mdash; the identical verdict already given "
         "in SN 12.13 and SN 12.14."),
        ("sāmaññatthaṁ vā brahmaññatthaṁ&hellip; sayaṁ abhiññā sacchikatvā",
         "&ldquo;the goal of life as an ascetic or brahmin&hellip; "
         "realized with their own insight&rdquo; &mdash; the same "
         "standard of personal realization already established in "
         "SN 12.13."),
        ("te kho me&hellip; samaṇasammatā",
         "&ldquo;I deem them as true ascetics and brahmins&rdquo; "
         "&mdash; the positive counterpart verdict, closing the "
         "discourse exactly as its predecessors close."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.29:1.3-1.16"),
        ("p", "&sect;2", "sn12.29:2.1-2.11"),
    ],
    quiz=[
        {"q": "How does this discourse relate to SN 12.13 and SN 12.14?",
         "opts": [
             "It returns to the same fourfold test, distinguished mainly by a single intensified verb",
             "It introduces an entirely new, unrelated teaching",
             "It directly contradicts the earlier discourses' verdict",
             "It replaces the twelve-link chain with a different framework"],
         "correct": 0,
         "expl": "A third pass over already-familiar ground, named honestly as such."},
        {"q": "What verb does this discourse use, differing from SN 12.13's wording?",
         "opts": [
             "Parijānāti, \"completely understand,\" rather than the plainer pajānāti",
             "An entirely unrelated verb with no connection to understanding",
             "The identical verb with no change at all",
             "A verb meaning \"to forget\""],
         "correct": 0,
         "expl": "A slightly intensified standard for the same underlying test."},
        {"q": "Does this verbal shift change the discourse's fundamental verdict?",
         "opts": [
             "No — the verdict and stakes match SN 12.13 and SN 12.14 precisely",
             "Yes — it reverses the entire verdict",
             "Yes — it introduces a third, intermediate category",
             "Yes — it removes any verdict from the discourse entirely"],
         "correct": 0,
         "expl": "The same conclusion, only the wording intensified."},
        {"q": "What happens to someone who fails this test on even one link?",
         "opts": [
             "The Buddha doesn't deem them a true ascetic or brahmin, regardless of title",
             "They are given a probationary period to improve",
             "The discourse offers no verdict for partial failure",
             "They are still deemed genuine if they fail only one link"],
         "correct": 0,
         "expl": "Matching the uncompromising standard from the earlier pair."},
        {"q": "Does the discourse give equal treatment to both failure and success?",
         "opts": [
             "Yes — the same two-part symmetry as SN 12.13 and SN 12.14",
             "No — only failure is addressed",
             "No — only success is addressed",
             "The discourse addresses neither failure nor success"],
         "correct": 0,
         "expl": "The identical balanced structure preserved once more."},
        {"q": "Where in Dasabalavagga does this reprise of the theme appear?",
         "opts": [
             "Near the chapter's close, suggesting a deliberate echo",
             "At the very opening of the chapter",
             "Exactly in the chapter's middle with no significance to placement",
             "This is actually the first appearance of the theme in the whole book"],
         "correct": 0,
         "expl": "Tying the chapter's closing material back to earlier content."},
        {"q": "What is the first link the fourfold test is applied to?",
         "opts": [
             "Old age and death",
             "Ignorance",
             "Consciousness",
             "Craving"],
         "correct": 0,
         "expl": "Matching the standard starting point already familiar from this chapter."},
        {"q": "What is the standard given for genuine ascetic or brahmin status?",
         "opts": [
             "Realizing the goal with one's own insight, matching SN 12.13 exactly",
             "A different, more lenient standard than SN 12.13's",
             "A different, stricter standard entirely replacing SN 12.13's",
             "No standard is specified in this version"],
         "correct": 0,
         "expl": "Identical substantive content to the earlier discourses."},
        {"q": "What is the twelfth and final link closing the enumeration?",
         "opts": [
             "Choices (saṅkhārā)",
             "Ignorance (avijjā)",
             "Rebirth (jāti)",
             "Feeling (vedanā)"],
         "correct": 0,
         "expl": "The consistent closing link across this chapter's related discourses."},
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
        ("A third pass, named honestly", [
            "not new content, but a familiar test again &mdash;",
            "distinguished by one intensified word",
        ]),
        ("Complete understanding, not just understanding", [
            "parijānāti, not pajānāti &mdash;",
            "the whole difference from SN 12.13",
        ]),
        ("The same verdict, unmoved", [
            "true or not, regardless of title &mdash;",
            "no softer standard offered here",
        ]),
        ("A deliberate echo near the chapter's end", [
            "returning to Āhāravagga's own theme &mdash;",
            "not coincidence, but reprise",
        ]),
    ],
    further=[
        '<a href="%s/sn12.29/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.13.html">SN 12.13 &middot; Ascetics and Brahmins</a> '
        "&mdash; the earlier discourse this one reprises with a "
        "single intensified verb.",
        '<a href="sn-12.28.html">SN 12.28 &middot; A Mendicant</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.30.html">SN 12.30 &middot; Ascetics and Brahmins (2nd)</a> '
        "&mdash; the next and final discourse in this chapter, "
        "closing Dasabalavagga.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.30 — Dutiyasamaṇabrāhmaṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 30, "Dutiyasamaṇabrāhmaṇa", "Ascetics and Brahmins (2nd)",
    meta_title="SN 12.30 — Ascetics and Brahmins (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasamaṇabrāhmaṇasutta — closing Dasabalavagga, the "
        "familiar test shifts from a verdict on title to a statement "
        "of what's actually possible: transcending each link, or "
        "not. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The familiar fourfold test, now framed around "
                 "possibility and impossibility rather than title"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "closes Dasabalavagga with a meaningful shift "
                       "in framing"),
    ],
    why=(
        "Closing Dasabalavagga, this discourse takes the same "
        "fourfold test already given three times in this chapter and "
        "reframes its conclusion. Rather than asking whether someone "
        "counts as a true ascetic or brahmin, it asks something more "
        "concrete: is it even possible for them to abide having "
        "transcended each link? For those lacking understanding, the "
        "answer is a flat impossibility &mdash; they simply cannot "
        "get beyond old age and death, or any other link, without "
        "understanding it fully. For those who understand, "
        "transcendence becomes genuinely possible. A shift from "
        "conferring or withholding a title to stating a plain fact "
        "about what can and cannot actually happen."),
    guide=[
        ("A familiar test, reframed around outcome rather than title", [
            "Where SN 12.13, SN 12.14, and SN 12.29 all conclude by "
            "granting or withholding the title of true ascetic or "
            "brahmin, this discourse instead states directly whether "
            "transcending each link is even possible."]),
        ("Impossibility stated as a plain fact, not a judgment", [
            "The language here isn't evaluative in the way a title "
            "verdict is; it states as a simple fact that it's "
            "impossible for someone lacking understanding to abide "
            "having transcended old age and death, or any other link."]),
        ("Possibility given equally direct, factual treatment", [
            "The positive case receives the same treatment in "
            "reverse: for those who understand each link fully, "
            "transcending it is stated as genuinely possible, with "
            "the same flat, factual phrasing."]),
        ("A closing chapter, its full shape now visible", [
            "This discourse closes Dasabalavagga, and the source's "
            "own closing summary verse lists all ten discourse titles "
            "in sequence &mdash; the two Ten Powers discourses, Vital "
            "Conditions, the contact-reduction trio, Dependency, A "
            "Mendicant, and the two Ascetics-and-Brahmins pairs "
            "closing the chapter."]),
        ("A fitting final note for a chapter grounding authority in understanding", [
            "Dasabalavagga opened by grounding the Buddha's own "
            "authority in mastery of this same material; closing on a "
            "statement of what genuine understanding actually makes "
            "possible brings the chapter's own concern with "
            "grounded, demonstrable knowledge full circle."]),
    ],
    terms=[
        ("te vata jarāmaraṇaṁ samatikkamma ṭhassantīti netaṁ ṭhānaṁ vijjati",
         "&ldquo;it's impossible that they will abide having "
         "transcended old age and death&rdquo; &mdash; the shift from "
         "a title verdict to a statement of plain impossibility."),
        ("te vata jarāmaraṇaṁ samatikkamma ṭhassantīti ṭhānametaṁ vijjati",
         "&ldquo;it's possible that they will abide having "
         "transcended old age and death&rdquo; &mdash; the positive "
         "counterpart, equally direct and factual."),
        ("saṅkhāre samatikkamma ṭhassanti",
         "&ldquo;abide having transcended choices&rdquo; &mdash; the "
         "same possibility-or-impossibility framing applied to the "
         "chain's final link."),
        ("dasabalavaggo tatiyo",
         "&ldquo;Dasabalavagga, the third [chapter]&rdquo; &mdash; "
         "the untranslated closing marker naming the chapter this "
         "discourse completes."),
        ("dve dasabalā upanisā ca&hellip; dve ca samaṇabrāhmaṇāti",
         "&ldquo;two Ten Powers discourses, and Vital "
         "Conditions&hellip; and two Ascetics-and-Brahmins&rdquo; "
         "&mdash; the closing summary verse naming this chapter's ten "
         "discourses in sequence."),
    ],
    text_intro=(
        "The discourse in full, closing Dasabalavagga. The chapter's "
        "closing summary verse, listing all ten discourse titles, is "
        "a structural index and is not reproduced as running prose "
        "here. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.30:1.3-1.13"),
        ("p", "&sect;2", "sn12.30:2.1-2.12"),
    ],
    quiz=[
        {"q": "How does this discourse's framing differ from SN 12.13, SN 12.14, and SN 12.29?",
         "opts": [
             "It states possibility or impossibility of transcending each link, rather than granting a title",
             "It abandons the fourfold test entirely",
             "It introduces an entirely new set of twelve links",
             "It reverses the verdict given in the earlier discourses"],
         "correct": 0,
         "expl": "A shift from conferring or withholding a title to stating a plain fact."},
        {"q": "What does the discourse say about someone lacking understanding of old age and death?",
         "opts": [
             "It's impossible that they will abide having transcended it",
             "It's still possible, though difficult",
             "The discourse offers no statement either way",
             "They will transcend it automatically over time"],
         "correct": 0,
         "expl": "A flat statement of impossibility, not a graded judgment."},
        {"q": "What does the discourse say about someone who does understand each link fully?",
         "opts": [
             "It's possible that they will abide having transcended it",
             "Transcendence remains impossible regardless of understanding",
             "The discourse gives no positive case",
             "Understanding alone guarantees transcendence with no further practice needed"],
         "correct": 0,
         "expl": "Equally direct, factual treatment for the positive case."},
        {"q": "What does this discourse close, structurally, within Nidānavagga?",
         "opts": [
             "Dasabalavagga, this book's third chapter of ten discourses",
             "The entire Nidānavagga book",
             "Only a minor sub-section with no larger significance",
             "Nothing; more discourses in this chapter follow"],
         "correct": 0,
         "expl": "Confirmed by the chapter's closing summary verse listing all ten titles."},
        {"q": "How does this discourse's closing theme connect back to Dasabalavagga's opening?",
         "opts": [
             "Both concern grounding authority or transcendence in genuine, demonstrable understanding",
             "There is no thematic connection between the opening and closing discourses",
             "The opening and closing discourses directly contradict each other",
             "The chapter's opening and closing address entirely unrelated topics"],
         "correct": 0,
         "expl": "Bringing the chapter's concern with grounded knowledge full circle."},
        {"q": "What is the language used to describe impossibility, according to this reading guide?",
         "opts": [
             "Plain and factual, not evaluative in the way a title verdict is",
             "Highly poetic and metaphorical",
             "Deliberately vague and ambiguous",
             "Framed as a personal opinion rather than a stated fact"],
         "correct": 0,
         "expl": "A statement of what can and cannot happen, not a judgment of worth."},
        {"q": "What is the first link addressed in this discourse's fourfold test?",
         "opts": [
             "Old age and death",
             "Ignorance",
             "Craving",
             "Consciousness"],
         "correct": 0,
         "expl": "The consistent starting point across this chapter's related discourses."},
        {"q": "What is the final link closing the enumeration?",
         "opts": [
             "Choices (saṅkhārā)",
             "Ignorance (avijjā)",
             "Rebirth (jāti)",
             "Feeling (vedanā)"],
         "correct": 0,
         "expl": "Matching the standard closing point already established in this chapter."},
        {"q": "What does the chapter's closing summary verse list?",
         "opts": [
             "All ten discourse titles of Dasabalavagga in sequence",
             "A list of every past Buddha mentioned in this book",
             "A count of total verses in the chapter",
             "Nothing further; only this discourse's own title is given"],
         "correct": 0,
         "expl": "A structural index summarizing the entire chapter by title."},
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
        ("A title verdict, replaced by a plain fact", [
            "not \"true\" or not &mdash;",
            "possible to transcend, or not",
        ]),
        ("Impossibility, stated flatly", [
            "not a harsh judgment &mdash;",
            "simply what cannot happen without understanding",
        ]),
        ("A chapter's concern, come full circle", [
            "authority grounded in understanding, at the opening &mdash;",
            "transcendence grounded in it, at the close",
        ]),
        ("Ten titles, named in one closing verse", [
            "the whole chapter's shape, summarized &mdash;",
            "not reproduced verbatim here",
        ]),
    ],
    further=[
        '<a href="%s/sn12.30/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.29.html">SN 12.29 &middot; Ascetics and Brahmins</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.31.html">SN 12.31 &middot; What Has Come to Be</a> '
        "&mdash; opening Kaḷārakhattiyavagga, this book's fourth "
        "chapter.",
    ],
)
