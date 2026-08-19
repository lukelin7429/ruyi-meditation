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


# --------------------------------------------------------------------------- #
# SN 1.11 — Nandanasutta (opens the Nandanavagga)
# --------------------------------------------------------------------------- #
page(
    1, 11, "Nandana", "The Garden of Delight",
    meta_title="SN 1.11 — The Garden of Delight | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nandanasutta — the "
        "Buddha's account of two deities in the heavenly Garden of Delight, one praising its "
        "pleasures, the other reciting a verse on impermanence. Opens the Nandanavagga. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; the Buddha narrates a past event "
                    "to the assembled mendicants rather than reporting a direct exchange"),
        ("Speakers", "The Buddha, narrating; within the story, two deities of the Thirty-Three "
                    "exchanging verses in the heavenly Garden of Delight"),
        ("Form", "Narrated frame in prose, containing two four-line verses spoken by "
                 "different deities"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form; the "
                       "closing verse is one of this collection&rsquo;s best known"),
        ("Opening this vagga", "The first discourse of the Nandanavagga (&lsquo;the Chapter "
                               "on the Garden of Delight&rsquo;), which takes its name from "
                               "this discourse&rsquo;s setting"),
    ],
    why=(
        "Unlike every discourse in the previous vagga, this one is not a direct exchange "
        "between a deity and the Buddha at Jeta's Grove &mdash; it is the Buddha narrating a "
        "past event to the assembled mendicants. He recounts how, once, a deity of the "
        "company of the Thirty-Three, amusing herself amid heavenly pleasure in the Garden "
        "of Delight (Nandana), declared that no one who hasn't seen that garden knows real "
        "pleasure. Another deity present answered with a rebuke: this speaker doesn't "
        "understand what the perfected ones say &mdash; that all conditions are impermanent, "
        "arising and passing, and that their stilling, not their enjoyment, is bliss."),
    guide=[
        ("A story within a story", [
            "The frame here is one step removed from every discourse in the Naḷavagga: the "
            "Buddha is not answering a deity who has just approached him, but telling the "
            "mendicants about a past exchange between two deities he witnessed or knows of. "
            "This narrated structure recurs across the Nandanavagga's opening discourses "
            "before the vagga's later discourses drop narrative framing almost entirely."]),
        ("Pleasure defended, then corrected", [
            "The first deity's claim is simple hedonism: real pleasure belongs to those who "
            "have seen Nandana, the abode of the &lsquo;lordly gods&rsquo; of the Thirty-"
            "Three. The second deity's reply does not dispute that Nandana is pleasurable "
            "&mdash; it dismisses the whole premise that any such pleasure, however "
            "glorious, constitutes real happiness at all."]),
        ("A verse this collection returns to often", [
            "The second deity's answer &mdash; &lsquo;all conditions "
            "(<em>saṅkhārā</em>) are impermanent, their nature is to rise and fall; having "
            "arisen, they cease; their settling is such bliss&rsquo; &mdash; states this "
            "collection's central teaching on impermanence in its most compact form. A "
            "closely related verse, differing in its opening word but sharing this same "
            "closing two lines almost exactly, is what Sakka is famously said to have "
            "recited on the Buddha's passing, in the Mahāparinibbāna Sutta (DN 16) &mdash; "
            "worth noting as a close variant, not a claim that the two verses are word-for-"
            "word identical."]),
        ("Where 'bliss' actually lies", [
            "The verse's final claim reverses the first deity's whole framework: not the "
            "arising of pleasant experience but its <em>vūpasama</em>, its "
            "&lsquo;settling&rsquo; or stilling, is called <em>sukha</em>, bliss. Heavenly "
            "sense-pleasure and the stilling of conditioned experience are treated here as "
            "opposite, not complementary, kinds of well-being."]),
    ],
    terms=[
        ("nandana",
         "the &ldquo;Garden of Delight,&rdquo; a park in the Tāvatiṃsa heaven of the Thirty-"
         "Three gods, and the setting this discourse and its vagga are named after."),
        ("tāvatiṃsakāyikā devatā",
         "&ldquo;a deity of the company of the Thirty-Three&rdquo; &mdash; the class of "
         "heavenly being the first speaker in this discourse belongs to."),
        ("aniccā sabbasaṅkhārā",
         "&ldquo;all conditions are impermanent&rdquo; &mdash; the second deity's opening "
         "claim, naming the universal characteristic the first deity's praise of Nandana "
         "overlooks."),
        ("uppādavayadhammino",
         "&ldquo;their nature is to rise and fall&rdquo; &mdash; describing conditioned "
         "phenomena's essential instability, not an occasional or exceptional trait."),
        ("vūpasamo sukho",
         "&ldquo;their settling is bliss&rdquo; &mdash; the verse's closing claim, locating "
         "true well-being in the stilling of conditions rather than in their arising."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's account of two deities, one praising heavenly "
        "pleasure, the other answering with a verse on impermanence. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha addresses the mendicants"),
        ("p", "&sect;1", "sn1.11:1.1-1.6"),
        ("h3", "One deity praises the Garden of Delight"),
        ("p", "&sect;2", "sn1.11:2.1-3.4"),
        ("h3", "Another deity answers"),
        ("p", "&sect;3", "sn1.11:4.1-5.6"),
    ],
    quiz=[
        {"q": "How does this discourse's frame differ from every discourse in the Naḷavagga?",
         "opts": [
             "The Buddha narrates a past event to the mendicants, rather than answering a deity directly",
             "It has no speakers at all",
             "It is spoken entirely by a king",
             "It takes place in a different collection entirely"],
         "correct": 0,
         "expl": "A story within a story, one step removed from a direct exchange."},
        {"q": "What does the first deity claim in the Garden of Delight?",
         "opts": [
             "That real pleasure belongs only to those who have seen Nandana",
             "That all pleasure is worthless",
             "That the Buddha should visit heaven",
             "That mendicants should never meditate"],
         "correct": 0,
         "expl": "A straightforward defense of heavenly sensual pleasure."},
        {"q": "How does the second deity respond?",
         "opts": [
             "By reciting a verse that all conditions are impermanent and their stilling, not their arising, is bliss",
             "By agreeing completely with the first deity",
             "By refusing to speak at all",
             "By summoning the Buddha directly"],
         "correct": 0,
         "expl": "A rebuke grounded in the teaching of impermanence."},
        {"q": "What does 'vūpasamo sukho' mean?",
         "opts": [
             "'Their settling is bliss' &mdash; locating well-being in the stilling of conditions",
             "'Their arising is bliss'",
             "'Pleasure is eternal'",
             "'The Garden of Delight is bliss'"],
         "correct": 0,
         "expl": "The verse's closing claim, reversing the first deity's framework."},
        {"q": "What well-known verse elsewhere in the canon closely resembles this discourse's closing verse?",
         "opts": [
             "The verse Sakka is said to recite at the Buddha's passing, in the Mahāparinibbāna Sutta (DN 16)",
             "The opening verse of the Dhammapada",
             "A verse spoken by Māra",
             "There is no resembling verse elsewhere"],
         "correct": 0,
         "expl": "A close variant sharing its closing two lines, not a word-for-word match."},
        {"q": "What class of deity does the first speaker belong to?",
         "opts": [
             "The company of the Thirty-Three (tāvatiṃsakāyikā devatā)",
             "A hungry ghost",
             "A human ancestor spirit",
             "A serpent deity (nāga)"],
         "correct": 0,
         "expl": "Named explicitly in the Buddha's narration."},
        {"q": "What does 'uppādavayadhammino' describe?",
         "opts": [
             "Conditioned phenomena's essential nature of rising and falling",
             "A type of meditation posture",
             "A specific heavenly realm",
             "A category of monastic rule"],
         "correct": 0,
         "expl": "Instability as an inherent, not occasional, characteristic."},
        {"q": "Does the second deity dispute that the Garden of Delight is pleasurable?",
         "opts": [
             "No &mdash; it dismisses the premise that such pleasure constitutes real happiness at all",
             "Yes, it claims the garden does not exist",
             "It claims the garden is actually painful",
             "It refuses to comment on the garden itself"],
         "correct": 0,
         "expl": "The rebuke targets the whole framework, not the garden's pleasantness."},
        {"q": "What is this discourse's position in its vagga?",
         "opts": [
             "It is the first discourse of the Nandanavagga, which takes its name from this setting",
             "It is the vagga's last discourse",
             "It belongs to the Naḷavagga, not the Nandanavagga",
             "It has no fixed position"],
         "correct": 0,
         "expl": "Opens the second vagga of the Devatāsaṃyutta."},
        {"q": "Whom does the second deity say the first deity fails to understand?",
         "opts": [
             "The perfected ones (arahata vaco, 'the saying of the arahants')",
             "The Buddha specifically, by name",
             "A group of ordinary humans",
             "No one; the verse names no source"],
         "correct": 0,
         "expl": "Yathā arahataṁ vaco &mdash; the saying attributed to the perfected ones."},
    ],
    marginalia=[
        ("A story, retold", [
            "the Buddha narrates",
            "a past exchange of deities",
        ]),
        ("Pleasure claimed", [
            "&ldquo;they don&rsquo;t know pleasure",
            "who don&rsquo;t see the Garden of Delight&rdquo;",
        ]),
        ("Pleasure corrected", [
            "all conditions impermanent &mdash;",
            "their stilling is bliss",
        ]),
        ("A verse echoed elsewhere", [
            "close kin to Sakka&rsquo;s verse",
            "at the Buddha&rsquo;s passing, DN 16",
        ]),
    ],
    further=[
        '<a href="%s/sn1.11/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.10.html">SN 1.10 &middot; Wilderness</a> &mdash; the discourse that '
        "closed the previous vagga, the Naḷavagga.",
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this '
        "collection&rsquo;s opening discourse.",
        "SN 1.12 &middot; Delight &mdash; the next discourse, playing on this vagga&rsquo;s "
        "name with a single-word substitution across an entire verse.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.12 — Nandatisutta
# --------------------------------------------------------------------------- #
page(
    1, 12, "Nandati", "Delight",
    meta_title="SN 1.12 — Delight | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nandatisutta — a "
        "deity's verse claiming children, cattle, and attachment bring delight, answered by "
        "the Buddha's verse substituting a single word throughout: sorrow. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the recurring frame, now "
                    "resumed after SN 1.11's narrated exception"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse built on the word &lsquo;delight,&rsquo; answered by an "
                 "identically structured verse substituting &lsquo;sorrow&rsquo; throughout"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a single, precise "
                       "substitution carries the entire discourse's meaning"),
        ("Wordplay", "This discourse's title, Nandati (&lsquo;delights&rsquo;), echoes "
                     "Nandana, the garden that opened this vagga and gives it its name"),
    ],
    why=(
        "The deity's verse claims that children, cattle, and possessions "
        "(<em>upadhi</em>, &lsquo;attachments&rsquo; or &lsquo;substrates&rsquo;) are a "
        "source of delight, and that without such attachments there is no delight at all. "
        "The Buddha's reply does something almost mechanical and entirely devastating: it "
        "repeats the verse's exact grammatical structure, replacing every occurrence of "
        "&lsquo;delight&rsquo; (<em>nandati</em>) with &lsquo;sorrow&rsquo; "
        "(<em>socati</em>). The same attachments the deity names as the source of pleasure "
        "are, without changing a single noun, renamed as the source of grief."),
    guide=[
        ("One substitution, total reversal", [
            "Every clause of the deity's verse survives into the Buddha's reply unchanged "
            "except its central verb: <em>nandati</em> becomes <em>socati</em> throughout. "
            "Children, cattle, and attachments (<em>upadhi</em>) are not denied as real "
            "sources of feeling &mdash; the claim is that the very same attachments "
            "produce sorrow as readily as they produce delight."]),
        ("Upadhi, what is attached to", [
            "<em>Upadhi</em>, translated here as &lsquo;attachments,&rsquo; more literally "
            "names what is laid down or accumulated as a support &mdash; possessions, "
            "relationships, anything taken up and held onto. Both verses agree that "
            "<em>upadhi</em> is the single common cause of both delight and sorrow; the "
            "one <em>nirūpadhī</em>, &lsquo;without attachments,&rsquo; experiences "
            "neither."]),
        ("Echoing this vagga's name", [
            "The verb this discourse's title comes from, <em>nandati</em>, shares its root "
            "with <em>Nandana</em>, the garden that opened this vagga at SN 1.11 and gave "
            "the whole vagga its name. Where SN 1.11 corrected delight in a heavenly "
            "garden, this discourse turns the same word toward the most ordinary objects "
            "of delight &mdash; family and livestock."]),
        ("Not a rejection of family, but a diagnosis", [
            "The verse makes no claim that having children or cattle is wrong; it claims "
            "only that whatever is held onto as <em>upadhi</em> will, by that very "
            "holding, produce sorrow as surely as it produces delight. The person free of "
            "attachments is described as free of both, not as someone who has simply lost "
            "what they loved."]),
    ],
    terms=[
        ("nandati",
         "&ldquo;delights&rdquo; &mdash; the verb this discourse's title comes from, "
         "sharing its root with <em>Nandana</em>, the garden of SN 1.11."),
        ("socati",
         "&ldquo;grieves, sorrows&rdquo; &mdash; the single word substituted for "
         "<em>nandati</em> throughout the Buddha's answering verse."),
        ("upadhi",
         "&ldquo;attachments&rdquo; or &ldquo;substrates&rdquo; &mdash; what is taken up "
         "and held onto, named in both verses as the single common cause of delight and "
         "sorrow alike."),
        ("nirūpadhī",
         "&ldquo;one without attachments&rdquo; &mdash; the condition in which, both "
         "verses agree, neither delight nor sorrow of this kind arises."),
        ("puttimā",
         "&ldquo;one who has children&rdquo; &mdash; the deity's opening example, paired "
         "with cattle-ownership as an ordinary source of feeling."),
    ],
    text_intro=(
        "The discourse in full: a verse on delight, answered by the same verse with one "
        "word changed throughout. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.12:1.1-1.2"),
        ("p", "&sect;2", "sn1.12:2.1-2.4"),
        ("p", "&sect;3", "sn1.12:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does the deity's verse claim brings delight?",
         "opts": [
             "Children, cattle, and attachments (upadhi)",
             "Wisdom alone",
             "Solitude in the wilderness",
             "The five faculties"],
         "correct": 0,
         "expl": "Nandati puttehi puttimā&hellip; &mdash; the deity's opening claim."},
        {"q": "What single word does the Buddha's reply substitute throughout the verse?",
         "opts": [
             "'Sorrow' (socati) replaces 'delight' (nandati)",
             "'Wisdom' replaces 'delight'",
             "'Impermanence' replaces 'attachment'",
             "No word is changed; the verses are identical"],
         "correct": 0,
         "expl": "A single, precise substitution carries the entire reply."},
        {"q": "Does the Buddha's reply deny that children and cattle can be sources of feeling?",
         "opts": [
             "No &mdash; it claims the same attachments produce sorrow as readily as delight",
             "Yes, it denies children and cattle exist",
             "It claims children and cattle are illusions",
             "It claims only cattle, not children, cause any feeling"],
         "correct": 0,
         "expl": "The claim is about what attachment produces, not about denying the objects."},
        {"q": "What does 'upadhi' mean?",
         "opts": [
             "'Attachments' or 'substrates' &mdash; what is taken up and held onto",
             "'Wisdom'",
             "'A deity's name'",
             "'The flood'"],
         "correct": 0,
         "expl": "Named in both verses as the common cause of delight and sorrow alike."},
        {"q": "What does 'nirūpadhī' describe?",
         "opts": [
             "One without attachments, who experiences neither delight nor sorrow of this kind",
             "One who has lost everything through misfortune",
             "A type of deity",
             "A meditation posture"],
         "correct": 0,
         "expl": "The condition both verses agree is free of both delight and sorrow."},
        {"q": "What root does 'nandati' share with a discourse earlier in this vagga?",
         "opts": [
             "It shares its root with 'Nandana,' the garden of SN 1.11",
             "It shares its root with 'ogha,' the flood of SN 1.1",
             "It shares no root with any earlier discourse",
             "It shares its root with 'lokāmisa'"],
         "correct": 0,
         "expl": "The same root word applied to a heavenly garden, then to ordinary family life."},
        {"q": "Does this discourse claim that having a family is wrong?",
         "opts": [
             "No &mdash; it claims that whatever is held onto as attachment produces sorrow along with delight",
             "Yes, it explicitly condemns having children",
             "It claims cattle-ownership is the only problem",
             "It makes no claim about family at all"],
         "correct": 0,
         "expl": "A diagnosis of attachment's double effect, not a condemnation of family itself."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the recurring frame, resumed after SN 1.11's exception",
             "In the heavenly Garden of Delight itself",
             "No setting is given",
             "Near Rājagaha"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's standard frame, after SN 1.11's narrated departure from it."},
        {"q": "How closely does the Buddha's verse structurally match the deity's?",
         "opts": [
             "It repeats the exact grammatical structure, changing only the central verb",
             "It shares no structural similarity at all",
             "It is written in prose rather than verse",
             "It only partially echoes the deity's wording"],
         "correct": 0,
         "expl": "A near-mechanical substitution across an otherwise identical verse."},
        {"q": "What condition does the deity's own verse already name as free of delight?",
         "opts": [
             "'Yo nirūpadhī' &mdash; one without attachments",
             "One who has many cattle",
             "One who has many children",
             "The deities of the Thirty-Three"],
         "correct": 0,
         "expl": "Already present in the deity's own verse, before the Buddha's reply reuses it."},
    ],
    marginalia=[
        ("One word, changed", [
            "nandati &mdash; socati;",
            "delight becomes sorrow",
        ]),
        ("Upadhi, the common cause", [
            "children, cattle, attachment &mdash;",
            "source of both feelings",
        ]),
        ("A root shared with Nandana", [
            "the same delight, named",
            "in heaven and at home",
        ]),
        ("Not a verdict on family", [
            "not condemned, but diagnosed:",
            "what is held brings both",
        ]),
    ],
    further=[
        '<a href="%s/sn1.12/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.11.html">SN 1.11 &middot; The Garden of Delight</a> &mdash; the '
        "discourse immediately before this one, and this vagga&rsquo;s namesake.",
        '<a href="sn-1.9.html">SN 1.9 &middot; Fond of Conceit</a> &mdash; further back, in '
        "the previous vagga.",
        "SN 1.13 &middot; There's Nothing Like a Child &mdash; the next discourse, "
        "reframing a similar list of worldly values toward their inward analogues.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.13 — Natthiputtasamasutta
# --------------------------------------------------------------------------- #
page(
    1, 13, "Natthiputtasama", "There's Nothing Like a Child",
    meta_title="SN 1.13 — There's Nothing Like a Child | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Natthiputtasamasutta — a deity's list of unmatched worldly values, and the "
        "Buddha's reply substituting each one for its inward counterpart. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the recurring frame"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse naming four unmatched worldly values, answered by a "
                 "four-line verse substituting an inward value for each"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form; the "
                       "pattern of substitution is easy to follow once named"),
        ("A different move from SN 1.12", "Where SN 1.12 turned delight into sorrow, this "
                                          "discourse redirects each value toward an inward "
                                          "counterpart rather than negating it"),
    ],
    why=(
        "The deity's verse names four things each said to be unmatched: no fondness "
        "equals that for a child, no wealth equals cattle, no light equals the sun's, and "
        "of lakes the ocean is paramount. The Buddha's reply keeps the verse's exact "
        "structure &mdash; four unmatched superlatives &mdash; but replaces each external "
        "object with an inward or more ordinary one: fondness for oneself, wealth in "
        "grain, the light of wisdom, and the paramount waters of rain rather than the "
        "ocean."),
    guide=[
        ("A structure of four superlatives, kept intact", [
            "Both verses share an identical shape: four claims that nothing else equals a "
            "named thing. The Buddha's reply does not argue with the shape or the logic of "
            "superlatives &mdash; it argues with which four things deserve to occupy that "
            "position."]),
        ("From family and cattle to self and grain", [
            "Fondness for a child becomes fondness for oneself (<em>atta</em>); wealth "
            "equal to cattle becomes wealth equal to grain (<em>dhañña</em>) &mdash; a shift "
            "from livestock, a form of wealth tied to social display, to grain, a form of "
            "wealth tied to sustenance. Neither substitution rejects the original value "
            "outright; each redirects the same superlative claim toward something more "
            "basic or more inward."]),
        ("From sun and ocean to wisdom and rain", [
            "The verse's second pair moves in the same direction: the sun's light "
            "(<em>sūriyasamā ābhā</em>) becomes wisdom's light (<em>paññāsamā ābhā</em>), "
            "and the ocean, paramount among standing waters, becomes rain, paramount among "
            "falling waters. The image shifts from what is vast and visible to what is "
            "immediate and, in the case of wisdom, invisible."]),
        ("A different move from the discourse before it", [
            "SN 1.12, immediately before this discourse, turned an entire verse against "
            "itself by substituting its central verb (delight becomes sorrow). This "
            "discourse does something structurally different: it keeps every claim "
            "affirmative, and simply names four different, more inward objects worthy of "
            "the same superlative. Both discourses use exact structural repetition, but "
            "toward opposite rhetorical ends &mdash; negation in one case, redirection in "
            "the other."]),
    ],
    terms=[
        ("natthi puttasamaṁ pemaṁ",
         "&ldquo;there's no fondness like that for a child&rdquo; &mdash; the deity's "
         "opening claim, and this discourse's title."),
        ("natthi attasamaṁ pemaṁ",
         "&ldquo;there's no fondness like that for oneself&rdquo; &mdash; the Buddha's "
         "reply, substituting <em>atta</em> (oneself) for <em>putta</em> (a child)."),
        ("dhañña",
         "&ldquo;grain&rdquo; &mdash; the Buddha's substitute for cattle as the paramount "
         "form of wealth, shifting the image from livestock to sustenance."),
        ("paññāsamā ābhā",
         "&ldquo;a light like that of wisdom&rdquo; &mdash; replacing the sun as the "
         "paramount light, moving from a visible to an invisible source of clarity."),
        ("vuṭṭhi ve paramā sarā",
         "&ldquo;of waters, rain is paramount&rdquo; &mdash; replacing the ocean, shifting "
         "the image from the vast and standing to the immediate and falling."),
    ],
    text_intro=(
        "The discourse in full: four unmatched worldly values, answered by four inward or "
        "more basic counterparts. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.13:1.1-1.2"),
        ("p", "&sect;2", "sn1.13:2.1-2.4"),
        ("p", "&sect;3", "sn1.13:3.1-3.4"),
    ],
    quiz=[
        {"q": "What four things does the deity's verse claim are unmatched?",
         "opts": [
             "Fondness for a child, wealth in cattle, the sun's light, and the ocean among lakes",
             "Wisdom, grain, rain, and oneself",
             "The five faculties",
             "The four noble truths"],
         "correct": 0,
         "expl": "Four external superlatives naming the deity's opening claim."},
        {"q": "What does the Buddha's reply substitute for 'fondness for a child'?",
         "opts": [
             "Fondness for oneself (atta)",
             "Fondness for wisdom",
             "Fondness for cattle",
             "No substitution is made"],
         "correct": 0,
         "expl": "Natthi attasamaṁ pemaṁ &mdash; the first of four inward substitutions."},
        {"q": "What replaces cattle as the paramount form of wealth in the Buddha's reply?",
         "opts": [
             "Grain (dhañña)",
             "Gold",
             "Land",
             "Nothing; wealth is denied entirely"],
         "correct": 0,
         "expl": "A shift from livestock to sustenance."},
        {"q": "What replaces the sun as the paramount light?",
         "opts": [
             "Wisdom (paññā)",
             "The moon",
             "Fire",
             "A deity's radiance"],
         "correct": 0,
         "expl": "Paññāsamā ābhā &mdash; from a visible to an invisible source of clarity."},
        {"q": "What replaces the ocean as paramount among waters?",
         "opts": [
             "Rain",
             "A river",
             "A well",
             "Nothing; water is denied entirely"],
         "correct": 0,
         "expl": "A shift from the vast and standing to the immediate and falling."},
        {"q": "Does the Buddha's reply keep the same four-superlative structure as the deity's verse?",
         "opts": [
             "Yes &mdash; only the four named objects change, not the structure itself",
             "No, it abandons the superlative structure entirely",
             "It reduces the four claims to only one",
             "It adds several new claims not present in the original"],
         "correct": 0,
         "expl": "An identical shape, redirected toward different objects."},
        {"q": "How does this discourse's rhetorical move differ from SN 1.12's?",
         "opts": [
             "SN 1.12 negated its verse by substituting a verb; this discourse redirects, keeping every claim affirmative",
             "Both discourses use exactly the same technique",
             "This discourse negates its verse; SN 1.12 redirects",
             "Neither discourse involves any substitution"],
         "correct": 0,
         "expl": "Two different uses of the same technique of structural repetition."},
        {"q": "Does the Buddha's reply reject fondness for a child as valueless?",
         "opts": [
             "No &mdash; it redirects the same superlative claim toward oneself, without denouncing the original",
             "Yes, it explicitly condemns fondness for children",
             "It claims children do not exist",
             "It claims only fondness for cattle is valueless"],
         "correct": 0,
         "expl": "A redirection of the claim's object, not an outright negation."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the recurring frame",
             "In the heavenly Garden of Delight",
             "Near Rājagaha",
             "No setting is given"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's standard frame."},
        {"q": "What does 'dhañña' mean?",
         "opts": [
             "'Grain'",
             "'Cattle'",
             "'Wisdom'",
             "'The ocean'"],
         "correct": 0,
         "expl": "The Buddha's substitute for cattle as the paramount wealth."},
    ],
    marginalia=[
        ("Four claims, kept", [
            "no fondness like&hellip;,",
            "no wealth equal to&hellip;",
        ]),
        ("Child, cattle, sun, ocean", [
            "the deity&rsquo;s four,",
            "external and visible",
        ]),
        ("Self, grain, wisdom, rain", [
            "the Buddha&rsquo;s four,",
            "inward and immediate",
        ]),
        ("Redirection, not negation", [
            "unlike SN 1.12&rsquo;s reversal,",
            "every claim stays affirmative",
        ]),
    ],
    further=[
        '<a href="%s/sn1.13/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.12.html">SN 1.12 &middot; Delight</a> &mdash; the discourse '
        "immediately before this one, using the same technique toward a different end.",
        '<a href="sn-1.11.html">SN 1.11 &middot; The Garden of Delight</a> &mdash; this '
        "vagga&rsquo;s opening discourse.",
        "SN 1.14 &middot; Aristocrats &mdash; the next discourse, another four-part list of "
        "worldly bests, answered by four spiritual counterparts.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.14 — Khattiyasutta
# --------------------------------------------------------------------------- #
page(
    1, 14, "Khattiya", "Aristocrats",
    meta_title="SN 1.14 — Aristocrats | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Khattiyasutta — "
        "a verse naming the best of bipeds, quadrupeds, wives, and sons by social rank, "
        "answered by a verse naming the best of each by spiritual quality. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring Sāvatthī frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly in the source; by the pattern of the surrounding "
                    "discourses, a deity's claim answered by the Buddha"),
        ("Form", "A four-line verse naming four social 'bests,' answered by a four-line "
                 "verse naming four bests by different criteria"),
        ("Length", "~45 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form"),
        ("A shift in this vagga", "This is the first discourse in this vagga to drop the "
                                  "narrative frame entirely &mdash; no setting, no "
                                  "'standing to one side,' just the two verses themselves"),
    ],
    why=(
        "The opening verse ranks four categories by social or physical criteria: an "
        "aristocrat (<em>khattiya</em>) is the best of two-legged beings, an ox the best "
        "of four-legged ones, a maiden the best of wives, and a firstborn the best of "
        "sons. The answering verse keeps every category but replaces the ranking "
        "criterion in each: a Buddha, not a ruler by birth, is the best of two-legged "
        "beings; a thoroughbred, not simply an ox, is best among quadrupeds; a good "
        "listener, not a maiden, is the best wife; and a loyal son, not merely a "
        "firstborn, is the best son."),
    guide=[
        ("Rank by birth, replaced by rank by quality", [
            "The opening verse's criteria are all matters of birth order or social "
            "category: aristocratic birth, being firstborn, being unmarried. The reply "
            "keeps the same four categories &mdash; bipeds, quadrupeds, wives, sons "
            "&mdash; but replaces each criterion with a demonstrated quality: spiritual "
            "attainment, breeding for capability, attentiveness, and loyalty."]),
        ("A Buddha displaces an aristocrat", [
            "The most pointed substitution is the first: <em>khattiya</em>, the warrior-"
            "aristocrat caste this discourse is titled after, is displaced by "
            "<em>sambuddha</em>, &lsquo;the awakened one.&rsquo; Social rank, however "
            "elevated, is not what this verse treats as the true measure of "
            "&lsquo;the best of bipeds.&rsquo;"]),
        ("A discourse without any frame", [
            "Every discourse before this one in the Devatāsaṃyutta, however brief, "
            "identifies at least a setting or a speaker. This is the first to offer "
            "neither &mdash; simply two four-line verses, presented back to back. Several "
            "discourses following this one in the same vagga share this same bare "
            "presentation."]),
        ("A pair of lists, not an argument", [
            "Unlike SN 1.12's reversal or SN 1.13's redirection toward inward qualities, "
            "this pair simply substitutes a different criterion for ranking within the "
            "same social categories &mdash; wife, son, biped, quadruped &mdash; without "
            "questioning whether ranking itself, or these categories, are the right way "
            "to measure value."]),
    ],
    terms=[
        ("khattiya",
         "the warrior-aristocrat caste, named here as &ldquo;best of bipeds&rdquo; by "
         "birth in the opening verse, and this discourse's title."),
        ("sambuddha",
         "&ldquo;the awakened one&rdquo; &mdash; the reply's substitute for "
         "<em>khattiya</em> as the true best of two-legged beings."),
        ("ājānīya",
         "&ldquo;thoroughbred&rdquo; &mdash; a horse bred and trained for capability, "
         "replacing a plain ox as the best of four-legged beings."),
        ("sussūsā",
         "&ldquo;a good listener,&rdquo; one who attends and heeds &mdash; the reply's "
         "criterion for the best wife, replacing simple youth (<em>komārī</em>, "
         "&ldquo;a maiden&rdquo;)."),
        ("puttānamassavo",
         "&ldquo;an obedient, loyal son&rdquo; &mdash; the reply's criterion for the best "
         "son, replacing mere birth order (<em>pubbajo</em>, &ldquo;firstborn&rdquo;)."),
    ],
    text_intro=(
        "The discourse in full: four social 'bests' by birth, answered by four 'bests' by "
        "demonstrated quality. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.14:1.1-1.4"),
        ("p", "&sect;2", "sn1.14:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does the opening verse name as 'the best of bipeds'?",
         "opts": [
             "An aristocrat (khattiya), by birth",
             "A Buddha",
             "A good listener",
             "A loyal son"],
         "correct": 0,
         "expl": "Khattiyo dvipadaṁ seṭṭho &mdash; ranked by caste and birth."},
        {"q": "What does the answering verse substitute for 'aristocrat' as the best of bipeds?",
         "opts": [
             "Sambuddha, 'the awakened one'",
             "A king",
             "A wealthy merchant",
             "No substitution is made"],
         "correct": 0,
         "expl": "The most pointed substitution in the discourse."},
        {"q": "What does the reply name as the best of quadrupeds, replacing a plain ox?",
         "opts": [
             "A thoroughbred (ājānīya), bred for capability",
             "An elephant",
             "A water buffalo",
             "No quadruped is named"],
         "correct": 0,
         "expl": "A shift from a generic ox to a horse specifically bred and trained."},
        {"q": "What criterion does the reply use for 'the best wife,' replacing being a maiden?",
         "opts": [
             "Being a good listener (sussūsā), one who attends and heeds",
             "Being wealthy",
             "Being firstborn",
             "Being from an aristocratic family"],
         "correct": 0,
         "expl": "A demonstrated quality, not youth or unmarried status."},
        {"q": "What criterion does the reply use for 'the best son,' replacing being firstborn?",
         "opts": [
             "Being loyal and obedient (puttānamassavo)",
             "Being the tallest",
             "Being the wealthiest",
             "Being born to an aristocrat"],
         "correct": 0,
         "expl": "A demonstrated quality, not birth order."},
        {"q": "What structural shift marks this discourse within its vagga?",
         "opts": [
             "It is the first discourse in this vagga to drop all narrative frame entirely",
             "It is the only discourse with a long prose narration",
             "It introduces an entirely new setting, Rājagaha",
             "It is spoken by three deities instead of two"],
         "correct": 0,
         "expl": "No setting, no speaker introduction &mdash; just the two verses."},
        {"q": "Does this discourse question whether ranking by 'best' is itself the right approach?",
         "opts": [
             "No &mdash; it substitutes different criteria within the same categories and ranking structure",
             "Yes, it rejects all ranking outright",
             "It claims all four categories are equally worthless",
             "It claims ranking should be abolished entirely"],
         "correct": 0,
         "expl": "A substitution of criteria, not a challenge to the structure of ranking itself."},
        {"q": "What does 'ājānīya' mean?",
         "opts": [
             "'Thoroughbred' &mdash; bred and trained for capability",
             "'Aristocrat'",
             "'A good listener'",
             "'Firstborn'"],
         "correct": 0,
         "expl": "The reply's substitute for a plain ox as best of quadrupeds."},
        {"q": "How many categories does each verse rank?",
         "opts": [
             "Four: bipeds, quadrupeds, wives, and sons",
             "Two",
             "Six",
             "Eight"],
         "correct": 0,
         "expl": "The same four categories persist across both verses; only the criteria change."},
        {"q": "Is a speaker explicitly named for either verse in the source text?",
         "opts": [
             "No &mdash; unlike earlier discourses in this collection, no speaker is identified",
             "Yes, both are attributed by name",
             "Only the first verse's speaker is named",
             "Only the second verse's speaker is named"],
         "correct": 0,
         "expl": "This discourse offers no narrative frame at all."},
    ],
    marginalia=[
        ("Best, by birth", [
            "aristocrat, ox,",
            "maiden, firstborn",
        ]),
        ("Best, by quality", [
            "the awakened one, a thoroughbred,",
            "a listener, a loyal son",
        ]),
        ("No frame at all", [
            "the first bare pair of verses",
            "in this vagga",
        ]),
        ("A substitution, not a challenge", [
            "the categories stay,",
            "only the criteria change",
        ]),
    ],
    further=[
        '<a href="%s/sn1.14/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.13.html">SN 1.13 &middot; There’s Nothing Like a Child</a> '
        "&mdash; the discourse immediately before this one, using a related substitution "
        "technique.",
        '<a href="sn-1.11.html">SN 1.11 &middot; The Garden of Delight</a> &mdash; this '
        "vagga&rsquo;s opening discourse.",
        "SN 1.15 &middot; Whispering &mdash; the next discourse, the shortest pair yet, "
        "differing in only a single word.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.15 — Saṇamānasutta
# --------------------------------------------------------------------------- #
page(
    1, 15, "Saṇamāna", "Whispering",
    meta_title="SN 1.15 — Whispering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṇamānasutta — "
        "two nearly identical verses on the sound of a great forest at noon, one finding "
        "it frightening, the other finding it delightful. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; by the pattern of the surrounding discourses, "
                    "two contrasting perspectives, presumably a deity's and the Buddha's"),
        ("Form", "Two nearly identical four-line verses, differing in only their final "
                 "word"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest and "
                       "simplest discourse in this vagga so far"),
        ("A minimal pair", "The two verses in this discourse are identical for three full "
                           "lines, differing only in their closing word"),
    ],
    why=(
        "Both verses describe the exact same scene: the still of high noon, birds "
        "settled and quiet, and the mighty forest itself somehow still resounding. The "
        "first speaker finds this &lsquo;so scary&rsquo; (<em>bhaya</em>); the second, "
        "describing the identical scene in identical words, finds it &lsquo;so "
        "delightful&rsquo; (<em>rati</em>). Nothing about the forest or the moment "
        "changes between the two verses &mdash; only the word naming what it strikes the "
        "hearer as."),
    guide=[
        ("The same scene, twice", [
            "Three of this discourse's four lines are word-for-word identical between "
            "the two verses: the same stillness, the same settled birds, the same "
            "resounding forest. This is the closest textual pairing anywhere in this "
            "vagga so far &mdash; not a shared refrain or a shared structure, but the "
            "same sentence repeated with a single word swapped."]),
        ("Bhaya and rati, fear and delight", [
            "The entire difference between the two verses sits in one word: "
            "<em>bhaya</em>, &lsquo;fear,&rsquo; against <em>rati</em>, "
            "&lsquo;delight.&rsquo; Nothing in the description that precedes either word "
            "explains why one observer is frightened and the other pleased &mdash; the "
            "verse offers no argument, only the bare contrast itself."]),
        ("A silence about which reaction is correct", [
            "Unlike SN 1.12 or SN 1.13, this discourse gives no indication that one "
            "response corrects or supersedes the other. Both verses are simply set side "
            "by side, describing the identical noon-time forest, without resolution into "
            "a single 'right' reaction to solitude and its natural sounds."]),
        ("Read against the wilderness discourses before it", [
            "This vagga's predecessor, SN 1.9 in the Naḷavagga, and this same collection's "
            "SN 1.10 both treated the wilderness as a place whose value depends on the "
            "diligence of the one dwelling there. This discourse adds a further layer: "
            "even the plain sensory experience of a wilderness at noon &mdash; before any "
            "question of diligence &mdash; can register as either threat or delight."]),
    ],
    terms=[
        ("majjhanhika",
         "&ldquo;high noon&rdquo; &mdash; the specific time of day both verses describe, "
         "when the heat stills the forest's usual movement."),
        ("sannisīvesu pakkhisu",
         "&ldquo;when the birds have settled down&rdquo; &mdash; the shared description of "
         "silence that both verses open with."),
        ("saṇateva brahāraññaṁ",
         "&ldquo;the mighty forest itself resounds&rdquo; &mdash; the paradox both verses "
         "name, that even a supposedly still forest is not silent."),
        ("bhaya",
         "&ldquo;fear, danger&rdquo; &mdash; the word that closes the first verse, naming "
         "the scene as frightening."),
        ("rati",
         "&ldquo;delight, pleasure&rdquo; &mdash; the word that closes the second verse, "
         "naming the identical scene as pleasing."),
    ],
    text_intro=(
        "The discourse in full: the same scene described twice, differing only in its "
        "final word. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.15:1.1-1.4"),
        ("p", "&sect;2", "sn1.15:2.1-2.4"),
    ],
    quiz=[
        {"q": "What scene do both verses in this discourse describe?",
         "opts": [
             "The stillness of high noon, with birds settled and the forest resounding",
             "A river flooding its banks",
             "A deity descending from heaven",
             "A crowded marketplace"],
         "correct": 0,
         "expl": "The identical scene, shared word for word across both verses."},
        {"q": "How much of the two verses is identical, word for word?",
         "opts": [
             "Three of the four lines in each verse",
             "None of the lines are shared",
             "Only the first word",
             "All four lines, with no difference at all"],
         "correct": 0,
         "expl": "The closest textual pairing in this vagga so far &mdash; one word differs."},
        {"q": "What single word differs between the two verses?",
         "opts": [
             "'Fear' (bhaya) versus 'delight' (rati)",
             "'Forest' versus 'ocean'",
             "'Noon' versus 'midnight'",
             "'Birds' versus 'deities'"],
         "correct": 0,
         "expl": "The entire contrast rests on this single closing word."},
        {"q": "Does the discourse explain why one observer is frightened and the other pleased?",
         "opts": [
             "No &mdash; it offers no argument, only the bare contrast between the two words",
             "Yes, it gives a detailed explanation",
             "It claims the frightened observer is simply mistaken",
             "It claims the delighted observer is simply mistaken"],
         "correct": 0,
         "expl": "The verse presents the contrast without resolving it."},
        {"q": "Does this discourse indicate that one reaction is correct and the other is not?",
         "opts": [
             "No &mdash; unlike SN 1.12 or SN 1.13, both verses are simply set side by side",
             "Yes, the second verse explicitly corrects the first",
             "Yes, the first verse explicitly corrects the second",
             "The discourse states both reactions are equally wrong"],
         "correct": 0,
         "expl": "No resolution into a single 'right' response is given."},
        {"q": "What does 'saṇateva brahāraññaṁ' name?",
         "opts": [
             "The paradox that even a supposedly still forest is not silent",
             "A type of deity",
             "A meditation technique",
             "A specific monastery"],
         "correct": 0,
         "expl": "'The mighty forest itself resounds' &mdash; shared by both verses."},
        {"q": "How does this discourse relate to the wilderness theme of SN 1.9 and SN 1.10?",
         "opts": [
             "It adds a layer beyond diligence: even the plain sensory experience of the wilderness can register as threat or delight",
             "It contradicts everything said about the wilderness in SN 1.9 and SN 1.10",
             "It has no relation to those discourses at all",
             "It claims the wilderness described there was different from this one"],
         "correct": 0,
         "expl": "A further dimension to this collection's recurring wilderness theme."},
        {"q": "What time of day do both verses specify?",
         "opts": [
             "High noon (majjhanhika)",
             "Dawn",
             "Midnight",
             "Dusk"],
         "correct": 0,
         "expl": "The specific stillness of midday heat."},
        {"q": "What is the length and difficulty of this discourse, relative to others in this vagga?",
         "opts": [
             "The shortest and simplest discourse in this vagga so far",
             "The longest discourse in the entire Devatāsaṃyutta",
             "Roughly the same length as SN 1.20",
             "Longer than SN 1.11 but shorter than SN 1.14"],
         "correct": 0,
         "expl": "Two nearly identical four-line verses, minimal in length."},
        {"q": "What does 'rati' mean?",
         "opts": [
             "'Delight, pleasure'",
             "'Fear, danger'",
             "'Silence'",
             "'A type of bird'"],
         "correct": 0,
         "expl": "The word closing the second verse, naming the identical scene as pleasing."},
    ],
    marginalia=[
        ("One scene, twice", [
            "high noon, birds settled,",
            "the forest still resounds",
        ]),
        ("One word, changed", [
            "bhaya &mdash; rati;",
            "fear, or delight",
        ]),
        ("No verdict given", [
            "both stand, unresolved,",
            "side by side",
        ]),
        ("A further wilderness layer", [
            "beyond diligence &mdash;",
            "even the senses divide",
        ]),
    ],
    further=[
        '<a href="%s/sn1.15/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.14.html">SN 1.14 &middot; Aristocrats</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.9.html">SN 1.9 &middot; Fond of Conceit</a> &mdash; this '
        "collection&rsquo;s earlier discourse on solitary wilderness practice.",
        "SN 1.16 &middot; Sleepiness and Sloth &mdash; the next discourse, a matched pair "
        "on obstacles to the noble path.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.16 — Niddātandīsutta
# --------------------------------------------------------------------------- #
page(
    1, 16, "Niddātandī", "Sleepiness and Sloth",
    meta_title="SN 1.16 — Sleepiness and Sloth | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Niddātandīsutta "
        "— a verse naming five obstacles that keep the noble path from shining, answered "
        "by a verse on overcoming them through energy. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; by the pattern of the surrounding discourses, "
                    "a problem stated, then its solution given"),
        ("Form", "A four-line verse naming five obstacles, answered by a four-line verse "
                 "naming their remedy"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a compact list of five "
                       "named hindrances, worth reading slowly"),
        ("A problem-and-remedy pair", "Unlike several nearby discourses, this pair is not "
                                      "opposed positions but a single diagnosis answered by "
                                      "its own solution"),
    ],
    why=(
        "The first verse names five specific obstacles: sleepiness, sloth, yawning, "
        "discontent, and grogginess after eating. Because of these, it says, the noble "
        "path does not shine for beings here. The second verse names the identical five "
        "obstacles in the identical order, but changes what happens to them: when they "
        "are energetically fended off, the noble path is purified. This is not a dispute "
        "between two positions, as several nearby discourses are, but a diagnosis "
        "immediately followed by its own remedy."),
    guide=[
        ("Five obstacles, named together", [
            "<em>Niddā</em> (sleepiness), <em>tandī</em> (sloth), <em>vijambhitā</em> "
            "(yawning), <em>arati</em> (discontent), and <em>bhattasammada</em> "
            "(grogginess after eating) are listed as a single cluster, all physical or "
            "near-physical states rather than views or emotions in the usual sense. This "
            "same list, in the same order, recurs unchanged in the second verse."]),
        ("The same five, energetically fended off", [
            "The verse's turn happens entirely in its third line: where the first verse "
            "says these obstacles keep the noble path from shining, the second says that "
            "when they are &lsquo;energetically fended off&rsquo; (<em>vīriyena "
            "paṇāmetvā</em>), the noble path is purified. The obstacles themselves are "
            "not denied or reinterpreted &mdash; only their outcome, contingent on "
            "energy, changes."]),
        ("A structure of diagnosis and remedy", [
            "Several discourses earlier in this vagga (SN 1.12, SN 1.13, SN 1.15) present "
            "two differing perspectives on the same subject, left standing side by side. "
            "This discourse instead presents one problem and its resolution in sequence "
            "&mdash; closer to a teaching than to a debate."]),
        ("A physical, not merely mental, obstacle list", [
            "Read alongside SN 1.6's riddle on 'gathering dust' and 'being cleansed,' "
            "this discourse's five named obstacles read as a more concrete, physically "
            "grounded version of the same basic contrast between dullness and clarity "
            "&mdash; naming specific bodily and appetitive states rather than a "
            "generalized dust."]),
    ],
    terms=[
        ("niddā",
         "&ldquo;sleepiness&rdquo; &mdash; the first of five obstacles named in this "
         "discourse's opening verse, and half of its title."),
        ("tandī",
         "&ldquo;sloth, sluggishness&rdquo; &mdash; the second obstacle, and the other "
         "half of this discourse's title."),
        ("arati",
         "&ldquo;discontent&rdquo; &mdash; the fourth named obstacle, a restless "
         "dissatisfaction distinct from simple drowsiness."),
        ("bhattasammada",
         "&ldquo;grogginess after eating&rdquo; &mdash; the fifth obstacle, naming a "
         "specific and ordinary bodily state as an obstacle to the path."),
        ("vīriyena paṇāmetvā",
         "&ldquo;energetically fended off&rdquo; &mdash; the remedy named in the second "
         "verse, the sole change between the two verses' otherwise identical lists."),
    ],
    text_intro=(
        "The discourse in full: five named obstacles, then the same five overcome by "
        "energy. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.16:1.1-1.4"),
        ("p", "&sect;2", "sn1.16:2.1-2.4"),
    ],
    quiz=[
        {"q": "What five obstacles does the opening verse name?",
         "opts": [
             "Sleepiness, sloth, yawning, discontent, and grogginess after eating",
             "Greed, hatred, delusion, conceit, and views",
             "The five aggregates",
             "The five faculties"],
         "correct": 0,
         "expl": "A cluster of physical and near-physical hindrances, named together."},
        {"q": "What does the first verse say these obstacles do to the noble path?",
         "opts": [
             "They keep it from shining for beings here",
             "They have no effect on it at all",
             "They immediately destroy it permanently",
             "They only affect deities, not humans"],
         "correct": 0,
         "expl": "'Ariyamaggo idha na pakāsati' &mdash; the path does not shine."},
        {"q": "What changes between the first verse and the second?",
         "opts": [
             "The same five obstacles are named, but the outcome changes when they are energetically fended off",
             "An entirely new list of obstacles is given",
             "The number of obstacles is reduced from five to three",
             "Nothing changes; the verses are identical"],
         "correct": 0,
         "expl": "The turn happens in the verse's third line: vīriyena paṇāmetvā."},
        {"q": "What does 'vīriyena paṇāmetvā' mean?",
         "opts": [
             "'Energetically fended off'",
             "'Permanently forgotten'",
             "'Gradually accepted'",
             "'Never overcome'"],
         "correct": 0,
         "expl": "The remedy named for the same five obstacles in the second verse."},
        {"q": "How does this discourse's structure differ from SN 1.12, 1.13, and 1.15?",
         "opts": [
             "It presents one problem and its resolution in sequence, rather than two differing perspectives side by side",
             "It presents no problem or resolution at all",
             "It uses exactly the same structure as those three discourses",
             "It presents three perspectives instead of two"],
         "correct": 0,
         "expl": "Closer to a teaching than to a debate between positions."},
        {"q": "What does 'bhattasammada' name?",
         "opts": [
             "Grogginess after eating",
             "A type of meditation",
             "A deity's name",
             "A monastery near Sāvatthī"],
         "correct": 0,
         "expl": "A specific and ordinary bodily state, named as an obstacle."},
        {"q": "Are the obstacles denied or reinterpreted in the second verse?",
         "opts": [
             "No &mdash; they remain the same; only their outcome, contingent on energy, changes",
             "Yes, they are declared not to exist",
             "Yes, they are reinterpreted as virtues",
             "The second verse names entirely different obstacles"],
         "correct": 0,
         "expl": "The five obstacles persist unchanged; the response to them is what shifts."},
        {"q": "What does 'arati' mean?",
         "opts": [
             "'Discontent' &mdash; a restless dissatisfaction",
             "'Delight'",
             "'Sleepiness'",
             "'Wisdom'"],
         "correct": 0,
         "expl": "The fourth named obstacle in the list, distinct from simple drowsiness."},
        {"q": "What earlier discourse in this collection uses a related contrast between dullness and clarity?",
         "opts": [
             "SN 1.6, on gathering dust and being cleansed",
             "SN 1.1, on crossing the flood",
             "SN 1.11, on the Garden of Delight",
             "No earlier discourse shares this theme"],
         "correct": 0,
         "expl": "This discourse offers a more physically concrete version of a similar contrast."},
        {"q": "How many obstacles are named in this discourse's list?",
         "opts": [
             "Five",
             "Three",
             "Seven",
             "Ten"],
         "correct": 0,
         "expl": "Niddā, tandī, vijambhitā, arati, and bhattasammada."},
    ],
    marginalia=[
        ("Five named together", [
            "sleepiness, sloth, yawning,",
            "discontent, grogginess",
        ]),
        ("The path dimmed", [
            "because of this,",
            "it doesn&rsquo;t shine",
        ]),
        ("The same five, fended off", [
            "vīriyena paṇāmetvā &mdash;",
            "energetically overcome",
        ]),
        ("Diagnosis, then remedy", [
            "not two views opposed,",
            "but problem and solution",
        ]),
    ],
    further=[
        '<a href="%s/sn1.16/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.15.html">SN 1.15 &middot; Whispering</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.6.html">SN 1.6 &middot; Awake</a> &mdash; an earlier discourse on '
        "a related contrast between dullness and clarity.",
        "SN 1.17 &middot; Hard to Do &mdash; the next discourse, on the difficulty of "
        "ascetic life for one who has not tamed the mind.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.17 — Dukkarasutta
# --------------------------------------------------------------------------- #
page(
    1, 17, "Dukkara", "Hard to Do",
    meta_title="SN 1.17 — Hard to Do | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dukkarasutta — a "
        "verse on how hard the ascetic life is for the inept, answered by two verses on "
        "the mind's instability and the tortoise-shell image of collecting one's "
        "thoughts. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; by the pattern of the surrounding discourses, "
                    "a challenge answered at greater length than usual"),
        ("Form", "A four-line opening verse, answered by two four-line verses rather than "
                 "the usual one"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form, with a "
                       "memorable closing image"),
        ("A longer reply", "Like SN 1.10, this discourse's answer runs to two stanzas "
                           "rather than this vagga's usual one"),
    ],
    why=(
        "The opening verse states a plain difficulty: the ascetic life is hard to do and "
        "hard to endure for the inept, since it is full of narrow passes where a fool "
        "founders. The reply does not soften this claim &mdash; it sharpens it into a "
        "question (how many days could an ascetic even survive without controlling the "
        "mind, foundering with every step under the sway of thoughts) before answering "
        "with a concrete image: a mendicant should draw their thoughts in, the way a "
        "tortoise draws its limbs into its shell, becoming independent, undisturbing, and "
        "quenched."),
    guide=[
        ("A difficulty stated, then intensified", [
            "The opening verse's claim &mdash; that the ascetic life is hard for the "
            "inept &mdash; is not contradicted by the reply. Instead the reply's first "
            "stanza intensifies it into a rhetorical question: without control over the "
            "mind, how many days could such a person even manage, foundering with each "
            "step under the sway of their own thoughts?"]),
        ("The tortoise and its shell", [
            "The reply's second stanza turns from diagnosis to instruction, with this "
            "vagga's most concrete image so far: a mendicant should collect their "
            "thoughts the way a tortoise draws its limbs into its shell "
            "(<em>kummova aṅgāni sake kapāle</em>). The image is protective rather than "
            "aggressive &mdash; withdrawal for safety, not suppression by force."]),
        ("Independence without disturbance", [
            "The verse's closing lines describe the result of this withdrawal: "
            "independent (<em>anissito</em>), not disturbing others "
            "(<em>aññamaheṭhayāno</em>), quenched (<em>parinibbuto</em>), such a person "
            "&lsquo;wouldn't blame anyone&rsquo; &mdash; a state defined as much by its "
            "effect on others as by its inner content."]),
        ("Two stanzas, not one", [
            "Like SN 1.10, this vagga's Naḷavagga counterpart, this discourse's answer "
            "runs longer than the vagga's usual single four-line reply. Both discourses "
            "use the extra length to move from diagnosis to a fuller, image-based "
            "resolution rather than a single compressed claim."]),
    ],
    terms=[
        ("dukkaraṁ duttitikkhañca",
         "&ldquo;hard to do, hard to endure&rdquo; &mdash; the opening verse's description "
         "of the ascetic life, and this discourse's title."),
        ("abyattena",
         "&ldquo;for the inept, the unskilled&rdquo; &mdash; naming who specifically finds "
         "the ascetic life so difficult, not ascetic life as such."),
        ("saṅkappānaṁ vasānugo",
         "&ldquo;under the sway of thoughts&rdquo; &mdash; the condition the reply says "
         "would make even a single day of ascetic life unmanageable."),
        ("kummova aṅgāni sake kapāle",
         "&ldquo;like a tortoise draws its limbs into its own shell&rdquo; &mdash; this "
         "discourse's central image for gathering the thoughts in for protection."),
        ("parinibbuto",
         "&ldquo;quenched&rdquo; &mdash; the state the verse's closing lines describe, "
         "paired with independence and not disturbing others."),
    ],
    text_intro=(
        "The discourse in full: a stated difficulty, sharpened into a question, then "
        "answered with the image of a tortoise drawing in its limbs. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.17:1.1-1.4"),
        ("p", "&sect;2", "sn1.17:2.1-2.4"),
        ("p", "&sect;3", "sn1.17:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does the opening verse say about the ascetic life?",
         "opts": [
             "It is hard to do and hard to endure for the inept",
             "It is easy for anyone who tries",
             "It should never be attempted",
             "It has no particular difficulty at all"],
         "correct": 0,
         "expl": "Dukkaraṁ duttitikkhañca abyattena ca sāmaññaṁ."},
        {"q": "How does the reply's first stanza respond to this claim?",
         "opts": [
             "It intensifies it into a question about surviving even one day without controlling the mind",
             "It flatly denies the ascetic life is difficult",
             "It changes the subject entirely",
             "It claims only fools attempt ascetic life"],
         "correct": 0,
         "expl": "A rhetorical question sharpening, not softening, the original claim."},
        {"q": "What image does the reply's second stanza use for gathering one's thoughts?",
         "opts": [
             "A tortoise drawing its limbs into its own shell",
             "A bird building a nest",
             "A river cutting through stone",
             "A lamp being lit"],
         "correct": 0,
         "expl": "Kummova aṅgāni sake kapāle &mdash; this vagga's most concrete image so far."},
        {"q": "What does 'parinibbuto' mean?",
         "opts": [
             "'Quenched'",
             "'Frightened'",
             "'Foundering'",
             "'Aristocratic'"],
         "correct": 0,
         "expl": "The state described alongside independence and not disturbing others."},
        {"q": "Who specifically does the opening verse say finds the ascetic life difficult?",
         "opts": [
             "The inept, the unskilled (abyattena)",
             "Everyone without exception",
             "Only deities",
             "Only those who have never heard the teaching"],
         "correct": 0,
         "expl": "Abyattena &mdash; the difficulty is attributed to lack of skill, not to the practice itself."},
        {"q": "How many stanzas does this discourse's reply run to?",
         "opts": [
             "Two, rather than this vagga's usual one",
             "One, the vagga's usual length",
             "Four full stanzas",
             "No verse reply is given at all"],
         "correct": 0,
         "expl": "Like SN 1.10, an extended reply moving from diagnosis to image-based resolution."},
        {"q": "What does the tortoise image emphasize about gathering one's thoughts?",
         "opts": [
             "Protective withdrawal, not suppression by force",
             "Aggressive confrontation with the mind",
             "Complete abandonment of all thought forever",
             "A physical posture for sitting meditation"],
         "correct": 0,
         "expl": "The shell protects; it does not attack."},
        {"q": "What three qualities does the verse's closing line attribute to the one who gathers their thoughts this way?",
         "opts": [
             "Independent, not disturbing others, and quenched",
             "Wealthy, famous, and respected",
             "Fearful, isolated, and silent",
             "Young, strong, and swift"],
         "correct": 0,
         "expl": "Anissito, aññamaheṭhayāno, parinibbuto."},
        {"q": "What does 'saṅkappānaṁ vasānugo' describe?",
         "opts": [
             "Being under the sway of one's own thoughts",
             "Being free from all thought",
             "A type of deity",
             "A monastery's name"],
         "correct": 0,
         "expl": "The condition that would make even a single day of ascetic life unmanageable."},
        {"q": "Does this discourse resemble SN 1.10 in its structure?",
         "opts": [
             "Yes &mdash; both extend the reply to two stanzas instead of this vagga's usual one",
             "No, SN 1.10 has no reply at all",
             "No, this discourse's reply is shorter than usual",
             "The two discourses share no similarity"],
         "correct": 0,
         "expl": "Both use the extra length to move toward a fuller resolution."},
    ],
    marginalia=[
        ("A difficulty, named", [
            "hard to do, hard to endure &mdash;",
            "many narrow passes",
        ]),
        ("Sharpened into a question", [
            "how many days, unguarded,",
            "under thought&rsquo;s sway?",
        ]),
        ("The tortoise&rsquo;s shell", [
            "kummova aṅgāni &mdash;",
            "limbs drawn in for safety",
        ]),
        ("Independent, undisturbing", [
            "quenched, blaming no one &mdash;",
            "the verse&rsquo;s close",
        ]),
    ],
    further=[
        '<a href="%s/sn1.17/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.16.html">SN 1.16 &middot; Sleepiness and Sloth</a> &mdash; the '
        "discourse immediately before this one.",
        '<a href="sn-1.10.html">SN 1.10 &middot; Wilderness</a> &mdash; this '
        "collection&rsquo;s other two-stanza reply, closing the previous vagga.",
        "SN 1.18 &middot; Conscience &mdash; the next discourse, closing with a line shared "
        "word for word with SN 1.7 and SN 1.8, two vaggas back.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.18 — Hirīsutta
# --------------------------------------------------------------------------- #
page(
    1, 18, "Hirī", "Conscience",
    meta_title="SN 1.18 — Conscience | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Hirīsutta — a "
        "question asking whether anyone constrained by conscience can be found in the "
        "world, answered with a verse closing on a line shared word for word with SN 1.7 "
        "and SN 1.8. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; by the pattern of the surrounding discourses, "
                    "a question answered directly"),
        ("Form", "A four-line question, answered by a four-line verse"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form, though "
                       "its closing line rewards recognizing where else it appears"),
        ("A recurring formula", "This discourse's closing line, &lsquo;they walk smoothly "
                                "in the rough,&rsquo; is identical to the closing lines of "
                                "SN 1.7 and SN 1.8, in the previous vagga"),
    ],
    why=(
        "The question is direct: can a person constrained by conscience "
        "(<em>hirīnisedho</em>) be found in the world &mdash; someone cognizant of blame "
        "the way a fine horse responds to the whip? The reply does not answer with a "
        "simple yes or no. It says such people are few, but they exist: those constrained "
        "by conscience who live always mindful, having reached the end of suffering, "
        "&lsquo;walk smoothly in the rough&rsquo; &mdash; the exact closing image already "
        "used twice in the Naḷavagga, at SN 1.7 and SN 1.8."),
    guide=[
        ("A question, not a claim", [
            "Unlike most discourses in this vagga, this one opens with an actual question "
            "&mdash; whether anyone so responsive to blame that they resemble a "
            "whip-trained horse can be found at all &mdash; rather than a declarative "
            "verse to be agreed with or reversed."]),
        ("A qualified answer: few, but not none", [
            "The reply neither confirms the question's premise fully nor denies it. "
            "&lsquo;Few&rsquo; (<em>appakā</em>) are those constrained by conscience who "
            "live always mindful &mdash; an answer that takes the difficulty seriously "
            "without claiming such people cannot exist."]),
        ("A closing line shared with two other discourses", [
            "&lsquo;They walk smoothly in the rough&rsquo; (<em>caranti visame samaṁ</em>) "
            "closes this discourse exactly as it closed both SN 1.7 and SN 1.8, in the "
            "Naḷavagga, this collection's first vagga. This is the third time this exact "
            "line has appeared, and the first time it has crossed from one vagga into "
            "another &mdash; evidence that it functions as a stock closing formula across "
            "the whole Devatāsaṃyutta, not only within a single chapter."]),
        ("A horse trained by the whip", [
            "The opening question's image &mdash; a fine horse (<em>asso bhadro</em>) that "
            "responds to the whip without needing to be struck &mdash; treats conscience "
            "as something like trainability: the capacity to be corrected by the mere "
            "threat or awareness of blame, rather than only by its actual infliction."]),
    ],
    terms=[
        ("hirī",
         "&ldquo;conscience, moral shame&rdquo; &mdash; this discourse's title, and the "
         "quality its opening question asks whether anyone truly possesses."),
        ("hirīnisedho",
         "&ldquo;constrained, restrained by conscience&rdquo; &mdash; the specific quality "
         "described in both the question and the reply."),
        ("asso bhadro kasāmiva",
         "&ldquo;like a fine horse of the whip&rdquo; &mdash; the opening question's "
         "image, comparing responsiveness to blame with a well-trained horse's "
         "responsiveness to the whip."),
        ("appakā",
         "&ldquo;few&rdquo; &mdash; the reply's qualified answer, acknowledging rarity "
         "without denying existence."),
        ("caranti visame samaṁ",
         "&ldquo;they walk smoothly in the rough&rdquo; &mdash; this discourse's closing "
         "line, identical to the closing lines of SN 1.7 and SN 1.8 in the previous "
         "vagga."),
    ],
    text_intro=(
        "The discourse in full: a question about conscience, answered by a verse closing "
        "on a formula already met twice before. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.18:1.1-1.4"),
        ("p", "&sect;2", "sn1.18:2.1-2.4"),
    ],
    quiz=[
        {"q": "What question does the opening verse ask?",
         "opts": [
             "Whether a person constrained by conscience, cognizant of blame like a fine horse of the whip, can be found in the world",
             "Whether the flood can be crossed",
             "Whether deities exist",
             "Whether the ascetic life is worthwhile"],
         "correct": 0,
         "expl": "A direct question, not a declarative claim to be reversed or echoed."},
        {"q": "How does the reply answer this question?",
         "opts": [
             "It says such people are few, but does not deny they exist",
             "It says no such person can ever exist",
             "It refuses to answer at all",
             "It says every person is naturally constrained by conscience"],
         "correct": 0,
         "expl": "Appakā &mdash; a qualified answer, acknowledging rarity."},
        {"q": "What closing line does this discourse share with SN 1.7 and SN 1.8?",
         "opts": [
             "'They walk smoothly in the rough' (caranti visame samaṁ)",
             "'A seeker of peace would drop the world's bait'",
             "'Like a green reed mowed down'",
             "'Their settling is bliss'"],
         "correct": 0,
         "expl": "Identical wording, appearing for a third time in this collection."},
        {"q": "What is significant about this repetition, compared to its two earlier appearances?",
         "opts": [
             "It is the first time this exact line has crossed from one vagga into another",
             "It is the first time this line has ever appeared in this collection",
             "It contradicts its two earlier appearances",
             "It appears with different wording this time"],
         "correct": 0,
         "expl": "Evidence the line functions as a stock formula across the whole Devatāsaṃyutta."},
        {"q": "What image does the opening question use for responsiveness to blame?",
         "opts": [
             "A fine horse responding to the whip",
             "A tortoise withdrawing into its shell",
             "A green reed being mowed down",
             "A deity vanishing at dawn"],
         "correct": 0,
         "expl": "Asso bhadro kasāmiva &mdash; trainability through mere awareness, not only actual force."},
        {"q": "What does 'hirī' mean?",
         "opts": [
             "'Conscience, moral shame'",
             "'Wisdom'",
             "'The flood'",
             "'Delight'"],
         "correct": 0,
         "expl": "This discourse's title and central subject."},
        {"q": "According to the reply, what do those constrained by conscience live as?",
         "opts": [
             "Always mindful (sadā satā)",
             "Always fearful",
             "Always wealthy",
             "Always silent"],
         "correct": 0,
         "expl": "Ye caranti sadā satā &mdash; a description of sustained mindfulness."},
        {"q": "What have those described in the reply reached, according to the verse?",
         "opts": [
             "The end of suffering",
             "The highest heaven",
             "Great wealth",
             "Political power"],
         "correct": 0,
         "expl": "Antaṁ dukkhassa pappuyya &mdash; before the closing image of walking smoothly in the rough."},
        {"q": "In which two discourses did 'caranti visame samaṁ' previously appear?",
         "opts": [
             "SN 1.7 and SN 1.8, in the Naḷavagga",
             "SN 1.11 and SN 1.12, in this same vagga",
             "SN 1.1 and SN 1.2",
             "It has not appeared before this discourse"],
         "correct": 0,
         "expl": "This collection's first vagga, now echoed in its second."},
        {"q": "Does the opening question's image involve the horse being struck?",
         "opts": [
             "Not necessarily &mdash; the point is responsiveness to the whip's mere presence, not only its actual use",
             "Yes, the horse must always be struck to respond",
             "The image does not involve a horse at all",
             "The horse in the image never responds"],
         "correct": 0,
         "expl": "Trainability through awareness of the whip, paralleling conscience's function."},
    ],
    marginalia=[
        ("A question asked plainly", [
            "constrained by conscience &mdash;",
            "does such a person exist?",
        ]),
        ("Few, but not none", [
            "appakā &mdash;",
            "rare, not impossible",
        ]),
        ("A line, a third time", [
            "caranti visame samaṁ &mdash;",
            "shared with SN 1.7, 1.8",
        ]),
        ("A formula crossing vaggas", [
            "no longer confined",
            "to a single chapter",
        ]),
    ],
    further=[
        '<a href="%s/sn1.18/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.17.html">SN 1.17 &middot; Hard to Do</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.7.html">SN 1.7 &middot; Not Comprehending</a> &mdash; the first '
        "appearance of this discourse&rsquo;s closing line, in the previous vagga.",
        "SN 1.19 &middot; Little Hut &mdash; the next discourse, an allegorical riddle "
        "unpacking family bonds as a hut, a nest, a network, and a shackle.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.19 — Kuṭikāsutta
# --------------------------------------------------------------------------- #
page(
    1, 19, "Kuṭikā", "Little Hut",
    meta_title="SN 1.19 — Little Hut | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kuṭikāsutta — an "
        "allegorical riddle in which a deity asks about a little hut, a little nest, "
        "networks, and shackles, then learns these name mother, wife, children, and "
        "craving. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a five-verse riddle exchange, question, "
                     "answer, request for the code, its solution, and confirmation"),
        ("Form", "Five four-line verses: a riddling question, a literal reply, a request "
                 "to decode the riddle, its answer, and a closing confirmation"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the riddle's answer is "
                       "given directly in the text, but its implications reward slow "
                       "reading"),
        ("This vagga's longest exchange so far", "Five verses, more than any other "
                                                  "discourse in the Nandanavagga up to "
                                                  "this point"),
    ],
    why=(
        "A deity asks a series of pointed questions: don't you have a little hut, a "
        "little nest, any networks &mdash; aren't you free of shackles? The reply is a "
        "flat denial of all four, indeed I have none of these, I'm free from shackles. "
        "The deity then asks what these four images actually stand for, and the answer "
        "unpacks them precisely: mother is called a little hut, wife a little nest, "
        "children a network, and craving the shackle. The deity's closing verse affirms "
        "each denial as good &mdash; it's good you have none of these."),
    guide=[
        ("A riddle in code, then decoded", [
            "The discourse's structure is unusually explicit for this collection: rather "
            "than leaving an image to interpretation, the deity directly asks &lsquo;what "
            "do I call your little hut,&rsquo; and the reply directly supplies the "
            "answer. Few discourses in this vagga spell out their own symbolism this "
            "openly."]),
        ("Mother, wife, children, craving", [
            "The code, once given, is precise: a &lsquo;little hut&rsquo; "
            "(<em>kuṭikā</em>) names one's mother, a &lsquo;little nest&rsquo; "
            "(<em>kulāvaka</em>) names one's wife, a &lsquo;network&rsquo; "
            "(<em>santānaka</em>) names one's children, and a &lsquo;shackle&rsquo; "
            "(<em>bandhana</em>) names craving (<em>taṇhā</em>) itself &mdash; the only "
            "one of the four that is not a relationship but an inner state."]),
        ("Set against this vagga's earlier praise of family", [
            "SN 1.12 and SN 1.13, earlier in this vagga, both took children as at least "
            "an ambiguous source of feeling &mdash; delight, or fondness unmatched by "
            "anything else. This discourse's imagery is starker: mother, wife, and "
            "children are named outright as confinement, structurally paired with "
            "craving as their shared root."]),
        ("Confirmation without further argument", [
            "The deity's final verse does not add a new claim; it simply confirms each "
            "denial as good, one by one, in the same four-part structure the whole "
            "discourse has used throughout. The riddle having been solved, nothing "
            "further is offered by way of justification."]),
    ],
    terms=[
        ("kuṭikā",
         "&ldquo;little hut,&rdquo; this discourse's title and its code-word for one's "
         "mother &mdash; the first of four images to be decoded."),
        ("kulāvaka",
         "&ldquo;little nest&rdquo; &mdash; the code-word for one's wife, the second "
         "image."),
        ("santānaka",
         "&ldquo;network&rdquo; &mdash; the code-word for one's children, the third "
         "image."),
        ("bandhana",
         "&ldquo;shackle&rdquo; &mdash; the code-word for craving (<em>taṇhā</em>) "
         "itself, the only one of the four images naming an inner state rather than a "
         "relationship."),
        ("muttosi bandhanā",
         "&ldquo;you are free from the shackle&rdquo; &mdash; the reply's claim, "
         "confirmed as good in the deity's closing verse."),
    ],
    text_intro=(
        "The discourse in full: a four-part riddle, its literal answer, its decoding, and "
        "a closing confirmation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A riddle, asked directly"),
        ("p", "&sect;1", "sn1.19:1.1-2.4"),
        ("h3", "The code, requested and given"),
        ("p", "&sect;2", "sn1.19:3.1-4.4"),
        ("h3", "Confirmed as good"),
        ("p", "&sect;3", "sn1.19:5.1-5.4"),
    ],
    quiz=[
        {"q": "What four things does the deity's opening question ask about?",
         "opts": [
             "A little hut, a little nest, networks, and shackles",
             "A flood, a mountain, a garden, and a reed",
             "Wisdom, faith, energy, and mindfulness",
             "Aristocrats, oxen, wives, and sons"],
         "correct": 0,
         "expl": "Kuṭikā, kulāvaka, santānaka, bandhana &mdash; the riddle's four images."},
        {"q": "How does the reply answer the opening question?",
         "opts": [
             "With a flat denial of all four, and a claim of freedom from shackles",
             "By ignoring the question entirely",
             "By affirming all four are present",
             "By asking a counter-riddle"],
         "correct": 0,
         "expl": "Indeed I have no little hut, no little nest, no networks, and am free from shackles."},
        {"q": "What does the code, once given, reveal 'a little hut' to mean?",
         "opts": [
             "One's mother",
             "One's wife",
             "One's children",
             "Craving itself"],
         "correct": 0,
         "expl": "Māturaṁ kuṭikaṁ brūsi &mdash; the first image decoded."},
        {"q": "What does 'a little nest' name in the decoded answer?",
         "opts": [
             "One's wife",
             "One's mother",
             "One's children",
             "One's teacher"],
         "correct": 0,
         "expl": "Bhariyaṁ brūsi kulāvakaṁ."},
        {"q": "What does 'a network' name, and what does 'a shackle' name?",
         "opts": [
             "Children, and craving (taṇhā)",
             "Wealth, and fame",
             "Deities, and humans",
             "The flood, and the shore"],
         "correct": 0,
         "expl": "Putte santānake brūsi; taṇhaṁ me brūsi bandhanaṁ."},
        {"q": "Which of the four decoded images names an inner state rather than a relationship?",
         "opts": [
             "The shackle, naming craving",
             "The little hut, naming the mother",
             "The little nest, naming the wife",
             "The network, naming the children"],
         "correct": 0,
         "expl": "The only one of the four that is not a person or relationship."},
        {"q": "How does the deity's closing verse respond to the decoded answer?",
         "opts": [
             "It confirms each denial as good, one by one, without further argument",
             "It rejects the decoding as incorrect",
             "It asks yet another riddle",
             "It changes the subject to the Garden of Delight"],
         "correct": 0,
         "expl": "Sāhu te kuṭikā natthi&hellip; &mdash; affirmation without new justification."},
        {"q": "How does this discourse's treatment of family compare to SN 1.12 and SN 1.13, earlier in this vagga?",
         "opts": [
             "It is starker, naming mother, wife, and children outright as confinement",
             "It is identical in every respect",
             "It praises family more strongly than either earlier discourse",
             "It makes no mention of family at all"],
         "correct": 0,
         "expl": "A sharper framing than those two discourses' more ambiguous treatment."},
        {"q": "How many verses does this discourse's full exchange run to?",
         "opts": [
             "Five",
             "Two",
             "Eight",
             "One"],
         "correct": 0,
         "expl": "The longest exchange in this vagga up to this point."},
        {"q": "What is 'muttosi bandhanā'?",
         "opts": [
             "'You are free from the shackle' &mdash; the reply's claim, later confirmed as good",
             "'You are bound by the shackle'",
             "'A type of deity'",
             "'A monastery near Rājagaha'"],
         "correct": 0,
         "expl": "The reply's central claim, affirmed in the deity's closing verse."},
    ],
    marginalia=[
        ("A riddle in four parts", [
            "hut, nest, network, shackle &mdash;",
            "do you have these?",
        ]),
        ("None of them, claimed", [
            "indeed I have none,",
            "free from the shackle",
        ]),
        ("The code, given", [
            "mother, wife, children &mdash;",
            "and craving, the shackle",
        ]),
        ("Confirmed as good", [
            "sāhu, sāhu, sāhu &mdash;",
            "good that you are free",
        ]),
    ],
    further=[
        '<a href="%s/sn1.19/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.18.html">SN 1.18 &middot; Conscience</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.12.html">SN 1.12 &middot; Delight</a> &mdash; this vagga&rsquo;s '
        "earlier, more ambiguous treatment of children as a source of feeling.",
        "SN 1.20 &middot; With Samiddhi &mdash; the next discourse, this vagga's last, and "
        "its longest by far.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.20 — Samiddhisutta (closes the Nandanavagga)
# --------------------------------------------------------------------------- #
page(
    1, 20, "Samiddhi", "With Samiddhi",
    meta_title="SN 1.20 — With Samiddhi | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samiddhisutta — "
        "a deity urges Venerable Samiddhi to enjoy sensual pleasures, he refers her to the "
        "Buddha, and the Buddha answers her with three compressed verses she must ask, "
        "three times, to have unpacked. Closes the Nandanavagga. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Near Rājagaha, at the Hot Springs Monastery &mdash; this vagga's only "
                    "departure from the recurring Sāvatthī frame"),
        ("Speakers", "Venerable Samiddhi, an unnamed deity, and, in the second half, the "
                    "Buddha addressing the deity directly"),
        ("Form", "An extended prose narrative framing two verse exchanges, the second "
                 "built from three compressed verses each met with a request for their "
                 "detailed meaning"),
        ("Length", "~4 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; by far the longest and "
                       "most demanding discourse in this vagga, closing on genuinely "
                       "difficult verses the text itself declines to fully resolve"),
        ("Closing this vagga", "The tenth and last discourse of the Nandanavagga, whose "
                               "own closing colophon names the vagga as finished"),
    ],
    why=(
        "Bathing before dawn near Rājagaha, Venerable Samiddhi is approached by a deity "
        "who urges him to enjoy human sensual pleasures while young, rather than deferring "
        "them for a teaching that only takes effect over time. Samiddhi answers with a "
        "formula he has heard but cannot yet explain in detail: sensual pleasures take "
        "effect over time, full of suffering; the teaching is apparent right now. Unable "
        "to elaborate, he sends the deity to the Buddha. What follows is not a straight "
        "explanation: the Buddha answers the deity's request with a compressed verse, she "
        "asks him to spell it out, and he answers with another compressed verse instead "
        "&mdash; three times over. Only the deity's own final paraphrase closes the "
        "discourse, and the text never confirms whether it is right."),
    guide=[
        ("A new setting, once", [
            "Every discourse so far in this vagga, and every discourse in the previous "
            "one, is set near Sāvatthī in Jeta's Grove. This discourse alone moves the "
            "action to Rājagaha's Hot Springs Monastery &mdash; a single, unexplained "
            "departure from this collection's otherwise unbroken setting."]),
        ("Sandiṭṭhika versus kālika", [
            "Samiddhi's reply to the deity's invitation turns on a specific contrast: "
            "sensual pleasures are <em>kālika</em>, taking effect only over time, full of "
            "suffering and distress; the teaching he follows is <em>sandiṭṭhika</em>, "
            "apparent in the present life, immediately effective, inviting inspection. "
            "Pressed to explain exactly how, he admits he cannot &mdash; he is junior, "
            "recently gone forth, and refers the deity onward to the Buddha himself."]),
        ("A retelling the text itself skips", [
            "When Samiddhi reaches the Buddha and recounts everything that happened, the "
            "source text repeats the entire earlier exchange word for word in Pāli "
            "&mdash; but its English translation leaves this retelling blank, since it "
            "would simply repeat what the reader has already read in full. This reading "
            "guide follows the source in passing over the repeated retelling rather than "
            "quoting it twice."]),
        ("Three verses, three requests, no plain answer", [
            "Once the deity confirms her presence to the Buddha directly, he addresses "
            "her not with a prose explanation but with a compressed verse on "
            "<em>akkheyya</em>, &lsquo;the communicable&rsquo; or nameable: beings who "
            "perceive it become established in it, and not understanding it, fall under "
            "Death's yoke. The deity admits she doesn't grasp the &lsquo;detailed "
            "meaning&rsquo; of this &lsquo;brief statement&rsquo; and asks him to spell "
            "it out. He answers, not with prose, but with another compressed verse, on "
            "not measuring oneself as equal, better, or worse. She asks again; he answers "
            "a third time, with a verse on cutting the ties of craving so completely that "
            "gods and humans, searching everywhere, cannot find the one who has done so."]),
        ("The deity's own unconfirmed answer", [
            "Only after the third verse does the deity offer her own paraphrase, in "
            "ordinary ethical terms: never do wrong by speech, mind, or body; having given "
            "up sensual pleasures, mindful and aware, don't keep doing what is painful "
            "and pointless. The discourse simply ends there &mdash; the Buddha never "
            "confirms or corrects her reading, and this reading guide follows the text in "
            "not supplying a resolution it does not itself provide."]),
    ],
    terms=[
        ("sandiṭṭhika, kālika",
         "&ldquo;apparent in the present life&rdquo; versus &ldquo;taking effect over "
         "time&rdquo; &mdash; Samiddhi's contrast between the teaching and sensual "
         "pleasure, which he can state but not yet explain in detail."),
        ("akkheyya",
         "&ldquo;the communicable, the nameable&rdquo; &mdash; the subject of the "
         "Buddha's first verse to the deity, describing what beings become established "
         "in when they fail to understand it fully."),
        ("saṅkhittena bhāsitassa vitthārena atthaṁ",
         "&ldquo;the detailed meaning of a brief statement&rdquo; &mdash; the deity's "
         "repeated request, asked identically after each of the Buddha's three "
         "compressed verses."),
        ("samo visesī uda vā nihīno",
         "&ldquo;equal, special, or worse&rdquo; &mdash; the three self-measurements "
         "(<em>vidhā</em>, discriminations) named in the Buddha's second verse as a "
         "source of dispute."),
        ("chinnaganthaṁ",
         "&ldquo;one whose ties are cut&rdquo; &mdash; the Buddha's third verse's "
         "description of a person gods and humans cannot find, searching anywhere, "
         "having cut craving for name and form at its root."),
    ],
    text_intro=(
        "The discourse in full, with its untranslated internal retelling passed over as "
        "the source itself does. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Samiddhi meets a deity before dawn"),
        ("p", "&sect;1", "sn1.20:1.1-1.5"),
        ("p", "&sect;2", "sn1.20:2.1-2.4"),
        ("p", "&sect;3", "sn1.20:3.1-3.4"),
        ("h3", "An invitation, and a refusal"),
        ("p", "&sect;4", "sn1.20:4.1-4.4"),
        ("p", "&sect;5", "sn1.20:5.1-5.4"),
        ("p", "&sect;6", "sn1.20:6.1-6.2"),
        ("p", "&sect;7", "sn1.20:7.1-7.5"),
        ("p", "&sect;8", "sn1.20:8.1-8.3"),
        ("h3", "The deity keeps her word"),
        ("p", "&sect;9", "sn1.20:17.4-18.2"),
        ("h3", "A verse on the communicable"),
        ("p", "&sect;10", "sn1.20:19.1-21.5"),
        ("p", "&sect;11", "sn1.20:22.1-22.2"),
        ("h3", "A second verse, on equal, special, or worse"),
        ("p", "&sect;12", "sn1.20:23.1-23.5"),
        ("p", "&sect;13", "sn1.20:24.1-24.2"),
        ("h3", "A third verse, on cutting the ties"),
        ("p", "&sect;14", "sn1.20:25.1-26.1"),
        ("h3", "The deity's own answer"),
        ("p", "&sect;15", "sn1.20:27.1-28.4"),
    ],
    quiz=[
        {"q": "What setting does this discourse use, unlike every other discourse in this vagga?",
         "opts": [
             "Rājagaha's Hot Springs Monastery, rather than Sāvatthī",
             "A mountain peak far from any monastery",
             "The heavenly Garden of Delight",
             "No setting is given at all"],
         "correct": 0,
         "expl": "The only departure from this collection's otherwise unbroken Sāvatthī frame."},
        {"q": "What does the deity urge Samiddhi to do?",
         "opts": [
             "Enjoy human sensual pleasures now, while young, rather than deferring them",
             "Give up eating entirely",
             "Return immediately to his family",
             "Abandon the monastic life"],
         "correct": 0,
         "expl": "An invitation framed around not letting the present moment pass."},
        {"q": "What contrast does Samiddhi draw in his reply?",
         "opts": [
             "Sensual pleasures take effect over time (kālika) and cause suffering; the teaching is apparent now (sandiṭṭhika)",
             "Sensual pleasures are apparent now; the teaching takes effect over time",
             "Both sensual pleasures and the teaching take effect only over time",
             "He refuses to draw any contrast at all"],
         "correct": 0,
         "expl": "A formula he can state but, as a junior mendicant, cannot yet explain in detail."},
        {"q": "Why does this reading guide skip a large section of the source text (segments 9 through 17)?",
         "opts": [
             "That section is Samiddhi's retelling of the same events, left blank in the English translation since it merely repeats what came before",
             "That section is missing from the source entirely",
             "That section contains content unsuitable for this project",
             "That section is written in a different language throughout"],
         "correct": 0,
         "expl": "The Pāli repeats the earlier exchange word for word; the English translation omits repeating it."},
        {"q": "How does the Buddha respond to the deity's first request to explain his verse in detail?",
         "opts": [
             "With another compressed verse, not a prose explanation",
             "With a full prose explanation, as requested",
             "By refusing to answer at all",
             "By asking Samiddhi to answer instead"],
         "correct": 0,
         "expl": "The pattern repeats three times: verse, request, another verse."},
        {"q": "What does 'akkheyya' mean, the subject of the Buddha's first verse?",
         "opts": [
             "'The communicable, the nameable'",
             "'The flood'",
             "'A little hut'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "What beings become established in in failing to understand it fully."},
        {"q": "What three self-measurements does the Buddha's second verse name as a source of dispute?",
         "opts": [
             "Equal, special, or worse (samo visesī uda vā nihīno)",
             "Rich, poor, or middling",
             "Young, old, or middle-aged",
             "Wise, foolish, or neutral"],
         "correct": 0,
         "expl": "The three vidhā, discriminations, named in the second compressed verse."},
        {"q": "Who ultimately offers a paraphrase explaining the Buddha's three verses?",
         "opts": [
             "The deity herself, in her own words, unconfirmed by the Buddha",
             "The Buddha, in a final prose explanation",
             "Venerable Samiddhi, after returning to the deity",
             "No paraphrase is ever offered; the discourse ends on the third verse"],
         "correct": 0,
         "expl": "The discourse ends with her own reading, without the Buddha confirming or correcting it."},
        {"q": "What does the deity's final paraphrase say, in ordinary ethical terms?",
         "opts": [
             "Never do wrong by speech, mind, or body; having given up sensual pleasures, don't keep doing what's painful and pointless",
             "Enjoy every sensual pleasure available without restraint",
             "Only aristocrats can achieve liberation",
             "Nothing can ever be understood about the Buddha's teaching"],
         "correct": 0,
         "expl": "Her own synthesis, offered as the discourse's closing lines."},
        {"q": "What is this discourse's position within the Nandanavagga?",
         "opts": [
             "It is the tenth and last discourse, closing the vagga",
             "It is the vagga's first discourse",
             "It belongs to the Naḷavagga, not the Nandanavagga",
             "It has no fixed position in either vagga"],
         "correct": 0,
         "expl": "This discourse's own closing colophon marks the Nandanavagga as finished."},
    ],
    marginalia=[
        ("A new setting, once", [
            "Rājagaha, not Sāvatthī &mdash;",
            "this vagga&rsquo;s only departure",
        ]),
        ("Now, or over time", [
            "sandiṭṭhika, kālika &mdash;",
            "stated, not yet explained",
        ]),
        ("Three verses, three requests", [
            "each brief statement met",
            "with another brief statement",
        ]),
        ("An answer, unconfirmed", [
            "the deity&rsquo;s own reading &mdash;",
            "the text simply ends",
        ]),
    ],
    further=[
        '<a href="%s/sn1.20/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.19.html">SN 1.19 &middot; Little Hut</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.11.html">SN 1.11 &middot; The Garden of Delight</a> &mdash; this '
        "vagga&rsquo;s opening discourse, ten discourses back.",
        '<a href="sn-1.10.html">SN 1.10 &middot; Wilderness</a> &mdash; the discourse that '
        "closed the previous vagga, the Naḷavagga.",
    ],
)
