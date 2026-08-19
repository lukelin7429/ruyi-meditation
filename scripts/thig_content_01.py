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


# --------------------------------------------------------------------------- #
# Thig 2.1 — Abhirūpanandā
# --------------------------------------------------------------------------- #
page(
    2, 1, "Abhir&umacr;panand&amacr;", "Abhir&umacr;panand&amacr;",
    meta_title="Thig 2.1 — Abhirūpanandā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Abhirūpanandā's verses, opening the Book of the Twos with a "
        "direct instruction toward meditation on the body's ugliness. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; a "
                    "closing attribution names speaker and occasion"),
        ("Speaker", "The Buddha, addressing the trainee nun Nandā by name"),
        ("Form", "Two four-line verses, with a closing attribution note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Later commentarial tradition associates this "
                              "nun with a striking story about vanity and "
                              "shock; this reading guide does not assert "
                              "this verse itself has a specific matching "
                              "text."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct, "
                       "unflinching body-contemplation instruction"),
    ],
    why=(
        "The Book of the Twos opens with two verses of unusually direct "
        "instruction: Nandā is told to see her own body as &lsquo;a bag of "
        "bones... diseased, filthy, and rotten&rsquo;. Her fuller title, "
        "Abhirūpanandā, means roughly &lsquo;Nandā the beautiful&rsquo; "
        "&mdash; and later commentarial tradition holds that this exact "
        "instruction was aimed precisely at a woman known for vanity about "
        "her own appearance."),
    guide=[
        ("A name that names her beauty first", [
            "&lsquo;Abhirūpanandā&rsquo; combines Nandā's name with "
            "<em>abhirūpa</em>, &lsquo;beautiful&rsquo; or "
            "&lsquo;attractive&rsquo; &mdash; the title itself identifies "
            "her by an attribute the verses' instruction works directly "
            "against."]),
        ("An unflinching image, not a gentle metaphor", [
            "Where several Book of the Ones poems used gentle astronomical "
            "images (the moon, an eclipse), this instruction is bodily and "
            "blunt: &lsquo;this bag of bones&rsquo;, &lsquo;diseased, "
            "filthy, and rotten&rsquo; &mdash; a form of meditation on the "
            "body's less flattering aspects, deployed deliberately."]),
        ("From the ugly body to the signless", [
            "The second verse moves from contemplating the body's aspects "
            "to a different object of meditation entirely: &lsquo;the "
            "signless&rsquo;, paired with giving up &lsquo;the tendency to "
            "conceit&rsquo; &mdash; the specific antidote named for the "
            "specific attachment the title's name implies."]),
        ("A commentarial story behind a spare verse", [
            "Later tradition tells a fuller story of a nun reluctant to "
            "face the Buddha's teaching for fear it would target her pride "
            "in her looks, eventually confronted with a vision of beauty "
            "aging into decay. This verse itself states none of that "
            "narrative directly &mdash; only the instruction survives here."]),
    ],
    terms=[
        ("Nandā",
         "the trainee nun addressed in these verses, whose fuller title, "
         "Abhirūpanandā, combines her name with a word for beauty."),
        ("asubha",
         "&ldquo;the unattractive&rdquo; or &ldquo;foulness&rdquo; "
         "&mdash; the broad category of meditation this verse's body-focused "
         "instruction belongs to."),
        ("animitta",
         "&ldquo;the signless&rdquo; &mdash; a meditation object named in "
         "this verse's second half, distinct from the body-contemplation of "
         "the first."),
        ("māna",
         "&ldquo;conceit&rdquo; &mdash; what Nandā is instructed to give up "
         "and comprehend, the attachment the title's name most directly "
         "implicates."),
        ("sekha",
         "a &ldquo;trainee&rdquo; &mdash; the stage of practice this "
         "verse's attribution describes Nandā as being in when addressed."),
    ],
    text_intro=(
        "The text in full: two verses, with a closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.1:1.1-1.4"),
        ("p", "&sect;2", "thig2.1:2.1-2.4"),
        ("p", "&sect;3", "thig2.1:3.1-3.1"),
    ],
    quiz=[
        {"q": "What does the title 'Abhirūpanandā' mean?",
         "opts": [
             "'Nandā the wise'",
             "Roughly 'Nandā the beautiful', combining her name with a word for beauty",
             "'Nandā the wanderer'",
             "The title has no particular meaning"],
         "correct": 1,
         "expl": "A title identifying her by an attribute the instruction works directly against."},
        {"q": "How does the first verse instruct Nandā to see her own body?",
         "opts": [
             "As a source of pride",
             "As 'a bag of bones... diseased, filthy, and rotten'",
             "As irrelevant to practice",
             "As beautiful and worth preserving"],
         "correct": 1,
         "expl": "A blunt, unflinching image compared to several Book of the Ones' gentler metaphors."},
        {"q": "What second object of meditation does the verse introduce after the body?",
         "opts": [
             "The breath alone",
             "The signless (animitta)",
             "A specific mantra",
             "No second object is introduced"],
         "correct": 1,
         "expl": "Paired with giving up the tendency to conceit."},
        {"q": "What does later commentarial tradition say about this instruction's background?",
         "opts": [
             "Nothing further is ever said",
             "That it was aimed at a nun reluctant to face teaching for fear it would target her pride in her looks",
             "That it was originally addressed to a king",
             "That the verse is unrelated to any particular person"],
         "correct": 1,
         "expl": "A story this verse itself does not narrate directly."},
        {"q": "Who does the closing attribution credit as this verse's speaker?",
         "opts": [
             "Nandā herself",
             "The Buddha, who 'regularly advised' the trainee nun Nandā",
             "An unnamed nun",
             "No speaker is credited"],
         "correct": 1,
         "expl": "The same 'regularly advised' phrasing used for Muttā in Thig 1.2."},
        {"q": "What does 'māna' mean?",
         "opts": [
             "'Conceit' — the attachment Nandā is told to give up and comprehend",
             "'Beauty'",
             "'The signless'",
             "'Bag of bones'"],
         "correct": 0,
         "expl": "The attachment the title's name most directly implicates."},
        {"q": "What broader category of meditation does this verse's body instruction belong to?",
         "opts": [
             "Asubha, meditation on the unattractive or foulness",
             "Mettā, loving-kindness meditation",
             "Ānāpānasati, breath meditation",
             "No specific category is named"],
         "correct": 0,
         "expl": "A well-established meditation category the verse's imagery draws on."},
        {"q": "How does this verse's approach compare to most of the Book of the Ones' gentler images?",
         "opts": [
             "Identical in tone throughout",
             "More blunt and bodily, rather than relying on astronomical or gentle metaphors",
             "Even gentler than the Book of the Ones",
             "This verse contains no imagery at all"],
         "correct": 1,
         "expl": "Contrasted directly with images like the moon and an eclipse."},
        {"q": "What position does this poem hold in the Therigatha?",
         "opts": [
             "It closes the Book of the Ones",
             "It opens the Book of the Twos, the collection's second book",
             "It is the collection's final poem",
             "It is not part of any book"],
         "correct": 1,
         "expl": "The first poem of ten in this second book."},
        {"q": "What does 'sekha' mean?",
         "opts": [
             "'Trainee' — the stage of practice Nandā is described as being in",
             "'Beautiful'",
             "'Conceit'",
             "'Signless'"],
         "correct": 0,
         "expl": "Named in the closing attribution, matching the pattern seen with Muttā in Thig 1.2."},
    ],
    marginalia=[
        ("A name naming beauty", [
            "'Abhirūpanandā' —",
            "the very attribute targeted"
        ]),
        ("An unflinching image", [
            "'diseased, filthy,",
            "and rotten'"
        ]),
        ("A second object", [
            "from the body",
            "to the signless"
        ]),
        ("A story behind the verse", [
            "commentary tells more",
            "than these lines state"
        ]),
    ],
    further=[
        '<a href="%s/thig2.1/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-1.18.html">Thig 1.18 &mdash; Sa&#7749;gh&amacr;</a> '
        "&mdash; the text immediately before this one, closing the Book of "
        "the Ones.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.2 — Jentā
# --------------------------------------------------------------------------- #
page(
    2, 2, "Jent&amacr;", "Jent&amacr;",
    meta_title="Thig 2.2 — Jentā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jentā's verses, a first-person account of developing the seven "
        "awakening factors to their completion. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Twos &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; a "
                    "closing attribution names the speaker"),
        ("Speaker", "The senior nun Jentā, speaking entirely in the first "
                    "person"),
        ("Form", "Two four-line verses, with a closing attribution note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; names a "
                       "specific doctrinal list by number"),
    ],
    why=(
        "Where Thig 2.1 gave an instruction still to be followed, this "
        "verse reports a specific, named practice already completed: Jentā "
        "states she has developed all seven of the awakening factors "
        "&mdash; not vaguely, but naming the number and the source, "
        "&lsquo;just as the Buddha taught&rsquo;."),
    guide=[
        ("A specific doctrinal list, named and counted", [
            "Jentā's report is precise: &lsquo;of the seven awakening "
            "factors... I have developed them all&rsquo; &mdash; not a "
            "general claim of progress, but a specific, countable list "
            "stated as complete."]),
        ("Attributed directly to the Buddha's own teaching", [
            "The verse credits its method explicitly: &lsquo;just as the "
            "Buddha taught&rsquo; &mdash; crediting a specific source for "
            "the path followed, rather than presenting the attainment as "
            "self-derived."]),
        ("A body already described as final", [
            "&lsquo;This bag of bones is my last&rsquo; echoes the same "
            "phrase used to instruct Nandā in Thig 2.1, but here spoken in "
            "the first person about an already-final body, not as an "
            "instruction toward seeing it that way."]),
        ("A closing claim about the future itself", [
            "The verse ends with the clearest possible statement about what "
            "comes next: &lsquo;transmigration through births is finished, "
            "now there'll be no more future lives&rsquo; &mdash; not "
            "hopeful language, but a flat declaration."]),
    ],
    terms=[
        ("Jentā",
         "the senior nun (therī) this verse's closing attribution credits "
         "as its speaker."),
        ("bojjhaṅga",
         "the &ldquo;awakening factors&rdquo;, seven qualities "
         "(mindfulness, investigation, energy, joy, tranquility, "
         "immersion, and equanimity) traditionally cultivated together on "
         "the path."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; named directly as the goal "
         "the seven awakening factors are described as the path toward."),
        ("aṭṭhimasañcayo",
         "&ldquo;this bag of bones&rdquo; &mdash; the same phrase used in "
         "Thig 2.1's instruction to Nandā, here describing Jentā's own "
         "final body."),
        ("cariyā",
         "not used here; this poem, like most in the Therigatha, closes "
         "with a simple attribution note rather than a formula naming a "
         "perfection."),
    ],
    text_intro=(
        "The text in full: two verses, with a closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.2:1.1-1.4"),
        ("p", "&sect;2", "thig2.2:2.1-2.4"),
        ("p", "&sect;3", "thig2.2:3.1-3.1"),
    ],
    quiz=[
        {"q": "What specific doctrinal list does Jentā say she has developed in full?",
         "opts": [
             "The five precepts",
             "The seven awakening factors",
             "The four noble truths",
             "No specific list is named"],
         "correct": 1,
         "expl": "A precise, countable claim, not a vague statement of progress."},
        {"q": "What source does the verse credit for this method?",
         "opts": [
             "Jentā's own independent discovery",
             "'Just as the Buddha taught' — an explicit, named source",
             "A teacher who is never identified",
             "No source is credited"],
         "correct": 1,
         "expl": "The path is credited directly, not presented as self-derived."},
        {"q": "What phrase does this verse share with Thig 2.1's instruction to Nandā?",
         "opts": [
             "'The signless'",
             "'This bag of bones'",
             "'Fulfilled the Buddha's instructions'",
             "No phrase is shared"],
         "correct": 1,
         "expl": "Here describing Jentā's own already-final body, not as an instruction."},
        {"q": "How does the verse describe the future, in its closing lines?",
         "opts": [
             "With uncertainty about what comes next",
             "Flatly: 'transmigration through births is finished, now there'll be no more future lives'",
             "As an open question",
             "The future is not addressed"],
         "correct": 1,
         "expl": "A declarative statement, not hopeful or tentative language."},
        {"q": "What does 'bojjhaṅga' refer to?",
         "opts": [
             "The four noble truths",
             "The seven awakening factors: mindfulness, investigation, energy, joy, tranquility, immersion, and equanimity",
             "The five precepts",
             "A type of meditation posture"],
         "correct": 1,
         "expl": "Traditionally cultivated together on the path to awakening."},
        {"q": "Who does the closing attribution credit as this verse's speaker?",
         "opts": [
             "The Buddha, addressing Jentā",
             "The senior nun Jentā herself",
             "An unnamed nun",
             "No speaker is credited"],
         "correct": 1,
         "expl": "Unlike Thig 2.1's attribution to the Buddha."},
        {"q": "What does Jentā say having 'seen the Blessed One' relates to?",
         "opts": [
             "Nothing in particular",
             "Her statement that her current body is her last",
             "A request for further teaching",
             "A physical description of the Buddha"],
         "correct": 1,
         "expl": "Connected directly to her declaration of final attainment."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The first poem",
             "The second poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following Abhirūpanandā's verses."},
        {"q": "What does 'nibbāna' mean, as named in this verse?",
         "opts": [
             "'Extinguishment' — the goal the awakening factors lead toward",
             "'Awakening factor'",
             "'Bag of bones'",
             "'Attribution'"],
         "correct": 0,
         "expl": "Named as the destination of the path Jentā describes completing."},
        {"q": "How does this poem's tone compare to Thig 2.1's?",
         "opts": [
             "Identical, both giving instructions to be followed",
             "This poem reports an attainment already complete, rather than instructing toward one",
             "This poem gives no content about attainment at all",
             "Thig 2.1 reports an attainment; this poem gives instruction"],
         "correct": 1,
         "expl": "A shift from instruction to first-person report."},
    ],
    marginalia=[
        ("A precise, counted claim", [
            "all seven",
            "awakening factors"
        ]),
        ("Credited to its source", [
            "'just as",
            "the Buddha taught'"
        ]),
        ("A final body, echoed", [
            "the same phrase",
            "as Thig 2.1's instruction"
        ]),
        ("A flat declaration", [
            "no more",
            "future lives"
        ]),
    ],
    further=[
        '<a href="%s/thig2.2/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.1.html">Thig 2.1 &mdash; '
        "Abhir&umacr;panand&amacr;</a> &mdash; the text immediately before "
        "this one, sharing the phrase 'this bag of bones'.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.3 — Sumaṅgala's Mother
# --------------------------------------------------------------------------- #
page(
    2, 3, "Suma&#7749;galam&amacr;t&amacr;", "Suma&#7749;gala&rsquo;s Mother",
    meta_title="Thig 2.3 — Sumaṅgala's Mother | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sumaṅgala's Mother's verses, one of the Therigatha's sharpest and "
        "most vivid declarations of freedom from domestic drudgery. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "A nun identified by her son's name, &lsquo;Sumaṅgala's "
                    "Mother&rsquo;, speaking entirely in the first person"),
        ("Form", "Two four-line verses, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; vivid, "
                       "biting imagery worth reading closely alongside Thig "
                       "1.11"),
    ],
    why=(
        "This is one of the Therigatha's most quoted verses, and it "
        "answers Thig 1.11's celebrated declaration almost as a direct "
        "companion piece: both open with a woman announcing freedom from "
        "the mortar and pestle of household labor, but this poem goes "
        "further, turning its wit directly on her former husband."),
    guide=[
        ("Identified through her son, not her own name", [
            "This poem's title names its speaker only in relation to her "
            "child: &lsquo;Sumaṅgala's Mother&rsquo;. Her own personal name "
            "is not preserved &mdash; only her identity as a mother, a "
            "common naming pattern for women elsewhere in the canon as "
            "well."]),
        ("An opening that echoes Thig 1.11 directly", [
            "&lsquo;I'm well freed, well freed, so very well freed from the "
            "pestle&rsquo; closely parallels Thig 1.11's Muttā, &lsquo;I'm "
            "well freed, so very well freed&rsquo; &mdash; two poems "
            "sharing the same triumphant, tripled declaration and the same "
            "grinding tool as the symbol of what has been left behind."]),
        ("A husband described with pointed, unflattering wit", [
            "Where Thig 1.11 named her husband only by a physical "
            "description (&lsquo;humpbacked&rsquo;), this verse is sharper "
            "still: &lsquo;my shameless husband was most certainly a "
            "mushroom&rsquo; &mdash; and the mortar itself &lsquo;wafted "
            "like an eel&rsquo;, an image of unpleasant smell attached to "
            "her former domestic labor."]),
        ("From bitter wit to quiet contentment", [
            "The second verse shifts register entirely: greed and hate are "
            "described as something actively &lsquo;sizzling and "
            "hissing&rsquo; as she extinguishes them, before she settles at "
            "the root of a tree, meditating &lsquo;happily&rsquo;, "
            "exclaiming &lsquo;oh, what bliss!&rsquo; &mdash; sharp humor "
            "giving way to genuine ease."]),
    ],
    terms=[
        ("Sumaṅgalamātā",
         "&ldquo;Sumaṅgala's Mother&rdquo; &mdash; this poem's speaker, "
         "identified through her son rather than by her own personal "
         "name."),
        ("musala",
         "&ldquo;pestle&rdquo; &mdash; the tool of domestic grinding labor "
         "named as the first thing this speaker celebrates being freed "
         "from, the same image opening Thig 1.11."),
        ("lobha, dosa",
         "&ldquo;greed&rdquo; and &ldquo;hate&rdquo; &mdash; described in "
         "this verse's second half as sizzling and hissing as they are "
         "extinguished, an unusually vivid, almost culinary image."),
        ("rukkhamūla",
         "&ldquo;the root of a tree&rdquo; &mdash; a traditional, simple "
         "meditation spot, where this verse's speaker settles into her "
         "happiness."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution at all, distinctive chiefly for its sharp, humorous "
         "voice."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.3:1.1-1.4"),
        ("p", "&sect;2", "thig2.3:2.1-2.4"),
    ],
    quiz=[
        {"q": "How is this poem's speaker identified in its title?",
         "opts": [
             "By her own personal name",
             "As 'Sumaṅgala's Mother', identified through her son rather than her own name",
             "By the city she was born in",
             "By a title of royal rank"],
         "correct": 1,
         "expl": "Her personal name is not preserved in this text."},
        {"q": "What earlier poem does this verse's opening closely echo?",
         "opts": [
             "Thig 1.1",
             "Thig 1.11, Muttā's celebrated 'I'm well freed' declaration",
             "Thig 2.1",
             "No earlier poem is echoed"],
         "correct": 1,
         "expl": "Both open with the same triumphant, tripled declaration and the mortar-and-pestle image."},
        {"q": "How does this poem describe the speaker's former husband?",
         "opts": [
             "With warm affection and praise",
             "As 'shameless' and 'certainly a mushroom' — sharper wit than Thig 1.11's simple 'humpbacked'",
             "The husband is not mentioned at all",
             "Neutrally, with no particular characterization"],
         "correct": 1,
         "expl": "Pointed, unflattering imagery beyond Thig 1.11's plainer physical description."},
        {"q": "How does the verse describe greed and hate being extinguished?",
         "opts": [
             "As a slow, gradual fading",
             "As sizzling and hissing, an unusually vivid, almost culinary image",
             "The verse does not mention greed or hate",
             "As silent and unnoticed"],
         "correct": 1,
         "expl": "A striking image marking the second verse's shift in register."},
        {"q": "Where does the speaker settle to meditate, described as blissful?",
         "opts": [
             "In a grand temple",
             "At the root of a tree",
             "Back in her former home",
             "No location is given"],
         "correct": 1,
         "expl": "A traditional, simple meditation spot."},
        {"q": "What does this poem share word for word with Thig 1.11's opening?",
         "opts": [
             "Nothing at all",
             "The tripled declaration of freedom and the image of the pestle",
             "The entire poem is identical",
             "Only the closing line matches"],
         "correct": 1,
         "expl": "Companion poems sharing the same triumphant opening structure."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Sumaṅgala's Mother herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution closes this poem."},
        {"q": "What tone does the poem's overall arc follow?",
         "opts": [
             "Sharp, humorous wit giving way to quiet contentment",
             "Sorrow throughout, with no resolution",
             "Anger that never resolves",
             "A flat, unemotional report throughout"],
         "correct": 0,
         "expl": "From pointed jabs at her husband to happy meditation under a tree."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The second poem",
             "The third poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following Jentā's verses."},
        {"q": "What does 'musala' mean?",
         "opts": [
             "'Pestle' — the tool of domestic labor named as the first thing celebrated being freed from",
             "'Mushroom'",
             "'Tree root'",
             "'Bliss'"],
         "correct": 0,
         "expl": "The shared image opening both this poem and Thig 1.11."},
    ],
    marginalia=[
        ("Echoing Thig 1.11", [
            "'well freed'",
            "from the pestle again"
        ]),
        ("A husband, mocked", [
            "'certainly",
            "a mushroom'"
        ]),
        ("Sizzling and hissing", [
            "greed and hate",
            "extinguished vividly"
        ]),
        ("From wit to bliss", [
            "the root of a tree,",
            "genuine ease"
        ]),
    ],
    further=[
        '<a href="%s/thig2.3/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.2.html">Thig 2.2 &mdash; Jent&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="thig-1.11.html">Thig 1.11 &mdash; Mutt&amacr; (2nd)</a> '
        "&mdash; the companion poem this one echoes so closely.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.4 — Aḍḍhakāsi
# --------------------------------------------------------------------------- #
page(
    2, 4, "A&#7693;&#7693;hak&amacr;si", "A&#7693;&#7693;hak&amacr;si",
    meta_title="Thig 2.4 — Aḍḍhakāsi | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Aḍḍhakāsi's verses, a former courtesan whose price equaled half a "
        "kingdom, now speaking of the three knowledges. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "The nun Aḍḍhakāsi, speaking entirely in the first "
                    "person about her former livelihood"),
        ("Form", "A four-line verse followed by a six-line verse, nothing "
                 "more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "distinctive voice among the Therigatha's known "
                       "former courtesans"),
    ],
    why=(
        "Aḍḍhakāsi's very name states her former worth in coin: it means "
        "roughly &lsquo;half of Kāsi&rsquo;, reflecting a price for her "
        "services once said to equal half the value of an entire kingdom. "
        "This verse is one of a small number in the collection spoken by a "
        "former courtesan, moving from an unusual boast about worldly value "
        "to a direct account of spiritual attainment."),
    guide=[
        ("A name that records a price, not an insult", [
            "&lsquo;Aḍḍhakāsi&rsquo; combines <em>aḍḍha</em>, "
            "&lsquo;half&rsquo;, with &lsquo;Kāsi&rsquo;, the kingdom "
            "&mdash; the name itself preserves a specific, extraordinary "
            "valuation of her former services, treated here as a fact "
            "stated plainly rather than a shameful secret."]),
        ("Worldly value stated, then reframed", [
            "The first verse describes the price the townsfolk set for her "
            "as having made her, paradoxically, &lsquo;priceless&rsquo; "
            "&mdash; before the second verse turns entirely away from that "
            "valuation toward disillusionment with the very form that "
            "commanded it."]),
        ("A warning addressed outward, not just a personal report", [
            "&lsquo;Don't journey on and on, transmigrating through "
            "rebirths!&rsquo; briefly shifts from first-person report to "
            "direct address &mdash; advice offered to a listener, not only "
            "a statement about her own path."]),
        ("The three knowledges named as the mark of completion", [
            "The verse closes by naming a specific traditional set: "
            "&lsquo;I've realized the three knowledges, and fulfilled the "
            "Buddha's instructions&rsquo; &mdash; a standard closing "
            "formula for full attainment, appearing again in several later "
            "poems in this book."]),
    ],
    terms=[
        ("Aḍḍhakāsi",
         "&ldquo;half of Kāsi&rdquo; &mdash; this nun's name, recording the "
         "extraordinary price once set for her services as a courtesan."),
        ("Kāsi",
         "the kingdom whose value this verse's speaker's former price is "
         "said to have equaled half of."),
        ("nibbindā",
         "&ldquo;disillusionment&rdquo; or &ldquo;dispassion&rdquo; "
         "&mdash; the shift the second verse describes toward her own "
         "form."),
        ("tevijjā",
         "&ldquo;the three knowledges&rdquo; &mdash; a traditional mark of "
         "full attainment (recollection of past lives, the divine eye, and "
         "the ending of defilements), named directly in this verse's "
         "closing lines."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution, ending instead on the standard 'three knowledges' "
         "formula."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.4:1.1-1.4"),
        ("p", "&sect;2", "thig2.4:2.1-2.6"),
    ],
    quiz=[
        {"q": "What does the name 'Aḍḍhakāsi' mean?",
         "opts": [
             "'Beautiful one'",
             "Roughly 'half of Kāsi', recording her former price as a courtesan",
             "'The wanderer'",
             "The name has no particular meaning"],
         "correct": 1,
         "expl": "Combining 'half' with the name of a kingdom."},
        {"q": "How does the verse describe the effect of the price set for her services?",
         "opts": [
             "It made her ashamed",
             "It made her, paradoxically, 'priceless'",
             "It made her poor",
             "No effect is described"],
         "correct": 1,
         "expl": "Worldly value stated plainly before being reframed entirely."},
        {"q": "What does the second verse describe happening to her regard for her own form?",
         "opts": [
             "Increased pride in her appearance",
             "Growing disillusionment and dispassion",
             "No change at all",
             "A desire to return to her former life"],
         "correct": 1,
         "expl": "A direct turn away from the very valuation described in the first verse."},
        {"q": "What does the verse briefly shift to, beyond first-person report?",
         "opts": [
             "A dialogue with the Buddha",
             "Direct address to a listener: 'Don't journey on and on, transmigrating through rebirths!'",
             "A description of a specific city",
             "No shift occurs"],
         "correct": 1,
         "expl": "Advice offered outward, not only a personal statement."},
        {"q": "What specific traditional set does the verse name as the mark of her completion?",
         "opts": [
             "The five precepts",
             "The three knowledges (tevijjā)",
             "The seven awakening factors",
             "No specific set is named"],
         "correct": 1,
         "expl": "A standard closing formula appearing again in several later poems in this book."},
        {"q": "What kingdom is named in this verse, whose value her former price is said to have equaled half of?",
         "opts": [
             "Magadha",
             "Kāsi",
             "Kosala",
             "Videha"],
         "correct": 1,
         "expl": "The second half of Aḍḍhakāsi's own name."},
        {"q": "What is unusual about this verse compared to most of this book's poems?",
         "opts": [
             "It is one of a small number in the collection spoken by a former courtesan",
             "It contains no first-person content",
             "It is the only poem naming a specific kingdom",
             "It is written entirely in the third person"],
         "correct": 0,
         "expl": "A distinctive voice and background among the Therigatha's speakers."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — it closes instead on the standard 'three knowledges' formula",
             "Yes, naming Aḍḍhakāsi herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note, unlike Thig 2.1 and 2.2."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The third poem",
             "The fourth poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following Sumaṅgala's Mother's verses."},
        {"q": "What does 'nibbindā' mean?",
         "opts": [
             "'Disillusionment' or 'dispassion' — the shift described toward her own form",
             "'Price'",
             "'Kingdom'",
             "'Three knowledges'"],
         "correct": 0,
         "expl": "Named as the turning point of the second verse."},
    ],
    marginalia=[
        ("A name recording a price", [
            "'half of Kāsi' —",
            "stated, not hidden"
        ]),
        ("Priceless, paradoxically", [
            "the very price",
            "reframed entirely"
        ]),
        ("A warning turned outward", [
            "'don't journey",
            "on and on'"
        ]),
        ("The three knowledges", [
            "a standard mark",
            "of completion"
        ]),
    ],
    further=[
        '<a href="%s/thig2.4/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.3.html">Thig 2.3 &mdash; Suma&#7749;gala&rsquo;s '
        "Mother</a> &mdash; the text immediately before this one in the "
        "Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.5 — Cittā
# --------------------------------------------------------------------------- #
page(
    2, 5, "Citt&amacr;", "Citt&amacr;",
    meta_title="Thig 2.5 — Cittā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Cittā's verses, a frail, sick nun who climbs a mountain leaning on "
        "a staff and awakens beside a rock. From Ru-Yi Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "The nun Cittā, speaking entirely in the first person"),
        ("Form", "Two four-line verses, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain "
                       "narrative, best read alongside the poem right "
                       "after it"),
    ],
    why=(
        "Like Thig 1.17's Dhammā, this verse describes physical frailty "
        "directly rather than glossing over it: &lsquo;skinny, sick, and "
        "very feeble&rsquo;, Cittā climbs a mountain leaning on a staff, "
        "and awakens not despite the effort but through it, propped "
        "against a rock partway up."),
    guide=[
        ("Frailty named before anything else", [
            "The verse opens with three separate descriptions of physical "
            "weakness in a row: &lsquo;skinny, sick, and very "
            "feeble&rsquo; &mdash; not a single mention of hardship but a "
            "stacked, insistent one."]),
        ("An effortful climb, not a passive setting", [
            "Cittā does not simply happen to be somewhere difficult; she "
            "actively climbs, &lsquo;leaning on a staff&rsquo; &mdash; the "
            "difficulty is chosen and undertaken, not accidental."]),
        ("Concrete monastic gestures marking the moment", [
            "The second verse describes specific physical actions: laying "
            "down the outer robe, overturning the alms bowl, propping "
            "herself against a rock &mdash; ordinary monastic objects and "
            "postures, named individually rather than summarized."]),
        ("The same closing image as Thig 1.3", [
            "&lsquo;I shattered the mass of darkness&rsquo; repeats the "
            "exact phrase closing Thig 1.3's instruction to Puṇṇā, here "
            "spoken in the first person as an accomplished fact rather "
            "than an instruction still to be followed."]),
    ],
    terms=[
        ("Cittā",
         "this verse's speaker, whose physical frailty is named directly "
         "at the poem's opening."),
        ("daṇḍa",
         "&ldquo;staff&rdquo; &mdash; the support Cittā leans on while "
         "climbing, the same object named in Thig 1.17's account of "
         "Dhammā's fall."),
        ("cīvara, patta",
         "&ldquo;robe&rdquo; and &ldquo;bowl&rdquo; &mdash; the two basic "
         "monastic possessions named as set down before Cittā's awakening."),
        ("avijjākhandha",
         "the &ldquo;mass of darkness&rdquo; &mdash; ignorance described "
         "as something solid enough to be shattered, the same image "
         "closing Thig 1.3."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution, best read alongside the very next poem, Thig 2.6."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.5:1.1-1.4"),
        ("p", "&sect;2", "thig2.5:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does the verse describe Cittā's physical condition?",
         "opts": [
             "Strong and vigorous",
             "'Skinny, sick, and very feeble' — three descriptions of weakness in a row",
             "No physical description is given",
             "Young and energetic"],
         "correct": 1,
         "expl": "A stacked, insistent description, not a single passing mention."},
        {"q": "What does Cittā do despite her frailty?",
         "opts": [
             "She stays in her dwelling and rests",
             "She actively climbs a mountain, leaning on a staff",
             "She asks others to carry her",
             "She gives up practice entirely"],
         "correct": 1,
         "expl": "The difficulty is chosen and undertaken, not accidental."},
        {"q": "What specific actions does the second verse describe?",
         "opts": [
             "Only a general statement of meditation",
             "Laying down the outer robe, overturning the bowl, propping against a rock",
             "A conversation with another nun",
             "Building a shelter"],
         "correct": 1,
         "expl": "Ordinary monastic objects and postures, named individually."},
        {"q": "What phrase closes this verse, identical to Thig 1.3's closing?",
         "opts": [
             "'Sanctuary from the yoke'",
             "'I shattered the mass of darkness'",
             "'Free of debt'",
             "'Cooled and quenched'"],
         "correct": 1,
         "expl": "Here spoken as an accomplished fact rather than an instruction still to be followed."},
        {"q": "What does 'avijjākhandha' mean?",
         "opts": [
             "'Mass of darkness' — ignorance described as solid enough to be shattered",
             "'Staff'",
             "'Robe'",
             "'Bowl'"],
         "correct": 0,
         "expl": "The exact image closing both this verse and Thig 1.3."},
        {"q": "What object does Cittā's staff share with Thig 1.17's Dhammā?",
         "opts": [
             "Both describe a staff used while frail",
             "Nothing is shared between the two poems",
             "Both describe a bowl instead of a staff",
             "Only the setting is shared, not the object"],
         "correct": 0,
         "expl": "A support named in both accounts of physical difficulty."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Cittā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note closes this poem."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The fourth poem",
             "The fifth poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following Aḍḍhakāsi's verses."},
        {"q": "What does 'cīvara' and 'patta' refer to together?",
         "opts": [
             "'Robe' and 'bowl' — the two basic monastic possessions",
             "'Staff' and 'rock'",
             "'Mountain' and 'darkness'",
             "'Feeble' and 'skinny'"],
         "correct": 0,
         "expl": "Named as set down before Cittā's awakening."},
        {"q": "What poem is this one best read alongside, sharing a very similar structure?",
         "opts": [
             "Thig 1.1",
             "Thig 2.6, the very next poem",
             "Thig 2.4",
             "No other poem shares this structure"],
         "correct": 1,
         "expl": "A closely matching account follows immediately."},
    ],
    marginalia=[
        ("Frailty, stacked up", [
            "skinny, sick,",
            "very feeble"
        ]),
        ("A chosen difficulty", [
            "climbing actively,",
            "not passively enduring"
        ]),
        ("Concrete monastic gestures", [
            "robe laid down,",
            "bowl overturned"
        ]),
        ("Echoing Thig 1.3", [
            "'shattered the",
            "mass of darkness'"
        ]),
    ],
    further=[
        '<a href="%s/thig2.5/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.4.html">Thig 2.4 &mdash; A&#7693;&#7693;hak&amacr;si</a> '
        "&mdash; the text immediately before this one in the Therigatha.",
        '<a href="thig-2.6.html">Thig 2.6 &mdash; Mettik&amacr;</a> &mdash; '
        "the text right after this one, sharing a nearly identical "
        "structure.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.6 — Mettikā
# --------------------------------------------------------------------------- #
page(
    2, 6, "Mettik&amacr;", "Mettik&amacr;",
    meta_title="Thig 2.6 — Mettikā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Mettikā's verses, closely matching Thig 2.5's account of an "
        "elderly, ailing nun's mountain climb and awakening. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "The nun Mettikā, speaking entirely in the first "
                    "person"),
        ("Form", "A four-line verse followed by a six-line verse, nothing "
                 "more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; best "
                       "read directly alongside Thig 2.5"),
    ],
    why=(
        "This poem repeats Thig 2.5's basic account almost exactly: an "
        "elderly, ailing nun climbs a mountain with a staff, sets down her "
        "robe and bowl, and awakens seated on a rock. The two poems are "
        "close enough in structure that reading them together reveals a "
        "shared template underlying two different women's testimony."),
    guide=[
        ("Age and pain named directly, as in Thig 2.5", [
            "&lsquo;Though in pain, feeble, my youth long gone&rsquo; opens "
            "this verse in language close to Cittā's own opening &mdash; "
            "physical difficulty stated as fact before anything else "
            "follows."]),
        ("The same climb, the same staff", [
            "&lsquo;I climb the mountain, leaning on a staff&rsquo; repeats "
            "Thig 2.5's exact line &mdash; the same active, chosen "
            "difficulty, described in identical wording."]),
        ("A small variation in the awakening's setting", [
            "Where Thig 2.5 describes Cittā &lsquo;propping herself "
            "against a rock&rsquo;, this verse has Mettikā &lsquo;sitting "
            "on a rock&rsquo; &mdash; nearly the same image, with a small "
            "shift from leaning to sitting."]),
        ("A different closing formula than Thig 2.5's", [
            "Rather than repeating Thig 1.3's &lsquo;mass of darkness&rsquo; "
            "image as Thig 2.5 does, this verse closes with the &lsquo;three "
            "knowledges&rsquo; formula already seen in Thig 2.4 &mdash; the "
            "same underlying template, closed with a different standard "
            "formula each time."]),
    ],
    terms=[
        ("Mettikā",
         "this verse's speaker, whose account closely parallels Thig 2.5's "
         "Cittā."),
        ("daṇḍa",
         "&ldquo;staff&rdquo; &mdash; named in identical wording to Thig "
         "2.5's account of the mountain climb."),
        ("tevijjā",
         "&ldquo;the three knowledges&rdquo; &mdash; the same closing "
         "formula used in Thig 2.4, here closing this verse instead of "
         "Thig 2.5's 'mass of darkness' image."),
        ("pabbata",
         "&ldquo;mountain&rdquo; &mdash; the setting shared between this "
         "verse and Thig 2.5, both describing an elderly, ailing nun's "
         "climb."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution, closely paired with Thig 2.5 immediately before "
         "it."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.6:1.1-1.4"),
        ("p", "&sect;2", "thig2.6:2.1-2.6"),
    ],
    quiz=[
        {"q": "How does this verse's opening compare to Thig 2.5's?",
         "opts": [
             "Completely unrelated",
             "Very close in structure — both name pain, feebleness, and age or youth's passing before anything else",
             "This verse mentions no physical condition at all",
             "This verse describes a young, healthy nun"],
         "correct": 1,
         "expl": "A close parallel between these two adjacent poems' openings."},
        {"q": "What line does this verse share in identical wording with Thig 2.5?",
         "opts": [
             "'I shattered the mass of darkness'",
             "'I climb the mountain, leaning on a staff'",
             "'I've realized the three knowledges'",
             "No line is shared exactly"],
         "correct": 1,
         "expl": "The same active, chosen difficulty, described in identical words."},
        {"q": "What small variation appears in this verse's description of the awakening moment?",
         "opts": [
             "Mettikā is described as 'sitting on a rock', rather than 'propping herself against a rock'",
             "The rock is replaced entirely by a river",
             "No awakening moment is described",
             "There is no variation at all"],
         "correct": 0,
         "expl": "A small shift from leaning to sitting, otherwise closely matching Thig 2.5."},
        {"q": "What closing formula does this verse use, different from Thig 2.5's?",
         "opts": [
             "The same 'mass of darkness' image as Thig 2.5",
             "The 'three knowledges' formula, also seen in Thig 2.4",
             "No closing formula at all",
             "A formula unique to this verse alone"],
         "correct": 1,
         "expl": "The same underlying template closed with a different standard formula."},
        {"q": "What does reading this poem alongside Thig 2.5 reveal?",
         "opts": [
             "That the two poems contradict each other",
             "A shared template underlying two different women's testimony",
             "That one poem is a forgery of the other",
             "Nothing of particular interest"],
         "correct": 1,
         "expl": "Close structural similarity worth noticing when the two are read together."},
        {"q": "What does 'tevijjā' mean?",
         "opts": [
             "'The three knowledges' — a standard formula for full attainment",
             "'Mountain'",
             "'Staff'",
             "'Youth'"],
         "correct": 0,
         "expl": "Also used to close Thig 2.4's verse."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Mettikā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note, matching Thig 2.5's pattern."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The fifth poem",
             "The sixth poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Immediately following Cittā's closely matching verses."},
        {"q": "What setting do both this poem and Thig 2.5 share?",
         "opts": [
             "A riverbank",
             "A mountain, climbed with a staff",
             "A royal palace",
             "A forest fire"],
         "correct": 1,
         "expl": "The shared physical setting of both accounts."},
        {"q": "How long is this poem's second verse, compared to Thig 2.5's?",
         "opts": [
             "Exactly the same length, four lines",
             "Six lines, two lines longer than Thig 2.5's second verse",
             "A single line only",
             "Twenty lines"],
         "correct": 1,
         "expl": "The closing 'three knowledges' formula adds length not present in Thig 2.5's version."},
    ],
    marginalia=[
        ("The same opening note", [
            "pain, feebleness,",
            "as in Thig 2.5"
        ]),
        ("An identical line", [
            "'climb the mountain,",
            "leaning on a staff'"
        ]),
        ("Leaning becomes sitting", [
            "a small shift",
            "in the same image"
        ]),
        ("A different closing formula", [
            "'three knowledges',",
            "not 'mass of darkness'"
        ]),
    ],
    further=[
        '<a href="%s/thig2.6/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.5.html">Thig 2.5 &mdash; Citt&amacr;</a> &mdash; '
        "the text immediately before this one, sharing an almost identical "
        "structure.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.7 — Mittā (2nd)
# --------------------------------------------------------------------------- #
page(
    2, 7, "Mitt&amacr;", "Mitt&amacr; (2nd)",
    meta_title="Thig 2.7 — Mittā (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for a "
        "second Mittā's verses, moving from devoted observance days to no "
        "longer even longing for rebirth among the gods. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "A second nun also named Mittā, speaking entirely in "
                    "the first person"),
        ("Form", "A four-line verse followed by a six-line verse, nothing "
                 "more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; traces "
                       "a clear before-and-after within two short verses"),
    ],
    why=(
        "This second Mittā's verse traces a specific spiritual trajectory "
        "in miniature: devoted observance of the sabbath in hopes of a "
        "heavenly rebirth, followed by ordination, and finally a state "
        "beyond even that earlier hope &mdash; no longer wanting rebirth "
        "among the gods at all."),
    guide=[
        ("A devout layperson's practice, described specifically", [
            "The first verse lists precise observance details: the sabbath "
            "&lsquo;complete in all eight factors&rsquo;, kept &lsquo;on "
            "the fourteenth and the fifteenth days&rsquo;, plus the "
            "eighth day and the fortnightly special displays &mdash; the "
            "specific calendar of a committed lay practice."]),
        ("A stated former goal: the company of gods", [
            "&lsquo;I rejoiced in the host of gods&rsquo; names what this "
            "devout observance once aimed at &mdash; a favorable heavenly "
            "rebirth, a legitimate and widely held aspiration in itself."]),
        ("A visible change in circumstance", [
            "The second verse marks ordination in concrete, physical "
            "terms: &lsquo;today I eat just once a day, my head is shaven, "
            "I wear the outer robe&rsquo; &mdash; description grounded in "
            "daily bodily practice, not abstract commitment."]),
        ("Outgrowing the earlier aspiration entirely", [
            "The verse's closing lines state something stronger than "
            "simple progress: &lsquo;I don't long for the host of gods, "
            "for stress has been removed from my heart&rsquo; &mdash; not "
            "achieving the earlier goal, but moving beyond wanting it at "
            "all."]),
    ],
    terms=[
        ("Mittā",
         "this verse's speaker, a second nun of the same name as Thig "
         "1.8's Mittā, distinguished by the title &lsquo;(2nd)&rsquo;."),
        ("uposatha",
         "the &ldquo;sabbath&rdquo; or observance day, kept here "
         "&lsquo;complete in all eight factors&rsquo; before ordination."),
        ("aṭṭhaṅgika",
         "&ldquo;eight-factored&rdquo; &mdash; describing the fuller "
         "observance-day precepts kept by a devoted layperson."),
        ("ekabhattika",
         "&ldquo;eating just once a day&rdquo; &mdash; one of the concrete "
         "monastic practices named as marking the change described in the "
         "second verse."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution, tracing a clear before-and-after across its two "
         "verses."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.7:1.1-1.4"),
        ("p", "&sect;2", "thig2.7:2.1-2.6"),
    ],
    quiz=[
        {"q": "What specific observance does the first verse describe in detail?",
         "opts": [
             "A vague, unspecified devotion",
             "The sabbath, complete in all eight factors, kept on specific calendar days",
             "A single act of charity",
             "No observance is described"],
         "correct": 1,
         "expl": "A precise calendar of committed lay practice."},
        {"q": "What did this devout observance originally aim at?",
         "opts": [
             "Wealth and social status",
             "Rejoicing in the host of gods — a favorable heavenly rebirth",
             "Political influence",
             "Nothing in particular is stated"],
         "correct": 1,
         "expl": "A legitimate and widely held aspiration in itself."},
        {"q": "How does the second verse describe the change to ordained life?",
         "opts": [
             "In vague, abstract terms",
             "Concretely: eating once a day, a shaven head, wearing the outer robe",
             "The verse does not describe ordination at all",
             "Through a lengthy philosophical argument"],
         "correct": 1,
         "expl": "Description grounded in daily bodily practice."},
        {"q": "What does the verse's closing state about the earlier goal of rebirth among the gods?",
         "opts": [
             "That it was finally achieved",
             "That she no longer longs for it at all — moving beyond wanting it",
             "That it remains her current aim",
             "The goal is not mentioned again"],
         "correct": 1,
         "expl": "Not achieving the earlier aspiration, but outgrowing it entirely."},
        {"q": "What does 'uposatha' mean?",
         "opts": [
             "'Sabbath' or observance day",
             "'Host of gods'",
             "'Shaven head'",
             "'Stress'"],
         "correct": 0,
         "expl": "Named directly in the first verse's opening."},
        {"q": "What does 'aṭṭhaṅgika' describe in this verse?",
         "opts": [
             "The eightfold path specifically",
             "'Eight-factored' — describing the fuller observance-day precepts",
             "A type of robe",
             "A meditation posture"],
         "correct": 1,
         "expl": "The fuller precept set kept by a devoted layperson before ordination."},
        {"q": "How is this Mittā distinguished from Thig 1.8's Mittā?",
         "opts": [
             "They are treated as the same person",
             "By the title '(2nd)', marking a different individual sharing the same name",
             "By a completely different name entirely",
             "No distinction is made"],
         "correct": 1,
         "expl": "A common pattern of shared names across this collection."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Mittā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note closes this poem."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The sixth poem",
             "The seventh poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following Mettikā's mountain-climbing verses."},
        {"q": "What overall trajectory does this poem trace?",
         "opts": [
             "A single unchanging state throughout",
             "A specific progression: devout lay practice, ordination, and moving beyond even the earlier heavenly aspiration",
             "A decline from a higher to a lower state",
             "No trajectory is described"],
         "correct": 1,
         "expl": "A clear before-and-after within two short verses."},
    ],
    marginalia=[
        ("A precise calendar", [
            "the sabbath,",
            "specific days named"
        ]),
        ("A former goal named", [
            "rejoicing in",
            "the host of gods"
        ]),
        ("Ordination, concretely", [
            "one meal,",
            "shaven head, the robe"
        ]),
        ("Beyond the earlier wish", [
            "no longer longing",
            "for what she once sought"
        ]),
    ],
    further=[
        '<a href="%s/thig2.7/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.6.html">Thig 2.6 &mdash; Mettik&amacr;</a> &mdash; '
        "the text immediately before this one in the Therigatha.",
        '<a href="thig-1.8.html">Thig 1.8 &mdash; Mitt&amacr; (1st)</a> '
        "&mdash; a different nun of the same name.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.8 — To Abhayā's Mother, From Her Daughter
# --------------------------------------------------------------------------- #
page(
    2, 8, "Abhayam&amacr;tu Ther&imacr; Ovadana", "To Abhay&amacr;&rsquo;s "
    "Mother From Her Daughter",
    meta_title="Thig 2.8 — To Abhayā's Mother, From Her Daughter | Ru-Yi "
                "Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for a "
        "daughter's verses to her own mother, an unusually direct instance "
        "of a mother-daughter relationship named in the Therigatha. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "A daughter, addressing her own mother, named in the "
                    "collection as &lsquo;Abhayā's Mother&rsquo;"),
        ("Form", "Two four-line verses, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple "
                       "instruction, notable chiefly for who is speaking "
                       "to whom"),
    ],
    why=(
        "This poem's title states its relationship directly: a verse "
        "addressed by a daughter to her own mother, identified in this "
        "collection only as &lsquo;Abhayā's Mother&rsquo;. Mother and "
        "daughter both appear to have entered monastic life, and here the "
        "child instructs the parent &mdash; a reversal of the more "
        "familiar direction of teaching."),
    guide=[
        ("A relationship named in the title itself", [
            "Where most poems in this collection identify their speaker or "
            "addressee by a personal name alone, this poem's title states "
            "a family relationship directly: written by a daughter, "
            "addressed to her own mother."]),
        ("A comprehensive instruction to examine the body", [
            "The daughter's instruction covers the whole body "
            "systematically: &lsquo;up from the soles of the feet, and "
            "down from the tips of the hairs&rsquo; &mdash; a complete "
            "range, not a selective glance."]),
        ("Impurity named without qualification", [
            "The body examined this way is described plainly as &lsquo;so "
            "impure and foul-smelling&rsquo; &mdash; the same unflinching "
            "register as Thig 2.1's instruction to Nandā, here addressed "
            "by a child to her own parent rather than by the Buddha to a "
            "trainee."]),
        ("A direction of teaching reversed", [
            "The ordinary expectation of a parent instructing a child is "
            "set aside here: it is the daughter offering meditation "
            "instruction to her mother, a detail the collection preserves "
            "without further comment on how unusual it might seem."]),
    ],
    terms=[
        ("Abhayāmātā",
         "&ldquo;Abhayā's Mother&rdquo; &mdash; this poem's addressee, "
         "identified through her daughter Abhayā, whose own verse follows "
         "immediately in Thig 2.9."),
        ("asubha",
         "&ldquo;the unattractive&rdquo; or &ldquo;foulness&rdquo; "
         "&mdash; the same broad meditation category behind Thig 2.1's "
         "instruction, here directed by a daughter to her mother."),
        ("kāya",
         "&ldquo;body&rdquo; &mdash; the object of examination named "
         "directly in this verse's opening line."),
        ("kesagga",
         "&ldquo;the tips of the hairs&rdquo; &mdash; part of the "
         "comprehensive range this instruction covers, from feet to "
         "hair."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution, notable chiefly for the family relationship its "
         "title names."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.8:1.1-1.4"),
        ("p", "&sect;2", "thig2.8:2.1-2.4"),
    ],
    quiz=[
        {"q": "What relationship does this poem's title state directly?",
         "opts": [
             "Two unrelated nuns exchanging advice",
             "A daughter addressing her own mother",
             "A teacher addressing a stranger",
             "No relationship is named"],
         "correct": 1,
         "expl": "Written by a daughter, addressed to her own mother, 'Abhayā's Mother'."},
        {"q": "What range does the daughter's instruction to examine the body cover?",
         "opts": [
             "Only the face",
             "The whole body, 'up from the soles of the feet, and down from the tips of the hairs'",
             "Only the hands",
             "No specific range is given"],
         "correct": 1,
         "expl": "A complete range, not a selective glance."},
        {"q": "How does the verse describe the body being examined?",
         "opts": [
             "As beautiful and worth preserving",
             "As 'so impure and foul-smelling'",
             "As irrelevant to practice",
             "With no description at all"],
         "correct": 1,
         "expl": "The same unflinching register as Thig 2.1's instruction to Nandā."},
        {"q": "What is unusual about the direction of teaching in this poem?",
         "opts": [
             "Nothing unusual — parents always instruct children in this collection",
             "The daughter offers instruction to her mother, reversing the more familiar direction",
             "The poem contains no instruction at all",
             "The mother instructs a stranger, not her daughter"],
         "correct": 1,
         "expl": "A reversal the collection preserves without further comment."},
        {"q": "Who is 'Abhayā', as identified through this poem's title?",
         "opts": [
             "A king mentioned in passing",
             "The daughter speaking in this poem, whose mother is addressed here",
             "An unrelated nun",
             "The name of a city"],
         "correct": 1,
         "expl": "Her own verse follows immediately as Thig 2.9."},
        {"q": "What does the verse say is the result of meditating on the body this way?",
         "opts": [
             "Increased attachment to appearance",
             "All lust eradicated, the fever of passion cut off",
             "No result is described",
             "A desire to leave monastic life"],
         "correct": 1,
         "expl": "Named directly in the second verse's closing lines."},
        {"q": "What does 'asubha' mean?",
         "opts": [
             "'The unattractive' or 'foulness' — the broad meditation category this instruction belongs to",
             "'Mother'",
             "'Daughter'",
             "'Feet'"],
         "correct": 0,
         "expl": "The same category behind Thig 2.1's instruction to Nandā."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Abhayā's Mother",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note closes this poem."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The seventh poem",
             "The eighth poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following the second Mittā's verses."},
        {"q": "How does this poem's title differ from most others in this book?",
         "opts": [
             "It uses a personal name alone, exactly like the others",
             "It states a family relationship directly, rather than a name alone",
             "It gives no identifying information at all",
             "It names a location instead of a person"],
         "correct": 1,
         "expl": "A distinctive way of identifying speaker and addressee together."},
    ],
    marginalia=[
        ("A daughter to her mother", [
            "the title names",
            "the relationship directly"
        ]),
        ("Head to foot, examined", [
            "a complete range,",
            "not a glance"
        ]),
        ("Impurity, unflinching", [
            "the same register",
            "as Thig 2.1"
        ]),
        ("Teaching, reversed", [
            "the child instructs",
            "the parent"
        ]),
    ],
    further=[
        '<a href="%s/thig2.8/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.7.html">Thig 2.7 &mdash; Mitt&amacr; (2nd)</a> '
        "&mdash; the text immediately before this one in the Therigatha.",
        '<a href="thig-2.9.html">Thig 2.9 &mdash; Abhay&amacr;</a> &mdash; '
        "the very next poem, presumably the daughter's own verse.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.9 — Abhayā
# --------------------------------------------------------------------------- #
page(
    2, 9, "Abhay&amacr;", "Abhay&amacr;",
    meta_title="Thig 2.9 — Abhayā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Abhayā's verses, following directly after the instruction "
        "addressed to her mother in Thig 2.8. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Twos &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "Not identified with certainty; the verse addresses "
                    "&lsquo;Abhayā&rsquo; by name in the second person"),
        ("Form", "Two four-line verses, nothing more"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; best "
                       "read as a pair with Thig 2.8"),
    ],
    why=(
        "This verse follows immediately after Thig 2.8's instruction from "
        "a daughter to her mother, and addresses someone named Abhayā "
        "directly &mdash; the same name identifying the previous poem's "
        "speaker. Read together, the two verses suggest a family whose "
        "spiritual concerns run in both directions between a mother and "
        "her daughter."),
    guide=[
        ("A direct address, following a direct instruction", [
            "Where Thig 2.8 instructed a mother to examine the body, this "
            "verse opens by addressing &lsquo;Abhayā&rsquo; on a related "
            "theme: &lsquo;the body is fragile, yet ordinary people are "
            "attached to it&rsquo; &mdash; a continuation of the same "
            "concern in a new verse."]),
        ("A resolve stated plainly", [
            "&lsquo;I'll lay down the body, aware and mindful&rsquo; "
            "states an intention with unusual directness &mdash; not fear "
            "of death, but a clear-eyed readiness, held together with "
            "awareness rather than denial."]),
        ("Difficulty acknowledged, not minimized", [
            "&lsquo;Though subject to so many painful things&rsquo; opens "
            "the second verse honestly, before crediting &lsquo;love of "
            "diligence&rsquo; as what carried the speaker through to "
            "&lsquo;the ending of craving&rsquo; despite that difficulty."]),
        ("A closing formula repeated exactly in the next poem", [
            "This verse's final four lines &mdash; &lsquo;though subject "
            "to so many painful things... fulfilled the Buddha's "
            "instructions&rsquo; &mdash; recur word for word as the "
            "closing verse of Thig 2.10, immediately after this one, "
            "shared between two otherwise distinct poems."]),
    ],
    terms=[
        ("Abhayā",
         "the figure addressed in this verse, sharing a name with the "
         "speaker of Thig 2.8's instruction to her own mother."),
        ("kāya",
         "&ldquo;body&rdquo; &mdash; described here as &lsquo;fragile&rsquo;, "
         "the same object of examination named in Thig 2.8."),
        ("appamāda",
         "&ldquo;diligence&rdquo; &mdash; credited directly, alongside "
         "love for it, as what carried the speaker through difficulty to "
         "the ending of craving."),
        ("taṇhākkhaya",
         "&ldquo;the ending of craving&rdquo; &mdash; named as the "
         "attainment reached, closing this verse's second half."),
        ("cariyā",
         "not used here; another of this book's poems with no closing "
         "attribution, closing instead on a formula repeated word for word "
         "in the very next poem."),
    ],
    text_intro=(
        "The text in full: two verses, with no attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.9:1.1-1.4"),
        ("p", "&sect;2", "thig2.9:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this verse relate to Thig 2.8, immediately before it?",
         "opts": [
             "It is entirely unrelated in theme",
             "It follows a related theme, addressing someone named Abhayā, the same name identifying the previous poem's speaker",
             "It contradicts Thig 2.8 directly",
             "It is a word-for-word repeat of Thig 2.8"],
         "correct": 1,
         "expl": "Read together, the two verses suggest a family whose concerns run in both directions."},
        {"q": "What does the first verse say about the body?",
         "opts": [
             "That it is permanent and reliable",
             "That it is fragile, though ordinary people remain attached to it",
             "That it should not be examined at all",
             "Nothing about the body is mentioned"],
         "correct": 1,
         "expl": "A continuation of the concern raised in Thig 2.8."},
        {"q": "What resolve does the verse state directly?",
         "opts": [
             "A fear of death",
             "'I'll lay down the body, aware and mindful' — a clear-eyed readiness",
             "A wish to extend life as long as possible",
             "No resolve is stated"],
         "correct": 1,
         "expl": "Held together with awareness rather than denial."},
        {"q": "What does the second verse credit for carrying the speaker through difficulty?",
         "opts": [
             "Wealth and status",
             "Love of diligence (appamāda)",
             "The help of others alone",
             "Nothing is credited"],
         "correct": 1,
         "expl": "Named directly alongside acknowledging 'so many painful things'."},
        {"q": "What happens to this verse's closing four lines in the very next poem, Thig 2.10?",
         "opts": [
             "They are contradicted entirely",
             "They recur word for word as Thig 2.10's own closing verse",
             "They are never mentioned again",
             "They are only loosely paraphrased"],
         "correct": 1,
         "expl": "The same closing formula shared exactly between two otherwise distinct poems."},
        {"q": "What does 'taṇhākkhaya' mean?",
         "opts": [
             "'The ending of craving' — the attainment named at this verse's close",
             "'Fragile body'",
             "'Diligence'",
             "'Painful things'"],
         "correct": 0,
         "expl": "The destination reached despite acknowledged difficulty."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Abhayā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note closes this poem."},
        {"q": "What position does this poem hold in the Book of the Twos?",
         "opts": [
             "The eighth poem",
             "The ninth poem",
             "The last poem",
             "It is not part of the Book of the Twos"],
         "correct": 1,
         "expl": "Following the instruction addressed to Abhayā's Mother in Thig 2.8."},
        {"q": "How does the second verse acknowledge difficulty?",
         "opts": [
             "By denying that any difficulty existed",
             "Directly: 'though subject to so many painful things'",
             "By blaming others for the difficulty",
             "Difficulty is never mentioned"],
         "correct": 1,
         "expl": "Acknowledged honestly before crediting what carried the speaker through it."},
        {"q": "What does 'appamāda' mean?",
         "opts": [
             "'Diligence' — credited as what led through difficulty to the ending of craving",
             "'Fragility'",
             "'Attachment'",
             "'Awareness' specifically, as a separate term"],
         "correct": 0,
         "expl": "Named directly, paired with 'love of' it, in this verse's second half."},
    ],
    marginalia=[
        ("A continued theme", [
            "the body,",
            "fragile and attached to"
        ]),
        ("A clear-eyed resolve", [
            "'aware and",
            "mindful'"
        ]),
        ("Difficulty, acknowledged", [
            "'so many",
            "painful things'"
        ]),
        ("A shared closing formula", [
            "repeated word for word",
            "in Thig 2.10"
        ]),
    ],
    further=[
        '<a href="%s/thig2.9/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.8.html">Thig 2.8 &mdash; To Abhay&amacr;&rsquo;s '
        "Mother From Her Daughter</a> &mdash; the text immediately before "
        "this one in the Therigatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 2.10 — Sāmā
# --------------------------------------------------------------------------- #
page(
    2, 10, "S&amacr;m&amacr;", "S&amacr;m&amacr;",
    meta_title="Thig 2.10 — Sāmā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sāmā's verses, closing the Book of the Twos with an unusually "
        "honest account of repeated failure before success. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Twos &middot; Poem 10 of 10",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "The nun Sāmā, speaking entirely in the first person "
                    "about a specific, dated struggle"),
        ("Form", "A six-line verse followed by a four-line verse, closing "
                 "the Book of the Twos"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "notable for its candor about repeated failure"),
    ],
    why=(
        "This poem closes the Book of the Twos with something the "
        "collection rarely states this plainly: outright failure, "
        "repeated, before success finally comes. Sāmā names leaving her "
        "dwelling four or five times without finding peace of mind, before "
        "dating her breakthrough precisely to &lsquo;the eighth "
        "night&rsquo;."),
    guide=[
        ("Failure counted, not glossed over", [
            "&lsquo;Four or five times I left my dwelling&rsquo; states a "
            "specific number of attempts, followed directly by an honest "
            "verdict: &lsquo;I had failed to find peace of heart, or any "
            "control over my mind&rsquo; &mdash; no softening, no framing "
            "of these attempts as partial progress."]),
        ("A breakthrough dated with precision", [
            "Where most poems in this collection describe attainment "
            "without a timeline, this one is specific: &lsquo;now it is "
            "the eighth night since craving was eradicated&rsquo; &mdash; a "
            "practice diary's precision applied to a spiritual "
            "breakthrough."]),
        ("The exact closing quatrain of Thig 2.9, repeated", [
            "This poem's second verse is word for word the same as Thig "
            "2.9's closing four lines: &lsquo;though subject to so many "
            "painful things... fulfilled the Buddha's instructions.&rsquo; "
            "Two different women's accounts, closing this book on the "
            "identical formula."]),
        ("A fitting close to a book of individual struggle", [
            "The Book of the Twos ends not on a triumphant image but on an "
            "honest account of difficulty overcome slowly &mdash; a "
            "counterpoint to Thig 2.2's Jentā, who opened this book's "
            "second poem with a confident, completed report, and a "
            "reminder that this collection preserves failure alongside "
            "success."]),
    ],
    terms=[
        ("Sāmā",
         "this poem's speaker, whose account is unusually specific about "
         "the number of failed attempts before her breakthrough."),
        ("cittassa vūpasama",
         "&ldquo;peace of heart&rdquo; &mdash; what Sāmā says she "
         "repeatedly failed to find before her eventual success."),
        ("aṭṭharattā",
         "&ldquo;the eighth night&rdquo; &mdash; the precise timing Sāmā "
         "gives for when craving was eradicated."),
        ("taṇhākkhaya",
         "&ldquo;the ending of craving&rdquo; &mdash; the same term "
         "closing Thig 2.9, repeated word for word in this poem's second "
         "verse."),
        ("cariyā",
         "not used here; the last of this book's poems, closing on a "
         "formula shared exactly with the poem immediately before it."),
    ],
    text_intro=(
        "The text in full: two verses, closing the Book of the Twos. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig2.10:1.1-1.6"),
        ("p", "&sect;2", "thig2.10:2.1-2.4"),
    ],
    quiz=[
        {"q": "How many times does Sāmā say she left her dwelling without success?",
         "opts": [
             "Once",
             "Four or five times",
             "Ten times",
             "The number is not given"],
         "correct": 1,
         "expl": "A specific count, stated plainly."},
        {"q": "How does the verse describe these earlier attempts?",
         "opts": [
             "As partial successes worth celebrating",
             "As outright failure — 'I had failed to find peace of heart, or any control over my mind'",
             "The attempts are not described at all",
             "As someone else's failure, not her own"],
         "correct": 1,
         "expl": "No softening or reframing as progress."},
        {"q": "How precisely does the verse date the eventual breakthrough?",
         "opts": [
             "With no timing at all",
             "To 'the eighth night' since craving was eradicated",
             "To an entire year",
             "Only in vague, general terms"],
         "correct": 1,
         "expl": "A practice diary's precision applied to a spiritual breakthrough."},
        {"q": "What does this poem's second verse share with Thig 2.9's closing?",
         "opts": [
             "Nothing at all",
             "The exact same four closing lines, word for word",
             "Only a loose paraphrase",
             "A direct contradiction"],
         "correct": 1,
         "expl": "Two different women's accounts closing on the identical formula."},
        {"q": "How does this poem's tone compare to Thig 2.2's Jentā, opening this book's second poem?",
         "opts": [
             "Identical in every way",
             "A counterpoint — honest struggle rather than a confident, already-completed report",
             "This poem describes no struggle at all",
             "Jentā's poem describes more struggle than this one"],
         "correct": 1,
         "expl": "A reminder that this collection preserves failure alongside success."},
        {"q": "What does 'cittassa vūpasama' mean?",
         "opts": [
             "'Peace of heart' — what Sāmā repeatedly failed to find",
             "'The eighth night'",
             "'Painful things'",
             "'Dwelling'"],
         "correct": 0,
         "expl": "Named as what eluded her across several attempts."},
        {"q": "Does this poem have a closing attribution?",
         "opts": [
             "Yes, naming the Buddha",
             "No — like several others in this book, it has none",
             "Yes, naming Sāmā herself",
             "It has two attributions"],
         "correct": 1,
         "expl": "No formal attribution note closes this poem."},
        {"q": "What position does this poem hold in the Therigatha?",
         "opts": [
             "It opens the Book of the Twos",
             "It closes the Book of the Twos, the collection's second book",
             "It is the final poem of the entire collection",
             "It is not part of any book"],
         "correct": 1,
         "expl": "The tenth and last poem of ten in this second book."},
        {"q": "What does 'aṭṭharattā' mean?",
         "opts": [
             "'The eighth night' — the precise timing given for the breakthrough",
             "'Peace of heart'",
             "'Dwelling'",
             "'Craving'"],
         "correct": 0,
         "expl": "A specific, dated detail unusual among this collection's poems."},
        {"q": "What overall impression does this closing poem leave about the path to awakening in this collection?",
         "opts": [
             "That it is always immediate and effortless",
             "That it can involve real, repeated failure before eventual success",
             "That failure means permanent inability to progress",
             "That timing is never mentioned anywhere in the collection"],
         "correct": 1,
         "expl": "An honest counterpoint closing this book of individual struggle."},
    ],
    marginalia=[
        ("Failure, counted", [
            "four or five times,",
            "no success"
        ]),
        ("A precise breakthrough", [
            "the eighth night,",
            "dated exactly"
        ]),
        ("The same closing as Thig 2.9", [
            "word for word,",
            "shared exactly"
        ]),
        ("Struggle, honestly kept", [
            "closing the book",
            "on real difficulty"
        ]),
    ],
    further=[
        '<a href="%s/thig2.10/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.9.html">Thig 2.9 &mdash; Abhay&amacr;</a> &mdash; '
        "the text immediately before this one, sharing this poem's exact "
        "closing formula.",
        '<a href="./">Therigatha</a> &mdash; back to the collection index.',
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.1 — Another Sāmā
# --------------------------------------------------------------------------- #
page(
    3, 1, "S&amacr;m&amacr;", "Another S&amacr;m&amacr;",
    meta_title="Thig 3.1 — Another Sāmā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "poem opening the Book of the Threes, a second Sāmā whose closing "
        "verse repeats a formula shared with two poems just before it. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 1 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "The nun Sāmā, speaking in the first person about "
                    "twenty-five years of unsuccessful effort"),
        ("Form", "Three verses of four, four, and six lines, opening the "
                 "Book of the Threes"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain "
                       "in form, notable chiefly for what it repeats from "
                       "the book just closed"),
    ],
    why=(
        "This poem opens the Book of the Threes with a second nun named "
        "Sāmā &mdash; its title, &lsquo;Another Sāmā&rsquo;, points back "
        "directly at Thig 2.10, the poem that just closed the book before "
        "it. The two poems share more than a name: a full line of this "
        "poem's opening verse repeats Thig 2.10 word for word, and its "
        "closing verse repeats a quatrain already used twice in the book "
        "just finished."),
    guide=[
        ("A name-pair spanning a book boundary", [
            "Earlier same-name pairs in this collection &mdash; the two "
            "Tissās of Thig 1.4 and 1.5, the two Sumanās of Thig 1.14 and "
            "1.16 &mdash; sit inside a single book. This is the first pair "
            "to fall across a boundary: Thig 2.10's Sāmā closes the Book "
            "of the Twos, and this &lsquo;Another Sāmā&rsquo; opens the "
            "Book of the Threes immediately after."]),
        ("A line repeated exactly from the poem just before", [
            "This poem's second verse opens &lsquo;I had failed to find "
            "peace of heart, or any control over my mind&rsquo; &mdash; "
            "the identical line, word for word, that opened Thig 2.10's "
            "account of the other Sāmā's struggle. Two different women, "
            "consecutive poems, the same confession of failure."]),
        ("A closing quatrain used for the third time", [
            "&lsquo;Though subject to so many painful things... fulfilled "
            "the Buddha's instructions&rsquo; closed both Thig 2.9 and "
            "Thig 2.10. Here it closes a third poem in a row, each time "
            "followed by a different precise count of days: unspecified "
            "urgency in 2.9, an eighth night in 2.10, and here a seventh "
            "day."]),
        ("Twenty-five years, then seven days", [
            "The poem's real span is the gap between two numbers: "
            "twenty-five years of monastic life without ever finding "
            "serenity, set against the seven days since her breakthrough "
            "&mdash; a long failure resolved abruptly once urgency, "
            "prompted by remembering the Buddha's own instructions, took "
            "hold."]),
    ],
    terms=[
        ("S&amacr;m&amacr;",
         "this poem's speaker, sharing a name with Thig 2.10's Sāmā but "
         "explicitly a different individual, as the title states."),
        ("jinas&amacr;sana",
         "&ldquo;the victor's instructions&rdquo; &mdash; remembering "
         "these is what struck her with a sense of urgency after "
         "twenty-five fruitless years."),
        ("saṁvega",
         "the sense of urgency or spiritual dismay named directly as her "
         "turning point, here translated &lsquo;struck with a sense of "
         "urgency&rsquo;."),
        ("taṇhakkhaya",
         "&ldquo;the ending of craving&rdquo; &mdash; the same term "
         "closing Thig 2.9 and Thig 2.10, repeated again in this poem's "
         "closing verse."),
        ("cariyā",
         "not used here; like several poems just before it, this one "
         "closes with no formal attribution note."),
    ],
    text_intro=(
        "The text in full: three verses, opening the Book of the Threes. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.1:1.1-1.4"),
        ("p", "&sect;2", "thig3.1:2.1-2.4"),
        ("p", "&sect;3", "thig3.1:3.1-3.6"),
    ],
    quiz=[
        {"q": "How many years does Sāmā say passed without her finding serenity?",
         "opts": [
             "Five years",
             "One year",
             "Twenty-five years",
             "The number is not given"],
         "correct": 2,
         "expl": "'In the twenty-five years since I went forth' — a long span of failure."},
        {"q": "What triggers her turning point, according to the second verse?",
         "opts": [
             "A dream",
             "A conversation with another nun",
             "No trigger is given",
             "Remembering the victor's — the Buddha's — instructions"],
         "correct": 3,
         "expl": "'When I remembered the victor's instructions, I was struck with a sense of urgency.'"},
        {"q": "What line does this poem's second verse share word for word with Thig 2.10?",
         "opts": [
             "'I had failed to find peace of heart, or any control over my mind'",
             "No line is shared",
             "The elephant simile",
             "The mention of Rājagaha"],
         "correct": 0,
         "expl": "The identical confession of failure opens both poems' accounts."},
        {"q": "What relationship does this poem's title state to Thig 2.10?",
         "opts": [
             "None — the title gives no indication",
             "'Another Sāmā', pointing back to the Sāmā who closed the book just before",
             "That they are sisters by blood",
             "That this poem predates Thig 2.10"],
         "correct": 1,
         "expl": "The title signals a shared name, not a shared identity, for two different nuns."},
        {"q": "How many times, counting this poem, has the closing quatrain 'though subject to so many painful things...fulfilled the Buddha's instructions' now appeared?",
         "opts": [
             "Once",
             "Twice",
             "Three times",
             "It has not appeared before"],
         "correct": 2,
         "expl": "Thig 2.9, Thig 2.10, and now this poem all close on the identical formula."},
        {"q": "How precisely does this poem date its speaker's breakthrough?",
         "opts": [
             "With no timing at all",
             "To an entire year",
             "Only in vague terms",
             "To the seventh day since craving dried up"],
         "correct": 3,
         "expl": "'This is the seventh day since my craving dried up' — a specific count, like 2.10's eighth night."},
        {"q": "What does 'saṁvega' name in this poem?",
         "opts": [
             "The sense of urgency struck into her on remembering the Buddha's instructions",
             "A place of pilgrimage",
             "A type of formal ordination",
             "The name of a fellow nun"],
         "correct": 0,
         "expl": "Her turning point, named directly rather than merely implied."},
        {"q": "What position does this poem hold in the Therigatha as a whole?",
         "opts": [
             "It closes the entire collection",
             "It opens the Book of the Threes, the collection's third book",
             "It is the final poem of the Book of the Twos",
             "It stands outside any book"],
         "correct": 1,
         "expl": "The first of eight poems opening this new, longer book."},
        {"q": "What does 'taṇhakkhaya' mean?",
         "opts": [
             "'Peace of heart'",
             "'The victor's instructions'",
             "'The ending of craving'",
             "'Twenty-five years'"],
         "correct": 2,
         "expl": "The same term that closed both poems just before this one."},
        {"q": "What overall shape does this poem's own numbers trace?",
         "opts": [
             "A long failure — twenty-five years — resolved abruptly within seven days of urgency",
             "A short, even struggle throughout",
             "Immediate success with no failure at all",
             "No numbers are given anywhere in the poem"],
         "correct": 0,
         "expl": "The real span of the poem is the gap between its two numbers."},
    ],
    marginalia=[
        ("A name, and a boundary crossed", [
            "the first same-name pair",
            "to span two books"
        ]),
        ("A line repeated exactly", [
            "from the poem",
            "just before it"
        ]),
        ("A closing formula, third use", [
            "the same quatrain,",
            "a different count of days"
        ]),
        ("Twenty-five years, then seven days", [
            "a long failure,",
            "resolved abruptly"
        ]),
    ],
    further=[
        '<a href="%s/thig3.1/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-2.10.html">Thig 2.10 &mdash; S&amacr;m&amacr;</a> '
        "&mdash; the poem this one is named after, sharing a full line and "
        "its closing formula.",
        '<a href="thig-3.2.html">Thig 3.2 &mdash; Uttam&amacr;</a> &mdash; '
        "the next poem in the Book of the Threes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.2 — Uttamā
# --------------------------------------------------------------------------- #
page(
    3, 2, "Uttam&amacr;", "Uttam&amacr;",
    meta_title="Thig 3.2 — Uttamā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Uttamā's verses, a breakthrough reached under a named teacher's "
        "guidance after seven days of unmoving meditation. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 2 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "The nun Uttamā, describing her own failed attempts, "
                    "then a breakthrough guided by another nun's teaching"),
        ("Form", "Three verses of four, four, and six lines"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "introduces three technical categories of analysis "
                       "in a single line"),
    ],
    why=(
        "This poem opens with the same confession of failure heard twice "
        "already in this book &mdash; but where Thig 2.10's Sāmā and Thig "
        "3.1's Sāmā broke through on their own, Uttamā names her turning "
        "point precisely: a nun she trusted, who taught her a specific "
        "threefold analysis of experience, after which seven days of "
        "unmoving meditation produced her release."),
    guide=[
        ("A confession repeated for the third time", [
            "&lsquo;Four or five times I left my dwelling. I had failed to "
            "find peace of heart, or any control over my mind&rsquo; opens "
            "this poem exactly as it opened Thig 2.10 &mdash; the same "
            "words now used by a third woman to describe the same early "
            "failure, three poems running."]),
        ("A teacher, trusted and named only by that trust", [
            "Uttamā does not name her teacher, only the relationship: "
            "&lsquo;a nun in whom I had faith&rsquo;. What this teacher "
            "gave her was not comfort but a specific analysis &mdash; "
            "&lsquo;the aggregates, sense fields, and elements&rsquo;, "
            "three standard categories for examining experience "
            "systematically rather than as a single undivided self."]),
        ("Seven days motionless, then release on the eighth", [
            "Following that teaching exactly, Uttamā sat &lsquo;cross-"
            "legged for seven days without moving, given over to rapture "
            "and bliss&rsquo;, then on the eighth day stretched out her "
            "feet, her meditation complete &mdash; a specific, embodied "
            "account of sustained absorption rather than a general claim "
            "of progress."]),
        ("A phrase that will return", [
            "Her closing image, &lsquo;having shattered the mass of "
            "darkness&rsquo;, is not unique to this poem: the same phrase, "
            "almost word for word, closes two later poems in this same "
            "book, Thig 3.7 and Thig 3.8 &mdash; a stock image for a "
            "breakthrough, reused across several different women's "
            "accounts."]),
    ],
    terms=[
        ("Uttam&amacr;",
         "this poem's speaker, whose breakthrough followed specific "
         "instruction from a trusted teacher."),
        ("khandh&amacr;yatanadh&amacr;tuyo",
         "&ldquo;the aggregates, sense fields, and elements&rdquo; "
         "&mdash; three standard analytical categories, taught to her as "
         "a single compound term in this line."),
        ("p&imacr;tisukha",
         "&ldquo;rapture and bliss&rdquo; &mdash; the quality of her "
         "seven motionless days of meditation."),
        ("tamokkhandha",
         "&ldquo;the mass of darkness&rdquo; &mdash; shattered at her "
         "breakthrough, a phrase repeated almost word for word by two "
         "later poems in this book."),
        ("cariy&amacr;",
         "not used here; like the poem before it, this one closes with no "
         "formal attribution note."),
    ],
    text_intro=(
        "The text in full: three verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.2:1.1-1.4"),
        ("p", "&sect;2", "thig3.2:2.1-2.4"),
        ("p", "&sect;3", "thig3.2:3.1-3.6"),
    ],
    quiz=[
        {"q": "What confession opens this poem, word for word identical to Thig 2.10's opening?",
         "opts": [
             "'Four or five times I left my dwelling... I had failed to find peace of heart'",
             "'In the twenty-five years since I went forth'",
             "'What's up with these people in Rājagaha?'",
             "No opening line is shared with any other poem"],
         "correct": 0,
         "expl": "The same confession of failure, now used by a third woman in three consecutive poems."},
        {"q": "How does Uttamā identify the nun who taught her?",
         "opts": [
             "By her formal ordination name",
             "As the daughter of a well-known family",
             "Only as 'a nun in whom I had faith' — no personal name given",
             "As a stranger she never met again"],
         "correct": 2,
         "expl": "The relationship is named directly; the teacher's own name is not."},
        {"q": "What did this teacher instruct her in?",
         "opts": [
             "Chanting practices only",
             "The aggregates, sense fields, and elements — a threefold analysis of experience",
             "Rules of monastic discipline",
             "No specific teaching is described"],
         "correct": 1,
         "expl": "'Khandhāyatanadhātuyo' — three standard categories, named together as a single teaching."},
        {"q": "How long did Uttamā sit without moving after receiving this instruction?",
         "opts": [
             "One day",
             "A full month",
             "Seven days",
             "The duration is not given"],
         "correct": 2,
         "expl": "'I sat cross-legged for seven days without moving, given over to rapture and bliss.'"},
        {"q": "What happened on the eighth day?",
         "opts": [
             "She left the monastic order",
             "She stretched out her feet, having shattered the mass of darkness",
             "She began the practice again from the start",
             "Nothing is recorded about an eighth day"],
         "correct": 1,
         "expl": "A specific, embodied close to seven days of sustained absorption."},
        {"q": "What phrase from this poem's closing line reappears in two later poems of this same book?",
         "opts": [
             "'The victor's instructions'",
             "'Twenty-five years'",
             "'A nun in whom I had faith'",
             "'Having shattered the mass of darkness'"],
         "correct": 3,
         "expl": "Thig 3.7 and Thig 3.8 both close on nearly the identical image."},
        {"q": "What does 'pītisukha' mean?",
         "opts": [
             "'Rapture and bliss' — the quality of her seven days of unmoving meditation",
             "'The mass of darkness'",
             "'Seven days'",
             "'A trusted teacher'"],
         "correct": 0,
         "expl": "Named directly as what filled her while seated cross-legged."},
        {"q": "How does this poem's account of breakthrough differ from Thig 2.10 and Thig 3.1's?",
         "opts": [
             "It does not differ at all",
             "It describes no breakthrough at all",
             "It happens instantly with no practice described",
             "It names a specific teacher's role and a specific, embodied seven-day practice, rather than describing the breakthrough alone"],
         "correct": 3,
         "expl": "A named teaching relationship and a concrete meditative account, distinct from the other two poems' shorter narratives."},
        {"q": "What position does this poem hold in the Book of the Threes?",
         "opts": [
             "The first poem",
             "The second poem, following Thig 3.1",
             "The last poem",
             "It is not part of the Book of the Threes"],
         "correct": 1,
         "expl": "Following the second Sāmā's poem that opened this book."},
        {"q": "What does 'khandhāyatanadhātuyo' name?",
         "opts": [
             "A place name",
             "The name of Uttamā's home village",
             "The aggregates, sense fields, and elements — three analytical categories taught as a unit",
             "A type of monastic robe"],
         "correct": 2,
         "expl": "A compound term bundling three standard frameworks for examining experience."},
    ],
    marginalia=[
        ("A confession, a third time", [
            "the same failure,",
            "three poems running"
        ]),
        ("A teacher, named by trust alone", [
            "no personal name,",
            "only the relationship"
        ]),
        ("Seven days, unmoving", [
            "rapture and bliss,",
            "then release"
        ]),
        ("A phrase that will return", [
            "the mass of darkness,",
            "shattered again later"
        ]),
    ],
    further=[
        '<a href="%s/thig3.2/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.1.html">Thig 3.1 &mdash; Another S&amacr;m&amacr;'
        "</a> &mdash; the poem immediately before this one, opening with "
        "the identical confession of failure.",
        '<a href="thig-3.3.html">Thig 3.3 &mdash; Another Uttam&amacr;</a> '
        "&mdash; the next poem, sharing this poem's own name.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.3 — Another Uttamā
# --------------------------------------------------------------------------- #
page(
    3, 3, "Uttam&amacr;", "Another Uttam&amacr;",
    meta_title="Thig 3.3 — Another Uttamā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for this "
        "second Uttamā's verses, a compact checklist of attainments "
        "closing on the collection's standard formula for rebirth ended. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 3 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; no "
                    "closing attribution"),
        ("Speaker", "A second nun named Uttamā, listing her own "
                    "attainments in the first person"),
        ("Form", "Three four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "most doctrinally dense checklist so far in this "
                       "book"),
    ],
    why=(
        "This poem's title, &lsquo;Another Uttamā&rsquo;, names the "
        "collection's second same-name pair to sit inside a single book "
        "&mdash; unlike Thig 2.10 and Thig 3.1's Sāmās, split across a "
        "book boundary, this Uttamā follows the first immediately. Where "
        "that first Uttamā told a story of a specific teacher and a "
        "seven-day practice, this one offers something different: a "
        "compact list of attainments, stated without narrative."),
    guide=[
        ("A second same-name pair, closer together this time", [
            "Thig 3.1's &lsquo;Another Sāmā&rsquo; pointed back across a "
            "book boundary to Thig 2.10. This poem's &lsquo;Another "
            "Uttamā&rsquo; points back only one poem, to Thig 3.2 &mdash; "
            "the collection's second instance of two same-named women "
            "placed one after the other."]),
        ("Seven factors, all of them developed", [
            "&lsquo;Of the seven awakening factors, the path for "
            "attaining extinguishment, I have developed them all, just as "
            "the Buddha taught&rsquo; &mdash; a direct claim to complete, "
            "not partial, mastery of a named standard list."]),
        ("Two meditations, available on demand", [
            "&lsquo;I attain the meditations on emptiness and signlessness "
            "whenever I want&rsquo; frames her mastery not as something "
            "that occurred once but as available at will &mdash; a "
            "distinct kind of claim from a single dated breakthrough."]),
        ("A rightful daughter, and a closing formula reused", [
            "&lsquo;I am the Buddha's rightful daughter, always delighting "
            "in extinguishment&rsquo; is a striking self-description, and "
            "the poem's final lines &mdash; &lsquo;transmigration through "
            "births is finished, now there'll be no more future "
            "lives&rsquo; &mdash; use this collection's standard closing "
            "formula for the first time in the Book of the Threes."]),
    ],
    terms=[
        ("bojjha&#7749;ga",
         "the seven awakening factors, a standard list this poem claims "
         "to have developed in full."),
        ("su&ntilde;&ntilde;ata",
         "&ldquo;emptiness&rdquo; &mdash; one of two meditations named as "
         "attainable &lsquo;whenever I want&rsquo;."),
        ("animitta",
         "&ldquo;signlessness&rdquo; &mdash; the second of the two "
         "meditations named alongside emptiness."),
        ("orasā dhītā buddhassa",
         "&ldquo;the Buddha's rightful daughter&rdquo; &mdash; this "
         "poem's own striking self-description."),
        ("punabbhava",
         "&ldquo;future life&rdquo; or rebirth &mdash; denied outright in "
         "this poem's closing line, the collection's standard formula for "
         "an ended cycle."),
    ],
    text_intro=(
        "The text in full: three verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.3:1.1-1.4"),
        ("p", "&sect;2", "thig3.3:2.1-2.4"),
        ("p", "&sect;3", "thig3.3:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does this poem's title, 'Another Uttamā', signal?",
         "opts": [
             "That this is the same speaker as Thig 3.2",
             "The collection's second same-name pair placed inside one book",
             "That this poem predates Thig 3.2",
             "Nothing — the title carries no particular significance"],
         "correct": 1,
         "expl": "Unlike Sāmā's pair, split across a book boundary, this pair sits one poem apart."},
        {"q": "What does the first verse claim about the seven awakening factors?",
         "opts": [
             "That they are impossible to develop fully",
             "That only one of the seven has been developed",
             "That all seven have been developed, just as the Buddha taught",
             "The seven factors are not mentioned"],
         "correct": 2,
         "expl": "A direct claim to complete, not partial, mastery."},
        {"q": "How does the poem describe her access to the meditations on emptiness and signlessness?",
         "opts": [
             "As having occurred only once, long ago",
             "As available whenever she wants",
             "As something she has never attained",
             "As available only with another nun's help"],
         "correct": 1,
         "expl": "'I attain the meditations... whenever I want' — mastery framed as availability, not a single event."},
        {"q": "How does this poem describe itself as the Buddha's daughter?",
         "opts": [
             "It makes no such claim",
             "As an adopted, distant relation",
             "As 'the Buddha's rightful daughter, always delighting in extinguishment'",
             "As a daughter by blood, in a literal family sense"],
         "correct": 2,
         "expl": "A striking, direct self-description at this poem's turning point."},
        {"q": "What closing formula appears in this poem for the first time in the Book of the Threes?",
         "opts": [
             "'Though subject to so many painful things...'",
             "'Transmigration through births is finished, now there'll be no more future lives'",
             "'Having shattered the mass of darkness'",
             "No closing formula is used"],
         "correct": 1,
         "expl": "The collection's standard formula for an ended cycle of rebirth, reused here."},
        {"q": "How does this poem's structure compare to Thig 3.2's?",
         "opts": [
             "Identical in every respect",
             "This poem tells a longer story than Thig 3.2",
             "Neither poem describes any attainment",
             "This poem offers a compact list of attainments rather than a narrative with a named teacher"],
         "correct": 3,
         "expl": "A checklist register rather than the specific seven-day narrative of the poem just before it."},
        {"q": "What does 'bojjhaṅga' refer to?",
         "opts": [
             "The seven awakening factors, a standard list this poem claims to have completed",
             "'Emptiness'",
             "A type of monastic robe",
             "'Rightful daughter'"],
         "correct": 0,
         "expl": "Named directly as fully developed, 'just as the Buddha taught'."},
        {"q": "What are the two meditations this poem names as attainable at will?",
         "opts": [
             "Emptiness and signlessness",
             "Loving-kindness and compassion",
             "Breath and body",
             "No specific meditations are named"],
         "correct": 0,
         "expl": "'Suññatassānimittassa' — emptiness and signlessness, named together."},
        {"q": "What position does this poem hold in the Book of the Threes?",
         "opts": [
             "The first poem",
             "The last poem",
             "It stands outside this book",
             "The third poem, immediately after the first Uttamā"],
         "correct": 3,
         "expl": "Directly following Thig 3.2, sharing that poem's speaker's name."},
        {"q": "What does 'animitta' mean?",
         "opts": [
             "'Emptiness'",
             "'Future life'",
             "'Signlessness' — the second of two meditations named alongside emptiness",
             "'Awakening factors'"],
         "correct": 2,
         "expl": "Paired directly with 'suññata' as the two meditations attained at will."},
    ],
    marginalia=[
        ("A second pair, closer together", [
            "one poem apart,",
            "not a book apart"
        ]),
        ("Seven factors, all developed", [
            "a complete claim,",
            "not a partial one"
        ]),
        ("Attainable at will", [
            "not a single event,",
            "but availability itself"
        ]),
        ("A formula reused", [
            "no more future lives,",
            "first time in this book"
        ]),
    ],
    further=[
        '<a href="%s/thig3.3/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.2.html">Thig 3.2 &mdash; Uttam&amacr;</a> &mdash; '
        "the poem immediately before this one, sharing this speaker's own "
        "name.",
        '<a href="thig-3.4.html">Thig 3.4 &mdash; Dantik&amacr;</a> &mdash; '
        "the next poem in the Book of the Threes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.4 — Dantikā
# --------------------------------------------------------------------------- #
page(
    3, 4, "Dantik&amacr;", "Dantik&amacr;",
    meta_title="Thig 3.4 — Dantikā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Dantikā's verses, a mind settled into serenity by watching a "
        "wild elephant tamed on Vulture's Peak. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Threes &middot; Poem 4 of 8",
    glance=[
        ("Setting", "Vulture's Peak Mountain, on a riverbank, after "
                    "leaving a day's meditation"),
        ("Speaker", "The nun Dantikā, narrating what she personally "
                    "witnessed and its effect on her mind"),
        ("Form", "Three four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "single concrete scene, simply told"),
    ],
    why=(
        "This poem breaks from the confessions and checklists just before "
        "it: instead of describing failure or listing attainments, "
        "Dantikā narrates a single scene she witnessed &mdash; a wild "
        "elephant submitting to a mahout's hook on a riverbank &mdash; and "
        "traces her own mind settling into serenity directly from watching "
        "it, a breakthrough triggered by observation rather than "
        "instruction."),
    guide=[
        ("A name that puns on its own scene", [
            "&lsquo;Dantikā&rsquo; shares its root with &lsquo;danta&rsquo;, "
            "&lsquo;tamed&rsquo; &mdash; her name itself echoes the very "
            "scene this poem describes, an echo the collection has already "
            "used for Sukkā (&lsquo;bright&rsquo;) later in this same book, "
            "and for Muttā (&lsquo;freed&rsquo;) earlier in Thig 1.2 and "
            "1.11."]),
        ("A specific, watched scene, not a recited teaching", [
            "&lsquo;Leaving my day's meditation on Vulture's Peak "
            "Mountain, I saw an elephant on the riverbank having just come "
            "up from his bath&rsquo; &mdash; a dated, located observation, "
            "distinct from this book's confessions of inner struggle or "
            "lists of doctrinal categories."]),
        ("The taming, described step by step", [
            "The scene itself is simple and complete: a man with a hook "
            "asks the elephant for its foot, the elephant presents it, the "
            "man mounts &mdash; three plain actions, given no more weight "
            "than they need."]),
        ("Insight drawn from watching, and a wry closing line", [
            "&lsquo;Seeing a wild beast so tamed, submitting to human "
            "control, my mind became serene&rsquo; states the insight "
            "directly from the scene, and the poem closes on an "
            "unusually personal aside &mdash; &lsquo;that is why I've "
            "gone to the forest&rsquo; &mdash; addressed almost "
            "conversationally to the reader."]),
    ],
    terms=[
        ("Dantik&amacr;",
         "this poem's speaker, whose name shares its root with "
         "&lsquo;danta&rsquo;, &lsquo;tamed&rsquo; &mdash; echoing the "
         "scene the poem describes."),
        ("Gijjhak&#363;&#7789;a",
         "Vulture's Peak Mountain, the specific, named setting where this "
         "poem opens."),
        ("a&#7749;kusa",
         "the hook used by the mahout to direct the elephant, the "
         "instrument named in the poem's second verse."),
        ("sam&amacr;dhi",
         "the settled, serene mind state Dantikā describes reaching, "
         "translated here as her mind &lsquo;becoming serene&rsquo;."),
        ("vana",
         "&ldquo;forest&rdquo; &mdash; named in this poem's closing line "
         "as the destination this insight sent her toward."),
    ],
    text_intro=(
        "The text in full: three verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.4:1.1-1.4"),
        ("p", "&sect;2", "thig3.4:2.1-2.4"),
        ("p", "&sect;3", "thig3.4:3.1-3.4"),
    ],
    quiz=[
        {"q": "Where does this poem's scene take place?",
         "opts": [
             "In a city marketplace",
             "In a monastery hall",
             "On Vulture's Peak Mountain, by a riverbank",
             "The location is not given"],
         "correct": 2,
         "expl": "A specific, named setting, unusual for this book so far."},
        {"q": "What does Dantikā see when she leaves her day's meditation?",
         "opts": [
             "An elephant on the riverbank, just come up from his bath",
             "A group of fellow nuns",
             "A burning building",
             "Nothing unusual is described"],
         "correct": 0,
         "expl": "The scene that triggers the rest of the poem."},
        {"q": "What does the man with the hook ask the elephant to do?",
         "opts": [
             "Kneel down completely",
             "Trumpet loudly",
             "Return to the river",
             "Give him its foot, so he can mount"],
         "correct": 3,
         "expl": "A simple, specific request, immediately obeyed."},
        {"q": "How does the elephant respond to the man's request?",
         "opts": [
             "It presents its foot, and the man mounts",
             "It runs away",
             "It attacks the man",
             "It ignores the request"],
         "correct": 0,
         "expl": "Full submission, described in a single plain action."},
        {"q": "What effect does watching this scene have on Dantikā's mind?",
         "opts": [
             "It became serene, seeing a wild beast so tamed",
             "No effect is described",
             "It became agitated by the sight",
             "She left the scene without any reaction"],
         "correct": 0,
         "expl": "The insight is drawn directly from what she observed."},
        {"q": "What does Dantikā's name share a root with?",
         "opts": [
             "A place name",
             "'Tamed' — echoing this very poem's scene",
             "'Serene'",
             "'River'"],
         "correct": 1,
         "expl": "Like Sukkā's 'bright' or Muttā's 'freed', her name echoes her poem's own content."},
        {"q": "How does this poem's approach to breakthrough differ from the confessions in Thig 3.1–3.2?",
         "opts": [
             "It does not differ; all describe the same kind of struggle",
             "It arises from watching an external scene, not from a teacher's instruction or dated inner struggle",
             "This poem describes no breakthrough at all",
             "It is identical to Thig 3.3's checklist of attainments"],
         "correct": 1,
         "expl": "An observation-triggered insight, distinct from confession or checklist."},
        {"q": "How does this poem end?",
         "opts": [
             "With the standard 'no more future lives' formula",
             "With an attribution naming the Buddha",
             "With a question left unanswered",
             "With a personal aside: 'that is why I've gone to the forest'"],
         "correct": 3,
         "expl": "An unusually direct, almost conversational closing line for this collection."},
        {"q": "What is the aṅkusa mentioned in this poem?",
         "opts": [
             "A type of alms bowl",
             "A meditation posture",
             "The hook used by the mahout to direct the elephant",
             "A monastic robe"],
         "correct": 2,
         "expl": "The instrument named directly in the poem's second verse."},
        {"q": "What position does this poem hold in the Book of the Threes?",
         "opts": [
             "The first poem",
             "The fourth poem, following the second Uttamā",
             "The last poem",
             "It is not part of the Book of the Threes"],
         "correct": 1,
         "expl": "Following Thig 3.3, opening a new kind of scene in this book."},
    ],
    marginalia=[
        ("A name that puns on the scene", [
            "Dantikā, 'tamed' —",
            "the elephant, tamed too"
        ]),
        ("Watched, not recited", [
            "a dated scene,",
            "not a doctrine"
        ]),
        ("Three plain actions", [
            "asked, given,",
            "mounted"
        ]),
        ("A wry, personal close", [
            "'that is why",
            "I've gone to the forest'"
        ]),
    ],
    further=[
        '<a href="%s/thig3.4/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.3.html">Thig 3.3 &mdash; Another Uttam&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-3.5.html">Thig 3.5 &mdash; Ubbir&imacr;</a> &mdash; '
        "the next poem in the Book of the Threes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.5 — Ubbirī
# --------------------------------------------------------------------------- #
page(
    3, 5, "Ubbir&imacr;", "Ubbir&imacr;",
    meta_title="Thig 3.5 — Ubbirī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ubbirī's verses, a grieving mother consoled at a cremation "
        "ground with a teaching built on her daughter's own name. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 5 of 8",
    glance=[
        ("Setting", "A cremation ground, where Ubbirī grieves her dead "
                    "daughter"),
        ("Speaker", "Two voices: an unnamed consoler, identified by "
                    "commentary as the Buddha, then Ubbirī herself in "
                    "reply"),
        ("Form", "A six-line verse addressed to Ubbirī, followed by two "
                 "four-line verses in her own voice"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "dialogue poem built on a name's double meaning"),
    ],
    why=(
        "This poem opens on a mother crying at a cremation ground for her "
        "dead daughter, whose name, Jīvā, means &lsquo;Live&rsquo;. The "
        "unnamed consoler &mdash; identified by the ancient commentary, "
        "though not by the verse itself, as the Buddha &mdash; answers her "
        "grief not with abstraction but with a fact of place: eighty-four "
        "thousand people, every one of them also named Jīvā, have been "
        "cremated at this exact ground. Ubbirī's own reply, in the verses "
        "that follow, completes the poem."),
    guide=[
        ("A named speaker, but only by commentary", [
            "The verse addressed to Ubbirī names no speaker. Bhikkhu "
            "Sujato's own note on this poem states plainly: &lsquo;the "
            "speaker of this verse... is not named in the text, but the "
            "commentary identifies it as the Buddha&rsquo; &mdash; a "
            "distinction this guide preserves rather than collapsing into "
            "certainty."]),
        ("A name turned into a teaching", [
            "Ubbirī's grief-cry, quoted back to her, is &lsquo;Live, my "
            "dear mother!&rsquo; &mdash; addressed to her daughter Jīvā, "
            "whose name means &lsquo;Live&rsquo;. The consoler's reply "
            "does not dispute her grief but widens it: eighty-four "
            "thousand people, &lsquo;all named &ldquo;Live&rdquo;&rsquo;, "
            "have been burnt at this very ground &mdash; turning a single "
            "child's name into a lesson about how ordinary loss is."]),
        ("An arrow, named and then pulled out", [
            "Ubbirī's own reply opens with a physical image for her grief: "
            "&lsquo;you have plucked the arrow from me, so hard to see, "
            "stuck in the heart&rsquo; &mdash; grief as a lodged, nearly "
            "invisible wound, removed by what she has just heard."]),
        ("Refuge, taken directly, closing the poem", [
            "Where earlier poems in this book close on formulas about "
            "craving ended or future lives finished, Ubbirī's own closing "
            "words are different: &lsquo;I go for refuge to that sage, "
            "the Buddha, to his teaching, and to the Sangha&rsquo; "
            "&mdash; an explicit statement of the Triple Refuge, plainly "
            "spoken rather than implied."]),
    ],
    terms=[
        ("Ubbir&imacr;",
         "this poem's grieving mother, whose reply forms this poem's "
         "second and third verses."),
        ("J&imacr;v&amacr;",
         "&ldquo;Live&rdquo; &mdash; the name of Ubbirī's dead daughter, "
         "and of eighty-four thousand others cremated at the same "
         "ground."),
        ("&#256;&#7773;&#257;hana",
         "the cremation ground where this poem is set, named directly in "
         "the consoling verse."),
        ("sallaṁ",
         "&ldquo;the arrow&rdquo; &mdash; Ubbirī's own image for her "
         "grief, described as &lsquo;plucked out&rsquo; by the teaching "
         "she has just heard."),
        ("parinibbut&amacr;",
         "&ldquo;quenched&rdquo; &mdash; Ubbirī's own closing "
         "self-description, punning on the word for full "
         "extinguishment."),
    ],
    text_intro=(
        "The text in full: a consoling verse addressed to Ubbirī, "
        "followed by her own two verses in reply. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.5:1.1-1.6"),
        ("p", "&sect;2", "thig3.5:2.1-2.4"),
        ("p", "&sect;3", "thig3.5:3.1-3.4"),
    ],
    quiz=[
        {"q": "What is Ubbirī doing at the start of this poem?",
         "opts": [
             "Teaching a group of students",
             "Grieving her dead daughter at a cremation ground",
             "Traveling to a distant city",
             "Celebrating a festival"],
         "correct": 1,
         "expl": "The poem opens on her cry of grief for her daughter."},
        {"q": "What does Ubbirī's daughter's name, Jīvā, mean?",
         "opts": [
             "A place name",
             "'Grief'",
             "'Mother'",
             "'Live'"],
         "correct": 3,
         "expl": "The double meaning at the center of this poem's teaching."},
        {"q": "Who is identified as the speaker of the poem's opening verse?",
         "opts": [
             "Not named in the text itself; identified by commentary as the Buddha",
             "Ubbirī's daughter, speaking from beyond death",
             "A stranger passing by",
             "Ubbirī herself, addressing her own memory"],
         "correct": 0,
         "expl": "This guide preserves Sujato's own hedge rather than asserting certainty."},
        {"q": "How many people does the speaker say share the name 'Live', all cremated at this ground?",
         "opts": [
             "Eighty-four thousand",
             "Just one, Ubbirī's daughter",
             "A hundred",
             "The number is not given"],
         "correct": 0,
         "expl": "'Eighty-four thousand people, all named ‘Live’, have been burnt in this funeral ground.'"},
        {"q": "What image does Ubbirī use for her own grief in her reply?",
         "opts": [
             "A storm",
             "A locked door",
             "An arrow, hard to see, stuck in the heart",
             "No image is used"],
         "correct": 2,
         "expl": "Grief as a lodged wound, now described as removed."},
        {"q": "What does Ubbirī say has happened to that arrow by the poem's end?",
         "opts": [
             "It remains lodged permanently",
             "It has grown larger",
             "She has forgotten about it entirely",
             "It has been plucked out"],
         "correct": 3,
         "expl": "'Today I've plucked the arrow, I'm hungerless, quenched.'"},
        {"q": "What does 'parinibbutā' mean, as Ubbirī applies it to herself?",
         "opts": [
             "'Grieving'",
             "'Quenched' — punning on the word for full extinguishment",
             "'Wandering'",
             "'A cremation ground'"],
         "correct": 1,
         "expl": "Her own self-description at the poem's turning point."},
        {"q": "How does this poem close?",
         "opts": [
             "With the 'no more future lives' formula",
             "With no closing statement",
             "With Ubbirī explicitly taking refuge in the Buddha, his teaching, and the Sangha",
             "With a question addressed to the Buddha"],
         "correct": 2,
         "expl": "A plainly spoken statement of the Triple Refuge, distinct from this book's other closing formulas."},
        {"q": "What structural feature makes this poem distinct within the Book of the Threes so far?",
         "opts": [
             "It is a dialogue between two voices, not a single first-person account",
             "It has no verses at all",
             "It is identical in structure to Thig 3.3",
             "It contains no named location"],
         "correct": 0,
         "expl": "The book's first two-speaker poem, opening with a verse addressed to its subject."},
        {"q": "What does 'Āḷāhana' name?",
         "opts": [
             "Ubbirī's home village",
             "A river",
             "A meditation posture",
             "The cremation ground where this poem is set"],
         "correct": 3,
         "expl": "Named directly in the consoling verse as the site of eighty-four thousand cremations."},
    ],
    marginalia=[
        ("A speaker, named only by commentary", [
            "not in the verse itself,",
            "held as an open question"
        ]),
        ("A name turned into a teaching", [
            "eighty-four thousand,",
            "all named 'Live'"
        ]),
        ("An arrow, plucked out", [
            "grief as a wound,",
            "now removed"
        ]),
        ("Refuge, plainly spoken", [
            "Buddha, teaching, Sangha —",
            "named directly"
        ]),
    ],
    further=[
        '<a href="%s/thig3.5/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.4.html">Thig 3.4 &mdash; Dantik&amacr;</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="thig-3.6.html">Thig 3.6 &mdash; Sukk&amacr;</a> &mdash; '
        "the next poem in the Book of the Threes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.6 — Sukkā
# --------------------------------------------------------------------------- #
page(
    3, 6, "Sukk&amacr;", "Sukk&amacr;",
    meta_title="Thig 3.6 — Sukkā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "poem praising Sukkā entirely from the outside, contrasting a "
        "distracted crowd in Rājagaha with those who drink in her "
        "teaching. From Ru-Yi Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 6 of 8",
    glance=[
        ("Setting", "Rājagaha, a city named directly in the poem's "
                    "opening line"),
        ("Speaker", "Not identified; an outside voice describing and "
                    "praising Sukkā throughout, never speaking as her"),
        ("Form", "Three four-line verses, entirely in the third person"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "notable chiefly for who is not speaking"),
    ],
    why=(
        "Every poem so far in this book has spoken in Sāmā's, Uttamā's, "
        "Dantikā's, or Ubbirī's own first-person voice, at least in part. "
        "This poem never does: an unnamed outside voice describes the "
        "nun Sukkā throughout, contrasting a distracted crowd in Rājagaha "
        "with those wise enough to &lsquo;drink up&rsquo; her teaching, "
        "then explains her very name as a description of her own bright "
        "qualities."),
    guide=[
        ("A poem with no first-person voice at all", [
            "Unlike every poem before it in this book, Sukkā never speaks "
            "in her own voice here. An outside speaker describes her "
            "throughout &mdash; asking, in effect, why the crowds of "
            "Rājagaha &lsquo;sprawl like they've been drinking mead&rsquo; "
            "instead of attending her teaching."]),
        ("A crowd distracted, and the wise who drink it in", [
            "The poem's central image is a contrast: ordinary people in "
            "Rājagaha ignore Sukkā as if intoxicated, while &lsquo;the "
            "wise&rsquo; take in her teaching &lsquo;as if they drink it "
            "up... like travelers enjoying a cool cloud&rsquo; &mdash; "
            "her Dhamma teaching itself described as refreshment."]),
        ("A name explained as a description", [
            "&lsquo;She's known as Sukkā because of her bright "
            "qualities&rsquo; states the pun directly: Sukkā, "
            "&lsquo;bright&rsquo;, named for being exactly that &mdash; "
            "joining Dantikā's &lsquo;tamed&rsquo; earlier in this book "
            "and Muttā's &lsquo;freed&rsquo; in Thig 1.2 and 1.11 as "
            "another name the collection treats as a description, not "
            "just a label."]),
        ("A martial image, closing an outsider's praise", [
            "The poem's final line &mdash; &lsquo;having vanquished Māra "
            "with his legions&rsquo; &mdash; is this book's first mention "
            "of Māra by name, delivered as an outsider's claim about "
            "Sukkā's attainment rather than her own account of it, ahead "
            "of the direct Māra confrontations still to come in Thig 3.7 "
            "and 3.8."]),
    ],
    terms=[
        ("Sukk&amacr;",
         "this poem's subject, whose name, meaning &lsquo;bright&rsquo;, "
         "is explained directly in the closing verse."),
        ("R&amacr;jagaha",
         "the city named in this poem's opening line, whose crowds are "
         "described as distracted."),
        ("appa&#7789;iv&amacr;n&imacr;ya",
         "&ldquo;irresistible&rdquo; &mdash; describing Sukkā's teaching "
         "as the wise experience it."),
        ("sukk&amacr; sukkehi dhammehi",
         "&ldquo;Sukkā, by her bright qualities&rdquo; &mdash; this "
         "poem's own etymological explanation of her name."),
        ("M&amacr;ra sav&amacr;hin&imacr;",
         "&ldquo;Māra with his legions&rdquo; &mdash; named as vanquished "
         "in this poem's closing line, this book's first mention of "
         "Māra."),
    ],
    text_intro=(
        "The text in full: three verses, entirely in the third person. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.6:1.1-1.4"),
        ("p", "&sect;2", "thig3.6:2.1-2.4"),
        ("p", "&sect;3", "thig3.6:3.1-3.4"),
    ],
    quiz=[
        {"q": "In what city does this poem's opening line say people ignore Sukkā's teaching?",
         "opts": [
             "Sāvatthī",
             "Kapilavatthu",
             "Vesālī",
             "Rājagaha"],
         "correct": 3,
         "expl": "Named directly in the poem's opening question."},
        {"q": "How does the poem describe the crowd who ignore Sukkā's teaching?",
         "opts": [
             "As if they've been drinking mead",
             "As diligent students",
             "As traveling merchants",
             "As fellow monastics"],
         "correct": 0,
         "expl": "A simile for their distraction, opening the poem."},
        {"q": "How does the poem describe the wise, by contrast?",
         "opts": [
             "As equally distracted",
             "As absent from the scene entirely",
             "As drinking in her teaching like travelers enjoying a cool cloud",
             "As critical of her teaching"],
         "correct": 2,
         "expl": "The poem's central contrasting image."},
        {"q": "Whose voice speaks throughout this poem?",
         "opts": [
             "Sukkā herself, throughout",
             "The Buddha, addressing Sukkā directly",
             "An unnamed outside voice; Sukkā never speaks in her own first-person voice",
             "Māra, taunting Sukkā"],
         "correct": 2,
         "expl": "Unlike every poem before it in this book, no first-person voice appears here."},
        {"q": "What does the poem's closing verse say Sukkā's name means?",
         "opts": [
             "'Wise'",
             "'Cloud'",
             "'Traveler'",
             "'Bright' — named for her own bright qualities"],
         "correct": 3,
         "expl": "'Sukkā sukkehi dhammehi' — the pun stated directly."},
        {"q": "What earlier name-pun in this book does Sukkā's join?",
         "opts": [
             "Uttamā's name has no stated meaning",
             "Dantikā's 'tamed', from the poem just before this one",
             "This is the collection's only name-pun",
             "Ubbirī's name is explained the same way"],
         "correct": 1,
         "expl": "Dantikā (Thig 3.4) and Muttā (Thig 1.2, 1.11) are the collection's other examples."},
        {"q": "What does this poem's closing line claim Sukkā has done?",
         "opts": [
             "Returned to lay life",
             "Traveled to Rājagaha for the first time",
             "Vanquished Māra with his legions",
             "Composed this very poem herself"],
         "correct": 2,
         "expl": "This book's first mention of Māra by name, ahead of the direct confrontations in 3.7 and 3.8."},
        {"q": "What does 'appaṭivānīya' describe?",
         "opts": [
             "A place name",
             "Sukkā's teaching, as the wise experience it — 'irresistible'",
             "The crowd's distraction",
             "A type of monastic robe"],
         "correct": 1,
         "expl": "Paired with 'asecanaka', 'delectable', in the poem's second verse."},
        {"q": "What position does this poem hold in the Book of the Threes?",
         "opts": [
             "The first poem",
             "The last poem",
             "It stands outside this book",
             "The sixth poem, following Ubbirī"],
         "correct": 3,
         "expl": "Following Thig 3.5, opening this book's only entirely third-person poem so far."},
        {"q": "How does this poem's voice differ from every poem before it in the Book of the Threes?",
         "opts": [
             "It contains no first-person account at all — entirely an outside voice describing Sukkā",
             "It does not differ at all",
             "It is Sukkā's own first-person account, like the others",
             "It is addressed directly to Māra"],
         "correct": 0,
         "expl": "The book's first fully third-person poem."},
    ],
    marginalia=[
        ("No first-person voice at all", [
            "an outside speaker,",
            "throughout"
        ]),
        ("A crowd distracted, the wise refreshed", [
            "drunk on mead,",
            "or drinking in the teaching"
        ]),
        ("A name explained directly", [
            "'bright', named",
            "for being exactly that"
        ]),
        ("Māra, named for the first time", [
            "in this book,",
            "ahead of direct confrontation"
        ]),
    ],
    further=[
        '<a href="%s/thig3.6/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.5.html">Thig 3.5 &mdash; Ubbir&imacr;</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="thig-3.7.html">Thig 3.7 &mdash; Sel&amacr;</a> &mdash; '
        "the next poem, this book's first direct confrontation with Māra.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.7 — Selā
# --------------------------------------------------------------------------- #
page(
    3, 7, "Sel&amacr;", "Sel&amacr;",
    meta_title="Thig 3.7 — Selā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Selā's verses, this book's first direct confrontation with "
        "Māra, answered with an image of sensual pleasure as a weapon "
        "against oneself. From Ru-Yi Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 7 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "the addressee is named only as Māra, the Wicked One"),
        ("Speaker", "Two voices: Māra, tempting with a worldly argument, "
                    "then Selā, refuting him directly"),
        ("Form", "Two four-line verses: Māra's temptation, then Selā's "
                 "reply"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "direct confrontation, answered with a vivid "
                       "counter-image"),
    ],
    why=(
        "This poem is the Book of the Threes' first direct confrontation "
        "with Māra: he argues plainly for indulgence &mdash; &lsquo;enjoy "
        "erotic delights, don't regret it later&rsquo; &mdash; and Selā "
        "answers not with abstraction but with a specific, visceral "
        "counter-image, comparing sensual pleasure itself to a weapon "
        "turned against the very aggregates that make up a person."),
    guide=[
        ("A direct temptation, plainly argued", [
            "Māra's opening verse makes a specific worldly case: "
            "&lsquo;there's no escape in the world, so what will "
            "seclusion do for you? Enjoy erotic delights; don't regret it "
            "later&rsquo; &mdash; not a vague threat, but an argument "
            "Selā answers point by point."]),
        ("Pleasure recast as a weapon", [
            "Selā's reply reframes the very terms of the offer: "
            "&lsquo;sensual pleasures are like swords and spears, the "
            "aggregates are their chopping block&rsquo; &mdash; what Māra "
            "calls delight, she names as violence turned inward, against "
            "one's own body and mind."]),
        ("A word reclaimed and reversed", [
            "&lsquo;What you call &ldquo;erotic delight&rdquo; is now no "
            "delight for me&rsquo; takes Māra's own word back and empties "
            "it &mdash; not simply refusing the offer, but declaring the "
            "category itself no longer applies to her."]),
        ("A closing formula shared word for word with the poem after it", [
            "&lsquo;Relishing is banished in every respect, and the mass "
            "of darkness is shattered... you're beaten, terminator!&rsquo; "
            "closes this poem exactly as it will close Thig 3.8 &mdash; "
            "the same victorious quatrain answering two separate "
            "temptations, and an echo of Thig 3.2's own &lsquo;shattered "
            "the mass of darkness&rsquo;."]),
    ],
    terms=[
        ("Sel&amacr;",
         "this poem's speaker, who answers Māra's temptation with a "
         "counter-image rather than a simple refusal."),
        ("P&amacr;pim&amacr;",
         "&ldquo;Wicked One&rdquo; &mdash; how Selā addresses Māra "
         "directly in this poem's closing line."),
        ("sattis&#363;l&#363;pam&amacr;",
         "&ldquo;like swords and spears&rdquo; &mdash; Selā's own "
         "description of sensual pleasures, in her reply's opening line."),
        ("khandha",
         "the aggregates, named here as the &lsquo;chopping block&rsquo; "
         "for the weapon of sensual pleasure &mdash; the same term "
         "Uttamā's teacher used in Thig 3.2."),
        ("antaka",
         "&ldquo;terminator&rdquo; or death itself &mdash; the name "
         "Selā gives Māra in this poem's final word."),
    ],
    text_intro=(
        "The text in full: Māra's temptation, followed by Selā's reply. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.7:1.1-1.4"),
        ("p", "&sect;2", "thig3.7:2.1-2.4"),
        ("p", "&sect;3", "thig3.7:3.1-3.4"),
    ],
    quiz=[
        {"q": "What argument does Māra make in this poem's opening verse?",
         "opts": [
             "That Selā should return to her family",
             "That she should study harder",
             "That there's no escape in the world, so she should enjoy erotic delights instead",
             "That she has already succeeded and needs no further practice"],
         "correct": 2,
         "expl": "A direct, worldly case for indulgence rather than seclusion."},
        {"q": "How does Selā describe sensual pleasures in her reply?",
         "opts": [
             "Like swords and spears, with the aggregates as their chopping block",
             "As harmless amusements",
             "As identical to meditation itself",
             "She does not describe them at all"],
         "correct": 0,
         "expl": "A visceral counter-image, reframing Māra's offer as violence turned inward."},
        {"q": "What does Selā say about the term 'erotic delight' that Māra uses?",
         "opts": [
             "That she agrees it is delightful",
             "That she has never heard the term before",
             "She avoids the term entirely",
             "That it is now no delight for her at all"],
         "correct": 3,
         "expl": "She reclaims Māra's own word and empties it of its former hold on her."},
        {"q": "What name does Selā give Māra in this poem's final line?",
         "opts": [
             "Friend",
             "'Terminator' — antaka",
             "Teacher",
             "No name is given"],
         "correct": 1,
         "expl": "Addressing him directly as death itself."},
        {"q": "What closing quatrain does this poem share word for word with Thig 3.8?",
         "opts": [
             "'Though subject to so many painful things...'",
             "'I go for refuge to that sage, the Buddha'",
             "'Relishing is banished in every respect... you're beaten, terminator!'",
             "No closing lines are shared between the two poems"],
         "correct": 2,
         "expl": "The identical victorious formula answers two separate temptations."},
        {"q": "What earlier phrase in this book does this poem's closing echo?",
         "opts": [
             "Thig 3.1's twenty-five years",
             "Thig 3.2's 'having shattered the mass of darkness'",
             "Thig 3.5's arrow",
             "No earlier phrase is echoed"],
         "correct": 1,
         "expl": "Nearly identical wording for a decisive breakthrough."},
        {"q": "What structural feature makes this poem distinct from Thig 3.6?",
         "opts": [
             "It has no distinct feature",
             "It is entirely third person, like Thig 3.6",
             "It contains no dialogue at all",
             "It is a two-voice confrontation, not an outside voice praising its subject"],
         "correct": 3,
         "expl": "Māra speaks first, and Selā answers him directly."},
        {"q": "What does 'khandha' refer to in Selā's reply?",
         "opts": [
             "A place name",
             "The aggregates, described as the chopping block for the weapon of sensual pleasure",
             "A type of monastic robe",
             "Māra's own title"],
         "correct": 1,
         "expl": "The same term used for Uttamā's teaching in Thig 3.2."},
        {"q": "What position does this poem hold in the Book of the Threes?",
         "opts": [
             "The first poem",
             "The last poem",
             "The seventh poem, following Sukkā",
             "It is not part of the Book of the Threes"],
         "correct": 2,
         "expl": "Following Thig 3.6, opening this book's pair of direct Māra confrontations."},
        {"q": "What does 'Pāpimā' mean, as Selā addresses Māra?",
         "opts": [
             "'Wicked One'",
             "'Friend'",
             "'Teacher'",
             "'Terminator'"],
         "correct": 0,
         "expl": "A direct address distinct from the closing word 'antaka'."},
    ],
    marginalia=[
        ("A temptation, plainly argued", [
            "no escape, Māra says —",
            "enjoy delights instead"
        ]),
        ("Pleasure, recast as a weapon", [
            "swords and spears,",
            "the aggregates their target"
        ]),
        ("A word reclaimed", [
            "'delight' —",
            "no longer delight for her"
        ]),
        ("A formula shared with the poem after it", [
            "the same victory,",
            "word for word"
        ]),
    ],
    further=[
        '<a href="%s/thig3.7/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.6.html">Thig 3.6 &mdash; Sukk&amacr;</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="thig-3.8.html">Thig 3.8 &mdash; Som&amacr;</a> &mdash; '
        "the next poem, sharing this poem's exact closing quatrain.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 3.8 — Somā
# --------------------------------------------------------------------------- #
page(
    3, 8, "Som&amacr;", "Som&amacr;",
    meta_title="Thig 3.8 — Somā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Somā's verses closing the Book of the Threes, answering Māra's "
        "taunt about women's wisdom with one of the collection's most "
        "quoted retorts. From Ru-Yi Meditation Center."),
    vagga="The Book of the Threes &middot; Poem 8 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "the addressee is named only as Māra, the Wicked One"),
        ("Speaker", "Two voices: Māra, taunting Somā's capacity as a "
                    "woman, then Somā, refuting him directly"),
        ("Form", "Two four-line verses, closing the Book of the Threes"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "one of the collection's most direct statements "
                       "on gender and awakening"),
    ],
    why=(
        "This poem closes the Book of the Threes with Māra's sharpest "
        "taunt in this book: that with a woman's &lsquo;two-inch "
        "wisdom&rsquo;, the state the sages attain is simply not "
        "possible for her. Somā's reply &mdash; &lsquo;what difference "
        "does womanhood make when the mind is serene&rsquo; &mdash; is "
        "one of the most direct statements on gender and awakening "
        "anywhere in this collection, closing the book on a note of "
        "outright refutation."),
    guide=[
        ("A taunt naming gender directly", [
            "Māra's opening verse is specific in a way the taunt to Selā "
            "was not: &lsquo;that state's very challenging, it's for the "
            "sages to attain&mdash;with her two-inch wisdom, it's not "
            "possible for a woman&rsquo;, naming Somā's gender as the "
            "stated obstacle itself."]),
        ("A retort that refuses the premise entirely", [
            "Somā's reply does not argue that women can attain despite "
            "being women; it dismisses the category as irrelevant "
            "outright: &lsquo;what difference does womanhood make when "
            "the mind is serene, and knowledge is present, as you "
            "rightly discern the Dhamma&rsquo; &mdash; gender named only "
            "to be set aside as beside the point."]),
        ("The same closing quatrain as the poem just before it", [
            "&lsquo;Relishing is banished in every respect, and the mass "
            "of darkness is shattered... you're beaten, terminator!&rsquo; "
            "closes this poem exactly as it closed Thig 3.7 &mdash; the "
            "same victorious formula given to two different women "
            "answering two separate confrontations with Māra."]),
        ("A book's ending, marked in the source text itself", [
            "Bilara's underlying source data marks the line immediately "
            "after this poem's verses with &lsquo;Tikanipāto "
            "niṭṭhito&rsquo;, &lsquo;the Book of the Threes is "
            "finished&rsquo; &mdash; a bibliographic note, not part of "
            "the poem's own spoken content, but a structural close this "
            "guide preserves by ending here as well."]),
    ],
    terms=[
        ("Som&amacr;",
         "this poem's speaker, whose reply to Māra's taunt closes the "
         "Book of the Threes."),
        ("dva&#7749;gulapa&ntilde;&ntilde;a",
         "&ldquo;two-inch wisdom&rdquo; &mdash; Māra's taunt about a "
         "woman's capacity, directly named in his opening verse."),
        ("itthibh&amacr;va",
         "&ldquo;womanhood&rdquo; &mdash; the term Somā herself uses in "
         "asking what difference it makes to a serene mind."),
        ("susam&amacr;hita",
         "&ldquo;serene&rdquo; &mdash; the condition Somā names as what "
         "actually matters, in place of gender."),
        ("antaka",
         "&ldquo;terminator&rdquo; or death itself &mdash; the same word "
         "Selā used to address Māra in Thig 3.7's identical closing "
         "line."),
    ],
    text_intro=(
        "The text in full: Māra's taunt, followed by Somā's reply, "
        "closing the Book of the Threes. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig3.8:1.1-1.4"),
        ("p", "&sect;2", "thig3.8:2.1-2.4"),
        ("p", "&sect;3", "thig3.8:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does Māra's taunt claim, in this poem's opening verse?",
         "opts": [
             "That Somā has not meditated long enough",
             "With a woman's 'two-inch wisdom', the sages' state is not possible for her",
             "That Somā should return to lay life",
             "That the Dhamma itself is false"],
         "correct": 1,
         "expl": "A taunt naming her gender directly as the stated obstacle."},
        {"q": "How does Somā's reply treat the question of gender?",
         "opts": [
             "By agreeing that gender is a genuine obstacle",
             "By avoiding the topic entirely",
             "By arguing women can succeed despite being women",
             "By dismissing it as irrelevant to a serene, discerning mind"],
         "correct": 3,
         "expl": "'What difference does womanhood make when the mind is serene' — the premise itself is set aside."},
        {"q": "What two conditions does Somā name as what actually matters?",
         "opts": [
             "A serene mind and knowledge rightly discerning the Dhamma",
             "Physical strength and endurance",
             "Wealth and social standing",
             "No conditions are named"],
         "correct": 0,
         "expl": "Named directly in her reply's second half."},
        {"q": "What closing quatrain does this poem share word for word with Thig 3.7?",
         "opts": [
             "'Though subject to so many painful things...'",
             "'I go for refuge to that sage, the Buddha'",
             "'Relishing is banished in every respect... you're beaten, terminator!'",
             "No closing lines are shared"],
         "correct": 2,
         "expl": "The identical victorious formula given to two different women."},
        {"q": "What position does this poem hold in the Therigatha?",
         "opts": [
             "It opens the Book of the Threes",
             "It closes the Book of the Threes, the collection's third book",
             "It is the final poem of the entire collection",
             "It stands outside any book"],
         "correct": 1,
         "expl": "The eighth and last of this book's eight poems."},
        {"q": "What structural marker does the underlying source text place immediately after this poem?",
         "opts": [
             "A note naming the next book's first poem",
             "No marker at all",
             "A repeat of the poem's own text",
             "'Tikanipāto niṭṭhito' — 'the Book of the Threes is finished'"],
         "correct": 3,
         "expl": "A bibliographic close, not part of the poem's own spoken content."},
        {"q": "What does 'dvaṅgulapaññā' mean?",
         "opts": [
             "'Two-inch wisdom' — Māra's taunt about a woman's capacity",
             "'Serene mind'",
             "'Womanhood'",
             "'The Book of the Threes'"],
         "correct": 0,
         "expl": "Named directly in Māra's opening taunt."},
        {"q": "How does this poem's confrontation compare to Thig 3.7's?",
         "opts": [
             "Identical in every particular, including the taunt itself",
             "Māra's taunt here names gender specifically, rather than arguing for indulgence generally",
             "This poem contains no confrontation at all",
             "Somā does not reply to Māra at all"],
         "correct": 1,
         "expl": "A sharper, more specific taunt than Māra's argument to Selā."},
        {"q": "What does 'itthibhāva' mean?",
         "opts": [
             "'Terminator'",
             "'Two-inch wisdom'",
             "'Womanhood' — the term Somā herself uses in her reply",
             "'Serene'"],
         "correct": 2,
         "expl": "Named directly by Somā, then set aside as beside the point."},
        {"q": "What overall claim does Somā's reply make about the relationship between gender and awakening?",
         "opts": [
             "That gender determines who can awaken",
             "That only men can attain a serene, discerning mind",
             "That gender is irrelevant once the mind is serene and rightly discerns the Dhamma",
             "That the question cannot be answered"],
         "correct": 2,
         "expl": "One of this collection's most direct statements on the question."},
    ],
    marginalia=[
        ("A taunt, naming gender directly", [
            "'two-inch wisdom' —",
            "the stated obstacle"
        ]),
        ("A premise refused outright", [
            "not despite womanhood,",
            "but beside the point"
        ]),
        ("A formula shared with the poem before it", [
            "the same victory,",
            "word for word"
        ]),
        ("A book, closed in the source itself", [
            "'the Book of the Threes",
            "is finished'"
        ]),
    ],
    further=[
        '<a href="%s/thig3.8/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.7.html">Thig 3.7 &mdash; Sel&amacr;</a> &mdash; '
        "the poem immediately before this one, sharing this poem's exact "
        "closing quatrain.",
        '<a href="./">Therigatha</a> &mdash; back to the collection index.',
    ],
)


# --------------------------------------------------------------------------- #
# Thig 4.1 — Bhaddā Kāpilānī
# --------------------------------------------------------------------------- #
page(
    4, 1, "Bhadd&amacr; K&amacr;pil&amacr;n&imacr;", "Bhadd&amacr; "
    "Daughter of Kapila",
    meta_title="Thig 4.1 — Bhaddā Daughter of Kapila | Ru-Yi Meditation "
                "Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Book of the Fours' single poem, which sets Bhaddā Kāpilānī's "
        "attainment side by side, verse for verse, with the monk "
        "Kassapa's. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fours &middot; Poem 1 of 1",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; a "
                    "closing attribution names the speaker"),
        ("Speaker", "The nun Bhaddā Kāpilānī, whose own attainment is "
                    "set directly alongside the monk Kassapa's"),
        ("Form", "Four four-line verses, the entire Book of the Fours in "
                 "a single poem"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "notable chiefly for its structure, comparing two "
                       "named individuals point by point"),
    ],
    why=(
        "The Book of the Fours holds only one poem, and it is built "
        "unlike anything before it in this collection: the first two "
        "verses describe the monk Kassapa's attainment in detail, then "
        "the third verse states directly, &lsquo;in exactly the same "
        "way, Bhaddā daughter of Kapila is master of the three "
        "knowledges&rsquo; &mdash; a nun's realization measured, verse "
        "for verse, against a specific, named senior monk's, and found "
        "identical."),
    guide=[
        ("A book of one poem, built on comparison", [
            "Every other book in this collection so far gathers several "
            "poems under one length. The Book of the Fours holds exactly "
            "one, and its structure is unique among them: rather than "
            "narrating Bhaddā's own path alone, it opens by describing "
            "someone else's attainment first."]),
        ("Kassapa's three knowledges, stated in full", [
            "The poem's first two verses describe Kassapa &mdash; &lsquo;the "
            "son and heir of the Buddha, whose mind is immersed in "
            "samādhi&rsquo; &mdash; and name his three knowledges "
            "explicitly: knowing his own past lives, seeing heaven and "
            "places of loss, and having reached the end of rebirth."]),
        ("The identical claim, made for Bhaddā without qualification", [
            "&lsquo;In exactly the same way, Bhaddā daughter of Kapila is "
            "master of the three knowledges, conqueror of death&rsquo; "
            "&mdash; not a lesser or derivative attainment, but the same "
            "three knowledges, the same standing, restated for a second, "
            "named individual."]),
        ("A shared history, spoken in 'we'", [
            "The closing verse shifts from comparison into shared voice: "
            "&lsquo;seeing the danger of the world, both of us went "
            "forth... we've become cooled and quenched&rsquo; &mdash; "
            "later tradition holds that Bhaddā Kāpilānī and Kassapa had "
            "been a married couple before renouncing together, a "
            "background this closing verse's &lsquo;we&rsquo; fits "
            "without stating outright."]),
    ],
    terms=[
        ("Bhadd&amacr; K&amacr;pil&amacr;n&imacr;",
         "&ldquo;Bhaddā, daughter of Kapila&rdquo; &mdash; this poem's "
         "speaker, whose attainment is compared directly to Kassapa's."),
        ("Kassapa",
         "the senior monk named in this poem's opening verses, "
         "&ldquo;the son and heir of the Buddha&rdquo;, against whom "
         "Bhaddā's own attainment is measured."),
        ("tevijj&amacr;",
         "&ldquo;master of the three knowledges&rdquo; &mdash; the "
         "identical title this poem applies to both Kassapa and Bhaddā."),
        ("maccuh&amacr;yin&imacr;",
         "&ldquo;conqueror of death&rdquo; (or, by another gloss, "
         "&ldquo;one who has abandoned death&rdquo;) &mdash; Bhaddā's own "
         "epithet, in a martial register echoing &lsquo;having vanquished "
         "Māra&rsquo; just below it."),
        ("pabbajita",
         "&ldquo;gone forth&rdquo; &mdash; the shared act named in this "
         "poem's closing verse, spoken in the first person plural, "
         "&lsquo;we&rsquo;."),
    ],
    text_intro=(
        "The text in full: four verses, the entire Book of the Fours. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig4.1:1.1-1.4"),
        ("p", "&sect;2", "thig4.1:2.1-2.4"),
        ("p", "&sect;3", "thig4.1:3.1-3.4"),
        ("p", "&sect;4", "thig4.1:4.1-4.4"),
    ],
    quiz=[
        {"q": "How many poems does the Book of the Fours hold?",
         "opts": [
             "Ten",
             "Four",
             "Just one",
             "Eight"],
         "correct": 2,
         "expl": "The shortest book in the Therigatha so far, a single poem."},
        {"q": "Whose attainment does this poem describe first, before turning to Bhaddā's?",
         "opts": [
             "The monk Kassapa's",
             "The Buddha's own",
             "No one else's attainment is described",
             "Ānanda's"],
         "correct": 0,
         "expl": "The poem's first two verses describe Kassapa in detail."},
        {"q": "What three things does the poem name as Kassapa's 'three knowledges'?",
         "opts": [
             "Chanting, discipline, and meditation",
             "Wealth, status, and lineage",
             "Compassion, patience, and generosity",
             "Knowing past lives, seeing heaven and loss, and reaching the end of rebirth"],
         "correct": 3,
         "expl": "Named explicitly in the poem's first two verses."},
        {"q": "How does the poem describe Bhaddā's attainment relative to Kassapa's?",
         "opts": [
             "As a lesser, partial version of his",
             "'In exactly the same way' — identical, not derivative",
             "As entirely unrelated to his",
             "The poem does not compare the two"],
         "correct": 1,
         "expl": "A direct, unqualified claim of identical standing."},
        {"q": "What epithet does the poem give Bhaddā that echoes 'having vanquished Māra' just after it?",
         "opts": [
             "'Daughter of the sun'",
             "'Teacher of kings'",
             "'Conqueror of death' — maccuhāyinī",
             "No epithet is given"],
         "correct": 2,
         "expl": "A martial register, glossed by commentary as either 'abandoner' or 'conqueror' of death."},
        {"q": "What voice does the poem's closing verse shift into?",
         "opts": [
             "A stranger's voice, addressing both of them",
             "Māra's voice, taunting them both",
             "No shift in voice occurs",
             "The first person plural, 'we'"],
         "correct": 3,
         "expl": "'Both of us went forth... we've become cooled and quenched.'"},
        {"q": "What does later tradition hold about Bhaddā Kāpilānī and Kassapa's relationship, consistent with this poem's closing 'we'?",
         "opts": [
             "That they were siblings",
             "That they had been a married couple before renouncing together",
             "That they never met before ordaining",
             "That Kassapa was her teacher only"],
         "correct": 1,
         "expl": "This guide notes the tradition as background, distinct from what the verse itself states outright."},
        {"q": "What does 'tevijjā' mean?",
         "opts": [
             "'Master of the three knowledges' — applied identically to both Kassapa and Bhaddā",
             "'Gone forth'",
             "'The danger of the world'",
             "'A married couple'"],
         "correct": 0,
         "expl": "The shared title this poem gives to both figures."},
        {"q": "What structural feature makes this poem unique among the books completed so far in this collection?",
         "opts": [
             "It has no structural features",
             "It is identical in form to Thig 3.6's third-person praise",
             "It measures a nun's attainment point by point against a specific, named senior monk's",
             "It is the collection's shortest poem overall"],
         "correct": 2,
         "expl": "No earlier poem in this collection builds itself as an explicit comparison to a named monk."},
        {"q": "What structural marker does bilara-data's underlying source place immediately after this poem, alongside an attribution stub naming Bhaddā Kāpilānī?",
         "opts": [
             "'Catukkanipāto niṭṭhito' — 'the Book of the Fours is finished'",
             "A note naming the next book's first poem",
             "No marker at all",
             "A repeat of the poem's own text"],
         "correct": 0,
         "expl": "The same kind of bibliographic close seen at the end of the Book of the Threes."},
    ],
    marginalia=[
        ("One book, one poem", [
            "the shortest book",
            "so far"
        ]),
        ("Kassapa, named first", [
            "his three knowledges,",
            "stated in full"
        ]),
        ("Identical, not derivative", [
            "'in exactly the same way' —",
            "the same standing"
        ]),
        ("A shared voice, closing", [
            "'both of us went forth' —",
            "spoken as 'we'"
        ]),
    ],
    further=[
        '<a href="%s/thig4.1/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-3.8.html">Thig 3.8 &mdash; Som&amacr;</a> &mdash; '
        "the poem immediately before this one, closing the Book of the "
        "Threes.",
        '<a href="./">Therigatha</a> &mdash; back to the collection index.',
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.1 — An Unnamed Nun (2nd)
# --------------------------------------------------------------------------- #
page(
    5, 1, "A&ntilde;&ntilde;atarather&imacr;", "An Unnamed Nun (2nd)",
    meta_title="Thig 5.1 — An Unnamed Nun (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "poem opening the Book of the Fives, an anonymous nun's account "
        "closing on the fullest enumeration yet of the six kinds of "
        "direct knowledge. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 1 of 12",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "An unnamed nun, narrating twenty-five years of "
                    "failure and then a teacher-guided breakthrough"),
        ("Form", "Five verses, mostly four lines, the last extending to "
                 "six"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "closes on the fullest list yet of the six kinds "
                       "of direct knowledge"),
    ],
    why=(
        "This poem opens the Book of the Fives exactly as an unnamed "
        "voice opened the Book of the Ones in Thig 1.1, and its own "
        "opening verses echo two poems from the book just finished: "
        "twenty-five years of failure, as in Thig 3.1, and a teacher's "
        "instruction in &lsquo;the aggregates, sense fields, and "
        "elements&rsquo;, the identical phrase used for Uttamā's teacher "
        "in Thig 3.2."),
    guide=[
        ("A second unnamed nun, opening a new book", [
            "This poem's title, &lsquo;An Unnamed Nun (2nd)&rsquo;, "
            "points directly back to Thig 1.1, the collection's very "
            "first poem &mdash; an anonymous voice opens the Book of the "
            "Fives just as one opened the Book of the Ones."]),
        ("Twenty-five years, told more viscerally than before", [
            "&lsquo;In the twenty-five years since I went forth, I have "
            "not found peace of mind, even for as long as a "
            "finger-snap&rsquo; echoes Thig 3.1's identical span, but "
            "adds a physical image absent there: &lsquo;I cried with "
            "flailing arms as I entered a dwelling&rsquo;."]),
        ("The identical teaching phrase reused from Thig 3.2", [
            "&lsquo;She taught me the Dhamma: the aggregates, sense "
            "fields, and elements&rsquo; repeats, word for word, the "
            "compound term &lsquo;khandhāyatanadhātuyo&rsquo; that "
            "Uttamā's teacher used in Thig 3.2 &mdash; the same "
            "instruction, given by a different trusted nun to a "
            "different anonymous student."]),
        ("The fullest list yet of the six direct knowledges", [
            "Where earlier poems named three knowledges, this one's "
            "closing verse names all six in sequence: past lives, "
            "clairvoyance, reading others' minds, clairaudience, psychic "
            "powers, and the ending of defilements &mdash; the most "
            "complete enumeration of this standard list anywhere in the "
            "collection so far."]),
    ],
    terms=[
        ("cittassūpasama",
         "&ldquo;peace of mind&rdquo; &mdash; what this nun says she "
         "failed to find for twenty-five years, echoing Thig 3.1's "
         "identical span."),
        ("khandh&amacr;yatanadh&amacr;tuyo",
         "&ldquo;the aggregates, sense fields, and elements&rdquo; "
         "&mdash; the identical compound term used for Uttamā's teacher "
         "in Thig 3.2."),
        ("cetopariccañ&amacr;&#7751;a",
         "the ability to encompass and read the minds of others, one of "
         "the six direct knowledges named in this poem's closing verse."),
        ("iddhi",
         "psychic powers, another of the six direct knowledges this poem "
         "names as realized."),
        ("cha&#7799;abhi&ntilde;&ntilde;&amacr;",
         "&ldquo;the six kinds of direct knowledge&rdquo; &mdash; named "
         "as a complete set only here, more fully than in any earlier "
         "poem in this collection."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.1:1.1-1.4"),
        ("p", "&sect;2", "thig5.1:2.1-2.4"),
        ("p", "&sect;3", "thig5.1:3.1-3.4"),
        ("p", "&sect;4", "thig5.1:4.1-4.4"),
        ("p", "&sect;5", "thig5.1:5.1-5.6"),
    ],
    quiz=[
        {"q": "What does this poem's title, 'An Unnamed Nun (2nd)', point back to?",
         "opts": [
             "Nothing in particular",
             "Thig 1.1, the collection's very first poem, also spoken by an unnamed nun",
             "Thig 3.1's Sāmā",
             "The Book of the Fours' single poem"],
         "correct": 1,
         "expl": "An anonymous voice opens this book just as one opened the Book of the Ones."},
        {"q": "How does this poem describe her twenty-five years of failure?",
         "opts": [
             "As entirely peaceful",
             "With no description at all",
             "As a minor inconvenience",
             "She had not found peace of mind, even for as long as a finger-snap"],
         "correct": 3,
         "expl": "An even briefer unit of time than most of this collection's confessions of failure."},
        {"q": "What physical detail does this poem add to its confession of failure?",
         "opts": [
             "She cried with flailing arms as she entered a dwelling",
             "She fainted",
             "No physical detail is given",
             "She fled to a distant city"],
         "correct": 0,
         "expl": "A vivid, embodied image absent from Thig 3.1's version of this same confession."},
        {"q": "What phrase does this poem's teacher use, word for word identical to Thig 3.2's Uttamā's teacher?",
         "opts": [
             "'The victor's instructions'",
             "'Twenty-five years'",
             "'The aggregates, sense fields, and elements'",
             "No phrase is shared"],
         "correct": 2,
         "expl": "'Khandhāyatanadhātuyo' — the identical compound term."},
        {"q": "How many of the six direct knowledges does this poem's closing verse name?",
         "opts": [
             "Three",
             "All six, in full sequence",
             "Only one",
             "None are named"],
         "correct": 1,
         "expl": "The fullest enumeration of this standard list anywhere in the collection so far."},
        {"q": "What does 'iddhi' refer to, among the six knowledges named here?",
         "opts": [
             "Reading others' minds",
             "Clairaudience",
             "Psychic powers",
             "Knowing past lives"],
         "correct": 2,
         "expl": "Named directly among the six, distinct from the other five."},
        {"q": "What does 'cetopariccañāṇa' mean?",
         "opts": [
             "The ending of defilements",
             "The ability to encompass and read the minds of others",
             "Purified clairvoyance",
             "A trusted teacher"],
         "correct": 1,
         "expl": "One of the six direct knowledges named in this poem's final verse."},
        {"q": "What position does this poem hold in the Therigatha as a whole?",
         "opts": [
             "It closes the Book of the Fours",
             "It is the final poem of the entire collection",
             "It stands outside any book",
             "It opens the Book of the Fives, the collection's fifth book"],
         "correct": 3,
         "expl": "The first of twelve poems in this new book."},
        {"q": "What does 'khandhāyatanadhātuyo' name?",
         "opts": [
             "A place name",
             "The name of this nun's teacher",
             "The aggregates, sense fields, and elements — three analytical categories",
             "A type of ordination"],
         "correct": 2,
         "expl": "The same compound term taught to Uttamā in Thig 3.2."},
        {"q": "How does this poem's structure compare to Thig 3.1 and Thig 3.2's?",
         "opts": [
             "It echoes elements of both: the twenty-five-year span of 3.1 and the teacher's exact instruction from 3.2",
             "It shares nothing with either poem",
             "It is identical to Thig 3.1 in every line",
             "It shares only its title with any earlier poem"],
         "correct": 0,
         "expl": "A poem that draws together two earlier confessions and teachings into one account."},
    ],
    marginalia=[
        ("A second unnamed nun", [
            "opening this book,",
            "as one opened the first"
        ]),
        ("Failure, told more viscerally", [
            "flailing arms,",
            "crying aloud"
        ]),
        ("A teaching, reused word for word", [
            "the same phrase",
            "as Thig 3.2"
        ]),
        ("Six knowledges, named in full", [
            "the fullest list",
            "so far"
        ]),
    ],
    further=[
        '<a href="%s/thig5.1/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-4.1.html">Thig 4.1 &mdash; Bhadd&amacr; Daughter of '
        "Kapila</a> &mdash; the poem immediately before this one, closing "
        "the Book of the Fours.",
        '<a href="thig-1.1.html">Thig 1.1 &mdash; An Unnamed Nun</a> '
        "&mdash; the poem this one's title points back to, opening the "
        "entire collection.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.2 — Vimalā, the Former Courtesan
# --------------------------------------------------------------------------- #
page(
    5, 2, "Vimal&amacr;", "Vimal&amacr;, the Former Courtesan",
    meta_title="Thig 5.2 — Vimalā, the Former Courtesan | Ru-Yi "
                "Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vimalā's verses, the collection's most vivid account yet from a "
        "former courtesan, contrasting her old trade with her later "
        "freedom from thought. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 2 of 12",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "The nun Vimalā, speaking in the first person about "
                    "her former livelihood and her present practice"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "collection's most vivid account from a former "
                       "courtesan"),
    ],
    why=(
        "This poem's title states its subject directly: &lsquo;Vimalā, "
        "the Former Courtesan&rsquo;. Where Thig 2.4's Aḍḍhakāsi named "
        "her former price and moved quickly past it, Vimalā's own "
        "account lingers longer on the specifics of her old trade "
        "&mdash; vanity, seduction, a self-description as a hunter "
        "setting a snare &mdash; before turning, in the space of a "
        "single verse, to alms-round, a shaved head, and a mind free of "
        "thought."),
    guide=[
        ("A second former courtesan, described more fully", [
            "Thig 2.4's Aḍḍhakāsi named her former worth and moved on "
            "quickly. Vimalā's account is longer and more specific about "
            "the trade itself &mdash; standing &lsquo;at the brothel "
            "door&rsquo;, adorning her body, and openly displaying "
            "herself to draw customers in."]),
        ("A hunter's snare, applied to herself", [
            "&lsquo;I stood at the brothel door, like a hunter setting a "
            "snare&rsquo; is Vimalā's own self-description, not an "
            "outside judgment &mdash; she names her former conduct as "
            "predatory toward the men she drew in, a harsher "
            "self-assessment than most confessions in this collection."]),
        ("A single verse spans the entire change", [
            "&lsquo;Today, having wandered for alms, my head shaven, "
            "wearing the outer robe&rsquo; opens the poem's fourth verse "
            "with the present tense &lsquo;today&rsquo;, setting the "
            "whole of her former trade against the whole of her new life "
            "in one compact turn."]),
        ("Freedom from thought, an unusual way to name attainment", [
            "&lsquo;I've gained freedom from thought&rsquo; "
            "(<em>avitakka</em>) is a distinctive way to describe "
            "realization, less common in this collection than "
            "&lsquo;peace of mind&rsquo; or &lsquo;quenching&rsquo; "
            "&mdash; naming the cessation of discursive thought itself "
            "as what she gained, before the closing verse's more usual "
            "formula of defilements ended."]),
    ],
    terms=[
        ("Vimal&amacr;",
         "this poem's speaker, whose title names her former trade "
         "directly: &lsquo;Vimalā, the Former Courtesan&rsquo;."),
        ("vesidv&amacr;ra",
         "&ldquo;the brothel door&rdquo; &mdash; the specific site named "
         "in this poem's second verse."),
        ("avitakka",
         "&ldquo;freedom from thought&rdquo; &mdash; Vimalā's own "
         "distinctive description of what she gained, naming the "
         "cessation of discursive thought."),
        ("yoga",
         "the &ldquo;yokes&rdquo; or bonds, human and heavenly, this "
         "poem describes as entirely severed in its closing verse."),
        ("&amacr;sava",
         "&ldquo;defilements&rdquo; &mdash; wiped out entirely, in the "
         "poem's final line, before she describes herself as "
         "&lsquo;cooled and quenched&rsquo;."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.2:1.1-1.4"),
        ("p", "&sect;2", "thig5.2:2.1-2.4"),
        ("p", "&sect;3", "thig5.2:3.1-3.4"),
        ("p", "&sect;4", "thig5.2:4.1-4.4"),
        ("p", "&sect;5", "thig5.2:5.1-5.4"),
    ],
    quiz=[
        {"q": "What does this poem's title state directly about Vimalā?",
         "opts": [
             "Nothing about her past",
             "That she was a queen",
             "That she was formerly a courtesan",
             "That she was a teacher of doctrine"],
         "correct": 2,
         "expl": "'Vimalā, the Former Courtesan' — the title itself names her trade."},
        {"q": "How does Vimalā describe herself at the brothel door?",
         "opts": [
             "Like a hunter setting a snare",
             "As a reluctant, unwilling participant",
             "The poem gives no description of this scene",
             "As indifferent to the men who came"],
         "correct": 0,
         "expl": "Her own self-description, naming her former conduct as predatory."},
        {"q": "How does this poem's account compare to Thig 2.4's Aḍḍhakāsi?",
         "opts": [
             "Identical in every detail",
             "Aḍḍhakāsi's account is longer and more explicit",
             "Neither poem mentions a former trade",
             "Vimalā's account lingers longer on the specifics of the trade itself"],
         "correct": 3,
         "expl": "Aḍḍhakāsi names her price and moves on quickly; Vimalā's account is fuller."},
        {"q": "What word marks the turn to Vimalā's new life, in the poem's fourth verse?",
         "opts": [
             "'Tomorrow'",
             "'Today'",
             "'Long ago'",
             "No specific word marks a turn"],
         "correct": 1,
         "expl": "'Today, having wandered for alms' — the present tense frames the whole shift."},
        {"q": "What does Vimalā say she gained, in an unusual formulation for this collection?",
         "opts": [
             "Wealth",
             "Freedom from thought",
             "A large following of students",
             "Nothing is named"],
         "correct": 1,
         "expl": "'Avitakka' — the cessation of discursive thought, distinct from this collection's more usual formulas."},
        {"q": "What does this poem's closing verse say about the 'yokes', human and heavenly?",
         "opts": [
             "That they remain unresolved",
             "That only some are cut off",
             "All are severed",
             "The poem does not mention them"],
         "correct": 2,
         "expl": "A complete, unqualified claim, closing the poem."},
        {"q": "What does 'āsava' mean, as used in this poem's final line?",
         "opts": [
             "'Ornaments'",
             "'A hunter's snare'",
             "'The brothel door'",
             "'Defilements' — wiped out entirely, by her own account"],
         "correct": 3,
         "expl": "Named directly as ended, just before she calls herself 'cooled and quenched'."},
        {"q": "How does Vimalā describe her own former conduct toward the men she drew in?",
         "opts": [
             "As entirely blameless",
             "As a predatory act, comparing herself to a hunter",
             "As someone else's fault, not her own",
             "The poem does not address this"],
         "correct": 1,
         "expl": "A harsher self-assessment than most confessions in this collection."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The last poem",
             "It stands outside this book",
             "The second poem, following the unnamed nun who opens the book",
             "The first poem"],
         "correct": 2,
         "expl": "Following Thig 5.1, continuing the Book of the Fives."},
        {"q": "What does 'vesidvāra' mean?",
         "opts": [
             "'The brothel door' — the site named in this poem's second verse",
             "'Freedom from thought'",
             "'A shaven head'",
             "'The outer robe'"],
         "correct": 0,
         "expl": "The specific site of her former trade, named directly."},
    ],
    marginalia=[
        ("A trade, named and described", [
            "more fully than",
            "Aḍḍhakāsi's account"
        ]),
        ("A hunter, a snare", [
            "her own self-description,",
            "not an outside verdict"
        ]),
        ("'Today' — the whole turn in one word", [
            "the former trade,",
            "set against the new life"
        ]),
        ("Freedom from thought", [
            "a distinctive phrase,",
            "naming a different kind of gain"
        ]),
    ],
    further=[
        '<a href="%s/thig5.2/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.1.html">Thig 5.1 &mdash; An Unnamed Nun (2nd)</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-2.4.html">Thig 2.4 &mdash; A&#7693;&#7693;hak&amacr;si'
        "</a> &mdash; another former courtesan's account, earlier in this "
        "collection.",
        '<a href="thig-5.3.html">Thig 5.3 &mdash; S&imacr;h&amacr;</a> '
        "&mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.3 — Sīhā
# --------------------------------------------------------------------------- #
page(
    5, 3, "S&imacr;h&amacr;", "S&imacr;h&amacr;",
    meta_title="Thig 5.3 — Sīhā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sīhā's verses, seven years of suffering under desire's grip, "
        "resolved at the exact moment of what should have been despair. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 3 of 12",
    glance=[
        ("Setting", "Seven years of struggle, then a forest, at a moment "
                    "of extremity"),
        ("Speaker", "The nun Sīhā, recounting seven years of failed "
                    "effort and a sudden turn"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; one "
                       "of this collection's starkest accounts of "
                       "prolonged suffering"),
    ],
    why=(
        "This poem recounts seven years of suffering under the grip of "
        "desire &mdash; described in stark physical terms, &lsquo;thin, "
        "pale, and wan&rsquo; &mdash; before Sīhā, at what the verses "
        "present as a point of complete exhaustion, resolves to end her "
        "life in the forest rather than continue as she had been. The "
        "poem's turn comes at the precise moment that resolve is carried "
        "out: her mind, the verses say, was freed."),
    guide=[
        ("Seven years, told in the body's own terms", [
            "&lsquo;Thin, pale, and wan&rsquo; describes seven years of "
            "wandering under &lsquo;irrational application of mind&rsquo; "
            "and desire's grip &mdash; the toll measured physically, not "
            "only as an inner report of unhappiness."]),
        ("A resolve reached only after prolonged failure", [
            "Sīhā's decision to end her life in the forest is not "
            "impulsive within the poem's own account: it follows seven "
            "full years of &lsquo;finding no happiness by day or "
            "night&rsquo;, presented as the exhausted end of sustained, "
            "failed effort rather than a sudden reaction."]),
        ("A noose, echoing the poem just before it", [
            "&lsquo;Pāsa&rsquo;, the noose Sīhā ties, is the same word "
            "Vimalā used one poem earlier as a metaphor for her former "
            "predatory conduct &mdash; here made literal, a striking "
            "echo across two consecutive poems in this book."]),
        ("The turn, at the exact moment of extremity", [
            "&lsquo;Casting it round my neck, my mind was freed&rsquo; "
            "places the poem's entire resolution at the single instant "
            "of complete confrontation with death &mdash; the verses "
            "offer no account of what shifted, only that it did, exactly "
            "there."]),
    ],
    terms=[
        ("S&imacr;h&amacr;",
         "this poem's speaker, whose account of seven years' struggle "
         "closes on a single, unexplained turn."),
        ("ayoniso manasik&amacr;ra",
         "&ldquo;irrational application of mind&rdquo; &mdash; named in "
         "this poem's opening line as the root of her seven years of "
         "suffering."),
        ("k&amacr;mar&amacr;ga",
         "desire for sensual pleasures, named twice in this poem as what "
         "afflicted her."),
        ("p&amacr;sa",
         "&ldquo;noose&rdquo; or &ldquo;snare&rdquo; &mdash; the same "
         "word Vimalā used metaphorically in Thig 5.2, here the literal "
         "object Sīhā ties."),
        ("cittaṁ vimucci",
         "&ldquo;my mind was freed&rdquo; &mdash; this poem's closing "
         "line, and its entire account of resolution."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.3:1.1-1.4"),
        ("p", "&sect;2", "thig5.3:2.1-2.4"),
        ("p", "&sect;3", "thig5.3:3.1-3.4"),
        ("p", "&sect;4", "thig5.3:4.1-4.4"),
        ("p", "&sect;5", "thig5.3:5.1-5.4"),
    ],
    quiz=[
        {"q": "What does this poem name as the root of Sīhā's seven years of suffering?",
         "opts": [
             "A specific illness",
             "Irrational application of mind, and desire for sensual pleasures",
             "Poverty",
             "No cause is named"],
         "correct": 1,
         "expl": "Named directly in the poem's opening lines."},
        {"q": "How does the poem describe the physical toll of these seven years?",
         "opts": [
             "It describes no physical toll",
             "As a source of increased strength",
             "As entirely unnoticeable to others",
             "'Thin, pale, and wan' — measured in the body, not only in feeling"],
         "correct": 3,
         "expl": "A stark, physical description of prolonged suffering."},
        {"q": "How does the poem present Sīhā's resolve to end her life?",
         "opts": [
             "As the exhausted end of seven years of failed effort, not an impulsive reaction",
             "As a sudden, unexplained whim",
             "As advice given to her by another nun",
             "The poem does not describe this at all"],
         "correct": 0,
         "expl": "Presented as the culmination of prolonged, sustained struggle."},
        {"q": "What word does this poem use for the noose, shared with a metaphor in the poem just before it?",
         "opts": [
             "Khandha",
             "Pāsa — 'noose' or 'snare', which Vimalā used metaphorically in Thig 5.2",
             "Āsava",
             "No word is shared between the two poems"],
         "correct": 1,
         "expl": "A striking echo: metaphorical in Thig 5.2, literal here."},
        {"q": "At what precise moment does the poem locate Sīhā's turn toward freedom?",
         "opts": [
             "Years afterward, in quiet reflection",
             "Before she ever entered the forest",
             "The poem does not specify a moment",
             "The exact moment of casting the noose around her neck"],
         "correct": 3,
         "expl": "'Casting it round my neck, my mind was freed' — the resolution and the moment are identical."},
        {"q": "Does the poem explain what caused her mind to be freed at that moment?",
         "opts": [
             "Yes, in extensive detail",
             "No — the verses state only that it happened, not why",
             "It attributes the change to another person's intervention",
             "It says nothing changed at all"],
         "correct": 1,
         "expl": "The poem offers the fact of the turn without an explanation for it."},
        {"q": "What does 'ayoniso manasikāra' mean?",
         "opts": [
             "'My mind was freed'",
             "'Thin, pale, and wan'",
             "'Irrational application of mind' — named as the root of her suffering",
             "'A noose'"],
         "correct": 2,
         "expl": "Named in this poem's very first line."},
        {"q": "How long does the poem say Sīhā wandered in this state of suffering?",
         "opts": [
             "One year",
             "A single day",
             "Seven years",
             "The duration is not given"],
         "correct": 2,
         "expl": "'For seven years I wandered... finding no happiness by day or night.'"},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The first poem",
             "The last poem",
             "It stands outside this book",
             "The third poem, following Vimalā"],
         "correct": 3,
         "expl": "Following Thig 5.2, continuing the Book of the Fives."},
        {"q": "What does 'kāmarāga' mean?",
         "opts": [
             "Desire for sensual pleasures — named twice as what afflicted Sīhā",
             "A place in the forest",
             "'Seven years'",
             "A type of noose"],
         "correct": 0,
         "expl": "Named directly in this poem's opening verses as the source of her struggle."},
    ],
    marginalia=[
        ("Seven years, in the body's terms", [
            "thin, pale, wan —",
            "the toll measured physically"
        ]),
        ("A resolve, not an impulse", [
            "reached only after",
            "years of failed effort"
        ]),
        ("A noose, made literal", [
            "the same word",
            "as Thig 5.2's metaphor"
        ]),
        ("The turn, unexplained", [
            "only that it happened,",
            "not why"
        ]),
    ],
    further=[
        '<a href="%s/thig5.3/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.2.html">Thig 5.2 &mdash; Vimal&amacr;, the Former '
        "Courtesan</a> &mdash; the poem immediately before this one, "
        "sharing the word for &lsquo;noose&rsquo; this poem makes literal.",
        '<a href="thig-5.4.html">Thig 5.4 &mdash; Sundar&imacr;nand&amacr;'
        "</a> &mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.4 — Sundarīnandā
# --------------------------------------------------------------------------- #
page(
    5, 4, "Sundar&imacr;nand&amacr;", "Sundar&imacr;nand&amacr;",
    meta_title="Thig 5.4 — Sundarīnandā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sundarīnandā's verses, opening with the identical instruction "
        "given to Nandā in Thig 2.1, now followed by her own completed "
        "realization. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 4 of 12",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "a fragmentary closing attribution names the "
                    "speaker"),
        ("Speaker", "Two quoted blocks: an instruction addressed to "
                    "Nandā, then her own first-person account of "
                    "realization"),
        ("Form", "Five four-line verses, in two quoted blocks of three "
                 "and two"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "opens with a word-for-word repetition from "
                       "earlier in this collection"),
    ],
    why=(
        "This poem's opening two verses are identical, word for word, to "
        "Thig 2.1's instruction to the trainee nun Nandā &mdash; whose "
        "own closing attribution notes that the Buddha &lsquo;regularly "
        "advised&rsquo; her this way. Where Thig 2.1 stopped at the "
        "instruction itself, this poem continues: three more verses "
        "carry the same address into an account of the body examined, "
        "disillusionment following, and a mind finally at peace."),
    guide=[
        ("An opening repeated word for word", [
            "&lsquo;Nandā, see this bag of bones as diseased, filthy, "
            "and rotten. With mind unified and serene, meditate on the "
            "ugly aspects of the body&rsquo; is identical, segment for "
            "segment, to Thig 2.1's opening instruction &mdash; the same "
            "address to the same name."]),
        ("An instruction given 'regularly', now shown taking root", [
            "Thig 2.1's own closing line states that &lsquo;the Buddha "
            "regularly advised the trainee nun Nandā with these "
            "verses&rsquo;. This poem does not simply repeat that "
            "instruction; it extends the same quoted address three "
            "verses further, into the reflection it produced."]),
        ("A first quoted block, ending inside its own reflection", [
            "The source text's quotation marks span three full verses "
            "here, not two &mdash; opening with the bag-of-bones "
            "instruction and closing only after &lsquo;reflecting in "
            "such a way, tireless all day and night, having broken "
            "through with my own wisdom, I saw&rsquo;, the address "
            "folding into its own outcome before the quote closes."]),
        ("A second block, her realization made explicit", [
            "A separate quoted block follows, unambiguously in her own "
            "voice: &lsquo;I truly saw this body both inside and "
            "out... growing disillusioned with the body, I became "
            "dispassionate within... I'm quenched and at peace&rsquo; "
            "&mdash; the instruction's completed result, stated "
            "directly."]),
    ],
    terms=[
        ("Sundar&imacr;nand&amacr;",
         "this poem's speaker, addressed by the shorter name "
         "&lsquo;Nandā&rsquo; within the verses, which open identically "
         "to Thig 2.1's instruction."),
        ("asubha",
         "&ldquo;the unattractive&rdquo; or &ldquo;foulness&rdquo; "
         "&mdash; the same meditation category named in Thig 2.1's "
         "instruction, repeated here word for word."),
        ("yoniso",
         "&ldquo;rationally&rdquo; or &ldquo;wisely&rdquo; &mdash; how "
         "this poem describes her own investigation of the body, in its "
         "second quoted block."),
        ("santarab&amacr;hira",
         "&ldquo;inside and out&rdquo; &mdash; the completeness this "
         "poem claims for her examination of the body."),
        ("nibbindati",
         "to become disillusioned or dispassionate &mdash; the state "
         "this poem names directly before its closing description of "
         "peace."),
    ],
    text_intro=(
        "The text in full: five verses in two quoted blocks. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.4:1.1-3.4"),
        ("p", "&sect;2", "thig5.4:4.1-5.4"),
    ],
    quiz=[
        {"q": "What do this poem's opening two verses share with Thig 2.1?",
         "opts": [
             "They are word-for-word identical",
             "Nothing at all",
             "Only the speaker's name is shared",
             "Only the closing line is shared"],
         "correct": 0,
         "expl": "'Nandā, see this bag of bones...' — the identical instruction, segment for segment."},
        {"q": "What does Thig 2.1's own closing line say about this instruction?",
         "opts": [
             "That it was given only once",
             "The Buddha regularly advised Nandā with these verses",
             "That it was written down by someone else entirely",
             "That Nandā rejected the instruction"],
         "correct": 1,
         "expl": "Explaining why the same words could recur, addressed to the same name."},
        {"q": "How many verses does this poem's opening quoted block span, according to the source text's punctuation?",
         "opts": [
             "One",
             "Five",
             "Two",
             "Three"],
         "correct": 3,
         "expl": "Unlike Thig 2.1's two verses, this poem's first quoted block extends to three."},
        {"q": "What does the poem's second quoted block describe?",
         "opts": [
             "A completely different, unrelated topic",
             "Her own realization: seeing the body fully, growing disillusioned, and reaching peace",
             "A dialogue with Māra",
             "Advice given to yet another nun"],
         "correct": 1,
         "expl": "The instruction's completed result, stated directly in her own voice."},
        {"q": "What does 'santarabāhira' mean?",
         "opts": [
             "'Inside and out' — the completeness of her examination of the body",
             "'Regularly advised'",
             "'A bag of bones'",
             "'Disillusioned'"],
         "correct": 0,
         "expl": "Naming the thoroughness of her investigation."},
        {"q": "What is this poem's relationship to Thig 2.1?",
         "opts": [
             "They share nothing in common",
             "This poem is set in an entirely different book with no textual connection",
             "This poem opens with the same instruction, then extends into an account of its result",
             "Thig 2.1 is the later poem, referencing this one"],
         "correct": 2,
         "expl": "A shared opening, followed by new material unique to this poem."},
        {"q": "What does 'nibbindati' describe?",
         "opts": [
             "Becoming disillusioned or dispassionate, named just before the poem's closing description of peace",
             "The act of shaving one's head",
             "A formal ordination",
             "The instruction's opening line"],
         "correct": 3,
         "expl": "Marking the shift from investigation to release."},
        {"q": "How does this poem close?",
         "opts": [
             "With a question left unanswered",
             "Mid-instruction, without any resolution",
             "With the 'no more future lives' formula",
             "'I'm quenched and at peace'"],
         "correct": 3,
         "expl": "A direct statement of completed peace."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The first poem",
             "The last poem",
             "The fourth poem, following Sīhā",
             "It stands outside this book"],
         "correct": 2,
         "expl": "Following Thig 5.3, continuing the Book of the Fives."},
        {"q": "What does 'yoniso' mean, as used in this poem's second block?",
         "opts": [
             "'A bag of bones'",
             "'Rationally' or 'wisely' — how she investigated the body",
             "'The unattractive'",
             "'Filthy and rotten'"],
         "correct": 1,
         "expl": "Describing the quality of her own examination, distinct from the instruction's opening imagery."},
    ],
    marginalia=[
        ("An opening, repeated exactly", [
            "the same words",
            "as Thig 2.1"
        ]),
        ("'Regularly advised' — now shown taking root", [
            "the same instruction,",
            "finally realized"
        ]),
        ("One quotation, spanning three verses", [
            "not two, as in",
            "Thig 2.1"
        ]),
        ("A second block, unambiguous", [
            "her own voice,",
            "her own peace"
        ]),
    ],
    further=[
        '<a href="%s/thig5.4/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.3.html">Thig 5.3 &mdash; S&imacr;h&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-2.1.html">Thig 2.1 &mdash; Abhir&umacr;panand&amacr;'
        "</a> &mdash; the poem whose opening instruction this one repeats "
        "word for word.",
        '<a href="thig-5.5.html">Thig 5.5 &mdash; Nanduttar&amacr;</a> '
        "&mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.5 — Nanduttarā
# --------------------------------------------------------------------------- #
page(
    5, 5, "Nanduttar&amacr;", "Nanduttar&amacr;",
    meta_title="Thig 5.5 — Nanduttarā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Nanduttarā's verses, describing years of ascetic vows and "
        "unresolved vanity before faith finally brought her to the "
        "Buddha's path. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 5 of 12",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "The nun Nanduttarā, recounting a religious life "
                    "before the Buddha's path, then her going forth"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "juxtaposes ascetic observance with unresolved "
                       "vanity in the same account"),
    ],
    why=(
        "This poem's speaker describes a religious life already underway "
        "before she ever went forth as a Buddhist nun &mdash; worshiping "
        "the sacred flame, the sun and moon, undertaking many vows, "
        "sleeping on the ground &mdash; and admits, in the very next "
        "verse, that she still &lsquo;loved ornaments and decorations&rsquo; "
        "and pandered to her own body. Only when she &lsquo;gained "
        "faith&rsquo; and went forth to homelessness did her account "
        "describe an actual change."),
    guide=[
        ("A religious life, before this collection's own tradition", [
            "&lsquo;In the past I worshiped the sacred flame, the moon, "
            "the sun, and the gods&rsquo; describes devotional practice "
            "outside the Buddha's path &mdash; vows undertaken, half her "
            "head shaved, sleeping on bare ground, no food eaten at "
            "night."]),
        ("Vanity, admitted alongside the austerity", [
            "The very next verse undercuts any sense of steady progress: "
            "&lsquo;I loved my ornaments and decorations, and with baths "
            "and oil-massages, I pandered to this body&rsquo; &mdash; "
            "elaborate external observance sitting, by her own account, "
            "beside unresolved attachment to appearance."]),
        ("Faith named as the actual turning point", [
            "&lsquo;But then I gained faith, and went forth to "
            "homelessness&rsquo; marks a distinct change from everything "
            "before it &mdash; not another vow or austerity, but "
            "&lsquo;saddhā&rsquo;, faith, named as what actually "
            "produced change where ritual observance alone had not."]),
        ("Seeing the body, where austerity had not reached", [
            "&lsquo;Truly seeing the body, desire for sensual pleasure is "
            "eradicated&rsquo; completes the contrast: the same body "
            "that survived years of vows and worship untransformed is "
            "resolved not by further austerity, but by seeing it "
            "&lsquo;as it really is&rsquo;."]),
    ],
    terms=[
        ("Nanduttar&amacr;",
         "this poem's speaker, whose account juxtaposes ascetic "
         "observance with admitted vanity before her actual going "
         "forth."),
        ("vata",
         "vows or observances &mdash; the many undertaken in this "
         "poem's second verse, part of a religious life outside the "
         "Buddha's path."),
        ("vibh&#363;s&amacr;",
         "ornaments and adornment &mdash; named directly as what she "
         "loved, alongside baths and oil-massages, even during her "
         "ascetic period."),
        ("saddh&amacr;",
         "&ldquo;faith&rdquo; &mdash; named as the specific turning "
         "point that led to her actual going forth, distinct from her "
         "earlier vows."),
        ("yoga",
         "the &ldquo;yokes&rdquo; this poem's closing verse describes as "
         "entirely unyoked, alongside all wishes and aspirations cut "
         "off."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.5:1.1-1.4"),
        ("p", "&sect;2", "thig5.5:2.1-2.4"),
        ("p", "&sect;3", "thig5.5:3.1-3.4"),
        ("p", "&sect;4", "thig5.5:4.1-4.4"),
        ("p", "&sect;5", "thig5.5:5.1-5.4"),
    ],
    quiz=[
        {"q": "What does this poem's opening verse describe Nanduttarā worshiping?",
         "opts": [
             "No specific object of worship is described",
             "A local king",
             "The sacred flame, the moon, the sun, and the gods",
             "The Buddha himself"],
         "correct": 2,
         "expl": "Devotional practice outside the Buddha's path, described first."},
        {"q": "What ascetic practices does the second verse describe?",
         "opts": [
             "Many vows, half her head shaved, sleeping on the ground, no food at night",
             "Nothing ascetic is described",
             "Extensive travel abroad",
             "Formal study of scripture only"],
         "correct": 0,
         "expl": "A concrete list of austere observances."},
        {"q": "What does the third verse admit, immediately after describing this austerity?",
         "opts": [
             "That the austerity had already succeeded completely",
             "That she loved ornaments and decorations, and pandered to her body with baths and oil-massages",
             "That she abandoned all practice entirely",
             "Nothing further is admitted"],
         "correct": 1,
         "expl": "Unresolved vanity, admitted alongside the austerity just described."},
        {"q": "What does the poem name as the actual turning point toward change?",
         "opts": [
             "A vision in a dream",
             "Another vow undertaken",
             "A conversation with a king",
             "Gaining faith, and going forth to homelessness"],
         "correct": 3,
         "expl": "'Saddhā' — distinct from the vows and worship described before it."},
        {"q": "What does the poem say happened once she truly saw the body?",
         "opts": [
             "Desire for sensual pleasure is eradicated",
             "Nothing changed",
             "Her vanity increased",
             "She returned to her earlier practices"],
         "correct": 0,
         "expl": "Where austerity alone had not resolved her attachment, seeing the body did."},
        {"q": "What does 'vibhūsā' mean?",
         "opts": [
             "'Faith'",
             "Ornaments and adornment — loved even during her ascetic period",
             "'The sacred flame'",
             "A type of vow"],
         "correct": 1,
         "expl": "Named directly as what she still loved, alongside baths and oil-massages."},
        {"q": "How does this poem's structure differ from a simple story of steady progress?",
         "opts": [
             "It has no particular structure",
             "It juxtaposes an already-devout life with an admission of unresolved vanity",
             "It describes only steady, uninterrupted progress",
             "It contains no austerity or vanity at all"],
         "correct": 1,
         "expl": "Ritual observance and unresolved attachment sit side by side in her own account."},
        {"q": "What does the poem's closing verse say about 'yoga', the yokes?",
         "opts": [
             "That they remain, unresolved",
             "That the poem does not mention them",
             "That only human yokes are cut, not heavenly ones",
             "That she is entirely unyoked, all wishes and aspirations cut off"],
         "correct": 3,
         "expl": "A complete, unqualified claim, closing the poem."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The last poem",
             "The first poem",
             "The fifth poem, following Sundarīnandā",
             "It stands outside this book"],
         "correct": 2,
         "expl": "Following Thig 5.4, continuing the Book of the Fives."},
        {"q": "What does 'saddhā' mean?",
         "opts": [
             "'Faith' — named as the specific cause of her actual going forth",
             "'Ornaments'",
             "'A vow'",
             "'The moon'"],
         "correct": 0,
         "expl": "Distinct from the many vows and worship described earlier in the poem."},
    ],
    marginalia=[
        ("A religious life, before this path", [
            "flame, sun, and moon —",
            "worship outside the Buddha's teaching"
        ]),
        ("Vanity, admitted alongside austerity", [
            "ornaments and oil-massages,",
            "even during her vows"
        ]),
        ("Faith, named as the actual turn", [
            "not another vow,",
            "but saddhā itself"
        ]),
        ("Seeing, where austerity had not reached", [
            "the same body,",
            "resolved differently"
        ]),
    ],
    further=[
        '<a href="%s/thig5.5/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.4.html">Thig 5.4 &mdash; Sundar&imacr;nand&amacr;'
        "</a> &mdash; the poem immediately before this one.",
        '<a href="thig-5.6.html">Thig 5.6 &mdash; Mitt&amacr;k&amacr;&#7735;'
        "&imacr;</a> &mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.6 — Mittākāḷī
# --------------------------------------------------------------------------- #
page(
    5, 6, "Mitt&amacr;k&amacr;&#7735;&imacr;", "Mitt&amacr;k&amacr;&#7735;"
    "&imacr;",
    meta_title="Thig 5.6 — Mittākāḷī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Mittākāḷī's verses, a rare account of backsliding after "
        "ordination, resolved by watching the rise and fall of the "
        "aggregates. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 6 of 12",
    glance=[
        ("Setting", "A hut, where a moment of urgency strikes while "
                    "sitting"),
        ("Speaker", "The nun Mittākāḷī, recounting drift after her own "
                    "ordination, then a turning point"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "rare account of failure occurring after, not "
                       "before, going forth"),
    ],
    why=(
        "Most confessions of failure in this collection describe "
        "struggle before ordination. Mittākāḷī's account is different: "
        "she went forth &lsquo;in faith&rsquo;, then admits to years of "
        "&lsquo;jealous of possessions and honors&rsquo;, neglecting the "
        "very goal she had ordained for &mdash; until a moment of sudden "
        "urgency, sitting alone in her hut, turned her toward the "
        "practice she had been avoiding."),
    guide=[
        ("Drift after ordination, not before it", [
            "&lsquo;Having gone forth in faith... I wandered here and "
            "there, jealous of possessions and honors&rsquo; describes "
            "backsliding within monastic life itself &mdash; a distinct "
            "kind of failure from Vimalā's or Sīhā's struggles, which "
            "took place entirely before they ever went forth."]),
        ("A verdict spoken to herself, quoted directly", [
            "&lsquo;I'm walking the wrong path, under the sway of "
            "craving&rsquo; is presented as her own words to herself, "
            "quoted directly &mdash; an unusually candid piece of "
            "internal speech, naming her own drift without excuse."]),
        ("Mortality named as the spur to change", [
            "&lsquo;My life is short, trampled by old age and "
            "sickness... there is no time for me to be careless&rsquo; "
            "gives her urgency a specific cause: not a vision or a "
            "teacher's rebuke, but a plain recognition of how little "
            "time remains."]),
        ("A named method, not just a stated result", [
            "&lsquo;I examined in line with the truth the rise and fall "
            "of the aggregates&rsquo; names the specific practice that "
            "followed her urgency &mdash; a stated technique, not only a "
            "claim of liberation."]),
    ],
    terms=[
        ("Mitt&amacr;k&amacr;&#7735;&imacr;",
         "this poem's speaker, whose account of backsliding after "
         "ordination is unusual in this collection."),
        ("l&amacr;bhasakk&amacr;ra",
         "&ldquo;possessions and honors&rdquo; &mdash; what she admits "
         "to pursuing jealously, at the expense of &lsquo;the highest "
         "goal&rsquo;."),
        ("saṁvega",
         "the sense of urgency that struck her while sitting in her "
         "hut, explicitly named as her turning point."),
        ("khandh&amacr;na&#7749; udayabbaya",
         "&ldquo;the rise and fall of the aggregates&rdquo; &mdash; the "
         "specific practice she names as what she examined, leading to "
         "her liberation."),
        ("vimuttacitt&amacr;",
         "&ldquo;mind liberated&rdquo; &mdash; how this poem describes "
         "her at its close, having fulfilled the Buddha's "
         "instructions."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.6:1.1-1.4"),
        ("p", "&sect;2", "thig5.6:2.1-2.4"),
        ("p", "&sect;3", "thig5.6:3.1-3.4"),
        ("p", "&sect;4", "thig5.6:4.1-4.4"),
        ("p", "&sect;5", "thig5.6:5.1-5.4"),
    ],
    quiz=[
        {"q": "How did Mittākāḷī go forth, according to this poem's opening line?",
         "opts": [
             "Reluctantly, under pressure from her family",
             "In faith",
             "By accident",
             "The poem does not describe how she went forth"],
         "correct": 1,
         "expl": "'Having gone forth in faith from the lay life to homelessness.'"},
        {"q": "What does she admit to doing after ordination, rather than before it?",
         "opts": [
             "Nothing is admitted",
             "Excelling immediately at meditation",
             "Leaving the monastic order entirely",
             "Wandering about, jealous of possessions and honors"],
         "correct": 3,
         "expl": "A rare account of drift occurring within monastic life itself."},
        {"q": "What words does the poem quote her saying to herself, at her turning point?",
         "opts": [
             "'I'm walking the wrong path, under the sway of craving'",
             "No words are quoted",
             "A prayer to the gods",
             "A complaint about her surroundings"],
         "correct": 0,
         "expl": "An unusually candid piece of internal speech, quoted directly."},
        {"q": "What does the poem name as the specific cause of her urgency?",
         "opts": [
             "A dream",
             "A rebuke from another nun",
             "A plain recognition that her life is short, trampled by old age and sickness",
             "No cause is given"],
         "correct": 2,
         "expl": "Mortality itself, plainly stated, rather than a vision or external event."},
        {"q": "What specific practice does the poem name as what she examined?",
         "opts": [
             "The rise and fall of the aggregates",
             "The teachings of a specific text",
             "No specific practice is named",
             "The behavior of other nuns"],
         "correct": 0,
         "expl": "A stated technique, not only a claim of liberation."},
        {"q": "How does this poem's structure differ from Vimalā's or Sīhā's accounts?",
         "opts": [
             "It does not differ at all",
             "It describes only pre-ordination struggle, like the others",
             "It contains no struggle of any kind",
             "Its failure takes place after ordination, not before it"],
         "correct": 3,
         "expl": "A distinct kind of drift, occurring within monastic life itself."},
        {"q": "What does 'lābhasakkāra' mean?",
         "opts": [
             "'Possessions and honors' — what she admits to pursuing jealously",
             "'The rise and fall'",
             "'A sense of urgency'",
             "'Old age and sickness'"],
         "correct": 0,
         "expl": "Named directly as what she pursued at the expense of the highest goal."},
        {"q": "How does the poem describe her at its close?",
         "opts": [
             "Still uncertain",
             "Standing up with mind liberated, having fulfilled the Buddha's instructions",
             "Returning to lay life",
             "Continuing to pursue possessions and honors"],
         "correct": 1,
         "expl": "A direct statement of completed liberation."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The last poem",
             "The first poem",
             "The sixth poem, following Nanduttarā",
             "It stands outside this book"],
         "correct": 2,
         "expl": "Following Thig 5.5, continuing the Book of the Fives."},
        {"q": "What does 'saṁvega' name in this poem?",
         "opts": [
             "A type of ornament",
             "A place name",
             "'Possessions and honors'",
             "The sense of urgency that struck her while sitting in her hut"],
         "correct": 3,
         "expl": "Explicitly named as her turning point."},
    ],
    marginalia=[
        ("Drift, after ordination", [
            "not before it,",
            "unusual in this collection"
        ]),
        ("A verdict, spoken to herself", [
            "'the wrong path' —",
            "quoted directly"
        ]),
        ("Mortality, named as the spur", [
            "no time left",
            "for carelessness"
        ]),
        ("A method, named directly", [
            "the rise and fall",
            "of the aggregates"
        ]),
    ],
    further=[
        '<a href="%s/thig5.6/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.5.html">Thig 5.5 &mdash; Nanduttar&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-5.7.html">Thig 5.7 &mdash; Sakul&amacr;</a> &mdash; '
        "the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.7 — Sakulā
# --------------------------------------------------------------------------- #
page(
    5, 7, "Sakul&amacr;", "Sakul&amacr;",
    meta_title="Thig 5.7 — Sakulā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sakulā's verses, insight arriving before renunciation, and an "
        "explicit account of what leaving lay life actually cost her. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 7 of 12",
    glance=[
        ("Setting", "A lay household, where she first hears the "
                    "teaching, before any renunciation"),
        ("Speaker", "The nun Sakulā, narrating insight while still a "
                    "layperson, then her subsequent going forth"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; names "
                       "the specific cost of her renunciation without "
                       "euphemism"),
    ],
    why=(
        "This poem's sequence runs differently from most confessions in "
        "this collection: Sakulā sees &lsquo;the stainless Dhamma, "
        "extinguishment, the state that does not pass&rsquo; while still "
        "&lsquo;staying at home&rsquo;, before she ever renounces "
        "&mdash; and when she does, the poem names exactly what she left "
        "behind: a son, a daughter, riches, and grain, stated without "
        "softening."),
    guide=[
        ("Insight before renunciation, not after it", [
            "&lsquo;While staying at home I heard the teaching from a "
            "monk. I saw the stainless Dhamma&rsquo; places her first "
            "moment of clear seeing before she has renounced anything "
            "&mdash; a different sequence from poems where insight "
            "follows years of monastic struggle."]),
        ("A cost, itemized rather than implied", [
            "&lsquo;Leaving behind my son and my daughter, my riches and "
            "my grain&rsquo; states plainly, in a single line, exactly "
            "what her going forth required &mdash; children and property "
            "named together, without euphemism or omission."]),
        ("Named stages, each with its own attainment", [
            "The poem tracks her progress through named stages: as a "
            "&lsquo;trainee nun&rsquo; she develops &lsquo;the direct "
            "path&rsquo; and gives up greed and hate; only &lsquo;when "
            "fully ordained&rsquo; does she recollect her past lives and "
            "purify her clairvoyance &mdash; each attainment tied to a "
            "specific point in her formal progress."]),
        ("Conditions seen as 'other', closing the account", [
            "&lsquo;Conditions are born of causes, crumbling; having "
            "seen them as other&rsquo; closes the poem with a specific "
            "insight into causality and impermanence, immediately before "
            "she gives up all remaining defilements."]),
    ],
    terms=[
        ("Sakul&amacr;",
         "this poem's speaker, whose insight into the Dhamma arrives "
         "while she is still a layperson."),
        ("nibb&amacr;na&#7749; padamaccuta&#7749;",
         "&ldquo;extinguishment, the state that does not pass&rdquo; "
         "&mdash; what she says she saw even before renouncing anything."),
        ("sikkham&amacr;n&amacr;",
         "a &ldquo;trainee nun&rdquo; &mdash; the stage at which this "
         "poem says she developed the direct path and gave up greed and "
         "hate."),
        ("upasampad&amacr;",
         "full ordination &mdash; the later stage at which she "
         "recollected her past lives and purified her clairvoyance."),
        ("sa&#7749;kh&amacr;ra",
         "&ldquo;conditions&rdquo; &mdash; named in this poem's closing "
         "verse as born of causes and crumbling, seen as other than "
         "self."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.7:1.1-1.4"),
        ("p", "&sect;2", "thig5.7:2.1-2.4"),
        ("p", "&sect;3", "thig5.7:3.1-3.4"),
        ("p", "&sect;4", "thig5.7:4.1-4.4"),
        ("p", "&sect;5", "thig5.7:5.1-5.4"),
    ],
    quiz=[
        {"q": "When did Sakulā first see 'the stainless Dhamma', according to this poem?",
         "opts": [
             "While still staying at home, before renouncing anything",
             "Only after many years as a nun",
             "In a dream, after her ordination",
             "The poem does not say when"],
         "correct": 0,
         "expl": "Insight arrives before renunciation, an unusual sequence in this collection."},
        {"q": "What does the poem name as the specific cost of her going forth?",
         "opts": [
             "Nothing is named specifically",
             "Only her wealth, not her family",
             "Her son and daughter, her riches and grain",
             "Only a vague sense of loss"],
         "correct": 2,
         "expl": "Stated plainly, in a single line, without euphemism."},
        {"q": "What did she develop and give up as a 'trainee nun'?",
         "opts": [
             "Nothing is described at this stage",
             "Recollection of past lives only",
             "Full ordination itself",
             "The direct path, giving up greed and hate"],
         "correct": 3,
         "expl": "A specific attainment tied to her trainee stage, distinct from what follows full ordination."},
        {"q": "What happened when she was fully ordained?",
         "opts": [
             "She returned to lay life",
             "She recollected her past lives and purified her clairvoyance",
             "Nothing new is described",
             "She lost her earlier attainments"],
         "correct": 1,
         "expl": "A distinct attainment marked at this later, specific stage."},
        {"q": "What insight does the poem's closing verse describe?",
         "opts": [
             "That conditions are born of causes and crumbling, seen as other",
             "That nothing can ever be known",
             "A vision of her former family",
             "No insight is described"],
         "correct": 0,
         "expl": "A specific insight into causality and impermanence, closing the poem."},
        {"q": "What does 'sikkhamānā' mean?",
         "opts": [
             "'Extinguishment'",
             "A 'trainee nun' — the stage at which she developed the direct path",
             "'Riches and grain'",
             "A fully ordained nun"],
         "correct": 1,
         "expl": "Distinct from 'upasampadā', full ordination, named later in the poem."},
        {"q": "How does this poem's sequence differ from many other confessions in this collection?",
         "opts": [
             "It does not differ at all",
             "Insight is described only after many years of monastic struggle, as usual",
             "It describes no insight at all",
             "Her first insight comes before she has renounced anything"],
         "correct": 3,
         "expl": "A different order from poems where clarity follows prolonged monastic effort."},
        {"q": "What does 'nibbānaṁ padamaccutaṁ' mean?",
         "opts": [
             "'Riches and grain'",
             "'Extinguishment, the state that does not pass' — what she saw even before renouncing",
             "'A trainee nun'",
             "'The direct path'"],
         "correct": 1,
         "expl": "Her first, lay-life glimpse of the Dhamma, named directly."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The last poem",
             "The first poem",
             "The seventh poem, following Mittākāḷī",
             "It stands outside this book"],
         "correct": 2,
         "expl": "Following Thig 5.6, continuing the Book of the Fives."},
        {"q": "What does 'saṅkhāra' mean, as used in this poem's closing verse?",
         "opts": [
             "'Full ordination'",
             "'A monk's teaching'",
             "'Conditions' — named as born of causes and crumbling",
             "'A son and daughter'"],
         "correct": 2,
         "expl": "The specific object of insight closing the poem."},
    ],
    marginalia=[
        ("Insight, before renunciation", [
            "seen while still",
            "at home"
        ]),
        ("A cost, named exactly", [
            "son, daughter,",
            "riches, grain"
        ]),
        ("Stages, each with its own mark", [
            "trainee, then",
            "fully ordained"
        ]),
        ("Conditions, seen as other", [
            "born of causes,",
            "crumbling"
        ]),
    ],
    further=[
        '<a href="%s/thig5.7/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.6.html">Thig 5.6 &mdash; Mitt&amacr;k&amacr;'
        "&#7735;&imacr;</a> &mdash; the poem immediately before this one.",
        '<a href="thig-5.8.html">Thig 5.8 &mdash; So&ntilde;&amacr;</a> '
        "&mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.8 — Soṇā
# --------------------------------------------------------------------------- #
page(
    5, 8, "So&ntilde;&amacr;", "So&ntilde;&amacr;",
    meta_title="Thig 5.8 — Soṇā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Soṇā's verses, ten children raised before ordination, closing "
        "on one of this collection's most defiant single lines. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 8 of 12",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "The nun Soṇā, describing a full lay life raising "
                    "children before her ordination in old age"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "closes on one of this collection's most direct, "
                       "defiant single lines"),
    ],
    why=(
        "Soṇā's account opens with an entire lay lifetime already lived: "
        "&lsquo;I gave birth to ten sons... then, when feeble and old, I "
        "approached a nun&rsquo;. The teaching she receives repeats, for "
        "a third time in this collection, the exact phrase given to "
        "Uttamā in Thig 3.2 and the unnamed nun in Thig 5.1 &mdash; and "
        "the poem closes on a line unlike any other in the book: a "
        "direct curse against old age itself."),
    guide=[
        ("A full lay life, before any renunciation", [
            "&lsquo;I gave birth to ten sons in this form, this bag of "
            "bones&rsquo; opens with an entire worldly lifetime already "
            "complete &mdash; ordination arriving only &lsquo;when "
            "feeble and old&rsquo;, later in life than most accounts in "
            "this collection."]),
        ("A teaching phrase used for a third time", [
            "&lsquo;She taught me the Dhamma: the aggregates, sense "
            "fields, and elements&rsquo; repeats, word for word, the "
            "same compound term &mdash; &lsquo;khandhāyatanadhātuyo&rsquo; "
            "&mdash; already used for Uttamā's teacher in Thig 3.2 and "
            "the unnamed nun's teacher in Thig 5.1: a recurring, "
            "formulaic instruction given across three different women's "
            "accounts."]),
        ("A specific term for a swift attainment", [
            "&lsquo;I achieved the immediate liberation, quenched by not "
            "grasping&rsquo; uses a distinctive term, "
            "&lsquo;anantarāvimokkha&rsquo;, naming her release as "
            "immediate rather than gradual &mdash; a specific claim "
            "about the pace of her final breakthrough."]),
        ("A curse against old age, unlike anything else in this book", [
            "&lsquo;Curse you, wretched old age!&rsquo; is addressed "
            "directly to old age itself, immediately after she states "
            "that the five aggregates &lsquo;remain, but their root is "
            "cut&rsquo; &mdash; one of the most vivid, unguarded single "
            "lines anywhere in this collection."]),
    ],
    terms=[
        ("So&ntilde;&amacr;",
         "this poem's speaker, whose account of raising ten children "
         "precedes her ordination in old age."),
        ("khandh&amacr;yatanadh&amacr;tuyo",
         "&ldquo;the aggregates, sense fields, and elements&rdquo; "
         "&mdash; the same teaching phrase used in Thig 3.2 and Thig "
         "5.1, now given for a third time."),
        ("anantar&amacr;vimokkha",
         "&ldquo;immediate liberation&rdquo; &mdash; a distinctive term "
         "for her final breakthrough, naming its pace as immediate "
         "rather than gradual."),
        ("pa&ntilde;cakkhandh&amacr;",
         "the five aggregates, described in this poem's closing verse as "
         "remaining, but with their root cut."),
        ("jar&amacr;",
         "&ldquo;old age&rdquo; &mdash; addressed directly and cursed in "
         "this poem's most vivid line."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.8:1.1-1.4"),
        ("p", "&sect;2", "thig5.8:2.1-2.4"),
        ("p", "&sect;3", "thig5.8:3.1-3.4"),
        ("p", "&sect;4", "thig5.8:4.1-4.4"),
        ("p", "&sect;5", "thig5.8:5.1-5.4"),
    ],
    quiz=[
        {"q": "How does this poem's opening verse describe Soṇā's earlier life?",
         "opts": [
             "She gave birth to ten sons",
             "She was a wandering ascetic",
             "She was a queen",
             "No earlier life is described"],
         "correct": 0,
         "expl": "A full lay lifetime already lived, before any renunciation."},
        {"q": "When did Soṇā approach a nun and begin her monastic path?",
         "opts": [
             "In her youth",
             "Before she had any children",
             "When feeble and old",
             "The poem does not say"],
         "correct": 2,
         "expl": "Ordination arriving later in life than most accounts in this collection."},
        {"q": "What phrase does her teacher use, identical to Thig 3.2 and Thig 5.1?",
         "opts": [
             "'Twenty-five years'",
             "'The victor's instructions'",
             "No phrase is shared with those poems",
             "'The aggregates, sense fields, and elements'"],
         "correct": 3,
         "expl": "The same compound term, now given for a third time in this collection."},
        {"q": "What distinctive term does the poem use for her final breakthrough?",
         "opts": [
             "'Anantarāvimokkha' — 'immediate liberation'",
             "'Peace of heart'",
             "'The signless'",
             "No specific term is used"],
         "correct": 0,
         "expl": "Naming the pace of her release as immediate, not gradual."},
        {"q": "What does this poem's most vivid closing line address directly?",
         "opts": [
             "A specific nun by name",
             "Old age itself, cursed directly",
             "The Buddha",
             "Māra"],
         "correct": 1,
         "expl": "'Curse you, wretched old age!' — one of the most unguarded lines in this collection."},
        {"q": "What does the poem say about the five aggregates, just before this curse?",
         "opts": [
             "That they have vanished entirely",
             "That they remain, but their root is cut",
             "That they were never real",
             "Nothing is said about them"],
         "correct": 1,
         "expl": "A precise image: continued existence, without the root that once drove it."},
        {"q": "What does 'jarā' mean?",
         "opts": [
             "'Immediate liberation'",
             "'Ten sons'",
             "'A trainee nun'",
             "'Old age' — addressed and cursed directly in this poem's closing verse"],
         "correct": 3,
         "expl": "The direct object of this poem's most vivid line."},
        {"q": "How does this poem's opening compare to most other accounts in this collection?",
         "opts": [
             "It is identical to most other accounts",
             "It begins with an entire lay lifetime, including raising children, complete before ordination",
             "It describes a childhood in a monastery",
             "It contains no lay life at all"],
         "correct": 1,
         "expl": "A fuller worldly life lived first, than in most poems in this book."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The first poem",
             "The last poem",
             "It stands outside this book",
             "The eighth poem, following Sakulā"],
         "correct": 3,
         "expl": "Following Thig 5.7, continuing the Book of the Fives."},
        {"q": "How many times, counting this poem, has the phrase 'khandhāyatanadhātuyo' now appeared in this collection?",
         "opts": [
             "Once",
             "Twice",
             "Three times",
             "It has never appeared before"],
         "correct": 2,
         "expl": "Thig 3.2, Thig 5.1, and now this poem — a recurring, formulaic instruction."},
    ],
    marginalia=[
        ("A full life, lived first", [
            "ten sons,",
            "before ordination"
        ]),
        ("A teaching, given a third time", [
            "the same phrase",
            "as 3.2 and 5.1"
        ]),
        ("Immediate, not gradual", [
            "a distinctive term",
            "for the final release"
        ]),
        ("A curse, unguarded", [
            "'wretched old age' —",
            "addressed directly"
        ]),
    ],
    further=[
        '<a href="%s/thig5.8/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.7.html">Thig 5.7 &mdash; Sakul&amacr;</a> &mdash; '
        "the poem immediately before this one.",
        '<a href="thig-5.9.html">Thig 5.9 &mdash; Bhadd&amacr; of the Curly '
        "Hair</a> &mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.9 — Bhaddā of the Curly Hair
# --------------------------------------------------------------------------- #
page(
    5, 9, "Bhadd&amacr; Ku&#7751;&#7693;alakes&amacr;", "Bhadd&amacr; of "
    "the Curly Hair",
    meta_title="Thig 5.9 — Bhaddā of the Curly Hair | Ru-Yi Meditation "
                "Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Bhaddā Kuṇḍalakesā's verses, a former ascetic's harsh "
        "self-judgment, an on-the-spot ordination, and a stranger's "
        "closing praise. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 9 of 12",
    glance=[
        ("Setting", "Vulture's Peak Mountain, then decades of wandering "
                    "across several kingdoms"),
        ("Speaker", "Three voices: Bhaddā's own retrospective account, "
                    "her account of ordination and travels, then an "
                    "outside voice praising a donor"),
        ("Form", "Five four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "shifts voice twice, closing on a stranger's "
                       "praise for someone other than the speaker"),
    ],
    why=(
        "This poem opens with unusually harsh self-judgment about a "
        "life before the Buddha's path &mdash; &lsquo;I saw fault where "
        "there was none, and was blind to the actual fault&rsquo; "
        "&mdash; then narrates an on-the-spot ordination echoing the "
        "earliest days of the monastic order, decades of extensive "
        "wandering, and closes with a voice that is not Bhaddā's own, "
        "praising a stranger's generosity toward her."),
    guide=[
        ("A former ascetic's harsh verdict on herself", [
            "&lsquo;My hair mown off, covered in mud, I used to wander "
            "wearing just one robe&rsquo; describes a life of austere "
            "practice outside the Buddha's path, judged afterward "
            "without sympathy: &lsquo;I saw fault where there was none, "
            "and was blind to the actual fault&rsquo;."]),
        ("An ordination echoing the earliest days of the order", [
            "&lsquo;&ldquo;Come Bhaddā,&rdquo; he said; that was my "
            "ordination&rsquo; uses the same simple formula as the "
            "Buddha's very first ordinations, &lsquo;come, monk&rsquo; "
            "&mdash; Bhikkhu Sujato's own note on this line observes that "
            "&lsquo;ehi&rsquo;, &lsquo;come&rsquo;, was itself a "
            "recognized sign of respect."]),
        ("Fifty years, named across five regions", [
            "&lsquo;I've wandered among the Aṅgans and Magadhans, the "
            "Vajjis, Kāsis, and Kosalans... free of debt for fifty "
            "years&rsquo; gives her subsequent life a scale and "
            "geographic specificity unusual in this collection, five "
            "named regions across five decades."]),
        ("A stranger's voice, closing the poem", [
            "The final verse shifts away from Bhaddā's own voice "
            "entirely: &lsquo;that lay follower is so very wise... he "
            "gave a robe to Bhaddā, who is released from all "
            "ties&rsquo; &mdash; an outside voice, like Thig 3.6's "
            "praise of Sukkā, but here praising not the nun herself, "
            "only the donor who supported her."]),
    ],
    terms=[
        ("Bhadd&amacr; Ku&#7751;&#7693;alakes&amacr;",
         "&ldquo;Bhaddā of the Curly Hair&rdquo; &mdash; this poem's "
         "speaker for most of its verses, formerly a wandering ascetic "
         "outside the Buddha's path."),
        ("vajje c&amacr;vajjadassin&imacr;",
         "&ldquo;blind to the actual fault&rdquo; &mdash; her own harsh "
         "verdict on her former practice, paired with seeing "
         "&lsquo;fault where there was none&rsquo;."),
        ("ehi bhadde",
         "&ldquo;Come, Bhaddā&rdquo; &mdash; the Buddha's ordination "
         "formula for her, echoing the earliest ordinations in the "
         "monastic order."),
        ("ra&#7789;&#7789;hapi&#7751;&#7693;a",
         "&ldquo;the almsfood of the nations&rdquo; &mdash; describing "
         "her decades of wandering across several named kingdoms, free "
         "of debt."),
        ("gantha",
         "&ldquo;ties&rdquo; or bonds &mdash; named in this poem's "
         "closing verse as what Bhaddā is entirely released from, "
         "spoken by a voice other than her own."),
    ],
    text_intro=(
        "The text in full: five verses, shifting voice twice. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.9:1.1-1.4"),
        ("p", "&sect;2", "thig5.9:2.1-2.4"),
        ("p", "&sect;3", "thig5.9:3.1-3.4"),
        ("p", "&sect;4", "thig5.9:4.1-4.4"),
        ("p", "&sect;5", "thig5.9:5.1-5.4"),
    ],
    quiz=[
        {"q": "How does the poem describe Bhaddā's appearance during her earlier ascetic life?",
         "opts": [
             "Hair mown off, covered in mud, wearing just one robe",
             "Richly dressed and adorned",
             "No physical description is given",
             "Wearing a crown"],
         "correct": 0,
         "expl": "A specific, austere image of her former practice."},
        {"q": "How does the poem judge that earlier life?",
         "opts": [
             "As entirely admirable",
             "As already fully successful",
             "As harmless but pointless",
             "'I saw fault where there was none, and was blind to the actual fault'"],
         "correct": 3,
         "expl": "An unusually harsh self-verdict on her prior practice."},
        {"q": "What words does the Buddha use to ordain her, on the spot?",
         "opts": [
             "A lengthy formal ceremony is described in full",
             "'Come, Bhaddā' — a simple, direct formula",
             "No ordination is described",
             "She ordains herself, without the Buddha's involvement"],
         "correct": 1,
         "expl": "Echoing the same simple formula used in the Buddha's very first ordinations."},
        {"q": "According to Sujato's own note, what did the word 'ehi', 'come', signify in this context?",
         "opts": [
             "A recognized sign of respect",
             "A command with no particular significance",
             "An insult",
             "A formal legal term"],
         "correct": 0,
         "expl": "Cited from a Vedic-era source in the guide's discussion of this line."},
        {"q": "Across how many named regions does the poem say she wandered over fifty years?",
         "opts": [
             "Just one",
             "Five: the Aṅgans, Magadhans, Vajjis, Kāsis, and Kosalans",
             "None are named",
             "Ten"],
         "correct": 1,
         "expl": "A scale and geographic specificity unusual in this collection."},
        {"q": "Whose voice speaks in this poem's final verse?",
         "opts": [
             "Bhaddā's own voice, unchanged",
             "The Buddha's voice",
             "Māra's voice",
             "An outside voice, praising a lay donor who is not Bhaddā herself"],
         "correct": 3,
         "expl": "A shift away from Bhaddā's own first-person account entirely."},
        {"q": "What does the poem's final verse actually praise?",
         "opts": [
             "Bhaddā's own attainment directly",
             "A lay follower's wisdom, for having given Bhaddā a robe",
             "Nothing in particular",
             "The Buddha's teaching in general"],
         "correct": 1,
         "expl": "Praise directed at the donor, not at Bhaddā's own realization."},
        {"q": "How does this poem's closing voice-shift compare to Thig 3.6's Sukkā?",
         "opts": [
             "The two poems are identical in every way",
             "Neither poem contains any outside voice",
             "It is a similar device, but here praising a supporter rather than the practitioner herself",
             "Thig 3.6 also praises a donor, not Sukkā"],
         "correct": 2,
         "expl": "A related but distinct use of an outside, praising voice."},
        {"q": "What does 'gantha' mean, as used in this poem's closing verse?",
         "opts": [
             "'Ties' or bonds — named as what Bhaddā is entirely released from",
             "'Curly hair'",
             "'An ordination formula'",
             "'Fifty years'"],
         "correct": 0,
         "expl": "Named by the outside voice that closes the poem."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The last poem",
             "The first poem",
             "The ninth poem, following Soṇā",
             "It stands outside this book"],
         "correct": 2,
         "expl": "Following Thig 5.8, continuing the Book of the Fives."},
    ],
    marginalia=[
        ("A harsh verdict on herself", [
            "fault where there was none,",
            "blind to the real fault"
        ]),
        ("'Come, Bhaddā' — the earliest formula", [
            "echoing the Buddha's",
            "very first ordinations"
        ]),
        ("Fifty years, five regions", [
            "a scale unusual",
            "in this collection"
        ]),
        ("A stranger's voice, closing", [
            "praising the donor,",
            "not Bhaddā herself"
        ]),
    ],
    further=[
        '<a href="%s/thig5.9/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli alongside, "
        "segment by segment." % SC,
        '<a href="thig-5.8.html">Thig 5.8 &mdash; So&ntilde;&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-3.6.html">Thig 3.6 &mdash; Sukk&amacr;</a> &mdash; '
        "an earlier poem whose closing outside voice this one's own "
        "closing verse resembles.",
        '<a href="thig-5.10.html">Thig 5.10 &mdash; Pa&#7789;&amacr;c&amacr;'
        "r&amacr;</a> &mdash; the next poem in the Book of the Fives.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.10 — Paṭācārā
# --------------------------------------------------------------------------- #
page(
    5, 10, "Pa&#7789;&amacr;c&amacr;r&amacr;", "Pa&#7789;&amacr;c&amacr;"
    "r&amacr;",
    meta_title="Thig 5.10 — Paṭācārā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Paṭācārā's own verses, insight arriving from watching water "
        "flow downhill and a lamp go out, not from the story later "
        "tradition remembers her for. From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 10 of 12",
    glance=[
        ("Setting", "A dwelling, at evening, washing feet and preparing "
                    "to sleep"),
        ("Speaker", "The nun Paṭācārā, questioning her own lack of "
                    "progress, then narrating two ordinary observations"),
        ("Form", "Five verses, mostly four lines, the fourth extending "
                 "to six"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; ends "
                       "on one of this collection's most quoted single "
                       "images"),
    ],
    why=(
        "Paṭācārā is remembered by later tradition for an elaborate and "
        "tragic story; this poem itself tells none of it. Instead, her "
        "own verses describe a precise puzzle &mdash; ethical, obedient, "
        "&lsquo;neither lazy nor restless&rsquo;, yet still short of "
        "quenching &mdash; resolved not by further striving but by "
        "watching water flow downhill while washing her feet, and then "
        "a lamp go out."),
    guide=[
        ("A famous name, and a spare verse that tells none of the story", [
            "Later Buddhist tradition remembers Paṭācārā for an "
            "elaborate account of personal loss; this poem's own verses "
            "state none of that narrative, only the puzzle of her "
            "practice and the two observations that resolved it."]),
        ("A precise self-diagnosis, ruling out the usual explanations", [
            "&lsquo;I am accomplished in ethics, and I do the Teacher's "
            "bidding... being neither lazy nor restless &mdash; why then "
            "do I not achieve quenching?&rsquo; rules out the obvious "
            "causes before the poem answers its own question."]),
        ("Water, flowing from high ground to low", [
            "Washing her feet, she &lsquo;took note of the water... "
            "flowing from high ground to low&rsquo; &mdash; an entirely "
            "ordinary, domestic action, not a teaching or a vision, "
            "becomes the first observation that settles her mind."]),
        ("A lamp extinguished, and the poem's most quoted image", [
            "&lsquo;The liberation of my heart was like the quenching of "
            "the lamp&rsquo; closes the poem on a simile that has "
            "become one of the most recognized single images in the "
            "entire Therigatha &mdash; drawn not from doctrine recited, "
            "but from putting out a light before sleep."]),
    ],
    terms=[
        ("Pa&#7789;&amacr;c&amacr;r&amacr;",
         "this poem's speaker, remembered by later tradition for an "
         "elaborate story this verse itself does not narrate."),
        ("aku&#7779;it&amacr; anuddhat&amacr;",
         "&ldquo;neither lazy nor restless&rdquo; &mdash; her own "
         "precise ruling-out of the usual explanations for slow "
         "progress."),
        ("thalato ninna&#7749;",
         "&ldquo;from high ground to low&rdquo; &mdash; the direction of "
         "the water she watches while washing her feet."),
        ("sam&amacr;dhi",
         "the settled, serene mind state named directly after this "
         "first observation, compared to &lsquo;a fine thoroughbred "
         "steed&rsquo;."),
        ("vimokkha",
         "&ldquo;liberation&rdquo; &mdash; the word at the center of "
         "this poem's closing simile, compared to a lamp's quenching."),
    ],
    text_intro=(
        "The text in full: five verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.10:1.1-1.4"),
        ("p", "&sect;2", "thig5.10:2.1-2.4"),
        ("p", "&sect;3", "thig5.10:3.1-3.4"),
        ("p", "&sect;4", "thig5.10:4.1-4.6"),
        ("p", "&sect;5", "thig5.10:5.1-5.4"),
    ],
    quiz=[
        {"q": "Does this poem itself narrate the tragic story later tradition remembers Paṭācārā for?",
         "opts": [
             "Yes, in full detail",
             "No — this verse states none of that narrative",
             "Only the ending is described",
             "The poem is entirely about that story"],
         "correct": 1,
         "expl": "This guide keeps the well-known later tradition distinct from what the verse itself states."},
        {"q": "What does Paṭācārā rule out as the cause of her lack of progress?",
         "opts": [
             "Nothing is ruled out",
             "Laziness and restlessness — she names herself as neither",
             "A lack of ethical conduct only",
             "Her teacher's instruction"],
         "correct": 1,
         "expl": "A precise self-diagnosis, sharpening the puzzle before it is resolved."},
        {"q": "What is Paṭācārā doing when she first observes the water?",
         "opts": [
             "Bathing in a river",
             "Cooking a meal",
             "Washing her feet",
             "Traveling to a distant city"],
         "correct": 2,
         "expl": "An entirely ordinary, domestic action."},
        {"q": "What direction does she observe the water flowing?",
         "opts": [
             "In a perfect circle",
             "Upward, against gravity",
             "The direction is not specified",
             "From high ground to low"],
         "correct": 3,
         "expl": "'Thalato ninnam āgataṁ' — the specific observation named in the text."},
        {"q": "What does the poem compare her settled mind to, after this observation?",
         "opts": [
             "A fine thoroughbred steed",
             "A still pond",
             "Nothing is compared",
             "A flying bird"],
         "correct": 0,
         "expl": "A specific simile for her mind's new serenity."},
        {"q": "What second action leads to this poem's closing image?",
         "opts": [
             "Reading a text",
             "Extinguishing a lamp before sleep",
             "A conversation with another nun",
             "No second action occurs"],
         "correct": 1,
         "expl": "The domestic act that produces the poem's most famous simile."},
        {"q": "What is this poem's closing simile?",
         "opts": [
             "The liberation of her heart was like the quenching of the lamp",
             "Her mind was like a raging fire",
             "No simile closes the poem",
             "Her heart was like an unlit lamp, still dark"],
         "correct": 0,
         "expl": "One of the most recognized single images in the entire Therigatha."},
        {"q": "What does 'akusītā anuddhatā' mean?",
         "opts": [
             "'A fine thoroughbred steed'",
             "'From high ground to low'",
             "'Neither lazy nor restless' — her own ruling-out of usual explanations",
             "'The quenching of the lamp'"],
         "correct": 2,
         "expl": "Named directly in her own opening question to herself."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The tenth poem, following Bhaddā of the Curly Hair",
             "The first poem",
             "The last poem",
             "It stands outside this book"],
         "correct": 0,
         "expl": "Following Thig 5.9, continuing the Book of the Fives."},
        {"q": "Where does this poem's insight come from, according to its own account?",
         "opts": [
             "A vision of the Buddha",
             "A formal doctrinal recitation",
             "A conversation with Māra",
             "Two ordinary, domestic observations: flowing water and an extinguished lamp"],
         "correct": 3,
         "expl": "Not doctrine recited, but everyday actions observed closely."},
    ],
    marginalia=[
        ("A famous name, a spare verse", [
            "the tragic story",
            "told elsewhere, not here"
        ]),
        ("A puzzle, precisely stated", [
            "neither lazy",
            "nor restless"
        ]),
        ("Water, flowing downhill", [
            "an ordinary act,",
            "watched closely"
        ]),
        ("A lamp, and the collection's most quoted image", [
            "liberation, like",
            "a light put out"
        ]),
    ],
    further=[
        '<a href="%s/thig5.10/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-5.9.html">Thig 5.9 &mdash; Bhadd&amacr; of the '
        "Curly Hair</a> &mdash; the poem immediately before this one.",
        '<a href="thig-5.11.html">Thig 5.11 &mdash; Thirty Nuns</a> '
        "&mdash; the next poem, the fruit of Paṭācārā's subsequent "
        "teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.11 — Thirty Nuns
# --------------------------------------------------------------------------- #
page(
    5, 11, "Ti&#7749;samatt&amacr;", "Thirty Nuns",
    meta_title="Thig 5.11 — Thirty Nuns | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Therigatha's only poem of collective realization: thirty nuns' "
        "awakening across a single night, under Paṭācārā's guidance. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Fives &middot; Poem 11 of 12",
    glance=[
        ("Setting", "A single night, tracked across its three watches"),
        ("Speaker", "Paṭācārā's instruction, then a third-person account "
                    "of thirty nuns' shared realization"),
        ("Form", "Five verses, mostly six lines, closing on a prose "
                 "colophon"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the "
                       "collection's only account of a shared, "
                       "collective realization"),
    ],
    why=(
        "Every other poem in this collection narrates one woman's own "
        "path. This one is different: after Paṭācārā instructs a group "
        "of listeners directly, the poem shifts to the third person "
        "plural and tracks thirty nuns' realization across a single "
        "night's three watches, closing with a prose line confirming "
        "the event plainly: &lsquo;that is how thirty senior nuns "
        "declared their enlightenment in the presence of "
        "Paṭācārā&rsquo;."),
    guide=[
        ("An instruction, addressed to a group", [
            "Paṭācārā's own words open the poem, contrasting young men "
            "who labor for worldly wealth with a direct call: &lsquo;do "
            "the Buddha's bidding, you won't regret it... devoted to "
            "serenity of heart, do the Buddha's bidding&rsquo;."]),
        ("Three watches, three attainments, shared by all", [
            "The poem tracks the night precisely: past lives recollected "
            "in the first watch, clairvoyance purified in the second, "
            "and in the third, &lsquo;they shattered the mass of "
            "darkness&rsquo; &mdash; the same phrase closing Thig 3.2, "
            "3.7, and 3.8, now marking a shared realization rather than "
            "one woman's alone."]),
        ("A comparison to the gods honoring Indra", [
            "&lsquo;We shall abide honoring you, as the Thirty gods "
            "honor Indra, undefeated in battle&rsquo; is an unusually "
            "elevated, mythological image for a teacher-student bond, "
            "closing the nuns' own declaration of mastery."]),
        ("A prose line, confirming the event plainly", [
            "The poem's final line drops verse entirely: &lsquo;that is "
            "how thirty senior nuns declared their enlightenment in the "
            "presence of Paṭācārā&rsquo; &mdash; a simple, direct "
            "colophon, unlike anything closing another poem in this "
            "collection so far."]),
    ],
    terms=[
        ("Pa&#7789;&amacr;c&amacr;r&amacr;",
         "the teacher whose instruction, given directly in this poem's "
         "opening verses, leads to the collective realization that "
         "follows."),
        ("cetosamatha",
         "&ldquo;serenity of heart&rdquo; &mdash; what Paṭācārā's "
         "listeners are instructed to devote themselves to."),
        ("tamokkhandha",
         "&ldquo;the mass of darkness&rdquo; &mdash; shattered here for "
         "a fourth time in this collection, echoing Thig 3.2, 3.7, and "
         "3.8."),
        ("tevijj&amacr;",
         "&ldquo;masters of the three knowledges&rdquo; &mdash; how the "
         "thirty nuns describe themselves in their own closing "
         "declaration."),
        ("a&ntilde;&ntilde;a&#7749; by&amacr;kari&#7749;s&#363;",
         "&ldquo;declared their enlightenment&rdquo; &mdash; the phrase "
         "in this poem's closing prose colophon, confirming the event "
         "plainly."),
    ],
    text_intro=(
        "The text in full: Paṭācārā's instruction, the nuns' shared "
        "realization, and a closing prose colophon. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.11:1.1-1.4"),
        ("p", "&sect;2", "thig5.11:2.1-2.6"),
        ("p", "&sect;3", "thig5.11:3.1-3.6"),
        ("p", "&sect;4", "thig5.11:4.1-4.6"),
        ("p", "&sect;5", "thig5.11:5.1-5.6"),
        ("p", "&sect;6", ["thig5.11:6.1"]),
    ],
    quiz=[
        {"q": "How does this poem differ structurally from every other poem in this collection so far?",
         "opts": [
             "It narrates a collective realization shared by thirty nuns, not one woman's own path",
             "It contains no instruction of any kind",
             "It is identical in structure to Thig 5.10",
             "It has no closing content of any kind"],
         "correct": 0,
         "expl": "The collection's only account of a shared, group realization."},
        {"q": "What does Paṭācārā's opening instruction contrast worldly labor with?",
         "opts": [
             "Nothing is contrasted",
             "A call to accumulate greater wealth",
             "A direct call to do the Buddha's bidding, devoted to serenity of heart",
             "A warning about specific dangers"],
         "correct": 2,
         "expl": "Ordinary labor for wealth, set against her direct instruction."},
        {"q": "What happens in the first watch of the night, according to this poem?",
         "opts": [
             "Nothing is described",
             "They recollect their past lives",
             "They purify their clairvoyance",
             "They shatter the mass of darkness"],
         "correct": 1,
         "expl": "The first of three watches, each marked by a specific attainment."},
        {"q": "What happens in the third and final watch?",
         "opts": [
             "They purify their clairvoyance",
             "Nothing further happens",
             "They shatter the mass of darkness",
             "They recollect their past lives"],
         "correct": 2,
         "expl": "The same phrase closing Thig 3.2, 3.7, and 3.8, now marking a shared realization."},
        {"q": "What comparison do the nuns use to describe their devotion to Paṭācārā?",
         "opts": [
             "Like the Thirty gods honoring Indra, undefeated in battle",
             "No comparison is used",
             "Like students honoring an ordinary teacher",
             "Like soldiers honoring a general"],
         "correct": 0,
         "expl": "An unusually elevated, mythological image for a teacher-student bond."},
        {"q": "How does this poem close?",
         "opts": [
             "With a question left unanswered",
             "Mid-verse, with no resolution",
             "With a prose colophon confirming that thirty senior nuns declared their enlightenment in Paṭācārā's presence",
             "With a dialogue with Māra"],
         "correct": 2,
         "expl": "A simple, direct closing line unlike any other poem's ending so far in this collection."},
        {"q": "What does 'tevijjā' mean, as the nuns use it of themselves?",
         "opts": [
             "'Serenity of heart'",
             "'Undefeated in battle'",
             "'The mass of darkness'",
             "'Masters of the three knowledges'"],
         "correct": 3,
         "expl": "Their own declared title, closing their account."},
        {"q": "How many times, counting this poem, has 'the mass of darkness' now been shattered in this collection?",
         "opts": [
             "Once",
             "Twice",
             "Three times",
             "A fourth time, after Thig 3.2, 3.7, and 3.8"],
         "correct": 3,
         "expl": "A recurring image for decisive breakthrough, now marking a group's shared attainment."},
        {"q": "How does this poem relate to Thig 5.10, the poem immediately before it?",
         "opts": [
             "It has no relationship to Thig 5.10",
             "It shows the fruit of Paṭācārā's own teaching, following her own realization in the previous poem",
             "It contradicts everything stated in Thig 5.10",
             "It is spoken by an entirely different, unrelated teacher"],
         "correct": 1,
         "expl": "Paṭācārā's own path in 5.10 leads directly into the mass realization she inspires here."},
        {"q": "What does 'cetosamatha' mean?",
         "opts": [
             "'A prose colophon'",
             "'Serenity of heart' — what Paṭācārā's listeners are told to devote themselves to",
             "'Thirty nuns'",
             "'The three watches of the night'"],
         "correct": 1,
         "expl": "Named directly in her opening instruction."},
    ],
    marginalia=[
        ("A collective realization, unique here", [
            "not one woman's path,",
            "but thirty together"
        ]),
        ("Three watches, three attainments", [
            "shared by all,",
            "in a single night"
        ]),
        ("Devotion, compared to the gods", [
            "as the Thirty",
            "honor Indra"
        ]),
        ("A colophon, confirming plainly", [
            "'that is how',",
            "stated directly"
        ]),
    ],
    further=[
        '<a href="%s/thig5.11/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-5.10.html">Thig 5.10 &mdash; Pa&#7789;&amacr;c'
        "&amacr;r&amacr;</a> &mdash; the poem immediately before this "
        "one, Paṭācārā's own realization.",
        '<a href="thig-5.12.html">Thig 5.12 &mdash; Cand&amacr;</a> '
        "&mdash; the next poem, another nun Paṭācārā personally guided.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 5.12 — Candā
# --------------------------------------------------------------------------- #
page(
    5, 12, "Cand&amacr;", "Cand&amacr;",
    meta_title="Thig 5.12 — Candā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Candā's verses, a destitute widow personally ordained by "
        "Paṭācārā, closing the Book of the Fives. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Fives &middot; Poem 12 of 12",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "The nun Candā, recounting destitution, then "
                    "ordination under Paṭācārā's personal guidance"),
        ("Form", "Five four-line verses, closing the Book of the Fives"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; one "
                       "of this collection's bleakest opening states, "
                       "before its resolution"),
    ],
    why=(
        "This poem closes the Book of the Fives with one of its bleakest "
        "openings: a childless widow, without friends or family, unable "
        "to secure &lsquo;food or clothes&rsquo;, begging from door to "
        "door for seven years, burned by heat and cold. It is Paṭācārā "
        "&mdash; named directly for a third consecutive poem in this "
        "book &mdash; who ordains her out of sympathy, and Candā's own "
        "closing declaration echoes, almost word for word, the thirty "
        "nuns' declaration in the poem just before it."),
    guide=[
        ("Destitution, stated without softening", [
            "&lsquo;A childless widow, bereft of friends or relatives, I "
            "got neither food nor clothes&rsquo; opens the poem in a "
            "state as bleak as any in this collection &mdash; seven "
            "years spent begging from family to family, &lsquo;burned "
            "by heat and cold&rsquo;."]),
        ("Paṭācārā, named for a third poem running", [
            "&lsquo;Out of sympathy for me, Paṭācārā gave me the going "
            "forth&rsquo; makes this the third consecutive poem in the "
            "Book of the Fives to name her directly &mdash; her own "
            "realization in Thig 5.10, the thirty nuns she taught in "
            "Thig 5.11, and now a single destitute widow she personally "
            "ordains."]),
        ("A specific request, quoted directly", [
            "&lsquo;Approaching her, I said: &ldquo;send me forth to "
            "homelessness&rdquo;&rsquo; preserves Candā's own words at "
            "the moment of asking &mdash; a specific, quoted request, "
            "not only a general account of seeking ordination."]),
        ("A declaration echoing the poem just before it", [
            "&lsquo;Master of the three knowledges, I am free of "
            "defilements&rsquo; closes this poem almost word for word "
            "as the thirty nuns closed Thig 5.11 &mdash; one woman's "
            "declaration now matching the group's, closing the entire "
            "book on the same formula."]),
    ],
    terms=[
        ("Cand&amacr;",
         "this poem's speaker, whose destitution before ordination is "
         "described in stark, unsoftened terms."),
        ("vidhav&amacr; aputtik&amacr;",
         "&ldquo;a childless widow&rdquo; &mdash; her own description of "
         "her situation before Paṭācārā's ordination."),
        ("anukamp&amacr;",
         "&ldquo;sympathy&rdquo; or compassion &mdash; named directly as "
         "Paṭācārā's motive for ordaining her."),
        ("paramattha",
         "&ldquo;the ultimate goal&rdquo; &mdash; what Paṭācārā, having "
         "ordained her, then urged her on toward."),
        ("tevijj&amacr; an&amacr;sav&amacr;",
         "&ldquo;master of the three knowledges, free of "
         "defilements&rdquo; &mdash; the same declaration, almost word "
         "for word, that closed the thirty nuns' account in Thig 5.11."),
    ],
    text_intro=(
        "The text in full: five verses, closing the Book of the Fives. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig5.12:1.1-1.4"),
        ("p", "&sect;2", "thig5.12:2.1-2.4"),
        ("p", "&sect;3", "thig5.12:3.1-3.4"),
        ("p", "&sect;4", "thig5.12:4.1-4.4"),
        ("p", "&sect;5", "thig5.12:5.1-5.4"),
    ],
    quiz=[
        {"q": "How does this poem describe Candā's situation before ordination?",
         "opts": [
             "A wealthy widow with many relatives",
             "A childless widow, bereft of friends or relatives, without food or clothes",
             "A queen who renounced her throne",
             "No earlier situation is described"],
         "correct": 1,
         "expl": "One of this collection's bleakest opening states."},
        {"q": "How long does the poem say Candā wandered begging, burned by heat and cold?",
         "opts": [
             "One year",
             "A single winter",
             "Seven years",
             "The duration is not given"],
         "correct": 2,
         "expl": "A specific span, echoing Thig 5.3's Sīhā's own seven years of suffering."},
        {"q": "Who ordains Candā, and why, according to this poem?",
         "opts": [
             "The Buddha himself, for no stated reason",
             "Paṭācārā, out of sympathy for her",
             "A relative, out of family obligation",
             "No one ordains her"],
         "correct": 1,
         "expl": "The third consecutive poem in this book to name Paṭācārā directly."},
        {"q": "What words does the poem quote Candā saying to Paṭācārā directly?",
         "opts": [
             "No words are quoted",
             "A complaint about her situation",
             "'Send me forth to homelessness'",
             "A question about the Dhamma"],
         "correct": 2,
         "expl": "A specific, quoted request at the moment of asking."},
        {"q": "How does this poem's closing declaration compare to Thig 5.11's?",
         "opts": [
             "It closes on an entirely different formula",
             "It is almost word for word the same: 'master of the three knowledges, free of defilements'",
             "This poem has no closing declaration",
             "It directly contradicts Thig 5.11's declaration"],
         "correct": 1,
         "expl": "One woman's declaration now matching the group's, closing the entire book on the same formula."},
        {"q": "What does 'anukampā' mean?",
         "opts": [
             "'A childless widow'",
             "'Send me forth'",
             "'Sympathy' or compassion — Paṭācārā's named motive for ordaining her",
             "'The ultimate goal'"],
         "correct": 2,
         "expl": "Named directly as the reason for Paṭācārā's action."},
        {"q": "What structural marker does bilara-data's underlying source place immediately after this poem?",
         "opts": [
             "'Pañcakanipāto niṭṭhito' — 'the Book of the Fives is finished'",
             "No marker at all",
             "A note naming the next book's first poem",
             "A repeat of the poem's own text"],
         "correct": 0,
         "expl": "The same kind of bibliographic close seen at the end of the Books of the Threes and Fours."},
        {"q": "What does 'paramattha' mean?",
         "opts": [
             "'The ultimate goal' — what Paṭācārā urged Candā toward, once ordained",
             "'Seven years'",
             "'A childless widow'",
             "'Heat and cold'"],
         "correct": 0,
         "expl": "Named directly in the verse describing Paṭācārā's guidance."},
        {"q": "What position does this poem hold in the Book of the Fives?",
         "opts": [
             "The first poem",
             "The eleventh poem",
             "It stands outside this book",
             "The twelfth and last poem, closing the book"],
         "correct": 3,
         "expl": "The final poem of twelve in the Book of the Fives."},
        {"q": "How many poems in a row, counting this one, name Paṭācārā directly?",
         "opts": [
             "Just this one",
             "Two",
             "None name her directly",
             "Three: Thig 5.10, 5.11, and this poem"],
         "correct": 3,
         "expl": "Her own realization, then the thirty nuns she taught, then this individually ordained widow."},
    ],
    marginalia=[
        ("Destitution, unsoftened", [
            "childless, friendless,",
            "without food or clothes"
        ]),
        ("Paṭācārā, a third time running", [
            "her own poem, the thirty,",
            "now this one widow"
        ]),
        ("A request, quoted directly", [
            "'send me forth' —",
            "her own words"
        ]),
        ("A declaration, matched to the group's", [
            "the same formula",
            "closing the whole book"
        ]),
    ],
    further=[
        '<a href="%s/thig5.12/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-5.11.html">Thig 5.11 &mdash; Thirty Nuns</a> '
        "&mdash; the poem immediately before this one, sharing this "
        "poem's exact closing declaration.",
        '<a href="./">Therigatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.1 — Paṭācārā, Who Had a Following of Five Hundred
# --------------------------------------------------------------------------- #
page(
    6, 1, "Pa&ntilde;casatamatt&amacr;", "Pa&#7789;&amacr;c&amacr;r&amacr;"
    ", Who Had a Following of Five Hundred",
    meta_title="Thig 6.1 — Paṭācārā, Who Had a Following of Five Hundred "
                "| Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the poem opening the Book of the Sixes: the grief and "
        "consolation this collection kept apart from Paṭācārā's own "
        "verse in Thig 5.10. From Ru-Yi Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 1 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "a prose colophon names the speaker"),
        ("Speaker", "Two voices: an unnamed consoler, then the grieving "
                    "woman's own reply"),
        ("Form", "A four-verse consoling address, followed by two "
                 "verses in reply, closing on a prose colophon"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "completes, two books later, an account this "
                       "collection deliberately held back"),
    ],
    why=(
        "Thig 5.10's own guide noted that Paṭācārā is remembered by "
        "later tradition for an elaborate story of loss, and that her "
        "own verse there tells none of it. This poem, closing on a "
        "prose colophon naming her directly, is where that grief "
        "appears: a mother mourning a dead son, consoled with the same "
        "&lsquo;plucked arrow&rsquo; imagery and refuge formula used "
        "for Ubbirī in Thig 3.5, confirmed by its own closing line as "
        "&lsquo;how Paṭācārā... declared her enlightenment&rsquo;."),
    guide=[
        ("An unnamed voice, consoling a specific grief", [
            "&lsquo;One whose path you do not know... you mourn that "
            "being, crying, &ldquo;Oh my son!&rdquo;&rsquo; opens a "
            "four-verse address to someone grieving a dead child &mdash; "
            "the speaker is not named in the text itself, only "
            "identified by the poem's own closing colophon as having "
            "addressed Paṭācārā."]),
        ("An argument from not-knowing, not from doctrine recited", [
            "The consoling voice reasons from ignorance itself: "
            "&lsquo;as he came, so he went: why weep over that?&rsquo; "
            "&mdash; you cannot know where a being came from or where "
            "it goes, so grief for one arrival and departure, among "
            "countless others, makes little sense."]),
        ("The exact reply Ubbirī once gave", [
            "&lsquo;Oh! For you have plucked the arrow from me... "
            "today I've plucked the arrow, I'm hungerless, quenched. I "
            "go for refuge to that sage, the Buddha, to his teaching, "
            "and to the Sangha&rsquo; repeats, almost word for word, "
            "the reply Ubbirī gave in Thig 3.5 &mdash; the same "
            "formula, now given to Paṭācārā's own grief."]),
        ("A colophon that completes an earlier omission", [
            "&lsquo;That is how Paṭācārā, who had a following of five "
            "hundred, declared her enlightenment&rsquo; confirms "
            "directly what Thig 5.10 left unstated &mdash; this fuller "
            "title marking her later fame, arriving only after this "
            "poem has shown what that fame grew out of."]),
    ],
    terms=[
        ("Pa&ntilde;casatamatt&amacr;",
         "&ldquo;who had a following of five hundred&rdquo; &mdash; the "
         "fuller epithet this poem's title gives Paṭācārā, marking her "
         "later renown as a teacher."),
        ("puttasoka",
         "&ldquo;grief for a son&rdquo; &mdash; named directly as what "
         "the consoling voice addresses."),
        ("sallaṁ",
         "&ldquo;the arrow&rdquo; &mdash; the same image Ubbirī used in "
         "Thig 3.5, describing grief as a lodged, hard-to-see wound."),
        ("nicch&amacr;t&amacr; parinibbut&amacr;",
         "&ldquo;hungerless, quenched&rdquo; &mdash; the identical "
         "self-description Ubbirī used at her own turning point."),
        ("sara&#7751;a",
         "&ldquo;refuge&rdquo; &mdash; taken in the Buddha, his "
         "teaching, and the Sangha, closing this poem exactly as it "
         "closed Thig 3.5."),
    ],
    text_intro=(
        "The text in full: a consoling address, a reply, and a closing "
        "prose colophon. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.1:1.1-4.4"),
        ("p", "&sect;2", "thig6.1:5.1-6.4"),
        ("p", "&sect;3", ["thig6.1:7.1"]),
    ],
    quiz=[
        {"q": "What does the poem's opening address respond to?",
         "opts": [
             "A question about doctrine",
             "A woman grieving her dead son",
             "A dispute between two nuns",
             "A request for ordination"],
         "correct": 1,
         "expl": "Consoling a specific, named grief: 'Oh my son!'"},
        {"q": "What argument does the consoling voice make?",
         "opts": [
             "That grief should be expressed more loudly",
             "That the dead deserve no mourning at all",
             "That since you cannot know where a being came from or goes, grief for one arrival and departure makes little sense",
             "No argument is made"],
         "correct": 2,
         "expl": "Reasoning from not-knowing, rather than doctrine recited."},
        {"q": "What does the grieving woman's reply repeat, almost word for word, from Thig 3.5?",
         "opts": [
             "Nothing is shared with that poem",
             "The 'plucked arrow' imagery and the refuge formula Ubbirī used",
             "A description of a cremation ground",
             "A different, unrelated teaching"],
         "correct": 1,
         "expl": "The same formula that closed Ubbirī's reply to her own consoler."},
        {"q": "What does this poem's closing colophon state directly?",
         "opts": [
             "Nothing about who is speaking",
             "That an unnamed nun composed this poem for a stranger",
             "That is how Paṭācārā, who had a following of five hundred, declared her enlightenment",
             "That the poem is unfinished"],
         "correct": 2,
         "expl": "Confirming the grieving woman in this poem's reply is Paṭācārā herself."},
        {"q": "How does this poem relate to Thig 5.10?",
         "opts": [
             "It has no relationship to that poem",
             "It directly contradicts everything stated there",
             "It completes, under a fuller title, the story of loss that poem's own guide noted was left untold",
             "It is spoken by an entirely unrelated nun"],
         "correct": 2,
         "expl": "Two books apart, this poem supplies what Thig 5.10 itself did not narrate."},
        {"q": "What does 'Pañcasatamattā' mean, as part of this poem's title?",
         "opts": [
             "'Who had a following of five hundred' — marking her later renown as a teacher",
             "'A childless widow'",
             "'The mass of darkness'",
             "'A single robe'"],
         "correct": 0,
         "expl": "A fuller epithet than the bare name used for her own poem in Thig 5.10."},
        {"q": "Is the consoling speaker in this poem's opening verses named in the text itself?",
         "opts": [
             "No — the text does not name this speaker",
             "Yes, explicitly named as the Buddha",
             "Yes, explicitly named as another nun",
             "Yes, explicitly named as Ānanda"],
         "correct": 0,
         "expl": "This guide preserves that lack of an explicit identification, as with Ubbirī's own consoler in Thig 3.5."},
        {"q": "What does 'sallaṁ' mean?",
         "opts": [
             "'Refuge'",
             "'The arrow' — the same image of grief used in Thig 3.5",
             "'A following of five hundred'",
             "'Homelessness'"],
         "correct": 1,
         "expl": "Grief described as a lodged wound, then removed."},
        {"q": "What does this poem's closing verse declare, alongside 'hungerless, quenched'?",
         "opts": [
             "A wish to return to lay life",
             "A question left open",
             "No further statement is made",
             "Taking refuge in the Buddha, his teaching, and the Sangha"],
         "correct": 3,
         "expl": "The same Triple Refuge formula that closed Thig 3.5."},
        {"q": "What position does this poem hold in the Therigatha?",
         "opts": [
             "It closes the Book of the Fives",
             "It is the final poem of the entire collection",
             "It stands outside any book",
             "It opens the Book of the Sixes, the collection's sixth book"],
         "correct": 3,
         "expl": "The first of eight poems opening this new book."},
    ],
    marginalia=[
        ("A story completed, two books later", [
            "what Thig 5.10",
            "left untold"
        ]),
        ("An argument from not-knowing", [
            "why weep over",
            "arrival and departure?"
        ]),
        ("The same reply as Ubbirī's", [
            "the arrow plucked,",
            "refuge taken"
        ]),
        ("A colophon, naming her directly", [
            "'that is how',",
            "Paṭācārā's own account"
        ]),
    ],
    further=[
        '<a href="%s/thig6.1/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-5.10.html">Thig 5.10 &mdash; Pa&#7789;&amacr;c'
        "&amacr;r&amacr;</a> &mdash; her own verse, deliberately silent "
        "on the story this poem tells.",
        '<a href="thig-3.5.html">Thig 3.5 &mdash; Ubbir&imacr;</a> '
        "&mdash; the poem whose consolation and reply this one repeats "
        "almost word for word.",
        '<a href="thig-6.2.html">Thig 6.2 &mdash; V&amacr;se&#7789;&#7789;'
        "&imacr;</a> &mdash; the next poem in the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.2 — Vāseṭṭhī
# --------------------------------------------------------------------------- #
page(
    6, 2, "V&amacr;se&#7789;&#7789;&imacr;", "V&amacr;se&#7789;&#7789;"
    "&imacr;",
    meta_title="Thig 6.2 — Vāseṭṭhī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vāseṭṭhī's verses, three years of grief-driven breakdown "
        "resolved the moment she sees the Buddha at Mithilā. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 2 of 8",
    glance=[
        ("Setting", "Rubbish heaps, cemeteries, and highways for three "
                    "years, then the city of Mithilā"),
        ("Speaker", "The nun Vāseṭṭhī, recounting an extreme breakdown "
                    "and its sudden resolution"),
        ("Form", "Six four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; one "
                       "of the collection's starkest accounts of "
                       "grief's physical toll"),
    ],
    why=(
        "This poem continues the book's opening turn toward grief with "
        "an even starker account: &lsquo;struck down with grief for my "
        "son, deranged, out of my mind... nude, my hair flying&rsquo;, "
        "Vāseṭṭhī describes three years living on rubbish heaps, in "
        "cemeteries, and on highways, stricken by hunger and thirst "
        "&mdash; resolved not gradually but at the single moment she "
        "sees the Buddha at Mithilā."),
    guide=[
        ("Breakdown described without euphemism", [
            "&lsquo;Deranged, out of my mind... nude, my hair flying, I "
            "wandered here and there&rsquo; states her condition in "
            "blunt terms &mdash; not grief as an inner feeling alone, "
            "but a complete breakdown in appearance and conduct."]),
        ("Three years, in specific, degrading places", [
            "&lsquo;I lived on rubbish heaps, in cemeteries and "
            "highways... stricken by hunger and thirst&rsquo; names the "
            "actual places of her three years' wandering, a physical "
            "geography of destitution rather than a general description "
            "of suffering."]),
        ("Sanity regained before any teaching is given", [
            "&lsquo;Regaining my mind, I paid homage and sat down&rsquo; "
            "places her recovery before the Dhamma is even taught to "
            "her &mdash; simply seeing the Buddha at Mithilā is what "
            "restores her, prior to and separate from receiving "
            "instruction."]),
        ("Insight into grief's own origin, not just its end", [
            "&lsquo;I've fully understood the basis from which grief "
            "comes to be&rsquo; closes the poem with a specific claim: "
            "not only that her sorrow ended, but that she understood "
            "the cause it arose from &mdash; a fitting close for a book "
            "that opens on grief itself."]),
    ],
    terms=[
        ("V&amacr;se&#7789;&#7789;&imacr;",
         "this poem's speaker, whose three years of breakdown are "
         "described in unusually blunt, physical terms."),
        ("khittacitt&amacr; visa&ntilde;&ntilde;in&imacr;",
         "&ldquo;deranged, out of my mind&rdquo; &mdash; her own "
         "description of her condition after her son's death."),
        ("sugata",
         "&ldquo;the Holy One&rdquo;, an epithet for the Buddha, seen at "
         "the city of Mithilā."),
        ("adant&amacr;na&#7749; damet&amacr;ra&#7749;",
         "&ldquo;tamer of the untamed&rdquo; &mdash; an epithet applied "
         "to the Buddha in this poem's description of him."),
        ("pada&#7749; siva&#7749;",
         "&ldquo;the state of grace&rdquo; &mdash; what this poem says "
         "she realized, applying herself to the Teacher's words."),
    ],
    text_intro=(
        "The text in full: six verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.2:1.1-1.4"),
        ("p", "&sect;2", "thig6.2:2.1-2.4"),
        ("p", "&sect;3", "thig6.2:3.1-3.4"),
        ("p", "&sect;4", "thig6.2:4.1-4.4"),
        ("p", "&sect;5", "thig6.2:5.1-5.4"),
        ("p", "&sect;6", "thig6.2:6.1-6.4"),
    ],
    quiz=[
        {"q": "How does this poem describe Vāseṭṭhī's condition after her son's death?",
         "opts": [
             "Deranged and out of her mind, nude, her hair flying",
             "Calm and composed throughout",
             "Mildly inconvenienced",
             "No description is given"],
         "correct": 0,
         "expl": "A complete breakdown, stated in blunt physical terms."},
        {"q": "Where does the poem say she lived for three years?",
         "opts": [
             "In a royal palace",
             "In a quiet forest hermitage",
             "On rubbish heaps, in cemeteries, and on highways",
             "The poem does not specify"],
         "correct": 2,
         "expl": "A specific, degrading physical geography of destitution."},
        {"q": "Where does she see the Buddha?",
         "opts": [
             "In a dream",
             "At the city of Mithilā",
             "No specific location is given",
             "In her own home"],
         "correct": 1,
         "expl": "A named location grounding the account."},
        {"q": "What happens immediately upon seeing the Buddha, before any teaching is given?",
         "opts": [
             "She regains her mind",
             "Nothing changes at all",
             "She becomes angry",
             "She flees the scene"],
         "correct": 0,
         "expl": "Sanity restored simply by the sight of him, prior to instruction."},
        {"q": "What does the poem's closing verse claim she has understood?",
         "opts": [
             "Nothing further is claimed",
             "A prophecy about the future",
             "The basis from which grief comes to be",
             "Only that her son will be reborn well"],
         "correct": 2,
         "expl": "Insight into grief's origin, not only its resolution."},
        {"q": "What does 'khittacittā visaññinī' mean?",
         "opts": [
             "'The state of grace'",
             "'Tamer of the untamed'",
             "'Rubbish heaps'",
             "'Deranged, out of my mind' — her own description of her condition"],
         "correct": 3,
         "expl": "Named directly in this poem's opening verse."},
        {"q": "How long does the poem say her breakdown lasted?",
         "opts": [
             "One month",
             "A single day",
             "The duration is not given",
             "Three years"],
         "correct": 3,
         "expl": "'For three years I wandered, stricken by hunger and thirst.'"},
        {"q": "What does 'adantānaṁ dametāraṁ' describe?",
         "opts": [
             "Vāseṭṭhī's own former condition",
             "An epithet for the Buddha: 'tamer of the untamed'",
             "The rubbish heaps she once lived on",
             "A type of ordination"],
         "correct": 1,
         "expl": "Part of the poem's description of the Buddha at Mithilā."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The last poem",
             "The first poem",
             "The second poem, following the poem naming Paṭācārā",
             "It stands outside this book"],
         "correct": 2,
         "expl": "Following Thig 6.1, continuing this book's opening turn toward grief."},
        {"q": "How does this poem's account of breakdown compare to most confessions earlier in this collection?",
         "opts": [
             "It is identical to all of them",
             "It describes a more extreme, physically visible breakdown than most earlier accounts",
             "It describes no breakdown at all",
             "It is the mildest account in the entire collection"],
         "correct": 1,
         "expl": "Nudity, wandering, and three years' duration mark this as one of the starkest such accounts."},
    ],
    marginalia=[
        ("Breakdown, without euphemism", [
            "deranged, nude,",
            "wandering"
        ]),
        ("Three years, named places", [
            "rubbish heaps,",
            "cemeteries, highways"
        ]),
        ("Sanity, before any teaching", [
            "restored by sight",
            "alone"
        ]),
        ("Grief's own origin, understood", [
            "not just its end,",
            "but its cause"
        ]),
    ],
    further=[
        '<a href="%s/thig6.2/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.1.html">Thig 6.1 &mdash; Pa&#7789;&amacr;c'
        "&amacr;r&amacr;, Who Had a Following of Five Hundred</a> "
        "&mdash; the poem immediately before this one.",
        '<a href="thig-6.3.html">Thig 6.3 &mdash; Khem&amacr;</a> '
        "&mdash; the next poem in the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.3 — Khemā
# --------------------------------------------------------------------------- #
page(
    6, 3, "Khem&amacr;", "Khem&amacr;",
    meta_title="Thig 6.3 — Khemā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Khemā's verses, a third confrontation with Māra, followed by "
        "an unusually specific admission about a past life of "
        "misdirected worship. From Ru-Yi Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 3 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "Two voices: Māra, disguised as a young man offering "
                    "music, then Khemā's reply"),
        ("Form", "Six four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; a "
                       "third Māra confrontation, extended beyond the "
                       "stock formula into personal history"),
    ],
    why=(
        "This poem opens as a third confrontation with Māra in this "
        "collection, closing on the identical victorious quatrain "
        "already used in Thig 3.7 and 3.8. But Khemā's reply does not "
        "stop there: two further verses add something new, an "
        "unusually specific admission that her own earlier religious "
        "life &mdash; worshiping the stars and a sacred flame &mdash; "
        "was, by her own later judgment, foolishness mistaken for "
        "purity."),
    guide=[
        ("A specific temptation, more elaborate than Selā's or Somā's", [
            "&lsquo;You're so young and beautiful!... come, Khemā, let "
            "us enjoy the music of a five-piece band&rsquo; is more "
            "detailed than Māra's arguments to Selā or Somā &mdash; a "
            "concrete, named entertainment offered alongside the usual "
            "appeal to youth and beauty."]),
        ("The identical victory formula, reused a third time", [
            "&lsquo;Relishing is banished in every respect, and the "
            "mass of darkness is shattered... you're beaten, "
            "terminator!&rsquo; closes Khemā's central reply exactly as "
            "it closed Thig 3.7 and 3.8 &mdash; the same formula now "
            "given to a third woman's confrontation."]),
        ("A confession that goes beyond the stock formula", [
            "Two further verses extend past where Selā's and Somā's "
            "poems ended: &lsquo;worshiping the stars, serving the "
            "sacred flame in a grove... foolish me, I thought this was "
            "purity&rsquo; &mdash; a specific, personal admission about "
            "a religious life before the Buddha's path, distinct from "
            "the victory over Māra itself."]),
        ("A judgment reversed, not merely a practice abandoned", [
            "&lsquo;Failing to grasp the true nature of things&rsquo; "
            "names the error precisely: not simply that her former "
            "practice was wrong, but that her very judgment of what "
            "counted as &lsquo;purity&rsquo; was mistaken."]),
    ],
    terms=[
        ("Khem&amacr;",
         "this poem's speaker, whose confrontation with Māra extends "
         "into an admission about her earlier religious life."),
        ("pa&ntilde;ca&#7749;gika turiya",
         "a &ldquo;five-piece band&rdquo; &mdash; the specific "
         "entertainment Māra offers in his temptation."),
        ("sattis&#363;l&#363;pam&amacr; k&amacr;m&amacr;",
         "&ldquo;sensual pleasures are like swords and spears&rdquo; "
         "&mdash; the same metaphor used by Selā in Thig 3.7, reused "
         "here."),
        ("yath&amacr;bhucca",
         "&ldquo;the true nature of things&rdquo; &mdash; what her "
         "earlier worship, by her own later account, failed to grasp."),
        ("satthus&amacr;sanak&amacr;rik&amacr;",
         "&ldquo;doing the teacher's bidding&rdquo; &mdash; Khemā's own "
         "closing self-description, naming her present practice."),
    ],
    text_intro=(
        "The text in full: six verses, extending past a third "
        "confrontation with Māra. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.3:1.1-1.4"),
        ("p", "&sect;2", "thig6.3:2.1-2.4"),
        ("p", "&sect;3", "thig6.3:3.1-3.4"),
        ("p", "&sect;4", "thig6.3:4.1-4.4"),
        ("p", "&sect;5", "thig6.3:5.1-5.4"),
        ("p", "&sect;6", "thig6.3:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does Māra specifically offer Khemā in his temptation?",
         "opts": [
             "Wealth and status",
             "The music of a five-piece band",
             "A journey to a distant kingdom",
             "Nothing specific is offered"],
         "correct": 1,
         "expl": "A concrete, named entertainment, more detailed than the temptations to Selā or Somā."},
        {"q": "What quatrain closes Khemā's central reply, identical to Thig 3.7 and 3.8?",
         "opts": [
             "'Though subject to so many painful things...'",
             "'I go for refuge to that sage, the Buddha'",
             "'Relishing is banished in every respect... you're beaten, terminator!'",
             "No closing quatrain is shared"],
         "correct": 2,
         "expl": "The identical victorious formula, now given to a third woman's confrontation."},
        {"q": "What does Khemā's poem add beyond this shared formula?",
         "opts": [
             "Nothing further is added",
             "An admission that her earlier worship of stars and a sacred flame was, by her own judgment, foolishness",
             "A second confrontation with Māra",
             "A description of a cremation ground"],
         "correct": 1,
         "expl": "Two further verses, extending past where Selā's and Somā's poems ended."},
        {"q": "How does Khemā describe her earlier religious practice, in retrospect?",
         "opts": [
             "As already fully correct",
             "As harmless but pointless",
             "As foolishness mistaken for purity",
             "The poem does not describe it"],
         "correct": 2,
         "expl": "'Foolish me, I thought this was purity.'"},
        {"q": "What specifically does 'yathābhucca' name as her earlier failure?",
         "opts": [
             "A failure of physical strength",
             "A failure to follow monastic rules",
             "No specific failure is named",
             "Failing to grasp the true nature of things — not just wrong practice, but a mistaken judgment"],
         "correct": 3,
         "expl": "The error was in judgment itself, not only in outward practice."},
        {"q": "What does this poem's central reply compare sensual pleasures to?",
         "opts": [
             "Swords and spears, with the aggregates as their chopping block",
             "A gentle breeze",
             "Nothing is compared",
             "A beautiful painting"],
         "correct": 0,
         "expl": "The same metaphor used by Selā in Thig 3.7."},
        {"q": "How many times, counting this poem, has the exact victory quatrain over Māra now appeared?",
         "opts": [
             "Three times, after Thig 3.7 and 3.8",
             "Once",
             "Twice",
             "It has never appeared before"],
         "correct": 0,
         "expl": "A recurring formula, now given to a third confrontation."},
        {"q": "How does this poem close?",
         "opts": [
             "With a question left unanswered",
             "'Doing the teacher's bidding, I am released from all suffering'",
             "Mid-confrontation, with no resolution",
             "With the 'no more future lives' formula"],
         "correct": 1,
         "expl": "Her own closing self-description, naming her present practice."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The last poem",
             "The first poem",
             "It stands outside this book",
             "The third poem, following Vāseṭṭhī"],
         "correct": 3,
         "expl": "Following Thig 6.2, continuing the Book of the Sixes."},
        {"q": "What does 'satthusāsanakārikā' mean?",
         "opts": [
             "'A five-piece band'",
             "'The true nature of things'",
             "'Doing the teacher's bidding' — Khemā's own closing self-description",
             "'Swords and spears'"],
         "correct": 2,
         "expl": "Naming her present practice, in contrast with her earlier misdirected worship."},
    ],
    marginalia=[
        ("A temptation, more specific", [
            "a five-piece band,",
            "named directly"
        ]),
        ("A formula, used a third time", [
            "the same victory,",
            "word for word"
        ]),
        ("A confession beyond the formula", [
            "stars and flame,",
            "foolishness mistaken for purity"
        ]),
        ("Judgment itself, reversed", [
            "not just wrong practice,",
            "but mistaken purity"
        ]),
    ],
    further=[
        '<a href="%s/thig6.3/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.2.html">Thig 6.2 &mdash; V&amacr;se&#7789;&#7789;'
        "&imacr;</a> &mdash; the poem immediately before this one.",
        '<a href="thig-3.7.html">Thig 3.7 &mdash; Sel&amacr;</a> '
        "&mdash; an earlier poem sharing this one's exact victory "
        "quatrain over Māra.",
        '<a href="thig-6.4.html">Thig 6.4 &mdash; Suj&amacr;t&amacr;</a> '
        "&mdash; the next poem in the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.4 — Sujātā
# --------------------------------------------------------------------------- #
page(
    6, 4, "Suj&amacr;t&amacr;", "Suj&amacr;t&amacr;",
    meta_title="Thig 6.4 — Sujātā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sujātā's verses, insight found by accident on the way home "
        "from a pleasure outing, not through any spiritual search. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 4 of 8",
    glance=[
        ("Setting", "A park outing, then a monastic dwelling encountered "
                    "on the way home"),
        ("Speaker", "The nun Sujātā, narrating an entirely unsought "
                    "encounter and its result"),
        ("Form", "Six four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "insight found entirely by chance, mid-pleasure "
                       "outing"),
    ],
    why=(
        "This poem opens with no religious intent whatsoever: "
        "&lsquo;adorned with jewelry and all dressed up... I left my "
        "house and took myself to the park&rsquo;. Only on the way "
        "home, entering a monastic dwelling simply &lsquo;to "
        "see&rsquo; it, does Sujātā encounter the Buddha at all "
        "&mdash; and finds &lsquo;the stainless Dhamma, the state free "
        "of death&rsquo; on the spot, still in the middle of an "
        "ordinary day's outing."),
    guide=[
        ("A pleasure outing, described in full", [
            "&lsquo;Adorned with jewelry and all dressed up, with "
            "garlands, and sandalwood makeup piled on... taking food and "
            "drink, staples and dainties in no small amount&rsquo; opens "
            "the poem with no hint of spiritual seeking &mdash; a "
            "detailed account of preparing for an ordinary day of "
            "enjoyment."]),
        ("An encounter entirely by accident", [
            "&lsquo;Returning to my own house, I saw a monastic "
            "dwelling, and so I entered the Añjana wood at Sāketa&rsquo; "
            "&mdash; she enters not seeking teaching, but simply to "
            "look, on her way back from the park she had already "
            "visited."]),
        ("Insight on the spot, mid-outing, before any renunciation", [
            "&lsquo;Right there I found the stainless Dhamma, the state "
            "free of death&rsquo; places her realization at the exact "
            "moment of this accidental visit &mdash; still dressed for "
            "pleasure, not yet having renounced anything."]),
        ("Formal renunciation, only afterward", [
            "&lsquo;Then, having understood the true teaching, I went "
            "forth to homelessness. I've attained the three "
            "knowledges&rsquo; separates this initial, unsought insight "
            "from her later, formal ordination &mdash; two distinct "
            "steps, not one event."]),
    ],
    terms=[
        ("Suj&amacr;t&amacr;",
         "this poem's speaker, whose first encounter with the Dhamma "
         "happens entirely by accident."),
        ("uyy&amacr;na",
         "the &ldquo;park&rdquo; she visits for pleasure, the "
         "destination of her outing before her accidental encounter."),
        ("A&ntilde;jana vana",
         "the Añjana wood at Sāketa, the monastic dwelling she enters "
         "simply to look at, on her way home."),
        ("lokapajjota",
         "&ldquo;the light of the world&rdquo; &mdash; her own epithet "
         "for the Buddha, seen for the first time at this dwelling."),
        ("amata&#7749; pada&#7749;",
         "&ldquo;the state free of death&rdquo; &mdash; what she says "
         "she found &lsquo;right there&rsquo;, at the moment of this "
         "unsought visit."),
    ],
    text_intro=(
        "The text in full: six verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.4:1.1-1.4"),
        ("p", "&sect;2", "thig6.4:2.1-2.4"),
        ("p", "&sect;3", "thig6.4:3.1-3.4"),
        ("p", "&sect;4", "thig6.4:4.1-4.4"),
        ("p", "&sect;5", "thig6.4:5.1-5.4"),
        ("p", "&sect;6", "thig6.4:6.1-6.4"),
    ],
    quiz=[
        {"q": "What is Sujātā doing at the start of this poem?",
         "opts": [
             "Seeking out a teacher",
             "Preparing for and enjoying a pleasure outing to a park",
             "Meditating in a forest",
             "Already living as a nun"],
         "correct": 1,
         "expl": "No religious intent at all in the poem's opening verses."},
        {"q": "How does Sujātā come to encounter the Buddha's teaching?",
         "opts": [
             "She had planned the visit for months",
             "A teacher sought her out directly",
             "By accident, entering a monastic dwelling simply to look at it on her way home",
             "She had no such encounter"],
         "correct": 2,
         "expl": "An entirely unsought visit, on the way back from the park."},
        {"q": "When does the poem say she found 'the stainless Dhamma'?",
         "opts": [
             "Years after her ordination",
             "Right there, at the moment of this accidental visit",
             "Before she was even born",
             "The poem does not specify a time"],
         "correct": 1,
         "expl": "Insight arriving in the middle of an ordinary day's outing."},
        {"q": "What had Sujātā already done earlier that same day, before this encounter?",
         "opts": [
             "Fasted completely",
             "Traveled to a distant kingdom",
             "Enjoyed herself at a park with food and drink",
             "Nothing else is described"],
         "correct": 2,
         "expl": "The pleasure outing described in the poem's opening verses."},
        {"q": "What does the poem say happened only afterward, once she understood the true teaching?",
         "opts": [
             "She went forth to homelessness and attained the three knowledges",
             "She returned to her former life unchanged",
             "She forgot what she had seen",
             "Nothing further happened"],
         "correct": 0,
         "expl": "Formal renunciation, kept distinct from her initial, unsought insight."},
        {"q": "What does 'lokapajjota' mean?",
         "opts": [
             "'A monastic dwelling'",
             "'A pleasure outing'",
             "'The three knowledges'",
             "'The light of the world' — her own epithet for the Buddha"],
         "correct": 3,
         "expl": "Named at the moment she first sees him."},
        {"q": "How is Sujātā dressed at the moment of her first encounter with the Buddha's teaching?",
         "opts": [
             "In simple monastic robes already",
             "The poem does not describe her clothing",
             "In mourning clothes",
             "Still adorned with jewelry and decorations, dressed for her outing"],
         "correct": 3,
         "expl": "Insight arrives before any change in her outward circumstances."},
        {"q": "What does 'Añjana vana' name?",
         "opts": [
             "A type of jewelry",
             "The park she visited for pleasure",
             "The monastic dwelling at Sāketa she enters by chance",
             "A river"],
         "correct": 2,
         "expl": "The specific site of her accidental encounter."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The fourth poem, following Khemā",
             "The last poem",
             "The first poem",
             "It stands outside this book"],
         "correct": 0,
         "expl": "Following Thig 6.3, continuing the Book of the Sixes."},
        {"q": "What makes this poem's sequence distinctive among accounts in this collection?",
         "opts": [
             "It is identical to every other account",
             "Insight arrives with no religious search at all, in the middle of an unrelated pleasure outing",
             "It describes years of prior monastic training",
             "No insight is described anywhere in the poem"],
         "correct": 1,
         "expl": "One of this collection's most incidental paths to realization."},
    ],
    marginalia=[
        ("No search at all, at first", [
            "jewelry, garlands,",
            "a day at the park"
        ]),
        ("An encounter, entirely by chance", [
            "entering only",
            "to look"
        ]),
        ("Insight, mid-outing", [
            "still dressed",
            "for pleasure"
        ]),
        ("Renunciation, only afterward", [
            "two distinct steps,",
            "not one event"
        ]),
    ],
    further=[
        '<a href="%s/thig6.4/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.3.html">Thig 6.3 &mdash; Khem&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-6.5.html">Thig 6.5 &mdash; Anopam&amacr;</a> '
        "&mdash; the next poem in the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.5 — Anopamā
# --------------------------------------------------------------------------- #
page(
    6, 5, "Anopam&amacr;", "Anopam&amacr;",
    meta_title="Thig 6.5 — Anopamā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Anopamā's verses, an heiress valued in gold by a quoted "
        "marriage proposal, who instead attains the third fruit on the "
        "spot. From Ru-Yi Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 5 of 8",
    glance=[
        ("Setting", "A wealthy household, sought after by suitors, then "
                    "an audience with the Buddha"),
        ("Speaker", "The nun Anopamā, narrating her own valuation by "
                    "suitors, then her attainment"),
        ("Form", "Six four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "quotes a marriage proposal's exact valuation in "
                       "gold"),
    ],
    why=(
        "This poem opens with Anopamā's worth quantified precisely by a "
        "suitor's own quoted words: &lsquo;however much your daughter "
        "Anopamā weighs, I'll give you eight times that in gold coin "
        "and gems&rsquo;. Against this transactional valuation, the "
        "poem sets what actually determines her path: seeing the "
        "Buddha, and attaining &lsquo;the third fruit&rsquo; on the "
        "spot, still seated, before she has renounced anything."),
    guide=[
        ("An heiress, sought and quantified", [
            "&lsquo;Born into an eminent family, affluent and "
            "wealthy... sought by princes, coveted by sons of the "
            "wealthy&rsquo; establishes her status before any suitor "
            "speaks &mdash; setting up the specific proposal that "
            "follows."]),
        ("A proposal, quoted in the suitor's own words", [
            "&lsquo;Give me Anopamā! However much your daughter Anopamā "
            "weighs, I'll give you eight times that in gold coin and "
            "gems&rsquo; is presented as direct quotation, not summary "
            "&mdash; her worth stated in a specific multiple of her own "
            "body weight in gold."]),
        ("A named attainment, reached while still seated", [
            "&lsquo;While sitting in that seat, I realized the third "
            "fruit&rsquo; names a specific stage of the path, reached "
            "in the same sitting as her audience with the Buddha "
            "&mdash; before she has shaved her head or gone forth at "
            "all."]),
        ("A count of days, closing the poem", [
            "&lsquo;This is the seventh day since my craving dried "
            "up&rsquo; closes the poem with the same precise-day formula "
            "used in Thig 2.9, 2.10, and 3.1 &mdash; a dated breakthrough, "
            "arriving only after she has finally gone forth."]),
    ],
    terms=[
        ("Anopam&amacr;",
         "this poem's speaker, &ldquo;Majjha's true-born daughter&rdquo;, "
         "whose worth a suitor quantifies precisely in gold."),
        ("r&amacr;japutta",
         "&ldquo;princes&rdquo; &mdash; among those named as seeking "
         "her, alongside the sons of wealthy families."),
        ("a&#7789;&#7789;hagu&#7751;a&#7749;",
         "&ldquo;eight times that&rdquo; &mdash; the specific multiple "
         "of her body weight in gold and gems offered for her."),
        ("tatiya&#7749; phala&#7749;",
         "&ldquo;the third fruit&rdquo; &mdash; a specific named stage "
         "of the path, attained while she is still seated before the "
         "Buddha."),
        ("ta&#7751;h&amacr; visosit&amacr;",
         "&ldquo;craving dried up&rdquo; &mdash; the poem's closing "
         "state, dated to a specific seventh day."),
    ],
    text_intro=(
        "The text in full: six verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.5:1.1-1.4"),
        ("p", "&sect;2", "thig6.5:2.1-2.4"),
        ("p", "&sect;3", "thig6.5:3.1-3.4"),
        ("p", "&sect;4", "thig6.5:4.1-4.4"),
        ("p", "&sect;5", "thig6.5:5.1-5.4"),
        ("p", "&sect;6", "thig6.5:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does this poem's opening verse establish about Anopamā's family?",
         "opts": [
             "That she was born into poverty",
             "That she was born into an eminent, wealthy family",
             "No family background is given",
             "That she had no living relatives"],
         "correct": 1,
         "expl": "Setting up the specific marriage proposal that follows."},
        {"q": "How is the marriage proposal presented in this poem?",
         "opts": [
             "Only summarized briefly",
             "It is not mentioned at all",
             "Quoted directly, in the suitor's own words",
             "Reported secondhand by a servant"],
         "correct": 2,
         "expl": "Direct quotation, not summary."},
        {"q": "How much gold and gems does the suitor offer for Anopamā, according to his quoted words?",
         "opts": [
             "An unspecified 'great fortune'",
             "Twice her weight",
             "Eight times her weight",
             "No amount is specified"],
         "correct": 2,
         "expl": "A precise multiple of her own body weight."},
        {"q": "What does Anopamā attain while still seated before the Buddha?",
         "opts": [
             "Nothing is attained at this point",
             "A promise of future teaching",
             "The third fruit — a specific named stage of the path",
             "Full ordination"],
         "correct": 2,
         "expl": "Before she has shaved her head or gone forth at all."},
        {"q": "How does this poem's closing line date her craving's ending?",
         "opts": [
             "To an unspecified future date",
             "To the seventh day",
             "It gives no specific date",
             "To many years later"],
         "correct": 1,
         "expl": "The same precise-day formula used in Thig 2.9, 2.10, and 3.1."},
        {"q": "What does 'tatiyaṁ phalaṁ' mean?",
         "opts": [
             "'Eight times that'",
             "'The third fruit' — a specific named stage of the path",
             "'A marriage proposal'",
             "'Craving dried up'"],
         "correct": 1,
         "expl": "Attained in the same sitting as her audience with the Buddha."},
        {"q": "Who besides princes is named as seeking Anopamā in marriage?",
         "opts": [
             "Sons of wealthy families",
             "No one else is named",
             "Only distant relatives",
             "Foreign kings exclusively"],
         "correct": 0,
         "expl": "Named alongside princes in this poem's second verse."},
        {"q": "What happens only after Anopamā's attainment of the third fruit?",
         "opts": [
             "She shaves her head and goes forth to homelessness",
             "She marries the suitor",
             "She returns to her family unchanged",
             "Nothing further happens"],
         "correct": 0,
         "expl": "Formal renunciation follows her initial attainment, not the reverse."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The last poem",
             "The first poem",
             "It stands outside this book",
             "The fifth poem, following Sujātā"],
         "correct": 3,
         "expl": "Following Thig 6.4, continuing the Book of the Sixes."},
        {"q": "What does 'aṭṭhaguṇaṁ' mean?",
         "opts": [
             "'The third fruit'",
             "'A monastic dwelling'",
             "'Craving dried up'",
             "'Eight times that' — the multiple of gold offered for her"],
         "correct": 3,
         "expl": "Part of the suitor's precisely quantified offer."},
    ],
    marginalia=[
        ("An heiress, precisely valued", [
            "eight times her weight,",
            "quoted directly"
        ]),
        ("A proposal, in his own words", [
            "not summarized,",
            "but quoted"
        ]),
        ("A fruit, attained while seated", [
            "before shaving her head,",
            "before going forth"
        ]),
        ("A dated breakthrough, closing", [
            "the seventh day,",
            "same formula as 3.1"
        ]),
    ],
    further=[
        '<a href="%s/thig6.5/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.4.html">Thig 6.4 &mdash; Suj&amacr;t&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-6.6.html">Thig 6.6 &mdash; Mah&amacr;paj&amacr;pati '
        "Gotam&imacr;</a> &mdash; the next poem in the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.6 — Mahāpajāpati Gotamī
# --------------------------------------------------------------------------- #
page(
    6, 6, "Mah&amacr;paj&amacr;pati Gotam&imacr;", "Mah&amacr;paj&amacr;"
    "pati Gotam&imacr;",
    meta_title="Thig 6.6 — Mahāpajāpati Gotamī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Mahāpajāpati Gotamī's verses, direct homage to the Buddha, an "
        "account of shifting family roles across many lives, and a "
        "closing turn to praise his own mother. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Sixes &middot; Poem 6 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "The nun Mahāpajāpati Gotamī, addressing the Buddha "
                    "directly, then reflecting more broadly"),
        ("Form", "Six four-line verses"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "opens with unusually direct, personal homage"),
    ],
    why=(
        "This poem opens with an exclamation rare in this collection's "
        "register: &lsquo;Oh Buddha, my hero: homage to you!&rsquo;, "
        "before mapping her own attainment directly onto the four noble "
        "truths. Partway through, it turns to an unusual reflection on "
        "her own past lives &mdash; not as one identity repeated, but "
        "as a shifting sequence of family roles across genders and "
        "generations &mdash; before closing with praise directed not at "
        "herself, but at the Buddha's own mother."),
    guide=[
        ("Homage, exclaimed rather than stated", [
            "&lsquo;Oh Buddha, my hero: homage to you! Supreme among "
            "all beings&rsquo; opens with a directness and warmth "
            "distinct from the calmer register of most poems in this "
            "collection &mdash; an address, not only an account."]),
        ("Attainment mapped onto the four noble truths directly", [
            "&lsquo;All suffering is fully understood; craving&mdash;its "
            "cause&mdash;is dried up; the eightfold path has been "
            "developed; and cessation has been realized by me&rsquo; "
            "states her attainment in the four truths' own structure, "
            "one clause for each."]),
        ("Past lives, remembered as shifting family roles", [
            "&lsquo;Previously I was a mother, a son, a father, a "
            "brother, and a grandmother&rsquo; is an unusually direct "
            "acknowledgment that rebirth crosses gender and generation "
            "&mdash; not the same identity recurring, but a sequence of "
            "different family positions entirely."]),
        ("A closing turn, praising someone else entirely", [
            "The poem's final verse shifts away from her own attainment "
            "to praise Māyā, the Buddha's birth mother: &lsquo;it was "
            "truly for the benefit of many that Māyā gave birth to "
            "Gotama&rsquo; &mdash; ending not on her own realization, "
            "but on gratitude directed outward."]),
    ],
    terms=[
        ("Mah&amacr;paj&amacr;pati Gotam&imacr;",
         "this poem's speaker, whose homage to the Buddha opens the "
         "poem directly."),
        ("a&#7789;&#7789;ha&#7749;gika magga",
         "the eightfold path, named as developed among the four "
         "elements of her attainment."),
        ("m&amacr;t&amacr; putto pit&amacr; bh&amacr;t&amacr; ayyak&amacr;",
         "&ldquo;mother, son, father, brother, and grandmother&rdquo; "
         "&mdash; the sequence of past-life family roles she recounts, "
         "crossing gender and generation."),
        ("vikkh&imacr;&#7751;o j&amacr;tisa&#7749;s&amacr;ro",
         "&ldquo;transmigration through births is finished&rdquo; "
         "&mdash; the collection's standard closing formula, used here "
         "mid-poem rather than at its very end."),
        ("M&amacr;y&amacr;",
         "the Buddha's birth mother, praised directly in this poem's "
         "closing verse for the benefit her son brought to many."),
    ],
    text_intro=(
        "The text in full: six verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.6:1.1-1.4"),
        ("p", "&sect;2", "thig6.6:2.1-2.4"),
        ("p", "&sect;3", "thig6.6:3.1-3.4"),
        ("p", "&sect;4", "thig6.6:4.1-4.4"),
        ("p", "&sect;5", "thig6.6:5.1-5.4"),
        ("p", "&sect;6", "thig6.6:6.1-6.4"),
    ],
    quiz=[
        {"q": "How does this poem open?",
         "opts": [
             "With a narrative setting",
             "With direct, exclaimed homage: 'Oh Buddha, my hero: homage to you!'",
             "With a dialogue with Māra",
             "With a description of a cremation ground"],
         "correct": 1,
         "expl": "An unusually warm and direct address, distinct from this collection's calmer register."},
        {"q": "What framework does the second verse use to state her attainment?",
         "opts": [
             "No specific framework is used",
             "A list of ornaments given up",
             "The four noble truths, one clause for each",
             "A description of a specific meditation posture"],
         "correct": 2,
         "expl": "Suffering understood, craving's cause dried up, the path developed, cessation realized."},
        {"q": "What does the poem say about her own past lives?",
         "opts": [
             "That she has no memory of them",
             "That she was always born as the same figure",
             "That she was previously a mother, a son, a father, a brother, and a grandmother",
             "That her past lives are not mentioned"],
         "correct": 2,
         "expl": "An unusual acknowledgment that rebirth crosses both gender and generation."},
        {"q": "Who does the poem's closing verse praise?",
         "opts": [
             "Māyā, the Buddha's birth mother",
             "Mahāpajāpati Gotamī's own achievement",
             "No one in particular",
             "A different, unnamed nun"],
         "correct": 0,
         "expl": "A shift away from her own attainment, praising someone else entirely."},
        {"q": "What does the poem say Māyā's giving birth to Gotama accomplished?",
         "opts": [
             "Nothing of significance",
             "It was truly for the benefit of many",
             "It caused only difficulty",
             "The poem does not describe any benefit"],
         "correct": 1,
         "expl": "Framed as a benefit extending far beyond her own son."},
        {"q": "What does 'vikkhīṇo jātisaṁsāro' mean?",
         "opts": [
             "'My hero'",
             "'The eightfold path'",
             "'A grandmother'",
             "'Transmigration through births is finished' — used here mid-poem"],
         "correct": 3,
         "expl": "The collection's standard closing formula, appearing before this poem's actual end."},
        {"q": "What does the poem's fifth verse describe seeing?",
         "opts": [
             "A vision of Māra",
             "The disciples in harmony, energetic and resolute",
             "A cremation ground",
             "Nothing is described in this verse"],
         "correct": 1,
         "expl": "Named directly as itself a form of homage to the Buddhas."},
        {"q": "How does this poem's opening tone compare to most other poems in this collection?",
         "opts": [
             "More directly warm and exclamatory than most",
             "Identical in every respect",
             "More reserved and understated than usual",
             "Entirely without any address to the Buddha"],
         "correct": 0,
         "expl": "A distinctive register for this collection."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The last poem",
             "The first poem",
             "It stands outside this book",
             "The sixth poem, following Anopamā"],
         "correct": 3,
         "expl": "Following Thig 6.5, continuing the Book of the Sixes."},
        {"q": "What does 'māta putto pitā bhātā ayyakā' name?",
         "opts": [
             "A list of monastic robes",
             "The four noble truths",
             "The sequence of family roles she recounts having held in past lives",
             "A place name"],
         "correct": 2,
         "expl": "Crossing gender and generation across her past lives."},
    ],
    marginalia=[
        ("Homage, exclaimed", [
            "'my hero' —",
            "an unusually warm address"
        ]),
        ("Attainment, in the truths' own shape", [
            "one clause",
            "for each truth"
        ]),
        ("Past lives, shifting roles", [
            "mother, son, father,",
            "brother, grandmother"
        ]),
        ("A closing turn, outward", [
            "praising Māyā,",
            "not herself"
        ]),
    ],
    further=[
        '<a href="%s/thig6.6/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.5.html">Thig 6.5 &mdash; Anopam&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-6.7.html">Thig 6.7 &mdash; Gutt&amacr;</a> '
        "&mdash; the next poem in the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.7 — Guttā
# --------------------------------------------------------------------------- #
page(
    6, 7, "Gutt&amacr;", "Gutt&amacr;",
    meta_title="Thig 6.7 — Guttā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the instruction addressed to Guttā, naming the fetters in "
        "full and predicting, rather than reporting, her release. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 7 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "Not identified; direct, second-person instruction "
                    "addressed to the nun Guttā throughout"),
        ("Form", "Six four-line verses, entirely instructional"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the "
                       "most doctrinally dense named list of fetters in "
                       "this collection"),
    ],
    why=(
        "Unlike most poems in this book, Guttā never speaks in her own "
        "voice here: an unnamed instructor addresses her directly, "
        "second person throughout, naming the fetters that bind beings "
        "to rebirth in unusually complete detail &mdash; and framing "
        "her release not as something already accomplished, but as a "
        "prediction of what will follow once she has let them go."),
    guide=[
        ("An instruction with no reply, like Abhirūpanandā's", [
            "&lsquo;Guttā, you have given up your child, your wealth, "
            "and all that you love. Foster the goal for which you went "
            "forth&rsquo; opens an address that, like Thig 2.1's "
            "instruction to Nandā, receives no first-person reply within "
            "this poem itself &mdash; only the instruction survives "
            "here."]),
        ("Five lower fetters, named completely", [
            "&lsquo;Sensual desire and ill will, and substantialist "
            "view; misapprehension of precepts and observances, and "
            "doubt as the fifth&rsquo; lists a specific, standard "
            "category &mdash; the five lower fetters &mdash; more "
            "completely and technically than any doctrinal list earlier "
            "in this collection."]),
        ("A second set, named further on", [
            "&lsquo;When you're rid of desire, conceit, ignorance, and "
            "restlessness, having cut the fetters, you'll make an end "
            "to suffering&rsquo; adds a further set of defilements, "
            "extending past the five already named."]),
        ("Prediction, not report", [
            "Every verb describing her release is future tense: "
            "&lsquo;you won't come back... you'll make an end... you "
            "will live at peace&rsquo; &mdash; this poem promises an "
            "outcome rather than confirming one already reached, a "
            "different grammatical stance from most first-person "
            "accounts in this collection."]),
    ],
    terms=[
        ("Gutt&amacr;",
         "the nun addressed throughout this poem, who is given no "
         "first-person reply within it."),
        ("sa&#7749;yojana",
         "&ldquo;fetters&rdquo; &mdash; the central doctrinal category "
         "this poem names in unusually complete detail."),
        ("sakk&amacr;yadi&#7789;&#7789;hi",
         "&ldquo;substantialist view&rdquo; &mdash; one of the five "
         "lower fetters named explicitly in this poem's third verse."),
        ("orambh&amacr;gamaniya",
         "&ldquo;lower&rdquo;, describing the specific category of five "
         "fetters this poem lists completely."),
        ("uddhacca",
         "&ldquo;restlessness&rdquo; &mdash; the last of a second set of "
         "defilements named further on in the poem."),
    ],
    text_intro=(
        "The text in full: six verses, entirely instructional. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.7:1.1-1.4"),
        ("p", "&sect;2", "thig6.7:2.1-2.4"),
        ("p", "&sect;3", "thig6.7:3.1-3.4"),
        ("p", "&sect;4", "thig6.7:4.1-4.4"),
        ("p", "&sect;5", "thig6.7:5.1-5.4"),
        ("p", "&sect;6", "thig6.7:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does this poem's opening verse remind Guttā she has already given up?",
         "opts": [
             "Nothing is mentioned",
             "Her child, her wealth, and all that she loves",
             "Only her wealth",
             "A specific piece of jewelry"],
         "correct": 1,
         "expl": "Named directly as the cost of her going forth, in the poem's first line."},
        {"q": "Does Guttā reply in her own first-person voice anywhere in this poem?",
         "opts": [
             "Yes, extensively",
             "Yes, but only in the final verse",
             "No — like Thig 2.1's instruction to Nandā, only the instruction survives here",
             "Yes, in every verse"],
         "correct": 2,
         "expl": "An instruction with no reply within the poem itself."},
        {"q": "What five things does this poem name as the 'lower fetters'?",
         "opts": [
             "No specific list is given",
             "Wealth, status, family, health, and reputation",
             "Sensual desire, ill will, substantialist view, misapprehension of precepts, and doubt",
             "Five different meditation postures"],
         "correct": 2,
         "expl": "A complete, technical enumeration of a standard category."},
        {"q": "What second set of defilements does the poem name further on?",
         "opts": [
             "No second set is named",
             "Desire, conceit, ignorance, and restlessness",
             "Only a repetition of the first five",
             "A list of monastic offenses"],
         "correct": 1,
         "expl": "Extending past the five lower fetters already named."},
        {"q": "What grammatical tense dominates this poem's description of Guttā's release?",
         "opts": [
             "Past tense, reporting an already-completed attainment",
             "Present tense only",
             "Future tense — a prediction, not a report",
             "No particular tense pattern"],
         "correct": 2,
         "expl": "'You won't come back... you'll make an end... you will live at peace.'"},
        {"q": "What does 'sakkāyadiṭṭhi' mean?",
         "opts": [
             "'Substantialist view' — one of the five lower fetters named here",
             "'Restlessness'",
             "'A child and wealth'",
             "'Peace'"],
         "correct": 0,
         "expl": "Named explicitly among the five lower fetters."},
        {"q": "How does this poem's structure compare to Thig 2.1's instruction to Nandā?",
         "opts": [
             "It has no similarity at all",
             "Both are entirely first-person accounts",
             "Thig 2.1 is far longer than this poem",
             "Similar in kind — direct instruction with no reply — but more doctrinally extensive here"],
         "correct": 3,
         "expl": "A shared structure, extended into more complete doctrinal detail."},
        {"q": "What does 'saṁyojana' mean?",
         "opts": [
             "'Fetters' — the central doctrinal category this poem addresses",
             "'A child'",
             "'The park'",
             "'Restlessness'"],
         "correct": 0,
         "expl": "The recurring category structuring this entire poem's instruction."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The last poem",
             "The first poem",
             "It stands outside this book",
             "The seventh poem, following Mahāpajāpati Gotamī"],
         "correct": 3,
         "expl": "Following Thig 6.6, continuing the Book of the Sixes."},
        {"q": "What does 'uddhacca' mean?",
         "opts": [
             "'Substantialist view'",
             "'A fetter cut in the first watch of the night'",
             "'Fostering the goal'",
             "'Restlessness' — the last of a second set of defilements named"],
         "correct": 3,
         "expl": "Named alongside desire, conceit, and ignorance in this poem's later verses."},
    ],
    marginalia=[
        ("An instruction, no reply given", [
            "like Thig 2.1's",
            "address to Nandā"
        ]),
        ("Five fetters, named in full", [
            "the most complete list",
            "in this collection"
        ]),
        ("A second set, further on", [
            "desire, conceit,",
            "ignorance, restlessness"
        ]),
        ("A prediction, not a report", [
            "future tense",
            "throughout"
        ]),
    ],
    further=[
        '<a href="%s/thig6.7/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.6.html">Thig 6.6 &mdash; Mah&amacr;paj&amacr;pati '
        "Gotam&imacr;</a> &mdash; the poem immediately before this one.",
        '<a href="thig-2.1.html">Thig 2.1 &mdash; Abhir&umacr;panand&amacr;'
        "</a> &mdash; an earlier poem with a similar instruction-only "
        "structure.",
        '<a href="thig-6.8.html">Thig 6.8 &mdash; Vijay&amacr;</a> '
        "&mdash; the next poem, closing the Book of the Sixes.",
    ],
)


# --------------------------------------------------------------------------- #
# Thig 6.8 — Vijayā
# --------------------------------------------------------------------------- #
page(
    6, 8, "Vijay&amacr;", "Vijay&amacr;",
    meta_title="Thig 6.8 — Vijayā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vijayā's verses, closing the Book of the Sixes with this "
        "collection's fullest doctrinal instruction and a phrase "
        "repeated twice within one poem. From Ru-Yi Meditation Center."),
    vagga="The Book of the Sixes &middot; Poem 8 of 8",
    glance=[
        ("Setting", "No narrative setting beyond what the verses state; "
                    "no closing attribution"),
        ("Speaker", "The nun Vijayā, describing early failure, a "
                    "teacher's instruction, and a night's progress"),
        ("Form", "Six four-line verses, closing the Book of the Sixes"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the "
                       "most doctrinally complete instruction in this "
                       "collection so far"),
    ],
    why=(
        "This poem closes the Book of the Sixes by drawing together "
        "several threads from earlier in the collection: its opening "
        "confession repeats Thig 2.10's exactly, its teacher's "
        "instruction is the most complete doctrinal list given anywhere "
        "so far, and its account of a night's progress echoes the "
        "three watches of Thig 5.11's thirty nuns &mdash; closing with "
        "&lsquo;the mass of darkness shattered&rsquo; not once, but "
        "twice in a single poem."),
    guide=[
        ("An opening confession, repeated exactly", [
            "&lsquo;Four or five times I left my dwelling; I had failed "
            "to find peace of heart, or any control over my mind&rsquo; "
            "is identical to Thig 2.10's opening &mdash; the same "
            "confession, now given by a further woman closing this "
            "book."]),
        ("The fullest doctrinal instruction in the collection so far", [
            "&lsquo;The elements and sense fields, the four noble "
            "truths, the faculties and the powers, the awakening "
            "factors, and the eightfold path&rsquo; combines more named "
            "categories in a single teaching than any earlier "
            "instruction in this collection &mdash; a cumulative "
            "instruction, not a single compact phrase."]),
        ("Three watches, echoing the thirty nuns", [
            "&lsquo;In the first watch of the night, I recollected my "
            "past lives... in the last watch... I shattered the mass of "
            "darkness&rsquo; tracks the same three-watch structure that "
            "marked the group realization in Thig 5.11, here applied to "
            "one individual's single night."]),
        ("A phrase, shattered twice in one poem", [
            "&lsquo;The mass of darkness&rsquo; is shattered once in "
            "the third watch of the night, and again in the poem's very "
            "last line, &lsquo;on the seventh day I stretched out my "
            "feet, having shattered the mass of darkness&rsquo; &mdash; "
            "the only poem in this collection to use the phrase twice "
            "within itself."]),
    ],
    terms=[
        ("Vijay&amacr;",
         "this poem's speaker, whose account closes the Book of the "
         "Sixes."),
        ("dh&amacr;tu&amacr;yatan&amacr;ni",
         "&ldquo;the elements and sense fields&rdquo; &mdash; the first "
         "category in this poem's cumulative doctrinal instruction."),
        ("cattāri ariyasacc&amacr;ni",
         "the four noble truths, named as part of the same extended "
         "teaching."),
        ("bojjha&#7749;ga&#7789;&#7789;ha&#7749;gika magga",
         "&ldquo;the awakening factors, and the eightfold path&rdquo; "
         "&mdash; the final categories completing this poem's "
         "instruction."),
        ("tamokkhandha",
         "&ldquo;the mass of darkness&rdquo; &mdash; shattered twice "
         "within this single poem, unique among this collection's "
         "poems."),
    ],
    text_intro=(
        "The text in full: six verses, closing the Book of the Sixes. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thig6.8:1.1-1.4"),
        ("p", "&sect;2", "thig6.8:2.1-2.4"),
        ("p", "&sect;3", "thig6.8:3.1-3.4"),
        ("p", "&sect;4", "thig6.8:4.1-4.4"),
        ("p", "&sect;5", "thig6.8:5.1-5.4"),
        ("p", "&sect;6", "thig6.8:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does this poem's opening verse repeat exactly from Thig 2.10?",
         "opts": [
             "Nothing is shared",
             "The elephant simile",
             "The closing refuge formula",
             "'Four or five times I left my dwelling; I had failed to find peace of heart'"],
         "correct": 3,
         "expl": "The identical confession, now closing this book."},
        {"q": "How does this poem's teaching compare to earlier instructions in this collection?",
         "opts": [
             "It is identical to Thig 3.2's teaching",
             "It combines more named doctrinal categories than any earlier single instruction",
             "It contains no doctrinal content at all",
             "It is shorter than every earlier instruction"],
         "correct": 1,
         "expl": "Elements, sense fields, the four truths, faculties, powers, awakening factors, and the eightfold path together."},
        {"q": "What structure does this poem's account of a single night share with Thig 5.11?",
         "opts": [
             "No shared structure",
             "Both describe the same thirty nuns",
             "The same three-watch progression, here applied to one individual",
             "Neither poem describes a night at all"],
         "correct": 2,
         "expl": "Past lives, then clairvoyance, then the mass of darkness shattered, across three watches."},
        {"q": "How many times does 'the mass of darkness' get shattered within this single poem?",
         "opts": [
             "Once",
             "Three times",
             "It is not mentioned",
             "Twice"],
         "correct": 3,
         "expl": "In the third watch of the night, and again in the poem's closing line — unique among this collection's poems."},
        {"q": "How does this poem end, on the seventh day?",
         "opts": [
             "With a question left open",
             "By stretching out her feet, having shattered the mass of darkness",
             "With a dialogue with Māra",
             "With a return to lay life"],
         "correct": 1,
         "expl": "The phrase's second appearance within this same poem."},
        {"q": "What structural marker does bilara-data's underlying source place immediately after this poem?",
         "opts": [
             "No marker at all",
             "A note naming the next book's first poem",
             "'Chakkanipāto niṭṭhito' — 'the Book of the Sixes is finished'",
             "A repeat of the poem's own text"],
         "correct": 2,
         "expl": "The same kind of bibliographic close seen at the end of the Books of the Threes, Fours, and Fives."},
        {"q": "What does 'dhātuāyatanāni' mean?",
         "opts": [
             "'The elements and sense fields' — the first category named in this poem's instruction",
             "'The mass of darkness'",
             "'Four or five times'",
             "'The seventh day'"],
         "correct": 0,
         "expl": "Opening a cumulative list extending across several more categories."},
        {"q": "What position does this poem hold in the Book of the Sixes?",
         "opts": [
             "The eighth and last poem, closing the book",
             "The first poem",
             "The fourth poem",
             "It stands outside this book"],
         "correct": 0,
         "expl": "The final poem of eight in the Book of the Sixes."},
        {"q": "How does Vijayā first receive this poem's teaching?",
         "opts": [
             "In a dream",
             "From the Buddha directly",
             "By approaching a nun and politely questioning her",
             "The poem does not describe how she received it"],
         "correct": 2,
         "expl": "A specific, respectful approach to a trusted teacher."},
        {"q": "What does this poem's structure suggest about its place in the collection?",
         "opts": [
             "It introduces entirely new material unrelated to any earlier poem",
             "It draws together several earlier threads — an opening confession, a doctrinal instruction, and a three-watch structure — closing the book",
             "It has no connection to any other poem in this book",
             "It repeats Thig 6.1 exactly"],
         "correct": 1,
         "expl": "A closing poem that gathers rather than introduces."},
    ],
    marginalia=[
        ("A confession, repeated exactly", [
            "the same words",
            "as Thig 2.10"
        ]),
        ("The fullest instruction yet", [
            "seven categories,",
            "named together"
        ]),
        ("Three watches, for one this time", [
            "the same structure",
            "as the thirty nuns"
        ]),
        ("Shattered twice, in one poem", [
            "unique among",
            "this collection's poems"
        ]),
    ],
    further=[
        '<a href="%s/thig6.8/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thig-6.7.html">Thig 6.7 &mdash; Gutt&amacr;</a> '
        "&mdash; the poem immediately before this one.",
        '<a href="thig-2.10.html">Thig 2.10 &mdash; S&amacr;m&amacr;</a> '
        "&mdash; the poem this one's opening confession repeats "
        "exactly.",
        '<a href="./">Therigatha</a> &mdash; back to the collection '
        "index.",
    ],
)
