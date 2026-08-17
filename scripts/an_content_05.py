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


VAGGA_5 = "<em>Muṇḍarājavagga</em> &mdash; the fifth chapter of the Fives"


# --------------------------------------------------------------------------- #
# AN 5.41 — Ādiyasutta
# --------------------------------------------------------------------------- #
page(
    41, "Ādiya", "Getting Rich",
    vagga=VAGGA_5,
    meta_title="AN 5.41 — Getting Rich | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ādiyasutta — five "
        "legitimate uses of wealth, from supporting one's own household to spirit-offerings for "
        "relatives, guests, ancestors, king, and deities, leaving a giver with no regrets either "
        "way. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery; stated at the head of "
                    "AN 5.41"),
        ("Speakers", "The householder Anāthapiṇḍika, addressed directly by the Buddha"),
        ("Form", "Five uses of legitimate wealth stated in turn, then a two-sided formula for "
                 "regret, closing with verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Fivefold schemes for the proper use of wealth, including "
                              "offerings to ancestors and rulers, recur across the Chinese "
                              "Āgamas' lay-ethics material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; opens this chapter with an "
                       "unusually wide-ranging account of a householder's obligations"),
    ],
    why=(
        "This chapter takes its name from King Muṇḍa, whose grief closes it at AN 5.50, but "
        "opens with something much less dramatic: a direct address to Anāthapiṇḍika, the "
        "Buddha's most prominent lay donor, on what legitimately earned wealth is actually for. "
        "The five reasons range from the intimate &mdash; making one's own household happy "
        "&mdash; to the frankly cosmological: five spirit-offerings to relatives, guests, "
        "ancestors, the king, and deities, sitting inside a Buddhist discourse without comment "
        "or apology."),
    guide=[
        ("The teaching in one sentence", [
            "With legitimate wealth, earned by one's own effort, a noble disciple makes "
            "themselves and their household happy, makes friends and colleagues happy, protects "
            "against loss, makes five spirit-offerings, and supports virtuous ascetics and "
            "brahmins with a religious donation."]),
        ("Wealth&rsquo;s legitimacy, stated before its use", [
            "Every one of the five reasons is prefaced by the identical qualifying phrase: wealth "
            "<em>earned by his efforts and initiative, built up with his own hands, gathered by "
            "the sweat of the brow</em>, and <em>dhammikehi dhammaladdhehi</em>, legitimate and "
            "legitimately acquired. The discourse is not indifferent to how wealth was obtained; "
            "the five uses that follow are licensed only for wealth that meets this standard "
            "first."]),
        ("Five spirit-offerings, without comment", [
            "The fourth reason names <em>pañcabali</em>, five spirit-offerings, to relatives, "
            "guests, ancestors, the king, and deities &mdash; a frankly non-monastic, culturally "
            "embedded set of obligations that this discourse simply includes as one of five "
            "legitimate uses of wealth, alongside supporting virtuous renunciates. This reading "
            "guide does not read this as a later addition or an embarrassment to be explained "
            "away; the discourse places ordinary social and religious duty and support for "
            "Buddhist practitioners side by side, without ranking one above the other."]),
        ("No regrets, either way", [
            "The discourse's final claim is its most psychologically interesting: a noble "
            "disciple who has used their wealth for these five reasons has no regrets whether "
            "their wealth later runs out or increases. Regret, on this account, is not a "
            "response to outcome; it is a response to whether the wealth was rightly used while "
            "it was held. Once that condition is met, the discourse says, either direction of "
            "fortune leaves the disciple equally free of remorse."]),
        ("The verses' closing claim", [
            "The verses restate the five uses in the first person and close with "
            "<em>I've achieved the goal for which an astute layperson wishes to gain wealth. I "
            "don't regret what I've done</em> &mdash; framing the entire discourse not as a rule "
            "to obey but as a description of what a satisfied conscience, examined honestly, "
            "actually rests on."]),
    ],
    terms=[
        ("bhogānaṁ ādiya",
         "&ldquo;reason to get rich, use of wealth&rdquo; &mdash; this discourse's title and "
         "organizing concept, naming five licensed purposes for legitimately earned wealth."),
        ("dhammikehi dhammaladdhehi",
         "&ldquo;legitimate and legitimately acquired&rdquo; &mdash; the qualifying phrase "
         "attached to every one of the five uses, marking wealth's origin as a precondition."),
        ("pañcabali",
         "&ldquo;five spirit-offerings&rdquo; &mdash; to relatives, guests, ancestors, the king, "
         "and deities, the fourth and most culturally specific of the five uses."),
        ("uddhaggikā dakkhiṇā",
         "&ldquo;an uplifting religious donation&rdquo; &mdash; the fifth use, support for "
         "virtuous ascetics and brahmins, conducive to heaven."),
        ("avippaṭisāra",
         "&ldquo;without regret&rdquo; &mdash; the discourse's closing psychological claim, "
         "holding regardless of whether wealth later increases or is lost."),
    ],
    text_intro=(
        "The discourse in full: the five reasons to get rich, and the formula for freedom from "
        "regret regardless of outcome, closing with verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five reasons to get rich"),
        ("p", "&sect;1", "an5.41:1.1-1.2"),
        ("p", "&sect;2", "an5.41:1.3-1.4"),
        ("p", "&sect;3", "an5.41:1.5-1.8"),
        ("p", "&sect;4", "an5.41:2.1-2.2"),
        ("p", "&sect;5", "an5.41:3.1-3.4"),
        ("p", "&sect;6", "an5.41:4.1-4.3"),
        ("p", "&sect;7", "an5.41:5.1-5.2"),
        ("h3", "No regrets, either way"),
        ("p", "&sect;8", "an5.41:6.1-6.6"),
        ("h3", "The closing verses"),
        ("p", "&sect;9", "an5.41:7.1-7.6"),
        ("p", "&sect;10", "an5.41:8.1-8.4"),
        ("p", "&sect;11", "an5.41:9.1-9.4"),
    ],
    quiz=[
        {"q": "What five reasons does this discourse give for legitimately getting rich?",
         "opts": [
             "The five powers of a trainee",
             "Making self and household happy, making friends happy, protecting against loss, "
             "spirit-offerings, and supporting virtuous ascetics",
             "Investment, savings, trade, taxation, and inheritance",
             "Faith, ethics, learning, generosity, and wisdom"],
         "correct": 1,
         "expl": "Five licensed purposes, each requiring legitimately earned wealth first."},
        {"q": "What qualifying phrase is attached to every one of the five reasons?",
         "opts": [
             "None; the discourse gives no qualification",
             "That the wealth is legitimate and legitimately acquired, earned by one's own effort",
             "That the wealth must exceed a certain amount",
             "That the wealth must be inherited"],
         "correct": 1,
         "expl": "Dhammikehi dhammaladdhehi — a precondition attached before every listed use."},
        {"q": "What does the fourth reason, the five spirit-offerings, name as recipients?",
         "opts": [
             "Only monastics",
             "Relatives, guests, ancestors, the king, and deities",
             "Only the poor",
             "Only close family"],
         "correct": 1,
         "expl": "A culturally embedded, non-monastic set of obligations included without apology."},
        {"q": "How does the guide read the presence of spirit-offerings alongside support for "
              "Buddhist renunciates in this list?",
         "opts": [
             "As a later addition to be explained away or dismissed as inauthentic",
             "As the discourse placing ordinary social and religious duty and support for "
             "practitioners side by side, without ranking one above the other",
             "As a contradiction the text fails to resolve",
             "As evidence the discourse is not really about Buddhist wealth ethics at all"],
         "correct": 1,
         "expl": "Presented honestly, without smoothing over its non-monastic content."},
        {"q": "What does the discourse claim about regret if wealth later runs out?",
         "opts": [
             "The disciple will necessarily regret their choices",
             "There is no regret, since the wealth was rightly used while it was held",
             "The discourse takes no position on this",
             "Regret depends entirely on how much wealth was lost"],
         "correct": 1,
         "expl": "Regret is tied to right use, not to outcome, on this discourse's account."},
        {"q": "What does the discourse claim about regret if wealth increases instead?",
         "opts": [
             "Regret increases proportionally",
             "The same freedom from regret holds, since the underlying condition — right use — is "
             "unchanged",
             "The disciple should feel guilty about the increase",
             "The discourse does not address this case"],
         "correct": 1,
         "expl": "Both directions of fortune leave the disciple equally free of remorse."},
        {"q": "Who is this discourse addressed to?",
         "opts": [
             "A group of mendicants generally",
             "The householder Anāthapiṇḍika, the Buddha's prominent lay donor",
             "King Muṇḍa",
             "Princess Sumanā"],
         "correct": 1,
         "expl": "A direct address to a specific, well-known lay figure."},
        {"q": "What does the closing verse say an astute layperson has achieved through this "
              "right use of wealth?",
         "opts": [
             "Nothing of lasting value",
             "The very goal for which an astute layperson wishes to gain wealth, with no regret "
             "for what was done",
             "Only temporary satisfaction",
             "Guaranteed enlightenment"],
         "correct": 1,
         "expl": "A description of a satisfied conscience, examined honestly."},
        {"q": "What kinds of loss does the third reason protect against?",
         "opts": [
             "Only financial market fluctuations",
             "Fire, water, kings, bandits, and unloved heirs",
             "Only natural disasters",
             "Only theft"],
         "correct": 1,
         "expl": "A specific, concrete list of disaster and misfortune scenarios."},
        {"q": "What chapter does this discourse open, and what does its title reference?",
         "opts": [
             "The Sekhabalavagga",
             "The Muṇḍarājavagga, named for King Muṇḍa, whose grief closes the chapter at AN 5.50",
             "The Balavagga",
             "The Pañcaṅgikavagga"],
         "correct": 1,
         "expl": "A very different opening than the chapter's dramatic closing narrative."},
    ],
    marginalia=[
        ("Five uses", [
            "self &amp; household",
            "friends, colleagues",
            "protection from loss",
            "spirit-offerings",
            "religious donation",
        ]),
        ("A precondition first", [
            "<span class=\"pali\">dhammikehi</span>",
            "&mdash; legitimate,",
            "before anything else",
        ]),
        ("No regrets, either way", [
            "wealth shrinks &rarr; no regret",
            "wealth grows &rarr; no regret",
            "&mdash; use, not outcome",
        ]),
        ("Cross-references", [
            "AN 5.34&ndash;40 &middot; giving, at length",
            "AN 5.42 &middot; next: a true person's benefit",
            "AN 5.50 &middot; the chapter's namesake",
        ]),
    ],
    further=[
        '<a href="%s/an5.41/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.40.html">AN 5.40 &middot; Great Sal Trees</a> &mdash; the previous '
        "chapter's closing discourse, on a household's growth.",
        '<a href="an-5.42.html">AN 5.42 &middot; A True Person</a> &mdash; next, on the benefit a '
        "person brings simply by being born into a family.",
        '<a href="an-5.50.html">AN 5.50 &middot; With Nārada</a> &mdash; the chapter&rsquo;s '
        "closing discourse, naming King Muṇḍa this vagga is titled for.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.42 — Sappurisasutta
# --------------------------------------------------------------------------- #
page(
    42, "Sappurisa", "A True Person",
    vagga=VAGGA_5,
    meta_title="AN 5.42 — A True Person | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sappurisasutta — a true "
        "person born into a family benefits everyone connected to it, parents to ascetics, "
        "compared to a rain cloud that nourishes every crop it falls on. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single claim of benefit extended through six named groups, illustrated by "
                 "one simile, closing with verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The rain-cloud image for a beneficial person's widespread effect "
                              "recurs across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short, and companion to AN "
                       "5.41's account of what wealth is for"),
    ],
    why=(
        "Where AN 5.41 detailed how a true person uses wealth, this discourse states something "
        "broader and prior: a true person's mere existence in a family is already a benefit, "
        "before any wealth changes hands. Six groups are named as beneficiaries in turn &mdash; "
        "parents, children and partners, household staff, friends, and ascetics and brahmins "
        "&mdash; and the whole claim is compressed into one image: a great rain cloud, which "
        "nourishes every crop it falls on without needing to be asked."),
    guide=[
        ("The teaching in one sentence", [
            "A true person, born into a family, is for the benefit, welfare, and happiness of "
            "many people: their parents, children and partners, household staff, friends and "
            "colleagues, and ascetics and brahmins."]),
        ("Benefit prior to action", [
            "AN 5.41 concerned what a true person <em>does</em> with wealth. This discourse "
            "concerns what a true person simply <em>is</em>, once born into a family &mdash; the "
            "claim precedes any specific act of giving or support. Read together, the two "
            "discourses distinguish a person&rsquo;s existence as a source of benefit from their "
            "actions as a further, separate source, layered on top."]),
        ("A widening circle, named in order", [
            "The six beneficiaries move outward in a specific sequence: parents first, then "
            "children and partners, then household staff, then friends and colleagues, then "
            "ascetics and brahmins &mdash; from the most intimate relationships to the most "
            "public. The rain-cloud simile matches this widening: a cloud does not choose which "
            "crops to nourish, and neither does the benefit of a true person&rsquo;s presence "
            "stop at the household&rsquo;s edge."]),
        ("The verses' additional claim", [
            "The closing verses add something the prose does not state directly: that <em>the "
            "gods protect one who is guarded by principle</em>, and that someone learned, "
            "ethical, and steady in principle <em>doesn't lose their reputation</em>. The verses "
            "extend the discourse&rsquo;s claim from human beneficiaries to divine protection, "
            "and frame reputation itself as a natural consequence of steadiness rather than "
            "something separately pursued."]),
        ("Where this fits the chapter's arc", [
            "Between AN 5.41's account of wealth's proper use and AN 5.50's narrative of a "
            "king's grief, this discourse and the next several establish what a genuinely "
            "beneficial life and a genuinely satisfying one consist of &mdash; groundwork the "
            "chapter will need before it turns, at its close, to what cannot be secured by any "
            "of it."]),
    ],
    terms=[
        ("sappurisa",
         "&ldquo;true person, good person&rdquo; &mdash; this discourse's subject, already met "
         "as a term across earlier discourses in this chapter and nipāta."),
        ("atthāya hitāya sukhāya",
         "&ldquo;for the benefit, welfare, and happiness&rdquo; &mdash; the fixed triple phrase "
         "repeated for each of the six named groups."),
        ("mahāmegha",
         "&ldquo;great rain cloud&rdquo; &mdash; the discourse's central simile, chosen for "
         "nourishing every crop without needing to be asked."),
        ("dhammagutta",
         "&ldquo;guarded by principle&rdquo; &mdash; the closing verse's description of one "
         "whom the gods are said to protect."),
        ("bahussuta",
         "&ldquo;learned&rdquo; &mdash; one of three qualities, alongside ethics and steadiness, "
         "the verses say prevents a loss of reputation."),
    ],
    text_intro=(
        "The discourse in full: the six beneficiaries of a true person's presence, the rain-cloud "
        "simile, and the closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.42:1.1-1.6"),
        ("h3", "The rain cloud"),
        ("p", "&sect;2", "an5.42:2.1-2.7"),
        ("h3", "The closing verses"),
        ("p", "&sect;3", "an5.42:3.1-3.4"),
        ("p", "&sect;4", "an5.42:4.1-4.6"),
    ],
    quiz=[
        {"q": "What claim does this discourse make about a true person's existence, distinct from "
              "AN 5.41's claim?",
         "opts": [
             "That a true person must actively give wealth to benefit anyone",
             "That a true person's mere presence in a family is already a benefit, prior to any "
             "specific action",
             "That only wealthy people can be true persons",
             "That true persons benefit no one but themselves"],
         "correct": 1,
         "expl": "Existence as a source of benefit, distinguished from action as a further, separate source."},
        {"q": "What six groups does the discourse name as benefiting from a true person's "
              "presence?",
         "opts": [
             "Only monastics",
             "Parents, children and partners, household staff, friends and colleagues, and "
             "ascetics and brahmins",
             "Only the wealthy",
             "Only the king and his court"],
         "correct": 1,
         "expl": "A widening circle from the most intimate relationships to the most public."},
        {"q": "What does the rain-cloud simile illustrate?",
         "opts": [
             "That benefit is selective and must be earned",
             "That a true person nourishes everyone connected to them without needing to be asked, "
             "like a cloud nourishing every crop it falls on",
             "That rain is unpredictable and unreliable",
             "That wealth, not presence, is what actually matters"],
         "correct": 1,
         "expl": "An image chosen for its indiscriminate, widespread benefit."},
        {"q": "What does the closing verse add about divine protection?",
         "opts": [
             "Nothing; the verses only repeat the prose",
             "That the gods protect one who is guarded by principle",
             "That the gods are indifferent to human conduct",
             "That only kings receive divine protection"],
         "correct": 1,
         "expl": "An extension from human beneficiaries to divine protection, not stated in the prose."},
        {"q": "How does the guide frame this discourse's relationship to AN 5.41?",
         "opts": [
             "As unrelated, on a completely different topic",
             "As a companion discourse, establishing benefit prior to action where AN 5.41 "
             "concerned action itself",
             "As a direct contradiction of AN 5.41",
             "As a verbatim repeat of AN 5.41"],
         "correct": 1,
         "expl": "Existence and action treated as two layered sources of benefit."},
        {"q": "In what order are the six beneficiary groups named?",
         "opts": [
             "Randomly, with no discernible order",
             "From the most intimate relationships outward to the most public",
             "From wealthiest to poorest",
             "Alphabetically"],
         "correct": 1,
         "expl": "Parents first, ascetics and brahmins last — matching the rain cloud's widening reach."},
        {"q": "What three qualities does the closing verse say prevent a loss of reputation?",
         "opts": [
             "Wealth, beauty, and fame",
             "Being learned, having intact ethics, and being steady in principle",
             "Physical strength, courage, and cunning",
             "Royal favor, popularity, and luck"],
         "correct": 1,
         "expl": "Bahussuta, sīlavatūpapanna, and steadiness in dhamma."},
        {"q": "What does the guide say this discourse and its neighbors establish, ahead of the "
              "chapter's close?",
         "opts": [
             "Nothing relevant to the chapter's ending",
             "What a genuinely beneficial and satisfying life consists of, groundwork for what the "
             "chapter shows cannot be secured by any of it",
             "A direct preview of King Muṇḍa's grief",
             "A contradiction of the chapter's later material"],
         "correct": 1,
         "expl": "Groundwork the chapter needs before turning to its final theme."},
        {"q": "Is a specific act of wealth-giving required for the benefit this discourse "
              "describes?",
         "opts": [
             "Yes, wealth must always be given",
             "No — the benefit described is prior to and separate from any specific act",
             "Only for the sixth group, ascetics and brahmins",
             "The discourse does not address this question"],
         "correct": 1,
         "expl": "The claim concerns presence and character, not a specific transaction."},
        {"q": "Where is AN 5.42 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Rājagaha",
             "Vesālī"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Six beneficiaries", [
            "parents &middot; children/partners",
            "household staff",
            "friends &middot; ascetics",
        ]),
        ("The image", [
            "<span class=\"pali\">mahāmegha</span>",
            "&mdash; nourishes every crop,",
            "unasked",
        ]),
        ("Existence, then action", [
            "AN 5.42: presence itself",
            "AN 5.41: wealth's right use",
            "&mdash; two layered sources",
        ]),
        ("Cross-references", [
            "AN 5.41 &middot; wealth's proper use",
            "AN 5.43 &middot; next: what can't be prayed for",
            "AN 5.38 &middot; the banyan, a related image",
        ]),
    ],
    further=[
        '<a href="%s/an5.42/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.41.html">AN 5.41 &middot; Getting Rich</a> &mdash; the previous discourse, '
        "on wealth's five legitimate uses.",
        '<a href="an-5.43.html">AN 5.43 &middot; Likable</a> &mdash; next, on what is hard to get '
        "and why prayer alone can't secure it.",
        '<a href="an-5.38.html">AN 5.38 &middot; Faith</a> &mdash; the earlier banyan-tree image, '
        "sharing this discourse's picture of one person sheltering many.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.43 — Iṭṭhasutta
# --------------------------------------------------------------------------- #
page(
    43, "Iṭṭha", "Likable",
    vagga=VAGGA_5,
    meta_title="AN 5.43 — Likable | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Iṭṭhasutta — five "
        "things everyone wants and few get, and the Buddha's blunt claim that none of them come "
        "from praying or wishing, only from practicing the way that leads to each. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None restated, though the same Anāthapiṇḍika continues as questioner from "
                    "AN 5.41"),
        ("Speakers", "The householder Anāthapiṇḍika, addressed by the Buddha"),
        ("Form", "Five desired things named, a flat rejection of prayer as their cause, five "
                 "parallel formulas naming practice instead, closing with verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Rejecting supplication in favor of causal practice as the route to "
                              "desired outcomes is a recurring emphasis across the Chinese "
                              "Āgamas' treatment of karma; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a direct, almost "
                       "argumentative discourse against wishing as a method"),
    ],
    why=(
        "This discourse makes one of the most direct anti-magical-thinking arguments in the "
        "collection so far. Long life, beauty, happiness, fame, and heaven &mdash; five things "
        "everyone wants and few get &mdash; are named, and the Buddha states flatly that they "
        "are <em>not got by supplication or wishing for them</em>, adding the plainest possible "
        "reason: <em>if they were, who would lack them?</em> What follows is not resignation but "
        "redirection: five parallel instructions to practice the way that actually leads to each."),
    guide=[
        ("The teaching in one sentence", [
            "Long life, beauty, happiness, fame, and heaven are hard to get and are not obtained "
            "by praying, hoping, or pining for them; a noble disciple who wants any of them "
            "should instead practice the way that leads to it."]),
        ("An argument, not just an assertion", [
            "The Buddha does not simply state that prayer doesn't work; he gives a reason: "
            "<em>if they were [got by supplication], who would lack them?</em> Since these five "
            "things are visibly unevenly distributed &mdash; some people are long-lived, others "
            "are not, some famous, others not &mdash; and everyone presumably wishes for all "
            "five, the uneven distribution itself is offered as evidence that wishing is not the "
            "operative mechanism."]),
        ("Five parallel formulas, one structure", [
            "For each of the five, the identical three-part structure repeats: a noble disciple "
            "should not pray, hope, or pine for it; instead they should practice the way that "
            "leads to it; and by practicing that way, they gain it, as a god or a human. The "
            "discourse does not vary this structure once across all five applications, making it "
            "function as a general template for how any desired outcome should be pursued, not "
            "only these five specific ones."]),
        ("What the discourse does not specify", [
            "Notably, this discourse never states what &lsquo;the way that leads to&rsquo; long "
            "life, beauty, happiness, fame, or heaven actually consists of. That content has "
            "already been supplied elsewhere in this nipāta &mdash; AN 5.37's giving of food, for "
            "instance, was explicitly said to produce exactly these kinds of results. This "
            "discourse assumes that groundwork rather than repeating it, and states only the "
            "general principle: cause, not petition, produces effect."]),
        ("The closing verses' redefinition of &lsquo;astute&rsquo;", [
            "The verses close by defining <em>paṇḍita</em>, astute, not as clever or "
            "knowledgeable in the abstract but as someone who secures <em>both benefits</em> "
            "&mdash; the benefit in this life and in lives to come &mdash; through diligence in "
            "merit-making. Astuteness, on this account, is measured by effective practice, not by "
            "intellectual sophistication."]),
    ],
    terms=[
        ("iṭṭhā kantā manāpā dullabhā",
         "&ldquo;likable, desirable, agreeable, hard to get&rdquo; &mdash; the fourfold "
         "description opening the discourse, naming both the appeal and the scarcity of its five "
         "subjects."),
        ("āyācanahetu patthanāhetu",
         "&ldquo;by reason of supplication, by reason of wishing&rdquo; &mdash; the two causes "
         "explicitly ruled out as producing any of the five desired things."),
        ("saṁvattanikā paṭipadā",
         "&ldquo;the way that leads to it&rdquo; &mdash; the discourse's fixed phrase for the "
         "practice substituted for prayer, repeated identically five times."),
        ("dibba mānusa",
         "&ldquo;divine or human&rdquo; &mdash; the two forms of existence in which each of the "
         "five things is said to be gained through practice."),
        ("paṇḍita",
         "&ldquo;astute&rdquo; &mdash; redefined in the closing verse as one who secures both "
         "this-life and future-life benefit through diligence."),
    ],
    text_intro=(
        "The discourse in full: the five hard-to-get things, the rejection of prayer, and the "
        "five parallel instructions to practice instead, closing with verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.43:1.1"),
        ("h3", "Five hard-to-get things"),
        ("p", "&sect;2", "an5.43:2.1-2.8"),
        ("h3", "Not by prayer or wishing"),
        ("p", "&sect;3", "an5.43:3.1-3.2"),
        ("h3", "The way that leads to each"),
        ("p", "&sect;4", "an5.43:4.1-4.4"),
        ("p", "&sect;5", "an5.43:5.1-5.4"),
        ("p", "&sect;6", "an5.43:6.1-6.4"),
        ("p", "&sect;7", "an5.43:7.1-7.4"),
        ("p", "&sect;8", "an5.43:8.1-8.4"),
        ("h3", "The closing verses"),
        ("p", "&sect;9", "an5.43:9.1-9.4"),
        ("p", "&sect;10", "an5.43:10.1-10.4"),
        ("p", "&sect;11", "an5.43:11.1-11.4"),
    ],
    quiz=[
        {"q": "What five things does this discourse name as hard to get in the world?",
         "opts": [
             "Faith, ethics, learning, generosity, and wisdom",
             "Long life, beauty, happiness, fame, and heaven",
             "The five powers of a trainee",
             "Wealth, family, health, friends, and status"],
         "correct": 1,
         "expl": "Five broadly desired things, said to be hard to obtain."},
        {"q": "What does the Buddha explicitly say does NOT produce these five things?",
         "opts": [
             "Ethical conduct",
             "Supplication or wishing for them",
             "Practicing the appropriate way",
             "Generosity"],
         "correct": 1,
         "expl": "Prayer and hope are ruled out directly."},
        {"q": "What reasoning does the Buddha give for rejecting prayer as the cause?",
         "opts": [
             "No reasoning is given at all",
             "'If they were [got by supplication], who would lack them?' — since desired things "
             "are unevenly distributed despite everyone presumably wishing for them",
             "A quotation from an earlier teacher",
             "A prediction about future rebirths"],
         "correct": 1,
         "expl": "The uneven distribution of these five things is offered as evidence against wishing as the mechanism."},
        {"q": "What does the discourse instruct instead of praying or wishing?",
         "opts": [
             "Giving up on the desired outcome entirely",
             "Practicing the way that leads to that outcome",
             "Consulting an oracle",
             "Waiting passively for fate to decide"],
         "correct": 1,
         "expl": "The identical three-part structure — no prayer, practice instead, gain follows — repeats five times."},
        {"q": "Does this discourse specify exactly what practice leads to each of the five "
              "things?",
         "opts": [
             "Yes, in full detail for each",
             "No — it states only the general principle, assuming groundwork already supplied "
             "elsewhere in this nipāta, such as AN 5.37's giving of food",
             "It specifies only for long life",
             "It specifies only for heaven"],
         "correct": 1,
         "expl": "The general causal principle is stated; specific content comes from earlier discourses like AN 5.37."},
        {"q": "How does the closing verse redefine 'paṇḍita', astute?",
         "opts": [
             "As someone with the highest intelligence",
             "As someone who secures both this-life and future-life benefit through diligence in "
             "merit-making, not merely cleverness",
             "As someone born into a wealthy family",
             "As a synonym for arahant"],
         "correct": 1,
         "expl": "Astuteness measured by effective practice, not intellectual sophistication."},
        {"q": "Is this discourse an argument for resignation in the face of these five hard-to-get "
              "things?",
         "opts": [
             "Yes, it counsels giving up entirely",
             "No — it redirects toward practice rather than counseling either wishing or "
             "resignation",
             "Yes, it claims these things are entirely unattainable",
             "The discourse takes no position at all"],
         "correct": 1,
         "expl": "A redirection toward causal practice, not a counsel of despair."},
        {"q": "How many times does the identical three-part formula (no prayer, practice instead, "
              "gain follows) repeat across the discourse?",
         "opts": ["Once", "Twice", "Five times, once per desired thing", "Ten times"],
         "correct": 2,
         "expl": "One unvarying structure applied to long life, beauty, happiness, fame, and heaven in turn."},
        {"q": "In what two forms of existence does practice yield each of the five things?",
         "opts": [
             "Only as a human",
             "As a god or human (dibba vā mānusa vā)",
             "Only as a god",
             "As an animal"],
         "correct": 1,
         "expl": "The same two destinations named across several discourses in this chapter."},
        {"q": "Who does this discourse continue addressing from AN 5.41?",
         "opts": [
             "Princess Sumanā",
             "The householder Anāthapiṇḍika",
             "General Sīha",
             "King Muṇḍa"],
         "correct": 1,
         "expl": "The setting is not restated, but the same interlocutor continues."},
    ],
    marginalia=[
        ("Five hard-to-get things", [
            "long life &middot; beauty",
            "happiness &middot; fame",
            "heaven",
        ]),
        ("Not by wishing", [
            "&ldquo;if prayer worked,",
            "who would lack them?&rdquo;",
        ]),
        ("Practice, instead", [
            "<span class=\"pali\">saṁvattanikā paṭipadā</span>",
            "&mdash; the way that leads,",
            "repeated five times",
        ]),
        ("Cross-references", [
            "AN 5.37 &middot; the specific practice, for one case",
            "AN 5.42 &middot; a person's own benefit",
            "AN 5.44 &middot; next: the giver of the agreeable",
        ]),
    ],
    further=[
        '<a href="%s/an5.43/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.41.html">AN 5.41 &middot; Getting Rich</a> &mdash; the discourse this one '
        "continues from, addressed to the same householder.",
        '<a href="an-5.37.html">AN 5.37 &middot; Food</a> &mdash; the specific practice this '
        "discourse's general principle presupposes, for one of its five items.",
        '<a href="an-5.44.html">AN 5.44 &middot; Agreeable</a> &mdash; next, a vivid narrative '
        "instance of practice producing exactly what this discourse describes.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.44 — Manāpadāyīsutta
# --------------------------------------------------------------------------- #
page(
    44, "Manāpadāyī", "Agreeable",
    vagga=VAGGA_5,
    meta_title="AN 5.44 — Agreeable | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Manāpadāyīsutta — Ugga "
        "of Vesālī offers the Buddha six specific things he finds agreeable, catching himself "
        "before offering an improper couch, then returns after death as a god to confirm the "
        "principle held. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with the peaked roof, then Ugga's "
                    "own home; later, Jeta's Grove near Sāvatthī"),
        ("Speakers", "The householder Ugga of Vesālī, and later his own reborn self, a mind-made "
                     "god"),
        ("Form", "Six sequential offerings, each citing the same principle, one self-corrected "
                 "mid-offer, followed by the donor's death, rebirth, and return"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "Narratives of a lay donor's rebirth confirming the fruit of a "
                              "specific gift recur across the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; this chapter's most concrete "
                       "and narratively complete discourse, naming real foods and fabrics by "
                       "name"),
    ],
    why=(
        "This discourse illustrates AN 5.43's abstract principle &mdash; practice, not wishing, "
        "produces results &mdash; with the most specific and human episode this chapter offers. "
        "Ugga, a householder who has personally heard the Buddha say <em>the giver of the "
        "agreeable gets the agreeable</em>, offers six things he finds agreeable in turn: sal "
        "flower porridge, pork with jujube, fried vegetable stalks, fine rice, imported cloth, "
        "and finally &mdash; catching himself &mdash; not his own luxurious couch, which he "
        "knows is improper for the Buddha to accept, but an extremely valuable sandalwood plank "
        "instead."),
    guide=[
        ("The teaching in one sentence", [
            "Citing what he has personally heard the Buddha say &mdash; the giver of the "
            "agreeable gets the agreeable &mdash; Ugga offers six things he finds agreeable in "
            "turn, and after his death is reborn as a god who confirms that everything happened "
            "just as he wished."]),
        ("Six offerings, named specifically", [
            "Nothing about this discourse is abstract. Sal flower porridge, pork with jujube, "
            "fried vegetable stalks, boiled fine rice with the dark grains picked out, cloths "
            "imported from Kāsi &mdash; each named plainly, each offered with the identical "
            "formula: <em>this is agreeable to me; may the Buddha please accept it out of "
            "sympathy</em>. The specificity is the point; this is not a discourse about giving in "
            "the abstract but about one donor's actual, named possessions."]),
        ("The sixth offering, and Ugga's own correction", [
            "Ugga's sixth offer begins with an elaborate couch &mdash; woolen covers, deer hide, "
            "a canopy, red pillows &mdash; and then he stops himself: <em>but, sir, I know that "
            "this is not proper for the Buddha</em>. Without being corrected by anyone, Ugga "
            "recognizes the mismatch between what he finds agreeable and what a mendicant may "
            "accept, and substitutes a sandalwood plank worth, the text says, over a thousand "
            "dollars. This moment of self-aware adjustment, offered by the donor himself rather "
            "than prompted by the Buddha, is worth noticing as a small but genuine act of "
            "discernment about what generosity should actually take the form of."]),
        ("Death, rebirth, and confirmation", [
            "The discourse does not end with the meal. Some time later Ugga dies and is reborn "
            "<em>as a host of mind-made gods</em>, and returns, glowing, to visit the Buddha at "
            "Sāvatthī. The Buddha asks directly, <em>I trust it is all you wished?</em>, and "
            "Ugga answers, just as directly, <em>it is indeed just as I wished</em>. The claim "
            "made at the discourse's opening is not left as doctrine alone; it is tested against "
            "an actual outcome, reported by the person it happened to."]),
        ("The verses' escalation", [
            "The Buddha's closing verses to the godling escalate the principle stated to Ugga in "
            "life: <em>the giver of the foremost gets the foremost, the giver of the excellent "
            "gets the excellent, the giver of the best gets the best</em>. What began as a claim "
            "about matching an ordinary preference &mdash; agreeable food gets agreeable results "
            "&mdash; is restated as a claim about quality generally: the standard of what is "
            "given is said to set the standard of what is received."]),
    ],
    terms=[
        ("manāpadāyī labhate manāpaṁ",
         "&ldquo;the giver of the agreeable gets the agreeable&rdquo; &mdash; the principle Ugga "
         "cites at the opening of every one of his six offerings."),
        ("anukampaṁ upādāya",
         "&ldquo;out of sympathy&rdquo; &mdash; the phrase describing why the Buddha accepts each "
         "gift, framing acceptance as a kindness to the giver rather than a need on his own part."),
        ("netaṁ bhagavato kappati",
         "&ldquo;this is not proper for the Buddha&rdquo; &mdash; Ugga&rsquo;s own words, "
         "recognizing unprompted that his couch is inappropriate to offer."),
        ("manomaya kāya",
         "&ldquo;mind-made body&rdquo; &mdash; the form of rebirth Ugga takes after death, "
         "returning to confirm the discourse's opening claim in person."),
        ("aggadāyī",
         "&ldquo;giver of the foremost&rdquo; &mdash; the escalated principle in the closing "
         "verses, generalizing from agreeable food to quality generally."),
    ],
    text_intro=(
        "The discourse in full: Ugga's six offerings, his own correction before the sixth, the "
        "Buddha's verses, and Ugga's return after death to confirm the outcome. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Ugga's home"),
        ("p", "&sect;1", "an5.44:1.1-1.2"),
        ("h3", "The first offering: porridge"),
        ("p", "&sect;2", "an5.44:1.3-2.5"),
        ("h3", "The second offering: pork with jujube"),
        ("p", "&sect;3", "an5.44:3.1-3.5"),
        ("h3", "The third offering: fried vegetables"),
        ("p", "&sect;4", "an5.44:4.1-4.5"),
        ("h3", "The fourth offering: fine rice"),
        ("p", "&sect;5", "an5.44:5.1-5.5"),
        ("h3", "The fifth offering: Kāsi cloth"),
        ("p", "&sect;6", "an5.44:6.1-6.5"),
        ("h3", "The sixth offering, corrected"),
        ("p", "&sect;7", "an5.44:7.1-7.9"),
        ("h3", "The Buddha's verses of appreciation"),
        ("p", "&sect;8", "an5.44:8.1-8.4"),
        ("p", "&sect;9", "an5.44:9.1-9.4"),
        ("p", "&sect;10", "an5.44:10.1"),
        ("h3", "Ugga's return, as a god"),
        ("p", "&sect;11", "an5.44:11.1-11.3"),
        ("p", "&sect;12", "an5.44:11.4-11.6"),
        ("p", "&sect;13", "an5.44:11.7"),
        ("h3", "The Buddha's final verses"),
        ("p", "&sect;14", "an5.44:12.1-12.4"),
        ("p", "&sect;15", "an5.44:13.1-13.4"),
    ],
    quiz=[
        {"q": "What principle does Ugga cite before every one of his offerings?",
         "opts": [
             "That giving guarantees enlightenment",
             "'The giver of the agreeable gets the agreeable', which he says he heard directly "
             "from the Buddha",
             "That only wealthy donors receive good rebirths",
             "That food offerings are worthless"],
         "correct": 1,
         "expl": "A principle he explicitly attributes to hearing it in the Buddha's own presence."},
        {"q": "What does Ugga do differently with his sixth offering compared to the first five?",
         "opts": [
             "He offers nothing at all",
             "He begins to describe an elaborate couch, then catches himself, recognizing it is "
             "not proper for the Buddha, and substitutes a sandalwood plank instead",
             "He refuses to let the Buddha accept it",
             "He offers exactly the same item as before"],
         "correct": 1,
         "expl": "Self-aware correction, offered by the donor himself without prompting."},
        {"q": "What happens to Ugga after this discourse's meal scene?",
         "opts": [
             "Nothing further is recorded",
             "He dies some time later and is reborn as a host of mind-made gods, then returns to "
             "visit the Buddha",
             "He becomes a mendicant immediately",
             "He loses his wealth"],
         "correct": 1,
         "expl": "The discourse follows him through death and rebirth to confirm its own claim."},
        {"q": "What does the Buddha ask the reborn Ugga, and how does Ugga answer?",
         "opts": [
             "'Do you regret your generosity?' — 'Yes, deeply'",
             "'I trust it is all you wished?' — 'It is indeed just as I wished'",
             "'Who are you?' — Ugga does not answer",
             "The Buddha asks nothing at all"],
         "correct": 1,
         "expl": "A direct confirmation of the outcome, reported by the person it happened to."},
        {"q": "How do the Buddha's final verses escalate the principle from earlier in the "
              "discourse?",
         "opts": [
             "They contradict the earlier principle",
             "They generalize from agreeable food specifically to quality generally — the giver "
             "of the foremost, excellent, and best gets the same in return",
             "They abandon the topic of giving entirely",
             "They apply only to Ugga personally, with no wider claim"],
         "correct": 1,
         "expl": "From matching an ordinary preference to a broader claim about quality and outcome."},
        {"q": "What items does Ugga offer across his first five offerings?",
         "opts": [
             "Only money",
             "Sal flower porridge, pork with jujube, fried vegetable stalks, fine rice, and cloths "
             "imported from Kāsi",
             "Only monastic robes",
             "Only medicine"],
         "correct": 1,
         "expl": "Specific, named items, not abstract categories of gift."},
        {"q": "What phrase describes why the Buddha accepts each of Ugga's gifts?",
         "opts": [
             "Because he is hungry",
             "'Anukampaṁ upādāya', out of sympathy — framing acceptance as a kindness to the "
             "giver",
             "Because refusal would be rude",
             "The discourse gives no reason"],
         "correct": 1,
         "expl": "Acceptance framed as generosity toward the donor, not need on the recipient's part."},
        {"q": "How does this discourse relate to AN 5.43's abstract principle about prayer and "
              "practice?",
         "opts": [
             "It contradicts AN 5.43 entirely",
             "It illustrates AN 5.43's principle with a specific, human, narratively complete "
             "episode",
             "It has no relation to AN 5.43",
             "It repeats AN 5.43 word for word"],
         "correct": 1,
         "expl": "A concrete instance of practice, not wishing, producing a matching result."},
        {"q": "What form does Ugga's rebirth take?",
         "opts": [
             "Rebirth as a human of low status",
             "A mind-made body (manomaya kāya) among a host of gods",
             "Rebirth as an animal",
             "No rebirth is described"],
         "correct": 1,
         "expl": "A specific, named form of divine rebirth."},
        {"q": "Where does the Buddha meet the reborn Ugga?",
         "opts": [
             "Still in Vesālī",
             "At Sāvatthī, in Jeta's Grove, where Ugga arrives at night, lighting up the entire "
             "grove",
             "In a dream",
             "At the royal palace"],
         "correct": 1,
         "expl": "A new setting, marking the passage of time and Ugga's changed circumstances."},
    ],
    marginalia=[
        ("Six offerings", [
            "porridge &middot; pork",
            "vegetables &middot; rice",
            "cloth &middot; (couch, corrected)",
            "&rarr; sandalwood plank",
        ]),
        ("Self-caught", [
            "&ldquo;this is not",
            "proper for the Buddha&rdquo;",
            "&mdash; unprompted",
        ]),
        ("Confirmed after death", [
            "&ldquo;just as I wished&rdquo;",
            "&mdash; a mind-made god,",
            "returning to report",
        ]),
        ("Cross-references", [
            "AN 5.43 &middot; the principle, stated",
            "AN 5.37 &middot; giving food, its own fruits",
            "AN 5.45 &middot; next: merit as an ocean",
        ]),
    ],
    further=[
        '<a href="%s/an5.44/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.43.html">AN 5.43 &middot; Likable</a> &mdash; the previous discourse, '
        "stating the principle this one puts into practice.",
        '<a href="an-5.37.html">AN 5.37 &middot; Food</a> &mdash; the earlier account of what '
        "food-giving specifically confers.",
        '<a href="an-5.45.html">AN 5.45 &middot; Overflowing Merit</a> &mdash; next, on merit too '
        "vast to measure, even for gifts far smaller than Ugga&rsquo;s.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.45 — Puññābhisandasutta
# --------------------------------------------------------------------------- #
page(
    45, "Puññābhisanda", "Overflowing Merit",
    vagga=VAGGA_5,
    meta_title="AN 5.45 — Overflowing Merit | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Puññābhisandasutta — "
        "when a mendicant enjoys a gift while dwelling in limitless immersion of heart, the "
        "donor's merit becomes as impossible to measure as the ocean's water. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five requisites named in turn, each tied to the recipient's own meditative "
                 "state, followed by an ocean simile and verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The ocean-of-merit image for immeasurable generosity is widely "
                              "attested across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a genuinely interesting "
                       "mechanism connecting a donor's merit to the recipient's own practice"),
    ],
    why=(
        "After Ugga's vivid, itemized generosity at AN 5.44, this discourse states a mechanism "
        "that changes what any gift, however modest, can become. When a mendicant uses a robe, "
        "almsfood, lodging, a bed or chair, or medicine while dwelling in <em>limitless "
        "immersion of heart</em>, the donor's resulting merit is said to be limitless too "
        "&mdash; not because of the gift's size, but because of the recipient's own meditative "
        "state at the moment of use."),
    guide=[
        ("The teaching in one sentence", [
            "When a mendicant enters and remains in limitless immersion of heart while using a "
            "robe, almsfood, lodging, a bed or chair, or medicine, the overflowing merit for the "
            "donor of that gift is limitless."]),
        ("Merit tied to the recipient's state, not the gift's size", [
            "This is a distinctive mechanism among this chapter's giving discourses. AN 5.37 tied "
            "food-giving to five specific returned qualities regardless of the recipient's "
            "meditative state; this discourse ties merit&rsquo;s scale directly to whether the "
            "recipient is, at the moment of use, dwelling in <em>appamāṇaṁ cetosamādhiṁ</em>, "
            "limitless immersion of heart &mdash; almost certainly the boundless meditations on "
            "love, compassion, joy, and equanimity extended without limit. The donor cannot "
            "control this directly; their merit depends in part on a state only the recipient "
            "produces."]),
        ("Five requisites, one formula", [
            "The five items &mdash; robe, almsfood, lodging, bed or chair, and medicine &mdash; "
            "are the standard monastic requisites named repeatedly across this collection. The "
            "discourse applies the identical formula to all five without variation, meaning the "
            "mechanism does not privilege one kind of gift over another; whichever requisite is "
            "used while the recipient dwells in limitless immersion produces the same limitless "
            "result."]),
        ("An ocean, not a container", [
            "The simile is deliberately chosen for its resistance to measurement: trying to say "
            "how many gallons the ocean holds is futile, and the discourse insists merit of this "
            "kind is the same &mdash; not simply large, but <em>asaṅkheyyo appameyyo</em>, "
            "incalculable and immeasurable, a category error to even attempt counting rather "
            "than a very big but countable number."]),
        ("The verses' river image", [
            "The closing verses extend the ocean image with rivers flowing into it from every "
            "direction, carrying merit toward the giver the way water reaches the sea "
            "&ldquo;as the rivers bring their waters to the sea.&rdquo; The image adds a "
            "directional claim the prose does not: merit is not static once produced, but "
            "continues moving toward the person who gave rise to it."]),
    ],
    terms=[
        ("puññābhisanda",
         "&ldquo;overflowing merit&rdquo; &mdash; this discourse's title, an image of merit "
         "exceeding any container built to hold it."),
        ("appamāṇaṁ cetosamādhiṁ",
         "&ldquo;limitless immersion of heart&rdquo; &mdash; the recipient's meditative state "
         "this discourse ties the donor's merit to, likely the boundless meditations extended "
         "without limit."),
        ("paribhuñjamāna",
         "&ldquo;while using&rdquo; &mdash; the verb marking the moment merit is generated: not "
         "at the moment of giving, but at the moment of the recipient's use."),
        ("asaṅkheyyo appameyyo",
         "&ldquo;incalculable, immeasurable&rdquo; &mdash; the discourse's description of merit "
         "at this scale, a category rather than a very large quantity."),
        ("mahāpuññakkhandha",
         "&ldquo;great mass of merit&rdquo; &mdash; the discourse's closing reckoning, echoing "
         "the ocean's own &lsquo;great mass of water&rsquo;."),
    ],
    text_intro=(
        "The discourse in full: the five requisites tied to limitless immersion, the ocean "
        "simile, and the closing verses on rivers reaching the sea. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.45:1.1"),
        ("h3", "Five requisites, one formula"),
        ("p", "&sect;2", "an5.45:2.2"),
        ("p", "&sect;3", "an5.45:4.1-4.2"),
        ("h3", "An ocean of merit"),
        ("p", "&sect;4", "an5.45:5.1-5.3"),
        ("p", "&sect;5", "an5.45:6.1-6.3"),
        ("p", "&sect;6", "an5.45:6.4-6.6"),
        ("h3", "The closing verses"),
        ("p", "&sect;7", "an5.45:7.1-7.4"),
        ("p", "&sect;8", "an5.45:8.1-8.4"),
    ],
    quiz=[
        {"q": "What condition does this discourse say ties a donor's merit to being limitless?",
         "opts": [
             "The size or expense of the gift",
             "The recipient dwelling in limitless immersion of heart while using the gift",
             "The number of gifts given",
             "The donor's own social status"],
         "correct": 1,
         "expl": "Merit's scale is tied to the recipient's meditative state at the moment of use."},
        {"q": "What five requisites does this discourse apply its formula to?",
         "opts": [
             "Food, water, shelter, clothing, and money",
             "Robe, almsfood, lodging, a bed or chair, and medicine",
             "Only robes",
             "Only medicine for the sick"],
         "correct": 1,
         "expl": "The standard monastic requisites, applied identically without variation."},
        {"q": "How does this discourse's mechanism differ from AN 5.37's account of giving food?",
         "opts": [
             "They are identical mechanisms",
             "AN 5.37 tied five specific returns to giving regardless of the recipient's state; "
             "this discourse ties merit's scale specifically to the recipient's meditative state",
             "This discourse rejects AN 5.37 entirely",
             "Neither discourse concerns merit at all"],
         "correct": 1,
         "expl": "A distinctive mechanism where the recipient's own practice, not just the gift, shapes the outcome."},
        {"q": "What does the ocean simile emphasize about merit at this scale?",
         "opts": [
             "That it is simply a very large but countable number",
             "That it is incalculable and immeasurable — a category error to attempt counting, "
             "like trying to measure the ocean in gallons",
             "That merit of this kind is actually quite small",
             "That the ocean has no relevance to merit at all"],
         "correct": 1,
         "expl": "Asaṅkheyyo appameyyo — not merely large, but resistant to quantification in principle."},
        {"q": "What does the closing verse's river image add to the ocean simile?",
         "opts": [
             "Nothing new",
             "A directional claim — merit continues moving toward the giver, like rivers carrying "
             "water to the sea",
             "That rivers are more important than the ocean",
             "A warning against giving too much"],
         "correct": 1,
         "expl": "Merit is not static once produced but keeps flowing toward its source."},
        {"q": "At what moment does this discourse say merit is actually generated?",
         "opts": [
             "At the moment the gift is handed over",
             "At the moment of the recipient's use (paribhuñjamāna), while dwelling in limitless "
             "immersion",
             "Only after the recipient dies",
             "The discourse does not specify a moment"],
         "correct": 1,
         "expl": "Use, not the act of giving itself, is when the described merit arises."},
        {"q": "Can a donor directly control whether this discourse's limitless merit arises?",
         "opts": [
             "Yes, entirely, through the size of the gift",
             "Not directly — it depends in part on a meditative state only the recipient produces",
             "Yes, by choosing a particularly holy recipient",
             "The discourse says merit is entirely random"],
         "correct": 1,
         "expl": "A mechanism partly outside the donor's own control."},
        {"q": "What likely meditative practice does 'appamāṇaṁ cetosamādhiṁ' refer to?",
         "opts": [
             "Walking meditation",
             "Almost certainly the boundless meditations on love, compassion, joy, and equanimity, "
             "extended without limit",
             "A single-pointed concentration on the breath only",
             "Recollection of past lives"],
         "correct": 1,
         "expl": "The guide's best reading of this specific technical phrase."},
        {"q": "Is the formula varied at all across the five requisites?",
         "opts": [
             "Yes, each requisite has its own distinct formula",
             "No — the identical formula applies without variation to all five",
             "Only medicine differs from the others",
             "Only robes differ from the others"],
         "correct": 1,
         "expl": "No privileging of one requisite over another."},
        {"q": "Where is AN 5.45 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five requisites", [
            "robe &middot; almsfood",
            "lodging &middot; bed/chair",
            "medicine",
        ]),
        ("The trigger", [
            "<span class=\"pali\">appamāṇaṁ cetosamādhiṁ</span>",
            "&mdash; limitless immersion,",
            "at the moment of use",
        ]),
        ("Not a number", [
            "<span class=\"pali\">asaṅkheyyo appameyyo</span>",
            "&mdash; incalculable,",
            "like ocean water",
        ]),
        ("Cross-references", [
            "AN 5.44 &middot; a vivid, itemized gift",
            "AN 5.37 &middot; a different mechanism",
            "AN 5.46 &middot; next: five accomplishments",
        ]),
    ],
    further=[
        '<a href="%s/an5.45/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.44.html">AN 5.44 &middot; Agreeable</a> &mdash; the previous discourse, on '
        "one donor's own itemized generosity.",
        '<a href="an-5.37.html">AN 5.37 &middot; Food</a> &mdash; the earlier, differently '
        "structured account of what a specific gift confers.",
        '<a href="an-5.46.html">AN 5.46 &middot; Success</a> &mdash; next, a bare five-item list '
        "this chapter will expand in full at AN 5.47.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.46 — Sampadāsutta
# --------------------------------------------------------------------------- #
page(
    46, "Sampadā", "Success",
    vagga=VAGGA_5,
    meta_title="AN 5.46 — Success | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sampadāsutta — five "
        "accomplishments named in a single bare sentence: faith, ethics, learning, generosity, "
        "and wisdom, expanded in full at the very next discourse. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five accomplishments, with no elaboration"),
        ("Length", "~15 seconds to read"),
        ("Northern parallel", "Faith, ethics, learning, generosity, and wisdom as a fixed lay "
                              "virtue set are widely attested across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the chapter's shortest "
                       "discourse, functioning as a bare-list companion to the one after it"),
    ],
    why=(
        "This is the shortest discourse in the chapter so far, and its brevity is deliberate: it "
        "names five accomplishments in a single sentence and stops, in the same "
        "<em>saṅkhitta</em>-then-<em>vitthata</em> pattern already used twice in this nipāta, at "
        "AN 5.1&ndash;2 and AN 5.13&ndash;14. AN 5.47, the very next discourse, will take this "
        "identical five-item list and define each item in full."),
    guide=[
        ("The teaching in one sentence", [
            "There are five accomplishments: faith, ethics, learning, generosity, and wisdom."]),
        ("A list already met, under two other names", [
            "<em>Saddhā, sīla, suta, cāga, paññā</em> is not new material. AN 5.40 closed the "
            "previous chapter with the identical five items, calling them a family's growth; this "
            "discourse calls them <em>sampadā</em>, accomplishments, applying the same five items "
            "to an individual rather than a household. The content does not change; only the "
            "frame does."]),
        ("Brief now, detailed next", [
            "As at AN 5.1 and AN 5.13, a bare list precedes its own expansion by exactly one "
            "discourse. This reading guide has already explained why the collection favors this "
            "pairing &mdash; a chanted formula gains from being stated compactly before being "
            "unpacked, giving reciters both a compressed anchor and a fuller version to draw on. "
            "That explanation is not repeated here."]),
        ("What five accomplishments implies, compared to five kinds of wealth", [
            "AN 5.47's own title, <em>Dhana</em>, wealth, frames the identical five items "
            "differently again &mdash; not as accomplishments achieved but as a kind of "
            "possession held. Two discourses, back to back, offer two different metaphors "
            "&mdash; achievement and possession &mdash; for what is, item by item, the same "
            "five-part list."]),
    ],
    terms=[
        ("sampadā",
         "&ldquo;accomplishment, success&rdquo; &mdash; this discourse's frame for the five "
         "items, distinct from AN 5.40's &lsquo;growth&rsquo; and AN 5.47's &lsquo;wealth&rsquo;."),
        ("saddhāsampadā",
         "&ldquo;accomplishment in faith&rdquo; &mdash; the first item, to be defined in full at "
         "AN 5.47 by the standard nine-quality formula."),
        ("cāgasampadā",
         "&ldquo;accomplishment in generosity&rdquo; &mdash; the fourth item, paired with "
         "learning as one of two qualities not used in any earlier power list in this nipāta."),
        ("paññāsampadā",
         "&ldquo;accomplishment in wisdom&rdquo; &mdash; the fifth item, to receive the same "
         "narrow insight-definition already used for wisdom throughout this nipāta."),
        ("saṅkhitta",
         "&ldquo;in brief&rdquo; &mdash; not this discourse's own title, but the structural role "
         "it plays, matching AN 5.1 and AN 5.13's opening pattern."),
    ],
    text_intro=(
        "The discourse in full: five accomplishments, named once. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.46:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five accomplishments does this discourse name?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Faith, ethics, learning, generosity, and wisdom",
             "The five powers of a trainee",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "Saddhā, sīla, suta, cāga, paññā."},
        {"q": "Where has this identical five-item list already appeared in this series?",
         "opts": [
             "Nowhere before this page",
             "AN 5.40, closing the previous chapter, calling the same five items a family's growth",
             "AN 5.1",
             "AN 4.163"],
         "correct": 1,
         "expl": "The same content, applied there to a household rather than an individual."},
        {"q": "What structural pattern does this discourse's brevity match?",
         "opts": [
             "No pattern; it is unique",
             "The saṅkhitta-then-vitthata pairing already used at AN 5.1–2 and AN 5.13–14",
             "The disrespect-qualifier pattern from AN 5.9–10",
             "The peyyāla compression pattern"],
         "correct": 1,
         "expl": "A bare list preceding its own expansion by exactly one discourse, for the third time in this nipāta."},
        {"q": "What does AN 5.47, the very next discourse, do with this list?",
         "opts": [
             "Nothing further; the list is dropped",
             "Defines each of the five items in full",
             "Replaces the list entirely",
             "Returns to the sekhabala"],
         "correct": 1,
         "expl": "The detailed companion this discourse's brevity anticipates."},
        {"q": "How does AN 5.47's title reframe the same five items?",
         "opts": [
             "Identically to this discourse",
             "As 'dhana', wealth — a kind of possession held, rather than an accomplishment "
             "achieved",
             "As a warning against materialism",
             "As a list of hindrances"],
         "correct": 1,
         "expl": "Two consecutive discourses, two different metaphors for the same five-part content."},
        {"q": "Which two of the five items does the guide note have not appeared in any earlier "
              "power list in this nipāta?",
         "opts": [
             "Faith and wisdom",
             "Learning and generosity",
             "Ethics and faith",
             "None; all five have appeared identically before"],
         "correct": 1,
         "expl": "Suta and cāga, distinct from the sekhabala and standard bala lists used earlier."},
        {"q": "How long is this discourse?",
         "opts": [
             "Several minutes, with an extended simile",
             "About fifteen seconds — a single sentence with no elaboration",
             "Identical in length to AN 5.44",
             "This discourse has no readable text"],
         "correct": 1,
         "expl": "The shortest discourse in the chapter so far."},
        {"q": "Does this discourse offer any definition of the five accomplishments it names?",
         "opts": [
             "Yes, in full detail",
             "No — none at all, consistent with the bare-list pattern already seen twice",
             "Only faith is defined",
             "Only wisdom is defined"],
         "correct": 1,
         "expl": "Definition is left entirely to the following discourse."},
        {"q": "What role does brevity play in a chanted, orally transmitted formula, according to "
              "the guide's earlier explanation?",
         "opts": [
             "It has no functional role, purely decorative",
             "A compact anchor that reciters can pair with a fuller version, already explained at "
             "earlier bare-list discourses in this series",
             "It indicates the material is less important",
             "It is a copying error"],
         "correct": 1,
         "expl": "An explanation given fully elsewhere and not repeated here."},
        {"q": "Where is AN 5.46 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five accomplishments", [
            "faith &middot; ethics",
            "learning &middot; generosity",
            "wisdom",
        ]),
        ("Same five, three frames", [
            "AN 5.40: a family's growth",
            "AN 5.46: accomplishment",
            "AN 5.47: wealth",
        ]),
        ("Brief, then detailed", [
            "third time in this nipāta",
            "&mdash; AN 5.1&ndash;2,",
            "5.13&ndash;14, now this",
        ]),
        ("Cross-references", [
            "AN 5.40 &middot; the same five, first",
            "AN 5.47 &middot; next: in full",
            "AN 5.1 &amp; 5.13 &middot; the earlier pairs",
        ]),
    ],
    further=[
        '<a href="%s/an5.46/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.40.html">AN 5.40 &middot; Great Sal Trees</a> &mdash; where this identical '
        "five-item list first appeared, applied to a household.",
        '<a href="an-5.47.html">AN 5.47 &middot; Wealth</a> &mdash; next, this discourse&rsquo;s '
        "full-detail companion.",
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; the first use of this exact '
        "brief-then-detailed pairing in this nipāta.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.47 — Dhanasutta
# --------------------------------------------------------------------------- #
page(
    47, "Dhana", "Wealth",
    vagga=VAGGA_5,
    meta_title="AN 5.47 — Wealth | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dhanasutta — AN 5.46's "
        "five accomplishments defined in full and reframed as wealth: faith, ethics, learning, "
        "generosity, and wisdom, none of it able to be confiscated or lost by force. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The same five named again, then each defined in turn, closing with verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Faith, ethics, learning, generosity, and wisdom framed as an "
                              "inalienable wealth recur across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the detailed companion to AN "
                       "5.46, reusing several definitions already given elsewhere in this nipāta"),
    ],
    why=(
        "AN 5.46 promised nothing and delivered five bare names. This discourse keeps that "
        "promise, defining faith, ethics, learning, generosity, and wisdom one at a time, and "
        "then makes an argument its title only implies: calling these five qualities "
        "<em>dhana</em>, wealth, is not simply metaphorical decoration. The closing verses "
        "state directly that whoever has this wealth is <em>adaliddo</em>, not poor, "
        "regardless of what they hold in the ordinary sense."),
    guide=[
        ("The teaching in one sentence", [
            "The wealth of faith, ethics, learning, generosity, and wisdom are five kinds of "
            "wealth, each defined in turn, and whoever has them is said to be truly prosperous, "
            "their life not lived in vain."]),
        ("Three definitions inherited without change", [
            "Faith (the nine-quality recollection of the Buddha) and wisdom (insight into "
            "arising and passing away) are worded here exactly as they have been worded every "
            "other time this nipāta has defined them. Ethics, too, is given as the standard five "
            "precepts. This discourse adds no new content to any of these three; a reader who "
            "has met them before can move through these paragraphs quickly, checking only that "
            "the wording matches."]),
        ("Learning, defined by retention and grasp", [
            "The wealth of learning is defined as being <em>bahussuta</em>, very learned, "
            "<em>remembering and keeping</em> teachings that are good in the beginning, middle, "
            "and end, and being able to recite them, scrutinize them mentally, and "
            "<em>penetrate them theoretically</em>. This is a fuller definition of learning than "
            "any earlier discourse in this nipāta has given, marking it as more than passive "
            "exposure to teaching &mdash; active retention and comprehension are both required."]),
        ("Generosity, defined by disposition", [
            "The wealth of generosity is defined not by any specific act of giving but by an "
            "ongoing disposition: living <em>rid of the stain of stinginess</em>, "
            "<em>freely generous, open-handed, loving to let go</em>. Where AN 5.36's timely "
            "gifts and AN 5.37's food-giving concerned specific acts, this definition concerns "
            "the character a person carries into every occasion for giving, whether or not any "
            "particular gift happens."]),
        ("Wealth that cannot be confiscated", [
            "The metaphor's real force becomes clear against AN 5.41's third reason to get "
            "rich: legitimate wealth protects against loss from fire, water, kings, bandits, or "
            "unloved heirs. This fivefold wealth needs no such protection, since none of the "
            "five items named &mdash; faith, ethics, learning, generosity, wisdom &mdash; can be "
            "seized, burned, flooded, or inherited away from the person who holds them. The "
            "discourse does not state this contrast explicitly, but it is available to a reader "
            "who has read AN 5.41 already."]),
    ],
    terms=[
        ("dhana",
         "&ldquo;wealth&rdquo; &mdash; this discourse's frame for the five qualities, chosen "
         "deliberately against the vulnerability of ordinary wealth named at AN 5.41."),
        ("bahussuta",
         "&ldquo;very learned&rdquo; &mdash; the wealth of learning, defined here more fully "
         "than any earlier discourse in this nipāta, requiring both retention and comprehension."),
        ("muttacāgo payatapāṇi",
         "&ldquo;loving to let go, open-handed&rdquo; &mdash; part of the wealth of "
         "generosity's definition, an ongoing character trait rather than a single act."),
        ("adaliddo",
         "&ldquo;not poor&rdquo; &mdash; the closing verse's direct claim for whoever holds this "
         "fivefold wealth, regardless of ordinary material circumstances."),
        ("amoghaṁ jīvitaṁ",
         "&ldquo;a life not in vain&rdquo; &mdash; the verse's further claim, tying this wealth "
         "to a life's basic worth rather than only its comfort."),
    ],
    text_intro=(
        "The discourse in full: the five kinds of wealth named again, then each defined in turn, "
        "closing with verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five kinds of wealth, named again"),
        ("p", "&sect;1", "an5.47:1.1-1.3"),
        ("h3", "The wealth of faith"),
        ("p", "&sect;2", "an5.47:2.1-2.4"),
        ("h3", "The wealth of ethics"),
        ("p", "&sect;3", "an5.47:3.1-3.3"),
        ("h3", "The wealth of learning"),
        ("p", "&sect;4", "an5.47:4.1-4.3"),
        ("h3", "The wealth of generosity"),
        ("p", "&sect;5", "an5.47:5.1-5.3"),
        ("h3", "The wealth of wisdom"),
        ("p", "&sect;6", "an5.47:6.1-6.4"),
        ("h3", "The closing verses"),
        ("p", "&sect;7", "an5.47:7.1-7.4"),
        ("p", "&sect;8", "an5.47:8.1-8.4"),
        ("p", "&sect;9", "an5.47:9.1-9.4"),
    ],
    quiz=[
        {"q": "How are faith, ethics, and wisdom defined in this discourse compared to elsewhere "
              "in this nipāta?",
         "opts": [
             "Completely differently, with new formulas",
             "Identically — the same nine-quality faith formula, the five precepts, and the same "
             "insight-wisdom formula",
             "Faith and wisdom are new; only ethics is unchanged",
             "This discourse gives no definitions at all"],
         "correct": 1,
         "expl": "Three of the five terms receive the identical treatment given every earlier time this nipāta defined them."},
        {"q": "How is the wealth of learning defined?",
         "opts": [
             "As simply having heard many teachings, with no further requirement",
             "As being very learned, remembering and keeping teachings, and reciting, scrutinizing, "
             "and penetrating them theoretically — more fully than any earlier discourse in this "
             "nipāta",
             "As identical to the wealth of wisdom",
             "As a synonym for ethics"],
         "correct": 1,
         "expl": "Active retention and comprehension, not passive exposure."},
        {"q": "How is the wealth of generosity defined?",
         "opts": [
             "By a single specific act of giving",
             "By an ongoing disposition — rid of stinginess, freely generous, open-handed, loving "
             "to let go — rather than any particular gift",
             "By the total monetary value given over a lifetime",
             "By generosity shown only to monastics"],
         "correct": 1,
         "expl": "Character carried into every occasion, distinct from AN 5.36 and 5.37's focus on specific acts."},
        {"q": "What contrast does the guide draw between this discourse's wealth and AN 5.41's "
              "wealth?",
         "opts": [
             "No contrast is drawn; the two are identical",
             "AN 5.41's wealth needs protection against fire, water, kings, bandits, and unloved "
             "heirs; this fivefold wealth cannot be confiscated or lost that way",
             "This discourse's wealth is worth less than AN 5.41's",
             "AN 5.41 never mentions wealth's vulnerability"],
         "correct": 1,
         "expl": "A contrast available to a reader who has read AN 5.41, though not stated explicitly here."},
        {"q": "What does the closing verse claim about whoever has this fivefold wealth?",
         "opts": [
             "That they are guaranteed material riches",
             "That they are 'adaliddo', not poor, and their life is not lived in vain",
             "That they will never face hardship",
             "That they must renounce all other wealth"],
         "correct": 1,
         "expl": "A direct claim about a life's basic worth, regardless of ordinary material circumstances."},
        {"q": "What are the five kinds of wealth named in this discourse?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Faith, ethics, learning, generosity, and wisdom",
             "The five powers of a trainee",
             "Long life, beauty, happiness, fame, heaven"],
         "correct": 1,
         "expl": "Identical to AN 5.46's five accomplishments, under a different frame."},
        {"q": "How is ethics defined in this discourse?",
         "opts": [
             "By an elaborate new formula unique to this discourse",
             "By the standard five precepts, worded as in every other discourse using this "
             "formula",
             "By a single vow of poverty",
             "Ethics is not defined at all"],
         "correct": 1,
         "expl": "No new content added beyond the familiar precept formula."},
        {"q": "What is the wealth of faith defined by?",
         "opts": [
             "Confidence in one's own abilities",
             "The nine-quality recollection of the Buddha, the identical formula used every other "
             "time this nipāta defines faith",
             "Trust in family members",
             "A vow of silence"],
         "correct": 1,
         "expl": "The same buddhānussati formula as at AN 5.2, 5.14, and elsewhere."},
        {"q": "Does this discourse claim ordinary material wealth is worthless?",
         "opts": [
             "Yes, explicitly condemning it",
             "No — it presents a different, inalienable kind of wealth without directly condemning "
             "the ordinary kind AN 5.41 already discussed",
             "Yes, it forbids all possessions",
             "The discourse does not mention ordinary wealth at all"],
         "correct": 1,
         "expl": "A parallel account, not an explicit renunciation of AN 5.41's earlier material."},
        {"q": "Where is AN 5.47 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five kinds of wealth", [
            "faith &middot; ethics",
            "learning &middot; generosity",
            "wisdom",
        ]),
        ("Inherited, unchanged", [
            "faith, ethics, wisdom:",
            "identical formulas,",
            "reused throughout",
        ]),
        ("Cannot be confiscated", [
            "unlike AN 5.41's wealth &mdash;",
            "no fire, flood, king,",
            "bandit, or heir can take it",
        ]),
        ("Cross-references", [
            "AN 5.46 &middot; the bare list, first",
            "AN 5.41 &middot; ordinary wealth, vulnerable",
            "AN 5.48 &middot; next: what no one can have",
        ]),
    ],
    further=[
        '<a href="%s/an5.47/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.46.html">AN 5.46 &middot; Success</a> &mdash; this discourse&rsquo;s '
        "compressed original, naming the same five without definitions.",
        '<a href="an-5.41.html">AN 5.41 &middot; Getting Rich</a> &mdash; the earlier, ordinary '
        "wealth this discourse's inalienable version stands against.",
        '<a href="an-5.48.html">AN 5.48 &middot; Things That Cannot Be Had</a> &mdash; next, '
        "turning to what no wealth of any kind can secure.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.48 — Alabbhanīyaṭhānasutta
# --------------------------------------------------------------------------- #
page(
    48, "Alabbhanīyaṭhāna", "Things That Cannot Be Had",
    vagga=VAGGA_5,
    meta_title="AN 5.48 — Things That Cannot Be Had | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Alabbhanīyaṭhānasutta "
        "— five things not even a god, Māra, or Brahmā can prevent: aging, sickness, death, "
        "ending, and perishing, and the poisoned arrow of grief that only reflection can draw "
        "out. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five universal impossibilities named, then two contrasting cases — grieving "
                 "and reflecting — worked through in parallel, closing with verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The poisoned-arrow image for grief, and the list of five "
                              "universal inevitabilities, recur widely across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; no wealth, gift, or "
                       "accomplishment named earlier in this chapter touches what this discourse "
                       "addresses"),
    ],
    why=(
        "Every discourse so far in this chapter has concerned something that can be gained, "
        "given, or secured. This one names five things that cannot &mdash; not by any ascetic, "
        "brahmin, god, Māra, or divinity, or by anyone at all: that someone liable to aging "
        "should not age, that someone liable to sickness should not sicken, that someone liable "
        "to death should not die, to ending should not end, to perishing should not perish. What "
        "the discourse offers is not an exception to this list, but a different relationship to "
        "it."),
    guide=[
        ("The teaching in one sentence", [
            "No one in the world &mdash; ascetic, brahmin, god, Māra, or Brahmā &mdash; can "
            "prevent someone liable to aging, sickness, death, ending, or perishing from "
            "undergoing it; an unlearned ordinary person, struck by this, mortifies themselves "
            "with grief, while a learned noble disciple, struck by the identical fact, draws the "
            "arrow out."]),
        ("Universality stated before consolation", [
            "Before offering any response, the discourse establishes the scope of the problem as "
            "completely as it can: aging, sickness, death, ending, and perishing are named as "
            "beyond the reach of every category of powerful being the canon recognizes, not only "
            "ordinary humans. This is not a discourse claiming the wise can escape these five "
            "things; both the unlearned and the learned person in the discourse experience the "
            "same aging, sickness, and death. What differs is entirely what happens next."]),
        ("The same reflection, twice recommended and once withheld", [
            "The discourse spells out, word for word, the very reflection the unlearned person "
            "fails to have and the learned person actually has: <em>it's not just me who has "
            "someone liable to old age who grows old&hellip; if I were to sorrow and wail and "
            "lament&hellip; I'd lose my appetite&hellip; my work wouldn't get done, my enemies "
            "would be encouraged, and my friends would be dispirited</em>. The unlearned person "
            "thinks this thought and then grieves anyway; the learned person thinks the identical "
            "thought and, having thought it, does not grieve. The reflection itself is not "
            "unique to wisdom; acting on it is."]),
        ("The poisoned arrow, drawn or left in", [
            "<em>Sokasalla</em>, sorrow's arrow, is the discourse's controlling image, and it is "
            "precise about who does what to whom. The unlearned person, struck by loss, "
            "<em>mortifies themselves</em> with a second, self-inflicted wound of grief on top of "
            "the first, unavoidable one. The learned person <em>draws out</em> the arrow and, the "
            "discourse says, <em>only extinguishes themselves</em> &mdash; the same verb root "
            "elsewhere translated nibbāna, applied here to something as ordinary as declining to "
            "add grief to loss."]),
        ("A discourse the chapter needs before its close", [
            "Every earlier discourse in this chapter offered something that could be pursued, "
            "given, or accomplished. This one names the boundary all of that sits inside: wealth, "
            "generosity, learning, and even the inalienable wealth of AN 5.47 do not touch aging, "
            "sickness, or death. AN 5.49 and AN 5.50, closing the chapter, will show this exact "
            "teaching delivered to two grieving kings in turn."]),
    ],
    terms=[
        ("alabbhanīyaṭhāna",
         "&ldquo;a thing that cannot be had&rdquo; &mdash; this discourse's title, naming a "
         "structural impossibility rather than an unlikely event."),
        ("assutavā puthujjano",
         "&ldquo;unlearned ordinary person&rdquo; &mdash; one who experiences loss without the "
         "reflection that would keep grief from compounding it."),
        ("sokasalla",
         "&ldquo;sorrow's arrow&rdquo; &mdash; the discourse's controlling image for grief added "
         "on top of an already unavoidable loss."),
        ("paritāpeti",
         "&ldquo;mortifies, torments&rdquo; &mdash; the verb for what an unlearned person does to "
         "themselves through grief, a self-inflicted second wound."),
        ("parinibbāpeti",
         "&ldquo;fully extinguishes&rdquo; &mdash; the verb for what a learned noble disciple "
         "does instead, sharing its root with nibbāna itself."),
    ],
    text_intro=(
        "The discourse in full: the five universal impossibilities, the unlearned person's "
        "grief, the learned person's reflection, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five things no one can prevent"),
        ("p", "&sect;1", "an5.48:1.1-1.4"),
        ("h3", "The unlearned person's grief"),
        ("p", "&sect;2", "an5.48:2.1-2.7"),
        ("p", "&sect;3", "an5.48:3.1-3.7"),
        ("h3", "The learned disciple's reflection"),
        ("p", "&sect;4", "an5.48:4.1-4.8"),
        ("p", "&sect;5", "an5.48:5.1-5.8"),
        ("p", "&sect;6", "an5.48:6.1"),
        ("h3", "The closing verses"),
        ("p", "&sect;7", "an5.48:7.1-7.4"),
        ("p", "&sect;8", "an5.48:8.1-8.4"),
        ("p", "&sect;9", "an5.48:9.1-9.4"),
        ("p", "&sect;10", "an5.48:10.1-10.4"),
    ],
    quiz=[
        {"q": "What five things does this discourse say cannot be had by anyone in the world?",
         "opts": [
             "Wealth, fame, power, beauty, and long life",
             "That someone liable to aging, sickness, death, ending, or perishing should not "
             "undergo it",
             "The five powers of a trainee",
             "Faith, ethics, learning, generosity, and wisdom"],
         "correct": 1,
         "expl": "Five structural impossibilities, not unlikely events."},
        {"q": "Who does the discourse say cannot prevent these five things, even in principle?",
         "opts": [
             "Only ordinary humans",
             "Any ascetic, brahmin, god, Māra, or divinity — every category of powerful being the "
             "canon recognizes",
             "Only unenlightened people",
             "No one is named; the discourse is vague"],
         "correct": 1,
         "expl": "Universality established before any response is offered."},
        {"q": "Does the learned noble disciple in this discourse avoid experiencing aging, "
              "sickness, and death?",
         "opts": [
             "Yes, entirely",
             "No — both the unlearned and learned person experience the identical aging, "
             "sickness, and death; what differs is what happens next",
             "The discourse does not address this",
             "Only the learned disciple experiences these things"],
         "correct": 1,
         "expl": "Wisdom does not exempt anyone from the five things; it changes the response to them."},
        {"q": "What reflection does the discourse say the learned disciple actually has, that the "
              "unlearned person also thinks but does not act on?",
         "opts": [
             "That grief will eventually pass on its own",
             "That everyone, not just oneself, has someone liable to aging who grows old, and that "
             "grieving would only cause further harm without doing any good",
             "That aging can be prevented through effort",
             "That grief should be suppressed and never expressed"],
         "correct": 1,
         "expl": "The identical thought occurs to both; only the learned disciple lets it actually change their response."},
        {"q": "What does the poisoned-arrow image distinguish?",
         "opts": [
             "Two different kinds of physical injury",
             "A first, unavoidable wound (loss itself) from a second, self-inflicted wound (added "
             "grief) that only the unlearned person adds",
             "Two different weapons used in warfare",
             "The image has no distinguishing function"],
         "correct": 1,
         "expl": "The unlearned person mortifies themselves with a second wound; the learned disciple draws the arrow out."},
        {"q": "What verb describes what the learned disciple does instead of grieving, sharing its "
              "root with 'nibbāna'?",
         "opts": [
             "Paritāpeti, mortifies",
             "Parinibbāpeti, fully extinguishes",
             "Socati, sorrows",
             "Kandati, wails"],
         "correct": 1,
         "expl": "Applied here to declining to add grief to an already unavoidable loss."},
        {"q": "According to the guide, why does this chapter need this discourse before its "
              "close?",
         "opts": [
             "It doesn't; the discourse is unrelated to the chapter",
             "Every earlier discourse concerned something pursuable or accomplishable; this one "
             "names the boundary all of that sits inside — aging, sickness, and death untouched "
             "by any of it",
             "It contradicts every earlier discourse in the chapter",
             "It replaces the chapter's earlier material entirely"],
         "correct": 1,
         "expl": "Even AN 5.47's inalienable wealth does not touch what this discourse names."},
        {"q": "What do the closing verses say about sorrowing and lamenting?",
         "opts": [
             "That they provide real comfort",
             "That they don't do even a little bit of good, and only encourage one's enemies",
             "That they are required by tradition",
             "That they speed up the grieving process"],
         "correct": 1,
         "expl": "A practical, not merely doctrinal, argument against grief's usefulness."},
        {"q": "What do the verses say an astute person should do when facing something that "
              "cannot be had 'by me or by anyone else'?",
         "opts": [
             "Continue struggling against it indefinitely",
             "Accept it without sorrowing, recognizing 'the deed is powerful; what can I do now?'",
             "Deny that it is happening",
             "Blame others for the loss"],
         "correct": 1,
         "expl": "Acceptance grounded in recognizing a genuine structural limit, not resignation to just anything."},
        {"q": "What do AN 5.49 and AN 5.50, closing this chapter, do with this exact teaching?",
         "opts": [
             "Nothing; the teaching is dropped after this discourse",
             "Show it delivered to two grieving kings in turn, as consolation rather than abstract "
             "doctrine",
             "Contradict what this discourse establishes",
             "Repeat only the verses, without the prose teaching"],
         "correct": 1,
         "expl": "The chapter's closing narrative payoff for this discourse's doctrine."},
    ],
    marginalia=[
        ("Five things no one can have", [
            "not aging &middot; not sickness",
            "not dying &middot; not ending",
            "not perishing",
        ]),
        ("Same loss, different response", [
            "unlearned: grieves,",
            "mortifies themselves",
            "learned: reflects,",
            "draws the arrow out",
        ]),
        ("The image", [
            "<span class=\"pali\">sokasalla</span>",
            "sorrow's arrow &mdash;",
            "a second, added wound",
        ]),
        ("Cross-references", [
            "AN 5.47 &middot; wealth that still can't touch this",
            "AN 5.49 &middot; next: a grieving king",
            "AN 5.50 &middot; the fuller narrative version",
        ]),
    ],
    further=[
        '<a href="%s/an5.48/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.47.html">AN 5.47 &middot; Wealth</a> &mdash; the previous discourse, on '
        "wealth that cannot be confiscated but still cannot prevent what this discourse names.",
        '<a href="an-5.49.html">AN 5.49 &middot; The King of Kosala</a> &mdash; next, this exact '
        "teaching delivered to a king whose queen has just died.",
        '<a href="an-5.50.html">AN 5.50 &middot; With Nārada</a> &mdash; the chapter&rsquo;s '
        "closing discourse, the fullest narrative version of this same teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.49 — Kosalasutta
# --------------------------------------------------------------------------- #
page(
    49, "Kosala", "The King of Kosala",
    vagga=VAGGA_5,
    meta_title="AN 5.49 — The King of Kosala | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kosalasutta — King "
        "Pasenadi is told mid-visit that Queen Mallikā has just died, and the Buddha delivers AN "
        "5.48's teaching directly into the moment of his grief. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery; stated at the head of "
                    "AN 5.49"),
        ("Speakers", "King Pasenadi of Kosala, silent with grief; the Buddha, teaching him "
                     "directly"),
        ("Form", "A visit interrupted by sudden news, and AN 5.48's teaching given in its "
                 "compressed form, without repeating the full doctrinal unpacking"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "A ruler's grief met with teaching on impermanence recurs across "
                              "the Chinese Āgamas' royal narratives; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief in its own text, "
                       "carrying the full weight of AN 5.48 behind it"),
    ],
    why=(
        "This discourse does not restate AN 5.48's teaching in full; it compresses it into a "
        "single reference, because the point here is not exposition but timing. King Pasenadi "
        "is already seated with the Buddha when a messenger whispers that Queen Mallikā has "
        "died. The king's reaction is given without embellishment &mdash; <em>miserable and "
        "sad&hellip; shoulders drooping, downcast, depressed, with nothing to say</em> &mdash; "
        "and the Buddha, seeing this, speaks directly into it."),
    guide=[
        ("The teaching in one sentence", [
            "Told that Queen Mallikā has just died, King Pasenadi sits in silent grief, and the "
            "Buddha, recognizing his state, gives him the teaching on the five things no one can "
            "have and the uselessness of sorrowing over what cannot be helped."]),
        ("Grief witnessed before it is addressed", [
            "The discourse spends real attention on the king's visible state before the Buddha "
            "says anything: <em>dukkhī dummano pattakkhandho adhomukho pajjhāyanto "
            "appaṭibhāno</em>, four distinct physical descriptions of collapse &mdash; drooping "
            "shoulders, a lowered face, brooding, nothing to say. The Buddha does not interrupt "
            "or rush past this; the text records that he spoke <em>knowing</em> this state, "
            "having first registered it fully."]),
        ("The teaching, compressed rather than repeated", [
            "Where AN 5.48 spelled out the reflection word for word, twice over, for both the "
            "unlearned and the learned response, this discourse gives only the opening and "
            "closing lines, with an ellipsis standing in for everything in between. The "
            "compression itself is a claim about audience: this discourse assumes a reader "
            "already knows AN 5.48's content, and reproducing it in full here would blunt rather "
            "than sharpen the moment."]),
        ("A king, not a monastic, as the direct recipient", [
            "This is one of the few discourses in this chapter where the full teaching on "
            "impermanence and grief is given to a layperson, and a ruler at that, in the middle "
            "of his own bereavement rather than as general instruction to mendicants. The "
            "discourse does not soften the content for a royal audience or offer any "
            "consolation beyond what AN 5.48 already supplies to anyone."]),
        ("What the discourse leaves unstated", [
            "Unlike AN 5.50, this discourse does not report how Pasenadi responded, whether he "
            "was consoled, or what he did afterward. It ends at the teaching itself, mid-scene, "
            "leaving the king's eventual reaction to be inferred rather than narrated &mdash; a "
            "contrast worth noticing against the fuller resolution AN 5.50 will supply for a "
            "different king's identical grief."]),
    ],
    terms=[
        ("mallikā devī",
         "&ldquo;Queen Mallikā&rdquo; &mdash; King Pasenadi's wife, whose sudden death is the "
         "occasion for this discourse."),
        ("pattakkhandho adhomukho",
         "&ldquo;shoulders drooping, face lowered&rdquo; &mdash; two of four physical "
         "descriptions of the king's grief, recorded before the Buddha speaks."),
        ("appaṭibhāna",
         "&ldquo;with nothing to say&rdquo; &mdash; the fourth description, marking the king's "
         "grief as beyond immediate speech."),
        ("viditvā",
         "&ldquo;having known, having recognized&rdquo; &mdash; the verb marking that the "
         "Buddha spoke only after registering the king's state fully."),
        ("mahārāja",
         "&ldquo;great king&rdquo; &mdash; the Buddha's form of address, distinct from "
         "&lsquo;bhikkhave&rsquo;, mendicants, used throughout most of this nipāta."),
    ],
    text_intro=(
        "The discourse in full: the king's visit, the sudden news, his visible grief, and the "
        "Buddha's teaching given in compressed form. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sudden news"),
        ("p", "&sect;1", "an5.49:1.1-1.2"),
        ("p", "&sect;2", "an5.49:2.1-2.3"),
        ("p", "&sect;3", "an5.49:2.4"),
        ("h3", "The Buddha's teaching"),
        ("p", "&sect;4", "an5.49:3.1-3.4"),
    ],
    quiz=[
        {"q": "What news interrupts King Pasenadi's visit to the Buddha?",
         "opts": [
             "News of a military defeat",
             "That Queen Mallikā has just died",
             "News of a famine",
             "That his treasury has been robbed"],
         "correct": 1,
         "expl": "A messenger whispers the news mid-visit."},
        {"q": "How is the king's grief described before the Buddha speaks?",
         "opts": [
             "Briefly, in one word",
             "In detail — miserable, sad, shoulders drooping, face lowered, brooding, with "
             "nothing to say",
             "The discourse does not describe his reaction at all",
             "As controlled and composed"],
         "correct": 1,
         "expl": "Four distinct physical descriptions, recorded before any teaching is given."},
        {"q": "Does the Buddha speak immediately, or after registering the king's state?",
         "opts": [
             "He speaks immediately, without pause",
             "He speaks 'having known' (viditvā) the king's grief, after registering it fully",
             "He waits for the king to speak first",
             "He remains silent throughout"],
         "correct": 1,
         "expl": "The text marks recognition before response."},
        {"q": "How does this discourse present AN 5.48's teaching — in full, or compressed?",
         "opts": [
             "In full, word for word",
             "Compressed, with an ellipsis standing in for the full reflection already spelled "
             "out at AN 5.48",
             "Not presented at all",
             "In an entirely different form from AN 5.48"],
         "correct": 1,
         "expl": "The compression assumes the reader already knows AN 5.48's fuller content."},
        {"q": "What does the guide say the compression implies about the discourse's intended "
              "audience?",
         "opts": [
             "That it was meant to be read in complete isolation",
             "That reproducing AN 5.48's content in full here would blunt rather than sharpen the "
             "moment for a reader who already knows it",
             "That the compression is a copying error",
             "That this discourse predates AN 5.48"],
         "correct": 1,
         "expl": "A deliberate structural choice, not an omission."},
        {"q": "Does this discourse report how King Pasenadi eventually responded to the teaching?",
         "opts": [
             "Yes, in full detail",
             "No — it ends at the teaching itself, leaving his reaction unstated, unlike AN 5.50",
             "Yes, but only briefly",
             "It reports that he rejected the teaching"],
         "correct": 1,
         "expl": "A contrast with AN 5.50's fuller resolution for a different king's grief."},
        {"q": "What form of address does the Buddha use for the king, distinct from most of this "
              "nipāta's 'bhikkhave'?",
         "opts": [
             "Gahapati, householder",
             "Mahārāja, great king",
             "Āvuso, friend",
             "Bhante, sir"],
         "correct": 1,
         "expl": "Marking the direct, personal nature of this address to a layperson in crisis."},
        {"q": "Is this teaching softened or altered for a royal, lay audience?",
         "opts": [
             "Yes, significantly softened",
             "No — no consolation is offered beyond what AN 5.48 already supplies to anyone",
             "Yes, an entirely different teaching is given",
             "The discourse does not specify"],
         "correct": 1,
         "expl": "The identical teaching, delivered without modification for the audience."},
        {"q": "Is this the first time in this chapter that a full impermanence teaching has been "
              "given directly to a layperson in the midst of their own grief?",
         "opts": [
             "No, this has happened multiple times already in this chapter",
             "Yes — one of the few such instances in this chapter",
             "This never happens in this chapter",
             "The question is not addressed by the guide"],
         "correct": 1,
         "expl": "A distinctive moment, noted by the guide as unusual within this chapter."},
        {"q": "Where is AN 5.49 set?",
         "opts": [
             "A new location, stated explicitly — Sāvatthī, in Jeta's Grove",
             "None restated",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 0,
         "expl": "Explicitly restated at the head of this discourse."},
    ],
    marginalia=[
        ("The scene", [
            "mid-visit &mdash;",
            "a whispered message:",
            "the queen has died",
        ]),
        ("Grief, recorded first", [
            "shoulders drooping",
            "face lowered",
            "nothing to say",
        ]),
        ("Compressed, not repeated", [
            "AN 5.48: full teaching",
            "AN 5.49: reference only",
            "&mdash; assumes the reader knows",
        ]),
        ("Cross-references", [
            "AN 5.48 &middot; the full teaching",
            "AN 5.50 &middot; next: fuller resolution",
            "AN 5.31 &middot; another royal questioner",
        ]),
    ],
    further=[
        '<a href="%s/an5.49/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.48.html">AN 5.48 &middot; Things That Cannot Be Had</a> &mdash; the full '
        "teaching this discourse compresses into a single reference.",
        '<a href="an-5.50.html">AN 5.50 &middot; With Nārada</a> &mdash; next, the same teaching '
        "given in full narrative detail to a different grieving king.",
        '<a href="an-5.31.html">AN 5.31 &middot; With Sumanā</a> &mdash; an earlier royal '
        "questioner, in a very different mood than this discourse's king.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.50 — Nāradasutta
# --------------------------------------------------------------------------- #
page(
    50, "Nārada", "With Nārada",
    vagga=VAGGA_5,
    meta_title="AN 5.50 — With Nārada | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nāradasutta, closing "
        "this chapter — King Muṇḍa refuses to cremate his dead queen, preserving her body in an "
        "oil-filled casket, until Venerable Nārada delivers the teaching that finally lets him "
        "let her go. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Pāṭaliputta, the Chicken Monastery, where Nārada is staying; the teaching "
                    "given there to King Muṇḍa, who travels from his own residence"),
        ("Speakers", "King Muṇḍa; Piyaka, keeper of the treasury; Venerable Nārada"),
        ("Form", "An extended narrative in three movements — the king's refusal to let go, "
                 "Piyaka's search for a teacher, and Nārada's full delivery of the teaching "
                 "already given in brief at AN 5.48"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "Narratives of a bereaved ruler consoled by a monastic teacher on "
                              "impermanence recur across the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; &mdash; this chapter's longest and "
                       "most unflinching discourse, closing on the namesake king's grief in full "
                       "detail"),
    ],
    why=(
        "This is the discourse the chapter is named for, and it does not soften what it "
        "describes. King Muṇḍa's beloved Queen Bhaddā dies, and rather than cremate her body he "
        "orders it sealed in oil inside an iron casket, closed within a second casket, so that "
        "he can keep viewing her corpse indefinitely. He stops bathing, eating properly, and "
        "attending to his rule, brooding over the body day and night. It takes his own "
        "treasury-keeper's initiative, and Venerable Nārada's full delivery of the teaching "
        "already given in brief at AN 5.48, to bring him back."),
    guide=[
        ("The teaching in one sentence", [
            "Grieving so completely that he preserves his dead queen's body rather than let it "
            "be cremated, King Muṇḍa is brought, through his treasury-keeper Piyaka's initiative, "
            "to hear Venerable Nārada teach the five things no one can have and the pointlessness "
            "of sorrow, and afterward has the queen's body cremated and resumes his life."]),
        ("A king's grief, described without euphemism", [
            "The discourse states plainly what Muṇḍa does: he has Bhaddā&rsquo;s body placed in "
            "an oil-filled iron casket, sealed inside a second casket, explicitly "
            "<em>so that we can view Queen Bhaddā's body even longer</em>. He stops bathing, "
            "anointing himself, eating properly, and doing his work, brooding over the corpse "
            "<em>day and night</em>. This reading guide will not soften this description into "
            "something gentler; the discourse itself does not, and the starkness of the image is "
            "what makes Piyaka's intervention, and Nārada's teaching, actually necessary rather "
            "than merely comforting."]),
        ("Piyaka's own initiative", [
            "Nothing in the discourse suggests Muṇḍa asked for help. It is Piyaka, watching his "
            "king&rsquo;s decline, who reasons through the problem himself &mdash; "
            "<em>what ascetic or brahmin might the king pay homage to, whose teaching could help "
            "the king give up sorrow's arrow?</em> &mdash; and independently recalls Nārada's "
            "reputation before proposing the visit. The chain of events that eventually frees the "
            "king from his grief begins with a subordinate's own observation and judgment, not "
            "with any royal request."]),
        ("The full teaching, restated at length", [
            "Where AN 5.49 compressed the teaching to a bare reference, this discourse delivers "
            "it at the same length as AN 5.48 itself &mdash; the five impossibilities, the "
            "unlearned person's grief over aging, the learned disciple's reflection over aging, "
            "and the identical pattern worked through again for the elided middle three (sickness, "
            "death, ending) using perishing as the worked example, exactly as AN 5.48 structured "
            "it. This reading guide does not repeat that content a third time here, having "
            "already presented it in full at AN 5.48; what is new in this discourse is entirely "
            "the frame around it."]),
        ("A named teaching, and a resolution", [
            "Muṇḍa asks Nārada directly what this exposition is called, and is told: "
            "<em>Sokasallaharaṇo</em>, Pulling Out Sorrow's Arrow &mdash; the same image AN 5.48 "
            "used, now given as the formal title of a teaching a king has just received and "
            "confirmed by his own testimony: <em>hearing this exposition, I've given up sorrow's "
            "arrow</em>. The discourse's final act is entirely practical: Muṇḍa orders the "
            "queen's body cremated and a monument built, and announces, in the same breath, that "
            "he will resume bathing, eating, and governing."]),
    ],
    terms=[
        ("teladoṇi",
         "&ldquo;oil-filled casket&rdquo; &mdash; the vessel King Muṇḍa uses to preserve his "
         "dead queen's body, described without euphemism."),
        ("ajjhomucchito",
         "&ldquo;brooding over, absorbed in&rdquo; &mdash; the discourse's description of "
         "Muṇḍa's state, day and night, over the queen's corpse."),
        ("sokasallaṁ pajahati",
         "&ldquo;give up sorrow's arrow&rdquo; &mdash; the goal Piyaka hopes Nārada's teaching "
         "will achieve, and which Muṇḍa later confirms achieving."),
        ("kosārakkha",
         "&ldquo;keeper of the treasury&rdquo; &mdash; Piyaka's official role, and the position "
         "from which he takes independent initiative to help his king."),
        ("sokasallaharaṇo",
         "&ldquo;pulling out sorrow's arrow&rdquo; &mdash; the formal name Nārada gives this "
         "exposition of the teaching, confirmed as accurate by Muṇḍa himself."),
    ],
    text_intro=(
        "The discourse in full: King Muṇḍa's grief and the preserved body, Piyaka's search for a "
        "teacher, the journey to Nārada, and the teaching's opening and closing movements. The "
        "central doctrinal repetition, identical to AN 5.48's full text, is represented here by "
        "its first working (aging) rather than reproduced a third time; the discourse itself "
        "runs the identical pattern again for the elided middle three conditions, using "
        "perishing as the worked example, exactly as at AN 5.48. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The queen's death, and the preserved body"),
        ("p", "&sect;1", "an5.50:1.1"),
        ("p", "&sect;2", "an5.50:1.2-1.4"),
        ("p", "&sect;3", "an5.50:1.5"),
        ("p", "&sect;4", "an5.50:1.6"),
        ("p", "&sect;5", "an5.50:1.7"),
        ("h3", "Piyaka's own initiative"),
        ("p", "&sect;6", "an5.50:2.1-2.5"),
        ("p", "&sect;7", "an5.50:3.1-3.5"),
        ("h3", "Seeking the king's approval"),
        ("p", "&sect;8", "an5.50:4.1-4.5"),
        ("p", "&sect;9", "an5.50:4.6-4.7"),
        ("h3", "The invitation to Nārada"),
        ("p", "&sect;10", "an5.50:4.8-5.4"),
        ("p", "&sect;11", "an5.50:5.5"),
        ("h3", "The journey to the Chicken Monastery"),
        ("p", "&sect;12", "an5.50:6.1-6.3"),
        ("p", "&sect;13", "an5.50:6.4"),
        ("p", "&sect;14", "an5.50:6.5-6.7"),
        ("p", "&sect;15", "an5.50:7.1-7.3"),
        ("h3", "Nārada's teaching begins"),
        ("p", "&sect;16", "an5.50:8.1-8.4"),
        ("p", "&sect;17", "an5.50:9.1-9.7"),
        ("h3", "The closing verses"),
        ("p", "&sect;18", "an5.50:14.1-14.4"),
        ("p", "&sect;19", "an5.50:15.1-15.4"),
        ("p", "&sect;20", "an5.50:16.1-16.4"),
        ("p", "&sect;21", "an5.50:17.1-17.4"),
        ("h3", "“Pulling Out Sorrow's Arrow”"),
        ("p", "&sect;22", "an5.50:18.1-18.2"),
        ("p", "&sect;23", "an5.50:18.3"),
        ("p", "&sect;24", "an5.50:18.4-18.5"),
        ("h3", "The queen is cremated"),
        ("p", "&sect;25", "an5.50:19.1-19.3"),
    ],
    quiz=[
        {"q": "What does King Muṇḍa do instead of cremating Queen Bhaddā's body after her death?",
         "opts": [
             "He buries it immediately",
             "He has it sealed in an oil-filled iron casket, closed inside a second casket, so he "
             "can keep viewing it",
             "He has it enshrined in a temple",
             "He scatters her ashes at once"],
         "correct": 1,
         "expl": "A stark, unsoftened description the discourse states plainly."},
        {"q": "How does the king's daily life change after the queen's death?",
         "opts": [
             "Nothing changes at all",
             "He stops bathing, anointing himself, eating properly, and doing his work, brooding "
             "over the corpse day and night",
             "He immediately abdicates the throne",
             "He becomes more active in governing"],
         "correct": 1,
         "expl": "A description this reading guide presents without euphemism, matching the discourse's own directness."},
        {"q": "Who first takes initiative to seek help for the king?",
         "opts": [
             "The king himself, requesting a teacher",
             "Piyaka, the keeper of the treasury, observing the king's decline and reasoning "
             "through the problem on his own",
             "Queen Bhaddā's family",
             "A group of ministers acting together"],
         "correct": 1,
         "expl": "A subordinate's own observation and judgment, not a royal request, begins the chain of events."},
        {"q": "How does this discourse's presentation of the core teaching compare to AN 5.48's?",
         "opts": [
             "It is entirely different content",
             "It delivers the identical teaching at the same length AN 5.48 already gave in full, "
             "which this reading guide does not repeat a third time here",
             "It gives only a summary, never the full teaching",
             "It contradicts AN 5.48"],
         "correct": 1,
         "expl": "The same five impossibilities and the same unlearned/learned contrast, worked through in full."},
        {"q": "What name does Nārada give this exposition of the teaching?",
         "opts": [
             "'The Five Powers'",
             "'Sokasallaharaṇo', Pulling Out Sorrow's Arrow",
             "'The King's Consolation'",
             "No name is given"],
         "correct": 1,
         "expl": "A formal title using the same arrow image already central to AN 5.48."},
        {"q": "How does King Muṇḍa confirm the teaching worked?",
         "opts": [
             "He says nothing at all",
             "He states directly, 'hearing this exposition, I've given up sorrow's arrow'",
             "He asks for a second teaching",
             "He rejects the teaching as insufficient"],
         "correct": 1,
         "expl": "A direct, first-person confirmation closing the discourse's emotional arc."},
        {"q": "What does the king do immediately after confirming the teaching worked?",
         "opts": [
             "Nothing changes in his behavior",
             "He orders the queen's body cremated and a monument built, and announces he will "
             "resume bathing, eating, and governing",
             "He orders the body preserved even longer",
             "He abdicates in favor of his son"],
         "correct": 1,
         "expl": "A fully practical resolution, matching the concreteness of his earlier grief."},
        {"q": "Where does Nārada deliver this teaching?",
         "opts": [
             "At the royal palace",
             "At the Chicken Monastery in Pāṭaliputta, where the king travels to meet him",
             "In a forest clearing",
             "On the road between two cities"],
         "correct": 1,
         "expl": "The king comes to Nārada, dismounting from his chariot to enter on foot."},
        {"q": "How does the guide characterize its own choice not to reproduce the doctrinal core "
              "a third time?",
         "opts": [
             "As an omission it apologizes for",
             "As a deliberate choice, since AN 5.48 already presented the identical content in "
             "full, and this discourse's new material is entirely in its narrative frame",
             "As evidence the teaching is unimportant",
             "As a correction of an error in AN 5.48"],
         "correct": 1,
         "expl": "The frame, not the doctrine, is what this discourse adds."},
        {"q": "What does this discourse's title and chapter placement signal about its role?",
         "opts": [
             "It is unrelated to the chapter's overall theme",
             "It is the discourse this whole chapter is named for, closing the chapter on its "
             "most unflinching and fully resolved note",
             "It is a minor, easily skippable discourse",
             "It contradicts the chapter's opening discourse, AN 5.41"],
         "correct": 1,
         "expl": "The Muṇḍarājavagga's own namesake, and its final word."},
    ],
    marginalia=[
        ("The refusal", [
            "oil-filled casket,",
            "sealed twice over &mdash;",
            "so he could keep viewing her",
        ]),
        ("A subordinate's initiative", [
            "Piyaka: watches, reasons,",
            "recalls Nārada,",
            "proposes the visit",
        ]),
        ("The named teaching", [
            "<span class=\"pali\">Sokasallaharaṇo</span>",
            "&mdash; Pulling Out",
            "Sorrow's Arrow",
        ]),
        ("Cross-references", [
            "AN 5.48 &middot; the full teaching, first",
            "AN 5.49 &middot; the compressed version",
            "AN 5.51 &middot; next: Nīvaraṇavagga",
        ]),
    ],
    further=[
        '<a href="%s/an5.50/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.48.html">AN 5.48 &middot; Things That Cannot Be Had</a> &mdash; the full '
        "doctrinal core this discourse's narrative frame surrounds.",
        '<a href="an-5.49.html">AN 5.49 &middot; The King of Kosala</a> &mdash; the previous '
        "discourse, the same teaching compressed for a different grieving king.",
        '<a href="an-5.41.html">AN 5.41 &middot; Getting Rich</a> &mdash; this chapter&rsquo;s '
        "opening discourse, on wealth&rsquo;s uses, before its close on what no wealth can secure.",
    ],
)


VAGGA_6 = "<em>Nīvaraṇavagga</em> &mdash; the sixth chapter of the Fives"


# --------------------------------------------------------------------------- #
# AN 5.51 — Āvaraṇasutta
# --------------------------------------------------------------------------- #
page(
    51, "Āvaraṇa", "Obstacles",
    vagga=VAGGA_6,
    meta_title="AN 5.51 — Obstacles | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Āvaraṇasutta, opening "
        "the chapter this whole nipāta has been anticipating — the five hindrances, named "
        "directly by their own term at last, and a mountain river that either runs strong or is "
        "drained by opened channels. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery; stated at the head of "
                    "AN 5.51 and understood to hold across this chapter unless a discourse "
                    "restates its own setting"),
        ("Speakers", SPEAKER),
        ("Form", "The five hindrances named, then a single simile run twice — once for their "
                 "presence, once for their absence"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The five hindrances (nīvaraṇa) are among the most widely attested "
                              "lists across the Chinese Āgamas and Abhidharma literature; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but naming material "
                       "this series has anticipated since AN 5.23"),
    ],
    why=(
        "This chapter's name has been visible on the horizon since <a href=\"an-5.23.html\">AN "
        "5.23</a> named the same five states <em>upakkilesa</em>, corruptions, and flagged that "
        "they would eventually give an entire chapter of the Fives its title. That chapter has "
        "arrived. Sensual desire, ill will, dullness and drowsiness, restlessness and remorse, "
        "and doubt are named here by their most familiar term, <em>nīvaraṇa</em>, hindrances, "
        "and illustrated by a single, exact image: a mountain river, either running its full "
        "course or drained away through opened channels."),
    guide=[
        ("The teaching in one sentence", [
            "The five hindrances &mdash; sensual desire, ill will, dullness and drowsiness, "
            "restlessness and remorse, and doubt &mdash; are obstacles and parasites of the mind "
            "that weaken wisdom, and a mendicant who has not given them up cannot know what is "
            "good for themselves, others, or both, while one who has given them up can."]),
        ("A third name for the same five states", [
            "This series has now met this identical five-item list under three separate labels: "
            "<em>upakkilesa</em>, corruptions, at AN 5.23; and now <em>āvaraṇa nīvaraṇa</em>, "
            "obstacles and hindrances, here. The content has not changed across any of these "
            "namings &mdash; sensual desire, ill will, dullness and drowsiness, restlessness and "
            "remorse, doubt, always in this order. What changes is the image each label carries: "
            "corruption suggested gold needing refinement; hindrance suggests something standing "
            "in a path."]),
        ("&lsquo;Parasites of the mind&rsquo;", [
            "<em>Cetaso ajjhāruhā</em>, translated here as parasites of the mind, is a more "
            "vivid image than &lsquo;hindrance&rsquo; alone conveys &mdash; something that grows "
            "on or into the mind, drawing from it rather than merely blocking its way. Paired "
            "with <em>paññāya dubbalīkaraṇā</em>, weakening wisdom, the compound description "
            "names both what the five states are (parasitic) and what they specifically damage "
            "(wisdom, not virtue or concentration in general)."]),
        ("A river, opened and closed", [
            "The simile is worked twice, changing only one verb: a man <em>opens</em> channels "
            "on both sides of a swift mountain river, and its current disperses, weakens, no "
            "longer reaches far; a man <em>closes</em> those same channels, and the current runs "
            "swift and far, carrying everything before it. The hindrances are the opened "
            "channels &mdash; not external obstacles blocking the river&rsquo;s path, but leaks "
            "in the container the water itself needed to keep moving with force."]),
        ("What this discourse decides for a mendicant's own good", [
            "The stakes named are specific: without giving up the five hindrances, a mendicant "
            "cannot know <em>attattha</em>, their own good, <em>parattha</em>, another's good, or "
            "<em>ubhayattha</em>, the good of both &mdash; nor realize any distinction in "
            "knowledge and vision worthy of the noble ones. The hindrances are not framed here as "
            "moral failings to be ashamed of, but as a specific, describable cause of a specific, "
            "describable incapacity."]),
    ],
    terms=[
        ("nīvaraṇa",
         "&ldquo;hindrance&rdquo; &mdash; the term giving this chapter its name, the same five "
         "states already met as upakkilesa at AN 5.23."),
        ("cetaso ajjhāruhā",
         "&ldquo;parasites of the mind&rdquo; &mdash; a vivid compound suggesting growth into the "
         "mind rather than mere external obstruction."),
        ("paññāya dubbalīkaraṇā",
         "&ldquo;that which weakens wisdom&rdquo; &mdash; naming the specific faculty the five "
         "hindrances are said to damage."),
        ("attattha parattha ubhayattha",
         "&ldquo;one's own good, another's good, the good of both&rdquo; &mdash; the threefold "
         "knowledge this discourse says the hindrances make impossible."),
        ("naṅgalamukha",
         "&ldquo;channel, sluice-gate&rdquo; &mdash; literally a plow's mouth, the opening in the "
         "riverbank the simile turns on."),
    ],
    text_intro=(
        "The discourse in full: the five hindrances named, and the river simile run twice, for "
        "their presence and their absence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Sāvatthī"),
        ("p", "&sect;1", "an5.51:1.1-1.6"),
        ("h3", "The five hindrances"),
        ("p", "&sect;2", "an5.51:2.1-2.8"),
        ("h3", "The river, drained"),
        ("p", "&sect;3", "an5.51:3.1"),
        ("p", "&sect;4", "an5.51:3.2-3.4"),
        ("p", "&sect;5", "an5.51:3.5"),
        ("h3", "The river, running strong"),
        ("p", "&sect;6", "an5.51:4.1"),
        ("p", "&sect;7", "an5.51:4.2-4.4"),
        ("p", "&sect;8", "an5.51:4.5"),
    ],
    quiz=[
        {"q": "What five states does this discourse name as obstacles and hindrances?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Sensual desire, ill will, dullness and drowsiness, restlessness and remorse, and "
             "doubt",
             "Iron, copper, tin, lead, and silver",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "The nīvaraṇa, already met once before under a different name."},
        {"q": "Where did this identical five-item list already appear in this series, under a "
              "different label?",
         "opts": [
             "Nowhere before this page",
             "AN 5.23, called upakkilesa, corruptions",
             "AN 5.1",
             "AN 4.163"],
         "correct": 1,
         "expl": "The same content, a different image, foreshadowed as far back as AN 5.23's own guide."},
        {"q": "What does 'cetaso ajjhāruhā', parasites of the mind, suggest that 'hindrance' alone "
              "does not?",
         "opts": [
             "Nothing different; the terms are synonyms with no distinction",
             "Something that grows on or into the mind, drawing from it, rather than merely "
             "standing in its way",
             "A physical illness",
             "A type of meditation posture"],
         "correct": 1,
         "expl": "A more vivid, organic image than a simple obstruction."},
        {"q": "What specifically does this discourse say the five hindrances weaken?",
         "opts": [
             "Physical strength",
             "Wisdom specifically (paññāya dubbalīkaraṇā), not virtue or concentration in general",
             "Only memory",
             "Only social reputation"],
         "correct": 1,
         "expl": "A specific, named faculty, not a vague general harm."},
        {"q": "What happens to the river when a man opens channels on both sides?",
         "opts": [
             "It flows faster and further",
             "Its current disperses, weakens, and no longer reaches far — matching a mind not "
             "given up to hindrances",
             "Nothing changes",
             "It floods the surrounding land"],
         "correct": 1,
         "expl": "The hindrances are pictured as leaks, not as blockages in the river's path."},
        {"q": "What three kinds of good does this discourse say the hindrances make impossible to "
              "know?",
         "opts": [
             "Wealth, health, and family",
             "One's own good, another's good, and the good of both",
             "Ethics, immersion, and wisdom",
             "Past, present, and future"],
         "correct": 1,
         "expl": "Attattha, parattha, ubhayattha — the specific incapacity the hindrances cause."},
        {"q": "How does the guide characterize the hindrances' framing in this discourse?",
         "opts": [
             "As moral failings to be ashamed of",
             "As a specific, describable cause of a specific, describable incapacity, not framed "
             "moralistically",
             "As entirely beyond a mendicant's control",
             "As unrelated to wisdom"],
         "correct": 1,
         "expl": "A functional, almost mechanical description rather than a condemnation."},
        {"q": "What single word changes between the two halves of the river simile?",
         "opts": [
             "The word for 'river'",
             "The verb — opening the channels versus closing them",
             "The word for 'mind'",
             "Nothing changes between the two halves"],
         "correct": 1,
         "expl": "One verb, run twice, produces the entire contrast."},
        {"q": "What does the guide say changes across the three names this five-item list has "
              "received in this series (upakkilesa, nīvaraṇa)?",
         "opts": [
             "The actual content of the list changes each time",
             "Only the image each label carries changes; the five items and their order stay fixed",
             "The number of items changes",
             "Nothing changes at all, including the labels"],
         "correct": 1,
         "expl": "Corruption suggests refinement; hindrance suggests a path obstructed — different images, same five states."},
        {"q": "Where is AN 5.51 set?",
         "opts": [
             "A new location, stated explicitly",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery, restated in full",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "A full restatement of the standard setting, opening this new chapter."},
    ],
    marginalia=[
        ("Five hindrances", [
            "sensual desire &middot; ill will",
            "dullness/drowsiness",
            "restlessness/remorse",
            "doubt",
        ]),
        ("Three names, one list", [
            "AN 5.23: upakkilesa",
            "AN 5.51: nīvaraṇa",
            "&mdash; same five, new image",
        ]),
        ("The river", [
            "channels open &rarr;",
            "current disperses",
            "channels closed &rarr;",
            "runs swift, far",
        ]),
        ("Cross-references", [
            "AN 5.23 &middot; the corruptions, first",
            "AN 5.52 &middot; next: a heap, entirely",
            "AN 5.53 &middot; then: what supports meditation",
        ]),
    ],
    further=[
        '<a href="%s/an5.51/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; where this identical '
        "five-item list first appeared, and where this chapter's arrival was foreshadowed.",
        '<a href="an-5.52.html">AN 5.52 &middot; A Heap of the Unskillful</a> &mdash; next, the '
        "same five named as unskillfulness in its entirety.",
        '<a href="an-5.53.html">AN 5.53 &middot; Factors That Support Meditation</a> &mdash; the '
        "discourse after that, on what makes meditation possible rather than what obstructs it.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.52 — Akusalarāsisutta
# --------------------------------------------------------------------------- #
page(
    52, "Akusalarāsi", "A Heap of the Unskillful",
    vagga=VAGGA_6,
    meta_title="AN 5.52 — A Heap of the Unskillful | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Akusalarāsisutta — a "
        "single, blunt claim: rightly speaking, the five hindrances are not merely unskillful "
        "but entirely constitute a heap of the unskillful. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single claim, stated once and then repeated verbatim as its own conclusion"),
        ("Length", "~20 seconds to read"),
        ("Northern parallel", "Characterizing the hindrances as the sum of unskillfulness "
                              "recurs across the Chinese Āgamas' treatment of the same list; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest discourse in "
                       "this chapter, making the boldest claim about its own subject"),
    ],
    why=(
        "This discourse makes a claim stronger than anything AN 5.51 said. It does not call the "
        "five hindrances a kind of unskillfulness, or a significant source of it; it says that "
        "<em>rightly speaking</em>, they are, entirely, <em>a heap of the unskillful</em> "
        "&mdash; as if unskillfulness itself, gathered into one pile, would turn out to be "
        "nothing more or less than these five things."),
    guide=[
        ("The teaching in one sentence", [
            "Rightly speaking, the five hindrances &mdash; sensual desire, ill will, dullness "
            "and drowsiness, restlessness and remorse, and doubt &mdash; are entirely a heap of "
            "the unskillful."]),
        ("A claim about totality, not membership", [
            "<em>Kevalo</em>, entirely, is the word doing the real work here. The discourse does "
            "not say the hindrances belong to the category of unskillful things among others; it "
            "says they exhaust the category. This is a stronger and more specific claim than a "
            "casual reader might assume &mdash; not &lsquo;these are examples of "
            "unskillfulness&rsquo; but &lsquo;this is what unskillfulness, entirely, consists "
            "of&rsquo;."]),
        ("&lsquo;Rightly speaking&rsquo;, and what it implies", [
            "The phrase <em>sammā vadamāno vadeyya</em>, rightly speaking, one would say, frames "
            "this as a claim about correct description, not merely a rhetorical flourish. The "
            "discourse is staking out a specific position on how the word "
            "&lsquo;unskillful&rsquo; ought to be used when applied to this list, against "
            "whatever looser usage might otherwise apply the term more broadly."]),
        ("A single sentence, repeated as its own proof", [
            "The discourse's entire structure is one claim, stated, and then the identical claim "
            "restated as its own conclusion, with the five hindrances named explicitly in "
            "between. There is no simile, no narrative, no argument beyond the assertion itself "
            "&mdash; a form matching the claim's own totalizing character: nothing more needs "
            "adding once the heap has been named complete."]),
    ],
    terms=[
        ("akusalarāsi",
         "&ldquo;heap of the unskillful&rdquo; &mdash; this discourse's title and central claim, "
         "an image of unskillfulness gathered entirely into one pile."),
        ("kevalo",
         "&ldquo;entirely, completely&rdquo; &mdash; the word marking this as a claim about "
         "totality, not mere membership in a category."),
        ("sammā vadamāno vadeyya",
         "&ldquo;rightly speaking, one would say&rdquo; &mdash; framing the claim as a matter of "
         "correct description, not rhetorical exaggeration."),
        ("nīvaraṇa",
         "&ldquo;hindrance&rdquo; &mdash; the five states this discourse claims exhaust the "
         "category of the unskillful entirely."),
        ("vicikicchā",
         "&ldquo;doubt&rdquo; &mdash; the fifth and final hindrance named, closing the list this "
         "discourse claims is complete."),
    ],
    text_intro=(
        "The discourse in full: a single claim, the five hindrances named, and the claim "
        "restated. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.52:1.1-1.6"),
    ],
    quiz=[
        {"q": "What claim does this discourse make about the five hindrances?",
         "opts": [
             "That they are one example among many kinds of unskillfulness",
             "That, rightly speaking, they entirely constitute a heap of the unskillful",
             "That only three of the five hindrances are truly unskillful",
             "That the hindrances are morally neutral"],
         "correct": 1,
         "expl": "A claim of totality, not mere membership in a category."},
        {"q": "What does 'kevalo', entirely, mark in this discourse?",
         "opts": [
             "Nothing significant",
             "That the hindrances exhaust the category of the unskillful, rather than being "
             "merely one part of it",
             "That only one hindrance matters",
             "A qualification limiting the claim's scope"],
         "correct": 1,
         "expl": "The word doing the discourse's real work, per the guide's reading."},
        {"q": "What does 'sammā vadamāno vadeyya', rightly speaking, one would say, frame this "
              "claim as?",
         "opts": [
             "A joke or exaggeration",
             "A matter of correct description, staking out a specific position on how "
             "'unskillful' ought to be used for this list",
             "An open question with no answer given",
             "A quotation from an unnamed source"],
         "correct": 1,
         "expl": "Not rhetorical flourish, but a claim about accurate terminology."},
        {"q": "What structure does this discourse's entire text follow?",
         "opts": [
             "An extended narrative with multiple characters",
             "A single claim stated, the five hindrances named, and the identical claim restated "
             "as its own conclusion",
             "A dialogue between the Buddha and a questioner",
             "A long simile with several stages"],
         "correct": 1,
         "expl": "No simile or argument beyond the assertion itself, matching its own totalizing content."},
        {"q": "How does this discourse's claim compare in strength to AN 5.51's treatment of the "
              "same five states?",
         "opts": [
             "Identical in every respect",
             "Stronger — AN 5.51 described their effect on wisdom; this discourse claims they "
             "exhaust the category of unskillfulness itself",
             "Weaker than AN 5.51's claim",
             "Unrelated to AN 5.51"],
         "correct": 1,
         "expl": "A bolder, more totalizing claim than the previous discourse made."},
        {"q": "What five hindrances does this discourse name?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Sensual desire, ill will, dullness and drowsiness, restlessness and remorse, and "
             "doubt",
             "Long life, beauty, happiness, fame, heaven",
             "Iron, copper, tin, lead, silver"],
         "correct": 1,
         "expl": "The identical five items named at AN 5.51, in the same order."},
        {"q": "Does this discourse offer any simile to illustrate its claim?",
         "opts": [
             "Yes, the river simile from AN 5.51",
             "No — a bare assertion with no illustration at all",
             "Yes, a new simile unique to this discourse",
             "Yes, the gold-refining simile"],
         "correct": 1,
         "expl": "The shortest and most direct discourse in this chapter."},
        {"q": "How long is this discourse?",
         "opts": [
             "Several minutes, with extended argument",
             "About twenty seconds — the shortest in this chapter",
             "Identical in length to AN 5.51",
             "This discourse has no readable text"],
         "correct": 1,
         "expl": "A single sentence, stated and then restated as conclusion."},
        {"q": "What comes next in this chapter?",
         "opts": [
             "A return to giving and wealth",
             "AN 5.53, on five factors that support meditation",
             "The chapter's final discourse",
             "A repeat of AN 5.52"],
         "correct": 1,
         "expl": "A shift from what obstructs meditation to what makes it possible."},
        {"q": "Where is AN 5.52 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("The claim", [
            "the five hindrances,",
            "<span class=\"pali\">kevalo</span>entirely,",
            "a heap of the unskillful",
        ]),
        ("Totality, not membership", [
            "not: one example among",
            "many unskillful things",
            "but: the whole category",
        ]),
        ("No argument needed", [
            "stated once,",
            "restated as conclusion",
            "&mdash; nothing more to add",
        ]),
        ("Cross-references", [
            "AN 5.51 &middot; the same five, weakening wisdom",
            "AN 5.23 &middot; the corruptions, first named",
            "AN 5.53 &middot; next: what supports meditation",
        ]),
    ],
    further=[
        '<a href="%s/an5.52/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.51.html">AN 5.51 &middot; Obstacles</a> &mdash; the previous discourse, on '
        "the same five states and their effect on wisdom.",
        '<a href="an-5.53.html">AN 5.53 &middot; Factors That Support Meditation</a> &mdash; '
        "next, turning from obstruction to support.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; the earlier appearance of '
        "this same five-item list, under a third name.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.53 — Padhāniyaṅgasutta
# --------------------------------------------------------------------------- #
page(
    53, "Padhāniyaṅga", "Factors That Support Meditation",
    vagga=VAGGA_6,
    meta_title="AN 5.53 — Factors That Support Meditation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Padhāniyaṅgasutta — "
        "five factors supporting meditation, and the one genuinely surprising item among them: "
        "good digestion, named alongside faith, honesty, energy, and wisdom. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five factors named in sequence, each described briefly, with no closing verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Physical health and digestion named as conditions for effective "
                              "meditation recur across the Chinese Āgamas' monastic-conduct "
                              "material; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a list mixing the doctrinal "
                       "and the bodily without apparent embarrassment"),
    ],
    why=(
        "Having just named what obstructs the mind and called it, entirely, a heap of the "
        "unskillful, this discourse turns to what actually supports the work of meditation "
        "&mdash; and the list it gives is not purely doctrinal. Faith and wisdom appear, in "
        "their usual formulas, but so does something unexpected: a stomach that digests well, "
        "<em>neither too hot nor too cold, but just right</em>."),
    guide=[
        ("The teaching in one sentence", [
            "Five factors support meditation: faith in the Buddha's awakening, freedom from "
            "illness with good digestion, honesty with one's teacher and companions, energy "
            "roused up for skillful qualities, and wisdom into arising and passing away."]),
        ("Three definitions inherited without change", [
            "Faith (the nine-quality recollection of the Buddha), energy (roused up for giving "
            "up the unskillful and taking up the skillful), and wisdom (insight into arising and "
            "passing away) are worded here exactly as this nipāta has worded them every other "
            "time. This discourse adds nothing new to any of the three; what is genuinely new "
            "sits in the second and third factors."]),
        ("A body that cooperates", [
            "The second factor is entirely physical: rarely ill, and possessing "
            "<em>samavepākiniyā gahaṇiyā</em>, an evenly-digesting constitution, "
            "<em>nātisītāya nāccuṇhāya majjhimāya</em>, neither too cold nor too hot, but "
            "moderate. This is a striking item to find alongside faith and wisdom in a list "
            "supporting meditation &mdash; the discourse treats bodily digestion as no less "
            "relevant to sustained practice than confidence in the teacher, without apparent "
            "embarrassment at the mixture."]),
        ("Honesty as a support, not only a virtue", [
            "The third factor, <em>asaṭho amāyāvī</em>, not devious or deceitful, is framed "
            "specifically around revealing oneself <em>honestly to the Teacher or sensible "
            "spiritual companions</em>. This is honesty in service of a practical function: "
            "concealment from those positioned to help would itself become an obstacle, so "
            "transparency is named as a condition for meditation to proceed rather than only as "
            "an independent ethical requirement."]),
        ("Support, not guarantee", [
            "Nothing in this list promises that meditation will succeed once these five factors "
            "are present; the discourse's title names them as what <em>supports</em> meditation, "
            "<em>padhāniyaṅga</em>, not what produces its result automatically. Compare this to "
            "AN 5.54, the very next discourse, which will name external circumstances that make "
            "meditation more or less possible in the first place &mdash; support operating at a "
            "second, different level entirely."]),
    ],
    terms=[
        ("padhāniyaṅga",
         "&ldquo;factor supporting meditation&rdquo; &mdash; this discourse's title, naming "
         "conditions for practice rather than a guarantee of its result."),
        ("samavepākiniyā gahaṇiyā",
         "&ldquo;evenly-digesting constitution&rdquo; &mdash; the striking physical item among "
         "the five, digestion neither too hot nor too cold."),
        ("asaṭho amāyāvī",
         "&ldquo;not devious or deceitful&rdquo; &mdash; the third factor, honesty framed "
         "specifically toward one's teacher and companions."),
        ("padhānakkhamā",
         "&ldquo;fit for meditation&rdquo; &mdash; the word describing the ideal digestive state, "
         "linking bodily comfort directly to meditative capacity."),
        ("udayatthagāminī paññā",
         "&ldquo;wisdom of arising and passing away&rdquo; &mdash; the fifth factor, worded "
         "identically to every other use of this formula in this nipāta."),
    ],
    text_intro=(
        "The discourse in full: the five factors that support meditation, named in sequence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Faith"),
        ("p", "&sect;1", "an5.53:1.1-1.2"),
        ("h3", "Health and digestion"),
        ("p", "&sect;2", "an5.53:1.3-1.4"),
        ("h3", "Honesty"),
        ("p", "&sect;3", "an5.53:1.5-1.6"),
        ("h3", "Energy"),
        ("p", "&sect;4", "an5.53:1.7-1.8"),
        ("h3", "Wisdom"),
        ("p", "&sect;5", "an5.53:1.9"),
        ("p", "&sect;6", "an5.53:1.10-1.11"),
    ],
    quiz=[
        {"q": "What five factors does this discourse say support meditation?",
         "opts": [
             "The five hindrances",
             "Faith, freedom from illness with good digestion, honesty with teacher and "
             "companions, energy, and wisdom",
             "The five powers of a trainee",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "A mix of doctrinal and physical factors."},
        {"q": "Which factor does the guide flag as genuinely surprising to find in this list?",
         "opts": [
             "Faith",
             "Good digestion — a physical condition alongside faith and wisdom",
             "Wisdom",
             "Energy"],
         "correct": 1,
         "expl": "A striking bodily item, treated as no less relevant than doctrinal confidence."},
        {"q": "How is the ideal digestive state described?",
         "opts": [
             "Extremely hot",
             "Neither too hot nor too cold, but moderate and fit for meditation",
             "Irrelevant to meditation entirely",
             "Only relevant for elderly mendicants"],
         "correct": 1,
         "expl": "Samavepākiniyā gahaṇiyā, nātisītāya nāccuṇhāya majjhimāya."},
        {"q": "How is the third factor, honesty, specifically framed?",
         "opts": [
             "As an abstract virtue unrelated to practice",
             "As revealing oneself honestly to the Teacher or sensible companions — a practical "
             "condition, since concealment would itself become an obstacle",
             "As honesty in business dealings",
             "As honesty only in written records"],
         "correct": 1,
         "expl": "Framed around a specific practical function, not only as independent ethics."},
        {"q": "Are faith, energy, and wisdom defined any differently here than elsewhere in this "
              "nipāta?",
         "opts": [
             "Yes, with entirely new formulas",
             "No — worded identically to every other use of these formulas in this nipāta",
             "Only wisdom differs",
             "Only faith differs"],
         "correct": 1,
         "expl": "No new content added to these three; what's new sits in the second and third factors."},
        {"q": "What does the guide say this discourse's title, 'padhāniyaṅga', promises?",
         "opts": [
             "Guaranteed success in meditation",
             "Support for meditation, not an automatic guarantee of its result",
             "Nothing; the title is decorative",
             "A specific timeline for attainment"],
         "correct": 1,
         "expl": "Conditions for practice, distinct from a promise of outcome."},
        {"q": "How does the guide connect this discourse to AN 5.54, the next one?",
         "opts": [
             "As identical in content",
             "As support operating at a different level — AN 5.54 names external circumstances "
             "rather than personal qualities",
             "As contradictory discourses",
             "AN 5.54 is unrelated to meditation"],
         "correct": 1,
         "expl": "Two different kinds of 'support' for meditation, personal versus circumstantial."},
        {"q": "Does this discourse close with verses, like most discourses in this chapter?",
         "opts": [
             "Yes, extensive verses",
             "No — it ends directly after naming the five factors, with no verse",
             "Yes, but only two lines",
             "The discourse has no prose at all, only verse"],
         "correct": 1,
         "expl": "A plain prose list with no poetic close."},
        {"q": "What does the faith factor's formula consist of?",
         "opts": [
             "A vow of poverty",
             "The nine-quality recollection of the Buddha's awakening",
             "A pledge of loyalty to a teacher",
             "A meditation on impermanence"],
         "correct": 1,
         "expl": "The same buddhānussati formula used throughout this nipāta."},
        {"q": "Where is AN 5.53 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five factors", [
            "faith &middot; health/digestion",
            "honesty &middot; energy",
            "wisdom",
        ]),
        ("An unexpected item", [
            "good digestion,",
            "named alongside",
            "faith and wisdom",
        ]),
        ("Support, not guarantee", [
            "<span class=\"pali\">padhāniyaṅga</span>",
            "&mdash; conditions,",
            "not automatic success",
        ]),
        ("Cross-references", [
            "AN 5.52 &middot; obstruction, entirely",
            "AN 5.54 &middot; next: external conditions",
            "AN 5.2 &middot; the faith formula, first",
        ]),
    ],
    further=[
        '<a href="%s/an5.53/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.52.html">AN 5.52 &middot; A Heap of the Unskillful</a> &mdash; the '
        "previous discourse, on what obstructs rather than what supports.",
        '<a href="an-5.54.html">AN 5.54 &middot; Times Good for Meditation</a> &mdash; next, '
        "external circumstances rather than personal qualities.",
        '<a href="an-5.2.html">AN 5.2 &middot; In Detail</a> &mdash; where the faith and wisdom '
        "formulas reused here first appeared in this nipāta.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.54 — Samayasutta
# --------------------------------------------------------------------------- #
page(
    54, "Samaya", "Times Good for Meditation",
    vagga=VAGGA_6,
    meta_title="AN 5.54 — Times Good for Meditation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samayasutta — five "
        "times unsuited to meditation, from illness to a schism in the Saṅgha, mirrored by five "
        "times well suited to it, admitting that circumstance shapes practice. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Five unfavorable circumstances named in turn, then their five favorable "
                 "mirrors, with no closing verse"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Naming external social and institutional conditions as relevant "
                              "to meditation practice recurs across the Chinese Āgamas' monastic "
                              "material; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; an unusually candid admission "
                       "that circumstance, not only willpower, shapes practice"),
    ],
    why=(
        "AN 5.53 named factors internal to a person as support for meditation. This discourse "
        "names something different: circumstances entirely outside a mendicant's control that "
        "make meditation more or less possible in the first place. Old age, sickness, famine, "
        "civil unrest, and a schism in the Saṅgha are named, without qualification, as times "
        "meditation does not go well &mdash; a admission this reading guide will not soften into "
        "a claim that sufficiently determined practice can simply override any circumstance."),
    guide=[
        ("The teaching in one sentence", [
            "Five times are not good for meditation &mdash; old age, sickness, famine, wilderness "
            "unrest, and a schism in the Saṅgha &mdash; and five mirror times are good for it: "
            "youth, health, abundance, social harmony, and harmony within the Saṅgha."]),
        ("Circumstance, named without euphemism", [
            "Two of the five unfavorable conditions are bodily &mdash; old age and sickness, "
            "conditions any individual mendicant might simply have no choice about. The other "
            "three are social and institutional: famine making almsfood hard to get, "
            "<em>aṭavisaṅkopo</em>, turmoil in the wilds severe enough that country people flee "
            "with their vehicles, and a split Saṅgha where members <em>abuse, insult, block, and "
            "forsake each other</em>. None of these five is framed as something meditation "
            "itself can simply overcome; they are named as conditions under which meditation is, "
            "factually, harder."]),
        ("A schism's specific damage", [
            "The fifth unfavorable time receives the most detailed description of any item on "
            "either list: a divided Saṅgha does not merely inconvenience its members but "
            "actively <em>doesn't inspire confidence in those without it, and causes some with "
            "confidence to change their minds</em>. Institutional conflict is treated here as "
            "having consequences beyond the immediate community &mdash; it damages the "
            "teaching's standing with outsiders and unsettles even committed supporters."]),
        ("The mirror list, exact and complete", [
            "Every unfavorable condition has a named favorable counterpart: youth in place of "
            "old age, health in place of sickness, abundance in place of famine, social harmony "
            "in place of unrest, and a harmonious Saṅgha <em>with one recitation</em> in place "
            "of schism. The parallel structure makes the discourse's point almost visually: these "
            "are not separate concerns but the same five variables, each capable of running "
            "either direction."]),
        ("What this discourse does not claim", [
            "Nothing here says a mendicant facing an unfavorable time should give up on "
            "meditation altogether, and nothing claims a favorable time guarantees success. The "
            "discourse's contribution is narrower and, arguably, more honest than either "
            "extreme: circumstance is a real variable in whether meditation goes well, worth "
            "naming plainly rather than folding into a purely individual account of practice and "
            "effort."]),
    ],
    terms=[
        ("asamaya samaya",
         "&ldquo;bad time, good time&rdquo; &mdash; the paired terms structuring this "
         "discourse's two matching lists."),
        ("aṭavisaṅkopo",
         "&ldquo;turmoil in the wilds&rdquo; &mdash; the fourth unfavorable condition, severe "
         "enough that country people flee with their vehicles."),
        ("saṅgho bhinno",
         "&ldquo;a split Saṅgha&rdquo; &mdash; the fifth and most fully described unfavorable "
         "condition, with consequences reaching beyond the immediate community."),
        ("khīrodakībhūtā",
         "&ldquo;blending like milk and water&rdquo; &mdash; the image for social harmony among "
         "the favorable conditions, a close, inseparable mixture."),
        ("ekuddesa",
         "&ldquo;with one recitation&rdquo; &mdash; the mark of a harmonious Saṅgha, reciting the "
         "monastic code together rather than splitting into factions."),
    ],
    text_intro=(
        "The discourse in full: the five times unfavorable for meditation, and their five "
        "favorable mirrors. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five times not good for meditation"),
        ("p", "&sect;1", "an5.54:1.1-1.2"),
        ("p", "&sect;2", "an5.54:1.3-1.4"),
        ("p", "&sect;3", "an5.54:2.1-2.2"),
        ("p", "&sect;4", "an5.54:3.1-3.2"),
        ("p", "&sect;5", "an5.54:4.1-4.2"),
        ("p", "&sect;6", "an5.54:5.1-5.4"),
        ("p", "&sect;7", "an5.54:5.5"),
        ("h3", "Five times good for meditation"),
        ("p", "&sect;8", "an5.54:6.1-6.2"),
        ("p", "&sect;9", "an5.54:6.3-6.4"),
        ("p", "&sect;10", "an5.54:7.1-7.2"),
        ("p", "&sect;11", "an5.54:8.1-8.2"),
        ("p", "&sect;12", "an5.54:9.1-9.2"),
        ("p", "&sect;13", "an5.54:10.1-10.4"),
        ("p", "&sect;14", "an5.54:10.5"),
    ],
    quiz=[
        {"q": "What five times does this discourse name as unfavorable for meditation?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Old age, sickness, famine, wilderness unrest, and a schism in the Saṅgha",
             "Long life, beauty, happiness, fame, and heaven",
             "The five hindrances"],
         "correct": 1,
         "expl": "Two bodily conditions and three social/institutional ones."},
        {"q": "Does this discourse frame meditation as able to simply overcome any of these five "
              "unfavorable conditions?",
         "opts": [
             "Yes, meditation is claimed to override all circumstances",
             "No — the five are named as conditions under which meditation is, factually, harder, "
             "without claiming willpower alone resolves this",
             "The discourse takes no clear position",
             "Only sickness is said to be overridable"],
         "correct": 1,
         "expl": "A candid admission that circumstance is a real variable, not merely an excuse to be dismissed."},
        {"q": "What does the discourse say about the consequences of a Saṅgha schism?",
         "opts": [
             "Only that it inconveniences its own members",
             "That it doesn't inspire confidence in those without it and causes some with "
             "confidence to change their minds — damage reaching beyond the immediate community",
             "That it has no real effect at all",
             "That it only affects the monks involved directly"],
         "correct": 1,
         "expl": "The most detailed description on either list, extending beyond internal effects."},
        {"q": "What is the mirror condition for old age among the five favorable times?",
         "opts": [
             "Wealth", "Youth, described in physical terms as pristine black hair and the prime "
             "of life", "Fame", "Wisdom"],
         "correct": 1,
         "expl": "An exact structural mirror to the first unfavorable condition."},
        {"q": "How does the guide describe the parallel structure between the two five-item "
              "lists?",
         "opts": [
             "As coincidental, with no real connection",
             "As the same five variables, each capable of running either direction, making the "
             "point almost visually",
             "As contradictory lists",
             "As unrelated to each other"],
         "correct": 1,
         "expl": "An exact, one-to-one mirroring across both lists."},
        {"q": "What image describes social harmony among the favorable conditions?",
         "opts": [
             "Fire and water, opposing forces",
             "Blending like milk and water — a close, inseparable mixture",
             "Two rivers running parallel but never meeting",
             "No image is given"],
         "correct": 1,
         "expl": "Khīrodakībhūtā, a classic image of seamless combination."},
        {"q": "What does the guide say this discourse does NOT claim?",
         "opts": [
             "That circumstance matters at all",
             "That a mendicant facing bad conditions should give up meditation, or that good "
             "conditions guarantee success",
             "That old age and sickness are real conditions",
             "That the Saṅgha's harmony matters"],
         "correct": 1,
         "expl": "A narrower, more honest contribution than either extreme claim."},
        {"q": "How many of the five unfavorable conditions concern the individual body, versus "
              "social or institutional circumstances?",
         "opts": [
             "All five are bodily",
             "Two bodily (old age, sickness), three social or institutional (famine, unrest, "
             "schism)",
             "None are bodily; all are social",
             "Four bodily, one social"],
         "correct": 1,
         "expl": "A mix spanning individual and communal levels."},
        {"q": "How does this discourse relate to AN 5.53's account of what supports meditation?",
         "opts": [
             "It repeats AN 5.53 exactly",
             "It names external circumstances, a different level of support than AN 5.53's "
             "personal qualities like faith and honesty",
             "It contradicts AN 5.53 entirely",
             "It has no relation to AN 5.53"],
         "correct": 1,
         "expl": "Two distinct kinds of factors bearing on whether meditation goes well."},
        {"q": "Where is AN 5.54 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five bad times", [
            "old age &middot; sickness",
            "famine &middot; unrest",
            "Saṅgha schism",
        ]),
        ("Five good times", [
            "youth &middot; health",
            "abundance &middot; harmony",
            "Saṅgha unity",
        ]),
        ("An honest admission", [
            "circumstance shapes practice",
            "&mdash; not only",
            "individual willpower",
        ]),
        ("Cross-references", [
            "AN 5.53 &middot; personal support factors",
            "AN 5.55 &middot; next: Mother and Son",
            "AN 5.51 &middot; obstacles, internal",
        ]),
    ],
    further=[
        '<a href="%s/an5.54/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.53.html">AN 5.53 &middot; Factors That Support Meditation</a> &mdash; the '
        "previous discourse, on personal rather than circumstantial support.",
        '<a href="an-5.55.html">AN 5.55 &middot; Mother and Son</a> &mdash; next, a stark case '
        "study in what unguarded intimacy, even during a good time for practice, can still "
        "produce.",
        '<a href="an-5.51.html">AN 5.51 &middot; Obstacles</a> &mdash; the chapter&rsquo;s '
        "opening discourse, on obstruction internal to the mind rather than external circumstance.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.55 — Mātāputtasutta
# --------------------------------------------------------------------------- #
page(
    55, "Mātāputta", "Mother and Son",
    vagga=VAGGA_6,
    meta_title="AN 5.55 — Mother and Son | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mātāputtasutta — a "
        "monk and his own mother, a nun, grow too close during a shared rains retreat and break "
        "their vows, prompting one of the canon's starkest warnings about desire, addressed "
        "specifically to a male monastic audience. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery; stated at the head of "
                    "AN 5.55"),
        ("Speakers", "The Buddha, addressing mendicants after being told what happened"),
        ("Form", "A reported incident, a five-step causal chain explaining how it happened, the "
                 "Buddha's direct response, and verses warning against unguarded closeness"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Warnings against unguarded closeness between monastics and the "
                              "opposite sex recur across Vinaya-adjacent literature in the "
                              "Chinese tradition; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; &mdash; the most difficult discourse "
                       "in this chapter, requiring direct acknowledgment of its content and its "
                       "limits"),
    ],
    why=(
        "This reading guide will state plainly what this discourse contains and does not "
        "soften it: a monk and his own mother, ordained as a nun, break their monastic vows "
        "together after growing too close during a shared rains retreat. The Buddha's response "
        "does not excuse this, but it also does not stop at condemning the two individuals; it "
        "generalizes into some of the starkest language in the collection about the danger a "
        "woman's presence is said to pose to a man's mind. This is addressed specifically to a "
        "male monastic audience managing a specific historical anxiety about desire, and this "
        "reading guide presents it as such rather than as this series&rsquo; own claim about "
        "women's nature."),
    guide=[
        ("The teaching in one sentence", [
            "A monk and his mother, a nun, who wanted to see each other often during a shared "
            "rains retreat grew close, then intimate, then overcome by lust, and had sex without "
            "formally leaving the training first; when told of this, the Buddha names how "
            "closeness of this kind develops and warns, in the strongest terms available to him, "
            "against unguarded proximity between a man and a woman."]),
        ("A five-step chain, named without blame at any single step", [
            "The discourse traces exactly how this happened, as a causal sequence: wanting to "
            "see each other often, leading to frequent seeing, leading to closeness "
            "(<em>saṁsagga</em>), leading to intimacy (<em>vissāsa</em>), leading to an opening "
            "for lust (<em>otāra</em>) that finally overcame them. No single step in this chain "
            "is itself framed as the transgression; the transgression is what the completed chain "
            "produced. This mirrors a structural pattern this nipāta has used before, at AN "
            "5.24's causal chain and AN 5.26's opportunity-chain, applied here to a case where "
            "the momentum runs toward harm rather than freedom."]),
        ("The Buddha's response, and what it does not say", [
            "The Buddha's first words &mdash; <em>how could that futile man imagine that a "
            "mother cannot lust for her son, or a son for his mother?</em> &mdash; refuse to let "
            "kinship be treated as automatic protection against desire. This reading guide reads "
            "this as a direct, unflinching acknowledgment of how thoroughly desire can operate, "
            "not as commentary on the mother and son&rsquo;s particular characters. What the "
            "discourse does not do is excuse what happened; it explains the mechanism honestly "
            "while still treating the outcome as a serious breach."]),
        ("What follows, and its intended audience", [
            "What comes next is addressed to a male monastic audience specifically, using the "
            "grammatical masculine throughout: no sight, sound, smell, taste, or touch is named "
            "as more arousing or more of an obstacle to freedom than a woman's; a woman is called "
            "<em>an all-round snare of Māra</em>; the verses counsel that one should sooner sit "
            "beside an armed stranger or a venomous snake than talk alone with a woman. This "
            "reading guide states this content directly rather than paraphrasing it into "
            "something gentler, because softening it would misrepresent both the discourse and "
            "the seriousness of what it is actually claiming."]),
        ("Reading this discourse honestly, without endorsing its frame", [
            "This is a text produced within and for a celibate male monastic community managing "
            "a specific, historically situated anxiety: how physical closeness with women "
            "specifically threatened the vows those particular listeners had taken. It is not "
            "presented here as this series' own claim that women are inherently dangerous, nor "
            "as a template for how anyone should regard anyone else today. The honest response "
            "to a text like this is neither to erase it from the record nor to repeat its "
            "framing as though this reading guide endorsed it; it is to state clearly what "
            "audience it addresses, what problem it is actually trying to solve, and what "
            "remains genuinely useful in it &mdash; the causal chain from casual contact to "
            "crossed vows applies to more situations than this one, even where the discourse's "
            "gendered framing does not travel."]),
    ],
    terms=[
        ("vassāvāsa",
         "&ldquo;rains residence&rdquo; &mdash; the shared retreat period during which the "
         "mother and son's closeness developed."),
        ("saṁsagga vissāsa otāra",
         "&ldquo;closeness, intimacy, an opening&rdquo; &mdash; the three middle steps of the "
         "five-step chain from frequent contact to lust overcoming both parties."),
        ("moghapurisa",
         "&ldquo;futile man&rdquo; &mdash; the Buddha's opening address, refusing the assumption "
         "that kinship alone would have prevented desire."),
        ("samantapāso mārassa",
         "&ldquo;an all-round snare of Māra&rdquo; &mdash; the discourse's starkest description "
         "of a woman, addressed to its male monastic audience specifically."),
        ("kāme pariññāya",
         "&ldquo;having fully understood sensual pleasures&rdquo; &mdash; the closing verse's "
         "positive counterpart, the state of one who has crossed over rather than been swept "
         "away."),
    ],
    text_intro=(
        "The discourse in full: the incident, its causal chain, the Buddha's response, and the "
        "closing verses. This page presents the discourse's content directly, including language "
        "addressed to a specific historical male monastic audience that this reading guide does "
        "not endorse as a general claim. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "What happened"),
        ("p", "&sect;1", "an5.55:1.1"),
        ("p", "&sect;2", "an5.55:1.2-1.10"),
        ("p", "&sect;3", "an5.55:2.1-2.4"),
        ("h3", "The Buddha's response"),
        ("p", "&sect;4", "an5.55:3.1-3.5"),
        ("p", "&sect;5", "an5.55:4.1-4.3"),
        ("p", "&sect;6", "an5.55:5.1-5.5"),
        ("h3", "The closing verses"),
        ("p", "&sect;7", "an5.55:6.1-6.6"),
        ("p", "&sect;8", "an5.55:7.1-7.6"),
        ("p", "&sect;9", "an5.55:8.1-8.4"),
        ("p", "&sect;10", "an5.55:9.1-9.4"),
        ("p", "&sect;11", "an5.55:10.1-10.4"),
    ],
    quiz=[
        {"q": "What incident does this discourse report?",
         "opts": [
             "A monk and a stranger breaking their vows",
             "A monk and his own mother, ordained as a nun, growing too close during a shared "
             "rains retreat and breaking their vows together",
             "Two unrelated monks arguing",
             "A theft in the monastery"],
         "correct": 1,
         "expl": "Reported to the Buddha by several mendicants after it occurred."},
        {"q": "What five-step chain does the discourse trace from wanting to see each other to "
              "the actual transgression?",
         "opts": [
             "No chain is described; it happened suddenly with no explanation",
             "Wanting frequent contact, leading to frequent seeing, closeness, intimacy, and "
             "finally an opening for lust that overcame them",
             "A single instantaneous decision with no preceding steps",
             "A plotted, premeditated plan"],
         "correct": 1,
         "expl": "A structural pattern mirroring AN 5.24's and AN 5.26's causal chains, here applied to a harmful outcome."},
        {"q": "What does the Buddha's opening question — 'how could that futile man imagine a "
              "mother cannot lust for her son?' — refuse to treat as automatic protection?",
         "opts": [
             "Monastic vows",
             "Kinship itself",
             "Old age",
             "Physical distance"],
         "correct": 1,
         "expl": "A direct acknowledgment that family relationship alone does not prevent desire from arising."},
        {"q": "How does the guide characterize the audience for the discourse's warnings about "
              "women?",
         "opts": [
             "As a universal claim about all people for all time",
             "As addressed specifically to a male monastic audience managing a historically "
             "situated anxiety about desire, not this series' own claim about women's nature",
             "As addressed equally to men and women",
             "As irrelevant to understanding the discourse"],
         "correct": 1,
         "expl": "Context the guide states explicitly rather than leaving unstated."},
        {"q": "Does this reading guide soften or paraphrase the discourse's starkest language, "
              "such as calling a woman 'an all-round snare of Māra'?",
         "opts": [
             "Yes, it removes this language entirely",
             "No — it states the content directly, judging that softening it would misrepresent "
             "the discourse and its seriousness",
             "It replaces the language with a modern equivalent",
             "It refuses to discuss this part of the discourse"],
         "correct": 1,
         "expl": "Direct presentation, with context, rather than erasure or repetition without comment."},
        {"q": "Does the Buddha's response excuse what the monk and his mother did?",
         "opts": [
             "Yes, entirely",
             "No — it explains the mechanism honestly while still treating the outcome as a "
             "serious breach",
             "The discourse takes no position on this",
             "Yes, and praises their actions"],
         "correct": 1,
         "expl": "Explanation of cause is distinguished from excuse in the guide's reading."},
        {"q": "What does the guide say remains genuinely useful in this discourse, even where its "
              "gendered framing does not travel to a general audience?",
         "opts": [
             "Nothing at all; the discourse should be disregarded entirely",
             "The causal chain from casual contact to crossed vows, which applies to more "
             "situations than this specific one",
             "Only its verses, not its prose",
             "Only the mother's perspective, which is absent from the text"],
         "correct": 1,
         "expl": "A structural insight the guide extracts from beneath the discourse's specific historical framing."},
        {"q": "What do the closing verses advise about being alone with a woman, compared to other "
              "risks?",
         "opts": [
             "That it is safer than any other risk",
             "That one should sooner sit beside an armed stranger or a venomous snake than talk "
             "alone, one on one, with a woman",
             "That it carries no particular risk at all",
             "That it is acceptable if brief"],
         "correct": 1,
         "expl": "Among the starkest comparisons in the collection, stated directly by this reading guide rather than hidden."},
        {"q": "What does the discourse's final verse describe as the alternative to being 'swept "
              "away' by desire?",
         "opts": [
             "Suppressing all sensation permanently",
             "Fully understanding sensual pleasures and living fearing nothing, having crossed "
             "over",
             "Avoiding all other people entirely",
             "The discourse offers no alternative"],
         "correct": 1,
         "expl": "Kāme pariññāya, the positive counterpart closing the discourse."},
        {"q": "Where is AN 5.55 set?",
         "opts": [
             "A new location, stated explicitly — Sāvatthī, in Jeta's Grove",
             "None restated",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 0,
         "expl": "Explicitly restated at the head of this discourse."},
    ],
    marginalia=[
        ("The five-step chain", [
            "wanting frequent contact &rarr;",
            "seeing often &rarr; closeness",
            "&rarr; intimacy &rarr; lust",
        ]),
        ("Named directly", [
            "&ldquo;a mother cannot",
            "lust for her son?&rdquo;",
            "&mdash; refused as an assumption",
        ]),
        ("Context stated plainly", [
            "addressed to male",
            "monastics specifically &mdash;",
            "not this guide's own claim",
        ]),
        ("Cross-references", [
            "AN 5.24 &middot; a related causal chain",
            "AN 5.26 &middot; another chain, toward freedom",
            "AN 5.56 &middot; next: a mentor's advice",
        ]),
    ],
    further=[
        '<a href="%s/an5.55/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.24.html">AN 5.24 &middot; Unethical</a> &mdash; an earlier causal chain in '
        "this nipāta, there tracing a path toward freedom rather than away from it.",
        '<a href="an-5.56.html">AN 5.56 &middot; Mentor</a> &mdash; next, a more encouraging case '
        "of a monk&rsquo;s difficulty resolved through practice.",
        '<a href="an-5.33.html">AN 5.33 &middot; With Uggaha</a> &mdash; this chapter&rsquo;s '
        "other discourse requiring the same honest, unflinching presentation of historically "
        "specific content.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.56 — Upajjhāyasutta
# --------------------------------------------------------------------------- #
page(
    56, "Upajjhāya", "Mentor",
    vagga=VAGGA_6,
    next=("an-5.57.html", "AN 5.57 &middot; Subjects for Regular Reviewing"),
    meta_title="AN 5.56 — Mentor | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Upajjhāyasutta — a "
        "mendicant reports feeling drugged, disoriented, drowsy, dissatisfied, and doubtful; the "
        "Buddha diagnoses the cause and prescribes the fix, and the mendicant, practicing alone, "
        "becomes an arahant. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", "An unnamed mendicant, his mentor, and the Buddha"),
        ("Form", "A symptom reported twice, a diagnosis and prescription, a report of complete "
                 "success, and the identical instruction repeated"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Mentor-mediated consultation with the Buddha over a specific "
                              "meditative difficulty recurs across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; after this chapter's "
                       "hardest discourse, one of its most encouraging"),
    ],
    why=(
        "After AN 5.55's account of practice failing badly, this discourse shows practice "
        "working completely, start to finish. A mendicant describes a cluster of symptoms with "
        "unusual precision &mdash; a drugged feeling in the body, disorientation, teachings that "
        "won't come to mind, drowsiness, dissatisfaction, doubt &mdash; and rather than treating "
        "any of this as a personal failing beyond remedy, the Buddha names a specific, "
        "correctable cause and gives a specific fix, which the mendicant then applies alone and "
        "which works completely."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant reporting a drugged, disoriented, drowsy, dissatisfied, and doubtful "
            "state is told this comes from unguarded senses, overeating, insufficient dedication "
            "to wakefulness, and neglecting the awakening factors, and instructed to reverse all "
            "five &mdash; which he does, alone, becoming an arahant."]),
        ("A precise cluster of symptoms, taken seriously", [
            "<em>Madhurakajāto kāyo</em>, a body that feels drugged, is an unusually vivid and "
            "specific complaint, and it is not treated as vague or dismissible. The mendicant "
            "names five distinct experiences &mdash; bodily heaviness, spatial disorientation, "
            "teachings that fail to surface in memory, dullness and drowsiness filling the mind, "
            "dissatisfaction with the spiritual life, and doubt about the teachings &mdash; and "
            "the Buddha's response engages with all five as a genuinely diagnosable condition, "
            "not a character flaw."]),
        ("Diagnosis, in four correctable causes", [
            "The Buddha names exactly what produces this state: unguarded sense doors, immoderate "
            "eating, insufficient dedication to wakefulness, and neglecting to discern skillful "
            "qualities and develop the awakening factors <em>in the evening and toward dawn</em>. "
            "Every one of these four is a matter of practice, not disposition &mdash; the "
            "discourse implies the mendicant's difficulty is not a fixed trait but a set of "
            "specific, correctable habits."]),
        ("The turnaround, reported in the mendicant's own words", [
            "The discourse gives the mendicant's transformed report the same precision as his "
            "original complaint, symptom by symptom, negated one at a time: no longer drugged, "
            "no longer disoriented, teachings now come to mind, no more drowsiness, satisfaction "
            "in the spiritual life, no doubt. This is not summarized as &lsquo;he "
            "improved&rsquo;; the discourse restates the entire original list in reverse, giving "
            "the recovery the same specificity as the original complaint."]),
        ("From individual instruction to general teaching", [
            "The Buddha's second delivery of this same instruction, after the mendicant's "
            "success, shifts address from singular <em>bhikkhu</em> to plural "
            "<em>bhikkhave</em> &mdash; the identical fix, now offered to the whole assembly "
            "rather than the one mendicant who needed it. A remedy that worked for one specific, "
            "precisely described case becomes, without modification, general instruction."]),
    ],
    terms=[
        ("madhurakajāto kāyo",
         "&ldquo;a body that feels drugged&rdquo; &mdash; the mendicant's opening complaint, an "
         "unusually vivid physical description."),
        ("indriyesu aguttadvāra",
         "&ldquo;unguarded sense doors&rdquo; &mdash; the first of four diagnosed causes of the "
         "mendicant's condition."),
        ("bhojane amattaññu",
         "&ldquo;not knowing moderation in eating&rdquo; &mdash; the second cause, overeating as "
         "a specific, correctable habit."),
        ("bodhipakkhiyā dhammā",
         "&ldquo;qualities on the side of awakening&rdquo; &mdash; the framework the fourth cause "
         "says was being neglected in the evening and toward dawn."),
        ("saddhivihārika",
         "&ldquo;co-resident, protégé&rdquo; &mdash; the term for the mendicant in relation to "
         "the mentor who brings him to the Buddha both times in this discourse."),
    ],
    text_intro=(
        "The discourse in full: the mendicant's complaint, the Buddha's diagnosis and "
        "instruction, the mendicant's success, and the same instruction restated for the whole "
        "assembly. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The complaint"),
        ("p", "&sect;1", "an5.56:1.1-1.2"),
        ("p", "&sect;2", "an5.56:2.1-2.3"),
        ("h3", "The diagnosis and instruction"),
        ("p", "&sect;3", "an5.56:3.1"),
        ("p", "&sect;4", "an5.56:3.2-3.4"),
        ("h3", "Practicing alone"),
        ("p", "&sect;5", "an5.56:4.1"),
        ("p", "&sect;6", "an5.56:4.2"),
        ("p", "&sect;7", "an5.56:4.3-4.4"),
        ("h3", "The turnaround, reported"),
        ("p", "&sect;8", "an5.56:5.1-5.2"),
        ("p", "&sect;9", "an5.56:5.3-5.5"),
        ("h3", "The same instruction, for everyone"),
        ("p", "&sect;10", "an5.56:6.1"),
        ("p", "&sect;11", "an5.56:6.2-6.4"),
    ],
    quiz=[
        {"q": "What five symptoms does the mendicant report to his mentor?",
         "opts": [
             "Physical pain, fever, hunger, thirst, and fatigue",
             "A drugged bodily feeling, disorientation, teachings not coming to mind, drowsiness, "
             "dissatisfaction, and doubt",
             "Anger, fear, greed, jealousy, and pride",
             "The five hindrances by their formal names"],
         "correct": 1,
         "expl": "A precise, specific cluster, taken seriously rather than dismissed."},
        {"q": "What four causes does the Buddha diagnose for this condition?",
         "opts": [
             "Fixed personal traits that cannot be changed",
             "Unguarded sense doors, overeating, insufficient dedication to wakefulness, and "
             "neglecting the awakening factors in the evening and toward dawn",
             "Poor diet alone",
             "Living in the wrong location"],
         "correct": 1,
         "expl": "Four correctable habits, not an unchangeable disposition."},
        {"q": "What does the mendicant do with this instruction?",
         "opts": [
             "Ignores it",
             "Applies it alone, diligently, and soon becomes an arahant",
             "Asks another teacher for a second opinion",
             "Gives up the training entirely"],
         "correct": 1,
         "expl": "Solitary, diligent practice leading to complete success."},
        {"q": "How does the discourse report the mendicant's eventual transformation?",
         "opts": [
             "With a brief summary: 'he improved'",
             "By restating the entire original symptom list in reverse, negating each item one "
             "at a time with the same specificity",
             "It does not report the outcome at all",
             "Only in verse, with no prose account"],
         "correct": 1,
         "expl": "The same precision applied to the recovery as to the original complaint."},
        {"q": "What shift happens when the Buddha delivers the same instruction a second time?",
         "opts": [
             "The instruction changes significantly",
             "The address shifts from singular 'bhikkhu' to plural 'bhikkhave' — the identical fix "
             "now offered to the whole assembly",
             "The instruction is contradicted",
             "A different set of causes is named"],
         "correct": 1,
         "expl": "An individual remedy becomes general teaching without modification."},
        {"q": "How does the guide contrast this discourse with AN 5.55, the previous one?",
         "opts": [
             "As identical in tone and outcome",
             "As showing practice working completely, after AN 5.55 showed practice failing badly",
             "As unrelated to AN 5.55",
             "As a direct continuation of the same narrative"],
         "correct": 1,
         "expl": "A deliberately encouraging discourse placed after the chapter's hardest one."},
        {"q": "What role does the mentor (upajjhāya) play in this discourse?",
         "opts": [
             "None; the mendicant approaches the Buddha alone",
             "He listens to the complaint and personally brings his protégé to the Buddha, both "
             "before and after the transformation",
             "He forbids the mendicant from seeking help",
             "He provides the diagnosis himself, without the Buddha's involvement"],
         "correct": 1,
         "expl": "An active, supportive role in both halves of the narrative."},
        {"q": "Is the mendicant's original condition treated as a moral failing?",
         "opts": [
             "Yes, he is condemned for it",
             "No — it is treated as a diagnosable, correctable condition arising from specific "
             "habits",
             "The discourse takes no position on this",
             "Yes, but only mildly"],
         "correct": 1,
         "expl": "A practical, almost clinical framing rather than a moralizing one."},
        {"q": "What term describes the mendicant's relationship to his mentor?",
         "opts": [
             "Sappurisa, true person",
             "Saddhivihārika, co-resident or protégé",
             "Sekha, trainee",
             "Ariyasāvako, noble disciple"],
         "correct": 1,
         "expl": "The standard term for a monk under a mentor's guidance."},
        {"q": "Where is AN 5.56 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five symptoms", [
            "drugged body &middot; lost",
            "teachings absent &middot; drowsy",
            "dissatisfied &middot; doubtful",
        ]),
        ("Four causes", [
            "unguarded senses",
            "overeating",
            "under-dedicated to waking",
            "awakening factors neglected",
        ]),
        ("Fully reversed", [
            "every symptom, negated",
            "one by one &mdash;",
            "then, arahantship",
        ]),
        ("Cross-references", [
            "AN 5.55 &middot; practice, failing",
            "AN 5.58 &middot; next: the Licchavi youths",
            "AN 5.51 &middot; the hindrances, this fix addresses",
        ]),
    ],
    further=[
        '<a href="%s/an5.56/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.55.html">AN 5.55 &middot; Mother and Son</a> &mdash; the previous '
        "discourse, this chapter's hardest case of unguarded closeness.",
        '<a href="an-5.51.html">AN 5.51 &middot; Obstacles</a> &mdash; the five hindrances this '
        "discourse's fix directly addresses, though never named explicitly here.",
        '<a href="an-5.58.html">AN 5.58 &middot; The Licchavi Youths</a> &mdash; next, a '
        "different kind of transformation observed from the outside.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.58 — Licchavikumārakasutta
# --------------------------------------------------------------------------- #
page(
    58, "Licchavikumāraka", "The Licchavi Youths",
    vagga=VAGGA_6,
    prev=("an-5.57.html", "AN 5.57 &middot; Subjects for Regular Reviewing"),
    meta_title="AN 5.58 — The Licchavi Youths | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Licchavikumārakasutta "
        "— violent, thieving young nobles are found silently paying homage to the Buddha, "
        "prompting a general teaching on what makes any leader's fortunes grow rather than "
        "decline. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood; the Buddha seated at the root of a tree after his "
                    "almsround"),
        ("Speakers", "Mahānāma the Licchavi, and the Buddha"),
        ("Form", "An observed scene, a bystander's exclamation and explanation, and a general "
                 "teaching on five conditions for a leader's growth"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Honoring family, dependents, and religious teachers as conditions "
                              "for a ruler's flourishing recurs across the Chinese Āgamas' "
                              "political-ethics material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a vivid character sketch "
                       "opening onto material already met once in this nipāta"),
    ],
    why=(
        "This discourse opens with a genuinely surprising image: a pack of Licchavi youths, "
        "described by their own townsman as violent, harsh, and given to stealing sweets and "
        "hitting girls, are found silently, respectfully paying homage to the seated Buddha, "
        "bows and hunting dogs set aside. Mahānāma's exclamation &mdash; <em>they will become "
        "Vajjis!</em> &mdash; becomes the occasion for the Buddha to generalize past this one "
        "scene into a teaching on what makes any leader's fortunes grow."),
    guide=[
        ("The teaching in one sentence", [
            "A gentleman in any position of leadership &mdash; king, official, general, chief, "
            "or clan ruler &mdash; can expect only growth, not decline, when he uses his "
            "legitimate wealth to honor his parents, his household, his business associates, the "
            "deities who receive spirit-offerings, and ascetics and brahmins."]),
        ("A scene worth pausing on before its lesson", [
            "The youths are not described neutrally: <em>caṇḍā pharusā apānubhā</em>, violent, "
            "harsh, brash, who steal sweets left out for families and hit girls of good families "
            "on their backs. The discourse does not soften this description to make the "
            "following scene more flattering; the contrast between what Mahānāma knows of them "
            "and what he now sees &mdash; silent, cupped-palm homage &mdash; is the whole point "
            "of his exclamation, and it only lands because the earlier description was left "
            "unflattering."]),
        ("&lsquo;They will become Vajjis&rsquo;", [
            "Mahānāma's exclamation is a specific compliment tied to the political identity of "
            "his own confederacy: to <em>become Vajjis</em>, in his mouth, means growing into "
            "the reputation the Vajjian confederation held for itself, presumably for competent, "
            "responsible leadership. The Buddha does not confirm or dwell on this reading of the "
            "youths' character; he moves directly to stating the general conditions under which "
            "any leader &mdash; not only these particular youths &mdash; can expect to flourish."]),
        ("The same wealth, the same five uses, restated for leaders", [
            "The five honored parties &mdash; parents, household and dependents, business "
            "associates, spirit-receiving deities, ascetics and brahmins &mdash; closely track "
            "<a href=\"an-5.41.html\">AN 5.41</a>'s five reasons to get rich from earlier in "
            "this nipāta, including the same frank inclusion of spirit-offerings without "
            "apology. What is new here is the frame: not an individual's personal satisfaction "
            "with how they used their wealth, but a structural claim about what determines "
            "whether any leader's position holds or erodes."]),
        ("Love repaid in the same words, five times over", [
            "Each of the five honored parties is said to respond identically: <em>ciraṁ jīva, "
            "dīghamāyuṁ pālehi</em>, live long, stay alive for a long time. The discourse does "
            "not vary this wish across parents, household, business partners, deities, or "
            "renunciates; the same blessing, repeated five times without change, becomes the "
            "discourse's own refrain for what honored parties give back."]),
    ],
    terms=[
        ("caṇḍā pharusā apānubhā",
         "&ldquo;violent, harsh, brash&rdquo; &mdash; Mahānāma's unflattering description of the "
         "youths before the scene that changes his assessment."),
        ("bhavissanti vajjī",
         "&ldquo;they will become Vajjis&rdquo; &mdash; Mahānāma's exclamation, tying the youths' "
         "changed bearing to his own confederacy's reputation."),
        ("vuddhi parihāni",
         "&ldquo;growth, decline&rdquo; &mdash; the paired outcomes this discourse's general "
         "teaching claims to determine for any leader."),
        ("khettakammantasāmantasabyohāra",
         "&ldquo;those who work neighboring fields, and business associates&rdquo; &mdash; the "
         "third honored party, extending the circle beyond household to economic relationships."),
        ("ciraṁ jīva dīghamāyuṁ pālehi",
         "&ldquo;live long, stay alive for a long time&rdquo; &mdash; the identical blessing "
         "repeated by all five honored parties."),
    ],
    text_intro=(
        "The discourse in full: the youths observed, Mahānāma's exclamation and explanation, and "
        "the general teaching on five conditions for a leader's growth. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha, seated in the wood"),
        ("p", "&sect;1", "an5.58:1.1"),
        ("p", "&sect;2", "an5.58:1.2-1.3"),
        ("h3", "The youths, homaging silently"),
        ("p", "&sect;3", "an5.58:2.1-2.2"),
        ("h3", "Mahānāma's exclamation"),
        ("p", "&sect;4", "an5.58:3.1-3.4"),
        ("p", "&sect;5", "an5.58:4.1-4.2"),
        ("p", "&sect;6", "an5.58:4.3-4.6"),
        ("h3", "Five conditions for growth"),
        ("p", "&sect;7", "an5.58:5.1-5.2"),
        ("p", "&sect;8", "an5.58:6.1-6.2"),
        ("p", "&sect;9", "an5.58:6.3-6.5"),
        ("p", "&sect;10", "an5.58:7.1-7.4"),
        ("p", "&sect;11", "an5.58:8.1-8.4"),
        ("p", "&sect;12", "an5.58:9.1-9.4"),
        ("p", "&sect;13", "an5.58:10.1-10.4"),
        ("p", "&sect;14", "an5.58:11.1-11.2"),
        ("h3", "The closing verses"),
        ("p", "&sect;15", "an5.58:12.1-12.4"),
        ("p", "&sect;16", "an5.58:13.1-13.4"),
        ("p", "&sect;17", "an5.58:14.1-14.4"),
        ("p", "&sect;18", "an5.58:15.1-15.4"),
    ],
    quiz=[
        {"q": "How does Mahānāma describe the Licchavi youths before he sees them paying homage?",
         "opts": [
             "As gentle and studious",
             "As violent, harsh, and brash — stealing sweets and hitting girls of good families",
             "As already devoted Buddhist practitioners",
             "As elderly and respected"],
         "correct": 1,
         "expl": "An unflattering description that makes the following scene's contrast land."},
        {"q": "What does Mahānāma exclaim upon seeing the youths silently paying homage?",
         "opts": [
             "'They will become monks!'",
             "'They will become Vajjis!' — tying their changed bearing to his own confederacy's "
             "reputation",
             "'They should be punished!'",
             "He says nothing at all"],
         "correct": 1,
         "expl": "A compliment specific to Licchavi/Vajjian political identity."},
        {"q": "What five parties does the Buddha's general teaching say a leader should honor with "
              "legitimate wealth?",
         "opts": [
             "Only the poor",
             "Parents, household and dependents, business associates, spirit-receiving deities, "
             "and ascetics and brahmins",
             "Only fellow rulers",
             "Only monastics"],
         "correct": 1,
         "expl": "A five-item list closely tracking AN 5.41's earlier account of wealth's proper uses."},
        {"q": "How does this list compare to AN 5.41's five reasons to get rich?",
         "opts": [
             "Entirely unrelated",
             "Closely tracking it, including the same frank inclusion of spirit-offerings without "
             "apology",
             "A direct contradiction",
             "Identical in every single word, with no variation"],
         "correct": 1,
         "expl": "The same underlying content, reframed here as a condition for leadership rather than personal satisfaction."},
        {"q": "What does each of the five honored parties say in response, according to the "
              "discourse?",
         "opts": [
             "Each says something different",
             "All five say the identical blessing: 'live long, stay alive for a long time'",
             "None respond at all",
             "Only the parents respond"],
         "correct": 1,
         "expl": "An unvarying refrain repeated five times."},
        {"q": "What outcome does this discourse claim follows from honoring all five parties?",
         "opts": [
             "Guaranteed decline",
             "Only growth, not decline, is to be expected",
             "No particular outcome is claimed",
             "Immediate enlightenment"],
         "correct": 1,
         "expl": "Vuddhiyeva pāṭikaṅkhā, no parihāni — the discourse's structural claim."},
        {"q": "What kinds of leaders does the Buddha's teaching apply to?",
         "opts": [
             "Only kings",
             "Any leadership position — an anointed king, an official, a general, a village or "
             "guild chief, or a clan ruler",
             "Only religious leaders",
             "Only military generals"],
         "correct": 1,
         "expl": "A broad, general claim about leadership as such, not confined to royalty."},
        {"q": "Does the Buddha confirm or dwell on Mahānāma's specific reading of the youths' "
              "character?",
         "opts": [
             "Yes, at great length",
             "No — he moves directly to a general teaching applicable beyond these particular "
             "youths",
             "He rejects Mahānāma's reading entirely",
             "He asks the youths to confirm it themselves"],
         "correct": 1,
         "expl": "The scene becomes an occasion for general teaching rather than commentary on these individuals specifically."},
        {"q": "What comes immediately before this discourse in the chapter's actual reading order?",
         "opts": [
             "AN 5.56",
             "AN 5.57, the legacy page this discourse's 'prev' link points to explicitly",
             "AN 5.51",
             "Nothing; this is the chapter's first discourse"],
         "correct": 1,
         "expl": "An explicit override, since AN 5.57 sits between AN 5.56 and AN 5.58 in sequence but is not regenerated."},
        {"q": "Where is AN 5.58 set?",
         "opts": [
             "A new location, stated explicitly — Vesālī, at the Great Wood",
             "None restated",
             "Sāvatthī",
             "Rājagaha"],
         "correct": 0,
         "expl": "Explicitly restated at the head of this discourse."},
    ],
    marginalia=[
        ("Before and after", [
            "violent, thieving youths",
            "&rarr; silent, cupped-palm",
            "homage to the Buddha",
        ]),
        ("Mahānāma's line", [
            "&ldquo;they will",
            "become Vajjis!&rdquo;",
        ]),
        ("Five honored parties", [
            "parents &middot; household",
            "business partners",
            "deities &middot; renunciates",
            "&mdash; same blessing, five times",
        ]),
        ("Cross-references", [
            "AN 5.41 &middot; the same five uses, first",
            "AN 5.57 &middot; the legacy page, before",
            "AN 5.59 &middot; next: hard to find, elderly",
        ]),
    ],
    further=[
        '<a href="%s/an5.58/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.41.html">AN 5.41 &middot; Getting Rich</a> &mdash; the earlier discourse '
        "this one's five honored parties closely track.",
        '<a href="an-5.56.html">AN 5.56 &middot; Mentor</a> &mdash; the preceding page in this '
        "chapter's reading order.",
        '<a href="an-5.59.html">AN 5.59 &middot; Gone Forth When Old (1st)</a> &mdash; next, a '
        "short pair of discourses on rarity among elderly ordainees.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.59 — Paṭhamavuḍḍhapabbajitasutta
# --------------------------------------------------------------------------- #
page(
    59, "Paṭhamavuḍḍhapabbajita", "Gone Forth When Old (1st)",
    vagga=VAGGA_6,
    meta_title="AN 5.59 — Gone Forth When Old (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first "
        "Vuḍḍhapabbajitasutta — five qualities rarely found together in someone who ordains "
        "late in life: sophistication, presentation, learning, teaching ability, and knowledge "
        "of the monastic law. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five qualities, each marked individually as rare"),
        ("Length", "~20 seconds to read"),
        ("Northern parallel", "Observations about the practical challenges facing those who "
                              "ordain later in life recur across Vinaya-adjacent literature in "
                              "the Chinese tradition; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, and notably free of "
                       "any judgment against those it describes"),
    ],
    why=(
        "This discourse names something practical rather than doctrinal: five qualities rarely "
        "found together in a person who has <em>gone forth when old</em>, entered monastic life "
        "later than the more typical youth. Each quality is marked rare individually, not "
        "collectively, which changes what the discourse is actually claiming."),
    guide=[
        ("The teaching in one sentence", [
            "It is hard to find someone gone forth when old who is sophisticated, "
            "well-presented, learned, able to teach the Dhamma, and has memorized the monastic "
            "law."]),
        ("Rarity, marked five times, not once", [
            "The Pāli repeats <em>dullabho</em>, hard to find, before each of the five qualities "
            "individually, rather than stating once that the whole package is rare. This is a "
            "small but real structural difference: the discourse is not only claiming the "
            "combination is uncommon, but that each individual quality on its own is not easily "
            "found in this specific population &mdash; late ordainees."]),
        ("No judgment attached", [
            "Nothing in this discourse criticizes those who ordain late in life, or suggests "
            "they should not have done so. It states a practical observation &mdash; certain "
            "qualities useful for teaching and preserving the monastic law take time most late "
            "ordainees have not had within the tradition &mdash; without moralizing about why "
            "someone came to the practice when they did."]),
        ("A companion discourse follows immediately", [
            "AN 5.60, the very next discourse, names a second set of five qualities equally rare "
            "in the same population, closing both this pair and the chapter itself. Together the "
            "two discourses give ten distinct qualities, none of them redundant with the other "
            "five, all concerning the same specific group."]),
    ],
    terms=[
        ("vuḍḍhapabbajita",
         "&ldquo;one gone forth when old&rdquo; &mdash; this discourse&rsquo;s subject, someone "
         "who ordained later in life than the more typical youth."),
        ("nipuṇa",
         "&ldquo;sophisticated, subtle&rdquo; &mdash; the first of the five rare qualities."),
        ("ākappasampanna",
         "&ldquo;well-presented&rdquo; &mdash; the second quality, concerning bearing and "
         "outward conduct."),
        ("dhammakathika",
         "&ldquo;one who can teach the Dhamma&rdquo; &mdash; the fourth quality, a specific "
         "practical skill rather than personal virtue."),
        ("vinayadhara",
         "&ldquo;one who has memorized the monastic law&rdquo; &mdash; the fifth quality, the "
         "kind of retention this nipāta has already marked as requiring time."),
    ],
    text_intro=(
        "The discourse in full: five qualities, each named rare in someone gone forth when old. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.59:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five qualities does this discourse say are hard to find in someone gone forth "
              "when old?",
         "opts": [
             "Wealth, family, health, friends, and status",
             "Sophistication, being well-presented, learning, teaching ability, and knowledge of "
             "the monastic law",
             "The five hindrances",
             "Faith, ethics, learning, generosity, and wisdom"],
         "correct": 1,
         "expl": "Practical, skill-based qualities, not moral judgments."},
        {"q": "How does the Pāli mark rarity — once for the whole set, or individually?",
         "opts": [
             "Once, for the combination as a whole",
             "Individually — 'dullabho' repeats before each of the five qualities separately",
             "Rarity is not mentioned at all",
             "Only the first quality is marked rare"],
         "correct": 1,
         "expl": "Each quality is claimed rare on its own, not only in combination."},
        {"q": "Does this discourse criticize those who ordain later in life?",
         "opts": [
             "Yes, strongly",
             "No — it states a practical observation without moralizing about the timing of "
             "someone's ordination",
             "Only implicitly",
             "Yes, but only for men"],
         "correct": 1,
         "expl": "A neutral, practical framing rather than a judgment."},
        {"q": "What does the guide say explains why these qualities might be rare in late "
              "ordainees specifically?",
         "opts": [
             "Personal moral failing",
             "Qualities useful for teaching and preserving the monastic law take time most late "
             "ordainees have not had within the tradition",
             "Late ordainees are said to lack the capacity to ever develop these qualities",
             "No explanation is offered anywhere"],
         "correct": 1,
         "expl": "A practical, time-based explanation rather than a claim about fixed capacity."},
        {"q": "What does AN 5.60, the very next discourse, do?",
         "opts": [
             "Repeats this discourse exactly",
             "Names a second, non-redundant set of five qualities equally rare in the same "
             "population, closing the pair and the chapter",
             "Contradicts this discourse",
             "Returns to the five hindrances"],
         "correct": 1,
         "expl": "Ten distinct qualities across the two discourses, none repeated."},
        {"q": "What does 'vinayadhara' mean?",
         "opts": [
             "One who breaks monastic rules",
             "One who has memorized the monastic law",
             "A synonym for arahant",
             "A lay supporter of the monastery"],
         "correct": 1,
         "expl": "The fifth quality, requiring significant time within the tradition to acquire."},
        {"q": "Is 'dhammakathika', ability to teach the Dhamma, a matter of personal virtue or "
              "practical skill?",
         "opts": [
             "Personal virtue exclusively",
             "A specific practical skill, distinct from moral character",
             "Neither; it is not defined at all",
             "It is identical to ethics"],
         "correct": 1,
         "expl": "A skill-based quality, consistent with the discourse's practical framing."},
        {"q": "How long is this discourse?",
         "opts": [
             "Several minutes, with an extended simile",
             "About twenty seconds — a single sentence with no elaboration",
             "Identical in length to AN 5.58",
             "This discourse has no readable text"],
         "correct": 1,
         "expl": "One of the shortest discourses in this chapter."},
        {"q": "Does this discourse offer a simile or narrative illustration?",
         "opts": [
             "Yes, an extended parable",
             "No — a direct, bare statement with no illustration",
             "Yes, the same story as AN 5.56",
             "Yes, a dialogue with a named questioner"],
         "correct": 1,
         "expl": "Consistent with the discourse's terse, practical form."},
        {"q": "Where is AN 5.59 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five rare qualities", [
            "sophisticated",
            "well-presented",
            "learned &middot; can teach",
            "knows the monastic law",
        ]),
        ("Marked individually", [
            "<span class=\"pali\">dullabho</span>",
            "&mdash; repeated five times,",
            "not stated once",
        ]),
        ("No judgment", [
            "a practical observation,",
            "not a criticism",
            "of late ordination",
        ]),
        ("Cross-references", [
            "AN 5.58 &middot; the previous discourse",
            "AN 5.60 &middot; next: a second five",
            "AN 5.47 &middot; learning, defined at length",
        ]),
    ],
    further=[
        '<a href="%s/an5.59/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.58.html">AN 5.58 &middot; The Licchavi Youths</a> &mdash; the previous '
        "discourse, on a very different kind of transformation.",
        '<a href="an-5.60.html">AN 5.60 &middot; Gone Forth When Old (2nd)</a> &mdash; next, this '
        "discourse's companion, closing the chapter.",
        '<a href="an-5.47.html">AN 5.47 &middot; Wealth</a> &mdash; where the wealth of learning '
        "this discourse presupposes was defined at length.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.60 — Dutiyavuḍḍhapabbajitasutta
# --------------------------------------------------------------------------- #
page(
    60, "Dutiyavuḍḍhapabbajita", "Gone Forth When Old (2nd)",
    vagga=VAGGA_6,
    meta_title="AN 5.60 — Gone Forth When Old (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second "
        "Vuḍḍhapabbajitasutta, closing this chapter — five more qualities rarely found in "
        "someone who ordains late in life, this time concerning how well they can still be "
        "taught. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming a second set of five qualities, each marked rare, "
                 "closing the chapter's own colophon"),
        ("Length", "~20 seconds to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.59"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, closing a chapter "
                       "that opened on the hindrances with a quiet, practical final note"),
    ],
    why=(
        "Where AN 5.59 named qualities of presentation and knowledge, this discourse turns to "
        "something different: how teachable a late ordainee still is. Easy to admonish, able to "
        "retain what is taught, and learning with the right attitude are named alongside the "
        "same two closing qualities from AN 5.59 &mdash; teaching ability and knowledge of the "
        "monastic law &mdash; closing this chapter on a note about receptivity to correction "
        "rather than accomplishment already achieved."),
    guide=[
        ("The teaching in one sentence", [
            "It is hard to find someone gone forth when old who is easy to admonish, retains "
            "what they learn, learns respectfully, can teach the Dhamma, and has memorized the "
            "monastic law."]),
        ("Three new qualities, about receptivity rather than achievement", [
            "<em>Suvaco</em>, easy to admonish, <em>suggahitaggāhī</em>, retaining what is "
            "grasped, and <em>padakkhiṇaggāhī</em>, learning in the right way &mdash; literally, "
            "grasping it clockwise, respectfully &mdash; all concern how a person receives "
            "correction and instruction, not what they have already accomplished. Read next to "
            "AN 5.59's sophistication and presentation, this discourse names the harder, more "
            "internal half of what makes a late ordainee's training go well."]),
        ("Two qualities repeated, unchanged", [
            "<em>Dhammakathika</em> and <em>vinayadhara</em>, teaching ability and knowledge of "
            "the monastic law, close both discourses identically. This is not filler repetition; "
            "these two skills genuinely matter regardless of how receptive or already "
            "accomplished the person is, and the pair of discourses agrees on that much even "
            "while differing on everything else."]),
        ("Ten qualities across two discourses, closing the chapter", [
            "AN 5.59 and 5.60 together name ten distinct qualities rarely found in a late "
            "ordainee &mdash; five concerning presentation and existing knowledge, five "
            "concerning receptivity and retention, with teaching ability and Vinaya knowledge "
            "anchoring both lists. The chapter that opened on what obstructs any mendicant's "
            "wisdom closes on a specific, practical account of what a particular group of "
            "mendicants often lacks &mdash; not through fault, but through the plain arithmetic "
            "of having started later."]),
        ("The chapter's own closing colophon", [
            "As at the close of every earlier chapter in this nipāta, the source appends "
            "<em>Nīvaraṇavaggo paṭhamo</em> &mdash; the first chapter, on hindrances, within the "
            "count that will restart with each subsequent nipāta &mdash; followed by the "
            "chapter's own untranslated uddāna verse, compressing all ten titles for "
            "memorization. The next chapter, Saññāvagga, turns to perception."]),
    ],
    terms=[
        ("suvaca",
         "&ldquo;easy to admonish&rdquo; &mdash; the first new quality, concerning openness to "
         "correction rather than existing accomplishment."),
        ("suggahitaggāhī",
         "&ldquo;retaining what is grasped&rdquo; &mdash; the second quality, memory retention "
         "specifically of instruction received."),
        ("padakkhiṇaggāhī",
         "&ldquo;learning respectfully&rdquo; &mdash; literally grasping clockwise, the "
         "traditional respectful direction, the third new quality."),
        ("dhammakathika vinayadhara",
         "&ldquo;one who can teach, one who knows the monastic law&rdquo; &mdash; the two "
         "qualities repeated unchanged from AN 5.59, closing both lists identically."),
        ("Nīvaraṇavaggo paṭhamo",
         "&ldquo;the first chapter, on hindrances&rdquo; &mdash; this vagga's closing colophon, "
         "matching the form already explained in full at AN 5.10."),
    ],
    text_intro=(
        "The discourse in full: five qualities concerning receptivity to teaching, rarely found "
        "in someone gone forth when old. The closing colophon and Pāli mnemonic verse are part "
        "of the source but are not translated text, and are described rather than reproduced "
        "here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.60:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five qualities does this discourse say are rare in someone gone forth when "
              "old?",
         "opts": [
             "Sophistication, presentation, learning, teaching ability, and Vinaya knowledge",
             "Being easy to admonish, retaining what is learned, learning respectfully, teaching "
             "ability, and Vinaya knowledge",
             "The five powers of a trainee",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "A second, non-redundant set of five, distinct from AN 5.59's."},
        {"q": "What do the three new qualities in this discourse concern, compared to AN 5.59's?",
         "opts": [
             "Existing accomplishment and outward presentation",
             "Receptivity to correction and instruction, rather than what has already been "
             "achieved",
             "Physical health",
             "Financial status"],
         "correct": 1,
         "expl": "The harder, more internal half of what makes training go well."},
        {"q": "What does 'padakkhiṇaggāhī' literally mean, and what does it signify?",
         "opts": [
             "'Grasping firmly' — physical strength",
             "'Grasping clockwise' — the traditional respectful direction, meaning learning with "
             "the right attitude",
             "'Grasping quickly' — fast comprehension only",
             "It has no specific literal meaning"],
         "correct": 1,
         "expl": "An image of respectful orientation toward what is being taught."},
        {"q": "What two qualities are repeated, unchanged, from AN 5.59?",
         "opts": [
             "Sophistication and being well-presented",
             "Teaching ability (dhammakathika) and knowledge of the monastic law (vinayadhara)",
             "Faith and wisdom",
             "None; all five qualities are new"],
         "correct": 1,
         "expl": "Two skills the guide notes matter regardless of the person's receptivity or existing accomplishment."},
        {"q": "How many total qualities do AN 5.59 and AN 5.60 name across both discourses?",
         "opts": [
             "Five, entirely overlapping",
             "Ten distinct qualities, with two shared between both lists",
             "Fifteen",
             "Three"],
         "correct": 1,
         "expl": "Eight unique qualities plus two repeated ones, anchoring both lists."},
        {"q": "What colophon closes this chapter?",
         "opts": [
             "No colophon is present",
             "Nīvaraṇavaggo paṭhamo, followed by the chapter's own untranslated uddāna verse",
             "A colophon naming a different chapter",
             "The colophon from AN 5.50, repeated verbatim"],
         "correct": 1,
         "expl": "Matching the structure already explained in full at AN 5.10."},
        {"q": "What chapter follows the Nīvaraṇavagga?",
         "opts": [
             "A return to the Muṇḍarājavagga",
             "The Saññāvagga, turning to perception",
             "The end of the entire nipāta",
             "A repeat of the Sekhabalavagga"],
         "correct": 1,
         "expl": "The next chapter in sequence, per this discourse's guide."},
        {"q": "Does this discourse frame the rarity of these qualities as a fault in late "
              "ordainees?",
         "opts": [
             "Yes, explicitly blaming them",
             "No — consistent with AN 5.59, a practical observation rather than a moral judgment",
             "Yes, but only mildly",
             "The discourse takes no clear position"],
         "correct": 1,
         "expl": "The same neutral framing carried over from the companion discourse."},
        {"q": "How does the guide describe the overall arc from this chapter's opening to its "
              "close?",
         "opts": [
             "No coherent arc; the discourses are unrelated",
             "From what obstructs any mendicant's wisdom (the hindrances) to a specific, "
             "practical account of what a particular group often lacks",
             "A repeat of the same single topic throughout",
             "A contradiction between the opening and closing discourses"],
         "correct": 1,
         "expl": "A shift from universal obstruction to a specific, practical closing observation."},
        {"q": "Where is AN 5.60 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five more rare qualities", [
            "easy to admonish",
            "retains learning",
            "learns respectfully",
            "can teach &middot; knows Vinaya",
        ]),
        ("Ten, across two pages", [
            "AN 5.59: presentation",
            "AN 5.60: receptivity",
            "&mdash; two shared, anchoring both",
        ]),
        ("The chapter closes", [
            "<span class=\"pali\">Nīvaraṇavaggo paṭhamo</span>",
            "the first chapter, on hindrances",
        ]),
        ("Cross-references", [
            "AN 5.59 &middot; the companion discourse",
            "AN 5.10 &middot; the colophon, explained",
            "AN 5.61 &middot; next: Saññāvagga",
        ]),
    ],
    further=[
        '<a href="%s/an5.60/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.59.html">AN 5.59 &middot; Gone Forth When Old (1st)</a> &mdash; the '
        "companion discourse, on presentation and existing knowledge.",
        '<a href="an-5.51.html">AN 5.51 &middot; Obstacles</a> &mdash; this chapter&rsquo;s '
        "opening discourse, on the hindrances that give this vagga its name.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; where this same '
        "chapter-closing colophon structure was first explained in full.",
    ],
)


VAGGA_7 = "<em>Saññāvagga</em> &mdash; the seventh chapter of the Fives"


# --------------------------------------------------------------------------- #
# AN 5.61 — Paṭhamasaññāsutta
# --------------------------------------------------------------------------- #
page(
    61, "Paṭhamasaññā", "Perceptions (1st)",
    vagga=VAGGA_7,
    meta_title="AN 5.61 — Perceptions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first Saññāsutta, "
        "opening a chapter of ten discourses built almost entirely in matched pairs — five "
        "perceptions with freedom from death as their goal: ugliness, death, drawbacks, food's "
        "repulsiveness, and dissatisfaction with the world. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five perceptions and their shared culmination, with "
                 "no elaboration"),
        ("Length", "~20 seconds to read"),
        ("Northern parallel", "Perception-based meditations culminating in freedom from death "
                              "recur widely across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, opening a chapter "
                       "built almost entirely from matched pairs of discourses"),
    ],
    why=(
        "This chapter is unusually uniform in structure: nearly every discourse in it arrives "
        "paired with a near-twin immediately following, the two sharing most of their content "
        "and differing in one deliberate respect. This opening pair, AN 5.61 and 5.62, both name "
        "five <em>saññā</em>, perceptions, that culminate in <em>amata</em>, freedom from death "
        "&mdash; but the two lists overlap in only three of their five items, a variation worth "
        "watching for across the whole chapter."),
    guide=[
        ("The teaching in one sentence", [
            "Five perceptions &mdash; ugliness, death, drawbacks, the repulsiveness of food, and "
            "dissatisfaction with the whole world &mdash; when developed and cultivated, are "
            "very fruitful and have freedom from death as their goal and culmination."]),
        ("A chapter of matched pairs", [
            "AN 5.63 and 5.64 will name identical growth for a male and female disciple in turn; "
            "AN 5.65 and 5.66 will name near-identical qualities for discussion and for shared "
            "life; AN 5.67 and 5.68 will give the same basis-of-psychic-power list first as "
            "general teaching, then as the Buddha's own pre-awakening practice; AN 5.69 and 5.70 "
            "will give an identical five-item list twice, differing only in what each says it "
            "leads to. This opening pair sets the pattern the rest of the chapter follows."]),
        ("Three items shared, two swapped", [
            "This discourse and AN 5.62 share <em>maraṇasaññā</em>, death, "
            "<em>āhāre paṭikūlasaññā</em>, food's repulsiveness, and "
            "<em>sabbaloke anabhiratasaññā</em>, dissatisfaction with the whole world. Where "
            "this discourse names <em>asubhasaññā</em>, ugliness, and <em>ādīnavasaññā</em>, "
            "drawbacks, AN 5.62 will instead name impermanence and not-self. The chapter is not "
            "simply repeating one list twice; it is showing two different five-item selections "
            "built from a larger, shared pool of contemplative objects."]),
        ("Amatogadhā, freedom from death as a destination", [
            "<em>Amatogadhā amatapariyosānā</em>, having freedom from death as their basis and "
            "culmination, is a striking pair of terms &mdash; <em>ogadha</em>, plunged into or "
            "grounded in, applied to something usually treated as an attainment rather than a "
            "location. The five perceptions are pictured here almost as a path that terminates "
            "in, and is already resting on, the deathless."]),
        ("A perception list already partly familiar", [
            "Several of these individual perceptions will return, worked together as a single "
            "practice rather than five separate objects, at "
            "<a href=\"an-5.69.html\">AN 5.69</a> and <a href=\"an-5.70.html\">AN 5.70</a> later "
            "in this chapter. Watching how the same handful of contemplative objects gets "
            "recombined into different five-item sets across this chapter is one of its main "
            "interests."]),
    ],
    terms=[
        ("saññā",
         "&ldquo;perception&rdquo; &mdash; the term giving this chapter its name, here naming a "
         "cultivated contemplative object rather than ordinary sense-perception."),
        ("asubhasaññā",
         "&ldquo;perception of ugliness&rdquo; &mdash; the first item, contemplation of the "
         "body's unattractive aspects, already met in this series at AN 4.163."),
        ("ādīnavasaññā",
         "&ldquo;perception of drawbacks&rdquo; &mdash; the third item, seeing the inherent cost "
         "or danger in conditioned existence."),
        ("amatogadhā",
         "&ldquo;grounded in the deathless&rdquo; &mdash; a striking compound treating freedom "
         "from death as a basis to rest on, not only a distant goal."),
        ("sabbaloke anabhiratasaññā",
         "&ldquo;perception of dissatisfaction with the whole world&rdquo; &mdash; the fifth "
         "item, shared with AN 5.62's differently composed list."),
    ],
    text_intro=(
        "The discourse in full: the five perceptions, named once. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.61:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five perceptions does this discourse name?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Ugliness, death, drawbacks, the repulsiveness of food, and dissatisfaction with the "
             "whole world",
             "Impermanence, not-self, death, food's repulsiveness, and world-dissatisfaction",
             "The five hindrances"],
         "correct": 1,
         "expl": "AN 5.62's list differs by two items, sharing the other three."},
        {"q": "What structural pattern does the guide say defines this whole chapter?",
         "opts": [
             "Every discourse stands entirely alone with no relation to any other",
             "Nearly every discourse arrives paired with a near-twin, sharing most content but "
             "differing in one deliberate respect",
             "All ten discourses are word-for-word identical",
             "The chapter has no internal structure at all"],
         "correct": 1,
         "expl": "A pattern this opening pair, AN 5.61 and 5.62, establishes immediately."},
        {"q": "How many of the five items does this discourse share with AN 5.62's list?",
         "opts": [
             "All five", "Three — death, food's repulsiveness, and world-dissatisfaction",
             "None", "Only one"],
         "correct": 1,
         "expl": "Two items differ: ugliness and drawbacks here, versus impermanence and not-self at AN 5.62."},
        {"q": "What does 'amatogadhā', grounded in the deathless, suggest about how freedom from "
              "death is pictured?",
         "opts": [
             "As an entirely future, unreachable goal",
             "As something the five perceptions are already resting on, a basis as much as a "
             "destination",
             "As irrelevant to the five perceptions",
             "As identical to physical immortality"],
         "correct": 1,
         "expl": "Ogadha, plunged into or grounded in, applied unusually to an attainment."},
        {"q": "Where do several of these individual perceptions reappear, recombined into a "
              "different five-item set?",
         "opts": [
             "Nowhere else in this chapter",
             "AN 5.69 and AN 5.70, later in this chapter",
             "Only in AN 4.163",
             "Only in AN 5.23"],
         "correct": 1,
         "expl": "The chapter reuses a shared pool of contemplative objects across different lists."},
        {"q": "What kind of term is 'saññā' in this discourse's usage?",
         "opts": [
             "Ordinary, passive sense-perception",
             "A cultivated contemplative object, developed deliberately",
             "A synonym for wisdom",
             "A synonym for faith"],
         "correct": 1,
         "expl": "Deliberately developed and cultivated, not simply what happens to be perceived."},
        {"q": "What does this discourse claim about the five perceptions when developed and "
              "cultivated?",
         "opts": [
             "That they are dangerous and should be avoided",
             "That they are very fruitful and beneficial, with freedom from death as their goal "
             "and culmination",
             "That they lead only to worldly benefit",
             "That they have no particular result"],
         "correct": 1,
         "expl": "The discourse's single claim, stated once with no elaboration."},
        {"q": "Does this discourse offer any simile or narrative illustration?",
         "opts": [
             "Yes, an extended parable",
             "No — a bare list with no illustration",
             "Yes, the river simile from AN 5.51",
             "Yes, a dialogue with a named questioner"],
         "correct": 1,
         "expl": "Consistent with this chapter's generally terse, list-based form."},
        {"q": "What does AN 5.63, the next discourse, turn to?",
         "opts": [
             "A repeat of this same perception list",
             "Growth in faith, ethics, learning, generosity, and wisdom, for a male noble "
             "disciple",
             "A return to the five hindrances",
             "The chapter's final discourse"],
         "correct": 1,
         "expl": "The familiar saddhā/sīla/suta/cāga/paññā list, met multiple times already in this nipāta."},
        {"q": "Where is AN 5.61 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five perceptions", [
            "ugliness &middot; death",
            "drawbacks",
            "food's repulsiveness",
            "world-dissatisfaction",
        ]),
        ("Shared with AN 5.62", [
            "death, food, world &mdash;",
            "three in common,",
            "two swapped",
        ]),
        ("A goal, and a ground", [
            "<span class=\"pali\">amatogadhā</span>",
            "&mdash; grounded in",
            "the deathless",
        ]),
        ("Cross-references", [
            "AN 4.163 &middot; ugliness, first met",
            "AN 5.62 &middot; next: the paired variant",
            "AN 5.69&ndash;70 &middot; the same items, recombined",
        ]),
    ],
    further=[
        '<a href="%s/an5.61/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.62.html">AN 5.62 &middot; Perceptions (2nd)</a> &mdash; next, this '
        "discourse's paired variant, swapping two of the five items.",
        '<a href="an-5.69.html">AN 5.69 &middot; Disillusionment</a> &mdash; later in this '
        "chapter, several of these same perceptions recombined into a single practice.",
        '<a href="an-4.163.html">AN 4.163 &middot; Ugly</a> &mdash; where the perception of '
        "ugliness first appeared in this series.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.62 — Dutiyasaññāsutta
# --------------------------------------------------------------------------- #
page(
    62, "Dutiyasaññā", "Perceptions (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 5.62 — Perceptions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Saññāsutta — "
        "AN 5.61's list restated with two items swapped: impermanence and not-self replacing "
        "ugliness and drawbacks. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.61's formula restated with two of five items changed"),
        ("Length", "~20 seconds to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.61"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the chapter's first "
                       "confirmed instance of its paired structure"),
    ],
    why=(
        "As promised at AN 5.61, this discourse swaps two of the five perceptions: "
        "<em>aniccasaññā</em>, impermanence, and <em>anattasaññā</em>, not-self, replace "
        "ugliness and drawbacks, while death, food's repulsiveness, and world-dissatisfaction "
        "carry over unchanged. The shared claim &mdash; freedom from death as goal and "
        "culmination &mdash; is identical in both discourses, word for word."),
    guide=[
        ("The teaching in one sentence", [
            "Five perceptions &mdash; impermanence, not-self, death, the repulsiveness of food, "
            "and dissatisfaction with the whole world &mdash; when developed and cultivated, are "
            "very fruitful and have freedom from death as their goal and culmination."]),
        ("Two of the canon's central themes, entering this list", [
            "Impermanence and not-self are, elsewhere in the canon, treated as two of the three "
            "marks of existence, alongside suffering. Their appearance here, standing alongside "
            "more concrete contemplative objects like food's repulsiveness, shows this list "
            "mixing doctrinal cornerstones with vivid, embodied practices rather than keeping "
            "the two registers separate."]),
        ("What stays fixed across both discourses", [
            "Death, food's repulsiveness, and world-dissatisfaction anchor both versions of the "
            "list. This constancy is worth noting precisely because it is not commented on in "
            "either discourse: the two lists are never explicitly compared to each other in the "
            "source text itself, and it is only by reading them side by side that the shared "
            "core and the swapped pair become visible."]),
        ("The identical closing claim", [
            "Every word of the discourse's final sentence &mdash; very fruitful and beneficial, "
            "freedom from death as goal and culmination &mdash; matches AN 5.61 exactly. The "
            "chapter is making the same claim about two different, overlapping sets of "
            "perceptions, rather than claiming one version is superior to the other."]),
        ("What follows", [
            "AN 5.63, next, leaves perceptions behind entirely and returns to this nipāta's "
            "most familiar five-item list &mdash; faith, ethics, learning, generosity, wisdom "
            "&mdash; now framed as growth, and given, unusually, in two versions distinguished "
            "by the disciple's gender rather than by any change in content."]),
    ],
    terms=[
        ("aniccasaññā",
         "&ldquo;perception of impermanence&rdquo; &mdash; the first of two swapped items, one "
         "of the three marks of existence elsewhere in the canon."),
        ("anattasaññā",
         "&ldquo;perception of not-self&rdquo; &mdash; the second swapped item, the third mark "
         "of existence alongside impermanence and suffering."),
        ("maraṇasaññā",
         "&ldquo;perception of death&rdquo; &mdash; one of three items shared unchanged with AN "
         "5.61's list."),
        ("āhāre paṭikūlasaññā",
         "&ldquo;perception of food's repulsiveness&rdquo; &mdash; the second shared item, a "
         "vivid, embodied practice alongside the more doctrinal impermanence and not-self."),
        ("amatapariyosānā",
         "&ldquo;culminating in the deathless&rdquo; &mdash; the closing phrase, worded "
         "identically to AN 5.61's."),
    ],
    text_intro=(
        "The discourse in full: the five perceptions, named once, with two items swapped from "
        "AN 5.61. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.62:1.1-1.4"),
    ],
    quiz=[
        {"q": "Which two items does this discourse swap in from AN 5.61's list?",
         "opts": [
             "Faith and wisdom",
             "Impermanence and not-self, replacing ugliness and drawbacks",
             "Ethics and generosity",
             "Nothing changes between the two discourses"],
         "correct": 1,
         "expl": "Two of the canon's central doctrinal themes, entering this contemplative list."},
        {"q": "Which three items stay unchanged between AN 5.61 and this discourse?",
         "opts": [
             "Ugliness, drawbacks, and death",
             "Death, food's repulsiveness, and dissatisfaction with the whole world",
             "Impermanence, not-self, and death",
             "None; all five items differ"],
         "correct": 1,
         "expl": "The shared core anchoring both versions of the list."},
        {"q": "Does the source text itself explicitly compare AN 5.61 and 5.62's lists?",
         "opts": [
             "Yes, at length",
             "No — the comparison only becomes visible by reading the two side by side",
             "Yes, but only briefly",
             "The two discourses never appear near each other in the source"],
         "correct": 1,
         "expl": "Neither discourse comments on the other; the pairing is structural, not stated."},
        {"q": "How does the discourse's closing claim compare to AN 5.61's?",
         "opts": [
             "Completely different",
             "Worded identically — very fruitful and beneficial, freedom from death as goal and "
             "culmination",
             "Weaker than AN 5.61's claim",
             "Stronger than AN 5.61's claim"],
         "correct": 1,
         "expl": "The same claim applied to two overlapping but distinct sets of perceptions."},
        {"q": "What are impermanence and not-self elsewhere called, alongside suffering?",
         "opts": [
             "The five hindrances",
             "Two of the three marks of existence",
             "The four noble truths",
             "The five powers"],
         "correct": 1,
         "expl": "A standard doctrinal grouping this discourse's list draws two items from."},
        {"q": "What does mixing impermanence and not-self with food's repulsiveness in one list "
              "suggest, according to the guide?",
         "opts": [
             "That the list is poorly organized",
             "That the list mixes doctrinal cornerstones with vivid, embodied practices rather "
             "than keeping the two registers separate",
             "That food's repulsiveness is not a real perception",
             "That the two items are contradictory"],
         "correct": 1,
         "expl": "A deliberate range from the abstract to the concrete within a single five-item set."},
        {"q": "Does this discourse claim its version of the list is superior to AN 5.61's?",
         "opts": [
             "Yes, explicitly",
             "No — both discourses make the identical claim about their respective lists",
             "Yes, but only implicitly",
             "The discourse takes no position on either list's value"],
         "correct": 1,
         "expl": "Neither version is ranked above the other."},
        {"q": "What does AN 5.63, the next discourse, turn to?",
         "opts": [
             "A third perception list",
             "The familiar faith/ethics/learning/generosity/wisdom list, framed as growth, given "
             "in gender-distinguished versions",
             "A return to the five hindrances",
             "The chapter's final discourse"],
         "correct": 1,
         "expl": "A shift away from perceptions to this nipāta's most recurring five-item list."},
        {"q": "Is any simile or narrative used in this discourse?",
         "opts": [
             "Yes, an extended parable",
             "No — a bare list with no illustration, matching AN 5.61's form",
             "Yes, a dialogue with a named questioner",
             "Yes, the tree simile"],
         "correct": 1,
         "expl": "Consistent with the chapter's terse, list-based style."},
        {"q": "Where is AN 5.62 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Swapped in", [
            "impermanence",
            "not-self",
        ]),
        ("Held constant", [
            "death &middot; food's",
            "repulsiveness &middot; world-",
            "dissatisfaction",
        ]),
        ("Same closing claim", [
            "very fruitful,",
            "grounded in the deathless",
            "&mdash; word for word",
        ]),
        ("Cross-references", [
            "AN 5.61 &middot; the paired original",
            "AN 5.63 &middot; next: growth, for a man",
            "AN 5.69&ndash;70 &middot; the items, recombined",
        ]),
    ],
    further=[
        '<a href="%s/an5.62/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.61.html">AN 5.61 &middot; Perceptions (1st)</a> &mdash; the previous '
        "discourse, this one's paired original.",
        '<a href="an-5.63.html">AN 5.63 &middot; Growth (1st)</a> &mdash; next, a shift to this '
        "nipāta's most recurring five-item list.",
        '<a href="an-5.69.html">AN 5.69 &middot; Disillusionment</a> &mdash; later in this '
        "chapter, several of these same perceptions recombined into a single practice.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.63 — Paṭhamavaḍḍhisutta
# --------------------------------------------------------------------------- #
page(
    63, "Paṭhamavaḍḍhi", "Growth (1st)",
    vagga=VAGGA_7,
    meta_title="AN 5.63 — Growth (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first Vaḍḍhisutta — a "
        "male noble disciple growing nobly in faith, ethics, learning, generosity, and wisdom, "
        "taking on what is essential in this life. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five kinds of growth, closing with a short verse"),
        ("Length", "~30 seconds to read"),
        ("Northern parallel", "Faith, ethics, learning, generosity, and wisdom as a fixed lay "
                              "growth set are widely attested across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, reusing a list this "
                       "nipāta has already given three times"),
    ],
    why=(
        "This is the fourth appearance, in this nipāta alone, of the identical five-item set "
        "&mdash; faith, ethics, learning, generosity, wisdom &mdash; already met at "
        "<a href=\"an-5.40.html\">AN 5.40</a>'s family growth, "
        "<a href=\"an-5.46.html\">AN 5.46</a>'s bare accomplishments, and "
        "<a href=\"an-5.47.html\">AN 5.47</a>'s detailed wealth. Here the frame shifts once "
        "more: growth, <em>vaḍḍhi</em>, applied specifically to a male noble disciple, "
        "<em>ariyasāvako</em>, and paired deliberately with AN 5.64's identical teaching for a "
        "female disciple."),
    guide=[
        ("The teaching in one sentence", [
            "A male noble disciple who grows in faith, ethics, learning, generosity, and wisdom "
            "grows nobly, taking on what is essential and excellent in this life."]),
        ("A fourth frame for one list", [
            "Growth, accomplishment, wealth, and a family's flourishing are now four different "
            "images this nipāta has applied to the identical five terms, without changing any of "
            "them. This discourse adds nothing new to the content of faith, ethics, learning, "
            "generosity, or wisdom; its contribution is entirely in the specific, gendered "
            "framing that follows immediately at AN 5.64."]),
        ("Sāradāyī varādāyī, taking hold of what is essential", [
            "The discourse's closing phrase, <em>sārādāyī ca hoti varādāyī ca kāyassa</em>, "
            "taking on what is essential and excellent for the body, uses an image of active "
            "grasping rather than passive reception. Growth, on this account, is not simply "
            "something that happens to a disciple; it is something they take hold of, "
            "specifically the essential and excellent part of what this life offers."]),
        ("Deliberately paired with a discourse for women", [
            "Unlike most repetitions in this nipāta, this pairing is not simply structural "
            "convenience; AN 5.64 restates the identical five-item teaching using feminine "
            "grammatical forms throughout &mdash; <em>ariyasāvikā</em>, a female noble disciple, "
            "not merely the masculine form left to stand for both. The collection did not leave "
            "this teaching ungendered or assume the masculine form would be read as covering "
            "everyone; it produced a second, explicitly feminine discourse instead."]),
        ("What follows", [
            "AN 5.65 and 5.66, next, leave growth behind and turn to a different five-item list "
            "&mdash; the AN 5.17&ndash;20 set of ethics, immersion, wisdom, freedom, and the "
            "knowledge and vision of freedom &mdash; reframed as what makes a mendicant fit for "
            "discussion and for sharing life with companions."]),
    ],
    terms=[
        ("vaḍḍhi",
         "&ldquo;growth&rdquo; &mdash; this discourse's frame for the five familiar items, "
         "distinct from AN 5.40's, 5.46's, and 5.47's earlier framings."),
        ("ariyasāvako",
         "&ldquo;male noble disciple&rdquo; &mdash; the masculine grammatical form this "
         "discourse uses throughout, paired deliberately with AN 5.64's feminine form."),
        ("sārādāyī",
         "&ldquo;taking hold of what is essential&rdquo; &mdash; an image of active grasping, "
         "not passive reception of growth."),
        ("varādāyī",
         "&ldquo;taking hold of what is excellent&rdquo; &mdash; paired with sārādāyī, "
         "completing the image of active appropriation."),
        ("kāyassa",
         "&ldquo;for the body, for this life&rdquo; &mdash; the scope of what is essential and "
         "excellent, taken hold of in this present existence."),
    ],
    text_intro=(
        "The discourse in full: the five kinds of growth for a male noble disciple, closing with "
        "a verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.63:1.1-1.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an5.63:2.1-2.4"),
    ],
    quiz=[
        {"q": "What five kinds of growth does this discourse name for a male noble disciple?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Faith, ethics, learning, generosity, and wisdom",
             "The five hindrances",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "The same five items already met three times earlier in this nipāta."},
        {"q": "How many times has this identical five-item list now appeared in this nipāta, "
              "counting this discourse?",
         "opts": ["Once", "Twice", "Four times", "Ten times"],
         "correct": 2,
         "expl": "AN 5.40, 5.46, 5.47, and now AN 5.63."},
        {"q": "What does 'sārādāyī varādāyī' suggest about how growth is pictured?",
         "opts": [
             "As something entirely passive, simply happening to the disciple",
             "As active grasping — taking hold of what is essential and excellent, not merely "
             "receiving it",
             "As irrelevant to the disciple's own effort",
             "As something only achieved after death"],
         "correct": 1,
         "expl": "An image of appropriation, not passive reception."},
        {"q": "What makes this discourse's pairing with AN 5.64 different from most repetitions "
              "in this nipāta?",
         "opts": [
             "It isn't different; the pairing is purely structural convenience",
             "AN 5.64 explicitly restates the teaching in feminine grammatical forms, rather than "
             "leaving the masculine form to stand for everyone",
             "AN 5.64 contradicts this discourse entirely",
             "AN 5.64 uses a completely different five-item list"],
         "correct": 1,
         "expl": "A deliberate second, explicitly gendered discourse, not an assumed universal masculine."},
        {"q": "Does this discourse add any new content to the definitions of faith, ethics, "
              "learning, generosity, or wisdom?",
         "opts": [
             "Yes, extensive new definitions",
             "No — its contribution is entirely in the frame (growth) and the specific gendered "
             "pairing that follows",
             "Only wisdom is redefined",
             "Only faith is redefined"],
         "correct": 1,
         "expl": "The content stays fixed across all four framings this nipāta has now given it."},
        {"q": "What does AN 5.65, the next discourse, turn to?",
         "opts": [
             "A repeat of this same growth teaching",
             "A different five-item list — ethics, immersion, wisdom, freedom, and the knowledge "
             "and vision of freedom — reframed as fitness for discussion",
             "A return to the five hindrances",
             "The chapter's final discourse"],
         "correct": 1,
         "expl": "The AN 5.17–20 set, given a new practical frame."},
        {"q": "What term does this discourse use for the disciple?",
         "opts": [
             "Sekha, trainee",
             "Ariyasāvako, male noble disciple",
             "Sappurisa, true person",
             "Bhikkhu, mendicant, without qualification"],
         "correct": 1,
         "expl": "The specific, gendered term this discourse pairs with AN 5.64's feminine equivalent."},
        {"q": "Where has faith, ethics, learning, generosity, and wisdom appeared earlier as "
              "'wealth' specifically?",
         "opts": [
             "Nowhere before this page",
             "AN 5.47",
             "AN 5.1",
             "AN 4.163"],
         "correct": 1,
         "expl": "One of three earlier framings this discourse's 'growth' adds a fourth to."},
        {"q": "Does this discourse include a closing verse?",
         "opts": [
             "No, it ends immediately after the prose",
             "Yes, a short verse restating the same five items and their outcome",
             "Yes, an extended set of ten verses",
             "The discourse is entirely in verse, with no prose"],
         "correct": 1,
         "expl": "A brief verse closes the discourse, matching AN 5.64's structure exactly."},
        {"q": "Where is AN 5.63 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five kinds of growth", [
            "faith &middot; ethics",
            "learning &middot; generosity",
            "wisdom",
        ]),
        ("A fourth frame", [
            "AN 5.40: family",
            "AN 5.46: accomplishment",
            "AN 5.47: wealth",
            "AN 5.63: growth",
        ]),
        ("Active grasping", [
            "<span class=\"pali\">sārādāyī varādāyī</span>",
            "&mdash; taking hold,",
            "not merely receiving",
        ]),
        ("Cross-references", [
            "AN 5.40, 5.46&ndash;47 &middot; the same list, earlier",
            "AN 5.64 &middot; next: for a female disciple",
            "AN 5.65 &middot; then: a different five-item set",
        ]),
    ],
    further=[
        '<a href="%s/an5.63/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.47.html">AN 5.47 &middot; Wealth</a> &mdash; the same five items, framed '
        "there as an inalienable kind of wealth.",
        '<a href="an-5.64.html">AN 5.64 &middot; Growth (2nd)</a> &mdash; next, this '
        "discourse's deliberate feminine counterpart.",
        '<a href="an-5.40.html">AN 5.40 &middot; Great Sal Trees</a> &mdash; where this same '
        "five-item list first appeared in this nipāta, applied to a family's growth.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.64 — Dutiyavaḍḍhisutta
# --------------------------------------------------------------------------- #
page(
    64, "Dutiyavaḍḍhi", "Growth (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 5.64 — Growth (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Vaḍḍhisutta — "
        "AN 5.63's teaching restated for a female noble disciple, in fully feminine "
        "grammatical form rather than left to an assumed masculine default. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.63's formula restated with feminine grammatical forms throughout, "
                 "closing with a matching verse"),
        ("Length", "~30 seconds to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.63"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, and worth noticing "
                       "for what its existence as a separate discourse implies"),
    ],
    why=(
        "This discourse could, in principle, not exist: nothing about AN 5.63's content "
        "requires restating for it to apply equally to a woman. That the collection produced it "
        "anyway &mdash; a full, separate discourse in feminine grammatical form, "
        "<em>ariyasāvikā</em> rather than a masculine default silently covering both &mdash; is "
        "itself worth reading as a deliberate choice, not an accident of transmission."),
    guide=[
        ("The teaching in one sentence", [
            "A female noble disciple who grows in faith, ethics, learning, generosity, and "
            "wisdom grows nobly, taking on what is essential and excellent in this life."]),
        ("Identical content, complete grammatical restatement", [
            "Every substantive claim in this discourse matches AN 5.63 exactly &mdash; the same "
            "five items, the same outcome, the same closing image of taking hold of what is "
            "essential. What changes is thorough and consistent: "
            "<em>ariyasāvikā</em> for <em>ariyasāvako</em>, <em>sārādāyinī varādāyinī</em> for "
            "<em>sārādāyī varādāyī</em>, feminine forms replacing masculine ones throughout both "
            "the prose and the closing verse."]),
        ("What this pairing implies about the collection's assumptions", [
            "A tradition confident that a masculine grammatical form automatically covered women "
            "as well would have had no reason to produce this discourse at all. Its existence "
            "suggests the opposite assumption was at least sometimes operative: that a teaching "
            "aimed explicitly and separately at women mattered enough to be composed and "
            "preserved as its own discourse, not folded silently into the male version."]),
        ("Upāsikā, named directly in the verse", [
            "The closing verse names its subject <em>sīlavatī upāsikā</em>, a virtuous "
            "laywoman, rather than only repeating <em>ariyasāvikā</em>. This gives the "
            "discourse's subject a concrete social identity &mdash; not an abstract disciple in "
            "either gender, but specifically a laywoman practicing in the world, matching AN "
            "5.63's parallel use of a general term for its own subject."]),
        ("Read against AN 5.55, earlier in this chapter", [
            "This discourse and AN 5.55's account of a mother, a son, and a stark warning about "
            "women sit in the same chapter, only nine discourses apart. This reading guide does "
            "not attempt to resolve the tension between them into a single, tidy statement about "
            "how this collection regards women; both discourses are genuinely present in the "
            "text, addressed to different concerns, and a reader doing this material justice "
            "should hold both rather than letting one silently stand for the whole."]),
    ],
    terms=[
        ("ariyasāvikā",
         "&ldquo;female noble disciple&rdquo; &mdash; the feminine grammatical form used "
         "throughout this discourse, paired deliberately with AN 5.63's masculine "
         "ariyasāvako."),
        ("sārādāyinī varādāyinī",
         "&ldquo;taking hold of what is essential and excellent&rdquo; &mdash; the feminine "
         "form of AN 5.63's closing image, otherwise unchanged."),
        ("sīlavatī upāsikā",
         "&ldquo;virtuous laywoman&rdquo; &mdash; the closing verse's concrete social identity "
         "for its subject, paralleling AN 5.63's own general term."),
        ("vaḍḍhi",
         "&ldquo;growth&rdquo; &mdash; the same frame as AN 5.63, unchanged between the two "
         "discourses."),
        ("saddhā sīla suta cāga paññā",
         "&ldquo;faith, ethics, learning, generosity, wisdom&rdquo; &mdash; the identical five "
         "items, now the fifth appearance of this list in this nipāta."),
    ],
    text_intro=(
        "The discourse in full: the five kinds of growth for a female noble disciple, closing "
        "with a matching verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.64:1.1-1.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an5.64:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 5.63's?",
         "opts": [
             "Completely different subject matter",
             "Identical substantive claims — the same five items, same outcome, same closing "
             "image — restated entirely in feminine grammatical form",
             "A shorter, abbreviated version",
             "A contradiction of AN 5.63"],
         "correct": 1,
         "expl": "A thorough, consistent grammatical restatement, not a content change."},
        {"q": "What does the guide say the existence of this discourse, as a separate text, "
              "implies?",
         "opts": [
             "Nothing significant; it is purely incidental",
             "That the collection did not assume a masculine grammatical form automatically "
             "covered women, and considered a teaching aimed explicitly at women worth "
             "composing separately",
             "That women were considered less capable than men",
             "That this discourse was added by mistake"],
         "correct": 1,
         "expl": "A deliberate choice worth reading as such, not an accident of transmission."},
        {"q": "What term does the closing verse use for this discourse's subject?",
         "opts": [
             "Only 'ariyasāvikā', repeated",
             "'Sīlavatī upāsikā', a virtuous laywoman — giving the subject a concrete social "
             "identity",
             "'Bhikkhunī', a fully ordained nun specifically",
             "No specific term is used"],
         "correct": 1,
         "expl": "Matching AN 5.63's parallel use of a general term for its own subject."},
        {"q": "How does the guide handle the tension between this discourse and AN 5.55's earlier "
              "material in the same chapter?",
         "opts": [
             "It ignores AN 5.55 entirely when discussing this discourse",
             "It does not resolve the tension into one tidy statement, holding both discourses as "
             "genuinely present, addressed to different concerns",
             "It claims AN 5.55 is inauthentic and should be disregarded",
             "It claims this discourse cancels out AN 5.55's content"],
         "correct": 1,
         "expl": "An honest acknowledgment that the collection contains material in real tension, without forcing false resolution."},
        {"q": "What five items does this discourse name for growth?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Faith, ethics, learning, generosity, and wisdom",
             "The five hindrances",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "Identical to AN 5.63's list, the same items met four times earlier in this nipāta."},
        {"q": "How many times has this five-item list now appeared in this nipāta, counting this "
              "discourse?",
         "opts": ["Once", "Three times", "Five times", "Ten times"],
         "correct": 2,
         "expl": "AN 5.40, 5.46, 5.47, 5.63, and now AN 5.64."},
        {"q": "Does this discourse offer a closing verse, like AN 5.63?",
         "opts": [
             "No, it ends immediately after the prose",
             "Yes, a matching verse in feminine grammatical form",
             "Yes, but with entirely different content",
             "The discourse has no prose, only verse"],
         "correct": 1,
         "expl": "A parallel structure to AN 5.63 throughout, including the closing verse."},
        {"q": "What word replaces 'ariyasāvako' throughout this discourse?",
         "opts": [
             "Upāsaka, layman",
             "Ariyasāvikā, female noble disciple",
             "Bhikkhu, monk",
             "No replacement occurs"],
         "correct": 1,
         "expl": "The consistent feminine grammatical substitution running through the whole discourse."},
        {"q": "What comes next in this chapter after this pair of growth discourses?",
         "opts": [
             "A repeat of the growth teaching a third time",
             "AN 5.65, turning to a different five-item list framed around fitness for discussion",
             "The chapter's final discourse",
             "A return to the five hindrances"],
         "correct": 1,
         "expl": "The chapter moves on to the AN 5.17–20 set, newly reframed."},
        {"q": "Where is AN 5.64 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Feminine throughout", [
            "<span class=\"pali\">ariyasāvikā</span>",
            "<span class=\"pali\">sārādāyinī varādāyinī</span>",
        ]),
        ("A deliberate choice", [
            "not a masculine default",
            "assumed to cover all &mdash;",
            "a separate discourse instead",
        ]),
        ("Held in tension", [
            "AN 5.55: a stark warning",
            "AN 5.64: full inclusion",
            "&mdash; both, genuinely present",
        ]),
        ("Cross-references", [
            "AN 5.63 &middot; the masculine counterpart",
            "AN 5.55 &middot; this chapter's hardest text",
            "AN 5.65 &middot; next: a different five-item set",
        ]),
    ],
    further=[
        '<a href="%s/an5.64/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.63.html">AN 5.63 &middot; Growth (1st)</a> &mdash; this discourse&rsquo;s '
        "masculine counterpart, identical apart from grammatical gender.",
        '<a href="an-5.55.html">AN 5.55 &middot; Mother and Son</a> &mdash; earlier in this '
        "chapter, material this discourse sits in real tension with.",
        '<a href="an-5.65.html">AN 5.65 &middot; Discussion</a> &mdash; next, a different '
        "five-item list reframed as fitness for discussion with companions.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.65 — Sākacchasutta
# --------------------------------------------------------------------------- #
page(
    65, "Sākaccha", "Discussion",
    vagga=VAGGA_7,
    meta_title="AN 5.65 — Discussion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sākacchasutta — a "
        "mendicant fit to discuss the Dhamma with companions is personally accomplished in, and "
        "able to answer questions about, ethics, immersion, wisdom, freedom, and the knowledge "
        "and vision of freedom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single sentence naming five paired qualities — personal accomplishment plus "
                 "ability to answer questions — for each of five topics"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Personal accomplishment paired with the ability to answer "
                              "questions on the same subject recurs as a standard for teaching "
                              "fitness across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; reuses a five-item list "
                       "already central to this nipāta, now applied to a specific social "
                       "function"),
    ],
    why=(
        "This discourse returns to the five-item set that structured "
        "<a href=\"an-5.17.html\">AN 5.17&ndash;20</a> &mdash; ethics, immersion, wisdom, "
        "freedom, and the knowledge and vision of freedom &mdash; and gives it a new, practical "
        "test: fitness to hold a discussion with one's spiritual companions. Each of the five "
        "items now comes doubled, requiring both personal accomplishment and the ability to "
        "field questions others raise about it."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant fit to hold a discussion with spiritual companions is personally "
            "accomplished in ethics, immersion, wisdom, freedom, and the knowledge and vision of "
            "freedom, and can answer questions that come up when each is discussed."]),
        ("A double requirement, not a single one", [
            "Each of the five items in this discourse is really two requirements folded "
            "together: <em>attanā ca&hellip;sampanno hoti</em>, personally accomplished, and "
            "<em>kathāya ca āgataṁ pañhaṁ byākattā hoti</em>, able to answer questions that arise "
            "in discussion. A mendicant could conceivably have one without the other &mdash; "
            "genuinely accomplished but unable to articulate it under questioning, or "
            "articulate without the underlying accomplishment &mdash; and this discourse "
            "requires both together, for all five items, before fitness for discussion is "
            "granted."]),
        ("The same five items, at a different depth than AN 5.17&ndash;20", [
            "AN 5.17 through 5.20 used this identical list to sort mendicants by whether they "
            "practiced for their own welfare, others', both, or neither. This discourse assumes "
            "accomplishment in all five as a baseline and adds a further, more specific "
            "capacity on top: the ability to withstand questioning about that accomplishment "
            "from one's own community. It is a narrower, more demanding standard than simply "
            "having encouraged others, as AN 5.20's fourth case required."]),
        ("What &lsquo;fit to discuss&rsquo; implies about the community it serves", [
            "This discourse assumes spiritual companions who will actually ask hard questions "
            "&mdash; a community where accomplishment is expected to be tested, not merely "
            "trusted on report. The standard it sets is not for private conviction alone, but "
            "for conviction robust enough to survive genuine scrutiny from peers."]),
        ("A companion discourse follows immediately", [
            "AN 5.66, next, restates this almost word for word, changing only the specific "
            "outcome from fitness for discussion to fitness to <em>share one's life</em> with "
            "companions &mdash; a small but real distinction between talking well about the "
            "path and actually living alongside others on it."]),
    ],
    terms=[
        ("alaṁsākaccho",
         "&ldquo;fit for discussion&rdquo; &mdash; this discourse&rsquo;s title and standard, "
         "naming a specific social capacity rather than private attainment alone."),
        ("sampanno",
         "&ldquo;accomplished&rdquo; &mdash; the first half of each paired requirement, personal "
         "attainment in each of the five items."),
        ("kathāya āgataṁ pañhaṁ byākattā",
         "&ldquo;able to answer questions that come up in discussion&rdquo; &mdash; the second "
         "half, the capacity to withstand questioning from companions."),
        ("vimuttiñāṇadassana",
         "&ldquo;the knowledge and vision of freedom&rdquo; &mdash; the fifth item, completing "
         "the AN 5.17&ndash;20 set reused here."),
        ("sabrahmacārī",
         "&ldquo;spiritual companion&rdquo; &mdash; the community this discourse assumes will "
         "actually test a mendicant's accomplishment through questioning."),
    ],
    text_intro=(
        "The discourse in full: the five paired qualities required for fitness to discuss the "
        "Dhamma with companions. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.65:1.1-1.2"),
        ("p", "&sect;2", "an5.65:1.3"),
        ("p", "&sect;3", "an5.65:1.4"),
        ("p", "&sect;4", "an5.65:1.5"),
        ("p", "&sect;5", "an5.65:1.6"),
        ("p", "&sect;6", "an5.65:1.7"),
        ("p", "&sect;7", "an5.65:1.8"),
    ],
    quiz=[
        {"q": "What five topics does this discourse require both accomplishment in and the "
              "ability to discuss?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Ethics, immersion, wisdom, freedom, and the knowledge and vision of freedom",
             "The five hindrances",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "The identical five-item list already central to AN 5.17–20."},
        {"q": "What double requirement does each of the five items carry in this discourse?",
         "opts": [
             "Only personal accomplishment, nothing more",
             "Both personal accomplishment and the ability to answer questions that come up in "
             "discussion",
             "Only the ability to answer questions, regardless of personal accomplishment",
             "Neither is required, only reputation"],
         "correct": 1,
         "expl": "A mendicant could conceivably have one without the other; this discourse requires both."},
        {"q": "How does this discourse's use of the AN 5.17–20 list differ from that earlier "
              "usage?",
         "opts": [
             "It is identical in every respect",
             "AN 5.17–20 sorted mendicants by welfare-orientation; this discourse assumes "
             "accomplishment and adds a further capacity — withstanding questioning",
             "This discourse rejects AN 5.17–20's framework entirely",
             "This discourse uses an entirely different five-item list"],
         "correct": 1,
         "expl": "A narrower, more demanding standard layered on top of the earlier framework."},
        {"q": "What does the guide say this discourse's standard implies about the community it "
              "assumes?",
         "opts": [
             "A community where accomplishment is simply trusted on report",
             "A community where accomplishment is expected to be tested through genuine "
             "questioning from peers",
             "A community with no interest in discussion at all",
             "A solitary practice with no community involved"],
         "correct": 1,
         "expl": "Conviction robust enough to survive scrutiny, not merely private conviction."},
        {"q": "What does AN 5.66, the next discourse, change from this one?",
         "opts": [
             "Nothing; it repeats this discourse verbatim",
             "The specific outcome — fitness to share one's life with companions, rather than "
             "fitness for discussion",
             "The five-item list itself",
             "It removes the personal-accomplishment requirement"],
         "correct": 1,
         "expl": "A small but real distinction between talking well and actually living alongside others."},
        {"q": "What is the fifth item in this discourse's list?",
         "opts": [
             "Wisdom", "The knowledge and vision of freedom (vimuttiñāṇadassana)",
             "Generosity", "Learning"],
         "correct": 1,
         "expl": "Completing the same set already used at AN 5.17–20."},
        {"q": "Where did this five-item list previously structure a four-discourse unit in this "
              "nipāta?",
         "opts": [
             "AN 5.41–44", "AN 5.17–20", "AN 5.61–64", "AN 5.1–4"],
         "correct": 1,
         "expl": "The self-welfare/others-welfare unit from earlier in the Fives."},
        {"q": "Does this discourse offer a simile or narrative illustration?",
         "opts": [
             "Yes, an extended parable",
             "No — a direct, structured statement with no illustration",
             "Yes, a dialogue with a named questioner",
             "Yes, the tree simile"],
         "correct": 1,
         "expl": "A structured list, consistent with much of this chapter's form."},
        {"q": "What is 'alaṁsākaccho' best translated as?",
         "opts": [
             "'Fit for discussion' — this discourse's own title and standard",
             "'Unfit for teaching'",
             "'Silent and withdrawn'",
             "'Argumentative'"],
         "correct": 0,
         "expl": "A positive standard of readiness, not a criticism."},
        {"q": "Where is AN 5.65 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five topics, doubled", [
            "ethics &middot; immersion",
            "wisdom &middot; freedom",
            "knowledge &amp; vision of it",
        ]),
        ("Two requirements each", [
            "accomplished, and",
            "able to answer",
            "questions raised",
        ]),
        ("A tested community", [
            "not trust on report &mdash;",
            "conviction that survives",
            "real questioning",
        ]),
        ("Cross-references", [
            "AN 5.17&ndash;20 &middot; the list, first used",
            "AN 5.66 &middot; next: sharing life",
            "AN 5.64 &middot; the previous discourse",
        ]),
    ],
    further=[
        '<a href="%s/an5.65/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; where this '
        "five-item list first structured a discourse unit in this nipāta.",
        '<a href="an-5.66.html">AN 5.66 &middot; Sharing Life</a> &mdash; next, this '
        "discourse's near-identical companion.",
        '<a href="an-5.64.html">AN 5.64 &middot; Growth (2nd)</a> &mdash; the previous discourse, '
        "on a different familiar five-item list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.66 — Sājīvasutta
# --------------------------------------------------------------------------- #
page(
    66, "Sājīva", "Sharing Life",
    vagga=VAGGA_7,
    meta_title="AN 5.66 — Sharing Life | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sājīvasutta — AN "
        "5.65's near-identical companion, the same five paired qualities now required for "
        "fitness to actually share one's life with spiritual companions. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.65's formula restated with one word changed in each of five paired "
                 "clauses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching sutra "
                              "number for this variant beyond the parallel already noted at AN "
                              "5.65"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; near-identical to its "
                       "predecessor, worth reading for its one genuine difference"),
    ],
    why=(
        "This discourse and AN 5.65 differ in exactly one respect, repeated five times: "
        "<em>kathāya ca āgataṁ pañhaṁ</em>, questions that <em>come up</em> in discussion, "
        "becomes <em>kathāya ca kataṁ pañhaṁ</em>, questions that are <em>posed</em>, and the "
        "outcome shifts from <em>alaṁsākaccho</em>, fit for discussion, to "
        "<em>alaṁsājīvo</em>, fit to share one's life. Small changes, worth reading precisely "
        "rather than treating as interchangeable."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant fit to share their life with spiritual companions is personally "
            "accomplished in ethics, immersion, wisdom, freedom, and the knowledge and vision of "
            "freedom, and can answer questions posed when each is discussed."]),
        ("Āgataṁ versus kataṁ, a small but real distinction", [
            "AN 5.65's questions <em>come up</em>, arising in the natural course of "
            "conversation; this discourse's questions are <em>posed</em>, more actively "
            "directed at the mendicant. It is a fine distinction, and this reading guide does "
            "not overstate it, but the two verbs are not accidental synonyms &mdash; one "
            "suggests organic conversation, the other suggests something closer to deliberate "
            "examination."]),
        ("From talking well to living alongside", [
            "The larger difference sits in the discourse's outcome, not its questions: "
            "<em>sājīva</em>, shared life, names something more sustained and total than "
            "<em>sākaccha</em>, discussion. A mendicant might handle a single conversation well "
            "without being someone their companions could actually live and practice alongside "
            "day after day. This discourse sets the higher bar of the two, using nearly "
            "identical language to do it."]),
        ("Why state this as a separate discourse rather than one combined teaching", [
            "As with several near-duplicate pairs already met in this nipāta, the likely answer "
            "is again transmission: a chanted tradition preserves two related but genuinely "
            "distinct claims &mdash; fitness for conversation, fitness for shared life &mdash; "
            "better as two complete, separately memorizable units than as one discourse with an "
            "appended variant."]),
        ("Closing this chapter's third pair", [
            "AN 5.65 and 5.66 complete the third of this chapter's matched pairs, after "
            "perceptions (61&ndash;62) and growth (63&ndash;64). AN 5.67 and 5.68, next, will "
            "give the chapter's fourth pair, moving from social fitness to the bases of psychic "
            "power &mdash; first as general teaching, then as the Buddha's own account of his "
            "pre-awakening practice."]),
    ],
    terms=[
        ("alaṁsājīvo",
         "&ldquo;fit to share one's life&rdquo; &mdash; this discourse's title and standard, a "
         "higher, more sustained bar than AN 5.65's fitness for discussion."),
        ("kataṁ pañhaṁ",
         "&ldquo;questions posed&rdquo; &mdash; this discourse's verb, more actively directed "
         "than AN 5.65's &lsquo;questions that come up&rsquo;."),
        ("sājīva",
         "&ldquo;shared life&rdquo; &mdash; the outcome this discourse names, naming something "
         "more total than a single successful conversation."),
        ("sākaccha",
         "&ldquo;discussion&rdquo; &mdash; AN 5.65's outcome, distinct from this discourse's "
         "sustained shared life."),
        ("byākattā",
         "&ldquo;one who answers, explains&rdquo; &mdash; the shared term across both "
         "discourses for the capacity to field questions on each of the five topics."),
    ],
    text_intro=(
        "The discourse in full: the five paired qualities required for fitness to share one's "
        "life with companions. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.66:1.1-1.2"),
        ("p", "&sect;2", "an5.66:1.3"),
        ("p", "&sect;3", "an5.66:1.4"),
        ("p", "&sect;4", "an5.66:1.5"),
        ("p", "&sect;5", "an5.66:1.6"),
        ("p", "&sect;6", "an5.66:1.7"),
        ("p", "&sect;7", "an5.66:1.8"),
    ],
    quiz=[
        {"q": "What single word changes across all five paired clauses, compared to AN 5.65?",
         "opts": [
             "The names of the five topics themselves",
             "'Āgataṁ' (comes up) becomes 'kataṁ' (posed), and the outcome shifts from 'fit for "
             "discussion' to 'fit to share one's life'",
             "Nothing changes at all",
             "The setting changes"],
         "correct": 1,
         "expl": "A small verb change plus a shift in the discourse's stated outcome."},
        {"q": "How does the guide distinguish 'āgataṁ' (questions that come up) from 'kataṁ' "
              "(questions posed)?",
         "opts": [
             "As identical, with no real difference",
             "As a fine but real distinction — organic conversation versus something closer to "
             "deliberate examination",
             "As a scribal error in one of the two discourses",
             "As contradictory claims"],
         "correct": 1,
         "expl": "A distinction worth noting without overstating its significance."},
        {"q": "How does 'alaṁsājīvo', fitness to share one's life, compare to AN 5.65's "
              "'alaṁsākaccho', fitness for discussion?",
         "opts": [
             "Identical in scope",
             "A higher, more sustained bar — naming something more total than a single "
             "successful conversation",
             "A lower bar than fitness for discussion",
             "Unrelated to fitness for discussion"],
         "correct": 1,
         "expl": "Living alongside companions day after day, not just conversing well once."},
        {"q": "Why does the guide suggest these two near-duplicate discourses are stated "
              "separately rather than combined into one?",
         "opts": [
             "There is no reason given",
             "A chanted tradition preserves genuinely distinct claims better as separate, "
             "complete, memorizable units than as one discourse with an appended variant",
             "Because the two discourses actually contradict each other",
             "Because one of them was composed much later"],
         "correct": 1,
         "expl": "The same oral-transmission reasoning already offered elsewhere in this nipāta."},
        {"q": "What pair of chapter discourses does AN 5.65–66 complete, following two earlier "
              "pairs?",
         "opts": [
             "The first pair in the chapter",
             "The third pair, after perceptions (61–62) and growth (63–64)",
             "The chapter's final pair",
             "There is no larger pattern of pairs in this chapter"],
         "correct": 1,
         "expl": "One of four matched pairs structuring this whole chapter."},
        {"q": "What five topics does this discourse require accomplishment in and ability to "
              "discuss?",
         "opts": [
             "Faith, conscience, prudence, energy, wisdom",
             "Ethics, immersion, wisdom, freedom, and the knowledge and vision of freedom",
             "The five hindrances",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "The identical five-item list as AN 5.65, from AN 5.17–20."},
        {"q": "What comes next in the chapter, after this pair?",
         "opts": [
             "A repeat of this pair",
             "AN 5.67 and 5.68, the bases of psychic power, first as general teaching then as the "
             "Buddha's own pre-awakening practice",
             "The chapter's final discourse",
             "A return to the five hindrances"],
         "correct": 1,
         "expl": "The chapter's fourth matched pair."},
        {"q": "Does this discourse offer any new definition of the five topics beyond AN 5.65's?",
         "opts": [
             "Yes, extensive new definitions",
             "No — the content is identical; only the verb and the outcome differ",
             "Only wisdom is redefined",
             "Only freedom is redefined"],
         "correct": 1,
         "expl": "A near-total repetition with two deliberate points of difference."},
        {"q": "What term describes the capacity to field questions on each topic, shared across "
              "both discourses?",
         "opts": [
             "Sākaccho", "Byākattā, one who answers or explains", "Sājīvo", "Sampanno"],
         "correct": 1,
         "expl": "The common term across both AN 5.65 and 5.66."},
        {"q": "Where is AN 5.66 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Rājagaha"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("One word changed", [
            "<span class=\"pali\">āgataṁ</span>comes up",
            "&darr;",
            "<span class=\"pali\">kataṁ</span>posed",
        ]),
        ("A higher bar", [
            "AN 5.65: discussion",
            "AN 5.66: shared life",
            "&mdash; one conversation vs. daily practice",
        ]),
        ("Chapter's third pair", [
            "perceptions &middot; growth",
            "discussion/sharing life",
            "&mdash; psychic power, next",
        ]),
        ("Cross-references", [
            "AN 5.65 &middot; the near-twin",
            "AN 5.17&ndash;20 &middot; the list, first used",
            "AN 5.67 &middot; next: psychic power",
        ]),
    ],
    further=[
        '<a href="%s/an5.66/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.65.html">AN 5.65 &middot; Discussion</a> &mdash; the previous discourse, '
        "this one's near-identical companion.",
        '<a href="an-5.67.html">AN 5.67 &middot; Bases of Psychic Power (1st)</a> &mdash; next, '
        "the chapter's fourth matched pair.",
        '<a href="an-5.17.html">AN 5.17 &middot; One&rsquo;s Own Welfare</a> &mdash; where this '
        "five-item list first structured a discourse unit in this nipāta.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.67 — Paṭhamaiddhipādasutta
# --------------------------------------------------------------------------- #
page(
    67, "Paṭhamaiddhipāda", "Bases of Psychic Power (1st)",
    vagga=VAGGA_7,
    meta_title="AN 5.67 — Bases of Psychic Power (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first Iddhipādasutta — "
        "the four bases of psychic power plus sheer vigor as a fifth, developed by any monk or "
        "nun, leading to enlightenment now or non-return at the least. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A guaranteed two-outcome claim, then five qualities named, four sharing an "
                 "identical formula and one standing apart"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four bases of psychic power (iddhipāda) are among the "
                              "thirty-seven aids to awakening widely attested across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a guaranteed outcome, "
                       "stated with unusual confidence for this chapter"),
    ],
    why=(
        "This discourse makes a claim stronger than a description of what supports practice; "
        "it names an outcome and guarantees one of exactly two results for anyone who develops "
        "these five qualities: full enlightenment in this very life, or, at the least, "
        "non-return. The five items themselves belong to one of the thirty-seven aids to "
        "awakening, the four <em>iddhipāda</em>, with a fifth quality added that stands outside "
        "the standard formula entirely."),
    guide=[
        ("The teaching in one sentence", [
            "Any monk or nun who develops the four bases of psychic power &mdash; immersion due "
            "to enthusiasm, energy, mental development, and inquiry, each with active effort "
            "&mdash; plus sheer vigor as a fifth, can expect either enlightenment in this life "
            "or non-return."]),
        ("A guaranteed either/or, not a maybe", [
            "<em>Dvinnaṁ phalānaṁ aññataraṁ phalaṁ pāṭikaṅkhaṁ</em>, one of two results can be "
            "expected, is a stronger claim than this chapter's other discourses have made. "
            "There is no third, lesser outcome named; the range runs from complete awakening at "
            "the top to non-return, itself among the highest attainments recognized in the "
            "canon, as the floor."]),
        ("Four bases, one formula, applied four times", [
            "<em>Chandasamādhipadhānasaṅkhārasamannāgataṁ iddhipādaṁ</em>, the basis of psychic "
            "power that has immersion born of enthusiasm and active effort, is one long compound "
            "applied unchanged four times, substituting only the driving quality: enthusiasm "
            "(<em>chanda</em>), energy (<em>vīriya</em>), mental development (<em>citta</em>), "
            "and inquiry (<em>vīmaṁsā</em>). Each names a different route to the same structural "
            "outcome &mdash; immersion paired with sustained effort."]),
        ("A fifth item, outside the formula", [
            "<em>Ussoḷhiññeva pañcamiṁ</em>, and the fifth is sheer vigor, breaks the pattern of "
            "the preceding four. It is not another basis of psychic power built from the same "
            "compound; it stands alone, unqualified, as if the four structured routes still "
            "needed something less formalized &mdash; raw, sustained determination &mdash; "
            "added on top."]),
        ("What follows", [
            "AN 5.68, immediately next, gives the identical five items a second time, but "
            "changes everything about their frame: not a general teaching to any monk or nun, "
            "but the Buddha's own first-person account of what he developed before his "
            "awakening, while still <em>a bodhisattva, not yet fully awakened</em>."]),
    ],
    terms=[
        ("iddhipāda",
         "&ldquo;basis of psychic power&rdquo; &mdash; one of the standard groups within the "
         "thirty-seven aids to awakening, four items sharing one compound formula here."),
        ("chanda vīriya citta vīmaṁsā",
         "&ldquo;enthusiasm, energy, mental development, inquiry&rdquo; &mdash; the four "
         "driving qualities, each substituted into the identical iddhipāda formula."),
        ("ussoḷhi",
         "&ldquo;sheer vigor&rdquo; &mdash; the fifth item, standing outside the four-item "
         "iddhipāda formula entirely, added unqualified."),
        ("diṭṭheva dhamme aññā",
         "&ldquo;enlightenment in this very life&rdquo; &mdash; the higher of the two "
         "guaranteed outcomes."),
        ("anāgāmitā",
         "&ldquo;non-return&rdquo; &mdash; the floor outcome, itself among the highest "
         "attainments recognized in the canon."),
    ],
    text_intro=(
        "The discourse in full: the guaranteed two-outcome claim, and the five qualities that "
        "produce it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.67:1.1-1.2"),
        ("h3", "The five qualities"),
        ("p", "&sect;2", "an5.67:2.1"),
        ("p", "&sect;3", "an5.67:2.2"),
        ("p", "&sect;4", "an5.67:2.3"),
        ("p", "&sect;5", "an5.67:2.4"),
        ("p", "&sect;6", "an5.67:2.5"),
        ("p", "&sect;7", "an5.67:2.6"),
        ("p", "&sect;8", "an5.67:2.7-2.8"),
    ],
    quiz=[
        {"q": "What two outcomes does this discourse guarantee for anyone who develops the five "
              "qualities?",
         "opts": [
             "A good rebirth or a bad one",
             "Enlightenment in this very life, or, at the least, non-return",
             "Wealth or poverty",
             "Fame or obscurity"],
         "correct": 1,
         "expl": "A guaranteed either/or, with no third, lesser outcome named."},
        {"q": "What are the four bases of psychic power, and what do they share?",
         "opts": [
             "Four entirely different formulas with nothing in common",
             "Enthusiasm, energy, mental development, and inquiry, each substituted into the "
             "identical iddhipāda compound formula",
             "The five hindrances",
             "The five powers of a trainee"],
         "correct": 1,
         "expl": "One long compound applied unchanged four times, only the driving quality changing."},
        {"q": "How does the fifth item, sheer vigor, differ from the preceding four?",
         "opts": [
             "It follows the identical formula as the others",
             "It stands outside the iddhipāda formula entirely, added unqualified rather than "
             "built from the same compound",
             "It is not actually part of the list",
             "It replaces one of the four bases"],
         "correct": 1,
         "expl": "Raw, sustained determination, added on top of the four structured routes."},
        {"q": "How does the strength of this discourse's claim compare to other discourses in "
              "this chapter?",
         "opts": [
             "Weaker — no specific outcome is claimed",
             "Stronger — a guaranteed outcome, unlike this chapter's more general claims about "
             "fruitfulness or fitness",
             "Identical to every other discourse in the chapter",
             "This discourse makes no claim at all"],
         "correct": 1,
         "expl": "A guaranteed either/or is unusually confident language for this chapter."},
        {"q": "What does AN 5.68, the next discourse, do with this identical list?",
         "opts": [
             "Nothing further; the list is dropped",
             "Gives it a second time, now as the Buddha's own first-person account of his "
             "pre-awakening practice",
             "Contradicts this discourse's claims",
             "Replaces it with a different five-item list"],
         "correct": 1,
         "expl": "The same content, reframed entirely as autobiography."},
        {"q": "Who is this discourse addressed to?",
         "opts": [
             "Only advanced meditators",
             "Any monk or nun (bhikkhu vā bhikkhunī vā)",
             "Only laypeople",
             "Only King Muṇḍa"],
         "correct": 1,
         "expl": "A general teaching, not restricted to any particular audience within the monastic community."},
        {"q": "What group of aids to awakening do the four iddhipāda belong to?",
         "opts": [
             "The five hindrances",
             "The thirty-seven aids to awakening (bodhipakkhiyā dhammā)",
             "The four noble truths",
             "The six perfections"],
         "correct": 1,
         "expl": "One of the standard groups within that wider framework."},
        {"q": "Is non-return described as a minor or lesser attainment?",
         "opts": [
             "Yes, a very minor one",
             "No — even as the floor outcome, it is itself among the highest attainments "
             "recognized in the canon",
             "The discourse does not characterize it at all",
             "It is described as worse than an ordinary rebirth"],
         "correct": 1,
         "expl": "The guaranteed range runs from complete awakening to a floor that is still exceptionally high."},
        {"q": "What does 'vīmaṁsā', the fourth driving quality, mean?",
         "opts": [
             "Physical strength",
             "Inquiry, investigation",
             "Wealth",
             "Faith"],
         "correct": 1,
         "expl": "The fourth of the four routes to the same iddhipāda structure."},
        {"q": "Where is AN 5.67 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Guaranteed outcome", [
            "enlightenment now, or",
            "non-return at the least",
        ]),
        ("Four bases, one formula", [
            "enthusiasm &middot; energy",
            "mental development",
            "inquiry",
        ]),
        ("A fifth, outside the pattern", [
            "<span class=\"pali\">ussoḷhi</span>",
            "&mdash; sheer vigor,",
            "unqualified",
        ]),
        ("Cross-references", [
            "AN 5.65&ndash;66 &middot; the previous pair",
            "AN 5.68 &middot; next: the Buddha's own practice",
            "AN 5.23 &amp; 5.28 &middot; the abhiññā this leads toward",
        ]),
    ],
    further=[
        '<a href="%s/an5.67/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.68.html">AN 5.68 &middot; Bases of Psychic Power (2nd)</a> &mdash; next, '
        "the same five qualities as the Buddha's own pre-awakening practice.",
        '<a href="an-5.66.html">AN 5.66 &middot; Sharing Life</a> &mdash; the previous discourse, '
        "closing this chapter's third matched pair.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; where the psychic-power '
        "abhiññā this discourse's outcome opens onto were listed in full.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.68 — Dutiyaiddhipādasutta
# --------------------------------------------------------------------------- #
page(
    68, "Dutiyaiddhipāda", "Bases of Psychic Power (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 5.68 — Bases of Psychic Power (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second Iddhipādasutta "
        "— the Buddha's own first-person account of developing the four bases of psychic power "
        "and vigor before his awakening, opening onto the full range of superhuman abilities. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", "The Buddha, speaking autobiographically in the first person"),
        ("Form", "AN 5.67's five qualities restated as first-person pre-awakening practice, "
                 "opening onto the extended abhiññā formula already met at AN 5.23 and AN 5.28"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "First-person accounts of the Buddha's own pre-awakening "
                              "practice recur across the Chinese Āgamas' biographical material; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the same five qualities as "
                       "AN 5.67, now spoken by the Buddha about himself"),
    ],
    why=(
        "This discourse takes AN 5.67's general teaching and does something this chapter has "
        "not done elsewhere: attributes it to the Buddha's own past, before awakening, "
        "<em>bodhisattova samāno</em>, while still a bodhisattva. The same five qualities that "
        "guarantee enlightenment or non-return for any monk or nun are here presented as what "
        "the Buddha himself developed and cultivated on the way to becoming the Buddha, opening "
        "directly onto the same extended list of superhuman abilities this series has already "
        "met."),
    guide=[
        ("The teaching in one sentence", [
            "Before his awakening, while still a bodhisattva, the Buddha developed and "
            "cultivated the same five qualities as AN 5.67, and having done so, was capable of "
            "realizing whatever he wished, since each and every ability was within range."]),
        ("The identical formula, now first person", [
            "Every word of the five qualities themselves &mdash; the four bases of psychic "
            "power built from enthusiasm, energy, mental development, and inquiry, plus sheer "
            "vigor as a fifth &mdash; matches AN 5.67 exactly. What changes entirely is the "
            "grammatical person: <em>bhāvesiṁ</em>, I developed, replacing the general "
            "<em>bhāveti</em>, one develops. A universal claim about any monk or nun becomes a "
            "specific claim about the Buddha's own past."]),
        ("A bodhisattva who needed the same five things", [
            "This is a genuinely notable claim, worth sitting with rather than passing over: the "
            "discourse does not present the Buddha's pre-awakening cultivation as categorically "
            "different from what any mendicant might develop. He is described using the same "
            "formula, requiring the same five qualities, as anyone else attempting this path "
            "&mdash; not exempted from the causal structure by virtue of who he would become."]),
        ("Opening onto the full abhiññā list, again", [
            "Once the five qualities are established, the discourse moves into the extended "
            "formula for superhuman abilities already given in full at "
            "<a href=\"an-5.23.html\">AN 5.23</a> and, in even greater length, at the legacy "
            "page <a href=\"an-5.28.html\">AN 5.28</a>: psychic power, clairaudience, reading "
            "minds, recollecting past lives, clairvoyance, and the ending of defilements. This "
            "discourse gives only the first and last of that list in full &mdash; multiplying "
            "the self, and freedom of heart and wisdom &mdash; trusting the reader to recall the "
            "complete formula from where it was already given twice."]),
        ("Closing this chapter's fourth pair", [
            "AN 5.67 and 5.68 complete the fourth of this chapter's matched pairs. AN 5.69 and "
            "5.70, the final two discourses, will return to perception, giving the chapter's "
            "fifth and last pair on the identical structural principle: one list, two "
            "consequences named."]),
    ],
    terms=[
        ("bodhisatta",
         "&ldquo;one intent on awakening&rdquo; &mdash; the Buddha's own term for himself "
         "before his awakening, used in this discourse's opening line."),
        ("anabhisambuddho",
         "&ldquo;not yet fully awakened&rdquo; &mdash; the qualifier marking this account as "
         "specifically pre-awakening practice."),
        ("bhāvesiṁ",
         "&ldquo;I developed&rdquo; &mdash; the first-person verb replacing AN 5.67's general "
         "third-person formula throughout this discourse."),
        ("sakkhibhabbataṁ pāpuṇāti",
         "&ldquo;becomes capable of realizing&rdquo; &mdash; the phrase marking the transition "
         "from the five qualities to the extended abhiññā formula."),
        ("cetovimutti paññāvimutti",
         "&ldquo;freedom of heart, freedom by wisdom&rdquo; &mdash; the final ability named, "
         "closing the abbreviated abhiññā list this discourse gives."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's first-person account of pre-awakening practice, "
        "and the abilities it opened onto, given here in abbreviated form. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Before my awakening"),
        ("p", "&sect;1", "an5.68:1.1-1.2"),
        ("p", "&sect;2", "an5.68:1.3-1.7"),
        ("p", "&sect;3", "an5.68:1.8-1.9"),
        ("h3", "What became possible"),
        ("p", "&sect;4", "an5.68:2.1-2.2"),
        ("p", "&sect;5", "an5.68:3.1-3.2"),
    ],
    quiz=[
        {"q": "Who is the speaker of this discourse, and what is distinctive about the framing?",
         "opts": [
             "A monk, addressing other monks generally",
             "The Buddha, speaking in the first person about his own pre-awakening practice as a "
             "bodhisattva",
             "Venerable Nārada",
             "An unnamed narrator describing events objectively"],
         "correct": 1,
         "expl": "A specific autobiographical claim, not general instruction."},
        {"q": "How do the five qualities in this discourse compare to AN 5.67's?",
         "opts": [
             "Entirely different qualities",
             "Identical — the same four iddhipāda plus vigor, with only the grammatical person "
             "changed",
             "Only three of the five match",
             "This discourse names six qualities instead of five"],
         "correct": 1,
         "expl": "A universal third-person claim becomes a specific first-person one."},
        {"q": "What does the guide find notable about how the Buddha describes his own "
              "pre-awakening cultivation?",
         "opts": [
             "That it is presented as categorically superior to and different from any ordinary "
             "mendicant's practice",
             "That he is described using the same formula and the same five required qualities as "
             "anyone else, not exempted from the causal structure",
             "That the discourse claims he needed no effort at all",
             "That the discourse denies he ever practiced these qualities"],
         "correct": 1,
         "expl": "Worth sitting with rather than passing over, per the guide's reading."},
        {"q": "Where was the extended abhiññā formula this discourse opens onto already given in "
              "full?",
         "opts": [
             "Nowhere before this page",
             "AN 5.23 and, at greater length, the legacy page AN 5.28",
             "Only in AN 5.67",
             "Only in AN 4.163"],
         "correct": 1,
         "expl": "This discourse gives only the first and last items, trusting the reader to recall the rest."},
        {"q": "Which two abilities does this discourse actually spell out from the full abhiññā "
              "list?",
         "opts": [
             "Clairaudience and past-life recall",
             "Multiplying the self, and freedom of heart and wisdom",
             "Reading minds and clairvoyance",
             "All six abilities in full"],
         "correct": 1,
         "expl": "The first and last of the extended list, with the rest left implicit."},
        {"q": "What term does the Buddha use for himself before his awakening?",
         "opts": [
             "Arahant", "Bodhisatta, one intent on awakening", "Tathāgata", "Sekha"],
         "correct": 1,
         "expl": "A specific term marking his pre-awakening status."},
        {"q": "What pair of chapter discourses does AN 5.67–68 complete?",
         "opts": [
             "The chapter's first pair",
             "The fourth of this chapter's matched pairs",
             "There is no larger pattern of pairs in this chapter",
             "The chapter's only pair"],
         "correct": 1,
         "expl": "Following perceptions, growth, and discussion/shared-life as the first three."},
        {"q": "What does AN 5.69, the next discourse, return to?",
         "opts": [
             "A repeat of the psychic-power material",
             "Perception, giving the chapter's fifth and final matched pair",
             "The five hindrances",
             "The chapter simply ends after AN 5.68"],
         "correct": 1,
         "expl": "One list, two consequences, closing the chapter on the same structural principle."},
        {"q": "Does this discourse claim the Buddha's pre-awakening practice differed in kind from "
              "what AN 5.67 describes for any monk or nun?",
         "opts": [
             "Yes, an entirely different set of qualities",
             "No — the identical five qualities and identical formula, only the grammatical "
             "person changes",
             "Yes, a shorter list",
             "The discourse does not compare the two at all"],
         "correct": 1,
         "expl": "The same structural claim, now spoken in the first person about a specific past."},
        {"q": "Where is AN 5.68 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Uruvelā, by the Nerañjarā"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Same five, first person", [
            "AN 5.67: any monk, nun",
            "AN 5.68: &ldquo;I developed&hellip;&rdquo;",
        ]),
        ("No exemption", [
            "the bodhisattva,",
            "same formula,",
            "same five qualities",
        ]),
        ("The abhiññā, abbreviated", [
            "multiplying the self &hellip;",
            "&hellip; freedom of heart",
            "&amp; wisdom",
        ]),
        ("Cross-references", [
            "AN 5.67 &middot; the general teaching",
            "AN 5.23 &amp; 5.28 &middot; the full abhiññā list",
            "AN 5.69 &middot; next: perception, again",
        ]),
    ],
    further=[
        '<a href="%s/an5.68/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.67.html">AN 5.67 &middot; Bases of Psychic Power (1st)</a> &mdash; the '
        "general teaching this discourse restates as the Buddha's own past practice.",
        '<a href="an-5.23.html">AN 5.23 &middot; Corruptions</a> &mdash; where the full abhiññā '
        "list this discourse abbreviates was given in complete form.",
        '<a href="an-5.69.html">AN 5.69 &middot; Disillusionment</a> &mdash; next, the '
        "chapter's fifth and closing matched pair, returning to perception.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.69 — Nibbidāsutta
# --------------------------------------------------------------------------- #
page(
    69, "Nibbidā", "Disillusionment",
    vagga=VAGGA_7,
    meta_title="AN 5.69 — Disillusionment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nibbidāsutta — five of "
        "this chapter's perceptions recombined into a single unified practice, leading through "
        "a seven-term chain to disillusionment, awakening, and extinguishment. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A seven-term consequence named first, then five perceptions combined into a "
                 "single practice rather than five separate contemplations"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Chains of consequence terms culminating in awakening and "
                              "extinguishment recur widely across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; recombines this chapter's "
                       "opening material into a single integrated practice"),
    ],
    why=(
        "This discourse returns to the perceptions this chapter opened with at "
        "<a href=\"an-5.61.html\">AN 5.61</a> and <a href=\"an-5.62.html\">AN 5.62</a>, but "
        "does something neither of those did: it combines five of them, drawn from both earlier "
        "lists, into what reads as a single continuous practice rather than five discrete "
        "objects, and names not one outcome but a chain of seven, ending in "
        "<em>nibbāna</em> itself."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who observes the body's ugliness, perceives food's repulsiveness, "
            "perceives dissatisfaction with the whole world, observes the impermanence of all "
            "conditions, and has well established the perception of their own death, develops "
            "five things that lead solely to disillusionment, dispassion, cessation, peace, "
            "insight, awakening, and extinguishment."]),
        ("Five items, drawn from both earlier lists", [
            "Ugliness and food's repulsiveness come from AN 5.61's list; world-dissatisfaction "
            "is shared by both AN 5.61 and 5.62; impermanence comes from AN 5.62's list; and "
            "death's perception appears, in slightly different phrasing, in both. This discourse "
            "is not simply repeating either earlier list; it is drawing a new fifth combination "
            "from the shared pool those two discourses established."]),
        ("One practice, not five separate contemplations", [
            "Where AN 5.61 and 5.62 each named five perceptions as parallel items in a set, this "
            "discourse's grammar runs the five together as a description of a single mendicant's "
            "ongoing practice &mdash; observing, perceiving, perceiving, observing, having "
            "established, one continuous sentence covering all five. The difference in "
            "presentation is worth noticing: a list to be selected from becomes, here, an "
            "integrated way of meditating."]),
        ("Seven terms, not one outcome", [
            "<em>Ekantanibbidāya virāgāya nirodhāya upasamāya abhiññāya sambodhāya "
            "nibbānāya</em>, disillusionment, dispassion, cessation, peace, insight, awakening, "
            "extinguishment &mdash; seven terms strung together rather than one word standing in "
            "for the whole result. This chain has appeared before in this series, at "
            "<a href=\"an-1.296-305.html\">AN 1.296&ndash;305</a>'s ten objects of "
            "recollection, applied there to a different set of practices; here it names the "
            "consequence of this specific five-part combination."]),
        ("A closing pair that differs only in outcome", [
            "AN 5.70, the very next and final discourse of this chapter, will give this "
            "identical five-part practice one more time, changing only what it is said to lead "
            "to &mdash; not the seven-term chain, but simply <em>āsavānaṁ khayāya</em>, the "
            "ending of defilements. The chapter's fifth and closing pair repeats a pattern this "
            "chapter has used four times already: one practice, two consequences."]),
    ],
    terms=[
        ("asubhānupassī",
         "&ldquo;observing ugliness&rdquo; &mdash; the first item, drawn from AN 5.61's earlier "
         "list."),
        ("sabbasaṅkhāresu aniccānupassī",
         "&ldquo;observing the impermanence of all conditions&rdquo; &mdash; the fourth item, "
         "drawn from AN 5.62's list."),
        ("maraṇasaññā sūpaṭṭhitā",
         "&ldquo;the perception of death, well established&rdquo; &mdash; the fifth item, "
         "phrased slightly differently from both AN 5.61 and 5.62's versions."),
        ("ekantanibbidā",
         "&ldquo;solely to disillusionment&rdquo; &mdash; the first term of the seven-part "
         "chain, marking this discourse's outcome as unidirectional."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; the final and highest term in the seven-part "
         "chain this discourse's practice leads to."),
    ],
    text_intro=(
        "The discourse in full: the seven-term outcome named, then the five perceptions combined "
        "into a single practice. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.69:1.1"),
        ("h3", "The combined practice"),
        ("p", "&sect;2", "an5.69:2.1-2.2"),
        ("p", "&sect;3", "an5.69:2.3"),
    ],
    quiz=[
        {"q": "What five items does this discourse combine into a single practice?",
         "opts": [
             "Faith, ethics, learning, generosity, and wisdom",
             "Observing ugliness, perceiving food's repulsiveness, perceiving "
             "world-dissatisfaction, observing impermanence, and the perception of death",
             "The five hindrances",
             "Long life, beauty, happiness, fame, and heaven"],
         "correct": 1,
         "expl": "A new combination drawn from AN 5.61 and 5.62's earlier lists."},
        {"q": "How does this discourse's grammar present the five items, compared to AN 5.61 and "
              "5.62?",
         "opts": [
             "Identically, as five parallel items in a set to select from",
             "As one continuous sentence describing a single mendicant's integrated ongoing "
             "practice, rather than five separate parallel items",
             "As five entirely unrelated topics",
             "In reverse order"],
         "correct": 1,
         "expl": "A list becomes, here, a description of one unified practice."},
        {"q": "What seven-term chain does this discourse name as the outcome?",
         "opts": [
             "A single word, 'awakening'",
             "Disillusionment, dispassion, cessation, peace, insight, awakening, and "
             "extinguishment",
             "The four noble truths",
             "The five powers"],
         "correct": 1,
         "expl": "Seven terms strung together, not one word standing for the whole result."},
        {"q": "Where has this same seven-term chain appeared before in this series?",
         "opts": [
             "Nowhere before this page",
             "AN 1.296–305, applied there to the ten objects of recollection",
             "Only in AN 5.61",
             "Only in AN 4.163"],
         "correct": 1,
         "expl": "The identical chain, applied to a different set of practices earlier in the series."},
        {"q": "What does AN 5.70, the final discourse of this chapter, change from this one?",
         "opts": [
             "Nothing; it repeats this discourse verbatim including the outcome",
             "Only the stated outcome — from the seven-term chain to simply 'the ending of "
             "defilements' — with the identical five-part practice",
             "The five items themselves",
             "It contradicts this discourse entirely"],
         "correct": 1,
         "expl": "The same practice, a different named consequence, completing the chapter's fifth pair."},
        {"q": "Which two of the five items in this discourse come specifically from AN 5.62's "
              "list rather than AN 5.61's?",
         "opts": [
             "Ugliness and food's repulsiveness",
             "Impermanence, and world-dissatisfaction (shared by both)",
             "Death and drawbacks",
             "None; all five come from AN 5.61 alone"],
         "correct": 1,
         "expl": "A genuine mixing of both earlier lists, not a simple repeat of either."},
        {"q": "What structural pattern does this discourse and AN 5.70 repeat, already used four "
              "times in this chapter?",
         "opts": [
             "No repeated pattern exists",
             "One practice or list, two different named consequences",
             "Two entirely different practices with the same consequence",
             "A three-part structure unique to this pair"],
         "correct": 1,
         "expl": "The chapter's fifth and final instance of its defining pairing structure."},
        {"q": "What does 'ekantanibbidā' mean?",
         "opts": [
             "'Occasionally to disillusionment'",
             "'Solely to disillusionment' — marking the outcome as unidirectional",
             "'Never to disillusionment'",
             "'Partially to disillusionment'"],
         "correct": 1,
         "expl": "The first term of the seven-part chain, emphasizing a single, unwavering direction."},
        {"q": "Is 'nibbāna' the first or last term in this discourse's seven-part chain?",
         "opts": [
             "The first term", "The last and highest term", "It does not appear in the chain",
             "It appears in the middle"],
         "correct": 1,
         "expl": "The chain's final and highest term."},
        {"q": "Where is AN 5.69 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Pāṭaliputta"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Five, recombined", [
            "ugliness &middot; food",
            "world-dissatisfaction",
            "impermanence &middot; death",
        ]),
        ("One practice, not a set", [
            "one continuous sentence,",
            "not five parallel",
            "items to select from",
        ]),
        ("Seven-term chain", [
            "disillusionment &rarr; dispassion",
            "&rarr; cessation &rarr; peace",
            "&rarr; insight &rarr; awakening",
            "&rarr; extinguishment",
        ]),
        ("Cross-references", [
            "AN 5.61&ndash;62 &middot; the source lists",
            "AN 1.296&ndash;305 &middot; the same chain, elsewhere",
            "AN 5.70 &middot; next: same practice, one outcome",
        ]),
    ],
    further=[
        '<a href="%s/an5.69/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.61.html">AN 5.61 &middot; Perceptions (1st)</a> &mdash; one of the two '
        "earlier lists this discourse draws its five items from.",
        '<a href="an-5.70.html">AN 5.70 &middot; The Ending of Defilements</a> &mdash; next, the '
        "identical practice with a single different outcome, closing the chapter.",
        '<a href="an-1.296-305.html">AN 1.296&ndash;305</a> &mdash; where this same seven-term '
        "chain first appeared in this series, applied to a different set of practices.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.70 — Āsavakkhayasutta
# --------------------------------------------------------------------------- #
page(
    70, "Āsavakkhaya", "The Ending of Defilements",
    vagga=VAGGA_7,
    meta_title="AN 5.70 — The Ending of Defilements | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Āsavakkhayasutta, "
        "closing this chapter — AN 5.69's identical five-part practice, now leading simply to "
        "the ending of defilements rather than a seven-term chain. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "AN 5.69's five-part practice restated word for word, with a single-term "
                 "outcome replacing the seven-term chain, closing the chapter's own colophon"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The ending of defilements (āsavakkhaya) as the culmination of "
                              "sustained contemplative practice is a standard formula across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; closes the chapter by "
                       "compressing AN 5.69's seven-term chain into its single practical core"),
    ],
    why=(
        "This chapter's final discourse takes AN 5.69's five-part practice &mdash; word for "
        "word identical, down to the last phrase &mdash; and names a single outcome in place of "
        "the seven-term chain: <em>āsavānaṁ khayāya</em>, the ending of defilements. Where AN "
        "5.69 traced the full arc from disillusionment to extinguishment, this discourse names "
        "only the arc's practical, functional endpoint."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who observes the body's ugliness, perceives food's repulsiveness, "
            "perceives dissatisfaction with the whole world, observes the impermanence of all "
            "conditions, and has well established the perception of their own death, develops "
            "five things that lead to the ending of defilements."]),
        ("One outcome standing in for seven", [
            "<em>Āsavakkhaya</em>, the ending of defilements, is not a different result from AN "
            "5.69's seven-term chain; it is, in effect, that entire chain's practical shorthand "
            "&mdash; the state that disillusionment, dispassion, cessation, peace, insight, "
            "awakening, and extinguishment collectively describe, named here by its single most "
            "concrete, functional term."]),
        ("Why give the same practice two different labels", [
            "Read together, AN 5.69 and 5.70 make the same point two ways: a rich, sevenfold "
            "description of what this practice culminates in, and a single, practical name for "
            "the same culmination. Neither discourse is more correct than the other; a reader "
            "who wants the full arc has AN 5.69, and a reader who wants the compressed, "
            "actionable term has this discourse."]),
        ("Five discourses, five variations on repetition", [
            "This chapter closes having used the same underlying device five separate times: "
            "perceptions with two overlapping lists (61&ndash;62), growth for two genders "
            "(63&ndash;64), fitness for two social functions (65&ndash;66), the bases of "
            "psychic power for two speakers (67&ndash;68), and now a single practice with two "
            "named outcomes (69&ndash;70). No two pairs vary in quite the same way, which is "
            "worth appreciating as the chapter's real accomplishment: repetition used five "
            "different times to make five genuinely different points."]),
        ("The chapter's own closing colophon", [
            "As at the close of every earlier chapter, the source appends "
            "<em>Saññāvaggo dutiyo</em> &mdash; the second chapter, on perceptions, within the "
            "restarting count &mdash; followed by the chapter's own untranslated uddāna verse. "
            "The next chapter, Yodhājīvavagga, turns to warriors."]),
    ],
    terms=[
        ("āsavakkhaya",
         "&ldquo;ending of defilements&rdquo; &mdash; this discourse's title and single-term "
         "outcome, the practical shorthand for AN 5.69's seven-term chain."),
        ("āsava",
         "&ldquo;defilement, taint, corruption&rdquo; &mdash; the underlying term, referring to "
         "the deep-seated impurities whose ending marks full liberation."),
        ("asubhānupassī",
         "&ldquo;observing ugliness&rdquo; &mdash; the first of the five practices, identical to "
         "AN 5.69's wording."),
        ("maraṇasaññā sūpaṭṭhitā",
         "&ldquo;the perception of death, well established&rdquo; &mdash; the fifth practice, "
         "worded identically to AN 5.69."),
        ("Saññāvaggo dutiyo",
         "&ldquo;the second chapter, on perceptions&rdquo; &mdash; this vagga's closing "
         "colophon, matching the form already explained in full at AN 5.10."),
    ],
    text_intro=(
        "The discourse in full: the same five-part practice as AN 5.69, now leading to the "
        "ending of defilements. The chapter's closing colophon and Pāli mnemonic verse are part "
        "of the source but are not translated text, and are described rather than reproduced "
        "here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "an5.70:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this discourse's five-part practice compare to AN 5.69's?",
         "opts": [
             "Entirely different practices",
             "Word for word identical",
             "Similar but with two items changed",
             "This discourse gives only three of the five items"],
         "correct": 1,
         "expl": "The identical practice, down to the last phrase."},
        {"q": "What single outcome does this discourse name in place of AN 5.69's seven-term "
              "chain?",
         "opts": [
             "Wealth and prosperity",
             "Āsavakkhaya, the ending of defilements",
             "Rebirth as a god",
             "Fame in this life"],
         "correct": 1,
         "expl": "A practical shorthand for the same culmination the seven-term chain describes."},
        {"q": "How does the guide characterize the relationship between AN 5.69's seven-term "
              "chain and this discourse's single term?",
         "opts": [
             "As two contradictory claims about different outcomes",
             "As the same culmination described two ways — a rich sevenfold arc and its "
             "compressed, functional shorthand",
             "As entirely unrelated results",
             "As AN 5.70 correcting an error in AN 5.69"],
         "correct": 1,
         "expl": "Neither discourse is more correct; they serve different purposes."},
        {"q": "How does the guide summarize this chapter's overall use of paired, near-duplicate "
              "discourses?",
         "opts": [
             "As a lazy, uncreative repetition of the same content five times",
             "As the same underlying device used five separate times, with no two pairs varying "
             "in quite the same way",
             "As an error in the text's transmission",
             "As unrelated to any pattern"],
         "correct": 1,
         "expl": "Five genuinely different points made through five differently structured pairs."},
        {"q": "What colophon closes this chapter?",
         "opts": [
             "No colophon is present",
             "Saññāvaggo dutiyo, followed by the chapter's own untranslated uddāna verse",
             "A colophon naming a different chapter",
             "The colophon from AN 5.60, repeated verbatim"],
         "correct": 1,
         "expl": "Matching the structure already explained in full at AN 5.10."},
        {"q": "What chapter follows the Saññāvagga?",
         "opts": [
             "A return to the Muṇḍarājavagga",
             "The Yodhājīvavagga, turning to warriors",
             "The end of the entire nipāta",
             "A repeat of the Nīvaraṇavagga"],
         "correct": 1,
         "expl": "The next chapter in sequence, per this discourse's guide."},
        {"q": "What does 'āsava' refer to?",
         "opts": [
             "A type of meditation posture",
             "Defilement, taint — deep-seated impurities whose ending marks full liberation",
             "A monastic robe",
             "A specific meal offering"],
         "correct": 1,
         "expl": "The underlying term behind this discourse's title, āsavakkhaya."},
        {"q": "How many discourses in this chapter used the same underlying pairing device, "
              "counting AN 5.69–70?",
         "opts": [
             "Only this one pair",
             "Five pairs total across the whole chapter",
             "Three pairs",
             "The chapter has no such pairs"],
         "correct": 1,
         "expl": "Perceptions, growth, discussion/shared-life, psychic power, and now practice/outcome."},
        {"q": "Are the five practices in this discourse newly defined, or inherited from AN 5.69?",
         "opts": [
             "Newly defined here in full",
             "Inherited unchanged from AN 5.69",
             "Only three of the five are repeated",
             "A different five items entirely"],
         "correct": 1,
         "expl": "Word for word identical to the previous discourse."},
        {"q": "Where is AN 5.70 set?",
         "opts": [
             "A new location, stated explicitly",
             "None restated — continuing from AN 5.1's setting",
             "Vesālī",
             "Bhaddiya"],
         "correct": 1,
         "expl": "Consistent with the default setting used throughout this nipāta when nothing new is stated."},
    ],
    marginalia=[
        ("Same practice", [
            "identical to AN 5.69,",
            "word for word",
        ]),
        ("One outcome named", [
            "<span class=\"pali\">āsavakkhaya</span>",
            "&mdash; ending of",
            "defilements",
        ]),
        ("Five pairs, five points", [
            "perceptions &middot; growth",
            "discussion/life &middot; power",
            "practice/outcome",
        ]),
        ("Cross-references", [
            "AN 5.69 &middot; the seven-term version",
            "AN 5.10 &middot; the colophon, explained",
            "AN 5.71 &middot; next: Yodhājīvavagga",
        ]),
    ],
    further=[
        '<a href="%s/an5.70/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.69.html">AN 5.69 &middot; Disillusionment</a> &mdash; the previous '
        "discourse, this one's word-for-word companion.",
        '<a href="an-5.61.html">AN 5.61 &middot; Perceptions (1st)</a> &mdash; where this '
        "chapter opened, on the source material this closing pair recombines.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; where this same '
        "chapter-closing colophon structure was first explained in full.",
    ],
)
# --------------------------------------------------------------------------- #
# AN 5.71 — Paṭhamacetovimuttiphalasutta
# --------------------------------------------------------------------------- #
VAGGA_8 = "<em>Yodhājīvavagga</em> &mdash; the eighth chapter of the Fives"

page(
    71, "Paṭhamacetovimuttiphala", "Freedom of Heart is the Fruit (1st)",
    vagga=VAGGA_8,
    meta_title="AN 5.71 — Freedom of Heart is the Fruit (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamacetovimuttiphalasutta, opening the Warriors chapter — AN 5.69's five practices "
        "recur, now leading to a besieged fortress finally standing open: cross-bar lifted, "
        "moat filled, pillar pulled, unimpeded, banner lowered. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "a numbered list of five practices, followed by five fortress epithets, each "
                 "explained in turn by naming what has been given up"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; military and fortress "
                       "vocabulary applied to interior states, unpacked term by term"),
    ],
    why=(
        "This discourse opens Yodhājīvavagga, the Warriors, with an image the chapter will "
        "return to twice more before it closes: liberation as a fortress finally standing open "
        "&mdash; its cross-bar lifted, its moat filled in, its central pillar pulled up, its "
        "gate unimpeded, its banner lowered and burden dropped. Five practices already used at "
        "AN 5.69&ndash;70 recur here, now leading not to disillusionment's long arc but to this "
        "single vivid image, unpacked term by term."),
    guide=[
        ("The five practices, once more", [
            "The opening list is exactly AN 5.69 and 5.70's five practices: observing the "
            "body's ugliness, perceiving food's repulsiveness, perceiving dissatisfaction with "
            "the whole world, observing the impermanence of all conditions, and having well "
            "established the perception of one's own death. Their fruit here is named as "
            "<em>cetovimutti</em> and <em>paññāvimutti</em> &mdash; freedom of heart and "
            "freedom by wisdom &mdash; the same twin outcome AN 5.69's seven-term chain and AN "
            "5.70's single term both ultimately named."]),
        ("A fortress, not a chain", [
            "Where AN 5.69&ndash;70 described an unfolding sequence, this discourse switches "
            "images entirely: a mendicant who has this twofold freedom is called, all at once, "
            "one who has lifted the cross-bar, filled in the moat, pulled up the pillar, become "
            "unimpeded, and lowered the banner while dropping the burden and becoming detached "
            "&mdash; five names for a single fortified position that has stopped needing its "
            "own defenses."]),
        ("Lifted the cross-bar, filled in the moat", [
            "The cross-bar (<em>paligha</em>) that once barred the gate stands for ignorance "
            "(<em>avijjā</em>); the moat (<em>parikha</em>) that once encircled the fortress, "
            "keeping the siege going indefinitely, stands for transmigration through future "
            "births (<em>ponobhavika jātisaṁsāra</em>). Both are described as given up by the "
            "same formula used throughout this collection for a fully eradicated quality: cut "
            "off at the root, made like a palm stump, obliterated, unable to arise again."]),
        ("Pulled up the pillar, unimpeded", [
            "The pillar (<em>esikā</em>), a fortification's load-bearing post, stands for "
            "craving (<em>taṇhā</em>) &mdash; pull it out and the whole structure it was "
            "holding up no longer stands. To be unimpeded (<em>niraggaḷa</em>, without a bolt "
            "or bar) is to have given up the five lower fetters, the bindings that tie a person "
            "to the sensual realm and its lower rebirths: identity view, doubt, misapprehension "
            "of precepts and observances, sensual desire, and ill will."]),
        ("Banner lowered, burden dropped, detached", [
            "The final epithet describes a noble one (<em>ariya</em>) with banner lowered, "
            "burden dropped, and detached &mdash; given up here as the conceit &lsquo;I "
            "am&rsquo; (<em>asmimāna</em>). This is traditionally the last and subtlest "
            "residue of self-reference to fall away, surviving even after the coarser fetters "
            "are gone; naming it last, after four other eradications, matches how gradually and "
            "how late this particular conceit is said to loosen its grip."]),
        ("A pair to come", [
            "AN 5.72 immediately follows with the identical fruit and the identical five "
            "fortress epithets, but reaches them through an entirely different, progressive "
            "five-step perception chain rather than this discourse's static five-topic list "
            "&mdash; two different routes into the same standing-open fortress."]),
    ],
    terms=[
        ("cetovimutti / paññāvimutti",
         "&ldquo;freedom of heart&rdquo; and &ldquo;freedom by wisdom&rdquo; &mdash; the twin "
         "fruit named at the head of this discourse, matching AN 5.69&ndash;70's culmination."),
        ("ukkhittapaligha",
         "&ldquo;one who has lifted the cross-bar&rdquo; &mdash; given up ignorance, cut off at "
         "the root."),
        ("taṇhā",
         "&ldquo;craving&rdquo; &mdash; the fortress's central pillar, pulled up and given up."),
        ("orambhāgiya saṁyojana",
         "the five lower fetters &mdash; identity view, doubt, misapprehension of precepts and "
         "observances, sensual desire, and ill will &mdash; given up to become unimpeded."),
        ("asmimāna",
         "the conceit &lsquo;I am&rsquo; &mdash; traditionally the last, subtlest residue of "
         "self-reference to fall away, named last in this discourse's sequence of eradications."),
    ],
    text_intro=(
        "The discourse in full: five practices, their twofold fruit, and five fortress epithets "
        "each unpacked in turn. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five practices, and their fruit"),
        ("p", "&sect;1", "an5.71:1.1-2.5"),
        ("h3", "Lifted the cross-bar"),
        ("p", "&sect;2", "an5.71:3.1-3.3"),
        ("h3", "Filled in the moat"),
        ("p", "&sect;3", "an5.71:4.1-4.3"),
        ("h3", "Pulled up the pillar"),
        ("p", "&sect;4", "an5.71:5.1-5.3"),
        ("h3", "Unimpeded"),
        ("p", "&sect;5", "an5.71:6.1-6.3"),
        ("h3", "Banner lowered, burden dropped, detached"),
        ("p", "&sect;6", "an5.71:7.1-7.3"),
    ],
    quiz=[
        {"q": "What twofold fruit is named for the five opening practices?",
         "opts": [
             "Wealth and long life",
             "Freedom of heart and freedom by wisdom",
             "Rebirth as a deity",
             "Mastery of the four jhānas only"],
         "correct": 1,
         "expl": "Cetovimutti and paññāvimutti, matching AN 5.69–70's culmination."},
        {"q": "Which of these is NOT one of the five opening practices?",
         "opts": [
             "Observing the body's ugliness",
             "Perceiving food's repulsiveness",
             "Reciting the discourses daily",
             "Well-established perception of one's own death"],
         "correct": 2,
         "expl": "The five are ugliness, food, world-dissatisfaction, impermanence, and death — not recitation."},
        {"q": "What does 'lifted the cross-bar' stand for giving up?",
         "opts": [
             "Craving",
             "Ignorance",
             "The five lower fetters",
             "The conceit 'I am'"],
         "correct": 1,
         "expl": "Avijjā, cut off at the root."},
        {"q": "What does 'filled in the moat' stand for giving up?",
         "opts": [
             "Transmigrating through future births",
             "Sensual desire alone",
             "Doubt",
             "Ill will"],
         "correct": 0,
         "expl": "Ponobhavika jātisaṁsāra — rebirth after rebirth, filled in like a moat."},
        {"q": "What does 'pulled up the pillar' stand for giving up?",
         "opts": [
             "Ignorance",
             "Craving",
             "Identity view",
             "The five lower fetters"],
         "correct": 1,
         "expl": "Taṇhā, the load-bearing post of the whole structure."},
        {"q": "What does 'unimpeded' stand for giving up?",
         "opts": [
             "The conceit 'I am'",
             "Craving",
             "The five lower fetters",
             "Ignorance"],
         "correct": 2,
         "expl": "The orambhāgiya saṁyojana — identity view, doubt, precept-misapprehension, sensual desire, ill will."},
        {"q": "What does the final epithet, 'banner lowered, burden dropped, detached', stand for giving up?",
         "opts": [
             "The five lower fetters",
             "Craving",
             "The conceit 'I am'",
             "Ignorance"],
         "correct": 2,
         "expl": "Asmimāna, traditionally the last and subtlest self-referential conceit to fall away."},
        {"q": "What formula describes each of these five acts of giving up?",
         "opts": [
             "Simply forgotten over time",
             "Suppressed but still present",
             "Cut off at the root, made like a palm stump, obliterated, unable to arise again",
             "Transformed into something wholesome"],
         "correct": 2,
         "expl": "The standard full-eradication formula used throughout this collection."},
        {"q": "Where did this same five-item opening list of practices previously appear in this nipāta?",
         "opts": [
             "Nowhere else",
             "AN 5.69 and AN 5.70",
             "AN 5.51 only",
             "AN 5.1"],
         "correct": 1,
         "expl": "Word for word the same five practices that closed the previous chapter."},
        {"q": "How does AN 5.72, immediately following, reach the same fortress epithets?",
         "opts": [
             "Through an unrelated topic entirely",
             "Through an identical five-topic list",
             "Through a different, progressive five-step perception chain",
             "It does not reach the same epithets"],
         "correct": 2,
         "expl": "Impermanence, suffering-in-impermanence, not-self-in-suffering, giving up, fading away — a chain, not a list."},
    ],
    marginalia=[
        ("Five images, one fortress", [
            "cross-bar &middot; moat",
            "pillar &middot; unimpeded",
            "banner lowered",
        ]),
        ("The eradication formula", [
            "cut off at the root,",
            "made like a palm stump,",
            "unable to arise again",
        ]),
        ("Term", [
            "<span class=\"pali\">asmimāna</span>",
            "&mdash; the conceit",
            "&lsquo;I am&rsquo;, named last",
        ]),
        ("Cross-references", [
            "AN 5.69&ndash;70 &middot; source of the five practices",
            "AN 5.72 &middot; same epithets, a different route",
            "AN 5.75 &middot; the chapter's title discourse",
        ]),
    ],
    further=[
        '<a href="%s/an5.71/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.72.html">AN 5.72 &middot; Freedom of Heart is the Fruit (2nd)</a> '
        "&mdash; this discourse's twin, reaching the same fortress epithets by a different route.",
        '<a href="an-5.70.html">AN 5.70 &middot; The Ending of Defilements</a> &mdash; the '
        "immediate source of this discourse's five opening practices.",
        '<a href="an-5.75.html">AN 5.75 &middot; Warriors (1st)</a> &mdash; where this '
        "chapter's title image, the warrior, becomes the subject rather than a fortress.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.72 — Dutiyacetovimuttiphalasutta
# --------------------------------------------------------------------------- #
page(
    72, "Dutiyacetovimuttiphala", "Freedom of Heart is the Fruit (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 5.72 — Freedom of Heart is the Fruit (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyacetovimuttiphalasutta, AN 5.71's twin — a different, progressive five-step "
        "perception chain reaching the identical fortress epithets, with the repeated "
        "explanation left elided in the source itself. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "a progressive five-step perception chain, followed by the same five fortress "
                 "epithets as AN 5.71; the source elides their repeated explanation as identical"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short, and the hardest part "
                       "already unpacked at AN 5.71"),
    ],
    why=(
        "AN 5.71's twin keeps the identical twofold fruit and the identical five fortress "
        "epithets, but replaces the opening five-topic list with a genuinely different, "
        "progressive chain: perceiving impermanence, then the suffering inherent in "
        "impermanence, then the not-self inherent in that suffering, then giving up, then "
        "fading away. Two different routes into the same standing-open fortress."),
    guide=[
        ("A chain, not a list", [
            "AN 5.71's five practices were five separate topics observed side by side. This "
            "discourse's five are a single deepening sequence, each step building on the "
            "realization of the one before it: impermanence noticed first, then the suffering "
            "bound up in anything impermanent, then the absence of any self within that "
            "suffering, then a resulting willingness to give up, and finally the fading away of "
            "what has been given up."]),
        ("Same fruit, same fortress", [
            "The twofold fruit &mdash; freedom of heart and freedom by wisdom &mdash; and all "
            "five fortress epithets &mdash; cross-bar lifted, moat filled in, pillar pulled up, "
            "unimpeded, banner lowered and burden dropped &mdash; are worded identically to AN "
            "5.71, down to the last phrase."]),
        ("Why the explanation is left blank", [
            "In the source, only the opening list and the naming of the five epithets are "
            "translated in full; the explanation of each epithet, spelled out in AN 5.71, is "
            "represented here only by an ellipsis, since it is word-for-word the same "
            "explanation already given. This reading guide follows the source exactly: nothing "
            "has been invented or expanded to fill the gap, and the full explanation can be "
            "read at AN 5.71."]),
        ("Two routes, one destination", [
            "Read as a pair, AN 5.71 and 5.72 make a structural point: the same liberating "
            "outcome, described with the same striking fortress image, can be reached either "
            "by observing several distinct facts about experience side by side, or by following "
            "a single chain of realization from one insight into the next."]),
        ("A familiar shape", [
            "The progressive linking of one perception into the next &mdash; each step both "
            "completing and motivating the next &mdash; echoes the structure of other chained "
            "formulas already seen in this nipāta, such as the sequence from joy through "
            "tranquility to immersion. This particular five-step perception chain (impermanence, "
            "suffering, not-self, giving up, fading away) is itself a well-known formula found "
            "widely elsewhere in the early canon."]),
        ("What comes next", [
            "AN 5.73 turns the chapter toward a different question entirely &mdash; what it "
            "means to &lsquo;live by the teaching&rsquo; &mdash; before AN 5.75 finally reaches "
            "the chapter's title image, the warrior."]),
    ],
    terms=[
        ("aniccasaññā",
         "&ldquo;perception of impermanence&rdquo; &mdash; the first step of this discourse's "
         "chain."),
        ("dukkhasaññā (anicce)",
         "&ldquo;perception of suffering in the impermanent&rdquo; &mdash; the second step, "
         "built on the first."),
        ("anattasaññā (dukkhe)",
         "&ldquo;perception of not-self in what is suffering&rdquo; &mdash; the third step."),
        ("pahānasaññā",
         "&ldquo;perception of giving up&rdquo; &mdash; the fourth step."),
        ("virāgasaññā",
         "&ldquo;perception of fading away&rdquo; &mdash; the fifth and final step of this "
         "discourse's chain."),
    ],
    text_intro=(
        "The discourse in full. The source leaves the explanation of the five fortress epithets "
        "untranslated here, as identical to AN 5.71's; only the opening chain and the naming of "
        "the epithets carry translated English text, and this page follows the source exactly. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The second five, and their fruit"),
        ("p", "&sect;1", "an5.72:1.1-1.6"),
    ],
    quiz=[
        {"q": "What are the five items of this discourse's perception chain, in order?",
         "opts": [
             "Ugliness, food, dissatisfaction, impermanence, death",
             "Impermanence, suffering-in-impermanence, not-self-in-suffering, giving up, fading away",
             "Faith, conscience, prudence, energy, wisdom",
             "Cross-bar, moat, pillar, unimpeded, banner"],
         "correct": 1,
         "expl": "A progressive chain, each step built on the one before."},
        {"q": "Is this the same five items as AN 5.71's opening list?",
         "opts": [
             "Yes, identical",
             "No, an entirely different five items",
             "Three of the five overlap",
             "Only the order differs"],
         "correct": 1,
         "expl": "AN 5.71 used a five-topic list; this discourse uses a progressive chain instead."},
        {"q": "What twofold fruit is named, matching AN 5.71?",
         "opts": [
             "Wealth and status",
             "Freedom of heart and freedom by wisdom",
             "Long life",
             "Rebirth in a heavenly realm"],
         "correct": 1,
         "expl": "Cetovimutti and paññāvimutti, worded identically to AN 5.71."},
        {"q": "Are the five fortress epithets (cross-bar, moat, pillar, unimpeded, banner) the same as AN 5.71's?",
         "opts": [
             "No, entirely different epithets",
             "Yes, identical, down to the last phrase",
             "Only two of the five match",
             "The order is reversed"],
         "correct": 1,
         "expl": "Worded identically to AN 5.71."},
        {"q": "Why does the source leave the explanation of the five epithets untranslated here?",
         "opts": [
             "The manuscript is damaged at this point",
             "Because it is word-for-word the same explanation already given at AN 5.71",
             "The translator considered it unimportant",
             "It was never composed"],
         "correct": 1,
         "expl": "Elided in the source itself, not omitted by this reading guide."},
        {"q": "What is virāgasaññā, the fifth item in this chain?",
         "opts": [
             "Perception of impermanence",
             "Perception of not-self",
             "Perception of fading away",
             "Perception of giving up"],
         "correct": 2,
         "expl": "The final step, following pahānasaññā, perception of giving up."},
        {"q": "Is anattasaññā, in this discourse, perceived within the impermanent or within suffering?",
         "opts": [
             "Within the impermanent",
             "Within suffering",
             "Within both equally",
             "Within neither; it stands alone"],
         "correct": 1,
         "expl": "Dukkhe anattasaññā — not-self perceived within what is suffering, the third link in the chain."},
        {"q": "What makes this list 'progressive' rather than a five-topic list like AN 5.71's?",
         "opts": [
             "It is longer",
             "Each item builds on the deepening realization of the one before it",
             "It uses different vocabulary only",
             "It is addressed to a different audience"],
         "correct": 1,
         "expl": "A chain of linked insight, not five separate observations."},
        {"q": "What chapter do both this discourse and AN 5.71 belong to?",
         "opts": [
             "Nīvaraṇavagga",
             "Saññāvagga",
             "Yodhājīvavagga, the Warriors",
             "Sekhabalavagga"],
         "correct": 2,
         "expl": "The chapter this discourse pair opens."},
        {"q": "Which discourse reaches this chapter's title image, the warrior, directly?",
         "opts": [
             "AN 5.73",
             "AN 5.74",
             "AN 5.75",
             "AN 5.80"],
         "correct": 2,
         "expl": "The chapter's eponymous discourse, three places further on."},
    ],
    marginalia=[
        ("Same fruit, same epithets", [
            "worded identically",
            "to AN 5.71",
        ]),
        ("A chain, not a list", [
            "impermanence &rarr; suffering",
            "&rarr; not-self &rarr; giving up",
            "&rarr; fading away",
        ]),
        ("Term", [
            "<span class=\"pali\">virāgasaññā</span>",
            "&mdash; perception",
            "of fading away",
        ]),
        ("Cross-references", [
            "AN 5.71 &middot; the fortress epithets, explained in full",
            "AN 5.75 &middot; next: the chapter's title discourse",
        ]),
    ],
    further=[
        '<a href="%s/an5.72/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.71.html">AN 5.71 &middot; Freedom of Heart is the Fruit (1st)</a> '
        "&mdash; this discourse's twin, where the five fortress epithets are explained in full.",
        '<a href="an-5.69.html">AN 5.69 &middot; Disillusionment</a> &mdash; an earlier, '
        "related perception list from the previous chapter.",
        '<a href="an-5.75.html">AN 5.75 &middot; Warriors (1st)</a> &mdash; next: the '
        "chapter&rsquo;s title discourse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.73 — Paṭhamadhammavihārīsutta
# --------------------------------------------------------------------------- #
page(
    73, "Paṭhamadhammavihārī", "One Who Lives by the Teaching (1st)",
    vagga=VAGGA_8,
    meta_title="AN 5.73 — One Who Lives by the Teaching (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamadhammavihārīsutta — a mendicant asks what 'living by the teaching' means; four "
        "candidates who study, teach, recite, or think too much are set against the one who "
        "does the same without neglecting retreat, closing with the Buddha's own exhortation "
        "to practice absorption. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", "An unnamed mendicant, questioning the Buddha; the Buddha's answer"),
        ("Form", "question and definition — four rejected candidates for a term, then the true "
                 "definition, closing with a direct exhortation"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a practical distinction "
                       "about balancing study with practice"),
    ],
    why=(
        "A mendicant asks the Buddha to define a term already in circulation: "
        "&lsquo;dhammavihārī&rsquo;, one who lives by the teaching. The answer turns out to "
        "hinge not on how much scripture someone studies, teaches, recites, or thinks about, "
        "but on whether that activity crowds out retreat and inner serenity. The discourse "
        "closes with one of the collection's most direct exhortations: roots of trees, empty "
        "huts &mdash; practice absorption, don't be negligent, don't regret it later."),
    guide=[
        ("The question", [
            "A mendicant simply asks the Buddha how &lsquo;one who lives by the "
            "teaching&rsquo; is defined &mdash; a term evidently already in use, not one the "
            "Buddha is introducing for the first time."]),
        ("Three who study, teach, and recite too much", [
            "Three parallel false candidates are named in turn: one who studies a lot "
            "(<em>pariyattibahula</em>), spending the whole day memorizing the teaching; one "
            "who advocates a lot (<em>paññattibahula</em>), spending the whole day teaching it "
            "to others; and one who rehearses a lot (<em>sajjhāyabahula</em>), spending the "
            "whole day reciting it. Each is said to neglect retreat and fail to commit to "
            "internal serenity of heart &mdash; and each, despite the activity's evident "
            "value, is denied the title dhammavihārī."]),
        ("One who thinks too much", [
            "A fourth candidate, one who thinks a lot (<em>vitakkabahula</em>), spends the "
            "whole day turning the teaching over mentally &mdash; considering, examining, "
            "reflecting on it &mdash; with the identical diagnosis: retreat neglected, "
            "serenity uncultivated."]),
        ("The one who truly lives by the teaching", [
            "The true dhammavihārī performs the identical activity as the first false "
            "candidate &mdash; memorizing the same ninefold body of material: statements, "
            "mixed prose and verse, discussions, verses, inspired exclamations, legends, "
            "stories of past lives, amazing stories, and elaborations (<em>vedalla</em>) "
            "&mdash; but does not neglect retreat, and is committed to internal serenity. The "
            "deciding difference is never the activity itself, only whether it crowds out "
            "retreat and serenity."]),
        ("The Buddha's instruction", [
            "The discourse closes with the Buddha naming what he has done for this mendicant "
            "&mdash; what a sympathetic teacher who wants the best for disciples should do "
            "&mdash; and issuing a direct exhortation: here are roots of trees, here are empty "
            "huts; practice absorption, don't be negligent, don't regret it later."]),
        ("A pair to come", [
            "AN 5.74 restates this entire structure with a sharper, different diagnostic axis: "
            "not whether retreat is neglected, but whether the deeper meaning of what is "
            "memorized is actually understood."]),
    ],
    terms=[
        ("dhammavihārī",
         "&ldquo;one who lives by the teaching&rdquo; &mdash; the term this discourse defines."),
        ("pariyattibahula",
         "&ldquo;one who studies a lot&rdquo; &mdash; the first false candidate, denied the "
         "title dhammavihārī for neglecting retreat."),
        ("paṭisallāna",
         "&ldquo;retreat, withdrawal into seclusion&rdquo; &mdash; what each false candidate "
         "is said to neglect."),
        ("ajjhattaṁ cetosamatha",
         "&ldquo;internal serenity of heart&rdquo; &mdash; what each false candidate fails to "
         "cultivate."),
        ("vedalla",
         "&ldquo;elaborations&rdquo; &mdash; one of nine genres named here in a neutral "
         "listing; the same term reappears at AN 5.79 in a strikingly different, cautionary "
         "context."),
    ],
    text_intro=(
        "The discourse in full: the question, four rejected candidates, the true definition, "
        "and the Buddha's closing exhortation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The question"),
        ("p", "&sect;1", "an5.73:1.1-1.3"),
        ("h3", "Three who study, teach, and recite too much"),
        ("p", "&sect;2", "an5.73:2.1-2.4"),
        ("p", "&sect;3", "an5.73:3.1-3.3"),
        ("p", "&sect;4", "an5.73:4.1-4.3"),
        ("h3", "One who thinks too much"),
        ("p", "&sect;5", "an5.73:5.1-5.3"),
        ("h3", "The one who truly lives by the teaching"),
        ("p", "&sect;6", "an5.73:6.1-6.4"),
        ("h3", "The Buddha's instruction"),
        ("p", "&sect;7", "an5.73:7.1-7.3"),
    ],
    quiz=[
        {"q": "What term does the mendicant ask the Buddha to define?",
         "opts": [
             "Arahant",
             "Dhammavihārī, one who lives by the teaching",
             "Sekha",
             "Āraññika"],
         "correct": 1,
         "expl": "The discourse's opening question."},
        {"q": "What is the first false candidate named?",
         "opts": [
             "One who meditates a lot",
             "One who studies a lot",
             "One who travels a lot",
             "One who fasts a lot"],
         "correct": 1,
         "expl": "Pariyattibahula — one who studies a lot."},
        {"q": "What do all four false candidates have in common, structurally?",
         "opts": [
             "Each is accused of laziness",
             "Each spends the whole day on one activity, neglects retreat, and fails to cultivate serenity",
             "Each is said to have broken a precept",
             "Each is praised without qualification"],
         "correct": 1,
         "expl": "An identical diagnosis applied to four different activities."},
        {"q": "What activity does the true dhammavihārī actually perform, compared to the first false candidate?",
         "opts": [
             "A completely different activity",
             "The identical activity — memorizing the teaching",
             "No scriptural activity at all",
             "Only meditation, never study"],
         "correct": 1,
         "expl": "The activity itself is not what distinguishes them."},
        {"q": "What is the deciding difference between the false candidates and the true dhammavihārī?",
         "opts": [
             "How much they have memorized",
             "Whether retreat is neglected and serenity is cultivated alongside the activity",
             "Their seniority in the Saṅgha",
             "Whether they teach in public"],
         "correct": 1,
         "expl": "The discourse's central point."},
        {"q": "How many genres of text are named in the passage describing what a mendicant memorizes?",
         "opts": [
             "Three",
             "Five",
             "Nine",
             "Twelve"],
         "correct": 2,
         "expl": "Statements, mixed prose and verse, discussions, verses, inspired exclamations, legends, past-life stories, amazing stories, and elaborations."},
        {"q": "What does the Buddha say he has done for the questioning mendicant by explaining this?",
         "opts": [
             "Given a formal ordination",
             "What a sympathetic teacher who wants the best for disciples should do",
             "Granted a special title",
             "Nothing beyond ordinary instruction"],
         "correct": 1,
         "expl": "Framed explicitly as a teacher's duty of sympathy toward students."},
        {"q": "What does the Buddha's closing exhortation urge mendicants to do?",
         "opts": [
             "Recite scripture continuously",
             "Practice absorption, and not be negligent",
             "Travel to teach in distant villages",
             "Debate philosophical points"],
         "correct": 1,
         "expl": "Jhāyatha — practice absorption, don't be negligent, don't regret it later."},
        {"q": "Fill in: 'Here are these roots of trees, and here are these ___.'",
         "opts": [
             "Rivers",
             "Empty huts",
             "Mountains",
             "Marketplaces"],
         "correct": 1,
         "expl": "The standard pairing naming secluded places suited to meditation."},
        {"q": "What does the companion discourse AN 5.74 change about this same structure?",
         "opts": [
             "Nothing; it repeats this discourse verbatim",
             "The diagnostic criterion shifts to understanding the higher meaning, not neglecting retreat",
             "It rejects the concept of dhammavihārī entirely",
             "It adds a fifth false candidate"],
         "correct": 1,
         "expl": "A sharper, different axis for the same four-plus-one structure."},
    ],
    marginalia=[
        ("Same act, different outcome", [
            "four false candidates,",
            "one true — identical",
            "activity throughout",
        ]),
        ("Nine genres", [
            "statements &middot; verse",
            "discussions &middot; legends",
            "&hellip; and elaborations",
        ]),
        ("Term", [
            "<span class=\"pali\">vedalla</span>",
            "&mdash; reappears darker",
            "at AN 5.79",
        ]),
        ("Cross-references", [
            "AN 5.74 &middot; same structure, sharper criterion",
            "AN 5.79 &middot; vedalla's later, cautionary echo",
        ]),
    ],
    further=[
        '<a href="%s/an5.73/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.74.html">AN 5.74 &middot; One Who Lives by the Teaching (2nd)</a> '
        "&mdash; this discourse's twin, with a sharper diagnostic criterion.",
        '<a href="an-5.79.html">AN 5.79 &middot; Future Perils (3rd)</a> &mdash; where '
        "vedalla, one of the nine genres named here, reappears in a cautionary context.",
        '<a href="an-5.75.html">AN 5.75 &middot; Warriors (1st)</a> &mdash; where this '
        "discourse's closing exhortation to practice absorption is unpacked in full.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.74 — Dutiyadhammavihārīsutta
# --------------------------------------------------------------------------- #
page(
    74, "Dutiyadhammavihārī", "One Who Lives by the Teaching (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 5.74 — One Who Lives by the Teaching (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyadhammavihārīsutta, AN 5.73's twin — the same four candidates and the same "
        "activity, now distinguished by a single different criterion: understanding the "
        "higher meaning of what is memorized. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", "An unnamed mendicant, questioning the Buddha; the Buddha's answer"),
        ("Form", "the same question-and-definition structure as AN 5.73, with one criterion "
                 "changed throughout"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a single clear change of "
                       "criterion, easy to follow once AN 5.73 is read"),
    ],
    why=(
        "AN 5.73's twin keeps the same question, the same four candidates, and the same "
        "closing exhortation, but replaces the diagnosis entirely: instead of neglecting "
        "retreat, the false candidates here simply fail to understand the higher meaning "
        "(<em>uttari&hellip;attha</em>) of what they study, teach, recite, or think about. Two "
        "independent ways to fail at living by the teaching, from two discourses that otherwise "
        "share a single frame."),
    guide=[
        ("The question, again", [
            "The same mendicant, or one like him, asks the same question in the same words: "
            "how is one who lives by the teaching defined?"]),
        ("Four who fail to grasp the higher meaning", [
            "The same four false candidates recur &mdash; one who studies a lot, advocates a "
            "lot, rehearses a lot, and thinks a lot &mdash; but this time none of them is "
            "accused of neglecting retreat. The sole diagnosis given for each is that they do "
            "not understand the higher meaning (<em>uttari cassa paññāya atthaṁ "
            "nappajānāti</em>) of what they are doing."]),
        ("The one who understands", [
            "The true dhammavihārī performs the same activity &mdash; memorizing the identical "
            "ninefold body of material &mdash; but does understand the higher meaning. As in "
            "AN 5.73, the activity itself never distinguishes the false candidates from the "
            "true one; only the single stated criterion does."]),
        ("Two ways to fail", [
            "Read together, AN 5.73 and 5.74 establish that living by the teaching can be "
            "undermined in at least two independent ways: by letting study, teaching, "
            "recitation, or thought crowd out retreat and serenity, or by remaining at the "
            "surface of what is memorized without grasping its deeper import. Either failure "
            "earns the same verdict &mdash; not a dhammavihārī."]),
        ("What 'the higher meaning' is left undefined", [
            "The discourse does not spell out what this higher meaning consists of; this "
            "reading guide does not supply a definition the text itself withholds. What is "
            "clear is only that memorizing correct words is, on its own, insufficient."]),
        ("The same closing exhortation", [
            "As at AN 5.73, the discourse closes with the identical instruction: roots of "
            "trees, empty huts, practice absorption, don't be negligent, don't regret it "
            "later &mdash; framed once more as what a sympathetic teacher owes students."]),
    ],
    terms=[
        ("uttari&hellip;attha",
         "&ldquo;the higher meaning&rdquo; &mdash; the single criterion distinguishing this "
         "discourse's false candidates from the true dhammavihārī, left otherwise undefined."),
        ("pariyattibahula",
         "&ldquo;one who studies a lot&rdquo; &mdash; the first candidate, here failing on "
         "understanding rather than neglecting retreat."),
        ("paññattibahula",
         "&ldquo;one who advocates a lot&rdquo; &mdash; the second candidate."),
        ("sajjhāyabahula",
         "&ldquo;one who rehearses a lot&rdquo; &mdash; the third candidate."),
        ("vitakkabahula",
         "&ldquo;one who thinks a lot&rdquo; &mdash; the fourth candidate."),
    ],
    text_intro=(
        "The discourse in full, restating AN 5.73's structure with one criterion changed "
        "throughout. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The question, again"),
        ("p", "&sect;1", "an5.74:1.1-1.3"),
        ("h3", "Four who fail to grasp the higher meaning"),
        ("p", "&sect;2", "an5.74:2.1-2.4"),
        ("p", "&sect;3", "an5.74:3.1-3.2"),
        ("p", "&sect;4", "an5.74:4.1-4.2"),
        ("p", "&sect;5", "an5.74:5.1-5.2"),
        ("h3", "The one who understands"),
        ("p", "&sect;6", "an5.74:6.1-6.4"),
        ("h3", "The Buddha's instruction, repeated"),
        ("p", "&sect;7", "an5.74:7.1-7.3"),
    ],
    quiz=[
        {"q": "What single criterion distinguishes the false candidates from the true dhammavihārī in this discourse?",
         "opts": [
             "Whether they neglect retreat",
             "Whether they understand the higher meaning",
             "Whether they are senior mendicants",
             "Whether they live in a wilderness"],
         "correct": 1,
         "expl": "Uttari…attha, unlike AN 5.73's retreat-neglect criterion."},
        {"q": "Unlike AN 5.73, does this version mention neglecting retreat as part of the diagnosis?",
         "opts": [
             "Yes, identically",
             "No",
             "Only for the fourth candidate",
             "Only for the true dhammavihārī"],
         "correct": 1,
         "expl": "The retreat-and-serenity language from AN 5.73 is entirely absent here."},
        {"q": "What is the term for 'the higher meaning', left undefined by the text?",
         "opts": [
             "Uttari…attha",
             "Paṭisallāna",
             "Ajjhattaṁ cetosamatha",
             "Vedalla"],
         "correct": 0,
         "expl": "Named but not further explained in this discourse."},
        {"q": "Which of the four false-candidate terms names one who advocates or teaches a lot?",
         "opts": [
             "Pariyattibahula",
             "Paññattibahula",
             "Sajjhāyabahula",
             "Vitakkabahula"],
         "correct": 1,
         "expl": "Paññattibahula — the second candidate."},
        {"q": "Which term names one who rehearses or recites a lot?",
         "opts": [
             "Pariyattibahula",
             "Paññattibahula",
             "Sajjhāyabahula",
             "Vitakkabahula"],
         "correct": 2,
         "expl": "Sajjhāyabahula — the third candidate."},
        {"q": "Which term names one who merely thinks a lot?",
         "opts": [
             "Pariyattibahula",
             "Paññattibahula",
             "Sajjhāyabahula",
             "Vitakkabahula"],
         "correct": 3,
         "expl": "Vitakkabahula — the fourth candidate."},
        {"q": "Is the activity performed by the true dhammavihārī here different from the false candidates'?",
         "opts": [
             "Yes, an entirely different activity",
             "No, identical activity throughout",
             "Only partly different",
             "The text does not say"],
         "correct": 1,
         "expl": "As at AN 5.73, only the stated criterion distinguishes them."},
        {"q": "What do AN 5.73 and AN 5.74 together establish about failing to live by the teaching?",
         "opts": [
             "That it is impossible to fail",
             "That there are at least two independent ways to fail — crowding out retreat, or missing the deeper meaning",
             "That only senior mendicants can fail",
             "That failure is defined only by breaking a precept"],
         "correct": 1,
         "expl": "Two discourses, two independent diagnostic criteria, same underlying question."},
        {"q": "What closing exhortation is repeated verbatim from AN 5.73?",
         "opts": [
             "A call to travel and teach widely",
             "Roots of trees, empty huts — practice absorption, don't be negligent",
             "A warning about monastic discipline",
             "An instruction to fast"],
         "correct": 1,
         "expl": "Identical wording to AN 5.73's close."},
        {"q": "What is the title of the chapter both discourses belong to?",
         "opts": [
             "Nīvaraṇavagga",
             "Saññāvagga",
             "Yodhājīvavagga, the Warriors",
             "Sekhabalavagga"],
         "correct": 2,
         "expl": "The chapter this pair sits within, before it reaches its title discourse at AN 5.75."},
    ],
    marginalia=[
        ("Same four, new criterion", [
            "not retreat-neglect,",
            "but understanding",
        ]),
        ("Two ways to fail", [
            "AN 5.73 &middot; retreat crowded out",
            "AN 5.74 &middot; meaning missed",
        ]),
        ("Term", [
            "<span class=\"pali\">uttari&hellip;attha</span>",
            "&mdash; the higher",
            "meaning, undefined",
        ]),
        ("Cross-references", [
            "AN 5.73 &middot; this discourse's twin",
            "AN 5.75&ndash;76 &middot; next: the chapter's warriors",
        ]),
    ],
    further=[
        '<a href="%s/an5.74/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.73.html">AN 5.73 &middot; One Who Lives by the Teaching (1st)</a> '
        "&mdash; this discourse's twin, criterion of retreat rather than meaning.",
        '<a href="an-5.75.html">AN 5.75 &middot; Warriors (1st)</a> &mdash; next: the '
        "chapter&rsquo;s title discourse.",
        '<a href="an-5.76.html">AN 5.76 &middot; Warriors (2nd)</a> &mdash; and its companion, '
        "immediately following.",
    ],
)

# --------------------------------------------------------------------------- #
# AN 5.75 — Paṭhamayodhājīvasutta
# --------------------------------------------------------------------------- #
page(
    75, "Paṭhamayodhājīva", "Warriors (1st)",
    vagga=VAGGA_8,
    meta_title="AN 5.75 — Warriors (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamayodhājīvasutta, this chapter's title discourse — five levels of a soldier's "
        "battlefield resilience mapped onto five levels of a monk's ability to withstand "
        "escalating temptation, closing with the fifth monk's full path to liberation. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "an extended graded simile — five kinds of warriors, then five kinds of monks "
                 "mapped onto them stage by stage, each explained by a short glossary exchange"),
        ("Length", "~7 minutes to read — the chapter's longest discourse so far"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; describes escalating sexual "
                       "temptation from an anxious, one-sided monastic vantage point; handled "
                       "here plainly, without endorsement"),
    ],
    why=(
        "This is the chapter's eponymous discourse, and it earns the title directly: five "
        "warriors, graded by how far into battle each one holds firm, mapped onto five monks, "
        "graded by how far into an escalating encounter with a woman each one holds firm. "
        "Stated plainly: this maps a soldier's resilience onto a monk's resistance to a "
        "specific kind of encounter, addressed to a celibate male monastic audience anxious "
        "about exactly that encounter &mdash; not a universal claim about women or about "
        "desire in general. The fifth monk, who holds firm throughout, goes on to complete "
        "liberation by the collection's standard formula."),
    guide=[
        ("The five warriors, restated", [
            "Literal warriors first: one falters merely at the sight of a dust cloud; one "
            "prevails there but falters at a banner's crest; one prevails past both but "
            "falters at the noise of turmoil; one prevails past all three but is killed or "
            "wounded when blows are actually struck; one prevails through the whole battle and "
            "wins outright, standing as foremost in the field."]),
        ("Five thresholds, mapped onto five monks", [
            "The first monk disrobes on merely hearing that an attractive woman lives in some "
            "village &mdash; his &lsquo;dust cloud&rsquo;. The second withstands hearsay but "
            "disrobes upon actually seeing her &mdash; his &lsquo;banner's crest&rsquo;. The "
            "third withstands seeing her but falters when she approaches and smiles, chats, "
            "laughs, and teases him &mdash; his &lsquo;turmoil&rsquo;. The fourth withstands "
            "all of that, but when she sits close, lies down near him, or embraces him, he has "
            "sex without even formally disrobing first &mdash; his &lsquo;blows struck&rsquo;. "
            "The fifth withstands that same physical approach, disentangles himself, and walks "
            "away &mdash; his &lsquo;victory&rsquo;."]),
        ("Naming the frame plainly", [
            "This reading guide states directly what the discourse is doing and for whom: it "
            "is addressed to celibate male monastics, treats a woman's approach as the "
            "advancing force to be resisted, and gives the woman herself no voice or interior "
            "life of her own &mdash; she exists in the account only as an occasion for the "
            "monk's own struggle. This is reported as what the text says and who it is "
            "addressed to, not endorsed as a description of women or of desire generally."]),
        ("What survives independently", [
            "One observation here is genuinely transferable beyond its specific historical "
            "framing: resilience against temptation is not a single yes-or-no trait. A person "
            "can hold firm against a distant, abstract version of a difficulty and still "
            "falter against a closer, more immediate one &mdash; failure and success can each "
            "occur at different thresholds within the same person, tested one at a time."]),
        ("The fifth monk's victory, unpacked", [
            "The discourse doesn't leave &lsquo;victory&rsquo; unexplained: the fifth monk "
            "withdraws to a secluded lodging, sits cross-legged, gives up the five hindrances, "
            "passes through the four absorptions, and applies the four noble truths to both "
            "suffering and defilement, arriving at the ending of defilements "
            "(<em>āsavakkhaya</em>) and the standard declaration that rebirth is ended. This "
            "full formula recurs at many points across this nipāta and is not re-explained "
            "here in full."]),
        ("A companion to come", [
            "AN 5.76 immediately follows with the same five-stage structure, but reframes it "
            "entirely: not escalating thresholds of temptation, but a single already-arisen "
            "crisis, tracked through five different outcomes depending on how the community "
            "responds."]),
    ],
    terms=[
        ("rajagga",
         "&ldquo;cloud of dust&rdquo; &mdash; the first, faintest threshold in the warrior "
         "simile, mapped onto mere rumor."),
        ("sikkhādubbalya",
         "&ldquo;declaring inability to continue training&rdquo; &mdash; the formal act of "
         "disrobing, named at each threshold where a monk falters."),
        ("nīvaraṇa",
         "the five hindrances, given up by the fifth monk before entering the four absorptions."),
        ("āsavakkhaya",
         "&ldquo;ending of defilements&rdquo; &mdash; the outcome of the fifth monk's full "
         "realization, closing the discourse."),
        ("saṅgāmasīsa",
         "&ldquo;foremost in battle&rdquo; &mdash; the victor's standing after the fight, "
         "mapped onto the fifth monk's liberation."),
    ],
    text_intro=(
        "The discourse in full: five literal warriors, then five monks mapped onto them stage "
        "by stage, closing with the fifth monk's full path to liberation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five warriors"),
        ("p", "&sect;1", "an5.75:1.1-1.5"),
        ("p", "&sect;2", "an5.75:2.1-2.4"),
        ("p", "&sect;3", "an5.75:3.1-3.4"),
        ("p", "&sect;4", "an5.75:4.1-4.4"),
        ("p", "&sect;5", "an5.75:5.1-5.5"),
        ("h3", "Five monks, mapped"),
        ("p", "&sect;6", "an5.75:6.1-6.2"),
        ("h3", "The first: falters at rumor"),
        ("p", "&sect;7", "an5.75:6.3-6.10"),
        ("p", "&sect;8", "an5.75:7.1-7.4"),
        ("h3", "The second: falters at the sight of her"),
        ("p", "&sect;9", "an5.75:8.1-8.10"),
        ("p", "&sect;10", "an5.75:9.1-9.5"),
        ("h3", "The third: falters when she approaches"),
        ("p", "&sect;11", "an5.75:10.1-10.8"),
        ("p", "&sect;12", "an5.75:11.1-11.5"),
        ("h3", "The fourth: overcome at her touch"),
        ("p", "&sect;13", "an5.75:12.1-12.6"),
        ("p", "&sect;14", "an5.75:13.1-13.4"),
        ("h3", "The fifth: victory"),
        ("p", "&sect;15", "an5.75:14.1-14.5"),
        ("h3", "What victory looks like"),
        ("p", "&sect;16", "an5.75:15.1-15.9"),
        ("h3", "The realization"),
        ("p", "&sect;17", "an5.75:16.1-16.7"),
        ("p", "&sect;18", "an5.75:17.1-17.5"),
    ],
    quiz=[
        {"q": "What five thresholds do the literal warriors falter at, from faintest to most severe?",
         "opts": [
             "Dust cloud, banner's crest, turmoil, being struck, or none (victory)",
             "Rain, wind, fire, flood, earthquake",
             "Morning, noon, evening, night, dawn",
             "Hunger, thirst, fatigue, cold, heat"],
         "correct": 0,
         "expl": "The five graded battlefield thresholds this discourse maps onto five monks."},
        {"q": "What is the monk's equivalent of 'faltering at the mere sight of a cloud of dust'?",
         "opts": [
             "Disrobing after actually meeting a woman",
             "Disrobing on merely hearing a rumor of an attractive woman",
             "Disrobing due to illness",
             "Disrobing after years of practice"],
         "correct": 1,
         "expl": "The faintest, most distant threshold — hearsay alone."},
        {"q": "What is the monk's equivalent of 'faltering at the banner's crest'?",
         "opts": [
             "Disrobing upon actually seeing her",
             "Disrobing on hearsay alone",
             "Disrobing after she speaks to him",
             "Disrobing after physical contact"],
         "correct": 0,
         "expl": "The second threshold — direct sight, one step closer than rumor."},
        {"q": "What is the monk's equivalent of 'faltering at turmoil'?",
         "opts": [
             "Disrobing when she smiles, chats, laughs, and teases him",
             "Disrobing on hearsay alone",
             "Disrobing after physical contact",
             "Disrobing due to a Saṅgha dispute"],
         "correct": 0,
         "expl": "The third threshold — active approach and address, not just sight."},
        {"q": "What happens to the fourth type of monk, distinct from the first three?",
         "opts": [
             "He successfully withstands the encounter",
             "He has sex without formally disrobing first, when she sits close or embraces him",
             "He reports the incident to the Saṅgha",
             "He leaves the monastic life quietly beforehand"],
         "correct": 1,
         "expl": "The fourth threshold — physical proximity — where this monk is 'struck down'."},
        {"q": "What does the fifth, victorious monk do differently at that same physical threshold?",
         "opts": [
             "He also has sex, but formally disrobes first",
             "He disentangles himself and leaves",
             "He calls for help from other monks",
             "He argues with her"],
         "correct": 1,
         "expl": "The one who holds firm through every threshold, including this final one."},
        {"q": "Who is the addressed audience of this discourse's central image, according to the reading guide?",
         "opts": [
             "All Buddhist lay followers, regardless of gender",
             "Celibate male monastics specifically, not a universal claim about women",
             "Married householders",
             "Kings and their ministers"],
         "correct": 1,
         "expl": "Named explicitly in the guide, rather than left as an unstated assumption."},
        {"q": "What formula follows the fifth monk's 'victory'?",
         "opts": [
             "A description of a monastic feast",
             "The standard hindrances, four absorptions, and four-noble-truths/āsavakkhaya realization sequence",
             "A genealogy of past Buddhas",
             "A set of monastic rules on robes"],
         "correct": 1,
         "expl": "The collection's standard full-liberation formula, applied here to this discourse's fifth case."},
        {"q": "What insight about resilience does the guide say survives independently of this discourse's specific historical framing?",
         "opts": [
             "That resistance can hold at an early threshold yet still fail at a later, closer one",
             "That resistance is either entirely present or entirely absent",
             "That only monks who live in cities can resist temptation",
             "That resistance improves automatically with age"],
         "correct": 0,
         "expl": "A transferable psychological point independent of the discourse's specific scenario."},
        {"q": "What does the companion discourse AN 5.76 change about this same five-stage structure?",
         "opts": [
             "Nothing; it repeats this discourse verbatim",
             "It reframes it around an actual crisis and the community's counseling response, not escalating thresholds",
             "It removes the fifth, victorious case entirely",
             "It applies the structure to nuns instead of monks"],
         "correct": 1,
         "expl": "A single already-arisen crisis, tracked through five outcomes, rather than five graded thresholds."},
    ],
    marginalia=[
        ("Five thresholds, one collapse", [
            "dust &middot; banner",
            "turmoil &middot; blow",
            "&middot; victory",
        ]),
        ("Who this addresses", [
            "a celibate male",
            "monastic audience —",
            "reported, not endorsed",
        ]),
        ("Term", [
            "<span class=\"pali\">saṅgāmasīsa</span>",
            "&mdash; foremost",
            "in battle, victorious",
        ]),
        ("Cross-references", [
            "AN 5.76 &middot; the companion discourse, a crisis instead of thresholds",
            "AN 5.55 &middot; earlier sensitive material, same handling",
        ]),
    ],
    further=[
        '<a href="%s/an5.75/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.76.html">AN 5.76 &middot; Warriors (2nd)</a> &mdash; this '
        "discourse&rsquo;s twin, a crisis tracked through five outcomes instead of five "
        "thresholds.",
        '<a href="an-5.55.html">AN 5.55 &middot; Mother and Son</a> &mdash; an earlier '
        "discourse in this nipāta handled with the same plain, non-endorsing approach.",
        '<a href="an-5.73.html">AN 5.73 &middot; One Who Lives by the Teaching (1st)</a> '
        "&mdash; where the exhortation to practice absorption, unpacked here in full, was "
        "first given.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.76 — Dutiyayodhājīvasutta
# --------------------------------------------------------------------------- #
page(
    76, "Dutiyayodhājīva", "Warriors (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 5.76 — Warriors (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyayodhājīvasutta, AN 5.75's companion — an already-arisen crisis of desire "
        "tracked through five outcomes shaped by the community's response, including the "
        "classic ten similes for the drawbacks of sensual pleasure. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "an extended narrative simile — five wounded-warrior outcomes mapped onto five "
                 "outcomes of a monk's crisis of desire, including a counseling scene"),
        ("Length", "~8 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the same considerations as "
                       "AN 5.75 apply; handled here plainly, without endorsement"),
    ],
    why=(
        "AN 5.75's companion tracks a single already-arisen crisis rather than graded "
        "thresholds: five wounded-warrior outcomes &mdash; killed outright, dying before "
        "reaching help, dying despite care, recovering under care, or emerging undamaged and "
        "victorious &mdash; mapped onto five monks who each encounter the same triggering "
        "sight and are followed to five different endings, shaped by whether and how their "
        "community intervenes. Along the way it introduces the ten classic similes for the "
        "drawbacks of sensual pleasure."),
    guide=[
        ("Five wounded warriors, restated", [
            "One warrior enters battle and is killed outright by his foes. One is wounded, "
            "carried toward his relatives, and dies on the road before reaching them. One "
            "reaches his relatives and is nursed, but dies of the wound anyway. One reaches "
            "them, is nursed, and recovers. One enters the same battle undamaged and wins "
            "outright."]),
        ("The mapping, stage by stage", [
            "A monk who enters a village without guarding his senses, sees a scantily-clad "
            "woman, and has sex immediately &mdash; without even attempting to leave first "
            "&mdash; is &lsquo;killed outright&rsquo;. One who burns with the same desire and "
            "resolves to confess it to his fellow monks, but disrobes on the road before "
            "reaching the monastery, &lsquo;dies before reaching help&rsquo;. One who reaches "
            "the monastery, receives counsel from his companions, but disrobes anyway "
            "&lsquo;dies despite care&rsquo;. One who receives the identical counsel and does "
            "not disrobe &lsquo;recovers&rsquo;. One who practices full sense-restraint from "
            "the very start of his almsround, before any crisis arises at all, is the one who "
            "&lsquo;wins outright&rsquo; and goes on to full liberation."]),
        ("Naming the frame plainly, again", [
            "As at AN 5.75, this reading guide states directly what the account does: it is "
            "addressed to a male monastic audience anxious about desire triggered by an "
            "unnamed woman's appearance, and she is never given a voice or any agency of her "
            "own in the account &mdash; only the monk's struggle is narrated. This is reported "
            "as the text's own framing, not endorsed by this guide as a description of women."]),
        ("The ten similes for sensual pleasure's drawbacks", [
            "The concerned fellow monks' counsel invokes ten stock images, among the most "
            "famous catalogs in the early canon: a skeleton, a scrap of meat, a grass torch, a "
            "pit of glowing coals, a dream, borrowed goods, fruit on a tree, a butcher's block, "
            "swords and spears, and a snake's head. Each image makes the same point in a "
            "different way &mdash; that sensual pleasure's apparent reward is disproportionate "
            "to, or actively conceals, the real danger it carries."]),
        ("The Saṅgha's role", [
            "Unlike AN 5.75, which treats each threshold as a private trial, this discourse "
            "foregrounds the community's collective responsibility: three of the five outcomes "
            "turn specifically on whether a struggling monk reaches his companions and what "
            "they say to him, not on his solitary willpower alone."]),
        ("The same realization, restated", [
            "The fifth monk's story closes with the identical formula as AN 5.75: full "
            "sense-restraint described first, then the five hindrances given up, the four "
            "absorptions, and the four-noble-truths realization ending in "
            "<em>āsavakkhaya</em>. Read together, the two discourses offer two different "
            "diagnostic frames &mdash; thresholds of temptation, and outcomes of an "
            "already-arisen crisis &mdash; converging on the same final formula."]),
    ],
    terms=[
        ("indriyasaṁvara",
         "&ldquo;restraint of the sense faculties&rdquo; &mdash; practiced by the fifth monk "
         "from the very outset, distinguishing him from the other four."),
        ("sabrahmacārī",
         "&ldquo;spiritual companions&rdquo;, fellow monks &mdash; who counsel the struggling "
         "monk in the third and fourth cases."),
        ("kāmānaṁ ādīnava",
         "&ldquo;the drawbacks of sensual pleasures&rdquo; &mdash; the heading under which the "
         "ten similes are spoken."),
        ("aṭṭhikaṅkalūpama",
         "&ldquo;the simile of a skeleton&rdquo; &mdash; the first of the ten images."),
        ("rāga",
         "&ldquo;lust, desire&rdquo; &mdash; named as what &lsquo;infects the mind&rsquo; "
         "(<em>cittaṁ anuddhaṁseti</em>) at the trigger of each of the first four cases."),
    ],
    text_intro=(
        "The discourse in full: five wounded warriors, then five monks tracked through the "
        "same crisis to five different outcomes, including the ten similes for the drawbacks "
        "of sensual pleasure. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five wounded warriors"),
        ("p", "&sect;1", "an5.76:1.1-1.7"),
        ("p", "&sect;2", "an5.76:2.1-2.7"),
        ("p", "&sect;3", "an5.76:3.1-3.8"),
        ("p", "&sect;4", "an5.76:4.1-4.8"),
        ("p", "&sect;5", "an5.76:5.1-5.5"),
        ("h3", "The first: killed outright"),
        ("p", "&sect;6", "an5.76:6.1-6.7"),
        ("p", "&sect;7", "an5.76:7.1-7.2"),
        ("h3", "The second: dies before reaching help"),
        ("p", "&sect;8", "an5.76:8.1-8.10"),
        ("p", "&sect;9", "an5.76:9.1-9.2"),
        ("h3", "The third: counseled, but dies anyway"),
        ("p", "&sect;10", "an5.76:10.1-10.12"),
        ("p", "&sect;11", "an5.76:11.1-11.14"),
        ("p", "&sect;12", "an5.76:12.1-12.4"),
        ("p", "&sect;13", "an5.76:13.1-13.2"),
        ("h3", "The fourth: counseled, and recovers"),
        ("p", "&sect;14", "an5.76:14.1-14.12"),
        ("p", "&sect;15", "an5.76:15.1-15.6"),
        ("p", "&sect;16", "an5.76:16.1-16.3"),
        ("p", "&sect;17", "an5.76:17.1-17.3"),
        ("h3", "The fifth: undamaged, victorious"),
        ("p", "&sect;18", "an5.76:18.1-18.15"),
        ("p", "&sect;19", "an5.76:19.1-19.3"),
        ("p", "&sect;20", "an5.76:20.1-20.4"),
    ],
    quiz=[
        {"q": "What happens to the first type of monk described here, before he even considers leaving?",
         "opts": [
             "He reports his feelings to fellow monks first",
             "He has sex immediately, without attempting to leave or disrobe first",
             "He leaves the village at once",
             "He asks the woman to leave"],
         "correct": 1,
         "expl": "The 'killed outright' case — no intervening step at all."},
        {"q": "What does the second type of monk resolve to do, but fail to complete?",
         "opts": [
             "Resolve to confess to fellow monks, but disrobes before reaching the monastery",
             "Resolve to meditate, and succeeds",
             "Resolve to travel abroad",
             "Resolve to ordain a student"],
         "correct": 0,
         "expl": "The 'dies before reaching help' case."},
        {"q": "What do the third and fourth types of monk have in common?",
         "opts": [
             "Both disrobe immediately without counsel",
             "Both reach the monastery and receive the same counsel from fellow monks",
             "Both are senior mendicants",
             "Both refuse to speak to anyone"],
         "correct": 1,
         "expl": "The two 'reached help' cases, differing only in the outcome after counsel."},
        {"q": "What distinguishes the third from the fourth?",
         "opts": [
             "The third disrobes anyway; the fourth does not",
             "The third is younger",
             "The third lives in a different region",
             "There is no difference between them"],
         "correct": 0,
         "expl": "'Dies despite care' versus 'recovers' — the same counsel, different outcomes."},
        {"q": "What is the first of the ten similes for the drawbacks of sensual pleasure?",
         "opts": [
             "A dream",
             "A skeleton",
             "A snake's head",
             "Borrowed goods"],
         "correct": 1,
         "expl": "Aṭṭhikaṅkalūpama, the first of the ten images in the catalog."},
        {"q": "Which of these is one of the ten similes named in this discourse?",
         "opts": [
             "A pit of glowing coals",
             "A river in flood",
             "A burning house",
             "A collapsing bridge"],
         "correct": 0,
         "expl": "One of the ten: skeleton, meat scrap, grass torch, coal pit, dream, borrowed goods, tree fruit, butcher's block, swords and spears, snake's head."},
        {"q": "What does the fifth type of monk do differently from the start, unlike the other four?",
         "opts": [
             "He avoids villages entirely for his whole life",
             "He practices full sense-restraint on almsround from the outset",
             "He asks a senior monk to accompany him at all times",
             "He takes an additional vow of silence"],
         "correct": 1,
         "expl": "Restraint practiced before any crisis arises, not applied only after the fact."},
        {"q": "What role does the Saṅgha play in this discourse that is largely absent from AN 5.75?",
         "opts": [
             "Formal disciplinary punishment",
             "Collective counseling of a struggling companion",
             "Public shaming",
             "No role at all — the two discourses are identical in this respect"],
         "correct": 1,
         "expl": "Three of the five outcomes turn on the community's intervention, not solitary willpower alone."},
        {"q": "What formula closes the fifth monk's story, matching AN 5.75?",
         "opts": [
             "A different, shorter formula",
             "The hindrances, four absorptions, and four-noble-truths/āsavakkhaya sequence",
             "A vow of future rebirth as a monk",
             "A description of a monastic ceremony"],
         "correct": 1,
         "expl": "The same standard full-liberation formula as AN 5.75's fifth case."},
        {"q": "How is the unnamed woman in this account treated, structurally, according to the reading guide?",
         "opts": [
             "As a fully developed character with her own stated motivations",
             "As an occasion for the monk's struggle, given no voice or agency of her own",
             "As the discourse's main speaker",
             "As a fellow monastic"],
         "correct": 1,
         "expl": "Named plainly in the guide as a limitation of the text's own framing."},
    ],
    marginalia=[
        ("Five wounds, one crisis", [
            "killed &middot; dies en route",
            "dies despite care",
            "recovers &middot; undamaged",
        ]),
        ("The ten similes", [
            "skeleton &middot; meat scrap",
            "coal pit &middot; dream &middot;",
            "&hellip; snake's head",
        ]),
        ("Term", [
            "<span class=\"pali\">indriyasaṁvara</span>",
            "&mdash; sense-faculty",
            "restraint, from the start",
        ]),
        ("Cross-references", [
            "AN 5.75 &middot; the twin, graded thresholds instead of a single crisis",
            "AN 5.55 &middot; earlier sensitive material, same handling",
        ]),
    ],
    further=[
        '<a href="%s/an5.76/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.75.html">AN 5.75 &middot; Warriors (1st)</a> &mdash; this '
        "discourse's twin, tracking graded thresholds rather than a single crisis.",
        '<a href="an-5.77.html">AN 5.77 &middot; Future Perils (1st)</a> &mdash; next: the '
        "chapter turns from an inner danger to physical dangers of the wilderness.",
        '<a href="an-5.55.html">AN 5.55 &middot; Mother and Son</a> &mdash; an earlier '
        "discourse in this nipāta handled with the same plain, non-endorsing approach.",
    ],
)

# --------------------------------------------------------------------------- #
# AN 5.77 — Paṭhamaanāgatabhayasutta
# --------------------------------------------------------------------------- #
page(
    77, "Paṭhamaanāgatabhaya", "Future Perils (1st)",
    vagga=VAGGA_8,
    meta_title="AN 5.77 — Future Perils (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaanāgatabhayasutta — five physical dangers a wilderness-dwelling mendicant "
        "should reflect on, each turned into motivation for diligent practice now. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "five parallel reflections, each following an identical three-part template"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a straightforward, "
                       "practical set of reflections"),
    ],
    why=(
        "The chapter turns from an inner danger to outer ones: five physical hazards a "
        "wilderness-dwelling mendicant might reasonably face &mdash; venomous bites, accident "
        "or illness, wild animals, criminals, and beings believed to inhabit wild places "
        "&mdash; each turned, by a single repeated template, into a reason to practice now "
        "rather than later."),
    guide=[
        ("One template, five dangers", [
            "Each of the five reflections follows an identical three-part shape: naming a "
            "specific danger, noting that dying from it now would be an obstacle to "
            "unfinished progress, and resolving to rouse energy for attaining what is not yet "
            "attained. The template repeats so exactly that the discourse reads almost like a "
            "checklist for turning mortality-awareness into motivation rather than paralysis."]),
        ("Snakebite", [
            "The first danger is being bitten by a snake, scorpion, or centipede &mdash; a "
            "real and ordinary risk of sleeping and sitting alone in undeveloped wilderness."]),
        ("Accident or illness", [
            "The second names stumbling off a cliff, food poisoning, or a disturbance of bile, "
            "phlegm, or piercing winds &mdash; naming the three humors (<em>pitta</em>, "
            "<em>semha</em>, <em>vāta</em>) of the ancient Indian medical model that frames "
            "illness throughout the early canon."]),
        ("Wild beasts", [
            "The third names five specific animals &mdash; lion, tiger, leopard, bear, hyena "
            "&mdash; real hazards of pre-modern South Asian forest life for anyone sleeping "
            "unprotected in the open."]),
        ("Criminals, and savage non-humans", [
            "The fourth names criminal youths, fleeing a crime or on their way to commit one, "
            "who might take the mendicant's life. The fifth names <em>amanussā</em> &mdash; "
            "non-human beings the discourse describes as savage and life-threatening, part of "
            "the traditional cosmology in which spirits and other non-human beings are "
            "understood to inhabit wild and remote places; this reading guide reports that "
            "belief as the text's own framing without asserting a claim about it either way."]),
        ("A companion that broadens the frame", [
            "AN 5.78 immediately follows with the identical template, but applies it to any "
            "mendicant rather than wilderness-dwellers specifically, replacing physical "
            "dangers with five future changes in life circumstance."]),
    ],
    terms=[
        ("āraññika",
         "&ldquo;wilderness-dweller&rdquo; &mdash; both the practice and the practitioner this "
         "discourse addresses."),
        ("antarāya",
         "&ldquo;obstacle, impediment&rdquo; &mdash; what an untimely death is said to "
         "represent to unfinished progress."),
        ("pitta / semha / vāta",
         "bile, phlegm, and wind &mdash; the three humors of the ancient Indian medical model "
         "named among the second peril's possible causes of illness."),
        ("amanussā",
         "&ldquo;non-human beings&rdquo; &mdash; spirits or other beings the traditional "
         "cosmology holds to inhabit wild and remote places, named as the fifth peril."),
        ("appamatta",
         "&ldquo;diligent, heedful&rdquo; &mdash; the disposition these five reflections are "
         "meant to produce."),
    ],
    text_intro=(
        "The discourse in full: five physical perils, each turned by an identical template "
        "into motivation for present practice. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five future perils"),
        ("p", "&sect;1", "an5.77:1.1"),
        ("h3", "Snakebite"),
        ("p", "&sect;2", "an5.77:2.1-2.8"),
        ("h3", "Accident or illness"),
        ("p", "&sect;3", "an5.77:3.1-3.7"),
        ("h3", "Wild beasts"),
        ("p", "&sect;4", "an5.77:4.1-4.7"),
        ("h3", "Criminals"),
        ("p", "&sect;5", "an5.77:5.1-5.7"),
        ("h3", "Savage non-humans"),
        ("p", "&sect;6", "an5.77:6.1-6.6"),
        ("h3", "The close"),
        ("p", "&sect;7", "an5.77:7.1"),
    ],
    quiz=[
        {"q": "Who specifically is this discourse's set of reflections addressed to?",
         "opts": [
             "Any mendicant, anywhere",
             "A wilderness-dwelling mendicant",
             "Lay followers only",
             "Senior mendicants exclusively"],
         "correct": 1,
         "expl": "Āraññika bhikkhu, named at the very opening."},
        {"q": "What is the first peril named?",
         "opts": [
             "Fire",
             "Snake, scorpion, or centipede bite",
             "Drowning",
             "Starvation"],
         "correct": 1,
         "expl": "The first of the five physical dangers."},
        {"q": "What three bodily humors are named among the potential causes of illness in the second peril?",
         "opts": [
             "Blood, sweat, and tears",
             "Bile, phlegm, and wind",
             "Heat, cold, and moisture",
             "Earth, water, and fire"],
         "correct": 1,
         "expl": "Pitta, semha, vāta — the ancient Indian medical model's three humors."},
        {"q": "Which five wild animals are named in the third peril?",
         "opts": [
             "Elephant, buffalo, boar, wolf, jackal",
             "Lion, tiger, leopard, bear, hyena",
             "Snake, scorpion, spider, centipede, wasp",
             "Crocodile, shark, eel, ray, octopus"],
         "correct": 1,
         "expl": "The five predators named in the third peril."},
        {"q": "Who is described as the fourth peril?",
         "opts": [
             "Tax collectors",
             "Criminal youths, fleeing a crime or on their way to commit one",
             "Rival ascetics",
             "Foreign soldiers"],
         "correct": 1,
         "expl": "A human, rather than animal, danger."},
        {"q": "What does the Pali term 'amanussā' refer to in the fifth peril?",
         "opts": [
             "Foreign travelers",
             "Non-human beings or spirits believed to inhabit the wilderness",
             "Escaped livestock",
             "Rival monastic orders"],
         "correct": 1,
         "expl": "Part of the traditional cosmology framing wild places as inhabited by non-human beings."},
        {"q": "What three-part structure does each of the five reflections share?",
         "opts": [
             "Naming the danger, noting death from it would be an obstacle, resolving to rouse energy now",
             "A story, a moral, and a blessing",
             "A question, an answer, and a verse",
             "A greeting, a teaching, and a farewell"],
         "correct": 0,
         "expl": "The identical template repeated across all five perils."},
        {"q": "What is the stated purpose of contemplating these five perils?",
         "opts": [
             "To induce fear and withdrawal from practice",
             "To spur diligent, keen, resolute meditation toward what is unattained",
             "To justify leaving the wilderness permanently",
             "To determine who should be ordained"],
         "correct": 1,
         "expl": "Motivation, not paralysis, is the discourse's explicit aim."},
        {"q": "Is this discourse about dangers that have already occurred, or ones that might occur?",
         "opts": [
             "Dangers already suffered by the speaker",
             "Dangers that might occur, used as present motivation",
             "Dangers from a past life",
             "Purely hypothetical dangers with no bearing on practice"],
         "correct": 1,
         "expl": "Future, possible dangers reflected on now."},
        {"q": "How does the companion discourse AN 5.78 broaden this same reflection template?",
         "opts": [
             "It removes the template entirely",
             "It applies the template to any mendicant, replacing physical dangers with future life-changes",
             "It restricts the template to forest-dwellers only",
             "It adds a sixth peril"],
         "correct": 1,
         "expl": "Old age, sickness, famine, unrest, and Saṅgha schism replace the physical dangers."},
    ],
    marginalia=[
        ("One template, five dangers", [
            "name it &middot; note the",
            "obstacle &middot; rouse",
            "energy now",
        ]),
        ("The three humors", [
            "<span class=\"pali\">pitta &middot; semha</span>",
            "<span class=\"pali\">vāta</span>",
            "&mdash; ancient Indian medicine",
        ]),
        ("Term", [
            "<span class=\"pali\">amanussā</span>",
            "&mdash; non-human",
            "beings of the wild",
        ]),
        ("Cross-references", [
            "AN 5.78 &middot; the twin, broadens the template",
            "AN 5.54 &middot; related material on times good and bad for practice",
        ]),
    ],
    further=[
        '<a href="%s/an5.77/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.78.html">AN 5.78 &middot; Future Perils (2nd)</a> &mdash; this '
        "discourse&rsquo;s twin, broadening the same template to any mendicant.",
        '<a href="an-5.54.html">AN 5.54 &middot; Untimely</a> &mdash; earlier, related '
        "material on times good and bad for meditation practice.",
        '<a href="an-5.76.html">AN 5.76 &middot; Warriors (2nd)</a> &mdash; the previous '
        "discourse, on an inner rather than an outer danger.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.78 — Dutiyaanāgatabhayasutta
# --------------------------------------------------------------------------- #
page(
    78, "Dutiyaanāgatabhaya", "Future Perils (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 5.78 — Future Perils (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaanāgatabhayasutta, AN 5.77's twin — the same reflection template applied to any "
        "mendicant, turned toward old age, sickness, famine, unrest, and Saṅgha schism. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "the same five-part reflection template as AN 5.77, applied to any mendicant "
                 "and turned toward future changes in circumstance rather than physical danger"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a straightforward, "
                       "practical set of reflections"),
    ],
    why=(
        "AN 5.77's template, generalized: instead of wilderness-specific physical dangers, "
        "any mendicant is invited to reflect on five future changes &mdash; old age, sickness, "
        "famine, civil unrest, and schism in the Saṅgha &mdash; each used as a spur to "
        "practice now, before circumstance makes practice harder."),
    guide=[
        ("The same template, generalized", [
            "As at AN 5.77, each reflection repeats an identical shape, but the addressee "
            "widens from wilderness-dwellers specifically to any mendicant, and the content "
            "shifts from external threats to predictable changes in one's own life and "
            "community."]),
        ("Old age and sickness", [
            "The first two perils are the ordinary bodily changes every practitioner can "
            "expect: old age, and sickness. Both follow the identical warning &mdash; that "
            "focusing on the Buddha's instructions, and frequenting remote wilderness "
            "lodgings, become harder once either has taken hold."]),
        ("Famine and civil unrest", [
            "The third and fourth perils &mdash; famine and civil unrest &mdash; share a "
            "single consequence: people move toward safety or sustenance and end up living "
            "crowded and cramped together (<em>saṅgaṇikavihāra</em>), which itself becomes an "
            "obstacle to focused practice. This material closely parallels AN 5.54, which "
            "named famine and unrest among its own list of times unfavorable for meditation."]),
        ("Schism in the Saṅgha", [
            "The fifth and gravest peril is schism within the monastic community itself "
            "&mdash; named last, as the deepest disruption to the shared conditions that "
            "otherwise support practice."]),
        ("Motivation, not fear", [
            "As at AN 5.77, each reflection closes not with resignation but with a resolve to "
            "preempt the coming difficulty by practicing now, specifically so that when old "
            "age, sickness, famine, unrest, or schism eventually arrives, one can live "
            "comfortably even so."]),
        ("A third companion to come", [
            "AN 5.79 shifts register entirely, from personal and circumstantial change to "
            "institutional and doctrinal decline &mdash; the corruption of teaching and "
            "training themselves, rather than external or bodily hardship."]),
    ],
    terms=[
        ("jarā",
         "&ldquo;old age&rdquo; &mdash; the first of the five future perils here."),
        ("byādhi",
         "&ldquo;sickness, disease&rdquo; &mdash; the second."),
        ("dubbhikkha",
         "&ldquo;famine, scarcity&rdquo; &mdash; the third."),
        ("saṅgaṇikavihāra",
         "&ldquo;crowded, cramped communal living&rdquo; &mdash; the shared consequence named "
         "for both the famine and civil-unrest perils."),
        ("saṅghabheda",
         "&ldquo;schism in the Saṅgha&rdquo; &mdash; the fifth and gravest peril named here."),
    ],
    text_intro=(
        "The discourse in full: the same reflection template as AN 5.77, applied to any "
        "mendicant and turned toward five future changes in circumstance. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five future perils, generalized"),
        ("p", "&sect;1", "an5.78:1.1-1.2"),
        ("h3", "Old age"),
        ("p", "&sect;2", "an5.78:1.3-1.9"),
        ("h3", "Sickness"),
        ("p", "&sect;3", "an5.78:2.1-2.7"),
        ("h3", "Famine"),
        ("p", "&sect;4", "an5.78:3.1-3.9"),
        ("h3", "Civil unrest"),
        ("p", "&sect;5", "an5.78:4.1-4.9"),
        ("h3", "Schism in the Saṅgha"),
        ("p", "&sect;6", "an5.78:5.1-5.7"),
        ("h3", "The close"),
        ("p", "&sect;7", "an5.78:6.1"),
    ],
    quiz=[
        {"q": "Unlike AN 5.77, who is this discourse's reflection template addressed to?",
         "opts": [
             "Only forest-dwelling mendicants",
             "Any mendicant, not specifically wilderness-dwellers",
             "Only senior mendicants",
             "Only newly ordained mendicants"],
         "correct": 1,
         "expl": "The generalized audience, distinguishing this discourse from AN 5.77."},
        {"q": "What is the first of the five future perils named here?",
         "opts": [
             "Old age",
             "Famine",
             "Schism",
             "Wild animals"],
         "correct": 0,
         "expl": "Jarā — old age, the first peril."},
        {"q": "What consequence do both the famine and civil-unrest perils share?",
         "opts": [
             "Both lead directly to death",
             "Both lead people to move and end up living crowded and cramped together",
             "Both are said to never actually occur",
             "Both are blamed on individual mendicants"],
         "correct": 1,
         "expl": "Saṅgaṇikavihāra — crowded communal living, the shared consequence."},
        {"q": "What is named as the gravest, final peril?",
         "opts": [
             "Old age",
             "Sickness",
             "Schism in the Saṅgha",
             "Famine"],
         "correct": 2,
         "expl": "Saṅghabheda, placed last among the five."},
        {"q": "What common warning closes each of the five reflections?",
         "opts": [
             "That the mendicant will be reborn poorly",
             "That focusing on the Buddha's instructions and frequenting remote lodgings become harder",
             "That lay supporters will withdraw support",
             "That ordination will become impossible"],
         "correct": 1,
         "expl": "The shared consequence-warning repeated across all five perils."},
        {"q": "What does the reflector resolve to do about each of these five perils?",
         "opts": [
             "Avoid thinking about them",
             "Preempt them now by rousing energy toward what is unattained",
             "Wait until the difficulty actually arrives",
             "Request reassignment to another monastery"],
         "correct": 1,
         "expl": "Motivation for present practice, not resignation."},
        {"q": "What earlier discourse in this nipāta shares this discourse's famine and unrest material almost exactly?",
         "opts": [
             "AN 5.1",
             "AN 5.54",
             "AN 5.10",
             "AN 5.71"],
         "correct": 1,
         "expl": "AN 5.54's list of times unfavorable for meditation names famine and unrest as well."},
        {"q": "Is old age presented here mainly as something to fear, or as motivation?",
         "opts": [
             "Purely as something to fear",
             "As motivation to practice now, so as to live comfortably even when old",
             "As an unavoidable tragedy with no bearing on practice",
             "As a reason to leave monastic life early"],
         "correct": 1,
         "expl": "Consistent with the discourse's overall reflective, motivating purpose."},
        {"q": "What Pali term names the crowded-living consequence shared by two of the five perils?",
         "opts": [
             "Saṅghabheda",
             "Saṅgaṇikavihāra",
             "Dubbhikkha",
             "Byādhi"],
         "correct": 1,
         "expl": "The shared consequence of famine and civil unrest."},
        {"q": "What does the third companion discourse, AN 5.79, shift toward that AN 5.77–78 do not address?",
         "opts": [
             "Weather patterns",
             "Institutional and doctrinal decline, rather than personal or circumstantial danger",
             "Foreign relations",
             "Agricultural techniques"],
         "correct": 1,
         "expl": "A shift from personal/circumstantial change to the corruption of teaching and training."},
    ],
    marginalia=[
        ("Five perils, now for everyone", [
            "old age &middot; sickness",
            "famine &middot; unrest",
            "&middot; schism",
        ]),
        ("Same material as AN 5.54", [
            "famine and unrest",
            "as bad times",
            "for practice",
        ]),
        ("Term", [
            "<span class=\"pali\">saṅghabheda</span>",
            "&mdash; schism,",
            "named as gravest",
        ]),
        ("Cross-references", [
            "AN 5.77 &middot; the twin, wilderness-specific dangers",
            "AN 5.79 &middot; next: institutional decline",
        ]),
    ],
    further=[
        '<a href="%s/an5.78/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.77.html">AN 5.77 &middot; Future Perils (1st)</a> &mdash; this '
        "discourse&rsquo;s twin, on wilderness-specific physical dangers.",
        '<a href="an-5.54.html">AN 5.54 &middot; Untimely</a> &mdash; the direct cross-'
        "reference, sharing this discourse's famine and unrest material.",
        '<a href="an-5.79.html">AN 5.79 &middot; Future Perils (3rd)</a> &mdash; next: '
        "institutional and doctrinal decline.",
    ],
)

# --------------------------------------------------------------------------- #
# AN 5.79 — Tatiyaanāgatabhayasutta
# --------------------------------------------------------------------------- #
page(
    79, "Tatiyaanāgatabhaya", "Future Perils (3rd)",
    vagga=VAGGA_8,
    meta_title="AN 5.79 — Future Perils (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Tatiyaanāgatabhayasutta — five predicted ways the monastic community could corrupt "
        "itself from within: undeveloped teachers, doctrine misunderstood in passing, poetry "
        "preferred over the Buddha's own teaching, and lax senior mendicants. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "five predictions of institutional decline, each closing with a two-way "
                 "corruption refrain"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a serious institutional "
                       "warning, still relevant to how any tradition transmits its own "
                       "understanding"),
    ],
    why=(
        "A different register from the previous two Future Perils discourses: instead of "
        "personal or circumstantial hardship, this discourse predicts five ways the monastic "
        "community could degrade from within &mdash; underqualified teachers producing "
        "underqualified students in a self-perpetuating chain, doctrine misunderstood in "
        "passing, a preference for pleasant poetry over the Buddha's own difficult teaching, "
        "and senior mendicants setting a bad example of laxity. This reading guide treats the "
        "content with the seriousness the text itself gives it, as a genuinely significant "
        "warning about how institutions transmit both understanding and its absence."),
    guide=[
        ("The refrain: two-way corruption", [
            "Each of the five perils closes with the identical formula: <em>dhammasandosā "
            "vinayasandoso, vinayasandosā dhammasandoso</em> &mdash; corrupt training comes "
            "from corrupt teachings, and corrupt teachings come from corrupt training. This "
            "two-way feedback loop is the discourse's real subject: doctrine and discipline "
            "degrading each other in either direction, not a single point of failure."]),
        ("A chain of undeveloped teachers", [
            "The first two perils describe the identical mechanism twice: mendicants who have "
            "not developed their physical endurance, ethics, mind, or wisdom nonetheless "
            "ordain others (peril one) or take on students as mentors (peril two), and are "
            "unable to guide them in the higher ethics, mind, and wisdom. The text repeats the "
            "formula &lsquo;they too will&rsquo; across three generations, making the "
            "compounding, self-perpetuating nature of the problem explicit rather than merely "
            "implied."]),
        ("Falling into dark teachings unnoticed", [
            "The third peril names a specific activity &mdash; discussing abhidhamma and "
            "elaborations (<em>vedalla</em>) &mdash; as a site of risk, not because the "
            "activity is inherently wrong, but because it is where people can fall into wrong "
            "views &lsquo;without realizing it&rsquo;. This is the same term, vedalla, that "
            "appeared at AN 5.73 as one neutral genre among nine; here it recurs in a "
            "strikingly different, cautionary light."]),
        ("Preferring poetry to the Buddha's own words", [
            "The fourth peril predicts that future mendicants will actively want to hear "
            "elaborate poetic compositions by outsiders or disciples, while having no interest "
            "in the Buddha's own deep, profound teachings dealing with emptiness "
            "(<em>suññatā</em>). Stated plainly, this predicts an audience-preference problem "
            "rather than a doctrinal error as such: people gravitating toward more pleasant, "
            "more accessible material, letting the harder teaching go unheard. This line is "
            "among the most frequently cited in later Buddhist commentary on the risks of "
            "textual transmission."]),
        ("Senior mendicants setting a bad example", [
            "The fifth peril names senior mendicants themselves as the failure point: becoming "
            "indulgent, slack, leaders in backsliding, neglecting seclusion. The text names "
            "explicitly what follows &mdash; those who come after copy the example set before "
            "them (<em>diṭṭhānugati</em>), the same compounding, generational logic used "
            "throughout this discourse."]),
        ("Read as prediction, not settled fact", [
            "This discourse is phrased throughout in the future tense, as prediction and "
            "warning rather than a claim about anything that has definitely already occurred. "
            "This reading guide does not editorialize about whether or how far the tradition "
            "considers this prediction to have come true; it reports what the discourse "
            "warns against, with the weight the text itself gives it."]),
    ],
    terms=[
        ("dhammasandosā vinayasandoso",
         "&ldquo;corrupt training from corrupt teachings&rdquo; &mdash; the two-way refrain "
         "closing all five perils in this discourse."),
        ("abhidhammakathā / vedallakathā",
         "discussion of abhidhamma and elaborations &mdash; the site of risk named in the "
         "third peril, not condemned in itself."),
        ("suññatā",
         "&ldquo;emptiness&rdquo; &mdash; the character of the Buddha's own &lsquo;deep, "
         "profound&rsquo; discourses, contrasted with poetic composition in the fourth peril."),
        ("kāveyya",
         "&ldquo;poetic composition&rdquo; &mdash; the preferred, more pleasant alternative "
         "feared in the fourth peril."),
        ("diṭṭhānugati",
         "&ldquo;following the example set by those who came before&rdquo; &mdash; the "
         "generational mechanism named explicitly in the fifth peril."),
    ],
    text_intro=(
        "The discourse in full: five predicted ways the monastic community could corrupt "
        "itself from within, each closing with the two-way corruption refrain. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The warning"),
        ("p", "&sect;1", "an5.79:1.1-1.3"),
        ("h3", "A chain of undeveloped teachers"),
        ("p", "&sect;2", "an5.79:2.1-2.11"),
        ("p", "&sect;3", "an5.79:3.1-3.10"),
        ("h3", "Falling into dark teachings unnoticed"),
        ("p", "&sect;4", "an5.79:4.1-4.5"),
        ("h3", "Preferring poetry to the Buddha's own words"),
        ("p", "&sect;5", "an5.79:5.1-5.6"),
        ("h3", "Senior mendicants setting a bad example"),
        ("p", "&sect;6", "an5.79:6.1-6.7"),
        ("h3", "The close"),
        ("p", "&sect;7", "an5.79:7.1-7.3"),
    ],
    quiz=[
        {"q": "What two-way refrain closes each of the five perils in this discourse?",
         "opts": [
             "A blessing for the Saṅgha's continued health",
             "Corrupt training comes from corrupt teachings, and corrupt teachings come from corrupt training",
             "A warning against eating after noon",
             "A prediction of the Buddha's return"],
         "correct": 1,
         "expl": "Dhammasandosā vinayasandoso; vinayasandosā dhammasandoso — the discourse's real subject."},
        {"q": "What do the first two perils describe?",
         "opts": [
             "Foreign invasion",
             "Undeveloped teachers ordaining or mentoring others equally undeveloped, compounding across generations",
             "A famine affecting the whole region",
             "A dispute over robe material"],
         "correct": 1,
         "expl": "The self-perpetuating chain of underqualified teaching."},
        {"q": "What activity is named as the site of the third peril?",
         "opts": [
             "Farming",
             "Discussing abhidhamma and elaborations (vedalla)",
             "Walking for alms",
             "Building monasteries"],
         "correct": 1,
         "expl": "Not condemned in itself, but named as a place risk can arise unnoticed."},
        {"q": "Does the text say that discussing abhidhamma is itself wrong?",
         "opts": [
             "Yes, it forbids the activity outright",
             "No — it says people can fall into wrong views there without realizing it",
             "The text does not mention abhidhamma at all",
             "It praises the activity without qualification"],
         "correct": 1,
         "expl": "A risk located in an activity, not a condemnation of the activity itself."},
        {"q": "What kind of discourses will future mendicants prefer to listen to, per the fourth peril?",
         "opts": [
             "The Buddha's own deep teachings on emptiness",
             "Poetic compositions by outsiders or disciples",
             "Historical chronicles",
             "Debates between rival schools"],
         "correct": 1,
         "expl": "The predicted, more pleasant, more accessible alternative."},
        {"q": "What kind of discourses will they neglect, per the same peril?",
         "opts": [
             "Stories of past lives",
             "The Buddha's own deep, profound teachings dealing with emptiness",
             "Rules of monastic conduct",
             "Verses of praise"],
         "correct": 1,
         "expl": "Suññatā-related teachings, predicted to go unheard in favor of poetry."},
        {"q": "What does the fifth peril say senior mendicants will become?",
         "opts": [
             "More diligent with age",
             "Indulgent and slack, leaders in backsliding",
             "Withdrawn from all teaching duties",
             "Stricter than younger mendicants"],
         "correct": 1,
         "expl": "The fifth and final predicted failure point."},
        {"q": "What Pali term names the pattern of later generations copying earlier ones' example?",
         "opts": [
             "Diṭṭhānugati",
             "Saṅghabheda",
             "Dubbhikkha",
             "Asmimāna"],
         "correct": 0,
         "expl": "Named explicitly in the fifth peril's description."},
        {"q": "Where did the term 'vedalla' first appear in this chapter, in a neutral context?",
         "opts": [
             "AN 5.71",
             "AN 5.73, as one of nine genres a mendicant memorizes",
             "AN 5.77",
             "It does not appear elsewhere in this chapter"],
         "correct": 1,
         "expl": "The same term recurs here in a strikingly different, cautionary light."},
        {"q": "What tense does this discourse use throughout — has this decline already happened, or is it predicted?",
         "opts": [
             "Past tense, describing events already completed",
             "Predicted, future tense throughout",
             "Present tense, describing current events",
             "The discourse does not specify a timeframe"],
         "correct": 1,
         "expl": "Framed explicitly as warning and prediction, not settled fact."},
    ],
    marginalia=[
        ("The refrain: two-way corruption", [
            "dhammasandosā",
            "vinayasandoso &mdash;",
            "each feeds the other",
        ]),
        ("Poetry over emptiness", [
            "the most-quoted line",
            "in later commentary",
            "on textual risk",
        ]),
        ("Term", [
            "<span class=\"pali\">diṭṭhānugati</span>",
            "&mdash; following",
            "the example set before",
        ]),
        ("Cross-references", [
            "AN 5.73 &middot; vedalla's earlier, neutral appearance",
            "AN 5.80 &middot; next: material comfort as a parallel corrupting force",
        ]),
    ],
    further=[
        '<a href="%s/an5.79/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-5.73.html">AN 5.73 &middot; One Who Lives by the Teaching (1st)</a> '
        "&mdash; where vedalla, recontextualized here, first appeared in a neutral listing.",
        '<a href="an-5.80.html">AN 5.80 &middot; Future Perils (4th)</a> &mdash; next: '
        "material comfort and improper association as parallel corrupting forces.",
        '<a href="an-5.78.html">AN 5.78 &middot; Future Perils (2nd)</a> &mdash; the previous '
        "discourse, on personal and circumstantial rather than institutional decline.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 5.80 — Catutthaanāgatabhayasutta
# --------------------------------------------------------------------------- #
page(
    80, "Catutthaanāgatabhaya", "Future Perils (4th)",
    vagga=VAGGA_8,
    meta_title="AN 5.80 — Future Perils (4th) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Catutthaanāgatabhayasutta, closing the Warriors chapter — five predicted corrupting "
        "forces of material comfort and improper association, ending with the chapter's own "
        "colophon and mnemonic verse. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "five predictions of decline through comfort and improper association, closing "
                 "the chapter's own colophon and uddāna verse"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "not identified in this collection"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; concrete, practical "
                       "monastic-discipline concerns, closing the chapter"),
    ],
    why=(
        "The chapter's closing discourse names five more predicted corrupting forces, "
        "distinct from AN 5.79's institutional and doctrinal ones: preference for nice robes, "
        "almsfood, and lodgings, and improper closeness with nuns, trainee nuns, novice nuns, "
        "monastery attendants, and novices. It ends the chapter with its own colophon and the "
        "opening line of the summary verse."),
    guide=[
        ("Three comforts, one pattern", [
            "The first three perils share an identical template: a preference for nice robes, "
            "then nice almsfood, then nice lodgings, each leading to neglect of the "
            "corresponding austere practice (rag-robes, alms-walking, dwelling at the root of "
            "a tree), abandonment of remote wilderness lodgings for towns and cities, and "
            "&lsquo;many kinds of improper solicitation&rsquo; for the item in question."]),
        ("Mixing closely with nuns, trainee nuns, and novice nuns", [
            "The fourth peril predicts that mendicants who mix closely with the women's "
            "monastic orders can be expected to end up dissatisfied with the spiritual life, "
            "to commit a corrupt offense, or to disrobe. This is a Vinaya-adjacent concern "
            "about boundary-keeping between the orders, stated plainly here without further "
            "claims about women generally."]),
        ("Mixing closely with monastery attendants and novices", [
            "The fifth peril predicts mendicants who mix closely with lay attendants "
            "(<em>ārāmika</em>) and novices will store up goods for personal use and make "
            "&lsquo;obvious hints&rsquo; about digging earth and cutting plants &mdash; a "
            "specific reference to Vinaya training rules that forbid mendicants themselves "
            "from damaging living plants or turned soil, worked around here by hinting at "
            "attendants and novices, who are not bound by the same rule, to do it for them."]),
        ("What's different from AN 5.79", [
            "This discourse drops AN 5.79's two-way corruption refrain entirely; the chapter's "
            "final pair of discourses instead separates two distinct tracks of predicted "
            "decline &mdash; institutional and doctrinal at AN 5.79, material and relational "
            "here."]),
        ("The chapter's close", [
            "The colophon <em>Dasamaṁ. Yodhājīvavaggo tatiyo</em> &mdash; the tenth discourse, "
            "closing the third Yodhājīvavagga &mdash; follows the same mechanism explained in "
            "full at AN 5.10 and not repeated here."]),
        ("The uddāna's opening line", [
            "The chapter's mnemonic verse opens by naming its own discourse-pairs: two on "
            "freedom of heart as fruit (AN 5.71&ndash;72), and two on one who lives by the "
            "teaching (AN 5.73&ndash;74), continuing on to name the warriors (AN 5.75&ndash;76) "
            "before the verse's remaining lines are left, as elsewhere in this collection, "
            "untranslated in the source."]),
    ],
    terms=[
        ("paṁsukūlika",
         "the rag-robe practice &mdash; neglected in the first peril's preference for nice "
         "robes."),
        ("piṇḍapātika",
         "the alms-walking practice, eating only what is collected on almsround &mdash; "
         "neglected in the second peril."),
        ("saṅkiliṭṭha āpatti",
         "&ldquo;a corrupt, defiled offense&rdquo; against the monastic rules &mdash; a "
         "predicted consequence of mixing closely with the women's orders."),
        ("ārāmika",
         "a monastery attendant, a lay worker not bound by the same rules as ordained "
         "mendicants."),
        ("uddāna",
         "the mnemonic summary verse closing a chapter, first explained in full at AN 5.10."),
    ],
    text_intro=(
        "The discourse in full: five predicted corrupting forces of comfort and association, "
        "closing the chapter's colophon and the opening line of its mnemonic verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nice robes"),
        ("p", "&sect;1", "an5.80:2.1-2.7"),
        ("h3", "Nice almsfood"),
        ("p", "&sect;2", "an5.80:3.1-3.6"),
        ("h3", "Nice lodgings"),
        ("p", "&sect;3", "an5.80:4.1-4.6"),
        ("h3", "Mixing closely with nuns"),
        ("p", "&sect;4", "an5.80:5.1-5.4"),
        ("h3", "Mixing closely with monastery attendants"),
        ("p", "&sect;5", "an5.80:6.1-6.4"),
        ("h3", "The close, and the chapter's colophon"),
        ("p", "&sect;6", "an5.80:7.1-7.5"),
        ("p", "&sect;7", "an5.80:8.1-8.3"),
    ],
    quiz=[
        {"q": "What three material comforts are named in the first three perils?",
         "opts": [
             "Fame, wealth, and rank",
             "Nice robes, nice almsfood, nice lodgings",
             "Music, dance, and entertainment",
             "Gold, silver, and jewels"],
         "correct": 1,
         "expl": "Each following an identical neglect-and-solicitation pattern."},
        {"q": "What is neglected in each of the first three cases?",
         "opts": [
             "Formal ordination procedures",
             "The corresponding austere practice — rag-robes, alms-walking, or tree-root dwelling",
             "Daily chanting",
             "The teaching of new students"],
         "correct": 1,
         "expl": "Comfort displacing the matching austere practice."},
        {"q": "What are the three predicted consequences of mixing closely with nuns, trainee nuns, and novice nuns?",
         "opts": [
             "Promotion, wealth, and fame",
             "Dissatisfaction with the spiritual life, a corrupt offense, or disrobing",
             "Illness, exile, and imprisonment",
             "None — the text says nothing will happen"],
         "correct": 1,
         "expl": "The fourth peril's three predicted outcomes."},
        {"q": "What is predicted about mendicants who mix closely with monastery attendants and novices?",
         "opts": [
             "They will become excellent teachers",
             "They will hoard goods and hint about digging earth or cutting plants",
             "They will leave monastic life immediately",
             "Nothing in particular is predicted"],
         "correct": 1,
         "expl": "The fifth peril's predicted consequence."},
        {"q": "Why is 'hinting' about digging earth or cutting plants specifically a problem?",
         "opts": [
             "It wastes time",
             "It circumvents a Vinaya rule binding mendicants but not attendants or novices",
             "It is a form of theft",
             "It violates a robe-related rule"],
         "correct": 1,
         "expl": "Using someone not bound by the rule to do what the rule itself forbids."},
        {"q": "Unlike AN 5.79, what refrain is absent from this discourse's five perils?",
         "opts": [
             "The naming of each peril by number",
             "The two-way 'corrupt training from corrupt teachings' refrain",
             "The closing exhortation to rouse energy",
             "There is no difference between the two discourses' refrains"],
         "correct": 1,
         "expl": "AN 5.80 separates material/relational decline from AN 5.79's institutional/doctrinal refrain."},
        {"q": "What does the closing colophon name this discourse as?",
         "opts": [
             "The first discourse of a new chapter",
             "The tenth discourse, closing the third Yodhājīvavagga",
             "An appendix with no chapter position",
             "The fifth discourse of the chapter"],
         "correct": 1,
         "expl": "Dasamaṁ. Yodhājīvavaggo tatiyo."},
        {"q": "Where was this same colophon and uddāna mechanism first explained in this project?",
         "opts": [
             "AN 5.1",
             "AN 5.10",
             "AN 5.61",
             "It has never been explained before"],
         "correct": 1,
         "expl": "Cited here rather than re-explained, per this project's running convention."},
        {"q": "What two discourse-pairs does the uddāna verse's opening line name?",
         "opts": [
             "The two on future perils and the two on warriors",
             "The two on freedom of heart as fruit, and the two on one who lives by the teaching",
             "The two on nuns and the two on attendants",
             "The verse names no specific pairs"],
         "correct": 1,
         "expl": "AN 5.71–72 and AN 5.73–74, named by their summary-verse tags."},
        {"q": "What comes next in the Fives, after this chapter closes?",
         "opts": [
             "The nipāta ends here",
             "Chapter 9, Theravagga ('Senior Mendicants'), AN 5.81–90",
             "A return to the Nīvaraṇavagga",
             "The Sixes begin immediately"],
         "correct": 1,
         "expl": "The next chapter in sequence."},
    ],
    marginalia=[
        ("Three comforts, one pattern", [
            "robes &middot; almsfood",
            "&middot; lodgings —",
            "same neglect, same solicitation",
        ]),
        ("The attendant loophole", [
            "hinting about digging",
            "earth or cutting plants",
            "&mdash; a Vinaya workaround",
        ]),
        ("Term", [
            "<span class=\"pali\">uddāna</span>",
            "&mdash; the mnemonic",
            "verse, explained at AN 5.10",
        ]),
        ("Cross-references", [
            "AN 5.79 &middot; twin theme, institutional rather than material decline",
            "AN 5.71 &middot; back to the chapter's opening",
        ]),
    ],
    further=[
        '<a href="%s/an5.80/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment, including the "
        "untranslated closing verse." % SC,
        '<a href="an-5.79.html">AN 5.79 &middot; Future Perils (3rd)</a> &mdash; the previous '
        "discourse, on institutional and doctrinal rather than material decline.",
        '<a href="an-5.10.html">AN 5.10 &middot; Disrespect (2nd)</a> &mdash; where this same '
        "chapter-closing colophon structure was first explained in full.",
        '<a href="an-5.71.html">AN 5.71 &middot; Freedom of Heart is the Fruit (1st)</a> '
        "&mdash; back to this chapter's opening, closing the loop.",
    ],
)
