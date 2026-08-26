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
