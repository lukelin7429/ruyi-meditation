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
        "the poem immediately before this one, closing Chapter Two.",
        '<a href="./">Theragatha</a> &mdash; back to the collection '
        "index.",
    ],
)
