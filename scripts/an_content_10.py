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


# --------------------------------------------------------------------------- #
# ch.3 — Mahāvagga (AN 10.21-30)
# --------------------------------------------------------------------------- #
VAGGA_3 = "<em>Mahāvagga</em> &mdash; the third chapter of the Tens"


# --------------------------------------------------------------------------- #
# AN 10.21 — Sīhanādasutta — this chapter's own namesake
# --------------------------------------------------------------------------- #
page(
    21, "Sīhanāda", "The Lion&rsquo;s Roar",
    vagga=VAGGA_3,
    meta_title="AN 10.21 — The Lion's Roar | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the famous Sīhanādasutta, naming the Buddha's ten powers "
        "through the image of a lion emerging to hunt, opening this "
        "chapter with one of the canon's best-known teachings. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A lion simile, then the Buddha's ten powers named in "
                 "turn, each closing the same refrain"),
        ("Length", "~3 minutes to read"),
        ("Chapter's namesake, and a famous teaching", "This discourse "
         "names the chapter and delivers one of the most cited "
         "teachings in the entire canon, the ten Tathāgata powers"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "dense and doctrinally central, worth reading "
                       "slowly"),
    ],
    why=(
        "Just as a lion emerges from his den at evening, surveys the "
        "four quarters, and roars three times before hunting, the "
        "Buddha's own teaching to an assembly is his lion's roar, "
        "grounded in ten powers &mdash; from knowing the possible and "
        "impossible to the ending of his own defilements &mdash; that "
        "let him claim the bull's place and turn the wheel of the "
        "teaching."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha possesses ten powers of a Realized One &mdash; "
            "knowing the possible and impossible, the results of "
            "deeds, where all paths of practice lead, the world's many "
            "elements, beings' diverse convictions and faculties, the "
            "states of meditative attainment, his own and others' past "
            "lives, others' rebirth according to their deeds, and the "
            "ending of his own defilements &mdash; and with these "
            "powers claims the bull's place and roars his lion's roar."]),
        ("A vivid animal image for a philosophical claim", [
            "The discourse opens with unusually concrete natural "
            "observation: a lion emerging at evening, yawning, "
            "surveying every direction, roaring three times before the "
            "hunt &mdash; even naming the lion's own reason, avoiding "
            "injury to small creatures on uneven ground &mdash; before "
            "turning this image directly onto the Buddha's own act of "
            "teaching."]),
        ("Ten powers, one shared refrain", [
            "Each of the ten powers follows an identical closing "
            "formula: since the Realized One truly understands this, "
            "it is a power of the Realized One, and relying on it he "
            "claims the bull's place, roars his lion's roar, and turns "
            "the divine wheel &mdash; the same three-part authority "
            "claimed identically ten times over."]),
        ("This chapter's own namesake, one of the canon's most cited "
         "teachings", [
            "This discourse lends its own image, sīhanāda, the lion's "
            "roar, to the chapter's name, Mahāvagga &mdash; though the "
            "chapter's own generic title doesn't reflect it directly. "
            "The ten powers named here are among the most frequently "
            "cited formulas across the entire Pāli canon, marking a "
            "Buddha's own distinctive, complete knowledge."]),
    ],
    terms=[
        ("sīhanādaṁ nadati",
         "&ldquo;roars his lion's roar&rdquo; &mdash; the discourse's "
         "own title image, applied directly to the Buddha teaching an "
         "assembly."),
        ("dasa tathāgatabalāni",
         "&ldquo;ten powers of a Realized One&rdquo; &mdash; the "
         "discourse's own central teaching, among the most cited "
         "formulas in the canon."),
        ("ṭhānañca ṭhānato aṭṭhānañca aṭṭhānato yathābhūtaṁ pajānāti",
         "&ldquo;truly understands the possible as possible and the "
         "impossible as impossible&rdquo; &mdash; the first power, "
         "opening the list."),
        ("āsavānaṁ khayā anāsavaṁ cetovimuttiṁ paññāvimuttiṁ",
         "&ldquo;the undefiled freedom of heart and freedom by wisdom "
         "... due to the ending of defilements&rdquo; &mdash; the "
         "tenth and final power, closing the list."),
        ("āsabhaṇṭhānaṁ paṭijānāti",
         "&ldquo;claims the bull's place&rdquo; &mdash; the "
         "discourse's own image of supreme confidence, repeated after "
         "each of the ten powers."),
    ],
    text_intro=(
        "The discourse in full: the lion simile, then the Buddha's ten "
        "powers, each closing the same refrain. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A lion, emerging to hunt"),
        ("p", "&sect;1", "an10.21:1.1-2.2"),
        ("h3", "Ten powers of a Realized One"),
        ("p", "&sect;2", "an10.21:3.1-3.4"),
        ("p", "&sect;3", "an10.21:4.1-4.2"),
        ("p", "&sect;4", "an10.21:5.1-5.2"),
        ("p", "&sect;5", "an10.21:6.1-6.2"),
        ("p", "&sect;6", "an10.21:7.1-7.2"),
        ("p", "&sect;7", "an10.21:8.1-8.2"),
        ("p", "&sect;8", "an10.21:9.1-9.2"),
        ("p", "&sect;9", "an10.21:10.1-10.2"),
        ("p", "&sect;10", "an10.21:11.1-11.2"),
        ("p", "&sect;11", "an10.21:12.1-13.1"),
    ],
    quiz=[
        {"q": "What image opens this discourse before applying it to "
              "the Buddha?",
         "opts": [
             "A wild bull elephant",
             "A lion emerging at evening, surveying the four "
             "quarters, and roaring three times before the hunt",
             "A stone post unmoved by storms",
             "A burning pile of twigs"],
         "correct": 1,
         "expl": "A vivid natural observation, turned directly onto the "
                 "Buddha's own act of teaching."},
        {"q": "What is the first of the ten powers?",
         "opts": [
             "Recollecting past lives",
             "Truly understanding the possible as possible and the "
             "impossible as impossible",
             "The ending of defilements",
             "Clairvoyance regarding others' rebirth"],
         "correct": 1,
         "expl": "Opening the list of ten powers."},
        {"q": "What refrain closes each of the ten powers?",
         "opts": [
             "A verse of praise",
             "That relying on this power, he claims the bull's place, "
             "roars his lion's roar, and turns the divine wheel",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "The same three-part claim of authority, repeated ten "
                 "times."},
        {"q": "What is the tenth and final power?",
         "opts": [
             "Knowledge of the world's elements",
             "The undefiled freedom of heart and freedom by wisdom, "
             "due to the ending of defilements",
             "Knowledge of others' faculties",
             "Understanding where all paths of practice lead"],
         "correct": 1,
         "expl": "Closing the list with the Buddha's own liberation."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular", "Its own image, sīhanāda (the "
             "lion's roar), though the chapter's title itself is "
             "generic",
             "A disciple's name", "A place name"],
         "correct": 1,
         "expl": "The chapter's own namesake, though titled generically "
                 "as Mahāvagga."},
        {"q": "How significant are the ten powers within the wider "
              "canon, according to the guide?",
         "opts": [
             "A minor, rarely mentioned teaching",
             "Among the most frequently cited formulas across the "
             "entire Pāli canon",
             "Unique to this single discourse",
             "A teaching later superseded"],
         "correct": 1,
         "expl": "One of the canon's most central and widely repeated "
                 "doctrinal formulas."},
    ],
    marginalia=[
        ("A lion, at evening", [
            "yawns, surveys all four",
            "quarters, roars three times &mdash;",
            "then sets out to hunt",
        ]),
        ("Ten powers, one refrain", [
            "possible, results,",
            "paths, elements, convictions,",
            "faculties, and more",
        ]),
        ("A famous teaching", [
            "cited throughout the",
            "canon &mdash; the ten powers,",
            "marking full awakening",
        ]),
        ("Cross-references", [
            "AN 10.20 &middot; previous chapter's closing page",
            "AN 10.22 &middot; next, the same ten powers reframed as "
            "unsurpassable knowledge",
        ]),
    ],
    further=[
        '<a href="%s/an10.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.20.html">AN 10.20 &middot; Abodes of the Noble Ones (2nd)</a> '
        "&mdash; previous.",
        '<a href="an-10.22.html">AN 10.22 &middot; Hypotheses</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.22 — Vesārajjasutta
# --------------------------------------------------------------------------- #
page(
    22, "Vesārajja", "Hypotheses",
    vagga=VAGGA_3,
    meta_title="AN 10.22 — Hypotheses | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Vesārajjasutta, in which the Buddha tells Ānanda his "
        "self-assurance rests on unsurpassable knowledge, then repeats "
        "the same ten powers already met at AN 10.21. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 10.21"),
        ("Speakers", "The Buddha, addressing Venerable Ānanda"),
        ("Form", "A claim of unsurpassable knowledge, then the "
                 "identical ten powers as AN 10.21"),
        ("Length", "~2 minutes to read"),
        ("Repeating AN 10.21's ten powers, differently framed", "The "
         "same list, now presented as the ground of the Buddha's own "
         "self-assurance rather than his lion's roar"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the same dense content as AN 10.21, worth "
                       "reading for its distinct framing"),
    ],
    why=(
        "Speaking to Ānanda, the Buddha claims self-assurance regarding "
        "the various hypotheses people hold, able to teach appropriately "
        "to different people and know each case truly &mdash; an "
        "unsurpassable knowledge grounded in the same ten powers of a "
        "Realized One already named at AN 10.21."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha's self-assurance in teaching Dhamma "
            "appropriately to different people, truly knowing every "
            "case as it is, rests on the identical ten powers of a "
            "Realized One already named at AN 10.21."]),
        ("A private conversation, not a public roar", [
            "Where AN 10.21 framed these powers as the Buddha's "
            "authority before an assembly, this discourse frames the "
            "identical content as a private claim made directly to "
            "Ānanda &mdash; the same ten powers, now grounding personal "
            "self-assurance rather than public declaration."]),
        ("Unsurpassable knowledge, named before the powers themselves", [
            "This discourse adds a claim AN 10.21 doesn't make "
            "explicitly: knowing whether something exists or doesn't, "
            "is inferior or superior, is the &lsquo;unsurpassable "
            "knowledge,&rsquo; truly knowing each and every case, with "
            "no other knowledge said to be better or finer &mdash; a "
            "framing statement introducing the same ten powers that "
            "follow."]),
        ("Identical content, worth reading as a pair", [
            "Apart from this opening framing and its narrower "
            "audience, this discourse's ten powers are word for word "
            "AN 10.21's own list, right down to the shared closing "
            "refrain &mdash; the two discourses worth reading together "
            "for how the same teaching serves two different rhetorical "
            "purposes."]),
    ],
    terms=[
        ("nānādhimuttikānaṁ ñeyyapariyāyaṁ",
         "&ldquo;the teachings that lead to realizing by insight the "
         "various different hypotheses&rdquo; &mdash; the Buddha's own "
         "opening claim to Ānanda, framing what follows."),
        ("anuttariyaṁ ñāṇaṁ",
         "&ldquo;the unsurpassable knowledge&rdquo; &mdash; this "
         "discourse's own name for truly knowing each and every case, "
         "introduced before the ten powers themselves."),
        ("dasa tathāgatabalāni",
         "&ldquo;ten powers of a Realized One&rdquo; &mdash; the "
         "identical list and order as AN 10.21."),
        ("āsabhaṇṭhānaṁ paṭijānāti, sīhanādaṁ nadati",
         "&ldquo;claims the bull's place, roars his lion's roar&rdquo; "
         "&mdash; the same closing refrain repeated after each power, "
         "unchanged from AN 10.21."),
        ("āyasmā ānando",
         "&ldquo;Venerable Ānanda&rdquo; &mdash; this discourse's own "
         "addressee, distinguishing it from AN 10.21's public "
         "assembly setting."),
    ],
    text_intro=(
        "The discourse in full: a claim of unsurpassable knowledge, "
        "then the identical ten powers as AN 10.21. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Unsurpassable knowledge, claimed to Ānanda"),
        ("p", "&sect;1", "an10.22:1.1-2.5"),
        ("h3", "Ten powers of a Realized One"),
        ("p", "&sect;2", "an10.22:3.1-3.4"),
        ("p", "&sect;3", "an10.22:4.1-4.2"),
        ("p", "&sect;4", "an10.22:5.1-5.2"),
        ("p", "&sect;5", "an10.22:6.1-6.2"),
        ("p", "&sect;6", "an10.22:7.1-7.2"),
        ("p", "&sect;7", "an10.22:8.1-8.2"),
        ("p", "&sect;8", "an10.22:9.1-9.2"),
        ("p", "&sect;9", "an10.22:10.1-10.2"),
        ("p", "&sect;10", "an10.22:11.1-11.2"),
        ("p", "&sect;11", "an10.22:12.1-13.1"),
    ],
    quiz=[
        {"q": "Who does the Buddha address in this discourse?",
         "opts": [
             "An assembly of mendicants publicly",
             "Venerable Ānanda, privately",
             "King Pasenadi",
             "A group of wanderers"],
         "correct": 1,
         "expl": "A private conversation, unlike AN 10.21's public "
                 "declaration."},
        {"q": "What does the Buddha name as &lsquo;unsurpassable "
              "knowledge&rsquo;?",
         "opts": [
             "Knowledge of the future alone",
             "Truly knowing each and every case, with no other "
             "knowledge said to be better or finer",
             "Knowledge of monastic law",
             "Knowledge available only to arahants"],
         "correct": 1,
         "expl": "A framing claim introduced before the ten powers "
                 "themselves."},
        {"q": "How does this discourse's ten powers compare to AN "
              "10.21's?",
         "opts": [
             "Entirely different content",
             "Word for word identical, including the shared closing "
             "refrain",
             "A shortened five-power version",
             "A contradiction of AN 10.21"],
         "correct": 1,
         "expl": "The same list and order, framed differently."},
        {"q": "What is the main difference between this discourse and "
              "AN 10.21?",
         "opts": [
             "The content of the ten powers themselves",
             "The framing and audience — private self-assurance to "
             "Ānanda rather than public authority before an assembly",
             "The number of powers named",
             "The closing refrain"],
         "correct": 1,
         "expl": "Same teaching, different rhetorical purpose and "
                 "setting."},
        {"q": "What refrain closes each power, unchanged from AN "
              "10.21?",
         "opts": [
             "A different formula entirely",
             "Claiming the bull's place and roaring the lion's roar",
             "A verse of thanks",
             "A request for confirmation"],
         "correct": 1,
         "expl": "Identical to AN 10.21, despite the different framing "
                 "context."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "Not restated, understood to continue from AN 10.21",
             "Yes, at Vesālī"],
         "correct": 2,
         "expl": "Continuing directly from the previous discourse."},
    ],
    marginalia=[
        ("A private claim", [
            "not before the crowd,",
            "but to Ānanda alone &mdash;",
            "the same ten powers",
        ]),
        ("Unsurpassable knowledge", [
            "truly knowing each",
            "and every case &mdash; no finer",
            "knowledge said to exist",
        ]),
        ("The same list, twice framed", [
            "public roar, then private",
            "assurance &mdash; one teaching,",
            "two rhetorical uses",
        ]),
        ("Cross-references", [
            "AN 10.21 &middot; the identical ten powers, there framed "
            "as public authority",
            "AN 10.23 &middot; next, Body",
        ]),
    ],
    further=[
        '<a href="%s/an10.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.21.html">AN 10.21 &middot; The Lion&rsquo;s Roar</a> &mdash; the '
        "identical ten powers, there framed as public authority.",
        '<a href="an-10.23.html">AN 10.23 &middot; Body</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.23 — Kāyasutta
# --------------------------------------------------------------------------- #
page(
    23, "Kāya", "Body",
    vagga=VAGGA_3,
    meta_title="AN 10.23 — Body | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kāyasutta, distinguishing what must be given up by the "
        "body, by speech, or by wisdom alone — the latter category "
        "including two items beyond this project's usual seventeen-"
        "item defilement list. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Three categories of what must be given up, the third "
                 "elaborated with two named examples"),
        ("Length", "~3 minutes to read"),
        ("A ten-item list that diverges from the familiar one", "This "
         "discourse's ten things given up by wisdom alone overlap with "
         "but don't exactly match this project's usual seventeen-item "
         "defilement list"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "worth reading carefully for exactly which "
                       "items appear and which don't"),
    ],
    why=(
        "Some faults are given up through bodily correction, some "
        "through verbal correction, and some &mdash; ten things "
        "including greed, hate, delusion, and several further "
        "corruptions, closing with nasty jealousy and corrupt wishes "
        "&mdash; can only be given up by seeing again and again with "
        "wisdom, never by bodily or verbal correction alone."),
    guide=[
        ("The teaching in one sentence", [
            "Some faults, once pointed out by companions, are given up "
            "through correcting bodily or verbal conduct directly, but "
            "ten deeper things &mdash; greed, hate, delusion, anger, "
            "acrimony, disdain, contempt, stinginess, nasty jealousy, "
            "and corrupt wishes &mdash; can only be given up by seeing "
            "again and again with wisdom."]),
        ("Correction by companions, for surface faults", [
            "The first two categories share an identical structure: a "
            "mendicant commits an offense by body or speech, "
            "&lsquo;sensible spiritual companions&rsquo; point it out "
            "after examination, and the mendicant, spoken to directly, "
            "gives up the bad conduct and develops good conduct in its "
            "place &mdash; correction working through social feedback."]),
        ("A tenfold list that diverges from the familiar one", [
            "The third category's list is worth checking carefully "
            "against this project's usual seventeen-item defilement "
            "list: it shares greed, hate, delusion, anger, acrimony, "
            "disdain, contempt, and stinginess with that standard list, "
            "but then closes with two items given their own full "
            "definitions &mdash; nasty jealousy (issā, defined here as "
            "resentment at others' prosperity) and corrupt wishes "
            "(pāpicchā, wanting to be seen as possessing virtues one "
            "lacks) &mdash; rather than continuing further down the "
            "standard list's remaining items."]),
        ("Corrupt wishes, defined in unusual detail", [
            "The discourse's definition of corrupt wishes is "
            "distinctively specific, naming nine separate false "
            "self-presentations in turn: wanting to seem faithful, "
            "ethical, learned, secluded, energetic, mindful, immersed, "
            "wise, and free of defilements, when none of these is "
            "actually true &mdash; a pointed catalogue of spiritual "
            "pretense."]),
    ],
    terms=[
        ("kāyena pahātabbā, vācāya pahātabbā",
         "&ldquo;should be given up by the body... by speech&rdquo; "
         "&mdash; the first two categories, each corrected through "
         "companions' direct feedback."),
        ("puna pappuna paññāya passitvā pahātabbā",
         "&ldquo;given up... by seeing again and again with "
         "wisdom&rdquo; &mdash; the third category's own distinctive "
         "phrase, naming what correction from others cannot reach."),
        ("issā",
         "&ldquo;nasty jealousy&rdquo; &mdash; defined here as "
         "resentment at another's prosperity or another ascetic's "
         "gains, the ninth item in this discourse's own list."),
        ("pāpicchatā",
         "&ldquo;corrupt wishes&rdquo; &mdash; the tenth and final "
         "item, wanting to be known for virtues one does not actually "
         "possess, defined here through nine specific false self-"
         "presentations."),
        ("assaddho saddhoti ñāyaṁ icchati",
         "&ldquo;a faithless person wishes to be known as "
         "faithful&rdquo; &mdash; the first of nine examples "
         "illustrating corrupt wishes."),
    ],
    text_intro=(
        "The discourse in full: three categories of what must be "
        "given up, the third elaborated with two named examples. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Given up by the body, or by speech"),
        ("p", "&sect;1", "an10.23:1.1-3.7"),
        ("h3", "Given up only by wisdom"),
        ("p", "&sect;2", "an10.23:4.1-4.9"),
        ("h3", "Nasty jealousy, and corrupt wishes"),
        ("p", "&sect;3", "an10.23:5.1-6.13"),
        ("h3", "Whether these things master a mendicant"),
        ("p", "&sect;4", "an10.23:7.1-8.21"),
    ],
    quiz=[
        {"q": "How are faults in the first two categories corrected, "
              "according to this discourse?",
         "opts": [
             "They cannot be corrected at all",
             "Through sensible spiritual companions pointing them out "
             "directly, leading the mendicant to correct bodily or "
             "verbal conduct",
             "Only through solitary meditation",
             "Only by the Buddha personally"],
         "correct": 1,
         "expl": "Social feedback working for surface-level conduct."},
        {"q": "How does this discourse's third-category list compare to "
              "this project's usual seventeen-item defilement list?",
         "opts": [
             "Identical in every item and order",
             "It shares the first eight items but then closes with two "
             "distinctively defined items, nasty jealousy and corrupt "
             "wishes, rather than continuing the standard list further",
             "It shares no items at all",
             "It has only five items total"],
         "correct": 1,
         "expl": "A genuine divergence worth checking carefully, not "
                 "simply another repetition of the familiar list."},
        {"q": "How does this discourse define &lsquo;nasty "
              "jealousy&rsquo;?",
         "opts": [
             "Wanting to travel to distant lands",
             "Resentment at another's prosperity or another ascetic's "
             "material gains",
             "Fear of poverty",
             "A desire for fame"],
         "correct": 1,
         "expl": "A specific, named form of ill will toward others' "
                 "good fortune."},
        {"q": "How many specific false self-presentations does this "
              "discourse name under &lsquo;corrupt wishes&rsquo;?",
         "opts": [
             "Three", "Five", "Nine", "Twelve"],
         "correct": 2,
         "expl": "Wanting to seem faithful, ethical, learned, secluded, "
                 "energetic, mindful, immersed, wise, and free of "
                 "defilements — nine in total."},
        {"q": "What can never correct the ten things in the third "
              "category, according to this discourse?",
         "opts": [
             "Wisdom alone",
             "Bodily or verbal correction by companions",
             "Meditation of any kind",
             "Nothing can correct them"],
         "correct": 1,
         "expl": "These deeper corruptions require seeing again and "
                 "again with wisdom, not social feedback."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, without narrative frame."},
    ],
    marginalia=[
        ("Two kinds, correctable", [
            "body's fault, speech's fault &mdash;",
            "pointed out, and changed",
            "through direct correction",
        ]),
        ("A list that diverges", [
            "greed through stinginess,",
            "then jealousy, corrupt wishes &mdash;",
            "not the usual close",
        ]),
        ("Nine false faces named", [
            "faithless claiming faith,",
            "witless claiming wisdom &mdash;",
            "pretense, catalogued",
        ]),
        ("Cross-references", [
            "AN 10.22 &middot; previous",
            "AN 10.24 &middot; next, By Mahācunda",
        ]),
    ],
    further=[
        '<a href="%s/an10.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.22.html">AN 10.22 &middot; Hypotheses</a> &mdash; previous.',
        '<a href="an-10.24.html">AN 10.24 &middot; By Mahācunda</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.24 — Mahācundasutta
# --------------------------------------------------------------------------- #
page(
    24, "Mahācunda", "By Mahācunda",
    vagga=VAGGA_3,
    meta_title="AN 10.24 — By Mahācunda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Mahācundasutta, testing declarations of knowledge and "
        "meditative development against AN 10.23's ten defilements, "
        "using a rich-versus-poor-person simile. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sahajāti, in the land of the Cetīs"),
        ("Speakers", "Venerable Mahācunda, addressing the mendicants"),
        ("Form", "Three kinds of declaration tested against the same "
                 "ten defilements, twice over, closed by a wealth "
                 "simile"),
        ("Length", "~4 minutes to read"),
        ("Reusing AN 10.23's own tenfold list", "The identical ten "
         "things given up only by wisdom, here used as a test for "
         "whether spiritual claims are genuine"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "highly repetitive by design, worth reading for "
                       "its closing simile"),
    ],
    why=(
        "A mendicant who declares knowledge, or meditative development, "
        "or both, but is still mastered by greed, hate, or any of the "
        "other eight things named at AN 10.23, is like a penniless "
        "person who claims to be wealthy but cannot produce payment "
        "when it's due; one whose declaration matches reality, unmastered "
        "by any of these ten, is like someone genuinely rich who can "
        "always pay."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant's declaration of knowledge, of meditative "
            "development, or of both together is only as trustworthy "
            "as whether they remain mastered by greed, hate, delusion, "
            "or any of AN 10.23's other seven items &mdash; like a "
            "declaration of wealth that proves false the moment payment "
            "actually comes due."]),
        ("Three kinds of declaration, each tested twice", [
            "Mahācunda names three claims a mendicant might make: "
            "knowing and seeing the teaching, being developed in "
            "physical endurance, ethics, mind, and wisdom, or both "
            "together &mdash; then tests each claim twice, once against "
            "being mastered by the ten defilements and once against not "
            "being mastered by them, producing six near-identical "
            "passages before the discourse's closing simile."]),
        ("Reusing AN 10.23's tenfold list directly", [
            "This discourse doesn't introduce a new list of "
            "corruptions; it applies the identical ten items just "
            "named at AN 10.23 &mdash; greed, hate, delusion, anger, "
            "acrimony, disdain, contempt, stinginess, nasty jealousy, "
            "and corrupt wishes &mdash; as the direct test for whether "
            "any of the three declarations actually holds up."]),
        ("A debt that proves whether wealth claims are genuine", [
            "The discourse's closing simile is precise and practical: a "
            "penniless person who claims wealth is exposed the moment "
            "payment comes due and they cannot produce it, while a "
            "genuinely wealthy person always can &mdash; the test isn't "
            "the claim itself but what happens when reality actually "
            "demands proof, exactly paralleling whether a mendicant's "
            "spiritual claims hold up against the ten defilements' "
            "continued presence or absence."]),
    ],
    terms=[
        ("ñāṇavādañca vadati",
         "&ldquo;makes a declaration of knowledge&rdquo; &mdash; the "
         "first of three claims this discourse tests, &lsquo;I know "
         "this teaching, I see this teaching.&rsquo;"),
        ("bhāvanāvādañca vadati",
         "&ldquo;makes a declaration of development&rdquo; &mdash; the "
         "second claim, development in physical endurance, ethics, "
         "mind, and wisdom."),
        ("rāgo taṁ bhikkhuṁ pariyādāya tiṭṭhati",
         "&ldquo;greed masters that mendicant and keeps going&rdquo; "
         "&mdash; the shared test applied to all three declarations, "
         "using the identical ten items from AN 10.23."),
        ("daliddo assako anāḷhiyo",
         "&ldquo;poor, needy, and penniless&rdquo; &mdash; the "
         "discourse's own closing simile, a false claim of wealth "
         "exposed when payment comes due."),
        ("aḍḍho mahaddhano mahābhogo",
         "&ldquo;rich, affluent, and wealthy&rdquo; &mdash; the "
         "simile's mirror-image half, a genuine claim confirmed when "
         "payment can actually be made."),
    ],
    text_intro=(
        "The discourse in full: three declarations tested against AN "
        "10.23's ten items, twice each, closed by a wealth simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three declarations, mastered by the ten"),
        ("p", "&sect;1", "an10.24:1.1-4.22"),
        ("h3", "A poor person's false claim of wealth"),
        ("p", "&sect;2", "an10.24:5.1-6.22"),
        ("h3", "Three declarations, unmastered by the ten"),
        ("p", "&sect;3", "an10.24:7.1-9.22"),
        ("h3", "A rich person's genuine claim of wealth"),
        ("p", "&sect;4", "an10.24:10.1-11.22"),
    ],
    quiz=[
        {"q": "What three kinds of declaration does Mahācunda name?",
         "opts": [
             "Declarations of wealth, status, and lineage",
             "Declarations of knowledge, of meditative development, "
             "and of both together",
             "Declarations of ordination, seniority, and merit",
             "Only a single declaration"],
         "correct": 1,
         "expl": "Three distinct spiritual claims, each tested the same "
                 "way."},
        {"q": "What test does this discourse apply to all three "
              "declarations?",
         "opts": [
             "A test of physical strength",
             "Whether the mendicant remains mastered by AN 10.23's ten "
             "items — greed, hate, and the rest",
             "A test of monastic seniority",
             "A test of teaching ability"],
         "correct": 1,
         "expl": "The identical tenfold list just introduced at AN "
                 "10.23, reused directly here."},
        {"q": "What simile closes this discourse?",
         "opts": [
             "A burning pile of twigs",
             "A penniless person falsely claiming wealth, exposed when "
             "payment comes due, versus a genuinely wealthy person who "
             "can always pay",
             "A tree lacking branches",
             "A stone post unmoved by storms"],
         "correct": 1,
         "expl": "The test isn't the claim itself but whether it holds "
                 "up when reality demands proof."},
        {"q": "How many near-identical passages does this discourse "
              "produce by testing three declarations against being "
              "mastered and not mastered?",
         "opts": [
             "Two", "Three", "Six", "Twelve"],
         "correct": 2,
         "expl": "Six passages total, three declarations each tested "
                 "twice."},
        {"q": "Who speaks this discourse, and where?",
         "opts": [
             "The Buddha, at Sāvatthī",
             "Venerable Mahācunda, at Sahajāti in the land of the Cetīs",
             "Sāriputta, at Rājagaha",
             "Ānanda, at Kosambī"],
         "correct": 1,
         "expl": "A senior disciple teaching independently of the "
                 "Buddha's own presence in the narrative."},
        {"q": "What does this discourse reuse directly from AN 10.23?",
         "opts": [
             "Nothing; it introduces entirely new content",
             "The identical ten-item list — greed, hate, delusion, and "
             "the rest — as the test for genuine versus false spiritual "
             "claims",
             "The three-category structure of body/speech/wisdom",
             "The nine corrupt-wishes examples"],
         "correct": 1,
         "expl": "A direct application of the immediately preceding "
                 "discourse's own tenfold list."},
    ],
    marginalia=[
        ("Three claims, tested", [
            "knowledge, development,",
            "or both &mdash; each measured by",
            "the same ten defilements",
        ]),
        ("A debt reveals the truth", [
            "poor, claiming wealth &mdash;",
            "exposed when payment's due;",
            "rich, and always can pay",
        ]),
        ("A list reused directly", [
            "the same ten from 10.23,",
            "now the very test",
            "of whether claims hold",
        ]),
        ("Cross-references", [
            "AN 10.23 &middot; the same ten items this discourse tests "
            "declarations against",
            "AN 10.25 &middot; next, Meditation on Universals",
        ]),
    ],
    further=[
        '<a href="%s/an10.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.23.html">AN 10.23 &middot; Body</a> &mdash; previous, the same '
        "ten items this discourse tests declarations against.",
        '<a href="an-10.25.html">AN 10.25 &middot; Meditation on Universals</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.25 — Kasiṇasutta
# --------------------------------------------------------------------------- #
page(
    25, "Kasiṇa", "Meditation on Universals",
    vagga=VAGGA_3,
    meta_title="AN 10.25 — Meditation on Universals | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kasiṇasutta, a bare list of the ten classic meditation "
        "devices — earth, water, fire, air, four colors, space, and "
        "consciousness — pervading without limit. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list, no narrative and no elaboration"),
        ("Length", "~30 seconds to read"),
        ("One of the canon's most famous meditation lists", "The "
         "kasiṇas are among the most widely known meditation objects "
         "in the entire Buddhist tradition, here given their fullest "
         "canonical form"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but naming a rich meditative tradition "
                       "worth knowing"),
    ],
    why=(
        "Ten universal dimensions of meditation are perceived above, "
        "below, across, undivided and limitless: earth, water, fire, "
        "air, blue, yellow, red, white, space, and consciousness "
        "&mdash; the classic kasiṇa objects of concentration practice."),
    guide=[
        ("The teaching in one sentence", [
            "Ten universal dimensions of meditation are perceived, "
            "each above, below, across, undivided and limitless: "
            "earth, water, fire, air, blue, yellow, red, white, space, "
            "and consciousness."]),
        ("A famous meditative tradition, named in full", [
            "The kasiṇas (universal dimensions) are among the most "
            "widely recognized meditation objects across the whole "
            "Buddhist tradition, later developed at great length in "
            "commentarial meditation manuals; this discourse gives "
            "their canonical listing in its complete tenfold form."]),
        ("Four elements, four colors, then two further dimensions", [
            "The list moves through a clear internal structure: the "
            "four physical elements (earth, water, fire, air), then "
            "four pure colors (blue, yellow, red, white), then two "
            "further dimensions that step beyond physical qualities "
            "entirely &mdash; space and consciousness itself."]),
        ("Pervading without division or limit", [
            "Each kasiṇa shares the identical qualifying phrase: "
            "perceived above, below, and across, undivided and "
            "limitless &mdash; not a bounded visual object held in mind, "
            "but that object's quality expanded to fill the whole of "
            "perceived space without interruption."]),
    ],
    terms=[
        ("kasiṇāyatanāni",
         "&ldquo;universal dimensions of meditation&rdquo; &mdash; "
         "this discourse's own title term, naming the classic tenfold "
         "list of meditation devices."),
        ("pathavīkasiṇaṁ",
         "&ldquo;the meditation on universal earth&rdquo; &mdash; the "
         "first kasiṇa, opening the fourfold elemental group."),
        ("nīlaṁ, pītaṁ, lohitaṁ, odātaṁ",
         "&ldquo;blue, yellow, red, white&rdquo; &mdash; the four "
         "color kasiṇas, following the four elements."),
        ("uddhaṁ adho tiriyaṁ advayaṁ appamāṇaṁ",
         "&ldquo;above, below, across, undivided and limitless&rdquo; "
         "&mdash; the shared qualifying phrase applied identically to "
         "all ten kasiṇas."),
        ("viññāṇakasiṇaṁ",
         "&ldquo;the meditation on universal consciousness&rdquo; "
         "&mdash; the tenth and final kasiṇa, closing the list."),
    ],
    text_intro=(
        "The discourse in full: the ten universal dimensions of "
        "meditation, each perceived without division or limit. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten universal dimensions"),
        ("p", "&sect;1", "an10.25:1.1-1.13"),
    ],
    quiz=[
        {"q": "What ten universal dimensions does this discourse name?",
         "opts": [
             "Ten monastic precepts",
             "Earth, water, fire, air, blue, yellow, red, white, "
             "space, and consciousness",
             "The five aggregates plus five hindrances",
             "Ten kinds of wrong view"],
         "correct": 1,
         "expl": "The classic kasiṇa list, among the most widely known "
                 "meditation objects in the tradition."},
        {"q": "How does this discourse's list organize internally?",
         "opts": [
             "Randomly, with no discernible structure",
             "Four physical elements, then four colors, then two "
             "further dimensions (space and consciousness)",
             "Alphabetically by Pāli term",
             "By difficulty, easiest to hardest"],
         "correct": 1,
         "expl": "A clear progression from elemental to chromatic to "
                 "abstract dimensions."},
        {"q": "What qualifying phrase applies identically to all ten "
              "kasiṇas?",
         "opts": [
             "&ldquo;Difficult to attain and rarely achieved&rdquo;",
             "&ldquo;Above, below, across, undivided and "
             "limitless&rdquo;",
             "&ldquo;Reserved for advanced meditators only&rdquo;",
             "&ldquo;Attained only in deep forest solitude&rdquo;"],
         "correct": 1,
         "expl": "The shared formula naming how each dimension is "
                 "meant to fill perception without interruption."},
        {"q": "According to the guide, how significant are the kasiṇas "
              "within the wider Buddhist tradition?",
         "opts": [
             "A minor, rarely used practice",
             "Among the most widely recognized meditation objects "
             "across the whole tradition, later developed at length in "
             "commentarial manuals",
             "Unique to this single discourse",
             "A later addition unrelated to canonical practice"],
         "correct": 1,
         "expl": "A foundational meditative catalogue with wide later "
                 "influence."},
        {"q": "What is the tenth and final kasiṇa named?",
         "opts": [
             "White", "Space",
             "Consciousness", "Air"],
         "correct": 2,
         "expl": "Closing the list at its most abstract dimension."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare catalogue, without narrative frame."},
    ],
    marginalia=[
        ("Four elements, four colors", [
            "earth, water, fire, air,",
            "blue, yellow, red, white &mdash;",
            "then space, consciousness",
        ]),
        ("Filling perception whole", [
            "above, below, across &mdash;",
            "undivided, limitless,",
            "not a bounded object",
        ]),
        ("A famous tradition", [
            "the kasiṇas, later",
            "developed at great length &mdash;",
            "here, their full ten named",
        ]),
        ("Cross-references", [
            "AN 10.24 &middot; previous",
            "AN 10.26 &middot; next, With Kāḷī",
        ]),
    ],
    further=[
        '<a href="%s/an10.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.24.html">AN 10.24 &middot; By Mahācunda</a> &mdash; previous.',
        '<a href="an-10.26.html">AN 10.26 &middot; With Kāḷī</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.26 — Kāḷīsutta
# --------------------------------------------------------------------------- #
page(
    26, "Kāḷī", "With Kāḷī",
    vagga=VAGGA_3,
    meta_title="AN 10.26 — With Kāḷī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kāḷīsutta, in which Mahākaccāna explains a cryptic Buddha "
        "verse to a laywoman by showing how the ten kasiṇas of AN "
        "10.25 can be mistaken for the ultimate goal. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "The land of the Avantis, near Kuraraghara on "
                    "Steep Mountain"),
        ("Speakers", "The laywoman Kāḷī of Kurughara questioning "
                     "Venerable Mahākaccāna"),
        ("Form", "A quoted verse, a request for its meaning, and an "
                 "answer built on AN 10.25's ten kasiṇas"),
        ("Length", "~3 minutes to read"),
        ("Putting AN 10.25's list to direct use", "The kasiṇas named "
         "in bare form at AN 10.25 here become the concrete substance "
         "of a philosophical explanation"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "subtle exegesis, worth reading alongside AN "
                       "10.25 directly"),
    ],
    why=(
        "The laywoman Kāḷī asks Mahākaccāna to explain a Buddha verse "
        "about having reached peace of heart apart from other people, "
        "and he answers by showing that some ascetics and brahmins "
        "mistake each kasiṇa attainment, one after another, for the "
        "ultimate goal, while the Buddha directly knew the limits of "
        "each and saw the beginning, drawback, and escape."),
    guide=[
        ("The teaching in one sentence", [
            "Some ascetics and brahmins regard each of the ten kasiṇa "
            "attainments as the ultimate goal and are reborn accordingly, "
            "but the Buddha directly knew the extent of each "
            "attainment, saw its beginning, drawback, and escape, and "
            "so reached genuine peace of heart, unattached to any of "
            "them."]),
        ("A cryptic verse, requiring exegesis", [
            "Kāḷī brings Mahākaccāna a specific quoted verse from "
            "&lsquo;The Maidens' Questions&rsquo; &mdash; the Buddha "
            "declaring he has conquered the army of the likable and "
            "pleasant, awakened alone in absorption, and no longer gets "
            "close to people nor they to him &mdash; and asks what it "
            "actually means in detail."]),
        ("Every kasiṇa, tested against the same standard", [
            "Mahākaccāna's answer runs through all ten kasiṇas from AN "
            "10.25 in turn &mdash; earth through consciousness &mdash; "
            "applying the identical logic to each: some regard this "
            "attainment as ultimate and are reborn thinking so, but the "
            "Buddha saw its limits, its drawback, and the escape from "
            "it, which is precisely how he reached true peace."]),
        ("Peace found through seeing limits, not through greater "
         "attainment", [
            "The discourse's underlying claim is pointed: the Buddha's "
            "peace of heart doesn't come from having mastered a kasiṇa "
            "attainment beyond what others reach, but from correctly "
            "seeing the limits, drawback, and escape of every such "
            "attainment &mdash; recognizing what looks like an ultimate "
            "goal as merely one more thing to see through."]),
    ],
    terms=[
        ("kumārikapañhesu",
         "&ldquo;in &lsquo;The Maidens' Questions&rsquo;&rdquo; "
         "&mdash; the specific earlier source Kāḷī quotes the Buddha's "
         "verse from."),
        ("santaṁ padamajjhagamaṁ",
         "&ldquo;I've reached the goal, peace of heart&rdquo; &mdash; "
         "the verse's own opening line, the statement Kāḷī asks to "
         "have explained."),
        ("pathavīkasiṇasamāpattiṁ",
         "&ldquo;the attainment of the meditation on universal "
         "earth&rdquo; &mdash; the first kasiṇa this discourse tests "
         "against the same standard, using AN 10.25's own list."),
        ("ādiñca disvā ādīnavañca nissaraṇañca",
         "&ldquo;he saw the beginning, the drawback, and the "
         "escape&rdquo; &mdash; Mahākaccāna's own explanation for why "
         "the Buddha, unlike others, reached genuine peace."),
        ("ayamaggo, ayaṁ paṭipadā",
         "&ldquo;what is the path and what is not the path&rdquo; "
         "&mdash; part of the Buddha's own knowledge and vision, "
         "distinguishing genuine liberation from mistaking attainment "
         "for the goal."),
    ],
    text_intro=(
        "The discourse in full: a quoted verse, and Mahākaccāna's "
        "explanation built on all ten kasiṇas from AN 10.25. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A cryptic verse, quoted"),
        ("p", "&sect;1", "an10.26:1.1-3.1"),
        ("h3", "Every kasiṇa, tested against the same standard"),
        ("p", "&sect;2", "an10.26:4.1-5.13"),
        ("h3", "The verse, explained"),
        ("p", "&sect;3", "an10.26:6.1-6.5"),
    ],
    quiz=[
        {"q": "What does Kāḷī bring to Mahākaccāna?",
         "opts": [
             "A personal complaint",
             "A quoted verse from &lsquo;The Maidens' Questions&rsquo; "
             "asking for its detailed meaning",
             "A donation of robes",
             "A request for ordination"],
         "correct": 1,
         "expl": "A specific cryptic verse requiring careful exegesis."},
        {"q": "What list does Mahākaccāna's answer run through in "
              "full?",
         "opts": [
             "The five hindrances",
             "All ten kasiṇas from AN 10.25, earth through "
             "consciousness",
             "The nine progressive attainments",
             "The four noble truths"],
         "correct": 1,
         "expl": "Putting the bare list from AN 10.25 to direct "
                 "explanatory use."},
        {"q": "What mistake does Mahākaccāna say some ascetics and "
              "brahmins make regarding each kasiṇa?",
         "opts": [
             "They never attempt them at all",
             "They regard each attainment as the ultimate goal and are "
             "reborn accordingly",
             "They abandon them too quickly",
             "They confuse them with each other"],
         "correct": 1,
         "expl": "Mistaking a meditative attainment for the final goal "
                 "itself."},
        {"q": "According to the guide, where does the Buddha's peace "
              "of heart actually come from?",
         "opts": [
             "From mastering a kasiṇa attainment beyond what others "
             "reach",
             "From correctly seeing the limits, drawback, and escape of "
             "every such attainment",
             "From avoiding meditation entirely",
             "From social isolation alone"],
         "correct": 1,
         "expl": "Insight into limits, not superior attainment, is the "
                 "discourse's real point."},
        {"q": "What three things did the Buddha see regarding each "
              "kasiṇa attainment?",
         "opts": [
             "Its beauty, its rarity, and its difficulty",
             "Its beginning, its drawback, and the escape from it",
             "Its cost, its duration, and its popularity",
             "Nothing in particular"],
         "correct": 1,
         "expl": "The specific threefold insight Mahākaccāna names as "
                 "the difference between the Buddha and others."},
        {"q": "Who questions whom in this discourse?",
         "opts": [
             "The Buddha questions Mahākaccāna",
             "The laywoman Kāḷī questions Venerable Mahākaccāna",
             "Ānanda questions Mahākaccāna",
             "Sāriputta questions Kāḷī"],
         "correct": 1,
         "expl": "A lay follower seeking exegesis from a senior "
                 "disciple, in the Buddha's own absence from the "
                 "narrative."},
    ],
    marginalia=[
        ("A cryptic verse", [
            "&ldquo;I've reached the goal,",
            "peace of heart&rdquo; &mdash; what does",
            "this actually mean?",
        ]),
        ("Ten kasiṇas, one test", [
            "earth, water, fire, air,",
            "colors, space, consciousness &mdash;",
            "each mistaken as final",
        ]),
        ("Peace through seeing limits", [
            "not a higher rung,",
            "but seeing the drawback",
            "and the way out, clearly",
        ]),
        ("Cross-references", [
            "AN 10.25 &middot; the same ten kasiṇas, here put to direct "
            "explanatory use",
            "AN 10.27 &middot; next, The Great Questions (1st)",
        ]),
    ],
    further=[
        '<a href="%s/an10.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.25.html">AN 10.25 &middot; Meditation on Universals</a> &mdash; '
        "previous, the same ten kasiṇas this discourse explains through.",
        '<a href="an-10.27.html">AN 10.27 &middot; The Great Questions (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.27 — Mahāpañhāsutta (1st)
# --------------------------------------------------------------------------- #
page(
    27, "Mahāpañhā", "The Great Questions (1st)",
    vagga=VAGGA_3,
    meta_title="AN 10.27 — The Great Questions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the first Mahāpañhāsutta, the Buddha's own catechism running "
        "one through ten — from all beings sustained by food to the "
        "ten unskillful deeds — that outsiders could never answer. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "Several mendicants, wanderers of other "
                     "religions, and the Buddha"),
        ("Form", "A wanderers' challenge deferred to the Buddha, then "
                 "ten numbered items each with its own referent"),
        ("Length", "~3 minutes to read"),
        ("A catechism outsiders cannot answer", "The Buddha claims no "
         "one but himself, his disciples, or those who've heard it "
         "from them could satisfactorily answer this one-through-ten "
         "formula"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "compressed by the source's own peyyāla, worth "
                       "reading for its ascending structure"),
    ],
    why=(
        "Wanderers of other religions challenge some mendicants: "
        "since both they and the Buddha teach disciples to directly "
        "know all things, what's the difference? Brought to the "
        "Buddha, the answer is a formula running from one thing "
        "through ten, each with its own specific referent, that only "
        "the Buddha, his disciples, or those who've heard it from them "
        "could ever satisfactorily answer."),
    guide=[
        ("The teaching in one sentence", [
            "Becoming completely disillusioned, dispassionate, and "
            "freed regarding one thing (all beings sustained by food) "
            "through ten things (the ten ways of performing unskillful "
            "deeds), seeing each set's limits and fully comprehending "
            "its meaning, a mendicant makes an end of suffering in "
            "this very life."]),
        ("A challenge neither approved nor rejected", [
            "When wanderers ask what distinguishes the Buddha's "
            "teaching to &lsquo;directly know all things&rsquo; from "
            "their own identical-sounding instruction, the mendicants "
            "don't attempt an answer on the spot; they neither approve "
            "nor reject the wanderers' framing, resolving instead to "
            "learn the answer from the Buddha himself &mdash; the same "
            "pattern of restraint already met at AN 9.12."]),
        ("A formula only the Buddha's tradition can answer", [
            "The Buddha's own claim is striking in its exclusivity: "
            "questioned about this one-through-ten formula, wanderers "
            "of other religions would be stumped and frustrated, "
            "&lsquo;because they're out of their element&rsquo; "
            "&mdash; no one anywhere, gods or humans, could provide a "
            "satisfying answer except the Realized One, his disciple, "
            "or someone who has heard it from them."]),
        ("Ten items, each a specific referent for its number", [
            "Each number from one to ten names a specific doctrinal "
            "referent: one (all beings sustained by food), two (name "
            "and form), three (three feelings), four (four foods), "
            "five (five grasping aggregates), six (six interior sense "
            "fields), seven (seven planes of consciousness), eight "
            "(eight worldly conditions), nine (nine abodes of sentient "
            "beings, the same list met at AN 9.24), and ten (ten ways "
            "of performing unskillful deeds) &mdash; a complete "
            "ascending survey of the tradition's own foundational "
            "categories."]),
    ],
    terms=[
        ("sabbadhammaṁ abhijānātha, sabbadhammaṁ abhiññāya",
         "&ldquo;directly know all things... having directly known "
         "all things&rdquo; &mdash; the wanderers' own claim to teach "
         "identically to the Buddha, prompting this discourse's real "
         "answer."),
        ("na kho ahaṁ, bhikkhave, aññaṁ ekapuggalampi samanupassāmi",
         "&ldquo;I don't see anyone... who could provide a satisfying "
         "answer to these questions&rdquo; &mdash; the Buddha's own "
         "exclusive claim regarding this formula."),
        ("ekaṁ dhammaṁ... sabbe sattā āhāraṭṭhitikā",
         "&ldquo;one thing... all sentient beings are sustained by "
         "food&rdquo; &mdash; the first and most fully explained item "
         "in the ascending formula."),
        ("nava sattāvāsā",
         "&ldquo;the nine abodes of sentient beings&rdquo; &mdash; the "
         "ninth item, identical to the classification already met at "
         "AN 9.24."),
        ("dasa akusalakammapathā",
         "&ldquo;the ten ways of performing unskillful deeds&rdquo; "
         "&mdash; the tenth and final item, closing the ascending "
         "formula."),
    ],
    text_intro=(
        "The discourse in full, as it survives: a wanderers' "
        "challenge deferred to the Buddha, then ten numbered items, "
        "each with its own referent. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A challenge from wanderers, deferred"),
        ("p", "&sect;1", "an10.27:1.1-4.3"),
        ("h3", "The Buddha's answer: one thing, fully explained"),
        ("p", "&sect;2", "an10.27:5.1-10.8"),
        ("h3", "Two things through three things"),
        ("p", "&sect;3", "an10.27:11.1-12.7"),
        ("h3", "Four things through five things"),
        ("p", "&sect;4", "an10.27:13.1-14.7"),
        ("h3", "Six things through seven things"),
        ("p", "&sect;5", "an10.27:15.1-16.7"),
        ("h3", "Eight things through nine things"),
        ("p", "&sect;6", "an10.27:17.1-18.7"),
        ("h3", "Ten things, fully explained"),
        ("p", "&sect;7", "an10.27:19.1-19.8"),
    ],
    quiz=[
        {"q": "What challenge do wanderers of other religions raise?",
         "opts": [
             "A challenge about monastic robes",
             "That they too teach disciples to &lsquo;directly know "
             "all things,&rsquo; asking what distinguishes this from "
             "the Buddha's identical-sounding teaching",
             "A challenge about almsfood",
             "A challenge about rebirth"],
         "correct": 1,
         "expl": "Prompting the mendicants to defer to the Buddha "
                 "rather than answer on the spot."},
        {"q": "What does the Buddha claim about who can answer this "
              "one-through-ten formula?",
         "opts": [
             "Anyone with sufficient education can answer it",
             "No one anywhere could provide a satisfying answer except "
             "the Realized One, his disciple, or someone who has heard "
             "it from them",
             "Only kings and nobles can answer it",
             "The wanderers themselves can answer it easily"],
         "correct": 1,
         "expl": "A striking claim of exclusivity for this particular "
                 "formula."},
        {"q": "What is the first item in the formula, given the "
              "fullest explanation?",
         "opts": [
             "The four noble truths",
             "All sentient beings are sustained by food",
             "The five aggregates",
             "The eightfold path"],
         "correct": 1,
         "expl": "Fully spelled out before the source's own peyyāla "
                 "compresses the remaining items."},
        {"q": "What is the ninth item, and where has this project "
              "already met it?",
         "opts": [
             "The eight worldly conditions, not met elsewhere",
             "The nine abodes of sentient beings, identical to the "
             "classification at AN 9.24",
             "The seven planes of consciousness, met at AN 9.31",
             "The six sense fields, met at AN 9.65"],
         "correct": 1,
         "expl": "The same nine-fold cosmological list already given "
                 "in full earlier in this project."},
        {"q": "What is the tenth and final item?",
         "opts": [
             "The ten fetters",
             "The ten ways of performing unskillful deeds",
             "The ten powers of a Realized One",
             "The ten kasiṇas"],
         "correct": 1,
         "expl": "Closing the ascending formula from one thing to ten."},
        {"q": "How did the mendicants respond to the wanderers' "
              "challenge in the moment?",
         "opts": [
             "They argued forcefully against it",
             "They neither approved nor rejected it, resolving to ask "
             "the Buddha directly — the same restraint already met at "
             "AN 9.12",
             "They agreed with the wanderers immediately",
             "They refused to engage at all"],
         "correct": 1,
         "expl": "A model of restraint this project has already met "
                 "elsewhere."},
    ],
    marginalia=[
        ("A challenge, deferred", [
            "&ldquo;we too teach this&rdquo; &mdash;",
            "neither approved nor argued,",
            "but brought to the Buddha",
        ]),
        ("One through ten, ascending", [
            "food, name-form, feelings,",
            "foods, aggregates, sense fields,",
            "consciousness, conditions",
        ]),
        ("A formula none else can answer", [
            "outsiders, stumped, frustrated &mdash;",
            "out of their own element,",
            "facing this alone",
        ]),
        ("Cross-references", [
            "AN 9.12, AN 9.24 &middot; earlier meetings with the "
            "restraint pattern and the nine abodes list",
            "AN 10.26 &middot; previous",
            "AN 10.28 &middot; next, the same formula reframed "
            "positively",
        ]),
    ],
    further=[
        '<a href="%s/an10.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.24.html">AN 9.24 &middot; Abodes of Sentient Beings</a> &mdash; the '
        "identical ninth item in this discourse's formula.",
        '<a href="an-10.26.html">AN 10.26 &middot; With Kāḷī</a> &mdash; previous.',
        '<a href="an-10.28.html">AN 10.28 &middot; The Great Questions (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.28 — Mahāpañhāsutta (2nd)
# --------------------------------------------------------------------------- #
page(
    28, "Mahāpañhā", "The Great Questions (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 10.28 — The Great Questions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the second Mahāpañhāsutta, a nun's own confident answer to "
        "lay followers, reframing AN 10.27's one-through-ten formula "
        "around positive development, later confirmed word for word "
        "by the Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kajaṅgalā, in a bamboo grove"),
        ("Speakers", "The nun Kajaṅgalikā, lay followers, and, at the "
                     "close, the Buddha"),
        ("Form", "A nun's independent explanation of the same formula "
                 "title as AN 10.27, later confirmed by the Buddha"),
        ("Length", "~4 minutes to read"),
        ("The same formula, developmental rather than "
         "disillusionment-focused", "Where AN 10.27 framed each item "
         "as something to grow disillusioned with, this version frames "
         "most items as something to develop"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "compressed by peyyāla, worth comparing item by "
                       "item against AN 10.27"),
    ],
    why=(
        "Lay followers bring the nun Kajaṅgalikā the same "
        "&lsquo;Great Questions&rsquo; formula met at AN 10.27, and, "
        "admitting she hasn't heard its explanation directly from the "
        "Buddha, she offers her own understanding &mdash; largely "
        "reframing the items as things to be developed rather than "
        "grown disillusioned with &mdash; which the Buddha later "
        "confirms he would have answered exactly the same way."),
    guide=[
        ("The teaching in one sentence", [
            "Becoming disillusioned regarding one thing (food) and "
            "developed in items two through ten &mdash; name and form, "
            "three feelings, the four kinds of mindfulness meditation, "
            "the five faculties, the six elements of escape, the seven "
            "awakening factors, the noble eightfold path, the nine "
            "abodes of sentient beings, and the ten ways of performing "
            "skillful deeds &mdash; a mendicant makes an end of "
            "suffering in this very life."]),
        ("A nun's honest disclaimer, then confident teaching", [
            "Kajaṅgalikā doesn't claim to be repeating something heard "
            "directly from the Buddha or senior mendicants; she states "
            "plainly that this is &lsquo;how it seems to me,&rsquo; "
            "then proceeds to teach the full formula with evident "
            "confidence &mdash; honesty about her source paired with "
            "genuine authority in the content."]),
        ("Several items reframed around development, not just "
         "disillusionment", [
            "Compared to AN 10.27, this version shifts several middle "
            "items to a developmental register: the fourth item "
            "becomes the four kinds of mindfulness meditation, the "
            "fifth the five faculties, the sixth the six elements of "
            "escape, the seventh the seven awakening factors, and the "
            "eighth the noble eightfold path &mdash; the classic "
            "bodhipakkhiyā dhammā, qualities on the side of awakening, "
            "replacing AN 10.27's more purely disillusionment-focused "
            "items at these same positions."]),
        ("Confirmed word for word by the Buddha himself", [
            "When the lay followers bring Kajaṅgalikā's answer back to "
            "the Buddha, his response is unqualified: &lsquo;the nun "
            "Kajaṅgalikā is astute, she has great wisdom... I would "
            "answer it in exactly the same way&rsquo; &mdash; the same "
            "pattern of confirmation, rather than correction, already "
            "met when Sāriputta taught AN 10.4's identical chain "
            "unaltered."]),
    ],
    terms=[
        ("nāhaṁ etaṁ bhagavato sammukhā sutaṁ",
         "&ldquo;I haven't heard and learned this in the presence of "
         "the Buddha&rdquo; &mdash; Kajaṅgalikā's own honest "
         "disclaimer, before offering her own understanding."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the fourth item in this version, replacing AN "
         "10.27's differently framed fourth item."),
        ("satta bojjhaṅgā",
         "&ldquo;the seven awakening factors&rdquo; &mdash; the "
         "seventh item, part of this version's shift toward the "
         "classic qualities on the side of awakening."),
        ("dasa kusalakammapathā",
         "&ldquo;the ten ways of performing skillful deeds&rdquo; "
         "&mdash; the tenth and final item, the positive counterpart "
         "to AN 10.27's ten unskillful ways."),
        ("evameva kho ahaṁ, gahapatayo, byākareyyaṁ",
         "&ldquo;I would answer it in exactly the same way&rdquo; "
         "&mdash; the Buddha's own closing confirmation of "
         "Kajaṅgalikā's independent explanation."),
    ],
    text_intro=(
        "The discourse in full, as it survives: a nun's own "
        "explanation of the same formula named at AN 10.27, later "
        "confirmed by the Buddha. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A question brought to a nun"),
        ("p", "&sect;1", "an10.28:1.1-3.5"),
        ("h3", "One thing: sustained by food"),
        ("p", "&sect;2", "an10.28:4.1-4.7"),
        ("h3", "Two things through three things"),
        ("p", "&sect;3", "an10.28:5.1-5.9"),
        ("h3", "Four things: the four kinds of mindfulness meditation"),
        ("p", "&sect;4", "an10.28:6.1-6.7"),
        ("h3", "Five things through eight things"),
        ("p", "&sect;5", "an10.28:7.1-7.13"),
        ("h3", "Nine things: the nine abodes of sentient beings"),
        ("p", "&sect;6", "an10.28:8.1-8.7"),
        ("h3", "Ten things: the ten ways of performing skillful deeds"),
        ("p", "&sect;7", "an10.28:9.1-9.7"),
        ("h3", "Confirmed by the Buddha himself"),
        ("p", "&sect;8", "an10.28:10.1-11.4"),
    ],
    quiz=[
        {"q": "What does Kajaṅgalikā say about the source of her "
              "answer?",
         "opts": [
             "That she heard it directly from the Buddha",
             "That she hasn't heard it from the Buddha or senior "
             "mendicants, but offers her own understanding",
             "That she refuses to answer at all",
             "That only the Buddha can answer such questions"],
         "correct": 1,
         "expl": "Honest disclaimer paired with confident teaching."},
        {"q": "How does this version's fourth item differ from AN "
              "10.27's?",
         "opts": [
             "It is identical",
             "This version names the four kinds of mindfulness "
             "meditation, part of a developmental reframing of several "
             "middle items",
             "This version omits a fourth item entirely",
             "This version reverses the numbering"],
         "correct": 1,
         "expl": "A shift toward the classic bodhipakkhiyā dhammā at "
                 "several positions."},
        {"q": "What happens when the lay followers bring Kajaṅgalikā's "
              "answer to the Buddha?",
         "opts": [
             "He corrects several errors in her explanation",
             "He confirms it without qualification, saying he would "
             "have answered exactly the same way",
             "He refuses to comment on it",
             "He contradicts her entirely"],
         "correct": 1,
         "expl": "Unqualified confirmation, the same pattern already "
                 "met when Sāriputta taught AN 10.4's chain unaltered."},
        {"q": "What is the tenth and final item in this version?",
         "opts": [
             "The ten unskillful ways of acting",
             "The ten ways of performing skillful deeds",
             "The ten fetters",
             "The ten powers of a Realized One"],
         "correct": 1,
         "expl": "The positive counterpart to AN 10.27's tenth item."},
        {"q": "What items do this version and AN 10.27 share exactly?",
         "opts": [
             "None; every item differs",
             "The first item (food) and the ninth item (nine abodes of "
             "sentient beings)",
             "Only the tenth item",
             "All ten items are identical"],
         "correct": 1,
         "expl": "Some positions match exactly while several middle "
                 "items are reframed developmentally."},
        {"q": "What quality does the Buddha attribute to Kajaṅgalikā?",
         "opts": [
             "Excessive caution",
             "Astuteness and great wisdom",
             "Uncertainty about the teaching",
             "A tendency to make errors"],
         "correct": 1,
         "expl": "High praise, closing the discourse with full "
                 "confirmation."},
    ],
    marginalia=[
        ("Honest, then confident", [
            "&ldquo;I haven't heard this",
            "from the Buddha himself&rdquo; &mdash;",
            "then answers fully",
        ]),
        ("Development, not just release", [
            "mindfulness, faculties,",
            "escape, awakening factors,",
            "the eightfold path itself",
        ]),
        ("Confirmed, not corrected", [
            "&ldquo;exactly the same way",
            "I would answer&rdquo; &mdash; the Buddha's",
            "own unqualified praise",
        ]),
        ("Cross-references", [
            "AN 10.4 &middot; the same confirmation-not-correction "
            "pattern",
            "AN 10.27 &middot; the identical formula title, there "
            "framed around disillusionment",
            "AN 10.29 &middot; next, Kosala (1st)",
        ]),
    ],
    further=[
        '<a href="%s/an10.28/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.4.html">AN 10.4 &middot; Vital Conditions (2nd)</a> &mdash; the same '
        "confirmation-not-correction pattern.",
        '<a href="an-10.27.html">AN 10.27 &middot; The Great Questions (1st)</a> &mdash; '
        "previous, the identical formula title.",
        '<a href="an-10.29.html">AN 10.29 &middot; Kosala (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.29 — Kosalasutta (1st)
# --------------------------------------------------------------------------- #
page(
    29, "Kosala", "Kosala (1st)",
    vagga=VAGGA_3,
    meta_title="AN 10.29 — Kosala (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the first Kosalasutta, an ascending cosmological survey from "
        "King Pasenadi through a thousandfold galaxy to the kasiṇas, "
        "liberations, and the Buddha's own claim to full "
        "extinguishment. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A cascading series of &lsquo;foremost, yet it "
                 "decays&rsquo; comparisons, ascending from a king to "
                 "cosmology to meditative attainment"),
        ("Length", "~6 minutes to read"),
        ("This chapter's most sweeping single discourse", "Moving "
         "from a named living king through galactic cosmology to the "
         "kasiṇas, the eight liberations, and finally the Buddha's own "
         "self-defense"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "the densest and most wide-ranging discourse in "
                       "this chapter"),
    ],
    why=(
        "King Pasenadi is foremost within Kāsi and Kosala, yet he "
        "decays and perishes; the Great Divinity is foremost within an "
        "entire galaxy, yet it too decays; even the gods of streaming "
        "radiance, the best kasiṇa, the best liberation, the best "
        "practice, the best perception, and the best outsider view all "
        "decay and perish &mdash; a learned noble disciple grows "
        "disillusioned with every one of them, down to the Buddha's own "
        "claim of full extinguishment through understanding the six "
        "fields of contact."),
    guide=[
        ("The teaching in one sentence", [
            "From a named king to the vastest cosmological scales to "
            "the subtlest meditative attainments, everything held up "
            "as &lsquo;the foremost&rsquo; still decays and perishes, "
            "and a learned noble disciple grows disillusioned with "
            "every one of them in turn, down to the Buddha's own "
            "understanding of the six fields of contact."]),
        ("An ascending scale, from a king to a galaxy", [
            "The discourse's opening movement escalates deliberately: "
            "King Pasenadi, foremost within Kāsi and Kosala; then a "
            "thousandfold galaxy containing a thousand of everything "
            "&mdash; moons, suns, mountains, oceans, heavens &mdash; "
            "with the Great Divinity foremost within it; then, at "
            "cosmic contraction, the gods of streaming radiance, "
            "foremost of all &mdash; each level vastly exceeding the "
            "one before, and each still subject to decay."]),
        ("The same test applied to meditative attainment", [
            "Having exhausted cosmological scale, the discourse turns "
            "the identical test onto meditation itself: the best of "
            "the ten kasiṇas (universal consciousness, already met at "
            "AN 10.25), the best of the eight liberations (the white "
            "kasiṇa-like attainment), the best of four ways of "
            "practice, the best of four perceptions, the best outsider "
            "view, and the best claim to ultimate purity of spirit "
            "&mdash; every one still decaying, still perishing."]),
        ("A self-defense, closing on the Buddha's own claim", [
            "The discourse ends unexpectedly personal: the Buddha "
            "names his own claim to full extinguishment through "
            "understanding the six fields of contact, then directly "
            "addresses a misrepresentation circulating against him "
            "&mdash; that he denies advocating complete understanding "
            "of sensual pleasures, forms, and feelings &mdash; "
            "insisting plainly that he does advocate exactly this, and "
            "full extinguishment through not grasping."]),
    ],
    terms=[
        ("rājā pasenadi kosalo aggamakkhāyati",
         "&ldquo;King Pasenadi is said to be the foremost&rdquo; "
         "&mdash; the discourse's opening comparison, the smallest "
         "scale before its cosmological ascent."),
        ("sahassī cūḷanikā lokadhātu",
         "&ldquo;a galaxy&rdquo; &mdash; literally a &ldquo;minor "
         "thousandfold world-system,&rdquo; containing a thousand of "
         "every cosmological feature."),
        ("ābhassarā devā",
         "&ldquo;the gods of streaming radiance&rdquo; &mdash; the "
         "beings most sentient beings migrate to when the cosmos "
         "contracts, foremost at that scale."),
        ("viññāṇakasiṇaṁ",
         "&ldquo;the meditation on universal consciousness&rdquo; "
         "&mdash; named here as the best of the ten kasiṇas already "
         "met in full at AN 10.25."),
        ("channaṁ phassāyatanānaṁ samudayañca atthaṅgamañca assādañca "
         "ādīnavañca nissaraṇañca yathābhūtaṁ viditvā",
         "&ldquo;truly understanding the origin, disappearance, "
         "gratification, drawback, and escape of the six fields of "
         "contact&rdquo; &mdash; the Buddha's own basis for claiming "
         "full extinguishment, closing the discourse."),
    ],
    text_intro=(
        "The discourse in full: an ascending series of comparisons, "
        "from a king through cosmology to the Buddha's own claim of "
        "extinguishment. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A king, and a galaxy"),
        ("p", "&sect;1", "an10.29:1.1-3.7"),
        ("h3", "The best kasiṇa, and the best liberation"),
        ("p", "&sect;2", "an10.29:4.1-14.6"),
        ("h3", "The best practice, perception, and outsider view"),
        ("p", "&sect;3", "an10.29:15.1-20.7"),
        ("h3", "The Buddha's own claim, and a misrepresentation "
               "corrected"),
        ("p", "&sect;4", "an10.29:21.1-21.5"),
    ],
    quiz=[
        {"q": "How does this discourse's opening comparison escalate?",
         "opts": [
             "It stays at a single fixed scale throughout",
             "From King Pasenadi, foremost in Kāsi and Kosala, to a "
             "thousandfold galaxy, to the gods of streaming radiance "
             "at cosmic contraction",
             "From the smallest insect to the largest animal",
             "From one mendicant to the whole monastic community"],
         "correct": 1,
         "expl": "A deliberate cosmological ascent, each level vastly "
                 "exceeding the one before."},
        {"q": "What is said to be the best of the ten kasiṇas?",
         "opts": [
             "The earth kasiṇa",
             "The meditation on universal consciousness, already met "
             "at AN 10.25",
             "The fire kasiṇa",
             "The white kasiṇa"],
         "correct": 1,
         "expl": "Applying the same &lsquo;foremost, yet it decays"
                 "&rsquo; test to meditative attainment."},
        {"q": "What single claim does the Buddha make about himself, "
              "closing the discourse?",
         "opts": [
             "That he has never taught about sensual pleasures",
             "Full extinguishment through truly understanding the "
             "origin, disappearance, gratification, drawback, and "
             "escape of the six fields of contact",
             "That he has surpassed the gods of streaming radiance in "
             "power",
             "That extinguishment is unattainable"],
         "correct": 1,
         "expl": "A personal claim closing an otherwise impersonal "
                 "cosmological survey."},
        {"q": "What misrepresentation does the Buddha address directly?",
         "opts": [
             "That he claims to be a god",
             "That he doesn't advocate complete understanding of "
             "sensual pleasures, forms, or feelings",
             "That he has never taught the four noble truths",
             "That he denies rebirth exists"],
         "correct": 1,
         "expl": "A false claim circulating against him, corrected "
                 "plainly in the discourse's final lines."},
        {"q": "What single refrain does this discourse repeat after "
              "every comparison?",
         "opts": [
             "A verse of praise",
             "That even the foremost decays and perishes, and a "
             "learned noble disciple grows disillusioned, desire "
             "fading even for the foremost",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "The same disillusionment logic applied consistently "
                 "across every scale, from king to cosmos to meditation."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare, sweeping doctrinal survey, without narrative "
                 "frame — unlike its companion, AN 10.30."},
    ],
    marginalia=[
        ("A king, then a galaxy", [
            "Pasenadi, foremost;",
            "then a thousandfold cosmos,",
            "each still decaying",
        ]),
        ("The same test, applied higher", [
            "best kasiṇa, best",
            "liberation, best practice &mdash;",
            "all still perish, still fade",
        ]),
        ("A personal close", [
            "the Buddha's own claim,",
            "and a lie corrected &mdash;",
            "plainly, without evasion",
        ]),
        ("Cross-references", [
            "AN 10.25 &middot; the same ten kasiṇas, here ranked and "
            "tested",
            "AN 10.28 &middot; previous",
            "AN 10.30 &middot; next, Kosala (2nd)",
        ]),
    ],
    further=[
        '<a href="%s/an10.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.25.html">AN 10.25 &middot; Meditation on Universals</a> &mdash; the '
        "same ten kasiṇas, here ranked and tested.",
        '<a href="an-10.28.html">AN 10.28 &middot; The Great Questions (2nd)</a> &mdash; '
        "previous.",
        '<a href="an-10.30.html">AN 10.30 &middot; Kosala (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.30 — Kosalasutta (2nd) — closes ch.3 Mahāvagga
# --------------------------------------------------------------------------- #
page(
    30, "Kosala", "Kosala (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 10.30 — Kosala (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the second Kosalasutta, closing this chapter with King "
        "Pasenadi's own devoted visit after a military victory, "
        "explaining his reverence through ten qualities he sees in the "
        "Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "King Pasenadi of Kosala, and the Buddha"),
        ("Form", "A vivid narrative visit, then ten reasons for "
                 "devotion, each closing the same refrain"),
        ("Length", "~4 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Mahāvagga</em>, the third chapter of the Tens; "
         "the source's own untranslated closing verse names all ten "
         "discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "warm, personal narrative closing a chapter of "
                       "otherwise abstract doctrine"),
    ],
    why=(
        "Fresh from a military victory, King Pasenadi visits the "
        "Buddha, prostrating with unusual physical affection and "
        "announcing his own name twice over; asked why, he names ten "
        "reasons for his devotion &mdash; the Buddha's welfare-focused "
        "practice, his ethics, his forest dwelling, his contentment, "
        "his worthiness of offerings, his access to elevated "
        "conversation, his mastery of the four absorptions, and his "
        "three knowledges."),
    guide=[
        ("The teaching in one sentence", [
            "King Pasenadi explains his own deference and manifest "
            "love for the Buddha through ten qualities he has "
            "observed: welfare-focused practice, mature ethics, forest "
            "dwelling, contentment with any requisites, worthiness of "
            "offerings, access to elevated conversation, mastery of "
            "the four absorptions, and the three knowledges."]),
        ("A king's unguarded physical devotion", [
            "The discourse's opening is unusually intimate: a king "
            "fresh from military victory approaches the Buddha's own "
            "closed door quietly, without hurrying, clears his throat "
            "and knocks as instructed, then once inside bows with his "
            "head at the Buddha's feet, caressing them and covering "
            "them with kisses, announcing his own name twice as if "
            "compelled to."]),
        ("Ten reasons, echoing this chapter's earlier discourses", [
            "Several of Pasenadi's ten reasons directly echo content "
            "already met earlier in this project: worthiness of "
            "offerings recalls AN 9.10 and AN 10.16's classifications, "
            "and the closing sequence of four absorptions plus three "
            "knowledges precisely matches AN 10.8 and AN 10.10's own "
            "&lsquo;impressive all around&rsquo; formula, here voiced "
            "not about a hypothetical mendicant but about the Buddha "
            "himself, by a king who has personally witnessed it."]),
        ("Closing the chapter on personal testimony", [
            "With this discourse, <em>Mahāvagga</em> closes not on "
            "abstract doctrine but on a specific person's specific "
            "devotion &mdash; the source's own untranslated colophon "
            "and chapter-summary verse name all ten discourses of the "
            "chapter by their opening words, closing a chapter that "
            "began with a lion's roar and ends with a king's kiss."]),
    ],
    terms=[
        ("sīse añjaliṁ paṇāmetvā",
         "&ldquo;bowed with his head at the Buddha's feet, caressing "
         "them and covering them with kisses&rdquo; &mdash; the "
         "discourse's own vivid image of the king's physical devotion."),
        ("bahujanahitāya bahujanasukhāya paṭipanno",
         "&ldquo;practicing for the welfare and happiness of the "
         "people&rdquo; &mdash; the first of the king's ten named "
         "reasons for his reverence."),
        ("āraññiko",
         "&ldquo;lives in the wilderness&rdquo; &mdash; the third "
         "reason, echoing the same forest-dwelling quality already met "
         "at AN 10.8-10."),
        ("cattāro jhāne nikāmalābhī",
         "&ldquo;gets the four absorptions... when he wants&rdquo; "
         "&mdash; the ninth reason, matching AN 10.8's own ninth "
         "quality exactly."),
        ("mahāvaggo tatiyo",
         "&ldquo;the third chapter, Mahāvagga, is finished&rdquo; "
         "&mdash; the source's own untranslated colophon closing this "
         "chapter."),
    ],
    text_intro=(
        "The discourse in full: King Pasenadi's devoted visit, and "
        "ten reasons for his reverence. The source's own closing "
        "colophon and chapter-summary verse are untranslated in the "
        "English and are described rather than quoted here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A king's visit, after victory"),
        ("p", "&sect;1", "an10.30:1.1-3.2"),
        ("h3", "Ten reasons for devotion"),
        ("p", "&sect;2", "an10.30:4.1-13.2"),
        ("h3", "Closing"),
        ("p", "&sect;3", "an10.30:14.1-14.4"),
    ],
    quiz=[
        {"q": "What does King Pasenadi do upon entering the Buddha's "
              "dwelling?",
         "opts": [
             "He demands an audience formally",
             "He bows with his head at the Buddha's feet, caressing "
             "and kissing them, and announces his own name twice",
             "He refuses to enter without an invitation",
             "He sends a messenger instead"],
         "correct": 1,
         "expl": "An unusually intimate display of physical devotion "
                 "from a reigning king."},
        {"q": "What occasion prompts this visit?",
         "opts": [
             "A religious festival",
             "Returning from combat after winning a battle",
             "His coronation",
             "A drought in his kingdom"],
         "correct": 1,
         "expl": "Fresh from military victory, the king seeks out the "
                 "Buddha directly."},
        {"q": "What do the king's ninth and tenth reasons for devotion "
              "match exactly?",
         "opts": [
             "Nothing found elsewhere in this project",
             "AN 10.8 and AN 10.10's own &lsquo;impressive all "
             "around&rsquo; formula — four absorptions and the three "
             "knowledges",
             "AN 10.21's ten powers",
             "AN 10.13's ten fetters"],
         "correct": 1,
         "expl": "The same qualities, here voiced personally about the "
                 "Buddha by someone who has witnessed them."},
        {"q": "What does this discourse close, and how?",
         "opts": [
             "Nothing; the chapter continues past it",
             "<em>Mahāvagga</em>, the third chapter, with an "
             "untranslated colophon and uddāna verse naming all ten "
             "discourses",
             "The entire nipāta",
             "Only this single discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "According to the guide, what does this discourse "
              "contribute to closing the chapter?",
         "opts": [
             "More abstract doctrine",
             "Personal testimony — a specific king's specific "
             "devotion, closing a chapter that opened with a lion's "
             "roar",
             "A contradiction of the chapter's earlier teachings",
             "A repeat of AN 10.21's content"],
         "correct": 1,
         "expl": "From an abstract lion's roar to a concrete king's "
                 "kiss, bracketing the chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "No setting is given"],
         "correct": 1,
         "expl": "A specific narrative setting, unlike AN 10.29's bare "
                 "cosmological survey."},
    ],
    marginalia=[
        ("A king's devotion", [
            "fresh from battle, he",
            "kisses the Buddha's feet,",
            "names himself twice over",
        ]),
        ("Ten reasons, witnessed", [
            "welfare, ethics, forest,",
            "contentment, worthiness,",
            "absorption, and three knowledges",
        ]),
        ("From roar to kiss", [
            "the chapter opened with",
            "a lion's roar &mdash; closes now",
            "with a king's own tears",
        ]),
        ("Cross-references", [
            "AN 10.8, AN 10.10 &middot; the same closing qualities, "
            "there about a hypothetical mendicant",
            "AN 10.29 &middot; previous",
            "AN 10.31 &middot; next, opening ch.4, Upālivagga",
        ]),
    ],
    further=[
        '<a href="%s/an10.30/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.8.html">AN 10.8 &middot; Inspiring All Around: the Absorptions</a> '
        "&mdash; the same closing qualities, there about a hypothetical mendicant.",
        '<a href="an-10.29.html">AN 10.29 &middot; Kosala (1st)</a> &mdash; previous.',
    ],
)


VAGGA_4 = "<em>Upālivagga</em> &mdash; the fourth chapter of the Tens"


# --------------------------------------------------------------------------- #
# AN 10.31 — Upālisutta
# --------------------------------------------------------------------------- #
page(
    31, "Upāli", "With Upāli",
    vagga=VAGGA_4,
    meta_title="AN 10.31 — With Upāli | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upālisutta, opening the Tens' fourth chapter with the ten "
        "reasons the Buddha laid down training rules and recited the "
        "monastic code &mdash; the canonical preface behind every "
        "Vinaya rule. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-item answer"),
        ("Length", "~1 minute to read"),
        ("Chapter's namesake", "This discourse gives its own name to "
                               "the chapter, <em>Upālivagga</em>, the "
                               "Chapter on Upāli, which turns from "
                               "doctrine to monastic law for its next "
                               "ten discourses"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a plain list, but a famous one, reaching well "
                       "beyond this single discourse"),
    ],
    why=(
        "Upāli, the Buddha's foremost disciple in matters of monastic "
        "discipline, asks the most basic question there is about the "
        "rules he specializes in: why do they exist at all? The "
        "ten-item answer he receives is the very formula that opens "
        "the origin story of nearly every rule in the Vinaya "
        "Piṭaka."),
    guide=[
        ("The teaching in one sentence", [
            "Training rules and the monastic code exist for ten "
            "reasons: the Saṅgha's well-being and comfort, restraining "
            "difficult individuals and protecting well-behaved "
            "mendicants, guarding against defilements in this life and "
            "in lives to come, inspiring and strengthening confidence, "
            "and sustaining the true teaching and its training."]),
        ("A new chapter, and a sharper turn than most", [
            "As with every chapter-opener in this nipāta, the "
            "discourse lends its own subject to the chapter's name, "
            "<em>Upālivagga</em>. But this turn cuts deeper than most "
            "chapter breaks in the project: from here through AN "
            "10.40 the subject is monastic law itself &mdash; who may "
            "ordain, who may judge a dispute, what tears the Saṅgha "
            "apart &mdash; not the doctrinal chains and cosmologies of "
            "chapters 1&ndash;3."]),
        ("Upāli, asking his own specialty", [
            "It is fitting that this turn comes through Upāli, named "
            "elsewhere as foremost among disciples expert in the "
            "monastic code. He asks the most fundamental possible "
            "question about the code he knows best &mdash; why does "
            "it exist &mdash; and receives the canonical answer, "
            "unadorned by any triggering incident."]),
        ("A list larger than this discourse", [
            "This ten-item list is not unique to AN 10.31: it is the "
            "standard formula that opens the origin story of nearly "
            "every individual rule in the Vinaya Piṭaka's own "
            "rule-by-rule analysis, explaining why the Buddha "
            "responded to a given incident by legislating. Meeting it "
            "here, stated on its own with no incident attached, shows "
            "the formula in its purest form."]),
    ],
    terms=[
        ("pātimokkha",
         "the monastic code &mdash; the set of training rules recited "
         "in full by the assembled Saṅgha, traditionally each "
         "fortnight."),
        ("sikkhāpada",
         "&ldquo;training rule&rdquo; &mdash; an individual rule "
         "within the monastic code."),
        ("saṅghasuṭṭhutāya",
         "&ldquo;for the well-being of the Saṅgha&rdquo; &mdash; the "
         "first and broadest of the ten purposes."),
        ("saddhammaṭṭhitiyā",
         "&ldquo;for the continuation of the true teaching&rdquo; "
         "&mdash; the ninth purpose, framing the rules as a support "
         "for the Dhamma's survival, not an end in themselves."),
        ("vinayānuggahāya",
         "&ldquo;for the support of the training&rdquo; &mdash; the "
         "tenth and final purpose, closing the list."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten-item answer. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.31:1.1-1.2"),
        ("h3", "Ten reasons"),
        ("p", "&sect;2", "an10.31:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does Upāli ask the Buddha?",
         "opts": [
             "Why the Buddha meditates",
             "For how many reasons the Realized One laid down "
             "training rules and recited the monastic code",
             "How one becomes enlightened",
             "What extinguishment (Nibbāna) means"],
         "correct": 1,
         "expl": "The most basic possible question about the code "
                 "Upāli specializes in."},
        {"q": "How many reasons does the Buddha give?",
         "opts": ["Five", "Seven", "Ten", "Twelve"],
         "correct": 2,
         "expl": "A ten-item list, opening the Tens' fourth chapter."},
        {"q": "Which of these is NOT among the ten reasons?",
         "opts": [
             "The Saṅgha's well-being and comfort",
             "Restraining defilements affecting this life and lives "
             "to come",
             "Inspiring and increasing confidence",
             "Guaranteeing worldly prosperity for donors"],
         "correct": 3,
         "expl": "Not part of the list; the ten reasons concern the "
                 "Saṅgha and the teaching, not donors' fortunes."},
        {"q": "According to the guide, where else does this same "
              "ten-item list appear?",
         "opts": [
             "Nowhere else in the canon",
             "At the head of nearly every rule's origin story in the "
             "Vinaya Piṭaka's own rule-by-rule analysis",
             "Only in the Abhidhamma",
             "In the Jātaka tales"],
         "correct": 1,
         "expl": "The standard formula explaining why the Buddha "
                 "legislated, repeated rule after rule."},
        {"q": "What does this discourse contribute to its chapter?",
         "opts": [
             "Nothing in particular",
             "Its own subject, giving the chapter its name, "
             "Upālivagga, and opening a turn to monastic law",
             "A place name",
             "A simile"],
         "correct": 1,
         "expl": "As with every chapter-opener in this nipāta, the "
                 "discourse names its own chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "Unlike most chapter-openers in this nipāta, no "
                 "location is given here."},
    ],
    marginalia=[
        ("Ten reasons for law", [
            "well-being, comfort,",
            "restraint, confidence &mdash;",
            "why rules exist at all",
        ]),
        ("From doctrine to discipline", [
            "chapters one through three",
            "taught chains and cosmos; now",
            "the Saṅgha's own law",
        ]),
        ("Upāli's own question", [
            "the code's own expert",
            "asks why it exists &mdash; and hears",
            "the canonical answer",
        ]),
        ("Cross-references", [
            "AN 10.30 &middot; previous, closing ch.3, Mahāvagga",
            "AN 10.32 &middot; next, the grounds for suspending "
            "recitation",
        ]),
    ],
    further=[
        '<a href="%s/an10.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.30.html">AN 10.30</a> &mdash; previous, closing chapter 3, '
        "Mahāvagga.",
        '<a href="an-10.32.html">AN 10.32 &middot; Suspending the Recitation of the '
        'Monastic Code</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.32 — Pātimokkhaṭṭhapanāsutta
# --------------------------------------------------------------------------- #
page(
    32, "Pātimokkhaṭṭhapanā", "Suspending the Recitation of the Monastic Code",
    vagga=VAGGA_4,
    meta_title="AN 10.32 — Suspending the Recitation of the Monastic Code | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Pātimokkhaṭṭhapanāsutta, listing the ten grounds on which "
        "the fortnightly recitation of the monastic code must be "
        "suspended. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha, "
                     "continuing directly from AN 10.31"),
        ("Form", "A single question, a single ten-item answer, in "
                 "five matched pairs"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "procedural, but the paired structure is easy "
                       "to follow once seen"),
    ],
    why=(
        "Upāli asks a second, more practical question: on what "
        "grounds may the fortnightly recitation of the monastic code "
        "be called off? The Buddha's answer names five kinds of taint "
        "to the assembly's purity, each given twice &mdash; once for "
        "when the fact is settled, once for when it is still being "
        "argued over."),
    guide=[
        ("The teaching in one sentence", [
            "The recitation of the monastic code must be suspended on "
            "ten grounds: someone who has committed an expulsion "
            "offense, is unordained, has resigned the training, is a "
            "eunuch, or is a rapist of nuns is sitting in the "
            "assembly &mdash; or an unfinished discussion is underway "
            "about whether any of those five is true."]),
        ("Five taints, doubled into ten", [
            "The list is not ten independent items but five paired "
            "ones: for each of the five conditions that would taint "
            "the assembly, the Buddha names both the settled case "
            "(the person is confirmed to be so) and the unsettled "
            "case (the matter is still under discussion). Either "
            "version halts the recitation."]),
        ("Why purity of the assembly matters", [
            "The pātimokkha recitation is understood as an act the "
            "entire assembled Saṅgha performs together in a state of "
            "shared purity; a single disqualified or disputed presence "
            "is treated as compromising the whole act, not just that "
            "one person's participation &mdash; hence the recitation "
            "stops rather than merely excluding the individual on the "
            "spot."]),
        ("Continuing directly from AN 10.31", [
            "No new narrative frame opens this discourse: it reads as "
            "a second question from the same Upāli, in the same "
            "conversation, moving from why the code exists (AN 10.31) "
            "to when its recitation cannot proceed."]),
    ],
    terms=[
        ("pārājika",
         "an &ldquo;expulsion offense&rdquo; &mdash; the most serious "
         "grade of monastic offense, permanently disqualifying the "
         "offender from the monastic life."),
        ("anupasampanna",
         "&ldquo;not fully ordained&rdquo; &mdash; someone present "
         "without the standing to take part in the Saṅgha's formal "
         "acts."),
        ("sikkhaṁ paccakkhātaka",
         "&ldquo;one who has resigned the training&rdquo; &mdash; "
         "someone who has formally disavowed monastic life."),
        ("paṇḍaka",
         "&ldquo;eunuch&rdquo; &mdash; the fourth of the five "
         "conditions named, whose presence, confirmed or disputed, "
         "suspends the recitation."),
        ("bhikkhunidūsaka",
         "&ldquo;a rapist of nuns&rdquo; &mdash; the fifth and final "
         "taint named, whose presence likewise voids the recitation."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten grounds. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Ten grounds to suspend recitation"),
        ("p", "&sect;1", "an10.32:1.1-1.5"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How many training rules exist",
             "How many grounds there are to suspend the recitation of "
             "the monastic code",
             "How long a novice must train",
             "What defines schism in the Saṅgha"],
         "correct": 1,
         "expl": "A practical follow-up question about when the "
                 "recitation cannot proceed."},
        {"q": "How is the ten-item list actually structured?",
         "opts": [
             "Ten fully independent conditions",
             "Five conditions, each named twice &mdash; once settled, "
             "once still under discussion",
             "A single condition repeated ten times",
             "Ten conditions in strict order of severity"],
         "correct": 1,
         "expl": "Five taints, doubled into settled and unsettled "
                 "versions."},
        {"q": "Which of these is one of the five conditions named?",
         "opts": [
             "Someone who has committed an expulsion offense is "
             "sitting in the assembly",
             "Someone who has broken a minor rule is sitting in the "
             "assembly",
             "Someone from another monastery is visiting",
             "The weather is unfavorable"],
         "correct": 0,
         "expl": "One of the five taints; minor rule-breaking and "
                 "weather are not among them."},
        {"q": "According to the guide, why does even an unsettled "
              "discussion halt the recitation?",
         "opts": [
             "It doesn't; only confirmed cases matter",
             "The recitation is a shared act of the whole assembly, "
             "and an unresolved doubt is treated as compromising it "
             "just as much as a confirmed taint",
             "Unsettled discussions are simply against the rules",
             "The text gives no reason"],
         "correct": 1,
         "expl": "Either the settled or the unsettled version of a "
                 "taint is enough to stop the recitation."},
        {"q": "How does this discourse relate to AN 10.31?",
         "opts": [
             "It is unrelated, opening a new topic entirely",
             "It reads as a second question in the same conversation, "
             "with no new narrative frame introduced",
             "It contradicts AN 10.31's answer",
             "It is a verbatim repeat of AN 10.31"],
         "correct": 1,
         "expl": "Upāli continues questioning the Buddha without a "
                 "fresh narrative setup."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "As with AN 10.31, no location is given."},
    ],
    marginalia=[
        ("Five taints, doubled", [
            "confirmed, or still disputed &mdash;",
            "either halts the rite,",
            "five conditions, twice",
        ]),
        ("A shared act, undone", [
            "one tainted presence",
            "voids the whole assembly's",
            "fortnightly recital",
        ]),
        ("Upāli continues", [
            "no new scene opens &mdash;",
            "the same questioner presses on",
            "from why to when not",
        ]),
        ("Cross-references", [
            "AN 10.31 &middot; previous, the ten reasons rules exist "
            "at all",
            "AN 10.33 &middot; next, ten qualities of a judge",
        ]),
    ],
    further=[
        '<a href="%s/an10.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.31.html">AN 10.31 &middot; With Upāli</a> &mdash; previous, the ten '
        "reasons rules exist at all.",
        '<a href="an-10.33.html">AN 10.33 &middot; A Judge</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.33 — Ubbāhikāsutta
# --------------------------------------------------------------------------- #
page(
    33, "Ubbāhikā", "A Judge",
    vagga=VAGGA_4,
    meta_title="AN 10.33 — A Judge | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ubbāhikāsutta, listing the ten qualities that qualify a "
        "mendicant to be deemed a judge in a Saṅgha dispute &mdash; "
        "including a four-part knowledge of disputes echoing the "
        "structure of the four noble truths. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-item answer"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "denser technical vocabulary than AN 10.31 or "
                       "10.32"),
    ],
    why=(
        "Upāli asks what qualifies a mendicant to serve as a judge "
        "&mdash; specifically, to sit on an <em>ubbāhikā</em>, a "
        "special committee convened to settle a disciplinary dispute "
        "outside the full assembly. The answer builds from basic "
        "conduct and learning up to a four-part knowledge of disputes "
        "that mirrors, in miniature, the structure of the four noble "
        "truths."),
    guide=[
        ("The teaching in one sentence", [
            "A judge needs ten qualities: ethical conduct restrained "
            "by the code, deep learning in the teaching, mastery of "
            "both monastic codes, firmness in training, skill at "
            "persuading opposing parties, skill at raising and "
            "settling disciplinary issues, and a four-part knowledge "
            "of what a dispute is, how it arises, how it ceases, and "
            "the way leading to its cessation."]),
        ("A recurring core, opening a new pattern", [
            "The first three qualities &mdash; ethical restraint, "
            "deep learning, and mastery of both monastic codes "
            "&mdash; will recur unchanged as the opening three "
            "qualities of AN 10.34, 10.35, and 10.36, each asking "
            "about a different kind of monastic authorization. AN "
            "10.33 is the first of that set, and the only one whose "
            "remaining seven qualities concern arbitration rather "
            "than pastoral care."]),
        ("A four-part echo of the four noble truths", [
            "The final four qualities &mdash; knowing what a dispute "
            "is, how it originates, how it ceases, and the practical "
            "way to its cessation &mdash; follow exactly the same "
            "four-part logic (the fact, its origin, its cessation, "
            "the path to cessation) used elsewhere in the canon for "
            "the four noble truths themselves, here applied to the "
            "narrower, practical problem of a Saṅgha dispute."]),
        ("An institution named only here", [
            "The <em>ubbāhikā</em> &mdash; a special tribunal drawn "
            "from senior mendicants to settle a matter the full "
            "assembly could not easily resolve &mdash; is not "
            "otherwise discussed in this project; this discourse "
            "gives the qualifications for sitting on one without "
            "narrating a case."]),
    ],
    terms=[
        ("ubbāhikā",
         "a special committee or tribunal convened to settle a "
         "disciplinary dispute, drawing the mendicant qualified for it "
         "away from ordinary assembly process &mdash; this discourse's "
         "own title."),
        ("adhikaraṇa",
         "&ldquo;disciplinary issue&rdquo; or dispute &mdash; the "
         "matter a judge must know how to raise, settle, and "
         "understand at four levels."),
        ("ubhayāni pātimokkhāni",
         "&ldquo;both monastic codes&rdquo; &mdash; the rules for "
         "monks and the rules for nuns, both of which a judge must "
         "have mastered in detail."),
        ("saññāpetuṁ, paññāpetuṁ, nijjhāpetuṁ",
         "&ldquo;to persuade, advocate, and convince&rdquo; &mdash; "
         "three of the five interpersonal verbs used to describe "
         "bringing opposing parties to see the other side."),
        ("bahussuta",
         "&ldquo;very learned&rdquo; &mdash; deep familiarity with "
         "the teaching, the second of the ten qualities, and a "
         "threshold that will recur unchanged in AN 10.34&ndash;36."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten qualities of a judge. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.33:1.1-1.3"),
        ("h3", "Ten qualities"),
        ("p", "&sect;2", "an10.33:1.4-1.14"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How many qualities a mendicant needs to be deemed a "
             "judge",
             "How many grounds suspend the recitation of the code",
             "How to ordain a new mendicant",
             "What defines harmony in the Saṅgha"],
         "correct": 0,
         "expl": "The qualifications for sitting on an ubbāhikā, a "
                 "disciplinary tribunal."},
        {"q": "According to the guide, which three qualities recur "
              "unchanged in the following three discourses (AN "
              "10.34&ndash;36)?",
         "opts": [
             "The four-part knowledge of disputes",
             "Ethical restraint, deep learning, and mastery of both "
             "monastic codes",
             "Skill at persuading opposing parties",
             "Firmness in the training"],
         "correct": 1,
         "expl": "The shared opening core of this whole run of "
                 "authorization discourses."},
        {"q": "What four-part structure does the final set of "
              "qualities echo?",
         "opts": [
             "The four foundations of mindfulness",
             "The four noble truths &mdash; the fact, its origin, its "
             "cessation, and the path to cessation, applied here to a "
             "dispute",
             "The four right efforts",
             "No structure; it is a random list"],
         "correct": 1,
         "expl": "Knowing what a dispute is, its origin, its "
                 "cessation, and the way to its cessation."},
        {"q": "What is an ubbāhikā?",
         "opts": [
             "A type of monastic robe",
             "A special tribunal convened to settle a disciplinary "
             "dispute",
             "A meditation retreat",
             "A category of training rule"],
         "correct": 1,
         "expl": "This discourse's own title, naming the institution a "
                 "qualified judge would sit on."},
        {"q": "Does this discourse narrate an actual dispute being "
              "settled?",
         "opts": [
             "Yes, in full detail",
             "No &mdash; it gives only the qualifications, with no "
             "case attached",
             "Yes, but only briefly summarized",
             "The text is ambiguous on this point"],
         "correct": 1,
         "expl": "A qualifications list, not a narrated case."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "As throughout this chapter so far, no location is "
                 "given."},
    ],
    marginalia=[
        ("Ten marks of a judge", [
            "ethics, learning, both codes,",
            "firmness, and the skill",
            "to settle a dispute",
        ]),
        ("Four truths, in miniature", [
            "what it is, its rise,",
            "its ceasing, the way there &mdash;",
            "applied to one dispute",
        ]),
        ("A shared opening core", [
            "the same first three marks",
            "will open three more discourses &mdash;",
            "each asking something new",
        ]),
        ("Cross-references", [
            "AN 10.32 &middot; previous, ten grounds to suspend "
            "recitation",
            "AN 10.34 &middot; next, ten qualities to give ordination",
        ]),
    ],
    further=[
        '<a href="%s/an10.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.32.html">AN 10.32 &middot; Suspending the Recitation of the Monastic '
        'Code</a> &mdash; previous.',
        '<a href="an-10.34.html">AN 10.34 &middot; Ordination</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.34 — Upasampadāsutta
# --------------------------------------------------------------------------- #
page(
    34, "Upasampadā", "Ordination",
    vagga=VAGGA_4,
    meta_title="AN 10.34 — Ordination | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upasampadāsutta, listing the ten qualities that qualify "
        "a mendicant to serve as preceptor giving full ordination. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-item answer"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "shares its opening third with AN 10.33"),
    ],
    why=(
        "Upāli asks what qualifies a mendicant to give full "
        "ordination &mdash; that is, to serve as preceptor. The same "
        "core of ethical restraint, learning, and mastery of both "
        "codes reappears from AN 10.33, but the remaining seven "
        "qualities turn from arbitration to pastoral care: nursing "
        "the sick, easing dissatisfaction, dispelling remorse, "
        "correcting misconceptions, and guiding a student through the "
        "three higher trainings."),
    guide=[
        ("The teaching in one sentence", [
            "A preceptor needs ten qualities: ethical conduct "
            "restrained by the code, deep learning, mastery of both "
            "monastic codes, and the practical ability to care for "
            "the sick, settle dissatisfaction, dispel remorse, "
            "dissuade misconceptions, and encourage a student in the "
            "higher ethics, the higher mind, and the higher wisdom."]),
        ("Same opening, different ending", [
            "The first three qualities are word-for-word identical to "
            "AN 10.33's opening three &mdash; ethical restraint, "
            "learning, mastery of both codes &mdash; but from the "
            "fourth quality on, this discourse turns entirely away "
            "from dispute-settling toward the ongoing pastoral duties "
            "of a preceptor toward the student they ordain."]),
        ("A list that will recur twice more, unchanged", [
            "This exact seven-item pastoral tail &mdash; caring for "
            "the sick, settling dissatisfaction, dispelling remorse, "
            "dissuading misconceptions, and the three higher trainings "
            "&mdash; reappears verbatim in AN 10.35 (for giving "
            "dependence) and AN 10.36 (for having a novice attend), "
            "with only the question at the top changing."]),
        ("Three duties, three trainings", [
            "The final three items &mdash; encouraging the higher "
            "ethics, the higher mind, and the higher wisdom &mdash; "
            "name the classic threefold training (<em>sikkhā</em>) "
            "that structures the whole of monastic practice, framed "
            "here as something a preceptor must be equipped to "
            "actively teach, not merely embody."]),
    ],
    terms=[
        ("upasampadā",
         "&ldquo;full ordination&rdquo; &mdash; the formal act "
         "admitting someone to the full status of a mendicant, this "
         "discourse's own title."),
        ("upajjhāya",
         "&ldquo;preceptor&rdquo; &mdash; the senior mendicant who "
         "gives ordination and takes ongoing responsibility for the "
         "student, though the term itself is implicit rather than "
         "named in this discourse's own segments."),
        ("kukkuccaṁ vinodetuṁ",
         "&ldquo;to dispel remorse&rdquo; &mdash; one of the "
         "preceptor's pastoral duties, addressing a student's guilt "
         "or anxiety over past conduct."),
        ("adhisīla, adhicitta, adhipaññā",
         "&ldquo;the higher ethics, the higher mind, the higher "
         "wisdom&rdquo; &mdash; the classic threefold training, named "
         "here as the preceptor's final three teaching duties."),
        ("diṭṭhigataṁ dhammato vivecetuṁ",
         "&ldquo;to rationally dissuade someone from misconceptions "
         "that come up&rdquo; &mdash; another of the preceptor's seven "
         "pastoral duties."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten qualities of a preceptor. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.34:1.1-1.3"),
        ("h3", "Ten qualities"),
        ("p", "&sect;2", "an10.34:1.4-1.14"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How many qualities a mendicant needs to give ordination",
             "How many grounds suspend the recitation of the code",
             "What defines schism in the Saṅgha",
             "How to be deemed a judge"],
         "correct": 0,
         "expl": "The qualifications for serving as preceptor."},
        {"q": "How do this discourse's opening three qualities "
              "compare to AN 10.33's?",
         "opts": [
             "Completely different",
             "Word-for-word identical: ethical restraint, learning, "
             "mastery of both monastic codes",
             "Similar in theme but different in wording",
             "This discourse has no opening qualities in common with "
             "AN 10.33"],
         "correct": 1,
         "expl": "The same three-item core opens both discourses "
                 "before they diverge."},
        {"q": "From the fourth quality onward, what does this "
              "discourse turn to?",
         "opts": [
             "Skill at settling disciplinary disputes",
             "Pastoral care of a student: nursing the sick, easing "
             "dissatisfaction, dispelling remorse, and guiding the "
             "three higher trainings",
             "Cosmology and rebirth",
             "Meditation technique alone"],
         "correct": 1,
         "expl": "A preceptor's ongoing duties toward the person they "
                 "ordain."},
        {"q": "According to the guide, where does this exact "
              "seven-item pastoral list reappear?",
         "opts": [
             "Nowhere else in this project",
             "Verbatim in AN 10.35 (dependence) and AN 10.36 (a "
             "novice's attendance), with only the opening question "
             "changing",
             "Only in a summarized form later",
             "In a completely different nipāta"],
         "correct": 1,
         "expl": "The same seven duties recur twice more, unchanged, "
                 "for two other kinds of authorization."},
        {"q": "What are the final three qualities named as?",
         "opts": [
             "Three kinds of meditation",
             "The threefold training: the higher ethics, the higher "
             "mind, and the higher wisdom",
             "Three monastic robes",
             "Three grounds for suspending recitation"],
         "correct": 1,
         "expl": "The classic sikkhā triad, framed as teaching duties "
                 "here."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, as throughout this chapter."},
    ],
    marginalia=[
        ("Same root, new branch", [
            "ethics, learning, codes &mdash;",
            "then care replaces judgment:",
            "sickness, doubt, remorse",
        ]),
        ("Three trainings taught", [
            "higher ethics, mind,",
            "and wisdom &mdash; a preceptor's",
            "final duty, named",
        ]),
        ("A list about to repeat", [
            "these same seven duties",
            "return twice more, word for word &mdash;",
            "only the question shifts",
        ]),
        ("Cross-references", [
            "AN 10.33 &middot; previous, sharing this discourse's "
            "opening three qualities",
            "AN 10.35 &middot; next, the same list for giving "
            "dependence",
        ]),
    ],
    further=[
        '<a href="%s/an10.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.33.html">AN 10.33 &middot; A Judge</a> &mdash; previous.',
        '<a href="an-10.35.html">AN 10.35 &middot; Dependence</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.35 — Nissayasutta
# --------------------------------------------------------------------------- #
page(
    35, "Nissaya", "Dependence",
    vagga=VAGGA_4,
    meta_title="AN 10.35 — Dependence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Nissayasutta, repeating AN 10.34's ten qualities of a "
        "preceptor for the separate role of giving a junior mendicant "
        "ongoing dependence on a mentor. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-item answer, "
                 "identical to AN 10.34's"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "straightforward repeat, once AN 10.34 is "
                       "known"),
    ],
    why=(
        "Upāli asks a closely related but distinct question: not who "
        "may ordain, but who may take a junior mendicant into "
        "ongoing <em>nissaya</em>, dependence on a senior mentor after "
        "ordination. The Buddha's answer is the identical ten-item "
        "list from AN 10.34, with the first two items elided in the "
        "source as an explicit repeat."),
    guide=[
        ("The teaching in one sentence", [
            "The same ten qualities that qualify a mendicant to give "
            "ordination (AN 10.34) also qualify them to give "
            "dependence: ethical restraint, learning, mastery of both "
            "codes, and the sevenfold pastoral ability to care for the "
            "sick, settle dissatisfaction, dispel remorse, dissuade "
            "misconceptions, and guide the three higher trainings."]),
        ("Ordination and dependence, two distinct roles", [
            "Full ordination (<em>upasampadā</em>) and dependence "
            "(<em>nissaya</em>) are related but separate monastic "
            "institutions: the preceptor performs the ordination "
            "ceremony itself, while a mentor giving dependence takes "
            "ongoing responsibility for a junior mendicant's training "
            "&mdash; in practice, the same person often fills both "
            "roles, which is presumably why the Buddha answers with "
            "the identical list."]),
        ("The source's own elision", [
            "Rather than writing out the first two qualities again, "
            "the source text itself abbreviates them with an ellipsis "
            "&mdash; &ldquo;It's when a mendicant is ethical &hellip;&rdquo; "
            "and &ldquo;They're learned &hellip;&rdquo; &mdash; a "
            "standard convention throughout this canon for signaling "
            "an exact repeat rather than fresh content."]),
        ("Third appearance of a pattern", [
            "This is the second of what will become three consecutive "
            "discourses (AN 10.34, 10.35, 10.36) sharing this exact "
            "seven-item pastoral tail, each attached to a different "
            "question about who may take on a different kind of "
            "responsibility for a junior mendicant."]),
    ],
    terms=[
        ("nissaya",
         "&ldquo;dependence&rdquo; &mdash; the formal relationship in "
         "which a newly ordained or otherwise unestablished mendicant "
         "relies on a senior mentor, this discourse's own title."),
        ("nissayaṁ dātuṁ",
         "&ldquo;to give dependence&rdquo; &mdash; the act a "
         "qualified senior performs, taking a junior mendicant under "
         "their guidance."),
        ("pe",
         "the standard Pāli abbreviation mark (rendered here as an "
         "ellipsis in translation) indicating text repeated exactly "
         "from an earlier passage, without being written out again."),
        ("bahussuta",
         "&ldquo;very learned&rdquo; &mdash; the same threshold of "
         "learning carried over unchanged from AN 10.33 and 10.34."),
        ("gilānaṁ upaṭṭhātuṁ",
         "&ldquo;to care for the sick&rdquo; &mdash; the first of the "
         "seven pastoral duties shared identically by AN 10.34, "
         "10.35, and 10.36."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten qualities, elided at the start where identical to AN "
        "10.34. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.35:1.1-1.3"),
        ("h3", "Ten qualities, repeated from AN 10.34"),
        ("p", "&sect;2", "an10.35:1.4-1.14"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How many qualities a mendicant needs to give a junior "
             "mendicant dependence (nissaya) on a mentor",
             "How many grounds suspend the recitation of the code",
             "What defines harmony in the Saṅgha",
             "How to be deemed a judge"],
         "correct": 0,
         "expl": "A distinct but related question to AN 10.34's, "
                 "about the mentoring relationship of dependence."},
        {"q": "How does the Buddha's answer compare to AN 10.34's?",
         "opts": [
             "Completely different",
             "The identical ten-item list, with the first two items "
             "elided in the source as an explicit repeat",
             "Similar but with three items changed",
             "Shorter, with only five qualities given"],
         "correct": 1,
         "expl": "Word-for-word the same list as the preceding "
                 "discourse on ordination."},
        {"q": "According to the guide, how are ordination and "
              "dependence related as institutions?",
         "opts": [
             "They are unrelated",
             "Related but distinct: one is the ordination ceremony "
             "itself, the other is the ongoing mentoring relationship "
             "&mdash; often filled by the same person",
             "Dependence always precedes ordination",
             "Only nuns receive dependence"],
         "correct": 1,
         "expl": "Distinct roles that in practice frequently overlap "
                 "in the same senior mendicant."},
        {"q": "How does the source text itself signal the repeated "
              "opening qualities?",
         "opts": [
             "By writing them out in full again",
             "With an ellipsis, a standard convention for exact "
             "repeats from an earlier passage",
             "By omitting them entirely",
             "By summarizing them in one new sentence"],
         "correct": 1,
         "expl": "The Pāli abbreviation convention, rendered as "
                 "ellipsis in translation."},
        {"q": "What pattern does this discourse continue, according "
              "to the guide?",
         "opts": [
             "It is unrelated to any pattern",
             "The second of three consecutive discourses (AN "
             "10.34&ndash;36) sharing the same seven-item pastoral "
             "tail",
             "The first of a brand new list",
             "A pattern that ends here"],
         "correct": 1,
         "expl": "AN 10.36 will repeat the same list once more, for "
                 "a novice's attendance."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, as throughout this chapter."},
    ],
    marginalia=[
        ("The same ten, again", [
            "ordination's list",
            "returns for dependence &mdash;",
            "one role, two questions",
        ]),
        ("An ellipsis, not new text", [
            "&ldquo;ethical &hellip;&rdquo; the source",
            "abbreviates what it already",
            "said one page before",
        ]),
        ("Preceptor and mentor", [
            "ordaining, and then",
            "staying on to guide &mdash; often",
            "the very same hand",
        ]),
        ("Cross-references", [
            "AN 10.34 &middot; previous, the identical list for "
            "ordination",
            "AN 10.36 &middot; next, the same list once more, for a "
            "novice's attendance",
        ]),
    ],
    further=[
        '<a href="%s/an10.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.34.html">AN 10.34 &middot; Ordination</a> &mdash; previous, the '
        "identical list.",
        '<a href="an-10.36.html">AN 10.36 &middot; A Novice</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.36 — Sāmaṇerasutta
# --------------------------------------------------------------------------- #
page(
    36, "Sāmaṇera", "A Novice",
    vagga=VAGGA_4,
    meta_title="AN 10.36 — A Novice | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sāmaṇerasutta, repeating the same ten qualities a third "
        "time, now for who may be attended on by a novice. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-item answer, "
                 "identical to AN 10.34 and 10.35"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the third and final repeat of this list, "
                       "closing out the run"),
    ],
    why=(
        "Upāli asks a third variant of the same question: who may "
        "have a <em>sāmaṇera</em>, a novice, attend on them? The "
        "Buddha's answer is, for a third consecutive time, the "
        "identical ten qualities &mdash; completing a run of three "
        "discourses that apply one list to three distinct kinds of "
        "responsibility for a junior mendicant."),
    guide=[
        ("The teaching in one sentence", [
            "The same ten qualities that qualify a mendicant to give "
            "ordination (AN 10.34) and to give dependence (AN 10.35) "
            "also qualify them to have a novice attend on them: "
            "ethical restraint, learning, mastery of both codes, and "
            "the sevenfold pastoral ability toward a junior in their "
            "care."]),
        ("A third and final repeat", [
            "AN 10.34, 10.35, and 10.36 together form a matched set: "
            "three distinct questions about three distinct monastic "
            "relationships &mdash; ordaining, mentoring through "
            "dependence, and having a novice in attendance &mdash; "
            "all answered with the exact same ten-item list. The "
            "underlying claim is that the same qualities of character "
            "and competence underwrite every form of responsibility "
            "for someone junior."]),
        ("A novice, not yet fully ordained", [
            "A <em>sāmaṇera</em> is someone who has gone forth under "
            "the ten precepts but has not yet received full "
            "ordination (<em>upasampadā</em>); this discourse asks "
            "what qualifies a senior mendicant to have such a person "
            "attend on and be guided by them, the most junior of the "
            "three relationships covered in this three-discourse "
            "set."]),
        ("Closing this sub-sequence, not the chapter", [
            "With this discourse the three-item run on ordination, "
            "dependence, and novice attendance is complete; the "
            "chapter's next two discourses turn to an entirely "
            "different subject &mdash; the definitions of schism and "
            "harmony in the Saṅgha."]),
    ],
    terms=[
        ("sāmaṇera",
         "&ldquo;novice&rdquo; &mdash; one who has gone forth under "
         "the ten precepts but not yet received full ordination, this "
         "discourse's own title."),
        ("upaṭṭhāpetuṁ",
         "&ldquo;to be attended on&rdquo; &mdash; the specific "
         "relationship this discourse asks about, a novice serving "
         "and being guided by a qualified senior."),
        ("dasahi dhammehi samannāgato",
         "&ldquo;endowed with ten qualities&rdquo; &mdash; the "
         "recurring formula opening the Buddha's answer in AN 10.33 "
         "through 10.36 alike."),
        ("anabhiratiṁ vūpakāsetuṁ",
         "&ldquo;to settle dissatisfaction&rdquo; &mdash; the second "
         "of the seven pastoral duties, appearing identically in AN "
         "10.34, 10.35, and 10.36."),
        ("kukkuccaṁ vinodetuṁ",
         "&ldquo;to dispel remorse&rdquo; &mdash; a third of those "
         "same seven duties, again shared unchanged across all three "
         "discourses."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten qualities, elided at the start where identical to AN "
        "10.34 and 10.35. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.36:1.1-1.3"),
        ("h3", "Ten qualities, repeated a third time"),
        ("p", "&sect;2", "an10.36:1.4-1.14"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How many qualities a mendicant needs to have a novice "
             "(sāmaṇera) attend on them",
             "How many grounds suspend the recitation of the code",
             "What defines schism in the Saṅgha",
             "How to be deemed a judge"],
         "correct": 0,
         "expl": "A third variant question about responsibility for a "
                 "junior mendicant."},
        {"q": "How does the Buddha's answer compare to AN 10.34 and "
              "10.35's?",
         "opts": [
             "Completely different from both",
             "The identical ten-item list for a third consecutive "
             "time",
             "Similar to 10.34 but different from 10.35",
             "A shortened five-item version"],
         "correct": 1,
         "expl": "The same list, applied a third time to a third "
                 "relationship."},
        {"q": "According to the guide, what do AN 10.34, 10.35, and "
              "10.36 together claim?",
         "opts": [
             "That three unrelated lists happen to share a title",
             "That the same qualities of character and competence "
             "underwrite every form of responsibility for someone "
             "junior &mdash; ordaining, mentoring, or having a novice "
             "attend",
             "That novices are held to a lower standard",
             "That only the third list is authoritative"],
         "correct": 1,
         "expl": "One underlying claim illustrated three times over."},
        {"q": "What is a sāmaṇera?",
         "opts": [
             "A fully ordained senior mendicant",
             "One who has gone forth under the ten precepts but not "
             "yet received full ordination",
             "A lay donor",
             "A special judge"],
         "correct": 1,
         "expl": "A novice, the most junior of the three relationships "
                 "covered across AN 10.34&ndash;36."},
        {"q": "What happens after this discourse, according to the "
              "guide?",
         "opts": [
             "The chapter ends",
             "The three-discourse run on ordination, dependence, and "
             "novice attendance is complete, and the chapter turns to "
             "the definitions of schism and harmony",
             "The same list repeats a fourth time",
             "Upāli stops questioning the Buddha"],
         "correct": 1,
         "expl": "AN 10.37 opens an entirely different subject within "
                 "the same chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, as throughout this chapter."},
    ],
    marginalia=[
        ("Third time, same ten", [
            "ordain, mentor, or",
            "take on a novice &mdash; one list",
            "answers all of them",
        ]),
        ("The most junior bond", [
            "not yet full ordained,",
            "a novice attends a senior &mdash;",
            "same ten marks required",
        ]),
        ("A run now complete", [
            "three discourses, one",
            "list &mdash; the chapter turns next",
            "to schism and peace",
        ]),
        ("Cross-references", [
            "AN 10.35 &middot; previous, the same list for giving "
            "dependence",
            "AN 10.34 &middot; the first of this three-discourse run, "
            "on ordination",
            "AN 10.37 &middot; next, defining schism in the Saṅgha",
        ]),
    ],
    further=[
        '<a href="%s/an10.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.35.html">AN 10.35 &middot; Dependence</a> &mdash; previous.',
        '<a href="an-10.37.html">AN 10.37 &middot; Schism in the Saṅgha</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.37 — Saṅghabhedasutta
# --------------------------------------------------------------------------- #
page(
    37, "Saṅghabheda", "Schism in the Saṅgha",
    vagga=VAGGA_4,
    meta_title="AN 10.37 — Schism in the Saṅgha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Saṅghabhedasutta, the canonical ten-ground definition of "
        "what constitutes schism in the Saṅgha. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-ground definition "
                 "in five mirrored pairs"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "repetitive by design, five paired categories"),
    ],
    why=(
        "Upāli asks for the technical definition of schism in the "
        "Saṅgha &mdash; one of the gravest acts named anywhere in the "
        "canon. The Buddha's answer is precise and structural: "
        "misrepresenting the teaching, the training, and the "
        "Realized One's own words, practice, and prescriptions, each "
        "in both directions, across five categories that combine into "
        "ten grounds."),
    guide=[
        ("The teaching in one sentence", [
            "Schism in the Saṅgha is defined as a mendicant "
            "misrepresenting five things &mdash; the teaching, the "
            "training, what the Realized One said, what he practiced, "
            "and what he prescribed &mdash; explaining each as its "
            "opposite, then splitting off to perform legal acts and "
            "recite the monastic code independently."]),
        ("Five categories, doubled into ten", [
            "As with AN 10.32's grounds for suspending recitation, "
            "the list is not ten unrelated items but five paired "
            "reversals: for each of five categories, the schismatic "
            "explains what is not the case as if it were, and what is "
            "the case as if it were not &mdash; ten grounds from five "
            "underlying distortions."]),
        ("A definition, not a narrative", [
            "This discourse gives the abstract legal definition of "
            "schism without naming any individual or incident; the "
            "canon elsewhere associates schism with the specific "
            "figure of Devadatta, but nothing here names him or "
            "narrates an actual case &mdash; this is the criterion "
            "itself, stated in the driest possible terms."]),
        ("Gravity to be revealed two discourses later", [
            "Nothing in this discourse states what schism actually "
            "costs the one who causes it; that consequence &mdash; an "
            "eon in hell &mdash; is withheld until AN 10.39, where "
            "Ānanda asks the follow-up question this discourse leaves "
            "open."]),
    ],
    terms=[
        ("saṅghabheda",
         "&ldquo;schism in the Saṅgha&rdquo; &mdash; a formal, "
         "legally defined split, this discourse's own title, and "
         "counted elsewhere in the canon among the gravest possible "
         "acts."),
        ("adhammaṁ dhammoti dīpeti",
         "&ldquo;explains what is not the teaching as the "
         "teaching&rdquo; &mdash; the first of the five reversals "
         "defining schism."),
        ("āveni kammāni karonti, āveni pātimokkhaṁ uddisanti",
         "&ldquo;they perform legal acts autonomously and recite the "
         "monastic code autonomously&rdquo; &mdash; the concrete, "
         "institutional act that follows from the ten grounds: "
         "operating as a separate Saṅgha."),
        ("avinayaṁ vinayoti dīpeti",
         "&ldquo;explains what is not the training as the "
         "training&rdquo; &mdash; the second of the five reversals "
         "defining schism."),
        ("bhinno",
         "&ldquo;split&rdquo; &mdash; the state Upāli asks about at "
         "the outset: at what point is the Saṅgha considered split?"),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "definition of schism. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.37:1.1-1.2"),
        ("h3", "Ten grounds defining schism"),
        ("p", "&sect;2", "an10.37:1.3-1.5"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How schism in the Saṅgha is defined",
             "How many qualities a mendicant needs to give ordination",
             "How to be deemed a judge",
             "How many grounds suspend the recitation of the code"],
         "correct": 0,
         "expl": "The technical definition of one of the canon's "
                 "gravest acts."},
        {"q": "How is the ten-ground definition actually structured?",
         "opts": [
             "Ten fully independent grounds",
             "Five categories, each doubled into a mirrored reversal "
             "&mdash; ten grounds from five underlying distortions",
             "A single ground repeated ten times",
             "Ten unrelated historical incidents"],
         "correct": 1,
         "expl": "Five paired reversals, the same structural device "
                 "as AN 10.32's grounds for suspending recitation."},
        {"q": "Which of these is one of the five categories "
              "misrepresented?",
         "opts": [
             "The teaching (dhamma) versus not the teaching",
             "The weather",
             "A donor's wealth",
             "The color of robes"],
         "correct": 0,
         "expl": "One of five categories: the teaching, the training, "
                 "and what the Realized One said, practiced, and "
                 "prescribed."},
        {"q": "According to the guide, does this discourse name "
              "Devadatta or narrate an actual case of schism?",
         "opts": [
             "Yes, in full narrative detail",
             "No &mdash; it gives only the abstract legal definition, "
             "with no individual named or incident narrated",
             "It names Devadatta but no incident",
             "It narrates an incident without naming anyone"],
         "correct": 1,
         "expl": "A dry, structural definition, not a narrative."},
        {"q": "According to the guide, where is the consequence of "
              "causing schism revealed?",
         "opts": [
             "Nowhere in this project",
             "Not in this discourse &mdash; it is withheld until AN "
             "10.39, where Ānanda asks the follow-up question",
             "Earlier, in AN 10.31",
             "In this discourse's own final line"],
         "correct": 1,
         "expl": "This discourse defines schism; AN 10.39 reveals its "
                 "cost."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, as throughout this chapter."},
    ],
    marginalia=[
        ("Five distortions, doubled", [
            "teaching, training, and",
            "the Realized One's own words &mdash;",
            "each reversed in turn",
        ]),
        ("A definition, not a story", [
            "no name is spoken here,",
            "no incident narrated &mdash;",
            "only the criterion",
        ]),
        ("A cost withheld", [
            "what schism actually",
            "costs is not yet said &mdash; two",
            "discourses from now",
        ]),
        ("Cross-references", [
            "AN 10.36 &middot; previous, closing the ordination-"
            "dependence-novice run",
            "AN 10.38 &middot; next, the mirrored definition of "
            "harmony",
            "AN 10.39 &middot; where the karmic cost of schism is "
            "finally named",
        ]),
    ],
    further=[
        '<a href="%s/an10.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.36.html">AN 10.36 &middot; A Novice</a> &mdash; previous.',
        '<a href="an-10.38.html">AN 10.38 &middot; Harmony in the Saṅgha</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.38 — Saṅghasāmaggīsutta
# --------------------------------------------------------------------------- #
page(
    38, "Saṅghasāmaggī", "Harmony in the Saṅgha",
    vagga=VAGGA_4,
    meta_title="AN 10.38 — Harmony in the Saṅgha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Saṅghasāmaggīsutta, the exact positive mirror of AN "
        "10.37's definition of schism, defining harmony in the "
        "Saṅgha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-ground definition, "
                 "the exact mirror of AN 10.37's"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "straightforward positive mirror of the "
                       "preceding discourse"),
    ],
    why=(
        "Immediately after defining schism, Upāli asks for its exact "
        "opposite: what counts as harmony in the Saṅgha? The Buddha's "
        "answer takes the same five categories from AN 10.37 and "
        "flips every reversal back the right way round &mdash; "
        "explaining what is not the teaching as not the teaching, and "
        "so on, so that no split occurs."),
    guide=[
        ("The teaching in one sentence", [
            "Harmony in the Saṅgha is defined as a mendicant "
            "correctly representing the same five things schism "
            "distorts &mdash; the teaching, the training, and what "
            "the Realized One said, practiced, and prescribed "
            "&mdash; so that no split occurs and legal acts and the "
            "monastic code continue to be performed together."]),
        ("An exact mirror, category by category", [
            "This discourse does not introduce new material: it takes "
            "AN 10.37's five categories one by one and simply "
            "corrects each reversal &mdash; where schism explained the "
            "teaching as not-the-teaching, harmony explains the "
            "teaching as the teaching. The structure is identical; "
            "only the direction of each item is flipped."]),
        ("A pairing typical of this project", [
            "Positive-negative discourse pairs sharing an identical "
            "underlying structure have appeared repeatedly throughout "
            "this project's earlier nipātas; this pair is among the "
            "starkest examples, since the two discourses' ten grounds "
            "correspond one-to-one with nothing added or removed on "
            "either side."]),
        ("Still no reward named, yet", [
            "Just as AN 10.37 withheld the cost of causing schism, "
            "this discourse withholds the reward of preserving harmony "
            "&mdash; both are named only in the discourses that "
            "follow, AN 10.39 and 10.40, where Ānanda asks the "
            "question this pair leaves open."]),
    ],
    terms=[
        ("saṅghasāmaggī",
         "&ldquo;harmony in the Saṅgha&rdquo; &mdash; this "
         "discourse's own title, the direct positive counterpart to "
         "saṅghabheda."),
        ("adhammaṁ adhammoti dīpeti",
         "&ldquo;explains what is not the teaching as not the "
         "teaching&rdquo; &mdash; the corrected, harmonious version of "
         "AN 10.37's first reversal."),
        ("na āveni kammāni karonti, na āveni pātimokkhaṁ uddisanti",
         "&ldquo;they don't perform legal acts autonomously or recite "
         "the monastic code autonomously&rdquo; &mdash; the concrete "
         "outcome of harmony: one Saṅgha, acting as one."),
        ("dhammaṁ dhammoti dīpeti",
         "&ldquo;explains the teaching as the teaching&rdquo; &mdash; "
         "the corrected, harmonious version of the first reversal, "
         "reading straightforwardly rather than against itself."),
        ("samaggo",
         "&ldquo;united, harmonious&rdquo; &mdash; the state of the "
         "Saṅgha this discourse defines and protects, the direct "
         "opposite of <em>bhinno</em>, split."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "definition of harmony. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.38:1.1-1.2"),
        ("h3", "Ten grounds defining harmony"),
        ("p", "&sect;2", "an10.38:1.3-1.5"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How harmony in the Saṅgha is defined",
             "How many qualities a mendicant needs to give ordination",
             "How to be deemed a judge",
             "How many grounds suspend the recitation of the code"],
         "correct": 0,
         "expl": "The exact positive counterpart to AN 10.37's "
                 "definition of schism."},
        {"q": "How does this discourse's structure compare to AN "
              "10.37's?",
         "opts": [
             "Completely unrelated content",
             "An exact mirror: the same five categories, with every "
             "reversal corrected back the right way round",
             "A shortened version with only five grounds",
             "A narrative account replacing the earlier definition"],
         "correct": 1,
         "expl": "Category-by-category, the same structure with the "
                 "direction of each item flipped."},
        {"q": "What is the concrete outcome of harmony described as?",
         "opts": [
             "Mendicants living in separate monasteries",
             "One Saṅgha performing legal acts and reciting the "
             "monastic code together, without splitting",
             "A vote among senior mendicants",
             "No concrete outcome is given"],
         "correct": 1,
         "expl": "The institutional opposite of schism's separate, "
                 "autonomous acts."},
        {"q": "According to the guide, what does this discourse "
              "still withhold?",
         "opts": [
             "Nothing; it states everything in full",
             "The reward of preserving harmony, named only in AN "
             "10.40",
             "The definition of harmony itself",
             "The names of the five categories"],
         "correct": 1,
         "expl": "Just as AN 10.37 withheld schism's cost, this "
                 "discourse withholds harmony's reward."},
        {"q": "According to the guide, how does this pair compare to "
              "other positive-negative pairs in this project?",
         "opts": [
             "It is the only such pair in the entire project",
             "It is among the starkest examples, with the ten grounds "
             "corresponding one-to-one and nothing added or removed",
             "It is a looser, less exact pairing than most others",
             "The two discourses do not actually correspond"],
         "correct": 1,
         "expl": "A very tight structural mirror, typical of this "
                 "project's recurring pairing pattern but unusually "
                 "exact here."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, as throughout this chapter."},
    ],
    marginalia=[
        ("Every reversal, corrected", [
            "teaching as teaching,",
            "training as training &mdash; five",
            "categories, righted",
        ]),
        ("One Saṅgha, one act", [
            "no separate rite,",
            "no autonomous recital &mdash;",
            "harmony's own mark",
        ]),
        ("A reward still withheld", [
            "what harmony earns",
            "waits two discourses more &mdash;",
            "Ānanda will ask",
        ]),
        ("Cross-references", [
            "AN 10.37 &middot; previous, the exact mirror image, "
            "defining schism",
            "AN 10.40 &middot; where the reward for harmony is finally "
            "named",
        ]),
    ],
    further=[
        '<a href="%s/an10.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.37.html">AN 10.37 &middot; Schism in the Saṅgha</a> &mdash; previous.',
        '<a href="an-10.39.html">AN 10.39 &middot; With Ānanda (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.39 — Paṭhamaānandasutta
# --------------------------------------------------------------------------- #
page(
    39, "Paṭhamaānanda", "With Ānanda (1st)",
    vagga=VAGGA_4,
    meta_title="AN 10.39 — With Ānanda (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamaānandasutta, in which Ānanda asks the Buddha to "
        "define schism again and learns its karmic cost &mdash; an "
        "eon in hell &mdash; closed with a four-line verse. From Ru-"
        "Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda questioning the Buddha"),
        ("Form", "A narrative opening, a repeated (elided) "
                 "definition, a follow-up question and answer, and a "
                 "closing verse"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "straightforward, but weighty in content"),
    ],
    why=(
        "For the first time in this chapter, a different questioner "
        "steps forward: Ānanda goes to the Buddha and asks the same "
        "question Upāli asked in AN 10.37 &mdash; what defines schism "
        "&mdash; but this time presses further, asking what the one "
        "who causes it actually reaps. The answer is stark: an eon in "
        "hell, sealed with a four-line verse."),
    guide=[
        ("The teaching in one sentence", [
            "A schismatic is defined exactly as in AN 10.37, but here "
            "the Buddha adds the consequence: whoever splits a "
            "harmonious Saṅgha brims with sin lasting an eon and burns "
            "in hell for that eon, a verdict sealed with a closing "
            "verse."]),
        ("A new narrative frame, a new questioner", [
            "Unlike AN 10.32&ndash;38, which read as one continuous "
            "conversation with Upāli, this discourse opens with its "
            "own narrative: &ldquo;Then Venerable Ānanda went up to "
            "the Buddha, bowed, sat down to one side&rdquo; &mdash; "
            "the same formal opening used for AN 10.31, signaling a "
            "fresh scene rather than a continued exchange."]),
        ("The same definition, elided", [
            "Rather than restating the ten grounds in full, the "
            "source elides most of the definition with an ellipsis, "
            "trusting the reader to recall AN 10.37's exact wording "
            "&mdash; a repeat acknowledged rather than reproduced."]),
        ("A cost finally named, in verse", [
            "This is the first point in the chapter where a karmic "
            "consequence is stated outright, and the first appearance "
            "of a closing verse anywhere in this chapter: the four "
            "lines drive home in poetic form what the preceding "
            "prose already said in legal form &mdash; a schismatic "
            "burns in hell for an eon."]),
    ],
    terms=[
        ("kappaṭṭhikaṁ kibbisaṁ",
         "&ldquo;sin that lasts for an eon&rdquo; &mdash; the specific "
         "phrase naming the weight of the offense, distinct from an "
         "ordinary bad outcome."),
        ("kappaṁ nirayamhi paccati",
         "&ldquo;they burn in hell for an eon&rdquo; &mdash; the "
         "literal consequence, repeated in both prose and the closing "
         "verse."),
        ("saṅghaṁ samaggaṁ bhinditvā",
         "&ldquo;after causing schism in a harmonious Saṅgha&rdquo; "
         "&mdash; the closing verse's own summary of the offense."),
        ("āpāyiko nerayiko",
         "&ldquo;a schismatic remains&hellip; in a place of loss, in "
         "hell&rdquo; &mdash; the verse's opening image, naming the "
         "destination before naming the cause."),
        ("yogakkhemā padhaṁsati",
         "&ldquo;they ruin their sanctuary&rdquo; &mdash; the verse's "
         "own image for what a schismatic destroys, echoed and "
         "inverted in AN 10.40's closing verse."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's questions, the Buddha's "
        "answers, and the closing verse. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda's question, and the definition repeated"),
        ("p", "&sect;1", "an10.39:1.1-1.7"),
        ("h3", "The cost of schism"),
        ("p", "&sect;2", "an10.39:2.1-2.4"),
        ("h3", "Closing verse"),
        ("p", "&sect;3", "an10.39:3.1-3.6"),
    ],
    quiz=[
        {"q": "Who questions the Buddha in this discourse?",
         "opts": [
             "Venerable Upāli, continuing from AN 10.38",
             "Venerable Ānanda, in a freshly opened narrative scene",
             "King Pasenadi of Kosala",
             "A group of unnamed mendicants"],
         "correct": 1,
         "expl": "A new questioner and a new narrative opening, "
                 "unlike the continuous Upāli exchange running through "
                 "AN 10.32&ndash;38."},
        {"q": "How does this discourse handle repeating the "
              "definition of schism from AN 10.37?",
         "opts": [
             "It restates all ten grounds in full again",
             "It elides most of the definition with an ellipsis, "
             "trusting the reader to recall AN 10.37's wording",
             "It gives a completely different definition",
             "It omits the definition entirely"],
         "correct": 1,
         "expl": "A repeat acknowledged, not reproduced word for "
                 "word."},
        {"q": "What new information does this discourse add beyond "
              "AN 10.37's definition?",
         "opts": [
             "Nothing new is added",
             "The karmic cost: whoever causes schism brims with sin "
             "lasting an eon and burns in hell for that eon",
             "A list of famous schismatics",
             "A method for preventing schism"],
         "correct": 1,
         "expl": "Ānanda's follow-up question draws out the "
                 "consequence AN 10.37 left unstated."},
        {"q": "What closes this discourse?",
         "opts": [
             "Nothing; it ends with the prose answer",
             "A four-line verse restating the consequence in poetic "
             "form",
             "A list of ten more grounds",
             "A question left unanswered"],
         "correct": 1,
         "expl": "The first closing verse to appear in this chapter."},
        {"q": "According to the guide, what signals that this is a "
              "fresh scene rather than a continuation of the Upāli "
              "conversation?",
         "opts": [
             "Nothing signals this; it is ambiguous",
             "The same formal narrative opening used for AN 10.31: "
             "Ānanda approaching, bowing, and sitting down",
             "A change of location being stated",
             "The Buddha addressing a different audience"],
         "correct": 1,
         "expl": "A fresh narrative frame, matching AN 10.31's own "
                 "opening formula."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, matching the rest of this "
                 "chapter despite the fresh narrative opening."},
    ],
    marginalia=[
        ("A new voice asks", [
            "not Upāli now, but",
            "Ānanda approaches &mdash;",
            "the same old question",
        ]),
        ("The cost, finally named", [
            "sin that lasts an eon,",
            "hellfire for that same eon &mdash;",
            "what AN 10.37 withheld",
        ]),
        ("Prose, then verse", [
            "the legal answer,",
            "then four lines drive it home &mdash;",
            "this chapter's first verse",
        ]),
        ("Cross-references", [
            "AN 10.37 &middot; the definition this discourse repeats "
            "and completes",
            "AN 10.38 &middot; previous, the mirrored definition of "
            "harmony",
            "AN 10.40 &middot; next, the same pattern for harmony's "
            "reward",
        ]),
    ],
    further=[
        '<a href="%s/an10.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.38.html">AN 10.38 &middot; Harmony in the Saṅgha</a> &mdash; previous.',
        '<a href="an-10.37.html">AN 10.37 &middot; Schism in the Saṅgha</a> &mdash; the '
        "definition repeated here.",
        '<a href="an-10.40.html">AN 10.40 &middot; With Ānanda (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.40 — Dutiyaānandasutta
# --------------------------------------------------------------------------- #
page(
    40, "Dutiyaānanda", "With Ānanda (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 10.40 — With Ānanda (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaānandasutta, closing the Upālivagga with harmony's "
        "reward &mdash; an eon in heaven &mdash; and the chapter's own "
        "untranslated closing colophon and uddāna verse. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda questioning the Buddha, "
                     "continuing directly from AN 10.39"),
        ("Form", "A repeated (elided) definition, a follow-up "
                 "question and answer, and a closing verse"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "the exact positive mirror of AN 10.39"),
    ],
    why=(
        "Ānanda asks the same follow-up question as AN 10.39, now "
        "about harmony rather than schism: what does someone who "
        "forges harmony in a divided Saṅgha reap? The answer completes "
        "the chapter's final mirrored pair &mdash; an eon rejoicing in "
        "heaven &mdash; and closes the Upālivagga with its own "
        "untranslated colophon and uddāna verse naming all ten "
        "discourses."),
    guide=[
        ("The teaching in one sentence", [
            "Harmony is defined exactly as in AN 10.38, and the "
            "Buddha adds its reward: whoever forges harmony in a "
            "divided Saṅgha brims with divine merit and rejoices in "
            "heaven for an eon, sealed with a four-line verse mirroring "
            "AN 10.39's."]),
        ("The chapter's final mirrored pair", [
            "AN 10.39 and 10.40 complete the same positive-negative "
            "pairing already seen between AN 10.37 and 10.38, now "
            "carried one step further into consequence: sin for an "
            "eon versus merit for an eon, hell for an eon versus "
            "heaven for an eon, verse for verse."]),
        ("A verse answering a verse", [
            "This discourse's closing verse mirrors AN 10.39's line "
            "by line &mdash; where that verse named a schismatic "
            "&ldquo;taking a stand against the teaching, favoring "
            "factions,&rdquo; this one names the harmonizer &ldquo;"
            "taking a stand on the teaching, favoring harmony&rdquo; "
            "&mdash; the same structure, inverted in substance."]),
        ("Closing the chapter, and naming all ten discourses", [
            "The source's own colophon, left untranslated in the "
            "English text, marks this both as the tenth discourse and "
            "as the close of <em>Upālivaggo catuttho</em>, the fourth "
            "chapter, followed by an uddāna verse listing all ten "
            "discourse names in brief &mdash; the same closing device "
            "seen at the end of chapters 1 through 3."]),
    ],
    terms=[
        ("brahmaṁ puññaṁ",
         "&ldquo;divine merit&rdquo; &mdash; the positive counterpart "
         "to the &ldquo;sin lasting an eon&rdquo; named in AN 10.39, "
         "the reward for forging harmony."),
        ("kappaṁ sagge pamodati",
         "&ldquo;they rejoice in heaven for an eon&rdquo; &mdash; the "
         "literal reward, mirroring AN 10.39's &ldquo;they burn in "
         "hell for an eon.&rdquo;"),
        ("sukhā saṅghassa sāmaggī",
         "&ldquo;a Saṅgha in harmony is happy&rdquo; &mdash; the "
         "verse's opening line, naming the state before naming the "
         "cause, mirroring AN 10.39's opening image of loss."),
        ("Upālivaggo catuttho",
         "&ldquo;the Upāli Chapter, the fourth&rdquo; &mdash; the "
         "chapter's own closing colophon, left untranslated in the "
         "English text."),
        ("uddāna",
         "a summary verse naming, in brief, all the discourses just "
         "covered &mdash; here closing the chapter, left untranslated "
         "in the English text as in previous chapters."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's questions, the Buddha's "
        "answers, and the closing verse. The chapter's own colophon "
        "and uddāna verse, in Pāli only, are described but not "
        "reproduced, following this project's convention for "
        "untranslated closing material. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda's question, and the definition repeated"),
        ("p", "&sect;1", "an10.40:1.1-1.5"),
        ("h3", "The reward of harmony"),
        ("p", "&sect;2", "an10.40:2.1-2.4"),
        ("h3", "Closing verse"),
        ("p", "&sect;3", "an10.40:3.1-3.6"),
    ],
    quiz=[
        {"q": "What does Ānanda ask about in this discourse?",
         "opts": [
             "What defines schism in the Saṅgha",
             "What someone who forges harmony in a divided Saṅgha "
             "reaps",
             "How many qualities a judge needs",
             "How to suspend the recitation of the monastic code"],
         "correct": 1,
         "expl": "The positive counterpart to AN 10.39's question "
                 "about schism's cost."},
        {"q": "What is the reward for forging harmony, according to "
              "this discourse?",
         "opts": [
             "Nothing in particular",
             "Brimming with divine merit and rejoicing in heaven for "
             "an eon",
             "Immediate liberation",
             "Rebirth as a deva king"],
         "correct": 1,
         "expl": "The exact positive mirror of AN 10.39's eon in "
                 "hell."},
        {"q": "How does this discourse's closing verse relate to AN "
              "10.39's?",
         "opts": [
             "It is unrelated",
             "It mirrors AN 10.39's verse line by line, inverting "
             "each image from schism to harmony",
             "It repeats AN 10.39's verse word for word, unchanged",
             "It replaces the verse with prose"],
         "correct": 1,
         "expl": "The same structure, with every image flipped from "
                 "division to unity."},
        {"q": "What does the chapter's own closing colophon mark, "
              "according to the guide?",
         "opts": [
             "Nothing; there is no colophon",
             "That this is the tenth discourse and the close of "
             "Upālivaggo catuttho, the fourth chapter, followed by an "
             "uddāna verse naming all ten discourses",
             "The opening of a fifth chapter",
             "A scribal error"],
         "correct": 1,
         "expl": "The same untranslated closing device used at the "
                 "end of chapters 1 through 3."},
        {"q": "How does this discourse connect to AN 10.37 and "
              "10.38?",
         "opts": [
             "It is unrelated to that earlier pair",
             "Together with AN 10.39, it extends that earlier "
             "schism/harmony pairing one step further, into the "
             "karmic consequence of each",
             "It contradicts AN 10.38's definition",
             "It replaces AN 10.37's definition with a new one"],
         "correct": 1,
         "expl": "Definition (10.37/10.38), then consequence "
                 "(10.39/10.40) &mdash; the same mirrored logic carried "
                 "one step further."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, matching the rest of this "
                 "chapter."},
    ],
    marginalia=[
        ("Merit for an eon", [
            "not hellfire this time,",
            "but heaven's own rejoicing &mdash;",
            "harmony's reward",
        ]),
        ("A verse mirrored", [
            "&ldquo;favoring factions&rdquo;",
            "becomes &ldquo;favoring harmony&rdquo; &mdash;",
            "one line, inverted",
        ]),
        ("The chapter closes", [
            "ten discourses named",
            "in a verse left untranslated &mdash;",
            "Upāli's own chapter",
        ]),
        ("Cross-references", [
            "AN 10.39 &middot; previous, schism's cost, mirrored here "
            "by harmony's reward",
            "AN 10.38 &middot; the definition of harmony this "
            "discourse builds on",
            "AN 10.31 &middot; opening this chapter, on why training "
            "rules exist at all",
        ]),
    ],
    further=[
        '<a href="%s/an10.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.39.html">AN 10.39 &middot; With Ānanda (1st)</a> &mdash; previous.',
        '<a href="an-10.31.html">AN 10.31 &middot; With Upāli</a> &mdash; opening this '
        "chapter.",
    ],
)


VAGGA_5 = "<em>Akkosavagga</em> &mdash; the fifth chapter of the Tens, closing the First Fifty"


# --------------------------------------------------------------------------- #
# AN 10.41 — Vivādasutta
# --------------------------------------------------------------------------- #
page(
    41, "Vivāda", "Dispute",
    vagga=VAGGA_5,
    meta_title="AN 10.41 — Dispute | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Vivādasutta, opening the Tens' fifth chapter with Upāli "
        "asking the root cause of every fight and quarrel in the "
        "Saṅgha &mdash; answered with the same five reversals that "
        "defined schism in AN 10.37. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha"),
        ("Form", "A single question, a single ten-ground answer"),
        ("Length", "~1 minute to read"),
        ("Chapter's namesake, or not", "This chapter is titled "
                                       "<em>Akkosavagga</em>, the "
                                       "Chapter on Abuse, but "
                                       "&ldquo;akkosa&rdquo; appears "
                                       "nowhere in any of its ten "
                                       "discourses' actual content "
                                       "&mdash; an unexplained "
                                       "mismatch this guide notes "
                                       "rather than resolves"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "familiar ground for anyone who has read AN "
                       "10.37"),
    ],
    why=(
        "Upāli asks the most practical possible question about "
        "conflict in the Saṅgha: what actually causes it? The "
        "Buddha's answer is, word for word, the same five reversals "
        "&mdash; misrepresenting the teaching, the training, and the "
        "Realized One's words, practice, and prescriptions &mdash; "
        "already met defining schism in AN 10.37."),
    guide=[
        ("The teaching in one sentence", [
            "Fights, quarrels, arguments, and disputes in the Saṅgha "
            "trace back to a mendicant explaining the same five "
            "things wrongly: the teaching, the training, and what the "
            "Realized One said, practiced, and prescribed, each "
            "explained as its opposite."]),
        ("The same list, a third time, reframed", [
            "This is not a new list: it is AN 10.37's ten grounds for "
            "schism, transplanted into a new question. Where AN 10.37 "
            "asked what counts as schism, this discourse asks what "
            "causes ordinary discord short of a full split &mdash; "
            "the same distortion, read at a smaller scale."]),
        ("A puzzling chapter title", [
            "Unusually for this nipāta, the chapter this discourse "
            "opens is named for a word that does not occur in it: "
            "<em>Akkosavagga</em>, the Chapter on Abuse. None of the "
            "ten discourses that follow is actually about abuse or "
            "reviling, by title or by content; the source gives no "
            "explanation, and this guide records the mismatch rather "
            "than inventing one."]),
        ("Setting up two more repeats", [
            "The same five-reversal list will appear again, nearly "
            "unchanged, in AN 10.42, before AN 10.43 finally varies "
            "the pattern with a genuinely different list of ten roots "
            "of dispute, this time about disciplinary offenses rather "
            "than doctrine."]),
    ],
    terms=[
        ("vivāda",
         "&ldquo;dispute&rdquo; &mdash; this discourse's own title, "
         "the general condition AN 10.37 gives its extreme case "
         "(schism) a technical definition for."),
        ("bhaṇḍanajātā, kalahajātā",
         "&ldquo;fights, quarrels&rdquo; &mdash; the concrete, "
         "unhappy symptoms Upāli asks the cause of."),
        ("bhikkhū ca na phāsu viharanti",
         "&ldquo;the mendicants don't live happily&rdquo; &mdash; the "
         "practical cost of the same distortion that, at its extreme, "
         "constitutes schism."),
        ("bhaṇḍanakalahaviggahavivādā",
         "&ldquo;fights, quarrels, arguments, and disputes&rdquo; "
         "&mdash; the compound naming, in one word, the full spectrum "
         "of Saṅgha discord Upāli asks about."),
        ("hetu, paccayo",
         "&ldquo;cause&rdquo; and &ldquo;reason&rdquo; &mdash; the "
         "paired terms in Upāli's own question, echoed in the "
         "Buddha's answer."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "answer. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.41:1.1-1.2"),
        ("h3", "The cause of dispute"),
        ("p", "&sect;2", "an10.41:1.3-1.4"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "What causes fights, quarrels, arguments, and disputes "
             "in the Saṅgha",
             "How many qualities a mendicant needs to give ordination",
             "What defines an expulsion offense",
             "How many grounds suspend the recitation of the code"],
         "correct": 0,
         "expl": "The practical root cause of ordinary Saṅgha "
                 "conflict."},
        {"q": "How does the Buddha's answer compare to AN 10.37's "
              "definition of schism?",
         "opts": [
             "Completely unrelated",
             "Word for word the same five reversals, now framed as "
             "the cause of dispute rather than the definition of "
             "schism",
             "A shortened three-item version",
             "The exact opposite content"],
         "correct": 1,
         "expl": "The identical list, reused for a related but "
                 "broader question."},
        {"q": "According to the guide, what is puzzling about this "
              "chapter's title?",
         "opts": [
             "Nothing; it is perfectly explained",
             "The chapter is named Akkosavagga, the Chapter on Abuse, "
             "but the word &ldquo;akkosa&rdquo; does not appear "
             "anywhere in its ten discourses",
             "The chapter has no title at all",
             "The title contradicts the content directly"],
         "correct": 1,
         "expl": "An honest, unresolved mismatch between the "
                 "chapter's name and its actual content."},
        {"q": "What happens to this same list in the following two "
              "discourses, according to the guide?",
         "opts": [
             "It never appears again",
             "AN 10.42 repeats it nearly unchanged, then AN 10.43 "
             "finally varies it with a genuinely different list about "
             "disciplinary offenses",
             "AN 10.42 immediately contradicts it",
             "It is expanded to twenty items"],
         "correct": 1,
         "expl": "One more repeat, then a real variation."},
        {"q": "What is described as the practical cost of this "
              "distortion, short of full schism?",
         "opts": [
             "Nothing in particular",
             "Fights, quarrels, arguments, and disputes, and the "
             "mendicants not living happily",
             "Automatic expulsion from the Saṅgha",
             "A permanent ban on ordaining others"],
         "correct": 1,
         "expl": "Ordinary discord, distinct from the formal, "
                 "extreme case of schism."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, continuing this nipāta's "
                 "pattern for the Upāli exchanges."},
    ],
    marginalia=[
        ("Five reversals, again", [
            "the same distortion",
            "that defines schism, now asked",
            "as a smaller cause",
        ]),
        ("A title that doesn't fit", [
            "&ldquo;Abuse&rdquo; names this",
            "chapter &mdash; yet no discourse here",
            "ever uses the word",
        ]),
        ("One more repeat to come", [
            "AN 10.42 echoes",
            "this list once more, before",
            "10.43 varies it",
        ]),
        ("Cross-references", [
            "AN 10.40 &middot; previous, closing ch.4, Upālivagga",
            "AN 10.37 &middot; the identical five reversals, there "
            "defining schism itself",
            "AN 10.42 &middot; next, the same list under a new title",
        ]),
    ],
    further=[
        '<a href="%s/an10.41/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.40.html">AN 10.40</a> &mdash; previous, closing chapter 4, '
        "Upālivagga.",
        '<a href="an-10.37.html">AN 10.37 &middot; Schism in the Saṅgha</a> &mdash; the '
        "identical five reversals, defining schism itself.",
        '<a href="an-10.42.html">AN 10.42 &middot; Roots of Dispute (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.42 — Paṭhamavivādamūlasutta
# --------------------------------------------------------------------------- #
page(
    42, "Paṭhamavivādamūla", "Roots of Dispute (1st)",
    vagga=VAGGA_5,
    meta_title="AN 10.42 — Roots of Dispute (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamavivādamūlasutta, restating the same ten grounds "
        "as AN 10.41 and AN 10.37 a third time, now as the ten roots "
        "of dispute. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha, "
                     "continuing directly from AN 10.41"),
        ("Form", "A single question, a single ten-item answer, "
                 "identical in substance to AN 10.37 and 10.41"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "third appearance of familiar content"),
    ],
    why=(
        "Upāli asks a more clinical version of AN 10.41's question: "
        "not what causes disputes in general, but how many "
        "<em>roots</em> of dispute there are. The Buddha's answer is, "
        "for a third time, the identical five reversals &mdash; here "
        "given their most technical framing yet."),
    guide=[
        ("The teaching in one sentence", [
            "There are ten roots of dispute: a mendicant explaining "
            "the teaching, the training, and what the Realized One "
            "said, practiced, and prescribed, each as its opposite "
            "&mdash; the same content as AN 10.37's definition of "
            "schism and AN 10.39's account of its cause."]),
        ("Third framing, same substance", [
            "AN 10.37 asked what defines schism; AN 10.41 asked what "
            "causes ordinary discord; this discourse asks, most "
            "abstractly, how many <em>roots</em> (<em>mūla</em>) of "
            "dispute exist. All three questions receive the identical "
            "ten-item answer, without variation."]),
        ("A title announcing its own sequel", [
            "This discourse's title, &ldquo;Roots of Dispute "
            "(1st)&rdquo;, explicitly signals a second installment to "
            "come &mdash; and AN 10.43 delivers it, but not as a mere "
            "repeat: it swaps in a wholly different list, about "
            "disciplinary offenses rather than doctrine, under the "
            "same title format."]),
    ],
    terms=[
        ("vivādamūla",
         "&ldquo;root of dispute&rdquo; &mdash; this discourse's own "
         "title, the most abstract framing yet given to the same "
         "five-reversal content."),
        ("dhammaṁ adhammoti dīpeti",
         "&ldquo;explains the teaching as not the teaching&rdquo; "
         "&mdash; the second half of the first reversal, completing "
         "the pair begun in AN 10.37's terms."),
        ("paṭhama",
         "&ldquo;first&rdquo; &mdash; marking this as the first of a "
         "paired discourse, with AN 10.43 as its explicitly numbered "
         "sequel."),
        ("avinayaṁ vinayoti dīpeti",
         "&ldquo;explains what is not the training as the "
         "training&rdquo; &mdash; the second reversal in this "
         "identical five-category list."),
        ("apaññattaṁ tathāgatena paññattaṁ tathāgatenāti dīpeti",
         "&ldquo;explains what was not prescribed by the Realized One "
         "as prescribed by the Realized One&rdquo; &mdash; the fifth "
         "and final reversal."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "ten roots. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.42:1.1-1.3"),
        ("h3", "Ten roots of dispute"),
        ("p", "&sect;2", "an10.42:1.4-1.5"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "How many roots of dispute there are",
             "How many grounds suspend the recitation of the code",
             "What qualifies a mendicant to be a judge",
             "How schism is defined"],
         "correct": 0,
         "expl": "The most abstract framing yet of the same recurring "
                 "content."},
        {"q": "How does the content of this discourse compare to AN "
              "10.37 and 10.41?",
         "opts": [
             "Completely different",
             "Identical: the same five reversals, appearing for a "
             "third time under a third framing",
             "A shortened summary",
             "An expanded version with new items"],
         "correct": 1,
         "expl": "Three questions, one unchanged ten-item answer."},
        {"q": "What does this discourse's title signal, according to "
              "the guide?",
         "opts": [
             "Nothing beyond this single discourse",
             "An explicit sequel: AN 10.43, &ldquo;Roots of Dispute "
             "(2nd)&rdquo;, which turns out to swap in genuinely "
             "different content",
             "That this is the final discourse in the chapter",
             "A contradiction with AN 10.41"],
         "correct": 1,
         "expl": "A numbered pairing that resolves differently than "
                 "expected."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, continuing the pattern for "
                 "the Upāli exchanges."},
    ],
    marginalia=[
        ("A third telling", [
            "schism, then dispute's",
            "cause, now its abstract roots &mdash;",
            "one list, three questions",
        ]),
        ("A sequel promised", [
            "&ldquo;first&rdquo; in its own name &mdash;",
            "10.43 answers,",
            "but with something new",
        ]),
        ("Most abstract framing yet", [
            "not schism, not cause &mdash;",
            "now simply &ldquo;roots&rdquo;, the same",
            "content, renamed again",
        ]),
        ("Cross-references", [
            "AN 10.41 &middot; previous, the same list as the cause "
            "of dispute",
            "AN 10.37 &middot; the same list again, there defining "
            "schism",
            "AN 10.43 &middot; next, a genuinely different list of "
            "roots",
        ]),
    ],
    further=[
        '<a href="%s/an10.42/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.41.html">AN 10.41 &middot; Dispute</a> &mdash; previous.',
        '<a href="an-10.43.html">AN 10.43 &middot; Roots of Dispute (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.43 — Dutiyavivādamūlasutta
# --------------------------------------------------------------------------- #
page(
    43, "Dutiyavivādamūla", "Roots of Dispute (2nd)",
    vagga=VAGGA_5,
    meta_title="AN 10.43 — Roots of Dispute (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyavivādamūlasutta, which finally breaks the pattern "
        "of the last three discourses with a genuinely new list of "
        "ten roots of dispute over disciplinary offenses. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Upāli questioning the Buddha, "
                     "continuing directly from AN 10.42"),
        ("Form", "A single question, a single ten-item answer, in "
                 "five newly paired reversals"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "genuinely new content after three repeats"),
    ],
    why=(
        "Upāli asks the identical question that opened AN 10.42, "
        "expecting perhaps another repeat &mdash; but this time the "
        "Buddha answers with a wholly different list: not "
        "distortions of doctrine, but disagreements over how to "
        "classify a specific disciplinary offense."),
    guide=[
        ("The teaching in one sentence", [
            "A second set of ten roots of dispute concerns offenses "
            "themselves: misjudging whether something is an offense "
            "at all, whether it is light or serious, whether corrupt "
            "intention was involved, whether it requires "
            "rehabilitation, and whether it has redress &mdash; each "
            "judged wrongly in either direction."]),
        ("The pattern finally breaks", [
            "After AN 10.37, 10.41, and 10.42 all delivered the same "
            "five doctrinal reversals under three different "
            "questions, this discourse repeats only the question's "
            "wording, not its answer &mdash; genuinely new content, "
            "arriving exactly where a fourth repeat might have been "
            "expected."]),
        ("A practical, procedural register", [
            "Where the earlier list concerned doctrine in the "
            "abstract, this one is squarely about case-by-case Vinaya "
            "judgment: whether a specific act counts as an offense, "
            "how serious it is, whether it was intentional, and what "
            "follows from each classification &mdash; the kind of "
            "dispute an <em>ubbāhikā</em> judge (AN 10.33) would "
            "actually be convened to settle."]),
    ],
    terms=[
        ("anāpattiṁ āpattīti dīpeti",
         "&ldquo;explains what is not an offense as an offense&rdquo; "
         "&mdash; the first of this discourse's five new reversals."),
        ("lahukaṁ āpattiṁ garukāpattīti dīpeti",
         "&ldquo;explains a light offense as a serious offense&rdquo; "
         "&mdash; the second reversal, over an offense's severity."),
        ("duṭṭhullaṁ āpattiṁ aduṭṭhullāpattīti dīpeti",
         "&ldquo;explains an offense committed with corrupt intention "
         "as an offense not committed with corrupt intention&rdquo; "
         "&mdash; the third reversal."),
        ("sāvasesaṁ āpattiṁ anavasesāpattīti dīpeti",
         "&ldquo;explains an offense requiring rehabilitation as an "
         "offense not requiring rehabilitation&rdquo; &mdash; the "
         "fourth reversal, over what remedy an offense calls for."),
        ("sappaṭikammaṁ āpattiṁ appaṭikammāpattīti dīpeti",
         "&ldquo;explains an offense with redress as an offense "
         "without redress&rdquo; &mdash; the fifth and final "
         "reversal."),
    ],
    text_intro=(
        "The discourse in full: Upāli's question, and the Buddha's "
        "second, distinct list of ten roots. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Upāli's question"),
        ("p", "&sect;1", "an10.43:1.1-1.3"),
        ("h3", "Ten roots of dispute, over offenses"),
        ("p", "&sect;2", "an10.43:1.4-1.5"),
    ],
    quiz=[
        {"q": "What does Upāli ask about in this discourse?",
         "opts": [
             "The same question as AN 10.42: how many roots of "
             "dispute there are",
             "How to suspend the recitation of the monastic code",
             "What defines harmony in the Saṅgha",
             "How many qualities a preceptor needs"],
         "correct": 0,
         "expl": "The identical question, but this time with a "
                 "different answer."},
        {"q": "How does the Buddha's answer here compare to AN 10.37, "
              "10.41, and 10.42?",
         "opts": [
             "Identical to all three",
             "A genuinely new list, about judging disciplinary "
             "offenses rather than doctrine",
             "A shortened version of the same list",
             "No answer is given"],
         "correct": 1,
         "expl": "The pattern of three straight repeats finally "
                 "breaks here."},
        {"q": "Which of these is one of this discourse's five new "
              "categories of dispute?",
         "opts": [
             "Whether an offense is light or serious",
             "Whether the weather favors travel",
             "Whether a donor's gift was generous",
             "Whether a mendicant is senior or junior"],
         "correct": 0,
         "expl": "One of five: offense/not, light/serious, corrupt/"
                 "not intention, needing/not needing rehabilitation, "
                 "with/without redress."},
        {"q": "According to the guide, what kind of dispute does this "
              "list concern, compared to the earlier one?",
         "opts": [
             "The same kind, doctrine in the abstract",
             "Practical, case-by-case Vinaya judgment &mdash; exactly "
             "the kind of matter an ubbāhikā judge (AN 10.33) would "
             "be convened to settle",
             "A dispute about meditation technique",
             "A dispute about cosmology"],
         "correct": 1,
         "expl": "A shift from doctrinal distortion to procedural "
                 "offense-classification."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given, continuing the pattern for "
                 "the Upāli exchanges."},
    ],
    marginalia=[
        ("The pattern breaks", [
            "same question asked twice &mdash;",
            "but this time a truly new",
            "answer follows it",
        ]),
        ("Judging the offense itself", [
            "light or serious,",
            "meant or not, with remedy",
            "or none &mdash; five new pairs",
        ]),
        ("A judge's real work", [
            "this is what AN 10.33's",
            "judge would actually face &mdash;",
            "not doctrine, but cases",
        ]),
        ("Cross-references", [
            "AN 10.42 &middot; previous, the same question, a "
            "different answer",
            "AN 10.33 &middot; A Judge, whose qualifications this "
            "discourse's content puts to practical use",
            "AN 10.44 &middot; next, at Kusinārā",
        ]),
    ],
    further=[
        '<a href="%s/an10.43/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.42.html">AN 10.42 &middot; Roots of Dispute (1st)</a> &mdash; previous.',
        '<a href="an-10.33.html">AN 10.33 &middot; A Judge</a> &mdash; whose work this '
        "discourse's content serves.",
        '<a href="an-10.44.html">AN 10.44 &middot; At Kusinārā</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.44 — Kusinārasutta
# --------------------------------------------------------------------------- #
page(
    44, "Kusinārā", "At Kusinārā",
    vagga=VAGGA_5,
    meta_title="AN 10.44 — At Kusinārā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kusinārasutta, in which the Buddha lists five things an "
        "accuser must check in themselves and five things they must "
        "establish before accusing another mendicant. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Near Kusinārā, in the Forest of Offerings"),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "Two matched sets of five, ten items total"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "straightforward, practically oriented"),
    ],
    why=(
        "Having just given the technical grounds for disputing an "
        "offense (AN 10.43), the Buddha now turns to the accuser's "
        "own conduct: before pointing a finger, a mendicant must "
        "check five qualities in themselves, and commit to five "
        "further standards of speech &mdash; a discourse about the "
        "ethics of accusation itself."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who wants to accuse another should first "
            "check whether their own bodily and verbal conduct is "
            "pure, whether their heart holds no resentment, whether "
            "they are sufficiently learned, and whether they know "
            "both monastic codes well enough &mdash; and should "
            "commit to speaking at the right time, truthfully, "
            "gently, beneficially, and lovingly."]),
        ("A checklist with social teeth", [
            "Each of the first five self-checks comes with a "
            "consequence attached: if the accuser is found wanting in "
            "any one of them, the source states plainly what "
            "onlookers will say &mdash; &ldquo;train your own bodily "
            "behavior first,&rdquo; and so on &mdash; making this not "
            "merely an ideal but a socially enforced standard."]),
        ("A famous quintet of speech", [
            "The second five &mdash; speaking at the right time, "
            "truthfully, gently, beneficially, and lovingly &mdash; "
            "closely track the well-known five factors of well-spoken "
            "speech taught elsewhere in the canon, here repurposed "
            "specifically for the moment of leveling an accusation."]),
        ("A rare place-name setting", [
            "Kusinārā, the site of the Buddha's eventual "
            "extinguishment, appears here simply as an ordinary "
            "teaching location with no narrative weight attached "
            "&mdash; this discourse gives no indication of when in "
            "the Buddha's life it was spoken."]),
    ],
    terms=[
        ("codaka",
         "&ldquo;accuser&rdquo; &mdash; the mendicant this discourse "
         "addresses, about to bring a charge against another."),
        ("kāyasamācāra, vacīsamācāra",
         "&ldquo;bodily behavior, verbal behavior&rdquo; &mdash; the "
         "first two qualities an accuser must check in themselves."),
        ("mettacitta",
         "a heart &ldquo;established in love&rdquo; for one's "
         "spiritual companions, without resentment &mdash; the third "
         "quality to check."),
        ("kālena vakkhāmi, no akālena",
         "&ldquo;I will speak at the right time, not at the wrong "
         "time&rdquo; &mdash; the first of the five standards an "
         "accuser must establish."),
        ("ubhayāni pātimokkhāni",
         "&ldquo;both monastic codes&rdquo; &mdash; the fifth "
         "self-check, echoing AN 10.33's judge qualification."),
    ],
    text_intro=(
        "The discourse in full: the setting, the five self-checks, "
        "and the five standards of speech. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Setting"),
        ("p", "&sect;1", "an10.44:1.1-1.5"),
        ("h3", "Five things to check in oneself"),
        ("p", "&sect;2", "an10.44:2.1-6.7"),
        ("h3", "Five things to establish in oneself"),
        ("p", "&sect;3", "an10.44:7.1-7.8"),
    ],
    quiz=[
        {"q": "What must a mendicant who wants to accuse another do "
              "first, according to this discourse?",
         "opts": [
             "Nothing; accusations may be made freely",
             "Check five qualities in themselves and establish five "
             "further standards of speech",
             "Consult only the preceptor",
             "Wait a full year before speaking"],
         "correct": 1,
         "expl": "A ten-item ethics of accusation, five to check and "
                 "five to establish."},
        {"q": "What happens if the accuser is found lacking in one of "
              "the first five qualities, according to the guide?",
         "opts": [
             "Nothing follows from it",
             "The source states what onlookers will say &mdash; e.g. "
             "&ldquo;train your own bodily behavior first&rdquo; "
             "&mdash; making it a socially enforced standard",
             "The accuser is automatically expelled",
             "The accusation becomes stronger"],
         "correct": 1,
         "expl": "A checklist with a stated social consequence "
                 "attached to each item."},
        {"q": "What does the guide note about the second set of five "
              "qualities?",
         "opts": [
             "They are unrelated to speech",
             "They closely track a well-known set of five factors of "
             "well-spoken speech found elsewhere in the canon",
             "They are ten items, not five",
             "They only apply to laypeople"],
         "correct": 1,
         "expl": "Right time, truth, gentleness, benefit, and love "
                 "&mdash; a familiar quintet repurposed here."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Near Kusinārā, in the Forest of Offerings",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "The place-name giving this discourse its title."},
        {"q": "Does this discourse connect Kusinārā to the Buddha's "
              "eventual passing?",
         "opts": [
             "Yes, explicitly",
             "No &mdash; the place appears here with no narrative "
             "weight, simply as an ordinary teaching location",
             "Only in a single ambiguous line",
             "The setting is left unstated"],
         "correct": 1,
         "expl": "No indication is given of when in the Buddha's life "
                 "this was spoken."},
    ],
    marginalia=[
        ("Before you accuse", [
            "check body, speech, heart,",
            "learning, both codes &mdash; then speak",
            "true, gentle, in time",
        ]),
        ("A checklist with teeth", [
            "fail one, and others",
            "will say so aloud &mdash; not just",
            "a private standard",
        ]),
        ("An ordinary place-name", [
            "Kusinārā here",
            "carries no special weight &mdash;",
            "just where this was taught",
        ]),
        ("Cross-references", [
            "AN 10.43 &middot; previous, the technical grounds for "
            "disputing an offense",
            "AN 10.45 &middot; next, ten drawbacks of entering a "
            "royal compound",
        ]),
    ],
    further=[
        '<a href="%s/an10.44/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.43.html">AN 10.43 &middot; Roots of Dispute (2nd)</a> &mdash; previous.',
        '<a href="an-10.45.html">AN 10.45 &middot; Entering a Royal Compound</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.45 — Rājantepurappavesanasutta
# --------------------------------------------------------------------------- #
page(
    45, "Rājantepurappavesana", "Entering a Royal Compound",
    vagga=VAGGA_5,
    meta_title="AN 10.45 — Entering a Royal Compound | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Rājantepurappavesanasutta, the Buddha's vivid, almost "
        "comic ten-item catalogue of everything that can go wrong "
        "when a monk enters a royal harem compound. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "Ten numbered drawbacks, mostly following a repeated "
                 "narrative pattern"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "vivid and easy to follow"),
    ],
    why=(
        "In the most concretely narrative discourse of this chapter "
        "so far, the Buddha catalogues ten specific ways a mendicant "
        "can come under suspicion simply by entering a king's private "
        "compound &mdash; from a shared smile misread as an affair to "
        "being blamed for a lost gem, a royal pregnancy, or a leaked "
        "state secret."),
    guide=[
        ("The teaching in one sentence", [
            "Entering a royal compound carries ten drawbacks: a "
            "misread smile, being blamed for an unremembered "
            "pregnancy, a lost gem, a leaked secret, a father or son's "
            "grief, a promotion or demotion, an army dispatched "
            "wrongly or recalled, and unavoidable sensory temptation "
            "&mdash; each capable of ruining a mendicant's reputation "
            "through no fault of their own."]),
        ("Suspicion, not misconduct", [
            "Strikingly, none of the first nine drawbacks describes "
            "actual wrongdoing by the monk: each is a case of "
            "circumstantial suspicion falling on him simply because "
            "he was present, illustrating how a monastic's mere "
            "proximity to power creates risk regardless of conduct."]),
        ("A repeated narrative engine", [
            "Drawbacks two through nine share a near-identical "
            "structure: something goes wrong in the palace, and the "
            "king or courtiers reason, &ldquo;no-one else has entered "
            "here except that monk &mdash; could this be his "
            "doing?&rdquo; &mdash; a refrain repeated eight times with "
            "only the misfortune changing."]),
        ("A tenth drawback of a different kind", [
            "Only the final drawback breaks the pattern: rather than "
            "another incident of misplaced blame, it names the plain "
            "sensory temptation &mdash; the trampling of elephants, "
            "horses, and chariots, and arousing sights, sounds, "
            "smells, tastes, and touches &mdash; that simply does not "
            "belong in a monastic life, closing the list on an "
            "internal rather than reputational risk."]),
    ],
    terms=[
        ("rājantepura",
         "&ldquo;royal compound&rdquo; or inner palace &mdash; "
         "specifically the women's quarters, this discourse's own "
         "title and subject."),
        ("ādīnava",
         "&ldquo;drawback&rdquo; or danger &mdash; the term counting "
         "each of the ten items in this list."),
        ("na kho idha añño koci pavisati, aññatra pabbajitena",
         "&ldquo;no-one else has entered here, except for that "
         "monk&rdquo; &mdash; the refrain repeated across most of the "
         "ten drawbacks."),
        ("na pabbajitassa sāruppāni",
         "&ldquo;that do not befit a monk&rdquo; &mdash; the closing "
         "phrase naming the tenth drawback's sensory dangers."),
        ("aññataraṁ ratanaṁ nassati",
         "&ldquo;a gem is lost somewhere in the royal compound&rdquo; "
         "&mdash; the third drawback, another case of circumstantial "
         "blame falling on the visiting monk."),
    ],
    text_intro=(
        "The discourse in full: all ten drawbacks. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten drawbacks of entering a royal compound"),
        ("p", "&sect;1", "an10.45:1.1-10.3"),
    ],
    quiz=[
        {"q": "What is this discourse's subject?",
         "opts": [
             "Ten benefits of royal patronage",
             "Ten drawbacks of a monk entering a royal compound",
             "Ten qualities of a good king",
             "Ten rules for lay donors"],
         "correct": 1,
         "expl": "A vivid catalogue of everything that can go wrong."},
        {"q": "According to the guide, what do the first nine "
              "drawbacks have in common?",
         "opts": [
             "They all describe actual misconduct by the monk",
             "None describes real wrongdoing; each is circumstantial "
             "suspicion falling on him simply for being present",
             "They are all about financial loss",
             "They only apply to nuns, not monks"],
         "correct": 1,
         "expl": "Proximity to power creates risk regardless of "
                 "actual conduct."},
        {"q": "What refrain is repeated across most of the ten "
              "drawbacks?",
         "opts": [
             "&ldquo;The king is generous&rdquo;",
             "&ldquo;No-one else has entered here, except for that "
             "monk &mdash; could this be his doing?&rdquo;",
             "&ldquo;The queen is wise&rdquo;",
             "There is no repeated refrain"],
         "correct": 1,
         "expl": "The same suspicious reasoning, applied to eight "
                 "different misfortunes."},
        {"q": "How does the tenth drawback differ from the rest, "
              "according to the guide?",
         "opts": [
             "It does not differ at all",
             "It names plain sensory temptation rather than another "
             "case of misplaced blame &mdash; an internal risk, not a "
             "reputational one",
             "It is about financial corruption specifically",
             "It repeats the ninth drawback exactly"],
         "correct": 1,
         "expl": "A shift from circumstantial suspicion to genuine "
                 "sensory danger."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("A smile, misread", [
            "queen smiles, monk smiles back &mdash;",
            "the king draws his own",
            "conclusion, wrongly",
        ]),
        ("Blamed by presence alone", [
            "a gem goes missing,",
            "a secret leaks &mdash; &ldquo;no-one else",
            "entered here but him&rdquo;",
        ]),
        ("A different tenth risk", [
            "not suspicion now,",
            "but elephants, chariots,",
            "sights not fit for robes",
        ]),
        ("Cross-references", [
            "AN 10.44 &middot; previous, at Kusinārā",
            "AN 10.46 &middot; next, with the Sakyans",
        ]),
    ],
    further=[
        '<a href="%s/an10.45/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.44.html">AN 10.44 &middot; At Kusinārā</a> &mdash; previous.',
        '<a href="an-10.46.html">AN 10.46 &middot; With the Sakyans</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.46 — Sakyasutta
# --------------------------------------------------------------------------- #
page(
    46, "Sakya", "With the Sakyans",
    vagga=VAGGA_5,
    meta_title="AN 10.46 — With the Sakyans | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sakyasutta, in which the Buddha uses an escalating "
        "wealth simile and a mirrored countdown of practice-years to "
        "urge lay Sakyans toward the eight-factored sabbath. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kapilavatthu, in the land of the Sakyans, at "
                     "the Banyan Tree Monastery"),
        ("Speakers", "The Buddha addressing several Sakyan lay "
                     "followers"),
        ("Form", "A dialogue building two escalating similes: rising "
                 "wealth, then a countdown of practice-time"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "long but propelled by clear repetition"),
    ],
    why=(
        "When several Sakyan lay followers admit they only "
        "sometimes keep the eight-factored sabbath, the Buddha builds "
        "a case in two movements: first, that even a lifetime of "
        "accumulated wealth cannot buy a single day of perfect "
        "happiness, and second, that even a single day of diligent "
        "practice can secure it, along with a real shot at "
        "stream-entry."),
    guide=[
        ("The teaching in one sentence", [
            "No amount of wealth, however large, can buy even a "
            "single day or night of perfect happiness, because "
            "sensual pleasures are impermanent and hollow; but a "
            "disciple who practices diligently for as little as a "
            "single day can experience that happiness for a hundred "
            "thousand years and become, at the very least, a "
            "stream-enterer."]),
        ("An escalating wealth simile", [
            "The Buddha walks the Sakyans up an elided ladder of "
            "daily earnings &mdash; half a dollar, then a dollar, "
            "then two through ten, twenty through a hundred &mdash; "
            "each time asking whether this still counts as an honest, "
            "industrious wage, before revealing that even a "
            "century's accumulated fortune cannot purchase a single "
            "day of true happiness."]),
        ("A mirrored countdown, in reverse", [
            "The second half runs the same rhetorical device "
            "backward: instead of climbing upward in wealth, it "
            "counts diligent practice downward &mdash; ten years, "
            "nine, eight&hellip; down through months, then days, all "
            "the way to a single day &mdash; each length still "
            "sufficient for the same extraordinary result, driving "
            "home how disproportionately small an investment secures "
            "an incomparably larger return."]),
        ("A concrete number in a doctrinal text", [
            "The wealth simile's dollar figures are an unusually "
            "concrete, almost mercantile detail for this project's "
            "discourses so far, giving the Sakyans' own world of "
            "trade and commerce as the very measure the Buddha uses "
            "to outbid it."]),
    ],
    terms=[
        ("uposatha aṭṭhaṅgasamannāgata",
         "&ldquo;the sabbath endowed with eight factors&rdquo; "
         "&mdash; the observance-day practice the Sakyans admit they "
         "keep only inconsistently."),
        ("aniccā, tucchā, musā, mosadhammā",
         "&ldquo;impermanent, hollow, false, and deceptive&rdquo; "
         "&mdash; the Sakyans' own four-word verdict on sensual "
         "pleasures, given in answer to the Buddha's question."),
        ("appamatto ātāpī pahitatto",
         "&ldquo;diligent, keen, and resolute&rdquo; &mdash; the "
         "three qualities of practice that, sustained even briefly, "
         "outweigh a lifetime of wealth."),
        ("apaṇṇakaṁ sotāpanno",
         "&ldquo;as a sure bet, a stream-enterer&rdquo; &mdash; the "
         "guaranteed minimum result promised even for the shortest "
         "span of diligent practice named."),
        ("kahāpaṇa",
         "a unit of currency, rendered &ldquo;dollar&rdquo; in this "
         "translation &mdash; the escalating unit counted upward "
         "through the wealth simile."),
    ],
    text_intro=(
        "The discourse in full: the Sakyans' admission, the rising "
        "wealth simile, and the descending countdown of practice. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Sakyans' admission"),
        ("p", "&sect;1", "an10.46:1.1-1.5"),
        ("h3", "A rising simile of wealth"),
        ("p", "&sect;2", "an10.46:2.1-5.3"),
        ("h3", "Wealth cannot buy a single day's happiness"),
        ("p", "&sect;3", "an10.46:6.1-6.5"),
        ("h3", "A countdown of practice, and the Sakyans' resolve"),
        ("p", "&sect;4", "an10.46:7.1-12.11"),
    ],
    quiz=[
        {"q": "What do the Sakyan lay followers admit at the start of "
              "this discourse?",
         "opts": [
             "That they never observe the sabbath",
             "That they only sometimes observe the eight-factored "
             "sabbath",
             "That they have never heard of the sabbath",
             "That they observe it perfectly every time"],
         "correct": 1,
         "expl": "An honest, partial admission that prompts the "
                 "Buddha's teaching."},
        {"q": "What does the rising wealth simile ultimately show, "
              "according to the guide?",
         "opts": [
             "That wealth is inherently evil",
             "That even a century's accumulated fortune cannot "
             "purchase a single day or night of true happiness",
             "That the Sakyans are unusually wealthy",
             "That daily wages should be higher"],
         "correct": 1,
         "expl": "An escalating ladder of earnings, climbing toward a "
                 "deliberately unsatisfying conclusion."},
        {"q": "How does the second half of the discourse mirror the "
              "first, according to the guide?",
         "opts": [
             "It repeats the same wealth figures exactly",
             "It runs a matching countdown in the opposite direction "
             "&mdash; practice-years descending from ten down to a "
             "single day, each still sufficient for the same result",
             "It has no relation to the first half",
             "It abandons similes entirely for plain statement"],
         "correct": 1,
         "expl": "A mirrored rhetorical structure, wealth ascending "
                 "and practice-time descending."},
        {"q": "What is guaranteed even for a single day of diligent "
              "practice, according to this discourse?",
         "opts": [
             "Nothing in particular",
             "Extraordinary happiness, and at the very least "
             "stream-entry as &ldquo;a sure bet&rdquo;",
             "Immediate full enlightenment",
             "Only a modest improvement in mood"],
         "correct": 1,
         "expl": "A remarkably strong guarantee attached to even the "
                 "shortest span named."},
        {"q": "How do the Sakyans respond by the end of the "
              "discourse?",
         "opts": [
             "They reject the Buddha's teaching",
             "They resolve, from that day forth, to observe the "
             "eight-factored sabbath",
             "They ask no further questions and leave silently",
             "They request a different teaching entirely"],
         "correct": 1,
         "expl": "A concrete resolution closing the exchange."},
    ],
    marginalia=[
        ("A fortune, still not enough", [
            "half a dollar, then",
            "a hundred a day for years &mdash;",
            "not one happy night",
        ]),
        ("One day, outweighing all", [
            "diligent a day,",
            "and stream-entry is a sure",
            "bet, the Buddha says",
        ]),
        ("Two similes, mirrored", [
            "wealth climbs up and up;",
            "practice-years count down instead &mdash;",
            "both arrive at one",
        ]),
        ("Cross-references", [
            "AN 10.45 &middot; previous, ten drawbacks of entering a "
            "royal compound",
            "AN 10.47 &middot; next, with Mahāli",
        ]),
    ],
    further=[
        '<a href="%s/an10.46/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.45.html">AN 10.45 &middot; Entering a Royal Compound</a> &mdash; '
        "previous.",
        '<a href="an-10.47.html">AN 10.47 &middot; With Mahāli</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.47 — Mahālisutta
# --------------------------------------------------------------------------- #
page(
    47, "Mahāli", "With Mahāli",
    vagga=VAGGA_5,
    meta_title="AN 10.47 — With Mahāli | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Mahālisutta, in which the Buddha gives Mahāli the "
        "Licchavi five causes of bad deeds and five causes of good "
        "deeds, expanding the classic three roots with two cognitive "
        "factors. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with "
                     "the peaked roof"),
        ("Speakers", "Mahāli the Licchavi questioning the Buddha"),
        ("Form", "Two matched questions, each answered with a "
                 "five-item list, in a repeated five-fold formula"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "builds on very familiar doctrinal ground"),
    ],
    why=(
        "Mahāli the Licchavi asks the most basic ethical question "
        "there is: why do people do bad things, and why do they do "
        "good things? The Buddha's paired five-item answers expand "
        "the classic three roots of greed, hate, and delusion with "
        "two further cognitive causes on each side."),
    guide=[
        ("The teaching in one sentence", [
            "Bad deeds arise from greed, hate, delusion, irrational "
            "application of mind, and a wrongly directed mind; good "
            "deeds arise from their five opposites &mdash; "
            "contentment, love, understanding, rational application "
            "of mind, and a rightly directed mind &mdash; and without "
            "all ten, neither immoral nor moral conduct would ever be "
            "seen in the world."]),
        ("The classic three roots, expanded to five", [
            "The first three items on each side &mdash; greed, hate, "
            "delusion versus their positive counterparts &mdash; are "
            "the three unwholesome and wholesome roots met "
            "repeatedly elsewhere in this project; this discourse "
            "adds two further causes on each side, both about how the "
            "mind attends to its object: irrational or rational "
            "application of mind, and a wrongly or rightly directed "
            "mind."]),
        ("A tidy symmetry", [
            "Unlike many of this chapter's lists, this one closes "
            "with an explicit logical claim rather than a bare "
            "listing: if these ten things did not exist in the world, "
            "neither immoral nor moral conduct would ever appear "
            "&mdash; the causes are offered as jointly necessary and "
            "sufficient, not merely descriptive."]),
    ],
    terms=[
        ("ayoniso manasikāra, yoniso manasikāra",
         "&ldquo;irrational application of mind, rational application "
         "of mind&rdquo; &mdash; the fourth cause on each side, "
         "concerning how attention is directed."),
        ("micchāpaṇihitaṁ cittaṁ, sammāpaṇihitaṁ cittaṁ",
         "&ldquo;a wrongly directed mind, a rightly directed "
         "mind&rdquo; &mdash; the fifth and final cause on each side."),
        ("lobha, dosa, moha",
         "greed, hate, and delusion &mdash; the classic three "
         "unwholesome roots, forming this discourse's first three "
         "causes of bad deeds."),
        ("alobho, adoso, amoho",
         "non-greed, non-hate, non-delusion &mdash; the three "
         "wholesome roots forming this discourse's first three causes "
         "of good deeds."),
        ("hetu, paccayo",
         "&ldquo;cause&rdquo; and &ldquo;reason&rdquo; &mdash; the "
         "paired terms in Mahāli's own question, echoed through both "
         "of the Buddha's five-item answers."),
    ],
    text_intro=(
        "The discourse in full: Mahāli's two questions, and the "
        "Buddha's two five-item answers. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "The cause of bad deeds"),
        ("p", "&sect;1", "an10.47:1.1-1.9"),
        ("h3", "The cause of good deeds"),
        ("p", "&sect;2", "an10.47:2.1-2.9"),
    ],
    quiz=[
        {"q": "What does Mahāli ask the Buddha?",
         "opts": [
             "Why the Saṅgha follows monastic law",
             "What causes bad deeds, and what causes good deeds",
             "How to enter a royal compound safely",
             "What defines schism in the Saṅgha"],
         "correct": 1,
         "expl": "The most basic possible ethical question."},
        {"q": "According to the guide, what do the first three items "
              "on each side represent?",
         "opts": [
             "A brand new list unique to this discourse",
             "The classic three unwholesome and wholesome roots "
             "&mdash; greed, hate, delusion and their opposites "
             "&mdash; met repeatedly elsewhere in this project",
             "Ten unrelated Vinaya categories",
             "A list about royal compounds"],
         "correct": 1,
         "expl": "Familiar doctrinal ground, expanded here."},
        {"q": "What two additional causes does this discourse add "
              "beyond the classic three roots?",
         "opts": [
             "Two more offense categories",
             "Irrational or rational application of mind, and a "
             "wrongly or rightly directed mind",
             "Two additional forms of greed",
             "No additional causes are given"],
         "correct": 1,
         "expl": "Two cognitive factors about how attention and "
                 "intention are directed."},
        {"q": "How does this discourse close, according to the "
              "guide?",
         "opts": [
             "With a bare list and nothing more",
             "With an explicit logical claim: without these ten "
             "things, neither immoral nor moral conduct would ever "
             "be seen in the world",
             "With a verse",
             "With an unanswered question"],
         "correct": 1,
         "expl": "The causes are framed as jointly necessary and "
                 "sufficient."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood, in the hall with the peaked "
             "roof",
             "No setting is stated in the source"],
         "correct": 2,
         "expl": "A specific, named location, unlike most of this "
                 "chapter's Upāli exchanges."},
    ],
    marginalia=[
        ("Ten causes, mirrored", [
            "greed, hate, delusion &mdash; then",
            "how the mind attends,",
            "and where it is aimed",
        ]),
        ("Three roots, familiar", [
            "met before, in other",
            "chapters, other nipātas &mdash;",
            "now given two more",
        ]),
        ("A necessary ten", [
            "without these causes,",
            "the guide notes, the world would see",
            "neither good nor bad",
        ]),
        ("Cross-references", [
            "AN 10.46 &middot; previous, with the Sakyans",
            "AN 10.48 &middot; next, ten regular reflections for a "
            "renunciate",
        ]),
    ],
    further=[
        '<a href="%s/an10.47/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.46.html">AN 10.46 &middot; With the Sakyans</a> &mdash; previous.',
        '<a href="an-10.48.html">AN 10.48 &middot; Ten Regular Reflections for a '
        'Renunciate</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.48 — Pabbajitaabhiṇhasutta
# --------------------------------------------------------------------------- #
page(
    48, "Pabbajitaabhiṇha", "Ten Regular Reflections for a Renunciate",
    vagga=VAGGA_5,
    meta_title="AN 10.48 — Ten Regular Reflections for a Renunciate | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Pabbajitaabhiṇhasutta, one of the canon's best-known "
        "chanted lists: the ten things a renunciate should reflect "
        "on again and again. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "Ten first-person reflections, listed in sequence"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plainly stated, though weighty to sit with"),
    ],
    why=(
        "This discourse gives one of the most widely known lists in "
        "the entire canon &mdash; still chanted in monasteries today "
        "&mdash; ten first-person reflections a renunciate should "
        "return to again and again, from having left social class "
        "behind to facing, unflinching, the fact of death."),
    guide=[
        ("The teaching in one sentence", [
            "One who has gone forth should often reflect: I have "
            "secured freedom from class; my livelihood depends on "
            "others; my behavior must change accordingly; am I "
            "blameless in ethics, and free of my companions' "
            "reproach; I will be parted from all I hold dear; I am "
            "the owner and heir of my own deeds; what am I becoming "
            "as the days pass; do I love solitude; and do I have "
            "anything to show for this practice when I die?"]),
        ("A list built for daily return", [
            "Unlike most lists in this project, this one is framed "
            "explicitly for repeated, ongoing use &mdash; "
            "<em>abhiṇhaṁ</em>, &ldquo;often, again and again&rdquo; "
            "&mdash; not as doctrine to be understood once but as a "
            "practice of regular self-examination, still recited in "
            "many monastic communities today."]),
        ("From social status to mortality", [
            "The ten reflections trace an arc: the first three "
            "concern the renunciate's changed social position "
            "(freedom from caste, dependent livelihood, changed "
            "conduct), the middle four turn inward to ethics, loss, "
            "and karma, and the final three confront practice "
            "directly &mdash; daily self-scrutiny, love of "
            "solitude, and, starkly, whether there will be anything "
            "to show for it at the moment of death."]),
        ("A death-facing final reflection", [
            "The tenth and final reflection is unusually direct for "
            "this project: it asks whether the renunciate has "
            "&ldquo;any superhuman distinctions in knowledge and "
            "vision&rdquo; worthy of the noble ones, so that when "
            "spiritual companions question them on their deathbed "
            "they will not be embarrassed &mdash; making the entire "
            "list, in effect, an examination to be passed before "
            "death arrives."]),
    ],
    terms=[
        ("abhiṇhaṁ paccavekkhitabbaṁ",
         "&ldquo;should often review&rdquo; &mdash; the phrase "
         "framing this list as a practice of repeated reflection, not "
         "a one-time teaching."),
        ("vevaṇṇiyamhi ajjhupagato",
         "&ldquo;I have secured freedom from class&rdquo; &mdash; "
         "the first reflection, on having left caste status behind "
         "at ordination."),
        ("kammassakomhi kammadāyādo kammayoni kammabandhu "
         "kammapaṭisaraṇo",
         "&ldquo;I am the owner of my deeds and heir to my deeds. "
         "Deeds are my womb, my relative, and my refuge&rdquo; "
         "&mdash; the seventh and eighth reflections together, on "
         "the ownership of karma."),
        ("suññāgāre abhiramāmi",
         "&ldquo;do I love to stay in empty huts?&rdquo; &mdash; the "
         "ninth reflection, on love of solitude."),
        ("añño me ākappo karaṇīyo",
         "&ldquo;my behavior should be different&rdquo; &mdash; the "
         "third reflection, on the changed conduct expected of a "
         "renunciate."),
    ],
    text_intro=(
        "The discourse in full: all ten reflections. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten regular reflections"),
        ("p", "&sect;1", "an10.48:1.1-13.1"),
    ],
    quiz=[
        {"q": "What kind of list is this discourse giving, according "
              "to the guide?",
         "opts": [
             "A doctrine to be understood once and set aside",
             "A list framed for repeated, ongoing use &mdash; "
             "reflected on again and again, still chanted in many "
             "monasteries today",
             "A list of monastic offenses",
             "A cosmological survey"],
         "correct": 1,
         "expl": "The word abhiṇhaṁ, &ldquo;often,&rdquo; frames the "
                 "whole list as a practice."},
        {"q": "What arc do the ten reflections trace, according to "
              "the guide?",
         "opts": [
             "A random, unordered list",
             "From changed social position, through ethics and karma, "
             "to practice and, finally, facing death",
             "A purely cosmological sequence",
             "A list of monastic ranks"],
         "correct": 1,
         "expl": "Social status, ethics and loss, then practice and "
                 "mortality."},
        {"q": "What does the tenth and final reflection ask?",
         "opts": [
             "Whether the renunciate has family wealth",
             "Whether they have any superhuman distinctions in "
             "knowledge and vision, so as not to be embarrassed when "
             "questioned on their deathbed",
             "Whether they have memorized all the rules",
             "Whether they are physically strong"],
         "correct": 1,
         "expl": "A death-facing conclusion to the whole list."},
        {"q": "What are the seventh and eighth reflections about?",
         "opts": [
             "The weather and seasons",
             "Being the owner and heir of one's own deeds (karma)",
             "Royal compounds",
             "The eight-factored sabbath"],
         "correct": 1,
         "expl": "Ownership of karma, described as one's womb, "
                 "relative, and refuge."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this well-known list."},
    ],
    marginalia=[
        ("Ten daily returns", [
            "class left behind, deeds",
            "owned and inherited, death",
            "faced without flinching",
        ]),
        ("Still chanted today", [
            "not a one-time teaching",
            "but a practice, returned to",
            "again and again",
        ]),
        ("An exam before death", [
            "the tenth reflection:",
            "will I be embarrassed when",
            "questioned at the end?",
        ]),
        ("Cross-references", [
            "AN 10.47 &middot; previous, with Mahāli",
            "AN 10.49 &middot; next, existing because of the body",
        ]),
    ],
    further=[
        '<a href="%s/an10.48/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.47.html">AN 10.47 &middot; With Mahāli</a> &mdash; previous.',
        '<a href="an-10.49.html">AN 10.49 &middot; Existing Because of the Body</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.49 — Sarīraṭṭhadhammasutta
# --------------------------------------------------------------------------- #
page(
    49, "Sarīraṭṭhadhamma", "Existing Because of the Body",
    vagga=VAGGA_5,
    meta_title="AN 10.49 — Existing Because of the Body | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sarīraṭṭhadhammasutta, a short, unusual list of ten "
        "things that exist simply because a body exists &mdash; from "
        "cold and hunger to the will to live on. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A single flat list of ten, with no elaboration"),
        ("Length", "under 1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the shortest discourse in this chapter"),
    ],
    why=(
        "In one of the briefest discourses in this project so far, "
        "the Buddha simply names ten things that exist because a "
        "body exists &mdash; an unusual mix spanning raw physical "
        "sensation, ethical restraint, and the will to be reborn, "
        "offered with no further comment."),
    guide=[
        ("The teaching in one sentence", [
            "Ten things exist because of the body: cold, heat, "
            "hunger, thirst, feces, urine, restraint of body, speech, "
            "and livelihood, and the will to live that leads to "
            "future lives."]),
        ("Three registers in one list", [
            "Unlike most ten-item lists in this project, which stay "
            "within a single register, this one mixes three: four "
            "purely physical discomforts (cold, heat, hunger, "
            "thirst), two bodily functions (feces, urine), three "
            "forms of ethical restraint bundled as one item, and, "
            "startlingly, the will to live that drives rebirth "
            "itself &mdash; placed on the same list as needing to "
            "urinate."]),
        ("No elaboration given", [
            "This discourse offers no similes, no narrative frame, "
            "and no explanation of why these ten specifically belong "
            "together; it simply states the list and stops, among "
            "the flattest, least adorned discourses met in this "
            "project."]),
        ("The body as the ground of practice, bluntly stated", [
            "Read together, the list makes an implicit point without "
            "spelling it out: having a body means living with its "
            "constant, unglamorous demands &mdash; and even the "
            "aspiration to escape the cycle of rebirth is itself, in "
            "this listing, counted as one more thing the body gives "
            "rise to."]),
    ],
    terms=[
        ("sarīraṭṭha",
         "&ldquo;existing because of the body&rdquo; &mdash; this "
         "discourse's own title, naming its whole subject in one "
         "compound."),
        ("sīta, uṇha, jighacchā, pipāsā",
         "&ldquo;cold, heat, hunger, thirst&rdquo; &mdash; the first "
         "four items, purely physical discomforts."),
        ("ponobhaviko bhavasaṅkhāro",
         "&ldquo;the will to live that leads to future lives&rdquo; "
         "&mdash; the tenth and final item, placing the drive toward "
         "rebirth itself on this otherwise mundane list."),
        ("uccāro, passāvo",
         "&ldquo;feces, urine&rdquo; &mdash; the plainest of the ten "
         "items, naming ordinary bodily function without euphemism."),
        ("kāyasaṁvaro, vacīsaṁvaro, ājīvasaṁvaro",
         "&ldquo;restraint of body, speech, and livelihood&rdquo; "
         "&mdash; three items of ethical restraint bundled together "
         "as the seventh, eighth, and ninth of the ten."),
    ],
    text_intro=(
        "The discourse in full: the ten things existing because of "
        "the body. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten things existing because of the body"),
        ("p", "&sect;1", "an10.49:1.1-1.4"),
    ],
    quiz=[
        {"q": "What is the subject of this discourse?",
         "opts": [
             "Ten meditation techniques",
             "Ten things that exist because a body exists",
             "Ten qualities of a good teacher",
             "Ten grounds for suspending recitation"],
         "correct": 1,
         "expl": "A flat, unelaborated list naming the body's "
                 "consequences."},
        {"q": "According to the guide, how many distinct registers "
              "does this list mix?",
         "opts": [
             "Just one: purely physical discomfort",
             "Three: physical discomfort, bodily function, and the "
             "will to be reborn",
             "Five separate registers",
             "None; every item is identical in kind"],
         "correct": 1,
         "expl": "Cold and hunger sit alongside ethical restraint and "
                 "the drive toward rebirth."},
        {"q": "What is unusual about the tenth and final item, "
              "according to the guide?",
         "opts": [
             "It is a repeat of the ninth item",
             "It places the will to live that drives rebirth itself "
             "on the same mundane list as needing to urinate",
             "It is left completely blank",
             "It contradicts the rest of the list"],
         "correct": 1,
         "expl": "A striking juxtaposition of the ordinary and the "
                 "profound."},
        {"q": "How much elaboration does this discourse give for its "
              "list?",
         "opts": [
             "A full simile for each item",
             "None &mdash; it simply states the list and stops, among "
             "the flattest discourses in this project",
             "A lengthy narrative frame",
             "A closing verse"],
         "correct": 1,
         "expl": "No similes, no narrative, no explanation of why "
                 "these ten belong together."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this brief discourse."},
    ],
    marginalia=[
        ("Ten things, one body", [
            "cold, hunger, thirst, and",
            "the urge to be reborn &mdash;",
            "all from having flesh",
        ]),
        ("No comment offered", [
            "no simile here,",
            "no story &mdash; just the list, stark",
            "and then the sutta ends",
        ]),
        ("Even rebirth, bodily", [
            "the drive to live on",
            "sits beside needing to pee &mdash;",
            "flesh explains it all",
        ]),
        ("Cross-references", [
            "AN 10.48 &middot; previous, ten regular reflections for "
            "a renunciate",
            "AN 10.50 &middot; next, closing this chapter and the "
            "First Fifty",
        ]),
    ],
    further=[
        '<a href="%s/an10.49/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.48.html">AN 10.48 &middot; Ten Regular Reflections for a '
        'Renunciate</a> &mdash; previous.',
        '<a href="an-10.50.html">AN 10.50 &middot; Fights</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.50 — Bhaṇḍanasutta
# --------------------------------------------------------------------------- #
page(
    50, "Bhaṇḍana", "Fights",
    vagga=VAGGA_5,
    meta_title="AN 10.50 — Fights | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bhaṇḍanasutta, closing the Akkosavagga and the First "
        "Fifty of the Tens: the Buddha catches mendicants quarreling "
        "and teaches ten warm-hearted qualities, the ten-item "
        "expansion of the six sāraṇīyā dhammā. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's "
                     "monastery"),
        ("Speakers", "The Buddha, addressing mendicants he catches "
                     "quarreling"),
        ("Form", "A narrative opening, then ten items in a repeated "
                 "formula, mostly elided"),
        ("Length", "~2 minutes to read"),
        ("Closing this chapter and the First Fifty", "This discourse "
                                                      "closes both "
                                                      "Akkosavagga, "
                                                      "the fifth "
                                                      "chapter, and "
                                                      "the First "
                                                      "Fifty of the "
                                                      "entire Book of "
                                                      "the Tens, "
                                                      "carrying a "
                                                      "double closing "
                                                      "colophon"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "an engaging narrative opening with a familiar "
                       "closing list"),
    ],
    why=(
        "Catching a group of mendicants fighting and wounding each "
        "other with barbed words right after almsround, the Buddha "
        "does not simply scold them: he teaches the full ten-item "
        "expansion of the warm-hearted qualities already met in "
        "shorter form at AN 6.11 and 6.12, closing both this chapter "
        "and the entire First Fifty of the Tens."),
    guide=[
        ("The teaching in one sentence", [
            "Ten warm-hearted qualities make for fondness, respect, "
            "and harmony without dispute: being ethical, learned, "
            "well-befriended, easy to admonish, deft in duties for "
            "one's companions, a lover of the teaching, energetic, "
            "content, mindful, and wise."]),
        ("A rare narrative catching the Saṅgha in the act", [
            "Unlike most discourses in this chapter, which open with "
            "a question or a bare teaching, this one opens as a "
            "narrative: the Buddha comes out of retreat specifically "
            "to interrupt mendicants who are actively fighting, "
            "quarreling, and wounding each other with barbed words "
            "&mdash; the very disharmony AN 10.37&ndash;41's "
            "definitions of schism and dispute were building toward "
            "all along."]),
        ("The six sāraṇīyā dhammā, expanded to ten", [
            "This discourse's ten qualities are not new: the first "
            "six correspond closely to the six warm-hearted "
            "(<em>sāraṇīya</em>) qualities already taught at AN 6.11 "
            "and AN 6.12 earlier in this project, here joined by four "
            "further qualities &mdash; good friendship, being easy to "
            "admonish, being deft in shared duties, and love of the "
            "teaching &mdash; completing the set of ten."]),
        ("Closing the chapter and the First Fifty together", [
            "The source's own colophon marks this discourse as both "
            "the tenth of Akkosavagga, the fifth chapter, and as the "
            "close of the entire Paṭhamapaṇṇāsaka, the First Fifty of "
            "the Tens &mdash; a double closing, with its own "
            "untranslated uddāna verse naming all ten discourses of "
            "this final chapter."]),
    ],
    terms=[
        ("bhaṇḍanajātā kalahajātā vivādāpannā",
         "&ldquo;fighting, quarreling, and disputing&rdquo; &mdash; "
         "the scene the Buddha interrupts, the very condition AN "
         "10.37&ndash;41 analyzed in the abstract."),
        ("sāraṇīyā dhammā",
         "&ldquo;warm-hearted qualities&rdquo; &mdash; the term "
         "shared with AN 6.11 and 6.12, there naming six such "
         "qualities, here expanded to ten."),
        ("kalyāṇamitto",
         "&ldquo;good friends&rdquo; &mdash; one of the four "
         "qualities added beyond the six already met in AN 6.11 and "
         "6.12."),
        ("suvaco",
         "&ldquo;easy to admonish&rdquo; &mdash; another of the four "
         "newly added qualities, patient and receptive to "
         "correction."),
        ("Paṭhamo paṇṇāsako samatto",
         "&ldquo;the First Fifty is finished&rdquo; &mdash; the "
         "source's own closing declaration, left untranslated in the "
         "English text, marking the halfway point of the entire Book "
         "of the Tens."),
    ],
    text_intro=(
        "The discourse in full: the narrative opening, and the ten "
        "warm-hearted qualities (mostly elided in the source after "
        "the first and last). The chapter's own colophon and uddāna "
        "verse, in Pāli only, are described but not reproduced. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha interrupts a quarrel"),
        ("p", "&sect;1", "an10.50:1.1-3.2"),
        ("h3", "Ten warm-hearted qualities"),
        ("p", "&sect;2", "an10.50:4.1-13.3"),
        ("h3", "Closing"),
        ("p", "&sect;3", "an10.50:14.1"),
    ],
    quiz=[
        {"q": "What does the Buddha find the mendicants doing when he "
              "comes out of retreat?",
         "opts": [
             "Meditating peacefully",
             "Fighting, quarreling, and disputing, wounding each "
             "other with barbed words",
             "Studying the monastic code together",
             "Sleeping"],
         "correct": 1,
         "expl": "A narrative catching the Saṅgha in the very "
                 "disharmony the chapter's earlier discourses "
                 "analyzed abstractly."},
        {"q": "According to the guide, how does this discourse's "
              "ten-item list relate to AN 6.11 and 6.12?",
         "opts": [
             "It is unrelated",
             "Its first six qualities correspond closely to the six "
             "warm-hearted (sāraṇīya) qualities already taught there, "
             "now expanded to ten",
             "It directly contradicts those two discourses",
             "It replaces meditation with ethics entirely"],
         "correct": 1,
         "expl": "The same core teaching, expanded by four further "
                 "qualities."},
        {"q": "Which of these is one of the four newly added "
              "qualities, beyond the original six?",
         "opts": [
             "Being ethical",
             "Being easy to admonish",
             "Being learned",
             "Being wise"],
         "correct": 1,
         "expl": "Good friendship, ease of admonishment, deftness in "
                 "duties, and love of the teaching are the four "
                 "additions."},
        {"q": "What two things does this discourse close, according "
              "to the guide?",
         "opts": [
             "Nothing beyond itself",
             "Both Akkosavagga, the fifth chapter, and the entire "
             "First Fifty (Paṭhamapaṇṇāsaka) of the Book of the Tens",
             "Only the fifth chapter, with the First Fifty ending "
             "later",
             "The entire nipāta"],
         "correct": 1,
         "expl": "A double closing colophon, marking the halfway "
                 "point of AN 10's 211 discourses."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 0,
         "expl": "A specific, named setting, unlike most of this "
                 "chapter's Upāli exchanges."},
        {"q": "What does the discourse's closing colophon leave "
              "untranslated, according to the guide?",
         "opts": [
             "Nothing; everything is translated",
             "The Pāli declaration that the First Fifty is finished, "
             "and the uddāna verse naming all ten discourses of this "
             "chapter",
             "The ten warm-hearted qualities themselves",
             "The narrative opening"],
         "correct": 1,
         "expl": "The same untranslated closing convention used "
                 "throughout this nipāta."},
    ],
    marginalia=[
        ("Caught in the act", [
            "barbed words traded, and",
            "the Buddha rises from",
            "retreat to intervene",
        ]),
        ("Six become ten", [
            "the old warm-hearted",
            "qualities, met once before &mdash;",
            "now four more besides",
        ]),
        ("A double closing", [
            "not just this chapter,",
            "but the First Fifty itself &mdash;",
            "one hundred pages, done",
        ]),
        ("Cross-references", [
            "AN 10.49 &middot; previous, existing because of the "
            "body",
            "AN 6.11 &middot; Warm-hearted (1st), the same qualities "
            "in their original six-item form",
            "AN 10.31 &middot; opening the Upāli-vagga run that this "
            "chapter's schism/dispute material completes",
        ]),
    ],
    further=[
        '<a href="%s/an10.50/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.49.html">AN 10.49 &middot; Existing Because of the Body</a> &mdash; '
        "previous.",
        '<a href="an-6.11.html">AN 6.11 &middot; Warm-hearted (1st)</a> &mdash; the same '
        "qualities, in their original six-item form.",
    ],
)


VAGGA_6 = "<em>Sacittavagga</em> &mdash; the sixth chapter of the Tens, opening the Second Fifty"


# --------------------------------------------------------------------------- #
# AN 10.51 — Sacittasutta
# --------------------------------------------------------------------------- #
page(
    51, "Sacitta", "Your Own Mind",
    vagga=VAGGA_6,
    meta_title="AN 10.51 — Your Own Mind | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sacittasutta, opening the Second Fifty with the famous "
        "mirror simile: a mendicant checking their own mind against "
        "ten qualities, the way one checks a reflection for dirt. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A simile, a ten-part checklist, and a branching "
                 "response"),
        ("Length", "~2 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own name to "
                               "the new chapter, <em>Sacittavagga</em>, "
                               "the Chapter on One's Own Mind, opening "
                               "the Second Fifty of the Tens"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a vivid, memorable simile"),
    ],
    why=(
        "If a mendicant cannot yet read another's mind, the Buddha "
        "says, they should at least master reading their own &mdash; "
        "checking it the way a vain young person checks their "
        "reflection for dirt, against ten paired qualities, and "
        "responding with urgency if anything is found wanting."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant unable to read another's mind should train "
            "to read their own, checking it as one checks a "
            "reflection in a mirror against ten paired qualities "
            "&mdash; covetous or not, malicious or not, dull or not, "
            "restless or not, doubtful or not, irritable or not, "
            "corrupted or not, disturbed or not, lazy or energetic, "
            "unsettled or immersed &mdash; and responding with urgency "
            "if anything is found wanting."]),
        ("A fallback skill, named first", [
            "The discourse opens by naming a harder skill it is not "
            "actually about: reading <em>another's</em> mind "
            "(<em>paracitta</em>). Only a mendicant who lacks that "
            "ability is instructed to fall back on the more accessible "
            "skill this discourse actually teaches &mdash; reading "
            "one's own."]),
        ("The mirror, checked without vanity", [
            "The simile deliberately borrows an image of ordinary "
            "vanity &mdash; a young person fond of adornments checking "
            "a mirror for blemishes &mdash; and repurposes it for "
            "ethical self-examination: the same habitual, unselfconscious "
            "act of checking, redirected from appearance to the state "
            "of one's own mind."]),
        ("Urgency modeled on catching fire", [
            "Should the check turn up any of the five bad qualities, "
            "the response demanded is not measured effort but the "
            "same extraordinary urgency one would apply to "
            "extinguishing a fire on one's own clothes or head &mdash; "
            "one of this canon's most physical images of spiritual "
            "urgency."]),
    ],
    terms=[
        ("sacittapariyāyakusalo",
         "&ldquo;skilled in encompassing one's own mind&rdquo; "
         "&mdash; this discourse's own title and central skill."),
        ("paracittapariyāyakusalo",
         "&ldquo;skilled in encompassing another's mind&rdquo; "
         "&mdash; the harder ability named first, whose absence "
         "triggers this discourse's fallback instruction."),
        ("ādittacelo vā ādittasīso vā",
         "&ldquo;clothes or head were on fire&rdquo; &mdash; the "
         "simile for the urgency demanded when bad qualities are "
         "found."),
        ("abhijjhālu, byāpannacitto, thinamiddhapariyuṭṭhito",
         "&ldquo;covetous, malicious, overcome with dullness and "
         "drowsiness&rdquo; &mdash; the first three of the five "
         "paired qualities checked for."),
        ("kodhano, saṅkiliṭṭhacitto, sāraddhakāyo",
         "&ldquo;irritable, corrupted in mind, disturbed in "
         "body&rdquo; &mdash; three more of the ten paired qualities "
         "checked for."),
    ],
    text_intro=(
        "The discourse in full: the setting, the fallback principle, "
        "and the mirror simile with its ten-part checklist. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Setting, and the fallback principle"),
        ("p", "&sect;1", "an10.51:1.1-2.1"),
        ("h3", "The mirror simile"),
        ("p", "&sect;2", "an10.51:3.1-3.6"),
        ("h3", "Two branching responses"),
        ("p", "&sect;3", "an10.51:4.1-5.2"),
    ],
    quiz=[
        {"q": "What skill does this discourse actually teach?",
         "opts": [
             "Reading another's mind directly",
             "Reading one's own mind, as a fallback for those who "
             "cannot yet read another's",
             "Predicting future events",
             "Interpreting dreams"],
         "correct": 1,
         "expl": "The more accessible of two named skills, taught as "
                 "a fallback."},
        {"q": "What simile does the Buddha use for this "
              "self-checking?",
         "opts": [
             "A ship navigating by the stars",
             "A young person checking their reflection in a mirror "
             "for dirt or blemish",
             "A farmer inspecting crops",
             "A physician diagnosing illness"],
         "correct": 1,
         "expl": "An image of ordinary vanity repurposed for ethical "
                 "self-examination."},
        {"q": "What response does the Buddha demand if the check "
              "finds bad qualities?",
         "opts": [
             "A gradual, unhurried effort over many years",
             "The same extraordinary urgency one would apply to "
             "putting out a fire on one's own clothes or head",
             "No response is needed",
             "Reporting it to a senior mendicant only"],
         "correct": 1,
         "expl": "One of this canon's most physical images of "
                 "spiritual urgency."},
        {"q": "According to the guide, what harder skill is named "
              "first in this discourse, though not actually taught?",
         "opts": [
             "Reading another's mind (paracitta)",
             "Levitation",
             "Predicting the weather",
             "Memorizing scripture instantly"],
         "correct": 0,
         "expl": "This discourse's fallback instruction is triggered "
                 "by lacking that harder ability."},
        {"q": "What does this discourse contribute to its chapter?",
         "opts": [
             "Nothing in particular",
             "Its own subject, giving the new chapter its name, "
             "Sacittavagga, and opening the Second Fifty of the Tens",
             "A place name",
             "A closing colophon"],
         "correct": 1,
         "expl": "As with every chapter-opener in this nipāta, the "
                 "discourse names its own chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 0,
         "expl": "A specific, named setting, opening the new chapter."},
    ],
    marginalia=[
        ("A mirror for the mind", [
            "check your reflection &mdash;",
            "not for dirt on skin, but",
            "covetous or calm",
        ]),
        ("A fallback, named first", [
            "reading minds is hard;",
            "if you can't read another's,",
            "at least read your own",
        ]),
        ("Urgency of fire", [
            "clothes ablaze, head ablaze &mdash;",
            "that same haste applied to",
            "a mind found wanting",
        ]),
        ("Cross-references", [
            "AN 10.50 &middot; previous, closing the First Fifty",
            "AN 10.52 &middot; next, the same teaching from Sāriputta",
        ]),
    ],
    further=[
        '<a href="%s/an10.51/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.50.html">AN 10.50 &middot; Fights</a> &mdash; previous, closing the '
        "First Fifty.",
        '<a href="an-10.52.html">AN 10.52 &middot; With Sāriputta</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.52 — Sāriputtasutta
# --------------------------------------------------------------------------- #
page(
    52, "Sāriputta", "With Sāriputta",
    vagga=VAGGA_6,
    meta_title="AN 10.52 — With Sāriputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Sāriputtasutta, in which Sāriputta teaches the assembly "
        "the identical mirror simile just given by the Buddha in AN "
        "10.51, in his own voice. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Presumably the same as AN 10.51, though no new "
                     "setting is stated"),
        ("Speakers", "Sāriputta, addressing the mendicants directly"),
        ("Form", "The identical simile and checklist from AN 10.51, "
                 "with minor lexical variants"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "familiar ground immediately after AN 10.51"),
    ],
    why=(
        "Where AN 10.51 gave the mirror simile in the Buddha's own "
        "voice, this discourse hands the identical teaching to "
        "Sāriputta, who addresses the mendicants directly, "
        "unprompted &mdash; a twin discourse illustrating a senior "
        "disciple restating the Teacher's own words."),
    guide=[
        ("The teaching in one sentence", [
            "Sāriputta gives the mendicants the same instruction just "
            "heard from the Buddha: a mendicant unable to read "
            "another's mind should check their own, the way one "
            "checks a mirror for blemishes, against the same ten "
            "paired qualities."]),
        ("Nearly word for word, with small variants", [
            "The content is substantially identical to AN 10.51, "
            "down to the fire simile for urgency &mdash; but a few "
            "words shift in translation (&ldquo;irritable&rdquo; "
            "becomes &ldquo;angry&rdquo; in one restatement, "
            "&ldquo;overcome with&rdquo; becomes &ldquo;rid of&rdquo; "
            "in another), the kind of small lexical drift natural to "
            "an independently transmitted repetition rather than a "
            "mechanically copied one."]),
        ("A disciple's voice, not a demotion", [
            "Sāriputta addresses the mendicants as &ldquo;Reverends&rdquo; "
            "rather than the Buddha's &ldquo;Mendicants,&rdquo; and "
            "speaks entirely in his own right, with no indication the "
            "Buddha authorized or was even present for this restatement "
            "&mdash; the teaching's authority rests on Sāriputta's own "
            "standing as chief disciple, not on relayed permission."]),
    ],
    terms=[
        ("āvuso",
         "&ldquo;reverend&rdquo; &mdash; Sāriputta's own form of "
         "address to the mendicants, distinct from the Buddha's "
         "&ldquo;bhikkhave.&rdquo;"),
        ("sacittapariyāyakusalo",
         "&ldquo;skilled in the ways of one's own mind&rdquo; &mdash; "
         "the same central skill as AN 10.51, restated here by "
         "Sāriputta."),
        ("uddhato, vicikiccho",
         "&ldquo;restless, doubtful&rdquo; &mdash; two more of the "
         "ten paired qualities, identical in Pāli to AN 10.51's own "
         "list."),
        ("kusīto, āraddhavīriyo",
         "&ldquo;lazy, energetic&rdquo; &mdash; another pair from the "
         "same identical ten-item list."),
        ("samāhito, asamāhito",
         "&ldquo;immersed in samādhi, not immersed&rdquo; &mdash; the "
         "tenth and final pair, closing the checklist."),
    ],
    text_intro=(
        "The discourse in full, spoken by Sāriputta. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta addresses the assembly"),
        ("p", "&sect;1", "an10.52:1.1-2.1"),
        ("h3", "The mirror simile, restated"),
        ("p", "&sect;2", "an10.52:3.1-4.2"),
        ("h3", "Two branching responses"),
        ("p", "&sect;3", "an10.52:5.1-6.2"),
    ],
    quiz=[
        {"q": "Who teaches in this discourse?",
         "opts": [
             "The Buddha, as in AN 10.51",
             "Sāriputta, addressing the mendicants directly",
             "Ānanda",
             "Upāli"],
         "correct": 1,
         "expl": "A senior disciple restating the Buddha's own recent "
                 "teaching."},
        {"q": "How does this discourse's content compare to AN "
              "10.51's?",
         "opts": [
             "Completely unrelated",
             "Substantially identical, with small lexical variants "
             "natural to an independent retelling",
             "A contradiction of AN 10.51",
             "A much shorter summary"],
         "correct": 1,
         "expl": "The same mirror simile and ten-part checklist, "
                 "nearly word for word."},
        {"q": "What form of address does Sāriputta use for the "
              "mendicants, according to the guide?",
         "opts": [
             "The Buddha's own &ldquo;bhikkhave&rdquo;",
             "&ldquo;Reverends&rdquo; (āvuso), his own distinct form "
             "of address",
             "No address is used",
             "He addresses only Ānanda"],
         "correct": 1,
         "expl": "A small but telling marker of a disciple's own "
                 "voice, not a copied script."},
        {"q": "According to the guide, on what does the authority of "
              "this restatement rest?",
         "opts": [
             "Explicit permission from the Buddha stated in the text",
             "Sāriputta's own standing as chief disciple, with no "
             "indication of relayed permission",
             "A vote among the mendicants",
             "It has no particular authority"],
         "correct": 1,
         "expl": "Sāriputta speaks in his own right."},
    ],
    marginalia=[
        ("The same teaching, twice", [
            "the Buddha spoke it;",
            "now Sāriputta gives it &mdash;",
            "nearly word for word",
        ]),
        ("A disciple's own voice", [
            "&ldquo;Reverends&rdquo; not "
            "&ldquo;Mendicants&rdquo; &mdash;",
            "small signs of someone",
            "speaking in their own right",
        ]),
        ("Identical in Pāli", [
            "the words don't differ &mdash;",
            "only the English's own",
            "small, natural drift",
        ]),
        ("Cross-references", [
            "AN 10.51 &middot; Your Own Mind, the identical teaching "
            "in the Buddha's own voice",
            "AN 10.53 &middot; next, Stagnation",
        ]),
    ],
    further=[
        '<a href="%s/an10.52/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.51.html">AN 10.51 &middot; Your Own Mind</a> &mdash; the identical '
        "teaching, in the Buddha's own voice.",
        '<a href="an-10.53.html">AN 10.53 &middot; Stagnation</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.53 — Ṭhitisutta
# --------------------------------------------------------------------------- #
page(
    53, "Ṭhiti", "Stagnation",
    vagga=VAGGA_6,
    meta_title="AN 10.53 — Stagnation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ṭhitisutta, which distinguishes decline, stagnation, and "
        "growth in five qualities before repeating AN 10.51's mirror "
        "simile in full. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A three-way distinction, then the full mirror "
                 "simile repeated from AN 10.51"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "new material followed by familiar ground"),
    ],
    why=(
        "Before returning to the now-familiar mirror simile, the "
        "Buddha first draws a precise three-way distinction the "
        "chapter has not made before: growth in skillful qualities is "
        "not the same as merely avoiding decline, and stagnation "
        "itself is neither."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant's qualities of faith, ethics, generosity, "
            "wisdom, and eloquence can decline, stagnate, or grow "
            "&mdash; three genuinely distinct conditions, only the "
            "third of which the Buddha praises &mdash; and the same "
            "mendicant should still check their own mind by the "
            "mirror simile already given."]),
        ("A three-way distinction, not a simple pair", [
            "Where much of this project's material contrasts only two "
            "states (skillful/unskillful, decline/growth), this "
            "discourse insists on a middle term: qualities that "
            "neither decline nor grow are not automatically praised "
            "for avoiding decline &mdash; stagnation gets its own "
            "name and its own, distinctly unenthusiastic, treatment."]),
        ("The mirror simile, folded in whole", [
            "After establishing this distinction, the discourse pivots "
            "directly into AN 10.51's mirror simile, reproduced here "
            "essentially in full &mdash; the two teachings are joined "
            "rather than merely juxtaposed, as if stagnation-avoidance "
            "is itself one more thing the self-check should catch."]),
    ],
    terms=[
        ("saddhā, sīla, cāga, paññā, paṭibhāna",
         "faith, ethics, generosity, wisdom, and eloquence &mdash; "
         "the five qualities whose decline, stagnation, or growth "
         "this discourse examines."),
        ("hāni, ṭhiti, vuddhi",
         "&ldquo;decline, stagnation, growth&rdquo; &mdash; the "
         "three-way distinction giving this discourse its title, "
         "<em>ṭhiti</em>."),
        ("neva tiṭṭhanti no vaḍḍhanti",
         "&ldquo;those qualities neither stagnate nor grow&rdquo; "
         "&mdash; the phrasing defining decline, one of the three "
         "conditions this discourse distinguishes."),
        ("bahulaṁ viharāmi",
         "&ldquo;I often abide&rdquo; &mdash; the recurring "
         "self-questioning frame of the mirror-simile checklist, "
         "repeated here from AN 10.51 and 10.52."),
        ("adhimatto chando",
         "&ldquo;extraordinary enthusiasm&rdquo; &mdash; the urgency "
         "demanded once the fire simile is invoked, repeated "
         "unchanged from AN 10.51."),
    ],
    text_intro=(
        "The discourse in full: the three-way distinction, followed "
        "by the mirror simile repeated from AN 10.51. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Decline, stagnation, and growth"),
        ("p", "&sect;1", "an10.53:1.1-4.4"),
        ("h3", "The mirror simile, repeated"),
        ("p", "&sect;2", "an10.53:5.1-8.2"),
    ],
    quiz=[
        {"q": "What three-way distinction does this discourse draw?",
         "opts": [
             "Good, bad, and neutral deeds",
             "Decline, stagnation, and growth in five qualities "
             "&mdash; three genuinely distinct conditions",
             "Past, present, and future",
             "Body, speech, and mind"],
         "correct": 1,
         "expl": "A middle term, stagnation, distinct from both "
                 "decline and growth."},
        {"q": "Which five qualities does this distinction apply to?",
         "opts": [
             "The five aggregates",
             "Faith, ethics, generosity, wisdom, and eloquence",
             "The five precepts",
             "The five hindrances"],
         "correct": 1,
         "expl": "A set not identical to any prior five-item list in "
                 "this project."},
        {"q": "How does this discourse relate to AN 10.51, according "
              "to the guide?",
         "opts": [
             "It contradicts AN 10.51 entirely",
             "After the new three-way distinction, it pivots directly "
             "into AN 10.51's mirror simile, reproduced essentially "
             "in full",
             "It has no relation to AN 10.51",
             "It replaces the mirror simile with a new one"],
         "correct": 1,
         "expl": "Two teachings joined into one discourse, not merely "
                 "placed side by side."},
        {"q": "Which condition does the Buddha praise, according to "
              "this discourse?",
         "opts": [
             "Decline",
             "Stagnation, for avoiding decline",
             "Growth alone",
             "All three equally"],
         "correct": 2,
         "expl": "Growth is praised; the Buddha explicitly states he "
                 "does not praise mere stagnation, let alone decline."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("Not just two states", [
            "decline, growth &mdash; and a",
            "third: standing still, praised",
            "by no one, least of all",
        ]),
        ("Two teachings, joined", [
            "a new distinction,",
            "then the mirror simile &mdash;",
            "folded into one",
        ]),
        ("A familiar refrain returns", [
            "the same ten paired checks,",
            "the same fire simile &mdash;",
            "now with new framing",
        ]),
        ("Cross-references", [
            "AN 10.52 &middot; previous, with Sāriputta",
            "AN 10.51 &middot; Your Own Mind, whose mirror simile "
            "this discourse repeats in full",
            "AN 10.54 &middot; next, Serenity",
        ]),
    ],
    further=[
        '<a href="%s/an10.53/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.52.html">AN 10.52 &middot; With Sāriputta</a> &mdash; previous.',
        '<a href="an-10.51.html">AN 10.51 &middot; Your Own Mind</a> &mdash; whose mirror '
        "simile this discourse repeats in full.",
        '<a href="an-10.54.html">AN 10.54 &middot; Serenity</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.54 — Samathasutta
# --------------------------------------------------------------------------- #
page(
    54, "Samatha", "Serenity",
    vagga=VAGGA_6,
    meta_title="AN 10.54 — Serenity | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Samathasutta, which narrows the mirror simile to a "
        "two-item serenity/discernment check, then pivots to a "
        "separate teaching on which robes, food, and company to "
        "adopt or avoid. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A narrowed two-item mirror check, then a distinct "
                 "six-category teaching in question-and-answer form"),
        ("Length", "~3 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "two teachings in one discourse"),
    ],
    why=(
        "This discourse narrows the mirror simile from ten items down "
        "to just two &mdash; serenity and discernment &mdash; before "
        "pivoting to something else entirely: a practical teaching, "
        "in the Buddha's own question-and-answer style, on which "
        "robes, food, lodging, places, and people to adopt or avoid."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant should check whether they have serenity of "
            "heart and discernment of principles, developing whichever "
            "is missing until both are present, then continue "
            "meditating to end the defilements &mdash; and should "
            "judge every robe, food, lodging, town, region, and "
            "companion by a single test: does it grow unskillful "
            "qualities or skillful ones?"]),
        ("A checklist narrowed to its essentials", [
            "Where AN 10.51&ndash;53 used a ten-item checklist, this "
            "discourse compresses the same self-checking structure "
            "down to the two most fundamental qualities of "
            "meditation practice: <em>samatha</em> (serenity) and "
            "<em>vipassanā</em>-adjacent <em>adhipaññādhammavipassanā</em> "
            "(discernment) &mdash; with four branching cases (neither, "
            "one only, the other only, both) rather than the ten-item "
            "version's two."]),
        ("A second, unrelated teaching, joined at the seam", [
            "After the serenity/discernment teaching concludes, the "
            "discourse continues with no narrative transition into a "
            "structurally separate teaching: six pairs of things "
            "(robes, almsfood, lodging, village or town, country, "
            "individual) that should be adopted or avoided based on a "
            "single practical test, each explained in the Buddha's "
            "own distinctive &ldquo;that's what I said, and this is "
            "why I said it&rdquo; self-questioning format."]),
        ("One test applied six times", [
            "Despite covering six very different categories, the test "
            "itself never changes: does using this robe, eating this "
            "food, or keeping this company cause unskillful qualities "
            "to grow and skillful ones to decline, or the reverse? "
            "The same question, asked six times over, turns an "
            "abstract ethical principle into a concrete decision "
            "procedure for daily monastic life."]),
    ],
    terms=[
        ("cetosamatha",
         "&ldquo;serenity of heart&rdquo; &mdash; the first of the "
         "two qualities checked, giving this discourse its title."),
        ("adhipaññādhammavipassanā",
         "&ldquo;the higher wisdom of discernment of principles&rdquo; "
         "&mdash; the second quality checked, paired with serenity."),
        ("iti kho panetaṁ vuttaṁ, kiñcetaṁ paṭicca vuttaṁ",
         "&ldquo;that's what I said, but why did I say it?&rdquo; "
         "&mdash; the Buddha's own recurring self-questioning formula "
         "structuring the six-part second teaching."),
        ("lābhī, na lābhī",
         "&ldquo;a gainer, not a gainer&rdquo; &mdash; the binary at "
         "the heart of the narrowed two-item check, applied "
         "separately to serenity and to discernment."),
        ("cīvara, piṇḍapāta, senāsana",
         "&ldquo;robes, almsfood, lodging&rdquo; &mdash; the first "
         "three of six categories judged by the same single test in "
         "this discourse's second half."),
    ],
    text_intro=(
        "The discourse in full: the serenity/discernment check, then "
        "the six-part teaching on what to adopt or avoid. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The mirror simile, narrowed to two qualities"),
        ("p", "&sect;1", "an10.54:1.1-6.2"),
        ("h3", "Six things to adopt or avoid, stated"),
        ("p", "&sect;2", "an10.54:7.1-7.12"),
        ("h3", "Robes and almsfood, explained"),
        ("p", "&sect;3", "an10.54:8.1-9.10"),
        ("h3", "Lodging, places, and company, explained"),
        ("p", "&sect;4", "an10.54:10.1-13.10"),
    ],
    quiz=[
        {"q": "How does this discourse's mirror-simile check differ "
              "from AN 10.51's?",
         "opts": [
             "It is identical, with ten items",
             "It narrows the check to just two qualities: serenity "
             "and discernment",
             "It expands the check to twenty items",
             "It removes the mirror simile entirely"],
         "correct": 1,
         "expl": "A compressed version of the same self-checking "
                 "structure."},
        {"q": "What does the discourse turn to after the serenity/"
              "discernment teaching concludes, according to the "
              "guide?",
         "opts": [
             "Nothing; the discourse ends there",
             "A structurally separate teaching on six pairs of things "
             "&mdash; robes, food, lodging, and more &mdash; to adopt "
             "or avoid",
             "A narrative about Sāriputta",
             "A closing verse"],
         "correct": 1,
         "expl": "Two distinct teachings joined into a single "
                 "discourse."},
        {"q": "What single test determines whether to adopt or avoid "
              "each of the six things?",
         "opts": [
             "Whether it is expensive",
             "Whether it causes unskillful qualities to grow and "
             "skillful ones to decline, or the reverse",
             "Whether a senior mendicant approves",
             "Whether it is popular among laypeople"],
         "correct": 1,
         "expl": "The same practical test applied six times, to six "
                 "different categories."},
        {"q": "What is the Buddha's recurring formula structuring the "
              "second half of this discourse?",
         "opts": [
             "A closing verse repeated six times",
             "&ldquo;That's what I said, but why did I say it?&rdquo; "
             "&mdash; followed by his own explanation",
             "A question from Ānanda each time",
             "No formula; it is a bare list"],
         "correct": 1,
         "expl": "A self-questioning device repeated for each of the "
                 "six categories."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("Two, not ten", [
            "serenity, discernment &mdash;",
            "the whole checklist boiled",
            "down to its two roots",
        ]),
        ("One test, six times", [
            "robe, food, lodging, place,",
            "country, company &mdash; each judged",
            "by the same question",
        ]),
        ("A seam without a scene", [
            "no story marks where",
            "one teaching ends and the next",
            "begins &mdash; just the seam",
        ]),
        ("Cross-references", [
            "AN 10.53 &middot; previous, Stagnation",
            "AN 10.51 &middot; Your Own Mind, the ten-item version of "
            "this discourse's narrowed check",
            "AN 10.55 &middot; next, Decline",
        ]),
    ],
    further=[
        '<a href="%s/an10.54/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.53.html">AN 10.53 &middot; Stagnation</a> &mdash; previous.',
        '<a href="an-10.55.html">AN 10.55 &middot; Decline</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.55 — Parihānasutta
# --------------------------------------------------------------------------- #
page(
    55, "Parihāna", "Decline",
    vagga=VAGGA_6,
    meta_title="AN 10.55 — Decline | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Parihānasutta, in which Sāriputta first defines the "
        "individual liable to decline, then gives a positive-only "
        "variant of the mirror simile with a three-tier response. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Sāriputta, teaching at the mendicants' request"),
        ("Form", "A four-part definition, requested and given, then "
                 "a positive-only mirror check with a three-tier "
                 "response"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "two related but distinct teachings"),
    ],
    why=(
        "Sāriputta returns, this time explicitly invited to speak "
        "after raising a question the mendicants themselves ask him "
        "to answer: what defines an individual liable to decline? "
        "His answer then flows into yet another variant of the "
        "mirror simile, this one checking only for the presence of "
        "good qualities."),
    guide=[
        ("The teaching in one sentence", [
            "An individual liable to decline fails to hear new "
            "teachings, forgets what they've heard, neglects familiar "
            "teachings, and fails to understand what was unclear; one "
            "not liable to decline does the opposite &mdash; and every "
            "mendicant should further check their own mind for ten "
            "positive qualities, responding according to how many are "
            "found."]),
        ("A formally requested teaching", [
            "Unlike Sāriputta's unprompted address in AN 10.52, this "
            "discourse opens with the mendicants explicitly asking him "
            "to clarify a question about the Buddha's own teaching "
            "&mdash; a small but real difference in how the same "
            "disciple's authority to speak is established from one "
            "discourse to the next."]),
        ("A third variant of the checklist", [
            "This discourse's mirror-simile check differs from both "
            "AN 10.51's ten paired items and AN 10.54's two items: it "
            "lists ten purely positive qualities (contentment, "
            "kind-heartedness, freedom from dullness, calm, "
            "confidence, love, purity of mind, joy in the teaching, "
            "serenity, and discernment) and asks only whether each is "
            "present, not paired against its negative."]),
        ("A three-tier response, not two", [
            "Where AN 10.51's check branches into two responses "
            "(found wanting, or grounded and ready to continue), this "
            "version adds a middle case: a mendicant may see none of "
            "the ten qualities, some of them, or all of them, with a "
            "distinct instruction for each &mdash; the most granular "
            "version of this recurring self-check structure so far."]),
    ],
    terms=[
        ("parihānadhamma",
         "&ldquo;liable to decline&rdquo; &mdash; this discourse's "
         "own title, the individual type defined in its opening "
         "section."),
        ("assutaṁ dhammaṁ na suṇāti",
         "&ldquo;doesn't get to hear a teaching they haven't heard "
         "before&rdquo; &mdash; the first of four marks of decline."),
        ("dhammapāmojja",
         "&ldquo;joy with the teaching&rdquo; &mdash; a quality "
         "appearing in this discourse's checklist that did not "
         "appear in AN 10.51's."),
        ("sutā cassa dhammā sammosaṁ gacchanti",
         "&ldquo;they forget those teachings they have heard&rdquo; "
         "&mdash; the second of the four marks of decline."),
        ("santuṭṭho, mettacitto",
         "&ldquo;contentment, loving&rdquo; &mdash; two of the ten "
         "positive qualities in this discourse's own variant "
         "checklist."),
    ],
    text_intro=(
        "The discourse in full: the mendicants' request, Sāriputta's "
        "definition of decline, and the positive-only mirror check. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A question, requested and answered"),
        ("p", "&sect;1", "an10.55:1.1-3.3"),
        ("h3", "Liable to decline, and not liable to decline"),
        ("p", "&sect;2", "an10.55:4.1-5.3"),
        ("h3", "The mirror simile, ten positive qualities"),
        ("p", "&sect;3", "an10.55:6.1-7.6"),
        ("h3", "Three branching responses"),
        ("p", "&sect;4", "an10.55:8.1-10.1"),
    ],
    quiz=[
        {"q": "How does this discourse's opening differ from AN "
              "10.52's, according to the guide?",
         "opts": [
             "There is no difference",
             "Here the mendicants explicitly ask Sāriputta to "
             "clarify a question, rather than his speaking "
             "unprompted",
             "The Buddha personally introduces Sāriputta",
             "Sāriputta refuses to answer"],
         "correct": 1,
         "expl": "A formally requested teaching, distinct from AN "
                 "10.52's unprompted address."},
        {"q": "What four marks define an individual liable to "
              "decline?",
         "opts": [
             "Poverty, illness, old age, and low birth",
             "Not hearing new teachings, forgetting what's heard, "
             "neglecting familiar teachings, and failing to "
             "understand what was unclear",
             "Breaking the five precepts",
             "Lacking a teacher"],
         "correct": 1,
         "expl": "A definition centered entirely on engagement with "
                 "the teaching."},
        {"q": "How does this discourse's mirror-simile checklist "
              "differ from AN 10.51's, according to the guide?",
         "opts": [
             "It is identical",
             "It lists ten purely positive qualities, asking only "
             "whether each is present, rather than paired positive/"
             "negative items",
             "It has only two items, like AN 10.54",
             "It removes the mirror simile entirely"],
         "correct": 1,
         "expl": "A third distinct variant of the recurring checklist "
                 "structure."},
        {"q": "How many response tiers does this version of the "
              "check offer, compared to AN 10.51's two?",
         "opts": [
             "Still two",
             "Three: seeing none, some, or all of the ten qualities",
             "Five",
             "Ten separate responses"],
         "correct": 1,
         "expl": "A more granular branching structure than the "
                 "earlier versions."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("Asked, not offered", [
            "the mendicants ask;",
            "Sāriputta answers &mdash;",
            "invited, not unprompted",
        ]),
        ("Ten qualities, positive only", [
            "not paired against their",
            "opposites this time &mdash; just",
            "present, or absent",
        ]),
        ("None, some, or all", [
            "a third response joins",
            "the earlier two &mdash; the most",
            "granular check yet",
        ]),
        ("Cross-references", [
            "AN 10.54 &middot; previous, Serenity",
            "AN 10.52 &middot; With Sāriputta, the earlier, unprompted "
            "version of this same disciple teaching the assembly",
            "AN 10.56 &middot; next, Perceptions (1st)",
        ]),
    ],
    further=[
        '<a href="%s/an10.55/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.54.html">AN 10.54 &middot; Serenity</a> &mdash; previous.',
        '<a href="an-10.56.html">AN 10.56 &middot; Perceptions (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.56 — Paṭhamasaññāsutta
# --------------------------------------------------------------------------- #
page(
    56, "Paṭhamasaññā", "Perceptions (1st)",
    vagga=VAGGA_6,
    meta_title="AN 10.56 — Perceptions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamasaññāsutta, a bare list of ten perceptions "
        "leading to freedom from death, opening this chapter's turn "
        "from mind-checking to formal meditation objects. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A single flat list of ten, with no elaboration"),
        ("Length", "under 1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and unelaborated"),
    ],
    why=(
        "After five discourses built around checking one's own mind, "
        "the chapter pivots to something more structural: the first "
        "of three related lists of ten <em>perceptions</em> "
        "&mdash; formal meditation objects &mdash; that this chapter "
        "will offer in escalating variation, all aimed at the same "
        "goal, freedom from death."),
    guide=[
        ("The teaching in one sentence", [
            "Ten perceptions, developed and cultivated, are very "
            "fruitful and lead to freedom from death: the perceptions "
            "of ugliness, death, repulsiveness of food, dissatisfaction "
            "with the whole world, impermanence, suffering in "
            "impermanence, not-self in suffering, giving up, fading "
            "away, and cessation."]),
        ("A shift from checking to cultivating", [
            "AN 10.51&ndash;55 all concerned checking the state of "
            "one's own mind against a standard; this discourse turns "
            "instead to naming ten specific objects of formal "
            "contemplation to be actively developed, the first of a "
            "small cluster of such lists running through the rest of "
            "this chapter."]),
        ("A logical chain within the list", [
            "The final four items of the ten follow their own "
            "internal logic rather than standing independently: "
            "impermanence leads to seeing suffering within "
            "impermanence, which leads to seeing not-self within that "
            "suffering, which in turn grounds giving up, fading away, "
            "and cessation &mdash; a compressed doctrinal chain "
            "embedded inside a bare list."]),
        ("The first of three related lists", [
            "This exact list will be varied twice more before the "
            "chapter closes: AN 10.57 keeps five of these ten items "
            "but replaces the rest with five distinct charnel-ground "
            "contemplations, and the chapter's final discourse "
            "(spliced in from an earlier page) gives the tradition's "
            "single most famous version of a ten-perception list."]),
    ],
    terms=[
        ("saññā",
         "&ldquo;perception&rdquo; &mdash; a formal object of "
         "meditative attention, this discourse's own subject."),
        ("asubhasaññā, maraṇasaññā",
         "&ldquo;the perception of ugliness, the perception of "
         "death&rdquo; &mdash; the first two items on this list."),
        ("amata",
         "&ldquo;freedom from death,&rdquo; the deathless &mdash; "
         "the stated objective and culmination shared by all three "
         "of this chapter's perception-lists."),
        ("āhāre paṭikūlasaññā",
         "&ldquo;the perception of the repulsiveness of food&rdquo; "
         "&mdash; the third item on this list, shared with AN "
         "10.57."),
        ("pahānasaññā, virāgasaññā, nirodhasaññā",
         "&ldquo;giving up, fading away, cessation&rdquo; &mdash; the "
         "final three items, closing the list's internal doctrinal "
         "chain."),
    ],
    text_intro=(
        "The discourse in full: the ten perceptions, listed without "
        "elaboration. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Ten perceptions"),
        ("p", "&sect;1", "an10.56:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this discourse list?",
         "opts": [
             "Ten monastic offenses",
             "Ten perceptions that, developed and cultivated, lead to "
             "freedom from death",
             "Ten qualities of a good teacher",
             "Ten grounds for suspending recitation"],
         "correct": 1,
         "expl": "A formal list of meditation objects, not a checklist "
                 "of mind-states."},
        {"q": "How does this discourse mark a shift from the chapter's "
              "earlier discourses, according to the guide?",
         "opts": [
             "It does not mark any shift",
             "It moves from checking the state of one's own mind to "
             "naming objects of formal contemplation to actively "
             "develop",
             "It abandons meditation entirely",
             "It returns to monastic law"],
         "correct": 1,
         "expl": "A pivot from self-checking to cultivation."},
        {"q": "According to the guide, what internal logic structures "
              "the final four items of this list?",
         "opts": [
             "No logic; they are unrelated",
             "Impermanence leads to seeing suffering within it, which "
             "leads to not-self, which grounds giving up, fading "
             "away, and cessation",
             "They are ordered alphabetically",
             "They repeat the first four items"],
         "correct": 1,
         "expl": "A compressed doctrinal chain embedded inside the "
                 "bare list."},
        {"q": "What does the guide say happens to this list in the "
              "rest of the chapter?",
         "opts": [
             "It never appears again",
             "It is varied twice more, including the tradition's most "
             "famous version of a ten-perception list at the "
             "chapter's close",
             "It is immediately contradicted",
             "It is expanded to twenty items"],
         "correct": 1,
         "expl": "The first of three related lists running through "
                 "this chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this brief discourse."},
    ],
    marginalia=[
        ("Ten objects, bare", [
            "ugliness, death, food's",
            "repulsion &mdash; and further still,",
            "impermanence, self",
        ]),
        ("From checking to building", [
            "no more mirror now &mdash;",
            "these are objects to develop,",
            "not states to detect",
        ]),
        ("A chain within the list", [
            "impermanence to",
            "suffering to not-self &mdash;",
            "then letting go, three times",
        ]),
        ("Cross-references", [
            "AN 10.55 &middot; previous, Decline",
            "AN 10.57 &middot; next, a second, partly different "
            "ten-perception list",
        ]),
    ],
    further=[
        '<a href="%s/an10.56/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.55.html">AN 10.55 &middot; Decline</a> &mdash; previous.',
        '<a href="an-10.57.html">AN 10.57 &middot; Perceptions (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.57 — Dutiyasaññāsutta
# --------------------------------------------------------------------------- #
page(
    57, "Dutiyasaññā", "Perceptions (2nd)",
    vagga=VAGGA_6,
    meta_title="AN 10.57 — Perceptions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasaññāsutta, which keeps half of AN 10.56's list "
        "but replaces the rest with five visceral charnel-ground "
        "corpse contemplations. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A single flat list of ten, with no elaboration"),
        ("Length", "under 1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, though vivid in content"),
    ],
    why=(
        "This second list of ten perceptions keeps five items from AN "
        "10.56 but drops the doctrinal chain entirely, replacing it "
        "with five specific, visceral stages of a decomposing corpse "
        "&mdash; among the most graphic content in this project so "
        "far."),
    guide=[
        ("The teaching in one sentence", [
            "A second set of ten perceptions, equally fruitful and "
            "aimed at the same freedom from death: impermanence, "
            "not-self, death, repulsiveness of food, dissatisfaction "
            "with the whole world, and five successive charnel-ground "
            "images &mdash; a skeleton, a worm-infested corpse, a "
            "livid corpse, a split-open corpse, and a bloated "
            "corpse."]),
        ("Five items shared, five replaced", [
            "This list keeps five of AN 10.56's ten items outright "
            "(impermanence, not-self, death, food's repulsiveness, "
            "and dissatisfaction with the world, though reordered), "
            "but drops that discourse's closing doctrinal chain "
            "&mdash; suffering-in-impermanence, not-self-in-suffering, "
            "giving up, fading away, cessation &mdash; entirely."]),
        ("The charnel ground, made concrete", [
            "In place of that abstract chain, this discourse names "
            "five specific stages of bodily decomposition in sequence "
            "&mdash; a traditional set of corpse contemplations "
            "practiced by observing an actual decaying body at "
            "different intervals, here compressed into a bare list "
            "with no narrative or simile to soften them."]),
        ("Same goal, sharper method", [
            "Despite the stark difference in content, this list "
            "closes with the identical formula as AN 10.56: developed "
            "and cultivated, these perceptions too have freedom from "
            "death as their objective and culmination &mdash; two very "
            "different routes to the same destination."]),
    ],
    terms=[
        ("aṭṭhikasaññā",
         "&ldquo;the perception of a skeleton&rdquo; &mdash; the "
         "first of the five charnel-ground images unique to this "
         "list."),
        ("puḷavakasaññā",
         "&ldquo;the perception of a worm-infested corpse&rdquo; "
         "&mdash; the second charnel-ground image."),
        ("uddhumātakasaññā",
         "&ldquo;the perception of a bloated corpse&rdquo; &mdash; "
         "the fifth and final charnel-ground image, closing the "
         "list."),
        ("vinīlakasaññā",
         "&ldquo;the perception of a livid corpse&rdquo; &mdash; the "
         "third of the five charnel-ground images."),
        ("vicchiddakasaññā",
         "&ldquo;the perception of a split-open corpse&rdquo; "
         "&mdash; the fourth charnel-ground image."),
    ],
    text_intro=(
        "The discourse in full: the ten perceptions, listed without "
        "elaboration. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Ten perceptions, a second list"),
        ("p", "&sect;1", "an10.57:1.1-1.4"),
    ],
    quiz=[
        {"q": "How many items does this list share with AN 10.56's?",
         "opts": [
             "None",
             "Five, though reordered: impermanence, not-self, death, "
             "food's repulsiveness, and dissatisfaction with the "
             "world",
             "All ten",
             "Nine"],
         "correct": 1,
         "expl": "Half the list overlaps; the other half is entirely "
                 "new."},
        {"q": "What replaces AN 10.56's closing doctrinal chain in "
              "this discourse?",
         "opts": [
             "A closing verse",
             "Five successive charnel-ground images of a decomposing "
             "corpse",
             "A repeat of the same five items",
             "Nothing; the list is shorter"],
         "correct": 1,
         "expl": "Concrete bodily imagery in place of an abstract "
                 "logical sequence."},
        {"q": "What kind of practice do the five new items reflect, "
              "according to the guide?",
         "opts": [
             "Walking meditation",
             "Traditional corpse contemplations, observing a "
             "decaying body at successive stages",
             "Breath meditation",
             "Loving-kindness meditation"],
         "correct": 1,
         "expl": "A traditional, visceral meditation method distinct "
                 "from AN 10.56's abstract chain."},
        {"q": "Despite the different content, how does this list "
              "close?",
         "opts": [
             "With a completely different goal",
             "With the identical formula as AN 10.56: freedom from "
             "death as the objective and culmination",
             "Without any closing statement",
             "By contradicting AN 10.56's stated goal"],
         "correct": 1,
         "expl": "Two different routes, the guide notes, to the same "
                 "destination."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this brief discourse."},
    ],
    marginalia=[
        ("Half kept, half new", [
            "impermanence stays;",
            "the chain of insight gives way",
            "to a decaying corpse",
        ]),
        ("Five stages, in sequence", [
            "skeleton, worm-eaten,",
            "livid, split open, bloated &mdash;",
            "watched without flinching",
        ]),
        ("Two routes, one destination", [
            "abstract chain, or corpse",
            "watched stage by stage &mdash; both lead",
            "past death, the text says",
        ]),
        ("Cross-references", [
            "AN 10.56 &middot; Perceptions (1st), sharing half this "
            "list's items",
            "AN 10.58 &middot; next, Rooted",
        ]),
    ],
    further=[
        '<a href="%s/an10.57/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.56.html">AN 10.56 &middot; Perceptions (1st)</a> &mdash; previous.',
        '<a href="an-10.58.html">AN 10.58 &middot; Rooted</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.58 — Mūlakasutta
# --------------------------------------------------------------------------- #
page(
    58, "Mūlaka", "Rooted",
    vagga=VAGGA_6,
    meta_title="AN 10.58 — Rooted | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Mūlakasutta, a rehearsed ten-part answer for when "
        "wanderers of other religions ask what roots, produces, and "
        "culminates all things &mdash; echoing this nipāta's opening "
        "chain at AN 10.1. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, rehearsing an answer with the "
                     "mendicants"),
        ("Form", "A hypothetical challenge, a request for guidance, "
                 "and a ten-part scripted answer"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "abstract but tightly patterned"),
    ],
    why=(
        "The Buddha poses a hypothetical: what would the mendicants "
        "say if wanderers of other religions asked them to name the "
        "root, source, and culmination of all things? When the "
        "mendicants defer to him, he supplies a rehearsed, ten-part "
        "answer for them to use."),
    guide=[
        ("The teaching in one sentence", [
            "All things are rooted in desire, produced by application "
            "of mind, originate in contact, meet in feeling, are "
            "chiefly led by immersion, ruled by mindfulness, overseen "
            "by wisdom, cored in freedom, aimed at freedom from death, "
            "and culminate in extinguishment &mdash; a scripted answer "
            "for mendicants challenged by outsiders."]),
        ("Rehearsal, not spontaneous teaching", [
            "Unusually, this discourse is explicitly a training "
            "exercise: the Buddha poses the outsiders' hypothetical "
            "question first, waits for the mendicants to admit they "
            "cannot yet answer it and ask him directly, and only then "
            "supplies the ten-part response &mdash; equipping them "
            "for a future encounter rather than addressing one already "
            "underway."]),
        ("A ten-link chain, echoing the chapter's very first page", [
            "This ten-part answer to &ldquo;what roots, produces, and "
            "culminates all things&rdquo; structurally echoes AN "
            "10.1's opening ten-link chain from ethics to the "
            "knowledge and vision of freedom, closing this nipāta's "
            "loop back to where the Book of the Tens itself began "
            "&mdash; both are progressive ten-step sequences ending in "
            "freedom, though built from entirely different material."]),
        ("Ten questions, ten distinct answers", [
            "Rather than a flat list, the ten items answer ten "
            "grammatically distinct questions posed by the "
            "hypothetical outsiders &mdash; root, producer, origin, "
            "meeting place, chief, ruler, overseer, core, objective, "
            "and culmination &mdash; each mapped to a different "
            "element of practice, from raw desire through to final "
            "extinguishment."]),
    ],
    terms=[
        ("chandamūlakā sabbe dhammā",
         "&ldquo;all things are rooted in desire&rdquo; &mdash; the "
         "first of the ten answers, and the discourse's own title, "
         "<em>mūlaka</em>, &ldquo;rooted.&rdquo;"),
        ("manasikārasambhavā",
         "&ldquo;produced by application of mind&rdquo; &mdash; the "
         "second answer, on what brings all things into being."),
        ("vimuttisārā",
         "&ldquo;freedom is their core&rdquo; &mdash; the eighth "
         "answer, naming what lies at the center of all things."),
        ("nibbānapariyosānā",
         "&ldquo;extinguishment is their culmination&rdquo; &mdash; "
         "the tenth and final answer, closing the chain."),
        ("phassasamudayā, vedanāsamosaraṇā",
         "&ldquo;contact is their origin, feeling is their meeting "
         "place&rdquo; &mdash; the third and fourth answers in the "
         "ten-part chain."),
    ],
    text_intro=(
        "The discourse in full: the hypothetical challenge, the "
        "mendicants' request, and the Buddha's ten-part answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A hypothetical challenge from outsiders"),
        ("p", "&sect;1", "an10.58:1.1-2.3"),
        ("h3", "The ten-part answer"),
        ("p", "&sect;2", "an10.58:3.1-3.5"),
    ],
    quiz=[
        {"q": "What hypothetical situation does the Buddha pose to "
              "the mendicants?",
         "opts": [
             "A dispute within the Saṅgha",
             "Wanderers of other religions asking what roots, "
             "produces, and culminates all things",
             "A king questioning the mendicants",
             "A dying mendicant's final question"],
         "correct": 1,
         "expl": "A rehearsal for a possible future encounter with "
                 "outsiders."},
        {"q": "What is unusual about how this discourse proceeds, "
              "according to the guide?",
         "opts": [
             "Nothing; it is a typical teaching",
             "It is explicitly a training exercise: the mendicants "
             "admit they cannot answer, then ask the Buddha to supply "
             "the response for future use",
             "The Buddha refuses to answer",
             "It is answered entirely by Sāriputta"],
         "correct": 1,
         "expl": "Equipping the mendicants for a hypothetical future "
                 "situation, not addressing a present one."},
        {"q": "According to the guide, what earlier discourse does "
              "this ten-part chain structurally echo?",
         "opts": [
             "AN 10.50, closing the First Fifty",
             "AN 10.1, this nipāta's own opening ten-link chain",
             "AN 9.1",
             "It echoes no earlier discourse"],
         "correct": 1,
         "expl": "Both are progressive ten-step sequences ending in "
                 "freedom, closing a structural loop within AN 10."},
        {"q": "What is named as the culmination of all things in this "
              "discourse's answer?",
         "opts": [
             "Wisdom", "Extinguishment (nibbāna)",
             "Mindfulness", "Desire"],
         "correct": 1,
         "expl": "The tenth and final term in the chain."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("A scripted answer", [
            "not spontaneous now &mdash;",
            "the Buddha drills a reply",
            "for a future test",
        ]),
        ("Ten questions, ten terms", [
            "root, producer, meeting",
            "place, ruler, core, culmination &mdash;",
            "each mapped in turn",
        ]),
        ("The chapter's loop, closed", [
            "AN 10.1's",
            "own ten-link chain, echoed here &mdash;",
            "the book folds back",
        ]),
        ("Cross-references", [
            "AN 10.57 &middot; previous, Perceptions (2nd)",
            "AN 10.1 &middot; What's the Goal?, this nipāta's own "
            "opening ten-link chain, echoed structurally here",
            "AN 10.59 &middot; next, Going Forth",
        ]),
    ],
    further=[
        '<a href="%s/an10.58/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.57.html">AN 10.57 &middot; Perceptions (2nd)</a> &mdash; previous.',
        '<a href="an-10.1.html">AN 10.1 &middot; What&rsquo;s the Goal?</a> &mdash; this '
        "nipāta's own opening ten-link chain, echoed structurally here.",
        '<a href="an-10.59.html">AN 10.59 &middot; Going Forth</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.59 — Pabbajjāsutta
# --------------------------------------------------------------------------- #
page(
    59, "Pabbajjā", "Going Forth",
    vagga=VAGGA_6,
    meta_title="AN 10.59 — Going Forth | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Pabbajjāsutta, closing the Sacittavagga with a third "
        "variant ten-perception training formula, guaranteeing "
        "enlightenment or non-return. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A single training formula, then its guaranteed "
                 "result"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "dense but tightly parallel in structure"),
    ],
    why=(
        "Closing this chapter's own discourses, the Buddha gives a "
        "third variant of the ten-perception formula, this one framed "
        "explicitly as a training to be undertaken and named for the "
        "very moment of ordination, with an unusually direct "
        "guarantee attached to its success."),
    guide=[
        ("The teaching in one sentence", [
            "Mendicants should train so their minds stay as "
            "consolidated as they were at the moment of going forth, "
            "never overrun by unskillful qualities, and consolidated "
            "in ten perceptions &mdash; impermanence, not-self, "
            "ugliness, drawbacks, fairness and unfairness in the "
            "world, existence and nonexistence in the world, the "
            "world's origin and disappearance, giving up, fading "
            "away, and cessation &mdash; guaranteeing either "
            "enlightenment in this life or non-return."]),
        ("A third variant, partly overlapping the first two", [
            "This list shares giving up, fading away, and cessation "
            "with AN 10.56, and impermanence and not-self with both AN "
            "10.56 and 10.57, but introduces genuinely new material "
            "not seen in either: three paired perceptions about "
            "&ldquo;the world&rdquo; itself &mdash; its fairness and "
            "unfairness, its existence and nonexistence, its origin "
            "and disappearance."]),
        ("Anchored to a specific moment, not a general ideal", [
            "Unlike AN 10.56 and 10.57's abstract lists, this "
            "discourse names a concrete reference point: the mental "
            "consolidation a mendicant had at the moment of "
            "<em>pabbajjā</em>, going forth itself, giving this "
            "discourse its title and framing the entire training as a "
            "matter of not losing ground already won."]),
        ("A rare explicit guarantee", [
            "Where most of this chapter's teachings simply describe a "
            "practice, this discourse closes with an unusually "
            "direct promise: consolidation in these ten perceptions "
            "guarantees one of exactly two results, full enlightenment "
            "in this very life or, at minimum, non-return &mdash; "
            "language echoing the guaranteed outcomes already met "
            "elsewhere in this project, such as AN 10.46's Sakyan "
            "teaching."]),
    ],
    terms=[
        ("yathāpabbajjāparicitaṁ cittaṁ",
         "&ldquo;minds consolidated as they were when we went "
         "forth&rdquo; &mdash; the discourse's own reference point, "
         "and the source of its title, <em>pabbajjā</em>."),
        ("lokassa samañca visamañca",
         "&ldquo;what is fair and unfair in the world&rdquo; &mdash; "
         "one of three new paired perceptions about the world not "
         "seen in AN 10.56 or 10.57."),
        ("diṭṭheva dhamme aññā",
         "&ldquo;enlightenment in this very life&rdquo; &mdash; the "
         "first of the two guaranteed results."),
        ("upādisese anāgāmitā",
         "&ldquo;non-return, if there's residue left behind&rdquo; "
         "&mdash; the second, fallback guaranteed result."),
        ("lokassa bhavañca vibhavañca",
         "&ldquo;existence and nonexistence in the world&rdquo; "
         "&mdash; the second of three new paired perceptions about "
         "the world introduced in this discourse."),
    ],
    text_intro=(
        "The discourse in full: the training formula and its "
        "guaranteed result. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A training formula"),
        ("p", "&sect;1", "an10.59:1.1-1.4"),
        ("h3", "Its guaranteed result"),
        ("p", "&sect;2", "an10.59:2.1-2.2"),
    ],
    quiz=[
        {"q": "What reference point does this discourse's training "
              "formula name?",
         "opts": [
             "The moment of full ordination",
             "The mental consolidation a mendicant had at the moment "
             "of going forth (pabbajjā)",
             "The moment of first meeting the Buddha",
             "No reference point is given"],
         "correct": 1,
         "expl": "The discourse's own title and central image: not "
                 "losing ground already won."},
        {"q": "According to the guide, which three paired perceptions "
              "are genuinely new, not seen in AN 10.56 or 10.57?",
         "opts": [
             "Ugliness, death, and food's repulsiveness",
             "Fairness/unfairness, existence/nonexistence, and "
             "origin/disappearance of the world",
             "Giving up, fading away, and cessation",
             "Impermanence, not-self, and death"],
         "correct": 1,
         "expl": "Three new pairs about the world itself, distinct "
                 "from the shared material with the earlier two lists."},
        {"q": "What guaranteed result does this discourse promise for "
              "a mind consolidated in these ten perceptions?",
         "opts": [
             "Nothing is guaranteed",
             "One of two results: enlightenment in this very life, "
             "or at minimum non-return",
             "Rebirth as a deva",
             "Immediate physical health"],
         "correct": 1,
         "expl": "An unusually direct guarantee, echoing similar "
                 "promises elsewhere in this project."},
        {"q": "What does this discourse close, within AN 10 so far?",
         "opts": [
             "Nothing in particular",
             "This chapter's own run of discourses, immediately "
             "before the chapter's final page, the older spliced-in "
             "AN 10.60",
             "The entire Second Fifty",
             "The entire nipāta"],
         "correct": 1,
         "expl": "The last of this chapter's newly built pages, "
                 "handing off to the existing AN 10.60."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("Ground already won", [
            "consolidated as",
            "at going forth &mdash; the training",
            "is not to lose it",
        ]),
        ("Three new pairs", [
            "the world's own fairness,",
            "existence, and origin &mdash;",
            "perceptions turned outward",
        ]),
        ("A guarantee, stated plainly", [
            "this life's awakening,",
            "or at the least, no return &mdash;",
            "one of only two",
        ]),
        ("Cross-references", [
            "AN 10.58 &middot; previous, Rooted",
            "AN 10.56 &middot; Perceptions (1st), sharing three items "
            "with this discourse's own list",
            "AN 10.60 &middot; next, With Girimānanda, closing this "
            "chapter with the tradition's best-known ten-perception "
            "list",
        ]),
    ],
    further=[
        '<a href="%s/an10.59/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.58.html">AN 10.58 &middot; Rooted</a> &mdash; previous.',
        '<a href="an-10.60.html">AN 10.60 &middot; With Girimānanda</a> &mdash; next, '
        "closing this chapter.",
    ],
    next=("an-10.60.html", "AN 10.60 &middot; With Girimānanda"),
)


VAGGA_7 = "<em>Yamakavagga</em> &mdash; the seventh chapter of the Tens, built from five matched pairs"


# --------------------------------------------------------------------------- #
# AN 10.61 — Avijjāsutta
# --------------------------------------------------------------------------- #
page(
    61, "Avijjā", "Ignorance",
    vagga=VAGGA_7,
    meta_title="AN 10.61 — Ignorance | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Avijjāsutta, opening the Tens' seventh chapter with a "
        "nine-link causal chain running from ignorance back to "
        "associating with untrue persons, mirrored by a positive "
        "chain to freedom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "Two nine-link causal chains, each doubled with a "
                 "rain-to-ocean simile"),
        ("Length", "~3 minutes to read"),
        ("Chapter's namesake", "This discourse, paired tightly with "
                               "AN 10.62, gives the new chapter its "
                               "name, <em>Yamakavagga</em>, the "
                               "Chapter on Pairs &mdash; a name this "
                               "chapter earns literally, as all ten "
                               "of its discourses come in five "
                               "matched pairs"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "long and repetitive by design, but logically "
                       "precise"),
    ],
    why=(
        "The Buddha denies that ignorance has any discoverable first "
        "point &mdash; but insists it is not uncaused either. What "
        "follows is one of this canon's most tightly constructed "
        "causal chains, tracing ignorance back through eight further "
        "conditions to something startlingly ordinary: associating "
        "with the wrong people."),
    guide=[
        ("The teaching in one sentence", [
            "Ignorance has no discoverable beginning, yet it is "
            "fueled: by the five hindrances, fueled by the three "
            "kinds of misconduct, fueled by lack of sense restraint, "
            "fueled by lack of mindfulness and situational awareness, "
            "fueled by irrational application of mind, fueled by lack "
            "of faith, fueled by listening to an untrue teaching, "
            "fueled by associating with untrue persons &mdash; and the "
            "positive chain runs in exact mirror, ending in knowledge "
            "and freedom."]),
        ("No first cause, but not uncaused either", [
            "The opening move is philosophically precise: the Buddha "
            "refuses to name a moment ignorance began (avoiding an "
            "infinite regress or an arbitrary starting point), while "
            "still insisting ignorance depends on conditions "
            "(avoiding the opposite error of treating it as brute, "
            "inexplicable fact) &mdash; conditioned but beginningless "
            "is the precise position staked out."]),
        ("A chain ending in the mundane, not the metaphysical", [
            "Rather than terminating in some cosmic first mover, the "
            "regress of causes bottoms out in something entirely "
            "social and practical: which people one associates with. "
            "The most abstract possible question &mdash; the origin "
            "of ignorance itself &mdash; resolves into the most "
            "concrete possible answer: choose your company well."]),
        ("The rain-to-ocean simile, doubled for each direction", [
            "Both the descending chain (toward ignorance) and the "
            "ascending chain (toward freedom) are illustrated by the "
            "same cascading image &mdash; mountain rain filling "
            "hollows, then pools, then lakes, then rivers, then the "
            "ocean itself &mdash; each small stage necessary before "
            "the next can fill, exactly mirroring how each link in "
            "the causal chain must be fulfilled before the next "
            "is."]),
    ],
    terms=[
        ("purimā koṭi na paññāyati",
         "&ldquo;no prior point is evident&rdquo; &mdash; the "
         "Buddha's refusal to name a first moment of ignorance."),
        ("sāhāraṁ, no anāhāraṁ",
         "&ldquo;fueled by something, not unfueled&rdquo; &mdash; "
         "the recurring formula insisting on conditionality without "
         "a first cause."),
        ("pañca nīvaraṇā",
         "&ldquo;the five hindrances&rdquo; &mdash; the first link "
         "in the descending chain, immediately fueling ignorance."),
        ("satta bojjhaṅgā",
         "&ldquo;the seven awakening factors&rdquo; &mdash; the "
         "final link in the ascending chain, immediately fueling "
         "knowledge and freedom."),
        ("thullaphusitake deve vassante",
         "&ldquo;when the heavens rain heavily&rdquo; &mdash; the "
         "opening image of the rain-to-ocean simile, doubled for "
         "both chains."),
    ],
    text_intro=(
        "The discourse in full: the descending chain toward "
        "ignorance, the rain-to-ocean simile, then the ascending "
        "chain toward knowledge and freedom, similarly illustrated. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "No first point, yet fueled"),
        ("p", "&sect;1", "an10.61:1.1-3.2"),
        ("h3", "The rain-to-ocean simile"),
        ("p", "&sect;2", "an10.61:4.1-5.2"),
        ("h3", "The ascending chain, to knowledge and freedom"),
        ("p", "&sect;3", "an10.61:6.1-9.2"),
    ],
    quiz=[
        {"q": "What does the Buddha say about ignorance's beginning?",
         "opts": [
             "It began at a specific, datable moment",
             "No prior point is evident where ignorance began, yet it "
             "is not uncaused &mdash; it is fueled by conditions",
             "Ignorance never existed",
             "Ignorance began with the first human"],
         "correct": 1,
         "expl": "Conditioned but beginningless, a precise middle "
                 "position."},
        {"q": "What does the descending nine-link chain eventually "
              "trace ignorance back to?",
         "opts": [
             "A cosmic first cause",
             "Associating with untrue persons",
             "The creation of the world",
             "A specific past life"],
         "correct": 1,
         "expl": "The most abstract question resolves into a "
                 "concrete, social answer."},
        {"q": "What simile illustrates both the descending and "
              "ascending chains?",
         "opts": [
             "A tree growing from a seed",
             "Mountain rain filling hollows, pools, lakes, rivers, "
             "and finally the ocean",
             "A fire spreading through a forest",
             "A river flowing backward"],
         "correct": 1,
         "expl": "Each small stage must fill before the next can, "
                 "mirroring the causal chain."},
        {"q": "What is the final link in the ascending chain, "
              "immediately fueling knowledge and freedom?",
         "opts": [
             "The five hindrances",
             "The seven awakening factors",
             "Faith alone",
             "The four noble truths"],
         "correct": 1,
         "expl": "The chain's own capstone before knowledge and "
                 "freedom themselves."},
        {"q": "What does this discourse contribute to its chapter, "
              "according to the guide?",
         "opts": [
             "Nothing in particular",
             "Together with AN 10.62, it gives the chapter its name, "
             "Yamakavagga, the Chapter on Pairs &mdash; a name earned "
             "literally by this chapter's five matched-pair "
             "discourses",
             "A place name",
             "A closing colophon"],
         "correct": 1,
         "expl": "This chapter's discourses come in five genuine "
                 "pairs, unusually literal for a vagga name."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("No first point, but fueled", [
            "ignorance has no",
            "datable start &mdash; yet it still",
            "runs on conditions",
        ]),
        ("Nine links, downward", [
            "hindrances, misconduct,",
            "lack of restraint, mindfulness &mdash;",
            "down to bad company",
        ]),
        ("Rain filling an ocean", [
            "hollow, then pool, lake,",
            "river, sea &mdash; each stage required",
            "before the next fills",
        ]),
        ("Cross-references", [
            "AN 10.60 &middot; previous, closing ch.6, Sacittavagga",
            "AN 10.62 &middot; next, the same chain with one more "
            "link, this chapter's first true pair",
        ]),
    ],
    further=[
        '<a href="%s/an10.61/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.60.html">AN 10.60</a> &mdash; previous, closing chapter 6, '
        "Sacittavagga.",
        '<a href="an-10.62.html">AN 10.62 &middot; Craving</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.62 — Taṇhāsutta
# --------------------------------------------------------------------------- #
page(
    62, "Taṇhā", "Craving",
    vagga=VAGGA_7,
    meta_title="AN 10.62 — Craving | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Taṇhāsutta, which prepends one more link to AN 10.61's "
        "nine-link chain, tracing craving for continued existence "
        "back through ignorance itself. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "Two ten-link causal chains, each doubled with the "
                 "rain-to-ocean simile"),
        ("Length", "~3 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "familiar structure, one link longer"),
    ],
    why=(
        "This discourse takes AN 10.61's entire nine-link chain and "
        "prepends a single new question: what fuels craving for "
        "continued existence? The answer folds ignorance itself, "
        "along with everything beneath it, into one link of a now "
        "ten-link chain."),
    guide=[
        ("The teaching in one sentence", [
            "Craving for continued existence has no discoverable "
            "beginning either, yet it too is fueled &mdash; by "
            "ignorance, which is fueled by the same eight conditions "
            "already traced in AN 10.61, down to associating with "
            "untrue persons &mdash; while the ascending chain to "
            "knowledge and freedom runs unchanged."]),
        ("This chapter's first true pair", [
            "AN 10.61 and 10.62 are not simply thematically related: "
            "10.62 literally contains 10.61's entire chain, unchanged, "
            "with one new link added at the top. This is the "
            "chapter's founding instance of the pairing that gives "
            "<em>Yamakavagga</em> its name &mdash; not a loose thematic "
            "echo but a structural nesting of one discourse inside "
            "the next."]),
        ("Craving for continued existence, and the deepest of roots", [
            "By placing <em>bhavataṇhā</em>, craving for continued "
            "existence, one step further back than even ignorance, "
            "this discourse suggests a subtlety often left implicit "
            "elsewhere: the drive to keep existing is not simply a "
            "product of not-knowing, but has its own further layer of "
            "conditioning, even as ignorance remains inseparably "
            "bound up with it."]),
        ("The ascending chain, exactly unchanged", [
            "While the descending chain grows by one link, the "
            "ascending chain to knowledge and freedom is reproduced "
            "here word for word from AN 10.61 &mdash; the positive "
            "path does not need a matching extra step, only the "
            "negative one requires probing one layer deeper."]),
    ],
    terms=[
        ("bhavataṇhā",
         "&ldquo;craving for continued existence&rdquo; &mdash; this "
         "discourse's own title and new topmost link, one step "
         "beyond even ignorance."),
        ("avijjā",
         "&ldquo;ignorance&rdquo; &mdash; the entire subject of AN "
         "10.61, here folded into a single link fueling craving."),
        ("pañca nīvaraṇā, tīṇi duccaritāni",
         "&ldquo;the five hindrances, the three kinds of "
         "misconduct&rdquo; &mdash; two of the eight further links "
         "inherited unchanged from AN 10.61's chain."),
        ("indriyaasaṁvaro, asatāsampajaññaṁ",
         "&ldquo;lack of sense restraint, lack of mindfulness and "
         "situational awareness&rdquo; &mdash; two more of the "
         "inherited links."),
        ("assaddhiyaṁ, asaddhammassavanaṁ, asappurisasaṁsevo",
         "&ldquo;lack of faith, listening to an untrue teaching, "
         "associating with untrue persons&rdquo; &mdash; the chain's "
         "final three inherited links, unchanged from AN 10.61."),
    ],
    text_intro=(
        "The discourse in full: the ten-link descending chain, the "
        "rain-to-ocean simile, then the unchanged ascending chain. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "No first point, yet fueled"),
        ("p", "&sect;1", "an10.62:1.1-3.2"),
        ("h3", "The rain-to-ocean simile"),
        ("p", "&sect;2", "an10.62:4.1-5.2"),
        ("h3", "The ascending chain, to knowledge and freedom"),
        ("p", "&sect;3", "an10.62:6.1-8.4"),
    ],
    quiz=[
        {"q": "How does this discourse relate to AN 10.61?",
         "opts": [
             "It is unrelated",
             "It contains AN 10.61's entire nine-link chain unchanged, "
             "with one new link (craving for continued existence) "
             "added at the top",
             "It contradicts AN 10.61's chain",
             "It shortens AN 10.61's chain by one link"],
         "correct": 1,
         "expl": "A structural nesting, not a loose thematic echo."},
        {"q": "What is the new topmost link in this discourse's "
              "descending chain?",
         "opts": [
             "The five hindrances",
             "Craving for continued existence (bhavataṇhā)",
             "The seven awakening factors",
             "Associating with untrue persons"],
         "correct": 1,
         "expl": "Placed one step further back than even ignorance "
                 "itself."},
        {"q": "How does the ascending chain to knowledge and freedom "
              "compare to AN 10.61's?",
         "opts": [
             "It is completely different",
             "It is reproduced word for word, unchanged",
             "It gains one new link, matching the descending chain",
             "It is entirely omitted"],
         "correct": 1,
         "expl": "Only the negative, descending chain gains an extra "
                 "layer here."},
        {"q": "According to the guide, what does this discourse "
              "represent for the chapter as a whole?",
         "opts": [
             "Nothing structurally significant",
             "The chapter's founding instance of the matched-pair "
             "structure giving Yamakavagga its name",
             "The chapter's final discourse",
             "An unrelated digression"],
         "correct": 1,
         "expl": "The first of five genuine pairs running through "
                 "this chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("One link deeper", [
            "past ignorance itself &mdash;",
            "craving for existence,",
            "one layer further back",
        ]),
        ("A chain within a chain", [
            "AN 10.61's",
            "whole argument, nested here",
            "beneath one new link",
        ]),
        ("Only one side grows", [
            "the descent gains a",
            "rung; the ascent to freedom",
            "needs none, unchanged still",
        ]),
        ("Cross-references", [
            "AN 10.61 &middot; Ignorance, whose entire nine-link "
            "chain this discourse nests beneath one new link",
            "AN 10.63 &middot; next, opening this chapter's second "
            "pair, on the noble persons",
        ]),
    ],
    further=[
        '<a href="%s/an10.62/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.61.html">AN 10.61 &middot; Ignorance</a> &mdash; whose chain this '
        "discourse nests beneath one new link.",
        '<a href="an-10.63.html">AN 10.63 &middot; Come to a Conclusion</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.63 — Niṭṭhaṅgatasutta
# --------------------------------------------------------------------------- #
page(
    63, "Niṭṭhaṅgata", "Come to a Conclusion",
    vagga=VAGGA_7,
    meta_title="AN 10.63 — Come to a Conclusion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Niṭṭhaṅgatasutta, classifying those accomplished in view "
        "into ten kinds of noble person, five completing the path in "
        "this realm and five after leaving it. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "A single technical classification, ten types in two "
                 "groups of five"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "dense technical vocabulary naming ten "
                       "distinct spiritual attainments"),
    ],
    why=(
        "Everyone who has come to a firm conclusion about the Buddha "
        "&mdash; accomplished in view &mdash; falls into one of ten "
        "precise categories, five who will complete the path within "
        "this human realm and five who will complete it only after "
        "leaving it behind."),
    guide=[
        ("The teaching in one sentence", [
            "All those accomplished in view divide into ten types: "
            "five who conclude their path in this realm (at most "
            "seven rebirths, family-to-family, one-seeder, "
            "once-returner, or arahant in this very life) and five "
            "who conclude it after leaving this realm (extinguished "
            "between lives, upon landing, without extra effort, with "
            "extra effort, or heading upstream to the Akaniṭṭha "
            "realm)."]),
        ("A technical map, not a narrative", [
            "Unlike most of this chapter's discourses, this one "
            "offers no story, simile, or setting &mdash; just a "
            "precise, exhaustive classification of noble persons, the "
            "kind of technical map more often associated with "
            "Abhidhamma-style analysis than narrative discourse."]),
        ("Realm as the organizing axis", [
            "The ten types are not ranked by attainment alone but "
            "sorted first by where completion happens: the first "
            "five complete the path while still human, the second "
            "five only after taking rebirth in a higher, non-human "
            "realm &mdash; five distinct sub-varieties of "
            "non-returner, distinguished by exactly when and how "
            "extinguishment occurs after that rebirth."]),
        ("A direct pair with AN 10.64", [
            "This discourse's entire ten-item classification "
            "reappears in AN 10.64 without a single change &mdash; "
            "only the criterion for entering the list differs: here, "
            "&ldquo;accomplished in view&rdquo; (<em>diṭṭhisampanna</em>), "
            "there, direct experiential confidence."]),
    ],
    terms=[
        ("niṭṭhaṅgata",
         "&ldquo;come to a conclusion&rdquo; &mdash; this discourse's "
         "own title, describing firm conviction about the Buddha."),
        ("diṭṭhisampanna",
         "&ldquo;accomplished in view&rdquo; &mdash; the entry "
         "criterion for this discourse's ten-fold classification."),
        ("sattakkhattuparama",
         "&ldquo;one who has seven rebirths at most&rdquo; &mdash; "
         "the first and least advanced of the five who complete the "
         "path in this realm."),
        ("uddhaṁsoto akaniṭṭhagāmī",
         "&ldquo;one who heads upstream, going to the Akaniṭṭha "
         "realm&rdquo; &mdash; the most advanced of the five who "
         "complete the path after leaving this realm."),
        ("pañcannaṁ idha niṭṭhā, pañcannaṁ idha vihāya niṭṭhā",
         "&ldquo;five conclude their path in this realm, five after "
         "leaving this realm behind&rdquo; &mdash; the discourse's "
         "own organizing division."),
    ],
    text_intro=(
        "The discourse in full: the ten-fold classification of noble "
        "persons. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten kinds of noble person"),
        ("p", "&sect;1", "an10.63:1.1-1.10"),
    ],
    quiz=[
        {"q": "What entry criterion does this discourse use for its "
              "ten-fold classification?",
         "opts": [
             "Years of monastic seniority",
             "Being accomplished in view (diṭṭhisampanna) about the "
             "Buddha",
             "Physical health",
             "Ordination lineage"],
         "correct": 1,
         "expl": "A firm, view-based conclusion about the Buddha, "
                 "this discourse's own title."},
        {"q": "How are the ten types of noble person primarily "
              "organized?",
         "opts": [
             "By age",
             "By where completion of the path happens: five within "
             "this human realm, five only after leaving it",
             "By ordination order",
             "By region of birth"],
         "correct": 1,
         "expl": "Realm, not degree of attainment alone, is the "
                 "organizing axis."},
        {"q": "What kind of discourse is this, according to the "
              "guide?",
         "opts": [
             "A narrative with a vivid setting",
             "A technical, exhaustive classification with no story, "
             "simile, or setting &mdash; closer to Abhidhamma-style "
             "analysis",
             "A dialogue with a wanderer",
             "A verse composition"],
         "correct": 1,
         "expl": "A precise map of noble persons, not a narrated "
                 "teaching."},
        {"q": "How does this discourse relate to AN 10.64, according "
              "to the guide?",
         "opts": [
             "They are unrelated",
             "The entire ten-item list reappears unchanged in AN "
             "10.64, with only the entry criterion differing",
             "AN 10.64 contradicts this discourse",
             "AN 10.64 shortens this list to five items"],
         "correct": 1,
         "expl": "The same classification, entered by a different "
                 "door."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("Ten types, one conviction", [
            "come to a conclusion &mdash;",
            "then sorted ten ways by",
            "where the path completes",
        ]),
        ("A map, not a story", [
            "no setting, no scene &mdash;",
            "just noble persons, sorted",
            "with technical care",
        ]),
        ("Realm as the axis", [
            "human still, or gone",
            "beyond it &mdash; five and five, split",
            "by where freedom lands",
        ]),
        ("Cross-references", [
            "AN 10.62 &middot; previous, Craving",
            "AN 10.64 &middot; next, the identical ten types entered "
            "by experiential confidence rather than view",
        ]),
    ],
    further=[
        '<a href="%s/an10.63/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.62.html">AN 10.62 &middot; Craving</a> &mdash; previous.',
        '<a href="an-10.64.html">AN 10.64 &middot; Experiential Confidence</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.64 — Aveccappasannasutta
# --------------------------------------------------------------------------- #
page(
    64, "Aveccappasanna", "Experiential Confidence",
    vagga=VAGGA_7,
    meta_title="AN 10.64 — Experiential Confidence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aveccappasannasutta, applying AN 10.63's identical "
        "ten-fold classification of noble persons to stream-enterers "
        "defined by direct experiential confidence. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "The identical ten-fold classification from AN "
                 "10.63, with a different entry criterion"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "familiar content once AN 10.63 is known"),
    ],
    why=(
        "This discourse takes AN 10.63's entire ten-fold "
        "classification and reapplies it to a differently defined "
        "starting group: not those who have reasoned their way to a "
        "firm view, but those who have entered the stream through "
        "direct, experiential confidence."),
    guide=[
        ("The teaching in one sentence", [
            "Everyone who has direct experiential confidence in the "
            "Buddha has entered the stream, and divides into the same "
            "ten types already given in AN 10.63: five who complete "
            "the path in this realm, five who complete it only after "
            "leaving it."]),
        ("One classification, two doors in", [
            "AN 10.63 and this discourse form this chapter's second "
            "matched pair, illustrating that the same ten-fold "
            "outcome can be reached by two distinct routes of "
            "entry &mdash; reasoned conviction (<em>diṭṭhisampanna</em>) "
            "or direct experiential confidence "
            "(<em>aveccappasanna</em>) &mdash; without changing what "
            "lies at the far end."]),
        ("A subtle shift in starting point", [
            "AN 10.63 begins with those &ldquo;accomplished in "
            "view,&rdquo; a more intellectual framing; this discourse "
            "begins with those who have entered the stream through "
            "<em>avecca</em>, unshakeable, experientially confirmed "
            "confidence &mdash; a subtly different door into an "
            "identical destination."]),
        ("The ten types, unchanged", [
            "Every one of the ten categories &mdash; from the "
            "least advanced stream-enterer with at most seven rebirths "
            "left, through to the most advanced non-returner heading "
            "upstream to the Akaniṭṭha realm &mdash; is reproduced "
            "here exactly as in AN 10.63, without a single word "
            "changed."]),
    ],
    terms=[
        ("aveccappasanna",
         "&ldquo;experiential confidence&rdquo; &mdash; this "
         "discourse's own title, unshakeable confidence confirmed by "
         "direct experience rather than reasoned conclusion."),
        ("sotāpanna",
         "&ldquo;stream-enterer&rdquo; &mdash; the entry-level "
         "attainment this discourse's criterion guarantees."),
        ("ye keci mayi aveccappasannā",
         "&ldquo;all those who have experiential confidence in "
         "me&rdquo; &mdash; the discourse's own opening line, "
         "echoing AN 10.63's structure with a new criterion."),
        ("sattakkhattuparama, kolaṅkola, ekabījī",
         "the first three of the five who conclude the path in this "
         "realm &mdash; the same terms reused unchanged from AN "
         "10.63."),
        ("antarāparinibbāyī, upahaccaparinibbāyī",
         "two of the five non-returner types who conclude the path "
         "only after leaving this realm &mdash; also reused unchanged "
         "from AN 10.63."),
    ],
    text_intro=(
        "The discourse in full: the identical ten-fold classification "
        "from AN 10.63, entered here by experiential confidence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten kinds of noble person, entered by confidence"),
        ("p", "&sect;1", "an10.64:1.1-1.10"),
    ],
    quiz=[
        {"q": "What entry criterion does this discourse use, compared "
              "to AN 10.63's?",
         "opts": [
             "The same criterion, unchanged",
             "Direct experiential confidence (aveccappasanna) rather "
             "than being accomplished in view",
             "Years of practice",
             "A vow taken at ordination"],
         "correct": 1,
         "expl": "A different door into the identical ten-fold "
                 "classification."},
        {"q": "How does this discourse's ten-fold classification "
              "compare to AN 10.63's?",
         "opts": [
             "Completely different",
             "Reproduced exactly, without a single word changed",
             "Shortened to five types",
             "Expanded to fifteen types"],
         "correct": 1,
         "expl": "The identical ten types, reached by a different "
                 "starting criterion."},
        {"q": "What immediate attainment does experiential confidence "
              "guarantee, according to this discourse?",
         "opts": [
             "Full arahantship",
             "Stream-entry (sotāpanna)",
             "Non-return only",
             "Nothing in particular"],
         "correct": 1,
         "expl": "The baseline attainment shared by all who meet this "
                 "discourse's criterion."},
        {"q": "According to the guide, what does this pairing with AN "
              "10.63 illustrate?",
         "opts": [
             "That the two discourses contradict each other",
             "That the same ten-fold outcome can be reached by two "
             "distinct routes of entry, without changing the "
             "destination",
             "That experiential confidence is inferior to view",
             "Nothing in particular"],
         "correct": 1,
         "expl": "Two doors, one identical destination."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood",
             "No setting is stated in the source"],
         "correct": 3,
         "expl": "No location is given for this discourse."},
    ],
    marginalia=[
        ("Two doors, one map", [
            "reasoned view, or felt",
            "confidence &mdash; either enters",
            "the same ten types",
        ]),
        ("Unshakeable, not argued", [
            "avecca &mdash; confirmed",
            "by experience itself,",
            "not concluded logic",
        ]),
        ("Word for word, again", [
            "the whole classification",
            "returns unchanged &mdash; only the",
            "entry door is new",
        ]),
        ("Cross-references", [
            "AN 10.63 &middot; Come to a Conclusion, whose identical "
            "ten-fold classification this discourse reuses",
            "AN 10.65 &middot; next, opening this chapter's third "
            "pair, on happiness and suffering",
        ]),
    ],
    further=[
        '<a href="%s/an10.64/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.63.html">AN 10.63 &middot; Come to a Conclusion</a> &mdash; previous.',
        '<a href="an-10.65.html">AN 10.65 &middot; Happiness (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.65 — Paṭhamasukhasutta
# --------------------------------------------------------------------------- #
page(
    65, "Paṭhamasukha", "Happiness (1st)",
    vagga=VAGGA_7,
    meta_title="AN 10.65 — Happiness (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamasukhasutta, in which Sāriputta answers a "
        "wanderer's question about happiness and suffering with a "
        "stark equation: rebirth is suffering, no rebirth is "
        "happiness. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The little village of Nālaka, in the land of "
                     "the Magadhans"),
        ("Speakers", "The wanderer Sāmaṇḍakāni questioning Venerable "
                     "Sāriputta"),
        ("Form", "A single question, a stark equation, illustrated "
                 "with concrete physical examples"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "blunt and direct"),
    ],
    why=(
        "A wanderer named Sāmaṇḍakāni puts the most general possible "
        "question to Sāriputta &mdash; what is happiness, what is "
        "suffering &mdash; and receives an answer that cuts straight "
        "past ordinary pleasures and pains to the condition "
        "underlying them all: being reborn at all."),
    guide=[
        ("The teaching in one sentence", [
            "Rebirth itself is suffering and no rebirth is happiness "
            "&mdash; where there is rebirth, expect cold, heat, "
            "hunger, thirst, the indignities of the body, contact "
            "with fire and weapons, and the irritations of one's own "
            "relatives and friends; where there is no rebirth, expect "
            "none of it."]),
        ("A question answered at the widest possible scale", [
            "Sāmaṇḍakāni's question is deliberately unqualified "
            "&mdash; simply &ldquo;what is happiness and what is "
            "suffering&rdquo; &mdash; and Sāriputta answers at the "
            "widest possible scale, bypassing everyday pleasures and "
            "pains entirely to locate suffering in the fact of "
            "embodied existence itself."]),
        ("Concrete indignities, not abstract doctrine", [
            "Rather than an abstract account of dukkha, the list of "
            "sufferings that come with rebirth is strikingly physical "
            "and unglamorous &mdash; cold, heat, hunger, thirst, "
            "bodily functions, violence, and even the mundane "
            "annoyance of family gathering &mdash; grounding a "
            "cosmic-scale claim in the most ordinary discomforts of a "
            "body."]),
        ("The first of this chapter's third pair", [
            "This discourse opens a matched pair with AN 10.66, which "
            "repeats the identical narrative frame &mdash; the same "
            "wanderer, the same village, the same greeting &mdash; "
            "but shifts the question from happiness and suffering in "
            "general to happiness and suffering specifically within "
            "monastic practice."]),
    ],
    terms=[
        ("Sāmaṇḍakāni",
         "the wandering ascetic (<em>paribbājaka</em>) who questions "
         "Sāriputta in both this discourse and its pair, AN 10.66."),
        ("abhinibbatti dukkhā, anabhinibbatti sukhā",
         "&ldquo;rebirth is suffering, no rebirth is happiness&rdquo; "
         "&mdash; Sāriputta's central equation, answering the "
         "question at its widest possible scale."),
        ("sītaṁ, uṇhaṁ, jighacchā, pipāsā",
         "&ldquo;cold, heat, hunger, thirst&rdquo; &mdash; the same "
         "physical items already met naming the body's consequences "
         "at AN 10.49, reused here as the concrete content of "
         "rebirth's suffering."),
        ("aggisamphasso, daṇḍasamphasso, satthasamphasso",
         "&ldquo;contact with fire, clubs, and knives&rdquo; &mdash; "
         "three of the concrete physical sufferings named as "
         "consequences of rebirth."),
        ("ñātīpi mittāpi saṅgamma samāgamma rosenti",
         "&ldquo;relatives and friends get together and annoy "
         "you&rdquo; &mdash; the discourse's own closing, almost wry "
         "example of rebirth's suffering."),
    ],
    text_intro=(
        "The discourse in full: Sāmaṇḍakāni's question, and "
        "Sāriputta's equation of rebirth with suffering. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A wanderer's question"),
        ("p", "&sect;1", "an10.65:1.1-1.3"),
        ("h3", "Rebirth is suffering, no rebirth is happiness"),
        ("p", "&sect;2", "an10.65:2.1-2.8"),
    ],
    quiz=[
        {"q": "What question does the wanderer Sāmaṇḍakāni ask "
              "Sāriputta?",
         "opts": [
             "What defines schism in the Saṅgha",
             "What is happiness and what is suffering",
             "How to enter a royal compound",
             "What causes bad deeds"],
         "correct": 1,
         "expl": "A deliberately unqualified, general question."},
        {"q": "What is Sāriputta's central equation?",
         "opts": [
             "Wealth is happiness, poverty is suffering",
             "Rebirth is suffering, no rebirth is happiness",
             "Meditation is happiness, distraction is suffering",
             "Company is happiness, solitude is suffering"],
         "correct": 1,
         "expl": "An answer pitched at the widest possible scale, "
                 "beyond ordinary pleasures and pains."},
        {"q": "What kind of examples does Sāriputta give for the "
              "suffering of rebirth?",
         "opts": [
             "Abstract philosophical arguments",
             "Concrete, physical indignities: cold, heat, hunger, "
             "thirst, bodily functions, violence, and family "
             "annoyance",
             "Financial hardship only",
             "Political turmoil"],
         "correct": 1,
         "expl": "A cosmic-scale claim grounded in ordinary bodily "
                 "discomfort."},
        {"q": "According to the guide, how does this discourse relate "
              "to AN 10.66?",
         "opts": [
             "They are unrelated",
             "AN 10.66 repeats the identical narrative frame but "
             "narrows the question to happiness and suffering within "
             "monastic practice specifically",
             "AN 10.66 contradicts this discourse",
             "AN 10.66 is spoken by a different wanderer"],
         "correct": 1,
         "expl": "This chapter's third matched pair, general then "
                 "monastic-specific."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "The little village of Nālaka, in the land of the "
             "Magadhans",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A specific, named setting shared with its pair, AN "
                 "10.66."},
    ],
    marginalia=[
        ("The widest possible answer", [
            "not this pain or that,",
            "but rebirth itself &mdash; the whole",
            "condition, named at once",
        ]),
        ("Ordinary indignities", [
            "cold, heat, hunger, thirst,",
            "even family visits &mdash;",
            "suffering, made concrete",
        ]),
        ("A pair about to open", [
            "the same wanderer,",
            "the same village, waits &mdash; but next",
            "a narrower question",
        ]),
        ("Cross-references", [
            "AN 10.64 &middot; previous, Experiential Confidence",
            "AN 10.49 &middot; Existing Because of the Body, sharing "
            "several of the same physical items",
            "AN 10.66 &middot; next, the same pair of speakers, now "
            "asking about happiness within the teaching itself",
        ]),
    ],
    further=[
        '<a href="%s/an10.65/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.64.html">AN 10.64 &middot; Experiential Confidence</a> &mdash; '
        "previous.",
        '<a href="an-10.66.html">AN 10.66 &middot; Happiness (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.66 — Dutiyasukhasutta
# --------------------------------------------------------------------------- #
page(
    66, "Dutiyasukha", "Happiness (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 10.66 — Happiness (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasukhasutta, in which the same wanderer asks "
        "Sāriputta the identical question narrowed to this teaching "
        "and training, answered across the four postures and six "
        "dwelling places. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The little village of Nālaka, in the land of "
                     "the Magadhans"),
        ("Speakers", "The wanderer Sāmaṇḍakāni questioning Venerable "
                     "Sāriputta"),
        ("Form", "A single narrowed question, answered across ten "
                 "elided situations"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, formulaic, and repetitive by design"),
    ],
    why=(
        "The identical wanderer returns with a narrower version of "
        "AN 10.65's question: not happiness and suffering in general, "
        "but happiness and suffering specifically within this "
        "teaching and training &mdash; and receives an answer keyed "
        "not to rebirth, but to dissatisfaction."),
    guide=[
        ("The teaching in one sentence", [
            "Within this teaching and training, dissatisfaction is "
            "suffering and satisfaction is happiness &mdash; the "
            "dissatisfied find no happiness whether walking, "
            "standing, sitting, or lying down, in a village, a "
            "wilderness, or anywhere else, while the satisfied find "
            "happiness in every one of those same situations."]),
        ("A narrower question, a different register", [
            "By adding just three words &mdash; &ldquo;in this "
            "teaching and training&rdquo; &mdash; the wanderer shifts "
            "the entire register of the answer: AN 10.65 spoke in "
            "terms of rebirth and its absence, a cosmic-scale claim; "
            "this discourse speaks in terms of contentment and "
            "discontent, a psychological state available moment to "
            "moment within monastic life itself."]),
        ("Four postures, six places, one variable", [
            "The list runs through the four postures (walking, "
            "standing, sitting, lying down) and six kinds of "
            "location (village, wilderness, tree-root, empty hut, "
            "open air, among the mendicants) &mdash; ten situations "
            "in total, each elided in the source after the pattern is "
            "established, showing that the same single variable, "
            "satisfaction or its lack, determines happiness "
            "regardless of posture or place."]),
        ("Completing this chapter's third pair", [
            "Together, AN 10.65 and this discourse trace the same "
            "question from its widest possible framing (rebirth "
            "itself) down to its narrowest, most practical one "
            "(one's own satisfaction, right now, in whatever posture "
            "or place one happens to be) &mdash; two scales of the "
            "same underlying concern."]),
    ],
    terms=[
        ("imasmiṁ dhammavinaye",
         "&ldquo;in this teaching and training&rdquo; &mdash; the "
         "three words distinguishing this discourse's narrower "
         "question from AN 10.65's general one."),
        ("anabhirati dukkhā, abhirati sukhā",
         "&ldquo;dissatisfaction is suffering, satisfaction is "
         "happiness&rdquo; &mdash; this discourse's own central "
         "equation, replacing AN 10.65's rebirth/no-rebirth pair."),
        ("gacchantopi, ṭhitopi, nisinnopi, sayānopi",
         "&ldquo;while walking, standing, sitting, or lying "
         "down&rdquo; &mdash; the four postures across which the same "
         "test is applied."),
        ("gāmagato, araññagato, rukkhamūlagato",
         "&ldquo;gone to a village, gone to a wilderness, gone to "
         "the root of a tree&rdquo; &mdash; three of the six "
         "locations across which the same test is applied."),
        ("suññāgāragato, abbhokāsagato, bhikkhumajjhagato",
         "&ldquo;gone to an empty hut, gone to the open air, gone "
         "among the mendicants&rdquo; &mdash; the remaining three "
         "locations completing the set of six."),
    ],
    text_intro=(
        "The discourse in full: the narrower question, and "
        "Sāriputta's equation applied across the four postures and "
        "six locations. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A narrower question, from the same wanderer"),
        ("p", "&sect;1", "an10.66:1.1-2.3"),
        ("h3", "Dissatisfaction, across posture and place"),
        ("p", "&sect;2", "an10.66:2.4-2.14"),
        ("h3", "Satisfaction, across posture and place"),
        ("p", "&sect;3", "an10.66:3.1-3.12"),
    ],
    quiz=[
        {"q": "How does this discourse's question differ from AN "
              "10.65's?",
         "opts": [
             "It is identical",
             "It narrows the question to happiness and suffering "
             "specifically within this teaching and training "
             "(dhammavinaya)",
             "It asks about a completely different topic",
             "It is asked by a different wanderer"],
         "correct": 1,
         "expl": "The same wanderer, the same setting, one narrower "
                 "phrase added."},
        {"q": "What is this discourse's central equation?",
         "opts": [
             "Rebirth is suffering, no rebirth is happiness",
             "Dissatisfaction is suffering, satisfaction is "
             "happiness",
             "Poverty is suffering, wealth is happiness",
             "Solitude is suffering, company is happiness"],
         "correct": 1,
         "expl": "A shift from a cosmic-scale claim to a "
                 "moment-to-moment psychological one."},
        {"q": "Across what does this discourse's test apply, "
              "according to the guide?",
         "opts": [
             "Only while seated in meditation",
             "The four postures (walking, standing, sitting, lying "
             "down) and six kinds of location",
             "Only during almsround",
             "Only at night"],
         "correct": 1,
         "expl": "Ten situations in total, each showing the same "
                 "single variable determines happiness."},
        {"q": "According to the guide, what do AN 10.65 and this "
              "discourse trace together?",
         "opts": [
             "Two unrelated topics",
             "The same underlying question at two scales: rebirth "
             "itself, then one's own moment-to-moment satisfaction",
             "A contradiction between the two discourses",
             "Nothing in particular"],
         "correct": 1,
         "expl": "From the widest possible framing to the most "
                 "immediate, practical one."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "The little village of Nālaka, in the land of the "
             "Magadhans",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "The same setting as its pair, AN 10.65."},
    ],
    marginalia=[
        ("Three words, new scale", [
            "&ldquo;in this teaching&rdquo; &mdash;",
            "rebirth gives way to a",
            "closer, present test",
        ]),
        ("One variable, ten scenes", [
            "walking, sitting, still,",
            "in hut or open air &mdash;",
            "only content shifts",
        ]),
        ("A pair completed", [
            "cosmic scale, then near",
            "at hand &mdash; the same question, asked",
            "twice, at two distances",
        ]),
        ("Cross-references", [
            "AN 10.65 &middot; Happiness (1st), the same speakers "
            "asking the wider version of this question",
            "AN 10.67 &middot; next, opening this chapter's fourth "
            "pair, at Naḷakapāna",
        ]),
    ],
    further=[
        '<a href="%s/an10.66/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.65.html">AN 10.65 &middot; Happiness (1st)</a> &mdash; previous.',
        '<a href="an-10.67.html">AN 10.67 &middot; At Naḷakapāna (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.67 — Paṭhamanaḷakapānasutta
# --------------------------------------------------------------------------- #
page(
    67, "Paṭhamanaḷakapāna", "At Naḷakapāna (1st)",
    vagga=VAGGA_7,
    meta_title="AN 10.67 — At Naḷakapāna (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamanaḷakapānasutta, in which a tired Buddha asks "
        "Sāriputta to teach in his place, giving the waxing/waning "
        "moon simile and two ten-item lists of decline and growth. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Naḷakapāna, in the land of the Kosalans, in the "
                     "grove of flame-of-the-forest trees"),
        ("Speakers", "Sāriputta teaching the assembly while the "
                     "Buddha rests, then the Buddha confirming it"),
        ("Form", "A narrative frame, a moon simile doubled for "
                 "decline and growth, and two ten-item lists of "
                 "individual types"),
        ("Length", "~3 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "vivid narrative carrying dense content"),
    ],
    why=(
        "In an unusually intimate narrative moment, the Buddha, "
        "physically tired after a long night's teaching, asks "
        "Sāriputta to take over and lies down to rest &mdash; and "
        "what Sāriputta delivers, on his own authority, the Buddha "
        "rises to personally confirm word for word."),
    guide=[
        ("The teaching in one sentence", [
            "A person lacking faith, conscience, prudence, energy, "
            "and wisdom can expect only decline in skillful qualities, "
            "like the moon in its waning fortnight; a person with "
            "those five qualities can expect only growth, like the "
            "moon waxing &mdash; illustrated further by two ten-item "
            "lists naming the individual in decline and the "
            "individual who does not decline."]),
        ("A rare, physically human moment", [
            "The Buddha's back is sore; he explicitly asks Sāriputta "
            "to continue the teaching so he can rest, then lies down "
            "in the traditional lion's posture, mindful even in "
            "repose &mdash; one of the more vivid glimpses in this "
            "project of the Buddha's own physical humanity within an "
            "otherwise formal teaching setting."]),
        ("An asymmetric pair of ten-item lists", [
            "The list of ten individual types &ldquo;in decline&rdquo; "
            "(faithless, no conscience, imprudent, lazy, witless, "
            "irritable, acrimonious, corrupt-wishes, bad-friends, "
            "wrong-view) does not simply mirror its counterpart of "
            "ten who &ldquo;don't decline&rdquo; (faithful, "
            "conscientious, prudent, energetic, wise, loving, kind, "
            "few-desires, good-friends, right-view): the first five "
            "items pair as exact opposites, but items six through ten "
            "shift register &mdash; the cure for irritability is not "
            "named as its literal opposite but as active loving-"
            "kindness."]),
        ("Delegated, then personally ratified", [
            "The Buddha does not merely permit Sāriputta's teaching in "
            "advance; he rises afterward and repeats large portions "
            "of it himself, word for word, publicly endorsing what "
            "his disciple taught in his absence with an explicit "
            "&ldquo;Good, good, Sāriputta!&rdquo;"]),
    ],
    terms=[
        ("Naḷakapāna",
         "a town of the Kosalans, and this discourse's own setting, "
         "in a grove of flame-of-the-forest (<em>naḷakapāna</em>) "
         "trees."),
        ("sīhaseyya",
         "the &ldquo;lion's posture&rdquo; &mdash; lying on the "
         "right side with one foot atop the other, mindful and aware, "
         "the traditional posture the Buddha adopts to rest."),
        ("kāḷapakkha, juṇhapakkha",
         "&ldquo;the waning fortnight, the waxing fortnight&rdquo; "
         "&mdash; the two halves of the lunar month structuring this "
         "discourse's central simile."),
        ("assaddho purisapuggalo",
         "&ldquo;a faithless individual&rdquo; &mdash; the opening "
         "item of the ten-item list naming who is in decline."),
        ("sādhu, sādhu, sāriputta",
         "&ldquo;good, good, Sāriputta!&rdquo; &mdash; the Buddha's "
         "own explicit endorsement upon rising and hearing what was "
         "taught in his absence."),
    ],
    text_intro=(
        "The discourse in full: the narrative setting, Sāriputta's "
        "teaching with the moon simile and both ten-item lists, and "
        "the Buddha's rising confirmation. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha, tired, hands over to Sāriputta"),
        ("p", "&sect;1", "an10.67:1.1-3.5"),
        ("h3", "The waning moon: decline"),
        ("p", "&sect;2", "an10.67:4.1-5.10"),
        ("h3", "The waxing moon: growth"),
        ("p", "&sect;3", "an10.67:6.1-7.10"),
        ("h3", "The Buddha rises and confirms it"),
        ("p", "&sect;4", "an10.67:8.1-11.10"),
    ],
    quiz=[
        {"q": "Why does the Buddha ask Sāriputta to take over the "
              "teaching?",
         "opts": [
             "He has nothing left to say",
             "His back is sore, and he wants to rest",
             "He is testing Sāriputta",
             "He has to leave for another town"],
         "correct": 1,
         "expl": "A rare, physically human moment of fatigue."},
        {"q": "What simile structures the core teaching?",
         "opts": [
             "A tree growing and withering",
             "The moon in its waning and waxing fortnights",
             "A river flowing to the sea",
             "A fire being lit and extinguished"],
         "correct": 1,
         "expl": "Decline mirrors the waning moon, growth the waxing "
                 "moon."},
        {"q": "According to the guide, how do the two ten-item lists "
              "of individual types relate to each other?",
         "opts": [
             "They mirror each other exactly, item for item",
             "The first five items pair as exact opposites, but items "
             "six through ten shift register &mdash; e.g. the cure "
             "for irritability is named as active loving-kindness, "
             "not simply its literal opposite",
             "They are completely unrelated lists",
             "The second list has fewer items than the first"],
         "correct": 1,
         "expl": "A partial, not total, mirroring between the two "
                 "lists."},
        {"q": "What does the Buddha do after Sāriputta finishes "
              "teaching?",
         "opts": [
             "Nothing; he remains resting",
             "He rises and personally repeats and confirms large "
             "portions of the teaching, with &ldquo;Good, good, "
             "Sāriputta!&rdquo;",
             "He criticizes Sāriputta's teaching",
             "He asks another disciple to verify it"],
         "correct": 1,
         "expl": "A public, explicit endorsement of the delegated "
                 "teaching."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Naḷakapāna, in the land of the Kosalans, in the grove "
             "of flame-of-the-forest trees",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A specific, named setting shared with its pair, AN "
                 "10.68."},
    ],
    marginalia=[
        ("A sore back, a rare glimpse", [
            "even the Buddha",
            "tires &mdash; and hands the teaching",
            "to his own disciple",
        ]),
        ("Waning moon, waxing moon", [
            "beauty, roundness, light &mdash;",
            "decline or growth, day and night,",
            "never standing still",
        ]),
        ("Not quite mirrored", [
            "faith's opposite is",
            "no faith &mdash; but anger's cure",
            "is love, not its twin",
        ]),
        ("Cross-references", [
            "AN 10.66 &middot; previous, Happiness (2nd)",
            "AN 10.68 &middot; next, the same setting, a compressed "
            "second telling",
        ]),
    ],
    further=[
        '<a href="%s/an10.67/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.66.html">AN 10.66 &middot; Happiness (2nd)</a> &mdash; previous.',
        '<a href="an-10.68.html">AN 10.68 &middot; At Naḷakapāna (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.68 — Dutiyanaḷakapānasutta
# --------------------------------------------------------------------------- #
page(
    68, "Dutiyanaḷakapāna", "At Naḷakapāna (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 10.68 — At Naḷakapāna (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyanaḷakapānasutta, retelling AN 10.67's scene with "
        "an expanded ten-factor condition compressed into a single "
        "clause, without the closing ten-item lists. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Naḷakapāna, in the grove of flame-of-the-forest "
                     "trees"),
        ("Speakers", "Sāriputta teaching the assembly while the "
                     "Buddha rests, then the Buddha confirming it"),
        ("Form", "The identical narrative frame as AN 10.67, with a "
                 "denser single condition replacing its two lists"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "same scene, more compressed content"),
    ],
    why=(
        "This second Naḷakapāna discourse repeats its pair's entire "
        "narrative scene &mdash; the Buddha's sore back, the "
        "delegated teaching, the rising confirmation &mdash; but "
        "compresses AN 10.67's five-item quality and separate "
        "ten-item lists into one denser, ten-factor condition."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant lacking faith, conscience, prudence, energy, "
            "and wisdom, who has no wish to listen, does not memorize "
            "the teachings, does not examine their meaning, does not "
            "practice accordingly, and is negligent, can expect only "
            "decline, like the waning moon; one with all ten "
            "qualities can expect only growth, like the waxing "
            "moon."]),
        ("The same scene, told again", [
            "Every detail of AN 10.67's narrative opening recurs here "
            "nearly verbatim: the sore back, the request to "
            "Sāriputta, the lion's posture, the address to the silent "
            "assembly &mdash; establishing this as a genuine "
            "companion piece rather than an unrelated discourse that "
            "merely shares a location."]),
        ("Five qualities become ten factors, compressed", [
            "Where AN 10.67 kept its five-item quality "
            "(faith/conscience/prudence/energy/wisdom) and its "
            "two ten-item lists of individual types separate, this "
            "discourse folds five more items &mdash; wanting to "
            "listen, memorizing teachings, examining their meaning, "
            "practicing accordingly, and diligence &mdash; directly "
            "into a single ten-part condition, then drops the "
            "separate individual-type lists entirely."]),
        ("A shorter, denser retelling", [
            "The overall effect is a more compressed cousin of AN "
            "10.67: the same moon simile, the same delegation-then-"
            "confirmation structure, but a single expanded condition "
            "in place of two distinct five-item and ten-item "
            "teachings &mdash; efficient where AN 10.67 was "
            "expansive."]),
    ],
    terms=[
        ("sotukāmatā",
         "&ldquo;wanting to listen&rdquo; &mdash; the first of five "
         "new factors folded into this discourse's expanded, ten-part "
         "condition."),
        ("dhammadhāraṇatā",
         "&ldquo;memorizing the teachings&rdquo; &mdash; the second "
         "of the five newly added factors."),
        ("appamāda",
         "&ldquo;diligence&rdquo; &mdash; the tenth and final factor "
         "in this discourse's compressed condition, absent from AN "
         "10.67's separate five-item quality."),
        ("atthūpaparikkhā",
         "&ldquo;examining their meaning&rdquo; &mdash; the third of "
         "the five new factors folded into this discourse's expanded "
         "condition."),
        ("dhammānudhammappaṭipatti",
         "&ldquo;practicing accordingly&rdquo; &mdash; the fourth of "
         "the five new factors, joining faith, conscience, prudence, "
         "energy, and wisdom."),
    ],
    text_intro=(
        "The discourse in full: the identical narrative frame, "
        "followed by the compressed ten-factor teaching. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha, tired, hands over to Sāriputta"),
        ("p", "&sect;1", "an10.68:1.1-3.5"),
        ("h3", "The waning and waxing moon, ten factors compressed"),
        ("p", "&sect;2", "an10.68:4.1-5.12"),
        ("h3", "The Buddha rises and confirms it"),
        ("p", "&sect;3", "an10.68:6.1-7.12"),
    ],
    quiz=[
        {"q": "How does this discourse's narrative opening compare to "
              "AN 10.67's?",
         "opts": [
             "Completely different",
             "Nearly verbatim: the same sore back, the same request "
             "to Sāriputta, the same lion's posture",
             "It omits the Buddha entirely",
             "It is set in a different location"],
         "correct": 1,
         "expl": "A genuine companion piece sharing the full narrative "
                 "scene."},
        {"q": "How does this discourse's core teaching differ from AN "
              "10.67's?",
         "opts": [
             "It is identical in every respect",
             "It folds five more factors (wanting to listen, "
             "memorizing, examining meaning, practicing accordingly, "
             "diligence) into a single ten-part condition, dropping "
             "the separate individual-type lists",
             "It removes the moon simile",
             "It is spoken by a different disciple"],
         "correct": 1,
         "expl": "A denser, more compressed version of the same "
                 "underlying teaching."},
        {"q": "What happens to AN 10.67's two ten-item lists of "
              "individual types in this discourse?",
         "opts": [
             "They are expanded further",
             "They are dropped entirely, replaced by the single "
             "compressed condition",
             "They are repeated unchanged",
             "They are reduced to five items each"],
         "correct": 1,
         "expl": "A shorter, denser retelling in place of the "
                 "separate lists."},
        {"q": "What simile does this discourse share with AN 10.67?",
         "opts": [
             "A tree growing and withering",
             "The waning and waxing moon",
             "A river reaching the sea",
             "No simile is used"],
         "correct": 1,
         "expl": "The same central image, applied to the newly "
                 "compressed condition."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Naḷakapāna, in the grove of flame-of-the-forest trees",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "The same setting as its pair, AN 10.67."},
    ],
    marginalia=[
        ("The same scene, retold", [
            "sore back, silent hall,",
            "Sāriputta rises to",
            "speak in the Buddha's place",
        ]),
        ("Five become ten, compressed", [
            "faith and wisdom, now",
            "joined by listening, practice,",
            "diligence as well",
        ]),
        ("Two lists become one clause", [
            "no separate roster",
            "of who declines and who doesn't &mdash;",
            "just one dense condition",
        ]),
        ("Cross-references", [
            "AN 10.67 &middot; At Naḷakapāna (1st), sharing this "
            "discourse's entire narrative frame",
            "AN 10.69 &middot; next, opening this chapter's fifth "
            "and final pair, on topics of discussion",
        ]),
    ],
    further=[
        '<a href="%s/an10.68/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.67.html">AN 10.67 &middot; At Naḷakapāna (1st)</a> &mdash; previous.',
        '<a href="an-10.69.html">AN 10.69 &middot; Topics of Discussion (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.69 — Paṭhamakathāvatthusutta
# --------------------------------------------------------------------------- #
page(
    69, "Paṭhamakathāvatthu", "Topics of Discussion (1st)",
    vagga=VAGGA_7,
    meta_title="AN 10.69 — Topics of Discussion (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭhamakathāvatthusutta, in which the Buddha catches "
        "mendicants in idle talk and names ten proper topics of "
        "discussion, promising glory surpassing sun and moon. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's "
                     "monastery"),
        ("Speakers", "The Buddha, addressing mendicants caught in "
                     "idle talk"),
        ("Form", "A narrative catching an offense in progress, a "
                 "sweeping catalogue of forbidden topics, and a "
                 "ten-item list of proper ones"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a long catalogue followed by a tight list"),
    ],
    why=(
        "Catching a group of mendicants deep in idle chatter about "
        "kings, armies, gossip, and worldly affairs, the Buddha "
        "names ten topics worth discussing instead &mdash; and makes "
        "an unusually grand promise for what proper conversation "
        "alone can achieve."),
    guide=[
        ("The teaching in one sentence", [
            "There are ten proper topics of discussion &mdash; "
            "fewness of wishes, contentment, seclusion, aloofness, "
            "arousing energy, ethics, immersion, wisdom, freedom, and "
            "the knowledge and vision of freedom &mdash; and "
            "mendicants who return to these topics again and again "
            "could outshine even the sun and moon in glory."]),
        ("A sweeping catalogue of forbidden talk", [
            "Before naming the proper ten, the discourse first "
            "catalogues, at unusual length, everything the mendicants "
            "were actually discussing: kings, bandits, ministers, "
            "armies, food, clothes, beds, garlands, fragrances, "
            "family, vehicles, geography, women, heroes, street "
            "gossip, well-side gossip, the dead, miscellany, "
            "travelers' tales, and speculation about future rebirths "
            "&mdash; one of this project's longest single "
            "enumerations of ordinary worldly conversation."]),
        ("A structural echo of ordinary talk", [
            "The sheer length and specificity of the forbidden-topics "
            "list, deliberately contrasted with the tight, "
            "disciplined ten-item list that replaces it, makes the "
            "point structurally as much as doctrinally: worldly talk "
            "sprawls without limit, while proper talk is precisely "
            "bounded."]),
        ("An unusually cosmic reward for mere conversation", [
            "The closing promise is striking in scale: mendicants who "
            "keep returning to these ten topics &ldquo;could surpass "
            "even the sun and moon, so mighty and powerful&rdquo; "
            "&mdash; an extravagant claim for something as ordinary "
            "as what one talks about after a meal."]),
    ],
    terms=[
        ("tiracchānakathā",
         "&ldquo;low talk,&rdquo; literally &ldquo;animal talk&rdquo; "
         "&mdash; the Buddha's own term for the sprawling catalogue "
         "of worldly conversation the mendicants were caught in."),
        ("dasa kathāvatthūni",
         "&ldquo;ten topics of discussion&rdquo; &mdash; this "
         "discourse's own title and central teaching."),
        ("appicchakathā, santuṭṭhikathā",
         "&ldquo;talk about fewness of wishes, talk about "
         "contentment&rdquo; &mdash; the first two of the ten proper "
         "topics."),
        ("candimasuriyānaṁ",
         "&ldquo;the sun and moon&rdquo; &mdash; the standard of "
         "glory this discourse claims proper conversation alone can "
         "surpass."),
        ("tejasā tejaṁ pariyādiyeyyātha",
         "&ldquo;you could surpass their radiance with your "
         "own&rdquo; &mdash; the discourse's own vivid image for "
         "outshining the sun and moon."),
    ],
    text_intro=(
        "The discourse in full: the mendicants caught in idle talk, "
        "the Buddha's rebuke, and the ten proper topics. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Caught in low talk"),
        ("p", "&sect;1", "an10.69:1.1-3.4"),
        ("h3", "Ten proper topics of discussion"),
        ("p", "&sect;2", "an10.69:4.1-5.1"),
    ],
    quiz=[
        {"q": "What does the Buddha catch the mendicants doing?",
         "opts": [
             "Meditating in silence",
             "Engaged in a long list of idle, worldly talk &mdash; "
             "about kings, armies, gossip, and more",
             "Reciting the monastic code",
             "Sleeping"],
         "correct": 1,
         "expl": "One of this project's longest single catalogues of "
                 "ordinary conversation."},
        {"q": "What are the ten proper topics of discussion named in "
              "this discourse?",
         "opts": [
             "Ten monastic offenses",
             "Fewness of wishes, contentment, seclusion, aloofness, "
             "energy, ethics, immersion, wisdom, freedom, and the "
             "knowledge and vision of freedom",
             "Ten meditation postures",
             "Ten grounds for accusation"],
         "correct": 1,
         "expl": "A tight, disciplined list contrasted with the "
                 "sprawling forbidden catalogue."},
        {"q": "According to the guide, what structural point does the "
              "contrast between the two lists make?",
         "opts": [
             "No particular point",
             "Worldly talk sprawls without limit, while proper talk "
             "is precisely bounded to ten items",
             "The two lists are actually identical",
             "The forbidden list is shorter than the proper one"],
         "correct": 1,
         "expl": "Length and specificity making the doctrinal point "
                 "structurally."},
        {"q": "What reward does the Buddha promise for returning to "
              "these ten topics again and again?",
         "opts": [
             "A comfortable rebirth",
             "Glory that could surpass even the sun and moon",
             "Immediate enlightenment",
             "Freedom from all illness"],
         "correct": 1,
         "expl": "An unusually cosmic-scale claim for ordinary "
                 "conversation."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Naḷakapāna",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 0,
         "expl": "A specific, named setting shared with its pair, AN "
                 "10.70."},
    ],
    marginalia=[
        ("Caught mid-gossip", [
            "kings, armies, beds,",
            "family, gossip by wells &mdash;",
            "the list runs and runs",
        ]),
        ("Ten, bounded and precise", [
            "few wishes, content,",
            "seclusion, energy, ethics &mdash;",
            "a tight list, at last",
        ]),
        ("Brighter than sun and moon", [
            "an ordinary thing &mdash;",
            "what mendicants talk about &mdash;",
            "promised cosmic glory",
        ]),
        ("Cross-references", [
            "AN 10.68 &middot; previous, At Naḷakapāna (2nd)",
            "AN 10.70 &middot; next, the same forbidden catalogue, "
            "reframed as grounds for praise",
        ]),
    ],
    further=[
        '<a href="%s/an10.69/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.68.html">AN 10.68 &middot; At Naḷakapāna (2nd)</a> &mdash; previous.',
        '<a href="an-10.70.html">AN 10.70 &middot; Topics of Discussion (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 10.70 — Dutiyakathāvatthusutta
# --------------------------------------------------------------------------- #
page(
    70, "Dutiyakathāvatthu", "Topics of Discussion (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 10.70 — Topics of Discussion (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyakathāvatthusutta, closing the Yamakavagga by "
        "reframing AN 10.69's ten topics as grounds for praise, each "
        "requiring both personal embodiment and teaching others. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's "
                     "monastery"),
        ("Speakers", "The Buddha alone, addressing the mendicants"),
        ("Form", "The same catalogue of forbidden talk, reframed as "
                 "ten grounds for praise"),
        ("Length", "~2 minutes to read"),
        ("Closing this chapter", "This discourse closes "
                                 "<em>Yamakavagga</em>, the seventh "
                                 "chapter, with its own untranslated "
                                 "colophon and uddāna verse naming "
                                 "all ten discourses"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "familiar list, reframed with a doubled "
                       "requirement"),
    ],
    why=(
        "Closing the chapter, this discourse repeats AN 10.69's "
        "sprawling catalogue of idle talk but changes what follows: "
        "rather than ten proper topics to discuss, it gives ten "
        "grounds for praise, each demanding a mendicant both embody a "
        "quality personally and be able to teach others on it."),
    guide=[
        ("The teaching in one sentence", [
            "There are ten grounds for praise: a mendicant who is "
            "personally has few wishes, content, secluded, aloof, "
            "energetic, ethical, immersed, wise, free, and possessed "
            "of the knowledge and vision of freedom, and who can also "
            "speak to others on each of these same qualities, earns "
            "praise on each count."]),
        ("The same catalogue, a different consequence", [
            "This discourse opens with the identical sprawling list "
            "of low talk already met in AN 10.69, but where that "
            "discourse responded with ten <em>topics</em> to discuss, "
            "this one responds with ten <em>grounds for praise</em> "
            "&mdash; shifting the emphasis from what mendicants should "
            "talk about to what kind of person is worthy of "
            "commendation."]),
        ("A doubled requirement, not a single quality", [
            "Each of the ten grounds is explicitly two-part: personal "
            "possession of the quality alone is not enough, nor is "
            "the ability to speak about it alone &mdash; praise "
            "requires both embodying the quality <em>and</em> being "
            "able to articulate it for others, a higher bar than "
            "either half alone."]),
        ("Closing the chapter of pairs, with a pair of its own", [
            "As the second half of this chapter's fifth and final "
            "matched pair, this discourse closes <em>Yamakavagga</em> "
            "fittingly &mdash; itself internally doubled (personal "
            "quality plus teaching ability), closing a chapter built "
            "entirely from doubled discourses, with its own colophon "
            "and uddāna verse naming all ten discourses of the "
            "chapter."]),
    ],
    terms=[
        ("dasa pāsaṁsāni ṭhānāni",
         "&ldquo;ten grounds for praise&rdquo; &mdash; this "
         "discourse's own central teaching, replacing AN 10.69's ten "
         "topics of discussion."),
        ("attanā ca appiccho hoti, appicchakathañca bhikkhūnaṁ "
         "kattā hoti",
         "&ldquo;personally has few wishes, and speaks to the "
         "mendicants on having few wishes&rdquo; &mdash; the doubled "
         "formula (embodiment plus teaching) repeated for each of the "
         "ten grounds."),
        ("Yamakavaggo dutiyo",
         "&ldquo;the Pairs Chapter, the second&rdquo; &mdash; the "
         "chapter's own closing colophon, left untranslated in the "
         "English text."),
        ("attanā ca āraddhavīriyo hoti, vīriyārambhakathañca "
         "bhikkhūnaṁ kattā hoti",
         "&ldquo;personally is energetic, and speaks to the "
         "mendicants on rousing energy&rdquo; &mdash; the fifth of "
         "the ten doubled grounds."),
        ("uddāna",
         "a summary verse naming, in brief, all ten discourses just "
         "covered &mdash; here closing the chapter, left untranslated "
         "in the English text."),
    ],
    text_intro=(
        "The discourse in full: the same catalogue of low talk, then "
        "the ten grounds for praise. The chapter's own colophon and "
        "uddāna verse, in Pāli only, are described but not "
        "reproduced. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Caught in low talk, again"),
        ("p", "&sect;1", "an10.70:1.1-1.3"),
        ("h3", "Ten grounds for praise"),
        ("p", "&sect;2", "an10.70:2.1-12.1"),
    ],
    quiz=[
        {"q": "How does this discourse's opening scene compare to AN "
              "10.69's?",
         "opts": [
             "Completely different",
             "It repeats the identical sprawling catalogue of low "
             "talk",
             "It shows the mendicants meditating instead",
             "It omits the catalogue entirely"],
         "correct": 1,
         "expl": "The same forbidden-topics list, reused here."},
        {"q": "What does this discourse give in place of AN 10.69's "
              "ten topics of discussion?",
         "opts": [
             "A list of monastic offenses",
             "Ten grounds for praise, each requiring both personal "
             "embodiment of a quality and the ability to teach others "
             "on it",
             "A closing verse only",
             "A repeat of the same ten topics, unchanged"],
         "correct": 1,
         "expl": "A shift from what to discuss to who deserves "
                 "commendation."},
        {"q": "According to the guide, what makes each ground for "
              "praise a \"doubled requirement\"?",
         "opts": [
             "It requires two separate mendicants to act together",
             "It requires both personally possessing the quality and "
             "being able to articulate it for others &mdash; neither "
             "alone is enough",
             "It requires the quality be praised twice",
             "It has no doubled structure"],
         "correct": 1,
         "expl": "A higher bar than either embodiment or teaching "
                 "ability alone."},
        {"q": "What does this discourse close, according to the "
              "guide?",
         "opts": [
             "Nothing in particular",
             "Yamakavagga, the seventh chapter, itself internally "
             "doubled and closing a chapter built entirely from "
             "matched pairs",
             "The entire Second Fifty",
             "The entire nipāta"],
         "correct": 1,
         "expl": "A fitting close, doubled in structure, to a chapter "
                 "of doubles."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Naḷakapāna",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 0,
         "expl": "The same setting as its pair, AN 10.69."},
    ],
    marginalia=[
        ("The same gossip, again", [
            "kings, armies, beds &mdash;",
            "the same sprawling list returns,",
            "answered differently",
        ]),
        ("Not just talk, but proof", [
            "few wishes alone",
            "isn't enough &mdash; teach it too,",
            "or praise doesn't land",
        ]),
        ("A pair closing pairs", [
            "doubled in structure,",
            "closing a chapter built from",
            "nothing but doubles",
        ]),
        ("Cross-references", [
            "AN 10.69 &middot; previous, the same catalogue answered "
            "with topics rather than praise",
            "AN 10.61 &middot; Ignorance, opening this chapter and "
            "this chapter's very first pair",
        ]),
    ],
    further=[
        '<a href="%s/an10.70/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-10.69.html">AN 10.69 &middot; Topics of Discussion (1st)</a> &mdash; '
        "previous.",
        '<a href="an-10.61.html">AN 10.61 &middot; Ignorance</a> &mdash; opening this '
        "chapter.",
    ],
)
