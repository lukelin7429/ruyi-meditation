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
