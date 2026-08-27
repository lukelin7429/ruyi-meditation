# -*- coding: utf-8 -*-
"""Jataka -- selected verses from the birth stories.

IMPORTANT SCOPE NOTE (per Luke's explicit decision 2026-08-19): the
traditional Jataka collection has 547 numbered birth stories, but bilara-data
contains Sujato CC0 translations for only 82 of them, scattered
non-sequentially (ja1, ja2... ja67, ja466...), and even those 82 are bare
verse excerpts -- the prose narrative framework that gives each Jataka tale
its story is post-canonical commentary, not part of the CC0 canonical text,
and is not available to build from. This collection can therefore never be
"complete" the way Dhammapada/Udana/Itivuttaka/Sutta-Nipata/Khuddakapatha
can. Every page in this module, and this collection's own index.html, must
say so explicitly and never imply full coverage of the traditional 547.
"""

SC = "https://suttacentral.net"

INDEX_HEADING = "Jataka — Selected Verses"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Jataka selections")
TAIL = ("./", "Jataka selections")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single Jataka verse excerpt.

    num is the traditional Jataka number (not sequential in this project --
    only the 82 numbers with a Sujato CC0 file exist at all; see this
    module's docstring). Every page built from this helper must include,
    in its own "why"/glance text, an honest note that this is a bare verse
    excerpt from a partial selection, not the traditional story in full.
    """
    d = {
        "slug": "ja-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "ja%d" % num,
        "crumb": "Ja %d" % num,
        "number_line": "Jataka &middot; No. %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 1 — Apaṇṇaka (Sure Bet)
# --------------------------------------------------------------------------- #
page(
    1, "Apa&#7751;&#7751;aka", "Sure Bet",
    meta_title="Ja 1 — Sure Bet | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 1, Sure Bet &mdash; a single aphoristic verse using "
        "gambling imagery, opening this site's partial selection from "
        "the traditional 547 Jātaka birth-story poems. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative scene &mdash; a single self-contained "
                    "aphoristic verse"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, but dense with a gambling "
                       "metaphor requiring context"),
    ],
    why=(
        "This is the first poem in this site's partial Jātaka "
        "selection &mdash; a bare single-verse aphorism, exactly the "
        "kind of text this collection is built from. Its central "
        "image, &lsquo;taking up the sure bet&rsquo;, draws on "
        "ancient dice-gambling terminology to make a point about "
        "wisdom: given a choice between a safe, certain path and a "
        "riskier, disputed one, an intelligent person takes the sure "
        "bet."),
    guide=[
        ("A single verse built entirely on a gambling metaphor", [
            "The whole poem is one image: &lsquo;apaṇṇaka&rsquo; "
            "(&lsquo;sure bet&rsquo;) is, per Sujato's comment, "
            "literally a gambling term &mdash; a guaranteed winning "
            "hand, as opposed to a riskier throw some &lsquo;sophists "
            "(takkikā)&rsquo; might argue for instead. The verse "
            "applies this directly to wisdom: when there are two "
            "possible paths, one certain and one merely argued for, "
            "&lsquo;an intelligent person, knowing this, would take "
            "up the sure bet.&rsquo;"]),
        ("A commentarial story behind the verse, not part of the canonical text", [
            "Per Sujato's own comment, the traditional prose "
            "narrative (composed later, and not part of the CC0 "
            "canonical text this site translates) compares the "
            "&lsquo;sophists&rsquo; of the verse to a native spirit "
            "(yakkha) who tried to persuade a merchant caravan to "
            "abandon its water supply while crossing a desert, "
            "trusting a false promise of water ahead. This reading "
            "guide notes the story for context, without presenting "
            "it as part of the verse itself."]),
        ("Opening this site's honest partial selection", [
            "As explained on this collection's own index page, "
            "Bhikkhu Sujato's CC0 translation of the Jātaka covers "
            "only 82 of the traditional 547 numbered tales, and even "
            "those 82 are bare verse excerpts &mdash; the prose "
            "narrative framework belongs to later commentary, not "
            "the canonical text. This poem, first of the entire "
            "Ekakanipāta (Book of the Ones, verses of a single "
            "stanza), sets that pattern for everything that follows."]),
    ],
    terms=[
        ("apaṇṇaka",
         "&ldquo;sure bet&rdquo; &mdash; per Sujato's comment, a "
         "gambling term for a guaranteed winning hand, as opposed to "
         "a riskier throw."),
        ("takkikā",
         "&ldquo;sophists&rdquo; &mdash; those who argue for the "
         "riskier, disputed &lsquo;second way&rsquo; instead of the "
         "sure bet."),
        ("medhāvī",
         "&ldquo;an intelligent person&rdquo; &mdash; the verse's "
         "model of right judgment, who takes up the sure bet."),
        ("Apaṇṇakajātaka",
         "the traditional title of this tale, &lsquo;Sure Bet&rsquo; "
         "&mdash; also the name given to the whole first chapter "
         "(Apaṇṇakavagga) this poem opens."),
        ("Ekakanipāta",
         "&ldquo;Book of the Ones&rdquo; &mdash; the traditional "
         "division of Jātaka tales told in a single verse, of which "
         "this is the first."),
    ],
    text_intro=(
        "The text in full: a homage line followed by the poem's "
        "single verse and its traditional closing tag. No comment "
        "note bears on the verse's individual words beyond what is "
        "already discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "", "ja1:1.1-1.1"),
        ("p", "&sect;1", "ja1:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does 'apaṇṇaka' (sure bet) literally mean, per Sujato's comment?",
         "opts": [
             'A gambling term for a guaranteed winning hand',
             'A type of ascetic robe',
             'A specific place name',
             'A type of alms bowl',
         ],
         "correct": 0,
         "expl": 'As opposed to a riskier throw some might argue for instead.'},
        {"q": "Who does the verse say would 'take up the sure bet'?",
         "opts": [
             'Only a king',
             'An intelligent person, knowing the choice between the two paths',
             'Only a monk',
             'No one in particular',
         ],
         "correct": 1,
         "expl": "The verse's central point about right judgment."},
        {"q": "Who are the 'sophists' (takkikā) in the verse?",
         "opts": [
             'A group of merchants',
             'The verse does not mention any sophists',
             'Those who argue for the riskier, disputed path instead of the sure bet',
             "The Buddha's own disciples",
         ],
         "correct": 2,
         "expl": "Contrasted with the 'sure bet' the intelligent person chooses instead."},
        {"q": 'What does the (non-canonical) commentarial story compare the sophists to?',
         "opts": [
             "A king's minister",
             'No story is mentioned in the comment',
             'A wise teacher',
             'A native spirit (yakkha) who tried to persuade a caravan to abandon its water in the desert',
         ],
         "correct": 3,
         "expl": 'Noted for context, without presenting it as part of the canonical verse itself.'},
        {"q": "How much of the traditional 547 Jātaka tales does this site's selection cover?",
         "opts": [
             '82, and only the verse portions, since the prose framework is later commentary not in the CC0 text',
             'Exactly 100',
             'Only this single poem',
             'All 547, in full prose and verse',
         ],
         "correct": 0,
         "expl": "As explained on this collection's own index page."},
        {"q": 'What position does this poem hold in the collection?',
         "opts": [
             'The final poem',
             'The first poem — opening both the Apaṇṇakavagga and the entire Ekakanipāta',
             'The middle poem',
             'It stands alone outside any chapter',
         ],
         "correct": 1,
         "expl": 'Setting the pattern of single-stanza aphorism for the poems that follow it.'},
        {"q": 'What is the Ekakanipāta?',
         "opts": [
             'A later commentary',
             'A collection of prose stories only',
             'The traditional division of Jātaka tales told in a single verse',
             'A collection of dialogues',
         ],
         "correct": 2,
         "expl": 'This poem is its first entry.'},
        {"q": 'Does the verse itself specify who is speaking?',
         "opts": [
             'Yes, it names the Buddha directly',
             'Yes, it names a merchant',
             'Yes, it names a specific king',
             'No — the canonical verse itself does not specify a speaker',
         ],
         "correct": 3,
         "expl": 'Unlike the commentarial story, which supplies specific characters.'},
        {"q": 'What image does the whole poem build on?',
         "opts": [
             'A gambling metaphor, contrasting a guaranteed hand with a riskier throw',
             'A sailing metaphor',
             'A cooking metaphor',
             'A farming metaphor',
         ],
         "correct": 0,
         "expl": 'Applied to the choice between a certain and a merely argued-for path.'},
        {"q": "What also shares the name 'Apaṇṇaka' with this poem?",
         "opts": [
             'Nothing else on this site',
             'The whole first chapter (Apaṇṇakavagga) that this poem opens',
             'A different Jātaka entirely',
             'A Dhammapada chapter',
         ],
         "correct": 1,
         "expl": 'Ten poems in total make up this opening chapter.'},
    ],
    marginalia=[
        ("Opening the selection", [
            "the first of 82, out of 547 —",
            "a single stanza, honestly framed"
        ]),
        ("A gambler's certainty", [
            "sure bet against the sophist's throw —",
            "wisdom as the safer wager"
        ]),
        ("A story kept at arm's length", [
            "a yakkha, a caravan, a desert —",
            "commentary, not canon, and said so"
        ]),
        ("Ten poems to a chapter", [
            "Apaṇṇakavagga begins here —",
            "each one a single, self-contained verse"
        ]),
    ],
    further=[
        '<a href="%s/ja1/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-2.html">Ja 2 &mdash; Sandy Waste</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 2 — Vaṇṇupatha (Sandy Waste)
# --------------------------------------------------------------------------- #
page(
    2, "Va&#7751;&#7751;upatha", "Sandy Waste",
    meta_title="Ja 2 — Sandy Waste | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 2, Sandy Waste &mdash; a single verse comparing "
        "untiring effort in a desert dig to a sage's persistent "
        "search for peace of heart. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative scene &mdash; a single self-contained "
                    "simile verse"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, clear simile"),
    ],
    why=(
        "This poem's single image &mdash; diggers who, by not giving "
        "up, eventually strike an underground stream beneath a sandy "
        "waste &mdash; is a compact, self-sufficient teaching on "
        "persistence in practice, needing no commentarial story to "
        "make its point (unlike several of its neighboring poems in "
        "this same chapter)."),
    guide=[
        ("A single, self-explanatory simile", [
            "The verse's first half describes diggers working "
            "&lsquo;untiringly in a sandy waste&rsquo; until they "
            "find water at an underground stream; per Sujato's "
            "comment, &lsquo;udaṅgaṇa&rsquo; is best read as "
            "&lsquo;water passage&rsquo; rather than the "
            "commentary's own reading. The second half applies the "
            "image directly: &lsquo;in the same way, a sage with "
            "strength aroused untiringly finds the peace of the "
            "heart.&rsquo;"]),
        ("A verse that needs no separate story to make its point", [
            "Unlike this site's own Ja 1, which leans on a "
            "commentarial story (the yakkha and the caravan) to "
            "fill out its gambling metaphor, this poem's simile is "
            "complete in itself: the labor of digging through sand "
            "for water directly mirrors the sustained effort of "
            "meditation practice, without needing any narrative "
            "frame to explain it."]),
    ],
    terms=[
        ("akilāsuno",
         "&ldquo;untiringly&rdquo; &mdash; the quality shared by both "
         "the diggers and the sage, repeated in both halves of the "
         "verse."),
        ("udaṅgaṇa",
         "&ldquo;underground stream&rdquo; &mdash; per Sujato's "
         "comment, best read as a water passage, against the "
         "commentary's own differing gloss."),
        ("viriyabalūpapanno",
         "&ldquo;with strength aroused&rdquo; &mdash; the sage's own "
         "energetic quality, matching the diggers' persistence."),
        ("hadayassa santiṁ",
         "&ldquo;the peace of the heart&rdquo; &mdash; what the sage "
         "finds, corresponding to the water the diggers find."),
        ("Vaṇṇupathajātaka",
         "the traditional title of this tale, &lsquo;Sandy "
         "Waste&rsquo;."),
    ],
    text_intro=(
        "The text in full: a single verse, with a technical comment "
        "on one term's reading discussed above. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja2:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What do the diggers in the verse eventually find?',
         "opts": [
             'Nothing — they give up',
             'Gold',
             'Water, at an underground stream, by digging untiringly in a sandy waste',
             'A buried treasure chest',
         ],
         "correct": 1,
         "expl": "The image the verse's second half applies to a sage's own persistence."},
        {"q": 'What quality is repeated in both halves of the verse?',
         "opts": [
             'Physical strength alone',
             'Speed',
             'Untiring persistence (akilāsuno)',
             'Wealth',
         ],
         "correct": 2,
         "expl": 'Shared explicitly by both the diggers and the sage.'},
        {"q": "What does the sage find, corresponding to the diggers' water?",
         "opts": [
             'A hidden teaching',
             'A new disciple',
             'Nothing in particular',
             'The peace of the heart',
         ],
         "correct": 3,
         "expl": "The verse's direct point of comparison."},
        {"q": "How does Sujato's comment read the term 'udaṅgaṇa'?",
         "opts": [
             "As 'water passage', against the commentary's own differing gloss",
             'As a type of tree',
             'As a proper name',
             'As a place name',
         ],
         "correct": 0,
         "expl": "A technical philological note distinct from the traditional commentary's reading."},
        {"q": 'Does this poem rely on a commentarial story to make its point?',
         "opts": [
             'Yes, extensively',
             'No — unlike its neighboring Ja 1, its simile is complete in itself',
             'Only partially',
             'The comment file does not address this',
         ],
         "correct": 1,
         "expl": 'The labor of digging for water directly mirrors sustained meditation effort without narrative framing.'},
        {"q": "What quality does the sage have, matching the diggers' effort?",
         "opts": [
             'Physical beauty',
             'Wealth',
             'Strength aroused (viriyabalūpapanno)',
             'Royal status',
         ],
         "correct": 2,
         "expl": "Directly paired with the diggers' own untiring labor."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Wanton Merchant',
             'Godly Qualities',
             'Sure Bet',
             'Sandy Waste (Vaṇṇupathajātaka)',
         ],
         "correct": 3,
         "expl": 'The second poem in the Apaṇṇakavagga.'},
        {"q": 'What form does this poem take?',
         "opts": [
             'A single four-line stanza built on one simile',
             'A ten-verse narrative',
             'A question-and-answer exchange',
             'A dialogue between two speakers',
         ],
         "correct": 0,
         "expl": 'Consistent with the brief, self-contained form of this whole opening chapter.'},
        {"q": "What is being compared to what in this verse's simile?",
         "opts": [
             'A king compared to a merchant',
             'Diggers finding water in a sandy waste, compared to a sage finding peace of heart',
             'A farmer compared to a soldier',
             'No comparison is made',
         ],
         "correct": 1,
         "expl": "The verse's entire structure rests on this single parallel."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The final poem of its chapter',
             'The second poem of the Apaṇṇakavagga, following Ja 1',
             'The first poem of a later chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem opening chapter as Ja 1.'},
    ],
    marginalia=[
        ("Digging for what lasts", [
            "sand gives way to an underground stream —",
            "the same patience finds peace of heart"
        ]),
        ("A simile needing no story", [
            "unlike its neighbor, complete alone —",
            "no commentary required to land"
        ]),
        ("One word, quietly corrected", [
            "'udaṅgaṇa' read against tradition —",
            "a water passage, not what the commentary says"
        ]),
        ("Untiring, twice over", [
            "the same word for digger and sage —",
            "persistence is persistence, either way"
        ]),
    ],
    further=[
        '<a href="%s/ja2/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-1.html">Ja 1 &mdash; Sure Bet</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-3.html">Ja 3 &mdash; The Wanton Merchant</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 3 — Serivavāṇija (The Wanton Merchant)
# --------------------------------------------------------------------------- #
page(
    3, "Serivav&amacr;&#7751;ija", "The Wanton Merchant",
    meta_title="Ja 3 — The Wanton Merchant | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 3, The Wanton Merchant &mdash; a warning verse "
        "against missing certainty in the true teaching, closely "
        "paralleling this site's own AN 8.29. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short warning verse"),
    ],
    why=(
        "This verse is, per Sujato's own comment, almost identical to "
        "a verse already complete on this site at AN 8.29, Lost "
        "Opportunities &mdash; both are believed to refer to the "
        "same underlying story, making this one of this partial "
        "Jātaka selection's clearest direct textual links to an "
        "already-completed page elsewhere on this site."),
    guide=[
        ("A warning against long regret", [
            "The verse warns plainly: fail to achieve certainty "
            "regarding the true teaching here, and &lsquo;you'll "
            "regret it for a long time, like this wanton "
            "merchant.&rsquo; The specific merchant named in the "
            "final line is left unexplained within the verse itself, "
            "pointing outward to a story the verse assumes its "
            "audience already knows."]),
        ("A near-identical verse already on this site", [
            "Sujato's own comment states that this verse is mostly "
            "the same as a verse already complete on this site at "
            "AN 8.29, Lost Opportunities, and that both are believed "
            "to refer to the same underlying story &mdash; making "
            "this one of the clearest direct parallels in this "
            "site's whole partial Jātaka selection."]),
        ("A commentarial story, and a comment questioning its own name", [
            "Per Sujato's comment, the traditional (non-canonical) "
            "prose story tells of a fraudulent merchant who tried to "
            "trick a poor woman into thinking her gold vase was "
            "worthless. The comment further notes that the "
            "commentary's own account of the merchant's name "
            "(&lsquo;Serivā&rsquo;, after a city of that name) seems "
            "implausible, since no such city appears elsewhere in the "
            "story; Sujato instead reads the word as simply "
            "&lsquo;wanton&rsquo;. This reading guide follows "
            "Sujato's own preferred reading, while noting the "
            "traditional alternative."]),
    ],
    terms=[
        ("saddhammassa niyāmataṁ",
         "&ldquo;certainty regarding the true teaching&rdquo; "
         "&mdash; what is at stake if the opportunity is missed."),
        ("ciraṁ anutappesi",
         "&ldquo;you'll regret it for a long time&rdquo; &mdash; the "
         "verse's warning for failing to achieve that certainty."),
        ("serivā / seri",
         "read by the commentary as a proper name (after a city), "
         "but by Sujato as simply &ldquo;wanton&rdquo; &mdash; see "
         "the guide above for the reasoning."),
        ("Serivavāṇijajātaka",
         "the traditional title of this tale, &lsquo;The Wanton "
         "Merchant&rsquo;."),
        ("AN 8.29",
         "&ldquo;Lost Opportunities&rdquo; &mdash; the already-"
         "completed page on this site with a verse Sujato's own "
         "comment identifies as nearly identical to this one."),
    ],
    text_intro=(
        "The text in full: a single verse, closely paralleling this "
        "site's own AN 8.29. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja3:1.1-1.4"),
    ],
    quiz=[
        {"q": "What already-completed page on this site does Sujato's comment identify as nearly identical to this verse?",
         "opts": [
             'MN 83',
             'No such parallel exists',
             'The Dhammapada',
             'AN 8.29, Lost Opportunities — both believed to refer to the same underlying story',
         ],
         "correct": 2,
         "expl": "One of the clearest direct textual links in this site's partial Jātaka selection."},
        {"q": 'What does the verse warn will happen if you fail to achieve certainty in the true teaching?',
         "opts": [
             "You'll be reborn immediately as a merchant",
             'The verse gives no consequence',
             'Nothing significant',
             "You'll regret it for a long time, like the wanton merchant",
         ],
         "correct": 3,
         "expl": "The verse's central warning."},
        {"q": 'What does the (non-canonical) commentarial story say the merchant tried to do?',
         "opts": [
             'Trick a poor woman into thinking her gold vase was worthless',
             'Found a new city',
             'Become a monk',
             'Give away his wealth',
         ],
         "correct": 0,
         "expl": 'Noted for context, without presenting it as part of the canonical verse itself.'},
        {"q": "How does Sujato read the word rendered 'wanton' in the final line?",
         "opts": [
             'As a proper name after a city, per the traditional commentary',
             "As simply 'wanton', questioning the commentary's own naming as implausible",
             'As a place name with no further meaning',
             'The comment does not address this word',
         ],
         "correct": 1,
         "expl": 'Since no such city appears elsewhere in the story to support the traditional reading.'},
        {"q": "What is at stake, according to the verse, if the true teaching's certainty is missed?",
         "opts": [
             'Nothing is said to be at stake',
             'A material loss only',
             "Long regret, illustrated by the wanton merchant's example",
             'Immediate punishment',
         ],
         "correct": 2,
         "expl": "The verse's structure moves directly from the warning to this illustrative comparison."},
        {"q": 'Does the verse itself explain who the wanton merchant was?',
         "opts": [
             'Yes, but only his profession',
             'The verse omits any reference to a merchant',
             'Yes, in full detail',
             'No — it names him only in passing, assuming the audience already knows the story',
         ],
         "correct": 3,
         "expl": 'Pointing outward to a story the canonical verse itself does not tell.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Wanton Merchant (Serivavāṇijajātaka)',
             'The Little Financier',
             'A Cup of Rice',
             'Sandy Waste',
         ],
         "correct": 0,
         "expl": 'The third poem in the Apaṇṇakavagga.'},
        {"q": 'What form does this poem take?',
         "opts": [
             'A ten-verse dialogue',
             'A single four-line warning verse',
             'A prose narrative',
             'A question-and-answer exchange',
         ],
         "correct": 1,
         "expl": "Consistent with this chapter's brief, self-contained form."},
        {"q": 'What theme connects this verse to AN 8.29?',
         "opts": [
             'No shared theme is identified',
             'A theme about generosity',
             'A theme about missing an opportunity for certainty in the teaching',
             'A theme about kingship',
         ],
         "correct": 2,
         "expl": "Sujato's comment identifies this as the shared underlying reference."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The third poem of the Apaṇṇakavagga, following Ja 1 and Ja 2',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem opening chapter.'},
    ],
    marginalia=[
        ("A verse with a twin elsewhere", [
            "nearly identical to AN 8.29 —",
            "the clearest link in this whole selection"
        ]),
        ("Regret, measured in years", [
            "miss the certainty, and pay long for it —",
            "the merchant's example left unexplained"
        ]),
        ("A name Sujato won't accept", [
            "not a city's name, just 'wanton' —",
            "the commentary's own guess set aside"
        ]),
        ("A vase mistaken for worthless", [
            "the story behind the warning, kept at arm's length —",
            "commentary, not canon, and said so"
        ]),
    ],
    further=[
        '<a href="%s/ja3/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../anguttara-nikaya/an-8.29.html">AN 8.29 &mdash; '
        "Lost Opportunities</a> &mdash; the nearly identical verse "
        "already complete on this site.",
        '<a href="ja-2.html">Ja 2 &mdash; Sandy Waste</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-4.html">Ja 4 &mdash; The Little Financier</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 4 — Cūḷaseṭṭhi (The Little Financier)
# --------------------------------------------------------------------------- #
page(
    4, "C&umacr;&#7789;ase&#7789;&#7789;hi", "The Little Financier",
    meta_title="Ja 4 — The Little Financier | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 4, The Little Financier — a verse on building wealth "
        "from small beginnings, paired with a commentarial story "
        "sometimes read as an early precursor to microfinance. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short simile verse"),
    ],
    why=(
        "This verse's plain simile — a tiny flame growing into a "
        "real fire when fanned — pairs with a commentarial story "
        "about a resourceful trader who built wealth from a single "
        "dead mouse. Sujato's own comment notes the story is "
        "sometimes read as an early precursor to the modern idea of "
        "microfinance, an unusual point of contact between this "
        "ancient collection and contemporary economic thinking."),
    guide=[
        ("A verse about starting small", [
            "The verse states plainly: &lsquo;even with a little "
            "capital the intelligent and clear-seeing man uplifts "
            "himself, like a tiny flame when fanned.&rsquo; The "
            "point is general enough to apply well beyond material "
            "wealth &mdash; to any capacity, skillfully tended, that "
            "grows from a small beginning."]),
        ("A commentarial story read as an early precursor to microfinance", [
            "Per Sujato's comment, the traditional prose story "
            "(not part of the canonical CC0 text) tells of an "
            "enterprising young man who started his business by "
            "trading a dead mouse for a penny as cat food, then "
            "built that single transaction into real wealth through "
            "successive small trades. Sujato's own comment notes "
            "this concept &lsquo;can be taken as a precursor for the "
            "modern concept of microfinance&rsquo; &mdash; an "
            "unusually direct point of contact between this ancient "
            "collection and a contemporary economic idea."]),
    ],
    terms=[
        ("appakenapi",
         "&ldquo;even with a little&rdquo; &mdash; the verse's "
         "opening concession, before turning to what can be built "
         "from that little."),
        ("medhāvī vicakkhaṇo",
         "&ldquo;the intelligent and clear-seeing man&rdquo; "
         "&mdash; the verse's model of one who grows a small "
         "beginning into something more."),
        ("aggiṁ sandhamaṁ",
         "&ldquo;a flame when fanned&rdquo; &mdash; the verse's "
         "closing image for how a small start can grow."),
        ("Cūḷaseṭṭhijātaka",
         "the traditional title of this tale, &lsquo;The Little "
         "Financier&rsquo;."),
        ("microfinance",
         "a modern economic concept &mdash; small loans or capital "
         "extended to those without access to conventional banking "
         "&mdash; that Sujato's own comment likens to the "
         "commentarial story behind this verse."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja4:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What image does the verse use for growing wealth from a small beginning?',
         "opts": [
             'A tiny flame growing when fanned',
             'A river growing from a spring',
             'No image is used',
             'A seed growing into a tree',
         ],
         "correct": 3,
         "expl": "The verse's closing line: 'like a tiny flame when fanned'."},
        {"q": "What modern economic concept does Sujato's own comment liken the commentarial story to?",
         "opts": [
             'Microfinance — small loans or capital extended to those without conventional banking access',
             'Stock markets',
             'No modern parallel is drawn',
             'International trade',
         ],
         "correct": 0,
         "expl": 'An unusually direct point of contact between this ancient collection and contemporary economic thinking.'},
        {"q": "What does the (non-canonical) commentarial story say the young man's first trade was?",
         "opts": [
             'Selling a piece of gold',
             'Trading a dead mouse for a penny as cat food',
             'Lending money at interest',
             'Selling a plot of land',
         ],
         "correct": 1,
         "expl": 'The starting point of a chain of successive small trades building real wealth.'},
        {"q": "Who does the verse describe as able to 'uplift himself' from a little capital?",
         "opts": [
             'No one in particular',
             'Only a king',
             'The intelligent and clear-seeing man',
             'Only a merchant by trade',
         ],
         "correct": 2,
         "expl": "The verse's general model of right judgment applied to resourcefulness."},
        {"q": "Does the verse's point apply only to material wealth?",
         "opts": [
             'The verse specifies it applies only to farming',
             'The verse specifies it applies only to meditation',
             'Yes, strictly to money',
             'No — the point is general enough to apply to any capacity that grows from a small beginning',
         ],
         "correct": 3,
         "expl": 'The guide notes this broader application beyond material wealth alone.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Little Financier (Cūḷaseṭṭhijātaka)',
             'Godly Qualities',
             'The Wood Gatherer',
             'Sure Bet',
         ],
         "correct": 0,
         "expl": 'The fourth poem in the Apaṇṇakavagga.'},
        {"q": 'What form does this poem take?',
         "opts": [
             'A ten-verse narrative',
             'A single four-line simile verse',
             'A dialogue between two speakers',
             'A prose story',
         ],
         "correct": 1,
         "expl": "Consistent with this chapter's brief, self-contained form."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fourth poem of the Apaṇṇakavagga, following Ja 1 through Ja 3',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem opening chapter.'},
        {"q": 'Is the commentarial story about the mouse trade part of the canonical CC0 text?',
         "opts": [
             'Partially canonical',
             'The question does not apply',
             'Yes, it is fully canonical',
             'No — it is later commentary, noted here for context only',
         ],
         "correct": 3,
         "expl": "Consistent with this whole collection's honest framing of verse versus commentary."},
        {"q": "What quality does the verse pair with 'intelligent' in describing the man who succeeds?",
         "opts": [
             'Clear-seeing (vicakkhaṇo)',
             'Royal',
             'Learned in scripture',
             'Wealthy',
         ],
         "correct": 0,
         "expl": "Together, 'the intelligent and clear-seeing man' is the verse's model."},
    ],
    marginalia=[
        ("A mouse, a penny, and what followed", [
            "the commentarial story kept at arm's length —",
            "microfinance, centuries early"
        ]),
        ("A flame, fanned", [
            "little capital, carefully tended —",
            "the verse's whole point in one image"
        ]),
        ("Beyond money alone", [
            "the principle reaches further than wealth —",
            "any small beginning, rightly grown"
        ]),
        ("Fourth of ten", [
            "the Apaṇṇakavagga continues —",
            "each verse standing on its own"
        ]),
    ],
    further=[
        '<a href="%s/ja4/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-3.html">Ja 3 &mdash; The Wanton Merchant</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-5.html">Ja 5 &mdash; A Cup of Rice</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 5 — Taṇḍulanāḷi (A Cup of Rice)
# --------------------------------------------------------------------------- #
page(
    5, "Ta&#7751;&#7693;ulan&amacr;&#7789;i", "A Cup of Rice",
    meta_title="Ja 5 — A Cup of Rice | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 5, A Cup of Rice — a dialogue verse on the folly of "
        "wildly wrong valuation, comparing five hundred horses to a "
        "cup of rice. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "A brief two-voice exchange, unlike this "
                    "chapter's mostly single-voice verses"),
        ("Speaker", "Horse traders asking a question, and the king "
                    "(or, per the verse alone, an unnamed valuer) "
                    "answering"),
        ("Form", "One four-line stanza in two matched halves"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short exchange, with an interesting "
                       "textual ambiguity"),
    ],
    why=(
        "Unlike most of this chapter's poems, this verse is a "
        "two-voice exchange, not a single aphoristic statement — and "
        "Sujato's own comment flags a genuine ambiguity in who is "
        "actually speaking the foolish valuation, since the verse "
        "itself, read alone, points to a different speaker than the "
        "traditional commentary does."),
    guide=[
        ("A dialogue about absurdly wrong valuation", [
            "Horse traders, whose 500 horses have been valued at a "
            "single cup of rice, ask the king directly: what is a "
            "cup of rice actually worth, for pricing horses? The "
            "answer given is deliberately absurd: a cup of rice is "
            "valued at the whole city of Varanasi, suburbs included "
            "&mdash; the verse's way of dramatizing a wildly, "
            "comically wrong price."]),
        ("A genuine ambiguity about who is speaking", [
            "Per Sujato's comment, the traditional prose story "
            "attributes the foolish valuation to a king's "
            "professional valuer, not the king himself. But taken on "
            "its own, without that commentarial framing, the verse "
            "appears to have the king himself giving the answer "
            "&mdash; a case where reading the bare canonical verse "
            "in isolation produces a genuinely different picture "
            "than the traditional story built around it."]),
        ("A historical note on valuation practices", [
            "Sujato's comment also observes that the importance of "
            "correct valuation is attested in other ancient texts, "
            "including detailed breakdowns in works such as the "
            "Arthaśāstra &mdash; situating this brief comic verse "
            "within a real, documented ancient concern with getting "
            "prices right."]),
    ],
    terms=[
        ("nāḷikā",
         "&ldquo;cup&rdquo; &mdash; literally a tube of bamboo; per "
         "Sujato's comment, a standard unit sufficient for a modest "
         "serving of rice."),
        ("assāna mūlāya",
         "&ldquo;for the pricing of horses&rdquo; &mdash; the "
         "question the horse traders put to the king."),
        ("Bārāṇasiṁ santarabāhirantaṁ",
         "&ldquo;Varanasi with its suburbs&rdquo; &mdash; the "
         "deliberately absurd valuation given for a single cup of "
         "rice."),
        ("Taṇḍulanāḷijātaka",
         "the traditional title of this tale, &lsquo;A Cup of "
         "Rice&rsquo;."),
        ("Arthaśāstra",
         "an ancient treatise on statecraft and economics, cited in "
         "Sujato's comment for its own detailed valuation "
         "breakdowns."),
    ],
    text_intro=(
        "The text in full: a single verse in two matched halves, "
        "with a comment flagging a genuine ambiguity about who "
        "speaks the second half, discussed above. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja5:1.1-1.4"),
    ],
    quiz=[
        {"q": "What form does this verse take, unlike most of this chapter's other poems?",
         "opts": [
             'A ten-verse narrative',
             'A two-voice dialogue exchange',
             'A prose story',
             'A silent meditation instruction',
         ],
         "correct": 0,
         "expl": "Horse traders asking a question, answered in the verse's second half."},
        {"q": 'What do the horse traders ask about?',
         "opts": [
             'The price of land',
             'What a cup of rice is worth, for pricing their 500 horses',
             'The value of gold',
             'The cost of a journey',
         ],
         "correct": 1,
         "expl": 'Their own 500 horses had been valued as a single cup of rice.'},
        {"q": 'What deliberately absurd valuation does the verse give for a cup of rice?',
         "opts": [
             'Nothing — the verse gives no valuation',
             'A single gold coin',
             'The whole city of Varanasi, with its suburbs',
             'A modest sum of silver',
         ],
         "correct": 2,
         "expl": 'Dramatizing a wildly, comically wrong price.'},
        {"q": "What ambiguity does Sujato's comment flag about this verse?",
         "opts": [
             'The number of horses involved',
             'The identity of the horse traders',
             'No ambiguity exists',
             'Whether the king or a professional valuer is the one giving the foolish valuation',
         ],
         "correct": 3,
         "expl": 'The traditional story names a valuer, but the bare verse alone appears to have the king himself speaking.'},
        {"q": 'What does the traditional (non-canonical) commentarial story attribute the foolish valuation to?',
         "opts": [
             "A king's professional valuer",
             'A group of merchants',
             'No commentarial story exists for this verse',
             'The king himself, with no other explanation',
         ],
         "correct": 0,
         "expl": 'Differing from what the bare verse alone appears to suggest.'},
        {"q": "What ancient text does Sujato's comment cite for its own detailed valuation practices?",
         "opts": [
             'The Dhammapada',
             'The Arthaśāstra, a treatise on statecraft and economics',
             'The Vinaya',
             'No other text is cited',
         ],
         "correct": 1,
         "expl": "Situating this verse's comic scenario within a real ancient concern with correct pricing."},
        {"q": "What is a 'nāḷikā', per Sujato's comment?",
         "opts": [
             'A type of horse breed',
             'A type of coin',
             'A cup, literally a bamboo tube, a standard unit for a modest serving of rice',
             'A unit of land measurement',
         ],
         "correct": 2,
         "expl": 'Confirmed by comparison with another already-completed text on this site, SN 3.13.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Godly Qualities',
             'The Wood Gatherer',
             'The Little Financier',
             'A Cup of Rice (Taṇḍulanāḷijātaka)',
         ],
         "correct": 3,
         "expl": 'The fifth poem in the Apaṇṇakavagga.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The fifth poem of the Apaṇṇakavagga, following Ja 1 through Ja 4',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem opening chapter.'},
        {"q": 'What broader point does this verse illustrate through its comic exaggeration?',
         "opts": [
             'The importance of generosity',
             'The folly of wildly wrong valuation',
             'The virtue of patience',
             'The danger of anger',
         ],
         "correct": 1,
         "expl": 'A cup of rice priced as an entire city dramatizes just how wrong a valuation can be.'},
    ],
    marginalia=[
        ("Five hundred horses, one cup of rice", [
            "the traders ask what such a price could mean —",
            "the answer, deliberately absurd"
        ]),
        ("A whole city, for a cup of rice", [
            "Varanasi, suburbs included —",
            "comic exaggeration with a real point"
        ]),
        ("Who's actually speaking?", [
            "the verse alone says one thing —",
            "the commentary, another"
        ]),
        ("An ancient concern with getting it right", [
            "the Arthaśāstra's own careful breakdowns —",
            "valuation mattered, seriously, elsewhere too"
        ]),
    ],
    further=[
        '<a href="%s/ja5/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-4.html">Ja 4 &mdash; The Little Financier</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-6.html">Ja 6 &mdash; Godly Qualities</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 6 — Devadhamma (Godly Qualities)
# --------------------------------------------------------------------------- #
page(
    6, "Devadhamma", "Godly Qualities",
    meta_title="Ja 6 — Godly Qualities | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 6, Godly Qualities — a verse defining true 'godly "
        "qualities' as conscience and prudence in good people, paired "
        "with a commentarial story of three brothers tested by a "
        "water-spirit. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short definitional verse"),
    ],
    why=(
        "This verse answers, in miniature, a question its "
        "commentarial story poses directly: what are &lsquo;godly "
        "qualities&rsquo;? Where two brothers in that story fail by "
        "naming external things (the sun and moon, the four "
        "directions), the verse itself gives the third brother's "
        "correct answer &mdash; conscience and prudence, found within "
        "good people themselves, not in any external phenomenon."),
    guide=[
        ("A definition of 'godly qualities' turned inward", [
            "The verse states its definition directly: &lsquo;endowed "
            "with conscience and prudence, and comprised of bright "
            "qualities, the good and true persons in the world are "
            "said to have godly qualities.&rsquo; The qualities named "
            "&mdash; hiri (conscience) and ottappa (prudence, or "
            "moral dread) &mdash; are internal ethical dispositions, "
            "not external, cosmic phenomena."]),
        ("A commentarial story of three brothers and a test", [
            "Per Sujato's comment, the traditional (non-canonical) "
            "story tells of three brothers asked by a water-spirit "
            "what constitute &lsquo;godly qualities&rsquo;. The first "
            "two brothers answer with external things &mdash; "
            "&lsquo;the sun and moon&rsquo; and &lsquo;the four "
            "directions&rsquo; &mdash; and are imprisoned for their "
            "wrong answers. Only the third brother's answer, matching "
            "this verse's own definition, is correct."]),
        ("A term this verse shares with another Jātaka outside this selection", [
            "Sujato's comment notes that the term &lsquo;devadhamma&rsquo; "
            "(godly qualities) also appears at Ja 458, where it "
            "carries the sense of &lsquo;god's character&rsquo; "
            "rather than this verse's own sense of a quality "
            "possessed by virtuous people. Ja 458 lies outside this "
            "site's own 82-poem selection, so this reading guide "
            "notes the cross-reference without a linked page."]),
    ],
    terms=[
        ("hiriottappasampannā",
         "&ldquo;endowed with conscience and prudence&rdquo; "
         "&mdash; the verse's own definition of godly qualities, "
         "naming two classic ethical dispositions."),
        ("sukkadhammasamāhitā",
         "&ldquo;comprised of bright qualities&rdquo; &mdash; "
         "further describing the good and true persons the verse "
         "has in mind."),
        ("devadhamma",
         "&ldquo;godly qualities&rdquo; &mdash; per Sujato's comment, "
         "a term that carries a different sense (&lsquo;god's "
         "character&rsquo;) at the unrelated Ja 458."),
        ("Devadhammajātaka",
         "the traditional title of this tale, &lsquo;Godly "
         "Qualities&rsquo;."),
        ("yakkha",
         "a native spirit; in the commentarial story, the one who "
         "poses the test to the three brothers."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja6:1.1-1.4"),
    ],
    quiz=[
        {"q": "What two qualities does the verse define as 'godly qualities'?",
         "opts": [
             'Learning and eloquence',
             'Wealth and status',
             'Conscience and prudence (hiri and ottappa)',
             'Physical strength and beauty',
         ],
         "correct": 1,
         "expl": 'Internal ethical dispositions, not external, cosmic phenomena.'},
        {"q": 'In the (non-canonical) commentarial story, how many brothers are tested?',
         "opts": [
             'Only one',
             'Two',
             'Three',
             'Five',
         ],
         "correct": 2,
         "expl": 'The first two give wrong answers and are imprisoned; only the third answers correctly.'},
        {"q": 'What wrong answers do the first two brothers give in the story?',
         "opts": [
             'Family and friendship',
             'The brothers give no answer at all',
             'Wealth and power',
             "'The sun and moon' and 'the four directions'",
         ],
         "correct": 3,
         "expl": "External, cosmic phenomena, contrasted with the third brother's correct internal answer."},
        {"q": 'Who poses the test to the three brothers in the commentarial story?',
         "opts": [
             'A water-spirit (yakkha)',
             'The Buddha himself',
             'Their own father',
             'The king',
         ],
         "correct": 0,
         "expl": 'A spirit figure who imprisons the brothers for their wrong answers.'},
        {"q": "What does Sujato's comment note about the term 'devadhamma' elsewhere?",
         "opts": [
             'It is never used elsewhere',
             "At Ja 458 (outside this site's selection), it carries the different sense of 'god's character'",
             'It always means exactly the same thing everywhere',
             'It is a modern coinage',
         ],
         "correct": 1,
         "expl": "A cross-reference noted without a linked page, since Ja 458 falls outside this site's 82-poem selection."},
        {"q": "What kind of qualities does the verse's definition emphasize — external or internal?",
         "opts": [
             'Neither — the verse gives no specifics',
             'External, cosmic phenomena',
             'Internal ethical dispositions, found within good people themselves',
             'Physical qualities only',
         ],
         "correct": 2,
         "expl": "In direct contrast to the first two brothers' failed external answers in the story."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Wood Gatherer',
             'The Chief',
             'A Cup of Rice',
             'Godly Qualities (Devadhammajātaka)',
         ],
         "correct": 3,
         "expl": 'The sixth poem in the Apaṇṇakavagga.'},
        {"q": 'What happens to the first two brothers for their wrong answers, per the commentarial story?',
         "opts": [
             'They are imprisoned',
             'They are exiled',
             'They are rewarded anyway',
             'Nothing — they are simply corrected',
         ],
         "correct": 0,
         "expl": 'Only the third brother, giving the correct answer, avoids this fate.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The sixth poem of the Apaṇṇakavagga, following Ja 1 through Ja 5',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem opening chapter.'},
        {"q": 'Does the verse itself name the three brothers or the water-spirit?',
         "opts": [
             'It names the brothers only',
             'Yes, in full detail',
             'No — those details belong only to the commentarial story, not the bare canonical verse',
             'It names the water-spirit only',
         ],
         "correct": 2,
         "expl": "Consistent with this collection's pattern of terse, self-contained verses pointing to fuller stories told only in later commentary."},
    ],
    marginalia=[
        ("A test with a wrong answer, twice", [
            "the sun and moon, the four directions —",
            "imprisoned for looking outward"
        ]),
        ("What's actually godly", [
            "conscience and prudence, nothing more exotic —",
            "found in good people, not the sky"
        ]),
        ("A shared word, a different sense", [
            "'devadhamma' means something else at Ja 458 —",
            "noted, but left unlinked, outside this selection"
        ]),
        ("Third time answers correctly", [
            "where two brothers failed, one succeeds —",
            "the verse itself is his answer"
        ]),
    ],
    further=[
        '<a href="%s/ja6/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-5.html">Ja 5 &mdash; A Cup of Rice</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-7.html">Ja 7 &mdash; The Wood Gatherer</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 7 — Kaṭṭhahāri (The Wood Gatherer)
# --------------------------------------------------------------------------- #
page(
    7, "Ka&#7789;&#7789;ah&amacr;ri", "The Wood Gatherer",
    meta_title="Ja 7 — The Wood Gatherer | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 7, The Wood Gatherer — a son's direct appeal to a "
        "king who denies him, paired with a commentarial story of a "
        "royal affair and a disowned child. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A direct appeal, spoken to an unnamed 'great "
                    "king'"),
        ("Speaker", "A son, per the commentarial story a child born "
                    "to the king and a wood-gathering woman"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, emotionally direct appeal"),
    ],
    why=(
        "Where most of this chapter's verses are general aphorisms, "
        "this one is a direct, personal appeal — a son's plea to a "
        "father who has denied him. Its commentarial story, involving "
        "a king's affair with a commoner and his initial refusal to "
        "acknowledge the resulting child, gives the bare verse a "
        "specific, human situation to stand for."),
    guide=[
        ("A son's direct appeal", [
            "The verse is spoken in the first person, directly to a "
            "&lsquo;great king&rsquo;: &lsquo;I am your son... "
            "provide for me, ruler of the people. The king provides "
            "for others, what then of his own offspring?&rsquo; Its "
            "logic is simple and pointed &mdash; if a king cares for "
            "his subjects generally, how much more should he care "
            "for his own child."]),
        ("A commentarial story of denial and eventual acknowledgment", [
            "Per Sujato's comment, the traditional (non-canonical) "
            "story tells of a king who, visiting a park, became "
            "enamoured of a simple country girl gathering wood and "
            "had sex with her. Knowing she had conceived, she "
            "informed the king, who gave her a signet ring as a "
            "token. Later, she brought the child before the court, "
            "but the king denied them, even when they presented "
            "themselves &mdash; setting up the direct appeal this "
            "verse itself gives voice to."]),
        ("A verse standing in for a resolution the canonical text does not give", [
            "The bare verse ends on the appeal itself, without "
            "confirming whether the king relents. This reading guide "
            "presents the verse as it stands in the canonical text, "
            "without asserting an ending that belongs only to the "
            "later commentarial tradition."]),
    ],
    terms=[
        ("putto tyāhaṁ mahārāja",
         "&ldquo;I am your son, great king!&rdquo; &mdash; the "
         "verse's opening, direct claim of kinship."),
        ("posa janādhipa",
         "&ldquo;provide for me, ruler of the people&rdquo; "
         "&mdash; the son's direct request."),
        ("sakaṁ pajaṁ",
         "&ldquo;his own offspring&rdquo; &mdash; the verse's "
         "closing point, that a king's own child deserves at least "
         "as much care as his subjects."),
        ("Kaṭṭhahārijātaka",
         "the traditional title of this tale, &lsquo;The Wood "
         "Gatherer&rsquo; &mdash; referring to the mother's "
         "occupation in the commentarial story."),
        ("signet ring",
         "in the commentarial story, the token the king gives the "
         "woman as proof of his identity, later used to support the "
         "child's claim."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja7:1.1-1.4"),
    ],
    quiz=[
        {"q": 'Who speaks this verse, and to whom?',
         "opts": [
             'A monk, to his teacher',
             'A merchant, to a customer',
             'A minister, to a foreign king',
             "A son, directly to a 'great king' he claims as his father",
         ],
         "correct": 2,
         "expl": "'I am your son, great king! Provide for me, ruler of the people.'"},
        {"q": "What is the verse's central logical appeal?",
         "opts": [
             'That the son deserves a share of the kingdom',
             'That the son wishes to become a monk',
             'That the king owes him a debt of money',
             'That if a king provides for his subjects generally, he should provide even more for his own offspring',
         ],
         "correct": 3,
         "expl": 'A simple, pointed logic moving from general care to particular obligation.'},
        {"q": "What does the (non-canonical) commentarial story say the mother's occupation was?",
         "opts": [
             'A woman gathering wood in a park',
             'A court musician',
             'A royal attendant',
             'A merchant',
         ],
         "correct": 0,
         "expl": "Giving this poem its traditional title, 'The Wood Gatherer'."},
        {"q": 'What token does the king give the woman in the commentarial story?',
         "opts": [
             'A sum of gold',
             'A signet ring',
             'A written letter',
             'No token is given',
         ],
         "correct": 1,
         "expl": "Later used to support the child's claim before the court."},
        {"q": 'Does the bare canonical verse confirm whether the king ultimately relents?',
         "opts": [
             'The verse states the king refuses permanently',
             'Yes, explicitly',
             'No — it ends on the appeal itself, without confirming a resolution',
             'Yes, but only implicitly',
         ],
         "correct": 2,
         "expl": 'This reading guide presents the verse as it stands, without asserting an ending belonging only to later commentary.'},
        {"q": 'What happened, per the commentarial story, when the mother first brought the child before the court?',
         "opts": [
             'The court expelled the mother',
             'The story gives no such scene',
             'The king immediately acknowledged them',
             'The king denied them, even when they presented themselves',
         ],
         "correct": 3,
         "expl": 'Setting up the direct appeal the verse itself gives voice to.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Wood Gatherer (Kaṭṭhahārijātaka)',
             'The Chief',
             'Maghadeva',
             'Godly Qualities',
         ],
         "correct": 0,
         "expl": 'The seventh poem in the Apaṇṇakavagga.'},
        {"q": "How does this verse's tone differ from most of this chapter's other poems?",
         "opts": [
             'It does not differ at all',
             'It is a direct, personal, emotionally charged appeal rather than a general aphorism',
             'It is more abstract than the others',
             'It is written in the third person only',
         ],
         "correct": 1,
         "expl": "Most of this chapter's verses state general principles; this one voices a specific, human plea."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The seventh poem of the Apaṇṇakavagga, following Ja 1 through Ja 6',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem opening chapter.'},
        {"q": 'How did the affair between the king and the woman begin, per the commentarial story?',
         "opts": [
             'She was already a member of the royal court',
             'The story does not explain how they met',
             'They had been childhood friends',
             'The king, visiting a park, became enamoured of her while she gathered wood',
         ],
         "correct": 3,
         "expl": "The origin point of the situation this verse's appeal responds to."},
    ],
    marginalia=[
        ("A son's plain claim", [
            "'I am your son, great king' —",
            "no other appeal needed"
        ]),
        ("A ring, once given", [
            "proof kept from a chance encounter —",
            "brought to court, and still denied"
        ]),
        ("The logic of a king's own child", [
            "he provides for others, what of his own? —",
            "the whole argument in four lines"
        ]),
        ("An ending the verse won't give", [
            "the appeal stands, unresolved —",
            "commentary alone says what happened next"
        ]),
    ],
    further=[
        '<a href="%s/ja7/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-6.html">Ja 6 &mdash; Godly Qualities</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-8.html">Ja 8 &mdash; The Chief</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 8 — Gāmaṇi (The Chief)
# --------------------------------------------------------------------------- #
page(
    8, "G&amacr;ma&#7751;i", "The Chief",
    meta_title="Ja 8 — The Chief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 8, The Chief — a verse on patient, unhurried success, "
        "paired with a commentarial story of a youngest prince who "
        "wins a kingdom through humble service. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "A direct address to a 'chief' (gāmaṇi)"),
        ("Speaker", "Unspecified in the canonical verse, though "
                    "per the commentarial story, a young prince"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with an interesting layer of "
                       "wordplay"),
    ],
    why=(
        "This verse's own wordplay is unusually rich for so short a "
        "text: Sujato's comment identifies a term that can mean "
        "either an ordinary word for 'chief' or a specific person's "
        "name, and a second term the traditional commentary reads "
        "narrowly as worldly success where Sujato's own comment "
        "argues it more naturally means spiritual practice."),
    guide=[
        ("A statement about patient, unhurried success", [
            "The verse opens with a general principle: &lsquo;even "
            "though they do not hurry, one who hopes for the fruit "
            "succeeds&rsquo; &mdash; before turning personal: &lsquo;I "
            "am one whose spiritual life has ripened: know this, "
            "chief.&rsquo;"]),
        ("A term the commentary and Sujato read differently", [
            "Per Sujato's comment, the word rendered &lsquo;spiritual "
            "life&rsquo; (brahmacariya) is explained by the "
            "traditional commentary as meaning &lsquo;best "
            "conduct&rsquo; leading to worldly success, since in the "
            "commentarial story the speaker's success is explicitly "
            "worldly (a prince winning a kingdom). Sujato's own "
            "comment judges this reading &lsquo;unlikely, since it "
            "invariably refers to a dedicated spiritual "
            "practice&rsquo; elsewhere &mdash; a case where the bare "
            "verse's own vocabulary sits in some tension with the "
            "worldly story built around it."]),
        ("A name that may simply be an ordinary word", [
            "Sujato's comment further notes that while "
            "&lsquo;gāmaṇi&rsquo; (chief, village head) is given in "
            "the commentarial story as the specific name of the "
            "prince, the verse itself gives no sign of being "
            "anything other than its ordinary sense &mdash; and, per "
            "the commentary's own account, the speaker may in fact "
            "be addressing himself, since &lsquo;chief&rsquo; is "
            "also his own title."]),
        ("A commentarial story of gradual, humble ascent", [
            "Per Sujato's comment, the traditional story tells of the "
            "youngest of several princes who won the kingdom not "
            "through force or cleverness, but through gradual acts of "
            "humble service &mdash; a patient path matching the "
            "verse's own opening statement about unhurried success."]),
    ],
    terms=[
        ("phalāsāva samijjhati",
         "&ldquo;one who hopes for the fruit succeeds&rdquo; "
         "&mdash; the verse's general statement about patient "
         "effort."),
        ("vipakkabrahmacariyosmi",
         "&ldquo;I am one whose spiritual life has ripened&rdquo; "
         "&mdash; a phrase Sujato's comment argues should keep its "
         "ordinary sense of dedicated spiritual practice, against "
         "the commentary's reading of mere worldly success."),
        ("gāmaṇi",
         "&ldquo;chief&rdquo; &mdash; per Sujato's comment, likely "
         "used here in its ordinary sense, though the commentary "
         "treats it as the specific name of the prince being "
         "addressed."),
        ("Gāmaṇijātaka",
         "the traditional title of this tale, &lsquo;The "
         "Chief&rsquo;."),
        ("brahmacariya",
         "&ldquo;spiritual life&rdquo; &mdash; a term Sujato's "
         "comment notes almost always refers to dedicated spiritual "
         "practice, not merely admirable worldly conduct."),
    ],
    text_intro=(
        "The text in full: a single verse, with two comments noting "
        "points of interpretive tension between the bare verse and "
        "the traditional commentary, discussed above. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja8:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What general principle does the verse open with?',
         "opts": [
             'That only the fast succeed',
             'No general principle is stated',
             'That hurry always leads to failure',
             'That even without hurrying, one who hopes for the fruit succeeds',
         ],
         "correct": 3,
         "expl": 'A statement about patient, unhurried effort leading to success.'},
        {"q": "How does the traditional commentary explain the term 'brahmacariya' (spiritual life) in this verse?",
         "opts": [
             "As 'best conduct' leading to worldly success, since the story's success is explicitly worldly",
             'As a synonym for kingship',
             'The commentary does not address this term',
             'As dedicated spiritual practice, exactly as elsewhere',
         ],
         "correct": 0,
         "expl": "A reading Sujato's own comment judges unlikely, given the term's usual dedicated-practice sense elsewhere."},
        {"q": "What does Sujato's own comment argue about that reading?",
         "opts": [
             'That it is certainly correct',
             "That it is unlikely, since 'brahmacariya' invariably refers to dedicated spiritual practice",
             'That the term has no fixed meaning at all',
             'Sujato offers no opinion',
         ],
         "correct": 1,
         "expl": "A case where the bare verse's vocabulary sits in tension with the worldly story built around it."},
        {"q": "What does the commentarial story say about the word 'gāmaṇi' (chief)?",
         "opts": [
             'No such term appears in the story',
             'It is only ever used as an ordinary word',
             'It is given as the specific name of the prince, though the verse itself shows no sign of this beyond its ordinary sense',
             'It refers to a place, not a person',
         ],
         "correct": 2,
         "expl": "Per the commentary, the speaker may even be addressing himself, since 'chief' is also his own title."},
        {"q": 'What does the (non-canonical) commentarial story say about how the prince won his kingdom?',
         "opts": [
             'Through a magical intervention',
             'Through inheritance alone, with no effort',
             'Through military conquest',
             'Through gradual acts of humble service, as the youngest of several princes',
         ],
         "correct": 3,
         "expl": "A patient path matching the verse's own opening statement about unhurried success."},
        {"q": 'What kind of success does the commentarial story describe — worldly or spiritual?',
         "opts": [
             'Explicitly worldly — winning a kingdom',
             'Explicitly spiritual — reaching awakening',
             'Neither is specified',
             'Both equally',
         ],
         "correct": 0,
         "expl": "Creating the interpretive tension Sujato's comment discusses regarding 'brahmacariya'."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Wood Gatherer',
             'The Chief (Gāmaṇijātaka)',
             'Maghadeva',
             'Living at Ease',
         ],
         "correct": 1,
         "expl": 'The eighth poem in the Apaṇṇakavagga.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The eighth poem of the Apaṇṇakavagga, following Ja 1 through Ja 7',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem opening chapter.'},
        {"q": 'Why is this verse unusually rich in interpretive tension for its short length?',
         "opts": [
             'It is written in an unusual meter',
             'It has no relation to any commentarial story',
             'It contains no ambiguous terms at all',
             "Two separate terms (brahmacariya and gāmaṇi) each carry a genuine gap between the bare verse's own sense and the commentary's reading",
         ],
         "correct": 3,
         "expl": "Both flagged directly in Sujato's own comment notes."},
        {"q": "According to Sujato's comment, might the speaker in the verse be addressing himself?",
         "opts": [
             "Yes — since 'chief' (gāmaṇi) is also the speaker's own title, per the commentary's account",
             'The comment rules this out entirely',
             'The verse names a completely different addressee',
             'No, this possibility is not raised',
         ],
         "correct": 0,
         "expl": 'A subtle possibility noted in the guide above.'},
    ],
    marginalia=[
        ("No hurry, but ripened", [
            "the fruit comes to those who wait for it —",
            "a claim made quietly, then personally"
        ]),
        ("A word in tension with its story", [
            "'spiritual life' or 'best conduct'? —",
            "Sujato sides against the commentary"
        ]),
        ("Addressing himself, perhaps", [
            "'chief' as his own title, not another's name —",
            "the verse blurs speaker and audience"
        ]),
        ("The youngest wins, slowly", [
            "not by force, but by humble service —",
            "a kingdom built one small act at a time"
        ]),
    ],
    further=[
        '<a href="%s/ja8/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-7.html">Ja 7 &mdash; The Wood Gatherer</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-9.html">Ja 9 &mdash; Maghadeva</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 9 — Maghadeva
# --------------------------------------------------------------------------- #
page(
    9, "Maghadeva", "Maghadeva",
    meta_title="Ja 9 — Maghadeva | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 9, Maghadeva — King Maghadeva's own verse on seeing "
        "his first grey hairs as a sign to renounce, directly linked "
        "to this site's own MN 83. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A king, alone, noticing his own first grey "
                    "hairs"),
        ("Speaker", "King Maghadeva himself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, image-rich verse"),
    ],
    why=(
        "This is one of this partial Jātaka selection's most direct "
        "links to an already-completed page on this site: Sujato's "
        "own comment points to this site's own MN 83, About King "
        "Maghadeva, for background on the same figure and the same "
        "grey-hair-as-signal tradition this verse gives voice to in "
        "miniature."),
    guide=[
        ("Grey hairs read as a messenger", [
            "The verse gives King Maghadeva's own first-person "
            "reaction to seeing his first grey hairs: &lsquo;growing "
            "on top of my head, these thieves of life have "
            "sprouted. Messengers of the gods have appeared &mdash; "
            "it is time for me to go forth.&rsquo; Grey hair here is "
            "not simply age; it is treated as a direct signal, a "
            "&lsquo;messenger of the gods&rsquo;, prompting immediate "
            "renunciation."]),
        ("A direct link to this site's own MN 83", [
            "Sujato's own comment directs readers to this site's own "
            "MN 83, About King Maghadeva, and its accompanying notes "
            "for fuller background on this same king and story "
            "&mdash; one of the clearest direct cross-references in "
            "this whole partial selection, connecting a single tiny "
            "verse straight to a fuller discourse already complete "
            "elsewhere on this site."]),
        ("A verse that avoids the word for old age", [
            "Sujato's comment notes something subtle: the verse "
            "deliberately avoids simply speaking of &lsquo;grey "
            "hair&rsquo; in plain terms, instead reaching for the "
            "vivid, active image of hair as &lsquo;thieves of "
            "life&rsquo; that have &lsquo;sprouted&rsquo; &mdash; a "
            "choice of language that, per the comment, shows its "
            "reliance on the fuller commentarial story for its full "
            "sense."]),
    ],
    terms=[
        ("uttamaṅgaruhā vayoharā",
         "&ldquo;thieves of life... growing on top of my "
         "head&rdquo; &mdash; the verse's vivid image for grey "
         "hairs."),
        ("devadūtā",
         "&ldquo;messengers of the gods&rdquo; &mdash; how the verse "
         "characterizes the appearance of grey hair, as a direct "
         "signal to act."),
        ("pabbajjāsamayo",
         "&ldquo;it is time for me to go forth&rdquo; &mdash; the "
         "king's own immediate resolution."),
        ("Maghadevajātaka",
         "the traditional title of this tale, named for King "
         "Maghadeva himself."),
        ("MN 83",
         "&ldquo;About King Maghadeva&rdquo; &mdash; the "
         "already-completed page on this site that Sujato's own "
         "comment directs readers to for fuller background on this "
         "same figure."),
    ],
    text_intro=(
        "The text in full: a single verse, directly cross-referenced "
        "in Sujato's comment to this site's own MN 83. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja9:1.1-1.4"),
    ],
    quiz=[
        {"q": "What prompts King Maghadeva's reaction in this verse?",
         "opts": [
             'Seeing his own first grey hairs',
             'A message from a messenger',
             'A conversation with a teacher',
             'A dream',
         ],
         "correct": 0,
         "expl": 'Treated in the verse as a direct signal to renounce.'},
        {"q": "What already-completed page on this site does Sujato's comment directly point to?",
         "opts": [
             'The Dhammapada',
             'MN 83, About King Maghadeva',
             'AN 8.29',
             'No cross-reference is given',
         ],
         "correct": 1,
         "expl": "One of this partial selection's clearest direct links to a fuller discourse elsewhere on this site."},
        {"q": 'How does the verse characterize the grey hairs?',
         "opts": [
             'The verse does not describe them',
             'As a blessing',
             "As 'thieves of life' and 'messengers of the gods'",
             'As a minor inconvenience',
         ],
         "correct": 2,
         "expl": 'Vivid, active imagery rather than a plain reference to aging.'},
        {"q": 'What does King Maghadeva resolve to do upon seeing the grey hairs?',
         "opts": [
             'Consult his ministers first',
             'Wait until more appear',
             'Ignore them',
             "Go forth immediately — 'it is time for me to go forth'",
         ],
         "correct": 3,
         "expl": 'An immediate, decisive resolution.'},
        {"q": "What does Sujato's comment note about the verse's choice of language?",
         "opts": [
             "That it avoids plainly speaking of 'grey hair', instead using vivid imagery that relies on the fuller commentarial story",
             'That it is written in an archaic dialect',
             'That it directly quotes the Buddha',
             'Nothing unusual',
         ],
         "correct": 0,
         "expl": "A subtle stylistic observation connecting the verse's imagery to its underlying narrative."},
        {"q": 'What does the verse call the grey hairs, using a very direct term?',
         "opts": [
             'Blessings of old age',
             "'Thieves of life' (vayoharā)",
             'Signs of wisdom only',
             'No specific term is used',
         ],
         "correct": 1,
         "expl": "One of the verse's two vivid images for the grey hairs."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Wood Gatherer',
             'The Chief',
             'Maghadeva (Maghadevajātaka)',
             'Living at Ease',
         ],
         "correct": 2,
         "expl": 'The ninth poem in the Apaṇṇakavagga, named directly for its speaker.'},
        {"q": 'Who speaks this verse?',
         "opts": [
             'A group of ministers',
             'A water-spirit',
             'An unnamed sage',
             'King Maghadeva himself, in the first person',
         ],
         "correct": 3,
         "expl": "Unlike several of this chapter's other poems, this verse names its speaker directly through the tale's own title."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The ninth poem of the Apaṇṇakavagga, following Ja 1 through Ja 8',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'The second-to-last poem in this ten-poem opening chapter.'},
        {"q": 'What phrase does the verse use to characterize the appearance of grey hair as a signal?',
         "opts": [
             "'A sign of weakness'",
             "'Messengers of the gods' (devadūtā)",
             "'A curse from the past'",
             'No such characterization appears',
         ],
         "correct": 1,
         "expl": 'Framing the physical sign as a direct prompt to renounce, not merely a fact of aging.'},
    ],
    marginalia=[
        ("A messenger you can't ignore", [
            "grey hair as a signal from the gods themselves —",
            "not a fact of age, but a summons"
        ]),
        ("A link straight to another page", [
            "Sujato's comment points directly to MN 83 —",
            "one verse, one fuller discourse elsewhere"
        ]),
        ("Words chosen carefully", [
            "not plainly 'grey hair', but 'thieves of life' —",
            "language that leans on the story behind it"
        ]),
        ("No delay after the sign appears", [
            "'it is time for me to go forth' —",
            "resolved in the same breath as noticed"
        ]),
    ],
    further=[
        '<a href="%s/ja9/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-083.html">MN 83 &mdash; About '
        "King Maghadeva</a> &mdash; the already-completed discourse "
        "Sujato's own comment points to for fuller background.",
        '<a href="ja-8.html">Ja 8 &mdash; The Chief</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-10.html">Ja 10 &mdash; Living at Ease</a> '
        "&mdash; the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 10 — Sukhavihāri (Living at Ease)
# --------------------------------------------------------------------------- #
page(
    10, "Sukhavih&amacr;ri", "Living at Ease",
    meta_title="Ja 10 — Living at Ease | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 10, Living at Ease, closing the Apaṇṇakavagga — a "
        "verse on freedom from mutual guardedness, identical to a "
        "line already complete on this site at Thag 11.1. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter One (Apaṇṇakavagga) &middot; Poem 10 of 10 (closing the chapter)",
    glance=[
        ("Setting", "An ascetic, addressed by a king, per the "
                    "commentarial story"),
        ("Speaker", "The ascetic, addressing the king directly as "
                    "&lsquo;O king&rsquo;"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, notable chiefly for its "
                       "exact match elsewhere on this site"),
    ],
    why=(
        "This verse's third line is word-for-word identical to a "
        "line already complete on this site's own Thag 11.1 "
        "(Saṅkicca) &mdash; per Sujato's comment, the only difference "
        "is that the Theragātha version addresses a mendicant rather "
        "than a king. It closes out the Apaṇṇakavagga, this "
        "collection's first ten-poem chapter, with the chapter's own "
        "traditional summary verse following immediately after."),
    guide=[
        ("Freedom found in not guarding, and not being guarded", [
            "The verse states its principle plainly: &lsquo;he who "
            "is not guarded by others, and who does not guard "
            "others, truly sleeps at ease, O king, unconcerned for "
            "sensual pleasures.&rsquo; Freedom from entanglement runs "
            "in both directions &mdash; not being watched over, and "
            "not watching over others &mdash; each a form of "
            "attachment given up."]),
        ("An identical line already on this site, addressed differently", [
            "Sujato's own comment notes that this verse's third line "
            "is identical to a line already complete on this site at "
            "Thag 11.1 (Saṅkicca), except that the Theragātha version "
            "is addressed to a mendicant rather than a king &mdash; a "
            "striking case of the exact same formula being repurposed "
            "across two different collections and two different "
            "addressees."]),
        ("A commentarial story of an ascetic who would not rise for a king", [
            "Per Sujato's comment, the traditional story concerns an "
            "ascetic who, lying in bliss, does not rise to greet a "
            "visiting king &mdash; the verse standing as this "
            "ascetic's own explanation for that apparent breach of "
            "courtesy: true ease comes precisely from not being "
            "bound by the mutual obligations of guarding and being "
            "guarded."]),
        ("Closing the Apaṇṇakavagga", [
            "This poem closes the Apaṇṇakavagga, the first of eight "
            "chapters this site's selection draws from within the "
            "Ekakanipāta. The source text's own untranslated summary "
            "verse (uddāna) immediately follows, naming all ten "
            "poems of this chapter in sequence &mdash; not presented "
            "here as quoted text, since it carries no separate "
            "translation, but noted for completeness."]),
    ],
    terms=[
        ("na rakkhanti / na rakkhati",
         "&ldquo;not guarded... does not guard&rdquo; &mdash; the "
         "verse's two-directional freedom, from being watched over "
         "and from watching over others."),
        ("sukhaṁ seti",
         "&ldquo;truly sleeps at ease&rdquo; &mdash; the verse's "
         "image for the resulting freedom, giving this poem its "
         "traditional title."),
        ("kāmesu anapekkhavā",
         "&ldquo;unconcerned for sensual pleasures&rdquo; &mdash; "
         "the verse's closing description of that ease."),
        ("Sukhavihārijātaka",
         "the traditional title of this tale, &lsquo;Living at "
         "Ease&rsquo;."),
        ("Thag 11.1",
         "Saṅkicca &mdash; the already-completed page on this site "
         "whose own verse shares this poem's third line word for "
         "word, addressed to a mendicant instead of a king."),
    ],
    text_intro=(
        "The text in full: a single verse, whose third line is "
        "identical to a verse already complete on this site at Thag "
        "11.1. The chapter's own untranslated closing summary verse "
        "(uddāna), which follows immediately in the source text, is "
        "not quoted here since it carries no English translation, "
        "but its content &mdash; the ten poem titles of this chapter "
        "in sequence &mdash; matches this reading guide's own further "
        "reading list below. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja10:1.1-1.4"),
    ],
    quiz=[
        {"q": "What already-completed page on this site shares this verse's third line word for word?",
         "opts": [
             'No such match exists',
             'MN 83',
             'Thag 11.1 (Saṅkicca), except addressed to a mendicant instead of a king',
             'AN 8.29',
         ],
         "correct": 1,
         "expl": 'A striking case of the exact same formula repurposed across two different collections.'},
        {"q": 'What two-directional freedom does the verse describe?',
         "opts": [
             'Freedom from travel',
             'Freedom from wealth alone',
             'Not being guarded by others, and not guarding others',
             'Freedom from speech',
         ],
         "correct": 2,
         "expl": 'Each direction is treated as its own form of attachment given up.'},
        {"q": 'What does the (non-canonical) commentarial story say about the ascetic who speaks this verse?',
         "opts": [
             'He refuses to speak to anyone',
             'No commentarial story exists for this verse',
             'He rises immediately to greet every visitor',
             'Lying in bliss, he does not rise to greet a visiting king',
         ],
         "correct": 3,
         "expl": 'The verse stands as his own explanation for this apparent breach of courtesy.'},
        {"q": 'What chapter does this poem close?',
         "opts": [
             "The Apaṇṇakavagga, the first of eight chapters this site's selection draws from",
             'It does not close any chapter',
             "A chapter outside this site's selection",
             'The final chapter of the whole Jātaka',
         ],
         "correct": 0,
         "expl": "The source text's own untranslated summary verse (uddāna) follows immediately after."},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'Yes, quoted in full',
             'No — it carries no separate English translation, so it is only noted for completeness',
             'It does not exist for this chapter',
             'It is presented as a direct quotation from the Buddha',
         ],
         "correct": 1,
         "expl": "Consistent with this collection's practice of not presenting untranslated material as quoted canonical text."},
        {"q": "What does the verse's final line describe?",
         "opts": [
             'A description of a meal',
             'A description of a palace',
             "Being 'unconcerned for sensual pleasures'",
             'A list of royal duties',
         ],
         "correct": 2,
         "expl": 'The closing quality of the ease the verse describes.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Chief',
             'Sure Bet',
             'Maghadeva',
             'Living at Ease (Sukhavihārijātaka)',
         ],
         "correct": 3,
         "expl": 'The tenth and final poem in the Apaṇṇakavagga.'},
        {"q": "Who is addressed as 'O king' in this verse?",
         "opts": [
             'The visiting king, by the ascetic speaking the verse',
             'A minister',
             'A fellow ascetic',
             'No one — the verse has no addressee',
         ],
         "correct": 0,
         "expl": 'Distinguishing this version of the shared line from its Theragātha counterpart, addressed to a mendicant instead.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of the Apaṇṇakavagga',
             'The tenth and final poem of the Apaṇṇakavagga, closing this chapter',
             'It stands outside any chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse following immediately after."},
        {"q": "How many chapters does this site's Jātaka selection draw poems from within the Ekakanipāta?",
         "opts": [
             'The full traditional count of chapters',
             'Just this one chapter',
             'Eight chapters',
             'Fifteen chapters',
         ],
         "correct": 2,
         "expl": "This site's 82-poem selection covers the first 79 of the Ekakanipāta's traditional poems, across eight chapters, plus three later outliers."},
    ],
    marginalia=[
        ("Guarding no one, guarded by none", [
            "freedom runs in both directions —",
            "true ease needs neither"
        ]),
        ("The same line, twice over", [
            "word for word with Thag 11.1 —",
            "a king here, a mendicant there"
        ]),
        ("Too much at peace to rise", [
            "the ascetic who won't greet the king —",
            "this verse is his own defense"
        ]),
        ("Ten poems, one chapter closed", [
            "the Apaṇṇakavagga's own summary follows —",
            "not quoted, since it has no translation"
        ]),
    ],
    further=[
        '<a href="%s/ja10/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../theragatha/thag-11.1.html">Thag 11.1 &mdash; '
        "Saṅkicca</a> &mdash; the already-completed page sharing "
        "this verse's third line word for word.",
        '<a href="ja-9.html">Ja 9 &mdash; Maghadeva</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 11 — Lakkhaṇamiga (The Deer Named Lucky Spot)
# --------------------------------------------------------------------------- #
page(
    11, "Lakkha&#7751;amiga", "The Deer Named Lucky Spot",
    meta_title="Ja 11 — The Deer Named Lucky Spot | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 11, opening the Sīlavagga — a verse contrasting a "
        "wise, protective deer-king with a careless one who loses his "
        "whole herd. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One stanza (six lines)"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short contrast verse"),
    ],
    why=(
        "This verse opens the Sīlavagga (&lsquo;Ethics Chapter&rsquo;) "
        "with a direct contrast between two named deer-kings, one "
        "prospering through virtuous, protective leadership and one "
        "brought low by carelessness &mdash; setting the ethical "
        "theme this whole second chapter of the collection develops."),
    guide=[
        ("Two deer-kings, two fates", [
            "The verse states its principle, then shows it: "
            "&lsquo;the virtuous ones prosper, who live extending "
            "protection. See Lucky Spot coming, surrounded by their "
            "family circle; then see this Black Mark, bereft of "
            "family.&rsquo; Per Sujato's comment, the traditional "
            "story explains the contrast directly &mdash; the wise "
            "and prudent deer-king Lucky Spot kept his herd safe on "
            "their journey, while the foolish and careless Black "
            "Mark lost his whole herd."]),
        ("Names that carry their own meaning", [
            "Sujato's comment notes that &lsquo;lakkhaṇa&rsquo; "
            "(Lucky Spot) means &lsquo;possessing beautiful or "
            "auspicious marks&rsquo;, fitting the common spotted "
            "(Chital) deer, elegant and gregarious; &lsquo;kāḷa&rsquo; "
            "(Black Mark) carries the opposite sense, "
            "&lsquo;unlucky&rsquo;. The two deer-kings' names "
            "themselves foreshadow their contrasting fates before the "
            "verse even describes them."]),
    ],
    terms=[
        ("sīlavataṁ attho",
         "&ldquo;the virtuous ones prosper&rdquo; &mdash; the "
         "verse's opening principle."),
        ("paṭisanthāravuttinaṁ",
         "&ldquo;who live extending protection&rdquo; &mdash; the "
         "specific virtue the verse credits for that prospering."),
        ("lakkhaṇa",
         "&ldquo;Lucky Spot&rdquo; &mdash; per Sujato's comment, "
         "&ldquo;possessing beautiful or auspicious marks&rdquo;, "
         "fitting a spotted (Chital) deer."),
        ("kāḷa",
         "&ldquo;Black Mark&rdquo; &mdash; the contrasting, "
         "&ldquo;unlucky&rdquo; name of the careless deer-king."),
        ("Lakkhaṇamigajātaka",
         "the traditional title of this tale, opening the "
         "Sīlavagga."),
    ],
    text_intro=(
        "The text in full: a single six-line verse. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja11:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does the verse's opening line state as a general principle?",
         "opts": [
             'That only the strong survive',
             'No general principle is stated',
             'That wealth alone brings prosperity',
             'That the virtuous ones prosper, who live extending protection',
         ],
         "correct": 2,
         "expl": 'Illustrated immediately by the contrast between the two deer-kings that follows.'},
        {"q": "What happened, per Sujato's comment on the commentarial story, to Lucky Spot's herd?",
         "opts": [
             'It scattered before the story begins',
             'No story is given for Lucky Spot',
             'It was lost entirely',
             'It was kept safe on their journey through his wisdom and prudence',
         ],
         "correct": 3,
         "expl": "Contrasted directly with Black Mark's fate."},
        {"q": "What happened to Black Mark's herd?",
         "opts": [
             'It was lost entirely, through his foolishness and carelessness',
             "It merged with Lucky Spot's herd",
             "The verse does not mention Black Mark's herd",
             'It also prospered',
         ],
         "correct": 0,
         "expl": "The verse's direct contrast: 'this Black Mark, bereft of family'."},
        {"q": "What does Sujato's comment say about the meaning of the name 'lakkhaṇa'?",
         "opts": [
             "It means 'swift runner'",
             "'Possessing beautiful or auspicious marks', fitting a spotted (Chital) deer",
             "It means 'leader of the herd'",
             'No meaning is given for the name',
         ],
         "correct": 1,
         "expl": "The name itself foreshadows the deer-king's fortunate fate."},
        {"q": "What does the name 'kāḷa' (Black Mark) mean, per the comment?",
         "opts": [
             'No meaning is given',
             "'Strong and swift'",
             "'Dark', carrying the opposite sense, 'unlucky'",
             "'Wise elder'",
         ],
         "correct": 2,
         "expl": "Contrasting directly with Lucky Spot's own auspicious name."},
        {"q": 'What chapter does this poem open?',
         "opts": [
             'The Kuruṅgavagga',
             'It does not open a chapter',
             'The Apaṇṇakavagga',
             'The Sīlavagga (Ethics Chapter)',
         ],
         "correct": 3,
         "expl": 'Setting the ethical theme this second chapter develops.'},
        {"q": 'How many deer-kings does the verse contrast?',
         "opts": [
             'Two — Lucky Spot and Black Mark',
             'Three',
             'None; the verse names no specific deer',
             'One',
         ],
         "correct": 0,
         "expl": "Their contrasting fortunes illustrate the verse's opening principle."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Deer Named Banyan',
             'The Deer Named Lucky Spot (Lakkhaṇamigajātaka)',
             'The Arrow',
             'Gales',
         ],
         "correct": 1,
         "expl": 'The eleventh poem overall, and the first of the Sīlavagga.'},
        {"q": "What kind of deer does Sujato's comment suggest 'Lucky Spot' describes?",
         "opts": [
             'No specific species is suggested',
             'A solitary predator',
             'A common spotted (Chital) deer, elegant and gregarious, roaming in herds',
             'A mythical, one-of-a-kind creature',
         ],
         "correct": 2,
         "expl": "Grounding the verse's imagery in an identifiable real animal."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The final poem of the Sīlavagga',
             'The final poem of the Ekakanipāta',
             'The first poem of the second chapter (Sīlavagga), following the completed Apaṇṇakavagga',
         ],
         "correct": 3,
         "expl": "Opening this collection's second ten-poem chapter."},
    ],
    marginalia=[
        ("Two names, two fates", [
            "Lucky Spot and Black Mark, side by side —",
            "the names themselves already tell the story"
        ]),
        ("A herd kept, a herd lost", [
            "wisdom on one journey, carelessness on the other —",
            "the verse's principle made concrete"
        ]),
        ("Opening the ethics chapter", [
            "protection extended is protection returned —",
            "ten poems on this theme begin here"
        ]),
        ("A spotted deer, elegantly named", [
            "auspicious marks give an auspicious name —",
            "unlucky in name, unlucky in fortune"
        ]),
    ],
    further=[
        '<a href="%s/ja11/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-10.html">Ja 10 &mdash; Living at Ease</a> '
        "&mdash; the closing poem of the previous chapter.",
        '<a href="ja-12.html">Ja 12 &mdash; The Deer Named '
        "Banyan</a> &mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 12 — Nigrodhamiga (The Deer Named Banyan)
# --------------------------------------------------------------------------- #
page(
    12, "Nigrodhamiga", "The Deer Named Banyan",
    meta_title="Ja 12 — The Deer Named Banyan | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 12 — a verse of resolute loyalty, paired with a "
        "commentarial story of a noble deer-king's self-sacrifice for "
        "a pregnant doe. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of resolute preference"),
    ],
    why=(
        "This tale's commentarial story &mdash; a noble deer-king "
        "offering himself in place of a pregnant doe about to be "
        "sacrificed &mdash; is one of the most affecting acts of "
        "self-sacrifice among this whole partial selection, and the "
        "verse's own stark preference (&lsquo;better death with "
        "Banyan than life with Branch&rsquo;) distills it into a "
        "single memorable line."),
    guide=[
        ("A stark preference between two leaders", [
            "The verse states its choice directly: &lsquo;befriend "
            "only Banyan, stay away from Branch. Better is death with "
            "Banyan than life with Branch.&rsquo; The names stand for "
            "two contrasting kinds of leadership, one worth dying "
            "under and the other not worth living under."]),
        ("A commentarial story of self-sacrifice", [
            "Per Sujato's comment, a meat-loving king hunted deer "
            "daily, until the deer made a pact to offer one animal "
            "from each herd by lot. When the lot fell on a pregnant "
            "doe in Branch's herd, the wicked deer-king Branch "
            "insisted she give herself up anyway &mdash; but Banyan, "
            "the noble deer-king of the other herd, intervened and "
            "went in her place himself. Moved by this act of "
            "self-sacrifice, the king spared not only Banyan's life "
            "but the lives of all the deer."]),
    ],
    terms=[
        ("nigrodha",
         "&ldquo;Banyan&rdquo; &mdash; the noble deer-king who "
         "offers himself in the pregnant doe's place."),
        ("sākha",
         "&ldquo;Branch&rdquo; &mdash; the wicked deer-king who "
         "insists the doe give herself up despite her condition."),
        ("nigrodhasmiṁ mataṁ seyyo",
         "&ldquo;better is death with Banyan&rdquo; &mdash; the "
         "verse's stark central preference."),
        ("Nigrodhamigajātaka",
         "the traditional title of this tale, &lsquo;The Deer Named "
         "Banyan&rsquo;."),
        ("self-sacrifice",
         "the act at the center of this tale's commentarial story "
         "&mdash; Banyan taking the doe's place, moving the king to "
         "spare every deer's life."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja12:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What choice does the verse state directly?',
         "opts": [
             'To befriend only Banyan and stay away from Branch — better death with Banyan than life with Branch',
             'To prefer Branch over Banyan',
             'No specific preference is stated',
             'To avoid both deer-kings equally',
         ],
         "correct": 3,
         "expl": 'A stark preference distilled into a single memorable line.'},
        {"q": "What pact, per Sujato's comment, did the deer make with the hunting king?",
         "opts": [
             'To offer one animal from each herd by lot, in exchange for the rest being spared',
             "To fight the king's hunters",
             'No such pact is described',
             'To flee the kingdom entirely',
         ],
         "correct": 0,
         "expl": 'Setting up the crisis when the lot fell on a pregnant doe.'},
        {"q": "What happened when the lot fell on a pregnant doe in Branch's herd?",
         "opts": [
             'Branch offered himself instead',
             'Branch, the wicked deer-king, insisted she give herself up anyway',
             'The king canceled the pact',
             'The doe was spared automatically due to her pregnancy',
         ],
         "correct": 1,
         "expl": "Prompting Banyan's intervention from the other herd."},
        {"q": 'What did Banyan do in response?',
         "opts": [
             'He challenged Branch to a fight',
             'Nothing — he was uninvolved',
             "He intervened and offered himself in the pregnant doe's place",
             'He fled with his own herd',
         ],
         "correct": 2,
         "expl": "An act of self-sacrifice that moved the king to spare every deer's life."},
        {"q": "What was the ultimate outcome of Banyan's self-sacrifice, per the commentarial story?",
         "opts": [
             'The king was unmoved and proceeded with the sacrifice',
             'The story does not describe an outcome',
             'Banyan alone was spared, but the doe still died',
             "The king spared not only Banyan's life but the lives of all the deer",
         ],
         "correct": 3,
         "expl": 'One of the most affecting acts of self-sacrifice among this whole partial selection.'},
        {"q": "What do the names 'Banyan' and 'Branch' represent in this verse?",
         "opts": [
             'Two contrasting kinds of leadership — one worth dying under, one not worth living under',
             'Two rival kingdoms',
             'No particular significance',
             'Two types of trees with no further significance',
         ],
         "correct": 0,
         "expl": "The verse's stark preference distills this contrast into a single line."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Deer Named Lucky Spot',
             'The Deer Named Banyan (Nigrodhamigajātaka)',
             'The Arrow',
             'The Wind-deer',
         ],
         "correct": 1,
         "expl": 'The twelfth poem overall, and the second of the Sīlavagga.'},
        {"q": 'How many lines make up this verse?',
         "opts": [
             'Eight lines',
             'Six lines',
             'Four lines',
             'Two lines',
         ],
         "correct": 2,
         "expl": "A standard single stanza, like most poems in this collection's Ekakanipāta selection."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The second poem of the Sīlavagga, following Ja 11',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Sīlavagga as Ja 11.'},
        {"q": "What broader theme does this tale's self-sacrifice illustrate, fitting the Sīlavagga's own name (Ethics Chapter)?",
         "opts": [
             'Noble leadership and self-sacrifice for the sake of others',
             'The danger of trusting kings',
             'The value of solitude',
             'The importance of wealth',
         ],
         "correct": 0,
         "expl": "Continuing the ethical theme opened by Ja 11's contrast of two deer-kings."},
    ],
    marginalia=[
        ("A pact, and a cruel loophole", [
            "one from each herd, by lot —",
            "Branch would not spare even a pregnant doe"
        ]),
        ("Better death with the noble one", [
            "the verse's whole preference in one line —",
            "Banyan over Branch, no exceptions"
        ]),
        ("A king moved by self-sacrifice", [
            "one deer's offer spares an entire herd —",
            "mercy answering mercy"
        ]),
        ("Two deer-kings, two chapters apart", [
            "Lucky Spot and Black Mark came first —",
            "now Banyan and Branch, the same lesson again"
        ]),
    ],
    further=[
        '<a href="%s/ja12/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-11.html">Ja 11 &mdash; The Deer Named Lucky '
        "Spot</a> &mdash; the poem immediately before this one.",
        '<a href="ja-13.html">Ja 13 &mdash; The Arrow</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 13 — Kaṇḍi (The Arrow)
# --------------------------------------------------------------------------- #
page(
    13, "Ka&#7751;&#7693;i", "The Arrow",
    meta_title="Ja 13 — The Arrow | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 13 — a verse voicing an ancient misogynistic "
        "prejudice, presented here alongside Sujato's own direct "
        "critical comment on it. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One stanza (six lines)"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "short, but ethically difficult content"),
    ],
    why=(
        "This verse voices an explicit prejudice against women's "
        "leadership, and this reading guide presents it honestly "
        "rather than passing over it &mdash; including Sujato's own "
        "direct comment, which states plainly that &lsquo;reality has "
        "disproven this ancient prejudice&rsquo; and identifies this "
        "as the first of several misogynistic verses in this "
        "collection, reflecting the adaptation of pre-Buddhist "
        "material into the Jātaka tradition."),
    guide=[
        ("A verse that curses women's rule alongside an arrow's wound", [
            "The verse links three curses together: &lsquo;curse the "
            "dart, the arrow that deeply strikes a man. Curse the "
            "nation where women rule. Those creatures are cursed who "
            "fall to women's sway.&rsquo; The underlying story, per "
            "Sujato's comment, tells of a naive mountain buck who "
            "falls for a doe skilled in the ways of men; when the "
            "path grows dangerous, she lets him lead the way, so that "
            "he alone falls to the arrow."]),
        ("Sujato's own direct comment on this verse's prejudice", [
            "Sujato's comment does not pass over this verse's "
            "misogyny in silence. It states directly: &lsquo;reality "
            "has disproven this ancient prejudice, as women leaders "
            "are at least as successful as men in both perception and "
            "results. This is the first of many misogynistic "
            "Jātakas. These show how Jātaka stories were adapted from "
            "non-Buddhist sources, introducing bigotry into "
            "Buddhism.&rsquo; This reading guide includes that "
            "comment in full, rather than presenting the verse's "
            "claim without context."]),
        ("A story about one deer's specific betrayal, not a general truth", [
            "Read against its own commentarial story, the verse's "
            "generalization is itself undercut by the specifics of "
            "the tale: the doe in the story is not condemned for "
            "being a leader, but for a personal act of self-interest "
            "in a moment of danger &mdash; the verse's broader claim "
            "about &lsquo;the nation where women rule&rsquo; does not "
            "actually follow from the story it is attached to."]),
    ],
    terms=[
        ("dhiratthu",
         "&ldquo;cursed be!&rdquo; &mdash; the imprecation repeated "
         "three times across the verse."),
        ("itthī pariṇāyikā",
         "&ldquo;where women rule&rdquo; &mdash; the target of the "
         "verse's second curse, explicitly identified by Sujato's "
         "comment as an ancient prejudice disproven by reality."),
        ("dhikkitā",
         "&ldquo;cursed&rdquo; &mdash; per Sujato's comment, a word "
         "of unique occurrence in Pali, from the same root as "
         "&lsquo;dhiratthu&rsquo;."),
        ("Kaṇḍijātaka",
         "the traditional title of this tale, &lsquo;The "
         "Arrow&rsquo;."),
        ("misogynistic Jātakas",
         "Sujato's own term, in his comment on this verse, for a "
         "category of tales adapted from non-Buddhist sources that "
         "introduced this kind of bigotry into the tradition."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, presented here "
        "alongside Sujato's own direct critical comment on its "
        "content, discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja13:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does Sujato's own comment say about this verse's claim regarding women's leadership?",
         "opts": [
             "That 'reality has disproven this ancient prejudice, as women leaders are at least as successful as men'",
             'Sujato offers no opinion on this verse',
             'That the verse should be removed from the translation',
             'That it is confirmed by later evidence',
         ],
         "correct": 0,
         "expl": 'A direct, unambiguous critical comment included in full in this reading guide.'},
        {"q": "What does Sujato's comment identify this verse as an example of?",
         "opts": [
             'A unique, isolated case',
             'The first of many misogynistic Jātakas, showing how such stories were adapted from non-Buddhist sources',
             'A later scribal error with no historical significance',
             'A verse later removed from the canon',
         ],
         "correct": 1,
         "expl": 'Reflecting the introduction of bigotry into Buddhism through adapted pre-Buddhist material.'},
        {"q": 'What does the commentarial story actually describe?',
         "opts": [
             'No commentarial story exists for this verse',
             'A woman ruling a nation unjustly',
             'A naive mountain buck falling for a doe skilled in the ways of men, who lets him lead into danger to save herself',
             'A battle between two kingdoms',
         ],
         "correct": 2,
         "expl": "A specific, personal act of self-interest, not a general case about women's rule."},
        {"q": "How does this reading guide characterize the relationship between the story and the verse's broader curse against 'women's rule'?",
         "opts": [
             'The story fully justifies the generalization',
             'There is no connection between them at all',
             'They match perfectly',
             "The verse's broader generalization does not actually follow from the specific story it is attached to",
         ],
         "correct": 3,
         "expl": 'The doe is condemned for a personal betrayal, not for being a leader.'},
        {"q": 'How many curses does this verse link together?',
         "opts": [
             "Three — the arrow, the nation where women rule, and those who fall under women's sway",
             'Five',
             'None; the verse contains no curses',
             'One',
         ],
         "correct": 0,
         "expl": "All three are marked with the repeated imprecation 'dhiratthu' (cursed be)."},
        {"q": "What does 'dhikkitā' mean, per Sujato's comment?",
         "opts": [
             'A term of blessing',
             "'Cursed', a word of unique occurrence in Pali sharing a root with 'dhiratthu'",
             'A proper name',
             'A type of weapon',
         ],
         "correct": 1,
         "expl": "Reinforcing the verse's repeated cursing language."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Gales',
             'The Deer Named Banyan',
             'The Arrow (Kaṇḍijātaka)',
             'The Wind-deer',
         ],
         "correct": 2,
         "expl": 'The thirteenth poem overall, and the third of the Sīlavagga.'},
        {"q": "Why does this reading guide include Sujato's critical comment in full, rather than presenting the verse alone?",
         "opts": [
             'Because the verse is not actually part of the canonical text',
             'There is no particular reason given',
             "To pad the page's length",
             "To present the verse's difficult content honestly, with its own translator's direct critical response, rather than passing over it in silence",
         ],
         "correct": 3,
         "expl": "Consistent with this site's practice of engaging honestly with ethically difficult historical material."},
        {"q": 'What specifically betrays the mountain buck, per the commentarial story?',
         "opts": [
             'The doe, who lets him lead the dangerous path so that he alone falls to the arrow',
             'The hunter directly',
             'No betrayal is described',
             'A rival buck',
         ],
         "correct": 0,
         "expl": 'The specific act of self-interest the story actually turns on.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The third poem of the Sīlavagga, following Ja 11 and Ja 12',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Sīlavagga.'},
    ],
    marginalia=[
        ("A curse the translator won't let stand", [
            "'reality has disproven this ancient prejudice' —",
            "Sujato's own comment, stated plainly"
        ]),
        ("One betrayal, generalized unfairly", [
            "a single doe's self-interest —",
            "stretched into a curse on a whole nation"
        ]),
        ("Named honestly as bigotry", [
            "'the first of many misogynistic Jātakas' —",
            "adapted from sources outside the tradition"
        ]),
        ("A story that undercuts its own verse", [
            "read closely, the tale doesn't prove the claim —",
            "personal fault, not proof of anything general"
        ]),
    ],
    further=[
        '<a href="%s/ja13/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment, including the full comment "
        "discussed above." % SC,
        '<a href="ja-12.html">Ja 12 &mdash; The Deer Named Banyan</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-14.html">Ja 14 &mdash; The Wind-deer</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 14 — Vātamiga (The Wind-deer)
# --------------------------------------------------------------------------- #
page(
    14, "V&amacr;tamiga", "The Wind-deer",
    meta_title="Ja 14 — The Wind-deer | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 14 — a verse on how even an elusive, wary creature "
        "can be trapped by desire for taste, cross-linked to this "
        "site's own SN 9.8. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with a naturalist's aside"),
    ],
    why=(
        "Sujato's comment on this verse cites a specific "
        "thirteenth-century naturalist text describing the "
        "&lsquo;wind-deer&rsquo; as an exceptionally fast, elusive "
        "creature, and cross-references this site's own SN 9.8 for a "
        "related description of the same animal &mdash; an unusually "
        "concrete zoological note anchoring this verse's teaching "
        "about the power of desire."),
    guide=[
        ("Even the elusive can be caught by taste", [
            "The verse states its point directly: &lsquo;nothing, it "
            "seems, is worse than tastes in monasteries or meeting "
            "places. The domesticated Wind-deer was brought under "
            "Victor's sway by tastes.&rsquo; Per Sujato's comment, "
            "the story behind it is simple: even the elusive "
            "wind-deer was trapped by honey left out by a groundskeeper "
            "named Victor, who released the deer once he had made his "
            "point about the pull of desire."]),
        ("A naturalist's note on a specific, fast creature", [
            "Sujato's comment cites Haṁsadeva's thirteenth-century "
            "Mṛgapakṣiśāstra to describe the &lsquo;wind-deer&rsquo; "
            "as fast, skilled at escaping weapons, and adept at "
            "vanishing from sight &mdash; lean, long-legged, and "
            "branch-antlered, dwelling in deep forests. The comment "
            "further cross-references this site's own SN 9.8, where "
            "the same creature is described as flighty and easily "
            "startled &mdash; making the verse's point sharper: if "
            "even so wary a creature can be caught by desire for "
            "taste, no one is beyond that risk."]),
        ("A philological note on a single word", [
            "Sujato's comment prefers the reading &lsquo;gehanissitaṁ&rsquo; "
            "(&lsquo;domesticated&rsquo;, connected to home comforts) "
            "over the metrically incorrect variant "
            "&lsquo;gahananissitaṁ&rsquo;, noting the confusion "
            "between the two readings is an old one, reflected even "
            "in the traditional commentary itself."]),
    ],
    terms=[
        ("vātamiga",
         "&ldquo;Wind-deer&rdquo; &mdash; per Sujato's comment, a "
         "fast, elusive forest creature described in a thirteenth-"
         "century naturalist text and cross-referenced at this "
         "site's own SN 9.8."),
        ("rasehi",
         "&ldquo;by tastes&rdquo; &mdash; the specific temptation "
         "that overcomes even the wariest creature."),
        ("gehanissitaṁ",
         "&ldquo;domesticated&rdquo; &mdash; Sujato's preferred "
         "reading, connected to the comforts of home life, over a "
         "metrically incorrect variant."),
        ("Vātamigajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Wind-deer&rsquo;."),
        ("SN 9.8",
         "&ldquo;The Mistress of the House&rdquo; &mdash; the "
         "already-completed page on this site cross-referenced in "
         "Sujato's comment for a related description of the same "
         "creature."),
    ],
    text_intro=(
        "The text in full: a single verse, with a naturalist's aside "
        "in Sujato's comment discussed above. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja14:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse identify as 'worse than' anything else, in monasteries or meeting places?",
         "opts": [
             'Loud noise',
             'Tastes',
             'Crowds',
             'Poor lighting',
         ],
         "correct": 1,
         "expl": 'The temptation that even overcomes the elusive wind-deer.'},
        {"q": "What already-completed page on this site does Sujato's comment cross-reference for the same creature?",
         "opts": [
             'No cross-reference is given',
             'MN 51',
             'SN 9.8, The Mistress of the House',
             'AN 8.13',
         ],
         "correct": 2,
         "expl": 'Describing the wind-deer there as flighty and easily startled.'},
        {"q": "What thirteenth-century text does Sujato's comment cite for a description of the wind-deer?",
         "opts": [
             'The Dhammapada commentary',
             'No specific text is cited',
             'The Arthaśāstra',
             "Haṁsadeva's Mṛgapakṣiśāstra",
         ],
         "correct": 3,
         "expl": 'Describing the creature as fast, elusive, and skilled at vanishing from sight.'},
        {"q": 'How was the wind-deer trapped, per the commentarial story?',
         "opts": [
             'By honey left out by a groundskeeper named Victor',
             'By being chased down',
             'No trapping method is described',
             'By a physical cage',
         ],
         "correct": 0,
         "expl": 'Once Victor had made his point, he released the deer.'},
        {"q": "What philological choice does Sujato's comment prefer for one word in this verse?",
         "opts": [
             'No such choice is discussed',
             "'Domesticated' (gehanissitaṁ) over the metrically incorrect variant 'gahananissitaṁ'",
             'A completely different reading unrelated to either option',
             "The commentary's reading over Sujato's own",
         ],
         "correct": 1,
         "expl": 'Noting the confusion between the two readings is an old one, reflected even in the traditional commentary.'},
        {"q": 'What overall point does this verse make?',
         "opts": [
             'That groundskeepers cannot be trusted',
             'That deer are untrainable',
             'That even an elusive, wary creature can be trapped by desire for taste',
             'That honey should never be used as bait',
         ],
         "correct": 2,
         "expl": 'Sharpened by the naturalist detail that the wind-deer is unusually fast and hard to catch.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Accept the Ass',
             'Gales',
             'The Arrow',
             'The Wind-deer (Vātamigajātaka)',
         ],
         "correct": 3,
         "expl": 'The fourteenth poem overall, and the fourth of the Sīlavagga.'},
        {"q": 'What happened to the wind-deer after the groundskeeper made his point?',
         "opts": [
             'It was released',
             'It was sold',
             'The story does not say',
             'It was kept in captivity',
         ],
         "correct": 0,
         "expl": 'The trapping was a lesson, not a permanent capture.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The fourth poem of the Sīlavagga, following Ja 11 through Ja 13',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Sīlavagga.'},
        {"q": 'What physical qualities does the naturalist text ascribe to the wind-deer?',
         "opts": [
             'No physical description is given',
             'Slow and heavy-set',
             'Lean, long-legged, and branch-antlered, dwelling in deep forests',
             'Small and hornless',
         ],
         "correct": 2,
         "expl": "Grounding the verse's point in a specific, identifiable creature."},
    ],
    marginalia=[
        ("Faster than weapons, slower than desire", [
            "a creature skilled at vanishing from sight —",
            "caught anyway, by a taste for honey"
        ]),
        ("A named groundskeeper's lesson", [
            "Victor traps, then releases —",
            "the point made, the deer set free"
        ]),
        ("The same animal, two pages apart", [
            "flighty and easily startled at SN 9.8 —",
            "and here, undone by a single taste"
        ]),
        ("A word restored against a scribal slip", [
            "'domesticated', not 'in the thicket' —",
            "an old confusion, carefully corrected"
        ]),
    ],
    further=[
        '<a href="%s/ja14/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../samyutta-nikaya/sn-9.8.html">SN 9.8 &mdash; The '
        "Mistress of the House</a> &mdash; cross-referenced in "
        "Sujato's own comment for the same creature.",
        '<a href="ja-13.html">Ja 13 &mdash; The Arrow</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-15.html">Ja 15 &mdash; Accept the Ass</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 15 — Kharādiya (Accept the Ass)
# --------------------------------------------------------------------------- #
page(
    15, "Khar&amacr;diya", "Accept the Ass",
    meta_title="Ja 15 — Accept the Ass | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 15 — a terse verse about giving up on an unteachable "
        "pupil, the first half of a deliberately paired set with the "
        "next poem, and cross-linked to this site's own MN 51 and AN "
        "8.13. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, exchanging two short "
                 "statements"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; unusually compressed, with a genuine "
                       "textual dispute"),
    ],
    why=(
        "Sujato's own comment identifies this poem as deliberately "
        "paired with the next (Ja 16) &mdash; composed together "
        "despite different meters, sharing terms, ideas, and poetic "
        "play &mdash; and flags a genuine dispute with the "
        "traditional commentary over whether a key word names an "
        "animal or a person."),
    guide=[
        ("Giving up on an unteachable pupil", [
            "The verse presents two short statements: an offer "
            "&mdash; &lsquo;please accept the eight-hooved ass, the "
            "deer more wily than the wily&rsquo; &mdash; met with a "
            "refusal: &lsquo;he has skipped the appointment seven "
            "times &mdash; I'll make no effort to instruct him.&rsquo; "
            "Per Sujato's comment, the story tells how the Bodhisatta "
            "declared a deer unteachable after it failed to show up "
            "for lessons on the ruses of deer, seven times running."]),
        ("A genuine dispute over one word's meaning", [
            "Sujato's comment flags real disagreement with the "
            "traditional commentary here: where the commentary reads "
            "&lsquo;kharādiye&rsquo; as a vocative address to "
            "&lsquo;Kharādiyā&rsquo;, the name of the Bodhisatta's "
            "own sister, Sujato instead reads &lsquo;khara&rsquo; as "
            "&lsquo;ass, mule&rsquo; and &lsquo;ādiye&rsquo; as a "
            "verb form meaning &lsquo;you should accept&rsquo; "
            "&mdash; giving two genuinely different readings of who "
            "or what is actually being discussed."]),
        ("Deliberately composed as a pair with the next poem", [
            "Sujato's comment states directly that this poem and the "
            "next (Ja 16) &lsquo;form a pair&rsquo; &mdash; though "
            "written in different meters, the &lsquo;prevalence of "
            "shared terms, ideas, and poetic play shows they must "
            "have been composed together.&rsquo; This reading guide "
            "notes the connection here and reprises it on the "
            "following page."]),
        ("A cross-linked theme of animal ruses", [
            "The theme of deer employing deceptive tricks to survive "
            "connects to already-completed pages on this site: "
            "Sujato's comment on the next verse's imagery points to "
            "MN 51 and AN 8.13, both of which discuss animal "
            "cunning and deceptive ruses in ways that illuminate this "
            "pair of poems."]),
    ],
    terms=[
        ("kharādiye",
         "read by the traditional commentary as a vocative address "
         "to the Bodhisatta's sister Kharādiyā, but by Sujato as "
         "&ldquo;you should accept the ass&rdquo; &mdash; see the "
         "guide above."),
        ("vaṅkātivaṅkinaṁ",
         "&ldquo;more wily than the wily&rdquo; &mdash; describing "
         "the deer's cunning, possibly meant as praise rather than "
         "criticism, per Sujato's comment."),
        ("sattahi kālātikkantaṁ",
         "&ldquo;he has skipped the appointment seven times&rdquo; "
         "&mdash; the specific reason given for abandoning the "
         "pupil."),
        ("Kharādiyajātaka",
         "the traditional title of this tale, &lsquo;Accept the "
         "Ass&rsquo;."),
        ("Ja 16",
         "the next poem in this chapter, which Sujato's own comment "
         "identifies as deliberately composed as a pair with this "
         "one."),
    ],
    text_intro=(
        "The text in full: a single verse, with a genuine "
        "interpretive dispute discussed above. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja15:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Sujato's comment say about this poem's relationship to the next poem, Ja 16?",
         "opts": [
             'This poem is a later addition based on Ja 16',
             'They are entirely unrelated',
             'They form a deliberately composed pair — despite different meters, they share terms, ideas, and poetic play',
             'Ja 16 was written centuries later as a response',
         ],
         "correct": 2,
         "expl": "Sujato's comment states they 'must have been composed together'."},
        {"q": "What genuine dispute does Sujato's comment raise about the word 'kharādiye'?",
         "opts": [
             'Whether it refers to a place or a person',
             'Whether it is even a real word',
             'No dispute exists — the meaning is settled',
             "Whether it addresses the Bodhisatta's sister by name, or means 'you should accept the ass'",
         ],
         "correct": 3,
         "expl": "The traditional commentary and Sujato's own reading genuinely diverge here."},
        {"q": 'Why, per the commentarial story, does the Bodhisatta refuse to instruct the deer?',
         "opts": [
             'The deer skipped the appointment seven times',
             'The deer was too old to learn',
             'No reason is given',
             'The deer insulted him',
         ],
         "correct": 0,
         "expl": "'I'll make no effort to instruct him' — a direct, terse refusal."},
        {"q": "What does Sujato's comment suggest 'more wily than the wily' might actually be, despite sounding critical?",
         "opts": [
             'A definite insult with no other reading',
             'Possibly meant as praise, referring to legitimate animal survival ruses',
             "A description of the deer's physical appearance only",
             'A mistranslation with no clear sense',
         ],
         "correct": 1,
         "expl": 'Connecting to the theme of animal cunning discussed further at Ja 16.'},
        {"q": 'What lessons was the deer supposed to attend, per the commentarial story?',
         "opts": [
             'No specific lessons are mentioned',
             'Lessons on finding water',
             'Lessons on the ruses of deer',
             'Lessons on herd migration',
         ],
         "correct": 2,
         "expl": "Directly connecting to the pair's shared theme, developed further in Ja 16."},
        {"q": 'What already-completed pages on this site does the theme of animal ruses connect to?',
         "opts": [
             'Only the Dhammapada',
             'SN 9.8 alone',
             'No related pages exist',
             'MN 51 and AN 8.13',
         ],
         "correct": 3,
         "expl": 'Both discuss animal cunning in ways that illuminate this pair of poems.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Accept the Ass (Kharādiyajātaka)',
             'The Triply Collapsed Deer',
             'Gales',
             'The Wind-deer',
         ],
         "correct": 0,
         "expl": 'The fifteenth poem overall, and the fifth of the Sīlavagga.'},
        {"q": 'What form does this verse take?',
         "opts": [
             'A single continuous statement',
             'Two short exchanged statements — an offer and a refusal',
             'A ten-line narrative',
             'A prose passage',
         ],
         "correct": 1,
         "expl": "Unusually compressed even for this collection's typically terse verses."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fifth poem of the Sīlavagga, following Ja 11 through Ja 14',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Sīlavagga, immediately preceding its deliberately paired companion.'},
        {"q": "How does the traditional commentary read 'khara' in 'kharādiye'?",
         "opts": [
             "As 'wisdom'",
             'As a place name',
             'The commentary offers no reading',
             "As part of the name Kharādiyā, the Bodhisatta's sister",
         ],
         "correct": 3,
         "expl": "Differing from Sujato's own preferred reading of 'khara' as 'ass, mule'."},
    ],
    marginalia=[
        ("Seven missed appointments", [
            "the teacher's patience finally runs out —",
            "'I'll make no effort to instruct him'"
        ]),
        ("An ass, or a sister?", [
            "the commentary and Sujato genuinely disagree —",
            "one word, two entirely different readings"
        ]),
        ("Composed as a matched set", [
            "different meters, shared terms and play —",
            "this poem and the next, written together"
        ]),
        ("Wily, and maybe worth praising for it", [
            "cunning that sounds like criticism —",
            "but might be admiration in disguise"
        ]),
    ],
    further=[
        '<a href="%s/ja15/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-051.html">MN 51 &mdash; With '
        "Kandaraka</a> &mdash; connected to this pair's theme of "
        "animal ruses.",
        '<a href="../anguttara-nikaya/an-8.13.html">AN 8.13 &mdash; '
        "A Thoroughbred</a> &mdash; likewise connected to that theme.",
        '<a href="ja-14.html">Ja 14 &mdash; The Wind-deer</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-16.html">Ja 16 &mdash; The Triply Collapsed '
        "Deer</a> &mdash; this poem's deliberately composed "
        "companion.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 16 — Tipallattha (The Triply Collapsed Deer)
# --------------------------------------------------------------------------- #
page(
    16, "Tipallattha", "The Triply Collapsed Deer",
    meta_title="Ja 16 — The Triply Collapsed Deer | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 16 — a compressed catalog of a clever deer's six "
        "survival tricks, completing this collection's deliberately "
        "paired set with Ja 15. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, densely packed with "
                 "wordplay"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; the most densely wordplay-packed verse "
                       "in this chapter"),
    ],
    why=(
        "This poem completes the deliberately composed pair begun at "
        "Ja 15, cataloging in just four lines a set of six survival "
        "tricks for a clever deer &mdash; each phrase, per Sujato's "
        "comment, doing double duty as wordplay chiming against terms "
        "in its companion verse."),
    guide=[
        ("A deer's earned second chance, densely described", [
            "Where Ja 15 ended in refusal, this verse describes a "
            "deer who has, per Sujato's comment, attentively learned "
            "the ruses of deer after all: &lsquo;triply collapsed "
            "with many illusions, eight-hooved, a midnight drinker "
            "&mdash; he's breathing on the ground through one "
            "nostril! Excelling with these six tricks, he deserves a "
            "chance.&rsquo;"]),
        ("Six specific tricks, named by the comment", [
            "Sujato's comment spells out what the verse only "
            "compresses: the &lsquo;six tricks&rsquo; are the three "
            "ways of playing dead, the eight hooves (making little "
            "sound with a dainty tread), sneaking a drink at "
            "midnight, and breathing through one nostril &mdash; a "
            "full catalog of deceptive survival behavior packed into "
            "a single dense stanza."]),
        ("Wordplay linking this poem to its companion", [
            "Sujato's comment traces deliberate verbal echoes between "
            "this verse and Ja 15: &lsquo;aṭṭha&rsquo; (eight) chimes "
            "with &lsquo;aḍḍha&rsquo; (midnight) here, just as "
            "&lsquo;chahi kalāhi&rsquo; (six tricks) chimes with "
            "&lsquo;sattahi kālāti&rsquo; (seven times) in the "
            "previous poem &mdash; confirming, at the level of "
            "individual sound, that these two verses were composed "
            "as a matched set."]),
    ],
    terms=[
        ("tipallattha",
         "&ldquo;triply collapsed&rdquo; &mdash; the first of the "
         "deer's six survival tricks, one of three distinct ways of "
         "playing dead."),
        ("aṭṭhakkhuraṁ",
         "&ldquo;eight-hooved&rdquo; &mdash; per Sujato's comment, "
         "possibly referring to a dainty, quiet tread rather than a "
         "literal extra pair of hooves."),
        ("aḍḍharattāpapāyiṁ",
         "&ldquo;a midnight drinker&rdquo; &mdash; one of the six "
         "tricks, sneaking a drink under cover of darkness."),
        ("chahi kalāhi",
         "&ldquo;with these six tricks&rdquo; &mdash; the verse's "
         "own summary count, chiming deliberately with "
         "&lsquo;sattahi kālāti&rsquo; (seven times) in Ja 15."),
        ("Tipallatthamigajātaka",
         "the traditional title of this tale, &lsquo;The Triply "
         "Collapsed Deer&rsquo;."),
    ],
    text_intro=(
        "The text in full: a single verse, densely packed with "
        "wordplay chiming against its companion poem, Ja 15, "
        "discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja16:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse describe, following on from Ja 15's refusal?",
         "opts": [
             'A deer who has attentively learned the ruses of deer, earning a second chance',
             'A different animal entirely',
             'The same refusal repeated',
             'A completely unrelated story',
         ],
         "correct": 3,
         "expl": "'Excelling with these six tricks, he deserves a chance.'"},
        {"q": "How many specific survival tricks does Sujato's comment identify in this verse?",
         "opts": [
             'Six — three ways of playing dead, eight hooves, midnight drinking, and breathing through one nostril',
             'Ten',
             'The comment gives no specific count',
             'Three',
         ],
         "correct": 0,
         "expl": 'A full catalog of deceptive survival behavior packed into a single dense stanza.'},
        {"q": "What wordplay does Sujato's comment identify linking this verse to Ja 15?",
         "opts": [
             'No wordplay is identified',
             "'Aṭṭha' (eight) chiming with 'aḍḍha' (midnight), and 'chahi kalāhi' (six tricks) chiming with 'sattahi kālāti' (seven times)",
             'Only a shared rhyme scheme',
             'A shared refrain repeated word for word',
         ],
         "correct": 1,
         "expl": 'Confirming, at the level of individual sound, that the two poems were composed as a matched set.'},
        {"q": "What might 'eight-hooved' actually refer to, per Sujato's comment?",
         "opts": [
             'The comment does not address this term',
             'A literal extra pair of hooves',
             'Possibly a dainty, quiet tread making little sound, rather than a literal anatomical detail',
             'A completely unrelated meaning',
         ],
         "correct": 2,
         "expl": "One of several places where the verse's compressed language requires the comment to unpack it."},
        {"q": "What is one of the deer's six tricks, according to the comment?",
         "opts": [
             'Swimming across rivers',
             'Changing color',
             'Climbing trees',
             'Sneaking a drink at midnight',
         ],
         "correct": 3,
         "expl": 'Listed alongside three ways of playing dead, eight hooves, and breathing through one nostril.'},
        {"q": "What is this poem's relationship to Ja 15?",
         "opts": [
             'A deliberately composed pair, sharing terms, ideas, and poetic wordplay despite different meters',
             'This poem was written centuries earlier',
             'They contradict each other directly',
             'No relationship — they are entirely separate',
         ],
         "correct": 0,
         "expl": "Confirmed by Sujato's own comment on both poems."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Accept the Ass',
             'The Triply Collapsed Deer (Tipallatthamigajātaka)',
             'Gales',
             'The Feast for the Dead',
         ],
         "correct": 1,
         "expl": 'The sixteenth poem overall, and the sixth of the Sīlavagga.'},
        {"q": "How would you describe this verse's density, compared to most others in this chapter?",
         "opts": [
             'The longest verse in the whole collection',
             'Unusually sparse and simple',
             'Unusually dense, packing six distinct tricks and layered wordplay into four lines',
             'About average for this chapter',
         ],
         "correct": 2,
         "expl": "Flagged directly in this reading guide's own difficulty rating as the chapter's most compressed verse."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The sixth poem of the Sīlavagga, immediately following its companion poem Ja 15',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Sīlavagga.'},
        {"q": "Why does the verse's conclusion say the deer 'deserves a chance'?",
         "opts": [
             'Because he has excelled at the six survival tricks he was meant to learn',
             'Because no reason is given',
             'Because the teacher relented out of pity alone',
             'Because he is young',
         ],
         "correct": 0,
         "expl": 'Reversing the outcome of the paired poem, Ja 15, where the same pupil was given up on.'},
    ],
    marginalia=[
        ("Six tricks, four lines", [
            "playing dead three ways, drinking by night —",
            "a whole survival curriculum, compressed"
        ]),
        ("A second chance, earned this time", [
            "where Ja 15 ended in refusal —",
            "this poem answers with 'he deserves a chance'"
        ]),
        ("Sound linking two poems", [
            "'aṭṭha' echoing 'aḍḍha', six echoing seven —",
            "composed together, and it shows"
        ]),
        ("The densest verse in the chapter", [
            "wordplay layered on wordplay —",
            "needing the comment to unpack it fully"
        ]),
    ],
    further=[
        '<a href="%s/ja16/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-15.html">Ja 15 &mdash; Accept the Ass</a> '
        "&mdash; this poem's deliberately composed companion, "
        "immediately before it.",
        '<a href="ja-17.html">Ja 17 &mdash; Gales</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 17 — Māluta (Gales)
# --------------------------------------------------------------------------- #
page(
    17, "M&amacr;luta", "Gales",
    meta_title="Ja 17 — Gales | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 17 — a verse resolving a friendly dispute by showing "
        "both sides were right, prompted by two friends arguing about "
        "when the cold comes. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "The Bodhisatta, per the commentarial story, "
                    "settling a dispute between two friends"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, gently humorous verse"),
    ],
    why=(
        "Unlike this chapter's more dramatic tales of sacrifice and "
        "betrayal, this poem resolves a small, almost comic dispute "
        "&mdash; and Sujato's own comment draws out a gentle, "
        "self-aware moral: that even close friends can end up "
        "arguing over trivial things."),
    guide=[
        ("A dispute resolved by finding both sides right", [
            "The verse settles a disagreement directly: &lsquo;whether "
            "the moon is waning or waxing, it is cool when the gale "
            "blows. Since the wind brings the cool, both are "
            "undefeated in this instance.&rsquo; Per Sujato's comment, "
            "two friends had been arguing about whether the cold came "
            "in the dark or bright phase of the moon, and the "
            "Bodhisatta's answer dissolves the argument rather than "
            "declaring a winner: neither is wrong, since the wind "
            "brings coolness at any time."]),
        ("A gentle moral about friends arguing over trivial things", [
            "Sujato's own comment draws out the poem's underlying "
            "point with a touch of humor: &lsquo;the moral of the "
            "story would seem to be that even close friends can end "
            "up arguing over stupid things.&rsquo; Compared to this "
            "chapter's other poems &mdash; involving self-sacrifice, "
            "betrayal, and unteachable pupils &mdash; this one settles "
            "for a lighter, more good-humored kind of wisdom."]),
    ],
    terms=[
        ("kāḷe vā yadi vā juṇhe",
         "&ldquo;whether the moon is waning or waxing&rdquo; "
         "&mdash; the two positions the friends had been arguing "
         "over."),
        ("vātajāni sītāni",
         "&ldquo;the wind brings the cool&rdquo; &mdash; the "
         "verse's actual explanation, bypassing the dispute "
         "entirely."),
        ("ubhotthamaparājitā",
         "&ldquo;both are undefeated&rdquo; &mdash; the verse's "
         "resolution, finding both friends correct rather than "
         "declaring a winner."),
        ("Mālutajātaka",
         "the traditional title of this tale, &lsquo;Gales&rsquo;."),
        ("Bodhisatta",
         "the Buddha-to-be in this and other Jātaka tales; here, the "
         "one who settles the friends' dispute."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja17:1.1-1.4"),
    ],
    quiz=[
        {"q": "What were the two friends arguing about, per Sujato's comment?",
         "opts": [
             'Which season was best',
             'Whether the cold came in the dark or bright phase of the moon',
             'Who was the better hunter',
             'The comment does not describe a dispute',
         ],
         "correct": 0,
         "expl": 'A small, almost comic dispute the verse then resolves.'},
        {"q": 'How does the verse resolve the dispute?',
         "opts": [
             'By declaring one friend the clear winner',
             "By showing the wind brings coolness at any time, so both are 'undefeated'",
             'By refusing to answer at all',
             'By dismissing the question as unimportant',
         ],
         "correct": 1,
         "expl": 'Dissolving the argument rather than declaring a winner.'},
        {"q": "What gentle moral does Sujato's own comment draw from this story?",
         "opts": [
             'No moral is drawn',
             'That arguments should always be settled by an authority',
             'That even close friends can end up arguing over stupid things',
             'That the moon controls the weather',
         ],
         "correct": 2,
         "expl": "A touch of self-aware humor distinct from this chapter's more dramatic poems."},
        {"q": 'Who resolves the dispute, per the commentarial story?',
         "opts": [
             'A third friend',
             'No one resolves it',
             'A king',
             'The Bodhisatta',
         ],
         "correct": 3,
         "expl": 'Settling the argument with an answer that satisfies both sides.'},
        {"q": "How does this poem's tone compare to this chapter's other tales, such as Ja 12 or Ja 13?",
         "opts": [
             'Lighter and more good-humored, settling for a gentler kind of wisdom',
             'Darker and more tragic',
             'There is no notable difference in tone',
             'Equally dramatic and weighty',
         ],
         "correct": 0,
         "expl": 'A contrast noted directly in this reading guide.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Triply Collapsed Deer',
             'Gales (Mālutajātaka)',
             'The Feast for the Dead',
             'The Vowed Feast',
         ],
         "correct": 1,
         "expl": 'The seventeenth poem overall, and the seventh of the Sīlavagga.'},
        {"q": "What single natural force does the verse credit for bringing the cold, regardless of the moon's phase?",
         "opts": [
             'Cloud cover',
             'Rain',
             'The gale (wind)',
             'The stars',
         ],
         "correct": 2,
         "expl": "'Since the wind brings the cool, both are undefeated in this instance.'"},
        {"q": 'Does the verse declare either friend to be wrong?',
         "opts": [
             'Yes, both friends are declared wrong',
             'The verse does not address the dispute directly',
             'Yes, one friend is clearly wrong',
             'No — the verse finds a way for both positions to be correct',
         ],
         "correct": 3,
         "expl": 'A diplomatic resolution rather than a declared winner.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The seventh poem of the Sīlavagga, following Ja 11 through Ja 16',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Sīlavagga.'},
        {"q": "What role does 'Bodhisatta' refer to in this and other Jātaka tales?",
         "opts": [
             'A title for any wise elder',
             'The Buddha-to-be, in his past lives',
             'A specific historical king',
             'A term with no fixed meaning',
         ],
         "correct": 1,
         "expl": "Here, the figure who settles the friends' small dispute."},
    ],
    marginalia=[
        ("An argument about the moon", [
            "waning or waxing, which brings the cold? —",
            "a dispute settled by looking past the question"
        ]),
        ("Both sides declared undefeated", [
            "not a winner and a loser —",
            "just a truer explanation than either guessed"
        ]),
        ("A moral with a wink", [
            "'even close friends argue over stupid things' —",
            "Sujato's own comment, lightly amused"
        ]),
        ("A break from this chapter's heavier tales", [
            "no sacrifice, no betrayal here —",
            "just wind, and a small dispute resolved"
        ]),
    ],
    further=[
        '<a href="%s/ja17/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-16.html">Ja 16 &mdash; The Triply Collapsed '
        "Deer</a> &mdash; the poem immediately before this one.",
        '<a href="ja-18.html">Ja 18 &mdash; The Feast for the '
        "Dead</a> &mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 18 — Matakabhatta (The Feast for the Dead)
# --------------------------------------------------------------------------- #
page(
    18, "Matakabhatta", "The Feast for the Dead",
    meta_title="Ja 18 — The Feast for the Dead | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 18 — a verse against animal sacrifice, paired with a "
        "commentarial story of a goat who laughs and weeps before "
        "being killed. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with a striking commentarial "
                       "image"),
    ],
    why=(
        "This verse's argument against killing is direct and "
        "compassionate on its own, but Sujato's comment adds a "
        "striking, unsettling image behind it &mdash; a sacrificial "
        "goat who alternates between laughing and weeping, each for "
        "its own reason &mdash; and situates the practice of animal "
        "sacrifice in a documented ancient context reaching back to "
        "Vedic ritual texts."),
    guide=[
        ("An argument against killing, grounded in shared suffering", [
            "The verse states its case plainly: &lsquo;if beings only "
            "knew how this suffering is created by birth, no creature "
            "would kill another, for the slayer of creatures "
            "grieves.&rsquo; The argument does not appeal to rules or "
            "commandments, but to a shared, honest recognition of "
            "what killing costs both the killed and the killer."]),
        ("A goat who laughs and weeps for different reasons", [
            "Per Sujato's comment, the commentarial story tells of a "
            "goat being prepared for a sacrificial offering to the "
            "departed, who startles those present by alternating "
            "between laughter and tears. It laughs, the story "
            "explains, because it knows its own bad karma is about "
            "to be expiated through this death; it weeps because it "
            "knows the one performing the sacrifice will suffer as it "
            "has &mdash; a single image carrying both the verse's "
            "compassion for the victim and its warning to the "
            "killer."]),
        ("A documented ancient practice", [
            "Sujato's comment situates this story within real "
            "documented history: goat sacrifice, it notes, was known "
            "since Vedic times, citing the Rig Veda and the "
            "Śatapatha Brāhmaṇa as textual evidence &mdash; grounding "
            "this tale's critique in an actually attested ancient "
            "ritual practice, not a hypothetical one."]),
    ],
    terms=[
        ("dukkhāyaṁ jātisambhavo",
         "&ldquo;how this suffering is created by birth&rdquo; "
         "&mdash; the shared condition the verse asks its audience "
         "to recognize."),
        ("pāṇaghātī hi socati",
         "&ldquo;the slayer of creatures grieves&rdquo; &mdash; the "
         "verse's closing warning to whoever kills."),
        ("matakabhatta",
         "&ldquo;the feast for the dead&rdquo; &mdash; the "
         "sacrificial offering ritual this tale's commentarial story "
         "concerns."),
        ("Matakabhattajātaka",
         "the traditional title of this tale, &lsquo;The Feast for "
         "the Dead&rsquo;."),
        ("Rig Veda / Śatapatha Brāhmaṇa",
         "ancient Vedic textual sources Sujato's comment cites as "
         "documented evidence that goat sacrifice was practiced "
         "since Vedic times."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja18:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What argument does the verse make against killing?',
         "opts": [
             'No argument is made',
             'That it violates a specific commandment',
             'That if beings knew how suffering is created by birth, no creature would kill another, since the killer also grieves',
             'That killing is only wrong for certain species',
         ],
         "correct": 1,
         "expl": 'An appeal to shared recognition rather than rules.'},
        {"q": "What striking image does the commentarial story add, per Sujato's comment?",
         "opts": [
             'No such image is described',
             'A goat that speaks in human language',
             'A goat who alternates between laughing and weeping before its sacrifice, each for a different reason',
             'A goat that escapes the sacrifice',
         ],
         "correct": 2,
         "expl": 'Carrying both compassion for the victim and a warning to the killer in a single image.'},
        {"q": 'Why does the goat laugh, per the commentarial story?',
         "opts": [
             'Because it finds the ritual absurd',
             'The story gives no reason',
             'Because it does not understand what is happening',
             'Because it knows its own bad karma is about to be expiated through this death',
         ],
         "correct": 3,
         "expl": "One half of the goat's dual reaction."},
        {"q": 'Why does the goat weep?',
         "opts": [
             'Because it knows the one performing the sacrifice will suffer as it has',
             'Because it wants to be spared',
             'The story gives no reason',
             'Out of fear alone',
         ],
         "correct": 0,
         "expl": "The other half of the goat's dual reaction, carrying the verse's warning to the killer."},
        {"q": "What ancient texts does Sujato's comment cite as evidence that goat sacrifice dates to Vedic times?",
         "opts": [
             'No texts are cited',
             'The Rig Veda and the Śatapatha Brāhmaṇa',
             'The Dhammapada',
             'The Arthaśāstra',
         ],
         "correct": 1,
         "expl": "Grounding this tale's critique in a documented, attested ancient ritual practice."},
        {"q": "What does the verse's closing line state about the one who kills?",
         "opts": [
             'No statement is made about the killer',
             'That they are rewarded',
             'That the slayer of creatures grieves',
             'That they feel nothing',
         ],
         "correct": 2,
         "expl": "The verse's final, direct warning."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Vowed Feast',
             'The Reed Drink',
             'Gales',
             'The Feast for the Dead (Matakabhattajātaka)',
         ],
         "correct": 3,
         "expl": 'The eighteenth poem overall, and the eighth of the Sīlavagga.'},
        {"q": "What kind of ritual does this tale's commentarial story concern?",
         "opts": [
             'An animal sacrifice offered as a feast for the departed',
             'A harvest festival',
             'A coronation',
             'A wedding ceremony',
         ],
         "correct": 0,
         "expl": "Giving this poem its traditional title, 'The Feast for the Dead'."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The eighth poem of the Sīlavagga, following Ja 11 through Ja 17',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Sīlavagga, sharing an anti-sacrifice theme with the next poem, Ja 19.'},
        {"q": "What is the basis of the verse's argument — rules, or shared suffering?",
         "opts": [
             'Purely a matter of ritual purity',
             'A specific prohibition handed down by authority',
             'A shared recognition of the suffering created by birth, applying to both victim and killer',
             'Neither — the verse gives no basis',
         ],
         "correct": 2,
         "expl": 'An appeal to empathy and honest recognition, not commandment.'},
    ],
    marginalia=[
        ("Two reasons, one animal", [
            "laughter for karma about to be paid —",
            "tears for the suffering still to come"
        ]),
        ("A grief that runs both ways", [
            "'the slayer of creatures grieves' —",
            "the verse's warning as much as its plea"
        ]),
        ("A practice documented, not imagined", [
            "the Rig Veda, the Śatapatha Brāhmaṇa —",
            "real ritual, real critique"
        ]),
        ("Understanding as the only real deterrent", [
            "not a rule, but recognition —",
            "if beings only knew, no one would kill"
        ]),
    ],
    further=[
        '<a href="%s/ja18/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-17.html">Ja 17 &mdash; Gales</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-19.html">Ja 19 &mdash; The Vowed Feast</a> '
        "&mdash; the next poem in this chapter, sharing this poem's "
        "anti-sacrifice theme.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 19 — Āyācitabhatta (The Vowed Feast)
# --------------------------------------------------------------------------- #
page(
    19, "&Amacr;y&amacr;citabhatta", "The Vowed Feast",
    meta_title="Ja 19 — The Vowed Feast | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 19 — a deliberately riddling verse against seeking "
        "release from a vow through sacrifice, with Sujato's own "
        "comment supplying the paraphrase the verse withholds. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, deliberately riddling"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; deliberately paradoxical, requiring "
                       "the comment's paraphrase"),
    ],
    why=(
        "Sujato's own comment states outright that this verse's "
        "riddling wordplay on &lsquo;release&rsquo; and "
        "&lsquo;binding&rsquo; is difficult enough that he translates "
        "literally and supplies a separate paraphrase &mdash; making "
        "this an unusually transparent look at the gap between a "
        "compressed canonical verse and the plain sense it is meant "
        "to carry."),
    guide=[
        ("A riddle built on the words 'release' and 'binding'", [
            "The verse plays on paradox: &lsquo;if you would be "
            "released, after death might you be released, because "
            "releasing binds. That's not how the attentive are "
            "released; such release is the fool's bondage.&rsquo; "
            "Sujato's comment acknowledges the verse is "
            "&lsquo;riddling&rsquo;, and offers a direct paraphrase: "
            "&lsquo;if you want to be released from your vow, only in "
            "some future life might you find release... because "
            "releasing yourself from a vow by sacrificing an animal "
            "only binds you to suffering.&rsquo;"]),
        ("A vow to sacrifice, and the trap it creates", [
            "Per Sujato's comment, the underlying story concerns a "
            "merchant who makes a sacrifice to ensure the success of "
            "his voyage, vowing that on his return he will perform "
            "another sacrifice, freeing him from that first vow. The "
            "verse's point is that this apparent &lsquo;release&rsquo; "
            "is no release at all: each sacrificial killing only "
            "creates further bondage to suffering, for both animal "
            "and vower."]),
        ("A companion piece to the previous poem's critique of sacrifice", [
            "This verse continues directly from Ja 18's argument "
            "against killing, applying the same underlying concern to "
            "a different specific case: not a feast honoring the "
            "dead, but a vow made to secure a safe journey. Together, "
            "the two poems form a short internal pair critiquing "
            "sacrificial practice from two angles."]),
    ],
    terms=[
        ("sace mucce pecca mucce",
         "&ldquo;if you would be released, after death might you be "
         "released&rdquo; &mdash; the verse's opening riddle, per "
         "Sujato's comment deliberately paradoxical."),
        ("muccamāno hi bajjhati",
         "&ldquo;because releasing binds&rdquo; &mdash; the verse's "
         "central paradox, resolved only by Sujato's separate "
         "paraphrase in his comment."),
        ("mutti bālassa bandhanaṁ",
         "&ldquo;such release is the fool's bondage&rdquo; &mdash; "
         "the verse's closing statement of its own paradox."),
        ("Āyācitabhattajātaka",
         "the traditional title of this tale, &lsquo;The Vowed "
         "Feast&rsquo;."),
        ("Ja 18",
         "the previous poem in this chapter, forming a short "
         "internal pair with this one, both critiquing sacrificial "
         "practice."),
    ],
    text_intro=(
        "The text in full: a single verse, deliberately riddling, "
        "which Sujato's own comment translates literally before "
        "supplying a separate paraphrase, discussed above. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja19:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Sujato's comment say directly about this verse's style?",
         "opts": [
             'That its meaning is permanently lost',
             'That it is perfectly clear and needs no explanation',
             "That it is 'riddling', requiring a literal translation plus a separate paraphrase",
             'That it is a later, corrupted addition',
         ],
         "correct": 2,
         "expl": 'An unusually transparent look at the gap between a compressed verse and its intended sense.'},
        {"q": "What paraphrase does Sujato's comment supply for the verse's central paradox?",
         "opts": [
             'That all vows should be broken immediately',
             'That vows made before a journey are meaningless',
             'No paraphrase is given',
             'That releasing yourself from a vow by sacrificing an animal only binds you to suffering',
         ],
         "correct": 3,
         "expl": "Resolving the wordplay on 'release' and 'binding' that the bare verse leaves compressed."},
        {"q": "What vow does the underlying story concern, per Sujato's comment?",
         "opts": [
             "A merchant's vow to perform another sacrifice upon his safe return from a voyage",
             'A vow to never sacrifice again',
             'No specific vow is described',
             'A vow of silence',
         ],
         "correct": 0,
         "expl": 'Made to ensure the success of his voyage, with a second sacrifice promised to release him from it.'},
        {"q": 'According to the verse, does completing the second sacrifice actually release the merchant?',
         "opts": [
             'Yes, completely and immediately',
             'No — the verse argues this apparent release only creates further bondage to suffering',
             'The verse does not address this',
             'Only if performed at a specific shrine',
         ],
         "correct": 1,
         "expl": "'Releasing binds' — each sacrificial killing creates further bondage, not less."},
        {"q": 'How does this poem relate to Ja 18, the previous poem in this chapter?',
         "opts": [
             'It retells the exact same story',
             'It contradicts Ja 18 directly',
             "It continues Ja 18's critique of sacrifice, applied to a different specific case (a vow before a journey)",
             'It has no relationship to Ja 18',
         ],
         "correct": 2,
         "expl": 'Together forming a short internal pair critiquing sacrificial practice from two angles.'},
        {"q": "What does the verse call 'the fool's bondage'?",
         "opts": [
             'Marriage',
             'Silence',
             'Wealth',
             'The kind of release the fool pursues through further sacrifice',
         ],
         "correct": 3,
         "expl": "Contrasted with how 'the attentive are released' — not through this paradoxical means."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Vowed Feast (Āyācitabhattajātaka)',
             'The Reed Drink',
             'Gales',
             'The Feast for the Dead',
         ],
         "correct": 0,
         "expl": 'The nineteenth poem overall, and the ninth of the Sīlavagga.'},
        {"q": "Why does this reading guide rate this poem's difficulty higher than most others in this chapter?",
         "opts": [
             'Because it is unusually long',
             "Because its deliberately paradoxical wordplay requires the comment's separate paraphrase to fully understand",
             'Because it uses an unusual meter',
             'Because no translation exists',
         ],
         "correct": 1,
         "expl": "One of the more overtly difficult verses in this collection's whole partial selection."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The ninth poem of the Sīlavagga, following Ja 11 through Ja 18',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'The second-to-last poem of this ten-poem chapter.'},
        {"q": "What two occasions for sacrifice does this poem's underlying story involve?",
         "opts": [
             'A wedding and a funeral',
             'No occasions are specified',
             'Two harvest festivals',
             'One sacrifice to ensure a safe voyage, and a second vowed sacrifice to release him from the first',
         ],
         "correct": 3,
         "expl": "The verse's paradox turns on this second, apparently liberating sacrifice actually creating further bondage."},
    ],
    marginalia=[
        ("A riddle the translator admits is a riddle", [
            "Sujato translates literally, then explains separately —",
            "the verse alone won't give up its meaning"
        ]),
        ("Release that only binds tighter", [
            "a second sacrifice, meant to free him —",
            "the verse says it does the opposite"
        ]),
        ("Two poems, one target", [
            "Ja 18's feast, this poem's vow —",
            "sacrifice critiqued from two directions"
        ]),
        ("The fool's own kind of freedom", [
            "not real release, just further bondage —",
            "the attentive find a different way"
        ]),
    ],
    further=[
        '<a href="%s/ja19/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-18.html">Ja 18 &mdash; The Feast for the '
        "Dead</a> &mdash; this poem's companion in critiquing "
        "sacrificial practice.",
        '<a href="ja-20.html">Ja 20 &mdash; The Reed Drink</a> '
        "&mdash; the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 20 — Naḷapāna (The Reed Drink)
# --------------------------------------------------------------------------- #
page(
    20, "Na&#7789;ap&amacr;na", "The Reed Drink",
    meta_title="Ja 20 — The Reed Drink | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 20, closing the Sīlavagga — a verse of collective "
        "ingenuity outwitting a lake monster by drinking through "
        "hollow reeds. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Two (Sīlavagga) &middot; Poem 10 of 10 (closing the chapter)",
    glance=[
        ("Setting", "A group speaking together, warning a hidden "
                    "danger by a body of water"),
        ("Speaker", "A collective &lsquo;we&rsquo;, per the "
                    "commentarial story, animals led by the "
                    "Bodhisatta"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of practical ingenuity"),
    ],
    why=(
        "This poem closes the Sīlavagga on a note of collective, "
        "practical wisdom &mdash; noticing danger through simple "
        "observation, and solving it through method rather than force "
        "&mdash; before the source text's own untranslated closing "
        "summary verse names all ten poems of this chapter in "
        "sequence."),
    guide=[
        ("Danger read from footprints, and outwitted by method", [
            "The verse states the observation and the solution "
            "together: &lsquo;seeing footprints go down into the "
            "water, and none that return, we shall drink water "
            "through a reed: no way shall you kill me.&rsquo; The "
            "logic is entirely practical &mdash; tracks entering the "
            "water with none coming back out are proof enough of "
            "danger, and the response is not to avoid the water "
            "altogether but to find a way around the danger itself."]),
        ("A monster in the lake, and a collective solution", [
            "Per Sujato's comment, a monster dwells in the lake, but "
            "the Bodhisatta thwarts it and keeps his people safe by "
            "having them drink through long hollow reeds rather than "
            "bending down to the water's surface &mdash; solving the "
            "danger through ingenuity rather than confrontation."]),
        ("Closing the Sīlavagga", [
            "This poem closes the Sīlavagga, the second of eight "
            "chapters this site's selection draws from within the "
            "Ekakanipāta. The source text's own untranslated summary "
            "verse (uddāna) immediately follows, naming all ten poems "
            "of this chapter in sequence &mdash; not presented here "
            "as quoted text, since it carries no separate translation, "
            "but noted for completeness, just as at the close of the "
            "previous chapter (Ja 10)."]),
    ],
    terms=[
        ("padamanuttiṇṇaṁ",
         "&ldquo;footprints go down into the water&rdquo; &mdash; "
         "the observed evidence of danger the verse opens with."),
        ("naḷena vāriṁ pissāma",
         "&ldquo;we shall drink water through a reed&rdquo; "
         "&mdash; the collective, practical solution the verse "
         "proposes."),
        ("neva maṁ tvaṁ vadhissasi",
         "&ldquo;no way shall you kill me&rdquo; &mdash; the verse's "
         "direct address to the danger itself, defeated by method "
         "rather than confrontation."),
        ("Naḷapānajātaka",
         "the traditional title of this tale, &lsquo;The Reed "
         "Drink&rsquo;, closing the Sīlavagga."),
        ("Sīlavaggo dutiyo",
         "&ldquo;the Sīlavagga, the second [chapter]&rdquo; &mdash; "
         "the source text's own untranslated closing marker for this "
         "chapter, followed immediately by its summary verse."),
    ],
    text_intro=(
        "The text in full: a single verse. The chapter's own "
        "untranslated closing summary verse (uddāna), which follows "
        "immediately in the source text, is not quoted here since it "
        "carries no English translation, but its content &mdash; the "
        "ten poem titles of this chapter in sequence &mdash; matches "
        "this reading guide's own further reading list below. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja20:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What evidence of danger does the verse open with?',
         "opts": [
             'A warning from another animal',
             'No specific evidence is mentioned',
             'A strange sound from the water',
             'Footprints going down into the water, with none that return',
         ],
         "correct": 3,
         "expl": 'Simple observation providing proof enough of danger.'},
        {"q": 'What solution does the verse propose?',
         "opts": [
             'Drinking water through a reed, rather than bending down to the surface',
             'Fighting the danger directly',
             'Waiting until the danger leaves',
             'Avoiding the water entirely',
         ],
         "correct": 0,
         "expl": 'Solving the danger through ingenuity rather than confrontation or avoidance.'},
        {"q": "What does Sujato's comment say lives in the lake?",
         "opts": [
             'A group of fish',
             'A monster',
             'A rival herd',
             'The comment does not specify',
         ],
         "correct": 1,
         "expl": "Thwarted by the Bodhisatta's practical solution rather than direct confrontation."},
        {"q": 'Who proposes and carries out the solution, per the commentarial story?',
         "opts": [
             'No solution is actually carried out',
             'A single individual acting alone',
             'The Bodhisatta, keeping his people safe collectively',
             'The monster itself',
         ],
         "correct": 2,
         "expl": "Matching the verse's own collective 'we shall drink water through a reed'."},
        {"q": 'What chapter does this poem close?',
         "opts": [
             'The final chapter of the whole Jātaka',
             'It does not close a chapter',
             'The Apaṇṇakavagga',
             "The Sīlavagga, the second of eight chapters this site's selection draws from",
         ],
         "correct": 3,
         "expl": "The source text's own untranslated summary verse (uddāna) follows immediately after."},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'No — it carries no separate English translation, so it is only noted for completeness',
             'It does not exist for this chapter',
             'It is presented as spoken by the Buddha',
             'Yes, quoted in full',
         ],
         "correct": 0,
         "expl": 'Consistent with the same practice at the close of the previous chapter, Ja 10.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Vowed Feast',
             'The Reed Drink (Naḷapānajātaka)',
             'The Feast for the Dead',
             'Gales',
         ],
         "correct": 1,
         "expl": 'The twentieth poem overall, and the tenth and final poem of the Sīlavagga.'},
        {"q": "How does the verse's problem-solving approach compare to force or direct confrontation?",
         "opts": [
             'It relies on simply ignoring the danger',
             'It relies entirely on force',
             'It relies on practical ingenuity — finding a way around the danger rather than confronting it directly',
             'It relies on prayer alone',
         ],
         "correct": 2,
         "expl": "The reed-drinking method avoids the danger's reach entirely."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The first poem of a later chapter',
             'The first poem of the Sīlavagga',
             'The tenth and final poem of the Sīlavagga, closing this chapter',
         ],
         "correct": 3,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse following immediately after."},
        {"q": "What broader quality does this poem's solution illustrate, closing out the Sīlavagga's ethical theme?",
         "opts": [
             'Practical wisdom and care for the safety of the group',
             'Individual heroism alone',
             'Resignation to fate',
             'Blind courage',
         ],
         "correct": 0,
         "expl": "Echoing the chapter's opening poem, Ja 11, on virtue and protection extended to others."},
    ],
    marginalia=[
        ("Tracks that never come back", [
            "proof enough, without a single word from the water —",
            "danger read plainly, from footprints alone"
        ]),
        ("A reed instead of a fight", [
            "no confrontation needed —",
            "just a way around what waits below"
        ]),
        ("Safety, kept collective", [
            "'we shall drink', not 'I alone will' —",
            "the whole group protected by one idea"
        ]),
        ("Ten poems, one chapter closed", [
            "the Sīlavagga's own summary follows —",
            "not quoted, since it has no translation"
        ]),
    ],
    further=[
        '<a href="%s/ja20/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-19.html">Ja 19 &mdash; The Vowed Feast</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 21 — Kuruṅgamiga (The Four-horned Antelope)
# --------------------------------------------------------------------------- #
page(
    21, "Kuru&#7749;gamiga", "The Four-horned Antelope",
    meta_title="Ja 21 — The Four-horned Antelope | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 21, opening the Kuruṅgavagga — a wary antelope's "
        "verse refusing bait from a hidden hunter. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "An antelope addressing a hunter hidden in a "
                    "tree"),
        ("Speaker", "The four-horned antelope"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of alert self-preservation"),
    ],
    why=(
        "This verse opens the Kuruṅgavagga with a model of wariness "
        "rewarded: the antelope sees through a hunter's disguise and "
        "simply declines the trap, without confrontation or drama "
        "&mdash; Sujato's comment grounds the animal itself in a "
        "specific, real species and its documented natural "
        "behavior."),
    guide=[
        ("Seeing through a trap, and simply walking away", [
            "The verse is spoken directly to the hidden hunter: "
            "&lsquo;the four-horned antelope knows that it's you who "
            "tosses fruit from the beechwood tree. I'll go to another "
            "beechwood, I don't like your fruit.&rsquo; Per Sujato's "
            "comment, a wary antelope spots a hunter hiding in a tree "
            "dropping bait, and simply seeks food elsewhere rather "
            "than confronting the danger directly."]),
        ("A specific, documented animal and tree", [
            "Sujato's comment identifies the &lsquo;kuruṅga&rsquo; as "
            "the four-horned antelope (Tetracerus quadricornis), "
            "citing the Mṛgapakṣiśāstra's description of it as short "
            "and red, with branched horns, wide eyes, shrewd and "
            "patient, grazing mostly on grass &mdash; and the "
            "&lsquo;sepaṇṇi&rsquo; as the beechwood or gamhar tree "
            "(Gmelina arborea), which grows to 30 metres and bears "
            "edible fruit. This kind of concrete natural detail "
            "grounds the verse's simple lesson in an identifiable "
            "real setting."]),
    ],
    terms=[
        ("kuruṅga",
         "the four-horned antelope (Tetracerus quadricornis), per "
         "Sujato's comment described in the Mṛgapakṣiśāstra as "
         "shrewd and patient."),
        ("sepaṇṇi",
         "the beechwood or gamhar tree (Gmelina arborea), whose "
         "fruit the hunter uses as bait."),
        ("na me te ruccate phalaṁ",
         "&ldquo;I don't like your fruit&rdquo; &mdash; the "
         "antelope's plain, undramatic refusal."),
        ("Kuruṅgamigajātaka",
         "the traditional title of this tale, opening the "
         "Kuruṅgavagga."),
        ("Mṛgapakṣiśāstra",
         "a medieval Sanskrit text on animals and birds, cited "
         "repeatedly in Sujato's comments across this chapter for "
         "naturalist detail."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja21:1.1-1.4"),
    ],
    quiz=[
        {"q": 'Who is the verse addressed to?',
         "opts": [
             'A fellow antelope',
             'A hunter hidden in a tree, dropping bait',
             'A king',
             'No addressee is named',
         ],
         "correct": 0,
         "expl": "'The four-horned antelope knows that it's you who tosses fruit from the beechwood tree.'"},
        {"q": 'How does the antelope respond to recognizing the trap?',
         "opts": [
             'By confronting the hunter directly',
             'By simply going to another beechwood tree instead',
             'By warning other animals loudly',
             'By eating the bait anyway',
         ],
         "correct": 1,
         "expl": 'A model of wariness rewarded, without confrontation or drama.'},
        {"q": "What species does Sujato's comment identify the 'kuruṅga' as?",
         "opts": [
             'A type of goat',
             'A type of deer with no specific identification',
             'The four-horned antelope (Tetracerus quadricornis)',
             'A wild boar',
         ],
         "correct": 2,
         "expl": 'Described in the cited Mṛgapakṣiśāstra as shrewd and patient.'},
        {"q": "What tree does the comment identify as the 'sepaṇṇi'?",
         "opts": [
             'A palm tree',
             'No specific tree is identified',
             'A banyan tree',
             'The beechwood or gamhar tree (Gmelina arborea)',
         ],
         "correct": 3,
         "expl": 'Growing to 30 metres and bearing edible fruit, used here as bait.'},
        {"q": "What medieval text does Sujato's comment cite for naturalist detail about the antelope?",
         "opts": [
             'The Mṛgapakṣiśāstra',
             'The Rig Veda',
             'No text is cited',
             'The Arthaśāstra',
         ],
         "correct": 0,
         "expl": "Cited repeatedly across this chapter's comments for naturalist detail."},
        {"q": 'What chapter does this poem open?',
         "opts": [
             'The Sīlavagga',
             'The Kuruṅgavagga',
             'The Kulāvakavagga',
             'It does not open a chapter',
         ],
         "correct": 1,
         "expl": "This collection's third ten-poem chapter."},
        {"q": "What quality does the verse model in the antelope's behavior?",
         "opts": [
             'Indifference to danger',
             'Aggression toward danger',
             'Wariness and calm self-preservation',
             'Recklessness',
         ],
         "correct": 2,
         "expl": 'Recognizing danger and simply avoiding it, without unnecessary confrontation.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             "The King's Thoroughbred",
             'Fords',
             'Hounds',
             'The Four-horned Antelope (Kuruṅgamigajātaka)',
         ],
         "correct": 3,
         "expl": 'The twenty-first poem overall, and the first of the Kuruṅgavagga.'},
        {"q": "What does the antelope's final line state plainly?",
         "opts": [
             "'I don't like your fruit' — a simple, undramatic refusal",
             'A request for help',
             'A promise to return later',
             'A threat against the hunter',
         ],
         "correct": 0,
         "expl": 'Ending the encounter without conflict.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of the Sīlavagga',
             'The first poem of the third chapter (Kuruṅgavagga), following the completed Sīlavagga',
             'It stands outside any chapter',
             'The final poem of the Kuruṅgavagga',
         ],
         "correct": 1,
         "expl": "Opening this collection's third ten-poem chapter."},
    ],
    marginalia=[
        ("A trap seen through, not sprung", [
            "no confrontation, just a quiet refusal —",
            "'I'll go to another beechwood'"
        ]),
        ("A real animal, precisely described", [
            "short, red, branch-horned, patient —",
            "grounded in documented naturalist detail"
        ]),
        ("Opening the third chapter", [
            "Kuruṅgavagga begins with wariness rewarded —",
            "ten more poems of animal wisdom follow"
        ]),
        ("Bait recognized for what it is", [
            "fruit from a tree, dropped by a hidden hand —",
            "the antelope simply isn't fooled"
        ]),
    ],
    further=[
        '<a href="%s/ja21/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-20.html">Ja 20 &mdash; The Reed Drink</a> '
        "&mdash; the closing poem of the previous chapter.",
        '<a href="ja-22.html">Ja 22 &mdash; Hounds</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 22 — Kukkura (Hounds)
# --------------------------------------------------------------------------- #
page(
    22, "Kukkura", "Hounds",
    meta_title="Ja 22 — Hounds | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 22 — a wild dog's protest against the unjust killing "
        "of the weak for the crimes of the privileged. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "A protest, spoken on behalf of wild dogs facing "
                    "unjust punishment"),
        ("Speaker", "The Bodhisatta, born as a leader of a pack of "
                    "dogs"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short protest verse"),
    ],
    why=(
        "This verse gives voice to a plain and still-relevant "
        "grievance: that the powerful escape consequences for their "
        "own wrongdoing while the powerless are punished in their "
        "place. Sujato's own comment identifies the story's setting "
        "&mdash; a cemetery dog-pack leader speaking against the "
        "court's own pedigreed hounds &mdash; as the real target of "
        "the protest."),
    guide=[
        ("A protest against punishing the wrong party", [
            "The verse states its grievance directly: &lsquo;the "
            "hounds raised in the royal family, pedigreed, handsome "
            "and strong, are not slaughtered, we are slaughtered "
            "&mdash; this is not the dogs deserving death, this is "
            "the killing of the weak.&rsquo; Per Sujato's comment, "
            "the Bodhisatta, born as the leader of a pack of dogs "
            "living in a cemetery, protests the unjust slaughter of "
            "wild dogs when it is actually the fancy hounds of the "
            "royal court who are responsible for the wrongdoing being "
            "punished."]),
        ("A grievance about power and consequence", [
            "The verse's underlying logic is not really about dogs at "
            "all: it names a pattern where those with status and "
            "protection (&lsquo;raised in the royal family, "
            "pedigreed&rsquo;) escape the consequences of their own "
            "actions, while those without such standing bear "
            "punishment meant for someone else entirely."]),
    ],
    terms=[
        ("koleyyakā",
         "&ldquo;pedigreed&rdquo; &mdash; per Sujato's comment, a "
         "term also found at this site's own AN 7.63, describing the "
         "privileged royal hounds."),
        ("teme na vajjhā mayamasma vajjhā",
         "&ldquo;they are not slaughtered, we are slaughtered&rdquo; "
         "&mdash; the verse's stark central complaint."),
        ("dubbalaghātikāyaṁ",
         "&ldquo;the killing of the weak&rdquo; &mdash; the verse's "
         "closing description of what is actually happening, "
         "against the pretense of justice."),
        ("Kukkurajātaka",
         "the traditional title of this tale, &lsquo;Hounds&rsquo;."),
        ("Bodhisatta",
         "the Buddha-to-be in this and other Jātaka tales; here, "
         "born as the leader of a cemetery-dwelling pack of dogs."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja22:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What grievance does the verse state?',
         "opts": [
             'That all dogs should be treated equally well',
             "That the royal family's pedigreed hounds are not slaughtered while others are, though it is the pedigreed hounds who did wrong",
             'That dogs should not be kept as pets',
             'No specific grievance is stated',
         ],
         "correct": 1,
         "expl": "'This is not the dogs deserving death, this is the killing of the weak.'"},
        {"q": "Where, per Sujato's comment, was the Bodhisatta born in this story?",
         "opts": [
             'As a human observer',
             'In the royal palace',
             'As the leader of a pack of dogs living in a cemetery',
             'As a single stray dog with no pack',
         ],
         "correct": 2,
         "expl": 'Protesting the unjust slaughter of dogs like himself.'},
        {"q": 'Who is actually responsible for the wrongdoing being punished, per the story?',
         "opts": [
             'A group of hunters',
             'The story does not specify',
             'The wild dogs themselves',
             "The royal court's own pedigreed hounds",
         ],
         "correct": 3,
         "expl": 'The wild dogs are punished in their place, despite being innocent.'},
        {"q": "What already-completed page on this site does Sujato's comment cite for the term 'koleyyakā' (pedigreed)?",
         "opts": [
             'AN 7.63',
             'SN 9.8',
             'No cross-reference is given',
             'MN 51',
         ],
         "correct": 0,
         "expl": "A linguistic cross-reference for the term's usage."},
        {"q": "What broader pattern does this verse's grievance describe?",
         "opts": [
             'A pattern specific only to dogs',
             'The powerful escaping consequences for their own wrongdoing while the powerless are punished instead',
             'A pattern of animal loyalty',
             'No broader pattern is implied',
         ],
         "correct": 1,
         "expl": "The verse's underlying point extends well beyond the literal dogs it describes."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Fords',
             'The Four-horned Antelope',
             'Hounds (Kukkurajātaka)',
             "The King's Thoroughbred",
         ],
         "correct": 2,
         "expl": 'The twenty-second poem overall, and the second of the Kuruṅgavagga.'},
        {"q": "How does the verse describe the royal family's own hounds?",
         "opts": [
             'As wild and untrained',
             'The verse does not describe them',
             'As poorly treated',
             'As pedigreed, handsome, and strong',
         ],
         "correct": 3,
         "expl": 'Contrasted directly with the wild dogs facing unjust punishment.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The second poem of the Kuruṅgavagga, following Ja 21',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Kuruṅgavagga.'},
        {"q": 'What tone does this verse take — resigned or protesting?',
         "opts": [
             'Entirely resigned, with no objection raised',
             'Directly protesting, naming the injustice plainly',
             'Celebratory',
             'Indifferent',
         ],
         "correct": 1,
         "expl": 'A clear, pointed statement of grievance rather than passive acceptance.'},
        {"q": "What does this verse's protest still resonate with, beyond its literal setting?",
         "opts": [
             'A specific legal code no longer in use',
             'Nothing beyond the literal story',
             'A still-relevant grievance about status shielding the privileged from consequence',
             'A purely historical curiosity with no modern relevance',
         ],
         "correct": 2,
         "expl": "Noted in this reading guide's own framing of the verse's underlying logic."},
    ],
    marginalia=[
        ("Punished for someone else's crime", [
            "the pedigreed hounds go free —",
            "the wild dogs pay the price instead"
        ]),
        ("A cemetery-dwelling protest", [
            "the Bodhisatta, leader of the unwanted pack —",
            "speaking plainly against injustice"
        ]),
        ("Status shielding the guilty", [
            "'raised in the royal family' means safety —",
            "the weak bear what the strong deserve"
        ]),
        ("A grievance that still lands", [
            "not really about dogs at all —",
            "a pattern recognizable well beyond this tale"
        ]),
    ],
    further=[
        '<a href="%s/ja22/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../anguttara-nikaya/an-7.63.html">AN 7.63 &mdash; '
        "Kinds of Wives</a> &mdash; cited in Sujato's comment for the "
        "term 'koleyyakā'.",
        '<a href="ja-21.html">Ja 21 &mdash; The Four-horned '
        "Antelope</a> &mdash; the poem immediately before this one.",
        "<a href=\"ja-23.html\">Ja 23 &mdash; The King's "
        "Thoroughbred</a> &mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 23 — Bhojājānīya (The King's Thoroughbred)
# --------------------------------------------------------------------------- #
page(
    23, "Bhoj&amacr;j&amacr;n&imacr;ya", "The King's Thoroughbred",
    meta_title="Ja 23 — The King's Thoroughbred | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 23 — a wounded warhorse's own plea to fight on, the "
        "first half of a matched pair with the next poem. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "A battlefield, a warhorse pierced by arrows"),
        ("Speaker", "The wounded warhorse itself, addressing its "
                    "rider"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of resolute determination"),
    ],
    why=(
        "This verse begins a matched pair with the next poem, Ja 24 "
        "&mdash; both give voice to a warhorse's own unbroken resolve "
        "under fire, and Sujato's comment on the companion poem "
        "explicitly notes the similarity: &lsquo;similar to the "
        "previous story, a warhorse declares its determination to go "
        "on.&rsquo;"),
    guide=[
        ("A wounded horse asking to be sent back into battle", [
            "The verse gives the warhorse its own voice: &lsquo;though "
            "lying on my side, pierced by many arrows, the king's "
            "stallion beats a gelding &mdash; harness me now, "
            "charioteer.&rsquo; Per Sujato's comment, a wounded "
            "warhorse urges its rider to take one last stand, "
            "confident that even wounded, a thoroughbred outperforms "
            "an ordinary horse."]),
        ("A technical note on an unusual grammatical form", [
            "Sujato's comment flags that &lsquo;vaḷavā&rsquo; is "
            "normally the word for &lsquo;mare&rsquo;, but here "
            "appears in a masculine ablative form, glossed elsewhere "
            "with a term for &lsquo;wild colt&rsquo; &mdash; a "
            "grammatical detail that shapes how the comparison "
            "between the wounded thoroughbred and an ordinary horse "
            "should actually be read."]),
    ],
    terms=[
        ("sallalīkato",
         "&ldquo;pierced by many arrows&rdquo; &mdash; the "
         "warhorse's own wounded condition."),
        ("vaḷavā bhojjo",
         "&ldquo;the king's stallion... a gelding&rdquo; &mdash; per "
         "Sujato's comment, an unusual grammatical construction "
         "comparing the wounded thoroughbred favorably to an "
         "ordinary horse."),
        ("yuñja maññeva sārathī",
         "&ldquo;harness me now, charioteer&rdquo; &mdash; the "
         "warhorse's own direct request."),
        ("Bhojājānīyajātaka",
         "the traditional title of this tale, &lsquo;The King's "
         "Thoroughbred&rsquo;."),
        ("Ja 24",
         "the next poem in this chapter, explicitly noted by "
         "Sujato's own comment as similar to this one."),
    ],
    text_intro=(
        "The text in full: a single verse, with a technical "
        "grammatical note discussed above. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja23:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What condition is the warhorse in when it speaks this verse?',
         "opts": [
             'Its condition is not described',
             'Fully healthy and rested',
             'Lying on its side, pierced by many arrows',
             'Already dead',
         ],
         "correct": 2,
         "expl": 'Yet still requesting to be sent back into battle.'},
        {"q": 'What does the warhorse ask its rider to do?',
         "opts": [
             'Find a replacement horse',
             'Rest before continuing',
             'Retreat immediately',
             'Harness it now, for one last stand',
         ],
         "correct": 3,
         "expl": 'Confident that even wounded, it outperforms an ordinary horse.'},
        {"q": "What does Sujato's comment say about this poem's relationship to Ja 24?",
         "opts": [
             "Ja 24's comment explicitly notes it is 'similar to the previous story' — both are warhorses declaring determination",
             'Ja 24 contradicts this poem directly',
             'Ja 24 was written far earlier',
             'They are unrelated',
         ],
         "correct": 0,
         "expl": 'A matched pair of warhorse-resolve poems.'},
        {"q": "What grammatical detail does Sujato's comment flag about 'vaḷavā'?",
         "opts": [
             'No unusual grammar is present',
             "Though normally meaning 'mare', it appears here in a masculine ablative form glossed with 'wild colt'",
             'It is a proper name',
             'It is a foreign loanword',
         ],
         "correct": 1,
         "expl": 'Shaping how the comparison between the wounded thoroughbred and an ordinary horse should be read.'},
        {"q": 'What comparison does the verse draw about the wounded warhorse?',
         "opts": [
             'No comparison is drawn',
             'That it is now useless',
             'That even wounded, it still beats an ordinary horse (gelding)',
             'That it should be retired',
         ],
         "correct": 2,
         "expl": 'The basis for its confident request to be sent back into the fight.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Thoroughbred',
             'Fords',
             'Hounds',
             "The King's Thoroughbred (Bhojājānīyajātaka)",
         ],
         "correct": 3,
         "expl": 'The twenty-third poem overall, and the third of the Kuruṅgavagga — not to be confused with the similarly-named next poem.'},
        {"q": 'Who speaks this verse?',
         "opts": [
             'The warhorse itself',
             'The king',
             'An unnamed narrator',
             'The charioteer',
         ],
         "correct": 0,
         "expl": "Giving voice directly to the wounded animal's own resolve."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The third poem of the Kuruṅgavagga, following Ja 21 and Ja 22',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Immediately followed by its thematically matched companion, Ja 24.'},
        {"q": "What quality does this verse's warhorse model?",
         "opts": [
             'Anger at its rider',
             'Fear and retreat',
             'Unbroken resolve and determination despite injury',
             'Indifference to the battle',
         ],
         "correct": 2,
         "expl": 'A quality the next poem, Ja 24, develops further with a different warhorse.'},
        {"q": "What does 'Bhoja' refer to, per Sujato's comment?",
         "opts": [
             'A type of weapon',
             'The comment does not address this term',
             'A place name only',
             'A common name or term for a king',
         ],
         "correct": 3,
         "expl": "Giving this poem its traditional title, 'The King's Thoroughbred'."},
    ],
    marginalia=[
        ("Pierced, but not finished", [
            "lying on its side, arrows still in it —",
            "still asking to be harnessed again"
        ]),
        ("A wounded champion, still favored", [
            "even hurt, better than an unwounded ordinary horse —",
            "the verse's whole claim in one comparison"
        ]),
        ("The first half of a matched pair", [
            "the same resolve returns in the next poem —",
            "Sujato's comment confirms the echo"
        ]),
        ("One last stand, requested plainly", [
            "no complaint, no hesitation —",
            "'harness me now, charioteer'"
        ]),
    ],
    further=[
        '<a href="%s/ja23/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-22.html\">Ja 22 &mdash; Hounds</a> &mdash; the "
        "poem immediately before this one.",
        '<a href="ja-24.html">Ja 24 &mdash; The Thoroughbred</a> '
        "&mdash; this poem's matched companion.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 24 — Ājañña (The Thoroughbred)
# --------------------------------------------------------------------------- #
page(
    24, "&Amacr;ja&ntilde;&ntilde;a", "The Thoroughbred",
    meta_title="Ja 24 — The Thoroughbred | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 24 — a second warhorse's declaration of unbroken "
        "drive, matching the previous poem and playing with repeated "
        "words. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "A warhorse, per the commentarial story, "
                    "declaring its own determination"),
        ("Form", "One four-line stanza, built almost entirely on "
                 "repetition"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "unusual repetitive structure, simple point"),
    ],
    why=(
        "Where the previous poem, Ja 23, gave a wounded warhorse's "
        "direct plea, this companion poem makes essentially the same "
        "point through an unusual and striking device: its opening "
        "two lines are built almost entirely from the repetition of "
        "just four words, an emphatic style rare in this "
        "collection."),
    guide=[
        ("A thoroughbred that keeps going, wherever and whenever", [
            "The verse's opening lines pile up repetition for "
            "emphasis: &lsquo;whenever whenever, wherever whenever, "
            "wherever wherever, whenever whenever&rsquo; &mdash; "
            "before landing its point: &lsquo;the thoroughbred drives "
            "onward, while the geldings fade right there.&rsquo; Per "
            "Sujato's comment, this is, like the previous poem, "
            "&lsquo;a warhorse declares its determination to go "
            "on.&rsquo;"]),
        ("An unusual grammatical form matching its companion poem", [
            "Sujato's comment notes that &lsquo;vāḷavā&rsquo; here is "
            "a masculine nominative plural, a secondary derivation "
            "related to &lsquo;mare&rsquo; but understood as "
            "&lsquo;reckoned as ordinary horses&rsquo; &mdash; the "
            "same underlying grammatical pattern already discussed at "
            "Ja 23, reinforcing that these two poems share not just a "
            "theme but specific technical vocabulary."]),
    ],
    terms=[
        ("yadā yadā yattha yadā",
         "&ldquo;whenever whenever, wherever whenever&rdquo; "
         "&mdash; the verse's striking opening repetition, building "
         "emphasis before its point."),
        ("ājañño kurute vegaṁ",
         "&ldquo;the thoroughbred drives onward&rdquo; &mdash; the "
         "verse's central claim."),
        ("hāyanti tattha vāḷavā",
         "&ldquo;the geldings fade right there&rdquo; &mdash; the "
         "verse's contrasting close."),
        ("Ājaññajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Thoroughbred&rsquo; &mdash; not to be confused with the "
         "similarly named previous poem, Ja 23, The King's "
         "Thoroughbred."),
        ("Ja 23",
         "the previous poem in this chapter, explicitly identified "
         "by Sujato's own comment as this poem's close companion."),
    ],
    text_intro=(
        "The text in full: a single verse, built on unusual repeated "
        "phrasing, discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja24:1.1-1.4"),
    ],
    quiz=[
        {"q": "What unusual device does this verse's opening two lines use?",
         "opts": [
             'A dialogue between two speakers',
             'No unusual device is used',
             'A rhyme scheme unique in this collection',
             'Heavy repetition of just four words, piled up for emphasis',
         ],
         "correct": 3,
         "expl": "'Whenever whenever, wherever whenever, wherever wherever, whenever whenever.'"},
        {"q": 'What does the verse claim about the thoroughbred, compared to ordinary horses?',
         "opts": [
             'That it drives onward while the geldings fade',
             'That it is slower but steadier',
             'No comparison is made',
             'That it tires just as quickly',
         ],
         "correct": 0,
         "expl": "The verse's central point, following the repetitive buildup."},
        {"q": "What does Sujato's comment say about this poem's relationship to Ja 23?",
         "opts": [
             'They are entirely unrelated',
             "Sujato's comment describes this poem as 'similar to the previous story' — both are warhorses declaring determination",
             'This poem predates Ja 23',
             'They tell contradictory stories',
         ],
         "correct": 1,
         "expl": 'A close companion poem, matching theme and technical vocabulary.'},
        {"q": "What grammatical detail does Sujato's comment note about 'vāḷavā' here?",
         "opts": [
             'A proper name',
             'No grammatical detail is noted',
             "A masculine nominative plural, a secondary derivation related to 'mare' but meaning ordinary horses",
             'A completely unrelated word with no connection to Ja 23',
         ],
         "correct": 2,
         "expl": 'The same underlying grammatical pattern already discussed at Ja 23, reinforcing the shared vocabulary between the two poems.'},
        {"q": "How should this poem's title be distinguished from Ja 23's?",
         "opts": [
             'This poem has no traditional title',
             'Ja 23 has no traditional title',
             'They are identical titles with no distinction needed',
             "Ja 23 is 'The King's Thoroughbred'; this poem is simply 'The Thoroughbred' — similarly named but separate poems",
         ],
         "correct": 3,
         "expl": 'Both concern warhorses, but are distinct poems with distinct (if similar) titles.'},
        {"q": 'What is the overall point of this verse?',
         "opts": [
             "That a true thoroughbred's drive persists in any circumstance, unlike an ordinary horse",
             'That circumstances alone determine performance',
             'That horses should not be used in battle',
             'That all horses perform equally',
         ],
         "correct": 0,
         "expl": 'Matching the resolve theme of its companion poem, Ja 23.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             "The King's Thoroughbred",
             'The Thoroughbred (Ājaññajātaka)',
             'Fords',
             'The Elephant Named Ladyface',
         ],
         "correct": 1,
         "expl": 'The twenty-fourth poem overall, and the fourth of the Kuruṅgavagga.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fourth poem of the Kuruṅgavagga, immediately following its companion poem Ja 23',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Kuruṅgavagga.'},
        {"q": "How does this verse's structure differ from most other poems in this collection?",
         "opts": [
             'It is written entirely in prose',
             'It contains no verbs',
             'It does not differ at all',
             'It relies unusually heavily on repeated words for its emphasis, rather than varied imagery',
         ],
         "correct": 3,
         "expl": "Flagged directly in this reading guide's own form and difficulty notes."},
        {"q": "What word describes horses that 'fade' compared to the thoroughbred?",
         "opts": [
             'Geldings (vāḷavā)',
             'Foals',
             'Mares specifically',
             'Stallions',
         ],
         "correct": 0,
         "expl": 'Contrasted with the enduring thoroughbred throughout both this poem and its companion, Ja 23.'},
    ],
    marginalia=[
        ("Repetition building to a point", [
            "whenever, wherever, four words piled up —",
            "then the claim: the thoroughbred never fades"
        ]),
        ("A companion poem, confirmed", [
            "Sujato's own comment says so directly —",
            "the same resolve, a different horse"
        ]),
        ("Shared grammar, shared theme", [
            "the same unusual word form as Ja 23 —",
            "two poems built from matching materials"
        ]),
        ("Two similarly named poems, kept distinct", [
            "'The King's Thoroughbred' and 'The Thoroughbred' —",
            "close cousins, not the same poem twice"
        ]),
    ],
    further=[
        '<a href="%s/ja24/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-23.html\">Ja 23 &mdash; The King's "
        "Thoroughbred</a> &mdash; this poem's close companion, "
        "immediately before it.",
        '<a href="ja-25.html">Ja 25 &mdash; Fords</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 25 — Tittha (Fords)
# --------------------------------------------------------------------------- #
page(
    25, "Tittha", "Fords",
    meta_title="Ja 25 — Fords | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 25 — a canny horse-keeper's insight, paired with a "
        "brief closing observation about overeating. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself, "
                    "addressed to a 'rider' (sārathi)"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse pairing two loosely related "
                       "observations"),
    ],
    why=(
        "This poem pairs a practical observation about a fussy "
        "horse's changing preferences with a second, only loosely "
        "connected remark about overeating &mdash; an example of how "
        "these terse single-verse tales can carry more than one idea "
        "at once, without spelling out how they relate."),
    guide=[
        ("A canny keeper's practical adjustment", [
            "The verse's first half is a simple instruction: "
            "&lsquo;at one ford or another, lead the horse to drink, "
            "rider.&rsquo; Per Sujato's comment, when a fussy horse "
            "refuses to drink at one ford, its canny keeper realizes "
            "the problem is not the horse's thirst but the specific "
            "location, and simply looks elsewhere."]),
        ("A second observation about excess", [
            "The verse's second half turns to a different point "
            "entirely: &lsquo;for a man who overeats, even milk-rice "
            "&mdash; a prized delicacy &mdash; becomes a torment.&rsquo; "
            "This reading guide presents both halves as the verse "
            "itself gives them, without asserting a specific "
            "connective logic beyond what the bare text supports; "
            "readers may notice their own resonance between a "
            "creature refusing what's wrong for it and a person "
            "spoiling even what's good through excess."]),
    ],
    terms=[
        ("tittha",
         "&ldquo;ford&rdquo; &mdash; a river crossing point, one of "
         "which the fussy horse eventually accepts."),
        ("accāsana",
         "&ldquo;overeating&rdquo; &mdash; per Sujato's comment, "
         "literally &lsquo;ati&rsquo; (over) plus &lsquo;asana&rsquo; "
         "(eating)."),
        ("pāyāsassapi tappati",
         "&ldquo;even milk-rice is a torment&rdquo; &mdash; the "
         "verse's closing point about how excess spoils even what is "
         "good."),
        ("Titthajātaka",
         "the traditional title of this tale, &lsquo;Fords&rsquo;."),
        ("sārathi",
         "&ldquo;rider&rdquo; (or charioteer) &mdash; the addressee "
         "of the verse's first-half instruction."),
    ],
    text_intro=(
        "The text in full: a single verse, pairing two loosely "
        "related observations, discussed above. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja25:1.1-1.4"),
    ],
    quiz=[
        {"q": "What practical problem does the verse's first half address?",
         "opts": [
             'A horse that refuses all food',
             'A horse refusing to drink at one particular ford',
             'A horse that will not be ridden',
             'No practical problem is addressed',
         ],
         "correct": 0,
         "expl": "'At one ford or another, lead the horse to drink, rider.'"},
        {"q": "What insight does the canny keeper have, per Sujato's comment?",
         "opts": [
             'That the horse is simply not thirsty',
             "That the problem is the specific location, not the horse's thirst, so he looks elsewhere",
             'That the horse needs to be punished',
             'That the horse should be replaced',
         ],
         "correct": 1,
         "expl": 'A simple adjustment rather than forcing the issue.'},
        {"q": "What does the verse's second half address?",
         "opts": [
             'A different animal entirely',
             'A description of the ford itself',
             'A completely unrelated topic — overeating spoiling even good food',
             "The same horse's diet specifically",
         ],
         "correct": 2,
         "expl": "'For a man who overeats, even milk-rice is a torment.'"},
        {"q": "Does this reading guide assert a specific logical connection between the verse's two halves?",
         "opts": [
             'The guide claims they are entirely unrelated',
             'The guide claims the second half is a later addition',
             'Yes, a definitive connection is asserted',
             'No — it presents both halves as given, without asserting a connective logic beyond what the text supports',
         ],
         "correct": 3,
         "expl": "Consistent with this collection's practice of not overclaiming meaning beyond the bare text."},
        {"q": "What does 'accāsana' mean, per Sujato's comment?",
         "opts": [
             "'Overeating' — literally 'over' plus 'eating'",
             'A type of food',
             'A place name',
             "'Under-eating'",
         ],
         "correct": 0,
         "expl": "Breaking down the term's literal construction."},
        {"q": "What is milk-rice (pāyāsa) generally regarded as, that makes the verse's point sharper?",
         "opts": [
             'A plain, ordinary food',
             'A prized delicacy, which even so becomes a torment when overeaten',
             'A punishment food',
             'An unusual, rarely eaten dish',
         ],
         "correct": 1,
         "expl": 'Even the best food becomes unpleasant in excess.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Frequent',
             'The Thoroughbred',
             'Fords (Titthajātaka)',
             'The Elephant Named Ladyface',
         ],
         "correct": 2,
         "expl": 'The twenty-fifth poem overall, and the fifth of the Kuruṅgavagga.'},
        {"q": "Who is addressed directly in the verse's first half?",
         "opts": [
             'The horse itself',
             'No one is addressed',
             'The king',
             'The rider (sārathi)',
         ],
         "correct": 3,
         "expl": 'Given the practical instruction to try a different ford.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The fifth poem of the Kuruṅgavagga, following Ja 21 through Ja 24',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Kuruṅgavagga.'},
        {"q": "What kind of resonance might a reader notice between the verse's two halves, without the guide asserting it as definitive?",
         "opts": [
             'No possible resonance exists',
             "A parallel between a creature refusing what's wrong for it and excess spoiling even what's good",
             'A resonance about royal authority',
             'A resonance about seasonal change',
         ],
         "correct": 1,
         "expl": "Offered as a possible reading, not an asserted fact about the verse's composition."},
    ],
    marginalia=[
        ("Not thirst, just the wrong ford", [
            "a canny keeper reads the real problem —",
            "and simply tries somewhere else"
        ]),
        ("Even a delicacy, ruined by excess", [
            "milk-rice, prized and still spoiled —",
            "too much undoes even the best thing"
        ]),
        ("Two observations, left unconnected", [
            "the verse doesn't explain the link —",
            "the reader is left to notice it, or not"
        ]),
        ("A short poem carrying two ideas", [
            "practical adjustment, then a warning about excess —",
            "more packed into four lines than it first appears"
        ]),
    ],
    further=[
        '<a href="%s/ja25/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-24.html">Ja 24 &mdash; The Thoroughbred</a> '
        "&mdash; the poem immediately before this one.",
        "<a href=\"ja-26.html\">Ja 26 &mdash; The Elephant Named "
        "Ladyface</a> &mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 26 — Mahiḷāmukha (The Elephant Named Ladyface)
# --------------------------------------------------------------------------- #
page(
    26, "Mahi&#7693;&amacr;mukha", "The Elephant Named Ladyface",
    meta_title="Ja 26 — The Elephant Named Ladyface | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 26 — a good-natured royal elephant corrupted by "
        "overheard bandit talk, and restored by overheard virtue. "
        "From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short contrast verse"),
    ],
    why=(
        "This tale gives a vivid image for a universal concern: how "
        "easily character can be shaped by what one merely overhears "
        "&mdash; a good-natured elephant turned violent by bandits' "
        "talk, then restored to virtue by the speech of the "
        "well-restrained, with no direct instruction involved either "
        "time."),
    guide=[
        ("Corrupted by overheard evil, restored by overheard virtue", [
            "The verse states its contrast directly: &lsquo;before, "
            "hearing the speech of the bandits, Ladyface went on a "
            "rampage. But hearing the speech of the well-restrained, "
            "the supreme elephant is established in all good "
            "qualities.&rsquo; Per Sujato's comment, a good-natured "
            "royal elephant was corrupted after overhearing bandits "
            "speaking evilly &mdash; and, the verse implies, was later "
            "restored by the reverse influence."]),
        ("Character shaped without direct instruction", [
            "In neither direction &mdash; corruption or restoration "
            "&mdash; is the elephant directly taught or trained; both "
            "changes happen simply through what it happens to "
            "overhear. The tale's underlying point concerns the "
            "quiet, cumulative power of environment and company on "
            "character, for better or worse."]),
    ],
    terms=[
        ("purāṇacorāna vaco",
         "&ldquo;the speech of the bandits&rdquo; &mdash; the "
         "corrupting influence the elephant first overhears."),
        ("susaññatānaṁ vaco",
         "&ldquo;the speech of the well-restrained&rdquo; &mdash; "
         "the restorative influence the elephant later overhears."),
        ("gajuttamo",
         "&ldquo;the supreme elephant&rdquo; &mdash; Ladyface, once "
         "restored to good qualities."),
        ("Mahiḷāmukhajātaka",
         "the traditional title of this tale, &lsquo;The Elephant "
         "Named Ladyface&rsquo;."),
        ("Mahiḷāmukha",
         "&ldquo;Ladyface&rdquo; &mdash; the elephant's own name, "
         "given as the title of this tale."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja26:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What causes Ladyface the elephant to go on a rampage, per the verse?',
         "opts": [
             'Physical mistreatment',
             'Overhearing the speech of bandits',
             'A lack of food',
             'No cause is given',
         ],
         "correct": 1,
         "expl": 'A good-natured elephant corrupted purely by what it overheard.'},
        {"q": 'What restores Ladyface to good qualities?',
         "opts": [
             'No restoration is described',
             'Direct training by a keeper',
             'Overhearing the speech of the well-restrained',
             'Being given more food',
         ],
         "correct": 2,
         "expl": 'The same kind of influence that corrupted it, now working in reverse.'},
        {"q": 'In either direction, is the elephant directly taught or trained?',
         "opts": [
             'Only the corruption is direct; the restoration is not',
             'Only the restoration is direct; the corruption is not',
             'Yes, always directly instructed',
             'No — both changes happen simply through what it happens to overhear',
         ],
         "correct": 3,
         "expl": 'Highlighting the quiet, cumulative power of environment and company.'},
        {"q": 'What underlying concern does this tale illustrate?',
         "opts": [
             'How easily character can be shaped by what one merely overhears',
             'The danger of elephants specifically',
             'The importance of royal status',
             'The importance of physical strength',
         ],
         "correct": 0,
         "expl": 'A concern that extends well beyond the literal elephant of the story.'},
        {"q": "What does Sujato's comment say about the elephant's original nature?",
         "opts": [
             'It was naturally violent',
             'It was good-natured before being corrupted',
             'Its nature is not described',
             'It had no fixed nature',
         ],
         "correct": 1,
         "expl": 'Making the corruption purely a matter of external influence, not an inherent trait.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Ox Named Nandivisāla',
             'Fords',
             'The Elephant Named Ladyface (Mahiḷāmukhajātaka)',
             'Frequent',
         ],
         "correct": 2,
         "expl": 'The twenty-sixth poem overall, and the sixth of the Kuruṅgavagga.'},
        {"q": 'What does the verse call the elephant once restored?',
         "opts": [
             'An ordinary elephant',
             'No description is given',
             'A dangerous beast',
             "'The supreme elephant', established in all good qualities",
         ],
         "correct": 3,
         "expl": 'Emphasizing the completeness of its restoration.'},
        {"q": 'Who does the elephant overhear the second time, restoring its virtue?',
         "opts": [
             'The well-restrained',
             'A king',
             'No one — it changes on its own',
             'Bandits again',
         ],
         "correct": 0,
         "expl": 'The direct contrast to the bandits it overheard the first time.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The sixth poem of the Kuruṅgavagga, following Ja 21 through Ja 25',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Kuruṅgavagga.'},
        {"q": "Is the elephant's transformation, in either direction, framed as sudden or the result of a process?",
         "opts": [
             'The verse denies any transformation occurred',
             'The verse specifies a long, gradual process each time',
             'The verse presents both changes concisely, without detailing the process, simply crediting the overheard speech',
             'The verse specifies the process took exactly one year',
         ],
         "correct": 2,
         "expl": "Consistent with this collection's typically terse, compressed verse form."},
    ],
    marginalia=[
        ("A rampage, caused by overheard words", [
            "no direct provocation needed —",
            "bandit talk alone was enough"
        ]),
        ("Restored the same way it was corrupted", [
            "not by training, but by better company —",
            "virtue overheard, just like the vice was"
        ]),
        ("A name that names the story", [
            "Ladyface, given the tale's own title —",
            "his character the whole point"
        ]),
        ("Environment shaping without instruction", [
            "no lesson given directly, either time —",
            "just what happened to be overheard"
        ]),
    ],
    further=[
        '<a href="%s/ja26/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-25.html\">Ja 25 &mdash; Fords</a> &mdash; the "
        "poem immediately before this one.",
        '<a href="ja-27.html">Ja 27 &mdash; Frequent</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 27 — Abhiṇha (Frequent)
# --------------------------------------------------------------------------- #
page(
    27, "Abhi&#7751;ha", "Frequent",
    meta_title="Ja 27 — Frequent | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 27 — a royal elephant's grief for its missing friend, "
        "a dog, and the quiet power of simply being seen often. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself, "
                    "reflecting on the elephant's grief"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, tender observation"),
    ],
    why=(
        "This brief tale offers a gentle, cross-species picture of "
        "friendship &mdash; a state elephant pining for a dog it has "
        "grown fond of, per the verse's own reasoning, simply through "
        "frequent, unremarkable proximity, not through any grand "
        "gesture or dramatic bond."),
    guide=[
        ("A friendship explained by simple frequency", [
            "The verse reflects on an unusual bond: &lsquo;it's not "
            "enough to give him a morsel, a bite, some grass, or a "
            "rubbing-down. I think by seeing the dog often, the "
            "elephant grew fond of him.&rsquo; Per Sujato's comment, "
            "a state elephant pines when his friend, a dog, goes "
            "missing &mdash; and the verse's own explanation for the "
            "bond is disarmingly simple: not favors or care alone, "
            "but the accumulated effect of frequent, ordinary "
            "presence."]),
        ("A quiet counterpoint to this chapter's more dramatic tales", [
            "Compared to the self-sacrifice, injustice, and battlefield "
            "resolve found elsewhere in this chapter, this poem's "
            "observation is small and domestic &mdash; grief for a "
            "missing companion, and an attempt to understand where "
            "that attachment actually came from."]),
    ],
    terms=[
        ("kabaḷaṁ / piṇḍaṁ / kuse / ghaṁsituṁ",
         "&ldquo;a morsel... a bite, some grass, or a "
         "rubbing-down&rdquo; &mdash; the list of favors the verse "
         "rules out as the source of the elephant's attachment."),
        ("abhiṇhadassanā",
         "&ldquo;by seeing... often&rdquo; &mdash; the verse's own "
         "proposed explanation for the bond, giving this poem its "
         "traditional title."),
        ("sneha",
         "&ldquo;fondness&rdquo; &mdash; the affection the elephant "
         "developed for the dog."),
        ("Abhiṇhajātaka",
         "the traditional title of this tale, &lsquo;Frequent&rsquo;."),
        ("nāgo",
         "&ldquo;elephant&rdquo; &mdash; here, the state elephant "
         "pining for its missing friend."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja27:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the elephant do when its friend, a dog, goes missing?',
         "opts": [
             'It finds a replacement immediately',
             'It shows no reaction',
             'It pines',
             'It searches aggressively',
         ],
         "correct": 2,
         "expl": "Per Sujato's comment, a state elephant pining for its missing companion."},
        {"q": "What does the verse rule out as the source of the elephant's attachment?",
         "opts": [
             "The dog's appearance",
             "The elephant's own personality",
             'Nothing is ruled out',
             'Favors such as a morsel of food, a bite, grass, or a rubbing-down',
         ],
         "correct": 3,
         "expl": "'It's not enough to give him a morsel... a bite, some grass, or a rubbing-down.'"},
        {"q": 'What does the verse propose as the actual source of the bond?',
         "opts": [
             'Simply seeing the dog often (abhiṇhadassanā)',
             'Shared meals specifically',
             'No explanation is proposed',
             'A single dramatic rescue',
         ],
         "correct": 0,
         "expl": "Giving this poem its traditional title, 'Frequent'."},
        {"q": "How does this poem's tone compare to other tales in this chapter, such as Ja 22's protest or Ja 23's battlefield resolve?",
         "opts": [
             'Equally dramatic',
             'Smaller and more domestic — a quiet observation about grief and ordinary attachment',
             'More violent',
             'There is no notable difference',
         ],
         "correct": 1,
         "expl": "A gentle counterpoint within this chapter's broader range of tone."},
        {"q": "What two species does this tale's friendship involve?",
         "opts": [
             'An elephant and a bird',
             'Two elephants',
             'An elephant and a dog',
             'A horse and a dog',
         ],
         "correct": 2,
         "expl": 'An unusual, tender cross-species bond.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Ox Named Nandivisāla',
             'The Ox Named Black',
             'The Elephant Named Ladyface',
             'Frequent (Abhiṇhajātaka)',
         ],
         "correct": 3,
         "expl": 'The twenty-seventh poem overall, and the seventh of the Kuruṅgavagga.'},
        {"q": "What role did the elephant hold, per Sujato's comment?",
         "opts": [
             'A state (royal) elephant',
             'A temple elephant',
             'The comment does not specify',
             'A wild, untamed elephant',
         ],
         "correct": 0,
         "expl": 'Adding a note of unexpected tenderness to its bond with an ordinary dog.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The seventh poem of the Kuruṅgavagga, following Ja 21 through Ja 26',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Kuruṅgavagga.'},
        {"q": "What quality does this verse's explanation for the bond emphasize?",
         "opts": [
             'Shared danger',
             'Dramatic, singular events',
             'The accumulated effect of ordinary, repeated presence',
             'Material exchange alone',
         ],
         "correct": 2,
         "expl": 'A disarmingly simple account of how attachment forms.'},
        {"q": 'How long is this poem?',
         "opts": [
             'A two-line couplet',
             'A prose passage',
             'A ten-verse narrative',
             'A single four-line stanza',
         ],
         "correct": 3,
         "expl": "Consistent with this chapter's typically terse verse form."},
    ],
    marginalia=[
        ("Not favors, just presence", [
            "no morsel, no rubbing-down explains it —",
            "just seeing each other, often"
        ]),
        ("An elephant pining for a dog", [
            "an unusual pair, a genuine bond —",
            "grief when the smaller friend goes missing"
        ]),
        ("A quiet poem among louder ones", [
            "no battle, no injustice, no sacrifice —",
            "just an ordinary attachment, examined gently"
        ]),
        ("Frequency as its own kind of care", [
            "not grand gestures, just showing up —",
            "the verse's whole theory of friendship"
        ]),
    ],
    further=[
        '<a href="%s/ja27/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-26.html\">Ja 26 &mdash; The Elephant Named "
        "Ladyface</a> &mdash; the poem immediately before this one.",
        "<a href=\"ja-28.html\">Ja 28 &mdash; The Ox Named "
        "Nandivisāla</a> &mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 28 — Nandivisāla (The Ox Named Nandivisāla)
# --------------------------------------------------------------------------- #
page(
    28, "Nandivis&amacr;la", "The Ox Named Nandivisāla",
    meta_title="Ja 28 — The Ox Named Nandivisāla | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 28 — a famous ox's proof that kind speech accomplishes "
        "what harsh speech cannot, and the origin story for a "
        "monastic rule outside this site's scope. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "The ox Nandivisāla, reflecting on why he pulled "
                    "the load"),
        ("Form", "One stanza (six lines)"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with a well-known story behind "
                       "it"),
    ],
    why=(
        "This is among the most well-known of this collection's "
        "animal tales, and Sujato's comment adds an unusual detail: "
        "it is also the origin story for a specific rule in the "
        "Buddhist monastic code (Vinaya) &mdash; a rare direct link "
        "between a Jātaka verse and monastic legislation, though that "
        "Vinaya text itself falls outside this site's own selections."),
    guide=[
        ("A bet won by kindness, not force", [
            "The verse gives the ox's own reflection: &lsquo;one "
            "should only speak sweetly, never not sweetly. For the "
            "one speaking sweetly, a large load was pulled, earning "
            "him money, and he was satisfied with that.&rsquo; Per "
            "Sujato's comment, a brahmin wagers that his ox, "
            "Nandivisāla, can pull a hundred carts. When yelled at, "
            "the ox refuses to pull; but when spoken to kindly, he "
            "pulls the load and wins the bet."]),
        ("An unusual link to a specific monastic rule", [
            "Sujato's comment adds that this tale is &lsquo;the "
            "origin story&rsquo; for a specific rule in the Buddhist "
            "monastic code, where &lsquo;the verse has some different "
            "readings.&rsquo; This site does not currently include "
            "the Vinaya (monastic legal code) among its own text "
            "selections, so this reading guide notes the connection "
            "without a linked page, but the detail illustrates how "
            "widely a single memorable verse could circulate across "
            "different parts of the early canon."]),
    ],
    terms=[
        ("manuññameva bhāseyya",
         "&ldquo;one should only speak sweetly&rdquo; &mdash; the "
         "ox's own opening principle."),
        ("garuṁ bhāraṁ udaddhari",
         "&ldquo;a large load was pulled&rdquo; &mdash; the direct "
         "result of being spoken to kindly."),
        ("Nandivisāla",
         "the ox's own name, giving this poem its traditional title "
         "&mdash; the subject of a famous wager over whether he could "
         "pull a hundred carts."),
        ("Nandivisālajātaka",
         "the traditional title of this tale, &lsquo;The Ox Named "
         "Nandivisāla&rsquo;."),
        ("Bu Pc 2",
         "a specific rule in the Buddhist monastic code (Vinaya), "
         "for which Sujato's comment identifies this tale as the "
         "origin story &mdash; not part of this site's own current "
         "selections."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, also serving, "
        "per Sujato's comment, as the origin story for a specific "
        "monastic rule outside this site's own selections. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja28:1.1-1.6"),
    ],
    quiz=[
        {"q": "What wager does the brahmin make, per Sujato's comment?",
         "opts": [
             'That his ox is the strongest in the region',
             'No specific wager is described',
             'That his ox cannot be trained',
             'That his ox, Nandivisāla, can pull a hundred carts',
         ],
         "correct": 3,
         "expl": 'Setting up the test of kind versus harsh speech.'},
        {"q": 'What happens when the ox is yelled at?',
         "opts": [
             'He refuses to pull',
             'He runs away',
             'No reaction is described',
             'He pulls even harder',
         ],
         "correct": 0,
         "expl": 'Contrasted directly with his response to kind speech.'},
        {"q": 'What happens when the ox is spoken to kindly?',
         "opts": [
             'No change occurs',
             'He pulls the load and wins the bet',
             'He becomes agitated',
             'He refuses regardless',
         ],
         "correct": 1,
         "expl": "Proving the verse's own principle about the power of sweet speech."},
        {"q": "What unusual detail does Sujato's comment add about this tale?",
         "opts": [
             'That it exists in no other form anywhere',
             'That it has no further significance',
             'That it is the origin story for a specific rule in the Buddhist monastic code (Vinaya)',
             'That it was later disproven',
         ],
         "correct": 2,
         "expl": 'A rare direct link between a Jātaka verse and monastic legislation.'},
        {"q": "Is the Vinaya text this tale connects to included among this site's own selections?",
         "opts": [
             'Only partially translated',
             'The question does not apply',
             'Yes, fully translated and linked',
             'No — this site does not currently include the Vinaya among its own text selections',
         ],
         "correct": 3,
         "expl": 'This reading guide notes the connection without a linked page.'},
        {"q": "What principle does the ox's own reflection state?",
         "opts": [
             'That one should only speak sweetly, never harshly',
             'That wagers should be avoided entirely',
             'That oxen cannot be reasoned with',
             'That strength alone determines success',
         ],
         "correct": 0,
         "expl": 'Proven directly by the outcome of the wager.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Frequent',
             'The Ox Named Nandivisāla (Nandivisālajātaka)',
             'The Ox Named Black',
             'The Pig Named Munika',
         ],
         "correct": 1,
         "expl": 'The twenty-eighth poem overall, and the eighth of the Kuruṅgavagga.'},
        {"q": 'How many lines make up this verse?',
         "opts": [
             'Eight lines',
             'Four lines',
             'Six lines',
             'Two lines',
         ],
         "correct": 2,
         "expl": 'Slightly longer than the four-line form most common in this chapter.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The eighth poem of the Kuruṅgavagga, following Ja 21 through Ja 27',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Kuruṅgavagga.'},
        {"q": 'What does the outcome of the wager suggest about kindness as a practical strategy, not just an ethical ideal?',
         "opts": [
             'That kindness can accomplish tangible results that harshness cannot, even in a purely practical wager',
             'That kindness only matters in spiritual contexts',
             "That the wager's outcome was accidental",
             'That kindness has no practical effect',
         ],
         "correct": 0,
         "expl": "The ox's own satisfaction and the money earned both follow directly from being spoken to sweetly."},
    ],
    marginalia=[
        ("A hundred carts, won by kindness", [
            "yelled at, he refused entirely —",
            "spoken to sweetly, he pulled it all"
        ]),
        ("A verse that traveled into monastic law", [
            "the origin story for a Vinaya rule —",
            "outside this site, but noted here"
        ]),
        ("Practical proof, not just principle", [
            "money earned, a bet won —",
            "kindness tested and shown to work"
        ]),
        ("An ox's own name remembered", [
            "Nandivisāla, still the tale's title —",
            "one of this collection's most famous animals"
        ]),
    ],
    further=[
        '<a href="%s/ja28/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-27.html\">Ja 27 &mdash; Frequent</a> &mdash; "
        "the poem immediately before this one.",
        "<a href=\"ja-29.html\">Ja 29 &mdash; The Ox Named Black</a> "
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 29 — Kaṇha (The Ox Named Black)
# --------------------------------------------------------------------------- #
page(
    29, "Ka&#7751;ha", "The Ox Named Black",
    meta_title="Ja 29 — The Ox Named Black | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 29 — a reliable ox's steady labor for the elderly "
        "woman who raised him, whatever the load or terrain. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of steady reliability"),
    ],
    why=(
        "Following the previous poem's proof that kindness "
        "accomplishes what harshness cannot, this poem offers a "
        "complementary picture: an ox whose sheer reliability, "
        "whatever the difficulty of the task, becomes itself an act "
        "of devotion to the one who raised him."),
    guide=[
        ("An ox who always pulls through, regardless of difficulty", [
            "The verse states its point plainly: &lsquo;no matter how "
            "heavy the load, or how deep the passage, when they "
            "harness Black, he pulls that load.&rsquo; Per Sujato's "
            "comment, an ox raised by an elderly woman earns money "
            "for his &lsquo;mother&rsquo; by pulling a heavy load "
            "across a deep river &mdash; a specific, difficult "
            "instance of the general reliability the verse "
            "describes."]),
        ("A quiet act of devotion, expressed through labor", [
            "The verse gives no dramatic speech or explicit statement "
            "of feeling; the ox's devotion to the woman who raised him "
            "is expressed entirely through consistent, effortful work, "
            "regardless of how heavy the load or how difficult the "
            "terrain."]),
    ],
    terms=[
        ("garu dhuraṁ",
         "&ldquo;heavy the load&rdquo; &mdash; the first of two "
         "difficulties the verse names."),
        ("gambhīravattanī",
         "&ldquo;deep the passage&rdquo; &mdash; the second "
         "difficulty, referring to a deep river crossing per Sujato's "
         "comment."),
        ("kaṇha",
         "&ldquo;Black&rdquo; &mdash; the ox's own name, giving this "
         "poem its traditional title."),
        ("Kaṇhajātaka",
         "the traditional title of this tale, &lsquo;The Ox Named "
         "Black&rsquo;."),
        ("&ldquo;mother&rdquo;",
         "per Sujato's comment, the elderly woman who raised the ox "
         "and for whom he earns money through his labor."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja29:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse say about the ox Black's reliability?",
         "opts": [
             'That no matter how heavy the load or deep the passage, he pulls it',
             'That he refuses difficult tasks',
             'No specific claim about reliability is made',
             'That he only pulls light loads',
         ],
         "correct": 0,
         "expl": 'Consistent effort regardless of the difficulty of the task.'},
        {"q": "Who raised the ox, per Sujato's comment?",
         "opts": [
             'A brahmin',
             'An elderly woman',
             'A king',
             'The comment does not specify',
         ],
         "correct": 1,
         "expl": "Referred to in the comment as his 'mother', for whom he earns money through his labor."},
        {"q": 'What specific difficult task does the commentarial story describe?',
         "opts": [
             'No specific task is described',
             'Plowing a field',
             'Pulling a heavy load across a deep river',
             'Carrying goods up a mountain',
         ],
         "correct": 2,
         "expl": 'A concrete instance of the general reliability the verse describes.'},
        {"q": "How is the ox's devotion to the woman expressed in this verse?",
         "opts": [
             'Through a formal ceremony',
             'The verse does not address devotion at all',
             'Through explicit spoken declarations',
             'Entirely through consistent, effortful labor, without dramatic speech',
         ],
         "correct": 3,
         "expl": 'A quiet act expressed through work rather than words.'},
        {"q": 'How does this poem relate to the previous poem, Ja 28?',
         "opts": [
             "It offers a complementary picture — reliability as its own form of devotion, following Ja 28's proof of kindness's power",
             'It has no relationship to Ja 28',
             'It retells the exact same story',
             "It contradicts Ja 28's message entirely",
         ],
         "correct": 0,
         "expl": 'Both poems concern draft animals whose behavior carries a moral about how effort and relationship intersect.'},
        {"q": 'What two specific difficulties does the verse name?',
         "opts": [
             'Heat and cold',
             'A heavy load and a deep passage (river crossing)',
             'Hunger and thirst',
             'Distance and time',
         ],
         "correct": 1,
         "expl": 'Both overcome consistently by the ox Black.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Frequent',
             'The Ox Named Nandivisāla',
             'The Ox Named Black (Kaṇhajātaka)',
             'The Pig Named Munika',
         ],
         "correct": 2,
         "expl": 'The twenty-ninth poem overall, and the ninth of the Kuruṅgavagga.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The ninth poem of the Kuruṅgavagga, following Ja 21 through Ja 28',
         ],
         "correct": 3,
         "expl": 'The second-to-last poem of this ten-poem chapter.'},
        {"q": "What does the ox earn through his labor, per Sujato's comment?",
         "opts": [
             'Money for the elderly woman who raised him',
             'His own freedom',
             'A better living situation for himself',
             'Nothing — the labor is unrewarded',
         ],
         "correct": 0,
         "expl": 'His labor directly benefits the one who raised him.'},
        {"q": 'What overall quality does this verse celebrate?',
         "opts": [
             'Cleverness',
             'Steady, unconditional reliability regardless of difficulty',
             'Physical strength alone, without regard to purpose',
             'Cunning and trickery',
         ],
         "correct": 1,
         "expl": "The ox's consistent performance, whatever the challenge, is the verse's whole point."},
    ],
    marginalia=[
        ("Whatever the load, whatever the depth", [
            "no exceptions named, no conditions attached —",
            "'when they harness Black, he pulls that load'"
        ]),
        ("Devotion, expressed through work alone", [
            "no speech, no declaration —",
            "just labor, consistently given"
        ]),
        ("A deep river, crossed for her sake", [
            "the specific difficulty behind the general claim —",
            "earning money for the one who raised him"
        ]),
        ("A companion piece to the previous poem", [
            "kindness proved its power in Ja 28 —",
            "here, reliability proves its own"
        ]),
    ],
    further=[
        '<a href="%s/ja29/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-28.html\">Ja 28 &mdash; The Ox Named "
        "Nandivisāla</a> &mdash; the poem immediately before this "
        "one.",
        "<a href=\"ja-30.html\">Ja 30 &mdash; The Pig Named "
        "Munika</a> &mdash; the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 30 — Munika (The Pig Named Munika)
# --------------------------------------------------------------------------- #
page(
    30, "Munika", "The Pig Named Munika",
    meta_title="Ja 30 — The Pig Named Munika | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 30, closing the Kuruṅgavagga — a hardworking ox's "
        "envy of a well-fed pig, and his brother's warning about what "
        "that rich diet actually means. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Three (Kuruṅgavagga) &middot; Poem 10 of 10 (closing the chapter)",
    glance=[
        ("Setting", "One ox addressing another, comparing their "
                    "situation to a nearby pig's"),
        ("Speaker", "An ox, warning his brother against envy"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with a dark twist beneath its "
                       "surface"),
    ],
    why=(
        "This poem closes the Kuruṅgavagga with a sharp reversal: "
        "what looks like an enviable, easy life &mdash; rich food, "
        "no hard labor &mdash; turns out, once its real cause is "
        "understood, to be nothing worth envying at all."),
    guide=[
        ("Contentment urged, with a hidden reason behind it", [
            "The verse gives one ox's advice to another: &lsquo;envy "
            "not what is Munika's, for he eats the food of the "
            "terminally ill. Don't worry, just eat your chaff, this "
            "is a mark of long life.&rsquo; On its surface, this "
            "reads as simple advice toward contentment &mdash; but the "
            "verse's own reasoning already hints that something is "
            "not quite as it first appears."]),
        ("A dark reason for the pig's rich diet, per the commentarial story", [
            "Per Sujato's comment, a hard-working ox is jealous of the "
            "rice scoffed by the pig Munika, but his brother tells him "
            "not to worry, since the pig is being fattened for a "
            "feast. The pig's rich food is not a reward or good "
            "fortune at all &mdash; it is preparation for slaughter. "
            "The ox's own plain chaff, by contrast, is genuinely "
            "&lsquo;a mark of long life&rsquo;: unremarkable, but "
            "safe."]),
        ("Closing the Kuruṅgavagga", [
            "This poem closes the Kuruṅgavagga, the third of eight "
            "chapters this site's selection draws from within the "
            "Ekakanipāta. The source text's own untranslated summary "
            "verse (uddāna) immediately follows, naming all ten poems "
            "of this chapter in sequence &mdash; not presented here "
            "as quoted text, since it carries no separate translation, "
            "but noted for completeness, as at the close of the "
            "previous two chapters."]),
    ],
    terms=[
        ("mā munikassa pihayi",
         "&ldquo;envy not what is Munika's&rdquo; &mdash; the "
         "verse's opening warning against envy."),
        ("āturannāni bhuñjati",
         "&ldquo;he eats the food of the terminally ill&rdquo; "
         "&mdash; the verse's own hint that the pig's rich diet has "
         "a hidden, unwelcome cause."),
        ("dīghāyulakkhaṇaṁ",
         "&ldquo;a mark of long life&rdquo; &mdash; the verse's own "
         "reframing of the plain chaff the ox actually eats."),
        ("Munika",
         "the pig's own name, giving this poem its traditional title "
         "&mdash; secretly being fattened for slaughter, not enjoying "
         "genuine good fortune."),
        ("Munikajātaka",
         "the traditional title of this tale, closing the "
         "Kuruṅgavagga."),
    ],
    text_intro=(
        "The text in full: a single verse. The chapter's own "
        "untranslated closing summary verse (uddāna), which follows "
        "immediately in the source text, is not quoted here since it "
        "carries no English translation, but its content &mdash; the "
        "ten poem titles of this chapter in sequence &mdash; matches "
        "this reading guide's own further reading list below. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja30:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What advice does the speaking ox give?',
         "opts": [
             'To demand better food',
             'Not to envy the pig Munika, and to be content eating chaff',
             'To flee the farm',
             'To fight the pig for its food',
         ],
         "correct": 1,
         "expl": 'Advice toward contentment, though the reasoning behind it holds a twist.'},
        {"q": 'What does the verse reveal about why the pig eats rich food?',
         "opts": [
             'No explanation is given',
             'The pig simply prefers rich food',
             "The pig eats 'the food of the terminally ill' — a hint that something is not as it first appears",
             'The pig stole the food',
         ],
         "correct": 2,
         "expl": 'Setting up the darker reveal confirmed by the commentarial story.'},
        {"q": "What does the commentarial story reveal is the real reason for the pig's rich diet?",
         "opts": [
             'The pig won a competition',
             'No further explanation is given in the comment',
             'The pig is a family pet',
             'The pig is being fattened for a feast — the rich food is preparation for slaughter, not good fortune',
         ],
         "correct": 3,
         "expl": 'Reframing what looked like an enviable situation as something genuinely undesirable.'},
        {"q": "How does the verse reframe the ox's own plain diet of chaff?",
         "opts": [
             "As 'a mark of long life' — unremarkable, but safe",
             'As a temporary situation soon to change',
             'The verse does not reframe it',
             'As a punishment',
         ],
         "correct": 0,
         "expl": "The ox's own hard, unglamorous labor is actually the safer position."},
        {"q": 'What chapter does this poem close?',
         "opts": [
             'The Sīlavagga',
             "The Kuruṅgavagga, the third of eight chapters this site's selection draws from",
             'The final chapter of the whole Jātaka',
             'It does not close a chapter',
         ],
         "correct": 1,
         "expl": "The source text's own untranslated summary verse (uddāna) follows immediately after."},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'It is presented as spoken by the pig',
             'Yes, quoted in full',
             'No — it carries no separate English translation, so it is only noted for completeness',
             'It does not exist for this chapter',
         ],
         "correct": 2,
         "expl": 'Consistent with the same practice at the close of the previous two chapters.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Ox Named Nandivisāla',
             'Frequent',
             'The Ox Named Black',
             'The Pig Named Munika (Munikajātaka)',
         ],
         "correct": 3,
         "expl": 'The thirtieth poem overall, and the tenth and final poem of the Kuruṅgavagga.'},
        {"q": "What sharp reversal does this poem's closing structure demonstrate?",
         "opts": [
             "What looks enviable (the pig's rich food) turns out, once understood, to be far worse than the plain but safe alternative",
             "The ox's own situation turns out to be worse",
             'Both animals end up in the same situation',
             'No reversal occurs',
         ],
         "correct": 0,
         "expl": "The poem's core irony, delivered in just four lines."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of the Kuruṅgavagga',
             'The tenth and final poem of the Kuruṅgavagga, closing this chapter',
             'It stands outside any chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse following immediately after."},
        {"q": "How many chapters of the Ekakanipāta does this site's selection now cover, after this poem?",
         "opts": [
             'Five',
             'One',
             'Three — the Apaṇṇakavagga, Sīlavagga, and now the Kuruṅgavagga',
             'All eight',
         ],
         "correct": 2,
         "expl": "Thirty poems complete, out of this site's 82-poem selection."},
    ],
    marginalia=[
        ("Rich food, dark purpose", [
            "not fortune, but fattening for the feast —",
            "the reveal the verse only half-conceals"
        ]),
        ("Chaff reframed as safety", [
            "plain, unremarkable, and long-lived for it —",
            "the ox's own diet, worth more than it looks"
        ]),
        ("A warning against envy, well-earned", [
            "don't wish for what you don't understand —",
            "the pig's apparent luck is nothing of the kind"
        ]),
        ("Thirty poems, three chapters closed", [
            "the Kuruṅgavagga's own summary follows —",
            "not quoted, since it has no translation"
        ]),
    ],
    further=[
        '<a href="%s/ja30/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-29.html\">Ja 29 &mdash; The Ox Named Black</a> "
        "&mdash; the poem immediately before this one.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 31 — Kulāvaka (Nests)
# --------------------------------------------------------------------------- #
page(
    31, "Kul&amacr;vaka", "Nests",
    meta_title="Ja 31 — Nests | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 31, opening the Kulāvakavagga — Sakka's own refusal "
        "to destroy bird nests even at the cost of losing a war, "
        "nearly identical to this site's own SN 11.6. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "A battlefield or its approach, addressed to a "
                    "charioteer"),
        ("Speaker", "Sakka, ruler of the gods, addressing his "
                    "charioteer Mātali"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of striking ethical priority"),
    ],
    why=(
        "This verse's central claim &mdash; that Sakka, ruler of the "
        "gods, would rather lose a war to the titans than let his own "
        "chariot destroy a stand of bird nests &mdash; is nearly "
        "identical to a verse already complete on this site at SN "
        "11.6, Bird Nests, and directly names the ecological cost of "
        "warfare as unacceptable, even to a divine king."),
    guide=[
        ("A war-god's priority, stated plainly", [
            "The verse is spoken by Sakka to his own charioteer: "
            "&lsquo;Mātali, don't ram the bird nests in the red "
            "silk-cotton woods with your draft-pole. I'd rather give "
            "up our lives to the titans than deprive these birds of "
            "their nests.&rsquo; Per Sujato's comment, this verse is "
            "nearly identical to one already complete on this site's "
            "own SN 11.6, only a couple of variant readings apart."]),
        ("An early, explicit acknowledgment of war's ecological cost", [
            "Sujato's comment observes that Sakka is directly "
            "&lsquo;acknowledging the unacceptable ecological damage "
            "of warfare&rsquo; &mdash; identifying Mātali as the "
            "traditional charioteer of Indra/Sakka in both Buddhist "
            "and Brahmanical literature. The verse's priority is "
            "strikingly absolute: not merely regret at collateral "
            "harm, but a willingness to lose the entire battle rather "
            "than cause it."]),
    ],
    terms=[
        ("kulāvakā",
         "&ldquo;nests&rdquo; &mdash; the bird nests Sakka refuses "
         "to let his charioteer destroy, giving this poem its "
         "traditional title."),
        ("mātali",
         "the traditional charioteer of Indra/Sakka in both Buddhist "
         "and Brahmanical literature, addressed directly in this "
         "verse."),
        ("asuresu pāṇaṁ cajāma",
         "&ldquo;I'd rather give up our lives to the titans&rdquo; "
         "&mdash; Sakka's own absolute statement of priority."),
        ("Kulāvakajātaka",
         "the traditional title of this tale, opening the "
         "Kulāvakavagga."),
        ("SN 11.6",
         "&ldquo;Bird Nests&rdquo; &mdash; the already-completed page "
         "on this site with a verse Sujato's own comment identifies "
         "as nearly identical to this one."),
    ],
    text_intro=(
        "The text in full: a single verse, nearly identical to a "
        "verse already complete on this site's own SN 11.6. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja31:1.1-1.4"),
    ],
    quiz=[
        {"q": "What already-completed page on this site does Sujato's comment identify as nearly identical to this verse?",
         "opts": [
             'MN 83',
             'No such parallel exists',
             'AN 8.29',
             'SN 11.6, Bird Nests',
         ],
         "correct": 2,
         "expl": 'Only a couple of variant readings apart, per the comment.'},
        {"q": 'Who speaks this verse, and to whom?',
         "opts": [
             'A hunter, to his companion',
             'A bird, to another bird',
             'A king, to his minister',
             'Sakka, ruler of the gods, to his charioteer Mātali',
         ],
         "correct": 3,
         "expl": 'Mātali is the traditional charioteer of Indra/Sakka in both Buddhist and Brahmanical literature.'},
        {"q": 'What does Sakka say he would rather do than have his chariot destroy the bird nests?',
         "opts": [
             "Give up his and his charioteer's lives to the titans (asuras) in battle",
             'Order the birds relocated',
             'Nothing — the verse gives no alternative',
             'Turn back entirely',
         ],
         "correct": 0,
         "expl": 'An absolute statement of priority, not merely regret at collateral harm.'},
        {"q": "What does Sujato's comment say this verse acknowledges directly?",
         "opts": [
             'The importance of military strategy',
             'The unacceptable ecological damage of warfare',
             'The superiority of the titans',
             'Nothing beyond the literal story',
         ],
         "correct": 1,
         "expl": 'A striking, explicit priority from a war-god himself.'},
        {"q": 'Where were the nests located, per the verse?',
         "opts": [
             'In a mountain cave',
             'In an ordinary forest',
             'In the red silk-cotton woods',
             'By a riverbank',
         ],
         "correct": 2,
         "expl": 'The specific setting Sakka warns his charioteer to avoid.'},
        {"q": 'What chapter does this poem open?',
         "opts": [
             'The Atthakāmavagga',
             'It does not open a chapter',
             'The Kuruṅgavagga',
             'The Kulāvakavagga',
         ],
         "correct": 3,
         "expl": "This collection's fourth ten-poem chapter."},
        {"q": "Who are the 'titans' (asuras) mentioned in the verse?",
         "opts": [
             "Sakka's traditional enemies in battle",
             'A group of birds',
             'The verse does not mention any titans',
             "Sakka's own allies",
         ],
         "correct": 0,
         "expl": 'The very battle Sakka is willing to lose rather than harm the nests.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Dancing',
             'Nests (Kulāvakajātaka)',
             'Agreement',
             'The Fish',
         ],
         "correct": 1,
         "expl": 'The thirty-first poem overall, and the first of the Kulāvakavagga.'},
        {"q": 'What instrument does Sakka warn his charioteer not to use against the nests?',
         "opts": [
             'No specific instrument is named',
             'A sword',
             'The draft-pole of the chariot',
             'A bow',
         ],
         "correct": 2,
         "expl": 'The literal mechanism by which the nests would be destroyed in passing.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The final poem of the Kulāvakavagga',
             'The final poem of the Kuruṅgavagga',
             'The first poem of the fourth chapter (Kulāvakavagga), following the completed Kuruṅgavagga',
         ],
         "correct": 3,
         "expl": "Opening this collection's fourth ten-poem chapter."},
    ],
    marginalia=[
        ("A war-god's unexpected priority", [
            "not victory first, but the nests spared —",
            "even at the cost of losing everything"
        ]),
        ("Nearly the same verse, twice on this site", [
            "SN 11.6 tells it almost word for word —",
            "confirmed directly in Sujato's own comment"
        ]),
        ("Warfare's cost, named plainly", [
            "not just human loss, but nests destroyed —",
            "an ancient acknowledgment of collateral harm"
        ]),
        ("Opening the fourth chapter", [
            "Kulāvakavagga begins with mercy over conquest —",
            "ten more poems of animal and human wisdom follow"
        ]),
    ],
    further=[
        '<a href="%s/ja31/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../samyutta-nikaya/sn-11.6.html">SN 11.6 &mdash; '
        "Bird Nests</a> &mdash; the nearly identical verse already "
        "complete on this site.",
        '<a href="ja-30.html">Ja 30 &mdash; The Pig Named Munika</a> '
        "&mdash; the closing poem of the previous chapter.",
        '<a href="ja-32.html">Ja 32 &mdash; Dancing</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 32 — Nacca (Dancing)
# --------------------------------------------------------------------------- #
page(
    32, "Nacca", "Dancing",
    meta_title="Ja 32 — Dancing | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 32 — a golden swan-king's rejection of a peacock "
        "suitor, the traditional source of an old idea about the "
        "peacock as splendid but foolish. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "A grand ball to choose a husband for a "
                    "princess"),
        ("Speaker", "The Golden Swan, king of all birds, addressing "
                    "a peacock suitor"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of gentle rejection"),
    ],
    why=(
        "This is the traditional origin of a long-running idea in "
        "Indian storytelling: the peacock as visually magnificent but "
        "foolish and undignified &mdash; a suitor rejected not for "
        "any flaw in beauty, but for immodest self-display at the "
        "worst possible moment."),
    guide=[
        ("Beauty praised in full, then a rejection", [
            "The verse first lavishes genuine praise: &lsquo;your cry "
            "is sweet, your back brilliant, your neck the color of "
            "sapphire, and your feathers a full fathom long&rsquo; "
            "&mdash; before the turn: &lsquo;still, because of your "
            "dancing, I will not give you my daughter.&rsquo; The "
            "rejection is not about appearance at all, but about "
            "behavior."]),
        ("A princess's own preference, overruled by a dance", [
            "Per Sujato's comment, when the Golden Swan was elected "
            "king of all the birds, he held a great ball to choose a "
            "husband for his daughter the princess. She herself "
            "favored the glorious peacock &mdash; but when he danced, "
            "immodestly displaying himself before the assembly, her "
            "father turned down the &lsquo;shameless suitor.&rsquo; "
            "Sujato's comment notes this story draws on an Indian "
            "tradition of the peacock as visually splendid but "
            "foolish and clumsy."]),
    ],
    terms=[
        ("rudaṁ manuññaṁ",
         "&ldquo;your cry is sweet&rdquo; &mdash; the first of "
         "several genuine compliments the verse pays the peacock."),
        ("naccena te dhītaraṁ no dadāmi",
         "&ldquo;because of your dancing, I will not give you my "
         "daughter&rdquo; &mdash; the verse's turn from praise to "
         "rejection."),
        ("Golden Swan",
         "per Sujato's comment, the king of all birds, presiding "
         "over the ball to choose his daughter's husband."),
        ("Naccajātaka",
         "the traditional title of this tale, &lsquo;Dancing&rsquo;."),
        ("peacock as splendid but foolish",
         "an established Indian storytelling tradition, per Sujato's "
         "comment, that this tale draws on and helps establish."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja32:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse's opening praise?",
         "opts": [
             "The peacock's cry, back, neck, and feathers — genuine physical beauty",
             "The peacock's intelligence",
             "The peacock's family lineage",
             "The peacock's wealth",
         ],
         "correct": 3,
         "expl": 'Setting up a turn from praise to rejection.'},
        {"q": 'Why does the Golden Swan ultimately refuse the peacock as a suitor?',
         "opts": [
             'Because of his dancing — immodest self-display',
             'Because of his family background',
             'No reason is given',
             'Because of his appearance',
         ],
         "correct": 0,
         "expl": 'The rejection is about behavior, not beauty.'},
        {"q": "Who originally favored the peacock as a suitor, per Sujato's comment?",
         "opts": [
             'No one favored him',
             'The princess herself',
             'The Golden Swan',
             'A rival bird',
         ],
         "correct": 1,
         "expl": "Her father overruled her preference after witnessing the peacock's dance."},
        {"q": 'What occasion, per the comment, brings the birds together?',
         "opts": [
             'A hunting expedition',
             'A funeral',
             'A great ball held by the Golden Swan to choose a husband for his daughter',
             'A war council',
         ],
         "correct": 2,
         "expl": "Setting the scene for the peacock's disqualifying dance."},
        {"q": "What Indian storytelling tradition does Sujato's comment say this tale draws on?",
         "opts": [
             'The peacock as a symbol of royalty alone',
             'No tradition is mentioned',
             'The peacock as wise and dignified',
             'The peacock as visually splendid but foolish and clumsy',
         ],
         "correct": 3,
         "expl": 'This tale is identified as a traditional origin point for that idea.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Dancing (Naccajātaka)',
             'Agreement',
             'The Fish',
             'Nests',
         ],
         "correct": 0,
         "expl": 'The thirty-second poem overall, and the second of the Kulāvakavagga.'},
        {"q": 'Who speaks this verse?',
         "opts": [
             'The princess',
             'The Golden Swan, king of all birds',
             'The peacock himself',
             'An unnamed narrator',
         ],
         "correct": 1,
         "expl": 'Addressing the peacock directly with both praise and rejection.'},
        {"q": "What color is the peacock's neck compared to in the verse?",
         "opts": [
             'No color comparison is made',
             'Gold',
             'Sapphire',
             'Emerald',
         ],
         "correct": 2,
         "expl": 'One of several genuine compliments preceding the rejection.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The second poem of the Kulāvakavagga, following Ja 31',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": 'What overall lesson does this tale suggest about outward beauty?',
         "opts": [
             'That beauty alone is not enough — conduct and dignity matter as much or more',
             'That beauty is irrelevant entirely',
             'No lesson is suggested',
             'That beauty alone always wins approval',
         ],
         "correct": 0,
         "expl": "The peacock's genuine beauty is fully acknowledged, yet still insufficient."},
    ],
    marginalia=[
        ("Praised fully, then turned down", [
            "sweet cry, sapphire neck, fathom-long feathers —",
            "none of it enough, after the dance"
        ]),
        ("A daughter's own choice, overruled", [
            "she favored him first —",
            "her father saw something else entirely"
        ]),
        ("The origin of an old idea", [
            "splendid but foolish, still told today —",
            "this tale among its earliest sources"
        ]),
        ("A dance that cost everything", [
            "immodest display before the whole assembly —",
            "beauty alone couldn't undo it"
        ]),
    ],
    further=[
        '<a href="%s/ja32/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-31.html">Ja 31 &mdash; Nests</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-33.html">Ja 33 &mdash; Agreement</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 33 — Sammodamāna (Agreement)
# --------------------------------------------------------------------------- #
page(
    33, "Sammodam&amacr;na", "Agreement",
    meta_title="Ja 33 — Agreement | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 33 — a hunter's patient wait for a flock of birds to "
        "start arguing, one of this collection's most famous fables "
        "about unity. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "A hunter, watching birds escape his own net"),
        ("Speaker", "The hunter"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, widely recognized fable"),
    ],
    why=(
        "This is one of this collection's most recognizable single "
        "images: a flock of birds lifting an entire net into the air "
        "together, escaping a hunter who nonetheless remains "
        "confident &mdash; because he knows unity, not strength, is "
        "the only thing keeping them free."),
    guide=[
        ("Escape through unity, and a hunter's patient confidence", [
            "The verse gives the hunter's own calculation: &lsquo;in "
            "agreement, the birds fly, taking away the net. But when "
            "they start arguing, they'll come under my sway.&rsquo; "
            "Per Sujato's comment, a flock of birds escapes the "
            "hunter by lifting off his net in unison &mdash; but the "
            "hunter knows their cooperation is fragile, and simply "
            "waits."]),
        ("A fable whose lesson needs no explanation", [
            "Unlike several other tales in this partial selection, "
            "this one requires almost no commentarial backstory to "
            "land its point: the image itself &mdash; a shared "
            "burden lifted together, then lost the moment cooperation "
            "breaks down &mdash; carries its own complete meaning "
            "about the fragility and power of collective action."]),
    ],
    terms=[
        ("sammodamānā",
         "&ldquo;in agreement&rdquo; &mdash; the condition under "
         "which the birds succeed, giving this poem its traditional "
         "title."),
        ("jālamādāya pakkhino",
         "&ldquo;the birds, taking away the net&rdquo; &mdash; the "
         "verse's central image of collective escape."),
        ("yadā te vivadissanti",
         "&ldquo;when they start arguing&rdquo; &mdash; the "
         "condition under which the hunter expects to reclaim his "
         "advantage."),
        ("Sammodamānajātaka",
         "the traditional title of this tale, &lsquo;Agreement&rsquo;."),
        ("tadā ehinti me vasaṁ",
         "&ldquo;then they'll come under my sway&rdquo; &mdash; the "
         "hunter's own confident, patient prediction."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja33:1.1-1.4"),
    ],
    quiz=[
        {"q": "How do the birds initially escape the hunter's net?",
         "opts": [
             'By breaking it apart individually',
             'By lifting it off together in unison',
             'By waiting for the hunter to leave',
             'They do not escape',
         ],
         "correct": 0,
         "expl": "'In agreement, the birds fly, taking away the net.'"},
        {"q": 'What does the hunter believe will eventually happen?',
         "opts": [
             'That the birds will escape permanently',
             'That the birds will start arguing, and then come under his sway',
             'That he will lose interest and leave',
             'That another hunter will catch them first',
         ],
         "correct": 1,
         "expl": "The hunter's patient, confident calculation."},
        {"q": 'Does this poem require an extensive commentarial backstory to understand?',
         "opts": [
             'The poem cannot be understood without the comment',
             'Yes, extensively',
             'No — the image itself carries a complete, self-sufficient meaning',
             'Only partially',
         ],
         "correct": 2,
         "expl": 'Unlike several other tales in this selection, this one needs almost no additional context.'},
        {"q": "What condition does the verse identify as the birds' actual vulnerability?",
         "opts": [
             "The hunter's superior equipment",
             'Bad weather',
             'Physical weakness',
             'The fragility of their own cooperation — the moment they start arguing',
         ],
         "correct": 3,
         "expl": 'Not strength, but unity, is what keeps them free.'},
        {"q": "What broader lesson does this fable's image carry?",
         "opts": [
             'The fragility and power of collective action, dependent on continued cooperation',
             'That hunters are always successful',
             'That birds cannot be caught at all',
             'That individual strength always wins',
         ],
         "correct": 0,
         "expl": "One of this collection's most recognizable single images."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Dancing',
             'Agreement (Sammodamānajātaka)',
             'The Fish',
             'The Quail',
         ],
         "correct": 1,
         "expl": 'The thirty-third poem overall, and the third of the Kulāvakavagga.'},
        {"q": 'What tool does the hunter use to try to catch the birds?',
         "opts": [
             'No tool is mentioned',
             'A bow',
             'A net',
             'A trap made of sticks',
         ],
         "correct": 2,
         "expl": 'The very net the birds lift off together in escape.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The third poem of the Kulāvakavagga, following Ja 31 and Ja 32',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": 'Who speaks this verse?',
         "opts": [
             'The hunter',
             'An unnamed narrator',
             'A third-party observer',
             'One of the birds',
         ],
         "correct": 0,
         "expl": 'Voicing his own patient strategy directly.'},
        {"q": "What emotion does the hunter's tone convey?",
         "opts": [
             'Despair at losing his prey',
             'Patient confidence that his opportunity will eventually come',
             'Anger',
             'Indifference',
         ],
         "correct": 1,
         "expl": 'He does not chase — he simply waits for their unity to break.'},
    ],
    marginalia=[
        ("A net, lifted by many wings", [
            "unity turns a trap into an escape —",
            "the verse's whole image in one line"
        ]),
        ("A hunter who only has to wait", [
            "no chase, no force needed —",
            "just patience, until agreement breaks"
        ]),
        ("A fable that explains itself", [
            "no backstory needed to land the point —",
            "the image alone carries the whole lesson"
        ]),
        ("Cooperation as the only real defense", [
            "not strength, not speed —",
            "just staying in agreement"
        ]),
    ],
    further=[
        '<a href="%s/ja33/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-32.html">Ja 32 &mdash; Dancing</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-34.html">Ja 34 &mdash; The Fish</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 34 — Maccha (The Fish)
# --------------------------------------------------------------------------- #
page(
    34, "Maccha", "The Fish",
    meta_title="Ja 34 — The Fish | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 34 — a caught fish's poignant, almost wry concern for "
        "what his wife thinks of him, more than for his own imminent "
        "death. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "A fish caught in a net, his wife having escaped"),
        ("Speaker", "The caught fish"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, wry, emotionally specific verse"),
    ],
    why=(
        "This poem's small, human irony &mdash; a creature facing "
        "death, yet more anxious about a misunderstanding with his "
        "wife than about that death itself &mdash; gives this "
        "collection one of its most emotionally specific and quietly "
        "funny moments."),
    guide=[
        ("Not fear of death, but fear of being misjudged", [
            "The verse states its priority with startling clarity: "
            "&lsquo;it's not the cold or heat for me, nor the being "
            "caught in the net; it's that my lady, the fish, thinks "
            "of me, “he went for joy to another.”&rsquo; Per Sujato's "
            "comment, when a fish is caught in the net while his wife "
            "escapes, he worries more about what she thinks of him "
            "than of his own imminent fate."]),
        ("A specific, recognizable kind of anxiety", [
            "The verse's power lies in its specificity: not a general "
            "lament about death, but a precise worry about "
            "reputation and misunderstanding within a relationship "
            "&mdash; a distinctly human anxiety placed, with a touch "
            "of gentle irony, inside a fish facing its own death."]),
    ],
    terms=[
        ("na maṁ sītaṁ na maṁ uṇhaṁ",
         "&ldquo;it's not the cold or heat for me&rdquo; &mdash; the "
         "fish's opening dismissal of the obvious physical "
         "discomforts."),
        ("jālasmi bādhanaṁ",
         "&ldquo;being caught in the net&rdquo; &mdash; the literal "
         "danger the fish also dismisses as not his real concern."),
        ("aññaṁ so ratiyā gato",
         "&ldquo;he went for joy to another&rdquo; &mdash; the "
         "misunderstanding the fish fears his wife now believes."),
        ("macchī",
         "&ldquo;my lady, the fish&rdquo; &mdash; the fish's own "
         "wife, whose opinion concerns him more than his own fate."),
        ("Macchajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Fish&rsquo;."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja34:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the fish say is NOT his real concern, facing death in the net?',
         "opts": [
             'Nothing — the verse gives no dismissals',
             'The cold, the heat, or being caught in the net itself',
             'His own hunger',
             'The location of the net',
         ],
         "correct": 1,
         "expl": 'All plainly stated as secondary to his actual worry.'},
        {"q": "What is the fish's real concern, per the verse?",
         "opts": [
             'That the net will break',
             'That he will be eaten',
             "That his wife now believes he 'went for joy to another'",
             'That he will never be found',
         ],
         "correct": 2,
         "expl": 'A precise worry about being misjudged by someone he cares about.'},
        {"q": "What happened to the fish's wife, per Sujato's comment?",
         "opts": [
             'She was never present',
             'The comment does not mention her',
             'She was also caught',
             'She escaped the net',
         ],
         "correct": 3,
         "expl": 'Leaving him caught alone, and anxious about how she now interprets his absence.'},
        {"q": 'What kind of anxiety does this verse place inside a fish facing death?',
         "opts": [
             'A specific, recognizably human worry about reputation and misunderstanding within a relationship',
             'A fear of physical pain',
             'No anxiety is described',
             'A general fear of death',
         ],
         "correct": 0,
         "expl": 'Giving the verse its distinctive, quietly ironic tone.'},
        {"q": 'What tone does this reading guide identify in this verse?',
         "opts": [
             'Purely tragic, with no lighter element',
             'Poignant with a touch of gentle irony',
             'Comic and lighthearted throughout',
             'Angry and accusatory',
         ],
         "correct": 1,
         "expl": 'A small, specific human irony rather than a general lament.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Bird',
             'Agreement',
             'The Fish (Macchajātaka)',
             'The Quail',
         ],
         "correct": 2,
         "expl": 'The thirty-fourth poem overall, and the fourth of the Kulāvakavagga.'},
        {"q": 'Who speaks this verse?',
         "opts": [
             'An unnamed narrator',
             'A fisherman',
             "The fish's wife",
             'The caught fish himself',
         ],
         "correct": 3,
         "expl": 'Giving direct voice to his own priorities in the moment of capture.'},
        {"q": 'What specific accusation does the fish fear his wife believes?',
         "opts": [
             "That he 'went for joy to another' — implying infidelity or abandonment",
             'That he was cowardly',
             'That he was greedy',
             'That he was careless',
         ],
         "correct": 0,
         "expl": 'The precise misunderstanding driving his anxiety.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The fourth poem of the Kulāvakavagga, following Ja 31 through Ja 33',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": "How does this verse's approach differ from a straightforward lament about mortality?",
         "opts": [
             'It focuses entirely on anger at the hunter',
             'It does not differ',
             'It redirects the entire emotional weight onto a specific relational anxiety instead of death itself',
             'It focuses entirely on physical suffering',
         ],
         "correct": 2,
         "expl": "The verse's distinctive, specific emotional focus."},
    ],
    marginalia=[
        ("Not death, but a misunderstanding", [
            "the net, the cold, the heat — none of it matters —",
            "only what she now believes of him"
        ]),
        ("A fish's very human worry", [
            "reputation outlasting even fear of dying —",
            "a small irony placed gently inside a big one"
        ]),
        ("An escape that leaves a question behind", [
            "she got away, he did not —",
            "and now he can't explain himself"
        ]),
        ("A quietly funny kind of tragedy", [
            "facing death, and still worried about being misjudged —",
            "recognizable, even across species"
        ]),
    ],
    further=[
        '<a href="%s/ja34/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-33.html">Ja 33 &mdash; Agreement</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-35.html">Ja 35 &mdash; The Quail</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 35 — Vaṭṭaka (The Quail)
# --------------------------------------------------------------------------- #
page(
    35, "Va&#7789;&#7789;aka", "The Quail",
    meta_title="Ja 35 — The Quail | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 35 — a helpless quail chick's protection chant "
        "turning back a wall of fire, shared word for word with this "
        "site's own Cp 29. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "A young quail, alone, facing an advancing "
                    "wildfire"),
        ("Speaker", "The quail chick itself"),
        ("Form", "One four-line stanza, a chant still used today"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, still-living protection chant"),
    ],
    why=(
        "This verse is not merely an old story: per Sujato's comment, "
        "it &lsquo;remains a popular protection chant&rsquo; used to "
        "this day, and appears word for word at this site's own "
        "already-completed Cp 29, giving this collection a rare case "
        "of a single verse serving simultaneously as narrative, "
        "theology, and living religious practice."),
    guide=[
        ("A helpless creature's own declaration of truth", [
            "The verse gives the quail chick's own words, facing a "
            "wall of flame: &lsquo;I have wings that do not fly! I "
            "have feet that do not walk! Mother and father have fled! "
            "Jātaveda the fire: go back!&rsquo; Per Sujato's comment, "
            "the little quail, alone and helpless, turns back the "
            "fire through &lsquo;the power of truth&rsquo; &mdash; not "
            "through any physical action, since by its own admission "
            "it is entirely incapable of any."]),
        ("A word from the Rig Veda, still alive in the Jātaka", [
            "Sujato's comment identifies &lsquo;Jātaveda&rsquo;, "
            "addressed here as the fire itself, as a name found "
            "commonly in the Rig Veda but only rarely in the Pali "
            "canon &mdash; mostly in the Jātakas, showing how "
            "&lsquo;Vedic ideas are still alive in this "
            "collection.&rsquo; Here it is addressed directly as an "
            "agent capable of responding to the chick's plea, "
            "identified with the god Agni."]),
        ("A verse shared word for word with this site's own Cariyapitaka", [
            "Sujato's comment notes this same verse &lsquo;is also "
            "found at Cp 29:10.1&rsquo; &mdash; this site's own "
            "already-completed page, The Baby Quail's Conduct, "
            "confirming this is the identical past-life story told "
            "in two different canonical collections."]),
    ],
    terms=[
        ("saccakiriyā",
         "&ldquo;truth-act&rdquo; or &ldquo;power of truth&rdquo; "
         "&mdash; the mechanism, per Sujato's comment, by which the "
         "quail's honest statement of its own helplessness turns "
         "back the fire."),
        ("jātaveda",
         "a name found commonly in the Rig Veda and rarely in the "
         "Pali canon (mostly in the Jātakas), here addressed as the "
         "fire itself, identified with the god Agni."),
        ("santi pakkhā apatanā",
         "&ldquo;I have wings that do not fly!&rdquo; &mdash; the "
         "chick's own honest admission of total helplessness."),
        ("Vaṭṭakajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Quail&rsquo;."),
        ("Cp 29",
         "&ldquo;The Baby Quail's Conduct&rdquo; &mdash; the "
         "already-completed page on this site sharing this verse "
         "word for word."),
    ],
    text_intro=(
        "The text in full: a single verse, still used today as a "
        "protection chant and shared word for word with this site's "
        "own Cp 29. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja35:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Sujato's comment say about this verse's ongoing use?",
         "opts": [
             'The comment does not address its later use',
             'That it fell out of use centuries ago',
             "That it 'remains a popular protection chant' used to this day",
             'That it was only ever a literary device',
         ],
         "correct": 2,
         "expl": 'A rare case of a Jātaka verse still functioning as living religious practice.'},
        {"q": 'What already-completed page on this site shares this verse word for word?',
         "opts": [
             'MN 83',
             'No such match exists',
             'SN 11.6',
             "Cp 29, The Baby Quail's Conduct",
         ],
         "correct": 3,
         "expl": 'Confirming this is the identical past-life story told in two different canonical collections.'},
        {"q": 'What does the quail chick admit about its own physical ability?',
         "opts": [
             'That it has wings that do not fly and feet that do not walk — total helplessness',
             'That it can run quickly',
             'No admission is made',
             'That it is strong and capable',
         ],
         "correct": 0,
         "expl": "The chick's honest statement of complete incapacity."},
        {"q": "What mechanism, per Sujato's comment, actually turns back the fire?",
         "opts": [
             'Physical strength',
             'The power of truth (saccakiriyā) — an honest declaration',
             'A weapon',
             "Divine intervention unrelated to the chick's own words",
         ],
         "correct": 1,
         "expl": 'Not through any physical action, since the chick openly admits it is incapable of any.'},
        {"q": "What is 'Jātaveda', per Sujato's comment?",
         "opts": [
             'A type of fire specifically',
             'A place name',
             'A name found commonly in the Rig Veda and rarely in the Pali canon, mostly in the Jātakas, identified with the god Agni',
             "The quail's own name",
         ],
         "correct": 2,
         "expl": 'Showing how Vedic ideas are still alive within this collection.'},
        {"q": 'What does the chick say happened to its parents?',
         "opts": [
             'They were killed by the fire',
             'The verse does not mention them',
             'They stayed to protect it',
             'They fled',
         ],
         "correct": 3,
         "expl": 'Leaving the chick entirely alone to face the fire.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Quail (Vaṭṭakajātaka)',
             'Bird',
             'The Partridge',
             'The Fish',
         ],
         "correct": 0,
         "expl": 'The thirty-fifth poem overall, and the fifth of the Kulāvakavagga.'},
        {"q": "What species does Sujato's comment suggest the quail likely is?",
         "opts": [
             'A completely mythical bird',
             'Probably the jungle bush quail, which roosts on the ground',
             'A domesticated chicken',
             'No species is suggested',
         ],
         "correct": 1,
         "expl": 'A small, ground-dwelling bird, adding to the vividness of its vulnerability.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fifth poem of the Kulāvakavagga, following Ja 31 through Ja 34',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": 'How is Jātaveda addressed in the verse — as a distant force, or a responsive agent?',
         "opts": [
             'The verse does not address it directly at all',
             'As an enemy to be defeated',
             'As a distant, impersonal force with no agency',
             'As a responsive agent who can hear and respond to a direct plea',
         ],
         "correct": 3,
         "expl": "Directly commanded, 'go back!', as one might address a listening being."},
    ],
    marginalia=[
        ("A chant still spoken today", [
            "not just an old story, but living practice —",
            "Sujato's own comment confirms its ongoing use"
        ]),
        ("Total helplessness, stated as truth", [
            "no wings that fly, no feet that walk —",
            "and the fire turns back anyway"
        ]),
        ("A word from the Rig Veda, still alive", [
            "Jātaveda, rare in the canon but common here —",
            "old ideas persisting inside a new tradition"
        ]),
        ("The same story, two collections", [
            "word for word with this site's own Cp 29 —",
            "one tale, told twice in the canon"
        ]),
    ],
    further=[
        '<a href="%s/ja35/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../cariyapitaka/cp-29.html">Cp 29 &mdash; The Baby '
        "Quail's Conduct</a> &mdash; this site's own already-"
        "completed page sharing this verse word for word.",
        '<a href="ja-34.html">Ja 34 &mdash; The Fish</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-36.html">Ja 36 &mdash; Bird</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 36 — Sakuṇa (Bird)
# --------------------------------------------------------------------------- #
page(
    36, "Sakuṇa", "Bird",
    meta_title="Ja 36 — Bird | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 36 — an urgent warning about a spreading fire, "
        "dismissed by a flock too complacent to listen. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "A tree sheltering a flock of birds, catching "
                    "fire"),
        ("Speaker", "The Bodhisatta, warning the flock"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, urgent verse"),
    ],
    why=(
        "This tale gives voice to a familiar frustration: an urgent, "
        "correct warning dismissed by those too complacent to act on "
        "it &mdash; per Sujato's comment, the birds mock the "
        "Bodhisatta as someone who is &lsquo;always seeing crocodiles "
        "in a drop of water&rsquo; even as their own shelter begins "
        "to burn around them."),
    guide=[
        ("An urgent warning, addressed directly", [
            "The verse gives the warning itself: &lsquo;you "
            "sky-flyers staying near the great evergreen, this fire "
            "is emerging! Geese! Flee to the quarters! The threat is "
            "born from the refuge!&rsquo; The final line's paradox "
            "&mdash; danger arising from the very shelter meant to "
            "protect &mdash; gives the warning its particular urgency."]),
        ("A warning dismissed as excessive caution", [
            "Per Sujato's comment, noticing a fire starting in the "
            "tree under which the flock shelters, the Bodhisatta "
            "tries to warn them &mdash; but the foolish birds dismiss "
            "him, mocking him as someone who is &lsquo;always seeing "
            "crocodiles in a drop of water&rsquo;, a vivid idiom for "
            "chronic, unwarranted alarm. The verse itself does not "
            "record whether the flock ultimately listens in time."]),
        ("An identified species and a poetic term for a tree", [
            "Sujato's comment identifies &lsquo;vakkaṅga&rsquo; "
            "(named for its curved neck) as the cakravāka or "
            "Brahminy goose, and notes that &lsquo;jagatirūha&rsquo; "
            "(literally &lsquo;planet-growth&rsquo;) is simply a "
            "poetic term for a tree, rather than referring to any "
            "specific species."]),
    ],
    terms=[
        ("jagatirūha",
         "&ldquo;evergreen&rdquo;, literally &ldquo;planet-"
         "growth&rdquo; &mdash; per Sujato's comment, a poetic term "
         "for a tree in general, not a specific species."),
        ("vakkaṅga",
         "&ldquo;geese&rdquo;, per Sujato's comment the cakravāka or "
         "Brahminy goose, named for its curved neck."),
        ("jātaṁ saraṇato bhayaṁ",
         "&ldquo;the threat is born from the refuge!&rdquo; &mdash; "
         "the verse's central paradox, danger arising from the very "
         "place meant to provide safety."),
        ("Sakuṇajātaka",
         "the traditional title of this tale, simply "
         "&lsquo;Bird&rsquo;."),
        ("always seeing crocodiles in a drop of water",
         "the flock's own mocking idiom, per Sujato's comment, "
         "dismissing the Bodhisatta's warning as excessive, "
         "unwarranted alarm."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja36:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the Bodhisatta notice, per Sujato's comment?",
         "opts": [
             'A storm approaching',
             'A rival flock nearby',
             'A predator approaching',
             'A fire starting in the tree the flock shelters under',
         ],
         "correct": 3,
         "expl": 'Prompting his urgent warning to the flock.'},
        {"q": "How does the flock respond to the Bodhisatta's warning?",
         "opts": [
             "They dismiss him, mocking him as someone always 'seeing crocodiles in a drop of water'",
             'They attack him',
             'They ask him to explain further',
             'They immediately flee',
         ],
         "correct": 0,
         "expl": 'A vivid idiom for chronic, unwarranted alarm — even as the danger was real.'},
        {"q": "What paradox does the verse's final line state?",
         "opts": [
             'That safety comes only from danger',
             'That the threat is born from the very refuge meant to provide safety',
             'That birds cannot fly from fire',
             'No paradox is stated',
         ],
         "correct": 1,
         "expl": 'Giving the warning its particular urgency — the shelter itself has become the danger.'},
        {"q": "What does Sujato's comment identify 'vakkaṅga' as?",
         "opts": [
             'No specific bird is identified',
             'A mythical bird',
             'The cakravāka or Brahminy goose, named for its curved neck',
             'A type of crow',
         ],
         "correct": 2,
         "expl": "One of several precise naturalist identifications across this chapter's comments."},
        {"q": "What does 'jagatirūha' (evergreen) actually mean, per the comment?",
         "opts": [
             'A type of flower',
             'The name of a specific location',
             'A specific rare tree species',
             "A general poetic term for a tree, literally 'planet-growth'",
         ],
         "correct": 3,
         "expl": 'Not referring to any particular species.'},
        {"q": 'Does the verse itself confirm whether the flock ultimately escapes in time?',
         "opts": [
             'No — the verse does not record whether they listen in time',
             'Yes, but only implicitly',
             'The verse states they all perish',
             'Yes, explicitly',
         ],
         "correct": 0,
         "expl": "Consistent with this collection's typically compressed, unresolved verse form."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Quail',
             'Bird (Sakuṇajātaka)',
             'The Partridge',
             'The Crane',
         ],
         "correct": 1,
         "expl": 'The thirty-sixth poem overall, and the sixth of the Kulāvakavagga.'},
        {"q": 'Who speaks the warning in this verse?',
         "opts": [
             'An outside observer',
             'A single ordinary bird',
             'The Bodhisatta',
             'The flock collectively',
         ],
         "correct": 2,
         "expl": 'Attempting, per the comment, to save the flock from complacency.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The sixth poem of the Kulāvakavagga, following Ja 31 through Ja 35',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": 'What familiar human frustration does this tale give voice to?',
         "opts": [
             'An urgent, correct warning dismissed by those too complacent to act on it',
             'The frustration of losing a competition',
             'No particular frustration is depicted',
             'The frustration of being unable to fly',
         ],
         "correct": 0,
         "expl": 'A recognizable dynamic well beyond the literal birds of the story.'},
    ],
    marginalia=[
        ("A fire in the very shelter", [
            "danger born from the place meant to protect —",
            "the verse's whole paradox in one line"
        ]),
        ("Mocked for sounding the alarm", [
            "'always seeing crocodiles in a drop of water' —",
            "even when the alarm turns out to be real"
        ]),
        ("A named species, precisely identified", [
            "the curved-necked cakravāka, not a generic goose —",
            "naturalist detail grounding the fable"
        ]),
        ("No confirmed ending given", [
            "the verse stops before we learn if they listened —",
            "left open, like much of this collection's brief verse"
        ]),
    ],
    further=[
        '<a href="%s/ja36/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-35.html">Ja 35 &mdash; The Quail</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-37.html">Ja 37 &mdash; The Partridge</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 37 — Tittira (The Partridge)
# --------------------------------------------------------------------------- #
page(
    37, "Tittira", "The Partridge",
    meta_title="Ja 37 — The Partridge | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 37 — the traditional source for the famous story of "
        "a partridge, monkey, and elephant who found happiness by "
        "honoring their eldest. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, source of a widely known "
                       "story"),
    ],
    why=(
        "This poem is the traditional source for one of the "
        "best-known friendship stories associated with the Jātaka "
        "tradition &mdash; three animals of unequal size and status "
        "who found lasting happiness together simply by determining, "
        "and then honoring, who among them was eldest."),
    guide=[
        ("A general principle about honoring elders", [
            "The verse states its principle in general terms: "
            "&lsquo;those people who honor the elder are experts in "
            "the teaching; praised in this life, they're destined for "
            "happiness in the next.&rsquo; On its own, the verse "
            "makes no mention of any specific animals."]),
        ("The specific story behind a general teaching", [
            "Per Sujato's comment, the underlying story concerns a "
            "partridge, a monkey, and an elephant who were friends "
            "and lived happily because they honored the eldest among "
            "them. This tale &mdash; determining seniority not by "
            "size or strength but by whichever animal remembered the "
            "oldest landmark or memory &mdash; became one of the most "
            "widely retold friendship stories associated with this "
            "collection, though the verse itself states only the "
            "general principle the story illustrates."]),
    ],
    terms=[
        ("vuḍḍham apacāyanti",
         "&ldquo;honor the elder&rdquo; &mdash; the verse's central "
         "principle."),
        ("dhammassa kovidā",
         "&ldquo;experts in the teaching&rdquo; &mdash; what those "
         "who honor the elder are said to become."),
        ("diṭṭheva dhamme pāsaṁsā",
         "&ldquo;praised in this life&rdquo; &mdash; the immediate "
         "reward the verse names, alongside a future one."),
        ("Tittirajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Partridge&rsquo; &mdash; though the verse itself concerns "
         "a principle shared by a partridge, monkey, and elephant "
         "together."),
        ("partridge, monkey, and elephant",
         "the three animal friends of the underlying commentarial "
         "story, per Sujato's comment, who found happiness by "
         "honoring whichever of them was eldest."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja37:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What principle does the verse state, in general terms?',
         "opts": [
             'That those who honor the elder are experts in the teaching, praised now and destined for future happiness',
             'That strength determines status',
             'No principle is stated',
             'That wealth brings happiness',
         ],
         "correct": 0,
         "expl": 'Stated generally, without naming any specific animals.'},
        {"q": 'What three animals does the underlying commentarial story involve?',
         "opts": [
             'A tiger, a snake, and a bird',
             'A partridge, a monkey, and an elephant',
             'A fish, a crab, and a crane',
             'The comment names no specific animals',
         ],
         "correct": 1,
         "expl": 'Friends who lived happily by honoring the eldest among them.'},
        {"q": 'Does the verse itself name these three specific animals?',
         "opts": [
             'Only the elephant is named',
             'Yes, all three are named directly',
             'No — the verse states only the general principle the story illustrates',
             'Only the partridge is named',
         ],
         "correct": 2,
         "expl": 'The specific story comes entirely from the commentarial tradition, not the canonical verse.'},
        {"q": 'How, per the wider tradition, did the three animals determine seniority?',
         "opts": [
             'By strength alone',
             'By a formal vote',
             'By size alone',
             'By whichever animal remembered the oldest landmark or memory, not by size or strength',
         ],
         "correct": 3,
         "expl": 'A distinctive method that made the story widely memorable.'},
        {"q": 'What reward does the verse promise for honoring the elder?',
         "opts": [
             'Both being praised in this life and happiness destined for the next',
             'Only a this-life reward',
             'No reward is mentioned',
             'Only a future-life reward',
         ],
         "correct": 0,
         "expl": 'A double benefit spanning both present and future.'},
        {"q": 'How well-known is this tale, per this reading guide?',
         "opts": [
             'Largely obscure and rarely retold',
             'One of the best-known friendship stories associated with the Jātaka tradition',
             'Known only to specialists',
             'Not connected to any wider tradition',
         ],
         "correct": 1,
         "expl": 'Its traditional source lies in this compact verse.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Nanda',
             'Bird',
             'The Partridge (Tittirajātaka)',
             'The Crane',
         ],
         "correct": 2,
         "expl": 'The thirty-seventh poem overall, and the seventh of the Kulāvakavagga — named for one of the three friends, though the verse itself is general.'},
        {"q": 'What relationship do the three animals have to each other in the underlying story?',
         "opts": [
             'They are strangers',
             'They are predator and prey',
             'They are rivals',
             'They are friends',
         ],
         "correct": 3,
         "expl": 'Living happily together through mutual respect for seniority.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The seventh poem of the Kulāvakavagga, following Ja 31 through Ja 36',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": 'What does this poem illustrate about the relationship between canonical verse and commentarial story in this collection?',
         "opts": [
             'They are always identical in detail',
             'A general canonical principle can correspond to a much more specific and memorable commentarial narrative',
             'The verse and story are always unrelated',
             'The verse always contains more detail than the story',
         ],
         "correct": 1,
         "expl": 'A pattern seen repeatedly across this partial Jātaka selection.'},
    ],
    marginalia=[
        ("A principle, stated without a story", [
            "the verse alone just says 'honor the elder' —",
            "the specific tale lives only in commentary"
        ]),
        ("Three friends, one method of seniority", [
            "not size, not strength, but memory —",
            "whoever recalled the oldest landmark led"
        ]),
        ("A widely retold tale, traced to one verse", [
            "the partridge, monkey, and elephant's fame —",
            "traced back to these four compact lines"
        ]),
        ("A double reward for a simple respect", [
            "praised now, destined well later —",
            "honoring an elder pays twice over"
        ]),
    ],
    further=[
        '<a href="%s/ja37/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-36.html">Ja 36 &mdash; Bird</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="ja-38.html">Ja 38 &mdash; The Crane</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 38 — Baka (The Crane)
# --------------------------------------------------------------------------- #
page(
    38, "Baka", "The Crane",
    meta_title="Ja 38 — The Crane | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 38 — a scheming crane outplayed by the very crab it "
        "tried to deceive, and a proverb about the limits of "
        "cleverness. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short proverb about the limits of "
                       "cheating"),
    ],
    why=(
        "This poem's proverb &mdash; that a clever cheat can never "
        "achieve real happiness through cheating &mdash; is "
        "sharpened by its own punchline: the crane's fraud succeeds "
        "only in getting him exactly what a crab, of all creatures, "
        "was able to do to him instead."),
    guide=[
        ("A proverb about the ceiling on what cheating can achieve", [
            "The verse states its principle, then delivers its own "
            "ironic proof: &lsquo;the clever cheat cannot achieve "
            "ultimate happiness by cheating. The clever cheat "
            "succeeds only in getting what the crane did from the "
            "crab.&rsquo; The final line is deliberately withholding "
            "&mdash; the reader must already know, or find out via "
            "the commentary, exactly what the crab did to the "
            "crane."]),
        ("A trickster outplayed by its own intended victim", [
            "Per Sujato's comment, the crane, appearing to "
            "contemplate deeply as it waits beside the pond, catches "
            "fish by means of fraud &mdash; but is ultimately "
            "&lsquo;outplayed by the canny crab&rsquo;, a creature it "
            "presumably expected to be an easy target. The specific "
            "irony is that the crane's downfall comes not from a "
            "stronger predator, but from the very kind of victim it "
            "assumed it could deceive without consequence."]),
    ],
    terms=[
        ("nikatippañño",
         "&ldquo;the clever cheat&rdquo; &mdash; the verse's own "
         "term for someone whose intelligence is put entirely toward "
         "deception."),
        ("nāccantaṁ... sukhamedhati",
         "&ldquo;cannot achieve ultimate happiness&rdquo; &mdash; "
         "the verse's central claim about the limits of cheating."),
        ("bako kakkaṭakāmiva",
         "&ldquo;what the crane did from the crab&rdquo; &mdash; the "
         "verse's own withheld punchline, requiring outside context "
         "to fully land."),
        ("Bakajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Crane&rsquo;."),
        ("kakkaṭaka",
         "&ldquo;crab&rdquo; &mdash; per Sujato's comment, the "
         "seemingly easy target who ultimately outplays the "
         "scheming crane."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja38:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse claim about the 'clever cheat'?",
         "opts": [
             'That cheating always leads to lasting happiness',
             'That the clever cheat cannot achieve ultimate happiness by cheating',
             'That cheating is impossible to detect',
             'No claim is made about cheating',
         ],
         "correct": 1,
         "expl": "The verse's central proverb about the limits of deception."},
        {"q": "How does the crane catch fish, per Sujato's comment?",
         "opts": [
             "The comment does not describe the crane's method",
             'Through honest effort',
             'By fraud, appearing to contemplate deeply while waiting beside the pond',
             'By asking politely',
         ],
         "correct": 2,
         "expl": 'A deceptive appearance masking predatory intent.'},
        {"q": 'Who ultimately outplays the crane?',
         "opts": [
             'Another crane',
             'The fish themselves',
             'A larger predator',
             'The crab, a seemingly easy target',
         ],
         "correct": 3,
         "expl": 'The specific irony central to this tale.'},
        {"q": "What does the verse's final line deliberately withhold?",
         "opts": [
             'The specific detail of what happened between the crane and the crab, requiring outside context to fully understand',
             "The crane's name",
             'The location of the pond',
             'Nothing is withheld',
         ],
         "correct": 0,
         "expl": 'A compact reference assuming the audience already knows or will learn the fuller story.'},
        {"q": 'What kind of victim did the crane presumably expect the crab to be?',
         "opts": [
             'A dangerous and difficult target',
             'An easy target, no different from the fish it had already deceived',
             'Not a target at all',
             'The verse does not address this',
         ],
         "correct": 1,
         "expl": "Making its downfall at the crab's hands especially ironic."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Pit of Acacia Coals',
             'The Partridge',
             'The Crane (Bakajātaka)',
             'Nanda',
         ],
         "correct": 2,
         "expl": 'The thirty-eighth poem overall, and the eighth of the Kulāvakavagga.'},
        {"q": 'What broader point does this proverb make about intelligence used for deception?',
         "opts": [
             'That it is morally neutral',
             'That it only fails against stronger creatures',
             'That it always succeeds',
             "That it has a ceiling — it cannot deliver 'ultimate happiness', and can be turned back on the cheat by an unexpected opponent",
         ],
         "correct": 3,
         "expl": "The crane's fraud is defeated not by strength but by a cleverness matching or exceeding its own."},
        {"q": 'What method does the crane use to appear non-threatening while hunting?',
         "opts": [
             'Standing still, appearing to contemplate deeply',
             'Approaching loudly',
             'No specific method is described',
             'Hiding entirely',
         ],
         "correct": 0,
         "expl": 'A deceptive posture that presumably worked on the fish, but not on the crab.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The eighth poem of the Kulāvakavagga, following Ja 31 through Ja 37',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Kulāvakavagga.'},
        {"q": "How does this verse's structure use compression for effect?",
         "opts": [
             'It repeats the same line four times',
             'It spells out every detail explicitly',
             'It states a general principle, then delivers a specific, withheld punchline that requires outside knowledge to appreciate',
             'It avoids any specific reference entirely',
         ],
         "correct": 2,
         "expl": 'A technique found across several poems in this partial selection.'},
    ],
    marginalia=[
        ("A cheat's own ceiling", [
            "cleverness in deception only goes so far —",
            "'ultimate happiness' stays out of reach"
        ]),
        ("Outplayed by the expected easy mark", [
            "not a stronger predator, but a crab —",
            "the irony is the whole point"
        ]),
        ("A punchline the verse won't spell out", [
            "'what the crane did from the crab' —",
            "you already have to know the story"
        ]),
        ("Contemplation as a mask for hunting", [
            "stillness that looked like wisdom —",
            "fooling fish, but not this one crab"
        ]),
    ],
    further=[
        '<a href="%s/ja38/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-37.html">Ja 37 &mdash; The Partridge</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-39.html">Ja 39 &mdash; Nanda</a> &mdash; the '
        "next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 39 — Nanda
# --------------------------------------------------------------------------- #
page(
    39, "Nanda", "Nanda",
    meta_title="Ja 39 — Nanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 39 — a coded verse hiding a buried inheritance behind "
        "a resentful servant's curses. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A son and a trusted family servant, standing at "
                    "a hidden location"),
        ("Speaker", "The son, working out the meaning behind the "
                    "servant's odd behavior"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; a genuine riddle requiring the "
                       "comment to unpack"),
    ],
    why=(
        "This tale hinges on a genuinely clever piece of behavioral "
        "reading: a servant's odd, hostile behavior is not what it "
        "first appears, and Sujato's comment unpacks exactly how a "
        "coded curse reveals the very information it seems to be "
        "hiding."),
    guide=[
        ("A son's suspicion, and a riddle solved through inference", [
            "The verse gives the son's own reasoning: &lsquo;I "
            "suspect the heap of gold and golden chains is where the "
            "house-born slave Nandaka stands yelling curses.&rsquo; "
            "Per Sujato's comment, before his death the father had "
            "entrusted only his servant Nanda with the location of "
            "his buried wealth, fearing his young wife would waste "
            "the inheritance on a new man rather than pass it to her "
            "son. When the servant arrives at the location with the "
            "heir, conceit leads him to curse rather than simply "
            "reveal the treasure &mdash; but his very presence and "
            "hostility at that specific spot gives the location "
            "away."]),
        ("The real motivation hidden inside an insult", [
            "Sujato's comment adds a further layer: having served the "
            "father since birth, Nanda was addressed as &lsquo;my "
            "dear&rsquo; and even &lsquo;uncle&rsquo;, treated almost "
            "as family. His curse against the young wife and son "
            "&mdash; calling the son &lsquo;you bastard son of a "
            "slave girl&rsquo; &mdash; reveals, per the comment, his "
            "real resentment: not simple loyalty being tested, but a "
            "servant who felt he deserved more standing than he was "
            "given, and who is finally saying so, however "
            "indirectly."]),
    ],
    terms=[
        ("sovaṇṇayo rāsi",
         "&ldquo;heap of gold&rdquo; &mdash; the buried inheritance "
         "the son is trying to locate."),
        ("āmajāto",
         "&ldquo;house-born&rdquo; &mdash; per Sujato's comment, "
         "from a Vedic root meaning &lsquo;house&rsquo;, though the "
         "traditional commentary explains it as &lsquo;with "
         "consent&rsquo;."),
        ("thullāni gajjati",
         "&ldquo;stands yelling curses&rdquo; &mdash; the servant's "
         "own hostile behavior, which paradoxically gives away the "
         "treasure's location."),
        ("Nandajātaka",
         "the traditional title of this tale, named for the servant "
         "Nanda."),
        ("tāta / mātula",
         "&ldquo;my dear&rdquo; and &ldquo;uncle&rdquo; &mdash; the "
         "affectionate, near-familial terms the servant was "
         "traditionally addressed with, per Sujato's comment, making "
         "his eventual resentment more pointed."),
    ],
    text_intro=(
        "The text in full: a single verse, requiring Sujato's "
        "comment to unpack its riddling logic, discussed above. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja39:1.1-1.4"),
    ],
    quiz=[
        {"q": "What information did the father entrust only to his servant Nanda, per Sujato's comment?",
         "opts": [
             'The location of a hidden weapon',
             'The identity of a rival',
             'The location of his buried wealth',
             'A secret family recipe',
         ],
         "correct": 2,
         "expl": 'Fearing his young wife would waste the inheritance rather than pass it to her son.'},
        {"q": "How does the son ultimately work out the treasure's location?",
         "opts": [
             'Through a written map',
             'By digging randomly until he finds it',
             'The servant tells him directly',
             "By recognizing that the servant's hostile cursing at a specific spot reveals that location",
         ],
         "correct": 3,
         "expl": "The very location of Nanda's outburst gives away what he seems to be trying to withhold."},
        {"q": 'Why, per the comment, does Nanda curse instead of simply revealing the treasure?',
         "opts": [
             'Out of conceit, and underlying resentment at his own status',
             "He is testing the son's patience",
             'He genuinely wants to keep the gold for himself',
             'He has completely forgotten the location',
         ],
         "correct": 0,
         "expl": 'Revealed further by the specific insult he directs at the son and his mother.'},
        {"q": 'What insult does Nanda direct at the son, per the comment?',
         "opts": [
             'A comment about his intelligence',
             "'You bastard son of a slave girl'",
             'A comment about his appearance',
             'No specific insult is recorded',
         ],
         "correct": 1,
         "expl": 'Revealing his real feelings toward the young wife and her son.'},
        {"q": "How was Nanda traditionally treated by the family, per Sujato's comment?",
         "opts": [
             'The comment does not address this',
             'As an ordinary servant with no special regard',
             "Almost as family, addressed as 'my dear' and even 'uncle'",
             'With open hostility from the start',
         ],
         "correct": 2,
         "expl": 'Making his eventual resentment and hostile outburst more pointed.'},
        {"q": "What does Sujato's comment say about the term 'āmajāto'?",
         "opts": [
             'It is a proper name',
             'The comment does not address this term',
             'It has an uncontested single meaning',
             "It derives from a Vedic root meaning 'house', though traditionally explained as 'with consent'",
         ],
         "correct": 3,
         "expl": "One of several philological notes threaded through this chapter's comments."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Nanda (Nandajātaka)',
             'The Pit of Acacia Coals',
             'The Partridge',
             'The Crane',
         ],
         "correct": 0,
         "expl": 'The thirty-ninth poem overall, and the ninth of the Kulāvakavagga, named for the servant.'},
        {"q": 'Why did the father specifically fear entrusting the location to his young wife?',
         "opts": [
             'He did not trust her intelligence',
             'He feared she would waste the inheritance on a new man rather than pass it to her son',
             'She had already betrayed him once',
             'No specific fear is given',
         ],
         "correct": 1,
         "expl": "The underlying motive for the father's unusual arrangement with his servant instead."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The ninth poem of the Kulāvakavagga, following Ja 31 through Ja 38',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'The second-to-last poem of this ten-poem chapter.'},
        {"q": "What makes this poem's central riddle distinctive among this chapter's other poems?",
         "opts": [
             'It is the only poem in the chapter about a human, not an animal',
             'It is the shortest poem in the chapter',
             'It requires no interpretation at all',
             'It hinges on a genuinely clever piece of behavioral reading — hostile behavior paradoxically revealing hidden information',
         ],
         "correct": 3,
         "expl": "A different kind of cleverness from this chapter's animal fables — psychological rather than purely moral."},
    ],
    marginalia=[
        ("A curse that gives away the secret", [
            "yelling at exactly the wrong spot —",
            "the outburst reveals what silence would have hidden"
        ]),
        ("Resentment, finally spoken", [
            "'my dear', 'uncle' — until this moment —",
            "the insult reveals what was always beneath the surface"
        ]),
        ("A father's careful, distrustful plan", [
            "the location entrusted to a servant, not a wife —",
            "protecting an inheritance he feared would be squandered"
        ]),
        ("Inference as the real solution", [
            "no confession needed, just careful reading —",
            "the son works it out from behavior alone"
        ]),
    ],
    further=[
        '<a href="%s/ja39/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-38.html">Ja 38 &mdash; The Crane</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-40.html">Ja 40 &mdash; The Pit of Acacia '
        "Coals</a> &mdash; the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 40 — Khadiraṅgāra (The Pit of Acacia Coals)
# --------------------------------------------------------------------------- #
page(
    40, "Khadira&#7749;g&amacr;ra", "The Pit of Acacia Coals",
    meta_title="Ja 40 — The Pit of Acacia Coals | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 40, closing the Kulāvakavagga — the Bodhisatta's "
        "unshaken resolve to give alms even facing an illusory pit of "
        "burning coals conjured by Māra. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter Four (Kulāvakavagga) &middot; Poem 10 of 10 (closing the chapter)",
    glance=[
        ("Setting", "The edge of what appears to be a vast pit of "
                    "burning coals"),
        ("Speaker", "The Bodhisatta"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of absolute resolve"),
    ],
    why=(
        "This poem closes the Kulāvakavagga with one of this "
        "collection's clearest declarations of unshaken generosity: "
        "the Bodhisatta, confronted with what appears to be certain "
        "death by fire, chooses to give rather than retreat, framing "
        "the refusal to act nobly as a worse fate than hell itself."),
    guide=[
        ("Choosing generosity over self-preservation, even facing hell itself", [
            "The verse states its resolve without hesitation: "
            "&lsquo;fine, let me fall head over heels into hell, but "
            "I shall not do what is ignoble. Please accept my alms "
            "offering.&rsquo; The logic inverts ordinary "
            "self-preservation entirely: falling into hell is treated "
            "as an acceptable cost, while failing to act nobly is "
            "not."]),
        ("An illusion created specifically to block generosity", [
            "Per Sujato's comment, Māra, in order to prevent the "
            "Bodhisatta from giving alms to a Paccekabuddha (a "
            "solitary awakened being), creates an illusion of a vast "
            "pit burning with coals of acacia wood directly in his "
            "path. The obstacle is not incidental danger but a "
            "deliberate attempt to intimidate the Bodhisatta out of "
            "his own generosity &mdash; and, per the comment, "
            "&lsquo;the Bodhisatta is not intimidated.&rsquo;"]),
        ("Closing the Kulāvakavagga", [
            "This poem closes the Kulāvakavagga, the fourth of eight "
            "chapters this site's selection draws from within the "
            "Ekakanipāta. The source text's own untranslated summary "
            "verse (uddāna) immediately follows, naming all ten poems "
            "of this chapter in sequence &mdash; not presented here "
            "as quoted text, since it carries no separate translation, "
            "but noted for completeness, as at the close of the "
            "previous three chapters."]),
    ],
    terms=[
        ("kāmaṁ patāmi nirayaṁ",
         "&ldquo;fine, let me fall into hell&rdquo; &mdash; the "
         "Bodhisatta's own opening statement of resolve."),
        ("nānariyaṁ karissāmi",
         "&ldquo;I shall not do what is ignoble&rdquo; &mdash; the "
         "verse's central commitment, prioritized above even hell "
         "itself."),
        ("handa piṇḍaṁ paṭiggaha",
         "&ldquo;please accept my alms offering&rdquo; &mdash; the "
         "Bodhisatta's direct request, addressed to the "
         "Paccekabuddha, even as the illusory pit burns before him."),
        ("Khadiraṅgārajātaka",
         "the traditional title of this tale, &lsquo;The Pit of "
         "Acacia Coals&rsquo;, closing the Kulāvakavagga."),
        ("Paccekabuddha",
         "a solitary awakened being, per Sujato's comment the "
         "intended recipient of the Bodhisatta's alms, whose gift "
         "Māra attempts to prevent through illusion."),
    ],
    text_intro=(
        "The text in full: a single verse. The chapter's own "
        "untranslated closing summary verse (uddāna), which follows "
        "immediately in the source text, is not quoted here since it "
        "carries no English translation, but its content &mdash; the "
        "ten poem titles of this chapter in sequence &mdash; matches "
        "this reading guide's own further reading list below. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja40:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the Bodhisatta say he is willing to do rather than act ignobly?',
         "opts": [
             'Abandon the alms offering',
             'Retreat immediately',
             'Nothing — he refuses to take any risk',
             'Fall head over heels into hell',
         ],
         "correct": 3,
         "expl": 'An inversion of ordinary self-preservation, prioritizing noble action above even that extreme cost.'},
        {"q": "Who created the illusion of the burning pit, per Sujato's comment?",
         "opts": [
             'Māra, specifically to prevent the Bodhisatta from giving alms',
             'The Paccekabuddha himself',
             'No specific source is given',
             'A hostile king',
         ],
         "correct": 0,
         "expl": 'A deliberate obstacle, not incidental danger.'},
        {"q": 'Who was the Bodhisatta trying to give alms to?',
         "opts": [
             'A king',
             'A Paccekabuddha (a solitary awakened being)',
             'A group of beggars',
             'His own family',
         ],
         "correct": 1,
         "expl": "The generosity Māra's illusion was specifically designed to prevent."},
        {"q": 'How does the Bodhisatta respond to the illusory pit?',
         "opts": [
             'He calls for help',
             'He is intimidated and turns back',
             'He is not intimidated, and proceeds to offer the alms',
             'He attacks the illusion directly',
         ],
         "correct": 2,
         "expl": "Per Sujato's comment, stated directly: 'the Bodhisatta is not intimidated.'"},
        {"q": 'What chapter does this poem close?',
         "opts": [
             'The final chapter of the whole Jātaka',
             'It does not close a chapter',
             'The Sīlavagga',
             "The Kulāvakavagga, the fourth of eight chapters this site's selection draws from",
         ],
         "correct": 3,
         "expl": "The source text's own untranslated summary verse (uddāna) follows immediately after."},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'No — it carries no separate English translation, so it is only noted for completeness',
             'It does not exist for this chapter',
             'It is presented as spoken by Māra',
             'Yes, quoted in full',
         ],
         "correct": 0,
         "expl": 'Consistent with the same practice at the close of the previous three chapters.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Nanda',
             'The Pit of Acacia Coals (Khadiraṅgārajātaka)',
             'The Crane',
             'The Partridge',
         ],
         "correct": 1,
         "expl": 'The fortieth poem overall, and the tenth and final poem of the Kulāvakavagga.'},
        {"q": "What material was the illusory pit's coals made of?",
         "opts": [
             'The verse does not specify',
             'Ordinary charcoal',
             'Acacia wood',
             'Sandalwood',
         ],
         "correct": 2,
         "expl": 'Giving this poem its traditional title.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The first poem of a later chapter',
             'The first poem of the Kulāvakavagga',
             'The tenth and final poem of the Kulāvakavagga, closing this chapter',
         ],
         "correct": 3,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse following immediately after."},
        {"q": "How many poems of this site's 82-poem Jātaka selection are complete after this one?",
         "opts": [
             'Forty',
             'Sixty',
             'All eighty-two',
             'Twenty',
         ],
         "correct": 0,
         "expl": 'Four of eight Ekakanipāta chapters now complete.'},
    ],
    marginalia=[
        ("Hell accepted, ignobility refused", [
            "the verse's whole priority in one line —",
            "'I shall not do what is ignoble'"
        ]),
        ("An illusion built to stop generosity", [
            "Māra's own deliberate obstacle —",
            "not incidental danger, but a targeted attempt"
        ]),
        ("Not intimidated, and still giving", [
            "the offering completed anyway —",
            "the pit proves to be exactly what it was: an illusion"
        ]),
        ("Forty poems, four chapters closed", [
            "the Kulāvakavagga's own summary follows —",
            "not quoted, since it has no translation"
        ]),
    ],
    further=[
        '<a href="%s/ja40/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-39.html">Ja 39 &mdash; Nanda</a> &mdash; the '
        "poem immediately before this one.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 41 — Losaka (About Losaka)
# --------------------------------------------------------------------------- #
page(
    41, "Losaka", "About Losaka",
    meta_title="Ja 41 — About Losaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 41, opening the Atthakāmavagga — the first of five "
        "poems sharing a refrain about ignoring good advice, this one "
        "illustrated by an absurd fate 'hanging off a goat's foot'. "
        "From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, opening a five-poem refrain "
                 "sequence"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, part of a formulaic sequence"),
    ],
    why=(
        "This poem opens a run of five consecutive poems (Ja "
        "41&ndash;45) sharing an identical two-line opening refrain "
        "&mdash; about ignoring the advice of someone who genuinely "
        "wants your good &mdash; each completed by a different, "
        "increasingly specific illustrative comparison. This "
        "chapter's very structure is worth noticing before reading "
        "any single poem within it."),
    guide=[
        ("A refrain that will repeat across the next four poems", [
            "The verse opens: &lsquo;one who does not follow advice "
            "when instructed by an ally who desires their good...&rsquo; "
            "&mdash; a couplet that recurs, word for word, at the "
            "opening of Ja 42, 43, and in modified form at 44 and 45. "
            "Only the second half changes each time, supplying a "
            "different example of what happens to someone who ignores "
            "good counsel."]),
        ("This poem's own absurd example", [
            "Here the illustration is deliberately strange: "
            "&lsquo;grieves like Mittaka hanging off a goat's "
            "foot.&rsquo; Per Sujato's comment, the full explanation "
            "of how Mittaka (also called Mittavindaka, or Losaka "
            "Tissa in a later life) came to be in that position is "
            "&lsquo;absurd and too complex to relate here&rsquo; "
            "&mdash; the comment notes this collates several "
            "archetypal scapegoat stories, using absurdity for "
            "humorous effect while still subsuming the tale under the "
            "doctrine of kamma. His troubles, per the comment, trace "
            "back across many lives to an act of jealousy toward an "
            "arahant."]),
    ],
    terms=[
        ("atthakāmassa hitānukampino",
         "&ldquo;an ally who desires their good&rdquo; &mdash; the "
         "figure whose advice, ignored, sets up each poem's "
         "consequence, giving this whole chapter its name."),
        ("Mittaka / Mittavindaka / Losaka Tissa",
         "per Sujato's comment, three names for the same figure "
         "across different points of his story &mdash; his past-life "
         "name, his more common name, and his name in the present-"
         "life story."),
        ("ajiyā pādamolamba",
         "&ldquo;hanging off a goat's foot&rdquo; &mdash; the "
         "poem's own deliberately strange central image."),
        ("Losakajātaka",
         "the traditional title of this tale, opening the "
         "Atthakāmavagga."),
        ("scapegoat archetype",
         "an ancient mythic and ritual pattern that, per Sujato's "
         "comment, this tale's absurd events draw on and recast "
         "under the doctrine of kamma."),
    ],
    text_intro=(
        "The text in full: a single verse, opening a five-poem "
        "refrain sequence. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja41:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this poem's opening refrain share with the next several poems?",
         "opts": [
             'Nothing — it is unique to this poem',
             'An identical or closely related two-line opening about ignoring good advice, repeated with variations across Ja 41-45',
             'The same closing image each time',
             "The same speaker's name",
         ],
         "correct": 0,
         "expl": 'Only the second half of each poem changes, supplying a different illustrative example.'},
        {"q": "What image completes this particular poem's refrain?",
         "opts": [
             'A description of a storm',
             "Grieving like Mittaka, hanging off a goat's foot",
             'A description of a shipwreck',
             'No specific image is given',
         ],
         "correct": 1,
         "expl": "A deliberately strange, absurd image per Sujato's own comment."},
        {"q": "What three names does Sujato's comment give for this poem's central figure?",
         "opts": [
             'No specific names are given',
             'Only one name is used throughout',
             'Mittaka, Mittavindaka, and Losaka Tissa, across different points of his story',
             'Two unrelated figures with similar names',
         ],
         "correct": 2,
         "expl": 'His past-life name, his more common name, and his name in the present-life story.'},
        {"q": "What does Sujato's comment say about the full explanation of the goat's-foot detail?",
         "opts": [
             'It does not exist in any source',
             'It is a modern invention',
             'It is simple and easily summarized',
             "It is 'absurd and too complex to relate here'",
         ],
         "correct": 3,
         "expl": 'The comment instead explains the broader pattern the story draws on.'},
        {"q": "What ancient pattern does Sujato's comment say this tale's absurd events collate?",
         "opts": [
             'Several archetypal scapegoat stories, subsumed under the doctrine of kamma',
             'A coronation ceremony',
             'No pattern is identified',
             'A harvest ritual',
         ],
         "correct": 0,
         "expl": 'Using absurdity for humorous effect while still fitting within Buddhist doctrine.'},
        {"q": "What does the comment say is the root cause, across many lives, of Mittaka's troubles?",
         "opts": [
             'Simple bad luck',
             'An act of jealousy toward an arahant in a distant past life',
             'A curse from a king',
             'No cause is given',
         ],
         "correct": 1,
         "expl": 'His bad character, as much as his bad kamma, resulted in a series of extravagant tragedies.'},
        {"q": 'What chapter does this poem open?',
         "opts": [
             'It does not open a chapter',
             'The Kulāvakavagga',
             'The Atthakāmavagga',
             'The Āsīsavagga',
         ],
         "correct": 2,
         "expl": "This collection's fifth ten-poem chapter."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Pole Acrobat',
             'The Mosquito',
             'The Pigeon',
             'About Losaka (Losakajātaka)',
         ],
         "correct": 3,
         "expl": 'The forty-first poem overall, and the first of the Atthakāmavagga.'},
        {"q": "What tone does Sujato's comment attribute to this tale's absurdity?",
         "opts": [
             'Used for humorous effect, while still serving a doctrinal point',
             'Entirely nonsensical with no deeper meaning',
             'Meant to be taken as literal historical fact',
             'Purely tragic, with no humor',
         ],
         "correct": 0,
         "expl": 'Drawing on surreal, fantastical narratives associated with Vedic ritual, reframed under kamma.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of the Kulāvakavagga',
             'The first poem of the fifth chapter (Atthakāmavagga), following the completed Kulāvakavagga',
             'It stands outside any chapter',
             'The final poem of the Atthakāmavagga',
         ],
         "correct": 1,
         "expl": "Opening this collection's fifth ten-poem chapter, and its first refrain sequence."},
    ],
    marginalia=[
        ("A refrain that will repeat four more times", [
            "the same opening couplet, poem after poem —",
            "only the illustration changes each time"
        ]),
        ("An absurd fate, deliberately so", [
            "hanging off a goat's foot, too complex to explain —",
            "humor doing doctrinal work"
        ]),
        ("Three names, one long story", [
            "Mittaka, Mittavindaka, Losaka Tissa —",
            "one figure traced across many lives"
        ]),
        ("An old archetype, given a new frame", [
            "scapegoat myths recast as karma —",
            "ancient story-shapes still doing new work"
        ]),
    ],
    further=[
        '<a href="%s/ja41/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-40.html">Ja 40 &mdash; The Pit of Acacia '
        "Coals</a> &mdash; the closing poem of the previous chapter.",
        '<a href="ja-42.html">Ja 42 &mdash; The Pigeon</a> &mdash; '
        "the next poem, continuing this chapter's refrain sequence.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 42 — Kapota (The Pigeon)
# --------------------------------------------------------------------------- #
page(
    42, "Kapota", "The Pigeon",
    meta_title="Ja 42 — The Pigeon | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 42 — the second of five poems sharing a refrain about "
        "ignoring good advice, here a greedy crow ignoring a wise "
        "pigeon's warning. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, continuing this chapter's "
                 "refrain sequence"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, part of a formulaic sequence"),
    ],
    why=(
        "This is the second poem in this chapter's refrain sequence "
        "begun at Ja 41, and its illustration is disarmingly simple: "
        "a greedy crow ignores a wise pigeon's own good counsel and "
        "pays the ordinary, predictable price."),
    guide=[
        ("The refrain continues, with a plain animal example", [
            "The verse repeats the chapter's opening formula "
            "&mdash; &lsquo;one who does not follow advice when "
            "instructed by an ally who wants to help&rsquo; &mdash; "
            "then supplies its own illustration: &lsquo;not following "
            "the pigeon's counsel, ends up in the hands of their "
            "foes.&rsquo; Per Sujato's comment, a greedy crow ignores "
            "the warning of the wise pigeon and continues to steal "
            "food from the kitchen, with predictable consequences."]),
        ("A simpler counterpart to the previous poem's absurdity", [
            "Where Ja 41's illustration required an elaborate, "
            "&lsquo;too complex to relate&rsquo; backstory, this "
            "poem's crow-and-pigeon story is straightforward and "
            "immediately legible &mdash; showing the range this "
            "chapter's shared refrain can accommodate, from the "
            "surreal to the mundane."]),
    ],
    terms=[
        ("kapotakassa vacanaṁ",
         "&ldquo;the pigeon's counsel&rdquo; &mdash; the good advice "
         "given and ignored, giving this poem its traditional title."),
        ("amittahatthatthagatova seti",
         "&ldquo;ends up in the hands of their foes&rdquo; &mdash; "
         "the crow's predictable fate."),
        ("Kapotajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Pigeon&rsquo;."),
        ("Ja 41",
         "the previous poem, opening this chapter's shared refrain "
         "sequence, which this poem continues."),
        ("crow",
         "per Sujato's comment, the greedy party in this tale, "
         "repeatedly stealing food despite the pigeon's warning."),
    ],
    text_intro=(
        "The text in full: a single verse, continuing the refrain "
        "sequence begun at Ja 41. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja42:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this poem's opening repeat?",
         "opts": [
             'No refrain is used',
             'A completely new formula',
             "The chapter's shared refrain about ignoring the advice of an ally who wants to help",
             'A refrain about kingship',
         ],
         "correct": 1,
         "expl": "The second poem in this chapter's five-poem refrain sequence begun at Ja 41."},
        {"q": "Who ignores good advice in this poem's illustration?",
         "opts": [
             'No specific animal is named',
             'A wise pigeon',
             "A greedy crow, ignoring the pigeon's warning",
             'A hunter',
         ],
         "correct": 2,
         "expl": 'Continuing to steal food from the kitchen despite being warned.'},
        {"q": "What is the crow's fate, per the verse?",
         "opts": [
             'It is rewarded',
             'The verse does not specify',
             'It escapes unharmed',
             'It ends up in the hands of its foes',
         ],
         "correct": 3,
         "expl": "The predictable consequence of ignoring the pigeon's counsel."},
        {"q": "How does this poem's illustration compare to Ja 41's in complexity?",
         "opts": [
             'Much simpler and more straightforward — an ordinary, immediately legible story',
             'Even more complex',
             'There is no notable difference',
             'Equally complex and absurd',
         ],
         "correct": 0,
         "expl": "Showing the range this chapter's shared refrain can accommodate."},
        {"q": 'What specifically does the crow keep doing despite the warning?',
         "opts": [
             'Building a nest in the wrong place',
             'Stealing food from the kitchen',
             'Attacking other birds',
             'Flying too close to a predator',
         ],
         "correct": 1,
         "expl": "Its persistent greed despite the pigeon's counsel."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Mosquito',
             'About Losaka',
             'The Pigeon (Kapotajātaka)',
             'The Pole Acrobat',
         ],
         "correct": 2,
         "expl": 'The forty-second poem overall, and the second of the Atthakāmavagga.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The second poem of the Atthakāmavagga, following Ja 41',
         ],
         "correct": 3,
         "expl": 'Part of the same refrain sequence as Ja 41, 43, 44, and 45.'},
        {"q": 'What role does the pigeon play in this tale?',
         "opts": [
             'The wise advisor whose counsel is ignored',
             'An uninvolved bystander',
             'The one who punishes the crow',
             'The greedy party',
         ],
         "correct": 0,
         "expl": 'Giving this poem its traditional title.'},
        {"q": 'What general theme does this poem share with Ja 41?',
         "opts": [
             'No shared theme',
             'The consequence of ignoring the advice of someone who genuinely wants your good',
             'A theme about royal succession',
             'A theme about seasonal change',
         ],
         "correct": 1,
         "expl": 'Both poems are variations on the same shared refrain.'},
        {"q": "How many poems total make up this chapter's refrain sequence, including this one?",
         "opts": [
             'Three',
             'Two',
             'Five (Ja 41 through 45)',
             'Ten',
         ],
         "correct": 2,
         "expl": 'Each supplying a different illustrative example of the same underlying warning.'},
    ],
    marginalia=[
        ("The same warning, a simpler case", [
            "no absurd goat's-foot tale needed here —",
            "just a crow who wouldn't listen"
        ]),
        ("Greed, repeated until it costs everything", [
            "the kitchen raided again and again —",
            "the pigeon's counsel ignored each time"
        ]),
        ("A wise bird, unheeded", [
            "the pigeon warns, the crow persists —",
            "the outcome exactly as predicted"
        ]),
        ("The chapter's range on display", [
            "from surreal to plainly ordinary —",
            "the same refrain fits both kinds of story"
        ]),
    ],
    further=[
        '<a href="%s/ja42/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-41.html">Ja 41 &mdash; About Losaka</a> '
        "&mdash; the poem immediately before this one, opening this "
        "chapter's refrain sequence.",
        '<a href="ja-43.html">Ja 43 &mdash; The Pole Acrobat</a> '
        "&mdash; the next poem, continuing the sequence.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 43 — Veḷuka (The Pole Acrobat)
# --------------------------------------------------------------------------- #
page(
    43, "Ve&#7789;uka", "The Pole Acrobat",
    meta_title="Ja 43 — The Pole Acrobat | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 43 — a pet viper's betrayal echoing Aesop's fable, "
        "and a contrasting image of trust rewarded at this site's own "
        "SN 42.8. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, continuing this chapter's "
                 "refrain sequence"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with a cross-cultural fable "
                       "parallel"),
    ],
    why=(
        "This poem's tale of a pet viper turning on its keeper closely "
        "resembles Aesop's fable The Farmer and the Viper, a "
        "similarity Sujato's own comment notes directly, adding that "
        "this same story pattern continues to be retold in modern "
        "songs and politics."),
    guide=[
        ("A warning ignored, ending in destruction", [
            "The verse continues the chapter's refrain, closing: "
            "&lsquo;ends up destroyed like the pole acrobat's "
            "father.&rsquo; Per Sujato's comment, the underlying "
            "story concerns an ascetic who kept a viper as a pet, "
            "despite being warned it would turn on him one day "
            "&mdash; caring for it, the comment notes, &lsquo;like a "
            "father.&rsquo;"]),
        ("A story paralleled well beyond this collection", [
            "Sujato's comment observes this tale is &lsquo;similar to "
            "Aesop's fable The Farmer and the Viper&rsquo;, and that "
            "the same underlying pattern &lsquo;is retold in modern "
            "songs and politics&rsquo; &mdash; a rare case in this "
            "partial selection where a comment explicitly reaches "
            "outside the Buddhist canon entirely to note a "
            "cross-cultural parallel."]),
        ("A contrasting picture of trust well placed", [
            "Sujato's comment also points to this site's own SN 42.8, "
            "where a different pole acrobat and student are protected "
            "specifically because they do listen to each other's wise "
            "advice &mdash; the same acrobatic image used there to "
            "show trust rewarded, in direct contrast to this poem's "
            "story of trust betrayed."]),
    ],
    terms=[
        ("veḷuka",
         "&ldquo;pole acrobat&rdquo;, also the name given to the "
         "pet viper in the underlying story, per Sujato's comment "
         "named for the bamboo tube (veḷu) it lived in."),
        ("nihato seti",
         "&ldquo;ends up destroyed&rdquo; &mdash; the fate of "
         "someone who ignores good counsel, closing this poem's "
         "refrain."),
        ("Aesop's The Farmer and the Viper",
         "a Western fable Sujato's comment identifies as closely "
         "similar to this tale's underlying story."),
        ("Veḷukajātaka",
         "the traditional title of this tale, &lsquo;The Pole "
         "Acrobat&rsquo;."),
        ("SN 42.8",
         "the already-completed page on this site with a "
         "contrasting pole-acrobat image, where mutual trust is "
         "rewarded rather than betrayed."),
    ],
    text_intro=(
        "The text in full: a single verse, continuing the refrain "
        "sequence begun at Ja 41. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja43:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this poem's illustration concern, per Sujato's comment?",
         "opts": [
             'No specific story is given',
             'A dispute between two kings',
             'An ascetic who kept a viper as a pet, despite warnings it would turn on him',
             "A merchant's failed voyage",
         ],
         "correct": 2,
         "expl": "Cared for 'like a father', per the comment."},
        {"q": "What Western fable does Sujato's comment identify this tale as similar to?",
         "opts": [
             'The Boy Who Cried Wolf',
             'No Western parallel is noted',
             'The Tortoise and the Hare',
             "Aesop's The Farmer and the Viper",
         ],
         "correct": 3,
         "expl": 'A rare case where the comment reaches outside the Buddhist canon to note a cross-cultural parallel.'},
        {"q": "What does Sujato's comment say about this story pattern's later use?",
         "opts": [
             'That it continues to be retold in modern songs and politics',
             'That it was only ever used once',
             'The comment does not address later use',
             'That it disappeared from use entirely',
         ],
         "correct": 0,
         "expl": 'A pattern still recognizable and referenced today.'},
        {"q": "What already-completed page on this site does Sujato's comment point to for a contrasting image?",
         "opts": [
             'MN 51',
             'SN 42.8, where mutual trust between a pole acrobat and student is rewarded',
             'AN 8.13',
             'No contrasting page is noted',
         ],
         "correct": 1,
         "expl": 'The same acrobatic image, used there to show trust rewarded rather than betrayed.'},
        {"q": "Why was the viper named Veḷuka, per Sujato's comment?",
         "opts": [
             'No explanation is given',
             'After its color',
             'Because it lived in a tube of bamboo (veḷu)',
             "After the ascetic's own name",
         ],
         "correct": 2,
         "expl": 'Giving this poem its traditional title.'},
        {"q": 'What is the fate of the person who ignored the warning in this poem?',
         "opts": [
             'He successfully tames the viper permanently',
             'The verse does not specify',
             'He is unharmed',
             'He ends up destroyed',
         ],
         "correct": 3,
         "expl": "Closing this poem's version of the chapter's shared refrain."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Pole Acrobat (Veḷukajātaka)',
             'The Mosquito',
             'About Rohinī',
             'The Pigeon',
         ],
         "correct": 0,
         "expl": 'The forty-third poem overall, and the third of the Atthakāmavagga.'},
        {"q": "How did the ascetic treat the viper, per Sujato's comment?",
         "opts": [
             'With constant suspicion',
             "With care, 'like a father'",
             'With cruelty',
             'With indifference',
         ],
         "correct": 1,
         "expl": 'Making the eventual betrayal more poignant.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The third poem of the Atthakāmavagga, following Ja 41 and Ja 42',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same refrain sequence as Ja 41, 42, 44, and 45.'},
        {"q": "What term does Sujato's comment note is used for 'pole acrobat' at SN 42.8, differing from this poem's term?",
         "opts": [
             'A completely unrelated word',
             'No comparison of terms is made',
             'An identical term with no variation',
             "'Vaṁsika', a synonym for this poem's 'veḷuka'",
         ],
         "correct": 3,
         "expl": 'Two different words for the same profession, appearing in contrasting stories.'},
    ],
    marginalia=[
        ("A pet cared for like a child", [
            "warned it would turn on him one day —",
            "he kept it close regardless"
        ]),
        ("A fable that crosses cultures", [
            "Aesop told nearly the same story —",
            "still echoed in songs and politics today"
        ]),
        ("Trust betrayed, trust rewarded", [
            "here, destruction follows misplaced care —",
            "at SN 42.8, the same image ends differently"
        ]),
        ("A name that tells its own story", [
            "Veḷuka, for the bamboo tube it lived in —",
            "the tale's title carries its own small detail"
        ]),
    ],
    further=[
        '<a href="%s/ja43/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../samyutta-nikaya/sn-42.8.html">SN 42.8</a> '
        "&mdash; a contrasting pole-acrobat image already complete "
        "on this site, where trust is rewarded rather than betrayed.",
        "<a href=\"ja-42.html\">Ja 42 &mdash; The Pigeon</a> &mdash; "
        "the poem immediately before this one.",
        '<a href="ja-44.html">Ja 44 &mdash; The Mosquito</a> '
        "&mdash; the next poem, continuing this chapter's sequence.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 44 — Makasa (The Mosquito)
# --------------------------------------------------------------------------- #
page(
    44, "Makasa", "The Mosquito",
    meta_title="Ja 44 — The Mosquito | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 44 — an idiot son's fatal overcorrection while trying "
        "to help his father, and a proverb preferring a considerate "
        "foe to a careless friend. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, a variant of this chapter's "
                 "refrain sequence"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, darkly comic verse"),
    ],
    why=(
        "This poem shifts the chapter's refrain from ignoring good "
        "advice to a related but distinct danger: well-meaning help "
        "delivered without judgment, illustrated by one of this "
        "collection's most darkly comic single images &mdash; a son "
        "who kills the mosquito on his father's head with an axe, "
        "killing his father in the process."),
    guide=[
        ("A modified refrain, and its own grim proof", [
            "The verse restates the chapter's underlying concern in "
            "new terms: &lsquo;better is a considerate foe than an "
            "inconsiderate friend&rsquo; &mdash; then delivers its "
            "proof: &lsquo;thinking, “I shall kill the mosquito”, the "
            "idiot son split open his father's head.&rsquo;"]),
        ("Good intentions, applied without any judgment", [
            "Per Sujato's comment, when the carpenter asked his son "
            "to rid him of a troublesome mosquito on his scalp, "
            "&lsquo;he did not think he would do it with an axe.&rsquo; "
            "The tragedy is not malice but a complete absence of "
            "proportion or judgment &mdash; the son genuinely wants to "
            "help, and that is precisely what makes the outcome "
            "possible."]),
    ],
    terms=[
        ("seyyo amitto matiyā upeto",
         "&ldquo;better is a considerate foe&rdquo; &mdash; the "
         "poem's opening proverb, reframing this chapter's concern in "
         "terms of judgment rather than loyalty."),
        ("mativippahīno",
         "&ldquo;inconsiderate&rdquo;, literally &ldquo;devoid of "
         "judgment&rdquo; &mdash; the disqualifying flaw in the "
         "well-meaning friend."),
        ("putto pitu abbhidā uttamaṅgaṁ",
         "&ldquo;the son split open his father's head&rdquo; "
         "&mdash; the poem's darkly comic proof of its own proverb."),
        ("Makasajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Mosquito&rsquo;."),
        ("eḷamūgo",
         "&ldquo;idiot&rdquo; &mdash; the verse's own blunt "
         "description of the son."),
    ],
    text_intro=(
        "The text in full: a single verse, continuing this chapter's "
        "sequence in modified form. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja44:1.1-1.4"),
    ],
    quiz=[
        {"q": "What proverb does this poem's opening state?",
         "opts": [
             'That a considerate foe is better than an inconsiderate friend',
             'That mosquitoes are more dangerous than they appear',
             'No proverb is stated',
             'That family is always more trustworthy than strangers',
         ],
         "correct": 3,
         "expl": "Reframing this chapter's underlying concern in terms of judgment rather than loyalty."},
        {"q": "What does the son do, trying to kill the mosquito on his father's head?",
         "opts": [
             "He splits open his father's head with an axe",
             'He asks someone else for help',
             'He fails to find the mosquito',
             'He successfully swats it away',
         ],
         "correct": 0,
         "expl": "The poem's own darkly comic proof of its opening proverb."},
        {"q": "What does Sujato's comment say the father expected?",
         "opts": [
             'That his son would use an axe',
             'He did not think his son would use an axe to solve the problem',
             'He expected to be killed',
             'No expectation is described',
         ],
         "correct": 1,
         "expl": 'Making the outcome a genuine, tragic surprise.'},
        {"q": "What is identified as the real flaw in the son's action?",
         "opts": [
             'Cowardice',
             'Malice',
             'A complete absence of proportion or judgment, despite genuinely good intentions',
             'Physical weakness',
         ],
         "correct": 2,
         "expl": 'The tragedy is precisely that he wanted to help.'},
        {"q": "How does this proverb relate to the previous poems' shared refrain?",
         "opts": [
             'It directly repeats the exact same words',
             'It contradicts the previous poems entirely',
             'It has no relationship at all',
             "It's a related but distinct danger — not ignoring advice, but well-meaning help delivered without judgment",
         ],
         "correct": 3,
         "expl": "A modification of the chapter's underlying concern about the risks connected to trusted relationships."},
        {"q": 'What word does the verse use to describe the son directly?',
         "opts": [
             "'Idiot' (eḷamūgo)",
             'Careful',
             'Cruel',
             'Wise',
         ],
         "correct": 0,
         "expl": 'A blunt assessment matching the outcome.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Pole Acrobat',
             'The Mosquito (Makasajātaka)',
             'About Rohinī',
             'Spoiling the Park',
         ],
         "correct": 1,
         "expl": 'The forty-fourth poem overall, and the fourth of the Atthakāmavagga.'},
        {"q": "What profession did the father have, per Sujato's comment?",
         "opts": [
             'A merchant',
             'A farmer',
             'A carpenter',
             'A fisherman',
         ],
         "correct": 2,
         "expl": 'Asking his son for a simple favor with unexpectedly fatal results.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fourth poem of the Atthakāmavagga, following Ja 41 through Ja 43',
         ],
         "correct": 3,
         "expl": 'Part of the same refrain sequence, with this and the next poem sharing a modified opening.'},
        {"q": "What tone does this reading guide identify in this poem's central image?",
         "opts": [
             'Darkly comic',
             'Lighthearted with no serious point',
             'Entirely absurdist with no moral',
             'Purely solemn with no humor',
         ],
         "correct": 0,
         "expl": "One of this collection's most darkly comic single images."},
    ],
    marginalia=[
        ("A favor that turns fatal", [
            "kill the mosquito, the father asked —",
            "not expecting an axe as the answer"
        ]),
        ("Good intentions, no judgment at all", [
            "not malice, just a total absence of proportion —",
            "the tragedy is that he wanted to help"
        ]),
        ("A proverb proven in the darkest way", [
            "better an enemy who thinks —",
            "than a friend who doesn't"
        ]),
        ("One of this collection's bleakest jokes", [
            "the image lands as both comic and horrifying —",
            "a single line doing double duty"
        ]),
    ],
    further=[
        '<a href="%s/ja44/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-43.html">Ja 43 &mdash; The Pole Acrobat</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-45.html">Ja 45 &mdash; About Rohinī</a> '
        "&mdash; the next poem, closing this chapter's refrain "
        "sequence.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 45 — Rohiṇī (About Rohinī)
# --------------------------------------------------------------------------- #
page(
    45, "Rohi&#7751;&imacr;", "About Rohinī",
    meta_title="Ja 45 — About Rohinī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 45, closing this chapter's refrain sequence — a "
        "servant girl's accidental matricide while trying to swat "
        "flies away from her mother. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, closing this chapter's "
                 "refrain sequence"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; a grim companion to Ja 44, with a "
                       "genuine textual puzzle"),
    ],
    why=(
        "This poem closes the five-poem refrain sequence begun at Ja "
        "41 with a tale strikingly similar to the previous poem's "
        "&mdash; a well-meaning act of care, misapplied, causing "
        "exactly the death it was meant to prevent &mdash; and "
        "Sujato's comment flags a specific word in the opening line "
        "that even the traditional commentary cannot satisfactorily "
        "explain."),
    guide=[
        ("A second version of the same tragic pattern", [
            "The verse restates the proverb once more: &lsquo;better "
            "is an intelligent foe than a foolish sympathizer&rsquo; "
            "&mdash; then delivers its own grim proof: &lsquo;see that "
            "wretched Rohinī, grieving after killing her "
            "mother.&rsquo; Per Sujato's comment, this tale is "
            "&lsquo;similar to the previous story&rsquo;: a servant "
            "girl kills her mother with a pestle while trying to rid "
            "her of flies."]),
        ("A word even the tradition itself struggles with", [
            "Sujato's comment flags a specific difficulty: the "
            "opening word &lsquo;yañce&rsquo; is &lsquo;hard to "
            "explain&rsquo;, with the traditional commentary offering "
            "&lsquo;several options, none of which are terribly "
            "convincing&rsquo;. Sujato's own suggestion is that it "
            "might be &lsquo;an old corruption&rsquo; of a phrase used "
            "in the previous poem, &lsquo;na tveva&rsquo; &mdash; an "
            "honest acknowledgment that not every textual puzzle in "
            "this collection has a fully satisfying answer."]),
    ],
    terms=[
        ("seyyo amitto medhāvī",
         "&ldquo;better is an intelligent foe&rdquo; &mdash; this "
         "poem's version of the chapter's closing proverb pair "
         "(shared with Ja 44)."),
        ("bālānukampako",
         "&ldquo;a foolish sympathizer&rdquo; &mdash; the "
         "disqualified alternative, echoing Ja 44's 'inconsiderate "
         "friend'."),
        ("yañce",
         "an opening word Sujato's comment describes as "
         "&ldquo;hard to explain&rdquo;, possibly an old corruption "
         "of &lsquo;na tveva&rsquo; from the previous poem."),
        ("Rohiṇijātaka",
         "the traditional title of this tale, named for the servant "
         "girl at its center."),
        ("Ja 44",
         "the previous poem, sharing both this poem's proverb "
         "structure and its underlying pattern of well-meaning harm."),
    ],
    text_intro=(
        "The text in full: a single verse, closing this chapter's "
        "refrain sequence, with a genuine textual puzzle discussed "
        "above. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja45:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse's opening proverb state?",
         "opts": [
             'That an intelligent foe is better than a foolish sympathizer',
             'That flies are more dangerous than they appear',
             'No proverb is stated',
             'That family is always trustworthy',
         ],
         "correct": 0,
         "expl": "Closing the chapter's refrain sequence with a variant of Ja 44's own proverb."},
        {"q": "What does Rohinī do, per the verse and Sujato's comment?",
         "opts": [
             'She successfully protects her mother',
             'She kills her mother with a pestle while trying to rid her of flies',
             'She abandons her mother',
             'She injures herself instead',
         ],
         "correct": 1,
         "expl": 'A well-meaning act of care causing exactly the death it was meant to prevent.'},
        {"q": "How does Sujato's comment describe this tale's relationship to the previous poem, Ja 44?",
         "opts": [
             'An earlier version later revised into Ja 44',
             'Completely unrelated',
             "'Similar to the previous story' — the same underlying pattern of well-meaning harm",
             'A direct contradiction',
         ],
         "correct": 2,
         "expl": 'Both poems share the pattern of good intentions applied without proportion or judgment.'},
        {"q": "What specific word does Sujato's comment say is 'hard to explain'?",
         "opts": [
             "The word for 'mother'",
             "The word for 'pestle'",
             'No word is flagged as difficult',
             "'Yañce', the opening word, with even the traditional commentary's explanations unconvincing",
         ],
         "correct": 3,
         "expl": 'An honest acknowledgment that not every textual puzzle has a fully satisfying answer.'},
        {"q": "What does Sujato's own comment suggest 'yañce' might be?",
         "opts": [
             "An old corruption of 'na tveva' from the previous poem",
             'A scribal addition with no meaning',
             'The comment offers no suggestion at all',
             'A completely unrelated new word',
         ],
         "correct": 0,
         "expl": 'A tentative, honestly-flagged hypothesis rather than a confident claim.'},
        {"q": "What does the traditional commentary offer for this word's meaning?",
         "opts": [
             'A single, confident, convincing explanation',
             'Several options, none of which Sujato finds terribly convincing',
             'No explanation is offered by the commentary either',
             "A completely different reading than Sujato's",
         ],
         "correct": 1,
         "expl": 'A rare case where the comment openly notes the limits of available scholarship.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Spoiling the Toddy',
             'The Mosquito',
             'About Rohinī (Rohiṇijātaka)',
             'Spoiling the Park',
         ],
         "correct": 2,
         "expl": "The forty-fifth poem overall, and the fifth and final poem of this chapter's refrain sequence."},
        {"q": 'What tool does Rohinī use, per the underlying story?',
         "opts": [
             'Her bare hands',
             'A stick',
             'A knife',
             'A pestle',
         ],
         "correct": 3,
         "expl": 'Meant to swat away flies, with fatal results.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The fifth poem of the Atthakāmavagga, closing the refrain sequence begun at Ja 41',
             'The final poem of the whole chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Five poems remain in this ten-poem chapter after this one.'},
        {"q": 'What does the verse call Rohinī, describing her state after the killing?',
         "opts": [
             'Triumphant',
             "'Wretched', grieving after killing her mother",
             'Indifferent',
             'Proud',
         ],
         "correct": 1,
         "expl": 'The poem does not treat her harshly as a villain, but as someone grieving a tragic accident.'},
    ],
    marginalia=[
        ("A second version of the same tragedy", [
            "flies swatted with a pestle, not an axe —",
            "the same fatal lack of proportion"
        ]),
        ("A word the tradition can't quite explain", [
            "even the commentary offers only guesses —",
            "Sujato names the difficulty honestly"
        ]),
        ("Grief, not villainy", [
            "the verse calls her wretched, not wicked —",
            "an accident, mourned rather than condemned"
        ]),
        ("Closing five poems on one theme", [
            "the last of the chapter's shared refrain —",
            "five different proofs of the same warning"
        ]),
    ],
    further=[
        '<a href="%s/ja45/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-44.html">Ja 44 &mdash; The Mosquito</a> '
        "&mdash; the poem immediately before this one, sharing this "
        "poem's underlying pattern.",
        '<a href="ja-46.html">Ja 46 &mdash; Spoiling the Park</a> '
        "&mdash; the next poem, opening a new, shorter refrain pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 46 — Ārāmadūsaka (Spoiling the Park)
# --------------------------------------------------------------------------- #
page(
    46, "&Amacr;r&amacr;mad&umacr;saka", "Spoiling the Park",
    meta_title="Ja 46 — Spoiling the Park | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 46 — well-meaning monkeys who ruin a whole park by "
        "misunderstanding simple instructions, and a wordplay-rich "
        "verse about two senses of 'good'. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, opening a new two-poem "
                 "refrain pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse built on deliberate wordplay"),
    ],
    why=(
        "This poem opens a new, shorter two-poem refrain pair "
        "(continuing at Ja 47), shifting the chapter's concern from "
        "ignored advice to misunderstood instructions &mdash; and "
        "Sujato's comment unpacks a deliberate play on two different "
        "senses of a single Pali word that the English translation "
        "alone cannot fully capture."),
    guide=[
        ("Good intentions undone by literal-minded misunderstanding", [
            "The verse opens a new refrain: &lsquo;surely not with "
            "one who misunderstands the meaning does good conduct "
            "lead to happiness. The simpleton destroys the good, like "
            "the monkey groundskeeper.&rsquo; Per Sujato's comment, a "
            "lazy groundskeeper asks monkeys in the park to water the "
            "trees in his absence; they set to work with genuine good "
            "cheer, but misconstrue the instructions and pull up each "
            "tree to examine its roots before watering &mdash; ruining "
            "the whole park through good intentions alone."]),
        ("A single word carrying two different senses at once", [
            "Sujato's comment explains that the verse plays on two "
            "meanings of &lsquo;attha&rsquo;: in the opening line it "
            "means &lsquo;meaning, basis&rsquo; (glossed as "
            "&lsquo;reason, cause&rsquo;), while later it means "
            "&lsquo;good, benefit&rsquo; &mdash; the same word doing "
            "double duty, a wordplay the English translation must "
            "render with two different words, losing the original's "
            "single-word pun."]),
    ],
    terms=[
        ("anatthakusalena",
         "&ldquo;one who misunderstands the meaning&rdquo; &mdash; "
         "the flawed figure at the center of this poem's warning."),
        ("attha",
         "a Pali word Sujato's comment identifies as carrying two "
         "distinct senses within this single verse: "
         "&lsquo;meaning/basis&rsquo; and &lsquo;good/benefit&rsquo;."),
        ("kapi ārāmiko",
         "&ldquo;the monkey groundskeeper&rdquo; &mdash; the "
         "well-meaning but literal-minded figures at the center of "
         "the underlying story."),
        ("Ārāmadūsakajātaka",
         "the traditional title of this tale, &lsquo;Spoiling the "
         "Park&rsquo;."),
        ("Ja 47",
         "the next poem in this chapter, sharing this poem's exact "
         "opening and closing formula with a different illustration."),
    ],
    text_intro=(
        "The text in full: a single verse, opening a two-poem "
        "refrain pair built on deliberate wordplay, discussed above. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja46:1.1-1.4"),
    ],
    quiz=[
        {"q": "What do the monkeys do, per Sujato's comment?",
         "opts": [
             'They refuse the task entirely',
             'They misconstrue the watering instructions and pull up each tree to examine its roots, ruining the park',
             'They water the trees perfectly',
             'They abandon the park to predators',
         ],
         "correct": 1,
         "expl": 'Despite setting to work with genuine good cheer.'},
        {"q": "What wordplay does Sujato's comment identify in this verse?",
         "opts": [
             "A pun on the word for 'monkey'",
             'No wordplay is present',
             "The word 'attha' carries two distinct senses within the same verse — 'meaning/basis' and 'good/benefit'",
             "A pun on the groundskeeper's name",
         ],
         "correct": 2,
         "expl": 'A single word doing double duty, which the English translation must render with two different words.'},
        {"q": 'Who asks the monkeys to water the trees?',
         "opts": [
             'A visiting merchant',
             'No one — they act on their own',
             'The king',
             'A lazy groundskeeper, in his own absence',
         ],
         "correct": 3,
         "expl": 'Setting up the well-meaning but disastrous misunderstanding.'},
        {"q": "What is the underlying cause of the park's destruction?",
         "opts": [
             'Good intentions combined with a literal-minded misunderstanding of the instructions',
             'A natural disaster',
             'Deliberate sabotage by a rival groundskeeper',
             'Malicious intent by the monkeys',
         ],
         "correct": 0,
         "expl": 'The monkeys genuinely wanted to help, but misconstrued what helping actually required.'},
        {"q": 'What relationship does this poem have to Ja 47?',
         "opts": [
             'No relationship at all',
             'They share the exact same opening and closing formula, illustrated by a different example',
             'Ja 47 predates this poem',
             'They tell contradictory morals',
         ],
         "correct": 1,
         "expl": 'A new, shorter two-poem refrain pair within this chapter.'},
        {"q": "What does the verse's opening line claim about someone who misunderstands the meaning?",
         "opts": [
             'No claim is made',
             'That their good conduct still leads to happiness regardless',
             'That good conduct does not lead to happiness for such a person',
             'That they cannot act at all',
         ],
         "correct": 2,
         "expl": "Setting up the poem's central warning about action without understanding."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Spoiling the Toddy',
             'About Vedabbha',
             'About Rohinī',
             'Spoiling the Park (Ārāmadūsakajātaka)',
         ],
         "correct": 3,
         "expl": 'The forty-sixth poem overall, and the sixth of the Atthakāmavagga.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The sixth poem of the Atthakāmavagga, following the five-poem refrain sequence of Ja 41-45',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Opening a new, shorter refrain pair within the same chapter.'},
        {"q": "How does this poem's concern differ from the previous five poems' shared refrain?",
         "opts": [
             'It is identical in every respect',
             'It shifts from ignoring good advice to misunderstanding instructions despite good intentions',
             'It concerns a completely unrelated topic',
             'It focuses on royal succession',
         ],
         "correct": 1,
         "expl": 'A related but distinct kind of failure within the same broader chapter theme.'},
        {"q": "What animal is specifically responsible for the park's ruin?",
         "opts": [
             'Deer',
             'Elephants',
             'Monkeys',
             'Birds',
         ],
         "correct": 2,
         "expl": 'Acting as groundskeepers in the absence of the human keeper.'},
    ],
    marginalia=[
        ("Good cheer, disastrous results", [
            "the monkeys set to work happily —",
            "and ruin the whole park by trying too hard"
        ]),
        ("One word, two meanings at once", [
            "'attha' shifting sense within the same line —",
            "a pun the translation can't fully carry over"
        ]),
        ("Understanding as the missing ingredient", [
            "not malice, just misunderstood instructions —",
            "good intentions alone were never enough"
        ]),
        ("A new pair begins", [
            "Ja 46 and 47 share the same frame —",
            "a shorter echo of the chapter's first sequence"
        ]),
    ],
    further=[
        '<a href="%s/ja46/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-45.html">Ja 45 &mdash; About Rohinī</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-47.html">Ja 47 &mdash; Spoiling the Toddy</a> '
        "&mdash; the next poem, completing this refrain pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 47 — Vāruṇidūsaka (Spoiling the Toddy)
# --------------------------------------------------------------------------- #
page(
    47, "V&amacr;ru&#7751;id&umacr;saka", "Spoiling the Toddy",
    meta_title="Ja 47 — Spoiling the Toddy | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 47 — a brewer's apprentice ruining a batch of drink "
        "through misunderstood instructions, completing this "
        "chapter's second refrain pair. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, completing this chapter's "
                 "second refrain pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, part of a two-poem pair"),
    ],
    why=(
        "This poem completes the two-poem refrain pair begun at Ja "
        "46, illustrating the same warning about misunderstood "
        "instructions with an entirely different, everyday setting "
        "&mdash; a brewery instead of a park."),
    guide=[
        ("The same refrain, a human rather than animal example", [
            "The verse repeats its companion poem's opening and "
            "closing formula exactly, changing only the illustration: "
            "&lsquo;the simpleton destroys the good, as Koṇḍañña did "
            "the toddy.&rsquo; Per Sujato's comment, a brewer's "
            "apprentice ruins an entire batch of toddy due to simply "
            "misunderstanding the instructions he was given."]),
        ("Two illustrations, one shared lesson", [
            "Where Ja 46 used monkeys destroying a park through "
            "misapplied enthusiasm, this poem uses a human apprentice "
            "destroying a batch of drink through the same underlying "
            "failure &mdash; showing that this chapter's warning "
            "about misunderstanding is not limited to animal folly, "
            "but applies equally to ordinary human error."]),
    ],
    terms=[
        ("koṇḍañño",
         "the name of the brewer's apprentice in this tale's "
         "underlying story &mdash; unrelated to the elder Koṇḍañña "
         "elsewhere in the canon."),
        ("vāruṇiṁ",
         "&ldquo;toddy&rdquo; &mdash; the fermented drink ruined by "
         "the apprentice's misunderstanding, giving this poem its "
         "traditional title."),
        ("hāpeti atthaṁ dummedho",
         "&ldquo;the simpleton destroys the good&rdquo; &mdash; the "
         "refrain shared word for word with Ja 46."),
        ("Vāruṇidūsakajātaka",
         "the traditional title of this tale, &lsquo;Spoiling the "
         "Toddy&rsquo;."),
        ("Ja 46",
         "the previous poem, sharing this poem's exact opening and "
         "closing formula with a different illustration."),
    ],
    text_intro=(
        "The text in full: a single verse, completing the refrain "
        "pair begun at Ja 46. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja47:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the brewer's apprentice ruin, per this poem?",
         "opts": [
             'A garden',
             'A batch of bread',
             'A batch of toddy (fermented drink)',
             'A shipment of grain',
         ],
         "correct": 2,
         "expl": "Giving this poem its traditional title, 'Spoiling the Toddy'."},
        {"q": "Why does the apprentice ruin the batch, per Sujato's comment?",
         "opts": [
             'A lack of ingredients',
             'Bad weather',
             'Deliberate sabotage',
             'Simply misunderstanding the instructions he was given',
         ],
         "correct": 3,
         "expl": "The same underlying pattern as Ja 46's monkey groundskeepers."},
        {"q": "How does this poem's opening and closing relate to Ja 46's?",
         "opts": [
             'The exact same formula, with only the illustration changed',
             'A loose paraphrase with significant differences',
             'No relationship at all',
             'Completely different wording throughout',
         ],
         "correct": 0,
         "expl": 'Completing a matched two-poem refrain pair.'},
        {"q": "What is the significance of this poem using a human example after Ja 46's animal one?",
         "opts": [
             'No particular significance',
             'It shows the same warning about misunderstanding applies equally to human error, not just animal folly',
             "It contradicts Ja 46's message",
             'It suggests only humans can misunderstand instructions',
         ],
         "correct": 1,
         "expl": "Broadening the lesson's apparent scope through a paired but distinct illustration."},
        {"q": "Is the 'Koṇḍañña' in this tale related to the well-known elder Koṇḍañña elsewhere in the canon?",
         "opts": [
             'They are explicitly identified as brothers',
             'Yes, the same figure',
             'No — an unrelated figure sharing only the name',
             'The comment does not address this',
         ],
         "correct": 2,
         "expl": 'A coincidence of naming, not a narrative connection.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'About Vedabbha',
             'Constellations',
             'Spoiling the Park',
             'Spoiling the Toddy (Vāruṇidūsakajātaka)',
         ],
         "correct": 3,
         "expl": 'The forty-seventh poem overall, and the seventh of the Atthakāmavagga.'},
        {"q": "What profession is involved in this poem's illustration?",
         "opts": [
             "A brewer's apprentice",
             "A ship's captain",
             'A royal minister',
             'A farmer',
         ],
         "correct": 0,
         "expl": "An ordinary trade, contrasting with Ja 46's park setting."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The seventh poem of the Atthakāmavagga, completing the refrain pair begun at Ja 46',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Atthakāmavagga.'},
        {"q": "What common thread connects this poem's illustration to Ja 46's?",
         "opts": [
             'No common thread exists',
             'Both involve royalty',
             'Both involve well-meaning effort undone by misunderstanding, in different settings',
             'Both involve the same specific characters',
         ],
         "correct": 2,
         "expl": 'The same underlying lesson given twice, in animal and human form.'},
        {"q": 'How many poems remain in the Atthakāmavagga after this one?',
         "opts": [
             'Five',
             'One',
             'None',
             'Three (Ja 48, 49, and 50)',
         ],
         "correct": 3,
         "expl": "The chapter's closing stretch, each a standalone poem rather than part of a refrain sequence."},
    ],
    marginalia=[
        ("The same lesson, a different setting", [
            "not a park this time, but a brewery —",
            "the same misunderstanding, the same ruin"
        ]),
        ("A human error, matching an animal one", [
            "the apprentice fares no better than the monkeys —",
            "misunderstanding spares no one"
        ]),
        ("A shared name, no shared story", [
            "Koṇḍañña here is not the famous elder —",
            "just a coincidence of naming"
        ]),
        ("A matched pair, closed out", [
            "Ja 46 and 47, the same frame twice —",
            "three standalone poems still remain in this chapter"
        ]),
    ],
    further=[
        '<a href="%s/ja47/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-46.html">Ja 46 &mdash; Spoiling the Park</a> '
        "&mdash; the poem immediately before this one, sharing this "
        "poem's exact formula.",
        '<a href="ja-48.html">Ja 48 &mdash; About Vedabbha</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 48 — Vedabba (About Vedabbha)
# --------------------------------------------------------------------------- #
page(
    48, "Vedabba", "About Vedabbha",
    meta_title="Ja 48 — About Vedabbha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 48 — a warning against profit by inappropriate means, "
        "where Sujato's comment directly questions whether the "
        "traditional commentary's story actually matches the verse. "
        "From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; a case where the traditional story "
                       "itself is called into question"),
    ],
    why=(
        "This poem offers a rare, direct look at how this collection "
        "was assembled: Sujato's own comment states plainly that the "
        "traditional commentary's elaborate story of bandits, spells, "
        "and a captured brahmin does not actually appear anywhere in "
        "the verse itself, and proposes a simpler, more historically "
        "grounded alternative."),
    guide=[
        ("A warning against profit through improper means", [
            "The verse states its principle directly: &lsquo;who "
            "wishes to profit by inappropriate means is tormented. "
            "The Cetans who killed Vedabbha all fell into "
            "ruin.&rsquo; The consequence named is total: not "
            "partial loss, but ruin for everyone involved."]),
        ("A traditional story the verse itself does not actually tell", [
            "Sujato's comment reports that the traditional "
            "commentary describes a brahmin named Vedabbha, captured "
            "by bandits from Cetī, who pays his ransom using a "
            "wealth-granting spell also called Vedabbha &mdash; only "
            "for the spell to inflame the bandits' greed until they "
            "kill him and then each other. But the comment adds a "
            "striking caveat: &lsquo;despite the commentary, however, "
            "the verse does not mention bandits, spells, or "
            "brahmins.&rsquo;"]),
        ("A simpler, more historically grounded alternative reading", [
            "Sujato's comment proposes instead that "
            "&lsquo;Vedabbha&rsquo; (Sanskrit vaidarbha) is simply a "
            "name for the king of Vidarbha, a country south of Cetī "
            "&mdash; suggesting the verse's original context may have "
            "been a real historical raid by the Cetans resulting in "
            "the death of the king of Vidarbha, a framework that could "
            "convey the same underlying moral without any of the "
            "commentary's elaborate later embellishment."]),
    ],
    terms=[
        ("anupāyena... atthaṁ icchati",
         "&ldquo;wishes to profit by inappropriate means&rdquo; "
         "&mdash; the verse's central warning."),
        ("vedabbaṁ",
         "&ldquo;Vedabbha&rdquo;, Sanskrit vaidarbha &mdash; per "
         "Sujato's comment, likely a name for the king of Vidarbha, "
         "rather than the brahmin of the traditional commentary's "
         "story."),
        ("cetā",
         "&ldquo;the Cetans&rdquo; &mdash; per Sujato's comment, "
         "likely raiders from Cetī, a country neighboring Vidarbha."),
        ("Vedabbajātaka",
         "the traditional title of this tale, &lsquo;About "
         "Vedabbha&rsquo;."),
        ("Vidarbha",
         "a country south of Cetī, per Sujato's comment the likely "
         "true referent of &lsquo;Vedabbha&rsquo;, rather than an "
         "individual brahmin."),
    ],
    text_intro=(
        "The text in full: a single verse, with Sujato's own comment "
        "directly questioning whether the traditional commentary's "
        "story actually matches it, discussed above. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja48:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the verse warn against?',
         "opts": [
             'Traveling too far from home',
             'No specific warning is given',
             'Excessive generosity',
             'Wishing to profit by inappropriate means',
         ],
         "correct": 3,
         "expl": 'Illustrated by the total ruin of the Cetans who killed Vedabbha.'},
        {"q": "What story does the traditional commentary tell about this verse, per Sujato's comment?",
         "opts": [
             "A brahmin named Vedabbha captured by bandits, who ransoms himself with a wealth-granting spell, inflaming the bandits' greed until they kill him and each other",
             "A story about a merchant's voyage",
             'No commentarial story exists',
             "A story about a king's coronation",
         ],
         "correct": 0,
         "expl": "The traditional elaboration Sujato's comment then directly questions."},
        {"q": "What striking observation does Sujato's comment make about this traditional story?",
         "opts": [
             'That it perfectly matches every detail of the verse',
             'That the verse itself does not actually mention bandits, spells, or brahmins',
             'That it is confirmed by multiple independent sources',
             'That it predates the verse itself',
         ],
         "correct": 1,
         "expl": "A rare, direct questioning of whether the traditional commentary's story matches its own verse."},
        {"q": "What alternative reading does Sujato's comment propose for 'Vedabbha'?",
         "opts": [
             'No alternative is proposed',
             'A type of ritual object',
             'A name for the king of Vidarbha, a country south of Cetī',
             'A brand of spell with no historical basis',
         ],
         "correct": 2,
         "expl": 'Suggesting a simpler, more historically grounded original context for the verse.'},
        {"q": "What historical framework does Sujato's comment suggest instead?",
         "opts": [
             'A dispute over agricultural land',
             'No alternative framework is suggested',
             'A purely mythological event with no historical basis',
             'A real raid by the Cetans resulting in the death of the king of Vidarbha',
         ],
         "correct": 3,
         "expl": "A framework that could convey the same underlying moral without the commentary's later embellishment."},
        {"q": 'What fate does the verse say befell the Cetans who killed Vedabbha?',
         "opts": [
             'They all fell into ruin',
             'They were forgiven',
             'The verse does not specify their fate',
             'They prospered afterward',
         ],
         "correct": 0,
         "expl": "A total consequence, matching the verse's opening warning about the torment of improper profit-seeking."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Spoiling the Toddy',
             'About Vedabbha (Vedabbajātaka)',
             'Constellations',
             'The Simpleton',
         ],
         "correct": 1,
         "expl": 'The forty-eighth poem overall, and the eighth of the Atthakāmavagga.'},
        {"q": 'What does this poem illustrate about the relationship between canonical verses and their traditional commentaries generally?',
         "opts": [
             'That verses never require any commentary at all',
             'That they always match perfectly with no discrepancy',
             "That a commentary's elaborate story can sometimes diverge from what the bare verse itself actually says",
             'That commentaries are always more reliable than verses',
         ],
         "correct": 2,
         "expl": 'A rare, explicit case of this general tension being directly named by the translator.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The eighth poem of the Atthakāmavagga, following the two refrain sequences of Ja 41-45 and 46-47',
         ],
         "correct": 3,
         "expl": 'A standalone poem, not part of either preceding refrain sequence.'},
        {"q": 'Does this poem form part of a refrain sequence like several earlier poems in this chapter?',
         "opts": [
             'No — it stands alone, unlike Ja 41-45 and Ja 46-47',
             'It shares a refrain with only one other poem',
             'The question does not apply to this poem',
             'Yes, sharing a refrain with several other poems',
         ],
         "correct": 0,
         "expl": 'Marking a shift to standalone poems for the remainder of this chapter.'},
    ],
    marginalia=[
        ("A story the verse doesn't actually tell", [
            "bandits, spells, a brahmin — all from the commentary —",
            "'the verse does not mention' any of it"
        ]),
        ("A simpler history, proposed instead", [
            "not a magic spell, but a king's own name —",
            "a raid, a death, a moral that still holds"
        ]),
        ("Total ruin, for everyone involved", [
            "not one bandit spared —",
            "'all fell into ruin', the verse says plainly"
        ]),
        ("A translator's honest caveat", [
            "'despite the commentary, however' —",
            "scholarship questioning its own tradition"
        ]),
    ],
    further=[
        '<a href="%s/ja48/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        "<a href=\"ja-47.html\">Ja 47 &mdash; Spoiling the "
        "Toddy</a> &mdash; the poem immediately before this one.",
        '<a href="ja-49.html">Ja 49 &mdash; Constellations</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 49 — Nakkhatta (Constellations)
# --------------------------------------------------------------------------- #
page(
    49, "Nakkhatta", "Constellations",
    meta_title="Ja 49 — Constellations | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 49 — a sharp dismissal of astrological superstition "
        "over practical good, echoed at this site's own DN 4. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short, pointed dismissal of superstition"),
    ],
    why=(
        "This poem's dismissal of astrological timing &mdash; "
        "&lsquo;the good is the constellation of the good; for what "
        "do the stars matter?&rsquo; &mdash; is echoed in structure by "
        "a comparable rhetorical question at this site's own DN 4, "
        "adding this to a small but consistent pattern of skepticism "
        "toward ritual and superstitious practice across this partial "
        "Jātaka selection."),
    guide=[
        ("A fool who lets practical good slip away, waiting on the stars", [
            "The verse delivers its point in two matched halves: "
            "&lsquo;waiting for a constellation, a fool lets the good "
            "pass them by. The good is the constellation of the good; "
            "for what do the stars matter?&rsquo; Per Sujato's "
            "comment, a family reneges on an already-set marriage date "
            "when told it falls under an unlucky constellation, so the "
            "intended bride ends up marrying someone else instead."]),
        ("An echo of the same rhetorical dismissal elsewhere on this site", [
            "Sujato's comment directly compares this poem's closing "
            "question to a comparable line at this site's own DN 4: "
            "&lsquo;what do the hymns matter?&rsquo; &mdash; both "
            "verses use the same rhetorical structure to dismiss a "
            "ritual or traditional practice in favor of a more direct, "
            "practical good."]),
    ],
    terms=[
        ("nakkhattaṁ paṭimānentaṁ",
         "&ldquo;waiting for a constellation&rdquo; &mdash; the "
         "superstitious delay the verse criticizes."),
        ("attho bālaṁ upaccagā",
         "&ldquo;a fool lets the good pass them by&rdquo; &mdash; "
         "the direct cost of that superstitious waiting."),
        ("attho atthassa nakkhattaṁ",
         "&ldquo;the good is the constellation of the good&rdquo; "
         "&mdash; the verse's own redefinition of what actually "
         "determines auspiciousness."),
        ("Nakkhattajātaka",
         "the traditional title of this tale, "
         "&lsquo;Constellations&rsquo;."),
        ("DN 4",
         "the already-completed page on this site with a "
         "comparable rhetorical dismissal &mdash; &lsquo;what do the "
         "hymns matter?&rsquo; &mdash; per Sujato's own comment."),
    ],
    text_intro=(
        "The text in full: a single verse, echoed in structure by a "
        "comparable line already complete on this site's own DN 4. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja49:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the verse criticize?',
         "opts": [
             'Waiting for an auspicious constellation before acting, letting practical good pass by',
             'Traveling too far',
             'No specific criticism is given',
             'Excessive generosity',
         ],
         "correct": 0,
         "expl": 'A fool lets the good pass them by while waiting for the stars to align.'},
        {"q": "What does the verse propose as the real 'constellation of the good'?",
         "opts": [
             'A specific favorable star pattern',
             'The good itself — practical benefit, not astrological timing',
             'The advice of an elder',
             'No alternative is proposed',
         ],
         "correct": 1,
         "expl": "'For what do the stars matter?' — a direct rhetorical dismissal."},
        {"q": "What happens in the commentarial story, per Sujato's comment?",
         "opts": [
             'No specific story is given',
             'A wedding proceeds exactly as planned',
             'A family reneges on an already-set marriage date over an unlucky constellation, and the bride marries someone else',
             'A king cancels a coronation',
         ],
         "correct": 2,
         "expl": 'A concrete illustration of practical opportunity lost to superstition.'},
        {"q": "What already-completed page on this site does Sujato's comment compare this verse's closing question to?",
         "opts": [
             'MN 83',
             'No comparison is made',
             'AN 8.29',
             "DN 4, with its comparable line 'what do the hymns matter?'",
         ],
         "correct": 3,
         "expl": 'Both use the same rhetorical structure to dismiss ritual practice in favor of practical good.'},
        {"q": 'What broader pattern does this poem add to, per this reading guide?',
         "opts": [
             'A small but consistent pattern of skepticism toward ritual and superstitious practice across this selection',
             'A pattern unrelated to any other poem',
             'A pattern specifically about marriage customs',
             'A pattern of praising ritual practice',
         ],
         "correct": 0,
         "expl": 'Connecting this poem to a wider thread across this partial Jātaka selection.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'About Vedabbha',
             'Constellations (Nakkhattajātaka)',
             'The Simpleton',
             'About Losaka',
         ],
         "correct": 1,
         "expl": 'The forty-ninth poem overall, and the ninth of the Atthakāmavagga.'},
        {"q": 'What structure does the verse use in its second half?',
         "opts": [
             'A list of examples',
             'A narrative continuation',
             'A rhetorical question dismissing the value of the thing just named',
             'A direct command',
         ],
         "correct": 2,
         "expl": "'For what do the stars matter?' — mirrored by DN 4's own rhetorical dismissal."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The ninth poem of the Atthakāmavagga, following Ja 41 through Ja 48',
         ],
         "correct": 3,
         "expl": 'The second-to-last poem of this ten-poem chapter.'},
        {"q": 'What specifically caused the marriage plans to fall through, per the commentarial story?',
         "opts": [
             'Being told the set date fell under an unlucky constellation',
             'A change of heart by the groom',
             'A family dispute unrelated to astrology',
             'A disagreement over dowry',
         ],
         "correct": 0,
         "expl": 'Superstition directly costing a real, practical opportunity.'},
        {"q": 'What tone does this verse take toward astrological practice?',
         "opts": [
             'Respectful and affirming',
             'Sharp and dismissive',
             'Neutral and purely descriptive',
             'Ambiguous with no clear position',
         ],
         "correct": 1,
         "expl": 'A pointed rhetorical question rather than a measured discussion.'},
    ],
    marginalia=[
        ("A wedding lost to bad timing, literally", [
            "the date called unlucky, so it's canceled —",
            "and she marries someone else instead"
        ]),
        ("The only constellation that matters", [
            "not the stars, but the good itself —",
            "a redefinition delivered as a question"
        ]),
        ("The same dismissal, echoed elsewhere", [
            "'what do the hymns matter?' at DN 4 —",
            "the same rhetorical move, a different ritual"
        ]),
        ("Skepticism, running quietly through this selection", [
            "not the first poem to question ritual timing —",
            "part of a small, consistent thread"
        ]),
    ],
    further=[
        '<a href="%s/ja49/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../digha-nikaya/dn-04.html">DN 4 &mdash; With '
        "Soṇadaṇḍa</a> &mdash; the already-completed page with a "
        "comparable rhetorical dismissal.",
        '<a href="ja-48.html">Ja 48 &mdash; About Vedabbha</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-50.html">Ja 50 &mdash; The Simpleton</a> '
        "&mdash; the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 50 — Dummedha (The Simpleton)
# --------------------------------------------------------------------------- #
page(
    50, "Dummedha", "The Simpleton",
    meta_title="Ja 50 — The Simpleton | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 50, closing the Atthakāmavagga and the first fifty "
        "poems of the Ekakanipāta — a king's calculated bluff about "
        "sacrificing evildoers, which works precisely because no one "
        "dares test it. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Five (Atthakāmavagga) &middot; Poem 10 of 10 (closing the chapter, and the first fifty poems)",
    glance=[
        ("Setting", "A newly crowned king, addressing his kingdom"),
        ("Speaker", "The Bodhisatta, as a new king"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse built on a clever bluff"),
    ],
    why=(
        "This poem closes both the Atthakāmavagga and the first fifty "
        "poems of the entire Ekakanipāta selection with an unusually "
        "clever twist: a threat that works precisely because it is "
        "never actually carried out, since simply announcing it "
        "eliminated the problem it was meant to solve."),
    guide=[
        ("A threat announced, and never needing to be fulfilled", [
            "The verse gives the king's own announcement: &lsquo;a "
            "sacrifice of simpletons by the thousand was pledged by "
            "me. Now I shall sacrifice many an unrighteous "
            "man.&rsquo; Per Sujato's comment, the Bodhisatta, though "
            "personally an unbeliever, had regularly offered flowers "
            "to a deity while still crown prince; upon ascending the "
            "throne, he announces he must repay the deity by "
            "sacrificing a thousand evildoers."]),
        ("A calculated bluff that achieves its goal without violence", [
            "Sujato's comment delivers the poem's real point: "
            "&lsquo;the bluff had the intended effect, for from that "
            "day not a single evildoer was to be found.&rsquo; The "
            "threat of sacrifice was never carried out, because "
            "announcing it was itself sufficient to eliminate the "
            "wrongdoing it targeted &mdash; a solution achieved "
            "entirely through calculated announcement rather than any "
            "actual violence."]),
        ("A technical term shared with a poem outside this selection", [
            "Sujato's comment notes that &lsquo;upayācita&rsquo; "
            "(&lsquo;pledged&rsquo;), meaning a promise made to "
            "propitiate a deity, also occurs at Ja 544, which lies "
            "outside this site's own 82-poem selection; this reading "
            "guide notes the cross-reference without a linked page."]),
        ("Closing the Atthakāmavagga, and the first fifty poems of the collection", [
            "This poem closes the Atthakāmavagga, the fifth of eight "
            "chapters this site's selection draws from within the "
            "Ekakanipāta &mdash; and, per the source text's own "
            "structural marker, &lsquo;paṭhamo paṇṇāsako&rsquo;, the "
            "first fifty poems of the entire Ekakanipāta as well. The "
            "source text's own untranslated summary verse (uddāna) "
            "immediately follows, naming all ten poems of this "
            "chapter in sequence &mdash; not presented here as quoted "
            "text, since it carries no separate translation, but "
            "noted for completeness, as at the close of the previous "
            "four chapters."]),
    ],
    terms=[
        ("dummedhānaṁ sahassena",
         "&ldquo;a sacrifice of simpletons by the thousand&rdquo; "
         "&mdash; the king's own opening pledge, giving this poem its "
         "traditional title."),
        ("upayācita",
         "&ldquo;pledged&rdquo; &mdash; per Sujato's comment, a "
         "promise made to propitiate a deity, also found at Ja 544 "
         "(outside this site's own selection)."),
        ("adhammiko jano",
         "&ldquo;unrighteous man&rdquo; &mdash; the actual, "
         "unspoken target of the king's announced threat."),
        ("Dummedhajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Simpleton&rsquo;."),
        ("paṭhamo paṇṇāsako",
         "&ldquo;the first fifty&rdquo; &mdash; the source text's "
         "own structural marker, following this poem, dividing the "
         "Ekakanipāta into blocks of fifty poems."),
    ],
    text_intro=(
        "The text in full: a single verse. The chapter's own "
        "untranslated closing summary verse (uddāna), which follows "
        "immediately in the source text, is not quoted here since it "
        "carries no English translation, but its content &mdash; the "
        "ten poem titles of this chapter in sequence &mdash; matches "
        "this reading guide's own further reading list below. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja50:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the newly crowned king announce?',
         "opts": [
             'A festival of celebration',
             'That he must sacrifice a thousand evildoers to repay a deity',
             'A tax reduction',
             'A new law code',
         ],
         "correct": 1,
         "expl": 'Fulfilling a promise made while he was still crown prince, offering flowers to the deity.'},
        {"q": "What does Sujato's comment reveal about the actual outcome of this threat?",
         "opts": [
             'No outcome is described',
             'The king carried out the sacrifice as announced',
             'The bluff had the intended effect — from that day not a single evildoer was to be found',
             'The kingdom rebelled against the king',
         ],
         "correct": 2,
         "expl": 'The threat achieved its goal entirely through announcement, without any actual violence.'},
        {"q": "What was the king's real, unspoken goal?",
         "opts": [
             'To honor the deity for its own sake',
             'To expand his territory',
             'To increase his own wealth',
             'To eliminate wrongdoing in his kingdom',
         ],
         "correct": 3,
         "expl": 'Achieved by framing evildoers as the sacrificial targets, making everyone afraid to be classified as one.'},
        {"q": "What does Sujato's comment say about the term 'upayācita'?",
         "opts": [
             "It means a promise made to propitiate a deity, also found at Ja 544, outside this site's own selection",
             'It refers to a specific ritual object',
             'It is a modern coinage',
             'It has no meaning outside this poem',
         ],
         "correct": 0,
         "expl": "Noted for completeness without a linked page, since Ja 544 falls outside this site's 82-poem selection."},
        {"q": 'What two things does this poem close, per this reading guide?',
         "opts": [
             'Nothing significant',
             "The Atthakāmavagga, and the first fifty poems of the entire Ekakanipāta ('paṭhamo paṇṇāsako')",
             "Only a single poem's own internal structure",
             'The entire Jātaka collection',
         ],
         "correct": 1,
         "expl": 'A double closing marker in the source text itself.'},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'It is presented as spoken by the deity',
             'Yes, quoted in full',
             'No — it carries no separate English translation, so it is only noted for completeness',
             'It does not exist for this chapter',
         ],
         "correct": 2,
         "expl": 'Consistent with the same practice at the close of the previous four chapters.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'About Vedabbha',
             'Spoiling the Toddy',
             'Constellations',
             'The Simpleton (Dummedhajātaka)',
         ],
         "correct": 3,
         "expl": 'The fiftieth poem overall, and the tenth and final poem of the Atthakāmavagga.'},
        {"q": "What personal detail does Sujato's comment give about the Bodhisatta's own beliefs?",
         "opts": [
             'He was, personally, an unbeliever, despite regularly offering flowers to the deity',
             'He converted to belief only after becoming king',
             'The comment does not address this',
             'He was a devout believer in the deity',
         ],
         "correct": 0,
         "expl": "Making his eventual 'sacrifice' announcement a calculated strategy rather than genuine religious devotion."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of the Atthakāmavagga',
             'The tenth and final poem of the Atthakāmavagga, closing this chapter and the first fifty poems overall',
             'It stands outside any chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse and the 'first fifty' marker following immediately after."},
        {"q": "What makes this poem's solution to wrongdoing distinctive?",
         "opts": [
             'It fails to achieve any effect',
             'It relies entirely on physical punishment',
             'It achieves its goal purely through calculated announcement, never requiring actual violence',
             'It relies on a lengthy legal process',
         ],
         "correct": 2,
         "expl": "One of this collection's cleverer illustrations of psychological rather than physical solutions to a social problem."},
    ],
    marginalia=[
        ("A threat that never has to be kept", [
            "announce the sacrifice, and the evildoers vanish —",
            "the bluff does all the actual work"
        ]),
        ("An unbeliever's calculated offering", [
            "flowers given without real faith —",
            "used later as leverage for a clever threat"
        ]),
        ("Fifty poems, closed together", [
            "the Atthakāmavagga's own summary follows —",
            "and the source text's own 'first fifty' marker with it"
        ]),
        ("Wrongdoing solved by fear alone", [
            "not a single evildoer found after that day —",
            "the announcement was the whole solution"
        ]),
    ],
    further=[
        '<a href="%s/ja50/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-49.html">Ja 49 &mdash; Constellations</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 51 — Mahāsīlava (The Great Virtuous One)
# --------------------------------------------------------------------------- #
page(
    51, "Mah&amacr;s&imacr;lava", "The Great Virtuous One",
    meta_title="Ja 51 — The Great Virtuous One | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 51, opening the Āsīsavagga — a deposed king's "
        "unbroken hope through torture, the first of five matched "
        "pairs structuring this whole chapter. From Ru-Yi Meditation "
        "Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "The king himself, reflecting after his ordeal"),
        ("Form", "One four-line stanza, the first half of a matched "
                 "pair with Ja 52"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse opening a matched-pair "
                       "structure"),
    ],
    why=(
        "This poem opens the Āsīsavagga (&lsquo;Hope Chapter&rsquo;), "
        "the first of five back-to-back matched pairs that structure "
        "this entire chapter &mdash; each pair sharing nearly "
        "identical wording, differing in one key term or image. This "
        "poem's own theme, hope surviving brutal reversal, sets the "
        "tone the whole chapter will develop."),
    guide=[
        ("Hope vindicated after brutal reversal", [
            "The verse states its conclusion plainly: &lsquo;a man "
            "should have hope, the astute should not be disillusioned. "
            "Now I truly see myself &mdash; as I wished, so I "
            "became.&rsquo; Per Sujato's comment, a good king, "
            "deposed by a violent foe, is subjected to brutal torture "
            "&mdash; yet neither slips from his own virtue nor loses "
            "hope, persevering until he eventually regains the "
            "crown."]),
        ("The first of five matched pairs structuring this chapter", [
            "This poem forms a matched pair with the next, Ja 52 (A "
            "Short Tale of Janaka): both share the identical second "
            "half &mdash; &lsquo;now I truly see myself...&rsquo; "
            "&mdash; differing only in their opening verb (hope "
            "versus effort) and their closing image. This same "
            "pattern &mdash; near-identical twin verses completing a "
            "single idea from two angles &mdash; recurs four more "
            "times across this chapter (Ja 53/54, 55/56, 57/58, "
            "59/60)."]),
    ],
    terms=[
        ("āsīsetha",
         "&ldquo;should have hope&rdquo; &mdash; the verse's opening "
         "instruction, giving this whole chapter its name "
         "(Āsīsavagga)."),
        ("na nibbindeyya paṇḍito",
         "&ldquo;the astute should not be disillusioned&rdquo; "
         "&mdash; shared word for word with the next poem, Ja 52."),
        ("yathā icchiṁ tathā ahū",
         "&ldquo;as I wished, so I became&rdquo; &mdash; the king's "
         "own vindication after enduring torture and reclaiming his "
         "throne."),
        ("Mahāsīlavajātaka",
         "the traditional title of this tale, opening the "
         "Āsīsavagga."),
        ("Ja 52",
         "the next poem, forming this chapter's first matched pair "
         "with this one."),
    ],
    text_intro=(
        "The text in full: a single verse, opening the first of five "
        "matched pairs structuring this chapter. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja51:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What structural pattern does this poem open, unique to this chapter?',
         "opts": [
             'A pattern shared with no other poem in the chapter',
             'No particular structure is present',
             'A single long narrative spanning all ten poems',
             'Five matched pairs of poems, each pair sharing nearly identical wording differing in one key term',
         ],
         "correct": 2,
         "expl": 'This same pattern recurs at Ja 53/54, 55/56, 57/58, and 59/60.'},
        {"q": "What happens to the king in this poem's underlying story, per Sujato's comment?",
         "opts": [
             'He willingly abdicates',
             'He is exiled peacefully',
             'He is never challenged',
             'He is deposed by a violent foe and subjected to brutal torture, yet never loses hope',
         ],
         "correct": 3,
         "expl": 'Persevering until he eventually regains the crown.'},
        {"q": "What does the verse's closing line state?",
         "opts": [
             "'Now I truly see myself — as I wished, so I became'",
             'A description of his torture',
             'A request for revenge',
             'A statement of regret',
         ],
         "correct": 0,
         "expl": 'Vindication after enduring the ordeal with unbroken hope.'},
        {"q": 'What does this poem share word for word with Ja 52?',
         "opts": [
             'Nothing at all',
             "The line 'the astute should not be disillusioned', and the opening structure of the poem's second half",
             'The entire verse identically',
             'Only the title',
         ],
         "correct": 1,
         "expl": "Differing in the opening verb and closing image, per this chapter's matched-pair structure."},
        {"q": "What does the verse's opening word, 'āsīsetha' (should have hope), give to this chapter?",
         "opts": [
             'No connection to the chapter title',
             'Nothing in particular',
             "Its own name — the Āsīsavagga, 'Hope Chapter'",
             "A different chapter's name",
         ],
         "correct": 2,
         "expl": "This poem's opening word directly names the whole chapter."},
        {"q": 'What chapter does this poem open?',
         "opts": [
             'The Itthivagga',
             'It does not open a chapter',
             'The Atthakāmavagga',
             'The Āsīsavagga',
         ],
         "correct": 3,
         "expl": "This collection's sixth ten-poem chapter."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Great Virtuous One (Mahāsīlavajātaka)',
             'The Full Cups',
             'The What-fruit',
             'A Short Tale of Janaka',
         ],
         "correct": 0,
         "expl": 'The fifty-first poem overall, and the first of the Āsīsavagga.'},
        {"q": 'What quality does the king in the underlying story maintain throughout his ordeal?',
         "opts": [
             'Anger and vengefulness',
             'His own virtue and hope',
             'Despair',
             'Indifference',
         ],
         "correct": 1,
         "expl": 'Neither slipping from virtue nor losing hope despite brutal torture.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of the Āsīsavagga',
             'The final poem of the Atthakāmavagga',
             'The first poem of the sixth chapter (Āsīsavagga), following the completed Atthakāmavagga',
             'It stands outside any chapter',
         ],
         "correct": 2,
         "expl": "Opening this collection's sixth ten-poem chapter, and its first matched pair."},
        {"q": 'How many matched pairs, including this one, structure the whole Āsīsavagga?',
         "opts": [
             'Ten',
             'One',
             'Two',
             'Five',
         ],
         "correct": 3,
         "expl": 'Ja 51/52, 53/54, 55/56, 57/58, and 59/60.'},
    ],
    marginalia=[
        ("Torture endured, the crown regained", [
            "hope kept through brutal reversal —",
            "'as I wished, so I became'"
        ]),
        ("A chapter named by its own first word", [
            "'āsīsetha' — should have hope —",
            "the Āsīsavagga takes its name from here"
        ]),
        ("The first of five twin poems", [
            "nearly identical wording, one key term changed —",
            "a structure repeated four more times in this chapter"
        ]),
        ("Virtue that survived the worst test", [
            "neither slipping nor despairing —",
            "the throne regained through persistence alone"
        ]),
    ],
    further=[
        '<a href="%s/ja51/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-50.html">Ja 50 &mdash; The Simpleton</a> '
        "&mdash; the closing poem of the previous chapter.",
        '<a href="ja-52.html">Ja 52 &mdash; A Short Tale of '
        "Janaka</a> &mdash; the next poem, completing this chapter's "
        "first matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 52 — Cūḷajanaka (A Short Tale of Janaka)
# --------------------------------------------------------------------------- #
page(
    52, "C&umacr;&#7789;ajanaka", "A Short Tale of Janaka",
    meta_title="Ja 52 — A Short Tale of Janaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 52 — a shipwrecked king's unremitting effort, "
        "completing this chapter's first matched pair, and "
        "cross-linked to this site's own Thag 1.88 and MN 83. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "King Janaka himself, reflecting after his "
                    "ordeal"),
        ("Form", "One four-line stanza, completing this chapter's "
                 "first matched pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, part of a matched pair"),
    ],
    why=(
        "This poem completes Ja 51's matched pair, shifting from hope "
        "to effort as the operative virtue, and connects directly to "
        "this site's own already-completed Thag 1.88 and MN 83 "
        "&mdash; a rare case of a single Jātaka verse threading "
        "through two entirely different collections already on this "
        "site."),
    guide=[
        ("Effort rewarded, after apparent disaster", [
            "The verse pairs with Ja 51 almost exactly: &lsquo;a man "
            "should make an effort, the astute should not be "
            "disillusioned. Now I truly see myself, lifted from the "
            "water to the shore.&rsquo; Per Sujato's comment, this "
            "brief telling relates how Janaka of Videha regained his "
            "kingdom through unremitting effort; the fuller version of "
            "the same story is told at Ja 539 (Mahājanakajātaka), "
            "outside this site's own 82-poem selection."]),
        ("A famous royal house, and a connection to this site's own MN 83", [
            "Sujato's comment identifies the Janakas as &lsquo;the "
            "famed kingly house of Videha&rsquo;, and notes that at "
            "this site's own MN 83, a different King Janaka is "
            "framed as the source of that kingdom's decline &mdash; "
            "the same royal name recurring across different "
            "generations and different moral roles within the wider "
            "tradition."]),
        ("A specific line shared with an already-completed Theragātha poem", [
            "Sujato's comment directly compares this poem's central "
            "lines to this site's own already-completed Thag 1.88 "
            "(Ajjuna) &mdash; a case of the same imagery of being "
            "rescued or lifted to safety appearing across two "
            "entirely separate collections within this site's own "
            "selections."]),
    ],
    terms=[
        ("vāyametha",
         "&ldquo;should make an effort&rdquo; &mdash; this poem's "
         "own variation on Ja 51's opening word, shifting the "
         "emphasis from hope to active effort."),
        ("udakā thalamubbhataṁ",
         "&ldquo;lifted from the water to the shore&rdquo; &mdash; "
         "the poem's own image of rescue after apparent disaster."),
        ("Cūḷajanakajātaka",
         "the traditional title of this tale, &lsquo;A Short Tale of "
         "Janaka&rsquo; &mdash; distinguished from the fuller "
         "Mahājanakajātaka at Ja 539, outside this site's own "
         "selection."),
        ("Thag 1.88",
         "Ajjuna &mdash; the already-completed page on this site "
         "Sujato's own comment compares to this poem's central "
         "lines."),
        ("MN 83",
         "&ldquo;About King Maghadeva&rdquo; &mdash; the "
         "already-completed page on this site where a different King "
         "Janaka is framed as the source of Videha's decline."),
    ],
    text_intro=(
        "The text in full: a single verse, completing the matched "
        "pair begun at Ja 51. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja52:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does King Janaka regain his kingdom, per Sujato's comment?",
         "opts": [
             'Through a marriage alliance',
             'The comment does not specify',
             'Through inherited right alone',
             'Through unremitting effort',
         ],
         "correct": 3,
         "expl": "Shifting this poem's emphasis from Ja 51's hope to active, sustained effort."},
        {"q": "Where is the fuller version of this same story told, per Sujato's comment?",
         "opts": [
             "Ja 539 (Mahājanakajātaka), outside this site's own 82-poem selection",
             'Within this same poem in full',
             "In a different chapter of this site's selection",
             'Nowhere else',
         ],
         "correct": 0,
         "expl": 'This poem gives only the shorter version.'},
        {"q": "What already-completed page on this site does Sujato's comment compare this poem's central lines to?",
         "opts": [
             'AN 8.29',
             'Thag 1.88 (Ajjuna)',
             'SN 9.8',
             'No comparison is made',
         ],
         "correct": 1,
         "expl": 'The same imagery of being rescued or lifted to safety, appearing in two separate collections on this site.'},
        {"q": "What already-completed page connects to a different King Janaka framed as a kingdom's decline?",
         "opts": [
             'No such connection exists',
             'DN 4',
             'MN 83',
             'SN 11.6',
         ],
         "correct": 2,
         "expl": 'The same royal name recurring across different generations and moral roles in the wider tradition.'},
        {"q": "What does the verse's closing image describe?",
         "opts": [
             'A coronation ceremony',
             'A journey by land',
             'A battle won',
             'Being lifted from the water to the shore',
         ],
         "correct": 3,
         "expl": "Per Sujato's comment, the fuller Ja 539 relates how he survived the sinking of his ship."},
        {"q": "What word does this poem substitute for Ja 51's 'hope'?",
         "opts": [
             'Effort (vāyametha)',
             'Wealth',
             'Courage',
             'Patience',
         ],
         "correct": 0,
         "expl": "Completing the matched pair's shift in emphasis."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Great Virtuous One',
             'A Short Tale of Janaka (Cūḷajanakajātaka)',
             'The Full Cups',
             'Prince Five-Weapons',
         ],
         "correct": 1,
         "expl": 'The fifty-second poem overall, and the second of the Āsīsavagga, completing its first matched pair.'},
        {"q": "What royal house are the Janakas, per Sujato's comment?",
         "opts": [
             'The comment does not identify them',
             'An obscure minor family',
             'The famed kingly house of Videha',
             'A merchant family later ennobled',
         ],
         "correct": 2,
         "expl": 'Connecting this brief tale to a well-known royal lineage within the wider tradition.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The second poem of the Āsīsavagga, completing the matched pair begun at Ja 51',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": "What is distinctive about this poem's cross-links compared to most other poems in this selection?",
         "opts": [
             'It connects to two different already-completed collections on this site (Theragātha and Majjhima Nikāya) simultaneously',
             'It only connects to texts outside this site entirely',
             'It connects only to another Jātaka poem',
             'It has no cross-links at all',
         ],
         "correct": 0,
         "expl": 'A relatively rare case of one verse threading through multiple already-completed collections.'},
    ],
    marginalia=[
        ("From shipwreck to shore", [
            "effort in place of hope, this time —",
            "the same vindication, a different ordeal"
        ]),
        ("A royal name, two different roles", [
            "here, effort regains a kingdom —",
            "at MN 83, a different Janaka causes its decline"
        ]),
        ("The same image, two collections", [
            "Thag 1.88 shares this poem's central lines —",
            "one image, threading through separate texts"
        ]),
        ("A brief telling of a longer story", [
            "the fuller Mahājanakajātaka lies beyond this selection —",
            "this poem gives only the short version"
        ]),
    ],
    further=[
        '<a href="%s/ja52/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../theragatha/thag-1.88.html">Thag 1.88 &mdash; '
        "Ajjuna</a> &mdash; the already-completed page sharing this "
        "poem's central imagery.",
        '<a href="../majjhima-nikaya/mn-083.html">MN 83 &mdash; '
        "About King Maghadeva</a> &mdash; connected to a different "
        "King Janaka within the wider Videha royal line.",
        '<a href="ja-51.html">Ja 51 &mdash; The Great Virtuous '
        "One</a> &mdash; the poem immediately before this one, "
        "opening this chapter's first matched pair.",
        '<a href="ja-53.html">Ja 53 &mdash; The Full Cups</a> '
        "&mdash; the next poem, opening a new matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 53 — Puṇṇapāti (The Full Cups)
# --------------------------------------------------------------------------- #
page(
    53, "Pu&#7751;&#7751;ap&amacr;ti", "The Full Cups",
    meta_title="Ja 53 — The Full Cups | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 53 — a would-be robbery victim who deduces the plot "
        "simply by watching who avoids their own drink. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "A drinking gathering, rogues among the guests"),
        ("Speaker", "The rich man targeted by the rogues"),
        ("Form", "One four-line stanza, opening a new matched pair "
                 "with Ja 54"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of quiet, careful deduction"),
    ],
    why=(
        "This poem opens a new matched pair with Ja 54, both sharing "
        "an identical deductive refrain &mdash; &lsquo;for this "
        "reason I know&rsquo; &mdash; each illustrating a different "
        "case of danger detected through simple, careful observation "
        "rather than any special insight."),
    guide=[
        ("A plot detected by watching what others don't drink", [
            "The verse gives the rich man's own quiet observation: "
            "&lsquo;the cups stay just as full, while the ignorant "
            "talk goes on. For this reason I know this is not an "
            "excellent beer.&rsquo; Per Sujato's comment, rogues "
            "attempt to spike a rich man's drink with a drug so they "
            "can rob him &mdash; but he notices they do not touch "
            "their own drinks, and deduces the danger from that alone."]),
        ("The first of a new refrain pair", [
            "This poem's closing structure &mdash; &lsquo;for this "
            "reason I know... this is not...&rsquo; &mdash; recurs "
            "exactly at the next poem, Ja 54, applied to a completely "
            "different situation and danger, continuing this "
            "chapter's pattern of matched pairs."]),
    ],
    terms=[
        ("tatheva puṇṇā pātiyo",
         "&ldquo;the cups stay just as full&rdquo; &mdash; the "
         "observed detail that gives away the plot."),
        ("ākāraṇena jānāmi",
         "&ldquo;for this reason I know&rdquo; &mdash; the "
         "deductive refrain shared word for word with the next poem, "
         "Ja 54."),
        ("bhaddikā surā",
         "&ldquo;excellent beer&rdquo; &mdash; what the drink is "
         "not, once the rich man's deduction is complete."),
        ("Puṇṇapātijātaka",
         "the traditional title of this tale, &lsquo;The Full "
         "Cups&rsquo;."),
        ("bhesajja",
         "&ldquo;drug&rdquo; &mdash; per Sujato's comment, what the "
         "rogues attempt to spike the rich man's drink with."),
    ],
    text_intro=(
        "The text in full: a single verse, opening a new matched "
        "pair with Ja 54. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja53:1.1-1.4"),
    ],
    quiz=[
        {"q": "What do the rogues attempt, per Sujato's comment?",
         "opts": [
             "To spike a rich man's drink with a drug so they can rob him",
             'To poison the whole gathering',
             'To challenge him to a wager',
             'To steal directly without deception',
         ],
         "correct": 0,
         "expl": 'A plan the rich man detects before it can succeed.'},
        {"q": 'What specific detail gives the plot away?',
         "opts": [
             'The rogues speaking too loudly',
             "The rogues' own cups staying just as full — they don't drink their own",
             'A strange smell in the drink',
             'A warning from another guest',
         ],
         "correct": 1,
         "expl": 'A simple, careful observation rather than any special insight.'},
        {"q": 'What refrain does this poem share with Ja 54?',
         "opts": [
             'Only the title format',
             'No shared refrain',
             "'For this reason I know...', applied to a different situation",
             'An identical full verse',
         ],
         "correct": 2,
         "expl": "Continuing this chapter's pattern of matched pairs."},
        {"q": 'What does the rich man conclude about the drink?',
         "opts": [
             'That it is completely safe',
             'No conclusion is stated',
             'That it is unusually good',
             'That it is not an excellent beer',
         ],
         "correct": 3,
         "expl": 'A polite understatement for having detected the plot.'},
        {"q": "What quality does this poem's deduction rely on?",
         "opts": [
             "Simple, careful observation of others' behavior",
             'A warning from a spirit',
             'Torture-extracted confession',
             'Magical foresight',
         ],
         "correct": 0,
         "expl": 'Noticing what the rogues themselves avoid doing.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'A Short Tale of Janaka',
             'The Full Cups (Puṇṇapātijātaka)',
             'The What-fruit',
             'Prince Five-Weapons',
         ],
         "correct": 1,
         "expl": 'The fifty-third poem overall, and the third of the Āsīsavagga.'},
        {"q": "What setting does this poem's story take place in?",
         "opts": [
             'A forest',
             'A battlefield',
             'A drinking gathering',
             'A royal court',
         ],
         "correct": 2,
         "expl": 'Among guests that include the plotting rogues.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The third poem of the Āsīsavagga, opening a new matched pair after Ja 51/52',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": 'What general theme connects this poem to Ja 54?',
         "opts": [
             'Danger detected through careful, ordinary observation rather than special insight',
             'A theme about royal succession',
             'A theme about seasonal change',
             'No connection',
         ],
         "correct": 0,
         "expl": 'Both poems are variations on the same deductive refrain.'},
        {"q": "What was the rich man's advantage over the rogues in this encounter?",
         "opts": [
             'Physical strength',
             'Attentiveness — noticing a small but telling behavioral detail',
             'Wealth alone',
             'A weapon',
         ],
         "correct": 1,
         "expl": 'The entire poem turns on this single act of careful noticing.'},
    ],
    marginalia=[
        ("A plot given away by inaction", [
            "the rogues' own cups, untouched —",
            "the tell that exposes everything"
        ]),
        ("Deduction, not luck", [
            "no warning needed, no confession forced —",
            "just watching what others don't do"
        ]),
        ("A refrain that will repeat once more", [
            "'for this reason I know' returns next poem —",
            "the same careful logic, a new danger"
        ]),
        ("Politeness masking a real threat detected", [
            "'not an excellent beer' — understated —",
            "for what was actually a plot to rob him"
        ]),
    ],
    further=[
        '<a href="%s/ja53/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-52.html">Ja 52 &mdash; A Short Tale of '
        "Janaka</a> &mdash; the poem immediately before this one.",
        '<a href="ja-54.html">Ja 54 &mdash; The What-fruit</a> '
        "&mdash; the next poem, completing this matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 54 — Kiṁphala (The What-fruit)
# --------------------------------------------------------------------------- #
page(
    54, "Ki&#7749;phala", "The What-fruit",
    meta_title="Ja 54 — The What-fruit | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 54 — a caravan leader's deduction that a "
        "mango-looking tree must be poisonous, completing this "
        "chapter's second matched pair. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "A tree beside a well-traveled road, laden with "
                    "fruit"),
        ("Speaker", "A wise caravan leader"),
        ("Form", "One four-line stanza, completing this chapter's "
                 "second matched pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of practical deduction"),
    ],
    why=(
        "This poem completes Ja 53's matched pair with a different "
        "kind of everyday deduction: a caravan leader reasons that "
        "fruit growing untouched on an accessible tree, right beside "
        "a well-traveled road, cannot possibly be as sweet as it "
        "looks &mdash; because if it were, someone would already have "
        "picked it clean."),
    guide=[
        ("A conclusion reached from what's absent, not what's present", [
            "The verse gives the caravan leader's own reasoning: "
            "&lsquo;this tree is not hard to climb, nor is it far "
            "from the village. For this reason I know this tree is "
            "not sweet-fruited.&rsquo; Per Sujato's comment, the tree "
            "is laden with fruit that looks like mango, but the wise "
            "caravan leader deduces it must be the poisonous "
            "&lsquo;what-fruit&rsquo; (kiṁphala) precisely because it "
            "is so easy to reach and so untouched."]),
        ("The same deductive refrain, a different domain entirely", [
            "Where Ja 53's deduction concerned a social plot detected "
            "through human behavior, this poem's deduction is purely "
            "practical and botanical &mdash; showing this chapter's "
            "shared refrain applies just as well to reading nature "
            "carefully as to reading people."]),
    ],
    terms=[
        ("durāruho",
         "&ldquo;hard to climb&rdquo; &mdash; what the tree is "
         "notably not, contributing to the caravan leader's suspicion."),
        ("ākāraṇena jānāmi",
         "&ldquo;for this reason I know&rdquo; &mdash; the "
         "deductive refrain shared word for word with the previous "
         "poem, Ja 53."),
        ("kiṁphala",
         "the &ldquo;what-fruit&rdquo;, a poisonous fruit "
         "resembling mango, giving this poem its traditional title."),
        ("Kiṁphalajātaka",
         "the traditional title of this tale, &lsquo;The "
         "What-fruit&rsquo;."),
        ("duma",
         "&ldquo;tree&rdquo;, per Sujato's comment specially "
         "indicating a flowering tree in this context."),
    ],
    text_intro=(
        "The text in full: a single verse, completing the matched "
        "pair begun at Ja 53. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja54:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What two facts about the tree does the caravan leader observe?',
         "opts": [
             'That it is diseased and withered',
             'That it is easy to climb and not far from the village',
             'That it is guarded',
             'That it has no fruit at all',
         ],
         "correct": 1,
         "expl": 'Precisely these accessible qualities lead to his suspicion.'},
        {"q": "What does the caravan leader conclude about the tree's fruit?",
         "opts": [
             'That the tree is sacred',
             'That it must be especially delicious',
             'That it cannot be sweet-fruited, since it would already have been picked clean if it were',
             'That it is entirely inedible for any reason',
         ],
         "correct": 2,
         "expl": "Reasoning from the absence of prior harvesting, not from the fruit's appearance."},
        {"q": "What is the fruit actually identified as, per Sujato's comment?",
         "opts": [
             'An unknown, harmless fruit',
             'The comment does not identify it',
             'A genuine mango',
             "The poisonous 'what-fruit' (kiṁphala), resembling mango",
         ],
         "correct": 3,
         "expl": 'Giving this poem its traditional title.'},
        {"q": 'What refrain does this poem share with Ja 53?',
         "opts": [
             "'For this reason I know...', applied to a completely different situation",
             'An identical full verse',
             'Only the closing word',
             'No shared refrain',
         ],
         "correct": 0,
         "expl": "Completing this chapter's second matched pair."},
        {"q": "How does this poem's kind of deduction differ from Ja 53's?",
         "opts": [
             'They are identical in every way',
             "Ja 53's concerns reading human behavior; this poem's concerns reading nature and circumstance",
             "This poem's deduction concerns human behavior instead",
             'Neither poem involves any deduction',
         ],
         "correct": 1,
         "expl": "Showing this chapter's shared refrain applies across very different domains of careful reasoning."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Mass of Gold',
             'The Full Cups',
             'The What-fruit (Kiṁphalajātaka)',
             'Prince Five-Weapons',
         ],
         "correct": 2,
         "expl": 'The fifty-fourth poem overall, and the fourth of the Āsīsavagga, completing its second matched pair.'},
        {"q": "What role does the speaker hold in this poem's underlying story?",
         "opts": [
             'A king',
             'A monk',
             'A farmer',
             'A caravan leader',
         ],
         "correct": 3,
         "expl": 'Applying practical, traveled experience to avoid a hidden danger.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The fourth poem of the Āsīsavagga, completing the matched pair begun at Ja 53',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": "What does Sujato's comment note about the word 'duma' in this context?",
         "opts": [
             'It is a completely generic word for any plant',
             'It specially indicates a flowering tree',
             'It refers only to fruit, not trees',
             'No note is given about this word',
         ],
         "correct": 1,
         "expl": "A small philological detail refining the verse's botanical picture."},
        {"q": "What underlying principle connects this poem's reasoning to Ja 53's?",
         "opts": [
             'A principle about seasonal timing',
             'No underlying principle connects them',
             'Reading the absence of an expected behavior (drinking, harvesting) as evidence of hidden danger',
             'A principle about royal authority',
         ],
         "correct": 2,
         "expl": "Both poems' central figures reason from what is conspicuously not happening."},
    ],
    marginalia=[
        ("Untouched, and that's the giveaway", [
            "easy to reach, right by the road —",
            "yet no one has picked it clean"
        ]),
        ("A caravan leader's practiced eye", [
            "not magic, just experience —",
            "reading the tree's own circumstances"
        ]),
        ("The same logic, applied to nature", [
            "where Ja 53 read people, this poem reads a tree —",
            "the refrain works in either domain"
        ]),
        ("Poison disguised as plenty", [
            "fruit that looks exactly like mango —",
            "deduced as dangerous before it's ever tasted"
        ]),
    ],
    further=[
        '<a href="%s/ja54/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-53.html">Ja 53 &mdash; The Full Cups</a> '
        "&mdash; the poem immediately before this one, opening this "
        "matched pair.",
        '<a href="ja-55.html">Ja 55 &mdash; Prince Five-Weapons</a> '
        "&mdash; the next poem, opening a new matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 55 — Pañcāvudha (Prince Five-Weapons)
# --------------------------------------------------------------------------- #
page(
    55, "Pa&ntilde;c&amacr;vudha", "Prince Five-Weapons",
    meta_title="Ja 55 — Prince Five-Weapons | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 55 — one of this tradition's most famous tales, a "
        "prince fighting a monster with five weapons and getting "
        "stuck fast, reinterpreted as a warning about violence "
        "itself. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One stanza (six lines), opening a new matched pair "
                 "with Ja 56"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one of this collection's most famous "
                       "underlying stories"),
    ],
    why=(
        "This is one of the most celebrated tales associated with the "
        "Jātaka tradition &mdash; a prince named for a prophecy who "
        "fights a monster with five weapons, only to become stuck "
        "fast to its coat with every attack &mdash; but Sujato's own "
        "comment reveals the verse attached to it reads the story "
        "against itself, turning a tale of martial courage into a "
        "warning about violence."),
    guide=[
        ("A prophecy fulfilled, and a hero stuck fast", [
            "Per Sujato's comment, a prince named &lsquo;Five-"
            "Weapons&rsquo; after a birth prophecy fulfills it when, "
            "returning from his studies, he encounters a ferocious "
            "native spirit in a forest and fights it with five "
            "weapons in turn &mdash; but each attack only sticks him "
            "tighter to the monster's own shaggy coat. The monster, "
            "recognizing his courage even in defeat, ultimately lets "
            "him go."]),
        ("A verse that reads the story's own central image against itself", [
            "The canonical verse itself makes no direct mention of "
            "the monster or the weapons: &lsquo;he whose heart is not "
            "stuck, a man of intrepid mind, develops skilful qualities "
            "for the sake of sanctuary from the yoke. Gradually he "
            "would attain the ending of all fetters.&rsquo; Sujato's "
            "comment explains the connection: getting "
            "&lsquo;stuck&rsquo; or &lsquo;bound&rsquo; to an "
            "adversary can be read as a metaphor for violence itself "
            "&mdash; one who lives by the sword becomes bound to the "
            "kamma of killing, becoming the same as those he fights. "
            "The verse is linked to the story precisely through the "
            "contrasting image of a mind that is not bound at all."]),
        ("The first of this chapter's final three matched pairs", [
            "This poem opens a matched pair with Ja 56 (The Mass of "
            "Gold), sharing every line except one key term &mdash; "
            "the two poems &lsquo;almost identical&rsquo;, per "
            "Sujato's comment on the following poem."]),
    ],
    terms=[
        ("alīnena cittena",
         "&ldquo;heart that is not stuck&rdquo; &mdash; the verse's "
         "own reframing of the underlying story's central image of "
         "the prince's weapons sticking to the monster."),
        ("yogakkhemassa pattiyā",
         "&ldquo;for the sake of sanctuary from the yoke&rdquo; "
         "&mdash; the true, spiritual goal the verse redirects the "
         "story's martial imagery toward."),
        ("allīna",
         "&ldquo;stuck, bound&rdquo; &mdash; per Sujato's comment, "
         "read as a metaphor for the kamma of violence, binding "
         "attacker to victim."),
        ("Pañcāvudhajātaka",
         "the traditional title of this tale, &lsquo;Prince "
         "Five-Weapons&rsquo;."),
        ("Ja 56",
         "the next poem, forming a near-identical matched pair with "
         "this one, differing chiefly in one key term."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, opening a new "
        "matched pair with Ja 56. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja55:1.1-1.6"),
    ],
    quiz=[
        {"q": "What happens to Prince Five-Weapons when he fights the forest spirit, per Sujato's comment?",
         "opts": [
             'The comment gives no details of the fight',
             'He defeats it immediately with his first weapon',
             "Each attack only sticks him tighter to the monster's own shaggy coat",
             'He flees without engaging',
         ],
         "correct": 2,
         "expl": "One of the tradition's most famous images, later inspiring the monster's own choice to release him."},
        {"q": 'Does the canonical verse itself directly mention the monster or the weapons?',
         "opts": [
             'It mentions the weapons but not the monster',
             'It mentions the monster but not the weapons',
             'Yes, in vivid detail',
             "No — it speaks only of a heart 'not stuck' and developing skilful qualities",
         ],
         "correct": 3,
         "expl": 'The connection to the story comes entirely through a reinterpreted central image.'},
        {"q": "How does Sujato's comment explain the connection between the verse and the story?",
         "opts": [
             "Being 'stuck' to an adversary is read as a metaphor for violence — one who lives by the sword becomes bound to the kamma of killing",
             'The verse simply retells the fight scene',
             'The connection is purely coincidental wordplay with no deeper meaning',
             'There is no real connection',
         ],
         "correct": 0,
         "expl": 'The verse contrasts this with a mind that is not bound at all.'},
        {"q": 'Why does the monster ultimately release the prince, per the comment?',
         "opts": [
             'It is defeated by force',
             'It recognizes his courage even in defeat',
             'He offers it a bribe',
             'It is bound by a prior agreement',
         ],
         "correct": 1,
         "expl": "A resolution achieved through the monster's own recognition, not through force."},
        {"q": "What does this poem's structure share with Ja 56?",
         "opts": [
             'A completely different theme',
             'No relationship at all',
             'Nearly identical wording throughout, differing in one key term',
             'Only the same number of lines',
         ],
         "correct": 2,
         "expl": "Per Sujato's comment on Ja 56, the two verses are 'almost identical'."},
        {"q": "What is the true goal the verse redirects toward, away from the story's literal combat?",
         "opts": [
             'Wealth',
             'Physical strength',
             'Royal power',
             'Sanctuary from the yoke — spiritual liberation',
         ],
         "correct": 3,
         "expl": "'Gradually he would attain the ending of all fetters.'"},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Prince Five-Weapons (Pañcāvudhajātaka)',
             'The Mass of Gold',
             'The Lord of Langurs',
             'The What-fruit',
         ],
         "correct": 0,
         "expl": 'The fifty-fifth poem overall, and the fifth of the Āsīsavagga, opening its third matched pair.'},
        {"q": 'How many lines make up this verse?',
         "opts": [
             'Four lines',
             'Six lines',
             'Two lines',
             'Eight lines',
         ],
         "correct": 1,
         "expl": 'Slightly longer than the four-line form most common in this chapter.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fifth poem of the Āsīsavagga, opening a new matched pair after Ja 51-54',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": "Why does the prince's name commemorate a prophecy, per Sujato's comment?",
         "opts": [
             'He chose the name himself as an adult',
             'The name refers only to his royal lineage',
             'It has no connection to any prophecy',
             "He was named 'Five-Weapons' at birth after a prophecy that his own later encounter with the forest spirit fulfilled",
         ],
         "correct": 3,
         "expl": 'The story frames his entire adventure as the fulfillment of that early prediction.'},
    ],
    marginalia=[
        ("Stuck fast, weapon after weapon", [
            "each attack only binds him tighter —",
            "one of this tradition's most famous images"
        ]),
        ("A verse that reads against its own story", [
            "no monster named directly here —",
            "'stuck' reinterpreted as the kamma of violence"
        ]),
        ("Courage recognized, even in defeat", [
            "the monster releases him, moved by his spirit —",
            "not force, but recognition, resolves it"
        ]),
        ("A near-perfect twin poem follows", [
            "Ja 56 shares this poem's structure almost entirely —",
            "one key term changes everything"
        ]),
    ],
    further=[
        '<a href="%s/ja55/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-54.html">Ja 54 &mdash; The What-fruit</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-56.html">Ja 56 &mdash; The Mass of Gold</a> '
        "&mdash; the next poem, completing this near-identical "
        "matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 56 — Kañcanakkhandha (The Mass of Gold)
# --------------------------------------------------------------------------- #
page(
    56, "Ka&ntilde;canakkhandha", "The Mass of Gold",
    meta_title="Ja 56 — The Mass of Gold | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 56 — a nearly identical twin to the previous poem, "
        "where a single wordplay-rich term does the whole work of "
        "distinguishing the two. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One stanza (six lines), nearly identical to Ja 55"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; nearly identical to Ja 55, hinging on "
                       "one deliberately ambiguous word"),
    ],
    why=(
        "This poem is, per Sujato's own comment, &lsquo;almost "
        "identical&rsquo; to the previous poem, differing only in "
        "its key term &mdash; a term Sujato's comment shows carries a "
        "deliberate double meaning connecting a story about "
        "smelting gold to the verse's own spiritual sense of a "
        "&lsquo;cheerful&rsquo; heart."),
    guide=[
        ("Nearly the same verse, one term changed", [
            "The verse repeats Ja 55's structure almost exactly: "
            "&lsquo;he whose heart is well-forged, a man of cheerful "
            "mind, develops skilful qualities for the sake of "
            "sanctuary from the yoke. Gradually he would attain the "
            "ending of all fetters.&rsquo; Per Sujato's comment, the "
            "underlying story concerns a man who discovers a large "
            "lump of gold, but must break it into four pieces to make "
            "it useful."]),
        ("A single term carrying two meanings at once", [
            "Sujato's comment explains that the key term "
            "&lsquo;pahaṭṭha&rsquo; normally means "
            "&lsquo;cheerful&rsquo;, but the traditional commentary "
            "connects it instead with gold that has been "
            "&lsquo;forged&rsquo; until luminous and radiant &mdash; "
            "two etymologically related but distinct senses, both "
            "meant to be heard together: a heart made bright and "
            "cheerful, like gold made bright through smelting."]),
        ("A twin poem, distinguished by exactly one word", [
            "Where Ja 55 used &lsquo;alīna&rsquo; (not stuck) to "
            "reframe a story about a monster's sticky coat, this poem "
            "uses &lsquo;pahaṭṭha&rsquo; (forged, cheerful) to "
            "reframe a story about smelting gold &mdash; the same "
            "underlying spiritual teaching, delivered twice, each "
            "time anchored to a completely different narrative through "
            "a single well-chosen pun."]),
    ],
    terms=[
        ("pahaṭṭhena cittena",
         "&ldquo;heart that is well-forged&rdquo; (or "
         "&ldquo;cheerful&rdquo;) &mdash; the verse's own double "
         "meaning, per Sujato's comment connecting gold-smelting to "
         "spiritual brightness."),
        ("pahaṭṭha",
         "a term Sujato's comment identifies as carrying two related "
         "senses at once: &ldquo;cheerful&rdquo; and, per the "
         "traditional commentary, &ldquo;forged (of gold) until "
         "luminous&rdquo;."),
        ("Kañcanakkhandha",
         "&ldquo;mass of gold&rdquo; &mdash; the large lump "
         "discovered in the underlying story, giving this poem its "
         "traditional title."),
        ("Kañcanakkhandhajātaka",
         "the traditional title of this tale, &lsquo;The Mass of "
         "Gold&rsquo;."),
        ("Ja 55",
         "the previous poem, sharing this poem's structure almost "
         "entirely, differing chiefly in this one key term."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, nearly identical "
        "to Ja 55, discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja56:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does Sujato's own comment say about this poem's relationship to Ja 55?",
         "opts": [
             'This poem predates Ja 55',
             'They contradict each other directly',
             'They are entirely unrelated',
             "'The verse is almost identical with the previous, only differing in the key term'",
         ],
         "correct": 3,
         "expl": 'One of the closest textual pairs in this whole collection.'},
        {"q": "What does the underlying story concern, per Sujato's comment?",
         "opts": [
             'A man who discovers a large lump of gold, which must be broken into four pieces to be useful',
             'A shipwreck',
             'A royal coronation',
             'A battle with a monster',
         ],
         "correct": 0,
         "expl": "A completely different narrative from Ja 55's monster-fighting prince."},
        {"q": "What two senses does the key term 'pahaṭṭha' carry at once, per Sujato's comment?",
         "opts": [
             'Only a single, unambiguous sense',
             "'Cheerful' and, per the traditional commentary, 'forged (of gold) until luminous'",
             "'Angry' and 'sad'",
             'No dual meaning is identified',
         ],
         "correct": 1,
         "expl": 'A heart made bright and cheerful, like gold made bright through smelting.'},
        {"q": 'What single word primarily distinguishes this poem from Ja 55?',
         "opts": [
             'Only the closing line differs',
             'The title alone differs',
             "'Alīna' (not stuck) in Ja 55 versus 'pahaṭṭha' (forged/cheerful) here",
             'The two poems use entirely different vocabularies throughout',
         ],
         "correct": 2,
         "expl": 'Each key term anchors the shared verse structure to a different underlying story.'},
        {"q": "What does this poem's underlying story require to make the gold useful?",
         "opts": [
             'Selling it immediately',
             'Burying it for safekeeping',
             'Melting it into coins',
             'Breaking it into four pieces',
         ],
         "correct": 3,
         "expl": 'A practical detail from the commentarial story.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Mass of Gold (Kañcanakkhandhajātaka)',
             'The Lord of Langurs',
             'Three Qualities',
             'Prince Five-Weapons',
         ],
         "correct": 0,
         "expl": 'The fifty-sixth poem overall, and the sixth of the Āsīsavagga, completing its third matched pair.'},
        {"q": 'What spiritual goal does this poem, like Ja 55, direct its imagery toward?',
         "opts": [
             'Material wealth',
             'Sanctuary from the yoke and the ending of all fetters',
             'Royal power',
             'Physical strength',
         ],
         "correct": 1,
         "expl": 'The shared closing lines of both poems in this matched pair.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The sixth poem of the Āsīsavagga, completing the matched pair begun at Ja 55',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": 'How many lines make up this verse?',
         "opts": [
             'Two lines',
             'Eight lines',
             'Four lines',
             'Six lines',
         ],
         "correct": 3,
         "expl": "Matching Ja 55's own six-line form exactly."},
        {"q": "What technique does this pair of poems (Ja 55/56) illustrate about this chapter's structure?",
         "opts": [
             'That a nearly identical verse can be anchored to entirely different stories through a single well-chosen pun on one key term',
             'That every poem in the chapter has six lines',
             'That this chapter contains no wordplay',
             'That all poems in the chapter are completely unrelated',
         ],
         "correct": 0,
         "expl": "One of the most tightly matched examples of this chapter's five-pair structure."},
    ],
    marginalia=[
        ("Almost the same poem, told twice", [
            "Sujato's own comment says so plainly —",
            "one term does all the distinguishing work"
        ]),
        ("A word meaning two things at once", [
            "'pahaṭṭha' — cheerful, and gold made bright —",
            "smelting and spirit, joined in a single term"
        ]),
        ("Gold that must be broken to be useful", [
            "a lump too large as it stands —",
            "divided into four before it can serve"
        ]),
        ("The same ending, twice over", [
            "sanctuary from the yoke, fetters ended —",
            "two stories, one shared spiritual destination"
        ]),
    ],
    further=[
        '<a href="%s/ja56/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-55.html">Ja 55 &mdash; Prince Five-Weapons</a> '
        "&mdash; the poem immediately before this one, nearly "
        "identical in structure.",
        '<a href="ja-57.html">Ja 57 &mdash; The Lord of Langurs</a> '
        "&mdash; the next poem, opening a new matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 57 — Vānarinda (The Lord of Langurs)
# --------------------------------------------------------------------------- #
page(
    57, "V&amacr;narinda", "The Lord of Langurs",
    meta_title="Ja 57 — The Lord of Langurs | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 57 — a monkey king who outwits a crocodile's trick, "
        "with a closing pun the crocodile's own body language "
        "confirms one reading of. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A river, a crocodile posing as a rock"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, opening a new matched pair "
                 "with Ja 58"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse with a resolved double "
                       "meaning"),
    ],
    why=(
        "This poem's underlying story is a well-known trickster tale "
        "&mdash; a crocodile disguised as a rock, trying to catch a "
        "monkey king &mdash; but its closing line carries a genuine "
        "double meaning that Sujato's comment resolves by pointing "
        "directly to the crocodile's own physical behavior in the "
        "story."),
    guide=[
        ("Four qualities that let the monkey king escape", [
            "The verse names its subject's virtues directly: "
            "&lsquo;whoever possesses these four qualities like you, "
            "lord of langurs &mdash; truth, principle, steadfastness, "
            "and generosity &mdash; escapes the visible foe.&rsquo; "
            "Per Sujato's comment, a crocodile's pregnant wife craves "
            "the heart of the monkey king; her husband tries to "
            "satisfy her by pretending to be a rock in the river, but "
            "the monkey sees through the disguise."]),
        ("A double meaning the story itself resolves", [
            "Sujato's comment identifies a deliberate ambiguity in "
            "the closing word &lsquo;diṭṭha&rsquo;: the traditional "
            "commentary reads it as &lsquo;foe&rsquo; (giving "
            "&lsquo;defeats the foe&rsquo;), but its more common sense "
            "is simply &lsquo;seen&rsquo;. The comment resolves this "
            "in favor of the more literal reading by pointing to the "
            "crocodile's own action in the story: he shuts his eyes "
            "and opens his mouth to catch the langur &mdash; making "
            "&lsquo;escapes the one seen [with eyes shut]&rsquo; the "
            "more pointed, story-supported reading."]),
        ("A story from a recognized cycle of tales, and named leaders", [
            "Sujato's comment situates this tale within &lsquo;a "
            "cycle of dohaḷa stories&rsquo; (concerning pregnancy "
            "cravings) in the Jātakas, and identifies the "
            "&lsquo;vānara&rsquo; as a legendary race of aggressive, "
            "human-like monkeys, whose leaders (such as Sugrīva or "
            "Hanuman in the wider tradition) carry the same title, "
            "&lsquo;lord of langurs&rsquo;, given here."]),
    ],
    terms=[
        ("saccaṁ dhammo dhiti cāgo",
         "&ldquo;truth, principle, steadfastness, and "
         "generosity&rdquo; &mdash; the four qualities the verse "
         "credits for the monkey king's escape."),
        ("dohaḷa",
         "&ldquo;pregnancy craving&rdquo; &mdash; per Sujato's "
         "comment, the trigger for this story, part of a recognized "
         "cycle of such tales within the Jātakas."),
        ("diṭṭha",
         "a deliberately ambiguous closing term, per Sujato's "
         "comment meaning either &ldquo;foe&rdquo; (per the "
         "traditional commentary) or, more literally, "
         "&ldquo;seen&rdquo; &mdash; resolved by the crocodile's own "
         "eyes-shut, mouth-open posture in the story."),
        ("vānarinda",
         "&ldquo;lord of langurs&rdquo;, per Sujato's comment a "
         "traditional title for legendary monkey-king leaders such as "
         "Sugrīva or Hanuman."),
        ("Vānarindajātaka",
         "the traditional title of this tale, &lsquo;The Lord of "
         "Langurs&rsquo;."),
    ],
    text_intro=(
        "The text in full: a single verse, opening a new matched "
        "pair with Ja 58, discussed above. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja57:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the crocodile's wife crave, per Sujato's comment?",
         "opts": [
             'The heart of the monkey king',
             'A rare fruit',
             'The comment does not specify a craving',
             'Gold from the riverbed',
         ],
         "correct": 0,
         "expl": "Setting up her husband's attempted trick."},
        {"q": 'How does the crocodile try to catch the monkey king?',
         "opts": [
             'By chasing him directly',
             'By pretending to be a rock in the river',
             'By luring him with food',
             'By asking him directly to cross',
         ],
         "correct": 1,
         "expl": 'A disguise the monkey king ultimately sees through.'},
        {"q": "What four qualities does the verse credit for the monkey king's escape?",
         "opts": [
             'No specific qualities are named',
             'Strength, speed, cunning, and luck',
             'Truth, principle, steadfastness, and generosity',
             'Wealth, status, beauty, and charm',
         ],
         "correct": 2,
         "expl": "Named directly in the verse's opening lines."},
        {"q": "What deliberate double meaning does Sujato's comment identify in the closing word 'diṭṭha'?",
         "opts": [
             "It only ever means 'crocodile'",
             'It is untranslatable',
             'No ambiguity exists',
             "It can mean either 'foe' (per the traditional commentary) or, more literally, 'seen'",
         ],
         "correct": 3,
         "expl": "Resolved by pointing to a specific detail in the crocodile's own physical behavior."},
        {"q": "What physical detail does Sujato's comment use to resolve this ambiguity?",
         "opts": [
             'The crocodile shuts his eyes and opens his mouth to catch the langur',
             "The river's current",
             'No specific detail is cited',
             "The monkey's own actions",
         ],
         "correct": 0,
         "expl": "Supporting the more literal reading of 'diṭṭha' as 'seen [with eyes shut]'."},
        {"q": "What recognized story category does Sujato's comment place this tale within?",
         "opts": [
             'A unique, unprecedented story type',
             "A cycle of 'dohaḷa' (pregnancy craving) stories within the Jātakas",
             'A category of purely historical accounts',
             'No category is identified',
         ],
         "correct": 1,
         "expl": 'Connecting this specific tale to a broader recognized pattern in the tradition.'},
        {"q": "Who are legendary examples of 'lord of langurs' leaders, per Sujato's comment?",
         "opts": [
             'The comment names no examples',
             'Historical kings with no legendary status',
             'Sugrīva and Hanuman',
             'Figures unrelated to any wider tradition',
         ],
         "correct": 2,
         "expl": "Situating this poem's title within a recognized legendary tradition of monkey leaders."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Three Qualities',
             'The Drummer',
             'The Mass of Gold',
             'The Lord of Langurs (Vānarindajātaka)',
         ],
         "correct": 3,
         "expl": 'The fifty-seventh poem overall, and the seventh of the Āsīsavagga, opening its fourth matched pair.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The seventh poem of the Āsīsavagga, opening a new matched pair after Ja 51-56',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": 'What relationship does this poem have to Ja 58?',
         "opts": [
             'No relationship at all',
             'Opening a matched pair, sharing closely related structure and phrasing',
             'A direct contradiction',
             'An unrelated, much later composition',
         ],
         "correct": 1,
         "expl": "Continuing this chapter's pattern of matched pairs."},
    ],
    marginalia=[
        ("A rock that wasn't a rock", [
            "the crocodile's disguise, nearly successful —",
            "seen through before the trap could close"
        ]),
        ("Four qualities, one narrow escape", [
            "truth, principle, steadfastness, generosity —",
            "the verse names exactly what saved him"
        ]),
        ("A pun resolved by the crocodile's own posture", [
            "eyes shut, mouth open — caught in the act —",
            "the literal reading wins out"
        ]),
        ("Named leaders from a wider legend", [
            "Sugrīva, Hanuman — the same title given here —",
            "this monkey king joins a recognized lineage"
        ]),
    ],
    further=[
        '<a href="%s/ja57/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-56.html">Ja 56 &mdash; The Mass of Gold</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-58.html">Ja 58 &mdash; Three Qualities</a> '
        "&mdash; the next poem, completing this matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 58 — Tayodhamma (Three Qualities)
# --------------------------------------------------------------------------- #
page(
    58, "Tayodhamma", "Three Qualities",
    meta_title="Ja 58 — Three Qualities | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 58 — the same monkey-and-crocodile escape retold with "
        "three qualities instead of four, completing this chapter's "
        "fourth matched pair. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza, completing this chapter's "
                 "fourth matched pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse, part of a matched pair"),
    ],
    why=(
        "This poem completes Ja 57's matched pair by counting a "
        "different, shorter list of qualities &mdash; three instead "
        "of four &mdash; for what appears to be the same underlying "
        "escape, and Sujato's comment unpacks a piece of grammatical "
        "wordplay building the new list's second term."),
    guide=[
        ("The same escape, a shorter list of qualities", [
            "The verse closely mirrors Ja 57's structure: &lsquo;"
            "whoever possesses these three qualities like you, lord "
            "of langurs &mdash; adroitness, heroism, wisdom &mdash; "
            "escapes the visible foe.&rsquo; Where the previous poem "
            "named four qualities (truth, principle, steadfastness, "
            "generosity), this one condenses the list to three, "
            "closing on the identical final line."]),
        ("A term built by analogy with another", [
            "Sujato's comment explains that &lsquo;dakkhiyaṁ&rsquo; "
            "(adroitness) is an abstract noun formed from "
            "&lsquo;dakkha&rsquo;, constructed &lsquo;by analogy "
            "with sūriyaṁ&rsquo;, which here means &lsquo;heroism&rsquo; "
            "&mdash; comparable to the more familiar term "
            "&lsquo;vīriya&rsquo; in the same sense. A small piece of "
            "grammatical craftsmanship sits behind this poem's "
            "otherwise simple list."]),
        ("Two related lists, closing this chapter's fourth pair", [
            "Together, Ja 57 and Ja 58 offer two different but "
            "overlapping accountings of what saved the same monkey "
            "king &mdash; four qualities in one telling, three in "
            "the other, both converging on the identical closing "
            "claim that these qualities let their possessor "
            "&lsquo;escape the visible foe.&rsquo;"]),
    ],
    terms=[
        ("dakkhiyaṁ",
         "&ldquo;adroitness&rdquo; &mdash; per Sujato's comment, an "
         "abstract noun formed from &lsquo;dakkha&rsquo; by analogy "
         "with &lsquo;sūriyaṁ&rsquo;."),
        ("sūriyaṁ",
         "&ldquo;heroism&rdquo; in this context, per Sujato's "
         "comment comparable to the more familiar term "
         "&lsquo;vīriya&rsquo;."),
        ("diṭṭhaṁ so ativattati",
         "&ldquo;escapes the visible foe&rdquo; &mdash; the closing "
         "line shared word for word with Ja 57."),
        ("Tayodhammajātaka",
         "the traditional title of this tale, &lsquo;Three "
         "Qualities&rsquo;."),
        ("Ja 57",
         "the previous poem, sharing this poem's structure and "
         "closing line, differing chiefly in the number and content "
         "of the qualities named."),
    ],
    text_intro=(
        "The text in full: a single verse, completing the matched "
        "pair begun at Ja 57. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja58:1.1-1.4"),
    ],
    quiz=[
        {"q": "How many qualities does this poem name, compared to Ja 57's four?",
         "opts": [
             'Five',
             'Three',
             'Two',
             'The same four qualities',
         ],
         "correct": 1,
         "expl": 'Adroitness, heroism, and wisdom, closing on the identical final line as Ja 57.'},
        {"q": "What does Sujato's comment say about the formation of 'dakkhiyaṁ' (adroitness)?",
         "opts": [
             'It is a proper name',
             'It is a completely unrelated loanword',
             "It is an abstract noun formed from 'dakkha' by analogy with 'sūriyaṁ'",
             'It has no clear grammatical formation',
         ],
         "correct": 2,
         "expl": "A small piece of grammatical craftsmanship behind this poem's otherwise simple list."},
        {"q": "What does 'sūriyaṁ' mean in this specific context, per the comment?",
         "opts": [
             "'Wealth'",
             'The comment gives no gloss',
             "'Sun' in its literal sense",
             "'Heroism', comparable to the more familiar term 'vīriya'",
         ],
         "correct": 3,
         "expl": 'One of the three qualities this poem credits for the escape.'},
        {"q": 'What closing line does this poem share word for word with Ja 57?',
         "opts": [
             "'Escapes the visible foe'",
             'A different closing line entirely',
             "Only the poem's title matches",
             'No shared closing line',
         ],
         "correct": 0,
         "expl": 'Both poems converge on the identical final claim despite naming different numbers of qualities.'},
        {"q": 'What relationship do Ja 57 and Ja 58 have to the same underlying escape story?',
         "opts": [
             'They tell completely unrelated stories',
             'They offer two different but overlapping accountings of what saved the same monkey king',
             'Ja 58 contradicts Ja 57 entirely',
             'Only one of the two poems concerns the monkey king',
         ],
         "correct": 1,
         "expl": 'Four qualities in one telling, three in the other, both closing identically.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Horn-Blower',
             'The Lord of Langurs',
             'Three Qualities (Tayodhammajātaka)',
             'The Drummer',
         ],
         "correct": 2,
         "expl": 'The fifty-eighth poem overall, and the eighth of the Āsīsavagga, completing its fourth matched pair.'},
        {"q": 'What three qualities does this poem name?',
         "opts": [
             'Wealth, status, and cunning',
             'Patience, silence, and speed',
             'Truth, principle, and generosity',
             'Adroitness, heroism, and wisdom',
         ],
         "correct": 3,
         "expl": "A condensed version of Ja 57's four-quality list."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The eighth poem of the Āsīsavagga, completing the matched pair begun at Ja 57',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Āsīsavagga.'},
        {"q": 'How many matched pairs remain in this chapter after Ja 57/58?',
         "opts": [
             'None — this is the final pair',
             'One more (Ja 59/60)',
             'Two more',
             'Three more',
         ],
         "correct": 1,
         "expl": 'The fifth and final matched pair of this ten-poem chapter.'},
        {"q": 'What technique does this poem, alongside Ja 57, illustrate?',
         "opts": [
             'That wordplay is absent from this chapter',
             'That this chapter avoids any repeated structure',
             'That the same story can be honored with slightly different, overlapping lists of virtues while still closing on an identical claim',
             'That all poems in this chapter must have exactly four lines',
         ],
         "correct": 2,
         "expl": "A variant form of this chapter's broader pattern of matched pairs."},
    ],
    marginalia=[
        ("Three qualities instead of four", [
            "adroitness, heroism, wisdom this time —",
            "a shorter list, the same escape"
        ]),
        ("A word built by analogy", [
            "'dakkhiyaṁ' shaped after 'sūriyaṁ' —",
            "small grammatical craft behind a simple list"
        ]),
        ("Two tellings, one shared ending", [
            "four qualities here, three there —",
            "'escapes the visible foe', unchanged either way"
        ]),
        ("The fourth pair, now complete", [
            "Ja 57 and 58, closely matched —",
            "one more pair remains in this chapter"
        ]),
    ],
    further=[
        '<a href="%s/ja58/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-57.html">Ja 57 &mdash; The Lord of Langurs</a> '
        "&mdash; the poem immediately before this one, opening this "
        "matched pair.",
        '<a href="ja-59.html">Ja 59 &mdash; The Drummer</a> '
        "&mdash; the next poem, opening this chapter's final matched "
        "pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 59 — Bherivādaka (The Drummer)
# --------------------------------------------------------------------------- #
page(
    59, "Bheriv&amacr;daka", "The Drummer",
    meta_title="Ja 59 — The Drummer | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 59 — a boy's excessive drumming that draws the "
        "attention of bandits, and a proverb about moderation with a "
        "hidden second meaning. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A road home from a festival, after a successful "
                    "day of earnings"),
        ("Speaker", "The drummer, addressing his own son"),
        ("Form", "One four-line stanza, opening this chapter's final "
                 "matched pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short proverb with an embedded second "
                       "meaning"),
    ],
    why=(
        "This poem opens the last of this chapter's five matched "
        "pairs with a memorable onomatopoetic refrain, and Sujato's "
        "comment uncovers a wordplay hiding beneath its literal "
        "warning: the same word used for the earnings lost can also "
        "mean &lsquo;the good, the true&rsquo;, quietly widening the "
        "proverb's reach well beyond drumming."),
    guide=[
        ("Excess undoing what moderation had earned", [
            "The verse gives its own refrain: &lsquo;blow, blow, "
            "don't overblow, for overblowing is bad. By blowing a "
            "hundred was gained, by overblowing it was lost.&rsquo; "
            "Per Sujato's comment, a drummer and his boy earned money "
            "playing at a festival, but on the return journey the "
            "boy's incessant, excessive drumming attracted the "
            "attention of bandits, undoing their whole day's profit."]),
        ("A word doing double duty beneath the surface", [
            "Sujato's comment notes that &lsquo;sataṁ&rsquo; "
            "(explained literally as &lsquo;a hundred dollars&rsquo;) "
            "carries a second sense at the same time: &lsquo;the "
            "good, the true&rsquo;. The proverb's warning about "
            "excess ruining earned gain quietly widens, through this "
            "single word, into a warning about excess ruining any "
            "good thing at all."]),
        ("An instrument, and an onomatopoetic verb, in creative tension", [
            "Sujato's comment also observes that while the story and "
            "title speak of a &lsquo;drum&rsquo; (bheri), the verse "
            "itself uses &lsquo;dhamati&rsquo;, which normally means "
            "&lsquo;blows&rsquo; &mdash; the repeated idiom recalling "
            "an onomatopoetic Sanskrit root, applied here to "
            "percussion rather than the wind instrument it would more "
            "naturally describe, in a playful mismatch the "
            "translation's own choice of &lsquo;blow&rsquo; preserves."]),
    ],
    terms=[
        ("dhame dhame nātidhame",
         "&ldquo;blow, blow, don't overblow&rdquo; &mdash; the "
         "verse's onomatopoetic refrain, shared word for word with "
         "the next poem, Ja 60."),
        ("sataṁ",
         "&ldquo;a hundred&rdquo;, per Sujato's comment carrying a "
         "second sense at once: &ldquo;the good, the true&rdquo;."),
        ("dhamati",
         "&ldquo;blows&rdquo; &mdash; the verb the verse uses for "
         "the boy's drumming, per Sujato's comment normally "
         "describing a wind instrument rather than a drum."),
        ("Bherivādakajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Drummer&rsquo;."),
        ("Ja 60",
         "the next poem, closing this chapter with the identical "
         "opening refrain applied to a different instrument and "
         "family member."),
    ],
    text_intro=(
        "The text in full: a single verse, opening this chapter's "
        "final matched pair. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja59:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the boy's excessive drumming cause, per Sujato's comment?",
         "opts": [
             'It scares away potential customers',
             'Nothing significant',
             "It attracts the attention of bandits, undoing the day's earned profit",
             'It wakes up the whole village',
         ],
         "correct": 2,
         "expl": "Excess turning a successful day's earnings into a loss."},
        {"q": "What second meaning does Sujato's comment identify for 'sataṁ' (a hundred)?",
         "opts": [
             "'Danger' or 'threat'",
             'A specific place name',
             'No second meaning exists',
             "'The good, the true' — widening the proverb beyond literal money",
         ],
         "correct": 3,
         "expl": "Quietly extending the poem's warning about excess to any good thing at all, not just earnings."},
        {"q": "What mismatch does Sujato's comment note between the story's title and the verse's own vocabulary?",
         "opts": [
             "The story and title speak of a 'drum' (bheri), but the verse uses 'dhamati', a verb normally meaning 'blows' (as with a wind instrument)",
             'The verse never mentions any instrument',
             'The title refers to a different instrument entirely',
             'No mismatch exists',
         ],
         "correct": 0,
         "expl": "A playful mismatch the English translation's own choice of 'blow' preserves."},
        {"q": 'What refrain does this poem open, shared with the next poem, Ja 60?',
         "opts": [
             'No shared refrain',
             "'Blow, blow, don't overblow, for overblowing is bad'",
             'A refrain about silence',
             'A refrain about generosity',
         ],
         "correct": 1,
         "expl": "Opening this chapter's final matched pair."},
        {"q": 'How did the drummer and his son earn money, per the underlying story?',
         "opts": [
             'By farming',
             'By begging',
             'By playing drums at a festival',
             'By trading goods',
         ],
         "correct": 2,
         "expl": 'Successful earnings later undone on the return journey home.'},
        {"q": "What specifically drew the bandits' attention?",
         "opts": [
             'A loud argument',
             'Following the pair from the festival itself',
             'Visible wealth being displayed',
             "The boy's incessant, excessive drumming",
         ],
         "correct": 3,
         "expl": 'The very excess the proverb warns against.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Drummer (Bherivādakajātaka)',
             'The Horn-Blower',
             'The Lord of Langurs',
             'Three Qualities',
         ],
         "correct": 0,
         "expl": 'The fifty-ninth poem overall, and the ninth of the Āsīsavagga, opening its fifth and final matched pair.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The ninth poem of the Āsīsavagga, opening the final matched pair after Ja 51-58',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'The second-to-last poem of this ten-poem chapter.'},
        {"q": 'Who speaks this verse, addressing whom?',
         "opts": [
             'An unnamed narrator with no addressee',
             'A stranger, addressing the drummer',
             'The drummer, addressing his own son',
             'A bandit, addressing his victims',
         ],
         "correct": 2,
         "expl": "A father's warning, delivered too late to prevent the loss."},
        {"q": "What broader lesson does this poem's wordplay on 'sataṁ' suggest?",
         "opts": [
             'That drumming should never be practiced',
             'No broader lesson is suggested',
             'That money is the only thing that matters',
             "That the danger of excess applies not just to earnings but to 'the good, the true' more generally",
         ],
         "correct": 3,
         "expl": "A single word quietly widening the proverb's reach."},
    ],
    marginalia=[
        ("A hundred earned, a hundred lost", [
            "moderation gained it, excess threw it away —",
            "the whole story in one tight proverb"
        ]),
        ("A word meaning more than money", [
            "'sataṁ' — a hundred, but also 'the good, the true' —",
            "the warning reaches further than it first seems"
        ]),
        ("A drum called a wind instrument", [
            "the verb says 'blows', the title says 'drum' —",
            "a playful mismatch, preserved in translation"
        ]),
        ("The final pair of this chapter begins", [
            "one more matched poem to come —",
            "the same refrain, a different instrument"
        ]),
    ],
    further=[
        '<a href="%s/ja59/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-58.html">Ja 58 &mdash; Three Qualities</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-60.html">Ja 60 &mdash; The Horn-Blower</a> '
        "&mdash; the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 60 — Saṅkhadhama (The Horn-Blower)
# --------------------------------------------------------------------------- #
page(
    60, "Sa&#7749;khadhama", "The Horn-Blower",
    meta_title="Ja 60 — The Horn-Blower | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 60, closing the Āsīsavagga — this time a father, not "
        "a son, squanders the family's earnings by overblowing his "
        "own horn. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Six (Āsīsavagga) &middot; Poem 10 of 10 (closing the chapter)",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself, "
                    "addressed as if to a son about his father"),
        ("Form", "One four-line stanza, closing this chapter's final "
                 "matched pair"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse closing a matched pair, with "
                       "its own pun"),
    ],
    why=(
        "This poem closes the Āsīsavagga by reversing Ja 59's family "
        "roles: here it is the father, not the son, whose excess "
        "squanders what had been earned &mdash; and its closing line "
        "carries its own deliberate pun that the English translation "
        "manages to preserve almost exactly."),
    guide=[
        ("The same lesson, the roles reversed", [
            "The verse repeats its companion's opening refrain, then "
            "closes differently: &lsquo;by blowing riches were "
            "earned, but your blowing dad blew it.&rsquo; Per "
            "Sujato's comment, this story is similar to the previous "
            "one, except here the instrument is a conch or horn, and "
            "&lsquo;the father is the overplayer, not the son.&rsquo;"]),
        ("A pun the English translation manages to carry over intact", [
            "Sujato's comment highlights the play on words between "
            "&lsquo;dhama&rsquo; (&lsquo;blowing&rsquo;) and "
            "&lsquo;vidhamī&rsquo; (&lsquo;squandered it&rsquo;, "
            "literally &lsquo;blew it&rsquo;) &mdash; a rare case "
            "where the English idiom &lsquo;blew it&rsquo;, meaning "
            "to squander an opportunity, happens to preserve almost "
            "exactly the same double meaning the Pali original plays "
            "on."]),
        ("A citation reaching outside the Jātaka, and closing this chapter", [
            "Sujato's comment also notes that a work outside this "
            "site's own selections, the Milinda Pañha (Mil 3.1.4), "
            "discusses what happens when a horn player breathes out "
            "too much &mdash; a technical parallel to this poem's own "
            "concern, noted here without a linked page. This poem "
            "closes the Āsīsavagga, the sixth of eight chapters this "
            "site's selection draws from within the Ekakanipāta. The "
            "source text's own untranslated summary verse (uddāna) "
            "immediately follows, naming all ten poems of this "
            "chapter in sequence &mdash; not presented here as quoted "
            "text, since it carries no separate translation, but "
            "noted for completeness, as at the close of the previous "
            "five chapters."]),
    ],
    terms=[
        ("dhama",
         "&ldquo;blowing&rdquo; &mdash; the shared opening refrain's "
         "own key verb."),
        ("vidhamī",
         "&ldquo;squandered it&rdquo;, literally &ldquo;blew "
         "it&rdquo; &mdash; per Sujato's comment, a pun the English "
         "idiom happens to preserve almost exactly."),
        ("Saṅkhadhamajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Horn-Blower&rsquo;, closing the Āsīsavagga."),
        ("Mil 3.1.4",
         "the Milinda Pañha, a work outside this site's own "
         "selections, cited in Sujato's comment for a technical "
         "parallel about excessive horn-blowing."),
        ("Āsīsavaggo chaṭṭho",
         "&ldquo;the Āsīsavagga, the sixth [chapter]&rdquo; &mdash; "
         "the source text's own untranslated closing marker for this "
         "chapter, followed immediately by its summary verse."),
    ],
    text_intro=(
        "The text in full: a single verse, closing this chapter's "
        "final matched pair with its own preserved pun, discussed "
        "above. The chapter's own untranslated closing summary verse "
        "(uddāna), which follows immediately in the source text, is "
        "not quoted here since it carries no English translation, but "
        "its content &mdash; the ten poem titles of this chapter in "
        "sequence &mdash; matches this reading guide's own further "
        "reading list below. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja60:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this poem's story differ from Ja 59's, per Sujato's comment?",
         "opts": [
             'It concerns an entirely unrelated family',
             'No difference is noted',
             'It is identical in every detail',
             'The instrument is a conch or horn instead of a drum, and the father is the overplayer instead of the son',
         ],
         "correct": 3,
         "expl": "A reversal of family roles completing this chapter's final matched pair."},
        {"q": "What pun does Sujato's comment highlight in this poem's closing line?",
         "opts": [
             "The play between 'dhama' (blowing) and 'vidhamī' (squandered it, literally 'blew it')",
             "A pun on the father's name",
             "A pun unrelated to the poem's theme",
             'No pun is present',
         ],
         "correct": 0,
         "expl": "A rare case where the English idiom 'blew it' preserves almost exactly the same double meaning as the Pali original."},
        {"q": "What external work does Sujato's comment cite for a technical parallel about horn-blowing?",
         "opts": [
             'The Rig Veda',
             "The Milinda Pañha (Mil 3.1.4), outside this site's own selections",
             'The Dhammapada',
             'No external work is cited',
         ],
         "correct": 1,
         "expl": "Noted here without a linked page, since it falls outside this site's own text selections."},
        {"q": 'What chapter does this poem close?',
         "opts": [
             'It does not close a chapter',
             'The Atthakāmavagga',
             "The Āsīsavagga, the sixth of eight chapters this site's selection draws from",
             'The final chapter of the whole Jātaka',
         ],
         "correct": 2,
         "expl": "The source text's own untranslated summary verse (uddāna) follows immediately after."},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'It does not exist for this chapter',
             'It is presented as spoken by the father',
             'Yes, quoted in full',
             'No — it carries no separate English translation, so it is only noted for completeness',
         ],
         "correct": 3,
         "expl": 'Consistent with the same practice at the close of the previous five chapters.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Horn-Blower (Saṅkhadhamajātaka)',
             'Three Qualities',
             'The Lord of Langurs',
             'The Drummer',
         ],
         "correct": 0,
         "expl": 'The sixtieth poem overall, and the tenth and final poem of the Āsīsavagga.'},
        {"q": 'What refrain does this poem open with, shared with Ja 59?',
         "opts": [
             'No shared refrain',
             "'Blow, blow, don't overblow, for overblowing is bad'",
             'A refrain about wealth alone',
             'A refrain about silence',
         ],
         "correct": 1,
         "expl": "Completing this chapter's fifth and final matched pair."},
        {"q": "Who is the 'overplayer' in this poem's version of the tale?",
         "opts": [
             'Both father and son equally',
             'The son',
             'The father',
             'A stranger',
         ],
         "correct": 2,
         "expl": 'Reversing the family roles from Ja 59, where the son was the excessive player.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The first poem of a later chapter',
             'The first poem of the Āsīsavagga',
             'The tenth and final poem of the Āsīsavagga, closing this chapter',
         ],
         "correct": 3,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse following immediately after."},
        {"q": 'How many total matched pairs structured this entire chapter?',
         "opts": [
             'Five (Ja 51/52, 53/54, 55/56, 57/58, 59/60)',
             'Ten, with each poem paired to itself',
             'None — the chapter had no repeated structure',
             'Two',
         ],
         "correct": 0,
         "expl": "The most tightly paired chapter structure found across this site's Jātaka selection so far."},
    ],
    marginalia=[
        ("Roles reversed, same lesson learned", [
            "not the son this time, but the father —",
            "excess costs the family either way"
        ]),
        ("A pun that survives translation", [
            "'dhama' and 'vidhamī' — blowing and 'blew it' —",
            "English keeps almost the exact same joke"
        ]),
        ("A citation reaching beyond this collection", [
            "the Milinda Pañha on breathless horn-blowers —",
            "noted, though outside this site's own texts"
        ]),
        ("Five pairs, ten poems, one chapter closed", [
            "the Āsīsavagga's own summary follows —",
            "not quoted, since it has no translation"
        ]),
    ],
    further=[
        '<a href="%s/ja60/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-59.html">Ja 59 &mdash; The Drummer</a> '
        "&mdash; the poem immediately before this one, opening this "
        "matched pair.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
# Ja 61 — Asātamanta (The Spell of the Unpleasant)
# --------------------------------------------------------------------------- #
page(
    61, "As&amacr;tamanta", "The Spell of the Unpleasant",
    meta_title="Ja 61 — The Spell of the Unpleasant | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 61, opening the Itthivagga — a fictional 'spell' "
        "invented to teach a student his mother's own prejudice "
        "against women, presented honestly as historical material "
        "rather than an endorsed view. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "A student, resolving to leave lay life behind"),
        ("Form", "One stanza (six lines), opening a chapter with "
                 "difficult historical content"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "short, but opening a chapter with genuinely "
                       "difficult content"),
    ],
    why=(
        "This poem opens the Itthivagga (&lsquo;Women Chapter&rsquo;), "
        "whose first several poems voice explicit misogynistic "
        "attitudes from ancient source material. This reading guide "
        "presents that content honestly, as this site does throughout "
        "&mdash; describing what the text says and what Sujato's own "
        "comments observe about it, without treating the attitudes "
        "themselves as endorsed teaching."),
    guide=[
        ("A fictional pretext for teaching an existing prejudice", [
            "The verse gives a student's resolution: &lsquo;the women "
            "in the world called unclaimed &mdash; there is no "
            "confining them. They are rude and full of desires, like "
            "an all-consuming flame. Leaving them behind, I shall go "
            "forth and foster seclusion.&rsquo; Per Sujato's comment, "
            "a young student is told by his mother that his education "
            "is incomplete until he learns a mysterious &lsquo;spell "
            "of the unpleasant&rsquo;. His teacher knows no such spell "
            "exists, but recognizes what the mother actually wants: "
            "for her son to learn of what she considers &lsquo;the "
            "wickedness of women.&rsquo;"]),
        ("The story's own framing device, worth noticing", [
            "The tale itself is built around a fiction: there is no "
            "real &lsquo;spell&rsquo;, only a mother's existing "
            "prejudice, delivered to her son through an invented "
            "teaching device by a teacher who privately knows better. "
            "This reading guide notes that structure plainly, without "
            "presenting the resulting verse's sweeping claims about "
            "&lsquo;women in the world&rsquo; as this site's own "
            "position."]),
    ],
    terms=[
        ("asā",
         "&ldquo;unclaimed&rdquo;, per Sujato's comment resolved as "
         "&lsquo;a&rsquo; + &lsquo;sva&rsquo;, &ldquo;without an "
         "owner&rdquo;."),
        ("asātamanta",
         "&ldquo;the spell of the unpleasant&rdquo; &mdash; a "
         "fictional teaching device, per Sujato's comment invented to "
         "deliver an existing prejudice rather than a real spell."),
        ("sikhī sabbaghaso",
         "&ldquo;an all-consuming flame&rdquo; &mdash; one of the "
         "verse's sweeping images, given here as the text states it, "
         "not as an endorsed claim."),
        ("Asātamantajātaka",
         "the traditional title of this tale, opening the "
         "Itthivagga."),
        ("Itthivagga",
         "&ldquo;Women Chapter&rdquo; &mdash; this collection's "
         "seventh chapter, whose first several poems voice "
         "misogynistic attitudes from ancient source material, "
         "presented here as historical content rather than endorsed "
         "teaching."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, opening a "
        "chapter with genuinely difficult historical content, "
        "discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja61:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does the mother in this poem's underlying story tell her son, per Sujato's comment?",
         "opts": [
             "That his education is incomplete until he learns a mysterious 'spell of the unpleasant'",
             'That he should marry immediately',
             'That he should abandon his studies',
             'That his education is complete',
         ],
         "correct": 0,
         "expl": "Setting up the poem's fictional framing device."},
        {"q": 'Does the teacher believe such a spell actually exists?',
         "opts": [
             'Yes, and teaches it as real magic',
             'No — he knows there is no such spell, but recognizes what the mother actually wants taught',
             'The comment does not address this',
             'The teacher invents the spell independently',
         ],
         "correct": 1,
         "expl": "A fictional pretext for delivering the mother's own existing prejudice."},
        {"q": "How does this reading guide characterize the sweeping claims this verse makes about 'women in the world'?",
         "opts": [
             'The guide avoids addressing this question',
             "As this site's own endorsed teaching",
             'As historical content presented honestly, not as an endorsed position',
             'As claims this site asserts to be literally true',
         ],
         "correct": 2,
         "expl": "Consistent with this site's practice of presenting difficult historical material honestly rather than silently or as endorsed."},
        {"q": 'What chapter does this poem open?',
         "opts": [
             'The Kulāvakavagga',
             'It does not open a chapter',
             'The Āsīsavagga',
             'The Itthivagga (Women Chapter)',
         ],
         "correct": 3,
         "expl": 'Whose first several poems voice misogynistic attitudes from ancient source material.'},
        {"q": 'What structural device does the underlying story use, worth noticing according to this guide?',
         "opts": [
             "A fictional teaching device (the invented 'spell') used to deliver an already-existing prejudice",
             'A direct scholarly treatise',
             'No particular structure is noted',
             'A dialogue between equals',
         ],
         "correct": 0,
         "expl": "The 'spell' itself is acknowledged within the story as fictional."},
        {"q": 'What resolution does the student reach in the verse?',
         "opts": [
             'To marry as soon as possible',
             'To leave women behind and go forth into seclusion',
             'To confront his mother directly',
             'No resolution is stated',
         ],
         "correct": 1,
         "expl": "The verse's own closing action."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'Hard to Understand',
             'Since Infancy',
             'The Spell of the Unpleasant (Asātamantajātaka)',
             'The Philosopher',
         ],
         "correct": 2,
         "expl": 'The sixty-first poem overall, and the first of the Itthivagga.'},
        {"q": 'How many lines make up this verse?',
         "opts": [
             'Two lines',
             'Eight lines',
             'Four lines',
             'Six lines',
         ],
         "correct": 3,
         "expl": 'Slightly longer than the four-line form most common in this collection.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of the seventh chapter (Itthivagga), following the completed Āsīsavagga',
             'It stands outside any chapter',
             'The final poem of the Itthivagga',
             'The final poem of the Āsīsavagga',
         ],
         "correct": 0,
         "expl": "Opening this collection's seventh ten-poem chapter."},
        {"q": "What approach does this reading guide take toward this chapter's difficult content generally?",
         "opts": [
             'Silently omitting it',
             'Presenting it honestly, including any critical comments Sujato himself offers, without treating it as endorsed',
             'Presenting it as fully accurate and endorsed',
             'Refusing to translate the affected poems at all',
         ],
         "correct": 1,
         "expl": 'Consistent with the approach already established at Ja 13 earlier in this collection.'},
    ],
    marginalia=[
        ("A spell that doesn't exist", [
            "invented to deliver a mother's own view —",
            "the teacher knows it, and teaches it anyway"
        ]),
        ("A fiction built to carry a prejudice", [
            "no real magic, just an existing attitude —",
            "given a mysterious name to make it stick"
        ]),
        ("A chapter that opens honestly, not silently", [
            "difficult content, presented as what it is —",
            "described, not endorsed"
        ]),
        ("A resolution to withdraw entirely", [
            "leaving behind what he's just been taught to fear —",
            "seclusion chosen as the response"
        ]),
    ],
    further=[
        '<a href="%s/ja61/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-60.html">Ja 60 &mdash; The Horn-Blower</a> '
        "&mdash; the closing poem of the previous chapter.",
        '<a href="ja-62.html">Ja 62 &mdash; Since Infancy</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 62 — Aṇḍabhūta (Since Infancy)
# --------------------------------------------------------------------------- #
page(
    62, "A&#7751;&#7693;abh&umacr;ta", "Since Infancy",
    meta_title="Ja 62 — Since Infancy | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 62 — a woman deliberately entrapped through cruelty "
        "and deception to 'prove' a claim about her own nature, "
        "presented here with the coercion it actually involved made "
        "explicit. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; disturbing underlying content, "
                       "presented with the coercion made explicit"),
    ],
    why=(
        "This poem's underlying story is genuinely troubling once "
        "read closely: a woman held in captivity her whole life is "
        "then deliberately, cruelly deceived into infidelity in order "
        "to &lsquo;prove&rsquo; a man's claim about women's nature "
        "&mdash; meaning the verse's conclusion is not evidence of "
        "anything about women at all, but a record of the harm done "
        "to secure it."),
    guide=[
        ("A verse presenting a conclusion as if it were simply observed", [
            "The verse states its point as though self-evident: "
            "&lsquo;the brahmin who played the harp while blindfolded "
            "had raised his wife since infancy &mdash; who would ever "
            "trust such women?&rsquo; Read on its own, this sounds "
            "like a simple cautionary proverb."]),
        ("A story of captivity and engineered betrayal, not natural weakness", [
            "Per Sujato's comment, the full story is considerably "
            "darker: an innocent baby girl was sold into slavery and "
            "kept locked up under guard her entire life by a brahmin "
            "who married her &mdash; done specifically to feed his "
            "gambling addiction, refuting a rival's own lucky charm "
            "(an oath asserting that all women are faithless). When "
            "the brahmin began winning, his adversary employed a "
            "&lsquo;knave&rsquo; who cruelly deceived the "
            "imprisoned woman's own attendant in order to engineer "
            "exactly the infidelity the wager required."]),
        ("What the story actually demonstrates, read honestly", [
            "Read in full, this story does not show a natural "
            "tendency in the woman at its center &mdash; it shows a "
            "woman held captive her entire life, then deliberately "
            "and cruelly manipulated by outside actors specifically "
            "to produce a predetermined result for a gambling bet "
            "between two men. This reading guide presents that fuller "
            "context directly, since the bare verse alone conceals "
            "far more than it reveals about what actually happened."]),
    ],
    terms=[
        ("bhatā bhariyā",
         "&ldquo;had raised his wife since infancy&rdquo; &mdash; "
         "the verse's own description of a woman held captive from "
         "childhood, giving this poem its traditional title."),
        ("ko jātu vissase",
         "&ldquo;who would ever trust such women?&rdquo; &mdash; the "
         "verse's rhetorical conclusion, presented by the text as "
         "though self-evidently proven."),
        ("dice wager",
         "per Sujato's comment, the actual motive behind the "
         "brahmin's marriage: an attempt to refute a rival gambler's "
         "lucky charm asserting all women are faithless."),
        ("Aṇḍabhūtajātaka",
         "the traditional title of this tale, &lsquo;Since "
         "Infancy&rsquo;."),
        ("knave",
         "per Sujato's comment, the agent employed by the brahmin's "
         "rival to deceive the captive woman's attendant, "
         "deliberately engineering the outcome the wager required."),
    ],
    text_intro=(
        "The text in full: a single verse, whose fuller context "
        "Sujato's own comment reveals to be considerably more "
        "disturbing than the bare text alone suggests, discussed "
        "above. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja62:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What does the bare verse present as though self-evident?',
         "opts": [
             'A specific historical fact about one couple',
             "A general rhetorical conclusion — 'who would ever trust such women?' — as though naturally proven",
             'A neutral description with no conclusion',
             'A question with no implied answer',
         ],
         "correct": 1,
         "expl": 'Read on its own, without the fuller story, it sounds like a simple cautionary proverb.'},
        {"q": "What was actually done to the woman at the center of this story, per Sujato's comment?",
         "opts": [
             'The comment gives no details of her life',
             'She lived a normal, free life',
             'She was sold into slavery as an infant and kept locked up under guard her entire life',
             'She chose her own circumstances freely',
         ],
         "correct": 2,
         "expl": 'Held captive from infancy by the man who later married her.'},
        {"q": "What was the brahmin's actual motive for this marriage, per the comment?",
         "opts": [
             'A political alliance',
             'Religious obligation',
             'Genuine affection',
             "To feed his gambling addiction, refuting a rival's lucky charm about women's faithlessness",
         ],
         "correct": 3,
         "expl": 'Using her as a pawn in an ongoing wager with another gambler.'},
        {"q": "How was the 'infidelity' the verse alludes to actually brought about?",
         "opts": [
             "A rival deliberately employed a knave to cruelly deceive the woman's own attendant, engineering the outcome",
             'The woman herself initiated it freely',
             'The comment does not explain how it occurred',
             'It arose naturally with no outside involvement',
         ],
         "correct": 0,
         "expl": 'A deliberate, calculated act of deception and manipulation by outside parties.'},
        {"q": 'What does this reading guide conclude the story actually demonstrates, read in full?',
         "opts": [
             "That the verse's claim about women is proven true",
             'That the woman was held captive and then deliberately manipulated to produce a predetermined result for a gambling bet — not evidence of any natural tendency',
             "That the brahmin's suspicions were entirely justified",
             'Nothing beyond what the bare verse states',
         ],
         "correct": 1,
         "expl": 'The bare verse alone conceals far more than it reveals about what actually happened.'},
        {"q": 'Why does this reading guide present the fuller context of this story rather than just the bare verse?',
         "opts": [
             "To defend the brahmin's actions",
             'To make the story more entertaining',
             'Because the bare verse alone conceals the coercion and deception underlying its stated conclusion',
             'There is no particular reason given',
         ],
         "correct": 2,
         "expl": "Consistent with this site's practice of engaging honestly with difficult historical material."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Philosopher',
             'Dissatisfaction',
             'The Spell of the Unpleasant',
             'Since Infancy (Aṇḍabhūtajātaka)',
         ],
         "correct": 3,
         "expl": 'The sixty-second poem overall, and the second of the Itthivagga.'},
        {"q": "What visual record does Sujato's comment mention for this story?",
         "opts": [
             'The brahmin of this story is depicted in a Bharhut sculpture',
             'A painting in a specific temple',
             'A modern illustration only',
             'No visual record exists',
         ],
         "correct": 0,
         "expl": "Evidence of the story's circulation and recognition in ancient Buddhist art."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The second poem of the Itthivagga, following Ja 61',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": 'Part of the same ten-poem Itthivagga.'},
        {"q": 'Who bears the moral responsibility, per the fuller context this reading guide presents?',
         "opts": [
             "The woman's attendant alone",
             'The captive woman alone',
             'The brahmin and his rival, who together engineered her captivity and manipulation',
             'No one — the outcome was inevitable',
         ],
         "correct": 2,
         "expl": 'The men who orchestrated both her lifelong captivity and the deception that produced the outcome they wanted.'},
    ],
    marginalia=[
        ("A conclusion stated as if self-evident", [
            "'who would ever trust such women?' —",
            "a question that hides everything that came before it"
        ]),
        ("A life spent locked away, from infancy on", [
            "sold as a baby, guarded her whole life —",
            "not a choice, a captivity"
        ]),
        ("A bet between two men, and a woman as its pawn", [
            "gambling debts settled through cruelty —",
            "a knave hired specifically to engineer betrayal"
        ]),
        ("What the story actually proves", [
            "not a fact about women, but about coercion —",
            "the verse's conclusion built on manufactured evidence"
        ]),
    ],
    further=[
        '<a href="%s/ja62/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-61.html">Ja 61 &mdash; The Spell of the '
        "Unpleasant</a> &mdash; the poem immediately before this one.",
        '<a href="ja-63.html">Ja 63 &mdash; The Philosopher</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 63 — Takkapaṇḍita (The Philosopher)
# --------------------------------------------------------------------------- #
page(
    63, "Takkapa&#7751;&#7693;ita", "The Philosopher",
    meta_title="Ja 63 — The Philosopher | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 63 — an imprecation the traditional commentary reads "
        "as aimed at women, though Sujato's own comment finds "
        "grammatical grounds to doubt that reading. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; a case where the traditional target of "
                       "an imprecation is genuinely uncertain"),
    ],
    why=(
        "This poem is placed within the Itthivagga by the traditional "
        "commentary, which reads its opening imprecation as directed "
        "at women &mdash; but Sujato's own comment finds a genuine "
        "grammatical basis to doubt that reading, noting that the "
        "verse's grammar does not actually require it and may not "
        "have originally concerned women at all."),
    guide=[
        ("An imprecation, and advice to live above it", [
            "The verse opens sharply: &lsquo;hateful ingrates! "
            "Slanderous traitors!&rsquo; &mdash; before turning to "
            "instruction: &lsquo;live the spiritual life, mendicant, "
            "you will not be bereft of happiness.&rsquo; Per Sujato's "
            "comment, the traditional commentary explains these "
            "opening lines as directed against women."]),
        ("A grammatical basis for genuine doubt", [
            "Sujato's comment observes something the traditional "
            "reading passes over: the grammatical gender across these "
            "lines is ambiguous, except for one word "
            "(&lsquo;akataññū&rsquo;, &lsquo;ingrates&rsquo;), which "
            "is masculine plural. The comment concludes that "
            "&lsquo;either a non-standard form is used, or the verse "
            "was not originally about women&rsquo; at all &mdash; an "
            "honest acknowledgment that the traditional interpretive "
            "framing of this whole chapter may, in this specific "
            "case, rest on shakier ground than it first appears."]),
        ("A parallel already on this site", [
            "Sujato's comment also points to a parallel at this "
            "site's own AN 5.230, connecting this verse's second half "
            "to a broader, already-completed discussion of monastic "
            "conduct and its rewards."]),
    ],
    terms=[
        ("kodhanā akataññū ca",
         "&ldquo;hateful ingrates!&rdquo; &mdash; the verse's "
         "opening imprecation, with &lsquo;akataññū&rsquo; "
         "grammatically masculine plural, per Sujato's comment "
         "casting doubt on the traditional reading that it targets "
         "women."),
        ("takka",
         "normally &ldquo;logic&rdquo;, giving this poem its "
         "traditional title, &lsquo;The Philosopher&rsquo;."),
        ("brahmacariyaṁ cara",
         "&ldquo;live the spiritual life&rdquo; &mdash; the verse's "
         "positive instruction, following its opening imprecation."),
        ("Takkapaṇḍitajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Philosopher&rsquo;."),
        ("AN 5.230",
         "the already-completed page on this site Sujato's comment "
         "connects to this verse's second half."),
    ],
    text_intro=(
        "The text in full: a single verse, whose traditional framing "
        "Sujato's own comment casts genuine grammatical doubt on, "
        "discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja63:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does the traditional commentary read this verse's opening imprecation, per Sujato's comment?",
         "opts": [
             'As having no specific target',
             'As directed against kings',
             'As directed against women',
             'As directed against animals',
         ],
         "correct": 2,
         "expl": "The reading this reading guide's own discussion goes on to question."},
        {"q": "What grammatical detail does Sujato's comment note about this verse?",
         "opts": [
             'That the verse contains no gendered forms at all',
             'That the verse is grammatically incomplete',
             'That the grammar is entirely unambiguous throughout',
             'That the gender is ambiguous except for one word, which is masculine plural',
         ],
         "correct": 3,
         "expl": "A detail the traditional commentary's reading passes over."},
        {"q": "What conclusion does Sujato's comment draw from this grammatical observation?",
         "opts": [
             'That either a non-standard form is used, or the verse was not originally about women at all',
             "That the verse's meaning is now permanently lost",
             'No conclusion is drawn',
             'That the traditional reading is certainly correct',
         ],
         "correct": 0,
         "expl": 'An honest acknowledgment that the traditional framing may rest on shakier ground than it first appears.'},
        {"q": "What already-completed page on this site does Sujato's comment connect to this verse's second half?",
         "opts": [
             'Snp 3.12',
             'AN 5.230',
             'Dhp 179',
             'No connection is made',
         ],
         "correct": 1,
         "expl": "Linking this verse's positive instruction to a broader already-completed discussion."},
        {"q": 'What positive instruction does the verse turn to after its opening imprecation?',
         "opts": [
             'No positive instruction follows',
             'A call to violence',
             "'Live the spiritual life, mendicant, you will not be bereft of happiness'",
             'A call to abandon all relationships',
         ],
         "correct": 2,
         "expl": "The verse's constructive turn, regardless of who or what its opening imprecation targets."},
        {"q": "What does 'takka' normally mean, giving this poem its title?",
         "opts": [
             "'War'",
             "'Marriage'",
             "'Wealth'",
             "'Logic', with an alternate title referring to a philosopher",
         ],
         "correct": 3,
         "expl": "The traditional title, 'The Philosopher'."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Philosopher (Takkapaṇḍitajātaka)',
             'Hard to Understand',
             'Dissatisfaction',
             'Since Infancy',
         ],
         "correct": 0,
         "expl": 'The sixty-third poem overall, and the third of the Itthivagga.'},
        {"q": "Why does this reading guide highlight the grammatical ambiguity Sujato's comment raises?",
         "opts": [
             'To dismiss the comment as unreliable',
             "Because it offers a genuine, scholarly basis for doubting whether this poem's traditional placement in the 'women' theme is accurate",
             'For no particular reason',
             'To argue the traditional reading is definitely wrong',
         ],
         "correct": 1,
         "expl": 'An honest engagement with uncertainty, rather than treating the traditional framing as settled fact.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The third poem of the Itthivagga, following Ja 61 and Ja 62',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Itthivagga.'},
        {"q": "What is the verse's reading uncertain about, per Sujato's comment on 'vihāhasi'?",
         "opts": [
             "Only the poem's title is uncertain",
             "The entire verse's authenticity is disputed",
             'Nothing — every word is certain',
             "The reading of 'vihāhasi' itself is uncertain, and Sujato follows the commentary's interpretation there",
         ],
         "correct": 3,
         "expl": 'A further layer of textual uncertainty noted honestly in the comment.'},
    ],
    marginalia=[
        ("An imprecation, and a doubt about its target", [
            "the tradition says 'women' —",
            "the grammar itself isn't so sure"
        ]),
        ("One masculine word, undoing a whole reading", [
            "'akataññū' doesn't fit the traditional claim —",
            "Sujato names the problem plainly"
        ]),
        ("Advice that stands regardless", [
            "live the spiritual life, whoever the target —",
            "the constructive turn survives the uncertainty"
        ]),
        ("Honesty about what isn't settled", [
            "not every reading in this tradition is certain —",
            "this guide says so, rather than pretending otherwise"
        ]),
    ],
    further=[
        '<a href="%s/ja63/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../anguttara-nikaya/an-5.230.html">AN 5.230</a> '
        "&mdash; connected in Sujato's comment to this verse's "
        "second half.",
        '<a href="ja-62.html">Ja 62 &mdash; Since Infancy</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-64.html">Ja 64 &mdash; Hard to Understand</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 64 — Durājāna (Hard to Understand)
# --------------------------------------------------------------------------- #
page(
    64, "Dur&amacr;j&amacr;na", "Hard to Understand",
    meta_title="Ja 64 — Hard to Understand | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 64 — a husband advised to stop trying to understand "
        "his wife, in a verse whose closing image is echoed almost "
        "verbatim to describe the Dhamma itself. From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified, offering counsel to a confused "
                    "husband"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but resting on a reductive premise "
                       "worth naming honestly"),
    ],
    why=(
        "This poem's underlying advice deserves a plain, unflattering "
        "summary: rather than making any effort to actually "
        "understand his wife, a confused husband is told simply to "
        "stop trying &mdash; and yet its closing image, describing "
        "human complexity as hard to fathom, is used almost word for "
        "word elsewhere in this site's own Sutta Nipāta to describe "
        "the Dhamma itself."),
    guide=[
        ("Advice to stop trying, rather than to understand", [
            "The verse counsels indifference directly: &lsquo;do not "
            "rejoice, “she loves me,” nor lament, “she loves me "
            "not.” The mood of women is hard to understand, like the "
            "track of fish in water.&rsquo; Per Sujato's comment, a "
            "husband, confused by his wife's shifting behavior "
            "toward him, seeks counsel &mdash; and rather than being "
            "encouraged to make any effort to actually understand "
            "her, he is advised simply to disregard her feelings "
            "altogether."]),
        ("A closing image echoed elsewhere for something entirely different", [
            "Sujato's comment notes that the phrase &lsquo;hard to "
            "understand&rsquo; is also applied, at this site's own "
            "Snp 3.12, to the Dhamma itself &mdash; an unexpected "
            "resonance: the same language used dismissively here to "
            "excuse not trying is used elsewhere to honor something "
            "worth the deepest possible effort to understand."]),
    ],
    terms=[
        ("thīnaṁ bhāvo durājāno",
         "&ldquo;the mood of women is hard to understand&rdquo; "
         "&mdash; the verse's central claim, echoed at this site's "
         "own Snp 3.12 in reference to the Dhamma."),
        ("macchasseva udake gataṁ",
         "&ldquo;like the track of fish in water&rdquo; &mdash; the "
         "verse's closing image for something too elusive to trace."),
        ("Durājānajātaka",
         "the traditional title of this tale, &lsquo;Hard to "
         "Understand&rsquo;."),
        ("Snp 3.12",
         "&ldquo;Contemplating Pairs&rdquo; &mdash; the "
         "already-completed page on this site where the same phrase "
         "&lsquo;hard to understand&rsquo; describes the Dhamma."),
        ("mativippahīno",
         "a term from this site's own Ja 44 for an absence of "
         "judgment; this poem's advice to simply stop trying shares "
         "something of that same underlying failure of effort."),
    ],
    text_intro=(
        "The text in full: a single verse, whose closing image "
        "recurs elsewhere on this site in a very different context, "
        "discussed above. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja64:1.1-1.4"),
    ],
    quiz=[
        {"q": "What advice does the verse give a husband confused by his wife's behavior?",
         "opts": [
             'To seek a divorce immediately',
             'To confront her directly and demand an explanation',
             'To make a greater effort to understand her',
             'To stop trying to interpret her feelings at all — neither rejoicing nor lamenting',
         ],
         "correct": 3,
         "expl": 'A reductive response that this reading guide names plainly rather than dressing up.'},
        {"q": "What behavior pattern does Sujato's comment describe as prompting the husband's confusion?",
         "opts": [
             'Shifting behavior depending on whether she has behaved well or badly toward him',
             'No specific pattern is described',
             'Total silence on her part',
             'A completely static, unchanging demeanor',
         ],
         "correct": 0,
         "expl": 'A complexity the advice given responds to by simply disengaging rather than engaging.'},
        {"q": "What already-completed page on this site does Sujato's comment connect to this verse's closing phrase?",
         "opts": [
             'AN 5.230',
             'Snp 3.12, where the same phrase describes the Dhamma itself',
             'Dhp 179',
             'No connection is made',
         ],
         "correct": 1,
         "expl": 'An unexpected resonance between two very different uses of the same language.'},
        {"q": 'How does this reading guide characterize the advice this poem gives?',
         "opts": [
             'The guide offers no characterization',
             'As wise and worth following',
             'As reductive — telling the husband to stop trying rather than to actually understand',
             'As deeply compassionate',
         ],
         "correct": 2,
         "expl": 'A plain, unflattering summary rather than a dressed-up one.'},
        {"q": "What image does the verse use for the difficulty of understanding the wife's mood?",
         "opts": [
             'The pattern of falling leaves',
             'The shape of clouds',
             'The path of a bird in the sky',
             'The track of fish in water',
         ],
         "correct": 3,
         "expl": 'Something that leaves no trace to follow, closing the verse.'},
        {"q": 'What does the same closing phrase describe when it appears at Snp 3.12?',
         "opts": [
             'The Dhamma itself',
             "A king's decree",
             'A natural disaster',
             'A different woman entirely',
         ],
         "correct": 0,
         "expl": 'Language used dismissively here, but used elsewhere to honor something worth the deepest effort to understand.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'The Philosopher',
             'Hard to Understand (Durājānajātaka)',
             'Dissatisfaction',
             'Queen Sweetheart',
         ],
         "correct": 1,
         "expl": 'The sixty-fourth poem overall, and the fourth of the Itthivagga.'},
        {"q": "Does the verse's advice ask the husband to change his own behavior toward his wife?",
         "opts": [
             'It asks him to seek outside counsel repeatedly',
             'Yes, extensively',
             'No — it asks him only to disengage emotionally from trying to interpret her',
             'It asks him to apologize',
         ],
         "correct": 2,
         "expl": 'A response of withdrawal rather than genuine engagement or understanding.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The fourth poem of the Itthivagga, following Ja 61 through Ja 63',
         ],
         "correct": 3,
         "expl": 'Part of the same ten-poem Itthivagga.'},
        {"q": 'What irony does this reading guide draw out from the Snp 3.12 connection?',
         "opts": [
             'The same phrase dismisses human complexity here, while honoring something worth deep effort elsewhere',
             'Both uses are equally dismissive',
             "The connection undermines Snp 3.12's own teaching",
             'No irony is present',
         ],
         "correct": 0,
         "expl": 'A resonance worth noticing rather than passing over.'},
    ],
    marginalia=[
        ("Advice to simply stop trying", [
            "not understanding, just disengaging —",
            "a reductive answer to a real confusion"
        ]),
        ("A phrase that means something else, elsewhere", [
            "'hard to understand' — used here dismissively —",
            "at Snp 3.12, the same words honor the Dhamma"
        ]),
        ("A track no one can follow", [
            "fish leaving no trace in water —",
            "the verse's own image for what it won't try to read"
        ]),
        ("Complexity, met with withdrawal", [
            "not engagement, but simple avoidance —",
            "this guide names the advice for what it is"
        ]),
    ],
    further=[
        '<a href="%s/ja64/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../sutta-nipata/snp-3.12.html">Snp 3.12 &mdash; '
        "Contemplating Pairs</a> &mdash; where the same phrase "
        "&lsquo;hard to understand&rsquo; describes the Dhamma "
        "itself.",
        '<a href="ja-63.html">Ja 63 &mdash; The Philosopher</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-65.html">Ja 65 &mdash; Dissatisfaction</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 65 — Anabhirati (Dissatisfaction)
# --------------------------------------------------------------------------- #
page(
    65, "Anabhirati", "Dissatisfaction",
    meta_title="Ja 65 — Dissatisfaction | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 65 — a verse comparing women to public taverns, met "
        "with Sujato's own sharpest direct rebuttal in this whole "
        "collection: 'contrary to the story, studies consistently "
        "indicate that men cheat more than women.' From Ru-Yi "
        "Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "short, but paired with the translator's own "
                       "direct factual rebuttal"),
    ],
    why=(
        "Sujato's own comment on this verse offers this whole "
        "chapter's most direct, unambiguous factual correction: "
        "against a verse comparing women to public taverns available "
        "to all, the comment states plainly, &lsquo;contrary to the "
        "story, studies consistently indicate that men cheat more "
        "than women.&rsquo; This reading guide features that "
        "rebuttal prominently, exactly as it appears in the source "
        "material."),
    guide=[
        ("A comparison meant to justify indifference to infidelity", [
            "The verse states its claim through comparison: "
            "&lsquo;just like rivers and roads, taverns, hotels, and "
            "pubs, are those called women in the world. Sages do not "
            "get angry with them.&rsquo; Per Sujato's comment, the "
            "underlying story holds that women are, by their nature, "
            "&lsquo;available to all&rsquo;, so a wise man should not "
            "be upset when his own wife is unfaithful."]),
        ("Sujato's own direct, factual rebuttal", [
            "Sujato's comment does not let this pass unremarked. It "
            "states plainly: &lsquo;contrary to the story, studies "
            "consistently indicate that men cheat more than "
            "women.&rsquo; This is the most direct, unambiguous "
            "factual correction found anywhere in this whole "
            "collection's comments &mdash; naming the verse's "
            "underlying claim as simply false, rather than merely "
            "noting historical context or textual ambiguity."]),
        ("A cross-reference to this site's own SN 9.8", [
            "Sujato's comment also compares this poem to this site's "
            "own already-completed SN 9.8, connecting this verse's "
            "underlying theme to a discourse already treated "
            "elsewhere on this site."]),
    ],
    terms=[
        ("lokitthiyo",
         "&ldquo;women in the world&rdquo; &mdash; the verse's own "
         "sweeping comparison, given here as the text states it, not "
         "as an endorsed claim."),
        ("nāsaṁ kujjhanti paṇḍitā",
         "&ldquo;sages do not get angry with them&rdquo; &mdash; the "
         "verse's own conclusion, built on the comparison Sujato's "
         "comment directly rebuts."),
        ("studies consistently indicate",
         "the opening of Sujato's own direct factual correction to "
         "this verse's underlying premise, quoted in full above."),
        ("Anabhiratijātaka",
         "the traditional title of this tale, "
         "&lsquo;Dissatisfaction&rsquo;."),
        ("SN 9.8",
         "&ldquo;The Mistress of the House&rdquo; &mdash; the "
         "already-completed page on this site Sujato's comment "
         "compares to this poem, previously cross-linked from this "
         "site's own Ja 14."),
    ],
    text_intro=(
        "The text in full: a single verse, accompanied by this whole "
        "collection's most direct factual rebuttal in Sujato's own "
        "comment, quoted in full above. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja65:1.1-1.4"),
    ],
    quiz=[
        {"q": 'What comparison does the verse draw?',
         "opts": [
             'Women compared to rivers, roads, taverns, hotels, and pubs — available to all',
             'Women compared to fortified cities',
             'No comparison is made',
             'Women compared to precious jewels',
         ],
         "correct": 0,
         "expl": "Used to argue that a wise man should not be upset by his wife's infidelity."},
        {"q": "What does Sujato's own comment state directly in response to this verse's premise?",
         "opts": [
             "Full agreement with the verse's claim",
             "'Contrary to the story, studies consistently indicate that men cheat more than women'",
             'That the question cannot be answered',
             'No response is given',
         ],
         "correct": 1,
         "expl": "The most direct, unambiguous factual correction found anywhere in this collection's comments."},
        {"q": "How does this rebuttal differ from Sujato's comments on earlier poems in this chapter, such as Ja 63's grammatical doubt?",
         "opts": [
             'It avoids taking any position at all',
             'It is essentially the same kind of comment',
             "It names the verse's underlying claim as simply false, based on evidence, rather than raising textual or grammatical uncertainty",
             'It is less direct than the earlier comments',
         ],
         "correct": 2,
         "expl": 'A direct, factual correction rather than a philological observation.'},
        {"q": "What already-completed page does Sujato's comment compare this poem to?",
         "opts": [
             'Snp 3.12',
             'No comparison is made',
             'AN 5.230',
             "SN 9.8, previously cross-linked from this site's own Ja 14",
         ],
         "correct": 3,
         "expl": "Connecting this verse's underlying theme to a discourse already treated elsewhere on this site."},
        {"q": 'What conclusion does the verse draw from its comparison?',
         "opts": [
             'That sages do not get angry when their wives are unfaithful',
             'That women should never marry',
             'No conclusion is drawn',
             'That women should be punished for infidelity',
         ],
         "correct": 0,
         "expl": "The verse's own closing line, following its comparison."},
        {"q": "Why does this reading guide feature Sujato's rebuttal prominently?",
         "opts": [
             'To avoid discussing the verse at all',
             "Because it is the source material's own translator directly correcting the verse's underlying factual claim, presented exactly as it appears",
             'To argue the rebuttal itself is mistaken',
             'There is no particular reason',
         ],
         "correct": 1,
         "expl": "Consistent with this site's practice of presenting difficult content honestly, including the translator's own critical response."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'In My Lap',
             'Hard to Understand',
             'Dissatisfaction (Anabhiratijātaka)',
             'Queen Sweetheart',
         ],
         "correct": 2,
         "expl": 'The sixty-fifth poem overall, and the fifth of the Itthivagga.'},
        {"q": "What specific method does Sujato's comment use to rebut the verse's claim?",
         "opts": [
             'A personal opinion with no supporting basis',
             'No method is specified',
             'An appeal to religious authority alone',
             'A reference to modern studies and their consistent findings',
         ],
         "correct": 3,
         "expl": "Citing empirical evidence directly against the verse's stated premise."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The fifth poem of the Itthivagga, following Ja 61 through Ja 64',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Itthivagga.'},
        {"q": "What pattern does this poem, alongside Ja 63, establish about how this reading guide handles this chapter's difficult content?",
         "opts": [
             'It ignores all critical comments',
             "It presents the verses honestly while also foregrounding Sujato's own critical responses where they exist",
             "It presents only the verses' claims as settled fact",
             'It refuses to translate any further poems in this chapter',
         ],
         "correct": 1,
         "expl": 'A consistent approach carried through this entire difficult chapter.'},
    ],
    marginalia=[
        ("A comparison meant to excuse indifference", [
            "women likened to taverns, open to all —",
            "used to argue a husband shouldn't mind betrayal"
        ]),
        ("The sharpest rebuttal in this whole collection", [
            "'studies consistently indicate' otherwise —",
            "Sujato's own comment, stated without hedging"
        ]),
        ("Evidence answering assertion", [
            "not textual doubt this time, but a factual correction —",
            "the verse's premise named simply false"
        ]),
        ("A rebuttal quoted, not buried", [
            "featured here exactly as the source gives it —",
            "honesty about what the translator himself objected to"
        ]),
    ],
    further=[
        '<a href="%s/ja65/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment, including the full comment "
        "discussed above." % SC,
        '<a href="../samyutta-nikaya/sn-9.8.html">SN 9.8 &mdash; The '
        "Mistress of the House</a> &mdash; compared to this poem in "
        "Sujato's own comment.",
        '<a href="ja-64.html">Ja 64 &mdash; Hard to Understand</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-66.html">Ja 66 &mdash; Queen Sweetheart</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 66 — Mudulakkhaṇa (Queen Sweetheart)
# --------------------------------------------------------------------------- #
page(
    66, "Mudulakkha&#7751;a", "Queen Sweetheart",
    meta_title="Ja 66 — Queen Sweetheart | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 66 — not about women's nature but about craving's "
        "own, discovering that getting exactly what you wanted only "
        "multiplies the wanting. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "An ascetic, reflecting on his own desire "
                    "fulfilled"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse about the nature of craving "
                       "itself"),
    ],
    why=(
        "Unlike several of this chapter's other poems, this verse's "
        "real target is not women at all, but the nature of craving "
        "itself &mdash; using one man's desire as its occasion to "
        "observe something that applies equally to any object of "
        "want: getting exactly what you wished for does not shrink "
        "your wanting, but multiplies it."),
    guide=[
        ("Desire fulfilled, only to multiply", [
            "The verse gives its own honest reversal: &lsquo;one wish "
            "I had in the past, before I won Queen Sweetheart. But "
            "when I won the moon-eyed lady, wish upon wish was "
            "born.&rsquo; Per Sujato's comment, an ascetic desires "
            "the queen, but once he actually gains her, he finds his "
            "list of desires does not shrink but grows."]),
        ("A verse about craving's own logic, not about her character", [
            "This poem's insight does not concern anything about the "
            "queen herself &mdash; it concerns the structure of "
            "craving, which by its own nature never resolves through "
            "satisfaction, only multiplies. Unlike several of this "
            "chapter's other poems, the object of desire here is "
            "incidental to the point being made, which could equally "
            "apply to any object of longing."]),
    ],
    terms=[
        ("mudulakkhaṇa",
         "&ldquo;Queen Sweetheart&rdquo;, literally &ldquo;of soft, "
         "gentle characteristics&rdquo; &mdash; giving this poem its "
         "traditional title."),
        ("icchā icchaṁ vijāyatha",
         "&ldquo;wish upon wish was born&rdquo; &mdash; the verse's "
         "own central observation about the self-multiplying nature "
         "of craving."),
        ("aḷārakkhī",
         "&ldquo;moon-eyed&rdquo;, per Sujato's comment a term "
         "meaning wide-open, expressive eyes."),
        ("Mudulakkhaṇajātaka",
         "the traditional title of this tale, &lsquo;Queen "
         "Sweetheart&rsquo;."),
        ("craving's own structure",
         "the poem's actual subject, per this reading guide, using a "
         "specific desire as its occasion without the verse's insight "
         "depending on anything about its particular object."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja66:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the ascetic discover after winning the queen he desired, per Sujato's comment?",
         "opts": [
             'That his desires are now completely satisfied',
             'That his list of desires does not shrink but grows',
             'That he no longer wants anything at all',
             'The comment does not address the outcome',
         ],
         "correct": 1,
         "expl": "'Wish upon wish was born.'"},
        {"q": "What does this reading guide say this poem's real target is?",
         "opts": [
             'A specific historical event',
             "The queen's own character specifically",
             'The nature and structure of craving itself, not anything about the object of desire',
             'A general condemnation of marriage',
         ],
         "correct": 2,
         "expl": "Unlike several of this chapter's other poems, the object of desire is incidental to the point."},
        {"q": "How does this poem's underlying insight compare to earlier poems in this chapter?",
         "opts": [
             "It is unrelated to any of this chapter's other themes",
             "It repeats Ja 65's argument exactly",
             'It makes the same misogynistic claim in different words',
             "It shifts focus away from women's nature entirely, toward the self-multiplying nature of craving generally",
         ],
         "correct": 3,
         "expl": 'A notable shift within this difficult chapter, toward a universal teaching about desire itself.'},
        {"q": "What does 'aḷārakkhī' mean, per Sujato's comment?",
         "opts": [
             "'Moon-eyed', describing wide-open, expressive eyes",
             "'Golden-haired'",
             'A proper name unrelated to appearance',
             "'Sharp-tongued'",
         ],
         "correct": 0,
         "expl": "A descriptive epithet for the queen, giving color to the verse's imagery."},
        {"q": "Could this poem's central insight apply equally to objects of desire other than a person?",
         "opts": [
             'No, it applies only to romantic desire specifically',
             "Yes — the insight about craving's self-multiplying nature could apply to any object of longing",
             'The poem restricts its scope explicitly',
             'The question does not apply',
         ],
         "correct": 1,
         "expl": "The verse's insight concerns the structure of craving generally, not anything specific to its particular object."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'At Sāketa',
             'Dissatisfaction',
             'Queen Sweetheart (Mudulakkhaṇajātaka)',
             'In My Lap',
         ],
         "correct": 2,
         "expl": 'The sixty-sixth poem overall, and the sixth of the Itthivagga.'},
        {"q": "What is the ascetic's own role in this poem's underlying story?",
         "opts": [
             'A judge presiding over a dispute',
             'An unrelated bystander',
             'A passive observer',
             'The one who desires the queen and eventually attains her',
         ],
         "correct": 3,
         "expl": "His own experience of unsatisfied craving after apparent success is the poem's whole subject."},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The sixth poem of the Itthivagga, following Ja 61 through Ja 65',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'Part of the same ten-poem Itthivagga.'},
        {"q": 'What general teaching about craving does this poem illustrate, familiar from Buddhist doctrine broadly?',
         "opts": [
             'That craving is satisfied once its object is obtained',
             'That craving does not resolve through satisfaction but tends to multiply',
             'That craving has no relationship to suffering',
             'That craving only affects certain people',
         ],
         "correct": 1,
         "expl": "A core observation about the nature of desire itself, illustrated through one man's specific experience."},
        {"q": "What time span does the verse's contrast span?",
         "opts": [
             'No time span is indicated',
             'A single moment only',
             'Before and after winning the queen he desired',
             'An entire lifetime in detail',
         ],
         "correct": 2,
         "expl": "The verse's own before-and-after structure delivering its insight about craving."},
    ],
    marginalia=[
        ("One wish, then many", [
            "before winning her, only a single desire —",
            "afterward, wish upon wish, endlessly born"
        ]),
        ("Not about her, but about wanting itself", [
            "the queen is incidental to the real point —",
            "craving multiplies, whatever its object"
        ]),
        ("Satisfaction that never actually satisfies", [
            "getting exactly what he wished for —",
            "and finding the wanting only grows"
        ]),
        ("A shift within a difficult chapter", [
            "not another verse about women's nature —",
            "a universal observation about desire"
        ]),
    ],
    further=[
        '<a href="%s/ja66/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-65.html">Ja 65 &mdash; Dissatisfaction</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-67.html">Ja 67 &mdash; In My Lap</a> &mdash; '
        "the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 67 — Ucchaṅga (In My Lap)
# --------------------------------------------------------------------------- #
page(
    67, "Uccha&#7749;ga", "In My Lap",
    meta_title="Ja 67 — In My Lap | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 67, closing this chapter's 'women' theme on a "
        "different note — a woman's own shrewd reasoning under an "
        "impossible choice, admired rather than criticized. From "
        "Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A royal court, an impossible choice forced on a "
                    "woman"),
        ("Speaker", "The woman herself, explaining her reasoning to "
                    "the king"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse of admired, clear-headed "
                       "reasoning"),
    ],
    why=(
        "This poem closes out this chapter's run of poems concerning "
        "women on a genuinely different note: rather than voicing a "
        "prejudice against a woman's character, it presents a "
        "woman's own clear, shrewd reasoning under an impossible "
        "forced choice &mdash; reasoning a king finds so persuasive "
        "that he releases everyone involved."),
    guide=[
        ("An impossible choice, and unflinching logic", [
            "The verse gives the woman's own explanation: &lsquo;a "
            "son in my lap, your highness, or a husband while walking "
            "the street &mdash; but I don't see the place from where "
            "I can fetch a brother.&rsquo; Per Sujato's comment, a "
            "king holds a woman's son, husband, and brother captive, "
            "forcing her to choose only one to save. She chooses her "
            "brother, reasoning that a son or husband may, in "
            "principle, be had again, but a brother, once lost, "
            "cannot be replaced."]),
        ("Reasoning admired, not condemned", [
            "The king, per Sujato's comment, is &lsquo;impressed with "
            "her reasoning&rsquo; and releases all three captives "
            "&mdash; a clear reversal of this chapter's earlier "
            "pattern. Here a woman's own careful, unsentimental logic "
            "under genuine duress is precisely what the story "
            "celebrates, closing this chapter's run of poems "
            "concerning women with real admiration rather than "
            "suspicion."]),
        ("A frank note on the verse's own opening image", [
            "Sujato's comment notes directly that &lsquo;ucchaṅge&rsquo; "
            "(&lsquo;lap&rsquo;) carries a sexual innuendo in this "
            "context, likened by the traditional commentary to a "
            "&lsquo;bag&rsquo; in which vegetables are kept &mdash; "
            "the woman's own opening line making a frank, practical "
            "point about how easily a son or husband might be "
            "acquired again, before her reasoning turns to what "
            "genuinely cannot be replaced."]),
    ],
    terms=[
        ("ucchaṅge",
         "&ldquo;in my lap&rdquo;, per Sujato's comment carrying a "
         "sexual innuendo, giving this poem its traditional title."),
        ("sodariyaṁ ānaye",
         "&ldquo;fetch a brother&rdquo; &mdash; the impossibility at "
         "the center of the woman's reasoning, since a brother, "
         "unlike a son or husband, cannot be replaced."),
        ("Ucchaṅgajātaka",
         "the traditional title of this tale, &lsquo;In My "
         "Lap&rsquo;."),
        ("the king",
         "per Sujato's comment, the one who forces this impossible "
         "choice, then releases all three captives once persuaded by "
         "her reasoning."),
        ("reasoning admired",
         "the outcome this reading guide highlights: a woman's own "
         "clear-headed logic under duress, presented for genuine "
         "admiration rather than suspicion, closing this chapter's "
         "run of poems concerning women."),
    ],
    text_intro=(
        "The text in full: a single verse. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja67:1.1-1.4"),
    ],
    quiz=[
        {"q": "What impossible choice does the king force on the woman, per Sujato's comment?",
         "opts": [
             'No specific choice is described',
             'To choose between two kingdoms',
             'To choose which of her son, husband, or brother to save, since he holds all three captive',
             'To choose her own punishment',
         ],
         "correct": 2,
         "expl": 'Setting up her carefully reasoned response.'},
        {"q": 'Which family member does she choose to save?',
         "opts": [
             'Her husband',
             'She refuses to choose',
             'Her son',
             'Her brother',
         ],
         "correct": 3,
         "expl": 'Reasoning that a son or husband may, in principle, be had again, but a brother cannot be replaced.'},
        {"q": "How does the king respond to her reasoning, per Sujato's comment?",
         "opts": [
             'He is impressed and releases all three captives',
             'He releases only her brother',
             'He dismisses her reasoning entirely',
             'He punishes her regardless',
         ],
         "correct": 0,
         "expl": "A clear reversal of this chapter's earlier pattern of suspicion toward women."},
        {"q": "How does this poem's treatment of a woman's reasoning differ from several earlier poems in this chapter?",
         "opts": [
             'It is identical in its suspicion',
             'It presents her clear-headed logic with genuine admiration rather than suspicion',
             'It ignores her perspective entirely',
             'It criticizes her reasoning as flawed',
         ],
         "correct": 1,
         "expl": "Closing this chapter's run of poems concerning women on a notably different note."},
        {"q": "What does Sujato's comment say about the word 'ucchaṅge' (lap) in this context?",
         "opts": [
             'It is a term of formal address',
             'It has no particular connotation',
             "It carries a sexual innuendo, likened by the traditional commentary to a 'bag' for keeping vegetables",
             'It refers only to a physical location with no further meaning',
         ],
         "correct": 2,
         "expl": 'A frank note on the practical point her opening line makes.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'At Sāketa',
             'Vomited Poison',
             'Queen Sweetheart',
             'In My Lap (Ucchaṅgajātaka)',
         ],
         "correct": 3,
         "expl": 'The sixty-seventh poem overall, and the seventh of the Itthivagga.'},
        {"q": 'Why, in her own reasoning, is a brother irreplaceable while a son or husband are not?',
         "opts": [
             'Because a son could be conceived again and a husband found again, but once parents are gone, no new brother can be had',
             'The verse gives no explanation for this distinction',
             'Because of a specific religious rule',
             'Because brothers are more valuable in general',
         ],
         "correct": 0,
         "expl": 'A frank, practical distinction rather than a sentimental one.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'It stands outside any chapter',
             'The seventh poem of the Itthivagga, following Ja 61 through Ja 66',
             'The final poem of its chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": "Part of the same ten-poem Itthivagga, and per Sujato's own comment on the next poem, the last of this chapter's poems actually concerning women."},
        {"q": "What genre convention does this poem follow, involving a ruler testing a subject's wisdom?",
         "opts": [
             'A battle narrative',
             'No such convention is present',
             "A wise-judgment story, where a ruler tests and then rewards someone's clear reasoning under pressure",
             'A romance narrative',
         ],
         "correct": 2,
         "expl": "The king's own admiration and release of all three captives confirms this pattern."},
        {"q": "What does this poem's placement, closing this chapter's 'women' theme, suggest about the chapter's overall range?",
         "opts": [
             'That this poem is a later, unrelated addition',
             'That no variation exists at all',
             'That the chapter is uniformly hostile throughout',
             "That the chapter's difficult content is not monolithic — including at least one poem presenting a woman's wisdom with genuine admiration",
         ],
         "correct": 3,
         "expl": "Worth noting honestly alongside the chapter's more troubling earlier poems."},
    ],
    marginalia=[
        ("An impossible choice, met with clear logic", [
            "son, husband, or brother — choose only one —",
            "her reasoning cuts straight to what can't be replaced"
        ]),
        ("A king persuaded, not just obeyed", [
            "impressed enough to release all three —",
            "reasoning rewarded, not merely permitted"
        ]),
        ("A frank opening line, plainly noted", [
            "'lap' carrying its own innuendo —",
            "Sujato's comment names it directly"
        ]),
        ("A different note, closing this theme", [
            "not suspicion this time, but admiration —",
            "this chapter's range is wider than its worst poems"
        ]),
    ],
    further=[
        '<a href="%s/ja67/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-66.html">Ja 66 &mdash; Queen Sweetheart</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="ja-68.html">Ja 68 &mdash; At Sāketa</a> &mdash; '
        "the next poem, where this chapter's remaining poems shift "
        "away from the theme of women entirely.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 68 — Sāketa (At Sāketa)
# --------------------------------------------------------------------------- #
page(
    68, "S&amacr;keta", "At Sāketa",
    meta_title="Ja 68 — At Sāketa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 68 — an old couple's instinctive trust in the Buddha, "
        "confirmed as their own son across many past lives; the first "
        "of this chapter's remaining poems unrelated to its 'women' "
        "theme. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 8 of 10",
    glance=[
        ("Setting", "The town of Sāketa, an elderly couple meeting "
                    "the Buddha"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse on instinctive, well-founded "
                       "trust"),
    ],
    why=(
        "Sujato's comment states directly that &lsquo;the remaining "
        "stories of this chapter do not concern women&rsquo; &mdash; "
        "this poem marks that shift, and is unusual in its own right: "
        "a story set entirely in the present, confirming an "
        "instinctive bond that turns out to be rooted in many past "
        "lives together."),
    guide=[
        ("Trust that settles on someone never met before", [
            "The verse states its principle: &lsquo;in whom the mind "
            "settles, and the heart too is confident &mdash; gladly "
            "one would trust in that man not seen before.&rsquo; Per "
            "Sujato's comment, this poem concerns only present-day "
            "events, with no proper past-life story behind it: an old "
            "couple dote on the Buddha as though he were their own "
            "son, and he confirms directly that they were, in fact, "
            "his parents across many past lives."]),
        ("A shift away from this chapter's earlier theme", [
            "Sujato's comment states plainly: &lsquo;the remaining "
            "stories of this chapter do not concern women.&rsquo; "
            "Despite belonging to the Itthivagga by its position in "
            "the traditional numbering, this poem and the two that "
            "follow it turn to entirely different subjects, closing "
            "out the chapter on themes unrelated to the difficult "
            "material found in its opening poems."]),
    ],
    terms=[
        ("mano nivisati",
         "&ldquo;the mind settles&rdquo; &mdash; the verse's own "
         "description of instinctive trust, not built on prior "
         "acquaintance."),
        ("adiṭṭhapubbake pose",
         "&ldquo;that man not seen before&rdquo; &mdash; the "
         "stranger the verse says can nonetheless be trusted, when "
         "the mind and heart both settle."),
        ("Sāketajātaka",
         "the traditional title of this tale, &lsquo;At "
         "Sāketa&rsquo;, named for the town where the events take "
         "place."),
        ("no proper story",
         "per Sujato's comment, this poem's own unusual status: it "
         "concerns only present-day events, with no separate "
         "past-life narrative of the kind most other tales in this "
         "collection are built around."),
        ("the remaining stories of this chapter",
         "per Sujato's comment, this poem and the two that follow "
         "it, which do not concern the theme of women found in this "
         "chapter's opening poems."),
    ],
    text_intro=(
        "The text in full: a single verse, marking a shift to themes "
        "unrelated to this chapter's earlier poems, discussed above. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja68:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Sujato's comment say directly about this poem and the two that follow it?",
         "opts": [
             'That they were later additions with no comment available',
             'That they repeat earlier poems exactly',
             "That they continue the chapter's earlier theme",
             "That 'the remaining stories of this chapter do not concern women'",
         ],
         "correct": 3,
         "expl": "Marking a clear shift away from this chapter's opening poems."},
        {"q": "What is unusual about this poem's underlying story, per the comment?",
         "opts": [
             "It has 'no proper story' — it concerns only present-day events, unlike most Jātaka tales",
             'It has multiple past-life narratives',
             'No story exists for this poem at all',
             'It has an unusually long past-life narrative',
         ],
         "correct": 0,
         "expl": 'A distinctive structural feature compared to most other tales in this collection.'},
        {"q": "What happens in this poem's present-day events, per Sujato's comment?",
         "opts": [
             'A dispute between merchants',
             'An old couple dotes on the Buddha as their own son, which he confirms across many past lives',
             'A battle between two kingdoms',
             'A trial before a king',
         ],
         "correct": 1,
         "expl": 'Confirming an instinctive bond rooted in a long history together.'},
        {"q": 'What principle does the verse itself state?',
         "opts": [
             'No principle is stated',
             'That trust should never be given to strangers',
             'That when the mind settles and the heart is confident, one may gladly trust even someone not seen before',
             'That trust must always be earned over time',
         ],
         "correct": 2,
         "expl": 'An instinctive form of trust the story then grounds in a much deeper history.'},
        {"q": 'Where is this poem set, giving it its traditional title?',
         "opts": [
             'Rājagaha',
             'No location is specified',
             'Varanasi',
             'Sāketa',
         ],
         "correct": 3,
         "expl": "'At Sāketa' — named for the town where the events take place."},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'At Sāketa (Sāketajātaka)',
             'Vomited Poison',
             'The Spade',
             'In My Lap',
         ],
         "correct": 0,
         "expl": 'The sixty-eighth poem overall, and the eighth of the Itthivagga.'},
        {"q": 'How does this poem relate to the Buddha specifically, unlike most Jātaka tales?',
         "opts": [
             'It has no connection to the Buddha',
             'The Buddha himself appears directly in the present-day frame and confirms the past-life relationship',
             'It only concerns his distant ancestors',
             "It predates the Buddha's own lifetime entirely",
         ],
         "correct": 1,
         "expl": 'A direct present-day confirmation rather than a purely past-life narrative.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of a later chapter',
             'It stands outside any chapter',
             'The eighth poem of the Itthivagga, following Ja 61 through Ja 67',
             'The final poem of its chapter',
         ],
         "correct": 2,
         "expl": 'Part of the same ten-poem Itthivagga, despite its unrelated subject matter.'},
        {"q": "Why does this poem remain classified within the 'Itthivagga' despite not concerning women?",
         "opts": [
             'It was misclassified by a later editor and should be moved',
             'The question is not addressed',
             'This reading guide asserts a hidden connection to the theme',
             'Its position in the traditional numbering places it in this chapter regardless of its actual subject matter',
         ],
         "correct": 3,
         "expl": "Noted plainly rather than forcing an artificial connection to the chapter's title theme."},
        {"q": 'What quality does the trust described in this verse depend on?',
         "opts": [
             'An instinctive settling of the mind and confidence of heart, even toward someone not seen before',
             'A formal introduction',
             'Financial obligation',
             'Prior long acquaintance',
         ],
         "correct": 0,
         "expl": 'Later revealed by the story to be grounded in a far deeper history than either party consciously knew.'},
    ],
    marginalia=[
        ("A stranger who feels instantly familiar", [
            "the mind settles before any explanation is given —",
            "trust that arrives before understanding does"
        ]),
        ("A story with no story", [
            "unusual among these tales: no separate past-life narrative —",
            "just present-day events, confirmed directly"
        ]),
        ("An old couple's son, confirmed by the Buddha himself", [
            "not a metaphor, but many actual past lives —",
            "instinct grounded in real history"
        ]),
        ("Where this chapter turns elsewhere", [
            "'the remaining stories do not concern women' —",
            "Sujato's comment marks the shift plainly"
        ]),
    ],
    further=[
        '<a href="%s/ja68/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-67.html">Ja 67 &mdash; In My Lap</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-69.html">Ja 69 &mdash; Vomited Poison</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 69 — Visavanta (Vomited Poison)
# --------------------------------------------------------------------------- #
page(
    69, "Visavanta", "Vomited Poison",
    meta_title="Ja 69 — Vomited Poison | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 69 — a snake who refuses, even under threat of death, "
        "to take back the poison it has already given up, and a "
        "genuine ambiguity in how the verse should even be read. "
        "From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "A snake, addressing its own discarded poison"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; a case where the verse's grammar "
                       "supports two different readings"),
    ],
    why=(
        "This poem's snake makes an absolute commitment: having given "
        "up its poison once, it will not take it back, even under "
        "threat of death &mdash; but Sujato's own comment reveals the "
        "Pali grammar genuinely supports two different readings of "
        "just how firm that refusal actually is."),
    guide=[
        ("Death preferred to reclaiming what was given up", [
            "The verse gives the snake's own resolve: &lsquo;curse "
            "that vomited poison, which I vomited for the sake of "
            "life, and now shall consume again. Death is better for "
            "me than life!&rsquo; Per Sujato's comment, a snake "
            "refuses to take back its own poison even on pain of "
            "death."]),
        ("A genuine grammatical fork in how to read the refusal", [
            "Sujato's comment identifies real ambiguity here: the "
            "story assumes the snake simply refuses to take the "
            "poison back, but the verse itself contains no negative "
            "particle qualifying the verb, so it could instead be "
            "read as a rhetorical question &mdash; &lsquo;I shall "
            "take back what I have vomited?&rsquo; &mdash; implying "
            "the snake is horrified at even having to ask, rather "
            "than flatly stating a refusal. Under either reading, "
            "the snake's underlying commitment to what it has already "
            "relinquished remains absolute, but the grammar leaves "
            "genuinely open exactly how that commitment is voiced."]),
    ],
    terms=[
        ("visaṁ vantaṁ",
         "&ldquo;vomited poison&rdquo; &mdash; the discarded poison "
         "the snake refuses to reclaim, giving this poem its "
         "traditional title."),
        ("mataṁ me jīvitā varaṁ",
         "&ldquo;death is better for me than life!&rdquo; &mdash; "
         "the snake's own absolute statement of commitment."),
        ("rhetorical question",
         "per Sujato's comment, one of two genuinely possible "
         "grammatical readings of the verse's central line, since no "
         "negative particle qualifies the verb."),
        ("Visavantajātaka",
         "the traditional title of this tale, &lsquo;Vomited "
         "Poison&rsquo;."),
        ("jīvitakāraṇā",
         "&ldquo;for the sake of life&rdquo;, a phrase Sujato's "
         "comment cross-references to Ps 1.1, outside this site's own "
         "selections."),
    ],
    text_intro=(
        "The text in full: a single verse, whose central line "
        "Sujato's own comment identifies as genuinely ambiguous in "
        "its grammar, discussed above. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja69:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the snake refuse to do, per Sujato's comment?",
         "opts": [
             'Take back its own poison, even on pain of death',
             'Leave its territory',
             'Speak to anyone else',
             'Attack anyone further',
         ],
         "correct": 0,
         "expl": 'An absolute commitment to what it has already given up.'},
        {"q": "What grammatical detail does Sujato's comment identify in the verse's central line?",
         "opts": [
             'No ambiguity exists',
             'There is no negative particle qualifying the verb, so it could be a flat refusal or a rhetorical question',
             'The line is grammatically incomplete',
             'The verb is in an unusual tense with no clear meaning',
         ],
         "correct": 1,
         "expl": "A genuine fork in how the verse's central line should actually be read."},
        {"q": "What are the two readings Sujato's comment identifies?",
         "opts": [
             'Only one reading is actually possible',
             'Two completely unrelated meanings',
             'A flat refusal to take the poison back, or a rhetorical question expressing horror at even being asked',
             'A statement about food and a statement about weather',
         ],
         "correct": 2,
         "expl": 'Under either reading, the underlying commitment remains absolute.'},
        {"q": 'What does the snake say about death compared to life in this situation?',
         "opts": [
             'That neither matters to it',
             'No comparison is made',
             'That life is always preferable',
             'That death is better for it than reclaiming the poison and living',
         ],
         "correct": 3,
         "expl": "The verse's own absolute closing statement."},
        {"q": "What external text does Sujato's comment cross-reference for the phrase 'jīvitakāraṇā'?",
         "opts": [
             "Ps 1.1, outside this site's own selections",
             'AN 5.230',
             'No external text is cited',
             'The Dhammapada',
         ],
         "correct": 0,
         "expl": 'Noted for completeness without a linked page.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'At Sāketa',
             'Vomited Poison (Visavantajātaka)',
             'The Spade',
             'In My Lap',
         ],
         "correct": 1,
         "expl": 'The sixty-ninth poem overall, and the ninth of the Itthivagga.'},
        {"q": "Does this poem concern the theme of women found in this chapter's opening poems?",
         "opts": [
             'The question is not addressed',
             'Yes, directly',
             "No — per Sujato's comment on Ja 68, this is one of the chapter's remaining poems on an unrelated theme",
             'Only indirectly through allegory',
         ],
         "correct": 2,
         "expl": "Continuing the shift away from this chapter's opening subject matter."},
        {"q": "What broader principle does this poem's snake illustrate?",
         "opts": [
             'That poison should always be reclaimed if possible',
             'No general principle is illustrated',
             'That commitments should be easily reversed under pressure',
             'Unwavering commitment to a decision already made, even under threat of death',
         ],
         "correct": 3,
         "expl": 'A vivid, absolute image for holding firm to a relinquished harm.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The ninth poem of the Itthivagga, following Ja 61 through Ja 68',
             'The final poem of its chapter',
             'The first poem of a later chapter',
             'It stands outside any chapter',
         ],
         "correct": 0,
         "expl": 'The second-to-last poem of this ten-poem chapter.'},
        {"q": "Under either of the two possible grammatical readings, does the snake's underlying position change?",
         "opts": [
             'Yes, the two readings imply opposite positions',
             'No — under either reading, its commitment to not reclaiming the poison remains absolute',
             "The readings are unrelated to the snake's position",
             'Only one reading involves the snake at all',
         ],
         "correct": 1,
         "expl": 'The ambiguity concerns how the commitment is voiced, not whether it holds.'},
    ],
    marginalia=[
        ("Poison, once given up, refused again", [
            "even death preferred to taking it back —",
            "an absolute line, once crossed, not recrossed"
        ]),
        ("A question, or a refusal?", [
            "the grammar itself won't settle it —",
            "Sujato names both readings honestly"
        ]),
        ("Either way, the same resolve", [
            "flat statement or rhetorical horror —",
            "the commitment holds regardless"
        ]),
        ("A theme already left behind", [
            "no women in this poem's story at all —",
            "the chapter's later poems turn elsewhere"
        ]),
    ],
    further=[
        '<a href="%s/ja69/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="ja-68.html">Ja 68 &mdash; At Sāketa</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="ja-70.html">Ja 70 &mdash; The Spade</a> &mdash; '
        "the next poem, closing this chapter.",
        '<a href="./">Jataka</a> &mdash; back to the collection index.',
    ],
)

# --------------------------------------------------------------------------- #
# Ja 70 — Kuddāla (The Spade)
# --------------------------------------------------------------------------- #
page(
    70, "Kudd&amacr;la", "The Spade",
    meta_title="Ja 70 — The Spade | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jātaka 70, closing the Itthivagga — a gardener-turned-ascetic "
        "who can't stop thinking about his favorite spade, and a "
        "verse on what makes a victory permanent, echoed at this "
        "site's own Dhammapada. From Ru-Yi Meditation Center."),
    vagga="Book of the Ones &middot; Chapter Seven (Itthivagga) &middot; Poem 10 of 10 (closing the chapter)",
    glance=[
        ("Setting", "No narrative scene in the canonical verse itself"),
        ("Speaker", "Unspecified in the canonical verse itself"),
        ("Form", "One four-line stanza"),
        ("Length", "Under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "one short verse on what makes a victory last"),
    ],
    why=(
        "This poem closes the Itthivagga on a note wholly unrelated "
        "to its opening theme &mdash; a small, almost comic attachment "
        "(a gardener-turned-ascetic who can't stop thinking about his "
        "favorite spade) used to make a serious point about the "
        "difference between a victory that holds and one that "
        "doesn't, echoed nearly word for word at this site's own "
        "Dhammapada."),
    guide=[
        ("An ascetic who can't quite let go of one small thing", [
            "Per Sujato's comment, a gardener goes forth as an "
            "ascetic, but cannot stop thinking about his favorite "
            "spade &mdash; a small, ordinary attachment standing in "
            "for the larger, harder-to-notice ones renunciation is "
            "actually meant to address."]),
        ("What separates a real victory from a temporary one", [
            "The verse delivers its teaching directly: &lsquo;that "
            "victory is not a good victory which may be undone. That "
            "victory is a good victory which may not be undone.&rsquo; "
            "Applied to the gardener's own small case, giving up "
            "possessions or habits only outwardly, while still "
            "quietly attached within, is not yet the kind of victory "
            "that holds."]),
        ("A near-identical teaching already on this site, and closing this chapter", [
            "Sujato's comment compares this verse directly to this "
            "site's own already-completed Dhp 179, in the Buddhas "
            "chapter of the Dhammapada &mdash; the same underlying "
            "concern with permanence versus reversal appearing in two "
            "different collections. This poem closes the Itthivagga, "
            "the seventh of eight chapters this site's selection "
            "draws from within the Ekakanipāta. The source text's own "
            "untranslated summary verse (uddāna) immediately follows, "
            "naming all ten poems of this chapter in sequence "
            "&mdash; not presented here as quoted text, since it "
            "carries no separate translation, but noted for "
            "completeness, as at the close of the previous six "
            "chapters."]),
    ],
    terms=[
        ("na taṁ jitaṁ sādhu jitaṁ",
         "&ldquo;that victory is not a good victory&rdquo; &mdash; "
         "the verse's opening half of its central contrast."),
        ("yaṁ jitaṁ nāvajīyati",
         "&ldquo;which may not be undone&rdquo; &mdash; the "
         "defining quality of a genuine, lasting victory."),
        ("Kuddāla",
         "&ldquo;spade&rdquo; &mdash; the small object of the "
         "gardener's lingering attachment, giving this poem its "
         "traditional title."),
        ("Kuddālajātaka",
         "the traditional title of this tale, &lsquo;The "
         "Spade&rsquo;, closing the Itthivagga."),
        ("Dhp 179",
         "the already-completed page on this site, in the Buddhas "
         "chapter of the Dhammapada, that Sujato's comment compares "
         "directly to this verse."),
    ],
    text_intro=(
        "The text in full: a single verse, echoed nearly word for "
        "word at this site's own Dhp 179. The chapter's own "
        "untranslated closing summary verse (uddāna), which follows "
        "immediately in the source text, is not quoted here since it "
        "carries no English translation, but its content &mdash; the "
        "ten poem titles of this chapter in sequence &mdash; matches "
        "this reading guide's own further reading list below. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "ja70:1.1-1.4"),
    ],
    quiz=[
        {"q": "What can't the gardener-turned-ascetic stop thinking about, per Sujato's comment?",
         "opts": [
             'His former house',
             'His favorite spade',
             'A former friend',
             'His previous income',
         ],
         "correct": 1,
         "expl": 'A small, ordinary attachment standing in for larger, harder-to-notice ones.'},
        {"q": 'What distinction does the verse draw between two kinds of victory?',
         "opts": [
             'No distinction is drawn',
             'Victories won by force versus by negotiation',
             'A victory that may be undone versus one that may not be undone',
             'Public versus private victories',
         ],
         "correct": 2,
         "expl": 'Only the second kind counts, per the verse, as a genuinely good victory.'},
        {"q": "What already-completed page on this site does Sujato's comment compare this verse to?",
         "opts": [
             'Snp 3.12',
             'No comparison is made',
             'AN 5.230',
             'Dhp 179, in the Buddhas chapter of the Dhammapada',
         ],
         "correct": 3,
         "expl": 'The same underlying concern with permanence versus reversal, appearing in two different collections.'},
        {"q": "How does the gardener's attachment to his spade relate to the verse's teaching about victory?",
         "opts": [
             'Outwardly giving up possessions while remaining quietly attached within is not yet the kind of victory that holds',
             'The spade represents a literal battle he must win',
             'The connection is left entirely unexplained',
             'It has no relationship at all',
         ],
         "correct": 0,
         "expl": 'A small, almost comic case illustrating a serious point about incomplete renunciation.'},
        {"q": 'What chapter does this poem close?',
         "opts": [
             'The Āsīsavagga',
             "The Itthivagga, the seventh of eight chapters this site's selection draws from",
             'The final chapter of the whole Jātaka',
             'It does not close a chapter',
         ],
         "correct": 1,
         "expl": "The source text's own untranslated summary verse (uddāna) follows immediately after."},
        {"q": "Is the chapter's closing summary verse (uddāna) presented as quoted text in this reading guide?",
         "opts": [
             'It is presented as spoken by the gardener',
             'Yes, quoted in full',
             'No — it carries no separate English translation, so it is only noted for completeness',
             'It does not exist for this chapter',
         ],
         "correct": 2,
         "expl": 'Consistent with the same practice at the close of the previous six chapters.'},
        {"q": "What is this poem's traditional title?",
         "opts": [
             'At Sāketa',
             'In My Lap',
             'Vomited Poison',
             'The Spade (Kuddālajātaka)',
         ],
         "correct": 3,
         "expl": 'The seventieth poem overall, and the tenth and final poem of the Itthivagga.'},
        {"q": "What was the gardener's profession before becoming an ascetic?",
         "opts": [
             'A gardener',
             'A soldier',
             'A scribe',
             'A merchant',
         ],
         "correct": 0,
         "expl": 'Explaining his particular, occupation-specific attachment to a spade.'},
        {"q": "Where does this poem sit in the collection's own chapter structure?",
         "opts": [
             'The first poem of the Itthivagga',
             'The tenth and final poem of the Itthivagga, closing this chapter',
             'It stands outside any chapter',
             'The first poem of a later chapter',
         ],
         "correct": 1,
         "expl": "Its closing position is directly confirmed by the chapter's own summary verse following immediately after."},
        {"q": "How does this poem's subject matter relate to this chapter's opening poems on women?",
         "opts": [
             'It explicitly criticizes the earlier poems',
             'It directly continues that same theme',
             'It is entirely unrelated, part of the shift away from that theme beginning at Ja 68',
             'It retells the same story from a different angle',
         ],
         "correct": 2,
         "expl": 'Closing the Itthivagga on a note wholly unrelated to its difficult opening content.'},
    ],
    marginalia=[
        ("A spade that won't stay let go of", [
            "renunciation, outwardly complete —",
            "but the mind keeps circling back to one small tool"
        ]),
        ("Two kinds of victory, only one that lasts", [
            "undone, or truly won — the verse draws the line —",
            "outward giving-up isn't always the real thing"
        ]),
        ("The same teaching, echoed elsewhere on this site", [
            "Dhp 179 makes nearly the same point —",
            "permanence, not appearance, is what counts"
        ]),
        ("Ten poems, one chapter closed", [
            "the Itthivagga's own summary follows —",
            "not quoted, since it has no translation"
        ]),
    ],
    further=[
        '<a href="%s/ja70/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../dhammapada/dhp-14.html">Dhammapada Chapter 14 '
        "&mdash; The Buddhas</a> &mdash; containing Dhp 179, "
        "compared directly to this verse in Sujato's own comment.",
        '<a href="ja-69.html">Ja 69 &mdash; Vomited Poison</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="./">Jataka</a> &mdash; back to the collection '
        "index.",
    ],
)
