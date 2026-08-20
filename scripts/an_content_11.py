# -*- coding: utf-8 -*-
"""Ekādasaka Nipāta — The Elevens. One discourse per page, from AN 11.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Ekādasaka Nipāta — The Elevens"
# HEAD points at the last page the Tens module reached. an-11.15.html, the
# sole survivor of the earlier eighteen-page selection, sat inside chapter 2
# (Anussativagga, 11.11-21) between 11.14 and 11.16; it is now spliced in
# with explicit prev=/next= kwargs on those two pages, per the an-10.60/
# an-10.176 precedent, and an-11.15.html's own prev/next were hand-edited to
# match. TAIL is the default collection link since no already-published page
# exists beyond this module's own PAGES until chapter 3 is built. (an_index.py
# accesses mod.TAIL directly with no getattr default, so it must stay defined.)
HEAD = ("an-10.267-746.html",
        "AN 10.267&ndash;746 &middot; Hate, Etc., Closing the Book of the Tens")
TAIL = ("./", "Aṅguttara Nikāya selections")
INDEX_EXTRA = [
    ("an-11.15", "Mettānisaṁsa", "The Benefits of Love"),
]

PAGES = []

VAGGA_1 = "<em>Nissayavagga</em> &mdash; the first chapter of the Elevens"
SETTING_SAVATTHI = "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery"
SETTING_NATIKA = "Ñātika, in the brick house"
SETTING_RAJAGAHA = ("Rājagaha, at the monastery of the wanderers in the "
                    "peacocks&rsquo; feeding ground")
SETTING_KAPILAVATTHU = ("The land of the Sakyans, near Kapilavatthu, in "
                        "the Banyan Tree Monastery")
SETTING_BELUVA = "Vesālī, in the little village of Beluva"
SETTING_NONE = "None stated in the source"
SPEAKER = "The Buddha alone, addressing the mendicants"
VAGGA_2 = "<em>Anussativagga</em> &mdash; the second chapter of the Elevens"
VAGGA_3 = "<em>Sāmaññavagga</em> &mdash; the third chapter of the Elevens"
EIGHT_CONTEMPLATIONS = (
    "impermanence, suffering, not-self, ending, vanishing, fading away, "
    "cessation, and letting go")


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Elevens."""
    d = {
        "slug": "an-11.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an11/an11.%d" % num,
        "crumb": "AN 11.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 11.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 11.1 — Kimatthiyasutta
# --------------------------------------------------------------------------- #
page(
    1, "Kimatthiya", "What&rsquo;s the Goal?",
    vagga=VAGGA_1,
    meta_title="AN 11.1 — What's the Goal? | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kimatthiyasutta, opening the Book of the Elevens with "
        "Ānanda's chained questioning of the Buddha — the same "
        "progressive logic met at AN 10.1, now extended to eleven "
        "links. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "Venerable Ānanda questioning the Buddha"),
        ("Form", "Ten repeated questions, each asking the goal of the "
                 "previous answer, then the full eleven-link chain "
                 "restated with a closing line not present at AN 10.1"),
        ("Length", "~2 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own name to "
                               "the chapter, <em>Nissayavagga</em>, the "
                               "Chapter on Dependence, and opens the "
                               "entire new nipāta"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "nearly identical to AN 10.1, worth reading "
                       "against it directly"),
    ],
    why=(
        "Ānanda asks the Buddha, link by link, what the goal and "
        "benefit of skillful ethics is, and each answer becomes the "
        "next question's subject: no regret, joy, rapture, tranquility, "
        "bliss, immersion, true knowledge and vision, disillusionment "
        "and dispassion, and finally the knowledge and vision of "
        "freedom &mdash; the same ten-link chain met at AN 10.1, but "
        "closing here with an explicit eleventh line naming the "
        "chain's own logic."),
    guide=[
        ("The teaching in one sentence", [
            "Skillful ethics leads progressively to the highest through "
            "the same ten links met at AN 10.1 &mdash; no regret, joy, "
            "rapture, tranquility, bliss, immersion, true knowledge and "
            "vision, disillusionment and dispassion, and the knowledge "
            "and vision of freedom &mdash; now closing with an eleventh, "
            "summary line."]),
        ("A new nipāta, reopening its predecessor's own opener", [
            "As with every new nipāta before it, the Book of the "
            "Elevens opens with a discourse lending its own subject "
            "&mdash; <em>nissaya</em>, dependence &mdash; to the "
            "chapter's name, <em>Nissayavagga</em>. Unlike every earlier "
            "nipāta transition, though, this opening discourse is not "
            "new content: it is AN 10.1's own Kimatthiyasutta, restated "
            "with one further line added to its closing chain."]),
        ("The same chain, one line longer", [
            "AN 10.1's chain closed at its tenth link, the knowledge "
            "and vision of freedom. This version adds an eleventh: "
            "&lsquo;skillful ethics progressively lead up to the "
            "highest&rsquo; &mdash; not a new stage in the sequence but "
            "an explicit naming of the sequence's own logic, giving "
            "this nipāta its numerical count without inventing new "
            "content."]),
        ("Why the Elevens often work this way", [
            "Several discourses early in this nipāta will repeat "
            "content already met in the Tens, padded to eleven items "
            "by an added summary line, a further simile, or one more "
            "item folded into an existing list &mdash; a structural "
            "pattern worth watching for across this chapter rather "
            "than assuming each discourse is freshly composed."]),
    ],
    terms=[
        ("kimatthiyā, kimānisaṁsā",
         "&ldquo;what is the goal, what is the benefit&rdquo; &mdash; "
         "Ānanda's own repeated question, identical to AN 10.1, giving "
         "this discourse its title and this chapter its name."),
        ("avippaṭisāra",
         "&ldquo;having no regrets&rdquo; &mdash; the first link, the "
         "immediate fruit of skillful ethics."),
        ("samādhi",
         "&ldquo;immersion&rdquo; &mdash; the sixth link, the point "
         "where the chain moves from feeling-based qualities to "
         "cognitive ones."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the "
         "tenth link, closing the chain proper before the new eleventh "
         "line."),
        ("uttaruttari",
         "&ldquo;progressively... to the highest&rdquo; &mdash; the "
         "closing eleventh line's own phrase, naming the chain's "
         "upward logic explicitly rather than leaving it implicit."),
    ],
    text_intro=(
        "The discourse in full: ten chained questions, then the full "
        "eleven-line chain restated. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Ten questions, chained"),
        ("p", "&sect;1", "an11.1:1.1-10.2"),
        ("h3", "The chain, restated in full"),
        ("p", "&sect;2", "an11.1:11.1-11.11"),
    ],
    quiz=[
        {"q": "How does this discourse build its chain?",
         "opts": [
             "By stating all eleven links outright in a single line",
             "Through ten repeated questions, each asking the goal of "
             "the previous answer, before restating the whole chain",
             "Through a narrative with several characters",
             "Through a simile alone"],
         "correct": 1,
         "expl": "A chain built by repeated questioning, exactly as at "
                 "AN 10.1."},
        {"q": "How does this discourse's chain differ from AN 10.1's?",
         "opts": [
             "It has entirely different content",
             "It is the identical ten-link chain, with one further "
             "summary line added at the close",
             "It has half as many links",
             "It removes the immersion link"],
         "correct": 1,
         "expl": "Same ten links, plus an eleventh naming the chain's "
                 "own upward logic."},
        {"q": "According to the guide, what does the new eleventh line "
              "add?",
         "opts": [
             "A new eleventh stage of practice",
             "An explicit statement that skillful ethics progressively "
             "lead up to the highest, naming the chain's own logic",
             "A description of a place",
             "A list of unrelated qualities"],
         "correct": 1,
         "expl": "Not a new stage, but an explicit naming of the "
                 "sequence's upward logic."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular", "Its own subject, dependence "
             "(nissaya), naming Nissayavagga",
             "A disciple's name", "A place name"],
         "correct": 1,
         "expl": "As with every new nipāta's opener, the discourse "
                 "names its own chapter."},
        {"q": "According to the guide, what structural pattern is "
              "worth watching for early in this nipāta?",
         "opts": [
             "Every discourse is freshly composed with no relation to "
             "the Tens",
             "Several early discourses repeat content from the Tens, "
             "padded to eleven items by an added line or item",
             "The nipāta abandons the ten-link chain entirely",
             "No pattern is discernible"],
         "correct": 1,
         "expl": "A recurring move in this nipāta's early chapters, "
                 "flagged here for what follows."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "No setting is given"],
         "correct": 1,
         "expl": "The standard opening setting for a new nipāta's first "
                 "discourse, identical to AN 10.1's own."},
    ],
    marginalia=[
        ("Eleven links, chained", [
            "no regret, joy, rapture,",
            "tranquility, bliss, on up",
            "one line longer now",
        ]),
        ("Built by questioning", [
            "Ānanda asks ten",
            "times over &mdash; then the whole",
            "chain, restated once",
        ]),
        ("A new nipāta's own namesake", [
            "nissaya gives its name",
            "to Nissayavagga &mdash;",
            "the chapter it opens",
        ]),
        ("Cross-references", [
            "AN 10.267&ndash;746 &middot; previous nipāta, closing the "
            "Tens",
            "AN 10.1 &middot; the identical ten-link chain this "
            "discourse extends by one line",
            "AN 11.2 &middot; next, the same chain restated positively",
        ]),
    ],
    further=[
        '<a href="%s/an11.1/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-10.267-746.html">AN 10.267&ndash;746</a> &mdash; previous, closing '
        "the Book of the Tens.",
        '<a href="an-11.2.html">AN 11.2 &middot; Making a Wish</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.2 — Cetanākaraṇīyasutta
# --------------------------------------------------------------------------- #
page(
    2, "Cetanākaraṇīya", "Making a Wish",
    vagga=VAGGA_1,
    meta_title="AN 11.2 — Making a Wish | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Cetanākaraṇīyasutta, restating AN 11.1's chain positively "
        "— each stage arising naturally from the one before, with no "
        "wish required. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same ten links as AN 11.1, restated as things "
                 "that need not be wished for, with the closing "
                 "near-shore-to-far-shore image"),
        ("Length", "~2 minutes to read"),
        ("The identical chain, reframed", "Same ten links, same order, "
         "but framed here as natural consequence rather than "
         "questioned goal"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as AN 10.2, worth comparing "
                       "the two framings directly"),
    ],
    why=(
        "An ethical person need not wish for freedom from regret "
        "&mdash; it arises naturally; and from there, joy, rapture, "
        "tranquility, bliss, immersion, true knowledge and vision, "
        "disillusionment and dispassion, and the knowledge and vision "
        "of freedom each arise naturally in turn, without need for a "
        "wish, so that good qualities flow from one to the next, from "
        "the near shore to the far."),
    guide=[
        ("The teaching in one sentence", [
            "An ethical person need not wish for any of the ten links "
            "&mdash; freedom from regret, joy, rapture, tranquility, "
            "bliss, immersion, true knowledge and vision, "
            "disillusionment and dispassion, and the knowledge and "
            "vision of freedom &mdash; since each arises naturally from "
            "the one before it."]),
        ("The same relation this project has already met once", [
            "This discourse's ten links, and its refrain that each "
            "&lsquo;need not be wished for&rsquo; since it &lsquo;only "
            "naturally&rsquo; arises, are word-for-word identical to AN "
            "10.2. As with AN 11.1's relation to AN 10.1, the Elevens "
            "reopens the Tens' second discourse unchanged, without "
            "the extra closing line AN 11.1 added to its own "
            "predecessor."]),
        ("From near shore to far shore", [
            "The discourse's closing image is distinctive within this "
            "opening pair: good qualities are said to &lsquo;flow on "
            "and fill up from one to the other, for going from the "
            "near shore to the far shore&rsquo; &mdash; a "
            "river-crossing metaphor for the whole progression, absent "
            "from AN 11.1's own closing restatement."]),
        ("Why naturalness matters here", [
            "The discourse's real claim is about causal reliability, "
            "not merely inspiration: given genuine ethical conduct as "
            "the base, the remaining links are not separate "
            "achievements requiring separate effort or aspiration, but "
            "a single unfolding process that completes itself once "
            "correctly started."]),
    ],
    terms=[
        ("cetanāya karaṇīyaṁ",
         "&ldquo;need [not] make a wish&rdquo; &mdash; this discourse's "
         "own title phrase, insisting each link arises without "
         "deliberate intention."),
        ("dhammatā esā",
         "&ldquo;it's only natural&rdquo; &mdash; the shared refrain "
         "closing each of the ten steps in this discourse."),
        ("kāyapassaddhi",
         "&ldquo;tranquility [of the body]&rdquo; &mdash; the fourth "
         "link, specified here as bodily tranquility following rapture, "
         "more precise than AN 11.1's bare &lsquo;tranquility&rsquo;."),
        ("orimā tīrā pārimaṁ tīraṁ gamanāya",
         "&ldquo;from the near shore to the far shore&rdquo; &mdash; "
         "this discourse's own closing image, absent from AN 11.1's "
         "restatement of the same chain."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the "
         "tenth and final link, identical to AN 11.1's own closing "
         "term."),
    ],
    text_intro=(
        "The discourse in full: the same ten links as AN 11.1, now "
        "framed as natural consequence requiring no wish. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten links, unfolding naturally"),
        ("p", "&sect;1", "an11.2:1.1-10.3"),
        ("h3", "The chain, restated in full"),
        ("p", "&sect;2", "an11.2:11.1-11.2"),
    ],
    quiz=[
        {"q": "How does this discourse's ten links compare to AN "
              "11.1's?",
         "opts": [
             "Entirely different content",
             "The identical ten links in the same order, framed "
             "as natural consequence rather than questioned goal",
             "Half as many links",
             "A different closing link"],
         "correct": 1,
         "expl": "Same chain, reframed from questioning to natural "
                 "unfolding."},
        {"q": "What refrain closes each of the ten steps in this "
              "discourse?",
         "opts": [
             "\"What is the goal and benefit?\"",
             "\"It's only natural\" (dhammatā esā)",
             "\"This is peaceful, this is sublime\"",
             "No refrain is used"],
         "correct": 1,
         "expl": "Each stage arises naturally from the one before, "
                 "with no wish required."},
        {"q": "What image closes this discourse that AN 11.1 does not "
              "use?",
         "opts": [
             "A tree with branches and foliage",
             "The near shore to the far shore, a river-crossing "
             "metaphor for the whole progression",
             "A thoroughbred horse",
             "A cowherd with eleven factors"],
         "correct": 1,
         "expl": "Distinctive to this discourse among the opening "
                 "pair."},
        {"q": "According to the guide, what is this discourse's "
              "relation to AN 10.2?",
         "opts": [
             "No relation at all",
             "Word-for-word identical content, reopened unchanged in "
             "the new nipāta",
             "A shortened summary",
             "A contradiction of it"],
         "correct": 1,
         "expl": "Like AN 11.1 and AN 10.1, this pair repeats the Tens' "
                 "content unchanged."},
        {"q": "What is the discourse's real claim, according to the "
              "guide?",
         "opts": [
             "That wishing hard enough produces results",
             "A claim about causal reliability: the sequence completes "
             "itself once genuine ethical conduct is the base",
             "That ethics is optional",
             "That each stage requires separate effort"],
         "correct": 1,
         "expl": "Not mere inspiration, but a claim about what follows "
                 "reliably from what."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, on Vulture's Peak",
             "No setting is stated in the source",
             "Ñātika, in the brick house"],
         "correct": 2,
         "expl": "No scene is set; the Buddha addresses the mendicants "
                 "directly."},
    ],
    marginalia=[
        ("No wish required", [
            "each stage flows from the last",
            "only naturally &mdash;",
            "nothing to strive for",
        ]),
        ("Near shore to far shore", [
            "good qualities filling up,",
            "flowing on and on,",
            "crossing to the far bank",
        ]),
        ("The same pair, one nipāta later", [
            "AN 10.2's own words",
            "reopened here unchanged &mdash;",
            "no eleventh line",
        ]),
        ("Cross-references", [
            "AN 11.1 &middot; previous, the same chain built by "
            "questioning",
            "AN 10.2 &middot; the identical discourse in the Book of "
            "the Tens",
            "AN 11.3 &middot; next, the same chain as destroyed or "
            "fulfilled vital conditions",
        ]),
    ],
    further=[
        '<a href="%s/an11.2/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.1.html">AN 11.1</a> &mdash; previous.',
        '<a href="an-11.3.html">AN 11.3 &middot; Vital Conditions (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.3 — Paṭhamaupanisāsutta
# --------------------------------------------------------------------------- #
page(
    3, "Paṭhamaupanisā", "Vital Conditions (1st)",
    vagga=VAGGA_1,
    meta_title="AN 11.3 — Vital Conditions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamaupanisāsutta, recasting the ten-link chain as "
        "vital conditions destroyed or fulfilled, with the famous "
        "branchless-tree simile. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same ten-link chain as vital conditions, each "
                 "destroying or fulfilling the next, with a paired "
                 "tree simile"),
        ("Length", "~2 minutes to read"),
        ("A third framing", "The same chain now cast causally: lacking "
         "one link destroys the vital condition for the next"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the causal vocabulary (upanisā) is new to this "
                       "chapter"),
    ],
    why=(
        "An unethical person destroys the vital condition for freedom "
        "from regret, and so on down the same ten-link chain to the "
        "knowledge and vision of freedom, exactly as a branchless tree "
        "cannot grow to fullness; an ethical person fulfills each "
        "vital condition in turn, exactly as a tree complete with "
        "branches and foliage grows to fullness."),
    guide=[
        ("The teaching in one sentence", [
            "Each link in the familiar ten-link chain is a "
            "&lsquo;vital condition&rsquo; (upanisā) for the next: "
            "lacking ethics destroys the condition for freedom from "
            "regret, and so on up to the knowledge and vision of "
            "freedom, exactly as lacking branches and foliage prevents "
            "a tree's shoots and heartwood from growing to fullness."]),
        ("A third framing of the same chain", [
            "This is the third discourse running to use this "
            "project's now-familiar ten-link chain: AN 11.1 questioned "
            "it, AN 11.2 called it natural, and this discourse recasts "
            "it as strict causal dependency, using the technical term "
            "<em>upanisā</em> &mdash; vital condition, proximate cause "
            "&mdash; that also names the Upanisā Sutta pattern met "
            "earlier in this project at AN 7.65."]),
        ("The branchless tree", [
            "The simile is symmetrical and vivid: a tree lacking "
            "branches and foliage cannot grow its shoots, bark, "
            "softwood, or heartwood to fullness, just as an unethical "
            "person cannot fulfill any of the ten downstream "
            "conditions; a tree complete with branches and foliage "
            "grows fully, just as an ethical person fulfills every "
            "condition in turn."]),
        ("Destruction and fulfillment as mirror structures", [
            "The discourse states the negative chain first in full "
            "(ten destroyed conditions), then abbreviates its own "
            "tree simile with an ellipsis before restating the "
            "positive chain in full and abbreviating the second tree "
            "simile the same way &mdash; a deliberately symmetrical "
            "construction that this chapter's next two discourses will "
            "repeat nearly verbatim, spoken by different speakers."]),
    ],
    terms=[
        ("upanisā",
         "&ldquo;vital condition&rdquo;, proximate cause &mdash; the "
         "technical term giving this discourse its title, also met at "
         "AN 7.65's own Upanisā Sutta."),
        ("vihiṁsitāyaṁ hoti upanisā",
         "&ldquo;has destroyed a vital condition&rdquo; &mdash; the "
         "refrain opening the negative chain, one link at a time."),
        ("paripūritāyaṁ hoti upanisā",
         "&ldquo;has fulfilled a vital condition&rdquo; &mdash; the "
         "mirror refrain opening the positive chain."),
        ("sākhāpalāsa",
         "&ldquo;branches and foliage&rdquo; &mdash; what the simile "
         "tree lacks or has, standing for ethics as the base condition "
         "for everything downstream."),
        ("pheggu sāra",
         "&ldquo;softwood, heartwood&rdquo; &mdash; the tree's "
         "innermost growth, standing for the chain's furthest links, "
         "reachable only once the nearer conditions are met."),
    ],
    text_intro=(
        "The discourse in full: the ten-link chain as destroyed or "
        "fulfilled vital conditions, each paired with a tree simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Destroyed, like a branchless tree"),
        ("p", "&sect;1", "an11.3:1.1-2.4"),
        ("h3", "Fulfilled, like a tree in full leaf"),
        ("p", "&sect;2", "an11.3:3.1-4.4"),
    ],
    quiz=[
        {"q": "What does the term \"upanisā\" mean in this discourse's "
              "title?",
         "opts": [
             "A type of meditation posture",
             "A vital condition, or proximate cause",
             "A monastic robe",
             "A place name"],
         "correct": 1,
         "expl": "The same technical term met earlier at AN 7.65's "
                 "Upanisā Sutta."},
        {"q": "What does the tree simile illustrate?",
         "opts": [
             "That trees should be planted near monasteries",
             "That lacking branches and foliage prevents a tree's "
             "shoots and heartwood from growing, just as lacking "
             "ethics destroys the downstream conditions",
             "A story about a specific historical tree",
             "Nothing related to the chain"],
         "correct": 1,
         "expl": "A symmetrical simile for destroyed or fulfilled "
                 "conditions."},
        {"q": "According to the guide, this is which framing of the "
              "familiar ten-link chain?",
         "opts": [
             "The first framing this project has met",
             "The third framing running, after questioning (AN 11.1) "
             "and naturalness (AN 11.2)",
             "An entirely unrelated chain",
             "A four-link chain"],
         "correct": 1,
         "expl": "Three consecutive discourses recast the same chain "
                 "three different ways."},
        {"q": "How is the discourse's structure symmetrical, according "
              "to the guide?",
         "opts": [
             "It has no discernible structure",
             "Negative chain and tree simile mirror positive chain and "
             "tree simile, each abbreviated with an ellipsis the same "
             "way",
             "Only the negative half is given",
             "Only the positive half is given"],
         "correct": 1,
         "expl": "A deliberately paired construction, repeated by the "
                 "chapter's next two discourses."},
        {"q": "What does the guide say about this discourse's relation "
              "to the chapter's next two discourses?",
         "opts": [
             "They are unrelated in content",
             "They repeat this same structure nearly verbatim, spoken "
             "by different speakers",
             "They contradict this discourse",
             "They abandon the tree simile entirely"],
         "correct": 1,
         "expl": "AN 11.4 and AN 11.5 restate this content, spoken by "
                 "Sāriputta and Ānanda respectively."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No scene is set; the Buddha addresses the mendicants "
                 "directly."},
    ],
    marginalia=[
        ("Vital conditions, chained", [
            "each link the ground",
            "for the one that follows &mdash;",
            "destroyed, or fulfilled",
        ]),
        ("The branchless tree", [
            "no branches, no leaves &mdash;",
            "shoots and heartwood cannot",
            "grow to their fullness",
        ]),
        ("A third framing", [
            "questioned, then natural,",
            "now causal &mdash; the same ten",
            "links, seen three ways",
        ]),
        ("Cross-references", [
            "AN 7.65 &middot; the earlier Upanisā Sutta, source of "
            "this discourse's key term",
            "AN 11.2 &middot; previous, the same chain as natural "
            "consequence",
            "AN 11.4 &middot; next, the same content spoken by "
            "Sāriputta",
        ]),
    ],
    further=[
        '<a href="%s/an11.3/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.2.html">AN 11.2</a> &mdash; previous.',
        '<a href="an-11.4.html">AN 11.4 &middot; Vital Conditions (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.4 — Dutiyaupanisāsutta
# --------------------------------------------------------------------------- #
page(
    4, "Dutiyaupanisā", "Vital Conditions (2nd)",
    vagga=VAGGA_1,
    meta_title="AN 11.4 — Vital Conditions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaupanisāsutta, in which Venerable Sāriputta restates "
        "AN 11.3's vital-conditions chain and tree simile to the "
        "mendicants directly. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Sāriputta addressing the mendicants"),
        ("Form", "AN 11.3's identical vital-conditions chain and tree "
                 "simile, now spoken by a disciple rather than the "
                 "Buddha"),
        ("Length", "~2 minutes to read"),
        ("Same content, different speaker", "Word-for-word AN 11.3, "
         "reassigned to Sāriputta addressing the mendicants directly"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to AN 11.3, the interest is "
                       "entirely in who now speaks it"),
    ],
    why=(
        "Venerable Sāriputta himself addresses the mendicants and "
        "restates AN 11.3's teaching word for word: an unethical "
        "person destroys the vital condition for freedom from regret, "
        "and so on down the same ten-link chain, exactly as a "
        "branchless tree cannot grow to fullness; an ethical person "
        "fulfills each condition in turn, exactly as a tree complete "
        "with branches and foliage grows to fullness."),
    guide=[
        ("The teaching in one sentence", [
            "Venerable Sāriputta restates AN 11.3's teaching to the "
            "mendicants directly, unchanged: each link in the ten-link "
            "chain is a vital condition for the next, destroyed by "
            "its absence or fulfilled by its presence, exactly as a "
            "tree lacking or having branches and foliage."]),
        ("A disciple speaks the Buddha's own words", [
            "This discourse opens not with the Buddha addressing the "
            "mendicants but with Sāriputta himself calling out "
            "&lsquo;Reverends, mendicants!&rsquo; and delivering the "
            "identical teaching just given at AN 11.3 &mdash; a "
            "familiar pattern in this project of a senior disciple "
            "restating the Buddha's own teaching under his own "
            "authority, without any framing narrative explaining why."]),
        ("What changes, and what does not", [
            "Every substantive line of the vital-conditions chain and "
            "both tree similes matches AN 11.3 exactly; the only "
            "difference is the opening frame identifying Sāriputta as "
            "speaker and the mendicants, rather than an unnamed "
            "audience, as those addressed &mdash; content and "
            "authority are treated as fully separable here."]),
        ("A pattern this project has met before", [
            "The move of reassigning an identical teaching to a named "
            "disciple, without further comment on why, echoes earlier "
            "instances across this project where the Buddha's own "
            "teaching is restated by Sāriputta, Ānanda, or Mahākaccāna "
            "&mdash; treated as carrying full authority simply because "
            "the content is identical, not because a narrative "
            "justifies the substitution."]),
    ],
    terms=[
        ("āvuso bhikkhave",
         "&ldquo;Reverends, mendicants!&rdquo; &mdash; Sāriputta's own "
         "address to the assembly, distinct from the Buddha's usual "
         "&lsquo;bhikkhave&rsquo; alone."),
        ("upanisā",
         "&ldquo;vital condition&rdquo;, proximate cause &mdash; "
         "identical in meaning and use to AN 11.3's own key term."),
        ("vihiṁsitāyaṁ hoti upanisā",
         "&ldquo;has destroyed a vital condition&rdquo; &mdash; the "
         "same refrain opening the negative chain, unchanged from AN "
         "11.3."),
        ("paripūritāyaṁ hoti upanisā",
         "&ldquo;has fulfilled a vital condition&rdquo; &mdash; the "
         "same mirror refrain opening the positive chain."),
        ("sākhāpalāsa",
         "&ldquo;branches and foliage&rdquo; &mdash; the identical "
         "simile vocabulary carried over unchanged from AN 11.3."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta's restatement of AN 11.3's "
        "vital-conditions chain and tree simile. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta addresses the mendicants"),
        ("p", "&sect;1", "an11.4:1.1-1.4"),
        ("h3", "Destroyed, like a branchless tree"),
        ("p", "&sect;2", "an11.4:2.1-3.4"),
        ("h3", "Fulfilled, like a tree in full leaf"),
        ("p", "&sect;3", "an11.4:4.1-5.4"),
    ],
    quiz=[
        {"q": "Who speaks this discourse's teaching?",
         "opts": [
             "The Buddha, as at AN 11.3",
             "Venerable Sāriputta, addressing the mendicants directly",
             "Venerable Ānanda",
             "A group of unnamed mendicants"],
         "correct": 1,
         "expl": "Sāriputta calls out to the assembly and delivers the "
                 "teaching under his own authority."},
        {"q": "How does this discourse's content compare to AN 11.3's?",
         "opts": [
             "Entirely different teaching",
             "Word-for-word identical, with only the speaker and "
             "opening frame changed",
             "A shortened summary",
             "The tree simile is dropped"],
         "correct": 1,
         "expl": "Every substantive line matches AN 11.3 exactly."},
        {"q": "According to the guide, what pattern does this "
              "discourse illustrate?",
         "opts": [
             "That only the Buddha may teach",
             "A senior disciple restating the Buddha's own teaching "
             "under his own authority, without explanatory narrative",
             "That Sāriputta corrects the Buddha",
             "A completely new teaching method"],
         "correct": 1,
         "expl": "Content and authority are treated as separable, "
                 "echoing earlier instances across this project."},
        {"q": "What is Sāriputta's own address to the assembly?",
         "opts": [
             "\"Bhikkhave\" alone, as the Buddha usually says",
             "\"Reverends, mendicants!\" (āvuso bhikkhave)",
             "No address is given",
             "\"Sir\""],
         "correct": 1,
         "expl": "Distinct phrasing from the Buddha's own usual "
                 "opening."},
        {"q": "What illustrates the destroyed or fulfilled vital "
              "conditions in this discourse?",
         "opts": [
             "A cowherd with eleven factors",
             "A tree lacking or having branches and foliage",
             "A thoroughbred horse",
             "A wanderers' feeding ground"],
         "correct": 1,
         "expl": "The identical tree simile carried over unchanged "
                 "from AN 11.3."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No scene is set beyond Sāriputta addressing the "
                 "mendicants."},
    ],
    marginalia=[
        ("A disciple's own voice", [
            "\"Reverends, mendicants!\" &mdash;",
            "Sāriputta calls out,",
            "then speaks unchanged",
        ]),
        ("The same tree again", [
            "branchless, it cannot",
            "grow &mdash; complete with leaf and",
            "branch, it grows to full",
        ]),
        ("Content over authority", [
            "the words are the same",
            "as the Buddha's own &mdash;",
            "only the speaker shifts",
        ]),
        ("Cross-references", [
            "AN 11.3 &middot; previous, the Buddha's own version of "
            "this identical teaching",
            "AN 11.5 &middot; next, the same content spoken by Ānanda",
        ]),
    ],
    further=[
        '<a href="%s/an11.4/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.3.html">AN 11.3</a> &mdash; previous.',
        '<a href="an-11.5.html">AN 11.5 &middot; Vital Conditions (3rd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.5 — Tatiyaupanisāsutta
# --------------------------------------------------------------------------- #
page(
    5, "Tatiyaupanisā", "Vital Conditions (3rd)",
    vagga=VAGGA_1,
    meta_title="AN 11.5 — Vital Conditions (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Tatiyaupanisāsutta, in which Venerable Ānanda restates "
        "the same vital-conditions chain and tree simile a third "
        "time. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda addressing the mendicants"),
        ("Form", "The identical vital-conditions chain and tree "
                 "simile, now spoken by a second named disciple"),
        ("Length", "~2 minutes to read"),
        ("A third speaker, same content", "The same chain given by "
         "the Buddha (AN 11.3) and Sāriputta (AN 11.4), now by Ānanda"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to the previous two "
                       "discourses"),
    ],
    why=(
        "Venerable Ānanda himself addresses the mendicants and "
        "restates the same teaching a third time: an unethical person "
        "destroys the vital condition for freedom from regret, and so "
        "on down the same ten-link chain, exactly as a branchless tree "
        "cannot grow to fullness; an ethical person fulfills each "
        "condition in turn, exactly as a tree complete with branches "
        "and foliage grows to fullness."),
    guide=[
        ("The teaching in one sentence", [
            "Venerable Ānanda restates the same vital-conditions "
            "teaching a third time: each link in the ten-link chain "
            "is a vital condition for the next, destroyed by its "
            "absence or fulfilled by its presence, exactly as a tree "
            "lacking or having branches and foliage."]),
        ("Three speakers, one teaching", [
            "This is the third consecutive discourse to give this "
            "identical vital-conditions teaching: the Buddha at AN "
            "11.3, Sāriputta at AN 11.4, and now Ānanda &mdash; a "
            "triple repetition this project has not seen assembled "
            "quite this compactly before, three named speakers in a "
            "row delivering the same content unchanged."]),
        ("A slightly different opening", [
            "Unlike AN 11.4's clean break into Sāriputta's own address, "
            "this discourse's opening line runs the frame and the "
            "teaching's first line together in a single segment "
            "&mdash; &lsquo;There Venerable Ānanda addressed the "
            "mendicants&hellip; An unethical person&hellip;&rsquo; "
            "&mdash; a minor segmentation difference in the source "
            "worth noting rather than a substantive change."]),
        ("Why three speakers might matter", [
            "Read together, these three discourses model something "
            "beyond the content itself: a teaching genuinely "
            "understood does not remain the Buddha's alone but "
            "becomes freely repeatable by his senior disciples, each "
            "carrying full authority, with no discourse marking one "
            "version as more authoritative than another."]),
    ],
    terms=[
        ("upanisā",
         "&ldquo;vital condition&rdquo;, proximate cause &mdash; the "
         "same key term shared across all three discourses of this "
         "sequence."),
        ("vihiṁsitāyaṁ hoti upanisā",
         "&ldquo;has destroyed a vital condition&rdquo; &mdash; the "
         "same refrain opening the negative chain, unchanged for a "
         "third time."),
        ("paripūritāyaṁ hoti upanisā",
         "&ldquo;has fulfilled a vital condition&rdquo; &mdash; the "
         "same mirror refrain opening the positive chain."),
        ("sākhāpalāsa",
         "&ldquo;branches and foliage&rdquo; &mdash; the identical "
         "simile vocabulary, carried over unchanged for a third time."),
        ("āyasmā ānando bhikkhū āmantesi",
         "&ldquo;Venerable Ānanda addressed the mendicants&rdquo; "
         "&mdash; this discourse's own opening frame, run together "
         "with the teaching's first line in a single source segment."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's restatement of the same "
        "vital-conditions chain and tree simile. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Destroyed, like a branchless tree"),
        ("p", "&sect;1", "an11.5:1.1-2.4"),
        ("h3", "Fulfilled, like a tree in full leaf"),
        ("p", "&sect;2", "an11.5:3.1-4.4"),
    ],
    quiz=[
        {"q": "Who speaks this discourse's teaching?",
         "opts": [
             "The Buddha", "Venerable Sāriputta",
             "Venerable Ānanda, addressing the mendicants",
             "A group of unnamed mendicants"],
         "correct": 2,
         "expl": "The third named speaker in this three-discourse "
                 "sequence."},
        {"q": "According to the guide, what makes this discourse "
              "notable as a set with AN 11.3 and AN 11.4?",
         "opts": [
             "Each gives contradictory content",
             "Three consecutive discourses give the identical "
             "vital-conditions teaching through three different named "
             "speakers",
             "Only this discourse includes the tree simile",
             "They are unrelated to each other"],
         "correct": 1,
         "expl": "A triple repetition assembled compactly: Buddha, "
                 "Sāriputta, Ānanda."},
        {"q": "What minor difference does the guide note in this "
              "discourse's opening?",
         "opts": [
             "It omits the tree simile entirely",
             "The frame and the teaching's first line run together in "
             "a single source segment, unlike AN 11.4's clean break",
             "It adds an entirely new simile",
             "It changes the chain's order"],
         "correct": 1,
         "expl": "A segmentation difference in the source, not a "
                 "substantive change."},
        {"q": "What does the guide suggest the three-speaker "
              "structure might model?",
         "opts": [
             "That only the Buddha's own words carry authority",
             "That a genuinely understood teaching becomes freely "
             "repeatable by senior disciples with full authority",
             "That disciples must always ask permission to teach",
             "Nothing beyond simple repetition"],
         "correct": 1,
         "expl": "No discourse marks one version as more authoritative "
                 "than another."},
        {"q": "What illustrates the destroyed or fulfilled vital "
              "conditions in this discourse?",
         "opts": [
             "A cowherd with eleven factors",
             "A tree lacking or having branches and foliage",
             "A thoroughbred horse",
             "A wanderers' feeding ground"],
         "correct": 1,
         "expl": "The identical tree simile carried over for a third "
                 "time."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No scene is set beyond Ānanda addressing the "
                 "mendicants."},
    ],
    marginalia=[
        ("A third voice", [
            "Buddha, Sāriputta,",
            "now Ānanda speaks it &mdash;",
            "the words still unchanged",
        ]),
        ("The same tree, once more", [
            "branchless, it cannot",
            "grow &mdash; complete with leaf and",
            "branch, it grows to full",
        ]),
        ("Teaching beyond the teacher", [
            "understood fully,",
            "a teaching becomes free &mdash;",
            "repeatable by all",
        ]),
        ("Cross-references", [
            "AN 11.3 &middot; the Buddha's own version, opening this "
            "three-discourse sequence",
            "AN 11.4 &middot; previous, Sāriputta's version",
            "AN 11.6 &middot; next, eleven disasters for abusing the "
            "noble ones",
        ]),
    ],
    further=[
        '<a href="%s/an11.5/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.4.html">AN 11.4</a> &mdash; previous.',
        '<a href="an-11.6.html">AN 11.6 &middot; Disasters</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.6 — Byasanasutta
# --------------------------------------------------------------------------- #
page(
    6, "Byasana", "Disasters",
    vagga=VAGGA_1,
    meta_title="AN 11.6 — Disasters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Byasanasutta, warning that abusing and denouncing the "
        "noble ones leads without doubt to one of eleven disasters, "
        "from failed practice to rebirth in hell. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eleven disasters listed for abusing the noble ones, "
                 "then the same eleven restated as avoided by not "
                 "doing so"),
        ("Length", "~2 minutes to read"),
        ("A genuine eleven-item list", "Unlike the chapter's opening "
         "discourses, this list is natively eleven items, not a "
         "ten-link chain padded by one"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a stark warning, worth reading slowly for its "
                       "specific items"),
    ],
    why=(
        "Any mendicant who abuses and insults their spiritual "
        "companions, denouncing the noble ones, will without doubt "
        "fall into one of eleven disasters &mdash; from failing to "
        "achieve what is unachieved to rebirth in hell &mdash; while "
        "any mendicant who does not will, without doubt, avoid every "
        "one of them."),
    guide=[
        ("The teaching in one sentence", [
            "Abusing and insulting one's spiritual companions, "
            "denouncing the noble ones, leads without doubt to one of "
            "eleven disasters, from failing to progress in practice "
            "to rebirth in hell; refraining from such abuse avoids "
            "every one of them."]),
        ("A genuinely eleven-item list", [
            "Unlike this chapter's first five discourses, which "
            "extend or repeat the Tens' own ten-link chain, this "
            "discourse's eleven disasters are native to this nipāta "
            "&mdash; a list this project has not met in this form "
            "before, marking a real shift in content rather than "
            "another variation on familiar material."]),
        ("The eleven disasters themselves", [
            "The list runs from subtle failures of practice (not "
            "achieving the unachieved, what has been achieved falling "
            "away, good qualities left unrefined or overestimated, "
            "dissatisfaction in the spiritual life) through concrete "
            "harms (committing a corrupt offense, resigning the "
            "training, severe illness, madness) to the final and "
            "gravest outcome, rebirth in hell &mdash; a graduated "
            "sequence from spiritual to physical to karmic "
            "consequence."]),
        ("Symmetry without a simile", [
            "Unlike the previous three discourses' shared tree simile, "
            "this discourse achieves its negative-positive symmetry "
            "through plain restatement alone: the same eleven items, "
            "first as disasters that follow from abuse, then as "
            "disasters avoided by its absence, with no supporting "
            "image required."]),
    ],
    terms=[
        ("byasana",
         "&ldquo;disaster&rdquo; &mdash; this discourse's own title "
         "term, the graduated list of eleven outcomes it names."),
        ("sabrahmacārī paribhāsati apasādeti",
         "&ldquo;abuses and insults their spiritual companions&rdquo; "
         "&mdash; the triggering act that sets the entire chain of "
         "disasters in motion."),
        ("ariyūpavādaka",
         "&ldquo;denouncing the noble ones&rdquo; &mdash; a "
         "particularly serious form of the same abuse, singled out "
         "explicitly in the discourse's framing."),
        ("dussīlyaṁ āpajjati",
         "&ldquo;commits a corrupt offense&rdquo; &mdash; the seventh "
         "disaster, a concrete monastic transgression amid the more "
         "abstract failures around it."),
        ("apāyaṁ duggatiṁ vinipātaṁ nirayaṁ upapajjati",
         "&ldquo;reborn in a place of loss, a bad place, the "
         "underworld, hell&rdquo; &mdash; the eleventh and final "
         "disaster, the gravest possible outcome closing both lists."),
    ],
    text_intro=(
        "The discourse in full: eleven disasters for abusing the "
        "noble ones, then the same eleven avoided by refraining. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eleven disasters, for abusing the noble ones"),
        ("p", "&sect;1", "an11.6:1.1-2.13"),
        ("h3", "Eleven disasters, avoided"),
        ("p", "&sect;2", "an11.6:3.1-4.13"),
    ],
    quiz=[
        {"q": "What triggers the eleven disasters in this discourse?",
         "opts": [
             "Breaking a minor monastic rule",
             "Abusing and insulting one's spiritual companions, "
             "denouncing the noble ones",
             "Eating after noon",
             "Failing to meditate daily"],
         "correct": 1,
         "expl": "The act named explicitly in the discourse's opening "
                 "line."},
        {"q": "According to the guide, how does this discourse's "
              "eleven-item list differ from the chapter's first five "
              "discourses?",
         "opts": [
             "It is identical to their ten-link chain",
             "It is a genuinely native eleven-item list, not the "
             "Tens' ten-link chain padded by one",
             "It has only nine items",
             "It repeats the tree simile"],
         "correct": 1,
         "expl": "A real shift in content, not another variation on "
                 "familiar material."},
        {"q": "What is the eleventh and gravest disaster listed?",
         "opts": [
             "Severe illness",
             "Rebirth in a place of loss, a bad place, the underworld, "
             "hell",
             "Resigning the training",
             "Losing one's mind"],
         "correct": 1,
         "expl": "The final and gravest outcome closing both the "
                 "negative and positive lists."},
        {"q": "How does the guide describe the list's overall "
              "sequence?",
         "opts": [
             "Random, with no discernible order",
             "Graduated, from subtle failures of practice through "
             "concrete harms to karmic rebirth",
             "Purely physical harms only",
             "Purely spiritual failures only"],
         "correct": 1,
         "expl": "A sequence moving from spiritual to physical to "
                 "karmic consequence."},
        {"q": "How does this discourse achieve its negative-positive "
              "symmetry, according to the guide?",
         "opts": [
             "Through the branchless-tree simile",
             "Through plain restatement alone, without a supporting "
             "image",
             "Through a cowherd simile",
             "It does not achieve symmetry"],
         "correct": 1,
         "expl": "Unlike the previous three discourses' shared tree "
                 "simile."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No scene is set; the Buddha addresses the mendicants "
                 "directly."},
    ],
    marginalia=[
        ("Eleven disasters", [
            "from failed practice",
            "to illness, madness, and",
            "at last, to hell itself",
        ]),
        ("Abuse, denounced", [
            "insulting companions,",
            "denouncing the noble ones &mdash;",
            "the act that sets it off",
        ]),
        ("A new kind of list", [
            "not the old ten links",
            "padded by one &mdash; genuinely",
            "eleven from the start",
        ]),
        ("Cross-references", [
            "AN 11.3&ndash;5 &middot; previous three, the shared "
            "vital-conditions chain and tree simile",
            "AN 11.7 &middot; next, a state of immersion beyond all "
            "perception",
        ]),
    ],
    further=[
        '<a href="%s/an11.6/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.5.html">AN 11.5</a> &mdash; previous.',
        '<a href="an-11.7.html">AN 11.7 &middot; Percipient</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.7 — Saññāsutta
# --------------------------------------------------------------------------- #
page(
    7, "Saññā", "Percipient",
    vagga=VAGGA_1,
    meta_title="AN 11.7 — Percipient | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Saññāsutta, in which Ānanda asks the Buddha about a "
        "state of immersion beyond all ordinary perception, then "
        "confirms the same answer independently from Sāriputta. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda questioning first the Buddha, "
                     "then Venerable Sāriputta"),
        ("Form", "A single question posed twice to two different "
                 "teachers, receiving the identical answer both times"),
        ("Length", "~3 minutes to read"),
        ("Chapter's transition", "The first of several discourses in "
         "this chapter exploring an immersion beyond all sensory and "
         "formless perception"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "a demanding description of an advanced "
                       "meditative state"),
    ],
    why=(
        "Ānanda asks whether a mendicant might gain a state of "
        "immersion where nothing at all is perceived in its usual "
        "way &mdash; not the elements, not the formless dimensions, "
        "not this world or another, not anything seen, heard, "
        "thought, or known &mdash; and yet still perceive; the Buddha "
        "confirms it is possible, through perceiving only that "
        "&lsquo;this is peaceful, this is sublime&rsquo;, the stilling "
        "of all activities and the ending of craving &mdash; and "
        "Sāriputta, asked the same question separately, gives the "
        "identical answer."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant can gain a state of immersion where nothing "
            "is perceived in its ordinary way &mdash; not the "
            "elements, the formless dimensions, this world or "
            "another, or anything seen, heard, thought, or known "
            "&mdash; and yet still perceive, by perceiving only the "
            "peace of nibbāna itself: the stilling of all activities, "
            "the ending of craving, fading away, cessation."]),
        ("An exhaustive list of what is not perceived", [
            "The question's own list is comprehensive by design: the "
            "four elements, the four formless dimensions, this world "
            "and the other world, and everything reached by the six "
            "senses including the mind &mdash; nothing conventional "
            "remains as an object of perception, and yet the "
            "discourse insists perception itself has not stopped."]),
        ("Two teachers, one answer", [
            "Having received the Buddha's answer, Ānanda does not "
            "simply accept it and move on: he independently poses the "
            "identical question to Sāriputta, without revealing he "
            "has already asked the Buddha, and receives word-for-word "
            "the same reply &mdash; a deliberate test of whether the "
            "teaching holds independent of its source."]),
        ("Why the agreement matters", [
            "Ānanda's own closing exclamation names the point "
            "directly: it is &lsquo;incredible, amazing&rsquo; that "
            "teacher and disciple agree without conflict on the chief "
            "matter, using the same words and phrases &mdash; genuine "
            "realization converges on identical expression, not "
            "merely similar meaning, when two people have actually "
            "understood the same thing."]),
    ],
    terms=[
        ("saññāvedayitanirodha",
         "not named directly here, but the immersion this discourse "
         "gestures toward &mdash; a state of &ldquo;yet still "
         "percipient&rdquo; despite the absence of every ordinary "
         "object of perception."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; the "
         "sole remaining perception in this immersion, describing "
         "nibbāna itself rather than any conditioned object."),
        ("sabbasaṅkhārasamatho sabbūpadhipaṭinissaggo taṇhākkhayo "
         "virāgo nirodho nibbānaṁ",
         "&ldquo;the stilling of all activities, the letting go of "
         "all attachments, the ending of craving, fading away, "
         "cessation, extinguishment&rdquo; &mdash; the full "
         "description of what is perceived when nothing conventional "
         "remains."),
        ("atthavyañjanasampanno",
         "roughly, the &ldquo;meaning and phrasing&rdquo; fitting "
         "together &mdash; Ānanda's own term for what he finds "
         "remarkable in the Buddha's and Sāriputta's matching "
         "answers."),
        ("acchariyaṁ abbhutaṁ",
         "&ldquo;incredible, amazing&rdquo; &mdash; Ānanda's own "
         "double exclamation, repeated at the discourse's close, "
         "marking his genuine astonishment at the agreement."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's question to the Buddha, then "
        "the same question independently confirmed by Sāriputta. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda asks the Buddha"),
        ("p", "&sect;1", "an11.7:1.1-6.2"),
        ("h3", "The same answer, confirmed by Sāriputta"),
        ("p", "&sect;2", "an11.7:7.1-10.6"),
    ],
    quiz=[
        {"q": "What does Ānanda ask the Buddha about?",
         "opts": [
             "How to build a monastery",
             "Whether a mendicant might gain a state of immersion "
             "beyond all ordinary perception, yet still perceive",
             "The rules of monastic discipline",
             "A dispute between two monks"],
         "correct": 1,
         "expl": "The discourse's central and demanding question."},
        {"q": "What is perceived in this state of immersion, "
              "according to the Buddha's answer?",
         "opts": [
             "Nothing whatsoever",
             "Only that \"this is peaceful, this is sublime\" — the "
             "stilling of all activities and the ending of craving",
             "The four elements in unusually vivid form",
             "A vision of a future Buddha"],
         "correct": 1,
         "expl": "The sole remaining perception, describing nibbāna "
                 "itself."},
        {"q": "What does Ānanda do after receiving the Buddha's "
              "answer?",
         "opts": [
             "Nothing further; the discourse ends there",
             "He independently asks Sāriputta the identical question, "
             "without revealing he had already asked the Buddha",
             "He asks the Buddha to repeat the answer",
             "He disputes the Buddha's answer"],
         "correct": 1,
         "expl": "A deliberate test of whether the teaching holds "
                 "independent of its source."},
        {"q": "How does Sāriputta's answer compare to the Buddha's?",
         "opts": [
             "It contradicts the Buddha's answer",
             "Word-for-word identical, using the same words and "
             "phrases",
             "A shorter summary only",
             "He declines to answer"],
         "correct": 1,
         "expl": "Ānanda himself marks this agreement as remarkable."},
        {"q": "According to the guide, what does Ānanda's closing "
              "exclamation emphasize?",
         "opts": [
             "That the teaching is too difficult to understand",
             "That genuine realization converges on identical "
             "expression, not merely similar meaning",
             "That Sāriputta is more advanced than the Buddha",
             "Disappointment at the answer"],
         "correct": 1,
         "expl": "Two people who have actually understood the same "
                 "thing express it identically."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No scene is set beyond Ānanda approaching the Buddha "
                 "and then Sāriputta."},
    ],
    marginalia=[
        ("Beyond all perceiving", [
            "no earth in earth, no",
            "world in world &mdash; yet somehow",
            "still, perception stays",
        ]),
        ("The peaceful, the sublime", [
            "one perception left:",
            "stilling, letting go, the end",
            "of craving itself",
        ]),
        ("Two teachers, one answer", [
            "asked twice, unrevealed &mdash;",
            "the same words come back both",
            "times, matched exactly",
        ]),
        ("Cross-references", [
            "AN 11.6 &middot; previous, eleven disasters for abusing "
            "the noble ones",
            "AN 11.8 &middot; next, the same immersion asked about "
            "again as \"focus\"",
        ]),
    ],
    further=[
        '<a href="%s/an11.7/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.6.html">AN 11.6</a> &mdash; previous.',
        '<a href="an-11.8.html">AN 11.8 &middot; Focus</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.8 — Manasikārasutta
# --------------------------------------------------------------------------- #
page(
    8, "Manasikāra", "Focus",
    vagga=VAGGA_1,
    meta_title="AN 11.8 — Focus | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Manasikārasutta, restating AN 11.7's immersion beyond "
        "all perception in terms of focus (manasikāra) instead, "
        "asked only of the Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda questioning the Buddha"),
        ("Form", "The same question and answer as AN 11.7, recast "
                 "from perception (saññā) to focus (manasikāra), "
                 "asked once only"),
        ("Length", "~2 minutes to read"),
        ("A single variable changed", "Same structure as AN 11.7 "
         "minus the Sāriputta confirmation, with one term swapped "
         "throughout"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the same demanding immersion as AN 11.7"),
    ],
    why=(
        "Ānanda asks whether a mendicant might gain a state of "
        "immersion where nothing at all is focused on in its usual "
        "way &mdash; not the six sense fields, not the elements, not "
        "the formless dimensions, not this world or another &mdash; "
        "and yet still focus; the Buddha confirms it, through "
        "focusing only on the peace of nibbāna itself: the stilling "
        "of all activities and the ending of craving."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant can gain a state of immersion where nothing "
            "conventional is focused on &mdash; not the six sense "
            "fields, the elements, the formless dimensions, or either "
            "world &mdash; and yet still focus, by focusing only on "
            "the peace of nibbāna: the stilling of all activities and "
            "the ending of craving."]),
        ("The same discourse, one term changed", [
            "This discourse is AN 11.7 in miniature: the identical "
            "question-and-answer structure, the identical closing "
            "formula about peace and stillness, with "
            "&lsquo;perceive&rsquo; (saññā) replaced throughout by "
            "&lsquo;focus&rsquo; (manasikāra) &mdash; and, unlike AN "
            "11.7, with one addition: the six sense fields (eye and "
            "sights, ear and sounds, and so on) are named explicitly "
            "as among what is not focused on, absent from AN 11.7's "
            "list."]),
        ("Why the added sense fields matter", [
            "AN 11.7's list moved directly from the four elements to "
            "the formless dimensions; this discourse's list opens "
            "with the six sense fields first &mdash; eye, ear, nose, "
            "tongue, body, and their objects &mdash; making explicit "
            "what AN 11.7 left implicit: that ordinary sensory "
            "engagement, not only elemental and formless perception, "
            "must also fall away in this immersion."]),
        ("No Sāriputta confirmation this time", [
            "Unlike AN 11.7's two-part structure, this discourse ends "
            "immediately after the Buddha's answer, with no parallel "
            "test of the teaching through a second teacher &mdash; a "
            "reminder that this chapter's pairs and near-repeats do "
            "not always follow the exact same shape twice."]),
    ],
    terms=[
        ("manasikāra",
         "&ldquo;focus&rdquo;, attention &mdash; this discourse's own "
         "key term, replacing AN 11.7's <em>saññā</em>, perception, "
         "throughout."),
        ("cakkhu rūpe, sotaṁ sadde",
         "&ldquo;the eye or sights, ear or sounds&rdquo; &mdash; the "
         "six sense fields, named explicitly here as not focused on, "
         "absent from AN 11.7's own list."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; the "
         "identical closing formula shared with AN 11.7, describing "
         "nibbāna itself."),
        ("sabbasaṅkhārasamatho sabbūpadhipaṭinissaggo taṇhākkhayo "
         "virāgo nirodho nibbānaṁ",
         "&ldquo;the stilling of all activities... extinguishment&rdquo; "
         "&mdash; the same full formula as AN 11.7, word for word."),
        ("upasaṅkamitvā",
         "&ldquo;went up to&rdquo; &mdash; the standard opening for "
         "Ānanda approaching the Buddha, identical to AN 11.7's own "
         "opening move."),
    ],
    text_intro=(
        "The discourse in full: Ānanda asks about an immersion beyond "
        "all focus, and the Buddha answers. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda asks, and the Buddha answers"),
        ("p", "&sect;1", "an11.8:1.1-5.5"),
    ],
    quiz=[
        {"q": "What term does this discourse use in place of AN "
              "11.7's \"perceive\" (saññā)?",
         "opts": [
             "\"Focus\" (manasikāra)",
             "\"Know\" (jānāti)",
             "\"See\" (passati)",
             "No substitution is made"],
         "correct": 0,
         "expl": "The same structure recast around a different term "
                 "throughout."},
        {"q": "What does this discourse add that AN 11.7 does not "
              "list explicitly?",
         "opts": [
             "The four formless dimensions",
             "The six sense fields — eye and sights, ear and sounds, "
             "and so on",
             "A description of hell",
             "A cowherd simile"],
         "correct": 1,
         "expl": "Making explicit what AN 11.7 left implicit about "
                 "ordinary sensory engagement."},
        {"q": "What is focused on in this state of immersion, "
              "according to the Buddha's answer?",
         "opts": [
             "Every sense object at once",
             "Only that \"this is peaceful, this is sublime\" — the "
             "same formula as AN 11.7",
             "Nothing whatsoever, even in principle",
             "A visualized deity"],
         "correct": 1,
         "expl": "Word for word the same closing formula as AN 11.7."},
        {"q": "How does this discourse's structure differ from AN "
              "11.7's, according to the guide?",
         "opts": [
             "It is much longer",
             "It ends after the Buddha's answer, without a parallel "
             "confirmation from Sāriputta",
             "It is spoken by Sāriputta instead of the Buddha",
             "It adds a third questioner"],
         "correct": 1,
         "expl": "This chapter's near-repeats do not always follow "
                 "the exact same shape twice."},
        {"q": "Who asks the question in this discourse?",
         "opts": [
             "Sāriputta", "Venerable Ānanda", "Venerable Sandha",
             "An unnamed mendicant"],
         "correct": 1,
         "expl": "The same questioner as AN 11.7, asking the Buddha "
                 "alone this time."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No scene is set beyond Ānanda approaching the "
                 "Buddha."},
    ],
    marginalia=[
        ("Focus, not perceiving", [
            "the same beyond-state,",
            "now named by a different",
            "word for the same thing",
        ]),
        ("Six sense fields, named", [
            "eye and sights, ear and",
            "sounds &mdash; explicit here, where",
            "AN 11.7 left them unsaid",
        ]),
        ("No second witness", [
            "just the Buddha's word",
            "this time &mdash; no Sāriputta",
            "called to confirm it",
        ]),
        ("Cross-references", [
            "AN 11.7 &middot; previous, the same immersion asked "
            "about as perception, confirmed twice",
            "AN 11.9 &middot; next, the thoroughbred and the wild colt",
        ]),
    ],
    further=[
        '<a href="%s/an11.8/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.7.html">AN 11.7</a> &mdash; previous.',
        '<a href="an-11.9.html">AN 11.9 &middot; With Sandha</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.9 — Saddhasutta
# --------------------------------------------------------------------------- #
page(
    9, "Saddha", "With Sandha",
    vagga=VAGGA_1,
    meta_title="AN 11.9 — With Sandha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Saddhasutta, the Buddha's famous instruction to "
        "Venerable Sandha to meditate like a thoroughbred, not a "
        "wild colt tied up thinking only of fodder. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NATIKA),
        ("Speakers", "The Buddha addressing Venerable Sandha"),
        ("Form", "A paired simile — the wild colt and the "
                 "thoroughbred — followed by a verse of homage from "
                 "the gods and a direct explanation"),
        ("Length", "~4 minutes to read"),
        ("A named disciple, a vivid simile", "One of this chapter's "
         "most narratively developed discourses, addressed to a "
         "specific named mendicant"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "a famous simile paired with a demanding "
                       "description of meditation without dependence"),
    ],
    why=(
        "The Buddha tells Venerable Sandha to meditate like a "
        "thoroughbred horse, not a wild colt tied to a feeding trough "
        "thinking only &lsquo;fodder, fodder!&rsquo;: a wild colt, "
        "like an ordinary meditator, remains dependent on what "
        "obstructs it and meditates dependent on the elements, the "
        "formless dimensions, and every object of the senses, while a "
        "thoroughbred meditates without any such dependence at all, "
        "the perception of every one of those things having simply "
        "vanished."),
    guide=[
        ("The teaching in one sentence", [
            "A wild colt tied to a feeding trough meditates only on "
            "&lsquo;fodder, fodder!&rsquo;, just as an ordinary "
            "meditator remains overcome by the hindrances and "
            "dependent on the elements, the formless dimensions, and "
            "every sense object; a thoroughbred meditates independent "
            "of all such things, the perception of each having simply "
            "vanished, yet still genuinely meditates."]),
        ("The wild colt's fodder", [
            "The simile's first half is vivid and specific: a wild "
            "colt tied up does not wonder what task the trainer has "
            "for it, but thinks only of the feed in front of it "
            "&mdash; matched to a person overcome by the five "
            "hindrances (sensual desire, ill will, dullness and "
            "drowsiness, restlessness and remorse, doubt) who "
            "meditates dependent on whatever object currently "
            "occupies the mind, from the elements up through the "
            "formless dimensions."]),
        ("The thoroughbred's independence", [
            "A fine thoroughbred, by contrast, regards even the "
            "trainer's goad as a debt or misfortune rather than "
            "something to resent, and a person free of the hindrances "
            "meditates dependent on nothing at all &mdash; not earth, "
            "water, fire, or air, not any formless dimension, not "
            "this world or another, not anything seen, heard, "
            "thought, or known. The gods themselves, unable to "
            "understand the basis of such absorption, pay homage from "
            "afar."]),
        ("How the thoroughbred actually meditates", [
            "Asked directly how this is possible, the Buddha explains "
            "that for such a person the very perception of each of "
            "these things &mdash; earth, water, the formless "
            "dimensions, this world, the other world, everything "
            "reached by the six senses &mdash; has vanished entirely, "
            "echoing the same &lsquo;beyond all perceiving, yet still "
            "perceiving&rsquo; territory explored at AN 11.7 and AN "
            "11.8, now delivered through narrative and simile rather "
            "than dialogue alone."]),
    ],
    terms=[
        ("ājānīya",
         "&ldquo;thoroughbred&rdquo; &mdash; the discourse's central "
         "image for a meditator free of dependence, contrasted "
         "throughout with the wild colt."),
        ("khaḷuṅka",
         "&ldquo;wild colt&rdquo; &mdash; the untrained horse tied to "
         "a feeding trough, standing for a meditator still overcome "
         "by the five hindrances."),
        ("nīvaraṇa",
         "&ldquo;hindrance&rdquo; &mdash; the five obstacles (sensual "
         "desire, ill will, dullness and drowsiness, restlessness and "
         "remorse, doubt) that keep the wild-colt meditator dependent."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; not "
         "used verbatim here, but the same underlying territory as AN "
         "11.7 and AN 11.8's shared closing formula."),
        ("saññā antarahitā hoti",
         "&ldquo;the perception... has vanished&rdquo; &mdash; the "
         "Buddha's direct answer to Sandha, describing how the "
         "thoroughbred meditates without dependence."),
    ],
    text_intro=(
        "The discourse in full: the wild colt, the thoroughbred, the "
        "gods' verse of homage, and the Buddha's direct explanation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The wild colt"),
        ("p", "&sect;1", "an11.9:1.1-2.17"),
        ("h3", "The thoroughbred"),
        ("p", "&sect;2", "an11.9:3.1-4.4"),
        ("h3", "How the thoroughbred meditates"),
        ("p", "&sect;3", "an11.9:5.1-8.4"),
    ],
    quiz=[
        {"q": "What does the wild colt tied to a feeding trough think "
              "of?",
         "opts": [
             "The trainer's next task",
             "Only \"fodder, fodder!\"",
             "Nothing at all",
             "Its freedom"],
         "correct": 1,
         "expl": "The image for a meditator still dependent on "
                 "whatever object currently occupies the mind."},
        {"q": "What does the wild colt stand for in the simile?",
         "opts": [
             "An advanced meditator",
             "A person overcome by the five hindrances, dependent on "
             "sense objects and mental states",
             "A monastic teacher",
             "A layperson with no meditation practice"],
         "correct": 1,
         "expl": "Matched explicitly to someone mired in sensual "
                 "desire, ill will, and the other hindrances."},
        {"q": "How does the thoroughbred regard the trainer's goad?",
         "opts": [
             "As an insult to be resented",
             "As a debt, a bond, a loss, a misfortune — to be avoided "
             "by responding readily",
             "As irrelevant",
             "As a reward"],
         "correct": 1,
         "expl": "The thoroughbred's own attitude, contrasted with "
                 "the wild colt's obliviousness."},
        {"q": "Who pays homage to the thoroughbred meditator, unable "
              "to understand the basis of the absorption?",
         "opts": [
             "Other mendicants",
             "The gods, together with Indra, the Divinity, and the "
             "Progenitor",
             "The horse trainer",
             "King Pasenadi"],
         "correct": 1,
         "expl": "The verse of homage spoken from afar."},
        {"q": "How does the Buddha explain the thoroughbred's "
              "meditation when Sandha asks directly?",
         "opts": [
             "Through years of gradual training alone",
             "The very perception of earth, water, the formless "
             "dimensions, and everything sensed has simply vanished",
             "Through reciting protective verses",
             "He declines to explain further"],
         "correct": 1,
         "expl": "Echoing the same territory explored at AN 11.7 and "
                 "AN 11.8."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Ñātika, in the brick house",
             "Rājagaha, on Vulture's Peak",
             "No setting is stated"],
         "correct": 1,
         "expl": "A specific named location, addressed to Venerable "
                 "Sandha by name."},
    ],
    marginalia=[
        ("Fodder, fodder", [
            "tied to the trough, the",
            "wild colt thinks of nothing",
            "but the feed in front",
        ]),
        ("The thoroughbred's readiness", [
            "the goad, no insult &mdash;",
            "just a debt to answer for,",
            "met without resentment",
        ]),
        ("Homage from afar", [
            "gods bow to a mind",
            "whose basis they cannot",
            "themselves understand",
        ]),
        ("Cross-references", [
            "AN 11.7&ndash;8 &middot; the same beyond-all-perceiving "
            "territory, asked about directly by Ānanda",
            "AN 11.10 &middot; next, the ultimate end and the "
            "aristocrat's own verse",
        ]),
    ],
    further=[
        '<a href="%s/an11.9/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.8.html">AN 11.8</a> &mdash; previous.',
        '<a href="an-11.10.html">AN 11.10 &middot; At the Peacocks&rsquo; Feeding '
        "Ground</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.10 — Moranivāpasutta
# --------------------------------------------------------------------------- #
page(
    10, "Moranivāpa", "At the Peacocks&rsquo; Feeding Ground",
    vagga=VAGGA_1,
    meta_title=("AN 11.10 — At the Peacocks' Feeding Ground | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Moranivāpasutta, closing chapter 1 with four sets of "
        "qualities reaching the ultimate end, and the divinity "
        "Sanaṅkumāra's verse on knowledge and conduct. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_RAJAGAHA),
        ("Speakers", SPEAKER),
        ("Form", "Four descending sets of qualities (three, three, "
                 "three, two) each said to reach the ultimate end, "
                 "closing with a quoted verse"),
        ("Length", "~2 minutes to read"),
        ("Chapter's closer", "This discourse closes Nissayavagga, the "
                             "chapter this project's first ten pages "
                             "of the Elevens have opened with"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "four short lists and a well-known verse"),
    ],
    why=(
        "A mendicant complete in an adept's ethics, immersion, and "
        "wisdom; or complete in the demonstrations of psychic power, "
        "revealing, and instruction; or complete in right view, "
        "right knowledge, and right freedom; or complete simply in "
        "knowledge and conduct &mdash; any of these four reaches the "
        "ultimate end and is best among gods and humans, confirmed by "
        "the divinity Sanaṅkumāra's own verse that one accomplished "
        "in knowledge and conduct is first among gods and humans."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant reaches the ultimate end through any of four "
            "sets of qualities &mdash; an adept's ethics, immersion, "
            "and wisdom; the three demonstrations of psychic power, "
            "revealing, and instruction; right view, right knowledge, "
            "and right freedom; or simply knowledge and conduct "
            "&mdash; closing with the divinity Sanaṅkumāra's own "
            "verse endorsed by the Buddha."]),
        ("Four sets, narrowing from three to two", [
            "The discourse's structure counts down: three sets of "
            "three qualities each, then a final pair, each "
            "independently sufficient to reach &lsquo;the ultimate "
            "end, the ultimate sanctuary from the yoke, the ultimate "
            "spiritual life, the ultimate goal&rsquo; &mdash; the "
            "same superlative formula repeated after each set, "
            "insisting there is more than one complete path to the "
            "same destination."]),
        ("A verse quoted, then requoted", [
            "The discourse's close is unusual in this project: rather "
            "than composing new prose, the Buddha explicitly quotes "
            "a verse already spoken by the divinity Sanaṅkumāra "
            "&mdash; &lsquo;the aristocrat is best among people who "
            "take clan as the standard, but one accomplished in "
            "knowledge and conduct is first among gods and "
            "humans&rsquo; &mdash; endorses it as well spoken and "
            "beneficial, and then repeats it himself in his own "
            "voice."]),
        ("Naming this project's own final chapter opener", [
            "This discourse closes Nissayavagga, the chapter these "
            "first ten pages have covered, with the traditional "
            "double colophon "
            "(&lsquo;Nissayavaggo paṭhamo&rsquo;, chapter one "
            "finished, followed by an uddāna summary verse) left "
            "untranslated in the English source, following this "
            "project's established convention for closing formulas."]),
    ],
    terms=[
        ("accantaniṭṭha accantayogakkhemī accantabrahmacārī "
         "accantapariyosāno",
         "&ldquo;the ultimate end, the ultimate sanctuary from the "
         "yoke, the ultimate spiritual life, the ultimate goal&rdquo; "
         "&mdash; the shared superlative formula closing each of the "
         "four sets."),
        ("asekha sīlakkhandha samādhikkhandha paññākkhandha",
         "&ldquo;the entire spectrum of an adept's ethics, immersion, "
         "and wisdom&rdquo; &mdash; the first and most familiar of the "
         "four sets, the threefold training completed."),
        ("iddhipāṭihāriya ādesanāpāṭihāriya anusāsanīpāṭihāriya",
         "&ldquo;a demonstration of psychic power, of revealing, and "
         "of instruction&rdquo; &mdash; the three miracles, the "
         "Buddha's own well-known threefold classification."),
        ("vijjācaraṇasampanna",
         "&ldquo;accomplished in knowledge and conduct&rdquo; &mdash; "
         "the final, simplest pair, and the phrase at the center of "
         "Sanaṅkumāra's verse."),
        ("khattiyo seṭṭho janetasmiṁ",
         "&ldquo;the aristocrat is best among people&rdquo; &mdash; "
         "the verse's opening line, conceding worldly rank before "
         "subordinating it to spiritual accomplishment."),
    ],
    text_intro=(
        "The discourse in full: four sets of qualities reaching the "
        "ultimate end, and the divinity Sanaṅkumāra's verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three sets of three, and a final pair"),
        ("p", "&sect;1", "an11.10:1.1-5.4"),
        ("h3", "The divinity's verse, quoted and requoted"),
        ("p", "&sect;2", "an11.10:5.5-8.4"),
    ],
    quiz=[
        {"q": "How many independent sets of qualities does this "
              "discourse say reach the ultimate end?",
         "opts": [
             "Only one", "Two", "Three",
             "Four — three sets of three, then a final pair"],
         "correct": 3,
         "expl": "A descending structure, each set independently "
                 "sufficient."},
        {"q": "What is the first of the four sets?",
         "opts": [
             "Right view, right knowledge, right freedom",
             "The entire spectrum of an adept's ethics, immersion, "
             "and wisdom",
             "Knowledge and conduct alone",
             "The three demonstrations"],
         "correct": 1,
         "expl": "The threefold training completed, the most "
                 "familiar of the four sets."},
        {"q": "What does the discourse call the three demonstrations?",
         "opts": [
             "Ethics, immersion, wisdom",
             "Psychic power, revealing, and instruction",
             "Knowledge and conduct",
             "Right view and right freedom"],
         "correct": 1,
         "expl": "The Buddha's own well-known threefold classification "
                 "of miracles."},
        {"q": "Whose verse does the Buddha quote and endorse at the "
              "discourse's close?",
         "opts": [
             "Venerable Sāriputta's",
             "The divinity Sanaṅkumāra's",
             "King Pasenadi's",
             "His own, composed for the occasion"],
         "correct": 1,
         "expl": "An already-existing verse, explicitly quoted rather "
                 "than newly composed."},
        {"q": "What does the quoted verse say is first among gods and "
              "humans?",
         "opts": [
             "The aristocrat by birth alone",
             "One accomplished in knowledge and conduct",
             "The wealthiest person",
             "The eldest person present"],
         "correct": 1,
         "expl": "Subordinating worldly rank to spiritual "
                 "accomplishment."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Ñātika, in the brick house",
             "Rājagaha, at the monastery of the wanderers in the "
             "peacocks' feeding ground",
             "No setting is stated"],
         "correct": 2,
         "expl": "The setting giving this discourse its own title."},
    ],
    marginalia=[
        ("Four paths, one end", [
            "ethics, power, right view,",
            "or knowledge and conduct alone &mdash;",
            "each reaches the goal",
        ]),
        ("A verse, twice spoken", [
            "Sanaṅkumāra's own",
            "words, endorsed, then repeated",
            "in the Buddha's voice",
        ]),
        ("Closing the first chapter", [
            "Nissayavaggo,",
            "the chapter this page ends &mdash;",
            "the Elevens, begun",
        ]),
        ("Cross-references", [
            "AN 11.9 &middot; previous, the thoroughbred and the wild "
            "colt",
            "AN 11.11 &middot; next, opening chapter 2, Anussativagga",
        ]),
    ],
    further=[
        '<a href="%s/an11.10/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.9.html">AN 11.9</a> &mdash; previous.',
        '<a href="an-11.11.html">AN 11.11</a> &mdash; next, opening chapter 2.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.11 — Paṭhamamahānāmasutta
# --------------------------------------------------------------------------- #
page(
    11, "Paṭhamamahānāma", "With Mahānāma (1st)",
    vagga=VAGGA_2,
    meta_title="AN 11.11 — With Mahānāma (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamamahānāmasutta, opening chapter 2 with Mahānāma's "
        "question and the Buddha's answer: five groundings, then six "
        "recollections. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_KAPILAVATTHU),
        ("Speakers", "Mahānāma the Sakyan questioning the Buddha"),
        ("Form", "Five qualities as a base, then six recollections "
                 "given in full, culminating in immersion"),
        ("Length", "~3 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own subject, "
                               "recollection (anussati), to the "
                               "chapter it opens, Anussativagga"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a foundational teaching on the six "
                       "recollections"),
    ],
    why=(
        "Mahānāma asks the Buddha which of the many ways of living he "
        "should practice, and the Buddha answers: grounded on faith, "
        "energy, mindfulness, immersion, and wisdom, a noble disciple "
        "should develop six further things &mdash; recollection of "
        "the Buddha, the teaching, the Saṅgha, one's own ethical "
        "conduct, one's own generosity, and the deities &mdash; each "
        "one calming the mind and, in two of the six, leading all the "
        "way to rapture, tranquility, bliss, and immersion."),
    guide=[
        ("The teaching in one sentence", [
            "Grounded on five qualities &mdash; faith, energy, "
            "mindfulness, immersion, and wisdom &mdash; a noble "
            "disciple develops six recollections: of the Buddha, the "
            "teaching, the Saṅgha, their own ethical conduct, their "
            "own generosity, and the deities, each clearing the mind "
            "of greed, hate, and delusion."]),
        ("A new chapter's own namesake", [
            "As with every chapter before it, this discourse lends its "
            "own subject to the chapter's name: <em>anussati</em>, "
            "recollection, naming Anussativagga. The occasion is "
            "concrete and specific &mdash; mendicants sewing a robe "
            "for the Buddha ahead of his departure prompts Mahānāma "
            "to ask how a busy lay life should be practiced."]),
        ("Two recollections given in full", [
            "Of the six recollections, only the first (the Buddha) and "
            "the last (the deities) are given in full in this "
            "discourse's source text, each culminating in the same "
            "chain already familiar from this project's opening "
            "chapter: an unswerving mind, inspiration, joy, rapture, "
            "tranquility, bliss, and immersion. The middle four "
            "&mdash; teaching, Saṅgha, ethical conduct, generosity "
            "&mdash; are abbreviated with an ellipsis, following the "
            "same underlying pattern."]),
        ("Recollecting the deities, not as worship", [
            "The recollection of deities is not devotional but "
            "diagnostic: a disciple recalls that the deities were "
            "reborn there through faith, ethics, learning, "
            "generosity, and wisdom, then reflects &lsquo;I, too, have "
            "the same kind of faith, ethics, learning, generosity, "
            "and wisdom&rsquo; &mdash; the deities serve as a mirror "
            "confirming one's own qualities, not an external power "
            "appealed to."]),
    ],
    terms=[
        ("anussati",
         "&ldquo;recollection&rdquo; &mdash; this discourse's own "
         "contribution, naming the chapter it opens."),
        ("saddhā viriya sati samādhi paññā",
         "&ldquo;faith, energy, mindfulness, immersion, wisdom&rdquo; "
         "&mdash; the five qualities grounding the six recollections "
         "that follow."),
        ("buddhānussati",
         "&ldquo;recollection of the Buddha&rdquo; &mdash; the first "
         "recollection, given in full, using the standard nine-part "
         "formula of the Buddha's qualities."),
        ("na rāgapariyuṭṭhitena cetasā viharati",
         "&ldquo;their mind is not full of greed, hate, and "
         "delusion&rdquo; &mdash; the shared refrain closing each of "
         "the six recollections."),
        ("devatānussati",
         "&ldquo;recollection of the deities&rdquo; &mdash; the sixth "
         "and final recollection, used diagnostically to confirm "
         "one's own faith, ethics, learning, generosity, and wisdom."),
    ],
    text_intro=(
        "The discourse in full: Mahānāma's question, then five "
        "groundings and six recollections. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Mahānāma's question"),
        ("p", "&sect;1", "an11.11:1.1-2.5"),
        ("h3", "Five groundings, six recollections"),
        ("p", "&sect;2", "an11.11:3.1-8.12"),
    ],
    quiz=[
        {"q": "What prompts Mahānāma to ask his question?",
         "opts": [
             "A dream he had",
             "Hearing that mendicants are sewing a robe for the "
             "Buddha ahead of his departure",
             "A dispute among the Sakyans",
             "An illness in his family"],
         "correct": 1,
         "expl": "A concrete, specific occasion opening the discourse."},
        {"q": "What five qualities ground the six recollections?",
         "opts": [
             "Ethics, immersion, wisdom, generosity, faith",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "The four absorptions and equanimity",
             "The six sense faculties"],
         "correct": 1,
         "expl": "The base on which the six recollections are "
                 "developed."},
        {"q": "Which two recollections are given in full in this "
              "discourse's source text?",
         "opts": [
             "Teaching and Saṅgha",
             "The Buddha (first) and the deities (last)",
             "Ethical conduct and generosity",
             "All six are given in full"],
         "correct": 1,
         "expl": "The middle four are abbreviated with an ellipsis."},
        {"q": "According to the guide, how does recollection of the "
              "deities function?",
         "opts": [
             "As an act of worship toward the deities",
             "Diagnostically, as a mirror confirming one's own faith, "
             "ethics, learning, generosity, and wisdom",
             "As a request for the deities' favor",
             "It plays no role in this discourse"],
         "correct": 1,
         "expl": "Not devotional appeal, but confirmation of qualities "
                 "already present."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular",
             "Its own subject, recollection (anussati), naming "
             "Anussativagga",
             "A place name",
             "A disciple's name"],
         "correct": 1,
         "expl": "As with every chapter's opener in this project."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "The land of the Sakyans, near Kapilavatthu, in the "
             "Banyan Tree Monastery",
             "Rājagaha, on Vulture's Peak",
             "No setting is stated"],
         "correct": 1,
         "expl": "Mahānāma's own home region, where he approaches the "
                 "Buddha directly."},
    ],
    marginalia=[
        ("Five, then six", [
            "faith, energy, mindful,",
            "immersed, wise &mdash; on this base,",
            "six recollections",
        ]),
        ("A mirror in the deities", [
            "they rose by virtue &mdash;",
            "I hold the same virtues too,",
            "not worship, but check",
        ]),
        ("A robe being sewn", [
            "mendicants at work,",
            "the Buddha soon to leave &mdash;",
            "prompting the question",
        ]),
        ("Cross-references", [
            "AN 11.10 &middot; previous, closing chapter 1",
            "AN 11.12 &middot; next, the same teaching for every "
            "posture and occasion",
        ]),
    ],
    further=[
        '<a href="%s/an11.11/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.10.html">AN 11.10</a> &mdash; previous.',
        '<a href="an-11.12.html">AN 11.12 &middot; With Mahānāma (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.12 — Dutiyamahānāmasutta
# --------------------------------------------------------------------------- #
page(
    12, "Dutiyamahānāma", "With Mahānāma (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 11.12 — With Mahānāma (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyamahānāmasutta, restating AN 11.11's teaching with "
        "one addition: the six recollections belong in every posture "
        "and occasion of daily life. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_KAPILAVATTHU),
        ("Speakers", "Mahānāma the Sakyan questioning the Buddha, "
                     "recently recovered from illness"),
        ("Form", "The same five groundings and six recollections as "
                 "AN 11.11, with one closing addition"),
        ("Length", "~2 minutes to read"),
        ("What's added", "Each recollection should be developed "
         "\"while walking, standing, sitting, lying down, while "
         "working, and while at home with your children\""),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the same content as AN 11.11, with a practical "
                       "extension"),
    ],
    why=(
        "Mahānāma, having recently recovered from an illness, asks "
        "the Buddha the same question as before, and receives the "
        "same answer &mdash; five groundings, six recollections "
        "&mdash; with one addition: each recollection should be "
        "developed not only in seated meditation but while walking, "
        "standing, sitting, lying down, working, and at home with "
        "one's children."),
    guide=[
        ("The teaching in one sentence", [
            "The same five groundings and six recollections taught at "
            "AN 11.11, now with an explicit instruction that each "
            "recollection should be developed in every posture and "
            "occasion of daily life, not reserved for formal "
            "meditation alone."]),
        ("A recovering man's question", [
            "The occasion this time is personal: Mahānāma has "
            "recently recovered from an illness when he hears the "
            "same news of the Buddha's coming departure and asks the "
            "same question &mdash; a small but telling detail absent "
            "from AN 11.11, suggesting a mind newly alert to how life "
            "should be practiced after a brush with mortality."]),
        ("Life as the container for recollection", [
            "The discourse's real addition is its closing phrase, "
            "repeated for each of the six recollections: develop this "
            "&lsquo;while walking, standing, sitting, lying down, "
            "while working, and while at home with your "
            "children&rsquo; &mdash; explicitly extending the practice "
            "beyond seated retreat into a layperson's full domestic "
            "and working life."]),
        ("A teaching addressed to a householder", [
            "Unlike many discourses in this project addressed to "
            "mendicants, both Mahānāma discourses speak directly to a "
            "lay follower with a household and children, and this "
            "discourse in particular makes that audience explicit in "
            "its own closing formula, treating recollection as "
            "compatible with, not opposed to, an active family life."]),
    ],
    terms=[
        ("gilānā vuṭṭhito",
         "&ldquo;recently recovered from an illness&rdquo; &mdash; "
         "the detail distinguishing this discourse's occasion from AN "
         "11.11's."),
        ("caraṁ, tiṭṭhaṁ, nisinno, sayāno, kammante payutto, "
         "putthasaṁvāse",
         "&ldquo;walking, standing, sitting, lying down, at work, at "
         "home with your children&rdquo; &mdash; the six occasions "
         "this discourse adds to each recollection's development."),
        ("buddhānussati",
         "&ldquo;recollection of the Buddha&rdquo; &mdash; identical "
         "in content to AN 11.11, but now closing with the six-fold "
         "occasion formula rather than the immersion chain alone."),
        ("devatānussati",
         "&ldquo;recollection of the deities&rdquo; &mdash; the sixth "
         "and final recollection, also closing with the same "
         "occasion formula."),
        ("gahaṭṭha",
         "&ldquo;householder&rdquo; &mdash; the implicit audience "
         "this discourse's closing formula addresses directly, unlike "
         "discourses aimed solely at renunciant mendicants."),
    ],
    text_intro=(
        "The discourse in full: Mahānāma's question, recently "
        "recovered from illness, and the same six recollections for "
        "every posture. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Mahānāma's question, having recovered from illness"),
        ("p", "&sect;1", "an11.12:1.1-2.8"),
        ("h3", "Five groundings, six recollections, for every "
               "occasion"),
        ("p", "&sect;2", "an11.12:3.1-5.16"),
    ],
    quiz=[
        {"q": "What personal detail distinguishes this discourse's "
              "occasion from AN 11.11's?",
         "opts": [
             "Mahānāma has just been ordained",
             "Mahānāma has recently recovered from an illness",
             "Mahānāma is about to travel abroad",
             "Mahānāma has just married"],
         "correct": 1,
         "expl": "A detail absent from AN 11.11's otherwise identical "
                 "occasion."},
        {"q": "What does this discourse add to each of the six "
              "recollections?",
         "opts": [
             "A new seventh recollection",
             "An instruction to develop it while walking, standing, "
             "sitting, lying down, working, and at home with your "
             "children",
             "A prohibition on developing it while working",
             "Nothing; the content is identical to AN 11.11"],
         "correct": 1,
         "expl": "Extending practice beyond seated meditation into "
                 "daily and domestic life."},
        {"q": "According to the guide, what does the closing formula "
              "suggest about the discourse's audience?",
         "opts": [
             "It is addressed only to forest-dwelling mendicants",
             "It explicitly addresses a householder with a family and "
             "work",
             "It excludes laypeople entirely",
             "It has no bearing on the audience"],
         "correct": 1,
         "expl": "Treating recollection as compatible with an active "
                 "family life."},
        {"q": "How many groundings and recollections does this "
              "discourse teach, in total?",
         "opts": [
             "Five groundings and six recollections, eleven in all",
             "Only six recollections, no groundings",
             "Eleven groundings, no recollections",
             "Three groundings and eight recollections"],
         "correct": 0,
         "expl": "Identical structure to AN 11.11."},
        {"q": "What triggers Mahānāma's question in both this "
              "discourse and AN 11.11?",
         "opts": [
             "A famine in the region",
             "Hearing that mendicants are sewing a robe for the "
             "Buddha ahead of his departure",
             "A royal decree",
             "A dispute among the Sakyans"],
         "correct": 1,
         "expl": "The same triggering news in both discourses."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "The land of the Sakyans, near Kapilavatthu, in the "
             "Banyan Tree Monastery",
             "Rājagaha, on Vulture's Peak",
             "No setting is stated"],
         "correct": 1,
         "expl": "The same setting as AN 11.11."},
    ],
    marginalia=[
        ("Recovered, and asking again", [
            "an illness passed, then",
            "the same question returns &mdash;",
            "life freshly noticed",
        ]),
        ("Every posture, every hour", [
            "walking, standing, sat,",
            "lying down, at work, with your",
            "children &mdash; all of it",
        ]),
        ("Recollection for householders", [
            "not for retreat alone &mdash;",
            "the whole busy life becomes",
            "the practice itself",
        ]),
        ("Cross-references", [
            "AN 11.11 &middot; previous, the same teaching's first "
            "telling",
            "AN 11.13 &middot; next, Nandiya's own six groundings and "
            "five inner mindfulnesses",
        ]),
    ],
    further=[
        '<a href="%s/an11.12/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.11.html">AN 11.11</a> &mdash; previous.',
        '<a href="an-11.13.html">AN 11.13 &middot; With Nandiya</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.13 — Nandiyasutta
# --------------------------------------------------------------------------- #
page(
    13, "Nandiya", "With Nandiya",
    vagga=VAGGA_2,
    meta_title="AN 11.13 — With Nandiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Nandiyasutta, in which Nandiya the Sakyan follows the "
        "Buddha to Sāvatthī and receives six groundings and five "
        "inner mindfulnesses. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The land of the Sakyans, then Sāvatthī, where "
                    "both the Buddha and Nandiya spend the rains "
                    "residence"),
        ("Speakers", "Nandiya the Sakyan questioning the Buddha"),
        ("Form", "Six groundings (adding ethics to AN 11.11's five), "
                 "then five inwardly established mindfulnesses"),
        ("Length", "~3 minutes to read"),
        ("A different eleven", "Six plus five here, not five plus "
         "six, with a different recollection list and a closing "
         "simile"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a genuine structural variant worth comparing "
                       "closely with AN 11.11&ndash;12"),
    ],
    why=(
        "Nandiya follows the Buddha to Sāvatthī for the rains "
        "residence so he can see him from time to time while "
        "attending to his own work, and when he hears the Buddha may "
        "soon depart again, he asks the same question Mahānāma asked: "
        "grounded on faith, ethics, energy, mindfulness, immersion, "
        "and wisdom, a noble disciple should establish mindfulness "
        "internally on five further things &mdash; the Buddha, the "
        "teaching, good friends, generosity, and the deities."),
    guide=[
        ("The teaching in one sentence", [
            "Grounded on six qualities &mdash; faith, ethics, energy, "
            "mindfulness, immersion, and wisdom &mdash; a noble "
            "disciple establishes mindfulness internally on five "
            "further things: the Buddha, the teaching, good friends, "
            "generosity, and the deities, giving up unskillful "
            "qualities the way a tipped pot drains and does not refill."]),
        ("Six plus five, not five plus six", [
            "This discourse's eleven items split differently from AN "
            "11.11&ndash;12's five-plus-six: here the base list adds "
            "ethics as a sixth grounding quality, while the five "
            "inner mindfulnesses replace two of the earlier "
            "discourses' six recollections (Saṅgha and one's own "
            "ethical conduct) with a single new item, good friends "
            "&mdash; a genuinely different eleven-item composition, "
            "not simply a renumbering."]),
        ("A follower who chooses to stay close", [
            "Nandiya's own narrative frame is distinctive: rather than "
            "simply hearing news at home, he deliberately follows the "
            "Buddha's own choice of where to spend the rains "
            "residence so that he can attend to his work and still "
            "see the Buddha from time to time &mdash; a portrait of a "
            "lay follower actively arranging his life around access "
            "to the teacher."]),
        ("The tipped pot and the uncontrolled fire", [
            "The discourse closes with a doubled simile absent from "
            "the two Mahānāma discourses: a pot of water once tipped "
            "over drains out and does not flow back in, and an "
            "uncontrolled fire advances through dry woodland without "
            "turning back over what it has burned &mdash; both images "
            "for how, once these eleven qualities are established, "
            "unskillful qualities are given up and not returned to."]),
    ],
    terms=[
        ("saddhā sīla viriya sati samādhi paññā",
         "&ldquo;faith, ethics, energy, mindfulness, immersion, "
         "wisdom&rdquo; &mdash; the six groundings, adding ethics to "
         "AN 11.11's five."),
        ("ajjhattaṁ satiṁ upaṭṭhāpetabbā",
         "&ldquo;you should establish mindfulness internally&rdquo; "
         "&mdash; the refrain introducing each of the five inner "
         "mindfulnesses, distinct from AN 11.11's "
         "&lsquo;recollection&rsquo; refrain."),
        ("kalyāṇamittatā",
         "&ldquo;good friends&rdquo; &mdash; the new item replacing "
         "Saṅgha and ethical conduct among this discourse's five "
         "inner mindfulnesses."),
        ("manomayā kāyā",
         "&ldquo;mind-made deities&rdquo; &mdash; the specific class "
         "of deity recollected here, different from the general "
         "deity list at AN 11.11."),
        ("ambho udakumbho bhinno appaṭisandhiko",
         "&ldquo;a pot full of water tipped over, so the water drains "
         "out and doesn't go back in&rdquo; &mdash; the discourse's "
         "closing simile for irreversibly giving up unskillful "
         "qualities."),
    ],
    text_intro=(
        "The discourse in full: Nandiya's move to Sāvatthī and his "
        "question, then six groundings, five inner mindfulnesses, and "
        "a closing simile. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Nandiya's move to Sāvatthī, and his question"),
        ("p", "&sect;1", "an11.13:1.1-4.8"),
        ("h3", "Six groundings, five inner mindfulnesses"),
        ("p", "&sect;2", "an11.13:5.1-10.5"),
        ("h3", "Giving up unskillful qualities, like water from a "
               "tipped pot"),
        ("p", "&sect;3", "an11.13:11.1-11.4"),
    ],
    quiz=[
        {"q": "Why does Nandiya choose to spend the rains residence at "
              "Sāvatthī?",
         "opts": [
             "He is ordered to by the Buddha",
             "So he can attend to his own work there and still see "
             "the Buddha from time to time",
             "To escape a famine at home",
             "He has no particular reason"],
         "correct": 1,
         "expl": "A lay follower actively arranging his life around "
                 "access to the teacher."},
        {"q": "How does this discourse's six groundings differ from "
              "AN 11.11's five?",
         "opts": [
             "They are identical",
             "This discourse adds ethics as a sixth grounding quality",
             "This discourse removes faith",
             "This discourse has only four groundings"],
         "correct": 1,
         "expl": "A genuinely different eleven-item composition, not "
                 "a renumbering."},
        {"q": "What new item appears among the five inner "
              "mindfulnesses here that AN 11.11 does not include?",
         "opts": [
             "The Saṅgha",
             "Good friends (kalyāṇamittatā)",
             "One's own ethical conduct",
             "The four absorptions"],
         "correct": 1,
         "expl": "Replacing two of AN 11.11's six recollections with "
                 "one new item."},
        {"q": "What does the tipped pot of water illustrate?",
         "opts": [
             "The impermanence of all conditioned things",
             "How, once established, unskillful qualities are given "
             "up irreversibly, like water that drains and does not "
             "return",
             "A monastic almsbowl offering",
             "The four elements"],
         "correct": 1,
         "expl": "Paired with the uncontrolled-fire simile for the "
                 "same point."},
        {"q": "What refrain introduces each of the five inner "
              "mindfulnesses, distinct from AN 11.11's recollection "
              "refrain?",
         "opts": [
             "\"When a noble disciple recollects...\"",
             "\"You should establish mindfulness internally...\"",
             "\"This is peaceful, this is sublime...\"",
             "No refrain is used"],
         "correct": 1,
         "expl": "A distinct refrain marking this discourse's own "
                 "structure."},
        {"q": "Where does this discourse open, before Nandiya moves to "
              "Sāvatthī?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "The land of the Sakyans, near Kapilavatthu",
             "Ñātika, in the brick house",
             "No setting is stated"],
         "correct": 1,
         "expl": "The same opening region as AN 11.11-12, before the "
                 "move to Sāvatthī."},
    ],
    marginalia=[
        ("Six, then five", [
            "faith, ethics, energy,",
            "mindful, immersed, wise &mdash; then",
            "five held within",
        ]),
        ("Following the teacher", [
            "work in one hand, and",
            "the Buddha's presence in",
            "the other &mdash; both kept",
        ]),
        ("A pot once tipped", [
            "water drains and drains,",
            "never flows back in again &mdash;",
            "unskillful, let go",
        ]),
        ("Cross-references", [
            "AN 11.11&ndash;12 &middot; previous, Mahānāma's own "
            "five-plus-six version",
            "AN 11.14 &middot; next, Subhūti tests the evidences of "
            "faith in the mendicant Saddha",
        ]),
    ],
    further=[
        '<a href="%s/an11.13/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.12.html">AN 11.12</a> &mdash; previous.',
        '<a href="an-11.14.html">AN 11.14 &middot; With Subhūti</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.14 — Subhūtisutta
# --------------------------------------------------------------------------- #
page(
    14, "Subhūti", "With Subhūti",
    vagga=VAGGA_2,
    meta_title="AN 11.14 — With Subhūti | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Subhūtisutta, in which the Buddha names eleven evidences "
        "of faith and Subhūti confirms each is found in the "
        "mendicant Saddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha and Venerable Subhūti, examining the "
                     "mendicant Saddha"),
        ("Form", "Eleven evidences of faith named in full, then "
                 "confirmed one by one by Subhūti"),
        ("Length", "~4 minutes to read"),
        ("A named test case", "Unlike this chapter's other "
         "discourses, this one examines a specific individual "
         "mendicant by name"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a clear, examinable list culminating in the "
                       "psychic attainments"),
    ],
    why=(
        "Venerable Subhūti brings the mendicant Saddha to the Buddha, "
        "who names eleven evidences of faith &mdash; from basic "
        "ethical conduct and learning up through the four absorptions, "
        "recollection of past lives, clairvoyance, and the ending of "
        "defilements &mdash; and Subhūti, examining Saddha directly, "
        "confirms that every one of them is genuinely found in him."),
    guide=[
        ("The teaching in one sentence", [
            "Eleven evidences of faith mark a genuinely faithful "
            "mendicant: ethical conduct, learning, good friends, "
            "ease of admonishment, diligence in communal duties, love "
            "of the teachings, energy, the four absorptions, "
            "recollection of past lives, clairvoyance, and the "
            "ending of defilements &mdash; and Subhūti confirms all "
            "eleven are found in the mendicant Saddha."]),
        ("A named test case", [
            "Unlike this chapter's other discourses, which speak in "
            "general terms about &lsquo;a noble disciple&rsquo;, this "
            "discourse examines one specific, named individual: the "
            "mendicant Saddha, son of the layman Sudatta, brought "
            "before the Buddha by Subhūti so that his qualities can "
            "be tested and confirmed directly."]),
        ("From ethics to psychic power, in one list", [
            "The eleven evidences form a clear ascending sequence: "
            "basic ethical conduct and learning, then social qualities "
            "(good friends, admonishability, communal diligence, love "
            "of teachings), then energy, then the four advanced "
            "meditative attainments &mdash; the four absorptions, "
            "recollection of past lives, clairvoyance, and finally the "
            "ending of defilements itself &mdash; treating faith not "
            "as a private feeling but as something that shows up "
            "concretely across an entire spiritual life."]),
        ("Subhūti's own examination and confirmation", [
            "Rather than simply accepting the Buddha's list, Subhūti "
            "explicitly examines Saddha against each of the eleven "
            "items and reports back that every one is found in him, "
            "after which the Buddha instructs Subhūti to live "
            "together with Saddha &mdash; the confirmed evidence of "
            "faith translating directly into a concrete monastic "
            "relationship."]),
    ],
    terms=[
        ("saddhāmatta",
         "&ldquo;evidence of faith&rdquo; &mdash; this discourse's own "
         "title term, the eleven items the Buddha names and Subhūti "
         "confirms."),
        ("sīlavā hoti",
         "&ldquo;is ethical&rdquo; &mdash; the first of the eleven "
         "evidences, restrained in the monastic code."),
        ("cattāro jhāne nikāmalābhī",
         "&ldquo;gets the four absorptions... when they want, without "
         "trouble or difficulty&rdquo; &mdash; the eighth evidence, "
         "opening the sequence's advanced meditative attainments."),
        ("pubbenivāsānussati",
         "&ldquo;recollection of many kinds of past lives&rdquo; "
         "&mdash; the ninth evidence, described here with its full "
         "traditional formula."),
        ("āsavānaṁ khayā",
         "&ldquo;due to the ending of defilements&rdquo; &mdash; the "
         "eleventh and final evidence, the ending of defilements "
         "itself, realized with one's own insight."),
    ],
    text_intro=(
        "The discourse in full: eleven evidences of faith, named by "
        "the Buddha and confirmed one by one by Subhūti. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Introducing the mendicant Saddha"),
        ("p", "&sect;1", "an11.14:1.1-3.3"),
        ("h3", "Eleven evidences of faith"),
        ("p", "&sect;2", "an11.14:4.1-14.2"),
        ("h3", "Subhūti confirms each one"),
        ("p", "&sect;3", "an11.14:15.1-27.3"),
    ],
    quiz=[
        {"q": "Who brings the mendicant Saddha before the Buddha?",
         "opts": [
             "Ānanda", "Venerable Subhūti", "Sāriputta",
             "The layman Sudatta"],
         "correct": 1,
         "expl": "The discourse's namesake, examining Saddha directly."},
        {"q": "How does this discourse differ from the chapter's "
              "other discourses, according to the guide?",
         "opts": [
             "It speaks only in general terms about a noble disciple",
             "It examines one specific, named individual mendicant",
             "It contains no list of qualities",
             "It is spoken entirely in verse"],
         "correct": 1,
         "expl": "A concrete test case rather than general teaching."},
        {"q": "What are the final three of the eleven evidences of "
              "faith?",
         "opts": [
             "Ethics, learning, good friends",
             "The four absorptions, recollection of past lives, "
             "clairvoyance, and the ending of defilements",
             "Generosity, wisdom, immersion",
             "Faith, energy, mindfulness"],
         "correct": 1,
         "expl": "The sequence's advanced meditative and liberating "
                 "attainments."},
        {"q": "What does Subhūti do after the Buddha names the eleven "
              "evidences?",
         "opts": [
             "Nothing further",
             "He examines Saddha against each item and confirms all "
             "eleven are found in him",
             "He disputes the list",
             "He asks for a twelfth evidence"],
         "correct": 1,
         "expl": "Direct examination and confirmation, not mere "
                 "acceptance."},
        {"q": "What does the Buddha instruct Subhūti to do at the "
              "discourse's close?",
         "opts": [
             "Ordain Saddha immediately",
             "Live together with Saddha",
             "Send Saddha to another monastery",
             "Nothing further is instructed"],
         "correct": 1,
         "expl": "The confirmed evidence of faith translates into a "
                 "concrete monastic relationship."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, in the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "No scene is set beyond Subhūti and Saddha "
                 "approaching the Buddha."},
    ],
    marginalia=[
        ("Eleven marks of faith", [
            "from ethics and learning",
            "up through the four jhānas",
            "to defilements' end",
        ]),
        ("A named test case", [
            "not \"a disciple\" but",
            "Saddha, son of Sudatta &mdash;",
            "examined by name",
        ]),
        ("Confirmed, and welcomed", [
            "every mark is found,",
            "Subhūti reports &mdash; then live",
            "together, the Buddha says",
        ]),
        ("Cross-references", [
            "AN 11.13 &middot; previous, Nandiya's six groundings and "
            "five inner mindfulnesses",
            "AN 11.15 &middot; next, The Benefits of Love, a page "
            "from this project's earlier eighteen-page selection",
        ]),
    ],
    further=[
        '<a href="%s/an11.14/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.13.html">AN 11.13</a> &mdash; previous.',
        '<a href="an-11.15.html">AN 11.15 &middot; The Benefits of Love</a> &mdash; next.',
    ],
    next=("an-11.15.html", "AN 11.15 &middot; The Benefits of Love"),
)


# --------------------------------------------------------------------------- #
# AN 11.16 — Aṭṭhakanāgarasutta
# --------------------------------------------------------------------------- #
page(
    16, "Aṭṭhakanāgara", "The Wealthy Citizen",
    vagga=VAGGA_2,
    meta_title="AN 11.16 — The Wealthy Citizen | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aṭṭhakanāgarasutta, in which Venerable Ānanda gives the "
        "householder Dasama eleven doors to the deathless, likened to "
        "a treasure trove with eleven entrances. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_BELUVA),
        ("Speakers", "The householder Dasama questioning Venerable "
                     "Ānanda"),
        ("Form", "Eleven doors to the deathless — four absorptions, "
                 "four divine abodes, three formless attainments — "
                 "each paired with insight into impermanence"),
        ("Length", "~4 minutes to read"),
        ("A recurring fixed list", "The same eleven-item list of "
         "meditative attainments this project will meet again at the "
         "close of this nipāta's own Rāgapeyyāla"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "eleven distinct attainments, each requiring "
                       "care to distinguish"),
    ],
    why=(
        "The wealthy citizen Dasama, traveling on business, seeks out "
        "Venerable Ānanda and asks for one thing taught by the Buddha "
        "that frees the mind and ends the defilements; Ānanda answers "
        "with eleven doors &mdash; the four absorptions, the four "
        "divine abodes of love, compassion, rejoicing, and equanimity, "
        "and the three lower formless attainments &mdash; each "
        "practiced, then seen through as impermanent and liable to "
        "cessation, ending the defilements or leading to rebirth "
        "beyond return."),
    guide=[
        ("The teaching in one sentence", [
            "Eleven meditative attainments &mdash; the four "
            "absorptions, the four divine abodes, and the three lower "
            "formless dimensions &mdash; each become doors to the "
            "deathless when a mendicant, having attained one, reflects "
            "that it too is produced by choices and intentions and "
            "therefore impermanent, ending the defilements or being "
            "reborn beyond return."]),
        ("Asked of Ānanda, not the Buddha", [
            "This discourse's occasion is distinctive: Dasama, a "
            "wealthy citizen from Pāṭaliputta, deliberately seeks out "
            "Ānanda rather than the Buddha directly, and Ānanda "
            "answers under his own authority, echoing this project's "
            "earlier pattern of senior disciples teaching in the "
            "Buddha's own voice."]),
        ("The same structure, eleven times over", [
            "Each of the eleven attainments follows an identical "
            "shape: enter the attainment, reflect that it is "
            "&lsquo;produced by choices and intentions&rsquo; and "
            "therefore impermanent, and from that insight either end "
            "the defilements outright or, failing that, be reborn "
            "spontaneously in a pure abode from which there is no "
            "return &mdash; a repeated formula this discourse applies "
            "systematically across every one of the eleven doors."]),
        ("A fixed list this project will meet again", [
            "The eleven items themselves &mdash; four absorptions, "
            "four divine abodes, three formless attainments (stopping "
            "short of the fourth, neither-perception-nor-"
            "non-perception) &mdash; form a fixed list that recurs "
            "later in this very nipāta, at the close of its own "
            "Rāgapeyyāla, where the same eleven things are said to be "
            "developed for insight into greed and each defilement "
            "after it."]),
    ],
    terms=[
        ("amatadvāra",
         "&ldquo;door to the deathless&rdquo; &mdash; Dasama's own "
         "closing image, and the discourse's central metaphor for "
         "each of the eleven attainments."),
        ("saṅkhatam abhisaṅkhataṁ",
         "&ldquo;produced by choices and intentions&rdquo; &mdash; "
         "the reflection applied to each attainment in turn, the "
         "pivot from meditative accomplishment to liberating insight."),
        ("brahmavihāra",
         "not named directly but present throughout &mdash; the four "
         "divine abodes of love, compassion, rejoicing, and "
         "equanimity, four of this discourse's eleven doors."),
        ("anāgāmī",
         "&ldquo;non-returner&rdquo; &mdash; the implicit attainment "
         "described when the defilements are not fully ended but "
         "rebirth beyond return still follows."),
        ("nidhikumbhīnaṁ mukhāni",
         "&ldquo;entrances to a treasure trove&rdquo; &mdash; "
         "Dasama's own simile for the eleven doors, paired with a "
         "house with eleven doors offering escape from fire."),
    ],
    text_intro=(
        "The discourse in full: Dasama's question to Ānanda, the "
        "eleven doors to the deathless, and Dasama's own gratitude. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Dasama seeks out Ānanda"),
        ("p", "&sect;1", "an11.16:1.1-3.2"),
        ("h3", "Eleven doors to the deathless"),
        ("p", "&sect;2", "an11.16:4.1-9.8"),
        ("h3", "Eleven doors, elevenfold gratitude"),
        ("p", "&sect;3", "an11.16:10.1-11.3"),
    ],
    quiz=[
        {"q": "Who does Dasama seek out with his question?",
         "opts": [
             "The Buddha directly",
             "Venerable Ānanda",
             "Venerable Sāriputta",
             "Venerable Subhūti"],
         "correct": 1,
         "expl": "A disciple answering under his own authority."},
        {"q": "What are the eleven doors to the deathless?",
         "opts": [
             "Eleven ethical precepts",
             "The four absorptions, the four divine abodes, and the "
             "three lower formless attainments",
             "Eleven historical Buddhas",
             "The noble eightfold path repeated"],
         "correct": 1,
         "expl": "Stopping short of the fourth formless attainment, "
                 "neither-perception-nor-non-perception."},
        {"q": "What reflection turns each attainment into a door to "
              "the deathless?",
         "opts": [
             "That the attainment is permanent and reliable",
             "That the attainment is produced by choices and "
             "intentions, and therefore impermanent",
             "That the attainment should be repeated forever",
             "No reflection is needed"],
         "correct": 1,
         "expl": "The pivot from meditative accomplishment to "
                 "liberating insight."},
        {"q": "What does Dasama compare the eleven doors to?",
         "opts": [
             "A single locked door",
             "Entrances to a treasure trove, and a house with eleven "
             "doors offering escape from fire",
             "A ladder with eleven rungs",
             "A river with eleven crossings"],
         "correct": 1,
         "expl": "Dasama's own closing simile, marking his gratitude."},
        {"q": "According to the guide, where does this project meet "
              "the same eleven-item list again?",
         "opts": [
             "Nowhere else in this project",
             "At the close of this nipāta's own Rāgapeyyāla, "
             "developed for insight into greed and each defilement",
             "In chapter 1 of the Elevens",
             "In the Book of the Tens"],
         "correct": 1,
         "expl": "A fixed list recurring later in this very nipāta."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Vesālī, in the little village of Beluva",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, in the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "Ānanda's own location, sought out by Dasama."},
    ],
    marginalia=[
        ("Eleven doors, one house", [
            "however it burns,",
            "any door lets you escape &mdash;",
            "any one will do",
        ]),
        ("Attained, then seen through", [
            "each state entered, then",
            "known as made, impermanent &mdash;",
            "that seeing frees the mind",
        ]),
        ("A grateful offering", [
            "no fee for the door,",
            "yet Dasama gives freely &mdash;",
            "robes, food, a dwelling",
        ]),
        ("Cross-references", [
            "AN 11.14 &middot; the last built page before this "
            "chapter's splice at AN 11.15",
            "AN 11.15 &middot; The Benefits of Love, previous, from "
            "this project's earlier eighteen-page selection",
            "the Rāgapeyyāla, closing this nipāta &middot; the same "
            "eleven-item list, developed there for insight into greed",
        ]),
    ],
    further=[
        '<a href="%s/an11.16/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.15.html">AN 11.15</a> &mdash; previous.',
        '<a href="an-11.17.html">AN 11.17 &middot; The Cowherd</a> &mdash; next.',
    ],
    prev=("an-11.15.html", "AN 11.15 &middot; The Benefits of Love"),
)


# --------------------------------------------------------------------------- #
# AN 11.17 — Gopālasutta
# --------------------------------------------------------------------------- #
page(
    17, "Gopāla", "The Cowherd",
    vagga=VAGGA_2,
    meta_title="AN 11.17 — The Cowherd | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Gopālasutta, applying the eleven-factor cowherd simile "
        "to a mendicant's own growth in the training — the same "
        "simile this nipāta will use again at far greater scale. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eleven factors preventing growth, each explained in "
                 "turn, then the same eleven reversed and explained "
                 "again as enabling growth"),
        ("Length", "~4 minutes to read"),
        ("A simile this nipāta will reuse", "The identical cowherd "
         "simile opens the massive peyyāla later in this nipāta's own "
         "chapter 3"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "eleven distinct factors, each explained with "
                       "its own definition"),
    ],
    why=(
        "A cowherd lacking eleven skills &mdash; knowing form, "
        "reading characteristics, removing flies' eggs, dressing "
        "wounds, spreading smoke, knowing the ford, knowing "
        "satisfaction, knowing the trail, skill in pastures, not "
        "milking dry, and respecting the herd's senior bulls &mdash; "
        "cannot maintain a herd; in the same way, a mendicant lacking "
        "the same eleven qualities, reinterpreted for the training, "
        "cannot grow, improve, or mature in the teaching, while a "
        "mendicant who has them can."),
    guide=[
        ("The teaching in one sentence", [
            "Just as a cowherd needs eleven practical skills to "
            "maintain a herd, a mendicant needs eleven reinterpreted "
            "qualities &mdash; from understanding form correctly to "
            "restraining the senses to respecting senior mendicants "
            "&mdash; to grow, improve, and mature in the teaching and "
            "training."]),
        ("A vivid simile, mapped point by point", [
            "Unlike this project's simpler similes, this discourse "
            "maps all eleven items of its herding vocabulary onto a "
            "specific spiritual meaning, then explains each mapped "
            "meaning again in its own right: not knowing form becomes "
            "not understanding the four elements and derived matter; "
            "not dressing wounds becomes leaving the six sense "
            "faculties unrestrained; not knowing the ford becomes "
            "never questioning learned elders to resolve doubts."]),
        ("The full inventory of eleven", [
            "The eleven qualities run: understanding form, skill in "
            "characterizing people by their deeds, removing arisen "
            "unskillful thoughts, sense restraint, teaching others "
            "what one has learned, questioning learned elders, "
            "finding inspiration in the teaching, understanding the "
            "noble eightfold path, understanding the four "
            "establishments of mindfulness, moderation in accepting "
            "requisites, and respecting senior mendicants &mdash; a "
            "genuinely comprehensive checklist spanning doctrine, "
            "practice, and community conduct."]),
        ("A simile this nipāta will meet again, at far greater "
         "scale", [
            "This same cowherd simile, down to its eleven items in "
            "the same order, opens the massive peyyāla that will fill "
            "most of this nipāta's chapter 3 &mdash; there stripped of "
            "its detailed explanations and used instead as a repeated "
            "refrain across hundreds of compressed discourses, making "
            "this discourse worth remembering as the simile's first "
            "and most fully explained appearance."]),
    ],
    terms=[
        ("gopālaka",
         "&ldquo;cowherd&rdquo; &mdash; the discourse's own title "
         "figure, mapped point by point onto a mendicant's own "
         "practice."),
        ("makkhikāhārako",
         "&ldquo;picks out flies' eggs&rdquo; &mdash; one of the "
         "cowherd's eleven skills, mapped to giving up arisen "
         "sensual, malicious, or cruel thoughts before they take "
         "hold."),
        ("vaṇaṁ paṭicchādetā",
         "&ldquo;dresses wounds&rdquo; &mdash; mapped to restraining "
         "the six sense faculties so that covetousness and "
         "displeasure do not become overwhelming."),
        ("titthaṁ jānāti",
         "&ldquo;knows the ford&rdquo; &mdash; mapped to regularly "
         "questioning learned elders to resolve doubtful points in "
         "the teaching."),
        ("theresu therataresu",
         "&ldquo;senior mendicants of long standing... fathers and "
         "leaders of the Saṅgha&rdquo; &mdash; the object of the "
         "eleventh quality, respect shown consistently in body, "
         "speech, and mind."),
    ],
    text_intro=(
        "The discourse in full: eleven factors preventing growth, "
        "then the same eleven reversed as enabling it. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eleven qualities that prevent growth"),
        ("p", "&sect;1", "an11.17:1.1-14.1"),
        ("h3", "Eleven qualities that bring growth"),
        ("p", "&sect;2", "an11.17:15.1-28.1"),
    ],
    quiz=[
        {"q": "What does a cowherd lacking eleven skills fail to do?",
         "opts": [
             "Sell milk profitably",
             "Maintain and expand a herd of cattle",
             "Find good pastureland",
             "Train new cowherds"],
         "correct": 1,
         "expl": "The simile's literal opening claim, mapped onto a "
                 "mendicant's training."},
        {"q": "What does \"dressing wounds\" map to in the mendicant's "
              "eleven qualities?",
         "opts": [
             "Literal first aid for injured mendicants",
             "Restraining the six sense faculties so covetousness and "
             "displeasure don't overwhelm the mind",
             "Repairing damaged robes",
             "Caring for the sick in the community"],
         "correct": 1,
         "expl": "One of the discourse's point-by-point mappings from "
                 "herding skill to spiritual practice."},
        {"q": "What does \"knowing the ford\" map to?",
         "opts": [
             "Finding the right meditation posture",
             "Regularly questioning learned elders to resolve doubts "
             "in the teaching",
             "Crossing a literal river",
             "Knowing when to eat"],
         "correct": 1,
         "expl": "Another of the eleven point-by-point mappings."},
        {"q": "According to the guide, where does this project meet "
              "the same cowherd simile again?",
         "opts": [
             "Nowhere else in this project",
             "Opening the massive peyyāla that fills most of this "
             "nipāta's chapter 3, at far greater scale",
             "Only in the Book of the Tens",
             "In the chapter's very next discourse"],
         "correct": 1,
         "expl": "The same eleven items in the same order, reused as "
                 "a repeated refrain."},
        {"q": "What is the eleventh quality in the mendicant's own "
              "list?",
         "opts": [
             "Moderation in accepting requisites",
             "Respecting senior mendicants of long standing, fathers "
             "and leaders of the Saṅgha",
             "Understanding the four elements",
             "Skill in characterizing people"],
         "correct": 1,
         "expl": "The list's closing item, mirroring the cowherd's own "
                 "respect for the herd's senior bulls."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No scene is set; the Buddha addresses the mendicants "
                 "directly."},
    ],
    marginalia=[
        ("A cowherd's eleven skills", [
            "know form, read the signs,",
            "clear the wounds, spread smoke, know",
            "the ford and the trail",
        ]),
        ("Mapped onto practice", [
            "each herding skill turned",
            "to sense restraint, questioning,",
            "respect for elders",
        ]),
        ("A simile that returns", [
            "the same eleven,",
            "met once explained in full &mdash;",
            "soon a bare refrain",
        ]),
        ("Cross-references", [
            "AN 11.16 &middot; previous, eleven doors to the deathless",
            "AN 11.18 &middot; next, an immersion beyond all "
            "perception, asked by several mendicants",
            "the Sāmaññavagga, chapter 3 &middot; this same cowherd "
            "simile, reused as a peyyāla refrain at far greater scale",
        ]),
    ],
    further=[
        '<a href="%s/an11.17/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.16.html">AN 11.16</a> &mdash; previous.',
        '<a href="an-11.18.html">AN 11.18 &middot; Immersion (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.18 — Paṭhamasamādhisutta
# --------------------------------------------------------------------------- #
page(
    18, "Paṭhamasamādhi", "Immersion (1st)",
    vagga=VAGGA_2,
    meta_title="AN 11.18 — Immersion (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamasamādhisutta, in which several mendicants ask the "
        "Buddha about the same immersion beyond all perception first "
        "met at AN 11.7-8. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Several mendicants questioning the Buddha"),
        ("Form", "The same question and answer as AN 11.7-8, now "
                 "asked by an unnamed group rather than Ānanda alone"),
        ("Length", "~2 minutes to read"),
        ("First of four variations", "This chapter closes with four "
         "discourses on the identical immersion, varying only who "
         "asks and who answers"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the same demanding immersion met earlier in "
                       "this nipāta"),
    ],
    why=(
        "Several mendicants ask the Buddha whether a mendicant might "
        "gain a state of immersion where nothing at all is perceived "
        "in its usual way &mdash; not the elements, the formless "
        "dimensions, this world or another, or anything seen, heard, "
        "thought, or known &mdash; and yet still perceive; the Buddha "
        "confirms it, through perceiving only that &lsquo;this is "
        "peaceful, this is sublime&rsquo;, the stilling of all "
        "activities and the ending of craving."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant can gain a state of immersion beyond every "
            "ordinary object of perception &mdash; the elements, the "
            "formless dimensions, either world, anything sensed "
            "&mdash; and yet still perceive, by perceiving only the "
            "peace of nibbāna: the stilling of all activities and the "
            "ending of craving."]),
        ("The same question, a different questioner", [
            "This is the identical question and answer already met at "
            "AN 11.7, but with the asker changed from Ānanda alone to "
            "&lsquo;several mendicants&rsquo; unnamed, and the "
            "follow-up dialogue with Sāriputta from AN 11.7 dropped "
            "entirely &mdash; the shortest and plainest of this "
            "chapter's four variations on the theme."]),
        ("A four-part set closing this chapter", [
            "This discourse opens a set of four that will close "
            "chapter 2: mendicants ask the Buddha (this discourse), "
            "the Buddha volunteers the same teaching to the "
            "mendicants unprompted (AN 11.19), mendicants ask "
            "Sāriputta (AN 11.20), and Sāriputta volunteers it to the "
            "mendicants unprompted (AN 11.21) &mdash; a structural "
            "chiasm testing the same content across every combination "
            "of asker and teacher."]),
        ("Why the repetition matters", [
            "Read as a set, these four short discourses make the same "
            "point AN 11.7 made through two direct witnesses "
            "(Buddha and Sāriputta): whether prompted or volunteered, "
            "asked of the Buddha or of a senior disciple, this "
            "teaching about immersion beyond perception is delivered "
            "identically every time, underscoring that it describes a "
            "fixed reality rather than a personal formulation."]),
    ],
    terms=[
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; the "
         "sole remaining perception in this immersion, identical "
         "across all four discourses in this closing set."),
        ("sabbasaṅkhārasamatho sabbūpadhipaṭinissaggo taṇhākkhayo "
         "virāgo nirodho nibbānaṁ",
         "&ldquo;the stilling of all activities... extinguishment&rdquo; "
         "&mdash; the same full closing formula shared with AN "
         "11.7&ndash;8."),
        ("sambahulā bhikkhū",
         "&ldquo;several mendicants&rdquo; &mdash; the unnamed group "
         "asking here, replacing AN 11.7's named questioner, Ānanda."),
        ("siyā nu kho",
         "&ldquo;could it be...?&rdquo; &mdash; the shared opening "
         "formula of the question in all four discourses of this set."),
        ("yathā kathaṁ panidaṁ",
         "&ldquo;but how could this be?&rdquo; &mdash; the shared "
         "follow-up question in all four, prompting the Buddha's or "
         "Sāriputta's explanation."),
    ],
    text_intro=(
        "The discourse in full: several mendicants ask about an "
        "immersion beyond all perception, and the Buddha answers. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Several mendicants ask, and the Buddha answers"),
        ("p", "&sect;1", "an11.18:1.1-5.3"),
    ],
    quiz=[
        {"q": "Who asks the question in this discourse?",
         "opts": [
             "Venerable Ānanda alone",
             "Several unnamed mendicants",
             "Venerable Sāriputta",
             "The householder Dasama"],
         "correct": 1,
         "expl": "Distinct from AN 11.7's named questioner, Ānanda."},
        {"q": "How does this discourse's content compare to AN "
              "11.7-8's?",
         "opts": [
             "Entirely different teaching",
             "The identical question and answer, with the "
             "Sāriputta follow-up dropped entirely",
             "A much longer expanded version",
             "A contradiction of the earlier teaching"],
         "correct": 1,
         "expl": "The shortest and plainest of this theme's four "
                 "variations."},
        {"q": "According to the guide, what four-part set does this "
              "discourse open?",
         "opts": [
             "Four discourses on an unrelated topic",
             "Four variations testing every combination of asker and "
             "teacher for the same immersion teaching",
             "A set of four unrelated similes",
             "Four discourses spoken only by the Buddha"],
         "correct": 1,
         "expl": "Mendicants-to-Buddha, Buddha-to-mendicants, "
                 "mendicants-to-Sāriputta, Sāriputta-to-mendicants."},
        {"q": "What is perceived in this state of immersion?",
         "opts": [
             "Every sense object heightened",
             "Only that \"this is peaceful, this is sublime\"",
             "Nothing whatsoever, even in principle",
             "A vision of past lives"],
         "correct": 1,
         "expl": "Identical across all four discourses in this "
                 "closing set."},
        {"q": "According to the guide, what does the fourfold "
              "repetition underscore?",
         "opts": [
             "That the teaching changes depending on who explains it",
             "That the teaching is delivered identically regardless "
             "of who asks or answers, describing a fixed reality",
             "That only the Buddha's version is authoritative",
             "Nothing beyond simple repetition"],
         "correct": 1,
         "expl": "A fixed reality, not a personal formulation."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No scene is set beyond the mendicants approaching "
                 "the Buddha."},
    ],
    marginalia=[
        ("The same immersion again", [
            "beyond earth and world,",
            "beyond all that's seen and heard &mdash;",
            "yet still, perceiving",
        ]),
        ("A group, not one voice", [
            "no longer Ānanda",
            "alone &mdash; several mendicants",
            "ask the question now",
        ]),
        ("Four askers, one answer", [
            "to Buddha, from Buddha,",
            "to Sāriputta, from him &mdash;",
            "the teaching, unchanged",
        ]),
        ("Cross-references", [
            "AN 11.7&ndash;8 &middot; the fuller telling of this same "
            "immersion, with the Sāriputta confirmation",
            "AN 11.19 &middot; next, the Buddha volunteers this same "
            "teaching unprompted",
        ]),
    ],
    further=[
        '<a href="%s/an11.18/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.17.html">AN 11.17</a> &mdash; previous.',
        '<a href="an-11.19.html">AN 11.19 &middot; Immersion (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.19 — Dutiyasamādhisutta
# --------------------------------------------------------------------------- #
page(
    19, "Dutiyasamādhi", "Immersion (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 11.19 — Immersion (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasamādhisutta, in which the Buddha himself raises "
        "the immersion-beyond-perception question, and the mendicants "
        "ask him to explain it in full. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha addressing the mendicants, then "
                     "responding to their request for explanation"),
        ("Form", "The same immersion as AN 11.18, this time raised by "
                 "the Buddha himself rather than asked of him"),
        ("Length", "~2 minutes to read"),
        ("Second of four variations", "The Buddha volunteers the "
         "teaching unprompted, reversing AN 11.18's direction"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the same demanding immersion, now offered "
                       "rather than requested"),
    ],
    why=(
        "The Buddha himself asks the mendicants whether a mendicant "
        "might gain a state of immersion beyond all ordinary "
        "perception, and when they ask him to clarify its meaning "
        "himself, he explains: it is when a mendicant perceives only "
        "that &lsquo;this is peaceful, this is sublime&rsquo;, the "
        "stilling of all activities and the ending of craving."),
    guide=[
        ("The teaching in one sentence", [
            "The same immersion beyond all ordinary perception "
            "already met at AN 11.7-8 and AN 11.18, now raised by "
            "the Buddha himself, who explains it as perceiving only "
            "the peace of nibbāna: the stilling of all activities and "
            "the ending of craving."]),
        ("The direction reversed", [
            "Where AN 11.18 had mendicants ask the Buddha, this "
            "discourse reverses the direction entirely: the Buddha "
            "addresses the mendicants first with the same question, "
            "and they respond not by answering but by formally "
            "requesting that he himself clarify its meaning &mdash; "
            "&lsquo;our teachings are rooted in the Buddha... may the "
            "Buddha himself please clarify the meaning of this&rsquo;."]),
        ("A formal request for explanation", [
            "The mendicants' request follows a set formula this "
            "project has met at moments of significant teaching "
            "elsewhere: acknowledging the Buddha as root, guide, and "
            "refuge, and asking him to speak so they may listen and "
            "remember &mdash; treating this repeated immersion "
            "teaching as significant enough to warrant the same "
            "formal deference given to major doctrinal statements."]),
        ("Two directions, the same content", [
            "Whether the Buddha is asked (AN 11.18) or volunteers the "
            "teaching himself and is then formally invited to explain "
            "it (this discourse), the substance delivered is "
            "identical &mdash; reinforcing this closing set's larger "
            "point that the teaching does not depend on the "
            "circumstances of its delivery."]),
    ],
    terms=[
        ("bhagavammūlakā no dhammā",
         "&ldquo;our teachings are rooted in the Buddha&rdquo; "
         "&mdash; the mendicants' own formal opening, acknowledging "
         "him as source before requesting explanation."),
        ("bhagavaṁ nissitā",
         "&ldquo;he is our refuge&rdquo; &mdash; continuing the same "
         "formal request, naming the Buddha as guide and refuge."),
        ("paṭibhātu bhagavantaññeva",
         "&ldquo;may the Buddha himself please clarify the "
         "meaning&rdquo; &mdash; the mendicants' explicit request that "
         "the Buddha, not another, provide the explanation."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; the "
         "same closing perception shared with every discourse in this "
         "set."),
        ("siyā nu kho bhikkhave",
         "&ldquo;could it be, mendicants...?&rdquo; &mdash; the "
         "Buddha's own opening here, addressed to the mendicants "
         "rather than posed to him."),
    ],
    text_intro=(
        "The discourse in full: the Buddha raises the question "
        "himself, and explains it at the mendicants' formal request. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha raises the question himself"),
        ("p", "&sect;1", "an11.19:1.1-6.3"),
    ],
    quiz=[
        {"q": "Who raises the question in this discourse?",
         "opts": [
             "Several unnamed mendicants",
             "The Buddha himself, addressing the mendicants",
             "Venerable Sāriputta",
             "Venerable Ānanda"],
         "correct": 1,
         "expl": "Reversing AN 11.18's direction, where mendicants "
                 "asked the Buddha."},
        {"q": "How do the mendicants respond to the Buddha's own "
              "question?",
         "opts": [
             "They answer it themselves immediately",
             "They formally request that the Buddha himself clarify "
             "its meaning",
             "They remain silent",
             "They ask Sāriputta to answer instead"],
         "correct": 1,
         "expl": "\"Our teachings are rooted in the Buddha... may the "
                 "Buddha himself please clarify.\""},
        {"q": "What formula does the mendicants' request follow, "
              "according to the guide?",
         "opts": [
             "A casual, informal question",
             "A set formula acknowledging the Buddha as root, guide, "
             "and refuge, used at moments of significant teaching",
             "A challenge to the Buddha's authority",
             "No particular formula"],
         "correct": 1,
         "expl": "Treating this teaching with the same formal "
                 "deference given major doctrinal statements."},
        {"q": "What is the content of the Buddha's explanation?",
         "opts": [
             "Entirely new content not met before",
             "The same immersion as AN 11.7-8 and AN 11.18: "
             "perceiving only that this is peaceful, this is sublime",
             "A description of a different meditative state",
             "He declines to explain"],
         "correct": 1,
         "expl": "Identical substance regardless of who asks or "
                 "answers."},
        {"q": "According to the guide, what does this discourse "
              "reinforce about the closing set as a whole?",
         "opts": [
             "That different circumstances produce different "
             "teachings",
             "That the teaching does not depend on the circumstances "
             "of its delivery",
             "That only volunteered teachings are reliable",
             "Nothing in particular"],
         "correct": 1,
         "expl": "The substance is identical whether asked or "
                 "volunteered."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No scene is set beyond the Buddha addressing the "
                 "mendicants."},
    ],
    marginalia=[
        ("Offered, not asked", [
            "this time the Buddha",
            "raises it himself &mdash; the same",
            "question, reversed",
        ]),
        ("A formal request", [
            "rooted in the Buddha,",
            "our guide and refuge &mdash; please,",
            "clarify it yourself",
        ]),
        ("The same peace, again", [
            "this is peaceful, this",
            "is sublime &mdash; the one thing left",
            "when all else falls still",
        ]),
        ("Cross-references", [
            "AN 11.18 &middot; previous, mendicants ask the Buddha",
            "AN 11.20 &middot; next, mendicants ask Sāriputta the "
            "same question",
        ]),
    ],
    further=[
        '<a href="%s/an11.19/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.18.html">AN 11.18</a> &mdash; previous.',
        '<a href="an-11.20.html">AN 11.20 &middot; Immersion (3rd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.20 — Tatiyasamādhisutta
# --------------------------------------------------------------------------- #
page(
    20, "Tatiyasamādhi", "Immersion (3rd)",
    vagga=VAGGA_2,
    meta_title="AN 11.20 — Immersion (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Tatiyasamādhisutta, in which several mendicants put the "
        "same immersion-beyond-perception question to Venerable "
        "Sāriputta. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Several mendicants questioning Venerable "
                     "Sāriputta"),
        ("Form", "The same question and answer as AN 11.18, now "
                 "addressed to Sāriputta rather than the Buddha"),
        ("Length", "~2 minutes to read"),
        ("Third of four variations", "The same content, this time "
         "answered by a senior disciple rather than the Buddha"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the same demanding immersion, answered by a "
                       "different teacher"),
    ],
    why=(
        "Several mendicants approach Venerable Sāriputta and ask him "
        "the same question already put to the Buddha: whether a "
        "mendicant might gain a state of immersion beyond all "
        "ordinary perception, and yet still perceive; Sāriputta "
        "confirms it, giving the identical explanation already heard "
        "from the Buddha in this chapter's earlier discourses."),
    guide=[
        ("The teaching in one sentence", [
            "The identical immersion beyond all ordinary perception "
            "met throughout this chapter, here answered by Sāriputta "
            "rather than the Buddha, in exactly the same words: "
            "perceiving only that this is peaceful, this is sublime, "
            "the stilling of all activities and the ending of craving."]),
        ("Mendicants choose a disciple this time", [
            "Where AN 11.18 had mendicants approach the Buddha "
            "directly, this discourse has them approach Sāriputta "
            "instead, exchanging the customary greetings before "
            "posing the identical question &mdash; testing whether "
            "the same teaching holds when sought from a senior "
            "disciple rather than the source."]),
        ("A brief, confident answer", [
            "Sāriputta's reply is immediate and unqualified: "
            "&lsquo;it could be, reverends&rsquo; &mdash; he does not "
            "hedge or defer to the Buddha before answering, but "
            "speaks with the same direct authority already "
            "demonstrated when Ānanda tested him independently at AN "
            "11.7."]),
        ("Completing the chiasm", [
            "With this discourse, three of this closing set's four "
            "combinations are now complete: mendicants asking the "
            "Buddha (AN 11.18), the Buddha volunteering to the "
            "mendicants (AN 11.19), and mendicants asking Sāriputta "
            "(this discourse) &mdash; leaving only Sāriputta "
            "volunteering the teaching himself, which the chapter's "
            "final discourse supplies."]),
    ],
    terms=[
        ("āyasmantaṁ sāriputtaṁ upasaṅkamiṁsu",
         "&ldquo;went up to Venerable Sāriputta&rdquo; &mdash; this "
         "discourse's own opening move, choosing a disciple over the "
         "Buddha as questioned teacher."),
        ("siyā āvuso",
         "&ldquo;it could be, reverends&rdquo; &mdash; Sāriputta's own "
         "immediate, unqualified confirmation."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; the "
         "identical closing perception shared across every discourse "
         "in this set."),
        ("āvuso",
         "&ldquo;reverend&rdquo; &mdash; the mendicants' own form of "
         "address to Sāriputta, distinct from &lsquo;sir&rsquo; used "
         "for the Buddha."),
        ("sammodanīyaṁ kathaṁ sāraṇīyaṁ vītisāretvā",
         "&ldquo;exchanged greetings... when the greetings and polite "
         "conversation were over&rdquo; &mdash; the standard courtesy "
         "formula opening an approach to a senior disciple."),
    ],
    text_intro=(
        "The discourse in full: several mendicants ask Sāriputta "
        "about the same immersion beyond all perception. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Mendicants ask Sāriputta"),
        ("p", "&sect;1", "an11.20:1.1-4.3"),
    ],
    quiz=[
        {"q": "Who do the mendicants approach with their question in "
              "this discourse?",
         "opts": [
             "The Buddha directly", "Venerable Sāriputta",
             "Venerable Ānanda", "Venerable Subhūti"],
         "correct": 1,
         "expl": "Testing whether the same teaching holds from a "
                 "senior disciple."},
        {"q": "How does Sāriputta respond to the question?",
         "opts": [
             "He defers to the Buddha before answering",
             "Immediately and unqualified: \"it could be, reverends\"",
             "He declines to answer",
             "He asks the mendicants to consult the Buddha instead"],
         "correct": 1,
         "expl": "The same direct authority shown when Ānanda tested "
                 "him at AN 11.7."},
        {"q": "What form of address do the mendicants use for "
              "Sāriputta, distinct from how they address the Buddha?",
         "opts": [
             "\"Sir\"", "\"Reverend\" (āvuso)", "\"Teacher\"",
             "No address is used"],
         "correct": 1,
         "expl": "Marking the difference between addressing a senior "
                 "disciple and the Buddha."},
        {"q": "According to the guide, which combination of this "
              "closing set does this discourse complete?",
         "opts": [
             "The Buddha volunteering to mendicants",
             "Mendicants asking Sāriputta",
             "Sāriputta volunteering to mendicants",
             "None; it repeats an earlier combination"],
         "correct": 1,
         "expl": "The third of four combinations, leaving only "
                 "Sāriputta volunteering for the chapter's final "
                 "discourse."},
        {"q": "What is the content of Sāriputta's explanation?",
         "opts": [
             "A different teaching from the Buddha's own",
             "Identical to the Buddha's: perceiving only that this is "
             "peaceful, this is sublime",
             "He redirects the question entirely",
             "A shortened partial answer"],
         "correct": 1,
         "expl": "The identical explanation given throughout this "
                 "chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No scene is set beyond the mendicants approaching "
                 "Sāriputta."},
    ],
    marginalia=[
        ("A different door", [
            "not to the Buddha,",
            "but to Sāriputta this",
            "time &mdash; the question, unchanged",
        ]),
        ("Confident, unqualified", [
            "\"it could be\" &mdash; no",
            "pause, no deferring first",
            "to the Buddha's word",
        ]),
        ("Three of four complete", [
            "asked, then offered, now",
            "asked again of a disciple &mdash;",
            "one combination left",
        ]),
        ("Cross-references", [
            "AN 11.7 &middot; the earlier test of Sāriputta's own "
            "independent authority",
            "AN 11.19 &middot; previous, the Buddha volunteers the "
            "teaching",
            "AN 11.21 &middot; next, Sāriputta volunteers it himself, "
            "completing this closing set and chapter 2",
        ]),
    ],
    further=[
        '<a href="%s/an11.20/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.19.html">AN 11.19</a> &mdash; previous.',
        '<a href="an-11.21.html">AN 11.21 &middot; Immersion (4th)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.21 — Catutthasamādhisutta
# --------------------------------------------------------------------------- #
page(
    21, "Catutthasamādhi", "Immersion (4th)",
    vagga=VAGGA_2,
    meta_title="AN 11.21 — Immersion (4th) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Catutthasamādhisutta, closing chapter 2 as Sāriputta "
        "himself volunteers the same immersion teaching, completing "
        "this closing set's full chiasm. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Sāriputta addressing the mendicants"),
        ("Form", "The same immersion, now volunteered by Sāriputta "
                 "and explained at the mendicants' formal request"),
        ("Length", "~2 minutes to read"),
        ("Chapter's closer", "This discourse closes Anussativagga, "
         "the chapter these ten pages have covered"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the same demanding immersion, completing this "
                       "chapter's fourfold set"),
    ],
    why=(
        "Sāriputta himself raises the same question with the "
        "mendicants that the Buddha raised at AN 11.19, and when they "
        "formally request that he clarify it himself, he explains: it "
        "is when a mendicant perceives only that &lsquo;this is "
        "peaceful, this is sublime&rsquo;, the stilling of all "
        "activities and the ending of craving &mdash; completing this "
        "chapter's full set of four variations on the same teaching."),
    guide=[
        ("The teaching in one sentence", [
            "The same immersion beyond all ordinary perception met "
            "four times across this chapter's closing discourses, "
            "here volunteered by Sāriputta himself and explained at "
            "the mendicants' request: perceiving only the peace of "
            "nibbāna, the stilling of all activities and the ending "
            "of craving."]),
        ("The fourth and final combination", [
            "This discourse completes the chiasm this chapter's "
            "closing set has built: mendicants asked the Buddha (AN "
            "11.18), the Buddha volunteered to the mendicants (AN "
            "11.19), mendicants asked Sāriputta (AN 11.20), and now "
            "Sāriputta volunteers the same teaching to the "
            "mendicants unprompted, mirroring AN 11.19's structure "
            "exactly but with the disciple in the Buddha's role."]),
        ("The same formal request, given to a disciple", [
            "The mendicants respond to Sāriputta's own question with "
            "language echoing, but not identical to, their earlier "
            "request of the Buddha at AN 11.19: rather than naming "
            "him root and refuge, they say they would travel a long "
            "way to learn this from Sāriputta specifically, asking "
            "him to clarify it in his own presence &mdash; formal "
            "deference calibrated to a senior disciple rather than "
            "the teacher himself."]),
        ("Closing the chapter, and its own colophon", [
            "This discourse closes Anussativagga, the chapter these "
            "ten pages have covered, with the traditional colophon "
            "(&lsquo;Anussativaggo dutiyo&rsquo;, chapter two "
            "finished, followed by an uddāna summary verse) left "
            "untranslated in the English source, following this "
            "project's established convention. With this chapter "
            "complete, the identical eleven-doors list already met at "
            "AN 11.16 will recur once more before this nipāta ends, "
            "at the close of its own Rāgapeyyāla."]),
    ],
    terms=[
        ("tatra kho āyasmā sāriputto bhikkhū āmantesi",
         "&ldquo;there Sāriputta addressed the mendicants&rdquo; "
         "&mdash; this discourse's own opening frame, mirroring AN "
         "11.19's identical frame for the Buddha."),
        ("dūratopi mayaṁ, āvuso, āgaccheyyāma",
         "&ldquo;we would travel a long way... reverend&rdquo; "
         "&mdash; the mendicants' own formal request, calibrated to "
         "Sāriputta rather than the Buddha."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful, this is sublime&rdquo; &mdash; the "
         "identical closing perception, shared across all four "
         "discourses of this set and back to AN 11.7-8."),
        ("Anussativaggo dutiyo",
         "&ldquo;the chapter on recollection, the second&rdquo; "
         "&mdash; the untranslated Pāli colophon closing this "
         "chapter, left in the source without an English rendering."),
        ("suṇātha sādhukaṁ manasi karotha",
         "&ldquo;listen and apply your mind well&rdquo; &mdash; "
         "Sāriputta's own version of the standard formula introducing "
         "a substantial teaching, identical to the Buddha's own "
         "phrasing at AN 11.19."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta volunteers the same "
        "immersion teaching, closing chapter 2. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta raises the question himself"),
        ("p", "&sect;1", "an11.21:1.1-6.3"),
    ],
    quiz=[
        {"q": "Who raises the question in this discourse?",
         "opts": [
             "Several unnamed mendicants",
             "The Buddha",
             "Venerable Sāriputta, addressing the mendicants",
             "The householder Dasama"],
         "correct": 2,
         "expl": "Mirroring AN 11.19's structure, with a disciple in "
                 "the Buddha's role."},
        {"q": "What combination does this discourse complete, "
              "according to the guide?",
         "opts": [
             "The full chiasm: asked/offered, by the Buddha and by "
             "Sāriputta, across this chapter's closing four "
             "discourses",
             "Only a repetition of AN 11.18",
             "An entirely new teaching",
             "Nothing in particular"],
         "correct": 0,
         "expl": "Mendicants-Buddha, Buddha-mendicants, "
                 "mendicants-Sāriputta, Sāriputta-mendicants."},
        {"q": "How do the mendicants phrase their request to "
              "Sāriputta?",
         "opts": [
             "Identical wording to their request of the Buddha at AN "
             "11.19",
             "That they would travel a long way to learn this from "
             "Sāriputta specifically",
             "They refuse to ask him at all",
             "They demand he consult the Buddha first"],
         "correct": 1,
         "expl": "Formal deference calibrated to a senior disciple "
                 "rather than the teacher himself."},
        {"q": "What does this discourse close, according to the "
              "guide?",
         "opts": [
             "Only this single discourse",
             "Chapter 2, Anussativagga, with the traditional "
             "untranslated colophon",
             "The entire nipāta",
             "Nothing; another chapter follows immediately with no "
             "closure marked"],
         "correct": 1,
         "expl": "\"Anussativaggo dutiyo\", left untranslated per this "
                 "project's convention."},
        {"q": "According to the guide, what will recur once more "
              "before this nipāta ends?",
         "opts": [
             "The cowherd simile only",
             "The identical eleven-doors list met at AN 11.16, at the "
             "close of the Rāgapeyyāla",
             "The Mahānāma discourses",
             "Nothing further recurs"],
         "correct": 1,
         "expl": "A fixed list this project has now flagged twice."},
        {"q": "What is the content of Sāriputta's explanation?",
         "opts": [
             "A different teaching from the Buddha's own",
             "Identical throughout this set: perceiving only that "
             "this is peaceful, this is sublime",
             "He redirects the question",
             "A shortened partial answer"],
         "correct": 1,
         "expl": "The same closing formula shared across all four "
                 "discourses and back to AN 11.7-8."},
    ],
    marginalia=[
        ("The fourth and final door", [
            "Sāriputta himself",
            "now offers it, unasked &mdash;",
            "the set complete at last",
        ]),
        ("Travel far to hear it", [
            "not \"root and refuge\"",
            "this time, but still a long",
            "journey, gladly made",
        ]),
        ("Closing the chapter", [
            "Anussativaggo,",
            "the second &mdash; recollection's",
            "chapter, now complete",
        ]),
        ("Cross-references", [
            "AN 11.20 &middot; previous, mendicants ask Sāriputta",
            "AN 11.16 &middot; the eleven-doors list, to recur once "
            "more at this nipāta's own close",
            "AN 11.22 &middot; next, opening chapter 3, Sāmaññavagga",
        ]),
    ],
    further=[
        '<a href="%s/an11.21/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.20.html">AN 11.20</a> &mdash; previous.',
        '<a href="an-11.22-29.html">AN 11.22&ndash;29</a> &mdash; next, opening chapter 3.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 11.22–29 — opening Sāmaññavagga: the cowherd simile, the eye,
# and the eight contemplations, spelled out in full
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.22-29",
    "index_pali": "(untitled)",
    "nav_title": "The Cowherd, and Eight Contemplations",
    "source": "an11/an11.22-29",
    "crumb": "AN 11.22&ndash;29",
    "meta_title": ("AN 11.22–29 — The Cowherd, and Eight Contemplations "
                   "| Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.22–29, opening this nipāta's massive closing peyyāla "
        "with the cowherd simile from AN 11.17 applied to the eye "
        "and eight ways of meditating on it. From Ru-Yi Meditation "
        "Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.22&ndash;29",
    "title": "The Cowherd, and Eight Contemplations",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s, opening "
                "the chapter's own peyyāla" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The eleven-factor cowherd simile from AN 11.17, "
                 "now applied to a mendicant's meditation on the eye, "
                 "crossed against eight ways of observing it"),
        ("Length", "~2 minutes to read; stands for eight discourses"),
        ("Opening this nipāta's largest structure", "This page opens "
         "chapter 3, a single sprawling peyyāla that will run all the "
         "way to AN 11.981 &mdash; 960 discourses compressed into "
         "just twelve pages"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the individual content is simple; the scale "
                       "it represents is what takes getting used to"),
    ],
    "why": (
        "A mendicant lacking the same eleven qualities already met at "
        "AN 11.17's cowherd simile cannot meditate observing "
        "impermanence, suffering, not-self, ending, vanishing, fading "
        "away, cessation, or letting go in the eye &mdash; eight "
        "discourses (AN 11.22&ndash;29), one for each way of "
        "observing, all built from the identical eleven-factor "
        "template."),
    "guide": [
        ("The teaching in one sentence", [
            "Just as a cowherd lacking eleven skills cannot maintain a "
            "herd, a mendicant lacking the same eleven qualities "
            "cannot meditate observing the eye as impermanent, "
            "suffering, not-self, ending, vanishing, fading away, "
            "ceasing, or being let go of &mdash; eight variations on "
            "one template, one discourse each."]),
        ("A simile reused, not reinvented", [
            "This page's opening lines are word for word AN 11.17's "
            "own cowherd simile, already given in full detail there. "
            "Rather than re-explain the eleven qualities, this page "
            "and everything that follows in this chapter simply "
            "invokes the simile by name and moves straight to what "
            "changes: what the mendicant fails to meditate observing, "
            "and in what way."]),
        ("Eight ways of observing, spelled out once", [
            "The eight contemplations &mdash; %s &mdash; are named "
            "individually across AN 11.22 through AN 11.29, each its "
            "own discourse in the source. This is the only place in "
            "the entire chapter where these eight are spelled out one "
            "at a time rather than compressed with an ellipsis; every "
            "later page in this peyyāla assumes the reader already "
            "has this list in mind." % EIGHT_CONTEMPLATIONS]),
        ("What this page opens", [
            "AN 11.22 gives this chapter its own namesake, "
            "<em>Sāmaññavagga</em>, the Chapter on Similarity &mdash; "
            "named for how each of its discourses shares an identical "
            "underlying pattern. What follows across the next eleven "
            "pages is the same pattern applied first to the other "
            "five sense faculties, then systematically to nine "
            "further categories, before a final page mirrors the "
            "whole structure as its positive counterpart."]),
    ],
    "terms": [
        ("gopālaka",
         "&ldquo;cowherd&rdquo; &mdash; the simile inherited whole "
         "from AN 11.17, invoked here by reference rather than "
         "re-explained."),
        ("cakkhusmiṁ aniccānupassī",
         "&ldquo;meditate observing impermanence in the eye&rdquo; "
         "&mdash; the first of eight contemplations, and the pattern "
         "every later page in this chapter will vary only by "
         "category."),
        ("khayānupassī, vayānupassī",
         "&ldquo;observing ending&rdquo;, &ldquo;observing "
         "vanishing&rdquo; &mdash; two closely related contemplations, "
         "the fourth and fifth of the eight, worth distinguishing "
         "from each other."),
        ("paṭinissaggānupassī",
         "&ldquo;observing letting go&rdquo; &mdash; the eighth and "
         "final contemplation, closing the sequence this page "
         "establishes."),
        ("sāmañña",
         "&ldquo;similarity&rdquo; &mdash; the term giving this "
         "chapter its name, Sāmaññavagga, for the identical pattern "
         "repeated across every discourse within it."),
    ],
    "text_intro": (
        "The compressed text in full: the cowherd simile, then eight "
        "ways of meditating on the eye, named one by one. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "The cowherd simile, applied to the eye"),
        ("p", "&sect;1", ["an11.22:1.1", "an11.22:1.2", "an11.22:1.3",
                          "an11.22:1.4", "an11.22:2.1"]),
        ("h3", "Eight contemplations, named in turn"),
        ("p", "&sect;2", ["an11.22:3.1", "an11.23:1.1", "an11.24:1.1",
                          "an11.25:1.1", "an11.26:1.1", "an11.27:1.1",
                          "an11.28:1.1", "an11.29:1.1"]),
    ],
    "quiz": [
        {"q": "What simile does this page's opening reuse?",
         "opts": [
             "A new simile invented for this chapter",
             "The eleven-factor cowherd simile already given in full "
             "at AN 11.17",
             "The thoroughbred and wild colt from AN 11.9",
             "The branchless tree from AN 11.3"],
         "correct": 1,
         "expl": "Invoked by reference, not re-explained."},
        {"q": "How many discourses does this single page stand for?",
         "opts": [
             "One", "Eight (AN 11.22–29), one per contemplation",
             "Forty", "Four hundred eighty"],
         "correct": 1,
         "expl": "One discourse for each of the eight ways of "
                 "observing the eye."},
        {"q": "What are the eight ways of observing named across "
              "these eight discourses?",
         "opts": [
             "Impermanence, suffering, not-self, ending, vanishing, "
             "fading away, cessation, and letting go",
             "The four elements and four formless dimensions",
             "The five hindrances and three unwholesome roots",
             "The seven factors of awakening"],
         "correct": 0,
         "expl": "Spelled out here in full for the only time in this "
                 "chapter."},
        {"q": "What does this chapter's name, Sāmaññavagga, refer to?",
         "opts": [
             "A specific place name",
             "\"Similarity\" — the identical underlying pattern "
             "shared across every discourse in the chapter",
             "A disciple's name",
             "A type of ascetic practice"],
         "correct": 1,
         "expl": "Naming the chapter's own defining structural feature."},
        {"q": "According to the guide, what makes this page unique "
              "within the whole chapter?",
         "opts": [
             "It is the only page with a narrative story",
             "It is the only place where the eight contemplations are "
             "spelled out one at a time rather than compressed with "
             "an ellipsis",
             "It is the shortest page in the chapter",
             "It introduces an entirely new simile not used again"],
         "correct": 1,
         "expl": "Every later page assumes this list already "
                 "established."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, in the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("A simile, reused", [
            "eleven factors,",
            "met once at AN 11.17 &mdash;",
            "now simply invoked",
        ]),
        ("Eight ways of seeing", [
            "impermanence,",
            "suffering, not-self, and on",
            "to letting go itself",
        ]),
        ("A chapter's own name", [
            "sāmañña, likeness &mdash;",
            "every page in this chapter",
            "shares one pattern",
        ]),
        ("Cross-references", [
            "AN 11.17 &middot; the cowherd simile's first full telling",
            "AN 11.21 &middot; previous, closing chapter 2",
            "AN 11.30&ndash;69 &middot; next, the same eight applied "
            "to the remaining five senses",
        ]),
    ],
    "further": [
        '<a href="%s/an11.22-29/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.21.html">AN 11.21</a> &mdash; previous.',
        '<a href="an-11.30-69.html">AN 11.30&ndash;69</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.30–69 — the ear, nose, tongue, body, and mind
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.30-69",
    "index_pali": "(untitled)",
    "nav_title": "The Ear, Etc.",
    "source": "an11/an11.30-69",
    "crumb": "AN 11.30&ndash;69",
    "meta_title": "AN 11.30–69 — The Ear, Etc. | Ru-Yi Meditation Center",
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.30–69, extending AN 11.22–29's cowherd simile and "
        "eight contemplations to the ear, nose, tongue, body, and "
        "mind. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.30&ndash;69",
    "title": "The Ear, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical cowherd simile and eight "
                 "contemplations from AN 11.22–29, now applied to "
                 "the remaining five sense faculties"),
        ("Length", "~1 minute to read; stands for forty discourses"),
        ("First fully-compressed page", "The first page in this "
         "chapter to use bare ellipsis rather than spell out its "
         "content in full"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial once AN 11.22&ndash;29's pattern is "
                       "understood"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and the same eight "
        "contemplations already given in full at AN 11.22&ndash;29 "
        "for the eye apply identically to the ear, nose, tongue, "
        "body, and mind &mdash; five more sense faculties times eight "
        "contemplations, forty further discourses (AN "
        "11.30&ndash;69), compressed onto a single page."),
    "guide": [
        ("The teaching in one sentence", [
            "Everything already established at AN 11.22&ndash;29 for "
            "the eye &mdash; the cowherd simile, the eight "
            "contemplations &mdash; applies without change to the "
            "remaining five sense faculties: ear, nose, tongue, body, "
            "and mind."]),
        ("The first fully compressed page", [
            "Where AN 11.22&ndash;29 spelled out all eight "
            "contemplations across eight separate discourses, this "
            "page compresses the same content into a single short "
            "passage using bare ellipsis: &lsquo;&hellip; ear &hellip; "
            "nose &hellip; tongue &hellip; body &hellip; mind&rsquo;, "
            "trusting the reader to supply both the cowherd simile "
            "and all eight contemplations from the previous page."]),
        ("The arithmetic", [
            "Five remaining sense faculties, each crossed against the "
            "same eight contemplations, gives forty discourses &mdash; "
            "matching the range AN 11.30 through AN 11.69 exactly, "
            "and completing the first of this chapter's ten "
            "categories: the six sense faculties in full (one eye "
            "page plus this one), fifty-six words of Pāli standing "
            "for forty-eight actual discourses across the two pages."]),
        ("How to read a page this compressed", [
            "From here through AN 11.454&ndash;501, most pages in "
            "this chapter will follow this same extremely compressed "
            "form: a category list swapped in place of the eye, "
            "eight contemplations left entirely implicit. The reading "
            "guide for each such page will name the arithmetic and "
            "the category being crossed, rather than re-explain a "
            "structure already established here."]),
    ],
    "terms": [
        ("sotasmiṁ, ghānasmiṁ, jivhāya, kāyasmiṁ, manasmiṁ",
         "&ldquo;in the ear, in the nose, in the tongue, in the body, "
         "in the mind&rdquo; &mdash; the five remaining sense "
         "faculties this page substitutes for AN 11.22&ndash;29's "
         "eye, in the standard six-sense-faculty order."),
        ("pe",
         "the Pāli ellipsis marker (peyyāla) &mdash; not itself part "
         "of the English translation, but the underlying convention "
         "this and most later pages in this chapter render as "
         "&lsquo;&hellip;&rsquo;."),
        ("cakkhusmiṁ, sotasmiṁ",
         "&ldquo;in the eye, in the ear&rdquo; &mdash; the first two "
         "of the six sense faculties, together spanning this page and "
         "its immediate predecessor."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations named in full at AN "
         "11.22&ndash;29, here left entirely implicit."),
        ("chaḷāyatana",
         "not named directly here, but the traditional term for the "
         "six sense faculties (āyatana) this page and its predecessor "
         "together complete."),
    ],
    "text_intro": (
        "The compressed text in full: the same cowherd simile and "
        "eight contemplations, now applied to five more sense "
        "faculties. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "Five more sense faculties, the same pattern"),
        ("p", "&sect;1", "an11.30-69:1.1-1.6"),
    ],
    "quiz": [
        {"q": "What does this page apply to the remaining five sense "
              "faculties?",
         "opts": [
             "An entirely new simile",
             "The identical cowherd simile and eight contemplations "
             "already given in full at AN 11.22–29",
             "Only the cowherd simile, without the contemplations",
             "A shortened five-item list"],
         "correct": 1,
         "expl": "The same pattern, unchanged, applied to new content."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty (five sense faculties times eight "
             "contemplations)",
             "Forty-eight", "Four hundred eighty"],
         "correct": 1,
         "expl": "5 × 8 = 40, matching AN 11.30 through AN 11.69."},
        {"q": "How does this page's own text differ from AN "
              "11.22–29's?",
         "opts": [
             "It is longer and more detailed",
             "It uses bare ellipsis, compressing everything into a "
             "single short passage rather than spelling content out",
             "It removes the cowherd simile entirely",
             "It introduces a ninth contemplation"],
         "correct": 1,
         "expl": "The first fully compressed page in this chapter."},
        {"q": "What five sense faculties does this page name?",
         "opts": [
             "Sights, sounds, smells, tastes, touches",
             "Ear, nose, tongue, body, and mind",
             "Consciousness, contact, feeling, perception, intention",
             "Craving, thought, consideration, view, intention"],
         "correct": 1,
         "expl": "Completing the six sense faculties alongside AN "
                 "11.22–29's eye."},
        {"q": "According to the guide, what should a reader expect "
              "from most later pages in this chapter?",
         "opts": [
             "Full narrative detail, re-explained each time",
             "Extremely compressed form, naming only the category "
             "swapped in and the arithmetic behind it",
             "A return to spelling out all eight contemplations",
             "No further compression at all"],
         "correct": 1,
         "expl": "This page sets the pattern the rest of the chapter "
                 "follows."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Five more doors", [
            "ear, nose, tongue, and",
            "body, mind &mdash; the same eight",
            "ways, applied again",
        ]),
        ("Compression begins", [
            "no longer spelled out,",
            "just named and passed over &mdash;",
            "the pattern, assumed",
        ]),
        ("Six senses complete", [
            "one page for the eye,",
            "one page for the other five &mdash;",
            "forty-eight in all",
        ]),
        ("Cross-references", [
            "AN 11.22&ndash;29 &middot; previous, the eye and all "
            "eight contemplations spelled out",
            "AN 11.70&ndash;117 &middot; next, the six sense objects",
        ]),
    ],
    "further": [
        '<a href="%s/an11.30-69/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.22-29.html">AN 11.22&ndash;29</a> &mdash; previous.',
        '<a href="an-11.70-117.html">AN 11.70&ndash;117</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.70–117 — sights, sounds, smells, tastes, touches, and ideas
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.70-117",
    "index_pali": "(untitled)",
    "nav_title": "Sights, Etc.",
    "source": "an11/an11.70-117",
    "crumb": "AN 11.70&ndash;117",
    "meta_title": "AN 11.70–117 — Sights, Etc. | Ru-Yi Meditation Center",
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.70–117, moving this chapter's peyyāla from the six "
        "sense faculties to the six sense objects: sights, sounds, "
        "smells, tastes, touches, and ideas. From Ru-Yi Meditation "
        "Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.70&ndash;117",
    "title": "Sights, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six sense objects"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("A new category, the standard scale", "The first of nine "
         "remaining categories in this chapter, each contributing "
         "forty-eight discourses"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations already established move from the six sense "
        "faculties to the six sense objects &mdash; sights, sounds, "
        "smells, tastes, touches, and ideas &mdash; six categories "
        "times eight contemplations, forty-eight further discourses "
        "(AN 11.70&ndash;117)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six sense objects &mdash; sights, "
            "sounds, smells, tastes, touches, and ideas &mdash; the "
            "second of this chapter's ten categories."]),
        ("From faculty to object", [
            "Having completed the six sense faculties (the eye and "
            "its five companions) across the previous two pages, this "
            "page moves to what those faculties perceive: the sense "
            "objects themselves. This shift &mdash; from the sensing "
            "organ to the thing sensed &mdash; is the first step of a "
            "systematic analytical sequence this chapter will now "
            "carry through eight further steps."]),
        ("The arithmetic, now standard", [
            "Six sense objects times eight contemplations gives "
            "forty-eight discourses, exactly matching AN 11.70 "
            "through AN 11.117. From this page onward, forty-eight "
            "is the standard unit this chapter's remaining categories "
            "will each contribute, until the final compressed page "
            "changes the pattern entirely."]),
        ("A familiar analytical sequence", [
            "Sense faculty, then sense object, then (as the following "
            "pages will show) consciousness, contact, feeling, "
            "perception, intention, craving, thought, and "
            "consideration &mdash; this ten-step progression will be "
            "recognizable to readers familiar with the analytical "
            "method found elsewhere in the canon's treatment of the "
            "six sense bases, systematically applied here to insight "
            "into impermanence."]),
    ],
    "terms": [
        ("rūpesu, saddesu, gandhesu, rasesu, phoṭṭhabbesu, dhammesu",
         "&ldquo;in sights, in sounds, in smells, in tastes, in "
         "touches, in ideas&rdquo; &mdash; the six sense objects, "
         "paired with the six sense faculties in the standard order."),
        ("rūpa",
         "&ldquo;sight&rdquo;, form &mdash; the first sense object, "
         "paired with the eye as its faculty."),
        ("dhamma",
         "&ldquo;idea&rdquo;, mental object &mdash; the sixth sense "
         "object, paired with the mind, completing the standard "
         "six-object list."),
        ("bāhira āyatana",
         "not named directly here, but the traditional term for the "
         "six external sense bases (objects) this page addresses, "
         "distinct from the six internal bases (faculties) of the "
         "previous two pages."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six sense objects. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    "text": [
        ("h3", "Six sense objects, the same pattern"),
        ("p", "&sect;1", "an11.70-117:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page move to, after the six "
              "sense faculties?",
         "opts": [
             "The six sense objects: sights, sounds, smells, tastes, "
             "touches, and ideas",
             "The five hindrances",
             "The four elements",
             "The eight contemplations themselves"],
         "correct": 0,
         "expl": "From the sensing organ to the thing sensed."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight (six objects times eight "
             "contemplations)", "Four hundred eighty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.70 through AN 11.117."},
        {"q": "What is the sixth and final sense object named here?",
         "opts": [
             "Touches", "Sounds", "Ideas (dhamma)", "Smells"],
         "correct": 2,
         "expl": "Paired with the mind, completing the six-object "
                 "list."},
        {"q": "According to the guide, what does forty-eight become "
              "from this page onward?",
         "opts": [
             "An irrelevant number",
             "The standard unit each of this chapter's remaining "
             "categories will contribute",
             "A number never repeated again",
             "The total for the whole chapter"],
         "correct": 1,
         "expl": "Six items times eight contemplations, repeated "
                 "category by category."},
        {"q": "According to the guide, what larger sequence does this "
              "page begin?",
         "opts": [
             "A random assortment of unrelated topics",
             "A systematic ten-step analytical sequence — faculty, "
             "object, consciousness, contact, and so on",
             "A sequence that abandons the eight contemplations",
             "Nothing beyond this single page"],
         "correct": 1,
         "expl": "Recognizable from the canon's broader treatment of "
                 "the six sense bases."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("From organ to object", [
            "not the eye itself now,",
            "but what it sees &mdash; sights, sounds,",
            "smells, tastes, touch, thought",
        ]),
        ("Forty-eight, the new unit", [
            "six objects, eight ways",
            "of seeing each &mdash; this number",
            "will recur again",
        ]),
        ("A sequence begins", [
            "faculty then object,",
            "soon consciousness, contact,",
            "feeling, and beyond",
        ]),
        ("Cross-references", [
            "AN 11.30&ndash;69 &middot; previous, the remaining five "
            "sense faculties",
            "AN 11.118&ndash;165 &middot; next, the six "
            "consciousnesses",
        ]),
    ],
    "further": [
        '<a href="%s/an11.70-117/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.30-69.html">AN 11.30&ndash;69</a> &mdash; previous.',
        '<a href="an-11.118-165.html">AN 11.118&ndash;165</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.118–165 — the six consciousnesses
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.118-165",
    "index_pali": "(untitled)",
    "nav_title": "Eye Consciousness, Etc.",
    "source": "an11/an11.118-165",
    "crumb": "AN 11.118&ndash;165",
    "meta_title": ("AN 11.118–165 — Eye Consciousness, Etc. | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.118–165, moving this chapter's peyyāla to the six "
        "kinds of sense consciousness. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.118&ndash;165",
    "title": "Eye Consciousness, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of consciousness"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Third of ten categories", "Consciousness, the third step "
         "in this chapter's ten-part analytical sequence"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of consciousness that "
        "arise from each sense faculty and its object &mdash; eye "
        "consciousness, ear consciousness, nose consciousness, "
        "tongue consciousness, body consciousness, and mind "
        "consciousness &mdash; forty-eight further discourses (AN "
        "11.118&ndash;165)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of consciousness &mdash; eye, "
            "ear, nose, tongue, body, and mind consciousness &mdash; "
            "the third of this chapter's ten categories."]),
        ("What consciousness adds to the sequence", [
            "Having covered the sense faculty (what perceives) and "
            "the sense object (what is perceived), this page moves to "
            "consciousness &mdash; the awareness that arises "
            "specifically when a given faculty meets its "
            "corresponding object, the third link in the causal chain "
            "this chapter's sequence is tracing."]),
        ("Named for its faculty, not its object", [
            "Each of the six consciousnesses in this page's list "
            "takes its name from the sense faculty it arises through "
            "&mdash; &lsquo;eye consciousness&rsquo;, not "
            "&lsquo;sight consciousness&rsquo; &mdash; a naming "
            "convention consistent throughout the canon's treatment "
            "of the six sense bases."]),
        ("The same forty-eight", [
            "Six kinds of consciousness times eight contemplations "
            "gives forty-eight discourses, matching AN 11.118 through "
            "AN 11.165 exactly &mdash; the same arithmetic already "
            "established at AN 11.70&ndash;117, now the third of "
            "eight remaining categories to repeat it."]),
    ],
    "terms": [
        ("cakkhuviññāṇe, sotaviññāṇe, ghānaviññāṇe, jivhāviññāṇe, "
         "kāyaviññāṇe, manoviññāṇe",
         "&ldquo;eye, ear, nose, tongue, body, and mind "
         "consciousness&rdquo; &mdash; the six kinds of consciousness, "
         "each named for its corresponding sense faculty."),
        ("viññāṇa",
         "&ldquo;consciousness&rdquo;, awareness &mdash; the third "
         "step in this chapter's analytical sequence, arising when "
         "faculty meets object."),
        ("cakkhuviññāṇa",
         "&ldquo;eye consciousness&rdquo; &mdash; the first of the "
         "six, arising specifically when the eye meets a sight."),
        ("manoviññāṇa",
         "&ldquo;mind consciousness&rdquo; &mdash; the sixth and "
         "final kind, completing the list."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of consciousness. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six consciousnesses, the same pattern"),
        ("p", "&sect;1", "an11.118-165:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six sense objects",
             "The six kinds of consciousness — eye, ear, nose, "
             "tongue, body, and mind consciousness",
             "The six kinds of contact",
             "The six kinds of feeling"],
         "correct": 1,
         "expl": "The third step in this chapter's analytical "
                 "sequence."},
        {"q": "What convention names each of the six consciousnesses, "
              "according to the guide?",
         "opts": [
             "Named for the object perceived",
             "Named for the sense faculty it arises through, e.g. "
             "\"eye consciousness\", not \"sight consciousness\"",
             "Named randomly with no consistent pattern",
             "Named for the contemplation applied to it"],
         "correct": 1,
         "expl": "Consistent throughout the canon's treatment of the "
                 "six sense bases."},
        {"q": "When does eye consciousness specifically arise, "
              "according to the guide?",
         "opts": [
             "At birth, permanently",
             "When the eye meets a sight",
             "Only during meditation",
             "It never arises"],
         "correct": 1,
         "expl": "Consciousness is the awareness arising when faculty "
                 "meets object."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "Four hundred eighty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.118 through AN 11.165."},
        {"q": "What is the sixth and final consciousness named here?",
         "opts": [
             "Body consciousness", "Tongue consciousness",
             "Mind consciousness (manoviññāṇa)", "Nose consciousness"],
         "correct": 2,
         "expl": "Completing the six-consciousness list."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("When faculty meets object", [
            "eye meets sight, and then",
            "eye consciousness arises &mdash;",
            "the third link, traced here",
        ]),
        ("Named for the door", [
            "not for what is seen,",
            "but for the seeing itself &mdash;",
            "eye, ear, nose, and on",
        ]),
        ("The same forty-eight", [
            "six kinds, eight ways each",
            "of seeing them fall away &mdash;",
            "the pattern repeats",
        ]),
        ("Cross-references", [
            "AN 11.70&ndash;117 &middot; previous, the six sense "
            "objects",
            "AN 11.166&ndash;213 &middot; next, the six kinds of "
            "contact",
        ]),
    ],
    "further": [
        '<a href="%s/an11.118-165/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.70-117.html">AN 11.70&ndash;117</a> &mdash; previous.',
        '<a href="an-11.166-213.html">AN 11.166&ndash;213</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.166–213 — the six kinds of contact
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.166-213",
    "index_pali": "(untitled)",
    "nav_title": "Eye Contact, Etc.",
    "source": "an11/an11.166-213",
    "crumb": "AN 11.166&ndash;213",
    "meta_title": "AN 11.166–213 — Eye Contact, Etc. | Ru-Yi Meditation Center",
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.166–213, moving this chapter's peyyāla to the six "
        "kinds of contact. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.166&ndash;213",
    "title": "Eye Contact, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of contact"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Fourth of ten categories", "Contact, the fourth step in "
         "this chapter's ten-part analytical sequence"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of contact &mdash; eye "
        "contact, ear contact, nose contact, tongue contact, body "
        "contact, and mind contact &mdash; forty-eight further "
        "discourses (AN 11.166&ndash;213)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of contact &mdash; eye, ear, "
            "nose, tongue, body, and mind contact &mdash; the fourth "
            "of this chapter's ten categories."]),
        ("What contact adds to the sequence", [
            "Contact (phassa) is the meeting itself of faculty, "
            "object, and consciousness together &mdash; not merely "
            "physical touch, but the technical convergence that "
            "the canon treats as the necessary condition for feeling "
            "to arise, the fourth link in this chapter's traced "
            "sequence."]),
        ("A term familiar from dependent origination", [
            "Contact is also a familiar link from the twelve-factor "
            "chain of dependent origination (paṭicca samuppāda), "
            "where contact conditions feeling, feeling conditions "
            "craving, and so on &mdash; the same causal ordering this "
            "chapter's own sequence will continue to trace through "
            "its remaining categories."]),
        ("The same forty-eight, continuing", [
            "Six kinds of contact times eight contemplations gives "
            "forty-eight discourses, matching AN 11.166 through AN "
            "11.213 exactly &mdash; the fourth category in a row to "
            "repeat this chapter's now-familiar arithmetic."]),
    ],
    "terms": [
        ("cakkhusamphasse, sotasamphasse, ghānasamphasse, "
         "jivhāsamphasse, kāyasamphasse, manosamphasse",
         "&ldquo;eye, ear, nose, tongue, body, and mind contact&rdquo; "
         "&mdash; the six kinds of contact, named for their "
         "corresponding sense faculties."),
        ("phassa",
         "&ldquo;contact&rdquo; &mdash; the fourth step in this "
         "chapter's sequence, the convergence of faculty, object, and "
         "consciousness."),
        ("cakkhusamphassa",
         "&ldquo;eye contact&rdquo; &mdash; the first of the six, "
         "opening this page's list."),
        ("paṭicca samuppāda",
         "not named directly here, but the twelve-factor chain of "
         "dependent origination in which contact is also a familiar "
         "link, conditioning feeling."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of contact. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of contact, the same pattern"),
        ("p", "&sect;1", "an11.166-213:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of consciousness",
             "The six kinds of contact — eye, ear, nose, tongue, "
             "body, and mind contact",
             "The six kinds of feeling",
             "The six kinds of perception"],
         "correct": 1,
         "expl": "The fourth step in this chapter's analytical "
                 "sequence."},
        {"q": "What does \"contact\" (phassa) technically refer to, "
              "according to the guide?",
         "opts": [
             "Physical touch alone",
             "The convergence of faculty, object, and consciousness "
             "together",
             "A type of monastic greeting",
             "An unrelated meditative state"],
         "correct": 1,
         "expl": "Not merely physical touch, but a technical "
                 "convergence."},
        {"q": "What familiar chain also includes contact as a link, "
              "according to the guide?",
         "opts": [
             "The noble eightfold path",
             "The twelve-factor chain of dependent origination "
             "(paṭicca samuppāda)",
             "The five hindrances",
             "The seven factors of awakening"],
         "correct": 1,
         "expl": "Where contact conditions feeling, and feeling "
                 "conditions craving."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "One hundred sixty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.166 through AN 11.213."},
        {"q": "What is the first kind of contact named in this page's "
              "list?",
         "opts": [
             "Mind contact", "Eye contact", "Ear contact",
             "Body contact"],
         "correct": 1,
         "expl": "Opening the list in the standard sense-faculty "
                 "order."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Where three meet", [
            "faculty, object,",
            "and consciousness together &mdash;",
            "contact, the fourth link",
        ]),
        ("A familiar chain", [
            "the same phassa that",
            "conditions feeling, craving &mdash;",
            "dependent origin",
        ]),
        ("Forty-eight, again", [
            "six kinds of touching,",
            "eight ways each fall away &mdash;",
            "the pattern, unbroken",
        ]),
        ("Cross-references", [
            "AN 11.118&ndash;165 &middot; previous, the six kinds of "
            "consciousness",
            "AN 11.214&ndash;261 &middot; next, feeling born of "
            "contact",
        ]),
    ],
    "further": [
        '<a href="%s/an11.166-213/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.118-165.html">AN 11.118&ndash;165</a> &mdash; previous.',
        '<a href="an-11.214-261.html">AN 11.214&ndash;261</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.214–261 — feeling born of contact
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.214-261",
    "index_pali": "(untitled)",
    "nav_title": "Feeling Born of Eye Contact, Etc.",
    "source": "an11/an11.214-261",
    "crumb": "AN 11.214&ndash;261",
    "meta_title": ("AN 11.214–261 — Feeling Born of Eye Contact, Etc. "
                   "| Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.214–261, moving this chapter's peyyāla to the six "
        "kinds of feeling born of contact. From Ru-Yi Meditation "
        "Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.214&ndash;261",
    "title": "Feeling Born of Eye Contact, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of feeling born "
                 "of contact"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Fifth of ten categories", "Feeling, the fifth step in this "
         "chapter's ten-part analytical sequence, and the point "
         "dependent origination flags as decisive"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of feeling that arise "
        "specifically from contact &mdash; feeling born of eye "
        "contact, ear contact, nose contact, tongue contact, body "
        "contact, and mind contact &mdash; forty-eight further "
        "discourses (AN 11.214&ndash;261)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of feeling born of contact "
            "&mdash; through the eye, ear, nose, tongue, body, and "
            "mind &mdash; the fifth of this chapter's ten categories."]),
        ("Why feeling matters more than the others", [
            "In the dependent origination chain this sequence echoes, "
            "feeling is the specific link where craving takes hold or "
            "does not: contact conditions feeling, and feeling "
            "conditions craving, making the contemplations applied "
            "here &mdash; especially observing feeling as impermanent "
            "&mdash; a point of real leverage, not simply one more "
            "category in a mechanical series."]),
        ("Named for its cause, not itself", [
            "Each of the six feelings in this page's list is named "
            "for the contact that gives rise to it &mdash; "
            "&lsquo;feeling born of eye contact&rsquo;, not simply "
            "&lsquo;eye feeling&rsquo; &mdash; making explicit the "
            "causal link between the fourth category (contact) and "
            "this fifth one."]),
        ("The same forty-eight, at the sequence's midpoint", [
            "Six kinds of feeling times eight contemplations gives "
            "forty-eight discourses, matching AN 11.214 through AN "
            "11.261 exactly &mdash; the fifth of ten categories, "
            "marking roughly the midpoint of this chapter's full "
            "ten-category sequence."]),
    ],
    "terms": [
        ("cakkhusamphassajā vedanāya, sotasamphassajā vedanāya",
         "&ldquo;feeling born of eye contact&rdquo;, &ldquo;feeling "
         "born of ear contact&rdquo; &mdash; the first two of the six "
         "feelings, each explicitly named for its causal source."),
        ("vedanā",
         "&ldquo;feeling&rdquo; &mdash; the fifth step in this "
         "chapter's sequence, and the pivotal link in dependent "
         "origination where craving may or may not take hold."),
        ("manosamphassajā vedanāya",
         "&ldquo;feeling born of mind contact&rdquo; &mdash; the "
         "sixth and final feeling, completing the list."),
        ("taṇhā",
         "not named directly here, but &ldquo;craving&rdquo;, the "
         "link feeling conditions in the dependent origination chain "
         "this category echoes."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of feeling born of contact. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of feeling, the same pattern"),
        ("p", "&sect;1", "an11.214-261:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of contact",
             "The six kinds of feeling born of contact",
             "The six kinds of perception",
             "The six kinds of craving"],
         "correct": 1,
         "expl": "The fifth step in this chapter's analytical "
                 "sequence."},
        {"q": "According to the guide, why does feeling carry special "
              "significance in this sequence?",
         "opts": [
             "It does not; it is just one more category",
             "In dependent origination, feeling is the specific link "
             "where craving takes hold or does not",
             "Feeling is unrelated to the other categories",
             "Feeling is the final category in the sequence"],
         "correct": 1,
         "expl": "A point of real leverage, not merely a mechanical "
                 "step."},
        {"q": "How is each of the six feelings named?",
         "opts": [
             "Randomly, with no naming pattern",
             "For the contact that gives rise to it — \"feeling born "
             "of eye contact\", not simply \"eye feeling\"",
             "For the object perceived",
             "For the contemplation applied to it"],
         "correct": 1,
         "expl": "Making explicit the causal link between contact and "
                 "feeling."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "One hundred sixty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.214 through AN 11.261."},
        {"q": "Where does this category fall in this chapter's "
              "ten-category sequence, according to the guide?",
         "opts": [
             "First", "Fifth, roughly the midpoint", "Last",
             "It is not part of the sequence"],
         "correct": 1,
         "expl": "The fifth of ten categories in the full sequence."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, in the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Where craving takes hold", [
            "contact gives feeling,",
            "feeling gives craving room &mdash;",
            "or does not, seen through",
        ]),
        ("Named for its source", [
            "not \"eye feeling\", but",
            "feeling born of eye contact &mdash;",
            "the cause, kept explicit",
        ]),
        ("Halfway through ten", [
            "five categories down,",
            "five more to come &mdash; the same",
            "forty-eight, again",
        ]),
        ("Cross-references", [
            "AN 11.166&ndash;213 &middot; previous, the six kinds of "
            "contact",
            "AN 11.262&ndash;309 &middot; next, the six kinds of "
            "perception",
        ]),
    ],
    "further": [
        '<a href="%s/an11.214-261/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.166-213.html">AN 11.166&ndash;213</a> &mdash; previous.',
        '<a href="an-11.262-309.html">AN 11.262&ndash;309</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.262–309 — perception of sights, etc.
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.262-309",
    "index_pali": "(untitled)",
    "nav_title": "Perception of Sights, Etc.",
    "source": "an11/an11.262-309",
    "crumb": "AN 11.262&ndash;309",
    "meta_title": ("AN 11.262–309 — Perception of Sights, Etc. | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.262–309, moving this chapter's peyyāla to the six "
        "kinds of perception. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.262&ndash;309",
    "title": "Perception of Sights, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of perception"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Sixth of ten categories", "Perception, returning this "
         "sequence to the six sense objects rather than the sense "
         "faculties"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of perception &mdash; "
        "perception of sights, sounds, smells, tastes, touches, and "
        "ideas &mdash; forty-eight further discourses (AN "
        "11.262&ndash;309)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of perception &mdash; of "
            "sights, sounds, smells, tastes, touches, and ideas "
            "&mdash; the sixth of this chapter's ten categories."]),
        ("A return to the sense objects, not the faculties", [
            "Unlike consciousness, contact, and feeling, which this "
            "sequence has been naming for their originating sense "
            "faculty (eye, ear, and so on), this category names each "
            "perception for its sense object instead &mdash; "
            "&lsquo;perception of sights&rsquo;, not &lsquo;eye "
            "perception&rsquo; &mdash; echoing AN 11.70&ndash;117's "
            "own naming convention rather than the faculty-based "
            "naming of the three categories in between."]),
        ("What perception adds", [
            "Perception (saññā) is what recognizes and labels a sense "
            "object once feeling has already registered it &mdash; "
            "the mind's act of identifying &lsquo;this is a "
            "sight&rsquo;, distinct from the bare feeling that arose "
            "moments before, and itself a well-known aggregate "
            "(khandha) in the canon's standard fivefold analysis of a "
            "person."]),
        ("The same forty-eight, continuing", [
            "Six kinds of perception times eight contemplations gives "
            "forty-eight discourses, matching AN 11.262 through AN "
            "11.309 exactly &mdash; the sixth of ten categories to "
            "repeat this chapter's now-familiar arithmetic."]),
    ],
    "terms": [
        ("rūpasaññāya, saddasaññāya, gandhasaññāya, rasasaññāya, "
         "phoṭṭhabbasaññāya, dhammasaññāya",
         "&ldquo;perception of sights, sounds, smells, tastes, "
         "touches, and ideas&rdquo; &mdash; the six kinds of "
         "perception, named for their sense objects."),
        ("saññā",
         "&ldquo;perception&rdquo; &mdash; the sixth step in this "
         "chapter's sequence, and one of the five aggregates "
         "(khandha) in the canon's standard analysis of a person."),
        ("rūpasaññā",
         "&ldquo;perception of sights&rdquo; &mdash; the first of the "
         "six, opening this page's list."),
        ("khandha",
         "not named directly here, but the five aggregates "
         "&mdash; form, feeling, perception, choices, and "
         "consciousness &mdash; of which perception (saññā) is one."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of perception. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of perception, the same pattern"),
        ("p", "&sect;1", "an11.262-309:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of feeling",
             "The six kinds of perception — of sights, sounds, "
             "smells, tastes, touches, and ideas",
             "The six kinds of contact",
             "The six kinds of craving"],
         "correct": 1,
         "expl": "The sixth step in this chapter's analytical "
                 "sequence."},
        {"q": "According to the guide, how does this category's "
              "naming convention differ from the three before it?",
         "opts": [
             "It names each item for its sense object, echoing AN "
             "11.70–117, rather than for the sense faculty",
             "It uses no naming convention at all",
             "It introduces an entirely new set of names",
             "It is identical to the feeling category's naming"],
         "correct": 0,
         "expl": "Consciousness, contact, and feeling were named for "
                 "their sense faculty; perception returns to naming "
                 "by object."},
        {"q": "What does perception (saññā) do, according to the "
              "guide?",
         "opts": [
             "Nothing; it plays no active role",
             "Recognizes and labels a sense object once feeling has "
             "already registered it",
             "Physically touches the sense object",
             "Replaces feeling entirely"],
         "correct": 1,
         "expl": "The mind's act of identifying what has been felt."},
        {"q": "What broader category does perception belong to, "
              "according to the guide?",
         "opts": [
             "The four elements",
             "The five aggregates (khandha)",
             "The seven factors of awakening",
             "The three unwholesome roots"],
         "correct": 1,
         "expl": "One of the five khandhas in the canon's standard "
                 "analysis of a person."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "One hundred sixty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.262 through AN 11.309."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Naming by object again", [
            "not eye but sight now,",
            "not ear but sound &mdash; the object",
            "gives its name back",
        ]),
        ("What labels the felt", [
            "feeling registers,",
            "then perception names it &mdash;",
            "\"this is a sight\", seen",
        ]),
        ("One of five heaps", [
            "saññā, one heap",
            "among form, feeling, choices,",
            "consciousness &mdash; and this",
        ]),
        ("Cross-references", [
            "AN 11.214&ndash;261 &middot; previous, feeling born of "
            "contact",
            "AN 11.310&ndash;357 &middot; next, intention regarding "
            "sights",
        ]),
    ],
    "further": [
        '<a href="%s/an11.262-309/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.214-261.html">AN 11.214&ndash;261</a> &mdash; previous.',
        '<a href="an-11.310-357.html">AN 11.310&ndash;357</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.310–357 — intention regarding sights, etc.
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.310-357",
    "index_pali": "(untitled)",
    "nav_title": "Intention Regarding Sights, Etc.",
    "source": "an11/an11.310-357",
    "crumb": "AN 11.310&ndash;357",
    "meta_title": ("AN 11.310–357 — Intention Regarding Sights, Etc. "
                   "| Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.310–357, moving this chapter's peyyāla to the six "
        "kinds of intention. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.310&ndash;357",
    "title": "Intention Regarding Sights, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of intention"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Seventh of ten categories", "Intention, the mental factor "
         "this chapter's sequence treats as following perception"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of intention regarding "
        "each sense object &mdash; sights, sounds, smells, tastes, "
        "touches, and ideas &mdash; forty-eight further discourses "
        "(AN 11.310&ndash;357)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of intention regarding sense "
            "objects &mdash; sights, sounds, smells, tastes, touches, "
            "and ideas &mdash; the seventh of this chapter's ten "
            "categories."]),
        ("From recognizing to intending", [
            "Where perception (the previous category) simply "
            "recognizes and labels a sense object, intention "
            "(sañcetanā) is the mind's active response to it &mdash; "
            "the volitional movement that, in the canon's broader "
            "analysis, shapes karma itself, since intention is what "
            "the Buddha elsewhere identifies as action (kamma) in its "
            "most fundamental sense."]),
        ("Named for the object, continuing", [
            "Like perception before it, this category names each "
            "intention for its sense object &mdash; &lsquo;intention "
            "regarding sights&rsquo;, not &lsquo;eye "
            "intention&rsquo; &mdash; maintaining the object-based "
            "naming this sequence returned to at AN 11.262&ndash;309."]),
        ("The same forty-eight, continuing", [
            "Six kinds of intention times eight contemplations gives "
            "forty-eight discourses, matching AN 11.310 through AN "
            "11.357 exactly &mdash; the seventh of ten categories to "
            "repeat this chapter's now-familiar arithmetic."]),
    ],
    "terms": [
        ("rūpasañcetanāya, saddasañcetanāya, gandhasañcetanāya, "
         "rasasañcetanāya, phoṭṭhabbasañcetanāya, dhammasañcetanāya",
         "&ldquo;intention regarding sights, sounds, smells, tastes, "
         "touches, and ideas&rdquo; &mdash; the six kinds of "
         "intention, named for their sense objects."),
        ("sañcetanā",
         "&ldquo;intention&rdquo; &mdash; the seventh step in this "
         "chapter's sequence, the mind's active, volitional response "
         "to a recognized sense object."),
        ("kamma",
         "not named directly here, but &ldquo;action&rdquo; itself "
         "&mdash; elsewhere in the canon the Buddha identifies "
         "intention as kamma in its most fundamental sense."),
        ("rūpasañcetanā",
         "&ldquo;intention regarding sights&rdquo; &mdash; the first "
         "of the six, opening this page's list."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of intention. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of intention, the same pattern"),
        ("p", "&sect;1", "an11.310-357:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of perception",
             "The six kinds of intention regarding sense objects",
             "The six kinds of craving",
             "The six kinds of thought"],
         "correct": 1,
         "expl": "The seventh step in this chapter's analytical "
                 "sequence."},
        {"q": "How does intention (sañcetanā) differ from perception, "
              "according to the guide?",
         "opts": [
             "There is no difference",
             "Perception recognizes and labels; intention is the "
             "mind's active, volitional response",
             "Intention comes before perception",
             "Intention is unrelated to the sense objects"],
         "correct": 1,
         "expl": "The shift from recognition to volitional response."},
        {"q": "What does the Buddha elsewhere identify intention "
              "with, according to the guide?",
         "opts": [
             "Nothing significant",
             "Action (kamma) in its most fundamental sense",
             "The five hindrances",
             "The four noble truths"],
         "correct": 1,
         "expl": "A well-known identification from elsewhere in the "
                 "canon."},
        {"q": "How is each of the six intentions named?",
         "opts": [
             "For the sense faculty, like consciousness and contact",
             "For the sense object, like perception before it",
             "Randomly",
             "For the contemplation applied"],
         "correct": 1,
         "expl": "Maintaining the object-based naming from the "
                 "previous category."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "One hundred sixty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.310 through AN 11.357."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("From labeling to acting", [
            "perception just names,",
            "intention moves toward or",
            "away &mdash; the will, stirred",
        ]),
        ("Intention itself is kamma", [
            "not the deed alone,",
            "but the will behind it &mdash;",
            "action, at its root",
        ]),
        ("Named for the object, still", [
            "sights, sounds, smells, and touch,",
            "tastes, and ideas &mdash; the will",
            "toward each, in turn",
        ]),
        ("Cross-references", [
            "AN 11.262&ndash;309 &middot; previous, the six kinds of "
            "perception",
            "AN 11.358&ndash;405 &middot; next, craving for sights",
        ]),
    ],
    "further": [
        '<a href="%s/an11.310-357/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.262-309.html">AN 11.262&ndash;309</a> &mdash; previous.',
        '<a href="an-11.358-405.html">AN 11.358&ndash;405</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.358–405 — craving for sights, etc.
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.358-405",
    "index_pali": "(untitled)",
    "nav_title": "Craving for Sights, Etc.",
    "source": "an11/an11.358-405",
    "crumb": "AN 11.358&ndash;405",
    "meta_title": ("AN 11.358–405 — Craving for Sights, Etc. | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.358–405, moving this chapter's peyyāla to the six "
        "kinds of craving — the link dependent origination names as "
        "feeling's own consequence. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.358&ndash;405",
    "title": "Craving for Sights, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of craving"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Eighth of ten categories, closing the circle", "Craving, "
         "the very link that AN 11.214&ndash;261's feeling was "
         "flagged as conditioning"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of craving for each "
        "sense object &mdash; sights, sounds, smells, tastes, "
        "touches, and ideas &mdash; forty-eight further discourses "
        "(AN 11.358&ndash;405)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of craving &mdash; for "
            "sights, sounds, smells, tastes, touches, and ideas "
            "&mdash; the eighth of this chapter's ten categories."]),
        ("The link this sequence has been building toward", [
            "AN 11.214&ndash;261's guide flagged feeling as the point "
            "where craving takes hold or does not. This page names "
            "that very consequence directly: craving (taṇhā), the "
            "link dependent origination identifies as arising from "
            "feeling and, left unchecked, driving the entire cycle of "
            "further becoming and rebirth."]),
        ("Three kinds of craving, though compressed here", [
            "Elsewhere in the canon craving is analyzed into three "
            "kinds &mdash; for sensual pleasure, for continued "
            "existence, and for non-existence &mdash; a finer "
            "distinction this compressed page does not draw out, "
            "treating craving here simply by its six sense-object "
            "categories rather than by its underlying motivations."]),
        ("The same forty-eight, two categories from the close", [
            "Six kinds of craving times eight contemplations gives "
            "forty-eight discourses, matching AN 11.358 through AN "
            "11.405 exactly &mdash; the eighth of ten categories, "
            "with only thought and consideration remaining before "
            "this chapter's massive mirror page closes the whole "
            "structure."]),
    ],
    "terms": [
        ("rūpataṇhāya, saddataṇhāya, gandhataṇhāya, rasataṇhāya, "
         "phoṭṭhabbataṇhāya, dhammataṇhāya",
         "&ldquo;craving for sights, sounds, smells, tastes, touches, "
         "and ideas&rdquo; &mdash; the six kinds of craving, named "
         "for their sense objects."),
        ("taṇhā",
         "&ldquo;craving&rdquo; &mdash; the eighth step in this "
         "chapter's sequence, and the link dependent origination "
         "identifies as arising directly from feeling."),
        ("rūpataṇhā",
         "&ldquo;craving for sights&rdquo; &mdash; the first of the "
         "six, opening this page's list."),
        ("kāmataṇhā, bhavataṇhā, vibhavataṇhā",
         "&ldquo;craving for sensual pleasure, for continued "
         "existence, for non-existence&rdquo; &mdash; the canon's own "
         "finer threefold analysis of craving, not drawn out in this "
         "compressed page's six-object treatment."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of craving. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of craving, the same pattern"),
        ("p", "&sect;1", "an11.358-405:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of intention",
             "The six kinds of craving — for sights, sounds, smells, "
             "tastes, touches, and ideas",
             "The six kinds of thought",
             "The six kinds of consideration"],
         "correct": 1,
         "expl": "The eighth step in this chapter's analytical "
                 "sequence."},
        {"q": "According to the guide, what earlier page flagged this "
              "category's own significance in advance?",
         "opts": [
             "AN 11.70–117, the sense objects",
             "AN 11.214–261, feeling born of contact",
             "AN 11.22–29, the eye",
             "AN 11.118–165, consciousness"],
         "correct": 1,
         "expl": "Feeling was flagged as the point where craving "
                 "takes hold or does not."},
        {"q": "What threefold analysis of craving does the canon "
              "offer elsewhere, not drawn out in this compressed "
              "page?",
         "opts": [
             "Craving for food, shelter, and companionship",
             "Craving for sensual pleasure, for continued existence, "
             "and for non-existence",
             "Craving for wealth, fame, and power",
             "There is no such analysis"],
         "correct": 1,
         "expl": "A finer distinction this page treats only by sense "
                 "object instead."},
        {"q": "How many categories remain after this one, before the "
              "chapter's closing mirror page, according to the "
              "guide?",
         "opts": [
             "None; this is the last category",
             "Two — thought and consideration",
             "Five", "Eight"],
         "correct": 1,
         "expl": "The eighth of ten categories."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "One hundred sixty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.358 through AN 11.405."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("What feeling gives rise to", [
            "the very craving",
            "flagged pages back &mdash; now named",
            "directly, at last",
        ]),
        ("A finer analysis, elsewhere", [
            "sensual, for being,",
            "for ending &mdash; three kinds unnamed",
            "in this compressed page",
        ]),
        ("Two categories left", [
            "thought and consideration",
            "still to come, then the mirror &mdash;",
            "the structure, nearly closed",
        ]),
        ("Cross-references", [
            "AN 11.310&ndash;357 &middot; previous, the six kinds of "
            "intention",
            "AN 11.214&ndash;261 &middot; where feeling's role in "
            "conditioning this very craving was first flagged",
            "AN 11.406&ndash;453 &middot; next, thoughts about sights",
        ]),
    ],
    "further": [
        '<a href="%s/an11.358-405/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.310-357.html">AN 11.310&ndash;357</a> &mdash; previous.',
        '<a href="an-11.406-453.html">AN 11.406&ndash;453</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.406–453 — thoughts about sights, etc.
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.406-453",
    "index_pali": "(untitled)",
    "nav_title": "Thoughts About Sights, Etc.",
    "source": "an11/an11.406-453",
    "crumb": "AN 11.406&ndash;453",
    "meta_title": ("AN 11.406–453 — Thoughts About Sights, Etc. | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.406–453, moving this chapter's peyyāla to the six "
        "kinds of thought, vitakka. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.406&ndash;453",
    "title": "Thoughts About Sights, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile and eight contemplations, "
                 "now crossed against the six kinds of thought "
                 "(vitakka)"),
        ("Length", "~1 minute to read; stands for forty-eight "
                   "discourses"),
        ("Ninth of ten categories", "Thought (vitakka), the mental "
         "factor familiar from the first absorption's own five "
         "factors"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same established pattern, one category "
                       "over"),
    ],
    "why": (
        "The same eleven-factor cowherd simile and eight "
        "contemplations apply to the six kinds of thought about each "
        "sense object &mdash; sights, sounds, smells, tastes, "
        "touches, and ideas &mdash; forty-eight further discourses "
        "(AN 11.406&ndash;453)."),
    "guide": [
        ("The teaching in one sentence", [
            "The identical cowherd simile and eight contemplations "
            "now apply to the six kinds of thought about sense "
            "objects &mdash; sights, sounds, smells, tastes, touches, "
            "and ideas &mdash; the ninth of this chapter's ten "
            "categories."]),
        ("A familiar term from meditation itself", [
            "Vitakka, translated here as &lsquo;thought&rsquo;, is "
            "the same term naming the first of the first absorption's "
            "five factors &mdash; the initial application of the "
            "mind to an object &mdash; here applied not to a "
            "meditation object specifically but to any of the six "
            "ordinary sense objects a mendicant might think about."]),
        ("The penultimate category", [
            "With thought in place, only consideration (vicāra, "
            "vitakka's own frequent pair in the description of the "
            "first absorption) remains before this chapter's "
            "ten-category cycle through the &lsquo;can't&rsquo; "
            "version completes and the massive mirror page begins."]),
        ("The same forty-eight, nearly through", [
            "Six kinds of thought times eight contemplations gives "
            "forty-eight discourses, matching AN 11.406 through AN "
            "11.453 exactly &mdash; the ninth of ten categories, with "
            "only one more to go before this chapter's structure "
            "turns to its mirror image."]),
    ],
    "terms": [
        ("rūpavitakke, saddavitakke, gandhavitakke, rasavitakke, "
         "phoṭṭhabbavitakke, dhammavitakke",
         "&ldquo;thoughts about sights, sounds, smells, tastes, "
         "touches, and ideas&rdquo; &mdash; the six kinds of thought, "
         "named for their sense objects."),
        ("vitakka",
         "&ldquo;thought&rdquo;, the initial application of the mind "
         "&mdash; the ninth step in this chapter's sequence, and also "
         "the first of the first absorption's five factors elsewhere "
         "in the canon."),
        ("rūpavitakka",
         "&ldquo;thought about sights&rdquo; &mdash; the first of the "
         "six, opening this page's list."),
        ("vicāra",
         "not treated here but named at the very next page, "
         "&ldquo;consideration&rdquo;, vitakka's own frequent "
         "pairing term in describing the first absorption's five "
         "factors."),
        ("aniccānupassī...paṭinissaggānupassī",
         "the same eight contemplations from AN 11.22&ndash;29, again "
         "left entirely implicit."),
    ],
    "text_intro": (
        "The compressed text in full: the same pattern, now applied "
        "to the six kinds of thought. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of thought, the same pattern"),
        ("p", "&sect;1", "an11.406-453:1.1-1.7"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of craving",
             "The six kinds of thought (vitakka) about sense objects",
             "The six kinds of consideration",
             "The six kinds of feeling"],
         "correct": 1,
         "expl": "The ninth step in this chapter's analytical "
                 "sequence."},
        {"q": "Where else does the term vitakka appear in the canon, "
              "according to the guide?",
         "opts": [
             "Nowhere else",
             "As the first of the first absorption's five factors",
             "Only in monastic disciplinary rules",
             "As a synonym for craving"],
         "correct": 1,
         "expl": "The initial application of the mind to an object, "
                 "familiar from jhāna descriptions."},
        {"q": "What category remains after this one, according to "
              "the guide?",
         "opts": [
             "None; this is the last category",
             "Consideration (vicāra), vitakka's own frequent pairing "
             "term",
             "Craving", "Perception"],
         "correct": 1,
         "expl": "The tenth and final category of the ten-part "
                 "sequence."},
        {"q": "How many discourses does this page stand for?",
         "opts": [
             "Eight", "Forty", "Forty-eight", "One hundred sixty"],
         "correct": 2,
         "expl": "6 × 8 = 48, matching AN 11.406 through AN 11.453."},
        {"q": "What is the first kind of thought named in this "
              "page's list?",
         "opts": [
             "Thought about sights", "Thought about ideas",
             "Thought about sounds", "Thought about touches"],
         "correct": 0,
         "expl": "Opening the list in the standard sense-object order."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("The mind's first touch", [
            "vitakka, thought's",
            "initial reach toward an object &mdash;",
            "met again in jhāna",
        ]),
        ("Nine of ten, now done", [
            "one category",
            "left &mdash; consideration, then",
            "the mirror opens",
        ]),
        ("A term from meditation", [
            "the same word that names",
            "the first absorption's own",
            "first factor, applied here",
        ]),
        ("Cross-references", [
            "AN 11.358&ndash;405 &middot; previous, the six kinds of "
            "craving",
            "AN 11.454&ndash;501 &middot; next, considerations, "
            "closing the ten-category cycle",
        ]),
    ],
    "further": [
        '<a href="%s/an11.406-453/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.358-405.html">AN 11.358&ndash;405</a> &mdash; previous.',
        '<a href="an-11.454-501.html">AN 11.454&ndash;501</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.454–501 — considerations regarding sights, etc., closing the
# ten-category "can't" cycle with the eight contemplations spelled out
# a second time
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.454-501",
    "index_pali": "(untitled)",
    "nav_title": "Considerations Regarding Sights, Etc.",
    "source": "an11/an11.454-501",
    "crumb": "AN 11.454&ndash;501",
    "meta_title": ("AN 11.454–501 — Considerations Regarding Sights, "
                   "Etc. | Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.454–501, closing this chapter's ten-category "
        "\"can't\" cycle with the six kinds of consideration and the "
        "eight contemplations spelled out a second time. From Ru-Yi "
        "Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.454&ndash;501",
    "title": "Considerations Regarding Sights, Etc.",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s, closing "
                "the ten-category cycle" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same cowherd simile, now crossed against the "
                 "six kinds of consideration, with the eight "
                 "contemplations spelled out in full a second time"),
        ("Length", "~2 minutes to read; stands for forty-eight "
                   "discourses"),
        ("Closing the cycle, matching the opening", "This page "
         "bookends AN 11.22&ndash;29 by spelling out the eight "
         "contemplations one more time, closing the ten-category "
         "\"can't\" sequence"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the arithmetic and the bookend structure are "
                       "worth holding in mind together"),
    ],
    "why": (
        "The same eleven-factor cowherd simile applies to the six "
        "kinds of consideration regarding each sense object &mdash; "
        "sights, sounds, smells, tastes, touches, and ideas &mdash; "
        "and this page, alone among the nine compressed pages since "
        "AN 11.22&ndash;29, spells out the eight contemplations again "
        "in full, closing this chapter's entire ten-category "
        "&lsquo;can't&rsquo; cycle at exactly AN 11.501."),
    "guide": [
        ("The teaching in one sentence", [
            "The tenth and final category of this chapter's "
            "&lsquo;can't&rsquo; sequence, consideration (vicāra) "
            "regarding each of the six sense objects, closes with the "
            "eight contemplations spelled out one more time, "
            "bookending AN 11.22&ndash;29's own opening full "
            "treatment."]),
        ("A deliberate bookend", [
            "Every one of the eight pages between AN 11.70&ndash;117 "
            "and AN 11.406&ndash;453 compressed its eight "
            "contemplations into a bare ellipsis, trusting the reader "
            "to hold the list in mind from AN 11.22&ndash;29. This "
            "page breaks that pattern deliberately, naming all eight "
            "&mdash; impermanence, suffering, not-self, ending, "
            "vanishing, fading away, cessation, letting go &mdash; "
            "one final time as this immense compressed structure "
            "closes."]),
        ("Vitakka's frequent partner", [
            "Consideration (vicāra) is the sustained application of "
            "the mind that, together with the previous page's thought "
            "(vitakka), forms two of the first absorption's five "
            "factors &mdash; initial and sustained attention, here "
            "applied to ordinary sense objects rather than a "
            "meditation subject."]),
        ("The full arithmetic of the ten-category cycle", [
            "Ten categories &mdash; six sense faculties, six sense "
            "objects, six consciousnesses, six contacts, six "
            "feelings, six perceptions, six intentions, six cravings, "
            "six thoughts, six considerations &mdash; each times "
            "eight contemplations, gives 480 discourses total, "
            "exactly matching AN 11.22 through AN 11.501. What "
            "follows next mirrors this entire structure as its "
            "positive counterpart, in a single further page."]),
    ],
    "terms": [
        ("rūpavicāre, saddavicāre, gandhavicāre, rasavicāre, "
         "phoṭṭhabbavicāre, dhammavicāre",
         "&ldquo;considerations regarding sights, sounds, smells, "
         "tastes, touches, and ideas&rdquo; &mdash; the six kinds of "
         "consideration, named for their sense objects, closing the "
         "ten-category cycle."),
        ("vicāra",
         "&ldquo;consideration&rdquo;, sustained attention &mdash; "
         "the tenth and final step in this chapter's sequence, "
         "vitakka's own frequent partner in the first absorption's "
         "five factors."),
        ("aniccānupassī",
         "&ldquo;observing impermanence&rdquo; &mdash; the first "
         "of the eight contemplations, spelled out here for the "
         "second and final time in this chapter."),
        ("paṭinissaggānupassī",
         "&ldquo;observing letting go&rdquo; &mdash; the eighth and "
         "final contemplation, closing both this page and the entire "
         "480-discourse \"can't\" cycle it completes."),
        ("dhammavicāra",
         "&ldquo;consideration regarding ideas&rdquo; &mdash; the "
         "sixth and final of the six considerations, completing the "
         "list before the eight contemplations are spelled out."),
    ],
    "text_intro": (
        "The compressed text in full: the six kinds of consideration, "
        "then all eight contemplations spelled out once more, closing "
        "the ten-category cycle. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    "text": [
        ("h3", "Six kinds of consideration"),
        ("p", "&sect;1", "an11.454-501:1.1-1.6"),
        ("h3", "Eight contemplations, spelled out a second time"),
        ("p", "&sect;2", "an11.454-501:1.7-1.14"),
    ],
    "quiz": [
        {"q": "What category does this page address?",
         "opts": [
             "The six kinds of thought (vitakka)",
             "The six kinds of consideration (vicāra) regarding "
             "sense objects",
             "The six kinds of craving",
             "The six sense faculties"],
         "correct": 1,
         "expl": "The tenth and final category in this chapter's "
                 "\"can't\" cycle."},
        {"q": "What makes this page different from the eight pages "
              "immediately before it, according to the guide?",
         "opts": [
             "Nothing; it is equally compressed",
             "It spells out the eight contemplations in full a "
             "second time, rather than compressing them with an "
             "ellipsis",
             "It removes the cowherd simile",
             "It introduces a ninth contemplation"],
         "correct": 1,
         "expl": "Bookending AN 11.22–29's own opening full treatment."},
        {"q": "What is vicāra's frequent partner in describing the "
              "first absorption's five factors?",
         "opts": [
             "Rapture (pīti)",
             "Thought (vitakka), from the previous page",
             "Immersion (samādhi)",
             "Equanimity (upekkhā)"],
         "correct": 1,
         "expl": "Initial and sustained attention, named consecutively "
                 "across these two pages."},
        {"q": "What is the full arithmetic of this chapter's entire "
              "ten-category \"can't\" cycle, according to the guide?",
         "opts": [
             "48 discourses total",
             "Ten categories × six items × eight contemplations = "
             "480 discourses, matching AN 11.22 through AN 11.501",
             "160 discourses total",
             "1,151 discourses total"],
         "correct": 1,
         "expl": "The full scope of the structure this page closes."},
        {"q": "What comes immediately after this page, according to "
              "the guide?",
         "opts": [
             "The Rāgapeyyāla directly",
             "A single further page mirroring this entire structure "
             "as its positive counterpart",
             "Nothing; the chapter ends here",
             "A return to chapter 2's content"],
         "correct": 1,
         "expl": "AN 11.502–981, the massive mirror page."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, in the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("The cycle's own bookend", [
            "eight ways, spelled out",
            "once at the start, once again",
            "here, closing the loop",
        ]),
        ("Vitakka's steady partner", [
            "thought applies itself,",
            "consideration sustains it &mdash;",
            "two factors, paired here",
        ]),
        ("Four hundred eighty", [
            "ten times six times eight &mdash;",
            "the whole \"can't\" cycle, complete",
            "at eleven fifty-one",
        ]),
        ("Cross-references", [
            "AN 11.22&ndash;29 &middot; the opening page this one "
            "bookends, spelling out the same eight contemplations",
            "AN 11.406&ndash;453 &middot; previous, the six kinds of "
            "thought",
            "AN 11.502&ndash;981 &middot; next, the entire structure "
            "mirrored as its positive counterpart",
        ]),
    ],
    "further": [
        '<a href="%s/an11.454-501/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.406-453.html">AN 11.406&ndash;453</a> &mdash; previous.',
        '<a href="an-11.502-981.html">AN 11.502&ndash;981</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.502–981 — the entire ten-category structure mirrored as its
# positive ("can") counterpart, compressed onto a single page
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.502-981",
    "index_pali": "(untitled)",
    "nav_title": "The Mirror: Can, Not Can't",
    "source": "an11/an11.502-981",
    "crumb": "AN 11.502&ndash;981",
    "meta_title": ("AN 11.502–981 — The Mirror: Can, Not Can't | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.502–981, closing this chapter's peyyāla by mirroring "
        "its entire 480-discourse \"can't\" cycle as its positive "
        "counterpart on a single page. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.502&ndash;981",
    "title": "The Mirror: Can, Not Can't",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s, closing "
                "the chapter" % VAGGA_3),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The entire ten-category, eight-contemplation "
                 "structure from AN 11.22&ndash;501, flipped from "
                 "\"can't\" to \"can\", compressed onto a single "
                 "page representing only the eye"),
        ("Length", "~1 minute to read; stands for 480 discourses, "
                   "the largest ratio of text to discourse count in "
                   "this entire project"),
        ("Closing this chapter", "This page closes Sāmaññavagga and "
         "the 960-discourse peyyāla it opened at AN 11.22"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the text itself is brief; holding the full "
                       "480-discourse multiplication in mind is the "
                       "real work"),
    ],
    "why": (
        "Everything just established across AN 11.22&ndash;501 "
        "&mdash; the eleven-factor cowherd simile and eight "
        "contemplations, crossed against ten categories of six items "
        "each &mdash; is restated here in its positive form: a "
        "cowherd <em>with</em> eleven skilful factors <em>can</em> "
        "maintain a herd, and a mendicant with the same eleven "
        "qualities <em>can</em> meditate observing all eight "
        "contemplations, across all ten categories, closing this "
        "chapter's entire 960-discourse peyyāla at AN 11.981."),
    "guide": [
        ("The teaching in one sentence", [
            "The mirror image of everything AN 11.22&ndash;501 "
            "established: a cowherd with eleven skilful factors can "
            "maintain a herd, and a mendicant with the same eleven "
            "qualities can meditate observing impermanence, "
            "suffering, not-self, ending, vanishing, fading away, "
            "cessation, and letting go, across all ten categories "
            "this chapter has built."]),
        ("The most compressed page in this entire project", [
            "Where the &lsquo;can't&rsquo; cycle took nine full pages "
            "just for its middle compressed categories, this page "
            "represents the identical 480-discourse mirror &mdash; "
            "every one of the same ten categories, flipped positive "
            "&mdash; using only ten short segments, naming just the "
            "eye as a single representative example before trailing "
            "into an unexpanded &lsquo;pe&rsquo; ellipsis for "
            "everything else."]),
        ("Why the source itself is this brief", [
            "Having spent nearly five hundred discourses "
            "establishing every category and every contemplation in "
            "full negative form, the source text trusts its reader "
            "entirely: reversing &lsquo;can't&rsquo; to "
            "&lsquo;can&rsquo; and &lsquo;doesn't know form&rsquo; to "
            "&lsquo;knows form&rsquo; requires no further "
            "elaboration, since every other term in the structure "
            "carries over unchanged from what came before."]),
        ("The complete arithmetic, and this chapter's own close", [
            "480 discourses (the mirror) plus 480 discourses (the "
            "original &lsquo;can't&rsquo; cycle, AN 11.22&ndash;501) "
            "totals exactly 960, matching this chapter's full span "
            "from AN 11.22 through AN 11.981 &mdash; closing "
            "Sāmaññavagga, the chapter this page and its eleven "
            "predecessors have built. What remains in this nipāta is "
            "only the Rāgapeyyāla, AN 11.982&ndash;1151, and with it "
            "the entire Aṅguttara Nikāya."]),
    ],
    "terms": [
        ("bhabbo",
         "&ldquo;can&rdquo;, capable &mdash; the single word this "
         "page flips from AN 11.22&ndash;501's repeated "
         "&lsquo;abhabbo&rsquo;, &ldquo;can't&rdquo;, reversing the "
         "entire structure's polarity."),
        ("rūpaññū hoti",
         "&ldquo;knows form&rdquo; &mdash; the positive mirror of AN "
         "11.17's &lsquo;na rūpaññū hoti&rsquo;, &ldquo;doesn't know "
         "form&rdquo;, the cowherd's first skill restated "
         "affirmatively."),
        ("cakkhusmiṁ aniccānupassī viharituṁ",
         "&ldquo;meditate observing impermanence in the eye&rdquo; "
         "&mdash; the same phrase from AN 11.22, now following "
         "&lsquo;can&rsquo; rather than &lsquo;can't&rsquo;."),
        ("pe",
         "the Pāli ellipsis marker, here doing the heaviest work in "
         "this entire project: standing in for the other nine "
         "categories and all six items each, none of them spelled "
         "out even once on this page."),
        ("Sāmaññavaggo",
         "&ldquo;the chapter on similarity&rdquo; &mdash; not stated "
         "as an explicit colophon on this page in the source, unlike "
         "chapters 1 and 2's own closing formulas, but the chapter "
         "this page nonetheless closes."),
    ],
    "text_intro": (
        "The compressed text in full: the cowherd simile's positive "
        "form, and the eye standing for all ten categories. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "The cowherd simile, reversed to the positive"),
        ("p", "&sect;1", "an11.502-981:1.1-2.3"),
    ],
    "quiz": [
        {"q": "What does this page do to the entire structure built "
              "across AN 11.22–501?",
         "opts": [
             "Repeats it unchanged",
             "Mirrors it as its positive counterpart, flipping "
             "\"can't\" to \"can\"",
             "Contradicts and rejects it",
             "Ignores it and introduces new content"],
         "correct": 1,
         "expl": "A cowherd WITH the eleven factors can maintain a "
                 "herd; a mendicant with the same eleven qualities "
                 "can meditate observing all eight contemplations."},
        {"q": "How many discourses does this single page stand for?",
         "opts": [
             "Forty-eight", "One hundred sixty",
             "480, mirroring the entire \"can't\" cycle",
             "Only one"],
         "correct": 2,
         "expl": "The largest ratio of text to discourse count in "
                 "this entire project."},
        {"q": "How does this page represent all ten categories, "
              "according to the guide?",
         "opts": [
             "By spelling out each one in full, as AN 11.454–501 did",
             "By naming only the eye as a single representative "
             "example, then trailing into an unexpanded ellipsis",
             "By listing all ten in a table",
             "It does not represent all ten; it covers only the eye"],
         "correct": 1,
         "expl": "The most compressed page in the entire project."},
        {"q": "What is the full arithmetic this page's guide gives "
              "for the whole chapter?",
         "opts": [
             "480 discourses total",
             "480 (mirror) plus 480 (\"can't\" cycle) equals 960, "
             "matching AN 11.22 through AN 11.981",
             "1,151 discourses total",
             "36 discourses total"],
         "correct": 1,
         "expl": "Closing Sāmaññavagga, the chapter these twelve "
                 "pages have built."},
        {"q": "What remains in this nipāta after this page, according "
              "to the guide?",
         "opts": [
             "Nothing; the nipāta ends here",
             "Only the Rāgapeyyāla, AN 11.982–1151, closing the "
             "entire Aṅguttara Nikāya",
             "Three more full chapters",
             "A return to chapter 1's content"],
         "correct": 1,
         "expl": "The final structure remaining before this project's "
                 "own completion."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Can, not can't", [
            "one word reversed, and",
            "the whole four hundred eighty",
            "flips to the positive",
        ]),
        ("The eye stands for all", [
            "just one sense named here,",
            "nine more categories left",
            "to a bare \"etc.\"",
        ]),
        ("Nine hundred sixty", [
            "can't plus can, both full &mdash;",
            "one chapter's entire span,",
            "closed on this one page",
        ]),
        ("Cross-references", [
            "AN 11.22&ndash;29 &middot; the chapter's opening page, "
            "spelling out the \"can't\" version this page mirrors",
            "AN 11.454&ndash;501 &middot; previous, closing the "
            "\"can't\" cycle",
            "AN 11.982&ndash;1151 &middot; next, the Rāgapeyyāla, "
            "closing the entire Aṅguttara Nikāya",
        ]),
    ],
    "further": [
        '<a href="%s/an11.502-981/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.454-501.html">AN 11.454&ndash;501</a> &mdash; previous.',
        '<a href="an-11.982.html">AN 11.982</a> &mdash; next, opening the Rāgapeyyāla.',
    ],
})


VAGGA_4 = ("<em>Rāgapeyyāla</em> &mdash; the abbreviated texts beginning "
          "with greed, closing this nipāta")
ELEVEN_ATTAINMENTS = (
    "the four absorptions, the four divine abodes of love, compassion, "
    "rejoicing, and equanimity, and the three lower formless "
    "attainments")


# --------------------------------------------------------------------------- #
# AN 11.982 — opening the Rāgapeyyāla: insight into greed
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.982",
    "index_pali": "(untitled)",
    "nav_title": "For Insight Into Greed",
    "source": "an11/an11.982",
    "crumb": "AN 11.982",
    "meta_title": ("AN 11.982 — For Insight Into Greed | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.982, opening this nipāta's closing Rāgapeyyāla with "
        "the eleven things to be developed for insight into greed — "
        "the same fixed list already met at AN 11.16. From Ru-Yi "
        "Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourse 11.982",
    "title": "For Insight Into Greed",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_4),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eleven things that should be developed for insight "
                 "into greed, named in full"),
        ("Length", "~1 minute to read; a single discourse"),
        ("Opening this nipāta's final structure", "This page opens "
         "the Rāgapeyyāla, the last of the two peyyāla this project "
         "has met bearing this name (the other closed AN 9 and AN "
         "10)"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "short, concrete list, easy to hold in mind"),
    ],
    "why": (
        "For insight into greed, eleven things should be developed: "
        "the four absorptions, the four divine abodes of love, "
        "compassion, rejoicing, and equanimity, and the dimensions of "
        "infinite space, infinite consciousness, and nothingness "
        "&mdash; the same eleven-item list already met in full at AN "
        "11.16, now opening this nipāta's own closing peyyāla."),
    "guide": [
        ("The teaching in one sentence", [
            "Eleven meditative attainments &mdash; the four "
            "absorptions, the four divine abodes, and the three lower "
            "formless dimensions &mdash; should be developed for "
            "insight (abhiññā) into greed, opening a peyyāla that "
            "will apply the same list, crossed against ten verbs and "
            "seventeen defilements, all the way to the close of this "
            "entire project."]),
        ("A list already met, now put to new work", [
            "This same eleven-item list &mdash; %s &mdash; was "
            "already met in full at AN 11.16, there framed as doors "
            "to the deathless, each seen through as impermanent once "
            "attained. Here, the framing shifts: the same eleven "
            "things are simply what should be developed &lsquo;for "
            "insight into greed&rsquo;, without repeating the earlier "
            "discourse's reflection on impermanence at all." %
            ELEVEN_ATTAINMENTS]),
        ("A second Rāgapeyyāla in this project", [
            "This is the second peyyāla in this project to bear the "
            "name Rāgapeyyāla, &lsquo;abbreviated texts beginning with "
            "greed&rsquo;: the first closed the Book of the Nines at "
            "AN 9.113&ndash;432 and the Book of the Tens at AN "
            "10.237&ndash;746, both built from sixteen defilements "
            "crossed against ten verbs and either two or three "
            "ten-item lists. This one, closing the Book of the "
            "Elevens, uses a single fixed eleven-item list instead "
            "&mdash; simpler in structure, though the underlying "
            "seventeen-defilement roster (adding greed itself to the "
            "familiar sixteen) is unchanged."]),
        ("What this single discourse opens", [
            "AN 11.982 covers only the first of ten verbs (insight, "
            "abhiññā) applied to greed alone. The next page supplies "
            "greed's remaining nine verbs, and the page after that "
            "extends the full ten-verb treatment to the sixteen "
            "further defilements already familiar from this "
            "project's two earlier Rāgapeyyāla, closing not only this "
            "nipāta but the entire 1,408-discourse project."]),
    ],
    "terms": [
        ("rāgassa abhiññāya",
         "&ldquo;for insight into greed&rdquo; &mdash; this "
         "discourse's own opening phrase, naming both its subject and "
         "the first of ten verbs this peyyāla will apply throughout."),
        ("cattāri jhānāni",
         "&ldquo;the four absorptions&rdquo; &mdash; the first four "
         "of the eleven things to be developed."),
        ("mettācetovimutti, karuṇācetovimutti, muditācetovimutti, "
         "upekkhācetovimutti",
         "&ldquo;the heart's releases by love, compassion, rejoicing, "
         "and equanimity&rdquo; &mdash; the four divine abodes, "
         "items five through eight."),
        ("ākāsānañcāyatana, viññāṇañcāyatana, ākiñcaññāyatana",
         "&ldquo;the dimensions of infinite space, infinite "
         "consciousness, and nothingness&rdquo; &mdash; the three "
         "lower formless attainments, items nine through eleven, "
         "stopping short of neither-perception-nor-non-perception."),
        ("Rāgapeyyāla",
         "&ldquo;abbreviated texts beginning with greed&rdquo; "
         "&mdash; this section's own name in the source, shared with "
         "the two earlier peyyāla of the same name closing AN 9 and "
         "AN 10."),
    ],
    "text_intro": (
        "The discourse in full: eleven things to be developed for "
        "insight into greed. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    "text": [
        ("h3", "Eleven things, for insight into greed"),
        ("p", "&sect;1", "an11.982:1.1-1.4"),
    ],
    "quiz": [
        {"q": "What eleven things does this discourse say should be "
              "developed for insight into greed?",
         "opts": [
             "The noble eightfold path and three additional factors",
             "The four absorptions, the four divine abodes, and the "
             "three lower formless attainments",
             "The five hindrances and six sense bases",
             "Ten verbs and one defilement"],
         "correct": 1,
         "expl": "The same fixed list already met in full at AN "
                 "11.16."},
        {"q": "Where did this project first meet this identical "
              "eleven-item list?",
         "opts": [
             "AN 11.9, the thoroughbred simile",
             "AN 11.16, the eleven doors to the deathless",
             "AN 11.17, the cowherd simile",
             "AN 9.113–432"],
         "correct": 1,
         "expl": "There framed as doors to the deathless; here, as "
                 "developments for insight into greed."},
        {"q": "How many Rāgapeyyāla has this project now met, "
              "including this one?",
         "opts": [
             "Just this one", "Two, closing the Nines and the Tens",
             "Three, including this one closing the Elevens",
             "Four"],
         "correct": 2,
         "expl": "AN 9.113–432, AN 10.237–746, and now this one "
                 "closing AN 11."},
        {"q": "How does this Rāgapeyyāla's underlying list structure "
              "differ from the earlier two, according to the guide?",
         "opts": [
             "It is identical in every respect",
             "It uses a single fixed eleven-item list, rather than "
             "two or three ten-item lists",
             "It has no fixed list at all",
             "It uses twenty items instead of eleven"],
         "correct": 1,
         "expl": "Simpler in structure, though the seventeen-"
                 "defilement roster carries over unchanged."},
        {"q": "What does this single discourse cover, according to "
              "the guide?",
         "opts": [
             "All ten verbs applied to all seventeen defilements",
             "Only the first of ten verbs (insight) applied to greed "
             "alone",
             "Nothing related to greed",
             "The entire Rāgapeyyāla in one page"],
         "correct": 1,
         "expl": "The next page supplies greed's remaining nine "
                 "verbs."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, in the little village of Beluva"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Eleven things, one purpose", [
            "four jhānas, four hearts "
            "released, three formless states",
            "&mdash; all for seeing greed",
        ]),
        ("A list met once before", [
            "the same eleven",
            "that opened doors to no-death &mdash;",
            "now applied to greed",
        ]),
        ("A third Rāgapeyyāla", [
            "the Nines, the Tens, and",
            "now the Elevens &mdash; greed's own",
            "name, closing each book",
        ]),
        ("Cross-references", [
            "AN 11.16 &middot; the eleven-item list's first full "
            "telling, as doors to the deathless",
            "AN 9.113&ndash;432, AN 10.237&ndash;746 &middot; the "
            "earlier two Rāgapeyyāla",
            "AN 11.502&ndash;981 &middot; previous, closing chapter 3",
        ]),
    ],
    "further": [
        '<a href="%s/an11.982/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.502-981.html">AN 11.502&ndash;981</a> &mdash; previous.',
        '<a href="an-11.983-991.html">AN 11.983&ndash;991</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.983–991 — greed's remaining nine verbs
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.983-991",
    "index_pali": "(untitled)",
    "nav_title": "Greed's Remaining Nine Verbs",
    "source": "an11/an11.983-991",
    "crumb": "AN 11.983&ndash;991",
    "meta_title": ("AN 11.983–991 — Greed's Remaining Nine Verbs | "
                   "Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "AN 11.983–991, completing greed's own ten-verb treatment in "
        "this nipāta's closing Rāgapeyyāla. From Ru-Yi Meditation "
        "Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.983&ndash;991",
    "title": "Greed's Remaining Nine Verbs",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s" % VAGGA_4),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same eleven things from AN 11.982, now "
                 "developed for nine further verbs applied to greed"),
        ("Length", "~1 minute to read; stands for nine discourses"),
        ("Completing greed's own treatment", "Together with AN "
         "11.982, this page completes the full ten-verb pattern for "
         "greed that the next page will apply to sixteen further "
         "defilements"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "nine verbs, compressed but individually "
                       "distinct"),
    ],
    "why": (
        "The same eleven things already named for insight into greed "
        "at AN 11.982 should likewise be developed for greed's "
        "complete understanding, complete ending, giving up, ending, "
        "vanishing, fading away, cessation, giving away, and letting "
        "go &mdash; nine further discourses (AN 11.983&ndash;991), "
        "completing greed's own ten-verb treatment."),
    "guide": [
        ("The teaching in one sentence", [
            "The same eleven attainments from AN 11.982 apply "
            "identically to nine further verbs regarding greed "
            "&mdash; complete understanding, complete ending, giving "
            "up, ending, vanishing, fading away, cessation, giving "
            "away, and letting go &mdash; completing the full "
            "ten-verb pattern this Rāgapeyyāla will apply to every "
            "remaining defilement."]),
        ("Ten verbs, the same set met twice before", [
            "Insight (abhiññā, AN 11.982) plus these nine gives the "
            "identical ten-verb sequence already met at both earlier "
            "Rāgapeyyāla in this project (AN 9.113&ndash;432 and AN "
            "10.237&ndash;746): complete understanding, complete "
            "ending, giving up, ending, vanishing, fading away, "
            "cessation, giving away, and letting go, always in this "
            "same order."]),
        ("Why greed gets two pages, not one", [
            "Greed alone receives its own dedicated ten-discourse "
            "treatment across this page and the last (AN "
            "11.982&ndash;991) before the next page compresses "
            "sixteen further defilements into a single further page "
            "&mdash; mirroring exactly how both earlier Rāgapeyyāla "
            "singled out greed for individual treatment before "
            "folding the remaining defilements into denser compressed "
            "form."]),
        ("The arithmetic so far", [
            "One discourse for insight (AN 11.982) plus nine more for "
            "the remaining verbs (this page) gives exactly ten "
            "discourses for greed, matching AN 11.982 through AN "
            "11.991 &mdash; the first tenth of this Rāgapeyyāla's full "
            "170-discourse span."]),
    ],
    "terms": [
        ("pariññāya",
         "&ldquo;for the complete understanding&rdquo; &mdash; the "
         "second verb, opening this page's list."),
        ("parikkhayāya",
         "&ldquo;complete ending&rdquo; &mdash; the third verb, "
         "distinct from the plain &lsquo;ending&rsquo; (khaya) that "
         "follows later in the sequence."),
        ("pahānāya",
         "&ldquo;giving up&rdquo; &mdash; the fourth verb, familiar "
         "from this project's many earlier discourses on abandoning "
         "unskillful qualities."),
        ("cāgāya",
         "&ldquo;giving away&rdquo; &mdash; the ninth verb, distinct "
         "from the tenth and final &lsquo;letting go&rsquo; "
         "(paṭinissagga) that closes the sequence."),
        ("paṭinissaggāya",
         "&ldquo;letting go&rdquo; &mdash; the tenth and final verb, "
         "closing greed's own ten-verb treatment across this page and "
         "AN 11.982."),
    ],
    "text_intro": (
        "The compressed text in full: nine further verbs applied to "
        "greed, completing its ten-verb treatment. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "Nine further verbs, applied to greed"),
        ("p", "&sect;1", "an11.983-991:1.1-1.10"),
    ],
    "quiz": [
        {"q": "What does this page add to AN 11.982's treatment of "
              "greed?",
         "opts": [
             "A twelfth attainment",
             "Nine further verbs, completing the full ten-verb "
             "pattern",
             "An entirely new eleven-item list",
             "Nothing; it repeats AN 11.982 exactly"],
         "correct": 1,
         "expl": "Insight plus these nine verbs gives the complete "
                 "ten-verb sequence."},
        {"q": "Where has this project already met this identical "
              "ten-verb sequence?",
         "opts": [
             "Nowhere else",
             "Both earlier Rāgapeyyāla, at AN 9.113–432 and AN "
             "10.237–746",
             "Only at AN 11.16",
             "Only in chapter 1 of this nipāta"],
         "correct": 1,
         "expl": "The same ten verbs, always in the same order."},
        {"q": "According to the guide, why does greed receive its own "
              "dedicated two-page treatment?",
         "opts": [
             "By accident of the source text",
             "Mirroring exactly how both earlier Rāgapeyyāla singled "
             "out greed before compressing the remaining defilements",
             "Greed is considered less important than other "
             "defilements",
             "There is no reason given"],
         "correct": 1,
         "expl": "A consistent structural choice across all three "
                 "Rāgapeyyāla in this project."},
        {"q": "What is the tenth and final verb, closing greed's own "
              "treatment?",
         "opts": [
             "Complete understanding",
             "Letting go (paṭinissagga)",
             "Giving up",
             "Insight"],
         "correct": 1,
         "expl": "Closing the sequence across this page and AN 11.982."},
        {"q": "What fraction of this Rāgapeyyāla's full span does "
              "greed's own ten-discourse treatment represent, "
              "according to the guide?",
         "opts": [
             "The entire span",
             "The first tenth (10 of 170 discourses)",
             "Half the span",
             "None of it"],
         "correct": 1,
         "expl": "AN 11.982 through AN 11.991, out of AN 11.982 "
                 "through AN 11.1151."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "No setting is stated in the source",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("Nine more verbs", [
            "understanding, end,",
            "giving up, ending, vanishing,",
            "fading, ceasing, gone",
        ]),
        ("Ten verbs, met twice before", [
            "the same sequence that",
            "closed the Nines, closed the Tens &mdash;",
            "now closing greed here",
        ]),
        ("Greed, given its due", [
            "two full pages, ten",
            "discourses, before the rest",
            "compress into one",
        ]),
        ("Cross-references", [
            "AN 11.982 &middot; previous, the first verb, insight",
            "AN 9.113&ndash;432, AN 10.237&ndash;746 &middot; the "
            "same ten-verb sequence in this project's two earlier "
            "Rāgapeyyāla",
            "AN 11.992&ndash;1151 &middot; next, sixteen further "
            "defilements, closing the entire Aṅguttara Nikāya",
        ]),
    ],
    "further": [
        '<a href="%s/an11.983-991/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.982.html">AN 11.982</a> &mdash; previous.',
        '<a href="an-11.992-1151.html">AN 11.992&ndash;1151</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 11.992–1151 — sixteen further defilements, ten verbs each,
# closing this chapter, this nipāta, and the entire Aṅguttara Nikāya
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-11.992-1151",
    "index_pali": "(untitled)",
    "nav_title": "Hate, Etc., Closing the Aṅguttara Nikāya",
    "source": "an11/an11.992-1151",
    "crumb": "AN 11.992&ndash;1151",
    "meta_title": ("AN 11.992–1151 — Hate, Etc. — Closing the "
                   "Aṅguttara Nikāya | Ru-Yi Meditation Center"),
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "the final page of this entire project — sixteen further "
        "defilements crossed against ten verbs, completing the "
        "Rāgapeyyāla and closing the Book of the Elevens and the "
        "whole Aṅguttara Nikāya at once. From Ru-Yi Meditation "
        "Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 11.992&ndash;1151",
    "title": "Hate, Etc., Closing the Aṅguttara Nikāya",
    "subtitle": ("<em>Untitled in the source</em> &mdash; %s, closing "
                "the entire nipāta and this project" % VAGGA_4),
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Sixteen further defilements, each crossed against "
                 "the same ten verbs and the same eleven-item list "
                 "already established for greed"),
        ("Length", "~2 minutes to read the compressed text; the full "
                   "160-discourse expansion would take many hours"),
        ("Closing this entire project", "This page closes the "
         "Rāgapeyyāla, chapter 3, the Book of the Elevens, and this "
         "1,408-discourse Aṅguttara Nikāya completion project all at "
         "once, with the source's own final colophon"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the compressed text is brief; understanding "
                       "what it stands for, and what it closes, "
                       "requires holding this entire project in mind"),
    ],
    "why": (
        "This single page stands for 160 discourses (AN "
        "11.992&ndash;1151), the sixteen further defilements &mdash; "
        "hate through negligence, the identical sixteen-item list "
        "already met at AN 9.113&ndash;432 and AN 10.267&ndash;746 "
        "&mdash; each crossed against the same ten verbs and the same "
        "eleven-item list established for greed, closing this "
        "chapter, this nipāta, and this entire project."),
    "guide": [
        ("The teaching in one sentence", [
            "Each of the sixteen remaining defilements &mdash; hate, "
            "delusion, anger, acrimony, disdain, contempt, jealousy, "
            "stinginess, deceitfulness, deviousness, obstinacy, "
            "aggression, conceit, arrogance, vanity, and negligence "
            "&mdash; should likewise be met by developing the same "
            "eleven things for insight, complete understanding, "
            "complete ending, giving up, ending, vanishing, fading "
            "away, cessation, giving away, and letting go of each "
            "defilement in turn."]),
        ("The same sixteen-item list, met a third time", [
            "Hate, delusion, anger, acrimony, disdain, contempt, "
            "jealousy, stinginess, deceitfulness, deviousness, "
            "obstinacy, aggression, conceit, arrogance, vanity, and "
            "negligence are the identical sixteen items, in the "
            "identical order, that closed both AN 9.113&ndash;432 and "
            "AN 10.267&ndash;746 &mdash; the same defilement list, now "
            "recurring a third and final time to close the Elevens as "
            "it once closed the Nines and the Tens."]),
        ("The arithmetic, and this project's own final closure", [
            "16 defilements &times; 10 verbs &times; 1 eleven-item "
            "list = 160, plus the 10 discourses already given for "
            "greed itself (AN 11.982&ndash;991), totals exactly 170, "
            "matching the discourse range AN 11.982 through AN "
            "11.1151 &mdash; and with this page, all 1,151 AN11 "
            "discourses, and with them this entire project's "
            "translation of all 1,408 discourses across AN 1 through "
            "AN 11, are complete."]),
        ("A colophon closing four things at once, and translated in "
         "full this time", [
            "This page's own closing lines mark a fourfold closure, "
            "and unlike this project's two earlier Rāgapeyyāla, whose "
            "final nipāta-closing lines were left untranslated in the "
            "English source, this time both closing declarations are "
            "given in English: first the standard formula "
            "&lsquo;that is what the Buddha said; satisfied, the "
            "mendicants approved&rsquo;, then (after the untranslated "
            "&lsquo;Rāgapeyyālaṁ niṭṭhitaṁ&rsquo; and a traditional "
            "recitation-count verse) the source's own words, quoted "
            "here directly: &lsquo;The Book of the Elevens is "
            "finished. The Numbered Discourses are completed.&rsquo; "
            "&mdash; not just this chapter, not just this nipāta, but "
            "the entire Aṅguttara Nikāya, and with it this project's "
            "full translation of all 1,408 discourses it set out to "
            "cover."]),
    ],
    "terms": [
        ("dosassa, mohassa, kodhassa",
         "&ldquo;hate, delusion, anger&rdquo; &mdash; the first three "
         "of the sixteen defilements opening this compressed range, "
         "the same standard list met at both this project's earlier "
         "Rāgapeyyāla."),
        ("upanāhassa, makkhassa, paḷāsassa, issāya, macchariyassa",
         "&ldquo;acrimony, disdain, contempt, jealousy, "
         "stinginess&rdquo; &mdash; five further defilements, matching "
         "the identical list and order already established at AN "
         "3.183&ndash;352 and repeated at every nipāta-closing "
         "peyyāla since."),
        ("pamādassa",
         "&ldquo;of negligence&rdquo; &mdash; the sixteenth and final "
         "defilement, given its own full ten-verb treatment before "
         "this page's own closing lines."),
        ("ime ekādasa dhammā bhāvetabbā",
         "&ldquo;these eleven things should be developed&rdquo; "
         "&mdash; the shared closing formula, repeated for each "
         "defilement crossed against each of the ten verbs."),
        ("Ekādasakanipātapāḷi niṭṭhitā. Aṅguttaranikāyo samatto.",
         "&ldquo;the Book of the Elevens is finished. The Numbered "
         "Discourses are completed.&rdquo; &mdash; the source's own "
         "final declaration, quoted here directly, closing this "
         "entire nipāta and, with it, this project's full translation "
         "of all 1,408 discourses across AN 1 through AN 11."),
    ],
    "text_intro": (
        "The compressed text in full: sixteen defilements crossed "
        "against ten verbs, then the discourse's own close and this "
        "project's final colophon, quoted directly. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "Sixteen defilements, ten verbs, compressed"),
        ("p", "&sect;1", "an11.992-1151:1.1-1.25"),
        ("h3", "The discourse ends, and the entire collection with it"),
        ("p", "&sect;2", "an11.992-1151:2.1-3.6"),
    ],
    "quiz": [
        {"q": "What does this compressed page stand for?",
         "opts": [
             "A single new discourse",
             "160 individually numbered discourses, produced by "
             "crossing sixteen further defilements against ten verbs "
             "and the eleven-item list",
             "A biography of a named disciple",
             "A monastic disciplinary case"],
         "correct": 1,
         "expl": "16 defilements × 10 verbs = 160, completing this "
                 "Rāgapeyyāla's full 170-discourse structure alongside "
                 "greed's own 10."},
        {"q": "According to the guide, what is significant about the "
              "sixteen-item defilement list this page uses?",
         "opts": [
             "It is entirely new vocabulary invented for this page",
             "It is the identical sixteen-item list, in the identical "
             "order, that closed both AN 9.113–432 and AN "
             "10.267–746",
             "It has no relation to any earlier discourse",
             "It differs completely from every earlier defilement "
             "list"],
         "correct": 1,
         "expl": "The same defilement list, now recurring a third and "
                 "final time."},
        {"q": "How does this page's own closing colophon differ from "
              "this project's two earlier Rāgapeyyāla, according to "
              "the guide?",
         "opts": [
             "It is identical, entirely untranslated",
             "Its final nipāta-closing declaration is given in "
             "English and quoted directly, unlike the earlier two",
             "It has no colophon at all",
             "It closes only this single page, nothing more"],
         "correct": 1,
         "expl": "\"The Book of the Elevens is finished. The Numbered "
                 "Discourses are completed.\" — translated this time."},
        {"q": "What does this page mark the completion of for this "
              "entire project, according to the guide?",
         "opts": [
             "Only this single compressed page",
             "All 1,151 AN11 discourses, and with them this project's "
             "complete translation of all 1,408 discourses across AN "
             "1 through AN 11",
             "Only chapter 3's own span",
             "Nothing beyond the Rāgapeyyāla itself"],
         "correct": 1,
         "expl": "The final page of the entire Aṅguttara Nikāya "
                 "completion project."},
        {"q": "What is the arithmetic behind this Rāgapeyyāla's full "
              "170-discourse span, according to the guide?",
         "opts": [
             "170 discourses with no discoverable structure",
             "16 defilements × 10 verbs (160) plus greed's own 10 "
             "discourses (AN 11.982–991) equals 170",
             "17 defilements repeated 10 times each with no verb "
             "multiplication",
             "A single list repeated 170 times"],
         "correct": 1,
         "expl": "Confirmed against bilara-data before writing, "
                 "matching the discourse range AN 11.982 through AN "
                 "11.1151 exactly."},
        {"q": "Where is this compressed passage set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this compressed passage."},
    ],
    "marginalia": [
        ("The same sixteen, met a third time", [
            "hate through negligence &mdash;",
            "the list that closed the Nines,",
            "the Tens, now the Elevens",
        ]),
        ("One hundred sixty, compressed to one page", [
            "sixteen times ten, plus",
            "greed's own ten &mdash; one hundred",
            "seventy, all told",
        ]),
        ("Four closures, one breath", [
            "the peyyāla ends,",
            "the Elevens end, and with them",
            "the whole collection",
        ]),
        ("Cross-references", [
            "AN 11.983&ndash;991 &middot; previous, greed's own "
            "closing verbs",
            "AN 9.113&ndash;432, AN 10.267&ndash;746 &middot; the "
            "earlier two uses of this identical sixteen-item "
            "defilement list, closing the Nines and the Tens",
            "AN 11.1 &middot; the opening page of this nipāta, "
            "reached from here by following the collection's own "
            "sequence backward through all 1,408 discourses",
        ]),
    ],
    "further": [
        '<a href="%s/an11.992-1151/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="an-11.983-991.html">AN 11.983&ndash;991</a> &mdash; previous.',
        '<a href="an-9.113-432.html">AN 9.113&ndash;432</a> &mdash; the earlier use of '
        "this identical sixteen-item defilement list.",
    ],
})
