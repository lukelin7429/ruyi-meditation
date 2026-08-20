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


# --------------------------------------------------------------------------- #
# Thag 1.11 — C&umacr;&lstrok;avaccha
# --------------------------------------------------------------------------- #
page(
    1, 11, "C&umacr;&#7735;avaccha", "C&umacr;&#7735;avaccha",
    meta_title="Thag 1.11 — Cūḷavaccha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Cūḷavaccha's verse, opening Chapter Two with joy in the "
        "teaching leading to the blissful stilling of conditions. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse opening "
                    "Chapter Two"),
        ("Speaker", "An unnamed voice describing a monk full of joy "
                    "in the teaching"),
        ("Form", "One four-line verse, without a closing attribution "
                 "line"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "short statement connecting joy to peace"),
    ],
    why=(
        "Chapter Two opens with joy: a monk full of joy in the "
        "teaching, the verse says, will realize the peaceful state, "
        "&lsquo;the blissful stilling of conditions&rsquo;. This "
        "chapter also opens a new pattern &mdash; unlike every poem in "
        "Chapter One, this verse carries no closing attribution "
        "sentence at all."),
    guide=[
        ("Joy as the cause, peace as the result", [
            "The verse's logic runs in one direction: a monk "
            "&lsquo;full of joy&rsquo; in the Buddha's teaching is the "
            "one who &lsquo;would realize the peaceful state&rsquo; "
            "&mdash; joy positioned as a condition for peace, not "
            "something peace produces afterward."]),
        ("A new pattern: no closing attribution line", [
            "Every poem in Chapter One closed with a full sentence "
            "naming its speaker: &lsquo;that is how this verse was "
            "recited by the senior venerable X&rsquo;. In the Pali "
            "text, Chapter Two abbreviates this same formula down to "
            "an ellipsis (&lsquo;&hellip; Cūḷavaccho thero &hellip;"
            "&rsquo;), trusting the reader to fill in what Chapter One "
            "already established &mdash; and Sujato's translation "
            "simply omits it, so this and the following poems in this "
            "chapter end right after their verse."]),
        ("Sharing a clan name with the poem just after it", [
            "&lsquo;Cūḷavaccha&rsquo; means roughly &lsquo;junior "
            "Vaccha&rsquo;. The very next poem in this chapter belongs "
            "to Mahāvaccha, &lsquo;senior Vaccha&rsquo; &mdash; two "
            "monks sharing the clan name Vaccha, placed as this "
            "chapter's first two poems, distinguished only by the "
            "junior/senior prefix."]),
    ],
    terms=[
        ("p&amacr;mojja",
         "&ldquo;joy&rdquo; or &ldquo;gladness&rdquo; &mdash; the "
         "verse's opening quality, positioned as leading toward peace."),
        ("padaṁ santaṁ",
         "&ldquo;the peaceful state&rdquo; &mdash; what a joyful monk "
         "is said to realize."),
        ("sa&#7749;kh&amacr;r&umacr;pasama",
         "&ldquo;the stilling of conditions&rdquo; &mdash; a term for "
         "nibbāna describing it as the quieting of all conditioned "
         "processes."),
        ("thera",
         "&ldquo;senior&rdquo; or &ldquo;elder&rdquo; &mdash; the "
         "title (as in Theragātha itself) that Chapter One's "
         "attribution lines always used, before Chapter Two abbreviates "
         "it away."),
        ("Vaccha",
         "a clan name shared by at least three monks in this chapter "
         "&mdash; Cūḷavaccha, Mahāvaccha, and Vanavaccha &mdash; "
         "distinguished from one another by an added qualifier."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.11:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse say a monk full of joy in the teaching would realize?",
         "opts": [
             "Nothing in particular",
             "Great wealth",
             "The peaceful state, the blissful stilling of conditions",
             "A new teaching of his own"],
         "correct": 2,
         "expl": "The verse's central claim, opening Chapter Two."},
        {"q": "How does this verse's logic connect joy and peace?",
         "opts": [
             "Peace comes first, joy follows",
             "Joy is positioned as a condition leading to peace",
             "The two are described as opposites",
             "No connection is drawn between them"],
         "correct": 1,
         "expl": "Joy named as the cause, not the result."},
        {"q": "How does this poem's ending differ from every poem in Chapter One?",
         "opts": [
             "It has no attribution line, unlike Chapter One's poems",
             "It is much longer",
             "It ends with a question",
             "There is no difference"],
         "correct": 0,
         "expl": "A new chapter-wide pattern begins here."},
        {"q": "What happened to the attribution formula in the Pali text for this chapter?",
         "opts": [
             "It was deleted entirely from the Pali",
             "It was expanded to twice its original length",
             "It was moved to the start of the poem instead",
             "It is abbreviated to an ellipsis, trusting the reader to recall it from Chapter One"],
         "correct": 3,
         "expl": "A standard abbreviation convention, left untranslated here."},
        {"q": "What does 'Cūḷavaccha' mean, roughly?",
         "opts": [
             "Great river",
             "Junior Vaccha",
             "Golden hut",
             "Forest wanderer"],
         "correct": 1,
         "expl": "Distinguishing him from Mahāvaccha, 'senior Vaccha', in the very next poem."},
        {"q": "How many monks in this chapter share the clan name Vaccha?",
         "opts": [
             "Just one",
             "None",
             "At least three: Cūḷavaccha, Mahāvaccha, and Vanavaccha",
             "All ten monks in this chapter"],
         "correct": 2,
         "expl": "Each distinguished by an added qualifier."},
        {"q": "What does 'saṅkhārūpasama' describe?",
         "opts": [
             "A type of hut",
             "A monastic robe",
             "A river crossing",
             "The stilling of conditions, a term for nibbāna"],
         "correct": 3,
         "expl": "The verse's closing description of the peaceful state."},
        {"q": "What title does 'thera' name, used throughout Chapter One's attribution lines?",
         "opts": [
             "King",
             "Senior or elder",
             "Merchant",
             "Farmer"],
         "correct": 1,
         "expl": "The same title giving the whole collection, Theragātha, its name."},
        {"q": "How long is this verse?",
         "opts": [
             "One four-line verse, without a closing attribution",
             "Twenty verses",
             "Six lines plus an attribution",
             "Two lines only"],
         "correct": 0,
         "expl": "The chapter's new, shorter standard form."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "It opens Chapter Two, the Book of the Ones' second chapter",
             "It closes the entire collection",
             "It is not part of the Book of the Ones",
             "It opens Chapter One"],
         "correct": 0,
         "expl": "The first of ten poems in this new chapter."},
    ],
    marginalia=[
        ("Joy first, then peace", [
            "joy in the teaching,",
            "leading to stillness"
        ]),
        ("A formula, now abbreviated", [
            "no closing line —",
            "just the verse itself"
        ]),
        ("Two Vacchas, side by side", [
            "junior and senior,",
            "sharing one clan name"
        ]),
        ("A new chapter begins", [
            "ten more poems,",
            "a shorter closing form"
        ]),
    ],
    further=[
        '<a href="%s/thag1.11/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.10.html">Thag 1.10 &mdash; Pu&#7751;&#7751;'
        "am&amacr;sa (1st)</a> &mdash; the poem immediately before "
        "this one, closing Chapter One.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.12 — Mah&amacr;vaccha
# --------------------------------------------------------------------------- #
page(
    1, 12, "Mah&amacr;vaccha", "Mah&amacr;vaccha",
    meta_title="Thag 1.12 — Mahāvaccha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Mahāvaccha's verse, a compact checklist of qualities for "
        "awaiting one's time free of desire. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse with no "
                    "closing attribution"),
        ("Speaker", "An unnamed voice describing Mahāvaccha, or "
                    "instructing in general terms"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "compact checklist of qualities"),
    ],
    why=(
        "Mahāvaccha's verse reads as a checklist: empowered by wisdom, "
        "precepts and observances intact, serene, absorbed, mindful, "
        "eating only what is needed &mdash; and on that basis, "
        "&lsquo;await one's time here, free of desire&rsquo;, a "
        "striking way to describe simply waiting for death."),
    guide=[
        ("A senior counterpart to the chapter's opening poem", [
            "&lsquo;Mahāvaccha&rsquo; means &lsquo;senior "
            "Vaccha&rsquo;, following directly on Cūḷavaccha, "
            "&lsquo;junior Vaccha&rsquo;. Where Cūḷavaccha's verse "
            "named a single cause (joy) and a single result (peace), "
            "this verse lists five or six qualities together without "
            "singling any one out as primary."]),
        ("Waiting for death described as a practice", [
            "The verse's closing instruction, &lsquo;await one's time "
            "here, free of desire&rsquo;, treats the interval before "
            "death itself as something to be lived a certain way "
            "&mdash; not urgency to escape the body, but an ongoing "
            "discipline of eating only what is needed and remaining "
            "without craving."]),
        ("Wisdom paired with ethical intactness, not opposed to it", [
            "The verse opens by pairing &lsquo;empowered by "
            "wisdom&rsquo; directly with &lsquo;precepts and "
            "observances intact&rsquo; in the same line &mdash; wisdom "
            "and ethical conduct presented as running together, not "
            "as separate or competing concerns."]),
    ],
    terms=[
        ("pa&ntilde;&ntilde;&amacr;bal&imacr;",
         "&ldquo;empowered by wisdom&rdquo; &mdash; the verse's "
         "opening quality."),
        ("s&imacr;lavat&umacr;papanno",
         "&ldquo;endowed with precepts and observances&rdquo; "
         "&mdash; paired directly with wisdom in the verse's first "
         "line."),
        ("jh&amacr;narato",
         "&ldquo;loving absorption&rdquo; or &ldquo;delighting in "
         "meditative absorption&rdquo; &mdash; one of the verse's "
         "middle qualities."),
        ("v&imacr;tar&amacr;go",
         "&ldquo;free of desire&rdquo; &mdash; the state in which "
         "this verse says one should await one's time."),
        ("kāla&#7745;",
         "&ldquo;one's time&rdquo;, here meaning the time of "
         "death &mdash; the object of the verse's closing "
         "instruction, kaṅkhetha kālaṁ, &lsquo;await your time&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.12:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does 'Mahāvaccha' mean, following on Cūḷavaccha's verse just before it?",
         "opts": [
             "Great river",
             "Senior Vaccha",
             "Golden hut",
             "Northern wanderer"],
         "correct": 1,
         "expl": "Senior to Cūḷavaccha's 'junior Vaccha' in the poem right before this one."},
        {"q": "How does this verse's structure compare to Cūḷavaccha's verse just before it?",
         "opts": [
             "This verse lists five or six qualities together, rather than naming one cause and one result",
             "Both verses are identical in structure",
             "This verse names no qualities at all",
             "This verse is written as a question"],
         "correct": 0,
         "expl": "A checklist rather than a single cause-and-effect claim."},
        {"q": "What does the verse's closing instruction, 'await one's time here, free of desire', describe?",
         "opts": [
             "Building a new monastery",
             "A pilgrimage to a distant site",
             "A specific meditation retreat schedule",
             "Waiting for death as an ongoing discipline, not an urgent escape"],
         "correct": 3,
         "expl": "Death treated as something to be lived toward a certain way, not merely awaited passively."},
        {"q": "How does the verse relate wisdom and ethical conduct?",
         "opts": [
             "It says wisdom makes ethical conduct unnecessary",
             "It never mentions ethical conduct",
             "It pairs them directly in its opening line, as running together",
             "It presents them as opposed to each other"],
         "correct": 2,
         "expl": "Named side by side, not in competition."},
        {"q": "What does this verse say about eating?",
         "opts": [
             "That one should fast entirely",
             "That eating is irrelevant to practice",
             "That one should eat only at night",
             "That one should eat only what is needed"],
         "correct": 3,
         "expl": "One of the qualities named among the verse's checklist."},
        {"q": "What does 'vītarāgo' mean?",
         "opts": [
             "Full of desire",
             "Wealthy",
             "Free of desire",
             "Fearful"],
         "correct": 2,
         "expl": "The state in which this verse says one should await one's time."},
        {"q": "What does 'jhānarato' describe?",
         "opts": [
             "Delighting in meditative absorption",
             "A type of robe",
             "A geographic region",
             "A meal schedule"],
         "correct": 0,
         "expl": "One of several qualities named in this verse's checklist."},
        {"q": "Does this verse's closing instruction describe urgency to escape the body?",
         "opts": [
             "Yes, urgent escape is the main theme",
             "No — it describes an ongoing, unhurried discipline instead",
             "The verse does not address this at all",
             "Yes, but only in its final word"],
         "correct": 1,
         "expl": "Waiting itself framed as the practice, not something to rush past."},
        {"q": "How many qualities does this verse's checklist name in total?",
         "opts": [
             "Five or six, named together across four lines",
             "Just one",
             "Exactly two",
             "None — it names no specific qualities"],
         "correct": 0,
         "expl": "Wisdom, precepts, calm, absorption, mindfulness, and moderate eating."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It closes the chapter",
             "The second poem, right after Cūḷavaccha's",
             "It is not part of this chapter",
             "It opens the chapter"],
         "correct": 1,
         "expl": "Following directly on the chapter's first poem."},
    ],
    marginalia=[
        ("A senior counterpart", [
            "Mahāvaccha,",
            "following Cūḷavaccha"
        ]),
        ("Qualities, listed together", [
            "wisdom, precepts,",
            "calm, mindfulness"
        ]),
        ("Waiting, as a discipline", [
            "free of desire,",
            "not urgent escape"
        ]),
        ("Wisdom and ethics, side by side", [
            "paired in one line,",
            "not opposed"
        ]),
    ],
    further=[
        '<a href="%s/thag1.12/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.11.html">Thag 1.11 &mdash; C&umacr;'
        "&#7735;avaccha</a> &mdash; the poem immediately before this "
        "one, opening this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.13 — Vanavaccha (1st)
# --------------------------------------------------------------------------- #
page(
    1, 13, "Vanavaccha", "Vanavaccha (1st)",
    meta_title="Thag 1.13 — Vanavaccha (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vanavaccha's verse, a pure nature poem delighting in blue "
        "rocky crags, cool streams, and ladybugs, with no doctrinal "
        "vocabulary at all. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 3 of 10",
    glance=[
        ("Setting", "Rocky crags in a forest, glistening like storm "
                    "clouds, with cool clear streams"),
        ("Speaker", "Vanavaccha, exclaiming his own delight directly"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "pure sensory delight, without a single "
                       "doctrinal term"),
    ],
    why=(
        "A third Vaccha appears in this chapter &mdash; Vanavaccha, "
        "&lsquo;forest Vaccha&rsquo; &mdash; and unlike Cūḷavaccha's "
        "or Mahāvaccha's compact instructive verses, his is pure "
        "nature description: rocky crags &lsquo;glistening, like blue "
        "stormclouds&rsquo;, cool clear streams, and crags "
        "&lsquo;covered all in ladybugs&rsquo;, closing in one direct "
        "exclamation of delight."),
    guide=[
        ("A third Vaccha, a different register entirely", [
            "Cūḷavaccha and Mahāvaccha, the two poems just before "
            "this one, each named specific qualities or practices. "
            "Vanavaccha's verse names none &mdash; no wisdom, no "
            "precepts, no absorption &mdash; only the physical scene "
            "in front of him, described for its own sake."]),
        ("Vivid, specific, almost whimsical imagery", [
            "The rocks are compared to blue stormclouds; the streams "
            "are named cool and clear; and one line is given entirely "
            "to a small, specific detail &mdash; the crags "
            "&lsquo;covered all in ladybugs&rsquo; &mdash; a degree of "
            "concrete, almost playful observation unusual among this "
            "chapter's more instructive verses."]),
        ("A name marked '(1st)', pointing to another poem later", [
            "The &lsquo;(1st)&rsquo; attached to Vanavaccha's name "
            "follows the same disambiguating convention already seen "
            "with Puṇṇa and Puṇṇamāsa in Chapter One &mdash; signaling "
            "that a second monk sharing this same name appears "
            "somewhere later in the collection."]),
    ],
    terms=[
        ("n&imacr;labbhava&#7751;&#7751;&amacr;",
         "&ldquo;the color of blue stormclouds&rdquo; &mdash; the "
         "opening simile describing the crags' appearance."),
        ("s&imacr;tav&amacr;r&imacr;",
         "&ldquo;cool water&rdquo; &mdash; one quality named among the "
         "streams at this site."),
        ("indagopaka",
         "a small insect, translated here as &ldquo;ladybug&rdquo; "
         "&mdash; the verse's most specific, concrete image."),
        ("sel&amacr;",
         "&ldquo;rocky crags&rdquo; or &ldquo;boulders&rdquo; &mdash; "
         "the verse's central subject, named directly in its closing "
         "line."),
        ("ramayanti",
         "&ldquo;they delight&rdquo; &mdash; the verb closing the "
         "verse, describing the crags' effect on Vanavaccha directly."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.13:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Vanavaccha's verse describe?",
         "opts": [
             "A dispute between monks",
             "Rocky crags, cool streams, and ladybugs",
             "A meditation technique",
             "A journey to a distant city"],
         "correct": 1,
         "expl": "Pure nature description, unlike the two verses just before it."},
        {"q": "How does this verse compare to Cūḷavaccha's and Mahāvaccha's verses just before it?",
         "opts": [
             "It names no doctrinal qualities at all, only the physical scene",
             "It is identical in content",
             "It names even more doctrinal terms than either",
             "It describes a completely different Vaccha's death"],
         "correct": 0,
         "expl": "A shift from instruction to pure sensory delight."},
        {"q": "What simile opens this verse?",
         "opts": [
             "The crags compared to blue stormclouds",
             "The crags compared to gold",
             "The crags compared to a lion's mane",
             "No simile is used"],
         "correct": 0,
         "expl": "The verse's opening image."},
        {"q": "What small, specific detail appears in this verse's third line?",
         "opts": [
             "A description of birds",
             "A description of fish in the stream",
             "A description of trees",
             "The crags covered all in ladybugs"],
         "correct": 3,
         "expl": "A concrete, almost whimsical observation."},
        {"q": "How does the verse close?",
         "opts": [
             "With a question left open",
             "With a warning about danger",
             "With a list of other monks",
             "With a direct exclamation: these rocky crags delight me"],
         "correct": 3,
         "expl": "A first-person statement of pure delight."},
        {"q": "What does the '(1st)' attached to Vanavaccha's name signal?",
         "opts": [
             "That he was the first monk ever ordained",
             "Nothing in particular",
             "That a second monk sharing this same name appears later in the collection",
             "That this is the first poem in the entire Theragātha"],
         "correct": 2,
         "expl": "The same disambiguating convention used for Puṇṇa and Puṇṇamāsa in Chapter One."},
        {"q": "What does 'sītavārī' mean?",
         "opts": [
             "Hot spring",
             "Cool water",
             "Muddy river",
             "Salt water"],
         "correct": 1,
         "expl": "Describing the streams at this site."},
        {"q": "Does this verse mention wisdom, precepts, or absorption?",
         "opts": [
             "Yes, all three are named directly",
             "Only wisdom is mentioned",
             "No — none of these are named in this verse",
             "Only precepts are mentioned"],
         "correct": 2,
         "expl": "A verse entirely about the physical scene, not doctrine."},
        {"q": "What is 'indagopaka' translated as in this verse?",
         "opts": [
             "Ladybug",
             "Deer",
             "Snake",
             "Butterfly"],
         "correct": 0,
         "expl": "A small insect covering the rocky crags."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "The third poem, following Cūḷavaccha and Mahāvaccha",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "The third of ten poems in this chapter."},
    ],
    marginalia=[
        ("A third Vaccha, a new register", [
            "no doctrine at all —",
            "only the scene itself"
        ]),
        ("Blue crags, cool streams", [
            "glistening,",
            "like stormclouds"
        ]),
        ("A small, specific detail", [
            "covered all",
            "in ladybugs"
        ]),
        ("A name marked '(1st)'", [
            "a second Vanavaccha",
            "appears later"
        ]),
    ],
    further=[
        '<a href="%s/thag1.13/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.12.html">Thag 1.12 &mdash; Mah&amacr;'
        "vaccha</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.14 — The Novice S&imacr;vaka
# --------------------------------------------------------------------------- #
page(
    1, 14, "S&imacr;vaka", "The Novice S&imacr;vaka",
    meta_title="Thag 1.14 — The Novice Sīvaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the novice Sīvaka's verse, his body in the village but his "
        "mind gone to the wilderness, closing on an aphorism about "
        "freedom. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 4 of 10",
    glance=[
        ("Setting", "A village, and the wilderness Sīvaka's mind has "
                    "gone to instead"),
        ("Speaker", "Sīvaka, quoting his mentor's own words before "
                    "answering in his own voice"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a quoted exchange, a striking split image, and "
                       "a closing aphorism"),
    ],
    why=(
        "Sīvaka's mentor tells him, &lsquo;let's leave here, "
        "Sīvaka&rsquo; &mdash; and Sīvaka answers not with agreement "
        "or refusal but with a striking image: his body still lives "
        "in the village, but his mind has already gone to the "
        "wilderness, present there even when he is lying down. "
        "&lsquo;You can't chain those who know&rsquo;, the verse "
        "closes."),
    guide=[
        ("A mentor's own words, quoted directly", [
            "Unlike most poems in this chapter, this verse opens by "
            "quoting another person's speech directly: &lsquo;my "
            "mentor said to me: &ldquo;let's leave here, "
            "Sīvaka&rdquo;&rsquo;. Sīvaka's own verse becomes his "
            "answer to that remark, rather than a self-contained "
            "statement."]),
        ("A body in one place, a mind in another", [
            "&lsquo;My body lives in the village, but my mind has "
            "gone to the wilderness&rsquo; separates physical location "
            "from mental location entirely &mdash; and the next line "
            "extends this further: &lsquo;I go there even when lying "
            "down&rsquo;, meaning the mind's presence in the "
            "wilderness does not depend on active effort or waking "
            "attention."]),
        ("The collection's first novice, not yet an elder", [
            "This poem's own file title identifies Sīvaka as a "
            "s&amacr;ma&#7751;era, a novice not yet fully ordained "
            "&mdash; distinct from the thera (&lsquo;senior&rsquo;) "
            "title carried by every other named speaker encountered so "
            "far in this collection."]),
        ("A personal answer, closing as a general maxim", [
            "The verse's final line, &lsquo;you can't chain those who "
            "know&rsquo;, shifts from Sīvaka's own particular situation "
            "to a general statement about anyone who has come to "
            "understand &mdash; his mentor's remark answered, in the "
            "end, with a principle rather than a plain yes or no."]),
    ],
    terms=[
        ("upajjh&amacr;ya",
         "&ldquo;preceptor&rdquo; or &ldquo;mentor&rdquo; &mdash; the "
         "one who speaks the verse's opening line, prompting Sīvaka's "
         "answer."),
        ("s&amacr;ma&#7751;era",
         "&ldquo;novice&rdquo; &mdash; Sīvaka's own status, per this "
         "poem's file title, distinct from the thera title used "
         "elsewhere in this collection."),
        ("g&amacr;ma",
         "&ldquo;village&rdquo; &mdash; where Sīvaka says his body "
         "still lives."),
        ("ara&ntilde;&ntilde;a",
         "&ldquo;wilderness&rdquo; or &ldquo;forest&rdquo; &mdash; "
         "where Sīvaka says his mind has already gone."),
        ("na bandhanti",
         "&ldquo;they cannot chain&rdquo; &mdash; the verse's closing "
         "verb, naming what cannot be done to &lsquo;those who "
         "know&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.14:1.1-1.6"),
    ],
    quiz=[
        {"q": "How does this verse open?",
         "opts": [
             "With a description of a hut",
             "By quoting Sīvaka's mentor directly: 'let's leave here, Sīvaka'",
             "With a question addressed to the Buddha",
             "With a list of other monks"],
         "correct": 1,
         "expl": "A rare instance in this collection of another person's speech quoted directly."},
        {"q": "Where does Sīvaka say his body lives?",
         "opts": [
             "In the village",
             "In a cave",
             "By a river",
             "In a palace"],
         "correct": 0,
         "expl": "Contrasted directly with where his mind has gone."},
        {"q": "Where does Sīvaka say his mind has gone?",
         "opts": [
             "To the wilderness",
             "Nowhere — his mind stays with his body",
             "To his childhood home",
             "To a distant kingdom"],
         "correct": 0,
         "expl": "The verse's central split between body and mind."},
        {"q": "According to the verse, when does Sīvaka's mind go to the wilderness?",
         "opts": [
             "Only during formal meditation sessions",
             "Only once a year",
             "Even when he is lying down",
             "Never — the verse says this cannot happen"],
         "correct": 2,
         "expl": "Presence in the wilderness independent of active effort."},
        {"q": "What does Sīvaka's file title identify him as?",
         "opts": [
             "A king",
             "A senior elder, like the other speakers so far",
             "A layperson",
             "A sāmaṇera, a novice not yet fully ordained"],
         "correct": 3,
         "expl": "The collection's first novice voice encountered so far."},
        {"q": "How does the verse close?",
         "opts": [
             "With a direct yes or no answer to his mentor",
             "With a question left open",
             "With a general maxim: you can't chain those who know",
             "With a list of monastic rules"],
         "correct": 2,
         "expl": "A shift from personal situation to general principle."},
        {"q": "What does 'ārañña' mean?",
         "opts": [
             "Village",
             "Wilderness or forest",
             "Riverbank",
             "Marketplace"],
         "correct": 1,
         "expl": "Where Sīvaka's mind is said to have gone."},
        {"q": "Who speaks the verse's opening quoted line?",
         "opts": [
             "The Buddha",
             "Sīvaka's mentor (upajjhāya)",
             "An unnamed stranger",
             "Sīvaka's mother"],
         "correct": 1,
         "expl": "Named directly as the one who prompts Sīvaka's answer."},
        {"q": "How many lines does this verse have?",
         "opts": [
             "Two",
             "Four",
             "Six",
             "Ten"],
         "correct": 2,
         "expl": "Slightly longer than this chapter's typical four-line verses."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "It is not part of this chapter",
             "The fourth poem, following Vanavaccha's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A mentor's words, quoted", [
            "'let's leave here,",
            "Sīvaka'"
        ]),
        ("Body here, mind elsewhere", [
            "village and wilderness,",
            "held apart"
        ]),
        ("The collection's first novice", [
            "sāmaṇera,",
            "not yet an elder"
        ]),
        ("An answer becomes a maxim", [
            "you can't chain",
            "those who know"
        ]),
    ],
    further=[
        '<a href="%s/thag1.14/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.13.html">Thag 1.13 &mdash; Vanavaccha '
        "(1st)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.15 — Ku&#7751;&#7693;adh&amacr;na
# --------------------------------------------------------------------------- #
page(
    1, 15, "Ku&#7751;&#7693;adh&amacr;na", "Ku&#7751;&#7693;adh&amacr;na",
    meta_title="Thag 1.15 — Kuṇḍadhāna | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kuṇḍadhāna's verse, a compressed numerical formula naming "
        "five things to cut, five to drop, and five to develop. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse structured "
                    "entirely as a numerical formula"),
        ("Speaker", "An unnamed voice describing a mendicant who has "
                    "achieved this formula's goal"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734; &mdash; a "
                       "densely compressed doctrinal formula, naming "
                       "categories without listing their contents"),
    ],
    why=(
        "This verse is built entirely from numbers: five things to "
        "cut, five to drop, five more to develop &mdash; a mendicant "
        "who slips five chains, it says, is said to have crossed the "
        "flood. Nothing is spelled out; the verse assumes its listener "
        "already knows what each group of five contains."),
    guide=[
        ("Three groups of five, compressed into two lines", [
            "&lsquo;Five to cut, five to drop, and five more to "
            "develop&rsquo; packs three distinct doctrinal categories "
            "into a single opening couplet &mdash; functioning less as "
            "a description than as a mnemonic prompt, testing whether "
            "the listener can supply the specific five items each "
            "category names."]),
        ("What the three fives traditionally name", [
            "In standard early Buddhist teaching, the five things to "
            "cut are the five lower fetters (identity view, doubt, "
            "attachment to precepts and observances, sensual desire, "
            "and ill will); the five to drop are the five higher "
            "fetters (desire for fine-material and formless existence, "
            "conceit, restlessness, and ignorance); and the five to "
            "develop are the five spiritual faculties (faith, energy, "
            "mindfulness, immersion, and wisdom). The verse itself "
            "names none of these directly."]),
        ("Crossing the flood as the formula's outcome", [
            "The verse closes by naming its result rather than "
            "describing it further: a mendicant who &lsquo;slips five "
            "chains&rsquo; &mdash; a fourth group of five, referring "
            "to attachments generally &mdash; is said to have "
            "&lsquo;crossed the flood&rsquo;, a standard image for "
            "having gone beyond the round of rebirth."]),
    ],
    terms=[
        ("pa&ntilde;ca chinde",
         "&ldquo;five to cut&rdquo; &mdash; traditionally the five "
         "lower fetters: identity view, doubt, attachment to rites "
         "and observances, sensual desire, and ill will."),
        ("pa&ntilde;ca jahe",
         "&ldquo;five to drop&rdquo; &mdash; traditionally the five "
         "higher fetters: desire for fine-material and formless "
         "existence, conceit, restlessness, and ignorance."),
        ("pa&ntilde;ca bh&amacr;vaye",
         "&ldquo;five to develop&rdquo; &mdash; traditionally the "
         "five spiritual faculties: faith, energy, mindfulness, "
         "immersion, and wisdom."),
        ("sa&#7749;ga",
         "&ldquo;chain&rdquo; or &ldquo;attachment&rdquo; &mdash; what "
         "a mendicant is said to slip free of in this verse's third "
         "line."),
        ("oghati&#7751;&#7751;a",
         "&ldquo;crossed the flood&rdquo; &mdash; a standard image for "
         "having gone beyond saṃsāra, closing this verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.15:1.1-1.4"),
    ],
    quiz=[
        {"q": "How is this verse structured?",
         "opts": [
             "Entirely as a numerical formula, naming groups of five",
             "As a narrative about a journey",
             "As a dialogue between two monks",
             "As a description of a landscape"],
         "correct": 0,
         "expl": "Three groups of five, compressed into a single couplet."},
        {"q": "Does the verse list the specific contents of its groups of five?",
         "opts": [
             "Yes, in full detail",
             "No — it names the categories without listing their contents",
             "Only the first group is listed",
             "Only the last group is listed"],
         "correct": 1,
         "expl": "Functioning as a mnemonic prompt rather than a full exposition."},
        {"q": "According to standard early Buddhist teaching, what do the 'five to cut' traditionally refer to?",
         "opts": [
             "The five spiritual faculties",
             "Five monastic rules",
             "Five types of food",
             "The five lower fetters"],
         "correct": 3,
         "expl": "Identity view, doubt, attachment to rites, sensual desire, and ill will."},
        {"q": "What do the 'five to develop' traditionally refer to?",
         "opts": [
             "The five higher fetters",
             "Five geographic regions",
             "The five spiritual faculties",
             "Five monastic robes"],
         "correct": 2,
         "expl": "Faith, energy, mindfulness, immersion, and wisdom."},
        {"q": "What does the verse say happens to a mendicant who slips five chains?",
         "opts": [
             "Nothing in particular",
             "They are said to have crossed the flood",
             "They are said to have failed",
             "They must start their training over"],
         "correct": 1,
         "expl": "The formula's stated outcome, closing the verse."},
        {"q": "What does 'oghatiṇṇa' mean?",
         "opts": [
             "Still crossing the flood",
             "Never having entered the flood",
             "Crossed the flood",
             "Drowned in the flood"],
         "correct": 2,
         "expl": "A standard image for having gone beyond the round of rebirth."},
        {"q": "What do the 'five to drop' traditionally refer to?",
         "opts": [
             "The five higher fetters",
             "The five lower fetters",
             "Five types of almsfood",
             "Five monastic vows"],
         "correct": 0,
         "expl": "Desire for fine-material and formless existence, conceit, restlessness, and ignorance."},
        {"q": "What does 'saṅga' mean in this verse's third line?",
         "opts": [
             "A song",
             "A chain or attachment",
             "A river",
             "A monastery"],
         "correct": 1,
         "expl": "What a mendicant is said to slip free of."},
        {"q": "How does this verse's style compare to Vanavaccha's nature poem just before it?",
         "opts": [
             "Both are pure nature description",
             "They are identical in style",
             "Neither uses any numbers",
             "This verse is a compressed doctrinal formula, unlike Vanavaccha's sensory imagery"],
         "correct": 3,
         "expl": "A shift back from sensory delight to dense doctrinal structure."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "The fifth poem, following Sīvaka's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Three fives, one couplet", [
            "cut, drop,",
            "and develop"
        ]),
        ("Named, not listed", [
            "categories only —",
            "contents assumed known"
        ]),
        ("A fourth five, closing the verse", [
            "chains slipped,",
            "the flood crossed"
        ]),
        ("From sensory delight to formula", [
            "a sharp contrast",
            "with the poem before it"
        ]),
    ],
    further=[
        '<a href="%s/thag1.15/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.14.html">Thag 1.14 &mdash; The Novice '
        "S&imacr;vaka</a> &mdash; the poem immediately before this "
        "one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.16 — Bela&#7789;&#7789;has&imacr;sa
# --------------------------------------------------------------------------- #
page(
    1, 16, "Bela&#7789;&#7789;has&imacr;sa", "Bela&#7789;&#7789;has&imacr;sa",
    meta_title="Thag 1.16 — Belaṭṭhasīsa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Belaṭṭhasīsa's verse, comparing his days and nights to a "
        "thoroughbred running with ease, full of joy not of the "
        "flesh. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse comparing "
                    "time itself to a running horse"),
        ("Speaker", "Belaṭṭhasīsa, describing his own days and "
                    "nights"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a horse simile applied not to a person but to "
                       "the passage of time itself"),
    ],
    why=(
        "Belaṭṭhasīsa compares his days and nights to a fine "
        "thoroughbred running with ease, tail and mane flying in the "
        "wind &mdash; not himself directly, but the passage of time "
        "itself, moving easily and full of &lsquo;joy not of the "
        "flesh&rsquo;."),
    guide=[
        ("A horse simile applied to time, not to a person", [
            "Most similes comparing someone to a fine horse describe "
            "the person's own bearing or conduct. Here the comparison "
            "lands somewhere less expected: &lsquo;so my days and "
            "nights proceed with ease&rsquo; &mdash; the thoroughbred "
            "image applied to the passage of time itself, rather than "
            "to Belaṭṭhasīsa's own posture or movement."]),
        ("A joy specifically 'not of the flesh'", [
            "The verse's closing phrase names a recognized "
            "distinction in early Buddhist vocabulary: pleasure that "
            "is āmisa, &lsquo;of the flesh&rsquo; or worldly, versus "
            "pleasure that is nirāmisa, arising instead from "
            "meditation and renunciation &mdash; and it is this second "
            "kind the verse claims fills his days."]),
        ("Joy returning at the chapter's midpoint", [
            "This chapter opened with Cūḷavaccha's verse naming joy "
            "as the condition for peace. Here, roughly at its "
            "midpoint, another poem returns to joy directly &mdash; "
            "this time specified precisely as joy that is not "
            "sensory, echoing rather than repeating the chapter's "
            "opening theme."]),
    ],
    terms=[
        ("&amacr;ja&ntilde;&ntilde;a",
         "&ldquo;thoroughbred&rdquo; &mdash; the fine, well-bred horse "
         "at the center of this verse's simile."),
        ("appakasirena",
         "&ldquo;with ease&rdquo; or &ldquo;without difficulty&rdquo; "
         "&mdash; describing how both the horse and Belaṭṭhasīsa's own "
         "days and nights proceed."),
        ("rattindiv&amacr;",
         "&ldquo;days and nights&rdquo; &mdash; what this verse "
         "compares directly to a running horse."),
        ("p&imacr;ti",
         "&ldquo;joy&rdquo; or &ldquo;rapture&rdquo; &mdash; the "
         "quality filling Belaṭṭhasīsa's days, according to this "
         "verse's closing line."),
        ("nir&amacr;misa",
         "&ldquo;not of the flesh&rdquo;, non-material or spiritual "
         "&mdash; distinguished in early Buddhist vocabulary from "
         "āmisa, worldly or sensory pleasure."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.16:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does this verse compare to a fine thoroughbred?",
         "opts": [
             "Belaṭṭhasīsa's own posture",
             "His days and nights, the passage of time itself",
             "A river",
             "A mountain path"],
         "correct": 1,
         "expl": "An unusual application of a common horse simile."},
        {"q": "How does the thoroughbred proceed, according to this verse?",
         "opts": [
             "Slowly and with great difficulty",
             "Only at night",
             "With ease, tail and mane flying in the wind",
             "The verse does not describe how it proceeds"],
         "correct": 2,
         "expl": "The verse's opening image."},
        {"q": "What kind of joy does the verse's closing line name?",
         "opts": [
             "Joy not of the flesh",
             "No joy is mentioned",
             "Joy purely from good food",
             "Joy from wealth and status"],
         "correct": 0,
         "expl": "A distinction between worldly and spiritual pleasure."},
        {"q": "What does 'nirāmisa' mean?",
         "opts": [
             "Wealthy",
             "Fearful",
             "A type of hut",
             "Not of the flesh, non-material or spiritual"],
         "correct": 3,
         "expl": "Distinguished from āmisa, worldly or sensory pleasure."},
        {"q": "How does this verse echo the chapter's opening poem, Cūḷavaccha's verse?",
         "opts": [
             "Both name joy directly, though in different ways",
             "There is no connection between the two",
             "Both are written entirely as dialogue",
             "Both describe the same horse"],
         "correct": 0,
         "expl": "A thematic echo at roughly the chapter's midpoint."},
        {"q": "What does 'rattindivā' mean?",
         "opts": [
             "A type of robe",
             "Days and nights",
             "A river crossing",
             "A monastic title"],
         "correct": 1,
         "expl": "What this verse compares directly to a running horse."},
        {"q": "What does 'appakasirena' describe?",
         "opts": [
             "Something done with great difficulty",
             "A type of meal",
             "A geographic region",
             "Something done with ease"],
         "correct": 3,
         "expl": "How both the horse and Belaṭṭhasīsa's days are said to proceed."},
        {"q": "How many lines does this verse have?",
         "opts": [
             "Two",
             "Four",
             "Six",
             "Ten"],
         "correct": 2,
         "expl": "Slightly longer than this chapter's shortest verses."},
        {"q": "Is this simile applied to a person's conduct or to something else?",
         "opts": [
             "To a person's conduct, as most such similes are",
             "To the weather",
             "To something less expected: the passage of time itself",
             "To a monastic building"],
         "correct": 2,
         "expl": "An unusual twist on a familiar comparison."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It opens the chapter",
             "The sixth poem, following Kuṇḍadhāna's",
             "It closes the chapter",
             "It is not part of this chapter"],
         "correct": 1,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A horse simile, redirected", [
            "not his posture —",
            "his days and nights"
        ]),
        ("Two kinds of pleasure", [
            "āmisa, and",
            "nirāmisa"
        ]),
        ("Joy, echoing the chapter's opening", [
            "returning again,",
            "at its midpoint"
        ]),
        ("Ease, without difficulty", [
            "tail and mane",
            "flying in the wind"
        ]),
    ],
    further=[
        '<a href="%s/thag1.16/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.15.html">Thag 1.15 &mdash; Ku&#7751;'
        "&#7693;adh&amacr;na</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.17 — D&amacr;saka
# --------------------------------------------------------------------------- #
page(
    1, 17, "D&amacr;saka", "D&amacr;saka",
    meta_title="Thag 1.17 — Dāsaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Dāsaka's verse, this chapter's only cautionary poem, warning "
        "against gluttony and drowsiness with a vivid hog simile. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative setting; a short cautionary verse "
                    "warning against a specific failing"),
        ("Speaker", "An unnamed voice criticizing a drowsy, "
                    "overfed dullard"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "vivid, unflattering warning rather than a "
                       "positive portrait"),
    ],
    why=(
        "Every poem in this chapter so far has praised a quality or "
        "described delight. This verse breaks that pattern: someone "
        "&lsquo;drowsy from overeating&rsquo;, rolling in bed "
        "&lsquo;like a great hog stuffed with grain&rsquo;, is called "
        "a dullard who &lsquo;returns to the womb again and "
        "again&rsquo; &mdash; the chapter's only warning against a "
        "failing, rather than praise for an attainment."),
    guide=[
        ("This chapter's only cautionary verse", [
            "Cūḷavaccha's joy, Mahāvaccha's checklist, Vanavaccha's "
            "delight, Sīvaka's freedom, Kuṇḍadhāna's formula, "
            "Belaṭṭhasīsa's ease &mdash; every poem before this one "
            "describes something to aspire to. This verse instead "
            "names a failing directly and criticizes it, the "
            "chapter's first and only poem built entirely as a "
            "warning."]),
        ("A deliberately unflattering simile", [
            "&lsquo;Like a great hog stuffed with grain, rolling round "
            "the bed&rsquo; is among the least dignified images "
            "anywhere in this collection so far &mdash; a pointed "
            "contrast to Belaṭṭhasīsa's fine thoroughbred just two "
            "poems earlier, and a deliberate choice to make laziness "
            "look as unappealing as possible."]),
        ("A stated consequence, not just a criticism", [
            "The verse does not simply call this behavior "
            "unattractive; it names a direct outcome &mdash; "
            "&lsquo;that dullard returns to the womb again and "
            "again&rsquo;, tying gluttony and oversleeping to repeated "
            "rebirth, teaching through the threat of consequence "
            "rather than through praise of an alternative."]),
    ],
    terms=[
        ("middh&imacr;",
         "&ldquo;drowsy&rdquo; or &ldquo;sluggish&rdquo; &mdash; the "
         "verse's opening description, caused by overeating."),
        ("mahagghasa",
         "&ldquo;a great eater&rdquo; or &ldquo;gluttonous&rdquo; "
         "&mdash; paired directly with drowsiness in the verse's "
         "first line."),
        ("mah&amacr;var&amacr;ha",
         "&ldquo;a great hog&rdquo; or &ldquo;great boar&rdquo; "
         "&mdash; the verse's central, deliberately unflattering "
         "simile."),
        ("manda",
         "&ldquo;dullard&rdquo; or &ldquo;fool&rdquo; &mdash; the "
         "verse's judgment on the person it describes."),
        ("punappuna&#7745; gabbhamupeti",
         "&ldquo;returns to the womb again and again&rdquo; &mdash; "
         "the stated consequence of this behavior, naming repeated "
         "rebirth directly."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.17:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this poem differ from every other poem in this chapter so far?",
         "opts": [
             "It is the chapter's only cautionary verse, warning against a failing",
             "It is the only poem written in the first person",
             "It is the only poem with no simile",
             "There is no difference"],
         "correct": 0,
         "expl": "Every poem before it praised a quality; this one criticizes a failing instead."},
        {"q": "What simile does the verse use for the person it describes?",
         "opts": [
             "A fine thoroughbred",
             "A great hog stuffed with grain, rolling round the bed",
             "A lion in a mountain cave",
             "A blooming lotus"],
         "correct": 1,
         "expl": "A deliberately unflattering image."},
        {"q": "What two causes does the verse name for this person's drowsiness?",
         "opts": [
             "Illness and old age",
             "Fear and doubt",
             "Nothing is named",
             "Overeating and fondness for sleep"],
         "correct": 3,
         "expl": "Named directly in the verse's opening line."},
        {"q": "What consequence does the verse say follows from this behavior?",
         "opts": [
             "Nothing in particular",
             "Great wealth",
             "Returning to the womb again and again",
             "Becoming a respected teacher"],
         "correct": 2,
         "expl": "A direct outcome, tying the behavior to repeated rebirth."},
        {"q": "How does this verse's tone compare to Belaṭṭhasīsa's thoroughbred simile two poems earlier?",
         "opts": [
             "Both use the exact same simile",
             "A pointed contrast — dignified ease there, an unflattering hog image here",
             "Neither uses any animal imagery",
             "This verse is even more flattering than Belaṭṭhasīsa's"],
         "correct": 1,
         "expl": "A deliberate contrast in register between the two poems."},
        {"q": "What does 'manda' mean?",
         "opts": [
             "Wise one",
             "King",
             "Teacher",
             "Dullard or fool"],
         "correct": 3,
         "expl": "The verse's judgment on the person it describes."},
        {"q": "What does 'mahagghasa' describe?",
         "opts": [
             "A great eater, or gluttonous",
             "A great warrior",
             "A great teacher",
             "A great river"],
         "correct": 0,
         "expl": "Paired with drowsiness in the verse's opening line."},
        {"q": "Does this verse describe a positive attainment or warn against a failing?",
         "opts": [
             "It describes a positive attainment",
             "It warns against a failing",
             "It does neither",
             "It describes both equally"],
         "correct": 1,
         "expl": "Teaching through the threat of consequence, not through praise."},
        {"q": "What does 'middhī' mean?",
         "opts": [
             "Drowsy or sluggish",
             "Energetic",
             "Wealthy",
             "Fearless"],
         "correct": 0,
         "expl": "The verse's opening description of this dullard's state."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The seventh poem, following Belaṭṭhasīsa's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A pattern broken", [
            "the chapter's only",
            "cautionary verse"
        ]),
        ("An unflattering image, on purpose", [
            "a hog stuffed with grain,",
            "rolling in bed"
        ]),
        ("A consequence, not just a criticism", [
            "returning to the womb",
            "again and again"
        ]),
        ("Contrast with the poem before it", [
            "a thoroughbred's ease,",
            "a hog's stupor"
        ]),
    ],
    further=[
        '<a href="%s/thag1.17/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.16.html">Thag 1.16 &mdash; Bela&#7789;'
        "&#7789;has&imacr;sa</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.18 — Si&#7749;g&amacr;la&rsquo;s Father
# --------------------------------------------------------------------------- #
page(
    1, 18, "Si&#7749;g&amacr;lapit&amacr;", "Si&#7749;g&amacr;la&rsquo;s Father",
    meta_title="Thag 1.18 — Siṅgāla's Father | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Siṅgāla's Father's verse, admiringly predicting another "
        "monk's swift release from sensual desire through the "
        "perception of bones. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 8 of 10",
    glance=[
        ("Setting", "Bhesakaḷā forest, where another, unnamed monk "
                    "practices"),
        ("Speaker", "Siṅgāla's Father, admiringly predicting this "
                    "other monk's swift attainment"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "an admiring prediction about someone else's "
                       "practice, not a self-description"),
    ],
    why=(
        "Unlike every poem in this chapter so far, this verse's "
        "speaker describes neither himself nor a generic figure, but "
        "a specific fellow monk he has been watching: an &lsquo;heir "
        "of the Buddha&rsquo; in Bhesakaḷā forest who &lsquo;suffused "
        "the entire earth with the perception of bones&rsquo;. "
        "&lsquo;I think he will quickly get rid of sensual "
        "desire&rsquo;, Siṅgāla's Father predicts."),
    guide=[
        ("Named through his son, a third naming pattern in this chapter", [
            "&lsquo;Siṅgāla's Father&rsquo; identifies this monk by "
            "his relationship to his son, not by clan (as with the "
            "three Vacchas) or by place (as with Vanavaccha or "
            "Sītavaniya in Chapter One) &mdash; a third distinct "
            "naming convention appearing within this same chapter."]),
        ("Admiration and prediction, not self-description", [
            "Every poem before this one in the chapter speaks about "
            "its own subject directly. This verse instead watches "
            "someone else practice and offers a considered assessment "
            "&mdash; &lsquo;I think he will quickly&hellip;&rsquo; "
            "&mdash; a poem of admiring observation rather than "
            "self-declaration."]),
        ("The perception of bones, described on a cosmic scale", [
            "&lsquo;Suffused the entire earth with the perception of "
            "bones&rsquo; names a specific traditional practice, "
            "meditating on the body reduced to its skeleton, but "
            "describes its scope in strikingly expansive terms "
            "&mdash; not a private inner exercise but something that "
            "seems to fill the whole world."]),
    ],
    terms=[
        ("d&amacr;y&amacr;da",
         "&ldquo;heir&rdquo; &mdash; the verse's opening title for "
         "the monk it describes, &lsquo;an heir of the Buddha&rsquo;."),
        ("Bhesaka&#7735;&amacr;vana",
         "the forest named as the setting where this other monk "
         "practices."),
        ("a&#7789;&#7789;hikasa&ntilde;&ntilde;&amacr;",
         "&ldquo;the perception of bones&rdquo; &mdash; a traditional "
         "meditation contemplating the body reduced to its skeleton."),
        ("pharati",
         "&ldquo;suffuses&rdquo; or &ldquo;pervades&rdquo; &mdash; "
         "the verb describing this meditation's strikingly expansive "
         "scope in the verse."),
        ("r&amacr;ga",
         "&ldquo;desire&rdquo; or &ldquo;passion&rdquo; &mdash; "
         "specifically sensual desire, which Siṅgāla's Father predicts "
         "this monk will soon be rid of."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.18:1.1-1.6"),
    ],
    quiz=[
        {"q": "Who is the subject of this verse?",
         "opts": [
             "A different, unnamed monk he has been observing",
             "Siṅgāla's Father himself",
             "The Buddha directly",
             "No specific person is described"],
         "correct": 0,
         "expl": "A poem of observation and prediction, not self-description."},
        {"q": "How does 'Siṅgāla's Father' get his own name?",
         "opts": [
             "Through a clan name, like the three Vacchas",
             "Through a place name, like Vanavaccha",
             "Through his relationship to his son",
             "His name has no particular meaning"],
         "correct": 2,
         "expl": "A third distinct naming convention within this chapter."},
        {"q": "What practice does the verse say the observed monk performs?",
         "opts": [
             "The perception of bones",
             "Chanting scripture aloud",
             "Fasting for many days",
             "Teaching new novices"],
         "correct": 0,
         "expl": "A traditional meditation on the body reduced to its skeleton."},
        {"q": "How does the verse describe the scope of this practice?",
         "opts": [
             "As a small, private exercise",
             "As suffusing the entire earth",
             "As lasting only a moment",
             "The scope is not described"],
         "correct": 1,
         "expl": "An expansive, almost cosmic description of an inner practice."},
        {"q": "What does Siṅgāla's Father predict about this monk?",
         "opts": [
             "That he will quickly get rid of sensual desire",
             "That he will fail in his practice",
             "That he will leave the monastery",
             "Nothing is predicted"],
         "correct": 0,
         "expl": "The verse's closing assessment."},
        {"q": "What does 'dāyāda' mean, as used in this verse's opening title?",
         "opts": [
             "Enemy",
             "Stranger",
             "Servant",
             "Heir"],
         "correct": 3,
         "expl": "'An heir of the Buddha', the verse's opening description."},
        {"q": "Where is this other monk said to practice?",
         "opts": [
             "In a royal palace",
             "In Bhesakaḷā forest",
             "By the ocean",
             "In a city market"],
         "correct": 1,
         "expl": "Named directly as the verse's setting."},
        {"q": "How does this poem's structure compare to the rest of this chapter so far?",
         "opts": [
             "Identical to every other poem",
             "Unique so far — an assessment of someone else's practice, not a self-portrait",
             "It is the only poem with no verbs",
             "It is the shortest poem in the chapter"],
         "correct": 1,
         "expl": "A shift from self-description to admiring observation of another."},
        {"q": "What does 'rāga' mean in this verse's closing line?",
         "opts": [
             "Wisdom",
             "A type of robe",
             "A monastic title",
             "Desire or passion"],
         "correct": 3,
         "expl": "Specifically sensual desire, predicted to soon be gone."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "The eighth poem, following Dāsaka's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Named through his son", [
            "a third naming pattern,",
            "within one chapter"
        ]),
        ("Watching, not declaring", [
            "'I think he will",
            "quickly...'"
        ]),
        ("A practice, described cosmically", [
            "suffusing",
            "the entire earth"
        ]),
        ("An heir, observed with admiration", [
            "bones perceived,",
            "desire soon to end"
        ]),
    ],
    further=[
        '<a href="%s/thag1.18/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.17.html">Thag 1.17 &mdash; D&amacr;saka</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.19 — Kula
# --------------------------------------------------------------------------- #
page(
    1, 19, "Kula", "Kula",
    meta_title="Thag 1.19 — Kula | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kula's verse, three trades shaping water, arrows, and "
        "timber, extended to self-taming as a fourth craft. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting; three trades named in "
                    "sequence, then applied to self-training"),
        ("Speaker", "An unnamed voice describing three crafts, then "
                    "those true to their vows"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "three concrete trades, then one closing "
                       "extension"),
    ],
    why=(
        "Three lines of craftspeople open this verse: irrigators "
        "guiding water, fletchers shaping arrows, carpenters carving "
        "timber. Only in its fourth and final line does the verse "
        "reveal its actual subject &mdash; &lsquo;those true to their "
        "vows tame themselves&rsquo; &mdash; treating ethical training "
        "as a fourth craft, alongside the other three."),
    guide=[
        ("Three trades, then one closing extension", [
            "The verse spends three full lines on concrete, familiar "
            "work before pivoting to its real subject in the fourth "
            "&mdash; a classic pattern of naming several examples "
            "before drawing the point they all lead toward."]),
        ("Each craft, a slightly different kind of shaping", [
            "The verbs vary precisely: water is guided, arrows are "
            "shaped, timber is carved &mdash; three distinct kinds of "
            "skilled work, each requiring patience and precision "
            "rather than force."]),
        ("Self-taming named as a fourth craft", [
            "The verse's point is not that ethical training resembles "
            "a trade in some vague sense, but that it is structurally "
            "the same kind of activity &mdash; a skill requiring the "
            "same deliberate, patient shaping that water, arrows, and "
            "timber all require from their respective craftspeople."]),
    ],
    terms=[
        ("nettika",
         "&ldquo;irrigator&rdquo; or &ldquo;canal-builder&rdquo; "
         "&mdash; the first of three trades named in this verse."),
        ("usuk&amacr;ra",
         "&ldquo;fletcher&rdquo;, one who shapes arrows &mdash; the "
         "second trade named."),
        ("tacchaka",
         "&ldquo;carpenter&rdquo; &mdash; the third trade named, "
         "carving timber."),
        ("subbata",
         "&ldquo;true to one's vows&rdquo; or &ldquo;good in "
         "observance&rdquo; &mdash; describing those the verse compares "
         "to these three craftspeople."),
        ("damayanti",
         "&ldquo;they tame&rdquo; &mdash; the verb closing the verse, "
         "attānaṁ damayanti, &lsquo;they tame themselves&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.19:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three trades does this verse name?",
         "opts": [
             "Farmers, fishers, and weavers",
             "Irrigators, fletchers, and carpenters",
             "Merchants, scribes, and physicians",
             "Potters, smiths, and bakers"],
         "correct": 1,
         "expl": "Each named in its own line before the verse's closing point."},
        {"q": "In what line does the verse reveal its real subject?",
         "opts": [
             "The first line",
             "The second line",
             "The fourth and final line",
             "The subject is never revealed"],
         "correct": 2,
         "expl": "Three examples given before the point they lead to."},
        {"q": "What does the verse's final line say?",
         "opts": [
             "Craftspeople should retire early",
             "Water cannot be guided",
             "Nothing follows the three trades",
             "Those true to their vows tame themselves"],
         "correct": 3,
         "expl": "Ethical training presented as a fourth craft."},
        {"q": "What does 'nettika' mean?",
         "opts": [
             "Fletcher",
             "Irrigator or canal-builder",
             "Carpenter",
             "Physician"],
         "correct": 1,
         "expl": "The first trade named in this verse."},
        {"q": "How does the verse's imagery differ across its three trades?",
         "opts": [
             "Each names a slightly different kind of skilled shaping",
             "All three describe the exact same action",
             "Only one trade is actually named",
             "None of the trades involve any skill"],
         "correct": 0,
         "expl": "Water guided, arrows shaped, timber carved — each distinct."},
        {"q": "What does 'usukāra' mean?",
         "opts": [
             "Irrigator",
             "Carpenter",
             "Fletcher, one who shapes arrows",
             "Farmer"],
         "correct": 2,
         "expl": "The second of the three trades named."},
        {"q": "What does 'subbata' describe?",
         "opts": [
             "Someone true to their vows",
             "A type of tree",
             "A river",
             "A monastic building"],
         "correct": 0,
         "expl": "Those the verse compares to skilled craftspeople."},
        {"q": "What kind of structure does this verse use?",
         "opts": [
             "A direct narrative with named characters",
             "Three examples building toward a closing point",
             "A question-and-answer dialogue",
             "A single unexplained image"],
         "correct": 1,
         "expl": "A classic rhetorical pattern of examples then application."},
        {"q": "What does 'tacchaka' mean?",
         "opts": [
             "Fletcher",
             "Irrigator",
             "Weaver",
             "Carpenter"],
         "correct": 3,
         "expl": "The third trade named, carving timber."},
        {"q": "Where does this poem fall in Chapter Two?",
         "opts": [
             "The ninth poem, following Siṅgāla's Father's",
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter"],
         "correct": 0,
         "expl": "Second to last in the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Three trades, one point", [
            "water, arrows, timber —",
            "then self-taming"
        ]),
        ("Different verbs, same patience", [
            "guided, shaped,",
            "carved"
        ]),
        ("A fourth craft", [
            "true to their vows,",
            "they tame themselves"
        ]),
        ("Examples, then application", [
            "three lines set up",
            "one closing line"
        ]),
    ],
    further=[
        '<a href="%s/thag1.19/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.18.html">Thag 1.18 &mdash; Si&#7749;'
        "g&amacr;la&rsquo;s Father</a> &mdash; the poem immediately "
        "before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.20 — Ajita
# --------------------------------------------------------------------------- #
page(
    1, 20, "Ajita", "Ajita",
    meta_title="Thag 1.20 — Ajita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ajita's verse, closing Chapter Two with equanimity toward "
        "both death and life, plus the chapter's own untranslated "
        "colophon. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Two &middot; Poem 10 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse closing "
                    "Chapter Two"),
        ("Speaker", "Ajita, stating his own equanimity directly"),
        ("Form", "One four-line verse, followed in the Pali by an "
                 "untranslated chapter colophon and mnemonic summary "
                 "verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a compact statement of equanimity, closing the "
                       "chapter"),
    ],
    why=(
        "Ajita's verse closes Chapter Two with a balanced statement: "
        "&lsquo;I do not fear death; nor do I long for life&rsquo; "
        "&mdash; refusing not only fear of dying but also any "
        "clinging to continued existence. &lsquo;I'll lay down this "
        "body, aware and mindful&rsquo;, he says, treating death as a "
        "deliberate release rather than something merely endured."),
    guide=[
        ("Equanimity toward both death and life, not just one", [
            "The verse's two opening claims work together rather than "
            "repeating each other: not fearing death addresses one "
            "common imbalance, while not longing for life addresses "
            "the opposite one &mdash; someone might lack fear of dying "
            "yet still cling to continued existence. Ajita's verse "
            "rules out both."]),
        ("'Lay down', not 'be torn from'", [
            "The verb Ajita chooses for his own death, &lsquo;I'll lay "
            "down this body&rsquo;, frames the act as a deliberate "
            "release under his own control, rather than something "
            "inflicted on him from outside."]),
        ("Aware and mindful, even at the final moment", [
            "The verse's closing pair, &lsquo;aware and "
            "mindful&rsquo;, names qualities of clear comprehension "
            "and recollection said to remain present even as the body "
            "is laid down &mdash; not lost in the process of dying, "
            "but sustained through it."]),
        ("A chapter's own close, left untranslated", [
            "As with Chapter One's close at Thag 1.10, the Pali text "
            "here carries vaggo dutiyo, &lsquo;the second chapter is "
            "finished&rsquo;, followed by an uddāna naming all ten "
            "monks of this chapter in sequence: Cūḷavaccha, "
            "Mahāvaccha, Vanavaccha, Sīvaka, Kuṇḍadhāna, Belaṭṭhasīsa, "
            "Dāsaka, Siṅgālapitā, Kula, and Ajita. Sujato's translation "
            "leaves both untranslated, and neither appears in this "
            "page's text below."]),
    ],
    terms=[
        ("mara&#7751;a",
         "&ldquo;death&rdquo; &mdash; named directly in this verse's "
         "opening line."),
        ("nikanti",
         "&ldquo;longing&rdquo; or &ldquo;craving&rdquo; &mdash; "
         "denied in this verse's second line, nikanti natthi "
         "j&imacr;vite, &lsquo;no craving for life&rsquo;."),
        ("sandeha",
         "&ldquo;this body&rdquo;, literally something like "
         "&ldquo;this heap&rdquo; &mdash; what Ajita says he will lay "
         "down."),
        ("sampaj&amacr;na",
         "&ldquo;aware&rdquo; or &ldquo;clearly comprehending&rdquo; "
         "&mdash; one of two qualities named in the verse's closing "
         "line."),
        ("pa&#7789;issata",
         "&ldquo;mindful&rdquo; &mdash; paired with sampajāna to "
         "close the verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.20:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Ajita say about death and life?",
         "opts": [
             "That he fears death but not life",
             "That he longs for both",
             "Nothing is said about either",
             "That he does not fear death, nor does he long for life"],
         "correct": 3,
         "expl": "A balanced statement addressing two different imbalances at once."},
        {"q": "Why do this verse's two opening claims matter together, not just separately?",
         "opts": [
             "One addresses fear of dying, the other addresses clinging to continued existence",
             "They repeat the exact same idea twice",
             "They contradict each other",
             "Only the first claim has any meaning"],
         "correct": 0,
         "expl": "Ruling out two different, opposite imbalances."},
        {"q": "What verb does Ajita use for his own death?",
         "opts": [
             "'Be torn from', implying force",
             "'Lay down', implying a deliberate release",
             "'Escape', implying urgency",
             "No verb is used"],
         "correct": 1,
         "expl": "Framing death as something under his own control."},
        {"q": "What two qualities close this verse?",
         "opts": [
             "Fear and doubt",
             "Wealth and status",
             "Aware and mindful",
             "Anger and grief"],
         "correct": 2,
         "expl": "Present, the verse implies, even at the moment of death."},
        {"q": "What does the Pali text carry immediately after this poem, left untranslated by Sujato?",
         "opts": [
             "A love poem",
             "A new eleventh poem",
             "Nothing follows this poem in the Pali",
             "'Vaggo dutiyo' ('the second chapter is finished') and an uddāna naming all ten monks of the chapter"],
         "correct": 3,
         "expl": "The same untranslated colophon pattern seen at the end of Chapter One."},
        {"q": "Does this page's text include that closing uddāna?",
         "opts": [
             "Yes, translated in full",
             "No — it is absent from Sujato's translation and not included here",
             "Yes, but only partially",
             "It is included as an image only"],
         "correct": 1,
         "expl": "Consistent with how this site handles untranslated structural material."},
        {"q": "What does 'sandeha' mean in this verse?",
         "opts": [
             "This body",
             "A river",
             "A monastic robe",
             "A type of hut"],
         "correct": 0,
         "expl": "What Ajita says he will lay down."},
        {"q": "How many monks' verses make up Chapter Two in total?",
         "opts": [
             "Five",
             "Ten",
             "Twenty",
             "One hundred and twenty"],
         "correct": 1,
         "expl": "Cūḷavaccha through Ajita, named in sequence in the untranslated uddāna."},
        {"q": "What does 'nikanti' mean?",
         "opts": [
             "Longing or craving",
             "Fear",
             "Wisdom",
             "Mindfulness"],
         "correct": 0,
         "expl": "Denied directly in the verse's second line."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the final chapter",
             "Exactly one more",
             "Ten more chapters",
             "The number is unknown"],
         "correct": 2,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
    ],
    marginalia=[
        ("Neither fear nor longing", [
            "not death feared,",
            "not life craved"
        ]),
        ("A release, not a loss", [
            "'I'll lay down",
            "this body'"
        ]),
        ("Present, even at the end", [
            "aware",
            "and mindful"
        ]),
        ("A second chapter closes", [
            "ten names, tabulated,",
            "left untranslated"
        ]),
    ],
    further=[
        '<a href="%s/thag1.20/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.19.html">Thag 1.19 &mdash; Kula</a> &mdash; '
        "the poem immediately before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.21 — Nigrodha
# --------------------------------------------------------------------------- #
page(
    1, 21, "Nigrodha", "Nigrodha",
    meta_title="Thag 1.21 — Nigrodha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Nigrodha's verse, opening Chapter Three with fearlessness "
        "grounded in the teacher's expertise in freedom from death. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse opening "
                    "Chapter Three"),
        ("Speaker", "Nigrodha, stating his own fearlessness directly"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "compact statement of fearlessness, grounded in "
                       "a specific reason"),
    ],
    why=(
        "Chapter Three opens with a direct claim: &lsquo;I'm not "
        "afraid of fear&rsquo;. But Nigrodha does not leave this "
        "unexplained &mdash; the reason follows immediately: "
        "&lsquo;our teacher is expert in freedom from death&rsquo;, "
        "and mendicants advance along a path where, in the end, "
        "&lsquo;no fear remains&rsquo;."),
    guide=[
        ("Fearlessness, immediately grounded in a reason", [
            "The verse's opening claim could stand alone as a simple "
            "boast, but its second line supplies the reason at once: "
            "not personal bravado, but confidence placed in the "
            "teacher's own expertise in &lsquo;freedom from "
            "death&rsquo; &mdash; amata, the deathless."]),
        ("A path defined by what it lacks", [
            "The verse's closing description names the path mendicants "
            "walk not by what it contains but by what it does not: "
            "&lsquo;where no fear remains&rsquo;. The destination is "
            "characterized as an absence, not an added quality."]),
        ("A short, declarative opener for a new chapter", [
            "Like Cūḷavaccha's joy opening Chapter Two, this verse "
            "opens Chapter Three with a single clear claim rather than "
            "an image or narrative &mdash; each of this book's chapters "
            "so far beginning on a plainly stated theme."]),
    ],
    terms=[
        ("bhaya",
         "&ldquo;fear&rdquo; &mdash; named twice in this short verse, "
         "denied at the start and again at the close."),
        ("satth&amacr;",
         "&ldquo;teacher&rdquo; &mdash; the source of the confidence "
         "this verse expresses, rather than personal bravado."),
        ("amata",
         "&ldquo;the deathless&rdquo; or &ldquo;freedom from "
         "death&rdquo; &mdash; the specific expertise credited to the "
         "teacher."),
        ("bhikkhu",
         "&ldquo;mendicant&rdquo; &mdash; those said to advance along "
         "the path this verse describes."),
        ("magga",
         "&ldquo;path&rdquo; &mdash; defined in this verse's closing "
         "line by what it lacks, not what it contains."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.21:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this verse open?",
         "opts": [
             "With a description of a hut",
             "With a direct claim: I'm not afraid of fear",
             "With a question addressed to the Buddha",
             "With a list of other monks"],
         "correct": 1,
         "expl": "Chapter Three's opening statement."},
        {"q": "What reason does the verse give for this fearlessness?",
         "opts": [
             "No reason is given",
             "Personal bravery alone",
             "The teacher's expertise in freedom from death",
             "Wealth and status"],
         "correct": 2,
         "expl": "Confidence placed in the teacher, not personal boldness."},
        {"q": "What does 'amata' mean?",
         "opts": [
             "A type of hut",
             "A monastic robe",
             "A river",
             "The deathless, or freedom from death"],
         "correct": 3,
         "expl": "The teacher's specific expertise, named in the verse's second line."},
        {"q": "How does the verse describe the path mendicants walk?",
         "opts": [
             "By what it contains",
             "By what it lacks: a place where no fear remains",
             "As dangerous and uncertain",
             "The path is not described"],
         "correct": 1,
         "expl": "Defined as an absence, not an added quality."},
        {"q": "How does this poem's opening compare to Cūḷavaccha's verse opening Chapter Two?",
         "opts": [
             "They are identical in wording",
             "Cūḷavaccha's verse opens with a question instead",
             "There is no similarity at all",
             "Both open their chapters with a single clear claim"],
         "correct": 3,
         "expl": "A shared pattern across this book's chapter openers."},
        {"q": "What does 'satthā' mean?",
         "opts": [
             "Teacher",
             "Enemy",
             "River",
             "Forest"],
         "correct": 0,
         "expl": "The source of the confidence expressed in this verse."},
        {"q": "How many times is 'fear' (bhaya) named in this verse?",
         "opts": [
             "Not at all",
             "Once",
             "Twice",
             "Four times"],
         "correct": 2,
         "expl": "Denied at the verse's start and again at its close."},
        {"q": "What does 'magga' mean?",
         "opts": [
             "Path",
             "Fear",
             "A monastic title",
             "A type of food"],
         "correct": 0,
         "expl": "What mendicants are said to advance along."},
        {"q": "Is this verse's fearlessness attributed to personal bravado?",
         "opts": [
             "Yes, entirely to personal bravado",
             "No — it is attributed to confidence in the teacher's expertise",
             "The verse does not explain its source",
             "Yes, and to wealth as well"],
         "correct": 1,
         "expl": "A reason given immediately, not left as an unsupported boast."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "It opens Chapter Three, the Book of the Ones' third chapter",
             "It closes the entire collection",
             "It is not part of the Book of the Ones",
             "It opens Chapter One"],
         "correct": 0,
         "expl": "The first of ten poems in this new chapter."},
    ],
    marginalia=[
        ("A claim, immediately grounded", [
            "not afraid —",
            "because the teacher knows"
        ]),
        ("The deathless, named directly", [
            "amata,",
            "freedom from death"
        ]),
        ("A path defined by absence", [
            "not what it holds,",
            "but what it lacks"
        ]),
        ("A new chapter, a clear claim", [
            "opening plainly,",
            "as Chapter Two also did"
        ]),
    ],
    further=[
        '<a href="%s/thag1.21/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.20.html">Thag 1.20 &mdash; Ajita</a> &mdash; '
        "the poem immediately before this one, closing Chapter Two.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.22 — Cittaka
# --------------------------------------------------------------------------- #
page(
    1, 22, "Cittaka", "Cittaka",
    meta_title="Thag 1.22 — Cittaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Cittaka's verse, blue-necked peacocks playing in a cool "
        "breeze whose cries wake the sleeper to practice absorption. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 2 of 10",
    glance=[
        ("Setting", "Karaṁvī, where crested peacocks cry out in a "
                    "cool breeze"),
        ("Speaker", "An unnamed voice describing the peacocks and "
                    "their effect"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "vivid nature imagery given a specific "
                       "practical purpose"),
    ],
    why=(
        "Crested peacocks with beautiful blue necks cry out at "
        "Karaṁvī, playing in a cool breeze &mdash; and their cries, "
        "this verse says, &lsquo;wake the sleeper to practice "
        "absorption&rsquo;. Unlike Vanavaccha's nature poem in Chapter "
        "Two, admired purely for its own sake, this scene is given a "
        "direct practical function."),
    guide=[
        ("Nature imagery given a purpose", [
            "Vanavaccha's rocky crags, cool streams, and ladybugs in "
            "Chapter Two closed simply in delight: &lsquo;these rocky "
            "crags delight me!&rsquo;. Here, comparably vivid imagery "
            "&mdash; crested peacocks, blue necks, a cool breeze "
            "&mdash; serves a stated end: rousing a sleeping meditator "
            "to practice."]),
        ("Peacocks at play, not merely present", [
            "The verse describes the peacocks as sītavātakīḷitā, "
            "&lsquo;playing in the cool breeze&rsquo; &mdash; a livelier "
            "image than simply being stirred by wind, giving the birds "
            "themselves an active, almost joyful role in the scene."]),
        ("A short chain from breeze to practice", [
            "The verse traces a small causal sequence: a cool breeze "
            "moves the peacocks to play, their play produces cries, "
            "and those cries wake a sleeper into meditative absorption "
            "&mdash; an ordinary natural event given a spiritual "
            "outcome."]),
    ],
    terms=[
        ("mora",
         "&ldquo;peacock&rdquo; &mdash; the verse's central image, "
         "described as crested and blue-necked."),
        ("n&imacr;l&amacr; sug&imacr;v&amacr;",
         "&ldquo;blue-necked&rdquo; &mdash; the descriptive compound "
         "opening this verse."),
        ("s&imacr;tav&amacr;tak&imacr;&#7735;it&amacr;",
         "&ldquo;playing in the cool breeze&rdquo; &mdash; describing "
         "the peacocks' lively activity, not mere passive stirring."),
        ("suttaṁ",
         "&ldquo;the sleeper&rdquo; &mdash; the one roused by the "
         "peacocks' cries."),
        ("nibodhenti",
         "&ldquo;they wake&rdquo; or &ldquo;they rouse&rdquo; &mdash; "
         "the verb naming this verse's stated outcome."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.22:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse describe?",
         "opts": [
             "Peacocks whose cries wake a sleeper to practice absorption",
             "A dispute between monks",
             "A meal in a village",
             "A journey across a river"],
         "correct": 0,
         "expl": "Vivid nature imagery given a direct practical purpose."},
        {"q": "How does this verse's use of nature differ from Vanavaccha's poem in Chapter Two?",
         "opts": [
             "Vanavaccha's poem also describes peacocks",
             "This verse gives the scene a stated practical function, rather than pure delight",
             "There is no difference at all",
             "This verse contains no nature imagery"],
         "correct": 1,
         "expl": "A function added to imagery that in Chapter Two stood on its own."},
        {"q": "How does the verse describe the peacocks' activity in the breeze?",
         "opts": [
             "As merely stirred, passively",
             "As sleeping",
             "As playing, actively and almost joyfully",
             "The verse does not describe their activity"],
         "correct": 2,
         "expl": "A livelier image than simple passive movement."},
        {"q": "What effect do the peacocks' cries have, according to the verse?",
         "opts": [
             "They frighten nearby animals",
             "They cause a storm",
             "No effect is described",
             "They wake a sleeper to practice absorption"],
         "correct": 3,
         "expl": "The verse's stated outcome."},
        {"q": "What sequence does the verse trace, from cause to spiritual result?",
         "opts": [
             "A river floods a field",
             "A breeze moves the peacocks to play, producing cries that wake a sleeper",
             "A fire spreads through a forest",
             "No sequence is traced"],
         "correct": 1,
         "expl": "An ordinary natural chain leading to a spiritual outcome."},
        {"q": "What color is emphasized in the verse's opening description?",
         "opts": [
             "Blue",
             "Red",
             "Gold",
             "Black"],
         "correct": 0,
         "expl": "The peacocks' necks, named directly."},
        {"q": "What does 'nibodhenti' mean?",
         "opts": [
             "They sleep",
             "They flee",
             "They sing",
             "They wake or rouse"],
         "correct": 3,
         "expl": "The verb naming this verse's stated effect."},
        {"q": "Where is this scene set, according to the verse?",
         "opts": [
             "In a royal palace",
             "At Karaṁvī",
             "By the ocean",
             "In a city market"],
         "correct": 1,
         "expl": "Named directly as the verse's setting."},
        {"q": "What does 'suttaṁ' refer to in this verse?",
         "opts": [
             "The sleeper roused by the peacocks' cries",
             "A type of robe",
             "A river",
             "A monastic title"],
         "correct": 0,
         "expl": "The one whose practice this verse's scene serves."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "The second poem, following Nigrodha's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Nature, given a purpose", [
            "not delight alone —",
            "a call to practice"
        ]),
        ("Playing, not merely stirred", [
            "peacocks at play",
            "in the cool breeze"
        ]),
        ("A chain from breeze to practice", [
            "breeze, play, cry,",
            "then waking"
        ]),
        ("Blue necks, a named place", [
            "crested peacocks,",
            "at Karaṁvī"
        ]),
    ],
    further=[
        '<a href="%s/thag1.22/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.21.html">Thag 1.21 &mdash; Nigrodha</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.23 — Gos&amacr;la
# --------------------------------------------------------------------------- #
page(
    1, 23, "Gos&amacr;la", "Gos&amacr;la",
    meta_title="Thag 1.23 — Gosāla | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Gosāla's verse, an ordinary day's plan &mdash; a meal, "
        "dexterous contemplation, and a return to seclusion &mdash; "
        "voiced as verse. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 3 of 10",
    glance=[
        ("Setting", "Veḷugumba, where Gosāla plans to eat, then his "
                    "forest hill, where he plans to return"),
        ("Speaker", "Gosāla, stating his own plans for the day"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "ordinary logistics voiced as verse, with one "
                       "noted wordplay"),
    ],
    why=(
        "Gosāla's verse reads almost like a plan for the day: eat "
        "honey and milk-rice at Veḷugumba, then, dexterously probing "
        "the rise and fall of the aggregates, return to his forest "
        "hill to foster seclusion &mdash; ordinary logistics and "
        "meditative practice folded into the same short itinerary."),
    guide=[
        ("Ordinary planning, voiced as verse", [
            "Where many verses in this collection describe an "
            "attainment or a teaching, this one states something "
            "closer to a plan: a specific meal at a specific place, "
            "then a specific destination &mdash; the stuff of daily "
            "monastic life, given the same verse form as loftier "
            "declarations."]),
        ("A wordplay Sujato's note unpacks", [
            "&lsquo;Dexterously probing&rsquo; translates padakkhiṇaṁ "
            "sammasanto. Sujato's note explains that padakkhiṇaṁ is "
            "used here adverbially, its sense reinforcing the rare "
            "verb sammasanto through a shared root: dakkha means "
            "&lsquo;right-handed, dexterous&rsquo;, while mas means "
            "&lsquo;stroke, probe&rsquo; &mdash; a deliberate echo "
            "built into the line's own sound."]),
        ("Meditation folded into an itinerary", [
            "The contemplation itself &mdash; the rise and fall of the "
            "aggregates &mdash; is not set apart as a separate, formal "
            "occasion, but placed directly between a meal and a walk "
            "home, practice woven into the ordinary movement of a "
            "day."]),
    ],
    terms=[
        ("madhup&amacr;yasa",
         "&ldquo;honey and milk-rice&rdquo; &mdash; the specific meal "
         "Gosāla names in this verse's opening line."),
        ("padakkhi&#7751;a&#7745;",
         "used adverbially here as &ldquo;dexterously&rdquo;, per "
         "Sujato's note reinforcing the following verb through a "
         "shared root."),
        ("sammasanto",
         "&ldquo;probing&rdquo; or &ldquo;contemplating&rdquo; "
         "&mdash; a rare verb, per Sujato's note, describing how "
         "Gosāla examines the aggregates."),
        ("khandh&amacr;na&#7745; udayabbaya&#7745;",
         "&ldquo;the rise and fall of the aggregates&rdquo; &mdash; "
         "the specific object of Gosāla's contemplation."),
        ("viveka",
         "&ldquo;seclusion&rdquo; &mdash; what Gosāla says he will "
         "foster upon returning to his forest hill."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.23:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does Gosāla say he will eat, and where?",
         "opts": [
             "Rice porridge, in the village",
             "Honey and milk-rice, at Veḷugumba",
             "Fruit, by a river",
             "Nothing is mentioned about food"],
         "correct": 1,
         "expl": "The verse's opening, stated plan."},
        {"q": "What does Gosāla plan to do after his meal?",
         "opts": [
             "Nothing further is planned",
             "Teach a large assembly",
             "Probe the rise and fall of the aggregates, then return to his forest hill",
             "Travel to a distant kingdom"],
         "correct": 2,
         "expl": "The rest of the verse's stated itinerary."},
        {"q": "According to Sujato's note, what does 'padakkhiṇaṁ' do in this verse?",
         "opts": [
             "Nothing in particular",
             "It reinforces the rare verb sammasanto through a shared root, dakkha",
             "It names a specific place",
             "It contradicts the rest of the verse"],
         "correct": 1,
         "expl": "A deliberate sound-based echo built into the line."},
        {"q": "What does 'khandhānaṁ udayabbayaṁ' mean?",
         "opts": [
             "The rise and fall of the aggregates",
             "A type of meal",
             "A monastic robe",
             "A river crossing"],
         "correct": 0,
         "expl": "The specific object of Gosāla's contemplation."},
        {"q": "How does this verse's style compare to declarations of attainment elsewhere in this collection?",
         "opts": [
             "It reads more like an ordinary plan for the day",
             "It is identical in style to every other verse",
             "It contains no practical detail at all",
             "It describes no destination or activity"],
         "correct": 0,
         "expl": "Daily logistics given the same verse form as loftier declarations."},
        {"q": "Where is Gosāla's meal, according to the verse?",
         "opts": [
             "In a royal palace",
             "By the ocean",
             "In a city market",
             "At Veḷugumba"],
         "correct": 3,
         "expl": "Named directly in the verse's opening line."},
        {"q": "What does 'sammasanto' mean?",
         "opts": [
             "Sleeping",
             "Probing or contemplating",
             "Building",
             "Fighting"],
         "correct": 1,
         "expl": "A rare verb, per Sujato's note, describing how Gosāla examines the aggregates."},
        {"q": "Where does the verse say Gosāla will return to?",
         "opts": [
             "A royal court",
             "His birthplace",
             "A river crossing",
             "His forest hill"],
         "correct": 3,
         "expl": "Named as his destination after the meal and contemplation."},
        {"q": "How is the contemplation of the aggregates positioned within this verse?",
         "opts": [
             "Folded directly into the itinerary, between a meal and a walk home",
             "As a separate, formal occasion set apart from daily life",
             "It is not mentioned at all",
             "As something Gosāla refuses to do"],
         "correct": 0,
         "expl": "Practice woven into the ordinary movement of a day."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The third poem, following Cittaka's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A plan for the day, in verse", [
            "a meal, then",
            "contemplation, then home"
        ]),
        ("A wordplay, noted", [
            "dakkha,",
            "echoed in sound"
        ]),
        ("Practice, folded into an itinerary", [
            "not set apart,",
            "but woven in"
        ]),
        ("Honey-rice, then the forest hill", [
            "ordinary logistics,",
            "spoken as verse"
        ]),
    ],
    further=[
        '<a href="%s/thag1.23/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.22.html">Thag 1.22 &mdash; Cittaka</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.24 — Sugandha
# --------------------------------------------------------------------------- #
page(
    1, 24, "Sugandha", "Sugandha",
    meta_title="Thag 1.24 — Sugandha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sugandha's verse, an exclamation over the teaching's "
        "excellence after attaining the three knowledges in a single "
        "rainy season. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative setting; a short exclamatory verse "
                    "about a fast attainment"),
        ("Speaker", "Sugandha, speaking of his own rapid progress"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a compact claim of exceptionally fast "
                       "attainment"),
    ],
    why=(
        "Sugandha opens with an exclamation, not a boast about "
        "himself directly: &lsquo;see the excellence of the "
        "teaching!&rsquo; Only then does he explain why &mdash; just "
        "one rainy season after going forth, he attained the three "
        "knowledges and fulfilled the Buddha's instructions."),
    guide=[
        ("An exclamation pointed outward, not inward", [
            "The verse's opening line does not say &lsquo;see my "
            "achievement&rsquo;; it says &lsquo;see the excellence of "
            "the teaching&rsquo;. Sugandha's own rapid progress is "
            "offered as evidence for the Dhamma's effectiveness, not "
            "simply as personal accomplishment."]),
        ("A specific, strikingly short timeframe", [
            "&lsquo;Just one rainy season after I went forth&rsquo; "
            "dates this attainment precisely: one full annual rains "
            "retreat, the traditional marker of a year's monastic "
            "seniority &mdash; an explicitly rapid timeline for "
            "reaching full liberation."]),
        ("A named formula, not left vague", [
            "&lsquo;The three knowledges&rsquo; names a specific, "
            "traditional set of attainments rather than a general "
            "claim of awakening &mdash; giving Sugandha's declaration "
            "a precise content, not only a triumphant tone."]),
    ],
    terms=[
        ("anuvassika",
         "&ldquo;after one rains-retreat&rdquo; or &ldquo;within one "
         "year&rdquo; &mdash; the specific timeframe this verse "
         "claims."),
        ("dhammasudhammat&amacr;",
         "&ldquo;the true excellence of the teaching&rdquo; &mdash; "
         "what Sugandha invites the reader to see."),
        ("tisso vijj&amacr;",
         "&ldquo;the three knowledges&rdquo; &mdash; a traditional "
         "formula of specific attainments, named directly rather than "
         "left as a vague claim of awakening."),
        ("pabbajita",
         "&ldquo;gone forth&rdquo; &mdash; describing Sugandha's own "
         "ordination, the starting point for this verse's timeframe."),
        ("s&amacr;sana",
         "&ldquo;instructions&rdquo; or &ldquo;dispensation&rdquo; "
         "&mdash; what Sugandha says he has fulfilled."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.24:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's opening line invite the reader to see?",
         "opts": [
             "Sugandha's own achievement, described directly",
             "A beautiful landscape",
             "Nothing in particular",
             "The excellence of the teaching"],
         "correct": 3,
         "expl": "Pointed outward to the Dhamma, not simply at himself."},
        {"q": "How long after going forth does Sugandha say he attained the three knowledges?",
         "opts": [
             "Many years",
             "Just one rainy season",
             "A single day",
             "The verse does not specify"],
         "correct": 1,
         "expl": "An explicitly rapid, precisely dated timeline."},
        {"q": "What does 'tisso vijjā' refer to?",
         "opts": [
             "A monastic robe",
             "A type of meal",
             "The three knowledges, a traditional formula of attainments",
             "A geographic region"],
         "correct": 2,
         "expl": "A specific, named set of attainments, not a vague claim."},
        {"q": "What does Sugandha say he has fulfilled?",
         "opts": [
             "The Buddha's instructions",
             "A local custom",
             "A family obligation",
             "Nothing is mentioned"],
         "correct": 0,
         "expl": "The verse's closing claim."},
        {"q": "Is this verse's opening exclamation framed as pointing to Sugandha himself or to the teaching?",
         "opts": [
             "To Sugandha's own cleverness",
             "To another named monk",
             "To the teaching's excellence",
             "To neither"],
         "correct": 2,
         "expl": "His own progress offered as evidence for the Dhamma's effectiveness."},
        {"q": "What does 'anuvassika' mean?",
         "opts": [
             "After one rains-retreat, or within one year",
             "After many decades",
             "Before ordination",
             "A type of hut"],
         "correct": 0,
         "expl": "The specific timeframe this verse claims for Sugandha's attainment."},
        {"q": "What does 'pabbajita' mean?",
         "opts": [
             "Gone forth, ordained",
             "Returned home",
             "Ill",
             "Wealthy"],
         "correct": 0,
         "expl": "Describing Sugandha's own ordination, the starting point for this verse's timeframe."},
        {"q": "How does this verse's tone compare to a simple boast?",
         "opts": [
             "It is identical to a simple boast",
             "It frames personal progress as testimony for the teaching's effectiveness",
             "It contains no claim of attainment at all",
             "It denies any attainment occurred"],
         "correct": 1,
         "expl": "Personal speed offered as evidence, not celebrated for its own sake."},
        {"q": "What does 'sāsana' mean?",
         "opts": [
             "A river",
             "Instructions or dispensation",
             "A type of food",
             "A monastic building"],
         "correct": 1,
         "expl": "What Sugandha says he has fulfilled."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The fourth poem, following Gosāla's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Pointed outward, not inward", [
            "'see the teaching,'",
            "not 'see my success'"
        ]),
        ("One year, not many", [
            "just one",
            "rainy season"
        ]),
        ("A named formula", [
            "the three",
            "knowledges"
        ]),
        ("Speed as testimony", [
            "his own progress,",
            "offered as evidence"
        ]),
    ],
    further=[
        '<a href="%s/thag1.24/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.23.html">Thag 1.23 &mdash; Gos&amacr;la</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.25 — Nandiya
# --------------------------------------------------------------------------- #
page(
    1, 25, "Nandiya", "Nandiya",
    meta_title="Thag 1.25 — Nandiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Nandiya's verse, addressing Māra directly and warning him of "
        "the consequence of attacking a monk whose mind is full of "
        "light. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a direct address to the "
                    "&lsquo;Dark One&rsquo;"),
        ("Speaker", "Nandiya, warning Māra of a consequence rather "
                    "than declaring his own victory"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "direct warning addressed to Māra, in place of "
                       "a triumphant declaration"),
    ],
    why=(
        "Nandiya addresses Māra directly as &lsquo;Dark One&rsquo;: "
        "attack a monk &lsquo;who has arrived at the fruit&rsquo;, "
        "whose mind is &lsquo;always full of light&rsquo;, and "
        "&lsquo;you'll fall into suffering&rsquo;. Rather than "
        "declaring his own victory, the verse warns Māra of a "
        "consequence."),
    guide=[
        ("A direct address to Māra", [
            "&lsquo;Kaṇha&rsquo;, &lsquo;Dark One&rsquo;, is a direct "
            "vocative address to Māra &mdash; a confrontation with the "
            "tempter figure that recurs at several points across this "
            "site's translations, most often in the Therīgātha, now "
            "appearing here in the Theragātha as well."]),
        ("A warning of consequence, not a claim of victory", [
            "Many Māra-confrontation verses culminate in the speaker "
            "declaring their own triumph directly. This one instead "
            "stays focused on Māra's own fate: &lsquo;you'll fall into "
            "suffering&rsquo; is framed as a prediction and a warning, "
            "not a celebration of personal victory already won."]),
        ("The target described through light and attainment", [
            "The monk Māra is warned against is characterized in two "
            "ways: someone &lsquo;who has arrived at the fruit&rsquo; "
            "&mdash; a specific attainment &mdash; and whose mind is "
            "&lsquo;always full of light&rsquo;, an image of radiance "
            "rather than a list of qualities or practices."]),
    ],
    terms=[
        ("ka&#7751;ha",
         "&ldquo;Dark One&rdquo; &mdash; the direct vocative address "
         "to Māra opening this verse."),
        ("phalaga",
         "&ldquo;arrived at the fruit&rdquo; &mdash; describing the "
         "monk's specific attainment."),
        ("obh&amacr;saj&amacr;ta",
         "&ldquo;full of light&rdquo; or &ldquo;born of "
         "radiance&rdquo; &mdash; describing this monk's mind."),
        ("&amacr;sajja",
         "&ldquo;having attacked&rdquo; or &ldquo;having "
         "assaulted&rdquo; &mdash; the action this verse warns Māra "
         "against."),
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; the consequence this verse "
         "predicts for Māra."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.25:1.1-1.4"),
    ],
    quiz=[
        {"q": "Who does this verse address directly?",
         "opts": [
             "The Buddha",
             "Another monk",
             "A village elder",
             "Māra, called 'Dark One'"],
         "correct": 3,
         "expl": "A direct vocative confrontation."},
        {"q": "What does the verse warn Māra will happen if he attacks this monk?",
         "opts": [
             "He will fall into suffering",
             "Nothing in particular",
             "He will gain great power",
             "He will become the monk's teacher"],
         "correct": 0,
         "expl": "A predicted consequence, named directly."},
        {"q": "Does the verse focus on the speaker's own declared victory, or on Māra's fate?",
         "opts": [
             "On the speaker's own declared victory",
             "On neither",
             "On a third, unnamed party",
             "On Māra's fate, as a warning"],
         "correct": 3,
         "expl": "A warning of consequence, not a triumphant proclamation."},
        {"q": "How is the monk Māra is warned against described?",
         "opts": [
             "As weak and untrained",
             "As arrived at the fruit, with a mind always full of light",
             "As fearful and doubting",
             "The verse gives no description"],
         "correct": 1,
         "expl": "Characterized through attainment and an image of radiance."},
        {"q": "What does 'kaṇha' mean?",
         "opts": [
             "Dark One",
             "Bright One",
             "Teacher",
             "Friend"],
         "correct": 0,
         "expl": "The direct address opening this verse, naming Māra."},
        {"q": "Where else on this site does a similar confrontation with Māra appear?",
         "opts": [
             "Nowhere else",
             "Only in the Khuddakapatha",
             "Most often in the Therīgātha",
             "Only in the Cariyapitaka"],
         "correct": 2,
         "expl": "A recurring motif across this site's translations, now appearing here too."},
        {"q": "What does 'obhāsajāta' describe?",
         "opts": [
             "A type of hut",
             "A mind full of light",
             "A monastic robe",
             "A river"],
         "correct": 1,
         "expl": "Describing the targeted monk's mind."},
        {"q": "What does 'phalaga' mean?",
         "opts": [
             "Fearful",
             "Arrived at the fruit",
             "Still training",
             "Wealthy"],
         "correct": 1,
         "expl": "The specific attainment named for this monk."},
        {"q": "What does 'āsajja' describe?",
         "opts": [
             "Having attacked or assaulted",
             "Having taught",
             "Having traveled",
             "Having eaten"],
         "correct": 0,
         "expl": "The action this verse warns Māra against."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The fifth poem, following Sugandha's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A direct address to Māra", [
            "'Dark One,'",
            "spoken to his face"
        ]),
        ("A warning, not a boast", [
            "not 'I have won,'",
            "but 'you will suffer'"
        ]),
        ("Light, not a list of qualities", [
            "a mind",
            "always full of light"
        ]),
        ("A motif recurring across the site", [
            "Māra confronted,",
            "here and elsewhere"
        ]),
    ],
    further=[
        '<a href="%s/thag1.25/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.24.html">Thag 1.24 &mdash; Sugandha</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.26 — Abhaya
# --------------------------------------------------------------------------- #
page(
    1, 26, "Abhaya", "Abhaya",
    meta_title="Thag 1.26 — Abhaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Abhaya's verse, penetrating the subtle truth like a hair-tip "
        "pierced with an arrow, after hearing the Buddha's fine "
        "words. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse about "
                    "hearing and immediately penetrating truth"),
        ("Speaker", "Abhaya, describing his own moment of "
                    "understanding"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "famous precision simile compressed into two "
                       "lines"),
    ],
    why=(
        "Abhaya's verse compresses cause and effect into two steps: "
        "hearing the Buddha's fine words, then penetrating &lsquo;the "
        "subtle truth&rsquo; &mdash; described with one of this "
        "collection's most exact images, &lsquo;like a hair-tip with "
        "an arrow&rsquo;."),
    guide=[
        ("An epithet naming a traditional lineage", [
            "&lsquo;Kinsman of the Sun&rsquo; translates &amacr;dicca"
            "bandhu, a traditional epithet for the Buddha referring to "
            "the Sakyan clan's own claimed solar lineage &mdash; a "
            "title of ancestry rather than a description of his "
            "teaching itself."]),
        ("Precision measured against something nearly impossible to hit", [
            "&lsquo;Like a hair-tip with an arrow&rsquo; describes "
            "piercing something almost too fine a target to strike at "
            "all &mdash; not a general image of skill, but a specific "
            "measure of exactness applied to understanding a subtle "
            "truth."]),
        ("Hearing and penetrating, with no described interval", [
            "The verse moves directly from &lsquo;having heard&rsquo; "
            "to &lsquo;I penetrated&rsquo;, with no account of "
            "prolonged practice in between &mdash; a compressed "
            "cause-and-effect structure, unlike verses elsewhere in "
            "this collection that describe years or seasons of "
            "training."]),
    ],
    terms=[
        ("&amacr;diccabandhu",
         "&ldquo;Kinsman of the Sun&rdquo; &mdash; a traditional "
         "epithet for the Buddha, referring to the Sakyan clan's "
         "claimed solar lineage."),
        ("subh&amacr;sita",
         "&ldquo;fine words&rdquo; or &ldquo;well-spoken&rdquo; "
         "&mdash; describing what Abhaya heard."),
        ("nipu&#7751;a",
         "&ldquo;subtle&rdquo; &mdash; describing the truth Abhaya "
         "says he penetrated."),
        ("paccabyadhi",
         "&ldquo;pierced through&rdquo; &mdash; the verb naming this "
         "verse's central action."),
        ("v&amacr;lagga",
         "&ldquo;hair-tip&rdquo; &mdash; the verse's image of an "
         "almost impossibly precise target."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.26:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Abhaya say he did after hearing the Buddha's fine words?",
         "opts": [
             "He returned home",
             "He became a teacher of others",
             "He penetrated the subtle truth",
             "Nothing further happened"],
         "correct": 2,
         "expl": "The verse's central claim, following directly from hearing."},
        {"q": "What simile does the verse use for this penetration?",
         "opts": [
             "A river cutting through stone",
             "Like a hair-tip pierced with an arrow",
             "A fire consuming wood",
             "No simile is used"],
         "correct": 1,
         "expl": "An image of extreme, almost impossible precision."},
        {"q": "What does 'Ādiccabandhu' mean?",
         "opts": [
             "A type of monastic robe",
             "A specific meditation technique",
             "A geographic region",
             "Kinsman of the Sun, an epithet for the Buddha"],
         "correct": 3,
         "expl": "Referring to the Sakyan clan's claimed solar lineage."},
        {"q": "How much time passes between hearing and penetrating, according to the verse?",
         "opts": [
             "No interval is described at all",
             "Many years are described",
             "Several decades",
             "A full lifetime"],
         "correct": 0,
         "expl": "A compressed structure, unlike verses describing prolonged practice."},
        {"q": "What does 'nipuṇa' describe?",
         "opts": [
             "A type of hut",
             "A monastic title",
             "The truth Abhaya penetrated, called subtle",
             "A river"],
         "correct": 2,
         "expl": "Named directly as the object of Abhaya's penetration."},
        {"q": "What kind of image is 'a hair-tip pierced with an arrow'?",
         "opts": [
             "A specific measure of nearly impossible exactness",
             "A vague, general image of skill",
             "An image of failure",
             "An image unrelated to precision"],
         "correct": 0,
         "expl": "A precise, almost impossibly fine target."},
        {"q": "What does 'subhāsita' mean?",
         "opts": [
             "Fine words, or well-spoken",
             "Harsh words",
             "Silence",
             "A written text"],
         "correct": 0,
         "expl": "Describing what Abhaya heard from the Buddha."},
        {"q": "What does 'paccabyadhi' mean?",
         "opts": [
             "Fled",
             "Pierced through",
             "Slept",
             "Built"],
         "correct": 1,
         "expl": "The verb naming this verse's central action."},
        {"q": "How does this verse's structure compare to verses describing years of training?",
         "opts": [
             "It is identical, describing many years",
             "It describes no cause at all",
             "It describes a much longer process than any other verse",
             "It compresses cause and effect into two immediate steps"],
         "correct": 3,
         "expl": "Hearing and penetrating, with no described interval between."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "The sixth poem, following Nandiya's",
             "It closes the chapter",
             "It is not part of this chapter"],
         "correct": 1,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Hearing, then penetrating", [
            "no interval",
            "described between"
        ]),
        ("An almost impossible target", [
            "a hair-tip,",
            "pierced by an arrow"
        ]),
        ("An epithet of lineage", [
            "Kinsman of the Sun,",
            "not of teaching"
        ]),
        ("Subtlety, precisely struck", [
            "the subtle truth,",
            "penetrated exactly"
        ]),
    ],
    further=[
        '<a href="%s/thag1.26/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.25.html">Thag 1.25 &mdash; Nandiya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.27 — Lomasaka&#7749;giya
# --------------------------------------------------------------------------- #
page(
    1, 27, "Lomasaka&#7749;giya", "Lomasaka&#7749;giya",
    meta_title="Thag 1.27 — Lomasakaṅgiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Lomasakaṅgiya's verse, thrusting aside grasses, vines, "
        "reeds, and creepers with his own chest to foster seclusion. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 7 of 10",
    glance=[
        ("Setting", "Dense undergrowth &mdash; grasses, vines, reeds, "
                    "and creepers &mdash; being physically pushed "
                    "aside"),
        ("Speaker", "Lomasakaṅgiya, describing his own determined "
                    "physical effort"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "concrete, physical image of determination"),
    ],
    why=(
        "Lomasakaṅgiya's verse is entirely physical: &lsquo;with my "
        "chest I'll thrust aside the grasses, vines, reeds and "
        "creepers&rsquo;, using his own body as the tool for pushing "
        "into seclusion, rather than describing determination in "
        "abstract terms."),
    guide=[
        ("Determination stated as bodily action", [
            "Rather than saying he will overcome obstacles in a "
            "general sense, Lomasakaṅgiya specifies exactly how: "
            "&lsquo;with my chest&rsquo;, physically forcing his way "
            "through undergrowth &mdash; determination given a "
            "concrete, bodily form."]),
        ("Four named plants, not a generic tangle", [
            "Grasses, vines, reeds, and creepers are named one after "
            "another rather than lumped together as simply "
            "&lsquo;undergrowth&rsquo; &mdash; an itemized, almost "
            "naturalist's list of what stands between him and "
            "seclusion."]),
        ("A closing line shared word for word with Gosāla's verse", [
            "This verse's closing phrase, &lsquo;fostering "
            "seclusion&rsquo;, matches Gosāla's verse (Thag 1.23) "
            "exactly in the Pali &mdash; vivekamanubrūhayaṁ &mdash; "
            "even though the two verses lead up to it in entirely "
            "different ways: Gosāla by way of a meal and quiet "
            "contemplation, Lomasakaṅgiya by way of physically forcing "
            "through undergrowth."]),
    ],
    terms=[
        ("ura",
         "&ldquo;chest&rdquo; &mdash; the body part Lomasakaṅgiya "
         "names as his tool for pushing through undergrowth."),
        ("panudissāmi",
         "&ldquo;I will thrust aside&rdquo; or &ldquo;I will push "
         "away&rdquo; &mdash; this verse's central verb."),
        ("kusa",
         "&ldquo;grass&rdquo; &mdash; the first of four plants named "
         "in this verse."),
        ("mu&ntilde;japabbaja",
         "&ldquo;reeds and rushes&rdquo; &mdash; among the plants "
         "named as obstacles in this verse."),
        ("vivekamanubr&umacr;haya&#7745;",
         "&ldquo;fostering seclusion&rdquo; &mdash; this verse's "
         "closing phrase, matching Gosāla's verse (Thag 1.23) exactly "
         "in the Pali."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.27:1.1-1.4"),
    ],
    quiz=[
        {"q": "What body part does Lomasakaṅgiya say he uses to push through undergrowth?",
         "opts": [
             "His hands",
             "His feet",
             "No body part is mentioned",
             "His chest"],
         "correct": 3,
         "expl": "A concrete, physical image rather than an abstract claim of determination."},
        {"q": "How many specific plants does the verse name?",
         "opts": [
             "None — it names only 'undergrowth' generally",
             "One",
             "Four: grasses, vines, reeds, and creepers",
             "Ten"],
         "correct": 2,
         "expl": "An itemized, naturalist's list rather than a generic tangle."},
        {"q": "What does this verse's closing phrase, 'fostering seclusion', match exactly?",
         "opts": [
             "Nothing — the phrase is unique to this verse",
             "Gosāla's verse (Thag 1.23), word for word in the Pali",
             "A phrase from the Therīgātha",
             "A phrase used in every poem in this chapter"],
         "correct": 1,
         "expl": "The exact same closing Pali phrase, vivekamanubrūhayaṁ."},
        {"q": "How do Gosāla's and Lomasakaṅgiya's verses differ in how they lead up to their shared closing phrase?",
         "opts": [
             "They are completely identical throughout",
             "Both describe the exact same journey",
             "Gosāla describes a meal and contemplation; Lomasakaṅgiya describes physically forcing through undergrowth",
             "Neither verse describes any activity"],
         "correct": 2,
         "expl": "Two very different paths to the same closing line."},
        {"q": "What does 'panudissāmi' mean?",
         "opts": [
             "I will thrust aside or push away",
             "I will sleep",
             "I will teach",
             "I will eat"],
         "correct": 0,
         "expl": "This verse's central verb, describing his physical action."},
        {"q": "How is Lomasakaṅgiya's determination expressed in this verse?",
         "opts": [
             "In purely abstract terms",
             "As a specific, bodily action",
             "The verse does not express any determination",
             "As a question rather than a statement"],
         "correct": 1,
         "expl": "Determination given a concrete, physical form."},
        {"q": "What does 'kusa' mean?",
         "opts": [
             "Grass",
             "A river",
             "A monastic robe",
             "A type of hut"],
         "correct": 0,
         "expl": "The first of four plants named in this verse."},
        {"q": "What does 'muñjapabbaja' refer to?",
         "opts": [
             "Reeds and rushes",
             "A type of food",
             "A monastic title",
             "A body of water"],
         "correct": 0,
         "expl": "Among the plants named as obstacles in this verse."},
        {"q": "What is Lomasakaṅgiya's stated goal in pushing through this undergrowth?",
         "opts": [
             "To find food",
             "To foster seclusion",
             "To build a shelter",
             "To meet another monk"],
         "correct": 1,
         "expl": "The verse's closing purpose."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The seventh poem, following Abhaya's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Determination, made physical", [
            "'with my chest,'",
            "not just resolve"
        ]),
        ("Four plants, named one by one", [
            "grasses, vines,",
            "reeds, creepers"
        ]),
        ("A closing line, shared exactly", [
            "the same Pali phrase",
            "as Gosāla's verse"
        ]),
        ("Two paths, one destination", [
            "a meal and a walk,",
            "or a chest pushing through"
        ]),
    ],
    further=[
        '<a href="%s/thag1.27/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.26.html">Thag 1.26 &mdash; Abhaya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.28 — Jambug&amacr;mikaputta
# --------------------------------------------------------------------------- #
page(
    1, 28, "Jambug&amacr;mikaputta", "Jambug&amacr;mikaputta",
    meta_title="Thag 1.28 — Jambugāmikaputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Jambugāmikaputta's verse, three rhetorical questions ruling "
        "out vanity and affirming the scent of virtue instead. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative setting; three rhetorical questions "
                    "addressed to an unnamed &lsquo;you&rsquo;"),
        ("Speaker", "Jambugāmikaputta; the text does not name who he "
                    "addresses"),
        ("Form", "One four-line verse, entirely in the form of "
                 "rhetorical questions"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734; &mdash; a "
                       "verse built entirely from rhetorical questions, "
                       "with its addressee left unnamed"),
    ],
    why=(
        "This verse is built from three rhetorical questions: "
        "&lsquo;aren't you obsessed with clothes? Don't you just love "
        "jewelry? Is it not you&mdash;and no-one else&mdash;who "
        "spreads the scent of virtue?&rsquo; The text never names who "
        "is being addressed, though the pattern of self-address "
        "elsewhere nearby in this chapter makes a self-examination "
        "reading the most natural one."),
    guide=[
        ("Rhetorical questions with no named addressee", [
            "Unlike verses that clearly quote another speaker (as in "
            "Sīvaka's poem in Chapter Two) or clearly address the "
            "self by name (as in the poem immediately after this "
            "one), this verse's &lsquo;you&rsquo; is never identified "
            "&mdash; the questions stand without a stated target."]),
        ("A plausible reading as self-examination", [
            "Given the pattern of self-address found elsewhere in "
            "this book &mdash; Dabba and Vīra naming themselves within "
            "their own verses, Hārita addressed directly by name in "
            "the very next poem &mdash; the most natural reading here "
            "is that Jambugāmikaputta questions himself, rhetorically "
            "ruling out vanity and affirming that he himself, not "
            "ornament, is what carries virtue's scent. This guide "
            "offers that reading without asserting it as certain."]),
        ("Virtue described through the language of scent", [
            "The verse's final line uses fragrance as its image for "
            "ethical conduct: &lsquo;the scent of virtue&rsquo;, "
            "contrasted directly against the external adornment of "
            "clothes and jewelry named in the two lines before it."]),
    ],
    terms=[
        ("vatthapasuta",
         "&ldquo;obsessed with clothes&rdquo; &mdash; the first "
         "vanity this verse's questions rule out."),
        ("bh&umacr;san&amacr;rata",
         "&ldquo;delighting in jewelry&rdquo; or &ldquo;loving "
         "ornaments&rdquo; &mdash; the second vanity named."),
        ("s&imacr;lamaya gandha",
         "&ldquo;the scent made of virtue&rdquo; &mdash; ethical "
         "conduct described through the image of fragrance."),
        ("netar&amacr; paj&amacr;",
         "&ldquo;no other people&rdquo; &mdash; emphasizing that it is "
         "specifically this &lsquo;you&rsquo;, and no one else, who "
         "carries this scent."),
        ("v&amacr;yati",
         "&ldquo;diffuses&rdquo; or &ldquo;emits&rdquo; &mdash; the "
         "verb describing how this scent spreads."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.28:1.1-1.4"),
    ],
    quiz=[
        {"q": "How is this verse structured?",
         "opts": [
             "As a narrative with named characters",
             "As a numerical formula",
             "As a description of a landscape",
             "Entirely as three rhetorical questions"],
         "correct": 3,
         "expl": "No narrative detail — only questions."},
        {"q": "Does the text name who this verse addresses?",
         "opts": [
             "Yes, it names the Buddha directly",
             "No — the addressee is never named in the text",
             "Yes, it names another monk",
             "Yes, it names a village elder"],
         "correct": 1,
         "expl": "An unnamed 'you' throughout."},
        {"q": "What two vanities does the verse's questions rule out?",
         "opts": [
             "Wealth and food",
             "Fear and doubt",
             "Obsession with clothes and love of jewelry",
             "Nothing is ruled out"],
         "correct": 2,
         "expl": "Named in the verse's first two questions."},
        {"q": "What does the verse's final question affirm instead?",
         "opts": [
             "That the addressee spreads the scent of virtue",
             "That the addressee is wealthy",
             "That the addressee should leave the monastery",
             "Nothing is affirmed"],
         "correct": 0,
         "expl": "The verse's closing rhetorical claim."},
        {"q": "Why does this guide suggest a self-examination reading is plausible, though not certain?",
         "opts": [
             "Because the text explicitly says so",
             "Because of the pattern of self-address found elsewhere nearby in this book",
             "Because a comment note confirms it directly",
             "There is no plausible reading offered"],
         "correct": 1,
         "expl": "An inference from context, not a claim stated in the text itself."},
        {"q": "What does 'sīlamaya gandha' mean?",
         "opts": [
             "The scent made of virtue",
             "A type of incense sold in markets",
             "A monastic robe",
             "A river"],
         "correct": 0,
         "expl": "Ethical conduct described through the image of fragrance."},
        {"q": "What does 'vatthapasuta' describe?",
         "opts": [
             "Being obsessed with clothes",
             "Being wealthy",
             "Being fearful",
             "Being a teacher"],
         "correct": 0,
         "expl": "The first vanity named in this verse's questions."},
        {"q": "What image does the verse use for virtue, in contrast to clothes and jewelry?",
         "opts": [
             "A blazing fire",
             "Scent or fragrance",
             "A flowing river",
             "A tall mountain"],
         "correct": 1,
         "expl": "Fragrance as the closing image, replacing literal ornament."},
        {"q": "What does 'netarā pajā' emphasize?",
         "opts": [
             "That everyone shares this quality equally",
             "That no one carries this scent",
             "Nothing in particular",
             "That specifically this 'you', and no one else, carries this scent"],
         "correct": 3,
         "expl": "A pointed emphasis on this one addressee, singled out."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The eighth poem, following Lomasakaṅgiya's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Questions, with no named target", [
            "'you' —",
            "never identified"
        ]),
        ("A guess, offered honestly", [
            "self-examination,",
            "read but not asserted"
        ]),
        ("Vanity, ruled out twice", [
            "not clothes,",
            "not jewelry"
        ]),
        ("Virtue, as a scent", [
            "spreading outward,",
            "carried by one person alone"
        ]),
    ],
    further=[
        '<a href="%s/thag1.28/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.27.html">Thag 1.27 &mdash; Lomasaka&#7749;'
        "giya</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.29 — H&amacr;rita (1st)
# --------------------------------------------------------------------------- #
page(
    1, 29, "H&amacr;rita", "H&amacr;rita (1st)",
    meta_title="Thag 1.29 — Hārita (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Hārita's verse, commanding himself by name to straighten his "
        "mind like a fletcher straightens an arrow, and break "
        "ignorance to bits. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting; a direct self-command"),
        ("Speaker", "Hārita, commanding himself by name"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "direct self-command, echoing an image from "
                       "earlier in this book"),
    ],
    why=(
        "Hārita commands himself directly, by name: &lsquo;straighten "
        "yourself, like a fletcher straightens an arrow&rsquo;, then "
        "&lsquo;when your mind is upright, Hārita, break ignorance to "
        "bits!&rsquo; &mdash; an imperative addressed to no one but "
        "himself."),
    guide=[
        ("A named, imperative self-command", [
            "Unlike Dabba or Vīra, whose verses praised them in the "
            "third person while still naming them within the verse, "
            "this poem addresses Hārita directly with commands: "
            "&lsquo;straighten yourself&rsquo;, &lsquo;break "
            "ignorance to bits&rsquo; &mdash; imperative, not "
            "descriptive."]),
        ("A fletcher simile echoing a poem two chapters earlier", [
            "&lsquo;Like a fletcher straightens an arrow&rsquo; nearly "
            "repeats the opening simile of Kula's verse (Thag 1.19) in "
            "Chapter Two &mdash; usukāra, &lsquo;fletcher&rsquo;, and "
            "tejana, &lsquo;arrow-shaft&rsquo;, both appearing in "
            "close to the same phrasing, a callback spanning two "
            "chapters rather than confined to one."]),
        ("Two commands, in sequence", [
            "The verse moves through a clear order: straighten the "
            "mind first, then break ignorance &mdash; discipline "
            "positioned as the precondition for the more decisive "
            "action that follows it."]),
    ],
    terms=[
        ("samunnamaya",
         "&ldquo;straighten&rdquo; or &ldquo;make upright&rdquo; "
         "&mdash; the verse's opening imperative."),
        ("usuk&amacr;ra",
         "&ldquo;fletcher&rdquo; &mdash; the same trade named in "
         "Kula's verse (Thag 1.19), echoed here."),
        ("tejana",
         "&ldquo;arrow-shaft&rdquo; &mdash; the object a fletcher "
         "straightens, and this verse's central simile."),
        ("uju",
         "&ldquo;straight&rdquo; or &ldquo;upright&rdquo; &mdash; "
         "describing the mind once straightened."),
        ("avijj&amacr;",
         "&ldquo;ignorance&rdquo; &mdash; what Hārita commands himself "
         "to break to bits."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.29:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this verse address Hārita?",
         "opts": [
             "In the third person, describing him from outside",
             "As a question posed to him",
             "As a direct, imperative self-command, naming him by name",
             "It does not name him at all"],
         "correct": 2,
         "expl": "Commands, not description."},
        {"q": "What simile does the verse use for straightening the mind?",
         "opts": [
             "A river cutting through stone",
             "A fletcher straightening an arrow",
             "A fire consuming wood",
             "No simile is used"],
         "correct": 1,
         "expl": "The verse's opening image."},
        {"q": "What earlier poem does this simile echo?",
         "opts": [
             "Kula's verse (Thag 1.19) in Chapter Two",
             "Subhūti's verse (Thag 1.1) in Chapter One",
             "No earlier poem is echoed",
             "Nandiya's verse (Thag 1.25) in this same chapter"],
         "correct": 0,
         "expl": "A callback spanning two chapters, not confined to one."},
        {"q": "What does the verse command Hārita to do once his mind is upright?",
         "opts": [
             "Nothing further is commanded",
             "Travel to a distant city",
             "Break ignorance to bits",
             "Teach a large assembly"],
         "correct": 2,
         "expl": "The verse's second, decisive command."},
        {"q": "In what order do this verse's two commands come?",
         "opts": [
             "Break ignorance first, then straighten the mind",
             "Both commands happen simultaneously with no order",
             "Only one command is given",
             "Straighten the mind first, then break ignorance"],
         "correct": 3,
         "expl": "Discipline positioned as the precondition for the decisive action."},
        {"q": "What does 'avijjā' mean?",
         "opts": [
             "Wisdom",
             "Ignorance",
             "Fear",
             "Wealth"],
         "correct": 1,
         "expl": "What Hārita commands himself to break to bits."},
        {"q": "What does 'usukāra' mean?",
         "opts": [
             "Fletcher",
             "Carpenter",
             "Irrigator",
             "Farmer"],
         "correct": 0,
         "expl": "The same trade named in Kula's verse, echoed here."},
        {"q": "How does this verse's self-address compare to Dabba's and Vīra's verses in Chapter One?",
         "opts": [
             "It is identical, using third-person praise",
             "This verse uses direct commands, not third-person description",
             "There is no comparison possible",
             "This verse never names its subject at all"],
         "correct": 1,
         "expl": "Imperative rather than descriptive self-naming."},
        {"q": "What does 'tejana' mean?",
         "opts": [
             "Arrow-shaft",
             "River",
             "Hut",
             "Robe"],
         "correct": 0,
         "expl": "The object a fletcher straightens, and this verse's central image."},
        {"q": "Where does this poem fall in Chapter Three?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The ninth poem, following Jambugāmikaputta's"],
         "correct": 3,
         "expl": "Second to last in the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A command, not a description", [
            "'Hārita,",
            "break ignorance to bits'"
        ]),
        ("A simile, echoed across chapters", [
            "the same fletcher,",
            "two chapters apart"
        ]),
        ("Straighten first, then break", [
            "discipline,",
            "then decisive action"
        ]),
        ("Naming oneself, imperatively", [
            "not praise —",
            "a command"
        ]),
    ],
    further=[
        '<a href="%s/thag1.29/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.28.html">Thag 1.28 &mdash; Jambug&amacr;'
        "mikaputta</a> &mdash; the poem immediately before this one, "
        "in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.30 — Uttiya (1st)
# --------------------------------------------------------------------------- #
page(
    1, 30, "Uttiya", "Uttiya (1st)",
    meta_title="Thag 1.30 — Uttiya (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Uttiya's verse, closing Chapter Three with illness "
        "recognized twice over as a prompt for mindfulness. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Three &middot; Poem 10 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse closing "
                    "Chapter Three, reflecting on illness past and "
                    "present"),
        ("Speaker", "Uttiya, reflecting on his own experience of "
                    "illness"),
        ("Form", "One four-line verse, followed in the Pali by an "
                 "untranslated chapter colophon and mnemonic summary "
                 "verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "quiet, undramatic reflection closing a "
                       "chapter of louder images"),
    ],
    why=(
        "Uttiya's verse closes Chapter Three quietly: illness in the "
        "past once brought mindfulness; illness now, once again, "
        "brings a renewed recognition &mdash; &lsquo;it's time for me "
        "to be heedful&rsquo;. After Nandiya's confrontation with "
        "Māra, Abhaya's precision simile, and Hārita's imperative "
        "self-command, this chapter ends on something modest: "
        "sickness noticed as a recurring teacher."),
    guide=[
        ("Illness recognized as a pattern, not a single event", [
            "The verse does not describe illness once, but twice: "
            "&lsquo;when I was ill in the past, mindfulness arose in "
            "me&rsquo;, and now, &lsquo;I am ill once more&rsquo; "
            "&mdash; a pattern noticed across time, not a single "
            "isolated occasion."]),
        ("A quiet close to a chapter of louder images", [
            "This chapter has moved through a Māra confrontation, an "
            "arrow-precision simile, and a named self-command. Its "
            "final poem instead closes on something undramatic: "
            "ordinary sickness, recognized honestly as an occasion for "
            "renewed attention rather than transformed into a grand "
            "image."]),
        ("Heedfulness as the verse's own conclusion", [
            "&lsquo;It's time for me to be heedful&rsquo; names "
            "appamāda, heedfulness or diligence &mdash; a quality "
            "described elsewhere across the early canon as "
            "foundational to every other wholesome quality, here "
            "arrived at simply through paying attention to a "
            "recurring bodily condition."]),
        ("A chapter's own close, left untranslated", [
            "As at Thag 1.10 and Thag 1.20, the Pali text here carries "
            "vaggo tatiyo, &lsquo;the third chapter is finished&rsquo;, "
            "followed by an uddāna naming all ten monks of this "
            "chapter in sequence: Nigrodha, Cittaka, Gosāla, Sugandha, "
            "Nandiya, Abhaya, Lomasakaṅgiya, Jambugāmikaputta, Hārita, "
            "and Uttiya. Sujato's translation leaves both untranslated, "
            "and neither appears in this page's text below."]),
    ],
    terms=[
        ("&amacr;b&amacr;dha",
         "&ldquo;illness&rdquo; or &ldquo;affliction&rdquo; &mdash; "
         "named twice in this verse, past and present."),
        ("sati",
         "&ldquo;mindfulness&rdquo; &mdash; what arose in Uttiya "
         "during his past illness."),
        ("k&amacr;la",
         "&ldquo;time&rdquo; &mdash; as in this verse's closing "
         "phrase, kālo me nappamajjituṁ, &lsquo;it's time for me not "
         "to be heedless&rsquo;."),
        ("appam&amacr;da",
         "&ldquo;heedfulness&rdquo; or &ldquo;diligence&rdquo; "
         "&mdash; the quality this verse arrives at, described "
         "elsewhere in the canon as foundational to every other "
         "wholesome quality."),
        ("vaggo tatiyo",
         "&ldquo;the third chapter is finished&rdquo; &mdash; the "
         "untranslated Pali colophon closing this chapter."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.30:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse say happened during Uttiya's past illness?",
         "opts": [
             "Nothing in particular",
             "He lost his mindfulness entirely",
             "Mindfulness arose in him",
             "He left the monastery"],
         "correct": 2,
         "expl": "The verse's first stated occasion of illness."},
        {"q": "What does the verse say is happening to Uttiya now?",
         "opts": [
             "He is ill once more",
             "He is traveling",
             "He is teaching a large assembly",
             "Nothing is said about his present state"],
         "correct": 0,
         "expl": "A second illness, prompting the verse's closing reflection."},
        {"q": "How does this verse's tone compare to Nandiya's Māra confrontation earlier in this chapter?",
         "opts": [
             "It is identical in tone and imagery",
             "It is quieter and more undramatic, closing on ordinary sickness rather than a grand image",
             "It is even more dramatic than Nandiya's verse",
             "There is no comparison possible"],
         "correct": 1,
         "expl": "A modest close after several louder poems."},
        {"q": "What does the verse conclude, given Uttiya's present illness?",
         "opts": [
             "That it's time for him to be heedful",
             "That he should ignore his illness",
             "That illness has no meaning at all",
             "That he should seek a different teacher"],
         "correct": 0,
         "expl": "The verse's closing resolution."},
        {"q": "What does the Pali text carry immediately after this poem, left untranslated by Sujato?",
         "opts": [
             "A love poem",
             "'Vaggo tatiyo' ('the third chapter is finished') and an uddāna naming all ten monks of the chapter",
             "A new eleventh poem",
             "Nothing follows this poem in the Pali"],
         "correct": 1,
         "expl": "The same untranslated colophon pattern seen at the end of Chapters One and Two."},
        {"q": "Does this page's text include that closing uddāna?",
         "opts": [
             "Yes, translated in full",
             "Yes, but only partially",
             "It is included as an image only",
             "No — it is absent from Sujato's translation and not included here"],
         "correct": 3,
         "expl": "Consistent with how this site handles untranslated structural material."},
        {"q": "What does 'appamāda' mean?",
         "opts": [
             "Fear",
             "Heedfulness or diligence",
             "Wealth",
             "A type of illness"],
         "correct": 1,
         "expl": "The quality this verse arrives at through reflecting on illness."},
        {"q": "How many monks' verses make up Chapter Three in total?",
         "opts": [
             "Five",
             "Twenty",
             "Ten",
             "One hundred and twenty"],
         "correct": 2,
         "expl": "Nigrodha through Uttiya, named in sequence in the untranslated uddāna."},
        {"q": "What does 'ābādha' mean?",
         "opts": [
             "Illness or affliction",
             "Joy",
             "A monastic robe",
             "A river"],
         "correct": 0,
         "expl": "Named twice in this verse, past and present."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the final chapter",
             "Exactly one more",
             "Ten more chapters",
             "Nine more chapters"],
         "correct": 3,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
    ],
    marginalia=[
        ("Illness, twice recognized", [
            "past illness, and",
            "illness once more"
        ]),
        ("A quiet close, after louder poems", [
            "no grand image —",
            "just honest sickness"
        ]),
        ("Heedfulness, arrived at simply", [
            "'time for me",
            "to be heedful'"
        ]),
        ("A third chapter closes", [
            "ten names, tabulated,",
            "left untranslated"
        ]),
    ],
    further=[
        '<a href="%s/thag1.30/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.29.html">Thag 1.29 &mdash; H&amacr;rita '
        "(1st)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.31 — Gahvarat&imacr;riya
# --------------------------------------------------------------------------- #
page(
    1, 31, "Gahvarat&imacr;riya", "Gahvarat&imacr;riya",
    meta_title="Thag 1.31 — Gahvaratīriya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Gahvaratīriya's verse, opening Chapter Four with endurance "
        "amid biting insects, compared to an elephant leading a "
        "battle. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 1 of 10",
    glance=[
        ("Setting", "The wilds, a formidable forest full of flies "
                    "and mosquitoes"),
        ("Speaker", "An unnamed voice offering advice on enduring "
                    "discomfort"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "single endurance simile opening a new chapter"),
    ],
    why=(
        "Chapter Four opens with a small, ordinary discomfort: flies "
        "and mosquitoes pestering a monk in the wilderness. The "
        "verse's advice is not to escape them but to endure mindfully "
        "&mdash; compared to an elephant standing at the head of a "
        "battle."),
    guide=[
        ("An ordinary irritant, not a dramatic threat", [
            "Where other verses describe confrontations with Māra or "
            "cosmic images of samsara, this one names something "
            "small and physical: insects. The advice that follows "
            "treats even minor, persistent discomfort as worth "
            "mindful endurance, not only dramatic dangers."]),
        ("An elephant at the head of a battle", [
            "The simile chosen for endurance is a striking one: not a "
            "patient farmer or a calm sage, but a war elephant "
            "standing firm at the front line &mdash; an image of "
            "steadiness under active assault, not passive tolerance."]),
        ("Mindfulness named as the specific method", [
            "The verse does not simply say &lsquo;endure&rsquo;; it "
            "says &lsquo;mindfully endure&rsquo; &mdash; sati named "
            "directly as the quality that makes the endurance "
            "possible, not mere stubbornness or distraction."]),
    ],
    terms=[
        ("ga&#7745;a",
         "&ldquo;the formidable forest&rdquo; or wilderness &mdash; "
         "the setting for this verse's discomfort."),
        ("sati",
         "&ldquo;mindfulness&rdquo; &mdash; the specific quality "
         "this verse credits with making endurance possible."),
        ("khama",
         "&ldquo;endure&rdquo; or &ldquo;bear with&rdquo; &mdash; "
         "the verse's central instruction."),
        ("n&amacr;ga",
         "&ldquo;elephant&rdquo; &mdash; the animal in this verse's "
         "central simile, specifically one leading a battle."),
        ("sa&#7749;g&amacr;ma",
         "&ldquo;battle&rdquo; &mdash; the setting of the simile's "
         "elephant, an image of active steadiness rather than "
         "passive calm."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.31:1.1-1.4"),
    ],
    quiz=[
        {"q": "What discomfort does this verse describe?",
         "opts": [
             "A confrontation with Māra",
             "Extreme hunger",
             "Flies and mosquitoes in the wilderness",
             "A dangerous storm"],
         "correct": 2,
         "expl": "An ordinary, physical irritant, not a dramatic threat."},
        {"q": "What simile does the verse use for enduring this discomfort?",
         "opts": [
             "A calm farmer",
             "A sleeping child",
             "A still lake",
             "An elephant at the head of a battle"],
         "correct": 3,
         "expl": "An image of active steadiness, not passive tolerance."},
        {"q": "What specific quality does the verse credit with making endurance possible?",
         "opts": [
             "Wealth",
             "Physical strength alone",
             "Mindfulness",
             "Nothing in particular is credited"],
         "correct": 2,
         "expl": "Named directly as the method, not left implicit."},
        {"q": "How does this verse's subject compare to more dramatic confrontations described elsewhere in this collection?",
         "opts": [
             "It is identical in scale and drama",
             "It describes no discomfort at all",
             "It is set in a royal palace",
             "It addresses something small and ordinary instead"],
         "correct": 3,
         "expl": "Minor, persistent discomfort treated as worth mindful attention."},
        {"q": "What does 'khama' mean?",
         "opts": [
             "Endure or bear with",
             "Flee",
             "Celebrate",
             "Forget"],
         "correct": 0,
         "expl": "The verse's central instruction."},
        {"q": "What does 'gaṇa' refer to in this verse?",
         "opts": [
             "A royal court",
             "The formidable forest, the setting for this discomfort",
             "A monastic robe",
             "A river"],
         "correct": 1,
         "expl": "The wilderness setting named in the verse's opening lines."},
        {"q": "Why is an elephant in battle a fitting image for this verse's advice?",
         "opts": [
             "It is an image of active steadiness under assault, not mere passive calm",
             "Elephants are afraid of insects",
             "It has no particular relevance",
             "It describes fleeing from danger"],
         "correct": 0,
         "expl": "Steadiness while actively under pressure, not withdrawal."},
        {"q": "What does 'saṅgāma' mean?",
         "opts": [
             "Battle",
             "A meal",
             "A monastic title",
             "A type of hut"],
         "correct": 0,
         "expl": "The setting of the verse's elephant simile."},
        {"q": "Does this verse advise escaping the discomfort it describes?",
         "opts": [
             "Yes, escape is the main advice",
             "No — it advises mindful endurance instead",
             "The verse gives no advice at all",
             "Yes, but only partially"],
         "correct": 1,
         "expl": "Enduring mindfully, not fleeing."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "It closes the entire collection",
             "It opens Chapter Four, the Book of the Ones' fourth chapter",
             "It is not part of the Book of the Ones",
             "It opens Chapter One"],
         "correct": 1,
         "expl": "The first of ten poems in this new chapter."},
    ],
    marginalia=[
        ("A small discomfort, taken seriously", [
            "flies and mosquitoes,",
            "not a grand threat"
        ]),
        ("Steadiness under active assault", [
            "an elephant,",
            "at the head of battle"
        ]),
        ("Named directly: mindfulness", [
            "not stubbornness,",
            "but sati"
        ]),
        ("A new chapter begins", [
            "ten more poems,",
            "opening with endurance"
        ]),
    ],
    further=[
        '<a href="%s/thag1.31/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.30.html">Thag 1.30 &mdash; Uttiya (1st)</a> '
        "&mdash; the poem immediately before this one, closing "
        "Chapter Three.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.32 — Suppiya
# --------------------------------------------------------------------------- #
page(
    1, 32, "Suppiya", "Suppiya",
    meta_title="Thag 1.32 — Suppiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Suppiya's verse, an exchange of old age for the unaging and "
        "burning for quenching, framed as the ultimate trade. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse framed as an "
                    "exchange"),
        ("Speaker", "Suppiya, describing his own goal as a trade"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "compact verse built entirely on the logic of "
                       "exchange"),
    ],
    why=(
        "Suppiya frames liberation as a transaction: &lsquo;I'll swap "
        "old age for the unaging, burning for quenching&rsquo; "
        "&mdash; not simply gaining something new, but trading one "
        "state directly for its opposite, culminating in &lsquo;the "
        "supreme sanctuary from the yoke&rsquo;."),
    guide=[
        ("A structure of exchange, not simple attainment", [
            "The verb nimināti, &lsquo;to exchange or barter&rsquo;, "
            "governs this whole verse: aging is traded for the "
            "unaging, burning for quenching &mdash; a transactional "
            "framing rather than a description of gradual "
            "development or arrival."]),
        ("Two trades, then an escalating description of the result", [
            "After naming its two specific exchanges, the verse "
            "piles on two further descriptions of what is gained: "
            "&lsquo;the ultimate peace&rsquo;, then &lsquo;the "
            "supreme sanctuary from the yoke&rsquo; &mdash; each term "
            "stronger than the last."]),
        ("The yoke as a recurring image of bondage", [
            "Yogakkhema, &lsquo;sanctuary from the yoke&rsquo;, uses "
            "yoga, the same image of binding attachment that recurs "
            "across this collection and its companion, the "
            "Therīgātha, as a term for what keeps beings tied to "
            "further rebirth."]),
    ],
    terms=[
        ("ajara",
         "&ldquo;unaging&rdquo; &mdash; what Suppiya says he will "
         "exchange for old age."),
        ("j&imacr;ram&amacr;na",
         "&ldquo;aging&rdquo; or &ldquo;growing old&rdquo; &mdash; "
         "the state being traded away."),
        ("nibbuti",
         "&ldquo;quenching&rdquo; &mdash; exchanged for burning in "
         "this verse's second trade."),
        ("tappam&amacr;na",
         "&ldquo;burning&rdquo; &mdash; describing the state of "
         "affliction being given up."),
        ("yogakkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; a compound "
         "combining yoga, the binding tie of attachment, with khema, "
         "safety or security."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.32:1.1-1.4"),
    ],
    quiz=[
        {"q": "What structure does this verse use to describe Suppiya's goal?",
         "opts": [
             "A narrative journey",
             "A numerical list",
             "An exchange, trading one state for its opposite",
             "A dialogue with another monk"],
         "correct": 2,
         "expl": "The verb 'to exchange' governs the whole verse."},
        {"q": "What does Suppiya say he will exchange old age for?",
         "opts": [
             "Wealth",
             "The unaging",
             "A longer life",
             "Nothing is exchanged for old age"],
         "correct": 1,
         "expl": "The verse's first stated trade."},
        {"q": "What is exchanged for burning, according to the verse?",
         "opts": [
             "More burning",
             "Silence",
             "Quenching",
             "Nothing is exchanged for burning"],
         "correct": 2,
         "expl": "The verse's second stated trade."},
        {"q": "What two descriptions does the verse pile onto the result of these exchanges?",
         "opts": [
             "No further description is given",
             "The ultimate peace, and the supreme sanctuary from the yoke",
             "A description of a specific place",
             "A list of other monks"],
         "correct": 1,
         "expl": "Two escalating descriptions closing the verse."},
        {"q": "What does 'yogakkhema' combine?",
         "opts": [
             "Two unrelated place names",
             "Yoga, the binding tie of attachment, with khema, safety or security",
             "Two words for fire",
             "A word for water and a word for earth"],
         "correct": 1,
         "expl": "A compound naming sanctuary from bondage."},
        {"q": "What does 'ajara' mean?",
         "opts": [
             "Unaging",
             "Fearful",
             "Wealthy",
             "A type of hut"],
         "correct": 0,
         "expl": "What Suppiya says he will gain in exchange for old age."},
        {"q": "What does 'tappamāna' describe?",
         "opts": [
             "Burning or affliction",
             "Calm stillness",
             "A monastic robe",
             "A river"],
         "correct": 0,
         "expl": "The state being traded away in this verse's second exchange."},
        {"q": "Does this verse describe gradual development, or a direct trade?",
         "opts": [
             "Gradual development over many years",
             "Neither — no change is described",
             "A trade that ultimately fails",
             "A direct trade, one state for its opposite"],
         "correct": 3,
         "expl": "A transactional framing, not a description of gradual arrival."},
        {"q": "What does 'nibbuti' mean?",
         "opts": [
             "Quenching",
             "A type of meal",
             "A monastic title",
             "A river crossing"],
         "correct": 0,
         "expl": "What is gained in exchange for burning."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "It is not part of this chapter",
             "The second poem, following Gahvaratīriya's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Not gained, but exchanged", [
            "old age",
            "for the unaging"
        ]),
        ("Two trades, then two names for the result", [
            "ultimate peace,",
            "supreme sanctuary"
        ]),
        ("A yoke, and safety from it", [
            "yogakkhema,",
            "a recurring image"
        ]),
        ("Burning, traded for quenching", [
            "tappamāna,",
            "for nibbuti"
        ]),
    ],
    further=[
        '<a href="%s/thag1.32/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.31.html">Thag 1.31 &mdash; Gahvarat&imacr;'
        "riya</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.33 — Sop&amacr;ka (1st)
# --------------------------------------------------------------------------- #
page(
    1, 33, "Sop&amacr;ka", "Sop&amacr;ka (1st)",
    meta_title="Thag 1.33 — Sopāka (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sopāka's verse, the mother-and-only-child image extended to "
        "all creatures, shared with this site's own Discourse on "
        "Love. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse moving from "
                    "one intimate case to a universal one"),
        ("Speaker", "Sopāka, offering instruction in general terms"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a well-known image, extended from one child to "
                       "all beings"),
    ],
    why=(
        "&lsquo;Just as a mother would be good to her beloved only "
        "child, so, to creatures all and everywhere, let one be "
        "good&rsquo; &mdash; the same core image, and the term "
        "ekaputta, &lsquo;only child&rsquo;, found in this site's own "
        "translation of the Discourse on Love (Khuddakapatha, Kp 9)."),
    guide=[
        ("A shared image with this site's Discourse on Love", [
            "This verse's mother-and-only-child image shares its "
            "central term, ekaputta, with the Khuddakapatha's Kp 9, "
            "the Discourse on Love &mdash; though the wording is not "
            "identical between the two, the same core image of total, "
            "protective care extended toward one child is common to "
            "both."]),
        ("From the narrowest case to the widest possible scope", [
            "The verse's structure moves in one direction: starting "
            "from the most intimate, particular relationship "
            "imaginable &mdash; a mother and her only child &mdash; "
            "and extending the same quality outward to &lsquo;all and "
            "everywhere&rsquo;, the broadest scope a sentence could "
            "name."]),
        ("Goodness named as a skill, not only a feeling", [
            "The verb kusalī siyā, translated &lsquo;would be "
            "good&rsquo;, carries the sense of skillfulness as much as "
            "warmth &mdash; goodness toward others framed partly as "
            "something practiced and developed, not purely a spontaneous "
            "emotion."]),
    ],
    terms=[
        ("ekaputta",
         "&ldquo;only child&rdquo; &mdash; the term shared with this "
         "site's own translation of the Discourse on Love (Kp 9)."),
        ("piya",
         "&ldquo;beloved&rdquo; or &ldquo;dear&rdquo; &mdash; "
         "describing the child in this verse's opening image."),
        ("kusal&imacr;",
         "&ldquo;good&rdquo; or &ldquo;skillful&rdquo; &mdash; the "
         "specific quality this verse extends from one child to all "
         "beings."),
        ("p&amacr;&#7751;a",
         "&ldquo;creature&rdquo; or &ldquo;living being&rdquo; "
         "&mdash; the object of this verse's universal extension."),
        ("sabbattha",
         "&ldquo;everywhere&rdquo; &mdash; the verse's closing word, "
         "naming its widest possible scope."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.33:1.1-1.4"),
    ],
    quiz=[
        {"q": "What image opens this verse?",
         "opts": [
             "A river crossing",
             "A blazing fire",
             "A battle scene",
             "A mother's care for her beloved only child"],
         "correct": 3,
         "expl": "The verse's central, well-known image."},
        {"q": "To what scope does the verse extend this image?",
         "opts": [
             "Only to the speaker's own family",
             "All creatures, everywhere",
             "Only to other monks",
             "The verse names no wider scope"],
         "correct": 1,
         "expl": "From one intimate case to the broadest possible scope."},
        {"q": "What term does this verse share with this site's own Discourse on Love (Kp 9)?",
         "opts": [
             "Ekaputta, 'only child'",
             "Nibbāna",
             "Saṅgha",
             "No term is shared"],
         "correct": 0,
         "expl": "A shared central image, though the wording is not identical."},
        {"q": "Is the wording of this verse identical to the Discourse on Love's version of this image?",
         "opts": [
             "Yes, word for word identical",
             "No — the core image and the term 'ekaputta' are shared, but the wording differs",
             "The two texts share no connection at all",
             "This verse quotes a completely different collection"],
         "correct": 1,
         "expl": "A shared image and term, not a verbatim quotation."},
        {"q": "What does 'kusalī' suggest about the quality this verse describes?",
         "opts": [
             "Purely spontaneous feeling with no skill involved",
             "A sense of skillfulness as well as warmth",
             "Fear rather than care",
             "Indifference"],
         "correct": 1,
         "expl": "Goodness framed partly as something practiced, not only felt."},
        {"q": "What does 'ekaputta' mean?",
         "opts": [
             "A monastic robe",
             "A river",
             "Only child",
             "A type of hut"],
         "correct": 2,
         "expl": "The term at the center of this verse's opening image."},
        {"q": "What does 'sabbattha' mean?",
         "opts": [
             "Nowhere",
             "Only in one place",
             "A specific city",
             "Everywhere"],
         "correct": 3,
         "expl": "The verse's closing word, naming its widest scope."},
        {"q": "What does 'pāṇa' refer to?",
         "opts": [
             "A monastic title",
             "A type of food",
             "A creature or living being",
             "A river"],
         "correct": 2,
         "expl": "The object of this verse's universal extension."},
        {"q": "How does this verse's structure move, from beginning to end?",
         "opts": [
             "From the narrowest, most intimate case to the widest possible scope",
             "From the widest scope to the narrowest",
             "It stays at the same scope throughout",
             "It describes no movement in scope at all"],
         "correct": 0,
         "expl": "One child, then all creatures everywhere."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The third poem, following Suppiya's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A shared image, across collections", [
            "ekaputta,",
            "echoed in the Discourse on Love"
        ]),
        ("From one child to all beings", [
            "the narrowest case,",
            "made universal"
        ]),
        ("Goodness, practiced as a skill", [
            "kusalī —",
            "not only felt"
        ]),
        ("A shared term, not a shared line", [
            "the same image,",
            "different wording"
        ]),
    ],
    further=[
        '<a href="%s/thag1.33/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../khuddakapatha/kp-9.html">Kp 9 &mdash; The '
        "Discourse on Love</a> &mdash; sharing this verse's core "
        "image and the term ekaputta, &lsquo;only child&rsquo;.",
        '<a href="thag-1.32.html">Thag 1.32 &mdash; Suppiya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.34 — Posiya
# --------------------------------------------------------------------------- #
page(
    1, 34, "Posiya", "Posiya",
    meta_title="Thag 1.34 — Posiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Posiya's verse, a specific incident of maintaining monastic "
        "boundaries, closing with his own name at the moment of "
        "decisive action. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 4 of 10",
    glance=[
        ("Setting", "A journey from village to wilderness, then into "
                    "a house where Posiya had gone to be fed"),
        ("Speaker", "An unnamed voice stating a general principle, "
                    "then Posiya himself, named at the verse's close"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a concrete, specific incident rather than a "
                       "general statement"),
    ],
    why=(
        "This verse traces an actual sequence of movement &mdash; "
        "village, wilderness, then a house Posiya entered to be fed "
        "&mdash; before ending on a decisive, specific action: he got "
        "up and left without taking leave, rather than remain in a "
        "situation the verse's opening lines describe as best "
        "avoided."),
    guide=[
        ("A specific incident, not only a general statement", [
            "Where many verses in this collection state a principle "
            "and stop there, this one traces a real itinerary &mdash; "
            "from village to wilderness to a particular house &mdash; "
            "giving its instruction narrative particularity rather "
            "than leaving it abstract."]),
        ("A named, decisive action at the close", [
            "The verse's final line names Posiya directly, in the "
            "third person, at the exact moment of his decision: "
            "&lsquo;he got up and left without taking leave, "
            "Posiya&rsquo; &mdash; the same technique of self-naming "
            "at a verse's climax already seen with Dabba and Vīra in "
            "Chapter One."]),
        ("A principle about monastic boundaries, dramatized in action", [
            "The verse opens by stating that a discerning person is "
            "better off avoiding close proximity to women in certain "
            "settings, then shows Posiya himself acting on that "
            "principle at once, choosing to leave an awkward "
            "situation abruptly rather than remain in it &mdash; "
            "instruction shown through action, not only stated."]),
    ],
    terms=[
        ("an&amacr;sanna",
         "&ldquo;not sitting close&rdquo; &mdash; the verse's opening "
         "principle about avoiding proximity."),
        ("vij&amacr;nat",
         "&ldquo;one who discerns&rdquo; or &ldquo;knows&rdquo; "
         "&mdash; describing the person this principle applies to."),
        ("g&amacr;ma",
         "&ldquo;village&rdquo; &mdash; the starting point of "
         "Posiya's itinerary in this verse."),
        ("ara&ntilde;&ntilde;a",
         "&ldquo;wilderness&rdquo; &mdash; the second stage of his "
         "journey, before entering the house."),
        ("an&amacr;mantetv&amacr;",
         "&ldquo;without informing&rdquo; or &ldquo;without taking "
         "leave&rdquo; &mdash; describing how abruptly Posiya "
         "departed."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.34:1.1-1.6"),
    ],
    quiz=[
        {"q": "What route does the verse describe Posiya taking?",
         "opts": [
             "From village to wilderness, then into a house",
             "From a river to a mountain",
             "From a monastery directly to a city",
             "No route is described"],
         "correct": 0,
         "expl": "A specific, traced itinerary."},
        {"q": "What does Posiya do once inside the house, according to the verse?",
         "opts": [
             "He stays for many days",
             "He teaches the household a long sermon",
             "He gets up and leaves without taking leave",
             "Nothing further is described"],
         "correct": 2,
         "expl": "A decisive, abrupt action closing the verse."},
        {"q": "How does the verse name Posiya?",
         "opts": [
             "It never names him at all",
             "By name, in the third person, at the verse's climactic moment",
             "Only in a separate attribution line",
             "By a title only, never his personal name"],
         "correct": 1,
         "expl": "The same self-naming-at-the-climax technique seen with Dabba and Vīra in Chapter One."},
        {"q": "What general principle opens this verse?",
         "opts": [
             "That wealth should be avoided",
             "That travel is always dangerous",
             "No general principle is stated",
             "That a discerning person is better off avoiding close proximity to women in certain settings"],
         "correct": 3,
         "expl": "A principle the rest of the verse then dramatizes in action."},
        {"q": "How does this verse relate its opening principle to what follows?",
         "opts": [
             "The principle is contradicted by what follows",
             "It shows Posiya acting on the principle directly",
             "The two are entirely unrelated",
             "The principle is repeated without any action shown"],
         "correct": 1,
         "expl": "Instruction shown through action, not only stated."},
        {"q": "What does 'anāmantetvā' mean?",
         "opts": [
             "Joyfully",
             "Slowly",
             "Without informing or without taking leave",
             "With great ceremony"],
         "correct": 2,
         "expl": "Describing the abruptness of Posiya's departure."},
        {"q": "What does 'gāma' mean?",
         "opts": [
             "Village",
             "River",
             "Mountain",
             "Ocean"],
         "correct": 0,
         "expl": "The starting point of the verse's traced itinerary."},
        {"q": "Was Posiya at the house to receive food, according to the verse?",
         "opts": [
             "No, he had no reason to be there",
             "Yes, he was there to be fed",
             "The verse does not say why he was there",
             "He was there to teach"],
         "correct": 1,
         "expl": "Named directly before his abrupt departure."},
        {"q": "How does this verse's specificity compare to more general instructive verses elsewhere in this chapter?",
         "opts": [
             "It is identical in its level of generality",
             "It contains no instruction at all",
             "It is far more abstract than any other verse in this chapter",
             "It traces a real, specific itinerary rather than staying abstract"],
         "correct": 3,
         "expl": "Narrative particularity rather than a purely general statement."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The fourth poem, following Sopāka's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A traced route, not a vague setting", [
            "village, wilderness,",
            "then a house"
        ]),
        ("Named at the decisive moment", [
            "'without taking leave,",
            "Posiya'"
        ]),
        ("A principle, then an action", [
            "stated, then",
            "shown"
        ]),
        ("An abrupt, deliberate exit", [
            "up and gone,",
            "no formal farewell"
        ]),
    ],
    further=[
        '<a href="%s/thag1.34/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.33.html">Thag 1.33 &mdash; Sop&amacr;ka '
        "(1st)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.35 — S&amacr;ma&ntilde;&ntilde;ak&amacr;ni
# --------------------------------------------------------------------------- #
page(
    1, 35, "S&amacr;ma&ntilde;&ntilde;ak&amacr;ni", "S&amacr;ma&ntilde;&ntilde;ak&amacr;ni",
    meta_title="Thag 1.35 — Sāmaññakāni | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sāmaññakāni's verse, happiness found as a byproduct of "
        "developing the noble eightfold path toward freedom from "
        "death. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a short verse naming a "
                    "specific practice and its effects"),
        ("Speaker", "An unnamed voice describing those who develop "
                    "this path"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a dense stack of descriptive terms for a "
                       "single named path"),
    ],
    why=(
        "Seeking happiness, this verse says, people find it &lsquo;"
        "through this practice&rsquo; &mdash; and gain a good "
        "reputation besides &mdash; before the verse names exactly "
        "what practice it means: &lsquo;the noble eightfold "
        "path&rsquo;, described in four stacked terms, developed "
        "toward freedom from death."),
    guide=[
        ("Happiness described as found, not directly pursued", [
            "The verse's opening line notes that those &lsquo;seeking "
            "happiness&rsquo; find it &lsquo;through this "
            "practice&rsquo; &mdash; happiness arriving as a result of "
            "the practice rather than something chased for its own "
            "sake, with social effects like reputation and fame named "
            "before the practice itself is even identified."]),
        ("A path named with four stacked qualifiers", [
            "Once named, the path is described densely: ariya "
            "(&lsquo;noble&rsquo;), a&#7789;&#7789;ha&#7749;gika "
            "(&lsquo;eightfold&rsquo;), a&ntilde;jasa (&lsquo;direct "
            "route&rsquo;), and uju (&lsquo;straight&rsquo;) &mdash; "
            "four descriptive terms compressed onto a single path "
            "before the verse names its final goal."]),
        ("A doctrinal landmark named directly", [
            "This is the first poem in this chapter-by-chapter "
            "reading of the Theragātha to name the noble eightfold "
            "path explicitly &mdash; a formula appearing elsewhere on "
            "this site in the Khuddakapatha, here given its own "
            "concentrated four-line treatment."]),
    ],
    terms=[
        ("sukha",
         "&ldquo;happiness&rdquo; &mdash; what this verse says is "
         "found through practice, not pursued directly."),
        ("kitti",
         "&ldquo;reputation&rdquo; &mdash; named as a further effect "
         "of this practice, alongside growing fame."),
        ("ariya",
         "&ldquo;noble&rdquo; &mdash; the first of four terms "
         "describing the path this verse names."),
        ("a&#7789;&#7789;ha&#7749;gika",
         "&ldquo;eightfold&rdquo; &mdash; identifying this path "
         "specifically as the eightfold path."),
        ("a&ntilde;jasa",
         "&ldquo;direct route&rdquo; &mdash; one of the path's four "
         "stacked descriptive terms, paired with uju, "
         "&ldquo;straight&rdquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.35:1.1-1.4"),
    ],
    quiz=[
        {"q": "According to this verse, how do those seeking happiness find it?",
         "opts": [
             "By avoiding all practice",
             "By chance alone",
             "The verse does not say",
             "Through this practice"],
         "correct": 3,
         "expl": "Happiness arriving as a result, not chased directly."},
        {"q": "What two social effects does the verse name, besides happiness?",
         "opts": [
             "Wealth and power",
             "Reputation and fame",
             "Fear and doubt",
             "None are named"],
         "correct": 1,
         "expl": "Named before the practice itself is identified."},
        {"q": "What specific path does the verse eventually name?",
         "opts": [
             "A path through a forest",
             "A path to a distant city",
             "No specific path is named",
             "The noble eightfold path"],
         "correct": 3,
         "expl": "The verse's central, doctrinal subject."},
        {"q": "How many descriptive terms does the verse stack onto this path?",
         "opts": [
             "None",
             "One",
             "Four",
             "Ten"],
         "correct": 2,
         "expl": "Noble, eightfold, direct route, and straight."},
        {"q": "What is this path developed toward, according to the verse?",
         "opts": [
             "Wealth",
             "Freedom from death",
             "Fame alone",
             "Nothing is stated"],
         "correct": 1,
         "expl": "The verse's stated final goal."},
        {"q": "What does 'ariya' mean?",
         "opts": [
             "Noble",
             "Fearful",
             "Wealthy",
             "Ordinary"],
         "correct": 0,
         "expl": "The first of four terms describing the path."},
        {"q": "What does 'aṭṭhaṅgika' mean?",
         "opts": [
             "Eightfold",
             "Threefold",
             "Single",
             "Endless"],
         "correct": 0,
         "expl": "Identifying this path specifically."},
        {"q": "Where else on this site does the noble eightfold path appear, according to this guide?",
         "opts": [
             "Nowhere else",
             "In the Khuddakapatha",
             "Only in the Cariyapitaka",
             "Only in a later chapter of this same book"],
         "correct": 1,
         "expl": "A formula appearing elsewhere on this site as well."},
        {"q": "What does 'añjasa' mean?",
         "opts": [
             "A direct route",
             "A winding detour",
             "A dead end",
             "A river crossing"],
         "correct": 0,
         "expl": "One of the path's four stacked descriptive terms."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The fifth poem, following Posiya's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Happiness, found rather than chased", [
            "through practice,",
            "not pursued directly"
        ]),
        ("A path, named densely", [
            "noble, eightfold,",
            "direct, straight"
        ]),
        ("A landmark, named explicitly", [
            "this chapter's first",
            "eightfold path"
        ]),
        ("Reputation, named before the goal", [
            "fame grows,",
            "then the path is named"
        ]),
    ],
    further=[
        '<a href="%s/thag1.35/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.34.html">Thag 1.34 &mdash; Posiya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.36 — Kum&amacr;putta
# --------------------------------------------------------------------------- #
page(
    1, 36, "Kum&amacr;putta", "Kum&amacr;putta",
    meta_title="Thag 1.36 — Kumāputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kumāputta's verse, a threefold 'good' opening that defines "
        "the ascetic life as questioning meaning and skillful action. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting; a checklist verse defining "
                    "the ascetic life"),
        ("Speaker", "Kumāputta, offering instruction in general "
                    "terms"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a threefold refrain resolving into a precise "
                       "definition"),
    ],
    why=(
        "&lsquo;Learning is good, living well is good, the life "
        "without abode is always good&rsquo; &mdash; three short "
        "claims, each opening with the same word, before the verse "
        "narrows to something precise: &lsquo;questions on the "
        "meaning, actions that are skillful&rsquo;, named directly as "
        "&lsquo;the ascetic life for one who has nothing&rsquo;."),
    guide=[
        ("A threefold refrain, then a precise definition", [
            "Sādhu, &lsquo;good&rsquo;, opens all three of the "
            "verse's first claims &mdash; learning, living well, "
            "homelessness &mdash; before the final two lines shift "
            "register entirely, defining exactly what &lsquo;the "
            "ascetic life&rsquo; consists of rather than simply "
            "praising it further."]),
        ("Homelessness named as a virtue in itself", [
            "Aniketavih&amacr;ra, &lsquo;dwelling without a fixed "
            "abode&rsquo;, is called good &lsquo;always&rsquo; "
            "&mdash; not merely a circumstance forced on a "
            "renunciant, but a quality actively valued in its own "
            "right."]),
        ("A term shared with Gosāla's verse earlier in this chapter", [
            "&lsquo;Skillful action&rsquo; translates "
            "padakkhi&#7751;akamma, sharing its root with padakkhi&#7751;a&#7745;, "
            "the term Sujato's note on Gosāla's verse (Thag 1.23) "
            "explained as playing on dakkha, &lsquo;skilled&rsquo; "
            "&mdash; the same word family surfacing a second time "
            "within this same chapter."]),
    ],
    terms=[
        ("s&amacr;dhu",
         "&ldquo;good&rdquo; &mdash; the word opening all three of "
         "this verse's first claims."),
        ("aniketavih&amacr;ra",
         "&ldquo;dwelling without a fixed abode&rdquo; &mdash; "
         "homelessness, named as a virtue in its own right."),
        ("atthapucchana",
         "&ldquo;questioning about the meaning&rdquo; &mdash; the "
         "first of two activities this verse defines the ascetic life "
         "by."),
        ("padakkhi&#7751;akamma",
         "&ldquo;skillful action&rdquo; &mdash; sharing its root with "
         "a term already noted in Gosāla's verse (Thag 1.23) earlier "
         "in this chapter."),
        ("aki&ntilde;cana",
         "&ldquo;one who has nothing&rdquo; &mdash; the verse's "
         "closing description of the ascetic life's practitioner."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.36:1.1-1.4"),
    ],
    quiz=[
        {"q": "What word opens all three of this verse's first claims?",
         "opts": [
             "Sādhu, 'good'",
             "Bhaya, 'fear'",
             "Dukkha, 'suffering'",
             "Rāga, 'desire'"],
         "correct": 0,
         "expl": "A threefold refrain opening the verse."},
        {"q": "What three things does the verse's opening call 'good'?",
         "opts": [
             "Wealth, status, and power",
             "Learning, living well, and the life without abode",
             "Food, sleep, and shelter",
             "Nothing specific is named"],
         "correct": 1,
         "expl": "The verse's threefold opening refrain."},
        {"q": "What two things does the verse's final definition name?",
         "opts": [
             "Questioning the meaning, and skillful action",
             "Wealth and status",
             "Fear and doubt",
             "Sleep and food"],
         "correct": 0,
         "expl": "The precise content the verse gives to 'the ascetic life'."},
        {"q": "How is the person practicing this ascetic life described, closing the verse?",
         "opts": [
             "As wealthy",
             "As fearful",
             "As one who has nothing",
             "As a king"],
         "correct": 2,
         "expl": "Akiñcana, closing the verse's definition."},
        {"q": "What does 'aniketavihāra' mean?",
         "opts": [
             "A grand palace",
             "A type of meal",
             "A monastic ceremony",
             "Dwelling without a fixed abode"],
         "correct": 3,
         "expl": "Homelessness, named good 'always' in this verse."},
        {"q": "What term in this verse shares a root with a term already seen in this chapter?",
         "opts": [
             "Sādhu",
             "Padakkhiṇakamma, sharing a root with a term in Gosāla's verse",
             "Aniketavihāra",
             "No term is shared"],
         "correct": 1,
         "expl": "The same word family, dakkha, surfacing a second time in this chapter."},
        {"q": "What does 'atthapucchana' mean?",
         "opts": [
             "Questioning about the meaning",
             "Sleeping soundly",
             "Traveling far",
             "Eating slowly"],
         "correct": 0,
         "expl": "One of two activities defining the ascetic life in this verse."},
        {"q": "Does this verse treat homelessness as a mere circumstance or as a valued quality?",
         "opts": [
             "As a mere unavoidable circumstance",
             "As a quality actively valued in its own right",
             "The verse does not mention homelessness",
             "As something to be avoided"],
         "correct": 1,
         "expl": "Called good 'always', not simply tolerated."},
        {"q": "What does 'akiñcana' mean?",
         "opts": [
             "A wealthy merchant",
             "A powerful king",
             "A skilled craftsman",
             "One who has nothing"],
         "correct": 3,
         "expl": "The verse's closing description of who lives this ascetic life."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The sixth poem, following Sāmaññakāni's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A threefold refrain", [
            "good, good,",
            "always good"
        ]),
        ("Then a precise definition", [
            "questioning meaning,",
            "skillful action"
        ]),
        ("Homelessness, valued in itself", [
            "not endured —",
            "called good always"
        ]),
        ("A term echoing earlier in the chapter", [
            "the same root,",
            "surfacing twice"
        ]),
    ],
    further=[
        '<a href="%s/thag1.36/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.35.html">Thag 1.35 &mdash; S&amacr;ma&ntilde;'
        "&ntilde;ak&amacr;ni</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.37 — Kum&amacr;puttasah&amacr;yaka
# --------------------------------------------------------------------------- #
page(
    1, 37, "Kum&amacr;puttasah&amacr;yaka", "Kum&amacr;puttasah&amacr;yaka",
    meta_title="Thag 1.37 — Kumāputtasahāyaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kumāputta's companion's verse, warning against undisciplined "
        "wandering that loses meditation, then prescribing the "
        "remedy. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative setting; a warning about "
                    "undisciplined wandering, then direct advice"),
        ("Speaker", "Kumāputta's companion, named only through his "
                    "relationship to Kumāputta"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a warning followed directly by its own "
                       "prescribed remedy"),
    ],
    why=(
        "Placed directly after Kumāputta's own verse, this poem "
        "belongs to a monk named only as his companion. Its warning "
        "&mdash; undisciplined wandering that loses meditation "
        "&mdash; is followed at once by a remedy: &lsquo;dispel "
        "aggression, practicing absorption undistracted&rsquo;."),
    guide=[
        ("A name built entirely from relationship", [
            "Kum&amacr;puttasah&amacr;yaka means, literally, "
            "&lsquo;Kum&amacr;putta's companion&rsquo; &mdash; this "
            "monk carries no independent name of his own in this "
            "collection, placed directly after Kum&amacr;putta's own "
            "verse as a linked pair."]),
        ("A warning echoing this project's earlier cautionary verse", [
            "Like D&amacr;saka's verse in Chapter Two, this poem "
            "criticizes a failing rather than praising an attainment "
            "&mdash; here, undisciplined wandering &lsquo;to different "
            "countries&rsquo; that ends in losing meditation "
            "altogether, asking pointedly what such conduct could "
            "possibly achieve."]),
        ("From warning to remedy, within the same verse", [
            "Unlike D&amacr;saka's verse, which ends on the warning "
            "itself, this one moves directly to a prescribed "
            "response: &lsquo;dispel aggression, practicing absorption "
            "undistracted&rsquo; &mdash; the failing named, then "
            "immediately answered."]),
    ],
    terms=[
        ("n&amacr;n&amacr;janapada",
         "&ldquo;various countries&rdquo; &mdash; where the verse "
         "says undisciplined wanderers travel."),
        ("asa&ntilde;&ntilde;ata",
         "&ldquo;undisciplined&rdquo; or &ldquo;unrestrained&rdquo; "
         "&mdash; describing this wandering."),
        ("sam&amacr;dhi",
         "&ldquo;immersion&rdquo; or meditative concentration "
         "&mdash; what such wandering is said to lose."),
        ("s&amacr;rambha",
         "&ldquo;aggression&rdquo; or vehemence &mdash; what the "
         "verse's remedy instructs dispelling."),
        ("apurakkhata",
         "&ldquo;undistracted&rdquo; &mdash; describing how "
         "absorption should be practiced, per this verse's closing "
         "instruction."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.37:1.1-1.6"),
    ],
    quiz=[
        {"q": "How does Kumāputtasahāyaka get his own name?",
         "opts": [
             "Through a clan name",
             "Through a place name",
             "Entirely through his relationship to Kumāputta",
             "His name has no particular meaning"],
         "correct": 2,
         "expl": "No independent name of his own in this collection."},
        {"q": "What does the verse criticize?",
         "opts": [
             "Excessive meditation",
             "Staying too long in one place",
             "Undisciplined wandering to different countries that loses meditation",
             "Nothing is criticized"],
         "correct": 2,
         "expl": "A warning against a specific failing."},
        {"q": "How does this verse compare to Dāsaka's cautionary verse in Chapter Two?",
         "opts": [
             "They are identical in every way",
             "Both criticize a failing, but this one adds a prescribed remedy",
             "Dāsaka's verse offers no criticism at all",
             "There is no similarity between the two"],
         "correct": 1,
         "expl": "A shared cautionary mode, extended further here."},
        {"q": "What remedy does the verse prescribe?",
         "opts": [
             "No remedy is given",
             "Travel to even more countries",
             "Abandon meditation entirely",
             "Dispel aggression, practicing absorption undistracted"],
         "correct": 3,
         "expl": "The verse's closing instruction."},
        {"q": "What does 'asaññata' mean?",
         "opts": [
             "Undisciplined or unrestrained",
             "Wise",
             "Fearless",
             "Wealthy"],
         "correct": 0,
         "expl": "Describing the wandering this verse criticizes."},
        {"q": "What does the verse say such undisciplined wandering causes someone to lose?",
         "opts": [
             "Their wealth",
             "Their meditation",
             "Their reputation",
             "Nothing is described as lost"],
         "correct": 1,
         "expl": "Named directly as the consequence of this failing."},
        {"q": "What does 'sārambha' mean?",
         "opts": [
             "Aggression or vehemence",
             "Peace",
             "A type of hut",
             "A river"],
         "correct": 0,
         "expl": "What the verse's remedy instructs dispelling."},
        {"q": "Does this verse stay only at the level of criticism, or move to instruction?",
         "opts": [
             "It stays only at criticism",
             "It moves directly to a prescribed remedy",
             "It contains neither criticism nor instruction",
             "It only asks questions with no answers"],
         "correct": 1,
         "expl": "Warning followed immediately by a stated response."},
        {"q": "What does 'samādhi' mean?",
         "opts": [
             "Immersion or meditative concentration",
             "A monastic robe",
             "A geographic region",
             "A type of food"],
         "correct": 0,
         "expl": "What undisciplined wandering is said to cause someone to lose."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The seventh poem, following Kumāputta's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A name built from relationship alone", [
            "Kumāputta's companion,",
            "no name of his own"
        ]),
        ("A shared cautionary mode", [
            "echoing Dāsaka's",
            "warning, two chapters back"
        ]),
        ("From warning straight to remedy", [
            "the failing named,",
            "then answered at once"
        ]),
        ("Wandering that loses its own goal", [
            "many countries,",
            "meditation lost"
        ]),
    ],
    further=[
        '<a href="%s/thag1.37/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.36.html">Thag 1.36 &mdash; Kum&amacr;'
        "putta</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.38 — Gavampati
# --------------------------------------------------------------------------- #
page(
    1, 38, "Gavampati", "Gavampati",
    meta_title="Thag 1.38 — Gavampati | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Gavampati's verse, a specific psychic feat &mdash; halting a "
        "river &mdash; and the gods themselves paying homage. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 8 of 10",
    glance=[
        ("Setting", "The river Sarabhū, made to stand still"),
        ("Speaker", "An unnamed voice praising Gavampati by name"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "specific, named miraculous feat, honored by "
                       "gods themselves"),
    ],
    why=(
        "This verse names a specific feat by a specific person: "
        "Gavampati's psychic power made the river Sarabhū stand "
        "still. &lsquo;The gods bow to that great sage&rsquo;, the "
        "verse says &mdash; an unusually high tribute, honoring a "
        "human disciple with reverence from deities themselves."),
    guide=[
        ("A named feat, not a general practice", [
            "Unlike Siṅgāla's Father's poem earlier in this book, "
            "praising an unnamed monk's general meditation practice, "
            "this verse credits a specific, named individual with a "
            "specific, singular event: making a named river, "
            "Sarabhū, stand still through psychic power."]),
        ("Reverence from gods, not only from people", [
            "&lsquo;The gods bow to that great sage&rsquo; elevates "
            "the tribute beyond ordinary human praise &mdash; this "
            "verse claims recognition from deities themselves, one of "
            "this collection's highest possible forms of honor."]),
        ("Two paired epithets closing the verse", [
            "Gavampati is described as having &lsquo;slipped all "
            "chains&rsquo; and gone &lsquo;beyond rebirth&rsquo; "
            "&mdash; two distinct closing descriptions of full "
            "liberation, phrased differently from the &lsquo;fully "
            "quenched, steadfast&rsquo; formula recurring earlier in "
            "Chapter One."]),
    ],
    terms=[
        ("iddhi",
         "&ldquo;psychic power&rdquo; or supernormal ability &mdash; "
         "what enabled Gavampati's feat with the river."),
        ("asita",
         "&ldquo;unbound&rdquo; or &ldquo;not clung to&rdquo; "
         "&mdash; one of two qualities describing Gavampati directly."),
        ("aneja",
         "&ldquo;unperturbed&rdquo;, free of the agitation of "
         "craving &mdash; paired with asita in this verse."),
        ("sabbasa&#7749;g&amacr;tigata",
         "&ldquo;gone beyond all ties&rdquo; &mdash; describing "
         "Gavampati's liberation."),
        ("bhavassa p&amacr;ragu",
         "&ldquo;one who has crossed to the far shore of "
         "existence&rdquo; &mdash; the verse's closing description of "
         "his attainment."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.38:1.1-1.4"),
    ],
    quiz=[
        {"q": "What specific feat does this verse credit to Gavampati?",
         "opts": [
             "Teaching a large assembly",
             "Building a monastery",
             "No specific feat is named",
             "Making the river Sarabhū stand still through psychic power"],
         "correct": 3,
         "expl": "A specific, singular event, not a general practice."},
        {"q": "Who is said to bow to Gavampati in this verse?",
         "opts": [
             "Only other monks",
             "Only his family",
             "The gods",
             "No one is described as bowing"],
         "correct": 2,
         "expl": "An unusually high tribute, honoring recognition from deities."},
        {"q": "How does this verse's praise differ from Siṅgāla's Father's poem earlier in this book?",
         "opts": [
             "Both describe an unnamed monk's general practice",
             "This verse names a specific individual and a specific feat, rather than a general practice",
             "There is no difference at all",
             "This verse names no one at all"],
         "correct": 1,
         "expl": "Specificity of person and event, not general praise."},
        {"q": "What two epithets close this verse, describing Gavampati's liberation?",
         "opts": [
             "Fearful and doubting",
             "Wealthy and powerful",
             "No epithets are given",
             "Slipped all chains, and gone beyond rebirth"],
         "correct": 3,
         "expl": "Two distinct closing descriptions of full liberation."},
        {"q": "What does 'iddhi' mean?",
         "opts": [
             "Psychic power or supernormal ability",
             "A monastic robe",
             "A river",
             "A type of meal"],
         "correct": 0,
         "expl": "What enabled Gavampati's feat with the river."},
        {"q": "What does 'aneja' mean?",
         "opts": [
             "Fearful",
             "Unperturbed, free of the agitation of craving",
             "Wealthy",
             "A place name"],
         "correct": 1,
         "expl": "One of two qualities describing Gavampati directly."},
        {"q": "What river is named in this verse?",
         "opts": [
             "The Ganges",
             "The Yamunā",
             "Sarabhū",
             "No river is named"],
         "correct": 2,
         "expl": "The river Gavampati's psychic power made stand still."},
        {"q": "How does this verse's closing epithets compare to the 'fully quenched, steadfast' formula from Chapter One?",
         "opts": [
             "They are the exact same words",
             "They describe full liberation but phrase it differently",
             "This verse denies any liberation occurred",
             "There is no comparison possible"],
         "correct": 1,
         "expl": "Different specific compounds, same underlying attainment."},
        {"q": "What does 'bhavassa pāragu' mean?",
         "opts": [
             "One who has crossed to the far shore of existence",
             "One who fears existence",
             "One still trapped in existence",
             "A type of monastic robe"],
         "correct": 0,
         "expl": "The verse's closing description of Gavampati's attainment."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The eighth poem, following Kumāputtasahāyaka's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A named feat, not a vague practice", [
            "Sarabhū,",
            "stopped by psychic power"
        ]),
        ("Honored by gods, not only people", [
            "the gods",
            "bow to him"
        ]),
        ("Two epithets, closing the verse", [
            "chains slipped,",
            "rebirth surpassed"
        ]),
        ("Specificity, where other poems stay general", [
            "a named river,",
            "a named monk"
        ]),
    ],
    further=[
        '<a href="%s/thag1.38/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.37.html">Thag 1.37 &mdash; Kum&amacr;'
        "puttasah&amacr;yaka</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.39 — Tissa (1st)
# --------------------------------------------------------------------------- #
page(
    1, 39, "Tissa", "Tissa (1st)",
    meta_title="Thag 1.39 — Tissa (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Tissa's verse, two escalating similes of urgency &mdash; a "
        "sword-strike, a burning head &mdash; prescribing mindful "
        "wandering to give up sensual desire. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting; two similes of extreme "
                    "urgency"),
        ("Speaker", "An unnamed voice prescribing mindful wandering"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "two escalating emergency similes framing a "
                       "specific practice"),
    ],
    why=(
        "&lsquo;Like they're struck by a sword, like their head was "
        "on fire&rsquo; &mdash; two images of extreme emergency open "
        "this verse, before it names exactly what response they "
        "demand: a mendicant should wander mindful, specifically to "
        "give up sensual desire."),
    guide=[
        ("Two escalating similes, not one", [
            "Being struck by a sword and having one's head on fire "
            "are not simply two versions of the same idea; the second "
            "image intensifies the first, moving from a sudden blow "
            "to an ongoing, all-consuming emergency &mdash; urgency "
            "compounded rather than merely repeated."]),
        ("A precisely named target", [
            "The verse's urgency is not directed at defilement in "
            "general but at one specific thing: k&amacr;mar&amacr;ga, "
            "sensual desire &mdash; a precise target rather than a "
            "vague call to effort."]),
        ("Urgency paired directly with mindfulness, not panic", [
            "The verse's prescribed response to these emergency "
            "images is not frantic action but sato, "
            "&lsquo;mindful&rsquo; wandering &mdash; crisis-level "
            "motivation channeled into a steady, attentive practice "
            "rather than chaotic urgency."]),
    ],
    terms=[
        ("satti",
         "&ldquo;sword&rdquo; or &ldquo;spear&rdquo; &mdash; the "
         "verse's first image of sudden emergency."),
        ("oma&#7789;&#7789;ha",
         "&ldquo;struck&rdquo; or &ldquo;touched&rdquo; &mdash; "
         "describing the impact of that sword."),
        ("&#7693;ayham&amacr;na",
         "&ldquo;burning&rdquo; &mdash; the verse's second, "
         "intensifying image."),
        ("matthaka",
         "&ldquo;head&rdquo; &mdash; where this verse's fire is said "
         "to burn."),
        ("k&amacr;mar&amacr;ga",
         "&ldquo;sensual desire&rdquo; &mdash; the precise target "
         "this verse's urgency is directed at."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.39:1.1-1.4"),
    ],
    quiz=[
        {"q": "What two similes open this verse?",
         "opts": [
             "A calm lake and a still forest",
             "Being struck by a sword, and having one's head on fire",
             "A blooming flower and a rising sun",
             "A sleeping child and a quiet house"],
         "correct": 1,
         "expl": "Two escalating images of extreme emergency."},
        {"q": "How do these two similes relate to each other?",
         "opts": [
             "The second intensifies the first, compounding urgency",
             "They contradict each other",
             "They are identical in meaning",
             "The second cancels out the first"],
         "correct": 0,
         "expl": "A sudden blow followed by an ongoing, all-consuming emergency."},
        {"q": "What specific target does this urgency address?",
         "opts": [
             "Defilement in general, unspecified",
             "Physical illness",
             "Sensual desire specifically",
             "No target is named"],
         "correct": 2,
         "expl": "A precise target, not a vague call to effort."},
        {"q": "What response does the verse prescribe to this urgency?",
         "opts": [
             "Panic and frantic action",
             "Complete inaction",
             "Mindful wandering",
             "Fleeing to a distant city"],
         "correct": 2,
         "expl": "Crisis-level motivation channeled into steady, attentive practice."},
        {"q": "What does 'kāmarāga' mean?",
         "opts": [
             "Fear of death",
             "Sensual desire",
             "Love of learning",
             "Physical pain"],
         "correct": 1,
         "expl": "The precise target this verse's urgency addresses."},
        {"q": "What does 'satti' mean?",
         "opts": [
             "Sword or spear",
             "A river",
             "A monastic robe",
             "A type of food"],
         "correct": 0,
         "expl": "The verse's opening image of sudden emergency."},
        {"q": "What does 'ḍayhamāna' mean?",
         "opts": [
             "Burning",
             "Sleeping",
             "Traveling",
             "Teaching"],
         "correct": 0,
         "expl": "The verse's second, intensifying image."},
        {"q": "Where does the verse say this burning takes place?",
         "opts": [
             "In the chest",
             "In the hands",
             "The verse does not specify a location",
             "In the head"],
         "correct": 3,
         "expl": "Matthaka, 'head', named directly."},
        {"q": "Does this verse's urgency lead to chaotic panic, or steady practice?",
         "opts": [
             "Chaotic panic",
             "Steady, mindful practice",
             "Neither — no response is prescribed",
             "Complete abandonment of practice"],
         "correct": 1,
         "expl": "Crisis-level motivation, channeled rather than chaotic."},
        {"q": "Where does this poem fall in Chapter Four?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The ninth poem, following Gavampati's"],
         "correct": 3,
         "expl": "Second to last in the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Urgency, doubled", [
            "struck by a sword,",
            "then a head on fire"
        ]),
        ("A precise target", [
            "not defilement generally —",
            "sensual desire specifically"
        ]),
        ("Crisis, channeled into steadiness", [
            "not panic,",
            "but mindful wandering"
        ]),
        ("Two images, one intensifying the other", [
            "a sudden blow,",
            "then an unrelenting burn"
        ]),
    ],
    further=[
        '<a href="%s/thag1.39/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.38.html">Thag 1.38 &mdash; Gavampati</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.40 — Va&#7693;&#7693;ham&amacr;na
# --------------------------------------------------------------------------- #
page(
    1, 40, "Va&#7693;&#7693;ham&amacr;na", "Va&#7693;&#7693;ham&amacr;na",
    meta_title="Thag 1.40 — Vaḍḍhamāna | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vaḍḍhamāna's verse, closing Chapter Four with the same "
        "urgency as Tissa's verse redirected toward desire for "
        "rebirth, plus a commentarial story and a cautious aside "
        "about the Jain founder. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Four &middot; Poem 10 of 10",
    glance=[
        ("Setting", "No narrative setting in the verse itself; the "
                    "commentary places an earlier incident before "
                    "Vaḍḍhamāna's ordination"),
        ("Speaker", "An unnamed voice urging Vaḍḍhamāna, per the "
                    "commentary, out of laziness"),
        ("Form", "One four-line verse, followed in the Pali by an "
                 "untranslated chapter colophon and mnemonic summary "
                 "verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same urgent template as the poem before "
                       "it, redirected to a different craving, plus a "
                       "commentarial backstory"),
    ],
    why=(
        "This verse repeats Tissa's opening almost exactly &mdash; "
        "struck by a sword, head on fire &mdash; but redirects its "
        "urgency toward a different target: not sensual desire, but "
        "bhavar&amacr;ga, desire for continued existence. Sujato's "
        "note adds a commentarial story behind the verse, and a "
        "cautious aside connecting Vaḍḍhamāna's name to the founder "
        "of Jainism."),
    guide=[
        ("The same template as the poem just before it, one word changed", [
            "&lsquo;Struck by a sword, head on fire, a mendicant "
            "should wander mindful&rsquo; matches Tissa's verse (Thag "
            "1.39) almost word for word. Only the final target "
            "changes: k&amacr;mar&amacr;ga, sensual desire, becomes "
            "bhavar&amacr;ga, desire for continued existence &mdash; "
            "two of early Buddhism's three classic cravings, named in "
            "sequence across these two neighboring poems."]),
        ("A commentarial story explaining the verse's occasion", [
            "Sujato's note reports that, per the commentary, "
            "Vaḍḍhamāna committed some offense as a layman serious "
            "enough that the Buddha overturned his alms bowl against "
            "him &mdash; a formal act of censure the note describes "
            "as &lsquo;like stepping on a fire&rsquo;. He repented, "
            "asked forgiveness, and later ordained &mdash; but grew "
            "lazy, prompting the Buddha to address him with this "
            "verse."]),
        ("A cautious aside about the Jain founder", [
            "The note also observes that the commentary places "
            "Vaḍḍhamāna's birth in the royal Licchav&imacr; family of "
            "Ves&amacr;l&imacr; &mdash; the same clan and region "
            "traditionally associated with the Jain founder "
            "Mah&amacr;v&imacr;ra Vaḍḍhamāna. Sujato raises the "
            "possibility that this verse was meant to needle the Jain "
            "founder by name, while stating plainly that the "
            "commentary itself never draws this connection &mdash; a "
            "speculation offered, not a claim confirmed."]),
        ("A monk otherwise unknown", [
            "Unlike Gavampati in the poem just two before this one, "
            "praised for a specific named feat, Sujato's note "
            "describes this Vaḍḍhamāna as &lsquo;unknown "
            "elsewhere&rsquo; in the canon &mdash; his only surviving "
            "trace outside the commentarial story is this single "
            "verse."]),
        ("A chapter's own close, left untranslated", [
            "As at the end of Chapters One through Three, the Pali "
            "text here carries vaggo catuttho, &lsquo;the fourth "
            "chapter is finished&rsquo;, followed by an uddāna naming "
            "all ten monks of this chapter in sequence: "
            "Gahvarat&imacr;riya, Suppiya, Sop&amacr;ka, Posiya, "
            "S&amacr;ma&ntilde;&ntilde;ak&amacr;ni, Kum&amacr;putta, "
            "Kum&amacr;puttasah&amacr;yaka, Gavampati, Tissa, and "
            "Vaḍḍhamāna. Sujato's translation leaves both untranslated, "
            "and neither appears in this page's text below."]),
    ],
    terms=[
        ("bhavar&amacr;ga",
         "&ldquo;desire for continued existence&rdquo; &mdash; the "
         "target this verse redirects Tissa's urgency toward."),
        ("pattanikkujjana",
         "the formal act of &ldquo;overturning the bowl&rdquo; "
         "against someone &mdash; the censure the commentary says "
         "the Buddha used against Vaḍḍhamāna as a layman."),
        ("Licchav&imacr;",
         "the clan the commentary associates with Vaḍḍhamāna's birth "
         "&mdash; the same clan traditionally linked to the Jain "
         "founder Mahāvīra."),
        ("paribbaje",
         "&ldquo;should wander&rdquo; &mdash; the verse's closing "
         "instruction, shared word for word with Tissa's verse (Thag "
         "1.39)."),
        ("vaggo catuttho",
         "&ldquo;the fourth chapter is finished&rdquo; &mdash; the "
         "untranslated Pali colophon closing this chapter."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.40:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse share with Tissa's verse (Thag 1.39) just before it?",
         "opts": [
             "Nothing — they are unrelated",
             "Only the closing attribution line",
             "The same speaker's name",
             "Almost the exact same opening two lines and closing structure"],
         "correct": 3,
         "expl": "The same template, with one target word changed."},
        {"q": "What target does this verse's urgency redirect toward, compared to Tissa's verse?",
         "opts": [
             "Bhavarāga, desire for continued existence, rather than sensual desire",
             "Fear of death",
             "Wealth",
             "No target is named, unlike Tissa's verse"],
         "correct": 0,
         "expl": "Two of the three classic cravings, named across two neighboring poems."},
        {"q": "According to the commentary Sujato's note cites, what happened to Vaḍḍhamāna as a layman?",
         "opts": [
             "Nothing notable is recorded",
             "The Buddha overturned his alms bowl against him as a formal censure",
             "He became a wealthy merchant",
             "He traveled to a distant country"],
         "correct": 1,
         "expl": "A serious offense prompting an extreme monastic response."},
        {"q": "What does the note say happened after Vaḍḍhamāna repented?",
         "opts": [
             "He was permanently barred from ordaining",
             "He immediately attained full awakening",
             "He later ordained, but grew lazy, prompting this verse",
             "Nothing further is recorded"],
         "correct": 2,
         "expl": "The occasion the commentary gives for this verse."},
        {"q": "What cautious speculation does Sujato's note raise about Vaḍḍhamāna's name?",
         "opts": [
             "That the verse might have been meant to needle the Jain founder, sharing his name and region",
             "That Vaḍḍhamāna and the Jain founder are definitely the same person",
             "No speculation is raised",
             "That the name is purely coincidental with certainty"],
         "correct": 0,
         "expl": "A possibility raised, explicitly not confirmed by the commentary itself."},
        {"q": "Does the commentary itself draw a direct link between Vaḍḍhamāna and the Jain founder?",
         "opts": [
             "Yes, explicitly and directly",
             "The commentary denies any similarity",
             "This question is not addressed at all",
             "No — the note states the commentary never draws this connection"],
         "correct": 3,
         "expl": "A speculation offered by Sujato, not a claim in the commentary."},
        {"q": "How does Sujato's note describe Vaḍḍhamāna's presence elsewhere in the canon?",
         "opts": [
             "Extensively documented in many other texts",
             "Unknown elsewhere",
             "The subject of an entire separate collection",
             "Mentioned only by the Buddha's chief disciples"],
         "correct": 1,
         "expl": "A monk whose only surviving trace is this verse and its commentarial story."},
        {"q": "What does the Pali text carry immediately after this poem, left untranslated by Sujato?",
         "opts": [
             "A love poem",
             "'Vaggo catuttho' ('the fourth chapter is finished') and an uddāna naming all ten monks of the chapter",
             "A new eleventh poem",
             "Nothing follows this poem in the Pali"],
         "correct": 1,
         "expl": "The same untranslated colophon pattern seen at the end of Chapters One through Three."},
        {"q": "What does 'pattanikkujjana' refer to?",
         "opts": [
             "A meal offering",
             "A type of ordination ceremony",
             "The formal act of overturning the alms bowl as censure",
             "A meditation technique"],
         "correct": 2,
         "expl": "The extreme monastic response the commentary attributes to the Buddha here."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the final chapter",
             "Exactly one more",
             "Eight more chapters",
             "Twenty more chapters"],
         "correct": 2,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
    ],
    marginalia=[
        ("The same template, redirected", [
            "sensual desire,",
            "then desire for existence"
        ]),
        ("A bowl, overturned as censure", [
            "an extreme response,",
            "per the commentary"
        ]),
        ("A cautious aside, clearly flagged", [
            "perhaps a jab",
            "at the Jain founder"
        ]),
        ("A fourth chapter closes", [
            "ten names, tabulated,",
            "left untranslated"
        ]),
    ],
    further=[
        '<a href="%s/thag1.40/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.39.html">Thag 1.39 &mdash; Tissa (1st)</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.41 — Siriva&#7693;&#7693;ha
# --------------------------------------------------------------------------- #
page(
    1, 41, "Siriva&#7693;&#7693;ha", "Siriva&#7693;&#7693;ha",
    meta_title="Thag 1.41 — Sirivaḍḍha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sirivaḍḍha's verse, opening Chapter Five with lightning over "
        "a mountain cleft, contrasted with unshaken absorption "
        "inside it. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 1 of 10",
    glance=[
        ("Setting", "The cleft between Mount Vebhāra and Mount "
                    "Paṇḍava, lit by lightning"),
        ("Speaker", "An unnamed voice describing Sirivaḍḍha, called "
                    "the son of the Buddha"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "storm outside, stillness within, opening a "
                       "new chapter"),
    ],
    why=(
        "Chapter Five opens with weather: lightning striking down on "
        "a mountain cleft between Vebhāra and Paṇḍava. Inside that "
        "same cleft, Sirivaḍḍha sits absorbed in jhāna, called "
        "&lsquo;the son of the Buddha, inimitable and "
        "unaffected&rsquo; &mdash; the storm outside left entirely "
        "without effect on the stillness within."),
    guide=[
        ("A storm outside, stillness inside the same space", [
            "The verse places its lightning and its meditator in "
            "exactly the same location &mdash; the mountain cleft "
            "&mdash; rather than contrasting a stormy world with a "
            "sheltered retreat elsewhere. The drama and the calm "
            "occupy the same physical spot at once."]),
        ("'Son of the Buddha', a kinship title", [
            "Putta, &lsquo;son&rsquo;, echoes appattima, "
            "&lsquo;inimitable&rsquo; &mdash; describing Sirivaḍḍha's "
            "relationship to the Buddha in familial terms, a title of "
            "spiritual lineage similar in spirit to d&amacr;y&amacr;da, "
            "&lsquo;heir&rsquo;, used for the unnamed monk in "
            "Si&#7749;g&amacr;la's Father's poem earlier in this "
            "book."]),
        ("A chapter that will close on the same image", [
            "This chapter's very last poem, Vimala's verse (Thag "
            "1.50), returns to storm imagery &mdash; celestial rain, "
            "wind, and lightning &mdash; set against the same kind of "
            "undisturbed stillness, bookending Chapter Five with a "
            "matched pair of weather-and-calm poems."]),
    ],
    terms=[
        ("vijjut&amacr;",
         "&ldquo;lightning&rdquo; &mdash; the verse's opening image, "
         "striking the mountain cleft."),
        ("nagavivara",
         "&ldquo;mountain cleft&rdquo; &mdash; the single location "
         "shared by both the storm and Sirivaḍḍha's absorption."),
        ("jh&amacr;yati",
         "&ldquo;is absorbed in jh&amacr;na&rdquo; &mdash; describing "
         "Sirivaḍḍha's meditation, undisturbed by the storm around "
         "him."),
        ("putta",
         "&ldquo;son&rdquo; &mdash; the kinship title given to "
         "Sirivaḍḍha in relation to the Buddha."),
        ("appa&#7789;ima",
         "&ldquo;inimitable&rdquo; or &ldquo;without equal&rdquo; "
         "&mdash; one of two descriptive terms closing this verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.41:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's opening line describe?",
         "opts": [
             "A calm, clear sky",
             "A quiet village",
             "Lightning striking a mountain cleft",
             "A gentle river"],
         "correct": 2,
         "expl": "The verse's dramatic opening image."},
        {"q": "Where is Sirivaḍḍha absorbed in jhāna, according to the verse?",
         "opts": [
             "In a distant village",
             "In a royal palace",
             "By the ocean",
             "In the same mountain cleft struck by lightning"],
         "correct": 3,
         "expl": "Storm and stillness occupying the same location at once."},
        {"q": "What title does the verse give Sirivaḍḍha, in relation to the Buddha?",
         "opts": [
             "Enemy",
             "Servant",
             "Stranger",
             "Son of the Buddha"],
         "correct": 3,
         "expl": "A kinship title expressing spiritual lineage."},
        {"q": "How does this verse's structure compare to a contrast between a stormy world and a sheltered retreat elsewhere?",
         "opts": [
             "The storm and the meditator share the exact same location",
             "The meditator flees the storm to a different place",
             "No storm is mentioned at all",
             "The meditator is described as afraid"],
         "correct": 0,
         "expl": "Drama and calm occupying one spot at once, not two separate scenes."},
        {"q": "What later poem in this chapter returns to similar storm imagery?",
         "opts": [
             "No later poem uses similar imagery",
             "Vimala's verse (Thag 1.50), closing the chapter",
             "Sumaṅgala's verse, several poems later",
             "Sānu's verse"],
         "correct": 1,
         "expl": "A matched pair bookending Chapter Five."},
        {"q": "What does 'jhāyati' mean?",
         "opts": [
             "Is sleeping",
             "Is traveling",
             "Is absorbed in jhāna",
             "Is teaching"],
         "correct": 2,
         "expl": "Describing Sirivaḍḍha's undisturbed meditation."},
        {"q": "What does 'appaṭima' mean?",
         "opts": [
             "Fearful",
             "Inimitable or without equal",
             "Wealthy",
             "Ordinary"],
         "correct": 1,
         "expl": "One of two descriptive terms closing this verse."},
        {"q": "How does 'son of the Buddha' compare to a title used earlier in this book?",
         "opts": [
             "It is unrelated to any earlier title",
             "It echoes 'heir', dāyāda, used for the unnamed monk in Siṅgāla's Father's poem",
             "It contradicts an earlier title directly",
             "No earlier title exists in this collection"],
         "correct": 1,
         "expl": "Two similar kinship-based titles of spiritual lineage."},
        {"q": "What mountains does the verse name?",
         "opts": [
             "Vebhāra and Paṇḍava",
             "No specific mountains are named",
             "A single unnamed peak",
             "Mount Vipula alone"],
         "correct": 0,
         "expl": "Named directly as the setting for the lightning."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "It opens Chapter Five, the Book of the Ones' fifth chapter",
             "It closes the entire collection",
             "It is not part of the Book of the Ones",
             "It opens Chapter One"],
         "correct": 0,
         "expl": "The first of ten poems in this new chapter."},
    ],
    marginalia=[
        ("One place, two realities", [
            "lightning above,",
            "stillness within"
        ]),
        ("A kinship title", [
            "son of the Buddha,",
            "echoing 'heir' elsewhere"
        ]),
        ("A chapter's bookend, foreshadowed", [
            "this storm returns,",
            "closing the chapter too"
        ]),
        ("Named mountains, a named cleft", [
            "Vebhāra, Paṇḍava,",
            "one shared space"
        ]),
    ],
    further=[
        '<a href="%s/thag1.41/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.40.html">Thag 1.40 &mdash; Va&#7693;'
        "&#7693;ham&amacr;na</a> &mdash; the poem immediately before "
        "this one, closing Chapter Four.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.42 — Revata of the Acacia Wood
# --------------------------------------------------------------------------- #
page(
    1, 42, "Khadiravaniya", "Revata of the Acacia Wood",
    meta_title="Thag 1.42 — Revata of the Acacia Wood | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "this verse naming Cālā, Upacālā, and Sīsūpacālā &mdash; "
        "grammatically feminine names matching three nuns already "
        "translated on this site, with a contested translation "
        "history. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative setting; three names addressed "
                    "directly, in the vocative case"),
        ("Speaker", "The monk known as Revata of the Acacia Wood, "
                    "addressing Cālā, Upacālā, and Sīsūpacālā"),
        ("Form", "One three-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734; &mdash; a short "
                       "verse carrying a genuine, unresolved question "
                       "about who it addresses"),
    ],
    why=(
        "&lsquo;C&amacr;l&amacr;, Upac&amacr;l&amacr;, S&imacr;"
        "s&umacr;pac&amacr;l&amacr; &mdash; meditate mindfully! I've "
        "come to you like a hair-splitter&rsquo;. These three names "
        "are grammatically feminine in the Pali, matching three nuns "
        "whose own verses already appear elsewhere on this site "
        "&mdash; yet a long translation tradition rendered them as "
        "men."),
    guide=[
        ("Grammatically feminine names, naming three known nuns", [
            "C&amacr;le, Upac&amacr;le, S&imacr;s&umacr;pac&amacr;le "
            "carry the feminine vocative singular ending in Pali. "
            "These same three names belong to nuns whose own verses "
            "appear on this site as Thig 7.2 (C&amacr;l&amacr;), Thig "
            "7.3 (Upac&amacr;l&amacr;), and Thig 8.1 "
            "(S&imacr;s&umacr;pac&amacr;l&amacr;) &mdash; each "
            "confronting M&amacr;ra directly in her own poem."]),
        ("A contested translation history", [
            "Sujato's note reports that earlier translators, Rhys "
            "Davids and Norman, rendered these names as masculine, "
            "following the traditional commentary &mdash; despite "
            "what the note calls &lsquo;grammatical "
            "implausibility&rsquo;, and despite no other known group "
            "of three monks sharing these names anywhere else in the "
            "canon. A passing mention of a C&amacr;la and Upac&amacr;la "
            "at AN 10.72 exists, but the note points out those monks "
            "are otherwise entirely unknown."]),
        ("A precision image, echoing an earlier poem in this collection", [
            "&lsquo;I've come to you like a hair-splitter&rsquo; "
            "measures precision in a way that echoes Abhaya's verse "
            "(Thag 1.26) earlier in this book, which compared "
            "penetrating a subtle truth to piercing a hair-tip with "
            "an arrow &mdash; two different images from the same "
            "family, both measuring exactness against something "
            "almost too fine to strike."]),
        ("What this page does, and does not, claim", [
            "This guide reports the grammatical fact and the "
            "cross-reference to the three nuns' own poems as Sujato's "
            "note presents them, without asserting a specific "
            "relationship between Revata of the Acacia Wood and the "
            "three women his verse's grammar addresses &mdash; the "
            "note itself flags &lsquo;some confusion in the "
            "attributions&rsquo; across the sources it cites."]),
    ],
    terms=[
        ("vedh&imacr;",
         "&ldquo;hair-splitter&rdquo;, one who splits a hair with "
         "precision &mdash; this verse's central image of exactness."),
        ("patissat&amacr;",
         "&ldquo;mindful&rdquo; &mdash; the quality this verse urges "
         "onto the three it addresses."),
        ("Khadiravaniya",
         "&ldquo;of the Acacia Wood&rdquo; &mdash; the epithet "
         "identifying this poem's speaker."),
        ("feminine vocative",
         "the grammatical case ending &lsquo;-e&rsquo; on C&amacr;le, "
         "Upac&amacr;le, and S&imacr;s&umacr;pac&amacr;le, marking "
         "these as names of women being directly addressed."),
        ("C&amacr;l&amacr;, Upac&amacr;l&amacr;, S&imacr;s&umacr;pac&amacr;l&amacr;",
         "three names matching nuns whose own verses appear on this "
         "site at Thig 7.2, Thig 7.3, and Thig 8.1."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.42:1.1-1.3"),
    ],
    quiz=[
        {"q": "What grammatical case do the names Cālā, Upacālā, and Sīsūpacālā carry in this verse?",
         "opts": [
             "Feminine vocative",
             "Masculine nominative",
             "Neuter genitive",
             "No specific case can be determined"],
         "correct": 0,
         "expl": "Marking these as the names of women being addressed directly."},
        {"q": "Where do these same three names appear elsewhere on this site?",
         "opts": [
             "Nowhere else",
             "As nuns' own verses at Thig 7.2, Thig 7.3, and Thig 8.1",
             "Only in the Cariyapitaka",
             "Only in the Khuddakapatha"],
         "correct": 1,
         "expl": "Each confronting Māra directly in her own poem."},
        {"q": "According to Sujato's note, how did earlier translators Rhys Davids and Norman render these names?",
         "opts": [
             "As feminine, matching the grammar",
             "They refused to translate the names at all",
             "As a single combined name",
             "As masculine, following the commentary despite grammatical implausibility"],
         "correct": 3,
         "expl": "A translation tradition the note pushes back against."},
        {"q": "Does the note claim a confirmed group of three male monks shares these names elsewhere in the canon?",
         "opts": [
             "Yes, a well-documented group exists",
             "The note does not address this question",
             "Yes, and they are extensively described",
             "No — a passing mention exists at AN 10.72, but those monks are otherwise entirely unknown"],
         "correct": 3,
         "expl": "The masculine reading's supporting evidence is thin, per the note."},
        {"q": "What simile does this verse use for precision?",
         "opts": [
             "A river cutting through stone",
             "Coming like a hair-splitter",
             "A fire consuming wood",
             "No simile is used"],
         "correct": 1,
         "expl": "An image of exact, fine-grained precision."},
        {"q": "How does this simile relate to an earlier poem in this collection?",
         "opts": [
             "It has no connection to any earlier poem",
             "It echoes Abhaya's hair-tip-and-arrow simile (Thag 1.26)",
             "It directly quotes Sirivaḍḍha's verse",
             "It contradicts an earlier simile"],
         "correct": 1,
         "expl": "Two related images of extreme precision, from the same family."},
        {"q": "Does this guide assert a specific relationship between Revata of the Acacia Wood and the three named women?",
         "opts": [
             "Yes, it confirms they are definitely his sisters",
             "Yes, it confirms they are unrelated to him entirely",
             "No — it reports the grammatical fact and cross-reference without asserting a specific relationship",
             "The guide does not mention this question at all"],
         "correct": 2,
         "expl": "A deliberately cautious framing, matching what the source note itself supports."},
        {"q": "What does 'patissatā' urge?",
         "opts": [
             "Mindfulness",
             "Fear",
             "Wealth",
             "Silence"],
         "correct": 0,
         "expl": "The quality this verse asks the three addressed to maintain."},
        {"q": "What does 'Khadiravaniya' mean?",
         "opts": [
             "Of the Acacia Wood",
             "Of the royal court",
             "Of the mountain peak",
             "Of the river crossing"],
         "correct": 0,
         "expl": "The epithet identifying this poem's speaker."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It closes the chapter",
             "It opens the chapter",
             "The second poem, following Sirivaḍḍha's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Feminine names, a contested reading", [
            "vocative -e,",
            "translated as masculine anyway"
        ]),
        ("Three names, already known here", [
            "Cālā, Upacālā,",
            "Sīsūpacālā — Thig 7.2, 7.3, 8.1"
        ]),
        ("A precision image, echoed", [
            "a hair-splitter,",
            "recalling Abhaya's arrow"
        ]),
        ("Caution over certainty", [
            "the note flags confusion —",
            "this guide does too"
        ]),
    ],
    further=[
        '<a href="%s/thag1.42/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../therigatha/thig-7.2.html">Thig 7.2 &mdash; '
        "C&amacr;l&amacr;</a>, <a href=\"../therigatha/thig-7.3.html\">"
        "Thig 7.3 &mdash; Upac&amacr;l&amacr;</a>, and <a "
        'href="../therigatha/thig-8.1.html">Thig 8.1 &mdash; '
        "S&imacr;s&umacr;pac&amacr;l&amacr;</a> &mdash; the three "
        "nuns' own verses, sharing the names this poem addresses.",
        '<a href="thag-1.41.html">Thag 1.41 &mdash; Siriva&#7693;'
        "&#7693;ha</a> &mdash; the poem immediately before this one, "
        "in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.43 — Suma&#7749;gala
# --------------------------------------------------------------------------- #
page(
    1, 43, "Suma&#7749;gala", "Suma&#7749;gala",
    meta_title="Thag 1.43 — Sumaṅgala | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sumaṅgala's verse, ecstatic doubled exclamations over being "
        "freed from a farmer's sickle, plough, and hoe, closing with "
        "self-exhortation. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative setting; an ecstatic declaration of "
                    "freedom from farm labor"),
        ("Speaker", "Sumaṅgala, exclaiming his own release, then "
                    "commanding himself by name"),
        ("Form", "One eight-line verse, built almost entirely on "
                 "doubled repetition"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "ecstatic doubling as its own rhetorical "
                       "device"),
    ],
    why=(
        "&lsquo;Well freed! Well freed!&rsquo; Sumaṅgala opens, before "
        "naming exactly what he's freed from: not sensual desire in "
        "the abstract, but his sickles, his ploughs, and his little "
        "hoes &mdash; a farmer's own tools, named specifically, "
        "renounced with unrestrained relief."),
    guide=[
        ("Repetition as the verse's central technique", [
            "&lsquo;Well freed! Well freed!&rsquo;, &lsquo;done with "
            "them, done!&rsquo;, &lsquo;practice absorption "
            "Sumaṅgala! Practice absorption Sumaṅgala!&rsquo; &mdash; "
            "this verse expresses its joy almost entirely through "
            "insistent doubling rather than elaborate description, "
            "each key phrase said twice in a row."]),
        ("Three specific tools, not an abstract craving", [
            "&lsquo;Three crooked things&rsquo; are named precisely: "
            "sickles, ploughs, and little hoes &mdash; the ordinary, "
            "backbreaking equipment of farm labor, giving this "
            "verse's relief a concrete, physical target rather than a "
            "general renunciation of sensual pleasure."]),
        ("Self-naming three times, each paired with a command", [
            "Sumaṅgala's own name appears three times in this verse's "
            "closing lines, each instance directly commanding "
            "himself: &lsquo;practice absorption, Sumaṅgala&rsquo;, "
            "repeated, then &lsquo;stay heedful, Sumaṅgala&rsquo; "
            "&mdash; a more concentrated use of self-naming-as-command "
            "than Hārita's single instance earlier in this book."]),
    ],
    terms=[
        ("sumuttika",
         "&ldquo;well freed&rdquo; &mdash; the verse's doubled "
         "opening exclamation."),
        ("t&imacr;hi khujjakehi",
         "&ldquo;from three crooked things&rdquo; &mdash; introducing "
         "the specific tools named next."),
        ("na&#7749;gala",
         "&ldquo;plough&rdquo; &mdash; one of the three farming tools "
         "this verse names."),
        ("khuddakudd&amacr;la",
         "&ldquo;little hoe&rdquo; &mdash; the third of the three "
         "tools."),
        ("appamatta",
         "&ldquo;heedful&rdquo; &mdash; the quality of the verse's "
         "final command to Sumaṅgala."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.43:1.1-1.8"),
    ],
    quiz=[
        {"q": "How does this verse open?",
         "opts": [
             "With a question",
             "With a description of a landscape",
             "With a list of other monks",
             "With a doubled exclamation: 'Well freed! Well freed!'"],
         "correct": 3,
         "expl": "Repetition as the verse's opening technique."},
        {"q": "What three things does Sumaṅgala say he's freed from?",
         "opts": [
             "Sensual desire in the abstract",
             "His sickles, ploughs, and little hoes",
             "Fear and doubt",
             "Wealth and status"],
         "correct": 1,
         "expl": "A former farmer's own specific tools, named directly."},
        {"q": "How many times does the verse repeat 'practice absorption, Sumaṅgala'?",
         "opts": [
             "Once",
             "Twice",
             "Never",
             "Four times"],
         "correct": 1,
         "expl": "Doubled, matching the verse's overall pattern."},
        {"q": "What rhetorical device does this verse rely on most heavily?",
         "opts": [
             "Elaborate metaphor",
             "A single extended narrative",
             "A rhetorical question left unanswered",
             "Doubled repetition of key phrases"],
         "correct": 3,
         "expl": "Nearly every key phrase said twice in a row."},
        {"q": "How does Sumaṅgala's self-naming compare to Hārita's earlier in this book?",
         "opts": [
             "Sumaṅgala names himself three times; Hārita, once",
             "Neither poem names its speaker",
             "They are identical in frequency",
             "Hārita's poem names himself more often"],
         "correct": 0,
         "expl": "A more concentrated use of self-naming-as-command here."},
        {"q": "What does 'naṅgala' mean?",
         "opts": [
             "Plough",
             "Sickle",
             "Hoe",
             "Basket"],
         "correct": 0,
         "expl": "One of the three farming tools named in this verse."},
        {"q": "What quality closes the verse, in its final command to Sumaṅgala?",
         "opts": [
             "Wealth",
             "Fear",
             "Heedfulness",
             "Silence"],
         "correct": 2,
         "expl": "Appamatta, the verse's final instruction."},
        {"q": "Is Sumaṅgala's relief in this verse directed at an abstract craving or a concrete circumstance?",
         "opts": [
             "An abstract craving with no specific object",
             "A concrete circumstance: specific farming tools",
             "Neither — no relief is expressed",
             "A fear of death"],
         "correct": 1,
         "expl": "Physical, ordinary tools, named precisely."},
        {"q": "What does 'khuddakuddāla' mean?",
         "opts": [
             "Little hoe",
             "Great river",
             "Royal palace",
             "Monastic robe"],
         "correct": 0,
         "expl": "The third of the three tools this verse names."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The third poem, following Revata of the Acacia Wood's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Joy, expressed by doubling", [
            "well freed,",
            "well freed!"
        ]),
        ("Three specific tools, not an abstraction", [
            "sickle, plough,",
            "and little hoe"
        ]),
        ("Named three times, commanded three times", [
            "Sumaṅgala,",
            "practice absorption"
        ]),
        ("Relief that is concrete, not vague", [
            "backbreaking labor,",
            "named and released"
        ]),
    ],
    further=[
        '<a href="%s/thag1.43/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.42.html">Thag 1.42 &mdash; Revata of the '
        "Acacia Wood</a> &mdash; the poem immediately before this "
        "one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.44 — S&amacr;nu
# --------------------------------------------------------------------------- #
page(
    1, 44, "S&amacr;nu", "S&amacr;nu",
    meta_title="Thag 1.44 — Sānu | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sānu's verse, his confused question to his weeping mother "
        "&mdash; the same line preserved in fuller context in this "
        "site's own SN 10.5. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 4 of 10",
    glance=[
        ("Setting", "A conversation between Sānu and his weeping "
                    "mother"),
        ("Speaker", "Sānu, addressing his mother directly by name in "
                    "every line"),
        ("Form", "One four-line verse, a question left unanswered "
                 "here"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a moment of genuine confusion, not yet "
                       "resolved within the verse itself"),
    ],
    why=(
        "&lsquo;Mum, they weep for the dead, or for one who's alive "
        "but missing. I'm alive and you can see me, so mum, why do "
        "you weep for me?&rsquo; This exact question appears, word "
        "for word, within a fuller story already translated on this "
        "site: SN 10.5, With S&amacr;nu &mdash; where his mother's "
        "answer follows."),
    guide=[
        ("This verse's fuller context, already on this site", [
            "SN 10.5 tells S&amacr;nu's complete story: possessed by "
            "a spirit as a child, his mother's grief and recovery "
            "prayer, his eventual recovery &mdash; and, at that "
            "story's own &sect;5, this exact verse, followed by his "
            "mother's answer at &sect;6, redefining what &lsquo;"
            "alive&rsquo; and &lsquo;dead&rsquo; actually mean."]),
        ("'Mum', repeated in every single line", [
            "Amma, &lsquo;mum&rsquo;, appears in all four lines of "
            "this verse &mdash; not once at the opening and assumed "
            "afterward, but insistently repeated, structuring the "
            "entire verse around the address itself."]),
        ("A question, not an answer", [
            "This Theragātha verse preserves only S&amacr;nu's side "
            "&mdash; his confusion at being wept over while plainly "
            "alive. His mother's reply, which SN 10.5 records "
            "separately, does not appear here at all."]),
        ("A rare moment of unresolved bewilderment", [
            "Where most verses in this collection declare an "
            "attainment, confront M&amacr;ra, or express ecstatic "
            "freedom, this one captures a moment before resolution "
            "&mdash; S&amacr;nu genuinely does not yet understand his "
            "mother's grief, and the verse ends without him "
            "understanding it."]),
    ],
    terms=[
        ("amma",
         "&ldquo;mum&rdquo; &mdash; repeated in every one of this "
         "verse's four lines."),
        ("mata",
         "&ldquo;dead&rdquo; &mdash; the first reason S&amacr;nu "
         "names for why people weep."),
        ("rodati",
         "&ldquo;weeps&rdquo; or &ldquo;cries&rdquo; &mdash; the "
         "action S&amacr;nu questions his mother about."),
        ("j&imacr;va",
         "&ldquo;alive&rdquo; &mdash; the state S&amacr;nu insists he "
         "is plainly in."),
        ("dissati",
         "&ldquo;is seen&rdquo; or &ldquo;visible&rdquo; &mdash; used "
         "in this verse to describe someone missing, not seen."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.44:1.1-1.4"),
    ],
    quiz=[
        {"q": "Where else on this site does this exact verse appear, in fuller context?",
         "opts": [
             "SN 10.5, With Sānu",
             "Nowhere else",
             "Only in the Cariyapitaka",
             "Only in the Khuddakapatha"],
         "correct": 0,
         "expl": "The same story, told at greater length elsewhere on this site."},
        {"q": "How many of this verse's four lines address 'mum' (amma) directly?",
         "opts": [
             "None",
             "Only the first line",
             "All four lines",
             "Only the last line"],
         "correct": 2,
         "expl": "An insistent, repeated address structuring the whole verse."},
        {"q": "What two reasons does Sānu say people usually weep, according to the verse?",
         "opts": [
             "Fear and doubt",
             "Wealth lost, or status lost",
             "No reasons are given",
             "For the dead, or for one who's alive but missing"],
         "correct": 3,
         "expl": "The premise behind Sānu's confused question."},
        {"q": "Does this Theragātha verse include the mother's answer to Sānu's question?",
         "opts": [
             "Yes, in full",
             "Yes, but only partially",
             "The verse has no question at all",
             "No — only Sānu's question is preserved here"],
         "correct": 3,
         "expl": "Her reply is recorded separately, at SN 10.5's §6."},
        {"q": "According to SN 10.5, what does the mother's fuller answer redefine?",
         "opts": [
             "Nothing in particular",
             "What 'alive' and 'dead' actually mean",
             "The price of goods",
             "A monastic rule"],
         "correct": 1,
         "expl": "Her answer, found elsewhere on this site, not in this verse."},
        {"q": "What does 'amma' mean?",
         "opts": [
             "Mum",
             "Brother",
             "Teacher",
             "Friend"],
         "correct": 0,
         "expl": "Repeated in every line of this verse."},
        {"q": "How does this verse's emotional register compare to most other poems in this collection?",
         "opts": [
             "Identical — a declaration of attainment",
             "A rare moment of unresolved confusion, not yet resolved",
             "A confrontation with Māra",
             "An ecstatic celebration"],
         "correct": 1,
         "expl": "Genuine bewilderment, preserved without its answer."},
        {"q": "What does 'jīva' mean?",
         "opts": [
             "Dead",
             "Alive",
             "Fearful",
             "Wealthy"],
         "correct": 1,
         "expl": "The state Sānu insists he is plainly in."},
        {"q": "What background does SN 10.5 provide for this cryptic saying, according to the site's own reading guide for that discourse?",
         "opts": [
             "A story of spirit possession, grief, and recovery",
             "A story about a lost sum of money",
             "A description of a royal ceremony",
             "No background is given anywhere"],
         "correct": 0,
         "expl": "The fuller narrative context for this exact verse."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The fourth poem, following Sumaṅgala's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("The same verse, told more fully elsewhere", [
            "SN 10.5,",
            "with the mother's answer too"
        ]),
        ("'Mum', in every line", [
            "amma,",
            "repeated four times"
        ]),
        ("A question, without its answer", [
            "confusion preserved,",
            "not yet resolved"
        ]),
        ("A rare, unresolved moment", [
            "not a declaration —",
            "genuine bewilderment"
        ]),
    ],
    further=[
        '<a href="%s/thag1.44/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../samyutta-nikaya/sn-10.5.html">SN 10.5 &mdash; '
        "With S&amacr;nu</a> &mdash; the fuller story this verse "
        "belongs to, including his mother's answer.",
        '<a href="thag-1.43.html">Thag 1.43 &mdash; Suma&#7749;'
        "gala</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.45 — Rama&#7751;&imacr;yavih&amacr;rin
# --------------------------------------------------------------------------- #
page(
    1, 45, "Rama&#7751;&imacr;yavih&amacr;rin", "Rama&#7751;&imacr;yavih&amacr;rin",
    meta_title="Thag 1.45 — Ramaṇīyavihārin | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ramaṇīyavihārin's verse, a thoroughbred that stumbles and "
        "recovers, sharing its opening line with an earlier poem in "
        "this collection. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a horse simile for "
                    "recovery after a stumble"),
        ("Speaker", "An unnamed voice describing a disciple "
                    "accomplished in vision"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a horse simile about resilience, not "
                       "uninterrupted perfection"),
    ],
    why=(
        "&lsquo;Though a fine thoroughbred may stumble, it soon "
        "stands firm again&rsquo; &mdash; this verse's point is not "
        "flawlessness but recovery: a disciple &lsquo;accomplished in "
        "vision&rsquo; is compared to a horse that stumbles and rights "
        "itself quickly, not one that never stumbles at all."),
    guide=[
        ("The same thoroughbred, used differently than before", [
            "&lsquo;A fine thoroughbred&rsquo;, bhaddo &amacr;ja&ntilde;"
            "&ntilde;o, opens this verse in the exact same Pali "
            "wording as Bela&#7789;&#7789;has&imacr;sa's verse (Thag "
            "1.16) in Chapter Two &mdash; but where that horse ran "
            "&lsquo;with ease&rsquo;, uninterrupted, this one stumbles "
            "first, and the verse's whole point rests on what happens "
            "next."]),
        ("Honesty about lapses, paired with confidence in recovery", [
            "Unlike verses declaring complete, uninterrupted freedom "
            "from fault, this one openly acknowledges that even a "
            "fine horse &mdash; and, by comparison, even an "
            "accomplished disciple &mdash; may stumble. The verse's "
            "confidence lies entirely in the speed of standing firm "
            "again, not in never falling."]),
        ("A specific attainment named directly", [
            "Dassanasampanna, &lsquo;accomplished in vision&rsquo;, "
            "names a specific attainment rather than praising the "
            "disciple in only general terms &mdash; likely referring "
            "to having gained right view, the clarity that makes "
            "quick recovery from a lapse possible."]),
    ],
    terms=[
        ("bhaddo &amacr;ja&ntilde;&ntilde;o",
         "&ldquo;a fine thoroughbred&rdquo; &mdash; the exact opening "
         "phrase shared with Bela&#7789;&#7789;has&imacr;sa's verse "
         "(Thag 1.16) in Chapter Two."),
        ("khalitv&amacr;",
         "&ldquo;having stumbled&rdquo; &mdash; the moment of lapse "
         "this verse openly acknowledges."),
        ("patiti&#7789;&#7789;hati",
         "&ldquo;stands firm again&rdquo; &mdash; the recovery this "
         "verse's confidence rests on."),
        ("dassanasampanna",
         "&ldquo;accomplished in vision&rdquo; &mdash; a specific "
         "attainment, likely referring to right view."),
        ("s&amacr;vaka",
         "&ldquo;disciple&rdquo; &mdash; the verse's closing "
         "description of the Buddha's student."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.45:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse say about a fine thoroughbred?",
         "opts": [
             "That it never stumbles",
             "That it always falls and never recovers",
             "That it may stumble, but soon stands firm again",
             "No horse is mentioned"],
         "correct": 2,
         "expl": "Resilience after a lapse, not flawless perfection."},
        {"q": "What earlier poem in this collection shares this verse's opening phrase, 'a fine thoroughbred'?",
         "opts": [
             "Belaṭṭhasīsa's verse (Thag 1.16) in Chapter Two",
             "Sirivaḍḍha's verse in this same chapter",
             "No earlier poem shares this phrase",
             "Sumaṅgala's verse, just before this one"],
         "correct": 0,
         "expl": "The exact same Pali opening, used to a different point."},
        {"q": "How does this verse's horse differ from the one in Belaṭṭhasīsa's verse?",
         "opts": [
             "They are identical in every respect",
             "This one never runs at all",
             "This one stumbles first, unlike the earlier verse's uninterrupted ease",
             "There is no difference"],
         "correct": 2,
         "expl": "A shared image put to a different rhetorical use."},
        {"q": "What does this verse's confidence rest on?",
         "opts": [
             "Never stumbling at all",
             "The speed of recovery after a stumble",
             "Avoiding all practice entirely",
             "Nothing specific is stated"],
         "correct": 1,
         "expl": "Resilience, not flawlessness."},
        {"q": "What does 'dassanasampanna' mean?",
         "opts": [
             "Accomplished in vision",
             "Fearful of the future",
             "Wealthy and powerful",
             "A type of monastic robe"],
         "correct": 0,
         "expl": "A specific attainment, likely referring to right view."},
        {"q": "What does 'khalitvā' mean?",
         "opts": [
             "Having stumbled",
             "Having taught",
             "Having traveled far",
             "Having eaten"],
         "correct": 0,
         "expl": "The moment of lapse this verse openly acknowledges."},
        {"q": "What does 'patitiṭṭhati' mean?",
         "opts": [
             "Falls permanently",
             "Flees",
             "Sleeps",
             "Stands firm again"],
         "correct": 3,
         "expl": "The recovery this verse's confidence rests on."},
        {"q": "Does this verse declare complete, uninterrupted freedom from fault?",
         "opts": [
             "Yes, it claims total flawlessness",
             "No — it openly acknowledges the possibility of stumbling",
             "The verse does not address this at all",
             "It denies any disciple could ever recover"],
         "correct": 1,
         "expl": "Honesty about lapses, paired with confidence in recovery."},
        {"q": "What does 'sāvaka' mean?",
         "opts": [
             "Enemy",
             "Disciple",
             "Stranger",
             "River"],
         "correct": 1,
         "expl": "The verse's closing description of the Buddha's student."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The fifth poem, following Sānu's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("The same phrase, a different point", [
            "'a fine thoroughbred,'",
            "this time it stumbles"
        ]),
        ("Confidence in recovery, not perfection", [
            "stumbles, then",
            "stands firm again"
        ]),
        ("A named attainment", [
            "accomplished in vision,",
            "not just praised generally"
        ]),
        ("Honesty about lapses", [
            "even fine horses",
            "sometimes stumble"
        ]),
    ],
    further=[
        '<a href="%s/thag1.45/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.16.html">Thag 1.16 &mdash; Bela&#7789;'
        "&#7789;has&imacr;sa</a> &mdash; sharing this verse's opening "
        "phrase, 'a fine thoroughbred', used to a different point.",
        '<a href="thag-1.44.html">Thag 1.44 &mdash; S&amacr;nu</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.46 — Samiddhi
# --------------------------------------------------------------------------- #
page(
    1, 46, "Samiddhi", "Samiddhi",
    meta_title="Thag 1.46 — Samiddhi | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Samiddhi's verse, a calm self-report of growth pivoting "
        "into a defiant challenge to whoever conjures illusions "
        "against him. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting; a calm report of growth, "
                    "then a direct challenge to an unnamed 'you'"),
        ("Speaker", "Samiddhi, describing his own progress, then "
                    "confronting an unnamed adversary"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a calm report pivoting sharply into direct "
                       "defiance"),
    ],
    why=(
        "Samiddhi's verse opens quietly &mdash; faith, growing "
        "mindfulness and wisdom, a serene mind &mdash; before pivoting "
        "sharply: &lsquo;make whatever illusions you want, it doesn't "
        "bother me&rsquo;, a direct challenge to an unnamed "
        "adversary, never named outright."),
    guide=[
        ("A calm report, then a sudden pivot to defiance", [
            "The verse's first four lines read as a settled, "
            "unremarkable self-report &mdash; faith, growth, "
            "serenity. Its final two lines shift register entirely, "
            "addressing someone directly with an open challenge, "
            "&lsquo;make whatever illusions you want&rsquo;."]),
        ("An adversary implied, not named", [
            "Unlike Nandiya's verse (Thag 1.25), which addresses "
            "M&amacr;ra directly as &lsquo;Dark One&rsquo;, this "
            "verse's &lsquo;you&rsquo; is never named &mdash; the "
            "conjuring of r&umacr;p&amacr;ni, illusory forms or "
            "apparitions, strongly implies the same adversary without "
            "stating it outright."]),
        ("Illusion specifically named as the threat", [
            "R&umacr;p&amacr;ni, &lsquo;forms&rsquo; or "
            "&lsquo;illusions&rsquo;, names the specific kind of "
            "attack being dismissed &mdash; not physical harm or "
            "argument, but conjured appearances meant to disturb, "
            "declared powerless against Samiddhi's serenity."]),
    ],
    terms=[
        ("saddh&amacr;",
         "&ldquo;faith&rdquo; &mdash; the stated reason Samiddhi went "
         "forth."),
        ("vu&#7693;&#7693;ha",
         "&ldquo;grown&rdquo; or &ldquo;increased&rdquo; &mdash; "
         "describing his mindfulness and wisdom."),
        ("susam&amacr;hita",
         "&ldquo;well immersed&rdquo; or &ldquo;serene&rdquo; "
         "&mdash; describing his mind before the verse's pivot."),
        ("r&umacr;pa",
         "&ldquo;form&rdquo; or &ldquo;illusion&rdquo; &mdash; the "
         "specific kind of conjured attack this verse dismisses."),
        ("by&amacr;dhayissasi",
         "&ldquo;you will afflict&rdquo; &mdash; the verb this verse "
         "denies has any power over Samiddhi."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.46:1.1-1.6"),
    ],
    quiz=[
        {"q": "How does this verse's first four lines read?",
         "opts": [
             "As an open challenge to an adversary",
             "As a calm, settled self-report of growth",
             "As a narrative journey",
             "As a numerical formula"],
         "correct": 1,
         "expl": "Faith, growth, and serenity, before the verse's pivot."},
        {"q": "What happens in this verse's final two lines?",
         "opts": [
             "The verse simply repeats its opening",
             "The verse ends without further development",
             "The register shifts sharply to direct defiance",
             "A new narrator is introduced by name"],
         "correct": 2,
         "expl": "A sudden pivot from calm report to open challenge."},
        {"q": "Does this verse name its adversary directly, as Nandiya's verse names Māra?",
         "opts": [
             "Yes, by the same epithet 'Dark One'",
             "No — the adversary is never named outright",
             "Yes, by a different specific name",
             "No adversary is implied at all"],
         "correct": 1,
         "expl": "Strongly implied through the mention of conjured illusions, but not stated outright."},
        {"q": "What kind of attack does this verse's challenge dismiss?",
         "opts": [
             "Conjured illusions or forms",
             "Physical violence",
             "Verbal argument",
             "Financial loss"],
         "correct": 0,
         "expl": "Rūpāni, illusory forms, named specifically."},
        {"q": "Why did Samiddhi say he went forth?",
         "opts": [
             "Out of fear",
             "Out of obligation to his family",
             "No reason is given",
             "Out of faith"],
         "correct": 3,
         "expl": "The verse's opening stated motivation."},
        {"q": "What does 'vuḍḍha' mean?",
         "opts": [
             "Grown or increased",
             "Diminished",
             "Fearful",
             "Wealthy"],
         "correct": 0,
         "expl": "Describing his mindfulness and wisdom."},
        {"q": "What does 'susamāhita' describe?",
         "opts": [
             "A troubled, restless mind",
             "A monastic robe",
             "A river",
             "A well immersed, serene mind"],
         "correct": 3,
         "expl": "Samiddhi's mental state before the verse's pivot."},
        {"q": "What does the verse claim about the effect of these illusions on Samiddhi?",
         "opts": [
             "That they will eventually overwhelm him",
             "That they have no effect on him at all",
             "That they might succeed if repeated enough",
             "The verse does not address this"],
         "correct": 1,
         "expl": "A flat denial of any power over him."},
        {"q": "What does 'rūpa' mean in this verse's closing lines?",
         "opts": [
             "Form or illusion",
             "A monastic title",
             "A type of food",
             "A river crossing"],
         "correct": 0,
         "expl": "The specific kind of conjured attack being dismissed."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The sixth poem, following Ramaṇīyavihārin's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("A calm report, then a sharp pivot", [
            "faith, growth, serenity —",
            "then a direct challenge"
        ]),
        ("An adversary implied, not named", [
            "unlike 'Dark One,'",
            "this 'you' stays unnamed"
        ]),
        ("Illusion, specifically dismissed", [
            "conjured forms,",
            "declared powerless"
        ]),
        ("From inward growth to outward defiance", [
            "mindfulness and wisdom,",
            "then a challenge issued"
        ]),
    ],
    further=[
        '<a href="%s/thag1.46/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.45.html">Thag 1.45 &mdash; Rama&#7751;'
        "&imacr;yavih&amacr;rin</a> &mdash; the poem immediately "
        "before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.47 — Ujjaya
# --------------------------------------------------------------------------- #
page(
    1, 47, "Ujjaya", "Ujjaya",
    meta_title="Thag 1.47 — Ujjaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ujjaya's verse, direct homage to the Buddha as hero, freed "
        "in every way, framing Ujjaya's own attainment as walking his "
        "footsteps. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative setting; a direct address of "
                    "homage to the Buddha"),
        ("Speaker", "Ujjaya, addressing the Buddha in the second "
                    "person"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "direct homage, framing personal attainment as "
                       "derivative of the Buddha's own"),
    ],
    why=(
        "&lsquo;Homage to you, O Buddha, O hero, freed in every "
        "way!&rsquo; &mdash; unlike verses declaring a monk's own "
        "attainment or describing him from outside, this one speaks "
        "directly to the Buddha, framing Ujjaya's freedom from "
        "defilements as walking a path the Buddha himself already "
        "left behind."),
    guide=[
        ("Direct address, not third-person praise or self-declaration", [
            "Most verses in this collection either describe a monk "
            "from outside or have him declare his own attainment. "
            "This one does neither &mdash; it speaks in the second "
            "person, directly to the Buddha, in a register of "
            "worship and gratitude rather than description."]),
        ("An unqualified liberation, named directly", [
            "&lsquo;Freed in every way&rsquo;, vippamutto sabbadhi, "
            "leaves no qualification or partial measure &mdash; total "
            "liberation, attributed specifically to the one being "
            "addressed."]),
        ("Ujjaya's own attainment framed as following the Buddha's footsteps", [
            "Apad&amacr;na, translated &lsquo;the fruits of your "
            "practice&rsquo;, literally suggests a footstep or track "
            "&mdash; Ujjaya describes himself as dwelling within that "
            "track, his own freedom from defilements presented as "
            "directly derivative of the path the Buddha already "
            "walked."]),
    ],
    terms=[
        ("namo",
         "&ldquo;homage&rdquo; &mdash; the verse's opening word, "
         "addressed directly to the Buddha."),
        ("v&imacr;ra",
         "&ldquo;hero&rdquo; &mdash; an epithet for the Buddha, "
         "sharing its root with V&imacr;ra's own name earlier in this "
         "book."),
        ("vippamutta",
         "&ldquo;freed&rdquo; or &ldquo;liberated&rdquo; &mdash; "
         "paired with sabbadhi, &lsquo;in every way&rsquo;, for a "
         "total, unqualified liberation."),
        ("apad&amacr;na",
         "&ldquo;footstep&rdquo; or &ldquo;track&rdquo; &mdash; the "
         "image behind &lsquo;the fruits of your practice&rsquo;, "
         "framing Ujjaya's own path as following the Buddha's."),
        ("an&amacr;sava",
         "&ldquo;without defilements&rdquo; or &ldquo;without "
         "effluents&rdquo; &mdash; describing Ujjaya's own attained "
         "state, closing the verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.47:1.1-1.4"),
    ],
    quiz=[
        {"q": "Who does this verse address directly?",
         "opts": [
             "Another monk",
             "Māra",
             "The Buddha, in the second person",
             "Ujjaya's own mother"],
         "correct": 2,
         "expl": "A register of worship and gratitude, not description."},
        {"q": "How does this verse's address compare to most other poems in this collection?",
         "opts": [
             "Identical to every other poem",
             "Most describe a monk from outside or have him self-declare; this one speaks directly to the Buddha",
             "This verse contains no address of any kind",
             "This verse addresses a river"],
         "correct": 1,
         "expl": "A distinct register among this collection's poems."},
        {"q": "How is the Buddha's liberation described in this verse?",
         "opts": [
             "Partial and qualified",
             "Still incomplete",
             "Freed in every way, without qualification",
             "Not mentioned at all"],
         "correct": 2,
         "expl": "An unqualified, total liberation."},
        {"q": "What does 'apadāna' literally suggest?",
         "opts": [
             "A footstep or track",
             "A river crossing",
             "A monastic robe",
             "A type of meal"],
         "correct": 0,
         "expl": "The image behind 'the fruits of your practice'."},
        {"q": "How does Ujjaya frame his own attainment in this verse?",
         "opts": [
             "As entirely unrelated to the Buddha",
             "As achieved before the Buddha's teaching existed",
             "As a mystery even to himself",
             "As following directly within the Buddha's own track"],
         "correct": 3,
         "expl": "His own freedom presented as derivative of the Buddha's path."},
        {"q": "What does 'vīra' mean?",
         "opts": [
             "Hero",
             "Enemy",
             "Stranger",
             "River"],
         "correct": 0,
         "expl": "An epithet for the Buddha, sharing a root with Vīra's own name earlier in this book."},
        {"q": "What does 'anāsava' mean?",
         "opts": [
             "Without defilements",
             "Full of defilements",
             "Wealthy",
             "Fearful"],
         "correct": 0,
         "expl": "Describing Ujjaya's own attained state, closing the verse."},
        {"q": "What does 'namo' mean?",
         "opts": [
             "Question",
             "Homage",
             "Warning",
             "Farewell"],
         "correct": 1,
         "expl": "The verse's opening word, addressed to the Buddha."},
        {"q": "Does this verse describe Ujjaya's attainment as separate from the Buddha's, or connected to it?",
         "opts": [
             "As entirely separate and unconnected",
             "As directly connected, following the Buddha's own path",
             "The verse does not address this at all",
             "As opposed to the Buddha's path"],
         "correct": 1,
         "expl": "A path explicitly framed as shared, not independently discovered."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The seventh poem, following Samiddhi's"],
         "correct": 3,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Homage, not description", [
            "spoken directly",
            "to the Buddha himself"
        ]),
        ("Freed, without qualification", [
            "in every way,",
            "not partially"
        ]),
        ("A path already walked", [
            "footsteps followed,",
            "not discovered alone"
        ]),
        ("Gratitude as its own register", [
            "worship,",
            "distinct from self-declaration"
        ]),
    ],
    further=[
        '<a href="%s/thag1.47/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.46.html">Thag 1.46 &mdash; Samiddhi</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.48 — Sa&ntilde;jaya
# --------------------------------------------------------------------------- #
page(
    1, 48, "Sa&ntilde;jaya", "Sa&ntilde;jaya",
    meta_title="Thag 1.48 — Sañjaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sañjaya's verse, sharing an exact line with Samiddhi's verse "
        "two poems earlier, and reporting the absence of one "
        "specific kind of thought. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative setting; a report of experience "
                    "since ordination"),
        ("Speaker", "Sañjaya, describing his own mind since going "
                    "forth"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a precise claim about the absence of one "
                       "specific kind of thought"),
    ],
    why=(
        "&lsquo;Since I went forth from the lay life to "
        "homelessness, I've not been aware of any thought that is "
        "ignoble and hateful&rsquo;. This verse's second line "
        "matches Samiddhi's verse (Thag 1.46), two poems earlier, "
        "word for word &mdash; though what follows diverges "
        "completely."),
    guide=[
        ("A shared line, with different openings and different endings", [
            "Agārasmānagāriyaṁ, &lsquo;from the household to "
            "homelessness&rsquo;, appears verbatim in both this verse "
            "and Samiddhi's (Thag 1.46). Their opening lines differ "
            "slightly &mdash; Samiddhi names faith as his reason, "
            "Sañjaya simply marks a moment in time &mdash; and their "
            "content diverges entirely after that one shared line."]),
        ("A precise claim, not a general one", [
            "Sañjaya does not claim a general purity of mind; he "
            "names exactly what has not arisen: thought that is "
            "&lsquo;ignoble and hateful&rsquo;, anariyaṁ "
            "dosasaṁhitaṁ &mdash; a specific target, in the same "
            "spirit as this collection's other verses that name their "
            "objects precisely rather than vaguely."]),
        ("Reported absence, not active elimination", [
            "N&amacr;bhij&amacr;n&amacr;mi, &lsquo;I've not been "
            "aware of&rsquo;, frames this as a report of direct "
            "experience rather than a claim of having actively "
            "eliminated something &mdash; the thought simply hasn't "
            "arisen to be noticed, not &lsquo;I destroyed it&rsquo;."]),
    ],
    terms=[
        ("pabbajita",
         "&ldquo;gone forth&rdquo; &mdash; marking the moment this "
         "verse measures from."),
        ("ag&amacr;rasm&amacr;n&amacr;g&amacr;riya&#7745;",
         "&ldquo;from the household to homelessness&rdquo; &mdash; "
         "the line shared verbatim with Samiddhi's verse (Thag 1.46)."),
        ("abhij&amacr;n&amacr;ti",
         "&ldquo;to know directly&rdquo; or &ldquo;to be aware "
         "of&rdquo; &mdash; negated in this verse to report an "
         "absence, not an elimination."),
        ("sa&#7749;kappa",
         "&ldquo;thought&rdquo; or &ldquo;intention&rdquo; &mdash; "
         "the object this verse says has not arisen."),
        ("dosasa&#7745;hita",
         "&ldquo;connected with hatred&rdquo; or "
         "&ldquo;ill-will&rdquo; &mdash; describing the specific kind "
         "of thought named."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.48:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's second line share with Samiddhi's verse (Thag 1.46)?",
         "opts": [
             "Nothing — they are unrelated",
             "Only the closing attribution",
             "The speaker's name",
             "The exact same line, word for word"],
         "correct": 3,
         "expl": "Agārasmānagāriyaṁ, shared verbatim between the two verses."},
        {"q": "How do the two verses' opening lines compare?",
         "opts": [
             "They are word for word identical",
             "Sañjaya's verse has no opening line at all",
             "They contradict each other directly",
             "They differ slightly — Samiddhi names faith, Sañjaya simply marks a moment"],
         "correct": 3,
         "expl": "A shared second line, but different first lines."},
        {"q": "What specific kind of thought does Sañjaya say he has not been aware of?",
         "opts": [
             "Any thought at all",
             "Thought that is ignoble and hateful",
             "Thoughts about food",
             "Thoughts about the weather"],
         "correct": 1,
         "expl": "A precise target, not a vague general claim."},
        {"q": "How is this claim framed — as active elimination, or reported absence?",
         "opts": [
             "As active, deliberate elimination",
             "As a reported absence of experience",
             "As a future goal not yet reached",
             "The verse makes no such claim"],
         "correct": 1,
         "expl": "'I've not been aware of', not 'I destroyed'."},
        {"q": "What does 'saṅkappa' mean?",
         "opts": [
             "Thought or intention",
             "A monastic robe",
             "A river",
             "A type of food"],
         "correct": 0,
         "expl": "The object this verse says has not arisen."},
        {"q": "What does 'dosasaṁhita' describe?",
         "opts": [
             "Connected with hatred or ill-will",
             "Connected with generosity",
             "Connected with wisdom",
             "Connected with fear alone"],
         "correct": 0,
         "expl": "The specific quality of the thought this verse names."},
        {"q": "What does 'abhijānāti' mean?",
         "opts": [
             "To know directly or be aware of",
             "To forget entirely",
             "To travel far",
             "To teach others"],
         "correct": 0,
         "expl": "Negated in this verse to report an absence."},
        {"q": "Does Sañjaya's verse diverge from Samiddhi's after their shared line?",
         "opts": [
             "No, they remain identical throughout",
             "Yes — their content diverges completely after that one shared line",
             "The verses have no shared line at all",
             "Sañjaya's verse simply repeats Samiddhi's in full"],
         "correct": 1,
         "expl": "One shared line, otherwise two distinct verses."},
        {"q": "What does 'pabbajita' mean?",
         "opts": [
             "Returned home",
             "Wealthy",
             "Gone forth",
             "Ill"],
         "correct": 2,
         "expl": "Marking the moment this verse measures from."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "The eighth poem, following Ujjaya's",
             "It is not part of this chapter"],
         "correct": 2,
         "expl": "Continuing the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("One line, shared exactly", [
            "from the household",
            "to homelessness"
        ]),
        ("A precise target, not a vague claim", [
            "ignoble and hateful,",
            "named specifically"
        ]),
        ("Reported absence, not conquest", [
            "'I've not been aware,'",
            "not 'I destroyed'"
        ]),
        ("Two verses, one shared line", [
            "different openings,",
            "different content after"
        ]),
    ],
    further=[
        '<a href="%s/thag1.48/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.46.html">Thag 1.46 &mdash; Samiddhi</a> '
        "&mdash; sharing this verse's second line exactly.",
        '<a href="thag-1.47.html">Thag 1.47 &mdash; Ujjaya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.49 — R&amacr;ma&#7751;eyyaka
# --------------------------------------------------------------------------- #
page(
    1, 49, "R&amacr;ma&#7751;eyyaka", "R&amacr;ma&#7751;eyyaka",
    meta_title="Thag 1.49 — Rāmaṇeyyaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Rāmaṇeyyaka's verse, an onomatopoeic burst of birdsong "
        "tested against a mind devoted entirely to oneness. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A place filled with chirping, cheeping birds"),
        ("Speaker", "Rāmaṇeyyaka, reporting his own unwavering mind"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "vivid onomatopoeic sound tested against "
                       "one-pointed stillness"),
    ],
    why=(
        "This verse opens with sound itself, rendered almost as "
        "onomatopoeia &mdash; the chirping and cheeping of birds "
        "&mdash; before declaring that none of it moves his mind at "
        "all, &lsquo;for I'm devoted to oneness&rsquo;. The "
        "noisiest possible opening sets up the strongest possible "
        "contrast with total stillness."),
    guide=[
        ("Sound rendered almost as its own noise", [
            "Cihacih&amacr;bhinadite echoes the very chirping it "
            "names, an onomatopoeic word giving this verse's opening "
            "a vivid, almost playful auditory texture rare among this "
            "collection's more austere imagery."]),
        ("Maximum noise, tested against total stillness", [
            "By naming specifically the chirping and cheeping of "
            "birds &mdash; not a vague &lsquo;disturbance&rsquo; "
            "&mdash; the verse sets up the strongest possible contrast "
            "with &lsquo;my mind doesn't waver&rsquo;, proving "
            "stability against a concrete, lively distraction rather "
            "than an abstract one."]),
        ("A name that may echo the poem just five poems earlier", [
            "R&amacr;ma&#7751;eyyaka shares its root, ramaṇīya "
            "(&lsquo;delightful&rsquo;), with Rama&#7751;&imacr;"
            "yavih&amacr;rin, &lsquo;one who dwells delightfully"
            "&rsquo;, the speaker of Thag 1.45 earlier in this "
            "chapter &mdash; an etymological echo worth noting, "
            "without asserting any further connection between the two "
            "names."]),
    ],
    terms=[
        ("cihacih&amacr;bhinadita",
         "an onomatopoeic word for chirping &mdash; the verse's "
         "opening burst of bird sound."),
        ("sippik&amacr;bhiruta",
         "&ldquo;cheeping&rdquo; or warbling &mdash; paired with the "
         "chirping in the verse's first line."),
        ("phandati",
         "&ldquo;wavers&rdquo; or &ldquo;trembles&rdquo; &mdash; "
         "negated in this verse to describe an unmoved mind."),
        ("ekattanirata",
         "&ldquo;devoted to oneness&rdquo; &mdash; the specific "
         "one-pointed quality this verse credits with its stability."),
        ("citta",
         "&ldquo;mind&rdquo; &mdash; the subject of this verse's "
         "central claim."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.49:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's opening describe?",
         "opts": [
             "A silent, empty landscape",
             "A crowded marketplace",
             "The chirping and cheeping of birds",
             "A storm"],
         "correct": 2,
         "expl": "Vivid, almost onomatopoeic bird sound."},
        {"q": "What does the verse say about Rāmaṇeyyaka's mind amid this sound?",
         "opts": [
             "It wavers constantly",
             "It doesn't waver at all",
             "It wavers only slightly",
             "The verse does not describe his mind"],
         "correct": 1,
         "expl": "Total stability, tested against a concrete distraction."},
        {"q": "Why does the verse's mind stay unmoved, according to its own closing line?",
         "opts": [
             "No reason is given",
             "Because he is devoted to oneness",
             "Because he cannot hear the birds",
             "Because he is asleep"],
         "correct": 1,
         "expl": "Ekattanirata, a specific one-pointed quality."},
        {"q": "How does naming specific bird sounds, rather than a vague 'disturbance', affect this verse's contrast?",
         "opts": [
             "It weakens the contrast",
             "It has no effect on the verse's meaning",
             "It sharpens the contrast, testing stability against something concrete and lively",
             "It removes the contrast entirely"],
         "correct": 2,
         "expl": "A concrete distraction, not an abstract one."},
        {"q": "What earlier poem's speaker shares a root with Rāmaṇeyyaka's own name?",
         "opts": [
             "No earlier poem shares any root with this name",
             "Ramaṇīyavihārin, from Thag 1.45 earlier in this chapter",
             "Sirivaḍḍha, opening this chapter",
             "Sumaṅgala"],
         "correct": 1,
         "expl": "An etymological echo, noted without asserting a further connection."},
        {"q": "What does 'phandati' mean?",
         "opts": [
             "Wavers or trembles",
             "Sings",
             "Sleeps",
             "Teaches"],
         "correct": 0,
         "expl": "Negated in this verse to describe an unmoved mind."},
        {"q": "What does 'ekattanirata' mean?",
         "opts": [
             "Afraid of solitude",
             "Devoted to wealth",
             "A type of hut",
             "Devoted to oneness"],
         "correct": 3,
         "expl": "The specific quality this verse credits with its stability."},
        {"q": "What kind of word is 'cihacihābhinadita'?",
         "opts": [
             "An onomatopoeic word echoing the sound it names",
             "A borrowed foreign word",
             "A purely abstract philosophical term",
             "A proper name"],
         "correct": 0,
         "expl": "A rare instance of sound-mimicking vocabulary in this collection."},
        {"q": "What does 'citta' mean?",
         "opts": [
             "Mind",
             "Body",
             "Speech",
             "A river"],
         "correct": 0,
         "expl": "The subject of this verse's central claim."},
        {"q": "Where does this poem fall in Chapter Five?",
         "opts": [
             "It opens the chapter",
             "It closes the chapter",
             "It is not part of this chapter",
             "The ninth poem, following Sañjaya's"],
         "correct": 3,
         "expl": "Second to last in the chapter's sequence of ten poems."},
    ],
    marginalia=[
        ("Sound that mimics itself", [
            "chirping rendered",
            "almost as its own noise"
        ]),
        ("Maximum noise, total stillness", [
            "birds calling,",
            "a mind unmoved"
        ]),
        ("Devoted to oneness", [
            "not silence itself,",
            "but one-pointedness"
        ]),
        ("A name, an echo", [
            "Rāmaṇeyyaka,",
            "recalling Ramaṇīyavihārin"
        ]),
    ],
    further=[
        '<a href="%s/thag1.49/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.45.html">Thag 1.45 &mdash; Rama&#7751;'
        "&imacr;yavih&amacr;rin</a> &mdash; sharing this poem's "
        "speaker's name-root, ramaṇīya.",
        '<a href="thag-1.48.html">Thag 1.48 &mdash; Sa&ntilde;'
        "jaya</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.50 — Vimala (1st)
# --------------------------------------------------------------------------- #
page(
    1, 50, "Vimala", "Vimala (1st)",
    meta_title="Thag 1.50 — Vimala (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vimala's verse, closing Chapter Five with a celestial storm "
        "of mythological allusion set against a perfectly stilled "
        "mind. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Five &middot; Poem 10 of 10",
    glance=[
        ("Setting", "A storm of celestial origin: a mythical lake "
                    "pouring, a Vedic wind-god's breeze, lightning "
                    "across the sky"),
        ("Speaker", "Vimala, reporting his own stilled mind"),
        ("Form", "One four-line verse, followed in the Pali by an "
                 "untranslated chapter colophon and mnemonic summary "
                 "verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "mythological storm imagery closing a chapter "
                       "that opened the same way"),
    ],
    why=(
        "&lsquo;The celestial lake Dhara&#7751;&imacr; pours, the "
        "heavenly gale blows, and lightning flashes across the "
        "sky!&rsquo; Vimala's verse closes Chapter Five exactly as it "
        "opened &mdash; a storm, drawn from inherited mythological "
        "vocabulary, set against a mind &lsquo;stilled&rsquo; and "
        "&lsquo;serene&rsquo;."),
    guide=[
        ("A chapter's bookend, completed", [
            "Sirivaḍḍha's verse (Thag 1.41) opened this chapter with "
            "lightning over a mountain cleft, absorption undisturbed "
            "inside it. This closing poem returns to the same "
            "pairing &mdash; storm outside, stillness within &mdash; "
            "completing a matched frame around all ten poems of "
            "Chapter Five."]),
        ("Storm imagery drawn from named mythology", [
            "Sujato's note identifies Dhara&#7751;&imacr; as an "
            "allusion to a specific celestial lake, the traditional "
            "source of rain, and M&amacr;luto as a poetic word for "
            "&lsquo;breeze&rsquo; derived from the Maruts, the Vedic "
            "storm gods &mdash; this verse's weather is not generic, "
            "but built from inherited, named mythological vocabulary."]),
        ("A closing word shared with Samiddhi's verse", [
            "Susamāhitaṁ, &lsquo;serene&rsquo; or &lsquo;well "
            "immersed&rsquo;, closes this verse exactly as it closed "
            "Samiddhi's (Thag 1.46) earlier in this same chapter "
            "&mdash; a small echo of vocabulary within Chapter Five's "
            "own ten poems."]),
        ("A chapter's own close, left untranslated", [
            "As at the end of Chapters One through Four, the Pali "
            "text here carries vaggo pañcamo, &lsquo;the fifth "
            "chapter is finished&rsquo;, followed by an uddāna naming "
            "all ten monks of this chapter in sequence: Sirivaḍḍha, "
            "Revata of the Acacia Wood, Sumaṅgala, Sānu, "
            "Ramaṇīyavihārin, Samiddhi, Ujjaya, Sañjaya, "
            "Rāmaṇeyyaka, and Vimala. Sujato's translation leaves both "
            "untranslated, and neither appears in this page's text "
            "below."]),
    ],
    terms=[
        ("Dhara&#7751;&imacr;",
         "the celestial lake traditionally understood as the source "
         "of rain, per a reference at DN 32."),
        ("M&amacr;luto",
         "a poetic word for &ldquo;breeze&rdquo;, derived from the "
         "Maruts, Vedic gods of the thunderstorm."),
        ("vijjut&amacr;",
         "&ldquo;lightning&rdquo; &mdash; closing this verse's list "
         "of storm imagery."),
        ("vitakka",
         "&ldquo;thoughts&rdquo; &mdash; what this verse says are "
         "stilled, despite the storm around them."),
        ("susam&amacr;hita",
         "&ldquo;serene&rdquo; or &ldquo;well immersed&rdquo; "
         "&mdash; the same word closing Samiddhi's verse (Thag 1.46) "
         "earlier in this chapter."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.50:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three elements of a storm does this verse name?",
         "opts": [
             "A lake pouring, wind blowing, and lightning flashing",
             "Thunder, hail, and snow",
             "A flood, a fire, and an earthquake",
             "None — no storm is described"],
         "correct": 0,
         "expl": "The verse's opening list of celestial storm imagery."},
        {"q": "According to Sujato's note, what does 'Dharaṇī' refer to?",
         "opts": [
             "A river in India",
             "A monastic building",
             "The celestial lake traditionally understood as the source of rain",
             "A mountain range"],
         "correct": 2,
         "expl": "An allusion referenced at DN 32."},
        {"q": "What does 'Māluto' derive from, per the note?",
         "opts": [
             "A local place name",
             "The Maruts, Vedic gods of the thunderstorm",
             "A type of tree",
             "A monastic title"],
         "correct": 1,
         "expl": "Inherited mythological vocabulary for 'breeze'."},
        {"q": "What earlier poem in this chapter does this verse's structure echo, opening and closing the chapter alike?",
         "opts": [
             "No earlier poem is echoed",
             "Sumaṅgala's verse",
             "Sānu's verse",
             "Sirivaḍḍha's verse (Thag 1.41), opening the chapter"],
         "correct": 3,
         "expl": "A matched pair of storm-and-stillness poems bookending Chapter Five."},
        {"q": "What word closes this verse and also closes Samiddhi's verse (Thag 1.46)?",
         "opts": [
             "Vitakka, 'thoughts'",
             "Vijjutā, 'lightning'",
             "No word is shared between the two",
             "Susamāhitaṁ, 'serene'"],
         "correct": 3,
         "expl": "A small echo of vocabulary within this chapter's own poems."},
        {"q": "What does the Pali text carry immediately after this poem, left untranslated by Sujato?",
         "opts": [
             "A love poem",
             "'Vaggo pañcamo' ('the fifth chapter is finished') and an uddāna naming all ten monks of the chapter",
             "A new eleventh poem",
             "Nothing follows this poem in the Pali"],
         "correct": 1,
         "expl": "The same untranslated colophon pattern seen at the end of Chapters One through Four."},
        {"q": "Does this page's text include that closing uddāna?",
         "opts": [
             "Yes, translated in full",
             "No — it is absent from Sujato's translation and not included here",
             "Yes, but only partially",
             "It is included as an image only"],
         "correct": 1,
         "expl": "Consistent with how this site handles untranslated structural material."},
        {"q": "What does 'vitakka' mean?",
         "opts": [
             "Thoughts",
             "A river",
             "A monastic robe",
             "A type of food"],
         "correct": 0,
         "expl": "What this verse says are stilled, despite the storm around them."},
        {"q": "How many monks' verses make up Chapter Five in total?",
         "opts": [
             "Ten",
             "Five",
             "Twenty",
             "One hundred and twenty"],
         "correct": 0,
         "expl": "Sirivaḍḍha through Vimala, named in sequence in the untranslated uddāna."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the final chapter",
             "Exactly one more",
             "Seven more chapters",
             "Twenty more chapters"],
         "correct": 2,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
    ],
    marginalia=[
        ("A chapter's frame, completed", [
            "storm outside,",
            "stillness within — again"
        ]),
        ("Named mythology, not generic weather", [
            "Dharaṇī, the Maruts,",
            "inherited vocabulary"
        ]),
        ("A word echoed within the chapter", [
            "susamāhitaṁ,",
            "closing two verses"
        ]),
        ("A fifth chapter closes", [
            "ten names, tabulated,",
            "left untranslated"
        ]),
    ],
    further=[
        '<a href="%s/thag1.50/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.41.html">Thag 1.41 &mdash; Siriva&#7693;'
        "&#7693;ha</a> &mdash; opening this chapter with a matching "
        "storm-and-stillness image.",
        '<a href="thag-1.49.html">Thag 1.49 &mdash; R&amacr;'
        "ma&#7751;eyyaka</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)
