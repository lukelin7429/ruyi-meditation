# -*- coding: utf-8 -*-
"""Therigatha — Verses of the Senior Nuns. Organized into books by the
number of verses attributed to each elder (Book of the Ones, Twos...)."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Therigatha — Verses of the Senior Nuns"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Therigatha selections")
TAIL = ("./", "Therigatha selections")
INDEX_EXTRA = []

PAGES = []


def page(book, num, pali, title, **kw):
    """Shared scaffolding for a single elder's verses in the Therigatha.

    Same two-level addressing as thag_content_01.py's page() -- see that
    file's docstring for the rationale.
    """
    d = {
        "slug": "thig-%d.%d" % (book, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "thig%d.%d" % (book, num),
        "crumb": "Thig %d.%d" % (book, num),
        "number_line": "Therigatha &middot; %d.%d" % (book, num),
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# Thig 1.1 — An Unnamed Nun
# --------------------------------------------------------------------------- #
page(
    1, 1, "An&ntilde;atara&#7749; Ther&imacr;", "An Unnamed Nun",
    meta_title="Thig 1.1 — An Unnamed Nun | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Therigatha's opening poem, an anonymous nun's tender address to herself "
        "at peace. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 1 of 18",
    glance=[
        ("Setting", "No narrative setting; a short verse with a one-line "
                    "attribution naming no individual"),
        ("Speaker", "An unnamed nun, addressing herself in the second person"),
        ("Form", "A homage line, one four-line verse, and a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; four lines, "
                       "opening a collection of seventy-three"),
    ],
    why=(
        "The Therigatha (&ldquo;Verses of the Senior Nuns&rdquo;) opens not with "
        "a named, celebrated figure but with an anonymous voice: a nun addressing "
        "herself tenderly, in the second person, as she settles into a peace "
        "compared to vegetables boiled down until nothing remains but stillness. "
        "It is one of seventy-three poems in this collection, attributed to "
        "enlightened women of the earliest generation of Buddhist nuns &mdash; "
        "among the oldest surviving spiritual autobiography by women anywhere in "
        "world literature."),
    guide=[
        ("A collection of seventy-three poems, organized by length", [
            "The Therigatha gathers seventy-three poems into &lsquo;books&rsquo; "
            "grouped by how many verses tradition attributes to each poet: a Book "
            "of the Ones for single-verse poems, a Book of the Twos, and onward, "
            "growing steadily longer, up to the Great Book &mdash; a single very "
            "long poem attributed to the nun Sumedhā that closes the entire "
            "collection."]),
        ("Not past-life stories, but this life", [
            "Unlike the Cariyapitaka, which recounts the Buddha's own past lives, "
            "every poem in the Therigatha concerns the speaker's present life: the "
            "hardship or insight that led her to renounce the household, the "
            "struggle of training, and, for many poems, the moment of her own "
            "awakening, stated directly."]),
        ("Two voices, not always distinguishable at a glance", [
            "Some Therigatha poems are addressed to a nun by someone else, often "
            "the Buddha, in the second person, encouraging her while she is still "
            "training. Others are spoken by a nun in the first person, often "
            "describing an awakening already achieved. This first poem uses the "
            "second-person form, but the attribution names no outside speaker "
            "&mdash; it is the nun herself, addressing herself as &lsquo;little "
            "nun&rsquo;."]),
        ("Beginning with no name at all", [
            "Before any of the collection's many named women appear, its first "
            "voice is anonymous. The image itself is domestic and exact: desire "
            "&lsquo;quelled, like vegetables boiled dry in a pot&rsquo; &mdash; "
            "craving not violently extinguished but simply, gradually, boiled away "
            "to nothing."]),
    ],
    terms=[
        ("therī",
         "&ldquo;senior nun&rdquo; or &ldquo;elder nun&rdquo; &mdash; the "
         "collection's own title, applied to the enlightened women whose verses "
         "it gathers."),
        ("gāthā",
         "&ldquo;verse&rdquo; &mdash; the second half of this collection's title, "
         "naming the form every one of its seventy-three poems takes."),
        ("yoga",
         "&ldquo;yoke&rdquo; &mdash; a recurring image across this collection for "
         "the ties, especially craving, binding a person to further rebirth."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; or &ldquo;quenching&rdquo; &mdash; not "
         "named directly in this poem, but the state its central image of "
         "boiled-dry vegetables describes without naming."),
        ("&lsquo;that is how this verse was recited by&rsquo;",
         "a closing attribution formula appearing after some of this book's "
         "shortest poems, naming who spoke the preceding verse and under what "
         "circumstance &mdash; present here, though for an unnamed speaker."),
    ],
    text_intro=(
        "The text in full: a homage line, then the verse itself, with its "
        "closing attribution. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", ["thig1.1:1.0"]),
        ("p", "&sect;2", "thig1.1:1.1-1.4"),
        ("p", "&sect;3", "thig1.1:2.1-2.1"),
    ],
    quiz=[
        {"q": "Who speaks this poem, according to its own attribution?",
         "opts": [
             "The Buddha, addressing a named nun",
             "An unnamed nun, addressing herself",
             "A group of nuns speaking in unison",
             "No attribution is given at all"],
         "correct": 1,
         "expl": "The collection's first voice is anonymous."},
        {"q": "How does the Therigatha organize its seventy-three poems?",
         "opts": [
             "Alphabetically by the poet's name",
             "Into books grouped by how many verses are attributed to each poet",
             "By the geographic region each poet lived in",
             "Randomly, with no organizing principle"],
         "correct": 1,
         "expl": "From the Book of the Ones through to the Great Book."},
        {"q": "How does the Therigatha differ from the Cariyapitaka in subject matter?",
         "opts": [
             "They cover identical subject matter",
             "The Cariyapitaka recounts past lives; the Therigatha concerns the speaker's present life",
             "The Therigatha is entirely in prose",
             "The Cariyapitaka is about nuns, the Therigatha about kings"],
         "correct": 1,
         "expl": "Hardship, training, and often the moment of awakening, all in this one life."},
        {"q": "What two kinds of speaker appear across the Therigatha's poems?",
         "opts": [
             "Only nuns speaking about other nuns",
             "Someone (often the Buddha) addressing a still-training nun, or a nun speaking in her own voice",
             "Only kings and queens",
             "Only anonymous group narrators"],
         "correct": 1,
         "expl": "Not always distinguishable at a glance without checking the attribution."},
        {"q": "What image does this poem use to describe the speaker's quelled desire?",
         "opts": [
             "A river running dry",
             "Vegetables boiled dry in a pot",
             "A fire doused with water",
             "A flower wilting in the sun"],
         "correct": 1,
         "expl": "Craving not violently extinguished, but gradually boiled away to nothing."},
        {"q": "What does the speaker call herself in this poem?",
         "opts": [
             "'Great teacher'",
             "'Little nun'",
             "Her own personal name",
             "'Elder'"],
         "correct": 1,
         "expl": "A tender, diminutive self-address."},
        {"q": "What is the traditional final book of the Therigatha, closing the whole collection?",
         "opts": [
             "The Book of the Twos",
             "The Great Book, a single long poem attributed to the nun Sumedhā",
             "The Book of the Ones, where this poem appears",
             "There is no final book; the collection has no fixed order"],
         "correct": 1,
         "expl": "The longest single poem in the entire collection."},
        {"q": "What does 'yoga' mean, as the term is used across this collection?",
         "opts": [
             "A physical practice",
             "'Yoke' — the ties, especially craving, binding a person to further rebirth",
             "A type of verse meter",
             "A monastic robe"],
         "correct": 1,
         "expl": "A recurring image across many Therigatha poems."},
        {"q": "What companion collection, still to come on this site, gathers similar verses attributed to monks?",
         "opts": [
             "The Dhammapada",
             "The Theragatha, 'Verses of the Senior Monks'",
             "The Sutta Nipāta",
             "The Udāna"],
         "correct": 1,
         "expl": "A much larger companion collection, 264 poems."},
        {"q": "What scholarly distinction is often made about the Therigatha as a body of literature?",
         "opts": [
             "It is the shortest text in the Pali canon",
             "It is among the oldest surviving spiritual autobiography by women in world literature",
             "It was composed most recently of all Khuddaka Nikāya texts",
             "It has no distinction beyond being part of the canon"],
         "correct": 1,
         "expl": "A frequently noted point about this collection's historical significance."},
    ],
    marginalia=[
        ("An anonymous first voice", [
            "no name given,",
            "before many follow"
        ]),
        ("A tender self-address", [
            "'sleep softly,",
            "little nun'"
        ]),
        ("Boiled dry, not doused", [
            "desire quelled",
            "gradually, completely"
        ]),
        ("Seventy-three poems", [
            "organized by length,",
            "Ones to the Great Book"
        ]),
    ],
    further=[
        '<a href="%s/thig1.1/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="../cariyapitaka/">Cariyapitaka</a> &mdash; another complete '
        "Khuddaka Nikāya collection on this site, past-life stories rather than "
        "this-life testimony.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.2 — Muttā (1st)
# --------------------------------------------------------------------------- #
page(
    1, 2, "Mutt&amacr;", "Mutt&amacr; (1st)",
    meta_title="Thig 1.2 — Muttā (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Muttā's "
        "verse, a four-line exhortation the Buddha is said to have given a "
        "trainee nun. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 2 of 18",
    glance=[
        ("Setting", "No narrative setting; a short verse with a closing "
                    "attribution naming both speaker and occasion"),
        ("Speaker", "The Buddha, addressing the trainee nun Muttā by name"),
        ("Form", "One four-line verse, with a closing attribution note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short "
                       "exhortation built on a play on the name Muttā"),
    ],
    why=(
        "This poem plays directly on its subject's name: Muttā means "
        "&lsquo;released&rsquo;, and the verse addressed to her opens with "
        "exactly that word as an instruction &mdash; &lsquo;Muttā, be released "
        "from your yokes&rsquo;. Unlike Thig 1.1's self-address, this poem's own "
        "attribution names its speaker directly: the Buddha, giving Muttā this "
        "exhortation &lsquo;regularly&rsquo;, not as a single occasion."),
    guide=[
        ("A name and its meaning, used as instruction", [
            "&lsquo;Muttā&rsquo; is itself the Pali word for &lsquo;released&rsquo; "
            "or &lsquo;freed&rsquo;. The verse opens by addressing her with her own "
            "name used as a direct command &mdash; be what your name already "
            "names."]),
        ("An image of gradual, natural release", [
            "The comparison offered is astronomical and cyclical rather than "
            "violent: &lsquo;like the moon released from the eclipse&rsquo;. An "
            "eclipse passes; the moon was never actually damaged, only "
            "temporarily obscured &mdash; a gentler image for release than a "
            "struggle or a battle."]),
        ("A practical, not just philosophical, close", [
            "The verse ends on something concretely monastic: once the mind is "
            "released, &lsquo;enjoy your alms free of debt&rsquo; &mdash; framing "
            "spiritual freedom in terms a nun's daily life of receiving alms food "
            "would make immediately, practically meaningful."]),
        ("An attribution naming a habit, not a single moment", [
            "Unlike Thig 1.1's anonymous, one-time attribution, this poem's "
            "closing note says the Buddha &lsquo;regularly advised&rsquo; Muttā "
            "with these words &mdash; suggesting an ongoing relationship of "
            "teaching and encouragement, not a single remembered exchange."]),
    ],
    terms=[
        ("Muttā",
         "a nun's name, also the Pali word for &lsquo;released&rsquo; or "
         "&lsquo;freed&rsquo; &mdash; the verse plays directly on this double "
         "meaning."),
        ("yoga",
         "&ldquo;yoke&rdquo; &mdash; the ties Muttā is instructed to be released "
         "from, the same image opening several poems in this book."),
        ("sekha",
         "a &ldquo;trainee&rdquo; &mdash; the stage of practice this poem's "
         "attribution describes Muttā as being in when addressed."),
        ("piṇḍapāta",
         "&ldquo;almsfood&rdquo; &mdash; named directly in the verse's closing "
         "line, the daily practical context the instruction is grounded in."),
        ("cariyā",
         "not used in this text, but worth noting by contrast: unlike the "
         "Cariyapitaka's stories, this poem needs no such word &mdash; its "
         "occasion is ordinary training life, not a dramatic past-life episode."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.2:1.1-1.4"),
        ("p", "&sect;2", "thig1.2:2.1-2.1"),
    ],
    quiz=[
        {"q": "What does the name 'Muttā' mean, and how does the verse use this?",
         "opts": [
             "'Wisdom' — used as a title of respect",
             "'Released' or 'freed' — used as a direct instruction, addressing her by what her name already means",
             "'Moon' — a purely descriptive nickname",
             "The name has no particular meaning"],
         "correct": 1,
         "expl": "A play on the name opening the verse itself."},
        {"q": "What image does the verse use for Muttā's release?",
         "opts": [
             "A bird breaking free of a cage",
             "The moon released from an eclipse",
             "A river bursting a dam",
             "A prisoner escaping a cell"],
         "correct": 1,
         "expl": "A gentle, cyclical image — the moon was never actually damaged, only obscured."},
        {"q": "What practical instruction closes the verse?",
         "opts": [
             "Build a new hermitage",
             "Enjoy your alms free of debt",
             "Travel to a distant city",
             "Teach other nuns immediately"],
         "correct": 1,
         "expl": "Framing spiritual freedom in terms of a nun's daily alms round."},
        {"q": "Who does the closing attribution name as the speaker of this verse?",
         "opts": [
             "An unnamed nun, as in Thig 1.1",
             "The Buddha, addressing Muttā directly",
             "Muttā herself, speaking about her own future",
             "No speaker is named"],
         "correct": 1,
         "expl": "Unlike Thig 1.1's anonymous attribution."},
        {"q": "How does this poem's attribution differ from Thig 1.1's?",
         "opts": [
             "It describes a single, one-time recitation, just like Thig 1.1",
             "It says the Buddha 'regularly advised' Muttā with these words, suggesting an ongoing relationship",
             "It gives no attribution at all",
             "It attributes the verse to a different Buddha"],
         "correct": 1,
         "expl": "An ongoing pattern of teaching, not one remembered exchange."},
        {"q": "What stage of practice does the attribution describe Muttā as being in?",
         "opts": [
             "Already fully awakened",
             "A trainee (sekha)",
             "Not yet ordained",
             "Her stage is not specified"],
         "correct": 1,
         "expl": "Addressed while still in training, unlike some later poems spoken after awakening."},
        {"q": "What does 'yoga' mean, as used in this poem and elsewhere in this book?",
         "opts": [
             "'Yoke' — the ties binding a person to further rebirth",
             "A specific meditation posture",
             "A monastic title",
             "A type of alms bowl"],
         "correct": 0,
         "expl": "The same image recurring across several of this book's poems."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The first poem",
             "The second poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following directly after Thig 1.1's anonymous verse."},
        {"q": "How long is this poem?",
         "opts": [
             "A single four-line verse, with attribution",
             "Twenty verses",
             "A single line only",
             "It has no fixed verse structure"],
         "correct": 0,
         "expl": "One of the shortest forms in this collection, typical of the Book of the Ones."},
        {"q": "What term names 'almsfood', used in this verse's closing line?",
         "opts": [
             "Piṇḍapāta",
             "Nibbāna",
             "Yoga",
             "Sekha"],
         "correct": 0,
         "expl": "Grounding the instruction in ordinary monastic practice."},
    ],
    marginalia=[
        ("A name used as instruction", [
            "'Muttā' means",
            "'released' itself"
        ]),
        ("Freed like the moon", [
            "an eclipse passes,",
            "nothing was damaged"
        ]),
        ("A practical close", [
            "alms enjoyed",
            "'free of debt'"
        ]),
        ("A habit, not one moment", [
            "advised",
            "'regularly'"
        ]),
    ],
    further=[
        '<a href="%s/thig1.2/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.1.html">Thig 1.1 &mdash; An Unnamed Nun</a> &mdash; the '
        "text immediately before this one, opening the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.3 — Puṇṇā
# --------------------------------------------------------------------------- #
page(
    1, 3, "Pu&#7751;&#7751;&amacr;", "Pu&#7751;&#7751;&amacr;",
    meta_title="Thig 1.3 — Puṇṇā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Puṇṇā's "
        "verse, another name-based exhortation comparing spiritual fullness to "
        "the full moon. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 3 of 18",
    glance=[
        ("Setting", "No narrative setting; a short verse with a closing "
                    "attribution"),
        ("Speaker", "The senior nun Puṇṇā herself, according to the "
                    "attribution"),
        ("Form", "One four-line verse, with a closing attribution note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short "
                       "verse, paired closely with Thig 1.2's structure"),
    ],
    why=(
        "This poem repeats Thig 1.2's basic pattern &mdash; a name used as its "
        "own instruction, paired with a lunar image &mdash; but with a telling "
        "difference in attribution: where Muttā's verse is credited to the "
        "Buddha addressing her, this verse's closing note credits it to "
        "&lsquo;the senior nun Puṇṇā&rsquo; herself, already carrying the title "
        "&lsquo;senior&rsquo; that names this whole collection."),
    guide=[
        ("Another name turned into instruction", [
            "&lsquo;Puṇṇā&rsquo; means &lsquo;full&rsquo; or "
            "&lsquo;fulfilled&rsquo;. As with Muttā, the verse addresses her "
            "using her own name as a directive: &lsquo;Puṇṇā, be filled with "
            "good qualities&rsquo;."]),
        ("A different lunar phase than Thig 1.2", [
            "Where Muttā's verse used an eclipse ending, Puṇṇā's uses the moon "
            "at its fullest: &lsquo;like the moon on the fifteenth day&rsquo; "
            "&mdash; completion rather than release, though both draw on the "
            "same recurring image of the moon."]),
        ("A specific outcome named directly", [
            "The verse's second half states a concrete result of that fullness: "
            "&lsquo;when your wisdom is full, shatter the mass of "
            "darkness&rsquo; &mdash; wisdom pictured as something that "
            "accumulates until it becomes powerful enough to break through "
            "ignorance entirely."]),
        ("Attributed to the poet herself, already senior", [
            "Unlike Thig 1.2, this poem's attribution does not credit the "
            "Buddha as speaker; it simply states &lsquo;this verse was recited "
            "by the senior nun Puṇṇā&rsquo; &mdash; the title &lsquo;therī&rsquo; "
            "this whole collection is named for, already applied to her within "
            "its very first book."]),
    ],
    terms=[
        ("Puṇṇā",
         "a nun's name, also the Pali word for &lsquo;full&rsquo; or "
         "&lsquo;fulfilled&rsquo; &mdash; the verse plays directly on this "
         "double meaning, as Thig 1.2 does with Muttā."),
        ("therī",
         "&ldquo;senior nun&rdquo; &mdash; the title this poem's own "
         "attribution applies to Puṇṇā, the same word naming this whole "
         "collection."),
        ("paññā",
         "&ldquo;wisdom&rdquo; &mdash; named directly as what becomes full in "
         "this verse's second half, powerful enough to shatter ignorance."),
        ("avijjā",
         "&ldquo;ignorance&rdquo; &mdash; the &lsquo;mass of darkness&rsquo; "
         "this verse says full wisdom shatters."),
        ("cariyā",
         "not used in this poem; unlike the Cariyapitaka, no closing formula "
         "names a &lsquo;perfection&rsquo; here &mdash; the Therigatha's own "
         "closing convention is a simple attribution note instead."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.3:1.1-1.4"),
        ("p", "&sect;2", "thig1.3:2.1-2.1"),
    ],
    quiz=[
        {"q": "What does the name 'Puṇṇā' mean, and how does the verse use this?",
         "opts": [
             "'Wisdom' — used as a formal title",
             "'Full' or 'fulfilled' — used as a direct instruction, playing on her name",
             "'Moon' — a purely descriptive nickname",
             "The name has no particular meaning"],
         "correct": 1,
         "expl": "The same naming device used in Thig 1.2 for Muttā."},
        {"q": "What lunar image does this verse use, compared to Thig 1.2's?",
         "opts": [
             "The exact same eclipse image",
             "The moon at its fullest, on the fifteenth day, rather than released from an eclipse",
             "No lunar image is used here",
             "A lunar eclipse specifically"],
         "correct": 1,
         "expl": "Completion rather than release, though both share the recurring moon motif."},
        {"q": "What does the verse say happens when wisdom becomes full?",
         "opts": [
             "Nothing further is described",
             "It shatters the mass of darkness",
             "It brings material wealth",
             "It attracts new students"],
         "correct": 1,
         "expl": "Wisdom pictured as accumulating until powerful enough to break through ignorance."},
        {"q": "Who does this poem's attribution credit as its speaker?",
         "opts": [
             "The Buddha, addressing Puṇṇā",
             "The senior nun Puṇṇā herself",
             "An unnamed nun",
             "No speaker is credited"],
         "correct": 1,
         "expl": "Unlike Thig 1.2's attribution to the Buddha."},
        {"q": "What title does the attribution apply to Puṇṇā?",
         "opts": [
             "'Trainee'",
             "'Senior nun' (therī) — the same word naming the whole collection",
             "'Novice'",
             "No title is applied"],
         "correct": 1,
         "expl": "Already carrying the collection's own title within its first book."},
        {"q": "What does 'avijjā' mean in this verse?",
         "opts": [
             "'Wisdom'",
             "'Ignorance' — the 'mass of darkness' full wisdom shatters",
             "'Fullness'",
             "'Moon'"],
         "correct": 1,
         "expl": "Directly opposed to the paññā (wisdom) named in the same verse."},
        {"q": "How does this poem's structure compare to Thig 1.2's?",
         "opts": [
             "Completely unrelated in form",
             "It repeats the same basic pattern — a name used as instruction, paired with a lunar image",
             "It has no closing attribution at all",
             "It is written entirely in prose"],
         "correct": 1,
         "expl": "A close structural echo between these two adjacent poems."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The first poem",
             "The third poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Thig 1.1 and Thig 1.2."},
        {"q": "Does this poem use a closing formula naming a 'perfection', as in the Cariyapitaka?",
         "opts": [
             "Yes, identical to the Cariyapitaka's formula",
             "No — the Therigatha's closing convention is a simple attribution note instead",
             "It uses a unique formula found nowhere else",
             "The poem has no ending at all"],
         "correct": 1,
         "expl": "A different collection with a different closing convention."},
        {"q": "What does 'paññā' mean?",
         "opts": [
             "'Wisdom' — what this verse says becomes full",
             "'Ignorance'",
             "'Moon'",
             "'Attribution'"],
         "correct": 0,
         "expl": "Named directly in the verse's second half."},
    ],
    marginalia=[
        ("A name used as instruction", [
            "'Puṇṇā' means",
            "'full' itself"
        ]),
        ("The moon at its fullest", [
            "the fifteenth day,",
            "not an eclipse"
        ]),
        ("Wisdom shatters darkness", [
            "full wisdom",
            "breaks through ignorance"
        ]),
        ("Attributed to herself", [
            "already called",
            "'senior nun'"
        ]),
    ],
    further=[
        '<a href="%s/thig1.3/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.2.html">Thig 1.2 &mdash; Mutt&amacr; (1st)</a> &mdash; '
        "the text immediately before this one, a closely matching structure.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.4 — Tissā
# --------------------------------------------------------------------------- #
page(
    1, 4, "Tiss&amacr;", "Tiss&amacr;",
    meta_title="Thig 1.4 — Tissā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Tissā's "
        "verse, a bare four-line exhortation with no closing attribution at "
        "all. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 4 of 18",
    glance=[
        ("Setting", "No narrative setting, and no closing attribution of any "
                    "kind"),
        ("Speaker", "Not identified; presented as direct address to Tissā, "
                    "with no attribution stating who speaks"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the bare "
                       "minimum form this collection's shortest poems take"),
    ],
    why=(
        "Where Thig 1.1 through 1.3 each closed with an attribution naming a "
        "speaker and occasion, this poem has none at all &mdash; just four "
        "lines addressed to a nun named Tissā, with no indication of who is "
        "speaking to her or when. From this poem through several more in this "
        "book, the collection settles into its barest possible form."),
    guide=[
        ("An address with no framing at all", [
            "Unlike the first three poems in this book, Thig 1.4 supplies "
            "neither a homage line nor a closing attribution &mdash; just the "
            "verse itself, addressed directly to &lsquo;Tissā&rsquo; in the "
            "second person."]),
        ("A double instruction: train, and don't be overcome", [
            "The verse gives two related commands: &lsquo;train in the "
            "trainings&rsquo; (an active pursuit) and &lsquo;don't let your "
            "yokes overcome you&rsquo; (a defensive posture) &mdash; discipline "
            "and resistance to setback presented as two sides of the same "
            "practice."]),
        ("A conditional promise closing the verse", [
            "The verse ends by describing what follows if the instruction is "
            "kept: &lsquo;unyoked from all yokes, live in the world free of "
            "defilements&rsquo; &mdash; not a promise of leaving the world "
            "behind, but of living within it differently."]),
        ("The first of several unattributed poems in this book", [
            "Several of the Book of the Ones' remaining poems follow this same "
            "bare pattern &mdash; a direct address with no framing device at "
            "all &mdash; before the book's later poems shift back toward "
            "first-person testimony."]),
    ],
    terms=[
        ("Tissā",
         "the nun addressed in this poem; a second, different nun of the same "
         "name is addressed in the very next poem, Thig 1.5."),
        ("sikkhā",
         "&ldquo;training&rdquo; &mdash; what Tissā is instructed to actively "
         "pursue in this verse's opening line."),
        ("yoga",
         "&ldquo;yoke&rdquo; &mdash; the same recurring image from Thig 1.2, "
         "here something to avoid being overcome by, rather than simply "
         "released from."),
        ("kilesa",
         "&ldquo;defilement&rdquo; &mdash; what the verse says a person "
         "unyoked from all yokes lives free of, while still living in the "
         "world."),
        ("cariyā",
         "not used here; this poem's total lack of any closing formula marks "
         "a further contrast with the Cariyapitaka's uniform closing "
         "convention."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.4:1.1-1.4"),
    ],
    quiz=[
        {"q": "What is unusual about this poem's ending, compared to Thig 1.1–1.3?",
         "opts": [
             "It has an especially long attribution",
             "It has no closing attribution at all — no speaker or occasion is named",
             "It ends mid-sentence",
             "It repeats the same attribution as Thig 1.3"],
         "correct": 1,
         "expl": "Just four lines of direct address, nothing more."},
        {"q": "What two instructions does the verse give?",
         "opts": [
             "Only a single instruction",
             "Train in the trainings, and don't let your yokes overcome you",
             "Leave the monastery and travel",
             "Seek out a specific teacher"],
         "correct": 1,
         "expl": "An active pursuit paired with a defensive posture."},
        {"q": "What does the verse promise if this instruction is followed?",
         "opts": [
             "Wealth and status",
             "Living in the world free of defilements, unyoked from all yokes",
             "Escape from the world entirely",
             "Nothing is promised"],
         "correct": 1,
         "expl": "Living within the world differently, not leaving it behind."},
        {"q": "How many nuns named Tissā appear across this book's poems?",
         "opts": [
             "Only one",
             "Two — this poem and Thig 1.5, 'Another Tissā'",
             "Three or more",
             "None; Tissā is not a name in this collection"],
         "correct": 1,
         "expl": "Distinguished by the title 'Another Tissā' in the next poem."},
        {"q": "What does 'sikkhā' mean?",
         "opts": [
             "'Training' — what Tissā is instructed to pursue",
             "'Yoke'",
             "'Defilement'",
             "'Attribution'"],
         "correct": 0,
         "expl": "Named directly in the verse's opening command."},
        {"q": "What does the phrase 'unyoked from all yokes' describe?",
         "opts": [
             "A physical posture for meditation",
             "The result of successfully training and resisting being overcome",
             "A punishment for failing to train",
             "A type of ordination ceremony"],
         "correct": 1,
         "expl": "The outcome the verse's second half describes."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The first poem",
             "The fourth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Thig 1.1 through 1.3."},
        {"q": "What does 'kilesa' mean?",
         "opts": [
             "'Defilement' — what one is free of when unyoked from all yokes",
             "'Training'",
             "'Attribution'",
             "'Moon'"],
         "correct": 0,
         "expl": "Named in the verse's closing line."},
        {"q": "How does this poem's lack of attribution affect what we know about its speaker?",
         "opts": [
             "It confirms the speaker is definitely the Buddha",
             "It leaves the speaker's identity entirely unstated",
             "It confirms Tissā is speaking to herself",
             "The verse names its speaker directly within the text"],
         "correct": 1,
         "expl": "No indication is given either way."},
        {"q": "What broader pattern does this poem begin within the Book of the Ones?",
         "opts": [
             "A shift to poems entirely in prose",
             "Several unattributed, bare address-poems before the book later shifts to first-person testimony",
             "The book's final poem",
             "A shift to poems about kings rather than nuns"],
         "correct": 1,
         "expl": "The barest possible form this collection's shortest poems take."},
    ],
    marginalia=[
        ("No framing at all", [
            "no homage,",
            "no attribution"
        ]),
        ("Two instructions", [
            "train actively,",
            "resist being overcome"
        ]),
        ("A world lived in differently", [
            "not escaped,",
            "but unyoked"
        ]),
        ("A second Tissā follows", [
            "distinguished",
            "by name only"
        ]),
    ],
    further=[
        '<a href="%s/thig1.4/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.3.html">Thig 1.3 &mdash; Pu&#7751;&#7751;&amacr;</a> '
        "&mdash; the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.5 — Another Tissā
# --------------------------------------------------------------------------- #
page(
    1, 5, "Tiss&amacr;", "Another Tiss&amacr;",
    meta_title="Thig 1.5 — Another Tissā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for this "
        "second Tissā's verse, a starker warning about missed opportunity and "
        "hell. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 5 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to a second nun also "
                    "named Tissā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the "
                       "collection's first mention of hell as a consequence"),
    ],
    why=(
        "This poem shares its addressee's name with Thig 1.4, but not its "
        "tone. Where the first Tissā is told to train and resist being "
        "overcome, this second Tissā is warned about squandering time itself "
        "&mdash; the verse's closing line names a consequence, grief in hell, "
        "sharper than anything in this book's poems so far."),
    guide=[
        ("The same name, a different urgency", [
            "The title &lsquo;Another Tissā&rsquo; signals directly that this "
            "is a different individual from Thig 1.4's addressee, sharing only "
            "a name &mdash; the collection is explicit about not conflating "
            "the two."]),
        ("An instruction about timing, not just conduct", [
            "Rather than a general call to train, this verse's core "
            "instruction is about not missing an opportunity: &lsquo;apply "
            "yourself to good qualities &mdash; don't let the moment pass you "
            "by.&rsquo;"]),
        ("A stated cost for missing it", [
            "The verse names a specific consequence for delay: &lsquo;if you "
            "miss your moment, you'll grieve when sent to hell&rsquo; &mdash; a "
            "starker warning than any offered to the first Tissā, or to Muttā "
            "or Puṇṇā before her."]),
        ("Grief located after the fact, not during", [
            "The verse's warning is not about suffering while missing the "
            "moment, but about grief afterward, once the consequence has "
            "already arrived &mdash; framing urgency around a regret that "
            "cannot be undone once too late."]),
    ],
    terms=[
        ("Tissā",
         "the name shared by this poem's addressee and Thig 1.4's, "
         "distinguished only by the title &lsquo;Another Tissā&rsquo;."),
        ("khaṇa",
         "&ldquo;moment&rdquo; or &ldquo;opportunity&rdquo; &mdash; what this "
         "verse warns against letting pass by."),
        ("niraya",
         "&ldquo;hell&rdquo; &mdash; named directly as the destination this "
         "verse warns of, the starkest consequence named so far in this book."),
        ("kusala",
         "&ldquo;good&rdquo; or &ldquo;skillful&rdquo; &mdash; the quality "
         "Tissā is told to apply herself to before her moment passes."),
        ("cariyā",
         "not used here; another of this book's several poems with no closing "
         "formula at all, unlike the Cariyapitaka's uniform pattern."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.5:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the title 'Another Tissā' signal?",
         "opts": [
             "A mistake in the text",
             "That this is a different individual from Thig 1.4's Tissā, sharing only a name",
             "That this is the same Tissā speaking a second time",
             "A nickname for the same person"],
         "correct": 1,
         "expl": "The collection is explicit about not conflating the two."},
        {"q": "What is this verse's central instruction?",
         "opts": [
             "Build a new hermitage",
             "Apply yourself to good qualities — don't let the moment pass you by",
             "Travel to a specific city",
             "Seek out a particular teacher"],
         "correct": 1,
         "expl": "An instruction about timing and opportunity, not general conduct alone."},
        {"q": "What consequence does the verse warn of for missing this moment?",
         "opts": [
             "A minor inconvenience",
             "Grief when sent to hell",
             "Simple forgetfulness",
             "No consequence is named"],
         "correct": 1,
         "expl": "The starkest warning offered in this book's poems so far."},
        {"q": "When does the verse locate the grief it describes?",
         "opts": [
             "During the moment of missing the opportunity",
             "Afterward, once the consequence has already arrived",
             "Before the opportunity even appears",
             "No timing is specified"],
         "correct": 1,
         "expl": "Urgency framed around a regret that cannot be undone once too late."},
        {"q": "How does this poem's tone compare to Thig 1.4's?",
         "opts": [
             "Identical in every respect",
             "Sharper — naming hell as a consequence, where Thig 1.4 only described a positive outcome",
             "Much gentler than Thig 1.4",
             "This poem contains no warning at all"],
         "correct": 1,
         "expl": "The starkest tone shift so far within the Book of the Ones."},
        {"q": "What does 'khaṇa' mean?",
         "opts": [
             "'Moment' or 'opportunity' — what the verse warns against missing",
             "'Hell'",
             "'Good quality'",
             "'Yoke'"],
         "correct": 0,
         "expl": "The central concept this verse's warning turns on."},
        {"q": "What does 'niraya' mean?",
         "opts": [
             "'Training'",
             "'Hell' — the destination this verse warns of",
             "'Moment'",
             "'Attribution'"],
         "correct": 1,
         "expl": "Named directly as the consequence of missing one's moment."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha as speaker",
             "No — like Thig 1.4, it has no attribution at all",
             "Yes, naming Tissā herself as speaker",
             "It has two separate attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern begun with Thig 1.4."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The fourth poem",
             "The fifth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Immediately following the first Tissā's poem."},
        {"q": "What does 'kusala' mean?",
         "opts": [
             "'Good' or 'skillful' — the quality Tissā is told to apply herself to",
             "'Hell'",
             "'Grief'",
             "'Moment'"],
         "correct": 0,
         "expl": "Named in the verse's opening instruction."},
    ],
    marginalia=[
        ("Same name, different urgency", [
            "'another Tissā',",
            "a different warning"
        ]),
        ("A moment not to miss", [
            "apply yourself",
            "before it passes"
        ]),
        ("A stark consequence", [
            "grief in hell,",
            "the sharpest warning yet"
        ]),
        ("Grief after the fact", [
            "regret that comes",
            "too late to undo"
        ]),
    ],
    further=[
        '<a href="%s/thig1.5/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.4.html">Thig 1.4 &mdash; Tiss&amacr;</a> &mdash; the '
        "text immediately before this one, sharing this poem's addressee's "
        "name.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.6 — Dhīrā
# --------------------------------------------------------------------------- #
page(
    1, 6, "Dh&imacr;r&amacr;", "Dh&imacr;r&amacr;",
    meta_title="Thig 1.6 — Dhīrā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Dhīrā's "
        "verse, a compact instruction to touch cessation and win "
        "extinguishment. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 6 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to the nun Dhīrā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; dense "
                       "technical vocabulary packed into four lines"),
    ],
    why=(
        "This verse compresses the goal of the entire path into four lines "
        "addressed to a nun whose name, Dhīrā, already means "
        "&lsquo;steadfast&rsquo; or &lsquo;wise&rsquo;. Where earlier poems in "
        "this book described release or fullness, this one names the "
        "destination directly: cessation, and then extinguishment itself."),
    guide=[
        ("A name meaning steadiness", [
            "&lsquo;Dhīrā&rsquo; carries connotations of firmness and wisdom "
            "&mdash; a fitting name for a verse whose instructions move "
            "directly and without hesitation toward the path's furthest "
            "point."]),
        ("Cessation described as blissful, not blank", [
            "The verse specifies what &lsquo;touching cessation&rsquo; means: "
            "&lsquo;the blissful settling of perception&rsquo; &mdash; not an "
            "absence or a void, but a settling described in terms of ease."]),
        ("Two words for the same destination", [
            "The verse's second half names the goal twice, in different "
            "registers: &lsquo;win extinguishment&rsquo;, then immediately "
            "&lsquo;the supreme sanctuary from the yoke&rsquo; &mdash; one term "
            "naming what is attained, the other naming what it protects "
            "against."]),
        ("The yoke, named again", [
            "This is the third poem in this book to use the image of the "
            "&lsquo;yoke&rsquo;, after Thig 1.2 and Thig 1.4 &mdash; a recurring "
            "thread across these otherwise very different, very short poems."]),
    ],
    terms=[
        ("Dhīrā",
         "a nun's name carrying connotations of &lsquo;steadfast&rsquo; or "
         "&lsquo;wise&rsquo;."),
        ("nirodha",
         "&ldquo;cessation&rdquo; &mdash; what Dhīrā is instructed to touch, "
         "described here as a blissful settling rather than a blank absence."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; named directly in this verse as "
         "the goal to be won."),
        ("yoga-kkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; a compound term "
         "naming safety from the ties that bind a person to further rebirth."),
        ("saññā",
         "&ldquo;perception&rdquo; &mdash; the faculty this verse says settles "
         "blissfully at the moment cessation is touched."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.6:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name 'Dhīrā' carry connotations of?",
         "opts": [
             "'Beautiful' or 'graceful'",
             "'Steadfast' or 'wise'",
             "'Young' or 'new'",
             "'Wealthy'"],
         "correct": 1,
         "expl": "A fitting name for a verse that moves directly toward the path's furthest point."},
        {"q": "How does the verse describe 'touching cessation'?",
         "opts": [
             "As a blank, empty absence",
             "As 'the blissful settling of perception'",
             "As a violent breaking-through",
             "The verse does not describe it further"],
         "correct": 1,
         "expl": "Ease and settling, not a void."},
        {"q": "What two terms does the verse's second half use for the same destination?",
         "opts": [
             "'Wisdom' and 'compassion'",
             "'Extinguishment' and 'the supreme sanctuary from the yoke'",
             "'Training' and 'discipline'",
             "'Fame' and 'fortune'"],
         "correct": 1,
         "expl": "One naming what is attained, the other what it protects against."},
        {"q": "How many poems in this book, including this one, have used the image of the 'yoke'?",
         "opts": [
             "Only this one",
             "Three — this poem, Thig 1.2, and Thig 1.4",
             "All eighteen poems in the book",
             "None; this poem does not use that image"],
         "correct": 1,
         "expl": "A recurring thread across otherwise very different poems."},
        {"q": "What does 'nirodha' mean?",
         "opts": [
             "'Cessation' — what Dhīrā is instructed to touch",
             "'Yoke'",
             "'Wisdom'",
             "'Sanctuary'"],
         "correct": 0,
         "expl": "Described here as a blissful settling of perception."},
        {"q": "What does 'yoga-kkhema' mean?",
         "opts": [
             "'Cessation'",
             "'Sanctuary from the yoke' — safety from the ties binding one to rebirth",
             "'Perception'",
             "'Steadfastness'"],
         "correct": 1,
         "expl": "A compound term naming a specific kind of safety."},
        {"q": "What faculty does the verse say settles blissfully at cessation?",
         "opts": [
             "Memory",
             "Perception (saññā)",
             "Speech",
             "Sight"],
         "correct": 1,
         "expl": "Named directly in the verse's first half."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Dhīrā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The fifth poem",
             "The sixth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following the two poems addressed to nuns named Tissā."},
        {"q": "What does 'nibbāna' mean?",
         "opts": [
             "'Extinguishment' — the goal this verse says to win",
             "'Yoke'",
             "'Perception'",
             "'Steadfastness'"],
         "correct": 0,
         "expl": "Named directly in this verse's second half."},
    ],
    marginalia=[
        ("A name meaning steady", [
            "'Dhīrā' —",
            "steadfast, wise"
        ]),
        ("Cessation as bliss", [
            "perception settling,",
            "not a void"
        ]),
        ("Two names, one goal", [
            "extinguishment,",
            "sanctuary from the yoke"
        ]),
        ("The yoke, a third time", [
            "recurring across",
            "very different poems"
        ]),
    ],
    further=[
        '<a href="%s/thig1.6/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.5.html">Thig 1.5 &mdash; Another Tiss&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.7 — Vīrā
# --------------------------------------------------------------------------- #
page(
    1, 7, "V&imacr;r&amacr;", "V&imacr;r&amacr;",
    meta_title="Thig 1.7 — Vīrā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Vīrā's "
        "verse, the Book of the Ones' first poem describing its subject in "
        "the third person rather than addressing her directly. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 7 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; unlike the previous six poems, this one "
                    "describes Vīrā in the third person rather than "
                    "addressing her directly"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the "
                       "book's first shift into third-person description"),
    ],
    why=(
        "Every poem so far in this book has addressed its subject directly, "
        "in the second person &mdash; &lsquo;Muttā, be released&rsquo;, "
        "&lsquo;Dhīrā, touch cessation&rsquo;. This poem breaks that pattern: "
        "it describes Vīrā from outside, in the third person, explaining her "
        "name and naming Māra as the opponent she has already defeated."),
    guide=[
        ("A shift from address to description", [
            "Where Thig 1.2 through 1.6 speak to their subjects directly, this "
            "poem speaks about Vīrā: &lsquo;she's known as Vīrā because of her "
            "heroic qualities&rsquo; &mdash; an outside voice explaining who "
            "she is, rather than instructing her."]),
        ("A name's meaning stated outright, not just played on", [
            "Where Muttā's and Puṇṇā's poems relied on the reader recognizing "
            "the wordplay in their names, this verse states the connection "
            "directly: Vīrā is called that &lsquo;because of her heroic "
            "qualities&rsquo; &mdash; <em>vīra</em> meaning &lsquo;hero&rsquo; "
            "or &lsquo;heroic&rsquo;."]),
        ("An achievement stated as already complete", [
            "Unlike the instructive tone of the previous poems, this verse "
            "describes something finished: &lsquo;she bears her final body, "
            "having vanquished Māra with his legions&rsquo; &mdash; not "
            "encouragement toward a goal, but a report of it already won."]),
        ("Māra named for the first time in this book", [
            "This is the first poem in the Book of the Ones to name Māra "
            "&mdash; the personification of death and temptation that "
            "recurs across the canon as the tradition's central antagonist "
            "&mdash; described here as defeated along with his forces."]),
    ],
    terms=[
        ("Vīrā",
         "a nun's name, related to <em>vīra</em>, &ldquo;hero&rdquo; or "
         "&ldquo;heroic&rdquo; &mdash; the verse states this connection "
         "directly."),
        ("indriya",
         "&ldquo;faculties&rdquo; &mdash; what the verse says Vīrā has "
         "developed, referring to the mental and spiritual capacities "
         "cultivated through practice."),
        ("Māra",
         "the personification of death and temptation, the tradition's "
         "recurring antagonist figure, named here as defeated &lsquo;with his "
         "legions&rsquo;."),
        ("antimadeha",
         "&ldquo;final body&rdquo; &mdash; the description applied to Vīrā, "
         "indicating she will not be reborn again."),
        ("cariyā",
         "not used here; this poem, like several others in the book, closes "
         "with no formula naming a perfection, unlike the Cariyapitaka's "
         "uniform convention."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.7:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this poem's perspective differ from Thig 1.2–1.6?",
         "opts": [
             "It is identical, addressing Vīrā directly",
             "It describes Vīrā in the third person, rather than addressing her directly",
             "It is written entirely in first person",
             "It has no perspective at all"],
         "correct": 1,
         "expl": "The book's first shift from second-person address to third-person description."},
        {"q": "What does the verse say Vīrā's name reflects?",
         "opts": [
             "Her physical appearance",
             "Her heroic qualities",
             "Her family lineage",
             "The city she was born in"],
         "correct": 1,
         "expl": "Stated directly, unlike the implicit wordplay in earlier poems."},
        {"q": "What does 'she bears her final body' indicate?",
         "opts": [
             "She is about to die of illness",
             "She will not be reborn again",
             "She has taken on a new physical form",
             "Nothing in particular"],
         "correct": 1,
         "expl": "A statement of completed attainment, not an instruction toward one."},
        {"q": "Who is named as defeated in this verse?",
         "opts": [
             "A rival teacher",
             "Māra, along with his legions",
             "A hostile king",
             "No opponent is named"],
         "correct": 1,
         "expl": "The first appearance of Māra in this book."},
        {"q": "What does Māra personify in the wider tradition?",
         "opts": [
             "Wisdom and insight",
             "Death and temptation",
             "Generosity",
             "Royal authority"],
         "correct": 1,
         "expl": "The tradition's recurring antagonist figure."},
        {"q": "What does 'indriya' mean in this verse?",
         "opts": [
             "'Faculties' — the mental and spiritual capacities Vīrā has developed",
             "'Final body'",
             "'Hero'",
             "'Legion'"],
         "correct": 0,
         "expl": "Named as something Vīrā possesses, already developed."},
        {"q": "How does this poem's tone compare to the instructive tone of Thig 1.2–1.6?",
         "opts": [
             "Identical, still giving direct commands",
             "It reports an achievement already complete, rather than encouraging one",
             "It is more urgent and commanding than the previous poems",
             "It contains no content about achievement at all"],
         "correct": 1,
         "expl": "A shift from encouragement toward a goal to a report of it already won."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The sixth poem",
             "The seventh poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Dhīrā's verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Vīrā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What does 'antimadeha' describe?",
         "opts": [
             "A type of monastic robe",
             "'Final body' — indicating no further rebirth",
             "A meditation posture",
             "A geographic region"],
         "correct": 1,
         "expl": "Applied to Vīrā as a statement of her attainment."},
    ],
    marginalia=[
        ("Described, not addressed", [
            "the book's first",
            "third-person poem"
        ]),
        ("A name explained outright", [
            "'heroic qualities' —",
            "stated, not implied"
        ]),
        ("An achievement completed", [
            "'her final body',",
            "already won"
        ]),
        ("Māra named and defeated", [
            "'with his legions' —",
            "first mention in this book"
        ]),
    ],
    further=[
        '<a href="%s/thig1.7/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.6.html">Thig 1.6 &mdash; Dh&imacr;r&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.8 — Mittā (1st)
# --------------------------------------------------------------------------- #
page(
    1, 8, "Mitt&amacr;", "Mitt&amacr; (1st)",
    meta_title="Thig 1.8 — Mittā (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Mittā's "
        "verse, an instruction to appreciate spiritual friendship, the first "
        "half of a closely matched pair with Thig 1.9. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Poem 8 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to the nun Mittā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; simple on "
                       "its own, but best read alongside Thig 1.9"),
    ],
    why=(
        "This verse and the one immediately after it, Thig 1.9, share nearly "
        "identical wording &mdash; a template repeated with only the "
        "addressee's name and one key phrase changed. Here, addressed to "
        "Mittā (&lsquo;friend&rsquo;), the instruction centers on appreciating "
        "&lsquo;spiritual friends&rsquo;, a concept the wider tradition treats "
        "as close to the whole of the path."),
    guide=[
        ("A name meaning friend, turned toward friendship itself", [
            "&lsquo;Mittā&rsquo; means &lsquo;friend&rsquo;. The instruction "
            "built on her name does not simply tell her to be a good friend, "
            "but to &lsquo;appreciate your spiritual friends&rsquo; &mdash; "
            "gratitude for companionship on the path, not just the quality of "
            "friendliness."]),
        ("Faith named as the starting point", [
            "The verse opens by naming what brought Mittā to this point: "
            "&lsquo;having gone forth in faith&rsquo; &mdash; renunciation "
            "framed as an act of trust, not calculation."]),
        ("A near-template shared with the very next poem", [
            "Compare this verse to Thig 1.9, addressed to Bhadrā: the "
            "structure, most of the wording, and the closing image of "
            "&lsquo;sanctuary from the yoke&rsquo; are identical, with only "
            "the name and the specific object of appreciation changed."]),
        ("A concept larger than this one short verse", [
            "&lsquo;Spiritual friendship&rsquo; (<em>kalyāṇamittatā</em>) is "
            "elsewhere in the canon described by the Buddha as effectively the "
            "whole of the spiritual life, not merely a support for it &mdash; "
            "this brief instruction rests on a much larger claim about how "
            "central companionship is to the path."]),
    ],
    terms=[
        ("Mittā",
         "a nun's name, also the Pali word for &lsquo;friend&rsquo; &mdash; "
         "the instruction plays directly on this meaning."),
        ("kalyāṇamittatā",
         "&ldquo;spiritual friendship&rdquo; or &ldquo;admirable "
         "companionship&rdquo; &mdash; elsewhere in the canon described as "
         "close to the whole of the spiritual path, not merely a support for "
         "it."),
        ("saddhā",
         "&ldquo;faith&rdquo; or &ldquo;confidence&rdquo; &mdash; named as "
         "what led Mittā to go forth from household life."),
        ("yoga-kkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; the same compound "
         "term closing Thig 1.6, appearing again here as the aim of "
         "developing skillful qualities."),
        ("cariyā",
         "not used here; another of this book's unattributed poems, closing "
         "with no formula naming a perfection."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.8:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name 'Mittā' mean?",
         "opts": [
             "'Blessing'",
             "'Friend'",
             "'Wisdom'",
             "'Steadfastness'"],
         "correct": 1,
         "expl": "The verse's instruction plays directly on this meaning."},
        {"q": "What is Mittā specifically instructed to appreciate?",
         "opts": [
             "Her own achievements",
             "Her spiritual friends",
             "Material wealth",
             "Royal patronage"],
         "correct": 1,
         "expl": "Gratitude for companionship on the path, not simply being friendly."},
        {"q": "What does the verse name as bringing Mittā to renunciation?",
         "opts": [
             "A family obligation",
             "Faith (saddhā)",
             "Financial hardship",
             "A direct command from a king"],
         "correct": 1,
         "expl": "Renunciation framed as an act of trust."},
        {"q": "How does this poem relate to Thig 1.9, the very next poem?",
         "opts": [
             "They are entirely unrelated in structure",
             "They share a near-identical template, differing mainly in the addressee's name and one phrase",
             "They contradict each other directly",
             "Thig 1.9 is a prose retelling of this verse"],
         "correct": 1,
         "expl": "Best read as a closely matched pair."},
        {"q": "What does 'kalyāṇamittatā' refer to, more broadly in the canon?",
         "opts": [
             "A minor supporting practice, rarely mentioned",
             "Something the Buddha elsewhere describes as close to the whole of the spiritual life",
             "A specific meditation technique",
             "A formal monastic rank"],
         "correct": 1,
         "expl": "A much larger claim than this brief instruction alone suggests."},
        {"q": "What does 'saddhā' mean?",
         "opts": [
             "'Faith' or 'confidence' — named as Mittā's starting point",
             "'Friend'",
             "'Sanctuary'",
             "'Yoke'"],
         "correct": 0,
         "expl": "Renunciation described as an act of trust, not calculation."},
        {"q": "What phrase closes this verse, also appearing in Thig 1.6?",
         "opts": [
             "'The blissful settling of perception'",
             "'Sanctuary from the yoke' (yoga-kkhema)",
             "'Vanquished Māra with his legions'",
             "'Free of debt'"],
         "correct": 1,
         "expl": "A recurring compound term across several of this book's poems."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The seventh poem",
             "The eighth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Vīrā's verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Mittā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What quality does the verse instruct Mittā to develop, alongside appreciating friendship?",
         "opts": [
             "Physical strength",
             "Skillful qualities",
             "Public speaking ability",
             "Financial independence"],
         "correct": 1,
         "expl": "Aimed at reaching sanctuary from the yoke."},
    ],
    marginalia=[
        ("A name meaning friend", [
            "'Mittā' —",
            "appreciate your friends"
        ]),
        ("Faith as the starting point", [
            "gone forth",
            "in trust, not calculation"
        ]),
        ("A near-template pair", [
            "almost identical",
            "to the poem right after"
        ]),
        ("A concept larger than one verse", [
            "spiritual friendship,",
            "close to the whole path"
        ]),
    ],
    further=[
        '<a href="%s/thig1.8/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.7.html">Thig 1.7 &mdash; V&imacr;r&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="thig-1.9.html">Thig 1.9 &mdash; Bhadr&amacr;</a> &mdash; the '
        "text right after this one, sharing nearly identical wording.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.9 — Bhadrā
# --------------------------------------------------------------------------- #
page(
    1, 9, "Bhadr&amacr;", "Bhadr&amacr;",
    meta_title="Thig 1.9 — Bhadrā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Bhadrā's "
        "verse, an instruction to appreciate one's blessings, the second half "
        "of a closely matched pair with Thig 1.8. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Poem 9 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to the nun Bhadrā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; simple on "
                       "its own, best read alongside Thig 1.8"),
    ],
    why=(
        "This poem completes the closely matched pair begun by Thig 1.8. The "
        "structure and most of the wording repeat exactly, with two changes: "
        "the name addressed, and what she is told to appreciate &mdash; not "
        "spiritual friends this time, but her own &lsquo;blessings&rsquo;."),
    guide=[
        ("A name meaning fortunate, turned toward gratitude", [
            "&lsquo;Bhadrā&rsquo; means &lsquo;blessed&rsquo;, "
            "&lsquo;fortunate&rsquo;, or &lsquo;auspicious&rsquo;. Where "
            "Mittā's verse directed her toward appreciating her friends, "
            "Bhadrā's directs her toward appreciating her own good "
            "fortune."]),
        ("The same opening line, word for word", [
            "&lsquo;Having gone forth in faith&rsquo; opens this verse "
            "exactly as it opens Thig 1.8 &mdash; the same starting "
            "condition, faith, credited for a different woman's renunciation."]),
        ("One word upgraded in the closing line", [
            "Where Thig 1.8 closes on &lsquo;sanctuary from the yoke&rsquo;, "
            "this verse closes on &lsquo;the supreme sanctuary from the "
            "yoke&rsquo; &mdash; the single addition of &lsquo;supreme&rsquo; "
            "the clearest wording difference between the two otherwise "
            "matching poems."]),
        ("A pair worth reading together, not separately", [
            "Read alone, this verse's instruction to &lsquo;appreciate your "
            "blessings&rsquo; might seem generic. Read beside Thig 1.8, the "
            "shared template becomes visible &mdash; two women, two "
            "name-based instructions, one underlying formula."]),
    ],
    terms=[
        ("Bhadrā",
         "a nun's name, also the Pali word for &lsquo;blessed&rsquo;, "
         "&lsquo;fortunate&rsquo;, or &lsquo;auspicious&rsquo; &mdash; the "
         "verse plays directly on this meaning."),
        ("saddhā",
         "&ldquo;faith&rdquo; or &ldquo;confidence&rdquo; &mdash; named as "
         "Bhadrā's starting point, in wording identical to Thig 1.8's "
         "opening line."),
        ("bhāgya",
         "&ldquo;fortune&rdquo; or &ldquo;blessing&rdquo; &mdash; what "
         "Bhadrā is instructed to appreciate, the one substituted term that "
         "distinguishes this verse from Thig 1.8."),
        ("yoga-kkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; closing this verse "
         "as it closes Thig 1.6 and Thig 1.8, here intensified with "
         "&lsquo;supreme&rsquo;."),
        ("cariyā",
         "not used here; another of this book's unattributed poems, closing "
         "with no formula naming a perfection."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.9:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name 'Bhadrā' mean?",
         "opts": [
             "'Friend'",
             "'Blessed', 'fortunate', or 'auspicious'",
             "'Steadfast'",
             "'Hero'"],
         "correct": 1,
         "expl": "The verse's instruction plays directly on this meaning."},
        {"q": "What is Bhadrā specifically instructed to appreciate?",
         "opts": [
             "Her spiritual friends, as in Thig 1.8",
             "Her own blessings",
             "Royal patronage",
             "A specific teacher"],
         "correct": 1,
         "expl": "The one substituted object of appreciation, compared to Thig 1.8's 'friends'."},
        {"q": "How does this verse's opening line compare to Thig 1.8's?",
         "opts": [
             "Completely different",
             "Word for word identical — 'having gone forth in faith'",
             "Only the general meaning is similar",
             "This verse has no opening line about faith"],
         "correct": 1,
         "expl": "The same starting condition credited for both women's renunciation."},
        {"q": "What single word distinguishes this verse's closing line from Thig 1.8's?",
         "opts": [
             "'Wisdom'",
             "'Supreme' — intensifying 'sanctuary from the yoke'",
             "'Eternal'",
             "There is no difference at all"],
         "correct": 1,
         "expl": "The clearest wording difference between these two otherwise matching poems."},
        {"q": "Why is this poem best read alongside Thig 1.8 rather than alone?",
         "opts": [
             "They contradict each other and must be reconciled",
             "The shared template between them only becomes visible when read together",
             "Thig 1.9 makes no sense without Thig 1.8's context",
             "There is no reason to read them together"],
         "correct": 1,
         "expl": "Two women, two name-based instructions, one underlying formula."},
        {"q": "What does 'bhāgya' mean?",
         "opts": [
             "'Fortune' or 'blessing' — what Bhadrā is told to appreciate",
             "'Faith'",
             "'Yoke'",
             "'Sanctuary'"],
         "correct": 0,
         "expl": "The key substituted term compared to Thig 1.8."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The eighth poem",
             "The ninth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Mittā's verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Bhadrā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What quality does the verse instruct Bhadrā to develop?",
         "opts": [
             "Physical endurance",
             "Skillful qualities",
             "Public reputation",
             "Wealth"],
         "correct": 1,
         "expl": "Aimed at reaching the supreme sanctuary from the yoke."},
        {"q": "What term closes both this verse and Thig 1.6 and Thig 1.8?",
         "opts": [
             "Nibbāna",
             "Yoga-kkhema, 'sanctuary from the yoke'",
             "Saddhā",
             "Bhāgya"],
         "correct": 1,
         "expl": "A recurring closing phrase across several poems in this book."},
    ],
    marginalia=[
        ("A name meaning blessed", [
            "'Bhadrā' —",
            "appreciate your fortune"
        ]),
        ("The same opening line", [
            "'gone forth in faith',",
            "word for word"
        ]),
        ("One word upgraded", [
            "'supreme' sanctuary,",
            "the only real change"
        ]),
        ("A pair, not two isolated poems", [
            "the shared template",
            "only visible together"
        ]),
    ],
    further=[
        '<a href="%s/thig1.9/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="thig-1.8.html">Thig 1.8 &mdash; Mitt&amacr; (1st)</a> &mdash; '
        "the text immediately before this one, sharing nearly identical "
        "wording.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.10 — Upasamā
# --------------------------------------------------------------------------- #
page(
    1, 10, "Upasam&amacr;", "Upasam&amacr;",
    meta_title="Thig 1.10 — Upasamā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Upasamā's verse, an instruction to cross the flood and vanquish "
        "Māra, closing the first half of the Book of the Ones. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 10 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to the nun Upasamā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short, "
                       "combining two of this book's recurring images"),
    ],
    why=(
        "This verse closes the first half of the Book of the Ones with an "
        "instruction that combines two images already seen separately in "
        "this book: the difficulty of a crossing, and the figure of Māra, "
        "here named together with his mount as an obstacle to be "
        "overcome before the goal already described in Thig 1.7 can be "
        "reached."),
    guide=[
        ("A name meaning peace, set against difficulty", [
            "&lsquo;Upasamā&rsquo; means &lsquo;peace&rsquo; or "
            "&lsquo;calm&rsquo;. The verse addressed to her does not describe "
            "peace as already present, but as something reached only by "
            "crossing something genuinely difficult first."]),
        ("A flood named as death's own territory", [
            "The crossing is described starkly: &lsquo;Death's dominion so "
            "hard to pass&rsquo; &mdash; not a minor obstacle but a domain "
            "belonging to death itself, framing the practice ahead as a "
            "genuine contest rather than a formality."]),
        ("Māra named again, with his mount", [
            "This is the second poem in the book to name Māra, after Thig "
            "1.7's Vīrā, here specifying &lsquo;Māra and his mount&rsquo; "
            "&mdash; the same antagonist figure, described with an added "
            "detail of his own transport."]),
        ("The same destination as Vīrā's verse", [
            "This poem closes with the identical phrase that closed Thig "
            "1.7: &lsquo;bear your final body&rsquo; &mdash; the same "
            "attainment, here offered as instruction rather than reported as "
            "already achieved."]),
    ],
    terms=[
        ("Upasamā",
         "a nun's name, also the Pali word for &lsquo;peace&rsquo; or "
         "&lsquo;calm&rsquo; &mdash; the verse's instruction moves toward "
         "this state through difficulty, not around it."),
        ("ogha",
         "&ldquo;flood&rdquo; &mdash; a common canonical image for the "
         "forces (sensuality, existence, views, ignorance) that sweep beings "
         "along in the cycle of rebirth."),
        ("maccu",
         "&ldquo;death&rdquo;, personified here as having a "
         "&lsquo;dominion&rdquo; &mdash; territory this verse instructs "
         "Upasamā to cross through, not avoid."),
        ("Māra",
         "the personification of death and temptation, named here for the "
         "second time in this book, after Thig 1.7."),
        ("antimadeha",
         "&ldquo;final body&rdquo; &mdash; the same term closing Thig 1.7, "
         "repeated here as this verse's own closing image."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.10:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name 'Upasamā' mean?",
         "opts": [
             "'Friend'",
             "'Peace' or 'calm'",
             "'Fortune'",
             "'Hero'"],
         "correct": 1,
         "expl": "A state this verse presents as reached through difficulty, not present already."},
        {"q": "How does the verse describe the flood Upasamā must cross?",
         "opts": [
             "As a minor, easily passed obstacle",
             "As 'Death's dominion so hard to pass'",
             "The verse mentions no flood at all",
             "As something already crossed"],
         "correct": 1,
         "expl": "Framing the practice ahead as a genuine contest, not a formality."},
        {"q": "Who is named as an obstacle in this verse, as in Thig 1.7?",
         "opts": [
             "A rival ascetic",
             "Māra, here specified together with his mount",
             "A hostile king",
             "No opponent is named"],
         "correct": 1,
         "expl": "The second appearance of Māra in this book."},
        {"q": "What phrase closes this verse, identical to Thig 1.7's closing?",
         "opts": [
             "'Sanctuary from the yoke'",
             "'Bear your final body'",
             "'Free of debt'",
             "'The blissful settling of perception'"],
         "correct": 1,
         "expl": "The same attainment, here offered as instruction rather than reported as achieved."},
        {"q": "What does 'ogha' mean?",
         "opts": [
             "'Flood' — the forces that sweep beings along in the cycle of rebirth",
             "'Peace'",
             "'Mount'",
             "'Dominion'"],
         "correct": 0,
         "expl": "A common canonical image this verse draws on."},
        {"q": "What is described as having a 'dominion' in this verse?",
         "opts": [
             "A king",
             "Death (maccu)",
             "Māra's mount specifically",
             "Nothing is described this way"],
         "correct": 1,
         "expl": "Personified territory this verse instructs crossing through."},
        {"q": "How does this poem's structure compare to Thig 1.7's?",
         "opts": [
             "Completely unrelated",
             "It combines images from earlier in the book — Māra and a final destination shared with Thig 1.7",
             "It contradicts Thig 1.7 directly",
             "It is written in prose, unlike Thig 1.7"],
         "correct": 1,
         "expl": "Closing the book's first half by drawing together earlier threads."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The ninth poem",
             "The tenth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Bhadrā's verse, closing the book's first half."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Upasamā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What does 'antimadeha' mean?",
         "opts": [
             "'Flood'",
             "'Final body' — indicating no further rebirth",
             "'Dominion'",
             "'Peace'"],
         "correct": 1,
         "expl": "Repeated word for word from Thig 1.7."},
    ],
    marginalia=[
        ("A name meaning peace", [
            "'Upasamā' —",
            "reached through difficulty"
        ]),
        ("Death's own territory", [
            "a flood",
            "hard to pass"
        ]),
        ("Māra, and his mount", [
            "the second mention",
            "in this book"
        ]),
        ("The same close as Thig 1.7", [
            "'bear your",
            "final body'"
        ]),
    ],
    further=[
        '<a href="%s/thig1.10/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.9.html">Thig 1.9 &mdash; Bhadr&amacr;</a> &mdash; the '
        "text immediately before this one in the Therigatha.",
        '<a href="thig-1.7.html">Thig 1.7 &mdash; V&imacr;r&amacr;</a> &mdash; '
        "the poem this one shares its closing image with.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.11 — Muttā (2nd)
# --------------------------------------------------------------------------- #
page(
    1, 11, "Mutt&amacr;", "Mutt&amacr; (2nd)",
    meta_title="Thig 1.11 — Muttā (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "second Muttā's verse, one of the Therigatha's most famous and "
        "vivid first-person declarations of freedom. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Poem 11 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "A second nun also named Muttā, speaking entirely in the "
                    "first person"),
        ("Form", "A single six-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; plain "
                       "and vivid, one of this book's most quoted verses"),
    ],
    why=(
        "This is one of the Therigatha's most celebrated verses, and it "
        "opens the second half of the Book of the Ones with a sharp turn: "
        "where Thig 1.2's Muttā was addressed by the Buddha with a gentle "
        "instruction, this second, different Muttā speaks entirely for "
        "herself, in plain, unglamorous, and strikingly joyful language."),
    guide=[
        ("A second Muttā, a different voice entirely", [
            "The title &lsquo;(2nd)&rsquo; distinguishes this poem's speaker "
            "from Thig 1.2's Muttā at once. Where that poem addressed its "
            "subject in the second person with careful, formal instruction, "
            "this one is spoken entirely in the first person, by a woman "
            "already free."]),
        ("Freedom stated three times, for emphasis", [
            "The poem opens with a doubled declaration &mdash; &lsquo;I'm "
            "well freed, so very well freed&rsquo; &mdash; before naming what "
            "she is freed from, an intensity of repetition unusual among this "
            "book's other, more measured verses."]),
        ("Domestic drudgery named without any elevated language at all", [
            "What she names as her former bondage is starkly ordinary: "
            "&lsquo;the mortar, the pestle, and my humpbacked husband&rsquo; "
            "&mdash; the daily grinding labor of a household, and a husband "
            "described by his physical appearance rather than any harsher "
            "accusation, placed in the very same list as a piece of "
            "kitchen equipment."]),
        ("From a household image to the whole of existence", [
            "The verse's final two lines pivot from that specific, homely "
            "image to the largest possible claim: &lsquo;I'm freed from birth "
            "and death; the leash to existence is eradicated&rsquo; &mdash; "
            "domestic freedom and final liberation held in the same short "
            "poem, without any sense of mismatch between them."]),
    ],
    terms=[
        ("Muttā",
         "a nun's name, also the Pali word for &lsquo;freed&rsquo; &mdash; "
         "here spoken by a second woman of the same name as Thig 1.2's, "
         "distinguished by the title &lsquo;(2nd)&rsquo;."),
        ("udukkhala, musala",
         "&ldquo;mortar&rdquo; and &ldquo;pestle&rdquo; &mdash; ordinary "
         "household tools for grinding grain, named among the things this "
         "verse's speaker is freed from."),
        ("jāti-maraṇa",
         "&ldquo;birth and death&rdquo; &mdash; the cycle of rebirth the "
         "verse's closing lines say the speaker is entirely freed from."),
        ("bhavanetti",
         "the &ldquo;leash to existence&rdquo; &mdash; the craving that ties "
         "a person to further rebirth, described here as "
         "&lsquo;eradicated&rsquo;."),
        ("cariyā",
         "not used here; another of this book's unattributed poems, though "
         "unlike most, spoken entirely in the first person."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.11:1.1-1.6"),
    ],
    quiz=[
        {"q": "How does this poem's speaker differ from Thig 1.2's Muttā?",
         "opts": [
             "They are the exact same person",
             "This is a second, different nun also named Muttā, distinguished by the title '(2nd)'",
             "This poem has no named speaker at all",
             "This Muttā is male"],
         "correct": 1,
         "expl": "A different voice entirely, speaking for herself rather than being addressed."},
        {"q": "How does the poem open?",
         "opts": [
             "With a formal greeting",
             "With a doubled declaration — 'I'm well freed, so very well freed'",
             "With a question",
             "With a description of a forest"],
         "correct": 1,
         "expl": "An intensity of repetition unusual among this book's other, more measured verses."},
        {"q": "What three things does the speaker say she is freed from?",
         "opts": [
             "Fear, doubt, and anger",
             "The mortar, the pestle, and her humpbacked husband",
             "Wealth, fame, and power",
             "Her family, her name, and her home village"],
         "correct": 1,
         "expl": "Starkly ordinary household imagery, with no elevated language."},
        {"q": "How is the husband described in this verse?",
         "opts": [
             "As cruel and violent, with detailed accusations",
             "By his physical appearance ('humpbacked'), placed in the same list as kitchen equipment",
             "With great affection and praise",
             "He is not mentioned at all"],
         "correct": 1,
         "expl": "A striking, matter-of-fact placement rather than an elaborate grievance."},
        {"q": "What claim does the verse's final two lines make?",
         "opts": [
             "A return to household life is planned",
             "Freedom from birth and death, with the leash to existence eradicated",
             "A request for material support",
             "Nothing further beyond the domestic image"],
         "correct": 1,
         "expl": "Domestic freedom and final liberation held in the same short poem."},
        {"q": "What does 'bhavanetti' mean?",
         "opts": [
             "'Mortar and pestle'",
             "The 'leash to existence' — craving that ties a person to further rebirth",
             "'Humpbacked husband'",
             "'Birth and death'"],
         "correct": 1,
         "expl": "Named in the verse's closing line as eradicated."},
        {"q": "How long is this poem, compared to most others in the Book of the Ones?",
         "opts": [
             "Four lines, the book's standard length",
             "Six lines, slightly longer than the book's typical four-line verses",
             "Twenty lines",
             "A single line only"],
         "correct": 1,
         "expl": "One of a small number of slightly longer poems in this book."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The tenth poem",
             "The eleventh poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Opening the second half of the book, following Upasamā's verse."},
        {"q": "Why is this poem considered one of the Therigatha's most celebrated verses?",
         "opts": [
             "It is the longest poem in the entire collection",
             "Its plain, unglamorous, vivid language and striking imagery",
             "It contains no spiritual content at all",
             "It was the first poem ever composed in Pali"],
         "correct": 1,
         "expl": "A frequently quoted example of this collection's directness."},
        {"q": "What does 'jāti-maraṇa' mean?",
         "opts": [
             "'Birth and death' — the cycle the speaker says she is freed from",
             "'Mortar and pestle'",
             "'Leash to existence'",
             "'Humpbacked husband'"],
         "correct": 0,
         "expl": "Named directly in the verse's closing lines."},
    ],
    marginalia=[
        ("Freedom, stated twice", [
            "'well freed,",
            "so very well freed'"
        ]),
        ("Ordinary, not elevated", [
            "mortar, pestle,",
            "humpbacked husband"
        ]),
        ("No harsh accusation", [
            "described plainly,",
            "not condemned"
        ]),
        ("From household to the whole", [
            "domestic freedom,",
            "final liberation"
        ]),
    ],
    further=[
        '<a href="%s/thig1.11/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.10.html">Thig 1.10 &mdash; Upasam&amacr;</a> &mdash; '
        "the text immediately before this one, closing the book's first half.",
        '<a href="thig-1.2.html">Thig 1.2 &mdash; Mutt&amacr; (1st)</a> '
        "&mdash; a different nun of the same name, addressed rather than "
        "speaking for herself.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.12 — Dhammadinnā
# --------------------------------------------------------------------------- #
page(
    1, 12, "Dhammadinn&amacr;", "Dhammadinn&amacr;",
    meta_title="Thig 1.12 — Dhammadinnā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Dhammadinnā's verse, an impersonal description of the eager and "
        "determined mind that heads upstream. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 12 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; the verse speaks impersonally of "
                    "whoever fits its description, rather than addressing "
                    "or describing Dhammadinnā by name within the text"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Dhammadinnā is a well-known figure elsewhere "
                              "in the canon, declared by the Buddha to be "
                              "foremost among nuns who teach the Dhamma; this "
                              "reading guide does not assert this verse "
                              "itself has a specific matching text."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "impersonal phrasing worth noticing on its own terms"),
    ],
    why=(
        "This verse is attributed to Dhammadinnā, one of the most learned "
        "women named anywhere in the early canon &mdash; elsewhere praised by "
        "the Buddha as foremost among nuns who teach the Dhamma, after giving "
        "a masterful doctrinal exposition to her former husband. Yet the "
        "verse itself names no one at all: it speaks generally of "
        "&lsquo;one who is eager and determined&rsquo;, not of Dhammadinnā "
        "specifically."),
    guide=[
        ("A name absent from its own verse", [
            "Unlike most poems in this book, which address or describe their "
            "subject by name, this verse never mentions Dhammadinnā within "
            "the text itself &mdash; only the title identifies whose verse "
            "it is."]),
        ("A description that could fit anyone who qualifies", [
            "The verse's opening line, &lsquo;one who is eager and "
            "determined&rsquo;, is phrased as a general condition rather "
            "than a personal address &mdash; describing a type of mind, not "
            "a specific individual's story."]),
        ("A direction opposite the ordinary current", [
            "The verse's closing image is directional: such a mind is "
            "&lsquo;said to be heading upstream&rsquo; &mdash; moving against "
            "the current of ordinary craving and habit, rather than being "
            "carried along by it."]),
        ("A learned teacher, known elsewhere in the canon", [
            "Dhammadinnā appears in a well-known discourse elsewhere in the "
            "canon giving an extended doctrinal exposition to her former "
            "husband, praised afterward by the Buddha himself as equal to "
            "his own teaching &mdash; a reputation this brief, impersonal "
            "verse gives no direct hint of."]),
    ],
    terms=[
        ("Dhammadinnā",
         "the nun this verse is attributed to, known elsewhere in the canon "
         "as foremost among nuns who teach the Dhamma."),
        ("ussoḷhī",
         "&ldquo;eagerness&rdquo; or &ldquo;determination&rdquo; &mdash; the "
         "quality this verse's opening line names as the starting condition "
         "for the mind it describes."),
        ("kāmaguṇa",
         "&ldquo;pleasures of sense&rdquo; &mdash; what this verse says the "
         "described mind is not bound to."),
        ("paṭisotagāmī",
         "&ldquo;heading upstream&rdquo; &mdash; a canonical image for "
         "moving against the current of ordinary craving, used here as this "
         "verse's closing description."),
        ("sati",
         "&ldquo;awareness&rdquo; or &ldquo;mindfulness&rdquo; &mdash; what "
         "the eager, determined mind is said to be filled with."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.12:1.1-1.4"),
    ],
    quiz=[
        {"q": "Does this verse name Dhammadinnā anywhere within its own text?",
         "opts": [
             "Yes, repeatedly",
             "No — only the title identifies whose verse it is",
             "Yes, but only once at the very end",
             "The verse names a different person entirely"],
         "correct": 1,
         "expl": "Unlike most poems in this book, which address or describe their subject by name."},
        {"q": "How is the verse's subject described?",
         "opts": [
             "By a specific personal story",
             "Impersonally, as 'one who is eager and determined' — a general condition, not a named individual",
             "By physical appearance",
             "By her family background"],
         "correct": 1,
         "expl": "A description of a type of mind, not a personal narrative."},
        {"q": "What does the verse say such a mind is filled with?",
         "opts": [
             "Doubt",
             "Awareness (sati)",
             "Fear",
             "Ambition"],
         "correct": 1,
         "expl": "Named directly in the verse's opening."},
        {"q": "What direction does the verse describe this mind as moving in?",
         "opts": [
             "Downstream, with the current",
             "Upstream, against the ordinary current of craving and habit",
             "In a circle",
             "No direction is described"],
         "correct": 1,
         "expl": "'Heading upstream' — a canonical image for resisting the pull of habitual craving."},
        {"q": "What is Dhammadinnā known for elsewhere in the canon?",
         "opts": [
             "Nothing of particular note",
             "Giving a masterful doctrinal exposition to her former husband, praised by the Buddha as equal to his own teaching",
             "Founding a rival religious movement",
             "Refusing to teach anyone"],
         "correct": 1,
         "expl": "A reputation this brief, impersonal verse gives no direct hint of."},
        {"q": "What does 'kāmaguṇa' mean?",
         "opts": [
             "'Pleasures of sense' — what the described mind is not bound to",
             "'Eagerness'",
             "'Upstream'",
             "'Awareness'"],
         "correct": 0,
         "expl": "Named in the verse's third line."},
        {"q": "What does 'ussoḷhī' mean?",
         "opts": [
             "'Eagerness' or 'determination' — the starting condition this verse names",
             "'Pleasures of sense'",
             "'Awareness'",
             "'Upstream'"],
         "correct": 0,
         "expl": "The opening quality named in this verse."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The eleventh poem",
             "The twelfth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following the second Muttā's celebrated verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Dhammadinnā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What is unusual about this poem compared to most others in this book?",
         "opts": [
             "It is written in prose",
             "It speaks impersonally of a general condition rather than addressing or describing its subject by name",
             "It has no verse content at all",
             "It is the longest poem in the book"],
         "correct": 1,
         "expl": "A notable structural contrast with the book's more personally addressed poems."},
    ],
    marginalia=[
        ("No name in the verse itself", [
            "only the title",
            "identifies the speaker"
        ]),
        ("A general condition", [
            "eager, determined —",
            "not one story"
        ]),
        ("Against the current", [
            "'heading upstream',",
            "not carried along"
        ]),
        ("A famous teacher elsewhere", [
            "praised as equal",
            "to the Buddha's own teaching"
        ]),
    ],
    further=[
        '<a href="%s/thig1.12/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.11.html">Thig 1.11 &mdash; Mutt&amacr; (2nd)</a> '
        "&mdash; the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.13 — Visākhā
# --------------------------------------------------------------------------- #
page(
    1, 13, "Vis&amacr;kh&amacr;", "Vis&amacr;kh&amacr;",
    meta_title="Thig 1.13 — Visākhā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Visākhā's verse, an unusually concrete, practical instruction on "
        "settling down to meditate. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 13 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to the nun Visākhā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "A laywoman also named Visākhā is famous "
                              "elsewhere as the Buddha's most eminent lay "
                              "female patron; this reading guide does not "
                              "assume the two are the same person, and "
                              "treats this poem's Visākhā as a nun in her "
                              "own right."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; simple, "
                       "practical, and refreshingly concrete"),
    ],
    why=(
        "Most poems in this book speak in fairly abstract terms &mdash; "
        "yokes, sanctuary, cessation. This verse is different: it gives an "
        "almost step-by-step practical instruction &mdash; wash your feet, "
        "find a discreet spot, sit down &mdash; grounding the promise of "
        "&lsquo;no regret&rsquo; in the ordinary mechanics of settling down "
        "to meditate."),
    guide=[
        ("A promise before the instruction", [
            "The verse opens with reassurance rather than a bare command: "
            "&lsquo;do the Buddha's bidding, you won't regret it&rsquo; "
            "&mdash; framing what follows as trustworthy before describing "
            "what it actually involves."]),
        ("An unusually concrete sequence of actions", [
            "Where most of this book's instructions describe an inner state "
            "or attitude, this verse describes a physical sequence: wash the "
            "feet, then find a discreet place, then sit to meditate &mdash; "
            "ordinary, replicable steps rather than an abstract exhortation."]),
        ("Not the famous lay patron of the same name", [
            "A laywoman named Visākhā is well known elsewhere in the canon "
            "as the Buddha's most eminent female lay supporter, famed for "
            "her wealth and generosity. This poem's Visākhā is presented "
            "here as a nun, and this reading guide treats the two as "
            "distinct individuals sharing only a name, rather than assuming "
            "an identity between them."]),
        ("Practicality as its own kind of teaching", [
            "By keeping its instruction this concrete, the verse suggests "
            "that settling the body correctly &mdash; clean feet, a private "
            "spot, an actual seated posture &mdash; is not separate from the "
            "spiritual content of practice, but part of it."]),
    ],
    terms=[
        ("Visākhā",
         "the nun this verse addresses; a laywoman of the same name is "
         "separately famous as the Buddha's most eminent female lay patron, "
         "presumably a different individual."),
        ("Buddhavacana",
         "not used directly in this translation, but the underlying idea "
         "behind &lsquo;the Buddha's bidding&rsquo; &mdash; instruction "
         "coming from the Buddha's own authority."),
        ("paṭisallāna",
         "&ldquo;seclusion&rdquo; or &ldquo;retreat&rdquo; &mdash; the "
         "underlying practice this verse's instruction to find &lsquo;a "
         "discreet place&rsquo; points toward."),
        ("bhāvanā",
         "&ldquo;meditation&rdquo; or &ldquo;development&rdquo; &mdash; "
         "named directly as what Visākhā is instructed to sit down and do."),
        ("cariyā",
         "not used here; another of this book's unattributed poems, "
         "notable for its concrete, procedural instruction."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.13:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this verse open?",
         "opts": [
             "With a warning about failure",
             "With reassurance: 'do the Buddha's bidding, you won't regret it'",
             "With a question",
             "With a description of a forest fire"],
         "correct": 1,
         "expl": "Framing the instruction as trustworthy before describing it."},
        {"q": "What kind of instruction does the rest of the verse give?",
         "opts": [
             "An abstract philosophical argument",
             "A concrete, step-by-step sequence — wash your feet, find a discreet place, sit to meditate",
             "A list of precepts to memorize",
             "No instruction is given at all"],
         "correct": 1,
         "expl": "Unusually practical compared to most of this book's more abstract verses."},
        {"q": "Is this poem's Visākhā the same person as the famous lay patron of that name?",
         "opts": [
             "Yes, definitely the same person",
             "This reading guide does not assume so — this poem presents her as a nun, likely a different individual",
             "The text explicitly states they are different",
             "The question cannot be raised at all"],
         "correct": 1,
         "expl": "Presumably distinct individuals sharing only a name."},
        {"q": "What is the famous lay Visākhā known for, elsewhere in the canon?",
         "opts": [
             "Being a hermit who avoided all society",
             "Being the Buddha's most eminent female lay patron, famed for wealth and generosity",
             "Leading a rival religious movement",
             "Nothing of particular note"],
         "correct": 1,
         "expl": "A well-known figure separate from this poem's addressee."},
        {"q": "What does the verse suggest about physical preparation for meditation?",
         "opts": [
             "That it is irrelevant to spiritual practice",
             "That settling the body correctly is presented as part of practice, not separate from it",
             "That it should be skipped entirely",
             "That only mental preparation matters"],
         "correct": 1,
         "expl": "Clean feet, a private spot, and an actual seated posture, all named directly."},
        {"q": "What does 'bhāvanā' mean?",
         "opts": [
             "'Meditation' or 'development' — what Visākhā is instructed to do",
             "'Seclusion'",
             "'Regret'",
             "'Feet'"],
         "correct": 0,
         "expl": "Named directly as the verse's closing instruction."},
        {"q": "What does 'paṭisallāna' refer to?",
         "opts": [
             "'Seclusion' or 'retreat' — the practice behind finding a discreet place",
             "'Meditation'",
             "'Regret'",
             "'Instruction'"],
         "correct": 0,
         "expl": "The underlying idea behind this verse's instruction to find a private spot."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The twelfth poem",
             "The thirteenth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Dhammadinnā's impersonal verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Visākhā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "How does this verse's approach compare to most of this book's other instructions?",
         "opts": [
             "Identical in every way",
             "More concrete and procedural, rather than describing an abstract inner state",
             "Entirely abstract, unlike any other poem",
             "This is the only poem to give any instruction at all"],
         "correct": 1,
         "expl": "A refreshingly practical exception among this book's more abstract verses."},
    ],
    marginalia=[
        ("A promise first", [
            "'you won't",
            "regret it'"
        ]),
        ("A concrete sequence", [
            "wash feet,",
            "find a spot, sit"
        ]),
        ("A different Visākhā", [
            "not the famous",
            "lay patron"
        ]),
        ("The body as practice", [
            "preparation itself",
            "part of the path"
        ]),
    ],
    further=[
        '<a href="%s/thig1.13/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.12.html">Thig 1.12 &mdash; Dhammadinn&amacr;</a> '
        "&mdash; the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.14 — Sumanā
# --------------------------------------------------------------------------- #
page(
    1, 14, "Suman&amacr;", "Suman&amacr;",
    meta_title="Thig 1.14 — Sumanā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sumanā's verse, an instruction to see the elements as suffering and "
        "discard desire for rebirth. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 14 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to the nun Sumanā"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; compact "
                       "doctrinal vocabulary in a short space"),
    ],
    why=(
        "This verse moves in three tight steps &mdash; seeing correctly, "
        "then not wishing for rebirth, then peace &mdash; addressed to a nun "
        "named Sumanā. A second, different nun of the same name appears "
        "later in this same book, distinguished there by the description "
        "&lsquo;who went forth late in life&rsquo;."),
    guide=[
        ("Seeing as the first step, not merely believing", [
            "The verse opens with perception, not doctrine stated abstractly: "
            "&lsquo;having seen the elements as suffering&rsquo; &mdash; a "
            "direct seeing is presented as the foundation the rest of the "
            "verse builds on."]),
        ("An instruction phrased as a consequence, not a command", [
            "&lsquo;Don't get reborn again&rsquo; follows the seeing "
            "described in the first line almost as a natural consequence "
            "&mdash; once the elements are truly seen as suffering, wanting "
            "further rebirth becomes the thing that no longer makes sense."]),
        ("Peace as an outcome, not a starting condition", [
            "The verse's closing promise, &lsquo;you will live at "
            "peace&rsquo;, is conditional on what comes before it: "
            "discarding desire for rebirth first, arriving at peace only "
            "afterward, not the reverse order."]),
        ("A name shared later in this same book", [
            "Thig 1.16, later in this book, is addressed to another nun also "
            "named Sumanā, there identified by the description &lsquo;who "
            "went forth late in life&rsquo; &mdash; a second instance of this "
            "book pairing two different women under one shared name, as it "
            "does with Tissā and Muttā."]),
    ],
    terms=[
        ("Sumanā",
         "a nun's name shared by a second, different woman addressed later "
         "in this book, in Thig 1.16."),
        ("khandha",
         "&ldquo;elements&rdquo; or &ldquo;aggregates&rdquo; &mdash; the "
         "components of experience this verse instructs seeing as "
         "suffering."),
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; the quality Sumanā is instructed "
         "to see the elements as having."),
        ("bhavataṇhā",
         "&ldquo;desire for rebirth&rdquo; or &ldquo;craving for "
         "existence&rdquo; &mdash; what the verse says must be discarded "
         "before peace follows."),
        ("santi",
         "&ldquo;peace&rdquo; &mdash; the verse's closing promise, "
         "conditional on the steps that come before it."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.14:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse instruct seeing the elements as?",
         "opts": [
             "As beautiful",
             "As suffering",
             "As permanent",
             "As irrelevant"],
         "correct": 1,
         "expl": "Presented as the foundation the rest of the verse builds on."},
        {"q": "How does the instruction 'don't get reborn again' relate to the first line?",
         "opts": [
             "It is entirely unrelated",
             "It follows almost as a natural consequence of truly seeing the elements as suffering",
             "It contradicts the first line",
             "It comes before the seeing described in line one"],
         "correct": 1,
         "expl": "Once the elements are truly seen this way, wanting rebirth stops making sense."},
        {"q": "In what order does the verse present discarding desire and finding peace?",
         "opts": [
             "Peace comes first, then desire is discarded",
             "Desire for rebirth is discarded first, and peace follows as a result",
             "They happen simultaneously with no order",
             "Neither is actually described"],
         "correct": 1,
         "expl": "Peace is conditional on what comes before it, not a starting condition."},
        {"q": "What other poem in this book addresses a different nun of the same name?",
         "opts": [
             "Thig 1.2",
             "Thig 1.16, addressed to a Sumanā 'who went forth late in life'",
             "Thig 1.9",
             "No other poem shares this name"],
         "correct": 1,
         "expl": "Another instance of this book pairing two different women under one name."},
        {"q": "What does 'khandha' mean?",
         "opts": [
             "'Elements' or 'aggregates' — the components of experience",
             "'Peace'",
             "'Rebirth'",
             "'Craving'"],
         "correct": 0,
         "expl": "What this verse instructs seeing as suffering."},
        {"q": "What does 'bhavataṇhā' mean?",
         "opts": [
             "'Peace'",
             "'Desire for rebirth' or 'craving for existence'",
             "'Elements'",
             "'Suffering'"],
         "correct": 1,
         "expl": "Named as what must be discarded before peace follows."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The thirteenth poem",
             "The fourteenth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Visākhā's practical instruction."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Sumanā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What does 'dukkha' mean?",
         "opts": [
             "'Suffering' — the quality the elements are to be seen as having",
             "'Peace'",
             "'Rebirth'",
             "'Restraint'"],
         "correct": 0,
         "expl": "Named directly in the verse's opening line."},
        {"q": "What structure does this verse follow?",
         "opts": [
             "A single unrelated image with no logical progression",
             "Three tight steps — seeing correctly, then not wishing for rebirth, then peace",
             "A question-and-answer format",
             "A narrative with named characters"],
         "correct": 1,
         "expl": "Each step building on the one before it."},
    ],
    marginalia=[
        ("Seeing as the first step", [
            "the elements",
            "seen as suffering"
        ]),
        ("A natural consequence", [
            "rebirth no longer",
            "makes sense"
        ]),
        ("Peace comes after", [
            "discarding desire",
            "first"
        ]),
        ("A shared name, later", [
            "another Sumanā",
            "in Thig 1.16"
        ]),
    ],
    further=[
        '<a href="%s/thig1.14/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.13.html">Thig 1.13 &mdash; Vis&amacr;kh&amacr;</a> '
        "&mdash; the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.15 — Uttarā (1st)
# --------------------------------------------------------------------------- #
page(
    1, 15, "Uttar&amacr;", "Uttar&amacr; (1st)",
    meta_title="Thig 1.15 — Uttarā (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Uttarā's verse, a first-person report of restraint and craving "
        "uprooted, closing in the same image as Thig 1.16. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 15 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "The nun Uttarā, speaking entirely in the first person"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short "
                       "and direct, a personal report rather than an "
                       "instruction"),
    ],
    why=(
        "Where several of this book's poems instruct a nun toward a goal, "
        "this one reports an achievement already reached, in the first "
        "person: restraint practiced across body, speech, and mind, craving "
        "pulled out entirely, ending in the same image of coolness that "
        "closes Thig 1.16, later in this book."),
    guide=[
        ("Restraint named across three domains at once", [
            "Uttarā's report is comprehensive rather than partial: "
            "&lsquo;restrained in body, speech, and mind&rsquo; names all "
            "three channels of action the tradition typically distinguishes, "
            "not just one."]),
        ("Craving described as uprooted, not merely reduced", [
            "The verse's central image is agricultural and total: "
            "&lsquo;having plucked out craving, root and all&rsquo; &mdash; "
            "not trimmed or weakened, but removed entirely, leaving nothing "
            "to regrow."]),
        ("A closing image shared with a later poem", [
            "&lsquo;I'm cooled and quenched&rsquo; closes this verse in "
            "language nearly identical to Thig 1.16's closing line, &lsquo;you're "
            "cooled and quenched&rsquo; &mdash; the same state of "
            "extinguishment, described here in the first person rather than "
            "as an instruction."]),
        ("The title '(1st)' signaling more to come", [
            "As with Muttā and the two Tissās, the numbered title implies "
            "another Uttarā appears elsewhere in the wider collection "
            "&mdash; a common pattern across the Therigatha, where several "
            "names recur among the many women whose verses it preserves."]),
    ],
    terms=[
        ("Uttarā",
         "this verse's speaker, distinguished by the title &lsquo;(1st)&rsquo; "
         "from at least one other woman of the same name elsewhere in the "
         "wider collection."),
        ("saṁvara",
         "&ldquo;restraint&rdquo; &mdash; named across the three domains of "
         "body, speech, and mind in this verse's opening line."),
        ("taṇhā",
         "&ldquo;craving&rdquo; &mdash; described here as plucked out "
         "&lsquo;root and all&rsquo;, the central image of this verse."),
        ("sīti-bhūta",
         "&ldquo;cooled&rdquo; &mdash; part of the closing phrase "
         "&lsquo;cooled and quenched&rsquo;, shared with Thig 1.16."),
        ("nibbuta",
         "&ldquo;quenched&rdquo; &mdash; the second half of that closing "
         "phrase, describing extinguishment achieved."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.15:1.1-1.4"),
    ],
    quiz=[
        {"q": "In what tense and person is this verse spoken?",
         "opts": [
             "Second person, addressing Uttarā directly",
             "First person, reporting Uttarā's own achievement",
             "Third person, describing Uttarā from outside",
             "The verse has no clear speaker"],
         "correct": 1,
         "expl": "An achievement already reached, not an instruction toward one."},
        {"q": "How many domains of restraint does the verse name?",
         "opts": [
             "One",
             "Three — body, speech, and mind",
             "Five",
             "None; restraint is not mentioned"],
         "correct": 1,
         "expl": "A comprehensive report, not a partial one."},
        {"q": "How does the verse describe craving being dealt with?",
         "opts": [
             "Gradually reduced over time",
             "Plucked out root and all — removed entirely",
             "Temporarily suppressed",
             "Craving is not mentioned"],
         "correct": 1,
         "expl": "An agricultural image of total removal, not partial trimming."},
        {"q": "What phrase closes this verse, echoed in Thig 1.16?",
         "opts": [
             "'Sanctuary from the yoke'",
             "'I'm cooled and quenched'",
             "'Free of debt'",
             "'Heading upstream'"],
         "correct": 1,
         "expl": "Nearly identical to Thig 1.16's closing line, though here in the first person."},
        {"q": "What does the title '(1st)' after Uttarā's name suggest?",
         "opts": [
             "Nothing in particular",
             "That another woman of the same name appears elsewhere in the wider collection",
             "That this is the very first poem in the entire Therigatha",
             "That Uttarā composed exactly one other verse"],
         "correct": 1,
         "expl": "A common pattern in the Therigatha, where several names recur."},
        {"q": "What does 'taṇhā' mean?",
         "opts": [
             "'Restraint'",
             "'Craving' — described as plucked out root and all",
             "'Coolness'",
             "'Quenching'"],
         "correct": 1,
         "expl": "The central image of this verse's second line."},
        {"q": "What does 'saṁvara' mean?",
         "opts": [
             "'Restraint' — named across body, speech, and mind",
             "'Craving'",
             "'Quenching'",
             "'Coolness'"],
         "correct": 0,
         "expl": "The comprehensive report opening this verse."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The fourteenth poem",
             "The fifteenth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following Sumanā's verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Uttarā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What does 'nibbuta' mean?",
         "opts": [
             "'Quenched' — describing extinguishment achieved",
             "'Restrained'",
             "'Craving'",
             "'Elements'"],
         "correct": 0,
         "expl": "The second half of this verse's closing phrase."},
    ],
    marginalia=[
        ("Three domains at once", [
            "body, speech,",
            "and mind restrained"
        ]),
        ("Uprooted, not trimmed", [
            "craving plucked out,",
            "root and all"
        ]),
        ("The same close as Thig 1.16", [
            "'cooled",
            "and quenched'"
        ]),
        ("More Uttarās to come", [
            "'(1st)' signals",
            "another elsewhere"
        ]),
    ],
    further=[
        '<a href="%s/thig1.15/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.14.html">Thig 1.14 &mdash; Suman&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.16 — Sumanā, Who Went Forth Late in Life
# --------------------------------------------------------------------------- #
page(
    1, 16, "Suman&amacr;", "Suman&amacr;, Who Went Forth Late in Life",
    meta_title="Thig 1.16 — Sumanā, Who Went Forth Late in Life | Ru-Yi "
                "Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for this "
        "second Sumanā's verse, echoing the Therigatha's opening poem almost "
        "word for word for an old woman rather than a young one. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 16 of 18",
    glance=[
        ("Setting", "No narrative setting; no closing attribution"),
        ("Speaker", "Not identified; direct address to a second nun also "
                    "named Sumanā, distinguished by ordaining late in life"),
        ("Form", "A single four-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; simple "
                       "in isolation, striking when read against Thig 1.1"),
    ],
    why=(
        "This poem repeats the Therigatha's very first verse almost word "
        "for word &mdash; but addresses an old woman rather than the "
        "unnamed &lsquo;little nun&rsquo; of Thig 1.1, and closes on a "
        "different final line. Near the end of the Book of the Ones, the "
        "collection reaches back to echo its own opening."),
    guide=[
        ("The same lullaby, a different age", [
            "&lsquo;Sleep softly&rsquo;, &lsquo;wrapped in the cloth you "
            "sewed yourself&rsquo;, &lsquo;your desire has been quelled&rsquo; "
            "&mdash; three lines shared almost exactly with Thig 1.1, with "
            "one substitution: &lsquo;little nun&rsquo; becomes &lsquo;old "
            "lady&rsquo;."]),
        ("A closing line that changes the image entirely", [
            "Where Thig 1.1 closed with vegetables boiled dry in a pot, this "
            "verse closes plainly: &lsquo;you're cooled and quenched&rsquo; "
            "&mdash; stating the attainment directly rather than through "
            "metaphor, the same phrase closing Thig 1.15's first-person "
            "report."]),
        ("A title naming the distinguishing fact plainly", [
            "This poem's title does not simply repeat the name Sumanā from "
            "Thig 1.14; it adds &lsquo;who went forth late in life&rsquo; "
            "&mdash; identifying her by the timing of her ordination, a "
            "detail the collection considers worth preserving."]),
        ("Two lullabies bracketing most of this book", [
            "Thig 1.1 opens the Book of the Ones and this poem sits near its "
            "close, both using the same tender, second-person lullaby form "
            "&mdash; a structural echo across the book's first sixteen "
            "poems, before the book's final two verses shift into extended "
            "first-person testimony."]),
    ],
    terms=[
        ("Sumanā",
         "a name shared with Thig 1.14's addressee; this poem's title "
         "distinguishes this second Sumanā by noting she went forth late in "
         "life."),
        ("pabbajjā",
         "&ldquo;going forth&rdquo; &mdash; the act this poem's title says "
         "this Sumanā undertook later than most, rather than in youth."),
        ("sīti-bhūta, nibbuta",
         "&ldquo;cooled&rdquo; and &ldquo;quenched&rdquo; &mdash; the same "
         "closing pair of terms used in Thig 1.15, here replacing Thig "
         "1.1's vegetable image."),
        ("cīvara",
         "&ldquo;robe&rdquo; or &ldquo;cloth&rdquo; &mdash; the "
         "self-sewn covering named in this verse's second line, shared word "
         "for word with Thig 1.1."),
        ("cariyā",
         "not used here; another of this book's unattributed poems, "
         "notable chiefly for its close echo of the book's opening verse."),
    ],
    text_intro=(
        "The text in full: a single four-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.16:1.1-1.4"),
    ],
    quiz=[
        {"q": "How closely does this poem's wording match Thig 1.1's?",
         "opts": [
             "Not at all similar",
             "Nearly identical for three lines, with 'little nun' changed to 'old lady'",
             "Identical in every single word, with no change at all",
             "Only the general theme is similar, no shared wording"],
         "correct": 1,
         "expl": "A close echo, but not a perfect repetition."},
        {"q": "How does this poem's closing line differ from Thig 1.1's?",
         "opts": [
             "It is identical to Thig 1.1's closing line",
             "It states the attainment directly ('cooled and quenched') rather than using Thig 1.1's vegetable image",
             "It has no closing line at all",
             "It adds an extra two lines not found in Thig 1.1"],
         "correct": 1,
         "expl": "A different final image, shared instead with Thig 1.15's closing phrase."},
        {"q": "What does this poem's title add to the name 'Sumanā'?",
         "opts": [
             "Nothing further",
             "'Who went forth late in life' — identifying her by the timing of her ordination",
             "Her family's name",
             "The city she was born in"],
         "correct": 1,
         "expl": "Distinguishing her from Thig 1.14's Sumanā."},
        {"q": "What structural pattern do Thig 1.1 and this poem form together?",
         "opts": [
             "No particular pattern",
             "Two lullaby-form poems bracketing most of the Book of the Ones",
             "They directly contradict each other",
             "They are actually the same poem duplicated by mistake"],
         "correct": 1,
         "expl": "A structural echo across the book's first sixteen poems."},
        {"q": "What phrase does this poem share with Thig 1.15's closing line?",
         "opts": [
             "'Sanctuary from the yoke'",
             "'Cooled and quenched'",
             "'Free of debt'",
             "'Heading upstream'"],
         "correct": 1,
         "expl": "The same closing image, here in second person rather than first."},
        {"q": "What does 'pabbajjā' mean?",
         "opts": [
             "'Going forth' — the act of renunciation this Sumanā undertook late in life",
             "'Cloth' or 'robe'",
             "'Cooled'",
             "'Quenched'"],
         "correct": 0,
         "expl": "Named in this poem's distinguishing title, not within the verse itself."},
        {"q": "What object is named in this verse's second line, shared word for word with Thig 1.1?",
         "opts": [
             "A begging bowl",
             "The cloth she sewed herself",
             "A walking staff",
             "A meditation mat"],
         "correct": 1,
         "expl": "One of the lines repeated almost exactly from the book's opening poem."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The fifteenth poem",
             "The sixteenth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following the first Uttarā's verse, near the book's close."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Sumanā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What does this poem's echo of Thig 1.1 suggest about the book's structure?",
         "opts": [
             "The book has no discernible structure at all",
             "The collection can deliberately reach back to echo its own opening near a book's close",
             "It proves the two poems were composed by the same author",
             "It has no significance beyond coincidence"],
         "correct": 1,
         "expl": "A structural echo worth noticing, whatever its original compositional history."},
    ],
    marginalia=[
        ("A near-repeat of Thig 1.1", [
            "'little nun' becomes",
            "'old lady'"
        ]),
        ("A different closing line", [
            "stated directly,",
            "not through image"
        ]),
        ("Ordained late in life", [
            "the title names",
            "this distinguishing fact"
        ]),
        ("Two lullabies, one book", [
            "bracketing most",
            "of the Book of the Ones"
        ]),
    ],
    further=[
        '<a href="%s/thig1.16/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.15.html">Thig 1.15 &mdash; Uttar&amacr; (1st)</a> '
        "&mdash; the text immediately before this one, sharing this poem's "
        "closing phrase.",
        '<a href="thig-1.1.html">Thig 1.1 &mdash; An Unnamed Nun</a> &mdash; '
        "the collection's opening poem, echoed closely here.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.17 — Dhammā
# --------------------------------------------------------------------------- #
page(
    1, 17, "Dhamm&amacr;", "Dhamm&amacr;",
    meta_title="Thig 1.17 — Dhammā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Dhammā's verse, a first-person account of a fall while begging for "
        "alms that leads directly to insight. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 17 of 18",
    glance=[
        ("Setting", "No narrative frame beyond what the verse itself "
                    "describes; no closing attribution"),
        ("Speaker", "The nun Dhammā, speaking entirely in the first person "
                    "about a specific incident"),
        ("Form", "A single six-line verse, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "concrete physical incident, not an abstract "
                       "instruction"),
    ],
    why=(
        "Unlike most of this book's poems, which give instruction or state "
        "an attainment without describing how it came about, this verse "
        "narrates a specific physical event: a feeble, staff-leaning nun "
        "wanders for alms, her limbs give out, and she falls &mdash; and it "
        "is precisely this fall that becomes the occasion for insight."),
    guide=[
        ("Frailty stated plainly, not minimized", [
            "The verse opens with an honest description of physical "
            "weakness: &lsquo;I wandered for alms though feeble, leaning on "
            "a staff&rsquo; &mdash; the difficulty of the alms round for an "
            "aging or unwell body stated without embellishment."]),
        ("A fall described without drama", [
            "&lsquo;My limbs wobbled and I fell to the ground right "
            "there&rsquo; &mdash; a plain, almost matter-of-fact account of "
            "an ordinary physical failure, not treated as a tragedy or a "
            "trial to be overcome."]),
        ("The fall itself as the turning point", [
            "The verse's final lines make the connection explicit: "
            "&lsquo;seeing the danger of the body, my mind was freed&rsquo; "
            "&mdash; the very moment of physical failure becomes the "
            "occasion for seeing the body's vulnerability clearly enough to "
            "let go of it."]),
        ("Insight through the body, not despite it", [
            "This poem offers a different route to the same destination "
            "described elsewhere in this book: not through instruction "
            "received, or a name's meaning turned into practice, but "
            "through a specific bodily experience recognized clearly in the "
            "moment it happened."]),
    ],
    terms=[
        ("Dhammā",
         "this verse's speaker, a nun who describes a specific fall while "
         "on the alms round."),
        ("piṇḍapāta",
         "&ldquo;the alms round&rdquo; &mdash; the activity Dhammā was "
         "engaged in, described here as physically demanding for someone "
         "feeble."),
        ("kāyassa ādīnava",
         "&ldquo;the danger of the body&rdquo; &mdash; what this verse says "
         "Dhammā saw clearly at the moment of her fall, the direct trigger "
         "for her freedom."),
        ("daṇḍa",
         "&ldquo;staff&rdquo; &mdash; the support Dhammā is described "
         "leaning on, indicating age or physical weakness before her fall."),
        ("cariyā",
         "not used here; another of this book's unattributed poems, "
         "distinctive for narrating a specific incident rather than stating "
         "an instruction or attainment alone."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.17:1.1-1.6"),
    ],
    quiz=[
        {"q": "What activity is Dhammā engaged in at the start of this verse?",
         "opts": [
             "Meditating in a hermitage",
             "Wandering for alms, though feeble and leaning on a staff",
             "Teaching a group of nuns",
             "Traveling to visit her family"],
         "correct": 1,
         "expl": "Physical weakness stated plainly, without embellishment."},
        {"q": "What specific event does the verse describe?",
         "opts": [
             "A conversation with the Buddha",
             "Her limbs wobbling and her falling to the ground",
             "A dream she had",
             "An attack by bandits"],
         "correct": 1,
         "expl": "A plain, matter-of-fact account of an ordinary physical failure."},
        {"q": "What does the fall become the occasion for?",
         "opts": [
             "Nothing further; the verse simply ends there",
             "Seeing the danger of the body clearly, leading directly to freedom",
             "A request for help from other nuns",
             "A decision to stop wandering for alms"],
         "correct": 1,
         "expl": "The moment of physical failure becomes the trigger for insight."},
        {"q": "How does this poem's route to insight differ from most others in this book?",
         "opts": [
             "It is identical to every other poem's route",
             "It comes through a specific bodily experience, rather than instruction received or a name's meaning",
             "This poem describes no insight at all",
             "It comes through a dream rather than a waking event"],
         "correct": 1,
         "expl": "A concrete physical incident recognized clearly in the moment, not an abstract instruction."},
        {"q": "What does 'kāyassa ādīnava' mean?",
         "opts": [
             "'The danger of the body' — what Dhammā saw at the moment of her fall",
             "'The alms round'",
             "'Staff'",
             "'Wandering'"],
         "correct": 0,
         "expl": "Named directly as the trigger for her freedom."},
        {"q": "What does the staff mentioned in this verse indicate about Dhammā?",
         "opts": [
             "Wealth and status",
             "Age or physical weakness",
             "A specific monastic rank",
             "Nothing in particular"],
         "correct": 1,
         "expl": "A support needed because of frailty, before her fall."},
        {"q": "How long is this poem, compared to the book's typical four-line verses?",
         "opts": [
             "Exactly four lines, the book's standard length",
             "Six lines, slightly longer than typical",
             "Twenty lines",
             "A single line only"],
         "correct": 1,
         "expl": "One of a small number of slightly longer poems in this book, like Thig 1.11."},
        {"q": "What position does this poem hold in the Book of the Ones?",
         "opts": [
             "The sixteenth poem",
             "The seventeenth poem",
             "The last poem",
             "It is not part of the Book of the Ones"],
         "correct": 1,
         "expl": "Following the second Sumanā's verse, near the book's very close."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Dhammā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What tone does the verse take toward Dhammā's fall?",
         "opts": [
             "Treated as a tragedy to be mourned",
             "Described plainly, almost matter-of-factly, not dramatized",
             "Treated as a punishment for wrongdoing",
             "The fall is described with great alarm and fear"],
         "correct": 1,
         "expl": "An ordinary event that becomes significant through what it reveals, not through drama."},
    ],
    marginalia=[
        ("Frailty, stated plainly", [
            "feeble, leaning",
            "on a staff"
        ]),
        ("A fall, without drama", [
            "limbs wobbled,",
            "she fell"
        ]),
        ("The fall as the turning point", [
            "the body's danger",
            "seen clearly"
        ]),
        ("Insight through the body", [
            "a specific moment,",
            "not an abstraction"
        ]),
    ],
    further=[
        '<a href="%s/thig1.17/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.16.html">Thig 1.16 &mdash; Suman&amacr;, Who Went '
        "Forth Late in Life</a> &mdash; the text immediately before this "
        "one, also concerned with the frailty of an aging body.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 1.18 — Saṅghā
# --------------------------------------------------------------------------- #
page(
    1, 18, "Sa&#7749;gh&amacr;", "Sa&#7749;gh&amacr;",
    meta_title="Thig 1.18 — Saṅghā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Saṅghā's verse, closing the Book of the Ones with an explicit, "
        "unsoftened account of giving up a child to go forth. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Poem 18 of 18",
    glance=[
        ("Setting", "No narrative setting beyond what the verse itself "
                    "states; no closing attribution"),
        ("Speaker", "The nun Saṅghā, speaking entirely in the first person"),
        ("Form", "A single six-line verse, closing the Book of the Ones"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this poem in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, "
                       "but naming a real and difficult cost directly"),
    ],
    why=(
        "This poem closes the Book of the Ones, and it does not soften what "
        "renunciation actually meant for its speaker: Saṅghā names her "
        "home, her cattle &mdash; and her child &mdash; among what she gave "
        "up to go forth, stated in the same breath and without any special "
        "pleading or justification attached."),
    guide=[
        ("A list that does not spare its hardest item", [
            "&lsquo;I gave up my home, my child, my cattle, and all that I "
            "love&rsquo; &mdash; the child is named directly within a list "
            "of possessions and property, neither singled out for special "
            "grief nor omitted out of discretion."]),
        ("Renunciation as loss, not only gain", [
            "Where several poems in this book describe renunciation "
            "primarily as arriving at something &mdash; peace, freedom, "
            "extinguishment &mdash; this verse opens by naming what leaving "
            "required giving up first, cost stated before attainment."]),
        ("The same uprooting image as Thig 1.15", [
            "&lsquo;Plucked out craving, root and all&rsquo; repeats Thig "
            "1.15's exact image for the total removal of craving &mdash; the "
            "same phrase closing the book that it appeared partway "
            "through."]),
        ("A closing poem that closes on repetition, not novelty", [
            "The Book of the Ones ends not with a new image but with "
            "&lsquo;I'm at peace, I'm quenched&rsquo; &mdash; language "
            "closely echoing several other poems in this same book, "
            "suggesting a shared destination reached by many different "
            "roads, including the difficult one this final poem names "
            "directly."]),
    ],
    terms=[
        ("Saṅghā",
         "this verse's speaker, whose name shares its root with "
         "&lsquo;saṅgha&rsquo;, the monastic community."),
        ("putta",
         "&ldquo;child&rdquo; &mdash; named directly among what Saṅghā gave "
         "up to go forth, alongside her home and cattle."),
        ("avijjā",
         "&ldquo;ignorance&rdquo; &mdash; named as dispelled in this verse's "
         "closing lines, the same obstacle named in Thig 1.3's image of "
         "shattered darkness."),
        ("taṇhā",
         "&ldquo;craving&rdquo; &mdash; described here, as in Thig 1.15, as "
         "&lsquo;plucked out, root and all&rsquo;."),
        ("santi, nibbuta",
         "&ldquo;peace&rdquo; and &ldquo;quenched&rdquo; &mdash; the pair of "
         "terms closing this final poem of the Book of the Ones, echoing "
         "language used across several earlier poems in the same book."),
    ],
    text_intro=(
        "The text in full: a single six-line verse, closing the Book of the "
        "Ones. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig1.18:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does Saṅghā name among what she gave up to go forth?",
         "opts": [
             "Only material possessions, no family",
             "Her home, her child, her cattle, and all that she loves",
             "Nothing is named specifically",
             "Only her reputation"],
         "correct": 1,
         "expl": "The child named directly, without being singled out or omitted."},
        {"q": "How does the verse treat the mention of her child?",
         "opts": [
             "With extensive, dramatized grief",
             "Within the same list as her home and cattle, without special pleading",
             "The child is not mentioned at all",
             "As a source of shame to be hidden"],
         "correct": 1,
         "expl": "Stated plainly, neither singled out for grief nor omitted out of discretion."},
        {"q": "How does this poem's structure differ from several others in this book?",
         "opts": [
             "It is identical to every other poem's structure",
             "It opens by naming what was given up, cost stated before attainment, rather than describing arrival at peace alone",
             "It contains no mention of any attainment at all",
             "It is written entirely in the third person"],
         "correct": 1,
         "expl": "Renunciation presented as loss as well as gain."},
        {"q": "What phrase does this poem share word for word with Thig 1.15?",
         "opts": [
             "'Sanctuary from the yoke'",
             "'Plucked out craving, root and all'",
             "'Free of debt'",
             "'Heading upstream'"],
         "correct": 1,
         "expl": "The same total-removal image used earlier in the book."},
        {"q": "What position does this poem hold in the Therigatha?",
         "opts": [
             "It opens the entire collection",
             "It closes the Book of the Ones, the collection's first book",
             "It is the collection's final poem overall",
             "It is not part of any book"],
         "correct": 1,
         "expl": "The eighteenth and last poem of the first of the Therigatha's many books."},
        {"q": "What does 'putta' mean?",
         "opts": [
             "'Cattle'",
             "'Child' — named directly among what was given up",
             "'Home'",
             "'Craving'"],
         "correct": 1,
         "expl": "Stated without euphemism in this verse's opening list."},
        {"q": "What does this poem's closing language suggest about the destination it describes?",
         "opts": [
             "That it is entirely unique to Saṅghā, unlike any other poem",
             "That it echoes language used across several earlier poems, suggesting a shared destination reached by different roads",
             "That the destination is left ambiguous",
             "That the poem contradicts the rest of the book"],
         "correct": 1,
         "expl": "Peace and quenching, described in terms close to several other poems in this same book."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Saṅghā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "Continuing the bare, unattributed pattern of several poems in this book."},
        {"q": "What does Saṅghā's name share its root with?",
         "opts": [
             "'Craving'",
             "'Saṅgha', the monastic community",
             "'Ignorance'",
             "'Child'"],
         "correct": 1,
         "expl": "A name closely tied to the community she joined by going forth."},
        {"q": "What overall impression does this closing poem leave about the Book of the Ones?",
         "opts": [
             "That renunciation was always effortless for these women",
             "That renunciation carried real, specific costs, honestly named, alongside its rewards",
             "That the book has no coherent theme at all",
             "That only wealthy women appear in this collection"],
         "correct": 1,
         "expl": "A closing note that neither hides nor dwells on what was given up."},
    ],
    marginalia=[
        ("A hard list, unsoftened", [
            "home, child, cattle —",
            "named together"
        ]),
        ("Loss before attainment", [
            "cost stated",
            "first"
        ]),
        ("Echoing Thig 1.15", [
            "craving plucked out,",
            "root and all"
        ]),
        ("A shared destination", [
            "peace and quenching,",
            "reached by many roads"
        ]),
    ],
    further=[
        '<a href="%s/thig1.18/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.17.html">Thig 1.17 &mdash; Dhamm&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="thig-1.1.html">Thig 1.1 &mdash; An Unnamed Nun</a> &mdash; '
        "the poem opening the book this one closes.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)
