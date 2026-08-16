# -*- coding: utf-8 -*-
"""Catukka Nipāta — The Fours. One discourse per page, from AN 4.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Catukka Nipāta — The Fours"
# The Fours follow the Threes. AN 4.13, 4.55, 4.62 and 4.170 were published
# before this series began working in order; they are listed in the index by
# INDEX_EXTRA and are not generated here. HEAD points at the last page the
# Threes module has reached and moves as that module advances.
HEAD = ("an-3.100.html", "AN 3.100 &middot; A Lump of Salt")
TAIL = ("an-4.55.html", "AN 4.55 &middot; Equality")
INDEX_EXTRA = [
    ("an-4.13", "Padhāna", "Effort"),
    ("an-4.55", "Samajīvina", "Equality"),
    ("an-4.62", "Ānaṇya", "Debtlessness"),
    ("an-4.170", "Yuganaddha", "In Conjunction"),
]

PAGES = []

VAGGA_1 = "<em>Bhaṇḍagāmavagga</em> &mdash; the first chapter of the Fours"
SETTING_1 = ("Bhaṇḍagāma, &lsquo;Wares Village&rsquo;, in the land of the Vajjis; stated at the "
             "head of AN 4.1 and understood to hold across the chapter")
SETTING_CONT = ("None stated; the discourse continues from AN 4.1, whose setting at Wares Village "
                "in the Vajjian country is understood to hold")
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Fours."""
    d = {
        "slug": "an-4.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an4/an4.%d" % num,
        "crumb": "AN 4.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 4.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 4.1 — Anubuddhasutta
# --------------------------------------------------------------------------- #
page(
    1, "Anubuddha", "Understood",
    meta_title="AN 4.1 — Understood | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anubuddhasutta, the "
        "discourse that opens the Fours — noble ethics, immersion, wisdom, and freedom, and the "
        "Buddha's statement that he too wandered for a very long time until he understood them. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "A statement of what was not understood, the list of four, a declaration that it "
                 "is now understood, and two closing verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The four-item set of ethics, immersion, wisdom, and freedom is "
                              "widespread in the Chinese Āgamas, and this material is close to the "
                              "Mahāparinibbāna cycle; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but the first-person "
                       "admission in it repays slow reading"),
    ],
    why=(
        "The Fours open with a list that will run through the whole collection &mdash; noble ethics, "
        "immersion, wisdom, and freedom &mdash; and with a sentence that is easy to read past. "
        "<em>Both you and I have wandered and transmigrated for such a very long time</em> because "
        "these four were not understood. The Buddha places himself inside the failure he is "
        "describing. Whatever else awakening is on this account, it is not a difference of kind "
        "between the teacher and the people he is addressing; it is the same four things, "
        "understood."),
    guide=[
        ("The teaching in one sentence", [
            "Four things &mdash; ethics, immersion, wisdom, freedom &mdash; are what nobody had "
            "understood, and understanding them is the whole difference between wandering on and "
            "being finished."]),
        ("The four, and why they are in this order", [
            "<em>Sīla</em>, <em>samādhi</em>, <em>paññā</em>, <em>vimutti</em>: ethical conduct, "
            "unification of mind, wisdom, and freedom. The first three are the standard threefold "
            "training, and the order is not decorative. Conduct settles the mind, a settled mind can "
            "see, and what it sees releases it.",
            "The fourth item is what makes the list belong to the Fours rather than the Threes. "
            "Freedom is not a fourth practice alongside the other three; it is what the other three "
            "arrive at. The set says that the training has a terminus and names it, which is why the "
            "same four recur throughout the collection whenever the path is summarized at speed.",
            "Note the qualifier attached to the first: <em>noble</em> ethics, <em>ariya sīla</em>. "
            "Not conduct in general, but the conduct of one on the path. The adjective governs all "
            "four items and quietly rules out reading the list as a description of ordinary "
            "virtue."]),
        ("&ldquo;Both you and I&rdquo;", [
            "The discourse says that not understanding these four is why <em>both you and I</em> have "
            "wandered so long. The Pāli puts the teacher and the audience in the same sentence and "
            "the same predicament.",
            "This matters for how the rest of the collection should be heard. A great deal of the "
            "Aṅguttara consists of the Buddha sorting people into kinds &mdash; fools and astute "
            "people, those who go with the stream and those who go against it. That sorting could be "
            "read as a permanent hierarchy. The opening discourse of the Fours forecloses that "
            "reading before it can start: the difference between the teacher and the listener is "
            "something that happened, not something that was always so."]),
        ("What is claimed at the end", [
            "The second half of the key paragraph is a declaration, and it is worth reading as one: "
            "these four <em>have been understood and comprehended</em>; craving for continued "
            "existence <em>has been cut off</em>; the leash to existence <em>is ended</em>; there "
            "will be no more future lives.",
            "Four statements, all in the perfect. The discourse does not argue for this or offer "
            "evidence; it states it, and then a verse repeats it in the third person. Read honestly, "
            "AN 4.1 is a claim on the listener&rsquo;s confidence at the very moment it has invited "
            "them to see themselves as the teacher&rsquo;s equal in the long past. Both moves are "
            "doing work, and they pull in different directions on purpose."]),
        ("The leash", [
            "<em>Bhavanetti</em> &mdash; Sujato&rsquo;s &ldquo;leash to existence&rdquo; &mdash; is "
            "one of the collection&rsquo;s better images. <em>Netti</em> is a guide-rope, the cord by "
            "which an animal is led. What holds a being in the round is not a wall but a tether, and "
            "the animal walks after it.",
            "The image explains why the discourse can pair &ldquo;craving for continued existence has "
            "been cut off&rdquo; with &ldquo;there will be no more future lives&rdquo; as if they "
            "were one thing said twice. On this picture they are. Cut the rope and nothing else has "
            "to be done; the walking simply stops."]),
        ("Where the chapter goes from here", [
            "AN 4.2 takes the same four and states the consequence of lacking them: one has fallen "
            "from this teaching and training. AN 4.3 and 4.4 turn to the untrue person and the "
            "damage they do to themselves. The chapter is arranged so that the definitive list "
            "arrives first and the human material follows.",
            "It is worth reading AN 4.1 and 4.2 together at a single sitting. They share a list, a "
            "verse form, and a single argument split across two discourses: here is what has to be "
            "understood, and here is what it means to be without it."]),
    ],
    terms=[
        ("anubuddha",
         "&ldquo;understood, awakened to&rdquo; &mdash; the participle the discourse is named for. "
         "It is used of the four items, not of a person: what is awakened <em>to</em>."),
        ("ariyaṁ sīlaṁ",
         "&ldquo;noble ethics&rdquo; &mdash; the first of the four, with the adjective that governs "
         "the whole list and marks it as the conduct of one on the path."),
        ("samādhi",
         "&ldquo;immersion, unification of mind&rdquo; &mdash; the second, and the standard middle "
         "term of the threefold training."),
        ("vimutti",
         "&ldquo;freedom, release&rdquo; &mdash; the fourth, and the item that makes this a set of "
         "four. Not a practice alongside the others but what they arrive at."),
        ("bhavanetti",
         "&ldquo;the leash to existence&rdquo; &mdash; <em>netti</em> is a guide-rope. What holds a "
         "being in the round is a tether, and cutting it is the whole of what is needed."),
    ],
    text_intro=(
        "The discourse in full: the setting at Wares Village, the four things not understood, the "
        "declaration that they now are, and the closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Wares Village"),
        ("p", "&sect;1", "an4.1:1.1-1.6"),
        ("h3", "Four things not understood"),
        ("p", "&sect;2", "an4.1:2.1-2.7"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.1:3.1-3.2"),
        ("p", "&sect;4", "an4.1:4.1-5.4"),
    ],
    quiz=[
        {"q": "What four things does AN 4.1 say were not understood?",
         "opts": [
             "The four noble truths",
             "Noble ethics, immersion, wisdom, and freedom",
             "The four bases of psychic power",
             "The four kinds of self-assurance"],
         "correct": 1,
         "expl": "Ethics, immersion, and wisdom &mdash; the threefold training &mdash; with freedom added as the fourth."},
        {"q": "Who is included in the long wandering the discourse describes?",
         "opts": [
             "Only the mendicants being addressed",
             "Both the listeners and the Buddha himself &mdash; &lsquo;both you and I&rsquo;",
             "Only those outside the teaching",
             "Only beings in the lower realms"],
         "correct": 1,
         "expl": "The teacher places himself inside the failure he is describing."},
        {"q": "Why does the guide say that inclusion matters?",
         "opts": [
             "Because it dates the discourse",
             "Because it forecloses reading the collection&rsquo;s sorting of people into kinds as a permanent hierarchy",
             "Because it proves the discourse is late",
             "Because it excuses the listeners"],
         "correct": 1,
         "expl": "The difference between teacher and listener is something that happened, not something that was always so."},
        {"q": "What is the significance of the word &lsquo;noble&rsquo; attached to ethics?",
         "opts": [
             "It refers to the social class of the listener",
             "It marks the conduct as that of one on the path, ruling out reading the list as ordinary virtue",
             "It is a scribal addition",
             "It indicates monastic rather than lay conduct"],
         "correct": 1,
         "expl": "The adjective governs all four items."},
        {"q": "How does freedom relate to the other three items?",
         "opts": [
             "It is a fourth practice to be taken up alongside them",
             "It is what the other three arrive at &mdash; the terminus the list names",
             "It replaces them once attained",
             "It precedes them"],
         "correct": 1,
         "expl": "Which is also why the set belongs to the Fours rather than the Threes."},
        {"q": "What does <em>bhavanetti</em> mean, and why is the image apt?",
         "opts": [
             "&lsquo;Wall of existence&rsquo; &mdash; because rebirth is a prison",
             "&lsquo;Leash to existence&rsquo; &mdash; <em>netti</em> is a guide-rope, and what holds a being in the round is a tether the animal walks after",
             "&lsquo;Root of existence&rsquo; &mdash; because craving grows",
             "&lsquo;Stream of existence&rsquo; &mdash; because beings are carried along"],
         "correct": 1,
         "expl": "Cut the rope and nothing else has to be done; the walking simply stops."},
        {"q": "In what tense are the four closing statements of the key paragraph?",
         "opts": [
             "The future &mdash; they describe what will happen",
             "The perfect &mdash; understood, cut off, ended, no more",
             "The imperative &mdash; they instruct the listener",
             "The conditional"],
         "correct": 1,
         "expl": "The discourse does not argue for this; it states it, and the verse repeats it."},
        {"q": "What tension does the guide identify in the discourse?",
         "opts": [
             "Between the prose and the verse metre",
             "Between inviting the listener to see themselves as the teacher&rsquo;s equal in the long past and asking for confidence in an unargued declaration",
             "Between two versions of the list",
             "Between the setting and the content"],
         "correct": 1,
         "expl": "Both moves are doing work, and they pull in different directions on purpose."},
        {"q": "What does AN 4.2 do with the same four things?",
         "opts": [
             "It replaces them with a different list",
             "It states the consequence of lacking them: one has fallen from this teaching and training",
             "It assigns them to four individuals",
             "It explains them one by one at length"],
         "correct": 1,
         "expl": "A single argument split across two discourses."},
        {"q": "Where is the discourse set?",
         "opts": [
             "Sāvatthī, in Jeta&rsquo;s Grove",
             "Bhaṇḍagāma, &lsquo;Wares Village&rsquo;, in the land of the Vajjis",
             "Rājagaha, on Vulture&rsquo;s Peak",
             "Uruvelā, by the Nerañjarā"],
         "correct": 1,
         "expl": "The setting is stated once and holds across the chapter."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">sīla</span>ethics",
            "<span class=\"pali\">samādhi</span>immersion",
            "<span class=\"pali\">paññā</span>wisdom",
            "<span class=\"pali\">vimutti</span>freedom",
        ]),
        ("The declaration", [
            "understood and comprehended",
            "craving cut off",
            "the leash ended",
            "&mdash; all in the perfect",
        ]),
        ("The image", [
            "<span class=\"pali\">bhavanetti</span>leash",
            "not a wall but a tether",
            "the animal walks after it",
        ]),
        ("Cross-references", [
            "AN 4.2 &middot; next: fallen and secure",
            "AN 3.1 &middot; where the Threes opened",
            "AN 4.5 &middot; four ways of standing in the stream",
        ]),
    ],
    further=[
        '<a href="%s/an4.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.2.html">AN 4.2 &middot; Fallen</a> &mdash; next in this series, and the other '
        "half of this discourse&rsquo;s argument.",
        '<a href="an-3.1.html">AN 3.1 &middot; Perils</a> &mdash; the discourse that opened the '
        "Threes, where this series has come from.",
        '<a href="an-4.13.html">AN 4.13 &middot; Effort</a> &mdash; further into this chapter, on the '
        "four right efforts.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.2 — Papatitasutta
# --------------------------------------------------------------------------- #
page(
    2, "Papatita", "Fallen",
    meta_title="AN 4.2 — Fallen | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Papatitasutta — without "
        "noble ethics, immersion, wisdom, and freedom one has fallen from this teaching and "
        "training; with them, one is secure in it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A negative statement, its positive mirror, and a four-line verse"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four-item set is widespread in the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; very short, and hard only in what "
                       "it implies about who counts as inside"),
    ],
    why=(
        "AN 4.1 said what has to be understood. This discourse says what it means to be without it, "
        "and the phrasing is severe: someone lacking these four <em>has fallen from this teaching "
        "and training</em>. Not is behind in it, not is a beginner in it. Has fallen from it. The "
        "discourse is one of the places where the collection draws a boundary around the tradition "
        "itself, and reading it carefully means noticing exactly where the line is drawn &mdash; "
        "because it is not drawn where most communities would draw it."),
    guide=[
        ("The teaching in one sentence", [
            "What makes someone inside this training is not affiliation but the four things "
            "themselves; without them one has fallen out of it, with them one stands secure in "
            "it."]),
        ("Where the line is drawn", [
            "Notice what the criterion is not. It is not ordination. It is not having taken refuge, "
            "or having been in the community a long time, or holding the right views about the "
            "teacher. It is ethics, immersion, wisdom, and freedom &mdash; the four of AN 4.1.",
            "That is a demanding standard, and taken at face value it puts almost everyone outside. "
            "The fourth item alone is the end of the path. Read strictly, only an arahant is "
            "&lsquo;secure in this teaching and training&rsquo;.",
            "There is a softer reading available, and the discourse does not settle between them. "
            "The four may be named as the axis along which one is inside or outside &mdash; the "
            "thing that measures, not a threshold to be cleared &mdash; so that to have some ethics, "
            "some immersion, some wisdom is to be that far in. On that reading &lsquo;fallen&rsquo; "
            "describes someone with none of it. It is worth being honest that the text supports the "
            "strict reading more naturally and that the softer one is doing interpretive work."]),
        ("&lsquo;Fallen&rsquo; and &lsquo;secure&rsquo;", [
            "<em>Papatita</em> is fallen down, fallen away, dropped out. <em>Apapatita</em> &mdash; "
            "Sujato&rsquo;s &lsquo;secure&rsquo; &mdash; is simply its negation: not fallen. The pair "
            "is spatial and the image is of position rather than progress.",
            "This is a different picture from the one most modern teaching uses. It is not a ladder "
            "where one climbs slowly; it is a place one is in or out of. The Aṅguttara uses both "
            "pictures freely, and neither is the collection&rsquo;s settled view, but the difference "
            "changes what the discourse feels like. There is no partial credit in the vocabulary "
            "here."]),
        ("The verse, and its difficulty", [
            "The closing verse is compressed to the point of obscurity, and honest reading should say "
            "so. <em>They fall, collapsed and fallen; greedy, they return.</em> Then, without "
            "transition: <em>the work is done, the joyful is enjoyed, happiness is found through "
            "happiness.</em>",
            "The two halves plainly correspond to the two halves of the prose &mdash; the fallen and "
            "the secure &mdash; but the verse does not mark the transition, and the second half is "
            "elliptical in the Pāli too. &lsquo;Happiness is found through happiness&rsquo; most "
            "likely means that the pleasant states of the path lead on to further ones, against the "
            "assumption that the way to the end of suffering must be miserable. AN 4.5, four "
            "discourses later, will complicate that considerably.",
            "Where a verse is this compressed, the responsible thing is to read it as a mnemonic "
            "rather than as an argument. It was there to hold the prose in memory, and it does that "
            "job without needing to be independently intelligible."]),
        ("Reading 4.1 and 4.2 as one", [
            "The two discourses share the list, the setting, and the verse form, and neither is "
            "complete alone. AN 4.1 gives the four and declares them understood; AN 4.2 gives the "
            "consequence of lacking them. Together they say: here is the content of the training, "
            "and being in the training just is having it.",
            "The chapter then leaves the list behind for several discourses and turns to conduct "
            "&mdash; how the untrue person breaks themselves, who goes with the stream and who "
            "against it. The definitive material comes first and the human material follows, which "
            "is the ordinary arrangement of a vagga in this collection."]),
    ],
    terms=[
        ("papatita",
         "&ldquo;fallen&rdquo; &mdash; fallen down, fallen away, dropped out. A word of position, not "
         "of progress."),
        ("apapatita",
         "&ldquo;secure&rdquo; &mdash; simply the negation: not fallen. Sujato&rsquo;s rendering "
         "supplies a positive word for what the Pāli states negatively."),
        ("dhammavinaya",
         "&ldquo;teaching and training&rdquo; &mdash; the standard compound for the whole of what the "
         "Buddha set out, and the thing one is here said to be inside or outside of."),
        ("ariyaṁ sīlaṁ",
         "&ldquo;noble ethics&rdquo; &mdash; the first of the four carried over unchanged from "
         "AN 4.1."),
        ("vimutti",
         "&ldquo;freedom&rdquo; &mdash; the fourth item, and the reason the strict reading of this "
         "discourse puts almost everyone outside."),
    ],
    text_intro=(
        "The discourse in full: the fallen, the secure, and the closing verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Fallen from this teaching and training"),
        ("p", "&sect;1", "an4.2:1.1-1.7"),
        ("h3", "Secure in this teaching and training"),
        ("p", "&sect;2", "an4.2:2.1-2.7"),
        ("h3", "The verse"),
        ("p", "&sect;3", "an4.2:3.1-3.4"),
    ],
    quiz=[
        {"q": "What makes someone &lsquo;fallen from this teaching and training&rsquo;?",
         "opts": [
             "Leaving the monastic community",
             "Lacking noble ethics, immersion, wisdom, and freedom",
             "Holding wrong views about the teacher",
             "Breaking a precept"],
         "correct": 1,
         "expl": "The same four things AN 4.1 named."},
        {"q": "What is notable about the criterion the discourse uses?",
         "opts": [
             "It is about affiliation rather than attainment",
             "It is not ordination, refuge, seniority, or right views about the teacher &mdash; it is the four things themselves",
             "It applies only to monastics",
             "It is left deliberately vague"],
         "correct": 1,
         "expl": "The line is not drawn where most communities would draw it."},
        {"q": "What does the strict reading of the discourse imply?",
         "opts": [
             "That everyone who has taken refuge is secure",
             "That since the fourth item is the end of the path, only an arahant is &lsquo;secure in this teaching and training&rsquo;",
             "That the four can be had partially",
             "That the criterion is unknowable"],
         "correct": 1,
         "expl": "A demanding standard, taken at face value."},
        {"q": "What softer reading does the guide offer, and how does it assess it?",
         "opts": [
             "That the four are an axis measuring how far in one is rather than a threshold &mdash; while admitting the text supports the strict reading more naturally",
             "That the discourse is not authentic",
             "That &lsquo;fallen&rsquo; is a scribal error",
             "That the four refer to something else entirely"],
         "correct": 0,
         "expl": "The softer reading is doing interpretive work, and the guide says so."},
        {"q": "What kind of image do <em>papatita</em> and <em>apapatita</em> use?",
         "opts": [
             "A ladder one climbs slowly",
             "Position &mdash; a place one is in or out of, with no partial credit in the vocabulary",
             "A journey with stages",
             "A seed that grows"],
         "correct": 1,
         "expl": "The Aṅguttara uses both pictures freely, but this one is spatial."},
        {"q": "How does Sujato&rsquo;s &lsquo;secure&rsquo; relate to the Pāli?",
         "opts": [
             "It translates a distinct positive term",
             "It supplies a positive word for what the Pāli states negatively: <em>apapatita</em>, not fallen",
             "It is a paraphrase of the verse",
             "It comes from the commentary"],
         "correct": 1,
         "expl": "Simply the negation."},
        {"q": "What does the guide say about the closing verse?",
         "opts": [
             "That it is the clearest part of the discourse",
             "That it is compressed to the point of obscurity and is best read as a mnemonic rather than an argument",
             "That it contradicts the prose",
             "That it is a later addition"],
         "correct": 1,
         "expl": "It was there to hold the prose in memory, and it does that job."},
        {"q": "What does &lsquo;happiness is found through happiness&rsquo; most likely mean?",
         "opts": [
             "That suffering has no cause",
             "That the pleasant states of the path lead on to further ones, against the assumption that the way to the end of suffering must be miserable",
             "That happiness is the goal of the training",
             "That lay life is preferable"],
         "correct": 1,
         "expl": "AN 4.5, four discourses later, will complicate that considerably."},
        {"q": "How do AN 4.1 and AN 4.2 fit together?",
         "opts": [
             "They contradict each other",
             "AN 4.1 gives the four and declares them understood; AN 4.2 gives the consequence of lacking them &mdash; neither is complete alone",
             "AN 4.2 repeats AN 4.1 verbatim",
             "They address different audiences"],
         "correct": 1,
         "expl": "Together: here is the content of the training, and being in the training just is having it."},
        {"q": "What does the chapter turn to after these two discourses?",
         "opts": [
             "A longer exposition of the four",
             "Conduct &mdash; how the untrue person breaks themselves, and who goes with or against the stream",
             "The life of the Buddha",
             "Monastic rules"],
         "correct": 1,
         "expl": "Definitive material first, human material after &mdash; the ordinary arrangement of a vagga."},
    ],
    marginalia=[
        ("The pair", [
            "<span class=\"pali\">papatita</span>fallen",
            "<span class=\"pali\">apapatita</span>not fallen",
            "&mdash; position, not progress",
        ]),
        ("The criterion", [
            "not ordination",
            "not refuge or seniority",
            "the four things themselves",
        ]),
        ("Two readings", [
            "strict: only the arahant is secure",
            "soft: an axis, not a threshold",
            "the text leans strict",
        ]),
        ("Cross-references", [
            "AN 4.1 &middot; where the four are named",
            "AN 4.3 &middot; next: the broken person",
            "AN 4.5 &middot; happiness and the hard road",
        ]),
    ],
    further=[
        '<a href="%s/an4.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; the discourse this one '
        "completes.",
        '<a href="an-4.3.html">AN 4.3 &middot; Broken (1st)</a> &mdash; next in this series, where '
        "the chapter turns to conduct.",
        '<a href="an-4.5.html">AN 4.5 &middot; With the Stream</a> &mdash; on the going that is done '
        "in pain and sadness, against this discourse&rsquo;s closing verse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.3 — Paṭhamakhatasutta
# --------------------------------------------------------------------------- #
page(
    3, "Paṭhamakhata", "Broken (1st)",
    meta_title="AN 4.3 — Broken (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamakhatasutta — four "
        "ways of praising and criticizing without examination that keep a person broken and damaged, "
        "with the verse of the losing hand at dice. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Four faults, their four mirrors, and three verses ending in a very large number"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Material on praising and blaming without examination is well "
                              "represented in the Chinese Āgamas; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain prose with one verse that "
                       "raises a real interpretive problem"),
    ],
    why=(
        "Four faults, and all four are faults of speech about other people: praising who should be "
        "criticized, criticizing who should be praised, inspiring confidence in what is dubious, "
        "failing to inspire it in what is worthy. The word running through them is "
        "<em>examining</em>. The fault is not being wrong; it is speaking without having looked. And "
        "the discourse says such a person <em>keeps themselves broken and damaged</em> &mdash; the "
        "harm named first is to the speaker."),
    guide=[
        ("The teaching in one sentence", [
            "Speaking well or ill of people without having examined them damages the speaker before "
            "it damages anyone else."]),
        ("Four faults that are one fault", [
            "The list is symmetrical: praise the blameworthy, blame the praiseworthy, arouse "
            "confidence in the dubious, withhold it from the inspiring. Two errors about persons, two "
            "about things, and each in both directions.",
            "What unites them is the phrase attached to the first pair: <em>without examining or "
            "scrutinizing</em> (<em>ananuvicca apariyogāhetvā</em>). This is not a discourse against "
            "criticism. The astute person in the second half criticizes too &mdash; they criticize "
            "those deserving of criticism, after examining. The fault is never the verdict. It is "
            "delivering a verdict one has not earned.",
            "That distinction is worth pressing on with students, because it is easy to hear these "
            "lists as counselling silence. They do not. AN 4.3 asks for more speech about merit and "
            "fault, not less &mdash; but only after the work of looking has been done."]),
        ("&ldquo;They keep themselves broken and damaged&rdquo;", [
            "<em>Khataṁ upahataṁ attānaṁ pariharati</em>: they carry around a self that is dug up and "
            "spoiled. <em>Khata</em> is the past participle of digging &mdash; excavated, undermined "
            "&mdash; which is where the title comes from.",
            "The grammar puts the damage in the reflexive. The person who misjudges publicly is "
            "described as maintaining their own injury, and the discourse says this before it "
            "mentions blame from sensible people or the consequences after death. The order is "
            "deliberate: the first cost of speaking without looking is what it does to the speaker&rsquo;s "
            "own condition.",
            "This is the same logic AN 3.2 used in the Threes &mdash; a person is characterized by "
            "their deeds because wisdom shines in its traces. Careless speech about others is itself "
            "a trace, and it is legible."]),
        ("The losing hand at dice", [
            "The second verse is the memorable one. A bad throw at dice is trivial even if you lose "
            "your money, everything you own, and yourself &mdash; because the really terrible hand is "
            "to hate the holy ones.",
            "The image assumes a listener who understands gambling ruin, which in this social world "
            "included staking oneself into slavery. The verse takes the worst outcome its audience "
            "could picture and calls it small. That is the whole rhetorical move, and it works "
            "because the comparison is concrete."]),
        ("The number, and how to read it", [
            "The third verse says a slanderer of noble ones goes to hell for a hundred thousand times "
            "a hundred million, times five hundred and thirty-six times a thousand times ten million "
            "years. Translators differ on how to parse the compound; the figure is astronomical on "
            "any reading.",
            "Two honest observations. First, the specificity is not precision &mdash; a number this "
            "size functions as an intensifier, in the way a modern speaker says a figure they have no "
            "intention of anyone computing. Second, verses of this kind sit awkwardly beside the "
            "sober analytic prose they follow, and this collection contains both registers without "
            "reconciling them.",
            "For teaching, the useful move is to name the tension rather than smooth it over. The "
            "prose gives a criterion anyone can apply tomorrow: examine before you speak. The verse "
            "supplies a threat. They are aimed at different listeners, and a student who notices the "
            "difference is reading well, not badly."]),
        ("The mirror, and the merit", [
            "The second half reverses every term: after examining, the astute person criticizes the "
            "blameworthy and praises the praiseworthy, and so keeps themselves <em>intact and "
            "unscathed</em> and brims with much merit.",
            "Note that accurate speech about other people is here a source of merit, not merely the "
            "avoidance of a fault. The collection generally treats merit as arising from giving, "
            "ethics, and cultivation; this discourse quietly adds sound judgment publicly expressed "
            "to the list."]),
    ],
    terms=[
        ("khata",
         "&ldquo;dug up, undermined, broken&rdquo; &mdash; the past participle of digging, and the "
         "word the discourse takes its name from."),
        ("ananuvicca apariyogāhetvā",
         "&ldquo;without examining or scrutinizing&rdquo; &mdash; the phrase that unites all four "
         "faults. The fault is not the verdict but the missing work behind it."),
        ("asappurisa / sappurisa",
         "&ldquo;untrue person&rdquo; and &ldquo;true person&rdquo; &mdash; the pair the discourse "
         "sorts by, defined here entirely by how they speak of others."),
        ("apuñña / puñña",
         "&ldquo;wickedness&rdquo; and &ldquo;merit&rdquo; &mdash; what each brims with. Accurate "
         "speech about people is treated as merit-making."),
        ("ariyūpavāda",
         "&ldquo;slandering the noble ones&rdquo; &mdash; the fault the third verse attaches its "
         "enormous number to, and traditionally one of the gravest."),
    ],
    text_intro=(
        "The discourse in full: the four faults, their mirrors, and the three closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The untrue person"),
        ("p", "&sect;1", "an4.3:1.1-1.7"),
        ("h3", "The true person"),
        ("p", "&sect;2", "an4.3:2.1-2.7"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.3:3.1-3.4"),
        ("p", "&sect;4", "an4.3:4.1-4.5"),
        ("p", "&sect;5", "an4.3:5.1-5.4"),
    ],
    quiz=[
        {"q": "What do all four faults have in common?",
         "opts": [
             "They are faults of thought",
             "They are faults of speech about others, committed without examining or scrutinizing",
             "They are monastic offenses",
             "They concern possessions"],
         "correct": 1,
         "expl": "The fault is never the verdict; it is delivering a verdict one has not earned."},
        {"q": "Does the discourse counsel against criticizing people?",
         "opts": [
             "Yes &mdash; silence is recommended throughout",
             "No &mdash; the astute person criticizes those deserving of criticism, after examining",
             "Yes, except for teachers",
             "It does not say"],
         "correct": 1,
         "expl": "It asks for more speech about merit and fault, not less &mdash; after the work of looking."},
        {"q": "What does the title word <em>khata</em> literally mean?",
         "opts": [
             "Burnt",
             "Dug up, undermined &mdash; the past participle of digging",
             "Abandoned",
             "Bound"],
         "correct": 1,
         "expl": "They carry around a self that is excavated and spoiled."},
        {"q": "Who is named as harmed first?",
         "opts": [
             "The person wrongly praised",
             "The speaker themselves &mdash; they keep themselves broken and damaged",
             "The community",
             "The person wrongly criticized"],
         "correct": 1,
         "expl": "The reflexive comes before any mention of blame from others or consequences after death."},
        {"q": "Which discourse of the Threes does the guide connect this to?",
         "opts": [
             "AN 3.1, on danger",
             "AN 3.2 &mdash; a person is characterized by their deeds, because wisdom shines in its traces",
             "AN 3.65, the Kālāma discourse",
             "AN 3.100, the lump of salt"],
         "correct": 1,
         "expl": "Careless speech about others is itself a trace, and it is legible."},
        {"q": "What is the point of the dice verse?",
         "opts": [
             "That gambling should be avoided",
             "That the worst outcome the audience could picture &mdash; losing money, property, even oneself &mdash; is small beside hating the holy ones",
             "That luck governs rebirth",
             "That poverty is a punishment"],
         "correct": 1,
         "expl": "The rhetorical move works because the comparison is concrete."},
        {"q": "How does the guide read the enormous number in the third verse?",
         "opts": [
             "As a precise chronological claim",
             "As an intensifier &mdash; specificity of that size is not precision",
             "As a scribal corruption",
             "As a metaphor for a single lifetime"],
         "correct": 1,
         "expl": "Translators differ on parsing the compound; the figure is astronomical on any reading."},
        {"q": "What tension does the guide name, and what does it recommend?",
         "opts": [
             "Between two manuscript traditions &mdash; and recommends choosing one",
             "Between the sober analytic prose and the threatening verse &mdash; and recommends naming the tension rather than smoothing it over",
             "Between the Pāli and the English &mdash; and recommends retranslating",
             "Between monastic and lay application"],
         "correct": 1,
         "expl": "A student who notices the difference is reading well, not badly."},
        {"q": "What does the second half of the discourse add about merit?",
         "opts": [
             "That merit comes only from giving",
             "That accurate speech about other people is a source of merit, not merely the avoidance of a fault",
             "That merit is irrelevant to the path",
             "That merit cannot be measured"],
         "correct": 1,
         "expl": "The discourse quietly adds sound judgment publicly expressed to the usual list."},
        {"q": "What are the four faults, in order?",
         "opts": [
             "Killing, stealing, lying, and intoxication",
             "Praising the blameworthy, criticizing the praiseworthy, arousing faith in the dubious, and failing to arouse it in the inspiring",
             "Greed, hate, delusion, and fear",
             "Doubt, sloth, restlessness, and ill will"],
         "correct": 1,
         "expl": "Two errors about persons, two about things, each in both directions."},
    ],
    marginalia=[
        ("The four faults", [
            "praise the blameworthy",
            "blame the praiseworthy",
            "faith in the dubious",
            "no faith in the inspiring",
        ]),
        ("The missing word", [
            "<span class=\"pali\">ananuvicca</span>unexamined",
            "the astute criticize too",
            "&mdash; after looking",
        ]),
        ("The dice verse", [
            "money, property, yourself",
            "&mdash; and that is the small loss",
            "the terrible hand: hating the holy",
        ]),
        ("Cross-references", [
            "AN 4.4 &middot; next: four people wronged",
            "AN 3.2 &middot; known by their deeds",
            "AN 2.42-51 &middot; assemblies and judgment",
        ]),
    ],
    further=[
        '<a href="%s/an4.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.4.html">AN 4.4 &middot; Broken (2nd)</a> &mdash; next in this series, the same '
        "frame applied to four individuals.",
        '<a href="an-3.2.html">AN 3.2 &middot; Characteristics</a> &mdash; wisdom shines in its '
        "traces, the principle behind this discourse&rsquo;s reflexive harm.",
        '<a href="an-2.42-51.html">AN 2.42&ndash;51 &middot; Assemblies</a> &mdash; the Twos on '
        "communities that judge well and badly.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.4 — Dutiyakhatasutta
# --------------------------------------------------------------------------- #
page(
    4, "Dutiyakhata", "Broken (2nd)",
    meta_title="AN 4.4 — Broken (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyakhatasutta — mother, "
        "father, a Realized One, and a disciple of a Realized One: four individuals toward whom "
        "acting wrongly keeps a person broken and damaged. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Four individuals, the same frame in both directions, and two pairs of verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The pairing of parents with the Buddha and the Saṅgha as supreme "
                              "recipients is common to the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, with a list whose "
                       "composition is the whole point"),
    ],
    why=(
        "The discourse repeats AN 4.3&rsquo;s frame exactly &mdash; broken and damaged, blamed by "
        "sensible people, brimming with wickedness &mdash; but replaces the four faults with four "
        "people: mother, father, a Realized One, and a disciple of a Realized One. The list is the "
        "teaching. Parents stand alongside the Buddha and the Saṅgha, in the same sentence and the "
        "same category, and the discourse offers no explanation for why. That silence is worth "
        "sitting with."),
    guide=[
        ("The teaching in one sentence", [
            "There are four people toward whom conduct counts double, and two of them are your "
            "parents."]),
        ("The composition of the list", [
            "Mother, father, a Realized One (<em>tathāgata</em>), and a disciple of a Realized One. "
            "The last two are the objects of religious reverence in this tradition. The first two are "
            "not religious figures at all.",
            "Placing them in one list makes a strong claim without arguing for it: the debt to those "
            "who gave you your life belongs in the same category as the debt to those who showed you "
            "the way out of it. Neither can be discharged by ordinary reciprocity, which is the "
            "feature the four have in common. You cannot repay being born, and you cannot repay being "
            "taught the path.",
            "The Aṅguttara says this outright elsewhere &mdash; AN 2.32&ndash;41 contains the "
            "well-known passage that even carrying your parents on your shoulders for a hundred years "
            "would not repay them. This discourse assumes that argument rather than making it."]),
        ("What &lsquo;acting wrongly&rsquo; covers", [
            "<em>Micchā paṭipajjamāno</em> is simply &lsquo;practising wrongly toward&rsquo;. The "
            "discourse does not specify the acts, and the vagueness is doing work: it is not a list "
            "of five prohibited things, it is a relation.",
            "The verse narrows it slightly &mdash; <em>because of their unprincipled conduct toward "
            "their parents</em>, <em>adhammacariyā</em> &mdash; and that word points to conduct that "
            "violates what is owed rather than to any particular injury. Neglect qualifies. So does "
            "contempt. The category is wider than harm."]),
        ("Where the harm falls", [
            "As in AN 4.3, the first thing said is reflexive: they keep <em>themselves</em> broken and "
            "damaged. Criticism from the astute comes second, and rebirth in a place of loss third.",
            "The consistent ordering across the pair of discourses is a point worth teaching. The "
            "tradition&rsquo;s account of why not to do these things is not primarily about "
            "punishment, and not primarily about the victim either. It is that the act constitutes a "
            "condition of the person doing it, immediately and by its own nature. Punishment is "
            "mentioned; it arrives third."]),
        ("The elided text", [
            "The Pāli of this discourse abbreviates heavily, and Sujato&rsquo;s translation preserves "
            "the ellipses: <em>Mother &hellip; father &hellip; a Realized One &hellip; and a disciple "
            "of a Realized One.</em> In the manuscript tradition each of the four would be spelled out "
            "with the full frame around it.",
            "It is worth knowing that this is how the collection is transmitted rather than a "
            "translator&rsquo;s shorthand. The Aṅguttara is built for memorization, and an oral "
            "reciter expands what the written text contracts. What looks on the page like a list of "
            "four words was, in performance, four full statements."]),
        ("The positive half", [
            "The mirror is exact: doing right by the same four keeps a person intact and unscathed, "
            "brimming with merit, praised in this life by the astute, and departing to rejoice in "
            "heaven.",
            "Two of the four rewards are worldly &mdash; one&rsquo;s own condition and the regard of "
            "sensible people &mdash; and only one is posthumous. The discourse is not asking anyone to "
            "defer the whole of the payoff, which is characteristic of how the Fours handle the "
            "subject."]),
    ],
    terms=[
        ("tathāgata",
         "&ldquo;Realized One&rdquo; &mdash; the Buddha&rsquo;s usual term for himself, and the third "
         "item on the list."),
        ("micchā paṭipajjati",
         "&ldquo;acts wrongly toward, practises wrongly&rdquo; &mdash; deliberately unspecified. The "
         "discourse names a relation, not a set of prohibited acts."),
        ("adhammacariyā",
         "&ldquo;unprincipled conduct&rdquo; &mdash; the verse&rsquo;s word, pointing at conduct that "
         "violates what is owed rather than at any particular injury."),
        ("khata upahata",
         "&ldquo;broken and damaged&rdquo; &mdash; the reflexive phrase carried over unchanged from "
         "AN 4.3, and the reason the two discourses share a name."),
        ("apāya",
         "&ldquo;place of loss&rdquo; &mdash; the destination named in the verse, and the third of "
         "the consequences rather than the first."),
    ],
    text_intro=(
        "The discourse in full: the four individuals, both directions, and the two pairs of verses. "
        "The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Acting wrongly toward four"),
        ("p", "&sect;1", "an4.4:1.1-1.5"),
        ("h3", "Acting rightly toward four"),
        ("p", "&sect;2", "an4.4:2.1-2.5"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.4:3.1-4.4"),
        ("p", "&sect;4", "an4.4:5.1-6.4"),
    ],
    quiz=[
        {"q": "Who are the four individuals?",
         "opts": [
             "Teacher, preceptor, parents, and ruler",
             "Mother, father, a Realized One, and a disciple of a Realized One",
             "The four assemblies",
             "The stream-enterer, once-returner, non-returner, and arahant"],
         "correct": 1,
         "expl": "Two family members and two religious figures, in one list."},
        {"q": "What claim does the composition of the list make?",
         "opts": [
             "That parents should be worshipped as buddhas",
             "That the debt to those who gave you your life belongs in the same category as the debt to those who showed you the way out of it",
             "That the Saṅgha is a kind of family",
             "That only ordained relatives count"],
         "correct": 1,
         "expl": "The common feature: neither debt can be discharged by ordinary reciprocity."},
        {"q": "Which earlier discourse makes the argument this one assumes?",
         "opts": [
             "AN 2.32&ndash;41, on carrying your parents for a hundred years",
             "AN 1.1&ndash;10, on the mind",
             "AN 3.65, the Kālāma discourse",
             "AN 4.1, on the four things"],
         "correct": 0,
         "expl": "Even that would not repay them &mdash; the argument this discourse takes for granted."},
        {"q": "Why does the discourse not specify what &lsquo;acting wrongly&rsquo; means?",
         "opts": [
             "Because the text is damaged",
             "Because it names a relation rather than a set of prohibited acts &mdash; the category is wider than harm",
             "Because the acts are listed in the Vinaya",
             "Because it applies only to monastics"],
         "correct": 1,
         "expl": "Neglect qualifies; so does contempt."},
        {"q": "In what order are the consequences given?",
         "opts": [
             "Rebirth, then criticism, then self-damage",
             "Self-damage first, criticism from the astute second, rebirth in a place of loss third",
             "All simultaneously",
             "Criticism first, then rebirth"],
         "correct": 1,
         "expl": "Consistent with AN 4.3, and the ordering is the point."},
        {"q": "What does that ordering say about the tradition&rsquo;s account of wrongdoing?",
         "opts": [
             "That punishment is the main deterrent",
             "That the act constitutes a condition of the person doing it, immediately and by its own nature &mdash; punishment arrives third",
             "That the victim&rsquo;s suffering is what matters",
             "That consequences are unknowable"],
         "correct": 1,
         "expl": "Punishment is mentioned, but it is not the primary account."},
        {"q": "What are the ellipses in the text?",
         "opts": [
             "The translator&rsquo;s omissions",
             "The Pāli&rsquo;s own abbreviation, which an oral reciter would expand into four full statements",
             "Damage in the manuscript",
             "Marks of uncertainty"],
         "correct": 1,
         "expl": "The Aṅguttara is built for memorization; the written text contracts what performance expands."},
        {"q": "What does <em>adhammacariyā</em> point at?",
         "opts": [
             "A specific list of injuries",
             "Conduct that violates what is owed, rather than any particular injury",
             "Failure to give alms",
             "Breaking a precept"],
         "correct": 1,
         "expl": "The word narrows the category slightly without turning it into a list."},
        {"q": "How are the rewards in the positive half distributed?",
         "opts": [
             "All are posthumous",
             "Two are worldly &mdash; one&rsquo;s own condition and the regard of sensible people &mdash; and only one is posthumous",
             "All are worldly",
             "They are not specified"],
         "correct": 1,
         "expl": "The discourse is not asking anyone to defer the whole of the payoff."},
        {"q": "What does this discourse share with AN 4.3?",
         "opts": [
             "The four faults",
             "The frame &mdash; broken and damaged, blamed by sensible people, brimming with wickedness &mdash; with a different four in it",
             "The dice verse",
             "The setting only"],
         "correct": 1,
         "expl": "Which is why the two share a name: <em>khata</em>, first and second."},
    ],
    marginalia=[
        ("The four", [
            "mother",
            "father",
            "a Realized One",
            "a disciple of a Realized One",
        ]),
        ("The order of harm", [
            "1 &middot; oneself, broken",
            "2 &middot; blamed by the astute",
            "3 &middot; a place of loss",
        ]),
        ("The ellipses", [
            "the Pāli&rsquo;s own abbreviation",
            "four full statements in performance",
            "&mdash; a collection built to be recited",
        ]),
        ("Cross-references", [
            "AN 4.3 &middot; the same frame, four faults",
            "AN 2.32-41 &middot; what parents cannot be repaid",
            "AN 4.5 &middot; next: four in the stream",
        ]),
    ],
    further=[
        '<a href="%s/an4.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.3.html">AN 4.3 &middot; Broken (1st)</a> &mdash; the discourse whose frame '
        "this one reuses.",
        '<a href="an-2.32-41.html">AN 2.32&ndash;41 &middot; People</a> &mdash; the Twos on the debt '
        "to parents that cannot be repaid.",
        '<a href="an-4.5.html">AN 4.5 &middot; With the Stream</a> &mdash; next in this series.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.5 — Anusotasutta
# --------------------------------------------------------------------------- #
page(
    5, "Anusota", "With the Stream",
    meta_title="AN 4.5 — With the Stream | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anusotasutta — four "
        "individuals: one who goes with the stream, one who goes against it in pain and sadness, "
        "one who is steadfast, and one who has crossed to the far shore. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Four individuals named, then defined one by one, then set out again in four "
                 "stanzas"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The four-person scheme by stream-metaphor appears in the Chinese "
                              "Āgamas and in the Puggalapaññatti; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the second of the four is the "
                       "hardest thing in the chapter"),
    ],
    why=(
        "Four kinds of person, arranged by a single image: the current. One drifts with it, one "
        "swims against it, one has got out and stands, one has crossed. The scheme is elegant and "
        "the second position is startling &mdash; the person going against the stream does so "
        "<em>in pain and sadness, weeping, with tearful faces</em>. The discourse puts that "
        "sentence in the middle of a list of good outcomes and does not soften it. Anyone teaching "
        "the path as reliably pleasant has to account for this line."),
    guide=[
        ("The teaching in one sentence", [
            "Four positions relative to the current: carried, swimming, standing, and across &mdash; "
            "and the swimming is described as painful."]),
        ("The image, and what the stream is", [
            "The current is craving, made explicit in the first stanza: <em>those who go with the "
            "stream are sunk in craving</em>. Going with it costs nothing and requires nothing, which "
            "is what makes it a current rather than a road.",
            "That is the first thing the image gets right. The unawakened life is not described as a "
            "wrong turning taken deliberately but as the direction one moves in when no effort is "
            "applied. The person who indulges in sensual pleasures and does bad deeds is not "
            "portrayed as having chosen the stream. They are simply in it."]),
        ("The one who weeps", [
            "<em>They live the full and pure spiritual life in pain and sadness, weeping, with tearful "
            "faces.</em> Sujato&rsquo;s rendering is faithful; the Pāli "
            "(<em>sahāpi dukkhena sahāpi domanassena assumukho rudamāno</em>) is as stark as it "
            "sounds.",
            "This deserves to be taken at face value before anything is done to soften it. The "
            "discourse is not describing a failed practitioner or a wrong method. This is the second "
            "of four ascending positions &mdash; the person who has stopped indulging and is doing the "
            "work &mdash; and their condition is grief. The going against is genuinely against.",
            "Three things are worth saying about it. First, it is a statement about a phase, not about "
            "the path as a whole: the third and fourth positions are not described this way. Second, "
            "it names a real experience that people in the middle of renunciation report and often "
            "believe they are wrong to feel. And third, the collection does contain the opposite "
            "emphasis &mdash; AN 4.2 has just closed with &lsquo;happiness is found through "
            "happiness&rsquo;, three discourses earlier.",
            "Holding both is the honest position. The Aṅguttara is a compilation and does not "
            "harmonize itself. A teacher who quotes only the pleasant line is misrepresenting the "
            "collection; so is one who quotes only this one."]),
        ("Steadfast, and the fetters", [
            "The third individual is <em>ṭhitatta</em>, &lsquo;steadfast&rsquo; or literally "
            "&lsquo;one whose self is standing&rsquo;. The definition is technical: with the ending of "
            "the five lower fetters they are reborn spontaneously, extinguished there, not liable to "
            "return from that world.",
            "This is the non-returner (<em>anāgāmī</em>), described without the label. Reborn "
            "spontaneously means in the Pure Abodes, without parents; not liable to return means never "
            "again to this level of existence. The image is exact &mdash; the person has come out of "
            "the water and is standing, but is not yet on the far bank."]),
        ("The far shore, and who counts as a brahmin", [
            "The fourth is described in three ways at once: crossed over, gone to the far shore, "
            "standing on solid ground &mdash; and called a <em>brahmin</em>. The definition given is "
            "the arahant&rsquo;s: undefiled freedom of heart and freedom by wisdom, realized in this "
            "very life by one&rsquo;s own insight, with the ending of defilements.",
            "The word choice is deliberate and polemical. In its own social setting <em>brahmin</em> "
            "named a birth. The discourse applies it to an attainment and defines the attainment "
            "precisely, which is the Buddhist redefinition of the term carried out in a single line. "
            "The final stanza reinforces it: the one called &lsquo;gone beyond&rsquo; is the sage who "
            "has comprehended all things high and low."]),
        ("Reading the four as a sequence", [
            "The scheme maps onto the standard stages without naming them: the ordinary person, the "
            "one in training, the non-returner, the arahant. What the stream image adds is a sense of "
            "the effort curve.",
            "Position one is effortless and going the wrong way. Position two is maximal effort "
            "against maximal resistance, and hurts. Position three is standing &mdash; the resistance "
            "has stopped, but the journey has not ended. Position four is arrival. Most descriptions "
            "of the path grade by attainment; this one grades by what it costs, and only this one "
            "makes clear that the cost is not evenly distributed."]),
    ],
    terms=[
        ("anusotagāmī",
         "&ldquo;one who goes with the stream&rdquo; &mdash; carried by the current, indulging in "
         "sensual pleasures and doing bad deeds."),
        ("paṭisotagāmī",
         "&ldquo;one who goes against the stream&rdquo; &mdash; the second individual, and the one "
         "whose condition is described as grief."),
        ("ṭhitatta",
         "&ldquo;steadfast&rdquo;, literally &lsquo;one whose self is standing&rsquo; &mdash; the "
         "non-returner, described here without the label."),
        ("orambhāgiyāni saṁyojanāni",
         "&ldquo;the five lower fetters&rdquo; &mdash; whose ending defines the third individual, and "
         "with it spontaneous rebirth and no return to this world."),
        ("brāhmaṇa tiṇṇo pāraṅgato",
         "&ldquo;a brahmin who has crossed over, gone to the far shore&rdquo; &mdash; the arahant, "
         "with the caste term redefined as an attainment in a single line."),
    ],
    text_intro=(
        "The discourse in full: the four individuals named, defined, and restated in verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four individuals"),
        ("p", "&sect;1", "an4.5:1.1-1.6"),
        ("h3", "Against the stream"),
        ("p", "&sect;2", "an4.5:2.1-2.3"),
        ("h3", "Steadfast, and gone beyond"),
        ("p", "&sect;3", "an4.5:3.1-3.3"),
        ("p", "&sect;4", "an4.5:4.1-4.4"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.5:5.1-5.4"),
        ("p", "&sect;6", "an4.5:6.1-6.4"),
        ("p", "&sect;7", "an4.5:7.1-7.4"),
        ("p", "&sect;8", "an4.5:8.1-8.4"),
    ],
    quiz=[
        {"q": "What are the four individuals?",
         "opts": [
             "The four assemblies",
             "One who goes with the stream, one who goes against it, a steadfast individual, and a brahmin who has crossed over",
             "Mother, father, a Realized One, and a disciple",
             "The learned, the unlearned, the ethical, and the unethical"],
         "correct": 1,
         "expl": "Four positions relative to a single current."},
        {"q": "What is the stream?",
         "opts": [
             "Rebirth",
             "Craving &mdash; made explicit in the first stanza",
             "The teaching",
             "Time"],
         "correct": 1,
         "expl": "&lsquo;Those who go with the stream are sunk in craving.&rsquo;"},
        {"q": "Why does the guide say the image works?",
         "opts": [
             "Because rivers were familiar to the audience",
             "Because going with it costs nothing and requires nothing &mdash; the unawakened life is the direction one moves when no effort is applied",
             "Because water symbolizes purity",
             "Because streams have two banks"],
         "correct": 1,
         "expl": "A current rather than a road; nobody chose it."},
        {"q": "How is the one who goes against the stream described?",
         "opts": [
             "As joyful and light",
             "As living the full and pure spiritual life in pain and sadness, weeping, with tearful faces",
             "As indifferent",
             "As already free"],
         "correct": 1,
         "expl": "The second of four ascending positions, and their condition is grief."},
        {"q": "How does the guide say that line should be handled?",
         "opts": [
             "Softened, since it must be metaphorical",
             "Taken at face value: it describes a phase, names a real experience, and stands alongside the opposite emphasis in AN 4.2 without being harmonized",
             "Treated as a later interpolation",
             "Read as applying only to monastics"],
         "correct": 1,
         "expl": "A teacher who quotes only the pleasant line misrepresents the collection; so does one who quotes only this one."},
        {"q": "Who is the &lsquo;steadfast&rsquo; individual, in standard terms?",
         "opts": [
             "The stream-enterer",
             "The non-returner &mdash; the five lower fetters ended, reborn spontaneously, not liable to return",
             "The once-returner",
             "The arahant"],
         "correct": 1,
         "expl": "Described precisely, but without the label <em>anāgāmī</em>."},
        {"q": "How does the stream image fit the third individual?",
         "opts": [
             "They are still swimming",
             "They have come out of the water and are standing, but are not yet on the far bank",
             "They have drowned",
             "They are back at the start"],
         "correct": 1,
         "expl": "<em>Ṭhitatta</em> &mdash; one whose self is standing."},
        {"q": "What is polemical about calling the fourth individual a brahmin?",
         "opts": [
             "Nothing; it was the ordinary usage",
             "In its own setting the word named a birth, and the discourse applies it to a precisely defined attainment",
             "It insults brahmins",
             "It refers to a particular person"],
         "correct": 1,
         "expl": "The Buddhist redefinition of the term carried out in a single line."},
        {"q": "What defines the fourth individual?",
         "opts": [
             "Long practice",
             "Undefiled freedom of heart and freedom by wisdom, realized in this very life by one&rsquo;s own insight, with the ending of defilements",
             "Rebirth in the Pure Abodes",
             "Renunciation of the household life"],
         "correct": 1,
         "expl": "The arahant&rsquo;s standard definition."},
        {"q": "What does the stream scheme add to the usual account of the stages?",
         "opts": [
             "A sense of the effort curve &mdash; it grades by what the path costs, and shows the cost is not evenly distributed",
             "A chronology",
             "A geography of rebirth",
             "A monastic hierarchy"],
         "correct": 0,
         "expl": "Effortless the wrong way, maximal effort against maximal resistance, standing, arrival."},
    ],
    marginalia=[
        ("Four positions", [
            "with the stream &middot; carried",
            "against it &middot; swimming",
            "steadfast &middot; standing",
            "gone beyond &middot; across",
        ]),
        ("The hard line", [
            "&ldquo;in pain and sadness,",
            "weeping, with tearful faces&rdquo;",
            "&mdash; position two of four",
        ]),
        ("Two emphases", [
            "AN 4.2 &middot; happiness through happiness",
            "AN 4.5 &middot; the tearful face",
            "&mdash; the collection holds both",
        ]),
        ("Cross-references", [
            "AN 4.6 &middot; next: learning and its point",
            "AN 4.2 &middot; the other emphasis",
            "AN 3.65 &middot; judging a teaching for oneself",
        ]),
    ],
    further=[
        '<a href="%s/an4.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.6.html">AN 4.6 &middot; A Little Learning</a> &mdash; next in this series.',
        '<a href="an-4.2.html">AN 4.2 &middot; Fallen</a> &mdash; whose closing verse this discourse '
        "should be read against.",
        '<a href="an-3.65.html">AN 3.65 &middot; With the Kālāmas of Kesamutta</a> &mdash; on '
        "judging for oneself what leads to welfare.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.6 — Appassutasutta
# --------------------------------------------------------------------------- #
page(
    6, "Appassuta", "A Little Learning",
    meta_title="AN 4.6 — A Little Learning | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Appassutasutta — four "
        "individuals sorted by how much they have learned and whether they get the point of it, "
        "with the nine divisions of the teaching and five closing verses. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A two-by-two grid, each cell defined in the same words, and five verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The learning-and-conduct grid is well represented in the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; highly repetitive prose with a "
                       "clear structure and one obscure simile"),
    ],
    why=(
        "A two-by-two grid: much or little learning, crossed with getting or not getting the point "
        "of it. Four cells, and the ranking they imply is the interesting part &mdash; little "
        "learning that lands beats much learning that does not. For a tradition transmitted by "
        "memorization, in which knowing the texts was the qualification, that is a pointed thing to "
        "say. And the verses that follow complicate it again by insisting that learning still "
        "counts."),
    guide=[
        ("The teaching in one sentence", [
            "What matters is not how much of the teaching you have learned but whether you understand "
            "the meaning and practise accordingly &mdash; though the verses will not let you conclude "
            "that learning is unnecessary."]),
        ("The grid", [
            "Little learning, no point. Little learning, point taken. Much learning, no point. Much "
            "learning, point taken. The Pāli phrase behind &lsquo;getting the point&rsquo; is "
            "<em>sutena upapanna</em> &mdash; furnished or endowed by what one has heard.",
            "Each cell is spelled out in identical words, varying only in the two variables. This is "
            "the standard Aṅguttara method and it is designed for oral transmission: the listener "
            "holds one template and swaps two terms. Read on a page it is tedious; recited it is a "
            "single memorable shape.",
            "The definition of &lsquo;getting the point&rsquo; is given three times over and is "
            "consistent: they understand the meaning (<em>attha</em>), understand the teaching "
            "(<em>dhamma</em>), and practise in line with the teaching. Three components, and the "
            "third is behavioral. Comprehension alone does not satisfy the definition."]),
        ("The nine divisions", [
            "The content that is learned much or little is given as a standard list: statements, mixed "
            "prose and verse, discussions, verses, inspired exclamations, legends, stories of past "
            "lives, amazing stories, and elaborations. This is the <em>navaṅga</em>, the ninefold "
            "division of the teaching by literary form.",
            "It is worth knowing that this list, not the later three-basket division, is how the early "
            "texts describe their own contents. It is a classification by genre rather than by "
            "subject or authority, and it includes narrative and verse forms alongside doctrinal "
            "exposition. Whatever the earliest canon looked like, it was not organized as we now find "
            "it."]),
        ("Where the ranking bites", [
            "The prose does not explicitly rank the four, but the arrangement does: the pairs are "
            "given as little-without, little-with, much-without, much-with. The praise attaches to "
            "&lsquo;with&rsquo;, not to &lsquo;much&rsquo;.",
            "That is a real claim in a tradition where recitation was the qualification for teaching "
            "and seniority. The person who has memorized a great deal and does not practise in line "
            "with it is placed below the person who has memorized little and does. This is the same "
            "point that AN 3.2 made about deeds, applied to the one domain where the tradition might "
            "have been expected to exempt itself."]),
        ("The verses pull back", [
            "The four stanzas that follow run the grid again, but they change one variable: instead of "
            "getting the point they use <em>steady in ethics</em>. Learned and unethical, unlearned "
            "and ethical, and so on &mdash; criticized on both counts, praised on one, praised on "
            "both.",
            "And the last stanza is unambiguous about learning: a wise disciple of the Buddha "
            "<em>who is learned and has memorized the teachings</em> is like a pendant of Black Plum "
            "River gold, praised even by the gods. The verses do not undo the prose, but they insist "
            "that learning is a genuine good and not merely a neutral quantity. Read together the two "
            "halves say: learning is worth having, and it is worth nothing by itself.",
            "The simile in that stanza &mdash; <em>jambonada</em>, gold from the Jambu river &mdash; "
            "names a legendary grade of gold, the finest available. The image is of an ornament that "
            "needs no defense; the rhetorical question &lsquo;who is worthy to criticize them?&rsquo; "
            "assumes the answer nobody."]),
        ("Teaching this discourse", [
            "It works well as a self-audit and badly as a judgment of others, because only one of the "
            "two variables is externally visible. How much someone has learned can be checked. Whether "
            "they have got the point &mdash; on the discourse&rsquo;s own three-part definition "
            "&mdash; requires knowing whether they practise accordingly, which takes time and "
            "proximity.",
            "Used on oneself the grid is sharp and easy to apply. Used on others it invites exactly "
            "the unexamined verdict AN 4.3 warned about three discourses earlier."]),
    ],
    terms=[
        ("appassuta / bahussuta",
         "&ldquo;of little learning&rdquo; and &ldquo;of much learning&rdquo; &mdash; the first "
         "variable of the grid. <em>Suta</em> is what has been heard."),
        ("sutena upapanna",
         "&ldquo;got the point of learning&rdquo; &mdash; literally furnished or endowed by what one "
         "has heard. The second variable, and the one the discourse ranks by."),
        ("attha / dhamma",
         "&ldquo;meaning&rdquo; and &ldquo;teaching&rdquo; &mdash; two of the three components of "
         "getting the point; the third is practising in line with it."),
        ("navaṅga",
         "the ninefold division of the teaching by literary form &mdash; statements, mixed prose and "
         "verse, discussions, verses, inspired exclamations, legends, past lives, amazing stories, "
         "elaborations."),
        ("jambonada",
         "gold from the Jambu river &mdash; a legendary finest grade, and the simile for the disciple "
         "who is both learned and ethical."),
    ],
    text_intro=(
        "The discourse in full: the four cells of the grid, each in the same words, and the five "
        "closing verses. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The four, and the first"),
        ("p", "&sect;1", "an4.6:1.1-1.11"),
        ("h3", "Little learning, point taken"),
        ("p", "&sect;2", "an4.6:2.1-2.5"),
        ("h3", "Much learning, point missed"),
        ("p", "&sect;3", "an4.6:3.1-3.5"),
        ("h3", "Much learning, point taken"),
        ("p", "&sect;4", "an4.6:4.1-4.6"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.6:5.1-5.4"),
        ("p", "&sect;6", "an4.6:6.1-6.4"),
        ("p", "&sect;7", "an4.6:7.1-7.4"),
        ("p", "&sect;8", "an4.6:8.1-8.4"),
        ("p", "&sect;9", "an4.6:9.1-9.6"),
    ],
    quiz=[
        {"q": "What two variables make up the grid?",
         "opts": [
             "Ethics and immersion",
             "How much one has learned, and whether one gets the point of learning",
             "Lay and monastic, young and old",
             "Faith and wisdom"],
         "correct": 1,
         "expl": "Four cells from two binary variables."},
        {"q": "What are the three components of &lsquo;getting the point&rsquo;?",
         "opts": [
             "Hearing, remembering, and reciting",
             "Understanding the meaning, understanding the teaching, and practising in line with the teaching",
             "Faith, effort, and mindfulness",
             "Study, reflection, and meditation"],
         "correct": 1,
         "expl": "The third is behavioral; comprehension alone does not satisfy the definition."},
        {"q": "What is the <em>navaṅga</em>?",
         "opts": [
             "The nine stages of concentration",
             "The ninefold division of the teaching by literary form &mdash; statements, mixed prose and verse, discussions, verses, and so on",
             "The nine grades of rebirth",
             "Nine kinds of person"],
         "correct": 1,
         "expl": "A classification by genre, and how the early texts describe their own contents."},
        {"q": "Why does the guide say the <em>navaṅga</em> is worth knowing about?",
         "opts": [
             "Because it lists the books of the canon",
             "Because this, not the later three-basket division, is how the early texts describe their own contents &mdash; a classification by genre",
             "Because it dates the discourse",
             "Because it excludes verse"],
         "correct": 1,
         "expl": "Whatever the earliest canon looked like, it was not organized as we now find it."},
        {"q": "Where does the praise attach in the grid?",
         "opts": [
             "To &lsquo;much&rsquo;",
             "To &lsquo;with&rsquo; &mdash; getting the point &mdash; rather than to quantity of learning",
             "To neither",
             "To both equally"],
         "correct": 1,
         "expl": "Little learning that lands beats much learning that does not."},
        {"q": "Why is that a pointed claim in this tradition?",
         "opts": [
             "Because learning was discouraged",
             "Because recitation was the qualification for teaching and seniority, so the claim applies the test to the one domain the tradition might have exempted",
             "Because the texts were written down",
             "Because few could read"],
         "correct": 1,
         "expl": "The same point AN 3.2 made about deeds, turned on the tradition itself."},
        {"q": "What variable do the verses substitute for &lsquo;getting the point&rsquo;?",
         "opts": [
             "Faith",
             "Being steady in ethics",
             "Age",
             "Attainment"],
         "correct": 1,
         "expl": "Learned and unethical, unlearned and ethical, and so on."},
        {"q": "What do the verses say about learning itself?",
         "opts": [
             "That it is worthless",
             "That it is a genuine good &mdash; the learned and ethical disciple is like a pendant of finest gold, praised even by the gods",
             "That it should be limited",
             "Nothing"],
         "correct": 1,
         "expl": "Read together: learning is worth having, and it is worth nothing by itself."},
        {"q": "What is <em>jambonada</em>?",
         "opts": [
             "A kind of tree",
             "Gold from the Jambu river &mdash; a legendary finest grade",
             "A monastery",
             "A meditation object"],
         "correct": 1,
         "expl": "An ornament that needs no defense: &lsquo;who is worthy to criticize them?&rsquo;"},
        {"q": "Why does the guide say the grid works better as a self-audit than as a judgment of others?",
         "opts": [
             "Because others resent being assessed",
             "Because only one variable is externally visible &mdash; whether someone practises accordingly takes time and proximity to know",
             "Because the discourse forbids assessing others",
             "Because the cells overlap"],
         "correct": 1,
         "expl": "Used on others it invites exactly the unexamined verdict AN 4.3 warned about."},
    ],
    marginalia=[
        ("The grid", [
            "little &middot; no point",
            "little &middot; point taken",
            "much &middot; no point",
            "much &middot; point taken",
        ]),
        ("Getting the point", [
            "understand the meaning",
            "understand the teaching",
            "practise accordingly",
        ]),
        ("The nine forms", [
            "statements, mixed prose &amp; verse",
            "discussions, verses, exclamations",
            "legends, past lives, marvels, elaborations",
        ]),
        ("Cross-references", [
            "AN 4.7 &middot; next: who graces the Saṅgha",
            "AN 4.3 &middot; the unexamined verdict",
            "AN 3.2 &middot; known by their deeds",
        ]),
    ],
    further=[
        '<a href="%s/an4.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.7.html">AN 4.7 &middot; Grace</a> &mdash; next in this series, and the same '
        "qualities set in the four assemblies.",
        '<a href="an-4.3.html">AN 4.3 &middot; Broken (1st)</a> &mdash; on judging without '
        "examining.",
        '<a href="an-1.296-305.html">AN 1.296&ndash;305 &middot; Recollection</a> &mdash; the Ones '
        "on what is worth holding in mind.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.7 — Sobhanasutta
# --------------------------------------------------------------------------- #
page(
    7, "Sobhana", "Grace",
    meta_title="AN 4.7 — Grace | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sobhanasutta — monk, nun, "
        "layman, and laywoman: the four who grace the Saṅgha when they are competent, learned, and "
        "practise in line with the teaching. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "One statement, the four assemblies named, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The fourfold assembly is standard across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; very short, and important for "
                       "what it takes for granted"),
    ],
    why=(
        "Who makes the community look good? The discourse answers: a monk, a nun, a layman, a "
        "laywoman &mdash; the same five qualities required of each, listed once and applied to all "
        "four without variation. Nothing in the discourse is argued, and that is the point. The "
        "equality of the four assemblies in this respect is stated as though it were obvious, and "
        "the list of qualities is identical in every case."),
    guide=[
        ("The teaching in one sentence", [
            "Four kinds of person grace the community, and the qualification is the same for all four "
            "of them."]),
        ("The four assemblies", [
            "<em>Bhikkhu</em>, <em>bhikkhunī</em>, <em>upāsaka</em>, <em>upāsikā</em> &mdash; monk, "
            "nun, layman, laywoman. This is the standard fourfold division of the Buddhist community, "
            "and it appears constantly in the collection.",
            "What the discourse does with it is the notable part. The qualities are stated once, at "
            "the head, and then the four are simply listed. There is no separate standard for lay "
            "people, none for women, and no suggestion that one of the four graces the Saṅgha more "
            "than another. Where the collection elsewhere distinguishes the duties of the four, here "
            "it declines to."]),
        ("The five qualities", [
            "Competent (<em>viyatta</em>), educated (<em>vinīta</em>), self-assured "
            "(<em>visārada</em>), learned (<em>bahussuta</em>), having memorized the teachings "
            "(<em>dhammadhara</em>) &mdash; and practising in line with the teaching.",
            "The list is worth comparing with AN 4.6, which has just been read. There the point was "
            "that learning is worthless without practice; here learning and practice are both "
            "present, and the discourse adds three social qualities the earlier one did not name. "
            "Competence, training, and self-assurance are qualities of how a person carries "
            "themselves in company.",
            "That is consistent with what the discourse is about. It is not describing who benefits "
            "most from the teaching but who <em>graces</em> the community &mdash; who makes it "
            "creditable to those looking at it from outside. Composure in public is relevant to that "
            "in a way it is not to liberation."]),
        ("&lsquo;Grace&rsquo; and what it translates", [
            "<em>Sobhati</em> is to shine, to be beautiful, to look well. The noun form appears in the "
            "closing line: these four <em>are the graces of the Saṅgha</em>, <em>saṅghasobhanā</em>. "
            "Sujato&rsquo;s &lsquo;grace&rsquo; keeps both the verbal and the ornamental sense, which "
            "matters because the Pāli image is decorative &mdash; these people are what the community "
            "is adorned by.",
            "The image recurs in AN 4.6&rsquo;s closing verse, where the learned and ethical disciple "
            "is a pendant of finest gold. Two consecutive discourses reach for ornament as the figure "
            "for a person of quality in a group."]),
        ("What the verses add", [
            "The second verse redistributes the qualities slightly: a monk accomplished in ethics, a "
            "learned nun, a faithful layman, a faithful laywoman. Where the prose gave all five "
            "qualities to all four, the verse gives each a characteristic one.",
            "It would be a mistake to read this as the real ranking beneath the prose&rsquo;s "
            "politeness. Verses in the Aṅguttara are compressed for metre and frequently vary the "
            "prose rather than qualifying it. But it is honest to notice that ethics goes to the monk, "
            "learning to the nun, and faith to both lay figures &mdash; and that the distribution "
            "matches what the wider collection tends to expect of each. The prose is the more "
            "egalitarian statement, and it is the one with authority here."]),
    ],
    terms=[
        ("sobhati / saṅghasobhanā",
         "&ldquo;to shine, to look well&rdquo; and &ldquo;graces of the Saṅgha&rdquo; &mdash; the "
         "image is decorative: these people are what the community is adorned by."),
        ("bhikkhu, bhikkhunī, upāsaka, upāsikā",
         "monk, nun, layman, laywoman &mdash; the fourfold assembly, given here with a single shared "
         "standard."),
        ("viyatta",
         "&ldquo;competent, accomplished&rdquo; &mdash; the first quality, and one of three that "
         "describe how a person carries themselves in company."),
        ("bahussuta",
         "&ldquo;learned, of much learning&rdquo; &mdash; carried straight over from AN 4.6, where "
         "its limits were set out."),
        ("dhammadhara",
         "&ldquo;one who has memorized the teachings&rdquo; &mdash; literally a bearer of the "
         "teaching, the role on which oral transmission depended."),
    ],
    text_intro=(
        "The discourse in full: the statement, the four assemblies, and the two verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four who grace the Saṅgha"),
        ("p", "&sect;1", "an4.7:1.1-1.7"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.7:2.1-2.4"),
        ("p", "&sect;3", "an4.7:3.1-3.6"),
    ],
    quiz=[
        {"q": "Who are the four who grace the Saṅgha?",
         "opts": [
             "The four great disciples",
             "A monk, a nun, a layman, and a laywoman",
             "Teachers, preceptors, students, and donors",
             "The four kinds of noble person"],
         "correct": 1,
         "expl": "The standard fourfold assembly."},
        {"q": "How does the discourse distribute the required qualities?",
         "opts": [
             "Different qualities for monastics and lay people",
             "The same qualities, stated once, applied to all four without variation",
             "Only the first two are required of lay people",
             "It does not specify"],
         "correct": 1,
         "expl": "There is no separate standard for lay people, none for women, and no ranking."},
        {"q": "What does <em>sobhati</em> mean?",
         "opts": [
             "To lead",
             "To shine, to be beautiful, to look well",
             "To protect",
             "To teach"],
         "correct": 1,
         "expl": "The Pāli image is decorative &mdash; these people are what the community is adorned by."},
        {"q": "Which three of the qualities are social rather than doctrinal?",
         "opts": [
             "Learned, memorizing, and practising",
             "Competent, educated, and self-assured &mdash; qualities of how a person carries themselves in company",
             "Faithful, ethical, and generous",
             "None of them"],
         "correct": 1,
         "expl": "Relevant because the subject is who makes the community creditable to outsiders."},
        {"q": "How does this discourse relate to AN 4.6?",
         "opts": [
             "It contradicts it",
             "It carries learning and practice over and adds three social qualities the earlier discourse did not name",
             "It repeats it in verse",
             "It has no connection"],
         "correct": 1,
         "expl": "Different subject: not who benefits most, but who graces the community."},
        {"q": "What image do AN 4.6 and AN 4.7 share?",
         "opts": [
             "A stream",
             "Ornament &mdash; a pendant of finest gold, and the graces of the Saṅgha",
             "Fire",
             "A chariot"],
         "correct": 1,
         "expl": "Two consecutive discourses reach for ornament as the figure for a person of quality."},
        {"q": "What does <em>dhammadhara</em> mean literally?",
         "opts": [
             "One who teaches the Dhamma",
             "A bearer of the teaching &mdash; one who has memorized it",
             "One who protects the Dhamma",
             "One who has realized the Dhamma"],
         "correct": 1,
         "expl": "The role on which oral transmission depended."},
        {"q": "How does the second verse differ from the prose?",
         "opts": [
             "It gives each of the four a characteristic quality &mdash; ethics to the monk, learning to the nun, faith to the lay figures",
             "It names only monastics",
             "It adds a fifth assembly",
             "It reverses the order"],
         "correct": 0,
         "expl": "Where the prose gave all five qualities to all four."},
        {"q": "How does the guide read that difference?",
         "opts": [
             "As the true ranking beneath the prose",
             "As metrical compression that varies the prose &mdash; while noting honestly that the distribution matches wider expectations, and that the prose is the statement with authority",
             "As a translation error",
             "As a later addition"],
         "correct": 1,
         "expl": "The prose is the more egalitarian statement, and it governs here."},
        {"q": "What does the guide say is notable about the discourse&rsquo;s manner?",
         "opts": [
             "That it argues carefully for the equality of the assemblies",
             "That nothing is argued &mdash; the equality is stated as though obvious",
             "That it is addressed to lay people only",
             "That it is unusually long"],
         "correct": 1,
         "expl": "What a text takes for granted is often more telling than what it defends."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">bhikkhu</span>monk",
            "<span class=\"pali\">bhikkhunī</span>nun",
            "<span class=\"pali\">upāsaka</span>layman",
            "<span class=\"pali\">upāsikā</span>laywoman",
        ]),
        ("The qualities", [
            "competent, educated, self-assured",
            "learned, memorizing the teachings",
            "practising in line with it",
        ]),
        ("The image", [
            "<span class=\"pali\">sobhati</span>to shine",
            "the graces of the Saṅgha",
            "&mdash; ornament, not office",
        ]),
        ("Cross-references", [
            "AN 4.6 &middot; learning and its point",
            "AN 4.8 &middot; next: the four assurances",
            "AN 1.248-257 &middot; foremost lay followers",
        ]),
    ],
    further=[
        '<a href="%s/an4.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.8.html">AN 4.8 &middot; Self-assured</a> &mdash; next in this series, the same '
        "word <em>visārada</em> applied to the Buddha.",
        '<a href="an-4.6.html">AN 4.6 &middot; A Little Learning</a> &mdash; where the limits of '
        "learning are set out.",
        '<a href="an-1.248-257.html">AN 1.248&ndash;257 &middot; Foremost Lay Followers</a> &mdash; '
        "the Ones on named laymen and laywomen.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.8 — Vesārajjasutta
# --------------------------------------------------------------------------- #
page(
    8, "Vesārajja", "Self-assured",
    meta_title="AN 4.8 — Self-assured | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vesārajjasutta — the four "
        "kinds of self-assurance of a Realized One, each stated as a challenge nobody can "
        "legitimately make. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Four parallel statements, each a challenge that cannot be made, with two verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The four assurances are a standard set across the Chinese Āgamas and "
                              "later Abhidharma; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; formulaic, but the logical shape "
                       "of the claim rewards attention"),
    ],
    why=(
        "Four things the Buddha says cannot be legitimately said against him, and because they "
        "cannot, he lives secure and fearless. The interesting thing is the form. Each assurance is "
        "stated as the absence of a possible accusation rather than as a positive attainment, which "
        "means the discourse can be read as a list of the four ways a teacher of this kind could "
        "actually be found out."),
    guide=[
        ("The teaching in one sentence", [
            "There are four charges that would destroy the Buddha&rsquo;s claim, none of them can be "
            "made, and that is what his confidence consists of."]),
        ("The four charges", [
            "Stated as accusations, they are: you claim full awakening but do not understand these "
            "things; you claim to have ended the defilements but still have some; the acts you call "
            "obstructions are not really obstructions; your teaching does not lead where you say it "
            "leads for the one who practises it.",
            "Two are about the teacher &mdash; his knowledge and his purification. Two are about the "
            "teaching &mdash; its analysis of what obstructs, and its efficacy. The set is complete in "
            "a way worth noticing: it covers competence, integrity, doctrine, and results. It is hard "
            "to think of a fifth kind of charge that would matter."]),
        ("Assurance as the absence of a charge", [
            "<em>Vesārajja</em> is confidence or fearlessness, from <em>visārada</em> &mdash; the same "
            "word AN 4.7 applied to the four who grace the Saṅgha. Here it is defined negatively: "
            "<em>since I see no such reason, I live secure, fearless, and self-assured.</em>",
            "This is a specific psychological claim rather than a general one. The confidence is not "
            "described as a temperament or a mood but as the state of someone with nothing "
            "outstanding &mdash; no unexamined corner where an accusation could land. That is a "
            "portable idea. Anyone can ask what charges they would be unable to answer, and the "
            "answer maps their own unfreedom quite precisely.",
            "It also explains the phrasing &lsquo;I see no reason&rsquo; rather than &lsquo;no such "
            "reason exists&rsquo;. The claim as stated is about what the speaker has looked for and "
            "not found. Whether that is a modest formulation or a strong one depends on how much you "
            "credit the looking."]),
        ("&lsquo;Legitimately&rsquo;", [
            "The qualifier <em>sahadhammena</em> &mdash; &lsquo;legitimately&rsquo;, in accordance "
            "with principle &mdash; is doing real work. The claim is not that nobody will accuse him. "
            "It is that no accusation of these kinds will be well founded.",
            "That distinction is why the discourse is not falsified by the fact that the Buddha was "
            "in fact accused of things, which the canon records at length. The assurance is about the "
            "ground of a charge, not about whether one is made."]),
        ("The bull&rsquo;s place and the lion&rsquo;s roar", [
            "The frame around the four is imperial: he claims <em>the bull&rsquo;s place</em> "
            "(<em>āsabhaṇṭhāna</em>, the position of the herd leader), <em>roars his lion&rsquo;s "
            "roar</em> in the assemblies, and <em>turns the divine wheel</em> "
            "(<em>brahmacakka</em>).",
            "All three images are about public, uncontested authority, and they are borrowed from the "
            "vocabulary of kingship and of animal dominance. It is worth being frank that this "
            "register sits oddly beside the discourses on examining before you speak and on the "
            "tearful face of the one going against the stream. The Aṅguttara contains both the "
            "analytic and the acclamatory voice, and this discourse is squarely in the second.",
            "The lion&rsquo;s roar in particular becomes a standing formula for a definitive public "
            "declaration, and the phrase is worth knowing because it recurs throughout the canon."]),
        ("How to use it", [
            "As a claim about the Buddha it is not something a reader can check, and the discourse "
            "offers no procedure for checking it. As a structure it is immediately usable: the four "
            "headings &mdash; do I know what I claim to know, am I what I claim to be, is my account "
            "of the obstacles right, does the method work &mdash; are the questions any teacher of "
            "anything should be able to face.",
            "Read that way the discourse is less a statement about one person than a specification of "
            "what would have to be true for a teaching tradition to deserve confidence."]),
    ],
    terms=[
        ("vesārajja",
         "&ldquo;self-assurance, fearlessness&rdquo; &mdash; defined here negatively, as the state of "
         "someone with no unexamined corner where an accusation could land."),
        ("sahadhammena",
         "&ldquo;legitimately, in accordance with principle&rdquo; &mdash; the qualifier that makes "
         "the claim about the ground of a charge rather than about whether one is made."),
        ("āsabhaṇṭhāna",
         "&ldquo;the bull&rsquo;s place&rdquo; &mdash; the position of the herd leader, one of three "
         "images of uncontested authority framing the four."),
        ("sīhanāda",
         "&ldquo;lion&rsquo;s roar&rdquo; &mdash; a standing formula for a definitive public "
         "declaration, recurring throughout the canon."),
        ("antarāyika dhammā",
         "&ldquo;acts that are obstructions&rdquo; &mdash; the subject of the third charge: whether "
         "the teaching&rsquo;s account of what blocks the path is correct."),
    ],
    text_intro=(
        "The discourse in full: the frame, the four assurances, and the closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first assurance"),
        ("p", "&sect;1", "an4.8:1.1-1.4"),
        ("h3", "The second"),
        ("p", "&sect;2", "an4.8:2.1-2.2"),
        ("h3", "The third"),
        ("p", "&sect;3", "an4.8:3.1-3.2"),
        ("h3", "The fourth"),
        ("p", "&sect;4", "an4.8:4.1-4.3"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.8:5.1-5.4"),
        ("p", "&sect;6", "an4.8:6.1-6.4"),
    ],
    quiz=[
        {"q": "How are the four assurances stated?",
         "opts": [
             "As positive attainments",
             "As accusations that cannot be legitimately made",
             "As vows",
             "As questions to the assembly"],
         "correct": 1,
         "expl": "Which lets the discourse be read as the four ways such a teacher could be found out."},
        {"q": "What do the four charges cover?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Competence, integrity, doctrine, and results &mdash; two about the teacher, two about the teaching",
             "Body, speech, mind, and livelihood",
             "Past, present, future, and timeless"],
         "correct": 1,
         "expl": "It is hard to think of a fifth kind of charge that would matter."},
        {"q": "What does <em>sahadhammena</em> add to the claim?",
         "opts": [
             "That the accusation must be public",
             "That the claim is not that nobody will accuse him, but that no accusation of these kinds will be well founded",
             "That only monastics may object",
             "Nothing substantive"],
         "correct": 1,
         "expl": "The assurance is about the ground of a charge, not about whether one is made."},
        {"q": "How is the confidence defined?",
         "opts": [
             "As a temperament",
             "Negatively &mdash; &lsquo;since I see no such reason, I live secure, fearless, and self-assured&rsquo;",
             "As a meditative attainment",
             "As faith in the teaching"],
         "correct": 1,
         "expl": "The state of someone with nothing outstanding."},
        {"q": "Why does the guide call this a portable idea?",
         "opts": [
             "Because it can be recited easily",
             "Because anyone can ask what charges they would be unable to answer, and the answer maps their own unfreedom",
             "Because it applies in every culture",
             "Because it requires no belief"],
         "correct": 1,
         "expl": "Confidence as the absence of an unexamined corner."},
        {"q": "What is significant about &lsquo;I see no reason&rsquo; rather than &lsquo;no such reason exists&rsquo;?",
         "opts": [
             "Nothing; they are equivalent",
             "The claim as stated is about what the speaker has looked for and not found",
             "It shows uncertainty about the teaching",
             "It is a translation artifact"],
         "correct": 1,
         "expl": "Whether that is modest or strong depends on how much you credit the looking."},
        {"q": "What are the three images framing the four assurances?",
         "opts": [
             "A stream, a fire, and a chariot",
             "The bull&rsquo;s place, the lion&rsquo;s roar, and turning the divine wheel",
             "A lamp, a raft, and a bridge",
             "A garden, a city, and a mountain"],
         "correct": 1,
         "expl": "All three are about public, uncontested authority."},
        {"q": "What does the guide say honestly about that register?",
         "opts": [
             "That it is the collection&rsquo;s only voice",
             "That it sits oddly beside the discourses on examining before speaking and on the tearful face &mdash; the Aṅguttara contains both the analytic and the acclamatory voice",
             "That it is inauthentic",
             "That it is a later gloss"],
         "correct": 1,
         "expl": "This discourse is squarely in the second."},
        {"q": "What are <em>antarāyika dhammā</em>?",
         "opts": [
             "Preliminary practices",
             "Acts that are obstructions &mdash; the subject of the third charge, about whether the teaching&rsquo;s account of what blocks the path is correct",
             "The four noble truths",
             "Rules of the Vinaya"],
         "correct": 1,
         "expl": "One of the two charges aimed at the doctrine rather than the person."},
        {"q": "What use does the guide suggest for the four headings?",
         "opts": [
             "As a devotional recitation",
             "As questions any teacher of anything should be able to face: do I know what I claim, am I what I claim, is my account of the obstacles right, does the method work",
             "As a test for ordination",
             "As a meditation subject"],
         "correct": 1,
         "expl": "A specification of what would have to be true for a teaching tradition to deserve confidence."},
    ],
    marginalia=[
        ("The four charges", [
            "you don&rsquo;t understand",
            "you aren&rsquo;t purified",
            "your obstructions aren&rsquo;t",
            "your path doesn&rsquo;t lead there",
        ]),
        ("The qualifier", [
            "<span class=\"pali\">sahadhammena</span>legitimately",
            "not: nobody will accuse",
            "but: no charge will hold",
        ]),
        ("Three images", [
            "the bull&rsquo;s place",
            "the lion&rsquo;s roar",
            "turning the divine wheel",
        ]),
        ("Cross-references", [
            "AN 4.7 &middot; <span class=\"pali\">visārada</span> in the assemblies",
            "AN 4.9 &middot; next: what raises craving",
            "AN 3.65 &middot; checking a teaching oneself",
        ]),
    ],
    further=[
        '<a href="%s/an4.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.9.html">AN 4.9 &middot; The Arising of Craving</a> &mdash; next in this '
        "series.",
        '<a href="an-4.7.html">AN 4.7 &middot; Grace</a> &mdash; where the same word for '
        "self-assurance is applied to the four assemblies.",
        '<a href="an-3.65.html">AN 3.65 &middot; With the Kālāmas of Kesamutta</a> &mdash; the '
        "discourse that asks the listener to check rather than trust.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.9 — Taṇhuppādasutta
# --------------------------------------------------------------------------- #
page(
    9, "Taṇhuppāda", "The Arising of Craving",
    meta_title="AN 4.9 — The Arising of Craving | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Taṇhuppādasutta — robes, "
        "almsfood, lodgings, and rebirth in this or that state: the four things that give rise to "
        "craving in a mendicant. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Four items named in a single breath, then two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The list recurs across the Chinese Āgamas in monastic contexts; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; very short, and sharper than its "
                       "length suggests"),
    ],
    why=(
        "Where does craving arise in someone who has already given up the household life? The "
        "discourse answers with three unglamorous items and one large one: robes, almsfood, "
        "lodgings, and rebirth in this or that state. The first three are the requisites &mdash; "
        "exactly the things a mendicant is permitted. The discourse locates craving not in what has "
        "been renounced but in what remains, which is the more uncomfortable place to look."),
    guide=[
        ("The teaching in one sentence", [
            "For someone who has renounced, craving does not appear in what was given up; it appears "
            "in what is still allowed."]),
        ("Three requisites and one destination", [
            "Robes, almsfood, and lodgings are three of the four monastic requisites (the fourth, "
            "medicine, is not named here). They are the permitted minimum: what a mendicant may own "
            "and must receive.",
            "The fourth item on the list is of a different order &mdash; <em>itibhavābhava</em>, "
            "rebirth in this or that state, meaning existence itself in whatever form. Three small "
            "things and one enormous one, presented without comment on the difference. The effect is "
            "to run a single continuous line from wanting a better robe to wanting to exist at all, "
            "and the discourse leaves the reader to notice that it is one line.",
            "That is the argument, compressed to a list. Craving does not have a scale of its own. "
            "The mechanism that attaches a person to a lodging is the mechanism that attaches them to "
            "being."]),
        ("Why the requisites", [
            "It would be easy to read this as a warning about monastic laxity, and the commentarial "
            "tradition does read it that way in part. But the sharper point is structural. The "
            "requisites are not a concession or a weakness; they are the necessary minimum for the "
            "life. There is no version of the training in which a mendicant does not receive robes, "
            "food, and shelter.",
            "So the discourse is not saying: be careful, you might backslide into luxury. It is "
            "saying: the ground on which craving grows is not removable by renunciation, because it "
            "is the ground you are standing on. Anything you must have is something you can want.",
            "For lay readers the transposition is direct. The equivalent list is not the things one "
            "has given up but the things one legitimately needs &mdash; work, home, health, family. "
            "Those are where craving actually lives, and no amount of simplifying elsewhere touches "
            "them."]),
        ("The partner", [
            "<em>Taṇhā dutiyo puriso</em> &mdash; craving is a person&rsquo;s second, their companion "
            "or partner, as they transmigrate on this long journey. The word <em>dutiya</em> means "
            "simply &lsquo;second&rsquo;, and is the ordinary word for a travelling companion.",
            "The image is unusually gentle for a warning. Craving is not a demon or a fetter here but "
            "the one who walks alongside &mdash; and the trouble with a travelling companion is "
            "precisely that one does not notice them. The verse then names the cost plainly: they go "
            "from this state to another and do not escape transmigration."]),
        ("The instruction", [
            "The second verse gives the whole practical content: knowing this drawback &mdash; that "
            "craving is the cause of suffering &mdash; rid of craving and free of grasping, a "
            "mendicant would wander mindful.",
            "<em>Sato</em>, mindful, is the operative word and it is the only method the discourse "
            "offers. Given that the four items are unavoidable, mindfulness is the only available "
            "response: one cannot stop receiving robes and food, so what changes is the attention "
            "brought to receiving them. The discourse is short because there is nothing else to say."]),
    ],
    terms=[
        ("taṇhuppāda",
         "&ldquo;the arising of craving&rdquo; &mdash; the title, and a technical term for the "
         "occasion on which craving comes up rather than for craving itself."),
        ("cīvara, piṇḍapāta, senāsana",
         "robes, almsfood, and lodgings &mdash; three of the four requisites, and the permitted "
         "minimum of the monastic life."),
        ("itibhavābhava",
         "&ldquo;rebirth in this or that state&rdquo; &mdash; existence in whatever form, and the "
         "fourth item, of an entirely different order from the first three."),
        ("dutiya",
         "&ldquo;second, companion&rdquo; &mdash; the ordinary word for a travelling partner, applied "
         "to craving in the first verse."),
        ("sato",
         "&ldquo;mindful&rdquo; &mdash; the only method the discourse offers, and the only one "
         "available when the occasions of craving cannot be removed."),
    ],
    text_intro=(
        "The discourse in full: the four things, and the two verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four things that give rise to craving"),
        ("p", "&sect;1", "an4.9:1.1-1.7"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.9:2.1-2.4"),
        ("p", "&sect;3", "an4.9:3.1-3.4"),
    ],
    quiz=[
        {"q": "What four things give rise to craving in a mendicant?",
         "opts": [
             "Sights, sounds, smells, and tastes",
             "Robes, almsfood, lodgings, and rebirth in this or that state",
             "Gain, honor, praise, and pleasure",
             "Family, wealth, status, and reputation"],
         "correct": 1,
         "expl": "Three requisites and one destination."},
        {"q": "What is notable about where the discourse locates craving?",
         "opts": [
             "In what has been renounced",
             "In what remains &mdash; exactly the things a mendicant is permitted",
             "In the lay life",
             "In meditation states"],
         "correct": 1,
         "expl": "The more uncomfortable place to look."},
        {"q": "How does the fourth item differ from the first three?",
         "opts": [
             "It is not a requisite but existence itself, in whatever form",
             "It is optional",
             "It applies only to lay people",
             "It is a later addition"],
         "correct": 0,
         "expl": "Three small things and one enormous one, presented without comment on the difference."},
        {"q": "What does that juxtaposition imply?",
         "opts": [
             "That rebirth is trivial",
             "That craving has no scale of its own &mdash; the mechanism that attaches a person to a lodging attaches them to being",
             "That the list is corrupt",
             "That monastics crave less"],
         "correct": 1,
         "expl": "A single continuous line from wanting a better robe to wanting to exist at all."},
        {"q": "Why does the guide reject reading this only as a warning about laxity?",
         "opts": [
             "Because monastics were not lax",
             "Because the requisites are the necessary minimum, not a concession &mdash; the ground on which craving grows is not removable by renunciation",
             "Because the commentary says otherwise",
             "Because the verses contradict it"],
         "correct": 1,
         "expl": "Anything you must have is something you can want."},
        {"q": "What is the lay equivalent the guide proposes?",
         "opts": [
             "Luxuries and entertainments",
             "The things one legitimately needs &mdash; work, home, health, family",
             "Religious observances",
             "Wealth alone"],
         "correct": 1,
         "expl": "No amount of simplifying elsewhere touches them."},
        {"q": "What does <em>dutiya</em> mean in the first verse?",
         "opts": [
             "Enemy",
             "Second, companion &mdash; the ordinary word for a travelling partner",
             "Shadow",
             "Debt"],
         "correct": 1,
         "expl": "The trouble with a travelling companion is that one does not notice them."},
        {"q": "Why does the guide call that image gentle?",
         "opts": [
             "Because craving is said to be harmless",
             "Because craving is not a demon or a fetter here but the one who walks alongside",
             "Because the verse is in a soft metre",
             "Because it addresses lay people"],
         "correct": 1,
         "expl": "The cost is then named plainly: they do not escape transmigration."},
        {"q": "What method does the discourse offer?",
         "opts": [
             "Renouncing the requisites",
             "Mindfulness &mdash; <em>sato</em>, wandering mindful, rid of craving and free of grasping",
             "Meditation on the elements",
             "Confession"],
         "correct": 1,
         "expl": "The only response available when the occasions cannot be removed."},
        {"q": "Why does the guide say the discourse is short?",
         "opts": [
             "Because it is a fragment",
             "Because given that the four items are unavoidable, there is nothing else to say &mdash; what changes is the attention brought to receiving them",
             "Because the audience was familiar with it",
             "Because the verses replace the prose"],
         "correct": 1,
         "expl": "One cannot stop receiving robes and food."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">cīvara</span>robes",
            "<span class=\"pali\">piṇḍapāta</span>almsfood",
            "<span class=\"pali\">senāsana</span>lodgings",
            "<span class=\"pali\">itibhavābhava</span>this or that state",
        ]),
        ("The point", [
            "not what was given up",
            "what is still allowed",
            "&mdash; and cannot be given up",
        ]),
        ("The companion", [
            "<span class=\"pali\">dutiya</span>second, partner",
            "walks alongside",
            "&mdash; and is not noticed",
        ]),
        ("Cross-references", [
            "AN 4.10 &middot; next: the four yokes",
            "AN 4.5 &middot; the stream as craving",
            "AN 2.64-76 &middot; the Twos on happiness",
        ]),
    ],
    further=[
        '<a href="%s/an4.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.10.html">AN 4.10 &middot; Yokes</a> &mdash; next in this series, and the '
        "chapter&rsquo;s full treatment of what binds.",
        '<a href="an-4.5.html">AN 4.5 &middot; With the Stream</a> &mdash; where the current is '
        "named as craving.",
        '<a href="an-2.64-76.html">AN 2.64&ndash;76 &middot; Happiness</a> &mdash; the Twos on the '
        "kinds of happiness and their ranking.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.10 — Yogasutta
# --------------------------------------------------------------------------- #
page(
    10, "Yoga", "Yokes",
    meta_title="AN 4.10 — Yokes | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Yogasutta — the four yokes "
        "of sensual pleasures, future lives, views, and ignorance, and the four unyokings that "
        "answer them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "Four yokes defined one by one, four unyokings in exact mirror, and three verses"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "The four yokes correspond to the standard set of four floods and four "
                              "defilements found throughout the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; long and highly formulaic, with a "
                       "definition worth extracting"),
    ],
    why=(
        "The longest discourse of the chapter, and the one that closes it. Four yokes &mdash; "
        "sensual pleasures, future lives, views, ignorance &mdash; each defined by exactly the same "
        "formula, and then four unyokings defined by its negation. The repetition is the "
        "discourse&rsquo;s method, not its padding: what it establishes by repeating is that "
        "bondage and release have one and the same structure, and that the difference between them "
        "is a single verb."),
    guide=[
        ("The teaching in one sentence", [
            "Four things yoke a being to existence, and in every case the yoke is not-understanding "
            "and the release is understanding."]),
        ("The formula, and the single verb", [
            "For each of the first three yokes the definition is identical. You do not truly "
            "understand that thing&rsquo;s <em>origin, disappearance, gratification, drawback, and "
            "escape</em>; therefore greed, relishing, affection, infatuation, thirst, passion, "
            "attachment, and craving for it linger on inside; that is the yoke.",
            "The unyoking half changes one word. You <em>do</em> truly understand the five headings; "
            "therefore the eight terms for wanting do not linger; that is the unyoking. Everything "
            "else is word for word the same.",
            "This is worth showing students side by side, because it makes an argument that is easy "
            "to state and hard to believe: nothing has to be added to a person to free them, and "
            "nothing has to be removed except a specific ignorance. The eight words for craving are "
            "not attacked directly at any point in the formula. They fail to linger because "
            "understanding has changed."]),
        ("The five headings", [
            "<em>Samudaya</em> origin, <em>atthaṅgama</em> disappearance, <em>assāda</em> "
            "gratification, <em>ādīnava</em> drawback, <em>nissaraṇa</em> escape. This is a standard "
            "analytic frame applied throughout the canon to whatever is under examination.",
            "The presence of <em>assāda</em> in the list is the part that repays attention. The frame "
            "does not ask the practitioner to deny that sensual pleasures are gratifying; it requires "
            "them to understand the gratification as one of five things to be known about it. A "
            "person who cannot say what is genuinely satisfying about what they are letting go has "
            "not completed the analysis, and the discourse counts that as a form of not understanding "
            "&mdash; which is to say, as part of the yoke."]),
        ("The fourth yoke breaks the pattern", [
            "The yoke of ignorance is defined differently from the other three, and the difference is "
            "easy to read past. Its object is not &lsquo;ignorance&rsquo; but <em>the six fields of "
            "contact</em> &mdash; the senses and the mind. And what lingers is not craving but "
            "&lsquo;ignorance and unknowing&rsquo; of them.",
            "So the fourth item is not parallel to the first three; it is underneath them. Not "
            "understanding the six senses is what makes not-understanding possible anywhere else. "
            "That is why the standard ordering of these sets always puts ignorance last and treats it "
            "as the one whose removal ends the others, and it is why the verse says "
            "<em>governed by ignorance</em> rather than merely yoked to it.",
            "The formula&rsquo;s recursive quality is worth naming: the cure for every yoke is "
            "understanding, and the fourth yoke is not understanding the very apparatus by which "
            "anything is understood at all."]),
        ("What a yoke is", [
            "<em>Yoga</em> here is the harness that ties a draught animal to a cart &mdash; the same "
            "root as the English &lsquo;yoke&rsquo;, and the same word that in other Indian traditions "
            "means the discipline of union. The Buddhist usage runs the other way: what is to be "
            "achieved is <em>visaṁyoga</em>, being unharnessed.",
            "The closing phrase of each half turns on this: someone yoked is called <em>one who has "
            "not found sanctuary from the yoke</em> (<em>ayogakkhemī</em>), and someone unyoked has "
            "found it. <em>Yogakkhema</em>, sanctuary from the yoke, is one of the canon&rsquo;s "
            "commonest terms for the goal, and this discourse is where the metaphor behind it is "
            "spelled out in full.",
            "The set of four is also standard under two other names &mdash; the four floods "
            "(<em>ogha</em>) and the four defilements (<em>āsava</em>), with the same members in the "
            "same order. A reader who knows the list under one name will recognize it under the "
            "others."]),
        ("Closing the chapter", [
            "The Bhaṇḍagāma chapter opened with four things not understood &mdash; ethics, immersion, "
            "wisdom, freedom &mdash; and closes with four things not understood in the technical "
            "sense: yokes analyzed under the five headings. The chapter is framed by the same verb, "
            "and the last verse says of the sage that they have <em>slipped their yoke</em>.",
            "Read as a unit, the ten discourses move from the content of the training (4.1&ndash;4.2), "
            "through conduct and the kinds of person (4.3&ndash;4.7), to the mechanism (4.8&ndash;4.10). "
            "It is a well-arranged chapter, and reading it straight through in one sitting takes about "
            "twenty-five minutes."]),
    ],
    terms=[
        ("yoga",
         "&ldquo;yoke&rdquo; &mdash; the harness tying a draught animal to a cart. In this tradition "
         "what is sought is not union but <em>visaṁyoga</em>, being unharnessed."),
        ("yogakkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; one of the canon&rsquo;s commonest terms for "
         "the goal, and spelled out here in full."),
        ("assāda",
         "&ldquo;gratification&rdquo; &mdash; one of the five headings. The frame requires "
         "understanding what is genuinely satisfying, not denying it."),
        ("nissaraṇa",
         "&ldquo;escape&rdquo; &mdash; the fifth heading, and the one the other four are analyzed in "
         "order to reach."),
        ("saḷāyatana",
         "&ldquo;the six fields of contact&rdquo; &mdash; the object of the fourth yoke, which is why "
         "ignorance sits underneath the other three rather than beside them."),
    ],
    text_intro=(
        "The discourse in full: the four yokes, the four unyokings in exact mirror, and the closing "
        "verses. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The yoke of sensual pleasures"),
        ("p", "&sect;1", "an4.10:1.1-1.8"),
        ("h3", "The yoke of future lives"),
        ("p", "&sect;2", "an4.10:2.1-2.5"),
        ("h3", "The yoke of views"),
        ("p", "&sect;3", "an4.10:3.1-3.5"),
        ("h3", "The yoke of ignorance"),
        ("p", "&sect;4", "an4.10:4.1-4.7"),
        ("h3", "Unyoking"),
        ("p", "&sect;5", "an4.10:5.1-5.8"),
        ("p", "&sect;6", "an4.10:6.1-6.5"),
        ("p", "&sect;7", "an4.10:7.1-7.5"),
        ("p", "&sect;8", "an4.10:8.1-8.7"),
        ("h3", "The verses"),
        ("p", "&sect;9", "an4.10:9.1-11.4"),
    ],
    quiz=[
        {"q": "What are the four yokes?",
         "opts": [
             "Greed, hate, delusion, and fear",
             "Sensual pleasures, future lives, views, and ignorance",
             "Body, feeling, mind, and principles",
             "Birth, aging, sickness, and death"],
         "correct": 1,
         "expl": "The same set appears elsewhere as the four floods and the four defilements."},
        {"q": "What is the difference between the yoking and unyoking formulas?",
         "opts": [
             "The unyoking adds a practice",
             "A single verb &mdash; whether you truly understand the five headings; everything else is word for word the same",
             "The unyoking omits the eight terms for craving",
             "The unyoking is in verse"],
         "correct": 1,
         "expl": "Bondage and release have one and the same structure."},
        {"q": "What does that identity of structure argue?",
         "opts": [
             "That release is impossible",
             "That nothing has to be added to free a person, and nothing removed except a specific ignorance &mdash; craving fails to linger because understanding has changed",
             "That craving must be attacked directly",
             "That the two halves are alternative versions"],
         "correct": 1,
         "expl": "The eight words for wanting are never attacked directly in the formula."},
        {"q": "What are the five headings?",
         "opts": [
             "Impermanence, suffering, not-self, emptiness, and peace",
             "Origin, disappearance, gratification, drawback, and escape",
             "Ethics, immersion, wisdom, freedom, and knowledge",
             "Faith, effort, mindfulness, immersion, and wisdom"],
         "correct": 1,
         "expl": "A standard analytic frame applied throughout the canon."},
        {"q": "Why does the guide single out <em>assāda</em>?",
         "opts": [
             "Because it is untranslatable",
             "Because the frame requires understanding what is genuinely satisfying rather than denying it &mdash; and failing to do so counts as part of the yoke",
             "Because it appears only here",
             "Because it replaces <em>ādīnava</em>"],
         "correct": 1,
         "expl": "A person who cannot say what is satisfying about what they are letting go has not completed the analysis."},
        {"q": "How is the fourth yoke defined differently?",
         "opts": [
             "It has no definition",
             "Its object is the six fields of contact, and what lingers is ignorance and unknowing rather than craving",
             "It is defined by a simile",
             "It uses only three of the five headings"],
         "correct": 1,
         "expl": "The difference is easy to read past."},
        {"q": "What does that difference mean?",
         "opts": [
             "That ignorance is the least important yoke",
             "That the fourth is not parallel to the other three but underneath them &mdash; not understanding the six senses is what makes not-understanding possible anywhere else",
             "That it belongs to a different list",
             "That it applies only to monastics"],
         "correct": 1,
         "expl": "Which is why the verse says <em>governed by</em> ignorance rather than merely yoked to it."},
        {"q": "What is the literal image behind <em>yoga</em>?",
         "opts": [
             "A rope binding a prisoner",
             "The harness tying a draught animal to a cart",
             "A net",
             "A chain of debt"],
         "correct": 1,
         "expl": "The Buddhist usage seeks <em>visaṁyoga</em> &mdash; being unharnessed &mdash; rather than union."},
        {"q": "What does <em>yogakkhema</em> mean, and why does it matter?",
         "opts": [
             "&lsquo;Effort in yoga&rsquo; &mdash; a technical practice term",
             "&lsquo;Sanctuary from the yoke&rsquo; &mdash; one of the canon&rsquo;s commonest terms for the goal, whose metaphor this discourse spells out in full",
             "&lsquo;The four yokes&rsquo; &mdash; a summary term",
             "&lsquo;Yoked to peace&rsquo; &mdash; a description of immersion"],
         "correct": 1,
         "expl": "Someone yoked is called one who has not found sanctuary from the yoke."},
        {"q": "How does AN 4.10 frame the chapter with AN 4.1?",
         "opts": [
             "By repeating the same four items",
             "By the same verb &mdash; the chapter opens with four things not understood and closes with four yokes analyzed under the headings of understanding",
             "By returning to the setting at Wares Village",
             "By naming the same individuals"],
         "correct": 1,
         "expl": "And the last verse says of the sage that they have slipped their yoke."},
    ],
    marginalia=[
        ("The four yokes", [
            "sensual pleasures",
            "future lives",
            "views",
            "ignorance",
        ]),
        ("Five headings", [
            "<span class=\"pali\">samudaya</span>origin",
            "<span class=\"pali\">assāda</span>gratification",
            "<span class=\"pali\">ādīnava</span>drawback",
            "<span class=\"pali\">nissaraṇa</span>escape",
        ]),
        ("One list, three names", [
            "<span class=\"pali\">yoga</span>yokes",
            "<span class=\"pali\">ogha</span>floods",
            "<span class=\"pali\">āsava</span>defilements",
        ]),
        ("Cross-references", [
            "AN 4.1 &middot; the chapter&rsquo;s opening four",
            "AN 4.9 &middot; where craving arises",
            "AN 4.13 &middot; further into the Fours",
        ]),
    ],
    further=[
        '<a href="%s/an4.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; the discourse this one closes '
        "the chapter against.",
        '<a href="an-4.9.html">AN 4.9 &middot; The Arising of Craving</a> &mdash; the occasions on '
        "which the first yoke tightens.",
        '<a href="an-4.13.html">AN 4.13 &middot; Effort</a> &mdash; further into the Fours, on the '
        "four right efforts.",
    ],
)


# --------------------------------------------------------------------------- #
# Caravagga — the second chapter of the Fours
# --------------------------------------------------------------------------- #
VAGGA_2 = "<em>Caravagga</em> &mdash; the second chapter of the Fours"
SETTING_2 = ("None stated; the Caravagga gives no location, and each discourse is addressed to the "
             "mendicants directly")


# --------------------------------------------------------------------------- #
# AN 4.11 — Carasutta
# --------------------------------------------------------------------------- #
page(
    11, "Cara", "Walking",
    vagga=VAGGA_2,
    meta_title="AN 4.11 — Walking | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Carasutta — walking, "
        "standing, sitting, lying down, and what a mendicant does with a bad thought in each of "
        "them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "Four postures, the same test in each, run twice in opposite directions, with "
                 "three verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The four-posture frame is common across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple in content, and worth "
                       "reading for what it does with time"),
    ],
    why=(
        "The chapter takes its name from this discourse, and the discourse takes its name from a "
        "posture. Walking, standing, sitting, lying down while awake: the four cover the whole of a "
        "waking day, and the test applied in each is identical. Did a sensual, malicious, or cruel "
        "thought come up, and did you tolerate it? The point of listing the postures is that there "
        "is no posture in which the question does not apply."),
    guide=[
        ("The teaching in one sentence", [
            "There is no position of the body in which the same question is not being asked, and the "
            "answer is either tolerate or do not."]),
        ("Why four postures", [
            "<em>Iriyāpatha</em>, the four postures, is one of the collection&rsquo;s standard ways "
            "of saying &lsquo;always&rsquo;. Walking, standing, sitting, and lying down while awake "
            "exhaust the waking body: there is no fifth thing a person can be doing with their frame.",
            "That is the whole reason the list is here. The discourse is not teaching a technique for "
            "each posture, and nothing in it varies from one to the next. It is closing an exit. A "
            "practitioner who thinks of practice as what happens on the cushion has three postures "
            "left over, and the discourse takes them away.",
            "Note the qualifier on the fourth: lying down <em>while awake</em>. The tradition is "
            "precise about this. Sleep is not covered, and the discourse does not pretend it is."]),
        ("The three bad thoughts", [
            "Sensual (<em>kāma</em>), malicious (<em>byāpāda</em>), and cruel (<em>vihiṁsā</em>) "
            "&mdash; the standard three unskillful kinds of thought, and they map onto greed, hatred, "
            "and a particular sharpening of hatred into the wish to injure.",
            "Cruelty is separated from malice on purpose. Malice wants someone gone or diminished; "
            "cruelty wants to watch them suffer. Keeping them apart lets the list catch a state that "
            "does not feel like anger at all, and which people are correspondingly less likely to "
            "recognize in themselves."]),
        ("&lsquo;Tolerate&rsquo; is the operative word", [
            "<em>Adhivāseti</em> is to put up with, to accommodate, to let stay. The fault is not "
            "having the thought &mdash; the discourse assumes it arises, in both halves &mdash; but "
            "in what happens next.",
            "This is worth stating plainly to students, because the opposite reading causes real "
            "damage. The discourse does not say a good practitioner has no cruel thoughts. It says a "
            "good practitioner does not house them. The two versions of the person in this discourse "
            "differ only after the thought has already arrived.",
            "The four verbs of the response &mdash; give up, get rid of, eliminate, obliterate "
            "(<em>pajahati, vinodeti, byantīkaroti, anabhāvaṁ gameti</em>) &mdash; are a fixed "
            "formula and their force is cumulative rather than sequential. They do not describe four "
            "stages of removal; they say the same thing four times, with increasing finality."]),
        ("What the labels mean", [
            "One who tolerates is called <em>not keen or prudent, always lazy, and lacking energy</em>; "
            "one who does not is <em>keen and prudent, always energetic and resolute</em>. The Pāli "
            "pair is <em>anātāpī anottāpī</em> against <em>ātāpī ottāpī</em>.",
            "<em>Ātāpī</em>, keen, is from the word for heat &mdash; ardent, burning. "
            "<em>Ottāpī</em> is from <em>ottappa</em>, the moral dread that shrinks from doing wrong. "
            "So the pair is warmth and recoil: enough energy to act and enough conscience to want to. "
            "Neither on its own produces the response the discourse asks for."]),
        ("The verses and the domestic life", [
            "The first verse specifies what the bad thought is &lsquo;to do with&rsquo;: "
            "<em>gehanissita</em>, dependent on the household, domestic. The prose said sensual, "
            "malicious, cruel; the verse names the whole family of them by their orientation.",
            "That is a useful gloss for lay readers, who might reasonably ask whether a discourse "
            "aimed at mendicants applies to them. The verse suggests the criterion is not the "
            "subject matter but the direction: thought that returns a person to the concerns they "
            "have set down. Everyone has something they have set down, and the test transfers."]),
    ],
    terms=[
        ("iriyāpatha",
         "&ldquo;posture, deportment&rdquo; &mdash; the four of walking, standing, sitting, and lying "
         "down, which together are the collection&rsquo;s way of saying &lsquo;always&rsquo;."),
        ("adhivāseti",
         "&ldquo;tolerates, puts up with, houses&rdquo; &mdash; the operative verb. The fault is not "
         "the arising of the thought but what is done with it."),
        ("vihiṁsāvitakka",
         "&ldquo;cruel thought&rdquo; &mdash; kept separate from malice because cruelty wants to "
         "watch suffering rather than merely wanting someone gone."),
        ("ātāpī",
         "&ldquo;keen&rdquo; &mdash; from the word for heat: ardent, burning. Paired with "
         "<em>ottāpī</em>, the conscience that recoils from wrongdoing."),
        ("gehanissita",
         "&ldquo;dependent on the household, domestic&rdquo; &mdash; the verse&rsquo;s name for the "
         "whole family of bad thoughts, defined by direction rather than subject."),
    ],
    text_intro=(
        "The discourse in full: the four postures with tolerance, the four without, and the closing "
        "verses. The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Tolerating the thought"),
        ("p", "&sect;1", "an4.11:1.1-1.3"),
        ("p", "&sect;2", "an4.11:2.1-4.3"),
        ("h3", "Not tolerating it"),
        ("p", "&sect;3", "an4.11:5.1-5.3"),
        ("p", "&sect;4", "an4.11:6.1-8.3"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.11:9.1-10.4"),
        ("p", "&sect;6", "an4.11:11.1-11.6"),
    ],
    quiz=[
        {"q": "What are the four postures?",
         "opts": [
             "Standing, kneeling, prostrating, and sitting",
             "Walking, standing, sitting, and lying down while awake",
             "The four jhānas",
             "Working, eating, resting, and meditating"],
         "correct": 1,
         "expl": "Together they exhaust the waking body."},
        {"q": "Why does the discourse list them?",
         "opts": [
             "Because each requires a different technique",
             "To close an exit &mdash; there is no posture in which the question does not apply",
             "Because they occur in that order",
             "To rank them by difficulty"],
         "correct": 1,
         "expl": "Nothing in the discourse varies from one posture to the next."},
        {"q": "What is the significance of &lsquo;while awake&rsquo;?",
         "opts": [
             "It is a scribal addition",
             "The tradition is precise: sleep is not covered, and the discourse does not pretend it is",
             "It means lying down is discouraged",
             "It refers to the meditation on wakefulness"],
         "correct": 1,
         "expl": "A qualifier worth noticing rather than smoothing over."},
        {"q": "What are the three bad thoughts?",
         "opts": [
             "Doubt, restlessness, and sloth",
             "Sensual, malicious, and cruel",
             "Greed, hatred, and delusion",
             "Envy, conceit, and fear"],
         "correct": 1,
         "expl": "The standard three unskillful kinds of thought."},
        {"q": "Why is cruelty separated from malice?",
         "opts": [
             "They are synonyms held apart by metre",
             "Malice wants someone gone; cruelty wants to watch them suffer &mdash; and the separation catches a state that does not feel like anger",
             "Cruelty is worse in every case",
             "Malice applies only to monastics"],
         "correct": 1,
         "expl": "People are correspondingly less likely to recognize it in themselves."},
        {"q": "What is the fault the discourse identifies?",
         "opts": [
             "Having the thought at all",
             "Tolerating it &mdash; housing it once it has arisen",
             "Speaking the thought aloud",
             "Failing to confess it"],
         "correct": 1,
         "expl": "The discourse assumes the thought arises in both halves; the two persons differ only afterward."},
        {"q": "How should the four verbs of the response be read?",
         "opts": [
             "As four sequential stages of removal",
             "As a fixed formula whose force is cumulative &mdash; the same thing said four times, with increasing finality",
             "As four different techniques",
             "As alternatives to choose between"],
         "correct": 1,
         "expl": "Give up, get rid of, eliminate, obliterate."},
        {"q": "What does <em>ātāpī</em> literally suggest?",
         "opts": [
             "Attentive",
             "Heat &mdash; ardent, burning",
             "Patient",
             "Restrained"],
         "correct": 1,
         "expl": "Paired with <em>ottāpī</em>, the conscience that recoils from wrongdoing."},
        {"q": "Why does the guide say neither term works alone?",
         "opts": [
             "Because they are metrically paired",
             "Because the pair is warmth and recoil &mdash; enough energy to act and enough conscience to want to",
             "Because the commentary requires both",
             "Because one is monastic and one lay"],
         "correct": 1,
         "expl": "Neither on its own produces the response the discourse asks for."},
        {"q": "What does <em>gehanissita</em> add for lay readers?",
         "opts": [
             "That the discourse applies only to monastics",
             "That the criterion is direction rather than subject matter &mdash; thought that returns a person to what they have set down",
             "That household life is blameless",
             "That the verses are later"],
         "correct": 1,
         "expl": "Everyone has something they have set down, and the test transfers."},
    ],
    marginalia=[
        ("Four postures", [
            "walking",
            "standing",
            "sitting",
            "lying down &mdash; awake",
        ]),
        ("Three thoughts", [
            "<span class=\"pali\">kāma</span>sensual",
            "<span class=\"pali\">byāpāda</span>malicious",
            "<span class=\"pali\">vihiṁsā</span>cruel",
        ]),
        ("The hinge", [
            "<span class=\"pali\">adhivāseti</span>tolerates",
            "not the arising",
            "but the housing",
        ]),
        ("Cross-references", [
            "AN 4.12 &middot; next: the same postures, the hindrances",
            "AN 4.14 &middot; the effort to give up",
            "AN 4.10 &middot; where craving lingers inside",
        ]),
    ],
    further=[
        '<a href="%s/an4.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.12.html">AN 4.12 &middot; Ethics</a> &mdash; next in this series, the same '
        "four postures with the hindrances in place of the three thoughts.",
        '<a href="an-4.14.html">AN 4.14 &middot; Restraint</a> &mdash; where not tolerating a thought '
        "is named as one of the four efforts.",
        '<a href="an-4.10.html">AN 4.10 &middot; Yokes</a> &mdash; on what lingers on inside, and '
        "why.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.12 — Sīlasutta
# --------------------------------------------------------------------------- #
page(
    12, "Sīla", "Ethics",
    vagga=VAGGA_2,
    next=("an-4.13.html", "AN 4.13 &middot; Effort"),
    meta_title="AN 4.12 — Ethics | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sīlasutta — keep the "
        "precepts and the monastic code, and then what more is there to do? The five hindrances "
        "given up in all four postures. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "An instruction, a question, the answer in four postures, and three verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The ethics-then-what sequence is standard across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; one memorable question and a "
                       "familiar list"),
    ],
    why=(
        "&ldquo;When you&rsquo;ve done this, what more is there to do?&rdquo; The question is asked "
        "immediately after the fullest statement of monastic ethical discipline in the collection "
        "&mdash; precepts, code, conduct, alms, seeing danger in the slightest fault &mdash; and it "
        "is not rhetorical. The answer takes up the rest of the discourse, and it says: the "
        "hindrances, in every posture. Ethics is where the discourse starts and the first place it "
        "declines to stop."),
    guide=[
        ("The teaching in one sentence", [
            "Complete ethical discipline is the beginning of the work rather than the end of it, and "
            "what follows is the five hindrances given up in all four postures."]),
        ("The opening formula", [
            "The first paragraph is one of the canon&rsquo;s standard blocks: live by the precepts and "
            "the monastic code, restrained in the code, conducting yourselves well, resorting for "
            "alms in suitable places, seeing danger in the slightest fault, keeping the rules "
            "undertaken.",
            "Read as a unit it is deliberately comprehensive. It covers what is prohibited "
            "(<em>pātimokkha</em>), how one behaves (<em>ācāragocara</em>), where one goes, and the "
            "attitude brought to the whole (<em>aṇumattesu vajjesu bhayadassāvī</em>, seeing danger "
            "in the slightest fault). Nothing about outward conduct is left unaddressed, which is "
            "what makes the question that follows carry weight."]),
        ("The question", [
            "<em>Kimassa uttari karaṇīyaṁ</em> &mdash; what is to be done beyond this? The force of "
            "the question depends entirely on the completeness of what precedes it. Someone who has "
            "done all of that has, by any ordinary reckoning, finished.",
            "The collection asks this question in several places and the answer is always the same in "
            "shape: ethics is not a lower stage that is passed through and left, but it is also not "
            "sufficient. Here the answer is the hindrances &mdash; that is, the mind. Outward conduct "
            "can be complete while the mind is still occupied, and the discourse simply moves the "
            "subject inward without disparaging what came before."]),
        ("The five hindrances, and the five positives", [
            "The list given is the standard five: desire, ill will, dullness and drowsiness, "
            "restlessness and remorse, doubt. But the discourse pairs their removal with four "
            "positive conditions, and those are the part usually skipped: energy roused up and "
            "unflagging, mindfulness established and lucid, body tranquil and undisturbed, mind "
            "immersed in samādhi.",
            "The pairing matters. The hindrances are named as things given up; the four conditions "
            "are named as things present. A description of practice that only lists what is absent "
            "leaves a reader without a way to tell progress from numbness, and this discourse "
            "supplies the missing half."]),
        ("Back to the postures", [
            "The four postures return unchanged from AN 4.11, and the label at the end of each is "
            "identical: <em>keen and prudent, always energetic and resolute</em>. The two discourses "
            "are built on the same frame with different content dropped into it &mdash; three bad "
            "thoughts there, five hindrances here.",
            "Read side by side they make the chapter&rsquo;s method visible. The Aṅguttara composes "
            "by substitution: one template, many fillings. A reader who has grasped one of these two "
            "discourses has effectively read the other, and the collection expects exactly that "
            "economy of attention from a reciter."]),
        ("The verses", [
            "The verses go somewhere the prose did not. <em>Above, below, all round, as far as the "
            "planet extends; they scrutinize the rise and fall of phenomena such as the "
            "aggregates.</em> That is insight practice, not hindrance-removal, and it is introduced "
            "without transition.",
            "The first verse stays with the postures and adds the small movements &mdash; bending and "
            "extending the limbs &mdash; which is a nod to the mindfulness of the body as taught in "
            "the Satipaṭṭhāna material. The third closes with <em>always determined</em>, "
            "<em>satataṁ pahitatto</em>.",
            "Taken together the three verses sketch a fuller path than the prose asks for: conduct, "
            "then continuous mindfulness, then contemplation of arising and passing. Verses in this "
            "collection often carry material the prose has not earned, and it is more honest to "
            "notice that than to read the extra content back into the prose."]),
    ],
    terms=[
        ("pātimokkha",
         "&ldquo;the monastic code&rdquo; &mdash; the recited list of training rules, and the first "
         "item of the opening formula."),
        ("ācāragocara",
         "&ldquo;conduct and resort&rdquo; &mdash; how one behaves and where one goes for alms; the "
         "part of the formula about a life lived in public."),
        ("aṇumattesu vajjesu bhayadassāvī",
         "&ldquo;seeing danger in the slightest fault&rdquo; &mdash; the attitude the formula asks "
         "for, and the phrase that makes it more than compliance."),
        ("nīvaraṇa",
         "&ldquo;hindrance&rdquo; &mdash; the five given up here: desire, ill will, dullness and "
         "drowsiness, restlessness and remorse, and doubt."),
        ("pahitatta",
         "&ldquo;determined, resolute&rdquo;, literally &lsquo;one whose self is sent forth&rsquo; "
         "&mdash; the closing word of the verses."),
    ],
    text_intro=(
        "The discourse in full: the ethical formula, the question, the four postures, and the three "
        "verses. The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ethics, and the question"),
        ("p", "&sect;1", "an4.12:1.1-1.2"),
        ("h3", "The hindrances in four postures"),
        ("p", "&sect;2", "an4.12:2.1"),
        ("p", "&sect;3", "an4.12:3.1-5.1"),
        ("h3", "The verses"),
        ("p", "&sect;4", "an4.12:6.1-6.4"),
        ("p", "&sect;5", "an4.12:7.1-7.4"),
        ("p", "&sect;6", "an4.12:8.1-8.4"),
    ],
    quiz=[
        {"q": "What question does the discourse ask after the ethical formula?",
         "opts": [
             "Who is qualified to teach?",
             "&lsquo;When you&rsquo;ve done this, what more is there to do?&rsquo;",
             "How long does the training take?",
             "What is the reward?"],
         "correct": 1,
         "expl": "And it is not rhetorical &mdash; the answer takes up the rest of the discourse."},
        {"q": "Why does the question carry weight?",
         "opts": [
             "Because it is asked by a senior monk",
             "Because what precedes it is deliberately comprehensive &mdash; someone who has done all of it has, by ordinary reckoning, finished",
             "Because it is repeated three times",
             "Because it appears in verse"],
         "correct": 1,
         "expl": "Nothing about outward conduct is left unaddressed."},
        {"q": "What does the opening formula cover?",
         "opts": [
             "Only the precepts",
             "What is prohibited, how one behaves, where one goes, and the attitude brought to the whole",
             "Only monastic offenses",
             "Meditation instructions"],
         "correct": 1,
         "expl": "Code, conduct, resort, and seeing danger in the slightest fault."},
        {"q": "What is the answer to the question?",
         "opts": [
             "More rules",
             "The five hindrances, given up in all four postures",
             "Ordination",
             "Teaching others"],
         "correct": 1,
         "expl": "The discourse moves the subject inward without disparaging what came before."},
        {"q": "What are the four positive conditions paired with the hindrances&rsquo; removal?",
         "opts": [
             "Faith, effort, mindfulness, and wisdom",
             "Energy roused and unflagging, mindfulness established and lucid, body tranquil and undisturbed, mind immersed in samādhi",
             "Ethics, immersion, wisdom, and freedom",
             "Loving-kindness, compassion, joy, and equanimity"],
         "correct": 1,
         "expl": "The part usually skipped."},
        {"q": "Why does the guide say that pairing matters?",
         "opts": [
             "Because it doubles the list",
             "Because a description that only lists what is absent leaves no way to tell progress from numbness",
             "Because the positives are easier",
             "Because the hindrances cannot be removed"],
         "correct": 1,
         "expl": "The discourse supplies the missing half."},
        {"q": "How does this discourse relate to AN 4.11?",
         "opts": [
             "It contradicts it",
             "Same frame, different content &mdash; three bad thoughts there, five hindrances here",
             "It is a shortened version",
             "It addresses lay people instead"],
         "correct": 1,
         "expl": "The Aṅguttara composes by substitution: one template, many fillings."},
        {"q": "What do the small movements in the first verse allude to?",
         "opts": [
             "Monastic etiquette",
             "Mindfulness of the body as taught in the Satipaṭṭhāna material &mdash; bending and extending the limbs",
             "The postures of meditation",
             "Manual labor"],
         "correct": 1,
         "expl": "A nod beyond what the prose asked for."},
        {"q": "What do the verses add that the prose does not have?",
         "opts": [
             "A setting",
             "Insight practice &mdash; scrutinizing the rise and fall of phenomena such as the aggregates",
             "A list of rules",
             "The name of a disciple"],
         "correct": 1,
         "expl": "Introduced without transition."},
        {"q": "How does the guide recommend handling that?",
         "opts": [
             "Read the extra content back into the prose",
             "Notice honestly that verses in this collection often carry material the prose has not earned",
             "Treat the verses as spurious",
             "Ignore the prose"],
         "correct": 1,
         "expl": "More honest than harmonizing the two."},
    ],
    marginalia=[
        ("The formula", [
            "precepts and code",
            "conduct and resort",
            "danger in the slightest fault",
        ]),
        ("The question", [
            "&ldquo;what more",
            "is there to do?&rdquo;",
            "&mdash; and it is answered",
        ]),
        ("Present, not just absent", [
            "energy unflagging",
            "mindfulness lucid",
            "body tranquil",
            "mind immersed",
        ]),
        ("Cross-references", [
            "AN 4.11 &middot; the same frame, three thoughts",
            "AN 4.13 &middot; next: the four right efforts",
            "AN 4.1 &middot; ethics as the first of four",
        ]),
    ],
    further=[
        '<a href="%s/an4.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.13.html">AN 4.13 &middot; Effort</a> &mdash; next in this chapter, on the four '
        "right efforts.",
        '<a href="an-4.11.html">AN 4.11 &middot; Walking</a> &mdash; the same four postures with the '
        "three bad thoughts in place of the hindrances.",
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; where ethics is the first of '
        "the four things to be understood.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.14 — Saṁvarasutta
# --------------------------------------------------------------------------- #
page(
    14, "Saṁvara", "Restraint",
    vagga=VAGGA_2,
    prev=("an-4.13.html", "AN 4.13 &middot; Effort"),
    meta_title="AN 4.14 — Restraint | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṁvarasutta — the four "
        "efforts to restrain, to give up, to develop, and to preserve, with the sense faculties, "
        "the awakening factors, and the corpse perceptions. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "Four efforts named, each defined in turn, and a summary verse"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A four-effort scheme with the same members appears in the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; four dense definitions, three of "
                       "them standard and one unexpected"),
    ],
    why=(
        "Four efforts: to restrain, to give up, to develop, and to preserve. The first three are "
        "familiar &mdash; sense restraint, dropping bad thoughts, cultivating the awakening factors. "
        "The fourth is strange. The effort to preserve turns out to mean holding on to a corpse "
        "meditation, and the discourse gives five of them by name. Understanding why that counts as "
        "an <em>effort</em>, and why it is listed alongside the other three, is what this page is "
        "for."),
    guide=[
        ("The teaching in one sentence", [
            "Effort has four jobs: guard the senses, drop what has arisen, build what is missing, and "
            "keep hold of what has been gained."]),
        ("Not the four right efforts", [
            "This set is easy to confuse with the four right efforts (<em>sammappadhāna</em>) of "
            "AN 4.13 and the eightfold path, which are: prevent unarisen bad states, abandon arisen "
            "ones, arouse unarisen good states, maintain arisen ones.",
            "The two sets overlap but are not the same, and the difference is instructive. The right "
            "efforts are organized by a two-by-two grid &mdash; arisen or not, good or bad. This set "
            "is organized by what the practitioner is actually doing: watching a door, dropping a "
            "thought, cultivating a faculty, holding a perception. It is a list of activities rather "
            "than a logical partition, which is why the fourth member does not correspond neatly to "
            "anything in the other list.",
            "Reading them side by side is the fastest way to see how the same material gets organized "
            "twice for different purposes. The Aṅguttara does this constantly and rarely comments on "
            "it."]),
        ("The effort to restrain", [
            "<em>Saṁvarapadhāna</em>, and the definition is the standard sense-restraint formula. On "
            "seeing a sight one does not get caught up in the <em>features and details</em> "
            "(<em>nimitta</em> and <em>anubyañjana</em>) &mdash; the overall impression and the "
            "particulars that follow it.",
            "The reason given is precise: if the faculty were unrestrained, covetousness and "
            "displeasure would become overwhelming. Note the pair. Restraint is not aimed at pleasure "
            "alone but at both directions of reaction, wanting and aversion. It is a guard against "
            "being moved, not against enjoying.",
            "All six senses are named, and the sixth is the mind. Ideas get the same treatment as "
            "sights, which is characteristic: in this analysis thinking is a sense modality, and "
            "there is no inner refuge from which the other five could be watched safely."]),
        ("Giving up and developing", [
            "The effort to give up is AN 4.11 compressed into a paragraph: the three bad thoughts, not "
            "tolerated, and then the same for any arisen unskillful quality. The four verbs recur "
            "unchanged.",
            "The effort to develop is the seven awakening factors &mdash; mindfulness, investigation "
            "of principles, energy, rapture, tranquility, immersion, equanimity &mdash; each with the "
            "standard tail: relying on seclusion, fading away, and cessation, ripening as letting go. "
            "That tail is doing work. It specifies what the factors are being developed toward, and "
            "without it the list could be read as a program of self-improvement."]),
        ("The effort to preserve", [
            "<em>Anurakkhaṇāpadhāna</em>, from <em>rakkhati</em>, to guard. What is guarded is "
            "<em>a fine basis of immersion</em> (<em>bhaddaka samādhinimitta</em>) &mdash; a "
            "meditation subject that has proved fruitful &mdash; and the five given are all "
            "cemetery contemplations: skeleton, worm-infested corpse, livid corpse, split-open "
            "corpse, bloated corpse.",
            "Two things are worth saying. First, on what &lsquo;preserve&rsquo; means: once a "
            "practitioner has found a subject that produces immersion, the effort involved is not in "
            "finding another but in not losing this one. Meditators reliably drift toward novelty, "
            "and the discourse names holding still as a distinct kind of work.",
            "Second, on the corpses. These practices are for a specific purpose &mdash; loosening "
            "attachment to the body and to sensuality &mdash; and the tradition itself records that "
            "they can be badly misapplied. They are not offered here as a beginner&rsquo;s subject "
            "and this page does not recommend taking them up unsupervised. What the discourse "
            "establishes is the structural point: whatever your fruitful subject is, keeping it is "
            "one of the four efforts."]),
        ("The Kinsman of the Sun", [
            "The closing verse attributes the four to <em>ādiccabandhu</em>, the Kinsman of the Sun "
            "&mdash; a title for the Buddha referring to the Ādicca or solar clan from which the "
            "Sakyans traced descent.",
            "It is a small thing, but epithets of this kind are how verse sections date and place "
            "themselves. The prose calls him nothing at all; the verse reaches for a clan name. The "
            "two registers of this collection are visible even in a four-line summary."]),
    ],
    terms=[
        ("padhāna",
         "&ldquo;effort, exertion&rdquo; &mdash; the general term. This set of four is organized by "
         "activity, unlike the <em>sammappadhāna</em> of AN 4.13, which is a logical grid."),
        ("nimitta / anubyañjana",
         "&ldquo;features and details&rdquo; &mdash; the overall impression and the particulars that "
         "follow it; what sense restraint declines to be caught up in."),
        ("abhijjhā domanassa",
         "&ldquo;covetousness and displeasure&rdquo; &mdash; the pair that would become overwhelming. "
         "Restraint guards both directions, wanting and aversion."),
        ("bojjhaṅga",
         "&ldquo;awakening factor&rdquo; &mdash; the seven developed under the third effort, each "
         "relying on seclusion, fading away, and cessation, and ripening as letting go."),
        ("samādhinimitta",
         "&ldquo;basis of immersion&rdquo; &mdash; the meditation subject that is guarded under the "
         "fourth effort. Holding still is named as a kind of work."),
    ],
    text_intro=(
        "The discourse in full: the four efforts named and defined, and the closing verse. "
        "The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The effort to restrain"),
        ("p", "&sect;1", "an4.14:1.1-1.13"),
        ("h3", "The effort to give up"),
        ("p", "&sect;2", "an4.14:2.1-2.6"),
        ("h3", "The effort to develop"),
        ("p", "&sect;3", "an4.14:3.1-3.9"),
        ("h3", "The effort to preserve"),
        ("p", "&sect;4", "an4.14:4.1-4.4"),
        ("h3", "The verse"),
        ("p", "&sect;5", "an4.14:5.1-5.6"),
    ],
    quiz=[
        {"q": "What are the four efforts of this discourse?",
         "opts": [
             "To prevent, to abandon, to arouse, and to maintain",
             "To restrain, to give up, to develop, and to preserve",
             "Bodily, verbal, mental, and livelihood",
             "Faith, energy, mindfulness, and wisdom"],
         "correct": 1,
         "expl": "A list of activities rather than a logical partition."},
        {"q": "How does this set differ from the four right efforts?",
         "opts": [
             "It is identical",
             "The right efforts are a two-by-two grid of arisen or not, good or bad; this set is organized by what the practitioner is actually doing",
             "This set is monastic only",
             "This set omits meditation"],
         "correct": 1,
         "expl": "Which is why the fourth member has no neat counterpart in the other list."},
        {"q": "What does sense restraint decline to get caught up in?",
         "opts": [
             "Pleasant objects only",
             "The features and details &mdash; the overall impression and the particulars that follow it",
             "Conversation",
             "Memories"],
         "correct": 1,
         "expl": "<em>Nimitta</em> and <em>anubyañjana</em>."},
        {"q": "What would become overwhelming if a faculty were unrestrained?",
         "opts": [
             "Craving alone",
             "Covetousness and displeasure &mdash; both directions of reaction",
             "Doubt",
             "Sleepiness"],
         "correct": 1,
         "expl": "A guard against being moved, not against enjoying."},
        {"q": "What is the sixth faculty treated in the same way as the eye?",
         "opts": [
             "Intuition",
             "The mind &mdash; ideas get the same treatment as sights",
             "Speech",
             "Memory"],
         "correct": 1,
         "expl": "In this analysis thinking is a sense modality; there is no inner refuge."},
        {"q": "What is developed under the third effort?",
         "opts": [
             "The four jhānas",
             "The seven awakening factors, each relying on seclusion, fading away, and cessation, and ripening as letting go",
             "The five faculties",
             "The four immeasurables"],
         "correct": 1,
         "expl": "The tail specifies what the factors are being developed toward."},
        {"q": "Why does the guide say that tail matters?",
         "opts": [
             "It supplies the metre",
             "Without it the list could be read as a program of self-improvement",
             "It names the teacher",
             "It dates the passage"],
         "correct": 1,
         "expl": "Seclusion, fading away, cessation, letting go."},
        {"q": "What does the effort to preserve mean?",
         "opts": [
             "Preserving the monastic rules",
             "Guarding a meditation subject that has proved fruitful &mdash; not losing what already works",
             "Memorizing the discourses",
             "Protecting the community"],
         "correct": 1,
         "expl": "Meditators reliably drift toward novelty; holding still is named as distinct work."},
        {"q": "What five subjects are given for the fourth effort?",
         "opts": [
             "The four elements and space",
             "Cemetery contemplations: skeleton, worm-infested corpse, livid corpse, split-open corpse, bloated corpse",
             "The five aggregates",
             "Breath, body, feelings, mind, and principles"],
         "correct": 1,
         "expl": "The guide notes these are not a beginner&rsquo;s subject and does not recommend taking them up unsupervised."},
        {"q": "Who is the &lsquo;Kinsman of the Sun&rsquo;?",
         "opts": [
             "A deity",
             "The Buddha &mdash; a title referring to the solar clan from which the Sakyans traced descent",
             "A senior disciple",
             "The narrator of the verse"],
         "correct": 1,
         "expl": "The prose calls him nothing at all; the verse reaches for a clan name."},
    ],
    marginalia=[
        ("Four efforts", [
            "<span class=\"pali\">saṁvara</span>restrain",
            "<span class=\"pali\">pahāna</span>give up",
            "<span class=\"pali\">bhāvanā</span>develop",
            "<span class=\"pali\">anurakkhaṇā</span>preserve",
        ]),
        ("Sense restraint", [
            "not the object",
            "the features and details",
            "&mdash; and both reactions",
        ]),
        ("Two sets, one subject", [
            "AN 4.13 &middot; a logical grid",
            "AN 4.14 &middot; a list of activities",
            "&mdash; organized twice",
        ]),
        ("Cross-references", [
            "AN 4.13 &middot; the four right efforts",
            "AN 4.11 &middot; not tolerating a thought",
            "AN 4.15 &middot; next: four regarded as foremost",
        ]),
    ],
    further=[
        '<a href="%s/an4.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.13.html">AN 4.13 &middot; Effort</a> &mdash; the four right efforts, with '
        "which this set should be compared.",
        '<a href="an-4.11.html">AN 4.11 &middot; Walking</a> &mdash; the effort to give up, set out '
        "at length.",
        '<a href="an-4.15.html">AN 4.15 &middot; Regarded as Foremost</a> &mdash; next in this '
        "series.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.15 — Paññattisutta
# --------------------------------------------------------------------------- #
page(
    15, "Paññatti", "Regarded as Foremost",
    vagga=VAGGA_2,
    meta_title="AN 4.15 — Regarded as Foremost | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paññattisutta — Rāhu, "
        "Mandhātā, Māra, and the Buddha: four holders of a superlative, and what each superlative "
        "is for. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "Four superlatives, each with a named holder, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Comparable lists of cosmological superlatives appear in the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and dependent on knowing "
                       "who three of the four are"),
    ],
    why=(
        "Four record-holders: the largest body, the greatest appetite for pleasure, the widest "
        "sovereignty, and the best. The first three are named individuals from Indian cosmology "
        "&mdash; Rāhu, Mandhātā, Māra &mdash; and each of the first three superlatives is something "
        "the tradition regards as worthless. The list is built so that the fourth term does not "
        "belong to the same scale as the other three, and noticing that is the whole reading."),
    guide=[
        ("The teaching in one sentence", [
            "Three beings hold the records for size, pleasure, and power, and the fourth item on the "
            "list is not another record."]),
        ("Who the three are", [
            "<em>Rāhu</em>, lord of the titans (<em>asura</em>), is the eclipse figure of Indian "
            "cosmology &mdash; the being who swallows the sun and moon. He holds the record for size "
            "of body, which in this literature is enormous and precisely quantified elsewhere.",
            "<em>Mandhātā</em> is a legendary wheel-turning monarch whose story is told at length in "
            "the Jātaka literature. He obtained everything a being can obtain, ruled the four "
            "continents, ascended to the heaven of the Thirty-Three, shared the throne with Sakka "
            "&mdash; and wanted more, which is what destroyed him. He holds the record for "
            "enjoyment.",
            "<em>Māra the Wicked</em> holds the record for sovereignty (<em>issariya</em>). In the "
            "canon he is the personification of death and of the pull of sensuality, and the ruler of "
            "the highest sensual heaven. His power is real in this cosmology, not decorative."]),
        ("Three worthless superlatives", [
            "The selection is deliberate and slightly mocking. Size of body is of no spiritual "
            "consequence whatever. The greatest enjoyer of pleasures is a cautionary tale whose "
            "appetite outran the largest supply the universe could offer. The greatest sovereign is "
            "the adversary.",
            "So the first three items are not lesser goods arranged below a greater one. They are "
            "three superlatives held by beings the tradition regards, respectively, as irrelevant, "
            "ruined, and hostile. The list does not say the Buddha is more of what they have more of. "
            "It changes the subject at the fourth item."]),
        ("The fourth is described differently", [
            "Notice the phrasing. The first three each get a short label: foremost in size, foremost "
            "pleasure seeker, foremost in sovereignty. The fourth gets a long formula &mdash; in this "
            "world with its gods, Māras, and divinities, this population with its ascetics and "
            "brahmins, gods and humans, a Realized One, the perfected one, the fully awakened Buddha "
            "is said to be the best.",
            "The scope clause is doing the work. The other three superlatives are held within a "
            "category: among bodies, among enjoyers, among rulers. The fourth is stated against the "
            "whole of existence with no category named, and the word is simply <em>aggo</em>, best.",
            "This is an acclamatory discourse and it should be read as one. It offers no argument and "
            "asks for none. Its interest for a careful reader is entirely in the construction: what "
            "it puts on the list, and what it declines to make the fourth item comparable to."]),
        ("<em>Paññatti</em>, and what the title means", [
            "The title word means designation, description, what is made known or laid down. The "
            "discourse is about what these four are <em>declared</em> to be foremost in &mdash; a "
            "matter of reputation and title rather than of measurement.",
            "That is a small but real qualification. The discourse does not say Rāhu is the largest "
            "being; it says he is the one designated as such. Read strictly, the discourse reports a "
            "set of standing titles and then adds a fourth of a different kind to the same sentence, "
            "which is a rhetorical move rather than a cosmological claim."]),
        ("Using it", [
            "The discourse is a good teaching text for a specific question: what do you actually want "
            "to be foremost in? Set out plainly, the three worldly superlatives are physical scale, "
            "quantity of pleasure, and extent of control &mdash; which between them cover most of what "
            "ambition pursues, in this world as in that one.",
            "The discourse&rsquo;s answer is not that a smaller share of these is better. It is that "
            "the whole scale is the wrong one, and that its record-holders are a monster, a "
            "cautionary tale, and the adversary."]),
    ],
    terms=[
        ("paññatti",
         "&ldquo;designation, description&rdquo; &mdash; the title word. The discourse reports "
         "standing titles rather than measurements."),
        ("Rāhu",
         "lord of the titans and the eclipse figure of Indian cosmology &mdash; the being who "
         "swallows the sun and moon. Foremost in size of body."),
        ("Mandhātā",
         "a legendary wheel-turning monarch who obtained everything and wanted more. Foremost in "
         "enjoying sensual pleasures, and a cautionary tale."),
        ("issariya",
         "&ldquo;sovereignty, lordship&rdquo; &mdash; the superlative held by Māra, whose power in "
         "this cosmology is real rather than decorative."),
        ("agga",
         "&ldquo;best, foremost&rdquo; &mdash; the word applied to the Buddha, stated against the "
         "whole of existence with no category named."),
    ],
    text_intro=(
        "The discourse in full: the four regarded as foremost, and the two verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four regarded as foremost"),
        ("p", "&sect;1", "an4.15:1.1-1.10"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.15:2.1-2.4"),
        ("p", "&sect;3", "an4.15:3.1-3.4"),
    ],
    quiz=[
        {"q": "Who holds the record for size of body?",
         "opts": [
             "Māra",
             "Rāhu, lord of titans",
             "Mandhātā",
             "Sakka"],
         "correct": 1,
         "expl": "The eclipse figure who swallows the sun and moon."},
        {"q": "Who is Mandhātā?",
         "opts": [
             "A brahmin teacher",
             "A legendary wheel-turning monarch who obtained everything a being can obtain and wanted more",
             "A titan general",
             "A disciple of the Buddha"],
         "correct": 1,
         "expl": "He shared the throne with Sakka, and wanting more is what destroyed him."},
        {"q": "What is Māra foremost in?",
         "opts": [
             "Deception",
             "Sovereignty",
             "Longevity",
             "Strength"],
         "correct": 1,
         "expl": "His power in this cosmology is real, not decorative."},
        {"q": "What does the guide say about the selection of the first three?",
         "opts": [
             "They are lesser goods arranged below a greater one",
             "They are three superlatives held by beings the tradition regards as irrelevant, ruined, and hostile",
             "They are chosen at random",
             "They are all deities of the same heaven"],
         "correct": 1,
         "expl": "The selection is deliberate and slightly mocking."},
        {"q": "How is the fourth item phrased differently?",
         "opts": [
             "It is shorter",
             "It gets a long scope clause against the whole of existence with no category named &mdash; simply <em>aggo</em>, best",
             "It is in verse only",
             "It names no one"],
         "correct": 1,
         "expl": "The other three superlatives are held within a category."},
        {"q": "What does that construction accomplish?",
         "opts": [
             "It ranks the Buddha above Māra on the same scale",
             "It changes the subject at the fourth item &mdash; the Buddha is not more of what they have more of",
             "It equates all four",
             "It leaves the ranking open"],
         "correct": 1,
         "expl": "Noticing that is the whole reading."},
        {"q": "What does <em>paññatti</em> mean?",
         "opts": [
             "Measurement",
             "Designation, description &mdash; what is made known or laid down",
             "Superlative",
             "Cosmology"],
         "correct": 1,
         "expl": "A matter of reputation and title rather than of measurement."},
        {"q": "What qualification does that put on the discourse?",
         "opts": [
             "None",
             "It reports standing titles rather than making cosmological claims &mdash; a rhetorical move",
             "It makes the fourth item uncertain",
             "It limits the claim to India"],
         "correct": 1,
         "expl": "Read strictly, the discourse adds a fourth of a different kind to the same sentence."},
        {"q": "What three things do the worldly superlatives cover?",
         "opts": [
             "Wealth, fame, and family",
             "Physical scale, quantity of pleasure, and extent of control",
             "Knowledge, virtue, and power",
             "Birth, beauty, and skill"],
         "correct": 1,
         "expl": "Between them, most of what ambition pursues."},
        {"q": "What is the discourse&rsquo;s answer to that ambition?",
         "opts": [
             "That a smaller share is better",
             "That the whole scale is the wrong one",
             "That the records cannot be broken",
             "That ambition is natural"],
         "correct": 1,
         "expl": "Its record-holders are a monster, a cautionary tale, and the adversary."},
    ],
    marginalia=[
        ("The four", [
            "Rāhu &middot; size",
            "Mandhātā &middot; pleasure",
            "Māra &middot; sovereignty",
            "the Buddha &middot; best",
        ]),
        ("Three worthless records", [
            "irrelevant",
            "ruined",
            "hostile",
        ]),
        ("The scope clause", [
            "with its gods and Māras",
            "ascetics and brahmins",
            "&mdash; and no category named",
        ]),
        ("Cross-references", [
            "AN 4.16 &middot; next: four subtleties",
            "AN 4.8 &middot; the Buddha&rsquo;s four assurances",
            "AN 4.9 &middot; craving that outruns supply",
        ]),
    ],
    further=[
        '<a href="%s/an4.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.16.html">AN 4.16 &middot; Subtlety</a> &mdash; next in this series.',
        '<a href="an-4.8.html">AN 4.8 &middot; Self-assured</a> &mdash; the other acclamatory '
        "discourse of the Fours&rsquo; opening chapters.",
        '<a href="an-4.9.html">AN 4.9 &middot; The Arising of Craving</a> &mdash; on the craving that '
        "no supply satisfies.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.16 — Sokhummasutta
# --------------------------------------------------------------------------- #
page(
    16, "Sokhumma", "Subtlety",
    vagga=VAGGA_2,
    meta_title="AN 4.16 — Subtlety | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sokhummasutta — ultimate "
        "subtlety of form, feeling, perception, and choices, and the mendicant who does not aim for "
        "anything finer. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "Four items, each with the same two-part clause, and three verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Analyses of the aggregates by degrees of refinement appear across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the most compressed discourse of "
                       "the chapter, and the hardest to be sure of"),
    ],
    why=(
        "Four subtleties &mdash; of form, feeling, perception, and choices &mdash; and in each case "
        "the same clause: the mendicant does not see any subtlety better or finer than that, and "
        "does not aim for one. It is a difficult discourse and honest reading has to say so. What "
        "is clear is the shape: four of the five aggregates, an endpoint reached in each, and the "
        "cessation of a particular kind of searching."),
    guide=[
        ("The teaching in one sentence", [
            "In each of four domains a practitioner reaches the finest available refinement and stops "
            "looking for a finer one &mdash; and the stopping is the point."]),
        ("Four of the five", [
            "Form, feeling, perception, choices. The fifth aggregate, consciousness "
            "(<em>viññāṇa</em>), is missing, and its absence is what makes this a discourse of the "
            "Fours rather than the Fives.",
            "It would be easy to over-read that. The Aṅguttara is organized by number, and material "
            "gets shaped to fit the section it lands in; a four-item version of a five-item set is "
            "not necessarily making a doctrinal point. What can be said is that the four named are "
            "the ones a meditator encounters as objects, and consciousness in this analysis is not an "
            "object alongside them."]),
        ("What &lsquo;subtlety&rsquo; means here", [
            "<em>Sokhumma</em> is fineness, refinement, subtlety &mdash; the abstract noun from "
            "<em>sukhuma</em>, subtle. The discourse says a mendicant has <em>ultimate</em> subtlety "
            "(<em>paramasokhumma</em>) of each.",
            "The most defensible reading takes this as meditative attainment. In the jhāna sequence "
            "and the formless attainments, form, feeling, and perception each become progressively "
            "more refined; the tradition speaks in exactly these terms. A practitioner who has gone "
            "as far as that progression goes has reached ultimate subtlety in each.",
            "The commentarial tradition reads it this way, and the second half of each clause "
            "supports it: not seeing a finer one and not aiming for one is the language of a search "
            "concluded, not of a doctrine held."]),
        ("The two clauses, and why the second matters", [
            "Each item has two parts. They do not see any other subtlety better or finer than that. "
            "And they do not aim for it.",
            "The second is not a repetition. Not seeing something finer might merely be a limit of "
            "vision; not aiming for it is a settled disposition. Together they describe a mind that "
            "has both arrived and stopped looking, and the discourse gives equal weight to each.",
            "This matters practically, because refinement is one of the more durable traps in "
            "contemplative practice. The pursuit of a subtler state is itself a form of wanting, and "
            "it survives most of the coarser forms. A discourse whose criterion is that one no longer "
            "aims for anything finer is naming that trap precisely."]),
        ("The verses go further than the prose", [
            "The verses do something the prose does not: they apply the three characteristics. "
            "Knowing choices <em>as alien, as suffering and as not-self</em> &mdash; and knowing where "
            "perception comes from and where it ends.",
            "That converts the discourse from an attainment scheme into an insight one. Reaching the "
            "finest refinement of an aggregate is one thing; seeing the aggregate as not-self is "
            "another, and only the second produces the outcome the verse claims: bearing the final "
            "body, having vanquished Māra.",
            "Read as a whole, then, the discourse and its verses together say that refinement is "
            "where the work happens but not what completes it. The prose ends the search; the verses "
            "supply what the search was for."]),
        ("Reading it honestly", [
            "This page has given the most defensible reading, and it should be said plainly that the "
            "prose is compressed enough to support others. The discourse does not define "
            "&lsquo;ultimate subtlety&rsquo;, does not say how it is reached, and does not explain why "
            "consciousness is absent.",
            "Where a text is this brief, the responsible teaching move is to give the structure "
            "confidently and the interpretation provisionally. The structure is secure: four "
            "aggregates, an endpoint in each, a search concluded, and verses that supply insight. "
            "What ultimate subtlety of form <em>is</em> remains a question this discourse leaves "
            "open."]),
    ],
    terms=[
        ("sokhumma",
         "&ldquo;subtlety, fineness&rdquo; &mdash; the abstract noun from <em>sukhuma</em>. The "
         "discourse speaks of <em>ultimate</em> subtlety in each of four domains."),
        ("rūpa, vedanā, saññā, saṅkhārā",
         "form, feeling, perception, and choices &mdash; four of the five aggregates. The fifth, "
         "consciousness, is absent."),
        ("nappaṇidahati",
         "&ldquo;does not aim for it&rdquo; &mdash; the second clause of each item, and a settled "
         "disposition rather than a limit of vision."),
        ("parato",
         "&ldquo;as alien, as other&rdquo; &mdash; one of the three terms the verses apply to "
         "choices, alongside suffering and not-self."),
        ("antimadeha",
         "&ldquo;the final body&rdquo; &mdash; what the mendicant of the closing verse bears, having "
         "vanquished Māra with his legions."),
    ],
    text_intro=(
        "The discourse in full: the four subtleties and the three verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four kinds of subtlety"),
        ("p", "&sect;1", "an4.16:1.1-1.15"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.16:2.1-2.6"),
        ("p", "&sect;3", "an4.16:3.1-3.4"),
    ],
    quiz=[
        {"q": "What four things does the discourse name subtlety of?",
         "opts": [
             "Body, feelings, mind, and principles",
             "Form, feeling, perception, and choices",
             "Earth, water, fire, and air",
             "Sight, sound, smell, and taste"],
         "correct": 1,
         "expl": "Four of the five aggregates."},
        {"q": "Which aggregate is missing?",
         "opts": [
             "Form",
             "Consciousness",
             "Perception",
             "Choices"],
         "correct": 1,
         "expl": "Its absence is what makes this a discourse of the Fours."},
        {"q": "How does the guide handle that absence?",
         "opts": [
             "As a decisive doctrinal claim",
             "Cautiously &mdash; the Aṅguttara shapes material to fit its number, though the four named are the ones a meditator encounters as objects",
             "As a textual error",
             "As proof of a late date"],
         "correct": 1,
         "expl": "Consciousness in this analysis is not an object alongside them."},
        {"q": "What is the most defensible reading of &lsquo;ultimate subtlety&rsquo;?",
         "opts": [
             "A philosophical position",
             "Meditative attainment &mdash; the progressive refinement of form, feeling, and perception in the jhānas and formless attainments",
             "Physical fineness of matter",
             "Skill in debate"],
         "correct": 1,
         "expl": "The commentarial tradition reads it this way, and the second clause supports it."},
        {"q": "What are the two clauses attached to each item?",
         "opts": [
             "That it is impermanent, and that it is suffering",
             "That they see nothing finer, and that they do not aim for anything finer",
             "That it arises, and that it ceases",
             "That it is known, and that it is abandoned"],
         "correct": 1,
         "expl": "A mind that has both arrived and stopped looking."},
        {"q": "Why is the second clause not a repetition?",
         "opts": [
             "It is in a different tense",
             "Not seeing something finer might merely be a limit of vision; not aiming for it is a settled disposition",
             "It applies to a different aggregate",
             "It belongs to the verses"],
         "correct": 1,
         "expl": "The discourse gives equal weight to each."},
        {"q": "Why does the guide call refinement a trap?",
         "opts": [
             "Because subtle states are unpleasant",
             "Because the pursuit of a subtler state is itself a form of wanting, and it survives most of the coarser forms",
             "Because they cannot be attained",
             "Because they lead to conceit only"],
         "correct": 1,
         "expl": "A criterion of no longer aiming for anything finer names that trap precisely."},
        {"q": "What do the verses add?",
         "opts": [
             "A setting",
             "The three characteristics &mdash; knowing choices as alien, as suffering, and as not-self",
             "A list of the jhānas",
             "The name of the speaker"],
         "correct": 1,
         "expl": "Which converts an attainment scheme into an insight one."},
        {"q": "What does the guide conclude from that?",
         "opts": [
             "That the verses contradict the prose",
             "That refinement is where the work happens but not what completes it &mdash; the prose ends the search, the verses supply what it was for",
             "That the prose is redundant",
             "That the verses are later"],
         "correct": 1,
         "expl": "Only insight produces the outcome the verse claims."},
        {"q": "What does the guide say remains open?",
         "opts": [
             "Whether the discourse is authentic",
             "What ultimate subtlety of form actually is &mdash; the discourse does not define it or say how it is reached",
             "Who the discourse addresses",
             "Whether the aggregates are four or five"],
         "correct": 1,
         "expl": "Structure confidently, interpretation provisionally."},
    ],
    marginalia=[
        ("Four subtleties", [
            "<span class=\"pali\">rūpa</span>form",
            "<span class=\"pali\">vedanā</span>feeling",
            "<span class=\"pali\">saññā</span>perception",
            "<span class=\"pali\">saṅkhārā</span>choices",
        ]),
        ("Two clauses", [
            "sees nothing finer",
            "aims for nothing finer",
            "&mdash; vision, then disposition",
        ]),
        ("The verses", [
            "alien",
            "suffering",
            "not-self",
        ]),
        ("Cross-references", [
            "AN 4.15 &middot; the other kind of superlative",
            "AN 4.17 &middot; next: prejudiced decisions",
            "AN 4.10 &middot; the five headings of analysis",
        ]),
    ],
    further=[
        '<a href="%s/an4.16/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.17.html">AN 4.17 &middot; Prejudice (1st)</a> &mdash; next in this series.',
        '<a href="an-4.10.html">AN 4.10 &middot; Yokes</a> &mdash; where the five headings of '
        "analysis are set out.",
        '<a href="an-4.170.html">AN 4.170 &middot; In Conjunction</a> &mdash; further into the Fours, '
        "on serenity and insight together.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.17 — Paṭhamaagatisutta
# --------------------------------------------------------------------------- #
page(
    17, "Paṭhamaagati", "Prejudice (1st)",
    vagga=VAGGA_2,
    meta_title="AN 4.17 — Prejudice (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamaagatisutta — "
        "favoritism, hostility, stupidity, and cowardice: the four ways of making prejudiced "
        "decisions, and the moon in the waning fortnight. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of four, and one verse"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "The four <em>agati</em> are widespread in the Chinese Āgamas and in "
                              "the Pāli Vinaya; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest kind of discourse in "
                       "the collection, and one of the most useful"),
    ],
    why=(
        "Four ways a decision goes wrong: favoritism, hostility, stupidity, and cowardice. The list "
        "is old, it is short, and it has outlived its context entirely &mdash; the same four terms "
        "are still quoted in Theravāda countries as the standard test of an official acting badly. "
        "This is the first of four consecutive discourses that use it, and the bare list is worth "
        "learning by heart."),
    guide=[
        ("The teaching in one sentence", [
            "A decision can be corrupted in four ways: by who you like, who you dislike, what you "
            "have not understood, and what you are afraid of."]),
        ("The four terms", [
            "<em>Chanda</em>, desire or preference, rendered here as favoritism &mdash; deciding for "
            "someone because they are yours. <em>Dosa</em>, hatred, as hostility &mdash; deciding "
            "against someone because of a grudge. <em>Moha</em>, delusion, as stupidity &mdash; "
            "deciding wrongly because you did not grasp the matter. <em>Bhaya</em>, fear, as "
            "cowardice &mdash; deciding to avoid a consequence to yourself.",
            "The collective term is <em>agati</em>, literally &lsquo;not-going&rsquo; or a wrong "
            "course. The image is of a path departed from: a decision has a proper route, and these "
            "are the four ways off it.",
            "It is a well-built list. The first two are partiality in both directions, positive and "
            "negative. The third is failure of competence rather than of will. The fourth is "
            "self-interest of a particular kind &mdash; not gain but the avoidance of cost. Between "
            "them they cover corruption by affection, by grudge, by incapacity, and by pressure, and "
            "it is genuinely hard to name a fifth."]),
        ("Stupidity is on the list", [
            "The inclusion of <em>moha</em> is the part most worth pausing on. Three of the four are "
            "faults of motive; one is a fault of understanding. The list makes no distinction between "
            "them in its consequences.",
            "That is a demanding standard and a fair one. A decision made in good faith by someone who "
            "did not do the work of understanding the case is on this list alongside a bribed one. "
            "The person harmed is harmed either way, and the discourse declines to grade by "
            "intention.",
            "It also connects this list to the rest of the collection. AN 4.3, thirteen discourses "
            "earlier, made exactly this point about praise and criticism: the fault is not the wrong "
            "verdict but the missing examination. Here the same principle is applied to office."]),
        ("The moon", [
            "The verse says that one who acts against the teaching in these four ways has their fame "
            "fade <em>like the moon in the waning fortnight</em>.",
            "The image is well chosen for the subject. A waning moon is not extinguished by an event; "
            "it diminishes on a schedule, visibly, a little each night, and everyone watching can see "
            "which way it is going. Reputation lost to partiality behaves the same way. Nobody "
            "announces it and everybody notices.",
            "AN 4.18 supplies the waxing half, and the two verses are meant to be held together."]),
        ("Why four discourses", [
            "AN 4.17 gives the negative list. AN 4.18 gives the positive. AN 4.19 gives both in one "
            "discourse with both verses. AN 4.20 applies the same four to a particular monastic "
            "officer.",
            "This is not padding, and it is not accident. The Aṅguttara is arranged for recitation, "
            "and a set of short discourses in negative, positive, combined, and applied forms is a "
            "complete teaching unit for a reciter &mdash; four ways of holding one list. A modern "
            "reader who finds the repetition tedious is encountering a genuine feature of an oral "
            "collection rather than a defect in it."]),
    ],
    terms=[
        ("agati",
         "&ldquo;prejudice&rdquo;, literally &lsquo;not-going&rsquo; or a wrong course &mdash; a "
         "decision has a proper route, and these are the four ways off it."),
        ("chanda",
         "&ldquo;desire, preference&rdquo;, here favoritism &mdash; deciding for someone because they "
         "are yours."),
        ("dosa",
         "&ldquo;hatred&rdquo;, here hostility &mdash; deciding against someone because of a "
         "grudge."),
        ("moha",
         "&ldquo;delusion&rdquo;, here stupidity &mdash; the one fault of competence rather than of "
         "motive, and graded no differently."),
        ("bhaya",
         "&ldquo;fear&rdquo;, here cowardice &mdash; self-interest of a particular kind: not gain but "
         "the avoidance of cost."),
    ],
    text_intro=(
        "The discourse in full: the four, and the verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four prejudiced decisions"),
        ("p", "&sect;1", "an4.17:1.1-1.4"),
        ("h3", "The verse"),
        ("p", "&sect;2", "an4.17:2.1-2.4"),
    ],
    quiz=[
        {"q": "What are the four ways of making prejudiced decisions?",
         "opts": [
             "Greed, hatred, delusion, and conceit",
             "Favoritism, hostility, stupidity, and cowardice",
             "Haste, delay, silence, and noise",
             "Bribery, threat, flattery, and deceit"],
         "correct": 1,
         "expl": "<em>Chanda</em>, <em>dosa</em>, <em>moha</em>, <em>bhaya</em>."},
        {"q": "What does <em>agati</em> literally mean?",
         "opts": [
             "Prejudice",
             "&lsquo;Not-going&rsquo; &mdash; a wrong course, a path departed from",
             "Corruption",
             "Judgment"],
         "correct": 1,
         "expl": "A decision has a proper route, and these are the four ways off it."},
        {"q": "Which of the four is a fault of competence rather than motive?",
         "opts": [
             "Favoritism",
             "Stupidity",
             "Hostility",
             "Cowardice"],
         "correct": 1,
         "expl": "And the list makes no distinction in its consequences."},
        {"q": "Why does the guide call that a fair standard?",
         "opts": [
             "Because incompetence is rare",
             "Because the person harmed is harmed either way, and the discourse declines to grade by intention",
             "Because good faith cannot be verified",
             "Because delusion is the root of the other three"],
         "correct": 1,
         "expl": "A decision made without doing the work sits alongside a bribed one."},
        {"q": "What does cowardice mean on this list?",
         "opts": [
             "Timidity in battle",
             "Deciding to avoid a consequence to yourself &mdash; self-interest as avoidance of cost rather than pursuit of gain",
             "Refusing to decide at all",
             "Fear of the teacher"],
         "correct": 1,
         "expl": "Which is what distinguishes it from ordinary self-dealing."},
        {"q": "What does the list cover between its four terms?",
         "opts": [
             "Only monastic faults",
             "Corruption by affection, by grudge, by incapacity, and by pressure",
             "The three unwholesome roots",
             "Speech, thought, action, and livelihood"],
         "correct": 1,
         "expl": "It is genuinely hard to name a fifth."},
        {"q": "Which earlier discourse of the Fours makes the same point about examination?",
         "opts": [
             "AN 4.1",
             "AN 4.3 &mdash; the fault is not the wrong verdict but the missing examination",
             "AN 4.10",
             "AN 4.15"],
         "correct": 1,
         "expl": "Here the same principle is applied to office."},
        {"q": "What is the image in the verse?",
         "opts": [
             "A fire that spreads",
             "The moon in the waning fortnight",
             "A river in flood",
             "A tree cut down"],
         "correct": 1,
         "expl": "AN 4.18 supplies the waxing half."},
        {"q": "Why does the guide say the image is well chosen?",
         "opts": [
             "Because the moon is beautiful",
             "Because a waning moon diminishes on a schedule, visibly &mdash; nobody announces it and everybody notices",
             "Because the moon returns",
             "Because it was a familiar sight"],
         "correct": 1,
         "expl": "Reputation lost to partiality behaves the same way."},
        {"q": "Why are there four consecutive discourses on this list?",
         "opts": [
             "Editorial accident",
             "Negative, positive, combined, and applied &mdash; a complete teaching unit for a reciter",
             "Because the list was disputed",
             "Because each has a different author"],
         "correct": 1,
         "expl": "A genuine feature of an oral collection rather than a defect in it."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">chanda</span>favoritism",
            "<span class=\"pali\">dosa</span>hostility",
            "<span class=\"pali\">moha</span>stupidity",
            "<span class=\"pali\">bhaya</span>cowardice",
        ]),
        ("What they cover", [
            "affection",
            "grudge",
            "incapacity",
            "pressure",
        ]),
        ("The image", [
            "the waning moon",
            "no announcement",
            "&mdash; and everybody notices",
        ]),
        ("Cross-references", [
            "AN 4.18 &middot; next: the waxing half",
            "AN 4.19 &middot; both in one",
            "AN 4.20 &middot; applied to the meal assigner",
        ]),
    ],
    further=[
        '<a href="%s/an4.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.18.html">AN 4.18 &middot; Prejudice (2nd)</a> &mdash; next in this series, the '
        "positive form.",
        '<a href="an-4.20.html">AN 4.20 &middot; A Meal Assigner</a> &mdash; the same four applied to '
        "a monastic office.",
        '<a href="an-4.3.html">AN 4.3 &middot; Broken (1st)</a> &mdash; on judging without '
        "examining.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.18 — Dutiyaagatisutta
# --------------------------------------------------------------------------- #
page(
    18, "Dutiyaagati", "Prejudice (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 4.18 — Prejudice (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyaagatisutta — the four "
        "ways of making unprejudiced decisions, and the moon in the waxing fortnight. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "The same four in the negative, and one verse"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "As with AN 4.17, the four <em>agati</em> are widespread in the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the mirror of the previous "
                       "discourse, and its whole interest is in being a mirror"),
    ],
    why=(
        "The same four terms, negated: decisions unprejudiced by favoritism, hostility, stupidity, "
        "and cowardice, and a reputation that swells like the waxing moon. On its own the discourse "
        "adds nothing to AN 4.17, and saying so is not a criticism &mdash; the pairing is the "
        "collection&rsquo;s method, and what it is for is worth understanding."),
    guide=[
        ("The teaching in one sentence", [
            "The four ways a decision goes wrong, stated as the four ways it can be sound."]),
        ("Why the mirror exists", [
            "The Aṅguttara pairs discourses like this constantly, and it is not filler. Two things "
            "are accomplished.",
            "First, the negative form gives the practitioner something to do. A list of four faults "
            "tells you what to avoid; the same list negated tells you what a good decision looks like "
            "from the inside &mdash; and those are different mental operations. A person checking "
            "themselves for favoritism is doing something other than a person aiming at "
            "impartiality.",
            "Second, it makes the pair recitable. In an oral collection the negative and the positive "
            "form a matched unit, and the reciter who has one has the other. This is the same "
            "economy visible in AN 4.11 and 4.12, and in AN 4.3 and 4.4."]),
        ("The waxing moon", [
            "AN 4.17&rsquo;s waning moon and this discourse&rsquo;s waxing one are one image split "
            "across two texts. The verse says that one who does not act against the teaching in these "
            "four ways has their fame <em>swell</em>, <em>like the moon in the waxing fortnight</em>.",
            "The observation embedded in the image is worth stating. Reputation for fairness is not "
            "made by a single decision, any more than the moon fills in a night. It accumulates "
            "through a sequence of small, individually unremarkable decisions in which nothing "
            "improper happened. That is why it is slow to build and, in the waning version, slow but "
            "steady to lose.",
            "It is also a notably modest promise. The discourse does not offer heaven, attainment, or "
            "the ending of suffering for making decisions well. It offers a reputation. For a "
            "collection frequently accused of promising too much, this is a discourse that promises "
            "exactly what the conduct in question actually produces."]),
        ("Fame as a criterion", [
            "<em>Yaso</em>, the word rendered &lsquo;fame&rsquo;, covers reputation, standing, and "
            "renown &mdash; and the collection is elsewhere sharply suspicious of it. Gain, honor, "
            "and praise are named repeatedly as dangers.",
            "There is no contradiction, but the distinction is worth drawing for students. What is "
            "dangerous is wanting fame and being changed by it. What this discourse describes is fame "
            "as an <em>indicator</em>: the visible consequence of a long run of sound decisions, "
            "reported from the outside. The verse tells you what happens, not what to aim at."]),
        ("Using the negative form", [
            "Practically, this is the version to hand to someone who holds an office. Read as "
            "questions the four become a checklist that can be run before a decision rather than "
            "after it: Am I deciding this because of who they are to me? Because of a grudge? Have I "
            "actually understood the case? Am I avoiding a cost to myself?",
            "AN 4.17 diagnoses; AN 4.18 prompts. That is the practical difference between a list of "
            "faults and its negation, and it is why the collection bothers to give both."]),
    ],
    terms=[
        ("agati",
         "&ldquo;prejudice&rdquo;, literally a wrong course &mdash; here negated: decisions that do "
         "not depart from the proper route."),
        ("yaso",
         "&ldquo;fame, reputation, standing&rdquo; &mdash; what swells. Elsewhere the collection is "
         "suspicious of it; here it is an indicator rather than a goal."),
        ("chanda",
         "&ldquo;preference, favoritism&rdquo; &mdash; the first of the four, negated. Not deciding "
         "for someone because they are yours."),
        ("bhaya",
         "&ldquo;fear, cowardice&rdquo; &mdash; the fourth, negated. Not deciding so as to avoid a "
         "cost to oneself."),
        ("sukkapakkha",
         "&ldquo;the bright fortnight&rdquo; &mdash; the waxing half of the lunar month, against "
         "AN 4.17&rsquo;s dark fortnight."),
    ],
    text_intro=(
        "The discourse in full: the four negated, and the verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four unprejudiced decisions"),
        ("p", "&sect;1", "an4.18:1.1-1.4"),
        ("h3", "The verse"),
        ("p", "&sect;2", "an4.18:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does AN 4.18 state?",
         "opts": [
             "A new list of four",
             "The four ways of making unprejudiced decisions &mdash; AN 4.17&rsquo;s list negated",
             "The consequences of prejudice",
             "The duties of an official"],
         "correct": 1,
         "expl": "Its whole interest is in being a mirror."},
        {"q": "What is the first thing the mirror accomplishes?",
         "opts": [
             "It shortens the teaching",
             "It gives the practitioner something to do &mdash; a list of faults tells you what to avoid, its negation tells you what a good decision looks like from the inside",
             "It adds a new fault",
             "It corrects an error"],
         "correct": 1,
         "expl": "Checking for favoritism and aiming at impartiality are different mental operations."},
        {"q": "What is the second?",
         "opts": [
             "It provides a verse",
             "It makes the pair recitable &mdash; in an oral collection the reciter who has one has the other",
             "It settles a dispute",
             "It names the audience"],
         "correct": 1,
         "expl": "The same economy visible in AN 4.11 and 4.12."},
        {"q": "What is the image in this verse?",
         "opts": [
             "The sun at noon",
             "The moon in the waxing fortnight",
             "A rising river",
             "A growing tree"],
         "correct": 1,
         "expl": "One image split across two texts with AN 4.17."},
        {"q": "What observation does the guide draw from it?",
         "opts": [
             "That reputation is fragile",
             "That reputation for fairness accumulates through a sequence of small, individually unremarkable decisions in which nothing improper happened",
             "That the moon is a symbol of the Buddha",
             "That fame is cyclical"],
         "correct": 1,
         "expl": "Slow to build, and slow but steady to lose."},
        {"q": "What does the discourse promise for deciding well?",
         "opts": [
             "Heaven",
             "A reputation &mdash; and nothing more",
             "Attainment of the path",
             "The ending of suffering"],
         "correct": 1,
         "expl": "A notably modest promise, and exactly what the conduct produces."},
        {"q": "How does this square with the collection&rsquo;s suspicion of fame?",
         "opts": [
             "It does not; the two conflict",
             "What is dangerous is wanting fame and being changed by it; here fame is an indicator reported from the outside",
             "The suspicion applies only to monastics",
             "This discourse is an exception"],
         "correct": 1,
         "expl": "The verse tells you what happens, not what to aim at."},
        {"q": "What does <em>yaso</em> cover?",
         "opts": [
             "Wealth",
             "Reputation, standing, and renown",
             "Rank in the order",
             "Merit"],
         "correct": 1,
         "expl": "Named elsewhere alongside gain and honor as a danger."},
        {"q": "How does the guide suggest using the negative form?",
         "opts": [
             "As a devotional recitation",
             "As a checklist that can be run before a decision rather than after it",
             "As a rule for ordination",
             "As a meditation subject"],
         "correct": 1,
         "expl": "Am I deciding this because of who they are to me? Because of a grudge? Have I understood the case? Am I avoiding a cost?"},
        {"q": "What is the practical difference between AN 4.17 and AN 4.18?",
         "opts": [
             "One is monastic and one lay",
             "AN 4.17 diagnoses; AN 4.18 prompts",
             "One is longer",
             "They address different faults"],
         "correct": 1,
         "expl": "Which is why the collection bothers to give both."},
    ],
    marginalia=[
        ("The four, negated", [
            "not favoritism",
            "not hostility",
            "not stupidity",
            "not cowardice",
        ]),
        ("Before or after", [
            "AN 4.17 &middot; diagnoses",
            "AN 4.18 &middot; prompts",
            "&mdash; a checklist, not a verdict",
        ]),
        ("The promise", [
            "not heaven",
            "not attainment",
            "a reputation",
        ]),
        ("Cross-references", [
            "AN 4.17 &middot; the waning moon",
            "AN 4.19 &middot; next: both halves at once",
            "AN 4.20 &middot; the office it applies to",
        ]),
    ],
    further=[
        '<a href="%s/an4.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.19.html">AN 4.19 &middot; Prejudice (3rd)</a> &mdash; next in this series, '
        "both halves in one discourse.",
        '<a href="an-4.17.html">AN 4.17 &middot; Prejudice (1st)</a> &mdash; the negative form and '
        "the waning moon.",
        '<a href="an-4.20.html">AN 4.20 &middot; A Meal Assigner</a> &mdash; the four applied to an '
        "office with real consequences.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.19 — Tatiyaagatisutta
# --------------------------------------------------------------------------- #
page(
    19, "Tatiyaagati", "Prejudice (3rd)",
    vagga=VAGGA_2,
    meta_title="AN 4.19 — Prejudice (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Tatiyaagatisutta — the four "
        "prejudiced and the four unprejudiced ways of deciding, given together with both moons. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "Both halves of AN 4.17 and 4.18 in one discourse, with both verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 4.17 and 4.18; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; nothing new, and the fact that "
                       "there is nothing new is the subject"),
    ],
    why=(
        "This discourse contains no material that AN 4.17 and AN 4.18 do not contain. It is the two "
        "of them joined, with both verses, and it exists because a combined form is a different "
        "thing to recite from a pair of separate ones. It is the clearest small window in the "
        "chapter onto how the collection was actually assembled, and it is worth one page for that "
        "reason alone."),
    guide=[
        ("The teaching in one sentence", [
            "The four prejudices and their negation, given in one breath so that the contrast is "
            "heard rather than reconstructed."]),
        ("What the combined form does", [
            "Reading AN 4.17 and 4.18 in sequence, the listener holds the first list, hears a closing "
            "verse, and then starts again. Reading AN 4.19, the two lists arrive without an "
            "interruption between them, and only then do the verses come &mdash; both of them, one "
            "after the other.",
            "The effect is different in a way that matters for oral teaching. In the combined form the "
            "moons are adjacent: waning immediately followed by waxing, one lunar month completed in "
            "eight lines. In the separate discourses each image stands alone and the pairing has to be "
            "supplied by the listener.",
            "A reciter would use whichever form suited the occasion. That the collection preserves "
            "both is not redundancy in the sense of waste; it is the retention of two usable "
            "versions."]),
        ("What this reveals about the collection", [
            "The Aṅguttara is a compilation, and discourses like this one make the seams visible. "
            "Somewhere behind AN 4.17&ndash;4.19 there is a single teaching about four ways of "
            "deciding badly, which has been transmitted in three arrangements, each preserved as its "
            "own numbered discourse.",
            "This is worth knowing because it changes what a reader should expect. The numbering of "
            "the Aṅguttara counts <em>units of recitation</em>, not distinct teachings. A collection "
            "of 1,408 discourses in the Fours does not contain 1,408 different things to learn, and a "
            "reader who expects it to will find the collection maddening.",
            "It also means that a page like this one, honestly written, has to be partly about the "
            "text&rsquo;s history rather than only about its content. There is no third teaching here "
            "to find, and pretending otherwise would be a disservice."]),
        ("The four, once more", [
            "For completeness: favoritism (<em>chanda</em>), hostility (<em>dosa</em>), stupidity "
            "(<em>moha</em>), and cowardice (<em>bhaya</em>). Partiality toward, partiality against, "
            "failure to understand, and fear of consequences.",
            "The version worth memorizing is this combined one, precisely because it carries both "
            "directions. A list held only in the negative tends to become a list of accusations to "
            "make of other people; held in both directions it stays usable on oneself."]),
        ("Where it goes next", [
            "AN 4.20 completes the group by applying the four to a named office &mdash; the mendicant "
            "who assigns meals &mdash; with consequences stated as hell and heaven rather than as "
            "reputation.",
            "That escalation is worth watching. Across four short discourses the same list moves from "
            "an abstract statement, to its mirror, to the combined form, to a concrete official with "
            "a specific job and a stated destination. The group is arranged from the general to the "
            "particular, which is a common shape in this collection and a good one for teaching."]),
    ],
    terms=[
        ("agati",
         "&ldquo;prejudice&rdquo;, a wrong course &mdash; the term for all four, given here in both "
         "the affirmative and the negative."),
        ("chanda / dosa",
         "&ldquo;favoritism&rdquo; and &ldquo;hostility&rdquo; &mdash; partiality in both directions, "
         "toward and against."),
        ("moha",
         "&ldquo;stupidity&rdquo; &mdash; the failure of understanding rather than of motive, "
         "included without any softening."),
        ("kāḷapakkha / sukkapakkha",
         "the dark and bright fortnights &mdash; the waning and waxing moons, given here adjacent to "
         "one another."),
        ("yaso",
         "&ldquo;fame, reputation&rdquo; &mdash; what fades in the first verse and swells in the "
         "second."),
    ],
    text_intro=(
        "The discourse in full: both lists and both verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Prejudiced decisions"),
        ("p", "&sect;1", "an4.19:1.1-1.4"),
        ("h3", "Unprejudiced decisions"),
        ("p", "&sect;2", "an4.19:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.19:3.1-3.4"),
        ("p", "&sect;4", "an4.19:4.1-4.4"),
    ],
    quiz=[
        {"q": "What does AN 4.19 contain?",
         "opts": [
             "A third list of four",
             "Both halves of AN 4.17 and AN 4.18, with both verses",
             "A commentary on the previous two",
             "An application to a monastic office"],
         "correct": 1,
         "expl": "No material that the previous two do not contain."},
        {"q": "Why does the combined form exist?",
         "opts": [
             "It replaced the separate versions",
             "Because it is a different thing to recite &mdash; the two lists arrive without interruption, and the moons are adjacent",
             "It corrects an error in AN 4.17",
             "It was added by a commentator"],
         "correct": 1,
         "expl": "One lunar month completed in eight lines."},
        {"q": "What does the guide say the preservation of both forms represents?",
         "opts": [
             "Waste in transmission",
             "The retention of two usable versions, each suited to different occasions",
             "A scribal duplication",
             "Two competing schools"],
         "correct": 1,
         "expl": "A reciter would use whichever suited."},
        {"q": "What do discourses like this reveal about the Aṅguttara?",
         "opts": [
             "That it is late",
             "That it is a compilation whose seams are visible &mdash; one teaching transmitted in three arrangements, each preserved as its own numbered discourse",
             "That it was written down early",
             "That the Fours are incomplete"],
         "correct": 1,
         "expl": "Somewhere behind AN 4.17&ndash;4.19 there is a single teaching."},
        {"q": "What does the numbering of the collection count?",
         "opts": [
             "Distinct teachings",
             "Units of recitation",
             "Chapters",
             "Speakers"],
         "correct": 1,
         "expl": "1,408 discourses in the Fours does not mean 1,408 different things to learn."},
        {"q": "Why does the guide say a page on this discourse must be partly about the text&rsquo;s history?",
         "opts": [
             "Because the content is disputed",
             "Because there is no third teaching here to find, and pretending otherwise would be a disservice",
             "Because the verses are unclear",
             "Because the Pāli is corrupt"],
         "correct": 1,
         "expl": "Honest reading has to say what is and is not new."},
        {"q": "What are the four, once more?",
         "opts": [
             "Greed, hatred, delusion, and fear of death",
             "Favoritism, hostility, stupidity, and cowardice",
             "Haste, partiality, silence, and pride",
             "Gain, honor, praise, and pleasure"],
         "correct": 1,
         "expl": "Partiality toward, partiality against, failure to understand, and fear of consequences."},
        {"q": "Why does the guide recommend memorizing the combined version?",
         "opts": [
             "It is shortest",
             "Because it carries both directions &mdash; a list held only in the negative becomes a list of accusations to make of others",
             "Because it has the best verses",
             "Because it is the oldest"],
         "correct": 1,
         "expl": "Held in both directions it stays usable on oneself."},
        {"q": "How does AN 4.20 complete the group?",
         "opts": [
             "By repeating the list a fourth time",
             "By applying the four to a named office, with hell and heaven rather than reputation as the consequences",
             "By refuting it",
             "By adding a fifth term"],
         "correct": 1,
         "expl": "An escalation worth watching."},
        {"q": "What shape is the group of four discourses arranged in?",
         "opts": [
             "From particular to general",
             "From the general to the particular &mdash; statement, mirror, combined form, concrete official",
             "Chronologically",
             "By length"],
         "correct": 1,
         "expl": "A common shape in this collection, and a good one for teaching."},
    ],
    marginalia=[
        ("Three arrangements", [
            "AN 4.17 &middot; negative",
            "AN 4.18 &middot; positive",
            "AN 4.19 &middot; both",
        ]),
        ("One month", [
            "waning",
            "waxing",
            "&mdash; adjacent, in eight lines",
        ]),
        ("What is counted", [
            "not distinct teachings",
            "units of recitation",
            "&mdash; and the seams show",
        ]),
        ("Cross-references", [
            "AN 4.17 &middot; the first form",
            "AN 4.18 &middot; the second",
            "AN 4.20 &middot; next: the office",
        ]),
    ],
    further=[
        '<a href="%s/an4.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.20.html">AN 4.20 &middot; A Meal Assigner</a> &mdash; next in this series, and '
        "the last discourse of the chapter.",
        '<a href="an-4.17.html">AN 4.17 &middot; Prejudice (1st)</a> &mdash; the first arrangement.',
        '<a href="an-4.18.html">AN 4.18 &middot; Prejudice (2nd)</a> &mdash; the second.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.20 — Bhattuddesakasutta
# --------------------------------------------------------------------------- #
page(
    20, "Bhattuddesaka", "A Meal Assigner",
    vagga=VAGGA_2,
    meta_title="AN 4.20 — A Meal Assigner | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bhattuddesakasutta — the "
        "four prejudices applied to the monk who assigns meals, with hell and heaven as the stated "
        "consequences and the assembly of the dregs. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_2),
        ("Speakers", SPEAKER),
        ("Form", "The four prejudices applied to one office, in both directions, with two verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Vinaya-adjacent material on monastic officers appears across the "
                              "Chinese Āgamas and Vinayas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, concrete, and much "
                       "sharper than the three discourses before it"),
    ],
    why=(
        "The chapter closes by taking the abstract list of four prejudices and handing it to one "
        "person with one job: the mendicant who decides which monk gets sent to which meal "
        "invitation. Do it by favoritism, hostility, stupidity, or cowardice and you are "
        "<em>placed in hell as if delivered there</em>. The escalation from AN 4.17&rsquo;s fading "
        "reputation to this is abrupt, and the reason for it is the office."),
    guide=[
        ("The teaching in one sentence", [
            "Whoever distributes what people need is the person for whom partiality carries the "
            "heaviest consequences."]),
        ("What a meal assigner did", [
            "<em>Bhattuddesaka</em> is a monastic officer appointed by the community. Lay donors "
            "would invite a number of monks to a meal; someone had to decide which monks went to "
            "which invitation. Since some invitations were far better than others, the office "
            "involved distributing a real and unequal good.",
            "The Vinaya lists a number of such appointed roles &mdash; assigners of lodgings, "
            "distributors of robe-cloth, storekeepers &mdash; and the qualification given for all of "
            "them is the same four negated. The list in AN 4.17&ndash;4.19 is not an abstract ethical "
            "principle that happens to be applied here; it is the standing job description for "
            "monastic office, and these discourses are where it is set out in teaching form."]),
        ("Why the consequence escalates", [
            "AN 4.17 said a prejudiced decider&rsquo;s fame wanes. This discourse says a prejudiced "
            "meal assigner is <em>placed in hell as if delivered there</em> &mdash; "
            "<em>yathābhataṁ nikkhitto evaṁ niraye</em>, an idiom of something set down exactly where "
            "it was carried to, without any further step required.",
            "The difference is not that the fault has changed. It is that the office has. The four "
            "prejudices are the same four; what has been added is a position in which acting on them "
            "harms specific people in a way they cannot avoid or appeal. Partiality in a private "
            "judgment costs the judge their reputation. Partiality in the distribution of food costs "
            "somebody their food.",
            "That is a coherent moral position and worth stating plainly: on this account "
            "responsibility scales with the power to allocate. The same disposition is a small fault "
            "in a person with nothing to give out and a very large one in the person holding the "
            "list."]),
        ("The dregs and the cream", [
            "The verses use a pair of images from liquid: <em>kasaṭa</em>, dregs or scum, and "
            "<em>maṇḍa</em>, the cream or clear top. An assembly whose members decide by the four "
            "prejudices is an assembly of the dregs; one whose members do not is an assembly of the "
            "cream.",
            "The shift from individual to assembly is significant. The prose judges one officer; the "
            "verse judges the whole body he belongs to. A community is characterized by how its "
            "appointed officers decide, which puts the responsibility for partiality on the group "
            "that tolerates it as well as on the individual who acts on it.",
            "&lsquo;That&rsquo;s what was said by the ascetic who knows&rsquo; closes both verses. "
            "The formula is unusual and marks the judgment as authoritative rather than "
            "observational."]),
        ("Reading it outside the monastery", [
            "The discourse transfers cleanly and is one of the more directly useful in the chapter. "
            "Anyone who assigns work, allocates budget, decides admissions, distributes shifts, or "
            "hands out anything scarce is a meal assigner in the relevant sense.",
            "The four questions come with it unchanged. Am I favoring someone because of my "
            "relationship to them? Am I penalizing someone over a grudge? Have I understood the case, "
            "or am I guessing? Am I deciding this way to avoid trouble for myself?",
            "The fourth is the one most often missed in institutional settings, because it disguises "
            "itself as prudence. A decision made to avoid a complaint, a difficult conversation, or a "
            "powerful person&rsquo;s displeasure is on this list, whatever else it is."]),
        ("Closing the chapter", [
            "The Caravagga began with a mendicant alone with a thought in four postures and ends with "
            "a mendicant holding a list and deciding who eats. Between them it has covered ethics, "
            "the four efforts, the four superlatives, and the four subtleties.",
            "It is a less unified chapter than the Bhaṇḍagāmavagga that precedes it, and the "
            "arrangement is partly numerical rather than thematic. But the movement from private "
            "discipline to public office is a real one, and the chapter reads well in that direction: "
            "what you do with an unnoticed thought and what you do with an unwatched decision are the "
            "same question asked at two scales."]),
    ],
    terms=[
        ("bhattuddesaka",
         "&ldquo;meal assigner&rdquo; &mdash; the monastic officer who decided which monks went to "
         "which meal invitation, distributing a real and unequal good."),
        ("yathābhataṁ nikkhitto",
         "&ldquo;placed as if delivered there&rdquo; &mdash; an idiom of something set down exactly "
         "where it was carried to, with no further step required."),
        ("kasaṭa",
         "&ldquo;dregs, scum&rdquo; &mdash; the verse&rsquo;s name for an assembly whose officers "
         "decide by the four prejudices."),
        ("maṇḍa",
         "&ldquo;cream, the clear top&rdquo; &mdash; the opposite image, for an assembly whose "
         "officers do not."),
        ("adhammika",
         "&ldquo;unprincipled&rdquo; &mdash; with no respect for principle; the verse&rsquo;s "
         "description of those led astray by the four."),
    ],
    text_intro=(
        "The discourse in full: the meal assigner in both directions, and the two verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Placed in hell"),
        ("p", "&sect;1", "an4.20:1.1-1.4"),
        ("h3", "Placed in heaven"),
        ("p", "&sect;2", "an4.20:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.20:3.1-4.1"),
        ("p", "&sect;4", "an4.20:4.2-4.6"),
    ],
    quiz=[
        {"q": "What did a meal assigner do?",
         "opts": [
             "Cook for the community",
             "Decide which monks went to which meal invitation &mdash; distributing a real and unequal good",
             "Collect alms",
             "Serve the senior monks"],
         "correct": 1,
         "expl": "An office appointed by the community."},
        {"q": "What is the stated consequence of doing it by the four prejudices?",
         "opts": [
             "A fading reputation",
             "Being placed in hell as if delivered there",
             "Loss of the office",
             "Rebirth as an animal"],
         "correct": 1,
         "expl": "An idiom of something set down exactly where it was carried to."},
        {"q": "Why does the consequence escalate from AN 4.17?",
         "opts": [
             "Because the fault is worse",
             "Because the office has changed &mdash; acting on the same four now harms specific people who cannot avoid or appeal it",
             "Because monastics are held to a higher standard",
             "Because the verses demand it"],
         "correct": 1,
         "expl": "Partiality in a private judgment costs the judge their reputation; in the distribution of food it costs somebody their food."},
        {"q": "What moral position does the guide draw from that?",
         "opts": [
             "That intention is irrelevant",
             "That responsibility scales with the power to allocate",
             "That officials should not be appointed",
             "That hell is a metaphor"],
         "correct": 1,
         "expl": "A small fault in a person with nothing to give out; a very large one in the person holding the list."},
        {"q": "How does the same list function in the Vinaya?",
         "opts": [
             "It does not appear there",
             "As the standing job description for monastic office &mdash; assigners of lodgings, distributors of robe-cloth, storekeepers",
             "As a penalty schedule",
             "As a confession formula"],
         "correct": 1,
         "expl": "These discourses set it out in teaching form."},
        {"q": "What are <em>kasaṭa</em> and <em>maṇḍa</em>?",
         "opts": [
             "Two monastic offices",
             "Dregs and cream &mdash; images for an assembly whose officers decide badly or well",
             "Two kinds of food",
             "Two verses"],
         "correct": 1,
         "expl": "A pair of images from liquid."},
        {"q": "Why is the shift from individual to assembly significant?",
         "opts": [
             "It softens the judgment",
             "Because a community is characterized by how its appointed officers decide &mdash; which puts responsibility on the group that tolerates partiality as well as the individual",
             "It changes the subject",
             "It applies only to large monasteries"],
         "correct": 1,
         "expl": "The prose judges one officer; the verse judges the body he belongs to."},
        {"q": "Who is a meal assigner outside the monastery?",
         "opts": [
             "Nobody; the discourse does not transfer",
             "Anyone who assigns work, allocates budget, decides admissions, distributes shifts, or hands out anything scarce",
             "Only ordained officials",
             "Only those who handle food"],
         "correct": 1,
         "expl": "The four questions come with it unchanged."},
        {"q": "Which of the four does the guide say is most often missed in institutions?",
         "opts": [
             "Favoritism",
             "Cowardice &mdash; because it disguises itself as prudence",
             "Hostility",
             "Stupidity"],
         "correct": 1,
         "expl": "A decision made to avoid a complaint or a powerful person&rsquo;s displeasure is on this list."},
        {"q": "How does the guide describe the chapter&rsquo;s movement?",
         "opts": [
             "From public office to private discipline",
             "From private discipline to public office &mdash; an unnoticed thought and an unwatched decision are the same question at two scales",
             "Chronological",
             "From short discourses to long ones"],
         "correct": 1,
         "expl": "The Caravagga begins with a thought in four postures and ends with a list of who eats."},
    ],
    marginalia=[
        ("The office", [
            "<span class=\"pali\">bhattuddesaka</span>meal assigner",
            "who goes to which invitation",
            "&mdash; an unequal good",
        ]),
        ("The escalation", [
            "AN 4.17 &middot; fame wanes",
            "AN 4.20 &middot; hell, as if delivered",
            "&mdash; the office, not the fault",
        ]),
        ("Two assemblies", [
            "<span class=\"pali\">kasaṭa</span>dregs",
            "<span class=\"pali\">maṇḍa</span>cream",
            "&mdash; the group, not the officer",
        ]),
        ("Cross-references", [
            "AN 4.17-19 &middot; the four, three ways",
            "AN 4.11 &middot; where the chapter began",
            "AN 4.55 &middot; further into the Fours",
        ]),
    ],
    further=[
        '<a href="%s/an4.20/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.19.html">AN 4.19 &middot; Prejudice (3rd)</a> &mdash; the combined form of the '
        "list this discourse applies.",
        '<a href="an-4.11.html">AN 4.11 &middot; Walking</a> &mdash; where the chapter began, with a '
        "thought in four postures.",
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; further into the Fours, on a '
        "married couple of matched conviction.",
    ],
)
