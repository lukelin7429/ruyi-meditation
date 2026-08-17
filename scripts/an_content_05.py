# -*- coding: utf-8 -*-
"""Pañcaka Nipāta — The Fives. One discourse per page, from AN 5.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Pañcaka Nipāta — The Fives"
# The Fives follow the Fours. an-5.28.html and an-5.57.html were published
# before this series began working in order, in the earlier eighteen-page
# selection; they are listed in the index by INDEX_EXTRA and are not
# generated here. HEAD points at the last page the Fours module reached, now
# fixed at 510/510. TAIL points at the nearest already-published page beyond
# the Fives -- an-6.16.html, from the same earlier selection -- until the
# Sixes module exists and TAIL can move to its own first page.
HEAD = ("an-4.304-783.html", "AN 4.304&ndash;783 &middot; Insight into Hate, and So On")
TAIL = ("an-6.16.html", "AN 6.16 &middot; Nakula&rsquo;s Father")
INDEX_EXTRA = [
    ("an-5.28", "Pañcaṅgika", "With Five Factors"),
    ("an-5.57", "Anussatiṭṭhāna", "Subjects for Regular Reviewing"),
]

PAGES = []

VAGGA_1 = "<em>Sekhabalavagga</em> &mdash; the first chapter of the Fives"
SETTING_1 = ("Sāvatthī, in Jeta’s Grove, Anāthapiṇḍika’s monastery; "
             "stated at the head of AN 5.1 and understood to hold across the chapter")
SETTING_CONT = ("None stated; the discourse continues from AN 5.1, whose setting at Sāvatthī "
                 "in Jeta’s Grove is understood to hold")
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Fives."""
    d = {
        "slug": "an-5.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an5/an5.%d" % num,
        "crumb": "AN 5.%d" % num,
        "number_line": "Aṅguttara Nikāya · Discourse 5.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 5.1 — Saṅkhittasutta
# --------------------------------------------------------------------------- #
page(
    1, "Saṅkhitta", "In Brief",
    meta_title="AN 5.1 — In Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṅkhittasutta, the "
        "discourse that opens the Fives — a bare list of five powers of a trainee: faith, "
        "conscience, prudence, energy, and wisdom, stated once with no elaboration. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming the five, and a single sentence of injunction to train "
                 "in them"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The five items recur widely as building blocks of larger training "
                              "lists across the Chinese Āgamas and Abhidharma literature; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest kind of opening "
                       "statement, and its interest is in what it deliberately withholds"),
    ],
    why=(
        "The Fives open the way the Fours did not: with a bare list and no argument at all. Five "
        "powers of a trainee &mdash; faith, conscience, prudence, energy, wisdom &mdash; named once, "
        "followed by a single line telling the listener to train in having them. No simile, no "
        "story, no declaration of what results. A reader who has just finished the Fours, which "
        "opened on a first-person confession, may find this terse. That terseness is itself the "
        "discourse&rsquo;s method: it names the material and waits for AN 5.2 to unpack it."),
    guide=[
        ("The teaching in one sentence", [
            "Five things &mdash; faith, conscience, prudence, energy, wisdom &mdash; are called the "
            "<em>sekhabala</em>, the powers of a trainee, and the listener is told to train so as to "
            "have them."]),
        ("A list met before, now made foundational", [
            "This exact five-item set already appeared once in this series, at "
            "<a href=\"an-4.163.html\">AN 4.163</a>, where it showed up almost in passing, one of "
            "two supports a mendicant was said to rely on. There it was a detail. Here it is the "
            "material the entire first chapter of the Fives is built from &mdash; the next nine "
            "discourses all turn the same five qualities over from different angles.",
            "The earlier page also flagged the point worth repeating briefly here: this list shares "
            "three of its five terms &mdash; faith, energy, wisdom &mdash; with the much better "
            "known five faculties and five powers (<em>indriya</em> and <em>bala</em>) that close "
            "out the thirty-seven aids to awakening. It replaces the other two, mindfulness and "
            "immersion, with <em>hiri</em> and <em>ottappa</em>, conscience and prudence. The two "
            "lists are not the same list under two names; a reader should keep them distinct."]),
        ("Conscience and prudence, briefly restated", [
            "<em>Hiri</em> and <em>ottappa</em> received a full discourse to themselves already, at "
            "<a href=\"an-2.1-10.html\">AN 2.9</a>, which called them <em>lokapāla</em>, "
            "world-protectors, and argued that without them ordinary social bonds would collapse. "
            "That argument is not repeated here; what matters for this page is only that the pair "
            "was already established as a fixed unit before the Fives began, and this discourse "
            "simply draws on it."]),
        ("Why &ldquo;in brief&rdquo;", [
            "The title <em>Saṅkhitta</em> names the discourse&rsquo;s own method: stated briefly. "
            "Its companion, the very next discourse, is titled <em>Vitthata</em>, &ldquo;in "
            "detail.&rdquo; This brief-then-detailed pairing at the head of a chapter has not "
            "appeared this way in this series before &mdash; the Fours opened with a confession, "
            "the Threes with a warning about three kinds of peril &mdash; and it is worth noticing "
            "as something distinctive to how the Fives choose to begin.",
            "The pairing also sets an expectation for how to read the two discourses: not as two "
            "independent teachings but as one teaching given twice, compressed and then expanded. "
            "AN 5.1 should not be read in isolation; its brevity only makes sense next to what "
            "follows it immediately."]),
        ("Who a &ldquo;trainee&rdquo; is", [
            "<em>Sekha</em>, trainee, is the canon&rsquo;s standing word for someone who has entered "
            "the path but not yet completed it &mdash; anyone still doing the work these five powers "
            "support. It is a term of the path&rsquo;s middle, neither beginner nor finished, and it "
            "is the word this whole chapter, and eventually this whole nipāta, takes its name from."]),
    ],
    terms=[
        ("sekhabala",
         "&ldquo;power of a trainee&rdquo; &mdash; the five-item list this chapter is named for, "
         "already met once at AN 4.163 and now the organizing material of an entire vagga."),
        ("sekha",
         "&ldquo;trainee&rdquo; &mdash; one who has entered the path but not yet completed it; the "
         "person these five powers are said to belong to."),
        ("saṅkhitta",
         "&ldquo;in brief&rdquo; &mdash; this discourse&rsquo;s own title, naming its compressed "
         "method and setting up its companion, <em>vitthata</em>."),
        ("vitthata",
         "&ldquo;in detail&rdquo; &mdash; the title of AN 5.2, the discourse immediately following, "
         "which expands each of these five powers in turn."),
        ("lokapāla",
         "&ldquo;world-protector&rdquo; &mdash; the epithet AN 2.9 gives to <em>hiri</em> and "
         "<em>ottappa</em>, two of this list&rsquo;s five items, before the Fives begin."),
    ],
    text_intro=(
        "The discourse in full: the five powers of a trainee, named once, and the injunction to "
        "train in them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Sāvatthī"),
        ("p", "&sect;1", "an5.1:1.1-1.6"),
        ("h3", "The five powers of a trainee"),
        ("p", "&sect;2", "an5.1:2.1-2.4"),
        ("h3", "The injunction"),
        ("p", "&sect;3", "an5.1:3.1-3.5"),
    ],
    quiz=[
        {"q": "What five qualities does AN 5.1 name as the powers of a trainee?",
         "opts": [
             "Faith, energy, mindfulness, immersion, and wisdom",
             "Faith, conscience, prudence, energy, and wisdom",
             "Ethics, immersion, wisdom, and freedom",
             "Generosity, ethics, patience, energy, and wisdom"],
         "correct": 1,
         "expl": "Saddhā, hiri, ottappa, vīriya, paññā — the sekhabala."},
        {"q": "What does the title &lsquo;Saṅkhitta&rsquo; mean, and what does it signal?",
         "opts": [
             "&lsquo;Complete&rsquo; — nothing more is said elsewhere",
             "&lsquo;In brief&rsquo; — signaling that a fuller version follows immediately at AN 5.2",
             "&lsquo;Secret&rsquo; — the teaching is withheld from most listeners",
             "&lsquo;Repeated&rsquo; — the discourse restates an earlier one"],
         "correct": 1,
         "expl": "Its companion discourse, titled &lsquo;Vitthata&rsquo;, does the expanding."},
        {"q": "Which two items does this five-list have that the standard five faculties/powers "
              "(faith, energy, mindfulness, immersion, wisdom) do not?",
         "opts": [
             "Ethics and freedom",
             "Conscience and prudence, replacing mindfulness and immersion",
             "Patience and generosity",
             "Nothing — the two lists are identical"],
         "correct": 1,
         "expl": "First flagged at AN 4.163, three chapters and one nipāta back."},
        {"q": "Where in this series was <em>hiri</em> and <em>ottappa</em>&rsquo;s role as "
              "&lsquo;world-protectors&rsquo; already established?",
         "opts": [
             "AN 3.65, the reference page for this whole series",
             "AN 2.1&ndash;10, at AN 2.9",
             "AN 1.616&ndash;627",
             "It has not appeared before this page"],
         "correct": 1,
         "expl": "AN 2.9 argued that without the pair, ordinary social bonds would collapse."},
        {"q": "What does &lsquo;sekha&rsquo; mean?",
         "opts": [
             "One who has completed the path",
             "One who has entered the path but not yet completed it",
             "A lay follower who has not yet ordained",
             "A synonym for the Buddha himself"],
         "correct": 1,
         "expl": "A term of the path&rsquo;s middle — neither beginner nor finished."},
        {"q": "What form does AN 5.1 take?",
         "opts": [
             "An extended simile followed by verses",
             "A single sentence naming the five, and a single sentence of injunction to train",
             "A dialogue between the Buddha and a wanderer",
             "A list of ten qualities with definitions for each"],
         "correct": 1,
         "expl": "No elaboration — that is left to what follows."},
        {"q": "What does the discourse instruct listeners to do with the five powers?",
         "opts": [
             "Avoid them until fully ordained",
             "Train so as to come to have them",
             "Debate their meaning with other mendicants",
             "Memorize them in Pāli only"],
         "correct": 1,
         "expl": "&lsquo;So you should train like this&rsquo; — a direct injunction, not a description."},
        {"q": "Where is AN 5.1 set?",
         "opts": [
             "Rājagaha, on Vulture&rsquo;s Peak",
             "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery",
             "Kapilavatthu, among the Sakyans",
             "Vesālī, in the Great Wood"],
         "correct": 1,
         "expl": "The setting most Aṅguttara discourses default to when nothing more specific is named."},
        {"q": "How does AN 5.1 relate to the discourse immediately following it?",
         "opts": [
             "They are unrelated, on separate topics",
             "AN 5.2 expands each of the same five powers in turn, matching its title &lsquo;In Detail&rsquo;",
             "AN 5.2 contradicts the list given here",
             "AN 5.2 belongs to a different chapter entirely"],
         "correct": 1,
         "expl": "A brief-then-detailed pair, meant to be read together."},
        {"q": "Why does the guide caution against treating &lsquo;sekhabala&rsquo; as simply another "
              "name for the well-known five faculties?",
         "opts": [
             "Because the two lists share no terms at all",
             "Because it is a distinct list sharing three of five terms with the faculties, not an "
             "alternate label for the same set",
             "Because the five faculties are a Northern-only concept",
             "Because sekhabala only has four items"],
         "correct": 1,
         "expl": "Two different technical sets under related names — worth noticing, not worth conflating."},
    ],
    marginalia=[
        ("The five", [
            "<span class=\"pali\">saddhā</span>faith",
            "<span class=\"pali\">hiri</span>conscience",
            "<span class=\"pali\">ottappa</span>prudence",
            "<span class=\"pali\">vīriya</span>energy",
            "<span class=\"pali\">paññā</span>wisdom",
        ]),
        ("Not the same five", [
            "faculties/powers:",
            "faith, energy,",
            "mindfulness, immersion, wisdom",
        ]),
        ("Brief, then detailed", [
            "<span class=\"pali\">saṅkhitta</span>this page",
            "<span class=\"pali\">vitthata</span>the next",
        ]),
        ("Cross-references", [
            "AN 4.163 &middot; this list, first met",
            "AN 2.9 &middot; hiri &amp; ottappa in full",
            "AN 5.2 &middot; next, expanded",
        ]),
    ],
    further=[
        '<a href="%s/an5.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.2.html">AN 5.2 &middot; In Detail</a> &mdash; next, and this discourse&rsquo;s '
        "own expansion, defining each of the five in turn.",
        '<a href="an-4.163.html">AN 4.163 &middot; Ugly</a> &mdash; where this same five-item list '
        "first appeared in this series, alongside the differently-composed five faculties.",
        '<a href="an-2.1-10.html">AN 2.1&ndash;10</a> &mdash; AN 2.9, where conscience and prudence '
        "were first called the world&rsquo;s protectors.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.2 — Vitthatasutta
# --------------------------------------------------------------------------- #
page(
    2, "Vitthata", "In Detail",
    meta_title="AN 5.2 — In Detail | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vitthatasutta, which "
        "expands AN 5.1&rsquo;s bare list of five powers — faith, conscience, prudence, energy, wisdom "
        "— into five fixed definitions, one of them the canon&rsquo;s standard formula for recollecting "
        "the Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The same five named again, then each defined in turn by a short fixed formula, "
                 "closing with the same injunction to train as AN 5.1"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The individual definitions — especially the nine-quality recollection "
                              "of the Buddha — are pan-canonical formulas found across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; five short definitions, one of "
                       "them a formula already met elsewhere in this series"),
    ],
    why=(
        "AN 5.1 named five powers and said nothing about what any of them meant. This discourse "
        "keeps the promise its own title makes: <em>vitthata</em>, in detail. Each of the five gets "
        "one paragraph, in the same order, closed by the same phrase &mdash; <em>this is called "
        "the power of</em> &mdash; four times over before the pattern breaks for wisdom. Read next "
        "to AN 5.1, the pair shows a working method the collection uses repeatedly: state a list "
        "bare, then state it again with the content filled in."),
    guide=[
        ("The teaching in one sentence", [
            "Faith is recollecting the Buddha&rsquo;s nine qualities; conscience and prudence are "
            "shame and dread at bad conduct, worded identically apart from the one term that names "
            "each; energy is effort aimed at giving up the unskillful and taking up the skillful; "
            "wisdom here is specifically insight into arising and passing away."]),
        ("Faith, defined by its object", [
            "The power of faith is not defined as a feeling of confidence in general. It is defined "
            "as <em>recollecting</em> a fixed list: the Realized One is <em>perfected, a fully "
            "awakened Buddha, accomplished in knowledge and conduct, holy, knower of the world, "
            "supreme guide for those fit for training, teacher of gods and humans, awakened, "
            "blessed</em>. Nine epithets, recited as a unit.",
            "This exact formula, <em>buddhānussati</em>, already has its own glossary entry at "
            "<a href=\"an-1.296-305.html\">AN 1.296&ndash;305</a>, where it is one of ten objects of "
            "recollection. What is worth adding here is what AN 5.2 does with it: faith is not left "
            "as an undefined mood but is tied to a specific, memorizable object, so that "
            "&ldquo;having faith&rdquo; becomes something a person can check &mdash; do I hold these "
            "nine in mind, or not &mdash; rather than something only felt."]),
        ("Conscience and prudence, worded as a matched pair", [
            "The two definitions are built from the same sentence with one word changed. Both "
            "concern <em>kāyaduccarita, vacīduccarita, manoduccarita</em> &mdash; bad conduct by "
            "body, speech, and mind &mdash; and both concern acquiring any bad, unskillful "
            "qualities. The only difference between them on the page is <em>hirīyati</em> versus "
            "<em>ottappati</em>: is conscientious about, is prudent regarding.",
            "AN 5.1&rsquo;s guide already pointed to <a href=\"an-2.1-10.html\">AN 2.9</a> for the "
            "fuller distinction between the two &mdash; shame that looks inward against dread that "
            "looks outward. This discourse does not draw that distinction itself; it simply gives "
            "both the identical scope and lets the reader supply, from what was already established, "
            "why one word is not simply a synonym for the other."]),
        ("Energy, defined by direction", [
            "The power of energy is not effort in the abstract. It has a stated direction: roused "
            "up <em>for giving up unskillful qualities and embracing skillful qualities</em>. The "
            "formula then adds three intensifiers &mdash; strong, staunchly vigorous, not slacking "
            "off &mdash; but the direction comes first in the sentence and does the defining work. "
            "A person could work very hard at the wrong thing; this definition rules that reading "
            "out before it can arise."]),
        ("Wisdom, defined narrowly", [
            "Of the five, wisdom gets the most restrictive definition. It is not learning, or "
            "cleverness, or doctrinal knowledge. It is specifically <em>the wisdom of arising and "
            "passing away which is noble, penetrative, and leads to the complete ending of "
            "suffering</em> &mdash; insight into how conditioned things come to be and cease, aimed "
            "in one direction only.",
            "This narrowing matters for how to read the rest of the chapter. When later discourses "
            "in the Fives speak of a mendicant being &lsquo;witless&rsquo; or &lsquo;wise&rsquo;, "
            "the specific insight named here is the standard the word is quietly measured against, "
            "not general intelligence."]),
        ("What the chapter does with this now", [
            "Having filled in all five, the discourse closes with the identical injunction AN 5.1 "
            "used: train so as to have them. From here the chapter turns to consequences &mdash; "
            "what happens, in this life and the next, to a mendicant who has these five or lacks "
            "them &mdash; which is where AN 5.3 begins."]),
    ],
    terms=[
        ("buddhānussati",
         "&ldquo;recollection of the Buddha&rdquo; &mdash; the nine-quality formula that defines the "
         "power of faith here, already given its own entry at AN 1.296&ndash;305."),
        ("hirībalaṁ",
         "&ldquo;power of conscience&rdquo; &mdash; shame at bad conduct of body, speech, and mind, "
         "and at acquiring unskillful qualities generally."),
        ("ottappabalaṁ",
         "&ldquo;power of prudence&rdquo; &mdash; worded identically to conscience apart from the one "
         "verb; the outward-facing partner AN 2.9 calls its co-protector of the world."),
        ("āraddhavīriya",
         "&ldquo;energy roused up&rdquo; &mdash; effort defined by its direction, toward giving up "
         "the unskillful and taking up the skillful, before its intensity is even mentioned."),
        ("udayatthagāminī paññā",
         "&ldquo;wisdom leading to arising and passing away&rdquo; &mdash; the specific, narrow sense "
         "of wisdom this discourse uses: insight, not learning or cleverness."),
    ],
    text_intro=(
        "The discourse in full: the five named again, then each defined in turn, closing with the "
        "same injunction to train. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five, named again"),
        ("p", "&sect;1", "an5.2:1.1-1.3"),
        ("h3", "The power of faith"),
        ("p", "&sect;2", "an5.2:2.1-2.4"),
        ("h3", "The power of conscience"),
        ("p", "&sect;3", "an5.2:3.1-3.3"),
        ("h3", "The power of prudence"),
        ("p", "&sect;4", "an5.2:4.1-4.3"),
        ("h3", "The power of energy"),
        ("p", "&sect;5", "an5.2:5.1-5.3"),
        ("h3", "The power of wisdom"),
        ("p", "&sect;6", "an5.2:6.1-6.4"),
        ("h3", "The injunction"),
        ("p", "&sect;7", "an5.2:7.1-7.3"),
    ],
    quiz=[
        {"q": "How does AN 5.2 define the power of faith?",
         "opts": [
             "As a general feeling of confidence",
             "As recollecting a fixed nine-quality formula describing the Realized One",
             "As belief without any specific content",
             "As trust in one&rsquo;s teacher personally"],
         "correct": 1,
         "expl": "The same buddhānussati formula already glossed at AN 1.296–305."},
        {"q": "What single word changes between the definitions of conscience and prudence?",
         "opts": [
             "Nothing changes — the two definitions are word-for-word identical",
             "Only the verb — hirīyati versus ottappati — while the scope named is the same",
             "Conscience concerns speech only; prudence concerns the body only",
             "Conscience is about laypeople; prudence is about mendicants"],
         "correct": 1,
         "expl": "Both concern bad conduct of body, speech, and mind, and unskillful qualities generally."},
        {"q": "Where was the fuller distinction between conscience and prudence already drawn in "
              "this series?",
         "opts": [
             "It has never been drawn anywhere in this series",
             "AN 2.9, on shame that looks inward against dread that looks outward",
             "AN 5.2 itself draws it in full",
             "AN 4.163"],
         "correct": 1,
         "expl": "AN 5.2 gives both definitions identical scope and leaves the distinction to what was already established."},
        {"q": "How does the discourse define the power of energy?",
         "opts": [
             "As raw physical stamina",
             "By its direction first — roused up for giving up the unskillful and embracing the "
             "skillful — with intensity added after",
             "As effort applied to any goal whatsoever",
             "As the ability to work without rest"],
         "correct": 1,
         "expl": "Direction comes first in the sentence and does the defining work."},
        {"q": "How is the power of wisdom defined here?",
         "opts": [
             "As broad general intelligence",
             "As doctrinal learning and memorized teachings",
             "Specifically as insight into arising and passing away, leading to the ending of suffering",
             "As skill in debate"],
         "correct": 2,
         "expl": "A narrow, specific sense of wisdom — not cleverness in general."},
        {"q": "Why does the guide say this narrow definition of wisdom matters for reading the rest "
              "of the chapter?",
         "opts": [
             "It doesn&rsquo;t &mdash; the definition is never used again",
             "Later talk of a mendicant being 'wise' or 'witless' is measured against this specific "
             "insight, not general intelligence",
             "It means only monks who have memorized scripture count as wise",
             "It applies only to this single discourse"],
         "correct": 1,
         "expl": "The standard set here is the quiet measure for later discourses in the chapter."},
        {"q": "How many discrete qualities make up the buddhānussati formula used to define faith?",
         "opts": ["Four", "Seven", "Nine", "Ten"],
         "correct": 2,
         "expl": "Perfected, fully awakened, accomplished in knowledge and conduct, holy, knower of the world, supreme guide, teacher of gods and humans, awakened, blessed."},
        {"q": "What does AN 5.2 close with?",
         "opts": [
             "A new list of five different qualities",
             "The identical injunction to train that closed AN 5.1",
             "A prediction of the questioner&rsquo;s future rebirth",
             "A refusal to answer further questions"],
         "correct": 1,
         "expl": "The pair of discourses share the same closing formula, not only the same list."},
        {"q": "What working method do AN 5.1 and AN 5.2 together demonstrate?",
         "opts": [
             "Stating a list bare, then restating it with the content filled in",
             "Two unrelated teachings placed side by side by coincidence",
             "A question-and-answer dialogue format",
             "A dispute between two schools resolved by the Buddha"],
         "correct": 0,
         "expl": "A method this reading guide flags because it recurs across the collection."},
        {"q": "What does the chapter turn to once both AN 5.1 and AN 5.2 have established the list?",
         "opts": [
             "A different list of five entirely",
             "Consequences — what happens to a mendicant who has, or lacks, these five qualities",
             "The end of the nipāta",
             "A debate with a rival teacher"],
         "correct": 1,
         "expl": "Beginning at AN 5.3, the very next discourse."},
    ],
    marginalia=[
        ("Five, defined", [
            "faith &mdash; nine epithets recalled",
            "conscience/prudence &mdash; matched pair",
            "energy &mdash; direction first",
            "wisdom &mdash; arising &amp; passing only",
        ]),
        ("The nine epithets", [
            "perfected, awakened,",
            "accomplished, holy,",
            "knower, guide, teacher,",
            "awakened, blessed",
        ]),
        ("One word apart", [
            "<span class=\"pali\">hirīyati</span>is conscientious",
            "<span class=\"pali\">ottappati</span>is prudent",
            "&mdash; everything else, identical",
        ]),
        ("Cross-references", [
            "AN 5.1 &middot; the bare list, first",
            "AN 1.296&ndash;305 &middot; buddhānussati in full",
            "AN 5.3 &middot; next: the stakes",
        ]),
    ],
    further=[
        '<a href="%s/an5.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; the previous discourse, and this '
        "one&rsquo;s own compressed original.",
        '<a href="an-1.296-305.html">AN 1.296&ndash;305</a> &mdash; the full ten objects of '
        "recollection, including the nine-quality formula used here to define faith.",
        '<a href="an-5.3.html">AN 5.3 &middot; Suffering</a> &mdash; next, where the chapter turns '
        "from defining the five to their consequences.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.3 — Dukkhasutta
# --------------------------------------------------------------------------- #
page(
    3, "Dukkha", "Suffering",
    meta_title="AN 5.3 — Suffering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dukkhasutta — the first "
        "consequence attached to the five powers of a trainee: lacking them means living unhappily "
        "now and a bad rebirth later; having them means the reverse. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Two mirror-image statements — five qualities absent, then the same five present "
                 "— each naming a this-life and a next-life consequence"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The pairing of present unhappiness with future bad rebirth is a "
                              "standard formula found widely in the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short and formulaic, but the "
                       "first discourse in the chapter to state stakes rather than definitions"),
    ],
    why=(
        "AN 5.1 and 5.2 said what the five powers are. AN 5.3 is the first to say what having or "
        "lacking them costs. The cost is stated in two parts, and both parts matter: a present-life "
        "condition &mdash; distress, anguish, fever, or their absence &mdash; and a next-life "
        "expectation, a bad or good rebirth. The discourse does not wait until death to make its "
        "point; it claims the difference is already felt now, in how a mendicant&rsquo;s days go."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant lacking faith, conscience, prudence, energy, and wisdom lives now with "
            "distress, anguish, and fever and can expect a bad rebirth; one who has all five lives "
            "now without them and can expect a good rebirth."]),
        ("Three words, kept together", [
            "The present-life half of the formula is not just &lsquo;unhappily&rsquo;; the Pāli "
            "gives three terms together &mdash; <em>savighātaṁ saupāyāsaṁ sapariḷāhaṁ</em>, with "
            "distress, with anguish, with fever &mdash; and Sujato keeps all three rather than "
            "collapsing them into one English word. The repetition is doing work: this is not a mild "
            "discomfort but a compounding one, named three ways so that no single English "
            "translation of the first term lets the reader round it down."]),
        ("Two timeframes, not one", [
            "It would be easy to read this discourse as being about karma and future rebirth alone, "
            "since that is the more dramatic half. But the sentence opens with "
            "<em>diṭṭheva dhamme</em>, &lsquo;in this very life&rsquo;, before it ever reaches "
            "the next one. The discourse insists on a present cost, felt inside the years a person is "
            "actually living, and only then adds the further one. Reading past the first half to get "
            "to the second misses half of what is being claimed."]),
        ("The list, again, doing no new work", [
            "The five qualities named here are the identical five from AN 5.1 and 5.2, worded the "
            "same way &mdash; faithless, shameless, imprudent, lazy, witless against their "
            "opposites. This discourse adds no new definition of any of them; its only contribution "
            "is the consequence attached. That is worth naming plainly rather than re-explaining the "
            "five again, since AN 5.2 already did that work in full."]),
        ("A pattern the chapter will repeat", [
            "This discourse, its five-quality list, and its two mirror-image halves establish a "
            "template AN 5.4, 5.8, 5.9, and 5.10 will all reuse with small variations: the same "
            "wording for lacking or having the five, attached each time to a different consequence. "
            "Reading them as variations on one template, rather than as five separate arguments, is "
            "the efficient way through the rest of this chapter."]),
    ],
    terms=[
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; this discourse&rsquo;s title, and the general condition "
         "the three-part present-life formula spells out in specific terms."),
        ("savighāta",
         "&ldquo;with distress&rdquo; &mdash; the first of three terms describing the present cost "
         "of lacking the five powers, kept distinct from the other two rather than merged."),
        ("saupāyāsa",
         "&ldquo;with anguish&rdquo; &mdash; the second of the three; a mental rather than physical "
         "term, paired with the physical <em>sapariḷāha</em>."),
        ("sapariḷāha",
         "&ldquo;with fever&rdquo; &mdash; the third of the three, a burning quality carried over "
         "from ordinary physical fever into a description of mental state."),
        ("diṭṭheva dhamme",
         "&ldquo;in this very life&rdquo; &mdash; the phrase that opens both halves of the formula, "
         "marking the discourse&rsquo;s claim as present, not only about a future rebirth."),
    ],
    text_intro=(
        "The discourse in full: the five qualities absent, with their present and future cost, then "
        "the same five present, with the reverse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Lacking the five"),
        ("p", "&sect;1", "an5.3:1.1-1.4"),
        ("h3", "Having the five"),
        ("p", "&sect;2", "an5.3:2.1-2.4"),
    ],
    quiz=[
        {"q": "What two kinds of consequence does AN 5.3 attach to the five powers?",
         "opts": [
             "Only a future rebirth, nothing about the present",
             "A present-life condition of distress or ease, and a future rebirth, good or bad",
             "Only social reputation among other mendicants",
             "Only physical health"],
         "correct": 1,
         "expl": "Diṭṭheva dhamme, 'in this very life', opens both halves before either reaches rebirth."},
        {"q": "What three Pāli terms describe the present-life cost of lacking the five powers?",
         "opts": [
             "Distress, anguish, and fever, kept as three distinct terms",
             "A single word meaning 'unhappiness'",
             "Sickness, poverty, and isolation",
             "Fear, anger, and grief"],
         "correct": 0,
         "expl": "Savighāta, saupāyāsa, sapariḷāha — three terms, not collapsed into one."},
        {"q": "What five qualities does AN 5.3 use, and how do they compare to AN 5.1 and 5.2's list?",
         "opts": [
             "A new, unrelated set of five",
             "The identical five from AN 5.1 and 5.2 — faith, conscience, prudence, energy, wisdom "
             "— with no new definition given",
             "Only three of the original five, with two dropped",
             "The five faculties, not the powers of a trainee"],
         "correct": 1,
         "expl": "AN 5.3 adds a consequence, not a new definition — that work was already done at AN 5.2."},
        {"q": "Why does the guide caution against reading this discourse as only about future rebirth?",
         "opts": [
             "Because it says nothing about rebirth at all",
             "Because the sentence opens by claiming a present-life cost before it ever reaches the "
             "next life",
             "Because rebirth is a later addition to the text",
             "Because the discourse only concerns lay listeners"],
         "correct": 1,
         "expl": "Diṭṭheva dhamme comes first in the sentence, and does real work."},
        {"q": "What happens to a mendicant who has all five powers, according to this discourse?",
         "opts": [
             "They live now without distress, anguish, or fever, and can expect a good rebirth",
             "They are guaranteed enlightenment in this life",
             "They become immune to physical illness",
             "Nothing changes for them either way"],
         "correct": 0,
         "expl": "The exact mirror image of the negative half."},
        {"q": "What later discourses in this chapter reuse this same mirror-image template?",
         "opts": [
             "None — AN 5.3's structure is unique in the chapter",
             "AN 5.4, 5.8, 5.9, and 5.10, each attaching a different consequence to the same "
             "lacking/having pattern",
             "Only AN 5.4",
             "The whole of AN 5.11–20"],
         "correct": 1,
         "expl": "A template worth recognizing rather than re-reading as five separate arguments."},
        {"q": "What does 'sapariḷāha' literally carry over from ordinary usage?",
         "opts": [
             "A burning quality, from physical fever into a mental description",
             "A reference to cold, not heat",
             "A term for physical hunger",
             "A term used only for describing weather"],
         "correct": 0,
         "expl": "Fever&rsquo;s heat, applied to a state of mind."},
        {"q": "Does AN 5.3 offer a simile or story to illustrate its claim?",
         "opts": [
             "Yes, an extended parable",
             "No — it states both halves directly, with no narrative framing",
             "Yes, a dialogue with a named questioner",
             "Yes, a set of verses"],
         "correct": 1,
         "expl": "Consistent with the terse, formulaic character of this discourse."},
        {"q": "What is the effect of keeping distress, anguish, and fever as three separate terms "
              "rather than one English word?",
         "opts": [
             "It has no effect; the terms are synonyms with no distinction",
             "It signals a compounding, layered unhappiness rather than a single mild discomfort",
             "It shows the text is corrupted",
             "It indicates three different mendicants are being described"],
         "correct": 1,
         "expl": "Three named terms resist being rounded down to something milder."},
        {"q": "What is the setting of AN 5.3?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — it continues from AN 5.1's setting at Sāvatthī",
             "Rājagaha",
             "Vesālī"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("The formula", [
            "lack the five &rarr;",
            "distress now, bad rebirth",
            "have the five &rarr;",
            "ease now, good rebirth",
        ]),
        ("Three, not one", [
            "<span class=\"pali\">savighāta</span>distress",
            "<span class=\"pali\">saupāyāsa</span>anguish",
            "<span class=\"pali\">sapariḷāha</span>fever",
        ]),
        ("Two timeframes", [
            "<span class=\"pali\">diṭṭheva dhamme</span>this very life",
            "then, separately,",
            "the next rebirth",
        ]),
        ("Cross-references", [
            "AN 5.2 &middot; the five, defined",
            "AN 5.4 &middot; next: same template",
            "AN 5.8&ndash;10 &middot; the template again",
        ]),
    ],
    further=[
        '<a href="%s/an5.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.2.html">AN 5.2 &middot; In Detail</a> &mdash; the previous discourse, where '
        "the five qualities this page names were fully defined.",
        '<a href="an-5.4.html">AN 5.4 &middot; Cast Down</a> &mdash; next, restating the same '
        "template with a more vivid image of the same two destinies.",
        '<a href="an-5.8.html">AN 5.8 &middot; Failure</a> &mdash; later in the chapter, the same '
        "lacking/having pattern applied to a mendicant&rsquo;s standing in the teaching itself.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.4 — Yathābhatasutta
# --------------------------------------------------------------------------- #
page(
    4, "Yathābhata", "Cast Down",
    meta_title="AN 5.4 — Cast Down | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Yathābhatasutta — the "
        "same five powers restated with a vivid image: a mendicant lacking or having them is "
        "placed in hell or heaven as if delivered there, package and destination already matched. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The identical lacking/having template from AN 5.3, with a new image replacing "
                 "the present-life/rebirth pairing"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The 'carried and set down' image for karmic destination recurs "
                              "across early Buddhist literature broadly; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and its single image "
                       "carries the whole discourse"),
    ],
    why=(
        "Where AN 5.3 spoke of a present condition and a future expectation, AN 5.4 compresses both "
        "into one picture: <em>yathābhataṁ nikkhitto</em>, carried and set down exactly so &mdash; "
        "the way a parcel is delivered to the one address it was addressed to, no detour possible. "
        "A mendicant lacking the five powers is placed in hell as if delivered there; one who has "
        "them is placed in heaven the same way. The image does the discourse&rsquo;s entire "
        "argument in four words."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant lacking the five powers is placed in hell as if delivered there; one who "
            "has all five is placed in heaven as if delivered there &mdash; the identical five "
            "qualities from every discourse so far in this chapter."]),
        ("The image itself", [
            "<em>Yathābhataṁ nikkhitto</em> is a delivery image: something carried and put down "
            "exactly where it was being carried to. It removes any sense of a journey, a trial, or "
            "a weighing of the evidence at the end. The destination was already fixed by what was "
            "being carried; arrival simply confirms it.",
            "This is a stronger claim than AN 5.3&rsquo;s &lsquo;can be expected&rsquo; "
            "(<em>pāṭikaṅkhā</em>), which leaves room for expectation to be an estimate. "
            "&lsquo;Placed as if delivered&rsquo; leaves none. The two discourses are not "
            "contradictory &mdash; both attach the same outcome to the same causes &mdash; but this "
            "one states it with more force."]),
        ("Hell and heaven, named without elaboration", [
            "Neither destination is described here. There is no picture of what hell or heaven "
            "contains, no duration given, no geography. The discourse is entirely about the "
            "mechanism &mdash; the fact of a match between quality and destination &mdash; and "
            "leaves every question about what either place is like to be answered, if at all, "
            "elsewhere in the canon. A reading guide should resist filling in what the text itself "
            "declines to specify."]),
        ("The list, unchanged a third time", [
            "This is now the third discourse in the chapter &mdash; after AN 5.1 and 5.3 &mdash; to "
            "use the identical five terms, faithless, shameless, imprudent, lazy, witless, against "
            "their five opposites. No discourse so far has varied the list itself; each varies only "
            "what is said to follow from it. That consistency is worth noticing as a feature, not "
            "an accident: the chapter is building confidence in one fixed list by attaching it to "
            "consequence after consequence."]),
        ("What is still to come", [
            "AN 5.5 turns from a cosmic destination to a social one &mdash; not where a person is "
            "reborn, but what other mendicants are entitled to say about someone who disrobes, or "
            "who endures. The image changes from a parcel delivered to a courtroom of one&rsquo;s "
            "peers, but the same five qualities remain the deciding factor."]),
    ],
    terms=[
        ("yathābhataṁ nikkhitto",
         "&ldquo;placed as if carried and set down there&rdquo; &mdash; the discourse&rsquo;s "
         "central image, a delivery with no possible detour between carrying and arrival."),
        ("niraya",
         "&ldquo;hell&rdquo; &mdash; named as a destination here without any description of what "
         "it contains; the text declines to elaborate."),
        ("sagga",
         "&ldquo;heaven&rdquo; &mdash; the positive destination, equally undescribed, matched "
         "here to having all five powers."),
        ("pāṭikaṅkhā",
         "&ldquo;can be expected&rdquo; &mdash; the softer verb AN 5.3 used for the same outcome; "
         "AN 5.4&rsquo;s delivery image states the same claim with more force."),
        ("assaddho",
         "&ldquo;faithless&rdquo; &mdash; the first of the five negative terms, identical in "
         "wording across every discourse in this chapter so far."),
    ],
    text_intro=(
        "The discourse in full: lacking the five, placed in hell as if delivered there; having "
        "them, placed in heaven the same way. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Lacking the five"),
        ("p", "&sect;1", "an5.4:1.1-1.4"),
        ("h3", "Having the five"),
        ("p", "&sect;2", "an5.4:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does the image &lsquo;yathābhataṁ nikkhitto&rsquo; convey?",
         "opts": [
             "Something carried and put down exactly where it was already being carried to, with no "
             "possible detour",
             "A slow, uncertain journey with an unknown ending",
             "A trial with witnesses and a judge",
             "A gift given freely, without cause"],
         "correct": 0,
         "expl": "A delivery image — destination fixed before arrival, arrival only confirming it."},
        {"q": "How does this discourse&rsquo;s claim compare in force to AN 5.3&rsquo;s &lsquo;can be expected&rsquo; "
              "(pāṭikaṅkhā)?",
         "opts": [
             "It is weaker and more hedged",
             "It is stronger &mdash; &lsquo;placed as if delivered&rsquo; leaves no room for estimate",
             "The two discourses make contradictory claims",
             "There is no difference between them"],
         "correct": 1,
         "expl": "Both attach the same outcome to the same causes; this one states it with more force."},
        {"q": "How much detail does AN 5.4 give about what hell and heaven actually contain?",
         "opts": [
             "Extensive, multi-paragraph descriptions of each",
             "None — both are named without any description of duration, geography, or contents",
             "Only heaven is described; hell is left blank",
             "Only hell is described; heaven is left blank"],
         "correct": 1,
         "expl": "The discourse is entirely about the mechanism, not the destinations' contents."},
        {"q": "How many discourses in this chapter, counting AN 5.4, have now used the identical "
              "five-quality list (faithless, shameless, imprudent, lazy, witless) against its "
              "opposites?",
         "opts": ["One", "Two", "Three — AN 5.1, 5.3, and 5.4", "All ten"],
         "correct": 2,
         "expl": "The list stays fixed; only the attached consequence changes each time."},
        {"q": "What does the guide suggest is the chapter&rsquo;s strategy in repeating the same list "
              "across multiple discourses?",
         "opts": [
             "A copying error in transmission",
             "Building confidence in one fixed list by attaching it to consequence after consequence",
             "Testing whether listeners were paying attention",
             "There is no discernible strategy"],
         "correct": 1,
         "expl": "Consistency treated as a deliberate feature, not an accident."},
        {"q": "What does AN 5.5, the next discourse, shift the consequence to?",
         "opts": [
             "A different cosmic destination",
             "A social one — what fellow mendicants are entitled to say about someone who disrobes "
             "or who endures",
             "A financial penalty",
             "Nothing — AN 5.5 repeats AN 5.4 exactly"],
         "correct": 1,
         "expl": "The image changes from parcel to courtroom of one&rsquo;s peers; the five qualities stay the deciding factor."},
        {"q": "Is a simile or extended story used to make this discourse&rsquo;s point?",
         "opts": [
             "Yes, an extended parable about a nursemaid",
             "No — a single compressed image carries the entire argument",
             "Yes, a dialogue with a heavenly being",
             "Yes, a set of closing verses"],
         "correct": 1,
         "expl": "Four words, &lsquo;placed as if delivered&rsquo;, do the whole discourse&rsquo;s work."},
        {"q": "What five qualities are absent in the mendicant placed in hell?",
         "opts": [
             "Generosity, ethics, patience, energy, wisdom",
             "Faith, conscience, prudence, energy, wisdom",
             "Mindfulness, immersion, faith, energy, wisdom",
             "Ethics, immersion, wisdom, freedom"],
         "correct": 1,
         "expl": "The sekhabala list, unchanged from AN 5.1."},
        {"q": "How does the reading guide caution against reading this discourse?",
         "opts": [
             "By encouraging speculation about what hell and heaven actually look like",
             "By resisting the urge to fill in what the text itself declines to specify",
             "By treating hell and heaven as purely metaphorical with no textual basis",
             "By assuming this discourse contradicts AN 5.3"],
         "correct": 1,
         "expl": "The text is silent on contents and duration, and the guide follows that silence."},
        {"q": "Where is AN 5.4 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Bamboo Grove near Rājagaha",
             "Kapilavatthu"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("The image", [
            "<span class=\"pali\">yathābhataṁ nikkhitto</span>",
            "carried, set down &mdash;",
            "exactly where addressed",
        ]),
        ("Stronger than AN 5.3", [
            "AN 5.3: can be expected",
            "AN 5.4: placed, as delivered",
            "same claim, more force",
        ]),
        ("Undescribed", [
            "<span class=\"pali\">niraya</span>hell",
            "<span class=\"pali\">sagga</span>heaven",
            "&mdash; contents left unstated",
        ]),
        ("Cross-references", [
            "AN 5.3 &middot; the softer version",
            "AN 5.1 &middot; the list, unchanged",
            "AN 5.5 &middot; next: a social courtroom",
        ]),
    ],
    further=[
        '<a href="%s/an5.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.3.html">AN 5.3 &middot; Suffering</a> &mdash; the previous discourse, whose '
        "softer &lsquo;can be expected&rsquo; this page restates with more force.",
        '<a href="an-5.5.html">AN 5.5 &middot; Disrobing</a> &mdash; next, shifting the same five '
        "qualities from a cosmic destination to a social judgment.",
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; where this chapter&rsquo;s fixed '
        "five-quality list first appeared.",
    ],
)



# --------------------------------------------------------------------------- #
# AN 5.5 — Sikkhāsutta
# --------------------------------------------------------------------------- #
page(
    5, "Sikkhā", "Disrobing",
    meta_title="AN 5.5 — Disrobing | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sikkhāsutta — the same "
        "five powers turned to a social judgment: legitimate grounds for criticizing a monk or nun "
        "who disavows the training, and for praising one who endures the holy life in pain and "
        "tears. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Two mirror-image cases — someone who disrobes, and someone who perseveres in "
                 "visible distress — each assessed against the same five qualities"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Formal grounds for criticism and praise of monastics attached to "
                              "fixed criteria recur across Vinaya-adjacent literature broadly; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the first discourse in the "
                       "chapter to picture ordinary monastic life without softening it"),
    ],
    why=(
        "This discourse does something the three before it did not: it admits, without flinching, "
        "that the full and pure spiritual life can be lived <em>in pain and sadness, weeping, with "
        "tearful face</em>. That is not a description of failure. It is the discourse&rsquo;s "
        "picture of someone who deserves praise on five legitimate grounds. AN 5.5 is worth reading "
        "slowly for that reason alone: it refuses to make endurance look easy, and refuses equally "
        "to let disrobing look like a private matter with no legitimate commentary attached."),
    guide=[
        ("The teaching in one sentence", [
            "A monk or nun who disavows the training deserves rebuttal and criticism on five "
            "legitimate grounds &mdash; having lacked faith, conscience, prudence, energy, and "
            "wisdom; one who lives the full and pure spiritual life through pain and tears deserves "
            "praise on the same five grounds, for having had them."]),
        ("What &lsquo;legitimate grounds&rsquo; means here", [
            "<em>Sahadhammikā vādānupātā</em>, legitimate grounds for criticism, is a specific, "
            "bounded claim. The discourse is not licensing any criticism a mendicant feels like "
            "making; it names exactly what the criticism may consist of &mdash; the five qualities "
            "&mdash; and nothing else. A community that took this discourse seriously would have a "
            "narrower, not a wider, license to comment on someone who has left the training than "
            "one that had not read it."]),
        ("The unflattering half, stated plainly", [
            "The second case is the one worth pausing on. Sujato&rsquo;s translation keeps the "
            "detail intact: <em>in pain and sadness, weeping, with tearful face</em>. This is not "
            "rhetorical exaggeration to make endurance sound impressive; nothing in the passage "
            "suggests the weeping is anything but real distress, genuinely felt.",
            "The discourse does not resolve this into something more comfortable. It simply says "
            "that a person who has all five of these qualities and lives this way, with the "
            "difficulty fully present, deserves praise on five legitimate grounds. Difficulty and "
            "worth are not presented as opposites here; the discourse holds both without "
            "smoothing either one away."]),
        ("Grounds, not outcomes", [
            "Notice what is and is not being judged. The discourse assesses whether the five "
            "qualities were present, not whether the person&rsquo;s life turned out well or badly "
            "by some external measure. Two people could disrobe under very different "
            "circumstances; what this discourse licenses commentary on is only whether faith, "
            "conscience, prudence, energy, and wisdom were there to begin with."]),
        ("Where this fits the chapter so far", [
            "AN 5.3 and 5.4 gave cosmic consequences &mdash; a present condition and a future "
            "rebirth, then hell or heaven pictured as delivery. AN 5.5 is the first to bring the "
            "same five qualities down to the scale of a single human decision and a single human "
            "community&rsquo;s legitimate response to it. The stakes have not shrunk; they have "
            "become immediate."]),
    ],
    terms=[
        ("sikkhaṁ paccakkhāya",
         "&ldquo;disavowing the training&rdquo; &mdash; the formal act of leaving monastic life, "
         "named directly in this discourse&rsquo;s title and opening line."),
        ("hīnāyāvattati",
         "&ldquo;returns to a lesser life&rdquo; &mdash; the standard phrase for returning to lay "
         "life after ordination, carrying an explicit value judgment in the word &lsquo;lesser&rsquo;."),
        ("sahadhammikā vādānupātā",
         "&ldquo;legitimate grounds for criticism&rdquo; &mdash; a bounded, specific license, "
         "naming exactly the five qualities and nothing beyond them."),
        ("pāsaṁsā ṭhānā",
         "&ldquo;grounds for praise&rdquo; &mdash; the positive counterpart, attached to the same "
         "five qualities in someone who endures rather than disrobes."),
        ("assumukho rudamāno",
         "&ldquo;weeping, with tearful face&rdquo; &mdash; the discourse&rsquo;s unsoftened picture "
         "of what enduring the holy life can actually look like."),
    ],
    text_intro=(
        "The discourse in full: legitimate grounds for criticizing one who disavows the training, "
        "and legitimate grounds for praising one who endures it in visible distress. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Disavowing the training"),
        ("p", "&sect;1", "an5.5:1.1-1.4"),
        ("h3", "Enduring the holy life"),
        ("p", "&sect;2", "an5.5:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does AN 5.5 say deserves criticism on five legitimate grounds?",
         "opts": [
             "Any monk or nun the community happens to dislike",
             "A monk or nun who disavows the training and returns to a lesser life, specifically "
             "for having lacked the five powers",
             "Anyone who ever expresses doubt",
             "Only monks, never nuns"],
         "correct": 1,
         "expl": "The discourse addresses both monks and nuns equally, and names exactly five bounded grounds."},
        {"q": "What does 'sahadhammikā vādānupātā' (legitimate grounds for criticism) actually "
              "license, according to the guide?",
         "opts": [
             "Any criticism a mendicant feels like making",
             "A bounded, specific claim naming exactly the five qualities and nothing else",
             "Public shaming without limit",
             "Criticism only from senior mendicants"],
         "correct": 1,
         "expl": "A narrower license than unrestricted commentary, not a wider one."},
        {"q": "How does the discourse describe someone who perseveres in the holy life and deserves "
              "praise?",
         "opts": [
             "As untroubled and serene at all times",
             "As living in pain and sadness, weeping, with tearful face — genuine distress, not "
             "softened",
             "As someone who has already become enlightened",
             "The discourse gives no description at all"],
         "correct": 1,
         "expl": "The guide reads this as an honest, unflattering picture rather than exaggeration."},
        {"q": "What does the guide say about how the discourse handles difficulty and worth "
              "together?",
         "opts": [
             "It treats them as opposites — difficulty proves the person is failing",
             "It holds both without smoothing either away — genuine distress and genuine praise, "
             "at once",
             "It ignores difficulty entirely",
             "It says difficulty disqualifies someone from praise"],
         "correct": 1,
         "expl": "Neither the weeping nor the praise is minimized to make the other easier to accept."},
        {"q": "What exactly is being judged by the five grounds, according to the guide?",
         "opts": [
             "Whether the person's life turned out well by external measures",
             "Whether the five qualities — faith, conscience, prudence, energy, wisdom — were "
             "present, not the outcome",
             "The person's social class before ordaining",
             "How long the person had been ordained"],
         "correct": 1,
         "expl": "Grounds, not outcomes — a distinction the guide draws explicitly."},
        {"q": "How does AN 5.5's scale compare to AN 5.3 and 5.4's?",
         "opts": [
             "Identical in every respect",
             "AN 5.3–5.4 gave cosmic consequences; AN 5.5 brings the same five qualities down to a "
             "single human decision and community response",
             "AN 5.5 is entirely unrelated to the earlier discourses",
             "AN 5.5 concerns only lay followers, not monastics"],
         "correct": 1,
         "expl": "The stakes shift from cosmic to immediate, without shrinking."},
        {"q": "What does 'hīnāyāvattati' mean, and what does its wording carry?",
         "opts": [
             "'Returns to a lesser life' — an explicit value judgment built into the phrase",
             "'Achieves a higher life' — a positive term",
             "A neutral term with no evaluative content",
             "A term used only for laypeople who never ordained"],
         "correct": 0,
         "expl": "The word 'lesser' is part of the standard phrase itself, not an added commentary."},
        {"q": "Does AN 5.5 address monks and nuns equally?",
         "opts": [
             "No, only monks",
             "No, only nuns",
             "Yes — 'bhikkhu vā bhikkhunī vā', monk or nun, in both halves of the discourse",
             "The discourse does not specify"],
         "correct": 2,
         "expl": "Both halves name both explicitly."},
        {"q": "What are the same five qualities used throughout this discourse?",
         "opts": [
             "Generosity, ethics, patience, energy, wisdom",
             "Faith, conscience, prudence, energy, wisdom",
             "Mindfulness, immersion, faith, energy, wisdom",
             "A new list distinct from the rest of the chapter"],
         "correct": 1,
         "expl": "The sekhabala list, unchanged since AN 5.1."},
        {"q": "Where is AN 5.5 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Vesālī, in the Great Wood",
             "The Deer Park at Isipatana"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("Two cases", [
            "disrobes, having lacked &rarr;",
            "criticism, legitimate",
            "endures, having had &rarr;",
            "praise, legitimate",
        ]),
        ("Unsoftened", [
            "<span class=\"pali\">assumukho rudamāno</span>",
            "weeping, tearful face",
            "&mdash; genuine distress, praised",
        ]),
        ("Grounds, not outcomes", [
            "judged: were the five present",
            "not judged: how life turned out",
        ]),
        ("Cross-references", [
            "AN 5.4 &middot; cosmic scale",
            "AN 5.1 &middot; the five, named",
            "AN 5.6 &middot; next: the mechanism",
        ]),
    ],
    further=[
        '<a href="%s/an5.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.4.html">AN 5.4 &middot; Cast Down</a> &mdash; the previous discourse, on the '
        "same five at cosmic scale.",
        '<a href="an-5.6.html">AN 5.6 &middot; Becoming</a> &mdash; next, on how the presence or '
        "absence of these same qualities actually operates.",
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; where this chapter&rsquo;s fixed '
        "five-quality list first appeared.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.6 — Samāpattisutta
# --------------------------------------------------------------------------- #
page(
    6, "Samāpatti", "Becoming",
    meta_title="AN 5.6 — Becoming | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samāpattisutta — the "
        "mechanism behind every consequence claimed so far in this chapter: you don't become "
        "unskillful as long as faith is established, but when it vanishes, unskillfulness moves "
        "in. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Faith stated in full, the same pattern repeated for conscience, prudence, and "
                 "energy in the source's own abbreviation, then wisdom restated in full"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The image of a vacated quality being immediately occupied by its "
                              "opposite is a recurring structural device across early Buddhist "
                              "literature; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, but the first discourse "
                       "in the chapter to state a mechanism rather than an outcome"),
    ],
    why=(
        "Every discourse so far in this chapter has said what follows from having or lacking the "
        "five powers. None has said how the lacking actually happens. AN 5.6 answers that: nothing "
        "is unskillful <em>while</em> a given power is established, and the moment it vanishes, its "
        "named opposite &mdash; faithlessness, shamelessness &mdash; moves into the space left "
        "behind. There is no gap, on this account, between a quality&rsquo;s absence and its "
        "replacement. One occupies the space the instant the other leaves it."),
    guide=[
        ("The teaching in one sentence", [
            "You do not become unskillful as long as a given power &mdash; faith, conscience, "
            "prudence, energy, wisdom &mdash; is established in skillful qualities; but the moment "
            "it vanishes, its named opposite takes over, and unskillfulness follows."]),
        ("A mechanism, not a further outcome", [
            "AN 5.3, 5.4, and 5.5 each attached a consequence &mdash; rebirth, a cosmic destination, "
            "a social judgment &mdash; to having or lacking the five powers, without saying how the "
            "lacking comes about. This discourse fills that gap. It describes a state that holds "
            "<em>as long as</em> (<em>yāva</em>) the power is present, and a transition that occurs "
            "the instant it is not. The other discourses describe destinations; this one describes "
            "the door."]),
        ("No gap between vacancy and occupation", [
            "The verb pair is precise: the quality <em>antarahitā hoti</em>, vanishes, and its "
            "opposite <em>pariyuṭṭhāya tiṭṭhati</em>, takes over and remains standing. There is no "
            "third state in between &mdash; no neutral pause where a mendicant has neither faith "
            "nor faithlessness. The moment one is absent, the discourse says the other is already "
            "in its place."]),
        ("The source's own shorthand", [
            "Bilara&rsquo;s underlying text writes this discourse once in full for faith, then "
            "abbreviates the identical pattern for conscience, prudence, and energy with an "
            "ellipsis, restating only wisdom in full at the close. This page follows that "
            "structure exactly rather than expanding what the source itself compresses: the "
            "first and last of the five are shown whole, and the reader is meant to supply the "
            "middle three by the same pattern, exactly as the source expects."]),
        ("What this sets up", [
            "AN 5.7, immediately following, will use an extended parable &mdash; a nursemaid and "
            "an infant &mdash; to make a related point about ongoing protection until these same "
            "five qualities are complete. Read together, AN 5.6 explains the mechanism by which a "
            "mendicant can slip, and AN 5.7 explains why they are watched over until slipping is no "
            "longer possible."]),
    ],
    terms=[
        ("samāpatti",
         "&ldquo;becoming, arising&rdquo; &mdash; this discourse&rsquo;s title, naming the moment "
         "an unskillful state comes to be."),
        ("yāva",
         "&ldquo;as long as, until&rdquo; &mdash; the word marking the condition under which "
         "unskillfulness does not arise: exactly as long as the power in question is established."),
        ("antarahita",
         "&ldquo;vanished, disappeared&rdquo; &mdash; the verb describing a power&rsquo;s absence, "
         "the trigger for its opposite to take over."),
        ("pariyuṭṭhāya tiṭṭhati",
         "&ldquo;takes over and remains standing&rdquo; &mdash; the verb for what moves into the "
         "vacated space; no gap is described between the two."),
        ("assaddhiya",
         "&ldquo;faithlessness&rdquo; &mdash; the named opposite that takes over the instant faith "
         "vanishes, first of the four negative terms this discourse pairs against the five powers."),
    ],
    text_intro=(
        "The discourse in full: faith stated whole, then wisdom restated whole at the close, "
        "following the source's own abbreviation of the identical pattern for conscience, "
        "prudence, and energy in between. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "As long as faith is established"),
        ("p", "&sect;1", "an5.6:1.1-1.3"),
        ("h3", "The same, for conscience, prudence, energy, and wisdom"),
        ("p", "&sect;2", "an5.6:2.1"),
        ("h3", "Wisdom, restated in full"),
        ("p", "&sect;3", "an5.6:5.2-5.3"),
    ],
    quiz=[
        {"q": "What does AN 5.6 add that AN 5.3–5.5 did not provide?",
         "opts": [
             "A sixth new quality beyond the original five",
             "A mechanism — how the absence of a power actually leads to unskillfulness",
             "A different setting for the discourse",
             "A retraction of the earlier discourses' claims"],
         "correct": 1,
         "expl": "The earlier discourses describe destinations; this one describes the door."},
        {"q": "According to AN 5.6, when does a mendicant not become unskillful?",
         "opts": [
             "Only after full enlightenment",
             "As long as (yāva) the relevant power remains established in skillful qualities",
             "Only while meditating",
             "Never — the discourse claims unskillfulness is unavoidable"],
         "correct": 1,
         "expl": "Yāva marks the condition precisely: exactly as long as the power holds."},
        {"q": "What happens the moment a power like faith vanishes, according to this discourse?",
         "opts": [
             "Nothing changes immediately; there is a long transition period",
             "Its named opposite immediately takes over and remains standing, with no gap between",
             "A different, unrelated power takes its place",
             "The mendicant simply forgets the teaching"],
         "correct": 1,
         "expl": "Antarahitā hoti, vanishes, paired directly with pariyuṭṭhāya tiṭṭhati, takes over and remains."},
        {"q": "How does the source text itself present the pattern for conscience, prudence, and "
              "energy?",
         "opts": [
             "In full, spelled out identically to faith and wisdom",
             "Abbreviated with an ellipsis, since the pattern is identical to the one given in full "
             "for faith",
             "Omitted entirely, with no trace in the source",
             "Replaced with a completely different formula"],
         "correct": 1,
         "expl": "Only faith and wisdom are given in full in the underlying bilara-data text; this page follows that structure."},
        {"q": "What is the effect of showing only faith and wisdom in full, with the middle three "
              "abbreviated?",
         "opts": [
             "It shortens the teaching by dropping content that matters",
             "It follows the source's own compression rather than inventing an expansion not present "
             "in the text",
             "It indicates conscience, prudence, and energy are less important",
             "It is simply an error in this reading guide"],
         "correct": 1,
         "expl": "The reading guide does not invent expanded text the source itself elides."},
        {"q": "What does AN 5.7, the next discourse, do with a related point?",
         "opts": [
             "It repeats AN 5.6 word for word",
             "It uses an extended parable about a nursemaid and an infant to explain protection "
             "until the five qualities are complete",
             "It contradicts AN 5.6's claim about vanishing and takeover",
             "It abandons the five-quality framework entirely"],
         "correct": 1,
         "expl": "AN 5.6 gives the mechanism of slipping; AN 5.7 gives the reason for being watched over."},
        {"q": "Is there a neutral, in-between state described in AN 5.6, where a mendicant has "
              "neither faith nor faithlessness?",
         "opts": [
             "Yes, an extended intermediate stage is described",
             "No — the discourse describes the opposite as occupying the space the instant the "
             "quality is absent",
             "The discourse does not address this question at all",
             "Yes, but only for advanced meditators"],
         "correct": 1,
         "expl": "No third state — vacancy and occupation are treated as simultaneous."},
        {"q": "What is the title 'Samāpatti' usually translated as here?",
         "opts": ["Attainment of jhāna", "Becoming, arising", "Death", "Return"],
         "correct": 1,
         "expl": "The moment an unskillful state comes to be, not a meditative attainment in this context."},
        {"q": "How many of the five powers are shown in full text on this page, versus condensed?",
         "opts": [
             "All five in full",
             "Two in full — faith and wisdom — with conscience, prudence, and energy condensed to a "
             "single line, following the source",
             "None in full; all five are condensed",
             "Only wisdom is shown at all"],
         "correct": 1,
         "expl": "Matching exactly how the underlying bilara-data text itself presents the discourse."},
        {"q": "Where is AN 5.6 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Bamboo Grove",
             "Jeta's Grove is explicitly restated in full"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("The mechanism", [
            "power present &rarr; no",
            "unskillfulness arises",
            "power vanishes &rarr;",
            "opposite takes over, at once",
        ]),
        ("No gap", [
            "<span class=\"pali\">antarahitā</span>vanished",
            "<span class=\"pali\">pariyuṭṭhāya tiṭṭhati</span>",
            "takes over, standing",
        ]),
        ("Source's own shorthand", [
            "faith: given in full",
            "conscience/prudence/energy:",
            "elided by the source itself",
            "wisdom: given in full",
        ]),
        ("Cross-references", [
            "AN 5.3&ndash;5 &middot; outcomes described",
            "AN 5.6 &middot; the mechanism",
            "AN 5.7 &middot; next: protection until complete",
        ]),
    ],
    further=[
        '<a href="%s/an5.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.5.html">AN 5.5 &middot; Disrobing</a> &mdash; the previous discourse, on the '
        "social consequence of the same lacking and having.",
        '<a href="an-5.7.html">AN 5.7 &middot; Sensual Pleasures</a> &mdash; next, an extended '
        "parable on being protected until these five are complete.",
        '<a href="an-4.163.html">AN 4.163 &middot; Ugly</a> &mdash; where this chapter&rsquo;s five '
        "powers first appeared in this series, described there as something relied on.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.7 — Kāmasutta
# --------------------------------------------------------------------------- #
page(
    7, "Kāma", "Sensual Pleasures",
    meta_title="AN 5.7 — Sensual Pleasures | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kāmasutta — the "
        "extended parable of a nursemaid removing a stick from a baby's mouth, even to the point "
        "of drawing blood, used to explain why a mendicant is watched over until faith, "
        "conscience, prudence, energy, and wisdom are complete. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A general observation about sensual pleasure and going forth, an extended "
                 "simile of a nursemaid and an infant, and the simile's direct application"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Nursemaid and childcare similes illustrating protective vigilance "
                              "appear across early Buddhist narrative literature broadly; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the chapter's longest discourse "
                       "so far, carried by a single vivid image"),
    ],
    why=(
        "This is the first narrative the Fives offer, and it does not flinch. A nursemaid, "
        "noticing a stick or stone in an infant's mouth, cradles the child's head with one hand and "
        "digs the object out with a hooked finger of the other &mdash; <em>even if it drew "
        "blood</em>. The discourse admits plainly that this distresses the child; there is no "
        "denying it. And it says the same care, including the same willingness to cause pain to "
        "prevent worse harm, is owed to a mendicant who has not yet finished developing faith, "
        "conscience, prudence, energy, and wisdom."),
    guide=[
        ("The teaching in one sentence", [
            "A gentleman who goes forth is called a &lsquo;faithful renunciate&rsquo; because "
            "sensual pleasures were available to him and he left them anyway; and just as a "
            "nursemaid protects an infant from swallowing a stick or stone, even at the cost of "
            "distress, the Buddha says he must go on looking after a mendicant until their "
            "development of the five powers is complete."]),
        ("Why the discourse starts with sensual pleasure at all", [
            "The opening claim is easy to read past: <em>sentient beings are mostly charmed by "
            "sensual pleasures</em>, and a young man who has abandoned <em>the scythe and "
            "flail</em> &mdash; ordinary farm labor, and by extension the pleasures that labor "
            "would have funded &mdash; earns the title <em>saddhāpabbajita</em>, one gone forth "
            "out of faith, precisely because pleasures of some kind were available to him. The "
            "discourse is explicit that <em>all</em> sensual pleasures, inferior, average, or "
            "superior, count equally as &lsquo;sensual pleasures&rsquo; for this purpose &mdash; "
            "renunciation is not only meaningful for someone giving up something spectacular."]),
        ("The nursemaid, in full", [
            "The simile is given at length and does not sand down its own difficulty. A negligent "
            "nursemaid lets an infant put a stick or stone in its mouth; a good one notices "
            "quickly, tries to remove it gently, and if that fails, cradles the child&rsquo;s head "
            "in one hand and uses a hooked finger of the other &mdash; <em>even if it drew "
            "blood</em>. The text has the Buddha say directly, in his own voice mid-simile: "
            "<em>&lsquo;This will distress the child; there&rsquo;s no denying.&rsquo;</em> The "
            "discourse does not claim the intervention is painless. It claims the intervention is "
            "still <em>karaṇīya</em>, something that should be done, by a nursemaid who wants "
            "what&rsquo;s best for the child, out of kindness and sympathy."]),
        ("Where the vigilance ends", [
            "The simile has a clear endpoint, and it is worth reading as carefully as the "
            "beginning. Once the boy has <em>grown up and has enough sense</em>, the nursemaid "
            "stops being concerned, on the grounds that <em>the boy can look after himself; he "
            "won&rsquo;t be negligent</em>. The application makes the parallel explicit: the "
            "Buddha says he must go on looking after a mendicant only <em>as long as</em> their "
            "faith, conscience, prudence, energy, and wisdom regarding skillful qualities is "
            "unfinished; once it is finished, the same release from concern applies."]),
        ("Reading this against AN 5.6", [
            "AN 5.6 described a mechanism with no gap: a power vanishes, its opposite instantly "
            "occupies the space. AN 5.7 supplies the reason that gap is watched at all &mdash; a "
            "mendicant who has not finished developing the five powers is, on this account, "
            "someone still vulnerable to exactly that kind of instant reversal, and still worth "
            "protecting from it even at real cost. The two discourses fit together as diagnosis "
            "and response."]),
    ],
    terms=[
        ("saddhāpabbajita",
         "&ldquo;one gone forth out of faith&rdquo; &mdash; the title earned by a gentleman who "
         "leaves available sensual pleasures behind, named in this discourse&rsquo;s opening."),
        ("asitabyābhaṅga",
         "&ldquo;having left behind sickle and carrying-pole&rdquo; &mdash; the image for ordinary "
         "farm labor and the livelihood it represents, abandoned at going forth."),
        ("dhāti",
         "&ldquo;nursemaid&rdquo; &mdash; the figure at the center of this discourse&rsquo;s "
         "extended simile, acting out of kindness and sympathy even when the act causes pain."),
        ("karaṇīya",
         "&ldquo;should be done&rdquo; &mdash; the word marking the nursemaid&rsquo;s painful "
         "intervention as still obligatory, not merely permissible."),
        ("anapekkha",
         "&ldquo;unconcerned, without need to watch over&rdquo; &mdash; the state the nursemaid "
         "reaches once the child can look after himself, paired to the mendicant who has finished "
         "developing the five powers."),
    ],
    text_intro=(
        "The discourse in full: sensual pleasures and going forth, the extended simile of the "
        "nursemaid and the infant, and its direct application to a mendicant still developing the "
        "five powers. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Going forth from available pleasures"),
        ("p", "&sect;1", "an5.7:1.1-1.5"),
        ("h3", "The nursemaid and the infant"),
        ("p", "&sect;2", "an5.7:1.6-1.15"),
        ("h3", "The application"),
        ("p", "&sect;3", "an5.7:2.1-2.3"),
    ],
    quiz=[
        {"q": "Why does a gentleman who goes forth earn the title 'saddhāpabbajita', one gone "
              "forth out of faith?",
         "opts": [
             "Because he was forced into monastic life",
             "Because sensual pleasures of some kind were available to him, and he left them anyway",
             "Because he had already achieved awakening before ordaining",
             "Because his family required it"],
         "correct": 1,
         "expl": "Even inferior, average, and superior pleasures all count equally as 'sensual pleasures' for this purpose."},
        {"q": "In the nursemaid simile, what does a good nursemaid do if gentle removal of the "
              "object fails?",
         "opts": [
             "Gives up and leaves the object in place",
             "Cradles the child's head and removes it with a hooked finger, even if it draws blood",
             "Calls for another caretaker",
             "Waits for the child to remove it himself"],
         "correct": 1,
         "expl": "The text states this plainly, without softening the image."},
        {"q": "Does the discourse claim the nursemaid's intervention is painless?",
         "opts": [
             "Yes, it claims no distress results",
             "No — the Buddha says directly, mid-simile, 'this will distress the child; there's no "
             "denying'",
             "The text is silent on this point",
             "It claims only mild discomfort, never real distress"],
         "correct": 1,
         "expl": "The discourse is honest about the cost rather than pretending the intervention is gentle."},
        {"q": "What word marks the nursemaid's painful intervention as more than merely permissible?",
         "opts": [
             "Anapekkha — 'unconcerned'",
             "Karaṇīya — 'should be done', naming it as obligatory",
             "Dukkha — 'suffering'",
             "Sekha — 'trainee'"],
         "correct": 1,
         "expl": "Done by a nursemaid who wants what's best for the child, out of kindness and sympathy."},
        {"q": "When does the nursemaid in the simile stop being concerned about the child?",
         "opts": [
             "Never — the concern is described as permanent",
             "Once the boy has grown up and has enough sense to look after himself",
             "As soon as the object is removed",
             "Only after the child's death"],
         "correct": 1,
         "expl": "'The boy can look after himself. He won't be negligent.'"},
        {"q": "How does the discourse apply the simile directly to a mendicant?",
         "opts": [
             "It does not apply the simile at all — it stands alone",
             "The Buddha says he must go on looking after a mendicant only as long as their faith, "
             "conscience, prudence, energy, and wisdom are unfinished",
             "It applies only to fully awakened mendicants",
             "It applies only to laypeople, not mendicants"],
         "correct": 1,
         "expl": "Once the five powers are complete, the same release from concern applies, matching the nursemaid's."},
        {"q": "How does the guide connect AN 5.7 to AN 5.6?",
         "opts": [
             "It says the two discourses are unrelated",
             "AN 5.6 gives the mechanism of instant reversal when a power vanishes; AN 5.7 gives the "
             "reason a mendicant is watched over against exactly that risk",
             "AN 5.7 contradicts AN 5.6's claim entirely",
             "AN 5.7 replaces the five powers with a new list"],
         "correct": 1,
         "expl": "Diagnosis, then response — read together rather than in isolation."},
        {"q": "What does the opening line claim about sentient beings generally?",
         "opts": [
             "That most beings actively reject sensual pleasure",
             "That beings are mostly charmed by sensual pleasures",
             "That sensual pleasure applies only to monastics",
             "That the discourse takes no position on this"],
         "correct": 1,
         "expl": "The premise that makes going forth from available pleasure meaningful in the first place."},
        {"q": "What does 'asitabyābhaṅga' refer to?",
         "opts": [
             "A meditation posture",
             "Sickle and carrying-pole — ordinary farm labor, abandoned at going forth",
             "A type of alms bowl",
             "A monastic robe"],
         "correct": 1,
         "expl": "The image for the livelihood and its pleasures left behind."},
        {"q": "How long is AN 5.7 compared to the discourses before it in this chapter?",
         "opts": [
             "Identical in length to all the others",
             "Noticeably longer — the chapter's longest so far, carried by its extended simile",
             "Much shorter than the others",
             "It has no text at all, only a title"],
         "correct": 1,
         "expl": "The narrative form takes more space than the formulaic discourses surrounding it."},
    ],
    marginalia=[
        ("The simile", [
            "infant, stick in mouth &rarr;",
            "nursemaid removes it,",
            "even drawing blood",
        ]),
        ("Named plainly", [
            "&ldquo;this will distress",
            "the child &mdash; there&rsquo;s",
            "no denying&rdquo;",
        ]),
        ("The endpoint", [
            "grown, has enough sense &rarr;",
            "nursemaid, unconcerned",
            "five powers complete &rarr;",
            "same release, for a mendicant",
        ]),
        ("Cross-references", [
            "AN 5.6 &middot; the mechanism",
            "AN 5.7 &middot; the protection",
            "AN 5.8 &middot; next: fails or establishes",
        ]),
    ],
    further=[
        '<a href="%s/an5.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.6.html">AN 5.6 &middot; Becoming</a> &mdash; the previous discourse, on the '
        "mechanism this page's protection is guarding against.",
        '<a href="an-5.8.html">AN 5.8 &middot; Failure</a> &mdash; next, returning to the '
        "chapter&rsquo;s compact fails/establishes formula.",
        '<a href="an-2.1-10.html">AN 2.1&ndash;10</a> &mdash; AN 2.9, on hiri and ottappa as '
        "world-protectors, two of the five powers this simile concerns.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.8 — Cavanasutta
# --------------------------------------------------------------------------- #
page(
    8, "Cavana", "Failure",
    meta_title="AN 5.8 — Failure | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Cavanasutta — a third "
        "image for the same five powers: lacking them, a mendicant falls away and fails to "
        "establish themselves in the true teaching; having them, they stand firm. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five clauses stated once for lacking each quality, folded into one summary "
                 "sentence, mirrored for having all five"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Falling away from and standing firm in the teaching is a standard "
                              "pair of images across early Buddhist literature broadly; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short and formulaic, its "
                       "interest lies in the image it adds to the chapter's set"),
    ],
    why=(
        "This chapter has now offered three different images for the same underlying claim: AN 5.4 "
        "pictured a parcel delivered to hell or heaven, AN 5.6 pictured a vacated quality instantly "
        "occupied by its opposite, and this discourse pictures falling and standing &mdash; "
        "<em>cavati</em>, falls away, against <em>patiṭṭhāti</em>, stands firm, both applied to a "
        "mendicant's place <em>in the true teaching</em>, <em>saddhamme</em>. None of the three "
        "images replaces the others; the collection seems content to restate one claim in several "
        "registers rather than settle on a single metaphor."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant lacking faith, conscience, prudence, energy, and wisdom falls away and "
            "fails to establish themselves in the true teaching; one who has all five does not "
            "fall away, and does establish themselves."]),
        ("A third image, not a repetition", [
            "<em>Cavati</em> and <em>patiṭṭhāti</em> are architectural verbs &mdash; falling and "
            "standing &mdash; applied here to a person's place within something, the true teaching. "
            "This is different in kind from AN 5.4's delivery image and AN 5.6's vacancy-and-"
            "occupation image, even though all three discourses are making the identical claim "
            "about the identical five qualities. A reader tracking the chapter as a whole is "
            "watching one argument tried in three different pictures: a destination reached, a "
            "space filled, and now a structure stood in or fallen from."]),
        ("What &lsquo;the true teaching&rsquo; names", [
            "<em>Saddhamma</em> here means something closer to standing, membership, a place held "
            "&mdash; not primarily a body of doctrine to be believed correctly. To fail to "
            "establish oneself in the true teaching is not described here as a doctrinal error; "
            "it is described as a kind of falling, parallel to the fall from heaven the earlier "
            "discourses pictured literally. This exact word will return with far more weight much "
            "later in the Fives, in the vagga explicitly devoted to its decline; this discourse is "
            "worth remembering when that material arrives."]),
        ("The list, for a fourth time unchanged", [
            "Faithless, shameless, imprudent, lazy, witless: identical wording to AN 5.1, 5.3, and "
            "5.4. By this point in the chapter the list itself should need no further "
            "introduction; what a reader should be tracking from here on is only which new "
            "consequence or qualifier each discourse attaches to it."]),
        ("What comes next", [
            "AN 5.9 takes this exact formula and adds one qualifier &mdash; disrespectful and "
            "irreverent &mdash; to both halves. AN 5.10 will then take the same qualified formula "
            "and swap the falling/standing image for one of growth and maturity, closing the "
            "chapter. The three discourses read fastest as one template inherited and modified "
            "twice in succession."]),
    ],
    terms=[
        ("cavati",
         "&ldquo;falls away&rdquo; &mdash; the verb for losing one&rsquo;s place, applied here to "
         "standing in the true teaching rather than to a literal fall."),
        ("patiṭṭhāti",
         "&ldquo;stands firm, is established&rdquo; &mdash; the positive counterpart, naming a "
         "settled place rather than an event or attainment."),
        ("saddhamma",
         "&ldquo;the true teaching&rdquo; &mdash; used here as something one has a standing within, "
         "a word this series will meet again with far more weight later in the Fives."),
        ("duppañño",
         "&ldquo;witless&rdquo; &mdash; the last of the five negative terms, naming absence of the "
         "specific insight-wisdom AN 5.2 defined."),
        ("kusīto",
         "&ldquo;lazy&rdquo; &mdash; the negative counterpart to energy roused up, named but not "
         "further defined in this discourse."),
    ],
    text_intro=(
        "The discourse in full: lacking the five, falling away and failing to establish oneself in "
        "the true teaching; having them, the reverse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Falling away"),
        ("p", "&sect;1", "an5.8:1.1-1.8"),
        ("h3", "Standing firm"),
        ("p", "&sect;2", "an5.8:2.1-2.8"),
    ],
    quiz=[
        {"q": "What image does AN 5.8 use for the consequence of lacking the five powers?",
         "opts": [
             "A parcel delivered to hell",
             "Falling away and failing to establish oneself in the true teaching",
             "A vacated quality being occupied",
             "A nursemaid's intervention"],
         "correct": 1,
         "expl": "Cavati against patiṭṭhāti — falling versus standing firm."},
        {"q": "How many distinct images has this chapter now used for the same underlying claim, "
              "counting AN 5.8?",
         "opts": [
             "Just one, repeated identically each time",
             "Three — delivery (AN 5.4), vacancy-and-occupation (AN 5.6), and falling/standing "
             "(AN 5.8)",
             "Five, one per quality",
             "None — this is the first image offered"],
         "correct": 1,
         "expl": "The collection restates one claim in several registers rather than settling on one metaphor."},
        {"q": "How does the guide characterize what 'saddhamma' (the true teaching) names in this "
              "discourse?",
         "opts": [
             "A body of doctrine to be believed correctly",
             "Something closer to a standing or place held, not primarily a set of correct beliefs",
             "A specific meditation technique",
             "A synonym for nibbāna"],
         "correct": 1,
         "expl": "Failing to establish oneself is pictured as a kind of falling, not a doctrinal error."},
        {"q": "What does the guide say awaits this same word 'saddhamma' later in the Fives?",
         "opts": [
             "It never appears again in this nipāta",
             "It returns with far more weight in a vagga explicitly devoted to its decline",
             "It is replaced entirely by a different term",
             "It becomes a proper name for a person"],
         "correct": 1,
         "expl": "A forward-pointing note worth remembering when that later material arrives."},
        {"q": "How does the five-quality list in AN 5.8 compare to AN 5.1, 5.3, and 5.4?",
         "opts": [
             "It is a completely new list",
             "It is worded identically — faithless, shameless, imprudent, lazy, witless, against "
             "their opposites",
             "It drops wisdom from the list",
             "It adds a sixth quality"],
         "correct": 1,
         "expl": "By this point the list needs no further introduction; only the attached image or consequence changes."},
        {"q": "What does AN 5.9, the next discourse, add to this exact formula?",
         "opts": [
             "A completely different list of qualities",
             "One qualifier — disrespectful and irreverent — added to both halves",
             "A shift to a lay audience",
             "Nothing; it is a verbatim repeat with no change"],
         "correct": 1,
         "expl": "The formula is inherited and modified, not simply repeated."},
        {"q": "What does AN 5.10, the discourse after that, change?",
         "opts": [
             "It returns to the original unqualified formula",
             "It swaps the falling/standing image for one of growth and maturity, and closes the "
             "chapter",
             "It introduces an entirely new set of five qualities",
             "It repeats AN 5.9 exactly"],
         "correct": 1,
         "expl": "A second modification of the inherited template, closing the vagga."},
        {"q": "What kind of verbs are 'cavati' and 'patiṭṭhāti'?",
         "opts": [
             "Verbs of speech",
             "Architectural verbs — falling and standing — applied to a person's place in something",
             "Verbs of eating and drinking",
             "Verbs found only in verse, never in prose"],
         "correct": 1,
         "expl": "A structural image, distinct from the delivery and vacancy images used earlier in the chapter."},
        {"q": "Is a new definition of any of the five qualities given in AN 5.8?",
         "opts": [
             "Yes, all five are redefined",
             "No — the wording is identical to earlier discourses; only the attached consequence is "
             "new",
             "Only wisdom is redefined",
             "Only faith is redefined"],
         "correct": 1,
         "expl": "AN 5.2 already did the defining work in full."},
        {"q": "Where is AN 5.8 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Squirrels' Sanctuary near Rājagaha",
             "Kosambī"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("Three images so far", [
            "AN 5.4 &middot; parcel, delivered",
            "AN 5.6 &middot; space, occupied",
            "AN 5.8 &middot; standing, or fallen",
        ]),
        ("The verbs", [
            "<span class=\"pali\">cavati</span>falls away",
            "<span class=\"pali\">patiṭṭhāti</span>stands firm",
        ]),
        ("A word to remember", [
            "<span class=\"pali\">saddhamma</span>true teaching",
            "&mdash; returns later, with weight",
        ]),
        ("Cross-references", [
            "AN 5.4 &amp; 5.6 &middot; earlier images",
            "AN 5.9 &middot; next: +disrespect",
            "AN 5.10 &middot; then: growth/maturity",
        ]),
    ],
    further=[
        '<a href="%s/an5.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.4.html">AN 5.4 &middot; Cast Down</a> &mdash; the delivery image this '
        "discourse's falling/standing image stands alongside.",
        '<a href="an-5.9.html">AN 5.9 &middot; Disrespect (1st)</a> &mdash; next, the same formula '
        "with one qualifier added.",
        '<a href="an-5.6.html">AN 5.6 &middot; Becoming</a> &mdash; the vacancy-and-occupation '
        "image, the second of the chapter's three pictures for this claim.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.9 — Paṭhamaagāravasutta
# --------------------------------------------------------------------------- #
page(
    9, "Paṭhamaagārava", "Disrespect (1st)",
    meta_title="AN 5.9 — Disrespect (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first Agāravasutta — AN "
        "5.8's falling/standing formula, inherited exactly and given one new qualifier: "
        "disrespectful and irreverent. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.8's formula verbatim, with 'disrespectful and irreverent' added to both "
                 "the mendicant who falls away and the one who stands firm"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the chapter's first case of "
                       "one discourse visibly building on the one before it"),
    ],
    why=(
        "AN 5.9 makes almost no independent claim. It takes AN 5.8&rsquo;s formula &mdash; falls "
        "away and fails to establish, or stands firm and does establish, in the true teaching "
        "&mdash; and prefixes both halves with <em>agāravo appatisso</em>, disrespectful and "
        "irreverent, or its opposite. The interesting question this discourse raises is not what "
        "it says but why the collection bothers to say it twice with one word changed, rather than "
        "leaving readers to infer the addition."),
    guide=[
        ("The teaching in one sentence", [
            "A disrespectful and irreverent mendicant lacking the five powers falls away and fails "
            "to establish themselves in the true teaching; a respectful and reverent mendicant "
            "with all five does not fall away, and does establish themselves &mdash; the identical "
            "claim as AN 5.8, with one qualifier attached to each side."]),
        ("Why state the obvious addition explicitly", [
            "A reader could reasonably ask why this discourse exists at all, given how little it "
            "adds. The likely answer is oral: a formula meant to be memorized and recited does not "
            "save effort by leaving additions implicit, since an implicit addition is exactly what "
            "a chanted transmission would lose first. Stating the qualified version in full, "
            "rather than as a note appended to AN 5.8, keeps the two formulas equally secure in "
            "memory and equally available to be cited on their own."]),
        ("What &lsquo;disrespect&rsquo; adds to the picture", [
            "<em>Agāravo appatisso</em> names an attitude, not a missing skill. It sits alongside "
            "the five powers rather than inside the list of five &mdash; a mendicant could in "
            "principle lack any combination of faith, conscience, prudence, energy, or wisdom and "
            "still be described, separately, as respectful or disrespectful. This discourse pairs "
            "the attitude with lacking the five specifically, but does not claim the two always "
            "travel together."]),
        ("A visible seam in the chapter's construction", [
            "AN 5.8 and 5.9 sitting side by side let a reader watch the collection's building "
            "method directly: a base formula, then a modified restatement, placed as two separate "
            "discourses rather than one discourse with a footnote. The Fours offered similar cases "
            "of adjacent discourses sharing a frame; this chapter's version of the same technique "
            "is unusually easy to see because so little separates the two texts."]),
        ("What follows", [
            "AN 5.10, closing the chapter, will take this same qualified formula one step further "
            "&mdash; keeping &lsquo;disrespectful and irreverent&rsquo; but swapping falling and "
            "standing for a claim about growth, improvement, and maturity in the training. That "
            "swap is a real addition to track; this discourse's own addition was smaller."]),
    ],
    terms=[
        ("agārava",
         "&ldquo;disrespect&rdquo; &mdash; the attitude this discourse adds to AN 5.8&rsquo;s "
         "formula, named as sitting alongside the five powers rather than inside the list."),
        ("appatissa",
         "&ldquo;irreverent&rdquo; &mdash; agārava&rsquo;s standing partner, always paired with it "
         "in this formula rather than appearing alone."),
        ("sagārava",
         "&ldquo;respectful&rdquo; &mdash; the positive counterpart, paired with the mendicant who "
         "has all five powers and stands firm."),
        ("sappatissa",
         "&ldquo;reverent&rdquo; &mdash; sagārava&rsquo;s partner in the positive half, completing "
         "the matched pair of qualifiers."),
        ("paṭhama",
         "&ldquo;first&rdquo; &mdash; the ordinal in this discourse&rsquo;s own title, marking it "
         "as the first of two discourses on disrespect, with AN 5.10 following as the second."),
    ],
    text_intro=(
        "The discourse in full: AN 5.8's formula, with 'disrespectful and irreverent' added "
        "throughout. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Disrespectful, falling away"),
        ("p", "&sect;1", "an5.9:1.1-1.8"),
        ("h3", "Respectful, standing firm"),
        ("p", "&sect;2", "an5.9:2.1-2.8"),
    ],
    quiz=[
        {"q": "What does AN 5.9 add to AN 5.8's formula?",
         "opts": [
             "An entirely new consequence",
             "One qualifier, 'disrespectful and irreverent', prefixed to both halves",
             "A new list of qualities replacing the five powers",
             "A different setting"],
         "correct": 1,
         "expl": "The claim is otherwise identical to AN 5.8."},
        {"q": "Why does the guide suggest the collection states this small addition as a full "
              "separate discourse rather than a footnote to AN 5.8?",
         "opts": [
             "By accident of transmission, with no purpose",
             "An oral, chanted tradition preserves additions better stated in full than left "
             "implicit",
             "Because the two discourses were composed centuries apart",
             "Because AN 5.8 was considered incomplete"],
         "correct": 1,
         "expl": "An implicit addition is exactly what a memorized recitation would lose first."},
        {"q": "According to the guide, is 'disrespect' presented as part of the five powers "
              "themselves?",
         "opts": [
             "Yes, it replaces one of the five",
             "No — it is an attitude that sits alongside the five powers, not inside the list",
             "Yes, it becomes a sixth power",
             "The discourse does not distinguish this at all"],
         "correct": 1,
         "expl": "A mendicant could in principle lack any of the five and still be respectful or disrespectful, separately."},
        {"q": "What visible feature do AN 5.8 and 5.9 let a reader observe directly?",
         "opts": [
             "That the two discourses contradict each other",
             "The collection's building method — a base formula, then a modified restatement, as "
             "two separate discourses",
             "That AN 5.9 was translated by a different translator",
             "That the five powers change between the two discourses"],
         "correct": 1,
         "expl": "An unusually visible seam because so little separates the two texts."},
        {"q": "What does AN 5.10, the next discourse, change from this formula?",
         "opts": [
             "It drops the disrespect qualifier entirely",
             "It keeps 'disrespectful and irreverent' but swaps falling/standing for a claim about "
             "growth, improvement, and maturity",
             "It repeats AN 5.9 verbatim with no change",
             "It abandons the five powers"],
         "correct": 1,
         "expl": "A larger addition than AN 5.9's own modification of AN 5.8."},
        {"q": "What does the discourse's own title, 'Paṭhama', signal?",
         "opts": [
             "That this is the final discourse of the nipāta",
             "That this is the first of two discourses on disrespect, with a second following",
             "That this is the first discourse of the entire collection",
             "Nothing — it is a scribal addition with no meaning"],
         "correct": 1,
         "expl": "AN 5.10 is the paired second discourse."},
        {"q": "Are 'agārava' and 'appatissa' ever used separately in this formula?",
         "opts": [
             "Yes, frequently apart",
             "No — they always appear paired together, as do their positive counterparts",
             "Only agārava appears; appatissa is never used",
             "Only appatissa appears; agārava is never used"],
         "correct": 1,
         "expl": "A fixed pair, matching the fixed pair hiri/ottappa elsewhere in this chapter's material."},
        {"q": "What are the five powers named in AN 5.9's negative half?",
         "opts": [
             "A new list unique to this discourse",
             "The same faithless, shameless, imprudent, lazy, witless from every earlier discourse "
             "in the chapter",
             "Only three of the original five",
             "The five faculties, not the powers of a trainee"],
         "correct": 1,
         "expl": "Unchanged since AN 5.1."},
        {"q": "Does AN 5.9 offer a new image, distinct from AN 5.8's falling/standing picture?",
         "opts": [
             "Yes, an entirely new metaphor",
             "No — it keeps AN 5.8's falling/standing image and adds only the qualifier",
             "Yes, it returns to the delivery image of AN 5.4",
             "Yes, it uses the nursemaid parable again"],
         "correct": 1,
         "expl": "The image is inherited; only the qualifier is new."},
        {"q": "Where is AN 5.9 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Mango Grove",
             "Sāketa"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("Inherited, plus one", [
            "AN 5.8: falls / stands firm",
            "AN 5.9: + disrespectful",
            "or + respectful",
        ]),
        ("Paired terms", [
            "<span class=\"pali\">agārava</span>disrespect",
            "<span class=\"pali\">appatissa</span>irreverent",
            "&mdash; always together",
        ]),
        ("Why say it in full", [
            "a chanted tradition",
            "loses what stays implicit",
        ]),
        ("Cross-references", [
            "AN 5.8 &middot; the base formula",
            "AN 5.9 &middot; this page, first of two",
            "AN 5.10 &middot; next: growth/maturity",
        ]),
    ],
    further=[
        '<a href="%s/an5.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.8.html">AN 5.8 &middot; Failure</a> &mdash; the base formula this discourse '
        "inherits and qualifies.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; next, and the '
        "chapter's closing discourse, adding a further variation.",
        '<a href="an-2.1-10.html">AN 2.1&ndash;10</a> &mdash; AN 2.9, on hiri and ottappa, the '
        "chapter's other fixed pair of paired qualifiers.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.10 — Dutiyaagāravasutta
# --------------------------------------------------------------------------- #
page(
    10, "Dutiyaagārava", "Disrespect (2nd)",
    meta_title="AN 5.10 — Disrespect (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Agāravasutta — "
        "the chapter's closing discourse, keeping AN 5.9's disrespect qualifier but swapping "
        "falling and standing for growth, improvement, and maturity, and closing with the "
        "vagga's own untranslated Pāli mnemonic verse. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.9's disrespect-qualified formula, with 'grows, improves, matures' replacing "
                 "'falls away, stands firm', followed by the vagga's closing colophon and mnemonic "
                 "verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short in its own text, but "
                       "closing material worth reading carefully"),
    ],
    why=(
        "AN 5.10 does two things at once. As a discourse, it takes AN 5.9's disrespect-qualified "
        "formula and swaps the image one more time: not falling and standing now, but "
        "<em>vuddhiṁ virūḷhiṁ vepullaṁ</em>, growth, improvement, and maturity, achieved or not "
        "achieved <em>in this teaching and training</em>. As the tenth discourse, it also closes "
        "the chapter, and the source text appended to it a piece of material this reading guide "
        "has not yet had occasion to explain: an <em>uddāna</em>, a Pāli mnemonic verse that "
        "compresses all ten titles of the chapter into a few lines for memorization, left "
        "untranslated in Sujato&rsquo;s English."),
    guide=[
        ("The teaching in one sentence", [
            "A disrespectful and irreverent mendicant lacking the five powers can&rsquo;t achieve "
            "growth, improvement, or maturity in this teaching and training; a respectful and "
            "reverent mendicant with all five can achieve all three."]),
        ("A third variation on the inherited formula", [
            "AN 5.8 gave the base claim in a falling/standing image. AN 5.9 added disrespect as a "
            "qualifier without changing the image. AN 5.10 keeps the qualifier and changes the "
            "image a second time, to a triad of growth words. <em>Vuddhi</em>, growth; "
            "<em>virūḷhi</em>, increase or flourishing; <em>vepulla</em>, fullness or maturity "
            "&mdash; three near-synonyms stacked together, in the same way AN 5.3&rsquo;s "
            "<em>distress, anguish, fever</em> were stacked rather than merged into one word. The "
            "chapter appears to favor this kind of triple emphasis at its more consequential "
            "moments."]),
        ("What is being grown or matured", [
            "The object is <em>imasmiṁ dhammavinaye</em>, in this teaching and training &mdash; "
            "the whole dispensation, not a single practice or a single quality. This is a broader "
            "claim than any earlier discourse in the chapter made: not that the mendicant "
            "themselves prospers, but that their whole participation in the Buddha&rsquo;s "
            "teaching and discipline either flourishes or stalls, depending on the same five "
            "qualities and the same one attitude."]),
        ("The uddāna: how a chapter carries its own index", [
            "At the very end of the source text, after the discourse itself closes, comes a line "
            "naming the chapter &mdash; <em>Sekhabalavaggo paṭhamo</em>, &lsquo;the first chapter, "
            "on the powers of a trainee&rsquo; &mdash; followed by a short verse in Pāli that "
            "compresses all ten discourse titles from this chapter into a chantable mnemonic: "
            "<em>in brief, in detail, suffering, cast down, the fifth by training, becoming and in "
            "sensual pleasures</em>, and so on. Sujato leaves this verse untranslated in the "
            "English edition, since it exists purely as an aid to memorizing the chapter&rsquo;s "
            "own contents in order, not as teaching in its own right. It is the collection&rsquo;s "
            "own index, built into the text rather than added by an editor, and every vagga from "
            "here through the rest of the Fives will close the same way &mdash; a colophon this "
            "reading guide will not re-explain each time it appears."]),
        ("What comes after this chapter", [
            "The Fives continue immediately with the Balavagga, the second chapter, still called "
            "&lsquo;Powers&rsquo; but now returning to the more familiar <em>bala</em> that shares "
            "three terms with the sekhabala rather than five. A reader arriving at AN 5.11 having "
            "read this chapter in full will recognize the terrain immediately."]),
    ],
    terms=[
        ("vuddhi",
         "&ldquo;growth&rdquo; &mdash; the first of three near-synonyms replacing the falling/"
         "standing image, applied here to a mendicant&rsquo;s whole participation in the teaching."),
        ("virūḷhi",
         "&ldquo;increase, flourishing&rdquo; &mdash; the second of the three, stacked rather than "
         "merged with the others."),
        ("vepulla",
         "&ldquo;fullness, maturity&rdquo; &mdash; the third, completing the triad this discourse "
         "uses at its most consequential moment."),
        ("dhammavinaya",
         "&ldquo;teaching and training&rdquo; &mdash; the Buddha&rsquo;s whole dispensation, named "
         "as what either flourishes or stalls, rather than a single practice."),
        ("uddāna",
         "&ldquo;mnemonic verse, summary&rdquo; &mdash; the chapter-closing Pāli verse compressing "
         "all ten titles for memorization, left untranslated and not re-explained on later pages."),
    ],
    text_intro=(
        "The discourse in full: the disrespect-qualified formula, now claiming growth, "
        "improvement, and maturity in the teaching and training rather than falling or standing. "
        "The closing colophon and Pāli mnemonic verse are part of the source but are not "
        "translated text, and are described rather than reproduced here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Disrespectful, unable to grow"),
        ("p", "&sect;1", "an5.10:1.1-1.8"),
        ("h3", "Respectful, able to grow"),
        ("p", "&sect;2", "an5.10:2.1-2.5"),
    ],
    quiz=[
        {"q": "What image does AN 5.10 use in place of AN 5.8 and 5.9's falling/standing image?",
         "opts": [
             "A parcel delivered to hell or heaven",
             "Growth, improvement, and maturity — vuddhi, virūḷhi, vepulla — achieved or not in "
             "this teaching and training",
             "A vacated quality being occupied",
             "The nursemaid parable"],
         "correct": 1,
         "expl": "A third variation on the formula inherited from AN 5.8."},
        {"q": "Does AN 5.10 keep AN 5.9's 'disrespectful and irreverent' qualifier?",
         "opts": [
             "No, it drops the qualifier entirely",
             "Yes — it keeps the qualifier and changes only the image",
             "It replaces disrespect with a different attitude altogether",
             "The discourse does not mention respect or disrespect"],
         "correct": 1,
         "expl": "AN 5.10 inherits AN 5.9's addition and adds a further change of its own."},
        {"q": "What is the object of the growth this discourse describes — what is said to grow or "
              "stall?",
         "opts": [
             "Only the mendicant's physical health",
             "'This teaching and training' — the whole dispensation, not a single practice",
             "Only the mendicant's reputation among laypeople",
             "The size of the monastic community"],
         "correct": 1,
         "expl": "A broader claim than any earlier discourse in the chapter — whole participation, not one quality."},
        {"q": "What is an 'uddāna', as explained in this discourse's guide?",
         "opts": [
             "A formal debate between two monks",
             "A Pāli mnemonic verse compressing a chapter's discourse titles into a chantable "
             "summary",
             "A type of monastic robe",
             "A ceremony marking ordination"],
         "correct": 1,
         "expl": "The collection's own built-in index, left untranslated by Sujato."},
        {"q": "Why does Sujato leave the uddāna verse untranslated in the English edition?",
         "opts": [
             "Because the Pāli is lost and cannot be recovered",
             "Because it exists purely as a memorization aid, not as teaching in its own right",
             "Because it is considered too sacred to translate",
             "Because it was added by a later editor and is not authentic"],
         "correct": 1,
         "expl": "The reading guide follows Sujato's choice rather than inventing a translation not in the source."},
        {"q": "How does the guide say later vaggas in the Fives will handle this same closing "
              "colophon?",
         "opts": [
             "It will not appear again anywhere in the Fives",
             "Every vagga will close the same way, and the guide will not re-explain it each time",
             "Only every other vagga will have one",
             "Each vagga's colophon will be fully translated on its own page"],
         "correct": 1,
         "expl": "Explained fully once here, referenced briefly from then on."},
        {"q": "What is the name given to this closing chapter itself, per the colophon?",
         "opts": [
             "Balavaggo, 'the chapter on powers'",
             "Sekhabalavaggo paṭhamo, 'the first chapter, on the powers of a trainee'",
             "Pañcakanipāto, 'the book of fives'",
             "No name is given"],
         "correct": 1,
         "expl": "Matching the chapter's own opening name from AN 5.1's glossary."},
        {"q": "What chapter follows immediately after this one, and what does the guide note about "
              "its name?",
         "opts": [
             "The Balavagga, still called 'Powers', but returning to the more familiar bala sharing "
             "three terms with sekhabala",
             "A chapter with no relation to this one's material",
             "A return to the Fours",
             "The final chapter of the Fives"],
         "correct": 0,
         "expl": "A reader who has read this chapter in full will recognize the terrain at AN 5.11."},
        {"q": "Are the three growth-words vuddhi, virūḷhi, and vepulla merged into one English "
              "term, or kept distinct?",
         "opts": [
             "Merged into a single word",
             "Kept as three stacked near-synonyms, matching the earlier triple emphasis at AN 5.3",
             "Only one of the three is translated at all",
             "They are treated as contradictory terms"],
         "correct": 1,
         "expl": "A pattern the chapter favors at its more consequential moments."},
        {"q": "Where is AN 5.10 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Eastern Monastery",
             "Nāḷandā"],
         "correct": 1,
         "expl": "Consistent with every discourse in this chapter after the first."},
    ],
    marginalia=[
        ("Three formulas, one list", [
            "AN 5.8: falls / stands",
            "AN 5.9: + disrespect",
            "AN 5.10: + growth triad",
        ]),
        ("The growth triad", [
            "<span class=\"pali\">vuddhi</span>growth",
            "<span class=\"pali\">virūḷhi</span>increase",
            "<span class=\"pali\">vepulla</span>maturity",
        ]),
        ("The chapter's own index", [
            "<span class=\"pali\">uddāna</span>mnemonic verse",
            "ten titles, compressed",
            "&mdash; untranslated by Sujato",
        ]),
        ("Cross-references", [
            "AN 5.9 &middot; the qualifier, added",
            "AN 5.1 &middot; the chapter's opening",
            "AN 5.11 &middot; next: the Balavagga",
        ]),
    ],
    further=[
        '<a href="%s/an5.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.9.html">AN 5.9 &middot; Disrespect (1st)</a> &mdash; the previous discourse, '
        "whose disrespect qualifier this page keeps.",
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; the chapter&rsquo;s opening '
        "discourse, where the five powers this whole vagga explores were first named.",
        '<a href="an-4.163.html">AN 4.163 &middot; Ugly</a> &mdash; where the sekhabala first '
        "appeared in this series, before an entire chapter was built from it.",
    ],
)


VAGGA_2 = "<em>Balavagga</em> &mdash; the second chapter of the Fives"


# --------------------------------------------------------------------------- #
# AN 5.11 — Ananussutasutta
# --------------------------------------------------------------------------- #
page(
    11, "Ananussuta", "Not Learned From Anyone Else",
    vagga=VAGGA_2,
    meta_title="AN 5.11 — Not Learned From Anyone Else | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ananussutasutta — the "
        "chapter's opening claim: the Realized One has his own five tathāgatabala, worded "
        "identically to the trainee's sekhabala from AN 5.1, by which he roars his lion's roar. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A first-person claim to unprecedented insight, followed by the five powers that "
                 "ground it"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The lion's roar and bull's-place imagery for the Buddha's "
                              "unprecedented insight recurs widely across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but its list is the "
                       "chapter's most surprising turn so far"),
    ],
    why=(
        "This chapter is also called &lsquo;Powers&rsquo;, the same English title as the last, and "
        "its first discourse makes an audacious move: it takes the exact five terms named in AN "
        "5.1 for a mere <em>trainee</em> &mdash; faith, conscience, prudence, energy, wisdom "
        "&mdash; and applies them, word for word, to the Realized One himself, calling them "
        "<em>tathāgatabala</em>, a Realized One's powers. The claim attached to them is the "
        "boldest in the collection so far: insight into principles never learned from anyone else."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha claims to have reached perfection in insight into principles not learned "
            "from another, and says the Realized One has five powers &mdash; faith, conscience, "
            "prudence, energy, wisdom &mdash; by which he claims the bull&rsquo;s place, roars his "
            "lion&rsquo;s roar in the assemblies, and turns the divine wheel."]),
        ("The same five words, a different subject", [
            "AN 5.1&rsquo;s sekhabala belonged to a <em>sekha</em>, someone still training. Here "
            "the identical five Pāli compounds &mdash; <em>saddhābalaṁ, hirībalaṁ, ottappabalaṁ, "
            "vīriyabalaṁ, paññābalaṁ</em> &mdash; are named <em>tathāgatabala</em> instead, powers "
            "belonging to one who has completed the path. The discourse does not explain why the "
            "same five items work for both a beginner and a Buddha; it simply uses them at both "
            "ends of the path without comment, which is itself worth noticing."]),
        ("Three images of authority", [
            "<em>Āsabhaṁ ṭhānaṁ</em>, the bull&rsquo;s place, <em>sīhanādaṁ</em>, the lion&rsquo;s "
            "roar, and <em>brahmacakkaṁ</em>, the divine wheel, are three separate images for the "
            "same claim to unmatched authority &mdash; a lead bull among cattle, the boldest cry "
            "in the forest, and the wheel of a world-ruling monarch turned instead as teaching. All "
            "three appear together often enough in the canon to function as a set formula for "
            "public, confident proclamation, not private certainty."]),
        ("&lsquo;Not learned from anyone else&rsquo;", [
            "<em>Ananussutesu dhammesu</em> is the discourse&rsquo;s own title and its central "
            "claim: this insight has no human teacher behind it. Whatever else the five "
            "tathāgatabala are doing here, they are offered as the grounds for that specific claim "
            "&mdash; not evidence of general virtue, but the named support for a claim to "
            "originality that nothing prior in this series has made this explicitly."]),
        ("What the rest of the chapter does with this opening", [
            "AN 5.12, immediately following, stays with the sekhabala one more discourse before "
            "the chapter pivots, at AN 5.13, to the more familiar five faculties/powers list "
            "already flagged at AN 4.163 and AN 5.1. Read in order, this chapter moves from the "
            "Buddha&rsquo;s own powers, to a trainee&rsquo;s powers restated once more, to the "
            "standard list shared across the thirty-seven aids to awakening &mdash; three related "
            "but distinct five-item sets in the space of a few discourses."]),
    ],
    terms=[
        ("tathāgatabala",
         "&ldquo;power of a Realized One&rdquo; &mdash; the same five terms as AN 5.1&rsquo;s "
         "sekhabala, here applied to the Buddha rather than to a trainee."),
        ("ananussuta",
         "&ldquo;not learned from another&rdquo; &mdash; this discourse&rsquo;s title and central "
         "claim, that this insight had no human teacher."),
        ("āsabhaṁ ṭhānaṁ",
         "&ldquo;the bull&rsquo;s place&rdquo; &mdash; the first of three images of public "
         "authority this discourse uses, a lead bull among cattle."),
        ("sīhanādaṁ",
         "&ldquo;lion&rsquo;s roar&rdquo; &mdash; the second image, a formula recurring across the "
         "canon for confident, public proclamation."),
        ("brahmacakkaṁ",
         "&ldquo;the divine wheel&rdquo; &mdash; the third image, recasting a world-ruling "
         "monarch&rsquo;s wheel as the wheel of teaching set in motion."),
    ],
    text_intro=(
        "The discourse in full: the claim to unprecedented insight, and the five powers of a "
        "Realized One that ground it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "An unprecedented claim"),
        ("p", "&sect;1", "an5.11:1.1-1.5"),
    ],
    quiz=[
        {"q": "What five terms does AN 5.11 use for the Realized One's own powers?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "The identical sekhabala from AN 5.1 — faith, conscience, prudence, energy, wisdom — "
             "now called tathāgatabala",
             "A completely new list unrelated to any earlier discourse",
             "Ethics, immersion, wisdom, freedom"],
         "correct": 1,
         "expl": "Word for word the same five compounds, applied to a different subject."},
        {"q": "What claim does 'ananussuta' name in this discourse's title?",
         "opts": [
             "That the teaching was learned from a previous Buddha",
             "That this insight was not learned from anyone else — no human teacher behind it",
             "That the discourse itself was never recorded",
             "That the five powers are inherited traits"],
         "correct": 1,
         "expl": "The discourse's central and boldest claim so far in this series."},
        {"q": "What three images of authority does this discourse use together?",
         "opts": [
             "A mountain, a river, and the sky",
             "The bull's place, the lion's roar, and the divine wheel",
             "A lotus, a jewel, and a lamp",
             "Only one image, the lion's roar"],
         "correct": 1,
         "expl": "A recurring formula for public, confident proclamation of authority."},
        {"q": "Does the discourse explain why the same five terms apply both to a trainee (AN 5.1) "
              "and to the Realized One himself?",
         "opts": [
             "Yes, at great length",
             "No — it uses the identical terms at both ends of the path without comment",
             "It explicitly denies any connection between the two lists",
             "It replaces the terms entirely for the Buddha's version"],
         "correct": 1,
         "expl": "Worth noticing as a deliberate silence, not an oversight."},
        {"q": "What does 'brahmacakkaṁ', the divine wheel, recast?",
         "opts": [
             "A farmer's plow",
             "A world-ruling monarch's wheel, turned instead as teaching",
             "A potter's wheel",
             "A ship's steering wheel"],
         "correct": 1,
         "expl": "One of three images of unmatched authority used together in this discourse."},
        {"q": "What happens to the sekhabala list at AN 5.12, the very next discourse?",
         "opts": [
             "It disappears entirely from the chapter",
             "It continues for one more discourse before the chapter pivots to the standard five "
             "faculties/powers list at AN 5.13",
             "It is immediately contradicted",
             "It becomes the tathāgatabala permanently"],
         "correct": 1,
         "expl": "A brief overlap before the chapter's larger pivot."},
        {"q": "According to the guide, how many related but distinct five-item lists does this "
              "chapter move through in its first several discourses?",
         "opts": [
             "Just one",
             "Three — the Realized One's powers, the trainee's powers restated, and the standard "
             "five faculties/powers",
             "Five separate unrelated lists",
             "None; all discourses use the identical list"],
         "correct": 1,
         "expl": "The Buddha's own powers, then a trainee's, then the standard shared list — moving through the chapter in order."},
        {"q": "What is the setting of AN 5.11?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Bamboo Grove near Rājagaha",
             "Kusinārā"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
        {"q": "Is this discourse spoken in the first person by the Buddha?",
         "opts": [
             "No, it is narrated in the third person throughout",
             "Yes — 'I claim to have attained perfection and consummation of insight...'",
             "It is spoken by a disciple describing the Buddha",
             "It is a dialogue with a questioner"],
         "correct": 1,
         "expl": "A direct first-person claim opens the discourse."},
        {"q": "How does this discourse compare in tone to AN 5.1's opening of the previous chapter?",
         "opts": [
             "Identical in every way",
             "Bolder — a first-person claim to unprecedented insight, rather than a bare list handed "
             "to listeners",
             "More hesitant and uncertain",
             "AN 5.11 makes no claims at all"],
         "correct": 1,
         "expl": "The chapter opens on an audacious note distinct from the previous chapter's terse start."},
    ],
    marginalia=[
        ("Same five, new subject", [
            "AN 5.1: sekhabala",
            "&mdash; a trainee's",
            "AN 5.11: tathāgatabala",
            "&mdash; the Buddha's own",
        ]),
        ("Three images", [
            "<span class=\"pali\">āsabhaṁ ṭhānaṁ</span>bull's place",
            "<span class=\"pali\">sīhanādaṁ</span>lion's roar",
            "<span class=\"pali\">brahmacakkaṁ</span>divine wheel",
        ]),
        ("The claim", [
            "<span class=\"pali\">ananussuta</span>",
            "not learned",
            "from anyone else",
        ]),
        ("Cross-references", [
            "AN 5.1 &middot; the sekhabala, first",
            "AN 5.12 &middot; next: wisdom, the peak",
            "AN 5.13 &middot; then: the standard bala",
        ]),
    ],
    further=[
        '<a href="%s/an5.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; where these five terms were '
        "first given, there naming a trainee's powers rather than a Buddha's.",
        '<a href="an-5.12.html">AN 5.12 &middot; Peak</a> &mdash; next, staying with the sekhabala '
        "one discourse longer.",
        '<a href="an-5.13.html">AN 5.13 &middot; In Brief</a> &mdash; where the chapter pivots to '
        "the more familiar five faculties and powers.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.12 — Kūṭasutta
# --------------------------------------------------------------------------- #
page(
    12, "Kūṭa", "Peak",
    vagga=VAGGA_2,
    meta_title="AN 5.12 — Peak | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kūṭasutta — the "
        "sekhabala one more time, with a new claim: wisdom is chief among the five, holding and "
        "binding everything together the way a roof-peak holds a bungalow. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The sekhabala restated, a ranking claim for wisdom, and a single architectural "
                 "simile"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Wisdom ranked as the culminating member of a training set is a "
                              "widespread structural claim across the Chinese Āgamas and "
                              "Abhidharma; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a short discourse, memorable "
                       "chiefly for its image"),
    ],
    why=(
        "Every earlier discourse using the sekhabala or the standard powers has treated the five "
        "as a set, with no member singled out. This discourse breaks that pattern: of the five "
        "powers of a trainee, it says, <em>the power of wisdom is the chief. It holds and binds "
        "everything together</em>, the way the roof-peak of a bungalow holds and binds the whole "
        "structure. It is a small claim with a large consequence for how to read every list of "
        "five that has come before it in this chapter and the last."),
    guide=[
        ("The teaching in one sentence", [
            "Of the five powers of a trainee, wisdom is called the chief &mdash; the member that "
            "holds and binds all the others together, illustrated by a bungalow&rsquo;s roof-peak."]),
        ("What &lsquo;chief&rsquo; is not claiming", [
            "The discourse does not say wisdom can stand in for the other four, or that a person "
            "could have wisdom alone and dispense with faith, conscience, prudence, and energy. A "
            "roof-peak does not replace the walls; it is the point where the walls, already built, "
            "are held together and given a single shape. The claim is architectural, about "
            "function within a completed structure, not substitutive."]),
        ("Why this ranking, and not a different one", [
            "AN 5.2 already defined wisdom, of these five, in the narrowest and most specific terms "
            "&mdash; not general intelligence but a particular insight into arising and passing "
            "away. This discourse&rsquo;s ranking makes sense against that earlier definition: the "
            "kind of wisdom named is exactly the kind that would let a person see whether their own "
            "faith, conscience, prudence, and energy are actually functioning as claimed, rather "
            "than being taken on trust. A capstone that surveys what it caps is a coherent image "
            "for that specific job."]),
        ("A simile that will return", [
            "The bungalow-peak image is not unique to this discourse. AN 5.16, four discourses "
            "ahead, repeats it word for word for the standard five powers rather than the "
            "sekhabala &mdash; the same architectural claim made twice, once for each of this "
            "chapter&rsquo;s two five-item lists. Reading the two together shows that the ranking "
            "survives the switch between lists; whichever five items are in play, wisdom is what "
            "the discourse calls chief."]),
        ("Where the chapter goes from here", [
            "AN 5.13 pivots the chapter to the standard five faculties/powers &mdash; faith, "
            "energy, mindfulness, immersion, wisdom &mdash; already flagged as distinct from the "
            "sekhabala at AN 4.163 and AN 5.1. This is the last discourse in the Fives, so far, to "
            "use the sekhabala terms."]),
    ],
    terms=[
        ("kūṭa",
         "&ldquo;peak, roof-ridge&rdquo; &mdash; the architectural term giving this discourse its "
         "title and its central image."),
        ("kūṭāgāra",
         "&ldquo;bungalow, peaked house&rdquo; &mdash; a building with a ridged roof, the structure "
         "the simile compares the five powers to."),
        ("saṅgāhika",
         "&ldquo;that which holds together&rdquo; &mdash; one of the two verbs applied to both the "
         "roof-peak and to wisdom among the five powers."),
        ("saṅghātaniya",
         "&ldquo;that which binds together&rdquo; &mdash; the second of the paired verbs, "
         "reinforcing rather than duplicating the first."),
        ("agga",
         "&ldquo;chief, foremost&rdquo; &mdash; the ranking word applied to wisdom, a claim this "
         "discourse is the first in the chapter to make about any single member of a five-item "
         "list."),
    ],
    text_intro=(
        "The discourse in full: the sekhabala restated, wisdom named chief, and the bungalow "
        "simile that explains why. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Wisdom, the chief power"),
        ("p", "&sect;1", "an5.12:1.1-1.5"),
        ("h3", "The simile"),
        ("p", "&sect;2", "an5.12:2.1-2.2"),
        ("h3", "The injunction"),
        ("p", "&sect;3", "an5.12:3.1-3.3"),
    ],
    quiz=[
        {"q": "What claim does AN 5.12 make that no earlier discourse using a five-item power list "
              "has made?",
         "opts": [
             "That one of the five powers is chief, holding and binding the others together",
             "That a sixth power should be added",
             "That the five powers contradict each other",
             "That only monks, not nuns, can develop the five powers"],
         "correct": 0,
         "expl": "Wisdom is singled out as chief — a first for this chapter's power lists."},
        {"q": "What image explains wisdom's role as chief?",
         "opts": [
             "A river flowing into the sea",
             "A bungalow's roof-peak, which holds and binds the whole structure together",
             "The trunk of a tree",
             "The keystone of a bridge"],
         "correct": 1,
         "expl": "Kūṭa, the roof-peak — the discourse's title and central simile."},
        {"q": "Does the discourse claim wisdom can replace the other four powers?",
         "opts": [
             "Yes, wisdom alone is said to be sufficient",
             "No — the image is architectural, about function within a completed structure, not "
             "substitution",
             "The discourse is ambiguous on this point",
             "Yes, but only for advanced trainees"],
         "correct": 1,
         "expl": "A roof-peak doesn't replace the walls; it holds what is already built together."},
        {"q": "How does the guide connect this ranking to AN 5.2's earlier definition of wisdom?",
         "opts": [
             "It sees no connection between the two",
             "AN 5.2 defined wisdom narrowly as insight into arising and passing away — exactly the "
             "kind of insight that could assess whether the other four powers are genuinely "
             "functioning",
             "AN 5.2 and AN 5.12 define wisdom in contradictory ways",
             "AN 5.12 redefines wisdom completely"],
         "correct": 1,
         "expl": "A capstone that surveys what it caps fits that specific, narrow definition."},
        {"q": "Where does this same bungalow-peak simile reappear later in the chapter?",
         "opts": [
             "It never reappears",
             "At AN 5.16, applied to the standard five faculties/powers rather than the sekhabala",
             "At AN 5.20, the chapter's final discourse",
             "In the very next discourse, AN 5.13"],
         "correct": 1,
         "expl": "The identical claim, made for each of the chapter's two five-item lists in turn."},
        {"q": "What does AN 5.13, the next discourse, do?",
         "opts": [
             "Repeats AN 5.12 verbatim",
             "Pivots the chapter to the standard five faculties/powers — faith, energy, mindfulness, "
             "immersion, wisdom",
             "Introduces a sixth power",
             "Returns to the tathāgatabala of AN 5.11"],
         "correct": 1,
         "expl": "AN 5.12 is the chapter's last use of the sekhabala terms so far."},
        {"q": "What two verbs are applied to both the roof-peak and to wisdom?",
         "opts": [
             "Saṅgāhika and saṅghātaniya — 'that which holds together' and 'that which binds "
             "together'",
             "Only one verb is used, repeated",
             "Verbs meaning 'to burn' and 'to shine'",
             "No verbs are shared between the two halves of the simile"],
         "correct": 0,
         "expl": "Paired, reinforcing terms rather than a single word repeated."},
        {"q": "What are the five powers named in this discourse?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Faith, conscience, prudence, energy, wisdom — the sekhabala",
             "Ethics, immersion, wisdom, freedom",
             "A new, sixth list"],
         "correct": 1,
         "expl": "Still the sekhabala at this point in the chapter, not yet the standard bala."},
        {"q": "What closing injunction does AN 5.12 share with AN 5.1?",
         "opts": [
             "None — the two discourses end differently",
             "'So you should train like this,' followed by the same wish to have all five powers",
             "A prediction of future rebirth",
             "A warning about disrobing"],
         "correct": 1,
         "expl": "The chapter's opening injunction formula recurs here."},
        {"q": "Where is AN 5.12 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Deer Park",
             "Vesālī"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("The image", [
            "<span class=\"pali\">kūṭāgāra</span>peaked house",
            "<span class=\"pali\">kūṭa</span>the roof-peak",
            "&mdash; holds it all together",
        ]),
        ("Not a replacement", [
            "wisdom, chief among five",
            "but does not stand in",
            "for the other four",
        ]),
        ("A simile that returns", [
            "AN 5.12: for sekhabala",
            "AN 5.16: for the standard bala",
            "&mdash; same claim, twice",
        ]),
        ("Cross-references", [
            "AN 5.2 &middot; wisdom, defined",
            "AN 5.11 &middot; the Buddha's own five",
            "AN 5.13 &middot; next: the standard bala",
        ]),
    ],
    further=[
        '<a href="%s/an5.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.2.html">AN 5.2 &middot; In Detail</a> &mdash; where wisdom&rsquo;s narrow '
        "definition, presupposed by this discourse's ranking, was first given.",
        '<a href="an-5.16.html">AN 5.16 &middot; The Peak, Again</a> &mdash; the same simile, later '
        "in the chapter, for the standard five powers.",
        '<a href="an-5.13.html">AN 5.13 &middot; In Brief</a> &mdash; next, where the chapter '
        "pivots to that standard list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.13 — Saṅkhittasutta
# --------------------------------------------------------------------------- #
page(
    13, "Saṅkhitta", "In Brief",
    vagga=VAGGA_2,
    meta_title="AN 5.13 — In Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Saṅkhittasutta — "
        "the chapter's pivot from the sekhabala to the standard five powers: faith, energy, "
        "mindfulness, immersion, and wisdom, the list shared with the thirty-seven aids to "
        "awakening. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming a second five-item list, sharing this chapter's own "
                 "title, 'Saṅkhitta', with AN 5.1"),
        ("Length", "~30 seconds to read"),
        ("Northern parallel", "The five powers (bala) are among the most widely attested lists "
                              "across the Chinese Āgamas and Abhidharma literature, as part of the "
                              "thirty-seven aids to awakening; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, but the moment this "
                       "chapter has been building toward since AN 4.163"),
    ],
    why=(
        "This is the moment flagged at AN 4.163, and again at AN 5.1: the chapter finally states "
        "the <em>other</em> five-item list, the one that actually belongs to the thirty-seven aids "
        "to awakening. Faith, energy, mindfulness, immersion, wisdom &mdash; not faith, conscience, "
        "prudence, energy, wisdom. Two of the five names are shared; two are different; one, faith, "
        "recurs unchanged in every version this series has met. The discourse reuses AN 5.1&rsquo;s "
        "own title, <em>Saṅkhitta</em>, and even its exact sentence structure, changing only the "
        "list inside it."),
    guide=[
        ("The teaching in one sentence", [
            "There are five powers &mdash; faith, energy, mindfulness, immersion, wisdom &mdash; "
            "named in a single sentence with no elaboration, exactly as AN 5.1 named the sekhabala."]),
        ("The swap, stated precisely", [
            "Against the sekhabala&rsquo;s <em>saddhā, hiri, ottappa, vīriya, paññā</em>, this "
            "list gives <em>saddhā, vīriya, sati, samādhi, paññā</em>. Faith and wisdom are "
            "unchanged at either end; energy moves from fourth position to second; conscience and "
            "prudence are dropped entirely, replaced by mindfulness and immersion. This is exactly "
            "the substitution AN 4.163 first flagged and AN 5.1 restated in summary; here, for the "
            "first time in this series, the substituted list gets its own discourse rather than "
            "being mentioned as a comparison."]),
        ("Why call both discourses &lsquo;In Brief&rsquo;", [
            "Reusing AN 5.1&rsquo;s title is not an accident of naming. It signals that this "
            "discourse is doing for the standard bala exactly what AN 5.1 did for the sekhabala "
            "&mdash; and, as AN 5.14&rsquo;s title <em>Vitthata</em> confirms a discourse later, "
            "the same brief-then-detailed pairing that opened the last chapter opens this list "
            "within the current one. The collection reuses its own structural habits deliberately, "
            "not only its content."]),
        ("Why this list, and not the sekhabala, is the more widely known one", [
            "This five-item set, unlike the sekhabala, recurs as one of the standard groups making "
            "up the thirty-seven aids to awakening (<em>bodhipakkhiyā dhammā</em>), alongside the "
            "four kinds of mindfulness meditation, the four right efforts, the four bases of "
            "psychic power, the five faculties (an identically worded list under a different "
            "name), and the seven awakening factors. A reader meeting &lsquo;the five "
            "powers&rsquo; without qualification elsewhere in the canon should expect this list, "
            "not the sekhabala &mdash; which makes this chapter&rsquo;s earlier use of the "
            "sekhabala, under the same English chapter title, worth remembering as the exception "
            "rather than the rule."]),
        ("What follows", [
            "AN 5.14 expands each of these five in turn, including, for immersion, the full "
            "four-absorption formula this series has met many times before. AN 5.15 will then "
            "locate each of the five within a different four-item list of its own, tying this "
            "whole set to material spanning most of the aids to awakening."]),
    ],
    terms=[
        ("bala",
         "&ldquo;power&rdquo; &mdash; the general term naming both this list and the sekhabala; "
         "context, not the word itself, tells a reader which set is meant."),
        ("satibalaṁ",
         "&ldquo;power of mindfulness&rdquo; &mdash; one of the two items replacing hiri and "
         "ottappa in this version of the five powers."),
        ("samādhibalaṁ",
         "&ldquo;power of immersion&rdquo; &mdash; the second replacement, to be defined at AN "
         "5.14 by the full four-absorption formula."),
        ("bodhipakkhiyā dhammā",
         "&ldquo;aids to awakening&rdquo; &mdash; the thirty-seven-item framework this five-power "
         "list belongs to, unlike the sekhabala."),
        ("indriya",
         "&ldquo;faculty&rdquo; &mdash; the near-identical five-item list sharing this set&rsquo;s "
         "exact five terms under a different name within the aids to awakening."),
    ],
    text_intro=(
        "The discourse in full: the five powers, named once, with no elaboration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.13:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five items does AN 5.13 name?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom — the sekhabala again",
             "Faith, energy, mindfulness, immersion, wisdom — the standard five faculties/powers",
             "Ethics, immersion, wisdom, freedom",
             "A new sixth list unrelated to any earlier discourse"],
         "correct": 1,
         "expl": "The list first flagged as distinct at AN 4.163, now given its own discourse."},
        {"q": "Which two items are unchanged between the sekhabala and this list?",
         "opts": [
             "Conscience and prudence",
             "Faith and wisdom",
             "Energy and mindfulness",
             "None — all five items differ"],
         "correct": 1,
         "expl": "Saddhā and paññā anchor both versions of the list."},
        {"q": "Which two items does this list have that the sekhabala does not?",
         "opts": [
             "Conscience and prudence",
             "Mindfulness and immersion",
             "Freedom and knowledge",
             "Ethics and generosity"],
         "correct": 1,
         "expl": "Sati and samādhi replace hiri and ottappa."},
        {"q": "Why does AN 5.13 share its title, 'Saṅkhitta', with AN 5.1?",
         "opts": [
             "By pure coincidence, with no significance",
             "It signals this discourse does for the standard bala what AN 5.1 did for the "
             "sekhabala — a deliberate reuse of the same brief-then-detailed pairing",
             "Because the two discourses are actually identical texts",
             "Because AN 5.1 was misnamed and this corrects it"],
         "correct": 1,
         "expl": "The collection reuses its own structural habits, not only its content."},
        {"q": "What larger framework does this five-power list belong to, unlike the sekhabala?",
         "opts": [
             "It belongs to no larger framework",
             "The thirty-seven aids to awakening (bodhipakkhiyā dhammā)",
             "The Vinaya rules for nuns",
             "The four noble truths exclusively"],
         "correct": 1,
         "expl": "Alongside mindfulness meditation, right efforts, bases of psychic power, faculties, and awakening factors."},
        {"q": "What does the guide say a reader should expect when meeting 'the five powers' "
              "without qualification elsewhere in the canon?",
         "opts": [
             "The sekhabala, since it appeared first in this series",
             "This standard list — faith, energy, mindfulness, immersion, wisdom — since it is the "
             "one belonging to the wider aids-to-awakening framework",
             "Either list interchangeably, with no real distinction",
             "Neither list; a third, unrelated set"],
         "correct": 1,
         "expl": "This chapter's earlier use of the sekhabala is flagged as the exception, not the rule."},
        {"q": "What does AN 5.14, the next discourse, do with this list?",
         "opts": [
             "Nothing further — the list is dropped after AN 5.13",
             "Expands each of the five in turn, including the full four-absorption formula for "
             "immersion",
             "Replaces it with yet another list",
             "Returns to the sekhabala"],
         "correct": 1,
         "expl": "The 'in detail' companion this title's own name promises."},
        {"q": "What does the near-identical list called 'indriya' share with this one?",
         "opts": [
             "Nothing; they are unrelated",
             "The exact same five terms, under a different name, within the aids to awakening",
             "Only the term for wisdom",
             "It shares no terms at all"],
         "correct": 1,
         "expl": "Faculties and powers: the same five items, two different labels."},
        {"q": "How long is this discourse compared to AN 5.1?",
         "opts": [
             "Much longer",
             "About the same — a single sentence naming the five, with no elaboration",
             "AN 5.13 has no text at all",
             "AN 5.13 is ten times longer"],
         "correct": 1,
         "expl": "The same terse, bare-list form as its namesake."},
        {"q": "Where is AN 5.13 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Squirrels' Sanctuary",
             "Campā"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("The swap", [
            "sekhabala: hiri, ottappa",
            "&darr;",
            "standard: sati, samādhi",
            "&mdash; faith, wisdom, unchanged",
        ]),
        ("Same title, new list", [
            "AN 5.1: Saṅkhitta",
            "&mdash; sekhabala",
            "AN 5.13: Saṅkhitta",
            "&mdash; standard bala",
        ]),
        ("The wider framework", [
            "bodhipakkhiyā dhammā:",
            "37 aids to awakening",
            "&mdash; this list belongs here",
        ]),
        ("Cross-references", [
            "AN 4.163 &middot; first flagged the split",
            "AN 5.1 &middot; the sekhabala's own page",
            "AN 5.14 &middot; next: in detail",
        ]),
    ],
    further=[
        '<a href="%s/an5.13/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; this discourse&rsquo;s namesake '
        "and structural twin, for the sekhabala instead.",
        '<a href="an-4.163.html">AN 4.163 &middot; Ugly</a> &mdash; where the split between these '
        "two five-item lists was first flagged in this series.",
        '<a href="an-5.14.html">AN 5.14 &middot; In Detail</a> &mdash; next, expanding each of '
        "these five powers in turn.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.14 — Vitthatasutta
# --------------------------------------------------------------------------- #
page(
    14, "Vitthata", "In Detail",
    vagga=VAGGA_2,
    meta_title="AN 5.14 — In Detail | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Vitthatasutta — "
        "the standard five powers defined in turn, including the full four-absorption formula "
        "for the power of immersion. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The same five named again, then each defined in turn by a fixed formula"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The individual definitions, especially the four absorptions, are "
                              "pan-canonical formulas found across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the chapter's most detailed "
                       "discourse so far, carrying the full four-jhāna formula"),
    ],
    why=(
        "AN 5.13 promised detail and this discourse delivers it, following the identical structure "
        "AN 5.2 used for the sekhabala: each power named, then defined by <em>and what is the "
        "power of&hellip;</em>, closed by <em>this is called the power of&hellip;</em>. Faith and "
        "wisdom are defined here in the exact same words as AN 5.2 &mdash; this discourse adds "
        "nothing new for either. What is new is mindfulness and immersion, taking the place hiri "
        "and ottappa held in the earlier version, and immersion in particular brings the full "
        "four-absorption formula into this chapter for the first time."),
    guide=[
        ("The teaching in one sentence", [
            "Faith and wisdom are defined identically to AN 5.2; energy is defined identically to "
            "AN 5.2 as well; mindfulness is defined as utmost alertness and the ability to recall "
            "what was said and done long ago; immersion is defined as the four absorptions in "
            "full."]),
        ("Three definitions inherited without change", [
            "Faith (the nine-quality recollection of the Buddha), energy (roused up for giving up "
            "the unskillful and taking up the skillful), and wisdom (insight into arising and "
            "passing away) are worded here exactly as AN 5.2 worded them for the sekhabala. This "
            "discourse does not redefine any of the three terms the two lists share; a reader who "
            "has read AN 5.2 can move through these three paragraphs quickly, checking only that "
            "the wording matches."]),
        ("Mindfulness, defined by memory", [
            "The power of mindfulness is defined specifically by recall: <em>utmost mindfulness "
            "and alertness</em>, able to <em>remember and recall what was said and done long "
            "ago</em>. This is a narrower definition than &lsquo;mindfulness&rsquo; sometimes "
            "carries in translation &mdash; not present-moment awareness in general, but "
            "specifically the capacity to retain and retrieve distant memory, tested against a "
            "concrete standard rather than described introspectively."]),
        ("Immersion, defined by the four absorptions in full", [
            "Where the sekhabala left immersion out entirely, this list defines the power of "
            "immersion with the complete, formulaic description of the four <em>jhāna</em> "
            "&mdash; rapture and bliss born of seclusion; rapture and bliss born of immersion with "
            "internal clarity; equanimous bliss, mindful and aware; and finally, beyond pleasure "
            "and pain, pure equanimity and mindfulness. This exact formula appeared already in "
            "this series, discussed at length at <a href=\"an-4.163.html\">AN 4.163</a>; it is not "
            "re-explained paragraph by paragraph here, since the earlier page already did that "
            "work."]),
        ("What the definitions together imply", [
            "Laid side by side, the standard five powers cover a wider practical range than the "
            "sekhabala did: a devotional object (faith), a directional effort (energy), a memory "
            "capacity (mindfulness), a set of four meditative attainments (immersion), and a "
            "specific insight (wisdom). AN 5.15, immediately following, will make this range "
            "explicit by locating each of the five inside a different one of the canon&rsquo;s "
            "other major four-item lists."]),
    ],
    terms=[
        ("satimā",
         "&ldquo;mindful&rdquo; &mdash; qualified here by paramena satinepakkena, utmost "
         "mindfulness and alertness, and defined specifically by the capacity for distant recall."),
        ("cirakataṁ cirabhāsitaṁ",
         "&ldquo;what was done and said long ago&rdquo; &mdash; the concrete test this discourse "
         "attaches to the power of mindfulness, rather than a general description."),
        ("paṭhamaṁ jhānaṁ",
         "&ldquo;the first absorption&rdquo; &mdash; rapture and bliss born of seclusion, the first "
         "of the four states defining the power of immersion, fully discussed already at AN 4.163."),
        ("vitakkavicāra",
         "&ldquo;placing the mind and keeping it connected&rdquo; &mdash; present in the first "
         "absorption and stilled by the second, marking the transition between the two."),
        ("upekkhāsatipārisuddhi",
         "&ldquo;pure equanimity and mindfulness&rdquo; &mdash; the fourth absorption's defining "
         "quality, beyond both pleasure and pain."),
    ],
    text_intro=(
        "The discourse in full: the five named again, then each defined in turn, including the "
        "complete four-absorption formula for immersion. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five, named again"),
        ("p", "&sect;1", "an5.14:1.1-1.3"),
        ("h3", "The power of faith"),
        ("p", "&sect;2", "an5.14:2.1-2.4"),
        ("h3", "The power of energy"),
        ("p", "&sect;3", "an5.14:3.1-3.3"),
        ("h3", "The power of mindfulness"),
        ("p", "&sect;4", "an5.14:4.1-4.3"),
        ("h3", "The power of immersion"),
        ("p", "&sect;5", "an5.14:5.1-5.6"),
        ("h3", "The power of wisdom"),
        ("p", "&sect;6", "an5.14:6.1-6.4"),
    ],
    quiz=[
        {"q": "How are faith, energy, and wisdom defined in AN 5.14 compared to AN 5.2?",
         "opts": [
             "Completely differently, with new formulas",
             "Identically — the same nine-quality faith formula, the same energy formula, and the "
             "same insight-wisdom formula",
             "Only faith is defined the same way; the others differ",
             "AN 5.14 gives no definitions at all"],
         "correct": 1,
         "expl": "The three shared terms between the two lists get the identical treatment both times."},
        {"q": "How is the power of mindfulness defined here?",
         "opts": [
             "As present-moment awareness in general",
             "Specifically by the capacity for distant recall — remembering what was said and done "
             "long ago",
             "As the ability to sit still without moving",
             "As a synonym for wisdom"],
         "correct": 1,
         "expl": "A narrower, more concrete definition than 'mindfulness' sometimes carries."},
        {"q": "How is the power of immersion defined?",
         "opts": [
             "As a single moment of calm",
             "By the complete, formulaic description of all four absorptions",
             "As the absence of thought entirely, with no further detail",
             "Immersion is not defined in this discourse"],
         "correct": 1,
         "expl": "The full four-jhāna formula, already discussed at length at AN 4.163."},
        {"q": "Where was the four-absorption formula already discussed at length in this series?",
         "opts": [
             "It has never appeared before this page",
             "AN 4.163",
             "AN 5.1",
             "AN 2.1–10"],
         "correct": 1,
         "expl": "The guide cross-references rather than re-explaining the formula paragraph by paragraph."},
        {"q": "What replaces hiri and ottappa in this version of the five powers, compared to the "
              "sekhabala?",
         "opts": [
             "Ethics and generosity",
             "Mindfulness and immersion",
             "Nothing; the list is otherwise identical",
             "Faith and energy"],
         "correct": 1,
         "expl": "The substitution first flagged at AN 4.163, now given full definitions."},
        {"q": "What does the guide say the five definitions together cover, when laid side by "
              "side?",
         "opts": [
             "Five nearly identical restatements of the same idea",
             "A wide practical range — a devotional object, a directional effort, a memory "
             "capacity, four meditative attainments, and a specific insight",
             "Only doctrinal categories, with no practical content",
             "Nothing distinguishable between the five"],
         "correct": 1,
         "expl": "A genuinely varied set of capacities, not five synonyms."},
        {"q": "What does AN 5.15, the next discourse, do with this same list?",
         "opts": [
             "Nothing further; the list is dropped",
             "Locates each of the five inside a different one of the canon's other major four-item "
             "lists",
             "Replaces the five with an entirely new set",
             "Returns to the sekhabala one more time"],
         "correct": 1,
         "expl": "Making the range implied by AN 5.14's definitions explicit."},
        {"q": "What is the defining quality of the fourth absorption, as given here?",
         "opts": [
             "Intense rapture and bliss",
             "Beyond pleasure and pain, with pure equanimity and mindfulness",
             "Complete unconsciousness",
             "Physical stillness only, with the mind still active"],
         "correct": 1,
         "expl": "Upekkhāsatipārisuddhi — the formula's final term."},
        {"q": "What marks the transition from the first to the second absorption in this formula?",
         "opts": [
             "The stilling of placing the mind and keeping it connected (vitakkavicāra)",
             "The arising of physical pain",
             "A change of physical posture",
             "The ending of all mental activity"],
         "correct": 0,
         "expl": "Present in the first absorption, stilled by the second."},
        {"q": "Where is AN 5.14 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Rājagaha",
             "Kapilavatthu"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("Five, defined", [
            "faith &mdash; unchanged from 5.2",
            "energy &mdash; unchanged",
            "mindfulness &mdash; distant recall",
            "immersion &mdash; four jhānas",
            "wisdom &mdash; unchanged",
        ]),
        ("The four absorptions", [
            "1st: rapture, bliss, seclusion",
            "2nd: rapture, bliss, clarity",
            "3rd: equanimous bliss",
            "4th: pure equanimity",
        ]),
        ("Inherited, not new", [
            "faith, energy, wisdom:",
            "identical to AN 5.2",
        ]),
        ("Cross-references", [
            "AN 5.2 &middot; the sekhabala's own detail",
            "AN 4.163 &middot; the jhāna formula in full",
            "AN 5.15 &middot; next: located in fours",
        ]),
    ],
    further=[
        '<a href="%s/an5.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.2.html">AN 5.2 &middot; In Detail</a> &mdash; this discourse&rsquo;s '
        "structural twin, defining the sekhabala instead.",
        '<a href="an-4.163.html">AN 4.163 &middot; Ugly</a> &mdash; where the four-absorption '
        "formula used here for immersion was already discussed at length.",
        '<a href="an-5.15.html">AN 5.15 &middot; Should Be Seen</a> &mdash; next, locating each of '
        "these five powers within a different four-item list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.15 — Daṭṭhabbasutta
# --------------------------------------------------------------------------- #
page(
    15, "Daṭṭhabba", "Should Be Seen",
    vagga=VAGGA_2,
    meta_title="AN 5.15 — Should Be Seen | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Daṭṭhabbasutta — each "
        "of the five powers located inside a different one of the canon's other major four-item "
        "lists: the four factors of stream-entry, the four right efforts, the four kinds of "
        "mindfulness meditation, the four absorptions, and the four noble truths. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five question-and-answer pairs, one per power, each naming a different fourfold "
                 "list as the place that power 'should be seen'"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Cross-mapping the powers onto other core doctrinal fours is a "
                              "structural device widespread across the Chinese Āgamas and "
                              "Abhidharma; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short lines, but each answer "
                       "opens onto a large body of material this series has already covered"),
    ],
    why=(
        "AN 5.14 defined the five powers one at a time, in isolation. This discourse does "
        "something more ambitious: it asks, for each power, <em>where should it be seen</em>, and "
        "answers with a different major fourfold category every time &mdash; stream-entry, right "
        "effort, mindfulness meditation, absorption, the noble truths. Five powers, five distinct "
        "fours. The discourse is, in effect, a compressed map of how one five-item list touches "
        "five different regions of the wider teaching."),
    guide=[
        ("The teaching in one sentence", [
            "Faith should be seen in the four factors of stream-entry; energy in the four right "
            "efforts; mindfulness in the four kinds of mindfulness meditation; immersion in the "
            "four absorptions; wisdom in the four noble truths."]),
        ("A map, not five new definitions", [
            "This discourse does not redefine any of the five powers &mdash; AN 5.14 already did "
            "that. Instead it answers a different question: not <em>what is</em> this power, but "
            "<em>where is it visible</em>, in practice, at scale. The verb <em>daṭṭhabba</em>, "
            "should be seen, treats each power as something observable in a larger, already "
            "familiar structure rather than as an abstraction requiring further definition."]),
        ("Four fours, briefly placed", [
            "The <em>sotāpattiyaṅga</em>, already discussed at "
            "<a href=\"an-4.52.html\">AN 4.52</a>, are the qualities of a stream-enterer; the "
            "<em>sammappadhāna</em>, discussed at <a href=\"an-4.69.html\">AN 4.69</a>, are the "
            "four right efforts; the <em>satipaṭṭhāna</em>, discussed at "
            "<a href=\"an-4.274.html\">AN 4.274</a>, are the four kinds of mindfulness meditation; "
            "and the four absorptions were discussed at length already this chapter, at AN 5.14 "
            "and, before that, AN 4.163. Each of those earlier pages does the explaining; this "
            "discourse only does the pointing."]),
        ("The fifth pairing, left unglossed elsewhere", [
            "Wisdom&rsquo;s placement in the four noble truths is the one pairing this series has "
            "not yet given its own dedicated page. That is worth noting rather than papering over: "
            "the four noble truths are foundational enough in the wider canon that this series, so "
            "far concerned with the numbered discourses specifically, has had less occasion to "
            "treat them as their own subject. This discourse is, so far, the fullest treatment "
            "they have received here."]),
        ("What the five pairings add up to", [
            "Read together, the five answers cover an unusually wide swath of the aids to "
            "awakening in a single short discourse: stream-entry factors, right efforts, "
            "mindfulness meditation, absorption, and the noble truths. A mendicant who has "
            "developed the five powers, on this discourse&rsquo;s account, is not developing five "
            "isolated skills but is visibly active across most of the frameworks this whole "
            "tradition organizes its practice around."]),
    ],
    terms=[
        ("sotāpattiyaṅga",
         "&ldquo;factor of stream-entry&rdquo; &mdash; the fourfold set faith is located within "
         "here, already discussed at AN 4.52."),
        ("sammappadhāna",
         "&ldquo;right effort&rdquo; &mdash; the fourfold set energy is located within, already "
         "discussed at AN 4.69."),
        ("satipaṭṭhāna",
         "&ldquo;establishment of mindfulness&rdquo; &mdash; the fourfold set mindfulness is "
         "located within, already discussed at AN 4.274."),
        ("daṭṭhabba",
         "&ldquo;should be seen&rdquo; &mdash; the verb giving this discourse its title, treating "
         "each power as observable within a larger structure rather than requiring further "
         "definition."),
        ("ariyasacca",
         "&ldquo;noble truth&rdquo; &mdash; the fourfold set wisdom is located within; unlike the "
         "other four sets, not yet given its own dedicated page in this series."),
    ],
    text_intro=(
        "The discourse in full: the five powers named, then each located within a different "
        "fourfold category. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five, named"),
        ("p", "&sect;1", "an5.15:1.1-1.3"),
        ("h3", "Faith, in the four factors of stream-entry"),
        ("p", "&sect;2", "an5.15:1.4-1.5"),
        ("h3", "Energy, in the four right efforts"),
        ("p", "&sect;3", "an5.15:1.7-1.8"),
        ("h3", "Mindfulness, in the four kinds of mindfulness meditation"),
        ("p", "&sect;4", "an5.15:1.10-1.11"),
        ("h3", "Immersion, in the four absorptions"),
        ("p", "&sect;5", "an5.15:1.13-1.14"),
        ("h3", "Wisdom, in the four noble truths"),
        ("p", "&sect;6", "an5.15:1.16-1.17"),
        ("h3", "Closing"),
        ("p", "&sect;7", "an5.15:1.19"),
    ],
    quiz=[
        {"q": "What question does AN 5.15 ask about each of the five powers?",
         "opts": [
             "What is this power, in full definition",
             "Where should this power be seen — daṭṭhabba — within a larger fourfold category",
             "Who first taught this power",
             "How long does this power take to develop"],
         "correct": 1,
         "expl": "A map of visibility, not a set of new definitions."},
        {"q": "Where should the power of faith be seen, according to this discourse?",
         "opts": [
             "In the four right efforts",
             "In the four factors of stream-entry",
             "In the four noble truths",
             "In the four absorptions"],
         "correct": 1,
         "expl": "Already discussed at AN 4.52."},
        {"q": "Where should the power of energy be seen?",
         "opts": [
             "In the four kinds of mindfulness meditation",
             "In the four right efforts",
             "In the four noble truths",
             "In the four factors of stream-entry"],
         "correct": 1,
         "expl": "Sammappadhāna, already discussed at AN 4.69."},
        {"q": "Where should the power of wisdom be seen?",
         "opts": [
             "In the four absorptions",
             "In the four right efforts",
             "In the four noble truths",
             "In the four factors of stream-entry"],
         "correct": 2,
         "expl": "The one pairing this series has not yet treated as its own dedicated subject."},
        {"q": "Does this discourse redefine any of the five powers?",
         "opts": [
             "Yes, all five are redefined from scratch",
             "No — AN 5.14 already defined them; this discourse only locates them",
             "Only wisdom is redefined",
             "Only faith is redefined"],
         "correct": 1,
         "expl": "A different question is being asked here: not what, but where visible."},
        {"q": "According to the guide, why has the four noble truths pairing not been given its "
              "own dedicated page elsewhere in this series?",
         "opts": [
             "Because the four noble truths are not part of the canon",
             "Because this series, concerned specifically with the numbered discourses, has had "
             "less occasion to treat them as their own subject until now",
             "Because the four noble truths are considered a later addition",
             "Because they are identical to the four right efforts"],
         "correct": 1,
         "expl": "This discourse is, so far, the fullest treatment they have received in this series."},
        {"q": "Where was the four-absorption formula, used here for immersion, already discussed "
              "at length in this series?",
         "opts": [
             "Nowhere before this page",
             "AN 5.14 and, before that, AN 4.163",
             "Only in a future, not-yet-written chapter",
             "AN 2.1–10"],
         "correct": 1,
         "expl": "This discourse points to material already covered rather than re-explaining it."},
        {"q": "What does the guide say a mendicant who has developed all five powers is doing, on "
              "this discourse's account?",
         "opts": [
             "Developing five entirely isolated, unrelated skills",
             "Visibly active across most of the frameworks the tradition organizes its practice "
             "around — stream-entry, right effort, mindfulness, absorption, and the noble truths",
             "Practicing only meditation, with nothing else relevant",
             "Nothing observable in any other framework"],
         "correct": 1,
         "expl": "An unusually wide swath of the aids to awakening covered in one short discourse."},
        {"q": "What form does the discourse take?",
         "opts": [
             "An extended narrative parable",
             "Five question-and-answer pairs, one per power",
             "A dialogue between two named monks",
             "A single unbroken paragraph with no structure"],
         "correct": 1,
         "expl": "Kattha ca... daṭṭhabbaṁ, asked and answered five times in a row."},
        {"q": "Where is AN 5.15 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Great Wood at Vesālī",
             "Ghosita's Monastery"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("The five mappings", [
            "faith &rarr; stream-entry",
            "energy &rarr; right efforts",
            "mindfulness &rarr; satipaṭṭhāna",
            "immersion &rarr; 4 jhānas",
            "wisdom &rarr; noble truths",
        ]),
        ("Already covered", [
            "AN 4.52, 4.69, 4.274,",
            "AN 4.163 &amp; 5.14",
            "&mdash; four of five, explained",
        ]),
        ("One left fresh", [
            "the four noble truths:",
            "not yet its own page,",
            "until this discourse",
        ]),
        ("Cross-references", [
            "AN 5.14 &middot; the five, defined",
            "AN 4.52, 4.69, 4.274 &middot; the fours",
            "AN 5.16 &middot; next: the peak, again",
        ]),
    ],
    further=[
        '<a href="%s/an5.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.14.html">AN 5.14 &middot; In Detail</a> &mdash; the previous discourse, '
        "where these same five powers were fully defined.",
        '<a href="an-4.52.html">AN 4.52</a> &mdash; the four factors of stream-entry, faith&rsquo;s '
        "home in this discourse's mapping.",
        '<a href="an-5.16.html">AN 5.16 &middot; The Peak, Again</a> &mdash; next, restating AN '
        "5.12's simile for this list's own wisdom.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.16 — Punakūṭasutta
# --------------------------------------------------------------------------- #
page(
    16, "Punakūṭa", "The Peak, Again",
    vagga=VAGGA_2,
    meta_title="AN 5.16 — The Peak, Again | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Punakūṭasutta — AN "
        "5.12's bungalow-peak simile restated, this time for the standard five powers rather "
        "than the sekhabala, with the identical claim that wisdom is chief. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.12's formula and simile, restated word for word with the standard five "
                 "powers in place of the sekhabala"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, its interest lying "
                       "entirely in what it confirms rather than what it adds"),
    ],
    why=(
        "The title says it plainly: <em>puna</em>, again. This discourse takes AN 5.12&rsquo;s "
        "claim that wisdom is chief among the powers, and its bungalow-peak simile, and restates "
        "both without change &mdash; except that the powers in question are now the standard five, "
        "faith, energy, mindfulness, immersion, wisdom, rather than the sekhabala. It is the "
        "clearest confirmation this chapter offers that its ranking of wisdom is not tied to one "
        "particular five-item list, but survives the switch between the two."),
    guide=[
        ("The teaching in one sentence", [
            "Of the five powers &mdash; faith, energy, mindfulness, immersion, wisdom &mdash; "
            "wisdom is the chief, holding and binding everything together, exactly as AN 5.12 said "
            "of the sekhabala."]),
        ("What changed, and what did not", [
            "Compare the two discourses directly and the only substitution is the noun phrase "
            "naming which five items are meant. The verbs, the simile, the ranking claim, even the "
            "sentence structure are unchanged. This is a stronger form of repetition than anything "
            "seen so far in the Fives &mdash; not a formula reused with one qualifier added, as at "
            "AN 5.9, but the identical argument transplanted wholesale onto a different list."]),
        ("Why this particular repetition earns its own discourse", [
            "A skeptical reader might ask why the collection needed two separate discourses to "
            "make one claim about two different lists, rather than a single discourse noting the "
            "claim holds for both. The likely answer, consistent with the reasoning offered "
            "already at AN 5.9, is that each five-item list circulates and is chanted as its own "
            "self-contained unit; a claim about the sekhabala does not automatically transfer, in "
            "oral practice, to the bala unless it is actually stated for the bala as well."]),
        ("A ranking now doubly confirmed", [
            "With this discourse, wisdom&rsquo;s status as chief has been claimed for both of this "
            "chapter&rsquo;s five-item power lists, in the same words, using the same image. A "
            "reader who has followed the chapter this far has now seen the strongest possible "
            "statement, within this material, that whichever version of &lsquo;the five "
            "powers&rsquo; is under discussion, wisdom is being treated as what completes and "
            "secures the rest."]),
        ("What follows", [
            "AN 5.17 turns the chapter toward a different concern entirely: not the five powers at "
            "all, but a different five-item set &mdash; ethics, immersion, wisdom, freedom, and "
            "the knowledge and vision of freedom &mdash; and whether a mendicant who has them "
            "shares them with others. The four discourses closing this chapter, AN 5.17 through "
            "5.20, form their own self-contained unit."]),
    ],
    terms=[
        ("puna",
         "&ldquo;again&rdquo; &mdash; the word giving this discourse its title, marking it as a "
         "deliberate restatement rather than new material."),
        ("kūṭa",
         "&ldquo;peak, roof-ridge&rdquo; &mdash; the identical image from AN 5.12, transplanted "
         "here without change."),
        ("bala",
         "&ldquo;power&rdquo; &mdash; here unambiguously the standard five powers, following the "
         "pivot made at AN 5.13."),
        ("agga",
         "&ldquo;chief, foremost&rdquo; &mdash; the ranking word applied to wisdom a second time, "
         "now for a second five-item list."),
        ("saṅgāhika saṅghātaniya",
         "&ldquo;that which holds together, that which binds together&rdquo; &mdash; the paired "
         "verbs from AN 5.12, repeated here word for word."),
    ],
    text_intro=(
        "The discourse in full: the standard five powers restated, wisdom named chief a second "
        "time, and the identical bungalow simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Wisdom, the chief power, restated"),
        ("p", "&sect;1", "an5.16:1.1-1.7"),
    ],
    quiz=[
        {"q": "What does the title 'Punakūṭa' mean, and what does it signal?",
         "opts": [
             "'New peak' — an entirely new claim",
             "'The peak, again' — a deliberate restatement of AN 5.12's claim and simile",
             "'False peak' — a claim being corrected",
             "'Distant peak' — unrelated content"],
         "correct": 1,
         "expl": "Puna, again, marking this as repetition rather than new material."},
        {"q": "What changes between AN 5.12 and AN 5.16?",
         "opts": [
             "Nothing at all — the two discourses are identical in every respect",
             "Only which five-item list is named — sekhabala at AN 5.12, the standard bala here",
             "The ranking itself changes; a different power is named chief",
             "The simile changes entirely"],
         "correct": 1,
         "expl": "Verbs, simile, and ranking claim unchanged; only the noun phrase for which five items is meant."},
        {"q": "How does the guide characterize this repetition compared to AN 5.9's modification of "
              "AN 5.8?",
         "opts": [
             "As identical in kind — both add a small qualifier",
             "As a stronger form of repetition — the identical argument transplanted wholesale onto "
             "a different list, not a formula with one qualifier added",
             "As entirely unrelated phenomena",
             "AN 5.16 is described as adding much more than AN 5.9 did"],
         "correct": 1,
         "expl": "A word-for-word transplant rather than a modification."},
        {"q": "Why does the guide suggest the collection needed a separate discourse for this "
              "repeated claim, rather than one discourse noting it for both lists?",
         "opts": [
             "There is no plausible reason, and it is treated as a pure copying error",
             "Each five-item list circulates as its own chanted unit; a claim doesn't automatically "
             "transfer between lists in oral practice unless stated for each",
             "Because AN 5.12 was considered incomplete",
             "Because the two lists are considered doctrinally incompatible"],
         "correct": 1,
         "expl": "The same reasoning already offered at AN 5.9 for a similar case."},
        {"q": "After AN 5.16, for how many of this chapter's five-item power lists has wisdom now "
              "been claimed as chief?",
         "opts": [
             "None", "Only the sekhabala", "Both the sekhabala and the standard bala",
             "Three separate lists"],
         "correct": 2,
         "expl": "The strongest possible statement, within this material, of wisdom's completing role."},
        {"q": "What does AN 5.17, the next discourse, turn the chapter toward?",
         "opts": [
             "A third five-item power list",
             "A different five-item set entirely — ethics, immersion, wisdom, freedom, and the "
             "knowledge and vision of freedom — and whether it is shared with others",
             "A return to the tathāgatabala",
             "The end of the chapter with no further content"],
         "correct": 1,
         "expl": "AN 5.17–20 form the chapter's own closing unit, on a related but distinct topic."},
        {"q": "Is the bungalow-peak simile itself altered in any way at AN 5.16?",
         "opts": [
             "Yes, extensively rewritten",
             "No — it is repeated word for word from AN 5.12",
             "Only the roof material is changed",
             "The simile is dropped entirely"],
         "correct": 1,
         "expl": "The identical image, transplanted onto the new list."},
        {"q": "What are the five powers named in this discourse?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Faith, energy, mindfulness, immersion, wisdom",
             "Ethics, immersion, wisdom, freedom",
             "A new sixth list"],
         "correct": 1,
         "expl": "The standard bala, following the chapter's pivot at AN 5.13."},
        {"q": "How long is AN 5.16 compared to AN 5.12?",
         "opts": [
             "Much shorter, missing the simile",
             "About the same length, containing the full formula and simile in one paragraph",
             "Much longer, with added explanation",
             "AN 5.16 has no text at all"],
         "correct": 1,
         "expl": "A close match, since the content is a direct restatement."},
        {"q": "Where is AN 5.16 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Isipatana",
             "The Mango Grove at Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("Twice claimed", [
            "AN 5.12: sekhabala",
            "&mdash; wisdom, chief",
            "AN 5.16: standard bala",
            "&mdash; wisdom, chief",
        ]),
        ("Unchanged", [
            "the simile,",
            "the verbs,",
            "the ranking &mdash; all the same",
        ]),
        ("Only difference", [
            "which five items",
            "are being named",
        ]),
        ("Cross-references", [
            "AN 5.12 &middot; the first statement",
            "AN 5.9 &middot; why repeat in full",
            "AN 5.17 &middot; next: a new topic",
        ]),
    ],
    further=[
        '<a href="%s/an5.16/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.12.html">AN 5.12 &middot; Peak</a> &mdash; the discourse this page restates '
        "word for word, for the sekhabala instead.",
        '<a href="an-5.9.html">AN 5.9 &middot; Disrespect (1st)</a> &mdash; the earlier case of a '
        "formula restated in full for oral-transmission reasons.",
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; next, and the '
        "start of this chapter's closing four-discourse unit.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.17 — Paṭhamahitasutta
# --------------------------------------------------------------------------- #
page(
    17, "Paṭhamahita", "One&rsquo;s Own Welfare",
    vagga=VAGGA_2,
    meta_title="AN 5.17 — One's Own Welfare | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first Hitasutta — a "
        "mendicant personally accomplished in ethics, immersion, wisdom, freedom, and the "
        "knowledge and vision of freedom, but who does not encourage others in them, is said to "
        "practice for their own welfare only. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A five-part accomplishment, each item paired with a failure to encourage others "
                 "in it, opening a four-discourse unit closing the chapter"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Ethics, immersion, wisdom, freedom, and the knowledge and vision of "
                              "freedom correspond closely to the wǔfēn fǎshēn 五分法身, the "
                              "'five-part dharma body' of ethics, immersion, wisdom, liberation, "
                              "and the knowledge and vision of liberation, a formula well attested "
                              "in Chinese Buddhist literature and commentary"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; introduces a new five-item set "
                       "distinct from every list this chapter has used so far"),
    ],
    why=(
        "This discourse opens the chapter's final unit by dropping the powers entirely and "
        "introducing a different, and in some ways more consequential, five-item set: personal "
        "accomplishment in ethics, immersion, wisdom, freedom, and the knowledge and vision of "
        "freedom. A mendicant who has all five but keeps them to themselves &mdash; personally "
        "accomplished, but <em>not encouraging others</em> &mdash; is said to be practicing for "
        "their own welfare only. Attainment alone, on this account, is not the whole of what a "
        "mendicant's life is asked to do."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant personally accomplished in ethics, immersion, wisdom, freedom, and the "
            "knowledge and vision of freedom, but who does not encourage others to develop the "
            "same five, is practicing for their own welfare but not that of others."]),
        ("A new list, worth naming precisely", [
            "<em>Sīla, samādhi, paññā, vimutti, vimuttiñāṇadassana</em> &mdash; ethics, immersion, "
            "wisdom, freedom, and the knowledge and vision of freedom &mdash; is a five-item "
            "sequence distinct from both the sekhabala and the standard bala this chapter has used "
            "so far. It closely resembles the fourfold sequence that opened AN 4.1 in the last "
            "nipāta &mdash; ethics, immersion, wisdom, freedom &mdash; with one further item "
            "appended: not just freedom itself, but the knowing and seeing that one is free."]),
        ("A well-attested formula beyond this collection", [
            "This exact five-part sequence corresponds closely to what became known in Chinese "
            "Buddhist literature as the <em>wǔfēn fǎshēn</em> 五分法身, the &lsquo;five-part "
            "dharma-body&rsquo;: 戒 ethics, 定 immersion, 慧 wisdom, 解脫 liberation, and 解脫知見 "
            "the knowledge and vision of liberation. Where this reading guide has generally hedged "
            "its Northern-parallel claims across the collection, this is one of the more solid "
            "correspondences available: the same five items, in the same order, doing comparable "
            "work as a description of what a fully accomplished practitioner has attained."]),
        ("The structure of the whole unit", [
            "AN 5.17 through 5.20 run through every logical combination of two variables: is the "
            "mendicant personally accomplished, and do they encourage others. AN 5.17 gives "
            "yes-and-no; AN 5.18, the next discourse, gives no-and-yes; AN 5.19 gives no-and-no; "
            "AN 5.20 gives yes-and-yes, closing the chapter. Reading all four in sequence is more "
            "informative than reading any one alone, since the four cases only become a complete "
            "picture together."]),
        ("What this discourse implies, read on its own", [
            "It is worth sitting with what AN 5.17 is actually saying before the fuller picture "
            "arrives: personal attainment, however genuine, is explicitly described here as only "
            "half of welfare when it is not shared. The discourse does not call this a failure or "
            "a fault &mdash; it does not criticize the mendicant it describes &mdash; but it does "
            "decline to call their practice complete."]),
    ],
    terms=[
        ("sīlasampanno",
         "&ldquo;accomplished in ethics&rdquo; &mdash; the first of five personal accomplishments "
         "named in this discourse."),
        ("vimutti",
         "&ldquo;freedom, liberation&rdquo; &mdash; the fourth item, already met as the culmination "
         "of AN 4.1's own fourfold list in the previous nipāta."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the fifth item, added beyond "
         "AN 4.1's four: not only being free, but knowing and seeing that one is."),
        ("samādapeti",
         "&ldquo;encourages, instigates&rdquo; &mdash; the verb whose absence, paired with "
         "personal accomplishment, defines this discourse's case."),
        ("attahita parahita",
         "&ldquo;one's own welfare, others' welfare&rdquo; &mdash; the two variables this "
         "four-discourse unit runs through every combination of."),
    ],
    text_intro=(
        "The discourse in full: personal accomplishment in the five, without encouraging others "
        "in them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Accomplished, but not encouraging others"),
        ("p", "&sect;1", "an5.17:1.1-1.8"),
    ],
    quiz=[
        {"q": "What five items does AN 5.17 introduce, distinct from the powers used earlier in "
              "this chapter?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Ethics, immersion, wisdom, freedom, and the knowledge and vision of freedom",
             "Generosity, ethics, patience, energy, wisdom",
             "The same sekhabala under a new name"],
         "correct": 1,
         "expl": "A new five-item sequence opening the chapter's closing unit."},
        {"q": "What does AN 5.17 say about a mendicant personally accomplished in all five but not "
              "encouraging others?",
         "opts": [
             "That they have failed completely",
             "That they are practicing for their own welfare, but not that of others",
             "That their accomplishment is not genuine",
             "The discourse says nothing about this case"],
         "correct": 1,
         "expl": "Attainment described as real, but only half of welfare when unshared."},
        {"q": "What Chinese Buddhist formula does the guide identify as a close correspondence to "
              "this five-item list?",
         "opts": [
             "The Three Refuges",
             "五分法身, the 'five-part dharma-body' — ethics, immersion, wisdom, liberation, and "
             "the knowledge and vision of liberation",
             "The Six Pāramitās",
             "The Twelve Links of Dependent Origination"],
         "correct": 1,
         "expl": "One of the more solid Northern-parallel correspondences this reading guide identifies."},
        {"q": "How does this five-item list relate to AN 4.1's opening list from the previous "
              "nipāta?",
         "opts": [
             "It is completely unrelated",
             "It closely resembles AN 4.1's ethics-immersion-wisdom-freedom sequence, with one "
             "further item appended — the knowledge and vision of freedom",
             "It contradicts AN 4.1's list",
             "It replaces ethics with a different term"],
         "correct": 1,
         "expl": "Four items shared, with vimuttiñāṇadassana added as a fifth."},
        {"q": "What two variables does the AN 5.17–20 unit run through every combination of?",
         "opts": [
             "Age and gender",
             "Whether a mendicant is personally accomplished, and whether they encourage others",
             "Monastic seniority and lay status",
             "Wealth and poverty"],
         "correct": 1,
         "expl": "Four discourses, four logical combinations."},
        {"q": "What combination does AN 5.17 specifically describe?",
         "opts": [
             "Not accomplished, and not encouraging others",
             "Accomplished, but not encouraging others",
             "Not accomplished, but encouraging others",
             "Accomplished, and encouraging others"],
         "correct": 1,
         "expl": "Yes-and-no — the first of the four cases."},
        {"q": "Does AN 5.17 explicitly criticize or condemn the mendicant it describes?",
         "opts": [
             "Yes, in strong terms",
             "No — it declines to call their practice complete, without calling it a fault",
             "Yes, it predicts a bad rebirth for them",
             "The discourse takes no position either way, offering no description at all"],
         "correct": 1,
         "expl": "A description of incompleteness, not a condemnation."},
        {"q": "What does AN 5.18, the next discourse, describe?",
         "opts": [
             "The identical case as AN 5.17",
             "The reverse combination — not personally accomplished, but encouraging others",
             "Both accomplished and encouraging others",
             "Neither accomplished nor encouraging others"],
         "correct": 1,
         "expl": "The second of the unit's four logical combinations."},
        {"q": "Is personal attainment described as false or fraudulent in this discourse?",
         "opts": [
             "Yes, entirely fraudulent",
             "No — the accomplishment described is treated as genuine; only its being unshared is "
             "noted",
             "The discourse is ambiguous on this point",
             "The discourse denies attainment is possible at all"],
         "correct": 1,
         "expl": "Genuine accomplishment, explicitly described as only half of welfare when kept private."},
        {"q": "Where is AN 5.17 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Hot Springs Monastery",
             "Sāketa"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("The five", [
            "<span class=\"pali\">sīla</span>ethics",
            "<span class=\"pali\">samādhi</span>immersion",
            "<span class=\"pali\">paññā</span>wisdom",
            "<span class=\"pali\">vimutti</span>freedom",
            "<span class=\"pali\">vimuttiñāṇadassana</span>knowledge &amp; vision of it",
        ]),
        ("A solid parallel", [
            "五分法身 wǔfēn fǎshēn",
            "戒定慧解脫解脫知見",
            "&mdash; the same five, in order",
        ]),
        ("This discourse's case", [
            "accomplished: yes",
            "encourages others: no",
            "&rarr; own welfare only",
        ]),
        ("Cross-references", [
            "AN 4.1 &middot; the four-item ancestor",
            "AN 5.18 &middot; next: the reverse case",
            "AN 5.20 &middot; both, closing the chapter",
        ]),
    ],
    further=[
        '<a href="%s/an5.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; the four-item ancestor of '
        "this discourse's five, from the previous nipāta.",
        '<a href="an-5.18.html">AN 5.18 &middot; Welfare of Others (2nd)</a> &mdash; next, the '
        "reverse case in this four-discourse unit.",
        '<a href="an-5.20.html">AN 5.20 &middot; The Welfare of Both</a> &mdash; the unit&rsquo;s '
        "closing case, and this chapter's final discourse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.18 — Dutiyahitasutta
# --------------------------------------------------------------------------- #
page(
    18, "Dutiyahita", "Welfare of Others (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 5.18 — Welfare of Others (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Hitasutta — the "
        "reverse of AN 5.17: a mendicant not personally accomplished in the five, but who "
        "encourages others in them anyway, practices for the welfare of others but not their "
        "own. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.17's formula inverted: absence of personal accomplishment paired with "
                 "encouraging others anyway"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.17"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the second of four cases, "
                       "best read against its predecessor"),
    ],
    why=(
        "AN 5.17 described someone accomplished but silent. This discourse describes the mirror "
        "case: a mendicant <em>not</em> personally accomplished in ethics, immersion, wisdom, "
        "freedom, or the knowledge and vision of freedom, who nonetheless <em>encourages others</em> "
        "in all five. The discourse calls this practicing for the welfare of others, but not one's "
        "own &mdash; a case at least as uncomfortable as the first, and one this reading guide will "
        "not soften."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant not personally accomplished in the five, but who encourages others in "
            "them, is practicing for the welfare of others but not their own &mdash; the exact "
            "inverse of AN 5.17."]),
        ("A harder case than it first appears", [
            "It would be easy to read this discourse as praising the mendicant it describes, since "
            "encouraging others sounds generous. But the discourse is precise: this person is "
            "<em>not</em> accomplished in what they are encouraging others toward. Whatever else "
            "this case is, the discourse does not claim it is safer or more admirable than AN "
            "5.17's; it simply names it as the other incomplete half of the same pair."]),
        ("Not a license to teach beyond one's attainment", [
            "Read alongside AN 5.17, the two discourses together resist an easy resolution in "
            "either direction &mdash; toward pure self-cultivation with no concern for others, or "
            "toward outward teaching with no concern for one's own practice. Both are named "
            "explicitly as incomplete. Neither discourse tells a reader which incompleteness is "
            "worse; that judgment is left unmade."]),
        ("The same five items, unchanged", [
            "Ethics, immersion, wisdom, freedom, and the knowledge and vision of freedom &mdash; "
            "AN 5.17 already introduced and glossed all five, including the Northern parallel to "
            "the 五分法身. This discourse adds no new definition of any of them; it only inverts "
            "which half of the formula is affirmed and which is negated."]),
        ("Two cases down, two to go", [
            "AN 5.19, next, gives the case where neither condition holds: not accomplished, and "
            "not encouraging others. AN 5.20 then closes the chapter with the case where both "
            "hold. The four discourses are best understood as a single argument in four parts, "
            "not four independent teachings."]),
    ],
    terms=[
        ("na sīlasampanno",
         "&ldquo;not accomplished in ethics&rdquo; &mdash; the negated form of AN 5.17's first "
         "term, marking this discourse's inverted case."),
        ("paraṁ samādapeti",
         "&ldquo;encourages another&rdquo; &mdash; the affirmed half of this discourse's formula, "
         "unchanged in wording from AN 5.17."),
        ("parahita",
         "&ldquo;welfare of others&rdquo; &mdash; the outcome this discourse attaches to its "
         "described case, without qualifying it as praiseworthy."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the fifth item of the shared "
         "list, here also negated for the mendicant being described."),
        ("dutiya",
         "&ldquo;second&rdquo; &mdash; the ordinal in this discourse's title, marking it as the "
         "second of the unit's four cases."),
    ],
    text_intro=(
        "The discourse in full: absence of personal accomplishment, paired with encouraging others "
        "anyway. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Not accomplished, but encouraging others"),
        ("p", "&sect;1", "an5.18:1.1-1.8"),
    ],
    quiz=[
        {"q": "What is the case AN 5.18 describes?",
         "opts": [
             "Personally accomplished, and encouraging others",
             "Not personally accomplished in the five, but encouraging others in them anyway",
             "Neither accomplished nor encouraging others",
             "Personally accomplished, but not encouraging others"],
         "correct": 1,
         "expl": "The exact inverse of AN 5.17's case."},
        {"q": "Does the guide read this discourse as straightforwardly praising the mendicant it "
              "describes?",
         "opts": [
             "Yes, entirely positively",
             "No — the discourse names this as the other incomplete half of the pair, not as safer "
             "or more admirable than AN 5.17's case",
             "The discourse condemns the mendicant outright",
             "The guide takes no interpretive position at all"],
         "correct": 1,
         "expl": "Both cases are named as incomplete, without ranking one above the other."},
        {"q": "What outcome does AN 5.18 attach to this case?",
         "opts": [
             "Practicing for the welfare of others, but not their own",
             "Practicing for neither welfare",
             "Practicing for both welfares equally",
             "No outcome is stated"],
         "correct": 0,
         "expl": "The mirror outcome to AN 5.17's 'own welfare, not others'."},
        {"q": "Does AN 5.18 introduce any new definition for the five items — ethics, immersion, "
              "wisdom, freedom, knowledge and vision of freedom?",
         "opts": [
             "Yes, all five are redefined",
             "No — AN 5.17 already defined them; this discourse only inverts which half is "
             "affirmed and which negated",
             "Only freedom is redefined",
             "The five items are entirely different from AN 5.17's"],
         "correct": 1,
         "expl": "The same five items throughout this four-discourse unit."},
        {"q": "According to the guide, do AN 5.17 and 5.18 together resolve toward pure "
              "self-cultivation or toward pure outward teaching?",
         "opts": [
             "Toward pure self-cultivation",
             "Toward pure outward teaching",
             "Neither — both extremes are named explicitly as incomplete, with no resolution given",
             "The discourses do not address this question"],
         "correct": 2,
         "expl": "Neither discourse tells a reader which incompleteness is worse."},
        {"q": "What does AN 5.19, the next discourse, describe?",
         "opts": [
             "Both accomplished and encouraging others",
             "Neither accomplished nor encouraging others",
             "The identical case as AN 5.18",
             "A return to the five powers"],
         "correct": 1,
         "expl": "The third of the unit's four logical combinations."},
        {"q": "What closes this four-discourse unit and the chapter as a whole?",
         "opts": [
             "AN 5.18 itself",
             "AN 5.20, describing both accomplishment and encouraging others together",
             "AN 5.19",
             "The unit has no closing discourse"],
         "correct": 1,
         "expl": "The fourth and final combination, ending the chapter on its most complete case."},
        {"q": "Is teaching or encouraging beyond one's own attainment presented as licensed or "
              "endorsed by this discourse?",
         "opts": [
             "Yes, explicitly encouraged as the better path",
             "No — the discourse names the case without endorsing it as an ideal to pursue",
             "The discourse forbids it outright with a warning of punishment",
             "The discourse does not address the question of endorsement at all"],
         "correct": 1,
         "expl": "A description of an incomplete case, not a recommendation."},
        {"q": "What is the setting of AN 5.18?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Kosambī",
             "The Bhagga country"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
        {"q": "How many of the four logical combinations in this unit have now been covered, "
              "counting AN 5.18?",
         "opts": ["One", "Two", "Three", "All four"],
         "correct": 1,
         "expl": "Own-welfare-only (AN 5.17) and others-welfare-only (AN 5.18); two remain."},
    ],
    marginalia=[
        ("The inversion", [
            "AN 5.17: accomplished,",
            "not encouraging &rarr; own only",
            "AN 5.18: not accomplished,",
            "encouraging &rarr; others only",
        ]),
        ("No ranking given", [
            "neither case called",
            "worse, or safer,",
            "than the other",
        ]),
        ("Same five items", [
            "sīla, samādhi, paññā,",
            "vimutti, vimuttiñāṇadassana",
        ]),
        ("Cross-references", [
            "AN 5.17 &middot; the mirror case",
            "AN 5.19 &middot; next: neither",
            "AN 5.20 &middot; then: both",
        ]),
    ],
    further=[
        '<a href="%s/an5.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; the previous '
        "discourse, whose case this page inverts.",
        '<a href="an-5.19.html">AN 5.19 &middot; The Welfare of Neither</a> &mdash; next, the '
        "unit's third case.",
        '<a href="an-5.20.html">AN 5.20 &middot; The Welfare of Both</a> &mdash; the unit&rsquo;s '
        "closing case.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.19 — Tatiyahitasutta
# --------------------------------------------------------------------------- #
page(
    19, "Tatiyahita", "The Welfare of Neither",
    vagga=VAGGA_2,
    meta_title="AN 5.19 — The Welfare of Neither | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the third Hitasutta — a "
        "mendicant neither personally accomplished in the five nor encouraging others in them, "
        "the third case in this chapter's closing four-part unit. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Both halves of AN 5.17's formula negated together"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.17"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the simplest of the four "
                       "cases, both conditions failing together"),
    ],
    why=(
        "The third case closes the logical square without ambiguity: a mendicant neither "
        "personally accomplished in ethics, immersion, wisdom, freedom, and the knowledge and "
        "vision of freedom, nor encouraging others toward them. Where AN 5.17 and 5.18 each "
        "offered something worth weighing &mdash; genuine private attainment against genuine "
        "outward generosity &mdash; this discourse offers nothing to weigh. It names the case where "
        "both fail at once."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant neither personally accomplished in the five, nor encouraging others in "
            "them, is practicing for neither their own welfare nor that of others."]),
        ("The simplest of the four cases", [
            "AN 5.17 and AN 5.18 each required a reader to weigh something genuine against "
            "something missing &mdash; real attainment against silence, or real generosity against "
            "lack of grounding. This discourse asks nothing to be weighed. Both halves of the "
            "formula are negated together, and the outcome follows without needing any "
            "qualification."]),
        ("Why the collection still gives this case its own discourse", [
            "A reader might expect this, the least interesting case logically, to be folded into "
            "one of the others or skipped. The chapter does neither. Keeping all four combinations "
            "as separate, equally weighted discourses is itself a small argument: the collection "
            "treats the logical square as worth completing in full, not only in its more "
            "psychologically interesting corners."]),
        ("What this case is not saying", [
            "The discourse does not say a mendicant in this position is beyond help, or condemns "
            "them further than the bare description. It states a fact about their present "
            "practice, in the same flat register used for the other three cases, and stops there. "
            "Whatever consequence might follow is left to other discourses in this series to "
            "address, not this one."]),
        ("One case remaining", [
            "AN 5.20 completes the square, and closes the chapter, with the fourth combination: "
            "personally accomplished <em>and</em> encouraging others. Reading all four discourses "
            "as a set makes plain that this final combination, not either of the two partial "
            "ones, is what the whole four-discourse unit has been building toward."]),
    ],
    terms=[
        ("neva&hellip;no",
         "&ldquo;neither&hellip;nor&rdquo; &mdash; the paired negation opening this discourse, "
         "distinguishing it from AN 5.17 and 5.18's single negations."),
        ("tatiya",
         "&ldquo;third&rdquo; &mdash; the ordinal in this discourse's title, marking its place in "
         "the four-part unit."),
        ("attahita",
         "&ldquo;one's own welfare&rdquo; &mdash; negated here alongside parahita, both failing "
         "together for the first time in the unit."),
        ("parahita",
         "&ldquo;others' welfare&rdquo; &mdash; likewise negated, completing the discourse's double "
         "failure."),
        ("aṅga",
         "&ldquo;factor, quality&rdquo; &mdash; the word this discourse uses for the five items, "
         "in place of dhamma, the term AN 5.17 used for the identical list."),
    ],
    text_intro=(
        "The discourse in full: neither personal accomplishment nor encouraging others. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Neither accomplished, nor encouraging others"),
        ("p", "&sect;1", "an5.19:1.1-1.8"),
    ],
    quiz=[
        {"q": "What case does AN 5.19 describe?",
         "opts": [
             "Accomplished, and encouraging others",
             "Neither personally accomplished nor encouraging others in the five",
             "Accomplished, but not encouraging others",
             "Not accomplished, but encouraging others"],
         "correct": 1,
         "expl": "Both halves of the formula negated together — the third of four combinations."},
        {"q": "How does the guide compare this case to AN 5.17 and 5.18's?",
         "opts": [
             "Equally complex, requiring the same weighing of genuine attainment against absence",
             "Simpler — nothing needs to be weighed, since both conditions fail together",
             "More complex, requiring additional interpretation",
             "Identical in every respect to AN 5.17"],
         "correct": 1,
         "expl": "AN 5.17 and 5.18 each weigh something genuine against something missing; this case has no such tension."},
        {"q": "Why does the guide say the collection still gives this least interesting case its "
              "own discourse?",
         "opts": [
             "By accident of transmission",
             "Keeping all four combinations as separate discourses treats the logical square as "
             "worth completing in full",
             "Because this case is considered the most important of the four",
             "Because the other three discourses were lost"],
         "correct": 1,
         "expl": "Completeness of the logical square, not only its more interesting corners."},
        {"q": "Does AN 5.19 condemn the mendicant it describes as beyond help?",
         "opts": [
             "Yes, explicitly",
             "No — it states a fact about present practice in the same flat register as the other "
             "cases, without further condemnation",
             "It predicts a specific bad rebirth",
             "It expels them from the monastic community"],
         "correct": 1,
         "expl": "A description, not a verdict beyond the bare fact stated."},
        {"q": "What word does AN 5.19 use for the five items, in place of AN 5.17's word?",
         "opts": [
             "Bala, power",
             "Aṅga, factor, in place of dhamma",
             "Indriya, faculty",
             "The same word, dhamma, unchanged"],
         "correct": 1,
         "expl": "A minor wording variation the guide notes without over-reading it."},
        {"q": "What does AN 5.20, the next and final discourse of the unit, complete?",
         "opts": [
             "A fifth, entirely new case",
             "The fourth combination — personally accomplished and encouraging others",
             "A repeat of AN 5.19",
             "The unit ends at AN 5.19 with no fourth case"],
         "correct": 1,
         "expl": "The combination the guide says the whole four-discourse unit has been building toward."},
        {"q": "How many of the unit's four logical combinations remain after AN 5.19?",
         "opts": ["None", "One", "Two", "Three"],
         "correct": 1,
         "expl": "Only the both-yes case, covered at AN 5.20, remains."},
        {"q": "What outcome does this discourse attach to its described case?",
         "opts": [
             "Practicing for both welfares",
             "Practicing for neither their own welfare nor that of others",
             "Practicing only for others' welfare",
             "No outcome is named"],
         "correct": 1,
         "expl": "The straightforward double negative outcome."},
        {"q": "Are the five items in this discourse newly defined, or inherited from AN 5.17?",
         "opts": [
             "Newly defined here in full",
             "Inherited unchanged from AN 5.17 — ethics, immersion, wisdom, freedom, and the "
             "knowledge and vision of freedom",
             "A different five items entirely",
             "Only three of the five are repeated"],
         "correct": 1,
         "expl": "The same list throughout this four-discourse unit."},
        {"q": "Where is AN 5.19 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Deer Park at Isipatana",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern so far."},
    ],
    marginalia=[
        ("The third case", [
            "accomplished: no",
            "encourages others: no",
            "&rarr; neither welfare",
        ]),
        ("Simplest of four", [
            "nothing to weigh &mdash;",
            "both conditions",
            "fail together",
        ]),
        ("Completing the square", [
            "AN 5.17: own only",
            "AN 5.18: others only",
            "AN 5.19: neither",
            "AN 5.20: both",
        ]),
        ("Cross-references", [
            "AN 5.17 &amp; 5.18 &middot; partial cases",
            "AN 5.19 &middot; this page, neither",
            "AN 5.20 &middot; next: both, closing",
        ]),
    ],
    further=[
        '<a href="%s/an5.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; the unit&rsquo;s '
        "opening case, accomplished but silent.",
        '<a href="an-5.18.html">AN 5.18 &middot; Welfare of Others (2nd)</a> &mdash; the second '
        "case, silent but generous.",
        '<a href="an-5.20.html">AN 5.20 &middot; The Welfare of Both</a> &mdash; next, closing '
        "both the unit and the chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.20 — Catutthahitasutta
# --------------------------------------------------------------------------- #
page(
    20, "Catutthahita", "The Welfare of Both",
    vagga=VAGGA_2,
    meta_title="AN 5.20 — The Welfare of Both | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the fourth Hitasutta — the "
        "chapter's closing discourse: a mendicant personally accomplished in the five and "
        "encouraging others in them too practices for both their own welfare and that of others. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Both halves of AN 5.17's formula affirmed together, closing the four-discourse "
                 "unit and the chapter"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.17"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the unit's resolving case, "
                       "closing the chapter on its most complete note"),
    ],
    why=(
        "The fourth combination is the one the whole unit has been building toward: a mendicant "
        "personally accomplished in ethics, immersion, wisdom, freedom, and the knowledge and "
        "vision of freedom, <em>and</em> encouraging others in the same five. This is the only one "
        "of the four cases the chapter does not qualify or leave partial. It closes both the "
        "four-discourse unit and the Balavagga itself, ending the chapter on the one combination "
        "that asks nothing to be weighed against anything else."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant personally accomplished in the five, and who encourages others in them "
            "too, is practicing for both their own welfare and that of others &mdash; the fourth "
            "and only unqualified case in the unit."]),
        ("Why this case closes the sequence, not opens it", [
            "The chapter could have led with this case and treated the other three as deficient "
            "variations. It does the opposite, working through the partial cases first and "
            "arriving at completeness last. Read in the order given, the four discourses build a "
            "case for what wholeness requires, rather than starting from an ideal and cataloguing "
            "how one falls short of it."]),
        ("What the whole unit has established", [
            "Across AN 5.17&ndash;20, the same five items &mdash; sīla, samādhi, paññā, vimutti, "
            "vimuttiñāṇadassana &mdash; and the same two variables, personal accomplishment and "
            "encouraging others, have generated all four possible combinations without exception. "
            "This discourse is not a new teaching so much as the completion of an argument spread "
            "across four discourses; reading it without the three before it would miss most of "
            "what it is doing."]),
        ("The chapter's own closing colophon", [
            "As with AN 5.10 at the close of the first chapter, the source text appends a "
            "colophon here &mdash; <em>Balavaggo dutiyo</em>, &lsquo;the second chapter, on "
            "powers&rsquo; &mdash; followed by the chapter&rsquo;s own uddāna verse, the same kind "
            "of untranslated Pāli mnemonic already explained in full at AN 5.10 and not "
            "re-explained here."]),
        ("What the next chapter takes up", [
            "The Fives continue with the Pañcaṅgikavagga, &lsquo;With Five Factors&rsquo;, the "
            "chapter that contains an-5.28.html, one of the two pages from this series&rsquo; "
            "earlier eighteen-page selection era. That existing page will be left as it is and "
            "linked into the index rather than rebuilt, exactly as flagged at the start of this "
            "chapter."]),
    ],
    terms=[
        ("catuttha",
         "&ldquo;fourth&rdquo; &mdash; the ordinal in this discourse's title, marking the last of "
         "the unit's four combinations."),
        ("attahitāya ca&hellip;parahitāya ca",
         "&ldquo;for one's own welfare and for others' welfare&rdquo; &mdash; both halves of the "
         "formula affirmed together, unique to this discourse in the unit."),
        ("Balavaggo dutiyo",
         "&ldquo;the second chapter, on powers&rdquo; &mdash; the colophon closing this vagga, "
         "matching Sekhabalavaggo paṭhamo's form from AN 5.10."),
        ("uddāna",
         "&ldquo;mnemonic verse&rdquo; &mdash; this chapter's own closing summary verse, explained "
         "in full at AN 5.10 and not repeated here."),
        ("dhamma",
         "&ldquo;quality&rdquo; &mdash; the word this discourse uses for the five items, matching "
         "AN 5.17 and 5.18's usage rather than AN 5.19's aṅga."),
    ],
    text_intro=(
        "The discourse in full: personal accomplishment and encouraging others, affirmed together. "
        "The closing colophon and Pāli mnemonic verse are part of the source but are not "
        "translated text, and are described rather than reproduced here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Accomplished, and encouraging others"),
        ("p", "&sect;1", "an5.20:1.1-1.7"),
    ],
    quiz=[
        {"q": "What case does AN 5.20 describe?",
         "opts": [
             "Neither accomplished nor encouraging others",
             "Personally accomplished in the five, and encouraging others in them too",
             "Accomplished, but not encouraging others",
             "Not accomplished, but encouraging others"],
         "correct": 1,
         "expl": "The fourth and only fully affirmed case in the unit."},
        {"q": "What outcome does this discourse attach to this case?",
         "opts": [
             "Practicing for neither welfare",
             "Practicing for both one's own welfare and that of others",
             "Practicing only for others' welfare",
             "No outcome is stated"],
         "correct": 1,
         "expl": "The only unqualified, fully positive outcome among the unit's four cases."},
        {"q": "Why does the guide say the chapter places this case last rather than first?",
         "opts": [
             "By accident, with no significance",
             "The chapter works through partial cases first and arrives at completeness last, "
             "building a case for what wholeness requires rather than starting from an ideal",
             "Because this case is considered the least important",
             "Because the text is corrupted and out of order"],
         "correct": 1,
         "expl": "A deliberate ordering, not starting from an ideal and cataloguing shortfalls."},
        {"q": "How many of the unit's four logical combinations does AN 5.17–20 cover in total?",
         "opts": ["Two", "Three", "All four, without exception", "Five"],
         "correct": 2,
         "expl": "Own-only, others-only, neither, and both."},
        {"q": "What colophon closes this chapter, matching AN 5.10's form?",
         "opts": [
             "No colophon is present",
             "Balavaggo dutiyo, 'the second chapter, on powers', followed by the chapter's own "
             "uddāna verse",
             "A colophon naming an entirely different chapter",
             "The colophon from AN 5.10 itself, repeated verbatim"],
         "correct": 1,
         "expl": "The same structural device, explained in full already and not repeated on this page."},
        {"q": "What chapter comes next, and what does the guide note about it?",
         "opts": [
             "The Pañcaṅgikavagga, which contains an-5.28.html, an existing page from the earlier "
             "eighteen-page selection era that will be left as is",
             "A chapter with no relation to any earlier material",
             "A return to the Sekhabalavagga",
             "The final chapter of the entire nipāta"],
         "correct": 0,
         "expl": "Consistent with the plan flagged at the very start of this project."},
        {"q": "Is AN 5.20 best read as a standalone teaching or as part of a larger argument?",
         "opts": [
             "Entirely standalone, with no connection to AN 5.17–19",
             "As the completion of an argument spread across all four discourses of the unit",
             "As a contradiction of AN 5.17–19",
             "As an unrelated appendix"],
         "correct": 1,
         "expl": "Reading it without the three before it would miss most of what it is doing."},
        {"q": "What word does AN 5.20 use for the five items?",
         "opts": [
             "Bala, power",
             "Dhamma, matching AN 5.17 and 5.18 rather than AN 5.19's aṅga",
             "Indriya, faculty",
             "A completely new term"],
         "correct": 1,
         "expl": "A minor wording detail the guide notes across the unit."},
        {"q": "Does this discourse introduce any new item beyond the five already named at AN "
              "5.17?",
         "opts": [
             "Yes, a sixth quality is added",
             "No — the same five: ethics, immersion, wisdom, freedom, and the knowledge and vision "
             "of freedom",
             "It replaces wisdom with a different term",
             "It drops two of the five items"],
         "correct": 1,
         "expl": "The identical list throughout the four-discourse unit."},
        {"q": "Where is AN 5.20 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Bamboo Grove",
             "Sāvatthī is restated in full here, unlike every other discourse in this chapter"],
         "correct": 1,
         "expl": "Consistent with the chapter's pattern from AN 5.11 through its close."},
    ],
    marginalia=[
        ("The fourth case", [
            "accomplished: yes",
            "encourages others: yes",
            "&rarr; both welfares",
        ]),
        ("Building to completeness", [
            "AN 5.17&ndash;19: partial",
            "AN 5.20: whole",
            "&mdash; placed last, deliberately",
        ]),
        ("The chapter closes", [
            "<span class=\"pali\">Balavaggo dutiyo</span>",
            "the second chapter, on powers",
        ]),
        ("Cross-references", [
            "AN 5.17&ndash;19 &middot; the partial cases",
            "AN 5.10 &middot; the uddāna, explained",
            "AN 5.21 &middot; next: Pañcaṅgikavagga",
        ]),
    ],
    further=[
        '<a href="%s/an5.20/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; the unit&rsquo;s '
        "opening case, and the discourse this page's completion answers.",
        '<a href="an-5.19.html">AN 5.19 &middot; The Welfare of Neither</a> &mdash; the previous '
        "discourse, the unit's third case.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; where this same '
        "closing-colophon structure was explained in full.",
    ],
)


VAGGA_3 = "<em>Pañcaṅgikavagga</em> &mdash; the third chapter of the Fives"


# --------------------------------------------------------------------------- #
# AN 5.21 — Paṭhamaagāravasutta
# --------------------------------------------------------------------------- #
page(
    21, "Paṭhamaagārava", "Disrespect (1st)",
    vagga=VAGGA_3,
    meta_title="AN 5.21 — Disrespect (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the third chapter's first "
        "Agāravasutta — a five-step ladder of prerequisites, from supplementary regulations up "
        "to right immersion, each rung impossible without the one before it for a disrespectful "
        "mendicant. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A five-rung ladder of prerequisites stated as impossible for a disrespectful "
                 "mendicant, then possible for a respectful one"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Graduated-training sequences building from minor observances up to "
                              "immersion are widespread across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; opens a new chapter by reusing "
                       "a title, and a concept, from the first"),
    ],
    why=(
        "This chapter opens by reusing both the title and the disrespect/respect framing already "
        "used at <a href=\"an-5.9.html\">AN 5.9</a> and <a href=\"an-5.10.html\">AN 5.10</a> in "
        "the first chapter &mdash; but applies it to something new: not the five powers, but a "
        "five-step causal ladder. Without fulfilling the supplementary regulations, the practice "
        "of a trainee is impossible; without that, ethics; without that, right view; without that, "
        "right immersion. Each rung depends strictly on the one below it, for better or worse."),
    guide=[
        ("The teaching in one sentence", [
            "A disrespectful mendicant with an incompatible lifestyle cannot fulfill supplementary "
            "regulations, and so cannot fulfill a trainee's practice, ethics, right view, or right "
            "immersion in turn; a respectful mendicant with a compatible lifestyle can fulfill all "
            "five in strict sequence."]),
        ("A ladder, not a list", [
            "Every five-item set met so far in this nipāta has been a set: five powers, five "
            "qualities, five items to be seen in different fours. This discourse is different in "
            "kind. Each rung is stated as a strict precondition for the next &mdash; "
            "<em>ābhisamācārika</em>, the supplementary regulations governing everyday monastic "
            "conduct, then the trainee's practice, then ethics, then right view, then right "
            "immersion &mdash; and the text is explicit that skipping a rung is not merely "
            "unlikely but <em>netaṁ ṭhānaṁ vijjati</em>, not a possible situation at all."]),
        ("Why the smallest matters begin the chain", [
            "It is worth noticing what sits at the bottom of the ladder: not ethics, and certainly "
            "not immersion, but the supplementary regulations &mdash; the minor, procedural rules "
            "of communal monastic life. The discourse's claim is structural: grand attainments like "
            "right view and right immersion are not available to someone who cannot manage the "
            "small, everyday cooperative discipline of living respectfully among spiritual "
            "companions."]),
        ("Reusing AN 5.9 and 5.10's framing, for new material", [
            "The disrespect/respect pairing, and the paired terms <em>agārava appatisso</em> "
            "against <em>sagārava sappatisso</em>, are identical to their earlier use in the first "
            "chapter's closing discourses. This discourse does not redefine either pair; it applies "
            "an already-established distinction to an entirely new five-step structure, showing "
            "that the disrespect/respect framing was never tied to the sekhabala specifically."]),
        ("What follows", [
            "AN 5.22, immediately next, restates this exact ladder with its final three rungs "
            "compressed into the more familiar threefold training &mdash; the whole spectrum of "
            "ethics, immersion, and wisdom &mdash; rather than the five discrete steps given here."]),
    ],
    terms=[
        ("ābhisamācārika",
         "&ldquo;supplementary regulation&rdquo; &mdash; the everyday, procedural conduct rules "
         "this discourse places at the base of its five-rung ladder."),
        ("sekhaṁ dhammaṁ",
         "&ldquo;the trainee's practice&rdquo; &mdash; the second rung, distinct from but "
         "dependent on the first."),
        ("sammādiṭṭhi",
         "&ldquo;right view&rdquo; &mdash; the fourth rung, itself dependent on ethics being "
         "fulfilled first."),
        ("netaṁ ṭhānaṁ vijjati",
         "&ldquo;this is not a possible situation&rdquo; &mdash; the strong formula marking each "
         "dependency as strict, not merely typical."),
        ("asabhāgavuttika",
         "&ldquo;of incompatible lifestyle&rdquo; &mdash; paired with disrespect and irreverence to "
         "describe the mendicant who cannot climb the ladder."),
    ],
    text_intro=(
        "The discourse in full: the five-rung ladder, impossible for a disrespectful mendicant, "
        "possible for a respectful one. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Impossible, for the disrespectful"),
        ("p", "&sect;1", "an5.21:1.1-1.5"),
        ("h3", "Possible, for the respectful"),
        ("p", "&sect;2", "an5.21:2.1-2.5"),
    ],
    quiz=[
        {"q": "What kind of structure does AN 5.21 present, compared to the five-item sets seen "
              "earlier in this nipāta?",
         "opts": [
             "A simple list with no internal order",
             "A five-rung ladder of strict prerequisites, each impossible without the one before it",
             "Five unrelated, independent qualities",
             "A repetition of the sekhabala"],
         "correct": 1,
         "expl": "Unlike a set, each rung here strictly depends on the one below it."},
        {"q": "What sits at the bottom of the ladder?",
         "opts": [
             "Right immersion",
             "The supplementary regulations — minor, procedural rules of communal monastic conduct",
             "Right view",
             "The five powers"],
         "correct": 1,
         "expl": "The smallest, most everyday discipline is the foundation everything else depends on."},
        {"q": "What does 'netaṁ ṭhānaṁ vijjati' mean, and how strong is its claim?",
         "opts": [
             "'This rarely happens' — a mild statistical claim",
             "'This is not a possible situation' — a strict impossibility, not merely an unlikelihood",
             "'This is forbidden by rule' — a disciplinary statement",
             "'This has not yet happened' — a historical claim"],
         "correct": 1,
         "expl": "Each dependency in the ladder is stated as strict impossibility, not tendency."},
        {"q": "Where was the disrespect/respect framing (agārava/sagārava) already used in this "
              "series?",
         "opts": [
             "Nowhere before this page",
             "AN 5.9 and AN 5.10, in the first chapter, applied there to the five powers",
             "Only in AN 4.163",
             "Only in the Threes"],
         "correct": 1,
         "expl": "The same pair of terms, now applied to an entirely different five-step structure."},
        {"q": "Does this discourse redefine what disrespect or respect mean?",
         "opts": [
             "Yes, with a new definition",
             "No — it applies the already-established distinction to new material",
             "It reverses their meaning from AN 5.9",
             "It drops the terms entirely"],
         "correct": 1,
         "expl": "Showing the framing was never tied specifically to the sekhabala."},
        {"q": "What are the five rungs of the ladder, in order?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Supplementary regulations, the trainee's practice, ethics, right view, right immersion",
             "Ethics, immersion, wisdom, freedom, knowledge and vision of freedom",
             "The four noble truths plus one"],
         "correct": 1,
         "expl": "A five-step causal chain, not a five-item set."},
        {"q": "What does AN 5.22, the next discourse, do with this same ladder?",
         "opts": [
             "Abandons it entirely for a new topic",
             "Restates it with the final three rungs compressed into the threefold training of "
             "ethics, immersion, and wisdom",
             "Reverses the order of the rungs",
             "Repeats it identically with no change"],
         "correct": 1,
         "expl": "A variant using the more familiar sīla-samādhi-paññā compression."},
        {"q": "What structural claim does the guide draw from the ladder's ordering?",
         "opts": [
             "That grand attainments are available regardless of everyday conduct",
             "That right view and right immersion are not available to someone who cannot manage "
             "small, everyday cooperative discipline first",
             "That ethics is unnecessary once right view is attained",
             "That the ladder has no real ordering at all"],
         "correct": 1,
         "expl": "The smallest matters, placed first, are structurally load-bearing for the guide's reading."},
        {"q": "Does the discourse offer a simile to illustrate the ladder?",
         "opts": [
             "Yes, an extended parable",
             "No — the ladder is stated directly, with no narrative illustration",
             "Yes, the bungalow-peak simile is reused",
             "Yes, the nursemaid parable is reused"],
         "correct": 1,
         "expl": "A direct statement, consistent with this discourse's terse form."},
        {"q": "Where is AN 5.21 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Icchānaṅgala",
             "The Bhagga country"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("The five rungs", [
            "1. supplementary regs",
            "2. trainee's practice",
            "3. ethics",
            "4. right view",
            "5. right immersion",
        ]),
        ("Strict, not typical", [
            "<span class=\"pali\">netaṁ ṭhānaṁ vijjati</span>",
            "&mdash; not a possible situation",
        ]),
        ("Reused framing", [
            "<span class=\"pali\">agārava/sagārava</span>",
            "from AN 5.9&ndash;10,",
            "now on a new ladder",
        ]),
        ("Cross-references", [
            "AN 5.9&ndash;10 &middot; the framing's origin",
            "AN 5.22 &middot; next: compressed variant",
            "AN 5.17&ndash;20 &middot; a related five-fold list",
        ]),
    ],
    further=[
        '<a href="%s/an5.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.9.html">AN 5.9 &middot; Disrespect (1st)</a> &mdash; where this '
        "discourse's title and disrespect framing originate.",
        '<a href="an-5.22.html">AN 5.22 &middot; Disrespect (2nd)</a> &mdash; next, the same ladder '
        "with its top compressed to the threefold training.",
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; the ethics-immersion-wisdom-'
        "freedom list this ladder's upper rungs echo.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.22 — Dutiyaagāravasutta
# --------------------------------------------------------------------------- #
page(
    22, "Dutiyaagārava", "Disrespect (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 5.22 — Disrespect (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Agāravasutta of "
        "this chapter — AN 5.21's ladder restated, with its top three rungs compressed into the "
        "whole spectrum of ethics, immersion, and wisdom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.21's ladder restated with the final three rungs replaced by the threefold "
                 "training in full"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.21"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a compressed variant, best "
                       "read directly against its predecessor"),
    ],
    why=(
        "AN 5.21 named five discrete rungs. This discourse keeps the first two &mdash; the "
        "supplementary regulations, then the trainee's practice &mdash; but collapses the last "
        "three into the whole spectrum (<em>khandha</em>) of ethics, then of immersion, then of "
        "wisdom: the threefold training, <em>sīla, samādhi, paññā</em>, in its most familiar form. "
        "The same dependency claim is made, in a shape many readers will recognize more readily "
        "than AN 5.21's five discrete steps."),
    guide=[
        ("The teaching in one sentence", [
            "Without fulfilling the supplementary regulations, the trainee's practice is "
            "impossible; without that, the whole spectrum of ethics; without that, the whole "
            "spectrum of immersion; without that, the whole spectrum of wisdom &mdash; and the "
            "reverse holds for a respectful mendicant."]),
        ("What changed from AN 5.21", [
            "AN 5.21 kept right view and right immersion as two separate rungs. This discourse "
            "instead names <em>sīlakkhandha, samādhikkhandha, paññākkhandha</em> &mdash; not right "
            "view specifically, but ethics, immersion, and wisdom as entire spectrums or "
            "aggregates. The base of the ladder is identical; only its upper reach is reshaped "
            "into the more familiar threefold training already used throughout this series."]),
        ("Why &lsquo;the entire spectrum&rsquo;, and not a single item", [
            "<em>Khandha</em> here means a whole mass or aggregate, not one discrete factor among "
            "several. The claim is broader than AN 5.21's: not one particular right view, but the "
            "entirety of what counts as ethics; not one particular immersion, but the entirety of "
            "what counts as immersion. This is a stronger, more encompassing dependency claim than "
            "the previous discourse's, even though it uses fewer named steps to make it."]),
        ("The threefold training, met again", [
            "Ethics, immersion, wisdom is the same core sequence already central to "
            "<a href=\"an-4.1.html\">AN 4.1</a>'s opening list in the previous nipāta, and to "
            "<a href=\"an-5.17.html\">AN 5.17&ndash;20</a>'s five-item set earlier in this one. "
            "This discourse adds no new content to that sequence; it only restates, once again, "
            "that the threefold training builds in strict order, each stage depending on the one "
            "before it."]),
        ("Two discourses, one point made twice", [
            "Read together, AN 5.21 and 5.22 make the identical structural claim &mdash; strict, "
            "cumulative dependency &mdash; using two different levels of granularity for the "
            "upper rungs. A reader who has followed both should now be able to state the underlying "
            "claim without reference to either discourse's specific wording: nothing higher is "
            "reached without what is lower being genuinely in place first."]),
    ],
    terms=[
        ("sīlakkhandha",
         "&ldquo;the whole spectrum of ethics&rdquo; &mdash; khandha, aggregate or mass, marking "
         "this as broader than any single ethical rule."),
        ("samādhikkhandha",
         "&ldquo;the whole spectrum of immersion&rdquo; &mdash; the second compressed rung, "
         "replacing AN 5.21's separate right view and right immersion."),
        ("paññākkhandha",
         "&ldquo;the whole spectrum of wisdom&rdquo; &mdash; the top of this discourse's ladder, "
         "completing the threefold training."),
        ("khandha",
         "&ldquo;aggregate, mass, spectrum&rdquo; &mdash; the word marking each of the three upper "
         "terms as an entirety rather than one factor among several."),
        ("sīla samādhi paññā",
         "&ldquo;ethics, immersion, wisdom&rdquo; &mdash; the threefold training, already central "
         "to AN 4.1 and AN 5.17&ndash;20, restated here in ladder form."),
    ],
    text_intro=(
        "The discourse in full: the same ladder as AN 5.21, with its top compressed to the "
        "threefold training. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Impossible, for the disrespectful"),
        ("p", "&sect;1", "an5.22:1.1-1.5"),
        ("h3", "Possible, for the respectful"),
        ("p", "&sect;2", "an5.22:2.1-2.5"),
    ],
    quiz=[
        {"q": "What does AN 5.22 change from AN 5.21's ladder?",
         "opts": [
             "Nothing at all",
             "The final three rungs are compressed into the threefold training — ethics, "
             "immersion, and wisdom in their entirety",
             "The base of the ladder changes; the top stays the same",
             "The disrespect framing is dropped"],
         "correct": 1,
         "expl": "The base — supplementary regulations, then the trainee's practice — is unchanged."},
        {"q": "What does 'khandha' mean in sīlakkhandha, samādhikkhandha, and paññākkhandha?",
         "opts": [
             "A single specific rule or factor",
             "A whole spectrum, mass, or aggregate — broader than one discrete item",
             "A monastic robe",
             "A meditation posture"],
         "correct": 1,
         "expl": "Marking each term as an entirety, not one factor among several."},
        {"q": "How does the guide compare the strength of this discourse's claim to AN 5.21's?",
         "opts": [
             "Weaker, since fewer steps are named",
             "Broader and more encompassing, despite using fewer named steps, since it claims the "
             "entirety of ethics, immersion, and wisdom rather than one factor of each",
             "Identical in every respect",
             "The two discourses make contradictory claims"],
         "correct": 1,
         "expl": "Fewer steps, but each covering more ground."},
        {"q": "What sequence does this discourse's upper ladder match, already central elsewhere "
              "in this series?",
         "opts": [
             "The five powers",
             "The threefold training — ethics, immersion, wisdom — from AN 4.1 and AN 5.17–20",
             "The four noble truths",
             "The sekhabala"],
         "correct": 1,
         "expl": "Ethics, immersion, wisdom recurs as a core sequence across multiple discourses in this series."},
        {"q": "Is the base of the ladder — supplementary regulations, then the trainee's practice "
              "— changed in this discourse?",
         "opts": [
             "Yes, entirely rewritten",
             "No — identical to AN 5.21",
             "Only the first rung changes",
             "Both base rungs are dropped"],
         "correct": 1,
         "expl": "Only the upper reach of the ladder is reshaped."},
        {"q": "What single underlying claim do AN 5.21 and 5.22 together make, according to the "
              "guide?",
         "opts": [
             "That the ladder's order can be rearranged freely",
             "Strict, cumulative dependency — nothing higher is reached without what is lower "
             "genuinely being in place first",
             "That ethics is optional for advanced practitioners",
             "That the two discourses contradict each other"],
         "correct": 1,
         "expl": "The same structural point, made at two different levels of granularity."},
        {"q": "Does this discourse offer any narrative illustration or simile?",
         "opts": [
             "Yes, an extended parable",
             "No — stated directly, matching AN 5.21's terse form",
             "Yes, the tree-and-branches simile from AN 5.24 is used here first",
             "Yes, the bungalow-peak simile"],
         "correct": 1,
         "expl": "Consistent with the pair's shared terse style."},
        {"q": "What is the disrespect/respect framing's origin in this series?",
         "opts": [
             "This discourse invents it",
             "AN 5.9 and AN 5.10, reused already at AN 5.21",
             "AN 4.163",
             "It has no clear origin"],
         "correct": 1,
         "expl": "Carried forward from AN 5.21 without modification."},
        {"q": "What comes next in the chapter?",
         "opts": [
             "A return to the sekhabala",
             "AN 5.23, on five corruptions of gold and of the mind",
             "The end of the chapter",
             "A repeat of AN 5.22"],
         "correct": 1,
         "expl": "A new topic and image, distinct from the ladder discourses."},
        {"q": "Where is AN 5.22 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Vesālī",
             "The Squirrels' Sanctuary"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("Same base, new top", [
            "1&ndash;2. unchanged",
            "3. sīlakkhandha",
            "4. samādhikkhandha",
            "5. paññākkhandha",
        ]),
        ("Entirety, not one item", [
            "<span class=\"pali\">khandha</span>",
            "&mdash; whole spectrum,",
            "not a single factor",
        ]),
        ("The threefold training", [
            "sīla &middot; samādhi &middot; paññā",
            "&mdash; met already at AN 4.1,",
            "AN 5.17&ndash;20",
        ]),
        ("Cross-references", [
            "AN 5.21 &middot; the fuller ladder",
            "AN 4.1 &middot; the training's origin here",
            "AN 5.23 &middot; next: corruptions",
        ]),
    ],
    further=[
        '<a href="%s/an5.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.21.html">AN 5.21 &middot; Disrespect (1st)</a> &mdash; the fuller, five-rung '
        "version of this same ladder.",
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; where the threefold training '
        "this discourse's upper rungs match first opened the Fours.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; next, a new topic and its '
        "own image.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.23 — Upakkilesasutta
# --------------------------------------------------------------------------- #
page(
    23, "Upakkilesa", "Corruptions",
    vagga=VAGGA_3,
    meta_title="AN 5.23 — Corruptions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Upakkilesasutta — the "
        "five corruptions of gold matched to the five corruptions of the mind, the classic "
        "hindrances, and the extended list of what becomes possible once the mind is purified of "
        "them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A metalworking simile mapped directly onto the mind, followed by an extended "
                 "list of what a purified mind is capable of"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "The gold-refining simile for mental purification and the six "
                              "superhuman abilities are widely attested across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the chapter's longest "
                       "discourse so far, naming the five hindrances by their classic list for "
                       "the first time in the Fives"),
    ],
    why=(
        "This discourse names, for the first time in the Fives, the five <em>nīvaraṇa</em>: "
        "sensual desire, ill will, dullness and drowsiness, restlessness and remorse, and doubt "
        "&mdash; the classic hindrances that will eventually give an entire chapter of this "
        "nipāta its name. Here they arrive under a different label, <em>upakkilesa</em>, "
        "corruptions, mapped directly onto five corruptions of native gold: iron, copper, tin, "
        "lead, and silver, each of which leaves gold brittle and unworkable until removed."),
    guide=[
        ("The teaching in one sentence", [
            "Just as gold corrupted by iron, copper, tin, lead, or silver is brittle and "
            "unworkable, a mind corrupted by sensual desire, ill will, dullness and drowsiness, "
            "restlessness and remorse, or doubt is not rightly immersed for the ending of "
            "defilements; free of these five, the mind becomes pliable, workable, and capable of "
            "realizing whatever it turns toward."]),
        ("The five hindrances, under a different name", [
            "<em>Kāmacchando, byāpādo, thinamiddhaṁ, uddhaccakukkuccaṁ, vicikicchā</em> is the "
            "identical five-item list the tradition elsewhere calls the <em>nīvaraṇa</em>, "
            "hindrances &mdash; a list important enough to eventually give its own chapter, later "
            "in this nipāta, its name. Here they are called <em>upakkilesa</em>, corruptions, and "
            "framed through a craftsman's image rather than the more common metaphor of "
            "obstruction. Both labels point at the same five states; a reader should not expect "
            "the vocabulary to stay fixed across the whole collection."]),
        ("The gold simile, read closely", [
            "The simile is precise about what corruption costs: gold that is corrupted is "
            "<em>na mudu</em>, not pliable; <em>na kammaniya</em>, not workable; "
            "<em>na pabhassara</em>, not radiant; and <em>pabhaṅgu</em>, brittle. Four distinct "
            "losses, not one vague deficiency. Purified, the same four qualities return in "
            "reverse, and only then can a goldsmith make whatever ornament they choose &mdash; a "
            "ring, earrings, a necklace, a garland. The simile&rsquo;s point is not that impure "
            "gold is worthless but that it cannot yet be shaped into anything in particular."]),
        ("What purification makes possible", [
            "The discourse then lists, at real length, what becomes available to a mind freed of "
            "the five corruptions: the various psychic powers, clairaudience, reading others' "
            "minds, recollecting past lives in detail, clairvoyance into others' rebirths "
            "according to their deeds, and finally the ending of defilements. This is an unusually "
            "long list for a discourse this size, and it is close to word-for-word what appears "
            "already at the legacy page <a href=\"an-5.28.html\">AN 5.28</a>, this vagga's own "
            "namesake discourse. The two texts are not identical, but they draw on the same "
            "standard formula for what a purified, immersed mind is said to be capable of."]),
        ("What this discourse does not claim", [
            "Notably, the discourse does not present the psychic powers or the recollection of "
            "past lives as ends in themselves, or even discuss them individually beyond naming "
            "each in the standard formula. Every item in the list is introduced with the same "
            "conditional, <em>if you wish</em>, and closed with the same refrain, "
            "<em>you're capable of realizing it, since each and every one is within range</em>. "
            "The claim is about capability opened up by purification, not about any one ability "
            "being recommended for its own sake."]),
    ],
    terms=[
        ("upakkilesa",
         "&ldquo;corruption&rdquo; &mdash; this discourse's word for what elsewhere in the canon "
         "is called nīvaraṇa, hindrance; the same five states under a different label."),
        ("jātarūpa",
         "&ldquo;native gold&rdquo; &mdash; unrefined gold as it occurs naturally, the material "
         "the simile's corruptions afflict."),
        ("thinamiddha",
         "&ldquo;dullness and drowsiness&rdquo; &mdash; the third of the five mental corruptions, "
         "paired as a single compound term throughout the canon."),
        ("uddhaccakukkucca",
         "&ldquo;restlessness and remorse&rdquo; &mdash; the fourth, likewise a fixed compound "
         "pairing two related mental states."),
        ("abhiññā",
         "&ldquo;direct knowledge, superhuman ability&rdquo; &mdash; the general term for the "
         "capacities this discourse lists as available once the mind is purified."),
    ],
    text_intro=(
        "The discourse in full: the gold simile, its application to the mind's five corruptions, "
        "and the extended list of what a purified mind can realize. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Corruptions of gold"),
        ("p", "&sect;1", "an5.23:1.1-1.6"),
        ("h3", "Corruptions of the mind"),
        ("p", "&sect;2", "an5.23:2.1-2.4"),
        ("p", "&sect;3", "an5.23:2.5-2.6"),
        ("h3", "Psychic power"),
        ("p", "&sect;4", "an5.23:3.1-3.2"),
        ("h3", "Clairaudience"),
        ("p", "&sect;5", "an5.23:4.1-4.2"),
        ("h3", "Reading minds"),
        ("p", "&sect;6", "an5.23:5.1-5.18"),
        ("h3", "Past lives"),
        ("p", "&sect;7", "an5.23:6.1-6.2"),
        ("h3", "Clairvoyance"),
        ("p", "&sect;8", "an5.23:7.1-7.2"),
        ("h3", "The ending of defilements"),
        ("p", "&sect;9", "an5.23:8.1-8.2"),
    ],
    quiz=[
        {"q": "What five items does the mind-corruption half of this discourse name?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Sensual desire, ill will, dullness and drowsiness, restlessness and remorse, and "
             "doubt — the classic five hindrances",
             "Iron, copper, tin, lead, and silver",
             "Greed, hate, delusion, conceit, and views"],
         "correct": 1,
         "expl": "The nīvaraṇa, here called upakkilesa, corruptions, for the first time by name in the Fives."},
        {"q": "What word does this discourse use for the hindrances, instead of 'nīvaraṇa'?",
         "opts": [
             "Bala, power",
             "Upakkilesa, corruption",
             "Aṅga, factor",
             "Khandha, spectrum"],
         "correct": 1,
         "expl": "The same five states, framed through a metalworking image rather than the more common obstruction metaphor."},
        {"q": "What four qualities does corrupted gold lack, according to the simile?",
         "opts": [
             "Weight, color, shine, and hardness",
             "Pliability, workability, radiance — and it is brittle instead",
             "Value, purity, rarity, and durability",
             "None are specified; the simile is vague"],
         "correct": 1,
         "expl": "Four distinct losses named precisely, not one vague deficiency."},
        {"q": "What does the goldsmith do once the gold is purified?",
         "opts": [
             "Nothing changes; purity has no practical effect",
             "Successfully creates any ornament they want — a ring, earrings, a necklace, a golden "
             "garland",
             "Melts the gold down for storage only",
             "Sells the gold immediately"],
         "correct": 1,
         "expl": "Purity opens up the capacity to be shaped into anything in particular."},
        {"q": "What does the guide note about the extended abhiññā list closing this discourse?",
         "opts": [
             "It is entirely unique to this discourse, appearing nowhere else in this series",
             "It closely matches, nearly word for word, material already seen at the legacy page "
             "AN 5.28",
             "It contradicts material at AN 5.28",
             "It is a shorter, abbreviated version with fewer items than AN 5.28's"],
         "correct": 1,
         "expl": "The same standard formula drawn on by this vagga's own namesake discourse."},
        {"q": "How is each ability in the extended list introduced and closed?",
         "opts": [
             "As a command that must be obeyed",
             "With the same conditional 'if you wish' and the same refrain about being within range",
             "As a warning against pursuing it",
             "With no repeated formula at all"],
         "correct": 1,
         "expl": "A consistent pattern across every item in the list."},
        {"q": "According to the guide, does this discourse recommend the psychic powers as ends in "
              "themselves?",
         "opts": [
             "Yes, explicitly urging their pursuit",
             "No — the claim is about capability opened up by purification, not about recommending "
             "any one ability for its own sake",
             "The discourse forbids them outright",
             "The discourse takes no position either way, offering no framing at all"],
         "correct": 1,
         "expl": "Introduced conditionally, as what becomes available, not what must be sought."},
        {"q": "What later chapter of this nipāta does the guide say the hindrances will eventually "
              "give its name to?",
         "opts": [
             "No later chapter is connected to this material",
             "A chapter later in the Fives, since this exact five-item list is important enough to "
             "be named for",
             "The chapter this discourse is already in",
             "A chapter in a different nipāta entirely"],
         "correct": 1,
         "expl": "A forward-pointing note the guide will confirm when that chapter arrives."},
        {"q": "How many of the six standard superhuman abilities does the extended list name?",
         "opts": [
             "Only one",
             "All six — psychic power, clairaudience, reading minds, past-life recall, "
             "clairvoyance, and the ending of defilements",
             "Only three",
             "None; the list stops before naming any specific ability"],
         "correct": 1,
         "expl": "The complete standard set, given at real length for a discourse this size."},
        {"q": "Where is AN 5.23 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Bhagga country",
             "Icchānaṅgala"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("Five corruptions, of gold", [
            "iron &middot; copper &middot; tin",
            "lead &middot; silver",
        ]),
        ("Five corruptions, of mind", [
            "sensual desire &middot; ill will",
            "dullness/drowsiness",
            "restlessness/remorse &middot; doubt",
        ]),
        ("Four losses, from corruption", [
            "not pliable, not workable,",
            "not radiant, brittle",
        ]),
        ("Cross-references", [
            "AN 5.28 &middot; the same abhiññā list",
            "AN 6.16 &middot; the nipāta ahead, waiting",
            "AN 5.24 &middot; next: a tree, lacking",
        ]),
    ],
    further=[
        '<a href="%s/an5.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.28.html">AN 5.28 &middot; With Five Factors</a> &mdash; this chapter&rsquo;s '
        "own namesake discourse, sharing nearly identical closing material with this page.",
        '<a href="an-5.24.html">AN 5.24 &middot; Unethical</a> &mdash; next, a different image for '
        "a related causal chain.",
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; the ending of defilements '
        "this discourse&rsquo;s final ability names, already the closing claim of AN 4.1.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.24 — Dussīlasutta
# --------------------------------------------------------------------------- #
page(
    24, "Dussīla", "Unethical",
    vagga=VAGGA_3,
    meta_title="AN 5.24 — Unethical | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dussīlasutta — a "
        "five-step causal chain from ethics through immersion, true knowledge, disillusionment, "
        "and freedom's knowledge and vision, illustrated by a tree that fails to grow when its "
        "branches and foliage are missing. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A five-step causal chain stated abstractly, then illustrated by a single tree "
                 "simile, then restated for its positive mirror"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Causal chains linking ethics through immersion to liberation "
                              "knowledge are a recurring structural device across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a five-step chain that "
                       "quietly expands the five-item set from AN 5.17&ndash;20"),
    ],
    why=(
        "This discourse takes the five-item set from <a href=\"an-5.17.html\">AN 5.17&ndash;20</a> "
        "&mdash; ethics, immersion, wisdom, freedom, the knowledge and vision of freedom &mdash; "
        "and expands the space between its middle terms into a fuller causal chain: ethics, right "
        "immersion, true knowledge and vision, disillusionment and dispassion, and the knowledge "
        "and vision of freedom. Each step is said to destroy or fulfill <em>a vital condition</em> "
        "for the next, illustrated by a single, exact image: a tree with or without its branches "
        "and foliage."),
    guide=[
        ("The teaching in one sentence", [
            "An unethical person has destroyed a vital condition for right immersion, which "
            "destroys a vital condition for true knowledge and vision, which destroys a vital "
            "condition for disillusionment and dispassion, which destroys a vital condition for "
            "the knowledge and vision of freedom; an ethical person fulfills each condition in "
            "turn."]),
        ("A chain, not a checklist", [
            "The word <em>upanisā</em>, vital condition or proximate cause, marks this as a "
            "causal claim rather than a simple list. Each item does not merely accompany the "
            "next; it is named as what the next depends on for its very possibility, which is why "
            "the discourse can say ethics alone <em>destroys</em> a condition for immersion before "
            "immersion has even been discussed on its own terms."]),
        ("The tree, and what it withholds", [
            "The simile names four specific parts of a tree that fail to grow to fullness when "
            "branches and foliage are missing: shoots, bark, softwood, and heartwood. This is more "
            "particular than a vague image of stunted growth; each named part corresponds, loosely "
            "but suggestively, to something built up in layers, outer to inner, exactly as this "
            "discourse's five-step chain builds from the outermost practice, ethics, toward the "
            "innermost realization, the knowledge and vision of freedom."]),
        ("Filling in AN 5.17&ndash;20's gap", [
            "AN 5.17 through 5.20 moved directly from immersion to freedom, by way of wisdom, with "
            "no stated mechanism connecting them. This discourse supplies two additional named "
            "steps in between &mdash; true knowledge and vision, then disillusionment and "
            "dispassion &mdash; showing that the shorter list was a compression of a longer, more "
            "granular process rather than a complete account on its own."]),
        ("What follows", [
            "AN 5.25, next, approaches the same territory from a different angle: not a causal "
            "chain but a claim about what supports right view specifically, naming five different "
            "supports rather than five sequential stages."]),
    ],
    terms=[
        ("upanisā",
         "&ldquo;vital condition, proximate cause&rdquo; &mdash; the word marking each step as "
         "what the next genuinely depends on, not merely accompanies."),
        ("yathābhūtañāṇadassana",
         "&ldquo;true knowledge and vision&rdquo; &mdash; the chain's third step, added here "
         "between immersion and disillusionment."),
        ("nibbidāvirāga",
         "&ldquo;disillusionment and dispassion&rdquo; &mdash; the fourth step, the turning away "
         "that arises from seeing clearly."),
        ("sākhāpalāsa",
         "&ldquo;branches and foliage&rdquo; &mdash; the tree's outer growth, whose absence in "
         "the simile prevents the inner parts from developing."),
        ("sāra",
         "&ldquo;heartwood&rdquo; &mdash; the innermost part of the tree, corresponding to the "
         "chain's own innermost term, the knowledge and vision of freedom."),
    ],
    text_intro=(
        "The discourse in full: the causal chain stated for lacking ethics, illustrated by the "
        "tree simile, then restated for having it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The chain, broken"),
        ("p", "&sect;1", "an5.24:1.1-1.4"),
        ("h3", "The tree, without branches or foliage"),
        ("p", "&sect;2", "an5.24:1.5-1.6"),
        ("p", "&sect;3", "an5.24:1.7-1.10"),
        ("h3", "The chain, fulfilled"),
        ("p", "&sect;4", "an5.24:2.1-2.4"),
        ("h3", "The tree, complete"),
        ("p", "&sect;5", "an5.24:2.5"),
        ("p", "&sect;6", "an5.24:2.6-2.9"),
    ],
    quiz=[
        {"q": "What five steps make up this discourse's causal chain?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Ethics, right immersion, true knowledge and vision, disillusionment and dispassion, "
             "and the knowledge and vision of freedom",
             "The five hindrances",
             "The five powers"],
         "correct": 1,
         "expl": "Each step named as a vital condition (upanisā) for the next."},
        {"q": "What does 'upanisā' mark each step as, relative to the next?",
         "opts": [
             "A loose association with no real dependency",
             "A vital condition or proximate cause the next step genuinely depends on",
             "An optional alternative",
             "A contradiction to be resolved"],
         "correct": 1,
         "expl": "A causal claim, not a simple accompanying list."},
        {"q": "What four parts of a tree does the simile name as failing to grow without branches "
              "and foliage?",
         "opts": [
             "Roots, trunk, leaves, and flowers",
             "Shoots, bark, softwood, and heartwood",
             "Fruit, seeds, sap, and bark",
             "Only the trunk is named"],
         "correct": 1,
         "expl": "Specific named parts, not a vague image of general stunting."},
        {"q": "How does the guide connect this discourse to AN 5.17–20?",
         "opts": [
             "It sees no connection between them",
             "This discourse fills in AN 5.17–20's gap, adding two named steps — true knowledge "
             "and vision, then disillusionment and dispassion — between immersion and freedom",
             "This discourse contradicts AN 5.17–20 entirely",
             "AN 5.17–20 already contained this exact chain in full"],
         "correct": 1,
         "expl": "The shorter list is read as a compression of this longer, more granular process."},
        {"q": "What two steps does this discourse add beyond ethics, immersion, and freedom's "
              "knowledge and vision?",
         "opts": [
             "Faith and energy",
             "True knowledge and vision, and disillusionment and dispassion",
             "Conscience and prudence",
             "No new steps are added"],
         "correct": 1,
         "expl": "Yathābhūtañāṇadassana and nibbidāvirāga, inserted between the more familiar terms."},
        {"q": "What happens to an ethical person's chain, according to the second half of the "
              "discourse?",
         "opts": [
             "The same destruction as the unethical person's",
             "Each condition is fulfilled in turn, mirroring the first half exactly in reverse",
             "The chain stops after the first step",
             "No positive case is given"],
         "correct": 1,
         "expl": "A precise mirror of the negative half, term for term."},
        {"q": "What does AN 5.25, the next discourse, approach differently from this one?",
         "opts": [
             "It repeats this exact chain",
             "It approaches related territory as five supports for right view specifically, rather "
             "than a causal chain of five sequential stages",
             "It abandons the topic of ethics and immersion entirely",
             "It returns to the sekhabala"],
         "correct": 1,
         "expl": "A structurally different approach to related material."},
        {"q": "Is the tree simile used to illustrate abundance or lack, in its first appearance?",
         "opts": [
             "Abundance only",
             "Lack — a tree missing branches and foliage, whose inner parts fail to grow",
             "Neither; the simile is purely decorative",
             "It illustrates a different topic entirely, unrelated to the chain"],
         "correct": 1,
         "expl": "The negative case comes first, then its positive mirror."},
        {"q": "What does the guide say about the relationship between the tree's parts and the "
              "chain's five steps?",
         "opts": [
             "No relationship is suggested",
             "A loose but suggestive correspondence — outer growth to inner, matching the chain's "
             "movement from outermost practice to innermost realization",
             "An exact one-to-one mapping stated explicitly in the text",
             "The tree simile contradicts the chain"],
         "correct": 1,
         "expl": "Suggestive rather than a stated formal correspondence."},
        {"q": "Where is AN 5.24 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Sāketa",
             "The Eastern Monastery"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("The chain", [
            "ethics &rarr;",
            "right immersion &rarr;",
            "true knowledge &amp; vision &rarr;",
            "disillusionment &rarr;",
            "freedom's knowledge &amp; vision",
        ]),
        ("The tree", [
            "no branches, foliage &rarr;",
            "shoots, bark, softwood,",
            "heartwood: stunted",
        ]),
        ("Filling a gap", [
            "AN 5.17&ndash;20: 3 steps",
            "AN 5.24: 5 steps",
            "&mdash; same journey, fuller",
        ]),
        ("Cross-references", [
            "AN 5.17&ndash;20 &middot; the shorter list",
            "AN 5.25 &middot; next: supports",
            "AN 5.23 &middot; the corruptions removed",
        ]),
    ],
    further=[
        '<a href="%s/an5.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; the shorter '
        "five-item list this discourse expands into a fuller causal chain.",
        '<a href="an-5.25.html">AN 5.25 &middot; Supported</a> &mdash; next, right view&rsquo;s '
        "own five supports.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; the previous discourse, on '
        "what stands in the way of the immersion this chain depends on.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.25 — Anuggahitasutta
# --------------------------------------------------------------------------- #
page(
    25, "Anuggahita", "Supported",
    vagga=VAGGA_3,
    meta_title="AN 5.25 — Supported | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anuggahitasutta — right "
        "view supported by five factors, ethics, learning, discussion, serenity, and discernment, "
        "bearing freedom of heart and freedom by wisdom as its fruit. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five supports for right view and the fruit they "
                 "produce"),
        ("Length", "~30 seconds to read"),
        ("Northern parallel", "Pairing serenity and discernment (samatha/vipassanā) as jointly "
                              "necessary supports is a standard doctrinal pairing across the "
                              "Chinese Āgamas and Abhidharma; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, but pairing terms not "
                       "yet combined this way elsewhere in this chapter"),
    ],
    why=(
        "Where AN 5.24 traced a chain of stages, this discourse names five things right view "
        "itself leans on: ethics, learning, discussion, serenity, and discernment. Two of these, "
        "<em>samatha</em> and <em>vipassanā</em>, serenity and discernment, are the classic "
        "meditative pair &mdash; calm and insight &mdash; named together here as jointly "
        "necessary supports rather than as sequential stages, which is a genuinely different "
        "relationship than the chain AN 5.24 just described."),
    guide=[
        ("The teaching in one sentence", [
            "Right view supported by ethics, learning, discussion, serenity, and discernment has "
            "freedom of heart and freedom by wisdom as its fruit and benefit."]),
        ("Support, not sequence", [
            "AN 5.24's chain moved in one direction, each stage a precondition for the next. This "
            "discourse instead names five things right view <em>leans on</em> "
            "(<em>anuggahitā</em>) all at once, with no stated order among them. Ethics does not "
            "come before discussion here, and discussion does not come before serenity; all five "
            "are named together as what holds right view up, the way several posts might support "
            "one roof rather than one post leading to the next."]),
        ("Two kinds of support, not one", [
            "The five split naturally into two kinds: ethics, learning, and discussion are things "
            "done largely in relation to others or to received teaching; serenity and discernment "
            "are internal meditative capacities. Right view, on this discourse's account, is not "
            "purely a private meditative achievement, nor purely a matter of study and "
            "conversation &mdash; it draws on both."]),
        ("Two fruits, named together", [
            "The discourse names both <em>cetovimutti</em>, freedom of heart, and "
            "<em>paññāvimutti</em>, freedom by wisdom, as the joint fruit of a well-supported "
            "right view &mdash; not one or the other, but both together, each with its own "
            "benefit named separately in the Pāli though rendered together in translation."]),
        ("Where the chapter goes from here", [
            "AN 5.26, next, turns from what supports right view to a related but distinct "
            "question: the specific occasions on which a mendicant's mind actually becomes freed, "
            "given as five concrete situations rather than five abstract supports."]),
    ],
    terms=[
        ("anuggahitā",
         "&ldquo;supported, leaned on&rdquo; &mdash; the word giving this discourse its title, "
         "naming a relationship of mutual support rather than sequence."),
        ("sākacchā",
         "&ldquo;discussion&rdquo; &mdash; the third support, placing conversation with others "
         "among what right view depends on."),
        ("samatha",
         "&ldquo;serenity&rdquo; &mdash; the fourth support, the calming half of the classic "
         "calm-and-insight meditative pair."),
        ("vipassanā",
         "&ldquo;discernment, insight&rdquo; &mdash; the fifth support, named alongside serenity "
         "as jointly necessary rather than as its successor."),
        ("cetovimutti paññāvimutti",
         "&ldquo;freedom of heart, freedom by wisdom&rdquo; &mdash; the joint fruit named for a "
         "well-supported right view, each named separately though rendered together."),
    ],
    text_intro=(
        "The discourse in full: the five supports for right view, and the fruit they produce "
        "together. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.25:1.1"),
        ("p", "&sect;2", "an5.25:2.2-2.3"),
    ],
    quiz=[
        {"q": "What five things does this discourse say right view is supported by?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Ethics, learning, discussion, serenity, and discernment",
             "The four noble truths plus one",
             "Ethics, immersion, wisdom, freedom, and knowledge and vision of freedom"],
         "correct": 1,
         "expl": "Five supports named together, not a sequence."},
        {"q": "How does the relationship between the five supports differ from AN 5.24's chain?",
         "opts": [
             "It is identical — a strict sequence",
             "The five supports are named together with no stated order, like several posts "
             "supporting one roof, rather than one stage leading to the next",
             "AN 5.25 has no relationship at all between its five items",
             "The five supports are ranked, with one named chief"],
         "correct": 1,
         "expl": "Support (anuggahitā), not sequence."},
        {"q": "What two kinds of support does the guide distinguish among the five?",
         "opts": [
             "Physical and mental",
             "Things done in relation to others or received teaching (ethics, learning, discussion) "
             "and internal meditative capacities (serenity, discernment)",
             "Monastic and lay supports",
             "No distinction is drawn among the five"],
         "correct": 1,
         "expl": "Right view draws on both social/textual and meditative sources, on this account."},
        {"q": "What two fruits does the discourse name together?",
         "opts": [
             "Wealth and reputation",
             "Freedom of heart (cetovimutti) and freedom by wisdom (paññāvimutti)",
             "Only freedom of heart, with wisdom left out",
             "Rebirth in a heavenly realm"],
         "correct": 1,
         "expl": "Both named jointly as the fruit of a well-supported right view."},
        {"q": "What classic meditative pair appears among the five supports?",
         "opts": [
             "Faith and energy",
             "Serenity (samatha) and discernment (vipassanā)",
             "Conscience and prudence",
             "Ethics and immersion"],
         "correct": 1,
         "expl": "Named together as jointly necessary, not as sequential stages."},
        {"q": "How long is this discourse compared to AN 5.24?",
         "opts": [
             "Much longer, with an extended simile",
             "Considerably shorter — a single sentence naming the five supports and their fruit",
             "Identical in length",
             "AN 5.25 has no text at all"],
         "correct": 1,
         "expl": "One of the briefest discourses in this chapter."},
        {"q": "What does AN 5.26, the next discourse, turn to?",
         "opts": [
             "A repeat of this same five-support list",
             "Five concrete occasions on which a mendicant's mind actually becomes freed",
             "A return to the sekhabala",
             "The end of the chapter"],
         "correct": 1,
         "expl": "A related but structurally distinct question — occasions, not abstract supports."},
        {"q": "Does this discourse offer a simile to illustrate its claim?",
         "opts": [
             "Yes, an extended parable",
             "No — a direct statement with no narrative illustration",
             "Yes, the gold-refining simile is reused",
             "Yes, the tree simile is reused"],
         "correct": 1,
         "expl": "Consistent with this discourse's terse, single-sentence form."},
        {"q": "Is ethics named among right view's supports here?",
         "opts": [
             "No, ethics is absent from this list",
             "Yes — ethics is the first of the five named supports",
             "Ethics is mentioned only as a contrast",
             "Ethics replaces right view entirely"],
         "correct": 1,
         "expl": "Sīla, learning, discussion, serenity, discernment — ethics named first."},
        {"q": "Where is AN 5.25 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Deer Park",
             "Campā"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("Five supports", [
            "ethics &middot; learning",
            "discussion &middot; serenity",
            "discernment",
        ]),
        ("Support, not sequence", [
            "<span class=\"pali\">anuggahitā</span>",
            "&mdash; posts holding up",
            "one roof, together",
        ]),
        ("Two fruits", [
            "<span class=\"pali\">cetovimutti</span>heart's freedom",
            "<span class=\"pali\">paññāvimutti</span>wisdom's freedom",
        ]),
        ("Cross-references", [
            "AN 5.24 &middot; a chain, by contrast",
            "AN 5.26 &middot; next: five occasions",
            "AN 5.17&ndash;20 &middot; freedom, named there too",
        ]),
    ],
    further=[
        '<a href="%s/an5.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.24.html">AN 5.24 &middot; Unethical</a> &mdash; the previous discourse, a '
        "causal chain by contrast with this page's simultaneous supports.",
        '<a href="an-5.26.html">AN 5.26 &middot; Opportunities for Freedom</a> &mdash; next, five '
        "concrete occasions rather than five abstract supports.",
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; where freedom '
        "and freedom by wisdom already appeared together in this chapter's predecessor.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.26 — Vimuttāyatanasutta
# --------------------------------------------------------------------------- #
page(
    26, "Vimuttāyatana", "Opportunities for Freedom",
    vagga=VAGGA_3,
    meta_title="AN 5.26 — Opportunities for Freedom | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vimuttāyatanasutta — "
        "five occasions on which a diligent mendicant's mind is freed, four of them built almost "
        "entirely from engagement with words: hearing the teaching, teaching it, reciting it, and "
        "reflecting on it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five occasions, each running through the identical five-link chain from "
                 "inspiration to immersion"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The joy-to-immersion chain (pāmojja, pīti, passaddhi, sukha, "
                              "samādhi) is one of the most widely attested formulas across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; five parallel cases sharing "
                       "one internal mechanism, worth reading for what the five have in common"),
    ],
    why=(
        "Four of this discourse's five opportunities for freedom have nothing to do with silent "
        "meditation. A mendicant hears the teaching from the Buddha or a respected companion; or "
        "teaches it to others from memory; or simply recites it to themselves; or turns it over "
        "in thought. Only the fifth involves a meditation subject directly. In every case the same "
        "five-link chain follows &mdash; inspiration, joy, rapture, tranquility, bliss, immersion "
        "&mdash; which means this discourse treats verbal and cognitive engagement with the "
        "Dhamma as, four times out of five, doorways to freedom in their own right."),
    guide=[
        ("The teaching in one sentence", [
            "There are five opportunities for freedom &mdash; hearing the teaching taught, "
            "teaching it to others, reciting it, reflecting on it, and properly grasping a "
            "meditation subject &mdash; and at any of them, a diligent mendicant's mind can "
            "become freed."]),
        ("One chain, run five times", [
            "Every one of the five occasions closes with the identical sequence: feeling inspired, "
            "joy springs up; being joyful, rapture springs up; the mind full of rapture, the body "
            "becomes tranquil; the body tranquil, one feels bliss; and blissful, the mind becomes "
            "immersed in samādhi. The discourse does not vary this chain across its five cases; it "
            "varies only what triggers the chain to begin."]),
        ("Four occasions built from words", [
            "The first occasion is hearing the Teacher or a respected companion teach. The second "
            "is teaching others oneself, from what was learned and memorized. The third is "
            "reciting the teaching, alone, from memory. The fourth is thinking it over and "
            "examining it in the heart. None of these is silent, wordless meditation; all four are "
            "forms of engagement with language &mdash; heard, spoken, recited, or turned over in "
            "thought &mdash; and each is said to be sufficient, on its own, to set the same chain "
            "toward freedom running."]),
        ("The fifth occasion, and what it shares with the other four", [
            "Only the fifth names a meditation subject directly: properly grasped, focused on, "
            "borne in mind, and penetrated with wisdom. Even here, though, the discourse frames "
            "the trigger as being <em>inspired</em> by it, using the same "
            "<em>atthapaṭisaṁvedī&hellip;dhammapaṭisaṁvedī</em>, inspired by the meaning and by "
            "the teaching, that describes the other four. The fifth occasion is not categorically "
            "different from the first four; it is simply the one where the object is a meditation "
            "sign rather than spoken or recited words."]),
        ("Why this list matters for how the teaching is used", [
            "A reader who assumes freedom is reached only through silent, wordless meditation "
            "practice will find this discourse worth sitting with. Teaching others, reciting from "
            "memory, and quiet reflection on the Dhamma are named here as equally capable "
            "opportunities, each running the identical mechanism through to immersion. The "
            "discourse does not rank the five, or call any one of them the true path and the "
            "others preliminary."]),
    ],
    terms=[
        ("vimuttāyatana",
         "&ldquo;opportunity for freedom&rdquo; &mdash; this discourse's title, naming five "
         "distinct occasions rather than one method."),
        ("atthapaṭisaṁvedī dhammapaṭisaṁvedī",
         "&ldquo;inspired by the meaning, inspired by the teaching&rdquo; &mdash; the shared "
         "trigger phrase opening the identical chain in all five occasions."),
        ("pāmojja",
         "&ldquo;joy&rdquo; &mdash; the first link in the chain, arising directly from feeling "
         "inspired."),
        ("passaddhi",
         "&ldquo;tranquility&rdquo; &mdash; the fourth link, where rapture in the mind settles "
         "into physical calm."),
        ("samādhinimitta",
         "&ldquo;meditation subject, sign for immersion&rdquo; &mdash; the fifth occasion's "
         "trigger, the only one of the five not built from spoken or recited words."),
    ],
    text_intro=(
        "The discourse in full: the five occasions, each running the identical chain from "
        "inspiration through to immersion. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five opportunities for freedom"),
        ("p", "&sect;1", "an5.26:1.1"),
        ("h3", "First: hearing the teaching taught"),
        ("p", "&sect;2", "an5.26:2.2-2.9"),
        ("h3", "Second: teaching others from memory"),
        ("p", "&sect;3", "an5.26:3.1-3.8"),
        ("h3", "Third: reciting the teaching"),
        ("p", "&sect;4", "an5.26:4.1-4.8"),
        ("h3", "Fourth: reflecting on the teaching"),
        ("p", "&sect;5", "an5.26:5.1-5.9"),
        ("h3", "Fifth: grasping a meditation subject"),
        ("p", "&sect;6", "an5.26:6.1-6.9"),
        ("h3", "Closing"),
        ("p", "&sect;7", "an5.26:7.1"),
    ],
    quiz=[
        {"q": "How many of this discourse's five opportunities for freedom involve a meditation "
              "subject directly, rather than spoken or recited words?",
         "opts": ["All five", "Four", "Only one", "None"],
         "correct": 2,
         "expl": "Only the fifth; the other four are built from hearing, teaching, reciting, or reflecting on the Dhamma."},
        {"q": "What chain follows each of the five occasions, without variation?",
         "opts": [
             "A different chain each time, tailored to the occasion",
             "Feeling inspired, joy, rapture, bodily tranquility, bliss, and immersion in samādhi",
             "A chain leading directly to a specific rebirth",
             "No chain is described; each occasion simply ends"],
         "correct": 1,
         "expl": "The identical five-link sequence closes all five occasions."},
        {"q": "What is the first opportunity for freedom?",
         "opts": [
             "Grasping a meditation subject",
             "Hearing the Teacher or a respected spiritual companion teach the Dhamma",
             "Teaching others from memory",
             "Silent walking meditation"],
         "correct": 1,
         "expl": "The most straightforwardly receptive of the five occasions."},
        {"q": "What is the second opportunity?",
         "opts": [
             "Reciting the teaching alone",
             "Teaching Dhamma in detail to others, as one learned and memorized it",
             "Grasping a meditation subject",
             "A dream during sleep"],
         "correct": 1,
         "expl": "Even in the act of teaching others, the same chain toward freedom can begin."},
        {"q": "How does the guide characterize the first four occasions as a group?",
         "opts": [
             "As entirely unrelated to each other",
             "As forms of engagement with language — heard, spoken, recited, or reflected on — "
             "rather than silent, wordless meditation",
             "As inferior preliminary steps before real practice begins",
             "As applicable only to advanced meditators"],
         "correct": 1,
         "expl": "Four of five occasions built from words, each sufficient on its own."},
        {"q": "How does the fifth occasion's trigger compare to the other four's?",
         "opts": [
             "It is categorically different, using entirely different language",
             "It uses the same 'inspired by the meaning, inspired by the teaching' phrasing as the "
             "other four, differing only in what the object is",
             "It requires no inspiration at all",
             "It contradicts the mechanism of the other four"],
         "correct": 1,
         "expl": "The fifth is not set apart in kind, only in the nature of its object."},
        {"q": "Does the discourse rank the five occasions, calling one the true path and the "
              "others preliminary?",
         "opts": [
             "Yes, the fifth is named as superior",
             "No — all five are presented as equally capable opportunities",
             "Yes, the first is named as superior",
             "The discourse takes no position on this question at all, offering no comparison"],
         "correct": 1,
         "expl": "Each occasion is said to be sufficient in its own right."},
        {"q": "What is required for the mind to actually become freed on any of these occasions?",
         "opts": [
             "Nothing further is required beyond the occasion occurring",
             "The mendicant must stay diligent, keen, and resolute at that time",
             "Years of prior training with no exceptions",
             "Permission from a senior monk"],
         "correct": 1,
         "expl": "Appamattassa ātāpino pahitattassa — the condition stated at both the opening and closing of the discourse."},
        {"q": "What phrase repeats identically to open the chain in every one of the five cases?",
         "opts": [
             "A prayer for rebirth",
             "'Inspired by the meaning and inspired by the teaching' (atthapaṭisaṁvedī "
             "dhammapaṭisaṁvedī)",
             "A vow of silence",
             "A request for permission to teach"],
         "correct": 1,
         "expl": "The shared trigger phrase across all five occasions."},
        {"q": "Where is AN 5.26 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Kosambī",
             "The Bhagga country"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("Five occasions", [
            "1. hearing it taught",
            "2. teaching others",
            "3. reciting it",
            "4. reflecting on it",
            "5. a meditation subject",
        ]),
        ("One chain, five times", [
            "inspired &rarr; joy &rarr; rapture",
            "&rarr; tranquil &rarr; bliss",
            "&rarr; immersed in samādhi",
        ]),
        ("Four out of five", [
            "built from words:",
            "heard, spoken,",
            "recited, reflected",
        ]),
        ("Cross-references", [
            "AN 5.25 &middot; supports for right view",
            "AN 5.28 &middot; the abhiññā this chain enables",
            "AN 5.27 &middot; next: five knowledges",
        ]),
    ],
    further=[
        '<a href="%s/an5.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.25.html">AN 5.25 &middot; Supported</a> &mdash; the previous discourse, on '
        "what right view leans on.",
        '<a href="an-5.27.html">AN 5.27 &middot; Immersion</a> &mdash; next, five knowledges that '
        "arise from developing the immersion these occasions lead toward.",
        '<a href="an-5.29.html">AN 5.29 &middot; Walking Meditation</a> &mdash; later in this '
        "chapter, a very different, physical opportunity for benefit.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.27 — Samādhisutta
# --------------------------------------------------------------------------- #
page(
    27, "Samādhi", "Immersion",
    vagga=VAGGA_3,
    next=("an-5.28.html", "AN 5.28 &middot; With Five Factors"),
    meta_title="AN 5.27 — Immersion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Samādhisutta of "
        "the Fives — five knowledges that arise personally from developing limitless immersion, "
        "including a warning against immersion held in place by forceful suppression. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A short injunction to develop immersion, followed by five self-arising "
                 "knowledges about the immersion developed"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Self-diagnostic criteria for genuine versus strained meditative "
                              "attainment appear widely in Chinese Buddhist meditation manuals; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, and unusually "
                       "practical for a self-check on one's own meditation"),
    ],
    why=(
        "This discourse offers something the chapter has not given before: a way to check one's "
        "own meditation, from the inside, without needing anyone else to confirm it. Develop "
        "limitless immersion, alert and mindful, and five knowledges are said to arise "
        "<em>personally</em> &mdash; not taught by another, but known directly. The fourth of the "
        "five draws a line this reading guide has not seen drawn this explicitly before: real "
        "immersion is <em>not held in place by forceful suppression</em>."),
    guide=[
        ("The teaching in one sentence", [
            "Develop limitless immersion, alert and mindful, and five knowledges arise "
            "personally: that this immersion is blissful now and later, noble and not of the "
            "flesh, not cultivated by inferior people, peaceful and not forced, and that one can "
            "enter and emerge from it mindfully."]),
        ("Knowledge arising personally, not taught", [
            "<em>Paccattaññeva</em>, personally, marks all five knowledges as self-verified rather "
            "than received on authority. This is a different relationship to knowledge than "
            "most of this chapter has described: not something a teacher confirms from outside, "
            "but something the immersion itself makes evident to the person developing it."]),
        ("The fourth knowledge, read closely", [
            "&lsquo;Peaceful and sublime and tranquil and unified, <em>not held in place by "
            "forceful suppression</em>&rsquo; &mdash; <em>na sasaṅkhāraniggayhavāritagato</em> "
            "&mdash; is the discourse's sharpest diagnostic. It distinguishes immersion that "
            "settles naturally from immersion maintained only by continuous effortful pressure. A "
            "reader straining to hold a meditative state still by force, rather than allowing it "
            "to settle, has, on this discourse's own terms, a way to recognize the difference "
            "themselves."]),
        ("Noble, and &lsquo;not of the flesh&rsquo;", [
            "<em>Nirāmisa</em>, not of the flesh, not carnal, marks the second knowledge as a "
            "distinction between two kinds of pleasure &mdash; one bound up with sensual "
            "gratification, one not. This distinction recurs across the canon whenever meditative "
            "bliss needs to be marked off from ordinary sensory pleasure, and this discourse uses "
            "it as one of the five marks a mendicant can personally verify."]),
        ("A practical page in a chapter of larger claims", [
            "Compared to AN 5.23's extended list of superhuman abilities, or AN 5.24's causal "
            "chain toward freedom, this discourse is narrowly practical: not what immersion leads "
            "to, but how to recognize when the immersion one has developed is the genuine article. "
            "For readers actually practicing meditation rather than only studying the canon "
            "academically, this is arguably the most directly usable discourse the chapter has "
            "offered so far."]),
    ],
    terms=[
        ("paccattaññeva",
         "&ldquo;personally, by oneself&rdquo; &mdash; marking all five knowledges as "
         "self-verified rather than received from a teacher."),
        ("nirāmisa",
         "&ldquo;not of the flesh, not carnal&rdquo; &mdash; the second knowledge, distinguishing "
         "meditative bliss from ordinary sensory pleasure."),
        ("akāpurisasevita",
         "&ldquo;not cultivated by reprobates&rdquo; &mdash; the third knowledge, an unusually "
         "blunt term marking genuine immersion by who does not typically attain it."),
        ("na sasaṅkhāraniggayhavāritagato",
         "&ldquo;not held in place by forceful suppression&rdquo; &mdash; the fourth knowledge's "
         "sharpest clause, distinguishing settled immersion from strained concentration."),
        ("sato samāpajjati sato vuṭṭhahati",
         "&ldquo;mindfully enters, mindfully emerges&rdquo; &mdash; the fifth knowledge, marking "
         "genuine immersion by the quality of attention at its boundaries, not only within it."),
    ],
    text_intro=(
        "The discourse in full: the injunction to develop limitless immersion, and the five "
        "knowledges that personally arise from doing so. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Develop limitless immersion"),
        ("p", "&sect;1", "an5.27:1.1-1.3"),
        ("h3", "Five knowledges, arising personally"),
        ("p", "&sect;2", "an5.27:1.4"),
        ("p", "&sect;3", "an5.27:1.5"),
        ("p", "&sect;4", "an5.27:1.6"),
        ("p", "&sect;5", "an5.27:1.7"),
        ("p", "&sect;6", "an5.27:1.8"),
        ("h3", "Closing"),
        ("p", "&sect;7", "an5.27:2.1-2.2"),
    ],
    quiz=[
        {"q": "What five knowledges does this discourse say arise from developing limitless "
              "immersion?",
         "opts": [
             "The five powers",
             "That the immersion is blissful, noble, not for inferior people, peaceful and not "
             "forced, and mindfully entered and left",
             "The five hindrances",
             "The five destinations of rebirth"],
         "correct": 1,
         "expl": "Five self-diagnostic marks of genuine immersion."},
        {"q": "What does 'paccattaññeva' mark these five knowledges as?",
         "opts": [
             "Received on the authority of a teacher",
             "Arising personally, self-verified rather than taught by another",
             "Doubtful and unreliable",
             "Applicable only to arahants"],
         "correct": 1,
         "expl": "A different relationship to knowledge than most of this chapter has described."},
        {"q": "What does the fourth knowledge, 'not held in place by forceful suppression', "
              "distinguish?",
         "opts": [
             "Nothing specific; it is a decorative phrase",
             "Immersion that settles naturally from immersion maintained only by continuous "
             "effortful pressure",
             "Monastic ordination from lay practice",
             "Two different postures for meditation"],
         "correct": 1,
         "expl": "The discourse's sharpest diagnostic clause, per the guide."},
        {"q": "What does 'nirāmisa' mean, and what does it distinguish?",
         "opts": [
             "'Not of the flesh' — distinguishing meditative bliss from ordinary sensory pleasure",
             "'Not visible' — meaning the immersion cannot be observed by others",
             "'Not permanent' — meaning the immersion always fades quickly",
             "'Not taught' — meaning no teacher ever describes it"],
         "correct": 0,
         "expl": "A recurring distinction across the canon between carnal and non-carnal pleasure."},
        {"q": "How does the guide characterize this discourse compared to AN 5.23 and 5.24?",
         "opts": [
             "Identical in scope and content",
             "Narrowly practical — how to recognize genuine immersion, rather than what immersion "
             "leads to",
             "Entirely unrelated to immersion",
             "A contradiction of AN 5.23 and 5.24"],
         "correct": 1,
         "expl": "Arguably the most directly usable discourse in the chapter for an actual meditator."},
        {"q": "What does the fifth knowledge concern?",
         "opts": [
             "The immersion's duration only",
             "Mindfully entering and emerging from the immersion, not only what happens within it",
             "The physical location where immersion should be practiced",
             "Whether other people can perceive the immersion"],
         "correct": 1,
         "expl": "Marking genuine immersion by the quality of attention at its boundaries as well as inside it."},
        {"q": "What comes immediately after AN 5.27 in this chapter, and what happens to it?",
         "opts": [
             "AN 5.28, a page from the earlier eighteen-page-selection era, left as is and linked "
             "rather than rebuilt",
             "The chapter simply ends",
             "A brand-new discourse built for this project",
             "A return to AN 5.21's ladder"],
         "correct": 0,
         "expl": "This page's 'next' link points explicitly to that existing page."},
        {"q": "What does 'akāpurisasevita' mean?",
         "opts": [
             "'Cultivated by everyone equally'",
             "'Not cultivated by reprobates' — an unusually blunt marker of genuine attainment",
             "'Cultivated only by monastics, never laypeople'",
             "'Not yet cultivated by anyone'"],
         "correct": 1,
         "expl": "The third of the five self-verifying knowledges."},
        {"q": "Is this discourse's immersion described as bounded by time?",
         "opts": [
             "Yes, only for one sitting",
             "The first knowledge names it as blissful now and resulting in bliss in the future",
             "The discourse takes no position on this",
             "It is described as instantly fading"],
         "correct": 1,
         "expl": "Both present and future benefit are named in the first knowledge."},
        {"q": "Where is AN 5.27 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "Rājagaha",
             "Vesālī"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("Five knowledges", [
            "blissful, now &amp; later",
            "noble, not of the flesh",
            "not for reprobates",
            "peaceful, not forced",
            "entered/left mindfully",
        ]),
        ("The sharp clause", [
            "<span class=\"pali\">na sasaṅkhāra-</span>",
            "<span class=\"pali\">niggayhavāritagato</span>",
            "not forced &mdash; settled",
        ]),
        ("Self-verified", [
            "<span class=\"pali\">paccattaññeva</span>",
            "&mdash; known directly,",
            "not taught by another",
        ]),
        ("Cross-references", [
            "AN 5.23 &middot; abhiññā, from purity",
            "AN 5.26 &middot; the chain toward this",
            "AN 5.28 &middot; next: the legacy page",
        ]),
    ],
    further=[
        '<a href="%s/an5.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.26.html">AN 5.26 &middot; Opportunities for Freedom</a> &mdash; the '
        "previous discourse, on how immersion of this kind is first reached.",
        '<a href="an-5.28.html">AN 5.28 &middot; With Five Factors</a> &mdash; next, this '
        "chapter&rsquo;s own namesake discourse, on immersion built from five factors in full.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; earlier in this chapter, '
        "on what stands in the way of the immersion checked here.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.29 — Caṅkamasutta
# --------------------------------------------------------------------------- #
page(
    29, "Caṅkama", "Walking Meditation",
    vagga=VAGGA_3,
    prev=("an-5.28.html", "AN 5.28 &middot; With Five Factors"),
    meta_title="AN 5.29 — Walking Meditation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Caṅkamasutta — five "
        "practical benefits of walking meditation: fitness for travel, fitness for striving, "
        "health, digestion, and longer-lasting immersion. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five practical benefits, with no elaboration"),
        ("Length", "~20 seconds to read"),
        ("Northern parallel", "The benefits of walking meditation for physical health and "
                              "digestion recur in monastic regulation texts across the Chinese "
                              "tradition; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest and most "
                       "physically concrete discourse in the chapter so far"),
    ],
    why=(
        "After a chapter of ladders, chains, corruptions, and self-verifying knowledges, this "
        "discourse returns to something almost entirely bodily: what walking meditation is "
        "actually good for. Fitness for travel, fitness for striving, health, proper digestion, "
        "and immersion that lasts longer once gained while walking. Nothing here is abstract; "
        "every benefit is something a practitioner could notice for themselves within days of "
        "trying it."),
    guide=[
        ("The teaching in one sentence", [
            "Walking meditation has five benefits: fitness for traveling, fitness for striving in "
            "meditation, health, proper digestion of what is eaten and drunk, and immersion gained "
            "while walking that lasts a long time."]),
        ("A body-first list, in a chapter of abstractions", [
            "Every other discourse in this chapter so far has concerned ethics, immersion, wisdom, "
            "freedom, or the corruptions and knowledges attached to them. This discourse names "
            "physical fitness and digestion in the same breath as immersion, without ranking the "
            "bodily benefits below the meditative one. The list moves from the concrete "
            "(<em>addhānakkhama</em>, fit for travel) to the meditative "
            "(<em>caṅkamādhigato samādhi</em>, immersion gained while walking) without a change of "
            "register."]),
        ("Why digestion appears in a list about meditation", [
            "&lsquo;What&rsquo;s eaten, drunk, chewed, and tasted is properly digested&rsquo; sits "
            "as the fourth benefit, between health and lasting immersion. For a monastic "
            "community eating once a day, often on alms food of uncertain quality, a practical "
            "aid to digestion is not a minor concern; the discourse treats it as worth naming "
            "alongside loftier benefits rather than beneath mention."]),
        ("&lsquo;Lasts a long time&rsquo;: a claim about durability, not depth", [
            "The final benefit, <em>ciraṭṭhitiko</em>, does not claim walking meditation produces "
            "a deeper or superior immersion &mdash; only a more durable one. This is a modest, "
            "specific claim, consistent with the rest of the list's practical, unhurried tone."]),
        ("Where the chapter closes from here", [
            "AN 5.30, the chapter's final discourse, returns to narrative &mdash; a crowd of "
            "brahmins and householders bringing food to the Buddha, and his own, sharply worded "
            "reflection on fame. It is a striking discourse to end a practical chapter on, and "
            "this reading guide will not soften its edges when it arrives."]),
    ],
    terms=[
        ("caṅkama",
         "&ldquo;walking meditation&rdquo; &mdash; this discourse's title and subject, a standard "
         "monastic practice alongside sitting."),
        ("addhānakkhama",
         "&ldquo;fit for traveling&rdquo; &mdash; the first benefit, a directly physical claim "
         "about stamina."),
        ("padhānakkhama",
         "&ldquo;fit for striving&rdquo; &mdash; the second benefit, connecting physical fitness "
         "to meditative effort specifically."),
        ("appābādha",
         "&ldquo;healthy, free of illness&rdquo; &mdash; the third benefit, named plainly without "
         "further qualification."),
        ("ciraṭṭhitika",
         "&ldquo;long-lasting&rdquo; &mdash; the fifth benefit's key word, a claim about "
         "durability rather than depth."),
    ],
    text_intro=(
        "The discourse in full: the five benefits of walking meditation, named once. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.29:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five benefits does this discourse name for walking meditation?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Fitness for travel, fitness for striving, health, proper digestion, and long-lasting "
             "immersion gained while walking",
             "The five hindrances overcome",
             "The five powers strengthened"],
         "correct": 1,
         "expl": "A body-first list, moving from concrete fitness to meditative durability."},
        {"q": "How does the guide characterize this discourse compared to the rest of the chapter?",
         "opts": [
             "Identical in register to every other discourse",
             "Almost entirely bodily, naming physical fitness and digestion alongside immersion "
             "without ranking one below the other",
             "Purely doctrinal, with no practical content",
             "A repeat of AN 5.23's corruptions"],
         "correct": 1,
         "expl": "A striking shift in register within the chapter."},
        {"q": "Why does the guide say digestion is worth including in a list about meditation?",
         "opts": [
             "It isn't worth including, and the guide calls it a scribal error",
             "For a monastic community eating alms food once daily, digestion is a genuine "
             "practical concern, not a minor one",
             "Digestion has nothing to do with the rest of the list",
             "Digestion is a later addition not in the original text"],
         "correct": 1,
         "expl": "Named alongside loftier benefits rather than beneath mention."},
        {"q": "What does the fifth benefit, 'ciraṭṭhitiko', actually claim?",
         "opts": [
             "That walking-meditation immersion is deeper than any other kind",
             "That it lasts a long time — a claim about durability, not superior depth",
             "That it is instantaneous",
             "That it never fades at all, under any circumstances"],
         "correct": 1,
         "expl": "A modest, specific claim, consistent with the list's practical tone."},
        {"q": "What comes immediately before this discourse in the chapter's actual reading order?",
         "opts": [
             "AN 5.27",
             "AN 5.28, the legacy page this discourse's 'prev' link points to explicitly",
             "AN 5.21",
             "Nothing; this is the chapter's first discourse"],
         "correct": 1,
         "expl": "An explicit override, since AN 5.28 sits between AN 5.27 and AN 5.29 in sequence but is not regenerated."},
        {"q": "What does AN 5.30, the chapter's closing discourse, turn to?",
         "opts": [
             "Another short list of practical benefits",
             "A narrative involving a crowd of brahmins and householders, and the Buddha's own "
             "sharply worded reflection on fame",
             "A repeat of the five hindrances",
             "The chapter simply has no closing discourse"],
         "correct": 1,
         "expl": "A striking shift from this discourse's practical brevity."},
        {"q": "Is any simile or narrative used to illustrate this discourse's claims?",
         "opts": [
             "Yes, an extended parable",
             "No — a single bare list, with no illustration",
             "Yes, the tree simile is reused",
             "Yes, a dialogue with a named questioner"],
         "correct": 1,
         "expl": "The chapter's shortest and most direct discourse."},
        {"q": "What is the second benefit, 'padhānakkhama', specifically about?",
         "opts": [
             "Fitness connected to meditative striving specifically, not fitness in general",
             "Immunity from all illness",
             "Freedom from hunger entirely",
             "The ability to travel without rest"],
         "correct": 0,
         "expl": "Distinct from the first benefit's more general travel fitness."},
        {"q": "How long is this discourse to read?",
         "opts": [
             "About twenty seconds — the shortest discourse in the chapter",
             "Several minutes, with an extended simile",
             "Roughly the same length as AN 5.23",
             "It has no readable text"],
         "correct": 0,
         "expl": "A single sentence, with no elaboration."},
        {"q": "Where is AN 5.29 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting at Sāvatthī",
             "The Squirrels' Sanctuary",
             "Uruvelā"],
         "correct": 1,
         "expl": "Consistent with the pattern across this nipāta so far."},
    ],
    marginalia=[
        ("Five benefits", [
            "fit for travel",
            "fit for striving",
            "healthy",
            "food digests well",
            "immersion lasts long",
        ]),
        ("Body, then mind", [
            "concrete fitness &rarr;",
            "meditative durability",
            "&mdash; no change in register",
        ]),
        ("A modest claim", [
            "<span class=\"pali\">ciraṭṭhitiko</span>",
            "&mdash; lasts long,",
            "not claimed to be deeper",
        ]),
        ("Cross-references", [
            "AN 5.28 &middot; the legacy page, before",
            "AN 5.27 &middot; five knowledges of samādhi",
            "AN 5.30 &middot; next: closing the chapter",
        ]),
    ],
    further=[
        '<a href="%s/an5.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.28.html">AN 5.28 &middot; With Five Factors</a> &mdash; the preceding page '
        "in this chapter's reading order.",
        '<a href="an-5.27.html">AN 5.27 &middot; Immersion</a> &mdash; five knowledges for '
        "checking the immersion this discourse says walking meditation can also produce.",
        '<a href="an-5.30.html">AN 5.30 &middot; With Nāgita</a> &mdash; next, and this '
        "chapter's closing discourse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.30 — Nāgitasutta
# --------------------------------------------------------------------------- #
page(
    30, "Nāgita", "With Nāgita",
    vagga=VAGGA_3,
    meta_title="AN 5.30 — With Nāgita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nāgitasutta, closing "
        "this chapter — a crowd of brahmins and householders bringing food to the Buddha, his "
        "blunt refusal of fame and the 'filthy, lazy pleasure' of popularity, and five stark "
        "meditations on what ordinary life's pleasures actually come to. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Icchānaṅgala, a Kosalan brahmin village, in a forest nearby; stated at the "
                    "head of this discourse"),
        ("Speakers", "The Buddha and his attendant, Venerable Nāgita"),
        ("Form", "A narrative frame — a crowd bringing food, a question about noise — opening "
                 "onto two rounds of the Buddha's own reflection on fame"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The Buddha's wariness of fame and popularity, and meditations on "
                              "impermanence closing a discourse, are recurring themes across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; closes the chapter on its "
                       "most unguarded and least comfortable note"),
    ],
    why=(
        "This chapter closes not with a list but with a scene: a crowd outside a forest gate, "
        "making enough noise that the Buddha mistakes it for fishermen hauling in a catch. When "
        "Nāgita explains they have come with food especially for him, the Buddha's response is "
        "immediate and severe: <em>may I never become famous. May fame not come to me.</em> What "
        "follows is one of the plainest statements in this series of what the Buddha says he "
        "does not want, and why &mdash; closing with five meditations this reading guide will not "
        "soften."),
    guide=[
        ("The teaching in one sentence", [
            "When brahmins and householders bring food and make a great commotion outside his "
            "forest dwelling, the Buddha tells his attendant Nāgita that he wants no part of fame "
            "or popularity, calling the pleasure of possessions, honor, and popularity "
            "&lsquo;filthy&rsquo; and &lsquo;lazy&rsquo;, and closes with five stark meditations "
            "on what ordinary pleasures actually lead to."]),
        ("A crowd, mistaken for fishermen", [
            "The discourse opens with an image worth sitting with before its argument begins: the "
            "Buddha, hearing a colossal racket outside, assumes it is fishermen hauling in a "
            "catch. The comparison is not flattering to the crowd that has actually come &mdash; "
            "devoted brahmins and householders bringing food specifically for him &mdash; and the "
            "discourse does not walk it back once Nāgita corrects the mistake."]),
        ("&lsquo;May I never become famous&rsquo;, said twice", [
            "The Buddha's refusal of fame is stated twice in this discourse, word for word "
            "identical both times: he does not want fame, because he already has, without "
            "trouble or difficulty, the pleasure of renunciation, seclusion, peace, and awakening "
            "&mdash; and those who lack that pleasure are welcome to <em>the filthy, lazy pleasure "
            "of possessions, honor, and popularity</em> instead. The language is unusually blunt "
            "for this series; the discourse does not round the phrase &lsquo;filthy, lazy "
            "pleasure&rsquo; into something gentler."]),
        ("Nāgita's argument for relenting, and its quiet irony", [
            "Between the two identical refusals, Nāgita urges the Buddha to relent, arguing that "
            "wherever the Buddha now goes, brahmins and householders will follow &mdash; like "
            "rain flowing downhill &mdash; because of his ethics and wisdom. Nāgita's argument is "
            "itself an instance of exactly the kind of appeal to reputation the Buddha has just "
            "rejected, and the discourse lets that tension stand without resolving it explicitly "
            "before the Buddha simply repeats his refusal and moves on to explain, more fully, "
            "why."]),
        ("Five outcomes, stated without comfort", [
            "The discourse's final teaching is five plain observations, each closed by the "
            "refrain <em>eso tassa nissando</em>, this is its outcome: food eaten ends as "
            "excrement and urine; the loss of loved ones brings grief; meditating on ugliness "
            "stabilizes revulsion at beauty; observing impermanence in the six sense fields "
            "stabilizes revulsion at contact; observing rise and fall in the five grasping "
            "aggregates stabilizes revulsion at grasping. None of these is offered as a comforting "
            "thought. They are named as facts about what ordinary attachments and their opposite "
            "meditations actually produce, in the plainest terms the discourse can manage."]),
    ],
    terms=[
        ("uccāsaddamahāsadda",
         "&ldquo;a colossal racket&rdquo; &mdash; the noise that opens the discourse, compared by "
         "the Buddha to fishermen hauling in a catch."),
        ("mīḷhasukha middhasukha",
         "&ldquo;filthy pleasure, lazy pleasure&rdquo; &mdash; the Buddha's blunt description of "
         "the pleasure of possessions, honor, and popularity."),
        ("nekkhammasukha",
         "&ldquo;the pleasure of renunciation&rdquo; &mdash; the first of four pleasures the "
         "Buddha says he already has without trouble, set against fame."),
        ("nissando",
         "&ldquo;outcome, result&rdquo; &mdash; the refrain closing each of the discourse's five "
         "final observations."),
        ("pāṭikulyatā",
         "&ldquo;revulsion, repulsion&rdquo; &mdash; the stabilized result each of the four "
         "meditation-based outcomes produces."),
    ],
    text_intro=(
        "The discourse in full: the crowd's arrival, the Buddha's refusal of fame stated twice, "
        "Nāgita's argument in between, and the five closing outcomes. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Icchānaṅgala"),
        ("p", "&sect;1", "an5.30:1.1-1.4"),
        ("p", "&sect;2", "an5.30:1.5-1.10"),
        ("p", "&sect;3", "an5.30:1.11"),
        ("h3", "A colossal racket"),
        ("p", "&sect;4", "an5.30:2.1-2.3"),
        ("p", "&sect;5", "an5.30:2.4"),
        ("h3", "&ldquo;May I never become famous&rdquo;"),
        ("p", "&sect;6", "an5.30:2.5-2.7"),
        ("h3", "Nāgita's argument"),
        ("p", "&sect;7", "an5.30:3.1-3.7"),
        ("h3", "Refused again, and explained"),
        ("p", "&sect;8", "an5.30:4.1-4.3"),
        ("h3", "Five outcomes"),
        ("p", "&sect;9", "an5.30:4.4-4.5"),
        ("p", "&sect;10", "an5.30:4.6-4.7"),
        ("p", "&sect;11", "an5.30:4.8-4.9"),
        ("p", "&sect;12", "an5.30:4.10-4.11"),
        ("p", "&sect;13", "an5.30:4.12-4.13"),
    ],
    quiz=[
        {"q": "What does the Buddha initially mistake the crowd's noise for?",
         "opts": [
             "An attacking army",
             "Fishermen hauling in a catch",
             "A festival celebration",
             "A funeral procession"],
         "correct": 1,
         "expl": "An unflattering comparison the discourse does not walk back."},
        {"q": "What is the Buddha's stated reaction to the crowd bringing food specifically for "
              "him?",
         "opts": [
             "Delight and gratitude",
             "'May I never become famous. May fame not come to me,' stated bluntly",
             "Indifference, with no comment at all",
             "He immediately leaves the area"],
         "correct": 1,
         "expl": "One of the plainest refusals of fame in this series."},
        {"q": "How does the Buddha describe the pleasure of possessions, honor, and popularity?",
         "opts": [
             "As a harmless minor pleasure",
             "As 'filthy' and 'lazy' pleasure",
             "As the highest form of happiness available",
             "As something he secretly desires"],
         "correct": 1,
         "expl": "Unusually blunt language, not softened in this reading guide's presentation."},
        {"q": "What argument does Nāgita make for the Buddha to relent?",
         "opts": [
             "That the food will otherwise go to waste",
             "That wherever the Buddha goes, people will follow because of his ethics and wisdom — "
             "like rain flowing downhill",
             "That refusing would violate a monastic rule",
             "That the crowd will become violent if refused"],
         "correct": 1,
         "expl": "An argument the guide notes is itself an appeal to exactly the reputation the Buddha has just rejected."},
        {"q": "Does the discourse explicitly resolve the tension in Nāgita's argument appealing to "
              "reputation right after the Buddha rejects fame?",
         "opts": [
             "Yes, at great length",
             "No — the tension is left standing, and the Buddha simply repeats his refusal",
             "The discourse claims there is no tension at all",
             "Nāgita withdraws his argument immediately"],
         "correct": 1,
         "expl": "The guide flags this as a quiet irony the text does not resolve for the reader."},
        {"q": "What refrain closes each of the discourse's five final observations?",
         "opts": [
             "'This is impermanent'",
             "'Eso tassa nissando' — this is its outcome",
             "'This must be abandoned'",
             "No refrain is used"],
         "correct": 1,
         "expl": "The same closing phrase repeated across all five observations."},
        {"q": "What is the first of the five outcomes named?",
         "opts": [
             "Food eaten ends up as excrement and urine",
             "Fame leads to happiness",
             "Wealth guarantees security",
             "Popularity ensures a good rebirth"],
         "correct": 0,
         "expl": "A plain, unflattering observation about ordinary bodily process."},
        {"q": "What does meditating on ugliness stabilize, according to the fourth outcome?",
         "opts": [
             "Attraction to beauty",
             "Revulsion at the feature of beauty",
             "Indifference to all sensation",
             "Physical health"],
         "correct": 1,
         "expl": "One of two meditation-based outcomes closing the discourse."},
        {"q": "Are any of these five outcomes offered as comforting?",
         "opts": [
             "Yes, all five are framed as reassuring",
             "No — the guide reads them as plain facts, stated without comfort",
             "Only the first is comforting",
             "The discourse explicitly calls them comforting"],
         "correct": 1,
         "expl": "Consistent with the discourse's overall unguarded tone."},
        {"q": "What closes this discourse besides its own content?",
         "opts": [
             "Nothing further",
             "The chapter's own colophon, Pañcaṅgikavaggo tatiyo, and its untranslated uddāna verse",
             "A quiz about an unrelated topic",
             "A repeat of AN 5.21's ladder"],
         "correct": 1,
         "expl": "Matching the structure already explained in full at AN 5.10 and AN 5.20."},
    ],
    marginalia=[
        ("The scene", [
            "a crowd, mistaken",
            "for fishermen &mdash;",
            "food, meant for the Buddha",
        ]),
        ("Refused, twice", [
            "&ldquo;may I never",
            "become famous&rdquo;",
            "&mdash; filthy, lazy pleasure",
        ]),
        ("Five outcomes", [
            "food &rarr; excrement",
            "loss &rarr; grief",
            "ugliness meditated &rarr; revulsion",
            "impermanence seen &rarr; revulsion",
        ]),
        ("Cross-references", [
            "AN 5.9&ndash;10, 5.20 &middot; the colophon form",
            "AN 5.23 &middot; another close look at desire",
            "AN 5.31 &middot; next: With Sumanā",
        ]),
    ],
    further=[
        '<a href="%s/an5.30/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.29.html">AN 5.29 &middot; Walking Meditation</a> &mdash; the previous '
        "discourse, this chapter's most purely practical page by contrast.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; where this same '
        "chapter-closing colophon structure was first explained in full.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; earlier in this chapter, '
        "another close look at what desire does to the mind.",
    ],
)


VAGGA_4 = "<em>Sumanavagga</em> &mdash; the fourth chapter of the Fives"


# --------------------------------------------------------------------------- #
# AN 5.31 — Sumanasutta
# --------------------------------------------------------------------------- #
page(
    31, "Sumanā", "With Sumanā",
    vagga=VAGGA_4,
    meta_title="AN 5.31 — With Sumanā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sumanasutta, opening a "
        "new chapter on giving — a princess asks whether an equally faithful, ethical, and wise "
        "giver and non-giver differ as gods, as humans, as renunciates, and as the freed. Three "
        "times yes; once, no difference at all. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery; stated at the head of "
                    "AN 5.31"),
        ("Speakers", "Princess Sumanā, questioning the Buddha"),
        ("Form", "Four rounds of the same question at rising stages of attainment, three answered "
                 "with a five-item difference, the fourth answered with none"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The claim that giving shapes worldly flourishing but not "
                              "liberation itself is a recurring theme across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; opens a new chapter with a "
                       "genuinely pointed question, asked four times in a row"),
    ],
    why=(
        "This chapter turns from monastic cultivation to giving, and opens with a question sharp "
        "enough to carry the whole shift: take two disciples equal in faith, ethics, and wisdom, "
        "one a giver and one not. Does giving make any difference? Three times the Buddha says "
        "yes, naming five respects each time. The fourth time &mdash; once both have become "
        "arahants &mdash; he says there is no difference at all between the freedom of one and "
        "the freedom of the other. Giving matters enormously, and it matters for nothing, "
        "depending entirely on what is being asked."),
    guide=[
        ("The teaching in one sentence", [
            "A giver surpasses an equally faithful, ethical, and wise non-giver in five respects "
            "&mdash; as a god, as a human, and as a renunciate &mdash; but once both attain "
            "freedom, there is no difference between them at all."]),
        ("Three victories, one erasure", [
            "As gods and as humans, the giver's five-item advantage is identical both times: "
            "lifespan, beauty, happiness, glory, and sovereignty. As renunciates, the advantage "
            "shifts to something more concrete &mdash; using requisites mostly when invited to, "
            "and being treated agreeably by fellow practitioners. Then, asked a fourth time about "
            "arahantship, the Buddha does not name five respects at all; he says there is "
            "<em>no difference</em>, <em>yadidaṁ vimuttiyā vimuttiṁ</em>, between the freedom of "
            "one and the freedom of the other. The pattern that repeated three times is broken on "
            "the fourth, and the break is the point."]),
        ("What this does not say about giving", [
            "It would be easy to hear this discourse as diminishing giving, since its worldly "
            "advantages vanish at the finish line. Sumanā's own reaction rules that reading out: "
            "she calls the teaching <em>incredible</em> and <em>amazing</em>, and says it is "
            "<em>quite enough to justify giving gifts and making merit</em>, precisely because "
            "merit helps a person at every stage &mdash; as a god, a human, and a renunciate "
            "&mdash; even though it stops mattering at the very last one."]),
        ("A princess, and a genuinely probing question", [
            "Sumanā is not a passive recipient of teaching here; she asks the same sharpened "
            "question four times in a row, pressing forward past each answer to the next stage of "
            "attainment, until she reaches the one stage where the pattern finally breaks. The "
            "discourse's structure is her structure, not a list the Buddha volunteers unprompted."]),
    ],
    terms=[
        ("dāyako adāyako",
         "&ldquo;giver, non-giver&rdquo; &mdash; the single variable this discourse isolates, "
         "holding faith, ethics, and wisdom equal between the two."),
        ("ādhipateyya",
         "&ldquo;sovereignty&rdquo; &mdash; the fifth item in the giver's advantage as a god or "
         "human, naming a degree of control over one's own circumstances."),
        ("yācitova",
         "&ldquo;only when invited&rdquo; &mdash; the renunciate giver's distinctive advantage, "
         "rarely needing to ask for requisites without being offered them first."),
        ("vimuttiyā vimuttiṁ",
         "&ldquo;the freedom of one, the freedom of the other&rdquo; &mdash; the phrase marking "
         "the point where the discourse's pattern of difference breaks entirely."),
        ("acchariyaṁ abbhutaṁ",
         "&ldquo;incredible, amazing&rdquo; &mdash; Sumanā's own reaction, marking the teaching's "
         "force rather than the guide's own commentary."),
    ],
    text_intro=(
        "The discourse in full: Sumanā's question and the Buddha's four answers, closing with "
        "verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sumanā's question"),
        ("p", "&sect;1", "an5.31:1.1-1.2"),
        ("p", "&sect;2", "an5.31:2.1-2.4"),
        ("h3", "As gods"),
        ("p", "&sect;3", "an5.31:3.1"),
        ("p", "&sect;4", "an5.31:3.2-3.4"),
        ("h3", "As humans"),
        ("p", "&sect;5", "an5.31:4.1"),
        ("p", "&sect;6", "an5.31:4.2"),
        ("p", "&sect;7", "an5.31:4.3-4.5"),
        ("h3", "As renunciates"),
        ("p", "&sect;8", "an5.31:5.1"),
        ("p", "&sect;9", "an5.31:5.2"),
        ("p", "&sect;10", "an5.31:5.3-5.6"),
        ("h3", "As the freed"),
        ("p", "&sect;11", "an5.31:6.1"),
        ("p", "&sect;12", "an5.31:6.2"),
        ("h3", "Sumanā's response"),
        ("p", "&sect;13", "an5.31:7.1-7.3"),
        ("p", "&sect;14", "an5.31:7.4-7.6"),
    ],
    quiz=[
        {"q": "What single variable does Sumanā's question isolate between the two disciples?",
         "opts": [
             "Their level of ordination",
             "Whether one is a giver and one is not, with faith, ethics, and wisdom held equal",
             "Their gender",
             "Their family wealth"],
         "correct": 1,
         "expl": "Everything else is deliberately equalized to isolate the effect of giving alone."},
        {"q": "What five respects does the giver surpass the non-giver in, as a god or as a human?",
         "opts": [
             "Faith, ethics, wisdom, freedom, and knowledge of freedom",
             "Lifespan, beauty, happiness, glory, and sovereignty",
             "Strength, courage, wisdom, patience, and generosity",
             "Nothing; there is no difference at either stage"],
         "correct": 1,
         "expl": "The identical five-item advantage at both the divine and human stages."},
        {"q": "What happens when Sumanā asks the same question a fourth time, about arahantship?",
         "opts": [
             "The Buddha names five respects again, unchanged",
             "The Buddha says there is no difference at all between the freedom of one and the "
             "freedom of the other",
             "The Buddha refuses to answer",
             "The giver is said to surpass the non-giver even more dramatically"],
         "correct": 1,
         "expl": "The three-times-repeated pattern breaks precisely at the final stage."},
        {"q": "How does Sumanā herself react to this teaching?",
         "opts": [
             "With disappointment that giving stops mattering",
             "She calls it incredible and amazing, saying it is quite enough to justify giving "
             "gifts and making merit",
             "She argues the Buddha is wrong",
             "She asks no further questions and leaves immediately"],
         "correct": 1,
         "expl": "Her own words rule out reading the teaching as diminishing the value of giving."},
        {"q": "What is the renunciate giver's distinctive advantage, different from the divine and "
              "human versions?",
         "opts": [
             "Longer life as a monastic",
             "Using requisites mostly when invited to, and being treated agreeably by fellow "
             "practitioners",
             "Exemption from monastic rules",
             "Guaranteed enlightenment"],
         "correct": 1,
         "expl": "A more concrete, monastic-specific version of the same underlying advantage."},
        {"q": "Why does merit still matter, according to Sumanā's own conclusion, even though it "
              "makes no difference at the final stage?",
         "opts": [
             "It doesn't matter at all, on her reading",
             "Because merit helps a person at every stage before that — as a god, a human, and a "
             "renunciate",
             "Because merit is required to attain arahantship at all",
             "Because merit determines one's gender in the next life"],
         "correct": 1,
         "expl": "Value at every intermediate stage, even where it stops mattering at the end."},
        {"q": "Who drives the structure of this discourse — asking the same sharpened question "
              "four times?",
         "opts": [
             "The Buddha, unprompted",
             "Princess Sumanā, pressing the question forward stage by stage",
             "A group of monks debating each other",
             "The discourse has no clear questioner"],
         "correct": 1,
         "expl": "Her own probing structures the whole teaching."},
        {"q": "What does 'vimuttiyā vimuttiṁ' mark?",
         "opts": [
             "A comparison between two types of freedom",
             "The exact point where the discourse's pattern of five-item difference breaks entirely",
             "A description of physical freedom from illness",
             "A term for monastic ordination"],
         "correct": 1,
         "expl": "'The freedom of one, the freedom of the other' — no difference stated."},
        {"q": "How many times, in total, does Sumanā ask her question?",
         "opts": ["Once", "Twice", "Three times", "Four times"],
         "correct": 3,
         "expl": "Divine, human, renunciate, and finally arahant — four rounds."},
        {"q": "What chapter does this discourse open, and what topic does it shift toward?",
         "opts": [
             "The Sekhabalavagga, continuing the powers of a trainee",
             "The Sumanavagga, shifting from monastic cultivation toward giving",
             "The Balavagga, continuing the standard powers",
             "A return to the Pañcaṅgikavagga's material"],
         "correct": 1,
         "expl": "A thematic pivot for the whole chapter, not just this one discourse."},
    ],
    marginalia=[
        ("Four rounds", [
            "as gods: 5 respects",
            "as humans: 5 respects",
            "as renunciates: 5 respects",
            "as the freed: none",
        ]),
        ("The break", [
            "<span class=\"pali\">vimuttiyā vimuttiṁ</span>",
            "&mdash; no difference,",
            "for the first time",
        ]),
        ("Sumanā's own verdict", [
            "&ldquo;incredible, amazing&rdquo;",
            "&mdash; reason enough",
            "to give, still",
        ]),
        ("Cross-references", [
            "AN 5.1&ndash;30 &middot; the chapters before",
            "AN 5.32 &middot; next: With Cundī",
            "AN 5.35 &middot; later: giving's benefits, generalized",
        ]),
    ],
    further=[
        '<a href="%s/an5.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.30.html">AN 5.30 &middot; With Nāgita</a> &mdash; the previous chapter’s '
        "closing discourse, on the dangers of fame rather than the benefits of giving.",
        '<a href="an-5.32.html">AN 5.32 &middot; With Cundī</a> &mdash; next, another royal '
        "questioner, on where confidence is best placed.",
        '<a href="an-5.35.html">AN 5.35 &middot; The Benefits of Giving</a> &mdash; later in this '
        "chapter, the general five benefits without Sumanā&rsquo;s four-stage structure.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.32 — Cundīsutta
# --------------------------------------------------------------------------- #
page(
    32, "Cundī", "With Cundī",
    vagga=VAGGA_4,
    meta_title="AN 5.32 — With Cundī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Cundīsutta — a princess "
        "relays her brother's formula for good rebirth, and the Buddha reframes it around "
        "confidence in the best: the best being, the best path, the best cessation, the best "
        "community, the best ethics. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, in the Bamboo Grove, the squirrels' feeding ground; stated at the "
                    "head of AN 5.32"),
        ("Speakers", "Princess Cundī, relaying her brother Prince Cunda's question, and the "
                     "Buddha"),
        ("Form", "A relayed question, then five parallel declarations that a specific thing is "
                 "&lsquo;the best&rsquo;, each with the same two-step consequence"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Ranking the Three Refuges and ethics as supreme fields of merit is "
                              "a standard formula across the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a formula repeated five times "
                       "with only its object changing"),
    ],
    why=(
        "Cundī does not ask her own question; she relays her brother Cunda's formula &mdash; refuge "
        "in the Three Jewels plus the five precepts guarantees good rebirth &mdash; and asks the "
        "Buddha what kind of teacher, teaching, community, and ethics deserve that confidence. The "
        "Buddha does not simply confirm Cunda's formula. He answers with a different structure "
        "entirely: five things named <em>the best</em> of their kind, each producing, by a fixed "
        "two-step logic, the best possible result."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha, the noble eightfold path, fading away, the Saṅgha, and the ethics loved "
            "by the noble ones are each named the best of their kind, and confidence in the best "
            "produces the best result."]),
        ("A reframe, not a confirmation", [
            "Cunda's formula, as Cundī relays it, is refuge in the Three Jewels plus the five "
            "precepts. The Buddha's answer covers overlapping ground &mdash; the Buddha, the "
            "teaching, the Saṅgha, and ethics all appear &mdash; but organized around a different "
            "logic: not a checklist to complete, but a claim about superlatives. Fading away, "
            "<em>virāga</em>, is added as a fifth item with no equivalent in Cunda's original "
            "formula at all."]),
        ("The same two-step logic, five times", [
            "Each of the five follows an identical pattern: this is said to be the best of its "
            "category; those with confidence in it have confidence in the best; and confidence in "
            "the best produces the best result. The pattern is not varied once across all five "
            "applications, which makes the discourse function almost as a template a reader could "
            "apply to any claim about supreme worth, not only these five specific ones."]),
        ("Fading away, defined at length", [
            "Of the five, only <em>virāga</em>, fading away, receives an extended definition: the "
            "quelling of vanity, the removing of thirst, the uprooting of clinging, the breaking "
            "of the round, the ending of craving, fading away, cessation, extinguishment. Eight "
            "terms stacked together for what is otherwise a one-word claim elsewhere in the "
            "discourse, marking this item as needing the most unpacking of the five."]),
        ("What the ethics named here specify", [
            "The &lsquo;ethics loved by the noble ones&rsquo; are given their own eightfold "
            "description &mdash; intact, impeccable, spotless, unmarred, liberating, praised by "
            "sensible people, not mistaken, and leading to immersion &mdash; distinguishing this "
            "as a specific quality of ethical conduct rather than simply the five precepts Cunda "
            "named. Not every observance of the five precepts, on this account, automatically "
            "counts as the ethics being praised here."]),
    ],
    terms=[
        ("aggamakkhāyati",
         "&ldquo;is said to be the best&rdquo; &mdash; the fixed phrase opening each of the five "
         "declarations in this discourse."),
        ("virāga",
         "&ldquo;fading away&rdquo; &mdash; the one item given an extended, eight-term "
         "definition, distinct from the four others named only briefly."),
        ("ariyakanta sīla",
         "&ldquo;ethics loved by the noble ones&rdquo; &mdash; a specific quality of conduct, "
         "distinguished here from simply keeping the five precepts."),
        ("puññakkhetta",
         "&ldquo;field of merit&rdquo; &mdash; the description given to the Saṅgha, the same "
         "image used elsewhere in this series for what returns the greatest karmic fruit."),
        ("aggo vipāko",
         "&ldquo;the best result&rdquo; &mdash; the fixed consequence closing each of the five "
         "declarations, following automatically from confidence in the best."),
    ],
    text_intro=(
        "The discourse in full: Cundī's relayed question, and the Buddha's five declarations of "
        "what is best, closing with verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Cundī relays her brother's question"),
        ("p", "&sect;1", "an5.32:1.1-1.2"),
        ("p", "&sect;2", "an5.32:2.1-2.7"),
        ("h3", "The best of beings"),
        ("p", "&sect;3", "an5.32:3.1-3.3"),
        ("h3", "The best of conditioned things"),
        ("p", "&sect;4", "an5.32:4.1-4.2"),
        ("h3", "The best of all things"),
        ("p", "&sect;5", "an5.32:5.1-5.4"),
        ("h3", "The best of communities"),
        ("p", "&sect;6", "an5.32:6.1-6.4"),
        ("h3", "The best of ethics"),
        ("p", "&sect;7", "an5.32:7.1-7.4"),
    ],
    quiz=[
        {"q": "What formula does Cundī relay from her brother Cunda?",
         "opts": [
             "The five powers of a trainee",
             "Refuge in the Three Jewels plus the five precepts guarantees good rebirth",
             "Walking meditation's five benefits",
             "The four noble truths"],
         "correct": 1,
         "expl": "Cundī does not ask her own question; she relays her brother's claim and asks for confirmation."},
        {"q": "Does the Buddha simply confirm Cunda's formula?",
         "opts": [
             "Yes, word for word",
             "No — he reframes the answer around five things named 'the best', with a different "
             "underlying logic",
             "He rejects the formula entirely",
             "He refuses to answer"],
         "correct": 1,
         "expl": "Overlapping ground, organized around superlatives rather than a checklist."},
        {"q": "What two-step logic repeats identically across all five declarations?",
         "opts": [
             "A different logic each time",
             "This is the best of its category; confidence in the best produces the best result",
             "A warning followed by a blessing",
             "A question followed by silence"],
         "correct": 1,
         "expl": "An unvarying template applied to five different superlatives."},
        {"q": "Which of the five items receives an extended, eight-term definition, unlike the "
              "other four?",
         "opts": [
             "The Buddha", "The Saṅgha", "Virāga, fading away", "The noble eightfold path"],
         "correct": 2,
         "expl": "Quelling vanity, removing thirst, uprooting clinging, and more — needing the most unpacking."},
        {"q": "How does the 'ethics loved by the noble ones' compare to simply keeping the five "
              "precepts, according to the guide?",
         "opts": [
             "They are identical, with no distinction",
             "They are a specific quality of conduct — intact, impeccable, spotless, and more — "
             "not automatically the same as observing the five precepts",
             "They apply only to monastics, never laypeople",
             "They replace the five precepts entirely"],
         "correct": 1,
         "expl": "Not every observance of the precepts automatically counts as this specific praised ethics."},
        {"q": "What item does the Buddha add that has no equivalent in Cunda's original formula?",
         "opts": [
             "The Saṅgha", "Virāga, fading away", "The five precepts", "Refuge itself"],
         "correct": 1,
         "expl": "A fifth item introduced beyond what Cundī relayed."},
        {"q": "What is the Saṅgha described as, in this discourse?",
         "opts": [
             "A political organization",
             "The supreme field of merit for the world",
             "A group with no special status",
             "Identical to the general population"],
         "correct": 1,
         "expl": "Puññakkhetta, the same image used elsewhere in this series."},
        {"q": "Is Cundī herself the one asking a spontaneous question, or relaying someone else's?",
         "opts": [
             "She asks her own original question",
             "She relays her brother Prince Cunda's formula and question",
             "She relays a question from an unnamed ascetic",
             "The discourse does not specify who is asking"],
         "correct": 1,
         "expl": "The discourse opens with an explicitly secondhand question."},
        {"q": "How many times does the 'is said to be the best' phrase (aggamakkhāyati) appear "
              "across the discourse's five declarations?",
         "opts": ["Once", "Twice", "Five times, once per declaration", "Ten times"],
         "correct": 2,
         "expl": "The fixed opening phrase for each of the five parallel claims."},
        {"q": "Where is AN 5.32 set?",
         "opts": [
             "Sāvatthī, continuing from AN 5.31",
             "Rājagaha, in the Bamboo Grove, the squirrels' feeding ground",
             "Vesālī, at the Great Wood",
             "Bhaddiya, in Jātiyā Wood"],
         "correct": 1,
         "expl": "A new, explicitly stated setting distinct from AN 5.31's."},
    ],
    marginalia=[
        ("Five superlatives", [
            "the Buddha &middot; the path",
            "fading away &middot; the Saṅgha",
            "noble ethics",
        ]),
        ("One template, five times", [
            "&ldquo;said to be the best&rdquo;",
            "&rarr; confidence in the best",
            "&rarr; the best result",
        ]),
        ("Unpacked at length", [
            "<span class=\"pali\">virāga</span>fading away",
            "&mdash; 8 terms, not just 1",
        ]),
        ("Cross-references", [
            "AN 5.31 &middot; the chapter's opener",
            "AN 5.38 &middot; later: faith's own benefits",
            "AN 5.33 &middot; next: With Uggaha",
        ]),
    ],
    further=[
        '<a href="%s/an5.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.31.html">AN 5.31 &middot; With Sumanā</a> &mdash; the previous discourse, '
        "another royal questioner opening this chapter.",
        '<a href="an-5.33.html">AN 5.33 &middot; With Uggaha</a> &mdash; next, a very different '
        "kind of instruction, addressed to daughters leaving for marriage.",
        '<a href="an-5.38.html">AN 5.38 &middot; Faith</a> &mdash; later in this chapter, on the '
        "benefits confidence itself brings to the one who has it.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.33 — Uggahasutta
# --------------------------------------------------------------------------- #
page(
    33, "Uggaha", "With Uggaha",
    vagga=VAGGA_4,
    meta_title="AN 5.33 — With Uggaha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Uggahasutta — a father "
        "asks the Buddha to instruct his daughters before their marriages, and receives five "
        "qualities framed entirely around service to a husband and his household. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Bhaddiya, in Jātiyā Wood; the instruction itself given the next day at "
                    "Uggaha's home"),
        ("Speakers", "Uggaha, grandson of Meṇḍaka, requesting instruction; the Buddha, addressing "
                     "Uggaha's daughters directly"),
        ("Form", "A meal offered and accepted, a father's request, and five qualities given "
                 "directly to the daughters in second person"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Instructions to a bride framed around household duty and deference "
                              "to a husband's family recur in Chinese Buddhist lay-ethics "
                              "literature; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the chapter's most "
                       "historically specific and least comfortable discourse for a modern reader"),
    ],
    why=(
        "This reading guide states plainly what this discourse contains, without softening it: "
        "five qualities given to young women on the eve of marriage, all of them organized around "
        "service &mdash; rising before their husband, deferring to whoever he respects, managing "
        "his household competently, and guarding his wealth. It is addressed to the specific "
        "social position of a bride entering her husband's family in ancient Indian society, and "
        "it reflects that position's norms rather than transcending them. The discourse is "
        "included here in full because the collection includes it, not because this reading guide "
        "endorses the norms it assumes."),
    guide=[
        ("The teaching in one sentence", [
            "Asked by their father to instruct his daughters before their marriages, the Buddha "
            "gives five qualities: deference and diligence toward the husband, respect for those "
            "he respects, competent and tireless household work, careful oversight of the "
            "domestic staff, and guarding the family's wealth."]),
        ("What the discourse actually asks of these women", [
            "Read closely, the five qualities are consistently outward-facing: getting up before "
            "the husband and retiring after him, honoring whoever he honors, being deft at "
            "domestic crafts, knowing the condition of every servant and worker in the household, "
            "and protecting money, grain, silver, or gold from waste or loss. Nothing in the five "
            "qualities concerns the women's own inner cultivation &mdash; no faith, no ethics "
            "practiced for their own sake, no meditation. The entire instruction is framed around "
            "competent, deferential management of someone else's household."]),
        ("A specific social position, not a universal teaching", [
            "This discourse is not addressed to women in general, or to laywomen as a class "
            "&mdash; other discourses in this collection address laywomen's own spiritual "
            "practice directly, in terms of faith, ethics, and wisdom rather than household "
            "management. This one is addressed to daughters at the specific moment of leaving "
            "their birth family for their husband's, and its content reflects what a father in "
            "that society wanted his daughters equipped with for that transition. Reading it as a "
            "timeless statement about women's proper role, rather than as historically specific "
            "advice for a specific social position, misreads what the text is doing."]),
        ("Where the reward is placed", [
            "Fulfilling these five qualities is said to lead to rebirth <em>manāpakāyikānaṁ "
            "devānaṁ sahabyataṁ</em>, in company with the Gods of the Agreeable Host &mdash; not "
            "the fuller, higher framework of stream-entry or freedom the discourse's own chapter "
            "opened with at AN 5.31. The reward offered here is modest and this-worldly, matching "
            "the modest and this-worldly scope of the instruction itself."]),
        ("Reading this discourse honestly", [
            "A teaching guide serving a mixed audience today does not need to defend this "
            "discourse's content, and does not need to pretend it is absent from the canon "
            "either. It is here, addressed to a real father's real request, reflecting norms this "
            "reading guide does not share and will not launder. What can be said honestly is that "
            "the collection preserves it as historical record of what one society, at one moment, "
            "asked of its young brides &mdash; not as this series' own statement of what any "
            "person, of any gender, owes anyone else."]),
    ],
    terms=[
        ("pubbuṭṭhāyī pacchānipātī",
         "&ldquo;rising before, retiring after&rdquo; &mdash; the discourse&rsquo;s summary phrase "
         "for the first quality, deference measured in literal waking hours."),
        ("dakkhā analasā",
         "&ldquo;deft and tireless&rdquo; &mdash; the description given to the third quality, "
         "domestic competence at spinning and sewing."),
        ("antojana",
         "&ldquo;household members, domestic staff&rdquo; &mdash; the servants and workers a wife "
         "is instructed to monitor and fairly provision under the fourth quality."),
        ("manāpakāyikā devā",
         "&ldquo;Gods of the Agreeable Host&rdquo; &mdash; the modest heavenly destination named "
         "as this discourse's reward, distinct from stream-entry or freedom."),
        ("meṇḍakanattā",
         "&ldquo;grandson of Meṇḍaka&rdquo; &mdash; Uggaha's identifying epithet, naming a "
         "wealthy, well-known family this discourse assumes without further explanation."),
    ],
    text_intro=(
        "The discourse in full: Uggaha's invitation and request, and the five qualities the "
        "Buddha addresses directly to his daughters. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "An invitation to a meal"),
        ("p", "&sect;1", "an5.33:1.1"),
        ("p", "&sect;2", "an5.33:1.2-2.3"),
        ("h3", "A father's request"),
        ("p", "&sect;3", "an5.33:3.1-3.2"),
        ("p", "&sect;4", "an5.33:3.3-3.7"),
        ("h3", "Five qualities, addressed to the daughters"),
        ("p", "&sect;5", "an5.33:4.1"),
        ("p", "&sect;6", "an5.33:4.2-4.4"),
        ("p", "&sect;7", "an5.33:5.1-5.3"),
        ("p", "&sect;8", "an5.33:6.1-6.3"),
        ("p", "&sect;9", "an5.33:7.1-7.3"),
        ("p", "&sect;10", "an5.33:8.1-8.4"),
    ],
    quiz=[
        {"q": "What does Uggaha ask the Buddha to do for his daughters?",
         "opts": [
             "Teach them to read and write",
             "Instruct and advise them, since they are about to leave for their husbands' families",
             "Ordain them as nuns",
             "Arrange their marriages personally"],
         "correct": 1,
         "expl": "A father's request at a specific transitional moment in his daughters' lives."},
        {"q": "What do the five qualities the Buddha names have in common, according to the guide?",
         "opts": [
             "They all concern the women's own inner spiritual cultivation",
             "They are consistently outward-facing, organized around service and management of "
             "someone else's household",
             "They concern only physical health",
             "They are identical to the five powers of a trainee"],
         "correct": 1,
         "expl": "No faith, ethics, or meditation practiced for its own sake appears among the five."},
        {"q": "How does the guide characterize this discourse's audience?",
         "opts": [
             "A universal teaching addressed to all women for all time",
             "A historically specific instruction addressed to daughters at the moment of leaving "
             "for their husband's family, not a timeless statement about women's role",
             "Addressed to monks exclusively",
             "Addressed to kings and rulers"],
         "correct": 1,
         "expl": "The guide explicitly cautions against reading this as a universal or timeless teaching."},
        {"q": "What reward does the discourse attach to fulfilling these five qualities?",
         "opts": [
             "Stream-entry",
             "Rebirth among the Gods of the Agreeable Host — a modest, this-worldly destination",
             "Full liberation, as at AN 5.31's fourth stage",
             "No reward is mentioned"],
         "correct": 1,
         "expl": "Matching the modest, this-worldly scope of the instruction itself."},
        {"q": "Does this reading guide defend or endorse the content of this discourse?",
         "opts": [
             "Yes, presenting it as an ideal to aspire to",
             "No — it states plainly what the discourse contains and does not launder norms it "
             "does not share",
             "It refuses to discuss the discourse's content at all",
             "It claims the discourse was added by a later, unreliable editor"],
         "correct": 1,
         "expl": "Presented as historical record, stated honestly rather than defended or hidden."},
        {"q": "What is the first of the five qualities, in summary?",
         "opts": [
             "Deference measured in waking hours — rising before the husband, retiring after him",
             "Meditative attainment",
             "Physical strength",
             "Literacy and education"],
         "correct": 0,
         "expl": "Pubbuṭṭhāyī pacchānipātī, the discourse's own summary phrase."},
        {"q": "What does the fourth quality involve?",
         "opts": [
             "Managing personal finances only",
             "Knowing the condition of every servant and worker in the household, and fairly "
             "distributing food",
             "Public speaking",
             "Religious study"],
         "correct": 1,
         "expl": "Oversight of the antojana, the household's domestic staff."},
        {"q": "Does the discourse's chapter otherwise address laywomen's own spiritual practice "
              "directly?",
         "opts": [
             "No, this collection never addresses women's spiritual practice",
             "The guide notes other discourses in this collection address laywomen's faith, "
             "ethics, and wisdom directly, in different terms than this one",
             "Only this discourse ever mentions women at all",
             "The question is not addressed"],
         "correct": 1,
         "expl": "This discourse is distinguished from that broader pattern, not treated as representative of it."},
        {"q": "What does the fifth quality concern?",
         "opts": [
             "Guarding the family's wealth from waste, theft, or loss",
             "Public religious ceremony",
             "Physical training",
             "Formal education of children"],
         "correct": 0,
         "expl": "Protection of money, grain, silver, or gold earned by the husband."},
        {"q": "Where does the instruction itself take place?",
         "opts": [
             "In the forest at Jātiyā Wood, where the Buddha was staying",
             "At Uggaha's own home, after a meal the Buddha accepted the previous day",
             "At the royal palace",
             "In a public assembly hall"],
         "correct": 1,
         "expl": "A private setting, following the standard meal-invitation sequence."},
    ],
    marginalia=[
        ("Five qualities", [
            "deference in hours kept",
            "respect for his kin",
            "domestic competence",
            "oversight of staff",
            "guarding the wealth",
        ]),
        ("What is absent", [
            "no faith, ethics, or",
            "meditation named",
            "for its own sake",
        ]),
        ("A specific audience", [
            "not laywomen generally &mdash;",
            "daughters, at the moment",
            "of leaving for marriage",
        ]),
        ("Cross-references", [
            "AN 5.31 &middot; freedom, without difference",
            "AN 5.32 &middot; next-of-kin, With Cundī",
            "AN 5.34 &middot; next: With General Sīha",
        ]),
    ],
    further=[
        '<a href="%s/an5.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.32.html">AN 5.32 &middot; With Cundī</a> &mdash; the previous discourse, a '
        "very different kind of instruction given to a different royal family.",
        '<a href="an-5.34.html">AN 5.34 &middot; With General Sīha</a> &mdash; next, a return to '
        "this chapter's central theme of giving.",
        '<a href="an-5.31.html">AN 5.31 &middot; With Sumanā</a> &mdash; where this chapter '
        "opened on freedom making no distinction at all between the freed.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.34 — Sīhasenāpatisutta
# --------------------------------------------------------------------------- #
page(
    34, "Sīhasenāpati", "With General Sīha",
    vagga=VAGGA_4,
    meta_title="AN 5.34 — With General Sīha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sīhasenāpatisutta — a "
        "general asks for a fruit of giving visible in this life, and then tells the Buddha which "
        "of the five he can verify himself and which one he must take on faith. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with the peaked roof; stated at the "
                    "head of AN 5.34"),
        ("Speakers", "General Sīha, questioning the Buddha"),
        ("Form", "A question about visible fruit, five named fruits split four-and-one, and the "
                 "questioner's own verification of exactly which four"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Distinguishing empirically verifiable from faith-based claims "
                              "within a single teaching recurs across the Chinese Āgamas' "
                              "treatment of giving; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a genuinely interesting moment "
                       "of the canon marking its own epistemic boundary"),
    ],
    why=(
        "General Sīha asks a pointed question: can you point to a fruit of giving apparent in "
        "<em>this very life</em>, not just the next one? The Buddha answers with five fruits, and "
        "then something unusual happens. Sīha, in his own words, sorts the five into two "
        "categories: four he says he already knows personally, requiring no faith in the Buddha "
        "at all, and one &mdash; heavenly rebirth &mdash; which he explicitly says he does not "
        "know, and must take on faith. The discourse marks its own epistemic boundary, in the "
        "questioner's own voice."),
    guide=[
        ("The teaching in one sentence", [
            "A giver is loved by many, is associated with by good people, gains a good "
            "reputation, and enters any assembly with confidence &mdash; four fruits apparent in "
            "this very life &mdash; and is reborn in a heavenly realm after death, a fifth fruit "
            "concerning lives to come."]),
        ("A distinction the text draws explicitly", [
            "The Buddha's own answer already separates the fruits into two categories, marked "
            "by different Pāli terms: <em>sandiṭṭhika</em>, apparent in this very life, for the "
            "first four, and <em>samparāyika</em>, concerning lives to come, for the fifth. This "
            "is not a distinction this reading guide is imposing on the text; the discourse makes "
            "it before Sīha ever responds."]),
        ("Sīha's own epistemology", [
            "What makes this discourse distinctive is what Sīha does with that distinction. He "
            "restates all five fruits back to the Buddha in the first person &mdash; <em>I am a "
            "giver, and I am dear and beloved to many people</em> &mdash; for the first four, "
            "explicitly saying <em>I don't rely on faith in the Buddha, for I know them too</em>. "
            "For the fifth, heavenly rebirth, he says the opposite just as explicitly: "
            "<em>this I don't know, so I have to rely on faith in the Buddha</em>. A listener is "
            "shown, in real time, someone distinguishing what they can verify from what they "
            "cannot."]),
        ("The Buddha's response to being told this", [
            "The Buddha does not correct Sīha's self-assessment or insist the fourth-and-fifth "
            "distinction should be collapsed. He responds, <em>that's so true, Sīha! That's so "
            "true!</em>, and simply restates the fifth fruit once more. The discourse lets Sīha's "
            "distinction between verified and trusted claims stand without dissolving it into a "
            "single undifferentiated category of belief."]),
        ("What this means for how the whole nipāta should be read", [
            "Not every claim in this chapter, or in this series, carries the same epistemic "
            "weight, and this discourse is the clearest place in the Fives so far where the "
            "canon itself makes that explicit. A reader working through discourses about heavenly "
            "rebirths and cosmic consequences can recall this page: even a devoted questioner "
            "like Sīha treats some claims as personally checkable and others as resting on trust "
            "in the teacher, and the text does not blur that line."]),
    ],
    terms=[
        ("sandiṭṭhika",
         "&ldquo;apparent in this very life&rdquo; &mdash; the term marking the first four fruits "
         "as personally verifiable, not requiring faith."),
        ("samparāyika",
         "&ldquo;concerning lives to come&rdquo; &mdash; the term marking the fifth fruit, "
         "heavenly rebirth, as belonging to a different epistemic category."),
        ("saddhāya gacchāmi",
         "&ldquo;I go by faith&rdquo; &mdash; Sīha&rsquo;s own phrase for what he does with the "
         "one claim he says he cannot personally verify."),
        ("visārado amaṅkubhūto",
         "&ldquo;bold and self-assured&rdquo; &mdash; the fourth visible fruit, entering any "
         "assembly without hesitation."),
        ("dāyako dānapati",
         "&ldquo;a giver, a donor&rdquo; &mdash; the fixed pairing used throughout this discourse "
         "for the person whose fruits are being described."),
    ],
    text_intro=(
        "The discourse in full: Sīha's question, the Buddha's five fruits, and Sīha's own "
        "division of them into what he knows and what he takes on faith. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A fruit visible in this life"),
        ("p", "&sect;1", "an5.34:1.1"),
        ("p", "&sect;2", "an5.34:1.2-1.3"),
        ("h3", "Five fruits of giving"),
        ("p", "&sect;3", "an5.34:2.1"),
        ("p", "&sect;4", "an5.34:2.2-2.3"),
        ("p", "&sect;5", "an5.34:3.1-3.2"),
        ("p", "&sect;6", "an5.34:4.1-4.2"),
        ("p", "&sect;7", "an5.34:5.1-5.2"),
        ("p", "&sect;8", "an5.34:6.1-6.2"),
        ("h3", "Sīha's own verification"),
        ("p", "&sect;9", "an5.34:7.1-7.9"),
        ("p", "&sect;10", "an5.34:7.10-7.11"),
    ],
    quiz=[
        {"q": "What question does General Sīha open with?",
         "opts": [
             "Whether giving guarantees enlightenment",
             "Whether the Buddha can point to a fruit of giving apparent in this very life, not "
             "only the next one",
             "How much should be given to be effective",
             "Whether monks may accept gifts at all"],
         "correct": 1,
         "expl": "A pointed request for something checkable now, not only a future promise."},
        {"q": "What two Pāli terms does the discourse itself use to divide the five fruits?",
         "opts": [
             "Sekha and asekha",
             "Sandiṭṭhika, apparent in this life, and samparāyika, concerning lives to come",
             "Saṅkhata and asaṅkhata",
             "Kusala and akusala"],
         "correct": 1,
         "expl": "A distinction the Buddha's own answer draws, before Sīha responds."},
        {"q": "What does Sīha say about the first four fruits?",
         "opts": [
             "He takes them on faith, like the fifth",
             "He says he already knows them personally and doesn't rely on faith in the Buddha for "
             "them",
             "He denies they are true",
             "He asks the Buddha to prove them"],
         "correct": 1,
         "expl": "Restated in the first person, as things he can verify from his own experience."},
        {"q": "What does Sīha say about the fifth fruit, heavenly rebirth?",
         "opts": [
             "He also claims to know it personally",
             "He explicitly says he doesn't know it, and must rely on faith in the Buddha",
             "He rejects the claim outright",
             "He refuses to comment"],
         "correct": 1,
         "expl": "The one fruit Sīha marks as resting on trust rather than personal verification."},
        {"q": "How does the Buddha respond to Sīha's distinction between what he knows and what he "
              "takes on faith?",
         "opts": [
             "He corrects Sīha, insisting all five must be taken on faith",
             "He affirms it — 'that's so true, Sīha!' — and simply restates the fifth fruit",
             "He ignores the distinction entirely",
             "He rebukes Sīha for doubting"],
         "correct": 1,
         "expl": "The distinction is allowed to stand rather than being dissolved."},
        {"q": "What does the guide say this discourse demonstrates about how the whole nipāta "
              "should be read?",
         "opts": [
             "That every claim carries identical epistemic weight",
             "That not every claim carries the same epistemic weight, and the canon itself makes "
             "that distinction explicit here",
             "That nothing in the canon can be personally verified",
             "That faith is unnecessary for any claim"],
         "correct": 1,
         "expl": "A rare moment where the text marks its own boundary between the checkable and the trusted."},
        {"q": "What are the four fruits apparent in this very life?",
         "opts": [
             "Long life, beauty, happiness, and strength",
             "Being loved by many, being associated with by good people, gaining a good "
             "reputation, and entering assemblies with confidence",
             "Wealth, health, family, and reputation",
             "Ethics, immersion, wisdom, and freedom"],
         "correct": 1,
         "expl": "All four are things Sīha says he can check against his own experience."},
        {"q": "What is General Sīha's role or title, as named in the discourse?",
         "opts": [
             "A minister of finance",
             "A general (senāpati)",
             "A physician",
             "A ferryman"],
         "correct": 1,
         "expl": "Named directly in the discourse's own title."},
        {"q": "What form do the discourse's closing verses take?",
         "opts": [
             "A repeat of Sīha's own words",
             "A restatement of the fruits of giving in verse, including images of the Third Heaven "
             "and the Garden of Delight",
             "A warning against giving",
             "A prose summary with no verse at all"],
         "correct": 1,
         "expl": "Verses extending the discourse's claims with additional heavenly imagery."},
        {"q": "Where is AN 5.34 set?",
         "opts": [
             "Sāvatthī",
             "Vesālī, at the Great Wood, in the hall with the peaked roof",
             "Rājagaha",
             "Bhaddiya"],
         "correct": 1,
         "expl": "A new, explicitly stated setting, distinct from the earlier discourses in this chapter."},
    ],
    marginalia=[
        ("Two categories", [
            "<span class=\"pali\">sandiṭṭhika</span>this life &mdash; 4",
            "<span class=\"pali\">samparāyika</span>next life &mdash; 1",
        ]),
        ("Sīha's own words", [
            "&ldquo;I know these four&rdquo;",
            "&ldquo;this one, I take",
            "on faith&rdquo;",
        ]),
        ("Confirmed, not corrected", [
            "&ldquo;that's so true, Sīha!&rdquo;",
            "&mdash; the distinction stands",
        ]),
        ("Cross-references", [
            "AN 5.31 &middot; giving's worldly fruits",
            "AN 5.35 &middot; next: the same fruits, general",
            "AN 5.38 &middot; faith's own five benefits",
        ]),
    ],
    further=[
        '<a href="%s/an5.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.33.html">AN 5.33 &middot; With Uggaha</a> &mdash; the previous discourse, a '
        "very different address to a different audience.",
        '<a href="an-5.35.html">AN 5.35 &middot; The Benefits of Giving</a> &mdash; next, this '
        "same fruit-list generalized beyond a single questioner.",
        '<a href="an-5.31.html">AN 5.31 &middot; With Sumanā</a> &mdash; where this chapter opened '
        "on what giving does, and does not, ultimately change.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.35 — Dānānisaṁsasutta
# --------------------------------------------------------------------------- #
page(
    35, "Dānānisaṁsa", "The Benefits of Giving",
    vagga=VAGGA_4,
    meta_title="AN 5.35 — The Benefits of Giving | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dānānisaṁsasutta — the "
        "five benefits of giving stated generally, swapping AN 5.34's confident public presence "
        "for not neglecting a layperson's ordinary duties. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of five general benefits, closing with verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "General lists of giving's this-life and next-life benefits recur "
                              "across the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, best read against its "
                       "more personal predecessor"),
    ],
    why=(
        "Where AN 5.34 built its five fruits around one general's own verified experience, this "
        "discourse states the same territory as a general teaching to mendicants, with one "
        "substitution worth noticing: in place of confidently entering any assembly, this "
        "discourse names not neglecting the ordinary duties of a layperson. The swap says "
        "something about which quality the collection considers essential to keep, and which "
        "one is negotiable depending on the audience."),
    guide=[
        ("The teaching in one sentence", [
            "A giver is dear and beloved by many people, is associated with by good and true "
            "persons, gains a good reputation, does not neglect a layperson's duties, and is "
            "reborn in a heavenly realm."]),
        ("One item swapped, four kept", [
            "The first three and the fifth benefit here are worded almost identically to AN "
            "5.34's first three and fifth fruits. The fourth is different: "
            "<em>gihidhammā anapagato hoti</em>, they don't neglect a layperson's duties, "
            "replaces AN 5.34's confident, self-assured presence in any assembly. A general like "
            "Sīha might reasonably be praised for public confidence; a general audience of "
            "mendicants addressing lay listeners might instead emphasize not letting generosity "
            "come at the expense of ordinary household obligations."]),
        ("A general teaching, not a personal exchange", [
            "AN 5.34 unfolded as dialogue, with a named questioner testing and confirming each "
            "claim against his own experience. This discourse has no questioner at all; it opens "
            "with the standard <em>mendicants, there are five benefits of giving</em> and states "
            "the list directly, without anyone verifying or challenging any part of it."]),
        ("The closing verse's sharper turn", [
            "The verses closing this discourse move further than AN 5.34's did, ending not simply "
            "with heavenly rebirth but with the Dhamma taught by good companions "
            "<em>casting aside all suffering</em>, so that <em>the undefiled one is fully "
            "extinguished</em>. A discourse that opened on giving's ordinary social and worldly "
            "benefits closes by pointing all the way to full extinguishment, the same movement "
            "AN 5.31 traced explicitly at the start of this chapter."]),
    ],
    terms=[
        ("gihidhammā anapagato",
         "&ldquo;not neglecting a layperson&rsquo;s duties&rdquo; &mdash; this discourse&rsquo;s "
         "substitution for AN 5.34&rsquo;s confident public presence."),
        ("sappurisā",
         "&ldquo;true persons, good people&rdquo; &mdash; the second benefit, matching AN "
         "5.34&rsquo;s wording closely."),
        ("kalyāṇo kittisaddo",
         "&ldquo;a good reputation&rdquo; &mdash; the third benefit, a fixed phrase for renown "
         "used identically across several discourses in this chapter."),
        ("sabbadukkhāpanūdana",
         "&ldquo;casting aside all suffering&rdquo; &mdash; the closing verse&rsquo;s description "
         "of the Dhamma good companions teach."),
        ("parinibbāti anāsavo",
         "&ldquo;the undefiled one is fully extinguished&rdquo; &mdash; the discourse&rsquo;s "
         "final line, reaching well beyond the worldly benefits it opened with."),
    ],
    text_intro=(
        "The discourse in full: the five general benefits of giving, closing with verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.35:1.1-1.8"),
        ("h3", "The closing verses"),
        ("p", "&sect;2", "an5.35:2.1-2.4"),
        ("p", "&sect;3", "an5.35:3.1-3.4"),
    ],
    quiz=[
        {"q": "Which single benefit differs between AN 5.34's list and this discourse's list?",
         "opts": [
             "Being loved by many",
             "Confident public presence, replaced here by not neglecting a layperson's duties",
             "Heavenly rebirth",
             "A good reputation"],
         "correct": 1,
         "expl": "Four items match closely; the fourth is swapped for a different quality."},
        {"q": "Why might this discourse's audience explain the swap, according to the guide?",
         "opts": [
             "No explanation is possible",
             "A general audience of mendicants addressing lay listeners might emphasize not "
             "letting generosity come at the expense of ordinary household duties",
             "The swap is a copying error",
             "The two lists are actually identical, with no swap at all"],
         "correct": 1,
         "expl": "A general like Sīha suits public confidence; a broader lay audience suits a different emphasis."},
        {"q": "How does this discourse's form differ from AN 5.34's?",
         "opts": [
             "Identical dialogue with a named questioner",
             "No questioner at all — a general statement of the list with nothing verified by "
             "anyone",
             "This discourse has no text",
             "It is spoken entirely in verse"],
         "correct": 1,
         "expl": "A direct teaching, not a personal exchange."},
        {"q": "What does the discourse's closing verse ultimately point toward?",
         "opts": [
             "Only worldly wealth",
             "Full extinguishment — 'the undefiled one is fully extinguished' — reached through the "
             "Dhamma taught by good companions",
             "A warning against giving",
             "A return to lay life"],
         "correct": 1,
         "expl": "A movement from ordinary benefit to the furthest goal, echoing AN 5.31's arc."},
        {"q": "What are the five benefits of giving named in this discourse?",
         "opts": [
             "Loved by many, associated with by good people, good reputation, not neglecting lay "
             "duties, and heavenly rebirth",
             "Long life, beauty, happiness, strength, and eloquence",
             "The five powers of a trainee",
             "Faith, ethics, learning, generosity, and wisdom"],
         "correct": 0,
         "expl": "The general five-item version of the benefits this chapter has been tracing."},
        {"q": "Is this discourse's list identical in every wording to AN 5.34's?",
         "opts": [
             "Yes, word for word",
             "No — four items are worded closely but the fourth is genuinely different",
             "No, all five items differ completely",
             "The two discourses share no wording at all"],
         "correct": 1,
         "expl": "Close but not identical, a pattern worth noticing rather than assuming automatic repetition."},
        {"q": "Does this discourse include a named questioner testing the claims personally?",
         "opts": [
             "Yes, like Sīha in AN 5.34",
             "No — it is stated as a direct teaching with no dialogue",
             "Yes, Sumanā appears again",
             "Yes, Uggaha's daughters respond"],
         "correct": 1,
         "expl": "A structural difference from the previous discourse's personal exchange."},
        {"q": "What phrase describes the Dhamma taught by good companions in the closing verse?",
         "opts": [
             "'The path of merit'",
             "'Casting aside all suffering' (sabbadukkhāpanūdana)",
             "'The gate to wealth'",
             "'The way of kings'"],
         "correct": 1,
         "expl": "A phrase reaching toward the teaching's furthest claim."},
        {"q": "How long is this discourse compared to AN 5.34?",
         "opts": [
             "Much longer",
             "Considerably shorter, without AN 5.34's extended dialogue",
             "Identical in length",
             "This discourse has no text at all"],
         "correct": 1,
         "expl": "A bare list plus closing verses, without the personal exchange."},
        {"q": "Where is AN 5.35 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Four kept, one swapped", [
            "loved &middot; associated with",
            "reputation &middot; reborn well",
            "&mdash; swap: lay duties, not",
            "confident assembly",
        ]),
        ("No questioner here", [
            "AN 5.34: dialogue",
            "AN 5.35: direct teaching",
        ]),
        ("The final turn", [
            "worldly benefit &rarr;",
            "&ldquo;fully extinguished&rdquo;",
        ]),
        ("Cross-references", [
            "AN 5.34 &middot; the personal version",
            "AN 5.36 &middot; next: timely gifts",
            "AN 5.31 &middot; the same arc, at length",
        ]),
    ],
    further=[
        '<a href="%s/an5.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.34.html">AN 5.34 &middot; With General Sīha</a> &mdash; the previous '
        "discourse, the same fruits personally verified by a single questioner.",
        '<a href="an-5.36.html">AN 5.36 &middot; Timely Gifts</a> &mdash; next, five moments when '
        "giving carries special weight.",
        '<a href="an-5.31.html">AN 5.31 &middot; With Sumanā</a> &mdash; where the same movement '
        "from worldly benefit to full freedom opened this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.36 — Kāladānasutta
# --------------------------------------------------------------------------- #
page(
    36, "Kāladāna", "Timely Gifts",
    vagga=VAGGA_4,
    meta_title="AN 5.36 — Timely Gifts | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kāladānasutta — five "
        "moments when a gift carries particular weight: for a visitor, a traveler, someone sick, "
        "at a time of famine, and first fruits offered to the ethical. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of five timely occasions for giving, closing with verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Naming specific occasions when giving carries heightened merit "
                              "recurs across the Chinese Āgamas and Vinaya-adjacent literature; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short, practical list "
                       "shifting this chapter's focus from what giving does to when it matters "
                       "most"),
    ],
    why=(
        "Every discourse in this chapter so far has asked what giving produces. This one asks a "
        "different question: when does giving matter most? Its answer is entirely occasion-based "
        "&mdash; a visitor arriving, someone setting out on a journey, a person who is sick, a "
        "time of famine, and the very first harvest of the season &mdash; none of them about the "
        "size or nature of the gift, all of them about its timing."),
    guide=[
        ("The teaching in one sentence", [
            "There are five timely gifts: to a visitor, to someone setting out on a journey, to "
            "someone sick, at a time of famine, and presenting the first harvested grains and "
            "fruits to the ethical."]),
        ("Four occasions of need, one of abundance", [
            "The first four items share an obvious logic: a visitor, a traveler, a sick person, "
            "and a famine are all moments of genuine need or vulnerability, where a gift meets a "
            "concrete gap. The fifth breaks that pattern &mdash; offering the season's first "
            "harvest is not a response to anyone's hardship, but a deliberate act of putting "
            "abundance first toward the ethical before using it oneself."]),
        ("Timing, not size, as the variable", [
            "Nothing in this list concerns how much is given. The entire discourse treats "
            "<em>when</em> as the operative factor determining a gift's weight, distinct from "
            "every earlier discourse in this chapter, which concerned what results from giving "
            "in general, without regard to occasion."]),
        ("Who shares in the merit", [
            "The closing verses extend the discourse's scope past the giver alone: "
            "<em>those who rejoice at that, or do other services, don't miss out on the "
            "offering; they too have a share in the merit</em>. Approval and assistance, on this "
            "account, are not passive; someone who merely rejoices at another's timely gift is "
            "said to share in what it produces."]),
    ],
    terms=[
        ("kāladāna",
         "&ldquo;timely gift&rdquo; &mdash; this discourse&rsquo;s title and organizing concept, "
         "naming occasion rather than quantity as the operative factor."),
        ("gamika",
         "&ldquo;one setting out on a journey&rdquo; &mdash; the second timely occasion, a "
         "traveler about to depart."),
        ("dubbhikkha",
         "&ldquo;famine, scarcity of food&rdquo; &mdash; the fourth occasion, the only one of the "
         "five concerning a communal rather than individual circumstance."),
        ("navasassāni navaphalāni",
         "&ldquo;freshly harvested grains and fruits&rdquo; &mdash; the fifth occasion's object, "
         "the season's first produce offered before personal use."),
        ("anumodanti",
         "&ldquo;rejoice at, approve of&rdquo; &mdash; the verb in the closing verse marking "
         "onlookers who share in the merit of a gift they did not themselves give."),
    ],
    text_intro=(
        "The discourse in full: the five timely gifts, closing with verses on sharing in another's "
        "merit. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.36:1.1-1.8"),
        ("h3", "The closing verses"),
        ("p", "&sect;2", "an5.36:2.1-2.4"),
        ("p", "&sect;3", "an5.36:3.1-3.6"),
        ("p", "&sect;4", "an5.36:4.1-4.4"),
    ],
    quiz=[
        {"q": "What five occasions does this discourse name for timely giving?",
         "opts": [
             "Any five arbitrary days of the year",
             "A visitor, someone setting out on a journey, someone sick, a time of famine, and "
             "offering the first harvest to the ethical",
             "The five powers of a trainee",
             "Five specific monastic festivals"],
         "correct": 1,
         "expl": "Occasion-based, not quantity-based."},
        {"q": "What do the first four occasions share, according to the guide?",
         "opts": [
             "All concern wealthy recipients",
             "All are moments of genuine need or vulnerability, where a gift meets a concrete gap",
             "All occur only once per year",
             "None involve any real need at all"],
         "correct": 1,
         "expl": "A visitor, traveler, sick person, and famine share an obvious logic of need."},
        {"q": "How does the fifth occasion, first-harvest offering, break that pattern?",
         "opts": [
             "It doesn't; it also concerns need",
             "It is not a response to hardship, but a deliberate act of putting abundance first "
             "toward the ethical before personal use",
             "It applies only to monks",
             "It concerns famine specifically"],
         "correct": 1,
         "expl": "A pattern shift from responding to need to prioritizing generosity in abundance."},
        {"q": "What is the operative variable this discourse treats as determining a gift's "
              "weight?",
         "opts": [
             "The size of the gift",
             "Timing — when the gift is given, not how much",
             "The wealth of the giver",
             "The gender of the recipient"],
         "correct": 1,
         "expl": "Distinct from every earlier discourse in this chapter, which concerned general results rather than occasion."},
        {"q": "What do the closing verses say about those who merely approve of another's gift?",
         "opts": [
             "They gain nothing at all",
             "Those who rejoice or assist don't miss out on the offering — they too share in the "
             "merit",
             "They are criticized for not giving themselves",
             "The verses say nothing about onlookers"],
         "correct": 1,
         "expl": "Approval and assistance are treated as active, merit-sharing participation."},
        {"q": "Is quantity given any weight in this discourse's account of timely giving?",
         "opts": [
             "Yes, extensively",
             "No — the entire discourse concerns timing, not amount",
             "Only for the fifth occasion",
             "Only for gifts to the sick"],
         "correct": 1,
         "expl": "Occasion, not size, is the discourse's sole variable."},
        {"q": "What kind of occasion is famine, compared to the other four?",
         "opts": [
             "Identical to the others in every respect",
             "The only one of the five concerning a communal rather than individual circumstance",
             "A purely individual concern",
             "Not actually included in the list"],
         "correct": 1,
         "expl": "A shift in scale from the personal occasions of the first three."},
        {"q": "Does this discourse specify a minimum amount that must be given at these five "
              "occasions?",
         "opts": [
             "Yes, a specific quantity for each",
             "No amount is specified at all",
             "Only for the famine occasion",
             "Only for the harvest occasion"],
         "correct": 1,
         "expl": "Consistent with the discourse's focus on timing rather than quantity."},
        {"q": "What comes next in this chapter, after this discourse on timing?",
         "opts": [
             "AN 5.37, on what giving food specifically confers on its recipient",
             "A return to the powers of a trainee",
             "The end of the chapter",
             "A repeat of AN 5.35"],
         "correct": 0,
         "expl": "A further narrowing of focus, this time to a specific kind of gift."},
        {"q": "Where is AN 5.36 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five occasions", [
            "a visitor &middot; a traveler",
            "the sick &middot; a famine",
            "first harvest",
        ]),
        ("Need, then abundance", [
            "four: meeting a gap",
            "one: offering surplus",
            "first, deliberately",
        ]),
        ("Sharing the merit", [
            "&ldquo;those who rejoice",
            "or assist &mdash; they too",
            "have a share&rdquo;",
        ]),
        ("Cross-references", [
            "AN 5.35 &middot; giving, in general",
            "AN 5.37 &middot; next: food specifically",
            "AN 5.34 &middot; giving's visible fruits",
        ]),
    ],
    further=[
        '<a href="%s/an5.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.35.html">AN 5.35 &middot; The Benefits of Giving</a> &mdash; the previous '
        "discourse, on what giving produces in general.",
        '<a href="an-5.37.html">AN 5.37 &middot; Food</a> &mdash; next, five specific things a '
        "gift of food gives its recipient.",
        '<a href="an-5.34.html">AN 5.34 &middot; With General Sīha</a> &mdash; earlier in this '
        "chapter, giving's fruits verified personally.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.37 — Bhojanasutta
# --------------------------------------------------------------------------- #
page(
    37, "Bhojana", "Food",
    vagga=VAGGA_4,
    meta_title="AN 5.37 — Food | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bhojanasutta — giving "
        "food gives the recipient five things, and the giver receives the identical five things "
        "in their own future lives. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A five-item list of what food-giving confers, restated as what the giver "
                 "receives in return, closing with verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Reciprocal like-for-like karmic mechanisms for specific kinds of "
                              "giving are common across the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and unusually precise "
                       "about the mechanism connecting gift to result"),
    ],
    why=(
        "This discourse narrows the chapter's focus a final step, from giving in general to one "
        "specific gift: food. And it makes an unusually exact claim about how the mechanism works. "
        "Giving food does not simply produce good karma in the abstract; it gives the recipient "
        "five named things &mdash; long life, beauty, happiness, strength, eloquence &mdash; and "
        "the giver is then said to receive the identical five things themselves, as a god or "
        "human, in return."),
    guide=[
        ("The teaching in one sentence", [
            "A giver of food gives the recipient long life, beauty, happiness, strength, and "
            "eloquence, and by giving each of these, becomes a sharer in that same thing "
            "themselves, as a god or human."]),
        ("A precise, symmetrical mechanism", [
            "Unlike most of this chapter's discourses, which name benefits without specifying "
            "exactly how cause connects to effect, this one states the connection item by item: "
            "<em>āyuṁ datvā āyussa bhāgī hoti</em>, having given long life, one becomes a sharer "
            "in long life. The same formula repeats for beauty, happiness, strength, and "
            "eloquence, with no variation in structure across the five."]),
        ("Why food specifically produces these five", [
            "The discourse does not explain why food-giving in particular maps onto exactly these "
            "five results rather than some other set, but the connection is not arbitrary on its "
            "face: food sustains the body's life, appearance, comfort, and vigor directly, and "
            "the fifth item, eloquence, extends the logic from bodily nourishment to the kind of "
            "vitality that shows in speech."]),
        ("A narrower discourse than it first appears", [
            "This is the most specific gift this chapter examines &mdash; not giving broadly, not "
            "giving at a particular time, but giving one particular substance, food, with a "
            "correspondingly precise account of what it returns. Read after AN 5.36's broader "
            "occasions, this discourse completes a narrowing movement across three consecutive "
            "discourses: general benefits, then timing, then one specific gift examined in detail."]),
    ],
    terms=[
        ("āyuṁ vaṇṇaṁ sukhaṁ balaṁ paṭibhānaṁ",
         "&ldquo;long life, beauty, happiness, strength, and eloquence&rdquo; &mdash; the five "
         "things this discourse says food-giving confers and returns."),
        ("bhāgī hoti",
         "&ldquo;becomes a sharer in&rdquo; &mdash; the verb marking the giver's own future share "
         "in each of the five things given."),
        ("paṭibhāna",
         "&ldquo;eloquence, quick wit&rdquo; &mdash; the fifth item, extending the logic from "
         "bodily nourishment to vitality in speech."),
        ("paṭiggāhaka",
         "&ldquo;recipient&rdquo; &mdash; the person receiving the food, whose gain the giver's "
         "own future gain is said to mirror."),
        ("dibba mānusa",
         "&ldquo;divine or human&rdquo; &mdash; the two forms of existence in which the giver is "
         "said to receive each of the five things back."),
    ],
    text_intro=(
        "The discourse in full: the five things given with food, and the giver's own share in "
        "each, closing with verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five things, given with food"),
        ("p", "&sect;1", "an5.37:1.1-1.3"),
        ("p", "&sect;2", "an5.37:1.4"),
        ("p", "&sect;3", "an5.37:1.5"),
        ("p", "&sect;4", "an5.37:1.6"),
        ("p", "&sect;5", "an5.37:1.7"),
        ("p", "&sect;6", "an5.37:1.8"),
        ("p", "&sect;7", "an5.37:1.9"),
        ("h3", "The closing verses"),
        ("p", "&sect;8", "an5.37:2.1-2.4"),
        ("p", "&sect;9", "an5.37:3.1-3.4"),
    ],
    quiz=[
        {"q": "What five things does this discourse say a giver of food gives to the recipient?",
         "opts": [
             "Faith, ethics, learning, generosity, wisdom",
             "Long life, beauty, happiness, strength, and eloquence",
             "The five powers of a trainee",
             "Wealth, status, family, health, and fame"],
         "correct": 1,
         "expl": "A precise, five-item list specific to food-giving."},
        {"q": "What happens to the giver, according to this discourse's mechanism?",
         "opts": [
             "Nothing further is said about the giver",
             "The giver becomes a sharer in each of the same five things themselves, as a god or "
             "human",
             "The giver loses these five things",
             "Only the recipient benefits; the giver gains nothing"],
         "correct": 1,
         "expl": "An exact, symmetrical return for each of the five items given."},
        {"q": "How does this discourse's account of cause and effect compare to most of this "
              "chapter's other discourses on giving?",
         "opts": [
             "Identical, with no distinction",
             "Unusually precise — it specifies exactly how each item given connects to each item "
             "received, item by item",
             "Vaguer than the other discourses",
             "This discourse gives no account of cause and effect at all"],
         "correct": 1,
         "expl": "Most other discourses name benefits without this level of item-by-item mechanism."},
        {"q": "Why might food-giving specifically map onto these five results, according to the "
              "guide?",
         "opts": [
             "No connection is suggested at all",
             "Food sustains the body's life, appearance, comfort, and vigor directly, extending to "
             "vitality in speech as well",
             "The five results are entirely unrelated to food",
             "Because food is the most expensive gift possible"],
         "correct": 1,
         "expl": "A connection the guide reads as not arbitrary on its face, even though the text itself doesn't explain it."},
        {"q": "How does the guide describe this discourse's place in a three-discourse sequence "
              "with AN 5.35 and 5.36?",
         "opts": [
             "Unrelated to the two discourses before it",
             "The completion of a narrowing movement — general benefits, then timing, then one "
             "specific gift examined in detail",
             "A contradiction of both earlier discourses",
             "An exact repeat of AN 5.36"],
         "correct": 1,
         "expl": "General, then timely, then specific — a deliberate narrowing across three discourses."},
        {"q": "What verb marks the giver's own future share in what was given?",
         "opts": [
             "Nissarati, 'departs'",
             "Bhāgī hoti, 'becomes a sharer in'",
             "Vinassati, 'is destroyed'",
             "Paṭikkamati, 'withdraws'"],
         "correct": 1,
         "expl": "Repeated identically for each of the five items."},
        {"q": "Is the structure of the five-item formula varied across the five items, or kept "
              "consistent?",
         "opts": [
             "Varied significantly for each item",
             "Kept consistent — the identical formula repeats for beauty, happiness, strength, and "
             "eloquence after being stated for long life",
             "Only stated once, for long life alone",
             "Each item uses a completely different grammatical structure"],
         "correct": 1,
         "expl": "No variation in structure across the five repetitions."},
        {"q": "In what two forms of existence does the giver receive each of the five things back?",
         "opts": [
             "Only as a human",
             "As a god or human (dibba vā mānusa vā)",
             "Only as a god",
             "As an animal or a hungry ghost"],
         "correct": 1,
         "expl": "The same two destinations named across several discourses in this chapter."},
        {"q": "Does this discourse concern giving broadly, or one specific kind of gift?",
         "opts": [
             "Giving in the broadest possible sense",
             "One specific kind of gift — food",
             "Only gifts of money",
             "Only gifts to monastics"],
         "correct": 1,
         "expl": "The narrowest, most specific gift examined in this chapter."},
        {"q": "Where is AN 5.37 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five given, five returned", [
            "long life &middot; beauty",
            "happiness &middot; strength",
            "eloquence",
        ]),
        ("An exact mechanism", [
            "<span class=\"pali\">bhāgī hoti</span>",
            "&mdash; becomes a sharer,",
            "item for item",
        ]),
        ("Narrowing focus", [
            "AN 5.35: giving, general",
            "AN 5.36: giving, timely",
            "AN 5.37: food, specific",
        ]),
        ("Cross-references", [
            "AN 5.36 &middot; timely occasions",
            "AN 5.38 &middot; next: faith's own five",
            "AN 5.34 &middot; giving's visible fruits",
        ]),
    ],
    further=[
        '<a href="%s/an5.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.36.html">AN 5.36 &middot; Timely Gifts</a> &mdash; the previous discourse, '
        "on when a gift matters most.",
        '<a href="an-5.38.html">AN 5.38 &middot; Faith</a> &mdash; next, shifting from what is '
        "given to the quality of the giver themselves.",
        '<a href="an-5.35.html">AN 5.35 &middot; The Benefits of Giving</a> &mdash; the general '
        "version of this chapter&rsquo;s benefits, before this discourse&rsquo;s narrowing.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.38 — Saddhasutta
# --------------------------------------------------------------------------- #
page(
    38, "Saddha", "Faith",
    vagga=VAGGA_4,
    meta_title="AN 5.38 — Faith | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saddhasutta — a "
        "faithful gentleman's five benefits, illustrated by a banyan tree that becomes a refuge "
        "for birds from all around. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five benefits stated for the faithful, then a single simile, then verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The banyan-tree image for a person who shelters many others "
                              "recurs across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; shifts this chapter's focus "
                       "from the gift to the giver's own quality of faith"),
    ],
    why=(
        "Having examined giving in general, giving at the right time, and giving food "
        "specifically, this discourse steps back to the quality underlying all of it: faith. A "
        "faithful gentleman, it says, is approached, shown sympathy, and taught Dhamma before an "
        "unfaithful one &mdash; and becomes, like a great banyan tree at a crossroads, a refuge "
        "for many kinds of people at once."),
    guide=[
        ("The teaching in one sentence", [
            "True persons show sympathy to, approach, receive alms from, and teach Dhamma to the "
            "faithful before the unfaithful, and a faithful gentleman is reborn well and becomes "
            "a refuge for many people, like a great banyan tree for birds."]),
        ("Priority, not exclusion", [
            "The Pāli formula is careful: <em>paṭhamaṁ&hellip;no tathā assaddhaṁ</em>, first to "
            "the faithful, not so much to the faithless. This is a claim about priority and "
            "degree, not a claim that the unfaithful are refused outright. Four times over, the "
            "same qualified structure repeats, marking a consistent difference of emphasis rather "
            "than a hard exclusion."]),
        ("A tree for many kinds of bird", [
            "The banyan simile names its beneficiaries specifically: monks, nuns, laymen, and "
            "laywomen, all four sheltered by the same tree. The image is not of a private "
            "resource but a public one, becoming valuable precisely by being available to more "
            "than one kind of visitor at once &mdash; matching the discourse's closing verse, "
            "where <em>those that need shade go in the shade, those that need fruit enjoy the "
            "fruit</em>, different needs met by the same single source."]),
        ("Where the tree simile has appeared before", [
            "This is not the first tree image in this chapter: AN 5.24 used branches, foliage, "
            "shoots, bark, softwood, and heartwood to picture ethics supporting deeper "
            "attainments, and AN 5.40, closing this chapter, will use a similar image for a "
            "family supported by its head. Trees recur across this chapter as a preferred image "
            "for something that grows in layers and, once grown, supports more than itself."]),
    ],
    terms=[
        ("saddha kulaputta",
         "&ldquo;faithful gentleman&rdquo; &mdash; this discourse&rsquo;s subject, named by the "
         "quality of faith rather than by rank or wealth."),
        ("paṭhamaṁ&hellip;no tathā",
         "&ldquo;first&hellip;not so much&rdquo; &mdash; the qualifying formula marking each "
         "benefit as a matter of priority, not exclusion."),
        ("mahānigrodha",
         "&ldquo;great banyan tree&rdquo; &mdash; the discourse&rsquo;s central simile, chosen for "
         "its capacity to shelter many different visitors at once."),
        ("paṭisaraṇa",
         "&ldquo;refuge&rdquo; &mdash; the word applied both to the tree for birds and to the "
         "faithful gentleman for monks, nuns, laymen, and laywomen."),
        ("puññakkhetta",
         "&ldquo;field of merit&rdquo; &mdash; the closing verse&rsquo;s description of those the "
         "faithful gentleman associates with, echoing the same term used for the Saṅgha at AN "
         "5.32."),
    ],
    text_intro=(
        "The discourse in full: the five benefits of faith, the banyan simile, and the closing "
        "verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.38:1.1-1.8"),
        ("h3", "The banyan tree"),
        ("p", "&sect;2", "an5.38:2.1-2.2"),
        ("h3", "The closing verses"),
        ("p", "&sect;3", "an5.38:3.1-3.4"),
        ("p", "&sect;4", "an5.38:4.1-4.4"),
        ("p", "&sect;5", "an5.38:5.1-5.4"),
        ("p", "&sect;6", "an5.38:6.1-6.4"),
        ("p", "&sect;7", "an5.38:7.1-7.4"),
    ],
    quiz=[
        {"q": "What does the formula 'paṭhamaṁ...no tathā assaddhaṁ' claim about the faithful "
              "and unfaithful?",
         "opts": [
             "That the unfaithful are refused help entirely",
             "That the faithful are approached and helped first, as a matter of priority — not "
             "that the unfaithful are excluded outright",
             "That faith is irrelevant to how people are treated",
             "That only the faithful may receive alms"],
         "correct": 1,
         "expl": "A claim about degree and priority, repeated identically four times."},
        {"q": "Who does the banyan tree simile name as sheltered by a faithful gentleman?",
         "opts": [
             "Only monks",
             "Monks, nuns, laymen, and laywomen — all four kinds of Buddhist follower",
             "Only wealthy donors",
             "Only his own family"],
         "correct": 1,
         "expl": "A public resource available to more than one kind of visitor."},
        {"q": "What does the closing verse say about the tree's shade and fruit?",
         "opts": [
             "Only shade is available, no fruit",
             "Different needs are met by the same single source — shade for those needing shade, "
             "fruit for those needing fruit",
             "Only fruit is available, no shade",
             "The tree provides nothing useful at all"],
         "correct": 1,
         "expl": "One source, multiple kinds of benefit, matching the discourse's account of the faithful gentleman."},
        {"q": "Where else in this chapter has a tree image already appeared, according to the "
              "guide?",
         "opts": [
             "Nowhere else in this chapter",
             "AN 5.24, using branches, foliage, shoots, bark, softwood, and heartwood for ethics "
             "supporting deeper attainments",
             "Only in AN 5.31",
             "Only in the previous nipāta"],
         "correct": 1,
         "expl": "A recurring image across the collection, not unique to this discourse."},
        {"q": "What does this discourse shift the chapter's focus toward, compared to AN "
              "5.35–5.37?",
         "opts": [
             "It continues examining specific gifts",
             "It steps back to the quality of faith underlying the giver, rather than the gift "
             "itself",
             "It abandons the topic of giving entirely",
             "It returns to the powers of a trainee"],
         "correct": 1,
         "expl": "From what is given, to who the giver is."},
        {"q": "What does 'puññakkhetta', field of merit, describe in this discourse's closing "
              "verse?",
         "opts": [
             "The faithful gentleman's farmland",
             "Those the faithful gentleman associates with — echoing the same term used for the "
             "Saṅgha at AN 5.32",
             "A type of monastic robe",
             "A specific meditation technique"],
         "correct": 1,
         "expl": "The same term applied to the Saṅgha reappears here for the company a faithful person keeps."},
        {"q": "How many times does the qualifying formula 'first...not so much' repeat across the "
              "discourse's list of benefits?",
         "opts": ["Once", "Twice", "Four times", "Not at all"],
         "correct": 2,
         "expl": "A consistent structure across sympathy, approach, receiving alms, and teaching Dhamma."},
        {"q": "What comes after this discourse in the chapter?",
         "opts": [
             "AN 5.39, on parents' reasons for wanting children",
             "A return to AN 5.31's material",
             "The end of the chapter",
             "A repeat of AN 5.37"],
         "correct": 0,
         "expl": "The chapter continues its exploration of lay social and family life."},
        {"q": "Does the discourse claim the unfaithful receive no teaching of Dhamma at all?",
         "opts": [
             "Yes, they are entirely excluded",
             "No — the claim is about who is taught first, not an absolute exclusion",
             "The discourse does not address this",
             "Yes, but only for one specific benefit"],
         "correct": 1,
         "expl": "Consistent with the priority-not-exclusion reading the guide applies throughout."},
        {"q": "Where is AN 5.38 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five benefits", [
            "sympathy first",
            "approached first",
            "alms given first",
            "taught first",
            "reborn well",
        ]),
        ("Priority, not exclusion", [
            "&ldquo;first&hellip;",
            "not so much&hellip;&rdquo;",
        ]),
        ("The banyan", [
            "monks, nuns,",
            "laymen, laywomen &mdash;",
            "all sheltered at once",
        ]),
        ("Cross-references", [
            "AN 5.24 &middot; the tree, before",
            "AN 5.32 &middot; field of merit, first used",
            "AN 5.39 &middot; next: why parents want a child",
        ]),
    ],
    further=[
        '<a href="%s/an5.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.37.html">AN 5.37 &middot; Food</a> &mdash; the previous discourse, on what '
        "a specific gift confers.",
        '<a href="an-5.39.html">AN 5.39 &middot; A Child</a> &mdash; next, a shift from the '
        "faithful adult to family life itself.",
        '<a href="an-5.24.html">AN 5.24 &middot; Unethical</a> &mdash; the earlier tree simile '
        "this discourse&rsquo;s banyan image echoes.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.39 — Puttasutta
# --------------------------------------------------------------------------- #
page(
    39, "Putta", "A Child",
    vagga=VAGGA_4,
    meta_title="AN 5.39 — A Child | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Puttasutta — five "
        "reasons parents in this discourse's world wish for a child: reciprocal care, family "
        "continuity, inheritance, and offerings for the dead. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of five parental motives, followed by verses addressed to grown "
                 "children"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Filial reciprocity and ancestral offerings are central themes "
                              "across Chinese Buddhist lay ethics; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a window into an "
                       "economic and religious logic of family this reading guide will not "
                       "modernize"),
    ],
    why=(
        "This discourse states, without embarrassment, why parents in its world want children: "
        "so the children will later support them, take on family duties, keep the family "
        "tradition alive, manage the inheritance, and make offerings to them after death. None of "
        "these five reasons concerns love, companionship, or anything resembling a modern account "
        "of why people want children. They are frankly transactional, and this reading guide "
        "presents them as the discourse states them rather than translating them into more "
        "familiar sentiment."),
    guide=[
        ("The teaching in one sentence", [
            "Parents wish for a child for five reasons: having been supported, the child will "
            "support them in turn; will do their duty for them; will keep the family tradition "
            "alive; will take care of the inheritance; and will make an offering on their behalf "
            "after they have died."]),
        ("An economic and religious logic, stated plainly", [
            "In a society without pensions or formal social security, an adult child was, quite "
            "literally, the parents' plan for old age and for what happens after death. The fifth "
            "reason, <em>dakkhiṇaṁ anuppadassati</em>, they will give an offering on our behalf, "
            "refers to the practice of dedicating merit to deceased relatives, particularly those "
            "reborn as <em>peta</em>, hungry ghosts, who were believed to depend on such offerings "
            "for their own relief. Reading this discourse without that context makes its "
            "priorities look coldly self-interested; reading it with that context shows a "
            "coherent, if unfamiliar, logic of mutual obligation across generations, including "
            "generations already dead."]),
        ("What is absent from this list", [
            "As with AN 5.33's instruction to daughters, it is worth noting what this list does "
            "not mention: no reason here concerns affection, the joy of raising a child, or "
            "anything the child might gain for their own sake. The discourse states parental "
            "motive from the parents' side only, and states it as reciprocal exchange, not "
            "sentiment."]),
        ("The child's side, in the closing verses", [
            "The verses that follow reframe the same material from the child's perspective, and "
            "shift register: a praiseworthy child is one who is <em>grateful and thankful</em>, "
            "who looks after parents <em>remembering past deeds</em>, doing for them "
            "<em>as their parents did for them in the past</em>. The obligation described is "
            "explicitly reciprocal &mdash; owed because it was first given &mdash; rather than "
            "unconditional."]),
    ],
    terms=[
        ("kulavaṁsa",
         "&ldquo;family lineage, tradition&rdquo; &mdash; the third parental motive, continuity of "
         "the family line and its customs through a child."),
        ("dāyajja",
         "&ldquo;inheritance&rdquo; &mdash; the fourth motive, a child's role managing what the "
         "family has accumulated."),
        ("peta",
         "&ldquo;departed one, hungry ghost&rdquo; &mdash; the deceased relatives the fifth "
         "motive's offering is understood to benefit."),
        ("dakkhiṇā",
         "&ldquo;religious offering, donation&rdquo; &mdash; the specific act of merit-dedication "
         "named in the fifth reason, given on behalf of the dead."),
        ("kataññū katavedī",
         "&ldquo;grateful and thankful&rdquo; &mdash; the closing verses&rsquo; description of a "
         "praiseworthy child, framing the obligation as reciprocal rather than unconditional."),
    ],
    text_intro=(
        "The discourse in full: the five parental reasons, and the closing verses addressed to "
        "grown children. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.39:1.1-1.8"),
        ("h3", "The closing verses"),
        ("p", "&sect;2", "an5.39:2.1-2.4"),
        ("p", "&sect;3", "an5.39:3.1-3.4"),
        ("p", "&sect;4", "an5.39:4.1-4.4"),
        ("p", "&sect;5", "an5.39:5.1-5.4"),
        ("p", "&sect;6", "an5.39:6.1-6.4"),
    ],
    quiz=[
        {"q": "What are the five reasons this discourse gives for parents wishing for a child?",
         "opts": [
             "Love, companionship, joy, curiosity, and legacy",
             "Reciprocal support in old age, doing duties for the parents, continuing family "
             "tradition, managing inheritance, and making offerings after death",
             "Wealth, status, education, health, and beauty",
             "The five powers of a trainee"],
         "correct": 1,
         "expl": "Explicitly reciprocal and transactional reasons, stated without sentiment."},
        {"q": "What does the guide say is notably absent from this list of reasons?",
         "opts": [
             "Nothing is absent; the list is comprehensive",
             "Any reason concerning affection, the joy of raising a child, or anything for the "
             "child's own sake",
             "Any mention of inheritance",
             "Any mention of family tradition"],
         "correct": 1,
         "expl": "Stated entirely from the parents' side, as reciprocal exchange rather than sentiment."},
        {"q": "What does 'dakkhiṇaṁ anuppadassati', the fifth reason, refer to?",
         "opts": [
             "A wedding gift",
             "Dedicating merit to deceased relatives, particularly those believed to depend on "
             "such offerings as hungry ghosts (peta)",
             "A tax payment",
             "A dowry"],
         "correct": 1,
         "expl": "A specific religious practice tied to belief about the afterlife of the dead."},
        {"q": "How does the guide frame the social and economic context behind this list?",
         "opts": [
             "As simply coldly self-interested, with nothing more to say about it",
             "As a coherent, if unfamiliar, logic of mutual obligation across generations, in a "
             "society without pensions or formal social security",
             "As entirely irrational and unexplainable",
             "As identical to modern family values"],
         "correct": 1,
         "expl": "Context that makes an unfamiliar-looking list legible rather than simply judged."},
        {"q": "How do the closing verses reframe the material, compared to the opening list?",
         "opts": [
             "They repeat the parents' perspective exactly",
             "They shift to the child's perspective, describing a praiseworthy child as grateful "
             "and thankful, repaying what was first given",
             "They abandon the topic of family entirely",
             "They criticize parents for expecting anything from children"],
         "correct": 1,
         "expl": "Explicit reciprocity: owed because it was first given."},
        {"q": "Does this reading guide modernize or soften this discourse's stated priorities?",
         "opts": [
             "Yes, translating them into more familiar sentiment",
             "No — it presents them as the discourse states them, with historical context rather "
             "than substitution",
             "It refuses to discuss the discourse at all",
             "It claims the discourse is not authentic"],
         "correct": 1,
         "expl": "Consistent with this reading guide's approach to historically specific material elsewhere in this chapter."},
        {"q": "What does 'kulavaṁsa' concern?",
         "opts": [
             "A specific meditation technique",
             "Family lineage and tradition, continued through a child",
             "A type of monastic robe",
             "A form of currency"],
         "correct": 1,
         "expl": "The third of the five parental motives."},
        {"q": "What other discourse in this chapter does the guide compare this one to, for "
              "similarly stating historically specific material honestly?",
         "opts": [
             "AN 5.31", "AN 5.33, on instructions given to daughters before marriage",
             "AN 5.36", "AN 5.34"],
         "correct": 1,
         "expl": "Both discourses require the same honest, unflinching presentation this reading guide applies throughout."},
        {"q": "Is the obligation described in the closing verses framed as unconditional?",
         "opts": [
             "Yes, entirely unconditional",
             "No — explicitly reciprocal, owed because it was first given",
             "The verses take no position on this",
             "Yes, but only for the eldest child"],
         "correct": 1,
         "expl": "'As their parents did for them in the past' — a stated basis for the obligation."},
        {"q": "Where is AN 5.39 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five reasons", [
            "reciprocal support",
            "duties done",
            "tradition continued",
            "inheritance managed",
            "offerings, after death",
        ]),
        ("A specific belief", [
            "<span class=\"pali\">peta</span>hungry ghosts",
            "&mdash; dependent on offerings",
            "from the living",
        ]),
        ("The child's side", [
            "&ldquo;grateful, thankful&rdquo;",
            "&mdash; repaying",
            "what was first given",
        ]),
        ("Cross-references", [
            "AN 5.33 &middot; another historical text",
            "AN 5.40 &middot; next: the chapter closes",
            "AN 5.38 &middot; the faithful, as refuge",
        ]),
    ],
    further=[
        '<a href="%s/an5.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.38.html">AN 5.38 &middot; Faith</a> &mdash; the previous discourse, on the '
        "faithful as a refuge for others.",
        '<a href="an-5.40.html">AN 5.40 &middot; Great Sal Trees</a> &mdash; next, closing this '
        "chapter with a family's own growth.",
        '<a href="an-5.33.html">AN 5.33 &middot; With Uggaha</a> &mdash; the earlier discourse '
        "this page's historical framing most closely matches.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.40 — Mahāsālaputtasutta
# --------------------------------------------------------------------------- #
page(
    40, "Mahāsāla", "Great Sal Trees",
    vagga=VAGGA_4,
    meta_title="AN 5.40 — Great Sal Trees | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahāsālaputtasutta, "
        "closing this chapter — great sal trees grow in five ways supported by the Himalayas, "
        "and a family grows in five ways supported by a faithful head: faith, ethics, learning, "
        "generosity, and wisdom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A tree simile stated in full, then applied directly to a family's growth, "
                 "closing with verses and this chapter's colophon"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The five-item lay virtue set — faith, ethics, learning, "
                              "generosity, wisdom — is a standard formula across the Chinese "
                              "Āgamas' treatment of household life; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; closes the chapter by "
                       "returning to its tree imagery one final time, now on family growth "
                       "specifically"),
    ],
    why=(
        "This chapter's final discourse returns to a tree one more time, but shifts what grows: "
        "not ethics supporting deeper attainment, as at AN 5.24, and not a refuge sheltering "
        "visitors, as at AN 5.38, but an entire household growing around a single faithful head. "
        "Great sal trees, supported by the Himalayas, grow in five named parts; a family, "
        "supported by a faithful family head, grows in five named qualities: faith, ethics, "
        "learning, generosity, and wisdom."),
    guide=[
        ("The teaching in one sentence", [
            "Just as great sal trees grow, supported by the Himalayas, in their branches, bark, "
            "shoots, softwood, and hardwood, a family grows, supported by a faithful family head, "
            "in faith, ethics, learning, generosity, and wisdom."]),
        ("A third tree, a third use", [
            "AN 5.24's tree measured the absence or presence of branches and foliage against four "
            "inner parts failing or succeeding to grow. AN 5.38's banyan sheltered visitors "
            "beneath it. This discourse's sal trees do neither; they grow themselves, in five "
            "named parts, and the simile's point is growth as a process rather than either "
            "structural support or shelter. Three trees, three distinct jobs, across one chapter."]),
        ("Five qualities, a set met before under a different frame", [
            "<em>Saddhā, sīla, suta, cāga, paññā</em> &mdash; faith, ethics, learning, generosity, "
            "wisdom &mdash; is a standard grouping of lay virtues, distinct from every five-item "
            "power list this nipāta has used for monastics. Learning and generosity, in "
            "particular, have not appeared together as named qualities to be developed anywhere "
            "earlier in the Fives; this is their first joint appearance."]),
        ("Who grows, and who is credited", [
            "The discourse is explicit about direction: it is the <em>antojana</em>, the "
            "household&rsquo;s members &mdash; children, partners, kin, colleagues, dependents "
            "&mdash; who grow, supported by the family head, not the reverse. The verses extend "
            "this further: those who see the family head's ethical conduct, generosity, and good "
            "deeds <em>do likewise</em>, a direct claim that a household's character propagates "
            "outward from whoever leads it by example rather than instruction."]),
        ("Closing the chapter", [
            "This is the fourth chapter to close with the same colophon structure explained in "
            "full at AN 5.10: a naming verse, <em>Sumanavaggo catuttho</em>, and the chapter's "
            "own untranslated uddāna, compressing all ten titles &mdash; Sumanā, Cundī, Uggaha, "
            "Sīha, the benefits of giving, timely gifts and food, faith, and so on &mdash; into a "
            "chantable mnemonic. The next chapter, Muṇḍarājavagga, turns to a specific king."]),
    ],
    terms=[
        ("mahāsāla",
         "&ldquo;great sal tree&rdquo; &mdash; this discourse's title and central image, a large "
         "hardwood tree native to the Himalayan foothills."),
        ("saddhā sīla suta cāga paññā",
         "&ldquo;faith, ethics, learning, generosity, wisdom&rdquo; &mdash; the five lay "
         "qualities this discourse says a household grows in, distinct from every monastic power "
         "list in this nipāta."),
        ("antojana",
         "&ldquo;household members&rdquo; &mdash; children, partners, kin, colleagues, and "
         "dependents, named as who grows around a faithful family head."),
        ("saddhaṁ kulaputtaṁ nissāya",
         "&ldquo;supported by a family head with faith&rdquo; &mdash; the phrase marking the "
         "faithful head as the household's Himalayas, the base everything else grows against."),
        ("Sumanavaggo catuttho",
         "&ldquo;the fourth chapter, With Sumanā&rdquo; &mdash; this vagga's closing colophon, "
         "matching the form already explained in full at AN 5.10."),
    ],
    text_intro=(
        "The discourse in full: the sal-tree simile and its application to a family's growth, "
        "closing with verses. The chapter's closing colophon and Pāli mnemonic verse are part of "
        "the source but are not translated text, and are described rather than reproduced here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Great sal trees, growing in five ways"),
        ("p", "&sect;1", "an5.40:1.1-1.8"),
        ("h3", "A family, growing in five ways"),
        ("p", "&sect;2", "an5.40:1.9-1.16"),
        ("h3", "The closing verses"),
        ("p", "&sect;3", "an5.40:2.1-2.4"),
        ("p", "&sect;4", "an5.40:3.1-3.6"),
        ("p", "&sect;5", "an5.40:4.1-4.4"),
        ("p", "&sect;6", "an5.40:5.1-5.4"),
    ],
    quiz=[
        {"q": "What five qualities does this discourse say a family grows in, supported by a "
              "faithful head?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Faith, ethics, learning, generosity, and wisdom",
             "The five powers of a trainee",
             "Long life, beauty, happiness, strength, and eloquence"],
         "correct": 1,
         "expl": "Saddhā, sīla, suta, cāga, paññā — a standard lay-virtue grouping."},
        {"q": "How does this discourse's tree image differ in function from AN 5.24's and AN "
              "5.38's, according to the guide?",
         "opts": [
             "All three trees serve the identical function",
             "AN 5.24's measured presence/absence of inner growth; AN 5.38's sheltered visitors; "
             "this one pictures growth itself as a process",
             "This discourse is the only one in the chapter to use a tree image",
             "The three trees contradict each other"],
         "correct": 1,
         "expl": "Three distinct jobs for the same recurring image across one chapter."},
        {"q": "Who does the discourse say grows, supported by the family head?",
         "opts": [
             "The family head grows; everyone else stays the same",
             "The antojana — children, partners, kin, colleagues, and dependents",
             "Only the eldest child",
             "No one; the discourse describes only the tree, not a family"],
         "correct": 1,
         "expl": "Direction matters: the household grows around the head, not the reverse."},
        {"q": "What do the closing verses add about how a household's character spreads?",
         "opts": [
             "Nothing further is said",
             "Those who see the family head's ethical conduct, generosity, and good deeds 'do "
             "likewise' — character propagating by example",
             "Character is said to be entirely inherited, not learned",
             "The verses claim character cannot be influenced by example"],
         "correct": 1,
         "expl": "Propagation by observed example, not by instruction."},
        {"q": "What is distinctive about learning (suta) and generosity (cāga) appearing together "
              "here, according to the guide?",
         "opts": [
             "Nothing; this pairing has appeared many times already in the Fives",
             "This is their first joint appearance as named qualities to be developed in this "
             "nipāta",
             "They are contradictory qualities that cannot coexist",
             "They only apply to monastics, not laypeople"],
         "correct": 1,
         "expl": "A first appearance worth noting, distinct from the monastic power lists used elsewhere."},
        {"q": "What colophon closes this chapter?",
         "opts": [
             "No colophon is present",
             "Sumanavaggo catuttho, 'the fourth chapter, With Sumanā', with the chapter's own "
             "uddāna verse",
             "A colophon naming a different chapter",
             "The colophon from AN 5.10, repeated verbatim"],
         "correct": 1,
         "expl": "Matching the structure already explained in full at AN 5.10 and repeated at AN 5.20 and AN 5.30."},
        {"q": "What chapter follows the Sumanavagga?",
         "opts": [
             "A return to the Sekhabalavagga",
             "The Muṇḍarājavagga, turning to a specific king",
             "The end of the entire nipāta",
             "A repeat of the Balavagga"],
         "correct": 1,
         "expl": "The next chapter in sequence, per this discourse's guide."},
        {"q": "What five parts does a sal tree grow in, per the simile's first half?",
         "opts": [
             "Roots, trunk, flowers, seeds, and sap",
             "Branches and foliage, bark, shoots, softwood, and hardwood",
             "Only the trunk and roots",
             "Leaves, fruit, thorns, flowers, and bark"],
         "correct": 1,
         "expl": "The tree's own named growth, before the simile is applied to a family."},
        {"q": "Is this five-item lay-virtue set (faith, ethics, learning, generosity, wisdom) the "
              "same as any monastic power list used earlier in this nipāta?",
         "opts": [
             "Yes, identical to the sekhabala",
             "No — distinct from every monastic power list this nipāta has used",
             "Yes, identical to the standard bala",
             "Yes, identical to AN 5.17–20's five items"],
         "correct": 1,
         "expl": "A separate five-item grouping specific to lay household life."},
        {"q": "Where is AN 5.40 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("The tree, growing", [
            "branches &amp; foliage",
            "bark &middot; shoots",
            "softwood &middot; hardwood",
        ]),
        ("The family, growing", [
            "faith &middot; ethics",
            "learning &middot; generosity",
            "wisdom",
        ]),
        ("Three trees, three jobs", [
            "AN 5.24: inner growth",
            "AN 5.38: shelter",
            "AN 5.40: growth itself",
        ]),
        ("Cross-references", [
            "AN 5.24 &amp; 5.38 &middot; earlier trees",
            "AN 5.10 &middot; the colophon form",
            "AN 5.41 &middot; next: Muṇḍarājavagga",
        ]),
    ],
    further=[
        '<a href="%s/an5.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.39.html">AN 5.39 &middot; A Child</a> &mdash; the previous discourse, on '
        "family from the parents' side.",
        '<a href="an-5.24.html">AN 5.24 &middot; Unethical</a> &mdash; and <a href="an-5.38.html">'
        "AN 5.38 &middot; Faith</a> &mdash; this chapter's two earlier tree similes.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; where this same '
        "chapter-closing colophon structure was first explained in full.",
    ],
)
