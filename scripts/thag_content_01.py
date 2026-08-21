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


# --------------------------------------------------------------------------- #
# Thag 1.51 — Godhika
# --------------------------------------------------------------------------- #
page(
    1, 51, "Godhika", "Godhika",
    meta_title="Thag 1.51 — Godhika | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Godhika's verse, opening Chapter Six with the same rain-and-hut "
        "image that opened the whole Theragātha, and a name shared with "
        "the monk of the Godhika Sutta. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 1 of 10",
    glance=[
        ("Setting", "A rain-sheltered hut"),
        ("Speaker", "Godhika, addressing the rain god directly"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "familiar image, reopened to begin a new "
                       "chapter"),
    ],
    why=(
        "Sujato's note on Subhūti's opening poem (Thag 1.1) predicted "
        "this: the rain-god-invited-from-a-hut image &lsquo;recurs many "
        "times in the Theragātha&rsquo;. Chapter Six is where that "
        "prediction pays off in full &mdash; Godhika's verse reopens "
        "the same scene almost fifty poems later, and it will not be "
        "the last time this chapter returns to it."),
    guide=[
        ("The collection's opening image, reopened", [
            "Godhika's second line, &lsquo;Channā me kuṭikā sukhā "
            "nivātā&rsquo; (&lsquo;my hut is roofed and pleasant, "
            "sheltered from the wind&rsquo;), repeats Subhūti's opening "
            "line word for word. The rain god is invited to fall as it "
            "pleases in both poems &mdash; here reordered so the rain "
            "itself opens the verse, before the hut is even "
            "described."]),
        ("A serene mind, stated plainly", [
            "Where Subhūti called his mind &lsquo;serene and "
            "freed&rsquo;, Godhika says only &lsquo;my mind is "
            "serene&rsquo; &mdash; a smaller claim, without the "
            "explicit word for freedom. The difference is subtle, but "
            "worth noticing across the run of poems this one opens."]),
        ("A name shared with a famous, harder story", [
            "This site's Saṁyutta Nikāya collection includes SN 4.23, "
            "&lsquo;With Godhika&rsquo;: a monk who repeatedly reached "
            "and then fell from temporary freedom of heart, and on a "
            "seventh fall took his own life, after which Māra searched "
            "the sky in vain for his consciousness. That text and this "
            "verse share only a name and a Chapter Six theme of huts "
            "and stillness; nothing here confirms they are the same "
            "person, and this reading guide does not assert that they "
            "are &mdash; but the resemblance, and the contrast between "
            "this verse's contentment and that sutta's crisis, is "
            "worth holding side by side."]),
        ("Four poems, one formula, about to begin", [
            "This verse is the first of four in a row (Thag 1.51 "
            "through 1.54) that share the same two opening lines "
            "almost exactly, each varying only its third line before "
            "returning to the same invitation to the rain. Watch for "
            "what each speaker changes."]),
    ],
    terms=[
        ("vassati",
         "&ldquo;rains&rdquo; &mdash; the verb opening this verse, "
         "describing the rain god's fall compared to a sweet song."),
        ("ku&#7789;ik&amacr;",
         "&ldquo;little hut&rdquo; &mdash; the same word that opened "
         "Subhūti's verse, Thag 1.1, at the very start of the "
         "collection."),
        ("susam&amacr;hita",
         "&ldquo;serene&rdquo; or &ldquo;well composed&rdquo; &mdash; "
         "describing Godhika's mind, a smaller claim than Subhūti's "
         "&lsquo;serene and freed&rsquo;."),
        ("deva",
         "&ldquo;god&rdquo;, here the rain deity Godhika invites to "
         "fall as it wishes."),
        ("pavassa",
         "&ldquo;rain forth&rdquo; &mdash; the imperative closing this "
         "verse, echoing Subhūti's own closing invitation to the sky."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.51:1.1-1.4"),
    ],
    quiz=[
        {"q": "What line does Godhika's verse share word for word with Subhūti's opening poem, Thag 1.1?",
         "opts": [
             "A line about a river crossing",
             "A line naming the Buddha",
             "'My hut is roofed and pleasant, sheltered from the wind'",
             "A line about almsfood"],
         "correct": 2,
         "expl": "The same image reopens the collection's rain-and-hut motif."},
        {"q": "According to Sujato's note on Thag 1.1, what does this rain-and-hut image do across the Theragātha?",
         "opts": [
             "It never appears again",
             "It recurs many times",
             "It is unique to Subhūti alone",
             "It only appears in the Therīgātha"],
         "correct": 1,
         "expl": "Chapter Six is where that recurrence arrives in force."},
        {"q": "How does Godhika describe his own mind?",
         "opts": [
             "Anxious",
             "Confused",
             "Angry",
             "Serene"],
         "correct": 3,
         "expl": "A plain, smaller claim than Subhūti's 'serene and freed'."},
        {"q": "What does the verse invite the rain god to do?",
         "opts": [
             "Rain forth, as it wishes",
             "Stop raining immediately",
             "Move to another region",
             "Nothing — no rain god is addressed"],
         "correct": 0,
         "expl": "An unafraid, welcoming address to the sky, as in Thag 1.1."},
        {"q": "What does this reading guide say about SN 4.23, 'With Godhika'?",
         "opts": [
             "It confirms this is definitely the same Godhika",
             "It shares only a name and a hut-and-stillness theme with this verse, without confirmed identity",
             "It has no connection to this collection at all",
             "It is a poem, not a discourse"],
         "correct": 1,
         "expl": "A resemblance worth noting, not a claim this guide asserts as fact."},
        {"q": "In SN 4.23, what happens to the monk named Godhika?",
         "opts": [
             "He becomes a teacher of many students",
             "He travels to another kingdom",
             "He disrobes and returns to lay life",
             "He repeatedly falls from temporary freedom of heart and eventually takes his own life"],
         "correct": 3,
         "expl": "A harder story than this verse's plain contentment."},
        {"q": "How many poems in a row, starting with this one, share nearly the same two opening lines?",
         "opts": [
             "Two",
             "Four",
             "Six",
             "All ten in this chapter"],
         "correct": 1,
         "expl": "Thag 1.51 through 1.54 share the formula, each varying its third line."},
        {"q": "What does 'pavassa' mean?",
         "opts": [
             "Rain forth",
             "Stop",
             "Depart",
             "Listen"],
         "correct": 0,
         "expl": "The imperative closing this verse's invitation to the sky."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "It opens Chapter Six, the Book of the Ones' sixth chapter",
             "It closes the entire collection",
             "It is part of the Book of the Twos",
             "It opens Chapter One"],
         "correct": 0,
         "expl": "The first of ten poems in this new chapter."},
        {"q": "What object does Godhika's verse share with Subhūti's, at the very start of the collection?",
         "opts": [
             "A begging bowl",
             "A robe",
             "A hut",
             "A river"],
         "correct": 2,
         "expl": "The same concrete image, reopened almost fifty poems later."},
    ],
    marginalia=[
        ("An old image, reopened", [
            "same hut, same rain,",
            "fifty poems later"
        ]),
        ("A prediction paying off", [
            "Sujato said it recurs;",
            "here it is again"
        ]),
        ("A name, not a claim", [
            "Godhika twice —",
            "resemblance, not proof"
        ]),
        ("Four poems, one formula", [
            "same two lines,",
            "then each one differs"
        ]),
    ],
    further=[
        '<a href="%s/thag1.51/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../samyutta-nikaya/sn-4.23.html">SN 4.23 &mdash; With '
        "Godhika</a> &mdash; a discourse about a monk sharing this "
        "name, its connection to this verse unconfirmed but worth "
        "holding side by side.",
        '<a href="thag-1.50.html">Thag 1.50 &mdash; Vimala '
        "(1st)</a> &mdash; the poem immediately before this one, "
        "closing Chapter Five.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.52 — Sub&amacr;hu
# --------------------------------------------------------------------------- #
page(
    1, 52, "Sub&amacr;hu", "Sub&amacr;hu",
    meta_title="Thag 1.52 — Subāhu | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Subāhu's verse, the second in Chapter Six's rain-and-hut "
        "formula, naming mindfulness immersed in the body as his one "
        "variation. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 2 of 10",
    glance=[
        ("Setting", "A rain-sheltered hut"),
        ("Speaker", "Subāhu, addressing the rain god directly"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same formula, one word changed"),
    ],
    why=(
        "Subāhu's verse repeats Godhika's opening two lines almost "
        "exactly, then varies only its third line: instead of a "
        "serene mind in general, Subāhu names his mind as "
        "&lsquo;immersed in the body&rsquo; &mdash; a specific nod to "
        "k&amacr;yagat&amacr;sati, mindfulness of the body, as his own "
        "particular practice inside the shared formula."),
    guide=[
        ("The same two lines, once more", [
            "Subāhu's first two lines &mdash; the rain falling like a "
            "sweet song, the hut roofed and pleasant &mdash; are "
            "identical to Godhika's, continuing the run of near-"
            "identical openings that began this chapter."]),
        ("One word changed: the body, not just the mind", [
            "Where Godhika said only &lsquo;my mind is serene&rsquo;, "
            "Subāhu specifies &lsquo;my mind is immersed in the "
            "body&rsquo; &mdash; naming k&amacr;yagat&amacr;sati "
            "specifically, a distinct meditative theme (mindfulness "
            "grounded in awareness of the body) rather than a generic "
            "description of calm."]),
        ("A formula built for small variation", [
            "Two poems into this run, the pattern is now visible: each "
            "speaker keeps the shared frame and changes exactly one "
            "line, using it to name what is most particular about "
            "their own practice. Watch for what the next two poems "
            "choose to name."]),
    ],
    terms=[
        ("k&amacr;ye",
         "&ldquo;in the body&rdquo; &mdash; the word Subāhu adds to "
         "the shared formula, specifying where his mind is immersed."),
        ("susam&amacr;hita",
         "&ldquo;serene&rdquo; or &ldquo;well composed&rdquo; &mdash; "
         "shared with Godhika's verse, here applied specifically to "
         "the body."),
        ("k&amacr;yagat&amacr;sati",
         "&ldquo;mindfulness immersed in the body&rdquo; &mdash; the "
         "meditative theme this verse's third line points toward, "
         "though the compound itself is not spelled out in the "
         "verse."),
        ("ku&#7789;ik&amacr;",
         "&ldquo;little hut&rdquo; &mdash; the shared setting of this "
         "whole run of poems."),
        ("pavassa",
         "&ldquo;rain forth&rdquo; &mdash; the closing invitation, "
         "identical to Godhika's."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.52:1.1-1.4"),
    ],
    quiz=[
        {"q": "How do Subāhu's first two lines compare to Godhika's verse just before it?",
         "opts": [
             "Completely different",
             "Nearly identical",
             "Only the setting matches",
             "Only the rain image matches"],
         "correct": 1,
         "expl": "The same shared opening formula continues."},
        {"q": "What does Subāhu specify about his mind, unlike Godhika?",
         "opts": [
             "That it is anxious",
             "That it is confused",
             "That it is immersed in the body",
             "Nothing is said about his mind"],
         "correct": 2,
         "expl": "A specific nod toward mindfulness grounded in the body."},
        {"q": "What meditative theme does this verse's third line point toward?",
         "opts": [
             "Loving-kindness meditation",
             "Walking meditation",
             "Breath counting",
             "Mindfulness immersed in the body"],
         "correct": 3,
         "expl": "Kāyagatāsati, though the compound isn't spelled out directly."},
        {"q": "What is the pattern emerging across this run of poems, according to this reading guide?",
         "opts": [
             "Each poem is entirely unrelated to the others",
             "Each speaker keeps the shared frame and varies exactly one line",
             "Every line changes each time",
             "No pattern is visible yet"],
         "correct": 1,
         "expl": "A formula built for small, telling variation."},
        {"q": "What does the verse invite the rain god to do?",
         "opts": [
             "Rain forth, as it wishes",
             "Stop raining",
             "Move elsewhere",
             "Nothing is addressed to the rain god"],
         "correct": 0,
         "expl": "The same closing invitation as Godhika's verse."},
        {"q": "What does 'kāye' mean?",
         "opts": [
             "In the forest",
             "In the sky",
             "In the village",
             "In the body"],
         "correct": 3,
         "expl": "The word Subāhu adds to the shared formula."},
        {"q": "How many poems in this chapter's opening run share nearly the same two opening lines?",
         "opts": [
             "Two",
             "Six",
             "All ten",
             "Four"],
         "correct": 3,
         "expl": "Thag 1.51 through 1.54, this poem being the second."},
        {"q": "Where does this poem fall in the chapter?",
         "opts": [
             "It is the first poem",
             "It is the last poem",
             "It is the second poem",
             "It falls outside this chapter"],
         "correct": 2,
         "expl": "Poem 2 of 10 in Chapter Six."},
        {"q": "What is the setting shared by this verse and the one before it?",
         "opts": [
             "A riverbank",
             "A rain-sheltered hut",
             "A royal court",
             "A marketplace"],
         "correct": 1,
         "expl": "The same domestic, rain-proof scene."},
        {"q": "What does 'pavassa' mean, closing this verse?",
         "opts": [
             "Rain forth",
             "Stop",
             "Depart",
             "Listen"],
         "correct": 0,
         "expl": "An unafraid, welcoming address to the sky, repeated from Thag 1.51."},
    ],
    marginalia=[
        ("Same frame, one word", [
            "hut and rain unchanged,",
            "the body named instead"
        ]),
        ("Mind, grounded in body", [
            "not just serene —",
            "immersed, specifically"
        ]),
        ("A formula, taking shape", [
            "two lines held fixed,",
            "one line free to speak"
        ]),
        ("Second of four", [
            "the pattern confirmed,",
            "two poems still to come"
        ]),
    ],
    further=[
        '<a href="%s/thag1.52/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.51.html">Thag 1.51 &mdash; Godhika</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.53 — Valliya (1st)
# --------------------------------------------------------------------------- #
page(
    1, 53, "Valliya", "Valliya (1st)",
    meta_title="Thag 1.53 — Valliya (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Valliya's verse, the third in Chapter Six's rain-and-hut "
        "formula, naming diligence as his one variation. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 3 of 10",
    glance=[
        ("Setting", "A rain-sheltered hut"),
        ("Speaker", "Valliya (distinguished from a second monk of the "
                    "same name elsewhere in this collection), "
                    "addressing the rain god directly"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the same formula, one word changed again"),
    ],
    why=(
        "The formula continues into its third poem: the same rain, "
        "the same hut, and this time a third line naming diligence "
        "&mdash; appam&amacr;da &mdash; as what Valliya does inside "
        "that shelter. His name carries the ordinal &lsquo;(1st)&rsquo;, "
        "marking him as distinct from another monk sharing his name "
        "elsewhere in the Theragātha."),
    guide=[
        ("Diligence, named directly", [
            "Where Godhika named a serene mind and Subāhu named "
            "mindfulness immersed in the body, Valliya's third line "
            "states simply that he dwells there &lsquo;diligent&rsquo; "
            "&mdash; appamatto, the same quality praised throughout "
            "the Theragātha and named explicitly as the Buddha's own "
            "final exhortation elsewhere in the canon."]),
        ("A name that expects a namesake", [
            "The ordinal &lsquo;(1st)&rsquo; attached to Valliya's "
            "name signals that another elder shares it later in the "
            "collection, following the same disambiguation pattern "
            "already seen with Tissa, Vaccha, and Sumaṅgala earlier in "
            "this book."]),
        ("Three poems in, the formula's real subject", [
            "By this third repetition, the shared frame &mdash; rain, "
            "hut, invitation to the sky &mdash; has become almost "
            "invisible scaffolding. What each poem is actually about "
            "is the single word each speaker chooses for that one "
            "open line: serenity, embodiment, now diligence."]),
    ],
    terms=[
        ("appamatta",
         "&ldquo;diligent&rdquo; or &ldquo;heedful&rdquo; &mdash; the "
         "quality Valliya names as his own variation on the shared "
         "formula."),
        ("appam&amacr;da",
         "&ldquo;diligence&rdquo; or &ldquo;heedfulness&rdquo; "
         "&mdash; the broader quality this verse's third line "
         "invokes, praised throughout the Theragātha."),
        ("ku&#7789;ik&amacr;",
         "&ldquo;little hut&rdquo; &mdash; the shared setting "
         "continuing from the two poems before this one."),
        ("tassa&#7745;",
         "&ldquo;there&rdquo; &mdash; the word opening Valliya's third "
         "line, referring back to the hut just described."),
        ("pavassa",
         "&ldquo;rain forth&rdquo; &mdash; the closing invitation, "
         "identical across all four poems in this run."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.53:1.1-1.4"),
    ],
    quiz=[
        {"q": "What quality does Valliya name in his verse's third line?",
         "opts": [
             "Anger",
             "Confusion",
             "Fear",
             "Diligence"],
         "correct": 3,
         "expl": "Appamatto, 'diligent' — his own variation on the shared formula."},
        {"q": "What does the ordinal '(1st)' attached to Valliya's name signal?",
         "opts": [
             "That he was the first monk ever ordained",
             "That another elder shares his name later in the collection",
             "That this is his first verse of many",
             "Nothing in particular"],
         "correct": 1,
         "expl": "The same disambiguation pattern seen with Tissa, Vaccha, and others earlier in this book."},
        {"q": "How do this verse's first two lines compare to the two poems before it?",
         "opts": [
             "Completely different",
             "Only the rain image is shared",
             "The same shared formula continues",
             "Only the hut image is shared"],
         "correct": 2,
         "expl": "Rain, hut — the same opening, three poems running."},
        {"q": "What did Godhika and Subāhu name in their own third lines, for comparison?",
         "opts": [
             "A serene mind, then mindfulness immersed in the body",
             "Both named diligence",
             "Neither varied the third line",
             "Both named a distant journey"],
         "correct": 0,
         "expl": "Each poem names a different single quality inside the shared frame."},
        {"q": "According to this reading guide, what has the shared frame become by this third repetition?",
         "opts": [
             "The main point of the poem",
             "Almost invisible scaffolding around each speaker's one distinct word",
             "Increasingly confusing",
             "Entirely abandoned"],
         "correct": 1,
         "expl": "The real content is the single varying word, not the repeated frame."},
        {"q": "What does 'appamāda' mean?",
         "opts": [
             "Wealth",
             "Silence",
             "Speed",
             "Diligence or heedfulness"],
         "correct": 3,
         "expl": "A quality praised throughout the Theragātha."},
        {"q": "What does the verse invite the rain god to do?",
         "opts": [
             "Stop raining",
             "Rain forth, as it wishes",
             "Move elsewhere",
             "Nothing is addressed to it"],
         "correct": 1,
         "expl": "The same closing invitation shared across this run of poems."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "First",
             "Second",
             "Third",
             "Last"],
         "correct": 2,
         "expl": "Poem 3 of 10, continuing the rain-and-hut formula."},
        {"q": "What is the setting of this verse?",
         "opts": [
             "A rain-sheltered hut",
             "A riverbank",
             "A marketplace",
             "A mountain peak"],
         "correct": 0,
         "expl": "The same domestic scene shared with the poems before it."},
        {"q": "What does 'tassaṁ' mean, opening Valliya's third line?",
         "opts": [
             "There",
             "Never",
             "Always",
             "Elsewhere"],
         "correct": 0,
         "expl": "Referring back to the hut just described."},
    ],
    marginalia=[
        ("A third word, offered", [
            "not calm, not body —",
            "diligence, this time"
        ]),
        ("A name expecting company", [
            "'(1st)' marks him,",
            "a namesake still to come"
        ]),
        ("Scaffolding, made visible", [
            "same rain, same hut,",
            "one word carries it"
        ]),
        ("Three of four", [
            "the pattern nearly complete,",
            "one poem left"
        ]),
    ],
    further=[
        '<a href="%s/thag1.53/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.52.html">Thag 1.52 &mdash; Sub&amacr;hu</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.54 — Uttiya (2nd)
# --------------------------------------------------------------------------- #
page(
    1, 54, "Uttiya", "Uttiya (2nd)",
    meta_title="Thag 1.54 — Uttiya (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Uttiya's verse, the fourth and final poem in Chapter Six's "
        "rain-and-hut formula, naming solitude as his one variation. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 4 of 10",
    glance=[
        ("Setting", "A rain-sheltered hut"),
        ("Speaker", "Uttiya (marked '(2nd)', distinct from another "
                    "monk of the same name), addressing the rain god "
                    "directly"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the formula's fourth and final word"),
    ],
    why=(
        "Uttiya's verse closes the run of four rain-and-hut poems that "
        "opened this chapter. His variation is solitude: he dwells in "
        "his hut &lsquo;without a partner&rsquo;, adutiyo &mdash; a "
        "literal &lsquo;without a second&rsquo;, closing a sequence "
        "that has now named a serene mind, embodied mindfulness, "
        "diligence, and finally aloneness itself."),
    guide=[
        ("The fourth word: aloneness", [
            "Adutiyo, &lsquo;without a second&rsquo; or "
            "&lsquo;without a partner&rsquo;, is Uttiya's variation on "
            "the shared third line &mdash; a direct statement that he "
            "dwells in his hut alone, closing this run on the theme of "
            "solitary practice itself."]),
        ("Four poems, four words, one formula", [
            "Read together, the run now reads as a small set: Godhika "
            "named serenity, Subāhu named the body, Valliya named "
            "diligence, and Uttiya names solitude &mdash; four "
            "different single words filling the same fixed frame, "
            "each pointing at a distinct facet of the same "
            "contentment."]),
        ("A second Uttiya, elsewhere", [
            "The ordinal &lsquo;(2nd)&rsquo; marks this Uttiya as "
            "distinct from another elder sharing his name, following "
            "the same pattern already seen with Valliya just before "
            "him and with Tissa, Vaccha, and Sumaṅgala earlier in this "
            "book."]),
        ("What comes after the formula breaks", [
            "The next poem, Añjanavaniya's verse, keeps this chapter's "
            "hut theme but drops the shared rain-and-invitation frame "
            "entirely &mdash; the formula that has carried the "
            "chapter's first four poems ends here."]),
    ],
    terms=[
        ("adutiya",
         "&ldquo;without a second&rdquo; or &ldquo;without a "
         "partner&rdquo; &mdash; Uttiya's variation, naming solitude "
         "directly."),
        ("ku&#7789;ik&amacr;",
         "&ldquo;little hut&rdquo; &mdash; the shared setting closing "
         "out this four-poem run."),
        ("tassa&#7745;",
         "&ldquo;there&rdquo; &mdash; the word opening Uttiya's third "
         "line, as in Valliya's verse just before it."),
        ("pavassa",
         "&ldquo;rain forth&rdquo; &mdash; the closing invitation, "
         "shared across all four poems in this formula."),
        ("Theragāthā",
         "&ldquo;Verses of the Senior Monks&rdquo; &mdash; this "
         "collection's own title; this run of four poems is one of "
         "its clearest examples of a shared formula varied by "
         "individual speakers."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.54:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Uttiya's third line name as his own variation on the shared formula?",
         "opts": [
             "Wealth",
             "Anger",
             "Travel",
             "Solitude, dwelling there 'without a partner'"],
         "correct": 3,
         "expl": "Adutiyo, 'without a second' — a direct statement of aloneness."},
        {"q": "What four words, in order, do the four poems in this run each contribute, according to this reading guide?",
         "opts": [
             "Serenity, the body, diligence, solitude",
             "Wealth, fame, power, victory",
             "Fear, doubt, anger, grief",
             "The four poems contribute nothing distinct"],
         "correct": 0,
         "expl": "Godhika, Subāhu, Valliya, and Uttiya, in sequence."},
        {"q": "What does the ordinal '(2nd)' attached to this Uttiya's name signal?",
         "opts": [
             "That he is the Buddha's second disciple",
             "That another elder shares his name elsewhere in the collection",
             "That this is his second verse",
             "Nothing in particular"],
         "correct": 1,
         "expl": "The same disambiguation pattern seen with Valliya and others in this book."},
        {"q": "According to this reading guide, what happens with the next poem, Añjanavaniya's verse?",
         "opts": [
             "It repeats this exact formula a fifth time",
             "It has nothing to do with huts at all",
             "It returns to Chapter One",
             "It keeps the hut theme but drops the shared rain-and-invitation frame"],
         "correct": 3,
         "expl": "The four-poem formula ends with this verse."},
        {"q": "What does 'adutiya' mean?",
         "opts": [
             "Without a second, or without a partner",
             "With many companions",
             "Married",
             "Newly ordained"],
         "correct": 0,
         "expl": "A literal statement of solitary dwelling."},
        {"q": "How do this verse's first two lines compare to the three poems before it?",
         "opts": [
             "Entirely different",
             "The same shared formula continues",
             "Only the hut is mentioned",
             "Only the rain is mentioned"],
         "correct": 1,
         "expl": "Rain, hut — unchanged across all four poems."},
        {"q": "What does the verse invite the rain god to do?",
         "opts": [
             "Stop raining",
             "Rain forth, as it wishes",
             "Move elsewhere",
             "Nothing is addressed to it"],
         "correct": 1,
         "expl": "The same closing invitation shared across this whole run."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "First",
             "Second",
             "Fourth",
             "Last"],
         "correct": 2,
         "expl": "Poem 4 of 10, closing the rain-and-hut formula."},
        {"q": "What is the setting of this verse?",
         "opts": [
             "A rain-sheltered hut",
             "A riverbank",
             "A royal court",
             "A mountain peak"],
         "correct": 0,
         "expl": "The same domestic scene shared with the three poems before it."},
        {"q": "Besides Uttiya himself, which other elder in this run is marked with a disambiguating ordinal?",
         "opts": [
             "Godhika",
             "Subāhu",
             "Valliya",
             "None of them"],
         "correct": 2,
         "expl": "Valliya (1st), the poem immediately before this one."},
    ],
    marginalia=[
        ("The fourth word, alone", [
            "not calm, body, diligence —",
            "solitude, this time"
        ]),
        ("Four words, one frame", [
            "serenity, body,",
            "diligence, solitude"
        ]),
        ("A second Uttiya, elsewhere", [
            "'(2nd)' marks him,",
            "a namesake unseen"
        ]),
        ("The formula ends here", [
            "four poems complete,",
            "the next one breaks the mold"
        ]),
    ],
    further=[
        '<a href="%s/thag1.54/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.53.html">Thag 1.53 &mdash; Valliya '
        "(1st)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.55 — A&ntilde;janavaniya
# --------------------------------------------------------------------------- #
page(
    1, 55, "A&ntilde;janavaniya", "A&ntilde;janavaniya",
    meta_title="Thag 1.55 — Añjanavaniya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Añjanavaniya's verse, named for the Añjana Wood where he "
        "built his hut, closing with the same three-knowledges formula "
        "as Sugandha's verse in Chapter Three. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 5 of 10",
    glance=[
        ("Setting", "The Añjana Wood, where he built his hut"),
        ("Speaker", "Añjanavaniya, named for the wood itself"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the chapter's hut theme, without the shared "
                       "formula"),
    ],
    why=(
        "Añjanavaniya's name simply means &lsquo;of the Añjana "
        "Wood&rsquo; &mdash; a place-based name, like Sītavaniya and "
        "Kosalavihārin elsewhere in this book, given after the "
        "location of his own hut. His verse keeps this chapter's hut "
        "theme but drops the rain-and-invitation frame that carried "
        "the four poems before it, closing instead with the same "
        "three-knowledges formula heard from Sugandha in Chapter "
        "Three."),
    guide=[
        ("A name taken from the place itself", [
            "Añjanavaniya built his hut having &lsquo;plunged into the "
            "Añjana wood&rsquo;, and his name simply records that "
            "location &mdash; the same place-name pattern already "
            "seen with Sītavaniya in Chapter Two and continuing later "
            "in this chapter with Kosalavihārin."]),
        ("The formula breaks, but the hut remains", [
            "Unlike the four poems before this one, Añjanavaniya's "
            "verse does not invite the rain god or describe his hut "
            "as roofed against the wind. The rain-and-hut formula that "
            "opened this chapter ends with Uttiya's verse; this poem "
            "keeps only the hut itself, now as the site of "
            "attainment rather than shelter from weather."]),
        ("The same closing couplet as Sugandha, three chapters back", [
            "Añjanavaniya's final two lines &mdash; &lsquo;I've "
            "attained the three knowledges and fulfilled the Buddha's "
            "instructions&rsquo; &mdash; repeat Sugandha's closing "
            "couplet from Chapter Three (Thag 1.24) word for word, a "
            "formula this collection uses for a monk's own plain "
            "declaration of completed practice."]),
    ],
    terms=[
        ("A&ntilde;jana&#7745; vana&#7745;",
         "&ldquo;the Añjana Wood&rdquo; &mdash; the specific forest "
         "Añjanavaniya's name records, and where he built his hut."),
        ("&amacr;sandi",
         "here rendered &ldquo;plunged&rdquo; &mdash; describing how "
         "Añjanavaniya entered the wood before building his hut."),
        ("tisso vijj&amacr;",
         "&ldquo;the three knowledges&rdquo; &mdash; recollection of "
         "past lives, the divine eye, and the ending of defilements, "
         "named as Añjanavaniya's attainment."),
        ("ku&#7789;ika&#7745; katv&amacr;",
         "&ldquo;having made a hut&rdquo; &mdash; this verse's only "
         "remaining trace of the chapter's shared hut theme."),
        ("kata&#7745; buddhassa s&amacr;sana&#7745;",
         "&ldquo;fulfilled the Buddha's instructions&rdquo; &mdash; "
         "the closing declaration shared word for word with Sugandha's "
         "verse in Chapter Three."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.55:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name Añjanavaniya mean?",
         "opts": [
             "A title meaning 'the wise one'",
             "A family clan name",
             "It has no particular meaning",
             "A place-based name recording the Añjana Wood, where he built his hut"],
         "correct": 3,
         "expl": "The same place-naming pattern seen elsewhere in this book."},
        {"q": "How does this verse compare structurally to the four poems just before it?",
         "opts": [
             "It repeats the same rain-and-invitation formula exactly",
             "It keeps the chapter's hut theme but drops the rain-god invitation",
             "It has no connection to huts at all",
             "It is identical in every line"],
         "correct": 1,
         "expl": "The formula that opened the chapter ends with Uttiya's verse."},
        {"q": "What does Añjanavaniya's closing couplet share with Sugandha's verse in Chapter Three (Thag 1.24)?",
         "opts": [
             "Nothing — they are unrelated",
             "The exact same closing couplet, word for word",
             "Only the setting",
             "Only the speaker's name"],
         "correct": 1,
         "expl": "'I've attained the three knowledges and fulfilled the Buddha's instructions.'"},
        {"q": "What are the 'three knowledges' this verse names?",
         "opts": [
             "Reading, writing, and arithmetic",
             "Three monastic rules",
             "Recollection of past lives, the divine eye, and the ending of defilements",
             "Three types of meditation posture"],
         "correct": 2,
         "expl": "A standard traditional set of attainments."},
        {"q": "What place-named elder from earlier in this book does Añjanavaniya's name resemble in pattern?",
         "opts": [
             "Subhūti, from Chapter One",
             "Godhika, opening this chapter",
             "No such pattern exists elsewhere",
             "Sītavaniya, from Chapter Two"],
         "correct": 3,
         "expl": "Both named after the place where they built their huts."},
        {"q": "What does Añjanavaniya do before attaining the three knowledges, according to the verse?",
         "opts": [
             "He builds a hut in the Añjana Wood",
             "He travels to a distant kingdom",
             "He debates another teacher",
             "He fasts for a year"],
         "correct": 0,
         "expl": "The verse's opening action, before the closing declaration."},
        {"q": "Which poem in this chapter does the rain-and-hut formula end with, according to this reading guide?",
         "opts": [
             "This poem, Thag 1.55",
             "The poem before this one, Uttiya's verse (Thag 1.54)",
             "The chapter's very first poem",
             "The formula never ends"],
         "correct": 1,
         "expl": "Añjanavaniya's verse is the first in this chapter to drop it."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "First",
             "Third",
             "Fifth",
             "Last"],
         "correct": 2,
         "expl": "Poem 5 of 10, opening the chapter's second half."},
        {"q": "What single word from this chapter's theme survives in Añjanavaniya's verse?",
         "opts": [
             "Hut",
             "Rain",
             "Wind",
             "Sky"],
         "correct": 0,
         "expl": "The hut remains, now as a site of attainment rather than shelter from weather."},
        {"q": "What does 'tisso vijjā' mean?",
         "opts": [
             "The three knowledges",
             "The three refuges",
             "The three trainings",
             "The three jewels"],
         "correct": 0,
         "expl": "Named directly as Añjanavaniya's own attainment."},
    ],
    marginalia=[
        ("Named for the wood itself", [
            "Añjana forest,",
            "the name he carries"
        ]),
        ("A formula, dropped", [
            "no rain invited here,",
            "only the hut remains"
        ]),
        ("The same couplet, again", [
            "the three knowledges,",
            "the same words as Sugandha"
        ]),
        ("A place-name pattern", [
            "Sītavaniya, then this —",
            "named where they dwelled"
        ]),
    ],
    further=[
        '<a href="%s/thag1.55/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.24.html">Thag 1.24 &mdash; Sugandha</a> '
        "&mdash; sharing this verse's closing couplet word for word, "
        "from Chapter Three.",
        '<a href="thag-1.54.html">Thag 1.54 &mdash; Uttiya '
        "(2nd)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.56 — Ku&#7789;ivih&amacr;rin (1st)
# --------------------------------------------------------------------------- #
page(
    1, 56, "Ku&#7789;ivih&amacr;rin", "Ku&#7789;ivih&amacr;rin (1st)",
    meta_title="Thag 1.56 — Kuṭivihārin (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kuṭivihārin's verse, a small dialogue asking who is in the "
        "hut and answering that his hut was not built in vain. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 6 of 10",
    glance=[
        ("Setting", "A hut, addressed from outside"),
        ("Speaker", "An exchange framed as a question and an answer; "
                    "the text does not specify how many voices are "
                    "involved"),
        ("Form", "One four-line verse, structured as dialogue"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734;&#9734; "
                       "&mdash; brief, but its voicing is genuinely "
                       "ambiguous"),
    ],
    why=(
        "Kuṭivihārin's name means, plainly, &lsquo;hut-dweller&rsquo; "
        "&mdash; a name drawn directly from his verse's own subject, "
        "not from clan or birthplace. The verse itself is built as a "
        "small exchange: &lsquo;Who is in this hut?&rsquo; is asked "
        "and answered, and someone then tells the monk inside that his "
        "hut &lsquo;wasn't built in vain&rsquo;."),
    guide=[
        ("A name taken from the poem's own subject", [
            "Unlike the clan names (Vaccha), place names (Sītavaniya, "
            "Añjanavaniya), and kinship names (Siṅgālapitā) already "
            "seen in this book, Kuṭivihārin's name is simply an "
            "epithet describing what the verse itself is about: a "
            "monk who dwells in a hut."]),
        ("A question, an answer, and a voice that isn't identified", [
            "The verse opens with &lsquo;Who is in this hut?&rsquo; "
            "answered by &lsquo;A monk is in this hut, free of lust, "
            "his mind serene&rsquo;, then closes with a direct address "
            "&mdash; &lsquo;you should know this, friend: your hut "
            "wasn't built in vain&rsquo;. The text does not say "
            "whether the asker and the one who delivers this closing "
            "praise are the same speaker, or whether the monk is "
            "describing himself in the third person before being "
            "addressed by someone else. This reading guide does not "
            "resolve that ambiguity, only notes that it is genuinely "
            "there."]),
        ("A precedent for quoted speech in this book", [
            "This is not the first verse in the collection built "
            "around directly quoted words: the novice Sīvaka's poem in "
            "Chapter Two opens by quoting his preceptor's own speech. "
            "Kuṭivihārin's verse pushes the device further, quoting an "
            "entire exchange rather than a single line."]),
        ("A pair, about to diverge", [
            "The next poem, spoken by a second monk also called "
            "Kuṭivihārin, shares this poem's hut theme and its "
            "address to &lsquo;monk&rsquo; &mdash; but carries the "
            "opposite message, warning against wanting a new hut "
            "rather than praising the one already built."]),
    ],
    terms=[
        ("ku&#7789;ivih&amacr;rin",
         "&ldquo;hut-dweller&rdquo; &mdash; the epithet this monk is "
         "named for, drawn from the verse's own subject rather than "
         "clan, place, or kin."),
        ("v&imacr;tar&amacr;ga",
         "&ldquo;free of lust&rdquo; &mdash; part of the answer "
         "describing the monk inside the hut."),
        ("susam&amacr;hitacitto",
         "&ldquo;his mind serene&rdquo; &mdash; completing that "
         "description, echoing this chapter's recurring vocabulary of "
         "calm."),
        ("&amacr;vuso",
         "&ldquo;friend&rdquo; or &ldquo;reverend&rdquo; &mdash; the "
         "direct address opening this verse's final two lines."),
        ("amogh&amacr;",
         "&ldquo;not in vain&rdquo; &mdash; the verse's closing "
         "judgment on the hut itself."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.56:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name Kuṭivihārin mean?",
         "opts": [
             "A clan name",
             "A place name",
             "A kinship title",
             "'Hut-dweller' — an epithet drawn from the verse's own subject"],
         "correct": 3,
         "expl": "Different from the clan, place, and kinship names seen so far in this book."},
        {"q": "How does the verse open?",
         "opts": [
             "With a question, 'Who is in this hut?'",
             "With a narrative setting",
             "With a teaching on ethics",
             "With praise of the Buddha"],
         "correct": 0,
         "expl": "A small dialogue frames the whole verse."},
        {"q": "How does the answer describe the monk in the hut?",
         "opts": [
             "Wealthy and respected",
             "Free of lust, his mind serene",
             "Fearful and doubting",
             "Newly ordained"],
         "correct": 1,
         "expl": "A brief description completing the opening question."},
        {"q": "According to this reading guide, does the text specify who delivers the closing line, 'your hut wasn't built in vain'?",
         "opts": [
             "Yes, it is clearly the monk's teacher",
             "No — the text leaves this ambiguous",
             "Yes, it is clearly the monk himself",
             "Yes, it is clearly a deity"],
         "correct": 1,
         "expl": "A genuine ambiguity this reading guide does not resolve."},
        {"q": "What earlier poem in this book also builds its verse around directly quoted speech?",
         "opts": [
             "Subhūti's opening poem",
             "Godhika's verse, opening this chapter",
             "The novice Sīvaka's poem in Chapter Two",
             "No earlier poem does this"],
         "correct": 2,
         "expl": "Sīvaka quotes his preceptor; this verse quotes a whole exchange."},
        {"q": "What does 'āvuso' mean?",
         "opts": [
             "Enemy",
             "Teacher",
             "Stranger",
             "Friend or reverend"],
         "correct": 3,
         "expl": "The direct address opening this verse's final two lines."},
        {"q": "What does the verse conclude about the hut?",
         "opts": [
             "That it was built in vain",
             "That it was not built in vain",
             "That it should be abandoned",
             "Nothing is concluded about the hut itself"],
         "correct": 1,
         "expl": "Amoghā, 'not in vain' — the verse's closing judgment."},
        {"q": "How does the next poem in this chapter relate to this one, according to this reading guide?",
         "opts": [
             "It is spoken by a second monk also called Kuṭivihārin, but carries the opposite message about wanting a new hut",
             "It repeats this poem exactly",
             "It has no connection to this poem",
             "It abandons the hut theme entirely"],
         "correct": 0,
         "expl": "A matched pair with contrasting messages."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "First",
             "Fifth",
             "Sixth",
             "Last"],
         "correct": 2,
         "expl": "Poem 6 of 10."},
        {"q": "What does 'vītarāga' mean?",
         "opts": [
             "Free of lust",
             "Wealthy",
             "Newly arrived",
             "Angry"],
         "correct": 0,
         "expl": "Part of the description answering 'who is in this hut?'"},
    ],
    marginalia=[
        ("A question, from outside", [
            "'who is in this hut?' —",
            "an answer, then a verdict"
        ]),
        ("A name from the poem itself", [
            "not clan, not place —",
            "simply, hut-dweller"
        ]),
        ("Voices left unassigned", [
            "asker and praiser —",
            "the text does not say"
        ]),
        ("A pair about to split", [
            "one hut praised,",
            "the next one warned against"
        ]),
    ],
    further=[
        '<a href="%s/thag1.56/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.14.html">Thag 1.14 &mdash; The Novice '
        "S&imacr;vaka</a> &mdash; this book's earlier verse built "
        "around directly quoted speech.",
        '<a href="thag-1.55.html">Thag 1.55 &mdash; A&ntilde;'
        "janavaniya</a> &mdash; the poem immediately before this one, "
        "in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.57 — Ku&#7789;ivih&amacr;rin (2nd)
# --------------------------------------------------------------------------- #
page(
    1, 57, "Ku&#7789;ivih&amacr;rin", "Ku&#7789;ivih&amacr;rin (2nd)",
    meta_title="Thag 1.57 — Kuṭivihārin (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for a "
        "second Kuṭivihārin's verse, a warning against craving a new "
        "hut that reverses the praise of the poem just before it. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A hut, old and already lived in"),
        ("Speaker", "An unnamed voice addressing the monk called "
                    "Kuṭivihārin directly, in the second person "
                    "throughout"),
        ("Form", "One four-line verse, entirely direct address"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "direct rebuke, reversing the poem just before "
                       "it"),
    ],
    why=(
        "A second monk sharing the name Kuṭivihārin gives his name to "
        "this verse, yet every line addresses him in the second "
        "person: &lsquo;this was your old hut, but you still want a "
        "new hut&rsquo;. Where the first Kuṭivihārin's poem praised a "
        "hut as not built in vain, this one warns against the very "
        "wish for a new one."),
    guide=[
        ("An entire verse of quoted rebuke", [
            "Unlike the first Kuṭivihārin's poem, where only part of "
            "the verse was framed as an exchange, this entire four-"
            "line poem is a direct address to &lsquo;monk&rsquo; "
            "&mdash; the whole verse reads as words spoken to "
            "Kuṭivihārin, which he then preserves as his own "
            "Theragātha entry, continuing this chapter's device of "
            "quoted speech seen already with the novice Sīvaka and the "
            "first Kuṭivihārin."]),
        ("A matched pair with opposite messages", [
            "Both poems share a monk named Kuṭivihārin and the word "
            "&lsquo;monk&rsquo; addressed directly, and both close on "
            "a judgment about a hut. But the first poem's judgment is "
            "approval &mdash; &lsquo;not built in vain&rsquo; &mdash; "
            "while this one is a warning: wanting a new hut, the verse "
            "says plainly, &lsquo;will only bring more suffering&rsquo;."]),
        ("Contentment against craving, within the same theme", [
            "Read together, the two Kuṭivihārin poems frame this "
            "chapter's hut theme from both sides: contentment with "
            "what one already has, and the suffering that follows "
            "from wanting more of the same kind of thing, even "
            "something as modest as a second hut."]),
    ],
    terms=[
        ("pur&amacr;&#7751;iy&amacr;",
         "&ldquo;old&rdquo; &mdash; describing the hut Kuṭivihārin "
         "already has, in contrast to the new one he wants."),
        ("patthayase",
         "&ldquo;you long for&rdquo; or &ldquo;you want&rdquo; "
         "&mdash; naming the craving this verse warns against."),
        ("&amacr;sa&#7745;...vir&amacr;jaya",
         "&ldquo;let go of hope&rdquo; &mdash; the verse's direct "
         "instruction to Kuṭivihārin."),
        ("dukkh&amacr;",
         "&ldquo;suffering&rdquo; &mdash; the consequence this verse "
         "attaches to craving a new hut."),
        ("ku&#7789;ivih&amacr;rin",
         "&ldquo;hut-dweller&rdquo; &mdash; the epithet shared with "
         "the monk of the poem just before this one, here marked "
         "&lsquo;(2nd)&rsquo; to distinguish them."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.57:1.1-1.4"),
    ],
    quiz=[
        {"q": "Who does this verse address, throughout all four lines?",
         "opts": [
             "The monk called Kuṭivihārin, in the second person",
             "The Buddha",
             "A group of villagers",
             "No one in particular"],
         "correct": 0,
         "expl": "An entire verse of direct address."},
        {"q": "What does the verse say Kuṭivihārin wants, despite already having an old hut?",
         "opts": [
             "A new robe",
             "A new hut",
             "A new teacher",
             "A new companion"],
         "correct": 1,
         "expl": "The craving this verse warns against."},
        {"q": "How does this poem compare to the one immediately before it, also about a monk named Kuṭivihārin?",
         "opts": [
             "It repeats the same praise exactly",
             "It has no connection to the poem before it",
             "It reverses the message, warning against wanting a new hut instead of praising the one already built",
             "It drops the hut theme entirely"],
         "correct": 2,
         "expl": "A matched pair with opposite judgments."},
        {"q": "What consequence does the verse attach to wanting a new hut?",
         "opts": [
             "Wealth",
             "Fame",
             "Nothing — no consequence is named",
             "More suffering"],
         "correct": 3,
         "expl": "Dukkhā, 'suffering' — stated plainly as the closing line."},
        {"q": "According to this reading guide, what device does this verse continue from Sīvaka's poem and the first Kuṭivihārin's poem?",
         "opts": [
             "Directly quoted speech addressed to the monk himself",
             "A place-based name",
             "A five-fold numbered list",
             "An animal simile"],
         "correct": 0,
         "expl": "The whole verse reads as words spoken to Kuṭivihārin."},
        {"q": "What does 'purāṇiyā' mean?",
         "opts": [
             "New",
             "Old",
             "Borrowed",
             "Broken"],
         "correct": 1,
         "expl": "Describing the hut Kuṭivihārin already has."},
        {"q": "What instruction does the verse give Kuṭivihārin directly?",
         "opts": [
             "Build a bigger hut",
             "Travel to another town",
             "Let go of hope for a hut",
             "Teach other monks"],
         "correct": 2,
         "expl": "Āsaṁ kuṭiyā virājaya — a direct command."},
        {"q": "Read together, what do the two Kuṭivihārin poems frame, according to this reading guide?",
         "opts": [
             "Two unrelated topics",
             "A dispute over property rights",
             "Nothing in particular",
             "Contentment with what one has, against the suffering of craving more of the same kind of thing"],
         "correct": 3,
         "expl": "The chapter's hut theme viewed from both sides."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "Seventh",
             "Sixth",
             "Eighth",
             "Last"],
         "correct": 0,
         "expl": "Poem 7 of 10."},
        {"q": "What does 'dukkhā' mean?",
         "opts": [
             "Joyful",
             "Suffering",
             "Peaceful",
             "Wealthy"],
         "correct": 1,
         "expl": "The word closing this verse's warning."},
    ],
    marginalia=[
        ("A hut already had", [
            "old and sufficient,",
            "yet still he wants new"
        ]),
        ("The same name, reversed", [
            "one hut praised,",
            "one craving warned against"
        ]),
        ("A command, not a question", [
            "'let go of hope' —",
            "spoken straight to him"
        ]),
        ("Contentment's other side", [
            "not what is lacking,",
            "but wanting more of enough"
        ]),
    ],
    further=[
        '<a href="%s/thag1.57/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.56.html">Thag 1.56 &mdash; Ku&#7789;ivih&amacr;'
        "rin (1st)</a> &mdash; the poem immediately before this one, "
        "in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.58 — Rama&#7751;&imacr;yaku&#7789;ika
# --------------------------------------------------------------------------- #
page(
    1, 58, "Rama&#7751;&imacr;yaku&#7789;ika", "Rama&#7751;&imacr;yaku&#7789;ika",
    meta_title="Thag 1.58 — Ramaṇīyakuṭika | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ramaṇīyakuṭika's verse, naming a hut he calls delightful and "
        "declining a visit from women. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 8 of 10",
    glance=[
        ("Setting", "A hut received as a gift given in faith"),
        ("Speaker", "Ramaṇīyakuṭika, describing his hut and declining "
                    "a visit"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain in its content, addressing a specific "
                       "situation"),
    ],
    why=(
        "Ramaṇīyakuṭika's name means &lsquo;pleasant little "
        "hut&rsquo; &mdash; drawn directly from his own verse's "
        "opening line, &lsquo;my hut is pleasing, delightful&rsquo;. "
        "The verse's second half turns to a specific situation: women "
        "have apparently come to see him, and he declines, sending "
        "them &lsquo;to those in need&rsquo;."),
    guide=[
        ("A name that is also the verse's first line", [
            "Where Kuṭivihārin's name was a general epithet "
            "(&lsquo;hut-dweller&rsquo;), Ramaṇīyakuṭika's name "
            "reproduces almost exactly the opening words of his own "
            "verse &mdash; &lsquo;Ramaṇīyā me kuṭikā&rsquo;, "
            "&lsquo;my hut is pleasing&rsquo; &mdash; the most literal "
            "case in this chapter of a monk's name drawn from his own "
            "poem's content."]),
        ("A gift given in faith", [
            "The verse specifies that this pleasant hut was "
            "&lsquo;saddhādeyyā&rsquo;, given as an offering by a lay "
            "supporter's faith, tying the hut's pleasantness directly "
            "to the generosity that produced it, rather than to any "
            "effort of his own."]),
        ("A boundary stated plainly, without elaboration", [
            "The verse's second half states, without narrative detail "
            "or explanation, that he has no need of the women who have "
            "come and sends them elsewhere. This reading guide reports "
            "what the verse says on its own terms &mdash; a monk "
            "declining a visit &mdash; without speculating about who "
            "these women were or why they came, since the text gives "
            "no further information."]),
    ],
    terms=[
        ("rama&#7751;&imacr;y&amacr;",
         "&ldquo;pleasing&rdquo; or &ldquo;delightful&rdquo; &mdash; "
         "the word opening this verse and forming half of "
         "Ramaṇīyakuṭika's own name."),
        ("saddh&amacr;deyy&amacr;",
         "&ldquo;a gift given in faith&rdquo; &mdash; describing how "
         "this hut came to be his."),
        ("kum&amacr;r&imacr;",
         "&ldquo;girls&rdquo; or &ldquo;young women&rdquo; &mdash; "
         "those the verse says he has no need of."),
        ("n&amacr;riyo",
         "&ldquo;women&rdquo; or &ldquo;ladies&rdquo; &mdash; the "
         "word used in the verse's closing line, sending them "
         "elsewhere."),
        ("ku&#7789;ika",
         "&ldquo;little hut&rdquo; &mdash; the same recurring word "
         "anchoring this whole chapter, here embedded in the "
         "speaker's own name."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.58:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name Ramaṇīyakuṭika mean?",
         "opts": [
             "'Pleasant little hut', drawn from his own verse's opening line",
             "'Free from doubt'",
             "A clan name",
             "A place name"],
         "correct": 0,
         "expl": "The most literal case in this chapter of a name drawn from its own poem's content."},
        {"q": "How did Ramaṇīyakuṭika's hut come to be his, according to the verse?",
         "opts": [
             "He built it himself from scratch",
             "He inherited it from his family",
             "The text does not say",
             "It was a gift given in faith by a lay supporter"],
         "correct": 3,
         "expl": "Saddhādeyyā — tying the hut's pleasantness to the generosity behind it."},
        {"q": "What does the verse's second half address?",
         "opts": [
             "A dispute with another monk",
             "A teaching on the four noble truths",
             "Women who have apparently come to see him, whom he declines",
             "A journey to another region"],
         "correct": 2,
         "expl": "A boundary stated plainly, without further narrative detail."},
        {"q": "According to this reading guide, does the verse explain who the women are or why they came?",
         "opts": [
             "Yes, in full narrative detail",
             "No — the text gives no further information, and this reading guide does not speculate",
             "Yes, but only in the attribution line",
             "Yes, through a Sujato comment"],
         "correct": 1,
         "expl": "Reporting what the verse states, without adding unstated detail."},
        {"q": "What does 'saddhādeyyā' mean?",
         "opts": [
             "A gift given in faith",
             "A stolen object",
             "A borrowed item",
             "A purchased item"],
         "correct": 0,
         "expl": "Describing how Ramaṇīyakuṭika's hut came to be his."},
        {"q": "What word opens this verse, also forming half of the speaker's own name?",
         "opts": [
             "Dukkhā, 'suffering'",
             "Vassati, 'rains'",
             "Adutiya, 'without a partner'",
             "Ramaṇīyā, 'pleasing' or 'delightful'"],
         "correct": 3,
         "expl": "The literal source of Ramaṇīyakuṭika's name."},
        {"q": "How does Ramaṇīyakuṭika's naming compare to Kuṭivihārin's, from the two poems before this one?",
         "opts": [
             "Both are clan names",
             "Kuṭivihārin's is a general epithet; Ramaṇīyakuṭika's reproduces his own verse's opening words almost exactly",
             "Neither name has any connection to the poem's content",
             "They are identical names"],
         "correct": 1,
         "expl": "A more literal case of self-naming from the poem's own content."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "Seventh",
             "Ninth",
             "Eighth",
             "Last"],
         "correct": 2,
         "expl": "Poem 8 of 10."},
        {"q": "What does 'nāriyo' mean?",
         "opts": [
             "Women",
             "Monks",
             "Deities",
             "Animals"],
         "correct": 0,
         "expl": "The word closing the verse, sending the visitors elsewhere."},
        {"q": "What shared word connects this verse to the rest of Chapter Six?",
         "opts": [
             "Rain",
             "Hut",
             "River",
             "Mountain"],
         "correct": 1,
         "expl": "Kuṭika, embedded directly in the speaker's own name."},
    ],
    marginalia=[
        ("A name from the first line", [
            "'my hut is pleasing' —",
            "and so, his own name"
        ]),
        ("A gift, not a labor", [
            "given in faith,",
            "not built by his own hand"
        ]),
        ("A boundary, stated plainly", [
            "no need of visitors,",
            "sent on, unexplained"
        ]),
        ("The chapter's word, embedded", [
            "kuṭika again —",
            "now inside a name"
        ]),
    ],
    further=[
        '<a href="%s/thag1.58/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.57.html">Thag 1.57 &mdash; Ku&#7789;ivih&amacr;'
        "rin (2nd)</a> &mdash; the poem immediately before this one, "
        "in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.59 — Kosalavih&amacr;rin
# --------------------------------------------------------------------------- #
page(
    1, 59, "Kosalavih&amacr;rin", "Kosalavih&amacr;rin",
    meta_title="Thag 1.59 — Kosalavihārin | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kosalavihārin's verse, a plain four-quality self-description "
        "after building a hut in the wilderness out of faith. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A hut he built himself in the wilderness"),
        ("Speaker", "Kosalavihārin, named for the Kosala region"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "plain list of qualities, without simile or "
                       "narrative"),
    ],
    why=(
        "Kosalavihārin's name simply records where he lived &mdash; "
        "the Kosala region &mdash; continuing this chapter's place-"
        "name pattern alongside Añjanavaniya. His verse states his "
        "own practice as a bare list of four qualities: heedful, "
        "ardent, aware, and mindful, with no simile or narrative "
        "framing at all."),
    guide=[
        ("A place name, matching Añjanavaniya's pattern", [
            "Like Añjanavaniya earlier in this chapter and Sītavaniya "
            "in Chapter Two, Kosalavihārin's name records a location "
            "rather than a clan or a family relation &mdash; here the "
            "Kosala region itself, rather than a single wood."]),
        ("Built by his own hand, unlike the poem just before it", [
            "Where Ramaṇīyakuṭika's hut was &lsquo;a gift given in "
            "faith&rsquo;, Kosalavihārin says plainly that he built "
            "his own hut in the wilderness after going forth &mdash; "
            "two adjacent poems drawing a quiet contrast between a "
            "received dwelling and a self-built one."]),
        ("Four qualities, listed without elaboration", [
            "Appamatto, ātāpī, sampajāno, patissato &mdash; heedful, "
            "ardent, aware, mindful &mdash; are stated back to back as "
            "a bare list, the same unadorned, catalog-like style "
            "already seen in this book with Kuṇḍadhāna's numbered "
            "categories in Chapter Two, though here the items are "
            "named outright rather than counted."]),
    ],
    terms=[
        ("saddh&amacr;ya",
         "&ldquo;out of faith&rdquo; &mdash; why Kosalavihārin says he "
         "went forth."),
        ("ara&ntilde;&ntilde;e",
         "&ldquo;in the wilderness&rdquo; &mdash; where he built his "
         "own hut."),
        ("&amacr;t&amacr;p&imacr;",
         "&ldquo;ardent&rdquo; &mdash; the second of the four "
         "qualities this verse names."),
        ("sampajāno",
         "&ldquo;aware&rdquo; or &ldquo;clearly comprehending&rdquo; "
         "&mdash; the third quality named."),
        ("patissato",
         "&ldquo;mindful&rdquo; &mdash; the fourth and final quality "
         "closing this verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.59:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name Kosalavihārin record?",
         "opts": [
             "A clan lineage",
             "A kinship relation",
             "A personal achievement",
             "A location — the Kosala region"],
         "correct": 3,
         "expl": "The same place-name pattern as Añjanavaniya and Sītavaniya."},
        {"q": "How did Kosalavihārin's hut come to be his, unlike the poem just before it?",
         "opts": [
             "It was a gift given in faith",
             "He inherited it",
             "He built it himself in the wilderness",
             "The text does not say"],
         "correct": 2,
         "expl": "A quiet contrast with Ramaṇīyakuṭika's received hut."},
        {"q": "What four qualities does this verse list about Kosalavihārin himself?",
         "opts": [
             "Wealthy, famous, respected, admired",
             "Heedful, ardent, aware, mindful",
             "Fearful, doubting, confused, tired",
             "Young, old, strong, weak"],
         "correct": 1,
         "expl": "Appamatto, ātāpī, sampajāno, patissato — a bare list."},
        {"q": "How does this verse present its list of qualities, according to this reading guide?",
         "opts": [
             "With an extended simile",
             "As a series of questions",
             "As a dialogue between two speakers",
             "As a bare list, without elaboration or narrative framing"],
         "correct": 3,
         "expl": "Named outright, one after another, with no further explanation."},
        {"q": "What earlier poem in this book uses a similar catalog-like, unadorned style?",
         "opts": [
             "Kuṇḍadhāna's numbered categories in Chapter Two",
             "Godhika's rain-and-hut verse",
             "Subhūti's opening frame",
             "No earlier poem resembles this one"],
         "correct": 0,
         "expl": "Though Kuṇḍadhāna's items are counted rather than named outright."},
        {"q": "Why does Kosalavihārin say he went forth?",
         "opts": [
             "To escape debt",
             "By royal command",
             "Out of faith",
             "The text does not say"],
         "correct": 2,
         "expl": "Saddhāya, 'out of faith' — the verse's opening reason."},
        {"q": "What does 'sampajāno' mean?",
         "opts": [
             "Aware or clearly comprehending",
             "Fearful",
             "Wealthy",
             "Sleepy"],
         "correct": 0,
         "expl": "The third of the four qualities this verse names."},
        {"q": "Where does this poem fall in Chapter Six?",
         "opts": [
             "Eighth",
             "Ninth",
             "Tenth",
             "First"],
         "correct": 1,
         "expl": "Poem 9 of 10, one before the chapter's close."},
        {"q": "What does 'araññe' mean?",
         "opts": [
             "In the village",
             "In the wilderness",
             "By the river",
             "In the royal court"],
         "correct": 1,
         "expl": "Where Kosalavihārin built his own hut."},
        {"q": "What word links this verse to the rest of Chapter Six?",
         "opts": [
             "Hut",
             "River",
             "Mountain",
             "Ocean"],
         "correct": 0,
         "expl": "Kuṭikā, continuing the chapter's shared theme."},
    ],
    marginalia=[
        ("A place, not a clan", [
            "Kosala's name,",
            "carried as his own"
        ]),
        ("Built, not given", [
            "his own hands,",
            "unlike the poem before"
        ]),
        ("Four words, no simile", [
            "heedful, ardent,",
            "aware, mindful"
        ]),
        ("Nine of ten", [
            "one poem remains,",
            "the chapter nearly closed"
        ]),
    ],
    further=[
        '<a href="%s/thag1.59/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.58.html">Thag 1.58 &mdash; Rama&#7751;&imacr;'
        "yaku&#7789;ika</a> &mdash; the poem immediately before this "
        "one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.60 — S&imacr;vali
# --------------------------------------------------------------------------- #
page(
    1, 60, "S&imacr;vali", "S&imacr;vali",
    meta_title="Thag 1.60 — Sīvali | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sīvali's verse, closing Chapter Six — the tenth poem in a row "
        "to mention a hut, and the chapter's only poem naming the "
        "conceit-tendency directly. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Six &middot; Poem 10 of 10",
    glance=[
        ("Setting", "The hut Sīvali entered with a specific purpose"),
        ("Speaker", "Sīvali, reporting his own fulfilled wish"),
        ("Form", "One four-line verse, followed in the Pali by an "
                 "untranslated chapter colophon and mnemonic summary "
                 "verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a quiet, grammatically compact close to a "
                       "unified chapter"),
    ],
    why=(
        "Sīvali's verse closes Chapter Six, and closes it as the "
        "tenth poem in a row to mention a hut &mdash; every single "
        "poem in this chapter, from Godhika's rain-soaked opening to "
        "this one, shares that one word. Sīvali reports that his "
        "purpose for entering his hut came true: seeking knowledge and "
        "liberation, he gave up the tendency to conceit."),
    guide=[
        ("Ten poems, one word, no exceptions", [
            "Godhika, Subāhu, Valliya, and Uttiya invited the rain "
            "from inside a hut; Añjanavaniya built one in the Añjana "
            "Wood; both monks called Kuṭivihārin were named for "
            "dwelling in one; Ramaṇīyakuṭika's own name was drawn from "
            "his; Kosalavihārin built his own in the wilderness; and "
            "now Sīvali closes the chapter by naming the hut he "
            "&lsquo;entered&rsquo; for a specific purpose. No other "
            "chapter completed so far in this book shares a single "
            "image across all ten of its poems this consistently."]),
        ("A grammatical note on the closing word", [
            "Sujato's comment on this verse identifies "
            "&lsquo;ujjahaṁ&rsquo;, the verb translated &lsquo;I gave "
            "up&rsquo;, as a reflexive first-person aorist &mdash; a "
            "grammatical detail confirming that Sīvali is describing "
            "an action he did to himself, his own tendency to "
            "conceit, rather than something done to him."]),
        ("The conceit-tendency, named for the first time in this book", [
            "M&amacr;n&amacr;nusaya, &lsquo;the tendency to "
            "conceit&rsquo;, is one of the underlying tendencies "
            "(anusaya) that recur across the wider canon as subtle, "
            "latent defilements rather than active thoughts &mdash; "
            "this is the first time this specific tendency is named "
            "outright in a Theragātha poem covered so far in this "
            "collection."]),
        ("A name shared with a much later reputation", [
            "This Sīvali shares his name with an elder listed "
            "elsewhere in the canon among the Buddha's foremost "
            "disciples for receiving gifts and offerings. Nothing in "
            "this verse itself makes that connection, and this reading "
            "guide does not assert they are the same person &mdash; "
            "only that the name recurs, as Godhika's and others' names "
            "did earlier in this same chapter."]),
        ("A chapter's own close, left untranslated", [
            "As at the end of Chapters One through Five, the Pali "
            "text here carries vaggo chaṭṭho, &lsquo;the sixth "
            "chapter is finished&rsquo;, followed by an uddāna naming "
            "all ten monks of this chapter in sequence: Godhika, "
            "Subāhu, Valliya, Uttiya, Añjanavaniya, the two "
            "Kuṭivihārins, Ramaṇīyakuṭika, and Kosalavihārin together "
            "with Sīvali, joined into one compound in the final line. "
            "Sujato's translation leaves both untranslated, and "
            "neither appears in this page's text below."]),
    ],
    terms=[
        ("ijjhi&#7745;su",
         "&ldquo;came true&rdquo; or &ldquo;succeeded&rdquo; &mdash; "
         "describing Sīvali's fulfilled wish."),
        ("vijj&amacr;vimutti&#7745;",
         "&ldquo;knowledge and liberation&rdquo; &mdash; what Sīvali "
         "says he sought."),
        ("m&amacr;n&amacr;nusaya",
         "&ldquo;the tendency to conceit&rdquo; &mdash; one of the "
         "underlying tendencies (anusaya), named here for the first "
         "time outright in this collection's poems so far."),
        ("ujjaha&#7745;",
         "&ldquo;I gave up&rdquo; &mdash; per Sujato's comment, a "
         "reflexive first-person aorist verb."),
        ("ku&#7789;i&#7745;",
         "&ldquo;hut&rdquo; &mdash; the word this verse shares with "
         "all nine poems before it in this chapter, without "
         "exception."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.60:1.1-1.4"),
    ],
    quiz=[
        {"q": "What word does this verse share with every other poem in Chapter Six, without exception?",
         "opts": [
             "Hut",
             "River",
             "Mountain",
             "Ocean"],
         "correct": 0,
         "expl": "Ten poems in a row, all sharing this one image."},
        {"q": "What does Sīvali say he gave up, according to this verse?",
         "opts": [
             "His robe",
             "His alms bowl",
             "His teacher",
             "The tendency to conceit"],
         "correct": 3,
         "expl": "Mānānusaya, named outright for the first time so far in this collection."},
        {"q": "According to Sujato's comment, what grammatical form is 'ujjahaṁ'?",
         "opts": [
             "A future tense verb",
             "A reflexive first-person aorist",
             "A passive imperative",
             "A vocative noun"],
         "correct": 1,
         "expl": "Confirming Sīvali gave up his own tendency, to himself."},
        {"q": "What did Sīvali say he sought, according to the verse?",
         "opts": [
             "Wealth and fame",
             "A larger hut",
             "Companionship",
             "Knowledge and liberation"],
         "correct": 3,
         "expl": "Vijjāvimuttiṁ, naming his stated purpose."},
        {"q": "What does this reading guide say about a later elder in the canon who shares Sīvali's name?",
         "opts": [
             "It confirms they are definitely the same person",
             "It notes the name recurs without asserting they are the same person",
             "It states they cannot possibly be the same person",
             "No such name recurs anywhere else"],
         "correct": 1,
         "expl": "The same cautious treatment applied to Godhika earlier in this chapter."},
        {"q": "What does the Pali text carry immediately after this poem, left untranslated by Sujato?",
         "opts": [
             "A new eleventh poem",
             "Nothing follows this poem",
             "'Vaggo chaṭṭho' ('the sixth chapter is finished') and an uddāna naming all ten monks of the chapter",
             "A prose narrative"],
         "correct": 2,
         "expl": "The same untranslated colophon pattern seen at the end of Chapters One through Five."},
        {"q": "Does this page's text include that closing uddāna?",
         "opts": [
             "Yes, translated in full",
             "No — it is absent from Sujato's translation and not included here",
             "Yes, but only partially",
             "It is included as an image only"],
         "correct": 1,
         "expl": "Consistent with how this site handles untranslated structural material."},
        {"q": "How many monks' verses make up Chapter Six in total?",
         "opts": [
             "Ten",
             "Six",
             "Twenty",
             "One hundred and twenty"],
         "correct": 0,
         "expl": "Godhika through Sīvali, named in sequence in the untranslated uddāna."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the final chapter",
             "Exactly one more",
             "Six more chapters",
             "Twenty more chapters"],
         "correct": 2,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
        {"q": "What does 'vijjāvimuttiṁ' mean?",
         "opts": [
             "Knowledge and liberation",
             "Wealth and power",
             "Robes and almsbowls",
             "Fame and honor"],
         "correct": 0,
         "expl": "What Sīvali says he sought upon entering his hut."},
    ],
    marginalia=[
        ("Ten for ten", [
            "every poem, one hut —",
            "no exception, this chapter"
        ]),
        ("A tendency, named outright", [
            "not just conceit —",
            "the tendency toward it"
        ]),
        ("A grammatical footnote", [
            "reflexive, first person —",
            "done to himself"
        ]),
        ("A name, not a claim", [
            "Sīvali, elsewhere too —",
            "resemblance, not proof"
        ]),
    ],
    further=[
        '<a href="%s/thag1.60/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.51.html">Thag 1.51 &mdash; Godhika</a> '
        "&mdash; opening this chapter with the same hut theme that "
        "closes it here.",
        '<a href="thag-1.59.html">Thag 1.59 &mdash; Kosalavih&amacr;'
        "rin</a> &mdash; the poem immediately before this one, in the "
        "same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.61 — Vappa
# --------------------------------------------------------------------------- #
page(
    1, 61, "Vappa", "Vappa",
    meta_title="Thag 1.61 — Vappa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vappa's verse, opening Chapter Seven with a compact, riddle-"
        "like wordplay on seeing and not seeing. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; a compact, self-contained "
                    "wordplay"),
        ("Speaker", "Vappa, stating a chiastic riddle about seeing"),
        ("Form", "One four-line verse, built entirely from four forms "
                 "of a single verb"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but genuinely puzzle-like"),
    ],
    why=(
        "Chapter Seven opens with a riddle built from a single "
        "repeated verb, passati, &lsquo;sees&rsquo;: one who sees "
        "sees both those who see and those who don't; one who doesn't "
        "see sees neither. The verse never says what &lsquo;seeing&rsquo; "
        "stands for &mdash; it leaves that entirely to the reader."),
    guide=[
        ("A verse built from one verb, four times", [
            "Passati, &lsquo;sees&rsquo;, and its negation appear in "
            "every line of this verse, arranged so that each half "
            "mirrors and inverts the other: seeing sees both "
            "categories, not-seeing sees neither. The structure itself "
            "is the entire content &mdash; there is no narrative, no "
            "simile, no named object of sight."]),
        ("A name shared with one of the first five", [
            "Vappa is also the name of one of the &lsquo;group of "
            "five&rsquo; ascetics who heard the Buddha's first sermon "
            "at Isipatana, alongside Koṇḍañña, Bhaddiya, Mahānāma, and "
            "Assaji &mdash; a piece of well-known background about the "
            "early Saṅgha, not a claim this verse itself makes or that "
            "this reading guide can confirm applies to this particular "
            "poem."]),
        ("Seeing, left uninterpreted", [
            "This reading guide does not resolve what &lsquo;seeing&rsquo; "
            "refers to here &mdash; likely insight or wisdom, given how "
            "the term functions elsewhere in the canon, but the verse "
            "itself supplies no object, no simile, and no narrative "
            "frame to anchor that reading. It is presented here as "
            "the compact, self-contained wordplay it is on the page."]),
    ],
    terms=[
        ("passati",
         "&ldquo;sees&rdquo; &mdash; the single verb this entire "
         "verse is built from, repeated and negated across all four "
         "lines."),
        ("passa",
         "&ldquo;one who sees&rdquo; &mdash; the verse's first "
         "category, said to see both those who see and those who "
         "don't."),
        ("apassanta",
         "&ldquo;one who doesn't see&rdquo; or &ldquo;not seeing&rdquo; "
         "&mdash; the verse's second category, said to see neither."),
        ("Isipatana",
         "the deer park near Vārāṇasī where the Buddha's first sermon "
         "was heard by the group of five, including a monk named "
         "Vappa."),
        ("Koṇḍañña",
         "the clan name of the first of the group of five to attain "
         "stream-entry, and a name shared by another elder later in "
         "this chapter, Vimalakoṇḍañña."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.61:1.1-1.4"),
    ],
    quiz=[
        {"q": "What single verb does this entire verse repeat and negate?",
         "opts": [
             "Passati, 'sees'",
             "Karoti, 'does'",
             "Gacchati, 'goes'",
             "Bhāsati, 'speaks'"],
         "correct": 0,
         "expl": "The verse's whole structure is built from this one verb."},
        {"q": "According to the verse, what does 'one who sees' see?",
         "opts": [
             "Only those who see",
             "Only those who don't see",
             "Both those who see and those who don't",
             "Nothing at all"],
         "correct": 2,
         "expl": "The first half of the chiastic structure."},
        {"q": "According to the verse, what does 'one who doesn't see' see?",
         "opts": [
             "Both categories",
             "Only those who see",
             "Neither category",
             "Only those who don't see"],
         "correct": 2,
         "expl": "The mirrored, inverted second half."},
        {"q": "Does this reading guide assert a specific meaning for 'seeing' in this verse?",
         "opts": [
             "Yes, it definitively means literal eyesight",
             "No — it notes a likely reading (insight or wisdom) without asserting the verse confirms it",
             "Yes, it definitively means memory",
             "The reading guide refuses to discuss the question at all"],
         "correct": 1,
         "expl": "The verse itself supplies no object or narrative frame."},
        {"q": "What well-known group does the name Vappa also belong to, according to this reading guide?",
         "opts": [
             "The group of five ascetics who heard the Buddha's first sermon",
             "The Buddha's own family",
             "A group of merchants",
             "No such group is mentioned"],
         "correct": 0,
         "expl": "Background knowledge about the early Saṅgha, not a claim this verse itself makes."},
        {"q": "Where was the Buddha's first sermon heard, according to this reading guide?",
         "opts": [
             "Rājagaha",
             "Sāvatthī",
             "Kapilavatthu",
             "Isipatana, near Vārāṇasī"],
         "correct": 3,
         "expl": "The traditional site of the first sermon."},
        {"q": "What other elder later in this chapter shares a clan name with one of the group of five?",
         "opts": [
             "Meghiya",
             "Vimalakoṇḍañña",
             "Channa",
             "Pakkha"],
         "correct": 1,
         "expl": "Both carry the name Koṇḍañña."},
        {"q": "What does this verse include, unlike most poems so far in this collection?",
         "opts": [
             "A narrative setting",
             "A named simile",
             "No narrative, no simile — only the repeated verb structure",
             "A direct address to the Buddha"],
         "correct": 2,
         "expl": "The structure itself is the entire content of the verse."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "It closes the entire collection",
             "It is part of the Book of the Twos",
             "It opens Chapter One",
             "It opens Chapter Seven, the Book of the Ones' seventh chapter"],
         "correct": 3,
         "expl": "The first of ten poems in this new chapter."},
        {"q": "What does 'apassanta' mean?",
         "opts": [
             "One who sees",
             "One who doesn't see",
             "One who speaks",
             "One who teaches"],
         "correct": 1,
         "expl": "The verse's second category, mirroring and inverting the first."},
    ],
    marginalia=[
        ("A verb, turned over four times", [
            "sees, and sees not —",
            "the whole verse, one word"
        ]),
        ("A mirror, not a lesson", [
            "seeing sees both;",
            "not-seeing sees neither"
        ]),
        ("A name from the first sermon", [
            "one of the five,",
            "unconfirmed but noted"
        ]),
        ("No object supplied", [
            "seeing what? —",
            "the verse does not say"
        ]),
    ],
    further=[
        '<a href="%s/thag1.61/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.60.html">Thag 1.60 &mdash; S&imacr;vali</a> '
        "&mdash; the poem immediately before this one, closing Chapter "
        "Six.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.62 — Vajjiputta (1st)
# --------------------------------------------------------------------------- #
page(
    1, 62, "Vajjiputta", "Vajjiputta (1st)",
    meta_title="Thag 1.62 — Vajjiputta (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vajjiputta's verse, comparing solitary forest life to a "
        "discarded log, yet envied the way hell-beings envy one bound "
        "for heaven. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 2 of 10",
    glance=[
        ("Setting", "The wilderness, dwelling alone"),
        ("Speaker", "Vajjiputta, comparing himself to a discarded "
                    "log"),
        ("Form", "One four-line verse, built on a single paired "
                 "simile"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "sharp reversal packed into two similes"),
    ],
    why=(
        "Vajjiputta compares his own solitary life to something "
        "ordinary people would consider worthless: &lsquo;a log "
        "dumped in a forest&rsquo;. Then the verse turns that "
        "worthlessness inside out &mdash; he is envied by many, the "
        "way beings in hell envy one bound for heaven."),
    guide=[
        ("A name marking regional origin, not clan or place of dwelling", [
            "Vajjiputta, &lsquo;son of a Vajjian&rsquo;, names its "
            "bearer by the region of his birth or family, the Vajji "
            "confederacy northeast of Magadha &mdash; a different kind "
            "of place-based name from Sītavaniya or Kosalavihārin "
            "earlier in this collection, which named where a monk "
            "lived rather than where he came from."]),
        ("A self-image chosen for its lowliness", [
            "A discarded log has no purpose left, no further use to "
            "anyone &mdash; the verse deliberately picks the least "
            "flattering possible image for a solitary forest-dwelling "
            "monk's own life, before reversing it entirely in the "
            "second half."]),
        ("Envy measured against its opposite", [
            "The verse's second simile doesn't simply say Vajjiputta "
            "is envied; it specifies the intensity by comparing it to "
            "the envy of beings in hell for one headed to heaven "
            "&mdash; the widest possible gap in fortune the canon's "
            "cosmology can supply, applied to something as modest as a "
            "life alone in the wilderness."]),
        ("A second Vajjiputta, expected elsewhere", [
            "The ordinal &lsquo;(1st)&rsquo; marks this monk as "
            "distinct from another elder sharing his name later in the "
            "collection, following the same pattern already seen with "
            "Tissa, Vaccha, Valliya, and Uttiya earlier in this book."]),
    ],
    terms=[
        ("Vajjiputta",
         "&ldquo;son of a Vajjian&rdquo; &mdash; naming this monk by "
         "his regional origin, the Vajji confederacy."),
        ("apaviddha&#7745;",
         "&ldquo;dumped&rdquo; or &ldquo;discarded&rdquo; &mdash; "
         "describing the log this verse compares its speaker to."),
        ("d&amacr;ruka&#7745;",
         "&ldquo;log&rdquo; or &ldquo;piece of wood&rdquo; &mdash; the "
         "verse's central, deliberately unflattering self-image."),
        ("pihayanti",
         "&ldquo;are jealous of&rdquo; or &ldquo;envy&rdquo; &mdash; "
         "what the verse says many people feel toward Vajjiputta."),
        ("nerayik&amacr;",
         "&ldquo;beings in hell&rdquo; &mdash; the extreme comparison "
         "the verse uses to measure that envy."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.62:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Vajjiputta compare himself to, dwelling alone in the wilderness?",
         "opts": [
             "A blazing fire",
             "A discarded log dumped in a forest",
             "A mountain peak",
             "A flowing river"],
         "correct": 1,
         "expl": "A deliberately unflattering, purposeless image."},
        {"q": "What does the name Vajjiputta mean?",
         "opts": [
             "A place where he built his hut",
             "A kinship title from his son",
             "It has no particular meaning",
             "Son of a Vajjian, naming him by regional origin"],
         "correct": 3,
         "expl": "A different kind of place-based name from Sītavaniya or Kosalavihārin."},
        {"q": "According to the verse, who envies Vajjiputta?",
         "opts": [
             "No one envies him",
             "Only his own family",
             "Lots of people",
             "Only other monks"],
         "correct": 2,
         "expl": "The verse's second, reversing half."},
        {"q": "What comparison does the verse use to measure that envy?",
         "opts": [
             "A poor farmer envying a merchant",
             "A student envying a teacher",
             "No comparison is given",
             "Beings in hell envying one bound for heaven"],
         "correct": 3,
         "expl": "The widest possible gap in fortune the canon's cosmology supplies."},
        {"q": "What does the ordinal '(1st)' attached to Vajjiputta's name signal?",
         "opts": [
             "That he was the very first monk ordained",
             "That another elder shares his name later in the collection",
             "That this is his first of many verses",
             "Nothing in particular"],
         "correct": 1,
         "expl": "The same disambiguation pattern seen with Tissa, Vaccha, Valliya, and Uttiya."},
        {"q": "What does 'dāruka' mean?",
         "opts": [
             "A log or piece of wood",
             "A mountain",
             "A river",
             "A robe"],
         "correct": 0,
         "expl": "The verse's central self-image."},
        {"q": "According to this reading guide, why does the verse choose a discarded log as its self-image?",
         "opts": [
             "Because logs are valuable building material",
             "Because it is deliberately the least flattering, most purposeless image available",
             "Because Vajjiputta was once a woodcutter",
             "The choice is never explained"],
         "correct": 1,
         "expl": "A lowliness chosen precisely to set up the verse's reversal."},
        {"q": "What does 'pihayanti' mean?",
         "opts": [
             "Are jealous of, or envy",
             "Are afraid of",
             "Ignore",
             "Respect from a distance"],
         "correct": 0,
         "expl": "What many people are said to feel toward Vajjiputta."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "First",
             "Last",
             "Second",
             "Third"],
         "correct": 2,
         "expl": "Poem 2 of 10."},
        {"q": "What does 'nerayikā' mean?",
         "opts": [
             "Beings in hell",
             "Gods in heaven",
             "Human beings",
             "Animals"],
         "correct": 0,
         "expl": "The extreme comparison used to measure Vajjiputta's envied status."},
    ],
    marginalia=[
        ("A log, dumped and forgotten", [
            "purposeless, discarded —",
            "the chosen self-image"
        ]),
        ("Envy, at its widest gap", [
            "hell for heaven —",
            "applied to a life alone"
        ]),
        ("A name from where he was born", [
            "Vajji's son,",
            "not where he now dwells"
        ]),
        ("A second Vajjiputta, expected", [
            "'(1st)' marks him,",
            "a namesake still ahead"
        ]),
    ],
    further=[
        '<a href="%s/thag1.62/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.61.html">Thag 1.61 &mdash; Vappa</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.63 — Pakkha
# --------------------------------------------------------------------------- #
page(
    1, 63, "Pakkha", "Pakkha",
    meta_title="Thag 1.63 — Pakkha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Pakkha's verse, a compact contrast between those who fall and "
        "greedily return and a happiness reached through happiness "
        "itself. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative setting; a compact, two-part "
                    "contrast"),
        ("Speaker", "Pakkha, contrasting those who fall and return "
                    "with his own completed happiness"),
        ("Form", "One four-line verse, split into two matched halves"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "compact and somewhat riddle-like, without "
                       "narrative support"),
    ],
    why=(
        "This verse's first half describes those who &lsquo;fall, "
        "collapsed and fallen&rsquo;, then &lsquo;greedy, "
        "return&rsquo; &mdash; language that suggests falling away "
        "from an attainment and being drawn back by craving. Its "
        "second half turns to Pakkha's own condition: the work "
        "finished, the joyful enjoyed, happiness reached through "
        "happiness itself."),
    guide=[
        ("Two halves, left to face each other", [
            "The verse never states outright that its two halves "
            "contrast &mdash; it simply places &lsquo;they fall&rsquo; "
            "beside &lsquo;the work is done&rsquo; and lets the "
            "reader draw the comparison between falling back into "
            "craving and reaching a settled happiness."]),
        ("A compact verse this reading guide does not over-resolve", [
            "Exactly who &lsquo;they&rsquo; are in the first half, "
            "and precisely what &lsquo;happiness found through "
            "happiness&rsquo; means in the technical sense, are left "
            "genuinely underspecified by the verse itself, with no "
            "comment from Sujato to anchor a single reading. This "
            "guide presents the verse as the compact, riddle-like "
            "statement it is rather than forcing one paraphrase onto "
            "it."]),
        ("A third puzzle-like verse to open this chapter", [
            "Pakkha's verse joins Vappa's seeing-and-not-seeing riddle "
            "and Vajjiputta's reversed simile as this chapter's third "
            "compact, structurally built poem in a row &mdash; a "
            "cluster of unusually dense, short verses opening Chapter "
            "Seven before the chapter's tone shifts with the poems "
            "that follow."]),
    ],
    terms=[
        ("cut&amacr;",
         "&ldquo;fallen away&rdquo; or &ldquo;departed&rdquo; &mdash; "
         "opening this verse's first half."),
        ("giddh&amacr;",
         "&ldquo;greedy&rdquo; &mdash; describing those who "
         "&lsquo;return&rsquo; in this verse's first half."),
        ("kata&#7745; kicca&#7745;",
         "&ldquo;the work is done&rdquo; &mdash; a standard phrase for "
         "completed practice, opening this verse's second half."),
        ("sukhena anv&amacr;gata&#7745; sukha&#7745;",
         "&ldquo;happiness found through happiness&rdquo; &mdash; the "
         "verse's closing phrase, left without further explanation."),
        ("Pakkha",
         "this monk's own name, meaning &ldquo;wing&rdquo; or "
         "&ldquo;side&rdquo; &mdash; not explained or played on "
         "within the verse itself."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.63:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's first half describe?",
         "opts": [
             "Those who fall, collapsed and fallen, then greedily return",
             "A journey across a river",
             "A teaching on ethics",
             "A description of a hut"],
         "correct": 0,
         "expl": "Language suggesting falling away from attainment and being drawn back by craving."},
        {"q": "What does this verse's second half describe?",
         "opts": [
             "A dispute with another monk",
             "The work done, the joyful enjoyed, happiness found through happiness",
             "A storm at sea",
             "A visit from deities"],
         "correct": 1,
         "expl": "Pakkha's own contrasting condition."},
        {"q": "According to this reading guide, does the verse explicitly state that its two halves contrast?",
         "opts": [
             "Yes, in an explicit statement",
             "Yes, but only in the attribution line",
             "The verse has only one half",
             "No — it simply places the two halves side by side, leaving the comparison to the reader"],
         "correct": 3,
         "expl": "The contrast is implied by structure, not stated outright."},
        {"q": "According to this reading guide, does a Sujato comment clarify the precise meaning of 'happiness found through happiness'?",
         "opts": [
             "Yes, in full detail",
             "Yes, but only partially",
             "No — no comment exists, and this guide does not force a single paraphrase onto the phrase",
             "The phrase does not appear in the verse"],
         "correct": 2,
         "expl": "A genuinely compact, underspecified phrase, presented honestly as such."},
        {"q": "What does 'giddhā' mean?",
         "opts": [
             "Fearful",
             "Wealthy",
             "Mindful",
             "Greedy"],
         "correct": 3,
         "expl": "Describing those who 'return' in this verse's first half."},
        {"q": "What two earlier poems in this chapter does this reading guide group this verse with, as compact and structurally built?",
         "opts": [
             "Godhika's and Subāhu's rain-and-hut verses",
             "Vappa's seeing riddle and Vajjiputta's reversed simile",
             "No earlier poems are similar",
             "Kuṭivihārin's two poems"],
         "correct": 1,
         "expl": "A cluster of three unusually dense, short verses opening Chapter Seven."},
        {"q": "What does 'kataṁ kiccaṁ' mean?",
         "opts": [
             "The work is done",
             "The journey begins",
             "The teaching continues",
             "The question remains"],
         "correct": 0,
         "expl": "A standard phrase for completed practice."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "First",
             "Second",
             "Third",
             "Last"],
         "correct": 2,
         "expl": "Poem 3 of 10."},
        {"q": "What does 'cutā' mean?",
         "opts": [
             "Fallen away or departed",
             "Arrived",
             "Awakened",
             "Taught"],
         "correct": 0,
         "expl": "Opening this verse's first half."},
        {"q": "What does the name Pakkha mean?",
         "opts": [
             "Fire",
             "Wing or side",
             "River",
             "Mountain"],
         "correct": 1,
         "expl": "Not explained or played on within the verse itself."},
    ],
    marginalia=[
        ("Two halves, unjoined by comment", [
            "they fall and return;",
            "the work, already done"
        ]),
        ("A phrase left to stand alone", [
            "happiness through happiness —",
            "no further gloss offered"
        ]),
        ("A third riddle in a row", [
            "seeing, a log,",
            "now falling and returning"
        ]),
        ("Craving's return, named plainly", [
            "greedy, they come back —",
            "no euphemism used"
        ]),
    ],
    further=[
        '<a href="%s/thag1.63/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.62.html">Thag 1.62 &mdash; Vajjiputta '
        "(1st)</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.64 — Vimalako&#7751;&ntilde;a&ntilde;&ntilde;a
# --------------------------------------------------------------------------- #
page(
    1, 64, "Vimalako&#7751;&ntilde;a&ntilde;&ntilde;a", "Vimalako&#7751;&ntilde;a&ntilde;&ntilde;a",
    meta_title="Thag 1.64 — Vimalakoṇḍañña | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vimalakoṇḍañña's verse, a densely worded riddle built on the "
        "word 'banner' repeated four times. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative setting; a dense, symbol-laden "
                    "verse about origin and destruction"),
        ("Speaker", "Vimalakoṇḍañña, describing his birth and an act "
                    "of destruction in riddling epithets"),
        ("Form", "One four-line verse, built around the word "
                 "&lsquo;banner&rsquo; repeated four times"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "densely metaphorical, and genuinely opaque in "
                       "places"),
    ],
    why=(
        "This verse states that Vimalakoṇḍañña &lsquo;arose from the "
        "one named after a tree&rsquo; and was &lsquo;born of the one "
        "whose banner shines&rsquo;, then closes with a riddling line: "
        "&lsquo;the banner killer has destroyed the great banner, by "
        "means of the banner itself&rsquo;. The word "
        "&lsquo;banner&rsquo;, ketu, appears four times in four "
        "lines, and this reading guide does not claim to fully "
        "untangle what each occurrence refers to."),
    guide=[
        ("A verse built on one recurring word", [
            "Ketu, &lsquo;banner&rsquo;, threads through all four "
            "lines of this verse in different forms &mdash; "
            "paṇḍaraketunā (&lsquo;by the one whose banner is "
            "pale&rsquo;), ketuhā (&lsquo;banner killer&rsquo;), "
            "ketunā (&lsquo;by the banner&rsquo;), and mahāketuṁ "
            "(&lsquo;the great banner&rsquo;) &mdash; a formal density "
            "unlike anything else in this chapter so far."]),
        ("Parentage described in epithets, not names", [
            "The verse's first half describes Vimalakoṇḍañña's birth "
            "through two epithets &mdash; &lsquo;the one named after "
            "a tree&rsquo; and &lsquo;the one whose banner "
            "shines&rsquo; &mdash; rather than naming his parents "
            "outright. Whether these epithets name his actual mother "
            "and father, or point to something else entirely, is not "
            "something this reading guide resolves."]),
        ("A closing riddle this guide presents without forcing a reading", [
            "&lsquo;The banner killer has destroyed the great banner, "
            "by means of the banner itself&rsquo; reads as a "
            "deliberate paradox &mdash; something is undone using its "
            "own instrument. No Sujato comment survives for this "
            "verse to anchor a specific interpretation, so this guide "
            "presents the line as written, in full recognition of its "
            "opacity, rather than supplying a confident paraphrase."]),
        ("A clan name shared with the founding elder Koṇḍañña", [
            "Koṇḍañña is also the clan name of Aññā Koṇḍañña, "
            "traditionally remembered as the first of the Buddha's "
            "disciples to attain stream-entry, at the first sermon "
            "alongside Vappa, who opened this chapter. Whether "
            "Vimalakoṇḍañña was related to that elder, this reading "
            "guide does not assert &mdash; only that the clan name "
            "recurs within a few poems of each other in this same "
            "chapter."]),
    ],
    terms=[
        ("ketu",
         "&ldquo;banner&rdquo; &mdash; the word this entire verse is "
         "built around, appearing in four different forms across its "
         "four lines."),
        ("dumavhay&amacr;",
         "&ldquo;named after a tree&rdquo; &mdash; the epithet given "
         "for the one Vimalakoṇḍañña says he &lsquo;arose from&rsquo;."),
        ("pa&#7751;&#7693;araketu",
         "&ldquo;pale-&rdquo; or &ldquo;white-banner&rdquo; &mdash; "
         "the epithet for the one he says he was &lsquo;born of&rsquo;."),
        ("ketuh&amacr;",
         "&ldquo;banner killer&rdquo; &mdash; the agent of this "
         "verse's closing, paradoxical act."),
        ("Ko&#7751;&ntilde;a&ntilde;&ntilde;a",
         "a clan name shared with A&ntilde;&ntilde;&amacr; Ko&#7751;"
         "&ntilde;a&ntilde;&ntilde;a, traditionally the first of the "
         "Buddha's disciples to attain stream-entry."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.64:1.1-1.4"),
    ],
    quiz=[
        {"q": "What word appears four times, in different forms, across this verse's four lines?",
         "opts": [
             "Ketu, 'banner'",
             "Kuṭi, 'hut'",
             "Vijjā, 'knowledge'",
             "Metta, 'kindness'"],
         "correct": 0,
         "expl": "A formal density unlike anything else in this chapter so far."},
        {"q": "How does the verse describe Vimalakoṇḍañña's parentage?",
         "opts": [
             "By naming his parents outright",
             "Through epithets — 'the one named after a tree' and 'the one whose banner shines' — rather than names",
             "It says nothing about his birth",
             "By describing his birthplace"],
         "correct": 1,
         "expl": "Riddling description rather than direct naming."},
        {"q": "What does the verse's closing line describe?",
         "opts": [
             "A journey to another kingdom",
             "A teaching to householders",
             "'The banner killer' destroying 'the great banner' by means of the banner itself",
             "A dialogue between two monks"],
         "correct": 2,
         "expl": "A deliberate paradox — something undone using its own instrument."},
        {"q": "According to this reading guide, does a surviving Sujato comment resolve this verse's riddling imagery?",
         "opts": [
             "Yes, in full detail",
             "No — no comment survives, and this guide does not force a confident paraphrase",
             "Yes, but only partially",
             "The verse contains no riddling imagery"],
         "correct": 1,
         "expl": "The line is presented as written, with its opacity acknowledged."},
        {"q": "What clan name does Vimalakoṇḍañña share with a founding figure of the early Saṅgha?",
         "opts": [
             "Vaccha",
             "Sākiya",
             "Koṇḍañña",
             "Gotama"],
         "correct": 2,
         "expl": "Shared with Aññā Koṇḍañña, traditionally the first to attain stream-entry."},
        {"q": "What earlier poem in this chapter also names a member of the traditional group of five ascetics?",
         "opts": [
             "Vappa's opening verse",
             "Vajjiputta's verse",
             "Pakkha's verse",
             "No earlier poem does this"],
         "correct": 0,
         "expl": "Vappa is also the name of one of the group of five."},
        {"q": "According to this reading guide, does it assert that Vimalakoṇḍañña was related to the elder Koṇḍañña?",
         "opts": [
             "Yes, definitively",
             "No — it only notes the clan name recurs, without asserting a relationship",
             "Yes, but only distantly",
             "The question never arises"],
         "correct": 1,
         "expl": "A careful, non-committal note rather than a claimed relationship."},
        {"q": "What does 'dumavhayā' mean?",
         "opts": [
             "Named after a river",
             "Named after a mountain",
             "Named after a star",
             "Named after a tree"],
         "correct": 3,
         "expl": "The epithet for the one Vimalakoṇḍañña 'arose from'."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "Second",
             "Third",
             "Fourth",
             "Last"],
         "correct": 2,
         "expl": "Poem 4 of 10."},
        {"q": "What does 'ketuhā' mean?",
         "opts": [
             "Tree climber",
             "River crosser",
             "Mountain dweller",
             "Banner killer"],
         "correct": 3,
         "expl": "The agent of this verse's closing, paradoxical act."},
    ],
    marginalia=[
        ("One word, four times over", [
            "banner, banner-killer,",
            "banner destroying banner"
        ]),
        ("Parents named by riddle", [
            "tree-named, banner-bright —",
            "no names given outright"
        ]),
        ("A paradox, left standing", [
            "destroyed by its own means —",
            "no gloss supplied"
        ]),
        ("A clan name, echoing forward", [
            "Koṇḍañña again,",
            "unconfirmed kinship"
        ]),
    ],
    further=[
        '<a href="%s/thag1.64/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.61.html">Thag 1.61 &mdash; Vappa</a> '
        "&mdash; naming another of the group of five ascetics, "
        "opening this chapter.",
        '<a href="thag-1.63.html">Thag 1.63 &mdash; Pakkha</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.65 — Ukkhepakatavaccha
# --------------------------------------------------------------------------- #
page(
    1, 65, "Ukkhepakatavaccha", "Ukkhepakatavaccha",
    meta_title="Thag 1.65 — Ukkhepakatavaccha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ukkhepakatavaccha's verse, a third-person account of Vaccha "
        "tossing away years of accumulation and teaching householders "
        "with joy. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 5 of 10",
    glance=[
        ("Setting", "Sitting comfortably, teaching a group of "
                    "householders"),
        ("Speaker", "A voice describing Vaccha in the third person"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "straightforward once the third-person voicing "
                       "is noticed"),
    ],
    why=(
        "Unlike the mostly first-person poems around it, this verse "
        "describes its own subject entirely in the third person: "
        "&lsquo;Vaccha has tossed away what he built over many "
        "years&rsquo;, then pictures him &lsquo;sitting comfortably, "
        "uplifted with joy&rsquo;, teaching householders. Even the "
        "monk's own name records that same act of tossing away."),
    guide=[
        ("A name that repeats the verse's own action", [
            "Ukkhepakata, &lsquo;has tossed away&rsquo;, is joined "
            "directly to Vaccha, the clan name already seen three "
            "times in Chapter Two (Cūḷavaccha, Mahāvaccha, Vanavaccha) "
            "&mdash; but here disambiguated not by a size-prefix "
            "(&lsquo;little&rsquo;, &lsquo;great&rsquo;, "
            "&lsquo;forest&rsquo;) but by an epithet describing the "
            "very deed the verse itself narrates."]),
        ("Third person, without a named narrator", [
            "The verse never says who is speaking or watching Vaccha "
            "teach &mdash; it simply reports what he did and how he "
            "now sits, joined to the Theragātha's convention that "
            "each poem is nonetheless attributed to its own subject "
            "as speaker, the same convention already seen with "
            "Siṅgālapitā's assessment of another monk in Chapter Two."]),
        ("What was 'built over many years', left unspecified", [
            "The verse doesn't say what Vaccha accumulated and then "
            "discarded &mdash; property, views, habits, or something "
            "else entirely. What the verse insists on is only the "
            "act itself, and the joy that followed it."]),
    ],
    terms=[
        ("ukkhepakata",
         "&ldquo;has tossed away&rdquo; or &ldquo;cast off&rdquo; "
         "&mdash; joined directly to this monk's own name."),
        ("saṅkalita&#7745;",
         "&ldquo;what was accumulated&rdquo; or &ldquo;built up&rdquo; "
         "&mdash; the object of that tossing away, left unspecified."),
        ("gaha&#7789;&#7745;",
         "&ldquo;householders&rdquo; &mdash; those Vaccha is described "
         "teaching."),
        ("u&#7735;&amacr;rap&amacr;mojjo",
         "&ldquo;uplifted with joy&rdquo; &mdash; describing Vaccha's "
         "state while teaching."),
        ("Vaccha",
         "a clan name shared with three monks already covered in "
         "Chapter Two: Cūḷavaccha, Mahāvaccha, and Vanavaccha."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.65:1.1-1.4"),
    ],
    quiz=[
        {"q": "In what grammatical person is this verse written?",
         "opts": [
             "First person throughout",
             "Second person throughout",
             "It shifts between all three",
             "Third person throughout"],
         "correct": 3,
         "expl": "An account of Vaccha, rather than a self-declaration."},
        {"q": "What does the verse say Vaccha has done?",
         "opts": [
             "Built a new hut",
             "Tossed away what he built over many years",
             "Traveled to a distant kingdom",
             "Debated another teacher"],
         "correct": 1,
         "expl": "The act his own name also records."},
        {"q": "What does the name Ukkhepakatavaccha mean?",
         "opts": [
             "A place-based name",
             "A kinship title",
             "It has no particular meaning",
             "'Vaccha who has tossed away' — the very act the verse describes"],
         "correct": 3,
         "expl": "The name repeats the verse's own content, joined to the Vaccha clan name."},
        {"q": "What clan name does Vaccha share with three monks already covered in Chapter Two?",
         "opts": [
             "Vaccha, shared with Cūḷavaccha, Mahāvaccha, and Vanavaccha",
             "Koṇḍañña",
             "Puṇṇa",
             "Tissa"],
         "correct": 0,
         "expl": "Disambiguated here by an action epithet rather than a size-prefix."},
        {"q": "According to the verse, what is Vaccha doing while he teaches?",
         "opts": [
             "Sitting comfortably, uplifted with joy",
             "Standing anxiously",
             "Weeping",
             "Fasting"],
         "correct": 0,
         "expl": "A settled, joyful state accompanying his teaching."},
        {"q": "Who is Vaccha described as teaching?",
         "opts": [
             "Other monks only",
             "Householders",
             "Animals",
             "No audience is mentioned"],
         "correct": 1,
         "expl": "Gahaṭṭhānaṁ, 'householders'."},
        {"q": "According to this reading guide, does the verse specify what Vaccha 'built over many years' and then discarded?",
         "opts": [
             "Yes, in full detail",
             "Yes, but only in the attribution line",
             "No — the verse leaves the object of that tossing away unspecified",
             "It says he discarded nothing"],
         "correct": 2,
         "expl": "Only the act and its resulting joy are insisted on."},
        {"q": "What earlier poem in this collection does this reading guide compare this verse's third-person voicing to?",
         "opts": [
             "Siṅgālapitā's assessment of another monk in Chapter Two",
             "Subhūti's opening frame",
             "Godhika's rain-and-hut verse",
             "No earlier poem is compared"],
         "correct": 0,
         "expl": "Another instance of a poem attributed to its subject while describing him in the third person."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "Third",
             "Fourth",
             "Fifth",
             "Last"],
         "correct": 2,
         "expl": "Poem 5 of 10."},
        {"q": "What does 'saṅkalitaṁ' mean?",
         "opts": [
             "What was destroyed",
             "What was accumulated or built up",
             "What was given away as alms",
             "What was taught"],
         "correct": 1,
         "expl": "The object of Vaccha's tossing away, left unspecified by the verse."},
    ],
    marginalia=[
        ("A name that narrates itself", [
            "'has tossed away' —",
            "joined right to his name"
        ]),
        ("Third person, no narrator named", [
            "Vaccha teaches, joyful —",
            "who is watching, unsaid"
        ]),
        ("Unspecified, on purpose", [
            "years of building, gone —",
            "what, exactly, unstated"
        ]),
        ("A fourth Vaccha, differently marked", [
            "not size this time —",
            "but the deed itself"
        ]),
    ],
    further=[
        '<a href="%s/thag1.65/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.64.html">Thag 1.64 &mdash; Vimalako&#7751;'
        "&ntilde;a&ntilde;&ntilde;a</a> &mdash; the poem immediately "
        "before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.66 — Meghiya
# --------------------------------------------------------------------------- #
page(
    1, 66, "Meghiya", "Meghiya",
    meta_title="Thag 1.66 — Meghiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Meghiya's verse, thanking the great hero's counsel and "
        "closing with the same three-knowledges formula heard "
        "earlier in this collection. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 6 of 10",
    glance=[
        ("Setting", "Staying close by his teacher, after receiving "
                    "counsel"),
        ("Speaker", "Meghiya, describing what he heard and attained"),
        ("Form", "One six-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a direct, gratitude-framed declaration"),
    ],
    why=(
        "Meghiya's verse opens with gratitude: &lsquo;he counseled "
        "me, the great hero, the one who has gone beyond all "
        "things&rsquo;. After staying close by that counsel, "
        "mindful, Meghiya closes with the same declaration heard "
        "from Sugandha (Thag 1.24) and Añjanavaniya (Thag 1.55) "
        "earlier in this collection: the three knowledges attained, "
        "the Buddha's instructions fulfilled."),
    guide=[
        ("A third appearance of the same closing formula", [
            "&lsquo;Tisso vijjā anuppattā, kataṁ buddhassa "
            "sāsanan&rsquo; ti &mdash; &lsquo;I've attained the three "
            "knowledges and fulfilled the Buddha's instructions&rsquo; "
            "&mdash; closes this verse exactly as it closed Sugandha's "
            "in Chapter Three and Añjanavaniya's in Chapter Six, now "
            "appearing for a third time across this collection."]),
        ("A name shared with the Buddha's attendant before Ānanda", [
            "Meghiya is also the name of the monk who served as the "
            "Buddha's personal attendant in a discourse recorded at "
            "AN 9.3 and Ud 4.1, both already covered on this site "
            "&mdash; there, Meghiya leaves the Buddha's side to "
            "meditate alone in a mango grove against advice, struggles "
            "with unwholesome thoughts, and is taught the five things "
            "that ripen the heart's release. Whether this verse's "
            "speaker is that same Meghiya, this reading guide does not "
            "assert; it notes the shared name and the matching role "
            "&mdash; staying close to a teacher's counsel &mdash; "
            "without claiming they are confirmed to be identical."]),
        ("Six lines, longer than most poems in this chapter", [
            "Where most poems in this collection's Book of the Ones "
            "run to four lines, this one extends to six &mdash; "
            "gratitude for counsel, then the act of staying close and "
            "listening, then the standard closing declaration, each "
            "given its own couplet."]),
    ],
    terms=[
        ("mah&amacr;v&imacr;ro",
         "&ldquo;the great hero&rdquo; &mdash; the title Meghiya gives "
         "the one who counseled him."),
        ("sabbadhamm&amacr;na p&amacr;rag&umacr;",
         "&ldquo;one who has gone beyond all things&rdquo; &mdash; a "
         "further epithet for that same teacher."),
        ("santike",
         "&ldquo;close by&rdquo; &mdash; describing where Meghiya "
         "stayed after hearing the teaching."),
        ("tisso vijj&amacr;",
         "&ldquo;the three knowledges&rdquo; &mdash; named in this "
         "verse's closing couplet, shared word for word with Sugandha "
         "and Añjanavaniya."),
        ("Meghiya",
         "a name shared with the Buddha's attendant in a discourse "
         "recorded at AN 9.3 and Ud 4.1, already covered on this "
         "site."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.66:1.1-1.6"),
    ],
    quiz=[
        {"q": "What title does Meghiya give to the one who counseled him?",
         "opts": [
             "The great hero, who has gone beyond all things",
             "A distant relative",
             "A fellow householder",
             "No title is given"],
         "correct": 0,
         "expl": "The verse's opening gratitude."},
        {"q": "What closing couplet does this verse share with Sugandha's (Thag 1.24) and Añjanavaniya's (Thag 1.55) verses?",
         "opts": [
             "A warning against craving",
             "An invitation to the rain god",
             "A riddle about seeing",
             "'I've attained the three knowledges and fulfilled the Buddha's instructions'"],
         "correct": 3,
         "expl": "Appearing here for a third time across this collection."},
        {"q": "What does Meghiya do after hearing the teaching, according to the verse?",
         "opts": [
             "Travels to a distant land",
             "Stays close by, mindful",
             "Debates the teaching",
             "Returns to lay life"],
         "correct": 1,
         "expl": "Vihāsiṁ santike sato — staying near, attentive."},
        {"q": "What does this reading guide say about the Meghiya of AN 9.3 and Ud 4.1?",
         "opts": [
             "It confirms this verse's speaker is definitely that same Meghiya",
             "It states they cannot possibly be the same person",
             "Neither discourse exists on this site",
             "It notes the shared name and matching role without asserting confirmed identity"],
         "correct": 3,
         "expl": "The same cautious treatment applied to other shared names earlier in this chapter."},
        {"q": "In AN 9.3, what happens after Meghiya leaves the Buddha to meditate in a mango grove?",
         "opts": [
             "He immediately attains awakening",
             "He struggles with unwholesome thoughts and is taught five things that ripen the heart's release",
             "He is expelled from the Saṅgha",
             "He returns to lay life permanently"],
         "correct": 1,
         "expl": "A well-known teaching moment, already covered on this site."},
        {"q": "How many lines does this verse have, compared to most poems in this chapter?",
         "opts": [
             "Four, the same as most poems",
             "Six, longer than most poems in this book",
             "Two, shorter than most poems",
             "Twelve"],
         "correct": 1,
         "expl": "Gratitude, staying close, and the closing declaration each given their own couplet."},
        {"q": "What role did the Meghiya of AN 9.3 hold at the time of that discourse?",
         "opts": [
             "The Buddha's personal attendant",
             "A visiting king",
             "A wandering ascetic from another tradition",
             "A merchant"],
         "correct": 0,
         "expl": "A role held before Ānanda took on that position."},
        {"q": "What does 'santike' mean?",
         "opts": [
             "Close by",
             "Far away",
             "Beneath",
             "Above"],
         "correct": 0,
         "expl": "Describing where Meghiya stayed after hearing the counsel."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "Fourth",
             "Fifth",
             "Sixth",
             "Last"],
         "correct": 2,
         "expl": "Poem 6 of 10."},
        {"q": "What does 'mahāvīro' mean?",
         "opts": [
             "The wise elder",
             "The humble servant",
             "The great hero",
             "The distant traveler"],
         "correct": 2,
         "expl": "The title opening this verse's gratitude."},
    ],
    marginalia=[
        ("A formula, heard a third time", [
            "the three knowledges again —",
            "Sugandha, then this"
        ]),
        ("A name, and a famous role", [
            "attendant before Ānanda —",
            "unconfirmed but noted"
        ]),
        ("Six lines, not four", [
            "gratitude, closeness,",
            "then the standard close"
        ]),
        ("Staying near, after counsel", [
            "not departing —",
            "remaining close, mindful"
        ]),
    ],
    further=[
        '<a href="%s/thag1.66/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../anguttara-nikaya/an-9.3.html">AN 9.3 &mdash; With '
        "Meghiya</a> &mdash; a discourse about a monk sharing this "
        "name, its connection to this verse unconfirmed but worth "
        "holding side by side.",
        '<a href="thag-1.24.html">Thag 1.24 &mdash; Sugandha</a> '
        "&mdash; sharing this verse's closing couplet, from Chapter "
        "Three.",
        '<a href="thag-1.65.html">Thag 1.65 &mdash; '
        "Ukkhepakatavaccha</a> &mdash; the poem immediately before "
        "this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.67 — Ekadhammasavan&imacr;ya
# --------------------------------------------------------------------------- #
page(
    1, 67, "Ekadhammasavan&imacr;ya", "Ekadhammasavan&imacr;ya",
    meta_title="Thag 1.67 — Ekadhammasavanīya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ekadhammasavanīya's verse, a declaration of full liberation "
        "built on a wordplay between burning away defilements and "
        "practicing absorption. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 7 of 10",
    glance=[
        ("Setting", "No narrative setting; a direct declaration of "
                    "attainment"),
        ("Speaker", "Ekadhammasavanīya, describing his own complete "
                    "liberation"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "direct, with one embedded wordplay"),
    ],
    why=(
        "Ekadhammasavanīya's own name records an unusually rapid "
        "path to awakening: eka-dhamma-savanīya, &lsquo;attained "
        "through hearing a single teaching&rsquo;. His verse opens "
        "with a wordplay Sujato's translation marks directly: "
        "&lsquo;my defilements have been burnt away, by practicing "
        "absorption&rsquo; &mdash; jhāpitā, &lsquo;burnt&rsquo;, "
        "sharing its root with jhāna, meditative absorption."),
    guide=[
        ("A name recording a claim about speed", [
            "Where Sugandha's verse (Thag 1.24) states outright that "
            "he attained the three knowledges in a single rainy "
            "season, Ekadhammasavanīya's name makes an even more "
            "compact version of the same claim &mdash; that hearing "
            "one teaching was enough &mdash; built directly into what "
            "he is called, rather than stated in the verse itself."]),
        ("A wordplay Sujato's own translation flags", [
            "Jhāpitā, &lsquo;burnt away&rsquo;, and jhāna, "
            "&lsquo;absorption&rsquo;, share a root in "
            "jhāyati &mdash; a pun the Pali makes available and that "
            "Sujato's translation marks explicitly with a bracketed "
            "note, &lsquo;by practicing absorption&rsquo;, rather than "
            "leaving the wordplay invisible in English."]),
        ("A complete declaration, stated without narrative", [
            "The verse's remaining three lines list total liberation "
            "in escalating terms: rebirth into every state of "
            "existence eradicated, transmigration through births "
            "finished, no future lives remaining &mdash; each line "
            "restating the same completion from a slightly different "
            "angle, without any narrative frame around it."]),
    ],
    terms=[
        ("jh&amacr;pit&amacr;",
         "&ldquo;burnt away&rdquo; &mdash; describing "
         "Ekadhammasavanīya's defilements, sharing a root with jhāna."),
        ("jh&amacr;na",
         "meditative absorption &mdash; the practice this verse's "
         "opening wordplay points toward without naming outright."),
        ("bhav&amacr;",
         "&ldquo;states of existence&rdquo; or &ldquo;rebirth&rdquo; "
         "&mdash; what this verse says has been entirely eradicated."),
        ("j&amacr;tisa&#7745;s&amacr;ro",
         "&ldquo;transmigration through births&rdquo; &mdash; the "
         "verse's third statement of the same completion."),
        ("punabbhavo",
         "&ldquo;future rebirth&rdquo; or &ldquo;renewed "
         "existence&rdquo; &mdash; what this verse says will no "
         "longer occur."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.67:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the name Ekadhammasavanīya mean?",
         "opts": [
             "A place-based name",
             "A clan name",
             "It has no particular meaning",
             "Attained through hearing a single teaching"],
         "correct": 3,
         "expl": "A claim about speed built directly into the name."},
        {"q": "What wordplay does the verse's opening line contain, according to this reading guide?",
         "opts": [
             "None — the line is entirely literal",
             "A pun between 'burnt away' (jhāpitā) and 'absorption' (jhāna), sharing a root",
             "A pun on the speaker's own name",
             "A pun involving the word for 'hut'"],
         "correct": 1,
         "expl": "A wordplay Sujato's translation flags with a bracketed note."},
        {"q": "How does Sujato's translation mark this wordplay?",
         "opts": [
             "It leaves the pun entirely invisible in English",
             "With a bracketed note, 'by practicing absorption'",
             "By adding a footnote citation only",
             "By omitting the line entirely"],
         "correct": 1,
         "expl": "An explicit editorial choice to surface the pun for English readers."},
        {"q": "What earlier poem in this collection makes a similar claim about the speed of attainment?",
         "opts": [
             "Godhika's rain-and-hut verse",
             "Vappa's riddle",
             "Sugandha's verse (Thag 1.24), attaining the three knowledges in a single rainy season",
             "No earlier poem makes such a claim"],
         "correct": 2,
         "expl": "Sugandha states it in the verse; Ekadhammasavanīya's name states it instead."},
        {"q": "What does the verse say has been 'entirely eradicated'?",
         "opts": [
             "Rebirth into every state of existence",
             "His alms bowl",
             "His teacher's authority",
             "His hut"],
         "correct": 0,
         "expl": "Bhavā sabbe samūhatā — total liberation stated directly."},
        {"q": "How many times does the verse restate the same completion, from different angles?",
         "opts": [
             "Once",
             "Twice",
             "Three times",
             "It never restates the same idea"],
         "correct": 2,
         "expl": "Eradicated rebirth, finished transmigration, no future lives — three angles on one claim."},
        {"q": "What does 'jātisaṁsāro' mean?",
         "opts": [
             "Transmigration through births",
             "A single teaching",
             "A hut in the wilderness",
             "A rain storm"],
         "correct": 0,
         "expl": "The verse's third statement of complete liberation."},
        {"q": "Does this verse include a narrative setting, according to this reading guide?",
         "opts": [
             "Yes, an extended one",
             "No — it is a direct declaration without narrative framing",
             "Only in the attribution line",
             "Yes, but only a brief one"],
         "correct": 1,
         "expl": "A list of completions, stated without any surrounding story."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "Fifth",
             "Sixth",
             "Seventh",
             "Last"],
         "correct": 2,
         "expl": "Poem 7 of 10."},
        {"q": "What does 'punabbhavo' mean?",
         "opts": [
             "A teaching heard once",
             "A monastic robe",
             "A meditation posture",
             "Future rebirth or renewed existence"],
         "correct": 3,
         "expl": "What the verse says will no longer occur."},
    ],
    marginalia=[
        ("A name that claims speed", [
            "one teaching heard,",
            "and that was enough"
        ]),
        ("Burnt away, or absorbed", [
            "jhāpitā, jhāna —",
            "one root, two meanings"
        ]),
        ("The same claim, three times over", [
            "eradicated, finished,",
            "no future life remains"
        ]),
        ("No story, only completion", [
            "no setting given —",
            "just the declaration itself"
        ]),
    ],
    further=[
        '<a href="%s/thag1.67/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.24.html">Thag 1.24 &mdash; Sugandha</a> '
        "&mdash; another verse claiming an unusually fast attainment, "
        "from Chapter Three.",
        '<a href="thag-1.66.html">Thag 1.66 &mdash; Meghiya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.68 — Ekud&amacr;niya
# --------------------------------------------------------------------------- #
page(
    1, 68, "Ekud&amacr;niya", "Ekud&amacr;niya",
    meta_title="Thag 1.68 — Ekudāniya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ekudāniya's verse, an impersonal maxim about the sage free "
        "from sorrow, with no first-person pronoun anywhere in it. "
        "From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative setting; a general statement about "
                    "an ideal type"),
        ("Speaker", "An impersonal voice describing 'the sage', not "
                    "a first-person self-declaration"),
        ("Form", "One four-line verse in the genitive and dative "
                 "case throughout"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain, but grammatically unusual for this "
                       "collection"),
    ],
    why=(
        "Unlike almost every poem around it, this verse contains no "
        "&lsquo;I&rsquo; at all &mdash; it describes &lsquo;a sage of "
        "higher consciousness, diligent&rsquo;, and states that "
        "&lsquo;there are no sorrows for the unaffected, calm and "
        "ever mindful&rsquo;, entirely in the third person, as a "
        "general maxim rather than a personal account."),
    guide=[
        ("A verse without a first-person pronoun", [
            "Every noun and adjective in this verse sits in the "
            "genitive or dative case, describing qualities that "
            "belong to &lsquo;such a one&rsquo; (tādino) rather than "
            "declaring &lsquo;I have done this&rsquo; or &lsquo;I am "
            "this&rsquo; &mdash; a grammatically distinct voice from "
            "the confessional first person heard through most of this "
            "collection so far."]),
        ("A name that may describe the verse itself", [
            "Ekudāniya, &lsquo;one of a single inspired "
            "utterance&rsquo;, may record that this monk was known "
            "for exactly one udāna &mdash; a spontaneous, generalized "
            "exclamation of the kind collected in the Udāna, rather "
            "than a first-person narrative of his own path. This "
            "verse's impersonal, maxim-like character fits that "
            "reading, though this guide does not assert it as "
            "confirmed."]),
        ("A maxim, not a confession", [
            "Read as a general statement rather than autobiography, "
            "the verse's claim is simple: sorrow does not arise for "
            "one who is calm, diligent, and mindful &mdash; a "
            "principle stated as true of any such person, not a "
            "report of one man's particular history."]),
    ],
    terms=[
        ("adhicetaso",
         "&ldquo;of higher consciousness&rdquo; &mdash; the first "
         "quality this verse names."),
        ("muni",
         "&ldquo;sage&rdquo; &mdash; the figure this entire verse "
         "describes, in the genitive case throughout."),
        ("t&amacr;dino",
         "&ldquo;for such a one&rdquo; or &ldquo;for the unaffected "
         "one&rdquo; &mdash; the word this verse's claim about sorrow "
         "is built around."),
        ("upasanta",
         "&ldquo;calm&rdquo; or &ldquo;peaceful&rdquo; &mdash; one of "
         "two final qualities closing the verse."),
        ("ud&amacr;na",
         "&ldquo;inspired utterance&rdquo; &mdash; the genre this "
         "monk's own name may point toward, and the title of a "
         "separate collection in the wider canon."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.68:1.1-1.4"),
    ],
    quiz=[
        {"q": "What grammatical feature does this verse lack, unlike almost every poem around it?",
         "opts": [
             "A verb",
             "Any adjectives",
             "A closing line",
             "A first-person pronoun"],
         "correct": 3,
         "expl": "The verse describes 'a sage' in the genitive and dative, not 'I'."},
        {"q": "According to the verse, what is true for 'the unaffected one, calm and ever mindful'?",
         "opts": [
             "Wealth naturally follows",
             "There are no sorrows for such a person",
             "Fame naturally follows",
             "Nothing in particular is said"],
         "correct": 1,
         "expl": "The verse's central claim, stated as a general principle."},
        {"q": "What might the name Ekudāniya record, according to this reading guide?",
         "opts": [
             "A place where he lived",
             "A kinship title",
             "Nothing in particular",
             "That he was known for exactly one spontaneous inspired utterance"],
         "correct": 3,
         "expl": "A reading this guide notes without asserting as confirmed."},
        {"q": "How does this reading guide characterize this verse compared to most poems so far?",
         "opts": [
             "As a first-person confession, like most others",
             "As a general maxim rather than a personal, autobiographical account",
             "As a dialogue between two speakers",
             "As a riddle with no resolvable meaning"],
         "correct": 1,
         "expl": "A grammatically and tonally distinct voice within this collection."},
        {"q": "What case does this verse's vocabulary sit in throughout?",
         "opts": [
             "Nominative, as a direct first-person subject",
             "Genitive and dative, describing qualities belonging to 'such a one'",
             "Vocative, addressing someone directly",
             "Accusative, as a direct object"],
         "correct": 1,
         "expl": "A structural mark of its impersonal, maxim-like character."},
        {"q": "What does 'muni' mean?",
         "opts": [
             "Sage",
             "Householder",
             "River",
             "Mountain"],
         "correct": 0,
         "expl": "The figure this entire verse describes."},
        {"q": "What does 'tādino' mean?",
         "opts": [
             "Never again",
             "In the beginning",
             "For such a one, or for the unaffected one",
             "Among householders"],
         "correct": 2,
         "expl": "The word this verse's central claim about sorrow is built around."},
        {"q": "What is the Udāna, according to this reading guide?",
         "opts": [
             "A separate collection of inspired utterances in the wider canon",
             "A monastic rule book",
             "A commentary on the Vinaya",
             "This monk's given family name"],
         "correct": 0,
         "expl": "The genre this monk's own name may point toward."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "Sixth",
             "Seventh",
             "Eighth",
             "Last"],
         "correct": 2,
         "expl": "Poem 8 of 10."},
        {"q": "What does 'adhicetaso' mean?",
         "opts": [
             "Of higher consciousness",
             "Of great wealth",
             "Of royal descent",
             "Of advanced age"],
         "correct": 0,
         "expl": "The first quality this verse names."},
    ],
    marginalia=[
        ("No 'I' anywhere in it", [
            "a sage, described —",
            "not a self, declared"
        ]),
        ("A name for a single utterance", [
            "one udāna spoken,",
            "perhaps this very verse"
        ]),
        ("A maxim, not a memoir", [
            "true of any such one —",
            "not one man's story"
        ]),
        ("Sorrow, ruled out by definition", [
            "calm, mindful, unaffected —",
            "no sorrow can enter"
        ]),
    ],
    further=[
        '<a href="%s/thag1.68/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.67.html">Thag 1.67 &mdash; '
        "Ekadhammasavan&imacr;ya</a> &mdash; the poem immediately "
        "before this one, in the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.69 — Channa
# --------------------------------------------------------------------------- #
page(
    1, 69, "Channa", "Channa",
    meta_title="Thag 1.69 — Channa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Channa's verse, entering the path after hearing the "
        "all-knowing master's sweet Dhamma. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting; a declaration made after "
                    "hearing the Dhamma"),
        ("Speaker", "Channa, describing his entry onto the path"),
        ("Form", "One four-line verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "a direct declaration built from praise of the "
                       "teacher"),
    ],
    why=(
        "Channa's verse describes hearing &lsquo;the sweet Dhamma "
        "taught by the master, all-knowing, of superb knowledge&rsquo;, "
        "and entering, on the strength of that teaching alone, "
        "&lsquo;the path to realize freedom from death&rsquo;. The "
        "verse itself says nothing beyond this moment of hearing and "
        "entering."),
    guide=[
        ("Praise of the teacher precedes the path itself", [
            "Three of this verse's four lines describe the quality of "
            "the teaching and the teacher before the fourth line "
            "states what Channa did in response &mdash; entering the "
            "path &mdash; a structure that gives more weight to why "
            "the teaching moved him than to his own subsequent "
            "progress."]),
        ("A name shared with the subject of a difficult discourse", [
            "Channa is also the name of the monk at the center of MN "
            "144, &lsquo;Advice to Channa&rsquo;, already covered on "
            "this site: gravely ill, he ends his own life after "
            "receiving counsel from Sāriputta and Mahācunda, and the "
            "Buddha subsequently declares him blameless, since he laid "
            "down no clinging when he died. Whether this verse's "
            "speaker is that same Channa, this reading guide does not "
            "assert; it notes only the shared name and reports what "
            "that discourse contains, without dwelling further on it."]),
        ("A path named, not yet walked", [
            "The verse describes entering the path, not completing "
            "it &mdash; unlike several poems elsewhere in this "
            "collection that close with a declaration of full "
            "liberation, this one ends at the point of setting out, "
            "calling the teacher &lsquo;the expert on the road to "
            "sanctuary from the yoke&rsquo; rather than claiming that "
            "sanctuary for himself yet."]),
    ],
    terms=[
        ("mahato mah&amacr;rasa&#7745;",
         "&ldquo;the sweet Dhamma taught by the master&rdquo; &mdash; "
         "literally &lsquo;of great, great flavor&rsquo;, describing "
         "the teaching Channa heard."),
        ("sabba&ntilde;&ntilde;utta&ntilde;&ntilde;&amacr;&#7751;avarena",
         "&ldquo;of superb, all-knowing knowledge&rdquo; &mdash; the "
         "epithet given to the teacher."),
        ("amata&#7745;",
         "&ldquo;freedom from death&rdquo; or &ldquo;the "
         "deathless&rdquo; &mdash; what Channa says he entered the "
         "path to realize."),
        ("yogakkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; the goal the "
         "teacher is called an expert on the road toward."),
        ("Channa",
         "a name shared with the monk at the center of MN 144, "
         "&ldquo;Advice to Channa&rdquo;, already covered on this "
         "site."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.69:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does Channa hear, according to this verse's opening lines?",
         "opts": [
             "A dispute between two teachers",
             "A story about his own past lives",
             "A warning about illness",
             "The sweet Dhamma taught by the all-knowing master"],
         "correct": 3,
         "expl": "Praise of the teaching precedes Channa's own response."},
        {"q": "What does Channa say he entered, in response to hearing that teaching?",
         "opts": [
             "A monastery",
             "The path to realize freedom from death",
             "A debate",
             "A new region to live in"],
         "correct": 1,
         "expl": "Maggaṁ papajjiṁ amatassa pattiyā."},
        {"q": "What does this reading guide say about the Channa of MN 144?",
         "opts": [
             "It confirms this verse's speaker is definitely that same Channa",
             "It states they cannot possibly be the same person",
             "MN 144 does not exist on this site",
             "It notes the shared name and reports the discourse's contents without asserting confirmed identity"],
         "correct": 3,
         "expl": "The same cautious treatment applied to other shared names in this chapter."},
        {"q": "What happens to the Channa of MN 144, according to that discourse?",
         "opts": [
             "He becomes a renowned teacher",
             "Gravely ill, he ends his own life, and the Buddha declares him blameless",
             "He disrobes and returns to lay life",
             "He travels to a distant kingdom"],
         "correct": 1,
         "expl": "A difficult discourse, reported here without further dwelling on it."},
        {"q": "How does this verse's ending compare to poems elsewhere in this collection that declare full liberation?",
         "opts": [
             "It makes the same declaration of complete liberation",
             "It denies that liberation is possible",
             "It ends at the point of entering the path, not completing it",
             "It says nothing about the path at all"],
         "correct": 2,
         "expl": "A verse about setting out, not arriving."},
        {"q": "What does 'amataṁ' mean?",
         "opts": [
             "Freedom from death, or the deathless",
             "A monastic robe",
             "A teaching heard once",
             "A hut in the wilderness"],
         "correct": 0,
         "expl": "What Channa says he entered the path to realize."},
        {"q": "What title does the verse give the teacher?",
         "opts": [
             "A humble servant",
             "The expert on the road to sanctuary from the yoke",
             "A distant traveler",
             "No title is given"],
         "correct": 1,
         "expl": "Praise closing the verse, directed outward rather than at Channa's own attainment."},
        {"q": "How much of this four-line verse describes the teaching and teacher, before turning to Channa's own response?",
         "opts": [
             "Three of its four lines",
             "None of it",
             "All four lines equally",
             "Only the attribution line"],
         "correct": 0,
         "expl": "A structure weighted toward praise before the personal response."},
        {"q": "Where does this poem fall in Chapter Seven?",
         "opts": [
             "Seventh",
             "Eighth",
             "Ninth",
             "Last"],
         "correct": 2,
         "expl": "Poem 9 of 10."},
        {"q": "What does 'yogakkhema' mean?",
         "opts": [
             "Sanctuary from the yoke",
             "A rainy season retreat",
             "A begging bowl",
             "A clan name"],
         "correct": 0,
         "expl": "The goal the teacher is called an expert on the road toward."},
    ],
    marginalia=[
        ("Praise, before response", [
            "three lines for the teacher,",
            "one for what he did"
        ]),
        ("A name, and a harder story", [
            "Channa, elsewhere too —",
            "resemblance, not proof"
        ]),
        ("Setting out, not arriving", [
            "entered the path —",
            "not yet its end"
        ]),
        ("Sweetness, named directly", [
            "mahārasaṁ —",
            "the Dhamma's own flavor"
        ]),
    ],
    further=[
        '<a href="%s/thag1.69/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-144.html">MN 144 &mdash; '
        "Advice to Channa</a> &mdash; a discourse about a monk sharing "
        "this name, its connection to this verse unconfirmed but "
        "worth holding side by side.",
        '<a href="thag-1.68.html">Thag 1.68 &mdash; Ekud&amacr;'
        "niya</a> &mdash; the poem immediately before this one, in "
        "the same chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.70 — Pu&#7751;&#7751;a (2nd)
# --------------------------------------------------------------------------- #
page(
    1, 70, "Pu&#7751;&#7751;a", "Pu&#7751;&#7751;a (2nd)",
    meta_title="Thag 1.70 — Puṇṇa (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Puṇṇa's verse, closing Chapter Seven with wisdom ranked above "
        "ethical conduct, and a Sujato comment confirming its speaker "
        "as the Puṇṇa of MN 145. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Seven &middot; Poem 10 of 10",
    glance=[
        ("Setting", "No narrative setting; a closing statement "
                    "ranking two qualities"),
        ("Speaker", "Puṇṇa (distinguished from another elder sharing "
                    "his name earlier in this book), stating a "
                    "principle about virtue and wisdom"),
        ("Form", "One four-line verse, followed in the Pali by an "
                 "untranslated chapter colophon and mnemonic summary "
                 "verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "plain ranking, closing the chapter"),
    ],
    why=(
        "Puṇṇa's verse closes Chapter Seven with a ranking: ethical "
        "conduct is best, but wisdom is supreme, and the one who "
        "holds both is victorious among men and gods. Unlike several "
        "same-named elders elsewhere in this chapter, this Puṇṇa's "
        "identity is directly confirmed by a Sujato comment, which "
        "names the exact discourse where he next appears."),
    guide=[
        ("A confirmed identity, unlike this chapter's other shared names", [
            "Godhika, Meghiya, and Channa earlier in this chapter all "
            "share their names with figures elsewhere in the canon "
            "without confirmation from any surviving comment. Puṇṇa "
            "is different: Sujato's own comment on this verse states "
            "outright that &lsquo;this Puṇṇa departs for the distant "
            "land of Sunāparanta&rsquo; in MN 145, &lsquo;Advice to "
            "Puṇṇa&rsquo;, already covered on this site &mdash; a "
            "direct, sourced identification rather than a shared-name "
            "resemblance this guide leaves open."]),
        ("A second Puṇṇa in this same collection", [
            "The ordinal &lsquo;(2nd)&rsquo; distinguishes this monk "
            "from Puṇṇa (1st), Thag 1.4 earlier in this book, whose "
            "verse gives direct advice to associate only with the "
            "virtuous &mdash; two different elders sharing one name "
            "within the Theragātha itself, confirmed by this "
            "collection's own numbering rather than an external "
            "source."]),
        ("A famous test of equanimity, waiting past this verse", [
            "MN 145 records the Buddha asking Puṇṇa, before he leaves "
            "for Sunāparanta, what he would think if its people abused "
            "him, struck him, or even killed him &mdash; a graduated "
            "series of questions Puṇṇa answers with escalating "
            "equanimity at each step. None of that exchange appears in "
            "this verse itself, which states only a general principle "
            "about virtue and wisdom."]),
        ("A chapter's own close, left untranslated", [
            "As at the end of Chapters One through Six, the Pali "
            "text here carries vaggo sattamo, &lsquo;the seventh "
            "chapter is finished&rsquo;, followed by an uddāna naming "
            "all ten monks of this chapter in sequence: Vappa, "
            "Vajjiputta, Pakkha, Vimalakoṇḍañña, Ukkhepakatavaccha, "
            "Meghiya, Ekadhammasavanīya, Ekudāniya and Channa joined "
            "into one compound, and Puṇṇa, called &lsquo;of great "
            "strength&rsquo; in this closing line. Sujato's "
            "translation leaves both untranslated, and neither "
            "appears in this page's text below."]),
    ],
    terms=[
        ("s&imacr;la",
         "&ldquo;ethical conduct&rdquo; &mdash; named &lsquo;best in "
         "this life&rsquo; in this verse's opening line."),
        ("pa&ntilde;&ntilde;av&amacr;",
         "&ldquo;one with wisdom&rdquo; &mdash; named "
         "&lsquo;supreme&rsquo;, ranked above ethical conduct alone."),
        ("s&imacr;lapa&ntilde;&ntilde;&amacr;&#7751;ato",
         "&ldquo;through virtue and wisdom&rdquo; &mdash; the combined "
         "quality this verse says brings victory."),
        ("Sun&amacr;paranta",
         "the distant region Puṇṇa asks permission to live in at MN "
         "145, described there as home to a wild and rough people."),
        ("Pu&#7751;&#7751;a",
         "this monk's own name, shared with another elder, Puṇṇa "
         "(1st), at Thag 1.4 earlier in this collection."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.70:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse call 'best in this life'?",
         "opts": [
             "Wealth",
             "Fame",
             "Physical strength",
             "Ethical conduct"],
         "correct": 3,
         "expl": "The verse's opening ranking."},
        {"q": "What does this verse call 'supreme', ranked above ethical conduct alone?",
         "opts": [
             "Wisdom",
             "Royal descent",
             "Long life",
             "Beauty"],
         "correct": 0,
         "expl": "Paññavā pana uttamo — wisdom ranked higher still."},
        {"q": "Unlike Godhika, Meghiya, and Channa earlier in this chapter, how is this Puṇṇa's identity treated by this reading guide?",
         "opts": [
             "With the same unconfirmed, cautious treatment",
             "As entirely unknown, with no comment at all",
             "As definitely a different person from any Puṇṇa elsewhere",
             "As directly confirmed by a Sujato comment naming the discourse where he next appears"],
         "correct": 3,
         "expl": "A sourced identification, not a shared-name resemblance."},
        {"q": "According to Sujato's comment, where does this Puṇṇa depart for?",
         "opts": [
             "Sāvatthī",
             "Rājagaha",
             "The distant land of Sunāparanta",
             "Kapilavatthu"],
         "correct": 2,
         "expl": "Named directly in MN 145, 'Advice to Puṇṇa'."},
        {"q": "What earlier poem in this collection features a different elder also named Puṇṇa?",
         "opts": [
             "Thag 1.4, Puṇṇa (1st), giving advice to associate only with the virtuous",
             "Thag 1.1, Subhūti's opening poem",
             "Thag 1.24, Sugandha's verse",
             "No earlier poem features a Puṇṇa"],
         "correct": 0,
         "expl": "Two different elders sharing one name within this same collection."},
        {"q": "What famous exchange does MN 145 record, according to this reading guide?",
         "opts": [
             "A dispute over monastic property",
             "The Buddha's graduated questions about Puṇṇa's equanimity toward abuse, violence, and even death",
             "A debate about cosmology",
             "A teaching on almsround etiquette"],
         "correct": 1,
         "expl": "Not included in this verse itself, which states only a general principle."},
        {"q": "What does the Pali text carry immediately after this poem, left untranslated by Sujato?",
         "opts": [
             "A new eleventh poem",
             "'Vaggo sattamo' ('the seventh chapter is finished') and an uddāna naming all ten monks of the chapter",
             "Nothing follows this poem",
             "A prose narrative"],
         "correct": 1,
         "expl": "The same untranslated colophon pattern seen at the end of Chapters One through Six."},
        {"q": "Does this page's text include that closing uddāna?",
         "opts": [
             "Yes, translated in full",
             "No — it is absent from Sujato's translation and not included here",
             "Yes, but only partially",
             "It is included as an image only"],
         "correct": 1,
         "expl": "Consistent with how this site handles untranslated structural material."},
        {"q": "How many monks' verses make up Chapter Seven in total?",
         "opts": [
             "Ten",
             "Seven",
             "Twenty",
             "One hundred and twenty"],
         "correct": 0,
         "expl": "Vappa through Puṇṇa, named in sequence in the untranslated uddāna."},
        {"q": "How many more chapters remain in the Book of the Ones after this one?",
         "opts": [
             "None — this is the final chapter",
             "Exactly one more",
             "Five more chapters",
             "Twenty more chapters"],
         "correct": 2,
         "expl": "Twelve chapters in total make up the Book of the Ones."},
    ],
    marginalia=[
        ("A confirmed name, for once", [
            "not a resemblance —",
            "a comment names him directly"
        ]),
        ("Two Puṇṇas, one collection", [
            "(1st) advised on friendship;",
            "(2nd) ranks virtue and wisdom"
        ]),
        ("A test still to come", [
            "abuse, violence, death —",
            "not written into this verse"
        ]),
        ("A seventh chapter closes", [
            "ten names, tabulated,",
            "left untranslated"
        ]),
    ],
    further=[
        '<a href="%s/thag1.70/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-145.html">MN 145 &mdash; '
        "Advice to Puṇṇa</a> &mdash; confirmed by Sujato's own comment "
        "as the discourse where this same Puṇṇa next appears.",
        '<a href="thag-1.4.html">Thag 1.4 &mdash; Pu&#7751;&#7751;a '
        "(1st)</a> &mdash; a different elder sharing this name, "
        "earlier in this collection.",
        '<a href="thag-1.69.html">Thag 1.69 &mdash; Channa</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.71 — Vacchap&amacr;la
# --------------------------------------------------------------------------- #
page(
    1, 71, "Vacchap&amacr;la", "Vacchap&amacr;la",
    meta_title="Thag 1.71 — Vacchapāla | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vacchapāla's verse, opening Chapter Eight with a teaching on "
        "the qualities that make extinguishment easy to reach — the "
        "collection's first verse to name Nibbāna outright. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; a general teaching verse "
                    "describing a type of practitioner"),
        ("Speaker", "An unnamed voice describing, in the third "
                    "person, the qualities that make extinguishment "
                    "easy to reach"),
        ("Form", "One four-line verse, a single compound description "
                 "in the instrumental case"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "compact, but dense with compound vocabulary"),
    ],
    why=(
        "Chapter Eight opens with a change of register from Chapter "
        "Seven's riddles: a straightforward teaching verse naming "
        "three qualities &mdash; subtle and fine insight, calm and "
        "skillful thought, and mature, well-cultivated ethics &mdash; "
        "that together make extinguishment &lsquo;not hard to "
        "gain&rsquo;. It is also the first verse in this collection "
        "so far to name Nibbāna itself, rather than only gesturing "
        "toward it through a synonym."),
    guide=[
        ("Three qualities, one easy outcome", [
            "The verse is built as a single compound description, in "
            "the instrumental case, of a certain kind of person: one "
            "who sees the meaning &lsquo;so very subtle and "
            "fine&rsquo;, who is &lsquo;skilled in thought and placid "
            "in manner&rsquo;, and who has &lsquo;cultivated mature "
            "ethics&rsquo;. For a person of this profile, the verse "
            "concludes, extinguishment is not hard to gain. Unlike "
            "much of the preceding chapter, this is not a "
            "first-person testimony or a riddle to be puzzled out "
            "&mdash; it is a straightforward teaching about what "
            "makes the goal reachable."]),
        ("The collection's first named Nibbāna", [
            "Across the seventy poems already covered in this "
            "collection, the goal has been named only through "
            "synonyms and cognates &mdash; &lsquo;the state that does "
            "not pass&rsquo; in the collection's own opening frame "
            "(Thag 1.1), or the participle nibbuta, "
            "&lsquo;quenched&rsquo;, used by several elders earlier "
            "in the Book of the Ones. This verse is the first to use "
            "the noun Nibbāna itself. The word choice is not treated "
            "here as doctrinally significant in itself &mdash; the "
            "earlier poems clearly meant the same goal &mdash; but it "
            "is the first plain naming of it."]),
        ("A name that echoes, cautiously", [
            "Vacchapāla's name reads literally as vaccha "
            "(&lsquo;calf&rsquo;) plus pāla (&lsquo;guardian, "
            "herder&rsquo;) &mdash; &lsquo;calf-herder&rsquo;, an "
            "occupation-flavored name. It sits alongside, but should "
            "not be folded into, the clan name Vaccha already carried "
            "by four monks earlier in this collection: Cūḷavaccha, "
            "Mahāvaccha, and Vanavaccha in Chapter Two, and "
            "Ukkhepakatavaccha in Chapter Seven. Vaccha the common "
            "noun for &lsquo;calf&rsquo; and Vaccha the gotta (clan) "
            "name are different senses of the same word, and nothing "
            "here confirms that this monk's name draws on the clan "
            "sense at all."]),
        ("An echo with the previous chapter's opening riddle", [
            "Chapter Seven opened with Vappa's verse (Thag 1.61), "
            "built entirely from four forms of passati, "
            "&lsquo;sees&rsquo;. This verse, opening Chapter Eight, is "
            "built around dassin, &lsquo;one who sees&rsquo; &mdash; a "
            "word from the same suppletive verb &lsquo;to see&rsquo; "
            "in Pali. The two chapter-openers otherwise share no "
            "content, but both reach for the same root at the start "
            "of a new chapter."]),
    ],
    terms=[
        ("dassin",
         "&ldquo;one who sees&rdquo; &mdash; from the same suppletive "
         "verb as passati, the word Vappa's chapter-opening riddle "
         "(Thag 1.61) was built from."),
        ("matikusala",
         "&ldquo;skilled in thought&rdquo; or &ldquo;skilled in "
         "judgment&rdquo; &mdash; one of the three qualities this "
         "verse names."),
        ("nivātavutti",
         "&ldquo;of placid manner&rdquo;, literally &ldquo;living "
         "without wind&rdquo; &mdash; a calm, undisturbed way of "
         "conducting oneself."),
        ("saṁsevitavuddhasīlin",
         "&ldquo;one who has cultivated mature ethics&rdquo; &mdash; "
         "the third of the verse's three qualities."),
        ("Nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; the first time this "
         "word itself, rather than the cognate participle nibbuta, "
         "&lsquo;quenched&rsquo;, appears in this collection."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.71:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three qualities does this verse say make extinguishment easy to reach?",
         "opts": [
             "Generosity, patience, and courage",
             "Faith, energy, and mindfulness",
             "Subtle insight, calm skillful thought, and mature ethics",
             "Wealth, health, and long life"],
         "correct": 2,
         "expl": "The verse's single compound description, in the instrumental case."},
        {"q": "What does this verse name for the first time in this collection?",
         "opts": [
             "The word Nibbāna itself, for the first time in this collection",
             "The Buddha, for the first time",
             "A specific meditation technique",
             "A specific monastery"],
         "correct": 0,
         "expl": "Earlier poems only gestured toward the goal through synonyms."},
        {"q": "What does 'dassin' mean?",
         "opts": [
             "one who hears",
             "one who sees",
             "one who speaks",
             "one who teaches"],
         "correct": 1,
         "expl": "From the same suppletive verb as passati."},
        {"q": "What does 'nivātavutti' literally describe?",
         "opts": [
             "living in a windy place",
             "living without a home",
             "living without food",
             "living without wind, i.e. calm in manner"],
         "correct": 3,
         "expl": "A calm, undisturbed way of conducting oneself."},
        {"q": "How does this poem's grammatical voice differ from much of Chapter Seven?",
         "opts": [
             "It is a third-person general teaching, not first-person testimony or riddle",
             "It is written entirely in dialogue",
             "It is the Buddha's own words",
             "It has no grammatical person at all"],
         "correct": 0,
         "expl": "A straightforward description of a type of person, not self-testimony."},
        {"q": "What clan name might Vacchapāla's name superficially resemble, without confirmed connection?",
         "opts": [
             "Koṇḍañña, the clan name of one of the first five ascetics",
             "Gotama, the Buddha's own clan name",
             "Vaccha, the clan name shared by four monks earlier in the collection",
             "Sākiya, the Buddha's own clan name"],
         "correct": 2,
         "expl": "This reading guide does not assert the connection, only notes the shared word."},
        {"q": "Literally, what does the name Vacchapāla mean?",
         "opts": [
             "Mountain-dweller",
             "Calf-herder",
             "Forest-wanderer",
             "River-crosser"],
         "correct": 1,
         "expl": "Vaccha ('calf') plus pāla ('guardian, herder')."},
        {"q": "What earlier chapter-opening poem does this verse echo through a shared verbal root?",
         "opts": [
             "Thag 1.1 Subhūti, the collection's frame verse",
             "Thag 1.51 Godhika",
             "Thag 1.41 Sirivaḍḍha",
             "Thag 1.61 Vappa, built from the verb 'sees'"],
         "correct": 3,
         "expl": "Both dassin and passati derive from the same suppletive verb."},
        {"q": "How had the goal been referred to earlier in this collection, before this verse?",
         "opts": [
             "Only through synonyms and cognates, such as 'quenched' or 'the state that does not pass'",
             "Never referred to at all",
             "Only in Sanskrit",
             "Only by the Buddha himself"],
         "correct": 0,
         "expl": "This verse is the first to name Nibbāna outright."},
        {"q": "What chapter does this poem open?",
         "opts": [
             "Chapter Seven",
             "Chapter One",
             "Chapter Eight",
             "The Great Book"],
         "correct": 2,
         "expl": "The first of ten poems in the new chapter."},
    ],
    marginalia=[
        ("Nibbāna, named at last", [
            "not quenched, not calm —",
            "the word itself, spoken"
        ]),
        ("Three qualities, one gate", [
            "insight, calm thought, ethics —",
            "the gate swings open"
        ]),
        ("A calf-herder's name", [
            "Vaccha, or just a calf —",
            "the text does not say"
        ]),
        ("Two chapters, one root", [
            "Vappa saw; this one sees —",
            "the same verb, twice"
        ]),
    ],
    further=[
        '<a href="%s/thag1.71/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.70.html">Thag 1.70 &mdash; Pu&#7751;&#7751;a '
        "(2nd)</a> &mdash; the poem immediately before this one, "
        "closing Chapter Seven.",
        '<a href="thag-1.61.html">Thag 1.61 &mdash; Vappa</a> '
        "&mdash; Chapter Seven's opening riddle, built from the same "
        "verbal root as this poem's dassin.",
        '<a href="thag-1.72.html">Thag 1.72 &mdash; &Amacr;tuma</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.72 — &Amacr;tuma
# --------------------------------------------------------------------------- #
page(
    1, 72, "&Amacr;tuma", "&Amacr;tuma",
    meta_title="Thag 1.72 — Ātuma | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ātuma's verse, comparing an arranged marriage to a bamboo "
        "shoot grown too woody to pull free — this collection's first "
        "verse to name a wife. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 2 of 10",
    glance=[
        ("Setting", "A moment of departure: asking for release from "
                    "an arranged marriage"),
        ("Speaker", "Ātuma, in the first person"),
        ("Form", "One four-line verse, built on a single simile"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one clear image"),
    ],
    why=(
        "Where the chapter's opening poem was an impersonal teaching, "
        "this one is sharply personal: Ātuma compares his marriage "
        "&mdash; arranged for him, not chosen &mdash; to a young "
        "bamboo shoot that was easy to pull up when small but is now "
        "&lsquo;hard to extract&rsquo; once grown woody and "
        "branching. He asks for release. It is the first verse "
        "anywhere in this collection so far to name a wife at all."),
    guide=[
        ("A bamboo shoot, grown too woody to pull", [
            "The verse's entire force rests on one image: a bamboo "
            "shoot (kaḷīra) is simple to pull up while young, but "
            "once it has grown tall and put out side-branches "
            "(pasākhajāto), it becomes &lsquo;hard to extract&rsquo; "
            "(dunnikkhamo). Ātuma applies this directly to his own "
            "marriage &mdash; not a marriage he chose, but one "
            "&lsquo;arranged for him&rsquo; (bhariyāya ānitāya) "
            "&mdash; which has grown just as entangling."]),
        ("The collection's first named wife", [
            "Across the seventy-one poems already covered in this "
            "collection, no verse has named a wife until this one. "
            "Domestic renunciation has appeared before in general "
            "terms &mdash; leaving household life, giving up sensual "
            "pleasures &mdash; but this is the first time the "
            "specific relationship being left is spelled out as a "
            "marriage, and an arranged one at that."]),
        ("A request, spoken after the fact", [
            "The verse's closing line is grammatically unusual: "
            "&lsquo;give me permission&rsquo; (anumaññaṁ maṁ) sits "
            "beside &lsquo;now I've gone forth&rsquo; (pabbajitomhi), "
            "a present-perfect form describing an already-completed "
            "act. Read plainly, Ātuma is asking for consent to "
            "something he has, in the same breath, already done. "
            "This reading guide does not resolve who the request is "
            "addressed to &mdash; the verse itself does not say "
            "&mdash; only notes the unusual timing: permission sought "
            "at, or just after, the moment of departure, not before "
            "it."]),
        ("Two opening poems, two registers", [
            "Chapter Eight opens by juxtaposing genres: Vacchapāla's "
            "verse (Thag 1.71) is an impersonal teaching about a type "
            "of person, entirely free of narrative detail; Ātuma's "
            "verse, immediately after, is the opposite &mdash; a "
            "single concrete image drawn from one man's own "
            "domestic life. The chapter's first two poems could "
            "hardly be more different in kind."]),
    ],
    terms=[
        ("kaḷīra",
         "&ldquo;bamboo shoot&rdquo; &mdash; the verse's central "
         "image, easy to pull when young."),
        ("dunnikkhama",
         "&ldquo;hard to extract, hard to pull out&rdquo; &mdash; "
         "describing the bamboo once grown woody and branching."),
        ("pasākhajāta",
         "&ldquo;having put out side-branches&rdquo; &mdash; the "
         "stage at which the shoot becomes hard to remove."),
        ("bhariyā",
         "&ldquo;wife&rdquo; &mdash; named here for the first time "
         "in this collection."),
        ("pabbajita",
         "&ldquo;one who has gone forth&rdquo;, i.e. ordained &mdash; "
         "here in a present-perfect form describing an act already "
         "completed."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.72:1.1-1.4"),
    ],
    quiz=[
        {"q": "What image does this verse use for the speaker's marriage?",
         "opts": [
             "A young bamboo shoot, easy to pull when small but hard to extract once grown woody",
             "A river that cannot be crossed",
             "A mountain that cannot be climbed",
             "A fire that cannot be put out"],
         "correct": 0,
         "expl": "The verse's single governing simile."},
        {"q": "What is named for the first time anywhere in this collection in this verse?",
         "opts": [
             "A monastery",
             "A king",
             "A river",
             "A wife"],
         "correct": 3,
         "expl": "No prior verse in the collection has named a wife."},
        {"q": "According to the verse, was this marriage chosen by the speaker?",
         "opts": [
             "No, it was arranged for him",
             "Yes, he chose it freely",
             "The verse doesn't mention a marriage at all",
             "Yes, but he later regretted the choice"],
         "correct": 0,
         "expl": "Bhariyāya ānitāya, 'the wife who was arranged/brought for me'."},
        {"q": "What does 'dunnikkhama' mean?",
         "opts": [
             "Easy to plant",
             "Quick to grow",
             "Hard to extract, hard to pull out",
             "Pleasant to look at"],
         "correct": 2,
         "expl": "Describing the bamboo once it has grown branches."},
        {"q": "What grammatical oddity does this reading guide point out in the verse's closing line?",
         "opts": [
             "It uses no verbs at all",
             "It is written entirely in the future tense",
             "It repeats the same word four times",
             "It asks for permission while, in the same breath, already describing the going-forth as completed"],
         "correct": 3,
         "expl": "Anumaññaṁ maṁ ('give me permission') beside pabbajitomhi ('I have gone forth')."},
        {"q": "Does this reading guide identify who Ātuma's request for permission is addressed to?",
         "opts": [
             "Yes, definitively his wife",
             "No — the verse itself does not say, and this reading guide does not resolve it",
             "Yes, definitively the Buddha",
             "Yes, definitively his parents"],
         "correct": 1,
         "expl": "The addressee is left open by the text."},
        {"q": "How does this poem's register compare to Thag 1.71, the poem immediately before it?",
         "opts": [
             "1.71 is an impersonal teaching; 1.72 is a personal, concrete domestic image",
             "Identical in every way",
             "Both are equally impersonal teachings",
             "Both are riddles with no clear meaning"],
         "correct": 0,
         "expl": "The chapter's first two poems contrast sharply in kind."},
        {"q": "What does 'pasākhajāta' describe?",
         "opts": [
             "A river in flood",
             "A monk's robe",
             "A shoot that has put out side-branches",
             "A newly built hut"],
         "correct": 2,
         "expl": "The stage of growth at which the bamboo becomes hard to remove."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "The tenth and final poem of Chapter Eight",
             "The opening poem of the whole collection",
             "A poem in the Book of the Twos",
             "The second poem of Chapter Eight"],
         "correct": 3,
         "expl": "Immediately after Vacchapāla's verse, which opens the chapter."},
        {"q": "What kind of verse is this, according to this reading guide?",
         "opts": [
             "A numeric doctrinal formula",
             "A single concrete simile applied to the speaker's own domestic life",
             "A dialogue between two named speakers",
             "A collective declaration by many monks at once"],
         "correct": 1,
         "expl": "One image, drawn from lived experience, not an abstract teaching."},
    ],
    marginalia=[
        ("A shoot, once easy to pull", [
            "small and green —",
            "now woody, branching"
        ]),
        ("A wife, named at last", [
            "arranged, not chosen —",
            "the collection's first"
        ]),
        ("Permission, asked too late", [
            "already gone forth —",
            "still asking leave"
        ]),
        ("Two poems, two worlds", [
            "one teaches in the abstract;",
            "one speaks from a house"
        ]),
    ],
    further=[
        '<a href="%s/thag1.72/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.71.html">Thag 1.71 &mdash; Vacchap&amacr;la</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.73.html">Thag 1.73 &mdash; M&amacr;&#7751;ava</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.73 — M&amacr;&#7751;ava
# --------------------------------------------------------------------------- #
page(
    1, 73, "M&amacr;&#7751;ava", "M&amacr;&#7751;ava",
    meta_title="Thag 1.73 — Māṇava | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Māṇava's verse, a plain retrospective account of going forth "
        "after seeing old age, sickness, and death. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 3 of 10",
    glance=[
        ("Setting", "A retrospective account of what triggered the "
                    "speaker's going forth"),
        ("Speaker", "Māṇava, in the first person, looking back on a "
                    "completed decision"),
        ("Form", "One four-line verse, a single plain narrative"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain, direct vocabulary throughout"),
    ],
    why=(
        "Māṇava gives the plainest possible account of a monastic "
        "conversion: seeing an old person, someone sick, and a "
        "corpse, he went forth, giving up sensual pleasure. No "
        "riddle, no dialogue, no simile carries the weight here "
        "&mdash; only the bare sequence of sights and the decision "
        "that followed."),
    guide=[
        ("Three sights, without a fourth", [
            "The verse names exactly three sights: an old person, "
            "someone &lsquo;suffering from disease&rsquo;, and "
            "&lsquo;a corpse come to the end of life&rsquo;. Readers "
            "familiar with the traditional story of the Buddha's own "
            "renunciation &mdash; encountering old age, sickness, "
            "death, and finally a renunciant, before leaving the "
            "palace &mdash; may recognize the first three of those "
            "four sights here. This reading guide does not assert "
            "that the verse itself alludes to that story; it notes "
            "only the well-known parallel in outline, as background, "
            "not as a claim this text makes."]),
        ("A name that is also a common word", [
            "Māṇava is not, on its face, a distinctive personal name "
            "&mdash; the word literally means &lsquo;young man&rsquo; "
            "or &lsquo;young brahmin student&rsquo;, and is used "
            "throughout the wider canon as an ordinary common noun as "
            "often as a proper name. Whether this particular elder "
            "had another name and was known by this generic title, or "
            "whether Māṇava was simply his name, is not something "
            "this verse or this reading guide can settle."]),
        ("A settled retrospective, not a live plea", [
            "The verse's closing verb, pabbajiṁ (&lsquo;I went "
            "forth&rsquo;), is a simple past form describing a "
            "completed act, told from a position of settled "
            "hindsight. This is a notably calmer grammar than the "
            "poem immediately before it, Thag 1.72, where Ātuma's "
            "verse mixed an already-completed going-forth with a "
            "present-tense request for permission. Side by side, the "
            "two verses show two different grammatical postures "
            "toward the same kind of event."]),
    ],
    terms=[
        ("jiṇṇa",
         "&ldquo;old, aged&rdquo; &mdash; the first of the three "
         "sights named in this verse."),
        ("byādhita",
         "&ldquo;suffering from disease, sick&rdquo; &mdash; the "
         "second of the three sights."),
        ("mata",
         "&ldquo;dead&rdquo;, here as &lsquo;a corpse come to the end "
         "of life&rsquo; &mdash; the third of the three sights."),
        ("pabbajiṁ",
         "&ldquo;I went forth&rdquo; &mdash; a simple past (aorist) "
         "form, describing the act as already completed."),
        ("Māṇava",
         "&ldquo;young man&rdquo; or &ldquo;young brahmin "
         "student&rdquo; &mdash; a generic term used across the wider "
         "canon as often as a proper name."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.73:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three things does the speaker say he saw that led him to go forth?",
         "opts": [
             "An old person, someone sick, and a corpse",
             "A king, a beggar, and a monk",
             "A fire, a flood, and a storm",
             "A teacher, a student, and a stranger"],
         "correct": 0,
         "expl": "The verse's plain, three-part list of sights."},
        {"q": "What does this verse's final line explicitly give up?",
         "opts": [
             "His family's wealth",
             "The pleasures of the senses",
             "His name and clan",
             "His robes"],
         "correct": 1,
         "expl": "Pahāya kāmāni manoramāni, 'giving up the pleasures of the senses'."},
        {"q": "What well-known story does this reading guide note as background, without asserting the verse alludes to it?",
         "opts": [
             "The story of the five ascetics at Isipatana",
             "The story of Māra's daughters",
             "The traditional four sights of the Buddha's own renunciation story",
             "The story of the bodhi tree"],
         "correct": 2,
         "expl": "Old age, sickness, death, and a renunciant — the traditional four."},
        {"q": "How many of the traditional 'four sights' does this verse's account include?",
         "opts": [
             "All four",
             "Only one",
             "Two",
             "Three — old age, sickness, and death, not the fourth, a renunciant"],
         "correct": 3,
         "expl": "The verse stops short of the fourth sight in the traditional story."},
        {"q": "What does the name Māṇava literally mean?",
         "opts": [
             "A young man, or young brahmin student",
             "A guardian of calves",
             "One who has gone forth",
             "A dweller in a hut"],
         "correct": 0,
         "expl": "A generic term used across the wider canon."},
        {"q": "Is 'Māṇava' treated in this reading guide as a distinctive personal name or a generic term?",
         "opts": [
             "A definitively distinctive personal name",
             "A generic term, used as often as a proper name across the wider canon",
             "A title reserved only for kings",
             "A term found nowhere else in the canon"],
         "correct": 1,
         "expl": "This reading guide does not settle whether it was his only name."},
        {"q": "What Pali verb form does the verse use for 'I went forth'?",
         "opts": [
             "A future tense form",
             "An imperative form",
             "Pabbajiṁ, a simple past (aorist) form describing a completed act",
             "A present-tense form"],
         "correct": 2,
         "expl": "Told from a position of settled hindsight."},
        {"q": "How does this poem's grammar differ from Thag 1.72, the poem before it?",
         "opts": [
             "They are grammatically identical",
             "1.73 is written entirely in dialogue",
             "1.72 uses no verbs at all",
             "1.72 mixes a completed act with a present request; 1.73 is told simply in the past, from settled hindsight"],
         "correct": 3,
         "expl": "Two different grammatical postures toward a similar kind of event."},
        {"q": "What does 'kāmāni manoramāni' mean?",
         "opts": [
             "Delightful sensory pleasures",
             "Painful memories",
             "Ancestral duties",
             "Monastic robes"],
         "correct": 0,
         "expl": "What the speaker gives up at the close of the verse."},
        {"q": "What kind of verse is this, according to this reading guide?",
         "opts": [
             "A riddle built on wordplay",
             "A plain, retrospective first-person account, without riddle or dialogue",
             "A dialogue between two named speakers",
             "A numeric doctrinal formula"],
         "correct": 1,
         "expl": "The bare sequence of sights and the decision that followed."},
    ],
    marginalia=[
        ("Three sights, one decision", [
            "old age, sickness, death —",
            "and then, the going forth"
        ]),
        ("A name, or just a word", [
            "young man, young student —",
            "the text does not clarify"
        ]),
        ("Hindsight, calmly told", [
            "no plea, no present tense —",
            "a settled 'I went forth'"
        ]),
        ("What was given up", [
            "delightful, sensory —",
            "set down, and left behind"
        ]),
    ],
    further=[
        '<a href="%s/thag1.73/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.72.html">Thag 1.72 &mdash; &Amacr;tuma</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.74.html">Thag 1.74 &mdash; Suy&amacr;mana</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.74 — Suy&amacr;mana
# --------------------------------------------------------------------------- #
page(
    1, 74, "Suy&amacr;mana", "Suy&amacr;mana",
    meta_title="Thag 1.74 — Suyāmana | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Suyāmana's verse, a compact list of the five hindrances "
        "declared absent in a monk — this collection's first explicit "
        "enumeration of them. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative setting; a compact doctrinal "
                    "enumeration"),
        ("Speaker", "An unnamed voice describing, in terms of "
                    "&lsquo;a monk&rsquo; rather than &lsquo;I&rsquo;, "
                    "what is absent from him"),
        ("Form", "One four-line verse, listing five qualities as "
                 "wholly absent"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary naming a well-known list"),
    ],
    why=(
        "Chapter Eight's fourth poem returns to the teaching register "
        "of its opener: a compact list of five qualities &mdash; "
        "sensual desire, ill will, dullness and drowsiness, "
        "restlessness, and doubt &mdash; declared &lsquo;not found in "
        "a monk at all&rsquo;. It is the collection's first explicit "
        "enumeration of the five hindrances, a standard doctrinal "
        "category well known throughout the wider canon."),
    guide=[
        ("The five hindrances, named in one breath", [
            "The verse lists, in order, kāmacchanda "
            "(&lsquo;sensual desire&rsquo;), byāpāda (&lsquo;ill "
            "will&rsquo;), thīnamiddha (&lsquo;dullness and "
            "drowsiness&rsquo;, treated as one combined item), "
            "uddhacca (&lsquo;restlessness&rsquo;), and vicikicchā "
            "(&lsquo;doubt&rsquo;). Together these are the five "
            "hindrances (pañca nīvaraṇāni), a standard and "
            "well-known category throughout the wider canon &mdash; "
            "broadly comparable, as a piece of basic doctrinal "
            "background, to the numeric formula Thag 1.15 "
            "(Kuṇḍadhāna) relied on without unpacking its terms "
            "either."]),
        ("A fourth item, alone", [
            "In its most common canonical form, the fourth hindrance "
            "is a compound, uddhacca-kukkucca (&lsquo;restlessness "
            "and remorse&rsquo;). This verse names only uddhaccaṁ, "
            "&lsquo;restlessness&rsquo;, without its usual paired "
            "companion. Read together with the four other named "
            "items, the list still totals the traditional five "
            "hindrances; this is most likely a matter of verse meter "
            "rather than a different accounting of the standard set, "
            "though the verse itself gives no comment on the "
            "omission."]),
        ("A monk, not an 'I'", [
            "The verse's grammar speaks of &lsquo;a monk&rsquo; "
            "(bhikkhuno) rather than using the first person. This "
            "could describe Suyāmana himself, spoken of indirectly, "
            "or a general ideal that any monk might meet; the verse "
            "does not distinguish between the two, and this reading "
            "guide does not resolve it. Either way, it shares its "
            "third-person, teaching-like register with Thag 1.71, "
            "which opened this chapter &mdash; the two general "
            "teaching-poems bracketing the chapter's more personal "
            "and narrative verses so far."]),
    ],
    terms=[
        ("kāmacchanda",
         "&ldquo;sensual desire&rdquo; &mdash; the first of the five "
         "hindrances named in this verse."),
        ("byāpāda",
         "&ldquo;ill will&rdquo; &mdash; the second hindrance."),
        ("thīnamiddha",
         "&ldquo;dullness and drowsiness&rdquo; &mdash; the third "
         "hindrance, treated as one combined item."),
        ("uddhacca",
         "&ldquo;restlessness&rdquo; &mdash; named alone here, "
         "without its usual paired companion kukkucca "
         "(&lsquo;remorse&rsquo;)."),
        ("vicikicchā",
         "&ldquo;doubt&rdquo; &mdash; the fifth and final hindrance "
         "named in this verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.74:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five qualities does this verse list as absent?",
         "opts": [
             "The five faculties",
             "The five aggregates",
             "The five hindrances: sensual desire, ill will, dullness and drowsiness, restlessness, and doubt",
             "The five precepts"],
         "correct": 2,
         "expl": "Pañca nīvaraṇāni, a standard doctrinal category."},
        {"q": "What does 'thīnamiddha' name?",
         "opts": [
             "Sensual desire",
             "Ill will",
             "Doubt",
             "Dullness and drowsiness, treated as one combined item"],
         "correct": 3,
         "expl": "The third of the five hindrances in this verse's list."},
        {"q": "Does this verse speak in the first person ('I') or of 'a monk' in general?",
         "opts": [
             "Of 'a monk' (bhikkhuno), not using the first person",
             "Entirely in the first person",
             "In direct address to a named listener",
             "In the voice of the Buddha"],
         "correct": 0,
         "expl": "The verse's grammar; this reading guide does not resolve whether it describes the speaker himself."},
        {"q": "What does this reading guide note about the verse's fourth item, 'uddhaccaṁ'?",
         "opts": [
             "It appears twice in the verse",
             "It stands alone, without its usual paired companion kukkucca — most likely for reasons of meter",
             "It is not one of the five hindrances at all",
             "It replaces vicikicchā entirely"],
         "correct": 1,
         "expl": "The list still totals the traditional five hindrances."},
        {"q": "What is this verse's significance for the collection so far?",
         "opts": [
             "It names the Buddha for the first time",
             "It is the shortest verse in the collection",
             "It is the collection's first explicit enumeration of the five hindrances",
             "It is the only verse addressed to a king"],
         "correct": 2,
         "expl": "No prior poem in the collection has listed this standard set."},
        {"q": "What does 'vicikicchā' mean?",
         "opts": [
             "Ill will",
             "Sensual desire",
             "Restlessness",
             "Doubt"],
         "correct": 3,
         "expl": "The fifth hindrance named in the verse."},
        {"q": "What does 'byāpāda' mean?",
         "opts": [
             "Ill will",
             "Dullness",
             "Doubt",
             "Restlessness"],
         "correct": 0,
         "expl": "The second of the five hindrances in this verse's list."},
        {"q": "How does this poem's register compare to Thag 1.72 and Thag 1.73, the two poems before it?",
         "opts": [
             "All three are equally personal and narrative",
             "This one is a general teaching, unlike the personal, narrative register of the two before it",
             "All three are riddles",
             "This one is the only one written in dialogue"],
         "correct": 1,
         "expl": "It shares its register instead with Thag 1.71, the chapter's opener."},
        {"q": "What comparable earlier poem in this collection uses a similarly unglossed doctrinal list?",
         "opts": [
             "Thag 1.15 Kuṇḍadhāna",
             "Thag 1.61 Vappa",
             "Thag 1.51 Godhika",
             "Thag 1.41 Sirivaḍḍha"],
         "correct": 0,
         "expl": "Both rely on standard categories without unpacking them within the verse."},
        {"q": "What does 'sabbasova na vijjatī' mean?",
         "opts": [
             "All of it is found in abundance",
             "Some of it remains",
             "It cannot be known",
             "None of it is found at all"],
         "correct": 3,
         "expl": "The verse's closing declaration."},
    ],
    marginalia=[
        ("Five, named at once", [
            "desire, ill will, doubt —",
            "dullness, restlessness too"
        ]),
        ("A pair, split apart", [
            "restlessness alone —",
            "remorse left unnamed"
        ]),
        ("A monk, not an 'I'", [
            "spoken at a distance —",
            "himself, or any monk"
        ]),
        ("Teaching, not testimony", [
            "no story, no riddle —",
            "only what is absent"
        ]),
    ],
    further=[
        '<a href="%s/thag1.74/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.73.html">Thag 1.73 &mdash; M&amacr;&#7751;ava</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.71.html">Thag 1.71 &mdash; Vacchap&amacr;la</a> '
        "&mdash; the chapter's opener, sharing this poem's general, "
        "third-person teaching register.",
        '<a href="thag-1.15.html">Thag 1.15 &mdash; Ku&#7751;&#7693;adh&amacr;na</a> '
        "&mdash; an earlier poem relying on an unglossed numeric "
        "doctrinal formula, the same way this one does.",
        '<a href="thag-1.75.html">Thag 1.75 &mdash; Sus&amacr;rada</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.75 — Sus&amacr;rada
# --------------------------------------------------------------------------- #
page(
    1, 75, "Sus&amacr;rada", "Sus&amacr;rada",
    meta_title="Thag 1.75 — Susārada | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Susārada's verse on the value of meeting good people, "
        "translated with the same phrase as this collection's own "
        "opening frame, though the underlying Pali differs. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a general teaching on the "
                    "value of good company"),
        ("Speaker", "An unnamed voice stating a general principle"),
        ("Form", "One four-line verse, building to a concluding "
                 "maxim"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a proverb-like structure"),
    ],
    why=(
        "This verse states a simple chain: seeing those who have "
        "&lsquo;practiced well&rsquo; cuts off doubt and grows "
        "intelligence &mdash; &lsquo;even a fool grows wise&rsquo; "
        "&mdash; and concludes that meeting good people is therefore "
        "good. Sujato's translation renders its opening phrase with "
        "the same English wording used for this collection's own "
        "opening frame in Thag 1.1, though the underlying Pali is a "
        "different word."),
    guide=[
        ("A chain from seeing to wisdom", [
            "The verse moves in three steps: seeing those who have "
            "practiced well (suvihitāna dassanaṁ) is good; that "
            "seeing cuts off doubt and grows intelligence; and this "
            "is powerful enough that &lsquo;even a fool grows "
            "wise&rsquo;. The closing line draws the general "
            "conclusion &mdash; meeting good people (sataṁ samāgamo) "
            "is good &mdash; making this one of the collection's "
            "clearest single-verse statements of a broader theme "
            "found throughout the wider canon: the value of "
            "association with virtuous companions."]),
        ("The same English phrase, a different Pali word", [
            "This verse's opening &mdash; &lsquo;good is the sight of "
            "those who've practiced well&rsquo; &mdash; is translated "
            "with the same phrase, &lsquo;practiced well&rsquo;, that "
            "Sujato uses for this collection's own opening frame in "
            "Thag 1.1 (&lsquo;hear now from those who've practiced "
            "well&rsquo;). But the underlying Pali differs: Thag 1.1 "
            "uses bhāvitatta (&lsquo;developed in oneself&rsquo;), "
            "while this verse uses suvihita (&lsquo;well disposed, "
            "well ordered&rsquo;). The echo exists at the level of "
            "Sujato's translation choice, not as a repetition in the "
            "Pali text itself &mdash; a distinction worth keeping "
            "clear rather than treating the two verses as sharing a "
            "phrase in the original."]),
        ("A third verse reaching for 'seeing'", [
            "This verse's dassanaṁ (&lsquo;sight, seeing&rsquo;) "
            "shares its root with dassin in Thag 1.71, which opened "
            "this chapter, and with passati in Thag 1.61, which "
            "opened the previous one. &lsquo;To see&rsquo; is common "
            "vocabulary throughout the canon, so this alone does not "
            "suggest a deliberate design across these poems &mdash; "
            "but it is the third time within five poems that this "
            "particular root has surfaced."]),
    ],
    terms=[
        ("suvihita",
         "&ldquo;well disposed, well practiced&rdquo; &mdash; "
         "translated with the same English phrase as Thag 1.1's "
         "bhāvitatta, though the two Pali words differ."),
        ("dassana",
         "&ldquo;sight, seeing&rdquo; &mdash; from the same root as "
         "dassin (Thag 1.71) and passati (Thag 1.61)."),
        ("kaṅkhā",
         "&ldquo;doubt&rdquo; &mdash; what this verse says is "
         "&lsquo;cut off&rsquo; by seeing good people."),
        ("paṇḍita",
         "&ldquo;wise&rdquo; &mdash; what even a fool (bāla) is said "
         "to become."),
        ("sataṁ samāgama",
         "&ldquo;meeting of good people&rdquo; &mdash; the verse's "
         "concluding maxim."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.75:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three steps does this verse's chain of reasoning follow?",
         "opts": [
             "Seeing good people cuts off doubt, grows intelligence, and makes meeting them worthwhile",
             "Giving alms, keeping precepts, and meditating",
             "Old age, sickness, and death",
             "Ordination, study, and teaching"],
         "correct": 0,
         "expl": "The verse's own three-step progression."},
        {"q": "What phrase does Sujato's translation of this verse's opening share with Thag 1.1's opening frame?",
         "opts": [
             "'Practiced well'",
             "'The state that does not pass'",
             "'Roofed and pleasant'",
             "'Mind serene and freed'"],
         "correct": 0,
         "expl": "Both are translated with this English phrase."},
        {"q": "Does this verse's Pali word for 'practiced well' match Thag 1.1's exactly?",
         "opts": [
             "Yes, both use the identical Pali word bhāvitatta",
             "No — this verse uses suvihita, while Thag 1.1 uses bhāvitatta; the echo is only in Sujato's English translation",
             "Yes, both use the identical Pali word suvihita",
             "The comparison cannot be made because Thag 1.1 has no Pali text"],
         "correct": 1,
         "expl": "A translation-level echo, not a textual repetition in the Pali."},
        {"q": "What does 'dassana' mean?",
         "opts": [
             "Hearing",
             "Speaking",
             "Sight, seeing",
             "Touching"],
         "correct": 2,
         "expl": "Sharing its root with dassin (Thag 1.71) and passati (Thag 1.61)."},
        {"q": "According to this reading guide, does the recurrence of 'seeing'-rooted words across three poems suggest a deliberate design?",
         "opts": [
             "Yes, definitively",
             "This reading guide notes it without claiming a deliberate design, since 'to see' is common vocabulary",
             "No, the word never recurs",
             "Yes, but only in the Northern parallel tradition"],
         "correct": 1,
         "expl": "A cautious, non-committal framing of the observation."},
        {"q": "What does 'kaṅkhā' mean?",
         "opts": [
             "Wisdom",
             "Faith",
             "Fear",
             "Doubt"],
         "correct": 3,
         "expl": "What the verse says is cut off by seeing good people."},
        {"q": "According to the verse, what happens even to a fool who meets good people?",
         "opts": [
             "Nothing changes",
             "He becomes wealthy",
             "He grows wise",
             "He becomes a teacher"],
         "correct": 2,
         "expl": "Bālampi karonti paṇḍitaṁ, 'even a fool grows wise'."},
        {"q": "What is the verse's concluding maxim?",
         "opts": [
             "It is good to meet good people",
             "It is good to live alone",
             "It is good to fast",
             "It is good to travel widely"],
         "correct": 0,
         "expl": "Tasmā sādhu sataṁ samāgamo, the verse's final line."},
        {"q": "What broader canonical theme does this verse's maxim connect to, according to this reading guide?",
         "opts": [
             "The theory of the four elements",
             "The rules of monastic discipline",
             "The geography of ancient India",
             "The value of association with virtuous companions, a theme found throughout the wider canon"],
         "correct": 3,
         "expl": "A well-known broader theme, of which this verse is a compact statement."},
        {"q": "Where does this poem fall in Chapter Eight?",
         "opts": [
             "The opening poem",
             "The final poem",
             "The fifth poem",
             "The second poem"],
         "correct": 2,
         "expl": "Midway through the chapter's ten poems."},
    ],
    marginalia=[
        ("A chain, three links long", [
            "seeing, then doubt cut —",
            "even a fool grows wise"
        ]),
        ("Practiced well, twice over", [
            "one word for two Pali roots —",
            "the echo is in English"
        ]),
        ("Seeing, a third time", [
            "passati, dassin, dassana —",
            "one root, three poems"
        ]),
        ("Good company, the maxim", [
            "meeting the virtuous —",
            "reason enough, alone"
        ]),
    ],
    further=[
        '<a href="%s/thag1.75/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.1.html">Thag 1.1 &mdash; Subh&umacr;ti</a> '
        "&mdash; the collection's own opening frame, translated with "
        "the same English phrase, 'practiced well', though the "
        "underlying Pali differs.",
        '<a href="thag-1.74.html">Thag 1.74 &mdash; Suy&amacr;mana</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.76.html">Thag 1.76 &mdash; Piya&ntilde;jaha</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.76 — Piya&ntilde;jaha
# --------------------------------------------------------------------------- #
page(
    1, 76, "Piya&ntilde;jaha", "Piya&ntilde;jaha",
    meta_title="Thag 1.76 — Piyañjaha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Piyañjaha's verse, four paired inversions counseling a "
        "deliberate departure from the crowd, spoken by a monk whose "
        "own name means 'one who has given up what is dear'. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting; four paired, paradoxical "
                    "instructions"),
        ("Speaker", "An unspecified voice, in a form this reading "
                    "guide does not resolve as either command or "
                    "resolve"),
        ("Form", "One four-line verse, built entirely from four "
                 "paired contrasts"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "compact, but genuinely puzzle-like"),
    ],
    why=(
        "Piyañjaha's verse is built entirely from four paired "
        "inversions: settle down when others rise, rise when others "
        "settle; remain when others depart; take no delight when "
        "others delight. Read together, they describe a habit of "
        "deliberately taking the opposite position from whatever the "
        "crowd is doing &mdash; and the verse never explains why."),
    guide=[
        ("Four deliberate inversions", [
            "Each line pairs a locative plural (&lsquo;among those "
            "who...&rsquo;) with a contrasting action: settle when "
            "others spring up, spring up when others settle; dwell "
            "when others have left their dwelling; take no delight "
            "when others delight. No narrative frames these four "
            "lines, and no simile explains them &mdash; the pattern "
            "itself, repeated four times, is the entire content of "
            "the verse."]),
        ("A name that matches its own message", [
            "Piyañjaha's name reads literally as piya "
            "(&lsquo;dear, pleasant&rsquo;) plus jaha (&lsquo;one who "
            "has given up, abandoned&rsquo;, from jahati) &mdash; "
            "&lsquo;one who has given up what is dear&rsquo;. This "
            "pairs naturally with the verse's fourth line in "
            "particular, declining delight when others delight, "
            "though the name matches the verse's overall theme rather "
            "than quoting any of its specific wording."]),
        ("Command, resolve, or plain description?", [
            "This reading guide does not settle whether the verse's "
            "four lines are meant as direct instruction to a "
            "listener, a private resolve spoken to oneself, or a "
            "plain description of how this monk already lives. "
            "Sujato's English renders them as direct counsel "
            "(&lsquo;settle down... don't delight...&rsquo;), but the "
            "verse supplies no addressee and no first-person marker "
            "to confirm who, exactly, is being told to act this way."]),
        ("A third riddle-like verse in close range", [
            "This poem joins a small cluster of compact, riddle-like "
            "verses that give no narrative or explanation for their "
            "own pattern &mdash; alongside Thag 1.61 (Vappa) and Thag "
            "1.63 (Pakkha) from the chapter before this one. All "
            "three withhold the very thing a reader might most want: "
            "a stated reason for the pattern they describe."]),
    ],
    terms=[
        ("uppatati",
         "&ldquo;springs up, rises&rdquo; &mdash; the first action "
         "named in the verse's paired contrasts."),
        ("nipatati",
         "&ldquo;settles down, falls&rdquo; &mdash; paired against "
         "uppatati in the verse's first two lines."),
        ("vasati",
         "&ldquo;dwells, remains&rdquo; &mdash; the verb behind the "
         "verse's third line, about remaining when others depart."),
        ("ramati",
         "&ldquo;delights, takes pleasure&rdquo; &mdash; the verb "
         "behind the verse's fourth line, declined in the final "
         "contrast."),
        ("Piyañjaha",
         "&ldquo;one who has given up what is dear&rdquo; &mdash; "
         "piya (&lsquo;dear&rsquo;) plus jaha (&lsquo;one who "
         "abandons&rsquo;)."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.76:1.1-1.4"),
    ],
    quiz=[
        {"q": "What structure does this entire verse follow?",
         "opts": [
             "Four paired, contrasting actions with no narrative frame",
             "A single extended simile",
             "A dialogue between two speakers",
             "A numeric list with definitions"],
         "correct": 0,
         "expl": "The pattern itself, repeated four times, is the verse's content."},
        {"q": "According to the verse, what should happen when others spring up?",
         "opts": [
             "One should also spring up",
             "One should settle down",
             "One should leave",
             "One should delight"],
         "correct": 1,
         "expl": "Uppatantesu nipate, the verse's first contrast."},
        {"q": "According to the verse, what should happen when others delight?",
         "opts": [
             "One should also delight",
             "One should depart",
             "One should settle down",
             "One should not delight"],
         "correct": 3,
         "expl": "Ramamānesu no rame, the verse's fourth and final contrast."},
        {"q": "What does the name Piyañjaha literally mean?",
         "opts": [
             "One who guards calves",
             "One who dwells in a hut",
             "One who has given up what is dear",
             "One who has come from the past"],
         "correct": 2,
         "expl": "Piya ('dear') plus jaha ('one who abandons')."},
        {"q": "How does this reading guide describe the connection between Piyañjaha's name and this verse?",
         "opts": [
             "The name quotes the verse's exact wording",
             "There is no connection at all",
             "The name matches the verse's overall theme, especially its final line, without quoting its specific wording",
             "The name contradicts the verse's message"],
         "correct": 2,
         "expl": "A thematic match, not a literal quotation."},
        {"q": "Does this reading guide resolve whether the verse is addressed to a listener, a private resolve, or a description of how the monk already lives?",
         "opts": [
             "Yes, it is definitively addressed to a listener",
             "No — the verse supplies no addressee or first-person marker to confirm which",
             "Yes, it is definitively a private resolve",
             "Yes, it is definitively a description of someone else"],
         "correct": 1,
         "expl": "The grammatical person is left genuinely ambiguous."},
        {"q": "What two earlier poems does this reading guide compare this verse to, as a small cluster of riddle-like verses?",
         "opts": [
             "Thag 1.1 Subhūti and Thag 1.15 Kuṇḍadhāna",
             "Thag 1.41 Sirivaḍḍha and Thag 1.51 Godhika",
             "Thag 1.71 Vacchapāla and Thag 1.72 Ātuma",
             "Thag 1.61 Vappa and Thag 1.63 Pakkha"],
         "correct": 3,
         "expl": "Both from Chapter Seven, offering no stated reason for their own pattern."},
        {"q": "What does 'vasati' mean?",
         "opts": [
             "To depart",
             "To dwell, to remain",
             "To delight",
             "To rise"],
         "correct": 1,
         "expl": "The verb behind the verse's third line."},
        {"q": "What is withheld from all three of the riddle-like verses this reading guide groups together?",
         "opts": [
             "A stated reason for the pattern they describe",
             "Any verbs at all",
             "Any mention of a monk",
             "Any mention of Pali vocabulary"],
         "correct": 0,
         "expl": "Each states its pattern without explaining it."},
        {"q": "Where does this poem fall in Chapter Eight?",
         "opts": [
             "The final poem",
             "The opening poem",
             "The sixth poem",
             "The third poem"],
         "correct": 2,
         "expl": "Midway through the chapter's ten poems."},
    ],
    marginalia=[
        ("Four lines, one pattern", [
            "rise when they settle;",
            "settle when they rise"
        ]),
        ("A name that fits", [
            "given up what's dear —",
            "even their delight"
        ]),
        ("Who is speaking?", [
            "command, or resolve —",
            "the verse does not say"
        ]),
        ("A pattern, unexplained", [
            "four contrasts, stated plainly —",
            "no reason given"
        ]),
    ],
    further=[
        '<a href="%s/thag1.76/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.75.html">Thag 1.75 &mdash; Sus&amacr;rada</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.61.html">Thag 1.61 &mdash; Vappa</a> '
        "&mdash; an earlier riddle-like verse offering no stated "
        "reason for its own pattern, as this one does.",
        '<a href="thag-1.63.html">Thag 1.63 &mdash; Pakkha</a> '
        "&mdash; another such verse, from the same earlier cluster.",
        '<a href="thag-1.77.html">Thag 1.77 &mdash; Hatth&amacr;rohaputta</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.77 — Hatth&amacr;rohaputta
# --------------------------------------------------------------------------- #
page(
    1, 77, "Hatth&amacr;rohaputta", "Hatth&amacr;rohaputta",
    meta_title="Thag 1.77 — Hatthārohaputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Hatthārohaputta's verse on training the mind like a rutting "
        "elephant — word for word identical to Dhammapada verse 326, "
        "already complete on this site. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A retrospective account of disciplining a "
                    "formerly wayward mind"),
        ("Speaker", "Hatthārohaputta, in the first person"),
        ("Form", "One four-line verse, built on a single simile"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one vivid image"),
    ],
    why=(
        "Hatthārohaputta compares his formerly wayward mind, which "
        "&lsquo;wandered how it wished, where it liked, as it "
        "pleased&rsquo;, to a rutting elephant now to be guided with "
        "a trainer's hook. The verse is word for word identical, in "
        "both Pali and Sujato's English, to Dhammapada verse 326 in "
        "the Nāgavagga (&lsquo;Elephants&rsquo;) chapter, already "
        "complete on this site &mdash; a genuine shared verse between "
        "the two collections, not merely a similar image."),
    guide=[
        ("A verse shared word for word with the Dhammapada", [
            "Compared directly against this site's own Dhammapada "
            "pages, this verse's four lines match Dhp 326 exactly "
            "&mdash; the same Pali, segment by segment, and the same "
            "English translation. Dhp 326 sits in the Nāgavagga, the "
            "Dhammapada's &lsquo;Elephants&rsquo; chapter, among "
            "several other verses built on taming and elephant "
            "imagery. This is the clearest verbatim match this "
            "reading guide has found between the Theragātha and the "
            "Dhammapada: not an echo or a shared phrase, but the same "
            "verse appearing in two independent collections, "
            "attributed here to a named elder."]),
        ("A name that supplies its own simile", [
            "Hatthārohaputta's name reads literally as hatthāroha "
            "(&lsquo;elephant-rider, mahout&rsquo;) plus putta "
            "(&lsquo;son&rsquo;) &mdash; &lsquo;son of an "
            "elephant-rider&rsquo;. Where other names in this "
            "collection have echoed a verse's specific wording or a "
            "narrated deed, this one works differently: it supplies "
            "the family trade that the verse's own central image "
            "draws from. A son raised around elephant-training reaches, "
            "naturally enough, for an elephant-training simile when "
            "describing how he now disciplines his mind."]),
        ("Not any elephant, but one in must", [
            "The verse's simile is more specific than a generic "
            "&lsquo;elephant&rsquo;: hatthippabhinna describes an "
            "elephant in rut, or musth &mdash; a periodic state of "
            "heightened aggression and unpredictability in bull "
            "elephants, requiring a trainer's most careful handling. "
            "The image is not simply of size or strength but of a "
            "mind at its most dangerously unruly, guided all the same "
            "by a hook (aṅkusa) in a skilled hand."]),
    ],
    terms=[
        ("hatthāroha",
         "&ldquo;elephant-rider, mahout&rdquo; &mdash; the trade "
         "this monk's name identifies as belonging to his father."),
        ("hatthippabhinna",
         "&ldquo;a rutting elephant&rdquo;, literally one "
         "&ldquo;whose temples have burst&rdquo; &mdash; describing "
         "the heightened, dangerous state of musth."),
        ("aṅkusa",
         "&ldquo;hook, goad&rdquo; &mdash; the tool a mahout uses to "
         "guide even an elephant in this state."),
        ("niggahessāmi",
         "&ldquo;I will restrain, I will guide&rdquo; &mdash; a "
         "future-tense verb, describing a resolve rather than a "
         "completed act."),
        ("Nāgavagga",
         "&ldquo;Elephants&rdquo;, the Dhammapada chapter (verses "
         "320&ndash;333) containing Dhp 326, identical to this "
         "verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.77:1.1-1.4"),
    ],
    quiz=[
        {"q": "What earlier-completed collection on this site contains a verse identical, word for word, to this one?",
         "opts": [
             "The Cariyapitaka",
             "The Dhammapada (verse 326, in the Nāgavagga)",
             "The Khuddakapatha",
             "The Therīgāthā"],
         "correct": 1,
         "expl": "Confirmed by direct comparison with this site's own Dhammapada pages."},
        {"q": "What does 'hatthippabhinna' specifically describe?",
         "opts": [
             "An elephant in rut (musth), a state of heightened aggression",
             "A young, newly born elephant",
             "A tame, docile elephant",
             "An elephant used for royal processions"],
         "correct": 0,
         "expl": "Not merely any elephant, but one at its most unruly."},
        {"q": "What does the name Hatthārohaputta literally mean?",
         "opts": [
             "One who has given up what is dear",
             "One who dwells in a hut",
             "Son of an elephant-rider (mahout)",
             "One who has come from the past"],
         "correct": 2,
         "expl": "Hatthāroha ('mahout') plus putta ('son')."},
        {"q": "How does this reading guide describe the connection between this name and the verse, compared to other name/verse connections in this collection?",
         "opts": [
             "It supplies the family trade behind the verse's own central simile, rather than quoting the verse's wording",
             "There is no connection at all",
             "It contradicts the verse's message entirely",
             "It quotes the verse's exact opening words"],
         "correct": 0,
         "expl": "A different kind of name/verse connection than the collection's earlier examples."},
        {"q": "What tool does the verse say a trainer uses to guide a rutting elephant?",
         "opts": [
             "A rope",
             "A whip",
             "A drum",
             "A hook (aṅkusa)"],
         "correct": 3,
         "expl": "Aṅkusaggaho, 'one who holds the hook'."},
        {"q": "What tense does 'niggahessāmi' use?",
         "opts": [
             "Past tense",
             "Imperative",
             "Future tense, describing a resolve",
             "Present tense"],
         "correct": 2,
         "expl": "'I will restrain/guide', not a completed act."},
        {"q": "According to the verse, how did the speaker's mind behave in the past?",
         "opts": [
             "It was always calm and obedient",
             "It never wandered at all",
             "It was guided carefully by a trainer",
             "It wandered however it wished, wherever it liked, as it pleased"],
         "correct": 3,
         "expl": "Idaṁ pure cittamacāri cārikaṁ, the verse's opening line."},
        {"q": "Where does Dhp 326, the Dhammapada parallel to this verse, appear?",
         "opts": [
             "In the Nāgavagga, the 'Elephants' chapter",
             "In the Cittavagga, the 'Mind' chapter",
             "In the first chapter of the Dhammapada",
             "In the final chapter of the Dhammapada"],
         "correct": 0,
         "expl": "Among several other elephant-taming verses."},
        {"q": "Is the Pali wording of the Dhammapada parallel identical to this Theragātha verse, or only similar in theme?",
         "opts": [
             "Only similar in theme, with different wording",
             "The Dhammapada version is much longer",
             "Identical, word for word, as confirmed by direct comparison",
             "There is no real similarity at all"],
         "correct": 2,
         "expl": "A genuine verbatim match, not merely a shared image."},
        {"q": "What image does the verse use to describe the disciplined mind?",
         "opts": [
             "A river returning to its banks",
             "A trainer guiding a rutting elephant with a hook",
             "A bird returning to its nest",
             "A fire being extinguished"],
         "correct": 1,
         "expl": "The verse's single governing simile."},
    ],
    marginalia=[
        ("The same verse, twice", [
            "Theragātha, Dhammapada —",
            "one quatrain, two homes"
        ]),
        ("A son of the trade", [
            "raised among elephants —",
            "the simile, inherited"
        ]),
        ("Not any elephant", [
            "temples burst with rut —",
            "the hardest one to guide"
        ]),
        ("A wandering mind, reined in", [
            "wherever it wished, once —",
            "now, hook in hand"
        ]),
    ],
    further=[
        '<a href="%s/thag1.77/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../dhammapada/dhp-23.html">Dhammapada 23 &mdash; '
        "Nāgavagga (Elephants)</a> &mdash; contains Dhp 326, identical "
        "word for word to this verse.",
        '<a href="thag-1.76.html">Thag 1.76 &mdash; Piya&ntilde;jaha</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.78.html">Thag 1.78 &mdash; Me&#7751;&#7693;asira</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.78 — Me&#7751;&#7693;asira
# --------------------------------------------------------------------------- #
page(
    1, 78, "Me&#7751;&#7693;asira", "Me&#7751;&#7693;asira",
    meta_title="Thag 1.78 — Meṇḍasira | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Meṇḍasira's verse, opening with the same words as the "
        "Dhammapada's famous 'house-builder' verses before closing on "
        "its own, different note. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 8 of 10",
    glance=[
        ("Setting", "A retrospective declaration of liberation, "
                    "opening with a well-known shared formula"),
        ("Speaker", "Meṇḍasira, in the first person"),
        ("Form", "One four-line verse: a borrowed opening, then an "
                 "independent close"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one notable borrowing"),
    ],
    why=(
        "This verse's first two lines &mdash; &lsquo;Transmigrating "
        "through countless rebirths, I've journeyed without "
        "reward&rsquo; &mdash; are identical, word for word in both "
        "Pali and Sujato's English, to the opening of Dhammapada "
        "verse 153: the celebrated couplet traditionally recited as "
        "the Buddha's own exultant cry on the night of his awakening, "
        "as this site's own Dhammapada guide (Dhp 11) describes it. "
        "But where Dhp 153 continues into the famous "
        "&lsquo;house-builder&rsquo; image, completed in Dhp 154, "
        "this verse takes the same opening somewhere else entirely."),
    guide=[
        ("A famous opening, borrowed", [
            "Compared directly against this site's own Dhammapada "
            "pages, this verse's first two lines match Dhp 153 "
            "exactly: the same Pali, and the same English translation. "
            "Dhp 153 opens the Dhammapada's celebrated 'house-builder' "
            "couplet (153&ndash;154), traditionally associated with "
            "the moment of the Buddha's own awakening &mdash; a "
            "genuinely famous piece of shared canonical language, not "
            "an obscure coincidence."]),
        ("A different ending", [
            "Dhp 153 continues, 'searching for the house-builder; "
            "painful is birth again and again', resolved in Dhp 154's "
            "triumphant 'I've seen you, house-builder!' This verse "
            "instead closes with 'for me, born to suffering, the mass "
            "of suffering is now shattered' &mdash; no house-builder, "
            "no construction imagery at all. This reading guide does "
            "not assert why the opening was redirected this way: "
            "whether this reflects an independent verse built on a "
            "common formulaic opening, or a deliberate variation on "
            "the famous couplet, is not something the text itself "
            "settles."]),
        ("A name describing an animal's head", [
            "Meṇḍasira reads literally as meṇḍa (&lsquo;ram, "
            "sheep&rsquo;) plus sira (&lsquo;head&rsquo;) &mdash; "
            "&lsquo;ram's head&rsquo;. The verse gives no account of "
            "why this elder carried the name, and this reading guide "
            "does not speculate beyond the plain meaning of the "
            "compound itself."]),
    ],
    terms=[
        ("saṁsāra",
         "&ldquo;the cycle of rebirth&rdquo; &mdash; the countless "
         "transmigration named in this verse's opening line, shared "
         "word for word with Dhp 153."),
        ("gahakāraka",
         "&ldquo;house-builder&rdquo; &mdash; the central image of "
         "Dhp 153&ndash;154, notably absent from this verse despite "
         "its shared opening."),
        ("dukkhakkhandha",
         "&ldquo;the mass of suffering&rdquo; &mdash; what this "
         "verse says has &lsquo;fallen away&rsquo;, in place of Dhp "
         "153&ndash;154's house-building imagery."),
        ("Meṇḍasira",
         "&ldquo;ram's head&rdquo; &mdash; meṇḍa (&lsquo;ram&rsquo;) "
         "plus sira (&lsquo;head&rsquo;)."),
        ("Jarāvagga",
         "&ldquo;Old Age&rdquo;, the Dhammapada chapter (verses "
         "146&ndash;156) containing Dhp 153&ndash;154, this verse's "
         "shared opening."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.78:1.1-1.4"),
    ],
    quiz=[
        {"q": "What do this verse's first two lines match, word for word?",
         "opts": [
             "The opening of Thag 1.61 Vappa",
             "A verse from the Khuddakapatha",
             "A verse from the Therīgāthā",
             "The opening of Dhammapada verse 153"],
         "correct": 3,
         "expl": "Confirmed by direct comparison with this site's own Dhammapada pages."},
        {"q": "What moment is Dhp 153–154 traditionally associated with, according to this site's own Dhammapada guide?",
         "opts": [
             "The Buddha's own awakening, on the night it occurred",
             "The Buddha's first sermon at Isipatana",
             "The Buddha's final passing",
             "The founding of the monastic order"],
         "correct": 0,
         "expl": "As described on this site's Dhp 11 (Jarāvagga) page."},
        {"q": "Does this verse continue into the Dhammapada's famous 'house-builder' image after its shared opening?",
         "opts": [
             "Yes, it completes the house-builder image exactly as Dhp 154 does",
             "No — it closes with a different declaration, about the mass of suffering falling away",
             "Yes, but with a different house-builder",
             "The verse has no closing lines at all"],
         "correct": 1,
         "expl": "The shared wording is limited to the opening two lines."},
        {"q": "What does this verse actually conclude with, instead of the house-builder image?",
         "opts": [
             "A request for permission to leave",
             "A list of the five hindrances",
             "A dialogue with Māra",
             "A declaration that the mass of suffering has fallen away"],
         "correct": 3,
         "expl": "Dukkhakkhandho aparaddho, the verse's own closing line."},
        {"q": "What does the name Meṇḍasira literally mean?",
         "opts": [
             "Son of an elephant-rider",
             "One who has given up what is dear",
             "One who guards calves",
             "Ram's head"],
         "correct": 3,
         "expl": "Meṇḍa ('ram') plus sira ('head')."},
        {"q": "What does 'gahakāraka' mean?",
         "opts": [
             "House-builder",
             "Elephant trainer",
             "Ram's head",
             "One who has gone forth"],
         "correct": 0,
         "expl": "The central image of Dhp 153–154, absent from this verse's own ending."},
        {"q": "Does this reading guide assert a specific reason why this verse's ending diverges from Dhp 153–154?",
         "opts": [
             "Yes, it was certainly composed as a deliberate parody",
             "No — it presents two possibilities without asserting which is correct",
             "Yes, it was certainly a scribal error",
             "Yes, it was certainly composed after the Dhammapada verse and directly responds to it"],
         "correct": 1,
         "expl": "The text itself does not settle the question."},
        {"q": "In which Dhammapada chapter does Dhp 153 appear?",
         "opts": [
             "The Cittavagga (Mind)",
             "The Nāgavagga (Elephants)",
             "The Jarāvagga (Old Age)",
             "The first chapter of the Dhammapada"],
         "correct": 2,
         "expl": "Verses 146–156, on the body's fragility and decay."},
        {"q": "How much of Dhp 153–154's wording, in total, is shared with this verse?",
         "opts": [
             "None of it",
             "All four lines of both verses",
             "Only the opening two lines of Dhp 153",
             "Only the closing line of Dhp 154"],
         "correct": 2,
         "expl": "The match is a shared opening, not a full-verse repetition."},
        {"q": "What kind of textual connection does this verse have to the Dhammapada, according to this reading guide?",
         "opts": [
             "A shared opening formula, redirected to a different closing declaration",
             "No connection at all",
             "An unrelated verse that happens to use similar vocabulary",
             "A full, complete repetition of both Dhp 153 and 154"],
         "correct": 0,
         "expl": "A partial, not total, verbatim match."},
    ],
    marginalia=[
        ("A famous opening, borrowed", [
            "countless rebirths, no reward —",
            "the same two lines, elsewhere"
        ]),
        ("No house-builder here", [
            "not seen, not broken —",
            "suffering's mass, instead"
        ]),
        ("A name for an animal's head", [
            "ram's head, plainly —",
            "no story given"
        ]),
        ("Two verses, one line apart", [
            "one seeks; one has found —",
            "the search left unfinished"
        ]),
    ],
    further=[
        '<a href="%s/thag1.78/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../dhammapada/dhp-11.html">Dhammapada 11 &mdash; '
        "Jar&amacr;vagga (Old Age)</a> &mdash; contains Dhp "
        "153&ndash;154, the famous 'house-builder' verses sharing "
        "this poem's opening two lines.",
        '<a href="thag-1.77.html">Thag 1.77 &mdash; Hatth&amacr;rohaputta</a> '
        "&mdash; the poem immediately before this one, also matched "
        "word for word to a Dhammapada verse.",
        '<a href="thag-1.79.html">Thag 1.79 &mdash; Rakkhita</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.79 — Rakkhita
# --------------------------------------------------------------------------- #
page(
    1, 79, "Rakkhita", "Rakkhita",
    meta_title="Thag 1.79 — Rakkhita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Rakkhita's verse declaring the three roots of greed, hatred, "
        "and delusion overcome, closing with the same 'quenched' "
        "image used earlier in this collection. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A retrospective declaration of the three roots "
                    "overcome"),
        ("Speaker", "Rakkhita, in the first person"),
        ("Form", "One four-line verse, one root named per line, "
                 "closing on a single image"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a well-known category"),
    ],
    why=(
        "Rakkhita declares all three of the traditional root "
        "defilements &mdash; greed, hatred, and delusion &mdash; "
        "overcome, one per line, before closing: &lsquo;I'm cooled, "
        "quenched&rsquo;. The closing word, nibbuta, is the same "
        "participle used by several elders earlier in the Book of the "
        "Ones, and pairs with this chapter's own opening poem (Thag "
        "1.71), which was the first in the collection to name Nibbāna "
        "outright."),
    guide=[
        ("Three roots, three different verbs", [
            "The verse names the three traditional root defilements "
            "&mdash; rāga (&lsquo;greed, lust&rsquo;), dosa "
            "(&lsquo;hatred&rsquo;), and moha (&lsquo;delusion&rsquo;) "
            "&mdash; but does not describe their removal with a single "
            "repeated verb. Each gets its own: rāga is pahīna "
            "(&lsquo;given up&rsquo;), dosa is samūhata "
            "(&lsquo;rooted out, eradicated&rsquo;), and moha is "
            "vigata (&lsquo;departed, gone&rsquo;). The variation "
            "keeps what could have been a mechanically repeated "
            "formula from reading as one."]),
        ("'Quenched', a recurring close", [
            "Sītibhūtosmi nibbuto, &lsquo;I'm cooled, quenched&rsquo;, "
            "closes the verse with a participle, nibbuta, already "
            "used earlier in the Book of the Ones (Thag 1.5, 1.7, "
            "1.8, and 1.32). This chapter's own opening poem, Thag "
            "1.71, was the first verse in the whole collection to "
            "name the noun Nibbāna directly, rather than only "
            "gesturing at the goal through a cognate like this one. "
            "Together, the chapter's first and second-to-last poems "
            "both reach for the same root, at opposite ends of "
            "explicitness."]),
        ("A name that doesn't obviously match", [
            "Rakkhita means &lsquo;protected, guarded&rsquo;, from "
            "rakkhati (&lsquo;protects&rsquo;) &mdash; a common, "
            "auspicious-sounding name, but not one that points "
            "directly at this verse's content the way several other "
            "names in this chapter do. Vacchapāla's name touched on "
            "an occupation, Piyañjaha's matched its verse's theme, "
            "and Hatthārohaputta's supplied its verse's own simile; "
            "Rakkhita's, by contrast, gives no obvious handle on the "
            "three-roots declaration that follows it."]),
    ],
    terms=[
        ("rāga",
         "&ldquo;greed, lust&rdquo; &mdash; the first root "
         "defilement named, described here as pahīna, "
         "&lsquo;given up&rsquo;."),
        ("dosa",
         "&ldquo;hatred, hostility&rdquo; &mdash; the second root, "
         "described as samūhata, &lsquo;rooted out&rsquo;."),
        ("moha",
         "&ldquo;delusion&rdquo; &mdash; the third root, described "
         "as vigata, &lsquo;departed, gone&rsquo;."),
        ("sītibhūta",
         "&ldquo;become cool&rdquo; &mdash; paired with nibbuta in "
         "the verse's closing line."),
        ("Rakkhita",
         "&ldquo;protected, guarded&rdquo; &mdash; from rakkhati, "
         "&lsquo;protects&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.79:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three root defilements does this verse name?",
         "opts": [
             "Faith, energy, and mindfulness",
             "Old age, sickness, and death",
             "Greed, hatred, and delusion",
             "Doubt, restlessness, and drowsiness"],
         "correct": 2,
         "expl": "Rāga, dosa, and moha, the traditional three roots."},
        {"q": "Does the verse use the same verb for the removal of all three roots?",
         "opts": [
             "Yes, the same verb is repeated three times",
             "No, the verse uses no verbs at all",
             "No — each root gets its own distinct verb: given up, rooted out, and departed",
             "Yes, but only for two of the three"],
         "correct": 2,
         "expl": "Pahīna, samūhata, and vigata, three different words."},
        {"q": "What does the verse's closing line declare?",
         "opts": [
             "'I'm cooled, quenched'",
             "A wish for future rebirth",
             "A request for teaching",
             "A description of a dream"],
         "correct": 0,
         "expl": "Sītibhūtosmi nibbuto, the verse's final words."},
        {"q": "Where else in the Book of the Ones has the participle 'nibbuta' appeared before this verse?",
         "opts": [
             "Nowhere — this is its first appearance",
             "Only in the collection's final poem",
             "Only in Chapter Seven",
             "Thag 1.5, 1.7, 1.8, and 1.32"],
         "correct": 3,
         "expl": "Several elders earlier in the Book of the Ones use this same word."},
        {"q": "How does this verse relate to Thag 1.71, this chapter's opening poem?",
         "opts": [
             "They share no vocabulary at all",
             "Both reach for the nibb- root, though 1.71 names Nibbāna directly while 1.79 uses the cognate participle nibbuta",
             "Both are addressed to the same person",
             "Both use exactly the same four lines"],
         "correct": 1,
         "expl": "The chapter's opening and near-closing poems bracket the same root."},
        {"q": "What does 'dosa' mean?",
         "opts": [
             "Hatred, hostility",
             "Doubt",
             "Delusion",
             "Restlessness"],
         "correct": 0,
         "expl": "The second of the three root defilements."},
        {"q": "What does the name Rakkhita mean?",
         "opts": [
             "Ram's head",
             "Son of an elephant-rider",
             "One who has given up what is dear",
             "Protected, guarded"],
         "correct": 3,
         "expl": "From rakkhati, 'protects'."},
        {"q": "According to this reading guide, does Rakkhita's name obviously connect to this verse's content?",
         "opts": [
             "Yes, exactly as directly as Hatthārohaputta's name connects to his verse",
             "No — unlike several other names in this chapter, it gives no obvious handle on the verse that follows it",
             "Yes, it directly names one of the three roots",
             "Yes, it is a direct quotation from the verse"],
         "correct": 1,
         "expl": "A contrast with this chapter's more transparently connected names."},
        {"q": "What does 'moha' mean?",
         "opts": [
             "Delusion",
             "Greed",
             "Hatred",
             "Doubt"],
         "correct": 0,
         "expl": "The third of the three root defilements, described as 'departed'."},
        {"q": "Where does this poem fall in Chapter Eight?",
         "opts": [
             "The opening poem",
             "The fourth poem",
             "The final poem",
             "The ninth poem"],
         "correct": 3,
         "expl": "The second-to-last poem, immediately before the chapter's close."},
    ],
    marginalia=[
        ("Three roots, three verbs", [
            "given up, rooted out, gone —",
            "no word repeated"
        ]),
        ("Cooled, quenched, again", [
            "the same word as before —",
            "four times, now a fifth"
        ]),
        ("A name, unconnected", [
            "protected, guarded —",
            "no link to what follows"
        ]),
        ("Opening and near-close", [
            "Nibbāna, named once —",
            "quenched, named again"
        ]),
    ],
    further=[
        '<a href="%s/thag1.79/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.78.html">Thag 1.78 &mdash; Me&#7751;&#7693;asira</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.71.html">Thag 1.71 &mdash; Vacchap&amacr;la</a> '
        "&mdash; the chapter's opener, the first poem in the "
        "collection to name Nibbāna directly.",
        '<a href="thag-1.80.html">Thag 1.80 &mdash; Ugga</a> '
        "&mdash; the next and final poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.80 — Ugga
# --------------------------------------------------------------------------- #
page(
    1, 80, "Ugga", "Ugga",
    meta_title="Thag 1.80 — Ugga | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ugga's verse declaring karma exhausted and no more future "
        "lives, closing Chapter Eight with its double formulaic "
        "ending. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Eight &middot; Poem 10 of 10",
    glance=[
        ("Setting", "A retrospective declaration, closing this "
                    "chapter's tenth and final poem"),
        ("Speaker", "Ugga, in the first person"),
        ("Form", "One four-line verse, followed by the chapter's "
                 "formulaic double closing"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain, direct vocabulary"),
    ],
    why=(
        "Ugga closes Chapter Eight with the plainest possible "
        "declaration: whatever deeds he has done, much or little, "
        "are all now &lsquo;completely exhausted&rsquo;, and "
        "&lsquo;there'll be no more future lives&rsquo;. It is the "
        "third such closing declaration in a row &mdash; after Thag "
        "1.78's fallen-away &lsquo;mass of suffering&rsquo; and Thag "
        "1.79's &lsquo;cooled, quenched&rsquo; &mdash; before the "
        "chapter's own formulaic close."),
    guide=[
        ("Karma exhausted, no more becoming", [
            "The verse's structure is simple: whatever deeds "
            "(kamma), large or small, once existed, are now "
            "parikkhīṇa, &lsquo;completely exhausted&rsquo;; "
            "therefore natthi dāni punabbhavo, &lsquo;there is now no "
            "more renewed existence&rsquo;. This is the third poem in "
            "a row to close Chapter Eight's back half with a "
            "declaration of this general kind &mdash; suffering "
            "fallen away in Thag 1.78, cooled and quenched in Thag "
            "1.79, and now karma exhausted here."]),
        ("The chapter's double closing", [
            "As in every chapter so far, two more lines follow the "
            "poem itself, both left untranslated by Sujato: vaggo "
            "aṭṭhamo (&lsquo;the eighth chapter [ends]&rsquo;), then "
            "an uddāna, a summary verse listing all ten names for "
            "easy memorization. This chapter's uddāna shortens "
            "Hatthārohaputta to Ārohaputta to fit its metrical line "
            "&mdash; the same kind of compression seen in earlier "
            "chapters' closing summaries &mdash; and adds one small "
            "detail not found in his own verse: it calls Māṇava "
            "isi, &lsquo;the sage&rsquo;, an epithet this reading "
            "guide notes only as it appears in the summary, not as "
            "a claim Māṇava's own poem makes about himself."]),
        ("Ten poems, no single mold", [
            "Looking back across the chapter: an impersonal teaching "
            "on nibbāna (1.71) beside a wife left behind (1.72); the "
            "three sights that trigger renunciation (1.73) beside an "
            "unglossed doctrinal list (1.74); a maxim about good "
            "company (1.75) beside a four-line paradox (1.76); a "
            "verse shared word for word with the Dhammapada (1.77) "
            "beside one borrowing only its opening from the "
            "Dhammapada's most famous couplet (1.78); and finally "
            "three closing declarations in a row (1.78&ndash;1.80). "
            "Unlike Chapter Six, built almost entirely around a "
            "single image, Chapter Eight moves through nearly as many "
            "different kinds of verse as it has poems."]),
        ("A name shared with a well-known lay disciple", [
            "Ugga is also the name of a celebrated lay follower, Ugga "
            "of Vesālī, listed elsewhere in the canon among those "
            "foremost for giving agreeable gifts. This reading guide "
            "does not assert that this monk and that lay disciple are "
            "the same person &mdash; the name is common, and nothing "
            "here confirms the connection &mdash; only notes the "
            "shared name, in keeping with this collection's usual "
            "caution about such cases."]),
    ],
    terms=[
        ("kamma",
         "&ldquo;deed, action&rdquo; &mdash; what the verse says is "
         "now completely exhausted."),
        ("parikkhīṇa",
         "&ldquo;completely exhausted, finished&rdquo; &mdash; "
         "describing all of the speaker's past deeds."),
        ("punabbhava",
         "&ldquo;renewed existence, future rebirth&rdquo; &mdash; "
         "puna (&lsquo;again&rsquo;) plus bhava "
         "(&lsquo;existence&rsquo;)."),
        ("vaggo aṭṭhamo",
         "&ldquo;the eighth chapter [ends]&rdquo; &mdash; the "
         "untranslated closing marker for this chapter."),
        ("uddāna",
         "a summary verse listing the names of all the elders "
         "covered in a chapter, for ease of memorization."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.80:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse declare about the speaker's past deeds?",
         "opts": [
             "They are all completely exhausted",
             "They are growing more numerous",
             "They are unknown to him",
             "They will be repeated"],
         "correct": 0,
         "expl": "Sabbametaṁ parikkhīṇaṁ, the verse's third line."},
        {"q": "What does the verse conclude follows from this?",
         "opts": [
             "A wish for a favorable next rebirth",
             "There will be no more future lives",
             "A request to remain in the order",
             "A description of a dream"],
         "correct": 1,
         "expl": "Natthi dāni punabbhavo, the verse's closing line."},
        {"q": "How many poems in a row, including this one, close with a similar declaration of liberation achieved?",
         "opts": [
             "Just this one",
             "Two",
             "Three — Thag 1.78, 1.79, and 1.80",
             "All ten poems in the chapter"],
         "correct": 2,
         "expl": "Suffering fallen away, then cooled and quenched, then karma exhausted."},
        {"q": "What two untranslated lines follow this verse, as in every chapter so far?",
         "opts": [
             "A second verse by the same elder",
             "A dedication to the Buddha",
             "A chapter-closing marker and a summary verse (uddāna) listing all ten names",
             "A list of monastic rules"],
         "correct": 2,
         "expl": "Vaggo aṭṭhamo, then the uddāna."},
        {"q": "How does the chapter's uddāna refer to Hatthārohaputta?",
         "opts": [
             "By his full name, unshortened",
             "Not at all — he is omitted",
             "By a completely different name",
             "Shortened to 'Ārohaputta', to fit the summary verse's meter"],
         "correct": 3,
         "expl": "The same kind of metrical compression seen in earlier chapters' uddānas."},
        {"q": "What epithet does the uddāna add to Māṇava's name, not found in his own verse?",
         "opts": [
             "'Thera', the elder",
             "'Mahā', the great",
             "No epithet is added at all",
             "'Isi', the sage"],
         "correct": 3,
         "expl": "Noted here only as it appears in the summary verse."},
        {"q": "According to this reading guide, does Chapter Eight repeat a single dominant image the way Chapter Six did?",
         "opts": [
             "Yes, exactly the same way",
             "No — it moves through nearly as many different kinds of verse as it has poems",
             "Yes, but with a different image",
             "This reading guide does not compare the two chapters"],
         "correct": 1,
         "expl": "Teaching verses, personal narrative, riddles, and Dhammapada parallels, all within one chapter."},
        {"q": "What well-known lay disciple shares this monk's name, according to this reading guide?",
         "opts": [
             "Anāthapiṇḍika",
             "Visākhā",
             "Cittagahapati",
             "Ugga of Vesālī, foremost among those giving agreeable gifts"],
         "correct": 3,
         "expl": "The same-name connection is noted, not asserted as a confirmed identity."},
        {"q": "What does 'parikkhīṇa' mean?",
         "opts": [
             "Completely exhausted, finished",
             "Newly begun",
             "Partially completed",
             "Uncertain"],
         "correct": 0,
         "expl": "Describing all of the speaker's past deeds, large or small."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "The opening poem of Chapter Eight",
             "The tenth and final poem of Chapter Eight",
             "The first poem of Chapter Nine",
             "A poem in the Book of the Twos"],
         "correct": 1,
         "expl": "Closing this chapter's set of ten."},
    ],
    marginalia=[
        ("Deeds, all exhausted", [
            "much or little, done —",
            "none of it remains"
        ]),
        ("A third declaration", [
            "suffering fell; quenched; now —",
            "no more becoming"
        ]),
        ("Ten names, one summary", [
            "shortened to fit the meter —",
            "a sage added, unasked"
        ]),
        ("No single thread", [
            "teaching, wife, three sights —",
            "riddle, elephant, house"
        ]),
    ],
    further=[
        '<a href="%s/thag1.80/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.79.html">Thag 1.79 &mdash; Rakkhita</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.71.html">Thag 1.71 &mdash; Vacchap&amacr;la</a> '
        "&mdash; this chapter's opening poem.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.81 — Samitigutta
# --------------------------------------------------------------------------- #
page(
    1, 81, "Samitigutta", "Samitigutta",
    meta_title="Thag 1.81 — Samitigutta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Samitigutta's verse, opening Chapter Nine with a claim that "
        "his remaining bad karma will ripen in this very life, "
        "nowhere else. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; a general reflection on "
                    "where remaining karma will ripen"),
        ("Speaker", "Samitigutta, in the first person"),
        ("Form", "One four-line verse, a single claim"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one doctrinal implication"),
    ],
    why=(
        "Chapter Nine opens with a claim that makes sense specifically "
        "for someone who has ended future rebirth: whatever bad "
        "deeds remain from past lives, Samitigutta says, will be "
        "experienced &lsquo;right here&rsquo;, in this very existence "
        "&mdash; &lsquo;not in any other place&rsquo;."),
    guide=[
        ("Karma with nowhere left to go", [
            "For someone still bound for future rebirths, unripened "
            "karma can, in principle, follow across many lives to "
            "come. But for one who has ended rebirth &mdash; an "
            "arahant in his final existence &mdash; there is no "
            "&lsquo;next place&rsquo; for any leftover karma to "
            "travel to. Whatever remains must work itself out within "
            "this one life, because this life is the only one left. "
            "Read this way, the verse's claim is less a general "
            "doctrine about how karma works for everyone than a "
            "specific consequence of Samitigutta's own situation: "
            "having no more lives ahead of him, this life is where "
            "everything left over has to land."]),
        ("A name this reading guide doesn't press", [
            "Samitigutta's name could plausibly connect to samita "
            "(&lsquo;calmed, pacified&rsquo;) or to samiti "
            "(&lsquo;assembly, gathering&rsquo;), with gutta "
            "(&lsquo;protected, guarded&rsquo;) as its second element "
            "either way. Given the ambiguity, this reading guide does "
            "not assert which sense the name draws on."]),
        ("Opening a chapter with no comments to draw on", [
            "None of the ten poems in Chapter Nine have a surviving "
            "Sujato comment to work from, unlike some earlier "
            "chapters. This reading guide relies more heavily here on "
            "the verses' own wording, cross-references within the "
            "collection, and well-known background where it applies "
            "cleanly &mdash; and is correspondingly more cautious "
            "about anything the text itself doesn't settle."]),
    ],
    terms=[
        ("pāpa",
         "&ldquo;bad, evil&rdquo; &mdash; describing the deeds this "
         "verse says remain to be experienced."),
        ("vedanīya",
         "&ldquo;to be experienced, to be felt&rdquo; &mdash; a "
         "gerundive form, describing karma still awaiting its "
         "result."),
        ("idheva",
         "&ldquo;right here&rdquo; &mdash; idha (&lsquo;here&rsquo;) "
         "plus eva (&lsquo;indeed, precisely&rsquo;), emphasizing "
         "this very existence."),
        ("vatthu",
         "&ldquo;place, ground, basis&rdquo; &mdash; what the verse "
         "says there is no other of, for this karma to ripen in."),
        ("Samitigutta",
         "a name this reading guide does not confidently gloss, "
         "given ambiguity between two possible first elements."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.81:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse say about bad deeds from previous lives?",
         "opts": [
             "They will be experienced right here, in this very life, not elsewhere",
             "They have already been forgotten",
             "They will ripen only after many more rebirths",
             "They never actually happened"],
         "correct": 0,
         "expl": "Idheva taṁ vedanīyaṁ, vatthu aññaṁ na vijjatī, the verse's core claim."},
        {"q": "According to this reading guide, why might this claim make particular sense for an arahant in his final life?",
         "opts": [
             "Because arahants are immune to all karma",
             "Because karma only exists in this one specific life for everyone",
             "Because the verse says karma disappears at death",
             "Because there is no future existence left for any leftover karma to ripen in"],
         "correct": 3,
         "expl": "A specific consequence of having no more lives ahead, not a universal claim about karma for everyone."},
        {"q": "Does this reading guide confidently explain the meaning of Samitigutta's name?",
         "opts": [
             "Yes, definitively, as 'protector of the assembly'",
             "Yes, definitively, as 'guardian of calm'",
             "No — it notes two possible first elements without asserting which applies",
             "Yes, definitively, as a place name"],
         "correct": 2,
         "expl": "Ambiguity between samita ('calmed') and samiti ('assembly') as the name's first element."},
        {"q": "What does 'idheva' mean?",
         "opts": [
             "Right here",
             "Nowhere at all",
             "In a future life",
             "In a distant place"],
         "correct": 0,
         "expl": "Idha ('here') plus eva ('indeed'), emphasizing this very existence."},
        {"q": "What does 'vatthu' mean?",
         "opts": [
             "A monk's robe",
             "Place, ground, basis",
             "A type of meditation",
             "A kind of tree"],
         "correct": 1,
         "expl": "What the verse says there is no other of, for karma to ripen in."},
        {"q": "How many of Chapter Nine's ten poems have a surviving Sujato comment, according to this reading guide?",
         "opts": [
             "All ten",
             "Five",
             "None",
             "Only this opening poem"],
         "correct": 2,
         "expl": "This chapter relies more heavily on the verses' own wording and cross-references."},
        {"q": "What does 'pāpa' mean?",
         "opts": [
             "Good, skillful",
             "Neutral, unclassified",
             "Bad, evil",
             "Sacred, holy"],
         "correct": 2,
         "expl": "Describing the deeds this verse addresses."},
        {"q": "What does 'vedanīya' describe?",
         "opts": [
             "Karma still awaiting its result, 'to be experienced'",
             "A place that no longer exists",
             "A teacher's instruction",
             "A monastic rule"],
         "correct": 0,
         "expl": "A gerundive form of the verb 'to feel, to experience'."},
        {"q": "Is this verse's claim presented as a general doctrine about how karma works for everyone, according to this reading guide?",
         "opts": [
             "Yes, explicitly and unambiguously",
             "The verse explicitly denies that karma exists at all",
             "The verse is addressed to a general audience of laypeople",
             "No — this reading guide reads it as a consequence specific to Samitigutta's own situation"],
         "correct": 3,
         "expl": "A reading tied to having no more future lives ahead, not a universal claim."},
        {"q": "What chapter does this poem open?",
         "opts": [
             "Chapter Eight",
             "Chapter Nine",
             "Chapter Ten",
             "The Great Book"],
         "correct": 1,
         "expl": "The first of ten poems in this new chapter."},
    ],
    marginalia=[
        ("Nowhere left to go", [
            "no other place, no other life —",
            "here, or not at all"
        ]),
        ("Karma, in its last life", [
            "one existence remaining —",
            "everything lands here"
        ]),
        ("A name, left open", [
            "calmed, or gathered —",
            "the text does not choose"
        ]),
        ("No comment to lean on", [
            "the verse alone, this time —",
            "read with extra care"
        ]),
    ],
    further=[
        '<a href="%s/thag1.81/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.80.html">Thag 1.80 &mdash; Ugga</a> '
        "&mdash; the poem immediately before this one, closing "
        "Chapter Eight.",
        '<a href="thag-1.82.html">Thag 1.82 &mdash; Kassapa</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.82 — Kassapa
# --------------------------------------------------------------------------- #
page(
    1, 82, "Kassapa", "Kassapa",
    meta_title="Thag 1.82 — Kassapa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kassapa's verse, words of parting comfort addressed to a "
        "child rather than a first-person declaration. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative frame; a direct address, in the "
                    "imperative, to a child"),
        ("Speaker", "Unnamed; the verse does not identify who is "
                    "speaking to whom"),
        ("Form", "One four-line verse, entirely second-person "
                 "instruction"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, an unusual register"),
    ],
    why=(
        "Unlike most verses in this collection, this one is not a "
        "first-person declaration of the speaker's own path. It is "
        "entirely in the imperative, addressed to puttaka "
        "(&lsquo;child, little one&rsquo;): go wherever there is "
        "plenty of food, safety, and freedom from danger, and "
        "&lsquo;may you not be overcome by sorrow&rsquo;. No "
        "narrative explains who is speaking, or why."),
    guide=[
        ("Words spoken to a child, not about the speaker", [
            "Every verb in this poem is a second-person imperative "
            "or optative directed at &lsquo;child&rsquo; &mdash; "
            "&lsquo;go... may you not be overcome&rsquo;. This is not "
            "Kassapa describing his own attainment; it reads instead "
            "as remembered or quoted speech, attributed to him but "
            "not spoken in his own first-person voice. This "
            "collection has already shown a few instances of an "
            "elder's verse actually preserving someone else's words "
            "&mdash; Thag 1.14 (Sīvaka) opens by quoting his "
            "preceptor directly, and Thag 1.56&ndash;1.57 (the two "
            "Kuṭivihārins) are built from quoted dialogue. This verse "
            "fits that same structural pattern, though it gives no "
            "clue to who is speaking, who the child is, or the "
            "occasion."]),
        ("A blessing, not a testimony", [
            "Where most of this collection's verses declare something "
            "already achieved &mdash; freedom, insight, the end of "
            "craving &mdash; this one is entirely forward-looking and "
            "protective: a wish for someone else's safety and freedom "
            "from grief, not a report of the speaker's own state."]),
        ("A name shared very widely", [
            "Kassapa is among the most common names in the early "
            "canon &mdash; shared by the Buddha's own foremost "
            "disciple in ascetic practice, by three brothers "
            "converted early in the Buddha's ministry, and by a "
            "Buddha of a past age. Given how widely the name was "
            "carried, this reading guide treats any specific "
            "identification as considerably less likely than in cases "
            "involving rarer names, and does not attempt one."]),
    ],
    terms=[
        ("puttaka",
         "&ldquo;little child, little son&rdquo; &mdash; a "
         "diminutive of putta, the person this verse addresses."),
        ("subhikkha",
         "&ldquo;having plentiful food&rdquo; &mdash; su "
         "(&lsquo;good&rsquo;) plus bhikkha (&lsquo;alms, "
         "food&rsquo;)."),
        ("sivā",
         "&ldquo;safe, wholesome&rdquo; &mdash; describing the place "
         "the child is told to seek out."),
        ("abhaya",
         "&ldquo;free from danger, fearless&rdquo; &mdash; a (negation) "
         "plus bhaya (&lsquo;fear, danger&rsquo;)."),
        ("sokāpahata",
         "&ldquo;overcome, struck down by sorrow&rdquo; &mdash; soka "
         "(&lsquo;sorrow&rsquo;) plus āpahata (&lsquo;struck, "
         "afflicted&rsquo;)."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.82:1.1-1.4"),
    ],
    quiz=[
        {"q": "What grammatical form does nearly every verb in this verse take?",
         "opts": [
             "Second-person imperative or optative, addressed to a child",
             "First-person past tense",
             "Third-person narrative",
             "A question form"],
         "correct": 0,
         "expl": "The verse is entirely instruction directed outward, not self-description."},
        {"q": "What does the verse tell the child to seek out?",
         "opts": [
             "A place of plentiful food, safety, and freedom from danger",
             "A place of great wealth",
             "A famous teacher",
             "A distant kingdom"],
         "correct": 0,
         "expl": "Subhikkhāni, sivāni, abhayāni — the three qualities named."},
        {"q": "What two earlier poems does this reading guide compare this verse to, as examples of an elder's verse preserving someone else's quoted words?",
         "opts": [
             "Thag 1.61 Vappa and Thag 1.63 Pakkha",
             "Thag 1.71 Vacchapāla and Thag 1.72 Ātuma",
             "Thag 1.5 Dabba and Thag 1.8 Vīra",
             "Thag 1.14 Sīvaka and Thag 1.56–1.57 (the two Kuṭivihārins)"],
         "correct": 3,
         "expl": "Both preserve quoted speech rather than first-person self-testimony."},
        {"q": "Does this verse describe the speaker's own attainment, the way most verses in this collection do?",
         "opts": [
             "Yes, entirely",
             "No — it is a forward-looking blessing for someone else's safety, not a report of the speaker's own state",
             "Yes, but only in the final line",
             "The verse has no clear content at all"],
         "correct": 1,
         "expl": "An unusually protective, other-directed register."},
        {"q": "What does 'puttaka' mean?",
         "opts": [
             "A teacher",
             "A place of pilgrimage",
             "Little child, little son",
             "A type of alms bowl"],
         "correct": 2,
         "expl": "A diminutive of putta, addressed directly by the verse."},
        {"q": "How common is the name Kassapa in the early canon, according to this reading guide?",
         "opts": [
             "Extremely rare, appearing nowhere else",
             "Used only for laypeople",
             "Used only by the Buddha himself",
             "Among the most common names, shared by several well-known figures"],
         "correct": 3,
         "expl": "Shared by a chief disciple, three converted brothers, and a past Buddha."},
        {"q": "Does this reading guide attempt to identify which Kassapa this elder was?",
         "opts": [
             "Yes, definitively identifies him as the Buddha's chief disciple",
             "Yes, definitively identifies him as one of the three brothers",
             "No — given how common the name was, it treats any specific identification as unlikely",
             "Yes, definitively identifies him as the past Buddha Kassapa"],
         "correct": 2,
         "expl": "A wider name than most other same-name cases in this collection."},
        {"q": "What does 'sokāpahata' mean?",
         "opts": [
             "Freed from sorrow permanently",
             "Never having known sorrow",
             "Overcome, struck down by sorrow",
             "A cause of joy"],
         "correct": 2,
         "expl": "What the verse hopes the child will not become."},
        {"q": "Does the verse identify who is speaking or who the child is?",
         "opts": [
             "Yes, both are named explicitly",
             "Only the speaker is named",
             "Only the child is named",
             "No — the verse gives no clue to either"],
         "correct": 3,
         "expl": "No narrative frame is supplied."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The opening poem",
             "The second poem",
             "The closing poem",
             "The fifth poem"],
         "correct": 1,
         "expl": "Immediately after Samitigutta's verse, which opens the chapter."},
    ],
    marginalia=[
        ("A blessing, not a boast", [
            "go where it's safe —",
            "may sorrow not find you"
        ]),
        ("Whose words are these?", [
            "no speaker named —",
            "only the instruction"
        ]),
        ("A very common name", [
            "Kassapa, shared by many —",
            "no guess ventured here"
        ]),
        ("A child, addressed once", [
            "puttaka, little one —",
            "then the verse falls silent"
        ]),
    ],
    further=[
        '<a href="%s/thag1.82/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.14.html">Thag 1.14 &mdash; S&imacr;vaka</a> '
        "&mdash; an earlier verse that also preserves someone else's "
        "quoted words rather than first-person testimony.",
        '<a href="thag-1.81.html">Thag 1.81 &mdash; Samitigutta</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.83.html">Thag 1.83 &mdash; S&imacr;ha</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.83 — S&imacr;ha
# --------------------------------------------------------------------------- #
page(
    1, 83, "S&imacr;ha", "S&imacr;ha",
    meta_title="Thag 1.83 — Sīha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sīha's verse, a direct exhortation that names its own "
        "listener, urging tireless practice and discarding 'this bag "
        "of bones'. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative frame; a direct address, naming "
                    "its own listener"),
        ("Speaker", "Unnamed; the verse does not identify who is "
                    "urging Sīha on"),
        ("Form", "One four-line verse, entirely second-person "
                 "exhortation"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a vivid closing image"),
    ],
    why=(
        "For the second poem in a row, this verse is not first-person "
        "testimony but direct address &mdash; and unlike Thag 1.82, "
        "which spoke to an anonymous &lsquo;child&rsquo;, this one "
        "names its own listener within the verse itself: "
        "&lsquo;Meditate diligently, Sīha&rsquo;. Whoever is speaking "
        "urges him toward tireless practice, closing with a vivid "
        "instruction to &lsquo;quickly discard this bag of "
        "bones&rsquo;."),
    guide=[
        ("A verse that names its own listener", [
            "Sīhappamatto vihara, &lsquo;live diligently, Sīha&rsquo;, "
            "builds the addressee's name directly into the verse's "
            "opening compound &mdash; a different technique from "
            "Thag 1.82, which addressed an unnamed &lsquo;child&rsquo; "
            "one poem earlier. Both verses share the same underlying "
            "structure, though: entirely second-person exhortation, "
            "with no narrative frame and no identification of who is "
            "speaking."]),
        ("Whose voice is this?", [
            "This reading guide does not resolve who is urging Sīha "
            "on. Elsewhere in the wider canon, the Buddha frequently "
            "addresses individual monks directly by name in exactly "
            "this way, which would fit the pattern here &mdash; but "
            "the verse gives no attribution, and this reading guide "
            "does not assume it."]),
        ("A vivid closing image, new to this collection", [
            "Jaha sīghaṁ samussayaṁ, &lsquo;quickly discard this bag "
            "of bones&rsquo;, uses samussaya (&lsquo;heap, "
            "aggregate&rsquo;) for the body in a way not seen earlier "
            "in this collection &mdash; a blunt, physical image for "
            "letting go of the body itself, alongside this verse's "
            "more familiar call to &lsquo;develop skillful "
            "qualities&rsquo;."]),
        ("A name shared with a well-known lay donor", [
            "Sīha (&lsquo;lion&rsquo;) is also the name of General "
            "Sīha, a well-known figure already covered elsewhere on "
            "this site (AN 7.57), remembered in the wider canon for "
            "his generosity and his conversion from Jainism to the "
            "Buddha's teaching. Traditional accounts describe him "
            "remaining a lay donor rather than taking ordination, "
            "which argues against this being the same person &mdash; "
            "a more specific reason for caution than the usual "
            "&lsquo;same name, no confirmation&rsquo;, though still "
            "not a settled conclusion."]),
    ],
    terms=[
        ("appamatta",
         "&ldquo;diligent, heedful&rdquo; &mdash; built into the "
         "verse's opening address to Sīha."),
        ("rattindivaṁ",
         "&ldquo;day and night&rdquo; &mdash; ratti "
         "(&lsquo;night&rsquo;) plus divā (&lsquo;day&rsquo;), "
         "describing the pace of the practice urged."),
        ("bhāveti",
         "&ldquo;develops, cultivates&rdquo; &mdash; the verb behind "
         "this verse's instruction to develop skillful qualities."),
        ("samussaya",
         "&ldquo;heap, aggregate&rdquo; &mdash; here used for the "
         "body itself, in this verse's closing image."),
        ("Sīha",
         "&ldquo;lion&rdquo; &mdash; also the name of a well-known "
         "lay donor covered elsewhere on this site (AN 7.57)."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.83:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this verse address its listener?",
         "opts": [
             "It names him directly, within the verse's own opening compound",
             "It never mentions who is being addressed",
             "It addresses an anonymous 'child'",
             "It addresses a crowd of listeners"],
         "correct": 0,
         "expl": "Sīhappamatto vihara, 'live diligently, Sīha'."},
        {"q": "How does this differ from Thag 1.82, the poem immediately before it?",
         "opts": [
             "1.82 is a first-person testimony, unlike this one",
             "They share no similarity at all",
             "1.82 addresses an anonymous 'child'; this one names its listener directly",
             "1.82 is much longer than this verse"],
         "correct": 2,
         "expl": "Both are second-person exhortation, but this one builds the name into the verse itself."},
        {"q": "Does this reading guide identify who is speaking to Sīha?",
         "opts": [
             "Yes, definitively the Buddha",
             "Yes, definitively another monk",
             "No — it notes the Buddha's frequent use of direct address elsewhere, without assuming that applies here",
             "Yes, definitively Sīha's own family"],
         "correct": 2,
         "expl": "The verse gives no attribution."},
        {"q": "What does the verse's closing line instruct?",
         "opts": [
             "To quickly discard 'this bag of bones'",
             "To build a new hut",
             "To travel to a distant land",
             "To recite a specific formula"],
         "correct": 0,
         "expl": "Jaha sīghaṁ samussayaṁ, the verse's final image."},
        {"q": "What does 'samussaya' mean, as used in this verse?",
         "opts": [
             "A type of alms bowl",
             "The body, described as a heap or aggregate",
             "A meditation posture",
             "A monastic robe"],
         "correct": 1,
         "expl": "A blunt, physical image not seen earlier in this collection."},
        {"q": "What well-known figure shares this elder's name, according to this reading guide?",
         "opts": [
             "The Buddha's own father",
             "One of the group of five ascetics",
             "A past Buddha",
             "General Sīha, a lay donor covered elsewhere on this site (AN 7.57)"],
         "correct": 3,
         "expl": "Remembered for his generosity and conversion from Jainism."},
        {"q": "According to this reading guide, does the traditional account of General Sīha support identifying him with this elder?",
         "opts": [
             "Yes, strongly, since both are described as monks",
             "The question cannot be addressed at all",
             "Yes, because both texts explicitly confirm the connection",
             "No — traditional accounts describe General Sīha remaining a lay donor, arguing against the identification"],
         "correct": 3,
         "expl": "A more specific reason for caution than a bare 'same name, unconfirmed'."},
        {"q": "What does 'bhāveti' mean?",
         "opts": [
             "Develops, cultivates",
             "Abandons, discards",
             "Remembers, recalls",
             "Teaches, instructs"],
         "correct": 0,
         "expl": "The verb behind the instruction to develop skillful qualities."},
        {"q": "What does 'rattindivaṁ' mean?",
         "opts": [
             "Morning and evening",
             "Once a year",
             "Never",
             "Day and night"],
         "correct": 3,
         "expl": "Ratti ('night') plus divā ('day')."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The opening poem",
             "The third poem",
             "The closing poem",
             "The seventh poem"],
         "correct": 1,
         "expl": "Immediately after Kassapa's verse."},
    ],
    marginalia=[
        ("A name, spoken aloud", [
            "Sīha, by name —",
            "urged on, day and night"
        ]),
        ("A bag of bones, discarded", [
            "quickly, the verse says —",
            "a new image, this time"
        ]),
        ("Whose voice, unnamed", [
            "urging, not testifying —",
            "the speaker left out"
        ]),
        ("A lion, a lay donor", [
            "same name, different life —",
            "the record argues against it"
        ]),
    ],
    further=[
        '<a href="%s/thag1.83/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../anguttara-nikaya/an-7.57.html">AN 7.57 &mdash; '
        "General Sīha</a> &mdash; a well-known lay donor sharing this "
        "elder's name, though traditional accounts argue against "
        "identifying the two.",
        '<a href="thag-1.82.html">Thag 1.82 &mdash; Kassapa</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.84.html">Thag 1.84 &mdash; N&imacr;ta</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.84 — N&imacr;ta
# --------------------------------------------------------------------------- #
page(
    1, 84, "N&imacr;ta", "N&imacr;ta",
    meta_title="Thag 1.84 — Nīta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Nīta's verse, a rhetorical question about 'the simpleton' "
        "who sleeps all night and socializes all day. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative frame; a rhetorical question about "
                    "an unnamed 'simpleton'"),
        ("Speaker", "Unnamed; this reading guide does not resolve "
                    "whether the question is self-directed or a "
                    "general critique"),
        ("Form", "One four-line verse, building to a rhetorical "
                 "question"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a pointed question"),
    ],
    why=(
        "For the third poem in a row, this verse doesn't declare the "
        "speaker's own attainment. Where Thag 1.82 addressed a "
        "child and Thag 1.83 addressed Sīha directly, this one asks a "
        "rhetorical question about &lsquo;the simpleton&rsquo; who "
        "sleeps all night and happily socializes all day: "
        "&lsquo;when will he make an end of suffering?&rsquo;"),
    guide=[
        ("A rhetorical question, aimed where?", [
            "The verse describes a pattern &mdash; sleeping through "
            "the night, then happily &lsquo;socializing&rsquo; "
            "(saṅgaṇike rato) through the day &mdash; and asks when "
            "someone living this way will ever end suffering. This "
            "reading guide does not resolve whether &lsquo;the "
            "simpleton&rsquo; is a self-directed reproach, perhaps "
            "recalling Nīta's own habits before he took practice "
            "seriously, or a general observation aimed outward. The "
            "verse's own wording supports either reading."]),
        ("A third non-testimonial voice in a row", [
            "This is the third consecutive poem in Chapter Nine that "
            "isn't first-person declaration of the speaker's own "
            "state: Thag 1.82 addressed a child, Thag 1.83 addressed "
            "Sīha by name, and this one poses a rhetorical question "
            "about an unnamed figure. Three poems running without a "
            "first-person testimony is an unusual concentration for "
            "this collection, though this reading guide does not "
            "claim the pattern was deliberately arranged."]),
        ("A related warning, earlier in the collection", [
            "Thag 1.17 (Dāsaka), much earlier in this collection, "
            "used a different image &mdash; a stuffed hog rolling in "
            "its pen &mdash; to warn against sloth and overeating "
            "leading back to rebirth. This verse's target is the same "
            "general failing, sleep and idle sociability standing in "
            "for the hog's gluttony, though the two verses are not "
            "otherwise connected."]),
    ],
    terms=[
        ("supati",
         "&ldquo;sleeps&rdquo; &mdash; the first half of the pattern "
         "this verse describes."),
        ("saṅgaṇika",
         "&ldquo;fond of company, socializing&rdquo; &mdash; the "
         "second half of the pattern, filling the daytime hours."),
        ("dummedha",
         "&ldquo;fool, simpleton&rdquo; &mdash; du "
         "(&lsquo;bad&rsquo;) plus medhā (&lsquo;wisdom, "
         "intelligence&rsquo;)."),
        ("dukkhassanta",
         "&ldquo;end of suffering&rdquo; &mdash; dukkha "
         "(&lsquo;suffering&rsquo;) plus anta (&lsquo;end&rsquo;), "
         "what the simpleton is asked when he will reach."),
        ("Nīta",
         "&ldquo;led, guided&rdquo; &mdash; the past participle of "
         "neti, &lsquo;to lead&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.84:1.1-1.4"),
    ],
    quiz=[
        {"q": "What pattern of behavior does this verse describe?",
         "opts": [
             "Sleeping all night and happily socializing all day",
             "Meditating tirelessly day and night",
             "Traveling constantly from place to place",
             "Fasting for long periods"],
         "correct": 0,
         "expl": "The pattern the verse's rhetorical question is aimed at."},
        {"q": "What question does the verse ask about this pattern?",
         "opts": [
             "Whether it leads to wealth",
             "When the simpleton will make an end of suffering",
             "Whether it is permitted by monastic rules",
             "How long it can be sustained"],
         "correct": 1,
         "expl": "Kudāssu nāma dummedho, dukkhassantaṁ karissatī, the verse's closing question."},
        {"q": "Does this reading guide resolve whether 'the simpleton' refers to the speaker himself or someone else?",
         "opts": [
             "Yes, definitively the speaker himself",
             "Yes, definitively someone else",
             "No — the verse's wording supports either reading",
             "The verse names the simpleton explicitly"],
         "correct": 2,
         "expl": "A genuine ambiguity the text does not settle."},
        {"q": "How many consecutive poems in Chapter Nine, including this one, are not first-person declarations of the speaker's own state?",
         "opts": [
             "Just this one",
             "Two",
             "All ten poems in the chapter",
             "Three — Thag 1.82, 1.83, and 1.84"],
         "correct": 3,
         "expl": "An unusual concentration of non-testimonial verses."},
        {"q": "What does 'saṅgaṇika' mean?",
         "opts": [
             "Fond of company, socializing",
             "Solitary, withdrawn",
             "Sleeping",
             "Traveling"],
         "correct": 0,
         "expl": "Filling the daytime half of the pattern the verse describes."},
        {"q": "What does 'dummedha' mean?",
         "opts": [
             "A wise teacher",
             "A skilled meditator",
             "Fool, simpleton",
             "A generous donor"],
         "correct": 2,
         "expl": "Du ('bad') plus medhā ('wisdom')."},
        {"q": "What earlier poem in this collection does this reading guide compare to this verse, as a related warning against sloth?",
         "opts": [
             "Thag 1.17 Dāsaka, using a stuffed hog rolling in its pen",
             "Thag 1.61 Vappa",
             "Thag 1.71 Vacchapāla",
             "Thag 1.5 Dabba"],
         "correct": 0,
         "expl": "A different image aimed at the same general failing."},
        {"q": "What does the name Nīta literally mean?",
         "opts": [
             "Protected, guarded",
             "Led, guided",
             "Given by the lord",
             "Ram's head"],
         "correct": 1,
         "expl": "The past participle of neti, 'to lead'."},
        {"q": "What does 'dukkhassanta' mean?",
         "opts": [
             "The beginning of suffering",
             "A type of meditation",
             "A monastic rule",
             "End of suffering"],
         "correct": 3,
         "expl": "Dukkha ('suffering') plus anta ('end')."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The eighth poem",
             "The fourth poem"],
         "correct": 3,
         "expl": "Immediately after Sīha's verse."},
    ],
    marginalia=[
        ("A pattern, described plainly", [
            "sleeping through the night —",
            "socializing all day"
        ]),
        ("A question, left open", [
            "the simpleton, who? —",
            "himself, or someone else"
        ]),
        ("A third voice, not testimony", [
            "child, then Sīha, then this —",
            "no self-report yet"
        ]),
        ("An old warning, echoed", [
            "a hog once rolled in its pen —",
            "now sleep, and idle talk"
        ]),
    ],
    further=[
        '<a href="%s/thag1.84/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.17.html">Thag 1.17 &mdash; D&amacr;saka</a> '
        "&mdash; an earlier warning against sloth, using a different "
        "image for the same general failing.",
        '<a href="thag-1.83.html">Thag 1.83 &mdash; S&imacr;ha</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.85.html">Thag 1.85 &mdash; Sun&amacr;ga</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.85 — Sun&amacr;ga
# --------------------------------------------------------------------------- #
page(
    1, 85, "Sun&amacr;ga", "Sun&amacr;ga",
    meta_title="Thag 1.85 — Sunāga | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sunāga's verse, a general teaching on the qualities leading "
        "to 'pleasure not of the flesh' — the fourth poem in a row in "
        "this chapter without first-person testimony. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 5 of 10",
    glance=[
        ("Setting", "No narrative setting; a general, hypothetical "
                    "teaching about a type of practitioner"),
        ("Speaker", "An unnamed voice describing, in the third "
                    "person, what such a person would realize"),
        ("Form", "One four-line verse, listing qualities that lead "
                 "to a stated outcome"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one doctrinal category"),
    ],
    why=(
        "This verse describes, in the third person, a person skilled "
        "in the mind's patterns, who understands the relish of "
        "seclusion and practices absorption, mindful and alert "
        "&mdash; such a person, it says, would realize &lsquo;pleasure "
        "not of the flesh&rsquo;. It is the fourth poem in a row in "
        "this chapter that isn't first-person testimony, though of a "
        "different kind than the three before it."),
    guide=[
        ("Four qualities, one outcome", [
            "The verse names four qualities in sequence &mdash; "
            "skilled in the mind's patterns (cittanimittassa kovido), "
            "understanding the relish of seclusion (pavivekarasaṁ "
            "vijāniya), practicing absorption, and being both prudent "
            "and mindful (nipako patissato) &mdash; before concluding "
            "that such a person would realize &lsquo;pleasure not of "
            "the flesh&rsquo; (sukhaṁ nirāmisaṁ). The whole verse is a "
            "single hypothetical: a description of the kind of person "
            "who reaches this outcome, not a first-person report that "
            "the speaker has reached it himself."]),
        ("A fourth non-testimonial poem, but a different kind", [
            "Thag 1.82 addressed a child, Thag 1.83 addressed Sīha "
            "by name, and Thag 1.84 posed a rhetorical question about "
            "an unnamed &lsquo;simpleton&rsquo; &mdash; none of them "
            "first-person declarations. This verse extends that run "
            "to four poems, but shifts register again: rather than "
            "address or rhetorical question, it is a general, "
            "hypothetical teaching in the third person, closer in "
            "kind to Thag 1.71 and Thag 1.74 from the chapter before "
            "this one."]),
        ("'Pleasure not of the flesh', a standard category", [
            "Nirāmisa sukha (&lsquo;pleasure not of the "
            "flesh&rsquo;) is a well-known doctrinal category "
            "throughout the wider canon, distinguished from sāmisa "
            "sukha, ordinary pleasure tied to sense experience and "
            "material things. This verse doesn't unpack the "
            "distinction &mdash; it simply names the outcome &mdash; "
            "in the same unglossed way earlier verses in this "
            "collection have relied on standard categories like the "
            "five hindrances (Thag 1.74) without spelling them out."]),
        ("A name sharing a root with the poem that follows", [
            "Sunāga reads as su (&lsquo;good&rsquo;) plus nāga, which "
            "can mean either &lsquo;elephant&rsquo; or "
            "&lsquo;serpent, dragon&rsquo; in Pali. The very next poem "
            "in this chapter, Thag 1.86, belongs to an elder named "
            "Nāgita &mdash; sharing the same root. This reading guide "
            "notes the adjacency without asserting it reflects any "
            "deliberate arrangement."]),
    ],
    terms=[
        ("nimitta",
         "&ldquo;sign, pattern, feature&rdquo; &mdash; here, the "
         "patterns of the mind this verse says a skilled person "
         "reads."),
        ("paviveka",
         "&ldquo;seclusion, solitude&rdquo; &mdash; whose "
         "&lsquo;relish&rsquo; (rasa) this verse says such a person "
         "comes to understand."),
        ("rasa",
         "&ldquo;taste, flavor, nectar&rdquo; &mdash; used here "
         "metaphorically for what seclusion offers to one who "
         "understands it."),
        ("nirāmisa",
         "&ldquo;not of the flesh&rdquo; &mdash; a (negation) plus "
         "āmisa (&lsquo;flesh, material things&rsquo;), describing a "
         "pleasure not tied to sense experience."),
        ("Sunāga",
         "&ldquo;good elephant&rdquo; or &ldquo;good serpent&rdquo; "
         "&mdash; su (&lsquo;good&rsquo;) plus nāga, a word carrying "
         "both senses in Pali."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.85:1.1-1.4"),
    ],
    quiz=[
        {"q": "What four qualities does this verse say lead to 'pleasure not of the flesh'?",
         "opts": [
             "Generosity, patience, courage, and faith",
             "Old age, sickness, death, and renunciation",
             "Sleep, socializing, food, and rest",
             "Being skilled in the mind's patterns, understanding seclusion's relish, absorption, and mindfulness"],
         "correct": 3,
         "expl": "The verse's own four-part list."},
        {"q": "What does 'nirāmisa' mean?",
         "opts": [
             "Not of the flesh, not tied to sense experience",
             "Full of sensory delight",
             "Related to food",
             "Related to wealth"],
         "correct": 0,
         "expl": "A (negation) plus āmisa ('flesh, material things')."},
        {"q": "What grammatical form does the verse's concluding verb, 'adhigaccheyya', take?",
         "opts": [
             "First-person past tense",
             "Third-person optative — 'such a person would realize'",
             "Second-person imperative",
             "A question form"],
         "correct": 1,
         "expl": "A hypothetical description, not a first-person report."},
        {"q": "How many consecutive poems in Chapter Nine, including this one, are not first-person testimony?",
         "opts": [
             "Just this one",
             "Two",
             "Four — Thag 1.82 through 1.85",
             "All ten poems in the chapter"],
         "correct": 2,
         "expl": "An unusual run extending across most of the chapter's first half."},
        {"q": "How does this poem's kind of non-testimonial voice differ from the three poems before it?",
         "opts": [
             "It is identical in kind to all three",
             "It is a dialogue between two speakers",
             "It is written entirely in riddle form",
             "It is a general, hypothetical teaching, unlike the direct address or rhetorical question of the poems before it"],
         "correct": 3,
         "expl": "Closer in kind to Thag 1.71 and Thag 1.74 from the previous chapter."},
        {"q": "What does 'nimitta' mean?",
         "opts": [
             "Sign, pattern, feature",
             "A place of pilgrimage",
             "A monastic robe",
             "A type of alms bowl"],
         "correct": 0,
         "expl": "Here, the patterns of the mind a skilled person reads."},
        {"q": "What does 'paviveka' mean?",
         "opts": [
             "Wealth, prosperity",
             "Seclusion, solitude",
             "A crowd, an assembly",
             "A kind of illness"],
         "correct": 1,
         "expl": "Whose 'relish' this verse says such a person comes to understand."},
        {"q": "What does the name Sunāga mean?",
         "opts": [
             "One who has given up what is dear",
             "Ram's head",
             "Good elephant, or good serpent",
             "Son of an elephant-rider"],
         "correct": 2,
         "expl": "Su ('good') plus nāga, a word meaning either animal in Pali."},
        {"q": "What does this reading guide note about the name of the poem immediately following this one, Thag 1.86?",
         "opts": [
             "It has nothing in common with this poem's name",
             "It belongs to an elder also from Chapter Two",
             "It is identical in meaning to Sunāga",
             "It belongs to an elder named Nāgita, sharing the same 'nāga' root"],
         "correct": 3,
         "expl": "Noted as an adjacency, without asserting deliberate design."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The fifth poem",
             "The opening poem",
             "The closing poem",
             "The ninth poem"],
         "correct": 0,
         "expl": "Midway through the chapter's ten poems."},
    ],
    marginalia=[
        ("Four qualities, named", [
            "skilled in the mind's signs —",
            "seclusion's own relish"
        ]),
        ("Not of the flesh", [
            "a pleasure named, not felt —",
            "a category, plainly stated"
        ]),
        ("A fourth voice, still not testimony", [
            "child, Sīha, simpleton —",
            "now, a general teaching"
        ]),
        ("A root, shared ahead", [
            "good elephant, this poem —",
            "the next one, too"
        ]),
    ],
    further=[
        '<a href="%s/thag1.85/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.74.html">Thag 1.74 &mdash; Suy&amacr;mana</a> '
        "&mdash; an earlier general teaching verse in the same "
        "third-person register as this one.",
        '<a href="thag-1.84.html">Thag 1.84 &mdash; N&imacr;ta</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.86.html">Thag 1.86 &mdash; N&amacr;gita</a> '
        "&mdash; the next poem in this chapter, whose name shares "
        "this one's 'nāga' root.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.86 — N&amacr;gita
# --------------------------------------------------------------------------- #
page(
    1, 86, "N&amacr;gita", "N&amacr;gita",
    meta_title="Thag 1.86 — Nāgita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Nāgita's verse praising the Buddha's transparent teaching, "
        "echoing his famous denial of any 'closed fist' in the "
        "Dīgha Nikāya. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 6 of 10",
    glance=[
        ("Setting", "No narrative setting; a claim about other "
                    "doctrines, then praise of the Buddha's own "
                    "transparency"),
        ("Speaker", "An unnamed voice, describing the Buddha's "
                    "teaching in the third person"),
        ("Form", "One four-line verse, in two halves"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one notable canonical echo"),
    ],
    why=(
        "This verse claims that other doctrines exist, but don't lead "
        "to extinguishment the way this one does &mdash; and closes "
        "by praising how the Buddha teaches the Saṅgha: &lsquo;the "
        "Teacher shows the palms of his hands&rsquo;, an image that "
        "closely echoes the Buddha's own famous words elsewhere in "
        "the canon about withholding nothing from his students."),
    guide=[
        ("Many paths, one that leads to extinguishment", [
            "The verse's first half makes an exclusivity claim: "
            "&lsquo;elsewhere there are many other doctrines&rsquo; "
            "(puthu aññavādinaṁ), but their paths, unlike this one, "
            "don't lead to nibbāna. The verse doesn't argue the point "
            "or name any rival teaching &mdash; it simply asserts the "
            "distinction before turning to why."]),
        ("An echo of the Buddha's own words on withholding nothing", [
            "&lsquo;The Teacher shows the palms of his hands&rsquo; "
            "(satthā sayaṁ pāṇitaleva dassayaṁ) closely echoes a "
            "passage in this site's own DN 16 (§2.25), where the "
            "Buddha tells Ānanda directly: &lsquo;The Realized One "
            "doesn't have the closed fist of a tutor when it comes to "
            "the teachings&rsquo; &mdash; no secret, no held-back "
            "portion kept from his students. This verse's open-palms "
            "image is the same claim turned into a physical gesture: "
            "hands opened rather than a fist closed."]),
        ("A fifth non-testimonial poem, in yet another register", [
            "Thag 1.82 through 1.85 were, in turn, an address to a "
            "child, an address to Sīha, a rhetorical question, and a "
            "general teaching about practitioners &mdash; none of "
            "them first-person testimony. This verse extends that run "
            "to five poems, shifting register once more: praise of "
            "the Buddha's own transparency as a teacher, rather than "
            "instruction aimed at anyone in particular."]),
        ("A name possibly belonging to the Buddha's own attendant", [
            "Nāgita is also the name of a monk who appears as the "
            "Buddha's personal attendant in two suttas already "
            "translated on this site, AN 5.30 and AN 6.42, both "
            "titled &lsquo;With Nāgita&rsquo;. The name is less "
            "common than some other cases in this collection, and "
            "this verse's content &mdash; praise for how openly the "
            "Buddha teaches the Saṅgha &mdash; would fit naturally "
            "with an attendant's vantage point. Still, without a "
            "comment confirming it, this reading guide notes the "
            "connection as plausible rather than settled."]),
    ],
    terms=[
        ("aññavādin",
         "&ldquo;an exponent of another doctrine&rdquo; &mdash; "
         "añña (&lsquo;other&rsquo;) plus vādin (&lsquo;one who "
         "asserts, a proponent&rsquo;)."),
        ("nibbānagama",
         "&ldquo;leading to extinguishment&rdquo; &mdash; describing "
         "what this verse says other paths do not do."),
        ("anusāsati",
         "&ldquo;instructs, teaches&rdquo; &mdash; the verb "
         "describing the Buddha's own action toward the Saṅgha."),
        ("pāṇitala",
         "&ldquo;the palm of the hand&rdquo; &mdash; pāṇi "
         "(&lsquo;hand&rsquo;) plus tala (&lsquo;surface, "
         "palm&rsquo;), the image this verse closes on."),
        ("ācariyamuṭṭhi",
         "&ldquo;the closed fist of a tutor&rdquo; &mdash; the "
         "concept the Buddha explicitly denies having, in this site's "
         "own DN 16 (&sect;2.25), that this verse's open-palms image "
         "echoes."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.86:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's first half claim about other doctrines?",
         "opts": [
             "They are identical to this one",
             "They lead to extinguishment just as effectively",
             "They exist, but their paths don't lead to extinguishment the way this one does",
             "They do not exist at all"],
         "correct": 2,
         "expl": "Puthu aññavādinaṁ, maggo na nibbānagamo yathā ayaṁ."},
        {"q": "What image closes this verse?",
         "opts": [
             "The Teacher showing the palms of his hands",
             "A closed fist held up",
             "A begging bowl held out",
             "A robe being folded"],
         "correct": 0,
         "expl": "Satthā sayaṁ pāṇitaleva dassayaṁ, the verse's final image."},
        {"q": "What passage on this site does this verse's closing image closely echo?",
         "opts": [
             "MN 145, Advice to Puṇṇa",
             "DN 16 §2.25, where the Buddha denies having any 'closed fist of a tutor'",
             "SN 4.23, With Godhika",
             "AN 9.3, With Meghiya"],
         "correct": 1,
         "expl": "The same claim of withholding nothing, expressed as open hands rather than a closed fist."},
        {"q": "What does the Buddha say about his teaching in DN 16 §2.25, as quoted in this reading guide?",
         "opts": [
             "That he teaches only his closest disciples",
             "That he has withheld certain advanced teachings",
             "That his teaching will be lost after his death",
             "That he has no closed fist of a tutor when it comes to the teachings"],
         "correct": 3,
         "expl": "No secret, no held-back portion kept from his students."},
        {"q": "How many consecutive poems in Chapter Nine, including this one, are not first-person testimony?",
         "opts": [
             "Two",
             "Three",
             "Four",
             "Five — Thag 1.82 through 1.86"],
         "correct": 3,
         "expl": "Each in a different register: address, address, rhetorical question, general teaching, and now praise of the Buddha."},
        {"q": "What does 'aññavādin' mean?",
         "opts": [
             "An exponent of another doctrine",
             "A skilled meditator",
             "A generous donor",
             "A monastic elder"],
         "correct": 0,
         "expl": "Añña ('other') plus vādin ('one who asserts')."},
        {"q": "What does 'pāṇitala' mean?",
         "opts": [
             "A monk's robe",
             "The palm of the hand",
             "A begging bowl",
             "A meditation seat"],
         "correct": 1,
         "expl": "Pāṇi ('hand') plus tala ('surface, palm')."},
        {"q": "What does this reading guide say about identifying this elder with the Buddha's attendant Nāgita from AN 5.30 and AN 6.42?",
         "opts": [
             "It is definitively confirmed by a Sujato comment",
             "It is definitively ruled out",
             "It notes the connection as plausible, given the less common name and fitting content, but not settled",
             "The two suttas never mention anyone named Nāgita"],
         "correct": 2,
         "expl": "A more favorable case than most 'same name' instances, but still not confirmed."},
        {"q": "What does 'anusāsati' mean?",
         "opts": [
             "Abandons, forsakes",
             "Travels, wanders",
             "Sleeps, rests",
             "Instructs, teaches"],
         "correct": 3,
         "expl": "Describing the Buddha's own action toward the Saṅgha."},
        {"q": "What does 'nibbānagama' mean?",
         "opts": [
             "Leading to extinguishment",
             "Leading to further rebirth",
             "Leading to wealth",
             "Leading to fame"],
         "correct": 0,
         "expl": "What this verse says other paths do not do."},
    ],
    marginalia=[
        ("Many paths, one true one", [
            "other doctrines, elsewhere —",
            "none reaching the goal"
        ]),
        ("A fist unclenched", [
            "open hands, not held back —",
            "the same claim, elsewhere made"
        ]),
        ("A fifth voice, still not testimony", [
            "child, Sīha, simpleton, teaching —",
            "now, praise for the Teacher"
        ]),
        ("An attendant's view, perhaps", [
            "close enough to see —",
            "hands opened, nothing hidden"
        ]),
    ],
    further=[
        '<a href="%s/thag1.86/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../digha-nikaya/dn-16.html">DN 16</a> '
        "&mdash; &sect;2.25, where the Buddha denies having any "
        "&lsquo;closed fist of a tutor&rsquo;, closely echoed by "
        "this verse's open-palms image.",
        '<a href="../anguttara-nikaya/an-5.30.html">AN 5.30 &mdash; '
        "With N&amacr;gita</a> &mdash; a sutta naming the Buddha's "
        "attendant Nāgita, possibly this same elder.",
        '<a href="thag-1.85.html">Thag 1.85 &mdash; Sun&amacr;ga</a> '
        "&mdash; the poem immediately before this one, sharing this "
        "elder's 'nāga' root.",
        '<a href="thag-1.87.html">Thag 1.87 &mdash; Pavi&#7789;&#7789;ha</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.87 — Pavi&#7789;&#7789;ha
# --------------------------------------------------------------------------- #
page(
    1, 87, "Pavi&#7789;&#7789;ha", "Pavi&#7789;&#7789;ha",
    meta_title="Thag 1.87 — Paviṭṭha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Paviṭṭha's verse, declaring the aggregates seen as they "
        "truly are, closing with the same exact couplet as an "
        "earlier poem from Chapter Seven. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A retrospective declaration of the aggregates "
                    "seen and rebirth ended"),
        ("Speaker", "Paviṭṭha, in the first person"),
        ("Form", "One four-line verse, closing on a couplet shared "
                 "with an earlier poem"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one well-known category"),
    ],
    why=(
        "Paviṭṭha declares the five aggregates seen as they truly "
        "are, all rebirths shattered, transmigration finished. Its "
        "closing two lines &mdash; &lsquo;transmigration through "
        "births is finished, now there'll be no more future "
        "lives&rsquo; &mdash; are word for word identical to the "
        "closing of Thag 1.67 (Ekadhammasavanīya), from Chapter "
        "Seven."),
    guide=[
        ("A closing couplet shared with Chapter Seven", [
            "Vikkhīṇo jātisaṁsāro, natthi dāni punabbhavo, this "
            "verse's final two lines, match Thag 1.67's closing "
            "exactly, in both Pali and Sujato's English. The line "
            "before it shows a partial echo too: both verses open "
            "their second line with bhavā sabbe (&lsquo;all "
            "rebirths&rsquo;), though each finishes with a different "
            "verb &mdash; 1.67 says they are samūhatā "
            "(&lsquo;eradicated&rsquo;), this verse says padālitā "
            "(&lsquo;shattered&rsquo;)."]),
        ("Aggregates seen as they truly are", [
            "Khandhā diṭṭhā yathābhūtaṁ opens the verse: the five "
            "aggregates (form, feeling, perception, formations, and "
            "consciousness &mdash; the standard components the "
            "canon analyzes a person into) seen &lsquo;as they truly "
            "are&rsquo; (yathābhūta), a common epistemic phrase "
            "throughout the wider canon for seeing something without "
            "distortion. The verse doesn't unpack the five "
            "aggregates individually &mdash; it simply names the "
            "outcome of having seen them clearly."]),
        ("A name meaning 'entered'", [
            "Paviṭṭha is the past participle of pavisati "
            "(&lsquo;to enter&rsquo;) &mdash; a plain, transparent "
            "name. This reading guide does not press any further "
            "connection between the name and the verse's content "
            "beyond noting its literal meaning."]),
    ],
    terms=[
        ("khandha",
         "&ldquo;aggregate&rdquo; &mdash; one of the five standard "
         "components (form, feeling, perception, formations, "
         "consciousness) the canon analyzes a person into."),
        ("yathābhūta",
         "&ldquo;as it truly is&rdquo; &mdash; a common epistemic "
         "phrase for seeing something without distortion."),
        ("padālita",
         "&ldquo;shattered, split open&rdquo; &mdash; describing "
         "this verse's own account of what has happened to all "
         "rebirths."),
        ("bhava",
         "&ldquo;existence, a state of being&rdquo; &mdash; shared "
         "vocabulary between this verse and Thag 1.67's closing "
         "couplet."),
        ("Paviṭṭha",
         "&ldquo;entered&rdquo; &mdash; the past participle of "
         "pavisati, &lsquo;to enter&rsquo;."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.87:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse say has been seen 'as it truly is'?",
         "opts": [
             "The five aggregates",
             "The four noble truths",
             "The three roots of unwholesomeness",
             "The five hindrances"],
         "correct": 0,
         "expl": "Khandhā diṭṭhā yathābhūtaṁ, the verse's opening line."},
        {"q": "What earlier poem does this verse's closing couplet match word for word?",
         "opts": [
             "Thag 1.61 Vappa",
             "Thag 1.67 Ekadhammasavanīya",
             "Thag 1.71 Vacchapāla",
             "Thag 1.15 Kuṇḍadhāna"],
         "correct": 1,
         "expl": "Both close with 'Vikkhīṇo jātisaṁsāro, natthi dāni punabbhavo'."},
        {"q": "Do the two verses' second lines also match exactly?",
         "opts": [
             "Yes, completely",
             "No, they share no vocabulary at all",
             "They share the opening words 'bhavā sabbe', but end with different verbs",
             "Only the Pali matches; the English translations differ entirely"],
         "correct": 2,
         "expl": "Samūhatā ('eradicated') in Thag 1.67 versus padālitā ('shattered') here."},
        {"q": "What does 'yathābhūta' mean?",
         "opts": [
             "As it truly is",
             "As it used to be",
             "As it will become",
             "As it is imagined"],
         "correct": 0,
         "expl": "A common epistemic phrase throughout the wider canon."},
        {"q": "What does 'padālita' mean?",
         "opts": [
             "Cultivated, developed",
             "Remembered, recalled",
             "Concealed, hidden",
             "Shattered, split open"],
         "correct": 3,
         "expl": "Describing what has happened to all rebirths, according to this verse."},
        {"q": "What does the name Paviṭṭha mean?",
         "opts": [
             "Entered",
             "Departed",
             "Protected",
             "Given"],
         "correct": 0,
         "expl": "The past participle of pavisati, 'to enter'."},
        {"q": "How many standard aggregates does the canon analyze a person into?",
         "opts": [
             "Three",
             "Four",
             "Five",
             "Seven"],
         "correct": 2,
         "expl": "Form, feeling, perception, formations, and consciousness."},
        {"q": "Does this verse individually unpack each of the five aggregates?",
         "opts": [
             "Yes, in detail",
             "No — it simply names the outcome of having seen them clearly",
             "It unpacks only two of the five",
             "It replaces the five aggregates with a different list"],
         "correct": 1,
         "expl": "The verse relies on the category without spelling it out, as several earlier verses in this collection also do."},
        {"q": "What does the verse's closing line declare about future lives?",
         "opts": [
             "There will be exactly one more",
             "They are uncertain",
             "They will continue indefinitely",
             "There will be no more of them"],
         "correct": 3,
         "expl": "Natthi dāni punabbhavo, the verse's final words."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The third poem",
             "The seventh poem"],
         "correct": 3,
         "expl": "Immediately after Nāgita's verse."},
    ],
    marginalia=[
        ("Aggregates, seen truly", [
            "form, feeling, perception —",
            "no distortion left"
        ]),
        ("A couplet, spoken twice", [
            "the same two lines —",
            "a chapter apart"
        ]),
        ("Shattered, not eradicated", [
            "one word differs —",
            "the ending, still the same"
        ]),
        ("A name, plainly entered", [
            "past the threshold —",
            "no further reading pressed"
        ]),
    ],
    further=[
        '<a href="%s/thag1.87/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.67.html">Thag 1.67 &mdash; '
        "Ekadhammasavan&imacr;ya</a> &mdash; an earlier poem from "
        "Chapter Seven, closing with the exact same couplet as this "
        "one.",
        '<a href="thag-1.86.html">Thag 1.86 &mdash; N&amacr;gita</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.88.html">Thag 1.88 &mdash; Ajjuna</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.88 — Ajjuna
# --------------------------------------------------------------------------- #
page(
    1, 88, "Ajjuna", "Ajjuna",
    meta_title="Thag 1.88 — Ajjuna | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Ajjuna's verse, an extended flood-and-rescue image where "
        "insight breaks through in the middle of the crisis, not "
        "after it. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 8 of 10",
    glance=[
        ("Setting", "A retrospective account, told through an "
                    "extended flood-and-rescue image"),
        ("Speaker", "Ajjuna, in the first person"),
        ("Form", "One four-line verse, a single continuous image"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one notable structural "
                       "detail"),
    ],
    why=(
        "Ajjuna describes lifting himself from water to shore while "
        "&lsquo;being swept away by the great flood&rsquo; &mdash; "
        "and in that same moment, still being swept along, he says he "
        "&lsquo;penetrated the truths&rsquo;. The insight doesn't "
        "come after the crisis is over; the verse places it in the "
        "middle of it."),
    guide=[
        ("Insight in the middle of the flood, not after", [
            "Vuyhamāno mahogheva, saccāni paṭivijjhahaṁ: "
            "&lsquo;while being swept along by the great flood, I "
            "penetrated the truths&rsquo;. Vuyhamāno is a present "
            "participle &mdash; the sweeping is still happening, "
            "ongoing, at the moment the verse describes the "
            "breakthrough. This is a different temporal structure "
            "from a more conventional telling, where crisis would "
            "come first, followed by escape, followed by insight: "
            "here the insight and the peril coincide."]),
        ("Ogha, a standard image for what sweeps beings along", [
            "Ogha (&lsquo;flood&rsquo;) is one of the wider canon's "
            "standard images for what carries beings through "
            "saṁsāra &mdash; traditionally enumerated as four: the "
            "floods of sensuality, of continued existence, of views, "
            "and of ignorance. This verse doesn't specify which, or "
            "how many; it simply names &lsquo;the great flood&rsquo; "
            "as the thing being escaped."]),
        ("'The truths', left unspecified", [
            "Saccāni (&lsquo;truths&rsquo;) most likely points toward "
            "the four noble truths, the canon's most common referent "
            "for this word in the plural &mdash; but the verse itself "
            "doesn't say &lsquo;four&rsquo;, or name them "
            "individually. This reading guide treats the likely "
            "referent as background, not something the verse itself "
            "confirms."]),
        ("A name that may mean 'bright, white'", [
            "Ajjuna can also function as an ordinary adjective "
            "meaning &lsquo;white, bright, clear&rsquo; &mdash; it is "
            "also the name of a tree valued for its pale bark. "
            "Whether this elder's name draws on that sense, this "
            "reading guide does not press further."]),
    ],
    terms=[
        ("ogha",
         "&ldquo;flood&rdquo; &mdash; a standard canonical image for "
         "what sweeps beings through saṁsāra, traditionally counted "
         "as four."),
        ("vuyhamāna",
         "&ldquo;being swept away&rdquo; &mdash; a present passive "
         "participle, describing an action still underway."),
        ("paṭivijjhati",
         "&ldquo;penetrates, breaks through to understanding&rdquo; "
         "&mdash; the verb behind this verse's central claim."),
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; here in the plural, most likely "
         "pointing toward the four noble truths, though the verse "
         "does not name them individually."),
        ("Ajjuna",
         "possibly &ldquo;white, bright, clear&rdquo; &mdash; also "
         "the name of a tree valued for its pale bark."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.88:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse say Ajjuna was able to do?",
         "opts": [
             "Lift himself from the water to the shore",
             "Build a raft",
             "Call for help",
             "Sink beneath the flood"],
         "correct": 0,
         "expl": "Asakkhiṁ vata attānaṁ, uddhātuṁ udakā thalaṁ, the verse's opening claim."},
        {"q": "When, according to the verse, did Ajjuna 'penetrate the truths'?",
         "opts": [
             "Before entering the flood",
             "While still being swept along by the flood",
             "Long after reaching the shore",
             "The verse doesn't connect the two events at all"],
         "correct": 1,
         "expl": "Vuyhamāno mahogheva, saccāni paṭivijjhahaṁ — the insight coincides with the peril."},
        {"q": "What grammatical form is 'vuyhamāno', and what does it indicate about the timing?",
         "opts": [
             "A past tense verb, indicating the sweeping had already ended",
             "A future tense verb, indicating the sweeping had not yet begun",
             "An imperative, addressed to someone else",
             "A present participle, indicating the sweeping was still ongoing"],
         "correct": 3,
         "expl": "The breakthrough happens in the middle of the crisis, not after it."},
        {"q": "How many floods (ogha) does the wider canon traditionally enumerate?",
         "opts": [
             "Two",
             "Three",
             "Four",
             "Six"],
         "correct": 2,
         "expl": "Sensuality, continued existence, views, and ignorance."},
        {"q": "Does this verse specify which flood, or how many, it refers to?",
         "opts": [
             "Yes, it names all four explicitly",
             "Yes, it names exactly one",
             "No — it simply names 'the great flood' without specifying",
             "It says there is no flood at all"],
         "correct": 2,
         "expl": "The verse relies on the image without enumerating it."},
        {"q": "What does this reading guide say 'saccāni' most likely refers to?",
         "opts": [
             "The five aggregates",
             "The four noble truths, though the verse doesn't name them individually",
             "The three roots of unwholesomeness",
             "The five hindrances"],
         "correct": 1,
         "expl": "The canon's most common referent for 'truths' in the plural."},
        {"q": "What does 'paṭivijjhati' mean?",
         "opts": [
             "Penetrates, breaks through to understanding",
             "Sinks, drowns",
             "Builds, constructs",
             "Forgets, loses track of"],
         "correct": 0,
         "expl": "The verb behind this verse's central claim."},
        {"q": "What does this reading guide suggest the name Ajjuna may possibly mean?",
         "opts": [
             "Protected, guarded",
             "Ram's head",
             "Given by the lord",
             "White, bright, clear"],
         "correct": 3,
         "expl": "Also the name of a tree valued for its pale bark."},
        {"q": "What does 'vuyhamāna' mean?",
         "opts": [
             "Being swept away",
             "Standing still",
             "Climbing upward",
             "Falling asleep"],
         "correct": 0,
         "expl": "A present passive participle, describing ongoing action."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The fourth poem",
             "The eighth poem"],
         "correct": 3,
         "expl": "Immediately after Paviṭṭha's verse."},
    ],
    marginalia=[
        ("Insight, mid-flood", [
            "still being swept along —",
            "and there, the truths break through"
        ]),
        ("A flood, unspecified", [
            "the great flood, named plainly —",
            "which one, left unsaid"
        ]),
        ("Shore reached, truths found", [
            "lifted himself up —",
            "the same moment, both"
        ]),
        ("A name, possibly bright", [
            "white, like pale bark —",
            "no further claim made"
        ]),
    ],
    further=[
        '<a href="%s/thag1.88/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.87.html">Thag 1.87 &mdash; Pavi&#7789;&#7789;ha</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.89.html">Thag 1.89 &mdash; Devasabha (1st)</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.89 — Devasabha (1st)
# --------------------------------------------------------------------------- #
page(
    1, 89, "Devasabha", "Devasabha (1st)",
    meta_title="Thag 1.89 — Devasabha (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Devasabha's verse, five obstacles named as already "
        "overcome — bogs, chasms, floods, ties, and conceit. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 9 of 10",
    glance=[
        ("Setting", "A retrospective declaration listing several "
                    "obstacles already overcome"),
        ("Speaker", "Devasabha, in the first person"),
        ("Form", "One four-line verse, five images in sequence"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a dense list"),
    ],
    why=(
        "Devasabha names five obstacles in a row, all already "
        "overcome: bogs and mire crossed, chasms avoided, floods and "
        "ties left behind, and all conceit wiped out. It is one of "
        "the more crowded single-verse lists in this collection, "
        "mixing concrete images &mdash; bog, chasm, flood &mdash; "
        "with abstract categories &mdash; ties, conceit."),
    guide=[
        ("Five obstacles, one after another", [
            "Paṅkapalipā (&lsquo;bog and mire&rsquo;, a near-synonym "
            "pair), pātāla (&lsquo;chasm&rsquo;), ogha "
            "(&lsquo;flood&rsquo;), gantha (&lsquo;tie&rsquo;), and "
            "māna (&lsquo;conceit&rsquo;) &mdash; five distinct "
            "obstacles named in sequence, each already dealt with: "
            "crossed, avoided, escaped, or wiped out. The density of "
            "the list is unusual even for this collection, which "
            "elsewhere tends to build a single verse around one image "
            "or one category rather than several at once."]),
        ("Floods, echoed from the poem before", [
            "Mutto oghā, &lsquo;freed from floods&rsquo;, repeats the "
            "same image the poem immediately before this one, Thag "
            "1.88 (Ajjuna), built its entire verse around &mdash; "
            "though the two treat it differently. Thag 1.88 "
            "dramatizes an active struggle, insight breaking through "
            "while still being swept along; here, the flood is simply "
            "one item in a completed list, already left behind."]),
        ("Ganthā, a standard fourfold set", [
            "Gantha (&lsquo;tie&rsquo;) is a standard category "
            "throughout the wider canon, traditionally enumerated as "
            "four: covetousness, ill will, attachment to rites and "
            "observances, and dogmatic insistence on one's own views. "
            "This verse names the category without breaking it down, "
            "the same unglossed treatment several earlier verses in "
            "this collection have given other standard lists."]),
        ("Devasabha, the first of two", [
            "Devasabha reads as deva (&lsquo;god, deity&rsquo;) plus "
            "sabha (&lsquo;assembly, hall&rsquo;) &mdash; &lsquo;an "
            "assembly of gods&rsquo;, or &lsquo;one with a divine "
            "assembly&rsquo;. The &lsquo;(1st)&rsquo; marking his "
            "name signals, as with Puṇṇa, Tissa, Uttiya, and Valliya "
            "earlier in this collection, that another elder later "
            "shares this name."]),
    ],
    terms=[
        ("paṅkapalipā",
         "&ldquo;bog and mire&rdquo; &mdash; a near-synonym pair, "
         "the first obstacle this verse names as crossed."),
        ("pātāla",
         "&ldquo;chasm, abyss&rdquo; &mdash; the second obstacle, "
         "described as avoided."),
        ("ogha",
         "&ldquo;flood&rdquo; &mdash; the same image the poem "
         "immediately before this one, Thag 1.88, built its verse "
         "around."),
        ("gantha",
         "&ldquo;tie, knot&rdquo; &mdash; traditionally enumerated as "
         "four: covetousness, ill will, attachment to rites, and "
         "dogmatic views."),
        ("māna",
         "&ldquo;conceit&rdquo; &mdash; the fifth and final obstacle "
         "this verse names, said to be wiped out entirely."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.89:1.1-1.4"),
    ],
    quiz=[
        {"q": "How many distinct obstacles does this verse name as already overcome?",
         "opts": [
             "Three",
             "Five",
             "Seven",
             "Ten"],
         "correct": 1,
         "expl": "Bog and mire, chasm, flood, tie, and conceit."},
        {"q": "What image does this verse share with the poem immediately before it, Thag 1.88?",
         "opts": [
             "The image of a hut",
             "The image of an elephant",
             "The image of a flood (ogha)",
             "The image of a bamboo shoot"],
         "correct": 2,
         "expl": "Mutto oghā, 'freed from floods', echoing Thag 1.88's central image."},
        {"q": "How does this verse's treatment of the flood differ from Thag 1.88's?",
         "opts": [
             "They are identical in every way",
             "This verse dramatizes an active struggle; Thag 1.88 lists it as already completed",
             "Neither verse actually mentions a flood",
             "Thag 1.88 dramatizes an active struggle; this verse lists it as one item in a completed list"],
         "correct": 3,
         "expl": "Ongoing peril in Thag 1.88, versus a settled, completed list here."},
        {"q": "What does 'gantha' mean, and how many are traditionally enumerated?",
         "opts": [
             "'Tie, knot' — traditionally four",
             "'Wisdom' — traditionally three",
             "'Robe' — traditionally two",
             "'Bowl' — traditionally one"],
         "correct": 0,
         "expl": "Covetousness, ill will, attachment to rites, and dogmatic views."},
        {"q": "Does this verse individually name the four ties?",
         "opts": [
             "Yes, all four are listed",
             "Only two are listed",
             "It replaces the four ties with a different list",
             "No — it names the category without breaking it down"],
         "correct": 3,
         "expl": "The same unglossed treatment given to other standard categories in this collection."},
        {"q": "What does the name Devasabha mean?",
         "opts": [
             "Ram's head",
             "An assembly of gods, or one with a divine assembly",
             "Son of an elephant-rider",
             "Given by the lord"],
         "correct": 1,
         "expl": "Deva ('god') plus sabha ('assembly')."},
        {"q": "What does the '(1st)' marking after Devasabha's name signal?",
         "opts": [
             "That he was the first monk ever ordained",
             "That he is the first of several brothers",
             "That another elder later in the collection shares this name",
             "That this is his first verse of several"],
         "correct": 2,
         "expl": "The same disambiguation pattern seen with Puṇṇa, Tissa, Uttiya, and Valliya."},
        {"q": "What does 'pātāla' mean?",
         "opts": [
             "Chasm, abyss",
             "A type of hut",
             "A monastic robe",
             "A river crossing"],
         "correct": 0,
         "expl": "The second obstacle this verse names, described as avoided."},
        {"q": "What does 'māna' mean?",
         "opts": [
             "Wisdom",
             "Generosity",
             "Doubt",
             "Conceit"],
         "correct": 3,
         "expl": "The fifth and final obstacle this verse names."},
        {"q": "Where does this poem fall in Chapter Nine?",
         "opts": [
             "The ninth poem",
             "The opening poem",
             "The fifth poem",
             "The first poem of the next chapter"],
         "correct": 0,
         "expl": "The second-to-last poem, immediately before the chapter's close."},
    ],
    marginalia=[
        ("Five obstacles, named in a row", [
            "bog, chasm, flood —",
            "tie and conceit, too"
        ]),
        ("A flood, echoed once more", [
            "the same word as before —",
            "now, already crossed"
        ]),
        ("Ties, left unbroken down", [
            "four, by tradition —",
            "named only as one word"
        ]),
        ("A first of two", [
            "assembly of gods —",
            "another, later, shares the name"
        ]),
    ],
    further=[
        '<a href="%s/thag1.89/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.88.html">Thag 1.88 &mdash; Ajjuna</a> '
        "&mdash; the poem immediately before this one, sharing this "
        "verse's flood (ogha) image.",
        '<a href="thag-1.90.html">Thag 1.90 &mdash; S&amacr;midatta</a> '
        "&mdash; the next and final poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.90 — S&amacr;midatta
# --------------------------------------------------------------------------- #
page(
    1, 90, "S&amacr;midatta", "S&amacr;midatta",
    meta_title="Thag 1.90 — Sāmidatta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sāmidatta's verse, closing Chapter Nine with the same exact "
        "couplet already heard twice before in this collection, and "
        "a precise doctrinal point about aggregates that remain but "
        "whose root is cut. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Nine &middot; Poem 10 of 10",
    glance=[
        ("Setting", "A retrospective declaration, closing this "
                    "chapter's tenth and final poem"),
        ("Speaker", "Sāmidatta, in the first person"),
        ("Form", "One four-line verse, followed by the chapter's "
                 "formulaic double closing"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one precise doctrinal "
                       "point"),
    ],
    why=(
        "Sāmidatta declares the five aggregates fully understood: "
        "&lsquo;they remain, but their root is cut&rsquo;. The "
        "verse's closing couplet &mdash; &lsquo;transmigration "
        "through births is finished, now there'll be no more future "
        "lives&rsquo; &mdash; is the third time this exact wording "
        "has appeared in this collection, after Thag 1.67 and Thag "
        "1.87."),
    guide=[
        ("Aggregates remain, but the root is cut", [
            "Pañcakkhandhā pariññātā, tiṭṭhanti chinnamūlakā: the "
            "five aggregates are fully understood; they remain, but "
            "their root is cut. This is a precise doctrinal claim, "
            "distinct from Thag 1.87's &lsquo;all rebirths are "
            "shattered&rsquo; one poem back &mdash; this verse says "
            "the present aggregates, body and mind, are still "
            "standing (tiṭṭhanti), because the speaker is still "
            "alive. What has been severed is their root: the craving "
            "and ignorance that would otherwise generate a new set of "
            "aggregates after this life ends. It is the difference "
            "between a fire already out and a fire that will not be "
            "fed again once this last supply of fuel burns down."]),
        ("A third appearance of the same closing couplet", [
            "Vikkhīṇo jātisaṁsāro, natthi dāni punabbhavo closes this "
            "verse exactly as it closed Thag 1.67 (from Chapter "
            "Seven) and Thag 1.87 (seven poems earlier in this same "
            "chapter). This is the third time this exact two-line "
            "formula has appeared, word for word, across the "
            "collection so far."]),
        ("Twin poems bookending the chapter's second half", [
            "Thag 1.87 and this verse are unusually closely matched: "
            "both open on the aggregates (khandhā diṭṭhā / "
            "pañcakkhandhā pariññātā), both close on the identical "
            "couplet, and both fall in the same chapter, seven poems "
            "apart. This is one of the more tightly matched pairs of "
            "poems within a single chapter found anywhere in this "
            "project so far."]),
        ("The chapter's double closing", [
            "As in every chapter so far, two more lines follow the "
            "poem itself, both left untranslated by Sujato: vaggo "
            "navamo (&lsquo;the ninth chapter [ends]&rsquo;), then an "
            "uddāna listing all ten names. This uddāna adds two "
            "epithets not found in either elder's own verse: Ajjuna "
            "becomes ajjuno isi (&lsquo;Ajjuna the sage&rsquo;), and "
            "Sāmidatta himself becomes sāmidatto mahabbalo "
            "(&lsquo;Sāmidatta of great strength&rsquo;) &mdash; the "
            "same kind of added detail seen in Chapter Eight's "
            "uddāna, which called Māṇava isi without his own verse "
            "making that claim."]),
    ],
    terms=[
        ("khandha",
         "&ldquo;aggregate&rdquo; &mdash; here specified as pañca "
         "(&lsquo;five&rsquo;), the standard components of a "
         "person."),
        ("pariññāta",
         "&ldquo;fully understood&rdquo; &mdash; describing the "
         "aggregates' status in this verse."),
        ("chinnamūlaka",
         "&ldquo;having its root cut&rdquo; &mdash; chinna "
         "(&lsquo;cut&rsquo;) plus mūla (&lsquo;root&rsquo;), the "
         "verse's key doctrinal image."),
        ("vaggo navamo",
         "&ldquo;the ninth chapter [ends]&rdquo; &mdash; the "
         "untranslated closing marker for this chapter."),
        ("mahabbala",
         "&ldquo;of great strength&rdquo; &mdash; an epithet added to "
         "Sāmidatta's name in the chapter's uddāna, not found in his "
         "own verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.90:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse say about the five aggregates?",
         "opts": [
             "They are fully understood, and remain, but their root is cut",
             "They have completely vanished",
             "They are just now beginning to form",
             "They have been replaced by new aggregates"],
         "correct": 0,
         "expl": "Pañcakkhandhā pariññātā, tiṭṭhanti chinnamūlakā."},
        {"q": "According to this reading guide, what is the doctrinal point of 'they remain, but their root is cut'?",
         "opts": [
             "The aggregates never existed in the first place",
             "The aggregates will be reborn exactly as they are",
             "The present aggregates persist because the speaker is still alive, but won't generate new ones after this life",
             "The verse denies the existence of the five aggregates entirely"],
         "correct": 2,
         "expl": "A fire already out, versus a fire that won't be fed again once its last fuel burns down."},
        {"q": "How many times has this verse's exact closing couplet now appeared in this collection?",
         "opts": [
             "Once",
             "Twice",
             "Three times — Thag 1.67, Thag 1.87, and this verse",
             "Five times"],
         "correct": 2,
         "expl": "Confirmed by direct comparison with the two earlier poems."},
        {"q": "What earlier poem in this same chapter does this verse form an unusually close pair with?",
         "opts": [
             "Thag 1.81 Samitigutta",
             "Thag 1.83 Sīha",
             "Thag 1.85 Sunāga",
             "Thag 1.87 Paviṭṭha"],
         "correct": 3,
         "expl": "Both open on the aggregates and close on the identical couplet."},
        {"q": "What two untranslated lines follow this verse, as in every chapter so far?",
         "opts": [
             "A dedication to the Buddha",
             "A list of monastic rules",
             "A second verse by the same elder",
             "A chapter-closing marker and a summary verse (uddāna) listing all ten names"],
         "correct": 3,
         "expl": "Vaggo navamo, then the uddāna."},
        {"q": "What epithet does the chapter's uddāna add to Ajjuna's name, not found in his own verse?",
         "opts": [
             "'Isi', the sage",
             "'Mahā', the great",
             "'Thera', the elder",
             "No epithet is added"],
         "correct": 0,
         "expl": "Ajjuno isi, matching the pattern seen with Māṇava in Chapter Eight's uddāna."},
        {"q": "What epithet does the uddāna add to Sāmidatta's own name?",
         "opts": [
             "'Isi', the sage",
             "'Ārohaputta', son of an elephant-rider",
             "No epithet is added",
             "'Mahabbalo', of great strength"],
         "correct": 3,
         "expl": "Sāmidatto mahabbalo, an addition not found in his own verse."},
        {"q": "What does 'pariññāta' mean?",
         "opts": [
             "Fully understood",
             "Completely forgotten",
             "Newly discovered",
             "Partially known"],
         "correct": 0,
         "expl": "Describing the aggregates' status in this verse."},
        {"q": "What does 'chinnamūlaka' mean?",
         "opts": [
             "Deeply rooted",
             "Having its root cut",
             "Growing new roots",
             "Without any roots to begin with"],
         "correct": 1,
         "expl": "Chinna ('cut') plus mūla ('root')."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "The opening poem of Chapter Nine",
             "The tenth and final poem of Chapter Nine",
             "The first poem of Chapter Ten",
             "A poem in the Book of the Twos"],
         "correct": 1,
         "expl": "Closing this chapter's set of ten."},
    ],
    marginalia=[
        ("A root, cut; a house, standing", [
            "the aggregates remain —",
            "nothing left to feed them"
        ]),
        ("A couplet, a third time", [
            "the same two lines again —",
            "once in Chapter Seven"
        ]),
        ("Two poems, matched closely", [
            "aggregates opening both —",
            "the same close, twice"
        ]),
        ("Two names, quietly enlarged", [
            "a sage added; great strength added —",
            "the uddāna's own touches"
        ]),
    ],
    further=[
        '<a href="%s/thag1.90/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.87.html">Thag 1.87 &mdash; Pavi&#7789;&#7789;ha</a> '
        "&mdash; this chapter's other aggregates-themed poem, closing "
        "with the identical couplet.",
        '<a href="thag-1.67.html">Thag 1.67 &mdash; '
        "Ekadhammasavan&imacr;ya</a> &mdash; the first appearance of "
        "this exact closing couplet, in Chapter Seven.",
        '<a href="thag-1.89.html">Thag 1.89 &mdash; Devasabha (1st)</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.91 — Paripu&#7751;&#7751;aka
# --------------------------------------------------------------------------- #
page(
    1, 91, "Paripu&#7751;&#7751;aka", "Paripu&#7751;&#7751;aka",
    meta_title="Thag 1.91 — Paripuṇṇaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Paripuṇṇaka's verse, opening Chapter Ten with a food "
        "metaphor for the Dhamma itself. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 1 of 10",
    glance=[
        ("Setting", "No narrative setting; a single comparison "
                    "between food and the Dhamma"),
        ("Speaker", "Paripuṇṇaka, in the first person"),
        ("Form", "One four-line verse, built on a food metaphor"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one clear comparison"),
    ],
    why=(
        "Chapter Ten opens with a simple comparison: what Paripuṇṇaka "
        "&lsquo;consumed today&rsquo; &mdash; the Dhamma taught by "
        "the Buddha &mdash; is better than &lsquo;delicious grain of "
        "a hundred flavors&rsquo;. The verse treats the teaching "
        "itself as a kind of food, more satisfying than any meal."),
    guide=[
        ("Better than a feast", [
            "The verse's whole force rests on the comparison: "
            "sudhanna, &lsquo;delicious grain&rsquo;, described as "
            "having a hundred flavors, set against what was actually "
            "&lsquo;consumed&rsquo; (paribhutta) that day &mdash; not "
            "food at all, but the Dhamma. The verb paribhutta, "
            "normally used for eating or partaking of something, is "
            "applied here to hearing or absorbing the teaching, "
            "extending the food image through the whole verse rather "
            "than stating the comparison and dropping it."]),
        ("Another epithet built on 'seeing'", [
            "Aparimitadassin, &lsquo;of unlimited vision&rsquo;, "
            "describes the Buddha in this verse's third line &mdash; "
            "another word built from the same root as dassin (Thag "
            "1.71), dassana (Thag 1.75), and passati (Thag 1.61). "
            "Three of this collection's last four chapters have now "
            "opened, or opened near, a poem reaching for this root; "
            "Chapter Nine's opener did not. This reading guide notes "
            "the recurrence without claiming it reflects deliberate "
            "arrangement."]),
        ("A name that matches its own theme", [
            "Paripuṇṇaka reads as pari (&lsquo;completely&rsquo;) "
            "plus puṇṇa (&lsquo;full&rsquo;) &mdash; &lsquo;completely "
            "full, fulfilled&rsquo;. Read against a verse entirely "
            "about being satisfied by what was &lsquo;consumed&rsquo; "
            "rather than by food, the name and the verse's own "
            "content point in the same direction."]),
    ],
    terms=[
        ("sudhanna",
         "&ldquo;delicious grain&rdquo; &mdash; the verse's image "
         "for fine food, set against the Dhamma."),
        ("paribhutta",
         "&ldquo;consumed, partaken of&rdquo; &mdash; normally used "
         "for eating, applied here to receiving the teaching."),
        ("aparimitadassin",
         "&ldquo;of unlimited vision&rdquo; &mdash; an epithet for "
         "the Buddha, sharing its root with dassin (Thag 1.71) and "
         "passati (Thag 1.61)."),
        ("desita",
         "&ldquo;taught, expounded&rdquo; &mdash; describing how the "
         "Dhamma was delivered."),
        ("Paripuṇṇaka",
         "&ldquo;completely full, fulfilled&rdquo; &mdash; pari "
         "(&lsquo;completely&rsquo;) plus puṇṇa (&lsquo;full&rsquo;)."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.91:1.1-1.4"),
    ],
    quiz=[
        {"q": "What comparison does this verse make?",
         "opts": [
             "The Dhamma is like the sound of distant thunder",
             "The Dhamma is like water in a desert",
             "The Dhamma is like a long journey",
             "What was 'consumed' today, the Dhamma, is better than delicious food of a hundred flavors"],
         "correct": 3,
         "expl": "The verse's central comparison, sustained through a food metaphor."},
        {"q": "What does 'paribhutta' normally describe, and how is it used here?",
         "opts": [
             "Normally describes eating; here applied to receiving the teaching",
             "Normally describes sleeping; here applied to meditating",
             "Normally describes traveling; here applied to teaching",
             "Normally describes building; here applied to ordaining"],
         "correct": 0,
         "expl": "Extending the food image through the whole verse."},
        {"q": "What does 'aparimitadassin' mean?",
         "opts": [
             "Of great strength",
             "Of unlimited vision",
             "Of humble birth",
             "Of many followers"],
         "correct": 1,
         "expl": "An epithet for the Buddha, sharing its root with dassin and passati."},
        {"q": "What earlier chapter-opening poems does this reading guide connect 'aparimitadassin' to?",
         "opts": [
             "Thag 1.61 Vappa and Thag 1.71 Vacchapāla",
             "Thag 1.1 Subhūti and Thag 1.11 Cūḷavaccha",
             "Thag 1.81 Samitigutta and Thag 1.51 Godhika",
             "Thag 1.41 Sirivaḍḍha and Thag 1.31 (unnamed)"],
         "correct": 0,
         "expl": "Both build their opening poem around the same 'seeing' root."},
        {"q": "According to this reading guide, did Chapter Nine's opening poem also use this 'seeing' root?",
         "opts": [
             "Yes, prominently",
             "No — this reading guide notes it did not",
             "The question cannot be answered",
             "Yes, but only in its closing line"],
         "correct": 1,
         "expl": "The recurrence is noted across three of the last four chapters, not all four."},
        {"q": "What does the name Paripuṇṇaka mean?",
         "opts": [
             "Given by the lord",
             "One who has given up what is dear",
             "Completely full, fulfilled",
             "Ram's head"],
         "correct": 2,
         "expl": "Pari ('completely') plus puṇṇa ('full')."},
        {"q": "How does this reading guide relate Paripuṇṇaka's name to this verse's content?",
         "opts": [
             "It finds no connection at all",
             "The name directly contradicts the verse's message",
             "The name and the verse's theme of being satisfied by the Dhamma point in the same direction",
             "The name is a direct quotation from the verse"],
         "correct": 2,
         "expl": "A thematic match between the name's meaning and the verse's content."},
        {"q": "What does 'sudhanna' mean?",
         "opts": [
             "Delicious grain",
             "A monastic robe",
             "A begging bowl",
             "A type of meditation"],
         "correct": 0,
         "expl": "The verse's image of fine food, set against the Dhamma."},
        {"q": "What does 'desita' mean?",
         "opts": [
             "Abandoned, discarded",
             "Remembered, recalled",
             "Forgotten",
             "Taught, expounded"],
         "correct": 3,
         "expl": "Describing how the Dhamma was delivered."},
        {"q": "What chapter does this poem open?",
         "opts": [
             "Chapter Nine",
             "Chapter Eleven",
             "The Great Book",
             "Chapter Ten"],
         "correct": 3,
         "expl": "The first of ten poems in this new chapter."},
    ],
    marginalia=[
        ("A meal, not of food", [
            "consumed today —",
            "better than a hundred flavors"
        ]),
        ("Unlimited vision, again", [
            "the same root, a third time —",
            "no design claimed"
        ]),
        ("A name, completely full", [
            "fulfilled, the name says —",
            "so does the verse itself"
        ]),
        ("Ten poems ahead", [
            "a new chapter opens —",
            "with a single taste"
        ]),
    ],
    further=[
        '<a href="%s/thag1.91/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.90.html">Thag 1.90 &mdash; S&amacr;midatta</a> '
        "&mdash; the poem immediately before this one, closing "
        "Chapter Nine.",
        '<a href="thag-1.71.html">Thag 1.71 &mdash; Vacchap&amacr;la</a> '
        "&mdash; an earlier chapter-opening poem built around the "
        "same 'seeing' root.",
        '<a href="thag-1.92.html">Thag 1.92 &mdash; Vijaya</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.92 — Vijaya
# --------------------------------------------------------------------------- #
page(
    1, 92, "Vijaya", "Vijaya",
    meta_title="Thag 1.92 — Vijaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Vijaya's verse, word for word identical to Dhammapada verse "
        "93 — a portrait of the arahant whose track is as hard to "
        "trace as a bird's flight through the sky. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 2 of 10",
    glance=[
        ("Setting", "No narrative setting; a general portrait of the "
                    "arahant, in the third person"),
        ("Speaker", "An unnamed voice describing a person who has "
                    "ended defilement"),
        ("Form", "One six-line verse, closing on a simile"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one memorable image"),
    ],
    why=(
        "This verse describes someone whose defilements have ended, "
        "unattached to food, ranging in the liberation of the "
        "signless and the empty &mdash; and closes: &lsquo;their "
        "track is hard to trace, like birds in the sky&rsquo;. Every "
        "line of it is word for word identical to Dhammapada verse "
        "93, already complete on this site."),
    guide=[
        ("A verse shared word for word with the Dhammapada, again", [
            "Compared directly against this site's own Dhammapada "
            "pages, all six lines of this verse match Dhp 93 exactly "
            "&mdash; the same Pali, the same English translation, "
            "start to finish. This is the third connection this "
            "reading guide has found between this collection and the "
            "Dhammapada (after Dhp 326 at Thag 1.77 and Dhp 153 at "
            "Thag 1.78), and the most complete of the three: not a "
            "shared opening or a single matching quatrain, but the "
            "entire verse, word for word."]),
        ("A twin already noted on this site", [
            "Dhp 93 doesn't stand alone in the Dhammapada either: "
            "this site's own reading guide for Dhp 92&ndash;93 (in "
            "Dhp 7, the Arahantavagga) already describes them as a "
            "&lsquo;striking case of near-repetition&rsquo;, sharing "
            "their final four lines while differing in their opening "
            "couplet &mdash; Dhp 92 speaks of &lsquo;those&rsquo; "
            "(plural) who have nothing stored up, Dhp 93 (and this "
            "verse) of &lsquo;one whose defilements have "
            "ended&rsquo; (singular). This Theragātha verse "
            "specifically matches the singular member of that "
            "existing Dhammapada pair."]),
        ("Birds leaving no trace in the sky", [
            "The closing image &mdash; a track as hard to follow as "
            "a bird's path through open air &mdash; needs no "
            "unpacking: someone who has let go of accumulation "
            "leaves nothing behind for anyone to trace. The verse "
            "names two of the three traditional &lsquo;doors to "
            "liberation&rsquo; &mdash; suññata (&lsquo;the "
            "empty&rsquo;) and animitta (&lsquo;the "
            "signless&rsquo;) &mdash; without naming the third, "
            "appaṇihita (&lsquo;the undirected&rsquo;)."]),
    ],
    terms=[
        ("āsava",
         "&ldquo;defilement, taint&rdquo; &mdash; what this verse "
         "says has &lsquo;ended&rsquo; in the person it describes."),
        ("anissita",
         "&ldquo;not attached, not dependent&rdquo; &mdash; "
         "describing this person's relationship to food."),
        ("suññata",
         "&ldquo;the empty&rdquo; &mdash; one of two liberations "
         "named in this verse, out of the traditional three."),
        ("animitta",
         "&ldquo;the signless&rdquo; &mdash; the second of the two "
         "liberations this verse names."),
        ("durannaya",
         "&ldquo;hard to trace, hard to follow&rdquo; &mdash; the "
         "verse's closing description of this person's track."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.92:1.1-1.6"),
    ],
    quiz=[
        {"q": "What earlier-completed collection on this site contains a verse identical, word for word, to this one?",
         "opts": [
             "The Cariyapitaka",
             "The Khuddakapatha",
             "The Therīgāthā",
             "The Dhammapada (verse 93, in the Arahantavagga)"],
         "correct": 3,
         "expl": "Confirmed by direct comparison with this site's own Dhammapada pages."},
        {"q": "How complete is this match, compared to the two earlier Dhammapada connections found in this collection (Thag 1.77 and Thag 1.78)?",
         "opts": [
             "It matches only the closing line",
             "It matches only the opening two lines",
             "It matches roughly half the verse",
             "It is the most complete of the three — all six lines match, word for word"],
         "correct": 3,
         "expl": "Unlike the shared opening (Thag 1.78) or the single matching quatrain (Thag 1.77), this is a full match."},
        {"q": "What does this site's own Dhammapada guide (Dhp 7) already say about Dhp 92 and Dhp 93?",
         "opts": [
             "That they are unrelated verses with no connection",
             "That they are a 'striking case of near-repetition', sharing their final four lines",
             "That Dhp 93 is a later forgery",
             "That only Dhp 92 is authentic"],
         "correct": 1,
         "expl": "Already documented as a matched pair before this Theragātha connection was found."},
        {"q": "Which of the two Dhammapada twin verses does this Theragātha verse match?",
         "opts": [
             "Dhp 93, the singular version",
             "Dhp 92, the plural version",
             "It matches parts of both equally",
             "It matches neither exactly"],
         "correct": 0,
         "expl": "Dhp 93 speaks of 'one whose defilements have ended', matching this verse's opening."},
        {"q": "What image does this verse close on?",
         "opts": [
             "A river returning to the sea",
             "A fire being extinguished",
             "A track as hard to trace as a bird's path through the sky",
             "A tree losing its leaves"],
         "correct": 2,
         "expl": "Ākāseva sakuntānaṁ, padaṁ tassa durannayaṁ, the verse's closing simile."},
        {"q": "How many of the traditional three 'doors to liberation' does this verse name?",
         "opts": [
             "All three",
             "Two — suññata and animitta, not appaṇihita",
             "Only one",
             "None"],
         "correct": 1,
         "expl": "The verse omits the third, appaṇihita ('the undirected')."},
        {"q": "What does 'āsava' mean?",
         "opts": [
             "Defilement, taint",
             "Wisdom, insight",
             "A monastic robe",
             "A begging bowl"],
         "correct": 0,
         "expl": "What this verse says has ended in the person it describes."},
        {"q": "What does 'anissita' mean?",
         "opts": [
             "Not attached, not dependent",
             "Fully attached",
             "Newly arrived",
             "Deeply asleep"],
         "correct": 0,
         "expl": "Describing this person's relationship to food."},
        {"q": "Is this verse first-person testimony or a third-person description?",
         "opts": [
             "First-person testimony",
             "A dialogue between two speakers",
             "A third-person description of a type of person",
             "A direct address to a named listener"],
         "correct": 2,
         "expl": "Yassa ('of whom'), describing someone rather than declaring the speaker's own state."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The fifth poem",
             "The second poem"],
         "correct": 3,
         "expl": "Immediately after Paripuṇṇaka's verse."},
    ],
    marginalia=[
        ("A verse, entirely shared", [
            "six lines, elsewhere too —",
            "the fullest match yet"
        ]),
        ("A twin, already known", [
            "singular, then plural —",
            "the same four closing lines"
        ]),
        ("No track left behind", [
            "a bird crosses the sky —",
            "nothing left to follow"
        ]),
        ("Two doors, not three", [
            "empty, signless, named —",
            "undirected, left silent"
        ]),
    ],
    further=[
        '<a href="%s/thag1.92/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="../dhammapada/dhp-07.html">Dhammapada 7 &mdash; '
        "Arahantavagga (The Perfected Ones)</a> &mdash; contains Dhp "
        "92&ndash;93, this verse's full match and its own documented "
        "twin.",
        '<a href="thag-1.91.html">Thag 1.91 &mdash; Paripu&#7751;&#7751;aka</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.93.html">Thag 1.93 &mdash; Eraka</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.93 — Eraka
# --------------------------------------------------------------------------- #
page(
    1, 93, "Eraka", "Eraka",
    meta_title="Thag 1.93 — Eraka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Eraka's verse, naming its own listener four times in a "
        "single short logical chain about sensual pleasure and "
        "suffering. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 3 of 10",
    glance=[
        ("Setting", "No narrative frame; a repeated direct address, "
                    "building a short logical chain"),
        ("Speaker", "Unnamed; this reading guide does not resolve "
                    "whether Eraka is being addressed by another "
                    "voice or addressing himself"),
        ("Form", "One six-line verse, naming its listener four "
                 "times"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a repetitive structure"),
    ],
    why=(
        "This verse names its own listener, Eraka, four separate "
        "times in six short lines, hammering home a simple chain of "
        "reasoning: sensual pleasures are suffering; one who enjoys "
        "them enjoys suffering; one who doesn't, doesn't. It is the "
        "most insistent name-repetition found anywhere in this "
        "collection so far."),
    guide=[
        ("Named four times in one breath", [
            "Eraka appears as a direct address at the end of lines "
            "one, two, four, and six &mdash; far more insistent than "
            "Thag 1.83, where Sīha's name appeared just once within "
            "the verse. The repetition itself does rhetorical work: "
            "each restatement of the name anchors a fresh step in the "
            "verse's logic, so that by the end &lsquo;Eraka&rsquo; "
            "has become almost a refrain as much as a name."]),
        ("A syllogism, not a story", [
            "The verse's structure is a clean chain: sensual "
            "pleasures are suffering, stated twice for emphasis; "
            "therefore whoever enjoys sensual pleasures enjoys "
            "suffering; and by the same logic, whoever doesn't enjoy "
            "them doesn't enjoy suffering. No narrative, no simile, "
            "carries any of this &mdash; the whole verse is argument, "
            "restated with each named address to Eraka."]),
        ("Whose voice, addressing whom?", [
            "As with Thag 1.83 (Sīha), this reading guide does not "
            "resolve who is speaking. The verse could be someone "
            "else's exhortation to Eraka &mdash; a teacher's, "
            "perhaps &mdash; or it could be Eraka addressing himself, "
            "repeating his own name the way a person might drill a "
            "lesson into their own mind. Unlike Thag 1.5 and Thag 1.8, "
            "where the name Vīra doubled as a plain descriptive word "
            "within the elder's own self-report, this verse's "
            "structure of repeated direct address doesn't fit that "
            "pattern as easily."]),
        ("A name, possibly a plant", [
            "Eraka may relate to a word for a kind of reed or grass "
            "used elsewhere in the wider canon's vocabulary. Given "
            "the uncertainty, this reading guide notes the "
            "possibility without treating it as established."]),
    ],
    terms=[
        ("kāma",
         "&ldquo;sensual pleasure&rdquo; &mdash; the subject of this "
         "verse's entire argument."),
        ("kāmayati",
         "&ldquo;enjoys, desires&rdquo; &mdash; a verb built "
         "directly from kāma, repeated through the verse."),
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; what the verse says "
         "sensual pleasure both is and leads to."),
        ("Eraka",
         "the name repeated four times in this verse, possibly "
         "related to a word for a kind of reed or grass."),
        ("kāmā dukkhā",
         "&ldquo;sensual pleasures are suffering&rdquo; &mdash; the "
         "verse's opening claim, stated twice."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.93:1.1-1.6"),
    ],
    quiz=[
        {"q": "How many times does this verse address its listener by name?",
         "opts": [
             "Once",
             "Twice",
             "Four times",
             "Not at all"],
         "correct": 2,
         "expl": "At the end of lines one, two, four, and six."},
        {"q": "How does this compare to Thag 1.83, where Sīha was addressed?",
         "opts": [
             "Identical — both name their listener the same number of times",
             "This verse names Eraka far more often than Thag 1.83 named Sīha",
             "Thag 1.83 named Sīha more often",
             "Neither verse names its listener at all"],
         "correct": 1,
         "expl": "Thag 1.83 used the name once; this verse uses it four times."},
        {"q": "What is the verse's overall structure?",
         "opts": [
             "A narrative about a journey",
             "A dialogue between two named speakers",
             "A short logical chain: pleasure is suffering, therefore enjoying it means enjoying suffering",
             "A riddle with no stated meaning"],
         "correct": 2,
         "expl": "Restated with each direct address to Eraka."},
        {"q": "Does this reading guide resolve whether Eraka is being addressed by someone else or is addressing himself?",
         "opts": [
             "Yes, definitively by the Buddha",
             "Yes, definitively by Eraka himself",
             "Yes, definitively by an unnamed layperson",
             "No — it presents both possibilities without resolving which applies"],
         "correct": 3,
         "expl": "The verse's grammar doesn't settle the question."},
        {"q": "How does this verse's use of Eraka's name differ from Vīra's self-naming in Thag 1.5 and Thag 1.8?",
         "opts": [
             "They are identical in structure",
             "Vīra's name doubled as a plain descriptive word in his own self-report; this verse's repeated address doesn't fit that pattern as easily",
             "Vīra's name never appears in either verse",
             "This verse never mentions Eraka at all"],
         "correct": 1,
         "expl": "A different kind of name-repetition than the earlier wordplay case."},
        {"q": "What does 'kāmayati' mean?",
         "opts": [
             "Enjoys, desires",
             "Abandons, discards",
             "Teaches, instructs",
             "Remembers, recalls"],
         "correct": 0,
         "expl": "A verb built directly from kāma, 'sensual pleasure'."},
        {"q": "What does this verse say happens to one who does not enjoy sensual pleasures?",
         "opts": [
             "They do not enjoy suffering",
             "They enjoy suffering instead",
             "They become wealthy",
             "They are reborn as a deva"],
         "correct": 0,
         "expl": "The verse's final logical step, mirroring the claim about those who do enjoy them."},
        {"q": "What does this reading guide suggest 'Eraka' may possibly relate to?",
         "opts": [
             "A word for a kind of reed or grass",
             "A word for a type of bird",
             "A word for a mountain",
             "A word for a river"],
         "correct": 0,
         "expl": "Noted as a possibility, not established fact."},
        {"q": "What does 'dukkha' mean?",
         "opts": [
             "Wisdom",
             "Faith",
             "Generosity",
             "Suffering"],
         "correct": 3,
         "expl": "What the verse says sensual pleasure both is and leads to."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The seventh poem",
             "The third poem"],
         "correct": 3,
         "expl": "Immediately after Vijaya's verse."},
    ],
    marginalia=[
        ("A name, four times over", [
            "Eraka, Eraka —",
            "the refrain of an argument"
        ]),
        ("Pleasure, suffering, the same", [
            "enjoy one, enjoy the other —",
            "the chain closes itself"
        ]),
        ("Whose voice repeats the name?", [
            "another's lesson, or his own —",
            "the verse does not choose"
        ]),
        ("A name, perhaps a reed", [
            "grass by a riverbank —",
            "or only a guess"
        ]),
    ],
    further=[
        '<a href="%s/thag1.93/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.83.html">Thag 1.83 &mdash; S&imacr;ha</a> '
        "&mdash; an earlier verse also naming its own listener "
        "directly, though only once.",
        '<a href="thag-1.92.html">Thag 1.92 &mdash; Vijaya</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.94.html">Thag 1.94 &mdash; Mettaji</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.94 — Mettaji
# --------------------------------------------------------------------------- #
page(
    1, 94, "Mettaji", "Mettaji",
    meta_title="Thag 1.94 — Mettaji | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Mettaji's verse, a homage to the Buddha echoing the "
        "collection's own opening formula. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 4 of 10",
    glance=[
        ("Setting", "No narrative setting; a verse of homage to the "
                    "Buddha"),
        ("Speaker", "Mettaji, praising the Buddha in the third "
                    "person"),
        ("Form", "One four-line verse, built on the word "
                 "&lsquo;best&rsquo; used twice"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one echo of the "
                       "collection's own opening"),
    ],
    why=(
        "Mettaji opens with homage &mdash; &lsquo;namo hi tassa "
        "bhagavato&rsquo;, &lsquo;homage to that Blessed One&rsquo; "
        "&mdash; wording that partly echoes the collection's own "
        "opening frame in Thag 1.1, before praising the Buddha for "
        "having reached &lsquo;the best&rsquo; and taught &lsquo;the "
        "best teaching&rsquo;."),
    guide=[
        ("An echo of the collection's own opening homage", [
            "Namo hi tassa bhagavato shares its first three words "
            "with the universal homage formula that opens Thag 1.1's "
            "frame verses, namo tassa bhagavato (arahato "
            "sammāsambuddhassa). This verse doesn't continue with the "
            "full canonical formula, though &mdash; it moves instead "
            "to sakyaputtassa sirīmato, &lsquo;the glorious Sakyan "
            "[son]&rsquo;, its own description rather than the "
            "standard closing words."]),
        ("'Best', twice over", [
            "Aggappattena (&lsquo;having reached the best&rsquo;) and "
            "aggadhammo (&lsquo;the best teaching&rsquo;) both build "
            "on agga, &lsquo;best, foremost, highest&rsquo;, giving "
            "the verse's second half a compact doubling: because he "
            "reached the best, what he taught was itself the best. "
            "Sudesito (&lsquo;beautifully taught&rsquo;) closes the "
            "verse, praising not just what was taught but how."]),
        ("Sakyaputta, a clan-based epithet", [
            "Sakyaputta, &lsquo;son of the Sakyans&rsquo;, refers to "
            "the Buddha's own clan, the Sakiyas of Kapilavatthu "
            "&mdash; a common way of identifying him by lineage "
            "throughout the wider canon, alongside epithets built "
            "from his achievements or qualities."]),
    ],
    terms=[
        ("namo",
         "&ldquo;homage&rdquo; &mdash; the verse's opening word, "
         "shared with the collection's own opening frame in Thag "
         "1.1."),
        ("sakyaputta",
         "&ldquo;son of the Sakyans&rdquo; &mdash; identifying the "
         "Buddha by his own clan."),
        ("sirīmant",
         "&ldquo;glorious, splendid&rdquo; &mdash; describing the "
         "Buddha in this verse's second line."),
        ("agga",
         "&ldquo;best, foremost, highest&rdquo; &mdash; the root "
         "this verse's second half builds twice on."),
        ("sudesita",
         "&ldquo;beautifully taught&rdquo; &mdash; su "
         "(&lsquo;well&rsquo;) plus desita (&lsquo;taught&rsquo;), "
         "the verse's closing word."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.94:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse's opening phrase share with Thag 1.1's opening frame?",
         "opts": [
             "Nothing at all",
             "The first three words, 'namo tassa bhagavato'",
             "The entire verse, word for word",
             "Only the meter, not the words"],
         "correct": 1,
         "expl": "Both open with this homage formula, though this verse continues differently."},
        {"q": "Does this verse continue with the full canonical formula ('arahato sammāsambuddhassa') after its opening words?",
         "opts": [
             "Yes, exactly",
             "No — it continues with its own description, 'sakyaputtassa sirīmato'",
             "It continues with a different canonical formula entirely",
             "The verse has no continuation at all"],
         "correct": 1,
         "expl": "A partial echo, not a full repetition of the standard formula."},
        {"q": "What root does this verse's second half build on, used twice?",
         "opts": [
             "Kāma ('sensual pleasure')",
             "Dukkha ('suffering')",
             "Agga ('best, foremost')",
             "Nibbāna ('extinguishment')"],
         "correct": 2,
         "expl": "Aggappattena and aggadhammo, both from the same root."},
        {"q": "What does 'sakyaputta' mean?",
         "opts": [
             "One who has given up what is dear",
             "Ram's head",
             "Given by the lord",
             "Son of the Sakyans"],
         "correct": 3,
         "expl": "Identifying the Buddha by his own clan."},
        {"q": "What does 'sirīmant' mean?",
         "opts": [
             "Glorious, splendid",
             "Ancient, aged",
             "Humble, modest",
             "Hidden, concealed"],
         "correct": 0,
         "expl": "Describing the Buddha in this verse's second line."},
        {"q": "What does 'sudesita' mean?",
         "opts": [
             "Poorly taught",
             "Never taught",
             "Beautifully taught",
             "Secretly taught"],
         "correct": 2,
         "expl": "Su ('well') plus desita ('taught')."},
        {"q": "What kind of verse is this, according to this reading guide?",
         "opts": [
             "A riddle with no stated meaning",
             "A first-person testimony of the speaker's own liberation",
             "A dialogue between two speakers",
             "A verse of homage to the Buddha, praising his teaching"],
         "correct": 3,
         "expl": "Praise directed outward, not a report of Mettaji's own attainment."},
        {"q": "What does 'namo' mean?",
         "opts": [
             "Homage",
             "Farewell",
             "Question",
             "Command"],
         "correct": 0,
         "expl": "The verse's opening word."},
        {"q": "What clan does 'sakyaputta' identify the Buddha with?",
         "opts": [
             "The Sakiyas of Kapilavatthu",
             "The Licchavis of Vesālī",
             "The Koliyas",
             "The Mallas"],
         "correct": 0,
         "expl": "The Buddha's own birth clan."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The eighth poem",
             "The fourth poem",
             "The closing poem"],
         "correct": 2,
         "expl": "Immediately after Eraka's verse."},
    ],
    marginalia=[
        ("An opening, half-echoed", [
            "homage, the same three words —",
            "then, a different close"
        ]),
        ("Best, doubled", [
            "reached the best —",
            "taught the best, too"
        ]),
        ("A clan, named plainly", [
            "son of the Sakyans —",
            "glorious, it says"
        ]),
        ("Praise, not testimony", [
            "no report of his own state —",
            "only homage, offered"
        ]),
    ],
    further=[
        '<a href="%s/thag1.94/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.1.html">Thag 1.1 &mdash; Subh&umacr;ti</a> '
        "&mdash; the collection's own opening frame, sharing this "
        "verse's opening three words.",
        '<a href="thag-1.93.html">Thag 1.93 &mdash; Eraka</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.95.html">Thag 1.95 &mdash; Cakkhup&amacr;la</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.95 — Cakkhup&amacr;la
# --------------------------------------------------------------------------- #
page(
    1, 95, "Cakkhup&amacr;la", "Cakkhup&amacr;la",
    meta_title="Thag 1.95 — Cakkhupāla | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Cakkhupāla's verse, a blind elder's resolve to keep going "
        "alone rather than travel easily with wicked companions — "
        "spoken by a monk whose own name means 'eye-guardian'. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 5 of 10",
    glance=[
        ("Setting", "A personal declaration of blindness and a "
                    "resolve to keep traveling alone"),
        ("Speaker", "Cakkhupāla, in the first person"),
        ("Form", "One four-line verse, a single resolve"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain, direct vocabulary"),
    ],
    why=(
        "Cakkhupāla declares himself blind, &lsquo;my eyes are "
        "ruined&rsquo;, traveling a desolate road &mdash; and resolves "
        "to keep going even if he has to crawl, so long as he doesn't "
        "have to travel &lsquo;with wicked companions&rsquo;. The "
        "verse's content stands in stark contrast to his own name, "
        "which means &lsquo;eye-guardian&rsquo;."),
    guide=[
        ("Blind, but still moving forward", [
            "The verse states its situation plainly &mdash; blind, "
            "eyes ruined, on a desolate road &mdash; then pivots to "
            "resolve: sayamānopi gacchissaṁ, &lsquo;even if I have to "
            "crawl I'll keep going&rsquo;. The final line adds a "
            "condition that reframes the whole verse: not the "
            "physical hardship, but the company kept, is what "
            "actually matters &mdash; solitary struggle is preferable "
            "to travel na sahāyena pāpena, &lsquo;with a wicked "
            "companion&rsquo;."]),
        ("A name that contradicts its own verse", [
            "Cakkhupāla reads as cakkhu (&lsquo;eye&rsquo;) plus pāla "
            "(&lsquo;guardian, protector&rsquo;) &mdash; "
            "&lsquo;eye-guardian&rsquo;. Set against a verse whose "
            "first words are &lsquo;I'm blind, my eyes are "
            "ruined&rsquo;, this is a striking contrast rather than a "
            "match: unlike names elsewhere in this collection that "
            "echo or supply their verse's content (Vacchapāla, "
            "Piyañjaha, Hatthārohaputta), this one points in the "
            "opposite direction from what the verse itself says."]),
        ("A later legend, held at a careful distance", [
            "A well-known later commentarial tradition, the "
            "Dhammapada's post-canonical commentary (not translated "
            "on this site), tells an elaborate story connecting a "
            "monk named Cakkhupāla to blindness brought on by "
            "over-exertion in meditation, followed by full "
            "awakening. This reading guide notes that such a legend "
            "exists in the wider tradition without treating it as "
            "confirmed for this particular verse &mdash; the verse "
            "itself, and this collection's own text, say nothing "
            "about how the blindness came about."]),
    ],
    terms=[
        ("andha",
         "&ldquo;blind&rdquo; &mdash; the verse's opening "
         "self-description."),
        ("hatanetta",
         "&ldquo;ruined eyes&rdquo; &mdash; hata "
         "(&lsquo;destroyed, struck&rsquo;) plus netta "
         "(&lsquo;eyes&rsquo;)."),
        ("kantāra",
         "&ldquo;wilderness, desolate wasteland&rdquo; &mdash; "
         "describing the road being traveled."),
        ("sahāya",
         "&ldquo;companion&rdquo; &mdash; here qualified as pāpa "
         "(&lsquo;wicked&rsquo;), the company the verse refuses."),
        ("Cakkhupāla",
         "&ldquo;eye-guardian&rdquo; &mdash; cakkhu (&lsquo;eye&rsquo;) "
         "plus pāla (&lsquo;guardian&rsquo;), standing in contrast to "
         "this verse's own content."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.95:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the speaker say about his own eyes?",
         "opts": [
             "They are perfectly sighted",
             "He is blind, his eyes are ruined",
             "He has one working eye",
             "The verse doesn't mention his eyes"],
         "correct": 1,
         "expl": "Andhohaṁ hatanettosmi, the verse's opening declaration."},
        {"q": "What does the speaker resolve to do, despite his blindness?",
         "opts": [
             "Wait for someone to guide him",
             "Turn back",
             "Keep going, even if he has to crawl",
             "Give up the journey entirely"],
         "correct": 2,
         "expl": "Sayamānopi gacchissaṁ, 'even if I have to crawl I'll keep going'."},
        {"q": "What condition does the verse's final line place on this resolve?",
         "opts": [
             "Only if the weather is fair",
             "Only if he has enough food",
             "Only during the daytime",
             "Not with a wicked companion"],
         "correct": 3,
         "expl": "Na sahāyena pāpena — solitary struggle is preferable to bad company."},
        {"q": "What does the name Cakkhupāla mean?",
         "opts": [
             "Eye-guardian",
             "Ram's head",
             "Given by the lord",
             "One who has given up what is dear"],
         "correct": 0,
         "expl": "Cakkhu ('eye') plus pāla ('guardian')."},
        {"q": "How does this reading guide characterize the relationship between this name and this verse's content?",
         "opts": [
             "A close match, like Vacchapāla or Hatthārohaputta",
             "A striking contrast — the name means 'eye-guardian', but the verse describes blindness",
             "No connection is discussed",
             "The name is a direct quotation from the verse"],
         "correct": 1,
         "expl": "The opposite of the name/verse alignment seen elsewhere in this collection."},
        {"q": "Does this reading guide confirm the later Dhammapada commentary's story about a blind monk named Cakkhupāla as applying to this specific verse?",
         "opts": [
             "Yes, treats it as an established, confirmed fact",
             "It denies any such legend exists",
             "It asserts the legend is definitely about a different Cakkhupāla",
             "No — it notes the legend exists in the wider tradition without treating it as confirmed here"],
         "correct": 3,
         "expl": "A post-canonical text, not translated on this site, held at a careful distance."},
        {"q": "What does 'kantāra' mean?",
         "opts": [
             "A monastery",
             "A river crossing",
             "Wilderness, desolate wasteland",
             "A market town"],
         "correct": 2,
         "expl": "Describing the road the speaker is traveling."},
        {"q": "What does 'hatanetta' mean?",
         "opts": [
             "Ruined eyes",
             "Sharp hearing",
             "Steady hands",
             "Strong legs"],
         "correct": 0,
         "expl": "Hata ('destroyed') plus netta ('eyes')."},
        {"q": "What does the verse imply matters more than physical hardship?",
         "opts": [
             "Wealth",
             "Speed of travel",
             "The company one keeps",
             "The distance traveled"],
         "correct": 2,
         "expl": "Crawling is acceptable; wicked company is not."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The ninth poem",
             "The fifth poem"],
         "correct": 3,
         "expl": "Immediately after Mettaji's verse."},
    ],
    marginalia=[
        ("Blind, still moving", [
            "eyes ruined, road desolate —",
            "crawling, if it comes to that"
        ]),
        ("A name, contradicted", [
            "eye-guardian, the name says —",
            "the verse says otherwise"
        ]),
        ("A legend, kept at arm's length", [
            "a later story, elsewhere told —",
            "not confirmed here"
        ]),
        ("Company, the real condition", [
            "alone, if it must be —",
            "never with the wicked"
        ]),
    ],
    further=[
        '<a href="%s/thag1.95/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.94.html">Thag 1.94 &mdash; Mettaji</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.96.html">Thag 1.96 &mdash; Kha&#7751;&#7693;asumana</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.96 — Kha&#7751;&#7693;asumana
# --------------------------------------------------------------------------- #
page(
    1, 96, "Kha&#7751;&#7693;asumana", "Kha&#7751;&#7693;asumana",
    meta_title="Thag 1.96 — Khaṇḍasumana | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Khaṇḍasumana's verse, an offering of one flower spent over "
        "eight hundred million heavenly years before its remainder "
        "carries him to final quenching. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 6 of 10",
    glance=[
        ("Setting", "A retrospective account spanning an immense "
                    "cosmic timescale"),
        ("Speaker", "Khaṇḍasumana, in the first person"),
        ("Form", "One four-line verse, treating merit as a "
                 "resource that gets spent"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one striking number"),
    ],
    why=(
        "Khaṇḍasumana offered a single flower, then spent eighty "
        "koṭi &mdash; eight hundred million &mdash; years enjoying "
        "the heavens; with what was left over of that offering's "
        "result, he says, he has become quenched. It is the most "
        "concrete large number named anywhere in this collection so "
        "far."),
    guide=[
        ("One flower, eight hundred million years", [
            "Asīti vassakoṭiyo, &lsquo;eighty koṭi years&rsquo; "
            "&mdash; koṭi being a standard large-number unit in "
            "Indian counting, ten million &mdash; gives a specific "
            "figure where most of this collection's verses speak "
            "only in general terms of &lsquo;countless rebirths&rsquo; "
            "or &lsquo;many lifetimes&rsquo;. The disproportion is "
            "the point: a single flower (ekapuppha), and eight "
            "hundred million years of heavenly enjoyment as its "
            "result."]),
        ("Merit as a resource, spent to the end", [
            "Sesakenamhi nibbuto, &lsquo;with what's left over I've "
            "become quenched&rsquo;, treats the offering's result "
            "almost like a store of currency: eight hundred million "
            "years of heavenly life drew down most of it, and the "
            "remainder was still enough to carry Khaṇḍasumana to "
            "final liberation in this life. This economic framing "
            "&mdash; merit as something spent rather than a cause "
            "simply ripening &mdash; is distinctive among this "
            "collection's many descriptions of how liberation was "
            "reached."]),
        ("A name that matches its own gift", [
            "Khaṇḍasumana likely reads as khaṇḍa (&lsquo;piece, "
            "fragment&rsquo;) plus sumana, which can mean either "
            "&lsquo;good-minded&rsquo; or, as a flower name, "
            "&lsquo;sumanā&rsquo; (jasmine) &mdash; giving "
            "&lsquo;a piece of a jasmine flower&rsquo; as a plausible "
            "reading. Set against a verse entirely about offering "
            "&lsquo;a single flower&rsquo;, the name and the verse's "
            "own content align, unlike the previous poem in this "
            "chapter (Thag 1.95, Cakkhupāla), where they stood in "
            "contrast."]),
    ],
    terms=[
        ("ekapuppha",
         "&ldquo;a single flower&rdquo; &mdash; eka (&lsquo;one&rsquo;) "
         "plus puppha (&lsquo;flower&rsquo;), the verse's opening "
         "offering."),
        ("koṭi",
         "a standard large-number unit in Indian counting, equal to "
         "ten million."),
        ("paricāreti",
         "&ldquo;amuses oneself, enjoys&rdquo; &mdash; the verb "
         "describing the heavenly enjoyment this offering produced."),
        ("sesaka",
         "&ldquo;remainder, what's left over&rdquo; &mdash; what the "
         "verse says finally carried Khaṇḍasumana to quenching."),
        ("Khaṇḍasumana",
         "possibly &ldquo;a piece of a jasmine flower&rdquo; &mdash; "
         "khaṇḍa (&lsquo;piece&rsquo;) plus sumana (a flower name)."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.96:1.1-1.4"),
    ],
    quiz=[
        {"q": "What did the speaker offer, according to this verse?",
         "opts": [
             "A single flower",
             "A bowl of rice",
             "A robe",
             "A large sum of gold"],
         "correct": 0,
         "expl": "Ekapuppham cajitvāna, the verse's opening act."},
        {"q": "How many years does the verse say this offering's result was enjoyed in the heavens?",
         "opts": [
             "Eighty years",
             "Eight hundred years",
             "Eight hundred million years",
             "Eight thousand years"],
         "correct": 2,
         "expl": "Asīti vassakoṭiyo, 'eighty koṭi', eighty times ten million."},
        {"q": "What does 'koṭi' mean as a number?",
         "opts": [
             "One hundred",
             "One thousand",
             "One million",
             "Ten million"],
         "correct": 3,
         "expl": "A standard large-number unit in Indian counting."},
        {"q": "How does this verse describe the offering's result being used up?",
         "opts": [
             "As a store of currency, spent down until only a remainder was left",
             "As a debt that had to be repaid",
             "As a punishment to be endured",
             "The verse says the result was never used at all"],
         "correct": 0,
         "expl": "An economic framing of merit, distinctive among this collection's verses."},
        {"q": "What finally carried the speaker to quenching, according to the verse?",
         "opts": [
             "A second offering",
             "The remainder of the first offering's result",
             "A teacher's direct instruction",
             "A vision in meditation"],
         "correct": 1,
         "expl": "Sesakenamhi nibbuto, 'with what's left over I've become quenched'."},
        {"q": "What does the name Khaṇḍasumana possibly mean?",
         "opts": [
             "A piece of a jasmine flower",
             "Son of an elephant-rider",
             "Ram's head",
             "One who has given up what is dear"],
         "correct": 0,
         "expl": "Khaṇḍa ('piece') plus sumana (a flower name)."},
        {"q": "How does this reading guide relate this name to this verse's content?",
         "opts": [
             "It finds a contradiction, as with the previous poem's name",
             "It finds an alignment — the name and the single-flower offering point in the same direction",
             "It finds no connection at all",
             "The name is a direct quotation from the verse"],
         "correct": 1,
         "expl": "Unlike Cakkhupāla, the poem immediately before this one, whose name contrasted with its own verse."},
        {"q": "What does 'paricāreti' mean?",
         "opts": [
             "Suffers, endures",
             "Teaches, instructs",
             "Fasts, abstains",
             "Amuses oneself, enjoys"],
         "correct": 3,
         "expl": "Describing the heavenly enjoyment this offering produced."},
        {"q": "What is unusual about this verse's number, compared to most other verses in this collection?",
         "opts": [
             "It is the only verse to mention any number at all",
             "It is the smallest number named anywhere in the collection",
             "It contradicts a number given in an earlier verse",
             "It gives a specific, concrete figure, where most verses speak only of 'countless' rebirths"],
         "correct": 3,
         "expl": "The most concrete large number named anywhere in this collection so far."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The sixth poem",
             "The second poem"],
         "correct": 2,
         "expl": "Immediately after Cakkhupāla's verse."},
    ],
    marginalia=[
        ("One flower, an immense return", [
            "eighty koṭi years —",
            "heaven, from a single offering"
        ]),
        ("Merit, spent to the last", [
            "a store drawn down —",
            "the remainder, enough"
        ]),
        ("A name, matching its gift", [
            "a petal, perhaps —",
            "the same flower, both times"
        ]),
        ("A number, rare in this collection", [
            "most verses say 'countless' —",
            "this one, exactly"
        ]),
    ],
    further=[
        '<a href="%s/thag1.96/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.95.html">Thag 1.95 &mdash; Cakkhup&amacr;la</a> '
        "&mdash; the poem immediately before this one, whose name "
        "contrasted with its own verse, unlike this one.",
        '<a href="thag-1.97.html">Thag 1.97 &mdash; Tissa (2nd)</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.97 — Tissa (2nd)
# --------------------------------------------------------------------------- #
page(
    1, 97, "Tissa", "Tissa (2nd)",
    meta_title="Thag 1.97 — Tissa (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Tissa's verse, giving up bronze and gold bowls for one made "
        "of clay, and framing the exchange as a 'second "
        "consecration'. From Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 7 of 10",
    glance=[
        ("Setting", "A retrospective account of exchanging precious "
                    "bowls for a clay one"),
        ("Speaker", "Tissa (2nd), in the first person"),
        ("Form", "One four-line verse, closing on an unexpected "
                 "reframing"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one striking word choice"),
    ],
    why=(
        "Tissa gives up a valuable bronze bowl and a precious golden "
        "one, taking instead a bowl made of clay &mdash; and calls "
        "the exchange his &lsquo;second initiation&rsquo; (dutiya "
        "abhiseka), a word ordinarily used for a formal consecration "
        "or royal anointing. What sounds like impoverishment is "
        "described in the language of ascension."),
    guide=[
        ("Renunciation reframed as coronation", [
            "Abhiseka is the standard word for a formal consecration "
            "ceremony, traditionally associated with anointing a "
            "king. Applying it here, to taking up a plain clay alms "
            "bowl in place of bronze and gold, inverts the word's "
            "usual direction: instead of ascending to worldly power, "
            "the verse frames going forth into monastic poverty in "
            "the vocabulary of royal ceremony."]),
        ("A first consecration, implied but never described", [
            "Calling this exchange his &lsquo;second&rsquo; "
            "consecration implies a first one happened, but the "
            "verse says nothing about what it was. This reading "
            "guide does not speculate about Tissa's prior life "
            "&mdash; whether the phrase points to an actual earlier "
            "ceremony or is simply a rhetorical framing for the "
            "verse's own effect &mdash; since nothing in the text or "
            "any surviving comment settles the question."]),
        ("Bronze, gold, then clay", [
            "The verse itemizes its materials with unusual "
            "specificity for this collection: satapala kaṁsa "
            "(&lsquo;a hundred-pala bronze bowl&rsquo;, pala being a "
            "unit of weight), a golden one, and finally mattikāpatta "
            "(&lsquo;a bowl made of clay&rsquo;). Most verses in this "
            "collection deal in general images rather than itemized "
            "possessions; this one names its objects precisely before "
            "setting them aside."]),
    ],
    terms=[
        ("kaṁsa",
         "&ldquo;bronze&rdquo; &mdash; the material of the first "
         "bowl given up."),
        ("sovaṇṇa",
         "&ldquo;golden&rdquo; &mdash; the material of the second "
         "bowl given up."),
        ("mattikāpatta",
         "&ldquo;a bowl made of clay&rdquo; &mdash; mattikā "
         "(&lsquo;clay&rsquo;) plus patta (&lsquo;bowl&rsquo;), what "
         "was taken up instead."),
        ("abhiseka",
         "&ldquo;consecration, anointing&rdquo; &mdash; ordinarily "
         "associated with a royal ceremony, applied here to taking "
         "up the clay bowl."),
        ("dutiya",
         "&ldquo;second&rdquo; &mdash; the ordinal marking this as "
         "not Tissa's first such consecration."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.97:1.1-1.4"),
    ],
    quiz=[
        {"q": "What two precious materials does the verse say Tissa gave up?",
         "opts": [
             "Bronze and gold",
             "Silver and ivory",
             "Silk and jade",
             "Iron and copper"],
         "correct": 0,
         "expl": "Satapalaṁ kaṁsaṁ and sovaṇṇaṁ satarājikaṁ, the verse's first two objects."},
        {"q": "What did Tissa take up instead?",
         "opts": [
             "A wooden bowl",
             "No bowl at all",
             "A bowl made of clay",
             "A bowl of silver"],
         "correct": 2,
         "expl": "Mattikāpattaṁ, the verse's third object."},
        {"q": "What word does the verse use to describe this exchange, and what does it ordinarily mean?",
         "opts": [
             "Nibbāna, ordinarily meaning 'extinguishment'",
             "Abhiseka, ordinarily meaning a formal consecration or royal anointing",
             "Dukkha, ordinarily meaning 'suffering'",
             "Paviveka, ordinarily meaning 'seclusion'"],
         "correct": 1,
         "expl": "A word usually associated with ascending to worldly power, applied here in reverse."},
        {"q": "Does the verse describe what Tissa's 'first' consecration was?",
         "opts": [
             "Yes, in detail",
             "No — the verse implies one happened but says nothing about it",
             "Yes, but only in a single word",
             "The verse denies any first consecration occurred"],
         "correct": 1,
         "expl": "This reading guide does not speculate about Tissa's prior life."},
        {"q": "How does this verse's level of detail about objects compare to most other verses in this collection?",
         "opts": [
             "Unusually specific — most verses use general images rather than itemized possessions",
             "Typical — most verses itemize possessions this precisely",
             "The verse names no objects at all",
             "It is less specific than most other verses"],
         "correct": 0,
         "expl": "A hundred-pala bronze bowl, a golden one, and a clay one, named precisely."},
        {"q": "What does 'kaṁsa' mean?",
         "opts": [
             "Bronze",
             "Silver",
             "Clay",
             "Wood"],
         "correct": 0,
         "expl": "The material of the first bowl given up."},
        {"q": "What does 'mattikāpatta' mean?",
         "opts": [
             "A golden bowl",
             "A bronze bowl",
             "A bowl made of clay",
             "A jeweled bowl"],
         "correct": 2,
         "expl": "Mattikā ('clay') plus patta ('bowl')."},
        {"q": "What does 'dutiya' mean?",
         "opts": [
             "First",
             "Last",
             "Every",
             "Second"],
         "correct": 3,
         "expl": "The ordinal marking this as not Tissa's first such consecration."},
        {"q": "What effect does calling this exchange a 'consecration' have, according to this reading guide?",
         "opts": [
             "It has no particular effect",
             "It confirms Tissa was literally crowned king",
             "It denies that any exchange took place",
             "It frames what sounds like impoverishment in the language of royal ascension"],
         "correct": 3,
         "expl": "The word's usual direction is inverted."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The third poem",
             "The seventh poem"],
         "correct": 3,
         "expl": "Immediately after Khaṇḍasumana's verse."},
    ],
    marginalia=[
        ("Bronze and gold, set down", [
            "precious bowls, given up —",
            "clay, taken instead"
        ]),
        ("A coronation, inverted", [
            "consecration, the word says —",
            "into poverty, not power"
        ]),
        ("A first ceremony, unnamed", [
            "'second', the verse claims —",
            "the first left untold"
        ]),
        ("Objects, named precisely", [
            "bronze, gold, clay —",
            "unlike most verses here"
        ]),
    ],
    further=[
        '<a href="%s/thag1.97/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.96.html">Thag 1.96 &mdash; Kha&#7751;&#7693;asumana</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.98.html">Thag 1.98 &mdash; Abhaya</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.98 — Abhaya
# --------------------------------------------------------------------------- #
page(
    1, 98, "Abhaya", "Abhaya",
    meta_title="Thag 1.98 — Abhaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Abhaya's verse, tracing how mindfulness is lost at the eye "
        "and grows into the root of rebirth. From Ru-Yi Meditation "
        "Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 8 of 10",
    glance=[
        ("Setting", "No narrative setting; a step-by-step account of "
                    "how mindfulness is lost at the eye"),
        ("Speaker", "An unnamed voice describing, in general terms, "
                    "what happens to &lsquo;one who&rsquo; attends to "
                    "a pleasant sight"),
        ("Form", "One six-line verse, a chain of cause and effect"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, a precise causal chain"),
    ],
    why=(
        "Abhaya traces a chain: seeing a sight, mindfulness is lost; "
        "attending to its pleasant feature, desire arises; "
        "experiencing it with an infatuated mind, clinging follows; "
        "and from there, defilements grow, &lsquo;leading to the "
        "root of rebirth&rsquo;. Each step follows plainly from the "
        "one before it."),
    guide=[
        ("Mindfulness lost at the eye", [
            "The verse's six lines trace a single causal sequence "
            "with no gaps: seeing (disvā) a sight (rūpa) is followed "
            "by lost mindfulness (sati muṭṭhā); attending to its "
            "pleasant feature (piyaṁ nimittaṁ manasikaroto) is "
            "followed by an infatuated mind (sāratta); experiencing "
            "it that way is followed by clinging (ajjhosa tiṭṭhati); "
            "and clinging is followed by growing defilements "
            "(āsavā), which lead to bhavamūla, &lsquo;the root of "
            "[continued] existence&rsquo;. Each link follows plainly "
            "from the one before it, without commentary or "
            "elaboration."]),
        ("Grammatically general, translated as 'you'", [
            "Sujato's English renders this verse in the second "
            "person throughout &mdash; &lsquo;when you see a "
            "sight...&rsquo; &mdash; but the Pali itself uses "
            "impersonal constructions: disvā is a gerund "
            "(&lsquo;having seen&rsquo;), and manasikaroto is a "
            "participle describing &lsquo;one who attends&rsquo;, "
            "with no explicit pronoun for who this is. The English "
            "&lsquo;you&rsquo; is a translator's choice for "
            "readability, closer in grammatical shape to the general, "
            "third-person teaching register of earlier verses like "
            "Thag 1.71 and Thag 1.74 than to true second-person "
            "address."]),
        ("A name already used as a common word", [
            "Abhaya (&lsquo;fearless, free from danger&rsquo;) is "
            "this elder's own name, but the same word already "
            "appeared as ordinary vocabulary earlier in this chapter "
            "&mdash; sivāni abhayāni ca, &lsquo;safe and free of "
            "peril&rsquo;, in Thag 1.82's blessing to a child. There, "
            "abhaya described a place to be sought; here, it is a "
            "person's name."]),
    ],
    terms=[
        ("rūpa",
         "&ldquo;a sight, a visible form&rdquo; &mdash; what "
         "triggers the chain this verse describes."),
        ("nimitta",
         "&ldquo;feature, sign&rdquo; &mdash; here, the "
         "&lsquo;pleasant feature&rsquo; of the sight that draws "
         "attention."),
        ("sāratta",
         "&ldquo;full of desire, infatuated&rdquo; &mdash; the state "
         "of mind that follows lost mindfulness."),
        ("āsava",
         "&ldquo;defilement, taint&rdquo; &mdash; what this verse "
         "says grows once clinging has taken hold."),
        ("bhavamūla",
         "&ldquo;the root of [continued] existence&rdquo; &mdash; "
         "bhava (&lsquo;existence&rsquo;) plus mūla "
         "(&lsquo;root&rsquo;), where this chain of causes leads."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.98:1.1-1.6"),
    ],
    quiz=[
        {"q": "What is the first step in this verse's causal chain?",
         "opts": [
             "Seeing a sight, mindfulness is lost",
             "Hearing a sound, mindfulness is lost",
             "Clinging arises with no cause",
             "Defilements appear before any sight is seen"],
         "correct": 0,
         "expl": "Rūpaṁ disvā sati muṭṭhā, the verse's opening line."},
        {"q": "What does the verse say this chain ultimately leads to?",
         "opts": [
             "Wealth and prosperity",
             "The root of rebirth",
             "A pleasant dream",
             "Immediate liberation"],
         "correct": 1,
         "expl": "Bhavamūlopagāmino, the verse's closing phrase."},
        {"q": "Does the Pali grammar of this verse use an explicit second-person pronoun ('you')?",
         "opts": [
             "Yes, throughout",
             "No — it uses gerunds and participles describing 'one who...' generally",
             "Only in the final line",
             "The verse has no verbs at all"],
         "correct": 1,
         "expl": "Sujato's 'you' is a translation choice, not a literal match to the Pali's grammatical person."},
        {"q": "What does this reading guide compare this verse's grammatical register to?",
         "opts": [
             "The direct address of Thag 1.83 (Sīha)",
             "The rhetorical question of Thag 1.84 (Nīta)",
             "The general, third-person teaching register of Thag 1.71 and Thag 1.74",
             "The homage of Thag 1.94 (Mettaji)"],
         "correct": 2,
         "expl": "Closer in grammatical shape to impersonal teaching than to true second-person address."},
        {"q": "Where did the word 'abhaya' already appear earlier in this chapter, before becoming this elder's name?",
         "opts": [
             "In Thag 1.91, describing food",
             "In Thag 1.95, describing blindness",
             "Nowhere else in this chapter",
             "In Thag 1.82, describing a safe place in Kassapa's blessing to a child"],
         "correct": 3,
         "expl": "There as ordinary vocabulary; here as a person's name."},
        {"q": "What does 'sāratta' mean?",
         "opts": [
             "Full of desire, infatuated",
             "Completely calm",
             "Newly ordained",
             "Physically exhausted"],
         "correct": 0,
         "expl": "The state of mind that follows lost mindfulness."},
        {"q": "What does 'bhavamūla' mean?",
         "opts": [
             "The end of suffering",
             "A type of meditation",
             "A monastic rule",
             "The root of continued existence"],
         "correct": 3,
         "expl": "Bhava ('existence') plus mūla ('root')."},
        {"q": "What does 'āsava' mean?",
         "opts": [
             "Defilement, taint",
             "Wisdom, insight",
             "A monastic robe",
             "A begging bowl"],
         "correct": 0,
         "expl": "What this verse says grows once clinging has taken hold."},
        {"q": "How many distinct steps does this verse's causal chain contain?",
         "opts": [
             "Two",
             "Three",
             "About five, from seeing to the root of rebirth",
             "Ten"],
         "correct": 2,
         "expl": "Seeing, lost mindfulness, desire, clinging, and growing defilements."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The closing poem",
             "The fourth poem",
             "The eighth poem"],
         "correct": 3,
         "expl": "Immediately after Tissa's verse."},
    ],
    marginalia=[
        ("A chain, link by link", [
            "seeing, then lost —",
            "desire, then clinging"
        ]),
        ("You, or one who", [
            "the English says 'you' —",
            "the Pali says 'one who'"
        ]),
        ("A name, already used", [
            "safe and free of peril —",
            "now, simply his name"
        ]),
        ("Where the root grows", [
            "defilements, fed —",
            "existence, taking hold"
        ]),
    ],
    further=[
        '<a href="%s/thag1.98/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.82.html">Thag 1.82 &mdash; Kassapa</a> '
        "&mdash; an earlier poem in this chapter using 'abhaya' as an "
        "ordinary word, before it becomes this elder's name.",
        '<a href="thag-1.97.html">Thag 1.97 &mdash; Tissa (2nd)</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="thag-1.99.html">Thag 1.99 &mdash; Uttiya (3rd)</a> '
        "&mdash; the next poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.99 — Uttiya (3rd)
# --------------------------------------------------------------------------- #
page(
    1, 99, "Uttiya", "Uttiya (3rd)",
    meta_title="Thag 1.99 — Uttiya (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Uttiya's verse, repeating Thag 1.98's causal chain almost "
        "word for word, but at the ear rather than the eye. From "
        "Ru-Yi Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 9 of 10",
    glance=[
        ("Setting", "No narrative setting; the same causal chain as "
                    "the poem immediately before this one, at a "
                    "different sense door"),
        ("Speaker", "An unnamed voice describing, in general terms, "
                    "what happens to &lsquo;one who&rsquo; attends to "
                    "a pleasant sound"),
        ("Form", "One six-line verse, four lines shared word for "
                 "word with Thag 1.98"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, an exact formulaic overlap"),
    ],
    why=(
        "This verse repeats Thag 1.98's entire causal chain almost "
        "word for word &mdash; lost mindfulness, desire, clinging, "
        "growing defilements &mdash; changing only the sense door "
        "involved: hearing a sound in place of seeing a sight, and "
        "&lsquo;transmigration&rsquo; in place of &lsquo;the root of "
        "rebirth&rsquo; in its final line."),
    guide=[
        ("The same chain, at a different sense door", [
            "Lines two through five of this verse &mdash; piyaṁ "
            "nimittaṁ manasikaroto, sārattacitto vedeti, tañca "
            "ajjhosa tiṭṭhati, tassa vaḍḍhanti āsavā &mdash; are word "
            "for word identical to Thag 1.98, the poem immediately "
            "before this one. Only two things differ: the opening "
            "line swaps rūpaṁ disvā (&lsquo;seeing a sight&rsquo;) "
            "for saddaṁ sutvā (&lsquo;hearing a sound&rsquo;), and "
            "the closing line swaps bhavamūlopagāmino (&lsquo;leading "
            "to the root of rebirth&rsquo;) for saṁsāraṁ upagāmino "
            "(&lsquo;leading to transmigration&rsquo;) &mdash; two "
            "near-synonymous endings for what is otherwise the "
            "identical chain."]),
        ("A fragment of a longer sequence, most likely", [
            "The wider canon standardly analyzes experience through "
            "six sense doors &mdash; eye, ear, nose, tongue, body, "
            "and mind. Two consecutive poems differing only in which "
            "sense door is named suggests these may be surviving "
            "fragments of what was once a longer formulaic sequence, "
            "possibly covering more of the six. This reading guide "
            "treats that as a plausible inference, not something "
            "confirmed by any surviving comment or by the text "
            "itself, which gives no indication that further members "
            "of such a sequence ever existed here."]),
        ("Uttiya, a third occurrence", [
            "This is the third elder in this collection to carry the "
            "name Uttiya, following two earlier occurrences, "
            "continuing the same disambiguation pattern already seen "
            "with Puṇṇa, Tissa, and Devasabha."]),
    ],
    terms=[
        ("sadda",
         "&ldquo;sound&rdquo; &mdash; the sense object this verse "
         "substitutes for Thag 1.98's rūpa, &lsquo;sight&rsquo;."),
        ("piyaṁ nimittaṁ",
         "&ldquo;pleasant feature&rdquo; &mdash; identical wording to "
         "Thag 1.98, describing what draws attention."),
        ("sārattacitta",
         "&ldquo;a mind full of desire&rdquo; &mdash; identical "
         "wording to Thag 1.98's description of the mind's state."),
        ("saṁsāra",
         "&ldquo;transmigration, the cycle of rebirth&rdquo; &mdash; "
         "this verse's closing term, in place of Thag 1.98's "
         "bhavamūla."),
        ("Uttiya",
         "the name of the third elder in this collection to carry "
         "it, after two earlier occurrences."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.99:1.1-1.6"),
    ],
    quiz=[
        {"q": "What sense door does this verse's opening line involve, in place of Thag 1.98's sight?",
         "opts": [
             "Touch",
             "Smell",
             "Taste",
             "Sound"],
         "correct": 3,
         "expl": "Saddaṁ sutvā, 'hearing a sound', replacing rūpaṁ disvā."},
        {"q": "How much of this verse's wording is identical to Thag 1.98?",
         "opts": [
             "None of it",
             "Only the first line",
             "The entire verse, with no differences at all",
             "Lines two through five, word for word"],
         "correct": 3,
         "expl": "Only the opening and closing lines differ."},
        {"q": "What does this verse's closing line say, in place of Thag 1.98's 'the root of rebirth'?",
         "opts": [
             "Transmigration",
             "Wealth",
             "Enlightenment",
             "A pleasant dream"],
         "correct": 0,
         "expl": "Saṁsāraṁ upagāmino, a near-synonymous ending."},
        {"q": "What does this reading guide suggest these two consecutive poems may represent?",
         "opts": [
             "Two completely unrelated verses that happen to be adjacent",
             "Possible surviving fragments of a longer formulaic sequence covering more of the six sense doors",
             "A confirmed, complete set covering all six senses",
             "A scribal duplication error"],
         "correct": 1,
         "expl": "A plausible inference, not confirmed by any surviving comment."},
        {"q": "How many sense doors does the wider canon standardly analyze experience through?",
         "opts": [
             "Four",
             "Five",
             "Six",
             "Eight"],
         "correct": 2,
         "expl": "Eye, ear, nose, tongue, body, and mind."},
        {"q": "What does 'sadda' mean?",
         "opts": [
             "Sound",
             "Sight",
             "Smell",
             "Taste"],
         "correct": 0,
         "expl": "The sense object this verse's opening line names."},
        {"q": "How many elders in this collection have now carried the name Uttiya, including this one?",
         "opts": [
             "One",
             "Two",
             "Three",
             "Five"],
         "correct": 2,
         "expl": "The same disambiguation pattern already seen with Puṇṇa, Tissa, and Devasabha."},
        {"q": "What does 'sārattacitta' mean?",
         "opts": [
             "A calm, undisturbed mind",
             "A mind full of desire",
             "A wandering, distracted mind",
             "A sleeping mind"],
         "correct": 1,
         "expl": "Identical wording to Thag 1.98's description of the mind's state."},
        {"q": "Does this verse's grammar use an explicit second-person pronoun, the way Sujato's English translation reads?",
         "opts": [
             "No — like Thag 1.98, it uses impersonal gerunds and participles",
             "Yes, throughout",
             "Only in the closing line",
             "The verse has no grammatical subject at all"],
         "correct": 0,
         "expl": "The same grammatical pattern noted in Thag 1.98."},
        {"q": "Where does this poem fall in Chapter Ten?",
         "opts": [
             "The opening poem",
             "The fifth poem",
             "The closing poem",
             "The ninth poem"],
         "correct": 3,
         "expl": "Immediately after Abhaya's verse, and immediately before the chapter's close."},
    ],
    marginalia=[
        ("The same chain, once more", [
            "four lines, unchanged —",
            "only the door is different"
        ]),
        ("Sound, where sight once was", [
            "heard, not seen —",
            "the rest, identical"
        ]),
        ("A sequence, perhaps broken off", [
            "two doors named —",
            "four more, unwritten here"
        ]),
        ("A third bearer of the name", [
            "Uttiya, once more —",
            "the third of this collection"
        ]),
    ],
    further=[
        '<a href="%s/thag1.99/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.98.html">Thag 1.98 &mdash; Abhaya</a> '
        "&mdash; the poem immediately before this one, sharing four "
        "lines of identical wording.",
        '<a href="thag-1.100.html">Thag 1.100 &mdash; Devasabha (2nd)</a> '
        "&mdash; the next and final poem in this chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)


# --------------------------------------------------------------------------- #
# Thag 1.100 — Devasabha (2nd)
# --------------------------------------------------------------------------- #
page(
    1, 100, "Devasabha", "Devasabha (2nd)",
    meta_title="Thag 1.100 — Devasabha (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Devasabha's verse, closing Chapter Ten with the image of "
        "someone 'festooned with the flowers of liberation', and "
        "completing a pair begun in Chapter Nine. From Ru-Yi "
        "Meditation Center."),
    vagga="The Book of the Ones &middot; Chapter Ten &middot; Poem 10 of 10",
    glance=[
        ("Setting", "A description, closing this chapter's tenth "
                    "and final poem"),
        ("Speaker", "An unnamed voice describing, in grammatically "
                    "third-person terms, a person accomplished in "
                    "practice"),
        ("Form", "One four-line verse, followed by the chapter's "
                 "formulaic double closing"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a "
                              "specific matching text for this poem in "
                              "other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "plain vocabulary, one striking image"),
    ],
    why=(
        "Devasabha closes Chapter Ten describing someone accomplished "
        "in the four right efforts, ranging in mindfulness "
        "meditation, &lsquo;festooned with the flowers of "
        "liberation&rsquo;, who will be fully quenched. It also "
        "completes a pair begun in Chapter Nine: Thag 1.89, Devasabha "
        "(1st), and this verse are the two halves of the same "
        "disambiguated name."),
    guide=[
        ("Completing a pair begun last chapter", [
            "Thag 1.89 (Devasabha, 1st) was a first-person testimony "
            "listing five obstacles overcome &mdash; bogs, chasms, "
            "floods, ties, conceit. This verse, closing the pair, is "
            "the opposite in voice: entirely a description of someone "
            "else, with no first-person claim at all. The two "
            "same-named elders' verses could hardly differ more in "
            "register."]),
        ("Grammatically third person, translated as 'you'", [
            "Sammappadhānasampanno, satipaṭṭhānagocaro, and the "
            "verse's other descriptive words are nominative singular "
            "forms &mdash; grammatically describing &lsquo;he&rsquo; "
            "or &lsquo;one who&rsquo;, not addressing &lsquo;you&rsquo; "
            "directly. Sujato's English nonetheless reads as direct "
            "address throughout. This is the third poem in this "
            "chapter, after Thag 1.98 and Thag 1.99, where the "
            "English &lsquo;you&rsquo; represents a Pali construction "
            "that is grammatically impersonal or third person rather "
            "than a literal second-person address."]),
        ("Two flowers, two chapters apart", [
            "Vimuttikusumasañchanno, &lsquo;festooned with the "
            "flowers of liberation&rsquo;, closes this chapter with a "
            "metaphorical bloom &mdash; liberation itself pictured as "
            "flowers covering the person who has attained it. This "
            "echoes, without repeating, Thag 1.96's actual single "
            "flower offering earlier in this same chapter: one a "
            "literal gift with an immense karmic result, the other a "
            "figurative garland standing for the result itself."]),
        ("The chapter's double closing", [
            "As in every chapter so far, two more lines follow the "
            "poem itself, both left untranslated by Sujato: vaggo "
            "dasamo (&lsquo;the tenth chapter [ends]&rsquo;), then an "
            "uddāna listing all ten names. This uddāna adds two more "
            "epithets not found in either elder's own verse: Mettaji "
            "becomes mettajī muni (&lsquo;Mettaji the sage&rsquo;), "
            "and Uttiya becomes uttiyo mahāpañño (&lsquo;Uttiya of "
            "great wisdom&rsquo;) &mdash; continuing the same pattern "
            "already seen in the uddānas closing Chapter Eight and "
            "Chapter Nine."]),
    ],
    terms=[
        ("sammappadhāna",
         "&ldquo;right effort&rdquo; &mdash; traditionally counted "
         "as four, a standard doctrinal category."),
        ("satipaṭṭhāna",
         "&ldquo;mindfulness meditation&rdquo;, literally "
         "&ldquo;establishment of mindfulness&rdquo; &mdash; also "
         "traditionally counted as four."),
        ("vimuttikusuma",
         "&ldquo;flower of liberation&rdquo; &mdash; vimutti "
         "(&lsquo;liberation&rsquo;) plus kusuma "
         "(&lsquo;flower&rsquo;), this verse's central image."),
        ("sañchanna",
         "&ldquo;covered, festooned, strewn over&rdquo; &mdash; "
         "describing how these flowers cover the person."),
        ("parinibbissati",
         "&ldquo;will be fully quenched&rdquo; &mdash; a future-tense "
         "verb, closing the verse."),
    ],
    text_intro=(
        "The text in full: one verse, with no separate attribution "
        "line in this chapter. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "thag1.100:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does this verse say the person it describes is accomplished in?",
         "opts": [
             "The four right efforts",
             "The five hindrances",
             "The three roots of unwholesomeness",
             "The eight worldly conditions"],
         "correct": 0,
         "expl": "Sammappadhānasampanno, the verse's opening description."},
        {"q": "How does this verse's voice compare to Thag 1.89, Devasabha (1st)?",
         "opts": [
             "Both are identical first-person testimonies",
             "Thag 1.89 was first-person testimony; this verse is entirely third-person description",
             "This verse is first-person testimony; Thag 1.89 was third-person description",
             "Neither verse has any discernible speaker"],
         "correct": 1,
         "expl": "The two same-named elders' verses differ sharply in register."},
        {"q": "What image does this verse use for liberation?",
         "opts": [
             "Flowers festooning the person who has attained it",
             "A river reaching the sea",
             "A fire being extinguished",
             "A bird crossing the sky"],
         "correct": 0,
         "expl": "Vimuttikusumasañchanno, 'festooned with the flowers of liberation'."},
        {"q": "How does this image relate to Thag 1.96, earlier in this same chapter?",
         "opts": [
             "It repeats Thag 1.96's exact wording",
             "It contradicts Thag 1.96 directly",
             "It echoes, without repeating, Thag 1.96's earlier flower offering — one literal, one figurative",
             "There is no relationship at all"],
         "correct": 2,
         "expl": "A literal single-flower gift, versus a metaphorical garland of liberation."},
        {"q": "What two untranslated lines follow this verse, as in every chapter so far?",
         "opts": [
             "A dedication to the Buddha",
             "A second verse by the same elder",
             "A list of monastic rules",
             "A chapter-closing marker and a summary verse (uddāna) listing all ten names"],
         "correct": 3,
         "expl": "Vaggo dasamo, then the uddāna."},
        {"q": "What epithet does the chapter's uddāna add to Mettaji's name?",
         "opts": [
             "'Isi', the sage",
             "'Mahā', the great",
             "No epithet is added",
             "'Muni', the sage"],
         "correct": 3,
         "expl": "Mettajī muni, not found in his own verse."},
        {"q": "What epithet does the uddāna add to Uttiya's name?",
         "opts": [
             "'Isi', the sage",
             "'Ārohaputta', son of an elephant-rider",
             "'Mahāpañño', of great wisdom",
             "No epithet is added"],
         "correct": 2,
         "expl": "Uttiyo mahāpañño, not found in his own verse."},
        {"q": "What does 'sañchanna' mean?",
         "opts": [
             "Covered, festooned, strewn over",
             "Completely empty",
             "Newly built",
             "Broken apart"],
         "correct": 0,
         "expl": "Describing how the flowers of liberation cover the person."},
        {"q": "Grammatically, are this verse's descriptive words nominative (describing 'he/one who') or vocative (addressing 'you')?",
         "opts": [
             "Vocative, directly addressing the listener",
             "Nominative, grammatically describing a third person",
             "Neither — the verse has no such forms",
             "Both forms are used equally"],
         "correct": 1,
         "expl": "Sujato's English 'you' represents an impersonal or third-person Pali construction."},
        {"q": "Where does this poem fall in the Theragātha?",
         "opts": [
             "The opening poem of Chapter Ten",
             "The first poem of Chapter Eleven",
             "A poem in the Book of the Twos",
             "The tenth and final poem of Chapter Ten"],
         "correct": 3,
         "expl": "Closing this chapter's set of ten."},
    ],
    marginalia=[
        ("Two Devasabhas, opposite voices", [
            "one lists what he crossed —",
            "one is only described"
        ]),
        ("You, or one who", [
            "a third time this chapter —",
            "the Pali says 'he'"
        ]),
        ("Two flowers, one chapter", [
            "a single bloom, offered —",
            "now, a garland worn"
        ]),
        ("Two more names, quietly enlarged", [
            "a sage added; great wisdom added —",
            "the uddāna's own touches"
        ]),
    ],
    further=[
        '<a href="%s/thag1.100/en/sujato" target="_blank" rel="noopener">'
        "Full Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment." % SC,
        '<a href="thag-1.89.html">Thag 1.89 &mdash; Devasabha (1st)</a> '
        "&mdash; the first half of this disambiguated pair, from "
        "Chapter Nine.",
        '<a href="thag-1.96.html">Thag 1.96 &mdash; Kha&#7751;&#7693;asumana</a> '
        "&mdash; an earlier poem in this chapter with its own, "
        "literal flower.",
        '<a href="thag-1.99.html">Thag 1.99 &mdash; Uttiya (3rd)</a> '
        "&mdash; the poem immediately before this one, in the same "
        "chapter.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)
