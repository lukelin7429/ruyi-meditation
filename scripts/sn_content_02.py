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
TAIL = ("sn-15.3.html", "SN 15.3 &middot; Tears")
# SN 12.15 (Kaccānagotta) is a pre-existing page sitting between this
# module's SN 12.14 and SN 12.16 (confirmed by Āhāravagga's own closing
# uddāna, which lists it fifth of ten); it is not itself in PAGES, so
# sn_build.py's auto-chain naturally skips over it when linking 12.14 to
# 12.16. As with sn_content_01.py's sn-4.1/sn-5.10/sn-6.2 fragility, this
# is a STABLE, RECURRING regression, confirmed to reset on every full
# build of this module (not just the first time 12.16 was added) --
# 12.14's next and 12.16's prev must be manually re-patched to route
# through 12.15 after every single sn_build.py run.
#
# Mahāvagga (SN 12.61-70) has the SAME fragility TWICE over, since two of
# its pre-existing pages sit mid-sequence rather than at a vagga boundary:
# SN 12.61 (Unlearned) sits between this module's SN 12.60 (Dukkhavagga's
# close) and SN 12.62, and SN 12.65 (The City) sits between SN 12.64 and
# SN 12.66. Neither 12.61 nor 12.65 is itself in PAGES, so every full
# build routes 12.60 straight to 12.62 (skipping 12.61) and 12.64 straight
# to 12.66 (skipping 12.65) -- both junctions need the identical manual
# re-patch as 12.14/12.16 after every single sn_build.py run: fix 12.60's
# next and 12.62's prev to route through 12.61, and fix 12.64's next and
# 12.66's prev to route through 12.65. TAIL is now sn-15.3.html rather
# than sn-12.61.html, since 12.61 no longer sits at this module's leading
# edge once Mahāvagga's own new pages are appended.
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


# --------------------------------------------------------------------------- #
# SN 12.31 — Bhūtasutta
# --------------------------------------------------------------------------- #
page(
    12, 31, "Bhūta", "What Has Come to Be",
    meta_title="SN 12.31 — What Has Come to Be | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bhūtasutta — opening Kaḷārakhattiyavagga, Sāriputta's "
        "three silences give way to a precise unpacking of an ancient "
        "verse from the Pārāyanavagga, distinguishing the trainee "
        "from the fully freed. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and Venerable Sāriputta"),
        ("Form", "A terse verse quoted, met with silence three "
                 "times, then unpacked in careful detail once the "
                 "question is reframed"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "opens a new chapter by reaching back to an "
                       "older text"),
    ],
    why=(
        "The Buddha quotes a terse verse from the Pārāyanavagga, the "
        "closing chapter of the Sutta Nipāta, and asks Sāriputta to "
        "explain its detailed meaning. Three times Sāriputta stays "
        "silent. Only when the Buddha reframes the question directly "
        "&mdash; do you see that this has come to be? &mdash; does "
        "Sāriputta answer, unpacking the verse's cryptic reference to "
        "trainees and those who have appraised the teaching into a "
        "precise threefold analysis: seeing what has come to be, "
        "seeing what it depends on for its origin, and seeing that "
        "it will cease when that dependency ceases. This distinction, "
        "applied at two depths, separates the trainee still "
        "practicing from the one already fully freed."),
    guide=[
        ("An old verse, given new commentary", [
            "Rather than teaching something entirely new, this "
            "discourse takes a genuinely older text &mdash; a verse "
            "from the Pārāyanavagga &mdash; and has Sāriputta supply "
            "the detailed explanation its terse original language "
            "leaves compressed."]),
        ("Three silences, left honestly unexplained", [
            "The text doesn't say why Sāriputta stays silent three "
            "times before answering; this reading guide doesn't "
            "invent a motive for it, whether caution, humility, or "
            "genuine uncertainty, and leaves the silence as the "
            "source presents it."]),
        ("A question reframed, not simply repeated", [
            "Rather than asking a fourth time in the same words, the "
            "Buddha shifts to a more direct, concrete question "
            "&mdash; do you see that this has come to be? &mdash; and "
            "this reframing is what finally draws out Sāriputta's "
            "answer."]),
        ("A threefold pattern applied at two distinct depths", [
            "The same three-part seeing &mdash; what has come to be, "
            "its fuel, and its cessation &mdash; is applied first to "
            "describe a trainee still practicing toward "
            "disillusionment, and then again, in slightly stronger "
            "language, to describe one who has already appraised the "
            "teaching and is freed."]),
        ("Confirmation given word for word", [
            "The Buddha doesn't merely approve of Sāriputta's answer "
            "in passing; he repeats it in full, affirming that this "
            "is exactly how the verse's brief statement should be "
            "understood in detail."]),
    ],
    terms=[
        ("saṅkhātadhammāse&hellip; sekkhā puthū idha",
         "&ldquo;those who have appraised the teaching&hellip; many "
         "kinds of trainees&rdquo; &mdash; the Pārāyanavagga verse's "
         "own compressed vocabulary, quoted before being unpacked."),
        ("tuṇhī ahosi",
         "&ldquo;kept silent&rdquo; &mdash; Sāriputta's repeated "
         "response, given three times before he finally answers."),
        ("bhūtamidanti&hellip; yathābhūtaṁ sammappaññāya passati",
         "&ldquo;do you see that this has come to be?&hellip; truly "
         "sees with right wisdom&rdquo; &mdash; the Buddha's "
         "reframed, more direct question that finally draws out an "
         "answer."),
        ("tadāhārasambhavaṁ&hellip; tadāhāranirodhā",
         "&ldquo;originated with that as fuel&hellip; when that fuel "
         "ceases&rdquo; &mdash; the threefold analytical structure "
         "applied to what has come to be."),
        ("sekho&hellip; saṅkhātadhammo",
         "&ldquo;trainee&hellip; one who has appraised the "
         "teaching&rdquo; &mdash; the two levels distinguished, the "
         "second marked by complete freedom through non-grasping."),
    ],
    text_intro=(
        "The discourse in full, opening Kaḷārakhattiyavagga. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.31:1.1-1.3"),
        ("p", "&sect;2", "sn12.31:2.1-3.1"),
        ("p", "&sect;3", "sn12.31:3.2-6.2"),
        ("p", "&sect;4", "sn12.31:7.1-7.8"),
        ("p", "&sect;5", "sn12.31:8.1-8.9"),
        ("p", "&sect;6", "sn12.31:9.1-10.1"),
        ("p", "&sect;7", "sn12.31:11.1-11.7"),
        ("p", "&sect;8", "sn12.31:12.1-14.1"),
    ],
    quiz=[
        {"q": "Where does the verse the Buddha quotes to Sāriputta originally come from?",
         "opts": [
             "The Pārāyanavagga, the closing chapter of the Sutta Nipāta",
             "A verse composed by Sāriputta himself for this occasion",
             "An earlier discourse in this same saṃyutta",
             "The verse has no identified source"],
         "correct": 0,
         "expl": "Reaching back to a genuinely older text for new commentary."},
        {"q": "How many times does Sāriputta stay silent before answering?",
         "opts": [
             "Three times",
             "Once",
             "He never stays silent; he answers immediately",
             "Five times"],
         "correct": 0,
         "expl": "A notable narrative beat this reading guide leaves unexplained."},
        {"q": "Does this reading guide invent a reason for Sāriputta's silence?",
         "opts": [
             "No — it leaves the silence honestly unexplained, as the source presents it",
             "Yes, it claims Sāriputta was asleep",
             "Yes, it claims Sāriputta was testing the Buddha",
             "Yes, it claims the silence was a scribal error"],
         "correct": 0,
         "expl": "An honest refusal to fill a gap the text itself leaves open."},
        {"q": "What question finally draws out Sāriputta's answer?",
         "opts": [
             "\"Do you see that this has come to be?\" — a more direct reframing",
             "The exact same question repeated a fourth time",
             "A question about an entirely different topic",
             "The Buddha never asks a further question; Sāriputta volunteers the answer"],
         "correct": 0,
         "expl": "A shift in approach, not mere repetition."},
        {"q": "What threefold pattern does Sāriputta's answer apply?",
         "opts": [
             "Seeing what has come to be, its fuel, and its cessation",
             "Seeing the past, present, and future separately",
             "Seeing the four noble truths as a single unit",
             "No pattern is applied; the answer is unstructured"],
         "correct": 0,
         "expl": "The same three-part seeing applied at two depths of understanding."},
        {"q": "What distinguishes a trainee from one who has appraised the teaching, in this discourse?",
         "opts": [
             "The trainee still practices toward freedom; the one who has appraised it is already freed",
             "The trainee is younger in age",
             "The trainee has taken fewer vows",
             "There is no meaningful distinction between the two"],
         "correct": 0,
         "expl": "Two depths of the same threefold seeing, one still in progress, one complete."},
        {"q": "How does the Buddha respond to Sāriputta's explanation?",
         "opts": [
             "He repeats it in full, confirming it word for word",
             "He rejects it as incomplete",
             "He offers a completely different explanation instead",
             "He declines to comment on it"],
         "correct": 0,
         "expl": "Full, explicit confirmation, not passing approval."},
        {"q": "What is \"fuel\" (āhāra) used to describe in this discourse?",
         "opts": [
             "What something has come to be dependent on for its origin",
             "Literal food eaten by monks",
             "A type of ritual offering",
             "The discourse doesn't use this term at all"],
         "correct": 0,
         "expl": "A term already introduced in SN 12.11, now applied more generally."},
        {"q": "Who are the only two speakers in this discourse?",
         "opts": [
             "The Buddha and Sāriputta",
             "The Buddha and Ānanda",
             "Sāriputta and Kaḷāra the Aristocrat",
             "The Buddha and a group of unnamed monks"],
         "correct": 0,
         "expl": "A direct exchange between teacher and disciple."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "Near Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The setting opening this fourth chapter of Nidānavagga."},
    ],
    marginalia=[
        ("An old verse, freshly unpacked", [
            "quoted from the Pārāyanavagga &mdash;",
            "its compression given room to breathe",
        ]),
        ("Three silences, left as they are", [
            "no invented reason supplied &mdash;",
            "the gap honestly left open",
        ]),
        ("A question reshaped, not repeated", [
            "\"do you see this has come to be?\" &mdash;",
            "directness where repetition had failed",
        ]),
        ("Two depths, one threefold pattern", [
            "trainee, and one already freed &mdash;",
            "the same seeing, carried further",
        ]),
    ],
    further=[
        '<a href="%s/sn12.31/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.30.html">SN 12.30 &middot; Ascetics and Brahmins (2nd)</a> '
        "&mdash; the discourse closing Dasabalavagga, immediately "
        "before this one.",
        '<a href="sn-12.32.html">SN 12.32 &middot; With Kaḷāra the Aristocrat</a> '
        "&mdash; the next discourse, where Sāriputta's own attainment "
        "is tested and confirmed in vivid, dramatic detail.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.32 — Kaḷārasutta
# --------------------------------------------------------------------------- #
page(
    12, 32, "Kaḷāra", "With Kaḷāra the Aristocrat",
    meta_title="SN 12.32 — With Kaḷāra the Aristocrat | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kaḷārasutta — news of one monk's quiet departure sets up "
        "another's understated declaration, tested by the Buddha "
        "question by question until Sāriputta's own confident "
        "seven-day boast. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "Kaḷāra the Aristocrat, Sāriputta, the Buddha, "
                     "and a group of mendicants"),
        ("Form", "A narrated episode in three movements &mdash; a "
                 "quiet exchange, a rigorous interrogation, and a "
                 "closing boast confirmed as genuine"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "one of this saṃyutta's most vivid, "
                       "characterful discourses"),
    ],
    why=(
        "This discourse opens with news that could easily read as "
        "discouraging: Phagguna, the monk who once questioned the "
        "Buddha about who consumes consciousness as fuel back in SN "
        "12.12, has disrobed and returned to lay life. Sāriputta's "
        "response is cool and understated, and when pressed about his "
        "own progress, he answers just as indirectly &mdash; no "
        "formal declaration, just two spare phrases: no uncertainty, "
        "no doubt. What follows is the Buddha testing that "
        "understatement rigorously, question by question, until "
        "Sāriputta closes with a genuinely confident claim: he could "
        "answer the same questions, in ever-different words, for "
        "seven full days and nights."),
    guide=[
        ("A departure setting up a very different outcome", [
            "News of Phagguna's disrobing isn't simply background; it "
            "frames everything that follows by contrast, one monk's "
            "quiet departure from the training set directly against "
            "another's quiet but unmistakable attainment within it."]),
        ("A declaration made without declaring", [
            "When Kaḷāra asks Sāriputta directly whether he has found "
            "solace in the teaching, Sāriputta doesn't use anything "
            "resembling the standard formula for announcing "
            "enlightenment; his answer is just two spare phrases, no "
            "uncertainty and no doubt."]),
        ("A report that outpaces what was actually said", [
            "Kaḷāra rushes to tell the Buddha that Sāriputta has "
            "formally declared enlightenment in the standard words, "
            "when Sāriputta never actually used that formula at "
            "all &mdash; a small but meaningful gap between what was "
            "said and how it was reported."]),
        ("An interrogation that tests substance, not phrasing", [
            "Rather than correcting Kaḷāra's misreport, the Buddha "
            "questions Sāriputta directly and rigorously, tracing "
            "back through the chain link by link and asking exactly "
            "how he knows what he claims to know &mdash; testing "
            "whether the understanding is genuine, regardless of what "
            "words were or weren't used to express it."]),
        ("A boast made in private, then confirmed in public", [
            "Sāriputta's remarkable claim &mdash; that he could "
            "answer the same question in different words for seven "
            "days and nights straight &mdash; is made privately to "
            "the other monks after the Buddha has already left, and "
            "only becomes public when Kaḷāra reports it back; the "
            "Buddha's confirmation that this is no exaggeration closes "
            "the discourse."]),
    ],
    terms=[
        ("sikkhaṁ paccakkhāya hīnāyāvatto",
         "&ldquo;resigned the training and returned to a lesser "
         "life&rdquo; &mdash; the news of Phagguna's disrobing, "
         "opening the discourse by contrast."),
        ("na khvāhaṁ kaṅkhāmi&hellip; na vicikicchāmi",
         "&ldquo;I have no uncertainty&hellip; I have no doubt&rdquo; "
         "&mdash; Sāriputta's understated, indirect response when "
         "asked about his own attainment."),
        ("na kho, bhante, etehi padehi etehi byañjanehi attho vutto",
         "&ldquo;I did not state the matter in these words and "
         "phrases&rdquo; &mdash; Sāriputta's insistence that Kaḷāra's "
         "report used language he himself never actually spoke."),
        ("yaṁ kiñci vedayitaṁ taṁ dukkhasmiṁ",
         "&ldquo;suffering includes whatever is felt&rdquo; &mdash; "
         "the Buddha's compact restatement of Sāriputta's reasoning "
         "on the impermanence of feeling."),
        ("divasañcepi maṁ bhagavā&hellip; satta rattindivānipāhaṁ byākareyyaṁ",
         "&ldquo;even for seven days and nights I could answer in "
         "different words and ways&rdquo; &mdash; Sāriputta's "
         "confident private boast, confirmed by the Buddha as his "
         "genuine &ldquo;lion's roar.&rdquo;"),
    ],
    text_intro=(
        "The discourse in full, one of this saṃyutta's most vivid "
        "and characterful. Several passages repeating earlier content "
        "are elided in the source exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.32:1.2-1.5"),
        ("p", "&sect;2", "sn12.32:2.1-4.1"),
        ("p", "&sect;3", "sn12.32:5.1-5.3"),
        ("p", "&sect;4", "sn12.32:6.1-6.12"),
        ("p", "&sect;5", "sn12.32:7.1-8.8"),
        ("p", "&sect;6", "sn12.32:9.1-11.10"),
        ("p", "&sect;7", "sn12.32:12.1-13.3"),
        ("p", "&sect;8", "sn12.32:14.1-15.5"),
        ("p", "&sect;9", "sn12.32:16.1-16.17"),
        ("p", "&sect;10", "sn12.32:17.1-17.13"),
        ("p", "&sect;11", "sn12.32:18.1-18.9"),
    ],
    quiz=[
        {"q": "What news opens this discourse?",
         "opts": [
             "That the monk Phagguna has disrobed and returned to lay life",
             "That a great battle has ended",
             "That the Buddha is gravely ill",
             "That a new monastery has been built"],
         "correct": 0,
         "expl": "Setting up a deliberate contrast with what follows."},
        {"q": "How does Sāriputta answer when Kaḷāra asks about his own progress?",
         "opts": [
             "Indirectly — just two spare phrases, no uncertainty and no doubt",
             "With the full, formal declaration of enlightenment",
             "By refusing to answer at all",
             "By claiming he has made no progress whatsoever"],
         "correct": 0,
         "expl": "An understated declaration, not the standard formula."},
        {"q": "What does Kaḷāra report to the Buddha about Sāriputta?",
         "opts": [
             "That Sāriputta formally declared enlightenment in the standard words, though he hadn't",
             "That Sāriputta had also disrobed",
             "That Sāriputta refused to speak with him",
             "Nothing; Kaḷāra never speaks to the Buddha in this discourse"],
         "correct": 0,
         "expl": "A gap between what was actually said and how it was reported."},
        {"q": "How does Sāriputta respond when the Buddha asks him to confirm the declaration?",
         "opts": [
             "He says he didn't state the matter in those exact words and phrases",
             "He confirms he used exactly those words",
             "He denies any attainment at all",
             "He refuses to respond to the Buddha"],
         "correct": 0,
         "expl": "Insisting on the gap between the report and his own actual words."},
        {"q": "How does the Buddha respond to this insistence on precise wording?",
         "opts": [
             "He says however a gentleman declares enlightenment, it should be regarded as such",
             "He agrees Sāriputta has not actually attained anything",
             "He dismisses the whole matter as unimportant",
             "He punishes Sāriputta for imprecise speech"],
         "correct": 0,
         "expl": "Substance over exact phrasing, while still proceeding to test the substance itself."},
        {"q": "What method does the Buddha use to test Sāriputta's understanding?",
         "opts": [
             "A series of hypothetical questions tracing back through the chain link by link",
             "A written examination",
             "A public debate with other monks",
             "No testing occurs; the Buddha simply accepts the claim"],
         "correct": 0,
         "expl": "Rigorous questioning of substance, not just acceptance of a claim."},
        {"q": "What compact restatement does the Buddha offer for Sāriputta's reasoning about feeling?",
         "opts": [
             "\"Suffering includes whatever is felt\"",
             "\"Feeling is entirely separate from suffering\"",
             "\"Only painful feeling is suffering\"",
             "No restatement is offered"],
         "correct": 0,
         "expl": "A briefer version of the same point about feeling's impermanence."},
        {"q": "What confident claim does Sāriputta make privately to the other monks?",
         "opts": [
             "That he could answer the same question in different words for seven days and nights",
             "That he intends to disrobe like Phagguna",
             "That he doubts his own attainment after all",
             "That he will never speak of this matter again"],
         "correct": 0,
         "expl": "A remarkable claim of total command over the teaching's underlying principle."},
        {"q": "How does the Buddha respond when Kaḷāra reports Sāriputta's boast?",
         "opts": [
             "He confirms it as true — Sāriputta has clearly penetrated the principle of the teaching",
             "He rebukes Sāriputta for arrogance",
             "He declines to comment",
             "He says the claim is exaggerated"],
         "correct": 0,
         "expl": "Full confirmation, calling it a genuine \"lion's roar\" rather than a boast."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting for this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A departure, framing a very different story", [
            "one monk leaves, quietly &mdash;",
            "another's attainment set against it",
        ]),
        ("A declaration without the formula", [
            "\"no uncertainty... no doubt\" &mdash;",
            "understated, not the standard words",
        ]),
        ("A report ahead of what was said", [
            "Kaḷāra's account outpacing Sāriputta's own &mdash;",
            "substance tested regardless",
        ]),
        ("A boast made private, confirmed public", [
            "seven days and nights, in different words &mdash;",
            "the Buddha calling it genuine",
        ]),
    ],
    further=[
        '<a href="%s/sn12.32/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.31.html">SN 12.31 &middot; What Has Come to Be</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.12.html">SN 12.12 &middot; Phagguna of the Top-Knot</a> '
        "&mdash; the earlier discourse featuring the monk whose "
        "disrobing opens this one.",
        '<a href="sn-12.33.html">SN 12.33 &middot; Grounds for Knowledge</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.33 — Ñāṇavatthusutta
# --------------------------------------------------------------------------- #
page(
    12, 33, "Ñāṇavatthu", "Grounds for Knowledge",
    meta_title="SN 12.33 — Grounds for Knowledge | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ñāṇavatthusutta — forty-four specific grounds for "
        "knowledge, and a distinction between direct knowledge of "
        "the teaching and inferential knowledge extending it across "
        "all time. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A numbered enumeration of knowledge-grounds, "
                 "followed by a distinction between two kinds of "
                 "knowing"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "introduces a genuinely new epistemological "
                       "distinction into this book's terminology"),
    ],
    why=(
        "This discourse names a precise figure &mdash; forty-four "
        "grounds for knowledge, eleven links each examined fourfold "
        "&mdash; but its real contribution lies in a distinction "
        "introduced partway through: knowledge of the teaching "
        "(direct, present understanding of a given link) is separated "
        "from inferential knowledge (the further step of recognizing "
        "that whoever understood this in the past understood it "
        "exactly the same way, and whoever will understand it in the "
        "future will understand it exactly the same way too). "
        "Genuine mastery, the discourse insists, requires both kinds "
        "purified together, not direct insight alone."),
    guide=[
        ("A precise count, not a loose estimate", [
            "The discourse names forty-four specifically, not "
            "\"many\" or \"numerous\"; eleven links, each examined "
            "through the same fourfold lens of thing, origin, "
            "cessation, and path, giving the number its exact "
            "structural basis."]),
        ("Two kinds of knowledge distinguished, not treated as one", [
            "Rather than describing understanding as a single "
            "achievement, the discourse separates knowledge of the "
            "teaching &mdash; direct comprehension of a link here and "
            "now &mdash; from inferential knowledge, a further step "
            "extending that comprehension across time."]),
        ("Inference reaching both backward and forward", [
            "The inferential knowledge described isn't limited to "
            "confirming the past; it extends with equal confidence "
            "into the future, claiming that anyone who will come to "
            "understand this link will understand it in exactly the "
            "same way, not a different one."]),
        ("Purification required of both kinds together", [
            "The discourse doesn't treat either kind of knowledge as "
            "sufficient alone; genuine accomplishment requires both "
            "knowledge of the teaching and inferential knowledge "
            "purified and cleansed together."]),
        ("The same closing titles, now earned through two knowledges", [
            "The nine honorific titles already familiar from SN 12.27 "
            "reappear here, but this time explicitly earned through "
            "the combination of direct and inferential knowledge, "
            "rather than through direct understanding alone."]),
    ],
    terms=[
        ("catucattārīsaṁ ñāṇavatthūni",
         "&ldquo;forty-four grounds for knowledge&rdquo; &mdash; the "
         "precise total, eleven links examined fourfold."),
        ("dhamme ñāṇaṁ",
         "&ldquo;knowledge of the teaching&rdquo; &mdash; direct, "
         "present-tense understanding of a given link's fourfold "
         "nature."),
        ("anvaye ñāṇaṁ",
         "&ldquo;inferential knowledge&rdquo; &mdash; extending that "
         "direct understanding by inference to all who knew, or will "
         "know, it identically across time."),
        ("sabbete evameva abbhaññaṁsu, seyyathāpāhaṁ etarahi",
         "&ldquo;all of them directly knew these things in exactly "
         "the same way that I do now&rdquo; &mdash; the specific "
         "inferential claim extending confidently into the past."),
        ("dhamme ñāṇañca anvaye ñāṇañca&hellip; parisuddhāni honti pariyodātāni",
         "&ldquo;knowledge of the teaching and inferential "
         "knowledge&hellip; purified and cleansed&rdquo; &mdash; both "
         "kinds required together, not either alone."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.33:1.2-2.2"),
        ("p", "&sect;2", "sn12.33:3.1-4.4"),
        ("p", "&sect;3", "sn12.33:5.1-5.2"),
        ("p", "&sect;4", "sn12.33:6.1-7.2"),
        ("p", "&sect;5", "sn12.33:8.1-8.3"),
    ],
    quiz=[
        {"q": "How many grounds for knowledge does this discourse name?",
         "opts": [
             "Forty-four, from eleven links examined fourfold",
             "Twelve, one for each link",
             "A vague, unspecified number",
             "Four, one for each noble truth"],
         "correct": 0,
         "expl": "A precise count with a clear structural basis."},
        {"q": "What two kinds of knowledge does this discourse distinguish?",
         "opts": [
             "Knowledge of the teaching, and inferential knowledge",
             "Knowledge gained by study, and knowledge gained by meditation",
             "Knowledge of the past, and knowledge of the present, with no mention of the future",
             "No distinction is made; only one kind of knowledge is discussed"],
         "correct": 0,
         "expl": "Direct, present comprehension separated from a further inferential step."},
        {"q": "What does knowledge of the teaching (dhamme ñāṇa) refer to?",
         "opts": [
             "Direct, present-tense understanding of a link's fourfold nature",
             "Knowledge gained secondhand from a teacher's report",
             "Knowledge limited only to the future",
             "A synonym for inferential knowledge, with no real difference"],
         "correct": 0,
         "expl": "Understanding grounded in one's own direct comprehension, here and now."},
        {"q": "What does inferential knowledge (anvaye ñāṇa) extend to?",
         "opts": [
             "Both the past and the future, claiming the same understanding held and will hold for others",
             "Only the past, with no claim about the future",
             "Only the future, with no claim about the past",
             "Only the present moment, with no extension in time"],
         "correct": 0,
         "expl": "Reaching backward and forward with equal confidence."},
        {"q": "Does the discourse treat either kind of knowledge as sufficient alone?",
         "opts": [
             "No — both must be purified and cleansed together",
             "Yes, knowledge of the teaching alone is sufficient",
             "Yes, inferential knowledge alone is sufficient",
             "The discourse doesn't address whether one alone suffices"],
         "correct": 0,
         "expl": "Genuine accomplishment requires both kinds combined."},
        {"q": "How is old age defined in this discourse's detailed treatment?",
         "opts": [
             "Broken teeth, grey hair, wrinkled skin, and failing faculties",
             "The discourse leaves old age undefined",
             "Only in relation to animals, not humans",
             "As identical in meaning to death"],
         "correct": 0,
         "expl": "The same vivid definition already familiar from SN 12.27."},
        {"q": "What is named as the practice leading to each link's cessation?",
         "opts": [
             "The noble eightfold path",
             "A vow of silence",
             "No practice is named",
             "A different practice unique to this discourse"],
         "correct": 0,
         "expl": "Matching SN 12.27's explicit naming of the path."},
        {"q": "How many honorific titles close this discourse, matching SN 12.27?",
         "opts": [
             "Nine",
             "Only one",
             "Three",
             "Forty-four, matching the number of knowledge-grounds"],
         "correct": 0,
         "expl": "The identical string of titles, now earned through two combined knowledges."},
        {"q": "What is the last of the eleven links this discourse's fourfold treatment is applied to?",
         "opts": [
             "Choices (saṅkhārā)",
             "Ignorance (avijjā)",
             "Rebirth (jāti)",
             "Feeling (vedanā)"],
         "correct": 0,
         "expl": "Closing the enumeration exactly where SN 12.27 and SN 12.28 close it."},
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
        ("A precise number, not a loose estimate", [
            "forty-four, structurally derived &mdash;",
            "eleven links, four aspects each",
        ]),
        ("Two knowledges, not one", [
            "direct understanding, and inference beyond it &mdash;",
            "a genuinely new distinction",
        ]),
        ("Inference reaching both directions", [
            "confident about the past and the future alike &mdash;",
            "not limited to confirming history",
        ]),
        ("Both required, neither sufficient alone", [
            "purified together, not separately &mdash;",
            "the standard this discourse actually sets",
        ]),
    ],
    further=[
        '<a href="%s/sn12.33/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.32.html">SN 12.32 &middot; With Kaḷāra the Aristocrat</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.34.html">SN 12.34 &middot; Grounds for Knowledge (2nd)</a> '
        "&mdash; the next discourse, further intensifying this same "
        "count to seventy-seven.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.34 — Dutiyañāṇavatthusutta
# --------------------------------------------------------------------------- #
page(
    12, 34, "Dutiyañāṇavatthu", "Grounds for Knowledge (2nd)",
    meta_title="SN 12.34 — Grounds for Knowledge (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyañāṇavatthusutta — seventy-seven grounds for "
        "knowledge, closing on the striking reflexive point that even "
        "knowledge of the stable principle is itself impermanent. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A further-intensified enumeration of "
                 "knowledge-grounds, closing on a reflexive claim "
                 "about knowledge itself"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "a dense, precisely structured discourse "
                       "closing on a genuinely subtle point"),
    ],
    why=(
        "This discourse takes SN 12.33's project of counting "
        "knowledge-grounds and multiplies it: seventy-seven this "
        "time, built from eleven conditioning relationships, each "
        "examined through knowledge of what conditions what, "
        "knowledge of its absence, and both extended across past and "
        "future, plus one further addition. That addition is the "
        "discourse's real point: even the knowledge of this stable, "
        "reliable natural principle is itself impermanent, liable to "
        "end, vanish, fade away, and cease &mdash; a reflexive "
        "caution against treating the principle of dependent "
        "origination as some kind of permanent, exempt truth standing "
        "outside the very impermanence it describes."),
    guide=[
        ("A number built from a precise, countable structure", [
            "Seventy-seven isn't an arbitrary intensification of "
            "forty-four; it's built from eleven relationships, each "
            "contributing seven distinct items of knowledge, giving "
            "the total figure exact structural grounding."]),
        ("Presence and absence paired at every step", [
            "Each relationship isn't examined only for what conditions "
            "what; it's paired with the mirror knowledge of what "
            "happens in that condition's absence &mdash; not just "
            "that rebirth conditions old age and death, but that "
            "without rebirth there is no old age and death."]),
        ("The same pairing repeated across all three times", [
            "This paired knowledge isn't confined to the present; the "
            "discourse extends it explicitly across the past and the "
            "future as well, tripling the basic pair into a "
            "sixfold structure before its final addition."]),
        ("A seventh item added to each set of six", [
            "Beyond the six items already covering presence, "
            "absence, and their extension across past and future, "
            "each relationship receives one further, reflexive "
            "addition, bringing the total for each relationship to "
            "seven."]),
        ("A caution against treating the principle as permanently exempt", [
            "That seventh addition is the discourse's real weight: "
            "even knowledge of this reliable, stable natural "
            "principle is itself impermanent and liable to cease, "
            "preventing the principle of dependent origination from "
            "being quietly exempted from the very impermanence it "
            "describes."]),
    ],
    terms=[
        ("sattasattari ñāṇavatthūni",
         "&ldquo;seventy-seven grounds for knowledge&rdquo; &mdash; "
         "the further-intensified count, eleven relationships each "
         "contributing seven items."),
        ("jātipaccayā jarāmaraṇanti ñāṇaṁ; asati jātiyā natthi jarāmaraṇanti ñāṇaṁ",
         "&ldquo;knowledge that rebirth is a requirement for old age "
         "and death&hellip; knowledge that without rebirth there is "
         "no old age and death&rdquo; &mdash; the paired presence "
         "and absence forming the basic unit."),
        ("atītampi addhānaṁ&hellip; anāgatampi addhānaṁ",
         "&ldquo;also regarding the past&hellip; also regarding the "
         "future&rdquo; &mdash; extending the same paired knowledge "
         "across all three times."),
        ("dhammaṭṭhitiñāṇaṁ",
         "&ldquo;knowledge of the stability of natural "
         "principles&rdquo; &mdash; the technical term for insight "
         "into the law's regularity, echoing SN 12.20."),
        ("tampi khayadhammaṁ vayadhammaṁ virāgadhammaṁ nirodhadhammanti ñāṇaṁ",
         "&ldquo;the knowledge that even this&hellip; is liable to "
         "end, vanish, fade away, and cease&rdquo; &mdash; the "
         "crucial reflexive point that even knowledge of the stable "
         "principle is itself impermanent."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.34:1.2-2.6"),
        ("p", "&sect;2", "sn12.34:3.10-3.14"),
    ],
    quiz=[
        {"q": "How many grounds for knowledge does this discourse name?",
         "opts": [
             "Seventy-seven, from eleven relationships each contributing seven",
             "Forty-four, identical to SN 12.33",
             "Twelve, one for each link",
             "An unspecified, open-ended number"],
         "correct": 0,
         "expl": "A further intensification of SN 12.33's count, with its own precise structure."},
        {"q": "What two things are paired for each conditioning relationship?",
         "opts": [
             "Knowledge of the condition's presence, and knowledge of its absence",
             "Knowledge of the past only, with no present knowledge",
             "Knowledge of feeling and knowledge of perception",
             "No pairing occurs; each relationship gets only one kind of knowledge"],
         "correct": 0,
         "expl": "Both what conditions what, and what happens without that condition."},
        {"q": "Across how many times is this paired knowledge extended?",
         "opts": [
             "Three — present, past, and future",
             "Only the present",
             "Only the past and present, with no future extension",
             "Five distinct time periods"],
         "correct": 0,
         "expl": "Tripling the basic pair before the discourse's final addition."},
        {"q": "What is the seventh item added to each relationship's set of six?",
         "opts": [
             "The knowledge that even this stable principle's own knowledge is impermanent",
             "A prayer for long life",
             "A description of the relevant deity",
             "No seventh item is added; each set contains only six"],
         "correct": 0,
         "expl": "The discourse's real, reflexive weight."},
        {"q": "What does this reflexive seventh item guard against?",
         "opts": [
             "Treating the principle of dependent origination as permanently exempt from impermanence",
             "Monks forgetting the twelve links entirely",
             "Excessive pride in monastic achievement",
             "Nothing specific; it's simply decorative"],
         "correct": 0,
         "expl": "Preventing the principle from being quietly exempted from what it describes."},
        {"q": "What technical term names insight into the law's regularity?",
         "opts": [
             "Dhammaṭṭhitiñāṇa, \"knowledge of the stability of natural principles\"",
             "Samādhi, \"immersion\"",
             "Vimutti, \"freedom\"",
             "No such technical term appears in this discourse"],
         "correct": 0,
         "expl": "A term echoing SN 12.20's earlier description of dependent origination as a discovered law."},
        {"q": "What is the first relationship examined in this discourse's structure?",
         "opts": [
             "Rebirth as a requirement for old age and death",
             "Ignorance as a requirement for choices",
             "Consciousness as a requirement for name and form",
             "Craving as a requirement for grasping"],
         "correct": 0,
         "expl": "The starting point before the pattern extends through all eleven relationships."},
        {"q": "What is the final relationship closing the enumeration?",
         "opts": [
             "Ignorance as a requirement for choices",
             "Rebirth as a requirement for old age and death",
             "Feeling as a requirement for craving",
             "Consciousness as a requirement for choices"],
         "correct": 0,
         "expl": "The chain's root condition, closing the backward sequence."},
        {"q": "How does this discourse relate to SN 12.33?",
         "opts": [
             "It intensifies the same project of counting knowledge-grounds to a higher, precisely structured total",
             "It contradicts SN 12.33's teaching entirely",
             "It shares no relationship with SN 12.33",
             "It reduces SN 12.33's count to a smaller number"],
         "correct": 0,
         "expl": "A further development of the same enumerative approach."},
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
        ("A number built from precise parts", [
            "seventy-seven, not arbitrary &mdash;",
            "eleven relationships, seven items each",
        ]),
        ("Presence and absence, always paired", [
            "not just what conditions what &mdash;",
            "but what happens without it",
        ]),
        ("Extended across all three times", [
            "present, past, future alike &mdash;",
            "tripling the basic pair",
        ]),
        ("Even this knowledge, impermanent", [
            "no exemption for the principle itself &mdash;",
            "the reflexive caution closing each set",
        ]),
    ],
    further=[
        '<a href="%s/sn12.34/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.33.html">SN 12.33 &middot; Grounds for Knowledge</a> '
        "&mdash; the discourse immediately before this one, whose "
        "count of forty-four this discourse intensifies to "
        "seventy-seven.",
        '<a href="sn-12.20.html">SN 12.20 &middot; Conditions</a> '
        "&mdash; the earlier discourse whose description of "
        "dependent origination as a discovered natural law this "
        "discourse's technical term echoes.",
        '<a href="sn-12.35.html">SN 12.35 &middot; Ignorance is a Condition</a> '
        "&mdash; the next discourse in this saṃyutta.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.35 — Avijjāpaccayasutta
# --------------------------------------------------------------------------- #
page(
    12, 35, "Avijjāpaccaya", "Ignorance is a Condition",
    meta_title="SN 12.35 — Ignorance is a Condition | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Avijjāpaccayasutta — a mendicant's question about old "
        "age and death is rejected as malformed four times over, "
        "each rejection unpacking the identity view baked into "
        "asking who a link in the chain belongs to. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and an unnamed mendicant"),
        ("Form", "A recurring four-beat pattern &mdash; a question "
                 "rejected as malformed, the identity view it "
                 "conceals exposed, and the middle way restated "
                 "&mdash; run four times, then mirrored in four "
                 "matching cessation paragraphs"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "repetitive in structure, but each repetition "
                       "makes a precise philosophical point"),
    ],
    why=(
        "A mendicant asks what old age and death are, and who they "
        "belong to. The Buddha refuses the question outright: asking "
        "who a link belongs to smuggles in the assumption that there "
        "is an owner standing behind it, and any such assumption "
        "collapses into one of two views &mdash; that the soul and "
        "the body are the same thing, or that they are two different "
        "things &mdash; both of which make the spiritual life "
        "impossible to live. Avoiding both, the Buddha restates the "
        "link in its proper conditional form: rebirth is a "
        "requirement for old age and death. The mendicant asks the "
        "same kind of question three more times, moving back through "
        "rebirth, continued existence, and choices, and receives the "
        "same rejection and the same restatement each time, before "
        "the discourse closes by showing that all four of these "
        "malformed questions are simply cut off, root and all, once "
        "ignorance itself has faded away."),
    guide=[
        ("A question refused, not merely answered", [
            "The Buddha doesn't correct the mendicant's premise while "
            "answering it; he declares the question itself not fit "
            "to be asked, because any answer to \"who does this "
            "belong to\" already assumes the thing it's trying to "
            "establish."]),
        ("Two extremes named as views about the body", [
            "The identity view is spelled out in two mirrored forms "
            "&mdash; the soul and the body are one and the same, or "
            "the soul is one thing and the body another &mdash; and "
            "both, without exception, are said to make it impossible "
            "to live the spiritual life."]),
        ("The same rejection, run four times", [
            "The mendicant asks about old age and death, then "
            "rebirth, then continued existence, then choices, and "
            "each time receives an identical structure of rejection, "
            "diagnosis, and restatement &mdash; a deliberate, "
            "unhurried repetition rather than a single illustration."]),
        ("A middle way that is a form of speech, not a compromise", [
            "\"Avoiding these two extremes, the Realized One teaches "
            "by the middle way\" doesn't describe splitting the "
            "difference between the two identity views; it describes "
            "replacing the whole framework of ownership with a "
            "purely conditional statement &mdash; this being a "
            "requirement for that."]),
        ("Four cessation paragraphs mirroring the four questions", [
            "Rather than simply asserting that ignorance's ending "
            "resolves all confusion, the discourse closes by walking "
            "back through the same four questions one at a time, "
            "confirming for each that its \"twists, ducks, and "
            "dodges\" are cut off at the root once ignorance fades "
            "away with nothing left over."]),
    ],
    terms=[
        ("no kallo pañho",
         "&ldquo;not a fit question&rdquo; &mdash; the Buddha's "
         "outright rejection, given identically before each of the "
         "four restatements."),
        ("taṁ jīvaṁ taṁ sarīraṁ&hellip; aññaṁ jīvaṁ aññaṁ sarīraṁ",
         "&ldquo;the soul and the body are one and the same&hellip; "
         "the soul is one thing, the body another&rdquo; &mdash; the "
         "two extremes of identity view exposed inside the rejected "
         "question."),
        ("ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the same closing "
         "formula used in SN 12.15's teaching on existence and "
         "non-existence."),
        ("visūkāyikāni visevitāni vipphanditāni",
         "&ldquo;twists, ducks, and dodges&rdquo; &mdash; the "
         "discourse's vivid term for the malformed questions "
         "themselves, given up once ignorance ceases."),
        ("ucchinnamūlāni tālāvatthukatāni anabhāvaṅkatāni "
         "āyatiṁ anuppādadhammāni",
         "&ldquo;cut off at the root, made like a palm stump, "
         "obliterated, and unable to arise in the future&rdquo; "
         "&mdash; the strong, repeated description of how completely "
         "these questions are dissolved."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.35:1.1-1.1"),
        ("p", "&sect;2", "sn12.35:1.2-1.4"),
        ("p", "&sect;3", "sn12.35:1.5-1.11"),
        ("p", "&sect;4", "sn12.35:2.1-2.6"),
        ("p", "&sect;5", "sn12.35:3.1-3.13"),
        ("p", "&sect;6", "sn12.35:4.1-4.6"),
        ("p", "&sect;7", "sn12.35:5.1-5.3"),
        ("p", "&sect;8", "sn12.35:6.1-6.3"),
        ("p", "&sect;9", "sn12.35:7.1-7.9"),
        ("p", "&sect;10", "sn12.35:8.1-8.3"),
    ],
    quiz=[
        {"q": "What does the mendicant first ask about?",
         "opts": [
             "What old age and death are, and who they belong to",
             "What consciousness is made of",
             "Whether the Buddha has attained awakening",
             "How long the path to liberation takes"],
         "correct": 0,
         "expl": "The first of four rounds of the same kind of question."},
        {"q": "How does the Buddha respond to the question?",
         "opts": [
             "He declares it not a fit question, rather than answering it directly",
             "He answers it in full detail immediately",
             "He asks another mendicant to answer instead",
             "He remains silent and changes the subject"],
         "correct": 0,
         "expl": "A refusal of the question's premise, not a direct answer."},
        {"q": "What two views does the Buddha say the question conceals?",
         "opts": [
             "That the soul and body are the same, or that they are two different things",
             "That the world is eternal, or that it is not eternal",
             "That the Buddha exists after death, or does not",
             "That suffering is caused by the gods, or by chance"],
         "correct": 0,
         "expl": "Two mirrored forms of identity view, both said to make the spiritual life impossible."},
        {"q": "How does the Buddha restate the link instead of answering \"who it belongs to\"?",
         "opts": [
             "As a purely conditional statement — rebirth is a requirement for old age and death",
             "By naming a specific person to whom it belongs",
             "By declaring that no answer is possible at all",
             "By quoting an older verse from the Sutta Nipāta"],
         "correct": 0,
         "expl": "Replacing ownership with conditionality — the middle way's actual content here."},
        {"q": "How many times is this same question-and-rejection pattern repeated?",
         "opts": [
             "Four times, moving back through old age and death, rebirth, continued existence, and choices",
             "Once only",
             "Twelve times, once for each link in the chain",
             "Three times"],
         "correct": 0,
         "expl": "A deliberate, unhurried repetition across four links."},
        {"q": "What happens to these malformed questions once ignorance fades away completely?",
         "opts": [
             "They are cut off at the root, made like a palm stump, and unable to arise again",
             "They become easier to answer correctly",
             "They are replaced by a new set of questions",
             "The discourse doesn't say what happens to them"],
         "correct": 0,
         "expl": "A strong description of complete dissolution, not mere improvement."},
        {"q": "How many matching cessation paragraphs close the discourse?",
         "opts": [
             "Four, mirroring the four questions examined earlier",
             "One general summary paragraph",
             "Twelve, one for each link",
             "Two"],
         "correct": 0,
         "expl": "A structural mirror of the four-part examination."},
        {"q": "What does the middle way avoid, according to this discourse's closing formula?",
         "opts": [
             "The two extremes of identity view named earlier in the discourse",
             "The extremes of pleasure and pain",
             "The extremes of eternalism and annihilationism about the cosmos",
             "The extremes of silence and speech"],
         "correct": 0,
         "expl": "The same formula used elsewhere in this saṃyutta for a related but distinct pair of extremes."},
        {"q": "Who asks the questions in this discourse?",
         "opts": [
             "An unnamed mendicant",
             "Venerable Sāriputta",
             "Venerable Ānanda",
             "A group of brahmins"],
         "correct": 0,
         "expl": "No name is given for the questioner."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A question refused, not answered", [
            "\"not a fit question\" &mdash;",
            "the premise itself rejected",
        ]),
        ("Two extremes, named precisely", [
            "same soul and body, or two apart &mdash;",
            "both close off the spiritual life",
        ]),
        ("Four questions, one pattern", [
            "old age, rebirth, existence, choices &mdash;",
            "the same rejection each time",
        ]),
        ("Cut off at the root", [
            "made like a palm stump &mdash;",
            "unable to arise again",
        ]),
    ],
    further=[
        '<a href="%s/sn12.35/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.34.html">SN 12.34 &middot; Grounds for Knowledge (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.15.html">SN 12.15 &middot; Kaccānagotta</a> '
        "&mdash; the earlier discourse using the same closing formula "
        "for a related but distinct pair of extremes, about "
        "existence and non-existence rather than identity.",
        '<a href="sn-12.36.html">SN 12.36 &middot; Ignorance is a Condition (2nd)</a> '
        "&mdash; the next discourse, restating this same teaching as "
        "a direct address to the assembled mendicants.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.36 — Dutiyaavijjāpaccayasutta
# --------------------------------------------------------------------------- #
page(
    12, 36, "Dutiyaavijjāpaccaya", "Ignorance is a Condition (2nd)",
    meta_title="SN 12.36 — Ignorance is a Condition (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaavijjāpaccayasutta — the same identity-view "
        "teaching as SN 12.35, recast as a direct address to the "
        "assembled mendicants rather than an answer to a question. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same four-question, four-cessation structure "
                 "as SN 12.35, but delivered as direct instruction "
                 "rather than triggered by a question"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as SN 12.35, in more "
                       "compressed form"),
    ],
    why=(
        "This discourse carries the identical teaching as SN 12.35 "
        "&mdash; the same two extremes of identity view, the same "
        "middle way, the same four questions run back through old "
        "age and death, rebirth, continued existence, and choices, "
        "and the same four matching cessation paragraphs &mdash; but "
        "delivered in a different narrative shape. There is no "
        "mendicant asking a question that gets rejected; instead the "
        "Buddha tells the assembled mendicants directly what they "
        "might say and why saying it would rest on identity view. "
        "Reading the two discourses side by side shows how much of "
        "SN 12.35's dramatic shape &mdash; the question-and-rejection "
        "rhythm &mdash; is a narrative choice layered onto a content "
        "that stands perfectly well without it."),
    guide=[
        ("The same content, a different frame", [
            "Every substantive claim in SN 12.35 reappears here "
            "&mdash; the two identity-view extremes, the middle way "
            "formula, the four questions, the four cessation "
            "paragraphs &mdash; but the frame of an individual "
            "mendicant asking and being corrected is gone."]),
        ("Hypothetical speech instead of an actual question", [
            "Rather than a mendicant asking \"what is old age and "
            "death,\" the Buddha tells the group directly, \"you "
            "might say\" this, describing the malformed question as "
            "a hypothetical possibility to be headed off in advance "
            "rather than a mistake actually made and corrected."]),
        ("No opening rejection formula needed", [
            "Because no one has actually asked the malformed "
            "question, the discourse skips SN 12.35's repeated "
            "\"that's not a fit question\" and moves straight to "
            "diagnosing what such a question would rest on."]),
        ("A more compressed middle section", [
            "The middle four links &mdash; continued existence, "
            "grasping, craving, feeling, contact, the six sense "
            "fields, name and form, consciousness &mdash; are run "
            "through with elision here, where SN 12.35 spelled each "
            "one out as its own question-and-answer round."]),
        ("A pairing that rewards reading both together", [
            "Set beside SN 12.35, this discourse functions less as "
            "new content than as a demonstration of how the same "
            "teaching can be delivered defensively, correcting an "
            "error already made, or preemptively, as instruction "
            "given before the error arises."]),
    ],
    terms=[
        ("bhikkhave, yo vadeyya",
         "&ldquo;mendicants, whoever might say&rdquo; &mdash; the "
         "hypothetical framing (rendered by Sujato as &ldquo;you "
         "might say&rdquo;) that replaces SN 12.35's actual question "
         "from an individual mendicant."),
        ("taṁ jīvaṁ taṁ sarīraṁ&hellip; aññaṁ jīvaṁ aññaṁ sarīraṁ",
         "&ldquo;the soul and the body are one and the same&hellip; "
         "the soul is one thing, the body another&rdquo; &mdash; the "
         "same two extremes of identity view named in SN 12.35."),
        ("ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the identical "
         "closing formula carried over from SN 12.35."),
        ("visūkāyikāni visevitāni vipphanditāni",
         "&ldquo;twists, ducks, and dodges&rdquo; &mdash; the same "
         "term for the malformed questions, given up once ignorance "
         "ceases."),
        ("kevalassa dukkhakkhandhassa samudayo",
         "&ldquo;this entire mass of suffering originates&rdquo; "
         "&mdash; the closing phrase of the opening formula, "
         "identical to its use throughout this saṃyutta."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.36:1.1-1.1"),
        ("p", "&sect;2", "sn12.36:1.2-1.4"),
        ("p", "&sect;3", "sn12.36:2.1-2.5"),
        ("p", "&sect;4", "sn12.36:3.1-3.14"),
        ("p", "&sect;5", "sn12.36:4.1-4.3"),
        ("p", "&sect;6", "sn12.36:5.1-5.12"),
    ],
    quiz=[
        {"q": "How is this discourse's teaching delivered, compared to SN 12.35?",
         "opts": [
             "As a direct address to the assembled mendicants, not triggered by a question",
             "As a private conversation with Sāriputta alone",
             "As a verse quoted from an older text",
             "As a dialogue with a visiting brahmin"],
         "correct": 0,
         "expl": "The same content, recast without the question-and-rejection frame."},
        {"q": "Does this discourse use SN 12.35's \"that's not a fit question\" formula?",
         "opts": [
             "No — because no one actually asks the malformed question here",
             "Yes, it repeats the formula four times exactly as SN 12.35 does",
             "Yes, but only once at the very end",
             "The discourse never mentions questions at all"],
         "correct": 0,
         "expl": "There is no actual question to reject in this version."},
        {"q": "What two extremes does this discourse name, just as SN 12.35 does?",
         "opts": [
             "That the soul and body are the same, or that they are two different things",
             "That the world had a beginning, or that it did not",
             "That the Buddha will be reborn, or will not",
             "That suffering can be ended, or cannot"],
         "correct": 0,
         "expl": "The identical pair of identity-view extremes carried over from SN 12.35."},
        {"q": "How are the middle links of the chain treated in this discourse compared to SN 12.35?",
         "opts": [
             "More compressed, run through with elision rather than spelled out one by one",
             "Expanded with additional detail not found in SN 12.35",
             "Omitted entirely",
             "Replaced with an entirely different set of links"],
         "correct": 0,
         "expl": "A more compact restatement of the same material."},
        {"q": "How many matching cessation paragraphs does this discourse contain?",
         "opts": [
             "Two, covering old age and death, and the remaining links together",
             "Four, exactly matching SN 12.35's structure",
             "None; the discourse ends without describing cessation",
             "Twelve, one for each link"],
         "correct": 0,
         "expl": "A more compressed cessation section than SN 12.35's four separate paragraphs."},
        {"q": "What phrase introduces the hypothetical malformed statement in this discourse?",
         "opts": [
             "\"Mendicants, you might say\"",
             "\"A certain mendicant asked\"",
             "\"Sāriputta declared\"",
             "\"It was heard by the assembly\""],
         "correct": 0,
         "expl": "Framing the error as a possibility to be headed off, not an actual mistake made."},
        {"q": "What is the relationship between this discourse and SN 12.35's content?",
         "opts": [
             "Identical substantive teaching, delivered in a different narrative shape",
             "A completely unrelated teaching on an unrelated topic",
             "A direct refutation of SN 12.35",
             "An expansion introducing several new doctrinal points"],
         "correct": 0,
         "expl": "Same teaching, defensive correction replaced with preemptive instruction."},
        {"q": "What does reading these two discourses together demonstrate?",
         "opts": [
             "How much of a discourse's dramatic shape is a narrative choice layered onto stable content",
             "That the two discourses actually teach contradictory doctrines",
             "That one of the two discourses must be a later forgery",
             "Nothing useful; the repetition serves no purpose"],
         "correct": 0,
         "expl": "A demonstration of narrative framing as distinct from doctrinal content."},
        {"q": "Who is the audience for this discourse?",
         "opts": [
             "The assembled mendicants as a group",
             "A single unnamed mendicant",
             "King Pasenadi and his court",
             "A gathering of brahmins"],
         "correct": 0,
         "expl": "Addressed collectively, unlike SN 12.35's one-on-one exchange."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting as SN 12.35, immediately before it."},
    ],
    marginalia=[
        ("The same teaching, no question asked", [
            "\"you might say\" &mdash; a hypothetical,",
            "not a mistake actually made",
        ]),
        ("Correction offered before the fall", [
            "heading off an error in advance &mdash;",
            "rather than repairing one already made",
        ]),
        ("The chain's middle, run through briefer", [
            "elided where SN 12.35 spelled it out &mdash;",
            "the same links, less unfolded",
        ]),
        ("Two discourses, one teaching", [
            "narrative shape set aside &mdash;",
            "the content stands without it",
        ]),
    ],
    further=[
        '<a href="%s/sn12.36/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.35.html">SN 12.35 &middot; Ignorance is a Condition</a> '
        "&mdash; the discourse immediately before this one, carrying "
        "identical content as an answer to an actual question.",
        '<a href="sn-12.37.html">SN 12.37 &middot; Not Yours</a> '
        "&mdash; the next discourse, turning from identity view about "
        "the chain's links to identity view about the body itself.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.37 — Natumhasutta
# --------------------------------------------------------------------------- #
page(
    12, 37, "Natumha", "Not Yours",
    meta_title="SN 12.37 — Not Yours | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Natumhasutta — the body belongs neither to you nor to "
        "anyone else, being old kamma to be felt, and the learned "
        "noble disciple turns instead to dependent origination "
        "itself, applied both forward and in reverse. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A short, direct teaching in two parts &mdash; a "
                 "claim about the body's ownership, followed by the "
                 "chain applied forward and in reverse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but its opening claim is easy to "
                       "misread"),
    ],
    why=(
        "Coming directly after two discourses dismantling the "
        "identity view built into asking who a link in the chain "
        "belongs to, this discourse turns the same question onto the "
        "body itself and gives a striking, easily misread answer: "
        "the body doesn't belong to you, but it doesn't belong to "
        "anyone else either. It is old kamma, produced by past "
        "choices and intentions, simply something to be felt. Having "
        "cleared away both the idea that the body is a self one owns "
        "and the idea that it belongs to some other agent, the "
        "discourse redirects attention entirely: rather than asking "
        "whose the body is, the learned noble disciple applies the "
        "mind carefully to dependent origination itself, running the "
        "chain forward to suffering's arising and in reverse to its "
        "complete cessation."),
    guide=[
        ("Not yours, but not anyone else's either", [
            "The opening claim is easy to hear as simply denying "
            "personal ownership of the body, but the discourse is "
            "careful to deny both halves at once: it doesn't belong "
            "to you, and it doesn't belong to anyone else."]),
        ("Old kamma, not a fresh creation", [
            "The body is described as something already produced "
            "&mdash; old deeds, formed by past choices and intentions "
            "&mdash; framing it as a result to be felt rather than a "
            "possession currently being claimed by any owner."]),
        ("A redirection, not a further argument", [
            "Rather than continuing to argue about ownership, the "
            "discourse simply changes the subject: the learned noble "
            "disciple's attention moves to dependent origination "
            "itself, addressed directly by name rather than through "
            "any question about who possesses what."]),
        ("The this/that conditionality formula stated in full", [
            "This discourse gives the compact, general statement of "
            "conditionality &mdash; when this exists, this comes to "
            "be; due to the arising of this, this arises &mdash; "
            "before applying it to the familiar twelve-link chain, "
            "making explicit the principle the chain is a specific "
            "case of."]),
        ("Both directions given in full, side by side", [
            "The discourse doesn't stop at describing how suffering "
            "arises; it immediately restates the entire chain in "
            "reverse, link by link, so that arising and complete "
            "cessation appear as two halves of the same short "
            "teaching."]),
    ],
    terms=[
        ("nāyaṁ, bhikkhave, kāyo tumhākaṁ napi aññesaṁ",
         "&ldquo;this body doesn't belong to you or to anyone "
         "else&rdquo; &mdash; the discourse's opening claim, denying "
         "ownership in both directions at once."),
        ("purāṇamidaṁ, bhikkhave, kammaṁ abhisaṅkhataṁ "
         "abhisañcetayitaṁ vedaniyaṁ",
         "&ldquo;old deeds, produced by choices and intentions, "
         "as something to be felt&rdquo; &mdash; how the body is "
         "described instead of as an owned possession."),
        ("sutavā ariyasāvako",
         "&ldquo;a learned noble disciple&rdquo; &mdash; the figure "
         "whose careful, rational attention is described turning to "
         "dependent origination itself."),
        ("paṭiccasamuppādaññeva sādhukaṁ yoniso manasi karoti",
         "&ldquo;carefully and rationally applies the mind to "
         "dependent origination itself&rdquo; &mdash; the "
         "redirection away from questions of ownership."),
        ("iti imasmiṁ sati idaṁ hoti, imassuppādā idaṁ uppajjati",
         "&ldquo;when this exists, this comes to be; due to the "
         "arising of this, this arises&rdquo; &mdash; the general "
         "this/that conditionality formula stated before the "
         "familiar chain is run through it."),
    ],
    text_intro=(
        "The discourse in full. The middle of the twelve-link chain "
        "is elided in both directions, exactly as bilara-data "
        "preserves it, trusting the reader's familiarity with SN "
        "12.1&ndash;2. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.37:1.1-1.3"),
        ("p", "&sect;2", "sn12.37:2.1-2.6"),
        ("p", "&sect;3", "sn12.37:2.7-2.9"),
    ],
    quiz=[
        {"q": "What does the discourse say about who the body belongs to?",
         "opts": [
             "It belongs neither to you nor to anyone else",
             "It belongs entirely to the individual who carries it",
             "It belongs to one's parents",
             "The discourse declines to say"],
         "correct": 0,
         "expl": "Ownership denied in both directions at once."},
        {"q": "How is the body described instead of as an owned possession?",
         "opts": [
             "As old deeds, produced by past choices and intentions, to be felt",
             "As a gift freely given by the gods",
             "As an illusion with no basis in past action",
             "As something created anew at each moment with no history"],
         "correct": 0,
         "expl": "A result of prior kamma, not a currently claimed possession."},
        {"q": "What does the learned noble disciple turn their attention to?",
         "opts": [
             "Dependent origination itself, applied carefully and rationally",
             "A renewed search for who truly owns the body",
             "The question of when the body was first created",
             "A debate with other ascetics about ownership"],
         "correct": 0,
         "expl": "A redirection away from ownership questions entirely."},
        {"q": "What general formula does this discourse state before applying the twelve-link chain?",
         "opts": [
             "\"When this exists, this comes to be; due to the arising of this, this arises\"",
             "\"All conditioned things are impermanent\"",
             "\"Whatever has a beginning has an ending\"",
             "The discourse states no general formula"],
         "correct": 0,
         "expl": "The compact this/that conditionality principle underlying the specific chain."},
        {"q": "In which directions is the twelve-link chain given in this discourse?",
         "opts": [
             "Both forward, toward suffering's arising, and in reverse, toward its cessation",
             "Only forward, toward suffering's arising",
             "Only in reverse, toward cessation",
             "Neither direction is given; only the general formula appears"],
         "correct": 0,
         "expl": "Arising and complete cessation given as two halves of one short teaching."},
        {"q": "What immediately precedes this discourse in the saṃyutta?",
         "opts": [
             "Two discourses examining identity view built into asking who a chain-link belongs to",
             "A long narrative about King Pasenadi",
             "A discourse on the four noble truths unrelated to this one's theme",
             "Nothing; this is the saṃyutta's opening discourse"],
         "correct": 0,
         "expl": "This discourse extends the same identity-view critique to the body itself."},
        {"q": "How does the discourse describe the body's origin?",
         "opts": [
             "As produced by past choices and intentions",
             "As arising without any cause",
             "As created directly by consciousness in the present moment",
             "As inherited unchanged from a prior life without modification"],
         "correct": 0,
         "expl": "Explicitly the product of prior volitional action."},
        {"q": "Is the middle of the twelve-link chain spelled out in full in this discourse's source text?",
         "opts": [
             "No — it's elided in both directions, trusting familiarity from earlier discourses",
             "Yes, every link is spelled out twice",
             "Only the forward direction is spelled out in full",
             "Only the reverse direction is spelled out in full"],
         "correct": 0,
         "expl": "Preserved exactly as bilara-data elides it, in keeping with earlier discourses in this book."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "Kaḷāra the Aristocrat"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
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
        ("Not yours &mdash; nor anyone else's", [
            "ownership denied both ways &mdash;",
            "the body claimed by no one",
        ]),
        ("Old kamma, not a fresh possession", [
            "formed by past choices &mdash;",
            "something to be felt, not owned",
        ]),
        ("A question set aside entirely", [
            "attention turns to what conditions what &mdash;",
            "not to who stands behind it",
        ]),
        ("Arising and ceasing, side by side", [
            "the chain run forward, then reversed &mdash;",
            "one short teaching, both halves given",
        ]),
    ],
    further=[
        '<a href="%s/sn12.37/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.36.html">SN 12.36 &middot; Ignorance is a Condition (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.38.html">SN 12.38 &middot; Intention</a> '
        "&mdash; the next discourse, turning from the body's "
        "ownership to what sustains consciousness across rebirth.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.38 — Cetanāsutta
# --------------------------------------------------------------------------- #
page(
    12, 38, "Cetanā", "Intention",
    meta_title="SN 12.38 — Intention | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Cetanāsutta — what one intends, plans, or merely has "
        "underlying tendencies for becomes a support for "
        "consciousness's continuation, feeding rebirth even when no "
        "active intending is present. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Three parallel cases, run through an identical "
                 "mechanism &mdash; a support for consciousness, "
                 "establishment, regeneration, and the arising of "
                 "the whole mass of suffering &mdash; with the third "
                 "case reversing every step into cessation"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "a compact but doctrinally dense account of "
                       "how kamma sustains rebirth"),
    ],
    why=(
        "This discourse gives one of the most precise accounts in "
        "this saṃyutta of how volitional activity actually feeds "
        "rebirth. What one intends, plans, or has underlying "
        "tendencies for becomes a support on which consciousness can "
        "become established; once established and grown, it "
        "regenerates into a new state of existence, bringing future "
        "rebirth, old age, death, and the whole train of grief in "
        "its wake. What makes the discourse's structure worth "
        "attending to closely is its second case: even where active "
        "intending and planning are absent, underlying tendencies "
        "alone are still enough to provide the same support and set "
        "the same process going. Only where none of the three &mdash; "
        "intending, planning, or underlying tendency &mdash; remains "
        "at all does the entire chain fail to get a foothold, and "
        "the whole mass of suffering ceases."),
    guide=[
        ("Three ingredients, not one", [
            "The discourse names three distinct things &mdash; "
            "intending, planning, and underlying tendency &mdash; "
            "rather than treating volition as a single undifferentiated "
            "activity, and then examines what happens when each "
            "combination is present or absent."]),
        ("A support, not a cause in isolation", [
            "What is intended, planned, or latent doesn't directly "
            "produce rebirth; it becomes an ārammaṇa, an object or "
            "support, on which consciousness can become established "
            "&mdash; a more precise, mechanical image than simple "
            "causation."]),
        ("The second case is the discourse's real point", [
            "The first case, where active intending and planning are "
            "both present, is unsurprising; the second case, where "
            "neither is present but underlying tendency remains, "
            "shows that dormant tendency alone is sufficient &mdash; "
            "liberation can't be achieved by merely suspending active "
            "volition while tendencies remain unresolved."]),
        ("Only the third case breaks the chain entirely", [
            "It's only when intending, planning, and underlying "
            "tendency are all three absent that consciousness gains "
            "no support, fails to become established, and the entire "
            "sequence toward future rebirth simply doesn't occur."]),
        ("A compressed final step, unlike SN 12.39", [
            "Once consciousness is established and grows, this "
            "discourse moves straight to regeneration into a new "
            "existence and the arising of old age and death, without "
            "spelling out the intervening links of name and form, the "
            "six sense fields, contact, and the rest &mdash; a "
            "compression the very next discourse, SN 12.39, doesn't "
            "make."]),
    ],
    terms=[
        ("ceteti&hellip; pakappeti&hellip; anuseti",
         "&ldquo;intends&hellip; plans&hellip; has underlying "
         "tendencies for&rdquo; &mdash; the three distinct volitional "
         "ingredients the discourse examines in combination."),
        ("ārammaṇametaṁ hoti viññāṇassa ṭhitiyā",
         "&ldquo;this becomes a support for the continuation of "
         "consciousness&rdquo; &mdash; the precise mechanical image "
         "linking intention to consciousness's persistence."),
        ("patiṭṭhā viññāṇassa",
         "&ldquo;consciousness becomes established&rdquo; &mdash; "
         "the step that follows once a support is present."),
        ("āyatiṁ punabbhavābhinibbatti",
         "&ldquo;regeneration into a new state of existence in the "
         "future&rdquo; &mdash; what follows once consciousness is "
         "established and grows."),
        ("anuseti",
         "&ldquo;has underlying tendencies for&rdquo; &mdash; the "
         "one ingredient of the three that alone, even without active "
         "intending or planning, is still sufficient to sustain the "
         "whole process, as the discourse's second case shows."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.38:1.1-1.1"),
        ("p", "&sect;2", "sn12.38:1.2-1.6"),
        ("p", "&sect;3", "sn12.38:2.1-2.5"),
        ("p", "&sect;4", "sn12.38:3.1-3.5"),
    ],
    quiz=[
        {"q": "What three things does the discourse examine as possible supports for consciousness?",
         "opts": [
             "Intending, planning, and having underlying tendencies",
             "Seeing, hearing, and touching",
             "Craving, grasping, and continued existence",
             "Ignorance, choices, and consciousness alone"],
         "correct": 0,
         "expl": "Three distinct volitional ingredients, examined in combination."},
        {"q": "What does an intention or underlying tendency become, according to this discourse?",
         "opts": [
             "A support (ārammaṇa) for the continuation of consciousness",
             "An immediate, direct cause of physical illness",
             "A permanent, unchanging feature of the mind",
             "The discourse doesn't describe what it becomes"],
         "correct": 0,
         "expl": "A precise, mechanical image of support rather than simple causation."},
        {"q": "In the discourse's second case, what is present and what is absent?",
         "opts": [
             "Underlying tendency is present, but active intending and planning are absent",
             "All three — intending, planning, and underlying tendency — are present",
             "None of the three is present",
             "Only planning is present, with intending and underlying tendency both absent"],
         "correct": 0,
         "expl": "The case that shows dormant tendency alone is sufficient."},
        {"q": "What does the second case show about liberation?",
         "opts": [
             "That suspending active volition alone isn't enough if underlying tendencies remain",
             "That underlying tendencies are harmless once intending stops",
             "That liberation requires only stopping active planning",
             "That the discourse says nothing relevant to liberation"],
         "correct": 0,
         "expl": "Dormant tendency alone is enough to sustain the process toward rebirth."},
        {"q": "What must be entirely absent for consciousness to gain no support at all?",
         "opts": [
             "Intending, planning, and underlying tendency, all three",
             "Only intending",
             "Only underlying tendency",
             "Physical contact with the world"],
         "correct": 0,
         "expl": "Only the third case, with all three absent, breaks the chain entirely."},
        {"q": "What happens once consciousness is established and grows, in this discourse's account?",
         "opts": [
             "Regeneration into a new state of existence in the future",
             "Consciousness immediately ceases on its own",
             "The mendicant achieves awakening automatically",
             "Nothing further is described"],
         "correct": 0,
         "expl": "The step leading toward future rebirth, old age, and death."},
        {"q": "How does this discourse's final step compare to SN 12.39's account?",
         "opts": [
             "It is more compressed, skipping the intervening links SN 12.39 spells out",
             "It is more detailed, adding links SN 12.39 omits",
             "The two discourses give identical final steps with no difference",
             "This discourse has no final step at all"],
         "correct": 0,
         "expl": "SN 12.39 spells out name and form, the six sense fields, and the rest explicitly."},
        {"q": "What closes the description of both the arising cases in this discourse?",
         "opts": [
             "\"This entire mass of suffering originates\"",
             "\"The mendicant is praised by the assembly\"",
             "\"The Buddha smiles and falls silent\"",
             "\"This is called right view\""],
         "correct": 0,
         "expl": "The recurring closing phrase marking suffering's arising."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "Kaḷāra the Aristocrat"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
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
        ("Three ingredients, not one", [
            "intending, planning, latent tendency &mdash;",
            "examined each in combination",
        ]),
        ("A support, precisely named", [
            "not cause alone, but a foothold &mdash;",
            "consciousness given somewhere to stand",
        ]),
        ("Dormant alone is still enough", [
            "no active intending required &mdash;",
            "the second case, quietly decisive",
        ]),
        ("Only all three absent breaks it", [
            "no foothold, no establishment &mdash;",
            "the whole mass of suffering ceases",
        ]),
    ],
    further=[
        '<a href="%s/sn12.38/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.37.html">SN 12.37 &middot; Not Yours</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.39.html">SN 12.39 &middot; Intention (2nd)</a> '
        "&mdash; the next discourse, spelling out the same mechanism "
        "through the full chain from name and form onward.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.39 — Dutiyacetanāsutta
# --------------------------------------------------------------------------- #
page(
    12, 39, "Dutiyacetanā", "Intention (2nd)",
    meta_title="SN 12.39 — Intention (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyacetanāsutta — the same intention-as-support "
        "mechanism as SN 12.38, this time spelled out through the "
        "full twelve-link chain from name and form's descent onward. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same three-case structure as SN 12.38, but "
                 "with consciousness's establishment connected "
                 "explicitly to the full downstream chain rather "
                 "than compressed into a single step"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the same density as SN 12.38, extended "
                       "across more links"),
    ],
    why=(
        "This discourse repeats SN 12.38's three-case structure "
        "&mdash; intending and planning present, only underlying "
        "tendency present, none of the three present &mdash; but "
        "fills in what the previous discourse compressed. Where SN "
        "12.38 moved directly from consciousness's establishment to "
        "regeneration into a new existence, this discourse spells "
        "out the specific mechanism: once consciousness is "
        "established, name and form are conceived, and from there "
        "the familiar chain runs forward exactly as in SN 12.1 "
        "&mdash; the six sense fields, contact, feeling, craving, "
        "grasping, continued existence, rebirth, and old age and "
        "death. Reading the two discourses together shows a single "
        "teaching given at two different resolutions, one naming the "
        "outcome directly and the other naming the specific links "
        "that produce it."),
    guide=[
        ("The same three cases, the same conclusion", [
            "Exactly as in SN 12.38, intending and planning present "
            "leads to suffering's arising, underlying tendency alone "
            "is equally sufficient, and only the complete absence of "
            "all three breaks the chain &mdash; nothing about the "
            "three-case logic itself has changed."]),
        ("Name and form's descent named explicitly", [
            "Where SN 12.38 skipped straight to regeneration, this "
            "discourse names the specific step in between: once "
            "consciousness is established and grows, name and form "
            "are conceived, connecting intention's role directly to "
            "the language used elsewhere for a being's descent into "
            "a new existence."]),
        ("The familiar chain resumed from its usual point", [
            "From name and form onward, the discourse runs through "
            "exactly the links familiar from SN 12.1 and SN 12.2 "
            "&mdash; the six sense fields, contact, feeling, craving, "
            "grasping, continued existence, rebirth, old age and "
            "death &mdash; elided here just as it is elsewhere, "
            "trusting the reader's familiarity."]),
        ("Two discourses at two resolutions", [
            "SN 12.38 and this discourse aren't presenting different "
            "teachings; they're the same account of how intention "
            "sustains rebirth, one compressed to name only the "
            "outcome, the other expanded to show the specific chain "
            "of links that produces it."]),
        ("The same reversal governs cessation here too", [
            "Exactly as in SN 12.38, it's the complete absence of "
            "intending, planning, and underlying tendency together "
            "&mdash; not merely two of the three &mdash; that removes "
            "consciousness's support and brings the entire downstream "
            "chain, now spelled out in full, to cessation."]),
    ],
    terms=[
        ("ceteti&hellip; pakappeti&hellip; anuseti",
         "&ldquo;intends&hellip; plans&hellip; has underlying "
         "tendencies for&rdquo; &mdash; the same three volitional "
         "ingredients examined in SN 12.38."),
        ("ārammaṇametaṁ hoti viññāṇassa ṭhitiyā",
         "&ldquo;this becomes a support for the continuation of "
         "consciousness&rdquo; &mdash; the identical mechanical image "
         "carried over from SN 12.38."),
        ("nāmarūpassa avakkanti",
         "&ldquo;name and form are conceived&rdquo; &mdash; literally "
         "name and form's descent, the specific step this discourse "
         "names where SN 12.38 skipped straight to regeneration."),
        ("nāmarūpapaccayā saḷāyatanaṁ",
         "&ldquo;name and form are requirements for the six sense "
         "fields&rdquo; &mdash; the point where the familiar "
         "twelve-link chain resumes and is elided onward as usual."),
        ("nāmarūpanirodhā saḷāyatananirodho",
         "&ldquo;when name and form cease, the six sense fields "
         "cease&rdquo; &mdash; the reverse direction, given once all "
         "three volitional ingredients are entirely absent."),
    ],
    text_intro=(
        "The discourse in full. The chain from name and form onward "
        "is elided in the source exactly as bilara-data preserves "
        "it, trusting the reader's familiarity with SN 12.1&ndash;2. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.39:1.1-1.1"),
        ("p", "&sect;2", "sn12.39:1.2-1.14"),
        ("p", "&sect;3", "sn12.39:2.1-2.5"),
        ("p", "&sect;4", "sn12.39:3.1-3.5"),
    ],
    quiz=[
        {"q": "What structure does this discourse share with SN 12.38?",
         "opts": [
             "The same three cases — intending and planning present, tendency alone present, none present",
             "A completely different structure with no shared cases",
             "A single case rather than three",
             "Five cases rather than three"],
         "correct": 0,
         "expl": "The identical three-case logic governing suffering's arising and cessation."},
        {"q": "What specific step does this discourse name that SN 12.38 skipped over?",
         "opts": [
             "Name and form's descent, once consciousness is established and grows",
             "The Buddha's own past lives",
             "The precise location of Sāvatthī",
             "The names of the mendicants present"],
         "correct": 0,
         "expl": "The link SN 12.38 compressed by moving straight to regeneration."},
        {"q": "From name and form onward, which links does this discourse run through?",
         "opts": [
             "The familiar twelve-link chain — six sense fields, contact, feeling, craving, and onward",
             "An entirely different sequence not found elsewhere in this saṃyutta",
             "Only two further links before stopping",
             "No further links; the discourse ends at name and form"],
         "correct": 0,
         "expl": "The chain familiar from SN 12.1 and SN 12.2, elided here as elsewhere."},
        {"q": "What must be absent for the entire chain, now spelled out in full, to cease?",
         "opts": [
             "Intending, planning, and underlying tendency, all three together",
             "Only intending, regardless of the other two",
             "Only underlying tendency, regardless of the other two",
             "Physical contact alone"],
         "correct": 0,
         "expl": "The same complete-absence requirement as SN 12.38's third case."},
        {"q": "How do SN 12.38 and this discourse relate to each other?",
         "opts": [
             "The same teaching given at two resolutions, one compressed and one expanded",
             "Contradictory teachings that cannot both be correct",
             "Entirely unrelated discourses on different topics",
             "This discourse replaces and supersedes SN 12.38"],
         "correct": 0,
         "expl": "One names the outcome directly, the other spells out the specific links producing it."},
        {"q": "What does \"nāmarūpassa avakkanti\" literally mean?",
         "opts": [
             "Name and form's descent",
             "The cessation of all suffering",
             "The arising of ignorance",
             "The Buddha's enlightenment"],
         "correct": 0,
         "expl": "Language elsewhere associated with a being's entry into a new existence."},
        {"q": "Is the underlying-tendency-alone case in this discourse sufficient to sustain the chain?",
         "opts": [
             "Yes — exactly as in SN 12.38, tendency alone is enough even without active intending",
             "No, this discourse says tendency alone is never sufficient",
             "The discourse doesn't address this case at all",
             "Only if combined with active planning"],
         "correct": 0,
         "expl": "The same conclusion as SN 12.38's second case, now run through the full chain."},
        {"q": "How is the middle of the chain treated in this discourse's source text?",
         "opts": [
             "Elided, trusting the reader's familiarity from SN 12.1 and SN 12.2",
             "Spelled out in complete, unelided detail",
             "Omitted entirely with no trace",
             "Replaced with a different formula altogether"],
         "correct": 0,
         "expl": "Preserved exactly as bilara-data elides it."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "Kaḷāra the Aristocrat"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
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
        ("The same three cases, again", [
            "intending, tendency alone, neither &mdash;",
            "unchanged from the discourse before",
        ]),
        ("A step named, not skipped this time", [
            "name and form's descent &mdash;",
            "spelled out where SN 12.38 compressed it",
        ]),
        ("The familiar chain, resumed", [
            "six fields, contact, feeling, craving &mdash;",
            "run forward exactly as before",
        ]),
        ("One teaching, two resolutions", [
            "compressed once, expanded once &mdash;",
            "the same mechanism, seen at each scale",
        ]),
    ],
    further=[
        '<a href="%s/sn12.39/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.38.html">SN 12.38 &middot; Intention</a> '
        "&mdash; the discourse immediately before this one, giving "
        "the same mechanism in compressed form.",
        '<a href="sn-12.40.html">SN 12.40 &middot; Intention (3rd)</a> '
        "&mdash; the next discourse, closing this chapter with a "
        "still more detailed account of the steps toward rebirth.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.40 — Tatiyacetanāsutta
# --------------------------------------------------------------------------- #
page(
    12, 40, "Tatiyacetanā", "Intention (3rd)",
    meta_title="SN 12.40 — Intention (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Tatiyacetanāsutta — the same intention-as-support "
        "mechanism as SN 12.38 and SN 12.39, this time naming an "
        "inclination, a coming and going, and a passing away and "
        "reappearing between consciousness and rebirth, closing "
        "Kaḷārakhattiyavagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same three-case structure as SN 12.38 and SN "
                 "12.39, this time naming three intermediate steps "
                 "&mdash; inclination, coming and going, passing "
                 "away and reappearing &mdash; not spelled out in "
                 "either earlier discourse"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "closes this chapter with its most granular "
                       "account of rebirth's mechanics"),
    ],
    why=(
        "Closing Kaḷārakhattiyavagga, this third and final discourse "
        "on intention repeats the same three-case structure as SN "
        "12.38 and SN 12.39, but names a set of intermediate steps "
        "neither earlier discourse spelled out. Once consciousness "
        "is established and grows, this discourse says, there is an "
        "inclination; where there is inclination, there is a coming "
        "and going; where there is coming and going, there is a "
        "passing away and reappearing; and only then does future "
        "rebirth, old age, and death follow. These three terms "
        "&mdash; leaning, transit, and the death-and-rebirth "
        "transition itself &mdash; give the most granular picture in "
        "this trio of discourses of what actually happens between "
        "consciousness's establishment and a new life's beginning, "
        "closing the vagga on its most mechanically detailed note."),
    guide=[
        ("A third variation on a stable pattern", [
            "The same three cases governing arising and cessation "
            "&mdash; intending and planning present, tendency alone "
            "present, none of the three present &mdash; return here "
            "unchanged for a third time, confirming this is the "
            "stable frame the trio of discourses shares."]),
        ("An inclination named where the others named nothing", [
            "Between consciousness's growth and what follows, this "
            "discourse inserts nati, an inclination or leaning "
            "&mdash; a term neither SN 12.38 nor SN 12.39 uses, "
            "describing something like a tilt toward a coming "
            "existence before that existence has taken any further "
            "shape."]),
        ("Coming and going, then passing away and reappearing", [
            "From that inclination, the discourse names a coming and "
            "going (āgatigati) and then a passing away and "
            "reappearing (cutūpapāta) &mdash; the second term the "
            "same one used elsewhere in the canon for the divine "
            "eye's knowledge of beings passing away and re-arising "
            "according to their deeds."]),
        ("Three discourses, one mechanism, three levels of detail", [
            "Set beside SN 12.38's single compressed step and SN "
            "12.39's full twelve-link chain from name and form "
            "onward, this discourse's three intermediate terms give "
            "a third, still more granular way of describing the same "
            "underlying process, none of them contradicting the "
            "others."]),
        ("Closing the vagga on rebirth's fine mechanics", [
            "Ending Kaḷārakhattiyavagga here, on the most detailed of "
            "the three intention discourses, leaves the chapter's "
            "close focused not on a dramatic narrative but on the "
            "precise, unglamorous steps by which volition actually "
            "carries a being from one existence into the next."]),
    ],
    terms=[
        ("ceteti&hellip; pakappeti&hellip; anuseti",
         "&ldquo;intends&hellip; plans&hellip; has underlying "
         "tendencies for&rdquo; &mdash; the same three volitional "
         "ingredients examined in SN 12.38 and SN 12.39."),
        ("nati",
         "&ldquo;an inclination&rdquo; &mdash; the leaning toward a "
         "coming existence named here where the two earlier "
         "discourses in this trio name nothing between consciousness "
         "and what follows."),
        ("āgatigati",
         "&ldquo;coming and going&rdquo; &mdash; the movement that "
         "follows from inclination, before rebirth itself occurs."),
        ("cutūpapāto",
         "&ldquo;passing away and reappearing&rdquo; &mdash; the "
         "same term used elsewhere in the canon for the divine eye's "
         "direct knowledge of beings' deaths and rebirths."),
        ("āyatiṁ jāti jarāmaraṇaṁ",
         "&ldquo;future rebirth, old age, and death&rdquo; &mdash; "
         "what follows only after inclination, coming and going, and "
         "passing away and reappearing have all occurred."),
    ],
    text_intro=(
        "The discourse in full, closing Kaḷārakhattiyavagga. The "
        "chapter's closing verse of discourse titles is not "
        "translated in the source and is not quoted here; see the "
        "reading guide above for its contents. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.40:1.1-1.1"),
        ("p", "&sect;2", "sn12.40:1.2-1.8"),
        ("p", "&sect;3", "sn12.40:2.1-2.7"),
        ("p", "&sect;4", "sn12.40:3.1-3.7"),
    ],
    quiz=[
        {"q": "What structure does this discourse share with SN 12.38 and SN 12.39?",
         "opts": [
             "The same three cases — intending and planning present, tendency alone present, none present",
             "A structure with only one case, unlike the other two discourses",
             "A structure with five cases rather than three",
             "No shared structure at all"],
         "correct": 0,
         "expl": "The stable three-case frame running through all three intention discourses."},
        {"q": "What does this discourse name once consciousness is established and grows, that the other two don't?",
         "opts": [
             "An inclination (nati)",
             "A vision of a past life",
             "A conversation with another mendicant",
             "A journey to a specific named city"],
         "correct": 0,
         "expl": "A term unique to this third discourse in the trio."},
        {"q": "What follows the inclination, according to this discourse?",
         "opts": [
             "A coming and going (āgatigati)",
             "Immediate final liberation",
             "A return to the inclination itself in an endless loop",
             "The discourse names nothing further"],
         "correct": 0,
         "expl": "The next of three intermediate steps unique to this discourse."},
        {"q": "What does cutūpapāta refer to, and where else does the term appear in the canon?",
         "opts": [
             "Passing away and reappearing — the same term used for the divine eye's knowledge of rebirth",
             "A type of meditative absorption unrelated to rebirth",
             "A geographic location near Sāvatthī",
             "A ritual offering made by lay followers"],
         "correct": 0,
         "expl": "Language shared with descriptions of the divine eye elsewhere in the canon."},
        {"q": "How do this discourse's three intermediate terms compare to SN 12.38 and SN 12.39?",
         "opts": [
             "They give a third, more granular way of describing the same underlying process",
             "They directly contradict what SN 12.38 and SN 12.39 describe",
             "They describe an entirely unrelated process",
             "They are identical in wording to SN 12.39's account"],
         "correct": 0,
         "expl": "Three discourses, one mechanism, three different levels of descriptive detail."},
        {"q": "What must be absent for this entire sequence to cease, according to the third case?",
         "opts": [
             "Intending, planning, and underlying tendency, all three together",
             "Only the inclination, regardless of the other two ingredients",
             "Only coming and going, regardless of the rest",
             "Physical contact alone"],
         "correct": 0,
         "expl": "The same complete-absence requirement shared with SN 12.38 and SN 12.39."},
        {"q": "What chapter does this discourse close?",
         "opts": [
             "Kaḷārakhattiyavagga",
             "Buddhavagga",
             "Dasabalavagga",
             "Gahapativagga"],
         "correct": 0,
         "expl": "The fourth chapter of Nidānavagga, named for SN 12.32's aristocrat."},
        {"q": "Is the chapter's closing verse of discourse titles quoted in this reading guide's text section?",
         "opts": [
             "No — it isn't translated in the source, and its contents are described in the reading guide instead",
             "Yes, it's quoted in full at the end of the text section",
             "Yes, but only its first line is quoted",
             "The discourse has no closing verse at all"],
         "correct": 0,
         "expl": "Following the same convention used for untranslated closing material elsewhere in this saṃyutta."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "Kaḷāra the Aristocrat"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
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
        ("A third variation, still stable", [
            "the same three cases return &mdash;",
            "unchanged for a third telling",
        ]),
        ("An inclination, newly named", [
            "nati &mdash; a leaning toward becoming &mdash;",
            "absent from the two discourses before",
        ]),
        ("Coming and going, then passing on", [
            "āgatigati, then cutūpapāta &mdash;",
            "the same term used for the divine eye",
        ]),
        ("A chapter closed on fine mechanics", [
            "not narrative, but precise steps &mdash;",
            "how volition carries a being onward",
        ]),
    ],
    further=[
        '<a href="%s/sn12.40/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.39.html">SN 12.39 &middot; Intention (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.31.html">SN 12.31 &middot; What Has Come to Be</a> '
        "&mdash; the discourse opening this chapter, Sāriputta's "
        "threefold seeing standing beside this discourse's threefold "
        "mechanics as two different ways this book examines how "
        "existence takes hold.",
        '<a href="sn-12.41.html">SN 12.41 &middot; Fears and Enmities</a> '
        "&mdash; opening Gahapativagga, this book's fifth chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.41 — Pañcaverabhayasutta
# --------------------------------------------------------------------------- #
page(
    12, 41, "Pañcaverabhaya", "Fears and Enmities",
    meta_title="SN 12.41 — Fears and Enmities | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Pañcaverabhayasutta — opening Gahapativagga, the Buddha "
        "gives the householder Anāthapiṇḍika a precise three-part "
        "self-test for stream-entry: five fears quelled, four "
        "factors possessed, and the noble system seen with wisdom. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and the householder Anāthapiṇḍika"),
        ("Form", "A structured self-test in three parts, each "
                 "unpacked in turn, framed by an identical opening "
                 "and closing declaration"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "structurally clear, though its three parts "
                       "each carry real doctrinal weight"),
    ],
    why=(
        "Opening Gahapativagga, this discourse gives the householder "
        "Anāthapiṇḍika &mdash; the wealthy donor of Jeta's Grove, "
        "encountered elsewhere in this collection both as a "
        "first-time visitor and, after his death, as a returning "
        "deity &mdash; one of the most widely cited checklists in "
        "the early texts for confirming one's own attainment of "
        "stream-entry. A noble disciple who has quelled five fears "
        "(the anxious residue of breaking each of the five "
        "precepts), who possesses four factors (confidence in the "
        "Buddha, the teaching, the Saṅgha, and one's own ethical "
        "conduct), and who has clearly seen and penetrated the noble "
        "system &mdash; dependent origination itself, run forward "
        "and in reverse &mdash; may, if they wish, declare of "
        "themselves that they are a stream-enterer, finished with "
        "rebirth in the lower realms and assured of eventual "
        "awakening. The discourse's value lies precisely in its "
        "structure: it doesn't ask for a feeling of confidence, but "
        "for three independently checkable conditions."),
    guide=[
        ("A self-test, not an external verdict", [
            "The declaration is something the disciple may make of "
            "themselves &mdash; \"so ākaṅkhamāno attanāva attānaṁ "
            "byākareyya\" &mdash; framed as self-knowledge available "
            "to be checked, not a status conferred from outside by "
            "the Buddha or anyone else."]),
        ("Five fears traced to a single mechanism", [
            "Each of the five fears follows an identical pattern: "
            "breaking a precept brings fear and enmity both in this "
            "life and in lives to come, along with mental pain and "
            "sadness, and refraining from it quells exactly that "
            "fear &mdash; the same causal shape repeated once for "
            "each of the five precepts."]),
        ("Four factors, three of them relational and one personal", [
            "Three of the four factors are confidence in something "
            "outside oneself &mdash; the Buddha, the teaching, the "
            "Saṅgha &mdash; described in a fixed formula of "
            "experiential confidence, while the fourth turns inward "
            "to one's own ethical conduct, described as loved by the "
            "noble ones and leading to immersion."]),
        ("The noble system given its full technical content", [
            "Where the first two parts of the test describe "
            "confidence and conduct, the third part names something "
            "more exacting: dependent origination itself, understood "
            "well enough to be applied to both the arising and the "
            "complete cessation of the whole mass of suffering, "
            "using the language of \"applies the mind carefully and "
            "rationally\" already seen in SN 12.37."]),
        ("A declaration that opens and closes the discourse identically", [
            "The discourse begins by describing the conditions under "
            "which the declaration may be made and ends by having "
            "the Buddha state, word for word, the same conditions and "
            "the same declaration &mdash; a frame that lets the "
            "three-part unpacking sit inside a stable, symmetrical "
            "shell."]),
    ],
    terms=[
        ("pañca bhayāni verāni vūpasantāni honti",
         "&ldquo;five fears and enmities have been quelled&rdquo; "
         "&mdash; the first of the three conditions, unpacked one "
         "precept at a time."),
        ("catūhi ca sotāpattiyaṅgehi samannāgato hoti",
         "&ldquo;possesses the four factors of stream-entry&rdquo; "
         "&mdash; the second condition, three of confidence and one "
         "of conduct."),
        ("ariyo cassa ñāyo paññāya sudiṭṭho hoti suppaṭividdho",
         "&ldquo;has clearly seen and penetrated the noble system "
         "with wisdom&rdquo; &mdash; the third condition, identified "
         "later in the discourse as dependent origination itself."),
        ("khīṇanirayomhi&hellip; sotāpannohamasmi avinipātadhammo "
         "niyato sambodhiparāyano",
         "&ldquo;I've finished with rebirth in hell&hellip; I am a "
         "stream-enterer! I'm not liable to be reborn in the "
         "underworld, and am assured, destined for awakening&rdquo; "
         "&mdash; the declaration itself, given identically at the "
         "discourse's start and close."),
        ("ariyakantehi sīlehi samannāgato hoti",
         "&ldquo;ethical conduct is loved by the noble ones&rdquo; "
         "&mdash; the fourth factor, turning from confidence in "
         "others to one's own practice."),
    ],
    text_intro=(
        "The discourse in full, opening Gahapativagga. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.41:1.1-1.2"),
        ("p", "&sect;2", "sn12.41:2.1-2.2"),
        ("p", "&sect;3", "sn12.41:3.1-3.2"),
        ("p", "&sect;4", "sn12.41:4.1-4.1"),
        ("p", "&sect;5", "sn12.41:5.1-5.1"),
        ("p", "&sect;6", "sn12.41:6.1-6.1"),
        ("p", "&sect;7", "sn12.41:7.1-7.2"),
        ("p", "&sect;8", "sn12.41:8.1-8.3"),
        ("p", "&sect;9", "sn12.41:9.1-9.2"),
        ("p", "&sect;10", "sn12.41:10.1-10.2"),
        ("p", "&sect;11", "sn12.41:11.1-11.2"),
        ("p", "&sect;12", "sn12.41:12.1-12.11"),
        ("p", "&sect;13", "sn12.41:13.1-13.2"),
    ],
    quiz=[
        {"q": "Who does the Buddha address this teaching to?",
         "opts": [
             "The householder Anāthapiṇḍika",
             "Venerable Sāriputta",
             "A group of unnamed mendicants",
             "King Pasenadi"],
         "correct": 0,
         "expl": "The donor of Jeta's Grove, encountered elsewhere in this collection too."},
        {"q": "How is the self-declaration of stream-entry framed?",
         "opts": [
             "As something a disciple may declare of themselves, if they wish",
             "As a formal title only the Buddha can confer",
             "As a status the Saṅgha must vote on",
             "As something that can never be known until after death"],
         "correct": 0,
         "expl": "Self-knowledge available to be checked, not an external verdict."},
        {"q": "What produces each of the five fears the discourse describes?",
         "opts": [
             "Breaking one of the five precepts",
             "Meditating incorrectly",
             "Disagreeing with the Buddha's teaching",
             "Failing to make offerings to the Saṅgha"],
         "correct": 0,
         "expl": "An identical causal pattern repeated once per precept."},
        {"q": "What are three of the four factors of stream-entry?",
         "opts": [
             "Confidence in the Buddha, the teaching, and the Saṅgha",
             "Wealth, status, and family lineage",
             "Meditative absorption, insight, and equanimity",
             "Generosity, patience, and courage"],
         "correct": 0,
         "expl": "Experiential confidence in the three refuges."},
        {"q": "What is the fourth factor of stream-entry, beyond confidence in the three refuges?",
         "opts": [
             "One's own ethical conduct, loved by the noble ones",
             "A vow of silence",
             "A specific meditative attainment",
             "Ordination as a monk or nun"],
         "correct": 0,
         "expl": "A turn from confidence in others to one's own practice."},
        {"q": "What is identified as the \"noble system\" seen and penetrated with wisdom?",
         "opts": [
             "Dependent origination itself, applied forward and in reverse",
             "The rules of monastic discipline",
             "The geography of the thirty-one realms",
             "A specific set of precepts unique to householders"],
         "correct": 0,
         "expl": "The third of the three conditions, given its full technical content."},
        {"q": "How does the discourse's opening and closing declaration compare?",
         "opts": [
             "They are given in identical wording, framing the three-part unpacking",
             "The closing declaration contradicts the opening one",
             "Only the opening includes the declaration; the closing omits it",
             "The two declarations use entirely different language"],
         "correct": 0,
         "expl": "A stable, symmetrical frame around the discourse's central unpacking."},
        {"q": "What does the noble disciple declare they are finished with, in this formula?",
         "opts": [
             "Rebirth in hell, the animal realm, and the ghost realm",
             "All future physical illness",
             "The need for further meditation",
             "Contact with other human beings"],
         "correct": 0,
         "expl": "The lower realms specifically, not all further experience."},
        {"q": "What language does this discourse share with SN 12.37 for how the disciple approaches dependent origination?",
         "opts": [
             "\"Applies the mind carefully and rationally\" to dependent origination itself",
             "\"Argues forcefully\" for dependent origination",
             "\"Doubts and questions\" dependent origination",
             "No shared language; the two discourses are unrelated"],
         "correct": 0,
         "expl": "The same phrase used for the learned noble disciple's approach in SN 12.37."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A test, not a feeling", [
            "three conditions, independently checked &mdash;",
            "not a mood of confidence alone",
        ]),
        ("Five fears, one mechanism", [
            "each precept broken, its own dread &mdash;",
            "quelled the moment it's kept",
        ]),
        ("Confidence outward, conduct inward", [
            "three factors turned toward others &mdash;",
            "the fourth turned back on oneself",
        ]),
        ("A declaration, framed twice", [
            "opening and closing in the same words &mdash;",
            "the unpacking held inside",
        ]),
    ],
    further=[
        '<a href="%s/sn12.41/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.40.html">SN 12.40 &middot; Intention (3rd)</a> '
        "&mdash; the discourse closing Kaḷārakhattiyavagga, "
        "immediately before this one.",
        '<a href="sn-10.8.html">SN 10.8 &middot; With Sudatta</a> '
        "&mdash; Anāthapiṇḍika's first meeting with the Buddha, "
        "under his birth name.",
        '<a href="sn-12.42.html">SN 12.42 &middot; Fears and Enmities (2nd)</a> '
        "&mdash; the next discourse, the same teaching addressed "
        "directly to the assembled mendicants.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.42 — Dutiyapañcaverabhayasutta
# --------------------------------------------------------------------------- #
page(
    12, 42, "Dutiyapañcaverabhaya", "Fears and Enmities (2nd)",
    meta_title="SN 12.42 — Fears and Enmities (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyapañcaverabhayasutta — the same three-part "
        "self-test for stream-entry as SN 12.41, addressed directly "
        "to the assembled mendicants and compressed throughout but "
        "for one factor left spelled out in full. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same three-part self-test as SN 12.41, "
                 "compressed with elision throughout except for one "
                 "factor left fully spelled out"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as SN 12.41, in compressed "
                       "form"),
    ],
    why=(
        "This discourse carries the identical three-part self-test "
        "as SN 12.41 &mdash; five fears quelled, four factors "
        "possessed, the noble system of dependent origination seen "
        "with wisdom &mdash; but delivered directly to the assembled "
        "mendicants rather than to the householder Anāthapiṇḍika, "
        "and compressed with elision through nearly every part. What "
        "makes the compression worth noticing closely is what it "
        "doesn't touch: of the four factors of stream-entry, three "
        "are elided down to a single word each, while the fourth "
        "&mdash; ethical conduct loved by the noble ones &mdash; is "
        "left standing in full, exactly as SN 12.41 gave it. Reading "
        "the two discourses side by side turns this asymmetry into a "
        "small but genuine question about what the redactors judged "
        "worth spelling out even in a compressed retelling."),
    guide=[
        ("The same three-part test, addressed differently", [
            "Every substantive element of SN 12.41 reappears here "
            "&mdash; the five fears, the four factors, the noble "
            "system, the opening and closing declaration &mdash; but "
            "the audience shifts from a single householder to the "
            "assembled mendicants as a group."]),
        ("Compression that isn't uniform", [
            "The five fears, three of the four factors, and the "
            "unpacking of the noble system are all elided down to "
            "a word or phrase followed by an ellipsis, but one "
            "factor &mdash; ethical conduct loved by the noble ones "
            "&mdash; is left standing in full, unelided."]),
        ("One phrase given full technical weight even here", [
            "Despite the heavy compression elsewhere, the discourse "
            "still spells out in full that a noble disciple "
            "\"carefully and rationally applies the mind to "
            "dependent origination itself,\" the same phrase used in "
            "SN 12.37 and SN 12.41, suggesting this particular "
            "formula was treated as too load-bearing to abbreviate."]),
        ("A declaration carried over word for word", [
            "Despite the compression everywhere else, the opening "
            "and closing declaration of stream-entry itself is given "
            "in the same full wording as SN 12.41, unelided even "
            "though it's the longest single formula in the "
            "discourse."]),
        ("A pairing that shows compression is selective, not uniform", [
            "Set beside SN 12.41, this discourse demonstrates that "
            "compressing a teaching for a general audience doesn't "
            "mean compressing everything equally; some formulas are "
            "judged essential enough to survive intact while others "
            "are trusted to elision."]),
    ],
    terms=[
        ("ariyasāvakassa pañca bhayāni verāni vūpasantāni honti",
         "&ldquo;a noble disciple has quelled five fears and "
         "enmities&rdquo; &mdash; the first condition, stated once "
         "before being elided through its five precepts."),
        ("catūhi ca sotāpattiyaṅgehi samannāgato hoti",
         "&ldquo;possesses the four factors of stream-entry&rdquo; "
         "&mdash; the same phrase used in SN 12.41."),
        ("ariyakantehi sīlehi samannāgato hoti",
         "&ldquo;ethical conduct is loved by the noble ones&rdquo; "
         "&mdash; the one factor left unelided even in this "
         "otherwise compressed retelling."),
        ("paṭiccasamuppādaññeva sādhukaṁ yoniso manasi karoti",
         "&ldquo;carefully and rationally applies the mind to "
         "dependent origination itself&rdquo; &mdash; the same "
         "phrase used in SN 12.37 and SN 12.41, also left unelided."),
        ("khīṇanirayomhi&hellip; avinipātadhammo niyato "
         "sambodhiparāyano",
         "&ldquo;I've finished with rebirth in hell&hellip; assured, "
         "destined for awakening&rdquo; &mdash; the declaration "
         "itself, carried over in full despite the compression "
         "elsewhere."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.42:1.1-1.3"),
        ("p", "&sect;2", "sn12.42:2.1-2.7"),
        ("p", "&sect;3", "sn12.42:3.1-3.6"),
        ("p", "&sect;4", "sn12.42:4.1-4.3"),
        ("p", "&sect;5", "sn12.42:5.1-5.2"),
    ],
    quiz=[
        {"q": "Who is this discourse addressed to, compared to SN 12.41?",
         "opts": [
             "The assembled mendicants, rather than a single householder",
             "King Pasenadi, rather than a group of mendicants",
             "Anāthapiṇḍika again, in a private setting",
             "A group of visiting brahmins"],
         "correct": 0,
         "expl": "A shift in audience from SN 12.41's householder to the monastic assembly."},
        {"q": "Which of the four factors of stream-entry is left unelided in this compressed retelling?",
         "opts": [
             "Ethical conduct loved by the noble ones",
             "Confidence in the Buddha",
             "Confidence in the teaching",
             "Confidence in the Saṅgha"],
         "correct": 0,
         "expl": "The one factor spelled out in full even here, unlike the other three."},
        {"q": "Is the compression in this discourse applied evenly across all its parts?",
         "opts": [
             "No — some formulas are elided while others are left standing in full",
             "Yes, every part is compressed to exactly the same degree",
             "No compression occurs anywhere in this discourse",
             "Only the declaration is compressed; everything else is spelled out"],
         "correct": 0,
         "expl": "A selective compression, not a uniform one."},
        {"q": "What phrase describing the noble disciple's approach to dependent origination survives uncompressed?",
         "opts": [
             "\"Carefully and rationally applies the mind to dependent origination itself\"",
             "\"Argues at length against dependent origination\"",
             "\"Memorizes dependent origination without understanding it\"",
             "No such phrase appears in this discourse"],
         "correct": 0,
         "expl": "The same load-bearing phrase used in SN 12.37 and SN 12.41."},
        {"q": "How does the opening and closing declaration of stream-entry compare to SN 12.41's?",
         "opts": [
             "Given in the same full wording, unelided despite the compression elsewhere",
             "Shortened to a single sentence fragment",
             "Omitted entirely from this discourse",
             "Rewritten with substantially different content"],
         "correct": 0,
         "expl": "The longest formula in the discourse, still carried over intact."},
        {"q": "What does comparing this discourse to SN 12.41 demonstrate about compression?",
         "opts": [
             "That compressing a teaching doesn't mean compressing every part of it equally",
             "That compressed versions always contain less doctrinal content overall",
             "That the two discourses actually teach contradictory doctrines",
             "That elision is applied completely at random with no discernible pattern"],
         "correct": 0,
         "expl": "Some formulas are judged too load-bearing to abbreviate."},
        {"q": "What are the five fears elided to in this discourse's telling?",
         "opts": [
             "A brief mention of killing followed by an ellipsis standing in for the other four",
             "A completely different list of five items",
             "Nothing; the five fears are omitted entirely",
             "Ten fears rather than five"],
         "correct": 0,
         "expl": "The same five precepts as SN 12.41, elided here rather than spelled out."},
        {"q": "What is identified as the noble system in this discourse, as in SN 12.41?",
         "opts": [
             "Dependent origination itself",
             "The rules of monastic discipline",
             "A set of precepts unique to this discourse",
             "The geography of the thirty-one realms"],
         "correct": 0,
         "expl": "The same third condition as SN 12.41, compressed here but not renamed."},
        {"q": "What is the relationship between this discourse and SN 12.41?",
         "opts": [
             "Identical substantive content, delivered to a different audience in more compressed form",
             "A direct refutation of SN 12.41",
             "An entirely unrelated teaching on a different topic",
             "An expansion introducing several new factors"],
         "correct": 0,
         "expl": "Same three-part test, different audience and selective compression."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting as SN 12.41, immediately before it."},
    ],
    marginalia=[
        ("The same test, a wider audience", [
            "no longer one householder alone &mdash;",
            "the whole assembly addressed",
        ]),
        ("Compression, but not evenly spread", [
            "three factors elided to a word &mdash;",
            "one left standing in full",
        ]),
        ("Too load-bearing to abbreviate", [
            "\"applies the mind\" to origination &mdash;",
            "spared the ellipsis given elsewhere",
        ]),
        ("A declaration, carried over intact", [
            "the longest formula, unelided &mdash;",
            "despite the shortening around it",
        ]),
    ],
    further=[
        '<a href="%s/sn12.42/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.41.html">SN 12.41 &middot; Fears and Enmities</a> '
        "&mdash; the discourse immediately before this one, giving "
        "the same teaching in full to Anāthapiṇḍika.",
        '<a href="sn-12.43.html">SN 12.43 &middot; Suffering</a> '
        "&mdash; the next discourse, turning from the three-part "
        "test to the six sense doors' role in suffering's origin.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.43 — Dukkhasutta
# --------------------------------------------------------------------------- #
page(
    12, 43, "Dukkha", "Suffering",
    meta_title="SN 12.43 — Suffering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dukkhasutta — the origin and disappearance of suffering "
        "traced not through the twelve familiar links but through "
        "each of the six sense doors, where consciousness, contact, "
        "feeling, and craving meet. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A formal announcement followed by the origin and "
                 "the disappearance of suffering, each run through "
                 "all six sense doors"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a compact reframing of familiar material "
                       "through a different entry point"),
    ],
    why=(
        "Rather than starting from ignorance and running the full "
        "twelve-link chain, this discourse enters dependent "
        "origination at a different point: the six sense doors. Eye "
        "consciousness arises dependent on the eye and sights, and "
        "the meeting of the three &mdash; sense faculty, sense "
        "object, consciousness &mdash; is contact, which conditions "
        "feeling, which conditions craving. This is the origin of "
        "suffering, run identically through all six doors, the eye "
        "and the mind alike. Where craving fades away and ceases "
        "with nothing left over, the discourse continues the chain "
        "downstream to its familiar full ending, closing on the "
        "cessation of the entire mass of suffering. The formal "
        "opening &mdash; \"listen and apply your mind well, I will "
        "speak\" &mdash; signals that what follows is meant to be "
        "received as a distinct teaching, not a passing remark."),
    guide=[
        ("A different entry point, not different content", [
            "This discourse doesn't abandon the twelve-link chain; "
            "it enters partway through, starting from the six sense "
            "doors' contact rather than from ignorance, and only "
            "resumes the chain's familiar full downstream sequence "
            "once craving's cessation is reached."]),
        ("The same three-way meeting, six times over", [
            "Eye consciousness dependent on the eye and sights, ear "
            "consciousness dependent on the ear and sounds, and so "
            "on through the mind and ideas &mdash; the identical "
            "structure of a sense faculty, its object, and "
            "consciousness meeting as contact, repeated for all six "
            "doors without variation."]),
        ("A formal announcement, not an offhand remark", [
            "The discourse opens with the Buddha explicitly "
            "announcing what he is about to teach and instructing "
            "the mendicants to listen and apply their minds well "
            "&mdash; a framing device marking this teaching as "
            "formally significant rather than incidental."]),
        ("Arising stated more briefly than cessation", [
            "The arising half of the teaching stops right after "
            "craving, closing with a simple \"this is the origin of "
            "suffering,\" while the cessation half continues the "
            "chain all the way down through grasping, continued "
            "existence, rebirth, and old age and death, giving the "
            "reversal noticeably fuller treatment than the arising."]),
        ("Suffering as this discourse's chosen name for the process", [
            "Naming the whole process \"the origin and disappearance "
            "of suffering\" rather than simply describing dependent "
            "origination in neutral terms makes explicit what the "
            "chain of conditions actually amounts to at the sense "
            "doors, in each moment of contact."]),
    ],
    terms=[
        ("dukkhassa&hellip; samudayañca atthaṅgamañca desessāmi",
         "&ldquo;I will teach you the origin and disappearance of "
         "suffering&rdquo; &mdash; the discourse's formal opening "
         "announcement."),
        ("cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṁ. "
         "Tiṇṇaṁ saṅgati phasso",
         "&ldquo;eye consciousness arises dependent on the eye and "
         "sights. The meeting of the three is contact&rdquo; &mdash; "
         "the formula repeated for all six sense doors."),
        ("phassapaccayā vedanā; vedanāpaccayā taṇhā",
         "&ldquo;contact is a requirement for feeling. Feeling is a "
         "requirement for craving&rdquo; &mdash; where the arising "
         "half of the teaching stops before resuming the familiar "
         "chain."),
        ("tassāyeva taṇhāya asesavirāganirodhā upādānanirodho",
         "&ldquo;when that craving fades away and ceases with no "
         "residue left behind, grasping ceases&rdquo; &mdash; the "
         "point where the cessation half rejoins the familiar "
         "downstream chain."),
        ("dukkhassa samudayo&hellip; dukkhassa atthaṅgamo",
         "&ldquo;the origin of suffering&hellip; the disappearance "
         "of suffering&rdquo; &mdash; the discourse's own name for "
         "the two halves of its teaching."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.43:1.1-1.5"),
        ("p", "&sect;2", "sn12.43:2.1-2.5"),
        ("p", "&sect;3", "sn12.43:3.1-3.8"),
        ("p", "&sect;4", "sn12.43:4.1-4.10"),
        ("p", "&sect;5", "sn12.43:5.1-5.13"),
    ],
    quiz=[
        {"q": "Where does this discourse enter dependent origination, unlike the familiar twelve-link version?",
         "opts": [
             "At the six sense doors, where a sense faculty, its object, and consciousness meet as contact",
             "At the very end, with old age and death alone",
             "It doesn't use dependent origination at all",
             "At rebirth, skipping everything before it"],
         "correct": 0,
         "expl": "A different entry point into the same underlying process."},
        {"q": "How many sense doors does this formula run through?",
         "opts": [
             "All six — eye, ear, nose, tongue, body, and mind",
             "Only the eye",
             "Only the mind",
             "Five, excluding the mind"],
         "correct": 0,
         "expl": "The identical structure repeated without variation across all six doors."},
        {"q": "How does the Buddha open this discourse?",
         "opts": [
             "With a formal announcement instructing the mendicants to listen and apply their minds well",
             "By answering a question just asked by a mendicant",
             "With a verse quoted from an older text",
             "In response to a visiting brahmin's challenge"],
         "correct": 0,
         "expl": "A framing device marking the teaching as formally significant."},
        {"q": "Where does the arising half of the teaching stop?",
         "opts": [
             "Right after craving, closing simply with \"this is the origin of suffering\"",
             "It continues all the way through to old age and death",
             "It stops before feeling is even mentioned",
             "It doesn't describe arising at all, only cessation"],
         "correct": 0,
         "expl": "A briefer treatment than the cessation half receives."},
        {"q": "Where does the cessation half of the teaching continue to, unlike the arising half?",
         "opts": [
             "All the way down through grasping, continued existence, rebirth, and old age and death",
             "It stops at the same point as the arising half",
             "It stops even earlier than the arising half",
             "It skips directly to old age and death with nothing in between"],
         "correct": 0,
         "expl": "A fuller treatment of the reversal than of the arising."},
        {"q": "What does the discourse call the whole process it describes?",
         "opts": [
             "\"The origin and disappearance of suffering\"",
             "\"The nature of consciousness\"",
             "\"The path to awakening\"",
             "\"The rules of monastic discipline\""],
         "correct": 0,
         "expl": "Naming what the chain of conditions amounts to at the sense doors."},
        {"q": "What three things meet to produce contact, according to this discourse?",
         "opts": [
             "A sense faculty, its object, and consciousness",
             "The Buddha, the teaching, and the Saṅgha",
             "Ignorance, choices, and craving",
             "Birth, aging, and death"],
         "correct": 0,
         "expl": "The recurring three-way meeting repeated at each of the six doors."},
        {"q": "Is the six-sense-door structure in this discourse a departure from the twelve-link chain, or a variation of it?",
         "opts": [
             "A variation — the same underlying process, entered at a different point",
             "A complete departure with no relationship to the twelve-link chain",
             "An entirely separate teaching unrelated to dependent origination",
             "A contradiction of the twelve-link chain's content"],
         "correct": 0,
         "expl": "The chain's familiar downstream sequence resumes once craving's cessation is reached."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
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
        ("A different door into the same house", [
            "not ignorance first, but the senses &mdash;",
            "contact where faculty meets object",
        ]),
        ("Six doors, one formula", [
            "eye, ear, nose, tongue, body, mind &mdash;",
            "the same meeting, six times over",
        ]),
        ("Arising brief, cessation full", [
            "one stops at craving &mdash;",
            "the other runs the whole chain down",
        ]),
        ("Suffering, named at the senses", [
            "not abstract origination &mdash;",
            "traced to each moment of contact",
        ]),
    ],
    further=[
        '<a href="%s/sn12.43/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.42.html">SN 12.42 &middot; Fears and Enmities (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.44.html">SN 12.44 &middot; The World</a> '
        "&mdash; the next discourse, the identical sense-door "
        "teaching under a different name.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.44 — Lokasutta
# --------------------------------------------------------------------------- #
page(
    12, 44, "Loka", "The World",
    meta_title="SN 12.44 — The World | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Lokasutta — the same six-sense-door teaching as SN "
        "12.43, renamed \"the world\" rather than \"suffering,\" "
        "with the arising direction spelled out in full where its "
        "twin elides it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same formal announcement and six-sense-door "
                 "structure as SN 12.43, with the arising direction "
                 "given in fuller, less elided detail"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the same content as SN 12.43, under a "
                       "different name"),
    ],
    why=(
        "This discourse teaches exactly the same content as SN "
        "12.43 &mdash; the same six sense doors, the same three-way "
        "meeting as contact, the same downstream chain to feeling "
        "and craving and beyond &mdash; but calls the whole process "
        "\"the world\" rather than \"suffering.\" The substitution is "
        "not decorative. By using the identical formula to name both "
        "\"the origin and disappearance of suffering\" and \"the "
        "origin and disappearance of the world,\" the two twin "
        "discourses together make an equation explicit: in this "
        "teaching's technical sense, the world just is the process "
        "by which suffering arises and ceases at the six sense "
        "doors, not a container that suffering happens to occur "
        "inside. This same equation of the world with the sense "
        "doors' activity resurfaces at the very end of this chapter, "
        "in SN 12.49 and SN 12.50's closing declaration that a noble "
        "disciple understands how \"this world\" originates and "
        "ceases."),
    guide=[
        ("The same formula, a different name for the process", [
            "Every structural element of SN 12.43 reappears here "
            "unchanged &mdash; the six sense doors, the three-way "
            "meeting as contact, the downstream chain &mdash; with "
            "only the word naming the whole process changed from "
            "\"suffering\" to \"the world.\""]),
        ("An equation, not a coincidence of vocabulary", [
            "Because the same underlying process is called both "
            "\"the origin and disappearance of suffering\" in SN "
            "12.43 and \"the origin and disappearance of the world\" "
            "here, the pairing amounts to a direct equation: the "
            "world, in this technical sense, is exactly this "
            "process at the six sense doors."]),
        ("Arising spelled out where SN 12.43 elided it", [
            "Where SN 12.43's arising half stopped right after "
            "craving with a peyyāla ellipsis, this discourse spells "
            "out the full downstream chain &mdash; grasping, "
            "continued existence, rebirth, old age and death &mdash; "
            "for the arising direction as well, giving both "
            "directions equally full treatment rather than favoring "
            "cessation."]),
        ("A phrase that returns at the vagga's close", [
            "The exact language of \"this world originates\" and "
            "\"this world ceases\" used here reappears at the very "
            "end of this chapter, in SN 12.49 and SN 12.50's closing "
            "declaration about the noble disciple's understanding "
            "&mdash; a deliberate thread running through the whole "
            "vagga, not an isolated formula."]),
        ("Two names, one teaching, told twice", [
            "Reading SN 12.43 and this discourse together shows a "
            "single teaching given under two names rather than two "
            "separate teachings, inviting the reader to treat "
            "\"suffering\" and \"the world\" as interchangeable terms "
            "for the same conditioned process."]),
    ],
    terms=[
        ("lokassa&hellip; samudayañca atthaṅgamañca desessāmi",
         "&ldquo;I will teach you the origin and disappearance of "
         "the world&rdquo; &mdash; the same formal opening as SN "
         "12.43, with &ldquo;the world&rdquo; in place of "
         "&ldquo;suffering.&rdquo;"),
        ("cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṁ. "
         "Tiṇṇaṁ saṅgati phasso",
         "&ldquo;eye consciousness arises dependent on the eye and "
         "sights. The meeting of the three is contact&rdquo; &mdash; "
         "the identical formula shared with SN 12.43."),
        ("vedanāpaccayā taṇhā; taṇhāpaccayā upādānaṁ; "
         "upādānapaccayā bhavo; bhavapaccayā jāti; "
         "jātipaccayā jarāmaraṇaṁ",
         "&ldquo;feeling is a requirement for craving. Craving is a "
         "requirement for grasping. Grasping is a requirement for "
         "continued existence. Continued existence is a requirement "
         "for rebirth. Rebirth is a requirement for old age and "
         "death&rdquo; &mdash; the full downstream chain given here "
         "for arising, where SN 12.43 elided it."),
        ("tassāyeva taṇhāya asesavirāganirodhā upādānanirodho",
         "&ldquo;when that craving fades away and ceases with no "
         "residue left behind, grasping ceases&rdquo; &mdash; the "
         "same cessation formula shared with SN 12.43."),
        ("lokassa samudayo&hellip; lokassa atthaṅgamo",
         "&ldquo;the origin of the world&hellip; the ending of the "
         "world&rdquo; &mdash; this discourse's name for what SN "
         "12.43 calls the origin and disappearance of suffering."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.44:1.1-1.5"),
        ("p", "&sect;2", "sn12.44:2.1-2.9"),
        ("p", "&sect;3", "sn12.44:3.1-3.8"),
        ("p", "&sect;4", "sn12.44:4.1-4.8"),
        ("p", "&sect;5", "sn12.44:5.1-5.11"),
    ],
    quiz=[
        {"q": "How does this discourse's teaching compare structurally to SN 12.43's?",
         "opts": [
             "Identical structure — the same six sense doors and formula, under a different name",
             "A completely different teaching with no shared structure",
             "The reverse of SN 12.43's teaching",
             "A much shorter summary with most content omitted"],
         "correct": 0,
         "expl": "The same underlying process, named differently."},
        {"q": "What does this discourse call the process that SN 12.43 calls \"suffering\"?",
         "opts": [
             "\"The world\"",
             "\"Consciousness\"",
             "\"The path\"",
             "\"Liberation\""],
         "correct": 0,
         "expl": "A direct substitution of terms for the identical underlying process."},
        {"q": "What does pairing SN 12.43 and this discourse together amount to?",
         "opts": [
             "An equation — the world, in this technical sense, is the process of suffering's arising and ceasing",
             "A contradiction between two incompatible teachings",
             "Proof that one of the two discourses must be a later addition",
             "Nothing significant; the naming difference is purely decorative"],
         "correct": 0,
         "expl": "Suffering and the world named as the same conditioned process."},
        {"q": "How does this discourse's treatment of the arising direction compare to SN 12.43's?",
         "opts": [
             "Spelled out in full through grasping, continued existence, rebirth, and old age and death",
             "Even more heavily elided than SN 12.43's",
             "Omitted entirely",
             "Identical in every detail, including the elision"],
         "correct": 0,
         "expl": "Fuller treatment of arising than SN 12.43 gives it."},
        {"q": "Where does the exact phrase \"this world originates\" and \"this world ceases\" reappear later in this chapter?",
         "opts": [
             "In SN 12.49 and SN 12.50's closing declaration about the noble disciple's understanding",
             "It appears nowhere else in this saṃyutta",
             "Only in SN 12.41's declaration of stream-entry",
             "In SN 12.31's opening verse"],
         "correct": 0,
         "expl": "A deliberate thread connecting this discourse to the vagga's close."},
        {"q": "What three things meet to produce contact, according to this discourse?",
         "opts": [
             "A sense faculty, its object, and consciousness",
             "The Buddha, the teaching, and the Saṅgha",
             "Ignorance, choices, and craving",
             "Birth, aging, and death"],
         "correct": 0,
         "expl": "The same three-way meeting used in SN 12.43."},
        {"q": "How many sense doors does this discourse's formula cover?",
         "opts": [
             "All six — eye, ear, nose, tongue, body, and mind",
             "Only the eye and the mind",
             "Five, excluding the mind",
             "Only the mind"],
         "correct": 0,
         "expl": "The same full six-door coverage as SN 12.43."},
        {"q": "How does the Buddha open this discourse?",
         "opts": [
             "With a formal announcement instructing the mendicants to listen and apply their minds well",
             "By answering a question just asked by a mendicant",
             "In response to a visiting brahmin's challenge",
             "With a verse quoted from an older text"],
         "correct": 0,
         "expl": "The same formal framing device used in SN 12.43."},
        {"q": "Is this discourse best read as an unrelated teaching, or a twin of SN 12.43?",
         "opts": [
             "A twin — the same teaching told under a different name",
             "An unrelated teaching sharing no content with SN 12.43",
             "A refutation of SN 12.43",
             "An earlier draft later replaced by SN 12.43"],
         "correct": 0,
         "expl": "A single teaching given twice under two different names."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting as SN 12.43, immediately before it."},
    ],
    marginalia=[
        ("The same formula, a new name", [
            "not suffering, but \"the world\" &mdash;",
            "the identical process, retitled",
        ]),
        ("An equation, quietly stated", [
            "world and suffering, one process &mdash;",
            "paired discourses making it explicit",
        ]),
        ("Arising given its full due", [
            "spelled out where SN 12.43 elided &mdash;",
            "both directions treated equally",
        ]),
        ("A phrase planted for later", [
            "\"this world originates, this world ceases\" &mdash;",
            "echoed again at the chapter's close",
        ]),
    ],
    further=[
        '<a href="%s/sn12.44/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.43.html">SN 12.43 &middot; Suffering</a> '
        "&mdash; the discourse immediately before this one, the same "
        "teaching under its other name.",
        '<a href="sn-12.49.html">SN 12.49 &middot; A Noble Disciple</a> '
        "&mdash; later in this chapter, where the phrase &ldquo;this "
        "world originates&hellip; this world ceases&rdquo; returns "
        "in the closing declaration.",
        '<a href="sn-12.45.html">SN 12.45 &middot; At Ñātika</a> '
        "&mdash; the next discourse, the same six-door teaching "
        "overheard by chance during the Buddha's private retreat.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.45 — Ñātikasutta
# --------------------------------------------------------------------------- #
page(
    12, 45, "Ñātika", "At Ñātika",
    meta_title="SN 12.45 — At Ñātika | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ñātikasutta — the same six-sense-door teaching as SN "
        "12.43 and SN 12.44, spoken alone during private retreat and "
        "preserved only because a mendicant happened to be "
        "eavesdropping. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Ñātika, in the brick house"),
        ("Speakers", "The Buddha, speaking alone during private "
                     "retreat, and an unnamed mendicant who "
                     "overhears him"),
        ("Form", "A solitary exposition of the teaching, followed "
                 "by a brief exchange once the Buddha notices he has "
                 "been overheard"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "familiar content, with an unusual frame "
                       "worth noticing"),
    ],
    why=(
        "This discourse gives the same six-sense-door teaching as SN "
        "12.43 and SN 12.44, but under a narrative frame unlike "
        "anything else in this chapter: the Buddha isn't addressing "
        "an audience at all. He's alone in private retreat at "
        "Ñātika, and simply speaks the exposition aloud to himself. "
        "It survives in the record only because a certain mendicant "
        "happens to be standing within earshot. When the Buddha "
        "notices him, rather than treating the moment as an "
        "intrusion, he asks whether the mendicant heard it, and on "
        "confirming that he did, instructs him directly to learn it, "
        "memorize it, and remember it, calling it beneficial and "
        "relevant to the fundamentals of the spiritual life. The "
        "frame quietly raises a question the discourse itself never "
        "addresses: how many teachings like this one exist only "
        "because someone happened to be listening at the right "
        "moment?"),
    guide=[
        ("Spoken to no one, at first", [
            "Unlike every other discourse in this chapter, this "
            "teaching doesn't open with anyone approaching the "
            "Buddha or asking a question; he is alone in retreat and "
            "simply speaks the exposition aloud, with no addressee "
            "named at all."]),
        ("The same six-door formula, given a third time", [
            "The content itself is identical in structure to SN "
            "12.43 and SN 12.44 &mdash; the same six sense doors, "
            "the same three-way meeting as contact, the same "
            "downstream chain to feeling, craving, and beyond "
            "&mdash; making this the third telling of the same "
            "underlying teaching in three consecutive discourses."]),
        ("Overheard, not delivered", [
            "The mendicant who receives this teaching does so purely "
            "by chance, standing within earshot rather than having "
            "sought the teaching out or been summoned to hear it, "
            "which the discourse frames neutrally rather than as "
            "either an accident to apologize for or a deliberate "
            "test."]),
        ("A triple instruction, not simple approval", [
            "Once the Buddha confirms the mendicant heard the "
            "exposition, he doesn't merely commend him; he gives "
            "three distinct imperatives in sequence &mdash; learn "
            "it, memorize it, remember it &mdash; treating what was "
            "overheard as something now formally worth deliberate "
            "retention."]),
        ("A teaching's survival made visible", [
            "By explaining how this particular teaching came to be "
            "recorded at all, the discourse's frame quietly shows "
            "the mechanism by which an oral tradition preserves "
            "material never originally addressed to anyone &mdash; a "
            "detail more discourses in this collection likely share "
            "without stating it so plainly."]),
    ],
    terms=[
        ("ñātike viharati giñjakāvasathe",
         "&ldquo;was staying at Ñātika in the brick house&rdquo; "
         "&mdash; the discourse's setting, distinct from the usual "
         "Sāvatthī."),
        ("rahogato paṭisallāno imaṁ dhammapariyāyaṁ abhāsi",
         "&ldquo;while in private retreat he spoke this exposition "
         "of the teaching&rdquo; &mdash; spoken alone, with no "
         "addressee named."),
        ("upassuti ṭhito",
         "&ldquo;standing listening in&rdquo; &mdash; how the "
         "discourse describes the mendicant who happens to overhear "
         "the Buddha."),
        ("uggaṇhāhi&hellip; pariyāpuṇāhi&hellip; dhārehi",
         "&ldquo;learn&hellip; memorize&hellip; and remember&rdquo; "
         "&mdash; the three imperatives the Buddha gives once he "
         "confirms the mendicant heard the teaching."),
        ("atthasaṁhito&hellip; dhammapariyāyo ādibrahmacariyako",
         "&ldquo;this exposition of the teaching is beneficial and "
         "relevant to the fundamentals of the spiritual life&rdquo; "
         "&mdash; the Buddha's own reason for the instruction to "
         "retain it."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.45:1.1-1.3"),
        ("p", "&sect;2", "sn12.45:2.1-2.5"),
        ("p", "&sect;3", "sn12.45:3.1-3.9"),
        ("p", "&sect;4", "sn12.45:4.1-4.6"),
        ("p", "&sect;5", "sn12.45:5.1-5.7"),
        ("p", "&sect;6", "sn12.45:6.1-6.9"),
    ],
    quiz=[
        {"q": "Where is the Buddha, and what is he doing, at the start of this discourse?",
         "opts": [
             "Alone at Ñātika, in private retreat, speaking the exposition aloud with no addressee",
             "Teaching a large assembly at Sāvatthī",
             "Answering a question from Anāthapiṇḍika",
             "Debating a visiting brahmin"],
         "correct": 0,
         "expl": "An unusual frame — no audience is present when the teaching is first spoken."},
        {"q": "How does this discourse's core teaching compare to SN 12.43 and SN 12.44?",
         "opts": [
             "The same six-sense-door structure, told a third time",
             "An entirely different, unrelated teaching",
             "A direct contradiction of the earlier two discourses",
             "A much shorter fragment with most content missing"],
         "correct": 0,
         "expl": "The third consecutive telling of the same underlying teaching."},
        {"q": "How does the mendicant come to hear this teaching?",
         "opts": [
             "By chance, standing within earshot while the Buddha spoke alone",
             "He was formally summoned to receive it",
             "He asked the Buddha directly for this teaching",
             "He read it from a written text"],
         "correct": 0,
         "expl": "Overheard, not deliberately delivered to him."},
        {"q": "How does the Buddha react upon noticing the mendicant overheard him?",
         "opts": [
             "He asks whether the mendicant heard it, then instructs him to learn, memorize, and remember it",
             "He scolds the mendicant for eavesdropping",
             "He ignores the mendicant entirely",
             "He asks the mendicant to repeat it back immediately word for word"],
         "correct": 0,
         "expl": "Treated neutrally, then turned into a formal instruction to retain the teaching."},
        {"q": "What three imperatives does the Buddha give the mendicant?",
         "opts": [
             "Learn it, memorize it, and remember it",
             "Ignore it, forget it, and move on",
             "Teach it, debate it, and refute it",
             "Translate it, copy it, and distribute it"],
         "correct": 0,
         "expl": "Three distinct instructions, not a single word of approval."},
        {"q": "Why does the Buddha say this teaching should be retained?",
         "opts": [
             "It's beneficial and relevant to the fundamentals of the spiritual life",
             "It's required for admission to the Saṅgha",
             "It's the only teaching the Buddha gave that year",
             "The text gives no reason at all"],
         "correct": 0,
         "expl": "The Buddha's own stated justification for the instruction."},
        {"q": "What does this discourse's frame quietly illustrate?",
         "opts": [
             "How a teaching not addressed to anyone could still come to be recorded and preserved",
             "That private teachings are always kept secret from the wider Saṅgha",
             "That the Buddha never taught anything while alone",
             "That eavesdropping was formally forbidden among mendicants"],
         "correct": 0,
         "expl": "A visible mechanism behind an otherwise invisible process of oral preservation."},
        {"q": "Where is this discourse set, unlike most of this chapter's other discourses?",
         "opts": [
             "Ñātika, in the brick house",
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, at the Bamboo Grove",
             "Kapilavatthu, the Buddha's home city"],
         "correct": 0,
         "expl": "A distinct setting from the usual Sāvatthī of this chapter."},
        {"q": "What three things meet to produce contact, in this discourse's formula?",
         "opts": [
             "A sense faculty, its object, and consciousness",
             "The Buddha, the teaching, and the Saṅgha",
             "Ignorance, choices, and craving",
             "Birth, aging, and death"],
         "correct": 0,
         "expl": "The same three-way meeting used in SN 12.43 and SN 12.44."},
        {"q": "Is the mendicant in this discourse named?",
         "opts": [
             "No — he is described only as \"a certain mendicant\"",
             "Yes, he is identified as Venerable Ānanda",
             "Yes, he is identified as Venerable Sāriputta",
             "Yes, he is identified as Kaḷāra the Aristocrat"],
         "correct": 0,
         "expl": "No name is given for the mendicant who overhears the teaching."},
    ],
    marginalia=[
        ("Spoken to no one at first", [
            "alone in retreat, aloud &mdash;",
            "no audience named or summoned",
        ]),
        ("Overheard, not delivered", [
            "a mendicant standing within earshot &mdash;",
            "chance, not design",
        ]),
        ("Three imperatives, not one word of praise", [
            "learn it, memorize it, remember it &mdash;",
            "retention made a formal instruction",
        ]),
        ("How a teaching survives by chance", [
            "preserved because someone was listening &mdash;",
            "the mechanism made visible, for once",
        ]),
    ],
    further=[
        '<a href="%s/sn12.45/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.44.html">SN 12.44 &middot; The World</a> '
        "&mdash; the discourse immediately before this one, the same "
        "teaching addressed to an assembly rather than overheard.",
        '<a href="sn-12.46.html">SN 12.46 &middot; A Certain Brahmin</a> '
        "&mdash; the next discourse, turning from the sense doors to "
        "a question about who acts and who experiences the result.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.46 — Aññatarabrāhmaṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 46, "Aññatarabrāhmaṇa", "A Certain Brahmin",
    meta_title="SN 12.46 — A Certain Brahmin | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aññatarabrāhmaṇasutta — a brahmin's question about "
        "whether the doer of a deed and the experiencer of its "
        "result are the same person or different meets the same "
        "middle-way formula already given for existence and "
        "identity elsewhere in this saṃyutta. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and an unnamed brahmin"),
        ("Form", "A brief two-question dialogue, each answer named "
                 "an extreme, followed by the middle way and a "
                 "closing conversion"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "brief, but its question reaches into how "
                       "kamma is understood to work across time"),
    ],
    why=(
        "A brahmin puts to the Buddha one of the oldest questions "
        "about how moral responsibility and rebirth fit together: is "
        "the one who performs a deed the very same person who later "
        "experiences its result, or is the doer one person and the "
        "experiencer another? Each answer, the Buddha says, is an "
        "extreme. Claiming strict identity risks the same trap "
        "already named for the soul and the body in SN 12.35 and SN "
        "12.36; claiming strict difference would make kamma's "
        "connection across a lifetime, or across rebirths, entirely "
        "arbitrary. Avoiding both, the Realized One teaches by the "
        "middle way &mdash; the same closing formula already used in "
        "SN 12.15 for existence and non-existence, and in SN 12.35 "
        "for the soul and the body &mdash; restating the question as "
        "a chain of conditions rather than a claim about identity."),
    guide=[
        ("A question about kamma phrased as identity", [
            "The brahmin's question isn't abstractly metaphysical; "
            "it's the practical puzzle of how an act performed by "
            "one person could have consequences for someone later in "
            "time, and whether that later person can meaningfully be "
            "called the same person at all."]),
        ("Two extremes, each rejected outright", [
            "Strict identity between doer and experiencer is named "
            "one extreme, and strict difference between them the "
            "second, with neither given as a preferred approximation "
            "of the truth &mdash; both are simply set aside."]),
        ("The same middle-way formula, a third confirmed use", [
            "\"Avoiding these two extremes, the Realized One teaches "
            "by the middle way\" is the identical closing formula "
            "already seen in SN 12.15, for existence and "
            "non-existence, and in SN 12.35, for the soul and the "
            "body &mdash; now applied to a third distinct pair of "
            "extremes, doer and experiencer."]),
        ("A chain of conditions replacing a claim about persons", [
            "Rather than settling whether doer and experiencer are "
            "the same or different, the Buddha's answer simply "
            "restates the twelve-link chain, treating the question "
            "of personal identity across time as one dissolved by "
            "conditionality rather than one requiring a direct "
            "answer."]),
        ("A conversion closing a brief, dense exchange", [
            "Despite its brevity, the discourse ends exactly as "
            "several other exchanges with visiting brahmins in this "
            "chapter do, with the questioner praising the teaching "
            "and declaring himself a lay follower gone for refuge "
            "for life."]),
    ],
    terms=[
        ("so karoti so paṭisaṁvedayati",
         "&ldquo;he who does the deed and he who experiences the "
         "result are one and the same&rdquo; &mdash; the first "
         "extreme, named and set aside."),
        ("añño karoti, añño paṭisaṁvedayati",
         "&ldquo;he who does the deed is one and he who experiences "
         "the result is another&rdquo; &mdash; the second extreme."),
        ("ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the same formula "
         "already used in SN 12.15 and SN 12.35, for two other pairs "
         "of extremes."),
        ("abhikkantaṁ, bho gotama",
         "&ldquo;excellent, worthy Gotama!&rdquo; &mdash; the "
         "brahmin's exclamation of praise closing the exchange."),
        ("upāsakaṁ maṁ bhavaṁ gotamo dhāretu&hellip; pāṇupetaṁ "
         "saraṇaṁ gataṁ",
         "&ldquo;may the worthy Gotama remember me as a lay follower "
         "who has gone for refuge for life&rdquo; &mdash; the "
         "formal declaration of conversion."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.46:1.1-1.3"),
        ("p", "&sect;2", "sn12.46:2.1-2.2"),
        ("p", "&sect;3", "sn12.46:3.1-3.9"),
        ("p", "&sect;4", "sn12.46:4.1-4.3"),
    ],
    quiz=[
        {"q": "What does the brahmin ask the Buddha?",
         "opts": [
             "Whether the one who does a deed and the one who experiences its result are the same person or different",
             "Whether the world is eternal or not eternal",
             "Whether the Buddha exists after death",
             "Whether all things exist or nothing exists"],
         "correct": 0,
         "expl": "A question about personal identity across the span of kamma's effect."},
        {"q": "How does the Buddha respond to \"the doer and the experiencer are the same\"?",
         "opts": [
             "He names it as one extreme",
             "He affirms it as correct",
             "He asks the brahmin to explain further before answering",
             "He refuses to comment on it"],
         "correct": 0,
         "expl": "Set aside as an extreme, not confirmed."},
        {"q": "How does the Buddha respond to \"the doer is one, the experiencer another\"?",
         "opts": [
             "He names it as the second extreme",
             "He affirms it as correct",
             "He says it's closer to the truth than the first claim",
             "He says the question makes no sense at all"],
         "correct": 0,
         "expl": "The second extreme, likewise set aside."},
        {"q": "What formula does the Buddha use to move past both extremes?",
         "opts": [
             "\"Avoiding these two extremes, the Realized One teaches by the middle way\"",
             "\"Neither claim can ever be settled\"",
             "\"Only a fully awakened Buddha could know the answer\"",
             "\"The question should not be asked at all\""],
         "correct": 0,
         "expl": "The same formula already used for other pairs of extremes in this saṃyutta."},
        {"q": "Where else in this saṃyutta does the identical middle-way formula appear?",
         "opts": [
             "SN 12.15, for existence and non-existence, and SN 12.35, for the soul and the body",
             "Nowhere else; this is the formula's only use",
             "Only in the discourses addressed to Anāthapiṇḍika",
             "Only in discourses involving King Pasenadi"],
         "correct": 0,
         "expl": "A formula now confirmed across three distinct pairs of extremes."},
        {"q": "What does the Buddha's answer replace the identity question with?",
         "opts": [
             "The twelve-link chain of dependent origination",
             "A direct ruling that the doer and experiencer are identical",
             "A direct ruling that they are entirely separate",
             "A refusal to answer the question in any form"],
         "correct": 0,
         "expl": "Conditionality offered in place of a verdict about personal identity."},
        {"q": "How does the discourse end?",
         "opts": [
             "The brahmin praises the teaching and declares himself a lay follower for life",
             "The brahmin walks away unconvinced",
             "The brahmin asks a further question that goes unanswered",
             "The discourse ends without any response from the brahmin"],
         "correct": 0,
         "expl": "A formal conversion, matching the pattern of several other brahmin exchanges in this chapter."},
        {"q": "Is the brahmin in this discourse named?",
         "opts": [
             "No — he is described only as \"a certain brahmin\"",
             "Yes, he is identified as Jāṇussoṇi",
             "Yes, he is identified as Kaḷāra the Aristocrat",
             "Yes, he is identified as Bhāradvāja"],
         "correct": 0,
         "expl": "Left unnamed, unlike the brahmin in the very next discourse."},
        {"q": "What practical concern underlies the brahmin's question, according to this reading guide?",
         "opts": [
             "How an act performed by one person could have consequences for someone later in time",
             "Whether brahmins are superior to other castes",
             "Whether meditation can be taught to laypeople",
             "Whether the Buddha permits alcohol in moderation"],
         "correct": 0,
         "expl": "A practical puzzle about kamma and continuity, not abstract wordplay."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A question about kamma's reach", [
            "same doer, same feeler of results &mdash;",
            "or two people entirely?",
        ]),
        ("Two extremes, both set aside", [
            "identity and difference alike &mdash;",
            "neither claim allowed to stand",
        ]),
        ("A formula heard a third time", [
            "the same middle way as SN 12.15, SN 12.35 &mdash;",
            "now applied to doer and deed",
        ]),
        ("Conditions in place of a verdict", [
            "not who, but what depends on what &mdash;",
            "the chain restated instead",
        ]),
    ],
    further=[
        '<a href="%s/sn12.46/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.45.html">SN 12.45 &middot; At Ñātika</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.35.html">SN 12.35 &middot; Ignorance is a Condition</a> '
        "&mdash; the earlier discourse using the same middle-way "
        "formula for the soul and the body.",
        '<a href="sn-12.47.html">SN 12.47 &middot; Jānussoṇi</a> '
        "&mdash; the next discourse, the same formula applied to a "
        "named brahmin's question about existence itself.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.47 — Jāṇussoṇisutta
# --------------------------------------------------------------------------- #
page(
    12, 47, "Jāṇussoṇi", "Jānussoṇi",
    meta_title="SN 12.47 — Jānussoṇi | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Jāṇussoṇisutta — the named brahmin Jānussoṇi asks "
        "whether everything exists or nothing exists, generalizing "
        "SN 12.15's question about the world into a question about "
        "all things, and receiving the identical middle way. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and the brahmin Jānussoṇi"),
        ("Form", "A brief two-question dialogue, structurally "
                 "identical to SN 12.46, closing in the same "
                 "conversion"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "brief, generalizing an existence question "
                       "already met elsewhere in this saṃyutta"),
    ],
    why=(
        "The brahmin Jānussoṇi &mdash; a named figure who appears "
        "questioning the Buddha in several discourses across the "
        "early texts &mdash; asks the broadest possible version of "
        "an existence question already met in this saṃyutta: not "
        "whether the world in particular exists or doesn't, as in SN "
        "12.15, but whether everything exists, or whether nothing "
        "does. The Buddha's answer follows exactly the same pattern "
        "as before: each claim is named an extreme and set aside, "
        "and the middle way is given not as a compromise between "
        "them but as the same twelve-link chain of conditions, run "
        "forward to suffering's arising and in reverse to its "
        "complete cessation. Reading this discourse against SN 12.15 "
        "shows how the same underlying teaching answers a question "
        "however broadly or narrowly it happens to be framed."),
    guide=[
        ("A generalized version of an already-answered question", [
            "Where SN 12.15 asked specifically about the existence "
            "or non-existence of the world, Jānussoṇi's question "
            "widens the scope to everything without restriction "
            "&mdash; \"does all exist\" rather than \"does the world "
            "exist\" &mdash; and receives an answer built on exactly "
            "the same structure."]),
        ("Two extremes named without qualification", [
            "\"All exists\" and \"all does not exist\" are each "
            "named an extreme in turn, with neither treated as a "
            "safer or more defensible default position than the "
            "other."]),
        ("The same middle way, a fourth confirmed use", [
            "\"Avoiding these two extremes, the Realized One teaches "
            "by the middle way\" appears here for a fourth time in "
            "this saṃyutta, following its use for the world's "
            "existence in SN 12.15, the soul and the body in SN "
            "12.35, and the doer and the experiencer in SN 12.46."]),
        ("A named, recurring questioner", [
            "Unlike the unnamed brahmin of SN 12.46, Jānussoṇi is "
            "identified by name &mdash; a brahmin who appears "
            "putting questions to the Buddha in several other "
            "discourses across the early texts, giving this "
            "particular exchange a slightly more documented "
            "questioner than most of this chapter's visitors."]),
        ("Breadth of question, sameness of answer", [
            "The discourse's real interest lies less in Jānussoṇi's "
            "particular question than in what it demonstrates: that "
            "however broadly an existence question is framed, "
            "sabbaṁ or loko alike, the teaching offered in response "
            "doesn't change in kind, only in the words used to state "
            "the question being set aside."]),
    ],
    terms=[
        ("jāṇussoṇi brāhmaṇo",
         "&ldquo;the brahmin Jānussoṇi&rdquo; &mdash; a named figure "
         "who appears questioning the Buddha in several discourses "
         "across the early texts."),
        ("sabbamatthi&hellip; sabbaṁ natthi",
         "&ldquo;all exists&hellip; all does not exist&rdquo; "
         "&mdash; the two extremes named in turn, a generalized "
         "version of SN 12.15's question about the world "
         "specifically."),
        ("ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the same formula "
         "confirmed for a fourth distinct pair of extremes in this "
         "saṃyutta."),
        ("abhikkantaṁ, bho gotama",
         "&ldquo;excellent, worthy Gotama!&rdquo; &mdash; Jānussoṇi's "
         "exclamation of praise, identical to the unnamed brahmin's "
         "in SN 12.46."),
        ("pāṇupetaṁ saraṇaṁ gataṁ",
         "&ldquo;gone for refuge for life&rdquo; &mdash; the closing "
         "formula of conversion, shared with SN 12.46."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.47:1.1-1.2"),
        ("p", "&sect;2", "sn12.47:2.1-2.2"),
        ("p", "&sect;3", "sn12.47:3.1-3.9"),
        ("p", "&sect;4", "sn12.47:4.1-4.3"),
    ],
    quiz=[
        {"q": "What does Jānussoṇi ask the Buddha?",
         "opts": [
             "Whether everything exists, or whether nothing exists",
             "Whether the doer and experiencer of a deed are the same person",
             "Whether the Buddha will be reborn",
             "Whether the world is finite or infinite in extent"],
         "correct": 0,
         "expl": "A generalized existence question, broader than SN 12.15's question about the world specifically."},
        {"q": "How does Jānussoṇi's question compare to SN 12.15's question about the world?",
         "opts": [
             "It generalizes SN 12.15's question from the world specifically to everything without restriction",
             "It is entirely unrelated to SN 12.15's question",
             "It narrows SN 12.15's question to a single sense faculty",
             "It reverses SN 12.15's question into its opposite"],
         "correct": 0,
         "expl": "The same existence question, widened in scope."},
        {"q": "How does the Buddha treat \"all exists\" and \"all does not exist\"?",
         "opts": [
             "He names each one an extreme in turn",
             "He affirms the first and rejects the second",
             "He affirms the second and rejects the first",
             "He declines to respond to either claim"],
         "correct": 0,
         "expl": "Both set aside without either being treated as the safer default."},
        {"q": "What formula resolves both extremes?",
         "opts": [
             "\"Avoiding these two extremes, the Realized One teaches by the middle way\"",
             "\"The question cannot be answered by anyone\"",
             "\"Both extremes are equally true\"",
             "\"Only a stream-enterer could know the answer\""],
         "correct": 0,
         "expl": "The identical formula used elsewhere in this saṃyutta."},
        {"q": "How many times has this exact middle-way formula now appeared in this saṃyutta, counting this discourse?",
         "opts": [
             "Four times — for the world's existence, the soul and body, doer and experiencer, and now everything",
             "Only once, exclusively in this discourse",
             "Twice, in this discourse and SN 12.15 alone",
             "This is a different formula from the ones used earlier"],
         "correct": 0,
         "expl": "A confirmed, recurring formula across four distinct pairs of extremes."},
        {"q": "Is Jānussoṇi named, unlike the brahmin in SN 12.46?",
         "opts": [
             "Yes — he is a named figure who appears in several other discourses across the early texts",
             "No, he is also left unnamed in this discourse",
             "He is named only in the closing verse, not the dialogue itself",
             "His name is given but described as uncertain"],
         "correct": 0,
         "expl": "A more documented questioner than SN 12.46's unnamed brahmin."},
        {"q": "What does the Buddha's answer replace the existence question with?",
         "opts": [
             "The twelve-link chain of dependent origination, run forward and in reverse",
             "A direct ruling that everything exists",
             "A direct ruling that nothing exists",
             "A refusal to address the question at all"],
         "correct": 0,
         "expl": "Conditionality offered in place of a verdict about existence."},
        {"q": "How does the discourse end?",
         "opts": [
             "Jānussoṇi praises the teaching and declares himself a lay follower for life",
             "Jānussoṇi walks away unconvinced",
             "Jānussoṇi asks a further question that goes unanswered",
             "The discourse ends without any response from Jānussoṇi"],
         "correct": 0,
         "expl": "The same conversion pattern as SN 12.46."},
        {"q": "What does this discourse demonstrate when read against SN 12.15?",
         "opts": [
             "That the same teaching answers an existence question however broadly or narrowly it's framed",
             "That the Buddha gave contradictory answers to similar questions",
             "That SN 12.15 must be a later addition to the canon",
             "That existence questions were considered off-limits for brahmins"],
         "correct": 0,
         "expl": "Breadth of question, sameness of answer."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("A question widened to everything", [
            "not the world alone, but all things &mdash;",
            "the same puzzle, broader scope",
        ]),
        ("Two extremes, again set aside", [
            "all exists, or all does not &mdash;",
            "neither claim allowed to stand",
        ]),
        ("A formula heard a fourth time", [
            "the same middle way, once more &mdash;",
            "answering however the question is framed",
        ]),
        ("A named questioner, for once", [
            "Jānussoṇi, met elsewhere too &mdash;",
            "a slightly less anonymous visitor",
        ]),
    ],
    further=[
        '<a href="%s/sn12.47/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.46.html">SN 12.46 &middot; A Certain Brahmin</a> '
        "&mdash; the discourse immediately before this one, "
        "structurally identical but for its question.",
        '<a href="sn-12.15.html">SN 12.15 &middot; Kaccānagotta</a> '
        "&mdash; the earlier discourse asking the same existence "
        "question specifically about the world.",
        '<a href="sn-12.48.html">SN 12.48 &middot; A Cosmologist</a> '
        "&mdash; the next discourse, the same two extremes joined by "
        "two further positions from a rival philosophical school.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.48 — Lokāyatikasutta
# --------------------------------------------------------------------------- #
page(
    12, 48, "Lokāyatika", "A Cosmologist",
    meta_title="SN 12.48 — A Cosmologist | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Lokāyatikasutta — a brahmin cosmologist names four "
        "positions instead of the usual two, and still receives the "
        "same twelve-link middle way already given for narrower "
        "pairs of extremes. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha and a brahmin cosmologist "
                     "(lokāyatika)"),
        ("Form", "Four questions in sequence, each answer named a "
                 "distinct cosmology, followed by the middle way and "
                 "a closing conversion"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "brief, but its four-position structure "
                       "raises an interpretive question this guide "
                       "doesn't try to resolve"),
    ],
    why=(
        "A brahmin identified as a lokāyatika &mdash; a term "
        "associated with a tradition of speculative natural "
        "philosophy, later linked to positions read as materialist, "
        "though this reading guide doesn't claim a precise "
        "identification with any later school &mdash; puts to the "
        "Buddha not two positions but four: everything exists, "
        "everything doesn't exist, everything is one, and everything "
        "is many. Each is named in turn as one of four cosmologies "
        "&mdash; the oldest, the second, the third, the fourth "
        "&mdash; without argument, before the Buddha responds with "
        "the same middle-way formula used elsewhere in this saṃyutta "
        "for narrower pairs of extremes. The discourse leaves an "
        "honest puzzle unresolved: the closing formula names "
        "avoiding \"these two extremes,\" yet four positions have "
        "just been listed, and the text itself doesn't clarify "
        "whether the middle way is meant to set aside all four or "
        "specifically the first pair."),
    guide=[
        ("Four positions where other discourses give two", [
            "Every other brahmin-question discourse in this chapter "
            "poses a single pair of extremes; this one uniquely "
            "poses four distinct cosmological positions in "
            "succession, each treated as its own numbered claim "
            "rather than folded into a binary."]),
        ("Named without argument, oldest to newest", [
            "Each position is introduced only to be labeled &mdash; "
            "\"this is the oldest cosmology,\" \"this is the second "
            "cosmology,\" and so on &mdash; with no reasoning given "
            "for why each one might seem plausible, unlike the "
            "brahmin's engagement in some other discourses in this "
            "collection."]),
        ("An honest interpretive puzzle left open", [
            "The closing formula speaks of avoiding \"these two "
            "extremes,\" but four positions have been named; this "
            "reading guide doesn't resolve whether the middle way is "
            "meant to address all four together or specifically "
            "returns to the first pair, since the source text itself "
            "doesn't clarify the point."]),
        ("The same middle way, regardless of how many extremes precede it", [
            "Whatever the resolution of that puzzle, the content of "
            "the Buddha's answer doesn't change: the same twelve-link "
            "chain, run forward to suffering's arising and in "
            "reverse to its cessation, already given for the "
            "questions in SN 12.15, SN 12.46, and SN 12.47."]),
        ("A term worth handling with care", [
            "Lokāyata is sometimes rendered \"cosmology\" and "
            "sometimes associated with later materialist or "
            "skeptical philosophy, but its precise scope in this "
            "discourse's own context is genuinely debated among "
            "scholars, and this reading guide doesn't assert a firm "
            "identification beyond what the text itself states."]),
    ],
    terms=[
        ("lokāyatiko brāhmaṇo",
         "&ldquo;a brahmin cosmologist&rdquo; &mdash; lokāyatika, a "
         "term whose precise scope and later associations with "
         "materialist philosophy are genuinely debated."),
        ("sabbamatthi&hellip; jeṭṭhametaṁ lokāyataṁ",
         "&ldquo;all exists: this is the oldest cosmology&rdquo; "
         "&mdash; the first of four positions named in turn."),
        ("sabbamekattaṁ&hellip; tatiyametaṁ lokāyataṁ",
         "&ldquo;all is oneness: this is the third cosmology&rdquo; "
         "&mdash; a position not raised by the other brahmins "
         "questioning existence elsewhere in this saṃyutta."),
        ("sabbaṁ puthuttaṁ&hellip; catutthametaṁ lokāyataṁ",
         "&ldquo;all is diversity: this is the fourth cosmology&rdquo; "
         "&mdash; the fourth and final position named."),
        ("ubho ante anupagamma majjhena tathāgato dhammaṁ deseti",
         "&ldquo;avoiding these two extremes, the Realized One "
         "teaches by the middle way&rdquo; &mdash; the same recurring "
         "formula, here following four named positions rather than "
         "two."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.48:1.1-1.3"),
        ("p", "&sect;2", "sn12.48:2.1-2.2"),
        ("p", "&sect;3", "sn12.48:3.1-3.2"),
        ("p", "&sect;4", "sn12.48:4.1-4.2"),
        ("p", "&sect;5", "sn12.48:5.1-5.2"),
        ("p", "&sect;6", "sn12.48:6.1-6.7"),
        ("p", "&sect;7", "sn12.48:7.1-7.3"),
    ],
    quiz=[
        {"q": "How many distinct positions does the brahmin cosmologist name, unlike most other brahmin-question discourses in this chapter?",
         "opts": [
             "Four, rather than the usual two",
             "Only one",
             "Two, exactly as in the other discourses",
             "Six"],
         "correct": 0,
         "expl": "A structurally unique discourse within this chapter's pattern."},
        {"q": "What are the four positions named in this discourse?",
         "opts": [
             "All exists, all doesn't exist, all is oneness, all is diversity",
             "All is permanent, all is impermanent, all is painful, all is pleasant",
             "The world is finite, infinite, both, and neither",
             "The self exists, doesn't exist, both, and neither"],
         "correct": 0,
         "expl": "Four cosmological claims, named oldest to newest."},
        {"q": "How does the Buddha respond to each of the four positions as they're raised?",
         "opts": [
             "He simply labels each one — the oldest cosmology, the second, and so on — without arguing against it",
             "He refutes each one in detailed argument",
             "He affirms two of the four as correct",
             "He refuses to engage with any of them"],
         "correct": 0,
         "expl": "Naming without argument, unlike some other brahmin exchanges in this collection."},
        {"q": "What interpretive puzzle does this reading guide note about the closing formula?",
         "opts": [
             "It speaks of \"these two extremes\" despite four positions having been named, and the text doesn't clarify the scope",
             "The closing formula is missing from this discourse entirely",
             "The formula explicitly names all four positions individually",
             "There is no puzzle; the formula clearly addresses all four"],
         "correct": 0,
         "expl": "An honest gap the reading guide doesn't try to resolve beyond what the text states."},
        {"q": "Does the content of the Buddha's answer change because four positions were raised instead of two?",
         "opts": [
             "No — the same twelve-link chain, forward and in reverse, is given regardless",
             "Yes, an entirely different teaching is given in this discourse",
             "Yes, the chain is given only in the forward direction here",
             "Yes, four separate teachings are given, one per position"],
         "correct": 0,
         "expl": "The same middle-way content as SN 12.15, SN 12.46, and SN 12.47."},
        {"q": "What term names the brahmin's own tradition in this discourse?",
         "opts": [
             "Lokāyatika",
             "Brāhmaṇa alone, with no further qualification",
             "Sāmaṇa",
             "Ājīvaka"],
         "correct": 0,
         "expl": "A term whose precise later associations this reading guide treats with caution."},
        {"q": "Does this reading guide assert a firm identification of lokāyata with a specific later philosophical school?",
         "opts": [
             "No — it notes the term's scope is genuinely debated among scholars",
             "Yes, it identifies it definitively with a specific later school",
             "Yes, it identifies the brahmin as a specific named historical figure",
             "The term is not discussed at all in this reading guide"],
         "correct": 0,
         "expl": "A deliberately cautious, non-overreaching treatment of a contested term."},
        {"q": "How does this discourse end?",
         "opts": [
             "The brahmin cosmologist praises the teaching and declares himself a lay follower for life",
             "The brahmin walks away unconvinced",
             "The brahmin challenges the Buddha to a formal debate",
             "The discourse ends without any response from the brahmin"],
         "correct": 0,
         "expl": "The same conversion pattern as SN 12.46 and SN 12.47."},
        {"q": "Which position among the four is unique to this discourse, not raised in SN 12.46 or SN 12.47?",
         "opts": [
             "That all is oneness, or that all is diversity",
             "That all exists",
             "That all does not exist",
             "None of the four positions are unique to this discourse"],
         "correct": 0,
         "expl": "The third and fourth cosmologies, absent from the narrower two-extreme exchanges."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The consistent setting across this chapter of Nidānavagga."},
    ],
    marginalia=[
        ("Four positions, not the usual two", [
            "existence, non-existence, oneness, diversity &mdash;",
            "each simply labeled and set down",
        ]),
        ("Named, not argued against", [
            "oldest, second, third, fourth cosmology &mdash;",
            "no rebuttal offered to any",
        ]),
        ("A puzzle left honestly open", [
            "\"these two extremes\" — but four were named &mdash;",
            "the text itself doesn't say which",
        ]),
        ("The same chain, however many named before it", [
            "twelve links, forward and reversed &mdash;",
            "unchanged by how the question was framed",
        ]),
    ],
    further=[
        '<a href="%s/sn12.48/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.47.html">SN 12.47 &middot; Jānussoṇi</a> '
        "&mdash; the discourse immediately before this one, posing "
        "the same first two positions alone.",
        '<a href="sn-12.49.html">SN 12.49 &middot; A Noble Disciple</a> '
        "&mdash; the next discourse, turning from a visitor's "
        "questions to how a noble disciple's own knowledge is "
        "independent of any such position.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.49 — Ariyasāvakasutta
# --------------------------------------------------------------------------- #
page(
    12, 49, "Ariyasāvaka", "A Noble Disciple",
    meta_title="SN 12.49 — A Noble Disciple | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ariyasāvakasutta — a learned noble disciple doesn't ask "
        "the twelve-link chain as a question at all, but holds it as "
        "knowledge independent of others, understanding this as how "
        "the world originates and ceases. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A contrast between a question never asked and the "
                 "independent knowledge held instead, run through "
                 "arising and cessation in full, unelided detail"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the fullest, most explicit statement in this "
                       "chapter of what distinguishes a noble "
                       "disciple's knowledge from ordinary inquiry"),
    ],
    why=(
        "This discourse draws a distinction easy to miss: a learned "
        "noble disciple doesn't think through dependent origination "
        "as a series of open questions &mdash; when what exists is "
        "there this, due to the arising of what does that arise? "
        "&mdash; because that framing would imply the matter is "
        "still uncertain. Instead they hold what the discourse calls "
        "knowledge independent of others (aparappaccayā ñāṇa), "
        "stated directly as a chain of conditions rather than "
        "arrived at by working through a series of hypotheticals. "
        "The forward and reverse directions are each given in full, "
        "unelided detail, link by link, closing with the "
        "understanding that this is how the world originates and "
        "how it ceases &mdash; the same equation of the world with "
        "the sense doors' conditioned process already made in SN "
        "12.44. The discourse ends with a cascade of honorific "
        "epithets for the disciple who holds this understanding, "
        "closing on the image of one who stands knocking at the door "
        "to freedom from death."),
    guide=[
        ("A question the disciple doesn't ask", [
            "The discourse opens by describing, at length, a series "
            "of hypothetical questions a learned noble disciple does "
            "not think &mdash; not because the questions are "
            "forbidden, but because thinking them would imply "
            "uncertainty about something the disciple already "
            "understands directly."]),
        ("Knowledge independent of others, named directly", [
            "\"Aparappaccayā ñāṇa\" &mdash; knowledge that doesn't "
            "depend on another for its validity &mdash; is offered "
            "as what the disciple has instead of the unanswered "
            "questions, a term naming a specific epistemic status "
            "rather than simple confidence or belief."]),
        ("The full chain, unelided in both directions", [
            "Unlike most treatments of the twelve links elsewhere in "
            "this saṃyutta, both the forward and reverse chains are "
            "spelled out link by link without peyyāla compression, "
            "giving this discourse the fullest explicit statement of "
            "the complete formula found in this chapter."]),
        ("The world, understood rather than debated", [
            "Each direction closes with the disciple simply "
            "understanding \"that is how this world originates\" or "
            "\"ceases\" &mdash; the identical equation of the world "
            "with the conditioned process at the sense doors already "
            "made explicit in SN 12.44, now folded into what a noble "
            "disciple's settled understanding actually consists of."]),
        ("A cascade of epithets closing the discourse", [
            "Rather than ending on a single description, the "
            "discourse closes by naming the disciple who holds this "
            "understanding through a sequence of honorific titles, "
            "building to the image of one who stands knocking at the "
            "door to freedom from death."]),
    ],
    terms=[
        ("sutavato ariyasāvakassa",
         "&ldquo;a learned noble disciple&rdquo; &mdash; the same "
         "recurring figure already named in SN 12.37 and SN 12.41."),
        ("aparappaccayā ñāṇaṁ",
         "&ldquo;knowledge independent of others&rdquo; &mdash; the "
         "discourse's key epistemological term, naming what the "
         "disciple has instead of open questions."),
        ("kismiṁ sati kiṁ hoti, kissuppādā kiṁ uppajjati",
         "&ldquo;when what exists, what is? Due to the arising of "
         "what, what arises?&rdquo; &mdash; the hypothetical "
         "question form the disciple does not think."),
        ("evamayaṁ loko samudayatī&hellip; nirujjhatī",
         "&ldquo;that is how this world originates&hellip; "
         "ceases&rdquo; &mdash; the closing understanding for each "
         "direction, echoing SN 12.44's equation of the world with "
         "this process."),
        ("amatadvāraṁ āhacca tiṭṭhati",
         "&ldquo;stands knocking at the door to freedom from "
         "death&rdquo; &mdash; the discourse's closing image, the "
         "last of a cascade of epithets."),
    ],
    text_intro=(
        "The discourse in full, given here without the peyyāla "
        "compression found elsewhere in this saṃyutta. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.49:1.1-1.2"),
        ("p", "&sect;2", "sn12.49:1.3-1.5"),
        ("p", "&sect;3", "sn12.49:2.1-2.15"),
        ("p", "&sect;4", "sn12.49:3.1-3.4"),
        ("p", "&sect;5", "sn12.49:4.1-4.11"),
        ("p", "&sect;6", "sn12.49:5.1-5.1"),
    ],
    quiz=[
        {"q": "What does the discourse say a learned noble disciple does not do?",
         "opts": [
             "Think through dependent origination as a series of open, hypothetical questions",
             "Practice meditation at all",
             "Speak to other mendicants",
             "Accept any teaching from the Buddha without question"],
         "correct": 0,
         "expl": "Not because the questions are forbidden, but because they'd imply unresolved uncertainty."},
        {"q": "What does the disciple have instead of these open questions?",
         "opts": [
             "Knowledge independent of others (aparappaccayā ñāṇa)",
             "A written scripture to consult",
             "A teacher who answers on their behalf",
             "Nothing; the discourse says the disciple simply remains uncertain"],
         "correct": 0,
         "expl": "A specific epistemic status, not mere belief or confidence."},
        {"q": "How is the twelve-link chain treated in this discourse, compared to most others in this saṃyutta?",
         "opts": [
             "Spelled out in full, unelided detail in both directions",
             "Heavily compressed with peyyāla ellipsis throughout",
             "Only the forward direction is given at all",
             "The chain is not mentioned in this discourse"],
         "correct": 0,
         "expl": "The fullest explicit statement of the complete formula in this chapter."},
        {"q": "What does the disciple understand at the close of each direction of the chain?",
         "opts": [
             "\"That is how this world originates\" or \"ceases\"",
             "\"That is how suffering is caused by the gods\"",
             "\"That is how the self is created\"",
             "The discourse gives no closing understanding at all"],
         "correct": 0,
         "expl": "Echoing SN 12.44's equation of the world with this conditioned process."},
        {"q": "What image closes the discourse's cascade of epithets?",
         "opts": [
             "One who stands knocking at the door to freedom from death",
             "One who has crossed the ocean of birth and death",
             "One who has extinguished all desire for food",
             "One who sits beneath the bodhi tree"],
         "correct": 0,
         "expl": "The final and most vivid of the honorific titles given."},
        {"q": "Why doesn't the disciple think the hypothetical question form at all, according to this discourse?",
         "opts": [
             "Because thinking it would imply uncertainty about something already understood directly",
             "Because such questions are forbidden by monastic rule",
             "Because the disciple has never heard of dependent origination",
             "Because the Buddha has explicitly banned all questions"],
         "correct": 0,
         "expl": "A framing issue, not a prohibition."},
        {"q": "What does \"aparappaccayā ñāṇa\" mean?",
         "opts": [
             "Knowledge independent of others, not dependent on another for its validity",
             "Knowledge received directly from a teacher's authority",
             "Knowledge gained only through years of study",
             "A term meaning \"doubt\" or \"uncertainty\""],
         "correct": 0,
         "expl": "A specific term for self-verified, direct understanding."},
        {"q": "Where does the equation of \"the world\" with this conditioned process first appear explicitly in this chapter?",
         "opts": [
             "SN 12.44, paired with SN 12.43's identical formula under the name \"suffering\"",
             "This is the first discourse in the chapter to make this equation",
             "SN 12.41, in the declaration of stream-entry",
             "SN 12.31, in Sāriputta's threefold seeing"],
         "correct": 0,
         "expl": "A phrase planted earlier in this chapter and echoed here."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
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
        ("A question never asked", [
            "not forbidden, but unnecessary &mdash;",
            "already understood, not wondered at",
        ]),
        ("Knowledge that answers to no one else", [
            "aparappaccayā ñāṇa &mdash;",
            "not dependent on another's word",
        ]),
        ("The full chain, this time unelided", [
            "every link spelled out, both ways &mdash;",
            "arising and cessation alike",
        ]),
        ("A cascade closing on one image", [
            "epithet after epithet &mdash;",
            "knocking at the door to no more death",
        ]),
    ],
    further=[
        '<a href="%s/sn12.49/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.48.html">SN 12.48 &middot; A Cosmologist</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.44.html">SN 12.44 &middot; The World</a> '
        "&mdash; the earlier discourse in this chapter first equating "
        "the world with the process this discourse's disciple "
        "understands.",
        '<a href="sn-12.50.html">SN 12.50 &middot; A Noble Disciple (2nd)</a> '
        "&mdash; the next discourse, closing this chapter with the "
        "same teaching and a fuller version of its closing epithets.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.50 — Dutiyaariyasāvakasutta
# --------------------------------------------------------------------------- #
page(
    12, 50, "Dutiyaariyasāvaka", "A Noble Disciple (2nd)",
    meta_title="SN 12.50 — A Noble Disciple (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaariyasāvakasutta — closing Gahapativagga with the "
        "same teaching as SN 12.49, its closing epithets spelled out "
        "in full where its twin elides them. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same contrast and chain as SN 12.49, with the "
                 "closing cascade of epithets given in full rather "
                 "than elided"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "closing this chapter with its fullest single "
                       "statement of a noble disciple's understanding"),
    ],
    why=(
        "Closing Gahapativagga, this discourse repeats SN 12.49's "
        "teaching almost word for word &mdash; the same hypothetical "
        "question the disciple doesn't think, the same knowledge "
        "independent of others, the same forward and reverse chain "
        "&mdash; but reverses where the compression falls. This "
        "discourse elides more of its middle sections with peyyāla "
        "than SN 12.49 does, yet spells out in full something SN "
        "12.49 elides: the complete cascade of nine epithets "
        "describing the disciple who holds this understanding, from "
        "\"accomplished in view\" through \"a noble one with "
        "penetrative wisdom\" to the closing image of one who stands "
        "at the door to freedom from death. Sujato's translation "
        "renders that closing phrase differently in the two twin "
        "discourses &mdash; \"knocking\" in SN 12.49, \"pressing "
        "against\" here &mdash; despite the identical Pali underlying "
        "both, a small, honestly noted variation in how the same "
        "phrase has been rendered twice."),
    guide=[
        ("The same teaching, compression redistributed", [
            "Every substantive element of SN 12.49 reappears here "
            "&mdash; the unasked question, knowledge independent of "
            "others, the full chain &mdash; but this discourse elides "
            "more of its middle material with peyyāla than its twin, "
            "while expanding elsewhere."]),
        ("Nine epithets, spelled out where SN 12.49 elides them", [
            "SN 12.49's closing cascade of titles for the "
            "understanding disciple uses a peyyāla ellipsis partway "
            "through; this discourse gives all nine in full &mdash; "
            "accomplished in view, accomplished in vision, come to "
            "the true teaching, one who sees the true teaching, "
            "endowed with a trainee's knowledge, endowed with a "
            "trainee's wisdom, entered the stream of the teaching, a "
            "noble one with penetrative wisdom &mdash; before the "
            "closing image."]),
        ("One phrase, two different translations", [
            "The closing phrase &ldquo;amatadvāraṁ āhacca "
            "tiṭṭhati&rdquo; is identical in the Pali of both "
            "discourses, yet Sujato renders it &ldquo;stands knocking "
            "at the door to freedom from death&rdquo; in SN 12.49 and "
            "&ldquo;stands pressing against the door to freedom from "
            "death&rdquo; here &mdash; a small, honestly noted "
            "translation variance between twin discourses rather "
            "than a difference in the underlying text."]),
        ("A chapter closing on understanding, not narrative drama", [
            "Unlike some other vaggas in this saṃyutta, which close "
            "on a dramatic or emotionally weighted episode, "
            "Gahapativagga ends on a purely doctrinal note: what "
            "exactly a noble disciple's settled understanding of "
            "dependent origination consists of, restated once more "
            "for emphasis."]),
        ("The vagga's own closing verse, present but untranslated", [
            "This discourse carries Gahapativagga's closing verse of "
            "discourse titles, not translated in the source and not "
            "quoted here; its ten titles are described in the "
            "reading guide's summary of this chapter instead, "
            "following the same convention used at the close of "
            "Kaḷārakhattiyavagga."]),
    ],
    terms=[
        ("aparappaccayā ñāṇaṁ",
         "&ldquo;knowledge independent of others&rdquo; &mdash; the "
         "same key term as SN 12.49."),
        ("evamayaṁ loko samudayatī&hellip; nirujjhatī",
         "&ldquo;that is how this world originates&hellip; "
         "ceases&rdquo; &mdash; the same closing understanding as SN "
         "12.49, for each direction of the chain."),
        ("dassanasampanno&hellip; sekkhena ñāṇena samannāgato&hellip; "
         "ariyo nibbedhikapañño",
         "&ldquo;accomplished in vision&hellip; endowed with a "
         "trainee's knowledge&hellip; a noble one with penetrative "
         "wisdom&rdquo; &mdash; part of the nine-epithet cascade "
         "this discourse spells out in full where SN 12.49 elides "
         "it with peyyāla."),
        ("amatadvāraṁ āhacca tiṭṭhati",
         "&ldquo;stands pressing against the door to freedom from "
         "death&rdquo; &mdash; the identical Pali phrase Sujato "
         "renders as &ldquo;knocking&rdquo; in SN 12.49, translated "
         "differently here."),
        ("kismiṁ sati kiṁ hoti, kissuppādā kiṁ uppajjati",
         "&ldquo;when what exists, what is? Due to the arising of "
         "what, what arises?&rdquo; &mdash; the same hypothetical "
         "question form the disciple does not think, shared with SN "
         "12.49."),
    ],
    text_intro=(
        "The discourse in full, closing Gahapativagga. The "
        "chapter's closing verse of discourse titles is not "
        "translated in the source and is not quoted here; see the "
        "reading guide above for its contents. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.50:1.1-1.2"),
        ("p", "&sect;2", "sn12.50:1.3-1.4"),
        ("p", "&sect;3", "sn12.50:2.1-2.15"),
        ("p", "&sect;4", "sn12.50:3.1-3.3"),
        ("p", "&sect;5", "sn12.50:4.1-4.9"),
        ("p", "&sect;6", "sn12.50:5.1-5.1"),
    ],
    quiz=[
        {"q": "How does this discourse's teaching compare to SN 12.49's?",
         "opts": [
             "The same substantive teaching, with compression redistributed differently",
             "An entirely different, unrelated teaching",
             "A direct contradiction of SN 12.49",
             "A much shorter fragment omitting most content"],
         "correct": 0,
         "expl": "Same content, differently compressed in different places."},
        {"q": "What does this discourse spell out in full that SN 12.49 elides?",
         "opts": [
             "The complete cascade of nine epithets describing the understanding disciple",
             "The twelve-link chain itself",
             "The setting and audience",
             "The hypothetical question the disciple doesn't think"],
         "correct": 0,
         "expl": "All nine epithets given here, where SN 12.49 uses an ellipsis partway through."},
        {"q": "How does Sujato translate \"amatadvāraṁ āhacca tiṭṭhati\" in this discourse, compared to SN 12.49?",
         "opts": [
             "\"Pressing against\" here, versus \"knocking\" in SN 12.49, for identical Pali",
             "The exact same English wording in both discourses",
             "This discourse omits the phrase entirely",
             "\"Breaking down\" here, versus \"opening\" in SN 12.49"],
         "correct": 0,
         "expl": "A small, honestly noted translation variance between twin discourses."},
        {"q": "What does this discourse's closing verse of discourse titles consist of?",
         "opts": [
             "An untranslated uddāna listing Gahapativagga's ten discourse titles, not quoted in the text section",
             "A fully translated poem quoted in the text section",
             "A prose summary of the whole chapter",
             "This discourse has no closing verse at all"],
         "correct": 0,
         "expl": "Following the same convention used for untranslated closing material elsewhere in this saṃyutta."},
        {"q": "What chapter does this discourse close?",
         "opts": [
             "Gahapativagga",
             "Kaḷārakhattiyavagga",
             "Dasabalavagga",
             "Dukkhavagga"],
         "correct": 0,
         "expl": "The fifth chapter of Nidānavagga, named for its opening discourse's householder."},
        {"q": "What does the disciple understand at the close of each direction of the chain?",
         "opts": [
             "\"That is how this world originates\" or \"ceases\"",
             "\"That is how the self is created\"",
             "\"That is how suffering is caused by fate\"",
             "The discourse gives no closing understanding"],
         "correct": 0,
         "expl": "The same equation of the world with this process as SN 12.49."},
        {"q": "Does Gahapativagga close on a dramatic narrative episode, like some other vaggas in this saṃyutta?",
         "opts": [
             "No — it closes on a purely doctrinal restatement of a noble disciple's understanding",
             "Yes, it closes with the Buddha's own death",
             "Yes, it closes with a dramatic confrontation with Māra",
             "Yes, it closes with a monk's sudden death"],
         "correct": 0,
         "expl": "A quieter, doctrinally focused close than Book I's more narrative vagga endings."},
        {"q": "What term names the epistemic status the disciple has instead of open questions?",
         "opts": [
             "Aparappaccayā ñāṇa, knowledge independent of others",
             "Saddhā, faith alone",
             "Vīmaṁsā, mere speculation",
             "Sati, mindfulness alone"],
         "correct": 0,
         "expl": "The same key term used in SN 12.49."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "Near Kapilavatthu"],
         "correct": 0,
         "expl": "The same setting as SN 12.49, immediately before it."},
    ],
    marginalia=[
        ("The same teaching, compression moved", [
            "elided more here, less there &mdash;",
            "one twin balancing the other",
        ]),
        ("Nine epithets, none left out", [
            "spelled out where SN 12.49 abbreviates &mdash;",
            "the full cascade, this time complete",
        ]),
        ("One phrase, two English hands", [
            "\"knocking\" there, \"pressing against\" here &mdash;",
            "the same Pali, rendered twice differently",
        ]),
        ("A chapter closed without drama", [
            "no death, no confrontation &mdash;",
            "only understanding, restated once more",
        ]),
    ],
    further=[
        '<a href="%s/sn12.50/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.49.html">SN 12.49 &middot; A Noble Disciple</a> '
        "&mdash; the discourse immediately before this one, its twin "
        "in every substantive respect.",
        '<a href="sn-12.41.html">SN 12.41 &middot; Fears and Enmities</a> '
        "&mdash; opening this chapter with Anāthapiṇḍika's three-part "
        "self-test, closed here by a purely doctrinal restatement of "
        "a noble disciple's understanding.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.51 — Parivīmaṁsanasutta
# --------------------------------------------------------------------------- #
page(
    12, 51, "Parivīmaṁsana", "An Inquiry",
    meta_title="SN 12.51 — An Inquiry | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Parivīmaṁsanasutta — opening Dukkhavagga, a systematic "
        "inquiry traces suffering back through the whole chain, the "
        "kammic mechanism of rebirth, the arahant's personal "
        "extinguishment, and a closing catechism climaxing in the "
        "Buddha's most emphatic single line in this saṃyutta. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A long, multi-movement discourse: a systematic "
                 "backward inquiry through the chain, the mechanism "
                 "of kammic rebirth, a description of the arahant's "
                 "extinguishment, and a closing catechism"),
        ("Length", "~9 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; "
                       "&mdash; the longest and most structurally "
                       "ambitious discourse in this chapter"),
    ],
    why=(
        "Opening Dukkhavagga, this discourse asks what it actually "
        "means to inquire for the complete ending of suffering, and "
        "answers by walking through the whole exercise from the "
        "start: a mendicant traces old age and death back to "
        "rebirth, rebirth back to continued existence, and onward "
        "through the chain to ignorance, understanding each link's "
        "origin, cessation, and the practice leading to that "
        "cessation. The discourse then turns to the mechanism itself "
        "&mdash; how an unenlightened person's good, bad, or "
        "imperturbable choices each carry consciousness forward into "
        "a corresponding rebirth, and how someone who has given up "
        "ignorance makes none of these choices at all, grasps at "
        "nothing, and \"personally becomes extinguished.\" A vivid "
        "simile of a hot clay pot cooling on level ground illustrates "
        "what happens to feeling at the end of such a life. The "
        "discourse closes with a rapid catechism reversing through "
        "every link in turn, and the Buddha's own unusually emphatic "
        "confirmation: trust this, have no doubts, this is simply "
        "the end of suffering."),
    guide=[
        ("Inquiry defined by what it accomplishes, not just its method", [
            "The discourse opens by asking how a mendicant's inquiry "
            "should be defined, and answers not with a description "
            "of technique but with what the inquiry is for: the "
            "complete ending of suffering, named as the standard "
            "against which the whole exercise that follows is "
            "measured."]),
        ("A four-part question asked at every link", [
            "At each stage the mendicant asks the same fourfold "
            "question &mdash; what is this suffering's source, "
            "origin, birthplace, and inception &mdash; a slightly "
            "more elaborate formula than the simpler \"when this "
            "exists, this comes to be\" used elsewhere in this "
            "saṃyutta, repeated at every link before the chain is "
            "elided with peyyāla for the middle links."]),
        ("A precise account of how choices carry consciousness forward", [
            "Rather than speaking abstractly about kamma and "
            "rebirth, the discourse specifies three kinds of choice "
            "&mdash; good, bad, and imperturbable &mdash; each said "
            "to carry consciousness forward \"by means of\" that "
            "same quality, giving a mechanically precise account "
            "before describing what happens when none of the three "
            "are made at all."]),
        ("Extinguishment described as personal, not abstract", [
            "\"Paccattaññeva parinibbāyati\" &mdash; becoming "
            "extinguished personally, for oneself &mdash; resists "
            "being read as a merely doctrinal outcome; the phrase "
            "insists on this being something that happens to a "
            "particular person, not a category shift."]),
        ("A closing catechism that reverses the entire chain in miniature", [
            "Rather than restating the reverse chain as a single "
            "declarative passage, the discourse closes by having the "
            "Buddha ask, link by link, whether each downstream "
            "phenomenon would still be found in the complete absence "
            "of what precedes it, met each time with a simple \"no, "
            "sir\" before the Buddha's own unusually emphatic "
            "confirmation closes the exchange."]),
    ],
    terms=[
        ("parivīmaṁsamāno parivīmaṁseyya sabbaso sammā "
         "dukkhakkhayāya",
         "&ldquo;a mendicant inquiring, for the complete ending of "
         "suffering&rdquo; &mdash; the standard the whole discourse "
         "measures its inquiry against."),
        ("kiṁnidānaṁ kiṁsamudayaṁ kiṁjātikaṁ kiṁpabhavaṁ",
         "&ldquo;what is its source, origin, birthplace, and "
         "inception?&rdquo; &mdash; the fourfold question asked at "
         "every link, more elaborate than this saṃyutta's usual "
         "conditionality formula."),
        ("avijjāgato&hellip; puññañce saṅkhāraṁ abhisaṅkharoti, "
         "puññūpagaṁ hoti viññāṇaṁ",
         "&ldquo;an ignoramus&hellip; if they make a good choice, "
         "consciousness passes on by means of goodness&rdquo; "
         "&mdash; the precise mechanism linking choice to rebirth."),
        ("anupādiyaṁ na paritassati, aparitassaṁ paccattaññeva "
         "parinibbāyati",
         "&ldquo;not grasping, they're not anxious. Not being "
         "anxious, they personally become extinguished&rdquo; "
         "&mdash; extinguishment insisted on as something happening "
         "to a particular person."),
        ("sādhu sādhu&hellip; saddahatha me taṁ&hellip; esevanto "
         "dukkhassa",
         "&ldquo;good, good!&hellip; trust me on this&hellip; just "
         "this is the end of suffering&rdquo; &mdash; the closing "
         "catechism's unusually emphatic confirmation."),
    ],
    text_intro=(
        "The discourse in full, opening Dukkhavagga. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.51:1.1-1.6"),
        ("p", "&sect;2", "sn12.51:2.1-2.5"),
        ("p", "&sect;3", "sn12.51:3.1-3.7"),
        ("p", "&sect;4", "sn12.51:4.1-4.2"),
        ("p", "&sect;5", "sn12.51:5.1-5.5"),
        ("p", "&sect;6", "sn12.51:6.1-6.2"),
        ("p", "&sect;7", "sn12.51:7.1-7.14"),
        ("p", "&sect;8", "sn12.51:8.1-8.2"),
        ("p", "&sect;9", "sn12.51:9.1-9.7"),
        ("p", "&sect;10", "sn12.51:10.1-10.6"),
        ("p", "&sect;11", "sn12.51:11.1-11.2"),
        ("p", "&sect;12", "sn12.51:12.1-12.4"),
        ("p", "&sect;13", "sn12.51:13.1-23.2"),
        ("p", "&sect;14", "sn12.51:24.1-24.3"),
    ],
    quiz=[
        {"q": "What standard does the discourse use to define a mendicant's inquiry?",
         "opts": [
             "The complete ending of suffering",
             "Success in monastic examinations",
             "Approval from a senior teacher",
             "The ability to recite scripture from memory"],
         "correct": 0,
         "expl": "What the entire exercise that follows is measured against."},
        {"q": "What fourfold question is asked at every link of the chain in this discourse?",
         "opts": [
             "What is its source, origin, birthplace, and inception?",
             "Is it permanent, painful, pleasant, or neutral?",
             "Who created it, when, why, and for whom?",
             "Is it visible, audible, tangible, or conceptual?"],
         "correct": 0,
         "expl": "A more elaborate formula than the simpler conditionality question used elsewhere."},
        {"q": "According to the discourse, what happens when an unenlightened person makes a good, bad, or imperturbable choice?",
         "opts": [
             "Consciousness passes on by means of that same quality",
             "Nothing happens; choices have no effect on rebirth",
             "Only bad choices affect future rebirth",
             "The choice is immediately erased by meditation"],
         "correct": 0,
         "expl": "A mechanically precise account of how choice carries consciousness forward."},
        {"q": "What does someone who has given up ignorance no longer do, according to this discourse?",
         "opts": [
             "Make good, bad, or imperturbable choices, or grasp at anything in the world",
             "Eat, sleep, or breathe",
             "Speak to other mendicants",
             "Feel any sensation whatsoever"],
         "correct": 0,
         "expl": "The absence of choice-making and grasping that leads to personal extinguishment."},
        {"q": "What image illustrates what happens to feeling at the end of such a life?",
         "opts": [
             "A hot clay pot removed from a kiln, cooling on level ground",
             "A river flowing endlessly into the sea",
             "A lamp burning until its oil runs out",
             "A tree growing new branches each spring"],
         "correct": 0,
         "expl": "A vivid image for feeling cooling once no longer taken pleasure in."},
        {"q": "How does the discourse phrase the arahant's extinguishment?",
         "opts": [
             "\"They personally become extinguished\" (paccattaññeva parinibbāyati)",
             "\"They vanish into an abstract state\"",
             "\"They are reborn in a higher heaven\"",
             "\"They achieve fame among mendicants\""],
         "correct": 0,
         "expl": "Insisted on as something happening to a particular person, not a category shift."},
        {"q": "How does the closing catechism proceed?",
         "opts": [
             "The Buddha asks, link by link, whether each phenomenon would be found without what precedes it, met with \"no, sir\"",
             "The mendicants ask the Buddha a series of unrelated questions",
             "The catechism consists of a single long question with no reply",
             "There is no catechism; the discourse ends with the hot clay pot simile"],
         "correct": 0,
         "expl": "A rapid reversal of the entire chain in miniature."},
        {"q": "How does the Buddha respond once the catechism is complete?",
         "opts": [
             "With unusually emphatic confirmation, urging the mendicants to trust him and have no doubts",
             "By asking the mendicants to repeat the catechism a second time",
             "With silence",
             "By introducing an entirely new teaching"],
         "correct": 0,
         "expl": "\"Good, good!... just this is the end of suffering.\""},
        {"q": "What do the mendicants say before the Buddha begins his teaching?",
         "opts": [
             "That their teachings are rooted in the Buddha, and ask him to clarify the meaning himself",
             "That they already understand the answer",
             "That they would prefer a different topic",
             "Nothing; the Buddha begins without any response from them"],
         "correct": 0,
         "expl": "A deferential request that the Buddha supply the meaning directly."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The usual Sāvatthī setting, distinct from a later discourse in this same chapter."},
    ],
    marginalia=[
        ("Inquiry defined by its aim", [
            "not method, but purpose &mdash;",
            "the complete ending of suffering",
        ]),
        ("Choice carrying consciousness forward", [
            "good, bad, or imperturbable &mdash;",
            "each one its own momentum",
        ]),
        ("Extinguished personally, not abstractly", [
            "paccattaññeva parinibbāyati &mdash;",
            "happening to someone, not a category",
        ]),
        ("A catechism ending in trust", [
            "\"no, sir\" through every link &mdash;",
            "then, \"just this is the end of suffering\"",
        ]),
    ],
    further=[
        '<a href="%s/sn12.51/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.50.html">SN 12.50 &middot; A Noble Disciple (2nd)</a> '
        "&mdash; the discourse closing Gahapativagga, immediately "
        "before this one.",
        '<a href="sn-12.52.html">SN 12.52 &middot; Grasping</a> '
        "&mdash; the next discourse, opening a run of similes "
        "illustrating the same craving fed or starved.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.52 — Upādānasutta
# --------------------------------------------------------------------------- #
page(
    12, 52, "Upādāna", "Grasping",
    meta_title="SN 12.52 — Grasping | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upādānasutta — craving grows or ceases depending on "
        "whether attention dwells on gratification or drawbacks, "
        "illustrated by a great mass of fire fed or starved of fuel. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Two matched pairs, each a direct statement "
                 "followed by a fire simile, for arising and then "
                 "for cessation"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "opens a run of similes sharing this "
                       "chapter's central image"),
    ],
    why=(
        "This discourse locates the lever that determines whether "
        "craving grows or dies down: not the things that fuel "
        "grasping themselves, but where attention settles on them. "
        "Concentrating on their gratification makes craving grow, "
        "setting the familiar chain in motion toward the whole mass "
        "of suffering; concentrating on their drawbacks makes "
        "craving cease, and the chain unwinds in reverse. A great "
        "mass of fire, burning on ten, twenty, thirty, or forty "
        "loads of wood, illustrates both directions: fed from time "
        "to time with dry grass, dung, or wood, it burns on "
        "indefinitely; left unfed, once its original fuel is used "
        "up, it simply goes out. The discourse opens a run of "
        "similes running through much of the rest of this chapter, "
        "each returning to some version of this same image of "
        "feeding and starving."),
    guide=[
        ("Attention as the actual variable, not the fuel itself", [
            "The things that fuel grasping don't change between the "
            "two halves of the teaching; what changes is whether "
            "attention dwells on their gratification or their "
            "drawbacks, locating the real lever in how something is "
            "attended to rather than in the object itself."]),
        ("A fire sustained by ordinary, unremarkable fuel", [
            "The simile's fire isn't stoked by anything exotic "
            "&mdash; dry grass, cow dung, and wood, added from time "
            "to time &mdash; making the point that craving's "
            "continuation doesn't require dramatic input, only "
            "small, repeated feeding."]),
        ("A concrete scale given to an otherwise abstract image", [
            "Specifying ten, twenty, thirty, or forty loads of wood "
            "gives the fire's initial size a concrete, almost "
            "mundane precision, grounding what could otherwise read "
            "as a purely poetic image."]),
        ("Extinguishment through simple absence, not active suppression", [
            "The fire doesn't need to be put out by force; once no "
            "more fuel is added and the original supply is used up, "
            "it goes out on its own &mdash; a model for craving's "
            "cessation as the natural result of withdrawn feeding "
            "rather than a struggle against it."]),
        ("The first of a chain of similes running through this chapter", [
            "This fire simile is the first of several images "
            "&mdash; an oil lamp, a great tree, a sapling &mdash; "
            "that recur through the rest of Dukkhavagga, each "
            "restating the same feeding-and-starving structure "
            "through a different concrete picture."]),
    ],
    terms=[
        ("upādāniyesu&hellip; dhammesu assādānupassino viharato "
         "taṇhā pavaḍḍhati",
         "&ldquo;there are things that fuel grasping. When you "
         "concentrate on the gratification provided by these "
         "things, your craving grows&rdquo; &mdash; the discourse's "
         "opening statement of the arising half."),
        ("dasannaṁ vā kaṭṭhavāhānaṁ&hellip; cattārīsāya vā "
         "kaṭṭhavāhānaṁ",
         "&ldquo;ten, twenty, thirty, or forty loads of wood&rdquo; "
         "&mdash; the concrete scale given to the simile's fire."),
        ("mahāaggikkhandho tadāhāro tadupādāno ciraṁ dīghamaddhānaṁ "
         "jaleyya",
         "&ldquo;the great mass of fire would burn for a long "
         "time&rdquo; &mdash; fed and fuelled, the standard formula "
         "for what sustains the simile's image."),
        ("upādāniyesu&hellip; dhammesu ādīnavānupassino viharato "
         "taṇhā nirujjhati",
         "&ldquo;there are things that fuel grasping. When you "
         "concentrate on the drawbacks of these things, your "
         "craving ceases&rdquo; &mdash; the mirrored statement "
         "opening the cessation half."),
        ("purimassa ca upādānassa pariyādānā aññassa ca anupahārā "
         "anāhāro nibbāyeyya",
         "&ldquo;as the original fuel is used up and no more is "
         "added, the great mass of fire would be extinguished due "
         "to not being fed&rdquo; &mdash; cessation through "
         "withdrawn feeding, not active suppression."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.52:1.1-1.7"),
        ("p", "&sect;2", "sn12.52:2.1-2.6"),
        ("p", "&sect;3", "sn12.52:3.1-3.6"),
        ("p", "&sect;4", "sn12.52:4.1-4.6"),
    ],
    quiz=[
        {"q": "What determines whether craving grows or ceases, according to this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The specific object being grasped",
             "How much wealth a person has",
             "Whether the person is ordained or a layperson"],
         "correct": 0,
         "expl": "Attention, not the object itself, is the real variable."},
        {"q": "What fuels the simile's fire?",
         "opts": [
             "Ordinary, unremarkable materials — dry grass, cow dung, and wood",
             "A rare and exotic incense",
             "Oil poured continuously from a large vessel",
             "The fire requires no fuel at all in this simile"],
         "correct": 0,
         "expl": "Craving's continuation doesn't require dramatic input, only small, repeated feeding."},
        {"q": "What concrete scale is given to the fire's initial size?",
         "opts": [
             "Ten, twenty, thirty, or forty loads of wood",
             "A single small twig",
             "An entire forest",
             "No scale is given; the fire's size is left vague"],
         "correct": 0,
         "expl": "A mundane precision grounding what could otherwise be purely poetic."},
        {"q": "How does the fire go out in the cessation half of the simile?",
         "opts": [
             "Simply by not being fed, once the original fuel is used up",
             "By someone actively dousing it with water",
             "By a sudden storm extinguishing it",
             "It never goes out in this simile"],
         "correct": 0,
         "expl": "Cessation through withdrawn feeding, not active suppression."},
        {"q": "What role does this discourse play within the rest of Dukkhavagga?",
         "opts": [
             "It opens a run of similes — an oil lamp, a great tree, a sapling — sharing the same structure",
             "It is the chapter's final discourse",
             "It stands alone with no connection to the discourses around it",
             "It contradicts the teaching given in the discourses that follow it"],
         "correct": 0,
         "expl": "The first of several images restating the same feeding-and-starving structure."},
        {"q": "What does the discourse call the things that determine craving's growth?",
         "opts": [
             "Things that fuel grasping",
             "Things that cause physical illness",
             "Things forbidden by monastic rule",
             "Things unrelated to the twelve-link chain"],
         "correct": 0,
         "expl": "Named directly, framing the object of grasping rather than a separate category."},
        {"q": "How is the arising half of the teaching structured?",
         "opts": [
             "A direct statement followed by the fire simile applied to the same content",
             "Only the simile is given, with no direct statement",
             "Only the direct statement is given, with no simile",
             "The arising half is entirely absent from this discourse"],
         "correct": 0,
         "expl": "A matched pair, statement then simile, repeated for cessation as well."},
        {"q": "What happens to the chain of conditions once craving ceases in this discourse?",
         "opts": [
             "It unwinds in reverse, through grasping, continued existence, rebirth, to the ending of suffering",
             "It has no further effect on anything downstream",
             "It reverses only partway, stopping at grasping",
             "The discourse doesn't describe what follows craving's cessation"],
         "correct": 0,
         "expl": "The familiar reverse chain, closing on suffering's complete cessation."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("Attention, the real lever", [
            "not the object, but where the mind rests &mdash;",
            "gratification, or its drawbacks",
        ]),
        ("Ordinary fuel, steadily added", [
            "dry grass, dung, wood &mdash;",
            "nothing exotic sustains the fire",
        ]),
        ("A scale given to the image", [
            "ten loads, forty loads &mdash;",
            "precision grounding the poetry",
        ]),
        ("Extinguished by simple absence", [
            "no force needed to put it out &mdash;",
            "just no more feeding it",
        ]),
    ],
    further=[
        '<a href="%s/sn12.52/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.51.html">SN 12.51 &middot; An Inquiry</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.53.html">SN 12.53 &middot; Fetters</a> '
        "&mdash; the next discourse, the same structure retold with "
        "an oil lamp in place of a fire.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.53 — Saṁyojanasutta
# --------------------------------------------------------------------------- #
page(
    12, 53, "Saṁyojana", "Fetters",
    meta_title="SN 12.53 — Fetters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Saṁyojanasutta — the same attention-driven growth and "
        "cessation of craving as SN 12.52, now framed around what "
        "tightens the fetters, illustrated by an oil lamp fed or "
        "left unattended. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same two matched pairs as SN 12.52, with an "
                 "oil lamp in place of a fire and a shift from "
                 "\"grasping\" to \"fetters\" in the framing"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as SN 12.52, in a "
                       "different image"),
    ],
    why=(
        "This discourse repeats SN 12.52's structure exactly &mdash; "
        "attention on gratification growing craving, attention on "
        "drawbacks ending it, each half paired with a fire-family "
        "simile &mdash; but changes two things at once. The framing "
        "shifts from \"things that fuel grasping\" (upādāniyesu "
        "dhammesu) to \"things that tighten the fetters\" "
        "(saṁyojaniyesu dhammesu), and the simile shifts from a "
        "great mass of fire to a small oil lamp, kept burning by "
        "someone pouring in oil and adjusting the wick from time to "
        "time, or left to go out once its fuel is used up and "
        "nothing more is added. The change in scale, from a great "
        "blaze to a single household lamp, doesn't change the "
        "underlying mechanism at all."),
    guide=[
        ("Two changes at once, one structure unchanged", [
            "Both the vocabulary naming what's at stake (fetters "
            "rather than grasping) and the simile's image (a lamp "
            "rather than a fire) change together, while the "
            "underlying two-part, attention-driven structure carries "
            "over from SN 12.52 without modification."]),
        ("Fetters as a different lens on the same danger", [
            "\"Saṁyojana\" names the same underlying things named "
            "\"upādāniya\" in SN 12.52, but foregrounds their "
            "binding, restraining function rather than their role "
            "as fuel for grasping &mdash; two names for the same "
            "hazard, each emphasizing a different aspect of it."]),
        ("A smaller, more domestic image than SN 12.52's blaze", [
            "Where SN 12.52's fire was scaled up to ten or forty "
            "loads of wood, this discourse's oil lamp is a modest, "
            "everyday object, tended by pouring in oil and adjusting "
            "the wick &mdash; a smaller image making the same point "
            "about ordinary, unremarkable maintenance sustaining "
            "craving."]),
        ("The same maintenance, the same neglect", [
            "Just as SN 12.52's fire needed only periodic feeding to "
            "keep burning, this discourse's lamp needs only "
            "occasional attention &mdash; pouring oil, adjusting the "
            "wick &mdash; and its extinguishing likewise requires "
            "nothing more dramatic than simply withholding that "
            "attention."]),
        ("A pairing that confirms the mechanism, not just the image", [
            "Because the underlying structure is identical to SN "
            "12.52's, reading the two discourses together confirms "
            "that the mechanism being taught doesn't depend on any "
            "particular image &mdash; fire or lamp, grasping or "
            "fetters &mdash; but on attention itself."]),
    ],
    terms=[
        ("saṁyojaniyesu&hellip; dhammesu assādānupassino viharato "
         "taṇhā pavaḍḍhati",
         "&ldquo;there are things that tighten the fetters. When "
         "you concentrate on the gratification provided by these "
         "things, your craving grows&rdquo; &mdash; the same "
         "structure as SN 12.52, with fetters in place of "
         "grasping."),
        ("telañca paṭicca vaṭṭiñca paṭicca telappadīpo jhāyeyya",
         "&ldquo;an oil lamp depended on oil and a wick to "
         "burn&rdquo; &mdash; the simile's image, in place of SN "
         "12.52's great mass of fire."),
        ("kālena kālaṁ telaṁ āsiñceyya vaṭṭiṁ upasaṁhareyya",
         "&ldquo;from time to time someone would pour oil in and "
         "adjust the wick&rdquo; &mdash; the small, periodic "
         "maintenance sustaining the lamp."),
        ("purimassa ca upādānassa pariyādānā aññassa ca anupahārā "
         "anāhāro nibbāyeyya",
         "&ldquo;as the original fuel is used up and no more is "
         "added, the oil lamp would be extinguished due to not "
         "being fed&rdquo; &mdash; the same extinguishing formula "
         "as SN 12.52, applied to the lamp."),
        ("assādānupassino&hellip; ādīnavānupassino",
         "&ldquo;concentrating on gratification&hellip; "
         "concentrating on drawbacks&rdquo; &mdash; the recurring "
         "contrast underlying every discourse in this chapter."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.53:1.1-1.7"),
        ("p", "&sect;2", "sn12.53:2.1-2.9"),
        ("p", "&sect;3", "sn12.53:3.1-3.6"),
        ("p", "&sect;4", "sn12.53:4.1-4.6"),
    ],
    quiz=[
        {"q": "How does this discourse's structure compare to SN 12.52's?",
         "opts": [
             "Identical two-part, attention-driven structure, with different vocabulary and a different simile",
             "A completely different, unrelated structure",
             "The reverse of SN 12.52's structure",
             "A much shorter summary omitting the simile entirely"],
         "correct": 0,
         "expl": "The same underlying mechanism, restated through new terms and image."},
        {"q": "What term does this discourse use in place of SN 12.52's \"things that fuel grasping\"?",
         "opts": [
             "\"Things that tighten the fetters\" (saṁyojaniyesu dhammesu)",
             "\"Things that cause illness\"",
             "\"Things forbidden to laypeople\"",
             "The same exact phrase as SN 12.52, unchanged"],
         "correct": 0,
         "expl": "A different name foregrounding the binding, restraining function of the same hazard."},
        {"q": "What simile replaces SN 12.52's great mass of fire?",
         "opts": [
             "An oil lamp, fed with oil and an adjusted wick",
             "A river in flood",
             "A tree bearing fruit",
             "A storm cloud"],
         "correct": 0,
         "expl": "A smaller, more domestic image making the same point."},
        {"q": "How is the oil lamp kept burning, according to this discourse?",
         "opts": [
             "By someone pouring in oil and adjusting the wick from time to time",
             "By constant, uninterrupted attention around the clock",
             "It burns forever without any maintenance",
             "By adding wood rather than oil"],
         "correct": 0,
         "expl": "Small, periodic maintenance, echoing SN 12.52's periodic feeding of the fire."},
        {"q": "How does the lamp go out, in the cessation half of this discourse?",
         "opts": [
             "Simply by not being fed, once its original fuel is used up",
             "By someone deliberately blowing it out",
             "By a sudden gust of wind",
             "It never goes out in this discourse"],
         "correct": 0,
         "expl": "The same extinguishing-through-absence formula as SN 12.52."},
        {"q": "What does reading this discourse together with SN 12.52 confirm?",
         "opts": [
             "That the teaching's mechanism doesn't depend on any particular image or vocabulary",
             "That the two discourses teach contradictory doctrines",
             "That one of the two discourses must be a later addition",
             "That fire and oil lamps have different effects on craving"],
         "correct": 0,
         "expl": "The mechanism being taught is attention itself, not the specific image used."},
        {"q": "What determines whether craving grows or ceases in this discourse, as in SN 12.52?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The specific type of fetter involved",
             "Whether the lamp is made of clay or metal",
             "How much oil is available"],
         "correct": 0,
         "expl": "The same lever as SN 12.52, unchanged by the shift in vocabulary and image."},
        {"q": "What happens to the chain of conditions once craving ceases in this discourse?",
         "opts": [
             "It unwinds in reverse, through grasping, continued existence, rebirth, to suffering's complete cessation",
             "Nothing further is described",
             "It reverses only partway",
             "A new, unrelated chain begins"],
         "correct": 0,
         "expl": "The same reverse chain as SN 12.52 and elsewhere in this saṃyutta."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("Two changes, one mechanism", [
            "new name, new image &mdash;",
            "the same lever underneath",
        ]),
        ("Fetters, not fuel for grasping", [
            "the same hazard, differently named &mdash;",
            "binding rather than feeding",
        ]),
        ("A smaller flame, the same lesson", [
            "oil and a wick, not a blazing pyre &mdash;",
            "ordinary upkeep, ordinary neglect",
        ]),
        ("Confirmed by repetition, not undermined", [
            "the image changes, the point doesn't &mdash;",
            "attention was always the real subject",
        ]),
    ],
    further=[
        '<a href="%s/sn12.53/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.52.html">SN 12.52 &middot; Grasping</a> '
        "&mdash; the discourse immediately before this one, the same "
        "structure told with a great mass of fire.",
        '<a href="sn-12.54.html">SN 12.54 &middot; Fetters (2nd)</a> '
        "&mdash; the next discourse, this same oil-lamp simile "
        "retold in more compressed form.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.54 — Dutiyasaṁyojanasutta
# --------------------------------------------------------------------------- #
page(
    12, 54, "Dutiyasaṁyojana", "Fetters (2nd)",
    meta_title="SN 12.54 — Fetters (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasaṁyojanasutta — the same oil-lamp teaching as SN "
        "12.53, folded from four movements into two by embedding the "
        "simile directly into each statement rather than restating "
        "it separately. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same oil-lamp teaching as SN 12.53, compressed "
                 "from four movements into two by folding the simile "
                 "directly into each statement"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as SN 12.53, more tightly "
                       "compressed"),
    ],
    why=(
        "This discourse carries exactly the same content as SN "
        "12.53 &mdash; the oil lamp fed by occasional oil and a "
        "tended wick, or left to go out once its fuel runs dry, "
        "illustrating craving's growth or cessation depending on "
        "attention &mdash; but restructures how that content is "
        "delivered. Where SN 12.53 gave a direct statement of the "
        "teaching first and only then introduced the simile as a "
        "second, separate movement, this discourse folds the simile "
        "directly into the opening statement from the start, "
        "collapsing what took four movements in SN 12.53 into just "
        "two. The change is purely a matter of arrangement: no "
        "content is added or removed, only the order and grouping in "
        "which the same material is presented."),
    guide=[
        ("The same content, a tighter arrangement", [
            "Every element present in SN 12.53 &mdash; the fetters "
            "framing, the oil lamp, the periodic feeding, the "
            "extinguishing through withheld fuel &mdash; reappears "
            "here unchanged; only the sequencing is different."]),
        ("Simile folded in from the start, not added afterward", [
            "SN 12.53 states the teaching plainly, then restates it "
            "a second time with the simile attached; this discourse "
            "opens directly with \"suppose an oil lamp,\" building "
            "the simile into the very first sentence rather than "
            "introducing it as a separate step."]),
        ("Four movements collapsed into two", [
            "SN 12.53's structure runs arising-alone, "
            "arising-with-simile, cessation-alone, "
            "cessation-with-simile; this discourse compresses that "
            "into arising-with-simile-already-included and "
            "cessation-with-simile-already-included, halving the "
            "number of distinct movements."]),
        ("A second confirmed instance of this specific compression style", [
            "This same fold-the-simile-in-from-the-start compression "
            "reappears later in this chapter for the great tree "
            "simile as well, in SN 12.56 relative to SN 12.55 "
            "&mdash; a recognizable pattern for how a \"(2nd)\" "
            "discourse in this chapter typically relates to its "
            "predecessor."]),
        ("Arrangement changed, substance untouched", [
            "Because no doctrinal content is gained or lost between "
            "the two discourses, this pairing demonstrates that this "
            "chapter's redactors treated the four-part and two-part "
            "arrangements as equally valid ways of presenting the "
            "identical teaching, not as different teachings in their "
            "own right."]),
    ],
    terms=[
        ("telañca paṭicca vaṭṭiñca paṭicca telappadīpo jhāyeyya",
         "&ldquo;suppose an oil lamp depended on oil and a wick to "
         "burn&rdquo; &mdash; the same simile as SN 12.53, now "
         "opening the discourse directly."),
        ("tadāhāro tadupādāno ciraṁ dīghamaddhānaṁ jaleyya",
         "&ldquo;fed and fuelled by that, the oil lamp would burn "
         "for a long time&rdquo; &mdash; the standard formula for "
         "what sustains the simile's image."),
        ("na kālena kālaṁ telaṁ āsiñceyya na vaṭṭiṁ upasaṁhareyya",
         "&ldquo;no-one would pour oil in and adjust the wick from "
         "time to time&rdquo; &mdash; the negated version of SN "
         "12.53's maintenance formula, opening this discourse's "
         "cessation half."),
        ("purimassa ca upādānassa pariyādānā aññassa ca anupahārā "
         "anāhāro nibbāyeyya",
         "&ldquo;as the original fuel is used up and no more is "
         "added, the oil lamp would be extinguished due to not "
         "being fed&rdquo; &mdash; the same extinguishing formula "
         "as SN 12.53."),
        ("saṁyojaniyesu&hellip; dhammesu",
         "&ldquo;things that tighten the fetters&rdquo; &mdash; "
         "the same framing as SN 12.53, carried over unchanged."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.54:1.1-1.7"),
        ("p", "&sect;2", "sn12.54:2.1-2.6"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to SN 12.53's?",
         "opts": [
             "Identical content, restructured into a more compressed arrangement",
             "Entirely different content on an unrelated topic",
             "A contradiction of SN 12.53's teaching",
             "An expansion adding new material not found in SN 12.53"],
         "correct": 0,
         "expl": "No content added or removed, only the sequencing changed."},
        {"q": "How does this discourse open, unlike SN 12.53?",
         "opts": [
             "Directly with the oil lamp simile, folded into the first statement",
             "With a direct statement and no simile at all",
             "With a question from a mendicant",
             "With a description of King Pasenadi's court"],
         "correct": 0,
         "expl": "The simile built into the opening sentence rather than introduced afterward."},
        {"q": "How many movements does this discourse compress SN 12.53's four movements into?",
         "opts": [
             "Two",
             "One",
             "Six",
             "The number of movements is unchanged"],
         "correct": 0,
         "expl": "Arising-with-simile and cessation-with-simile, each already combined."},
        {"q": "Where else in this chapter does this same compression style reappear?",
         "opts": [
             "SN 12.56, relative to SN 12.55's great tree simile",
             "Nowhere else in this chapter",
             "Only in the discourses addressed to brahmins",
             "In SN 12.51's opening inquiry"],
         "correct": 0,
         "expl": "A recognizable pattern for how a \"(2nd)\" discourse in this chapter relates to its predecessor."},
        {"q": "What does this pairing with SN 12.53 demonstrate?",
         "opts": [
             "That the four-part and two-part arrangements were treated as equally valid ways of presenting the same teaching",
             "That one of the two discourses must be doctrinally incorrect",
             "That the oil lamp simile was later replaced by a tree simile",
             "That compression always removes some doctrinal content"],
         "correct": 0,
         "expl": "Arrangement changed, substance untouched."},
        {"q": "What determines whether craving grows or ceases in this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The type of oil used in the lamp",
             "How large the wick is",
             "Whether the lamp is indoors or outdoors"],
         "correct": 0,
         "expl": "The same lever as SN 12.52 and SN 12.53, unchanged by the compression."},
        {"q": "How does the lamp go out in this discourse's cessation half?",
         "opts": [
             "Simply by not being fed, once its original fuel is used up",
             "By someone deliberately extinguishing it",
             "By a strong wind",
             "The lamp never goes out in this discourse"],
         "correct": 0,
         "expl": "The same extinguishing-through-absence formula as SN 12.53."},
        {"q": "What framing vocabulary does this discourse share with SN 12.53?",
         "opts": [
             "\"Things that tighten the fetters\" (saṁyojaniyesu dhammesu)",
             "\"Things that fuel grasping\" (upādāniyesu dhammesu)",
             "An entirely new, unrelated term",
             "No shared vocabulary at all"],
         "correct": 0,
         "expl": "Carried over unchanged from SN 12.53, distinguishing it from SN 12.52's grasping framing."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("The same lamp, differently arranged", [
            "no new content added &mdash;",
            "only the order rearranged",
        ]),
        ("Simile built in from the first word", [
            "not attached afterward &mdash;",
            "present from the opening sentence",
        ]),
        ("Four movements folded to two", [
            "arising and cessation, simile included &mdash;",
            "a tighter shape, the same substance",
        ]),
        ("A pattern confirmed a second time", [
            "the same fold seen again at SN 12.56 &mdash;",
            "how a \"(2nd)\" discourse tends to compress",
        ]),
    ],
    further=[
        '<a href="%s/sn12.54/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.53.html">SN 12.53 &middot; Fetters</a> '
        "&mdash; the discourse immediately before this one, the same "
        "teaching in its four-movement form.",
        '<a href="sn-12.55.html">SN 12.55 &middot; A Great Tree</a> '
        "&mdash; the next discourse, shifting from an oil lamp to a "
        "tree fed by its own roots.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.55 — Mahārukkhasutta
# --------------------------------------------------------------------------- #
page(
    12, 55, "Mahārukkha", "A Great Tree",
    meta_title="SN 12.55 — A Great Tree | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Mahārukkhasutta — the same attention-driven arising and "
        "cessation of craving as SN 12.52, now pictured as a great "
        "tree drawing sap through its own roots, or felled, "
        "uprooted, and reduced to scattered ash. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same four-movement structure as SN 12.52 and "
                 "SN 12.53, with a great tree in place of a fire or "
                 "lamp, its felling given in unusually vivid detail"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the most visually elaborate simile in this "
                       "chapter so far"),
    ],
    why=(
        "This discourse returns to SN 12.52's \"grasping\" framing "
        "and full four-movement structure, but replaces the fire "
        "with an image this chapter, and Sujato's English title for "
        "the whole chapter, is named after: a great tree, its roots "
        "reaching down and spreading sideways to draw sap upward, "
        "standing for a long time as long as it's fed. The felling "
        "half of the simile is given in unusually vivid, step-by-step "
        "detail &mdash; cut down at the roots, the roots dug up to "
        "the last fiber, the trunk chopped into splinters, dried in "
        "wind and sun, burned to ash, and the ash itself scattered "
        "in a strong wind or floated down a swift stream &mdash; a "
        "far more elaborate destruction sequence than the simpler "
        "extinguishing formulas used for the fire and the lamp."),
    guide=[
        ("The image the chapter is named for", [
            "Sujato's English title for this whole chapter, \"A "
            "Tree,\" most plausibly draws on this discourse and its "
            "close companions rather than on the chapter's literal "
            "Pali name, Dukkhavagga, which names suffering rather "
            "than any image at all."]),
        ("Roots reaching both down and sideways", [
            "The tree's feeding mechanism is described with unusual "
            "specificity &mdash; roots going downward and roots "
            "spreading across all draw sap upward together &mdash; "
            "giving the image a more complete botanical picture than "
            "the fire or lamp similes needed."]),
        ("A felling sequence far more elaborate than extinguishing a fire", [
            "Where the fire and lamp similes ended with a brief "
            "formula about fuel running out unfed, this discourse "
            "walks through cutting, digging up every root down to "
            "the fibers, chopping into splinters, drying, burning, "
            "and finally scattering the ashes &mdash; a full "
            "sequence of deliberate, effortful destruction rather "
            "than passive neglect."]),
        ("Destruction as active work, not simple withholding", [
            "Unlike the fire or lamp, which went out simply by not "
            "being fed, the tree requires someone to actively arrive "
            "with a spade and basket and carry out its felling "
            "step by step &mdash; cessation here is pictured as "
            "deliberate effort, not passive absence."]),
        ("A formula of totality closing the felling", [
            "\"Cut off at the root, made like a palm stump, "
            "obliterated, and unable to arise in the future\" is a "
            "stronger, more absolute description of finality than "
            "the fire and lamp similes' simple \"extinguished due to "
            "not being fed,\" matching the greater effort just "
            "described."]),
    ],
    terms=[
        ("seyyathāpi&hellip; mahārukkho",
         "&ldquo;suppose there was a great tree&rdquo; &mdash; the "
         "image this discourse and its companions are built "
         "around."),
        ("yāni ceva mūlāni adhogamāni, yāni ca tiriyaṅgamāni, "
         "sabbāni tāni uddhaṁ ojaṁ abhiharanti",
         "&ldquo;its roots going downwards and across all draw the "
         "sap upwards&rdquo; &mdash; the tree's feeding mechanism, "
         "described with unusual botanical detail."),
        ("mūle chindeyya&hellip; mūlāni uddhareyya antamaso "
         "usīranāḷimattānipi",
         "&ldquo;cut down at the roots, dig them up, and pull them "
         "out, down to the fibers and stems&rdquo; &mdash; the "
         "start of the felling sequence's unusual detail."),
        ("sakalikaṁ sakalikaṁ kareyya&hellip; agginā ḍaheyya&hellip; "
         "nadiyā vā sīghasotāya pavāheyya",
         "&ldquo;chop it into splinters&hellip; burn them with "
         "fire&hellip; float them away down a swift stream&rdquo; "
         "&mdash; the full destruction sequence, far more elaborate "
         "than the fire or lamp similes' endings."),
        ("ucchinnamūlo assa tālāvatthukato anabhāvaṅkato āyatiṁ "
         "anuppādadhammo",
         "&ldquo;cut off at the root, made like a palm stump, "
         "obliterated, and unable to arise in the future&rdquo; "
         "&mdash; a stronger, more absolute formula of finality "
         "than this chapter's earlier similes use."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.55:1.1-1.5"),
        ("p", "&sect;2", "sn12.55:2.1-2.6"),
        ("p", "&sect;3", "sn12.55:3.1-3.4"),
        ("p", "&sect;4", "sn12.55:4.1-4.10"),
    ],
    quiz=[
        {"q": "What image does this discourse use, replacing SN 12.52's fire and SN 12.53's lamp?",
         "opts": [
             "A great tree, fed by its own roots",
             "A river flowing to the sea",
             "A mountain being worn down by rain",
             "A candle in a windowless room"],
         "correct": 0,
         "expl": "The image this whole chapter's English title likely draws its name from."},
        {"q": "How does the tree's feeding mechanism get described?",
         "opts": [
             "Roots going downward and roots spreading sideways together draw sap upward",
             "The tree needs no roots at all in this simile",
             "It is fed only by rainfall from above",
             "It draws nutrients directly from sunlight alone"],
         "correct": 0,
         "expl": "An unusually specific botanical picture compared to the fire and lamp similes."},
        {"q": "How does the felling sequence in this discourse compare to the fire and lamp similes' endings?",
         "opts": [
             "Far more elaborate — cutting, digging up roots, chopping, drying, burning, and scattering ashes",
             "Much briefer, using only a single short phrase",
             "Identical in every detail to the fire simile's ending",
             "This discourse describes no felling or destruction at all"],
         "correct": 0,
         "expl": "A full sequence of deliberate, effortful destruction."},
        {"q": "How does the tree's destruction differ from the fire's or lamp's extinguishing?",
         "opts": [
             "It requires active, deliberate work rather than simple withholding of fuel",
             "It also happens through simple neglect, identically to the fire",
             "The tree cannot be destroyed at all in this simile",
             "It happens instantly with no described process"],
         "correct": 0,
         "expl": "Someone must actively arrive with a spade and basket to carry it out."},
        {"q": "What formula closes the description of the tree's destruction?",
         "opts": [
             "\"Cut off at the root, made like a palm stump, obliterated, and unable to arise in the future\"",
             "\"Extinguished due to not being fed\"",
             "\"The tree simply disappears without explanation\"",
             "No closing formula is given"],
         "correct": 0,
         "expl": "A stronger, more absolute statement of finality than the fire and lamp similes use."},
        {"q": "What framing does this discourse use, matching SN 12.52 rather than SN 12.53 or SN 12.54?",
         "opts": [
             "\"Things that fuel grasping\" (upādāniyesu dhammesu)",
             "\"Things that tighten the fetters\" (saṁyojaniyesu dhammesu)",
             "An entirely new framing not used elsewhere",
             "No framing vocabulary is used at all"],
         "correct": 0,
         "expl": "A return to SN 12.52's grasping framing rather than SN 12.53's fetters framing."},
        {"q": "How many movements structure this discourse?",
         "opts": [
             "Four — arising alone, arising with simile, cessation alone, cessation with simile",
             "Two, folded together like SN 12.54",
             "Six",
             "One continuous statement with no distinct movements"],
         "correct": 0,
         "expl": "The same four-part structure as SN 12.52 and SN 12.53, not the compressed two-part style."},
        {"q": "What determines whether craving grows or ceases in this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The species of tree involved",
             "How deep the roots grow",
             "The season in which the tree is examined"],
         "correct": 0,
         "expl": "The same lever as every other discourse in this chapter so far."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("The tree the chapter is named for", [
            "roots down, roots sideways &mdash;",
            "drawing sap upward together",
        ]),
        ("A felling given full detail", [
            "cut, dug up, chopped, dried, burned &mdash;",
            "far more than a fire going out",
        ]),
        ("Destruction as effort, not neglect", [
            "someone must arrive with spade and basket &mdash;",
            "not simply withheld fuel",
        ]),
        ("A stronger formula for the ending", [
            "\"like a palm stump\" &mdash; unable to arise again",
            "more absolute than \"extinguished, unfed\"",
        ]),
    ],
    further=[
        '<a href="%s/sn12.55/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.54.html">SN 12.54 &middot; Fetters (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.56.html">SN 12.56 &middot; A Great Tree (2nd)</a> '
        "&mdash; the next discourse, this same tree simile "
        "compressed into a shorter, more elided retelling.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.56 — Dutiyamahārukkhasutta
# --------------------------------------------------------------------------- #
page(
    12, 56, "Dutiyamahārukkha", "A Great Tree (2nd)",
    meta_title="SN 12.56 — A Great Tree (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyamahārukkhasutta — SN 12.55's great tree retold "
        "with two layers of compression at once, folding the simile "
        "into a single statement and eliding much of the felling "
        "sequence's own detail. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 12.55's great tree teaching compressed into two "
                 "movements, with the felling sequence itself also "
                 "elided partway through"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as SN 12.55, compressed "
                       "twice over"),
    ],
    why=(
        "This discourse relates to SN 12.55 exactly as SN 12.54 "
        "relates to SN 12.53: the same tree, drawing sap through "
        "roots reaching down and sideways, standing so long as it's "
        "fed, or felled and reduced to scattered ash once it isn't "
        "&mdash; but folded from four movements into two by building "
        "the simile into each statement from the start. This "
        "discourse goes a step further than SN 12.54 did, however: "
        "not only is the overall four-part structure compressed, but "
        "the felling sequence's own elaborate detail &mdash; cutting, "
        "digging, chopping, drying, burning, scattering &mdash; is "
        "itself elided with a peyyāla ellipsis partway through, "
        "leaving only its first and last steps stated in full. The "
        "result is a discourse compressed on two independent axes at "
        "once, not just one."),
    guide=[
        ("The same fold seen at SN 12.54, applied here", [
            "Exactly as SN 12.54 embedded the oil lamp simile "
            "directly into a single statement rather than restating "
            "it separately, this discourse embeds the great tree "
            "simile the same way, collapsing SN 12.55's four "
            "movements into two."]),
        ("A second, independent layer of compression", [
            "Beyond the structural fold shared with SN 12.54, this "
            "discourse also elides the felling sequence's own "
            "internal detail with a peyyāla ellipsis, jumping "
            "directly from cutting down the roots to floating the "
            "ashes downstream, where SN 12.55 spelled out every "
            "intervening step."]),
        ("Two compressions that don't have to travel together", [
            "SN 12.54 compressed its overall structure without "
            "eliding any of the oil lamp simile's own detail, since "
            "the lamp simile was already brief; this discourse shows "
            "that when the underlying simile is itself elaborate, "
            "both kinds of compression can be applied at once, "
            "independently of each other."]),
        ("What survives the double compression intact", [
            "Despite both layers of elision, the discourse still "
            "preserves the tree's feeding mechanism in full and the "
            "closing formula of finality &mdash; cut off at the "
            "root, made like a palm stump, obliterated &mdash; "
            "suggesting these two elements were judged too "
            "load-bearing to abbreviate even under heavy "
            "compression."]),
        ("A confirmed pattern across two pairs of \"2nd\" discourses", [
            "Between SN 12.53/12.54 and SN 12.55/12.56, this "
            "chapter now shows two separate confirmed cases of a "
            "\"(2nd)\" discourse folding its predecessor's simile "
            "into a tighter statement, with this second case adding "
            "an extra layer of internal elision the first case "
            "didn't need."]),
    ],
    terms=[
        ("yāni ceva mūlāni adhogamāni, yāni ca tiriyaṅgamāni, "
         "sabbāni tāni uddhaṁ ojaṁ abhiharanti",
         "&ldquo;its roots going downwards and across all draw the "
         "sap upwards&rdquo; &mdash; the same feeding mechanism as "
         "SN 12.55, preserved in full despite the compression "
         "elsewhere."),
        ("tadāhāro tadupādāno ciraṁ dīghamaddhānaṁ tiṭṭheyya",
         "&ldquo;fed and fuelled by that, the great tree would "
         "stand for a long time&rdquo; &mdash; the standard formula "
         "carried over unchanged from SN 12.55."),
        ("mūle chindeyya&hellip; mūlāni uddhareyya&hellip;pe&hellip; "
         "nadiyā vā sīghasotāya pavāheyya",
         "&ldquo;cut down at the roots, dig them up&hellip; float "
         "them away down a swift stream&rdquo; &mdash; the felling "
         "sequence's own internal detail elided here with a peyyāla "
         "ellipsis, unlike SN 12.55's full step-by-step version."),
        ("ucchinnamūlo assa tālāvatthukato anabhāvaṅkato āyatiṁ "
         "anuppādadhammo",
         "&ldquo;cut off at the root, made like a palm stump, "
         "obliterated, and unable to arise in the future&rdquo; "
         "&mdash; the closing formula of finality, preserved "
         "intact despite the compression around it."),
        ("upādāniyesu&hellip; dhammesu",
         "&ldquo;things that fuel grasping&rdquo; &mdash; the same "
         "framing as SN 12.55, carried over unchanged."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.56:1.1-1.7"),
        ("p", "&sect;2", "sn12.56:2.1-2.8"),
    ],
    quiz=[
        {"q": "How does this discourse relate to SN 12.55, structurally?",
         "opts": [
             "The same content, folded from four movements into two, as SN 12.54 does for SN 12.53",
             "An entirely different, unrelated teaching",
             "A direct contradiction of SN 12.55",
             "An expansion adding new content not found in SN 12.55"],
         "correct": 0,
         "expl": "The same fold-the-simile-in compression pattern seen at SN 12.54."},
        {"q": "What additional compression does this discourse apply, beyond the structural fold?",
         "opts": [
             "Eliding the felling sequence's own internal detail with a peyyāla ellipsis",
             "Removing the tree's feeding mechanism entirely",
             "Changing the framing from grasping to fetters",
             "No additional compression is applied"],
         "correct": 0,
         "expl": "A second, independent layer of compression not present in SN 12.54's relationship to SN 12.53."},
        {"q": "What does this discourse's felling sequence jump directly between?",
         "opts": [
             "Cutting down the roots and floating the ashes downstream, skipping the intervening steps",
             "Planting a new tree and watering it",
             "Two entirely different similes",
             "There is no felling sequence in this discourse at all"],
         "correct": 0,
         "expl": "A peyyāla ellipsis where SN 12.55 spelled out every step."},
        {"q": "What does this discourse demonstrate about compression that SN 12.54 alone didn't show?",
         "opts": [
             "That structural folding and internal elision can be applied independently of each other",
             "That compression always removes doctrinal content",
             "That SN 12.54's compression style was incorrect",
             "That similes can never be compressed at all"],
         "correct": 0,
         "expl": "Two compressions that don't have to travel together, shown here to co-occur."},
        {"q": "What survives this discourse's double compression intact?",
         "opts": [
             "The tree's feeding mechanism and the closing formula of finality",
             "Nothing; the entire teaching is reduced to a single sentence",
             "Only the setting and audience",
             "Only the framing vocabulary"],
         "correct": 0,
         "expl": "Elements judged too load-bearing to abbreviate even under heavy compression."},
        {"q": "How many confirmed cases of a \"(2nd)\" discourse folding its predecessor's simile does this chapter now show?",
         "opts": [
             "Two — SN 12.53/12.54 and SN 12.55/12.56",
             "Only one, this discourse alone",
             "None; this is not actually a compression",
             "Four separate cases"],
         "correct": 0,
         "expl": "A confirmed, recurring pattern across two separate pairs."},
        {"q": "What framing does this discourse use?",
         "opts": [
             "\"Things that fuel grasping\" (upādāniyesu dhammesu), matching SN 12.55",
             "\"Things that tighten the fetters\", matching SN 12.53",
             "An entirely new framing",
             "No framing vocabulary at all"],
         "correct": 0,
         "expl": "Carried over unchanged from SN 12.55."},
        {"q": "What determines whether craving grows or ceases in this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The size of the tree involved",
             "The season of the year",
             "How many people witness the felling"],
         "correct": 0,
         "expl": "The same lever as every other discourse in this chapter."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("The same fold, a second time", [
            "four movements into two &mdash;",
            "matching SN 12.54's earlier pattern",
        ]),
        ("A second layer of compression", [
            "the felling itself elided now &mdash;",
            "not just the overall shape",
        ]),
        ("Two compressions, independent of each other", [
            "structure folded, detail elided &mdash;",
            "neither one requiring the other",
        ]),
        ("What survives even so", [
            "the roots, the closing formula &mdash;",
            "too load-bearing to cut",
        ]),
    ],
    further=[
        '<a href="%s/sn12.56/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.55.html">SN 12.55 &middot; A Great Tree</a> '
        "&mdash; the discourse immediately before this one, the same "
        "simile in its full, unelided form.",
        '<a href="sn-12.57.html">SN 12.57 &middot; A Sapling</a> '
        "&mdash; the next discourse, a new image of a young tree "
        "nurtured to maturity rather than a mature tree already "
        "standing.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.57 — Taruṇarukkhasutta
# --------------------------------------------------------------------------- #
page(
    12, 57, "Taruṇarukkha", "A Sapling",
    meta_title="SN 12.57 — A Sapling | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Taruṇarukkhasutta — the same fetters teaching as SN "
        "12.53, now pictured through a young sapling actively "
        "nurtured toward maturity rather than a mature tree simply "
        "standing. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same four-movement structure as SN 12.53 and "
                 "SN 12.55, with a young sapling in place of a "
                 "mature tree"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a small but genuine shift in the tree "
                       "image's meaning"),
    ],
    why=(
        "This discourse returns to the fetters framing shared with "
        "SN 12.53, but introduces a new variation on this chapter's "
        "tree image: not a great tree already standing, drawing sap "
        "through established roots, but a sapling &mdash; a young "
        "tree still being brought toward maturity by someone who "
        "clears around its roots, supplies soil, and waters it from "
        "time to time. Fed this way, the sapling doesn't merely "
        "stand for a long time, as the great tree does; it grows, "
        "increases, and matures. The shift from a mature tree's "
        "static persistence to a young tree's active growth adds a "
        "genuinely new dimension to this chapter's central image, "
        "suggesting that what craving does when fed isn't only "
        "sustain itself but actively develop and expand."),
    guide=[
        ("A young tree, not a mature one already standing", [
            "Where SN 12.55's great tree was already fully grown and "
            "simply persisted so long as it was fed, this discourse's "
            "sapling is explicitly still developing, introducing a "
            "growth stage this chapter's tree imagery hadn't yet "
            "used."]),
        ("Active cultivation, not passive feeding", [
            "The sapling's care is described with more deliberate, "
            "gardener-like verbs &mdash; clearing around the roots, "
            "supplying soil, watering &mdash; than the simpler "
            "\"feeding\" language used for the fire, lamp, or "
            "mature tree, matching the more hands-on relationship a "
            "young plant requires."]),
        ("Growth as the outcome, not mere persistence", [
            "\"Vuddhiṁ virūḷhiṁ vepullaṁ āpajjeyya\" &mdash; grow, "
            "increase, and mature &mdash; describes an actively "
            "developing outcome, distinct from the great tree's "
            "simple \"stand for a long time\" or the fire and lamp's "
            "simple continued burning."]),
        ("A suggestion the tree simile alone hadn't made explicit", [
            "By showing craving's growth through a plant that is "
            "itself growing, this discourse makes a point the "
            "mature-tree and fire similes leave only implicit: fed "
            "craving doesn't just persist unchanged, it develops and "
            "expands over time."]),
        ("The same felling, applied to something still young", [
            "The cessation half applies this chapter's now-familiar "
            "felling sequence &mdash; cut down, dug up, chopped, "
            "dried, burned, scattered &mdash; to the sapling exactly "
            "as it was applied to the mature tree, showing that a "
            "young, still-developing growth is no more resistant to "
            "being uprooted than an established one."]),
    ],
    terms=[
        ("taruṇo rukkho",
         "&ldquo;a sapling&rdquo; &mdash; literally a young tree, "
         "introducing a growth stage this chapter's tree imagery "
         "hadn't yet used."),
        ("mūlāni palimajjeyya&hellip; paṁsuṁ dadeyya&hellip; udakaṁ "
         "dadeyya",
         "&ldquo;clear around the roots, supply soil, and water "
         "it&rdquo; &mdash; more deliberate, gardener-like care than "
         "this chapter's other similes describe."),
        ("vuddhiṁ virūḷhiṁ vepullaṁ āpajjeyya",
         "&ldquo;grow, increase, and mature&rdquo; &mdash; an "
         "actively developing outcome, distinct from the mature "
         "tree's simple persistence."),
        ("saṁyojaniyesu&hellip; dhammesu",
         "&ldquo;things that tighten the fetters&rdquo; &mdash; the "
         "same framing as SN 12.53."),
        ("ucchinnamūlo assa tālāvatthukato anabhāvaṅkato āyatiṁ "
         "anuppādadhammo",
         "&ldquo;cut off at the root, made like a palm stump, "
         "obliterated, and unable to arise in the future&rdquo; "
         "&mdash; the same formula of finality applied here to a "
         "young sapling rather than a mature tree."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.57:1.1-1.4"),
        ("p", "&sect;2", "sn12.57:2.1-2.6"),
        ("p", "&sect;3", "sn12.57:3.1-3.3"),
        ("p", "&sect;4", "sn12.57:4.1-4.7"),
    ],
    quiz=[
        {"q": "What new image does this discourse introduce to this chapter's tree simile?",
         "opts": [
             "A sapling — a young tree still being brought toward maturity",
             "A tree already dead and rotting",
             "A tree bearing fruit for the first time",
             "A tree struck by lightning"],
         "correct": 0,
         "expl": "A growth stage this chapter's imagery hadn't yet used."},
        {"q": "How is the sapling's care described, compared to the fire, lamp, or mature tree similes?",
         "opts": [
             "With more deliberate, gardener-like verbs — clearing roots, supplying soil, watering",
             "With identical language to the fire simile",
             "The sapling requires no care at all in this discourse",
             "Only with a single generic word for \"feeding\""],
         "correct": 0,
         "expl": "A more hands-on relationship matching what a young plant requires."},
        {"q": "What outcome does the sapling reach when fed, unlike the mature tree's simple persistence?",
         "opts": [
             "It grows, increases, and matures",
             "It stops growing entirely and remains fixed in size",
             "It withers despite being fed",
             "It transforms into a different kind of plant"],
         "correct": 0,
         "expl": "An actively developing outcome, distinct from mere standing."},
        {"q": "What point does this discourse make that the mature-tree and fire similes leave only implicit?",
         "opts": [
             "That fed craving doesn't just persist unchanged, but develops and expands over time",
             "That craving cannot grow under any circumstances",
             "That only mature practitioners experience craving",
             "That craving is entirely unrelated to attention"],
         "correct": 0,
         "expl": "Growth shown through a plant that is itself growing."},
        {"q": "What happens to the sapling in the cessation half of this discourse?",
         "opts": [
             "The same felling sequence used for the mature tree — cut down, dug up, chopped, burned, scattered",
             "It is left to grow indefinitely with no cessation described",
             "It is transplanted to a different location",
             "It simply stops growing without being felled"],
         "correct": 0,
         "expl": "A young, still-developing growth proves no more resistant to being uprooted than a mature one."},
        {"q": "What framing does this discourse use?",
         "opts": [
             "\"Things that tighten the fetters\" (saṁyojaniyesu dhammesu)",
             "\"Things that fuel grasping\" (upādāniyesu dhammesu)",
             "An entirely new framing not used elsewhere",
             "No framing vocabulary at all"],
         "correct": 0,
         "expl": "The same fetters framing as SN 12.53, matching this discourse to that side of the chapter's pairing."},
        {"q": "How many movements structure this discourse?",
         "opts": [
             "Four — arising alone, arising with simile, cessation alone, cessation with simile",
             "Two, folded together like SN 12.54 and SN 12.56",
             "Six",
             "One continuous statement with no distinct movements"],
         "correct": 0,
         "expl": "The full four-part structure, not the compressed two-part style used for this chapter's \"(2nd)\" discourses."},
        {"q": "What determines whether craving grows or ceases in this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The age of the tree involved",
             "The type of soil used",
             "How much water is available"],
         "correct": 0,
         "expl": "The same lever as every other discourse in this chapter."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("A young tree, not one already grown", [
            "still being brought toward maturity &mdash;",
            "a new stage in the chapter's imagery",
        ]),
        ("Cultivation, not just feeding", [
            "cleared roots, soil, water &mdash;",
            "a gardener's hands-on care",
        ]),
        ("Growth as the outcome this time", [
            "not merely standing, but maturing &mdash;",
            "craving shown actively developing",
        ]),
        ("No more resistant for being young", [
            "the same felling applies &mdash;",
            "a sapling uprooted as easily as a great tree",
        ]),
    ],
    further=[
        '<a href="%s/sn12.57/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.56.html">SN 12.56 &middot; A Great Tree (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.58.html">SN 12.58 &middot; Name and Form</a> '
        "&mdash; the next discourse, shifting from craving's growth "
        "to the conception of name and form itself.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.58 — Nāmarūpasutta
# --------------------------------------------------------------------------- #
page(
    12, 58, "Nāmarūpa", "Name and Form",
    meta_title="SN 12.58 — Name and Form | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Nāmarūpasutta — this chapter's tree simile applied not "
        "to craving's growth but to the conception of name and form "
        "itself, moving the point of feeding one full step earlier "
        "in the chain. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same four-movement, great-tree structure as "
                 "SN 12.55, with name and form's conception in place "
                 "of craving's growth"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a genuine shift in what the tree simile is "
                       "applied to, not just a new image"),
    ],
    why=(
        "Every discourse in this chapter so far has applied its "
        "simile to craving's growth or cessation. This discourse "
        "moves the point of application one full step earlier in "
        "the chain: rather than concentrating on gratification "
        "making craving grow, it says concentrating on gratification "
        "makes name and form be conceived (nāmarūpassa avakkanti "
        "hoti) &mdash; the same language of a being's \"descent\" "
        "into a new existence already used in SN 12.39. The great "
        "tree simile returns unchanged, but what it now illustrates "
        "isn't craving's persistence but the very entry point of a "
        "new existence taking shape, tying this chapter's central "
        "image directly back to the mechanics of rebirth examined "
        "earlier in this book."),
    guide=[
        ("The tree simile, redirected to a different target", [
            "The great tree's feeding mechanism &mdash; roots "
            "reaching down and sideways, drawing sap upward &mdash; "
            "is repeated here word for word from SN 12.55, but what "
            "it now illustrates has shifted from craving's growth to "
            "name and form's conception."]),
        ("A phrase reaching back to SN 12.39", [
            "\"Nāmarūpassa avakkanti\" &mdash; name and form's "
            "descent &mdash; is the identical phrase already used in "
            "SN 12.39's account of what happens once consciousness "
            "is established and grows, tying this discourse directly "
            "to that earlier discourse's mechanics of rebirth."]),
        ("One step earlier in the chain than this chapter's other similes", [
            "Where SN 12.52 through SN 12.57 all locate the tree "
            "simile's lesson at the level of craving, this discourse "
            "moves it upstream to name and form itself, the point at "
            "which a new existence's basic constituents first take "
            "shape."]),
        ("Fetters framing carried over, not grasping", [
            "This discourse shares SN 12.53, SN 12.54, and SN "
            "12.57's \"things that tighten the fetters\" framing "
            "rather than SN 12.52 and SN 12.55's \"things that fuel "
            "grasping,\" a detail worth tracking alongside which "
            "simile is used, since the two variables don't always "
            "move together."]),
        ("A tree simile applied to something more abstract than craving", [
            "Craving is at least experientially familiar as "
            "something that grows or fades; name and form's "
            "conception is a more abstract, structural event, and "
            "applying the same concrete tree image to it suggests "
            "the simile's real subject was always the general "
            "mechanism of conditioned arising, not craving "
            "specifically."]),
    ],
    terms=[
        ("nāmarūpassa avakkanti hoti",
         "&ldquo;name and form are conceived&rdquo; &mdash; "
         "literally name and form's descent, the same phrase used "
         "in SN 12.39 for what follows consciousness's "
         "establishment."),
        ("nāmarūpapaccayā saḷāyatanaṁ",
         "&ldquo;name and form are requirements for the six sense "
         "fields&rdquo; &mdash; where the familiar downstream chain "
         "resumes after this discourse's point of entry."),
        ("nāmarūpassa avakkanti na hoti",
         "&ldquo;name and form are not conceived&rdquo; &mdash; the "
         "negated version opening the cessation half."),
        ("nāmarūpanirodhā saḷāyatananirodho",
         "&ldquo;when name and form cease, the six sense fields "
         "cease&rdquo; &mdash; the reverse chain resuming from this "
         "discourse's point of entry."),
        ("saṁyojaniyesu&hellip; dhammesu",
         "&ldquo;things that tighten the fetters&rdquo; &mdash; the "
         "framing shared with SN 12.53, SN 12.54, and SN 12.57, "
         "distinct from the grasping framing of the tree similes in "
         "SN 12.55 and SN 12.56."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.58:1.1-1.4"),
        ("p", "&sect;2", "sn12.58:2.1-2.4"),
        ("p", "&sect;3", "sn12.58:3.1-3.3"),
        ("p", "&sect;4", "sn12.58:4.1-4.6"),
    ],
    quiz=[
        {"q": "What does this discourse say happens when attention concentrates on gratification, unlike this chapter's earlier discourses?",
         "opts": [
             "Name and form are conceived, rather than craving simply growing",
             "The tree immediately dies",
             "Nothing at all; this discourse describes no arising",
             "The mendicant achieves awakening automatically"],
         "correct": 0,
         "expl": "The point of application shifted one step earlier in the chain."},
        {"q": "What earlier discourse in this saṃyutta uses the identical phrase \"nāmarūpassa avakkanti\"?",
         "opts": [
             "SN 12.39, describing what follows consciousness's establishment",
             "SN 12.1, the opening statement of dependent origination",
             "SN 12.15, on existence and non-existence",
             "No earlier discourse uses this phrase"],
         "correct": 0,
         "expl": "A direct textual link back to the Intention discourses' rebirth mechanics."},
        {"q": "Which tree simile does this discourse reuse?",
         "opts": [
             "The great tree simile from SN 12.55, word for word",
             "An entirely new simile not used elsewhere",
             "The sapling simile from SN 12.57",
             "The oil lamp simile from SN 12.53"],
         "correct": 0,
         "expl": "The same feeding mechanism, redirected to a different target."},
        {"q": "What framing does this discourse use?",
         "opts": [
             "\"Things that tighten the fetters\" (saṁyojaniyesu dhammesu)",
             "\"Things that fuel grasping\" (upādāniyesu dhammesu)",
             "An entirely new framing not seen elsewhere",
             "No framing vocabulary at all"],
         "correct": 0,
         "expl": "Matching SN 12.53, SN 12.54, and SN 12.57 rather than the grasping framing of the tree similes."},
        {"q": "What does applying the tree simile to name and form's conception suggest about the simile's real subject?",
         "opts": [
             "That the simile was always about the general mechanism of conditioned arising, not craving specifically",
             "That the simile only ever applies to craving and nothing else",
             "That name and form and craving are entirely unrelated concepts",
             "That this discourse is a scribal error unrelated to the rest of the chapter"],
         "correct": 0,
         "expl": "A more abstract, structural event illustrated by the same concrete image."},
        {"q": "Where does the downstream chain resume after this discourse's point of entry?",
         "opts": [
             "At the six sense fields, conditioned by name and form",
             "At old age and death directly",
             "At ignorance",
             "The chain does not resume; the discourse ends at name and form"],
         "correct": 0,
         "expl": "The familiar chain continuing from where this discourse enters it."},
        {"q": "How many movements structure this discourse?",
         "opts": [
             "Four — arising alone, arising with simile, cessation alone, cessation with simile",
             "Two, folded together",
             "Six",
             "One continuous statement"],
         "correct": 0,
         "expl": "The same four-part structure as SN 12.55 and SN 12.57."},
        {"q": "What determines whether name and form are conceived or not, in this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The species of tree used in the simile",
             "Whether the mendicant is ordained or a layperson",
             "The time of day the teaching is given"],
         "correct": 0,
         "expl": "The same attention-driven lever as every other discourse in this chapter."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("The same tree, a different target", [
            "not craving's growth this time &mdash;",
            "but name and form conceived",
        ]),
        ("A phrase reaching back", [
            "nāmarūpassa avakkanti &mdash;",
            "the same words as SN 12.39",
        ]),
        ("One step earlier in the chain", [
            "upstream of craving altogether &mdash;",
            "at the point a new existence takes shape",
        ]),
        ("The simile's real subject revealed", [
            "not craving alone, but conditioning itself &mdash;",
            "the tree standing for the mechanism, not the feeling",
        ]),
    ],
    further=[
        '<a href="%s/sn12.58/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.57.html">SN 12.57 &middot; A Sapling</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.39.html">SN 12.39 &middot; Intention (2nd)</a> '
        "&mdash; the earlier discourse using the identical phrase "
        "for name and form's descent.",
        '<a href="sn-12.59.html">SN 12.59 &middot; Consciousness</a> '
        "&mdash; the next discourse, moving the same tree simile "
        "one further step upstream to consciousness itself.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.59 — Viññāṇasutta
# --------------------------------------------------------------------------- #
page(
    12, 59, "Viññāṇa", "Consciousness",
    meta_title="SN 12.59 — Consciousness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Viññāṇasutta — this chapter's tree simile pushed one "
        "further step upstream than SN 12.58, now applied to "
        "consciousness's own conception rather than name and form's. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same four-movement, great-tree structure as "
                 "SN 12.58, with consciousness's conception in place "
                 "of name and form's"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the furthest upstream this chapter's tree "
                       "simile is pushed"),
    ],
    why=(
        "This discourse takes the shift SN 12.58 made and pushes it "
        "one step further. Where SN 12.58 applied the tree simile to "
        "name and form's conception, this discourse applies it to "
        "consciousness's own conception (viññāṇassa avakkanti hoti) "
        "&mdash; the very earliest point in the downstream chain the "
        "tree simile is used for anywhere in this saṃyutta. The "
        "downstream chain then resumes with consciousness "
        "conditioning name and form, exactly reversing SN 12.58's "
        "entry point one link further back. Heavily elided even by "
        "this chapter's compressed standards, the discourse reads "
        "almost as a template: the same tree, the same "
        "attention-driven mechanism, moved one more notch toward the "
        "chain's root."),
    guide=[
        ("One further step upstream than SN 12.58", [
            "Exactly as SN 12.58 moved the tree simile's target from "
            "craving to name and form, this discourse moves it again "
            "from name and form to consciousness itself, the "
            "earliest point in the chain this simile is applied to "
            "anywhere in this saṃyutta."]),
        ("The downstream chain resuming one link earlier", [
            "Where SN 12.58 continued with name and form conditioning "
            "the six sense fields, this discourse continues with "
            "consciousness conditioning name and form, showing the "
            "same reverse-chain logic simply shifted one position "
            "back."]),
        ("The most heavily elided discourse in this pairing", [
            "Even the tree's own feeding mechanism, spelled out in "
            "SN 12.55 and SN 12.58 alike, is elided here with a "
            "peyyāla ellipsis, making this the most compressed member "
            "of the great-tree family of similes in this chapter."]),
        ("A small variant in the reverse formula's wording", [
            "The reverse chain's opening phrase appears in two "
            "slightly different forms across this discourse &mdash; "
            "\"viññāṇanirodhā\" in one place and \"viññāṇassa "
            "nirodhā\" in another &mdash; a minor wording variation "
            "this reading guide notes rather than silently "
            "smoothing over."]),
        ("Three discourses, one simile, three points of entry", [
            "Read together, SN 12.55, SN 12.58, and this discourse "
            "show the same great tree simile applied at three "
            "distinct points &mdash; craving, name and form, and "
            "consciousness &mdash; confirming that the image itself "
            "was never tied to any single link, only to the general "
            "shape of something fed or starved by attention."]),
    ],
    terms=[
        ("viññāṇassa avakkanti hoti",
         "&ldquo;consciousness is conceived&rdquo; &mdash; the "
         "earliest point in the chain this chapter's tree simile is "
         "applied to, one step upstream of SN 12.58's name and "
         "form."),
        ("viññāṇapaccayā nāmarūpaṁ",
         "&ldquo;consciousness is a requirement for name and "
         "form&rdquo; &mdash; where the downstream chain resumes, "
         "one link earlier than SN 12.58's entry point."),
        ("viññāṇassa avakkanti na hoti",
         "&ldquo;consciousness is not conceived&rdquo; &mdash; the "
         "negated version opening the cessation half."),
        ("viññāṇanirodhā nāmarūpanirodho",
         "&ldquo;when consciousness ceases, name and form "
         "cease&rdquo; &mdash; appearing later in the discourse in "
         "the slightly different form &ldquo;viññāṇassa "
         "nirodhā,&rdquo; a minor wording variation this guide notes "
         "rather than smooths over."),
        ("saṁyojaniyesu&hellip; dhammesu",
         "&ldquo;things that tighten the fetters&rdquo; &mdash; the "
         "same framing as SN 12.58."),
    ],
    text_intro=(
        "The discourse in full, heavily elided even by this "
        "chapter's compressed standards. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.59:1.1-1.4"),
        ("p", "&sect;2", "sn12.59:2.1-2.3"),
        ("p", "&sect;3", "sn12.59:3.1-3.3"),
        ("p", "&sect;4", "sn12.59:4.1-4.6"),
    ],
    quiz=[
        {"q": "What does this discourse apply the tree simile to, one step earlier than SN 12.58?",
         "opts": [
             "Consciousness's own conception",
             "Old age and death directly",
             "The six sense fields",
             "Ignorance itself"],
         "correct": 0,
         "expl": "The earliest point in the chain this simile is applied to anywhere in this saṃyutta."},
        {"q": "Where does the downstream chain resume after this discourse's point of entry?",
         "opts": [
             "At name and form, conditioned by consciousness",
             "At the six sense fields directly",
             "At craving",
             "At rebirth"],
         "correct": 0,
         "expl": "One link earlier than SN 12.58's entry point at name and form."},
        {"q": "How does this discourse's use of elision compare to SN 12.55 and SN 12.58?",
         "opts": [
             "More heavily elided, even eliding the tree's own feeding mechanism",
             "Less elided, spelling out every detail in full",
             "Identically elided, with no difference at all",
             "This discourse contains no elision whatsoever"],
         "correct": 0,
         "expl": "The most compressed member of the great-tree family of similes in this chapter."},
        {"q": "What minor wording variation does this reading guide note in the reverse formula?",
         "opts": [
             "\"Viññāṇanirodhā\" appears in one place and \"viññāṇassa nirodhā\" in another",
             "The discourse uses two completely different words for consciousness",
             "The Pali and English versions contradict each other",
             "No variation is noted; the wording is perfectly consistent"],
         "correct": 0,
         "expl": "Noted honestly rather than silently smoothed over."},
        {"q": "What do SN 12.55, SN 12.58, and this discourse together demonstrate about the great tree simile?",
         "opts": [
             "That it was never tied to any single link, only to the general shape of something fed or starved by attention",
             "That the simile only ever applies to consciousness",
             "That the three discourses teach contradictory doctrines",
             "That the tree simile was abandoned after SN 12.55"],
         "correct": 0,
         "expl": "The same image applied at three distinct points in the chain."},
        {"q": "What framing does this discourse use?",
         "opts": [
             "\"Things that tighten the fetters\" (saṁyojaniyesu dhammesu)",
             "\"Things that fuel grasping\" (upādāniyesu dhammesu)",
             "An entirely new framing",
             "No framing vocabulary at all"],
         "correct": 0,
         "expl": "The same framing as SN 12.58, immediately before it."},
        {"q": "How many movements structure this discourse?",
         "opts": [
             "Four — arising alone, arising with simile, cessation alone, cessation with simile",
             "Two, folded together",
             "Six",
             "One continuous statement"],
         "correct": 0,
         "expl": "The same four-part structure as SN 12.58, though each movement is more heavily elided."},
        {"q": "What determines whether consciousness is conceived or not, in this discourse?",
         "opts": [
             "Whether attention dwells on gratification or on drawbacks",
             "The height of the tree in the simile",
             "Whether the mendicant has taken formal ordination",
             "The season of the year"],
         "correct": 0,
         "expl": "The same attention-driven lever running through every discourse in this chapter."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with most of this chapter's discourses."},
    ],
    marginalia=[
        ("One step further upstream still", [
            "not name and form, but consciousness &mdash;",
            "the earliest point this simile reaches",
        ]),
        ("The chain resumed one link earlier", [
            "consciousness conditioning name and form &mdash;",
            "the same reversal, shifted back",
        ]),
        ("The most compressed telling yet", [
            "even the tree's own detail elided &mdash;",
            "a template more than a full picture",
        ]),
        ("Three points, one recurring image", [
            "craving, name and form, consciousness &mdash;",
            "the tree standing for the shape, not the link",
        ]),
    ],
    further=[
        '<a href="%s/sn12.59/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.58.html">SN 12.58 &middot; Name and Form</a> '
        "&mdash; the discourse immediately before this one, applying "
        "the same simile one link later in the chain.",
        '<a href="sn-12.60.html">SN 12.60 &middot; Causation</a> '
        "&mdash; the next discourse, closing this chapter with "
        "Ānanda's famous remark and the Buddha's equally famous "
        "reply.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.60 — Nidānasutta
# --------------------------------------------------------------------------- #
page(
    12, 60, "Nidāna", "Causation",
    meta_title="SN 12.60 — Causation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Nidānasutta — closing Dukkhavagga, Ānanda's offhand "
        "remark that dependent origination seems plain as day meets "
        "the Buddha's famous rebuke and the image of humanity "
        "tangled like a knotted ball of thread. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Kammāsadamma, a town among the Kurus"),
        ("Speakers", "The Buddha and Venerable Ānanda"),
        ("Form", "A famous opening exchange, followed by this "
                 "chapter's now-familiar great-tree teaching in its "
                 "full four-movement form"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "a famous opening exchange closing this "
                       "chapter on its most quoted note"),
    ],
    why=(
        "Closing Dukkhavagga, this discourse opens with one of the "
        "most quoted exchanges in the early texts. Ānanda remarks to "
        "the Buddha that dependent origination, despite being deep "
        "and appearing deep, seems to him as plain as can be. The "
        "Buddha's reply is immediate and emphatic: not so, Ānanda, "
        "not so &mdash; this teaching is genuinely deep, and it's "
        "precisely because people fail to understand and penetrate "
        "it that humanity remains tangled like string, knotted like "
        "a ball of thread, matted like rushes and reeds, unable to "
        "escape the lower realms and the whole cycle of transmigration. "
        "Only after this exchange does the discourse turn to "
        "material this chapter has made familiar &mdash; the great "
        "tree fed by its own roots, felled and scattered when "
        "starved &mdash; set here not at the usual Sāvatthī but among "
        "the Kurus, at Kammāsadamma."),
    guide=[
        ("An admission, not a boast", [
            "Ānanda's remark isn't framed as arrogance; it reads as "
            "an honest, almost puzzled admission that a teaching "
            "everyone describes as profound doesn't strike him that "
            "way, making the Buddha's correction land as a genuine "
            "clarification rather than a public rebuke."]),
        ("A doubled denial for emphasis", [
            "\"Mā hevaṁ, ānanda, mā hevaṁ, ānanda\" &mdash; not so, "
            "Ānanda, not so, Ānanda &mdash; repeats the same denial "
            "twice in immediate succession, a level of emphasis this "
            "saṃyutta rarely uses elsewhere."]),
        ("A three-part image of human entanglement", [
            "Tangled like string, knotted like a ball of thread, "
            "matted like rushes and reeds &mdash; three distinct "
            "images of confusion and binding, stacked together "
            "rather than relying on any single metaphor to carry the "
            "point."]),
        ("Real stakes named directly, not left abstract", [
            "The consequence of failing to understand this teaching "
            "isn't described as mere confusion; it's named directly "
            "as not escaping the places of loss, the bad places, the "
            "underworld, and transmigration &mdash; the same lower "
            "realms named in SN 12.41's declaration of stream-entry."]),
        ("A familiar teaching, given weight by an unfamiliar setting", [
            "Once the exchange with Ānanda ends, the discourse "
            "delivers the same great-tree teaching already given in "
            "SN 12.55, in the same full four-movement form, but "
            "relocates it to Kammāsadamma among the Kurus rather than "
            "the chapter's usual Sāvatthī, a rare change of setting "
            "that gives even this familiar material a distinct "
            "occasion."]),
    ],
    terms=[
        ("acchariyaṁ, bhante, abbhutaṁ, bhante",
         "&ldquo;it's incredible, sir! It's amazing&rdquo; &mdash; "
         "Ānanda's opening exclamation, framing an honest remark "
         "rather than a challenge."),
        ("gambhīro cāyaṁ paṭiccasamuppādo gambhīrāvabhāso ca, "
         "atha ca pana me uttānakuttānako viya khāyati",
         "&ldquo;this dependent origination is deep and appears "
         "deep, yet to me it seems as plain as can be&rdquo; "
         "&mdash; the remark that draws the Buddha's famous "
         "correction."),
        ("mā hevaṁ, ānanda, mā hevaṁ, ānanda",
         "&ldquo;not so, Ānanda! Not so, Ānanda!&rdquo; &mdash; a "
         "doubled denial, an unusual degree of emphasis in this "
         "saṃyutta."),
        ("tantākulakajātā kulagaṇṭhikajātā muñjapabbajabhūtā",
         "&ldquo;tangled like string, knotted like a ball of "
         "thread, and matted like rushes and reeds&rdquo; &mdash; "
         "three stacked images of human entanglement."),
        ("apāyaṁ duggatiṁ vinipātaṁ saṁsāraṁ nātivattati",
         "&ldquo;doesn't escape the places of loss, the bad places, "
         "the underworld, transmigration&rdquo; &mdash; the "
         "consequence of not understanding this teaching, named "
         "directly rather than left abstract."),
    ],
    text_intro=(
        "The discourse in full, closing Dukkhavagga. The chapter's "
        "closing verse of discourse titles is not translated in the "
        "source and is not quoted here; see the reading guide above "
        "for its contents. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.60:1.1-1.4"),
        ("p", "&sect;2", "sn12.60:2.1-2.3"),
        ("p", "&sect;3", "sn12.60:3.1-3.6"),
        ("p", "&sect;4", "sn12.60:4.1-4.7"),
        ("p", "&sect;5", "sn12.60:5.1-5.4"),
        ("p", "&sect;6", "sn12.60:6.1-6.13"),
    ],
    quiz=[
        {"q": "What does Ānanda remark to the Buddha at the start of this discourse?",
         "opts": [
             "That dependent origination, though called deep, seems to him as plain as can be",
             "That he has fully understood the four noble truths",
             "That he wishes to disrobe and return to lay life",
             "That he disagrees with the Buddha's teaching on rebirth"],
         "correct": 0,
         "expl": "An honest admission, not a boast or a challenge."},
        {"q": "How does the Buddha respond to Ānanda's remark?",
         "opts": [
             "With a doubled denial — \"not so, Ānanda! Not so, Ānanda!\"",
             "By agreeing that it is indeed simple",
             "By remaining silent",
             "By asking another mendicant to respond instead"],
         "correct": 0,
         "expl": "An unusual level of emphasis for this saṃyutta."},
        {"q": "What three images does the Buddha use to describe humanity's confusion?",
         "opts": [
             "Tangled like string, knotted like a ball of thread, matted like rushes and reeds",
             "Lost like a traveler without a map",
             "Blind like someone born without sight",
             "Drowning like a swimmer caught in a current"],
         "correct": 0,
         "expl": "Three distinct images stacked together rather than a single metaphor."},
        {"q": "What consequence does the Buddha name for failing to understand this teaching?",
         "opts": [
             "Not escaping the places of loss, the bad places, the underworld, and transmigration",
             "Losing the respect of other mendicants",
             "Being unable to recite scripture correctly",
             "The discourse names no specific consequence"],
         "correct": 0,
         "expl": "The same lower realms named in SN 12.41's declaration of stream-entry."},
        {"q": "What teaching does the discourse turn to after the exchange with Ānanda?",
         "opts": [
             "The great tree simile already given in SN 12.55, in its full form",
             "An entirely new teaching not found elsewhere in this chapter",
             "The catechism from SN 12.51",
             "No further teaching follows; the discourse ends with the exchange"],
         "correct": 0,
         "expl": "Familiar material given weight by the exchange preceding it."},
        {"q": "Where is this discourse set, unlike most of this chapter's other discourses?",
         "opts": [
             "Kammāsadamma, a town among the Kurus",
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, at the Bamboo Grove",
             "Kapilavatthu, the Buddha's home city"],
         "correct": 0,
         "expl": "A rare change of setting from this chapter's usual Sāvatthī."},
        {"q": "How is the great tree teaching's structure in this discourse, compared to SN 12.55?",
         "opts": [
             "The same full four-movement form",
             "Compressed into two movements, unlike SN 12.55",
             "Reduced to a single sentence",
             "Expanded with additional new movements not in SN 12.55"],
         "correct": 0,
         "expl": "The full, unelided structure rather than the compressed style of this chapter's \"(2nd)\" discourses."},
        {"q": "How does this discourse handle its closing verse of discourse titles?",
         "opts": [
             "It is untranslated in the source and not quoted in the text section",
             "It is fully translated and quoted in the text section",
             "This discourse has no closing verse at all",
             "The closing verse is translated but placed in a footnote"],
         "correct": 0,
         "expl": "Following the same convention used for untranslated closing material elsewhere in this saṃyutta."},
        {"q": "What chapter does this discourse close?",
         "opts": [
             "Dukkhavagga",
             "Gahapativagga",
             "Kaḷārakhattiyavagga",
             "Mahāvagga"],
         "correct": 0,
         "expl": "The sixth chapter of Nidānavagga, named for suffering though Sujato's English title calls it \"A Tree.\""},
        {"q": "Who are the two speakers in this discourse?",
         "opts": [
             "The Buddha and Venerable Ānanda",
             "The Buddha and Venerable Sāriputta",
             "The Buddha and a visiting brahmin",
             "The Buddha and King Pasenadi"],
         "correct": 0,
         "expl": "A direct exchange between teacher and attendant, unusual for this chapter."},
    ],
    marginalia=[
        ("An honest remark, not a boast", [
            "\"it seems plain to me\" &mdash;",
            "puzzlement, not arrogance",
        ]),
        ("A denial doubled for weight", [
            "\"not so, Ānanda! Not so!\" &mdash;",
            "emphasis rare in this saṃyutta",
        ]),
        ("Three images of the same tangle", [
            "string, thread, matted reeds &mdash;",
            "no single metaphor enough",
        ]),
        ("A familiar tree, an unfamiliar place", [
            "Kammāsadamma, not Sāvatthī &mdash;",
            "old material, new occasion",
        ]),
    ],
    further=[
        '<a href="%s/sn12.60/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.59.html">SN 12.59 &middot; Consciousness</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.55.html">SN 12.55 &middot; A Great Tree</a> '
        "&mdash; the earlier discourse giving the same tree teaching "
        "this discourse repeats, without the exchange with Ānanda.",
        '<a href="sn-12.41.html">SN 12.41 &middot; Fears and Enmities</a> '
        "&mdash; opening the previous chapter with the same lower "
        "realms this discourse warns of escaping.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.62 — Dutiyaassutavāsutta
# --------------------------------------------------------------------------- #
page(
    12, 62, "Dutiyaassutavā", "Unlearned (2nd)",
    meta_title="SN 12.62 — Unlearned (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaassutavāsutta — the body persists for decades "
        "while the mind arises and ceases all day and all night, "
        "and a learned disciple traces even this constant churn "
        "back through dependent origination. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A restatement of SN 12.61's body-versus-mind "
                 "argument without its monkey simile, followed by a "
                 "noble disciple's response applying dependent "
                 "origination to feeling itself"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the same claim as SN 12.61, extended further"),
    ],
    why=(
        "This discourse restates the argument already made in SN "
        "12.61 &mdash; that the body made of the four principal "
        "states is easier to release than what's called mind, "
        "sentience, or consciousness, precisely because the mind "
        "changes so much more constantly &mdash; but without the "
        "monkey swinging through the forest that makes SN 12.61's "
        "version so memorable. Instead it makes the same point with "
        "a starker comparison: the body can last a year, two years, "
        "ten, fifty, even a hundred years or more, while that which "
        "is called mind arises as one thing and ceases as another "
        "all day and all night. Having established this, the "
        "discourse turns to what a learned noble disciple does about "
        "it: not simply noting the mind's instability, but applying "
        "dependent origination to trace exactly how pleasant, "
        "painful, and neutral feelings arise from contact and cease "
        "when that contact ceases, illustrated by the ordinary "
        "image of heat generated by rubbing two sticks together."),
    guide=[
        ("The same claim, a different vehicle", [
            "SN 12.61 makes its case for the mind's instability "
            "using the monkey image; this discourse makes exactly "
            "the same case using only a direct comparison of "
            "durations, without any animal or forest involved."]),
        ("A body given a full range of possible lifespans", [
            "Rather than simply saying the body \"lasts a long "
            "time,\" the discourse lists out a year, two, three, "
            "four, five, ten, twenty, thirty, forty, fifty, a "
            "hundred years, or even longer, giving the comparison "
            "concrete, escalating weight before contrasting it with "
            "the mind's day-and-night churn."]),
        ("From a claim about instability to a method for working with it", [
            "Where the first half of the discourse simply "
            "establishes that the mind changes constantly, the "
            "second half shows what a learned noble disciple "
            "actually does in response: applying the mind carefully "
            "and rationally to dependent origination itself, tracing "
            "feeling specifically back to its condition."]),
        ("Feeling traced to contact, not to some deeper mystery", [
            "Pleasant, painful, and neutral feeling are each said to "
            "arise dependent on their corresponding kind of contact, "
            "and to cease when that contact ceases &mdash; a modest, "
            "almost mechanical account rather than an appeal to "
            "anything hidden or metaphysical."]),
        ("An ordinary friction fire replacing the monkey's forest", [
            "Two sticks rubbed together generate heat and produce "
            "fire; parted and set aside, that same heat ceases and "
            "stops &mdash; a domestic, easily observed image "
            "standing in for feeling's arising and ceasing, in "
            "keeping with this discourse's generally plainer, less "
            "vivid style compared to SN 12.61."]),
    ],
    terms=[
        ("imasmiṁ cātumahābhūtikasmiṁ kāyasmiṁ",
         "&ldquo;this body made up of the four principal "
         "states&rdquo; &mdash; the body, contrasted throughout with "
         "what's called mind, sentience, or consciousness."),
        ("etaṁ mama, esohamasmi, eso me attā",
         "&ldquo;this is mine, I am this, this is my self&rdquo; "
         "&mdash; the identity-view formula naming why the mind is "
         "harder to release than the body."),
        ("rattiyā ca divasassa ca aññadeva uppajjati aññaṁ "
         "nirujjhati",
         "&ldquo;arises as one thing and ceases as another all day "
         "and all night&rdquo; &mdash; the mind's constant churn, "
         "contrasted with the body's decades-long persistence."),
        ("dvinnaṁ kaṭṭhānaṁ saṅghaṭṭanasamodhānā usmā jāyati "
         "tejo abhinibbattati",
         "&ldquo;when you rub two sticks together, heat is "
         "generated and fire is produced&rdquo; &mdash; the domestic "
         "image standing in for feeling's arising and ceasing."),
        ("evaṁ passaṁ&hellip; sutavā ariyasāvako phassepi "
         "nibbindati, vedanāyapi nibbindati",
         "&ldquo;seeing this, a learned noble disciple grows "
         "disillusioned with contact, feeling&hellip;&rdquo; "
         "&mdash; the closing movement from understanding to "
         "liberation."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.62:1.1-1.10"),
        ("p", "&sect;2", "sn12.62:2.1-2.4"),
        ("p", "&sect;3", "sn12.62:3.1-3.9"),
        ("p", "&sect;4", "sn12.62:4.1-4.6"),
        ("p", "&sect;5", "sn12.62:5.1-5.3"),
    ],
    quiz=[
        {"q": "What claim does this discourse repeat from SN 12.61?",
         "opts": [
             "That the body is easier to release than the mind, because the mind changes far more constantly",
             "That the mind is easier to release than the body",
             "That neither the body nor the mind can ever be released",
             "That the body and mind are identical in every respect"],
         "correct": 0,
         "expl": "The same argument as SN 12.61, without its monkey simile."},
        {"q": "How long does the discourse say the body can last?",
         "opts": [
             "A year, several years, ten, fifty, a hundred years, or even longer",
             "Only a single day",
             "Exactly one year, with no variation",
             "The discourse gives no specific durations"],
         "correct": 0,
         "expl": "A concrete, escalating range of possible lifespans."},
        {"q": "How is the mind described, by contrast?",
         "opts": [
             "It arises as one thing and ceases as another all day and all night",
             "It persists unchanged for a hundred years, like the body",
             "It cannot be observed at all",
             "It changes only once per year"],
         "correct": 0,
         "expl": "Constant churn, contrasted with the body's long persistence."},
        {"q": "What does the discourse say pleasant, painful, and neutral feelings arise dependent on?",
         "opts": [
             "Their corresponding kind of contact",
             "The phase of the moon",
             "A person's social status",
             "The discourse doesn't specify a cause"],
         "correct": 0,
         "expl": "A modest, mechanical account rather than an appeal to anything hidden."},
        {"q": "What image illustrates feeling's arising and ceasing in this discourse?",
         "opts": [
             "Rubbing two sticks together to generate heat and fire",
             "A monkey swinging branch to branch",
             "A great tree drawing sap through its roots",
             "An ocean surging and receding"],
         "correct": 0,
         "expl": "A domestic, easily observed image in keeping with this discourse's plainer style."},
        {"q": "What does a learned noble disciple do, according to this discourse's second half?",
         "opts": [
             "Applies the mind carefully and rationally to dependent origination, tracing feeling to its condition",
             "Simply avoids thinking about feeling altogether",
             "Rejects the teaching on dependent origination",
             "Focuses exclusively on the body's decline"],
         "correct": 0,
         "expl": "A method for working with the mind's instability, not just an observation about it."},
        {"q": "What does the discourse say an unlearned ordinary person would be better off doing?",
         "opts": [
             "Taking the body to be their self, rather than the mind",
             "Taking the mind to be their self, rather than the body",
             "Rejecting the idea of a self entirely",
             "Taking both body and mind equally as self"],
         "correct": 0,
         "expl": "Not an endorsement of identity view, but a comparison of which mistake is less entrenched."},
        {"q": "What five things does a learned noble disciple grow disillusioned with, at the discourse's close?",
         "opts": [
             "Contact, feeling, perception, choices, and consciousness",
             "Only the body itself",
             "Only feeling",
             "The Buddha, the teaching, and the Saṅgha"],
         "correct": 0,
         "expl": "Contact plus four of the five aggregates, form having already been addressed earlier."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with SN 12.61 and much of this chapter."},
    ],
    marginalia=[
        ("The same claim, no monkey this time", [
            "just durations set side by side &mdash;",
            "a hundred years against a single night",
        ]),
        ("A body given its full range", [
            "one year, ten, fifty, a hundred &mdash;",
            "concrete weight before the contrast lands",
        ]),
        ("From observation to method", [
            "not just noting the mind's churn &mdash;",
            "tracing feeling to its condition",
        ]),
        ("An ordinary fire, plainly made", [
            "two sticks rubbed, then set apart &mdash;",
            "heat that simply stops",
        ]),
    ],
    further=[
        '<a href="%s/sn12.62/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.61.html">SN 12.61 &middot; Unlearned</a> '
        "&mdash; this book's already-published companion discourse, "
        "making the same argument with the monkey simile.",
        '<a href="sn-12.63.html">SN 12.63 &middot; A Child’s Flesh</a> '
        "&mdash; the next discourse, turning to the four fuels that "
        "sustain existence.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.63 — Puttamaṁsasutta
# --------------------------------------------------------------------------- #
page(
    12, 63, "Puttamaṁsa", "A Child’s Flesh",
    meta_title="SN 12.63 — A Child’s Flesh | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Puttamaṁsasutta — one of the most disturbing and famous "
        "similes in the canon, a couple crossing a desert forced to "
        "eat their own child to survive, opens a teaching on the "
        "four fuels that sustain all existence. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Four fuels named, each unpacked through its own "
                 "vivid, escalating simile"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; "
                       "&mdash; contains one of this canon's most "
                       "disturbing images, presented without "
                       "flinching"),
    ],
    why=(
        "This discourse names four fuels (āhāra) that maintain all "
        "sentient beings already born and support those about to be "
        "born: edible food, contact, mental intention, and "
        "consciousness. Each is unpacked through its own simile, and "
        "the first is among the most unflinching in the early texts: "
        "a couple crossing a desert with their only child, whose "
        "supplies run out partway across, and who kill and eat that "
        "child's flesh &mdash; grieving as they do it, crying out "
        "\"where are you, our only child?\" &mdash; simply to survive "
        "the remaining distance. The point isn't shock for its own "
        "sake; it's to establish exactly how physical food should be "
        "regarded &mdash; as bare necessity, never for pleasure, "
        "adornment, or indulgence &mdash; before the discourse moves "
        "through three further, almost equally vivid images for "
        "contact, mental intention, and consciousness as fuels."),
    guide=[
        ("A disturbing image used deliberately, not gratuitously", [
            "The couple's grief is described directly &mdash; they "
            "cry out for their child even as they eat &mdash; and "
            "the discourse doesn't soften or skip past this, because "
            "the whole force of the simile depends on food here "
            "being reduced to bare, joyless necessity, never "
            "pleasure."]),
        ("A question that pins down the simile's point", [
            "The Buddha doesn't simply state the moral; he asks the "
            "mendicants directly whether the couple would eat that "
            "food for fun, indulgence, adornment, or decoration, and "
            "only after they answer no does he confirm this is "
            "exactly how edible food should be regarded."]),
        ("Three further fuels, each with its own escalating image", [
            "A flayed cow bitten by creatures wherever she stands "
            "illustrates contact's inescapable vulnerability; a pit "
            "of glowing coals a person is dragged toward illustrates "
            "intention's aim to escape at all costs; being struck "
            "with three hundred spears a day illustrates "
            "consciousness's sheer weight as something borne, not "
            "chosen."]),
        ("Each fuel's understanding unlocking a specific further understanding", [
            "The discourse doesn't simply say understanding each "
            "fuel is good in general; it specifies exactly what "
            "completely understanding each one unlocks &mdash; "
            "desire for the five sensual stimulations, the three "
            "feelings, the three cravings, and name and form, in "
            "turn."]),
        ("Four fuels moving from the coarse to the subtle", [
            "The sequence itself is worth noticing: edible food is "
            "the coarsest and most physical of the four, contact "
            "less so, mental intention more subtle still, and "
            "consciousness the most fundamental, each fuel's simile "
            "growing correspondingly starker as the fuel itself "
            "grows more foundational."]),
    ],
    terms=[
        ("cattārome&hellip; āhārā bhūtānaṁ vā sattānaṁ ṭhitiyā "
         "sambhavesīnaṁ vā anuggahāya",
         "&ldquo;these four fuels maintain sentient beings that "
         "have been born and help those about to be born&rdquo; "
         "&mdash; the discourse's opening statement of its subject."),
        ("puttamaṁsāni khādantā",
         "&ldquo;eating their child's flesh&rdquo; &mdash; the "
         "central, unflinching image of the first simile."),
        ("kabaḷīkāre&hellip; āhāre pariññāte pañca kāmaguṇiko "
         "rāgo pariññāto hoti",
         "&ldquo;when edible food is completely understood, desire "
         "for the five kinds of sensual stimulation is completely "
         "understood&rdquo; &mdash; what understanding the first "
         "fuel unlocks."),
        ("gāvī niccammā",
         "&ldquo;a flayed cow&rdquo; &mdash; the image for contact "
         "as fuel, bitten by creatures wherever she stands."),
        ("aṅgārakāsu&hellip; vītaccikānaṁ vītadhūmānaṁ",
         "&ldquo;a pit of glowing coals&hellip; that neither flamed "
         "nor smoked&rdquo; &mdash; the image for mental intention "
         "as fuel."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.63:1.1-1.5"),
        ("p", "&sect;2", "sn12.63:2.1-2.12"),
        ("p", "&sect;3", "sn12.63:3.1-3.8"),
        ("p", "&sect;4", "sn12.63:4.1-4.9"),
        ("p", "&sect;5", "sn12.63:5.1-5.11"),
        ("p", "&sect;6", "sn12.63:6.1-6.24"),
    ],
    quiz=[
        {"q": "What four fuels does this discourse name?",
         "opts": [
             "Edible food, contact, mental intention, and consciousness",
             "Wealth, fame, pleasure, and power",
             "Earth, water, fire, and air",
             "Faith, generosity, patience, and wisdom"],
         "correct": 0,
         "expl": "The four āhāra that maintain existing beings and support those about to be born."},
        {"q": "What does the couple in the first simile do to survive crossing the desert?",
         "opts": [
             "Kill and eat their only child, grieving as they do it",
             "Turn back and abandon the crossing",
             "Find an oasis with abundant food",
             "Ration their remaining supplies successfully without further hardship"],
         "correct": 0,
         "expl": "One of the most unflinching images in the early texts, presented without softening."},
        {"q": "Why does the Buddha ask whether the couple would eat that food for fun or indulgence?",
         "opts": [
             "To pin down the point that edible food should be regarded only as bare necessity",
             "To test whether the mendicants were paying attention",
             "To introduce an unrelated topic about desert survival",
             "The question has no particular point"],
         "correct": 0,
         "expl": "The mendicants' answer of \"no\" confirms exactly how food should be regarded."},
        {"q": "What image illustrates contact as fuel?",
         "opts": [
             "A flayed cow, bitten by creatures wherever she stands",
             "A bird flying freely through the sky",
             "A river flowing to the sea",
             "A lamp burning steadily"],
         "correct": 0,
         "expl": "Contact's inescapable vulnerability, illustrated concretely."},
        {"q": "What image illustrates mental intention as fuel?",
         "opts": [
             "A person being dragged toward a pit of glowing coals",
             "A person planting a garden",
             "A person building a house",
             "A person reading a book"],
         "correct": 0,
         "expl": "Intention's aim to escape at all costs, made vivid."},
        {"q": "What image illustrates consciousness as fuel?",
         "opts": [
             "A criminal struck with a hundred spears three times a day",
             "A criminal released without punishment",
             "A criminal given a fair trial",
             "A criminal who escapes custody"],
         "correct": 0,
         "expl": "Consciousness's sheer weight as something borne, not chosen."},
        {"q": "What does understanding contact as fuel unlock, according to this discourse?",
         "opts": [
             "Complete understanding of the three feelings",
             "Complete understanding of the four noble truths directly",
             "Immediate rebirth in a heavenly realm",
             "Nothing further; contact stands alone"],
         "correct": 0,
         "expl": "Each fuel's understanding is said to unlock a specific further understanding."},
        {"q": "How does the sequence of the four fuels move, according to this reading guide?",
         "opts": [
             "From the coarse and physical to the subtle and fundamental",
             "From the subtle to the coarse",
             "In no particular order",
             "Randomly, with no discernible progression"],
         "correct": 0,
         "expl": "Edible food is coarsest; consciousness is most foundational."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears, though the mendicants respond to his questions."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with much of this chapter."},
    ],
    marginalia=[
        ("A necessity, never a pleasure", [
            "eaten in grief, not indulgence &mdash;",
            "the point food is meant to make",
        ]),
        ("A cow with nowhere safe to stand", [
            "bitten wherever she goes &mdash;",
            "contact's inescapable exposure",
        ]),
        ("An intention bent entirely on escape", [
            "dragged toward the glowing pit &mdash;",
            "wanting only to get away",
        ]),
        ("A weight borne, not chosen", [
            "three hundred spears a day &mdash;",
            "consciousness as something suffered",
        ]),
    ],
    further=[
        '<a href="%s/sn12.63/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.62.html">SN 12.62 &middot; Unlearned (2nd)</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.64.html">SN 12.64 &middot; If There Is Desire</a> '
        "&mdash; the next discourse, tracing how desire for these "
        "same four fuels leads consciousness into a new existence.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 12.64 — Atthirāgasutta
# --------------------------------------------------------------------------- #
page(
    12, 64, "Atthirāga", "If There Is Desire",
    meta_title="SN 12.64 — If There Is Desire | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Atthirāgasutta — desire for any of SN 12.63's four "
        "fuels gives consciousness somewhere to land and grow, "
        "illustrated by a painter creating a figure and a sunbeam "
        "seeking a wall to land on. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The same four fuels as SN 12.63, now traced "
                 "forward into a full chain toward rebirth, and in "
                 "reverse toward its absence, each illustrated by "
                 "its own simile"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; "
                       "&mdash; a precise mechanical account, dense "
                       "with repetition by design"),
    ],
    why=(
        "Where SN 12.63 named the four fuels and showed how each "
        "should be regarded, this discourse traces what happens when "
        "desire, relishing, and craving attach to any one of them: "
        "consciousness becomes established there and grows, name and "
        "form are conceived, choices grow, and the whole sequence "
        "runs forward into future rebirth, old age, death, and the "
        "grief that follows. Two similes make the mechanism vivid. "
        "An artist creating a full human figure on a polished plank "
        "using ordinary dyes illustrates how consciousness, given "
        "desire to work with, actively constructs a new existence "
        "rather than merely persisting. A ray of morning sunlight "
        "entering a window and searching for a wall, then the "
        "ground, then water to land on &mdash; landing nowhere at "
        "all if none of these exist &mdash; illustrates the reverse: "
        "consciousness needs something to become established on, and "
        "without desire providing that foothold, it simply doesn't "
        "take hold."),
    guide=[
        ("The same four fuels, now given their consequence", [
            "SN 12.63 taught how to regard edible food, contact, "
            "mental intention, and consciousness; this discourse "
            "picks up exactly where that left off, showing what "
            "happens specifically when desire attaches to any one of "
            "them."]),
        ("A precise chain, not a vague warning", [
            "The sequence from desire to suffering is spelled out "
            "step by step &mdash; consciousness established and "
            "growing, name and form conceived, choices growing, "
            "regeneration into a new existence, rebirth, old age and "
            "death &mdash; a mechanism, not a general caution."]),
        ("An artist actively constructing, not passively persisting", [
            "The painter simile emphasizes construction: dye applied "
            "to a polished plank produces \"the form of a woman or a "
            "man, whole in its major and minor limbs,\" a deliberate "
            "act of making something new, paralleling how "
            "consciousness given desire to work with doesn't simply "
            "continue but actively takes shape in a new existence."]),
        ("A sunbeam that needs somewhere to land", [
            "The second simile inverts the logic: light entering a "
            "window will land on a wall, or failing that the ground, "
            "or failing that water, and only fails to land anywhere "
            "if none of these supports exist &mdash; a precise image "
            "for consciousness needing an object to become "
            "established on, absent which it simply has nowhere to "
            "take hold."]),
        ("The same structure run twice, for presence and absence", [
            "Every step of the arising sequence is mirrored exactly "
            "in reverse for its absence &mdash; no desire, no "
            "establishment, no conception, no growth, no rebirth, no "
            "sorrow &mdash; giving the discourse a rigorously "
            "symmetrical shape across all four fuels in both "
            "directions."]),
    ],
    terms=[
        ("atthi rāgo atthi nandī atthi taṇhā, patiṭṭhitaṁ tattha "
         "viññāṇaṁ virūḷhaṁ",
         "&ldquo;if there is desire, relishing, and craving, "
         "consciousness becomes established there and grows&rdquo; "
         "&mdash; the discourse's key mechanism, repeated for each "
         "of the four fuels."),
        ("nāmarūpassa avakkanti",
         "&ldquo;name and form are conceived&rdquo; &mdash; the "
         "same phrase used in SN 12.39 and SN 12.58, marking the "
         "next step once consciousness is established."),
        ("āyatiṁ punabbhavābhinibbatti",
         "&ldquo;regeneration into a new state of existence in the "
         "future&rdquo; &mdash; the same term used in SN 12.38 and "
         "SN 12.39 for what follows established, growing "
         "consciousness."),
        ("rajako vā cittakārako&hellip; itthirūpaṁ vā purisarūpaṁ "
         "vā abhinimmineyya",
         "&ldquo;an artist or painter&hellip; would create the form "
         "of a woman or a man&rdquo; &mdash; the image of active "
         "construction, not passive persistence."),
        ("vātapānena rasmi pavisitvā kvāssa patiṭṭhitā",
         "&ldquo;a ray of light enters through a window, where "
         "would it land?&rdquo; &mdash; the image of consciousness "
         "needing somewhere to become established."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.64:1.1-1.5"),
        ("p", "&sect;2", "sn12.64:2.1-2.6"),
        ("p", "&sect;3", "sn12.64:3.1-3.8"),
        ("p", "&sect;4", "sn12.64:4.1-4.7"),
        ("p", "&sect;5", "sn12.64:5.1-5.8"),
        ("p", "&sect;6", "sn12.64:6.1-6.6"),
        ("p", "&sect;7", "sn12.64:7.1-7.8"),
        ("p", "&sect;8", "sn12.64:8.1-8.9"),
        ("p", "&sect;9", "sn12.64:9.1-9.8"),
    ],
    quiz=[
        {"q": "What happens when desire, relishing, and craving attach to one of the four fuels?",
         "opts": [
             "Consciousness becomes established there and grows",
             "The fuel is immediately destroyed",
             "Nothing happens; desire has no effect on consciousness",
             "The mendicant automatically achieves awakening"],
         "correct": 0,
         "expl": "The discourse's key mechanism, repeated for each fuel."},
        {"q": "What follows once consciousness is established and grows?",
         "opts": [
             "Name and form are conceived",
             "The chain immediately ends with no further consequence",
             "The body dissolves instantly",
             "The mendicant loses all memory"],
         "correct": 0,
         "expl": "The same phrase used in SN 12.39 and SN 12.58 for this step."},
        {"q": "What does the painter simile emphasize?",
         "opts": [
             "Active construction — consciousness given desire actively takes shape in a new existence",
             "Passive, unchanging persistence with no activity involved",
             "The impossibility of ever creating anything new",
             "A warning against practicing visual art"],
         "correct": 0,
         "expl": "A deliberate act of making, paralleling consciousness's role given desire to work with."},
        {"q": "What does the sunbeam simile illustrate?",
         "opts": [
             "Consciousness needing somewhere to become established, just as light needs a surface to land on",
             "The literal physics of how sunlight travels",
             "That windows should always face east",
             "That consciousness can exist without any support at all"],
         "correct": 0,
         "expl": "Absent a wall, the ground, or water, the light simply doesn't land anywhere."},
        {"q": "How is the reverse sequence structured, when there is no desire for the fuels?",
         "opts": [
             "Every step is mirrored exactly in reverse — no establishment, no conception, no rebirth, no sorrow",
             "The reverse sequence bears no relation to the forward one",
             "Only some steps are reversed, with others left unexplained",
             "The discourse doesn't describe a reverse sequence at all"],
         "correct": 0,
         "expl": "A rigorously symmetrical structure across all four fuels in both directions."},
        {"q": "How does this discourse relate to SN 12.63?",
         "opts": [
             "It picks up where SN 12.63 left off, showing the consequence of desire for the same four fuels",
             "It contradicts SN 12.63's teaching on the four fuels",
             "It introduces an entirely unrelated set of fuels",
             "It has no relationship to SN 12.63 at all"],
         "correct": 0,
         "expl": "The same four fuels — edible food, contact, mental intention, consciousness — given their consequence."},
        {"q": "What is the final result of the forward chain described in this discourse?",
         "opts": [
             "Future rebirth, old age, and death, full of sorrow, anguish, and distress",
             "Immediate liberation from suffering",
             "A pleasant, painless existence with no further consequence",
             "The discourse doesn't specify a final result"],
         "correct": 0,
         "expl": "The chain's endpoint, stated directly rather than left implicit."},
        {"q": "What term does this discourse share with SN 12.38 and SN 12.39 for what follows established, growing consciousness?",
         "opts": [
             "\"Regeneration into a new state of existence in the future\" (āyatiṁ punabbhavābhinibbatti)",
             "\"Complete liberation\"",
             "\"Eternal rest\"",
             "No shared terminology appears"],
         "correct": 0,
         "expl": "The same mechanism already examined from a different angle in the Intention discourses."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears, though the mendicants respond briefly."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with SN 12.63, immediately before it."},
    ],
    marginalia=[
        ("Desire giving consciousness a foothold", [
            "not neutral, but a place to land &mdash;",
            "established, then growing",
        ]),
        ("A figure built, not merely continued", [
            "dye on a polished plank &mdash;",
            "a new existence actively shaped",
        ]),
        ("A ray searching for somewhere to land", [
            "wall, then ground, then water &mdash;",
            "or nowhere, if none of these exist",
        ]),
        ("The same chain, mirrored exactly", [
            "presence and absence, step for step &mdash;",
            "no desire, no foothold, no sorrow",
        ]),
    ],
    further=[
        '<a href="%s/sn12.64/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.63.html">SN 12.63 &middot; A Child’s Flesh</a> '
        "&mdash; the discourse immediately before this one, naming "
        "the same four fuels.",
        '<a href="sn-12.39.html">SN 12.39 &middot; Intention (2nd)</a> '
        "&mdash; the earlier discourse examining the same "
        "consciousness-to-rebirth mechanism from the angle of "
        "intention rather than desire for the fuels.",
        '<a href="sn-12.65.html">SN 12.65 &middot; The City</a> '
        "&mdash; this book's already-published companion discourse, "
        "the Buddha's first-person account of discovering this same "
        "chain before his awakening.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.66 — Sammasasutta
# --------------------------------------------------------------------------- #
page(
    12, 66, "Sammasa", "Probing Within",
    meta_title="SN 12.66 — Probing Within | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sammasasutta — set among the Kurus, a mendicant's "
        "unsatisfying answer prompts the Buddha to trace suffering "
        "not through the familiar twelve links but through a "
        "distinct chain to attachment and craving, closing on a "
        "poisoned goblet offered to a dying-of-thirst traveler. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kammāsadamma, a town among the Kurus"),
        ("Speakers", "The Buddha, an unnamed mendicant, and Venerable "
                     "Ānanda"),
        ("Form", "A brief unsatisfying exchange, Ānanda's "
                 "intervention, then a probing chain to attachment "
                 "and craving illustrated by a threefold time "
                 "analysis and a poison simile"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; "
                       "&mdash; a distinct analytical chain and a "
                       "psychologically rich closing simile"),
    ],
    why=(
        "Set at Kammāsadamma among the Kurus &mdash; the same "
        "distinctive setting as SN 12.60's exchange with Ānanda "
        "&mdash; this discourse opens with the Buddha asking whether "
        "the mendicants \"probe within,\" and a mendicant's confident "
        "but unsatisfying answer, which Ānanda has to step in to "
        "rescue by asking the Buddha to teach the matter himself. "
        "What follows traces suffering back not through the full "
        "twelve-link chain but through a shorter, distinct sequence "
        "&mdash; old age and death traced to attachment (upadhi), "
        "attachment traced to craving, craving located precisely at "
        "whatever in the world seems nice and pleasant, starting at "
        "the six senses. A threefold analysis across past, future, "
        "and present ascetics and brahmins shows how seeing pleasant "
        "things as permanent, pleasurable, self, healthy, and safe "
        "grows craving into suffering, while seeing them as "
        "impermanent, painful, not-self, diseased, and dangerous lets "
        "craving go &mdash; illustrated by a beautiful, "
        "poisoned drink offered to someone dying of thirst, drunk "
        "recklessly by one traveler and refused, after reflection, "
        "by another."),
    guide=[
        ("An answer that doesn't satisfy, corrected by intervention", [
            "The discourse doesn't simply present a teaching; it "
            "opens with a mendicant's confident but unsatisfying "
            "attempt, which the Buddha's silence implicitly rejects, "
            "and which only Ānanda's direct request &mdash; \"now is "
            "the time!\" &mdash; manages to redirect toward a proper "
            "answer."]),
        ("A distinct chain, not the familiar twelve links", [
            "\"Probing\" here traces old age and death directly to "
            "attachment (upadhi), and attachment directly to craving "
            "&mdash; a shorter, more targeted sequence than the full "
            "twelve-link chain, built for locating exactly where "
            "craving takes hold rather than for tracing every "
            "intervening condition."]),
        ("Craving located precisely, not left vague", [
            "Rather than describing craving abstractly, the "
            "discourse names exactly where it arises and settles: "
            "whatever in the world seems nice and pleasant, run "
            "through each of the six senses in turn, giving craving "
            "a concrete address rather than treating it as free-floating."]),
        ("Three tenses, one identical mechanism", [
            "Past, future, and present ascetics and brahmins are "
            "each run through the same sequence &mdash; seeing "
            "pleasant things as permanent, pleasurable, self, "
            "healthy, safe, and growing craving, attachment, and "
            "suffering as a result &mdash; making explicit that this "
            "isn't a historical curiosity but a mechanism operating "
            "identically at every point in time."]),
        ("A drink that looks and tastes wonderful, and kills anyway", [
            "The poisoned goblet isn't disguised as poison; it has a "
            "genuinely nice color, aroma, and flavor, making the "
            "point that what destroys through craving typically "
            "presents itself as entirely appealing, and that the "
            "difference between the traveler who drinks recklessly "
            "and the one who reflects and refuses is exactly the "
            "difference this discourse is teaching."]),
    ],
    terms=[
        ("sammasatha no tumhe&hellip; antaraṁ sammasan",
         "&ldquo;do you probe within?&rdquo; &mdash; the Buddha's "
         "opening question, met first with an unsatisfying answer."),
        ("upadhinidānaṁ upadhisamudayaṁ upadhijātikaṁ "
         "upadhipabhavaṁ",
         "&ldquo;the source of this suffering is attachment&rdquo; "
         "&mdash; the distinct, shorter chain this discourse traces, "
         "naming upadhi directly rather than the full twelve links."),
        ("yaṁ loke piyarūpaṁ sātarūpaṁ etthesā taṇhā "
         "uppajjamānā uppajjati",
         "&ldquo;craving arises and settles on whatever in the "
         "world seems nice and pleasant&rdquo; &mdash; craving given "
         "a concrete address at each of the six senses."),
        ("niccato&hellip; sukhato&hellip; attato&hellip; "
         "ārogyato&hellip; khemato addakkhuṁ",
         "&ldquo;saw&hellip; as permanent, as pleasurable, as self, "
         "as healthy, and as safe&rdquo; &mdash; the fivefold "
         "misperception that grows craving, run through past, "
         "future, and present alike."),
        ("āpānīyakaṁso vaṇṇasampanno gandhasampanno "
         "rasasampanno&hellip; visena saṁsaṭṭho",
         "&ldquo;a bronze goblet of beverage that had a nice color, "
         "aroma, and flavor&hellip; mixed with poison&rdquo; "
         "&mdash; the closing simile, drunk recklessly by one "
         "traveler and refused, after reflection, by another."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.66:1.1-1.12"),
        ("p", "&sect;2", "sn12.66:2.1-2.6"),
        ("p", "&sect;3", "sn12.66:3.1-3.9"),
        ("p", "&sect;4", "sn12.66:4.1-4.7"),
        ("p", "&sect;5", "sn12.66:5.1-5.11"),
        ("p", "&sect;6", "sn12.66:6.1-8.5"),
        ("p", "&sect;7", "sn12.66:9.1-9.16"),
        ("p", "&sect;8", "sn12.66:10.1-12.5"),
        ("p", "&sect;9", "sn12.66:13.1-13.17"),
        ("p", "&sect;10", "sn12.66:14.1-14.6"),
    ],
    quiz=[
        {"q": "What question does the Buddha open this discourse with?",
         "opts": [
             "\"Do you probe within?\"",
             "\"Do you understand the four noble truths?\"",
             "\"Have you attained awakening?\"",
             "\"Where were you born?\""],
         "correct": 0,
         "expl": "A question one mendicant answers unsatisfyingly at first."},
        {"q": "Who intervenes to redirect the teaching toward a proper answer?",
         "opts": [
             "Venerable Ānanda",
             "Venerable Sāriputta",
             "King Pasenadi",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "Ānanda's \"now is the time!\" request prompts the Buddha to teach directly."},
        {"q": "What does this discourse trace old age and death to, rather than the full twelve-link chain?",
         "opts": [
             "Attachment (upadhi), traced in turn to craving",
             "Ignorance directly, with no intervening links",
             "The six sense fields alone",
             "This discourse doesn't trace old age and death to anything"],
         "correct": 0,
         "expl": "A shorter, more targeted sequence built for locating where craving takes hold."},
        {"q": "Where does craving arise and settle, according to this discourse?",
         "opts": [
             "Whatever in the world seems nice and pleasant, at each of the six senses",
             "Only in dreams",
             "Only in the body, never in the mind",
             "Craving has no specific location according to this discourse"],
         "correct": 0,
         "expl": "A concrete address, not a vague, free-floating force."},
        {"q": "What fivefold misperception is said to grow craving into suffering?",
         "opts": [
             "Seeing pleasant things as permanent, pleasurable, self, healthy, and safe",
             "Seeing pleasant things as impermanent and painful",
             "Ignoring pleasant things entirely",
             "Actively despising anything pleasant"],
         "correct": 0,
         "expl": "The mechanism run identically across past, future, and present ascetics and brahmins."},
        {"q": "What does the poisoned goblet in the closing simile look and taste like?",
         "opts": [
             "Genuinely appealing — a nice color, aroma, and flavor",
             "Obviously foul and repulsive, warning drinkers away",
             "Colorless and tasteless",
             "The simile doesn't describe its appearance"],
         "correct": 0,
         "expl": "Craving's danger typically presents itself as entirely appealing, not obviously harmful."},
        {"q": "What is the difference between the two travelers in the poison simile?",
         "opts": [
             "One drinks recklessly without reflection; the other reflects and refuses",
             "One is thirsty and the other is not",
             "One is a mendicant and the other is a layperson",
             "There is no difference; both travelers behave identically"],
         "correct": 0,
         "expl": "Exactly the difference this discourse is teaching between craving indulged and craving released."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kammāsadamma, a town among the Kurus",
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, at the Bamboo Grove",
             "Kapilavatthu, the Buddha's home city"],
         "correct": 0,
         "expl": "The same distinctive setting as SN 12.60's exchange with Ānanda."},
        {"q": "How does seeing pleasant things as impermanent, painful, not-self, diseased, and dangerous affect craving, according to this discourse?",
         "opts": [
             "It leads to craving being given up, and eventually freedom from suffering",
             "It has no effect on craving whatsoever",
             "It causes craving to grow even faster",
             "It is described as impossible for anyone to achieve"],
         "correct": 0,
         "expl": "The mirror image of the fivefold misperception that grows craving."},
        {"q": "What term names the specific attachment this discourse traces old age and death to?",
         "opts": [
             "Upadhi",
             "Saṅkhāra",
             "Viññāṇa",
             "Nāmarūpa"],
         "correct": 0,
         "expl": "A term not commonly used as the direct link elsewhere in this saṃyutta's standard formula."},
    ],
    marginalia=[
        ("An answer that doesn't land", [
            "one mendicant tries, and falls short &mdash;",
            "Ānanda steps in to ask again",
        ]),
        ("A shorter chain, aimed precisely", [
            "not all twelve links this time &mdash;",
            "straight to attachment, straight to craving",
        ]),
        ("Craving given an address", [
            "the six senses, where the nice and pleasant sit &mdash;",
            "not a vague force, but a location",
        ]),
        ("A drink that tastes wonderful and kills", [
            "color, aroma, flavor, all appealing &mdash;",
            "one drinks, one reflects and refuses",
        ]),
    ],
    further=[
        '<a href="%s/sn12.66/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.65.html">SN 12.65 &middot; The City</a> '
        "&mdash; this book's already-published companion discourse, "
        "immediately before this one.",
        '<a href="sn-12.60.html">SN 12.60 &middot; Causation</a> '
        "&mdash; the earlier discourse set at the same Kammāsadamma, "
        "also featuring an exchange with Ānanda.",
        '<a href="sn-12.67.html">SN 12.67 &middot; Sheaves of Reeds</a> '
        "&mdash; the next discourse, Sāriputta and Mahākoṭṭhita "
        "probing the chain's structure from a different angle."],
)


# --------------------------------------------------------------------------- #
# SN 12.67 — Naḷakalāpīsutta
# --------------------------------------------------------------------------- #
page(
    12, 67, "Naḷakalāpī", "Sheaves of Reeds",
    meta_title="SN 12.67 — Sheaves of Reeds | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Naḷakalāpīsutta — Sāriputta rejects the fourfold "
        "self-made-or-other-made question for every link in the "
        "chain, then resolves the apparent circularity between "
        "consciousness and name and form with the canon's most "
        "famous image of mutual support. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Varanasi, in the deer park at Isipatana"),
        ("Speakers", "Venerable Mahākoṭṭhita and Venerable Sāriputta"),
        ("Form", "A repeated fourfold question met with the same "
                 "rejection at every link, then a direct challenge "
                 "about circularity, resolved with a simile"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; "
                       "&mdash; directly addresses a structural "
                       "puzzle at the base of the whole chain"),
    ],
    why=(
        "Mahākoṭṭhita puts to Sāriputta, link by link, the same "
        "fourfold question already met elsewhere in this saṃyutta: "
        "is old age and death made by oneself, by another, by both, "
        "or does it arise anomalously, uncaused by either? Sāriputta "
        "rejects all four options at every single link, all the way "
        "up to consciousness, replacing each with the proper "
        "conditional statement instead. But when he reaches "
        "consciousness and name and form, something unusual happens: "
        "he states that consciousness is a requirement for name and "
        "form, and then, asked the same question about consciousness "
        "itself, states that name and form are requirements for "
        "consciousness &mdash; an apparent circularity Mahākoṭṭhita "
        "immediately notices and presses him on. Sāriputta's answer "
        "is the image this discourse is named for: two sheaves of "
        "reeds leaning against each other, each held up by the "
        "other, neither standing alone."),
    guide=[
        ("The same fourfold rejection, run through every link", [
            "Unlike discourses elsewhere in this saṃyutta that pose "
            "this fourfold question once, this discourse runs it "
            "through the entire chain from old age and death back to "
            "consciousness, with Sāriputta giving the identical "
            "rejection and replacement at every single step."]),
        ("A circularity that isn't smoothed over", [
            "Rather than avoiding or downplaying the apparent "
            "circularity between consciousness and name and form, "
            "the discourse has Mahākoṭṭhita name it explicitly, "
            "quoting Sāriputta's own two statements back to him "
            "before asking directly how this should be understood."]),
        ("A simile offered because some people need one", [
            "Sāriputta doesn't simply restate his position more "
            "firmly; he explicitly says he'll give a simile because "
            "\"by means of a simile some sensible people understand "
            "the meaning of what is said,\" treating the image as a "
            "genuine aid to understanding rather than mere "
            "decoration."]),
        ("Two supports, neither one primary", [
            "The two sheaves of reeds don't represent one thing "
            "causing another in sequence; they represent mutual, "
            "simultaneous support &mdash; pull either one away and "
            "the other collapses, a structure genuinely different "
            "from the one-way conditioning used everywhere else in "
            "the chain."]),
        ("Thirty-six grounds for a single moment of praise", [
            "Mahākoṭṭhita's admiration isn't left as a vague "
            "compliment; it's spelled out across twelve links times "
            "three qualifications each &mdash; speaking Dhamma, "
            "practicing in line with it, and attaining extinguishment "
            "&mdash; giving the discourse's closing praise the same "
            "systematic precision as its opening question."]),
    ],
    terms=[
        ("sayaṅkataṁ jarāmaraṇaṁ, paraṅkataṁ jarāmaraṇaṁ&hellip; "
         "adhiccasamuppannaṁ jarāmaraṇaṁ",
         "&ldquo;old age and death made by oneself, by another&hellip; "
         "arising anomalously&rdquo; &mdash; the fourfold question "
         "posed and rejected at every link."),
        ("dve naḷakalāpiyo aññamaññaṁ nissāya tiṭṭheyyuṁ",
         "&ldquo;two sheaves of reeds leaning up against each "
         "other&rdquo; &mdash; the image resolving the apparent "
         "circularity between consciousness and name and form."),
        ("nāmarūpapaccayā viññāṇaṁ; viññāṇapaccayā nāmarūpaṁ",
         "&ldquo;name and form are requirements for consciousness. "
         "Consciousness is a requirement for name and form&rdquo; "
         "&mdash; the mutual conditioning Mahākoṭṭhita presses "
         "Sāriputta on."),
        ("tāsañce&hellip; naḷakalāpīnaṁ ekaṁ ākaḍḍheyya, ekā "
         "papateyya",
         "&ldquo;if the first of those sheaves of reeds were to be "
         "pulled away, the other would collapse&rdquo; &mdash; the "
         "simile's cessation half, mutual support withdrawn."),
        ("imehi chattiṁsāya vatthūhi anumodāma",
         "&ldquo;we express our agreement&hellip; on these "
         "thirty-six grounds&rdquo; &mdash; twelve links times three "
         "qualifications, giving the closing praise systematic "
         "precision."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.67:1.1-1.6"),
        ("p", "&sect;2", "sn12.67:2.1-2.3"),
        ("p", "&sect;3", "sn12.67:3.1-3.9"),
        ("p", "&sect;4", "sn12.67:4.1-4.3"),
        ("p", "&sect;5", "sn12.67:5.1-6.3"),
        ("p", "&sect;6", "sn12.67:7.1-7.16"),
        ("p", "&sect;7", "sn12.67:8.1-8.4"),
        ("p", "&sect;8", "sn12.67:9.1-9.16"),
    ],
    quiz=[
        {"q": "What fourfold question does Mahākoṭṭhita pose to Sāriputta about old age and death?",
         "opts": [
             "Whether it's made by oneself, by another, by both, or arises anomalously uncaused",
             "Whether it's permanent, impermanent, both, or neither",
             "Whether it's painful, pleasant, both, or neither",
             "Whether it's visible, invisible, both, or neither"],
         "correct": 0,
         "expl": "The same fourfold structure asked about identity/causation questions elsewhere in this saṃyutta."},
        {"q": "How does Sāriputta answer this fourfold question at every link?",
         "opts": [
             "He rejects all four options and gives the proper conditional statement instead",
             "He affirms the first option every time",
             "He affirms a different option depending on the link",
             "He declines to answer at all"],
         "correct": 0,
         "expl": "A consistent rejection-and-replacement pattern run through the entire chain."},
        {"q": "What apparent problem does Mahākoṭṭhita notice once the questioning reaches consciousness and name and form?",
         "opts": [
             "An apparent circularity — each is said to be a requirement for the other",
             "That Sāriputta contradicts an earlier discourse entirely",
             "That consciousness and name and form are declared identical",
             "That Sāriputta refuses to discuss these two links"],
         "correct": 0,
         "expl": "Consciousness conditions name and form, and name and form condition consciousness."},
        {"q": "What image does Sāriputta use to resolve this apparent circularity?",
         "opts": [
             "Two sheaves of reeds leaning against each other",
             "A wheel turning on its axle",
             "Two rivers merging into one",
             "A single reed standing alone"],
         "correct": 0,
         "expl": "The image this discourse is named for."},
        {"q": "What happens if one of the two sheaves of reeds is pulled away?",
         "opts": [
             "The other collapses as well",
             "The other stands even more firmly",
             "Nothing changes for either sheaf",
             "Both sheaves burst into flame"],
         "correct": 0,
         "expl": "Mutual, simultaneous support — a structure distinct from one-way conditioning."},
        {"q": "Why does Sāriputta offer a simile rather than simply restating his position?",
         "opts": [
             "Because \"by means of a simile some sensible people understand the meaning of what is said\"",
             "Because he has run out of things to say",
             "Because Mahākoṭṭhita explicitly forbids further direct explanation",
             "Because similes are required by monastic rule in this situation"],
         "correct": 0,
         "expl": "The image treated as a genuine aid to understanding, not mere decoration."},
        {"q": "How many \"grounds\" does Mahākoṭṭhita use to express his agreement at the discourse's close?",
         "opts": [
             "Thirty-six — twelve links times three qualifications each",
             "Twelve",
             "Three",
             "One hundred and eight"],
         "correct": 0,
         "expl": "A systematic structure matching the discourse's precise, methodical opening."},
        {"q": "What three qualifications make up each set of three in the thirty-six grounds?",
         "opts": [
             "Speaking Dhamma, practicing in line with it, and attaining extinguishment",
             "Ordination, meditation, and almsround",
             "Faith, generosity, and patience",
             "Sight, hearing, and touch"],
         "correct": 0,
         "expl": "Each of the twelve links paired with these three qualifications."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "Varanasi, in the deer park at Isipatana",
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, at the Bamboo Grove",
             "Kammāsadamma, among the Kurus"],
         "correct": 0,
         "expl": "The location where the Buddha's first teaching to the five ascetics also took place."},
        {"q": "Who are the two speakers in this discourse?",
         "opts": [
             "Venerable Mahākoṭṭhita and Venerable Sāriputta",
             "The Buddha and Venerable Ānanda",
             "The Buddha and an unnamed mendicant",
             "Venerable Sāriputta and a visiting brahmin"],
         "correct": 0,
         "expl": "A dialogue between two senior disciples, without the Buddha present."},
    ],
    marginalia=[
        ("The same question, every link", [
            "self-made, other-made, both, neither &mdash;",
            "all four rejected, every time",
        ]),
        ("A circularity named, not hidden", [
            "consciousness needs name and form &mdash;",
            "name and form need consciousness",
        ]),
        ("Two sheaves, holding each other up", [
            "neither one standing alone &mdash;",
            "pull one, and both collapse",
        ]),
        ("Praise given systematic weight", [
            "thirty-six grounds, not a vague compliment &mdash;",
            "twelve links, three qualifications each",
        ]),
    ],
    further=[
        '<a href="%s/sn12.67/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.66.html">SN 12.66 &middot; Probing Within</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.68.html">SN 12.68 &middot; At Kosambī</a> '
        "&mdash; the next discourse, four senior mendicants probing "
        "how personal knowledge of this same chain relates to full "
        "awakening."],
)


# --------------------------------------------------------------------------- #
# SN 12.68 — Kosambisutta
# --------------------------------------------------------------------------- #
page(
    12, 68, "Kosambi", "At Kosambī",
    meta_title="SN 12.68 — At Kosambī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kosambisutta — Musīla and Nārada each affirm personal, "
        "independent knowledge of the whole chain and of "
        "extinguishment itself, yet only one of them is willing to "
        "call himself an arahant, illustrated by a waterless well on "
        "a desert road. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kosambī, at Ghosita's monastery"),
        ("Speakers", "Venerables Saviṭṭha, Musīla, Nārada, and "
                     "Ānanda"),
        ("Form", "A repeated formula tested first against Musīla, "
                 "then against Nārada, exposing a distinction "
                 "between them that the formula alone doesn't "
                 "capture"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; "
                       "&mdash; a careful distinction between "
                       "knowing and being that easy formulas can't "
                       "settle"),
    ],
    why=(
        "Saviṭṭha asks Musīla, link by link through the whole chain "
        "and then all the way to \"the cessation of continued "
        "existence is extinguishment,\" whether he knows this "
        "personally &mdash; apart from faith, endorsement, oral "
        "transmission, reasoned argument, or accepting a view after "
        "reflection. Musīla affirms every single step with the same "
        "formula: he knows and sees it himself. Satisfied, Saviṭṭha "
        "concludes Musīla must be a fully awakened arahant &mdash; "
        "and Musīla simply falls silent. Nārada then volunteers to "
        "answer the identical questions, gives identical answers, "
        "but when Saviṭṭha draws the same conclusion, Nārada refuses "
        "it outright: he has genuinely seen with right wisdom that "
        "the cessation of existence is extinguishment, and yet he is "
        "not an arahant. His explanation is the discourse's central "
        "image &mdash; a well on a desert road with neither rope nor "
        "bucket, its water visible to a parched traveler who knows "
        "perfectly well that it's there, but cannot physically touch "
        "it."),
    guide=[
        ("The same formula, tested on two different people", [
            "Saviṭṭha's question and its precise wording &mdash; "
            "apart from faith, endorsement, oral transmission, "
            "reasoned argument, or accepted view, do you personally "
            "know &mdash; is repeated identically for Musīla and then "
            "for Nārada, making the two responses directly "
            "comparable rather than two separate teachings."]),
        ("A formula that measures knowledge, not necessarily attainment", [
            "Both Musīla and Nārada give exactly the same affirmative "
            "answers to exactly the same questions, right up to and "
            "including the cessation of existence being "
            "extinguishment &mdash; yet this identical knowledge "
            "doesn't settle whether either of them has fully "
            "attained what they know."]),
        ("Silence as its own kind of answer", [
            "When Saviṭṭha calls Musīla an arahant, Musīla doesn't "
            "correct him or explain; he simply falls silent, leaving "
            "the reader to draw their own conclusion about what that "
            "silence means, since the text itself doesn't say."]),
        ("A direct refusal, backed by a precise image", [
            "Where Musīla stays quiet, Nārada speaks up clearly: he "
            "has truly seen with right wisdom that the cessation of "
            "existence is extinguishment, and states plainly that he "
            "is not an arahant, refusing to let the formula's "
            "affirmative answers stand in for a claim he won't make."]),
        ("Water seen, but not yet touched", [
            "The waterless well doesn't describe someone deceived or "
            "mistaken about where the water is; the traveler's "
            "knowledge is completely accurate &mdash; the gap is "
            "purely between knowing something is real and being able "
            "to physically reach it, a precise distinction between "
            "clear seeing and complete attainment."]),
    ],
    terms=[
        ("aññatreva&hellip; saddhāya aññatra ruciyā aññatra "
         "anussavā aññatra ākāraparivitakkā aññatra "
         "diṭṭhinijjhānakkhantiyā&hellip; paccattameva ñāṇaṁ",
         "&ldquo;apart from faith, endorsement, oral transmission, "
         "reasoned train of thought, or acceptance of a view after "
         "deliberation&hellip; personal knowledge&rdquo; &mdash; "
         "the discourse's repeated, precisely worded question."),
        ("bhavanirodho nibbānaṁ",
         "&ldquo;the cessation of continued existence is "
         "extinguishment&rdquo; &mdash; the final, most demanding "
         "step both Musīla and Nārada affirm knowing personally."),
        ("tenahāyasmā&hellip; arahaṁ khīṇāsavo",
         "&ldquo;then Venerable&hellip; is a perfected one, with "
         "defilements ended&rdquo; &mdash; Saviṭṭha's conclusion, "
         "met with silence from Musīla and direct refusal from "
         "Nārada."),
        ("kantāramagge udapāno, tatra nevassa rajju na "
         "udakavārako",
         "&ldquo;a well on a desert road&hellip; with neither rope "
         "nor bucket&rdquo; &mdash; Nārada's image for knowing "
         "something is real without being able to reach it."),
        ("udakan&rdquo;ti hi kho ñāṇaṁ assa, na ca kāyena "
         "phusitvā vihareyya",
         "&ldquo;they'd know that there was water, but they "
         "couldn't physically touch it&rdquo; &mdash; the precise "
         "distinction between clear seeing and complete attainment."),
    ],
    text_intro=(
        "The discourse in full. Section 8 elides an identical "
        "repetition of Saviṭṭha's questions to Venerable Nārada, "
        "exactly as bilara-data leaves it elided, trusting the "
        "reader's memory of the parallel exchange with Musīla just "
        "given. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.68:1.1-1.6"),
        ("p", "&sect;2", "sn12.68:2.1-2.13"),
        ("p", "&sect;3", "sn12.68:3.1-3.4"),
        ("p", "&sect;4", "sn12.68:4.1-4.13"),
        ("p", "&sect;5", "sn12.68:5.1-5.4"),
        ("p", "&sect;6", "sn12.68:6.1-6.2"),
        ("p", "&sect;7", "sn12.68:7.1-8.1"),
        ("p", "&sect;8", "sn12.68:12.1-12.4"),
        ("p", "&sect;9", "sn12.68:13.1-13.6"),
        ("p", "&sect;10", "sn12.68:14.1-14.3"),
    ],
    quiz=[
        {"q": "What precise question does Saviṭṭha ask Musīla about each link of the chain?",
         "opts": [
             "Whether he personally knows it, apart from faith, endorsement, oral transmission, or reasoned argument",
             "Whether he has memorized it word for word",
             "Whether he learned it directly from the Buddha",
             "Whether other mendicants agree with him about it"],
         "correct": 0,
         "expl": "A precisely worded question about independent, personal knowledge, repeated at every step."},
        {"q": "How does Musīla answer every one of Saviṭṭha's questions?",
         "opts": [
             "Affirmatively — he knows and sees each point personally",
             "He refuses to answer any of the questions",
             "He gives a different answer for each question",
             "He answers only the first few questions and then stops"],
         "correct": 0,
         "expl": "A consistent, identical formula of personal affirmation at every link."},
        {"q": "What does Musīla do when Saviṭṭha concludes he must be an arahant?",
         "opts": [
             "He falls silent",
             "He explicitly agrees",
             "He explicitly denies it with a detailed explanation",
             "He leaves the conversation immediately"],
         "correct": 0,
         "expl": "The text doesn't explain what this silence means, leaving it open."},
        {"q": "How does Nārada's response differ from Musīla's, despite giving identical answers to the same questions?",
         "opts": [
             "He explicitly refuses the conclusion that he is an arahant",
             "He gives different answers to the chain questions",
             "He refuses to discuss the topic at all",
             "He claims to be an arahant more emphatically than Musīla"],
         "correct": 0,
         "expl": "A direct, spoken refusal rather than silence."},
        {"q": "What image does Nārada use to explain his position?",
         "opts": [
             "A well on a desert road with neither rope nor bucket",
             "A boat without oars",
             "A locked door with no key",
             "A map without a destination marked"],
         "correct": 0,
         "expl": "The discourse's central image for knowing something is real without reaching it."},
        {"q": "What is the traveler's relationship to the water in Nārada's well simile?",
         "opts": [
             "He knows accurately that it's there, but cannot physically touch it",
             "He is mistaken about the water's location",
             "He believes there is no water at all",
             "He successfully drinks the water without difficulty"],
         "correct": 0,
         "expl": "Accurate knowledge, but a gap between knowing and complete attainment."},
        {"q": "What does this discourse's structure — the same formula tested on two people — accomplish?",
         "opts": [
             "It makes the two responses directly comparable, showing the formula alone doesn't settle everything",
             "It proves that only one of the two men actually understood the chain",
             "It shows that Saviṭṭha's questions were poorly designed",
             "It has no particular purpose beyond repetition"],
         "correct": 0,
         "expl": "Identical knowledge, yet a real difference the formula's affirmative answers can't capture."},
        {"q": "What is the final, most demanding step both Musīla and Nārada affirm personally knowing?",
         "opts": [
             "That the cessation of continued existence is extinguishment",
             "That the Buddha is omniscient",
             "That all mendicants will become arahants eventually",
             "That rebirth is impossible to escape"],
         "correct": 0,
         "expl": "The culminating link in the sequence of questions."},
        {"q": "How does Venerable Ānanda respond at the discourse's close?",
         "opts": [
             "He asks Saviṭṭha what he has to say to Nārada's explanation",
             "He declares Nārada mistaken",
             "He leaves the conversation without comment",
             "He repeats the entire chain of questions himself"],
         "correct": 0,
         "expl": "A closing question drawing the exchange to its final point."},
        {"q": "Where does this exchange take place?",
         "opts": [
             "Kosambī, at Ghosita's monastery",
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, at the Bamboo Grove",
             "Kammāsadamma, among the Kurus"],
         "correct": 0,
         "expl": "A distinct setting from most of this chapter's other discourses."},
    ],
    marginalia=[
        ("One question, asked all the way down", [
            "not faith, not hearsay — personal knowledge &mdash;",
            "tested link by link to the very end",
        ]),
        ("Silence as its own kind of answer", [
            "Musīla says nothing at all &mdash;",
            "the text doesn't explain why",
        ]),
        ("A refusal spoken plainly", [
            "\"I see it, yet I am not arahant\" &mdash;",
            "Nārada won't let the formula speak for him",
        ]),
        ("Water seen, not yet touched", [
            "a well with neither rope nor bucket &mdash;",
            "knowing it's real, still out of reach",
        ]),
    ],
    further=[
        '<a href="%s/sn12.68/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.67.html">SN 12.67 &middot; Sheaves of Reeds</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.49.html">SN 12.49 &middot; A Noble Disciple</a> '
        "&mdash; the earlier discourse naming a related but simpler "
        "term, knowledge independent of others, for a noble "
        "disciple's understanding.",
        '<a href="sn-12.69.html">SN 12.69 &middot; Surge</a> '
        "&mdash; the next discourse, the whole chain pictured as "
        "water cascading from ocean to smallest pond."],
)

# --------------------------------------------------------------------------- #
# SN 12.69 — Upayantisutta
# --------------------------------------------------------------------------- #
page(
    12, 69, "Upayanti", "Surge",
    meta_title="SN 12.69 — Surge | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upayantisutta — the whole twelve-link chain pictured as "
        "a single cascade, the ocean's surge passing down through "
        "rivers, streams, lakes, and ponds to the smallest link, and "
        "receding the same way in reverse. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single unbroken cascade simile applied to the "
                 "entire chain at once, given forward and then in "
                 "reverse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but its single unbroken image is "
                       "worth noticing for its own sake"),
    ],
    why=(
        "Where most discourses in this saṃyutta apply their simile "
        "to one or two links at a time, this brief discourse pictures "
        "the entire twelve-link chain in a single continuous image: "
        "the ocean surging makes the great rivers surge, the great "
        "rivers surging make the streams surge, the streams surging "
        "make the lakes surge, the lakes surging make the ponds "
        "surge. In exactly the same unbroken cascade, ignorance "
        "surging makes choices surge, choices surging make "
        "consciousness surge, and so on down through name and form, "
        "the six sense fields, contact, feeling, craving, grasping, "
        "continued existence, rebirth, all the way to old age and "
        "death. The reverse direction runs the identical cascade "
        "backward, describing recession rather than a separate "
        "cessation formula, giving the whole discourse an unusually "
        "unified, single-breath quality."),
    guide=[
        ("One image for the whole chain, not one per link", [
            "Rather than pairing a simile with a single link or a "
            "small cluster of links, as most of this saṃyutta's "
            "similes do, this discourse maps the entire twelve-link "
            "sequence onto a single continuous natural process from "
            "start to finish."]),
        ("A cascade with a clear direction and no repeated pauses", [
            "The ocean-to-pond sequence and the ignorance-to-old-age-and-death "
            "sequence are each given in one unbroken run rather "
            "than being broken into separate arising and cessation "
            "movements with their own formulas, giving the whole "
            "discourse a rare single-breath continuity."]),
        ("Surging as continuation, not one-time causation", [
            "\"Upayanti\" describes an ongoing surge, a swelling that "
            "keeps propagating outward, rather than a single "
            "triggering event &mdash; a subtly different image from "
            "this saṃyutta's more common \"requirement for\" "
            "language, emphasizing continuous momentum over discrete "
            "causal steps."]),
        ("Recession as the same process in reverse, not a new one", [
            "The cessation half doesn't introduce a different "
            "vocabulary or structure; it simply runs the identical "
            "cascade backward &mdash; the ocean receding, the rivers "
            "receding in turn &mdash; treating cessation as the same "
            "process reversed rather than as something requiring its "
            "own distinct account."]),
        ("A brief discourse whose scale outruns its length", [
            "At only two sections, this is among the shortest "
            "discourses in this chapter, yet it's also one of the "
            "very few to hold the entire twelve-link chain in view "
            "simultaneously rather than examining it piece by piece."]),
    ],
    terms=[
        ("mahāsamuddo&hellip; upayanto mahānadiyo upayāpeti",
         "&ldquo;when the ocean surges it makes the great rivers "
         "surge&rdquo; &mdash; the opening link of the cascade "
         "simile applied to the whole chain at once."),
        ("avijjā upayantī saṅkhāre upayāpeti",
         "&ldquo;when ignorance surges it makes choices "
         "surge&rdquo; &mdash; the natural image mapped directly "
         "onto the chain's first link."),
        ("kusobbhe upayāpenti",
         "&ldquo;makes the ponds surge&rdquo; &mdash; the smallest "
         "body of water in the cascade, corresponding to old age "
         "and death at the chain's far end."),
        ("mahāsamuddo&hellip; apayanto&hellip; apayāpeti",
         "&ldquo;when the ocean recedes&hellip; it makes [them] "
         "recede&rdquo; &mdash; the identical cascade run backward "
         "for the reverse, cessation direction."),
        ("jāti apayantī jarāmaraṇaṁ apayāpeti",
         "&ldquo;when rebirth recedes it makes old age and death "
         "recede&rdquo; &mdash; the closing link of the reverse "
         "cascade."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.69:1.1-1.5"),
        ("p", "&sect;2", "sn12.69:2.1-2.2"),
    ],
    quiz=[
        {"q": "How does this discourse's simile differ from most others in this saṃyutta?",
         "opts": [
             "It maps the entire twelve-link chain onto a single continuous image, rather than one or two links at a time",
             "It uses no simile at all",
             "It applies twelve entirely separate similes, one per link",
             "It only covers the first three links of the chain"],
         "correct": 0,
         "expl": "A rare, single unbroken cascade covering the whole chain at once."},
        {"q": "What natural process does the discourse use as its image?",
         "opts": [
             "The ocean surging, cascading down through rivers, streams, lakes, to ponds",
             "A mountain eroding over centuries",
             "A forest fire spreading",
             "Seasons changing from summer to winter"],
         "correct": 0,
         "expl": "A water cascade running from the largest body of water to the smallest."},
        {"q": "What does \"upayanti\" (surge) emphasize, compared to this saṃyutta's more common \"requirement for\" language?",
         "opts": [
             "Continuous, ongoing momentum rather than a single discrete causal step",
             "A one-time triggering event with no continuation",
             "Complete stillness and absence of movement",
             "Random, unpredictable change with no pattern"],
         "correct": 0,
         "expl": "A swelling that keeps propagating outward, not a single cause-and-effect moment."},
        {"q": "How is the reverse, cessation direction handled in this discourse?",
         "opts": [
             "The identical cascade is simply run backward, as recession rather than a separate formula",
             "A completely different vocabulary and structure is introduced",
             "The discourse doesn't describe a reverse direction at all",
             "Only the first three links are reversed"],
         "correct": 0,
         "expl": "Cessation treated as the same process reversed, not something requiring its own account."},
        {"q": "What corresponds to old age and death in the water cascade image?",
         "opts": [
             "The ponds, the smallest body of water in the sequence",
             "The ocean itself",
             "The great rivers",
             "Nothing in the image corresponds to old age and death"],
         "correct": 0,
         "expl": "The final, smallest link at the far end of the cascade."},
        {"q": "How long is this discourse, compared to most others in this chapter?",
         "opts": [
             "Among the shortest, at only two sections",
             "Among the longest, spanning thirty sections",
             "Exactly average in length",
             "Longer than SN 12.70"],
         "correct": 0,
         "expl": "Brief in length but unusually comprehensive in scope."},
        {"q": "What is unusual about this discourse's scope despite its brevity?",
         "opts": [
             "It holds the entire twelve-link chain in view simultaneously, rather than examining it piece by piece",
             "It only discusses a single link in great depth",
             "It covers material entirely unrelated to dependent origination",
             "It repeats content already given verbatim elsewhere with no variation"],
         "correct": 0,
         "expl": "A rare case of comprehensive scope achieved in very few words."},
        {"q": "What is the first link named in the forward cascade?",
         "opts": [
             "Ignorance, surging and making choices surge",
             "Old age and death",
             "Consciousness",
             "Craving"],
         "correct": 0,
         "expl": "The chain's traditional starting point, mapped onto the ocean's surge."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "An unnamed mendicant",
             "A visiting brahmin"],
         "correct": 0,
         "expl": "No interlocutor or visiting figure appears."},
        {"q": "Where does the Buddha deliver this teaching?",
         "opts": [
             "At Sāvatthī",
             "Near Rājagaha",
             "Near Vesālī",
             "In the land of the Kurus"],
         "correct": 0,
         "expl": "The consistent setting shared with much of this chapter."},
    ],
    marginalia=[
        ("One image, the whole chain at once", [
            "not link by link this time &mdash;",
            "a single cascade from source to pond",
        ]),
        ("Surge, not a single cause", [
            "momentum propagating outward &mdash;",
            "continuation more than triggering",
        ]),
        ("The same water, running backward", [
            "no new formula for cessation &mdash;",
            "recession is simply the reverse",
        ]),
        ("Small in length, wide in scope", [
            "two sections holding all twelve links &mdash;",
            "brevity that doesn't shrink the picture",
        ]),
    ],
    further=[
        '<a href="%s/sn12.69/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.68.html">SN 12.68 &middot; At Kosambī</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.70.html">SN 12.70 &middot; The Wanderer Susīma</a> '
        "&mdash; the next discourse, closing this chapter with its "
        "longest and most consequential exchange.",
    ],
)

# --------------------------------------------------------------------------- #
# SN 12.70 — Susīmaparibbājakasutta
# --------------------------------------------------------------------------- #
page(
    12, 70, "Susīmaparibbājaka", "The Wanderer Susīma",
    meta_title="SN 12.70 — The Wanderer Susīma | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Susīmaparibbājakasutta — closing Mahāvagga, a wanderer "
        "ordains to steal the teaching for profit, discovers "
        "arahants without a single supernormal power, and receives "
        "the Buddha's famous teaching that knowledge of natural "
        "law precedes knowledge of extinguishment. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, in the Bamboo Grove"),
        ("Speakers", "The Buddha, the wanderer-turned-mendicant "
                     "Susīma, Venerable Ānanda, and several unnamed "
                     "mendicants"),
        ("Form", "An extended narrative in three movements &mdash; "
                 "a mercenary ordination, a failed interrogation of "
                 "genuine arahants, and the Buddha's own teaching "
                 "and forgiveness"),
        ("Length", "~11 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; "
                       "&mdash; closing this chapter with one of the "
                       "canon's most consequential single discourses"),
    ],
    why=(
        "Closing Mahāvagga, this discourse tells one of the fullest "
        "narratives in this saṃyutta. The wanderer Susīma is sent by "
        "his own community to infiltrate the Buddha's teaching "
        "purely for material gain &mdash; the Buddhist Saṅgha is "
        "receiving offerings that rival ascetics aren't &mdash; and "
        "ordains under false pretenses. When he hears several "
        "mendicants declare their own full awakening, he interrogates "
        "them expecting the traditional marks of attainment: psychic "
        "power, clairaudience, mind-reading, memory of past lives, "
        "the divine eye, formless meditative attainments. They "
        "answer no to every single one, telling him only that they "
        "are \"freed by wisdom.\" Confused, Susīma brings the puzzle "
        "to the Buddha himself, who gives one of the most quoted "
        "lines in the early texts &mdash; knowledge of the stability "
        "of natural principles comes first, knowledge of "
        "extinguishment comes after &mdash; before walking Susīma "
        "through the same five-aggregate reflection and the same "
        "full twelve-link catechism that produced those mendicants' "
        "understanding, then asking Susīma the identical six "
        "questions he'd put to them. Susīma, now understanding "
        "everything intellectually, still answers no to every one. "
        "The discourse closes not with triumph but with confession "
        "and an act of forgiveness."),
    guide=[
        ("A spy, not a genuine seeker, at the outset", [
            "The discourse doesn't soften Susīma's motive; his own "
            "community sends him explicitly to memorize the teaching "
            "so they can sell it to laypeople and win back the "
            "material support flowing to the Buddhist Saṅgha, "
            "making his ordination transactional from the very "
            "start."]),
        ("An interrogation built on a specific, testable assumption", [
            "Susīma's six questions aren't vague; they name specific, "
            "checkable attainments &mdash; the many kinds of psychic "
            "power, clairaudience, reading others' minds, "
            "recollecting past lives, the divine eye, the formless "
            "liberations &mdash; treating awakening as something "
            "that should show up as a checklist of supernormal "
            "abilities."]),
        ("\"Freed by wisdom,\" repeated without elaboration", [
            "When the mendicants answer no to every question, they "
            "don't try to explain or justify themselves further; "
            "they simply repeat \"we are freed by wisdom,\" twice, "
            "whether or not Susīma understands it, refusing to make "
            "their attainment depend on his approval."]),
        ("A famous line that reorders the whole path", [
            "\"Pubbe kho, susima, dhammaṭṭhitiñāṇaṁ, pacchā "
            "nibbāne ñāṇan\" places knowledge of how conditioned "
            "things actually work before any knowledge of "
            "extinguishment itself, suggesting liberation is reached "
            "through understanding causality thoroughly, not through "
            "acquiring extraordinary powers as evidence of it."]),
        ("The same test turned back on the one who gave it", [
            "After walking Susīma through the five aggregates and "
            "the full twelve-link chain, the Buddha asks him the "
            "identical six questions he'd asked the other mendicants "
            "&mdash; and Susīma, now genuinely understanding the "
            "teaching, still has to answer no to every one, "
            "confirming that intellectual and even liberating "
            "understanding doesn't automatically come bundled with "
            "supernormal powers."]),
        ("Confession met with a severe comparison and genuine acceptance", [
            "The Buddha doesn't minimize what Susīma did; he compares "
            "\"stealing the teaching\" to a criminal publicly "
            "executed, calling the spiritual consequence worse than "
            "that death &mdash; but immediately accepts Susīma's "
            "confession as genuine growth, closing the discourse, and "
            "this whole chapter, on forgiveness rather than "
            "condemnation."]),
    ],
    terms=[
        ("dhammatthenako",
         "&ldquo;a thief of the teachings&rdquo; &mdash; Susīma's "
         "own word for what he did, ordaining to extract the "
         "Dhamma for material gain."),
        ("paññāvimuttā kho mayaṁ",
         "&ldquo;we are freed by wisdom&rdquo; &mdash; the "
         "mendicants' repeated answer, offered without further "
         "explanation."),
        ("pubbe kho, susima, dhammaṭṭhitiñāṇaṁ, pacchā nibbāne "
         "ñāṇaṁ",
         "&ldquo;first comes knowledge of the stability of natural "
         "principles. Afterwards there is knowledge of "
         "extinguishment&rdquo; &mdash; one of the most quoted "
         "single lines in the early texts."),
        ("netaṁ mama nesohamasmi na meso attā",
         "&ldquo;this is not mine, I am not this, this is not my "
         "self&rdquo; &mdash; the not-self reflection applied to "
         "all five aggregates before Susīma's own liberation."),
        ("yathābālaṁ yathāmūḷhaṁ yathāakusalaṁ",
         "&ldquo;foolish, stupid, and unskillful&rdquo; &mdash; "
         "Susīma's own description of his crime, confirmed word for "
         "word by the Buddha before he is forgiven."),
    ],
    text_intro=(
        "The discourse in full, closing Mahāvagga. The chapter's "
        "closing verse of discourse titles is not translated in the "
        "source and is not quoted here; see the reading guide above "
        "for its contents. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn12.70:1.1-1.5"),
        ("p", "&sect;2", "sn12.70:2.1-2.9"),
        ("p", "&sect;3", "sn12.70:3.1-3.5"),
        ("p", "&sect;4", "sn12.70:4.1-4.10"),
        ("p", "&sect;5", "sn12.70:5.1-10.2"),
        ("p", "&sect;6", "sn12.70:11.1-12.3"),
        ("p", "&sect;7", "sn12.70:13.1-14.3"),
        ("p", "&sect;8", "sn12.70:15.1-15.31"),
        ("p", "&sect;9", "sn12.70:16.1-17.3"),
        ("p", "&sect;10", "sn12.70:18.1-19.14"),
        ("p", "&sect;11", "sn12.70:20.1-26.1"),
        ("p", "&sect;12", "sn12.70:27.1-27.3"),
        ("p", "&sect;13", "sn12.70:28.1-29.4"),
    ],
    quiz=[
        {"q": "Why does Susīma originally ordain in the Buddha's teaching?",
         "opts": [
             "His community sends him to memorize the teaching so they can profit from teaching it to laypeople",
             "He has a genuine, immediate conviction after hearing the Buddha teach",
             "He is ordered to by King Bimbisāra",
             "He wants to escape a personal tragedy"],
         "correct": 0,
         "expl": "A transactional motive, not softened or hidden by the discourse."},
        {"q": "What six things does Susīma ask the mendicants who declared awakening?",
         "opts": [
             "Whether they wield psychic power, clairaudience, mind-reading, past-life memory, the divine eye, and formless attainments",
             "Whether they have memorized the entire scriptures",
             "Whether they can perform miracles for the public",
             "Whether they have taken more than one hundred vows"],
         "correct": 0,
         "expl": "A specific, checkable list of traditional supernormal attainments."},
        {"q": "How do the mendicants answer all six of Susīma's questions?",
         "opts": [
             "No, to every single one, simply stating that they are freed by wisdom instead",
             "Yes, to every single one",
             "They refuse to answer at all",
             "They give different answers depending on the question"],
         "correct": 0,
         "expl": "No supernormal powers claimed, only wisdom-liberation, without further elaboration."},
        {"q": "What is the Buddha's famous response when Susīma brings him this puzzle?",
         "opts": [
             "\"First comes knowledge of the stability of natural principles. Afterwards there is knowledge of extinguishment.\"",
             "\"Those mendicants were mistaken to declare awakening.\"",
             "\"Psychic powers are required for genuine liberation.\"",
             "\"You should not have asked such a question.\""],
         "correct": 0,
         "expl": "One of the most quoted single lines in the early texts."},
        {"q": "What does the Buddha teach Susīma before running him through the twelve-link catechism?",
         "opts": [
             "The five aggregates as impermanent, suffering, and not-self",
             "A new set of monastic rules",
             "The geography of the thirty-one realms",
             "Nothing further; the catechism is given without preparation"],
         "correct": 0,
         "expl": "The same reflection that produced the other mendicants' understanding."},
        {"q": "What happens when the Buddha asks Susīma the same six questions he'd asked the other mendicants?",
         "opts": [
             "Susīma also answers no to every one, despite now understanding the teaching",
             "Susīma answers yes to all six, having gained the powers instantly",
             "Susīma refuses to answer",
             "The Buddha doesn't ask Susīma these questions"],
         "correct": 0,
         "expl": "Understanding doesn't automatically come bundled with supernormal powers."},
        {"q": "How does Susīma respond once he realizes the full situation?",
         "opts": [
             "He confesses his original mercenary motive as foolish and unskillful",
             "He denies ever having a mercenary motive",
             "He leaves the Saṅgha in shame without speaking to the Buddha",
             "He blames the other mendicants for misleading him"],
         "correct": 0,
         "expl": "A direct confession, using the same self-description the Buddha then confirms."},
        {"q": "How severe is the comparison the Buddha uses for \"stealing the teaching\"?",
         "opts": [
             "He compares it to a criminal's public execution, calling the spiritual consequence worse",
             "He treats it as a minor, easily forgiven mistake with no serious comparison",
             "He compares it to a minor breach of etiquette",
             "He refuses to comment on its severity at all"],
         "correct": 0,
         "expl": "A severe comparison, not a minimizing one."},
        {"q": "How does the discourse ultimately end?",
         "opts": [
             "With the Buddha accepting Susīma's confession as genuine growth and forgiving him",
             "With Susīma being expelled from the Saṅgha permanently",
             "With Susīma achieving full awakening on the spot",
             "With no resolution at all"],
         "correct": 0,
         "expl": "Forgiveness following genuine recognition and correction of the mistake."},
        {"q": "What chapter does this discourse close?",
         "opts": [
             "Mahāvagga",
             "Gahapativagga",
             "Dukkhavagga",
             "Kaḷārakhattiyavagga"],
         "correct": 0,
         "expl": "The seventh chapter of Nidānavagga, closing on one of its longest and most consequential discourses."},
    ],
    marginalia=[
        ("A spy, ordained for profit", [
            "sent to memorize, not to seek &mdash;",
            "the motive stated plainly, not hidden",
        ]),
        ("A checklist that comes up empty", [
            "six powers asked for, six times no &mdash;",
            "\"we are freed by wisdom\" and nothing more",
        ]),
        ("A line that reorders the path", [
            "knowledge of how things work, first &mdash;",
            "extinguishment's knowledge comes after",
        ]),
        ("The same test, turned back on the tester", [
            "Susīma understands, and still says no &mdash;",
            "wisdom without the powers he expected",
        ]),
    ],
    further=[
        '<a href="%s/sn12.70/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-12.69.html">SN 12.69 &middot; Surge</a> '
        "&mdash; the discourse immediately before this one.",
        '<a href="sn-12.68.html">SN 12.68 &middot; At Kosambī</a> '
        "&mdash; the earlier discourse in this chapter distinguishing "
        "personal knowledge of the chain from the attainment of "
        "arahantship, a distinction this discourse tests from a very "
        "different angle.",
        '<a href="sn-12.41.html">SN 12.41 &middot; Fears and Enmities</a> '
        "&mdash; opening the previous chapter with a self-declaration "
        "of stream-entry, contrasted here with a declaration this "
        "discourse subjects to the sharpest scrutiny in this "
        "saṃyutta.",
    ],
)
