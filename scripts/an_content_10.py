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
