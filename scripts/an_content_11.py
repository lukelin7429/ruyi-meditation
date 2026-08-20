# -*- coding: utf-8 -*-
"""Ekādasaka Nipāta — The Elevens. One discourse per page, from AN 11.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Ekādasaka Nipāta — The Elevens"
# HEAD points at the last page the Tens module reached. TAIL points at the
# nearest already-published page beyond the current build -- an-11.15.html,
# the sole survivor of the earlier eighteen-page selection, until this
# module's own PAGES reaches and splices past it, per the an-10.60/
# an-10.176 precedent. an-11.15 sits inside chapter 2 (Anussativagga,
# 11.11-21), between 11.14 and 11.16; once chapter 2 is built it is spliced
# in with explicit prev=/next= kwargs and this TAIL constant stops being
# needed for that purpose, moving on to whatever real page follows it.
HEAD = ("an-10.267-746.html",
        "AN 10.267&ndash;746 &middot; Hate, Etc., Closing the Book of the Tens")
TAIL = ("an-11.15.html", "AN 11.15 &middot; The Benefits of Love")
INDEX_EXTRA = [
    ("an-11.15", "Mettānisaṁsa", "The Benefits of Love"),
]

PAGES = []

VAGGA_1 = "<em>Nissayavagga</em> &mdash; the first chapter of the Elevens"
SETTING_SAVATTHI = "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery"
SETTING_NATIKA = "Ñātika, in the brick house"
SETTING_RAJAGAHA = ("Rājagaha, at the monastery of the wanderers in the "
                    "peacocks&rsquo; feeding ground")
SETTING_NONE = "None stated in the source"
SPEAKER = "The Buddha alone, addressing the mendicants"


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
