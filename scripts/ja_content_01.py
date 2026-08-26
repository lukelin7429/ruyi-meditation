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
