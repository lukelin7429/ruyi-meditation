# -*- coding: utf-8 -*-
"""Sagāthāvagga — The Book with Verses (SN 1–11). One discourse per page."""

SC = "https://suttacentral.net"

INDEX_HEADING = "I. Sagāthāvagga — The Book with Verses"
# SN 1.1, SN 3.25, and SN 6.1 were published before this series began working
# in order, in the earlier twenty-page selection; they are listed in the
# index by INDEX_EXTRA and are not generated here. Systematic coverage of
# this book starts at SN 1.2, the first discourse not already published.
# HEAD is "./" (this is the first module of the whole Saṃyutta Nikāya). TAIL
# points at the nearest already-published page beyond this book -- SN 12.1,
# from the same earlier selection -- until a sn_content_02 module exists for
# the Nidānavagga and TAIL can move to its own first page.
HEAD = ("./", "Saṃyutta Nikāya selections")
TAIL = ("sn-12.1.html", "SN 12.1 &middot; Dependent Origination")
INDEX_EXTRA = [
    ("sn-1.1", "Oghataraṇa", "Crossing the Flood"),
    ("sn-3.25", "Pabbatūpama", "The Simile of the Mountain"),
    ("sn-6.1", "Āyācana", "The Appeal of the Divinity"),
]

PAGES = []


def page(samyutta, num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Sagāthāvagga.

    Unlike the Aṅguttara content modules, one Saṃyutta Nikāya book spans
    several independently numbered saṃyuttas (SN 1.1..., SN 2.1..., SN
    3.1..., not one flat number space), so both the saṃyutta and the
    discourse number are required.
    """
    d = {
        "slug": "sn-%d.%d" % (samyutta, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "sn%d/sn%d.%d" % (samyutta, samyutta, num),
        "crumb": "SN %d.%d" % (samyutta, num),
        "number_line": "Saṃyutta Nikāya &middot; Discourse %d.%d" % (samyutta, num),
        "title": title,
        "subtitle": "<em>%ssutta</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# SN 1.2 — Nimokkhasutta
# --------------------------------------------------------------------------- #
page(
    1, 2, "Nimokkha", "Liberation",
    meta_title="SN 1.2 — Liberation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nimokkhasutta — a "
        "deity's question about liberation, answered in a compact three-line verse naming "
        "the end of relish for rebirth, the finishing of perception and consciousness, and "
        "the stilling of feeling. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove, late at night; the same "
                    "circumstances as SN 1.1"),
        ("Speakers", "The Buddha and an unnamed, radiant deity"),
        ("Form", "A three-part riddle-and-answer exchange in prose, closed with a compact "
                 "verse naming three causes"),
        ("Length", "~1.5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the Chinese Saṃyukta-āgama "
                              "(T99), though this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, but the closing "
                       "verse compresses three separate technical claims into three lines"),
    ],
    why=(
        "A deity asks the Buddha, twice over, whether he knows the liberation, emancipation, "
        "and seclusion of sentient beings &mdash; first whether he knows it at all, then how "
        "he knows it. The answer, given in verse, names three specific causes: the ending of "
        "relish for rebirth, the finishing of perception and consciousness, and the cessation "
        "and stilling of feelings. Three of the five aggregates &mdash; perception, "
        "consciousness, and feeling &mdash; already appear here, in the second discourse of "
        "the entire collection, well before any discourse devoted to the aggregates as a "
        "topic in their own right."),
    guide=[
        ("A question asked twice, then answered once", [
            "The deity's exchange follows a three-step pattern already used at SN 1.1: a "
            "first question asking simply whether the Buddha knows a thing, a second "
            "confirming that he does, and a third asking how &mdash; which the Buddha answers "
            "directly, in verse, without further prompting."]),
        ("Three technical terms, closely related", [
            "<em>Nimokkha</em>, <em>pamokkha</em>, and <em>viveka</em> &mdash; liberation, "
            "emancipation, and seclusion &mdash; are named together as a set, without being "
            "distinguished from one another in this discourse. The verse answer addresses "
            "all three at once, as a single achievement rather than three separate ones."]),
        ("Three causes, three aggregates", [
            "The verse names three specific causes: the ending of relish for continued "
            "existence (<em>nandībhavaparikkhaya</em>), the finishing of perception and "
            "consciousness (<em>saññāviññāṇasaṅkhaya</em>), and the cessation and stilling of "
            "feelings (<em>vedanānaṁ nirodhā upasamā</em>). Perception, consciousness, and "
            "feeling are three of the five aggregates (<em>khandha</em>) that later become "
            "this collection's own dedicated subject in its third book, the Khandhavagga."]),
        ("A verse, not further prose explanation", [
            "Unlike a discourse that might unpack each of these three causes in prose, this "
            "one simply states them, compressed into four lines of verse, and ends. Nothing "
            "in the text explains what &lsquo;finishing perception and consciousness&rsquo; "
            "or &lsquo;stilling feelings&rsquo; concretely involves; the deity asks no further "
            "question, and none is offered unprompted."]),
        ("A shape this book's opening chapter repeats", [
            "This same short question-and-answer shape, closed by a compact verse, recurs "
            "across the Naḷavagga, the first sub-chapter of the Devatāsaṃyutta this discourse "
            "belongs to &mdash; the same &lsquo;deity approaches, asks, is answered&rsquo; "
            "frame already met at SN 1.1, now applied to a different subject."]),
    ],
    terms=[
        ("nimokkha, pamokkha, viveka",
         "liberation, emancipation, and seclusion &mdash; three closely related terms named "
         "together as a single achievement in this discourse's question."),
        ("nandībhavaparikkhaya",
         "&ldquo;the ending of relish for rebirth&rdquo; &mdash; the first of the verse's "
         "three named causes."),
        ("saññāviññāṇasaṅkhaya",
         "&ldquo;the finishing of perception and consciousness&rdquo; &mdash; the second "
         "cause, naming two of the five aggregates directly."),
        ("vedanānaṁ nirodhā upasamā",
         "&ldquo;the cessation and stilling of feelings&rdquo; &mdash; the third cause, "
         "naming a third aggregate."),
        ("khandha",
         "&ldquo;aggregate&rdquo; &mdash; perception, consciousness, and feeling, three of "
         "the five aggregates, appear here well before this collection's own dedicated book "
         "on the subject."),
    ],
    text_intro=(
        "The discourse in full: a deity's question, asked twice, answered once in verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.2:1.1-1.2"),
        ("p", "&sect;2", "sn1.2:2.1-2.1"),
        ("p", "&sect;3", "sn1.2:3.1-3.1"),
        ("p", "&sect;4", "sn1.2:4.1-4.1"),
        ("p", "&sect;5", "sn1.2:5.1-5.5"),
    ],
    quiz=[
        {"q": "What three things does the deity ask the Buddha about?",
         "opts": [
             "Liberation, emancipation, and seclusion of sentient beings",
             "The five aggregates",
             "The four noble truths",
             "The eightfold path"],
         "correct": 0,
         "expl": "Nimokkha, pamokkha, viveka &mdash; named together as a single question."},
        {"q": "What pattern does this exchange follow, already used at SN 1.1?",
         "opts": [
             "A question asking whether the Buddha knows a thing, confirmation that he does, then a question asking how",
             "A long philosophical debate spanning many exchanges",
             "A silent gesture with no words exchanged",
             "A question the Buddha refuses to answer"],
         "correct": 0,
         "expl": "The same three-step shape recurs across this sub-chapter."},
        {"q": "What three causes does the closing verse name?",
         "opts": [
             "Ending relish for rebirth, finishing perception and consciousness, and stilling feelings",
             "The five precepts",
             "The four right efforts",
             "Faith, energy, mindfulness, immersion, and wisdom"],
         "correct": 0,
         "expl": "Three separate technical claims compressed into four lines of verse."},
        {"q": "How many of the five aggregates (khandha) does this verse name directly?",
         "opts": [
             "Three: perception, consciousness, and feeling",
             "All five",
             "None; the aggregates are not mentioned at all",
             "Only one"],
         "correct": 0,
         "expl": "Well before this collection's own dedicated book on the aggregates."},
        {"q": "Does this discourse explain in prose what 'finishing perception and consciousness' concretely involves?",
         "opts": [
             "No &mdash; the verse simply states the three causes and the discourse ends",
             "Yes, in extensive detail across several paragraphs",
             "Yes, but only in a footnote",
             "The discourse asks a follow-up question to clarify this itself"],
         "correct": 0,
         "expl": "No further question is asked, and none is offered unprompted."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove, late at night &mdash; the same circumstances as SN 1.1",
             "On a mountaintop at dawn",
             "In a different city entirely from SN 1.1",
             "No setting is given"],
         "correct": 0,
         "expl": "Identical circumstances to the discourse immediately preceding it."},
        {"q": "Who are the two speakers in this discourse?",
         "opts": [
             "The Buddha and an unnamed, radiant deity",
             "Two named mendicants",
             "The Buddha and a king",
             "A deity speaking alone, with no reply from the Buddha"],
         "correct": 0,
         "expl": "The deity asks; the Buddha answers, twice."},
        {"q": "What sub-chapter of the Devatāsaṃyutta does this discourse belong to?",
         "opts": [
             "The Naḷavagga",
             "The Nidānavagga",
             "The Khandhavagga",
             "This discourse belongs to no sub-chapter"],
         "correct": 0,
         "expl": "Named directly in the Pali source's own heading."},
        {"q": "What does 'khandha' mean?",
         "opts": [
             "'Aggregate' &mdash; the topic this collection later devotes an entire book to",
             "'Liberation'",
             "'A deity'",
             "'Verse'"],
         "correct": 0,
         "expl": "Three of the five aggregates appear by name in this discourse's closing verse."},
        {"q": "What form does the Buddha's final answer take?",
         "opts": [
             "A compact four-line verse",
             "A long prose explanation",
             "A single-word answer",
             "A refusal to answer"],
         "correct": 0,
         "expl": "Compressing three separate causes into four lines."},
    ],
    marginalia=[
        ("Three terms, one question", [
            "nimokkha, pamokkha,",
            "viveka &mdash; asked as one",
        ]),
        ("Three causes, in verse", [
            "ending relish for rebirth,",
            "finishing perception &amp; consciousness,",
        ]),
        ("Aggregates, early", [
            "perception, consciousness, feeling",
            "&mdash; three of the five khandha",
        ]),
        ("A pattern repeating", [
            "the same question-shape",
            "as SN 1.1, this sub-chapter",
        ]),
    ],
    further=[
        '<a href="%s/sn1.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; the previous '
        "discourse in this collection, and this same question-and-answer shape&rsquo;s first "
        "appearance.",
        '<a href="sn-22.1.html">SN 22.1 &middot; Nakula&rsquo;s Father</a> &mdash; this '
        "collection&rsquo;s own book devoted to the five aggregates this verse names three "
        "of.",
        '<a href="sn-3.25.html">SN 3.25 &middot; The Simile of the Mountain</a> &mdash; the '
        "next discourse in this book&rsquo;s currently published selection.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.3 — Upanīyasutta
# --------------------------------------------------------------------------- #
page(
    1, 3, "Upanīya", "Led On",
    meta_title="SN 1.3 — Led On | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Upanīyasutta — a "
        "deity's verse on how short life is led onward toward old age with no shelter, and "
        "the Buddha's reply naming what that peril calls for. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as SN 1.1 and SN 1.2"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse spoken by the deity, answered by a four-line verse from "
                 "the Buddha that shares its first two lines"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a short, direct verse "
                       "with one compressed image, &lsquo;the world&rsquo;s bait&rsquo;"),
        ("A pattern to watch", "The next discourse, SN 1.4, reuses this verse&rsquo;s exact "
                               "second half &mdash; only the opening image changes"),
    ],
    why=(
        "A deity states the plain fact of impermanence &mdash; life is short and is "
        "constantly &lsquo;led onward&rsquo; (<em>upanīyati</em>) toward old age, which "
        "offers no shelter from what is coming &mdash; and draws from it a conventional "
        "conclusion: seeing this peril in death, do good deeds that bring joy. The Buddha "
        "repeats the deity's diagnosis word for word, but changes the prescription. Where "
        "the deity counsels accumulating merit, the Buddha counsels renunciation: a seeker "
        "of peace would drop the world's bait entirely. Same premise, two different answers "
        "&mdash; the discourse's whole point sits in that substitution."),
    guide=[
        ("The same peril, seen twice", [
            "Both verses open by naming exactly the same danger in exactly the same words: "
            "&lsquo;this life, so very short, is led onward; one led on to old age has no "
            "shelter. Seeing this peril in death&hellip;&rsquo; The deity and the Buddha do "
            "not disagree about the diagnosis at all &mdash; only about what follows from it."]),
        ("Merit versus renunciation", [
            "The deity's own conclusion is conventional and virtuous as far as it goes: "
            "&lsquo;do good deeds that bring you joy&rsquo; &mdash; make merit while there is "
            "still time. The Buddha's closing line replaces this with something more "
            "radical: &lsquo;a seeker of peace would drop the world&rsquo;s bait "
            "(<em>lokāmisa</em>).&rsquo; Not merely do good, but let go of what the world "
            "offers as bait in the first place."]),
        ("Lokāmisa, the world's bait", [
            "<em>Lokāmisa</em> literally combines <em>loka</em> (&lsquo;world&rsquo;) with "
            "<em>āmisa</em> (&lsquo;flesh, meat, bait&rsquo;) &mdash; the image is of "
            "sensory and worldly pleasures as bait set out to hook a creature, the way meat "
            "baits a trap. Dropping the bait, not merely avoiding the trap's mechanism, is "
            "the discourse's image for renunciation."]),
        ("A verse this vagga will repeat", [
            "The very next discourse in this collection, SN 1.4, restates this verse's "
            "second half &mdash; &lsquo;seeing this peril in death, do good deeds that bring "
            "you joy&rsquo; and the Buddha's &lsquo;a seeker of peace would drop the world's "
            "bait&rsquo; &mdash; word for word, changing only the opening two lines' image of "
            "impermanence. This vagga returns to the same closing thought more than once, "
            "trying different openings on it."]),
    ],
    terms=[
        ("upanīyati",
         "&ldquo;is led onward&rdquo; &mdash; the verb this discourse's title comes from, "
         "describing life as something continuously carried toward its end, not a state "
         "that simply persists."),
        ("jarūpanītassa",
         "&ldquo;for one led on to old age&rdquo; &mdash; the specific destination this "
         "onward motion has, with no shelter (<em>na santi tāṇā</em>) once arrived."),
        ("lokāmisa",
         "&ldquo;the world's bait&rdquo; &mdash; worldly and sensory pleasure imaged as bait "
         "set to hook a creature, from <em>loka</em> (&ldquo;world&rdquo;) + <em>āmisa</em> "
         "(&ldquo;flesh, bait&rdquo;)."),
        ("santipekkho",
         "&ldquo;one who seeks peace&rdquo; &mdash; the discourse's description of the "
         "person who drops the world's bait, from <em>santi</em> (&ldquo;peace&rdquo;) + "
         "<em>pekkha</em> (&ldquo;looking toward, seeking&rdquo;)."),
        ("puññāni",
         "&ldquo;good deeds, merit&rdquo; &mdash; the deity's own prescription, named in the "
         "verse's first half before the Buddha's answer replaces it."),
    ],
    text_intro=(
        "The discourse in full: a deity's verse on impermanence, and the Buddha's answer, "
        "sharing its diagnosis but not its prescription. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.3:1.1-1.2"),
        ("p", "&sect;2", "sn1.3:2.1-2.4"),
        ("p", "&sect;3", "sn1.3:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does the deity say about life in the opening verse?",
         "opts": [
             "It is very short and is constantly led onward toward old age, which offers no shelter",
             "It is long and full of opportunity",
             "It ends only through misfortune, not naturally",
             "It cannot be described in words"],
         "correct": 0,
         "expl": "&lsquo;Upanīyati jīvitam appamāyu&rsquo; &mdash; life, so very short, is led onward."},
        {"q": "What conclusion does the deity draw from this peril?",
         "opts": [
             "Do good deeds that bring you joy",
             "Nothing can be done, so there is no point acting",
             "One should seek out more pleasure while there is time",
             "One should argue with death directly"],
         "correct": 0,
         "expl": "The deity's own prescription is conventional merit-making."},
        {"q": "How does the Buddha's verse differ from the deity's?",
         "opts": [
             "It repeats the same diagnosis of impermanence but replaces the prescription with dropping the world's bait",
             "It denies that life is short at all",
             "It rejects the deity's question outright",
             "It is identical in every line to the deity's verse"],
         "correct": 0,
         "expl": "Same first half, a different closing line: renunciation, not merit alone."},
        {"q": "What does 'lokāmisa' mean, and what image does it carry?",
         "opts": [
             "'The world's bait' &mdash; worldly pleasure imaged as bait set to hook a creature",
             "'The world's wisdom'",
             "'The world's suffering'",
             "'The world's teacher'"],
         "correct": 0,
         "expl": "From loka ('world') + āmisa ('flesh, bait')."},
        {"q": "What does 'jarūpanītassa' name?",
         "opts": [
             "Being led on to old age, which offers no shelter",
             "A type of meditation",
             "A deity's name",
             "A monastery near Sāvatthī"],
         "correct": 0,
         "expl": "The destination life's onward motion has, with no shelter once arrived."},
        {"q": "What happens in the very next discourse, SN 1.4, in relation to this one?",
         "opts": [
             "It reuses this verse's exact second half, changing only the opening image",
             "It directly contradicts this discourse",
             "It has no relation to this discourse at all",
             "It repeats this discourse word for word with no changes"],
         "correct": 0,
         "expl": "Same closing couplet, both deity's and Buddha's, with a new opening image."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as SN 1.1 and SN 1.2",
             "On a mountaintop",
             "In a different city from the previous two discourses",
             "No setting is given"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame."},
        {"q": "Who speaks the first verse?",
         "opts": [
             "An unnamed deity",
             "The Buddha",
             "A group of monks",
             "A king"],
         "correct": 0,
         "expl": "The deity states the diagnosis; the Buddha answers."},
        {"q": "What does 'santipekkho' describe?",
         "opts": [
             "One who seeks peace &mdash; the person who drops the world's bait",
             "A type of demon",
             "A meditation posture",
             "A season of the year"],
         "correct": 0,
         "expl": "Santi ('peace') + pekkha ('looking toward, seeking')."},
        {"q": "Do the two verses in this discourse disagree about the diagnosis of impermanence?",
         "opts": [
             "No &mdash; they state it in identical words; only the prescription differs",
             "Yes, they give completely opposite accounts of impermanence",
             "The Buddha denies impermanence exists",
             "The deity denies impermanence exists"],
         "correct": 0,
         "expl": "The disagreement is entirely about what follows from the same premise."},
    ],
    marginalia=[
        ("Same diagnosis, twice", [
            "life led onward,",
            "old age with no shelter",
        ]),
        ("Two prescriptions", [
            "merit-making, or",
            "dropping the world&rsquo;s bait",
        ]),
        ("Lokāmisa", [
            "the world&rsquo;s bait &mdash;",
            "loka + āmisa, flesh",
        ]),
        ("A refrain returning", [
            "SN 1.4 reuses",
            "this verse&rsquo;s closing half",
        ]),
    ],
    further=[
        '<a href="%s/sn1.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.2.html">SN 1.2 &middot; Liberation</a> &mdash; the previous discourse '
        "in this collection.",
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this vagga&rsquo;s '
        "opening discourse, and the same recurring frame.",
        "SN 1.4 &middot; Time Flies &mdash; the next discourse, reusing this verse&rsquo;s "
        "closing couplet with a new opening image.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.4 — Accentisutta
# --------------------------------------------------------------------------- #
page(
    1, 4, "Accenti", "Time Flies",
    meta_title="SN 1.4 — Time Flies | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Accentisutta — a "
        "deity's verse on time passing and the stages of life falling away one by one, "
        "closed with the same reply the Buddha gave at SN 1.3. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as the discourses before it"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse from the deity, answered by the Buddha's four-line "
                 "verse &mdash; both sharing their closing two lines with SN 1.3"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest kind of "
                       "reading here, since half the verse repeats a discourse just read"),
        ("Companion discourse", "SN 1.3, immediately before this one, closes with the exact "
                                "same two-line refrain in both the deity's and the Buddha's "
                                "verse"),
    ],
    why=(
        "This discourse is best read directly alongside SN 1.3, the one immediately before "
        "it. Its opening image changes &mdash; time flying, nights passing, the stages of "
        "life leaving one by one &mdash; but its closing two lines, in both the deity's "
        "verse and the Buddha's, are identical, word for word, to SN 1.3's. The vagga is "
        "showing the same conclusion is reachable from more than one starting image of "
        "impermanence."),
    guide=[
        ("A new opening image", [
            "Where SN 1.3 pictured life as continuously &lsquo;led onward,&rsquo; this "
            "discourse pictures time itself in motion: &lsquo;time flies, nights pass by, "
            "the stages of life leave us one by one&rsquo; (<em>vayoguṇā anupubbaṁ "
            "jahanti</em>). The image has shifted from being carried to being left behind, "
            "piece by piece, as time moves past."]),
        ("The identical closing couplet", [
            "From &lsquo;seeing this peril in death&rsquo; onward, this verse and SN 1.3's "
            "match exactly: the deity again counsels &lsquo;do good deeds that bring you "
            "joy,&rsquo; and the Buddha again answers that &lsquo;a seeker of peace would "
            "drop the world's bait.&rsquo; Nothing here is a fresh answer &mdash; it is the "
            "same answer, reached from a different starting point."]),
        ("Why the vagga repeats itself", [
            "Reciting several distinct images of impermenance &mdash; being led onward, "
            "time flying, the stages of life falling away &mdash; that all resolve to the "
            "same closing counsel is itself a rhetorical shape, not a redundancy to smooth "
            "over. It is closer to variations on a theme than to a single verse told twice."]),
        ("Vayoguṇā, the stages of life", [
            "<em>Vayoguṇā</em> names the successive phases a life passes through &mdash; "
            "commentarial tradition reads this as childhood, youth, and old age &mdash; each "
            "one dropped in turn (<em>anupubbaṁ jahanti</em>, &lsquo;left behind in "
            "order&rsquo;) as time moves the person through them."]),
    ],
    terms=[
        ("accenti",
         "&ldquo;flies, passes swiftly&rdquo; &mdash; the verb this discourse's title comes "
         "from, describing time's motion rather than the person's."),
        ("vayoguṇā",
         "&ldquo;the stages of life&rdquo; &mdash; traditionally read as childhood, youth, "
         "and old age, each one left behind in turn as time passes."),
        ("anupubbaṁ jahanti",
         "&ldquo;leave us one by one, in order&rdquo; &mdash; describing how the stages of "
         "life fall away successively, not all at once."),
        ("lokāmisa",
         "&ldquo;the world's bait&rdquo; &mdash; the same image from SN 1.3, worldly "
         "pleasure as bait set to hook a creature, repeated here word for word."),
        ("santipekkho",
         "&ldquo;one who seeks peace&rdquo; &mdash; the same description, again shared "
         "verbatim with SN 1.3's closing line."),
    ],
    text_intro=(
        "The discourse in full: a new opening image of impermanence, closed with the same "
        "answer already given at SN 1.3. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.4:1.1-1.2"),
        ("p", "&sect;2", "sn1.4:2.1-2.4"),
        ("p", "&sect;3", "sn1.4:3.1-3.4"),
    ],
    quiz=[
        {"q": "What new image does this discourse's opening verse use for impermanence?",
         "opts": [
             "Time flying, nights passing, the stages of life leaving one by one",
             "Life being led onward toward old age",
             "A flood sweeping a person away",
             "A mountain wearing down over ages"],
         "correct": 0,
         "expl": "'Accenti kālā tarayanti rattiyo' &mdash; a new opening, distinct from SN 1.3's."},
        {"q": "How does this discourse's closing couplet compare to SN 1.3's?",
         "opts": [
             "It is word-for-word identical, in both the deity's and the Buddha's verse",
             "It is completely different",
             "Only the deity's closing line matches; the Buddha's differs",
             "Only the Buddha's closing line matches; the deity's differs"],
         "correct": 0,
         "expl": "Both verses' closing two lines match SN 1.3's exactly."},
        {"q": "What does 'vayoguṇā' name?",
         "opts": [
             "The stages of life, traditionally read as childhood, youth, and old age",
             "A type of deity",
             "The five aggregates",
             "A meditation technique"],
         "correct": 0,
         "expl": "Left behind in order as time passes, per commentarial reading."},
        {"q": "What does 'anupubbaṁ jahanti' describe?",
         "opts": [
             "The stages of life falling away one by one, in order",
             "All stages of life ending simultaneously",
             "A deity vanishing after speaking",
             "The Buddha teaching in stages"],
         "correct": 0,
         "expl": "Successive, not simultaneous, loss."},
        {"q": "What is the Buddha's closing line in this discourse?",
         "opts": [
             "A seeker of peace would drop the world's bait",
             "One should never make merit",
             "Time cannot truly be understood",
             "There is no answer to impermanence"],
         "correct": 0,
         "expl": "Identical to the closing line already given at SN 1.3."},
        {"q": "What does reading SN 1.3 and SN 1.4 together suggest about this vagga's approach?",
         "opts": [
             "It offers several distinct images of impermanence that resolve to the same counsel",
             "It contradicts itself between discourses",
             "Each discourse in the vagga is entirely unrelated to the others",
             "Later discourses always overrule earlier ones"],
         "correct": 0,
         "expl": "Variations on a theme, not redundant repetition."},
        {"q": "What does 'accenti' mean?",
         "opts": [
             "'Flies, passes swiftly' &mdash; describing time's own motion",
             "'Is led onward'",
             "'Is completely still'",
             "'Returns again'"],
         "correct": 0,
         "expl": "The verb this discourse's title is drawn from."},
        {"q": "Does this discourse's prescription differ from the deity's own conclusion?",
         "opts": [
             "Yes &mdash; the deity counsels merit-making, the Buddha counsels dropping the world's bait",
             "No, they give identical prescriptions",
             "The deity gives no prescription at all",
             "The Buddha refuses to answer"],
         "correct": 0,
         "expl": "Same structure as SN 1.3: shared diagnosis, different prescription."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as before",
             "A different monastery entirely",
             "No setting is given",
             "A forest far from any city"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame continues."},
        {"q": "What does 'lokāmisa' mean, repeated here from SN 1.3?",
         "opts": [
             "'The world's bait' &mdash; worldly pleasure imaged as bait for a creature",
             "'The world's peace'",
             "'The world's teacher'",
             "'The world's ending'"],
         "correct": 0,
         "expl": "Loka ('world') + āmisa ('flesh, bait'), unchanged from SN 1.3."},
    ],
    marginalia=[
        ("A new opening", [
            "time flies, nights pass,",
            "life&rsquo;s stages fall away",
        ]),
        ("The same closing", [
            "word for word",
            "matching SN 1.3",
        ]),
        ("Vayoguṇā", [
            "the stages of life &mdash;",
            "left behind in order",
        ]),
        ("Variations on a theme", [
            "different openings,",
            "one recurring counsel",
        ]),
    ],
    further=[
        '<a href="%s/sn1.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.3.html">SN 1.3 &middot; Led On</a> &mdash; the discourse immediately '
        "before this one, sharing this verse&rsquo;s exact closing couplet.",
        '<a href="sn-1.2.html">SN 1.2 &middot; Liberation</a> &mdash; two discourses back in '
        "this same collection.",
        "SN 1.5 &middot; Cut How Many? &mdash; the next discourse, a riddle-verse on what a "
        "mendicant crosses the flood by cutting, dropping, and developing.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.5 — Katichindasutta
# --------------------------------------------------------------------------- #
page(
    1, 5, "Katichinda", "Cut How Many?",
    meta_title="SN 1.5 — Cut How Many? | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Katichindasutta — "
        "a deity's riddle asking how many things a mendicant must cut, drop, and develop to "
        "cross the flood, and the Buddha's answer: five each. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as the discourses before it"),
        ("Speakers", "An unnamed deity, posing a riddle, and the Buddha, answering it"),
        ("Form", "A four-line riddle-verse, answered by a four-line verse repeating its "
                 "exact structure with the number supplied"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the verse itself is "
                       "short, but names four separate sets of five without specifying which"),
        ("Cross-reference", "The Buddha's answering verse is word-for-word identical to "
                            "Dhammapada verse 370 (Bhikkhuvagga)"),
    ],
    why=(
        "A deity asks a riddle built entirely from the number &lsquo;how many&rsquo; "
        "(<em>kati</em>): how many things must a mendicant cut, how many drop, how many "
        "more develop, and by slipping how many chains are they said to have crossed the "
        "flood? The Buddha's answer supplies a single number to all four blanks &mdash; "
        "five &mdash; without naming what the four sets of five actually are. The riddle "
        "form itself is the point: this discourse rewards recognizing the shape of a "
        "teaching before knowing its full content."),
    guide=[
        ("A riddle built on one word", [
            "Every line of the deity's verse repeats the interrogative <em>kati</em> "
            "(&lsquo;how many&rsquo;): how many to cut, how many to drop, how many more to "
            "develop, how many chains slipped. The Buddha's reply answers in exactly the "
            "same four-part structure, simply replacing each <em>kati</em> with "
            "<em>pañca</em> (&lsquo;five&rsquo;)."]),
        ("Four fives, left unnamed", [
            "The verse itself never says what the &lsquo;five to cut,&rsquo; &lsquo;five to "
            "drop,&rsquo; and &lsquo;five to develop&rsquo; actually are. Commentarial "
            "tradition reads them as three distinct sets: the five lower fetters "
            "(<em>orambhāgiya saṁyojana</em>) to cut, the five higher fetters "
            "(<em>uddhambhāgiya saṁyojana</em>) to drop, and the five spiritual faculties "
            "(<em>indriya</em> &mdash; faith, energy, mindfulness, immersion, and wisdom) "
            "to develop further. This reading is not spelled out in the verse itself."]),
        ("Crossing the flood, again", [
            "The riddle's closing question &mdash; &lsquo;when a mendicant slips how many "
            "chains are they said to have crossed the flood&rsquo; &mdash; returns to the "
            "exact image that opened this whole collection at SN 1.1, where the Buddha "
            "described crossing the flood &lsquo;neither standing nor swimming.&rsquo; This "
            "discourse gives that same crossing a specific number attached to it."]),
        ("A verse shared with the Dhammapada", [
            "The Buddha's answering verse here &mdash; &lsquo;pañca chinde pañca jahe, "
            "pañca cuttari bhāvaye&hellip;&rsquo; &mdash; is word-for-word identical to "
            "Dhammapada verse 370, in its Bhikkhuvagga (&lsquo;Chapter on Mendicants&rsquo;). "
            "The same four-part formula appears as free-standing teaching in one collection "
            "and as a deity's riddle-answer in another."]),
    ],
    terms=[
        ("kati",
         "&ldquo;how many?&rdquo; &mdash; the interrogative repeated in every line of the "
         "deity's riddle, this discourse's title Katichinda meaning roughly &ldquo;how many "
         "to cut.&rdquo;"),
        ("orambhāgiya saṁyojana",
         "the five &ldquo;lower fetters&rdquo; &mdash; commentarial tradition's reading of "
         "what is to be &ldquo;cut&rdquo; in this verse, though the verse itself does not "
         "name them."),
        ("uddhambhāgiya saṁyojana",
         "the five &ldquo;higher fetters&rdquo; &mdash; the commentarial reading of what is "
         "to be &ldquo;dropped,&rdquo; distinct from the lower fetters cut first."),
        ("indriya",
         "the five spiritual &ldquo;faculties&rdquo; &mdash; faith, energy, mindfulness, "
         "immersion, and wisdom &mdash; the commentarial reading of what is to be "
         "&ldquo;developed further.&rdquo;"),
        ("saṅgātigo",
         "&ldquo;one who has slipped past the ties&rdquo; &mdash; the condition the riddle "
         "asks about, describing the mendicant who has crossed the flood."),
    ],
    text_intro=(
        "The discourse in full: a riddle built on 'how many,' answered with a single number "
        "repeated four times. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.5:1.1-1.2"),
        ("p", "&sect;2", "sn1.5:2.1-2.4"),
        ("p", "&sect;3", "sn1.5:3.1-3.4"),
    ],
    quiz=[
        {"q": "What word does the deity's riddle repeat in every line?",
         "opts": [
             "Kati, 'how many?'",
             "Pañca, 'five'",
             "Ogha, 'flood'",
             "Bhikkhu, 'mendicant'"],
         "correct": 0,
         "expl": "The riddle is built entirely around this one interrogative."},
        {"q": "What single number does the Buddha's answer supply to every blank?",
         "opts": [
             "Five",
             "Four",
             "Eight",
             "A different number for each blank"],
         "correct": 0,
         "expl": "Pañca, 'five,' answers all four parts of the riddle."},
        {"q": "Does the verse itself name what the four sets of five actually are?",
         "opts": [
             "No &mdash; the verse gives only the number, not the content",
             "Yes, it lists all twenty items by name",
             "It names only the first set",
             "It names only the last set"],
         "correct": 0,
         "expl": "The specific identification comes from commentarial tradition, not the verse."},
        {"q": "According to commentarial tradition, what is to be 'cut'?",
         "opts": [
             "The five lower fetters",
             "The five higher fetters",
             "The five faculties",
             "The five aggregates"],
         "correct": 0,
         "expl": "Orambhāgiya saṁyojana, per the traditional reading."},
        {"q": "According to commentarial tradition, what is to be 'developed further'?",
         "opts": [
             "The five spiritual faculties: faith, energy, mindfulness, immersion, wisdom",
             "The five lower fetters",
             "The five higher fetters",
             "The five hindrances"],
         "correct": 0,
         "expl": "Indriya, the five faculties, per the traditional reading."},
        {"q": "What image does the riddle's closing question return to?",
         "opts": [
             "Crossing the flood, the same image that opened this collection at SN 1.1",
             "The world's bait, from SN 1.3 and 1.4",
             "A green reed being mowed down",
             "A deity vanishing after speaking"],
         "correct": 0,
         "expl": "The same crossing described at SN 1.1, now given a specific number."},
        {"q": "What well-known verse collection shares this discourse's answering verse word for word?",
         "opts": [
             "The Dhammapada (verse 370, Bhikkhuvagga)",
             "The Theragāthā",
             "The Jātaka tales",
             "The Vinaya Piṭaka"],
         "correct": 0,
         "expl": "An identical four-line formula appears in both collections."},
        {"q": "What does 'saṅgātigo' describe?",
         "opts": [
             "One who has slipped past the ties, having crossed the flood",
             "A type of deity",
             "A riddle format",
             "A monastery near Sāvatthī"],
         "correct": 0,
         "expl": "The condition the riddle's closing question asks about."},
        {"q": "What is the form of the Buddha's answering verse?",
         "opts": [
             "It repeats the deity's exact four-part structure, replacing each 'how many' with 'five'",
             "It is written entirely in prose",
             "It rejects the riddle's premise",
             "It asks a counter-question instead of answering"],
         "correct": 0,
         "expl": "The same shape, filled in with a single number."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as before",
             "A different city, unconnected to earlier discourses",
             "No setting is given",
             "A mountain peak"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame continues."},
    ],
    marginalia=[
        ("A riddle on one word", [
            "kati, kati, kati &mdash;",
            "how many, asked four times",
        ]),
        ("One number, four blanks", [
            "pañca chinde, pañca jahe,",
            "pañca cuttari bhāvaye",
        ]),
        ("Fetters and faculties", [
            "commentary reads: lower fetters,",
            "higher fetters, five faculties",
        ]),
        ("Shared with the Dhammapada", [
            "the same four lines,",
            "verse 370, Bhikkhuvagga",
        ]),
    ],
    further=[
        '<a href="%s/sn1.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this collection&rsquo;s '
        "opening image of crossing the flood, given a number here.",
        '<a href="sn-1.4.html">SN 1.4 &middot; Time Flies</a> &mdash; the discourse '
        "immediately before this one.",
        "SN 1.6 &middot; Awake &mdash; the next discourse, another riddle-verse answered "
        "with the number five.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.6 — Jāgarasutta
# --------------------------------------------------------------------------- #
page(
    1, 6, "Jāgara", "Awake",
    meta_title="SN 1.6 — Awake | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Jāgarasutta — a "
        "deity's riddle on who sleeps among the waking, who wakes among the sleeping, and "
        "by how many things one gathers dust or is cleansed. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as the discourses before it"),
        ("Speakers", "An unnamed deity, posing a paradox, and the Buddha, resolving it with "
                    "a single repeated number"),
        ("Form", "A four-line riddle-verse built on paradox, answered by a four-line verse "
                 "supplying the same number to each part"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the paradox (sleeping "
                       "among the waking) is easy to read past without noticing it is a "
                       "riddle at all"),
        ("Companion discourse", "SN 1.5, immediately before this one, is the same riddle "
                                "shape answered with the same number, five"),
    ],
    why=(
        "This riddle plays on a paradox: how can someone &lsquo;sleep&rsquo; while outwardly "
        "&lsquo;awake,&rsquo; or &lsquo;wake&rsquo; while outwardly asleep? The deity asks "
        "how many things account for this, and by how many things a person gathers dust or "
        "is cleansed. As with SN 1.5 immediately before it, the Buddha's answer supplies a "
        "single number &mdash; five &mdash; to every part of the riddle, again without "
        "spelling out what the four sets of five are."),
    guide=[
        ("A paradox stated as a riddle", [
            "The deity's opening two lines invert the ordinary meaning of waking and "
            "sleeping: some people &lsquo;sleep among the waking&rsquo; &mdash; they are "
            "physically alert but spiritually unroused &mdash; while others &lsquo;wake "
            "among the sleeping,&rsquo; spiritually alert even in circumstances that dull "
            "most people. The riddle asks how many of each kind there are."]),
        ("The same shape as SN 1.5, the same number", [
            "Like the discourse immediately before it, this one is a four-part riddle "
            "answered with a single repeated number: five sleep among the waking, five "
            "wake among the sleeping, by five one gathers dust, by five one is cleansed. "
            "Commentarial tradition again supplies content the verse itself withholds "
            "&mdash; commonly the five hindrances (<em>nīvaraṇa</em>) as what dulls a "
            "person into figurative sleep, and the five faculties (<em>indriya</em>) as "
            "what wakes and cleanses them."]),
        ("Dust and cleansing", [
            "The closing two lines shift the image again, from waking and sleeping to "
            "gathering dust (<em>rajaṁ ādeti</em>) and being cleansed "
            "(<em>parisujjhati</em>). Read alongside the hindrances/faculties gloss, dust "
            "is what obscures and faculties are what clear it &mdash; the same five-versus-"
            "five structure carried through a third pair of images within one verse."]),
        ("Two riddles, back to back", [
            "SN 1.5 and SN 1.6 form a matched pair: both riddle-verses, both answered with "
            "the number five repeated four times, both left unglossed in the verse itself. "
            "Placed next to each other in this vagga, they read as two variations on the "
            "same rhetorical device rather than as unrelated discourses."]),
    ],
    terms=[
        ("suttā jāgarataṁ",
         "&ldquo;asleep among the waking&rdquo; &mdash; the discourse's opening paradox, "
         "describing spiritual dullness beneath outward alertness."),
        ("jāgarā suttesu",
         "&ldquo;awake among the sleeping&rdquo; &mdash; the paradox's mirror image, "
         "spiritual alertness beneath outward dullness."),
        ("rajaṁ ādeti",
         "&ldquo;gathers dust&rdquo; &mdash; the image for whatever obscures or "
         "contaminates, paired in this verse with being cleansed."),
        ("parisujjhati",
         "&ldquo;is cleansed, purified&rdquo; &mdash; the counterpart to gathering dust, "
         "completing the verse's third pair of images."),
        ("nīvaraṇa",
         "the five &ldquo;hindrances&rdquo; &mdash; commentarial tradition's common reading "
         "of what causes figurative sleep and gathered dust in this verse, though unnamed "
         "in the verse itself."),
    ],
    text_intro=(
        "The discourse in full: a paradox stated as a riddle, resolved with the same number "
        "used at SN 1.5. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.6:1.1-1.2"),
        ("p", "&sect;2", "sn1.6:2.1-2.4"),
        ("p", "&sect;3", "sn1.6:3.1-3.4"),
    ],
    quiz=[
        {"q": "What paradox does the deity's riddle open with?",
         "opts": [
             "Some sleep while outwardly awake, and some wake while outwardly asleep",
             "Some deities are visible and some are invisible",
             "Time both moves and stands still",
             "The flood can be crossed by both standing and swimming"],
         "correct": 0,
         "expl": "Suttā jāgarataṁ / jāgarā suttesu &mdash; the verse's opening inversion."},
        {"q": "What number does the Buddha's answer supply to every part of the riddle?",
         "opts": [
             "Five",
             "Four",
             "Seven",
             "A different number for each part"],
         "correct": 0,
         "expl": "The same number used at SN 1.5, the discourse immediately before this."},
        {"q": "What two images does the verse's closing half use?",
         "opts": [
             "Gathering dust and being cleansed",
             "Crossing a flood and reaching a shore",
             "A reed being mowed down and growing back",
             "A deity arriving and departing"],
         "correct": 0,
         "expl": "Rajaṁ ādeti and parisujjhati, a third pair of paired images in one verse."},
        {"q": "Does the verse itself name what the four sets of five actually are?",
         "opts": [
             "No &mdash; as with SN 1.5, only the number is given, not the content",
             "Yes, it lists all items explicitly",
             "It names only the hindrances, not the faculties",
             "It names only the faculties, not the hindrances"],
         "correct": 0,
         "expl": "Commentarial tradition supplies the gloss the verse withholds."},
        {"q": "What does commentarial tradition commonly read as the cause of figurative sleep here?",
         "opts": [
             "The five hindrances (nīvaraṇa)",
             "The five aggregates",
             "The four noble truths",
             "The eightfold path"],
         "correct": 0,
         "expl": "A common, though not text-stated, gloss."},
        {"q": "How does this discourse relate to SN 1.5, immediately before it?",
         "opts": [
             "Both are riddle-verses answered with the number five, forming a matched pair",
             "They directly contradict one another",
             "SN 1.6 explicitly explains SN 1.5's riddle",
             "They share no similarity at all"],
         "correct": 0,
         "expl": "Two variations on the same rhetorical device, placed back to back."},
        {"q": "What does 'jāgarā suttesu' mean?",
         "opts": [
             "'Awake among the sleeping' &mdash; spiritually alert beneath outward dullness",
             "'Asleep among the waking'",
             "'Neither asleep nor awake'",
             "'A deity who never sleeps'"],
         "correct": 0,
         "expl": "The mirror image of the verse's opening paradox."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as before",
             "A different city, unrelated to earlier discourses",
             "No setting is given",
             "A riverbank"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame continues."},
        {"q": "What is the form of the Buddha's answering verse?",
         "opts": [
             "It repeats the deity's four-part structure, supplying 'five' to each part",
             "It rejects the riddle as unanswerable",
             "It is written entirely in prose",
             "It asks the deity a counter-riddle"],
         "correct": 0,
         "expl": "The same shape as SN 1.5's answer, one verse earlier."},
        {"q": "What does 'parisujjhati' mean?",
         "opts": [
             "'Is cleansed, purified'",
             "'Gathers dust'",
             "'Falls asleep'",
             "'Crosses the flood'"],
         "correct": 0,
         "expl": "The counterpart to gathering dust in the verse's closing image."},
    ],
    marginalia=[
        ("A paradox, stated plainly", [
            "asleep among the waking,",
            "awake among the sleeping",
        ]),
        ("The same number again", [
            "five, five, five, five &mdash;",
            "as at SN 1.5",
        ]),
        ("Dust and cleansing", [
            "rajaṁ ādeti,",
            "parisujjhati",
        ]),
        ("A matched pair of riddles", [
            "SN 1.5 and SN 1.6,",
            "back to back",
        ]),
    ],
    further=[
        '<a href="%s/sn1.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.5.html">SN 1.5 &middot; Cut How Many?</a> &mdash; the matched riddle '
        "immediately before this one, answered with the same number.",
        '<a href="sn-1.2.html">SN 1.2 &middot; Liberation</a> &mdash; further back in this '
        "same collection.",
        "SN 1.7 &middot; Not Comprehending &mdash; the next discourse, on being led astray "
        "by other doctrines while still spiritually asleep.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.7 — Appaṭividitasutta
# --------------------------------------------------------------------------- #
page(
    1, 7, "Appaṭividita", "Not Comprehending",
    meta_title="SN 1.7 — Not Comprehending | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Appaṭividitasutta "
        "— a deity's verse on those who have not deciphered the teachings being led astray "
        "by other doctrines, and the Buddha's answer for those who have. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as the discourses before it"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse on those who have not understood, answered by a "
                 "four-line verse in the same structure for those who have"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple in form, though "
                       "sleep is again used figuratively, as at SN 1.6"),
        ("Companion discourse", "SN 1.8, the next discourse, restates this verse's exact "
                                "skeleton with a single key term swapped"),
    ],
    why=(
        "The deity's verse describes a specific spiritual danger: those who have not "
        "&lsquo;deciphered&rsquo; or penetrated the teachings (<em>appaṭividitā</em>) are "
        "liable to be led astray by the doctrines of others. Still figuratively asleep, they "
        "have not woken up, and it is time for them to. The Buddha's reply gives the mirror "
        "image: those who have well deciphered the teachings are not led astray; having "
        "woken and rightly understood, they &lsquo;smoothly walk in the rough&rsquo; "
        "&mdash; moving without difficulty through terrain that would otherwise trip "
        "others up."),
    guide=[
        ("A verse in two mirrored halves", [
            "The deity's verse and the Buddha's answer share an identical grammatical "
            "shape, differing only by negation: &lsquo;those whose teachings are not "
            "deciphered&rsquo; versus &lsquo;those whose teachings are well "
            "deciphered,&rsquo; &lsquo;may be led astray&rsquo; versus &lsquo;won't be led "
            "astray,&rsquo; &lsquo;have not woken up&rsquo; versus &lsquo;have woken up.&rsquo; "
            "Every clause in the answer directly inverts a clause in the question."]),
        ("Sleep as a figure, again", [
            "Like SN 1.6 immediately before it, this discourse uses waking and sleeping "
            "figuratively rather than literally: to be &lsquo;asleep&rsquo; here is to lack "
            "understanding of the teachings, and to &lsquo;wake up&rsquo; is to comprehend "
            "them. The image recurs across consecutive discourses in this vagga without "
            "being announced as a repeating device."]),
        ("Walking smoothly in the rough", [
            "The Buddha's closing image &mdash; those who have rightly understood "
            "&lsquo;smoothly walk in the rough&rsquo; (<em>caranti visame samaṁ</em>) "
            "&mdash; pictures uneven, difficult terrain that nonetheless poses no obstacle "
            "to someone who sees clearly. The difficulty of the terrain has not changed; "
            "only the walker's footing has."]),
        ("A pair with SN 1.8", [
            "The very next discourse in this collection restates this verse almost word for "
            "word, changing only the key term for the failure being described: "
            "&lsquo;not deciphered&rsquo; (<em>appaṭividitā</em>) here becomes &lsquo;very "
            "confused&rsquo; (<em>susammuṭṭhā</em>) there. Reading the two together shows how "
            "close but not identical two nearby verses in this vagga can be."]),
    ],
    terms=[
        ("appaṭividitā",
         "&ldquo;not deciphered, not penetrated&rdquo; &mdash; the failure this discourse's "
         "title names, describing teachings not properly understood."),
        ("paravādesu nīyare",
         "&ldquo;may be led astray by the doctrines of others&rdquo; &mdash; the "
         "consequence the deity's verse attaches to not comprehending the teachings."),
        ("suttā nappabujjhanti",
         "&ldquo;asleep, they have not woken up&rdquo; &mdash; the figurative sleep shared "
         "with SN 1.6, here applied specifically to not understanding the teachings."),
        ("sambuddhā sammadaññāya",
         "&ldquo;having woken up, rightly knowing&rdquo; &mdash; the Buddha's mirrored "
         "description of those who have deciphered the teachings well."),
        ("caranti visame samaṁ",
         "&ldquo;they walk smoothly in the rough&rdquo; &mdash; the closing image, picturing "
         "difficult terrain posing no obstacle to one who understands clearly."),
    ],
    text_intro=(
        "The discourse in full: a warning for those who have not understood the teachings, "
        "mirrored by an answer for those who have. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.7:1.1-1.2"),
        ("p", "&sect;2", "sn1.7:2.1-2.4"),
        ("p", "&sect;3", "sn1.7:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does the deity's verse say about those who have not 'deciphered' the teachings?",
         "opts": [
             "They may be led astray by the doctrines of others",
             "They will automatically attain awakening",
             "They cannot ever learn the teachings",
             "They are punished by the deities"],
         "correct": 0,
         "expl": "Appaṭividitā &mdash; not penetrated, leaving them vulnerable to other doctrines."},
        {"q": "How does the Buddha's answering verse relate to the deity's question?",
         "opts": [
             "It mirrors the same structure, inverting each clause for those who have understood well",
             "It ignores the question and changes the subject",
             "It rejects the deity's premise entirely",
             "It repeats the question without answering"],
         "correct": 0,
         "expl": "Every clause in the answer directly inverts a clause in the question."},
        {"q": "What figurative image does this discourse share with SN 1.6?",
         "opts": [
             "Waking and sleeping, used to describe understanding versus not understanding",
             "Crossing a flood",
             "A green reed being mowed down",
             "The world's bait"],
         "correct": 0,
         "expl": "Sleep figures a lack of comprehension in both discourses."},
        {"q": "What does 'caranti visame samaṁ' mean?",
         "opts": [
             "'They walk smoothly in the rough' &mdash; difficult terrain poses no obstacle to one who understands",
             "'They avoid all difficult places'",
             "'They cannot walk at all'",
             "'They walk only in comfortable places'"],
         "correct": 0,
         "expl": "The terrain's difficulty is unchanged; only the walker's footing differs."},
        {"q": "How does the next discourse, SN 1.8, relate to this one?",
         "opts": [
             "It restates this verse almost word for word, swapping one key term",
             "It directly contradicts this discourse",
             "It has no relation to this discourse",
             "It is a much longer prose expansion"],
         "correct": 0,
         "expl": "'Not deciphered' (appaṭividitā) here becomes 'very confused' (susammuṭṭhā) there."},
        {"q": "What does 'sambuddhā sammadaññāya' describe?",
         "opts": [
             "Those who have woken up and rightly know, per the Buddha's answer",
             "Those who remain asleep to the teachings",
             "A type of deity",
             "A meditation posture"],
         "correct": 0,
         "expl": "The mirrored description of those who have deciphered the teachings well."},
        {"q": "What consequence does the deity's verse attach to not comprehending the teachings?",
         "opts": [
             "Being led astray by the doctrines of others",
             "Immediate liberation",
             "Rebirth as a deity",
             "No consequence is named"],
         "correct": 0,
         "expl": "Paravādesu nīyare &mdash; led astray by others' doctrines."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as before",
             "A forest hermitage",
             "No setting is given",
             "A different city entirely"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame continues."},
        {"q": "What does 'appaṭividitā' mean?",
         "opts": [
             "'Not deciphered, not penetrated'",
             "'Well understood'",
             "'A deity's name'",
             "'A type of verse'"],
         "correct": 0,
         "expl": "The specific failure this discourse's title names."},
        {"q": "Is the terrain itself different for the one who understands well, according to the closing image?",
         "opts": [
             "No &mdash; the terrain remains rough; only the walker's footing changes",
             "Yes, the terrain becomes completely smooth",
             "The terrain disappears entirely",
             "The image does not involve terrain at all"],
         "correct": 0,
         "expl": "Caranti visame samaṁ &mdash; smooth walking in what remains rough ground."},
    ],
    marginalia=[
        ("A mirrored verse", [
            "not deciphered, led astray &mdash;",
            "well deciphered, not led astray",
        ]),
        ("Sleep, again as figure", [
            "asleep to the teachings,",
            "not yet woken up",
        ]),
        ("Smooth in the rough", [
            "caranti visame samaṁ &mdash;",
            "the ground unchanged, the footing sure",
        ]),
        ("A near-twin ahead", [
            "SN 1.8 restates this verse,",
            "one term swapped",
        ]),
    ],
    further=[
        '<a href="%s/sn1.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.6.html">SN 1.6 &middot; Awake</a> &mdash; the discourse immediately '
        "before this one, sharing its figurative use of sleep.",
        '<a href="sn-1.5.html">SN 1.5 &middot; Cut How Many?</a> &mdash; further back in '
        "this same collection.",
        "SN 1.8 &middot; Very Confused &mdash; the next discourse, restating this verse's "
        "skeleton with one key term changed.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.8 — Susammuṭṭhasutta
# --------------------------------------------------------------------------- #
page(
    1, 8, "Susammuṭṭha", "Very Confused",
    meta_title="SN 1.8 — Very Confused | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Susammuṭṭhasutta "
        "— a near-restatement of SN 1.7 with a single key term changed, from 'not "
        "deciphered' to 'very confused.' From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as the discourses before it"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "The same four-line verse structure as SN 1.7, with one key term replaced "
                 "throughout"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest kind of "
                       "reading here, given how closely it tracks the discourse just read"),
        ("Companion discourse", "SN 1.7, immediately before this one, shares every line of "
                                "this verse's structure but one term"),
    ],
    why=(
        "This discourse restates SN 1.7 almost exactly, with a single substitution: where "
        "that verse spoke of teachings &lsquo;not deciphered&rsquo; (<em>appaṭividitā</em>), "
        "this one speaks of teachings &lsquo;very confused&rsquo; or thoroughly muddled "
        "(<em>susammuṭṭhā</em>). Every other line &mdash; the danger of being led astray by "
        "other doctrines, the figure of sleep, the Buddha's mirrored answer, the closing "
        "image of walking smoothly in the rough &mdash; carries over unchanged."),
    guide=[
        ("One term changed, the rest identical", [
            "Set beside SN 1.7 directly, the two verses diverge only in their opening "
            "description of the failure at hand: &lsquo;not deciphered&rsquo; there becomes "
            "&lsquo;very confused&rsquo; here. The consequence named &mdash; being led "
            "astray by other doctrines &mdash; and the Buddha's full mirrored answer are "
            "word for word the same in both discourses."]),
        ("Not deciphering versus being confused", [
            "The distinction between the two terms is one of degree or kind, not of "
            "outcome: <em>appaṭividitā</em> describes teachings simply not yet penetrated, "
            "while <em>susammuṭṭhā</em> describes something closer to active confusion "
            "&mdash; a mind that has muddled what it encountered, rather than one that "
            "merely has not yet grasped it. Both are treated as equally liable to being led "
            "astray."]),
        ("Why place two such close verses side by side", [
            "This vagga elsewhere pairs discourses that share an opening formula and vary "
            "only their conclusion, as at SN 1.3 and SN 1.4. Here the pattern runs the "
            "other direction: the conclusion, structure, and most of the wording stay fixed, "
            "and only the diagnosis at the very start shifts. Reading SN 1.7 and SN 1.8 "
            "together shows this vagga using near-repetition itself as a way of marking out "
            "closely related but distinct failures."]),
        ("The unchanged answer", [
            "The Buddha's reply here is identical to SN 1.7's: those whose teachings are "
            "well deciphered (<em>suppaṭividitā</em>, contrasted with "
            "<em>asammuṭṭhā</em>, &lsquo;unconfused,&rsquo; here) are not led astray, have "
            "woken up, rightly know, and walk smoothly in the rough. The prescription for "
            "confusion and the prescription for non-comprehension turn out to be exactly "
            "the same."]),
    ],
    terms=[
        ("susammuṭṭhā",
         "&ldquo;very confused, thoroughly muddled&rdquo; &mdash; the failure this "
         "discourse's title names, distinct from but closely related to SN 1.7's &lsquo;not "
         "deciphered.&rsquo;"),
        ("asammuṭṭhā",
         "&ldquo;unconfused&rdquo; &mdash; the Buddha's counter-term in his answering verse, "
         "mirroring <em>susammuṭṭhā</em> by simple negation."),
        ("paravādesu nīyare",
         "&ldquo;may be led astray by the doctrines of others&rdquo; &mdash; the same "
         "consequence named in SN 1.7, carried over here unchanged."),
        ("suttā nappabujjhanti",
         "&ldquo;asleep, they have not woken up&rdquo; &mdash; the same figurative sleep "
         "used at SN 1.6 and SN 1.7, appearing here for a third consecutive discourse."),
        ("caranti visame samaṁ",
         "&ldquo;they walk smoothly in the rough&rdquo; &mdash; the closing image, identical "
         "to SN 1.7's, describing understanding that meets difficult ground without "
         "difficulty."),
    ],
    text_intro=(
        "The discourse in full: SN 1.7's verse restated with one key term changed. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.8:1.1-1.2"),
        ("p", "&sect;2", "sn1.8:2.1-2.4"),
        ("p", "&sect;3", "sn1.8:3.1-3.4"),
    ],
    quiz=[
        {"q": "What single term changes between SN 1.7 and this discourse?",
         "opts": [
             "'Not deciphered' (appaṭividitā) becomes 'very confused' (susammuṭṭhā)",
             "'Sleep' becomes 'wakefulness'",
             "'Led astray' becomes 'guided rightly'",
             "The setting changes from Sāvatthī to another city"],
         "correct": 0,
         "expl": "The only substitution between these two closely paired verses."},
        {"q": "What consequence does this discourse attach to being 'very confused' about the teachings?",
         "opts": [
             "Being led astray by the doctrines of others, the same as SN 1.7",
             "Immediate rebirth as a deity",
             "No consequence is named",
             "Being unable to ever hear the teachings again"],
         "correct": 0,
         "expl": "Paravādesu nīyare &mdash; identical to SN 1.7's stated consequence."},
        {"q": "How does the Buddha's answering verse here compare to SN 1.7's?",
         "opts": [
             "It is essentially identical, mirroring 'confused' with 'unconfused' the way SN 1.7 mirrored 'not deciphered' with 'well deciphered'",
             "It is a completely different answer",
             "It refuses to answer the riddle",
             "It gives a much longer prose explanation instead"],
         "correct": 0,
         "expl": "Asammuṭṭhā mirrors susammuṭṭhā by simple negation, as in SN 1.7."},
        {"q": "What distinction, if any, exists between 'not deciphered' and 'very confused'?",
         "opts": [
             "One suggests not yet grasping the teachings, the other suggests actively muddled understanding",
             "They are completely unrelated concepts",
             "One refers to deities and the other to humans",
             "There is no meaningful difference at all between the discourses"],
         "correct": 0,
         "expl": "A difference in degree or kind, though both lead to the same danger."},
        {"q": "What figurative image, used across three consecutive discourses, appears again here?",
         "opts": [
             "Sleep and waking, describing spiritual dullness and alertness",
             "The flood being crossed",
             "The world's bait",
             "A reed being mowed down"],
         "correct": 0,
         "expl": "Continuing from SN 1.6 and SN 1.7."},
        {"q": "What closing image does this discourse share word for word with SN 1.7?",
         "opts": [
             "'They walk smoothly in the rough' (caranti visame samaṁ)",
             "'They cross the flood neither standing nor swimming'",
             "'A seeker of peace drops the world's bait'",
             "'Like a green reed mowed down'"],
         "correct": 0,
         "expl": "Identical closing line to SN 1.7's answering verse."},
        {"q": "What does this pairing of SN 1.7 and SN 1.8 illustrate about this vagga's method?",
         "opts": [
             "It can hold structure and conclusion fixed while varying only the initial diagnosis",
             "It always varies every line between consecutive discourses",
             "It never repeats any wording between discourses",
             "It abandons verse form entirely for this pair"],
         "correct": 0,
         "expl": "The opposite pattern from SN 1.3/1.4, which varied the opening and kept the conclusion fixed."},
        {"q": "What does 'asammuṭṭhā' mean?",
         "opts": [
             "'Unconfused'",
             "'Very confused'",
             "'Asleep'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "The Buddha's counter-term, negating susammuṭṭhā."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as before",
             "A mountain retreat",
             "No setting is given",
             "A river crossing"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame continues."},
        {"q": "Does the Buddha's prescription differ between confusion (SN 1.8) and non-comprehension (SN 1.7)?",
         "opts": [
             "No &mdash; the prescription given is exactly the same in both discourses",
             "Yes, entirely different prescriptions are given",
             "SN 1.8 gives no prescription at all",
             "SN 1.7 gives no prescription at all"],
         "correct": 0,
         "expl": "Both failures receive the identical mirrored answer."},
    ],
    marginalia=[
        ("One term swapped", [
            "not deciphered, or",
            "very confused &mdash; same danger",
        ]),
        ("The rest, unchanged", [
            "led astray, asleep,",
            "not yet woken up",
        ]),
        ("Asammuṭṭhā", [
            "unconfused &mdash;",
            "the Buddha's mirrored term",
        ]),
        ("A third sleep, in a row", [
            "SN 1.6, 1.7, 1.8 &mdash;",
            "the same figure, three times",
        ]),
    ],
    further=[
        '<a href="%s/sn1.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.7.html">SN 1.7 &middot; Not Comprehending</a> &mdash; the discourse '
        "this one restates, with one key term changed.",
        '<a href="sn-1.6.html">SN 1.6 &middot; Awake</a> &mdash; the first of three '
        "consecutive discourses to use sleep as a figure for spiritual dullness.",
        "SN 1.9 &middot; Fond of Conceit &mdash; the next discourse, on conceit and solitary "
        "practice in the wilderness.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.9 — Mānakāmasutta
# --------------------------------------------------------------------------- #
page(
    1, 9, "Mānakāma", "Fond of Conceit",
    meta_title="SN 1.9 — Fond of Conceit | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mānakāmasutta — a "
        "deity's verse on conceit as an obstacle to taming, and the Buddha's answer "
        "describing the one who has given up conceit and practices alone in the "
        "wilderness. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as the discourses before it"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse naming conceit as an obstacle, answered by a four-line "
                 "verse describing its opposite"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form, "
                       "introducing the wilderness-dwelling theme this vagga's closing "
                       "discourse will take up next"),
        ("Looking ahead", "The image of practicing &lsquo;alone in the wilderness&rsquo; "
                          "recurs, expanded, in this vagga's final discourse, SN 1.10"),
    ],
    why=(
        "The deity's verse names a specific obstacle: one fond of conceit "
        "(<em>mānakāma</em>) cannot be tamed, and no sage lacks immersion &mdash; meaning "
        "conceit and the absence of immersion are treated as of a piece. Living negligently "
        "alone in the wilderness, such a person cannot cross beyond Death's dominion "
        "&mdash; solitude by itself accomplishes nothing without the right inner condition. "
        "The Buddha's reply describes the reverse: one who has given up conceit, is well "
        "immersed, good-hearted, and everywhere free, living diligently &mdash; not "
        "merely alone &mdash; in the wilderness does cross beyond Death's dominion."),
    guide=[
        ("Conceit as an obstacle to taming", [
            "<em>Mānakāma</em>, &lsquo;fond of conceit,&rsquo; opens the verse as a "
            "description of someone who cannot be tamed or trained. The verse pairs this "
            "directly with a lack of immersion (<em>asamāhitassa</em>): a mind occupied "
            "with conceit and a mind lacking immersion are treated as two names for one and "
            "the same untrained condition."]),
        ("Solitude is not sufficient by itself", [
            "The deity's verse makes a point easy to miss: living alone in the wilderness "
            "does not, by itself, get anyone beyond Death's dominion, if that solitude is "
            "negligent (<em>pamatto</em>). The setting of wilderness practice is named in "
            "both halves of this verse, but only diligence (<em>appamatto</em>) in the "
            "Buddha's reply, not the wilderness itself, is what makes the difference."]),
        ("A precise inversion", [
            "As in several other discourses in this vagga, the Buddha's answer inverts the "
            "deity's terms one by one: conceit given up rather than indulged, well "
            "immersed rather than lacking immersion, diligent rather than negligent. The "
            "wilderness setting itself does not change between the two verses &mdash; only "
            "the inner condition of the one dwelling there does."]),
        ("Setting up the vagga's closing discourse", [
            "This is the second discourse in a row, after SN 1.6 through SN 1.8's shared "
            "sleep-imagery, to dwell on solitary wilderness practice. The very next "
            "discourse, SN 1.10 &mdash; and this vagga's last &mdash; takes up the same "
            "wilderness setting directly, in the well-known verse that gives the whole "
            "vagga its name."]),
    ],
    terms=[
        ("mānakāma",
         "&ldquo;fond of conceit&rdquo; &mdash; this discourse's title, describing the "
         "obstacle its opening verse names."),
        ("asamāhitassa",
         "&ldquo;for one lacking immersion&rdquo; &mdash; paired with conceit in the "
         "deity's verse as two names for the same untrained condition."),
        ("pamatto",
         "&ldquo;negligent&rdquo; &mdash; the quality that, in the deity's verse, makes "
         "solitary wilderness dwelling insufficient by itself."),
        ("appamatto",
         "&ldquo;diligent&rdquo; &mdash; its opposite, in the Buddha's reply, describing "
         "the wilderness-dweller who does cross beyond Death's dominion."),
        ("maccudheyya",
         "&ldquo;Death's dominion&rdquo; &mdash; what remains uncrossed by conceit and "
         "negligence, and crossed by their absence."),
    ],
    text_intro=(
        "The discourse in full: conceit and negligence as obstacles, given up and reversed "
        "in the Buddha's answer. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.9:1.1-1.2"),
        ("p", "&sect;2", "sn1.9:2.1-2.4"),
        ("p", "&sect;3", "sn1.9:3.1-3.4"),
    ],
    quiz=[
        {"q": "What obstacle does the deity's verse open by naming?",
         "opts": [
             "Being fond of conceit (mānakāma), which prevents taming",
             "Being too generous",
             "Living in a city rather than the wilderness",
             "Speaking too much"],
         "correct": 0,
         "expl": "Māna, 'conceit,' + kāma, 'fond of' &mdash; the discourse's title."},
        {"q": "What does the deity's verse pair conceit with?",
         "opts": [
             "A lack of immersion (asamāhitassa)",
             "Excessive wealth",
             "Physical illness",
             "A large following of students"],
         "correct": 0,
         "expl": "Both treated as two names for the same untrained condition."},
        {"q": "According to the deity's verse, is living alone in the wilderness sufficient by itself?",
         "opts": [
             "No &mdash; if that solitude is negligent (pamatto), it accomplishes nothing",
             "Yes, solitude alone always guarantees liberation",
             "The verse does not mention wilderness at all",
             "Only if performed in a specific season"],
         "correct": 0,
         "expl": "Negligent solitude does not cross beyond Death's dominion."},
        {"q": "What quality does the Buddha's reply substitute for negligence?",
         "opts": [
             "Diligence (appamatto)",
             "Wealth",
             "Fame",
             "Silence"],
         "correct": 0,
         "expl": "The precise inversion of pamatto in the deity's verse."},
        {"q": "What does 'maccudheyya' mean?",
         "opts": [
             "'Death's dominion' &mdash; what is crossed by giving up conceit and negligence",
             "'A type of deity'",
             "'A meditation posture'",
             "'The world's bait'"],
         "correct": 0,
         "expl": "The goal named in both the deity's verse and the Buddha's reply."},
        {"q": "How does the Buddha's answering verse relate structurally to the deity's question?",
         "opts": [
             "It inverts the deity's terms one by one: conceit given up, well immersed, diligent",
             "It ignores the deity's terms entirely",
             "It repeats the deity's verse without change",
             "It rejects the wilderness setting as unhelpful"],
         "correct": 0,
         "expl": "A precise, term-by-term inversion, as seen elsewhere in this vagga."},
        {"q": "What discourse immediately follows this one, continuing the wilderness theme?",
         "opts": [
             "SN 1.10, this vagga's closing discourse",
             "SN 1.1, the vagga's opening discourse",
             "SN 2.1, the next saṃyutta",
             "No discourse follows; this is the vagga's last"],
         "correct": 0,
         "expl": "SN 1.10 takes up the wilderness setting directly, in this vagga's namesake verse."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as before",
             "Deep in the wilderness itself",
             "No setting is given",
             "A royal palace"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame continues, even while its content describes wilderness practice."},
        {"q": "What does 'appamatto' mean?",
         "opts": [
             "'Diligent'",
             "'Negligent'",
             "'Fond of conceit'",
             "'Lacking immersion'"],
         "correct": 0,
         "expl": "The Buddha's substituted quality, opposite to pamatto."},
        {"q": "According to this discourse, does the wilderness setting itself change between the two verses?",
         "opts": [
             "No &mdash; only the inner condition of the one dwelling there changes",
             "Yes, the Buddha describes a completely different location",
             "The wilderness disappears in the Buddha's reply",
             "The deity's verse does not mention any setting"],
         "correct": 0,
         "expl": "Both verses describe wilderness dwelling; only diligence versus negligence differs."},
    ],
    marginalia=[
        ("Conceit, untamed", [
            "mānakāma &mdash;",
            "fond of conceit, untamed",
        ]),
        ("Solitude alone is not enough", [
            "negligent in the wilderness,",
            "still short of the goal",
        ]),
        ("A precise inversion", [
            "conceit given up,",
            "diligent, not negligent",
        ]),
        ("Wilderness, twice", [
            "this discourse, and the next &mdash;",
            "SN 1.10 closes the theme",
        ]),
    ],
    further=[
        '<a href="%s/sn1.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="sn-1.8.html">SN 1.8 &middot; Very Confused</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.6.html">SN 1.6 &middot; Awake</a> &mdash; further back in this same '
        "collection.",
        "SN 1.10 &middot; Wilderness &mdash; the next discourse, this vagga's last, and the "
        "source of the whole chapter's name.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.10 — Araññasutta (closes the Naḷavagga)
# --------------------------------------------------------------------------- #
page(
    1, 10, "Arañña", "Wilderness",
    meta_title="SN 1.10 — Wilderness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Araññasutta — a "
        "deity's question about the clear complexion of wilderness-dwelling renunciants, "
        "and the Buddha's two-stanza reply on not grieving the past or the future. The "
        "discourse that closes the Naḷavagga and gives it its name. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the same recurring "
                    "circumstances as this vagga's other nine discourses"),
        ("Speakers", "An unnamed deity and the Buddha, this time in a two-stanza reply "
                    "rather than one"),
        ("Form", "A four-line question, answered by two four-line stanzas continuing one "
                 "thought"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple in its central "
                       "image, though the closing simile gives this vagga its name"),
        ("Closing the chapter", "This is the tenth and last discourse of the Naḷavagga "
                                "(&lsquo;the Chapter on a Reed&rsquo;), which takes its "
                                "name from this discourse's final line"),
    ],
    why=(
        "A deity asks a simple, almost curious question: wilderness-dwelling renunciants, "
        "peaceful and eating only one meal a day, nonetheless have a notably clear "
        "complexion &mdash; why? The Buddha's answer, unusually given in two stanzas rather "
        "than the vagga's usual one, locates the reason not in diet or setting but in "
        "relationship to time: those who neither grieve the past nor long for the future, "
        "living on whatever the present day brings, keep a clear complexion; those who do "
        "long and grieve wither away &lsquo;like a green reed mowed down&rsquo; &mdash; the "
        "very image this vagga, the Naḷavagga, takes its name from."),
    guide=[
        ("A question about appearances", [
            "The deity's question is concrete and almost domestic: people eating one meal a "
            "day in the wilderness would seem, by ordinary reasoning, to look drawn and "
            "worn &mdash; instead their complexion is clear. The question asks for the "
            "cause of an effect anyone could observe."]),
        ("The answer is temporal, not dietary", [
            "The Buddha's answer does not address diet or asceticism directly. Instead it "
            "names a relationship to time: not grieving the past (<em>atītaṁ "
            "nānusocanti</em>), not longing for the future (<em>nappajappanti "
            "anāgataṁ</em>), and living on whatever the present day brings "
            "(<em>paccuppannena yāpenti</em>). Clarity of complexion, in this verse, is the "
            "visible mark of an undivided relationship to the present."]),
        ("The reed that gives this vagga its name", [
            "The second stanza states the reverse case in a single memorable image: those "
            "who long for the future and grieve the past &lsquo;wither away, like a green "
            "reed mowed down&rsquo; (<em>naḷova harito luto</em>). This simile is the source "
            "of this vagga's own name, Naḷavagga, &lsquo;the Chapter on a Reed&rsquo; "
            "&mdash; the whole chapter is named after the closing image of its final "
            "discourse."]),
        ("A two-stanza reply, unusual in this vagga", [
            "Every other discourse in this vagga answers a deity's four-line verse with "
            "exactly one four-line verse of its own. This discourse's answer runs to two "
            "full stanzas, elaborating the same thought &mdash; presence versus longing "
            "and grief &mdash; before it closes. Nothing in the text explains the "
            "extension; it simply gives the vagga's closing discourse more room than its "
            "others."]),
        ("An unmarked closing verse", [
            "In the source text, this discourse is followed immediately by two lines "
            "marking the end of the Naḷavagga and a mnemonic verse (<em>uddāna</em>) "
            "listing all ten of its discourse-titles in order &mdash; standard "
            "bookkeeping for reciters, not part of the discourse itself, and left "
            "untranslated in this edition. It is described here rather than quoted, "
            "following this project's practice of not putting untranslated source lines "
            "into the text panel."]),
    ],
    terms=[
        ("araññe viharataṁ",
         "&ldquo;for those dwelling in the wilderness&rdquo; &mdash; the deity's opening "
         "description, naming the setting this discourse's title and this vagga's closing "
         "image both draw on."),
        ("atītaṁ nānusocanti",
         "&ldquo;they don't grieve for the past&rdquo; &mdash; the first half of the "
         "Buddha's answer, describing an undivided relationship to time."),
        ("paccuppannena yāpenti",
         "&ldquo;they feed on whatever comes that day&rdquo; &mdash; living on the present "
         "moment, given as the specific cause of a clear complexion."),
        ("naḷova harito luto",
         "&ldquo;like a green reed mowed down&rdquo; &mdash; the discourse's closing simile, "
         "and the source of this vagga's own name, Naḷavagga."),
        ("vaṇṇo pasīdati",
         "&ldquo;the complexion becomes clear&rdquo; &mdash; the specific effect the deity "
         "asks about and the Buddha's two stanzas explain."),
    ],
    text_intro=(
        "The discourse in full: a question about clear complexion, answered in two stanzas "
        "on grief, longing, and the present. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.10:1.1-1.2"),
        ("p", "&sect;2", "sn1.10:2.1-2.4"),
        ("p", "&sect;3", "sn1.10:3.1-3.4"),
        ("p", "&sect;4", "sn1.10:4.1-4.4"),
    ],
    quiz=[
        {"q": "What question does the deity ask at the start of this discourse?",
         "opts": [
             "Why wilderness-dwelling renunciants who eat only one meal a day have such a clear complexion",
             "How to cross the flood",
             "How many things must be cut, dropped, and developed",
             "What causes conceit"],
         "correct": 0,
         "expl": "A concrete question about an observable effect."},
        {"q": "What does the Buddha's answer locate as the cause of a clear complexion?",
         "opts": [
             "Not grieving the past and not longing for the future, living on the present",
             "The specific food eaten",
             "The particular wilderness location",
             "The number of meals eaten per day"],
         "correct": 0,
         "expl": "A temporal explanation, not a dietary one."},
        {"q": "What image closes this discourse's second stanza, and gives this vagga its name?",
         "opts": [
             "'Like a green reed mowed down' (naḷova harito luto)",
             "'Like a flood sweeping all away'",
             "'Like a deity vanishing at dawn'",
             "'Like a mountain wearing down'"],
         "correct": 0,
         "expl": "The source of this vagga's own name, Naḷavagga, 'the Chapter on a Reed.'"},
        {"q": "How many stanzas does the Buddha's reply run to in this discourse?",
         "opts": [
             "Two, unlike every other discourse in this vagga, which answer with one",
             "One, the same as every other discourse in this vagga",
             "Four full stanzas",
             "The Buddha gives no verse reply at all"],
         "correct": 0,
         "expl": "An unusual extension for this vagga's closing discourse."},
        {"q": "What does 'paccuppannena yāpenti' mean?",
         "opts": [
             "'They feed on whatever comes that day'",
             "'They grieve for the future'",
             "'They cross the flood'",
             "'They gather dust'"],
         "correct": 0,
         "expl": "Living on the present moment, given as the cause of clear complexion."},
        {"q": "What follows this discourse in the source text, according to this reading guide?",
         "opts": [
             "A closing line marking the vagga's end, plus an untranslated mnemonic verse listing all ten discourse titles",
             "The opening of the next saṃyutta, SN 2",
             "A prose commentary explaining the reed simile",
             "Nothing; the source text ends abruptly"],
         "correct": 0,
         "expl": "Standard reciter's bookkeeping, described here but not quoted, since it is untranslated."},
        {"q": "According to the discourse, what happens to those who long for the future and grieve the past?",
         "opts": [
             "They 'wither away, like a green reed mowed down'",
             "They immediately attain awakening",
             "Nothing; the verse says this has no effect",
             "They become deities"],
         "correct": 0,
         "expl": "The fate the second stanza names for the opposite orientation to time."},
        {"q": "What is this discourse's position within the Naḷavagga?",
         "opts": [
             "It is the tenth and last discourse of the vagga",
             "It is the first discourse of the vagga",
             "It is the fifth discourse, at the vagga's midpoint",
             "It does not belong to the Naḷavagga at all"],
         "correct": 0,
         "expl": "This discourse closes the vagga and supplies its name."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the same recurring circumstances as this vagga's other discourses",
             "In the wilderness itself, where the renunciants described are dwelling",
             "No setting is given",
             "At a different monastery from the rest of the vagga"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's recurring frame, even while the content describes wilderness dwellers."},
        {"q": "What does 'atītaṁ nānusocanti' mean?",
         "opts": [
             "'They don't grieve for the past'",
             "'They don't remember the past at all'",
             "'They grieve constantly'",
             "'They long for the future'"],
         "correct": 0,
         "expl": "The first half of the Buddha's two-part explanation."},
    ],
    marginalia=[
        ("A question about complexion", [
            "one meal a day, in the wilderness &mdash;",
            "why so clear a look?",
        ]),
        ("Not diet, but time", [
            "no grief for the past,",
            "no longing for what's ahead",
        ]),
        ("The reed, mowed down", [
            "naḷova harito luto &mdash;",
            "this vagga's own name",
        ]),
        ("The Naḷavagga closes", [
            "ten discourses complete;",
            "the next saṃyutta lies ahead",
        ]),
    ],
    further=[
        '<a href="%s/sn1.10/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.9.html">SN 1.9 &middot; Fond of Conceit</a> &mdash; the discourse '
        "immediately before this one, also set in the wilderness.",
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this vagga&rsquo;s '
        "opening discourse, ten discourses back.",
        '<a href="sn-1.5.html">SN 1.5 &middot; Cut How Many?</a> &mdash; another discourse '
        "in this vagga returning to the theme of what must be left behind.",
    ],
)
