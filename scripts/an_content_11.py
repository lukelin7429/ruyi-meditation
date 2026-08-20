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
        '<a href="an-11.22.html">AN 11.22</a> &mdash; next, opening chapter 3.',
    ],
)
