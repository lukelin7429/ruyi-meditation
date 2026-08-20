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
TAIL = ("sn-12.15.html", "SN 12.15 &middot; Kaccānagotta")
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
