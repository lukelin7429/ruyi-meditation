# -*- coding: utf-8 -*-
"""Theragatha — Verses of the Senior Monks. Organized into books by the
number of verses attributed to each elder (Book of the Ones, Twos...)."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Theragatha — Verses of the Senior Monks"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Theragatha selections")
TAIL = ("./", "Theragatha selections")
INDEX_EXTRA = []

PAGES = []


def page(book, num, pali, title, **kw):
    """Shared scaffolding for a single elder's verses in the Theragatha.

    Like the Saṃyutta Nikāya, this collection spans several independently
    numbered books (Book of the Ones, Book of the Twos...), so both the book
    and the poem number are required. Unlike SN, bilara-data keeps every
    file flat (no per-book subfolder) -- see thag_build.py's load_source.
    """
    d = {
        "slug": "thag-%d.%d" % (book, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "thag%d.%d" % (book, num),
        "crumb": "Thag %d.%d" % (book, num),
        "number_line": "Theragatha &middot; %d.%d" % (book, num),
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# Thag 1.1 — Subh&umacr;ti
# --------------------------------------------------------------------------- #
page(
    1, 1, "Subh&umacr;ti", "Subh&umacr;ti",
    meta_title="Thag 1.1 — Subhūti | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Theragātha's opening poem, the collection's own frame "
        "verses followed by Subhūti's contented verse about his "
        "rain-proof hut. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; the collection's own "
                    "opening frame, then a single monk's verse about "
                    "his hut"),
        ("Speaker", "An unnamed narrator introducing the whole "
                    "collection, then Subhūti himself"),
        ("Form", "A four-verse frame for the entire collection, then "
                 "Subhūti's own four-line verse and its attribution"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "short, but carrying the whole collection's own "
                       "explanation of itself"),
    ],
    why=(
        "The Theragātha (&ldquo;Verses of the Senior Monks&rdquo;) "
        "opens not with a single monk's testimony but with the "
        "collection's own explanation of itself: an unnamed voice "
        "announces that the verses to follow were spoken by those "
        "&lsquo;who've practiced well&rsquo;, reviewing their "
        "completed task after reaching &lsquo;the state that does not "
        "pass&rsquo;. Only then does the first individual voice "
        "appear: Subhūti, content in a well-roofed hut safe from the "
        "rain, his mind serene and free."),
    guide=[
        ("A frame for the whole collection, not just this poem", [
            "This file uniquely carries the Theragātha's own "
            "four-verse preamble &mdash; a homage line, then three "
            "verses explaining what a Theragātha verse is and why it "
            "exists: to record a monk's name and clan, how he lived "
            "by the teaching, how dedicated he was, and that he "
            "reached the imperishable state, reviewing his completed "
            "task before speaking. Therīgātha's own opening poem "
            "assumes this same self-referential purpose without ever "
            "spelling it out this explicitly; here, the collection "
            "states it directly before a single individual has "
            "spoken."]),
        ("Subhūti, and a small joke at the rain god's expense", [
            "Subhūti's own verse, once the frame ends, is entirely "
            "domestic and content: his hut is &lsquo;roofed and "
            "pleasant, sheltered from the wind&rsquo;, so he invites "
            "the rain to fall as it pleases &mdash; a playful, "
            "unafraid address to the sky itself, paired with a "
            "straightforward statement that his mind is serene and "
            "freed."]),
        ("A recurring image across the whole collection", [
            "Sujato's note on this verse points out that invoking the "
            "rain-god from the safety of a hut is a small motif that "
            "&lsquo;recurs many times in the Theragātha&rsquo;, and "
            "surfaces elsewhere too, at Snp 1.2, in the context of "
            "household offerings to the gods &mdash; worth watching "
            "for as this book continues."]),
        ("A companion opener to the Therīgātha", [
            "Like Therīgātha's own first poem, this opens its "
            "collection. But where Thig 1.1 is an anonymous nun "
            "addressing herself, this poem names its speaker outright "
            "and gives him a specific, concrete, almost cozy "
            "circumstance &mdash; two different ways of beginning a "
            "book of enlightened verse."]),
    ],
    terms=[
        ("nid&amacr;nag&amacr;th&amacr;",
         "&ldquo;origin verses&rdquo; or &ldquo;background "
         "verses&rdquo; &mdash; the Pali label (rendered "
         "&ldquo;Background&rdquo; in translation) for this poem's "
         "opening frame, unique to this file in the whole "
         "collection."),
        ("accuta&#7745; pada&#7745;",
         "&ldquo;the imperishable state&rdquo; &mdash; what the frame "
         "verses say these monks &lsquo;touched&rsquo; before "
         "reviewing their completed task and speaking."),
        ("deva",
         "&ldquo;god&rdquo;, here the sky or rain deity Subhūti "
         "playfully invites to do as it pleases from the safety of "
         "his hut."),
        ("ku&#7789;ik&amacr;",
         "&ldquo;little hut&rdquo; &mdash; the central, concrete image "
         "of Subhūti's verse."),
        ("Therag&amacr;th&amacr;",
         "&ldquo;Verses of the Senior Monks&rdquo; &mdash; this "
         "collection's own title, paired with the Therīgātha as its "
         "companion collection."),
    ],
    text_intro=(
        "The text in full: the collection's own opening frame, then "
        "Subhūti's verse and its attribution. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.1:1.0.2-3.4"),
        ("p", "&sect;2", "thag1.1:4.1-4.5"),
    ],
    quiz=[
        {"q": "What does this poem's opening frame explain?",
         "opts": [
             "What a Theragātha verse is, and why these verses are recorded at all",
             "A rule about monastic robes",
             "The geography of ancient India",
             "Nothing — the poem has no frame"],
         "correct": 0,
         "expl": "The collection's own self-explanation, unique to this file."},
        {"q": "According to the frame, what had these monks done before speaking their verses?",
         "opts": [
             "Nothing in particular is said",
             "Traveled to a distant city",
             "Reached the imperishable state and reviewed their completed task",
             "Composed music"],
         "correct": 2,
         "expl": "The frame's own account of what qualifies a monk to speak."},
        {"q": "What is Subhūti's own verse mainly about?",
         "opts": [
             "A dispute with another monk",
             "A journey across a river",
             "His well-roofed hut, safe from the rain, and his freed mind",
             "A teaching on ethics"],
         "correct": 2,
         "expl": "A contented, domestic image rather than a dramatic account."},
        {"q": "How does Subhūti address the rain?",
         "opts": [
             "He invites it to fall as it pleases, unafraid",
             "He curses it",
             "He ignores it entirely",
             "He prays for it to stop"],
         "correct": 0,
         "expl": "A playful, confident address to the sky itself."},
        {"q": "According to Sujato's note, what does this rain-and-hut image do across the Theragātha?",
         "opts": [
             "It never appears again",
             "It is unique to this one poem only",
             "It is a later scribal addition",
             "It recurs many times across the collection"],
         "correct": 3,
         "expl": "A motif worth watching for as the book continues."},
        {"q": "Where else does Sujato's note say a similar idea about gods appears?",
         "opts": [
             "Nowhere else in the canon",
             "Only in a much later commentary",
             "At Snp 1.2, in the context of household offerings to the gods",
             "In a Chinese parallel text"],
         "correct": 2,
         "expl": "A cross-reference the note itself supplies."},
        {"q": "How does this poem's opening compare to Therīgātha's own opening poem?",
         "opts": [
             "They are word-for-word identical",
             "Neither poem names a speaker",
             "This poem is far longer than Thig 1.1",
             "Thig 1.1 is an anonymous nun addressing herself; this poem names its speaker and gives him a concrete circumstance"],
         "correct": 3,
         "expl": "Two different ways two companion collections choose to begin."},
        {"q": "What does Subhūti say about his mind in this verse?",
         "opts": [
             "That it is troubled",
             "That it is serene and freed",
             "Nothing is said about his mind",
             "That it is still in training"],
         "correct": 1,
         "expl": "Stated directly alongside the hut's physical shelter."},
        {"q": "What two things does the frame say a Theragātha verse should record about a monk?",
         "opts": [
             "Only his age and birthplace",
             "His name and clan, and how he lived by the teaching",
             "Only the date he ordained",
             "Nothing specific is listed"],
         "correct": 1,
         "expl": "Named explicitly in the frame's second verse."},
        {"q": "What closes Subhūti's verse?",
         "opts": [
             "A question left unanswered",
             "An attribution line naming him as the one who spoke it",
             "A warning to other monks",
             "A description of his birthplace"],
         "correct": 1,
         "expl": "The same closing attribution formula used across the collection."},
    ],
    marginalia=[
        ("The collection explains itself first", [
            "name, clan, practice,",
            "before a single verse"
        ]),
        ("A hut, and a joke at the sky", [
            "rain, heavens,",
            "as you please"
        ]),
        ("A motif to watch for", [
            "gods, rain, and huts,",
            "recurring across the book"
        ]),
        ("Two companion openings", [
            "an anonymous nun,",
            "a named, content monk"
        ]),
    ],
    further=[
        '<a href="%s/thag1.1/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../therigatha/thig-1.1.html">Thig 1.1 &mdash; An '
        "Unnamed Nun</a> &mdash; the Therīgātha's own opening poem, a "
        "companion collection.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.2 — Mah&amacr;ko&#7789;&#7789;hita
# --------------------------------------------------------------------------- #
page(
    1, 2, "Mah&amacr;ko&#7789;&#7789;hita", "Mah&amacr;ko&#7789;&#7789;hita",
    meta_title="Thag 1.2 — Mahākoṭṭhita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Mahākoṭṭhita's verse, a third-person portrait of a calm mind "
        "shedding bad qualities like leaves in a gale. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse with a "
                    "closing attribution"),
        ("Speaker", "An unnamed voice describing Mahākoṭṭhita in the "
                    "third person"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "four lines of description and a single simile"),
    ],
    why=(
        "Unlike Subhūti's first-person hut verse just before it, this "
        "poem describes Mahākoṭṭhita from the outside: calm, "
        "unrestless, thoughtful in counsel, shedding bad qualities the "
        "way a gale shakes leaves off a tree &mdash; a portrait rather "
        "than a declaration."),
    guide=[
        ("Third-person praise, not first-person declaration", [
            "Where Subhūti's verse spoke as &lsquo;my hut&rsquo; and "
            "&lsquo;my mind&rsquo;, this poem describes Mahākoṭṭhita "
            "entirely in the third person &mdash; &lsquo;he shakes off "
            "bad qualities&rsquo; &mdash; the first instance in this "
            "chapter of a verse praising its subject rather than "
            "letting him speak about himself directly."]),
        ("An image of natural, effortless shedding", [
            "The verse's single simile compares removing bad "
            "qualities to a gale shaking leaves off a tree &mdash; not "
            "a struggle or a battle, but something that happens "
            "naturally and thoroughly once the conditions (here, a "
            "calm and unrestless mind) are in place."]),
        ("Four qualities, front-loaded before the simile", [
            "The verse packs four descriptive qualities &mdash; calm, "
            "still, thoughtful in counsel, not restless &mdash; into "
            "its first three lines, saving the entire fourth line for "
            "the single image that ties them together."]),
    ],
    terms=[
        ("upasanto",
         "&ldquo;calm&rdquo; or &ldquo;peaceful&rdquo; &mdash; the "
         "first quality named in this verse."),
        ("uparato",
         "&ldquo;stilled&rdquo; or &ldquo;at rest&rdquo; &mdash; "
         "paired directly with upasanto to open the verse."),
        ("mantabh&amacr;&#7751;&imacr;",
         "&ldquo;thoughtful in speech&rdquo; or &ldquo;wise in "
         "counsel&rdquo; &mdash; describing how Mahākoṭṭhita speaks, "
         "not only how he sits."),
        ("anuddhato",
         "&ldquo;not restless&rdquo; or &ldquo;not agitated&rdquo; "
         "&mdash; completing the verse's four-part portrait."),
        ("dhun&amacr;ti",
         "&ldquo;shakes off&rdquo; &mdash; the verb behind this "
         "verse's central image, echoed in the simile of a gale "
         "shaking leaves from a tree."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.2:1.1-1.4"),
        ("p", "&sect;2", ["thag1.2:1.5"]),
    ],
    quiz=[
        {"q": "How does this poem describe Mahākoṭṭhita, compared to Subhūti's verse just before it?",
         "opts": [
             "In the third person, rather than Subhūti's first-person voice",
             "Also in the first person",
             "As a dialogue between two people",
             "The poem does not describe him at all"],
         "correct": 0,
         "expl": "A portrait rather than a self-declaration."},
        {"q": "What simile closes this verse?",
         "opts": [
             "A river cutting through stone",
             "A gale shaking leaves off a tree",
             "A lamp burning out",
             "A bird leaving its nest"],
         "correct": 1,
         "expl": "An image of natural, thorough removal."},
        {"q": "What does the simile describe Mahākoṭṭhita doing?",
         "opts": [
             "Building a shelter",
             "Teaching other monks",
             "Shaking off bad qualities",
             "Traveling to a new town"],
         "correct": 2,
         "expl": "The verse's central action, named directly before the simile."},
        {"q": "How many distinct qualities does the verse name before its closing simile?",
         "opts": [
             "None",
             "One",
             "Four",
             "Ten"],
         "correct": 2,
         "expl": "Calm, still, thoughtful in counsel, and not restless."},
        {"q": "Is Mahākoṭṭhita's struggle to remove bad qualities described as violent or effortful?",
         "opts": [
             "Yes, described as a long battle",
             "The verse does not address this",
             "Yes, described as painful",
             "No — the image is of something happening naturally, once conditions are right"],
         "correct": 3,
         "expl": "A gale shaking leaves, not a fight."},
        {"q": "What does 'anuddhato' describe in this verse?",
         "opts": [
             "A place",
             "Being not restless or not agitated",
             "A type of offering",
             "A monastic robe"],
         "correct": 1,
         "expl": "One of the verse's four opening qualities."},
        {"q": "What does the verse say about how Mahākoṭṭhita speaks?",
         "opts": [
             "That he never speaks",
             "That he speaks harshly",
             "That he is thoughtful in counsel",
             "Nothing about his speech"],
         "correct": 2,
         "expl": "Named directly among his four qualities."},
        {"q": "What closes this verse, as with other poems in this chapter?",
         "opts": [
             "A question",
             "An attribution line naming who spoke it",
             "A list of other monks",
             "A prophecy"],
         "correct": 1,
         "expl": "The same closing formula used across the collection."},
        {"q": "How long is this poem?",
         "opts": [
             "A single four-line verse plus its attribution",
             "Twenty verses",
             "It has no fixed length",
             "Two full chapters"],
         "correct": 0,
         "expl": "One of this chapter's shortest entries."},
        {"q": "Where does this poem fall in Chapter One of the Book of the Ones?",
         "opts": [
             "It is the chapter's last poem",
             "It is not part of this chapter",
             "Its position is unknown",
             "It is the second poem, right after Subhūti's"],
         "correct": 3,
         "expl": "Following directly on the collection's opening poem."},
    ],
    marginalia=[
        ("Praise from the outside", [
            "not 'my mind,'",
            "but 'he shakes off'"
        ]),
        ("A gale, not a battle", [
            "leaves fall",
            "when the wind is right"
        ]),
        ("Four qualities, one image", [
            "calm, still, thoughtful,",
            "unrestless"
        ]),
        ("A short poem, fully formed", [
            "four lines,",
            "one closing simile"
        ]),
    ],
    further=[
        '<a href="%s/thag1.2/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.1.html">Thag 1.1 &mdash; Subh&umacr;ti</a> '
        "&mdash; the poem immediately before this one, opening this "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.3 — Revata the Doubter
# --------------------------------------------------------------------------- #
page(
    1, 3, "Ka&#7749;kh&amacr;revata", "Revata the Doubter",
    meta_title="Thag 1.3 — Revata the Doubter | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Revata the Doubter's verse, praising the wisdom of the "
        "Realized Ones as a fire that dispels doubt like darkness. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse with a "
                    "closing attribution"),
        ("Speaker", "Revata the Doubter, praising the wisdom of the "
                    "Realized Ones in general terms"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "single fire simile, praising wisdom that "
                       "dispels doubt"),
    ],
    why=(
        "Revata's own epithet, &lsquo;the Doubter&rsquo;, carries the "
        "word kaṅkhā, &lsquo;doubt&rsquo;, built directly into his "
        "name &mdash; yet his one surviving verse is not about his own "
        "doubt at all. It praises the wisdom of the Realized Ones as a "
        "fire blazing in the night, giving light and vision, that "
        "&lsquo;dispels the doubt of those who've come&rsquo;."),
    guide=[
        ("A name built from doubt, a verse built from its opposite", [
            "&lsquo;Kaṅkhārevata&rsquo;, rendered here as &lsquo;Revata "
            "the Doubter&rsquo;, carries kaṅkhā (&lsquo;doubt&rsquo;) "
            "directly in his name. His verse never mentions his own "
            "doubt; instead, it describes exactly the wisdom capable "
            "of dispelling it in others &mdash; a quiet resonance "
            "between a name and the content of the one verse attached "
            "to it."]),
        ("Fire, light, and vision as a single image", [
            "The verse's simile is entirely visual: wisdom is a fire "
            "blazing in the night, and its effect is described in two "
            "matched phrases, &lsquo;giving light, giving vision"
            "&rsquo; &mdash; not just illumination in the abstract, "
            "but the specific gift of being able to see."]),
        ("Praise pitched at the plural, not the personal", [
            "Where Mahākoṭṭhita's verse just before this one described "
            "one man, this verse speaks of &lsquo;the Realized "
            "Ones&rsquo; as a class and of &lsquo;those who dispel the "
            "doubt of those who've come&rsquo; in the plural &mdash; "
            "general praise of wisdom itself, rather than an account "
            "of any one person's experience of receiving it."]),
    ],
    terms=[
        ("ka&#7749;kh&amacr;",
         "&ldquo;doubt&rdquo; &mdash; built into Revata's own epithet, "
         "though absent from the content of his verse itself."),
        ("Tath&amacr;gata",
         "&ldquo;Realized One&rdquo;, an epithet for the Buddha (and, "
         "here, by extension those who share his realization) &mdash; "
         "whose wisdom this verse praises."),
        ("&amacr;loka",
         "&ldquo;light&rdquo; &mdash; the first of two effects this "
         "verse credits to that wisdom."),
        ("cakkhu",
         "&ldquo;eye&rdquo; or &ldquo;vision&rdquo; &mdash; the second "
         "effect, paired directly with light in the same line."),
        ("vinayanti",
         "&ldquo;they dispel&rdquo; or &ldquo;they remove&rdquo; "
         "&mdash; sharing a root with Vinaya, the monastic code, "
         "though used here simply to mean the removal of doubt."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.3:1.1-1.4"),
        ("p", "&sect;2", ["thag1.3:1.5"]),
    ],
    quiz=[
        {"q": "What does the word 'kaṅkhā', built into Revata's own name, mean?",
         "opts": [
             "Fire",
             "Doubt",
             "Wisdom",
             "Night"],
         "correct": 1,
         "expl": "The very word his epithet, 'the Doubter', is built from."},
        {"q": "Does Revata's verse describe his own doubt directly?",
         "opts": [
             "Yes, at length",
             "Only briefly, in the second line",
             "Yes, it is the verse's main subject",
             "No — it describes the wisdom that dispels doubt in general"],
         "correct": 3,
         "expl": "A quiet resonance rather than a direct personal account."},
        {"q": "What simile does the verse use for the wisdom of the Realized Ones?",
         "opts": [
             "A fire blazing in the night",
             "A river in flood",
             "A mountain peak",
             "A closed door"],
         "correct": 0,
         "expl": "Central image of the verse's second line."},
        {"q": "What two effects does this fire-wisdom give, according to the verse?",
         "opts": [
             "Warmth and safety",
             "Food and shelter",
             "Light and vision",
             "Silence and stillness"],
         "correct": 2,
         "expl": "Named in a matched pair in the verse's third line."},
        {"q": "Whose doubt does this wisdom dispel, according to the verse?",
         "opts": [
             "Only Revata's own doubt",
             "The doubt of those who've come",
             "No one's — the verse says doubt cannot be dispelled",
             "Only the doubt of other monks specifically named"],
         "correct": 1,
         "expl": "Framed generally, not as a single personal episode."},
        {"q": "Is this verse addressed to one person's experience, or framed more generally?",
         "opts": [
             "One specific person's experience only",
             "It is addressed to no one",
             "Framed generally, praising the Realized Ones' wisdom as a class",
             "It names a specific date and place"],
         "correct": 2,
         "expl": "Plural praise, not a personal narrative."},
        {"q": "What does 'Tathāgata' mean, as used in this verse?",
         "opts": [
             "A type of hut",
             "'Realized One', an epithet for the Buddha and those who share his realization",
             "A geographic region",
             "A musical instrument"],
         "correct": 1,
         "expl": "The subject whose wisdom the verse praises."},
        {"q": "What root does 'vinayanti' ('they dispel') share with a familiar Buddhist term?",
         "opts": [
             "It shares no roots with any other term",
             "Dhamma",
             "Sangha",
             "Vinaya, the monastic code"],
         "correct": 3,
         "expl": "A shared root, though used here for dispelling doubt rather than for monastic rules."},
        {"q": "How is Revata's verse similar to Mahākoṭṭhita's verse just before it?",
         "opts": [
             "Both are addressed directly to the Buddha",
             "They are identical in content",
             "Neither uses any simile",
             "Both describe their subject from outside, rather than in the first person"],
         "correct": 3,
         "expl": "Both poems in this chapter praise rather than declare."},
        {"q": "What closes this verse?",
         "opts": [
             "An attribution line naming Revata the Doubter as its speaker",
             "A question left open",
             "A list of other monks",
             "A prophecy about the future"],
         "correct": 0,
         "expl": "The same closing formula used across the collection."},
    ],
    marginalia=[
        ("A name built from doubt", [
            "kaṅkhā,",
            "absent from his own verse"
        ]),
        ("Fire in the night", [
            "giving light,",
            "giving vision"
        ]),
        ("Whose doubt is dispelled", [
            "not his own —",
            "'those who've come'"
        ]),
        ("A shared root, a different use", [
            "vinayanti,",
            "not the monastic code"
        ]),
    ],
    further=[
        '<a href="%s/thag1.3/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.2.html">Thag 1.2 &mdash; Mah&amacr;'
        "ko&#7789;&#7789;hita</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.4 — Pu&#7751;&#7751;a (1st)
# --------------------------------------------------------------------------- #
page(
    1, 4, "Pu&#7751;&#7751;a", "Pu&#7751;&#7751;a (1st)",
    meta_title="Thag 1.4 — Puṇṇa (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Puṇṇa's verse of practical advice, urging companionship with "
        "the virtuous as the path to a goal &lsquo;great and "
        "profound&rsquo;. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse of general "
                    "advice, with a closing attribution"),
        ("Speaker", "Puṇṇa, giving advice in the imperative rather "
                    "than describing himself"),
        ("Form", "One six-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "direct advice, then four stacked descriptions "
                       "of a single goal"),
    ],
    why=(
        "Unlike the poems just before it, Puṇṇa's verse is neither a "
        "self-declaration nor third-person praise, but direct advice: "
        "&lsquo;associate only with the virtuous&rsquo;. What follows "
        "describes the goal such companionship leads to in four "
        "stacked terms &mdash; great, profound, hard to see, subtle "
        "&mdash; before the diligent and clear-seeing wise are said to "
        "reach it."),
    guide=[
        ("Advice, not description or declaration", [
            "Where the previous three poems in this chapter described "
            "a hut, a calm mind, or wisdom's effect, this verse opens "
            "with a direct imperative: &lsquo;associate only with the "
            "virtuous, the astute ones who see the goal&rsquo; &mdash; "
            "practical instruction rather than a portrait or a "
            "confession."]),
        ("A goal described four ways before it is reached", [
            "Before saying anyone attains it, the verse piles up four "
            "descriptions of the goal itself: &lsquo;great and "
            "profound&rsquo;, &lsquo;hard to see&rsquo;, &lsquo;"
            "subtle&rsquo;, and &lsquo;fine&rsquo; &mdash; only then "
            "does it say the wise, diligent and clear-seeing, reach "
            "it."]),
        ("A named identity, per Sujato's note", [
            "Sujato's note identifies this Puṇṇa as the monk famous "
            "for his conversation with Sāriputta recorded at MN 24 "
            "&mdash; one of very few poems in this opening chapter "
            "whose speaker is cross-referenced to a specific text "
            "elsewhere in the canon."]),
    ],
    terms=[
        ("sabbhi",
         "&ldquo;with the good&rdquo; or &ldquo;with the "
         "virtuous&rdquo; &mdash; the companionship this verse opens "
         "by recommending."),
        ("pa&#7751;&#7693;ita",
         "&ldquo;wise&rdquo; or &ldquo;astute&rdquo; &mdash; describing "
         "those worth associating with, and later those who reach the "
         "goal."),
        ("attha",
         "&ldquo;goal&rdquo; or &ldquo;meaning&rdquo; &mdash; the "
         "object described in four stacked terms across this verse's "
         "middle lines."),
        ("appamatta",
         "&ldquo;diligent&rdquo; or &ldquo;heedful&rdquo; &mdash; one "
         "of two qualities, alongside clear sight, credited with "
         "reaching that goal."),
        ("vicakkha&#7751;a",
         "&ldquo;clear-seeing&rdquo; or &ldquo;discerning&rdquo; "
         "&mdash; paired with diligence in the verse's closing line."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.4:1.1-1.6"),
        ("p", "&sect;2", ["thag1.4:1.7"]),
    ],
    quiz=[
        {"q": "How does this verse open?",
         "opts": [
             "With a description of a hut",
             "With direct advice: associate only with the virtuous",
             "With a question addressed to the Buddha",
             "With a list of monks' names"],
         "correct": 1,
         "expl": "Practical instruction, not description or declaration."},
        {"q": "How many descriptive terms does the verse stack up for the goal, before saying anyone reaches it?",
         "opts": [
             "None",
             "Two",
             "Four",
             "Ten"],
         "correct": 2,
         "expl": "Great, profound, hard to see, and subtle."},
        {"q": "According to the verse, who reaches this goal?",
         "opts": [
             "Anyone at all, without condition",
             "Only kings",
             "The wise, diligent and clear-seeing",
             "No one — the verse says it cannot be reached"],
         "correct": 2,
         "expl": "Named directly in the verse's closing lines."},
        {"q": "According to Sujato's note, what is this particular Puṇṇa famous for?",
         "opts": [
             "Nothing further is noted",
             "A conversation with Sāriputta recorded at MN 24",
             "Building the first monastery",
             "A dispute over Vinaya rules"],
         "correct": 1,
         "expl": "A cross-reference to another canonical text."},
        {"q": "What does 'sabbhi' mean in this verse's opening line?",
         "opts": [
             "A type of offering",
             "A place name",
             "A monastic robe",
             "With the good, or with the virtuous"],
         "correct": 3,
         "expl": "The companionship this verse recommends from its first word."},
        {"q": "How does this verse's form compare to the three poems just before it?",
         "opts": [
             "It is advice, rather than self-declaration or third-person praise",
             "It is identical in form to all three",
             "It is much longer than any other poem in the whole collection",
             "It contains no verbs at all"],
         "correct": 0,
         "expl": "A third distinct register within this chapter's first four poems."},
        {"q": "What two qualities does the verse credit with reaching the goal?",
         "opts": [
             "Wealth and status",
             "Youth and strength",
             "Diligence and clear sight",
             "Silence and solitude"],
         "correct": 2,
         "expl": "Named together in the verse's closing line."},
        {"q": "Is the goal in this verse described as easy or difficult to perceive?",
         "opts": [
             "Easy — obvious to anyone",
             "Difficult — hard to see and subtle",
             "The verse does not describe its difficulty",
             "Impossible to perceive under any condition"],
         "correct": 1,
         "expl": "Two of the four stacked descriptive terms."},
        {"q": "What closes this verse?",
         "opts": [
             "An attribution line naming Puṇṇa, son of Mantāṇī, as its speaker",
             "A question left open",
             "A warning to other monks",
             "A description of a river"],
         "correct": 0,
         "expl": "The same closing formula used across the collection."},
        {"q": "How long is this verse compared to most others in this chapter?",
         "opts": [
             "Shorter than average",
             "Exactly the same length as every other poem here",
             "Length cannot be compared across poems",
             "Six lines, slightly longer than this chapter's typical four-line verses"],
         "correct": 3,
         "expl": "One of the chapter's slightly longer entries."},
    ],
    marginalia=[
        ("Advice, not confession", [
            "'associate only",
            "with the virtuous'"
        ]),
        ("A goal, described four times over", [
            "great, profound,",
            "hard to see, subtle"
        ]),
        ("A name cross-referenced elsewhere", [
            "famous for a dialogue",
            "with Sāriputta"
        ]),
        ("Two qualities, one attainment", [
            "diligence",
            "and clear sight"
        ]),
    ],
    further=[
        '<a href="%s/thag1.4/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.3.html">Thag 1.3 &mdash; Revata the '
        "Doubter</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.5 — Dabba
# --------------------------------------------------------------------------- #
page(
    1, 5, "Dabba", "Dabba",
    meta_title="Thag 1.5 — Dabba | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Dabba's verse, a before-and-after portrait of taming, naming "
        "him twice within his own four lines. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse with a "
                    "closing attribution"),
        ("Speaker", "An unnamed voice describing Dabba, naming him "
                    "twice within the verse itself"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "compact before-and-after portrait, stacking "
                       "several attainment epithets"),
    ],
    why=(
        "This verse opens with compression: &lsquo;once hard to tame, "
        "now tamed himself&rsquo; packs an entire transformation into "
        "a single line, before piling on further epithets &mdash; "
        "content, doubt overcome, victorious, fears vanished, "
        "steadfast &mdash; naming Dabba by name twice within his own "
        "four lines."),
    guide=[
        ("A name spoken inside its own verse, not only in the attribution", [
            "Unlike Mahākoṭṭhita's or Revata's verses, which name "
            "their subject only in the closing attribution line, this "
            "verse says &lsquo;Dabba&rsquo; twice within its own four "
            "lines &mdash; once mid-verse, once at the close &mdash; "
            "making his identity part of the verse's own content, not "
            "just its editorial frame."]),
        ("A whole transformation compressed into one line", [
            "&lsquo;Once hard to tame, now tamed himself&rsquo; states "
            "an entire before-and-after arc in four words each side "
            "&mdash; no narrative detail about how the taming "
            "happened, only the fact of the change itself."]),
        ("Synonyms stacked for a single attainment", [
            "The verse's remaining lines pile up near-synonymous "
            "descriptions of the same state &mdash; content, doubt "
            "overcome, victorious, fears vanished, steadfast, fully "
            "quenched &mdash; a formulaic accumulation rather than a "
            "single fresh image, typical of several short verses in "
            "this opening chapter."]),
    ],
    terms=[
        ("duddamiya",
         "&ldquo;hard to tame&rdquo; &mdash; describing Dabba's state "
         "before, in the verse's very first word."),
        ("danta",
         "&ldquo;tamed&rdquo; &mdash; the direct contrast completing "
         "the verse's opening before-and-after line."),
        ("viti&#7751;&#7751;aka&#7749;kha",
         "&ldquo;doubt crossed over&rdquo; or &ldquo;doubt "
         "overcome&rdquo; &mdash; one of several near-synonymous "
         "attainment terms stacked in this verse."),
        ("vijit&amacr;v&imacr;",
         "&ldquo;victorious&rdquo; &mdash; describing Dabba once his "
         "fears have vanished."),
        ("parinibbuta",
         "&ldquo;fully quenched&rdquo; or &ldquo;fully "
         "extinguished&rdquo; &mdash; the verse's final and strongest "
         "term, closing its list of attainment epithets."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.5:1.1-1.4"),
        ("p", "&sect;2", ["thag1.5:1.5"]),
    ],
    quiz=[
        {"q": "How many times is Dabba named within his own four-line verse?",
         "opts": [
             "Twice",
             "Never — only in the attribution line",
             "Four times",
             "Once"],
         "correct": 0,
         "expl": "Once mid-verse, once at the close."},
        {"q": "What does the verse's opening line describe?",
         "opts": [
             "A journey to a distant city",
             "A dispute over teachings",
             "A before-and-after change: once hard to tame, now tamed himself",
             "A description of his birthplace"],
         "correct": 2,
         "expl": "An entire transformation compressed into one line."},
        {"q": "Does the verse explain how Dabba's taming happened?",
         "opts": [
             "Yes, in great narrative detail",
             "No — only the fact of the change is stated",
             "Yes, through a long dialogue",
             "The verse says the taming never happened"],
         "correct": 1,
         "expl": "Compression, not narrative detail."},
        {"q": "What is the verse's final and strongest attainment term?",
         "opts": [
             "Content",
             "Victorious",
             "Doubt overcome",
             "Fully quenched (parinibbuta)"],
         "correct": 3,
         "expl": "The closing word of the verse's stacked epithets."},
        {"q": "How does this verse's naming pattern differ from Mahākoṭṭhita's or Revata's verses earlier in this chapter?",
         "opts": [
             "It names its subject only in the closing attribution, like those poems",
             "It never names its subject at all",
             "It names its subject twice within the verse itself, not only in the attribution",
             "There is no difference"],
         "correct": 2,
         "expl": "Identity built into the verse's own content here."},
        {"q": "What does 'vitiṇṇakaṅkha' mean?",
         "opts": [
             "A type of hut",
             "Doubt crossed over, or doubt overcome",
             "A monastic robe",
             "A geographic region"],
         "correct": 1,
         "expl": "One of the stacked attainment terms in this verse."},
        {"q": "What single word opens this verse?",
         "opts": [
             "Danto ('tamed')",
             "Santusito ('content')",
             "Duddamiyo ('hard to tame')",
             "Vijitāvī ('victorious')"],
         "correct": 2,
         "expl": "The verse's opening word, describing Dabba's earlier state."},
        {"q": "What kind of poem is this, in terms of its structure?",
         "opts": [
             "A narrative with named characters and dialogue",
             "A formulaic accumulation of near-synonymous attainment epithets",
             "A question-and-answer exchange",
             "A description of a specific place"],
         "correct": 1,
         "expl": "Typical of several short verses in this opening chapter."},
        {"q": "Is Dabba described as still fearful in this verse?",
         "opts": [
             "Yes, still deeply fearful",
             "The verse does not mention fear",
             "Only partially fearful",
             "No — his fears are said to have vanished"],
         "correct": 3,
         "expl": "Named directly before the verse calls him victorious."},
        {"q": "What closes this verse?",
         "opts": [
             "An attribution line naming Dabba as its speaker",
             "A question left open",
             "A prophecy",
             "A list of other monks"],
         "correct": 0,
         "expl": "The same closing formula used across the collection."},
    ],
    marginalia=[
        ("Named twice, inside the verse itself", [
            "not just the",
            "closing attribution"
        ]),
        ("A whole change, in four words", [
            "once hard to tame,",
            "now tamed himself"
        ]),
        ("Synonyms, stacked", [
            "content, victorious,",
            "fully quenched"
        ]),
        ("No story, only the fact of it", [
            "how it happened",
            "goes unsaid"
        ]),
    ],
    further=[
        '<a href="%s/thag1.5/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.4.html">Thag 1.4 &mdash; Pu&#7751;&#7751;a '
        "(1st)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.6 — S&imacr;tavaniya
# --------------------------------------------------------------------------- #
page(
    1, 6, "S&imacr;tavaniya", "S&imacr;tavaniya",
    meta_title="Thag 1.6 — Sītavaniya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sītavaniya's verse, a monk named for the Cool Grove he went "
        "to practice in, guarding mindfulness of the body. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 6 of 10",
    glance=[
        ("Setting", "The Cool Grove, a place-name built directly into "
                    "this monk's own name"),
        ("Speaker", "An unnamed voice describing Sītavaniya"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "compact portrait naming one specific practice "
                       "directly"),
    ],
    why=(
        "Sītavaniya's very name records where he practiced: "
        "&lsquo;Sītavaniya&rsquo; means &lsquo;of the Cool "
        "Grove&rsquo;, and his one verse opens by naming that same "
        "place. Unlike the epithet-stacked verses around it, this poem "
        "names one specific practice directly &mdash; guarding "
        "mindfulness of the body."),
    guide=[
        ("A name that is also a place", [
            "&lsquo;Sītavaniya&rsquo; is formed directly from "
            "&lsquo;Sītavana&rsquo;, the Cool Grove &mdash; a "
            "charnel-ground-adjacent forest used by early monks for "
            "solitary practice. His verse opens by naming this same "
            "place, so that his identity and his practice site are "
            "recorded in the very same word."]),
        ("One named practice, not only stacked epithets", [
            "Where several verses in this chapter accumulate general "
            "attainment terms &mdash; content, victorious, steadfast "
            "&mdash; this one names a specific practice directly: "
            "&lsquo;guarding mindfulness of the body&rsquo;, the first "
            "poem in this chapter to identify what, exactly, its "
            "subject was doing."]),
        ("An idiom for fear overcome, not a literal claim", [
            "&lsquo;Goosebumps vanished&rsquo; translates an idiom for "
            "fear itself &mdash; hair standing on end being the "
            "physical marker of terror &mdash; so the phrase describes "
            "fearlessness achieved, not a literal physical detail."]),
    ],
    terms=[
        ("S&imacr;tavana",
         "the &ldquo;Cool Grove&rdquo;, a forest site used for "
         "solitary practice &mdash; the place-name built directly "
         "into this monk's own name."),
        ("eka",
         "&ldquo;alone&rdquo; or &ldquo;solitary&rdquo; &mdash; "
         "describing how Sītavaniya practiced at that grove."),
        ("santusita",
         "&ldquo;content&rdquo; &mdash; an epithet recurring across "
         "several verses in this chapter."),
        ("k&amacr;yagat&amacr;sati",
         "&ldquo;mindfulness of the body&rdquo; &mdash; the one "
         "specific practice this verse names directly, unlike its "
         "neighbors' more general epithets."),
        ("apetalomaha&#7745;sa",
         "&ldquo;goosebumps vanished&rdquo;, literally &ldquo;hair "
         "standing departed&rdquo; &mdash; an idiom for fear "
         "overcome, not a literal physical description."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.6:1.1-1.4"),
        ("p", "&sect;2", ["thag1.6:1.5"]),
    ],
    quiz=[
        {"q": "What does the name 'Sītavaniya' mean?",
         "opts": [
             "Of the Cool Grove, the place he went to practice",
             "Fully quenched",
             "Doubt overcome",
             "Victorious"],
         "correct": 0,
         "expl": "A name built directly from the place his verse names."},
        {"q": "What specific practice does this verse name directly?",
         "opts": [
             "Chanting scripture",
             "Guarding mindfulness of the body",
             "Teaching new monks",
             "Fasting"],
         "correct": 1,
         "expl": "The first poem in this chapter to name a specific practice."},
        {"q": "How does this verse differ from several others in this chapter?",
         "opts": [
             "It names one specific practice, rather than only stacking general epithets",
             "It is written entirely in the first person",
             "It contains no attribution line",
             "It is much longer than any other poem here"],
         "correct": 0,
         "expl": "A concrete practice, not only a list of attainment terms."},
        {"q": "What does 'goosebumps vanished' describe, according to this guide?",
         "opts": [
             "A literal physical detail",
             "A weather condition",
             "A type of clothing",
             "An idiom for fear overcome"],
         "correct": 3,
         "expl": "Hair standing on end as the physical marker of fear, now gone."},
        {"q": "What kind of place is the Cool Grove associated with?",
         "opts": [
             "A royal palace",
             "A charnel-ground-adjacent forest used for solitary practice",
             "A busy marketplace",
             "A river crossing"],
         "correct": 1,
         "expl": "The setting built into Sītavaniya's own name."},
        {"q": "Is Sītavaniya described as practicing alone or with company?",
         "opts": [
             "With a large group",
             "With one companion",
             "Alone, described as solitary",
             "The verse does not say"],
         "correct": 2,
         "expl": "Named directly in the verse's opening lines."},
        {"q": "What does 'santusita' mean?",
         "opts": [
             "Restless",
             "Content",
             "Fearful",
             "Wealthy"],
         "correct": 1,
         "expl": "One of the epithets shared with several other poems in this chapter."},
        {"q": "What connects Sītavaniya's identity and his practice site especially closely?",
         "opts": [
             "Nothing connects them",
             "They are unrelated topics in the verse",
             "His own name is built from the name of the place",
             "The verse never mentions a location"],
         "correct": 2,
         "expl": "Name and place recorded in the very same word."},
        {"q": "What closes this verse?",
         "opts": [
             "A question left open",
             "A description of a battle",
             "A list of other monks",
             "An attribution line naming Sītavaniya as its speaker"],
         "correct": 3,
         "expl": "The same closing formula used across the collection."},
        {"q": "How many lines does this verse have, not counting its attribution?",
         "opts": [
             "Two",
             "Six",
             "Four",
             "Eight"],
         "correct": 2,
         "expl": "The standard length for most poems in this chapter."},
    ],
    marginalia=[
        ("A name built from a place", [
            "Sītavaniya,",
            "of the Cool Grove"
        ]),
        ("One named practice", [
            "guarding mindfulness",
            "of the body"
        ]),
        ("An idiom, not a literal claim", [
            "goosebumps vanished —",
            "fear overcome"
        ]),
        ("Solitary, by name and by practice", [
            "alone,",
            "content and serene"
        ]),
    ],
    further=[
        '<a href="%s/thag1.6/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.5.html">Thag 1.5 &mdash; Dabba</a> &mdash; '
        "the poem immediately before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.7 — Bhalliya
# --------------------------------------------------------------------------- #
page(
    1, 7, "Bhalliya", "Bhalliya",
    meta_title="Thag 1.7 — Bhalliya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Bhalliya's verse, casting aside the army of the King of "
        "Death like a flood sweeping away a fragile reed bridge. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse with a "
                    "closing attribution"),
        ("Speaker", "An unnamed voice describing Bhalliya; his own "
                    "name never appears within the verse itself"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "striking new opening image, paired with lines "
                       "shared word for word with an earlier poem"),
    ],
    why=(
        "This verse opens with the chapter's first martial image: "
        "casting aside the army of the King of Death as easily as a "
        "great flood sweeps away a fragile bridge of reeds. Its second "
        "half then echoes Dabba's verse (Thag 1.5) almost word for "
        "word &mdash; except that where Dabba named himself twice, "
        "this verse never once says &lsquo;Bhalliya&rsquo;."),
    guide=[
        ("A new image: an army cast aside, a bridge swept away", [
            "Where this chapter's verses so far have used domestic or "
            "natural images &mdash; a hut, a gale, a fire, a taming "
            "&mdash; this one opens with something closer to warfare: "
            "the army of the King of Death, cast aside as easily as a "
            "flood sweeps away a bridge built from fragile reeds."]),
        ("Two lines shared word for word with Dabba's verse", [
            "This verse's closing two lines &mdash; &lsquo;victorious "
            "since his fears have vanished&rsquo;, &lsquo;fully "
            "quenched, steadfast&rsquo; &mdash; match Dabba's verse "
            "(Thag 1.5) almost exactly in the Pali, sharing the same "
            "formulaic phrase apetabheravo, &lsquo;fear "
            "departed&rsquo;, that Dabba's verse also used."]),
        ("Unlike Dabba, never naming himself inside the verse", [
            "Dabba's verse says &lsquo;Dabba&rsquo; twice within its "
            "own four lines. This verse's closing line instead says "
            "only &lsquo;tame and steadfast&rsquo; &mdash; a generic "
            "description standing where Dabba's own name once stood "
            "&mdash; so Bhalliya's identity appears only in the "
            "external attribution, not inside the verse itself."]),
    ],
    terms=[
        ("maccur&amacr;ja",
         "the &ldquo;King of Death&rdquo;, an epithet for Māra "
         "&mdash; whose army this verse says has been cast aside."),
        ("sen&amacr;",
         "&ldquo;army&rdquo; &mdash; the martial image opening this "
         "verse, unlike anything used so far in this chapter."),
        ("na&#7735;asetu",
         "&ldquo;a bridge of reeds&rdquo; &mdash; the fragile object "
         "in this verse's central simile."),
        ("mahogha",
         "&ldquo;a great flood&rdquo; &mdash; the force said to sweep "
         "that reed bridge away."),
        ("apetabheravo",
         "&ldquo;fear departed&rdquo; &mdash; a phrase shared word "
         "for word with Dabba's verse (Thag 1.5)."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.7:1.1-1.4"),
        ("p", "&sect;2", ["thag1.7:1.5"]),
    ],
    quiz=[
        {"q": "What image opens this verse?",
         "opts": [
             "A description of a hut",
             "Casting aside the army of the King of Death, like a flood sweeping away a reed bridge",
             "A conversation between two monks",
             "A journey by boat"],
         "correct": 1,
         "expl": "The chapter's first martial image."},
        {"q": "How do this verse's closing two lines compare to Dabba's verse (Thag 1.5)?",
         "opts": [
             "They share no wording at all",
             "They are about a completely different topic",
             "They match almost word for word in the Pali",
             "Dabba's verse quotes this one, not the reverse"],
         "correct": 2,
         "expl": "A shared formulaic phrase, apetabheravo, 'fear departed'."},
        {"q": "Does Bhalliya's own name appear within the verse itself?",
         "opts": [
             "Twice, like Dabba's verse",
             "Three times",
             "Once, in the opening line",
             "No — it appears only in the external attribution line"],
         "correct": 3,
         "expl": "A generic description stands where a name might have gone instead."},
        {"q": "What is described as fragile in this verse's simile?",
         "opts": [
             "A hut roof",
             "A mountain path",
             "A bridge of reeds",
             "A clay pot"],
         "correct": 2,
         "expl": "Swept away by a great flood in the same line."},
        {"q": "What does 'maccurāja' mean?",
         "opts": [
             "A type of offering",
             "The King of Death, an epithet for Māra",
             "A monastic title",
             "A river name"],
         "correct": 1,
         "expl": "Whose army this verse says has been cast aside."},
        {"q": "How does this verse's opening image compare to the images used earlier in this chapter?",
         "opts": [
             "It is the first martial image, unlike the hut, gale, or fire images before it",
             "It repeats the exact same image as Subhūti's hut verse",
             "It is identical to every other opening in this chapter",
             "This chapter never uses any images at all"],
         "correct": 0,
         "expl": "A shift in register from domestic and natural images to warfare."},
        {"q": "What force is said to sweep the reed bridge away?",
         "opts": [
             "A great flood",
             "A strong wind",
             "An earthquake",
             "A fire"],
         "correct": 0,
         "expl": "Named directly in the verse's second line."},
        {"q": "What word replaces Bhalliya's own name in this verse's closing line?",
         "opts": [
             "A place name",
             "A generic description: 'tame and steadfast'",
             "The Buddha's name",
             "No word replaces it — the line is left blank"],
         "correct": 1,
         "expl": "Contrasting with Dabba's verse, which names Dabba directly instead."},
        {"q": "What closes this verse?",
         "opts": [
             "A question left open",
             "A list of other monks",
             "A prophecy",
             "An attribution line naming Bhalliya as its speaker"],
         "correct": 3,
         "expl": "The same closing formula used across the collection."},
        {"q": "Where does this poem fall in Chapter One?",
         "opts": [
             "It is the seventh poem, following Sītavaniya's",
             "It is the chapter's opening poem",
             "It is not part of this chapter",
             "It is the chapter's final poem"],
         "correct": 0,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("An army, cast aside", [
            "like a flood",
            "sweeping a reed bridge"
        ]),
        ("Two lines, borrowed almost whole", [
            "shared word for word",
            "with Dabba's verse"
        ]),
        ("A name withheld from its own verse", [
            "'tame and steadfast,'",
            "not 'Bhalliya'"
        ]),
        ("A shift from hut to battlefield", [
            "this chapter's first",
            "martial image"
        ]),
    ],
    further=[
        '<a href="%s/thag1.7/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.6.html">Thag 1.6 &mdash; S&imacr;tavaniya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.8 — V&imacr;ra
# --------------------------------------------------------------------------- #
page(
    1, 8, "V&imacr;ra", "V&imacr;ra",
    meta_title="Thag 1.8 — Vīra | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vīra's verse, a name meaning &lsquo;hero&rsquo; used twice "
        "over, and a verse built from the same template as Dabba's. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse with a "
                    "closing attribution"),
        ("Speaker", "An unnamed voice describing Vīra, using his own "
                    "name twice within the verse"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "wordplay on a name, built from a template "
                       "shared with an earlier poem"),
    ],
    why=(
        "&lsquo;Vīra&rsquo; is itself the Pali word for &lsquo;"
        "hero&rsquo;, and this verse uses that very word twice: once "
        "as a plain description (&lsquo;a hero, content&rsquo;), once "
        "as his proper name (&lsquo;Vīra is steadfast&rsquo;). The "
        "verse's opening line, meanwhile, matches Dabba's (Thag 1.5) "
        "word for word."),
    guide=[
        ("A name that is also its own epithet", [
            "&lsquo;Vīra&rsquo; simply means &lsquo;hero&rsquo; or "
            "&lsquo;brave one&rsquo;. The Pali uses the single word "
            "vīro twice in four lines &mdash; once functioning as a "
            "plain descriptive epithet (&lsquo;a hero, content, with "
            "doubt overcome&rsquo;), once as his proper name (&lsquo;"
            "Vīra is steadfast&rsquo;) &mdash; the same wordplay "
            "technique the Therīgātha uses for Muttā, whose own name "
            "means &lsquo;released&rsquo;."]),
        ("The same opening line as Dabba's verse, almost exactly", [
            "&lsquo;Once hard to tame, now tamed himself&rsquo; opens "
            "this verse in wording identical to Dabba's (Thag 1.5). "
            "The third line then substitutes &lsquo;goosebumps "
            "vanished&rsquo; for Dabba's &lsquo;fear departed&rsquo; "
            "&mdash; the same idiom Sītavaniya's verse (Thag 1.6) also "
            "used."]),
        ("A formulaic bank, mixed and matched across four poems", [
            "By this point in the chapter, a pattern is visible: Thag "
            "1.5, 1.6, 1.7, and 1.8 all draw from a shared bank of "
            "closing phrases &mdash; victorious, fear or goosebumps "
            "vanished, fully quenched, steadfast &mdash; recombined "
            "with different opening images and different degrees of "
            "self-naming, rather than each being composed as an "
            "entirely fresh, unrelated verse."]),
        ("Named twice, like Dabba, unlike Bhalliya", [
            "Where Bhalliya's verse just before this one never once "
            "said his own name, this verse returns to Dabba's pattern "
            "&mdash; naming Vīra twice within his own four lines, once "
            "mid-verse and once at the close."]),
    ],
    terms=[
        ("v&imacr;ra",
         "&ldquo;hero&rdquo; or &ldquo;brave one&rdquo; &mdash; both "
         "this monk's proper name and, used a second time in the same "
         "verse, a plain descriptive epithet."),
        ("duddamiya",
         "&ldquo;hard to tame&rdquo; &mdash; the verse's opening "
         "word, identical to Dabba's verse (Thag 1.5)."),
        ("apetalomaha&#7745;sa",
         "&ldquo;goosebumps vanished&rdquo; &mdash; the idiom for fear "
         "overcome shared with Sītavaniya's verse (Thag 1.6)."),
        ("vijit&amacr;v&imacr;",
         "&ldquo;victorious&rdquo; &mdash; one of this chapter's most "
         "frequently recurring attainment terms."),
        ("parinibbuta",
         "&ldquo;fully quenched&rdquo; &mdash; the closing epithet "
         "shared across several poems in this chapter's formulaic "
         "bank."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.8:1.1-1.4"),
        ("p", "&sect;2", ["thag1.8:1.5"]),
    ],
    quiz=[
        {"q": "What does the name 'Vīra' mean?",
         "opts": [
             "River",
             "Hero, or brave one",
             "Grove",
             "Doubt"],
         "correct": 1,
         "expl": "The same word this verse uses twice, once as name and once as epithet."},
        {"q": "How many times does the word 'vīro' appear in this four-line verse?",
         "opts": [
             "Never",
             "Once",
             "Twice — once as a plain epithet, once as his proper name",
             "Four times"],
         "correct": 2,
         "expl": "A double function for the same word."},
        {"q": "How does this verse's opening line compare to Dabba's verse (Thag 1.5)?",
         "opts": [
             "It is completely different in wording",
             "It uses the opposite meaning",
             "It is identical: 'once hard to tame, now tamed himself'",
             "Dabba's verse has no opening line to compare"],
         "correct": 2,
         "expl": "The chapter's second use of this exact opening."},
        {"q": "What idiom does this verse's third line share with Sītavaniya's verse (Thag 1.6)?",
         "opts": [
             "'Goosebumps vanished', for fear overcome",
             "'Fear departed', a different phrase entirely",
             "No idiom is shared between the two",
             "A phrase about rivers"],
         "correct": 0,
         "expl": "The same idiom-family used slightly differently across this chapter."},
        {"q": "What pattern becomes visible across Thag 1.5 through 1.8, according to this guide?",
         "opts": [
             "Each poem is entirely unrelated to the others",
             "A shared bank of closing phrases, recombined with different opening images",
             "All four poems are identical in every line",
             "No pattern is discernible"],
         "correct": 1,
         "expl": "A glimpse of formulaic, oral-composition technique."},
        {"q": "How does this verse's use of Vīra's own name compare to Bhalliya's verse (Thag 1.7)?",
         "opts": [
             "Both verses avoid naming their subject entirely",
             "Both verses name their subject exactly once",
             "This verse names Vīra twice; Bhalliya's verse never names Bhalliya at all",
             "There is no difference between the two"],
         "correct": 2,
         "expl": "A return to Dabba's pattern of internal self-naming."},
        {"q": "What Therīgātha poem uses a similar wordplay on its subject's own name?",
         "opts": [
             "Thig 15.1, Isidāsī",
             "Thig 16.1, Sumedhā",
             "No Therīgātha poem uses this technique",
             "Thig 1.2, Muttā, whose name means 'released'"],
         "correct": 3,
         "expl": "A cross-reference to the companion collection's own name-based verse."},
        {"q": "What does 'vijitāvī' mean?",
         "opts": [
             "Steadfast",
             "Content",
             "A place name",
             "Victorious"],
         "correct": 3,
         "expl": "One of the chapter's most frequently recurring attainment terms."},
        {"q": "What closes this verse?",
         "opts": [
             "A prophecy",
             "A question left unanswered",
             "A list of other monks",
             "An attribution line naming Vīra as its speaker"],
         "correct": 3,
         "expl": "The same closing formula used across the collection."},
        {"q": "Where does this poem fall within Chapter One?",
         "opts": [
             "The eighth poem, following Bhalliya's",
             "The chapter's opening poem",
             "It is not part of this chapter",
             "The chapter's final poem"],
         "correct": 0,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A name used twice over", [
            "vīro — 'hero,'",
            "vīro — his own name"
        ]),
        ("The same opening as Dabba's verse", [
            "hard to tame,",
            "now tamed himself"
        ]),
        ("Four poems, one formulaic bank", [
            "closing phrases,",
            "recombined each time"
        ]),
        ("Named twice, like Dabba", [
            "not withheld,",
            "as Bhalliya's was"
        ]),
    ],
    further=[
        '<a href="%s/thag1.8/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.7.html">Thag 1.7 &mdash; Bhalliya</a> &mdash; '
        "the poem immediately before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.9 — Pilindavaccha
# --------------------------------------------------------------------------- #
page(
    1, 9, "Pilindavaccha", "Pilindavaccha",
    meta_title="Thag 1.9 — Pilindavaccha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Pilindavaccha's verse, a first-person statement of gratitude "
        "for good advice and having arrived at the best of "
        "well-explained teachings. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting; a short first-person verse "
                    "with a closing attribution"),
        ("Speaker", "Pilindavaccha, speaking about his own experience "
                    "of receiving good advice"),
        ("Form", "One four-line verse, with a closing attribution "
                 "note"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "understated gratitude, without a single "
                       "simile"),
    ],
    why=(
        "After a run of third-person portraits built from stacked "
        "epithets, this verse returns to the first person: "
        "Pilindavaccha states simply that the advice he received was "
        "welcome and good, and that among well-explained teachings, "
        "he arrived at the best &mdash; gratitude for guidance, not an "
        "enumeration of attainment."),
    guide=[
        ("A return to the first person", [
            "Since Subhūti's opening hut verse, most poems in this "
            "chapter have described their subject from outside. This "
            "verse returns to &lsquo;I&rsquo; &mdash; &lsquo;the "
            "advice I got was good&rsquo;, &lsquo;I arrived at the "
            "best&rsquo; &mdash; the chapter's second first-person "
            "statement."]),
        ("A double negative, stated plainly", [
            "The verse opens by saying the advice was &lsquo;welcome, "
            "not unwelcome&rsquo; &mdash; stating the same idea twice, "
            "once positively and once by denying its opposite, before "
            "adding a third confirmation: &lsquo;the advice I got was "
            "good&rsquo;."]),
        ("Gratitude for teaching, not a list of attainments", [
            "Unlike the neighboring verses' stacked epithets for "
            "personal attainment &mdash; content, victorious, "
            "steadfast &mdash; this verse's subject is entirely "
            "external: the quality of the teaching Pilindavaccha "
            "received, and his own good fortune in receiving it."]),
    ],
    terms=[
        ("sv&amacr;gata&#7745;",
         "&ldquo;welcome&rdquo; &mdash; the verse's opening word, "
         "describing the advice Pilindavaccha received."),
        ("dur&amacr;gata&#7745;",
         "&ldquo;unwelcome&rdquo; &mdash; negated in the same line as "
         "sv&amacr;gataṁ, stating the same idea twice over."),
        ("dumantita&#7745;",
         "&ldquo;badly advised&rdquo; &mdash; also negated, a third "
         "confirmation that the advice he received was good."),
        ("sa&#7745;vibhattesu",
         "&ldquo;well-analyzed&rdquo; or &ldquo;well-classified&rdquo; "
         "&mdash; describing the teachings among which he found the "
         "best."),
        ("se&#7789;&#7789;ha&#7745;",
         "&ldquo;the best&rdquo; &mdash; what Pilindavaccha says he "
         "arrived at, closing the verse."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.9:1.1-1.4"),
        ("p", "&sect;2", ["thag1.9:1.5"]),
    ],
    quiz=[
        {"q": "In what voice is this verse written?",
         "opts": [
             "Third person, describing Pilindavaccha from outside",
             "First person, Pilindavaccha speaking about his own experience",
             "Second person, addressed directly to Pilindavaccha",
             "A dialogue between two speakers"],
         "correct": 1,
         "expl": "The chapter's second first-person statement."},
        {"q": "How does the verse describe the advice Pilindavaccha received?",
         "opts": [
             "As harsh but necessary",
             "As unwelcome at first",
             "Nothing is said about the advice",
             "As welcome, not unwelcome, and good"],
         "correct": 3,
         "expl": "Stated three ways: positively, then twice by denying its opposite."},
        {"q": "What structure does the verse's opening line use?",
         "opts": [
             "A simile comparing advice to fire",
             "A direct question",
             "A list of names",
             "A double negative, stating the same idea positively and by denying its opposite"],
         "correct": 3,
         "expl": "'Welcome, not unwelcome' — the same claim made twice over."},
        {"q": "What does Pilindavaccha say he arrived at, among well-explained teachings?",
         "opts": [
             "The best",
             "Only a small part",
             "Nothing in particular",
             "The most difficult"],
         "correct": 0,
         "expl": "The verse's closing claim."},
        {"q": "How does this verse's subject matter differ from several verses just before it?",
         "opts": [
             "It is about the quality of teaching received, not a list of personal attainments",
             "It is about a journey to a distant city",
             "It is identical in subject matter to all the others",
             "It describes a dispute between monks"],
         "correct": 0,
         "expl": "Gratitude for guidance, not an enumeration of epithets."},
        {"q": "Does this verse use a simile, like Mahākoṭṭhita's gale-and-leaves or Bhalliya's flood-and-bridge?",
         "opts": [
             "Yes, a simile comparing teaching to fire",
             "No — it states its claims plainly, without a simile",
             "Yes, a simile comparing teaching to a river",
             "Yes, several similes in sequence"],
         "correct": 1,
         "expl": "A more understated, direct register than some neighboring verses."},
        {"q": "What does 'saṁvibhattesu' describe?",
         "opts": [
             "A place name",
             "A type of hut",
             "Teachings that are well-analyzed or well-classified",
             "A monastic rule"],
         "correct": 2,
         "expl": "Describing the teachings among which Pilindavaccha found the best."},
        {"q": "How many distinct ways does the verse confirm that Pilindavaccha's advice was good?",
         "opts": [
             "None — the verse never says the advice was good",
             "Only one",
             "Three: welcome, not unwelcome, and not badly advised",
             "Ten"],
         "correct": 2,
         "expl": "A threefold confirmation packed into two lines."},
        {"q": "What closes this verse?",
         "opts": [
             "A prophecy",
             "An attribution line naming Pilindavaccha as its speaker",
             "A question left open",
             "A description of a battle"],
         "correct": 1,
         "expl": "The same closing formula used across the collection."},
        {"q": "Where does this poem fall within Chapter One?",
         "opts": [
             "The ninth poem, following Vīra's",
             "The chapter's opening poem",
             "It is not part of this chapter",
             "The chapter's final poem"],
         "correct": 0,
         "expl": "Second to last in the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A return to 'I'", [
            "after several",
            "third-person portraits"
        ]),
        ("The same claim, three times over", [
            "welcome, not unwelcome,",
            "not badly advised"
        ]),
        ("Gratitude, not attainment", [
            "praise for teaching,",
            "not a list of epithets"
        ]),
        ("No simile at all", [
            "just a plain,",
            "direct claim"
        ]),
    ],
    further=[
        '<a href="%s/thag1.9/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.8.html">Thag 1.8 &mdash; V&imacr;ra</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.10 — Pu&#7751;&#7751;am&amacr;sa (1st)
# --------------------------------------------------------------------------- #
page(
    1, 10, "Pu&#7751;&#7751;am&amacr;sa", "Pu&#7751;&#7751;am&amacr;sa (1st)",
    meta_title="Thag 1.10 — Puṇṇamāsa (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Puṇṇamāsa's verse, closing Chapter One with a knowledge "
        "master unsullied amid all things, plus the chapter's own "
        "untranslated colophon. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter One &middot; Poem 10 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse closing "
                    "Chapter One, with a closing attribution"),
        ("Speaker", "An unnamed voice describing Puṇṇamāsa"),
        ("Form", "One four-line verse and its attribution, followed "
                 "in the Pali by an untranslated chapter colophon and "
                 "mnemonic summary verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "compact closing portrait, plus a chapter's own "
                       "structural close"),
    ],
    why=(
        "Puṇṇamāsa's verse closes Chapter One with a knowledge master "
        "&mdash; rid of concern for this world and the next, unsullied "
        "amid all things, knowing the arising and passing of the "
        "world. In the Pali text itself, this poem's attribution is "
        "followed by two structural elements Sujato left untranslated: "
        "a line marking &lsquo;the first chapter is finished&rsquo;, "
        "and a six-line mnemonic verse naming all ten monks of this "
        "chapter in sequence."),
    guide=[
        ("A knowledge master, unsullied amid all things", [
            "The verse itself describes someone rid of concern for "
            "&lsquo;this world and the world beyond&rsquo;, "
            "&lsquo;unsullied in the midst of all things&rsquo;, who "
            "knows &lsquo;the arising and passing of the world&rsquo; "
            "&mdash; a description pitched at a wider scope than most "
            "of this chapter's more compact epithet-verses, closing on "
            "cosmic terms rather than a single image or a personal "
            "confession."]),
        ("A chapter's own closing line, left untranslated", [
            "Immediately after this poem's attribution, the Pali text "
            "carries the phrase vaggo paṭhamo, &lsquo;the first "
            "chapter is finished&rsquo; &mdash; a structural colophon "
            "Sujato's translation leaves untranslated, the same way "
            "Therīgātha's own closing colophon was left untranslated "
            "at the end of Thig 16.1."]),
        ("A mnemonic verse naming all ten monks, also untranslated", [
            "After that chapter colophon, the Pali carries an "
            "uddāna &mdash; a six-line tabulation verse naming, in "
            "order, all ten monks whose verses make up this chapter: "
            "Subhūti, Koṭṭhika, Revata, Mantānīputta, Dabba, "
            "Sītavaniya, Bhalliya, Vīra, Pilindavaccha, and "
            "Puṇṇamāsa. This memorization aid, too, is absent from "
            "Sujato's translation, and does not appear as part of "
            "this page's text below."]),
        ("A chapter's arc, briefly reviewed", [
            "Chapter One opened with the collection's own "
            "self-explanation and Subhūti's contented hut, moved "
            "through a run of third-person portraits drawing on an "
            "increasingly visible shared bank of formulaic phrases, "
            "returned briefly to the first person with Pilindavaccha, "
            "and closes here with a wider, more cosmic description "
            "&mdash; ten poems, and eleven more chapters still to come "
            "in the Book of the Ones alone."]),
    ],
    terms=[
        ("vedag&umacr;",
         "&ldquo;knowledge master&rdquo; &mdash; the epithet opening "
         "this verse."),
        ("an&umacr;palitta",
         "&ldquo;unsullied&rdquo; &mdash; describing this knowledge "
         "master's state amid all things."),
        ("udayabbaya",
         "&ldquo;arising and passing&rdquo; &mdash; a standard pair "
         "of terms for impermanence, named directly in this verse's "
         "closing line."),
        ("udd&amacr;na",
         "a &ldquo;tabulation&rdquo; or mnemonic summary verse, "
         "appearing at the end of this chapter in the Pali but absent "
         "from Sujato's translation, naming all ten of its monks in "
         "sequence."),
        ("vaggo",
         "&ldquo;chapter&rdquo; &mdash; the structural unit this poem "
         "closes, marked in the untranslated Pali colophon &lsquo;"
         "vaggo pa&#7789;hamo&rsquo;, &lsquo;the first chapter is "
         "finished&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with its closing attribution. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.10:1.1-1.4"),
        ("p", "&sect;2", ["thag1.10:1.5"]),
    ],
    quiz=[
        {"q": "What does this verse call Puṇṇamāsa?",
         "opts": [
             "A knowledge master",
             "A king",
             "A merchant",
             "A gatekeeper"],
         "correct": 0,
         "expl": "The verse's opening epithet."},
        {"q": "What is Puṇṇamāsa said to be rid of concern for?",
         "opts": [
             "Only his own health",
             "This world and the world beyond",
             "Nothing — concern is not mentioned",
             "Only his family"],
         "correct": 1,
         "expl": "Named directly in the verse's second line."},
        {"q": "What Pali phrase, left untranslated by Sujato, immediately follows this poem's attribution?",
         "opts": [
             "A love poem",
             "A list of monastic rules",
             "Vaggo paṭhamo, 'the first chapter is finished'",
             "A prophecy about a future Buddha"],
         "correct": 2,
         "expl": "A structural colophon marking the end of Chapter One."},
        {"q": "What does the untranslated uddāna after that colophon do?",
         "opts": [
             "Nothing — the text simply ends",
             "Introduces a brand new eleventh poem",
             "Repeats Puṇṇamāsa's verse a second time",
             "Names all ten monks of this chapter, in order, as a memorization aid"],
         "correct": 3,
         "expl": "A traditional tabulation verse, absent from the translation and from this page's text."},
        {"q": "How does this verse's scope compare to several more compact epithet-verses earlier in the chapter?",
         "opts": [
             "It is identical in scope to all of them",
             "It is much shorter than any other verse here",
             "It closes on wider, more cosmic terms — the arising and passing of the world",
             "It describes only a single physical object"],
         "correct": 2,
         "expl": "A broader closing note for the chapter's final poem."},
        {"q": "What does 'udayabbaya' mean?",
         "opts": [
             "Arising and passing",
             "Hut and shelter",
             "Doubt and certainty",
             "Victory and defeat"],
         "correct": 0,
         "expl": "A standard pair of terms for impermanence."},
        {"q": "How many monks' verses make up Chapter One in total?",
         "opts": [
             "Five",
             "Ten",
             "Twenty",
             "One hundred and twenty"],
         "correct": 1,
         "expl": "Subhūti through Puṇṇamāsa, named in sequence in the untranslated uddāna."},
        {"q": "Where else in this reading guide's series does a similar untranslated closing colophon appear?",
         "opts": [
             "Nowhere else",
             "At the end of Thig 16.1, closing the Therīgātha",
             "At the start of every single poem",
             "Only in the Cariyapitaka"],
         "correct": 1,
         "expl": "The same pattern of an untranslated structural colophon."},
        {"q": "Does this page's text include the uddāna naming all ten monks?",
         "opts": [
             "Yes, translated in full",
             "Yes, but only partially",
             "No — it is absent from Sujato's translation and not included here",
             "It is included as an image only"],
         "correct": 2,
         "expl": "Consistent with how this site handles untranslated structural material."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the only chapter",
             "Exactly one more",
             "The number is unknown",
             "Eleven more chapters"],
         "correct": 3,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
    ],
    marginalia=[
        ("A wider, more cosmic close", [
            "the arising",
            "and passing of the world"
        ]),
        ("A chapter ends, untranslated", [
            "'vaggo paṭhamo' —",
            "left out of the translation"
        ]),
        ("Ten names, tabulated", [
            "an uddāna,",
            "also untranslated"
        ]),
        ("One chapter of twelve", [
            "ten poems down,",
            "eleven more to come"
        ]),
    ],
    further=[
        '<a href="%s/thag1.10/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.9.html">Thag 1.9 &mdash; Pilindavaccha</a> '
        "&mdash; the poem immediately before this one, closing "
        "Chapter One.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)
