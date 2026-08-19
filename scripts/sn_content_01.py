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


# --------------------------------------------------------------------------- #
# SN 1.21 — Sattisutta (opens the Sattivagga)
# --------------------------------------------------------------------------- #
page(
    1, 21, "Satti", "A Sword",
    meta_title="SN 1.21 — A Sword | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sattisutta — a "
        "deity's verse on the urgency of going forth to give up sensual desire, met by "
        "the Buddha's identical verse redirected toward giving up substantialist view. "
        "Opens the Sattivagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the recurring frame, "
                    "resumed after this vagga's predecessor dropped it almost entirely"),
        ("Speakers", "An unnamed deity and the Buddha, in a single exchange of verses"),
        ("Form", "A four-line verse of urgency, answered by the same verse with only its "
                 "final line changed"),
        ("Length", "~45 seconds to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple in form, though "
                       "its single substitution carries real doctrinal weight"),
        ("Opening this vagga", "The first discourse of the Sattivagga (&lsquo;the Chapter "
                               "on a Sword&rsquo;), which takes its name from this "
                               "discourse's opening image"),
    ],
    why=(
        "The deity's verse is one of urgency: as if struck by a sword, as if one's head "
        "were on fire, a mendicant should go forth mindfully &mdash; to give up sensual "
        "desire. The Buddha's reply repeats every word of this verse except its very last "
        "phrase: the same urgency, the same imagery, but aimed at giving up "
        "<em>sakkāyadiṭṭhi</em>, substantialist or identity view, instead. The deity names "
        "the danger most people would name first; the Buddha's answer, changing nothing "
        "but the target, names a deeper one."),
    guide=[
        ("An image of extreme urgency", [
            "Being struck by a sword and having one's head catch fire are this "
            "discourse's opening images &mdash; not gradual dangers to be addressed in "
            "due course, but emergencies demanding immediate response. The verse frames "
            "spiritual practice with exactly this same urgency."]),
        ("One word changed, a different target named", [
            "Three of this verse's four lines are identical between the deity's version "
            "and the Buddha's. Only the object of &lsquo;giving up&rsquo; changes: "
            "<em>kāmarāga</em>, sensual desire, in the deity's verse, becomes "
            "<em>sakkāyadiṭṭhi</em>, the view that there is a substantial self identified "
            "with the aggregates, in the Buddha's."]),
        ("Why identity view might be named as the deeper danger", [
            "Sensual desire is the danger most readily recognized as needing urgent "
            "abandonment; identity view is more easily overlooked, since it operates as "
            "an assumption underneath ordinary experience rather than as a felt craving. "
            "By keeping the deity's urgent imagery and simply redirecting it, the Buddha's "
            "reply treats identity view as no less urgent a matter than sensual desire "
            "&mdash; arguably more foundational, since it structures how desire itself is "
            "experienced as belonging to a self."]),
        ("A vagga named for its opening image", [
            "This is the first discourse in this collection so far whose vagga is named "
            "after its own opening image rather than its closing one: <em>satti</em>, "
            "&lsquo;sword,&rsquo; the emergency-image this verse opens with, gives the "
            "whole Sattivagga its name &mdash; unlike the Naḷavagga, named after its "
            "final discourse's closing simile."]),
    ],
    terms=[
        ("satti",
         "&ldquo;sword&rdquo; &mdash; the emergency-image this discourse opens with, and "
         "the source of this vagga's own name."),
        ("ādittasīsūpamo",
         "&ldquo;like one whose head is on fire&rdquo; &mdash; the second emergency-"
         "image, paired with the sword to convey maximum urgency."),
        ("kāmarāgassa pahānāya",
         "&ldquo;to give up sensual desire&rdquo; &mdash; the deity's own stated goal for "
         "this urgent going-forth."),
        ("sakkāyadiṭṭhippahānāya",
         "&ldquo;to give up substantialist view&rdquo; &mdash; the Buddha's single "
         "substitution, redirecting the same urgency toward the view of a substantial "
         "self."),
        ("sato bhikkhu pabbaje",
         "&ldquo;a mendicant, mindful, should go forth&rdquo; &mdash; the shared central "
         "instruction both verses agree on, before their final lines diverge."),
    ],
    text_intro=(
        "The discourse in full: an urgent verse on going forth, answered by the same "
        "verse redirected toward a deeper target. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.21:1.1-1.2"),
        ("p", "&sect;2", "sn1.21:2.1-2.4"),
        ("p", "&sect;3", "sn1.21:3.1-3.4"),
    ],
    quiz=[
        {"q": "What two images does the deity's verse use to convey urgency?",
         "opts": [
             "Being struck by a sword, and having one's head on fire",
             "A flood sweeping everything away",
             "A garden in full bloom",
             "A tortoise withdrawing into its shell"],
         "correct": 0,
         "expl": "Two emergency-images, demanding immediate rather than gradual response."},
        {"q": "What does the deity's verse say a mendicant should go forth to give up?",
         "opts": [
             "Sensual desire (kāmarāga)",
             "Substantialist view",
             "Wealth",
             "Family relationships"],
         "correct": 0,
         "expl": "The deity's own stated goal, before the Buddha's substitution."},
        {"q": "What single change does the Buddha's reply make to the deity's verse?",
         "opts": [
             "It replaces 'sensual desire' with 'substantialist view' (sakkāyadiṭṭhi) as the goal to give up",
             "It rejects the urgency of the deity's imagery entirely",
             "It changes the setting to a different location",
             "It adds an entirely new fifth line"],
         "correct": 0,
         "expl": "Three lines unchanged; only the final target of 'giving up' differs."},
        {"q": "What does 'sakkāyadiṭṭhi' mean?",
         "opts": [
             "The view that there is a substantial self identified with the aggregates",
             "Fear of death",
             "A type of meditation posture",
             "A specific heavenly realm"],
         "correct": 0,
         "expl": "Identity view, the Buddha's substituted target."},
        {"q": "Why might identity view be treated as no less urgent than sensual desire?",
         "opts": [
             "It operates as an underlying assumption structuring experience, more easily overlooked than felt craving",
             "It is a rare view held by almost no one",
             "It has no connection to sensual desire at all",
             "The verse claims it is actually less important than sensual desire"],
         "correct": 0,
         "expl": "A foundational assumption beneath ordinary experience, not a felt craving."},
        {"q": "What gives the Sattivagga its name?",
         "opts": [
             "This discourse's opening image of a sword",
             "This discourse's closing image",
             "The vagga's last discourse",
             "A garden mentioned in a later discourse"],
         "correct": 0,
         "expl": "Unlike the Naḷavagga, named after its closing simile, this vagga is named after its opening image."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the recurring frame",
             "Near Rājagaha",
             "In the heavenly Garden of Delight",
             "No setting is given"],
         "correct": 0,
         "expl": "Resumed here after the previous vagga largely dropped narrative framing."},
        {"q": "How many lines of the deity's and the Buddha's verses are identical?",
         "opts": [
             "Three of four lines",
             "None of the lines match",
             "All four lines match exactly",
             "Only the first line matches"],
         "correct": 0,
         "expl": "Only the final line's target of 'giving up' differs."},
        {"q": "What instruction do both verses share before their final lines diverge?",
         "opts": [
             "That a mendicant, mindful, should go forth (sato bhikkhu pabbaje)",
             "That a mendicant should never go forth",
             "That only aristocrats should go forth",
             "That going forth is unnecessary"],
         "correct": 0,
         "expl": "The shared central instruction, common to both verses."},
        {"q": "Does the Buddha's reply reject the urgency of the deity's imagery?",
         "opts": [
             "No &mdash; it keeps the same urgent imagery and simply redirects its target",
             "Yes, it dismisses the imagery as excessive",
             "Yes, it claims there is no urgency at all",
             "It replaces the imagery with a calmer image instead"],
         "correct": 0,
         "expl": "The urgency itself is preserved; only what it is urgent about changes."},
    ],
    marginalia=[
        ("Struck, on fire", [
            "like a sword, like flame &mdash;",
            "urgency named twice",
        ]),
        ("One target named", [
            "give up sensual desire,",
            "says the deity",
        ]),
        ("A deeper target", [
            "give up substantialist view,",
            "says the Buddha",
        ]),
        ("A vagga named at its start", [
            "satti, the sword &mdash;",
            "this chapter&rsquo;s own name",
        ]),
    ],
    further=[
        '<a href="%s/sn1.21/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.20.html">SN 1.20 &middot; With Samiddhi</a> &mdash; the discourse '
        "that closed the previous vagga, the Nandanavagga.",
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this '
        "collection&rsquo;s opening discourse.",
        "SN 1.22 &middot; Impact &mdash; the next discourse, on how wronging the "
        "innocent backfires on the one who wrongs them.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.22 — Phusatisutta
# --------------------------------------------------------------------------- #
page(
    1, 22, "Phusati", "Impact",
    meta_title="SN 1.22 — Impact | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Phusatisutta — "
        "two verses on how wronging an innocent person backfires on the wrongdoer, closing "
        "with a simile shared word for word with the Dhammapada. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; two verses on the same theme, presented in "
                     "sequence"),
        ("Form", "Two four-line verses on karmic backfire, sharing a single theme"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form"),
        ("Cross-reference", "The second verse's closing simile is close to identical to "
                            "Dhammapada verse 125 (Bālavagga)"),
    ],
    why=(
        "The first verse states a principle: harm doesn't land on one who doesn't harm "
        "others; it lands on someone precisely because they harm others; that's why it "
        "lands on the one who wrongs someone who has done no wrong. The second verse "
        "restates this with a concrete image: whoever wrongs a pure, unblemished person, "
        "the evil backfires on the fool &mdash; like fine dust thrown upwind, which "
        "returns to blow back on the thrower rather than travel forward."),
    guide=[
        ("A principle, then an image", [
            "The first verse states the logic of karmic backfire abstractly: harm has no "
            "purchase on one who gives none, and finds its target specifically in the one "
            "who wrongs an innocent party. The second verse restates the same claim "
            "concretely, through a single vivid image."]),
        ("Dust thrown against the wind", [
            "&lsquo;Like fine dust thrown upwind&rsquo; (<em>sukhumo rajo "
            "paṭivātaṁva khitto</em>) pictures an attempt to throw dust at someone "
            "while facing into the wind: the dust does not reach its target but blows "
            "back onto the thrower instead. The image makes the abstract principle "
            "physically vivid &mdash; harm aimed outward returns to its source by the "
            "very mechanics of the attempt."]),
        ("A verse shared with the Dhammapada", [
            "This same simile, describing harm done to one who is pure and without "
            "blemish, appears in the Dhammapada as well, at verse 125 in its Bālavagga "
            "(&lsquo;Chapter on Fools&rsquo;) &mdash; close enough in wording to be "
            "recognized as the same verse appearing in two different collections, as "
            "with SN 1.5's parallel to Dhammapada verse 370."]),
        ("Innocence specified, not assumed", [
            "Both verses are careful to specify that the one harmed has done no wrong "
            "(<em>appaduṭṭha</em>) and is unblemished (<em>anaṅgaṇa</em>) &mdash; the "
            "claim is not that all harm backfires indiscriminately, but specifically that "
            "harming genuine innocence returns to its source."]),
    ],
    terms=[
        ("phusati",
         "&ldquo;impacts, touches, lands on&rdquo; &mdash; the verb this discourse's title "
         "comes from, describing how harm finds or fails to find its mark."),
        ("appaduṭṭha",
         "&ldquo;one who has done no wrong&rdquo; &mdash; both verses' description of the "
         "person harmed, specifying genuine innocence rather than harm in general."),
        ("anaṅgaṇa",
         "&ldquo;unblemished, without a fault&rdquo; &mdash; paired with "
         "<em>appaduṭṭha</em> to underscore the purity of the one wronged."),
        ("sukhumo rajo paṭivātaṁva khitto",
         "&ldquo;like fine dust thrown upwind&rdquo; &mdash; the discourse's closing "
         "simile, appearing near-identically at Dhammapada verse 125."),
        ("bālaṁ pacceti pāpaṁ",
         "&ldquo;the evil backfires on the fool&rdquo; &mdash; the verse's direct "
         "statement of the principle the dust simile then illustrates."),
    ],
    text_intro=(
        "The discourse in full: a principle of karmic backfire, then the image that makes "
        "it vivid. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.22:1.1-1.4"),
        ("p", "&sect;2", "sn1.22:2.1-2.4"),
    ],
    quiz=[
        {"q": "What principle does the first verse state?",
         "opts": [
             "Harm doesn't land on one who harms no one, but lands on one who wrongs an innocent party",
             "Harm always lands equally on everyone",
             "Harm never has any real effect on anyone",
             "Only deities can be harmed"],
         "correct": 0,
         "expl": "The abstract statement of karmic backfire this discourse opens with."},
        {"q": "What image does the second verse use to make this concrete?",
         "opts": [
             "Fine dust thrown upwind, blowing back on the thrower",
             "A sword striking its target",
             "A flood sweeping everything away",
             "A tortoise withdrawing into its shell"],
         "correct": 0,
         "expl": "Sukhumo rajo paṭivātaṁva khitto &mdash; harm aimed outward returning to its source."},
        {"q": "What well-known verse collection shares this discourse's closing simile?",
         "opts": [
             "The Dhammapada (verse 125, Bālavagga)",
             "The Jātaka tales",
             "The Vinaya Piṭaka",
             "The Theragāthā"],
         "correct": 0,
         "expl": "A near-identical simile appears in both collections, as with SN 1.5's Dhammapada parallel."},
        {"q": "How do both verses describe the person who is wronged?",
         "opts": [
             "As having done no wrong (appaduṭṭha) and being unblemished (anaṅgaṇa)",
             "As wealthy and powerful",
             "As a deity, not a human",
             "As having provoked the harm themselves"],
         "correct": 0,
         "expl": "Genuine innocence is specified, not harm in general."},
        {"q": "Does this discourse claim that all harm backfires indiscriminately?",
         "opts": [
             "No &mdash; it specifies harming genuine innocence as what returns to its source",
             "Yes, it claims all forms of harm always backfire equally",
             "It claims harm never backfires under any circumstances",
             "It makes no distinction about who is harmed"],
         "correct": 0,
         "expl": "The careful specification of innocence and purity is central to the claim."},
        {"q": "What does 'phusati' mean?",
         "opts": [
             "'Impacts, touches, lands on'",
             "'Escapes, avoids'",
             "'Delights in'",
             "'Sleeps through'"],
         "correct": 0,
         "expl": "This discourse's title, describing how harm finds or fails to find its mark."},
        {"q": "What happens to dust thrown while facing into the wind, according to the image?",
         "opts": [
             "It blows back onto the thrower rather than reaching its intended target",
             "It travels further than usual",
             "It disappears completely",
             "It has no effect on anyone"],
         "correct": 0,
         "expl": "The physical mechanics of the image illustrate the karmic principle."},
        {"q": "What does 'bālaṁ pacceti pāpaṁ' mean?",
         "opts": [
             "'The evil backfires on the fool'",
             "'The wise are never harmed'",
             "'Evil never has consequences'",
             "'The fool is always innocent'"],
         "correct": 0,
         "expl": "The direct statement the dust simile then illustrates."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set near Rājagaha",
             "Explicitly set in the heavenly Garden of Delight",
             "Explicitly set at a river crossing"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "How many verses does this discourse contain?",
         "opts": [
             "Two",
             "One",
             "Five",
             "Eight"],
         "correct": 0,
         "expl": "A principle stated, then illustrated by a single vivid image."},
    ],
    marginalia=[
        ("A principle stated", [
            "harm lands on the one",
            "who wrongs the innocent",
        ]),
        ("Dust against the wind", [
            "thrown forward, it returns &mdash;",
            "sukhumo rajo paṭivātaṁva khitto",
        ]),
        ("Shared with the Dhammapada", [
            "the same simile,",
            "verse 125, Bālavagga",
        ]),
        ("Innocence, specified", [
            "appaduṭṭha, anaṅgaṇa &mdash;",
            "not harm in general",
        ]),
    ],
    further=[
        '<a href="%s/sn1.22/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.21.html">SN 1.21 &middot; A Sword</a> &mdash; the discourse '
        "immediately before this one, and this vagga&rsquo;s opening discourse.",
        '<a href="sn-1.5.html">SN 1.5 &middot; Cut How Many?</a> &mdash; this '
        "collection&rsquo;s other verse shared word for word with the Dhammapada.",
        "SN 1.23 &middot; A Tangle &mdash; the next discourse, and the verse traditionally "
        "said to have prompted Buddhaghosa's Visuddhimagga.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.23 — Jaṭāsutta
# --------------------------------------------------------------------------- #
page(
    1, 23, "Jaṭā", "A Tangle",
    meta_title="SN 1.23 — A Tangle | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Jaṭāsutta — a "
        "deity's question asking who can untangle the human tangle of confusion, answered "
        "in three stages: ethics and wisdom, the ended defilements, and the cessation of "
        "name and form. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "A deity, addressing the Buddha by name (&lsquo;Gotama&rsquo;), and "
                    "the Buddha, replying at unusual length"),
        ("Form", "A four-line question, answered by three four-line verses"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; simple in language, "
                       "demanding in what it asks the reader to hold together"),
        ("A famous question", "This discourse's opening verse is traditionally said to be "
                              "the verse that prompted Buddhaghosa's 5th-century treatise "
                              "the Visuddhimagga, written as an extended answer to it"),
    ],
    why=(
        "The deity's question is direct, and addresses the Buddha by his clan name, "
        "Gotama, rather than an honorific: people are tangled within and tangled without, "
        "tangled in tangles &mdash; who can untangle this tangle? The Buddha's answer "
        "unfolds in three verses rather than this vagga's usual one, moving from a "
        "practitioner in training, to the fully perfected arahant, to the very point "
        "&mdash; the cessation of name and form &mdash; where the tangle is finally cut."),
    guide=[
        ("A tangle within and without", [
            "The deity's opening image, <em>jaṭā</em>, names matted or knotted hair, used "
            "here for the condition of being entangled both internally (in one's own "
            "mental confusion) and externally (in one's relationships and circumstances). "
            "The question &lsquo;who can untangle this tangle&rsquo; treats this as the "
            "single most pressing human problem."]),
        ("Three verses, three stages", [
            "The Buddha's answer does not name a single untangler but traces a sequence: "
            "first, a wise person grounded in ethics (<em>sīla</em>), developing mind and "
            "wisdom (<em>citta</em>, <em>paññā</em>), keen and alert, who <em>can</em> "
            "untangle the tangle; second, those in whom greed, hate, and ignorance have "
            "faded, the perfected ones (<em>arahant</em>) with defilements ended, who "
            "<em>have</em> untangled it; third, the specific point &mdash; where name and "
            "form (<em>nāmarūpa</em>) cease without residue &mdash; where the tangle is "
            "actually cut."]),
        ("A famous verse, traditionally", [
            "This discourse's opening question is traditionally identified as the verse "
            "that prompted Buddhaghosa's Visuddhimagga (&lsquo;Path of Purification&rsquo;), "
            "the great 5th-century Theravāda commentarial treatise, which frames its own "
            "entire systematic exposition of ethics, concentration, and wisdom as an "
            "extended answer to precisely this question."]),
        ("From training to cutting, not merely untangling", [
            "The verse's final line shifts its own verb: the first two stages "
            "&lsquo;untangle&rsquo; (<em>vijaṭaye</em>) the tangle, but the third names "
            "the tangle as &lsquo;cut&rsquo; (<em>chinna</em>) at the specific point where "
            "name-and-form and the perception of form cease entirely &mdash; suggesting "
            "untangling is not the final image; cutting off the very conditions for "
            "tangling is."]),
    ],
    terms=[
        ("jaṭā",
         "&ldquo;a tangle&rdquo; &mdash; literally matted hair, this discourse's title "
         "and central image for both inner and outer entanglement."),
        ("gotama",
         "the Buddha's clan name, used here by the deity directly rather than an "
         "honorific title &mdash; a notably informal address in this collection."),
        ("sīla, citta, paññā",
         "&ldquo;ethics, mind, wisdom&rdquo; &mdash; the three qualities the first stage "
         "of the reply names as grounding one who can untangle the tangle."),
        ("nāmarūpa",
         "&ldquo;name and form&rdquo; &mdash; mental and physical phenomena together, "
         "whose cessation without residue the verse's final stage names as where the "
         "tangle is actually cut."),
        ("vijaṭaye",
         "&ldquo;can untangle&rdquo; &mdash; the verb used for the first two stages of "
         "the reply, before the final line shifts to <em>chinna</em>, &ldquo;cut.&rdquo;"),
    ],
    text_intro=(
        "The discourse in full: a famous question, and an answer unfolding in three "
        "stages. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A question, addressed to Gotama by name"),
        ("p", "&sect;1", "sn1.23:1.1-1.4"),
        ("h3", "Three stages of an answer"),
        ("p", "&sect;2", "sn1.23:2.1-2.4"),
        ("p", "&sect;3", "sn1.23:3.1-3.4"),
        ("p", "&sect;4", "sn1.23:4.1-4.4"),
    ],
    quiz=[
        {"q": "What image does the deity's question use for human confusion?",
         "opts": [
             "A tangle (jaṭā), knotted both within and without",
             "A flood sweeping everything away",
             "A sword striking its target",
             "Dust thrown against the wind"],
         "correct": 0,
         "expl": "Matted or knotted hair, used for both inner and outer entanglement."},
        {"q": "How does the deity address the Buddha in this discourse?",
         "opts": [
             "By his clan name, Gotama, rather than an honorific",
             "By a formal royal title",
             "The deity does not address the Buddha directly",
             "By calling him 'Great Hero' only"],
         "correct": 0,
         "expl": "A notably informal address for this collection."},
        {"q": "How many verses does the Buddha's answer run to, and what does this signal?",
         "opts": [
             "Three, unfolding in stages rather than a single compressed answer",
             "One, matching the vagga's usual length",
             "Five, the longest reply in this collection",
             "The Buddha gives no verse reply at all"],
         "correct": 0,
         "expl": "A sequence from training, to arahantship, to cessation itself."},
        {"q": "What does the reply's first stage name as grounding one who can untangle the tangle?",
         "opts": [
             "Ethics, developing the mind, and wisdom (sīla, citta, paññā)",
             "Wealth and social status",
             "Physical strength alone",
             "Political power"],
         "correct": 0,
         "expl": "The first of three stages in the Buddha's answer."},
        {"q": "What does the reply's second stage describe?",
         "opts": [
             "Those in whom greed, hate, and ignorance have faded — the arahants with defilements ended",
             "Ordinary householders",
             "Deities of the Thirty-Three",
             "Newly ordained mendicants"],
         "correct": 0,
         "expl": "Those who have already untangled the tangle, not merely those capable of doing so."},
        {"q": "What does the reply's third and final stage name as the actual point of cutting?",
         "opts": [
             "Where name and form (nāmarūpa) cease without residue",
             "Where a mendicant first goes forth",
             "Where a deity first speaks",
             "Where ethics alone is established"],
         "correct": 0,
         "expl": "Cessation itself, not merely training or even arahantship, is named as the cutting point."},
        {"q": "What treatise is this discourse's opening question traditionally said to have prompted?",
         "opts": [
             "Buddhaghosa's Visuddhimagga",
             "The Abhidhamma Piṭaka",
             "The Milindapañhā",
             "The Dhammapada"],
         "correct": 0,
         "expl": "A 5th-century systematic treatise on ethics, concentration, and wisdom."},
        {"q": "What verb does the verse's final line use, distinct from the earlier stages?",
         "opts": [
             "'Cut' (chinna), rather than 'untangle' (vijaṭaye)",
             "'Ignore'",
             "'Delay'",
             "'Repeat'"],
         "correct": 0,
         "expl": "Suggesting cessation is a different kind of resolution than mere untangling."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set at the Hot Springs Monastery",
             "Explicitly set in the heavenly Garden of Delight",
             "Explicitly set at a riverbank"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "Is the tangle described as only an external, social problem?",
         "opts": [
             "No &mdash; it is described as tangled both within and without",
             "Yes, it is described as purely external",
             "Yes, it is described as purely internal",
             "The discourse does not specify"],
         "correct": 0,
         "expl": "Jaṭā jaṭinī &mdash; both inner and outer entanglement named together."},
    ],
    marginalia=[
        ("A tangle, named", [
            "within and without &mdash;",
            "who can untangle this?",
        ]),
        ("Three stages, given", [
            "ethics and wisdom,",
            "then arahantship, then cessation",
        ]),
        ("A famous prompt", [
            "traditionally the seed",
            "of the Visuddhimagga",
        ]),
        ("Untangled, then cut", [
            "vijaṭaye, then chinna &mdash;",
            "two different resolutions",
        ]),
    ],
    further=[
        '<a href="%s/sn1.23/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.22.html">SN 1.22 &middot; Impact</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.19.html">SN 1.19 &middot; Little Hut</a> &mdash; an earlier '
        "discourse in this same collection, also unpacked in stages.",
        "SN 1.24 &middot; Shielding the Mind &mdash; the next discourse, correcting an "
        "over-broad prescription with a more precise one.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.24 — Manonivāraṇasutta
# --------------------------------------------------------------------------- #
page(
    1, 24, "Manonivāraṇa", "Shielding the Mind",
    meta_title="SN 1.24 — Shielding the Mind | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Manonivāraṇasutta — a proposal to shield the mind from everything, corrected "
        "by the Buddha's reply that only where bad things come from needs shielding. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a proposal offered, then corrected"),
        ("Form", "A four-line claim, answered by a four-line correction rather than "
                 "agreement or reversal"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form, with "
                       "an unusually precise correction"),
        ("A third kind of exchange", "Unlike this vagga's reversals (SN 1.21) or "
                                     "confirmations (SN 1.22), this discourse's reply "
                                     "moderates an overgeneralized claim"),
    ],
    why=(
        "The opening verse proposes something that sounds reasonable at first: whatever "
        "you've shielded the mind from can't cause you suffering, so shield the mind from "
        "everything, and you'll be freed from all suffering. The reply does not accept "
        "this conclusion. It says you need not shield the mind from everything &mdash; "
        "nor, it adds, has total shielding actually given the mind self-control. The mind "
        "needs to be shielded only from where bad things specifically come from."),
    guide=[
        ("A proposal that overshoots", [
            "The opening verse's logic seems sound as a general principle &mdash; what "
            "the mind is shielded from cannot cause suffering &mdash; but it draws from "
            "this a sweeping conclusion: shield the mind from everything. The reply "
            "targets exactly this overreach, not the underlying principle itself."]),
        ("Total shielding does not equal self-control", [
            "The reply's second line makes a claim easy to miss: total shielding "
            "(<em>na ca sabbattha nivarayissasi</em>) does not, by itself, give the mind "
            "genuine mastery over itself. Blanket restriction and trained self-control "
            "are treated as different things &mdash; the first does not automatically "
            "produce the second."]),
        ("Shielding only where bad things come from", [
            "The reply's precise correction &mdash; shield the mind only "
            "&lsquo;from where bad things come&rsquo; (<em>yatoni pāpakā āgacchanti</em>) "
            "&mdash; treats discernment, knowing specifically which sources produce harm, "
            "as doing the actual work that blanket restriction only appears to do."]),
        ("A third pattern within this vagga", [
            "SN 1.21, this vagga's opening discourse, redirected a claim by changing one "
            "word; SN 1.22 restated a single claim with a supporting image. This "
            "discourse does neither &mdash; it takes a proposal seriously enough to "
            "correct its scope precisely, rather than either affirming or reversing it "
            "wholesale."]),
    ],
    terms=[
        ("mano",
         "&ldquo;the mind&rdquo; &mdash; the subject of both verses, and half of this "
         "discourse's title."),
        ("nivāraṇa",
         "&ldquo;shielding, restraining&rdquo; &mdash; the other half of this discourse's "
         "title, naming the practice both verses discuss but disagree about the scope "
         "of."),
        ("na ca sabbattha nivarayissasi",
         "&ldquo;nor has the mind gained self-control [through total shielding]&rdquo; "
         "&mdash; the reply's claim that blanket restriction does not by itself produce "
         "genuine mastery."),
        ("yatoni pāpakā āgacchanti",
         "&ldquo;from where bad things come&rdquo; &mdash; the reply's precise target for "
         "where shielding is actually needed."),
        ("sabbato",
         "&ldquo;from everything&rdquo; &mdash; the opening verse's proposed, and "
         "rejected, scope for shielding the mind."),
    ],
    text_intro=(
        "The discourse in full: a proposal to shield the mind from everything, corrected "
        "toward precision. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.24:1.1-1.4"),
        ("p", "&sect;2", "sn1.24:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does the opening verse propose?",
         "opts": [
             "That the mind should be shielded from everything, to be freed from all suffering",
             "That the mind should never be shielded from anything",
             "That only the body, not the mind, needs shielding",
             "That suffering cannot be avoided by any means"],
         "correct": 0,
         "expl": "A sweeping conclusion drawn from a reasonable-sounding premise."},
        {"q": "How does the reply respond to this proposal?",
         "opts": [
             "It corrects the proposal's scope, rather than fully agreeing or reversing it",
             "It fully agrees with the proposal as stated",
             "It completely rejects the value of shielding the mind at all",
             "It ignores the proposal and changes the subject"],
         "correct": 0,
         "expl": "Neither confirmation nor reversal, but a precise correction."},
        {"q": "What does the reply say about total shielding and self-control?",
         "opts": [
             "That total shielding does not, by itself, give the mind genuine self-control",
             "That total shielding is the only way to achieve self-control",
             "That self-control is impossible under any circumstances",
             "That self-control requires no shielding whatsoever"],
         "correct": 0,
         "expl": "Blanket restriction and trained mastery are treated as different things."},
        {"q": "What does the reply say the mind actually needs to be shielded from?",
         "opts": [
             "Only where bad things specifically come from (yatoni pāpakā āgacchanti)",
             "Absolutely everything without exception",
             "Nothing at all",
             "Only pleasant experiences"],
         "correct": 0,
         "expl": "A precise, discerning target rather than a blanket rule."},
        {"q": "How does this discourse's structure differ from SN 1.21 and SN 1.22?",
         "opts": [
             "It corrects a claim's scope precisely, rather than redirecting it or restating it with an image",
             "It uses exactly the same technique as SN 1.21",
             "It uses exactly the same technique as SN 1.22",
             "It contains no second verse at all"],
         "correct": 0,
         "expl": "A third distinct pattern of exchange within this vagga."},
        {"q": "What does 'mano' mean?",
         "opts": [
             "'The mind'",
             "'The body'",
             "'A sword'",
             "'A tangle'"],
         "correct": 0,
         "expl": "The subject both verses discuss, and half this discourse's title."},
        {"q": "Does the reply reject the underlying principle that what the mind is shielded from cannot cause suffering?",
         "opts": [
             "No &mdash; it targets the proposal's overreach in scope, not the underlying principle",
             "Yes, it rejects the principle entirely",
             "It claims the principle applies only to deities",
             "It claims the principle was never stated"],
         "correct": 0,
         "expl": "The correction is about scope, not about the basic logic of shielding."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set near Rājagaha",
             "Explicitly set at a mountain peak",
             "Explicitly set in a marketplace"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "What does 'sabbato' mean?",
         "opts": [
             "'From everything' &mdash; the opening verse's rejected proposed scope",
             "'From nothing'",
             "'Sometimes'",
             "'Rarely'"],
         "correct": 0,
         "expl": "The overgeneralized scope the reply corrects."},
        {"q": "How many verses does this discourse contain?",
         "opts": [
             "Two",
             "One",
             "Four",
             "Five"],
         "correct": 0,
         "expl": "A proposal, then a precise correction."},
    ],
    marginalia=[
        ("A sweeping proposal", [
            "shield the mind",
            "from everything",
        ]),
        ("A precise correction", [
            "not everywhere &mdash;",
            "only where bad things come from",
        ]),
        ("Shielding is not mastery", [
            "total restriction alone",
            "doesn&rsquo;t give self-control",
        ]),
        ("A third kind of exchange", [
            "neither reversal nor echo &mdash;",
            "scope, corrected",
        ]),
    ],
    further=[
        '<a href="%s/sn1.24/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.23.html">SN 1.23 &middot; A Tangle</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.16.html">SN 1.16 &middot; Sleepiness and Sloth</a> &mdash; an '
        "earlier discourse in this collection also concerned with disciplined attention.",
        "SN 1.25 &middot; A Perfected One &mdash; the next discourse, on whether an "
        "arahant's ordinary speech implies conceit.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.25 — Arahantasutta
# --------------------------------------------------------------------------- #
page(
    1, 25, "Arahanta", "A Perfected One",
    meta_title="SN 1.25 — A Perfected One | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Arahantasutta — "
        "a deity's question on whether an arahant's use of 'I speak' and 'they speak to "
        "me' implies conceit, and the Buddha's answer distinguishing convention from "
        "clinging. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "An unnamed deity and the Buddha, across two rounds of question and "
                    "answer"),
        ("Form", "Two paired questions, each answered by a verse of matching or greater "
                 "length"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; one of this "
                       "collection's more philosophically demanding discourses, on "
                       "language, self-reference, and conceit"),
        ("A recurring philosophical question", "This discourse addresses directly a "
                                                "question relevant well beyond this "
                                                "single exchange: how someone free of "
                                                "self-view can still say &lsquo;I&rsquo;"),
    ],
    why=(
        "The deity's first question asks something genuinely puzzling: would a mendicant "
        "who is perfected, with defilements ended, ever say &lsquo;I speak&rsquo; or "
        "&lsquo;they speak to me&rsquo;? The Buddha answers that yes, they would &mdash; "
        "skillful, understanding the world's own labels, they use such terms merely as "
        "expressions. The deity presses further: doesn't saying &lsquo;I&rsquo; draw such "
        "a person close to conceit? The Buddha's second answer distinguishes precisely "
        "between the ties of conceit, which such a person has entirely dissolved, and the "
        "ordinary use of conventional language, which continues regardless."),
    guide=[
        ("A puzzle about self-reference", [
            "If an arahant has fully seen through the notion of a substantial self, the "
            "deity's question implicitly asks, how could they still use ordinary "
            "first-person language at all &mdash; 'I speak,' 'they speak to me' &mdash; "
            "without contradicting what they have realized? This is not a rhetorical "
            "question the Buddha simply dismisses; it receives a direct, considered "
            "answer."]),
        ("Loka-samaññā, the world's own labels", [
            "The Buddha's first answer turns on a specific phrase: such a person, being "
            "skillful, understands <em>lokasamaññaṁ</em>, the world's own conventional "
            "labels, and uses terms like 'I' as mere expressions "
            "(<em>voharamattena</em>) rather than as claims about an underlying "
            "substantial self. The words are used, but not believed in the way ordinary "
            "usage might imply."]),
        ("Conceit as ties, not as vocabulary", [
            "The deity's second question sharpens the puzzle: doesn't using 'I' bring "
            "such a person close to conceit (<em>māna</em>) after all? The Buddha's "
            "second answer relocates the issue entirely: conceit is a matter of "
            "<em>ties</em> (<em>gantha</em>), all of which such a person has dissolved, "
            "not a matter of which words are spoken. Someone can be completely free of "
            "conceit's ties while still using the vocabulary conceit also happens to use."]),
        ("A distinction with wide implications", [
            "This discourse's distinction between conventional language and the "
            "psychological ties it might, in an unliberated speaker, accompany has "
            "relevance well past this single exchange: it addresses directly how "
            "teaching, conversation, and ordinary reference remain possible for someone "
            "who has, by the collection's own account, seen through the assumption of a "
            "substantial self underlying such reference."]),
    ],
    terms=[
        ("khīṇāsavo",
         "&ldquo;one whose defilements are ended&rdquo; &mdash; the description of the "
         "arahant both of the deity's questions concern."),
        ("lokasamaññaṁ",
         "&ldquo;the world's own labels, conventional usage&rdquo; &mdash; what the "
         "arahant is said to understand, allowing ordinary language to be used skillfully "
         "rather than naively."),
        ("voharamattena",
         "&ldquo;as mere expression, as a manner of speaking&rdquo; &mdash; how the "
         "arahant is said to use terms like 'I,' without the underlying belief in a "
         "substantial self such usage might otherwise imply."),
        ("māna",
         "&ldquo;conceit&rdquo; &mdash; the specific concern raised by the deity's second "
         "question, distinguished in the reply from ordinary linguistic convention."),
        ("chinnagantho",
         "&ldquo;one whose ties are cut&rdquo; &mdash; the reply's description of someone "
         "free of conceit's ties, regardless of what conventional words they continue to "
         "use."),
    ],
    text_intro=(
        "The discourse in full: two questions on whether an arahant's ordinary speech "
        "implies conceit, and two careful answers. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A question about self-reference"),
        ("p", "&sect;1", "sn1.25:1.1-1.4"),
        ("p", "&sect;2", "sn1.25:2.1-2.6"),
        ("h3", "A sharper question about conceit"),
        ("p", "&sect;3", "sn1.25:3.1-3.5"),
        ("p", "&sect;4", "sn1.25:4.1-5.3"),
    ],
    quiz=[
        {"q": "What does the deity's first question ask?",
         "opts": [
             "Whether a fully perfected mendicant would ever say 'I speak' or 'they speak to me'",
             "Whether the flood can be crossed",
             "Whether deities exist",
             "Whether the ascetic life is worthwhile"],
         "correct": 0,
         "expl": "A puzzle about self-reference for someone who has seen through self-view."},
        {"q": "How does the Buddha answer this first question?",
         "opts": [
             "Yes &mdash; such a person, skillful and understanding the world's labels, uses these terms as mere expressions",
             "No, such a person would never speak at all",
             "The question is refused as unanswerable",
             "Only deities, never mendicants, may use such language"],
         "correct": 0,
         "expl": "Voharamattena &mdash; used as expression, not as a claim about a substantial self."},
        {"q": "What does the deity's second question press further?",
         "opts": [
             "Whether using 'I' brings such a person close to conceit",
             "Whether such a person has any wisdom at all",
             "Whether the first answer was a lie",
             "Whether deities can also become arahants"],
         "correct": 0,
         "expl": "Sharpening the puzzle raised by the first question and answer."},
        {"q": "How does the Buddha's second answer relocate the issue?",
         "opts": [
             "Conceit is a matter of ties (gantha), all dissolved, not a matter of which words are spoken",
             "Conceit is entirely a matter of vocabulary choice",
             "Conceit cannot be dissolved under any circumstances",
             "The second question is dismissed without an answer"],
         "correct": 0,
         "expl": "Language and psychological clinging are treated as separate matters."},
        {"q": "What does 'lokasamaññaṁ' mean?",
         "opts": [
             "'The world's own labels, conventional usage'",
             "'A type of deity'",
             "'The flood'",
             "'A monastery near Rājagaha'"],
         "correct": 0,
         "expl": "What the arahant is said to understand and use skillfully."},
        {"q": "What does 'voharamattena' mean?",
         "opts": [
             "'As mere expression, as a manner of speaking'",
             "'As an absolute truth'",
             "'Never, under any circumstances'",
             "'Only when compelled by force'"],
         "correct": 0,
         "expl": "How ordinary words like 'I' are used without an underlying belief in a substantial self."},
        {"q": "What does 'chinnagantho' describe?",
         "opts": [
             "One whose ties are cut, free of conceit regardless of conventional words used",
             "One who has never spoken at all",
             "One who is still bound by every tie",
             "A type of deity"],
         "correct": 0,
         "expl": "The reply's precise description of freedom from conceit's ties."},
        {"q": "Does this discourse claim that arahants cannot use ordinary language?",
         "opts": [
             "No &mdash; it explicitly affirms they use such language skillfully, as mere expression",
             "Yes, it claims arahants can never speak",
             "Yes, it claims arahants must invent an entirely new language",
             "It does not address this question at all"],
         "correct": 0,
         "expl": "The whole discourse turns on affirming, then explaining, this continued use."},
        {"q": "What description is given to the arahant discussed in both questions?",
         "opts": [
             "Perfected, proficient, with defilements ended, bearing the final body",
             "Wealthy and politically powerful",
             "A deity of the Thirty-Three",
             "A junior, recently ordained mendicant"],
         "correct": 0,
         "expl": "Khīṇāsavo antimadehadharo &mdash; the recurring description across all four verses."},
        {"q": "How many rounds of question and answer does this discourse contain?",
         "opts": [
             "Two",
             "One",
             "Five",
             "Eight"],
         "correct": 0,
         "expl": "A first question and answer on self-reference, then a sharper second round on conceit."},
    ],
    marginalia=[
        ("A puzzle, posed", [
            "would a perfected one",
            "still say &lsquo;I speak&rsquo;?",
        ]),
        ("Yes, as expression", [
            "lokasamaññaṁ, understood &mdash;",
            "words used, not believed in",
        ]),
        ("Pressed further", [
            "doesn&rsquo;t &lsquo;I&rsquo; draw one",
            "close to conceit?",
        ]),
        ("Ties, not vocabulary", [
            "chinnagantho &mdash;",
            "the ties are cut, the words remain",
        ]),
    ],
    further=[
        '<a href="%s/sn1.25/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.24.html">SN 1.24 &middot; Shielding the Mind</a> &mdash; the '
        "discourse immediately before this one.",
        '<a href="sn-1.9.html">SN 1.9 &middot; Fond of Conceit</a> &mdash; an earlier '
        "discourse in this collection also concerned with conceit and its abandonment.",
        "SN 1.26 &middot; Lamps &mdash; the next discourse, a question-and-answer on the "
        "four lamps that light the world.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.26 — Pajjotasutta
# --------------------------------------------------------------------------- #
page(
    1, 26, "Pajjota", "Lamps",
    meta_title="SN 1.26 — Lamps | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Pajjotasutta — "
        "a question asking how many lamps light up the world, answered with four: the "
        "sun, the moon, fire, and, supreme among them, a Buddha. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a direct question and a complete, itemized "
                     "answer"),
        ("Form", "A four-line question, answered by two four-line verses listing exactly "
                 "four items"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the simplest kind of "
                       "list-completion in this collection"),
        ("A closed list", "The answer specifies explicitly that a fifth lamp is not "
                          "found, closing the list rather than leaving it open"),
    ],
    why=(
        "The question is plain: how many lamps light up the world? The answer counts "
        "exactly four, and states directly that a fifth is not to be found: the sun "
        "blazing by day, the moon radiating by night, fire illuminating both day and "
        "night, and, named as the best of these blazes and the supreme radiance, a "
        "Buddha."),
    guide=[
        ("A question inviting a specific count", [
            "Unlike this vagga's riddles built on open-ended contrasts, this question "
            "asks for an exact number, and the answer supplies one directly: four, with "
            "the explicit statement that no fifth exists. The form is closer to a "
            "catalogue than to a puzzle."]),
        ("Three ordinary lights, then one further", [
            "The first three items are unremarkable as light sources: the sun by day, "
            "the moon by night, and fire capable of either. Each is named for the "
            "specific circumstance in which it functions, before the fourth item breaks "
            "the pattern entirely."]),
        ("A Buddha as the supreme radiance", [
            "The fourth lamp is not another physical source of light but a person: a "
            "Buddha, named as <em>pajjotamuttamo</em>, &lsquo;the best of blazes,&rsquo; "
            "and <em>etaṁ anuttariyaṁ</em>, &lsquo;the supreme radiance.&rsquo; The list "
            "moves from physical illumination to a different order of &lsquo;light&rsquo; "
            "altogether, without announcing the shift beforehand."]),
        ("A closed count, not a metaphor left open", [
            "The verse's explicit &lsquo;a fifth is not found&rsquo; forecloses reading "
            "this as an open-ended list of things that might illuminate the world in some "
            "sense. Four, and only four, are named &mdash; a structure that treats a "
            "Buddha's teaching as literally completing the set of the world's light "
            "sources, not merely resembling one."]),
    ],
    terms=[
        ("pajjota",
         "&ldquo;a lamp, a blaze&rdquo; &mdash; this discourse's title, and the general "
         "term the question asks to enumerate."),
        ("suriyo",
         "&ldquo;the sun&rdquo; &mdash; the first named lamp, blazing specifically by "
         "day."),
        ("cando",
         "&ldquo;the moon&rdquo; &mdash; the second named lamp, radiating specifically by "
         "night."),
        ("aggi",
         "&ldquo;fire&rdquo; &mdash; the third named lamp, the only one of the first "
         "three able to illuminate both day and night."),
        ("pajjotamuttamo",
         "&ldquo;the best of blazes&rdquo; &mdash; the answer's description of a Buddha, "
         "named as the fourth lamp and the supreme radiance."),
    ],
    text_intro=(
        "The discourse in full: a question about how many lamps light the world, and a "
        "complete, closed list of four. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.26:1.1-1.4"),
        ("p", "&sect;2", "sn1.26:2.1-3.4"),
    ],
    quiz=[
        {"q": "What question does this discourse open with?",
         "opts": [
             "How many lamps are there that light up the world?",
             "How many chains must a mendicant slip to cross the flood?",
             "How many sons does an aristocrat have?",
             "How many days would an ascetic survive?"],
         "correct": 0,
         "expl": "A direct request for an exact count."},
        {"q": "How many lamps does the answer name, and does it leave the count open?",
         "opts": [
             "Four, with the explicit statement that a fifth is not found",
             "An unlimited number",
             "Three, with more implied but unnamed",
             "One only"],
         "correct": 0,
         "expl": "A closed list, not an open-ended catalogue."},
        {"q": "What are the first three lamps named?",
         "opts": [
             "The sun, the moon, and fire",
             "A sword, a flood, and a tangle",
             "Ethics, mind, and wisdom",
             "Home, wife, and children"],
         "correct": 0,
         "expl": "Ordinary physical light sources, each tied to specific circumstances."},
        {"q": "What distinguishes fire from the sun and moon in this list?",
         "opts": [
             "Fire alone illuminates both day and night",
             "Fire alone is described as harmful",
             "Fire alone is said not to exist",
             "Fire is not actually included in the list"],
         "correct": 0,
         "expl": "The sun blazes by day, the moon by night, but fire spans both."},
        {"q": "What is named as the fourth lamp?",
         "opts": [
             "A Buddha, called 'the best of blazes' and 'the supreme radiance'",
             "A fifth physical light source",
             "A deity of the Thirty-Three",
             "No fourth lamp is actually named"],
         "correct": 0,
         "expl": "The list shifts from physical illumination to a person."},
        {"q": "What does 'pajjotamuttamo' mean?",
         "opts": [
             "'The best of blazes'",
             "'The dimmest light'",
             "'A type of deity'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "The answer's description of a Buddha as the fourth and supreme lamp."},
        {"q": "Does this discourse's structure resemble a riddle built on contrast, like several earlier discourses in this vagga?",
         "opts": [
             "No &mdash; it is a direct question answered by a complete, itemized list",
             "Yes, it uses exactly the same contrast structure as SN 1.15",
             "Yes, it uses exactly the same reversal structure as SN 1.21",
             "It uses no question-and-answer structure at all"],
         "correct": 0,
         "expl": "Closer to a catalogue than to a puzzle or reversal."},
        {"q": "What does explicitly stating 'a fifth is not found' accomplish?",
         "opts": [
             "It forecloses reading the list as open-ended, treating the four as literally complete",
             "It suggests there could be many more lamps left unnamed",
             "It contradicts the rest of the verse",
             "It has no particular significance"],
         "correct": 0,
         "expl": "A structural claim that the set of four is genuinely complete."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set at night in a forest",
             "Explicitly set at the Hot Springs Monastery",
             "Explicitly set at a river crossing"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "During what time does the moon radiate, according to the answer?",
         "opts": [
             "By night",
             "By day",
             "Both day and night equally",
             "Neither day nor night"],
         "correct": 0,
         "expl": "Cando rattiṁ virocati &mdash; specifically at night, contrasted with the sun's day."},
    ],
    marginalia=[
        ("A question, direct", [
            "how many lamps",
            "light up the world?",
        ]),
        ("Three, ordinary", [
            "sun by day, moon by night,",
            "fire spanning both",
        ]),
        ("A fourth, supreme", [
            "a Buddha &mdash; the best of blazes,",
            "the supreme radiance",
        ]),
        ("A closed count", [
            "four, and no fifth &mdash;",
            "the list complete",
        ]),
    ],
    further=[
        '<a href="%s/sn1.26/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.25.html">SN 1.25 &middot; A Perfected One</a> &mdash; the '
        "discourse immediately before this one.",
        '<a href="sn-1.14.html">SN 1.14 &middot; Aristocrats</a> &mdash; an earlier '
        "discourse also naming a Buddha as the best among a set of comparisons.",
        "SN 1.27 &middot; Streams &mdash; the next discourse, on where the four elements "
        "find no footing.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.27 — Sarasutta
# --------------------------------------------------------------------------- #
page(
    1, 27, "Sara", "Streams",
    meta_title="SN 1.27 — Streams | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sarasutta — a "
        "question asking where streams recoil and name and form cease, answered by "
        "locating the point where earth, water, fire, and air find no footing. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a compressed question and an equally "
                     "compressed answer"),
        ("Form", "A four-line question, answered by a six-line verse"),
        ("Length", "~45 seconds to read"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; brief in length, "
                       "dense in what it names"),
        ("A thematic echo", "This discourse's question, on where the four elements find "
                            "no footing, closely resembles a theme also explored at "
                            "length in the Kevaḍḍhasutta (DN 11)"),
    ],
    why=(
        "The question compresses three related questions into one: from where do streams "
        "recoil, where does the cycle of existence spin no more, where does name and "
        "form cease without residue? The answer locates all three at a single point: "
        "where water, earth, fire, and air &mdash; the four elements &mdash; have no "
        "footing. From there, it says, the streams recoil; in reference to this point, "
        "the cycle stops; in reference to this same point, name and form cease."),
    guide=[
        ("Three questions, one answer", [
            "The question's three parts &mdash; streams recoiling, the cycle no longer "
            "spinning, name and form ceasing &mdash; might seem to call for three "
            "separate answers. The reply treats them instead as three descriptions of "
            "the same single point, answered together rather than one by one."]),
        ("The four elements, without footing", [
            "<em>Āpo, pathavī, tejo, vāyo</em> &mdash; water, earth, fire, and air, the "
            "four elements (<em>mahābhūta</em>) that in ordinary experience compose the "
            "physical world &mdash; are named as together having &lsquo;no footing&rsquo; "
            "(<em>na gādhati</em>) at exactly the point this verse is describing."]),
        ("A theme met at greater length elsewhere in the canon", [
            "The image of a point where the four elements find no footing closely "
            "resembles a question explored at much greater length in the Kevaḍḍhasutta "
            "(DN 11), where a mendicant's search for where the elements cease without "
            "remainder is eventually redirected back to the Buddha for an answer. This "
            "discourse compresses a related question into six lines what that other "
            "discourse treats as its central narrative concern."]),
        ("Streams, cycle, and name-and-form, together", [
            "The verse's closing structure repeats &lsquo;in reference to this&rsquo; "
            "(<em>ettha</em>) twice, tying the cessation of the cycle of rebirth and the "
            "cessation of name-and-form to the same single reference point already "
            "established by the streams recoiling &mdash; a single locus answering what "
            "the question posed as three."]),
    ],
    terms=[
        ("sara",
         "&ldquo;a stream&rdquo; &mdash; this discourse's title, and the first of three "
         "linked images the opening question asks about."),
        ("vaṭṭa",
         "&ldquo;the cycle&rdquo; &mdash; the round of repeated existence, whose "
         "no-longer-spinning the question asks about as its second concern."),
        ("nāmarūpa",
         "&ldquo;name and form&rdquo; &mdash; mental and physical phenomena together, "
         "whose cessation without residue is the question's third concern, echoing SN "
         "1.23's closing verse."),
        ("āpo pathavī tejo vāyo",
         "&ldquo;water, earth, fire, and air&rdquo; &mdash; the four elements "
         "(<em>mahābhūta</em>), named together as having no footing at the point this "
         "verse describes."),
        ("na gādhati",
         "&ldquo;has no footing, finds no foothold&rdquo; &mdash; the specific condition "
         "the answer names as marking the point where streams, cycle, and name-and-form "
         "all cease."),
    ],
    text_intro=(
        "The discourse in full: three linked questions, answered together at a single "
        "point. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.27:1.1-1.4"),
        ("p", "&sect;2", "sn1.27:2.1-2.6"),
    ],
    quiz=[
        {"q": "What three things does the opening question ask about?",
         "opts": [
             "Where streams recoil, where the cycle spins no more, and where name and form cease",
             "How many lamps light the world",
             "What four things a mendicant should shield the mind from",
             "Who can untangle the human tangle"],
         "correct": 0,
         "expl": "Three questions compressed into a single four-line verse."},
        {"q": "Does the answer treat these three questions as needing three separate answers?",
         "opts": [
             "No &mdash; it locates all three at a single point, answered together",
             "Yes, it gives three completely unrelated answers",
             "It answers only the first question and ignores the rest",
             "It answers only the third question and ignores the rest"],
         "correct": 0,
         "expl": "One locus, described three ways in the question."},
        {"q": "What does the answer name as having 'no footing' at this point?",
         "opts": [
             "The four elements: water, earth, fire, and air",
             "The five aggregates",
             "The four noble truths",
             "The eightfold path"],
         "correct": 0,
         "expl": "Āpo pathavī tejo vāyo &mdash; the four elements, together."},
        {"q": "What discourse elsewhere in the canon explores a closely related theme at greater length?",
         "opts": [
             "The Kevaḍḍhasutta (DN 11)",
             "The Dhammapada",
             "The Visuddhimagga",
             "No related discourse exists elsewhere"],
         "correct": 0,
         "expl": "A mendicant's search for where the elements cease without remainder."},
        {"q": "What does 'nāmarūpa' mean?",
         "opts": [
             "'Name and form' &mdash; mental and physical phenomena together",
             "'A type of deity'",
             "'The world's bait'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "Echoing the same term from SN 1.23's closing verse."},
        {"q": "What word does the verse's closing lines repeat to tie its three concerns together?",
         "opts": [
             "'In reference to this' (ettha)",
             "'Never' (na kadāci)",
             "'Everywhere' (sabbattha)",
             "No repeated word is used"],
         "correct": 0,
         "expl": "Linking the cycle's cessation and name-and-form's cessation to the same point."},
        {"q": "What does 'na gādhati' mean?",
         "opts": [
             "'Has no footing, finds no foothold'",
             "'Flows swiftly forward'",
             "'Burns brightly'",
             "'Is tangled within'"],
         "correct": 0,
         "expl": "The specific condition marking the point this verse describes."},
        {"q": "What does 'vaṭṭa' mean?",
         "opts": [
             "'The cycle,' the round of repeated existence",
             "'A stream'",
             "'A lamp'",
             "'A sword'"],
         "correct": 0,
         "expl": "The second of the question's three linked concerns."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set at a riverbank",
             "Explicitly set at the Hot Springs Monastery",
             "Explicitly set in a marketplace"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "How many elements are named together as having no footing?",
         "opts": [
             "Four",
             "Two",
             "Six",
             "Eight"],
         "correct": 0,
         "expl": "Water, earth, fire, and air &mdash; the four mahābhūta."},
    ],
    marginalia=[
        ("Three questions, compressed", [
            "streams, the cycle,",
            "name and form",
        ]),
        ("One point, answering all three", [
            "where the elements",
            "find no footing",
        ]),
        ("Four elements, grounded nowhere", [
            "water, earth, fire, air &mdash;",
            "na gādhati",
        ]),
        ("A theme met again elsewhere", [
            "echoed at length",
            "in DN 11",
        ]),
    ],
    further=[
        '<a href="%s/sn1.27/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.26.html">SN 1.26 &middot; Lamps</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.23.html">SN 1.23 &middot; A Tangle</a> &mdash; an earlier '
        "discourse in this same vagga, also closing on the cessation of name and form.",
        "SN 1.28 &middot; Affluent &mdash; the next discourse, contrasting the "
        "insatiable wealthy with those who have given up craving.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.28 — Mahaddhanasutta
# --------------------------------------------------------------------------- #
page(
    1, 28, "Mahaddhana", "Affluent",
    meta_title="SN 1.28 — Affluent | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahaddhanasutta "
        "— a question asking who, among the insatiably jealous wealthy, is not avid, "
        "answered by naming those who gave up home, child, and cattle to go forth. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a question describing a social condition, "
                     "answered by naming its exception"),
        ("Form", "A two-verse question, answered by a verse naming who escapes the "
                 "condition it describes"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form, "
                       "echoing this vagga's earlier imagery closely"),
        ("An echo of earlier imagery", "This discourse's answer names home, child, and "
                                       "cattle almost exactly as SN 1.12 and SN 1.19 do, "
                                       "earlier in this collection"),
    ],
    why=(
        "The question describes a social condition rather than asking a riddle: the "
        "affluent and wealthy, even ruling aristocrats, are jealous of one another and "
        "insatiable in sensual pleasure. Among people of such an avid nature, flowing "
        "along the stream of repeated lives, who has actually given up craving? Who in "
        "the world is not avid? The answer names those who gave up their home, their "
        "child, their cattle, and everything they loved to go forth &mdash; having given "
        "up desire, hate, and ignorance, the arahants are the ones, in the whole world, "
        "who are not avid."),
    guide=[
        ("A social diagnosis, not a riddle", [
            "Where several discourses in this vagga open with a puzzle or a paradox, this "
            "one opens with a plain observation about wealth and status: even those with "
            "the most resources remain jealous and insatiable. The verse takes this as a "
            "given, rather than something needing to be proven, before asking who "
            "escapes it."]),
        ("Home, child, and cattle, given up", [
            "The answer's list of what is renounced &mdash; <em>gharaṁ</em> (home), "
            "<em>puttaṁ</em> (child), <em>pasuṁ</em> (cattle) &mdash; closely echoes the "
            "vocabulary of two earlier discourses in this collection: SN 1.12's list of "
            "children and cattle as sources of delight and sorrow, and SN 1.19's coded "
            "list of hut, nest, network, and shackle. This discourse names the same "
            "objects directly, without the riddle-form of either earlier treatment."]),
        ("Wealth and renunciation, contrasted directly", [
            "Unlike SN 1.13's redirection of worldly superlatives toward inward "
            "counterparts, this discourse simply contrasts two groups outright: the "
            "affluent, caught in jealousy and insatiability regardless of their "
            "resources, and those who have renounced resources entirely, described as "
            "alone free of avidity."]),
        ("Not-avid as a description of arahantship", [
            "The final line's claim &mdash; that the arahants, having given up desire, "
            "hate, and dispelled ignorance, &lsquo;are not avid&rsquo; &mdash; ties this "
            "discourse's social observation to the collection's broader account of "
            "liberation: avidity is not corrected by any amount of wealth, but only by "
            "the ending of the underlying causes wealth cannot touch."]),
    ],
    terms=[
        ("mahaddhana",
         "&ldquo;affluent, greatly wealthy&rdquo; &mdash; this discourse's title, "
         "describing the social class the opening question focuses on."),
        ("usuyyanti",
         "&ldquo;are jealous of each other&rdquo; &mdash; the specific condition the "
         "question attributes to the wealthy and the ruling aristocrats alike."),
        ("kāmesu atittā",
         "&ldquo;insatiable in sensual pleasures&rdquo; &mdash; paired with jealousy as "
         "the wealthy's defining trait in the opening verse."),
        ("gharaṁ puttaṁ pasuṁ",
         "&ldquo;home, child, and cattle&rdquo; &mdash; the answer's list of what is "
         "given up, closely echoing SN 1.12 and SN 1.19 earlier in this collection."),
        ("anussukā",
         "&ldquo;avid, restlessly craving&rdquo; &mdash; the condition the question asks "
         "who, if anyone, is free from, answered by naming the arahants."),
    ],
    text_intro=(
        "The discourse in full: a diagnosis of wealth's insatiability, and the naming of "
        "its one exception. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.28:1.1-2.4"),
        ("p", "&sect;2", "sn1.28:3.1-3.6"),
    ],
    quiz=[
        {"q": "What does the opening verse observe about the affluent and wealthy?",
         "opts": [
             "That they are jealous of each other and insatiable in sensual pleasures, regardless of their wealth",
             "That they are entirely free of craving",
             "That only the poor experience jealousy",
             "That wealth automatically produces contentment"],
         "correct": 0,
         "expl": "A social diagnosis presented as given, not as a puzzle to prove."},
        {"q": "What question does the verse then ask?",
         "opts": [
             "Who, among such avid people, has given up craving and is not avid?",
             "How many lamps light the world?",
             "Who can untangle the human tangle?",
             "How is one released from suffering, addressed to a specific ascetic?"],
         "correct": 0,
         "expl": "Naming an exception to the condition just described."},
        {"q": "What does the answer say was given up by those who are not avid?",
         "opts": [
             "Home, child, cattle, and all that they loved",
             "Nothing at all; they retained everything",
             "Only their home, but nothing else",
             "Their monastic robes"],
         "correct": 0,
         "expl": "Gharaṁ puttaṁ pasuṁ &mdash; renunciation named directly."},
        {"q": "Which two earlier discourses in this collection does this list closely echo?",
         "opts": [
             "SN 1.12 and SN 1.19",
             "SN 1.1 and SN 1.2",
             "SN 1.5 and SN 1.6",
             "SN 1.21 and SN 1.22"],
         "correct": 0,
         "expl": "Both used closely related vocabulary of children, cattle, and household ties."},
        {"q": "How does this discourse's treatment of these images differ from SN 1.12 and SN 1.19?",
         "opts": [
             "It names the same objects directly, without either discourse's riddle-form",
             "It uses exactly the same riddle-form as SN 1.19",
             "It denies any connection to either earlier discourse",
             "It reverses the meaning entirely"],
         "correct": 0,
         "expl": "A direct social contrast, not a coded or single-word-substituted verse."},
        {"q": "What three things does the answer say the arahants have given up, beyond home and family?",
         "opts": [
             "Desire, hate, and ignorance",
             "Wealth, fame, and power",
             "Speech, thought, and action entirely",
             "Only ignorance, retaining desire and hate"],
         "correct": 0,
         "expl": "Chandañca dosañca pahāya, avijjaṁ vinodetvā."},
        {"q": "What does 'usuyyanti' mean?",
         "opts": [
             "'Are jealous of each other'",
             "'Are entirely content'",
             "'Have gone forth'",
             "'Have crossed the flood'"],
         "correct": 0,
         "expl": "The specific social condition named in the opening verse."},
        {"q": "Does wealth, according to this discourse, resolve avidity on its own?",
         "opts": [
             "No &mdash; even the wealthiest and most powerful are described as jealous and insatiable",
             "Yes, wealth is described as the direct cure for avidity",
             "The discourse makes no claim about wealth's effect on avidity",
             "Only royal wealth specifically resolves avidity"],
         "correct": 0,
         "expl": "The opening verse explicitly includes ruling aristocrats among the avid."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set in a royal palace",
             "Explicitly set at the Hot Springs Monastery",
             "Explicitly set in the heavenly Garden of Delight"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "What does 'kāmesu atittā' mean?",
         "opts": [
             "'Insatiable in sensual pleasures'",
             "'Completely satisfied with little'",
             "'Free of all sensual desire'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "Paired with jealousy as the wealthy's defining trait."},
    ],
    marginalia=[
        ("A social diagnosis", [
            "the wealthy, jealous,",
            "insatiable regardless",
        ]),
        ("Who is the exception?", [
            "who here has given up craving?",
            "who is not avid?",
        ]),
        ("Home, child, cattle", [
            "given up outright &mdash;",
            "echoing SN 1.12, 1.19",
        ]),
        ("Not by wealth, but by ending", [
            "desire, hate, ignorance",
            "dispelled entirely",
        ]),
    ],
    further=[
        '<a href="%s/sn1.28/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.27.html">SN 1.27 &middot; Streams</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.19.html">SN 1.19 &middot; Little Hut</a> &mdash; this '
        "collection&rsquo;s coded treatment of the same household imagery.",
        "SN 1.29 &middot; Four Wheels &mdash; the next discourse, a riddle describing the "
        "body itself as a burdened cart.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.29 — Catucakkasutta
# --------------------------------------------------------------------------- #
page(
    1, 29, "Catucakka", "Four Wheels",
    meta_title="SN 1.29 — Four Wheels | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Catucakkasutta "
        "— a riddle picturing the body as a cart with four wheels and nine doors, stuffed "
        "full and bound with greed, answered by cutting the harness of desire at its "
        "root. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a riddle addressed to &lsquo;great "
                    "hero,&rsquo; answered directly"),
        ("Form", "A four-line riddle-image, answered by a four-line verse of practical "
                 "instruction"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the riddle's imagery "
                       "is vivid but compressed, and rewards unpacking"),
        ("A body pictured as a vehicle", "This discourse's central image reads the body "
                                         "itself as a heavily laden cart, stuck in mud"),
    ],
    why=(
        "The question pictures something concrete and strange: a thing with four wheels "
        "and nine doors, stuffed full, bound with greed, and born from a bog &mdash; how, "
        "it asks the &lsquo;great hero,&rsquo; will I keep going? The answer does not "
        "explain the image further; it gives an instruction instead: having cut the "
        "strap and harness &mdash; wicked desire and greed &mdash; and having plucked out "
        "craving root and all, that is how you will keep going."),
    guide=[
        ("A vehicle, stuck and overloaded", [
            "The riddle's imagery &mdash; wheels, doors, being stuffed full, being bound, "
            "being born from a bog &mdash; together describe something like an "
            "overburdened cart mired in mud, straining under its own load. The riddle "
            "never states outright that this vehicle is the human body, but its "
            "components map closely onto it."]),
        ("Four wheels and nine doors", [
            "Commentarial tradition reads the four wheels as the body's four postures "
            "&mdash; walking, standing, sitting, lying down &mdash; through which it is "
            "constantly, cyclically moved, and the nine doors as the body's nine "
            "openings: the eyes, ears, nostrils, mouth, and the two lower orifices. This "
            "reading is not stated in the verse itself, but is a widely used gloss for "
            "this same &lsquo;nine-doored&rsquo; body imagery elsewhere in Buddhist "
            "literature."]),
        ("Greed as harness, craving as root", [
            "The answer's practical instruction shifts from picturing the vehicle to "
            "picturing what drives it: a strap and harness, named directly as wicked "
            "desire and greed, and craving, which must be plucked out &lsquo;root and "
            "all&rsquo; (<em>samūlaṁ</em>) rather than merely restrained. The vehicle "
            "itself is not discarded; what pulls it forward through the mud is."]),
        ("A question of continuing, not stopping", [
            "The riddle's own question is not &lsquo;how do I stop&rsquo; but &lsquo;how "
            "will I keep going&rsquo; (<em>kathaṁ jaññaṁ</em>) &mdash; treating the "
            "difficulty as one of a vehicle unable to move forward under its present "
            "load, and the answer as removing what obstructs progress rather than "
            "abandoning the journey."]),
    ],
    terms=[
        ("catucakka",
         "&ldquo;four-wheeled&rdquo; &mdash; this discourse's title, describing the "
         "riddle's central image."),
        ("navadvāra",
         "&ldquo;nine-doored&rdquo; &mdash; the riddle's second descriptive feature, "
         "commonly glossed elsewhere in Buddhist literature as the body's nine physical "
         "openings."),
        ("paṅkajāta",
         "&ldquo;born from a bog, arisen from mud&rdquo; &mdash; the riddle's description "
         "of the vehicle's origin, contributing to its image of being mired and "
         "burdened."),
        ("yottañca varattañca chetvā",
         "&ldquo;having cut the strap and harness&rdquo; &mdash; the answer's opening "
         "instruction, naming wicked desire and greed as what must be severed."),
        ("samūlaṁ taṇhaṁ abbuyha",
         "&ldquo;having plucked out craving, root and all&rdquo; &mdash; the answer's "
         "second instruction, treating partial restraint as insufficient."),
    ],
    text_intro=(
        "The discourse in full: a riddle picturing the body as an overburdened cart, and "
        "an instruction for how it moves forward. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.29:1.1-1.4"),
        ("p", "&sect;2", "sn1.29:2.1-2.4"),
    ],
    quiz=[
        {"q": "What image does the opening riddle describe?",
         "opts": [
             "Something with four wheels and nine doors, stuffed full, bound with greed, born from a bog",
             "A sword striking its target",
             "A garden of heavenly delight",
             "A tangle of matted hair"],
         "correct": 0,
         "expl": "An overburdened, mired vehicle, closely mapping onto the body."},
        {"q": "According to commentarial tradition, what do the 'four wheels' represent?",
         "opts": [
             "The body's four postures: walking, standing, sitting, and lying down",
             "The four noble truths",
             "The four elements",
             "Four literal cart wheels, with no further meaning"],
         "correct": 0,
         "expl": "A widely used gloss, though not stated explicitly in the verse itself."},
        {"q": "What do the 'nine doors' commonly represent, per the same tradition?",
         "opts": [
             "The body's nine physical openings: eyes, ears, nostrils, mouth, and two lower orifices",
             "Nine specific monasteries",
             "The nine fetters",
             "Nine deities of the Thirty-Three"],
         "correct": 0,
         "expl": "A common gloss for 'nine-doored' body imagery elsewhere in Buddhist literature."},
        {"q": "What does the answer instruct cutting?",
         "opts": [
             "The strap and harness, named as wicked desire and greed",
             "The four wheels themselves",
             "The nine doors themselves",
             "Nothing needs to be cut"],
         "correct": 0,
         "expl": "Yottañca varattañca chetvā &mdash; what drives the vehicle, not the vehicle itself."},
        {"q": "How thoroughly does the answer say craving should be removed?",
         "opts": [
             "Root and all (samūlaṁ), not merely restrained",
             "Only partially, leaving some craving intact",
             "Craving does not need to be addressed at all",
             "Only for one day at a time"],
         "correct": 0,
         "expl": "Samūlaṁ taṇhaṁ abbuyha &mdash; complete removal, not partial restraint."},
        {"q": "What question does the riddle itself ask?",
         "opts": [
             "How will I keep going?",
             "How do I stop moving entirely?",
             "How many wheels does the cart have?",
             "Who built this vehicle?"],
         "correct": 0,
         "expl": "Kathaṁ jaññaṁ &mdash; a question about continuing forward, not halting."},
        {"q": "What does 'paṅkajāta' mean?",
         "opts": [
             "'Born from a bog, arisen from mud'",
             "'Born from fire'",
             "'Born from a lotus with no impurity'",
             "'Born from a mountain'"],
         "correct": 0,
         "expl": "Part of the riddle's image of being mired and burdened."},
        {"q": "Is the vehicle itself discarded in the answer's instruction?",
         "opts": [
             "No &mdash; what pulls it forward through the mud is removed, not the vehicle itself",
             "Yes, the vehicle is explicitly destroyed",
             "The answer does not mention the vehicle at all",
             "The vehicle is replaced with an entirely different one"],
         "correct": 0,
         "expl": "The harness and craving are cut; the image of the vehicle persists."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set on a road",
             "Explicitly set at the Hot Springs Monastery",
             "Explicitly set in a marketplace"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
        {"q": "Who is the riddle addressed to?",
         "opts": [
             "A 'great hero' (mahāvīra)",
             "A specific named king",
             "A group of deities",
             "No addressee is named"],
         "correct": 0,
         "expl": "The riddle's own vocative, addressed within the verse itself."},
    ],
    marginalia=[
        ("A vehicle, mired", [
            "four wheels, nine doors,",
            "stuffed full, born from a bog",
        ]),
        ("What the wheels and doors mean", [
            "four postures, nine openings &mdash;",
            "commentary&rsquo;s reading",
        ]),
        ("Cut the harness", [
            "wicked desire and greed,",
            "severed at the strap",
        ]),
        ("Root and all", [
            "craving plucked out entirely,",
            "not merely restrained",
        ]),
    ],
    further=[
        '<a href="%s/sn1.29/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.28.html">SN 1.28 &middot; Affluent</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.17.html">SN 1.17 &middot; Hard to Do</a> &mdash; an earlier '
        "discourse in this collection also using a concrete image for disciplined "
        "practice.",
        "SN 1.30 &middot; Antelope Calves &mdash; the next discourse, this vagga's last, "
        "closing on a vivid physical description of the Buddha himself.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.30 — Eṇijaṅghasutta (closes the Sattivagga)
# --------------------------------------------------------------------------- #
page(
    1, 30, "Eṇijaṅgha", "Antelope Calves",
    meta_title="SN 1.30 — Antelope Calves | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Eṇijaṅghasutta "
        "— a vivid physical description of the Buddha as lean, alone, and lion-like, "
        "asked how one is released from suffering, and answered with the world's five "
        "kinds of sensual stimulation plus the mind as a sixth. Closes the Sattivagga. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; questioners addressing the Buddha directly by "
                    "physical description, and the Buddha's reply"),
        ("Form", "A six-line description and question, answered by a four-line verse, "
                 "with two further blank verses left untranslated"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; vivid and direct, "
                       "closing on a compact doctrinal point"),
        ("Closing this vagga", "The tenth and last discourse of the Sattivagga, whose own "
                               "closing colophon names the vagga as finished"),
    ],
    why=(
        "This discourse opens with some of the most physically vivid language used for "
        "the Buddha anywhere in this collection: lean, with antelope calves, not greedy, "
        "eating little, a giant wandering alone like a lion, unconcerned for sensual "
        "pleasures. Having described him this way, the questioners ask directly: how is "
        "one released from all suffering? The answer is compact: the world has five kinds "
        "of sensual stimulation, and the mind itself is said to be a sixth; discard "
        "desire for these, and you are released from all suffering."),
    guide=[
        ("A body described, not merely a teaching", [
            "Unlike most discourses in this collection, which move quickly to doctrine or "
            "riddle, this one lingers on physical description first: slender legs like an "
            "antelope's, leanness, restraint in eating, solitary wandering compared "
            "specifically to a lion rather than a herd animal. The Buddha's asceticism is "
            "made visible before it is discussed."]),
        ("Five familiar senses, and a sixth", [
            "The answer names the world's <em>pañca kāmaguṇā</em>, five kinds of sensual "
            "stimulation &mdash; the classic list of sights, sounds, smells, tastes, and "
            "touch &mdash; and then adds <em>mano</em>, the mind itself, as "
            "<em>chaṭṭha</em>, a sixth. Release from suffering is described as "
            "discarding desire across all six, not only the five ordinarily associated "
            "with the physical senses."]),
        ("A vagga whose name comes from its opening image", [
            "As with SN 1.21, this vagga's opening discourse, the Sattivagga takes its "
            "name from an image named at a discourse's start rather than its end &mdash; "
            "here, however, it is this vagga's closing discourse, not its first, that "
            "supplies its own vivid, separate image, one that does not itself name the "
            "vagga."]),
        ("An untranslated close", [
            "As with SN 1.10 and SN 1.20, this discourse is followed in the source text "
            "by a closing colophon and a mnemonic verse (<em>uddāna</em>) naming the "
            "Sattivagga as finished and listing its ten titles in order &mdash; left "
            "untranslated in this edition, and described here rather than quoted, "
            "following this project's established practice."]),
        ("Named for the opening discourse, closed by the tenth", [
            "It is worth noting explicitly that this vagga's name, Sattivagga, comes from "
            "SN 1.21's opening image of a sword, not from this closing discourse's own "
            "striking image of antelope calves and a lion's solitary gait &mdash; a "
            "reminder that a vivid closing image does not automatically become a vagga's "
            "namesake, unlike what happened with the Naḷavagga before it."]),
    ],
    terms=[
        ("eṇijaṅgha",
         "&ldquo;antelope calves&rdquo; &mdash; this discourse's title and opening "
         "physical description, naming the Buddha's slender legs."),
        ("sīhaṁvekacaraṁ",
         "&ldquo;wandering alone like a lion&rdquo; &mdash; the questioners' description "
         "of the Buddha's solitary manner, comparing him to a predator rather than a herd "
         "animal."),
        ("pañca kāmaguṇā",
         "the world's &ldquo;five kinds of sensual stimulation&rdquo; &mdash; the "
         "classic list of pleasing sights, sounds, smells, tastes, and touch."),
        ("mano chaṭṭha",
         "&ldquo;the mind as a sixth&rdquo; &mdash; the answer's addition to the five "
         "senses, extending the scope of what desire must be discarded from."),
        ("chandaṁ virājetvā",
         "&ldquo;having discarded desire&rdquo; &mdash; the specific action the verse "
         "names as producing release from all suffering, applied across all six."),
    ],
    text_intro=(
        "The discourse in full, with its untranslated closing colophon and mnemonic "
        "verse described rather than quoted, as with SN 1.10 and SN 1.20. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha, described"),
        ("p", "&sect;1", "sn1.30:1.1-1.6"),
        ("h3", "An answer in six senses"),
        ("p", "&sect;2", "sn1.30:2.1-2.4"),
    ],
    quiz=[
        {"q": "How is the Buddha physically described at the start of this discourse?",
         "opts": [
             "Lean, with antelope calves, not greedy, eating little, wandering alone like a lion",
             "As a wealthy king surrounded by attendants",
             "As invisible and without physical form",
             "As young and inexperienced"],
         "correct": 0,
         "expl": "Some of the most physically vivid language used for the Buddha in this collection."},
        {"q": "What question do the questioners ask after this description?",
         "opts": [
             "How is one released from all suffering?",
             "How many lamps light the world?",
             "How many wheels does the body have?",
             "Who can untangle the human tangle?"],
         "correct": 0,
         "expl": "A direct question following the physical description."},
        {"q": "What does the answer name as the world's kinds of sensual stimulation?",
         "opts": [
             "Five: sights, sounds, smells, tastes, and touch",
             "Three: sight, sound, and touch only",
             "Seven, including thought and memory",
             "None; sensual stimulation is denied entirely"],
         "correct": 0,
         "expl": "Pañca kāmaguṇā &mdash; the classic list of five."},
        {"q": "What does the answer add as a sixth item, beyond the five senses?",
         "opts": [
             "The mind itself (mano)",
             "A sixth physical sense organ",
             "Wealth",
             "Family relationships"],
         "correct": 0,
         "expl": "Manochaṭṭhā pavaditā &mdash; the mind is said to be a sixth."},
        {"q": "What does the verse say produces release from all suffering?",
         "opts": [
             "Discarding desire (chandaṁ virājetvā) for all six",
             "Acquiring more of all six",
             "Ignoring the question entirely",
             "Physical asceticism alone, without addressing desire"],
         "correct": 0,
         "expl": "The specific action named as producing release."},
        {"q": "What animal is the Buddha compared to in his manner of wandering?",
         "opts": [
             "A lion, wandering alone",
             "An antelope, moving in herds",
             "An elephant, traveling in groups",
             "No animal comparison is made for his manner of wandering"],
         "correct": 0,
         "expl": "Sīhaṁvekacaraṁ &mdash; a predator's solitary gait, not a herd animal's."},
        {"q": "Does this vagga's name, Sattivagga, come from this closing discourse's imagery?",
         "opts": [
             "No &mdash; it comes from SN 1.21's opening sword image, not from this discourse",
             "Yes, it comes directly from the antelope-calves image",
             "It comes from the lion comparison specifically",
             "The vagga has no fixed source for its name"],
         "correct": 0,
         "expl": "Unlike the Naḷavagga, this vagga's namesake image is at its start, not its end."},
        {"q": "What follows this discourse in the source text, left untranslated?",
         "opts": [
             "A closing colophon and mnemonic verse listing the vagga's ten discourse titles",
             "An entirely new discourse beginning immediately",
             "A prose commentary explaining the six senses",
             "Nothing follows; the source text ends abruptly"],
         "correct": 0,
         "expl": "The same pattern already seen at SN 1.10 and SN 1.20."},
        {"q": "What is this discourse's position within the Sattivagga?",
         "opts": [
             "It is the tenth and last discourse, closing the vagga",
             "It is the vagga's first discourse",
             "It belongs to the Nandanavagga, not the Sattivagga",
             "It has no fixed position"],
         "correct": 0,
         "expl": "This discourse's own closing colophon marks the Sattivagga as finished."},
        {"q": "What does 'chandaṁ virājetvā' mean?",
         "opts": [
             "'Having discarded desire'",
             "'Having acquired desire'",
             "'Having ignored the question'",
             "'Having wandered alone'"],
         "correct": 0,
         "expl": "The specific action the verse names as producing release from suffering."},
    ],
    marginalia=[
        ("A body, described", [
            "antelope calves, lean,",
            "alone like a lion",
        ]),
        ("A question, direct", [
            "how is one released",
            "from all suffering?",
        ]),
        ("Five senses, and a sixth", [
            "sight, sound, smell, taste, touch &mdash;",
            "and the mind besides",
        ]),
        ("The Sattivagga closes", [
            "ten discourses complete;",
            "named for its opening sword",
        ]),
    ],
    further=[
        '<a href="%s/sn1.30/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.29.html">SN 1.29 &middot; Four Wheels</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.21.html">SN 1.21 &middot; A Sword</a> &mdash; this vagga&rsquo;s '
        "opening discourse, and the true source of its name.",
        '<a href="sn-1.20.html">SN 1.20 &middot; With Samiddhi</a> &mdash; the discourse '
        "that closed the previous vagga, the Nandanavagga.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.31 — Sabbhisutta (opens the Satullapakāyikavagga)
# --------------------------------------------------------------------------- #
page(
    1, 31, "Sabbhi", "Virtuous",
    meta_title="SN 1.31 — Virtuous | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sabbhisutta — "
        "six deities of the Satullapakāyikā host each complete the same refrain on "
        "associating with the virtuous, and the Buddha adds a seventh completion of his "
        "own. Opens the Satullapakāyikavagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; several deities of the "
                    "Satullapakāyikā host arrive together, rather than the single deity "
                    "of most earlier discourses"),
        ("Speakers", "Six deities in turn, each completing a shared refrain, then the "
                    "Buddha, adding a seventh completion of his own"),
        ("Form", "A refrain repeated six times with a new closing line each time, capped "
                 "by a final round from the Buddha and a request to judge who spoke best"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple in each "
                       "individual verse, but this collection's first sustained multi-"
                       "speaker structure"),
        ("Opening this vagga", "The first discourse of the Satullapakāyikavagga "
                               "(&lsquo;the Chapter on the Satullapa Group&rsquo;), named "
                               "for this recurring host of deities"),
    ],
    why=(
        "This discourse introduces a structure new to this collection: rather than one "
        "deity and the Buddha exchanging a single pair of verses, several deities of the "
        "Satullapakāyikā host arrive together, and one by one each recites the same "
        "three-line refrain &mdash; &lsquo;associate only with the virtuous, try to get "
        "close to the virtuous, understanding the true teaching of the good&rsquo; "
        "&mdash; completed by a different fourth line each time. After six deities have "
        "spoken, one asks the Buddha directly who has spoken best. His answer neither "
        "ranks nor dismisses any of them: you've all spoken well in your own way &mdash; "
        "and he offers a seventh completion of the same refrain."),
    guide=[
        ("A shared refrain, six different endings", [
            "Every deity's verse opens identically: associate with the virtuous, draw "
            "close to them, understand their true teaching. What changes each time is "
            "only the fourth line, naming a different specific benefit &mdash; things "
            "improving, wisdom gained independently, freedom from grief, standing out "
            "among relatives, a good rebirth, and a happy life."]),
        ("A question the Buddha declines to answer competitively", [
            "When asked directly who spoke best, the Buddha's reply refuses the framing "
            "of the question: &lsquo;you've all spoken well in your own way.&rsquo; Rather "
            "than ranking six true statements against one another, he treats them as "
            "compatible facets of a single underlying claim."]),
        ("A seventh line, not a correction", [
            "The Buddha's own contribution keeps the shared refrain and adds a seventh "
            "ending &mdash; &lsquo;you're released from all suffering&rsquo; &mdash; a "
            "claim more comprehensive than, but not contradicting, any of the six the "
            "deities already offered. It reads as completing the list rather than "
            "correcting it."]),
        ("A new host, named for this whole vagga", [
            "The Satullapakāyikā deities introduced here return across several more "
            "discourses in this vagga, which takes its own name from this recurring "
            "group &mdash; a fourth pattern for how a vagga acquires its name, following "
            "an opening image (Sattivagga), an opening setting (Nandanavagga), and a "
            "closing image (Naḷavagga)."]),
    ],
    terms=[
        ("satullapakāyikā devatā",
         "&ldquo;deities of the Satullapakāyikā host&rdquo; &mdash; the recurring group "
         "of deities this vagga is named after, appearing together rather than singly."),
        ("sabbhi",
         "&ldquo;with the virtuous, with the good&rdquo; &mdash; the refrain's central "
         "instruction, and this discourse's title."),
        ("saddhammamaññāya",
         "&ldquo;understanding the true teaching&rdquo; &mdash; the shared refrain's "
         "third line, present unchanged in every deity's verse."),
        ("vimuccati sabbadukkhā",
         "&ldquo;you're released from all suffering&rdquo; &mdash; the Buddha's own, "
         "seventh completion of the shared refrain."),
        ("subhāsitaṁ",
         "&ldquo;spoken well&rdquo; &mdash; the term the deities use asking the Buddha to "
         "judge among them, and that his answer applies to all six equally."),
    ],
    text_intro=(
        "The discourse in full: six deities complete a shared refrain, and the Buddha "
        "adds a seventh completion. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Several deities arrive together"),
        ("p", "&sect;1", "sn1.31:1.1-1.4"),
        ("h3", "Six completions of one refrain"),
        ("p", "&sect;2", "sn1.31:2.1-2.4"),
        ("p", "&sect;3", "sn1.31:3.1-4.4"),
        ("p", "&sect;4", "sn1.31:5.1-6.4"),
        ("p", "&sect;5", "sn1.31:7.1-8.4"),
        ("p", "&sect;6", "sn1.31:9.1-10.4"),
        ("p", "&sect;7", "sn1.31:11.1-12.4"),
        ("h3", "A question, and a seventh completion"),
        ("p", "&sect;8", "sn1.31:13.1-16.2"),
    ],
    quiz=[
        {"q": "What structure does this discourse introduce, new to this collection?",
         "opts": [
             "Several deities arriving together, each completing a shared refrain in turn",
             "A single deity asking a riddle answered by the Buddha",
             "A dialogue between two named mendicants only",
             "A silent exchange with no verses at all"],
         "correct": 0,
         "expl": "This collection's first sustained multi-speaker structure."},
        {"q": "What three lines does every deity's verse share?",
         "opts": [
             "Associate with the virtuous, get close to them, understand their true teaching",
             "Cross the flood, drop the world's bait, walk in the rough",
             "Give up conceit, cut the fetters, cross Death's dominion",
             "No lines are shared; each verse is entirely different"],
         "correct": 0,
         "expl": "The refrain repeated identically across all speakers."},
        {"q": "What changes between each deity's verse?",
         "opts": [
             "Only the fourth line, naming a different specific benefit each time",
             "The entire verse changes completely each time",
             "Only the setting changes",
             "Nothing changes at all between speakers"],
         "correct": 0,
         "expl": "A single varying line, capping an otherwise fixed refrain."},
        {"q": "How does the Buddha answer when asked who spoke best?",
         "opts": [
             "He says all six spoke well in their own way, declining to rank them",
             "He names one deity as clearly superior",
             "He says none of them spoke correctly",
             "He refuses to answer the question at all"],
         "correct": 0,
         "expl": "A refusal of the question's competitive framing."},
        {"q": "What does the Buddha's own seventh completion of the refrain add?",
         "opts": [
             "'You're released from all suffering'",
             "'You should never speak to anyone'",
             "'Wealth is the true measure of virtue'",
             "Nothing; he declines to add his own ending"],
         "correct": 0,
         "expl": "A more comprehensive claim than, but not contradicting, the six already given."},
        {"q": "What group of deities is introduced in this discourse?",
         "opts": [
             "The Satullapakāyikā host, who recur across this vagga",
             "The Pure Abode deities",
             "The fault-finding deities",
             "The deities of the Thirty-Three"],
         "correct": 0,
         "expl": "The group this whole vagga is named after."},
        {"q": "How does this vagga's naming pattern compare to earlier vaggas?",
         "opts": [
             "It is named for a recurring group of deities, a fourth distinct naming pattern in this collection",
             "It is named for its closing image, like the Naḷavagga",
             "It is named for its opening image, like the Sattivagga",
             "It has no name at all"],
         "correct": 0,
         "expl": "A new pattern, distinct from opening image, opening setting, or closing image."},
        {"q": "What does 'saddhammamaññāya' mean?",
         "opts": [
             "'Understanding the true teaching'",
             "'Rejecting the teaching entirely'",
             "'A type of deity'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "The shared refrain's unchanging third line."},
        {"q": "How many deities speak before the Buddha adds his own completion?",
         "opts": [
             "Six",
             "Two",
             "Ten",
             "One"],
         "correct": 0,
         "expl": "Six varying endings, then the Buddha's seventh."},
        {"q": "What is 'subhāsitaṁ'?",
         "opts": [
             "'Spoken well' &mdash; the term used asking the Buddha to judge among the deities' verses",
             "'Spoken poorly'",
             "'Never spoken'",
             "'A type of riddle'"],
         "correct": 0,
         "expl": "The Buddha's answer applies this term to all six speakers equally."},
    ],
    marginalia=[
        ("Several deities, together", [
            "not one, but many &mdash;",
            "a new kind of exchange",
        ]),
        ("One refrain, six endings", [
            "associate with the virtuous &mdash;",
            "six different benefits named",
        ]),
        ("Who spoke best?", [
            "all of you, in your own way,",
            "says the Buddha",
        ]),
        ("A seventh completion", [
            "released from all suffering &mdash;",
            "not a correction, but a capstone",
        ]),
    ],
    further=[
        '<a href="%s/sn1.31/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.30.html">SN 1.30 &middot; Antelope Calves</a> &mdash; the '
        "discourse that closed the previous vagga, the Sattivagga.",
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this '
        "collection&rsquo;s opening discourse.",
        "SN 1.32 &middot; Stinginess &mdash; the next discourse, the same multi-deity "
        "structure applied to the theme of giving.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.32 — Maccharisutta
# --------------------------------------------------------------------------- #
page(
    1, 32, "Macchari", "Stinginess",
    meta_title="SN 1.32 — Stinginess | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Maccharisutta — "
        "four deities speak in turn on generosity and stinginess, the Buddha values a "
        "modest ethical life over grand sacrifice, and a deity presses him on why. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; several Satullapakāyikā "
                    "deities, as at SN 1.31"),
        ("Speakers", "Four deities in turn, then the Buddha, then a further exchange "
                    "between a deity and the Buddha probing his answer"),
        ("Form", "Four independent verses on giving, the Buddha's own verse, and a "
                 "follow-up question-and-answer extending the discourse further"),
        ("Length", "~2.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the closing exchange "
                       "on sacrifice carries real ethical weight"),
        ("A pointed critique", "The Buddha's answer explicitly ranks a modest, ethical "
                               "life above &lsquo;a hundred thousand people making a "
                               "thousand sacrifices&rsquo;"),
    ],
    why=(
        "Four deities speak in turn on stinginess and giving, each adding a distinct "
        "angle: negligence as the simple cause of withheld gifts; the miser's fear "
        "backfiring into the very hunger and thirst it dreaded; small gifts from those "
        "who have little outweighing withheld surplus from those who have much; and "
        "giving what's hard to give as what actually distinguishes the virtuous from the "
        "wicked. Asked who spoke best, the Buddha adds a verse ranking one person living "
        "rightly on little above a hundred thousand people performing lavish sacrifices "
        "&mdash; and when a deity presses him on why, he explains: because such "
        "sacrifices are funded by violence."),
    guide=[
        ("Four deities, four distinct angles on giving", [
            "Where SN 1.31's deities varied only a single closing line of a shared "
            "refrain, this discourse's four deities offer genuinely different arguments: "
            "generosity as simple opportunity not taken, generosity as protection against "
            "a feared outcome that withholding actually causes, generosity from scarcity "
            "outweighing withheld abundance, and generosity as specifically what is hard "
            "to do &mdash; the real measure of virtue, not merely its ordinary practice."]),
        ("A fear that creates what it fears", [
            "The second deity's verse names a specific irony: the miser who withholds out "
            "of fear of future want brings about exactly that want, in this world and the "
            "next, through the withholding itself &mdash; a structure of self-defeating "
            "avoidance echoing SN 1.22's image of harm returning to its source."]),
        ("A pointed ranking of sacrifice below ethical life", [
            "Asked who spoke best, the Buddha's own verse does something none of the four "
            "deities attempted: it explicitly ranks &lsquo;a hundred thousand people "
            "making a thousand sacrifices&rsquo; below a single person living rightly on "
            "gleanings, or supporting a partner with little. This directly challenges the "
            "assumed value of large-scale ritual sacrifice, a theme this collection meets "
            "again elsewhere in the broader canon's critiques of Brahminical sacrifice."]),
        ("Pressed for a reason, and given one", [
            "Rather than let this ranking stand unexplained, a deity asks directly why "
            "such an abundant, magnificent sacrifice fails to equal a moral person's "
            "gift. The Buddha's answer is specific, not general: such sacrifices are "
            "funded &lsquo;after slaying, killing, and tormenting&rsquo; &mdash; the "
            "disqualification is about the violence embedded in how the offering was "
            "obtained, not merely about its scale or ritual form."]),
    ],
    terms=[
        ("macchariya",
         "&ldquo;stinginess&rdquo; &mdash; this discourse's title, and the first "
         "deity's named cause for gifts not given."),
        ("dāna",
         "&ldquo;giving, a gift&rdquo; &mdash; the practice all four deities and the "
         "Buddha discuss from different angles."),
        ("porāṇaka",
         "&ldquo;ancient, of long standing&rdquo; &mdash; how the third deity's verse "
         "describes its own teaching, an unusual explicit claim to inherited wisdom "
         "rather than fresh insight."),
        ("yañña",
         "&ldquo;sacrifice&rdquo; &mdash; the large-scale ritual offering the Buddha's "
         "verse ranks below one moral person's modest gift."),
        ("hantvā chinditvā chetvā",
         "&ldquo;after slaying, killing, and tormenting&rdquo; &mdash; the Buddha's "
         "specific answer for why such sacrifices fail to equal a moral gift's value."),
    ],
    text_intro=(
        "The discourse in full: four deities on giving, the Buddha's ranking of ethical "
        "life above sacrifice, and his reason why. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Deities arrive; a first verse on stinginess"),
        ("p", "&sect;1", "sn1.32:1.1-1.3"),
        ("p", "&sect;2", "sn1.32:2.1-2.4"),
        ("h3", "A second deity: fear that creates what it fears"),
        ("p", "&sect;3", "sn1.32:3.1-5.4"),
        ("h3", "A third deity: what's given from little"),
        ("p", "&sect;4", "sn1.32:6.1-8.4"),
        ("h3", "A fourth deity: what's hard to give"),
        ("p", "&sect;5", "sn1.32:9.1-11.4"),
        ("h3", "A question, and the Buddha's ranking"),
        ("p", "&sect;6", "sn1.32:12.1-14.4"),
        ("h3", "A deity presses further"),
        ("p", "&sect;7", "sn1.32:15.1-16.4"),
        ("p", "&sect;8", "sn1.32:17.1-18.2"),
    ],
    quiz=[
        {"q": "What does the first deity name as the cause of gifts not given?",
         "opts": [
             "Stinginess and negligence",
             "Poverty alone",
             "A lack of merit already accumulated",
             "The Buddha's own instruction not to give"],
         "correct": 0,
         "expl": "Macchariyā ca pamādā ca &mdash; the discourse's opening claim."},
        {"q": "What irony does the second deity's verse describe?",
         "opts": [
             "A miser's fear of hunger and thirst is brought about by their own withholding",
             "Generosity always leads to poverty",
             "Fear has no relationship to giving at all",
             "Only the wealthy ever experience hunger"],
         "correct": 0,
         "expl": "The very thing feared comes to pass through the withholding itself."},
        {"q": "What does the third deity's verse claim about gifts given from little?",
         "opts": [
             "They are multiplied a thousand times, unlike withheld abundance from those who have much",
             "They are worthless compared to large donations",
             "They should never be given at all",
             "They only benefit the giver, never anyone else"],
         "correct": 0,
         "expl": "An offering given from little is multiplied a thousand times."},
        {"q": "What does the fourth deity identify as the true measure of virtue in giving?",
         "opts": [
             "Giving what's hard to give, doing what's hard to do",
             "Giving only what is easy and convenient",
             "Never giving under any circumstances",
             "Giving only to relatives"],
         "correct": 0,
         "expl": "Dukkaraṁ dadanti dukkaraṁ karonti &mdash; distinguishing the virtuous from the wicked."},
        {"q": "What does the Buddha's own verse rank above 'a hundred thousand people making a thousand sacrifices'?",
         "opts": [
             "One person living rightly on gleanings, or supporting a partner with little",
             "A single wealthy king's donation",
             "Nothing; he says nothing can exceed such sacrifices",
             "A thousand additional sacrifices"],
         "correct": 0,
         "expl": "A direct and pointed ranking of modest ethical life above lavish ritual."},
        {"q": "Why, according to the Buddha's explanation, does such a sacrifice fail to equal a moral gift?",
         "opts": [
             "Because it is funded through slaying, killing, and tormenting",
             "Because it involves too much wealth",
             "Because it takes place in the wrong location",
             "Because too many people are involved"],
         "correct": 0,
         "expl": "The disqualification concerns the violence in how the offering was obtained."},
        {"q": "What does 'porāṇaka' mean, and where is it used?",
         "opts": [
             "'Ancient, of long standing' &mdash; how the third deity describes their own teaching",
             "'Brand new' &mdash; describing a teaching never heard before",
             "'False' &mdash; describing a teaching to be rejected",
             "It does not appear in this discourse"],
         "correct": 0,
         "expl": "An unusual explicit claim to inherited wisdom."},
        {"q": "How does this discourse's structure compare to SN 1.31?",
         "opts": [
             "The four deities offer genuinely different arguments, unlike SN 1.31's single varying refrain-line",
             "It uses exactly the same shared refrain as SN 1.31",
             "Only one deity speaks, unlike SN 1.31's six",
             "No deities speak at all in this discourse"],
         "correct": 0,
         "expl": "Four distinct angles on giving, rather than one refrain completed six ways."},
        {"q": "What does 'yañña' mean?",
         "opts": [
             "'Sacrifice' &mdash; the large-scale ritual the Buddha's verse ranks below modest ethical living",
             "'Stinginess'",
             "'A type of deity'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "The specific target of the Buddha's ranking and explanation."},
        {"q": "Does a deity accept the Buddha's ranking without question?",
         "opts": [
             "No &mdash; a deity presses him further, asking directly why the ranking holds",
             "Yes, every deity immediately agrees without further discussion",
             "The deities leave in anger without responding",
             "No deity speaks again after the Buddha's verse"],
         "correct": 0,
         "expl": "A genuine follow-up question, met with a specific rather than general answer."},
    ],
    marginalia=[
        ("Four deities, four angles", [
            "negligence, fear,",
            "little given, hard given",
        ]),
        ("A fear, self-fulfilling", [
            "what the miser dreads",
            "comes from withholding itself",
        ]),
        ("Sacrifice, outranked", [
            "a hundred thousand rituals &mdash;",
            "one right life outweighs them",
        ]),
        ("Why: the violence beneath it", [
            "funded by slaying and killing,",
            "tearful, not equal to a moral gift",
        ]),
    ],
    further=[
        '<a href="%s/sn1.32/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.31.html">SN 1.31 &middot; Virtuous</a> &mdash; the discourse '
        "immediately before this one, and this vagga&rsquo;s opening discourse.",
        '<a href="sn-1.22.html">SN 1.22 &middot; Impact</a> &mdash; an earlier discourse '
        "on harm returning to its own source.",
        "SN 1.33 &middot; Good &mdash; the next discourse, six deities building a single "
        "cumulative list on giving well.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.33 — Sādhusutta
# --------------------------------------------------------------------------- #
page(
    1, 33, "Sādhu", "Good",
    meta_title="SN 1.33 — Good | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sādhusutta — six "
        "deities build a single cumulative list of what makes giving good, from mere "
        "generosity to giving intelligently and non-harming, before the Buddha ranks "
        "teaching above all giving. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; several Satullapakāyikā "
                    "deities, as at SN 1.31 and SN 1.32"),
        ("Speakers", "Six deities in turn, each repeating and extending the previous "
                     "deity's list, then the Buddha"),
        ("Form", "A cumulative refrain, each speaker adding one further qualification to "
                 "everything said before, closed by the Buddha's own capping verse"),
        ("Length", "~2.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the cumulative "
                       "structure rewards tracking what each new deity actually adds"),
        ("A third structure within three discourses", "Distinct again from both SN 1.31's "
                                                       "single varying line and SN 1.32's "
                                                       "four independent arguments"),
    ],
    why=(
        "Six deities speak in sequence, each one repeating everything the deities before "
        "them have already said and adding exactly one further qualification: giving is "
        "good; even giving from little is good; giving out of faith is good; giving "
        "legitimately earned wealth is good; giving intelligently, to those worthy of it, "
        "is good; and restraint toward living creatures is good. By the sixth deity, a "
        "discourse that began simply praising generosity has expanded into something "
        "closer to a full ethical program. The Buddha's own closing verse then ranks "
        "something above every form of giving discussed: a passage of teaching."),
    guide=[
        ("A cumulative list, not a set of independent claims", [
            "Unlike SN 1.32's four deities, each making a distinct and separable "
            "argument, this discourse's six deities build a single expanding statement "
            "&mdash; each new speaker repeats every qualification already given before "
            "adding their own, so the sixth deity's full verse contains all six "
            "qualifications at once."]),
        ("Giving and warfare, compared", [
            "The third deity's verse makes a startling comparison: &lsquo;giving and "
            "warfare are similar, they say, for even a few of the good may conquer the "
            "many.&rsquo; The point is not violence but quality over quantity &mdash; a "
            "small amount given with genuine faith is treated as more decisive than a "
            "large amount given without it, the way a disciplined few can defeat a "
            "larger, less committed force."]),
        ("From giving to non-harming", [
            "The list's final addition marks a real shift: restraint toward living "
            "creatures is not, strictly, a form of giving at all, but a form of "
            "non-harming (<em>ahiṁsā</em>). By the sixth deity, this discourse has "
            "expanded from dāna specifically into a broader account of ethical conduct, "
            "without announcing that expansion directly."]),
        ("Virtue without fear as its motive", [
            "The sixth deity's verse makes a subtle distinction easy to miss: one who "
            "avoids harm only from fear of others' blame would, if blame were the whole "
            "story, deserve to be called a coward rather than praised as virtuous. "
            "Genuine virtue, the verse insists, avoids harm for its own sake, not merely "
            "to escape social consequence."]),
        ("Teaching ranked above every gift named", [
            "The Buddha's closing verse does not add a seventh item to the list; it "
            "reorders the whole discussion, ranking &lsquo;a passage of teaching&rsquo; "
            "above giving in every form the six deities have just described &mdash; a "
            "claim closely related to the well-known principle, stated elsewhere in the "
            "canon, that the gift of the teaching surpasses every other kind of gift."]),
    ],
    terms=[
        ("sādhu",
         "&ldquo;good&rdquo; &mdash; the exclamation opening every deity's verse in this "
         "discourse, and this discourse's title."),
        ("saddhāya dānaṁ",
         "&ldquo;giving out of faith&rdquo; &mdash; the third deity's addition to the "
         "cumulative list, introducing motive as a further qualification beyond the bare "
         "act of giving."),
        ("dhammadinnaṁ",
         "&ldquo;legitimate wealth, rightfully given&rdquo; &mdash; the fourth deity's "
         "addition, specifying that what is given must itself be honestly earned."),
        ("ahiṁsā",
         "&ldquo;non-harming, restraint toward living creatures&rdquo; &mdash; the sixth "
         "and final addition, marking this discourse's shift from giving specifically "
         "into broader ethical conduct."),
        ("dhammapadaṁ",
         "&ldquo;a passage of teaching&rdquo; &mdash; what the Buddha's closing verse "
         "ranks above every form of giving already described."),
    ],
    text_intro=(
        "The discourse in full: six deities building one cumulative list on giving well, "
        "and the Buddha's ranking of teaching above it all. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Deities arrive; a first item is named"),
        ("p", "&sect;1", "sn1.33:1.1-2.5"),
        ("h3", "A second item: even from little"),
        ("p", "&sect;2", "sn1.33:3.1-5.4"),
        ("h3", "A third item: out of faith"),
        ("p", "&sect;3", "sn1.33:6.1-7.7"),
        ("h3", "A fourth item: legitimate wealth"),
        ("p", "&sect;4", "sn1.33:8.1-10.4"),
        ("h3", "A fifth item: intelligently"),
        ("p", "&sect;5", "sn1.33:11.1-13.4"),
        ("h3", "A sixth item: non-harming"),
        ("p", "&sect;6", "sn1.33:14.1-16.4"),
        ("h3", "A question, and the Buddha's ranking"),
        ("p", "&sect;7", "sn1.33:17.1-19.4"),
    ],
    quiz=[
        {"q": "How does this discourse's structure differ from SN 1.32's four deities?",
         "opts": [
             "Each deity repeats everything said before and adds one new qualification, building a single cumulative list",
             "Each deity makes a completely unrelated, independent claim",
             "Only one deity speaks in this discourse",
             "The structure is identical to SN 1.32 in every respect"],
         "correct": 0,
         "expl": "A cumulative refrain, distinct from SN 1.32's four separate arguments."},
        {"q": "What comparison does the third deity's verse make?",
         "opts": [
             "Giving and warfare are similar, since even a few of the good may conquer the many",
             "Giving is compared to a flood sweeping everything away",
             "Giving is compared to a lamp lighting the world",
             "No comparison is made in the third deity's verse"],
         "correct": 0,
         "expl": "A point about quality over quantity, not about violence itself."},
        {"q": "What does the sixth and final item added to the list concern?",
         "opts": [
             "Restraint toward living creatures (ahiṁsā), a shift from giving into non-harming",
             "Giving even larger amounts of wealth",
             "Giving only to one's immediate family",
             "Refusing to give under any circumstances"],
         "correct": 0,
         "expl": "A shift from dāna specifically into broader ethical conduct."},
        {"q": "What subtle point does the sixth deity's verse make about motive?",
         "opts": [
             "Avoiding harm only from fear of blame would make cowardice, not virtue, praiseworthy",
             "Fear of blame is the only valid reason to avoid harm",
             "Motive has no relevance to whether an act counts as virtuous",
             "Only deities can act virtuously; humans cannot"],
         "correct": 0,
         "expl": "Genuine virtue avoids harm for its own sake, not merely from social pressure."},
        {"q": "What does the Buddha's closing verse rank above every form of giving described?",
         "opts": [
             "A passage of teaching (dhammapadaṁ)",
             "An even larger sacrifice",
             "Wealth accumulated over a lifetime",
             "Nothing; he ranks giving as supreme"],
         "correct": 0,
         "expl": "Closely related to the canon's broader claim that teaching surpasses all other gifts."},
        {"q": "What does 'saddhāya dānaṁ' mean?",
         "opts": [
             "'Giving out of faith'",
             "'Giving out of fear'",
             "'Refusing to give'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "The third deity's addition, introducing motive as a qualification."},
        {"q": "What does 'dhammadinnaṁ' specify about what is given?",
         "opts": [
             "That it must be legitimate wealth, rightfully earned",
             "That it must be given in secret",
             "That it must be given only once a year",
             "That it must be given only by aristocrats"],
         "correct": 0,
         "expl": "The fourth deity's addition to the cumulative list."},
        {"q": "By the sixth deity's full verse, how many qualifications does it contain?",
         "opts": [
             "All six, since each deity repeats everything said before",
             "Only the sixth, with earlier qualifications dropped",
             "Only one, unrelated to the previous five",
             "None; the sixth deity contradicts all five before"],
         "correct": 0,
         "expl": "The defining feature of this discourse's cumulative structure."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove, with several Satullapakāyikā deities as at SN 1.31 and 1.32",
             "Near Rājagaha, with a single deity",
             "In the heavenly Garden of Delight",
             "No setting is given"],
         "correct": 0,
         "expl": "The same recurring host and setting as the two discourses before it."},
        {"q": "What does 'ahiṁsā' mean?",
         "opts": [
             "'Non-harming, restraint toward living creatures'",
             "'Generosity toward the wealthy only'",
             "'A type of sacrifice'",
             "'Fear of blame'"],
         "correct": 0,
         "expl": "The sixth and final addition to this discourse's cumulative list."},
    ],
    marginalia=[
        ("A list, building", [
            "each deity repeats,",
            "then adds one more",
        ]),
        ("Giving as warfare", [
            "a few of the good",
            "may conquer the many",
        ]),
        ("From giving to non-harming", [
            "the sixth item shifts",
            "beyond dāna itself",
        ]),
        ("Teaching, ranked highest", [
            "a passage of Dhamma &mdash;",
            "above every gift named",
        ]),
    ],
    further=[
        '<a href="%s/sn1.33/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.32.html">SN 1.32 &middot; Stinginess</a> &mdash; the discourse '
        "immediately before this one, on the same broad theme of giving.",
        '<a href="sn-1.31.html">SN 1.31 &middot; Virtuous</a> &mdash; this vagga&rsquo;s '
        "opening discourse, this collection's first multi-deity exchange.",
        "SN 1.34 &middot; There Are None &mdash; the next discourse, closing with a verse "
        "shared word for word with the Buddha's answer to a deity at SN 1.20.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.34 — Nasantisutta
# --------------------------------------------------------------------------- #
page(
    1, 34, "Nasanti", "There Are None",
    meta_title="SN 1.34 — There Are None | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nasantisutta — "
        "deities debate whether sensual pleasures are permanent, verses trace desire to "
        "its cessation, and Venerable Mogharāja asks the Buddha whether an unseen "
        "liberation is still worth revering. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; several Satullapakāyikā "
                    "deities, then a further exchange with the named mendicant "
                    "Venerable Mogharāja"),
        ("Speakers", "One or more deities across four verses, then Venerable Mogharāja "
                    "and the Buddha in a final exchange"),
        ("Form", "A sequence of verses on desire and its cessation, closed by a named "
                 "mendicant's direct question and the Buddha's answer"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the closing verses "
                       "repeat some of this collection's most doctrinally dense material"),
        ("A named questioner", "Venerable Mogharāja, known elsewhere in the canon for a "
                               "celebrated question of his own, appears here asking a "
                               "different question entirely"),
    ],
    why=(
        "This discourse opens with a claim about sensual pleasure &mdash; nothing among "
        "mankind is permanent, and those bound to and intoxicated by sensuous things "
        "never return from Death's dominion &mdash; and traces the causal chain "
        "underlying it: gloom is born of desire, suffering is born of desire, and "
        "removing desire removes both in turn. The verses build to a description of one "
        "who has fully let go, cut every tie, and become impossible for gods or humans to "
        "locate anywhere. At this point Venerable Mogharāja, a named mendicant, asks a "
        "pointed question: if such a person can't be seen or found by anyone, are those "
        "who still revere them worthy of praise at all?"),
    guide=[
        ("A causal chain, traced step by step", [
            "The verses move through a specific sequence rather than simply asserting a "
            "conclusion: desire gives rise to gloom, gloom and desire together give rise "
            "to suffering, and removing desire removes gloom, which in turn removes "
            "suffering. The logic is presented as a chain of dependency, not a single "
            "unexplained claim."]),
        ("Pretty things are not themselves the problem", [
            "One verse draws a distinction easy to overlook: &lsquo;the world's pretty "
            "things aren't sensual pleasures &mdash; greedy intention is a person's "
            "sensual pleasure.&rsquo; The pretty things &lsquo;stay just as they "
            "are&rsquo;; what the attentive remove is their own desire for them, not the "
            "things themselves."]),
        ("A verse this collection has met before", [
            "The closing description of one who has cut every tie, whom gods and humans "
            "cannot find &lsquo;in this life or the next&hellip; not in heaven nor in any "
            "abode,&rsquo; is close to verses already met in this collection at SN 1.20's "
            "third compressed verse to the deity Samiddhi encountered &mdash; the same "
            "image of complete untraceability recurring in a new context."]),
        ("Mogharāja's question, and a different Mogharāja moment", [
            "Venerable Mogharāja is known elsewhere in the wider canon, in the "
            "Pārāyanavagga, for a celebrated question of his own about how to regard the "
            "world so as to escape Death's notice. Here his question is different: not "
            "how to achieve the liberation just described, but whether those who revere "
            "someone so thoroughly untraceable are themselves still worthy of respect. "
            "The Buddha's answer is unambiguous &mdash; yes, and specifically because "
            "they have understood the teaching and given up doubt."]),
    ],
    terms=[
        ("nasanti",
         "&ldquo;there are none, there do not exist&rdquo; &mdash; this discourse's "
         "title, from its opening claim that no sensual pleasures among mankind are "
         "permanent."),
        ("domanassaṁ jāyati kāmato",
         "&ldquo;gloom is born of desire&rdquo; &mdash; the first link in the causal "
         "chain the verses trace from desire through to suffering and its removal."),
        ("chandarāgo",
         "&ldquo;greedy intention&rdquo; &mdash; identified as a person's true sensual "
         "pleasure, distinguished from the world's pretty things themselves."),
        ("chinnagantho",
         "&ldquo;one whose ties are cut&rdquo; &mdash; the same term already met at SN "
         "1.20, describing someone gods and humans cannot locate anywhere."),
        ("mogharājā",
         "Venerable Mogharāja, the named mendicant who questions the Buddha in this "
         "discourse's final exchange, known elsewhere in the canon for a different, "
         "well-known question of his own."),
    ],
    text_intro=(
        "The discourse in full: verses tracing desire to its cessation, and a named "
        "mendicant's closing question. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Deities arrive; sensual pleasures, and their true cause"),
        ("p", "&sect;1", "sn1.34:1.1-1.3"),
        ("p", "&sect;2", "sn1.34:2.1-2.4"),
        ("p", "&sect;3", "sn1.34:3.1-3.3"),
        ("h3", "What is actually removed"),
        ("p", "&sect;4", "sn1.34:4.1-6.6"),
        ("h3", "Mogharāja asks a question"),
        ("p", "&sect;5", "sn1.34:7.1-8.5"),
    ],
    quiz=[
        {"q": "What does the opening verse claim about sensual pleasures?",
         "opts": [
             "Nothing among mankind is permanent, and those bound to sensuous things never return from Death's dominion",
             "Sensual pleasures are entirely harmless if pursued in moderation",
             "Sensual pleasures do not exist at all",
             "Only deities, never humans, experience sensual pleasure"],
         "correct": 0,
         "expl": "The discourse's opening claim, giving it its title."},
        {"q": "What causal chain do the verses trace?",
         "opts": [
             "Desire gives rise to gloom, which together with desire gives rise to suffering; removing desire removes both",
             "Suffering causes desire, which causes gloom",
             "No causal relationship is described at all",
             "Gloom causes sensual pleasure directly"],
         "correct": 0,
         "expl": "A step-by-step dependency, not a single unexplained assertion."},
        {"q": "What distinction does one verse draw about 'the world's pretty things'?",
         "opts": [
             "They are not themselves sensual pleasure; greedy intention is",
             "They must all be physically destroyed",
             "They are identical to sensual pleasure with no distinction possible",
             "Only aristocrats are permitted to enjoy them"],
         "correct": 0,
         "expl": "Chandarāgo, greedy intention, is what is actually removed, not the things themselves."},
        {"q": "What earlier discourse in this collection shares imagery with this discourse's closing description of one who has cut every tie?",
         "opts": [
             "SN 1.20, in its third compressed verse to the deity",
             "SN 1.1, on crossing the flood",
             "SN 1.11, on the Garden of Delight",
             "No earlier discourse shares this imagery"],
         "correct": 0,
         "expl": "The same image of complete untraceability recurring in a new context."},
        {"q": "Who asks the Buddha a question in this discourse's closing exchange?",
         "opts": [
             "Venerable Mogharāja, a named mendicant",
             "An unnamed deity",
             "A king",
             "No one asks a question; the discourse ends with the verses on cutting ties"],
         "correct": 0,
         "expl": "This collection's first discourse in this vagga to name its questioner directly."},
        {"q": "What does Mogharāja specifically ask?",
         "opts": [
             "Whether those who revere someone untraceable to gods and humans are themselves worthy of praise",
             "How to achieve liberation for himself",
             "Whether the Buddha is truly liberated at all",
             "How many lamps light the world"],
         "correct": 0,
         "expl": "A question about the worth of reverence directed at someone unfindable."},
        {"q": "How does the Buddha answer Mogharāja's question?",
         "opts": [
             "Yes, unambiguously, specifically because they have understood the teaching and given up doubt",
             "No, such reverence is entirely worthless",
             "He refuses to answer the question",
             "He answers only with another question"],
         "correct": 0,
         "expl": "A direct, affirmative answer with a specific reason given."},
        {"q": "What is Venerable Mogharāja known for elsewhere in the canon?",
         "opts": [
             "A celebrated question of his own, in the Pārāyanavagga, about escaping Death's notice",
             "Being the first mendicant ever ordained",
             "Composing the Dhammapada",
             "Nothing; he appears only in this discourse"],
         "correct": 0,
         "expl": "A different, well-known question from the one he asks here."},
        {"q": "What does 'chandarāgo' mean?",
         "opts": [
             "'Greedy intention' &mdash; identified as a person's true sensual pleasure",
             "'The world's pretty things themselves'",
             "'A type of deity'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "Distinguished in this discourse from the pretty things themselves."},
        {"q": "What does 'chinnagantho' mean?",
         "opts": [
             "'One whose ties are cut' &mdash; a term already met at SN 1.20",
             "'One who is bound by every tie'",
             "'A type of sacrifice'",
             "'A monastery near Rājagaha'"],
         "correct": 0,
         "expl": "Describing someone gods and humans cannot find anywhere."},
    ],
    marginalia=[
        ("Nothing permanent", [
            "sensual pleasures, none lasting &mdash;",
            "bound to them, no return",
        ]),
        ("A chain, traced", [
            "desire to gloom,",
            "gloom and desire to suffering",
        ]),
        ("The things, or the wanting", [
            "pretty things stay as they are &mdash;",
            "desire is removed, not the things",
        ]),
        ("Mogharāja&rsquo;s question", [
            "if none can find them,",
            "is reverence still worth it?",
        ]),
    ],
    further=[
        '<a href="%s/sn1.34/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.33.html">SN 1.33 &middot; Good</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.20.html">SN 1.20 &middot; With Samiddhi</a> &mdash; the earlier '
        "discourse sharing this discourse&rsquo;s closing image of untraceability.",
        "SN 1.35 &middot; Fault-Finding Deities &mdash; the next discourse, a very "
        "different and more dramatic encounter with a hostile group of deities.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.35 — Ujjhānasaññisutta
# --------------------------------------------------------------------------- #
page(
    1, 35, "Ujjhānasaññī", "Fault-Finding Deities",
    meta_title="SN 1.35 — Fault-Finding Deities | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ujjhānasaññisutta — a hostile group of deities taunts the Buddha as a hypocrite, "
        "apologizes, then taunts him again about forgiveness itself, before he explicitly "
        "pardons them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; a distinct, hostile host "
                    "&mdash; deities of the fault-finders, standing in the air rather "
                    "than approaching respectfully"),
        ("Speakers", "One or more of the fault-finding deities, and the Buddha, across "
                    "two full rounds of confrontation"),
        ("Form", "An accusatory verse exchange, an apology, a renewed taunt, and a final "
                 "direct exchange ending in explicit pardon"),
        ("Length", "~2.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the narrative "
                       "structure carries as much weight as the verses themselves"),
        ("A distinctly dramatic discourse", "One of very few in this collection where the "
                                            "Buddha is shown reacting emotionally "
                                            "&mdash; here, with a smile"),
    ],
    why=(
        "This discourse's deities are not the friendly Satullapakāyikā of the four "
        "discourses before it, but a group Sujato names &lsquo;fault-finders&rsquo; "
        "&mdash; and they arrive standing in the air rather than approaching "
        "respectfully. Their opening verses accuse the Buddha of hypocrisy: someone who "
        "pretends to be other than they are is like a cheating gambler profiting from "
        "theft. The Buddha does not defend himself directly; he describes what genuine "
        "attainment looks like instead. The deities then apologize &mdash; and the "
        "Buddha smiles &mdash; only to fly back up and taunt him again, this time about "
        "whether he will actually forgive them."),
    guide=[
        ("A hostile posture, marked from the start", [
            "Every deity elsewhere in this collection who addresses the Buddha "
            "approaches and stands respectfully &lsquo;to one side.&rsquo; This "
            "discourse's fault-finding deities instead stand &lsquo;in the air&rsquo; "
            "&mdash; a physical detail marking confrontation and distance rather than the "
            "usual deference, before a single word is spoken."]),
        ("An accusation of hypocrisy, answered without denial", [
            "The deities' opening verses accuse the Buddha, implicitly, of saying one "
            "thing and doing another &mdash; like a cheating gambler enjoying stolen "
            "gains. Rather than protest his own innocence, the Buddha's reply simply "
            "describes what genuine progress on the path actually looks like: not "
            "achieved by speaking or listening alone, but by understanding &lsquo;the "
            "way of the world&rsquo; and being quenched by that understanding. The "
            "accusation is left for the deities themselves to judge against this "
            "description."]),
        ("An apology, a smile, and a renewed attack", [
            "The deities land, bow at the Buddha's feet, and apologize directly for their "
            "foolish presumption &mdash; a moment of genuine humility this collection "
            "rarely shows. The Buddha's response is recorded as a smile, one of very few "
            "places in this collection where his emotional reaction is described "
            "directly. Remarkably, the deities do not settle after apologizing: they "
            "become &lsquo;even more fault-finding&rsquo; and fly back up to taunt him "
            "again, this time about forgiveness itself."]),
        ("A trap in the second taunt, and an answer that sidesteps it", [
            "The deities' second taunt is a kind of trap: if you don't pardon a confessed "
            "mistake, you're stuck in hidden enmity. The Buddha's reply doesn't take the "
            "bait of self-defense; it questions the premise instead &mdash; if no "
            "mistake had even been found, wouldn't settling any remaining enmity still be "
            "skillful regardless? Only after the deities then ask directly who, if "
            "anyone, never errs, does the Buddha answer plainly, naming himself, and "
            "explicitly states: &lsquo;I pardon your mistake.&rsquo;"]),
    ],
    terms=[
        ("ujjhānasaññī",
         "&ldquo;fault-finding, perceiving blame&rdquo; &mdash; the name of this "
         "discourse's deity host, and this discourse's title, distinct from the "
         "Satullapakāyikā of the discourses before it."),
        ("vehāsaṁ ṭhitā",
         "&ldquo;standing in the air&rdquo; &mdash; the deities' confrontational posture, "
         "contrasted with the respectful &lsquo;standing to one side&rsquo; used "
         "elsewhere in this collection."),
        ("lokassa gatiṁ",
         "&ldquo;the way of the world&rdquo; &mdash; what the attentive are said to "
         "understand, in the Buddha's non-defensive reply to the deities' accusation."),
        ("sitaṁ pātvākāsi",
         "&ldquo;smiled&rdquo; &mdash; the Buddha's described reaction to the deities' "
         "apology, a rare direct description of his emotional response in this "
         "collection."),
        ("khamāmi te accayaṁ",
         "&ldquo;I pardon your mistake&rdquo; &mdash; the Buddha's explicit, final "
         "statement of forgiveness closing this discourse."),
    ],
    text_intro=(
        "The discourse in full: an accusation, a non-defensive answer, an apology, a "
        "renewed taunt, and an explicit pardon. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Fault-finding deities arrive, standing in the air"),
        ("p", "&sect;1", "sn1.35:1.1-1.3"),
        ("p", "&sect;2", "sn1.35:2.1-3.4"),
        ("h3", "The Buddha's answer, without denial"),
        ("p", "&sect;3", "sn1.35:4.1-5.4"),
        ("h3", "An apology, a smile, and a renewed taunt"),
        ("p", "&sect;4", "sn1.35:6.1-6.6"),
        ("p", "&sect;5", "sn1.35:7.1-7.4"),
        ("h3", "The Buddha turns the trap aside"),
        ("p", "&sect;6", "sn1.35:8.1-8.4"),
        ("h3", "Who never errs? A direct answer, and a pardon"),
        ("p", "&sect;7", "sn1.35:9.1-9.4"),
        ("p", "&sect;8", "sn1.35:10.1-11.6"),
    ],
    quiz=[
        {"q": "How do the fault-finding deities' posture differ from other deities elsewhere in this collection?",
         "opts": [
             "They stand in the air, rather than approaching respectfully to one side",
             "They kneel before the Buddha immediately",
             "They remain invisible throughout the entire discourse",
             "They arrive during the day rather than at night"],
         "correct": 0,
         "expl": "A physical detail marking confrontation before any words are spoken."},
        {"q": "What do the deities accuse the Buddha of in their opening verses?",
         "opts": [
             "Hypocrisy, comparing him to a cheating gambler who profits from theft",
             "Excessive generosity",
             "Failing to teach at all",
             "Breaking a specific monastic rule"],
         "correct": 0,
         "expl": "An accusation of pretending to be other than he really is."},
        {"q": "How does the Buddha respond to this accusation?",
         "opts": [
             "He does not deny it directly; he describes what genuine attainment actually looks like",
             "He angrily denies every word",
             "He refuses to respond at all",
             "He agrees the accusation is entirely correct"],
         "correct": 0,
         "expl": "A non-defensive answer, leaving the deities to judge for themselves."},
        {"q": "What happens after the deities apologize for their presumption?",
         "opts": [
             "The Buddha smiles, and the deities become even more fault-finding, flying up to taunt him again",
             "The Buddha immediately punishes them",
             "The deities settle down permanently and never speak again",
             "The discourse ends immediately after the apology"],
         "correct": 0,
         "expl": "A remarkably human, escalating turn rather than a tidy resolution."},
        {"q": "What is the 'trap' in the deities' second taunt?",
         "opts": [
             "If he doesn't pardon a confessed mistake, he's accused of hidden enmity",
             "They ask him to perform an impossible miracle",
             "They demand he leave Jeta's Grove permanently",
             "They ask him to name a successor"],
         "correct": 0,
         "expl": "A challenge designed to put the Buddha in a difficult position either way."},
        {"q": "How does the Buddha's reply address this trap?",
         "opts": [
             "He questions the premise: even absent a found mistake, settling enmity would still be skillful",
             "He falls directly into the trap and admits fault",
             "He refuses to answer the question at all",
             "He accuses the deities of lying"],
         "correct": 0,
         "expl": "Sidestepping the taunt rather than accepting its framing."},
        {"q": "Who does the Buddha name as the one who 'makes no mistakes' and 'doesn't go astray'?",
         "opts": [
             "Himself, the Realized One",
             "A specific deity in the group",
             "No one; he says such a person cannot exist",
             "Venerable Mogharāja"],
         "correct": 0,
         "expl": "A direct, plain answer once the deities ask the question outright."},
        {"q": "What does the Buddha explicitly state at the discourse's close?",
         "opts": [
             "'I pardon your mistake'",
             "'I will never pardon you'",
             "'There was no mistake to begin with'",
             "He says nothing further after naming himself"],
         "correct": 0,
         "expl": "Khamāmi te accayaṁ &mdash; explicit, final forgiveness."},
        {"q": "What emotional reaction is the Buddha described as having in this discourse?",
         "opts": [
             "He smiled, in response to the deities' apology",
             "He wept",
             "He laughed uncontrollably",
             "No emotional reaction is described anywhere in the discourse"],
         "correct": 0,
         "expl": "A rare direct description of the Buddha's emotional response in this collection."},
        {"q": "What does 'lokassa gatiṁ' mean?",
         "opts": [
             "'The way of the world' &mdash; what the attentive are said to understand",
             "'The end of the world'",
             "'A type of deity'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "Part of the Buddha's non-defensive answer to the deities' accusation."},
    ],
    marginalia=[
        ("A hostile arrival", [
            "standing in the air,",
            "not to one side",
        ]),
        ("An accusation, unanswered directly", [
            "a cheating gambler, they say &mdash;",
            "he describes attainment instead",
        ]),
        ("A smile, then renewed taunting", [
            "an apology given,",
            "and taken up again",
        ]),
        ("A trap sidestepped, then pardon", [
            "even without fault, settling is skillful &mdash;",
            "&ldquo;I pardon your mistake&rdquo;",
        ]),
    ],
    further=[
        '<a href="%s/sn1.35/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.34.html">SN 1.34 &middot; There Are None</a> &mdash; the '
        "discourse immediately before this one.",
        '<a href="sn-1.31.html">SN 1.31 &middot; Virtuous</a> &mdash; this vagga&rsquo;s '
        "opening discourse, with a very different, friendly deity host.",
        "SN 1.36 &middot; Faith &mdash; the next discourse, returning to the "
        "Satullapakāyikā host and its more familiar multi-deity form.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.36 — Saddhāsutta
# --------------------------------------------------------------------------- #
page(
    1, 36, "Saddhā", "Faith",
    meta_title="SN 1.36 — Faith | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saddhāsutta — "
        "two Satullapakāyikā deities speak, one on faith as a person's partner, the other "
        "in three stanzas on diligence, ending without this vagga's usual closing "
        "question. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove; the friendly Satullapakāyikā "
                    "host, returning after SN 1.35's hostile deities"),
        ("Speakers", "Two deities, the second speaking three stanzas in a row"),
        ("Form", "One short verse, then a longer three-stanza verse, with no closing "
                 "question to the Buddha"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form"),
        ("An open ending", "Unlike SN 1.31 through SN 1.33, this discourse ends without "
                           "anyone asking who spoke best, or any reply from the Buddha"),
    ],
    why=(
        "The first deity offers a single image: faith is a person's partner, and if "
        "faithlessness doesn't linger, fame and heaven follow. The second deity then "
        "speaks at greater length, across three stanzas: giving up anger and conceit "
        "frees one from torment; the wise protect diligence as their best treasure, "
        "unlike fools devoted to negligence; and diligent practice of absorption, rather "
        "than negligence or erotic intimacy, leads to ultimate happiness. The discourse "
        "then simply ends &mdash; without the &lsquo;who spoke best&rsquo; question or "
        "the Buddha's own capping verse that closed several discourses earlier in this "
        "vagga."),
    guide=[
        ("Faith as a companion, not a possession", [
            "The first deity's image treats faith (<em>saddhā</em>) as a "
            "<em>sahāyā</em>, a &lsquo;partner&rsquo; or companion, rather than something "
            "simply held or lacked. The metaphor suggests faith accompanies a person "
            "through their life the way a companion would, rather than functioning as a "
            "static possession."]),
        ("A verse nearly repeating SN 1.34, with one word changed", [
            "The second deity's opening stanza &mdash; &lsquo;give up anger, get rid of "
            "conceit, and get past all the fetters&rsquo; &mdash; is nearly identical to "
            "a verse already met two discourses earlier, at SN 1.34: only "
            "&lsquo;chains&rsquo; here replaces &lsquo;sufferings&rsquo; there as what "
            "doesn't torment one who has nothing. The near-repetition, this time within "
            "a few discourses of each other rather than across vaggas, shows this "
            "particular verse circulating closely within this collection's own material."]),
        ("Diligence as a treasure, negligence as folly", [
            "The second stanza's image is direct: fools and simpletons devote themselves "
            "to negligence, while the wise protect diligence &lsquo;as their best "
            "treasure&rsquo; (<em>seṭṭhaṁ dhanaṁ</em>) &mdash; framing sustained "
            "attentiveness not as a burden but as something valuable enough to actively "
            "guard."]),
        ("An ending without resolution", [
            "This discourse simply stops after the second deity's third stanza, with no "
            "one asking who spoke best and no closing verse from the Buddha. Compared "
            "with SN 1.31 through SN 1.33's consistent pattern of ending in exactly that "
            "way, this discourse's abrupt close is a reminder that the multi-deity "
            "structure introduced earlier in this vagga is not a fixed template applied "
            "identically every time."]),
    ],
    terms=[
        ("saddhā",
         "&ldquo;faith, confidence&rdquo; &mdash; this discourse's title, and the first "
         "deity's central image."),
        ("sahāyā",
         "&ldquo;a partner, a companion&rdquo; &mdash; how the first deity's verse "
         "describes faith's relationship to a person."),
        ("pamādaṁ anuyuñjanti",
         "&ldquo;devote themselves to negligence&rdquo; &mdash; the second deity's "
         "description of fools and simpletons, contrasted with the wise."),
        ("seṭṭhaṁ dhanaṁ",
         "&ldquo;their best treasure&rdquo; &mdash; how the second deity's verse "
         "describes diligence, framing it as something actively guarded rather than "
         "merely practiced."),
        ("paramaṁ sukhaṁ",
         "&ldquo;ultimate happiness&rdquo; &mdash; what the second deity's closing line "
         "says diligent practice of absorption leads to."),
    ],
    text_intro=(
        "The discourse in full: two deities on faith and diligence, ending without this "
        "vagga's usual closing question. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A first deity: faith as a partner"),
        ("p", "&sect;1", "sn1.36:1.1-1.3"),
        ("p", "&sect;2", "sn1.36:2.1-2.4"),
        ("h3", "A second deity, in three stanzas"),
        ("p", "&sect;3", "sn1.36:3.1-4.4"),
        ("p", "&sect;4", "sn1.36:5.1-5.4"),
        ("p", "&sect;5", "sn1.36:6.1-6.4"),
    ],
    quiz=[
        {"q": "What image does the first deity use for faith?",
         "opts": [
             "A partner or companion (sahāyā)",
             "A weapon",
             "A burden to be discarded",
             "A type of sacrifice"],
         "correct": 0,
         "expl": "Faith accompanies a person, rather than being merely held or lacked."},
        {"q": "What does the first deity's verse say happens when faithlessness doesn't linger?",
         "opts": [
             "Fame and renown are theirs, and they go to heaven",
             "They immediately lose all their possessions",
             "Nothing changes at all",
             "They are reborn as deities of the Thirty-Three specifically"],
         "correct": 0,
         "expl": "The consequence the first deity's verse names for sustained faith."},
        {"q": "How does the second deity's opening stanza relate to a verse at SN 1.34?",
         "opts": [
             "It is nearly identical, with 'chains' replacing 'sufferings' as what doesn't torment one who has nothing",
             "It is completely unrelated to anything in SN 1.34",
             "It directly contradicts SN 1.34's verse",
             "It quotes SN 1.34 word for word with no changes at all"],
         "correct": 0,
         "expl": "A near-repetition within a few discourses, showing this verse circulating closely within the collection."},
        {"q": "What does the second deity's second stanza say the wise protect as their best treasure?",
         "opts": [
             "Diligence",
             "Wealth",
             "Social status",
             "Physical strength"],
         "correct": 0,
         "expl": "Seṭṭhaṁ dhanaṁ &mdash; framing diligence as actively guarded, not merely practiced."},
        {"q": "What does the second deity's third stanza name as leading to ultimate happiness?",
         "opts": [
             "Being diligent and practicing absorption, rather than negligence or erotic intimacy",
             "Accumulating as much wealth as possible",
             "Avoiding all forms of meditation",
             "Seeking out sensual pleasure directly"],
         "correct": 0,
         "expl": "Paramaṁ sukhaṁ &mdash; the stanza's closing claim."},
        {"q": "How does this discourse's ending differ from SN 1.31 through SN 1.33?",
         "opts": [
             "It ends without anyone asking who spoke best, and without a closing verse from the Buddha",
             "It ends with an even longer question-and-answer exchange",
             "It ends identically to those three discourses in every respect",
             "It has no ending at all; the text is incomplete"],
         "correct": 0,
         "expl": "A reminder that this vagga's multi-deity structure isn't applied identically every time."},
        {"q": "How many deities speak in this discourse?",
         "opts": [
             "Two",
             "Six",
             "One",
             "Four"],
         "correct": 0,
         "expl": "A first deity with a single verse, and a second with three stanzas."},
        {"q": "What deity host does this discourse return to, after SN 1.35's hostile deities?",
         "opts": [
             "The friendly Satullapakāyikā host",
             "The Pure Abode deities",
             "The deities of the Thirty-Three",
             "No deities appear in this discourse"],
         "correct": 0,
         "expl": "The same host from SN 1.31 through SN 1.34, resumed here."},
        {"q": "What does 'pamādaṁ anuyuñjanti' describe?",
         "opts": [
             "Devoting oneself to negligence, the behavior of fools and simpletons",
             "The wise protecting diligence",
             "A type of deity",
             "A monastery near Sāvatthī"],
         "correct": 0,
         "expl": "Contrasted directly with the wise, who protect diligence instead."},
        {"q": "What does 'saddhā' mean?",
         "opts": [
             "'Faith, confidence'",
             "'Anger'",
             "'Conceit'",
             "'Negligence'"],
         "correct": 0,
         "expl": "This discourse's title and the first deity's central subject."},
    ],
    marginalia=[
        ("Faith, as companion", [
            "sahāyā &mdash; a partner,",
            "not a possession",
        ]),
        ("A near-repeat, close by", [
            "chains, not sufferings &mdash;",
            "echoing SN 1.34",
        ]),
        ("Diligence, guarded", [
            "seṭṭhaṁ dhanaṁ &mdash;",
            "the wise protect it as treasure",
        ]),
        ("No question asked", [
            "the discourse simply ends &mdash;",
            "no verdict, no reply",
        ]),
    ],
    further=[
        '<a href="%s/sn1.36/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.35.html">SN 1.35 &middot; Fault-Finding Deities</a> &mdash; the '
        "discourse immediately before this one, with a very different, hostile host.",
        '<a href="sn-1.34.html">SN 1.34 &middot; There Are None</a> &mdash; the source '
        "of this discourse's nearly repeated opening stanza.",
        "SN 1.37 &middot; The Congregation &mdash; the next discourse, an entirely "
        "different setting with deities gathered from ten world-systems.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.37 — Samayasutta
# --------------------------------------------------------------------------- #
page(
    1, 37, "Samaya", "The Congregation",
    meta_title="SN 1.37 — The Congregation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samayasutta — "
        "four deities of the Pure Abodes each praise the vast gathered Saṅgha of five "
        "hundred arahants at Kapilavatthu, in a scene closely paralleling the Mahāsamaya "
        "Sutta (DN 20). From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Kapilavatthu, in the Sakyan lands, at the Great Wood &mdash; a "
                    "setting entirely new to this vagga, with a Saṅgha of five hundred "
                    "arahants and deities gathered from ten world-systems"),
        ("Speakers", "Four deities of the Pure Abodes (<em>Suddhāvāsa</em>), each "
                    "reciting one verse in turn"),
        ("Form", "A brief narrated frame, followed by four independent verses of praise, "
                 "with no closing question or reply"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; direct in form, with "
                       "one especially vivid martial image"),
        ("A famous parallel", "This discourse's setting and premise closely parallel the "
                              "opening of the Mahāsamaya Sutta (DN 20), which describes "
                              "the same or a very similar gathering at much greater "
                              "length"),
    ],
    why=(
        "This discourse opens on an unusually large scale: the Buddha at Kapilavatthu "
        "with a Saṅgha of five hundred mendicants, every one of them a perfected arahant, "
        "and most of the deities from ten entire world-systems gathered to see them. Four "
        "deities of the Pure Abodes, noticing this, decide together to approach the "
        "Buddha and each recite a verse. What follows is not debate or riddle but praise "
        "&mdash; four distinct images of the gathered Saṅgha's discipline, restraint, "
        "strength, and the safety of taking refuge in it."),
    guide=[
        ("A scale unlike any earlier discourse in this vagga", [
            "Five hundred arahants and deities from ten world-systems is a vastly larger "
            "gathering than any earlier discourse in this collection describes. The four "
            "Pure Abode deities' shared decision to each recite a verse &mdash; rather "
            "than one deity speaking alone, or several building a single refrain "
            "&mdash; introduces yet another variation on this vagga's multi-speaker "
            "structure."]),
        ("A famous parallel scene, briefly told", [
            "This same premise &mdash; the Buddha and his Saṅgha at the Great Wood near "
            "Kapilavatthu, with deities from across the cosmos gathering to see them "
            "&mdash; is the opening scene of the Mahāsamaya Sutta (DN 20), a much longer "
            "discourse that goes on to name dozens of deities in an extended roll call. "
            "This discourse gives the same basic scene in compact form, with only its "
            "four Pure Abode deities speaking."]),
        ("Reins, and a torn-out gatepost", [
            "The second deity's charioteer-and-reins image for sense-restraint is a "
            "familiar figure of controlled attention; the third deity's image is far more "
            "startling &mdash; the mendicants described as having &lsquo;snapped the post "
            "and snapped the cross-bar&rsquo; and &lsquo;torn out Indra's pillar,&rsquo; "
            "the massive gatepost marking a city's boundary. Read alongside the "
            "traditional gloss, this pictures the arahants' strength as sufficient to "
            "break through obstacles &mdash; the fetters and hindrances &mdash; that "
            "would stop an ordinary traveler entirely."]),
        ("Refuge, and its stated benefit", [
            "The fourth deity's verse closes the discourse on a more practical note: "
            "anyone who has gone to the Buddha for refuge will not fall to a plane of "
            "loss, and after this human life will instead join &lsquo;the hosts of "
            "gods.&rsquo; Unlike the discourse's first three verses, which describe the "
            "Saṅgha itself, this final verse addresses what taking refuge does for the "
            "one who takes it."]),
    ],
    terms=[
        ("suddhāvāsa",
         "the &ldquo;Pure Abodes,&rdquo; a set of heavenly realms reserved for "
         "non-returners &mdash; the four deities who speak in this discourse belong to "
         "this specific class."),
        ("dasahi lokadhātūhi",
         "&ldquo;from ten world-systems&rdquo; &mdash; the scale of deities said to have "
         "gathered, indicating a cosmically significant occasion."),
        ("sārathīva nettāni gahetvā",
         "&ldquo;like a charioteer holding the reins&rdquo; &mdash; the second deity's "
         "image, a common figure elsewhere in the canon for restraining the senses."),
        ("indakhīla",
         "&ldquo;Indra's pillar,&rdquo; the massive gatepost marking a city's boundary "
         "&mdash; the third deity's image of something torn out by the mendicants' "
         "unshaken strength."),
        ("apāyaṁ na gacchati",
         "&ldquo;won't go to a plane of loss&rdquo; &mdash; the specific benefit the "
         "fourth deity's verse attributes to going to the Buddha for refuge."),
    ],
    text_intro=(
        "The discourse in full: a vast gathering, and four deities' praise of the "
        "assembled Saṅgha. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A vast gathering, and four deities' shared plan"),
        ("p", "&sect;1", "sn1.37:1.1-1.7"),
        ("h3", "Four verses of praise"),
        ("p", "&sect;2", "sn1.37:2.1-3.4"),
        ("p", "&sect;3", "sn1.37:4.1-5.4"),
        ("p", "&sect;4", "sn1.37:6.1-7.4"),
        ("p", "&sect;5", "sn1.37:8.1-9.4"),
    ],
    quiz=[
        {"q": "What scale of gathering does this discourse describe?",
         "opts": [
             "Five hundred arahant mendicants and deities gathered from ten world-systems",
             "A single deity visiting alone",
             "Two deities in casual conversation",
             "A small group of six local villagers"],
         "correct": 0,
         "expl": "A vastly larger occasion than any earlier discourse in this collection."},
        {"q": "Who decides to approach the Buddha and recite verses?",
         "opts": [
             "Four deities of the Pure Abodes (Suddhāvāsa)",
             "The five hundred mendicants themselves",
             "A single unnamed deity",
             "King Suddhodana"],
         "correct": 0,
         "expl": "A specific class of deity, reserved for non-returners."},
        {"q": "What famous discourse elsewhere in the canon shares this discourse's basic setting?",
         "opts": [
             "The Mahāsamaya Sutta (DN 20)",
             "The Dhammapada",
             "The Visuddhimagga",
             "No comparable discourse exists elsewhere"],
         "correct": 0,
         "expl": "A much longer discourse describing the same or a very similar gathering."},
        {"q": "What image does the second deity use for sense-restraint?",
         "opts": [
             "A charioteer holding the reins",
             "A tortoise withdrawing into its shell",
             "A sword striking its target",
             "Dust thrown against the wind"],
         "correct": 0,
         "expl": "A familiar figure elsewhere in the canon for controlled attention."},
        {"q": "What striking image does the third deity's verse use?",
         "opts": [
             "The mendicants have snapped a post and cross-bar and torn out Indra's pillar, a massive gatepost",
             "The mendicants have built an entirely new city",
             "The mendicants have crossed a great ocean",
             "The mendicants have planted a garden"],
         "correct": 0,
         "expl": "An image of strength sufficient to break through what would stop an ordinary traveler."},
        {"q": "What benefit does the fourth deity's verse attribute to taking refuge in the Buddha?",
         "opts": [
             "Not falling to a plane of loss, and joining the hosts of gods after this life",
             "Immediate wealth in this present life",
             "Freedom from all illness",
             "No stated benefit is given"],
         "correct": 0,
         "expl": "The discourse's only verse addressing the benefit to the one who takes refuge, rather than describing the Saṅgha itself."},
        {"q": "How many verses do the four deities recite in total?",
         "opts": [
             "Four, one from each deity",
             "One shared verse recited together",
             "Twelve, three from each deity",
             "No verses are recited; only prose is used"],
         "correct": 0,
         "expl": "Each of the four Pure Abode deities speaks exactly once."},
        {"q": "Does this discourse end with a question asking who spoke best?",
         "opts": [
             "No &mdash; it ends after the fourth deity's verse, with no closing exchange",
             "Yes, followed by a long debate",
             "Yes, and the Buddha names a winner",
             "The discourse has no ending at all"],
         "correct": 0,
         "expl": "A structure without this vagga's earlier closing-question pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Near Kapilavatthu, in the Sakyan lands, at the Great Wood",
             "Near Sāvatthī, in Jeta's Grove",
             "Near Rājagaha, at the Hot Springs Monastery",
             "Near Vesālī, at the peaked-roof hall"],
         "correct": 0,
         "expl": "An entirely new setting for this vagga, distinct from the recurring Sāvatthī frame."},
        {"q": "What are the 'Pure Abodes'?",
         "opts": [
             "A set of heavenly realms reserved for non-returners",
             "A type of monastery on earth",
             "A realm reserved exclusively for humans",
             "A name for the human plane of existence"],
         "correct": 0,
         "expl": "The specific class of deity the four speaking deities belong to."},
    ],
    marginalia=[
        ("A vast assembly", [
            "five hundred arahants,",
            "deities from ten worlds",
        ]),
        ("A famous parallel", [
            "the same scene, briefly told,",
            "as DN 20&rsquo;s opening",
        ]),
        ("Reins, then a torn gatepost", [
            "controlled senses,",
            "unshakeable strength",
        ]),
        ("Refuge, and its benefit", [
            "no plane of loss &mdash;",
            "the hosts of gods instead",
        ]),
    ],
    further=[
        '<a href="%s/sn1.37/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.36.html">SN 1.36 &middot; Faith</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.29.html">SN 1.29 &middot; Four Wheels</a> &mdash; an earlier '
        "discourse in this collection also using imagery of restraint under control.",
        "SN 1.38 &middot; A Splinter &mdash; the next discourse, seven hundred deities "
        "praising the Buddha's endurance of physical pain.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.38 — Sakalikasutta
# --------------------------------------------------------------------------- #
page(
    1, 38, "Sakalika", "A Splinter",
    meta_title="SN 1.38 — A Splinter | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sakalikasutta — "
        "the Buddha endures a foot wound with unbroken mindfulness, seven hundred "
        "deities praise him through six animal similes, and closing verses repeat SN "
        "1.9's teaching on conceit and diligence. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Rājagaha, at the Maddakucchi deer park &mdash; a new setting "
                    "for this vagga, prompted by a physical injury to the Buddha "
                    "himself"),
        ("Speakers", "The narrator describing the Buddha's own conduct, then seven "
                    "deities in turn, the last introducing closing verses"),
        ("Form", "A narrated account of physical endurance, six brief similes from six "
                 "deities, a seventh deity's fuller reflection, and closing verses"),
        ("Length", "~3 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; direct in form, with "
                       "a psychologically precise closing description of freedom"),
        ("An injury, not explained here", "This discourse doesn't say how the splinter "
                                          "came to wound the Buddha's foot; later "
                                          "tradition elsewhere in the canon associates a "
                                          "similar injury with Devadatta's attempt on his "
                                          "life by rolling a boulder"),
    ],
    why=(
        "This discourse opens not with a deity's question but with an injury: the "
        "Buddha's foot has been cut by a wooden splinter, and he is described as "
        "stricken by sharp, severe pain &mdash; which he endures unbothered, mindful and "
        "aware, before lying down deliberately in the lion's posture. Seven hundred "
        "deities arrive and, one after another, compare him to an elephant, a lion, a "
        "thoroughbred, a boss bull, and a behemoth, before a seventh deity describes his "
        "freedom directly: not leaning forward, not pulling back, and not held in place "
        "by forceful suppression. Closing verses then contrast a century of futile "
        "ascetic mortification with the same two verses on conceit and diligence already "
        "met earlier in this collection, at SN 1.9."),
    guide=[
        ("Pain endured, not denied", [
            "The narration is specific about the pain's intensity &mdash; "
            "&lsquo;painful, sharp, severe, acute, unpleasant, and disagreeable&rsquo; "
            "&mdash; rather than minimizing it. What distinguishes the Buddha's response "
            "is not an absence of pain but enduring it &lsquo;unbothered, with "
            "mindfulness and situational awareness,&rsquo; a description of composure "
            "under real discomfort rather than an absence of discomfort altogether."]),
        ("Six similes, one refrain, six animals", [
            "Six deities in turn compare the Buddha to an elephant, a lion, a "
            "thoroughbred, a boss bull, a behemoth, and finally someone simply "
            "&lsquo;truly tamed&rsquo; &mdash; each repeating an identical description "
            "of enduring painful feelings unbothered, changing only the single noun "
            "naming what kind of formidable being he resembles. This is the densest "
            "instance yet in this collection of the &lsquo;same refrain, different "
            "single word&rsquo; pattern already met with pairs of discourses; here it "
            "spans six speakers in one."]),
        ("A seventh deity names the freedom directly", [
            "Where the first six deities reach for comparison, the seventh describes the "
            "Buddha's actual inner state: immersion well developed, mind well freed "
            "&mdash; &lsquo;not leaning forward or pulling back, and not held in place by "
            "forceful suppression.&rsquo; Three distinct ways of failing to achieve real "
            "balance are named and set aside together: grasping forward toward what is "
            "wanted, recoiling from what is not, and merely forcing stillness through "
            "suppression rather than genuine release."]),
        ("A closing verse this collection has already used", [
            "The two verses that close this discourse &mdash; on conceit preventing "
            "taming, and on giving up conceit to cross beyond Death's dominion &mdash; "
            "are word for word the same two verses that closed SN 1.9, much earlier in "
            "this collection. There, they answered a deity's challenge about conceit and "
            "solitary wilderness practice; here, the identical verses instead cap a "
            "reflection on enduring severe physical pain without complaint &mdash; the "
            "same teaching applied to a different circumstance entirely."]),
    ],
    terms=[
        ("sakalika",
         "&ldquo;a splinter, a chip&rdquo; &mdash; this discourse's title, naming the "
         "cause of the Buddha's physical pain."),
        ("sato sampajāno adhivāsesi",
         "&ldquo;he endured unbothered, with mindfulness and situational "
         "awareness&rdquo; &mdash; the description this discourse repeats for how the "
         "Buddha met his pain."),
        ("purisanāgaṁ purisasīhaṁ",
         "&ldquo;an elephant of a man, a lion of a man&rdquo; &mdash; two of the six "
         "animal-comparisons the seven hundred deities offer in turn."),
        ("na cābhinataṁ na cāpanataṁ",
         "&ldquo;not leaning forward, not pulling back&rdquo; &mdash; the seventh "
         "deity's precise description of the Buddha's freed mind, naming two failure "
         "modes rather than describing the freedom only in positive terms."),
        ("na ca sasaṅkhāraniggayhavāritagataṁ",
         "&ldquo;not held in place by forceful suppression&rdquo; &mdash; the third "
         "failure mode named, distinguishing genuine release from mere forced "
         "stillness."),
    ],
    text_intro=(
        "The discourse in full: an injury endured with mindfulness, six animal similes, "
        "a direct description of freedom, and closing verses shared with SN 1.9. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha, wounded and unshaken"),
        ("p", "&sect;1", "sn1.38:1.1-1.6"),
        ("h3", "Seven hundred deities, six similes"),
        ("p", "&sect;2", "sn1.38:2.1-7.3"),
        ("h3", "A seventh deity names the freedom directly"),
        ("p", "&sect;3", "sn1.38:8.1-8.3"),
        ("h3", "Closing verses, shared with SN 1.9"),
        ("p", "&sect;4", "sn1.38:9.1-10.4"),
        ("p", "&sect;5", "sn1.38:11.1-12.4"),
    ],
    quiz=[
        {"q": "How was the Buddha's foot injured in this discourse?",
         "opts": [
             "Cut by a wooden splinter; the text does not explain how it got there",
             "Bitten by a snake",
             "Struck by lightning",
             "Injured by a fall from a tree"],
         "correct": 0,
         "expl": "The immediate cause given; later tradition elsewhere links a similar injury to Devadatta."},
        {"q": "How is the Buddha's response to the pain described?",
         "opts": [
             "He endured it unbothered, with mindfulness and situational awareness, without the pain itself being denied",
             "He felt no pain whatsoever",
             "He cried out in visible distress",
             "He immediately sought medical treatment and refused to continue teaching"],
         "correct": 0,
         "expl": "Composure under real discomfort, not an absence of discomfort."},
        {"q": "What pattern do the first six deities' verses follow?",
         "opts": [
             "An identical description of enduring pain, changing only a single animal comparison each time",
             "Six completely unrelated statements with no shared structure",
             "A debate among the deities about whether the Buddha is truly unbothered",
             "Six separate riddles, each with a different answer"],
         "correct": 0,
         "expl": "The densest instance in this collection of the 'same refrain, different word' pattern."},
        {"q": "What does the seventh deity describe, distinct from the first six?",
         "opts": [
             "The Buddha's actual inner state directly, rather than reaching for a comparison",
             "A different physical ailment entirely",
             "The deity's own past lives",
             "A request for the Buddha to teach the entire assembly"],
         "correct": 0,
         "expl": "Naming three specific failure modes of imbalance the Buddha's mind is free from."},
        {"q": "What three failure modes does the seventh deity's verse name and set aside?",
         "opts": [
             "Leaning forward, pulling back, and forced suppression",
             "Hunger, thirst, and fatigue",
             "Wealth, fame, and power",
             "Speech, thought, and physical action"],
         "correct": 0,
         "expl": "Grasping toward what is wanted, recoiling from what is not, and merely forcing stillness."},
        {"q": "What earlier discourse in this collection do this discourse's closing two verses repeat word for word?",
         "opts": [
             "SN 1.9, on conceit and solitary wilderness practice",
             "SN 1.1, on crossing the flood",
             "SN 1.20, With Samiddhi",
             "No earlier discourse shares these verses"],
         "correct": 0,
         "expl": "The identical verses applied to a new circumstance, physical pain endured."},
        {"q": "What does the closing teaching say about a century of Vedic-learned brahmins' austerity?",
         "opts": [
             "Their minds are not properly freed, despite the mortification",
             "It always leads directly to full liberation",
             "It is praised without qualification",
             "It is not mentioned in this discourse at all"],
         "correct": 0,
         "expl": "A critique preceding the repeated verses on conceit and diligence."},
        {"q": "How many deities are said to have gathered in this discourse?",
         "opts": [
             "Seven hundred",
             "Seven",
             "Seventy",
             "Seven thousand"],
         "correct": 0,
         "expl": "One of the largest explicitly named deity-counts in this collection."},
        {"q": "What posture does the Buddha adopt after enduring the pain?",
         "opts": [
             "The lion's posture, lying on his right side with one foot on the other, mindful and aware",
             "Standing upright throughout",
             "Seated in full lotus posture only",
             "No posture is described"],
         "correct": 0,
         "expl": "A deliberate, composed posture rather than a collapse from pain."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Rājagaha, at the Maddakucchi deer park",
             "Near Sāvatthī, in Jeta's Grove",
             "Near Kapilavatthu, at the Great Wood",
             "Near Vesālī, at the peaked-roof hall"],
         "correct": 0,
         "expl": "A new setting for this vagga, distinct from its recurring Sāvatthī frame."},
    ],
    marginalia=[
        ("Pain, named plainly", [
            "sharp, severe, acute &mdash;",
            "endured unbothered",
        ]),
        ("Six animals, one refrain", [
            "elephant, lion, thoroughbred,",
            "bull, behemoth, tamed",
        ]),
        ("Freedom, described directly", [
            "not leaning forward,",
            "not held by force",
        ]),
        ("A verse returning", [
            "SN 1.9&rsquo;s teaching,",
            "now applied to pain endured",
        ]),
    ],
    further=[
        '<a href="%s/sn1.38/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.37.html">SN 1.37 &middot; The Congregation</a> &mdash; the '
        "discourse immediately before this one.",
        '<a href="sn-1.9.html">SN 1.9 &middot; Fond of Conceit</a> &mdash; the source of '
        "this discourse's closing two verses.",
        "SN 1.39 &middot; With Pajjunna's Daughter (1st) &mdash; the next discourse, a "
        "named deity's devotional verses at Vesālī.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.39 — Paṭhamapajjunnadhītusutta
# --------------------------------------------------------------------------- #
page(
    1, 39, "Paṭhamapajjunnadhītu", "With Pajjunna's Daughter (1st)",
    meta_title="SN 1.39 — With Pajjunna's Daughter (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first "
        "Paṭhamapajjunnadhītusutta — Kokanadā, a deity named by her own father's name, "
        "describes moving from hearsay to witnessed knowledge of the teaching, at "
        "Vesālī. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Vesālī, at the Great Wood, in the hall with the peaked roof "
                    "&mdash; a new setting for this vagga"),
        ("Speakers", "Kokanadā, Pajjunna's daughter, speaking alone in devotional verse"),
        ("Form", "Four four-line verses of praise and reflection, with no dialogue or "
                 "reply from the Buddha"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form"),
        ("A named individual, with a named father", "The first deity in this vagga "
                                                     "identified both by her own personal "
                                                     "name and by her parentage, rather "
                                                     "than as an unnamed member of a "
                                                     "group"),
    ],
    why=(
        "Unlike the group discourses earlier in this vagga, this one gives a single "
        "named individual the entire floor: Kokanadā, identified as the daughter of "
        "Pajjunna, arrives at Vesālī and speaks four verses of her own, naming herself "
        "within her own speech, describing a shift from merely having heard the teaching "
        "to now knowing it &lsquo;as a witness&rsquo; while the Buddha himself teaches, "
        "and closing with the contrasting fates of those who denounce the teaching and "
        "those who accept it."),
    guide=[
        ("A named individual, not a group", [
            "Every deity discourse so far in this vagga has featured either an unnamed "
            "single deity, an unnamed collective host, or a specific but unnamed class "
            "(the Pure Abode deities, the fault-finders). This discourse is the first to "
            "name its speaker personally, and by parentage &mdash; &lsquo;Pajjunna's "
            "daughter&rsquo; identifies her specifically as the offspring of Pajjunna, a "
            "deity elsewhere associated with rain."]),
        ("Naming herself, mid-speech", [
            "Kokanadā's own verse names herself in the third person even as she speaks "
            "&mdash; &lsquo;Kokanadā am I who worships him&rsquo; &mdash; a somewhat "
            "unusual self-referential convention, closer to formal self-introduction "
            "than to the anonymous questions most deities in this collection ask."]),
        ("From hearsay to witnessed knowledge", [
            "Her second verse draws a specific epistemological distinction: "
            "&lsquo;previously I had only heard the teaching realized by the Clear-eyed "
            "One&rsquo;; now, listening to the Buddha teach directly, she knows it "
            "&lsquo;as a witness&rsquo; (<em>sakkhi</em>) &mdash; a distinction between "
            "secondhand report and personally verified knowing, made explicit rather "
            "than assumed."]),
        ("Denouncing the teaching, and its stated cost", [
            "The closing two verses contrast sharply: those who go about denouncing the "
            "teaching of the noble ones fall to the &lsquo;terrible Hell of Screams&rsquo; "
            "(<em>roruva</em>) and suffer there long, while those who find acceptance and "
            "peace in the same teaching swell the hosts of gods after this life. The "
            "consequence named is specifically for denunciation of the teaching, not for "
            "unrelated wrongdoing."]),
    ],
    terms=[
        ("pajjunna",
         "a deity elsewhere associated with rain; Kokanadā is identified throughout this "
         "discourse specifically as his daughter."),
        ("kokanadā",
         "the name of the deity who speaks this discourse's verses, naming herself "
         "within her own speech."),
        ("sakkhi",
         "&ldquo;as a witness, firsthand&rdquo; &mdash; how Kokanadā describes her "
         "present knowledge of the teaching, contrasted with merely having heard of it "
         "before."),
        ("cakkhumantena desite",
         "&ldquo;taught by the Clear-eyed One&rdquo; &mdash; her description of the "
         "Buddha as the teaching's source, using an epithet for clear vision."),
        ("roruva",
         "the &ldquo;Hell of Screams,&rdquo; the specific destination this discourse "
         "names for those who denounce the teaching of the noble ones."),
    ],
    text_intro=(
        "The discourse in full: a named deity's verses on witnessed knowledge and the "
        "cost of denouncing the teaching. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Kokanadā arrives at Vesālī"),
        ("p", "&sect;1", "sn1.39:1.1-1.4"),
        ("p", "&sect;2", "sn1.39:2.1-2.4"),
        ("h3", "From hearsay to witnessed knowledge"),
        ("p", "&sect;3", "sn1.39:3.1-3.4"),
        ("h3", "Two fates, contrasted"),
        ("p", "&sect;4", "sn1.39:4.1-4.4"),
        ("p", "&sect;5", "sn1.39:5.1-5.4"),
    ],
    quiz=[
        {"q": "How is the speaker of this discourse identified, unlike earlier discourses in this vagga?",
         "opts": [
             "By a personal name and by parentage, rather than as unnamed or an unnamed group",
             "By no identification of any kind",
             "Only by her physical appearance",
             "Only by the name of her husband"],
         "correct": 0,
         "expl": "Kokanadā, Pajjunna's daughter &mdash; the first such naming in this vagga."},
        {"q": "What deity is Kokanadā identified as the daughter of?",
         "opts": [
             "Pajjunna, a deity elsewhere associated with rain",
             "Sakka, ruler of the Thirty-Three",
             "Brahmā",
             "No father is named"],
         "correct": 0,
         "expl": "Named directly in this discourse's title and opening verse."},
        {"q": "How does Kokanadā's second verse describe her present knowledge of the teaching?",
         "opts": [
             "As witnessed firsthand (sakkhi), contrasted with merely having heard of it before",
             "As entirely uncertain and unverified",
             "As identical to what she had always known",
             "As learned only from another deity, never from the Buddha directly"],
         "correct": 0,
         "expl": "A specific distinction between secondhand report and personally verified knowing."},
        {"q": "What fate does the third verse describe for those who denounce the teaching?",
         "opts": [
             "Falling to the Hell of Screams (roruva) and suffering there long",
             "Immediate rebirth as deities",
             "No consequence at all",
             "Becoming wealthy in their next life"],
         "correct": 0,
         "expl": "A specific, named destination for this specific offense."},
        {"q": "What fate does the fourth verse describe for those who accept the teaching?",
         "opts": [
             "Swelling the hosts of gods after giving up their human body",
             "Falling to the Hell of Screams",
             "Remaining permanently as humans",
             "No fate is described for them"],
         "correct": 0,
         "expl": "A contrasting destination to the one named for denouncers."},
        {"q": "How does Kokanadā refer to herself within her own verse?",
         "opts": [
             "In the third person, naming herself directly as she speaks",
             "She never names herself at all",
             "Only in the first person, with no name given",
             "By a different name than the discourse's title uses"],
         "correct": 0,
         "expl": "An unusual, formal self-introduction within the verse itself."},
        {"q": "Does this discourse contain any reply from the Buddha?",
         "opts": [
             "No &mdash; it consists entirely of Kokanadā's own four verses",
             "Yes, an extensive prose reply",
             "Yes, a single short verse in response",
             "The Buddha asks her a counter-question"],
         "correct": 0,
         "expl": "A solo devotional discourse, unlike the dialogic discourses elsewhere in this collection."},
        {"q": "What does 'cakkhumantena' refer to?",
         "opts": [
             "The Buddha, described by an epithet for clear vision ('the Clear-eyed One')",
             "A type of deity",
             "A monastery near Vesālī",
             "A specific meditation technique"],
         "correct": 0,
         "expl": "Kokanadā's description of the teaching's source."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Vesālī, at the Great Wood, in the hall with the peaked roof",
             "Near Sāvatthī, in Jeta's Grove",
             "Near Rājagaha, at the Maddakucchi deer park",
             "Near Kapilavatthu, at the Great Wood"],
         "correct": 0,
         "expl": "A new setting for this vagga, shared with the discourse immediately following it."},
        {"q": "What does 'sakkhi' mean?",
         "opts": [
             "'As a witness, firsthand'",
             "'By hearsay only'",
             "'Never known'",
             "'A type of hell'"],
         "correct": 0,
         "expl": "Kokanadā's description of her present, verified knowledge of the teaching."},
    ],
    marginalia=[
        ("A name, and a father named", [
            "Kokanadā,",
            "Pajjunna&rsquo;s daughter",
        ]),
        ("From hearing to witnessing", [
            "once only heard of,",
            "now known firsthand",
        ]),
        ("Denouncers, and their fate", [
            "the Hell of Screams,",
            "suffering long",
        ]),
        ("Acceptance, and its fate", [
            "peace found in the teaching &mdash;",
            "swelling the hosts of gods",
        ]),
    ],
    further=[
        '<a href="%s/sn1.39/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.38.html">SN 1.38 &middot; A Splinter</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.37.html">SN 1.37 &middot; The Congregation</a> &mdash; an earlier '
        "discourse in this vagga also set outside the usual Sāvatthī frame.",
        "SN 1.40 &middot; With Pajjunna's Daughter (2nd) &mdash; the next discourse, "
        "this vagga's last, spoken by a second deity of the same name and parentage.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.40 — Dutiyapajjunnadhītusutta (closes the Satullapakāyikavagga)
# --------------------------------------------------------------------------- #
page(
    1, 40, "Dutiyapajjunnadhītu", "With Pajjunna's Daughter (2nd)",
    meta_title="SN 1.40 — With Pajjunna's Daughter (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second "
        "Dutiyapajjunnadhītusutta — Kokanadā the Younger states the teaching's meaning "
        "in brief, using the same verse that closed SN 1.20 as a deity's own uncertain "
        "paraphrase. Closes the Satullapakāyikavagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Vesālī, at the Great Wood, in the hall with the peaked roof "
                    "&mdash; the same setting as the discourse immediately before it"),
        ("Speakers", "Kokanadā the Younger, Pajjunna's daughter, speaking alone in "
                    "devotional verse"),
        ("Form", "Three four-line verses of praise and summary, closing this vagga"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but its "
                       "closing verse rewards comparison with an earlier discourse"),
        ("Closing this vagga", "The tenth and last discourse of the Satullapakāyikavagga, "
                               "whose own closing colophon names the vagga as finished"),
    ],
    why=(
        "A second deity named Kokanadā, also identified as Pajjunna's daughter, arrives "
        "at the same Vesālī setting as the discourse immediately before this one, "
        "described as beautiful as a flash of lightning. She acknowledges that the "
        "teaching could be analyzed in many different ways, but chooses to state its "
        "meaning briefly, as far as she has learned it by heart &mdash; and the verse she "
        "then recites is, word for word, the same verse that closed SN 1.20, much "
        "earlier in this collection, where an unnamed deity offered it as her own "
        "uncertain paraphrase of a teaching the Buddha never directly confirmed."),
    guide=[
        ("A second Kokanadā, at the same setting", [
            "This discourse shares its setting exactly with the one before it, and its "
            "speaker shares the name and parentage of the deity who spoke there &mdash; "
            "&lsquo;Kokanadā the Younger&rsquo; distinguishing her from her predecessor "
            "without explaining their relationship further. The pairing of two same-named "
            "deities at one setting closes this vagga the way SN 1.39 and SN 1.40 close "
            "it together, as a matched set."]),
        ("Choosing brevity over exhaustive analysis", [
            "Kokanadā the Younger's second verse makes an explicit choice: the teaching "
            "could be analyzed &lsquo;in many different ways,&rsquo; but she will state "
            "its meaning briefly, limited to what she has &lsquo;learned it by "
            "heart.&rsquo; The modesty of this framing, naming the limits of her own "
            "memorized understanding, sits close to her namesake's emphasis on witnessed "
            "rather than merely reported knowledge at SN 1.39."]),
        ("The same verse, given very differently", [
            "The verse she recites &mdash; never do wrong by speech, mind, or body; "
            "having given up sensual pleasures, don't keep doing what's painful and "
            "pointless &mdash; is word for word identical to the verse that closed SN "
            "1.20. There, an unnamed deity offered it as her own uncertain attempt to "
            "paraphrase three compressed verses the Buddha had just given, with nothing "
            "in the text confirming whether her reading was correct. Here, a named, "
            "devoted deity states the identical verse directly and confidently, with no "
            "surrounding uncertainty at all."]),
        ("An untranslated close, as with the vaggas before it", [
            "As with SN 1.10, SN 1.20, and SN 1.30, this discourse is followed in the "
            "source text by a closing colophon and a mnemonic verse naming the "
            "Satullapakāyikavagga as finished and listing its ten titles &mdash; left "
            "untranslated in this edition, and described here rather than quoted, "
            "following this project's established practice."]),
        ("A vagga named for a recurring host, closed by two individuals", [
            "This vagga opened at SN 1.31 with the Satullapakāyikā host that gives it its "
            "name, and moved through several structural variations &mdash; a shared "
            "refrain, independent arguments, a cumulative list, a hostile confrontation, "
            "an entirely different setting and scale, a physical ordeal &mdash; before "
            "closing on two individually named deities, sisters or otherwise related by "
            "the same father, neither belonging to the host the vagga is titled after."]),
    ],
    terms=[
        ("cūḷakokanadā",
         "&ldquo;Kokanadā the Younger&rdquo; &mdash; this discourse's speaker, "
         "distinguished from her namesake at SN 1.39 by this compound qualifier."),
        ("vijjulatāva",
         "&ldquo;beautiful as a flash of lightning&rdquo; &mdash; the description of her "
         "arrival, a vivid image for radiance and suddenness together."),
        ("pariyāyena",
         "&ldquo;in different ways, by different methods&rdquo; &mdash; how she "
         "acknowledges the teaching could be analyzed, before choosing brevity instead."),
        ("yāvatā me manasā pariyattaṁ",
         "&ldquo;as far as I have learned it by heart&rdquo; &mdash; her explicit "
         "acknowledgment of the limits of her own memorized understanding."),
        ("pāpaṁ na kayirā vacasā manasā",
         "&ldquo;never do anything bad by speech or mind&rdquo; &mdash; the opening "
         "words of this discourse's closing verse, identical to the verse that closed "
         "SN 1.20."),
    ],
    text_intro=(
        "The discourse in full, with its untranslated closing colophon and mnemonic "
        "verse described rather than quoted, as with SN 1.10, SN 1.20, and SN 1.30. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Kokanadā the Younger arrives"),
        ("p", "&sect;1", "sn1.40:1.1-1.4"),
        ("p", "&sect;2", "sn1.40:2.1-2.4"),
        ("h3", "Brevity, chosen deliberately"),
        ("p", "&sect;3", "sn1.40:3.1-3.4"),
        ("h3", "A verse already met at SN 1.20"),
        ("p", "&sect;4", "sn1.40:4.1-4.4"),
    ],
    quiz=[
        {"q": "How is this discourse's speaker related to SN 1.39's speaker?",
         "opts": [
             "Same name and parentage, distinguished as 'the Younger,' at the same setting",
             "No relationship at all; a completely different deity",
             "She is explicitly said to be the mother of SN 1.39's speaker",
             "She is explicitly said to be an enemy of SN 1.39's speaker"],
         "correct": 0,
         "expl": "A matched pairing closing this vagga, sharing name, parentage, and setting."},
        {"q": "How is Kokanadā the Younger's arrival described?",
         "opts": [
             "Beautiful as a flash of lightning",
             "Silent and invisible",
             "Angry and confrontational",
             "Weeping and distressed"],
         "correct": 0,
         "expl": "A vivid image for radiance and suddenness together."},
        {"q": "What choice does she explicitly make about how to present the teaching?",
         "opts": [
             "To state its meaning briefly, though it could be analyzed in many ways",
             "To recite the entire teaching in exhaustive detail",
             "To refuse to discuss the teaching at all",
             "To ask the Buddha to speak in her place"],
         "correct": 0,
         "expl": "A deliberate choice of brevity, with the limits of this choice acknowledged directly."},
        {"q": "What earlier discourse does this discourse's closing verse repeat word for word?",
         "opts": [
             "SN 1.20's closing verse, With Samiddhi",
             "SN 1.9's closing verses",
             "SN 1.1's opening exchange",
             "No earlier discourse shares this verse"],
         "correct": 0,
         "expl": "The identical verse given very differently in each context."},
        {"q": "How does the verse's context differ between SN 1.20 and this discourse?",
         "opts": [
             "At SN 1.20 it was an unnamed deity's uncertain paraphrase, unconfirmed by the Buddha; here it is stated confidently and directly by a named deity",
             "The context is identical in every respect",
             "At SN 1.20 the Buddha stated it himself; here a deity merely repeats it",
             "This discourse rejects the verse as incorrect"],
         "correct": 0,
         "expl": "The same words, offered with very different degrees of certainty."},
        {"q": "What does 'yāvatā me manasā pariyattaṁ' mean?",
         "opts": [
             "'As far as I have learned it by heart'",
             "'As far as the Buddha has taught it in full'",
             "'Without any limitation whatsoever'",
             "'As commanded by another deity'"],
         "correct": 0,
         "expl": "Her explicit acknowledgment of the limits of her own memorized understanding."},
        {"q": "What follows this discourse in the source text, left untranslated?",
         "opts": [
             "A closing colophon and mnemonic verse listing the vagga's ten discourse titles",
             "An entirely new discourse beginning immediately",
             "A long prose commentary",
             "Nothing follows; the source text ends abruptly"],
         "correct": 0,
         "expl": "The same pattern already seen at SN 1.10, SN 1.20, and SN 1.30."},
        {"q": "What is this discourse's position within the Satullapakāyikavagga?",
         "opts": [
             "It is the tenth and last discourse, closing the vagga",
             "It is the vagga's first discourse",
             "It belongs to the previous vagga, the Sattivagga",
             "It has no fixed position"],
         "correct": 0,
         "expl": "This discourse's own closing colophon marks the Satullapakāyikavagga as finished."},
        {"q": "Does this vagga's closing discourse belong to the Satullapakāyikā host the vagga is named after?",
         "opts": [
             "No &mdash; it closes on two individually named deities unrelated to that host",
             "Yes, Kokanadā is explicitly identified as a member of that host",
             "The discourse does not identify any deity host at all",
             "The vagga has no named host to begin with"],
         "correct": 0,
         "expl": "A vagga that opens with its namesake host but closes on two named individuals instead."},
        {"q": "What does 'pariyāyena' mean?",
         "opts": [
             "'In different ways, by different methods'",
             "'Never, under any circumstances'",
             "'Only once, and never again'",
             "'By force'"],
         "correct": 0,
         "expl": "Acknowledging the teaching's many possible analyses, before she chooses brevity."},
    ],
    marginalia=[
        ("A second Kokanadā", [
            "the Younger, same father &mdash;",
            "same setting as before",
        ]),
        ("Brevity, chosen", [
            "many ways to analyze it,",
            "but stated briefly here",
        ]),
        ("A verse returning", [
            "the same words as SN 1.20,",
            "now spoken with confidence",
        ]),
        ("The Satullapakāyikavagga closes", [
            "ten discourses complete;",
            "named for a host, closed by two names",
        ]),
    ],
    further=[
        '<a href="%s/sn1.40/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.39.html">SN 1.39 &middot; With Pajjunna&rsquo;s Daughter (1st)</a> '
        "&mdash; the discourse immediately before this one, and this vagga&rsquo;s "
        "matched companion piece.",
        '<a href="sn-1.20.html">SN 1.20 &middot; With Samiddhi</a> &mdash; the source of '
        "this discourse's closing verse, given there with far more uncertainty.",
        '<a href="sn-1.31.html">SN 1.31 &middot; Virtuous</a> &mdash; this vagga&rsquo;s '
        "opening discourse, ten discourses back.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.41 — Ādittasutta (opens the Ādittavagga)
# --------------------------------------------------------------------------- #
page(
    1, 41, "Āditta", "On Fire",
    meta_title="SN 1.41 — On Fire | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ādittasutta — a "
        "deity's extended verse comparing giving to rescuing what's useful from a "
        "burning house, since the whole world itself is on fire with old age and death. "
        "Opens the Ādittavagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Sāvatthī, in Jeta&rsquo;s Grove &mdash; the recurring frame"),
        ("Speakers", "An unnamed deity, speaking alone in an extended verse"),
        ("Form", "A single sustained verse of five stanzas, developing one image "
                 "throughout"),
        ("Length", "~1.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form, "
                       "building one extended comparison"),
        ("Opening this vagga", "The first discourse of the Ādittavagga (&lsquo;the "
                               "Chapter on Fire&rsquo;), named for this discourse's "
                               "opening image"),
    ],
    why=(
        "This discourse builds a single sustained comparison across five stanzas: when a "
        "house catches fire, you rescue the useful pot, not the one already burnt "
        "&mdash; and since the whole world is likewise on fire, consumed by old age and "
        "death, the only way to truly rescue anything is by giving it away. What is "
        "given bears the fruit of happiness; what is kept is eventually lost regardless "
        "&mdash; to bandits, rulers, fire, or simple loss &mdash; and at death, the "
        "corpse itself is cast off along with every possession never given."),
    guide=[
        ("A house on fire, extended to the whole world", [
            "The verse's opening image is domestic and immediate: rescuing a useful pot "
            "from a burning house, leaving behind whatever is already ruined. The second "
            "stanza expands this single-house scale to the entire world, on fire "
            "&lsquo;with old age and death&rsquo; &mdash; treating impermanence itself as "
            "the fire, and giving as the only genuine rescue available."]),
        ("Giving as the only lasting form of keeping", [
            "The verse's logic is deliberately counterintuitive: what is given bears "
            "fruit as happiness, while what is kept is eventually lost anyway &mdash; to "
            "theft, taxation, fire, or simple misfortune. Rather than framing giving as a "
            "sacrifice of what could otherwise be kept safely, the verse treats "
            "unshared possessions as already, inevitably, lost."]),
        ("A corpse cast off with everything unshared", [
            "The verse's final image is stark: death casts off the corpse "
            "&lsquo;along with all your possessions&rsquo; &mdash; nothing kept is kept "
            "past that point regardless of how carefully it was guarded. A clever "
            "person, understanding this, both enjoys their possessions and gives them "
            "away, according to their means."]),
        ("A vagga named for an opening image, again", [
            "Like the Sattivagga before it, this vagga takes its name from its opening "
            "discourse's central image &mdash; here, fire &mdash; rather than from a "
            "recurring group of deities or a closing simile. The pattern of naming a "
            "vagga after its first discourse, established at SN 1.11 and SN 1.21, "
            "continues here."]),
    ],
    terms=[
        ("āditta",
         "&ldquo;on fire, ablaze&rdquo; &mdash; this discourse's title, and the image "
         "extended from a single house to the entire world."),
        ("jarāya maraṇena ca",
         "&ldquo;with old age and death&rdquo; &mdash; what the verse names as the fire "
         "consuming the whole world, the counterpart to a literal house fire."),
        ("dinnaṁ hoti sukhudrayaṁ",
         "&ldquo;what's given has happiness as its fruit&rdquo; &mdash; the verse's "
         "central claim, contrasted directly with what is kept and eventually lost."),
        ("adinnaṁ",
         "&ldquo;what isn't given&rdquo; &mdash; named as vulnerable to bandits, rulers, "
         "fire, or simple loss, regardless of how carefully it is guarded."),
        ("bhuñjetha ca dadetha ca",
         "&ldquo;would enjoy what they have and also give it away&rdquo; &mdash; the "
         "verse's practical conclusion, describing a balance rather than an extreme."),
    ],
    text_intro=(
        "The discourse in full: a single sustained comparison between a burning house "
        "and the burning world. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A deity arrives, and speaks at length"),
        ("p", "&sect;1", "sn1.41:1.1-1.4"),
        ("p", "&sect;2", "sn1.41:2.1-3.4"),
        ("p", "&sect;3", "sn1.41:4.1-5.6"),
    ],
    quiz=[
        {"q": "What image does the verse open with?",
         "opts": [
             "Rescuing a useful pot from a burning house, leaving behind what's already ruined",
             "Crossing a flood neither standing nor swimming",
             "A tortoise drawing its limbs into its shell",
             "A deity in the Garden of Delight"],
         "correct": 0,
         "expl": "The domestic scale the verse then expands."},
        {"q": "What does the verse say the whole world is 'on fire' with?",
         "opts": [
             "Old age and death",
             "Literal flames only",
             "Excessive wealth",
             "Conceit alone"],
         "correct": 0,
         "expl": "Impermanence itself treated as the fire consuming everything."},
        {"q": "What does the verse claim about what is given versus what is kept?",
         "opts": [
             "What's given bears happiness as its fruit; what's kept is eventually lost regardless",
             "What's kept always remains perfectly safe",
             "Giving and keeping produce identical results",
             "Nothing given ever produces any benefit"],
         "correct": 0,
         "expl": "A deliberately counterintuitive claim about giving as the real form of keeping."},
        {"q": "What four things does the verse name as threats to unshared possessions?",
         "opts": [
             "Bandits, rulers, fire, or simple loss",
             "Only natural disasters",
             "Only theft by other deities",
             "Nothing threatens unshared possessions"],
         "correct": 0,
         "expl": "Multiple, ordinary ways possessions are eventually lost regardless of care taken."},
        {"q": "What image closes the verse?",
         "opts": [
             "A corpse cast off at death, along with all possessions never given",
             "A deity vanishing into the sky",
             "A reed being mowed down",
             "A sword striking its target"],
         "correct": 0,
         "expl": "Nothing kept is kept past the point of death, regardless of how it was guarded."},
        {"q": "What practical balance does the verse recommend?",
         "opts": [
             "Enjoying one's possessions and also giving them away, according to one's means",
             "Giving away absolutely everything with nothing kept at all",
             "Keeping everything and giving nothing at all",
             "Destroying all possessions rather than using or giving them"],
         "correct": 0,
         "expl": "Bhuñjetha ca dadetha ca &mdash; a balance, not an extreme."},
        {"q": "What gives this vagga its name?",
         "opts": [
             "This discourse's opening image of fire",
             "A closing image from the vagga's last discourse",
             "A recurring group of deities",
             "The name of a specific monastery"],
         "correct": 0,
         "expl": "Following the naming pattern already seen at SN 1.11 and SN 1.21."},
        {"q": "How many stanzas does this discourse's verse contain?",
         "opts": [
             "Five",
             "One",
             "Ten",
             "Two"],
         "correct": 0,
         "expl": "A single sustained comparison developed across five stanzas."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Near Sāvatthī, in Jeta's Grove &mdash; the recurring frame",
             "Near Rājagaha",
             "Near Kapilavatthu",
             "Near Vesālī"],
         "correct": 0,
         "expl": "The Devatāsaṃyutta's standard frame, resumed after the previous vagga's varied settings."},
        {"q": "Does the verse frame giving as a sacrifice of what could otherwise be kept safely?",
         "opts": [
             "No &mdash; it treats unshared possessions as already, inevitably, lost",
             "Yes, giving is framed entirely as a painful sacrifice",
             "The verse makes no claim about safety at all",
             "It claims kept possessions are always safer than given ones"],
         "correct": 0,
         "expl": "A reframing of what 'keeping' actually accomplishes."},
    ],
    marginalia=[
        ("A house on fire", [
            "rescue the useful pot,",
            "not the one already burnt",
        ]),
        ("The world, likewise burning", [
            "old age and death,",
            "the fire that consumes all",
        ]),
        ("Given, or lost regardless", [
            "what's kept: bandits, fire, loss &mdash;",
            "what's given: happiness",
        ]),
        ("A corpse, and what remains", [
            "cast off with all possessions &mdash;",
            "enjoy, and also give",
        ]),
    ],
    further=[
        '<a href="%s/sn1.41/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.40.html">SN 1.40 &middot; With Pajjunna&rsquo;s Daughter '
        "(2nd)</a> &mdash; the discourse that closed the previous vagga, the "
        "Satullapakāyikavagga.",
        '<a href="sn-1.32.html">SN 1.32 &middot; Stinginess</a> &mdash; an earlier '
        "discourse in this collection also concerned with giving and its rewards.",
        "SN 1.42 &middot; Giving What? &mdash; the next discourse, a direct question and "
        "answer on what specifically each kind of gift produces.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.42 — Kiṁdadasutta
# --------------------------------------------------------------------------- #
page(
    1, 42, "Kiṁdada", "Giving What?",
    meta_title="SN 1.42 — Giving What? | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kiṁdadasutta — "
        "a deity's five-part question on what specifically produces strength, beauty, "
        "happiness, and vision, answered gift by gift before naming the greatest gift of "
        "all. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a five-part question, answered point by "
                     "point"),
        ("Form", "A six-line question, answered by a matching, itemized eight-line "
                 "reply"),
        ("Length", "~45 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form, a "
                       "clean list matched point for point"),
        ("A ranked answer", "The reply doesn't just answer all five parts of the "
                            "question; it closes by naming a gift that exceeds every "
                            "other one listed"),
    ],
    why=(
        "The question is structured, asking specifically what produces four distinct "
        "benefits &mdash; strength, beauty, happiness, and vision &mdash; and who, "
        "beyond these four, is the giver of everything at once. The answer matches each "
        "question point for point: food for strength, clothes for beauty, a vehicle for "
        "happiness, a lamp for vision. Then, rather than stopping there, it names one "
        "gift &mdash; monastic quarters &mdash; as the giver of all four benefits "
        "together, and a further gift &mdash; teaching the Dhamma &mdash; as something "
        "categorically greater still: freedom from death itself."),
    guide=[
        ("A question built for a matched answer", [
            "Each of the question's first four lines asks about a single specific "
            "benefit, and the reply answers in exactly the same order and structure: "
            "food, clothes, a vehicle, and a lamp, each paired with the one benefit it "
            "specifically produces. The tight correspondence between question and answer "
            "is itself part of this discourse's clarity."]),
        ("From specific gifts to one gift that gives everything", [
            "The question's fifth line asks something structurally different from the "
            "first four: not what produces one specific benefit, but who is &lsquo;the "
            "giver of all.&rsquo; The reply's answer &mdash; one who gives monastic "
            "quarters &mdash; is treated as combining strength, beauty, happiness, and "
            "vision into a single act of giving, rather than requiring four separate "
            "gifts."]),
        ("A fifth gift, exceeding the rest categorically", [
            "The reply doesn't stop at answering the question as asked. Its final line "
            "adds an unrequested fifth category: one who teaches the Dhamma "
            "&lsquo;gives the gift of freedom from death&rsquo; (<em>amataṁ dadāti</em>) "
            "&mdash; not a fifth item on the same scale as food, clothing, shelter, and "
            "light, but something the verse treats as a different order of gift "
            "altogether."]),
        ("A structural echo of SN 1.33's closing claim", [
            "This discourse's closing move &mdash; naming the gift of the teaching as "
            "surpassing every other kind of giving &mdash; closely echoes the Buddha's "
            "own closing verse at SN 1.33, which ranked &lsquo;a passage of "
            "teaching&rsquo; above giving in every other form the deities there had just "
            "described."]),
    ],
    terms=[
        ("kiṁdada",
         "&ldquo;giving what?&rdquo; &mdash; the interrogative repeated across the "
         "question's first four lines, and this discourse's title."),
        ("balaṁ",
         "&ldquo;strength&rdquo; &mdash; the first benefit named, matched in the reply "
         "with the gift of food."),
        ("vaṇṇadā",
         "&ldquo;giver of beauty&rdquo; &mdash; the second benefit, matched with the "
         "gift of clothing."),
        ("sabbadadaṁ",
         "&ldquo;the giver of all&rdquo; &mdash; the question's fifth and final part, "
         "answered by naming the gift of monastic quarters."),
        ("amataṁ dadāti",
         "&ldquo;gives the gift of freedom from death&rdquo; &mdash; the reply's "
         "unrequested final addition, naming the teaching of the Dhamma as exceeding "
         "every other gift listed."),
    ],
    text_intro=(
        "The discourse in full: a five-part question, answered point by point, then "
        "exceeded by an unrequested final claim. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.42:1.1-1.6"),
        ("p", "&sect;2", "sn1.42:2.1-3.4"),
    ],
    quiz=[
        {"q": "What four specific benefits does the opening question ask about?",
         "opts": [
             "Strength, beauty, happiness, and vision",
             "Wealth, fame, power, and status",
             "The four noble truths",
             "The four elements"],
         "correct": 0,
         "expl": "Each paired in the reply with a specific corresponding gift."},
        {"q": "What gift does the reply match with strength?",
         "opts": [
             "Food",
             "A vehicle",
             "A lamp",
             "Clothing"],
         "correct": 0,
         "expl": "Annadā balado hoti &mdash; the first of four matched pairs."},
        {"q": "What gift does the reply match with vision?",
         "opts": [
             "A lamp",
             "Food",
             "Clothing",
             "A vehicle"],
         "correct": 0,
         "expl": "The fourth of the four matched pairs."},
        {"q": "What does the question's fifth line ask, structurally different from the first four?",
         "opts": [
             "Who is 'the giver of all', rather than what produces one specific benefit",
             "What produces the most wealth",
             "Who should never be given anything",
             "What produces the least benefit"],
         "correct": 0,
         "expl": "A shift from specific benefits to a single comprehensive gift."},
        {"q": "What gift does the reply name as 'the giver of all'?",
         "opts": [
             "Monastic quarters",
             "A vehicle",
             "Gold and jewels",
             "Nothing is named as the giver of all"],
         "correct": 0,
         "expl": "Treated as combining all four benefits into one act of giving."},
        {"q": "What unrequested fifth category does the reply add at its close?",
         "opts": [
             "Teaching the Dhamma, which gives freedom from death",
             "An additional physical gift not yet mentioned",
             "Nothing further is added beyond the question's five parts",
             "A warning against giving anything at all"],
         "correct": 0,
         "expl": "Amataṁ dadāti &mdash; a different order of gift from the rest."},
        {"q": "What earlier discourse in this collection does this discourse's closing move echo?",
         "opts": [
             "SN 1.33, which ranked a passage of teaching above every other form of giving",
             "SN 1.1, on crossing the flood",
             "SN 1.21, on the sword and fire",
             "No earlier discourse shares this structural move"],
         "correct": 0,
         "expl": "Both discourses close by ranking the gift of teaching above material giving."},
        {"q": "What does 'amataṁ' mean?",
         "opts": [
             "'Freedom from death,' or 'the deathless'",
             "'Wealth'",
             "'A type of deity'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "What the gift of teaching is said to give, beyond ordinary material benefit."},
        {"q": "How closely does the reply's structure match the question's structure?",
         "opts": [
             "Very closely &mdash; each of the first four points answered in the same order the question asked them",
             "The reply bears no structural relationship to the question at all",
             "The reply answers only the first point and ignores the rest",
             "The reply reverses the order of every point"],
         "correct": 0,
         "expl": "A tightly matched question-and-answer structure."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set at the Hot Springs Monastery",
             "Explicitly set in the heavenly Garden of Delight",
             "Explicitly set at Kapilavatthu"],
         "correct": 0,
         "expl": "Like several discourses elsewhere in this collection, no setting is given directly."},
    ],
    marginalia=[
        ("Four questions, four gifts", [
            "food, clothes, a vehicle, a lamp &mdash;",
            "each matched exactly",
        ]),
        ("One gift, giving all", [
            "monastic quarters &mdash;",
            "strength, beauty, ease, vision together",
        ]),
        ("A fifth, unrequested", [
            "teaching the Dhamma &mdash;",
            "the gift of freedom from death",
        ]),
        ("An echo of SN 1.33", [
            "the same ranking again:",
            "teaching above every gift",
        ]),
    ],
    further=[
        '<a href="%s/sn1.42/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.41.html">SN 1.41 &middot; On Fire</a> &mdash; the discourse '
        "immediately before this one, and this vagga&rsquo;s opening discourse.",
        '<a href="sn-1.33.html">SN 1.33 &middot; Good</a> &mdash; the earlier discourse '
        "this one's closing move echoes.",
        "SN 1.43 &middot; Food &mdash; the next discourse, on who among gods and humans "
        "doesn't share in food, and why.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.43 — Annasutta
# --------------------------------------------------------------------------- #
page(
    1, 43, "Anna", "Food",
    meta_title="SN 1.43 — Food | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Annasutta — a "
        "riddle asking which spirit doesn't share in food that both gods and humans "
        "enjoy, answered by reframing the question around who has actually given with "
        "faith. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a riddle answered by reframing its own "
                    "premise"),
        ("Form", "A four-line riddle-question, answered by two four-line verses"),
        ("Length", "~30 seconds to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the answer doesn't "
                       "name what the question asked for directly"),
        ("A theme running through this vagga", "Food is the fourth discourse in a row in "
                                                "this vagga substantially concerned with "
                                                "giving"),
    ],
    why=(
        "The question is a riddle with an implied trick: both gods and humans enjoy "
        "food, so what is the name of the spirit who does not? Rather than naming a "
        "specific being, the reply reframes the whole premise: those who give with "
        "faith and a clear, confident heart partake of food's fruit in this world and "
        "the next; by implication, whoever has never given anything, never having sown "
        "that cause, is the one who goes without &mdash; not because of what kind of "
        "spirit they are, but because of what they never did."),
    guide=[
        ("A riddle that isn't answered as asked", [
            "The question asks for a name &mdash; what is this spirit called &mdash; and "
            "the reply supplies no name at all. Instead of identifying a specific being, "
            "it redirects entirely toward a cause: generosity, or its absence, as what "
            "actually determines who partakes of food's benefit and who doesn't."]),
        ("Food as a stand-in for merit, not merely a meal", [
            "Read literally, the riddle sounds like it concerns actual eating; the "
            "reply's answer only makes sense once &lsquo;food&rsquo; is understood more "
            "broadly, as the fruit of merit that follows a person into their next life. "
            "Those who give partake of that fruit &lsquo;in this world and the next"
            "&rsquo;; those who never gave have nothing of that kind waiting for them."]),
        ("An implied answer, not a stated one", [
            "The reply never directly says who the spirit without food actually is. Left "
            "unstated, but strongly implied by the reply's second verse urging the "
            "hearer to dispel stinginess, is that the miserly &mdash; whether reborn "
            "human, animal, or as a hungry spirit unable to receive what is offered them "
            "&mdash; are exactly the ones who go without."]),
        ("A fourth discourse on giving in a row", [
            "SN 1.41 on rescuing what's given from a burning world, SN 1.42 on what each "
            "specific gift produces, and now this discourse on who partakes of food's "
            "fruit: giving has been this vagga's central concern since its first "
            "discourse, more consistently than any earlier vagga in this collection."]),
    ],
    terms=[
        ("anna",
         "&ldquo;food&rdquo; &mdash; this discourse's title, and the riddle's literal "
         "and figurative subject."),
        ("yakkho",
         "&ldquo;spirit&rdquo; &mdash; the being the opening riddle asks to be named, "
         "left unidentified when the reply redirects the question instead."),
        ("saddhāya denti",
         "&ldquo;those who give with faith&rdquo; &mdash; the reply's actual subject, "
         "replacing the question's search for a named spirit."),
        ("vippasannena cetasā",
         "&ldquo;with a clear and confident heart&rdquo; &mdash; the quality of mind "
         "paired with faith in the reply's description of true givers."),
        ("macchariyamalaṁ",
         "&ldquo;the stain of stinginess&rdquo; &mdash; what the reply's second verse "
         "urges dispelling, echoing the same term already met at SN 1.32."),
    ],
    text_intro=(
        "The discourse in full: a riddle about who goes without food, answered by "
        "redirecting toward generosity itself. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.43:1.1-1.4"),
        ("p", "&sect;2", "sn1.43:2.1-3.4"),
    ],
    quiz=[
        {"q": "What does the opening riddle ask?",
         "opts": [
             "The name of the spirit who, unlike gods and humans, doesn't enjoy food",
             "How many lamps light the world",
             "Who can untangle the human tangle",
             "How a mendicant should shield their mind"],
         "correct": 0,
         "expl": "A riddle framed as asking for a specific name."},
        {"q": "Does the reply actually name the spirit the question asks about?",
         "opts": [
             "No &mdash; it redirects the question entirely toward generosity as a cause",
             "Yes, it names the spirit directly and explicitly",
             "It names several different spirits by name",
             "It refuses to answer at all"],
         "correct": 0,
         "expl": "A reframing of the riddle's own premise, rather than a direct answer."},
        {"q": "What does the reply say those who give with faith receive?",
         "opts": [
             "A share of food's fruit in this world and the next",
             "Nothing at all, in this world or the next",
             "Only worldly wealth, with no benefit after death",
             "Punishment for their generosity"],
         "correct": 0,
         "expl": "The actual subject the reply substitutes for the question's search for a name."},
        {"q": "How should 'food' likely be understood in this discourse's answer?",
         "opts": [
             "More broadly, as the fruit of merit following a person into their next life",
             "Only as a literal meal, with no broader meaning",
             "As a synonym for wealth specifically",
             "As a term with no connection to giving at all"],
         "correct": 0,
         "expl": "Literal reading alone doesn't make sense of the reply's actual claim."},
        {"q": "What is left implied, rather than stated directly, by this discourse's answer?",
         "opts": [
             "That the miserly are the ones who go without, whatever form their rebirth takes",
             "That everyone equally receives food regardless of generosity",
             "That only deities can ever go hungry",
             "That the question has no possible answer"],
         "correct": 0,
         "expl": "The second verse's urging to dispel stinginess strongly implies this connection."},
        {"q": "What earlier discourse in this collection shares the term for 'the stain of stinginess'?",
         "opts": [
             "SN 1.32, on stinginess and giving",
             "SN 1.1, on crossing the flood",
             "SN 1.21, on a sword",
             "No earlier discourse shares this term"],
         "correct": 0,
         "expl": "Macchariyamalaṁ, echoed from that earlier discourse."},
        {"q": "How many discourses in a row does this vagga devote substantially to giving?",
         "opts": [
             "Four, from SN 1.41 through this discourse",
             "Only this single discourse",
             "The entire vagga is unrelated to giving",
             "Ten, the vagga's full length"],
         "correct": 0,
         "expl": "A more consistent focus on giving than any earlier vagga in this collection."},
        {"q": "What does 'vippasannena cetasā' mean?",
         "opts": [
             "'With a clear and confident heart'",
             "'With a troubled and doubting mind'",
             "'Without any thought at all'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "The quality of mind paired with faith in true giving."},
        {"q": "Is this riddle's answer identical in form to riddles like SN 1.5 or SN 1.6?",
         "opts": [
             "No &mdash; those riddles supply a direct numerical answer, while this one redirects the question's whole premise",
             "Yes, it uses exactly the same numerical-answer format",
             "This discourse contains no riddle at all",
             "Both discourses give no answer whatsoever"],
         "correct": 0,
         "expl": "A different rhetorical strategy from the earlier number-riddles."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set at Kapilavatthu",
             "Explicitly set at Vesālī",
             "Explicitly set at the Hot Springs Monastery"],
         "correct": 0,
         "expl": "Like several discourses elsewhere in this collection, no setting is given directly."},
    ],
    marginalia=[
        ("A riddle, asked", [
            "who among the spirits",
            "doesn&rsquo;t share in food?",
        ]),
        ("No name given", [
            "the question redirected &mdash;",
            "toward those who give",
        ]),
        ("Food as merit&rsquo;s fruit", [
            "given with faith, received",
            "in this world and the next",
        ]),
        ("A vagga about giving", [
            "the fourth discourse running",
            "on the same theme",
        ]),
    ],
    further=[
        '<a href="%s/sn1.43/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.42.html">SN 1.42 &middot; Giving What?</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.32.html">SN 1.32 &middot; Stinginess</a> &mdash; the earlier '
        "discourse sharing this discourse's term for the stain of stinginess.",
        "SN 1.44 &middot; One Root &mdash; the next discourse, this collection's most "
        "compressed and enigmatic riddle-verse.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.44 — Ekamūlasutta
# --------------------------------------------------------------------------- #
page(
    1, 44, "Ekamūla", "One Root",
    meta_title="SN 1.44 — One Root | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ekamūlasutta — "
        "a single, sealed riddle-verse of numbers describing an abyss crossed by the "
        "seer, left unanswered anywhere in the text itself. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a single riddle-verse with no question, no "
                     "reply, and no narrator's frame at all"),
        ("Form", "One four-line verse only, entirely self-contained"),
        ("Length", "~15 seconds to read"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; &mdash; this collection's "
                       "most compressed and genuinely obscure verse, left unglossed by "
                       "the text itself"),
        ("An unanswered riddle", "Unlike this collection's other numerical riddles (SN "
                                 "1.5, SN 1.6), this one receives no reply from anyone "
                                 "&mdash; the verse simply is the whole discourse"),
    ],
    why=(
        "This is the shortest and most opaque discourse in this collection so far: a "
        "single sealed verse, with no speaker identified, no question posed to anyone, "
        "and no answer given anywhere in the text. It describes an abyss defined by a "
        "series of numbers &mdash; one root, two loops, three stains, five spreads, and "
        "an ocean as a twelfth whirlpool &mdash; crossed, it says, by &lsquo;the "
        "seer.&rsquo; What each number refers to is not stated, and this reading guide "
        "does not supply a confident answer where the text itself gives none."),
    guide=[
        ("A riddle with no one to answer it", [
            "SN 1.5 and SN 1.6, this collection's earlier numerical riddles, are both "
            "asked by a deity and directly answered by the Buddha. This discourse "
            "breaks that pattern entirely: there is no questioner, no respondent, and no "
            "narrative frame of any kind &mdash; just the verse itself, presented "
            "without commentary."]),
        ("Numbers without stated referents", [
            "The verse names a root (one), loops (two), stains (three), spreads (five), "
            "and a twelfth whirlpool called the ocean, all forming an abyss "
            "(<em>pātāla</em>) that &lsquo;the seer&rsquo; (<em>muni</em>) crosses. "
            "Commentarial tradition offers allegorical readings for some of these terms "
            "&mdash; the three stains, for instance, are commonly read elsewhere in the "
            "canon as greed, hatred, and delusion &mdash; but the precise referents for "
            "several of the other numbers, particularly the two loops and the five "
            "spreads, are genuinely debated even within traditional exegesis, and this "
            "reading guide does not assert a specific identification where the "
            "commentarial record itself is uncertain."]),
        ("A structure, if not a content, that is legible", [
            "Even without confidently unpacking each number, the verse's shape is "
            "clear: a sequence of increasing quantities &mdash; one, two, three, five, "
            "twelve &mdash; builds toward a single image, an abyss or ocean, that "
            "poses a genuine obstacle, and that only &lsquo;the seer&rsquo; is said to "
            "cross. The verse asserts that this crossing is possible without explaining "
            "the terrain in terms a casual reader could reconstruct."]),
        ("Honesty about the limits of this reading guide", [
            "This project's consistent practice, when a passage's meaning is genuinely "
            "unsettled rather than merely unfamiliar, is to say so plainly rather than "
            "supply a confident-sounding gloss the source itself doesn't support. This "
            "discourse is one of the clearest instances of that practice in this "
            "collection so far: better to name the uncertainty than to manufacture "
            "false clarity."]),
    ],
    terms=[
        ("ekamūla",
         "&ldquo;one root&rdquo; &mdash; the verse's first numbered element, and this "
         "discourse's title."),
        ("dvirāvaṭṭaṁ",
         "&ldquo;two loops, two whirls&rdquo; &mdash; the verse's second numbered "
         "element, its precise referent debated in traditional exegesis."),
        ("timalaṁ",
         "&ldquo;three stains&rdquo; &mdash; commonly read elsewhere in the canon as "
         "greed, hatred, and delusion, though this specific verse doesn't state that "
         "identification directly."),
        ("pātālaṁ",
         "&ldquo;abyss&rdquo; &mdash; the verse's central image, defined by the full "
         "sequence of numbers it lists."),
        ("muni",
         "&ldquo;the seer, the sage&rdquo; &mdash; the one the verse says crosses this "
         "abyss, left otherwise unidentified."),
    ],
    text_intro=(
        "The discourse in full: a single sealed riddle-verse, presented here exactly as "
        "it is in the source, without an invented resolution. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.44:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this discourse differ from SN 1.5 and SN 1.6, this collection's earlier numerical riddles?",
         "opts": [
             "It has no questioner and no respondent; the verse itself is the entire discourse",
             "It is much longer than either of those two discourses",
             "It is answered in exhaustive detail by the Buddha",
             "It uses no numbers at all"],
         "correct": 0,
         "expl": "A complete break from the deity-asks, Buddha-answers pattern."},
        {"q": "What sequence of numbers does the verse name?",
         "opts": [
             "One root, two loops, three stains, five spreads, and a twelfth whirlpool",
             "Four wheels and nine doors",
             "Five kinds of sensual stimulation and a sixth",
             "Ten discourses in a single vagga"],
         "correct": 0,
         "expl": "A building sequence culminating in an ocean-sized abyss."},
        {"q": "Who does the verse say crosses this abyss?",
         "opts": [
             "'The seer' (muni), otherwise unidentified",
             "A named king",
             "A specific deity by name",
             "No one; the verse says the abyss cannot be crossed"],
         "correct": 0,
         "expl": "The verse's only description of who succeeds."},
        {"q": "Does this reading guide assert confident identifications for every numbered term?",
         "opts": [
             "No &mdash; it names where commentarial tradition is genuinely uncertain, rather than inventing false clarity",
             "Yes, every number is confidently and specifically identified",
             "The guide claims the verse has no meaning at all",
             "The guide claims scholars universally agree on every detail"],
         "correct": 0,
         "expl": "An explicit practice of honesty about genuine interpretive uncertainty."},
        {"q": "What are the 'three stains' commonly read as elsewhere in the canon?",
         "opts": [
             "Greed, hatred, and delusion",
             "Wealth, fame, and power",
             "Hunger, thirst, and fatigue",
             "The three characteristics of existence"],
         "correct": 0,
         "expl": "A common triad elsewhere, though this specific verse doesn't state the identification directly."},
        {"q": "What image does the verse build toward?",
         "opts": [
             "An abyss (pātāla), also called an ocean, with the described sequence forming a twelfth whirlpool",
             "A burning house",
             "A garden of heavenly delight",
             "A wilderness at high noon"],
         "correct": 0,
         "expl": "The verse's culminating image, crossed only by the seer."},
        {"q": "How long is this discourse compared to most others in this collection?",
         "opts": [
             "Among the shortest, consisting of a single four-line verse only",
             "Among the longest, spanning many stanzas",
             "Exactly the same length as SN 1.50",
             "Longer than any prose discourse in this collection"],
         "correct": 0,
         "expl": "One sealed verse, with no narrative frame at all."},
        {"q": "What does 'muni' mean?",
         "opts": [
             "'The seer, the sage'",
             "'A deity of the Thirty-Three'",
             "'A type of hell'",
             "'A monastery near Sāvatthī'"],
         "correct": 0,
         "expl": "The verse's only named agent, who successfully crosses the abyss."},
        {"q": "Is this discourse's meaning fully settled among translators and commentators?",
         "opts": [
             "No &mdash; several of its terms, especially the two loops and five spreads, are genuinely debated",
             "Yes, every element has one universally agreed meaning",
             "The verse is considered entirely meaningless by all traditional sources",
             "No commentarial tradition has ever addressed this verse"],
         "correct": 0,
         "expl": "Genuine, acknowledged uncertainty, not merely unfamiliarity."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text at all; no frame of any kind is given",
             "Explicitly set near Rājagaha",
             "Explicitly set at Kapilavatthu",
             "Explicitly set at Vesālī"],
         "correct": 0,
         "expl": "The most minimal presentation of any discourse in this collection so far."},
    ],
    marginalia=[
        ("A sealed riddle", [
            "no question asked,",
            "no answer given",
        ]),
        ("A sequence of numbers", [
            "one root, two loops,",
            "three stains, five spreads",
        ]),
        ("An abyss, an ocean", [
            "twelve whirlpools deep &mdash;",
            "crossed by the seer",
        ]),
        ("Honesty over false clarity", [
            "some terms genuinely uncertain &mdash;",
            "named as such, not guessed at",
        ]),
    ],
    further=[
        '<a href="%s/sn1.44/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.43.html">SN 1.43 &middot; Food</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.5.html">SN 1.5 &middot; Cut How Many?</a> &mdash; this '
        "collection&rsquo;s earlier numerical riddle, directly answered by the Buddha.",
        "SN 1.45 &middot; Peerless &mdash; the next discourse, a brief verse of praise "
        "for the Buddha himself.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.45 — Anomasutta
# --------------------------------------------------------------------------- #
page(
    1, 45, "Anoma", "Peerless",
    meta_title="SN 1.45 — Peerless | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anomasutta — a "
        "single brief verse of unqualified praise for the Buddha, naming him peerless, "
        "unattached, all-knowing, and treading the noble road. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a single verse of direct address and praise"),
        ("Form", "One four-line verse only, addressed directly to whoever is invited to "
                 "&lsquo;behold&rsquo; the one described"),
        ("Length", "~15 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; simple in form, a "
                       "dense concentration of epithets in four lines"),
        ("A companion to SN 1.44", "The shortest pair of discourses in this vagga, back "
                                   "to back &mdash; an unglossed riddle, then an "
                                   "unqualified verse of praise"),
    ],
    why=(
        "Where SN 1.44 immediately before it withholds explanation entirely, this "
        "discourse withholds nothing but a name: it simply invites the hearer to "
        "&lsquo;behold him of peerless name,&rsquo; unpacking that invitation across "
        "four dense epithets &mdash; one who sees the subtle meaning, a giver of "
        "wisdom, unattached to sensuality, all-knowing, intelligent, and a great seer "
        "treading the noble road. No riddle, no reply, no narrative context is "
        "supplied &mdash; only concentrated praise."),
    guide=[
        ("An invitation to look, not a question to answer", [
            "Unlike this vagga's riddles, this verse doesn't ask anything of its "
            "hearer except attention: &lsquo;behold&rsquo; (<em>passa</em>) opens the "
            "verse, directing focus toward a figure named only by an epithet, "
            "&lsquo;peerless&rsquo; (<em>anoma</em>), before the epithets accumulate "
            "further."]),
        ("Six qualities in four compressed lines", [
            "In the space of a single short verse, six distinct qualities are named: "
            "seeing subtle meaning, giving wisdom, non-attachment to sensuality, "
            "omniscience, exceptional intelligence, and treading the noble road as a "
            "great seer. The density is itself notable &mdash; more descriptive terms "
            "packed into four lines than almost any other verse this brief in this "
            "collection."]),
        ("Unattachment paired with, not opposed to, wisdom", [
            "The verse pairs &lsquo;giver of wisdom&rsquo; directly with "
            "&lsquo;unattached to the realm of sensuality&rsquo; in the same line, "
            "treating detachment from sensual pleasure not as a separate achievement "
            "but as bound up with the capacity to give wisdom to others in the first "
            "place."]),
        ("The shortest pair in this vagga, read together", [
            "Placed immediately after SN 1.44's sealed, unanswered riddle, this "
            "discourse's unreserved clarity of praise makes an interesting contrast: "
            "one discourse in this vagga withholds meaning almost entirely, the very "
            "next withholds nothing but ambiguity, offering only direct, unqualified "
            "description."]),
    ],
    terms=[
        ("anoma",
         "&ldquo;peerless, unsurpassed&rdquo; &mdash; the epithet this discourse's "
         "title comes from, opening the verse's description."),
        ("sukhumatthadassiṁ",
         "&ldquo;one who sees the subtle meaning&rdquo; &mdash; the first quality "
         "named, describing insight into what is not obvious."),
        ("paññādadaṁ",
         "&ldquo;a giver of wisdom&rdquo; &mdash; the second quality, paired directly "
         "with detachment from sensuality in the same line."),
        ("kāmālaye asattaṁ",
         "&ldquo;unattached to the realm of sensuality&rdquo; &mdash; the third "
         "quality, linked in the verse to the capacity to give wisdom."),
        ("ariyamaggaṁ",
         "&ldquo;the noble road&rdquo; &mdash; what the great seer is described as "
         "&lsquo;treading&rsquo; in the verse's closing line."),
    ],
    text_intro=(
        "The discourse in full: a single dense verse of praise, naming six qualities "
        "in four lines. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.45:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the verse's opening word invite the hearer to do?",
         "opts": [
             "'Behold' (passa) the one described",
             "Answer a riddle",
             "Cross a flood",
             "Recite a refrain of their own"],
         "correct": 0,
         "expl": "An invitation to attention, not a question demanding a reply."},
        {"q": "How many distinct qualities does the verse name in its four lines?",
         "opts": [
             "Six",
             "One",
             "Twelve",
             "Two"],
         "correct": 0,
         "expl": "A notably dense concentration of epithets for such a short verse."},
        {"q": "What does the verse pair 'giver of wisdom' directly with?",
         "opts": [
             "Being unattached to the realm of sensuality",
             "Great physical strength",
             "Wealth and possessions",
             "Political power"],
         "correct": 0,
         "expl": "Treating detachment and the capacity to give wisdom as bound together."},
        {"q": "What does 'anoma' mean?",
         "opts": [
             "'Peerless, unsurpassed'",
             "'Ordinary, common'",
             "'Fearful'",
             "'A type of hell'"],
         "correct": 0,
         "expl": "This discourse's title and opening epithet."},
        {"q": "What is the great seer described as treading in the verse's closing line?",
         "opts": [
             "The noble road (ariyamagga)",
             "A path leading nowhere",
             "A path shared with ordinary travelers only",
             "No path is mentioned"],
         "correct": 0,
         "expl": "The verse's final image, closing its list of qualities."},
        {"q": "How does this discourse contrast with SN 1.44, immediately before it?",
         "opts": [
             "SN 1.44 withholds meaning almost entirely; this discourse offers direct, unqualified description",
             "Both discourses are identical in tone and content",
             "This discourse is far longer than SN 1.44",
             "This discourse is also an unanswered riddle"],
         "correct": 0,
         "expl": "The shortest pair of discourses in this vagga, contrasting in approach."},
        {"q": "Does this discourse pose a question that requires an answer?",
         "opts": [
             "No &mdash; it is entirely a verse of praise, with no question posed to anyone",
             "Yes, and the reply is given in a second verse",
             "Yes, but the question is left unanswered",
             "The discourse consists only of a question with no verse at all"],
         "correct": 0,
         "expl": "A direct address and description, not a riddle-and-answer structure."},
        {"q": "What does 'sukhumatthadassiṁ' mean?",
         "opts": [
             "'One who sees the subtle meaning'",
             "'One who never sees clearly'",
             "'One who avoids all meaning'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "The first of six qualities named in the verse."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set near Rājagaha",
             "Explicitly set at Kapilavatthu",
             "Explicitly set at Vesālī"],
         "correct": 0,
         "expl": "Like SN 1.44 immediately before it, no setting is given directly."},
        {"q": "How long is this discourse?",
         "opts": [
             "A single four-line verse, among the shortest in this collection",
             "Several pages of extended prose",
             "Exactly the same length as SN 1.50",
             "Longer than SN 1.41's five-stanza verse"],
         "correct": 0,
         "expl": "As brief as SN 1.44 immediately before it, though very different in content."},
    ],
    marginalia=[
        ("An invitation", [
            "behold him of peerless name &mdash;",
            "no riddle, just praise",
        ]),
        ("Six qualities, four lines", [
            "subtle sight, wisdom given,",
            "unattached, all-knowing",
        ]),
        ("Wisdom and detachment, paired", [
            "giving wisdom bound up",
            "with freedom from sensuality",
        ]),
        ("A contrast with SN 1.44", [
            "withheld meaning, then",
            "unreserved description",
        ]),
    ],
    further=[
        '<a href="%s/sn1.45/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.44.html">SN 1.44 &middot; One Root</a> &mdash; the discourse '
        "immediately before this one, and its sharpest possible contrast.",
        '<a href="sn-1.26.html">SN 1.26 &middot; Lamps</a> &mdash; an earlier discourse '
        "also naming the Buddha as supreme among a set of qualities.",
        "SN 1.46 &middot; Nymphs &mdash; the next discourse, an extended chariot "
        "allegory for the path itself.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.46 — Accharāsutta
# --------------------------------------------------------------------------- #
page(
    1, 46, "Accharā", "Nymphs",
    meta_title="SN 1.46 — Nymphs | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Accharāsutta — "
        "a deity fears a grove haunted by goblins and beguiled by nymphs, and the "
        "Buddha answers with an extended chariot allegory for the path to "
        "extinguishment. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a fearful question, answered by an extended "
                    "allegory"),
        ("Form", "A four-line question, answered by three four-line verses building a "
                 "single sustained image"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the chariot's parts "
                       "map cleanly onto named qualities once the allegory is seen "
                       "clearly"),
        ("An explicit inclusivity", "The closing line states directly that the "
                                    "vehicle described is available to &lsquo;any "
                                    "woman or man&rsquo; alike"),
    ],
    why=(
        "The question describes a real hazard: a grove called &lsquo;Deluding,&rsquo; "
        "resounding with alluring nymphs but haunted by a gang of goblins &mdash; how, "
        "the speaker asks, will I keep going through it? The answer doesn't address the "
        "grove directly. It describes a different path entirely and the vehicle for "
        "traveling it: a chariot called &lsquo;unswerving,&rsquo; fitted with the "
        "wheels of the teaching, its bench-back conscience, its upholstery "
        "mindfulness, the teaching itself as driver, and right view running ahead as "
        "guide. Anyone, woman or man, who has such a vehicle has already drawn near to "
        "extinguishment."),
    guide=[
        ("A dangerous grove, answered indirectly", [
            "The question's imagery is concrete and unsettling: a specific named place, "
            "&lsquo;Deluding&rsquo; (<em>mohana</em>), combining alluring beauty with "
            "genuine danger. Rather than offering advice for navigating that particular "
            "grove, the reply redirects entirely toward a different journey and a "
            "different vehicle altogether."]),
        ("A chariot built entirely from qualities", [
            "Every part of the described chariot is an abstraction made concrete: the "
            "path itself is called &lsquo;the direct way,&rsquo; heading to a place "
            "called &lsquo;fearless&rsquo;; the chariot is &lsquo;unswerving,&rsquo; "
            "fitted with wheels made of the teaching itself; its bench-back is "
            "conscience (<em>hiri</em>), its upholstery mindfulness "
            "(<em>sati</em>) &mdash; nothing about this vehicle is a literal, physical "
            "object."]),
        ("The teaching as driver, right view as scout", [
            "The verse's most striking claim assigns roles within the allegory "
            "precisely: the teaching itself (<em>dhamma</em>) drives, while right view "
            "(<em>sammādiṭṭhi</em>) runs out ahead, functioning as a scout or "
            "outrider rather than as the driver. Understanding correctly leads the way; "
            "the teaching as a whole steers."]),
        ("An explicit, stated inclusivity", [
            "The verse's closing line states plainly that &lsquo;any woman or "
            "man&rsquo; (<em>itthī vā puriso vā</em>) who has this vehicle draws near "
            "to extinguishment &mdash; an explicit inclusion this collection doesn't "
            "always state so directly, closing what could otherwise read as a purely "
            "abstract allegory on a note of universal availability."]),
    ],
    terms=[
        ("mohanaṁ",
         "&ldquo;Deluding,&rdquo; the name the question gives the dangerous grove it "
         "describes, combining beguiling nymphs with haunting goblins."),
        ("ujuko nāma so maggo",
         "&ldquo;that path is called &lsquo;the direct way&rsquo;&rdquo; &mdash; the "
         "reply's redirection toward an entirely different journey."),
        ("hirī tassa apālambo",
         "&ldquo;conscience is its bench-back&rdquo; &mdash; the first of several "
         "abstract qualities built directly into the chariot's physical structure."),
        ("dhammaṁ sārathiṁ brūmi",
         "&ldquo;I say the teaching is the driver&rdquo; &mdash; assigning the "
         "controlling role in the allegory to the teaching as a whole."),
        ("itthī vā puriso vā",
         "&ldquo;any woman or man&rdquo; &mdash; the verse's explicit, stated "
         "inclusivity in naming who can possess this vehicle."),
    ],
    text_intro=(
        "The discourse in full: a fearful question about a dangerous grove, answered by "
        "an extended chariot allegory for the path. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A dangerous, deluding grove"),
        ("p", "&sect;1", "sn1.46:1.1-1.4"),
        ("h3", "A chariot built from named qualities"),
        ("p", "&sect;2", "sn1.46:2.1-4.4"),
    ],
    quiz=[
        {"q": "What does the opening question describe?",
         "opts": [
             "A grove called 'Deluding,' resounding with nymphs and haunted by goblins",
             "A burning house",
             "A vast congregation of deities",
             "A riddle about numbers"],
         "correct": 0,
         "expl": "A concrete image of danger combining beauty and threat."},
        {"q": "Does the reply give advice for navigating this specific grove?",
         "opts": [
             "No &mdash; it redirects entirely toward a different path and vehicle",
             "Yes, in exhaustive practical detail",
             "Yes, but only by naming the goblins individually",
             "The reply refuses to answer at all"],
         "correct": 0,
         "expl": "A redirection of the whole question toward an extended allegory."},
        {"q": "What is the chariot in the allegory fitted with?",
         "opts": [
             "Wheels made of the teaching itself",
             "Wheels made of gold",
             "No wheels; it travels without them",
             "Wheels made of stone"],
         "correct": 0,
         "expl": "Cakkehi dhammamayehi &mdash; an abstraction made structurally concrete."},
        {"q": "What two qualities form the chariot's bench-back and upholstery?",
         "opts": [
             "Conscience and mindfulness",
             "Wealth and fame",
             "Speed and strength",
             "Fear and doubt"],
         "correct": 0,
         "expl": "Hirī as bench-back, sati as upholstery."},
        {"q": "What role does the teaching play in the allegory, and what role does right view play?",
         "opts": [
             "The teaching is the driver; right view runs ahead as a scout or outrider",
             "Right view is the driver; the teaching runs ahead",
             "Neither has any role in the allegory",
             "Both are described as passengers only"],
         "correct": 0,
         "expl": "Distinct, precisely assigned roles within the chariot allegory."},
        {"q": "What does the verse's closing line state explicitly?",
         "opts": [
             "That any woman or man who has this vehicle draws near to extinguishment",
             "That only men can attain this vehicle",
             "That only deities can attain this vehicle",
             "That this vehicle is available to no one at all"],
         "correct": 0,
         "expl": "Itthī vā puriso vā &mdash; a stated, explicit inclusivity."},
        {"q": "What does 'mohanaṁ' mean?",
         "opts": [
             "'Deluding' &mdash; the name given to the dangerous grove",
             "'Fearless'",
             "'Unswerving'",
             "'The direct way'"],
         "correct": 0,
         "expl": "The grove's own name in the opening question."},
        {"q": "Where is the described path said to lead?",
         "opts": [
             "To a place called 'fearless'",
             "Back to the deluding grove",
             "Nowhere; the path is said to be endless",
             "To a literal physical city"],
         "correct": 0,
         "expl": "Abhayassa nagaraṁ &mdash; the allegory's destination."},
        {"q": "How many verses does the reply use to build its chariot allegory?",
         "opts": [
             "Three",
             "One",
             "Ten",
             "Five"],
         "correct": 0,
         "expl": "A single sustained image developed across three stanzas."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set within the deluding grove itself",
             "Explicitly set at Kapilavatthu",
             "Explicitly set at Vesālī"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
    ],
    marginalia=[
        ("A grove, named and feared", [
            "Deluding &mdash; nymphs and goblins,",
            "how will I keep going?",
        ]),
        ("A different path entirely", [
            "the direct way,",
            "heading to fearless",
        ]),
        ("A chariot of qualities", [
            "wheels of the teaching,",
            "conscience the bench-back",
        ]),
        ("Open to any who have it", [
            "any woman or man &mdash;",
            "near to extinguishment",
        ]),
    ],
    further=[
        '<a href="%s/sn1.46/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.45.html">SN 1.45 &middot; Peerless</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.29.html">SN 1.29 &middot; Four Wheels</a> &mdash; an earlier '
        "discourse in this collection also using a vehicle as an extended image.",
        "SN 1.47 &middot; Planters &mdash; the next discourse, on whose merit grows "
        "continually, day and night.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.47 — Vanaropasutta
# --------------------------------------------------------------------------- #
page(
    1, 47, "Vanaropa", "Planters",
    meta_title="SN 1.47 — Planters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vanaropasutta "
        "— a question on whose merit keeps growing day and night, answered by naming "
        "those who plant groves, build bridges, dig wells, and give shelter to "
        "travelers and mendicants. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; a question answered by naming specific "
                    "civic acts"),
        ("Form", "A four-line question, answered by a matching four-line verse that "
                 "then restates the question's own opening lines as its conclusion"),
        ("Length", "~45 seconds to read"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; direct in form, "
                       "concerned with concrete, practical acts"),
        ("A civic, not only personal, kind of merit", "The specific deeds named "
                                                       "&mdash; groves, bridges, wells, "
                                                       "lodgings &mdash; all benefit "
                                                       "strangers who will never meet "
                                                       "the giver"),
    ],
    why=(
        "The question asks something practical: whose merit keeps growing, day and "
        "night without pause, and which people, firm in principle and accomplished in "
        "conduct, are headed for heaven? The answer doesn't point to meditation or "
        "doctrine but to a specific set of civic acts: planting parks and groves, "
        "building bridges, providing a drinking place and a well, and giving shelter "
        "to travelers and mendicants &mdash; deeds whose benefit continues to "
        "accumulate precisely because they keep serving people the giver will never "
        "personally encounter."),
    guide=[
        ("Merit that grows without further effort", [
            "The question's framing &mdash; merit growing &lsquo;by day and by "
            "night&rsquo; &mdash; describes something distinct from a single completed "
            "act of giving. What is named in reply are not one-time gifts but standing "
            "infrastructure: a planted grove keeps providing shade, a built bridge keeps "
            "being crossed, a dug well keeps being drawn from, long after the initial "
            "act is finished."]),
        ("Benefit to strangers, not only to known recipients", [
            "Every example named benefits people the giver will likely never meet: "
            "travelers passing through, thirsty strangers at a well, mendicants seeking "
            "shelter. Unlike gifts given directly to a specific known person, these acts "
            "extend benefit indefinitely outward, to whoever happens to make use of "
            "them."]),
        ("A verse that returns to its own question as its answer", [
            "The reply's structure is notably circular: after naming the specific acts, "
            "its closing two lines restate almost exactly the question's own opening "
            "two lines &mdash; &lsquo;their merit always grows, by day and by "
            "night&rsquo; &mdash; confirming that the acts just listed are precisely "
            "what the question was asking about, rather than introducing any new claim."]),
        ("A concrete companion to this vagga's other giving-themed discourses", [
            "Where SN 1.42 named categories of gift matched to specific benefits and SN "
            "1.43 addressed giving more abstractly, this discourse grounds the same "
            "broad theme in specific, identifiable civic works &mdash; a practical "
            "complement to this vagga's more abstract treatments of generosity."]),
    ],
    terms=[
        ("vanaropa",
         "&ldquo;planting parks or groves&rdquo; &mdash; this discourse's title, and "
         "the first specific act the reply names."),
        ("setukārakā",
         "&ldquo;those who build a bridge&rdquo; &mdash; the second act named, "
         "extending benefit to travelers indefinitely."),
        ("papañca udapānañca",
         "&ldquo;a drinking place and well&rdquo; &mdash; the third act, providing "
         "water to strangers who will never be known personally."),
        ("ārāmadā",
         "&ldquo;those who give monastic quarters&rdquo; &mdash; the fourth act, "
         "already met as this collection's highest-ranked single gift at SN 1.42."),
        ("divā ca ratto ca",
         "&ldquo;by day and by night&rdquo; &mdash; the phrase framing both the "
         "question and its answer, describing merit that accumulates without pause."),
    ],
    text_intro=(
        "The discourse in full: a question on continually growing merit, answered by "
        "naming specific, lasting civic acts. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn1.47:1.1-1.4"),
        ("p", "&sect;2", "sn1.47:2.1-3.4"),
    ],
    quiz=[
        {"q": "What does the opening question ask about?",
         "opts": [
             "Whose merit keeps growing continually, day and night",
             "How many lamps light the world",
             "Who can untangle the human tangle",
             "What produces strength, beauty, happiness, and vision"],
         "correct": 0,
         "expl": "A question about ongoing, rather than one-time, merit."},
        {"q": "What four specific acts does the reply name?",
         "opts": [
             "Planting groves, building bridges, providing water, and giving monastic quarters",
             "Meditation, chanting, fasting, and silence",
             "Giving food, clothing, a vehicle, and a lamp",
             "Ethics, concentration, wisdom, and liberation"],
         "correct": 0,
         "expl": "Concrete, lasting civic works rather than personal spiritual practices."},
        {"q": "Why does this discourse's merit keep growing without further effort?",
         "opts": [
             "Because the acts named are standing infrastructure that keeps benefiting people over time",
             "Because merit automatically doubles every day regardless of any action",
             "Because the giver must repeat the act daily",
             "The discourse doesn't explain why merit grows this way"],
         "correct": 0,
         "expl": "A grove, bridge, or well continues serving people long after the initial act."},
        {"q": "Who benefits from the acts named in this discourse?",
         "opts": [
             "Strangers the giver will likely never personally meet",
             "Only the giver's immediate family",
             "Only deities, never humans",
             "No one benefits; the acts are purely symbolic"],
         "correct": 0,
         "expl": "Travelers, thirsty strangers, and mendicants seeking shelter."},
        {"q": "How does the reply's closing structure relate to the opening question?",
         "opts": [
             "It restates the question's own opening lines almost exactly, confirming the acts just named answer it",
             "It contradicts the question entirely",
             "It asks an entirely new, unrelated question",
             "It ignores the question and changes the subject"],
         "correct": 0,
         "expl": "A notably circular structure, closing on the same phrase that opened the question."},
        {"q": "What earlier discourse in this vagga already ranked giving monastic quarters highly?",
         "opts": [
             "SN 1.42, which named it 'the giver of all'",
             "SN 1.41, on fire",
             "SN 1.44, on one root",
             "No earlier discourse mentions monastic quarters"],
         "correct": 0,
         "expl": "A recurring theme within this vagga's cluster of giving-related discourses."},
        {"q": "What does 'divā ca ratto ca' mean?",
         "opts": [
             "'By day and by night'",
             "'Never, under any circumstances'",
             "'Only once in a lifetime'",
             "'A type of deity'"],
         "correct": 0,
         "expl": "The phrase framing both the question and its answer."},
        {"q": "How does this discourse's approach to giving compare to SN 1.43's?",
         "opts": [
             "It grounds the theme in specific, identifiable civic works, complementing SN 1.43's more abstract treatment",
             "It is identical in every respect to SN 1.43",
             "It rejects everything SN 1.43 claims about giving",
             "It has no relationship to SN 1.43 at all"],
         "correct": 0,
         "expl": "A practical complement within this vagga's broader concern with generosity."},
        {"q": "What does 'setukārakā' mean?",
         "opts": [
             "'Those who build a bridge'",
             "'Those who dig graves'",
             "'Those who plant trees'",
             "'Those who give food'"],
         "correct": 0,
         "expl": "The second specific act named in the reply."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not narrated in the source text; presumably the same recurring frame as the rest of this vagga",
             "Explicitly set beside a river",
             "Explicitly set at Kapilavatthu",
             "Explicitly set at Vesālī"],
         "correct": 0,
         "expl": "Like several discourses in this vagga, no setting is given directly."},
    ],
    marginalia=[
        ("A question about ongoing merit", [
            "whose merit grows",
            "by day and by night?",
        ]),
        ("Four lasting acts", [
            "groves planted, bridges built,",
            "wells dug, shelter given",
        ]),
        ("Benefit to strangers", [
            "travelers never met,",
            "served indefinitely",
        ]),
        ("The question, echoed as answer", [
            "the same phrase returns &mdash;",
            "this is what was asked",
        ]),
    ],
    further=[
        '<a href="%s/sn1.47/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.46.html">SN 1.46 &middot; Nymphs</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.42.html">SN 1.42 &middot; Giving What?</a> &mdash; the earlier '
        "discourse already ranking monastic quarters as a comprehensive gift.",
        "SN 1.48 &middot; Jeta's Grove &mdash; the next discourse, praising the grove "
        "itself and naming Sāriputta directly.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.48 — Jetavanasutta
# --------------------------------------------------------------------------- #
page(
    1, 48, "Jetavana", "Jeta's Grove",
    meta_title="SN 1.48 — Jeta's Grove | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Jetavanasutta "
        "— a deity's joy at the grove that hosted the Buddha, a teaching that conduct "
        "purifies rather than clan or wealth, and singular praise for Sāriputta by "
        "name. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga, at Jeta&rsquo;s Grove "
                    "itself"),
        ("Speakers", "Not named explicitly; a single sustained verse moving from joy at "
                    "a place, to a teaching on purification, to praise for a named "
                    "individual"),
        ("Form", "Four four-line stanzas, moving from personal feeling to doctrine to "
                 "individual praise"),
        ("Length", "~1 minute to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form, "
                       "with real social and doctrinal weight in its middle stanzas"),
        ("A named individual, singled out", "This discourse names Sāriputta directly "
                                            "and ranks him as, at best, matched but not "
                                            "exceeded even among liberated mendicants"),
    ],
    why=(
        "This discourse opens on a note of simple feeling: this is indeed that Jeta's "
        "Grove, frequented by the Saṅgha of seers, where the King of Dhamma himself "
        "stayed &mdash; it brings me joy. From there it moves to a direct claim about "
        "what actually purifies a person: deeds, knowledge, principle, ethical conduct, "
        "and an excellent livelihood &mdash; not clan or wealth, categories a person is "
        "simply born into or accumulates. It closes with focused praise for one "
        "individual by name: Sāriputta, said to be so full of wisdom, ethics, and "
        "peace that even a mendicant who has fully crossed over might, at best, only "
        "equal him."),
    guide=[
        ("A place, and the feeling it evokes", [
            "The opening stanza is unusually personal for this collection: not a "
            "riddle, not a teaching, but a direct expression of joy at recognizing a "
            "specific, familiar place &mdash; the same grove frequented by the "
            "&lsquo;Saṅgha of seers&rsquo; and once home to the &lsquo;King of "
            "Dhamma.&rsquo;"]),
        ("Purification by conduct, not by birth", [
            "The second stanza makes an explicit, pointed claim: mortals are purified "
            "by deeds, knowledge, principle, ethics, and livelihood &mdash; "
            "&lsquo;not by clan or wealth.&rsquo; This directly rejects the idea that "
            "birth into a particular family or the accumulation of riches has any "
            "bearing on genuine purification, a claim with real social weight in its "
            "original context."]),
        ("Examining the teaching rationally, not merely accepting it", [
            "The third stanza adds a further instruction: an astute person, seeing "
            "what's good for themselves, would &lsquo;examine the teaching "
            "rationally&rsquo; (<em>dhammaṁ anuvicceyya</em>) rather than accept it on "
            "authority alone, and only then be purified by it &mdash; a call to "
            "reasoned investigation rather than passive acceptance."]),
        ("Sāriputta, named and ranked", [
            "The closing stanza breaks from generality entirely to name one person: "
            "Sāriputta, described as full of wisdom, ethics, and peace, with even a "
            "mendicant who has &lsquo;crossed over&rsquo; &mdash; presumably a fellow "
            "arahant &mdash; said to at best equal him, not exceed him. This is a rare, "
            "direct, individually named endorsement in a collection that otherwise "
            "speaks mostly in general terms about qualities and attainments."]),
    ],
    terms=[
        ("jetavana",
         "&ldquo;Jeta's Grove&rdquo; &mdash; this discourse's title and its setting, "
         "the same grove named throughout this collection's recurring frame."),
        ("dhammarājā",
         "&ldquo;the King of Dhamma&rdquo; &mdash; the verse's epithet for the Buddha, "
         "describing his former residence at this grove."),
        ("na jaccā na dhanena vā",
         "&ldquo;not by clan or wealth&rdquo; &mdash; the verse's direct rejection of "
         "birth and riches as sources of purification."),
        ("dhammaṁ anuvicceyya",
         "&ldquo;having examined the teaching rationally&rdquo; &mdash; the verse's "
         "call to reasoned investigation, rather than passive acceptance, before "
         "purification follows."),
        ("sāriputto",
         "Sāriputta, the individual mendicant named and praised directly in this "
         "discourse's closing stanza, for wisdom, ethics, and peace together."),
    ],
    text_intro=(
        "The discourse in full: joy at a familiar place, a teaching on what purifies, "
        "and praise for Sāriputta by name. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Joy at a familiar grove"),
        ("p", "&sect;1", "sn1.48:1.1-1.4"),
        ("h3", "What actually purifies"),
        ("p", "&sect;2", "sn1.48:2.1-3.4"),
        ("h3", "Sāriputta, named directly"),
        ("p", "&sect;3", "sn1.48:4.1-4.4"),
    ],
    quiz=[
        {"q": "What feeling does the opening stanza express?",
         "opts": [
             "Joy at recognizing Jeta's Grove, where the Buddha himself once stayed",
             "Fear of a haunted grove",
             "Confusion about where the Buddha is staying",
             "Anger at being denied entry to the grove"],
         "correct": 0,
         "expl": "An unusually personal, direct expression of feeling for this collection."},
        {"q": "What does the second stanza claim actually purifies a person?",
         "opts": [
             "Deeds, knowledge, principle, ethics, and livelihood &mdash; not clan or wealth",
             "Clan and wealth alone",
             "Physical strength alone",
             "Nothing can purify a person"],
         "correct": 0,
         "expl": "A direct, pointed rejection of birth and riches as sources of purification."},
        {"q": "What does the third stanza recommend doing with the teaching, rather than merely accepting it?",
         "opts": [
             "Examining it rationally (dhammaṁ anuvicceyya)",
             "Memorizing it without any reflection",
             "Ignoring it entirely",
             "Accepting it purely on authority, without question"],
         "correct": 0,
         "expl": "A call to reasoned investigation rather than passive acceptance."},
        {"q": "Who is named and praised in the closing stanza?",
         "opts": [
             "Sāriputta",
             "Venerable Mogharāja",
             "Venerable Samiddhi",
             "Ghaṭīkāra"],
         "correct": 0,
         "expl": "A rare, direct, individually named endorsement in this collection."},
        {"q": "How is Sāriputta ranked relative to a mendicant who has 'crossed over'?",
         "opts": [
             "Such a mendicant might, at best, only equal him",
             "Such a mendicant would always clearly exceed him",
             "Sāriputta is ranked below all other mendicants",
             "No comparison is made at all"],
         "correct": 0,
         "expl": "A striking claim, ranking him at or near the highest possible standard."},
        {"q": "What three qualities is Sāriputta specifically described as full of?",
         "opts": [
             "Wisdom, ethics, and peace",
             "Wealth, fame, and power",
             "Strength, beauty, and speed",
             "Anger, conceit, and doubt"],
         "correct": 0,
         "expl": "The three qualities named directly in the closing stanza."},
        {"q": "What does 'dhammarājā' mean?",
         "opts": [
             "'The King of Dhamma' &mdash; an epithet for the Buddha",
             "'The King of Wealth'",
             "'A type of deity'",
             "'A monastery near Rājagaha'"],
         "correct": 0,
         "expl": "Describing the Buddha's former residence at this specific grove."},
        {"q": "How many stanzas does this discourse contain, and what do they move through?",
         "opts": [
             "Four, moving from personal feeling to doctrine to individual praise",
             "One stanza only, containing no development",
             "Twelve, covering many unrelated topics",
             "Four, all repeating the same single claim"],
         "correct": 0,
         "expl": "A clear progression across the discourse's structure."},
        {"q": "What claim does the second stanza reject about purification?",
         "opts": [
             "That birth into a particular clan or accumulated wealth has any bearing on it",
             "That deeds or ethics have any bearing on it",
             "That purification is possible at all",
             "That knowledge has any bearing on purification"],
         "correct": 0,
         "expl": "A claim with real social weight in its original context."},
        {"q": "What is the setting of this discourse?",
         "opts": [
             "Not explicitly narrated, but at Jeta's Grove itself, given the discourse's subject",
             "Explicitly set at Kapilavatthu",
             "Explicitly set at Vesālī",
             "Explicitly set at the Hot Springs Monastery"],
         "correct": 0,
         "expl": "The grove being praised is the same one named throughout this collection's recurring frame."},
    ],
    marginalia=[
        ("A place, recognized with joy", [
            "Jeta&rsquo;s Grove &mdash;",
            "where the King of Dhamma stayed",
        ]),
        ("Purified by deeds, not birth", [
            "not by clan or wealth,",
            "but by conduct and knowledge",
        ]),
        ("Examined, not merely accepted", [
            "the teaching, weighed rationally,",
            "then purifying",
        ]),
        ("Sāriputta, named", [
            "wisdom, ethics, peace &mdash;",
            "matched at best, not exceeded",
        ]),
    ],
    further=[
        '<a href="%s/sn1.48/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.47.html">SN 1.47 &middot; Planters</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.1.html">SN 1.1 &middot; Crossing the Flood</a> &mdash; this '
        "collection&rsquo;s opening discourse, set at the same Jeta&rsquo;s Grove.",
        "SN 1.49 &middot; Stingy &mdash; the next discourse, contrasting the karmic "
        "destinations of the miserly and the generous.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.49 — Maccharisutta (second discourse of this title in this collection)
# --------------------------------------------------------------------------- #
page(
    1, 49, "Macchari", "Stingy",
    meta_title="SN 1.49 — Stingy | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second "
        "Maccharisutta — two rounds of question and answer contrasting the detailed "
        "karmic destinations of the stingy and the generous, in this life and the "
        "next. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "Not named explicitly; two full rounds of question and answer, "
                    "addressing the Buddha as &lsquo;Gotama&rsquo;"),
        ("Form", "Two matched question-and-answer pairs, tracing detailed rebirth "
                 "outcomes for two opposite characters"),
        ("Length", "~2 minutes to read"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct in form, "
                       "unusually specific in its cosmological detail"),
        ("A second discourse of this title", "This discourse shares its Pali title, "
                                             "Maccharisutta, with SN 1.32, though the "
                                             "two are otherwise unrelated in content and "
                                             "structure"),
    ],
    why=(
        "This discourse traces two full, parallel accounts of karmic consequence in "
        "unusually specific detail. The first asks about people who are stingy, "
        "miserly, and abusive, actively obstructing others who wish to give: they are "
        "reborn in hell, the animal realm, or Yama's world, and if they return to human "
        "life, into a poor family lacking even what they hope for from others. The "
        "second asks about the bountiful, confident in the Buddha, the teaching, and "
        "the Saṅgha: they illuminate the heavens wherever they're reborn, and if they "
        "return to human life, it is into a rich family where everything is easy to "
        "find."),
    guide=[
        ("Two questions, addressed to 'Gotama' directly", [
            "Both rounds of this discourse address the Buddha by his clan name, "
            "Gotama, the same informal address already met at SN 1.23 &mdash; and both "
            "explicitly acknowledge understanding the previous answer before asking a "
            "further question, giving this exchange a genuinely conversational, "
            "step-by-step quality unusual for this collection."]),
        ("Specific realms, not a generalized 'bad rebirth'", [
            "The first answer doesn't simply say the stingy suffer; it names three "
            "specific possible destinations &mdash; hell, the animal realm, or Yama's "
            "world &mdash; before describing what happens if they do return to human "
            "life: birth into poverty where even hoped-for help from others doesn't "
            "materialize."]),
        ("Illuminating the heavens, and abundance if reborn human", [
            "The second answer is structured as a precise mirror of the first: the "
            "generous illuminate the heavens wherever reborn, and if they return to "
            "human life, it is into wealth where clothes, food, pleasure, and play "
            "&mdash; the same four items named as lacking for the stingy &mdash; are "
            "instead easy to find."]),
        ("Present and future consequence, both named explicitly", [
            "Both answers close with the same structural claim: 'this is the result in "
            "the present life, and in the next, a good' or 'bad destination' &mdash; "
            "making explicit that the consequences described aren't confined to some "
            "distant future rebirth alone, but shape the present life as well."]),
    ],
    terms=[
        ("maccharī",
         "&ldquo;stingy&rdquo; &mdash; this discourse's title, shared with SN 1.32 "
         "though the two discourses are otherwise unrelated."),
        ("vinipātaṁ",
         "&ldquo;obstacles&rdquo; &mdash; what the stingy are described as setting up "
         "specifically for others who wish to give."),
        ("yamalokaṁ",
         "&ldquo;Yama's world&rdquo; &mdash; one of three specific destinations named "
         "for the stingy, alongside hell and the animal realm."),
        ("saggaṁ obhāsayanti",
         "&ldquo;they illuminate the heavens&rdquo; &mdash; the description given for "
         "the generous, wherever they happen to be reborn."),
        ("vigatamalā",
         "&ldquo;rid of stinginess&rdquo; &mdash; the specific quality named for the "
         "generous, framed as an absence of the first question's central fault."),
    ],
    text_intro=(
        "The discourse in full: two parallel accounts of karmic consequence, for the "
        "stingy and for the generous. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The stingy: a question, and its answer"),
        ("p", "&sect;1", "sn1.49:1.1-2.4"),
        ("p", "&sect;2", "sn1.49:3.1-5.6"),
        ("h3", "The generous: a second question, and its answer"),
        ("p", "&sect;3", "sn1.49:6.1-7.6"),
        ("p", "&sect;4", "sn1.49:8.1-10.4"),
    ],
    quiz=[
        {"q": "What does the first question ask about?",
         "opts": [
             "The karmic result and future life of people who are stingy, miserly, and abusive",
             "How many lamps light the world",
             "What produces strength and beauty",
             "Who can untangle the human tangle"],
         "correct": 0,
         "expl": "A question about consequence, not a riddle about identity."},
        {"q": "What three specific destinations does the first answer name for the stingy?",
         "opts": [
             "Hell, the animal realm, or Yama's world",
             "The Garden of Delight only",
             "The Pure Abodes only",
             "No specific destination is named"],
         "correct": 0,
         "expl": "Named directly, rather than left as a vague 'bad rebirth.'"},
        {"q": "What happens if the stingy return to human life, according to the first answer?",
         "opts": [
             "They're born into a poor family lacking even what they hope for from others",
             "They're born wealthy despite their stinginess",
             "They're immediately liberated regardless of past conduct",
             "They can never return to human life at all"],
         "correct": 0,
         "expl": "A specific description of continued hardship in human rebirth."},
        {"q": "What does the second question ask about?",
         "opts": [
             "The karmic result and future life of the bountiful, confident in the Buddha, teaching, and Saṅgha",
             "The same question as the first, repeated without change",
             "How to become stingy",
             "A completely unrelated topic"],
         "correct": 0,
         "expl": "A parallel question about the opposite character."},
        {"q": "How does the second answer describe the generous, wherever they are reborn?",
         "opts": [
             "They illuminate the heavens",
             "They remain invisible and unnoticed",
             "They are immediately reborn as stingy people",
             "No description is given"],
         "correct": 0,
         "expl": "Saggaṁ obhāsayanti &mdash; a vivid image of radiant presence."},
        {"q": "What happens if the generous return to human life, according to the second answer?",
         "opts": [
             "They're born into a rich family where clothes, food, pleasure, and play are easy to find",
             "They're born into poverty despite their generosity",
             "They can never return to human life at all",
             "No description of human rebirth is given"],
         "correct": 0,
         "expl": "A precise mirror of the hardship described for the stingy."},
        {"q": "How does each answer describe the timing of its stated consequences?",
         "opts": [
             "As applying both to the present life and to the next",
             "As applying only to some distant future life, never the present",
             "As applying only to the present life, never affecting rebirth",
             "No timing is specified in either answer"],
         "correct": 0,
         "expl": "Both answers close by naming present and future consequence explicitly."},
        {"q": "How does the questioner address the Buddha in this discourse?",
         "opts": [
             "By his clan name, Gotama, as at SN 1.23",
             "By a formal royal title only",
             "The questioner never addresses the Buddha directly",
             "By calling him 'Great Hero' exclusively"],
         "correct": 0,
         "expl": "The same informal address already met earlier in this collection."},
        {"q": "What earlier discourse in this collection shares this discourse's Pali title?",
         "opts": [
             "SN 1.32, though the two are otherwise unrelated in content",
             "SN 1.1, on crossing the flood",
             "SN 1.21, on a sword",
             "No earlier discourse shares this title"],
         "correct": 0,
         "expl": "Both titled Maccharisutta, but structurally and thematically distinct."},
        {"q": "What does 'vinipātaṁ' describe in this discourse?",
         "opts": [
             "The obstacles the stingy set up for others who wish to give",
             "A specific heavenly realm",
             "A type of meditation",
             "A monastery near Sāvatthī"],
         "correct": 0,
         "expl": "Named as part of the stingy's described behavior in the opening question."},
    ],
    marginalia=[
        ("A question about the stingy", [
            "hell, animal realm, Yama&rsquo;s world &mdash;",
            "and poverty if human again",
        ]),
        ("A mirrored question", [
            "confident in Buddha, teaching, Saṅgha &mdash;",
            "what result do they reap?",
        ]),
        ("Illuminating the heavens", [
            "wherever reborn,",
            "radiant with generosity",
        ]),
        ("Present and future, both named", [
            "this life, and the next &mdash;",
            "consequence stated plainly",
        ]),
    ],
    further=[
        '<a href="%s/sn1.49/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.48.html">SN 1.48 &middot; Jeta&rsquo;s Grove</a> &mdash; the '
        "discourse immediately before this one.",
        '<a href="sn-1.32.html">SN 1.32 &middot; Stinginess</a> &mdash; an earlier, '
        "differently structured discourse sharing this one's Pali title.",
        "SN 1.50 &middot; With Ghaṭīkāra &mdash; the next discourse, this vagga's "
        "last, and a reunion between old friends across two Buddha-eras.",
    ],
)


# --------------------------------------------------------------------------- #
# SN 1.50 — Ghaṭīkārasutta (closes the Ādittavagga)
# --------------------------------------------------------------------------- #
page(
    1, 50, "Ghaṭīkāra", "With Ghaṭīkāra",
    meta_title="SN 1.50 — With Ghaṭīkāra | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ghaṭīkārasutta — a deity reports seven liberated mendicants, then reveals "
        "himself as Ghaṭīkāra the potter, the Buddha's own closest friend in a past "
        "life under the previous Buddha Kassapa. Closes the Ādittavagga. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not narrated in this discourse's source text; presumably the same "
                    "recurring frame as the rest of this vagga"),
        ("Speakers", "An unnamed deity, gradually revealed across the discourse to be "
                    "Ghaṭīkāra, and the Buddha"),
        ("Form", "A long, building exchange: a report, a naming, a deepening question, "
                 "a startled follow-up, and a personal revelation"),
        ("Length", "~3.5 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; narratively rich "
                       "rather than doctrinally dense, rewarding attention to its "
                       "unfolding structure"),
        ("Closing this vagga", "The tenth and last discourse of the Ādittavagga, closing "
                               "on a reunion spanning two entire Buddha-eras"),
    ],
    why=(
        "A deity reports something remarkable: seven mendicants reborn in Aviha, one of "
        "the Pure Abodes, have been fully freed. Asked to name them, the deity lists "
        "seven mendicants by name, then explains that they understood none other than "
        "the Buddha's own teaching on the cessation of name and form. What startles the "
        "Buddha is not the report itself but its depth &mdash; how does this deity "
        "understand something so profound? The answer unfolds into a revelation: in a "
        "past life, under the previous Buddha Kassapa, this deity was Ghaṭīkāra the "
        "potter &mdash; and the Buddha's own closest friend, in that ancient lifetime, "
        "long before either of them became what they are now."),
    guide=[
        ("Seven mendicants, freed in the Pure Abodes", [
            "Aviha, where these seven mendicants were reborn, is one of the five Pure "
            "Abodes (<em>suddhāvāsa</em>) already met in this collection at SN 1.37, "
            "reserved for non-returners. Their being reported as now &lsquo;freed&rsquo; "
            "means they have progressed from non-return to full arahantship in that "
            "realm &mdash; a specific, tracked spiritual trajectory rather than a vague "
            "claim of attainment."]),
        ("Two names with their own stories elsewhere in the canon", [
            "Among the seven named &mdash; Upaka, Palagaṇḍa, Pukkusāti, Bhaddiya, "
            "Bhaddadeva, Bāhudanti, and Piṅgiya &mdash; two are traditionally identified "
            "with figures whose stories appear elsewhere in the canon. Upaka is "
            "traditionally identified with the ascetic who met the newly awakened "
            "Buddha on the road to Varanasi and walked away unconvinced; Pukkusāti is "
            "traditionally identified with the monk of the Dhātuvibhaṅga Sutta (MN 140), "
            "who received a profound teaching from the Buddha without recognizing him, "
            "and who died shortly after, declared to have reached non-return. If these "
            "identifications are correct, this discourse quietly reports that both men "
            "eventually reached full liberation, whatever their earlier stories left "
            "unresolved."]),
        ("A question that turns from the seven to the deity itself", [
            "Once the deity explains that all seven understood the Buddha's own "
            "teaching on the cessation of name and form, the Buddha's next question "
            "shifts entirely: not about the seven mendicants any longer, but about the "
            "deity's own understanding &mdash; 'the words you say are deep, hard to "
            "understand&hellip; whose teaching did you understand that you can say such "
            "things?'"]),
        ("Ghaṭīkāra revealed: a potter, a friend, a past life", [
            "The deity's answer is a full personal history: in the past, in Vebhaliṅga, "
            "a potter named Ghaṭīkāra, a devoted lay follower who cared for his parents "
            "under the previous Buddha Kassapa, celibate and spiritual &mdash; and, "
            "crucially, the Buddha's own comrade, living in the same village in that "
            "ancient lifetime. This same relationship between Ghaṭīkāra and the "
            "bodhisatta who would eventually become this Buddha is told at much greater "
            "length in the Ghaṭīkārasutta (MN 81)."]),
        ("Both of them, evolved, in their final body", [
            "The Buddha confirms every detail exactly, addressing the deity by his "
            "clan-name, Bhaggava. The discourse's closing line describes both of "
            "them &mdash; the Buddha and his ancient friend, now a deity &mdash; as "
            "&lsquo;evolved, bearing their final body,&rsquo; a quiet symmetry: two old "
            "friends from a distant, previous Buddha-era, meeting once more at the very "
            "end of both their journeys through repeated rebirth."]),
    ],
    terms=[
        ("aviha",
         "one of the five Pure Abode realms, already met at SN 1.37, where the seven "
         "mendicants named in this discourse were reborn before reaching full "
         "liberation."),
        ("upaka",
         "traditionally identified with the ascetic who met the newly awakened Buddha "
         "on the road to Varanasi and walked away unconvinced &mdash; named here among "
         "the seven now fully freed."),
        ("pukkusāti",
         "traditionally identified with the monk of the Dhātuvibhaṅga Sutta (MN 140), "
         "who died shortly after receiving a profound teaching from the Buddha without "
         "recognizing him."),
        ("ghaṭīkāra",
         "&ldquo;the potter&rdquo; &mdash; the identity this discourse's speaking "
         "deity reveals as their own past life, under the previous Buddha Kassapa."),
        ("bhaggava",
         "the clan-name the Buddha uses to address the deity once Ghaṭīkāra's identity "
         "is revealed, confirming the shared past directly."),
    ],
    text_intro=(
        "The discourse in full: a report of seven mendicants freed, and a deity's "
        "gradual revelation as the Buddha's own friend from a past life. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A deity reports seven mendicants, freed"),
        ("p", "&sect;1", "sn1.50:1.1-1.4"),
        ("h3", "Who are they?"),
        ("p", "&sect;2", "sn1.50:2.1-3.6"),
        ("h3", "Whose teaching did they understand?"),
        ("p", "&sect;3", "sn1.50:4.1-6.4"),
        ("h3", "A startled question, turned back on the deity"),
        ("p", "&sect;4", "sn1.50:7.1-7.4"),
        ("h3", "A revelation: Ghaṭīkāra the potter"),
        ("p", "&sect;5", "sn1.50:8.1-9.4"),
        ("p", "&sect;6", "sn1.50:10.1-10.4"),
        ("h3", "Confirmed: old friends, meeting once more"),
        ("p", "&sect;7", "sn1.50:11.1-13.4"),
    ],
    quiz=[
        {"q": "What does the deity report at the start of this discourse?",
         "opts": [
             "Seven mendicants reborn in Aviha have been fully freed",
             "A grove haunted by goblins",
             "A riddle about numbers",
             "A request for the Buddha to visit a new monastery"],
         "correct": 0,
         "expl": "A specific report of spiritual progress in a named realm."},
        {"q": "What is Aviha?",
         "opts": [
             "One of the five Pure Abode realms, already met at SN 1.37",
             "A realm reserved exclusively for animals",
             "A hell realm",
             "A city in the human world"],
         "correct": 0,
         "expl": "Reserved for non-returners, the same class of realm as SN 1.37's speakers."},
        {"q": "Which two of the seven named mendicants are traditionally identified with figures known from elsewhere in the canon?",
         "opts": [
             "Upaka and Pukkusāti",
             "Bhaddiya and Bhaddadeva",
             "Bāhudanti and Piṅgiya",
             "None of the seven have any identification elsewhere"],
         "correct": 0,
         "expl": "Upaka from the road to Varanasi, and Pukkusāti from the Dhātuvibhaṅga Sutta (MN 140)."},
        {"q": "What teaching does the deity say all seven understood?",
         "opts": [
             "The Buddha's own teaching on the cessation of name and form",
             "A teaching given by a different, unnamed teacher",
             "No specific teaching is named",
             "A teaching about wealth and prosperity"],
         "correct": 0,
         "expl": "Attributed specifically and directly to the Buddha."},
        {"q": "What does the Buddha's follow-up question shift toward?",
         "opts": [
             "The deity's own understanding, rather than the seven mendicants",
             "An entirely unrelated new topic",
             "A request for the deity to leave immediately",
             "A repeat of the exact same question already answered"],
         "correct": 0,
         "expl": "Surprise at the depth of the deity's own grasp of the teaching."},
        {"q": "Who does the deity reveal themselves to have been in a past life?",
         "opts": [
             "Ghaṭīkāra, a potter and devoted lay follower of the previous Buddha Kassapa",
             "A king",
             "A different, unrelated deity",
             "The deity refuses to reveal any past identity"],
         "correct": 0,
         "expl": "A full personal history, not a vague or general claim."},
        {"q": "What relationship did Ghaṭīkāra have with the Buddha in that past life?",
         "opts": [
             "They were comrades, living in the same village",
             "They were strangers who never met",
             "They were rivals and enemies",
             "The text does not describe any relationship"],
         "correct": 0,
         "expl": "Confirmed directly by the Buddha in his reply."},
        {"q": "What discourse elsewhere in the canon tells this same relationship at greater length?",
         "opts": [
             "The Ghaṭīkārasutta (MN 81)",
             "The Dhammapada",
             "The Visuddhimagga",
             "No other discourse addresses this relationship"],
         "correct": 0,
         "expl": "A much fuller account of Ghaṭīkāra and the bodhisatta's friendship."},
        {"q": "What does the discourse's closing line say about both the Buddha and the deity?",
         "opts": [
             "Both are described as evolved, bearing their final body",
             "Only the Buddha is described this way; the deity is not",
             "Only the deity is described this way; the Buddha is not",
             "Neither is described in any particular way"],
         "correct": 0,
         "expl": "A quiet symmetry closing this reunion across two Buddha-eras."},
        {"q": "What is this discourse's position within the Ādittavagga?",
         "opts": [
             "It is the tenth and last discourse, closing the vagga",
             "It is the vagga's first discourse",
             "It belongs to the previous vagga, the Satullapakāyikavagga",
             "It has no fixed position"],
         "correct": 0,
         "expl": "This discourse's own closing colophon marks the Ādittavagga as finished."},
    ],
    marginalia=[
        ("Seven, freed", [
            "reborn in Aviha,",
            "now fully liberated",
        ]),
        ("Names with their own stories", [
            "Upaka, from the road,",
            "Pukkusāti, from MN 140",
        ]),
        ("A question turned inward", [
            "whose teaching did you",
            "yourself understand?",
        ]),
        ("An old friend, revealed", [
            "Ghaṭīkāra the potter &mdash;",
            "comrades, long ago",
        ]),
    ],
    further=[
        '<a href="%s/sn1.50/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment."
        % SC,
        '<a href="sn-1.49.html">SN 1.49 &middot; Stingy</a> &mdash; the discourse '
        "immediately before this one.",
        '<a href="sn-1.37.html">SN 1.37 &middot; The Congregation</a> &mdash; the '
        "earlier discourse introducing the Pure Abode deities this discourse's seven "
        "mendicants belong to.",
        '<a href="sn-1.41.html">SN 1.41 &middot; On Fire</a> &mdash; this vagga&rsquo;s '
        "opening discourse, ten discourses back.",
    ],
)
