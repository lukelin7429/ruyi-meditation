# -*- coding: utf-8 -*-
"""Dasaka Nipāta — The Tens. One discourse per page, from AN 10.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Dasaka Nipāta — The Tens"
# HEAD points at the last page the Nines module reached. TAIL points at the
# nearest already-published page beyond the Tens -- an-11.15.html, from the
# earlier eighteen-page selection -- until the Elevens module exists and
# TAIL can move to its own first page. an-10.60.html and an-10.176.html,
# also from that earlier selection, sit inside this module's own range
# (an-10.60 closes ch.6 Sacittavagga; an-10.176 sits mid-chapter in ch.12
# Janussonivagga) and are spliced in with explicit prev=/next= kwargs, per
# the an-6.16/an-6.63/an-7.6/an-8.30/an-8.53/an-9.20 precedent.
HEAD = ("an-9.113-432.html",
        "AN 9.113&ndash;432 &middot; Sixteen Defilements, Ten Verbs")
TAIL = ("an-11.15.html", "AN 11.15 &middot; The Benefits of Love")
INDEX_EXTRA = [
    ("an-10.60", "Girimānandasutta", "With Girimānanda"),
    ("an-10.176", "Cundasutta", "With Cunda"),
]

PAGES = []

VAGGA_1 = "<em>Anisaṁsavagga</em> &mdash; the first chapter of the Tens"
SETTING_SAVATTHI = "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery"
SETTING_NONE = "None stated in the source"
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Tens."""
    d = {
        "slug": "an-10.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an10/an10.%d" % num,
        "crumb": "AN 10.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 10.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 10.1 — Kimatthiyasutta
# --------------------------------------------------------------------------- #
page(
    1, "Kimatthiya", "What&rsquo;s the Goal?",
    vagga=VAGGA_1,
    meta_title="AN 10.1 — What's the Goal? | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kimatthiyasutta, opening the Book of the Tens with Ānanda's "
        "chained questioning of the Buddha — ten links from ethics to "
        "the knowledge and vision of freedom. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "Venerable Ānanda questioning the Buddha"),
        ("Form", "Nine repeated questions, each asking the goal of the "
                 "previous answer, then the full ten-link chain restated"),
        ("Length", "~2 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own name to "
                               "the chapter, <em>Anisaṁsavagga</em>, the "
                               "Chapter on Benefits, and opens the "
                               "entire new nipāta"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "famous ten-link chain, worth reading slowly"),
    ],
    why=(
        "Ānanda asks the Buddha, link by link, what the goal and "
        "benefit of skillful ethics is, and each answer becomes the "
        "next question's subject: no regret, joy, rapture, tranquility, "
        "bliss, immersion, true knowledge and vision, disillusionment "
        "and dispassion, and finally the knowledge and vision of "
        "freedom &mdash; ten links opening the Book of the Tens."),
    guide=[
        ("The teaching in one sentence", [
            "Skillful ethics leads progressively to the highest through "
            "ten links: no regret, joy, rapture, tranquility, bliss, "
            "immersion, true knowledge and vision, disillusionment and "
            "dispassion, and the knowledge and vision of freedom, each "
            "the goal and benefit of the one before it."]),
        ("A new nipāta, and this chapter's own namesake", [
            "As with every new nipāta before it, the Book of the Tens "
            "opens with a discourse lending its own subject &mdash; "
            "<em>atthiya</em>, goal or benefit &mdash; to the chapter's "
            "name, <em>Anisaṁsavagga</em>, the Chapter on Benefits."]),
        ("A chain built by repeated questioning", [
            "Rather than stating the ten links outright, the discourse "
            "builds them one at a time: Ānanda asks the goal of ethics, "
            "receives an answer, then asks the goal of that answer, and "
            "so on nine times running, before the Buddha restates the "
            "whole chain in a single unbroken recitation."]),
        ("A ten-link version of a chain met before, in shorter form", [
            "This same progressive logic &mdash; each stage the "
            "necessary ground for the next &mdash; already appeared in "
            "shorter form in this project, at AN 7.65's six-link chain "
            "from conscience to freedom, and echoes the well-known "
            "Upanisā Sutta pattern found elsewhere in the canon. This "
            "version's own ten links culminate not in freedom itself but "
            "in the <em>knowledge and vision</em> of freedom &mdash; "
            "explicit reflective awareness of liberation already "
            "attained."]),
    ],
    terms=[
        ("kimatthiyā, kimānisaṁsā",
         "&ldquo;what is the goal, what is the benefit&rdquo; &mdash; "
         "Ānanda's own repeated question, giving this discourse its "
         "title and this chapter its name."),
        ("avippaṭisāra",
         "&ldquo;having no regrets&rdquo; &mdash; the first link, the "
         "immediate fruit of skillful ethics."),
        ("samādhi",
         "&ldquo;immersion&rdquo; &mdash; the sixth link, the point "
         "where the chain moves from feeling-based qualities to "
         "cognitive ones."),
        ("yathābhūtañāṇadassana",
         "&ldquo;truly knowing and seeing&rdquo; &mdash; the seventh "
         "link, insight arising from a concentrated mind."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the "
         "tenth and final link, closing the chain."),
    ],
    text_intro=(
        "The discourse in full: nine chained questions, then the full "
        "ten-link chain restated. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Nine questions, chained"),
        ("p", "&sect;1", "an10.1:1.1-10.2"),
        ("h3", "The chain, restated in full"),
        ("p", "&sect;2", "an10.1:11.1-11.10"),
    ],
    quiz=[
        {"q": "How does this discourse build its ten-link chain?",
         "opts": [
             "By stating all ten links outright in a single line",
             "Through nine repeated questions, each asking the goal of "
             "the previous answer, before restating the whole chain",
             "Through a narrative with several characters",
             "Through a simile alone"],
         "correct": 1,
         "expl": "A chain built by repeated questioning, not simply "
                 "announced."},
        {"q": "What is the first link in the chain?",
         "opts": [
             "Immersion", "No regret (the goal of skillful ethics)",
             "Rapture", "Freedom itself"],
         "correct": 1,
         "expl": "The immediate fruit of skillful ethics, opening the "
                 "chain."},
        {"q": "What is the tenth and final link?",
         "opts": [
             "Bliss", "Tranquility",
             "The knowledge and vision of freedom",
             "Disillusionment alone"],
         "correct": 2,
         "expl": "Not freedom itself, but explicit reflective awareness "
                 "of it."},
        {"q": "According to the guide, where has this project already "
              "met a shorter version of this same progressive logic?",
         "opts": [
             "Nowhere before this discourse",
             "AN 7.65's six-link chain from conscience to freedom",
             "Only in a completely unrelated nipāta",
             "AN 9.1, the opening of the previous nipāta"],
         "correct": 1,
         "expl": "A shorter chain sharing the same each-stage-grounds-"
                 "the-next logic."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular", "Its own subject, goal or benefit "
             "(atthiya), naming Anisaṁsavagga",
             "A disciple's name", "A place name"],
         "correct": 1,
         "expl": "As with every new nipāta's opener, the discourse "
                 "names its own chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "No setting is given"],
         "correct": 1,
         "expl": "The standard opening setting for a new nipāta's first "
                 "discourse."},
    ],
    marginalia=[
        ("Ten links, chained", [
            "no regret, joy, rapture,",
            "tranquility, bliss,",
            "immersion, and beyond",
        ]),
        ("Built by questioning", [
            "Ānanda asks nine",
            "times over &mdash; then the whole",
            "chain, restated once",
        ]),
        ("A new nipāta's own namesake", [
            "atthiya gives its name",
            "to Anisaṁsavagga &mdash;",
            "the chapter it opens",
        ]),
        ("Cross-references", [
            "AN 9.113&ndash;432 &middot; previous nipāta, closing the "
            "Nines",
            "AN 7.65 &middot; an earlier, shorter version of this same "
            "progressive logic",
            "AN 10.2 &middot; next, the same chain restated positively",
        ]),
    ],
    further=[
        '<a href="%s/an10.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.113-432.html">AN 9.113&ndash;432</a> &mdash; previous, closing the '
        "Book of the Nines.",
        '<a href="an-10.2.html">AN 10.2 &middot; Making a Wish</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.2 — Cetanākaraṇīyasutta
# --------------------------------------------------------------------------- #
page(
    2, "Cetanākaraṇīya", "Making a Wish",
    vagga=VAGGA_1,
    meta_title="AN 10.2 — Making a Wish | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Cetanākaraṇīyasutta, restating AN 10.1's ten-link chain "
        "positively — each stage arising naturally from the one "
        "before, with no wish required. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same ten links as AN 10.1, restated as things "
                 "that need not be wished for"),
        ("Length", "~2 minutes to read"),
        ("The identical chain, reframed", "Same ten links, same order, "
         "but framed here as natural consequence rather than "
         "questioned goal"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content as AN 10.1, worth comparing "
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
        ("The identical chain, a different frame", [
            "This discourse's ten links are exactly AN 10.1's, in the "
            "same order, but the framing shifts entirely: rather than "
            "Ānanda asking what each stage's goal is, this discourse "
            "insists no wishing is needed at all &mdash; the whole "
            "sequence unfolds &lsquo;only natural[ly]&rsquo; once its "
            "foundation, ethical conduct, is genuinely fulfilled."]),
        ("From near shore to far shore", [
            "The discourse's closing image is distinctive to this "
            "version: good qualities are said to &lsquo;flow on and "
            "fill up from one to the other, for going from the near "
            "shore to the far shore&rsquo; &mdash; a river-crossing "
            "metaphor for the whole ten-link progression, not present "
            "in AN 10.1's own closing restatement."]),
        ("Why naturalness matters here", [
            "The discourse's real claim is about causal reliability, "
            "not merely inspiration: given genuine ethical "
            "conduct as the base, the remaining nine links are not "
            "separate achievements requiring separate effort or "
            "aspiration, but a single unfolding process that completes "
            "itself once correctly started."]),
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
         "more precise than AN 10.1's bare &lsquo;tranquility&rsquo;."),
        ("orimā tīrā pārimaṁ tīraṁ gamanāya",
         "&ldquo;from the near shore to the far shore&rdquo; &mdash; "
         "this discourse's own closing image, absent from AN 10.1's "
         "restatement of the same chain."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the "
         "tenth and final link, identical to AN 10.1's own closing "
         "term."),
    ],
    text_intro=(
        "The discourse in full: the same ten links as AN 10.1, now "
        "framed as natural consequence requiring no wish. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten links, unfolding naturally"),
        ("p", "&sect;1", "an10.2:1.1-1.27"),
        ("h3", "The chain, restated in full"),
        ("p", "&sect;2", "an10.2:2.1-2.10"),
    ],
    quiz=[
        {"q": "How does this discourse's ten links compare to AN "
              "10.1's?",
         "opts": [
             "Entirely different content",
             "The identical ten links in the same order, framed "
             "differently",
             "A shortened five-link version",
             "A contradiction of AN 10.1"],
         "correct": 1,
         "expl": "Same chain, different frame — natural unfolding "
                 "rather than questioned goal."},
        {"q": "What refrain closes each of the ten steps in this "
              "discourse?",
         "opts": [
             "A verse of praise",
             "&ldquo;It's only natural&rdquo;",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "Insisting each stage requires no deliberate wish."},
        {"q": "What image closes this discourse that AN 10.1 doesn't "
              "use?",
         "opts": [
             "A burning pile of twigs",
             "Going from the near shore to the far shore",
             "A tree with branches and foliage",
             "A lame four-footed animal"],
         "correct": 1,
         "expl": "A river-crossing metaphor distinctive to this "
                 "version of the chain."},
        {"q": "According to the guide, what is this discourse's real "
              "claim?",
         "opts": [
             "That effort is unnecessary at every stage of practice",
             "That given genuine ethical conduct as the base, the "
             "remaining links unfold as one reliable process, not "
             "separate achievements requiring separate aspiration",
             "That wishing is the only path to freedom",
             "That ethics has nothing to do with the later links"],
         "correct": 1,
         "expl": "A claim about causal reliability, not about "
                 "eliminating effort at the foundation."},
        {"q": "What does this discourse specify more precisely than AN "
              "10.1 at the fourth link?",
         "opts": [
             "Immersion",
             "Bodily tranquility, rather than bare &lsquo;tranquility"
             "&rsquo;",
             "Rapture",
             "The three knowledges"],
         "correct": 1,
         "expl": "A slightly more precise term at one point in the "
                 "otherwise identical chain."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, unlike AN 10.1's narrative frame with "
                 "Ānanda."},
    ],
    marginalia=[
        ("The same chain, no wishing", [
            "no regret, joy, rapture &mdash;",
            "&ldquo;it's only natural&rdquo;,",
            "not something to ask for",
        ]),
        ("Near shore to far shore", [
            "good qualities flow,",
            "filling one from the other &mdash;",
            "a river, crossed",
        ]),
        ("One process, not ten wishes", [
            "ethics genuinely",
            "fulfilled, and the rest unfolds &mdash;",
            "reliable, not separate",
        ]),
        ("Cross-references", [
            "AN 10.1 &middot; the identical ten links under their "
            "original questioning frame",
            "AN 10.3 &middot; next, the same chain stated negatively",
        ]),
    ],
    further=[
        '<a href="%s/an10.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.1.html">AN 10.1 &middot; What&rsquo;s the Goal?</a> &mdash; the '
        "identical ten links under their original questioning frame.",
        '<a href="an-10.3.html">AN 10.3 &middot; Vital Conditions (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.3 — Upanisasutta (1st)
# --------------------------------------------------------------------------- #
page(
    3, "Upanisa", "Vital Conditions (1st)",
    vagga=VAGGA_1,
    meta_title="AN 10.3 — Vital Conditions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the first Upanisasutta, stating AN 10.1's ten-link chain "
        "negatively — each missing link destroying the condition for "
        "the next — with a tree-without-branches simile. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same ten links stated negatively (destruction) "
                 "and positively (fulfillment), each with a tree "
                 "simile"),
        ("Length", "~2 minutes to read"),
        ("A third framing of the same chain", "After AN 10.1's "
         "questioning and AN 10.2's natural unfolding, this discourse "
         "states the identical ten links as vital conditions that can "
         "be destroyed or fulfilled"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the "
                       "same content a third time, now with an explicit "
                       "simile"),
    ],
    why=(
        "An unethical person destroys the vital condition for freedom "
        "from regret, and from there each missing link destroys the "
        "condition for the next, like a branchless tree whose shoots "
        "and heartwood never grow to fullness; an ethical person, "
        "conversely, fulfills each vital condition in turn, like a "
        "tree complete with branches and foliage."),
    guide=[
        ("The teaching in one sentence", [
            "Lacking ethics destroys the vital condition for freedom "
            "from regret, and each further missing link &mdash; joy, "
            "rapture, tranquility, bliss, immersion, true knowledge and "
            "vision, disillusionment and dispassion &mdash; destroys "
            "the vital condition for the next, exactly as fulfilling "
            "each in turn builds toward the knowledge and vision of "
            "freedom."]),
        ("A third framing of the identical chain", [
            "This project has now met the same ten links three times "
            "running: AN 10.1's questioned goals, AN 10.2's natural "
            "unfolding, and now this discourse's vital-condition "
            "framing &mdash; &lsquo;upanisā,&rsquo; the same term "
            "already met in AN 9.23's chain rooted in craving, here "
            "applied to a wholesome sequence instead."]),
        ("A tree, twice over", [
            "The discourse's own simile makes the causal logic vivid: a "
            "tree lacking branches and foliage cannot grow shoots, "
            "bark, softwood, or heartwood to fullness, just as a person "
            "lacking any one link in the chain cannot develop what "
            "depends on it; a tree complete with branches and foliage "
            "grows to fullness in every part, just as fulfilling each "
            "link enables the next."]),
        ("Destruction and fulfillment as mirror images", [
            "Unlike AN 10.1 and AN 10.2, which each state the chain "
            "only in one direction, this discourse gives both: what is "
            "destroyed when ethics is lacking, and what is fulfilled "
            "when ethics is complete, closing on the same tree image "
            "used for both directions."]),
    ],
    terms=[
        ("upanisā",
         "&ldquo;vital condition&rdquo; &mdash; this discourse's own "
         "title term, the same word already met in AN 9.23's chain "
         "rooted in craving, here applied wholesomely."),
        ("dussīlo, sīlavipanno",
         "&ldquo;an unethical person, who lacks ethics&rdquo; &mdash; "
         "the discourse's opening figure, whose lack destroys the "
         "chain's first vital condition."),
        ("upacchinnūpaniso hoti",
         "&ldquo;has destroyed a vital condition&rdquo; &mdash; the "
         "shared refrain for each negative step of the chain."),
        ("rukkho sākhāpalāsavikalo",
         "&ldquo;a tree that lacked branches and foliage&rdquo; "
         "&mdash; the simile's negative half, illustrating how missing "
         "one link prevents growth in what depends on it."),
        ("paripūrūpaniso hoti",
         "&ldquo;has fulfilled a vital condition&rdquo; &mdash; the "
         "shared refrain for each positive step, mirroring the negative "
         "framing exactly."),
    ],
    text_intro=(
        "The discourse in full: the same ten links stated as vital "
        "conditions, destroyed or fulfilled, each with a tree simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Vital conditions destroyed"),
        ("p", "&sect;1", "an10.3:1.1-1.13"),
        ("h3", "Vital conditions fulfilled"),
        ("p", "&sect;2", "an10.3:2.1-2.13"),
    ],
    quiz=[
        {"q": "What term does this discourse use for each link in the "
              "chain, and where has this project already met it?",
         "opts": [
             "&lsquo;Bhāvanā&rsquo;, met nowhere else",
             "&lsquo;Upanisā&rsquo;, vital condition, already met in AN "
             "9.23's chain rooted in craving",
             "&lsquo;Nirodha&rsquo;, met at AN 9.31",
             "A term unique to this discourse"],
         "correct": 1,
         "expl": "The same term, here applied to a wholesome sequence "
                 "rather than a chain rooted in craving."},
        {"q": "What simile illustrates this discourse's causal logic?",
         "opts": [
             "A burning pile of twigs",
             "A tree lacking (or complete with) branches and foliage, "
             "affecting whether shoots and heartwood grow to fullness",
             "A wild bull elephant",
             "A stone post unmoved by storms"],
         "correct": 1,
         "expl": "Applied twice, once for destruction and once for "
                 "fulfillment."},
        {"q": "How does this discourse's structure differ from AN 10.1 "
              "and AN 10.2's?",
         "opts": [
             "It states the chain only once, briefly",
             "It gives both directions — destruction when ethics is "
             "lacking, and fulfillment when ethics is complete",
             "It uses entirely different links",
             "It has no relationship to those two discourses"],
         "correct": 1,
         "expl": "A third framing of the identical chain, this time "
                 "with both mirror-image directions given in full."},
        {"q": "What happens when a person destroys the vital condition "
              "for freedom from regret?",
         "opts": [
             "Nothing further is affected",
             "Each subsequent link's own vital condition is also "
             "destroyed in turn, cascading through the whole chain",
             "Only the final link is affected",
             "The chain reverses direction"],
         "correct": 1,
         "expl": "A cascading destruction, mirrored by cascading "
                 "fulfillment in the positive half."},
        {"q": "How many times has this project now met this identical "
              "ten-link chain?",
         "opts": [
             "Once", "Twice", "Three times", "Four times"],
         "correct": 2,
         "expl": "AN 10.1, AN 10.2, and now this discourse."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 10.2 immediately before "
                 "it."},
    ],
    marginalia=[
        ("A third framing", [
            "questioned, then natural,",
            "now a vital condition &mdash;",
            "the same ten links again",
        ]),
        ("A tree, twice told", [
            "branchless, no fullness;",
            "complete, and it grows &mdash;",
            "the same logic, mirrored",
        ]),
        ("A term reused wholesomely", [
            "upanisā, once",
            "craving's own chain &mdash; now,",
            "the opposite direction",
        ]),
        ("Cross-references", [
            "AN 9.23 &middot; the same term &lsquo;upanisā&rsquo;, "
            "there naming craving's own chain",
            "AN 10.2 &middot; previous",
            "AN 10.4 &middot; next, the same chain reported by "
            "Sāriputta",
        ]),
    ],
    further=[
        '<a href="%s/an10.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.23.html">AN 9.23 &middot; Rooted in Craving</a> &mdash; the same term '
        "&lsquo;upanisā&rsquo;, there naming a different chain.",
        '<a href="an-10.2.html">AN 10.2 &middot; Making a Wish</a> &mdash; previous.',
        '<a href="an-10.4.html">AN 10.4 &middot; Vital Conditions (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.4 — Upanisasutta (2nd)
# --------------------------------------------------------------------------- #
page(
    4, "Upanisa", "Vital Conditions (2nd)",
    vagga=VAGGA_1,
    meta_title="AN 10.4 — Vital Conditions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the second Upanisasutta, the identical vital-conditions chain "
        "as AN 10.3, this time reported by Sāriputta rather than the "
        "Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from the "
                    "chapter's opening"),
        ("Speakers", "Venerable Sāriputta, addressing the mendicants"),
        ("Form", "The identical vital-conditions chain as AN 10.3, "
                 "abbreviated, spoken by a different teacher"),
        ("Length", "~1 minute to read"),
        ("Same content, a different speaker", "The only real change "
         "from AN 10.3 is who is teaching — a pattern this project has "
         "met before with other chains and formulas"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, best read as a companion to AN 10.3"),
    ],
    why=(
        "Sāriputta addresses the mendicants with the identical vital-"
        "conditions chain already given by the Buddha at AN 10.3 "
        "&mdash; lacking ethics destroying the condition for freedom "
        "from regret and cascading through the whole chain, fulfilling "
        "ethics building it in the same order &mdash; abbreviated but "
        "unchanged in content."),
    guide=[
        ("The teaching in one sentence", [
            "The same vital-conditions chain as AN 10.3 &mdash; lacking "
            "or fulfilling ethics cascading through freedom from "
            "regret, joy, rapture, tranquility, bliss, immersion, true "
            "knowledge and vision, disillusionment and dispassion, to "
            "the knowledge and vision of freedom &mdash; is here taught "
            "by Sāriputta rather than the Buddha."]),
        ("A shift in speaker, not in content", [
            "Word for word, apart from compression through the "
            "source's own peyyāla, this discourse repeats AN 10.3's "
            "chain exactly, including its tree simile in both "
            "directions. The only substantive change is the speaker: "
            "Sāriputta teaching the mendicants directly, without the "
            "Buddha present in the narrative."]),
        ("A pattern already familiar from this project", [
            "This project has already met teachings repeated by a "
            "different speaker without changing content &mdash; AN "
            "9.27 and AN 9.28's identical stream-entry formula, "
            "addressed first to Anāthapiṇḍika and then to the "
            "mendicants generally, is the closest precedent. Here the "
            "variable is not audience but teacher."]),
        ("Confirming the chain's standing beyond the Buddha's own "
         "voice", [
            "That a senior disciple can teach this exact sequence "
            "without alteration suggests the chain was understood as "
            "settled doctrine, not a teaching unique to how the Buddha "
            "himself happened to phrase it on one occasion."]),
    ],
    terms=[
        ("āyasmā sāriputto bhikkhū āmantesi",
         "&ldquo;Venerable Sāriputta addressed the mendicants&rdquo; "
         "&mdash; this discourse's own opening, the sole narrative "
         "difference from AN 10.3."),
        ("upanisā",
         "&ldquo;vital condition&rdquo; &mdash; the identical term and "
         "chain-structure as AN 10.3."),
        ("upacchinnūpaniso, paripūrūpaniso",
         "&ldquo;destroyed a vital condition... fulfilled a vital "
         "condition&rdquo; &mdash; the same two refrains carried over "
         "unchanged from AN 10.3."),
        ("rukkho sākhāpalāsavikalo",
         "&ldquo;a tree that lacked branches and foliage&rdquo; "
         "&mdash; the identical simile, repeated in both directions as "
         "at AN 10.3."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; "
         "the chain's shared final link."),
    ],
    text_intro=(
        "The discourse in full, as it survives: the same vital-"
        "conditions chain as AN 10.3, taught by Sāriputta. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The same chain, taught by Sāriputta"),
        ("p", "&sect;1", "an10.4:1.1-1.8"),
        ("p", "&sect;2", "an10.4:2.1-2.7"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 10.3's?",
         "opts": [
             "Entirely different chain",
             "The identical vital-conditions chain and tree simile, "
             "unchanged apart from compression",
             "A shortened five-link version",
             "A contradiction of AN 10.3"],
         "correct": 1,
         "expl": "Word for word the same content, differing only in "
                 "who teaches it."},
        {"q": "Who teaches this discourse, unlike AN 10.3?",
         "opts": [
             "The Buddha, exactly as at AN 10.3",
             "Venerable Sāriputta, addressing the mendicants directly",
             "Venerable Ānanda",
             "A group of deities"],
         "correct": 1,
         "expl": "The one substantive change from its companion "
                 "discourse."},
        {"q": "Where has this project already met a teaching repeated "
              "by a different speaker without changing content?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.27 and AN 9.28's identical stream-entry formula, "
             "there varying by audience rather than teacher",
             "Only in a completely unrelated nipāta",
             "AN 10.1, the opening discourse"],
         "correct": 1,
         "expl": "A related but distinct pattern — there the audience "
                 "varied, here the speaker does."},
        {"q": "According to the guide, what does Sāriputta's ability to "
              "teach this chain unaltered suggest?",
         "opts": [
             "That Sāriputta misunderstood the original teaching",
             "That the chain was settled doctrine, not unique to the "
             "Buddha's own particular phrasing",
             "That the chain is unreliable",
             "Nothing significant"],
         "correct": 1,
         "expl": "A teaching stable enough to be repeated by a senior "
                 "disciple without alteration."},
        {"q": "What simile does this discourse share with AN 10.3?",
         "opts": [
             "A burning pile of twigs",
             "A tree lacking or complete with branches and foliage",
             "A wild bull elephant",
             "A stone post"],
         "correct": 1,
         "expl": "The identical tree image, in both directions."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "Not restated, understood to continue from the "
                 "chapter's opening setting."},
    ],
    marginalia=[
        ("The same chain, new voice", [
            "not the Buddha now,",
            "but Sāriputta teaches",
            "the identical chain",
        ]),
        ("A settled teaching", [
            "repeated unaltered",
            "by a senior disciple &mdash;",
            "not one man's phrasing",
        ]),
        ("A related pattern", [
            "there, one audience, two;",
            "here, one chain, two teachers &mdash;",
            "the variable shifts",
        ]),
        ("Cross-references", [
            "AN 9.27, AN 9.28 &middot; a related pattern, the same "
            "content repeated for a different audience",
            "AN 10.3 &middot; the identical chain, there taught by the "
            "Buddha",
            "AN 10.5 &middot; next, the same chain a third time, taught "
            "by Ānanda",
        ]),
    ],
    further=[
        '<a href="%s/an10.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.3.html">AN 10.3 &middot; Vital Conditions (1st)</a> &mdash; the '
        "identical chain, there taught by the Buddha.",
        '<a href="an-10.5.html">AN 10.5 &middot; Vital Conditions (3rd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.5 — Upanisasutta (3rd)
# --------------------------------------------------------------------------- #
page(
    5, "Upanisa", "Vital Conditions (3rd)",
    vagga=VAGGA_1,
    meta_title="AN 10.5 — Vital Conditions (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the third Upanisasutta, the identical vital-conditions chain "
        "given in full a third time, now taught by Ānanda, closing this "
        "chain's own three-teacher sequence. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from the "
                    "chapter's opening"),
        ("Speakers", "Venerable Ānanda, addressing the mendicants"),
        ("Form", "The identical vital-conditions chain as AN 10.3-4, "
                 "given here in full rather than abbreviated"),
        ("Length", "~2 minutes to read"),
        ("Closing a three-teacher sequence", "The Buddha (AN 10.3), "
         "Sāriputta (AN 10.4), and now Ānanda each teach the identical "
         "chain, completing a small deliberate set"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the same content a third time, worth noting who "
                       "has now taught it"),
    ],
    why=(
        "Ānanda addresses the mendicants with the same vital-conditions "
        "chain the Buddha gave at AN 10.3 and Sāriputta repeated at AN "
        "10.4, given here in full detail rather than compressed, "
        "closing a sequence in which three different teachers deliver "
        "the identical teaching."),
    guide=[
        ("The teaching in one sentence", [
            "The same vital-conditions chain met at AN 10.3 and AN "
            "10.4 &mdash; ethics cascading through freedom from regret "
            "to the knowledge and vision of freedom, illustrated by a "
            "tree's branches and foliage &mdash; is here taught in full "
            "by Ānanda."]),
        ("A third teacher, closing the set", [
            "With this discourse, three different teachers have now "
            "delivered the identical chain: the Buddha himself at AN "
            "10.3, Sāriputta at AN 10.4, and now Ānanda &mdash; not "
            "three variant teachings but the same content, its "
            "authority underscored by three separate tellings rather "
            "than diluted by repetition."]),
        ("Full detail restored", [
            "Unlike AN 10.4's abbreviated version, this discourse gives "
            "the complete chain in both directions without compression "
            "&mdash; the same full treatment as AN 10.3 itself, "
            "matching the Buddha's own original telling in every "
            "detail."]),
        ("Ānanda as both questioner and teacher", [
            "This discourse adds a further dimension to Ānanda's own "
            "role in this chapter: at AN 10.1 he questioned the Buddha "
            "to draw out this same chain; here, several discourses "
            "later, he teaches it himself to the mendicants, suggesting "
            "the chain has by now become fully his own to transmit."]),
    ],
    terms=[
        ("āyasmā ānando bhikkhū āmantesi",
         "&ldquo;Venerable Ānanda addressed the mendicants&rdquo; "
         "&mdash; this discourse's own opening, naming the third "
         "teacher in this sequence."),
        ("upanisā",
         "&ldquo;vital condition&rdquo; &mdash; the identical term and "
         "chain-structure as AN 10.3 and AN 10.4."),
        ("upacchinnūpaniso, paripūrūpaniso",
         "&ldquo;destroyed a vital condition... fulfilled a vital "
         "condition&rdquo; &mdash; the same two refrains, given here in "
         "full rather than abbreviated."),
        ("rukkho sākhāpalāsavikalo",
         "&ldquo;a tree that lacked branches and foliage&rdquo; "
         "&mdash; the identical simile, in full detail as at AN 10.3."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; "
         "the chain's shared final link, closing this three-teacher "
         "sequence."),
    ],
    text_intro=(
        "The discourse in full: the same vital-conditions chain as AN "
        "10.3 and AN 10.4, taught in full by Ānanda. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The same chain, taught in full by Ānanda"),
        ("p", "&sect;1", "an10.5:1.1-1.14"),
        ("p", "&sect;2", "an10.5:2.1-2.13"),
    ],
    quiz=[
        {"q": "Who teaches this discourse, and how does that relate to "
              "AN 10.3 and AN 10.4?",
         "opts": [
             "The Buddha, exactly as at AN 10.3",
             "Venerable Ānanda, completing a set of three different "
             "teachers delivering the identical chain",
             "A group of deities, unrelated to the earlier two",
             "Sāriputta again, repeating AN 10.4"],
         "correct": 1,
         "expl": "The Buddha, Sāriputta, and now Ānanda — three "
                 "tellings of the same content."},
        {"q": "How does this discourse's level of detail compare to AN "
              "10.4's?",
         "opts": [
             "Equally abbreviated",
             "Given in full, matching AN 10.3's original complete "
             "treatment rather than AN 10.4's compression",
             "Even more compressed than AN 10.4",
             "Missing entirely"],
         "correct": 1,
         "expl": "Full detail restored, in both directions of the "
                 "chain."},
        {"q": "According to the guide, what does three different "
              "teachers delivering identical content suggest?",
         "opts": [
             "That the teaching is unreliable or disputed",
             "That its authority is underscored by multiple tellings "
             "rather than diluted by repetition",
             "That each teacher secretly disagrees",
             "That the chain changes meaning with each speaker"],
         "correct": 1,
         "expl": "Confirmation through multiple independent tellings, "
                 "not variation."},
        {"q": "What dual role does Ānanda play across this chapter so "
              "far, according to the guide?",
         "opts": [
             "He only ever questions, never teaches",
             "At AN 10.1 he questioned the Buddha to draw out this "
             "chain; here he teaches it himself",
             "He appears only in this single discourse",
             "He contradicts his own earlier questions"],
         "correct": 1,
         "expl": "From questioner to teacher of the same material "
                 "within one chapter."},
        {"q": "What simile does this discourse share with AN 10.3 and "
              "AN 10.4?",
         "opts": [
             "A burning pile of twigs",
             "A tree lacking or complete with branches and foliage",
             "A wild bull elephant",
             "A stone post"],
         "correct": 1,
         "expl": "The identical tree image, given here in full detail."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "Not restated, matching AN 10.4's own lack of an "
                 "explicit setting."},
    ],
    marginalia=[
        ("A third teacher", [
            "Buddha, Sāriputta,",
            "now Ānanda &mdash; the same",
            "chain, three times told",
        ]),
        ("Full detail, restored", [
            "not compressed this time &mdash;",
            "the whole tree simile,",
            "both directions given",
        ]),
        ("From questioner to teacher", [
            "he asked it at 10.1;",
            "now Ānanda himself",
            "passes it on",
        ]),
        ("Cross-references", [
            "AN 10.1 &middot; where Ānanda first questioned the Buddha "
            "to draw out this chain",
            "AN 10.3, AN 10.4 &middot; the same chain's first two "
            "tellings",
            "AN 10.6 &middot; next, Immersion",
        ]),
    ],
    further=[
        '<a href="%s/an10.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.1.html">AN 10.1 &middot; What&rsquo;s the Goal?</a> &mdash; where '
        "Ānanda first questioned the Buddha to draw out this chain.",
        '<a href="an-10.4.html">AN 10.4 &middot; Vital Conditions (2nd)</a> &mdash; previous.',
        '<a href="an-10.6.html">AN 10.6 &middot; Immersion</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.6 — Samādhisutta
# --------------------------------------------------------------------------- #
page(
    6, "Samādhi", "Immersion",
    vagga=VAGGA_1,
    meta_title="AN 10.6 — Immersion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Samādhisutta, in which Ānanda asks the Buddha about a "
        "state of immersion that perceives nothing as itself yet is "
        "still fully percipient. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda questioning the Buddha"),
        ("Form", "A precisely worded question, repeated verbatim in "
                 "the answer, then a brief explanation"),
        ("Length", "~1 minute to read"),
        ("A companion pair with AN 10.7", "Ānanda asks the Buddha this "
         "question here, then asks Sāriputta the identical question "
         "next, receiving a very different kind of answer"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "subtle and precisely worded meditative puzzle"),
    ],
    why=(
        "Ānanda asks whether a mendicant might gain a state of "
        "immersion where the four elements, the four formless "
        "dimensions, and even this world and the next are not "
        "perceived as themselves, and yet perception continues; the "
        "Buddha confirms this is possible through perceiving "
        "&lsquo;this is peaceful, this is sublime&rsquo; &mdash; the "
        "stilling of all activities, extinguishment itself."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant can gain a state of immersion where none of "
            "the four elements, the four formless dimensions, or this "
            "world and the next are perceived as themselves, and yet "
            "perception continues, by perceiving that the stilling of "
            "all activities and the ending of craving is peaceful and "
            "sublime."]),
        ("An unusually precise question", [
            "Ānanda's question is remarkable for its exhaustiveness: it "
            "names all four elements, all four formless dimensions, and "
            "both this world and another, denying that any of them are "
            "perceived as themselves &mdash; a near-total inventory of "
            "possible objects of perception, all set aside at once."]),
        ("Perceiving something else entirely", [
            "The Buddha's answer doesn't describe an absence of "
            "perception but a redirection of it: what remains "
            "perceived, when none of the usual objects are perceived as "
            "themselves, is the peace and sublimity of extinguishment "
            "itself &mdash; the same &lsquo;this is peaceful; this is "
            "sublime&rsquo; formula already met turning the mind toward "
            "the deathless at AN 9.36."]),
        ("A companion question, a different kind of answer next", [
            "This discourse's exchange between Ānanda and the Buddha "
            "sets up AN 10.7 directly: there, Ānanda puts the identical "
            "question to Sāriputta, who answers not with a general "
            "formula but with his own specific, personally verified "
            "experience of exactly this state."]),
    ],
    terms=[
        ("tathārūpaṁ samādhiṁ",
         "&ldquo;a state of immersion like this&rdquo; &mdash; "
         "Ānanda's own phrase, repeated verbatim in the Buddha's "
         "confirming reply."),
        ("na pathaviyaṁ pathavisaññī assa",
         "&ldquo;they wouldn't perceive earth in earth&rdquo; &mdash; "
         "the first item in Ānanda's exhaustive inventory of set-aside "
         "perceptions."),
        ("tajjā saññā na assa",
         "&ldquo;and yet they would still perceive&rdquo; &mdash; the "
         "discourse's own paradox, insisting perception itself "
         "continues despite none of its usual objects being perceived."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful; this is sublime&rdquo; &mdash; the "
         "same formula already met at AN 9.36, here answering Ānanda's "
         "own precisely worded question."),
        ("sabbasaṅkhārasamatho... nibbānaṁ",
         "&ldquo;the stilling of all activities... extinguishment"
         "&rdquo; &mdash; what is perceived in this state, closing the "
         "Buddha's answer."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's precisely worded question, "
        "and the Buddha's confirming answer. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A precisely worded question"),
        ("p", "&sect;1", "an10.6:1.1-2.1"),
        ("h3", "What remains, when nothing else is perceived"),
        ("p", "&sect;2", "an10.6:3.1-3.3"),
    ],
    quiz=[
        {"q": "What does Ānanda's question deny is perceived, in this "
              "state of immersion?",
         "opts": [
             "Only physical sensations",
             "The four elements, the four formless dimensions, and "
             "this world and the next — a near-total inventory of "
             "possible perceptual objects",
             "Only sounds and sights",
             "Nothing is denied at all"],
         "correct": 1,
         "expl": "An unusually exhaustive question, covering nearly "
                 "every category of possible perception."},
        {"q": "Despite denying all these objects, what does the "
              "discourse insist still continues?",
         "opts": [
             "Nothing continues at all",
             "Perception itself continues, redirected rather than "
             "absent",
             "Only physical sensation continues",
             "Memory alone continues"],
         "correct": 1,
         "expl": "A paradox the Buddha's answer resolves by naming what "
                 "is perceived instead."},
        {"q": "What does the Buddha say is perceived in this state?",
         "opts": [
             "Nothing whatsoever",
             "That the stilling of all activities and the ending of "
             "craving is peaceful and sublime",
             "A vision of the Buddha himself",
             "The four noble truths recited in full"],
         "correct": 1,
         "expl": "The same &lsquo;peaceful, sublime&rsquo; formula "
                 "already met turning the mind toward the deathless."},
        {"q": "What does this discourse set up for AN 10.7?",
         "opts": [
             "Nothing; the two are unrelated",
             "Ānanda asks the identical question to Sāriputta next, "
             "who answers from his own specific personal experience",
             "AN 10.7 contradicts this discourse's answer",
             "AN 10.7 asks a completely different question"],
         "correct": 1,
         "expl": "A companion pair — the same question, put to two "
                 "different teachers."},
        {"q": "Where has this project already met the &lsquo;peaceful, "
              "sublime&rsquo; formula?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.36, turning the mind toward the deathless from "
             "within absorption",
             "Only in a completely unrelated nipāta",
             "AN 10.1, the opening discourse"],
         "correct": 1,
         "expl": "The identical formula, reused here to answer Ānanda's "
                 "precise question."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare dialogue, without an explicit narrative "
                 "setting."},
    ],
    marginalia=[
        ("An exhaustive question", [
            "earth, water, fire, air,",
            "four formless realms, both worlds &mdash;",
            "none perceived as such",
        ]),
        ("Perception, redirected", [
            "not absence, but a",
            "different object &mdash;",
            "peace itself, perceived",
        ]),
        ("A companion question ahead", [
            "the same words, put to",
            "Sāriputta next &mdash;",
            "a personal answer",
        ]),
        ("Cross-references", [
            "AN 9.36 &middot; the same &lsquo;peaceful, sublime&rsquo; "
            "formula, turning the mind toward the deathless",
            "AN 10.5 &middot; previous",
            "AN 10.7 &middot; next, Sāriputta, the same question "
            "answered personally",
        ]),
    ],
    further=[
        '<a href="%s/an10.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.36.html">AN 9.36 &middot; Depending on Absorption</a> &mdash; the same '
        "&lsquo;peaceful, sublime&rsquo; formula, first met there.",
        '<a href="an-10.5.html">AN 10.5 &middot; Vital Conditions (3rd)</a> &mdash; previous.',
        '<a href="an-10.7.html">AN 10.7 &middot; Sāriputta</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.7 — Sāriputtasutta
# --------------------------------------------------------------------------- #
page(
    7, "Sāriputta", "Sāriputta",
    vagga=VAGGA_1,
    meta_title="AN 10.7 — Sāriputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sāriputtasutta, in which Ānanda asks Sāriputta the "
        "identical question as AN 10.6 and receives a personal account "
        "of the burning-twigs perception at the Dark Forest. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, at the Dark Forest, recalled within the "
                    "dialogue"),
        ("Speakers", "Venerable Ānanda questioning Venerable Sāriputta"),
        ("Form", "The identical question as AN 10.6, answered here "
                 "through Sāriputta's own first-person recollection"),
        ("Length", "~2 minutes to read"),
        ("A general formula, then a personal account", "Where AN 10.6 "
         "answered with a general teaching, this discourse answers "
         "with Sāriputta's own specific, remembered experience"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the same puzzle as AN 10.6, now grounded in a "
                       "vivid personal account"),
    ],
    why=(
        "Ānanda puts the identical question to Sāriputta that he asked "
        "the Buddha at AN 10.6, and Sāriputta confirms it from his own "
        "experience at the Dark Forest: one perception arising as "
        "another ceased, &lsquo;the cessation of continued existence is "
        "extinguishment,&rsquo; like a burning pile of twigs where one "
        "flame arises as another dies away."),
    guide=[
        ("The teaching in one sentence", [
            "Sāriputta confirms Ānanda's question from personal "
            "experience: at the Dark Forest, he gained a state of "
            "immersion perceiving none of the usual objects as "
            "themselves, while one perception arose as another ceased "
            "&mdash; &lsquo;the cessation of continued existence is "
            "extinguishment.&rsquo;"]),
        ("The same question, a personal rather than general answer", [
            "Ānanda repeats to Sāriputta, word for word, the same "
            "elaborate question already put to the Buddha at AN 10.6. "
            "But where the Buddha answered with a general teaching "
            "formula, Sāriputta answers by recounting a specific "
            "occasion in his own past: &lsquo;this one time I was "
            "staying right here at Sāvatthī in the Dark Forest.&rsquo;"]),
        ("A perception replacing a perception", [
            "Sāriputta's own account adds a detail AN 10.6 didn't "
            "supply: not simply the absence of ordinary perceptions, "
            "but one perception directly arising as another ceases "
            "&mdash; the repeated realization &lsquo;the cessation of "
            "continued existence is extinguishment&rsquo; replacing "
            "whatever perception came before it."]),
        ("A burning pile of twigs", [
            "The simile closing this discourse is vivid and precise: "
            "flames in a burning pile of twigs arise and cease in "
            "continuous succession, never all present at once yet the "
            "fire itself continuous &mdash; matching exactly how "
            "Sāriputta describes one perception replacing another "
            "without any gap in perceiving itself."]),
    ],
    terms=[
        ("tathārūpaṁ samādhiṁ",
         "&ldquo;a state of immersion like this&rdquo; &mdash; the "
         "identical phrase Ānanda uses to put the same question to "
         "Sāriputta as he asked the Buddha at AN 10.6."),
        ("andhavanasmiṁ",
         "&ldquo;the Dark Forest&rdquo; &mdash; the specific location "
         "near Sāvatthī where Sāriputta recalls attaining this state."),
        ("aññā saññā uppajjati, aññā saññā nirujjhati",
         "&ldquo;one perception arose... and another perception "
         "ceased&rdquo; &mdash; Sāriputta's own precise description of "
         "what actually occurred, not simply an absence of perception."),
        ("bhavanirodho nibbānaṁ",
         "&ldquo;the cessation of continued existence is "
         "extinguishment&rdquo; &mdash; the specific perception that "
         "repeatedly arose for Sāriputta at the Dark Forest."),
        ("dārukkhandhe... ekā acci uppajjati, ekā acci nirujjhati",
         "&ldquo;a burning pile of twigs. One flame would arise and "
         "another would cease&rdquo; &mdash; the discourse's own "
         "closing simile, matching Sāriputta's account of continuous "
         "perception without ordinary perceptual objects."),
    ],
    text_intro=(
        "The discourse in full: the same question as AN 10.6, answered "
        "through Sāriputta's own personal recollection. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The same question, put to Sāriputta"),
        ("p", "&sect;1", "an10.7:1.1-3.1"),
        ("h3", "A personal account, and a simile"),
        ("p", "&sect;2", "an10.7:4.1-5.5"),
    ],
    quiz=[
        {"q": "How does Ānanda's question to Sāriputta compare to his "
              "question to the Buddha at AN 10.6?",
         "opts": [
             "A completely different question",
             "Word for word identical",
             "A shortened version",
             "The opposite question"],
         "correct": 1,
         "expl": "The same elaborate question, put to a second teacher."},
        {"q": "How does Sāriputta's answer differ in kind from the "
              "Buddha's answer at AN 10.6?",
         "opts": [
             "It is identical in every way",
             "Sāriputta answers with his own specific, remembered "
             "personal experience rather than a general formula",
             "Sāriputta refuses to answer",
             "Sāriputta contradicts the Buddha's answer"],
         "correct": 1,
         "expl": "A personal account grounding the same teaching in "
                 "lived experience."},
        {"q": "Where does Sāriputta say he attained this state?",
         "opts": [
             "On Vulture's Peak at Rājagaha",
             "At the Dark Forest, near Sāvatthī",
             "In Jeta's Grove itself",
             "At the Bamboo Grove"],
         "correct": 1,
         "expl": "A specific, named location for a specific remembered "
                 "occasion."},
        {"q": "What perception does Sāriputta say repeatedly arose for "
              "him?",
         "opts": [
             "A vision of past lives",
             "&lsquo;The cessation of continued existence is "
             "extinguishment&rsquo;",
             "A memory of his ordination",
             "The four noble truths"],
         "correct": 1,
         "expl": "One perception replacing another in continuous "
                 "succession, not simple absence."},
        {"q": "What simile closes this discourse?",
         "opts": [
             "A tree lacking branches",
             "A burning pile of twigs, where one flame arises as "
             "another ceases",
             "A stone post unmoved by storms",
             "A wild bull elephant"],
         "correct": 1,
         "expl": "Continuous succession without any actual gap, "
                 "matching Sāriputta's own description exactly."},
        {"q": "Who questions whom in this discourse?",
         "opts": [
             "The Buddha questions Sāriputta",
             "Ānanda questions Sāriputta",
             "Sāriputta questions Ānanda",
             "Mahākoṭṭhita questions Sāriputta"],
         "correct": 1,
         "expl": "The same questioner as AN 10.6, now addressing a "
                 "different teacher."},
    ],
    marginalia=[
        ("The same question, asked twice", [
            "word for word, once to",
            "the Buddha, now to",
            "Sāriputta himself",
        ]),
        ("A remembered occasion", [
            "the Dark Forest, once &mdash;",
            "not a general teaching,",
            "but what he lived through",
        ]),
        ("Flames, arising and ceasing", [
            "one perception dies,",
            "another arises &mdash; like",
            "twigs, continuously burning",
        ]),
        ("Cross-references", [
            "AN 10.6 &middot; the identical question, there answered "
            "by the Buddha with a general formula",
            "AN 10.8 &middot; next, Inspiring All Around: the "
            "Absorptions",
        ]),
    ],
    further=[
        '<a href="%s/an10.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.6.html">AN 10.6 &middot; Immersion</a> &mdash; previous, the '
        "identical question answered there by the Buddha.",
        '<a href="an-10.8.html">AN 10.8 &middot; Inspiring All Around: the Absorptions</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.8 — Samajīvinasutta (Absorptions version)
# --------------------------------------------------------------------------- #
page(
    8, "Samajīvina", "Inspiring All Around: the Absorptions",
    vagga=VAGGA_1,
    meta_title=("AN 10.8 — Inspiring All Around: the Absorptions | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the first of three &lsquo;inspiring all around&rsquo; "
        "discourses, naming ten qualities that complete a mendicant, "
        "the ninth being mastery of the four absorptions. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Ten qualities named as incomplete until fulfilled, "
                 "the ninth naming the four absorptions specifically"),
        ("Length", "~2 minutes to read"),
        ("The first of a three-discourse set", "AN 10.8 through AN "
         "10.10 share nine identical qualities, differing only in "
         "their shared ninth item"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "clean ten-item list, worth reading alongside "
                       "its two companions"),
    ],
    why=(
        "A mendicant incomplete in faith, ethics, learning, teaching "
        "ability, frequenting assemblies, teaching with assurance, "
        "expertise in the training, forest dwelling, mastery of the "
        "four absorptions, or the ending of defilements should fulfill "
        "what is lacking, becoming, once all ten are complete, "
        "&lsquo;impressive all around.&rsquo;"),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who is faithful, ethical, learned, a Dhamma "
            "speaker, one who frequents assemblies, teaches with "
            "assurance, is expert in the training, lives in the "
            "wilderness, masters the four absorptions, and has ended "
            "the defilements possesses all ten qualities and is "
            "&lsquo;impressive all around.&rsquo;"]),
        ("Ten qualities, incomplete until all are present", [
            "The discourse names each quality's absence as leaving a "
            "mendicant &lsquo;incomplete in that respect,&rsquo; then "
            "prescribes fulfilling it &mdash; a cumulative structure "
            "where the final declaration of completeness only arrives "
            "once every one of the ten has been addressed in turn."]),
        ("The ninth quality: the four absorptions", [
            "This discourse's own distinctive ninth item &mdash; "
            "getting the four absorptions &lsquo;when they want, "
            "without trouble or difficulty&rsquo; &mdash; is what "
            "distinguishes it from its two companion discourses, which "
            "otherwise share all nine remaining qualities exactly."]),
        ("A three-discourse set, one variable item", [
            "AN 10.8 through AN 10.10 form a deliberate set: nine "
            "qualities held constant &mdash; faith, ethics, learning, "
            "teaching ability, assembly attendance, teaching with "
            "assurance, training expertise, and forest dwelling, plus "
            "the ending of defilements as the tenth &mdash; while the "
            "ninth item varies across the three, naming first the four "
            "absorptions, then the formless liberations, then the three "
            "knowledges."]),
    ],
    terms=[
        ("samantapāsādiko",
         "&ldquo;impressive all around&rdquo; &mdash; this discourse's "
         "own closing declaration, and the shared title concept for all "
         "three discourses in this set."),
        ("bahussuto",
         "&ldquo;learned&rdquo; &mdash; the third quality, opening the "
         "nine items shared across all three discourses in this set."),
        ("araññavanapatthāni pantāni senāsanāni paṭisevitā",
         "&ldquo;stay in the wilderness, in remote lodgings&rdquo; "
         "&mdash; the eighth quality, shared across all three "
         "discourses."),
        ("cattāro jhāne... nikāmalābhī hoti akicchalābhī akasiralābhī",
         "&ldquo;get the four absorptions... when they want, without "
         "trouble or difficulty&rdquo; &mdash; this discourse's own "
         "distinctive ninth quality."),
        ("āsavānaṁ khayā... sacchikatvā upasampajja viharati",
         "&ldquo;realize the undefiled freedom of heart and freedom by "
         "wisdom... due to the ending of defilements&rdquo; &mdash; "
         "the tenth and final quality, shared across all three "
         "discourses."),
    ],
    text_intro=(
        "The discourse in full: ten qualities, the ninth naming "
        "mastery of the four absorptions. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten qualities, completed one at a time"),
        ("p", "&sect;1", "an10.8:1.1-3.3"),
    ],
    quiz=[
        {"q": "What ninth quality distinguishes this discourse from its "
              "two companions?",
         "opts": [
             "Learning", "Getting the four absorptions when wanted, "
             "without trouble or difficulty",
             "Forest dwelling", "Ethical conduct"],
         "correct": 1,
         "expl": "The one variable item across this three-discourse "
                 "set."},
        {"q": "How many qualities does this discourse name in total?",
         "opts": [
             "Five", "Seven", "Ten", "Twelve"],
         "correct": 2,
         "expl": "Ten qualities, culminating in being &lsquo;impressive "
                 "all around.&rsquo;"},
        {"q": "What structure does the discourse use for each quality?",
         "opts": [
             "A simile for each item",
             "Naming its absence as leaving the mendicant "
             "&lsquo;incomplete,&rsquo; then prescribing its "
             "fulfillment",
             "A dialogue between two speakers",
             "A verse for each item"],
         "correct": 1,
         "expl": "A cumulative structure building toward the final "
                 "declaration of completeness."},
        {"q": "What do AN 10.8, AN 10.9, and AN 10.10 share, and what "
              "varies?",
         "opts": [
             "Nothing is shared; all three are unrelated",
             "Nine qualities are identical across all three; only the "
             "ninth item varies",
             "All ten items are identical in every discourse",
             "Only the tenth item is shared"],
         "correct": 1,
         "expl": "A deliberate three-discourse set built on a single "
                 "variable."},
        {"q": "What is the tenth and final quality, shared across all "
              "three discourses?",
         "opts": [
             "Wealth and fame",
             "Realizing freedom due to the ending of defilements",
             "Physical strength",
             "Popularity among laypeople"],
         "correct": 1,
         "expl": "The culminating quality, identical across the whole "
                 "set."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, without narrative frame."},
    ],
    marginalia=[
        ("Ten qualities, completed", [
            "faith, ethics, learning,",
            "speaking, assemblies, training,",
            "forest life, and more",
        ]),
        ("The ninth, this time", [
            "the four absorptions,",
            "gained without trouble &mdash;",
            "this set's own variable",
        ]),
        ("A deliberate trio", [
            "nine items held constant,",
            "one item swapped twice more &mdash;",
            "10.9, 10.10 next",
        ]),
        ("Cross-references", [
            "AN 10.7 &middot; previous",
            "AN 10.9 &middot; next, the same nine qualities with the "
            "formless liberations",
        ]),
    ],
    further=[
        '<a href="%s/an10.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.7.html">AN 10.7 &middot; Sāriputta</a> &mdash; previous.',
        '<a href="an-10.9.html">AN 10.9 &middot; Inspiring All Around: the Peaceful '
        "Liberations</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.9 — Samajīvinasutta (Peaceful Liberations version)
# --------------------------------------------------------------------------- #
page(
    9, "Samajīvina", "Inspiring All Around: the Peaceful Liberations",
    vagga=VAGGA_1,
    meta_title=("AN 10.9 — Inspiring All Around: the Peaceful "
                "Liberations | Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the second of three &lsquo;inspiring all around&rsquo; "
        "discourses, sharing AN 10.8's nine qualities but swapping its "
        "ninth for the formless liberations. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical nine qualities as AN 10.8, with a "
                 "different ninth item"),
        ("Length", "~1 minute to read"),
        ("The middle discourse of a three-part set", "Shares every "
         "quality with AN 10.8 and AN 10.10 except the ninth"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, best read as a companion to AN 10.8"),
    ],
    why=(
        "The same nine qualities as AN 10.8 recur, but the ninth "
        "changes: rather than mastery of the four absorptions, this "
        "discourse names direct meditative experience of the peaceful "
        "liberations that are formless, transcending form."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant complete in faith, ethics, learning, teaching "
            "ability, assembly attendance, teaching with assurance, "
            "training expertise, forest dwelling, direct experience of "
            "the formless liberations, and the ending of defilements is "
            "&lsquo;impressive all around.&rsquo;"]),
        ("The identical nine, one substitution", [
            "This discourse repeats AN 10.8's first eight qualities and "
            "tenth quality without change, substituting only the ninth: "
            "where AN 10.8 named the four absorptions, this discourse "
            "names the formless liberations, meditative attainments "
            "that transcend form altogether."]),
        ("Absorption and formless liberation, a meaningful pairing", [
            "The substitution isn't arbitrary. The four absorptions and "
            "the formless liberations represent adjacent territory in "
            "this project's own nine progressive attainments &mdash; "
            "the first four and the next four of that same nine-stage "
            "sequence &mdash; suggesting this three-discourse set moves "
            "through increasingly subtle meditative accomplishments as "
            "its shared ninth quality."]),
        ("A middle term, between absorption and knowledge", [
            "Positioned between AN 10.8's absorptions and AN 10.10's "
            "three knowledges, this discourse's formless liberations "
            "occupy a middle position: subtler than ordinary jhāna, yet "
            "still a matter of meditative attainment rather than the "
            "cognitive knowledges AN 10.10 will name next."]),
    ],
    terms=[
        ("samantapāsādiko",
         "&ldquo;impressive all around&rdquo; &mdash; the shared "
         "closing declaration for this whole three-discourse set."),
        ("santā vimokkhā atikkamma rūpe āruppā",
         "&ldquo;the peaceful liberations that are formless, "
         "transcending form&rdquo; &mdash; this discourse's own "
         "distinctive ninth quality, replacing AN 10.8's four "
         "absorptions."),
        ("kāyena phusitvā viharati",
         "&ldquo;have direct meditative experience of&rdquo; &mdash; "
         "the verb governing this discourse's ninth quality, echoing "
         "the same &lsquo;kāyasakkhī&rsquo; vocabulary met at AN 9.43."),
        ("bahussuto, dhammakathiko",
         "&ldquo;learned... a Dhamma speaker&rdquo; &mdash; two of the "
         "nine qualities shared unchanged with AN 10.8 and AN 10.10."),
        ("āsavānaṁ khayā",
         "&ldquo;due to the ending of defilements&rdquo; &mdash; the "
         "tenth quality, identical across this entire set."),
    ],
    text_intro=(
        "The discourse in full, as it survives: the same nine "
        "qualities as AN 10.8, with the formless liberations as the "
        "ninth. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten qualities, the ninth now the formless liberations"),
        ("p", "&sect;1", "an10.9:1.1-2.3"),
    ],
    quiz=[
        {"q": "What ninth quality does this discourse name, replacing "
              "AN 10.8's four absorptions?",
         "opts": [
             "The three knowledges",
             "Direct meditative experience of the peaceful liberations "
             "that are formless, transcending form",
             "The six higher knowledges",
             "The nine progressive attainments"],
         "correct": 1,
         "expl": "The one variable item in this three-discourse set."},
        {"q": "How do the other nine qualities compare to AN 10.8's?",
         "opts": [
             "Entirely different",
             "Identical — faith, ethics, learning, teaching ability, "
             "assembly attendance, teaching with assurance, training "
             "expertise, forest dwelling, and the ending of defilements",
             "Only three qualities are shared",
             "None are shared"],
         "correct": 1,
         "expl": "Only the ninth item changes across this whole set."},
        {"q": "According to the guide, how do the four absorptions and "
              "formless liberations relate within this project's own "
              "nine progressive attainments?",
         "opts": [
             "They are unrelated categories",
             "They represent adjacent stages — the first four and next "
             "four of the same nine-stage sequence",
             "The formless liberations come before the absorptions",
             "They are identical attainments under different names"],
         "correct": 1,
         "expl": "A meaningful, not arbitrary, substitution between the "
                 "two companion discourses' ninth items."},
        {"q": "What position does this discourse's ninth quality "
              "occupy between AN 10.8 and AN 10.10?",
         "opts": [
             "The most basic of the three",
             "A middle position — subtler than ordinary jhāna, but "
             "still meditative attainment rather than cognitive "
             "knowledge",
             "Identical to AN 10.10's ninth item",
             "Unrelated to either companion discourse"],
         "correct": 1,
         "expl": "Between absorption and the cognitive knowledges named "
                 "next."},
        {"q": "What verb governs this discourse's ninth quality, "
              "echoing earlier vocabulary in this project?",
         "opts": [
             "&lsquo;Understand with wisdom&rsquo;",
             "&lsquo;Have direct meditative experience of&rsquo;, "
             "echoing the &lsquo;kāyasakkhī&rsquo; vocabulary from AN "
             "9.43",
             "&lsquo;Merely believe in&rsquo;",
             "&lsquo;Teach to others&rsquo;"],
         "correct": 1,
         "expl": "The same embodied-experience vocabulary met earlier "
                 "in this project."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching AN 10.8."},
    ],
    marginalia=[
        ("One item swapped", [
            "not the four absorptions,",
            "but the formless liberations &mdash;",
            "nine others unchanged",
        ]),
        ("Adjacent stages", [
            "the first four, then the",
            "next four of nine attainments &mdash;",
            "a meaningful pairing",
        ]),
        ("A middle position", [
            "subtler than jhāna,",
            "not yet the knowledges &mdash;",
            "between 10.8, 10.10",
        ]),
        ("Cross-references", [
            "AN 9.43 &middot; the same embodied-experience vocabulary, "
            "kāyasakkhī",
            "AN 10.8 &middot; previous, the same nine qualities with "
            "the four absorptions",
            "AN 10.10 &middot; next, the same nine qualities with the "
            "three knowledges",
        ]),
    ],
    further=[
        '<a href="%s/an10.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.8.html">AN 10.8 &middot; Inspiring All Around: the Absorptions</a> '
        "&mdash; previous.",
        '<a href="an-10.10.html">AN 10.10 &middot; Inspiring All Around: the Three '
        "Knowledges</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.10 — Samajīvinasutta (Three Knowledges version) — closes ch.1
# Anisaṁsavagga
# --------------------------------------------------------------------------- #
page(
    10, "Samajīvina", "Inspiring All Around: the Three Knowledges",
    vagga=VAGGA_1,
    meta_title=("AN 10.10 — Inspiring All Around: the Three Knowledges "
                "| Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the third of three &lsquo;inspiring all around&rsquo; "
        "discourses, closing this chapter with the classic three "
        "knowledges as its shared ninth and tenth qualities combined. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical nine qualities as AN 10.8-9, with the "
                 "three knowledges closing the set"),
        ("Length", "~2 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Anisaṁsavagga</em>, the first chapter of the "
         "Tens; the source's own untranslated closing verse names all "
         "ten discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "closes a clean three-discourse set with the "
                       "canon's most classic threefold knowledge"),
    ],
    why=(
        "The same nine qualities as AN 10.8 and AN 10.9 recur, closing "
        "this chapter with the three knowledges &mdash; recollecting "
        "past lives, clairvoyance regarding others' rebirth, and the "
        "ending of defilements &mdash; the classic threefold "
        "attainment traditionally associated with the Buddha's own "
        "night of awakening."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant complete in faith, ethics, learning, teaching "
            "ability, assembly attendance, teaching with assurance, "
            "training expertise, forest dwelling, and the classic three "
            "knowledges &mdash; recollection of past lives, clairvoyance "
            "regarding others' rebirth, and the ending of defilements "
            "&mdash; is &lsquo;impressive all around.&rsquo;"]),
        ("The identical nine, a third substitution", [
            "This discourse repeats AN 10.8 and AN 10.9's first eight "
            "qualities without change, but its ninth and tenth items "
            "merge into what the tradition names as a single unit: the "
            "three knowledges (tevijjā), here spread across two "
            "positions in the list rather than compressed into one, as "
            "AN 10.8 and AN 10.9 each kept a single ninth item separate "
            "from the tenth."]),
        ("The canon's most classic threefold attainment", [
            "Where AN 10.8's absorptions and AN 10.9's formless "
            "liberations are meditative accomplishments, the three "
            "knowledges are traditionally the specific content "
            "attributed to the Buddha's own awakening night: recalling "
            "his own past lives in the first watch, seeing other beings' "
            "rebirths according to their deeds in the second, and "
            "realizing the ending of defilements in the third."]),
        ("Closing a deliberate ascending sequence", [
            "Read together, this three-discourse set moves through "
            "increasingly specific and traditionally weighty "
            "attainments: ordinary jhāna mastery at AN 10.8, subtler "
            "formless liberation at AN 10.9, and finally the canon's "
            "own signature threefold knowledge at AN 10.10, closing both "
            "this small set and the entire chapter. With this "
            "discourse, <em>Anisaṁsavagga</em> closes; the source's own "
            "untranslated colophon and chapter-summary verse name all "
            "ten discourses by their opening words."]),
    ],
    terms=[
        ("samantapāsādiko",
         "&ldquo;impressive all around&rdquo; &mdash; the shared "
         "closing declaration for this entire three-discourse set."),
        ("pubbenivāsaṁ anussarati",
         "&ldquo;recollect their many kinds of past lives&rdquo; "
         "&mdash; the first of the three knowledges, traditionally "
         "attained in the first watch of the Buddha's awakening night."),
        ("dibbena cakkhunā visuddhena atikkantamānusakena satte "
         "passati cavamāne upapajjamāne",
         "&ldquo;with clairvoyance that is purified and superhuman, see "
         "sentient beings passing away and being reborn&rdquo; &mdash; "
         "the second knowledge, traditionally the second watch."),
        ("āsavānaṁ khayā",
         "&ldquo;due to the ending of defilements&rdquo; &mdash; the "
         "third knowledge, closing the set and traditionally the third "
         "watch of the awakening night."),
        ("anisaṁsavaggo paṭhamo",
         "&ldquo;the first chapter, Anisaṁsavagga, is finished&rdquo; "
         "&mdash; the source's own untranslated colophon closing this "
         "chapter."),
    ],
    text_intro=(
        "The discourse in full: the same nine qualities as AN 10.8-9, "
        "closing with the three knowledges. The source's own closing "
        "colophon and chapter-summary verse are untranslated in the "
        "English and are described rather than quoted here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten qualities, closing with the three knowledges"),
        ("p", "&sect;1", "an10.10:1.1-3.3"),
    ],
    quiz=[
        {"q": "What closes this discourse's list, replacing AN 10.8's "
              "single ninth item?",
         "opts": [
             "A single new meditative attainment",
             "The three knowledges — recollecting past lives, "
             "clairvoyance regarding rebirth, and the ending of "
             "defilements — spread across two positions",
             "Nothing; the list ends at nine items",
             "A repeat of AN 10.9's formless liberations"],
         "correct": 1,
         "expl": "The classic threefold attainment, occupying what "
                 "were separate ninth and tenth positions in the "
                 "earlier two discourses."},
        {"q": "What is the traditional significance of the three "
              "knowledges?",
         "opts": [
             "They are a minor, rarely mentioned attainment",
             "They are traditionally the specific content of the "
             "Buddha's own awakening night, one per watch",
             "They apply only to laypeople",
             "They contradict the four absorptions"],
         "correct": 1,
         "expl": "The canon's most classic and weighty threefold "
                 "attainment."},
        {"q": "How does this three-discourse set progress, according "
              "to the guide?",
         "opts": [
             "No progression; all three are identical in weight",
             "Through increasingly specific and traditionally weighty "
             "attainments — jhāna, then formless liberation, then the "
             "three knowledges",
             "From most advanced to least advanced",
             "Randomly, with no discernible order"],
         "correct": 1,
         "expl": "A deliberate ascending sequence closing on the "
                 "canon's own signature attainment."},
        {"q": "What does this discourse close, and how?",
         "opts": [
             "Nothing; the chapter continues past it",
             "<em>Anisaṁsavagga</em>, the first chapter, with an "
             "untranslated colophon and uddāna verse naming all ten "
             "discourses",
             "The entire nipāta",
             "Only this single discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "What is traditionally attained in the second watch of "
              "the awakening night?",
         "opts": [
             "Recollection of past lives",
             "Clairvoyance regarding other beings' rebirth according "
             "to their deeds",
             "The ending of defilements",
             "The four absorptions"],
         "correct": 1,
         "expl": "The second of the three knowledges, following past-"
                 "life recollection and preceding the ending of "
                 "defilements."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching AN 10.8 and AN "
                 "10.9."},
    ],
    marginalia=[
        ("The classic threefold", [
            "past lives, others' rebirth,",
            "defilements ended &mdash;",
            "the awakening night itself",
        ]),
        ("An ascending set", [
            "jhāna, then formless,",
            "then the night's own three lights &mdash;",
            "closing on the deepest",
        ]),
        ("Closing the first chapter", [
            "Anisaṁsavaggo,",
            "finished &mdash; ten discourses",
            "named in its own verse",
        ]),
        ("Cross-references", [
            "AN 10.8, AN 10.9 &middot; the same nine qualities under "
            "two earlier ninth items",
            "AN 10.9 &middot; previous",
            "AN 10.11 &middot; next, opening ch.2, Nāthavagga",
        ]),
    ],
    further=[
        '<a href="%s/an10.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.9.html">AN 10.9 &middot; Inspiring All Around: the Peaceful '
        "Liberations</a> &mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# ch.2 — Nāthavagga (AN 10.11-20)
# --------------------------------------------------------------------------- #
VAGGA_2 = "<em>Nāthavagga</em> &mdash; the second chapter of the Tens"


# --------------------------------------------------------------------------- #
# AN 10.11 — Senāsanasutta
# --------------------------------------------------------------------------- #
page(
    11, "Senāsana", "Lodgings",
    vagga=VAGGA_2,
    meta_title="AN 10.11 — Lodgings | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Senāsanasutta, opening this chapter with five factors of "
        "a ready mendicant crossed against five factors of a suitable "
        "lodging. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five personal factors, then five factors of a "
                 "lodging, combined into a ten-item total"),
        ("Length", "~2 minutes to read"),
        ("Ten by combination, not by one flat list", "This chapter's "
         "number is reached the same way as AN 9.21's three-particular "
         "comparison — two distinct five-item sets, combined"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; two "
                       "clean fivefold lists, worth reading for how "
                       "they complement each other"),
    ],
    why=(
        "A mendicant with five factors &mdash; faith in the Buddha's "
        "awakening, good health, honesty, energy, and wisdom &mdash; "
        "who uses a lodging with five factors of its own &mdash; "
        "convenient location, quiet, freedom from pests, easy "
        "requisites, and learned senior mendicants nearby &mdash; will "
        "soon realize freedom."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant with five personal factors, using a lodging "
            "with five factors of its own, will soon realize the "
            "undefiled freedom of heart and freedom by wisdom in this "
            "very life."]),
        ("Five personal factors, an internal readiness", [
            "The mendicant's own five factors span the inner life "
            "needed for practice: confidence in the Buddha, physical "
            "health fit for meditation, honesty with teacher and "
            "companions, roused energy, and the wisdom that sees "
            "arising and passing away."]),
        ("Five factors of place, an external readiness", [
            "The lodging's own five factors are entirely practical: "
            "neither too far nor too near, undisturbed by day and "
            "quiet by night, free of biting insects and reptiles, easy "
            "requisites, and &mdash; distinctively &mdash; the presence "
            "of learned senior mendicants able to answer questions and "
            "clarify doubts."]),
        ("Ten by combination, this chapter's own method", [
            "Like AN 9.21's three-particular comparison earlier in this "
            "project, this discourse reaches its ten-count not through "
            "one flat list but by combining two distinct five-item "
            "sets &mdash; inner readiness and outer circumstance "
            "&mdash; suggesting that neither alone is sufficient "
            "without the other."]),
    ],
    terms=[
        ("saddho hoti, saddahati tathāgatassa bodhiṁ",
         "&ldquo;has faith in the Realized One's awakening&rdquo; "
         "&mdash; the first of the mendicant's five factors, using the "
         "standard formula for confidence in the Buddha."),
        ("appābādho hoti appātaṅko",
         "&ldquo;rarely ill or unwell&rdquo; &mdash; the second "
         "factor, physical health specifically suited to meditation."),
        ("nātidūre hoti nāccāsanne gamanāgamanasampannaṁ",
         "&ldquo;neither too far nor too near, but convenient for "
         "coming and going&rdquo; &mdash; the lodging's first factor."),
        ("bahussutā āgatāgamā dhammadharā vinayadharā mātikādharā",
         "&ldquo;very learned, inheritors of the heritage, who have "
         "memorized the teachings, the monastic law, and the "
         "outlines&rdquo; &mdash; the lodging's fifth and final factor, "
         "naming the presence of learned senior mendicants."),
        ("āsavānaṁ khayā... sacchikatvā upasampajja viharati",
         "&ldquo;realize the undefiled freedom of heart and freedom by "
         "wisdom... due to the ending of defilements&rdquo; &mdash; the "
         "outcome this discourse's combined ten factors point toward."),
    ],
    text_intro=(
        "The discourse in full: five personal factors, then five "
        "factors of a suitable lodging. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Five personal factors"),
        ("p", "&sect;1", "an10.11:1.1-2.8"),
        ("h3", "Five factors of a lodging"),
        ("p", "&sect;2", "an10.11:3.1-3.11"),
    ],
    quiz=[
        {"q": "What are the mendicant's own five factors?",
         "opts": [
             "Faith, good health, honesty, energy, and wisdom",
             "The five hindrances",
             "The five aggregates",
             "The five precepts"],
         "correct": 0,
         "expl": "Inner readiness for practice."},
        {"q": "What distinctive fifth factor does a suitable lodging "
              "have, according to this discourse?",
         "opts": [
             "Expensive furnishings",
             "The presence of learned senior mendicants able to answer "
             "questions and clarify doubts",
             "A large garden",
             "Proximity to a city center"],
         "correct": 1,
         "expl": "Access to guidance, not merely physical comfort."},
        {"q": "How does this discourse reach its ten-item total?",
         "opts": [
             "Through a single flat list of ten items",
             "By combining two distinct five-item sets — the "
             "mendicant's own factors and the lodging's factors",
             "By listing ten different lodgings",
             "Through a narrative with ten characters"],
         "correct": 1,
         "expl": "The same combination method already met at AN 9.21."},
        {"q": "What outcome does this discourse promise for someone "
              "with all ten factors?",
         "opts": [
             "Wealth and long life",
             "Soon realizing the undefiled freedom of heart and "
             "freedom by wisdom",
             "Rebirth as a deity",
             "Fame among laypeople"],
         "correct": 1,
         "expl": "Full liberation, promised as a near-term result of "
                 "combined inner and outer readiness."},
        {"q": "According to the guide, what does the combination of "
              "personal and lodging factors suggest?",
         "opts": [
             "That the lodging's qualities matter more than the "
             "person's",
             "That neither inner readiness nor outer circumstance alone "
             "is sufficient without the other",
             "That lodging conditions are irrelevant to practice",
             "That personal factors alone guarantee awakening"],
         "correct": 1,
         "expl": "A deliberate pairing of internal and external "
                 "conditions."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, opening this chapter."},
    ],
    marginalia=[
        ("Five factors, inward", [
            "faith, health, honesty,",
            "energy, and wisdom &mdash;",
            "readiness within",
        ]),
        ("Five factors, outward", [
            "not too far, not too near,",
            "quiet, easy needs, and",
            "learned mendicants nearby",
        ]),
        ("Ten by combination", [
            "inner and outer both",
            "needed together &mdash;",
            "neither one alone",
        ]),
        ("Cross-references", [
            "AN 9.21 &middot; the same ten-by-combination method",
            "AN 10.10 &middot; previous chapter's closing page",
            "AN 10.12 &middot; next, Five Factors",
        ]),
    ],
    further=[
        '<a href="%s/an10.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.10.html">AN 10.10 &middot; Inspiring All Around: the Three '
        "Knowledges</a> &mdash; previous.",
        '<a href="an-10.12.html">AN 10.12 &middot; Five Factors</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.12 — Dasadhammasutta (Five Factors)
# --------------------------------------------------------------------------- #
page(
    12, "Dasadhamma", "Five Factors",
    vagga=VAGGA_2,
    meta_title="AN 10.12 — Five Factors | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "this discourse naming the &lsquo;supreme person&rsquo; — one "
        "who has given up the five hindrances and possesses the five "
        "aggregates of an adept, closing with a summary verse. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five things given up, five things possessed, then a "
                 "closing verse restating both"),
        ("Length", "~1 minute to read"),
        ("A verse closing a prose teaching", "This discourse is "
         "unusual for restating its own prose content in verse "
         "immediately afterward, within the same page"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, naming a well-known fivefold Dhamma "
                       "category"),
    ],
    why=(
        "A mendicant who has given up the five hindrances and possesses "
        "the five aggregates of an adept &mdash; ethics, immersion, "
        "wisdom, freedom, and the knowledge and vision of freedom "
        "&mdash; is called consummate, accomplished, a supreme person, "
        "a teaching then restated in verse."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has given up the five hindrances and "
            "possesses the five aggregates of an adept &mdash; ethics, "
            "immersion, wisdom, freedom, and the knowledge and vision "
            "of freedom &mdash; is called consummate, accomplished, a "
            "supreme person."]),
        ("Five given up, a familiar list", [
            "The five things given up are the standard hindrances "
            "already met repeatedly in this project: sensual desire, "
            "ill will, dullness and drowsiness, restlessness and "
            "remorse, and doubt."]),
        ("Five possessed, the aggregates of an adept", [
            "The five things possessed are the classic "
            "&lsquo;dhammakkhandha,&rsquo; the fivefold Dhamma body "
            "attributed to an adept (asekha, one beyond further "
            "training): ethics, immersion, wisdom, freedom, and "
            "knowledge and vision of freedom &mdash; the same final "
            "term that closed AN 10.1's entire ten-link chain, here "
            "serving as the culmination of just five."]),
        ("Prose, then verse, of the same content", [
            "This discourse's distinctive structure restates its own "
            "prose teaching in verse immediately afterward &mdash; not "
            "a separate teaching but the identical ten-item content "
            "(five given up, five possessed) recast in poetic form "
            "within the same page, a compact demonstration of how the "
            "same doctrine could travel in either register."]),
    ],
    terms=[
        ("kevalī, kevalaṁ, uttamapuriso",
         "&ldquo;consummate, accomplished, a supreme person&rdquo; "
         "&mdash; the discourse's own title concept, the outcome of "
         "having given up five things and gained five more."),
        ("kāmacchando, byāpādo, thinamiddhaṁ, uddhaccakukkuccaṁ, "
         "vicikicchā",
         "the five hindrances &mdash; the same standard list already "
         "met repeatedly in this project, here what must be given up."),
        ("asekhena sīlakkhandhena samannāgato hoti",
         "&ldquo;has the entire spectrum of an adept's ethics&rdquo; "
         "&mdash; the first of the five aggregates possessed, naming "
         "the standard of one beyond further training."),
        ("vimuttiñāṇadassanakkhandha",
         "&ldquo;the aggregate of knowledge and vision of freedom"
         "&rdquo; &mdash; the fifth and final aggregate, the same "
         "closing term as AN 10.1's ten-link chain."),
        ("kevalī tehi vuccati",
         "&ldquo;they're called &lsquo;consummate&rsquo;&rdquo; "
         "&mdash; the closing verse's own final line, restating the "
         "prose teaching's conclusion in verse."),
    ],
    text_intro=(
        "The discourse in full: five things given up, five things "
        "possessed, then a closing verse. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Five given up, five possessed"),
        ("p", "&sect;1", "an10.12:1.1-3.1"),
        ("h3", "The same teaching, in verse"),
        ("p", "&sect;2", "an10.12:4.1-6.4"),
    ],
    quiz=[
        {"q": "What five things must be given up, according to this "
              "discourse?",
         "opts": [
             "The five lower fetters",
             "The five hindrances",
             "The five aggregates",
             "The five precepts"],
         "correct": 1,
         "expl": "The standard hindrance list, already met repeatedly "
                 "in this project."},
        {"q": "What five things must be possessed?",
         "opts": [
             "Five kinds of wealth",
             "The aggregates of an adept: ethics, immersion, wisdom, "
             "freedom, and knowledge and vision of freedom",
             "The five formless attainments",
             "Five monastic robes"],
         "correct": 1,
         "expl": "The classic &lsquo;dhammakkhandha&rsquo;, the "
                 "fivefold Dhamma body."},
        {"q": "What is distinctive about this discourse's structure?",
         "opts": [
             "It has no structure at all",
             "It restates its own prose teaching in verse immediately "
             "afterward, within the same page",
             "It is entirely in verse from the start",
             "It contradicts itself between prose and verse"],
         "correct": 1,
         "expl": "The same content in two registers, side by side."},
        {"q": "What term closes both this discourse's five aggregates "
              "and AN 10.1's entire ten-link chain?",
         "opts": [
             "Immersion", "Ethics",
             "The knowledge and vision of freedom",
             "Rapture"],
         "correct": 2,
         "expl": "The same culminating term, here closing a shorter "
                 "fivefold list."},
        {"q": "What title does a mendicant with these ten qualities "
              "earn?",
         "opts": [
             "Impressive all around",
             "Consummate, accomplished, a supreme person",
             "Worthy of offerings",
             "A direct witness"],
         "correct": 1,
         "expl": "This discourse's own distinctive closing title, "
                 "different from AN 10.8-10's &lsquo;impressive all "
                 "around&rsquo;."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching most discourses "
                 "in this chapter."},
    ],
    marginalia=[
        ("Five given up, familiar", [
            "desire, ill will, dullness,",
            "restlessness, doubt &mdash;",
            "the standard hindrances",
        ]),
        ("Five possessed, the adept's own", [
            "ethics, immersion, wisdom,",
            "freedom, and knowledge",
            "of freedom itself",
        ]),
        ("Prose, then the same in verse", [
            "the teaching twice told &mdash;",
            "once plain, once poetic,",
            "the same ten counted",
        ]),
        ("Cross-references", [
            "AN 10.1 &middot; the same closing term, there ending a "
            "ten-link chain",
            "AN 10.11 &middot; previous",
            "AN 10.13 &middot; next, Fetters",
        ]),
    ],
    further=[
        '<a href="%s/an10.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.11.html">AN 10.11 &middot; Lodgings</a> &mdash; previous.',
        '<a href="an-10.13.html">AN 10.13 &middot; Fetters</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.13 — Saṁyojanasutta
# --------------------------------------------------------------------------- #
page(
    13, "Saṁyojana", "Fetters",
    vagga=VAGGA_2,
    meta_title="AN 10.13 — Fetters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Saṁyojanasutta, a bare list of the ten fetters — the same "
        "five lower and five higher fetters already met separately, "
        "now combined into one complete list. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list, no narrative and no similes"),
        ("Length", "~30 seconds to read"),
        ("Ten by union, not by a new list", "This discourse simply "
         "combines the two five-item fetter lists already met "
         "separately in AN 9, without adding new content"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the briefest and simplest discourse in this "
                       "chapter so far"),
    ],
    why=(
        "The ten fetters are the five lower fetters &mdash; "
        "substantialist view, doubt, misapprehension of precepts and "
        "observances, sensual desire, and ill will &mdash; and the "
        "five higher fetters &mdash; desire for rebirth in the realm "
        "of luminous form, desire for rebirth in the formless realm, "
        "conceit, restlessness, and ignorance."),
    guide=[
        ("The teaching in one sentence", [
            "The ten fetters are the five lower fetters (substantialist "
            "view, doubt, misapprehension of precepts and observances, "
            "sensual desire, ill will) and the five higher fetters "
            "(desire for form-realm rebirth, desire for formless-realm "
            "rebirth, conceit, restlessness, ignorance)."]),
        ("Nothing new, simply combined", [
            "This discourse introduces no content this project hasn't "
            "already met: both five-item lists appeared separately at "
            "AN 9.67 (lower fetters) and AN 9.70 (higher fetters), each "
            "there paired with the four kinds of mindfulness "
            "meditation as their remedy. Here the two lists are simply "
            "placed side by side to reach this chapter's own tens."]),
        ("A milestone this project has tracked repeatedly", [
            "Ending the five lower fetters marks non-return; ending all "
            "ten marks arahantship &mdash; the same graduated milestone "
            "traced with far more granularity at AN 9.12's nine-fold "
            "classification of non-returners, and named again as the "
            "goal of AN 9.35's gradualist cow simile."]),
        ("A bare list, deliberately unadorned", [
            "Unlike most discourses so far in this chapter, this one "
            "offers no simile, no narrative, and no explanation of why "
            "each fetter binds &mdash; simply the complete inventory, "
            "trusting readers already familiar with both halves from "
            "elsewhere in this project to recognize the whole."]),
    ],
    terms=[
        ("dasa saṁyojanāni",
         "&ldquo;ten fetters&rdquo; &mdash; this discourse's own title "
         "term, the union of the two five-item lists already met "
         "separately."),
        ("pañcorambhāgiyāni saṁyojanāni",
         "&ldquo;the five lower fetters&rdquo; &mdash; identical to "
         "the list given in full at AN 9.67."),
        ("pañcuddhambhāgiyāni saṁyojanāni",
         "&ldquo;the five higher fetters&rdquo; &mdash; identical to "
         "the list given in full at AN 9.70."),
        ("sakkāyadiṭṭhi",
         "&ldquo;substantialist view&rdquo; &mdash; the first of the "
         "five lower fetters, opening the complete tenfold list."),
        ("avijjā",
         "&ldquo;ignorance&rdquo; &mdash; the tenth and final fetter, "
         "closing the complete list."),
    ],
    text_intro=(
        "The discourse in full: the ten fetters, combining the two "
        "five-item lists already met separately. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten fetters"),
        ("p", "&sect;1", "an10.13:1.1-2.4"),
    ],
    quiz=[
        {"q": "What ten fetters does this discourse name?",
         "opts": [
             "Ten entirely new items not met before",
             "The five lower fetters and the five higher fetters, each "
             "already met separately at AN 9.67 and AN 9.70",
             "The five hindrances plus five shackles of the heart",
             "The ten qualities that serve as protector"],
         "correct": 1,
         "expl": "A simple combination of two familiar lists, not new "
                 "content."},
        {"q": "Where has this project already met the five lower "
              "fetters and five higher fetters separately?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.67 (lower fetters) and AN 9.70 (higher fetters), "
             "each paired there with mindfulness meditation",
             "Only in a completely unrelated nipāta",
             "At AN 10.1, the opening discourse"],
         "correct": 1,
         "expl": "Both halves already given in full detail earlier in "
                 "this project."},
        {"q": "What milestone does ending all ten fetters mark?",
         "opts": [
             "Stream-entry", "Once-return",
             "Arahantship, full awakening",
             "Non-return only"],
         "correct": 2,
         "expl": "Ending the five lower fetters alone marks non-return; "
                 "all ten together marks full liberation."},
        {"q": "How does this discourse present its content, unlike "
              "most others so far in this chapter?",
         "opts": [
             "With an extended simile",
             "As a bare list, with no simile, narrative, or "
             "explanation of why each fetter binds",
             "As a narrative dialogue",
             "In verse throughout"],
         "correct": 1,
         "expl": "The briefest and simplest treatment in this chapter "
                 "so far."},
        {"q": "What is the tenth and final fetter named?",
         "opts": [
             "Sensual desire", "Conceit",
             "Ignorance", "Restlessness"],
         "correct": 2,
         "expl": "Closing the complete tenfold list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, the briefest in this chapter so far."},
    ],
    marginalia=[
        ("Two familiar lists, joined", [
            "view, doubt, rites clung to,",
            "desire, ill will &mdash; then",
            "form, formless, conceit, more",
        ]),
        ("Nothing new here", [
            "already met at",
            "AN 9.67, 9.70 &mdash;",
            "simply combined now",
        ]),
        ("A milestone, tracked before", [
            "five ends non-return;",
            "all ten, full awakening &mdash;",
            "the same goal, named again",
        ]),
        ("Cross-references", [
            "AN 9.67, AN 9.70 &middot; this discourse's two component "
            "lists, each given in full",
            "AN 9.12 &middot; the same milestone traced with far more "
            "granularity",
            "AN 10.12 &middot; previous",
            "AN 10.14 &middot; next, Hard-heartedness",
        ]),
    ],
    further=[
        '<a href="%s/an10.13/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.67.html">AN 9.67 &middot; Lower Fetters</a> &mdash; the first half '
        "of this discourse's list, given in full.",
        '<a href="an-9.70.html">AN 9.70 &middot; Higher Fetters</a> &mdash; the second half '
        "of this discourse's list, given in full.",
        '<a href="an-10.12.html">AN 10.12 &middot; Five Factors</a> &mdash; previous.',
        '<a href="an-10.14.html">AN 10.14 &middot; Hard-heartedness</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.14 — Cetokhilasutta (combined version)
# --------------------------------------------------------------------------- #
page(
    14, "Cetokhila", "Hard-heartedness",
    vagga=VAGGA_2,
    meta_title="AN 10.14 — Hard-heartedness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "this discourse combining the five kinds of hard-heartedness "
        "and five shackles of the heart into one ten-item teaching, "
        "closed by a waxing-and-waning moon simile. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Ten items combined (five hard-heartedness, five "
                 "shackles), given both destroyed and fulfilled, with a "
                 "moon simile for each direction"),
        ("Length", "~4 minutes to read"),
        ("Ten by union, like AN 10.13", "The same combination method "
         "as the fetters discourse, joining two five-item lists "
         "already met separately in AN 9"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "substantial, with a memorable simile closing "
                       "each half"),
    ],
    why=(
        "A mendicant who has not given up five kinds of hard-"
        "heartedness and not severed five shackles of the heart can "
        "expect only decline in skillful qualities, like the moon "
        "waning; one who has given up both sets can expect only "
        "growth, like the moon waxing."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has given up the five kinds of hard-"
            "heartedness (doubt about the Teacher, the teaching, the "
            "Saṅgha, the training, and anger at companions) and "
            "severed the five shackles of the heart (unresolved greed "
            "for sensual pleasures, the body, form, comfort and sleep, "
            "and rebirth as a god through practice) can expect only "
            "growth in skillful qualities."]),
        ("Ten by union, matching AN 10.13's method", [
            "As with the ten fetters at AN 10.13, this discourse "
            "combines two five-item lists this project has already met "
            "in full &mdash; the cetokhila from AN 9.71 and the cetaso "
            "vinibandha from AN 9.72, AN 9.82, and AN 9.92 &mdash; here "
            "joined into a single ten-item teaching for the first "
            "time."]),
        ("Both directions, and a moon for each", [
            "Unlike AN 10.13's bare list, this discourse gives both "
            "directions in full: what remains when the ten items "
            "aren't given up, and what results when they are, each "
            "closed by its own half of a single extended simile "
            "&mdash; the waning moon losing beauty, roundness, and "
            "luminosity night after night, and the waxing moon gaining "
            "them in exactly the same way."]),
        ("A vivid image for a familiar teaching", [
            "This is the first time this project has met a moon simile "
            "applied to the hard-heartedness and shackles teaching "
            "&mdash; the content itself unchanged from AN 9.71 and AN "
            "9.72's separate treatments, but framed here with an image "
            "of gradual, night-by-night change that neither earlier "
            "discourse used."]),
    ],
    terms=[
        ("cetokhilā, cetaso vinibandhā",
         "&ldquo;hard-heartedness, shackles of the heart&rdquo; "
         "&mdash; the two five-item lists this discourse combines, "
         "each already met separately in AN 9."),
        ("satthari kaṅkhati vicikicchati",
         "&ldquo;has doubts about the Teacher&rdquo; &mdash; the "
         "first of the five kinds of hard-heartedness, identical to "
         "AN 9.71's list."),
        ("iminā sīlena vā vatena vā tapena vā brahmacariyena vā "
         "devo vā bhavissāmi",
         "&ldquo;by this precept or observance or fervent austerity "
         "or spiritual practice, may I become one of the gods&rdquo; "
         "&mdash; the fifth shackle, identical to AN 9.72's list."),
        ("kāḷapakkhe candimā",
         "&ldquo;the moon in the waning fortnight&rdquo; &mdash; the "
         "simile for decline, its beauty and roundness diminishing "
         "night after night."),
        ("juṇhapakkhe candimā",
         "&ldquo;the moon in the waxing fortnight&rdquo; &mdash; the "
         "mirror-image simile for growth, gaining exactly what the "
         "waning moon loses."),
    ],
    text_intro=(
        "The discourse in full: ten combined items, given as both "
        "obstacle and remedy, each closed by a moon simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten items, not given up: decline"),
        ("p", "&sect;1", "an10.14:1.1-7.2"),
        ("h3", "Ten items, given up: growth"),
        ("p", "&sect;2", "an10.14:8.1-14.2"),
    ],
    quiz=[
        {"q": "What ten items does this discourse combine?",
         "opts": [
             "Ten entirely new items",
             "The five kinds of hard-heartedness and five shackles of "
             "the heart, each already met separately in AN 9",
             "The five lower and five higher fetters",
             "The five hindrances and five aggregates"],
         "correct": 1,
         "expl": "The same combination method as AN 10.13's ten "
                 "fetters, applied to a different pair of lists."},
        {"q": "What simile closes each half of this discourse?",
         "opts": [
             "A burning pile of twigs",
             "The waning moon for decline, the waxing moon for growth",
             "A tree lacking branches",
             "A stone post unmoved by storms"],
         "correct": 1,
         "expl": "A single extended image, split across both "
                 "directions of the teaching."},
        {"q": "How does this discourse's structure compare to AN "
              "10.13's ten fetters?",
         "opts": [
             "Identical brevity, with no simile",
             "Fuller — it gives both directions in full, each closed "
             "by its own half of a moon simile",
             "Even more compressed than AN 10.13",
             "Unrelated in structure"],
         "correct": 1,
         "expl": "A richer treatment than the bare list at AN 10.13."},
        {"q": "Where has this project already met the five kinds of "
              "hard-heartedness and five shackles of the heart "
              "separately?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.71 (hard-heartedness) and AN 9.72/9.82/9.92 "
             "(shackles of the heart)",
             "Only in a completely unrelated nipāta",
             "At AN 10.1, the opening discourse"],
         "correct": 1,
         "expl": "Both lists given in full detail multiple times "
                 "earlier in this project."},
        {"q": "What is new about this discourse's treatment, compared "
              "to those earlier ones?",
         "opts": [
             "The content itself changes significantly",
             "The moon simile — the first time this project has met "
             "this image applied to this particular teaching",
             "The remedy changes to right effort",
             "The obstacle-lists are shortened"],
         "correct": 1,
         "expl": "Same content, framed here with a vivid image of "
                 "gradual, night-by-night change."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, despite its substantial "
                 "length."},
    ],
    marginalia=[
        ("Ten items, combined", [
            "hard-heartedness, five;",
            "shackles of the heart, five &mdash;",
            "joined as one teaching",
        ]),
        ("A moon for each direction", [
            "waning, night by night,",
            "loses light and roundness &mdash;",
            "waxing gains the same",
        ]),
        ("Old content, new image", [
            "the same ten items met",
            "before &mdash; now framed by",
            "the moon's own cycle",
        ]),
        ("Cross-references", [
            "AN 9.71 &middot; the same five kinds of hard-heartedness, "
            "given in full",
            "AN 9.72 &middot; the same five shackles of the heart, "
            "given in full",
            "AN 10.13 &middot; previous, the same combination method",
            "AN 10.15 &middot; next, Diligence",
        ]),
    ],
    further=[
        '<a href="%s/an10.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.71.html">AN 9.71 &middot; Hard-heartedness</a> &mdash; the first '
        "half of this discourse's list, given in full.",
        '<a href="an-9.72.html">AN 9.72 &middot; Shackles of the Heart</a> &mdash; the '
        "second half of this discourse's list, given in full.",
        '<a href="an-10.13.html">AN 10.13 &middot; Fetters</a> &mdash; previous.',
        '<a href="an-10.15.html">AN 10.15 &middot; Diligence</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.15 — Appamādasutta
# --------------------------------------------------------------------------- #
page(
    15, "Appamāda", "Diligence",
    vagga=VAGGA_2,
    meta_title="AN 10.15 — Diligence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Appamādasutta, the famous &lsquo;diligence is the root of "
        "all skillful qualities&rsquo; teaching, expanded here into ten "
        "cascading similes. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Ten similes, each closing with the identical refrain "
                 "about diligence"),
        ("Length", "~2 minutes to read"),
        ("A famous teaching, expanded to ten", "This teaching appears "
         "elsewhere in the canon far more briefly; this version "
         "multiplies its similes to reach this nipāta's own count"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "vivid, cumulative list of images, pleasant to "
                       "read in sequence"),
    ],
    why=(
        "All skillful qualities are rooted in diligence and meet at "
        "diligence, just as the Buddha is the best of all beings, an "
        "elephant's footprint the largest, a roof's peak where all "
        "rafters meet, the best root, heartwood, and flower each named, "
        "a wheel-turning monarch supreme over lesser kings, the moon "
        "outshining the stars, the autumn sun dispelling darkness, and "
        "all great rivers flowing to the ocean."),
    guide=[
        ("The teaching in one sentence", [
            "All skillful qualities are rooted in diligence and meet "
            "at diligence, which is said to be the best of them all "
            "&mdash; a claim illustrated through ten different images "
            "of one thing standing supreme among many."]),
        ("A famous teaching, given its fullest treatment here", [
            "The core claim &mdash; diligence as the root of all "
            "skillful qualities &mdash; is one of the most quoted "
            "teachings in the canon, often appearing in much briefer "
            "form. This version develops it at unusual length, "
            "multiplying its similes specifically to reach ten, "
            "matching this nipāta's own number."]),
        ("Ten images, one shared logic", [
            "Each simile follows the identical structure: name "
            "something supreme in its category (footprint, roof-peak, "
            "root, heartwood, flower, monarch, moon, sun, river's "
            "destination), then apply the identical comparison &mdash; "
            "just as this excels, diligence excels among skillful "
            "qualities. The opening simile, the elephant's footprint, "
            "and the closing rivers-to-the-ocean image are all given "
            "in full; the six similes in between (root, heartwood, "
            "flower, monarch, moon, sun) are compressed to their "
            "images alone, trusting the refrain already established."]),
        ("From nature to kingship to cosmology", [
            "The similes range widely: two are botanical (root, "
            "heartwood, flower), one is political (the wheel-turning "
            "monarch), two are astronomical (moon, sun), and one is "
            "geographic (all rivers to the ocean) &mdash; a deliberately "
            "varied catalogue rather than similes drawn from a single "
            "domain, suggesting diligence's primacy is meant to be "
            "recognized from every possible angle."]),
    ],
    terms=[
        ("appamādamūlakā sabbe kusalā dhammā",
         "&ldquo;all skillful qualities are rooted in diligence&rdquo; "
         "&mdash; the discourse's own repeated refrain, closing every "
         "one of its ten similes."),
        ("hatthipadaṁ",
         "&ldquo;an elephant's footprint&rdquo; &mdash; the second "
         "simile, said to contain the footprints of all other walking "
         "creatures."),
        ("tagaramūlaṁ, lohitacandanaṁ, vassikaṁ",
         "&ldquo;spikenard... red sandalwood... jasmine&rdquo; &mdash; "
         "the best fragrant root, heartwood, and flower respectively, "
         "three consecutive botanical similes."),
        ("cakkavattī rājā",
         "&ldquo;a wheel-turning monarch&rdquo; &mdash; the seventh "
         "simile, supreme over all lesser kings who become his vassals."),
        ("gaṅgā yamunā aciravatī sarabhū mahī",
         "&ldquo;the Ganges, Yamunā, Aciravatī, Sarabhū, and Mahī"
         "&rdquo; &mdash; the five named great rivers of the tenth and "
         "final simile, all flowing toward the ocean."),
    ],
    text_intro=(
        "The discourse in full: ten similes, each closing with the "
        "same refrain about diligence. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten similes of one thing supreme among many"),
        ("p", "&sect;1", "an10.15:1.1-1.2"),
        ("p", "&sect;2", "an10.15:2.1-2.2"),
        ("p", "&sect;3", "an10.15:3.1-3.2"),
        ("p", "&sect;4", "an10.15:4.1-4.2"),
        ("p", "&sect;5", "an10.15:5.1-5.2"),
        ("p", "&sect;6", "an10.15:6.1-6.2"),
        ("p", "&sect;7", "an10.15:7.1-7.2"),
        ("p", "&sect;8", "an10.15:8.1-8.2"),
        ("p", "&sect;9", "an10.15:9.1-9.2"),
        ("p", "&sect;10", "an10.15:10.1-10.2"),
    ],
    quiz=[
        {"q": "What is this discourse's central claim?",
         "opts": [
             "That wisdom is the root of all skillful qualities",
             "That all skillful qualities are rooted in diligence and "
             "meet at diligence",
             "That ethics alone matters",
             "That immersion is unnecessary"],
         "correct": 1,
         "expl": "One of the canon's most quoted teachings, developed "
                 "here at unusual length."},
        {"q": "How does this version of the teaching compare to its "
              "more common appearances elsewhere in the canon?",
         "opts": [
             "Identical in every respect",
             "This version develops the teaching at unusual length, "
             "multiplying its similes specifically to reach ten",
             "This version is much shorter",
             "This version omits the core claim entirely"],
         "correct": 1,
         "expl": "Expanded specifically to match this nipāta's own "
                 "number."},
        {"q": "What domains do this discourse's ten similes draw from?",
         "opts": [
             "Only botanical images",
             "A deliberately varied range — nature, kingship, "
             "astronomy, and geography",
             "Only images of monastic life",
             "Only images related to fire"],
         "correct": 1,
         "expl": "Recognition of diligence's primacy from every "
                 "possible angle."},
        {"q": "Which similes are given in full, unlike the six in "
              "between?",
         "opts": [
             "Only the monarch and the moon",
             "The opening Buddha simile, the elephant's footprint, "
             "the roof-peak, and the closing rivers-to-the-ocean image",
             "None are given in full",
             "Only the botanical similes"],
         "correct": 1,
         "expl": "The five middle similes (root, heartwood, flower, "
                 "monarch, moon, sun) are compressed to their images "
                 "alone, sharing the same refrain."},
        {"q": "What five rivers does the tenth simile name?",
         "opts": [
             "Five unnamed rivers",
             "The Ganges, Yamunā, Aciravatī, Sarabhū, and Mahī",
             "Only the Ganges",
             "Five rivers not found in the canon elsewhere"],
         "correct": 1,
         "expl": "All flowing toward the ocean, the simile's own point "
                 "of comparison."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, structured entirely around "
                 "its similes."},
    ],
    marginalia=[
        ("One root, many images", [
            "elephant's footprint,",
            "roof-peak, root, heartwood, flower,",
            "monarch, moon, sun, rivers",
        ]),
        ("Ten similes, one refrain", [
            "&ldquo;all skillful qualities",
            "rooted in diligence&rdquo; &mdash;",
            "the same close, ten times",
        ]),
        ("Recognized from every angle", [
            "nature, kingship, sky,",
            "geography &mdash; diligence",
            "supreme in each domain",
        ]),
        ("Cross-references", [
            "AN 10.14 &middot; previous",
            "AN 10.16 &middot; next, Worthy of Offerings Dedicated to "
            "the Gods",
        ]),
    ],
    further=[
        '<a href="%s/an10.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.14.html">AN 10.14 &middot; Hard-heartedness</a> &mdash; previous.',
        '<a href="an-10.16.html">AN 10.16 &middot; Worthy of Offerings Dedicated to the '
        "Gods</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.16 — Āhuneyyasutta
# --------------------------------------------------------------------------- #
page(
    16, "Āhuneyya", "Worthy of Offerings Dedicated to the Gods",
    vagga=VAGGA_2,
    meta_title=("AN 10.16 — Worthy of Offerings Dedicated to the Gods | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Āhuneyyasutta, expanding this project's nine-fold "
        "classification of worthy individuals to ten by adding the "
        "Independent Buddha and splitting the ninth item in two. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list of ten kinds of person, no "
                 "narrative and no similes"),
        ("Length", "~30 seconds to read"),
        ("The fullest classification of worthy persons yet", "This "
         "list expands AN 9.10's nine individuals by adding the "
         "Independent Buddha and splitting its final &lsquo;lamb of "
         "the flock&rsquo; into four further gradations"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "dense classification, worth comparing directly "
                       "against AN 9.9-10"),
    ],
    why=(
        "Ten individuals are worthy of offerings, hospitality, "
        "donation, and reverent greeting, the supreme field of merit "
        "for the world: a fully awakened Buddha, an Independent "
        "Buddha, one freed both ways, one freed by wisdom, a direct "
        "witness, one attained to view, one freed by faith, a follower "
        "by faith, a follower of teachings, and a lamb of the flock."),
    guide=[
        ("The teaching in one sentence", [
            "Ten kinds of person are worthy of offerings and the "
            "supreme field of merit for the world: a fully awakened "
            "Buddha, an Independent Buddha, one freed both ways, one "
            "freed by wisdom, a direct witness, one attained to view, "
            "one freed by faith, a follower by faith, a follower of "
            "teachings, and a lamb of the flock."]),
        ("Expanding AN 9.9-10's nine to ten", [
            "This list builds directly on the nine-fold classification "
            "already met at AN 9.9 and AN 9.10 &mdash; the four pairs "
            "on the path to and fruit of awakening, plus a ninth member "
            "&mdash; but reaches ten by two changes: adding an "
            "Independent Buddha (paccekabuddha) at the very top, and "
            "expanding the categories describing those still on the "
            "path with several further gradations by conviction and "
            "understanding."]),
        ("Two kinds of Buddha, distinguished", [
            "This discourse is the first in this project to "
            "distinguish a fully awakened Buddha (sammāsambuddha) from "
            "an Independent Buddha (paccekabuddha) &mdash; one who "
            "awakens without a living teacher but, unlike a "
            "sammāsambuddha, does not establish a teaching for others "
            "to follow to the same awakening."]),
        ("Terms already met, now assembled together", [
            "Several items in this list are already familiar from this "
            "project's own Sāmaññavagga chapter (AN 9.42-51): "
            "&lsquo;freed both ways&rsquo; and &lsquo;freed by "
            "wisdom&rsquo; matched AN 9.44-45's terms exactly, and "
            "&lsquo;direct witness&rsquo; matches AN 9.43's own "
            "kāyasakkhī &mdash; there defined through the nine "
            "progressive attainments, here simply named as points on "
            "a single graded scale."]),
    ],
    terms=[
        ("sammāsambuddho, paccekabuddho",
         "&ldquo;a fully awakened Buddha... an Independent Buddha"
         "&rdquo; &mdash; the first two of the ten, distinguishing a "
         "teaching Buddha from one who awakens without establishing a "
         "path for others."),
        ("ubhatobhāgavimutto, paññāvimutto, kāyasakkhī",
         "&ldquo;one freed both ways, one freed by wisdom, a direct "
         "witness&rdquo; &mdash; three terms identical to those defined "
         "through the nine attainments at AN 9.43-45."),
        ("diṭṭhippatto",
         "&ldquo;one attained to view&rdquo; &mdash; a further "
         "gradation not previously named in this project, describing "
         "someone who has seen the truth but not yet fully realized "
         "freedom."),
        ("saddhāvimutto, saddhānusārī, dhammānusārī",
         "&ldquo;one freed by faith, a follower by faith, a follower "
         "of teachings&rdquo; &mdash; three further gradations "
         "expanding what AN 9.9-10 named simply as the &lsquo;one "
         "practicing&rsquo; for each fruit."),
        ("gotrabhū",
         "&ldquo;a lamb of the flock&rdquo; &mdash; the same "
         "distinctive translation choice already met at AN 9.10, "
         "closing this expanded list."),
    ],
    text_intro=(
        "The discourse in full: ten kinds of person worthy of "
        "offerings, expanding AN 9.9-10's nine-fold classification. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten worthy of offerings"),
        ("p", "&sect;1", "an10.16:1.1-1.4"),
    ],
    quiz=[
        {"q": "What ten kinds of person does this discourse name?",
         "opts": [
             "Ten monastic ranks",
             "A fully awakened Buddha, an Independent Buddha, and eight "
             "further gradations of practitioner",
             "Nine individuals repeated with no change",
             "Ten kinds of layperson"],
         "correct": 1,
         "expl": "An expansion of AN 9.9-10's nine-fold classification "
                 "by two members."},
        {"q": "How does this list expand AN 9.9-10's nine individuals "
              "to reach ten?",
         "opts": [
             "By simply repeating one item twice",
             "By adding an Independent Buddha and further subdividing "
             "the categories describing those still on the path",
             "By removing the four pairs entirely",
             "By adding a tenth unrelated topic"],
         "correct": 1,
         "expl": "Two structural changes distinguish this list from "
                 "the earlier nine-fold version."},
        {"q": "What distinguishes an Independent Buddha "
              "(paccekabuddha) from a fully awakened Buddha, according "
              "to the guide?",
         "opts": [
             "No distinction exists",
             "An Independent Buddha awakens without a living teacher "
             "but does not establish a teaching for others to follow",
             "An Independent Buddha is inferior in every respect",
             "Only a fully awakened Buddha can attain nirvana"],
         "correct": 1,
         "expl": "Two related but distinct categories, named together "
                 "for the first time in this project."},
        {"q": "Which three terms in this list match items already "
              "defined at AN 9.43-45?",
         "opts": [
             "Only &lsquo;gotrabhū&rsquo;",
             "Freed both ways, freed by wisdom, and direct witness",
             "Fully awakened Buddha and Independent Buddha",
             "None of the terms overlap"],
         "correct": 1,
         "expl": "The same terms, there defined through the nine "
                 "progressive attainments, here simply named on a "
                 "graded scale."},
        {"q": "What ninth member, already met at AN 9.10, closes this "
              "expanded list?",
         "opts": [
             "The ordinary person (puthujjana)",
             "&lsquo;A lamb of the flock&rsquo; (gotrabhū)",
             "A follower of teachings",
             "One attained to view"],
         "correct": 1,
         "expl": "The same distinctive translation choice noted at AN "
                 "9.10."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare classification, without narrative frame."},
    ],
    marginalia=[
        ("Nine becomes ten", [
            "an Independent Buddha",
            "added, and the path itself",
            "split into finer stages",
        ]),
        ("Two kinds of Buddha", [
            "one teaches the path;",
            "one awakens alone,",
            "founding nothing new",
        ]),
        ("Terms already known", [
            "freed both ways, by wisdom,",
            "direct witness &mdash; met before,",
            "now simply listed",
        ]),
        ("Cross-references", [
            "AN 9.9, AN 9.10 &middot; the earlier nine-fold "
            "classification this list expands",
            "AN 9.43&ndash;45 &middot; three terms defined there "
            "through the nine attainments",
            "AN 10.15 &middot; previous",
            "AN 10.17 &middot; next, A Protector (1st)",
        ]),
    ],
    further=[
        '<a href="%s/an10.16/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.9.html">AN 9.9 &middot; Individuals</a> &mdash; the earlier '
        "nine-fold classification this list expands.",
        '<a href="an-9.10.html">AN 9.10 &middot; Worthy of Offerings Dedicated to the '
        "Gods</a> &mdash; the earlier nine-fold version of this same discourse type.",
        '<a href="an-10.15.html">AN 10.15 &middot; Diligence</a> &mdash; previous.',
        '<a href="an-10.17.html">AN 10.17 &middot; A Protector (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.17 — Nāthasutta (1st) — this chapter's own namesake
# --------------------------------------------------------------------------- #
page(
    17, "Nātha", "A Protector (1st)",
    vagga=VAGGA_2,
    meta_title="AN 10.17 — A Protector (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the first Nāthasutta, this chapter's own namesake, naming ten "
        "qualities that serve as a mendicant's own protector. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Ten qualities named as a mendicant's own protector, "
                 "each stated briefly"),
        ("Length", "~2 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own name to "
                               "the chapter, <em>Nāthavagga</em>, the "
                               "Chapter on a Protector"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "clear ten-item list, worth comparing with AN "
                       "10.18's fuller version"),
    ],
    why=(
        "A mendicant should live with a protector, since living without "
        "one is suffering; ten qualities themselves serve as that "
        "protector &mdash; ethical conduct, learning, good friends, "
        "openness to correction, diligence in communal duties, love of "
        "the teachings, energy, contentment, mindfulness, and wisdom."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant should live with a protector, since living "
            "without one is suffering, and ten qualities themselves "
            "serve as protector: ethical conduct, learning, good "
            "friends, openness to correction, diligence in communal "
            "duties, love of the teachings, energy, contentment, "
            "mindfulness, and wisdom."]),
        ("A protector that is not another person", [
            "The discourse's real turn is conceptual: rather than "
            "naming a teacher or companion as the protector a "
            "mendicant needs, it names ten internal qualities "
            "themselves as protective &mdash; the mendicant becomes "
            "their own safeguard by cultivating each in turn."]),
        ("This chapter's own namesake", [
            "This discourse lends its own subject, nātha, protector, "
            "to the chapter's name, Nāthavagga &mdash; though notably "
            "positioned seventh within the chapter rather than as its "
            "opener, following the same pattern already seen at AN "
            "9.24 within the Nines."]),
        ("A companion discourse follows immediately", [
            "AN 10.18, next, restates this identical ten-item list, "
            "elaborating what this discourse leaves as a bare listing "
            "&mdash; the source's own peyyāla compresses several "
            "elaborating phrases here that the following discourse "
            "spells out in full."]),
    ],
    terms=[
        ("nātho",
         "&ldquo;a protector&rdquo; &mdash; this discourse's own title "
         "term and the chapter's own name, referring not to another "
         "person but to internal qualities."),
        ("nāthakaraṇā dhammā",
         "&ldquo;qualities that serve as protector&rdquo; &mdash; the "
         "discourse's own framing for all ten items."),
        ("sīlavā hoti, pātimokkhasaṁvarasaṁvuto",
         "&ldquo;ethical, restrained in the monastic code&rdquo; "
         "&mdash; the first quality, opening the list."),
        ("kalyāṇamitto, kalyāṇasahāyo, kalyāṇasampavaṅko",
         "&ldquo;good friends, companions, and associates&rdquo; "
         "&mdash; the third quality, the same phrase already met at "
         "AN 9.1."),
        ("udayatthagāminiyā paññāya samannāgato",
         "&ldquo;wise... the wisdom of arising and passing away&rdquo; "
         "&mdash; the tenth and final quality, closing the list."),
    ],
    text_intro=(
        "The discourse in full, as it survives: ten qualities that "
        "serve as a mendicant's own protector. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten qualities that serve as protector"),
        ("p", "&sect;1", "an10.17:1.1-11.3"),
    ],
    quiz=[
        {"q": "What does this discourse claim serves as a mendicant's "
              "protector?",
         "opts": [
             "A senior teacher assigned to them",
             "Ten internal qualities themselves — ethics, learning, "
             "good friends, openness to correction, and more",
             "A physical amulet",
             "The monastery's walls"],
         "correct": 1,
         "expl": "A conceptual turn: the protector is not another "
                 "person but cultivated qualities."},
        {"q": "What does the discourse say about living without a "
              "protector?",
         "opts": [
             "It is preferable",
             "It is suffering",
             "It has no consequence",
             "It is impossible"],
         "correct": 1,
         "expl": "The discourse's own opening declaration, framing "
                 "why the ten qualities matter."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular", "Its own subject, nātha "
             "(protector), naming Nāthavagga",
             "A disciple's name", "A place name"],
         "correct": 1,
         "expl": "Though positioned seventh in the chapter, not as its "
                 "opener."},
        {"q": "What relationship does this discourse have with AN "
              "10.18?",
         "opts": [
             "No relationship at all",
             "AN 10.18 restates the identical ten-item list, "
             "elaborating what this discourse leaves compressed",
             "AN 10.18 contradicts this discourse",
             "AN 10.18 uses a completely different list"],
         "correct": 1,
         "expl": "A companion pair, this one abbreviated and the next "
                 "given in full."},
        {"q": "What is the third quality named?",
         "opts": [
             "Wisdom",
             "Good friends, companions, and associates",
             "Contentment",
             "Mindfulness"],
         "correct": 1,
         "expl": "The same phrase already met at AN 9.1, opening this "
                 "project's very first chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, opening this two-"
                 "discourse companion pair."},
    ],
    marginalia=[
        ("A protector, redefined", [
            "not a person guarding you,",
            "but ten qualities",
            "cultivated within",
        ]),
        ("A chapter's own name", [
            "nātha gives its name",
            "to Nāthavagga &mdash;",
            "though not as its opener",
        ]),
        ("A companion discourse next", [
            "the same ten qualities,",
            "elaborated in full &mdash;",
            "see AN 10.18",
        ]),
        ("Cross-references", [
            "AN 9.1 &middot; the same &ldquo;good friends&rdquo; "
            "phrase, this project's very first chapter",
            "AN 10.16 &middot; previous",
            "AN 10.18 &middot; next, the same list given in full",
        ]),
    ],
    further=[
        '<a href="%s/an10.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.16.html">AN 10.16 &middot; Worthy of Offerings Dedicated to the '
        "Gods</a> &mdash; previous.",
        '<a href="an-10.18.html">AN 10.18 &middot; A Protector (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.18 — Nāthasutta (2nd)
# --------------------------------------------------------------------------- #
page(
    18, "Nātha", "A Protector (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 10.18 — A Protector (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the second Nāthasutta, restating AN 10.17's ten protective "
        "qualities in full narrative frame, each one earning a "
        "mendicant the community's trust and instruction. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", SPEAKER),
        ("Form", "The identical ten qualities as AN 10.17, each now "
                 "elaborated with a shared social consequence"),
        ("Length", "~3 minutes to read"),
        ("Full elaboration, and a narrative frame", "Unlike AN 10.17's "
         "bare listing, this discourse gives a complete narrative "
         "opening and explains what each quality earns a mendicant"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the "
                       "same content as AN 10.17, worth reading for "
                       "what it adds"),
    ],
    why=(
        "The same ten protective qualities as AN 10.17 recur, each now "
        "explained: knowing a mendicant has fulfilled a given quality, "
        "senior, middle, and junior mendicants alike consider them "
        "worth advising and instructing, and being treated with such "
        "kindness, that mendicant can expect only growth, not decline."),
    guide=[
        ("The teaching in one sentence", [
            "The same ten qualities as AN 10.17 &mdash; ethics, "
            "learning, good friends, openness to correction, diligence "
            "in duties, love of the teachings, energy, contentment, "
            "mindfulness, and wisdom &mdash; each earn a mendicant the "
            "community's trust and willingness to instruct them, "
            "ensuring only growth in skillful qualities."]),
        ("The same list, now with its social mechanism explained", [
            "AN 10.17 named the ten qualities as protective without "
            "explaining how; this discourse supplies the missing "
            "mechanism for every single item: knowing a mendicant "
            "possesses a given quality, mendicants of every seniority "
            "consider them worth advising, and that ongoing "
            "instruction is what actually protects them from decline."]),
        ("A full narrative frame, unlike AN 10.17", [
            "This discourse also restores the standard narrative "
            "opening &mdash; the setting at Sāvatthī, the Buddha "
            "addressing the mendicants, their reply &mdash; that AN "
            "10.17 omitted entirely, along with the standard closing "
            "formula of the mendicants' satisfaction."]),
        ("Protection through community, not isolation", [
            "Read together with AN 10.17, this pair makes a pointed "
            "claim: the ten qualities don't simply protect a mendicant "
            "in isolation, but function by drawing the surrounding "
            "community's guidance toward them &mdash; a protector "
            "built from cultivated qualities that in turn earns "
            "external support, not one or the other alone."]),
    ],
    terms=[
        ("nāthakaraṇā dhammā",
         "&ldquo;qualities that serve as protector&rdquo; &mdash; the "
         "identical framing phrase as AN 10.17."),
        ("theragopi majjhimagopi navagopi bhikkhū sotabbaṁ maññanti",
         "&ldquo;the mendicants &mdash; whether senior, middle, or "
         "junior &mdash; think that mendicant is worth advising and "
         "instructing&rdquo; &mdash; the shared social mechanism this "
         "discourse adds for every one of the ten qualities."),
        ("sotabbaṁ maññamānā ovadanti anusāsanti",
         "&ldquo;being treated with such kindness... can expect only "
         "growth, not decline&rdquo; &mdash; the direct link between "
         "receiving instruction and continued growth."),
        ("evaṁ vutte, te bhikkhū bhagavato bhāsitaṁ abhinandunti",
         "&ldquo;satisfied, the mendicants approved what the Buddha "
         "said&rdquo; &mdash; the standard closing formula, absent "
         "from AN 10.17's own more abbreviated version."),
        ("udayatthagāminiyā paññāya samannāgato",
         "&ldquo;the wisdom of arising and passing away&rdquo; "
         "&mdash; the tenth and final quality, identical to AN 10.17's "
         "closing item."),
    ],
    text_intro=(
        "The discourse in full: the same ten qualities as AN 10.17, "
        "each explained through its social consequence. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A full narrative frame"),
        ("p", "&sect;1", "an10.18:1.1-2.4"),
        ("h3", "Ten qualities, each earning trust"),
        ("p", "&sect;2", "an10.18:2.5-11.4"),
        ("h3", "Closing"),
        ("p", "&sect;3", "an10.18:12.1-12.5"),
    ],
    quiz=[
        {"q": "How does this discourse's ten qualities compare to AN "
              "10.17's?",
         "opts": [
             "Entirely different qualities",
             "Word-for-word identical, now each explained through a "
             "shared social mechanism",
             "Only five qualities are shared",
             "A contradiction of AN 10.17"],
         "correct": 1,
         "expl": "The same ten qualities, given fuller elaboration "
                 "here."},
        {"q": "What social mechanism does this discourse add for each "
              "quality?",
         "opts": [
             "Nothing is added",
             "Mendicants of every seniority consider someone with that "
             "quality worth advising and instructing, ensuring growth",
             "A material reward is given",
             "A formal ceremony is held"],
         "correct": 1,
         "expl": "The missing explanation for how each quality "
                 "actually protects a mendicant."},
        {"q": "What does this discourse restore that AN 10.17 omits?",
         "opts": [
             "Nothing; both are identical in structure",
             "A full narrative frame — setting, the Buddha addressing "
             "the mendicants, and the standard closing formula",
             "A completely different list of qualities",
             "A dialogue with a named disciple"],
         "correct": 1,
         "expl": "AN 10.17 gives a bare listing; this discourse "
                 "supplies the standard narrative wrapper."},
        {"q": "According to the guide, what pointed claim does this "
              "pair of discourses make together?",
         "opts": [
             "That a mendicant should avoid all community contact",
             "That the ten qualities function by drawing the "
             "surrounding community's guidance toward the mendicant, "
             "not protecting them in isolation",
             "That only senior mendicants can be protected",
             "That protection requires no cultivated qualities at all"],
         "correct": 1,
         "expl": "Protection built from cultivated qualities that in "
                 "turn earns community support."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "No setting is given, matching AN 10.17"],
         "correct": 1,
         "expl": "The standard narrative setting AN 10.17 itself "
                 "omits."},
        {"q": "What closes this discourse, unlike AN 10.17?",
         "opts": [
             "Nothing different",
             "The standard formula: the mendicants, satisfied, "
             "approved what the Buddha said",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "The complete narrative frame, opening and closing "
                 "this fuller version."},
    ],
    marginalia=[
        ("The same ten, explained", [
            "each quality earns",
            "trust from every mendicant &mdash;",
            "senior, middle, junior",
        ]),
        ("Instruction as protection", [
            "trusted, they're advised;",
            "advised, they only grow &mdash;",
            "the missing mechanism",
        ]),
        ("A full frame, restored", [
            "Sāvatthī, the Buddha",
            "speaking, and their assent &mdash;",
            "what 10.17 left bare",
        ]),
        ("Cross-references", [
            "AN 10.17 &middot; the identical ten qualities, there "
            "listed without explanation",
            "AN 10.19 &middot; next, Abodes of the Noble Ones (1st)",
        ]),
    ],
    further=[
        '<a href="%s/an10.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.17.html">AN 10.17 &middot; A Protector (1st)</a> &mdash; previous, '
        "the same ten qualities without their social mechanism explained.",
        '<a href="an-10.19.html">AN 10.19 &middot; Abodes of the Noble Ones (1st)</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.19 — Ariyavāsasutta (1st)
# --------------------------------------------------------------------------- #
page(
    19, "Ariyavāsa", "Abodes of the Noble Ones (1st)",
    vagga=VAGGA_2,
    meta_title=("AN 10.19 — Abodes of the Noble Ones (1st) | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the first Ariyavāsasutta, a bare list of the ten abodes in "
        "which noble ones of every era dwell, from the five hindrances "
        "given up to freedom in mind and by wisdom. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list, no narrative and no elaboration"),
        ("Length", "~30 seconds to read"),
        ("A timeless claim", "The discourse names these ten abodes as "
         "shared by noble ones of the past, present, and future alike"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and dense, best read alongside AN "
                       "10.20's full elaboration"),
    ],
    why=(
        "There are ten abodes of the noble ones, in which the noble "
        "ones of the past, present, and future all abide: having given "
        "up five factors, being endowed with six factors, having a "
        "single guard, four supports, having cast aside idiosyncratic "
        "interpretations of the truth, having totally given up "
        "searching, having pure intentions, having stilled the physical "
        "process, and being well freed in mind and by wisdom."),
    guide=[
        ("The teaching in one sentence", [
            "Ten abodes are shared by every noble one of the past, "
            "present, and future: five factors given up, six factors "
            "possessed, a single guard, four supports, dogmatic views "
            "cast aside, searching abandoned, intentions purified, the "
            "physical process stilled, and freedom in both mind and "
            "wisdom."]),
        ("Ten items named, none explained", [
            "This discourse simply lists all ten abodes by name, "
            "trusting either prior familiarity or its own companion "
            "discourse to supply the content behind each phrase &mdash; "
            "&lsquo;a single guard&rsquo; and &lsquo;four "
            "supports&rsquo; in particular give no hint here of what "
            "they actually name."]),
        ("A timeless claim about all noble ones everywhere", [
            "The discourse's opening frame is unusually sweeping: not "
            "a description of one mendicant's own progress, but a "
            "claim about every noble one across all three times "
            "&mdash; past, present, and future &mdash; abiding in "
            "these same ten conditions without exception."]),
        ("A companion discourse follows immediately", [
            "AN 10.20, next, restates this identical ten-item list and "
            "explains every single term in full &mdash; readers wanting "
            "to know what &lsquo;a single guard&rsquo; or "
            "&lsquo;stilled the physical process&rsquo; actually means "
            "should read that discourse directly."]),
    ],
    terms=[
        ("dasa ariyavāsā",
         "&ldquo;ten abodes of the noble ones&rdquo; &mdash; this "
         "discourse's own title term, naming a timeless dwelling shared "
         "across all three times."),
        ("pañcaṅgavippahīno",
         "&ldquo;has given up five factors&rdquo; &mdash; the first "
         "abode, left unexplained here."),
        ("ekārakkho",
         "&ldquo;has a single guard&rdquo; &mdash; the third abode, a "
         "phrase whose meaning this discourse doesn't supply."),
        ("catunissayo",
         "&ldquo;has four supports&rdquo; &mdash; the fourth abode, "
         "likewise unexplained here."),
        ("suvimuttacitto, suvimuttapañño",
         "&ldquo;well freed in mind and well freed by wisdom&rdquo; "
         "&mdash; the ninth and tenth abodes, closing the list."),
    ],
    text_intro=(
        "The discourse in full: the ten abodes of the noble ones, "
        "named without elaboration. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Ten abodes, named"),
        ("p", "&sect;1", "an10.19:1.1-1.4"),
    ],
    quiz=[
        {"q": "What claim does this discourse make about the ten "
              "abodes?",
         "opts": [
             "That only the Buddha himself dwells in them",
             "That every noble one of the past, present, and future "
             "abides in these same ten conditions",
             "That they apply only to monastics, never laypeople",
             "That they are attained only after death"],
         "correct": 1,
         "expl": "A sweeping, timeless claim spanning all three eras."},
        {"q": "How does this discourse present its ten items?",
         "opts": [
             "Each with a full explanation and simile",
             "As a bare list, with no elaboration of what any phrase "
             "actually means",
             "As a narrative dialogue",
             "In verse throughout"],
         "correct": 1,
         "expl": "Names alone, trusting the reader or a companion "
                 "discourse to supply the content."},
        {"q": "What does &lsquo;a single guard&rsquo; refer to, "
              "according to this discourse's own text?",
         "opts": [
             "It is explained in detail here",
             "This discourse gives no explanation at all",
             "A literal monastery gatekeeper",
             "A weapon for self-defense"],
         "correct": 1,
         "expl": "Left unexplained, requiring AN 10.20's fuller "
                 "treatment."},
        {"q": "What relationship does this discourse have with AN "
              "10.20?",
         "opts": [
             "No relationship at all",
             "AN 10.20 restates the identical ten-item list and "
             "explains every term in full",
             "AN 10.20 uses a completely different list",
             "AN 10.20 contradicts this discourse"],
         "correct": 1,
         "expl": "A companion pair, matching AN 10.17-18's own "
                 "structure earlier in this chapter."},
        {"q": "What are the ninth and tenth abodes?",
         "opts": [
             "The five lower and five higher fetters",
             "Being well freed in mind and well freed by wisdom",
             "The four absorptions",
             "The three knowledges"],
         "correct": 1,
         "expl": "Closing the list, though their content awaits AN "
                 "10.20's explanation."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare, timeless declaration, without narrative "
                 "frame."},
    ],
    marginalia=[
        ("Ten abodes, named", [
            "five given up, six held,",
            "a single guard, four supports,",
            "and more, unexplained",
        ]),
        ("A timeless claim", [
            "past, present, future &mdash;",
            "every noble one dwells",
            "in these same ten",
        ]),
        ("Names without content", [
            "&lsquo;a single guard&rsquo; &mdash; what",
            "does that even mean?",
            "AN 10.20 answers",
        ]),
        ("Cross-references", [
            "AN 10.18 &middot; previous",
            "AN 10.20 &middot; next, the same list fully explained, "
            "closing this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an10.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.18.html">AN 10.18 &middot; A Protector (2nd)</a> &mdash; previous.',
        '<a href="an-10.20.html">AN 10.20 &middot; Abodes of the Noble Ones (2nd)</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.20 — Ariyavāsasutta (2nd) — closes ch.2 Nāthavagga
# --------------------------------------------------------------------------- #
page(
    20, "Ariyavāsa", "Abodes of the Noble Ones (2nd)",
    vagga=VAGGA_2,
    meta_title=("AN 10.20 — Abodes of the Noble Ones (2nd) | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the second Ariyavāsasutta, closing this chapter with a full "
        "explanation of all ten abodes — including the four "
        "undetermined questions cast aside as dogma. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "The land of the Kurus, near the Kuru town of "
                    "Kammāsadamma"),
        ("Speakers", SPEAKER),
        ("Form", "The same ten abodes as AN 10.19, each fully "
                 "explained in turn"),
        ("Length", "~4 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Nāthavagga</em>, the second chapter of the Tens; "
         "the source's own untranslated closing verse names all ten "
         "discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "dense and doctrinally rich, closing this "
                       "chapter's densest discourse"),
    ],
    why=(
        "The same ten abodes of the noble ones named at AN 10.19 are "
        "here fully explained: the five hindrances given up, "
        "equanimity toward all six sense doors, mindfulness as the "
        "single guard, the fourfold reflective use of requisites, the "
        "four undetermined questions cast aside as dogma, searching "
        "abandoned, intentions purified, the fourth absorption as the "
        "physical process stilled, and freedom in both mind and wisdom."),
    guide=[
        ("The teaching in one sentence", [
            "The ten abodes named at AN 10.19 are: the five hindrances "
            "given up, equanimity toward all six sense doors, "
            "mindfulness as the single guard, reflective use of the "
            "four requisites, dogmatic views cast aside, searching for "
            "sensuality, existence, and spiritual life abandoned, "
            "intentions of sensuality, malice, and cruelty given up, "
            "the fourth absorption as the stilled physical process, "
            "and a mind and wisdom freed from greed, hate, and "
            "delusion."]),
        ("Six sense doors, met with equanimity", [
            "The second abode extends a pattern already familiar from "
            "this project: equanimity toward each of the six sense "
            "doors in turn &mdash; sights, sounds, smells, tastes, "
            "touches, and mental phenomena &mdash; neither happy nor "
            "sad about any of them, remaining mindful and aware "
            "throughout."]),
        ("Four supports, the same reflective formula as AN 9.2", [
            "The fourth abode's &lsquo;four supports&rsquo; turn out "
            "to be the identical formula already met at AN 9.2: after "
            "appraisal, using some things, enduring some things, "
            "avoiding some things, and getting rid of some things "
            "&mdash; a compact reprise of that earlier teaching on "
            "reflective use of requisites."]),
        ("Four undetermined questions, named explicitly", [
            "This discourse's fifth abode is unusually specific for "
            "this project: it names the classic four sets of "
            "&lsquo;idiosyncratic interpretations&rsquo; the Buddha "
            "famously declined to settle &mdash; whether the cosmos is "
            "eternal or not, finite or infinite; whether the soul and "
            "body are the same or different; and four positions on "
            "whether a realized one exists, doesn't exist, both, or "
            "neither after death. A noble one has cast aside all of "
            "these dogmatic positions entirely, not adopted a fifth "
            "one of their own."]),
        ("Closing the chapter, in full detail", [
            "With this discourse, <em>Nāthavagga</em>, the second "
            "chapter, closes on its most doctrinally dense treatment "
            "&mdash; the source's own untranslated colophon and "
            "chapter-summary verse name all ten discourses of the "
            "chapter by their opening words."]),
    ],
    terms=[
        ("chasu dvāresu upekkhako",
         "&ldquo;possesses six factors&rdquo; &mdash; equanimity "
         "toward each of the six sense doors, the second abode's own "
         "full explanation."),
        ("satārakkhena cetasā samannāgato",
         "&ldquo;a single guard&rdquo; &mdash; explained here as a "
         "heart guarded specifically by mindfulness."),
        ("paṭisaṅkhā yoniso sevati, adhivāseti, parivajjeti, vinodeti",
         "&ldquo;after appraisal... uses... endures... avoids... gets "
         "rid of&rdquo; &mdash; the four supports, identical to the "
         "formula already met at AN 9.2."),
        ("sassato loko... hoti ca na ca hoti tathāgato paraṁ maraṇā",
         "&ldquo;the cosmos is eternal... after death, a realized one "
         "both exists and no longer exists&rdquo; &mdash; the classic "
         "undetermined questions this discourse names explicitly as "
         "dogma to be cast aside."),
        ("nāthavaggo dutiyo",
         "&ldquo;the second chapter, Nāthavagga, is finished&rdquo; "
         "&mdash; the source's own untranslated colophon closing this "
         "chapter."),
    ],
    text_intro=(
        "The discourse in full: the same ten abodes as AN 10.19, each "
        "fully explained. The source's own closing colophon and "
        "chapter-summary verse are untranslated in the English and "
        "are described rather than quoted here. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten abodes, named and introduced"),
        ("p", "&sect;1", "an10.20:1.1-2.3"),
        ("h3", "Five factors given up, six possessed"),
        ("p", "&sect;2", "an10.20:3.1-4.8"),
        ("h3", "A single guard, four supports"),
        ("p", "&sect;3", "an10.20:5.1-6.3"),
        ("h3", "Dogma cast aside, searching abandoned"),
        ("p", "&sect;4", "an10.20:7.1-8.3"),
        ("h3", "Pure intentions, the physical process stilled"),
        ("p", "&sect;5", "an10.20:9.1-10.3"),
        ("h3", "Freed in mind and by wisdom"),
        ("p", "&sect;6", "an10.20:11.1-13.4"),
    ],
    quiz=[
        {"q": "How does this discourse's second abode, six factors, "
              "get explained?",
         "opts": [
             "As six kinds of wealth",
             "As equanimity toward each of the six sense doors — "
             "sights, sounds, smells, tastes, touches, mental "
             "phenomena — remaining mindful and aware",
             "As six monastic ranks",
             "As six precepts"],
         "correct": 1,
         "expl": "A pattern of equanimity across all six senses, not a "
                 "separate new list."},
        {"q": "What formula turns out to explain the fourth abode, "
              "&lsquo;four supports&rsquo;?",
         "opts": [
             "A completely new teaching",
             "The identical reflective-use formula already met at AN "
             "9.2 — using, enduring, avoiding, and getting rid of "
             "things after appraisal",
             "The four noble truths",
             "The four right efforts"],
         "correct": 1,
         "expl": "A direct reprise of an earlier discourse's own "
                 "teaching."},
        {"q": "What does the fifth abode explicitly name, unusually "
              "specifically for this project?",
         "opts": [
             "The four noble truths",
             "The classic four sets of undetermined questions the "
             "Buddha declined to settle — the cosmos's eternality, the "
             "soul-body relationship, and the Realized One's status "
             "after death",
             "The four right efforts",
             "The four bases of psychic power"],
         "correct": 1,
         "expl": "Named explicitly as dogma to be cast aside entirely, "
                 "not resolved with a competing position."},
        {"q": "What does a noble one do with these undetermined "
              "questions, according to this discourse?",
         "opts": [
             "Adopts one position as correct",
             "Casts aside, throws out, discards, and relinquishes all "
             "of these dogmatic positions entirely",
             "Debates them at length with outsiders",
             "Ignores the question of whether they matter"],
         "correct": 1,
         "expl": "Complete relinquishment, not resolution by adopting "
                 "a fifth alternative view."},
        {"q": "What does this discourse close, and how?",
         "opts": [
             "Nothing; the chapter continues past it",
             "<em>Nāthavagga</em>, the second chapter, with an "
             "untranslated colophon and uddāna verse naming all ten "
             "discourses",
             "The entire nipāta",
             "Only this single discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "The land of the Kurus, near Kammāsadamma",
             "Rājagaha, on Vulture's Peak",
             "No setting is given"],
         "correct": 1,
         "expl": "A distinctive setting, closing this chapter's "
                 "densest discourse."},
    ],
    marginalia=[
        ("Six doors, one equanimity", [
            "sight, sound, smell, taste,",
            "touch, and thought &mdash; neither",
            "happy nor sad at any",
        ]),
        ("Dogma, cast aside whole", [
            "eternal or not, one",
            "soul or two &mdash; none adopted,",
            "all simply released",
        ]),
        ("A formula, reprised", [
            "the same four supports",
            "as AN 9.2 &mdash;",
            "use, endure, avoid, discard",
        ]),
        ("Cross-references", [
            "AN 9.2 &middot; the identical four-supports formula",
            "AN 10.19 &middot; previous, the same ten abodes named "
            "without explanation",
            "AN 10.21 &middot; next, opening ch.3, Mahāvagga",
        ]),
    ],
    further=[
        '<a href="%s/an10.20/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.2.html">AN 9.2 &middot; Supported</a> &mdash; the identical '
        "four-supports formula, first met there.",
        '<a href="an-10.19.html">AN 10.19 &middot; Abodes of the Noble Ones (1st)</a> '
        "&mdash; previous.",
    ],
)
