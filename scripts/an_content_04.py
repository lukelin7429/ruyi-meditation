# -*- coding: utf-8 -*-
"""Catukka Nipāta — The Fours. One discourse per page, from AN 4.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Catukka Nipāta — The Fours"
# The Fours follow the Threes. AN 4.13, 4.55, 4.62 and 4.170 were published
# before this series began working in order; they are listed in the index by
# INDEX_EXTRA and are not generated here. HEAD points at the last page the
# Threes module has reached and moves as that module advances.
HEAD = ("an-3.100.html", "AN 3.100 &middot; A Lump of Salt")
TAIL = ("an-4.62.html", "AN 4.62 &middot; Debtlessness")
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


# --------------------------------------------------------------------------- #
# Uruvelavagga — the third chapter of the Fours
# --------------------------------------------------------------------------- #
VAGGA_3 = "<em>Uruvelavagga</em> &mdash; the third chapter of the Fours"
SETTING_3 = ("None stated; the Uruvelavagga gives no location for this discourse, and it is "
             "addressed to the mendicants directly")


# --------------------------------------------------------------------------- #
# AN 4.21 — Paṭhamauruvelasutta
# --------------------------------------------------------------------------- #
page(
    21, "Paṭhamauruvela", "At Uruvelā (1st)",
    vagga=VAGGA_3,
    meta_title="AN 4.21 — At Uruvelā (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamauruvelasutta — "
        "newly awakened and with nobody left to revere, the Buddha resolves to honor the teaching "
        "itself, and Brahmā Sahampati confirms it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery &mdash; the "
                    "frame; the events recalled took place at Uruvelā, by the goatherd&rsquo;s "
                    "banyan on the Nerañjarā"),
        ("Speakers", "The Buddha, recalling his own thoughts, and Brahmā Sahampati"),
        ("Form", "A first-person recollection, a divine visitation, verses, and a closing "
                 "resolution"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The Gārava or Uruvelā episode is well represented in the Chinese "
                              "Āgamas and in SN 6.2; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; narrative and clear, with a "
                       "genuinely unusual problem at its center"),
    ],
    why=(
        "A problem nobody else can have. Newly awakened, the Buddha reflects that living without "
        "respect and reverence is living in suffering &mdash; and then looks for someone to revere "
        "and finds nobody in the world more accomplished than himself in ethics, immersion, wisdom, "
        "or freedom. The solution he reaches is the interesting part: he reveres the teaching he "
        "woke up to. Not himself, and not nothing."),
    guide=[
        ("The teaching in one sentence", [
            "Nobody should live without something above them, including the person with nobody above "
            "them &mdash; who therefore reveres the truth he found rather than the fact of having "
            "found it."]),
        ("The premise", [
            "<em>One without respect and reverence lives in suffering.</em> The claim is stated flatly "
            "and never argued for, here or elsewhere, and it is worth noticing how strong it is. Not "
            "that reverence is beneficial or conducive; that its absence is <em>dukkha</em>.",
            "The tradition takes this as a fact about minds rather than a social rule. A person with "
            "nothing they hold above themselves has no correction available to them and nothing to "
            "measure by, and the resulting condition is described not as arrogance but as suffering. "
            "That is a diagnosis, and it is one that transfers well outside its original setting."]),
        ("The search, and its result", [
            "The four things searched for are the four of AN 4.1: ethics, immersion, wisdom, freedom. "
            "The chapter that opened the Fours supplies the list this discourse runs down.",
            "The phrasing of the search is careful. He would honor another ascetic or brahmin "
            "<em>so as to complete the entire spectrum</em> of each, if it were incomplete &mdash; "
            "the conditional is real, not rhetorical. The search is for a teacher who could finish "
            "something unfinished, and it fails because there is nothing unfinished.",
            "Read charitably, this is not a claim of superiority so much as a report of a structural "
            "problem. The mechanism by which people improve is finding someone further along. Someone "
            "at the end of the road cannot use that mechanism, and the discourse treats that as a "
            "difficulty to be solved rather than as a privilege to be enjoyed."]),
        ("Revering the Dhamma", [
            "<em>Why don&rsquo;t I honor and respect and rely on the same teaching to which I was "
            "awakened?</em> The solution separates the teaching from the teacher, and it separates it "
            "from the awakening too.",
            "The consequences of that separation run through the whole tradition. The Dhamma is not "
            "the Buddha&rsquo;s possession or invention; he is described as having found it, which is "
            "why it can stand above him. It is also why the tradition can survive his death without "
            "an appointed successor &mdash; the thing to be revered was never the person.",
            "This is the discourse that grounds the standard formula about respecting the teaching, "
            "and it is worth teaching whenever the relationship between a tradition and its founder "
            "comes up. The founder here is depicted as a subordinate of what he taught."]),
        ("Sahampati&rsquo;s part", [
            "Brahmā Sahampati appears, folds his hands, and confirms: all Buddhas past, future, and "
            "present honor this same teaching. He is the same divinity who, in the better-known "
            "episode, persuades the newly awakened Buddha to teach at all.",
            "Two things are worth saying about his role. Narratively, the confirmation makes the "
            "resolution a pattern rather than an improvisation &mdash; this is what Buddhas do, not "
            "what this one decided. And structurally, it is notable that the highest deity in the "
            "cosmology appears in order to endorse the Dhamma&rsquo;s superiority to Buddhas. The "
            "story arranges every available authority to point at the same place.",
            "Whether one reads Sahampati as a real being, as a personification of the "
            "Buddha&rsquo;s own reflection, or as narrative convention, the discourse works. It does "
            "not depend on the reader settling that question, and a teaching guide should not settle "
            "it for them."]),
        ("The last line", [
            "<em>And since the Saṅgha has also achieved greatness, I also respect the Saṅgha.</em> "
            "The sentence is appended almost casually and does a great deal of work.",
            "It is transparently later in origin than the rest &mdash; at the moment recalled, "
            "immediately after the awakening, there was no Saṅgha. So the closing line speaks from "
            "the time of the telling rather than the time of the events, and it extends the "
            "principle: the community, once it exists and has come to something, joins what is "
            "revered.",
            "That is honest to point out rather than to hide. It also gives the discourse its final "
            "shape: a teacher who reveres what he taught, and then the people who have realized it."]),
    ],
    terms=[
        ("gārava",
         "&ldquo;respect, reverence&rdquo; &mdash; the quality whose absence is said flatly to be a "
         "life of suffering."),
        ("Uruvelā",
         "the place of the awakening, on the bank of the Nerañjarā, where the events recalled here "
         "took place at the goatherd&rsquo;s banyan tree."),
        ("Sahampati",
         "the Brahmā who appears to confirm the resolution &mdash; the same divinity who elsewhere "
         "persuades the Buddha to teach."),
        ("sīlakkhandha",
         "&ldquo;the spectrum of ethics&rdquo; &mdash; literally the mass or aggregate of it. The "
         "search is for someone who could complete it, if it were incomplete."),
        ("saddhamma",
         "&ldquo;the true teaching&rdquo; &mdash; what the verses say all Buddhas respect, and what "
         "stands above the one who found it."),
    ],
    text_intro=(
        "The discourse in full: the recollection, the search, the resolution, Sahampati&rsquo;s "
        "confirmation and verses, and the closing line. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "an4.21:1.1-1.6"),
        ("h3", "One without reverence lives in suffering"),
        ("p", "&sect;2", "an4.21:2.1-2.4"),
        ("h3", "The search"),
        ("p", "&sect;3", "an4.21:3.1-6.2"),
        ("h3", "The resolution"),
        ("p", "&sect;4", "an4.21:7.1-7.2"),
        ("h3", "Sahampati"),
        ("p", "&sect;5", "an4.21:8.1-8.8"),
        ("p", "&sect;6", "an4.21:9.1-11.4"),
        ("p", "&sect;7", "an4.21:12.1-12.4"),
    ],
    quiz=[
        {"q": "What claim does the Buddha&rsquo;s reflection open with?",
         "opts": [
             "That teachers are necessary for the path",
             "That one without respect and reverence lives in suffering",
             "That awakening ends all need for others",
             "That brahmins deserve respect"],
         "correct": 1,
         "expl": "Stated flatly and never argued for."},
        {"q": "What does he search for, and in what four areas?",
         "opts": [
             "A successor, in body, speech, mind, and livelihood",
             "Someone to revere, more accomplished than himself in ethics, immersion, wisdom, or freedom",
             "A monastery, in each of the four directions",
             "A disciple, among gods, Māras, ascetics, and brahmins"],
         "correct": 1,
         "expl": "The four of AN 4.1, which opened the collection&rsquo;s Fours."},
        {"q": "How does the guide read the failure of that search?",
         "opts": [
             "As a claim of superiority to be enjoyed",
             "As a structural problem &mdash; the mechanism by which people improve is finding someone further along, and someone at the end of the road cannot use it",
             "As a later addition",
             "As modesty"],
         "correct": 1,
         "expl": "The discourse treats it as a difficulty to be solved."},
        {"q": "What is the resolution?",
         "opts": [
             "To revere himself",
             "To honor and respect and rely on the same teaching to which he was awakened",
             "To revere nothing",
             "To wait for another Buddha"],
         "correct": 1,
         "expl": "Not himself, and not nothing."},
        {"q": "Why can the Dhamma stand above the Buddha?",
         "opts": [
             "Because it is older than he is in every sense",
             "Because it is not his possession or invention &mdash; he is described as having found it",
             "Because deities decreed it",
             "Because he was not fully awakened yet"],
         "correct": 1,
         "expl": "Which is also why the tradition can survive his death without an appointed successor."},
        {"q": "Who is Sahampati?",
         "opts": [
             "A senior monk",
             "The Brahmā who confirms the resolution, and who elsewhere persuades the Buddha to teach",
             "A wanderer",
             "A king"],
         "correct": 1,
         "expl": "The highest deity in the cosmology, appearing to endorse the Dhamma&rsquo;s superiority to Buddhas."},
        {"q": "What does his confirmation accomplish narratively?",
         "opts": [
             "It corrects the Buddha",
             "It makes the resolution a pattern rather than an improvisation &mdash; this is what Buddhas do",
             "It introduces a new teaching",
             "It delays the decision"],
         "correct": 1,
         "expl": "Past, future, and present Buddhas alike."},
        {"q": "How does the guide treat the question of whether Sahampati is a real being?",
         "opts": [
             "It settles it in favor of literal reading",
             "It leaves it open &mdash; the discourse works on any of the readings, and a teaching guide should not settle it for the reader",
             "It rejects the episode as fiction",
             "It does not raise the question"],
         "correct": 1,
         "expl": "The discourse does not depend on the reader settling it."},
        {"q": "What is unusual about the closing line on the Saṅgha?",
         "opts": [
             "Nothing",
             "At the moment recalled there was no Saṅgha &mdash; so the line speaks from the time of the telling rather than the time of the events",
             "It contradicts the resolution",
             "It is in verse"],
         "correct": 1,
         "expl": "Honest to point out rather than to hide."},
        {"q": "Where did the events recalled take place?",
         "opts": [
             "Sāvatthī, in Jeta&rsquo;s Grove",
             "Uruvelā, at the goatherd&rsquo;s banyan tree on the bank of the Nerañjarā",
             "Rājagaha, on Vulture&rsquo;s Peak",
             "Sāketa, at Kāḷaka&rsquo;s monastery"],
         "correct": 1,
         "expl": "Sāvatthī is the frame in which the recollection is told."},
    ],
    marginalia=[
        ("The problem", [
            "no reverence &rarr; suffering",
            "nobody further along",
            "&mdash; and it is a problem",
        ]),
        ("The solution", [
            "revere the teaching",
            "not the teacher",
            "not the awakening",
        ]),
        ("Sahampati", [
            "all Buddhas past",
            "all Buddhas future",
            "&mdash; a pattern, not a choice",
        ]),
        ("Cross-references", [
            "AN 4.1 &middot; the four searched for",
            "AN 4.22 &middot; next: what makes a senior",
            "AN 4.23 &middot; the world as he knows it",
        ]),
    ],
    further=[
        '<a href="%s/an4.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.22.html">AN 4.22 &middot; At Uruvelā (2nd)</a> &mdash; next in this series, '
        "the second recollection from the same place.",
        '<a href="an-4.1.html">AN 4.1 &middot; Understood</a> &mdash; where the four items of the '
        "search are set out.",
        '<a href="an-4.23.html">AN 4.23 &middot; The World</a> &mdash; the chapter&rsquo;s fullest '
        "statement of what a Realized One is.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.22 — Dutiyauruvelasutta
# --------------------------------------------------------------------------- #
page(
    22, "Dutiyauruvela", "At Uruvelā (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 4.22 — At Uruvelā (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyauruvelasutta — old "
        "brahmins complain that the Buddha does not rise for his elders, and he redefines seniority "
        "by four qualities rather than by years. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Recalled from Uruvelā, at the goatherd&rsquo;s banyan on the Nerañjarā, when "
                    "the Buddha was newly awakened"),
        ("Speakers", "The Buddha, recalling the visit, and several elderly brahmins"),
        ("Form", "A complaint, a private reflection, two contrasting figures, four qualities, and "
                 "four verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The childish-elder and true-elder contrast recurs across the Chinese "
                              "Āgamas and the Dhammapada; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear argument with a sharp "
                       "edge on it"),
    ],
    why=(
        "Old brahmins arrive with a grievance: the ascetic Gotama does not bow to his elders, does "
        "not rise for them, does not offer them a seat, and this is not appropriate. His reply is "
        "not a defense of his manners. It is a redefinition of what an elder is &mdash; and the "
        "criterion he substitutes is one that a young person can meet and a hundred-year-old can "
        "fail."),
    guide=[
        ("The teaching in one sentence", [
            "Seniority is not conferred by age; it is constituted by speech, conduct, and attainment, "
            "and it can be held by the young and lacked by the old."]),
        ("The complaint", [
            "The brahmins are courteous. They exchange greetings, sit to one side, report what they "
            "have heard, confirm it is true, and then say plainly: this is not appropriate. It is a "
            "reasonable social complaint from a culture in which age was the ranking principle.",
            "It is worth honoring the force of it before reading the reply. Rising for one&rsquo;s "
            "elders is not a trivial custom; it is the visible form of a whole theory of authority. "
            "The visitors are not being petty. They are pointing out that the new teacher does not "
            "acknowledge the order of things."]),
        ("The reply, and what it does not do", [
            "The Buddha&rsquo;s reflection is: <em>These venerables don&rsquo;t know what a senior "
            "is, or what qualities make you a senior.</em> He does not deny the practice, apologize "
            "for it, or explain it as an oversight. He rejects the premise.",
            "Notice also what he does not do: he does not argue that respect is unnecessary. AN 4.21, "
            "the discourse immediately before, has just established that living without reverence is "
            "suffering. The two are consistent, and reading them in order shows why. Reverence is "
            "required; the question is what earns it, and the answer is not duration."]),
        ("The childish senior and the astute senior", [
            "The pair is drawn with deliberate exaggeration. Eighty, ninety, or a hundred years old, "
            "but speaking untimely, false, meaningless things against the teaching &mdash; that is a "
            "<em>childish senior</em> (<em>bāla thera</em>), a contradiction held together as a "
            "phrase. Young, black-haired, in the prime of life, but speaking what is timely, true, "
            "meaningful, and in line with the teaching &mdash; that is an <em>astute senior</em>.",
            "The criterion in both cases is speech, and the same five-part test is used positively "
            "and negatively: timely, true, meaningful, in line with the teaching, and beneficial. "
            "That is the canon&rsquo;s standard analysis of right speech, applied here as a "
            "qualification for rank.",
            "There is a real proposal in this. Authority is to be assigned by what a person says "
            "under examination, which is a testable criterion, rather than by when they were born, "
            "which is not a criterion at all but a fact."]),
        ("The four qualities", [
            "The formal answer is four: ethical conduct with the monastic code, extensive learning "
            "with the teachings memorized and penetrated, the four absorptions attainable at will, "
            "and the ending of defilements realized in this life.",
            "This is a much higher bar than the speech test, and the two halves of the discourse "
            "should not be blurred together. The speech test distinguishes a foolish old man from a "
            "sensible young one. The four qualities describe an arahant with jhāna and learning "
            "&mdash; and by that standard almost nobody is a senior.",
            "The gap is instructive rather than contradictory. The discourse gives a usable rule of "
            "thumb and a full definition in the same breath, which is characteristic of the "
            "collection. The rule of thumb is what one applies in a room; the definition is what the "
            "word actually means."]),
        ("Where the verses land", [
            "The verses drop the age question entirely and end somewhere else: <em>That&rsquo;s who I "
            "call a senior, who has no defilements. With the ending of defilements, a mendicant is "
            "declared a &lsquo;senior&rsquo;.</em>",
            "So the final word goes to the strict definition, not the rule of thumb. That is worth "
            "noticing for anyone tempted to use this discourse to dismiss the elderly: its own "
            "conclusion sets the bar at arahantship, which excludes the young and confident as "
            "comprehensively as it excludes the old and foolish.",
            "Read whole, the discourse replaces one unearned criterion with an earned one, and then "
            "makes the earned one demanding enough that very few people qualify under either. That is "
            "a more careful position than the opening exchange suggests."]),
    ],
    terms=[
        ("thera",
         "&ldquo;senior, elder&rdquo; &mdash; the word in dispute. In ordinary usage it meant age; "
         "the discourse reassigns it to qualities."),
        ("bāla thera",
         "&ldquo;childish senior&rdquo; &mdash; a contradiction held together as a phrase, for the "
         "old person whose speech fails the test."),
        ("kālavādī saccavādī",
         "&ldquo;speaking at the right time, speaking truth&rdquo; &mdash; the first two of the five "
         "marks of right speech used here as a qualification for rank."),
        ("jhāna",
         "&ldquo;absorption&rdquo; &mdash; the four, attainable when wanted without trouble or "
         "difficulty, are the third of the four qualities."),
        ("āsavakkhaya",
         "&ldquo;the ending of defilements&rdquo; &mdash; the fourth quality, and where the verses "
         "set the final bar."),
    ],
    text_intro=(
        "The discourse in full: the brahmins&rsquo; complaint, the two figures, the four qualities, "
        "and the verses. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The brahmins&rsquo; complaint"),
        ("p", "&sect;1", "an4.22:1.1-1.8"),
        ("h3", "The childish senior"),
        ("p", "&sect;2", "an4.22:2.1-2.5"),
        ("h3", "The astute senior"),
        ("p", "&sect;3", "an4.22:3.1-3.3"),
        ("h3", "Four qualities that make a senior"),
        ("p", "&sect;4", "an4.22:4.1-4.7"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.22:5.1-5.6"),
        ("p", "&sect;6", "an4.22:6.1-6.4"),
        ("p", "&sect;7", "an4.22:7.1-7.4"),
        ("p", "&sect;8", "an4.22:8.1-8.4"),
    ],
    quiz=[
        {"q": "What is the brahmins&rsquo; complaint?",
         "opts": [
             "That the Buddha teaches in the vernacular",
             "That he does not bow to elderly brahmins, rise in their presence, or offer them a seat",
             "That he accepts alms from anyone",
             "That he ordains the young"],
         "correct": 1,
         "expl": "A reasonable social complaint in a culture where age was the ranking principle."},
        {"q": "How does the guide characterize the complaint before the reply?",
         "opts": [
             "As petty",
             "As reasonable &mdash; rising for one&rsquo;s elders is the visible form of a whole theory of authority",
             "As dishonest",
             "As a test"],
         "correct": 1,
         "expl": "They are pointing out that the new teacher does not acknowledge the order of things."},
        {"q": "What is the Buddha&rsquo;s response?",
         "opts": [
             "An apology",
             "A rejection of the premise &mdash; they do not know what a senior is",
             "An explanation of monastic custom",
             "Silence"],
         "correct": 1,
         "expl": "He does not deny the practice or defend his manners."},
        {"q": "How is this consistent with AN 4.21?",
         "opts": [
             "It is not",
             "AN 4.21 requires reverence; this discourse asks what earns it, and answers that duration does not",
             "AN 4.21 applies only to Buddhas",
             "The two address different audiences"],
         "correct": 1,
         "expl": "Reading them in order shows why."},
        {"q": "What is a &lsquo;childish senior&rsquo;?",
         "opts": [
             "A novice",
             "Someone eighty, ninety, or a hundred whose speech is untimely, false, meaningless, and against the teaching",
             "A young monk with a senior&rsquo;s title",
             "A layman"],
         "correct": 1,
         "expl": "A contradiction held together as a phrase."},
        {"q": "What criterion distinguishes the two figures?",
         "opts": [
             "Attainment",
             "Speech &mdash; timely, true, meaningful, in line with the teaching, and beneficial",
             "Ordination date",
             "Learning"],
         "correct": 1,
         "expl": "The canon&rsquo;s standard analysis of right speech, applied as a qualification for rank."},
        {"q": "Why does the guide call that a real proposal?",
         "opts": [
             "Because it is easy to apply",
             "Because authority is assigned by what a person says under examination &mdash; a testable criterion rather than a fact about birth",
             "Because it favors the young",
             "Because it matches brahminical custom"],
         "correct": 1,
         "expl": "When one was born is not a criterion at all."},
        {"q": "What are the four qualities that formally make a senior?",
         "opts": [
             "Age, learning, ordination, and reputation",
             "Ethical conduct with the code, extensive learning penetrated, the four absorptions at will, and the ending of defilements",
             "Contentment, good will, mindfulness, and immersion",
             "Faith, energy, mindfulness, and wisdom"],
         "correct": 1,
         "expl": "A much higher bar than the speech test."},
        {"q": "How does the guide relate the speech test and the four qualities?",
         "opts": [
             "As a contradiction",
             "As a usable rule of thumb and a full definition given in the same breath &mdash; one applies in a room, the other says what the word means",
             "As two competing traditions",
             "As monastic and lay standards"],
         "correct": 1,
         "expl": "Characteristic of the collection."},
        {"q": "Where do the verses set the final bar?",
         "opts": [
             "At right speech",
             "At the ending of defilements &mdash; which excludes the young and confident as comprehensively as the old and foolish",
             "At sixty years of age",
             "At ten years of ordination"],
         "correct": 1,
         "expl": "A more careful position than the opening exchange suggests."},
    ],
    marginalia=[
        ("The complaint", [
            "does not bow",
            "does not rise",
            "offers no seat",
        ]),
        ("Two figures", [
            "a hundred years &middot; childish",
            "black-haired &middot; astute",
            "&mdash; the test is speech",
        ]),
        ("The four", [
            "ethical, in the code",
            "learned and penetrating",
            "the four absorptions at will",
            "defilements ended",
        ]),
        ("Cross-references", [
            "AN 4.21 &middot; reverence required",
            "AN 4.23 &middot; next: the Realized One",
            "AN 4.6 &middot; learning and its point",
        ]),
    ],
    further=[
        '<a href="%s/an4.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.23.html">AN 4.23 &middot; The World</a> &mdash; next in this series.',
        '<a href="an-4.21.html">AN 4.21 &middot; At Uruvelā (1st)</a> &mdash; where reverence is '
        "established as necessary.",
        '<a href="an-4.6.html">AN 4.6 &middot; A Little Learning</a> &mdash; the other discourse of '
        "the Fours on qualification without attainment.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.23 — Lokasutta
# --------------------------------------------------------------------------- #
page(
    23, "Loka", "The World",
    vagga=VAGGA_3,
    meta_title="AN 4.23 — The World | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Lokasutta — the world, its "
        "origin, cessation, and the practice leading there, all understood by the Realized One, and "
        "four reasons the title is given. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_3),
        ("Speakers", SPEAKER),
        ("Form", "A fourfold understanding, four explanations of a title, and seven verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "This discourse corresponds closely to material at Itivuttaka 112 and "
                              "has counterparts in the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the etymological play in it needs "
                       "explaining, and the verses are the most exalted in the chapter"),
    ],
    why=(
        "The four noble truths, with &lsquo;the world&rsquo; where &lsquo;suffering&rsquo; usually "
        "stands. Understood, given up, realized, developed &mdash; the same four verbs, applied to "
        "the world and its origin and cessation and path. And then four separate explanations of "
        "why the title <em>tathāgata</em> is given, which together form the fullest short statement "
        "in the collection of what that word is supposed to mean."),
    guide=[
        ("The teaching in one sentence", [
            "The world is the first noble truth under another name, and the one who has completed all "
            "four tasks in respect of it is what &lsquo;Realized One&rsquo; means."]),
        ("The world as the first truth", [
            "The opening paragraph runs the four-truth structure exactly: the world understood, its "
            "origin given up, its cessation realized, the practice leading to its cessation "
            "developed. Each truth has its own verb, and those four verbs are the standard set.",
            "Substituting &lsquo;world&rsquo; for &lsquo;suffering&rsquo; is not a casual variation. "
            "Elsewhere the canon defines the world in terms of the six senses &mdash; the world is "
            "where there is seeing, hearing, and the rest &mdash; which makes the substitution "
            "precise rather than poetic. The world in question is the experienced world, and it is "
            "coextensive with the first truth.",
            "Note also the second clause of the first line: the world has been understood, "
            "<em>and he is detached from it</em>. Understanding and detachment are stated as separate "
            "achievements throughout, which keeps the discourse from collapsing into intellectualism."]),
        ("Four reasons for the title", [
            "The discourse gives four explanations of why the Realized One is called the Realized "
            "One, and they are of different kinds: he has understood everything seen, heard, thought, "
            "and known in the whole world; everything he says between awakening and final "
            "extinguishment is real and not otherwise; he does as he says and says as he does; and "
            "he is the vanquisher, the unvanquished, the universal seer, the wielder of power.",
            "Knowledge, truthfulness, consistency, and mastery. The second and third are the ones "
            "worth dwelling on, because they are the only claims on the list that a listener could in "
            "principle test. That everything a teacher says is true is checkable over time; that they "
            "do what they say is checkable immediately."]),
        ("The word itself", [
            "<em>Tathāgata</em> is a compound of <em>tathā</em>, &lsquo;thus, in that way, so&rsquo;, "
            "with either <em>āgata</em>, come, or <em>gata</em>, gone. The tradition has never settled "
            "which, and both readings are ancient: thus-come and thus-gone.",
            "This discourse plays on the <em>tathā</em> element rather than on the motion verb. "
            "Everything he says is <em>tathā</em>, so; he does as he says. The title on this reading "
            "means something like &lsquo;the one who is so&rsquo;, the one in whom word, deed, and "
            "fact do not come apart. Sujato&rsquo;s &lsquo;Realized One&rsquo; catches that sense.",
            "It is worth telling students that the ambiguity is real and old, and that no reading is "
            "the settled correct one. A term the tradition uses constantly and has never fully "
            "resolved is a useful thing for a student to know about early on."]),
        ("The verses", [
            "Seven verses, and they are the most exalted language in the chapter: the champion "
            "released from all ties, the supreme lion, turning the divine wheel, with no rival in the "
            "world with its gods.",
            "The fourth-to-last verse is the one to hold: <em>Tamed, he is the best of tamers; "
            "peaceful, he is the seer among the peaceful; liberated, he is the foremost of "
            "liberators; crossed over, he is the most excellent of guides across.</em> Each line has "
            "the same structure &mdash; a state achieved, then the corresponding role toward others.",
            "That structure is the discourse&rsquo;s answer to a question it never asks aloud: what "
            "qualifies someone to teach? Nothing but having done the thing. One does not become a "
            "guide across by studying the crossing."]),
        ("Reading an acclamatory text", [
            "This is a devotional discourse, and it is more useful to say so than to pretend "
            "otherwise. It offers no argument, invites no examination, and asks the listener to "
            "revere. AN 4.24, the next discourse, will take the same subject and handle it with "
            "great analytic care; the contrast between the two is one of the more striking in the "
            "chapter.",
            "For a reader who finds the register difficult, the two testable claims are the place to "
            "stand: he says what is so, and he does what he says. Everything else in the discourse "
            "follows from those or is beyond checking, and the discourse itself puts them in the "
            "middle of the list."]),
    ],
    terms=[
        ("tathāgata",
         "&ldquo;Realized One&rdquo; &mdash; <em>tathā</em> plus either <em>āgata</em> or "
         "<em>gata</em>; thus-come or thus-gone. The ambiguity is ancient and unresolved."),
        ("loka",
         "&ldquo;world&rdquo; &mdash; defined elsewhere in the canon by the six senses, which makes "
         "its substitution for &lsquo;suffering&rsquo; here precise rather than poetic."),
        ("visaṁyutta",
         "&ldquo;detached, unyoked&rdquo; &mdash; the second clause of the first line. Understanding "
         "and detachment are stated as separate achievements."),
        ("anuttara",
         "&ldquo;unvanquished, unsurpassed&rdquo; &mdash; one of the four titles in the last "
         "explanation, alongside vanquisher, universal seer, and wielder of power."),
        ("dantānaṁ danto",
         "&ldquo;tamed, the best of tamers&rdquo; &mdash; the pattern of the verse: a state achieved, "
         "then the corresponding role toward others."),
    ],
    text_intro=(
        "The discourse in full: the fourfold understanding, the four explanations of the title, and "
        "the verses. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The world and its cessation"),
        ("p", "&sect;1", "an4.23:1.1-1.8"),
        ("h3", "Why he is called the Realized One"),
        ("p", "&sect;2", "an4.23:2.1-2.2"),
        ("p", "&sect;3", "an4.23:3.1-3.2"),
        ("p", "&sect;4", "an4.23:4.1-4.3"),
        ("p", "&sect;5", "an4.23:5.1-5.2"),
        ("h3", "The verses"),
        ("p", "&sect;6", "an4.23:6.1-7.4"),
        ("p", "&sect;7", "an4.23:8.1-9.4"),
        ("p", "&sect;8", "an4.23:10.1-12.4"),
    ],
    quiz=[
        {"q": "What structure does the opening paragraph follow?",
         "opts": [
             "The four postures",
             "The four noble truths, with &lsquo;the world&rsquo; where &lsquo;suffering&rsquo; usually stands",
             "The four right efforts",
             "The four assurances"],
         "correct": 1,
         "expl": "Understood, given up, realized, developed &mdash; each truth with its own verb."},
        {"q": "Why is that substitution precise rather than poetic?",
         "opts": [
             "Because the world is impermanent",
             "Because the canon elsewhere defines the world in terms of the six senses, making it coextensive with the first truth",
             "Because Sujato chose the word",
             "Because the verses require it"],
         "correct": 1,
         "expl": "The world in question is the experienced world."},
        {"q": "What is stated alongside &lsquo;the world has been understood&rsquo;?",
         "opts": [
             "That it will end",
             "That he is detached from it &mdash; understanding and detachment as separate achievements",
             "That others cannot understand it",
             "That it is unreal"],
         "correct": 1,
         "expl": "Which keeps the discourse from collapsing into intellectualism."},
        {"q": "What are the four reasons given for the title?",
         "opts": [
             "Birth, awakening, teaching, and extinguishment",
             "Knowledge of all that is seen and known, truthfulness of all he says, doing as he says, and mastery",
             "Ethics, immersion, wisdom, and freedom",
             "The four assurances"],
         "correct": 1,
         "expl": "Four explanations of different kinds."},
        {"q": "Which two of the four could a listener in principle test?",
         "opts": [
             "The first and fourth",
             "The second and third &mdash; that everything he says is true, and that he does as he says",
             "None of them",
             "All four"],
         "correct": 1,
         "expl": "One is checkable over time, the other immediately."},
        {"q": "What does <em>tathāgata</em> combine?",
         "opts": [
             "&lsquo;Truth&rsquo; and &lsquo;teacher&rsquo;",
             "<em>Tathā</em>, thus or so, with either <em>āgata</em>, come, or <em>gata</em>, gone",
             "&lsquo;World&rsquo; and &lsquo;knower&rsquo;",
             "&lsquo;Awakened&rsquo; and &lsquo;one&rsquo;"],
         "correct": 1,
         "expl": "Thus-come and thus-gone; the tradition has never settled which."},
        {"q": "Which element does this discourse play on?",
         "opts": [
             "The motion verb",
             "The <em>tathā</em> element &mdash; the one in whom word, deed, and fact do not come apart",
             "Neither",
             "The prefix"],
         "correct": 1,
         "expl": "Which is what Sujato&rsquo;s &lsquo;Realized One&rsquo; catches."},
        {"q": "What structure does the &lsquo;tamed, best of tamers&rsquo; verse use?",
         "opts": [
             "A simile in each line",
             "A state achieved, then the corresponding role toward others",
             "A question and answer",
             "A negation followed by an affirmation"],
         "correct": 1,
         "expl": "Tamed, peaceful, liberated, crossed over &mdash; each with its role."},
        {"q": "What question does that verse answer without asking it?",
         "opts": [
             "Why the Buddha taught",
             "What qualifies someone to teach &mdash; nothing but having done the thing",
             "How long the path takes",
             "Who may be ordained"],
         "correct": 1,
         "expl": "One does not become a guide across by studying the crossing."},
        {"q": "How does the guide characterize this discourse&rsquo;s register?",
         "opts": [
             "Analytic",
             "Devotional &mdash; it offers no argument and invites no examination, in contrast to AN 4.24 which follows",
             "Polemical",
             "Narrative"],
         "correct": 1,
         "expl": "More useful to say so than to pretend otherwise."},
    ],
    marginalia=[
        ("Four truths, one word", [
            "the world &mdash; understood",
            "its origin &mdash; given up",
            "its cessation &mdash; realized",
            "the practice &mdash; developed",
        ]),
        ("Four titles", [
            "knowledge",
            "truthfulness",
            "consistency",
            "mastery",
        ]),
        ("The verse to hold", [
            "tamed &rarr; best of tamers",
            "crossed &rarr; guide across",
            "&mdash; the state, then the role",
        ]),
        ("Cross-references", [
            "AN 4.24 &middot; next: the same subject, analytically",
            "AN 4.8 &middot; the four assurances",
            "AN 4.22 &middot; what qualifies a senior",
        ]),
    ],
    further=[
        '<a href="%s/an4.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.24.html">AN 4.24 &middot; At Kāḷaka&rsquo;s Monastery</a> &mdash; next in this '
        "series, and the analytic counterpart to this one.",
        '<a href="an-4.8.html">AN 4.8 &middot; Self-assured</a> &mdash; the other statement of what '
        "cannot be charged against a Realized One.",
        '<a href="an-4.21.html">AN 4.21 &middot; At Uruvelā (1st)</a> &mdash; on what a Buddha '
        "reveres.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.24 — Kāḷakārāmasutta
# --------------------------------------------------------------------------- #
page(
    24, "Kāḷakārāma", "At Kāḷaka&rsquo;s Monastery",
    vagga=VAGGA_3,
    meta_title="AN 4.24 — At Kāḷaka&rsquo;s Monastery | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kāḷakārāmasutta — the "
        "Realized One knows all that is seen, heard, thought, and known, and conceives nothing about "
        "it: not the seen, not the unseen, not a seer. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāketa, in Kāḷaka&rsquo;s monastery"),
        ("Speakers", SPEAKER),
        ("Form", "A claim, three rejected reformulations, a fourfold analysis, and two verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The four-cornered denial and the seen-heard-thought-known set are "
                              "widespread across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the most philosophically "
                       "demanding discourse of the chapter, and worth the work"),
    ],
    why=(
        "AN 4.23 said the Realized One knows everything in the world and left it there. This "
        "discourse says the same thing and then spends the rest of itself preventing the obvious "
        "misunderstanding. He knows what is to be known &mdash; and does not conceive what is known, "
        "does not conceive what is unknown, does not conceive what is to be known, and does not "
        "conceive a knower. Four negations, and the last one is the one that matters."),
    guide=[
        ("The teaching in one sentence", [
            "Complete knowledge of everything experienced is compatible with taking up no position "
            "about it at all &mdash; including no position about there being someone who knows."]),
        ("The four-cornered denial", [
            "Before the main argument the discourse clears three alternatives. To say &lsquo;I do not "
            "know&rsquo; would be a lie. To say &lsquo;I both know and do not know&rsquo; would be "
            "just the same. To say &lsquo;I neither know nor do not know&rsquo; would be a fault.",
            "This is the <em>catuṣkoṭi</em>, the four-cornered logic familiar from Indian debate: "
            "affirm, deny, both, neither. The discourse works through the last three and rules them "
            "out, leaving the first, which it has already asserted.",
            "The move is worth naming because the same structure is more often used in Buddhist texts "
            "to reject all four corners. Here it does the opposite: it defends a plain positive "
            "claim by eliminating the evasions. Whatever else the Realized One is, he is not being "
            "coy about whether he knows."]),
        ("The formula, four times", [
            "Then the central passage, run through sight, hearing, thought, and knowledge. Taking "
            "sight: he sees what is to be seen; he does not conceive the seen; does not conceive the "
            "unseen; does not conceive what is to be seen; does not conceive a seer.",
            "<em>Maññati</em>, &lsquo;conceives&rsquo;, is a technical term of the first importance "
            "in this literature. It means to imagine, to suppose, to construct a notion about "
            "something &mdash; and specifically to construct it in relation to a self. The discourse "
            "is not saying he has no thoughts about what he sees. It is saying he builds nothing on "
            "the seeing.",
            "The first three negations remove the object in its three tenses: what has been seen, "
            "what has not been, what will be. The fourth removes the subject. A reader who tracks "
            "only the first three will hear a discourse about not clinging to experiences; the fourth "
            "makes it a discourse about there being no experiencer to do the clinging."]),
        ("&lsquo;Unaffected&rsquo;", [
            "<em>Tādī</em>, translated here as &lsquo;the unaffected one&rsquo;, is one of the "
            "canon&rsquo;s highest terms &mdash; literally &lsquo;such&rsquo;, the one who is thus, "
            "unchanged by circumstance. It is from the same <em>tathā</em> family as "
            "<em>tathāgata</em> in AN 4.23, and the two discourses are quietly linked by it.",
            "The discourse says: since a Realized One is unaffected in the midst of things that ought "
            "to be seen, heard, thought, and known, he is the unaffected one. And then: <em>I say "
            "that there is no better or finer poise than this.</em>",
            "That superlative is the discourse&rsquo;s claim about value, and it should be read "
            "against AN 4.16 on subtlety, where the criterion was also that nothing better or finer "
            "is seen or aimed at. The same phrase marks the endpoint in both."]),
        ("The dart", [
            "The closing verse gives the image the discourse is remembered for. Others get attached "
            "and think it is the truth, limited by their preconceptions; the Realized Ones have seen "
            "<em>this dart</em> to which people cling &mdash; the dart being the saying "
            "<em>&lsquo;I know, I see, that&rsquo;s how it is&rsquo;</em>.",
            "The object of criticism is precisely stated and it is not knowledge. It is the position "
            "taken up on the basis of knowledge: the assertion of one&rsquo;s own seeing as final. "
            "That is the dart, and the discourse has just spent four paragraphs describing someone "
            "who knows everything and does not throw it.",
            "For teaching, this is the discourse to reach for when a student worries that Buddhist "
            "epistemology is either a claim to omniscience or a refusal to claim anything. It is "
            "neither, and it says so at length."]),
        ("Against AN 4.23", [
            "The two discourses are adjacent and cover the same ground in opposite registers. AN 4.23 "
            "acclaims: supreme lion, no rival, turning the divine wheel. AN 4.24 analyzes: four "
            "corners, four negations, a technical term for construing, and a warning about "
            "certainty.",
            "That the compilers put them side by side is worth pointing out. A reader who takes only "
            "the first will have a devotional picture with nothing in it to think with; a reader who "
            "takes only the second will miss that the tradition also sings. The chapter offers both "
            "and does not rank them."]),
    ],
    terms=[
        ("maññati",
         "&ldquo;conceives, imagines, construes&rdquo; &mdash; to build a notion about something, "
         "especially in relation to a self. The key term of the central passage."),
        ("tādī",
         "&ldquo;the unaffected one&rdquo;, literally &lsquo;such&rsquo; &mdash; unchanged by "
         "circumstance, from the same family as <em>tathāgata</em>."),
        ("diṭṭha suta muta viññāta",
         "&ldquo;seen, heard, thought, known&rdquo; &mdash; the canonical fourfold division of "
         "everything that can be experienced."),
        ("catuṣkoṭi",
         "the four-cornered scheme of affirm, deny, both, and neither &mdash; used here to eliminate "
         "the evasions and leave a plain positive claim standing."),
        ("salla",
         "&ldquo;dart&rdquo; &mdash; not knowledge but the position taken up on it: "
         "&lsquo;I know, I see, that&rsquo;s how it is&rsquo;."),
    ],
    text_intro=(
        "The discourse in full: the claim, the three rejected reformulations, the fourfold analysis, "
        "and the verses. The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "an4.24:1.1-1.5"),
        ("h3", "That I know"),
        ("p", "&sect;2", "an4.24:2.1-3.2"),
        ("h3", "Three things he will not say"),
        ("p", "&sect;3", "an4.24:4.1-6.1"),
        ("h3", "Seeing without conceiving"),
        ("p", "&sect;4", "an4.24:7.1-7.6"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.24:8.1-9.4"),
    ],
    quiz=[
        {"q": "What three formulations does the discourse rule out?",
         "opts": [
             "That he knows, that he teaches, that he is awakened",
             "&lsquo;I do not know&rsquo;, &lsquo;I both know and do not know&rsquo;, and &lsquo;I neither know nor do not know&rsquo;",
             "The three characteristics",
             "Past, present, and future knowledge"],
         "correct": 1,
         "expl": "The four-cornered scheme, with the positive corner left standing."},
        {"q": "How is that use of the four corners unusual?",
         "opts": [
             "It is the only occurrence in the canon",
             "The structure is more often used to reject all four corners; here it defends a plain positive claim by eliminating the evasions",
             "It omits one corner",
             "It reverses the order"],
         "correct": 1,
         "expl": "He is not being coy about whether he knows."},
        {"q": "What does <em>maññati</em> mean?",
         "opts": [
             "To perceive",
             "To conceive, imagine, or construe &mdash; especially in relation to a self",
             "To remember",
             "To deny"],
         "correct": 1,
         "expl": "Not that he has no thoughts, but that he builds nothing on the seeing."},
        {"q": "What are the four things not conceived, taking sight as the example?",
         "opts": [
             "The eye, the sight, the consciousness, and the contact",
             "The seen, the unseen, what is to be seen, and a seer",
             "Past, present, future, and timeless sights",
             "Form, feeling, perception, and choices"],
         "correct": 1,
         "expl": "Three tenses of the object, then the subject."},
        {"q": "Why does the guide say the fourth negation matters most?",
         "opts": [
             "It is the longest",
             "A reader tracking only the first three hears a discourse about not clinging to experiences; the fourth makes it a discourse about there being no experiencer",
             "It is repeated",
             "It appears in the verse"],
         "correct": 1,
         "expl": "The fourth removes the subject."},
        {"q": "What does <em>tādī</em> mean?",
         "opts": [
             "Silent",
             "&lsquo;Such&rsquo; &mdash; the one who is thus, unchanged by circumstance",
             "Learned",
             "Detached"],
         "correct": 1,
         "expl": "From the same <em>tathā</em> family as <em>tathāgata</em> in AN 4.23."},
        {"q": "Which earlier discourse of the Fours uses the same &lsquo;nothing better or finer&rsquo; criterion?",
         "opts": [
             "AN 4.8",
             "AN 4.16, on subtlety",
             "AN 4.10",
             "AN 4.21"],
         "correct": 1,
         "expl": "The same phrase marks the endpoint in both."},
        {"q": "What is the dart?",
         "opts": [
             "Knowledge itself",
             "The position taken up on the basis of knowledge &mdash; &lsquo;I know, I see, that&rsquo;s how it is&rsquo;",
             "Craving",
             "Wrong view about the self"],
         "correct": 1,
         "expl": "The object of criticism is precisely stated, and it is not knowledge."},
        {"q": "What worry does the guide say this discourse answers?",
         "opts": [
             "That the Buddha was not omniscient",
             "That Buddhist epistemology is either a claim to omniscience or a refusal to claim anything &mdash; it is neither, and says so at length",
             "That the four corners are illogical",
             "That knowledge is impossible"],
         "correct": 1,
         "expl": "Someone who knows everything and does not throw the dart."},
        {"q": "How does the guide describe the pairing of AN 4.23 and AN 4.24?",
         "opts": [
             "As a contradiction to be resolved",
             "As the same ground in opposite registers &mdash; one acclaims, one analyzes &mdash; offered side by side without ranking",
             "As two versions of one discourse",
             "As addressed to different audiences"],
         "correct": 1,
         "expl": "Taking only one leaves the reader with half of what the tradition does."},
    ],
    marginalia=[
        ("Four corners", [
            "I do not know &mdash; a lie",
            "both &mdash; the same",
            "neither &mdash; a fault",
            "&mdash; leaving: I know",
        ]),
        ("Four negations", [
            "not the seen",
            "not the unseen",
            "not what is to be seen",
            "not a seer",
        ]),
        ("The dart", [
            "not knowing",
            "not seeing",
            "&ldquo;that&rsquo;s how it is&rdquo;",
        ]),
        ("Cross-references", [
            "AN 4.23 &middot; the same subject, acclaimed",
            "AN 4.16 &middot; nothing better or finer",
            "AN 4.25 &middot; next: what the life is for",
        ]),
    ],
    further=[
        '<a href="%s/an4.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.23.html">AN 4.23 &middot; The World</a> &mdash; the acclamatory treatment of '
        "the same subject.",
        '<a href="an-4.16.html">AN 4.16 &middot; Subtlety</a> &mdash; where the same criterion of '
        "nothing better or finer appears.",
        '<a href="an-4.25.html">AN 4.25 &middot; The Spiritual Life</a> &mdash; next in this series.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.25 — Brahmacariyasutta
# --------------------------------------------------------------------------- #
page(
    25, "Brahmacariya", "The Spiritual Life",
    vagga=VAGGA_3,
    meta_title="AN 4.25 — The Spiritual Life | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Brahmacariyasutta — four "
        "things the spiritual life is not lived for, and the four it is: restraint, giving up, "
        "fading away, and cessation. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_3),
        ("Speakers", SPEAKER),
        ("Form", "Four wrong reasons, four right ones, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Statements of the purpose of the holy life are common across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, and unusually direct about "
                       "institutional temptation"),
    ],
    why=(
        "Four things the spiritual life is not for: fawning on people, possessions and honor and "
        "popularity, winning debates, and being known about. Every one of them is a temptation "
        "available to a successful religious institution, and the discourse names them in a single "
        "sentence before saying what the life is actually for. It is a short text and an "
        "uncomfortable one to read in any century."),
    guide=[
        ("The teaching in one sentence", [
            "The spiritual life is for restraint, giving up, fading away, and cessation &mdash; and "
            "specifically not for the four things a successful religious life tends to become for."]),
        ("The four wrong reasons", [
            "Fawning and flattering people (<em>janakuhana</em>, <em>janalapana</em>); possessions, "
            "honor, and popularity (<em>lābhasakkārasiloka</em>); winning debates; and the thought "
            "<em>&lsquo;So let people know about me!&rsquo;</em>",
            "The list is a good one because the four are not the same temptation repeated. Flattery "
            "is about managing patrons. Gain and honor are about receiving. Debate is about "
            "intellectual dominance. And the last is about being seen at all &mdash; which is the "
            "subtlest, because it survives the renunciation of the other three.",
            "The third deserves particular note in a tradition with a long history of formal debate. "
            "Winning arguments is disqualified as a purpose, which does not mean argument is "
            "forbidden; AN 4.24 has just conducted one. The purpose is what is ruled out."]),
        ("The four right ones", [
            "<em>Saṁvara, pahāna, virāga, nirodha</em> &mdash; restraint, giving up, fading away, "
            "cessation. The first two are the first two efforts of AN 4.14, and the second two are "
            "part of the standard tail attached to the awakening factors there.",
            "Read as a sequence they describe a narrowing: hold back, let go, cool off, stop. Each "
            "term is less active than the one before it. That is characteristic of how the tradition "
            "describes the far end of the path &mdash; the early work is effortful and the late work "
            "is a subsiding, and the vocabulary tracks the change."]),
        ("The verse and tradition", [
            "The first verse contains a line worth pausing on: the Buddha taught the spiritual life "
            "<em>not because of tradition</em>. The Pāli is <em>na itihītihaṁ</em> &mdash; not by "
            "hearsay, not by &lsquo;so it is said, so it is said&rsquo;.",
            "The same phrase appears in the Kālāma discourse&rsquo;s famous list of insufficient "
            "grounds. Here it is applied not to the listener&rsquo;s reasons for accepting a teaching "
            "but to the teacher&rsquo;s reasons for giving one. The life is not taught because it was "
            "handed down; it is taught because of what it is for.",
            "That is a strong claim for a tradition to make about itself, and it does not sit "
            "comfortably beside AN 4.28, five discourses later, which will praise four noble "
            "traditions precisely for being <em>primordial, long-standing, traditional, and "
            "ancient</em>. The two are reconcilable &mdash; antiquity as a fact about the practices "
            "versus antiquity as a reason for them &mdash; but the tension is real and a student who "
            "spots it is reading well."]),
        ("Using it", [
            "The list of four wrong reasons transfers exactly to any institution that does good work "
            "and becomes successful at it. Managing donors, accumulating standing, winning the "
            "public argument, and being known: these are the four ways an organization&rsquo;s "
            "purpose gets replaced by its survival.",
            "The discourse offers no remedy and does not need to. Its whole function is to keep the "
            "purpose stated, so that the drift is visible when it happens. That is what a short text "
            "recited regularly is for."]),
    ],
    terms=[
        ("brahmacariya",
         "&ldquo;the spiritual life&rdquo;, literally the divine or best conduct &mdash; the whole "
         "life of training, not merely celibacy, though it includes that."),
        ("lābhasakkārasiloka",
         "&ldquo;possessions, honor, and popularity&rdquo; &mdash; a standing compound in the canon "
         "for what corrupts a religious life from outside."),
        ("saṁvara / pahāna",
         "&ldquo;restraint&rdquo; and &ldquo;giving up&rdquo; &mdash; the first two purposes, and "
         "the first two of the four efforts in AN 4.14."),
        ("virāga / nirodha",
         "&ldquo;fading away&rdquo; and &ldquo;cessation&rdquo; &mdash; the second two, each less "
         "active than the term before it."),
        ("itihītiha",
         "&ldquo;hearsay, &lsquo;so it is said&rsquo;&rdquo; &mdash; what the verse says the teaching "
         "was <em>not</em> given on account of."),
    ],
    text_intro=(
        "The discourse in full: what the life is not for, what it is for, and the two verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Not for these, but for these"),
        ("p", "&sect;1", "an4.25:1.1-1.2"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.25:2.1-2.6"),
        ("p", "&sect;3", "an4.25:3.1-3.4"),
    ],
    quiz=[
        {"q": "What four things is the spiritual life not lived for?",
         "opts": [
             "Rebirth, merit, praise, and long life",
             "Fawning on people, possessions and honor and popularity, winning debates, and being known about",
             "Gain, comfort, safety, and company",
             "Teaching, healing, ruling, and building"],
         "correct": 1,
         "expl": "Four temptations available to a successful religious institution."},
        {"q": "Why does the guide say the four are not one temptation repeated?",
         "opts": [
             "Because they occur at different stages",
             "Because they are managing patrons, receiving, intellectual dominance, and being seen at all",
             "Because three are monastic and one is lay",
             "Because the verse separates them"],
         "correct": 1,
         "expl": "The last is subtlest, because it survives the renunciation of the other three."},
        {"q": "Does the discourse forbid argument?",
         "opts": [
             "Yes, entirely",
             "No &mdash; it disqualifies winning as a purpose; AN 4.24 has just conducted an argument",
             "Only with brahmins",
             "Only in public"],
         "correct": 1,
         "expl": "The purpose is what is ruled out."},
        {"q": "What four things is the life lived for?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Restraint, giving up, fading away, and cessation",
             "Faith, energy, mindfulness, and immersion",
             "Contentment, good will, mindfulness, and immersion"],
         "correct": 1,
         "expl": "<em>Saṁvara, pahāna, virāga, nirodha</em>."},
        {"q": "What pattern does the guide find in those four?",
         "opts": [
             "Increasing effort",
             "A narrowing &mdash; hold back, let go, cool off, stop &mdash; with each term less active than the one before",
             "Alternating inner and outer",
             "No pattern"],
         "correct": 1,
         "expl": "The early work is effortful and the late work is a subsiding."},
        {"q": "What does <em>na itihītihaṁ</em> mean in the verse?",
         "opts": [
             "&lsquo;Not in this world&rsquo;",
             "&lsquo;Not because of tradition&rsquo; &mdash; not by hearsay, not by &lsquo;so it is said&rsquo;",
             "&lsquo;Not for a reward&rsquo;",
             "&lsquo;Not for the many&rsquo;"],
         "correct": 1,
         "expl": "The same phrase as in the Kālāma discourse&rsquo;s list of insufficient grounds."},
        {"q": "How is the phrase applied differently here?",
         "opts": [
             "It is not applied differently",
             "Not to the listener&rsquo;s reasons for accepting a teaching but to the teacher&rsquo;s reasons for giving one",
             "It is applied to lay followers",
             "It is applied to the Vinaya"],
         "correct": 1,
         "expl": "The life is taught because of what it is for, not because it was handed down."},
        {"q": "What tension does the guide flag with AN 4.28?",
         "opts": [
             "None",
             "AN 4.28 praises four traditions precisely for being primordial and ancient",
             "AN 4.28 rejects restraint",
             "AN 4.28 is addressed to wanderers"],
         "correct": 1,
         "expl": "Reconcilable &mdash; antiquity as a fact versus antiquity as a reason &mdash; but real."},
        {"q": "How does the guide say the four wrong reasons transfer?",
         "opts": [
             "They do not transfer outside monasticism",
             "To any institution that does good work and becomes successful &mdash; donors, standing, the public argument, and being known",
             "Only to religious institutions",
             "Only to individuals"],
         "correct": 1,
         "expl": "Four ways an organization&rsquo;s purpose gets replaced by its survival."},
        {"q": "What does the guide say the discourse&rsquo;s function is?",
         "opts": [
             "To prescribe a remedy",
             "To keep the purpose stated, so that drift is visible when it happens",
             "To rank the four faults",
             "To define the monastic life"],
         "correct": 1,
         "expl": "What a short text recited regularly is for."},
    ],
    marginalia=[
        ("Not for", [
            "flattering patrons",
            "gain and honor",
            "winning debates",
            "being known about",
        ]),
        ("But for", [
            "<span class=\"pali\">saṁvara</span>restraint",
            "<span class=\"pali\">pahāna</span>giving up",
            "<span class=\"pali\">virāga</span>fading away",
            "<span class=\"pali\">nirodha</span>cessation",
        ]),
        ("A tension", [
            "4.25 &middot; not by tradition",
            "4.28 &middot; primordial, ancient",
            "&mdash; worth noticing",
        ]),
        ("Cross-references", [
            "AN 4.26 &middot; next: who is no follower",
            "AN 4.14 &middot; restraint and giving up",
            "AN 3.65 &middot; the same phrase on hearsay",
        ]),
    ],
    further=[
        '<a href="%s/an4.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.26.html">AN 4.26 &middot; Deceivers</a> &mdash; next in this series, and the '
        "personal version of the same warning.",
        '<a href="an-3.65.html">AN 3.65 &middot; With the Kālāmas of Kesamutta</a> &mdash; where '
        "hearsay appears in the list of insufficient grounds.",
        '<a href="an-4.28.html">AN 4.28 &middot; The Noble Traditions</a> &mdash; the discourse this '
        "one sits in tension with.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.26 — Kuhasutta
# --------------------------------------------------------------------------- #
page(
    26, "Kuha", "Deceivers",
    vagga=VAGGA_3,
    meta_title="AN 4.26 — Deceivers | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kuhasutta — deceivers, "
        "flatterers, the pompous and fake, the insolent and scattered are no followers of mine. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_3),
        ("Speakers", SPEAKER),
        ("Form", "Five faults, their five opposites, and two verses repeating both"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Lists of the deceitful monastic recur across the Chinese Āgamas and "
                              "the Nikāya commentaries; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short and blunt, with one "
                       "question worth raising about its severity"),
    ],
    why=(
        "&ldquo;Those mendicants are no followers of mine.&rdquo; The disavowal is unusually direct, "
        "and the faults that earn it are not moral catastrophes: deceit, flattery, pomposity, "
        "insolence, and a scattered mind. This is the personal counterpart to AN 4.25 &mdash; there "
        "the institution&rsquo;s purposes, here the individual&rsquo;s manner &mdash; and it is "
        "harsher than the discourse before it."),
    guide=[
        ("The teaching in one sentence", [
            "Five habits of self-presentation disqualify a person from the training, whatever else "
            "they are doing."]),
        ("The five faults", [
            "<em>Kuha</em>, deceiver &mdash; specifically one who fakes attainments or virtues. "
            "<em>Lapa</em>, flatterer &mdash; one who talks people round, especially for support. "
            "<em>Nemittika</em> and <em>nippesika</em>, rendered pompous and fake, cover hinting for "
            "gifts and belittling others into giving. <em>Unnaḷa</em>, insolent &mdash; literally "
            "&lsquo;with the reed raised&rsquo;, a fine image for someone holding themselves up. "
            "<em>Asamāhita</em>, scattered &mdash; not composed, not in samādhi.",
            "Four of the five are ways of managing other people&rsquo;s opinion of you. The fifth is "
            "not: a scattered mind is a private condition. Its inclusion is what makes the list a "
            "spiritual diagnosis rather than a code of manners &mdash; and the ordering suggests why "
            "the two belong together, since a mind occupied with how it appears is not available to "
            "settle."]),
        ("The disavowal", [
            "<em>Those mendicants are no followers of mine</em> &mdash; <em>na me te bhikkhave "
            "bhikkhū māmakā</em>. <em>Māmaka</em> is &lsquo;mine&rsquo; used as a noun: my people.",
            "It is the strongest formula of exclusion in the chapter and it is worth handling "
            "carefully. AN 4.2 said that someone lacking ethics, immersion, wisdom, and freedom has "
            "fallen from this teaching and training; that was a statement about a condition. This is "
            "a statement about a relationship, in the first person, and it is a disowning.",
            "Read plainly, the discourse says that a person may be ordained, resident, and outwardly "
            "practising and still not be one of the teacher&rsquo;s own. Whether that is meant as a "
            "sociological fact or as a warning designed to be overheard is not something the text "
            "settles."]),
        ("Why these faults and not worse ones", [
            "A fair question: why is the disavowal reserved for pretension rather than for, say, "
            "cruelty or theft? The discourse does not answer, but the shape of the collection "
            "suggests one.",
            "Gross misconduct is the Vinaya&rsquo;s business and has formal procedures attached. What "
            "the discourses handle is the class of faults that no procedure catches &mdash; the ones "
            "that are entirely compatible with keeping every rule. A monk who hints for gifts and "
            "carries himself grandly has broken nothing formal, which is precisely why a discourse is "
            "needed to name it.",
            "There is also a coherent reason internal to the fault. These five are the faults of "
            "someone using the training for standing. That is not a failure within the training; it "
            "is a substitution of something else for it, and a substitution is disqualifying in a way "
            "that a lapse is not."]),
        ("The positive list", [
            "Genuine (<em>amāya</em>, without deceit), not flatterers, attentive, amenable, serene. "
            "Two of these are worth noting: <em>amāya</em> is the negation of illusion or trickery, "
            "and <em>suvaca</em> &mdash; here &lsquo;amenable&rsquo; &mdash; means literally "
            "&lsquo;easy to speak to&rsquo;, that is, someone who takes correction.",
            "<em>Suvaca</em> is a quietly demanding virtue and appears throughout the monastic "
            "literature. It names the quality that makes any of the rest of the training possible: "
            "if a person cannot be told, nothing anyone observes about them can reach them."]),
        ("The verses", [
            "The verses repeat both halves almost word for word, adding only that these do or do not "
            "<em>grow in the teaching that was taught by the perfected Buddha</em>.",
            "That verb is the discourse&rsquo;s one addition. The prose said such mendicants achieve "
            "no growth, improvement, or maturity; the verse compresses it to growth alone. The image "
            "is organic and it fits the diagnosis: pretension does not damage the training so much as "
            "arrest it. Nothing goes wrong; nothing happens."]),
    ],
    terms=[
        ("kuha",
         "&ldquo;deceiver&rdquo; &mdash; specifically one who fakes attainments or virtues; the "
         "discourse takes its name from this word."),
        ("unnaḷa",
         "&ldquo;insolent&rdquo;, literally &lsquo;with the reed raised&rsquo; &mdash; a fine image "
         "for someone holding themselves up."),
        ("asamāhita",
         "&ldquo;scattered, uncomposed&rdquo; &mdash; the one private fault on the list, and what "
         "makes it a spiritual diagnosis rather than a code of manners."),
        ("māmaka",
         "&ldquo;mine, my people&rdquo; &mdash; the noun in the disavowal. A statement about a "
         "relationship rather than about a condition."),
        ("suvaca",
         "&ldquo;amenable&rdquo;, literally &lsquo;easy to speak to&rsquo; &mdash; one who takes "
         "correction, and the quality that makes the rest of the training possible."),
    ],
    text_intro=(
        "The discourse in full: the five faults, their opposites, and the two verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "No followers of mine"),
        ("p", "&sect;1", "an4.26:1.1-1.4"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.26:2.1-2.4"),
        ("p", "&sect;3", "an4.26:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does the Buddha say of deceivers and flatterers?",
         "opts": [
             "That they must be expelled",
             "That they are no followers of his",
             "That they will be reborn in hell",
             "That they should be corrected"],
         "correct": 1,
         "expl": "The strongest formula of exclusion in the chapter."},
        {"q": "How does that differ from AN 4.2&rsquo;s &lsquo;fallen&rsquo;?",
         "opts": [
             "It does not differ",
             "AN 4.2 states a condition; this states a relationship, in the first person &mdash; it is a disowning",
             "AN 4.2 is harsher",
             "This applies only to lay people"],
         "correct": 1,
         "expl": "<em>Māmaka</em> is &lsquo;mine&rsquo; used as a noun: my people."},
        {"q": "Which of the five faults is not about managing others&rsquo; opinion?",
         "opts": [
             "Deceit",
             "A scattered mind &mdash; a private condition",
             "Flattery",
             "Insolence"],
         "correct": 1,
         "expl": "Its inclusion makes the list a spiritual diagnosis rather than a code of manners."},
        {"q": "What does <em>unnaḷa</em> literally mean?",
         "opts": [
             "Loud",
             "&lsquo;With the reed raised&rsquo; &mdash; holding oneself up",
             "Empty",
             "Unbending"],
         "correct": 1,
         "expl": "A fine image for insolence."},
        {"q": "Why does the guide say pretension and a scattered mind belong together?",
         "opts": [
             "They are the same word in Pāli",
             "A mind occupied with how it appears is not available to settle",
             "Both are Vinaya offenses",
             "The verses pair them"],
         "correct": 1,
         "expl": "Which is why the ordering makes sense."},
        {"q": "Why might the disavowal be reserved for pretension rather than gross misconduct?",
         "opts": [
             "Because pretension is worse in every case",
             "Because gross misconduct is the Vinaya&rsquo;s business; the discourses handle faults that no procedure catches",
             "Because gross misconduct was rare",
             "Because pretension is easier to see"],
         "correct": 1,
         "expl": "A monk who hints for gifts and carries himself grandly has broken nothing formal."},
        {"q": "What internal reason does the guide give?",
         "opts": [
             "That these faults are incurable",
             "That these five are the faults of someone using the training for standing &mdash; a substitution rather than a lapse",
             "That they offend donors",
             "That they spread to others"],
         "correct": 1,
         "expl": "A substitution is disqualifying in a way that a lapse is not."},
        {"q": "What does <em>suvaca</em> mean?",
         "opts": [
             "Well-spoken",
             "&lsquo;Easy to speak to&rsquo; &mdash; one who takes correction",
             "Silent",
             "Truthful"],
         "correct": 1,
         "expl": "If a person cannot be told, nothing anyone observes about them can reach them."},
        {"q": "What single verb do the verses add?",
         "opts": [
             "Fall",
             "Grow &mdash; these do or do not grow in the teaching",
             "Attain",
             "Depart"],
         "correct": 1,
         "expl": "The prose said growth, improvement, or maturity; the verse compresses it."},
        {"q": "What does the guide draw from that image?",
         "opts": [
             "That the fault is easily corrected",
             "That pretension does not damage the training so much as arrest it &mdash; nothing goes wrong, nothing happens",
             "That growth is guaranteed",
             "That the verses are decorative"],
         "correct": 1,
         "expl": "The image is organic and fits the diagnosis."},
    ],
    marginalia=[
        ("Five faults", [
            "<span class=\"pali\">kuha</span>deceiver",
            "<span class=\"pali\">lapa</span>flatterer",
            "pompous and fake",
            "<span class=\"pali\">unnaḷa</span>insolent",
            "<span class=\"pali\">asamāhita</span>scattered",
        ]),
        ("The disavowal", [
            "<span class=\"pali\">māmaka</span>my people",
            "&mdash; and these are not",
        ]),
        ("The virtue to note", [
            "<span class=\"pali\">suvaca</span>easy to speak to",
            "one who takes correction",
            "&mdash; without it, nothing reaches",
        ]),
        ("Cross-references", [
            "AN 4.25 &middot; the institutional version",
            "AN 4.27 &middot; next: four trifles",
            "AN 4.2 &middot; fallen from the training",
        ]),
    ],
    further=[
        '<a href="%s/an4.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.25.html">AN 4.25 &middot; The Spiritual Life</a> &mdash; the same warning '
        "aimed at purposes rather than persons.",
        '<a href="an-4.27.html">AN 4.27 &middot; Contentment</a> &mdash; next in this series, and the '
        "positive practice these faults displace.",
        '<a href="an-4.2.html">AN 4.2 &middot; Fallen</a> &mdash; the other statement of being '
        "outside the training.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.27 — Santuṭṭhisutta
# --------------------------------------------------------------------------- #
page(
    27, "Santuṭṭhi", "Contentment",
    vagga=VAGGA_3,
    meta_title="AN 4.27 — Contentment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Santuṭṭhisutta — rag-robes, "
        "a lump of almsfood, the root of a tree, and rancid urine as medicine: four trifles that are "
        "easy to find and blameless. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_3),
        ("Speakers", SPEAKER),
        ("Form", "Four items, a conclusion, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four resorts or <em>nissaya</em> are standard across the Chinese "
                              "Āgamas and Vinayas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, concrete, and easy to "
                       "misread as asceticism for its own sake"),
    ],
    why=(
        "The four minimum requisites, named at their humblest: robes made from rags, a lump of "
        "almsfood, lodging at the foot of a tree, and rancid urine for medicine. The word attached "
        "to them is not &lsquo;hard&rsquo; or &lsquo;pure&rsquo; but <em>appa</em>, trifling &mdash; "
        "and the two adjectives that matter are that they are easy to find and that they are "
        "blameless. The argument is about availability, not austerity."),
    guide=[
        ("The teaching in one sentence", [
            "There is a version of each necessity that costs nobody anything and can be had "
            "anywhere, and being content with that version removes a whole category of trouble."]),
        ("The four", [
            "These are the four <em>nissaya</em>, the resorts or supports, recited to every candidate "
            "at ordination in the Theravāda tradition to this day. They are the floor of the monastic "
            "life: the least a mendicant can be given and still live.",
            "The fourth is the one that startles modern readers. <em>Pūtimutta</em>, rancid or "
            "fermented urine, was a real medicine of the period, generally understood as cattle urine "
            "used as a preservative and treatment. It is on the list because it was free and "
            "universally available, which is the criterion the whole list is built on."]),
        ("Easy to find, and blameless", [
            "Two adjectives, and they are doing different work. <em>Sulabha</em>, easy to find, is "
            "about supply: these things can be obtained anywhere, at any season, without a patron. "
            "<em>Anavajja</em>, blameless, is about acquisition: getting them injures nobody and "
            "requires nothing improper.",
            "That second one is the point most easily missed. The recommendation is not that "
            "discomfort is meritorious. It is that a person whose needs are at this level cannot be "
            "compromised by the process of meeting them &mdash; no hinting, no flattery, no "
            "dependence on anyone who might then have a claim.",
            "Read directly after AN 4.26, which listed hinting for gifts and flattering patrons among "
            "the faults that disqualify a person, the arrangement is transparent. AN 4.26 named the "
            "corruption; AN 4.27 names the condition that makes it unnecessary."]),
        ("What contentment is being praised", [
            "<em>Santuṭṭhi</em> is contentment or satisfaction &mdash; being pleased with what is "
            "there. The discourse says that being content with trifles easy to find is <em>one of the "
            "factors of the ascetic life</em>, <em>sāmaññaṅga</em>.",
            "The qualifier &lsquo;one of&rsquo; is honest and worth keeping. Contentment is a "
            "component, not the whole; the discourse does not claim that a person satisfied with "
            "little has thereby done the work. The verses say the same thing in the other direction "
            "&mdash; these qualities are integral to the ascetic life, and they are mastered by one "
            "who trains."]),
        ("The negative payoff", [
            "The first verse states the benefit entirely negatively: you do not get upset about "
            "lodgings, robes, food, and drink, and you are <em>not obstructed anywhere</em> "
            "(<em>na ca kattha ci vighāto</em>).",
            "This is characteristic and worth noticing as a pattern. The gain from contentment is not "
            "described as a positive pleasure but as the absence of a friction. A large amount of any "
            "life is spent managing the gap between what is wanted and what is available; close the "
            "gap by lowering the requirement and the management stops.",
            "&lsquo;Not obstructed anywhere&rsquo; also carries a practical meaning for a wandering "
            "life. A mendicant whose requirements can be met in any village is free to go to any "
            "village. Contentment here is not only an inner state; it is what makes movement "
            "possible."]),
        ("How not to teach it", [
            "The obvious misuse of this discourse is to preach contentment to people who lack things "
            "&mdash; which turns a description of voluntary simplicity into an instruction to the "
            "poor to want less. Nothing in the text supports that, and the setting rules it out: "
            "these are the requisites of people who have deliberately given up property.",
            "The transferable claim is narrower and sound. For anything you have chosen to pursue, "
            "there is a level of provision below which you cannot be leveraged. Finding that level "
            "and being genuinely content at it is a form of freedom, and it is the form this "
            "discourse is describing."]),
    ],
    terms=[
        ("santuṭṭhi",
         "&ldquo;contentment&rdquo; &mdash; being pleased with what is there. Named as one of the "
         "factors of the ascetic life, not the whole of it."),
        ("nissaya",
         "&ldquo;resort, support&rdquo; &mdash; the four requisites at their minimum, recited to "
         "candidates at ordination to this day."),
        ("sulabha",
         "&ldquo;easy to find&rdquo; &mdash; the first adjective, about supply: obtainable anywhere, "
         "at any season, without a patron."),
        ("anavajja",
         "&ldquo;blameless&rdquo; &mdash; the second, about acquisition: getting them injures nobody "
         "and requires nothing improper."),
        ("pūtimutta",
         "&ldquo;rancid urine&rdquo; &mdash; a real medicine of the period, on the list because it "
         "was free and universally available."),
    ],
    text_intro=(
        "The discourse in full: the four trifles and the two verses. The ellipses are the "
        "Pāli&rsquo;s own abbreviation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four trifles"),
        ("p", "&sect;1", "an4.27:1.1-1.8"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.27:2.1-2.6"),
        ("p", "&sect;3", "an4.27:3.1-3.4"),
    ],
    quiz=[
        {"q": "What are the four trifles?",
         "opts": [
             "Silence, solitude, simplicity, and study",
             "Rag-robes, a lump of almsfood, lodgings at the root of a tree, and rancid urine as medicine",
             "Food, clothing, shelter, and medicine of any kind",
             "The four requisites of a wheel-turning monarch"],
         "correct": 1,
         "expl": "The four <em>nissaya</em>, recited at ordination to this day."},
        {"q": "What two adjectives are attached to them?",
         "opts": [
             "Hard and pure",
             "Easy to find, and blameless",
             "Ancient and uncorrupted",
             "Sufficient and lasting"],
         "correct": 1,
         "expl": "One about supply, one about acquisition."},
        {"q": "What does &lsquo;blameless&rsquo; add?",
         "opts": [
             "That the items are ritually clean",
             "That getting them injures nobody and requires nothing improper",
             "That they are permitted by the Vinaya",
             "That they cannot be stolen"],
         "correct": 1,
         "expl": "The point most easily missed."},
        {"q": "How does this connect to AN 4.26?",
         "opts": [
             "It does not",
             "AN 4.26 named the corruption &mdash; hinting for gifts, flattering patrons &mdash; and this names the condition that makes it unnecessary",
             "It repeats the same faults",
             "It contradicts it"],
         "correct": 1,
         "expl": "The arrangement is transparent."},
        {"q": "Why is rancid urine on the list?",
         "opts": [
             "As a mortification",
             "Because it was a real medicine of the period and was free and universally available",
             "As a metaphor",
             "Because other medicines were forbidden"],
         "correct": 1,
         "expl": "Availability is the criterion the whole list is built on."},
        {"q": "How strong a claim does the discourse make for contentment?",
         "opts": [
             "That it is the whole of the ascetic life",
             "That it is one of the factors of the ascetic life",
             "That it guarantees awakening",
             "That it replaces meditation"],
         "correct": 1,
         "expl": "The qualifier is honest and worth keeping."},
        {"q": "How is the benefit stated in the verse?",
         "opts": [
             "As a positive pleasure",
             "Negatively &mdash; you do not get upset about requisites, and are not obstructed anywhere",
             "As rebirth in heaven",
             "As long life"],
         "correct": 1,
         "expl": "The gain is the absence of a friction."},
        {"q": "What practical meaning does &lsquo;not obstructed anywhere&rsquo; carry?",
         "opts": [
             "Freedom from illness",
             "A mendicant whose requirements can be met in any village is free to go to any village",
             "Freedom from criticism",
             "Freedom from the Vinaya"],
         "correct": 1,
         "expl": "Contentment here is what makes movement possible."},
        {"q": "What misuse does the guide warn against?",
         "opts": [
             "Reading it as monastic only",
             "Preaching contentment to people who lack things &mdash; turning voluntary simplicity into an instruction to the poor to want less",
             "Reading it literally",
             "Applying it to medicine"],
         "correct": 1,
         "expl": "The setting rules it out: these are the requisites of people who have deliberately given up property."},
        {"q": "What is the transferable claim the guide offers instead?",
         "opts": [
             "That poverty is virtuous",
             "That for anything you have chosen to pursue there is a level of provision below which you cannot be leveraged",
             "That needs should be ignored",
             "That simplicity is efficient"],
         "correct": 1,
         "expl": "Finding that level and being content at it is a form of freedom."},
    ],
    marginalia=[
        ("The four", [
            "rag-robes",
            "a lump of almsfood",
            "the root of a tree",
            "rancid urine",
        ]),
        ("Two adjectives", [
            "<span class=\"pali\">sulabha</span>easy to find",
            "<span class=\"pali\">anavajja</span>blameless",
            "&mdash; supply, and acquisition",
        ]),
        ("The payoff", [
            "not upset about requisites",
            "not obstructed anywhere",
            "&mdash; stated as an absence",
        ]),
        ("Cross-references", [
            "AN 4.26 &middot; the corruption this prevents",
            "AN 4.28 &middot; next: the noble traditions",
            "AN 4.9 &middot; craving and the requisites",
        ]),
    ],
    further=[
        '<a href="%s/an4.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.28.html">AN 4.28 &middot; The Noble Traditions</a> &mdash; next in this '
        "series, where contentment becomes the first of four ancient traditions.",
        '<a href="an-4.9.html">AN 4.9 &middot; The Arising of Craving</a> &mdash; where the same '
        "requisites are named as the occasions of craving.",
        '<a href="an-4.26.html">AN 4.26 &middot; Deceivers</a> &mdash; on hinting for gifts and '
        "flattering patrons.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.28 — Ariyavaṁsasutta
# --------------------------------------------------------------------------- #
page(
    28, "Ariyavaṁsa", "The Noble Traditions",
    vagga=VAGGA_3,
    meta_title="AN 4.28 — The Noble Traditions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ariyavaṁsasutta — four "
        "noble traditions, primordial and uncorrupted: contentment with robes, almsfood, and "
        "lodgings, and the love of meditation and of giving up. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_3),
        ("Speakers", SPEAKER),
        ("Form", "Four traditions with a repeated formula, a clause on the four directions, and two "
                 "verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The <em>ariyavaṁsa</em> is a well-known set with counterparts across "
                              "the Chinese Āgamas and a long commentarial life in Sri Lanka; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; formulaic, with one clause that "
                       "does most of the work"),
    ],
    why=(
        "Four traditions called primordial, long-standing, and ancient, which sensible people do "
        "not look down on. Three of them are contentment with robes, almsfood, and lodgings; the "
        "fourth is enjoying meditation and enjoying giving up. But the sentence attached to every "
        "one of them is the discourse&rsquo;s real content: <em>they don&rsquo;t glorify themselves "
        "or put others down on account of it</em>. Every virtue on this list comes with its own "
        "corruption named."),
    guide=[
        ("The teaching in one sentence", [
            "Four ancient practices, each stated together with the way of holding it that would "
            "spoil it."]),
        ("What <em>ariyavaṁsa</em> means", [
            "<em>Vaṁsa</em> is a lineage, a line of descent, a tradition handed down &mdash; the word "
            "used of family lines and of dynasties. <em>Ariya</em> is noble. So: the noble lineages, "
            "the descent line of the noble ones.",
            "The set is described with four adjectives &mdash; primordial, long-standing, "
            "traditional, ancient &mdash; and then with a clause about corruption: uncorrupted as "
            "they have been since the beginning, not being corrupted now, and not going to be. That "
            "is a strong claim of continuity in a tradition well aware that institutions decay.",
            "It is fair to read this against AN 4.25, three discourses earlier, which said the "
            "spiritual life was taught <em>not because of tradition</em>. The two can be held "
            "together: antiquity is not offered here as the reason to practise these four, but as an "
            "observation that they are the practices which do not degrade. What ages badly is "
            "everything else."]),
        ("The first three", [
            "Contentment with any kind of robe, almsfood, and lodgings, and praising such "
            "contentment. Each comes with three further conditions: no improper solicitation for it; "
            "no worry if it does not come; and if it does come, using it <em>untied, uninfatuated, "
            "unattached, seeing the drawback, and understanding the escape</em>.",
            "That last formula is the one to notice. It is not asked that the mendicant refuse a good "
            "robe. It is asked that they use it with the five headings of AN 4.10 in view. "
            "Contentment here is not a preference for less; it is a particular relationship to "
            "whatever arrives.",
            "AN 4.27, just read, gave the floor of provision. This discourse gives the disposition "
            "that makes any level of provision safe, which is a different and more portable "
            "teaching."]),
        ("The fourth, and why it is different", [
            "The fourth is not contentment with a requisite. It is enjoying meditation and loving to "
            "meditate, enjoying giving up and loving to give up &mdash; <em>bhāvanārāma</em> and "
            "<em>pahānārāma</em>.",
            "So three renunciations and one appetite. The list would be lopsided without it: three "
            "practices of not-wanting, and then one thing it is right to want. The tradition is "
            "consistently uninterested in a purely negative account of the path, and this is where "
            "the chapter says so most plainly.",
            "The word <em>ārāma</em> is worth a note. It means delight or pleasure, and also a park "
            "or pleasure-garden &mdash; the same word in the name of Anāthapiṇḍika&rsquo;s monastery. "
            "The compound suggests a place one likes to be, which is a more relaxed image than "
            "&lsquo;devoted to&rsquo; would give."]),
        ("The clause that does the work", [
            "After each of the four: <em>But they don&rsquo;t glorify themselves or put others down "
            "on account of it.</em>",
            "This is what keeps the discourse from being a list of things to be proud of, and it is "
            "aimed at the specific failure mode of each item. Ascetic practices are unusually "
            "available to display, because they are visible and comparative: a worse robe is a "
            "publicly legible fact about you. Meditation is the same. The four practices most likely "
            "to earn admiration are exactly the four listed, and the clause is attached to each.",
            "The corruption named is double &mdash; self-elevation and putting others down &mdash; "
            "and the second half is the more insidious. A person can hold their own practice modestly "
            "and still measure everyone else by it."]),
        ("The four directions, and the verses", [
            "The closing prose says that a mendicant with these four prevails over discontent "
            "(<em>arati</em>) wherever they live, east, west, north, or south, because "
            "<em>the attentive prevail over desire and discontent</em>.",
            "The point is portability. These four are not tied to a place, a climate, a supporter, or "
            "a season, which is precisely why they can be a lineage rather than a local custom. A "
            "tradition that can be carried anywhere is one that can last.",
            "The second verse reuses the Black Plum River gold simile that closed AN 4.6 &mdash; a "
            "pendant of finest gold, whom even the gods praise. That the compilers reached for the "
            "same image for the learned disciple and for the one standing in the noble traditions is "
            "a small piece of evidence about how the collection was assembled, and worth pointing out "
            "to a reader who has been through both."]),
    ],
    terms=[
        ("ariyavaṁsa",
         "&ldquo;noble tradition&rdquo; &mdash; <em>vaṁsa</em> is a lineage or line of descent, the "
         "word used of family lines and dynasties."),
        ("bhāvanārāma",
         "&ldquo;enjoying meditation&rdquo; &mdash; <em>ārāma</em> is delight, and also a "
         "pleasure-garden: a place one likes to be."),
        ("pahānārāma",
         "&ldquo;enjoying giving up&rdquo; &mdash; the fourth tradition&rsquo;s other half, and the "
         "one appetite among three renunciations."),
        ("arati",
         "&ldquo;discontent, dissatisfaction&rdquo; &mdash; what the attentive prevail over in any of "
         "the four directions."),
        ("anavaññatti",
         "the refusal to glorify oneself or put others down &mdash; the clause attached to every item "
         "on the list, and where its real content lies."),
    ],
    text_intro=(
        "The discourse in full: the four traditions, the four directions, and the verses. "
        "The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Contentment with robes"),
        ("p", "&sect;1", "an4.28:1.1-1.5"),
        ("h3", "Almsfood and lodgings"),
        ("p", "&sect;2", "an4.28:2.1-3.3"),
        ("h3", "Enjoying meditation and giving up"),
        ("p", "&sect;3", "an4.28:4.1-4.4"),
        ("h3", "In any direction"),
        ("p", "&sect;4", "an4.28:5.1-5.6"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.28:6.1-6.4"),
        ("p", "&sect;6", "an4.28:7.1-7.6"),
    ],
    quiz=[
        {"q": "What are the four noble traditions?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Contentment with robes, with almsfood, and with lodgings, and enjoying meditation and giving up",
             "Contentment, good will, mindfulness, and immersion",
             "The four requisites"],
         "correct": 1,
         "expl": "Three renunciations and one appetite."},
        {"q": "What does <em>vaṁsa</em> mean?",
         "opts": [
             "Practice",
             "A lineage or line of descent &mdash; the word used of family lines and dynasties",
             "Vow",
             "Community"],
         "correct": 1,
         "expl": "So: the descent line of the noble ones."},
        {"q": "How does the guide reconcile this with AN 4.25&rsquo;s &lsquo;not because of tradition&rsquo;?",
         "opts": [
             "It does not; they conflict",
             "Antiquity is not offered as the reason to practise these four, but as an observation that they are the practices which do not degrade",
             "AN 4.25 is later",
             "The two use different words for tradition"],
         "correct": 1,
         "expl": "What ages badly is everything else."},
        {"q": "What three conditions accompany each of the first three traditions?",
         "opts": [
             "Silence, solitude, and simplicity",
             "No improper solicitation, no worry if it does not come, and using it untied and unattached, seeing the drawback and the escape",
             "Ethics, immersion, and wisdom",
             "Faith, effort, and mindfulness"],
         "correct": 1,
         "expl": "The five headings of AN 4.10 applied to a robe."},
        {"q": "What kind of contentment is being described?",
         "opts": [
             "A preference for less",
             "A particular relationship to whatever arrives &mdash; the mendicant is not asked to refuse a good robe",
             "Refusal of all requisites",
             "Indifference to the body"],
         "correct": 1,
         "expl": "A different and more portable teaching than AN 4.27&rsquo;s floor of provision."},
        {"q": "Why does the guide say the fourth item is needed?",
         "opts": [
             "To reach the number four",
             "Because the list would otherwise be three practices of not-wanting with nothing it is right to want",
             "Because meditation is the hardest",
             "Because the verses require it"],
         "correct": 1,
         "expl": "The tradition is consistently uninterested in a purely negative account of the path."},
        {"q": "What clause is attached to every one of the four?",
         "opts": [
             "That it leads to heaven",
             "That they do not glorify themselves or put others down on account of it",
             "That it is difficult",
             "That it was taught by past Buddhas"],
         "correct": 1,
         "expl": "What keeps the discourse from being a list of things to be proud of."},
        {"q": "Why is that clause aimed at these four in particular?",
         "opts": [
             "Because they are the easiest",
             "Because ascetic practices are visible and comparative &mdash; a worse robe is a publicly legible fact about you",
             "Because they are monastic",
             "Because they are ancient"],
         "correct": 1,
         "expl": "The four practices most likely to earn admiration are exactly the four listed."},
        {"q": "Which half of the double corruption does the guide call more insidious?",
         "opts": [
             "Self-elevation",
             "Putting others down &mdash; a person can hold their own practice modestly and still measure everyone else by it",
             "Neither",
             "They are the same"],
         "correct": 1,
         "expl": "The second half is easier to miss in oneself."},
        {"q": "What is the point of the four directions?",
         "opts": [
             "Missionary expansion",
             "Portability &mdash; these four are not tied to a place, climate, supporter, or season, which is why they can be a lineage",
             "Cosmology",
             "The four assemblies"],
         "correct": 1,
         "expl": "A tradition that can be carried anywhere is one that can last."},
    ],
    marginalia=[
        ("The four", [
            "content with robes",
            "content with almsfood",
            "content with lodgings",
            "loving to meditate, to give up",
        ]),
        ("The clause", [
            "no glorifying oneself",
            "no putting others down",
            "&mdash; attached to each",
        ]),
        ("Four adjectives", [
            "primordial",
            "long-standing",
            "traditional",
            "ancient",
        ]),
        ("Cross-references", [
            "AN 4.27 &middot; the floor of provision",
            "AN 4.29 &middot; next: the footprints",
            "AN 4.6 &middot; the same gold simile",
        ]),
    ],
    further=[
        '<a href="%s/an4.28/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.29.html">AN 4.29 &middot; Footprints of the Dhamma</a> &mdash; next in this '
        "series, and the same four adjectives applied to a different set.",
        '<a href="an-4.27.html">AN 4.27 &middot; Contentment</a> &mdash; the four trifles this '
        "discourse builds on.",
        '<a href="an-4.6.html">AN 4.6 &middot; A Little Learning</a> &mdash; where the Black Plum '
        "River gold simile also appears.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.29 — Dhammapadasutta
# --------------------------------------------------------------------------- #
page(
    29, "Dhammapada", "Footprints of the Dhamma",
    vagga=VAGGA_3,
    meta_title="AN 4.29 — Footprints of the Dhamma | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dhammapadasutta — "
        "contentment, good will, right mindfulness, and right immersion: four footprints of the "
        "Dhamma, primordial and uncorrupted. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_3),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of four inside a repeated frame, and one verse"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "The four <em>dhammapada</em> recur across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; four words in a large frame, and "
                       "the frame is borrowed"),
    ],
    why=(
        "Four items only: contentment, good will, right mindfulness, right immersion. They arrive "
        "inside exactly the frame AN 4.28 used for the noble traditions &mdash; primordial, "
        "long-standing, traditional, ancient, uncorrupted &mdash; and the discourse says nothing "
        "further about any of them. The interest is in the selection, and in the word "
        "<em>dhammapada</em>, which is more concrete than it looks."),
    guide=[
        ("The teaching in one sentence", [
            "Four things &mdash; contentment, good will, mindfulness, immersion &mdash; are where the "
            "teaching has left its mark, and nobody sensible disputes them."]),
        ("What a <em>dhammapada</em> is", [
            "<em>Pada</em> is a foot, a footprint, a track, and by extension a step or a line of "
            "verse. Sujato&rsquo;s &lsquo;footprints of the Dhamma&rsquo; takes the concrete sense, "
            "and it is the right choice for this discourse: these are the places where the teaching "
            "shows.",
            "The same word gives the Dhammapada its name, where it is usually rendered by way of the "
            "&lsquo;verse&rsquo; sense. Knowing both senses is useful. A <em>pada</em> is what "
            "something leaves behind, and a line of verse is what a teaching leaves behind in "
            "memory.",
            "AN 3.2, in the Threes, said that wisdom shines in its traces &mdash; <em>apadāna</em>, "
            "from the same root. This discourse names four traces and does not argue for them."]),
        ("The selection", [
            "Contentment (<em>anabhijjhā</em>, literally non-covetousness), good will "
            "(<em>abyāpāda</em>, non-ill-will), right mindfulness, and right immersion. Note that the "
            "first two are stated negatively in the Pāli and positively in the English.",
            "The set is a compressed path. The first two are the negations of the first two "
            "unwholesome roots as they show up in conduct; the second two are the last two factors of "
            "the eightfold path. So: what must not be there, and what must be. Greed and hatred "
            "absent, mindfulness and immersion present.",
            "Delusion, the third root, is not on the list, and its absence is worth noticing. The "
            "counter to delusion is wisdom, which arises from the two positive members rather than "
            "standing alongside them. The list is arranged so that the fourth item is the one from "
            "which the missing thing comes."]),
        ("The borrowed frame", [
            "Every word of the surrounding formula is AN 4.28&rsquo;s. Primordial, long-standing, "
            "traditional, ancient; uncorrupted since the beginning, not being corrupted now, not "
            "going to be; sensible ascetics and brahmins do not look down on them.",
            "Two discourses in a row, the same frame, different contents. This is the "
            "Aṅguttara&rsquo;s method in its clearest form, and the two lists are genuinely "
            "different: AN 4.28 gave practices of the monastic life, this gives qualities of any "
            "mind. The frame asserts of both that they are the durable part.",
            "The claim that <em>sensible ascetics and brahmins do not look down on them</em> is the "
            "most interesting element. It is an appeal to cross-sectarian agreement: whatever else "
            "the schools dispute, no reputable teacher of any of them disparages contentment, good "
            "will, mindfulness, or composure. AN 4.30, the next discourse, will take that claim and "
            "turn it into a challenge."]),
        ("The abbreviation", [
            "The Pāli here is abbreviated almost to nothing &mdash; the four are named once and the "
            "frame is restated, with the intermediate expansion left out entirely. Sujato&rsquo;s "
            "translation preserves the gaps.",
            "In performance each of the four would have been expanded with its own definition, as "
            "AN 4.28&rsquo;s items are. What survives on the page is a skeleton. That is worth saying "
            "plainly rather than treating the brevity as significant in itself: this discourse is "
            "short because it was written down short, not because it was taught short."]),
        ("The verse", [
            "One verse, four lines, and it converts the list into an instruction: live with "
            "contentment, and a heart of good will, mindful, with unified mind, serene within.",
            "That is the whole discourse made usable, and it is the part worth memorizing. The four "
            "items in order, in the imperative, with one addition &mdash; <em>ajjhattaṁ susamāhita</em>, "
            "well composed within &mdash; which restates the fourth item as an interior condition "
            "rather than an attainment."]),
    ],
    terms=[
        ("dhammapada",
         "&ldquo;footprint of the Dhamma&rdquo; &mdash; <em>pada</em> is a foot or track, and by "
         "extension a step or a line of verse. Here the concrete sense: where the teaching shows."),
        ("anabhijjhā",
         "&ldquo;contentment&rdquo;, literally non-covetousness &mdash; stated negatively in the "
         "Pāli, positively in the English."),
        ("abyāpāda",
         "&ldquo;good will&rdquo;, literally non-ill-will &mdash; the second of the pair of absences "
         "that opens the list."),
        ("sammāsati / sammāsamādhi",
         "&ldquo;right mindfulness&rdquo; and &ldquo;right immersion&rdquo; &mdash; the last two "
         "factors of the eightfold path, and the two presences that close the list."),
        ("susamāhita",
         "&ldquo;well composed&rdquo; &mdash; the verse&rsquo;s addition, restating immersion as an "
         "interior condition rather than an attainment."),
    ],
    text_intro=(
        "The discourse in full: the four footprints and the verse. The gaps are the Pāli&rsquo;s own "
        "abbreviation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four footprints of the Dhamma"),
        ("p", "&sect;1", "an4.29:1.1-1.3"),
        ("p", "&sect;2", "an4.29:2.1-4.2"),
        ("h3", "The verse"),
        ("p", "&sect;3", "an4.29:5.1-5.4"),
    ],
    quiz=[
        {"q": "What are the four footprints of the Dhamma?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Contentment, good will, right mindfulness, and right immersion",
             "The four noble traditions",
             "The four right efforts"],
         "correct": 1,
         "expl": "Two absences and two presences."},
        {"q": "What does <em>pada</em> mean?",
         "opts": [
             "Teaching",
             "A foot, a footprint, a track &mdash; and by extension a step or a line of verse",
             "Truth",
             "Path"],
         "correct": 1,
         "expl": "The same word that gives the Dhammapada its name."},
        {"q": "Which discourse of the Threes uses a related word for traces?",
         "opts": [
             "AN 3.1",
             "AN 3.2 &mdash; wisdom shines in its traces, <em>apadāna</em>",
             "AN 3.65",
             "AN 3.100"],
         "correct": 1,
         "expl": "From the same root."},
        {"q": "How are the first two items stated in the Pāli?",
         "opts": [
             "Positively",
             "Negatively &mdash; non-covetousness and non-ill-will",
             "In verse only",
             "As imperatives"],
         "correct": 1,
         "expl": "The English renders them positively."},
        {"q": "How does the guide describe the set as a whole?",
         "opts": [
             "As four unrelated virtues",
             "As a compressed path &mdash; greed and hatred absent, mindfulness and immersion present",
             "As monastic requisites",
             "As stages of attainment"],
         "correct": 1,
         "expl": "What must not be there, and what must be."},
        {"q": "Why is delusion not on the list?",
         "opts": [
             "It was forgotten",
             "Its counter is wisdom, which arises from the two positive members rather than standing alongside them",
             "It is covered by contentment",
             "It is not an unwholesome root"],
         "correct": 1,
         "expl": "The list is arranged so the fourth item is where the missing thing comes from."},
        {"q": "Where does the surrounding formula come from?",
         "opts": [
             "The Vinaya",
             "AN 4.28, word for word &mdash; the same frame with different contents",
             "The verses",
             "A commentary"],
         "correct": 1,
         "expl": "The Aṅguttara&rsquo;s method in its clearest form."},
        {"q": "What is notable about &lsquo;sensible ascetics and brahmins do not look down on them&rsquo;?",
         "opts": [
             "It is a threat",
             "It is an appeal to cross-sectarian agreement &mdash; no reputable teacher of any school disparages these four",
             "It excludes non-Buddhists",
             "It is a later addition"],
         "correct": 1,
         "expl": "AN 4.30 will turn that claim into a challenge."},
        {"q": "Why is the discourse so short on the page?",
         "opts": [
             "Because it was taught briefly",
             "Because it was written down abbreviated &mdash; in performance each item would have been expanded with its own definition",
             "Because the text is damaged",
             "Because the verse replaces the prose"],
         "correct": 1,
         "expl": "Worth saying plainly rather than treating the brevity as significant."},
        {"q": "What does the verse add to the list?",
         "opts": [
             "A fifth item",
             "The imperative, and <em>well composed within</em> &mdash; immersion restated as an interior condition rather than an attainment",
             "A simile",
             "A setting"],
         "correct": 1,
         "expl": "The whole discourse made usable, and the part worth memorizing."},
    ],
    marginalia=[
        ("The four", [
            "contentment",
            "good will",
            "right mindfulness",
            "right immersion",
        ]),
        ("Two and two", [
            "greed absent",
            "hatred absent",
            "mindfulness present",
            "immersion present",
        ]),
        ("The word", [
            "<span class=\"pali\">pada</span>footprint",
            "also: a line of verse",
            "&mdash; what is left behind",
        ]),
        ("Cross-references", [
            "AN 4.28 &middot; the same frame",
            "AN 4.30 &middot; next: the challenge",
            "AN 3.2 &middot; wisdom in its traces",
        ]),
    ],
    further=[
        '<a href="%s/an4.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.30.html">AN 4.30 &middot; Wanderers</a> &mdash; next in this series, where '
        "these same four are put to a public challenge.",
        '<a href="an-4.28.html">AN 4.28 &middot; The Noble Traditions</a> &mdash; the discourse whose '
        "frame this one borrows.",
        '<a href="an-3.2.html">AN 3.2 &middot; Characteristics</a> &mdash; on wisdom shining in its '
        "traces.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.30 — Paribbājakasutta
# --------------------------------------------------------------------------- #
page(
    30, "Paribbājaka", "Wanderers",
    vagga=VAGGA_3,
    meta_title="AN 4.30 — Wanderers | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paribbājakasutta — the "
        "Buddha takes the four footprints of the Dhamma to a monastery of rival wanderers and "
        "challenges anyone to deny them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture&rsquo;s Peak; the Buddha goes to the wanderers&rsquo; "
                    "monastery on the bank of the Sappinī, where Annabhāra, Varadhara, Sakuludāyī "
                    "and others were staying"),
        ("Speakers", "The Buddha, addressing an audience of non-Buddhist wanderers"),
        ("Form", "The four footprints restated, a challenge issued four times, four grounds of "
                 "rebuttal, a historical observation, and a verse"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "The <em>dhammapada</em> challenge appears in the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the argument is simple and the "
                       "rhetorical situation is what needs explaining"),
    ],
    why=(
        "The Buddha walks into a monastery of rival teachers and issues a challenge: deny any of "
        "these four, and describe for me a true ascetic who covets, or hates, or is unmindful, or "
        "is scattered. <em>Let them come, speak, and discuss. We&rsquo;ll see how powerful they "
        "are.</em> It is one of the few discourses that shows the Buddha making a public argument "
        "to outsiders, and the form of the argument is more interesting than its confidence."),
    guide=[
        ("The teaching in one sentence", [
            "The four footprints cannot be denied by anyone who also wants to call someone a genuine "
            "ascetic, because denying them means praising the opposite."]),
        ("The setting matters", [
            "This is not a talk to mendicants. The Buddha comes out of retreat, walks to the "
            "<em>paribbājakārāma</em> &mdash; the wanderers&rsquo; own residence &mdash; sits on a "
            "seat made ready, and addresses them as <em>wanderers</em>. Three are named, including "
            "Sakuludāyī, who appears elsewhere in the canon in long philosophical exchanges.",
            "The venue is theirs and the audience is not his. Reading the discourse without that in "
            "view makes it sound like triumphalism among friends; reading it with the setting in view "
            "makes it what it is, which is a public argument made on someone else&rsquo;s ground."]),
        ("The shape of the argument", [
            "It is a <em>reductio</em>, and a clean one. If you reject the footprint of contentment, "
            "then you must honor and praise ascetics who covet sensual pleasures with acute lust. If "
            "you reject good will, you must praise those with ill will and malicious intent. And so "
            "for mindfulness and immersion.",
            "The argument does not claim the four are self-evidently good or that the Buddha&rsquo;s "
            "teaching is true. It claims something narrower and much harder to refuse: that these "
            "four are entailed by anyone&rsquo;s notion of a genuine ascetic, whatever else they "
            "hold. Reject them and you are not disagreeing with the Buddha; you are committed to "
            "praising a greedy, hateful, heedless, scattered holy man.",
            "That is why the challenge is safe to issue in a rival monastery. It does not require the "
            "audience to concede anything Buddhist. It only requires them to have a concept of a good "
            "ascetic at all."]),
        ("&ldquo;We&rsquo;ll see how powerful they are&rdquo;", [
            "<em>Passāmi tesaṁ pāṭihīraṁ</em> &mdash; let us see their marvel, their demonstration. "
            "The tone is unmistakably combative, and it would be dishonest to soften it. This is a "
            "challenge to public debate in a culture where such debates were a serious institution "
            "with reputations attached.",
            "It is worth setting alongside AN 4.25, five discourses earlier, which said the spiritual "
            "life is not lived <em>for the benefit of winning debates</em>. The two are compatible "
            "&mdash; one may argue without arguing for the sake of winning &mdash; but the reader "
            "should feel the friction rather than have it explained away. This discourse is confident "
            "in a way the collection elsewhere warns about."]),
        ("The historical observation", [
            "The most striking sentence comes near the end: even the loud and bold advocates of the "
            "doctrines of no-cause, inaction, and nihilism did not imagine that these four could be "
            "criticized &mdash; <em>for fear of being blamed, provoked, and faulted</em>.",
            "The three named positions are those of the well-known non-Buddhist teachers of the "
            "period: <em>ahetuvāda</em>, that there is no cause; <em>akiriyavāda</em>, that action "
            "has no moral consequence; <em>natthikavāda</em>, that there is nothing after death. "
            "These are the most radical positions available in the debate culture the discourse is "
            "addressing.",
            "And the observation is empirical rather than doctrinal: even they did not attack these "
            "four, and the reason given is social &mdash; fear of blame. The discourse is making an "
            "argument from consensus and is candid that the consensus was enforced by reputation. "
            "That candor is worth pointing out; it is a more sophisticated move than a simple appeal "
            "to universal agreement."]),
        ("The four again, and the verse", [
            "The four are AN 4.29&rsquo;s exactly: contentment, good will, right mindfulness, right "
            "immersion, in the same frame of primordial and uncorrupted. The two discourses are a "
            "pair &mdash; the list stated internally, then the list defended externally.",
            "The verse compresses the four into three lines and adds the label: one who has good "
            "will, ever mindful, serene within, training to remove desire, is called "
            "<em>a diligent one</em>, <em>appamatta</em>. Diligence is the collection&rsquo;s "
            "standard summary virtue, and the four footprints turn out to be its content.",
            "This closes the Uruvelavagga, which began with the newly awakened Buddha wondering what "
            "he could revere and ends with him defending, in a rival monastery, four things nobody "
            "reputable was willing to attack. The chapter is about authority throughout: where it "
            "comes from, who has it, and what it rests on."]),
    ],
    terms=[
        ("paribbājaka",
         "&ldquo;wanderer&rdquo; &mdash; a religious mendicant of any school; here specifically the "
         "non-Buddhist ones whose residence the Buddha visits."),
        ("pāṭihīra",
         "&ldquo;marvel, demonstration&rdquo; &mdash; in the challenge, &lsquo;we&rsquo;ll see how "
         "powerful they are&rsquo;. The tone is combative and the venue is a debate culture."),
        ("ahetuvāda",
         "&ldquo;the doctrine of no cause&rdquo; &mdash; one of the three radical positions named as "
         "having declined to attack these four."),
        ("akiriyavāda",
         "&ldquo;the doctrine of inaction&rdquo; &mdash; that action has no moral consequence; the "
         "second of the three."),
        ("appamatta",
         "&ldquo;diligent&rdquo; &mdash; the verse&rsquo;s label, and the collection&rsquo;s standard "
         "summary virtue, whose content turns out to be these four."),
    ],
    text_intro=(
        "The discourse in full: the visit, the four footprints, the challenge, the four grounds of "
        "rebuttal, the historical observation, and the verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At the wanderers&rsquo; monastery"),
        ("p", "&sect;1", "an4.30:1.1-1.3"),
        ("h3", "Four footprints of the Dhamma"),
        ("p", "&sect;2", "an4.30:2.1-2.5"),
        ("h3", "The challenge"),
        ("p", "&sect;3", "an4.30:3.1-3.4"),
        ("p", "&sect;4", "an4.30:4.1-6.4"),
        ("h3", "Four grounds of rebuttal"),
        ("p", "&sect;5", "an4.30:7.1-7.6"),
        ("p", "&sect;6", "an4.30:8.1-8.4"),
        ("h3", "The verse"),
        ("p", "&sect;7", "an4.30:9.1-9.4"),
    ],
    quiz=[
        {"q": "Where and to whom is this discourse given?",
         "opts": [
             "To mendicants at Sāvatthī",
             "To non-Buddhist wanderers at their own monastery on the bank of the Sappinī, near Rājagaha",
             "To brahmins at Uruvelā",
             "To lay followers at Sāketa"],
         "correct": 1,
         "expl": "The venue is theirs and the audience is not his."},
        {"q": "What shape does the argument take?",
         "opts": [
             "An appeal to scripture",
             "A <em>reductio</em> &mdash; reject a footprint and you are committed to praising its opposite",
             "A syllogism",
             "An appeal to the Buddha&rsquo;s authority"],
         "correct": 1,
         "expl": "Reject good will and you must praise ascetics with malicious intent."},
        {"q": "What does the argument not claim?",
         "opts": [
             "That the four are good",
             "That the four are self-evidently good or that the Buddha&rsquo;s teaching is true &mdash; only that they are entailed by anyone&rsquo;s notion of a genuine ascetic",
             "That wanderers are mistaken",
             "That the four are ancient"],
         "correct": 1,
         "expl": "Which is why the challenge is safe to issue in a rival monastery."},
        {"q": "What does the challenge require of the audience?",
         "opts": [
             "To accept the Buddha as teacher",
             "Only to have a concept of a good ascetic at all",
             "To renounce their own doctrines",
             "To debate publicly"],
         "correct": 1,
         "expl": "It requires no Buddhist concession."},
        {"q": "How does the guide describe the tone of &lsquo;we&rsquo;ll see how powerful they are&rsquo;?",
         "opts": [
             "Gentle",
             "Unmistakably combative &mdash; a challenge to public debate in a culture where debates were a serious institution",
             "Ironic",
             "Conditional"],
         "correct": 1,
         "expl": "It would be dishonest to soften it."},
        {"q": "What friction does the guide flag with AN 4.25?",
         "opts": [
             "None",
             "AN 4.25 said the spiritual life is not lived for the benefit of winning debates",
             "AN 4.25 rejects good will",
             "AN 4.25 was addressed to wanderers"],
         "correct": 1,
         "expl": "Compatible, but the reader should feel the friction rather than have it explained away."},
        {"q": "What three doctrines are named at the end?",
         "opts": [
             "Eternalism, annihilationism, and agnosticism",
             "No-cause, inaction, and nihilism",
             "Fatalism, materialism, and skepticism",
             "Self, world, and soul"],
         "correct": 1,
         "expl": "The most radical positions available in the period&rsquo;s debate culture."},
        {"q": "What reason is given for their not attacking the four?",
         "opts": [
             "That they agreed with them",
             "Fear of being blamed, provoked, and faulted &mdash; a social reason",
             "That they had not heard of them",
             "That they were forbidden to"],
         "correct": 1,
         "expl": "An argument from consensus, candid that the consensus was enforced by reputation."},
        {"q": "Why does the guide call that candor sophisticated?",
         "opts": [
             "Because it flatters the opponents",
             "Because it is a more careful move than a simple appeal to universal agreement",
             "Because it cites sources",
             "Because it names individuals"],
         "correct": 1,
         "expl": "The observation is empirical rather than doctrinal."},
        {"q": "How does the chapter close, and what has it been about?",
         "opts": [
             "With a list of requisites; about the monastic life",
             "With a public defense of four things nobody reputable would attack &mdash; and the chapter has been about authority throughout",
             "With a verse on rebirth; about cosmology",
             "With the Buddha&rsquo;s biography"],
         "correct": 1,
         "expl": "It began with the newly awakened Buddha wondering what he could revere."},
    ],
    marginalia=[
        ("The venue", [
            "the wanderers&rsquo; own monastery",
            "Annabhāra, Varadhara, Sakuludāyī",
            "&mdash; not his audience",
        ]),
        ("The reductio", [
            "deny contentment",
            "&rarr; praise the covetous",
            "deny good will",
            "&rarr; praise the malicious",
        ]),
        ("The observation", [
            "even no-cause, inaction, nihilism",
            "did not attack these four",
            "&mdash; for fear of blame",
        ]),
        ("Cross-references", [
            "AN 4.29 &middot; the list stated internally",
            "AN 4.25 &middot; not for winning debates",
            "AN 4.21 &middot; where the chapter began",
        ]),
    ],
    further=[
        '<a href="%s/an4.30/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.29.html">AN 4.29 &middot; Footprints of the Dhamma</a> &mdash; the same four, '
        "stated to mendicants.",
        '<a href="an-4.25.html">AN 4.25 &middot; The Spiritual Life</a> &mdash; on not living for the '
        "sake of winning debates.",
        '<a href="an-4.21.html">AN 4.21 &middot; At Uruvelā (1st)</a> &mdash; where this chapter '
        "began, with a Buddha looking for something to revere.",
    ],
)


# --------------------------------------------------------------------------- #
# Cakkavagga — the fourth chapter of the Fours
# --------------------------------------------------------------------------- #
VAGGA_4 = "<em>Cakkavagga</em> &mdash; the fourth chapter of the Fours"
SETTING_4 = ("None stated; the Cakkavagga gives no location for this discourse, and it is addressed "
             "to the mendicants directly")


# --------------------------------------------------------------------------- #
# AN 4.31 — Cakkasutta
# --------------------------------------------------------------------------- #
page(
    31, "Cakka", "Situations",
    vagga=VAGGA_4,
    meta_title="AN 4.31 — Situations | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Cakkasutta — a suitable "
        "region, reliance on true persons, right resolve, and past merit: the four wheels on which "
        "a life runs. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_4),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of four with a stated result, and one verse"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "The four <em>cakka</em> appear across the Chinese Āgamas as a "
                              "condition-set for worldly success; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a short list whose fourth item "
                       "needs discussing"),
    ],
    why=(
        "Four conditions under which a person &mdash; god or human &mdash; comes into great wealth: "
        "living somewhere suitable, keeping company with true persons, being rightly resolved, and "
        "having merit from the past. The Pāli word is <em>cakka</em>, wheel, and it gives the "
        "chapter its name. Three of the four are things one can act on and the fourth is not, and "
        "the list is more interesting for including it than it would be without."),
    guide=[
        ("The teaching in one sentence", [
            "Four conditions have to be in place for a life to prosper, and only three of them are "
            "yours to arrange."]),
        ("Why &lsquo;wheel&rsquo;", [
            "<em>Cakka</em> is a wheel &mdash; the wheel of a cart, and by extension a turning, a "
            "condition, a state of affairs. Sujato&rsquo;s &lsquo;situations&rsquo; takes the "
            "extended sense; other translators have used &lsquo;wheels&rsquo; and kept the image.",
            "The image is worth keeping in view, because a cart needs all its wheels. That is the "
            "implicit logic of the list: these are not four contributing factors that add up, but "
            "four supports of which a missing one stops the vehicle. The discourse does not say this "
            "outright, and it is fair to say the reading comes from the word rather than from the "
            "argument."]),
        ("The first three", [
            "<em>Patirūpadesavāsa</em>, living in a suitable region &mdash; the environment. "
            "<em>Sappurisūpassaya</em>, relying on true persons &mdash; the company. "
            "<em>Attasammāpaṇidhi</em>, being rightly resolved in oneself &mdash; the intention.",
            "Read as a sequence they move from outside to inside: place, then people, then one&rsquo;s "
            "own direction. That is a realistic ordering. A person can change their resolve most "
            "readily, their company with more effort, and their region least easily &mdash; but the "
            "discourse lists them in the order of dependence rather than of difficulty, since the "
            "outer conditions are what make the inner one sustainable.",
            "&lsquo;Suitable region&rsquo; is not defined here. The commentarial tradition glosses it "
            "as a place where the teaching is available and the four assemblies are found, which is a "
            "reasonable reading of what would make a region suitable for the purposes this "
            "collection cares about."]),
        ("The fourth", [
            "<em>Pubbekatapuññatā</em>, having done merit in the past. This is the item that a modern "
            "reader is most likely to want to remove, and it should not be removed quietly.",
            "Taken at face value it says that some part of how a life goes was settled before the "
            "life began, and that no amount of good resolve or good company fully substitutes for it. "
            "That is a claim about luck, expressed in the vocabulary of rebirth, and the collection "
            "makes it without embarrassment.",
            "There is something to be said for its honesty. A list of three would imply that outcomes "
            "follow reliably from choices, which is both false and cruel to people whose choices have "
            "not produced the outcomes. Including the fourth item concedes that the world contains "
            "conditions nobody in this life arranged. Whether one accounts for those conditions by "
            "past lives or by ordinary contingency, the structural point survives: three of the four "
            "are yours to work on, and it is a mistake to treat the fourth as if it were."]),
        ("What is promised", [
            "The stated result is <em>great and abundant wealth</em>, and the verse expands it: grain, "
            "riches, fame, reputation, and happiness. This is a worldly discourse, addressed to gods "
            "and humans alike, and it does not mention the path.",
            "The Aṅguttara contains a good deal of this material and it is better to read it as what "
            "it is than to spiritualize it. The collection addresses lay audiences with lay concerns "
            "and does not treat prosperity as shameful. What it does, consistently, is specify the "
            "conditions &mdash; and two of the four conditions here are moral ones."]),
        ("Using it", [
            "As a diagnostic the list is unusually practical, and it works best asked in order. Is the "
            "place I am in one where the thing I am trying to do is possible? Are the people around me "
            "ones who are doing it? Is my own intention actually pointed at it?",
            "Most people examining a stalled effort look only at the third question. This discourse "
            "puts two environmental conditions ahead of it, which is a corrective worth having: "
            "resolve applied in an unsuitable place among unsuitable company is being asked to do "
            "work that is not its own."]),
    ],
    terms=[
        ("cakka",
         "&ldquo;wheel&rdquo; &mdash; and by extension a turning, a condition, a state of affairs. "
         "The chapter takes its name from this discourse."),
        ("patirūpadesavāsa",
         "&ldquo;living in a suitable region&rdquo; &mdash; undefined here; the commentaries gloss it "
         "as a place where the teaching and the four assemblies are found."),
        ("sappurisūpassaya",
         "&ldquo;relying on true persons&rdquo; &mdash; the second condition, and the one about "
         "company."),
        ("attasammāpaṇidhi",
         "&ldquo;being rightly resolved in oneself&rdquo; &mdash; the third, and the only one wholly "
         "internal."),
        ("pubbekatapuññatā",
         "&ldquo;having done merit in the past&rdquo; &mdash; the fourth, and a claim about luck "
         "expressed in the vocabulary of rebirth."),
    ],
    text_intro=(
        "The discourse in full: the four situations and the verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four situations"),
        ("p", "&sect;1", "an4.31:1.1-1.4"),
        ("h3", "The verse"),
        ("p", "&sect;2", "an4.31:2.1-2.6"),
    ],
    quiz=[
        {"q": "What are the four situations?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Living in a suitable region, relying on true persons, being rightly resolved, and past merit",
             "Giving, kindly words, taking care, and equality",
             "Contentment, good will, mindfulness, and immersion"],
         "correct": 1,
         "expl": "Three that can be acted on, and one that cannot."},
        {"q": "What does <em>cakka</em> literally mean?",
         "opts": [
             "Condition",
             "Wheel &mdash; and by extension a turning or state of affairs",
             "Foundation",
             "Season"],
         "correct": 1,
         "expl": "Which gives the chapter its name."},
        {"q": "What reading does the guide draw from the image, and how does it qualify it?",
         "opts": [
             "That the four turn in sequence &mdash; and this is stated in the text",
             "That a cart needs all its wheels, so a missing one stops the vehicle &mdash; while noting the reading comes from the word rather than the argument",
             "That the four are cyclical &mdash; supported by the verse",
             "That wheels symbolize the Dhamma &mdash; per the commentary"],
         "correct": 1,
         "expl": "The discourse does not say it outright."},
        {"q": "In what order do the first three run?",
         "opts": [
             "Inside to outside",
             "Outside to inside &mdash; place, then people, then one&rsquo;s own direction",
             "By difficulty",
             "By duration"],
         "correct": 1,
         "expl": "Listed in the order of dependence rather than of difficulty."},
        {"q": "How do the commentaries gloss &lsquo;suitable region&rsquo;?",
         "opts": [
             "A fertile country",
             "A place where the teaching is available and the four assemblies are found",
             "A monastery",
             "The Middle Country"],
         "correct": 1,
         "expl": "The discourse itself does not define it."},
        {"q": "What does the fourth item claim?",
         "opts": [
             "That effort is unnecessary",
             "That some part of how a life goes was settled before it began, and no amount of resolve fully substitutes for it",
             "That merit can be transferred",
             "That the past is unknowable"],
         "correct": 1,
         "expl": "A claim about luck, expressed in the vocabulary of rebirth."},
        {"q": "Why does the guide say the fourth item should not be quietly removed?",
         "opts": [
             "Because the commentary forbids it",
             "Because a list of three would imply outcomes follow reliably from choices &mdash; which is false, and cruel to people whose choices have not produced them",
             "Because it is the most important",
             "Because it is the oldest part of the text"],
         "correct": 1,
         "expl": "Including it concedes that the world contains conditions nobody in this life arranged."},
        {"q": "What is promised as the result?",
         "opts": [
             "Awakening",
             "Great and abundant wealth &mdash; grain, riches, fame, reputation, and happiness",
             "Rebirth in heaven",
             "Freedom from illness"],
         "correct": 1,
         "expl": "A worldly discourse, and better read as what it is."},
        {"q": "How does the guide say such material should be handled?",
         "opts": [
             "By spiritualizing it",
             "By reading it as what it is &mdash; the collection addresses lay concerns and does not treat prosperity as shameful, while specifying the conditions",
             "By treating it as inauthentic",
             "By omitting it"],
         "correct": 1,
         "expl": "And two of the four conditions here are moral ones."},
        {"q": "What corrective does the guide draw for a stalled effort?",
         "opts": [
             "Increase resolve",
             "Two environmental conditions come before resolve &mdash; resolve in an unsuitable place among unsuitable company is being asked to do work that is not its own",
             "Wait for past merit to ripen",
             "Change the goal"],
         "correct": 1,
         "expl": "Most people examining a stalled effort look only at the third question."},
    ],
    marginalia=[
        ("Four wheels", [
            "a suitable region",
            "true persons",
            "right resolve",
            "past merit",
        ]),
        ("Three and one", [
            "place, company, intention",
            "&mdash; yours to arrange",
            "and one that is not",
        ]),
        ("Asked in order", [
            "is this place possible?",
            "are these people doing it?",
            "is my intention pointed at it?",
        ]),
        ("Cross-references", [
            "AN 4.32 &middot; next: four ways of being inclusive",
            "AN 4.28 &middot; contentment as portable",
            "AN 4.1 &middot; the four of the training",
        ]),
    ],
    further=[
        '<a href="%s/an4.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.32.html">AN 4.32 &middot; Inclusion</a> &mdash; next in this series.',
        '<a href="an-4.30.html">AN 4.30 &middot; Wanderers</a> &mdash; the discourse that closed the '
        "previous chapter.",
        '<a href="an-4.62.html">AN 4.62 &middot; Debtlessness</a> &mdash; further into the Fours, on '
        "the four happinesses of a lay person.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.32 — Saṅgahasutta
# --------------------------------------------------------------------------- #
page(
    32, "Saṅgaha", "Inclusion",
    vagga=VAGGA_4,
    meta_title="AN 4.32 — Inclusion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṅgahasutta — giving, "
        "kindly words, taking care, and equality: the four ways of being inclusive, and the "
        "linchpin of a moving chariot. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_4),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of four, and three verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four <em>saṅgahavatthu</em> are a standard set across the Chinese "
                              "Āgamas and later Mahāyāna literature; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; four words and a simile, with a "
                       "surprising argument in the second verse"),
    ],
    why=(
        "Four ways of holding people together: giving, kindly words, taking care, and treating "
        "people as equals. The list is short and famous, and the argument attached to it is the "
        "part worth reading. Without these four, the verse says, <em>neither mother nor father "
        "would be respected and honored for what they&rsquo;ve done for their children</em> "
        "&mdash; which is a claim about where obligation itself comes from."),
    guide=[
        ("The teaching in one sentence", [
            "Four practices hold a society together, and without them even the debt to parents would "
            "not be recognized."]),
        ("The four", [
            "<em>Dāna</em>, giving. <em>Peyyavajja</em>, kindly or agreeable speech. "
            "<em>Atthacariyā</em>, taking care &mdash; literally conduct that is for the benefit of "
            "someone. <em>Samānattatā</em>, equality &mdash; literally &lsquo;the state of being of "
            "the same self&rsquo;, treating others as one treats oneself.",
            "The collective term is <em>saṅgahavatthu</em>, grounds of inclusion. <em>Saṅgaha</em> is "
            "gathering together, holding, comprising &mdash; from the same root that gives "
            "<em>saṅgha</em>, an assembly. The four are the means by which people are drawn into and "
            "held within a group.",
            "The last of the four does most of the work and is the easiest to translate flatly. "
            "<em>Samānattatā</em> is not equality as a political principle but the refusal to treat "
            "oneself as a different kind of thing from other people. The verse glosses it as "
            "<em>treating equally in worldly conditions, as they deserve in each case</em>, which "
            "keeps it from collapsing into identical treatment: same standard, applied to different "
            "situations."]),
        ("The linchpin", [
            "<em>Yānassa āṇīva sandhanaṁ</em> &mdash; these are like the linchpin of a moving "
            "chariot. The <em>āṇī</em> is the pin that holds the wheel on the axle: a small piece "
            "with nothing impressive about it, and without it the wheel comes off at speed.",
            "The simile is exact about the kind of importance being claimed. These four are not the "
            "cargo, the horses, or the destination. They are the thing that keeps a moving structure "
            "from disassembling, and their absence is noticed only when everything falls apart."]),
        ("The argument about parents", [
            "The second verse makes a claim that repays a slow reading: if there were no such ways of "
            "being inclusive, neither mother nor father would be respected and honored for what they "
            "have done for their children.",
            "The obvious reading is that parents practise these four toward their children, and so "
            "earn the honor they receive. On that reading the verse says filial respect is a response "
            "to a real history of giving, kind speech, care, and even-handedness &mdash; not a "
            "natural fact and not an unconditional obligation.",
            "That is a striking position for a tradition that elsewhere places parents alongside the "
            "Buddha as recipients of an unrepayable debt (AN 4.4, twenty-eight discourses earlier). "
            "The two are compatible if the debt is understood as incurred rather than automatic, and "
            "reading them together makes both sharper: the debt is enormous, and it is a debt for "
            "something done.",
            "It is honest to note that the Pāli here is compressed and other readings are possible "
            "&mdash; the verse can also be taken as saying that without these four in society "
            "generally, the recognition of parental care would have no soil to grow in. Both readings "
            "make obligation depend on practice rather than on nature."]),
        ("Where the list goes in the tradition", [
            "The four <em>saṅgahavatthu</em> have a long life after this. They are one of the sets "
            "the Mahāyāna takes over wholesale as the bodhisattva&rsquo;s means of gathering beings, "
            "and they appear in Chinese and Tibetan literature in the same order with the same "
            "members.",
            "That durability is easy to explain: the list is entirely about conduct toward others, "
            "requires no doctrinal commitment, and can be practised by anyone in any role. It is one "
            "of the small number of early sets that transferred across the whole of Buddhist "
            "history without modification."]),
        ("Teaching it", [
            "The four make a usable audit for any group &mdash; a family, a team, a community. Is "
            "anything actually given? Is the speech in this room agreeable to be on the receiving end "
            "of? Does anyone act for anyone else&rsquo;s benefit at cost to themselves? And is the "
            "person at the top subject to the same standard as everyone else?",
            "The last question is the one that fails most often, and the discourse&rsquo;s ordering "
            "puts it last for what may be the same reason: it is the hardest, and the other three can "
            "be present without it."]),
    ],
    terms=[
        ("saṅgahavatthu",
         "&ldquo;ground of inclusion&rdquo; &mdash; <em>saṅgaha</em> is gathering or holding "
         "together, from the same root as <em>saṅgha</em>."),
        ("peyyavajja",
         "&ldquo;kindly words&rdquo; &mdash; agreeable speech; the second of the four."),
        ("atthacariyā",
         "&ldquo;taking care&rdquo; &mdash; literally conduct that is for the benefit of someone."),
        ("samānattatā",
         "&ldquo;equality&rdquo;, literally the state of being of the same self &mdash; the refusal "
         "to treat oneself as a different kind of thing from other people."),
        ("āṇī",
         "&ldquo;linchpin&rdquo; &mdash; the pin holding the wheel on the axle. Unimpressive, and "
         "without it the wheel comes off at speed."),
    ],
    text_intro=(
        "The discourse in full: the four ways of being inclusive and the three verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four ways of being inclusive"),
        ("p", "&sect;1", "an4.32:1.1-1.4"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.32:2.1-2.6"),
        ("p", "&sect;3", "an4.32:3.1-3.4"),
        ("p", "&sect;4", "an4.32:4.1-4.4"),
    ],
    quiz=[
        {"q": "What are the four ways of being inclusive?",
         "opts": [
             "Faith, ethics, generosity, and wisdom",
             "Giving, kindly words, taking care, and equality",
             "Contentment, good will, mindfulness, and immersion",
             "Loving-kindness, compassion, joy, and equanimity"],
         "correct": 1,
         "expl": "<em>Dāna, peyyavajja, atthacariyā, samānattatā</em>."},
        {"q": "What does <em>saṅgaha</em> mean?",
         "opts": [
             "Community",
             "Gathering together, holding, comprising &mdash; from the same root as <em>saṅgha</em>",
             "Support",
             "Kindness"],
         "correct": 1,
         "expl": "The four are the means by which people are drawn into and held within a group."},
        {"q": "What does <em>samānattatā</em> literally mean?",
         "opts": [
             "Fairness",
             "&lsquo;The state of being of the same self&rsquo; &mdash; treating others as one treats oneself",
             "Impartiality",
             "Equal shares"],
         "correct": 1,
         "expl": "Not equality as a political principle but the refusal to treat oneself as a different kind of thing."},
        {"q": "How does the verse keep it from collapsing into identical treatment?",
         "opts": [
             "It does not",
             "&lsquo;Treating equally in worldly conditions, as they deserve in each case&rsquo; &mdash; same standard, different situations",
             "By restricting it to monastics",
             "By adding a fifth item"],
         "correct": 1,
         "expl": "A useful qualification."},
        {"q": "What is the <em>āṇī</em>?",
         "opts": [
             "The axle",
             "The linchpin &mdash; the pin holding the wheel on the axle",
             "The yoke",
             "The rim"],
         "correct": 1,
         "expl": "A small piece with nothing impressive about it."},
        {"q": "What kind of importance does that simile claim?",
         "opts": [
             "That the four are the destination",
             "That they keep a moving structure from disassembling, and their absence is noticed only when everything falls apart",
             "That they carry the load",
             "That they set the direction"],
         "correct": 1,
         "expl": "Not the cargo, the horses, or the destination."},
        {"q": "What does the second verse claim about parents?",
         "opts": [
             "That they should be obeyed",
             "That without these four ways of being inclusive, neither mother nor father would be respected for what they have done",
             "That they must be repaid",
             "That they are the first teachers"],
         "correct": 1,
         "expl": "A claim about where obligation itself comes from."},
        {"q": "How does the guide relate this to AN 4.4?",
         "opts": [
             "As a contradiction",
             "As compatible if the debt is understood as incurred rather than automatic &mdash; enormous, and a debt for something done",
             "As two separate traditions",
             "As unrelated"],
         "correct": 1,
         "expl": "Reading them together makes both sharper."},
        {"q": "What second reading of the verse does the guide allow?",
         "opts": [
             "That parents are exempt from the four",
             "That without these four in society generally, the recognition of parental care would have no soil to grow in",
             "That the verse is corrupt",
             "That it applies only to monastics"],
         "correct": 1,
         "expl": "Both readings make obligation depend on practice rather than on nature."},
        {"q": "Why does the guide say the list transferred across all of Buddhist history?",
         "opts": [
             "Because it is short",
             "Because it is entirely about conduct toward others, requires no doctrinal commitment, and can be practised by anyone in any role",
             "Because the Mahāyāna invented it",
             "Because it is easy to memorize"],
         "correct": 1,
         "expl": "It appears in Chinese and Tibetan literature in the same order with the same members."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">dāna</span>giving",
            "<span class=\"pali\">peyyavajja</span>kindly words",
            "<span class=\"pali\">atthacariyā</span>taking care",
            "<span class=\"pali\">samānattatā</span>equality",
        ]),
        ("The simile", [
            "<span class=\"pali\">āṇī</span>linchpin",
            "not the cargo",
            "&mdash; what stops the wheel coming off",
        ]),
        ("The audit", [
            "is anything given?",
            "is the speech bearable?",
            "does anyone act at cost?",
            "is the top held to it?",
        ]),
        ("Cross-references", [
            "AN 4.31 &middot; four wheels of a life",
            "AN 4.33 &middot; next: the lion&rsquo;s roar",
            "AN 4.4 &middot; the debt to parents",
        ]),
    ],
    further=[
        '<a href="%s/an4.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.33.html">AN 4.33 &middot; The Lion</a> &mdash; next in this series.',
        '<a href="an-4.4.html">AN 4.4 &middot; Broken (2nd)</a> &mdash; where parents stand alongside '
        "the Buddha as recipients of an unrepayable debt.",
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; further into the Fours, where '
        "matched conduct is applied to a marriage.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.33 — Sīhasutta
# --------------------------------------------------------------------------- #
page(
    33, "Sīha", "The Lion",
    vagga=VAGGA_4,
    meta_title="AN 4.33 — The Lion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sīhasutta — the lion's roar "
        "scatters the animals, and the teaching of substantial reality frightens the long-lived gods "
        "into discovering they are impermanent. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_4),
        ("Speakers", SPEAKER),
        ("Form", "An extended simile, its application, and four verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The lion simile applied to the Buddha&rsquo;s teaching is widespread "
                              "in the Chinese Āgamas and at SN 22.78; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; vivid, and turning on one "
                       "technical term"),
    ],
    why=(
        "A lion comes out at evening, stretches, looks around, roars three times, and goes hunting "
        "&mdash; and every animal that hears him runs, including elephants that break their "
        "harnesses in terror. Then the application: when a Realized One teaches, the gods who "
        "thought they were permanent hear it and are afraid. The discourse is about who the teaching "
        "is bad news for, and the answer is: whoever has the most to lose."),
    guide=[
        ("The teaching in one sentence", [
            "The teaching of impermanence lands hardest on those whose position is best, because they "
            "are the ones who had most reason to believe they were exempt."]),
        ("The lion", [
            "The simile is unusually detailed and every detail is doing something. The lion emerges "
            "toward evening; he yawns; he surveys the four quarters; he roars three times; and only "
            "then does he set out to hunt.",
            "The roar precedes the hunting. It is not a byproduct of the kill but an announcement "
            "made in advance, and everything that happens to the animals happens on hearing it, "
            "before anything has been done to any of them. That is the structural point the "
            "application depends on: what frightens is the sound, not the injury.",
            "The elephants are the sharpest part. Royal elephants, bound with strong harnesses in "
            "villages, towns, and capital cities &mdash; the most valuable and best-secured animals "
            "in the human world &mdash; break their bonds and lose control of themselves. The image "
            "is deliberately undignified, and it is aimed at exactly the class of beings the "
            "application will name."]),
        ("Substantial reality", [
            "The teaching that produces the effect is stated in the four-truth form, with "
            "<em>sakkāya</em> where suffering usually stands: such is substantial reality, its "
            "origin, its cessation, and the practice leading to its cessation.",
            "<em>Sakkāya</em> is a hard word. Literally something like &lsquo;the existing "
            "body&rsquo; or &lsquo;the own-body&rsquo;, it names the five aggregates considered as "
            "what a person takes themselves to be. Sujato&rsquo;s &lsquo;substantial reality&rsquo; "
            "is an attempt at the sense of a solid, self-standing existence; other translators have "
            "used &lsquo;identity&rsquo; or &lsquo;personal existence&rsquo;. None of the English "
            "options is comfortable and it is better to teach the Pāli alongside whichever is used.",
            "The relevant point for this discourse is that <em>sakkāya</em> is what the gods discover "
            "they are included within. Not that they will die soon &mdash; they are long-lived &mdash; "
            "but that they are the kind of thing that ends at all."]),
        ("What the gods say", [
            "Their reaction is given in their own words and it is worth reading slowly, because the "
            "grammar of each line is the same: <em>It turns out we&rsquo;re impermanent, though we "
            "thought we were permanent.</em> Three times, with three pairs of terms, and then a "
            "summary.",
            "The formula is one of discovery rather than of threat. Nothing has been done to the "
            "gods; they have been informed. What produces the fear is a correction to a belief, and "
            "the belief was about themselves.",
            "This is why the lion simile fits so precisely. In both halves the damage is done by "
            "information arriving, and in both halves the ones most disturbed are the ones with the "
            "most secure position. An animal in a hole has somewhere to go. A royal elephant has been "
            "given every reason to believe it is safe."]),
        ("Who this discourse is for", [
            "Read as consolation it is a strange text; read as a description of who finds the "
            "teaching difficult, it is precise. The people to whom impermanence is genuinely bad news "
            "are those whose lives are going well and are expected to keep going well.",
            "That is a useful thing to say plainly in a teaching setting. A person in difficulty "
            "often finds the first noble truth a relief &mdash; it names what they already know. A "
            "person who is comfortable, admired, and secure hears the same sentence as an attack on "
            "something they were relying on, and the discourse says so without apologizing for it."]),
        ("The lion&rsquo;s roar as a formula", [
            "<em>Sīhanāda</em>, the lion&rsquo;s roar, has already appeared in AN 4.8, where the "
            "Buddha roars it in the assemblies on the strength of his four assurances. Here the "
            "content of the roar is supplied: it is the teaching of <em>sakkāya</em> and its "
            "cessation.",
            "The two discourses together give the formula its full sense. The roar is a public, "
            "unhedged declaration made by someone with nothing outstanding against them, and what it "
            "declares is that nothing anyone is holding on to will last. The image of dominance and "
            "the content of the teaching are not as far apart as they first appear."]),
    ],
    terms=[
        ("sakkāya",
         "&ldquo;substantial reality&rdquo; &mdash; the five aggregates considered as what a person "
         "takes themselves to be. No English rendering is comfortable; the Pāli is worth teaching "
         "alongside."),
        ("sīhanāda",
         "&ldquo;lion&rsquo;s roar&rdquo; &mdash; a public, unhedged declaration; here its content is "
         "supplied, where AN 4.8 gave its grounds."),
        ("aniccā",
         "&ldquo;impermanent&rdquo; &mdash; the first word of the gods&rsquo; discovery, against "
         "<em>nicca</em>, permanent, which is what they had believed."),
        ("dīghāyukā devā",
         "&ldquo;long-lived gods&rdquo; &mdash; beautiful, happy, and lasting long in their palaces; "
         "the beings with the most reason to think themselves exempt."),
        ("uttāsa",
         "&ldquo;terror&rdquo; &mdash; the reaction in both halves of the simile, produced in each "
         "case by information rather than by injury."),
    ],
    text_intro=(
        "The discourse in full: the lion, the application, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The lion"),
        ("p", "&sect;1", "an4.33:1.1-1.9"),
        ("h3", "The Realized One"),
        ("p", "&sect;2", "an4.33:2.1-2.8"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.33:3.1-4.4"),
        ("p", "&sect;4", "an4.33:5.1-6.4"),
    ],
    quiz=[
        {"q": "What does the lion do before hunting?",
         "opts": [
             "Drinks",
             "Emerges at evening, yawns, surveys the four quarters, and roars three times",
             "Circles the herd",
             "Waits until dark"],
         "correct": 1,
         "expl": "The roar precedes the hunting."},
        {"q": "Why does the guide say that ordering matters?",
         "opts": [
             "It shows the lion is patient",
             "Everything that happens to the animals happens on hearing the roar, before anything has been done to them &mdash; what frightens is the sound, not the injury",
             "It marks the time of day",
             "It explains the three roars"],
         "correct": 1,
         "expl": "The structural point the application depends on."},
        {"q": "Why are the royal elephants the sharpest part of the simile?",
         "opts": [
             "They are the largest animals",
             "They are the most valuable and best-secured animals in the human world, and they break their bonds and lose control of themselves",
             "They are sacred",
             "They cannot flee"],
         "correct": 1,
         "expl": "The image is deliberately undignified, and aimed at the beings the application will name."},
        {"q": "What is <em>sakkāya</em>?",
         "opts": [
             "The physical body",
             "The five aggregates considered as what a person takes themselves to be",
             "The world",
             "Rebirth"],
         "correct": 1,
         "expl": "Rendered here &lsquo;substantial reality&rsquo;; no English option is comfortable."},
        {"q": "What do the gods discover?",
         "opts": [
             "That they will die soon",
             "That they are included within substantial reality &mdash; that they are the kind of thing that ends at all",
             "That the Buddha is superior",
             "That their palaces are illusions"],
         "correct": 1,
         "expl": "They are long-lived; that is not the issue."},
        {"q": "What kind of formula is their reaction?",
         "opts": [
             "A lament",
             "A discovery &mdash; a correction to a belief, and the belief was about themselves",
             "A confession",
             "A prayer"],
         "correct": 1,
         "expl": "Nothing has been done to them; they have been informed."},
        {"q": "What does the simile share with its application?",
         "opts": [
             "Animals",
             "In both halves the damage is done by information arriving, and the most disturbed are the ones with the most secure position",
             "An evening setting",
             "A threefold structure"],
         "correct": 1,
         "expl": "An animal in a hole has somewhere to go; a royal elephant has been given every reason to feel safe."},
        {"q": "Who does the guide say finds this teaching genuinely difficult?",
         "opts": [
             "The poor",
             "Those whose lives are going well and are expected to keep going well",
             "The young",
             "Non-Buddhists"],
         "correct": 1,
         "expl": "A person in difficulty often finds the first noble truth a relief."},
        {"q": "Where has the lion&rsquo;s roar appeared earlier in the Fours?",
         "opts": [
             "AN 4.1",
             "AN 4.8, where the Buddha roars it on the strength of his four assurances",
             "AN 4.23",
             "AN 4.30"],
         "correct": 1,
         "expl": "There the grounds; here the content."},
        {"q": "What do the two discourses together give the formula?",
         "opts": [
             "A date",
             "Its full sense &mdash; a public, unhedged declaration by someone with nothing outstanding, declaring that nothing anyone holds on to will last",
             "A monastic application",
             "A cosmological setting"],
         "correct": 1,
         "expl": "The image of dominance and the content are not as far apart as they first appear."},
    ],
    marginalia=[
        ("The lion", [
            "emerges at evening",
            "surveys the four quarters",
            "roars three times",
            "&mdash; then hunts",
        ]),
        ("The elephants", [
            "royal, harnessed",
            "in capital cities",
            "&mdash; and they break loose",
        ]),
        ("The discovery", [
            "&ldquo;it turns out",
            "we&rsquo;re impermanent&rdquo;",
            "&mdash; not a threat, a correction",
        ]),
        ("Cross-references", [
            "AN 4.8 &middot; the roar and its grounds",
            "AN 4.34 &middot; next: the best confidences",
            "AN 4.23 &middot; the world in four truths",
        ]),
    ],
    further=[
        '<a href="%s/an4.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.34.html">AN 4.34 &middot; The Best Kinds of Confidence</a> &mdash; next in '
        "this series.",
        '<a href="an-4.8.html">AN 4.8 &middot; Self-assured</a> &mdash; where the lion&rsquo;s roar '
        "is grounded in the four assurances.",
        '<a href="an-4.23.html">AN 4.23 &middot; The World</a> &mdash; the same four-truth form with '
        "another word in the first place.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.34 — Aggappasādasutta
# --------------------------------------------------------------------------- #
page(
    34, "Aggappasāda", "The Best Kinds of Confidence",
    vagga=VAGGA_4,
    meta_title="AN 4.34 — The Best Kinds of Confidence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Aggappasādasutta — the "
        "Buddha, the eightfold path, fading away, and the Saṅgha: four bests, and confidence in the "
        "best gives the best result. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_4),
        ("Speakers", SPEAKER),
        ("Form", "Four superlatives, each with the same two-line consequence, and four verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The <em>aggappasāda</em> set is widespread across the Chinese Āgamas "
                              "and appears at Iti 90; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; one careful distinction in the "
                       "third item is worth the whole page"),
    ],
    why=(
        "Four things that are the best of their kind, and confidence in the best has the best "
        "result. Three of them are the familiar refuges, in a slightly unfamiliar form: the Buddha "
        "as best of beings, the eightfold path as best of conditioned things, and the Saṅgha as "
        "best of communities. But the third item is not the teaching in general &mdash; it is "
        "specifically <em>fading away</em>, the best of all things conditioned <em>and "
        "unconditioned</em>, and that qualification is the discourse&rsquo;s one piece of technical "
        "precision."),
    guide=[
        ("The teaching in one sentence", [
            "Confidence placed in the best of each category yields the best result, and the four "
            "categories are beings, conditioned things, everything at all, and communities."]),
        ("Best of beings", [
            "The Buddha is best of all sentient beings, and the list of what he is best among is "
            "worth reading in full: footless, two-footed, four-footed, many-footed; with form or "
            "formless; with perception, without perception, or with neither perception nor "
            "non-perception.",
            "That is a complete inventory of the possible modes of existence in this cosmology, "
            "arranged first by body and then by mind. The formless realms and the neither-perception-"
            "nor-non-perception sphere are the highest attainments available to a being who has not "
            "gone beyond rebirth. Naming them here places the Buddha above the ceiling rather than at "
            "the top of the range."]),
        ("Best of conditioned things", [
            "The noble eightfold path is best of all <em>saṅkhata</em>, conditioned things &mdash; "
            "everything that is made, put together, dependent on causes.",
            "This is a carefully bounded claim and the boundary is the interesting part. The path is "
            "not said to be the best thing there is. It is the best thing among things that are made, "
            "which is to say the best available instrument. An instrument is not the goal, and the "
            "discourse is about to name something that is."]),
        ("Best of everything, conditioned or not", [
            "<em>Virāga</em>, fading away, is best of all things <em>whether conditioned or "
            "unconditioned</em> &mdash; and the discourse then gives eight names for it: the quelling "
            "of vanity, the removing of thirst, the abolishing of clinging, the breaking of the "
            "round, the ending of craving, fading away, cessation, extinguishment.",
            "The widened category is the point. Everything else on the list is best within a class; "
            "this is best without qualification, because the class named includes both halves of the "
            "only exhaustive division the tradition recognizes. There is nothing outside "
            "<em>saṅkhata</em> and <em>asaṅkhata</em>.",
            "The eight names are worth teaching as a set. They approach one thing from eight "
            "directions &mdash; conceit, thirst, attachment, rebirth, craving, passion, continuation, "
            "and the fire &mdash; and none of them is a positive description. What is being called "
            "the best of all things is stated exclusively as a series of endings, which is "
            "characteristic and worth pausing on rather than rushing past."]),
        ("Best of communities", [
            "The Saṅgha is best of all <em>gaṇa</em> and <em>parisā</em>, groups and assemblies, and "
            "the definition given is the technical one: the four pairs, the eight individual persons.",
            "That is the noble Saṅgha &mdash; those on and past the four stages, counted as four "
            "pairs (each path and its fruit) or eight individuals. It is not the monastic order as an "
            "institution. This distinction matters for the whole discourse: the confidence being "
            "recommended is not confidence in an organization but in the existence of people who have "
            "actually done this.",
            "The standard formula follows: worthy of offerings, of hospitality, of a religious "
            "donation, of greeting with cupped palms, and the supreme field of merit for the world."]),
        ("What is promised, and to whom", [
            "The verses turn the four confidences into a giving practice and promise a worldly return: "
            "the best lifespan, beauty, fame, reputation, happiness, and strength, whether reborn as "
            "a god or a human.",
            "It is worth being straightforward about the register here. The prose is precise "
            "doctrinal analysis; the verses are an encouragement to donors with a list of rewards. "
            "Both are in the discourse and the collection puts them side by side without "
            "explanation.",
            "The connective that makes them one text is the word <em>agga</em>, best, which appears "
            "in every clause of both halves. Confidence in the best, giving to the best, the best of "
            "merit, the best results. Whatever else it is, the discourse is a sustained piece of "
            "rhetoric built on a single word, and hearing it repeated is most of the experience of "
            "reciting it."]),
    ],
    terms=[
        ("aggappasāda",
         "&ldquo;the best kind of confidence&rdquo; &mdash; <em>pasāda</em> is confidence or clarity "
         "of heart, and <em>agga</em> is the word that runs through every clause."),
        ("saṅkhata / asaṅkhata",
         "&ldquo;conditioned&rdquo; and &ldquo;unconditioned&rdquo; &mdash; the only exhaustive "
         "division the tradition recognizes, which is why the third item&rsquo;s claim is "
         "unqualified."),
        ("virāga",
         "&ldquo;fading away&rdquo; &mdash; given eight names here, all of them endings, and called "
         "best of all things whatever."),
        ("cattāri purisayugāni",
         "&ldquo;the four pairs&rdquo; &mdash; each path with its fruit, counted also as the eight "
         "individual persons; the noble Saṅgha rather than the institution."),
        ("puññakkhetta",
         "&ldquo;field of merit&rdquo; &mdash; the standing image for a recipient in whom a gift "
         "grows; here the Saṅgha is called the supreme one."),
    ],
    text_intro=(
        "The discourse in full: the four bests, each with its consequence, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Best of beings"),
        ("p", "&sect;1", "an4.34:1.1-1.5"),
        ("h3", "Best of conditioned things"),
        ("p", "&sect;2", "an4.34:2.1-2.3"),
        ("h3", "Best of all things"),
        ("p", "&sect;3", "an4.34:3.1-3.3"),
        ("h3", "Best of communities"),
        ("p", "&sect;4", "an4.34:4.1-4.4"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.34:5.1-6.4"),
        ("p", "&sect;6", "an4.34:7.1-8.4"),
    ],
    quiz=[
        {"q": "What are the four bests?",
         "opts": [
             "Buddha, Dhamma, Saṅgha, and ethics",
             "The Buddha among beings, the eightfold path among conditioned things, fading away among all things, and the Saṅgha among communities",
             "Ethics, immersion, wisdom, and freedom",
             "Giving, ethics, meditation, and wisdom"],
         "correct": 1,
         "expl": "Three familiar refuges in a slightly unfamiliar form, and one technical item."},
        {"q": "What is notable about the inventory of beings?",
         "opts": [
             "It lists only animals",
             "It is a complete inventory of possible modes of existence, arranged by body and then by mind &mdash; placing the Buddha above the ceiling rather than at the top of the range",
             "It omits humans",
             "It is drawn from the Vinaya"],
         "correct": 1,
         "expl": "Including the formless and neither-perception-nor-non-perception spheres."},
        {"q": "What is the eightfold path said to be best among?",
         "opts": [
             "All things",
             "Conditioned things &mdash; everything made, put together, dependent on causes",
             "Paths taught by ascetics",
             "Practices of the Saṅgha"],
         "correct": 1,
         "expl": "The best available instrument, and an instrument is not the goal."},
        {"q": "Why is the third item&rsquo;s category wider?",
         "opts": [
             "Because fading away is a practice",
             "Because it names both conditioned and unconditioned &mdash; the only exhaustive division the tradition recognizes",
             "Because it includes the gods",
             "Because the verses require it"],
         "correct": 1,
         "expl": "So the claim is best without qualification."},
        {"q": "How is <em>virāga</em> described?",
         "opts": [
             "By a simile",
             "By eight names, all of them endings &mdash; quelling of vanity, removing of thirst, abolishing of clinging, and so on",
             "By its result",
             "By its cause"],
         "correct": 1,
         "expl": "What is called the best of all things is stated exclusively as a series of endings."},
        {"q": "How is the Saṅgha defined here?",
         "opts": [
             "The monastic order",
             "The four pairs, the eight individual persons &mdash; the noble Saṅgha",
             "The four assemblies",
             "All followers of the Buddha"],
         "correct": 1,
         "expl": "Each path with its fruit."},
        {"q": "Why does that distinction matter for the discourse?",
         "opts": [
             "It restricts giving to monastics",
             "The confidence recommended is not confidence in an organization but in the existence of people who have actually done this",
             "It excludes lay followers",
             "It dates the discourse"],
         "correct": 1,
         "expl": "Not the institution."},
        {"q": "What do the verses promise?",
         "opts": [
             "Awakening",
             "The best lifespan, beauty, fame, reputation, happiness, and strength, whether reborn as a god or a human",
             "Rebirth in the Pure Abodes",
             "Nothing"],
         "correct": 1,
         "expl": "An encouragement to donors with a list of rewards."},
        {"q": "How does the guide describe the relation between prose and verse here?",
         "opts": [
             "The verses summarize the prose",
             "The prose is precise doctrinal analysis and the verses are donor encouragement, put side by side without explanation",
             "The verses contradict the prose",
             "The prose depends on the verses"],
         "correct": 1,
         "expl": "Both are in the discourse."},
        {"q": "What holds the two halves together?",
         "opts": [
             "The setting",
             "The word <em>agga</em>, best, which appears in every clause of both halves",
             "The metre",
             "The list of four"],
         "correct": 1,
         "expl": "A sustained piece of rhetoric built on a single word."},
    ],
    marginalia=[
        ("Four bests", [
            "the Buddha &middot; of beings",
            "the path &middot; of the conditioned",
            "fading away &middot; of all",
            "the Saṅgha &middot; of communities",
        ]),
        ("The wider class", [
            "<span class=\"pali\">saṅkhata</span>conditioned",
            "<span class=\"pali\">asaṅkhata</span>unconditioned",
            "&mdash; nothing outside the two",
        ]),
        ("Eight names, all endings", [
            "vanity quelled",
            "thirst removed",
            "clinging abolished",
            "the round broken",
        ]),
        ("Cross-references", [
            "AN 4.33 &middot; who the teaching frightens",
            "AN 4.35 &middot; next: with Vassakāra",
            "AN 4.15 &middot; the other list of foremosts",
        ]),
    ],
    further=[
        '<a href="%s/an4.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.35.html">AN 4.35 &middot; With Vassakāra</a> &mdash; next in this series.',
        '<a href="an-4.15.html">AN 4.15 &middot; Regarded as Foremost</a> &mdash; the other discourse '
        "of the Fours built on superlatives.",
        '<a href="an-4.32.html">AN 4.32 &middot; Inclusion</a> &mdash; the chapter&rsquo;s other '
        "short list with a long afterlife in the tradition.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.35 — Vassakārasutta
# --------------------------------------------------------------------------- #
page(
    35, "Vassakāra", "With Vassakāra",
    vagga=VAGGA_4,
    meta_title="AN 4.35 — With Vassakāra | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vassakārasutta — a chief "
        "minister of Magadha defines the great man by learning and competence, and the Buddha "
        "answers with a different four. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, in the Bamboo Grove, the squirrels&rsquo; feeding ground"),
        ("Speakers", "The Buddha and Vassakāra the brahmin, a chief minister of Magadha"),
        ("Form", "A definition offered, a counter-definition given, an inference drawn, and a "
                 "rebuke, with two verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Exchanges with Vassakāra appear across the Chinese Āgamas, notably in "
                              "the Mahāparinibbāna material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a conversation with three moves "
                       "and a sharp closing line"),
    ],
    why=(
        "A senior politician proposes a definition of the great man: broad learning, grasp of "
        "meaning, a long memory, and competence in getting things done. It is an excellent "
        "definition of a useful minister. The Buddha declines to agree or disagree and offers "
        "another four &mdash; and then, when Vassakāra applies them to him, tells him his words are "
        "<em>invasive and intrusive</em> before confirming every one."),
    guide=[
        ("The teaching in one sentence", [
            "Two definitions of greatness are placed side by side, one of capacity and one of "
            "attainment, and the second is confirmed only under protest."]),
        ("Who Vassakāra is", [
            "A chief minister of Magadha under King Ajātasattu, and one of the more consequential lay "
            "figures in the canon. He appears at the opening of the Mahāparinibbāna material, sent to "
            "ask whether the king can defeat the Vajjis, and is associated with the fortification of "
            "Pāṭaliputta.",
            "He is not a disciple and is not portrayed as one. He is an able administrator making "
            "conversation with a famous teacher, and the definition he proposes is exactly what a man "
            "in his position would admire."]),
        ("His four", [
            "Very learned in diverse fields; able to explain what statements mean; mindful, in the "
            "sense of remembering what was said and done long ago; and deft and tireless in household "
            "duties, understanding how to organize and complete work.",
            "This is a description of administrative excellence and it is a good one. Note that the "
            "third item uses <em>sati</em> in its plain sense of memory rather than in the technical "
            "sense the tradition gives it, which is a useful reminder that the word had ordinary "
            "usage.",
            "&ldquo;If the worthy Gotama agrees with me, please say so. If he disagrees, please say "
            "so.&rdquo; The framing is a politician&rsquo;s: a direct request for endorsement, with "
            "both options offered."]),
        ("&ldquo;I neither agree nor disagree&rdquo;", [
            "The refusal of the frame is the discourse&rsquo;s first real move. Vassakāra has offered "
            "a binary and the Buddha steps out of it, then supplies his own account without "
            "criticizing the one he was given.",
            "That is worth noticing as a conversational technique. Nothing in Vassakāra&rsquo;s list "
            "is denied; it is simply not the subject. The four qualities the Buddha names are about "
            "something else, and the disagreement, such as it is, is about what the phrase "
            "&lsquo;great man of great wisdom&rsquo; should be reserved for."]),
        ("The Buddha&rsquo;s four", [
            "Practising for the welfare and happiness of the people; having established many in the "
            "principles of goodness and skillfulness; mastery of the paths of thought &mdash; "
            "thinking what one wants to think and not what one does not; the four absorptions at "
            "will; and the ending of defilements.",
            "Counted strictly that is five items in four slots, with mental mastery and the "
            "absorptions grouped together; the Pāli treats them as one. The set moves outward to "
            "inward, opposite to Vassakāra&rsquo;s, which stayed entirely in the domain of capability.",
            "The first two are the striking ones. Greatness begins, on this account, with acting for "
            "others and establishing others &mdash; not with attainment. The private qualities come "
            "third and fourth. A reader expecting the tradition to define greatness by meditative "
            "achievement should notice which items were put first."]),
        ("&ldquo;Invasive and intrusive&rdquo;", [
            "Vassakāra immediately applies all four to the Buddha himself, in the form of a "
            "compliment. The reply is <em>abhinipātī kho tyāyaṁ brāhmaṇa vācā abhinippīḷā</em> "
            "&mdash; your words are clearly invasive and intrusive. <em>Nevertheless, I will answer "
            "you.</em> And then he confirms every item in the first person.",
            "The rebuke is real and should not be softened. Vassakāra has done something socially "
            "clumsy: he has put a claim of attainment into another person&rsquo;s mouth by "
            "attributing it, which leaves that person either accepting praise or publicly denying it. "
            "It is a form of pressure and the discourse names it.",
            "That the Buddha then confirms the four anyway is the more interesting half. He does not "
            "avoid the question to preserve modesty. He objects to the manner and answers the "
            "substance, which is a distinction worth teaching: the objection was to being maneuvered, "
            "not to the truth being stated.",
            "It is also a useful corrective to a reading of the canon in which the Buddha is "
            "unfailingly serene. He is depicted here as finding a conversational move objectionable "
            "and saying so."]),
    ],
    terms=[
        ("mahāpañña",
         "&ldquo;of great wisdom&rdquo; &mdash; the phrase both speakers are defining, and the thing "
         "actually in dispute."),
        ("Vassakāra",
         "a chief minister of Magadha under Ajātasattu, associated with the fortification of "
         "Pāṭaliputta and with the embassy about the Vajjis."),
        ("sati",
         "&ldquo;mindfulness&rdquo; &mdash; used by Vassakāra in its plain sense of memory, a useful "
         "reminder that the word had ordinary usage."),
        ("vitakkapatha",
         "&ldquo;paths of thought&rdquo; &mdash; what the third quality claims mastery over: thinking "
         "what one wants to think and not what one does not."),
        ("abhinipātī vācā",
         "&ldquo;invasive words&rdquo; &mdash; the rebuke, for putting a claim of attainment into "
         "another person&rsquo;s mouth by attributing it."),
    ],
    text_intro=(
        "The discourse in full: Vassakāra&rsquo;s definition, the Buddha&rsquo;s, the application, "
        "the rebuke, and the verses. The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "an4.35:1.1-1.3"),
        ("h3", "Vassakāra&rsquo;s four"),
        ("p", "&sect;2", "an4.35:2.1-2.9"),
        ("h3", "The Buddha&rsquo;s four"),
        ("p", "&sect;3", "an4.35:3.1-3.12"),
        ("h3", "The application, and the rebuke"),
        ("p", "&sect;4", "an4.35:4.1-4.9"),
        ("p", "&sect;5", "an4.35:5.1-5.8"),
        ("h3", "The verses"),
        ("p", "&sect;6", "an4.35:6.1-6.6"),
        ("p", "&sect;7", "an4.35:7.1-7.4"),
    ],
    quiz=[
        {"q": "Who is Vassakāra?",
         "opts": [
             "A disciple of the Buddha",
             "A chief minister of Magadha, associated with the embassy about the Vajjis and the fortification of Pāṭaliputta",
             "A wanderer",
             "A brahmin teacher"],
         "correct": 1,
         "expl": "Not a disciple, and not portrayed as one."},
        {"q": "What four qualities does he propose?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Broad learning, grasp of what statements mean, a long memory, and competence in getting work done",
             "Giving, kindly words, care, and equality",
             "Faith, energy, mindfulness, and immersion"],
         "correct": 1,
         "expl": "A description of administrative excellence, and a good one."},
        {"q": "What is notable about his use of <em>sati</em>?",
         "opts": [
             "He misuses it",
             "He uses it in its plain sense of memory rather than the technical sense &mdash; a reminder that the word had ordinary usage",
             "He omits it",
             "He borrows it from the Buddha"],
         "correct": 1,
         "expl": "Remembering what was said and done long ago."},
        {"q": "How does the Buddha respond to the request for endorsement?",
         "opts": [
             "He agrees",
             "He neither agrees nor disagrees, and supplies his own account without criticizing the one he was given",
             "He disagrees",
             "He stays silent"],
         "correct": 1,
         "expl": "Vassakāra offered a binary and the Buddha steps out of it."},
        {"q": "What comes first in the Buddha&rsquo;s four?",
         "opts": [
             "The four absorptions",
             "Practising for the welfare and happiness of the people, and having established many in goodness and skillfulness",
             "The ending of defilements",
             "Mastery of thought"],
         "correct": 1,
         "expl": "A reader expecting greatness to be defined by meditative achievement should notice which items were put first."},
        {"q": "How do the two lists differ in direction?",
         "opts": [
             "They do not differ",
             "Vassakāra&rsquo;s stays in the domain of capability; the Buddha&rsquo;s moves from outward to inward",
             "The Buddha&rsquo;s is shorter",
             "Vassakāra&rsquo;s is about attainment"],
         "correct": 1,
         "expl": "Acting for others first, private qualities after."},
        {"q": "What does the Buddha say about Vassakāra&rsquo;s compliment?",
         "opts": [
             "That it is well spoken",
             "That his words are clearly invasive and intrusive",
             "That it is untrue",
             "Nothing"],
         "correct": 1,
         "expl": "The rebuke is real and should not be softened."},
        {"q": "Why is the compliment objectionable?",
         "opts": [
             "It is inaccurate",
             "It puts a claim of attainment into another person&rsquo;s mouth by attributing it, leaving them to accept praise or publicly deny it",
             "It is too public",
             "It is flattery of a patron"],
         "correct": 1,
         "expl": "A form of pressure, and the discourse names it."},
        {"q": "What does the Buddha do after the rebuke?",
         "opts": [
             "Changes the subject",
             "Confirms every item in the first person",
             "Denies the qualities",
             "Ends the conversation"],
         "correct": 1,
         "expl": "He objects to the manner and answers the substance."},
        {"q": "What corrective does the guide draw from the exchange?",
         "opts": [
             "That modesty requires denial",
             "That the canon does not depict the Buddha as unfailingly serene &mdash; he finds a conversational move objectionable and says so",
             "That ministers should not ask questions",
             "That claims of attainment are forbidden"],
         "correct": 1,
         "expl": "The objection was to being maneuvered, not to the truth being stated."},
    ],
    marginalia=[
        ("His four", [
            "much learning",
            "grasp of meaning",
            "long memory",
            "competence at work",
        ]),
        ("His four", [
            "for the welfare of the people",
            "establishing many",
            "mastery of thought",
            "the absorptions, and the end",
        ]),
        ("The rebuke", [
            "&ldquo;invasive and intrusive&rdquo;",
            "&ldquo;nevertheless,",
            "I will answer you&rdquo;",
        ]),
        ("Cross-references", [
            "AN 4.22 &middot; another definition contested",
            "AN 4.36 &middot; next: with Doṇa",
            "AN 4.8 &middot; claims made in the first person",
        ]),
    ],
    further=[
        '<a href="%s/an4.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.36.html">AN 4.36 &middot; Doṇa</a> &mdash; next in this series, and the other '
        "conversation with a brahmin in this chapter.",
        '<a href="an-4.22.html">AN 4.22 &middot; At Uruvelā (2nd)</a> &mdash; the other discourse in '
        "which a brahmin&rsquo;s definition is refused.",
        '<a href="an-4.8.html">AN 4.8 &middot; Self-assured</a> &mdash; on what the Buddha will say '
        "of himself, and how.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.36 — Doṇasutta
# --------------------------------------------------------------------------- #
page(
    36, "Doṇa", "Doṇa",
    vagga=VAGGA_4,
    meta_title="AN 4.36 — Doṇa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Doṇasutta — a brahmin "
        "follows wheel-marked footprints, asks whether the Buddha is a god, a spirit, or a human, "
        "and is told: remember me as a Buddha. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "On the road between Ukkaṭṭhā and Setavyā, and then at the root of a tree beside "
                    "it"),
        ("Speakers", "The Buddha and Doṇa the brahmin"),
        ("Form", "A narrative approach, four questions with four refusals, a lotus simile, and two "
                 "verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The Doṇa episode is well represented in the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; famous, short, and turning "
                       "entirely on a verb tense"),
    ],
    why=(
        "One of the best-known exchanges in the canon. A brahmin sees footprints marked with "
        "thousand-spoked wheels, follows them, and asks the man sitting at the tree whether he is a "
        "god, a centaur, a spirit, or a human. Four questions, four refusals &mdash; and the refusal "
        "is in the future tense. Everything interesting about this discourse is in that tense, and "
        "most retellings lose it."),
    guide=[
        ("The teaching in one sentence", [
            "Asked what kind of being he is, the Buddha answers that he will not <em>become</em> any "
            "of them, because the defilements that would produce such a rebirth are gone."]),
        ("The footprints", [
            "Doṇa sees the wheel-marks and concludes these could not be a human being&rsquo;s. That "
            "is the premise of the whole conversation: he has already decided the answer is not "
            "&lsquo;human&rsquo; before he asks anything.",
            "The wheel on the sole is one of the thirty-two marks of a great man, a piece of "
            "brahminical lore the canon repeatedly puts in the mouths of brahmins. It is worth noting "
            "that the text does not argue for the marks; it uses them as the reason a brahmin gets "
            "interested, which is a slightly different thing from asserting them.",
            "What Doṇa then finds is described carefully, and the description is not marvellous: "
            "sitting cross-legged, body straight, mindfulness present, faculties peaceful, "
            "self-controlled, like a tamed elephant. The extraordinary sign leads to an ordinary "
            "posture, and the discourse spends more words on the composure than on the miracle."]),
        ("The verb", [
            "&ldquo;Might you be a god?&rdquo; &mdash; <em>&ldquo;I will not be a god, "
            "brahmin.&rdquo;</em> The Pāli is <em>na kho ahaṁ brāhmaṇa devo bhavissāmi</em>, and "
            "<em>bhavissāmi</em> is future: I will not become.",
            "Sujato keeps the tense, and it changes the discourse completely. The common rendering "
            "&mdash; &lsquo;I am not a god&rsquo; &mdash; makes this a text about what the Buddha "
            "mysteriously is. With the future tense it becomes a text about rebirth: he is not going "
            "to be reborn as any of these, because he is not going to be reborn.",
            "The explanation confirms it. <em>If I had not given up defilements I might have become a "
            "god, a centaur, a spirit, or a human. But I have given up those defilements.</em> The "
            "four categories are four possible destinations, and the answer is that none of them "
            "applies because there is no further destination at all.",
            "This is a case where a translation choice carries the meaning, and it is worth showing "
            "students both versions. The mystical reading is not available once the tense is "
            "restored."]),
        ("The four categories", [
            "God (<em>deva</em>), centaur (<em>gandhabba</em>), spirit (<em>yakkha</em>), human "
            "(<em>manussa</em>). These are four of the possible rebirth destinations in the "
            "cosmology, running from the highest downward and ending with the ordinary.",
            "Doṇa is asking a taxonomic question in good faith. Given the footprints, something "
            "non-ordinary is in front of him, and his framework has a slot for that. The "
            "discourse&rsquo;s answer is that the framework has no slot, not because the Buddha is "
            "more exalted than the highest slot but because he has stepped out of the system the "
            "slots belong to."]),
        ("The lotus", [
            "<em>Though it sprouted and grew in the water, it would rise up above the water and stand "
            "with no water clinging to it. In the same way, though I was born and grew up in the "
            "world, I live having mastered the world, unsullied by the world.</em>",
            "The simile answers the question Doṇa actually asked, in a way the negations did not. It "
            "concedes the origin fully &mdash; born in the world, grew up in it, sprouted in the "
            "water &mdash; and locates the difference entirely in the present relationship. Nothing "
            "about the lotus&rsquo;s substance differs from the water it grew in.",
            "That is a deflationary image in the best sense. It rules out the reading that the Buddha "
            "is made of some other material, which is precisely the reading the footprints had "
            "invited."]),
        ("&ldquo;Remember me as a Buddha&rdquo;", [
            "<em>Buddhoti maṁ brāhmaṇa dhārehi</em> &mdash; hold me in mind as a Buddha. The word is "
            "offered as the answer to &lsquo;what are you?&rsquo;, and it is a term for someone who "
            "has done something rather than for a kind of being.",
            "That is the discourse&rsquo;s resolution and it is a category shift rather than an "
            "answer within the category. Doṇa asked which of four species; he is told the relevant "
            "word names an achievement.",
            "For teaching, this pairs naturally with AN 4.15 and AN 4.34, both of which place the "
            "Buddha at the top of a list of beings. This discourse says the list is the wrong shape. "
            "The collection contains both moves and it is more honest to show the seam than to "
            "smooth it."]),
    ],
    terms=[
        ("bhavissāmi",
         "&ldquo;I will be, I will become&rdquo; &mdash; the future tense on which the whole "
         "discourse turns, and which most retellings lose."),
        ("gandhabba",
         "&ldquo;centaur&rdquo; &mdash; a class of celestial being; one of the four rebirth "
         "destinations Doṇa proposes."),
        ("āsava",
         "&ldquo;defilement&rdquo; &mdash; what has been given up, cut off at the root, made like a "
         "palm stump, so no further becoming can occur."),
        ("paṇḍarīka",
         "&ldquo;white lotus&rdquo; &mdash; with the blue water lily and pink lotus, the simile that "
         "concedes the origin and locates the difference in the present relationship."),
        ("dhārehi",
         "&ldquo;hold in mind, remember&rdquo; &mdash; <em>remember me as a Buddha</em>: a term for "
         "someone who has done something rather than for a kind of being."),
    ],
    text_intro=(
        "The discourse in full: the footprints, the four questions, the explanation, the lotus, and "
        "the verses. The gaps are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The footprints"),
        ("p", "&sect;1", "an4.36:1.1-1.9"),
        ("h3", "Four questions"),
        ("p", "&sect;2", "an4.36:2.1-2.8"),
        ("p", "&sect;3", "an4.36:3.1-3.9"),
        ("h3", "The lotus"),
        ("p", "&sect;4", "an4.36:4.1-4.5"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.36:5.1-5.6"),
        ("p", "&sect;6", "an4.36:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does Doṇa see, and what does he conclude?",
         "opts": [
             "A halo, and that this is a god",
             "Footprints marked with thousand-spoked wheels, and that these could not be a human being&rsquo;s",
             "A crowd, and that a teacher is present",
             "A robe, and that this is an ascetic"],
         "correct": 1,
         "expl": "He has decided the answer is not &lsquo;human&rsquo; before he asks anything."},
        {"q": "How does the discourse describe what Doṇa finds?",
         "opts": [
             "A marvellous apparition",
             "An ordinary posture &mdash; sitting cross-legged, body straight, faculties peaceful, like a tamed elephant",
             "A teaching in progress",
             "An empty seat"],
         "correct": 1,
         "expl": "The extraordinary sign leads to an ordinary posture."},
        {"q": "What tense is the Buddha&rsquo;s refusal in?",
         "opts": [
             "Present &mdash; &lsquo;I am not&rsquo;",
             "Future &mdash; <em>bhavissāmi</em>, &lsquo;I will not become&rsquo;",
             "Past",
             "Conditional"],
         "correct": 1,
         "expl": "Sujato keeps the tense, and it changes the discourse completely."},
        {"q": "What does the tense make the discourse about?",
         "opts": [
             "What the Buddha mysteriously is",
             "Rebirth &mdash; he is not going to be reborn as any of these, because he is not going to be reborn",
             "Brahminical lore",
             "The thirty-two marks"],
         "correct": 1,
         "expl": "The mystical reading is not available once the tense is restored."},
        {"q": "What explanation confirms it?",
         "opts": [
             "The lotus simile",
             "That if he had not given up defilements he might have become a god, centaur, spirit, or human &mdash; but he has given them up",
             "The footprints",
             "The verses"],
         "correct": 1,
         "expl": "Four categories, four possible destinations, and no further destination at all."},
        {"q": "What are the four categories Doṇa proposes?",
         "opts": [
             "God, brahmin, ascetic, and human",
             "God, centaur, spirit, and human",
             "Deva, Māra, Brahmā, and human",
             "The four assemblies"],
         "correct": 1,
         "expl": "Running from the highest downward and ending with the ordinary."},
        {"q": "Why does the framework have no slot?",
         "opts": [
             "Because the Buddha is above the highest slot",
             "Because he has stepped out of the system the slots belong to",
             "Because Doṇa asked wrongly",
             "Because the categories are fictional"],
         "correct": 1,
         "expl": "A category shift rather than an answer within the category."},
        {"q": "What does the lotus simile concede?",
         "opts": [
             "Nothing",
             "The origin fully &mdash; born in the world, grew up in it, sprouted in the water",
             "That the Buddha is a god",
             "That defilements remain"],
         "correct": 1,
         "expl": "The difference is located entirely in the present relationship."},
        {"q": "Why does the guide call the simile deflationary in the best sense?",
         "opts": [
             "Because it is modest",
             "Because it rules out the reading that the Buddha is made of some other material &mdash; the reading the footprints had invited",
             "Because lotuses are common",
             "Because it avoids the question"],
         "correct": 1,
         "expl": "Nothing about the lotus&rsquo;s substance differs from the water it grew in."},
        {"q": "How does this discourse sit with AN 4.15 and AN 4.34?",
         "opts": [
             "It agrees with them exactly",
             "Those place the Buddha at the top of a list of beings; this says the list is the wrong shape &mdash; and the guide shows the seam rather than smoothing it",
             "It replaces them",
             "It is unrelated"],
         "correct": 1,
         "expl": "The collection contains both moves."},
    ],
    marginalia=[
        ("Four questions", [
            "a god?",
            "a centaur?",
            "a spirit?",
            "a human?",
        ]),
        ("The tense", [
            "<span class=\"pali\">bhavissāmi</span>I will become",
            "not: I am not",
            "&mdash; the whole discourse",
        ]),
        ("The lotus", [
            "sprouted in the water",
            "grew in the water",
            "&mdash; and no water clings",
        ]),
        ("Cross-references", [
            "AN 4.35 &middot; the other brahmin conversation",
            "AN 4.37 &middot; next: four that cannot decline",
            "AN 4.24 &middot; conceiving nothing of what is known",
        ]),
    ],
    further=[
        '<a href="%s/an4.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.37.html">AN 4.37 &middot; Non-decline</a> &mdash; next in this series.',
        '<a href="an-4.24.html">AN 4.24 &middot; At Kāḷaka&rsquo;s Monastery</a> &mdash; the other '
        "discourse of the Fours on what a Realized One will and will not say of himself.",
        '<a href="an-4.15.html">AN 4.15 &middot; Regarded as Foremost</a> &mdash; where the Buddha '
        "is placed at the head of a list of beings.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.37 — Aparihāniyasutta
# --------------------------------------------------------------------------- #
page(
    37, "Aparihāniya", "Non-decline",
    vagga=VAGGA_4,
    meta_title="AN 4.37 — Non-decline | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Aparihāniyasutta — ethics, "
        "guarding the sense doors, moderation in eating, and dedication to wakefulness: four "
        "qualities under which a mendicant cannot decline. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_4),
        ("Speakers", SPEAKER),
        ("Form", "Four qualities named and then defined one by one, with three verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "This four-part sequence is a standard training block across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; entirely made of standard "
                       "formulas, and useful precisely for that"),
    ],
    why=(
        "Four ordinary things &mdash; keeping the precepts, guarding the senses, eating carefully, "
        "and not sleeping too much &mdash; and the claim attached to them is not modest: a "
        "mendicant with these <em>can&rsquo;t decline, and has drawn near to extinguishment</em>. "
        "Nothing on the list is an attainment. The discourse is the collection&rsquo;s clearest "
        "statement that the unglamorous parts of the training are the part that holds."),
    guide=[
        ("The teaching in one sentence", [
            "Four maintenance practices, none of them impressive, are between them enough to make "
            "backsliding impossible."]),
        ("The claim", [
            "<em>Abhabbo parihānāya, nibbānasseva santike</em> &mdash; incapable of decline, in the "
            "very presence of extinguishment. The two halves are different claims and both are "
            "strong.",
            "&lsquo;Cannot decline&rsquo; is a claim about stability: whatever has been gained will "
            "not be lost. &lsquo;Has drawn near to extinguishment&rsquo; is a claim about direction: "
            "not merely holding but approaching. Together they describe a life that only moves one "
            "way.",
            "What earns this is worth restating, because it is surprising. Not insight, not "
            "attainment, not a realization. Conduct, sense restraint, diet, and sleep. The discourse "
            "is making an argument about what actually determines whether a practice holds, and its "
            "answer is the daily maintenance rather than the peak."]),
        ("Ethics, and sense restraint", [
            "The first two definitions are formulas already seen in this chapter. Ethics is the block "
            "from AN 4.12 &mdash; restrained in the monastic code, conduct and resort, seeing danger "
            "in the slightest fault. Sense restraint is the block from AN 4.14 &mdash; not getting "
            "caught up in the features and details, all six faculties, covetousness and displeasure "
            "as what would otherwise overwhelm.",
            "Their reappearance here is not repetition for its own sake. The Aṅguttara builds "
            "discourses out of interchangeable blocks, and the interest lies in which blocks are put "
            "together. Here ethics and sense restraint are joined to two items that are rarely given "
            "this much weight."]),
        ("Eating in moderation", [
            "The reflection given is one of the finest short passages in the collection: "
            "<em>Not for fun, indulgence, adornment, or decoration, but only to sustain this body, to "
            "avoid harm, and to support spiritual practice.</em>",
            "Four things eating is not for, and three it is for, and then a formula about old and new "
            "discomfort: <em>I shall put an end to old discomfort and not give rise to new "
            "discomfort, and I will have the means to keep going, blamelessness, and a comfortable "
            "abiding.</em>",
            "The old discomfort is hunger; the new discomfort is what comes of eating too much. The "
            "reflection is not ascetic. It asks for a comfortable abiding explicitly, and it treats "
            "both under-eating and over-eating as failures of the same kind &mdash; conditions of the "
            "body that will occupy the mind.",
            "This passage is recited before meals in monasteries throughout the Theravāda world, and "
            "it transfers to lay use without modification, which is unusual for material of this "
            "kind."]),
        ("Dedication to wakefulness", [
            "<em>Jāgariyānuyoga</em>, devotion to being awake. The schedule is given in full: walking "
            "and sitting meditation by day; the same in the first watch of the night; lying down in "
            "the lion&rsquo;s posture in the middle watch, mindful and aware and focused on the time "
            "of getting up; and back to walking and sitting in the last watch.",
            "That is roughly four hours of sleep, taken in one block in the middle of the night, on "
            "the right side, with an intention to wake. It is worth stating the actual content rather "
            "than leaving &lsquo;wakefulness&rsquo; abstract.",
            "Two details repay attention. The lying down is described as a posture with a form &mdash; "
            "the lion&rsquo;s posture, one foot on the other &mdash; rather than as a lapse in the "
            "practice; and the mendicant lies down <em>mindful and aware</em>. Sleep is scheduled and "
            "entered deliberately. The discourse is not asking anyone not to sleep; it is asking that "
            "sleep be one of the four things done on purpose."]),
        ("Why this list holds", [
            "The four have a common shape: each is a boundary placed on something that runs "
            "continuously. Conduct bounds action, restraint bounds sense contact, moderation bounds "
            "eating, and the schedule bounds sleep. None of them is an activity added to the day; all "
            "of them are limits on activities that would happen anyway.",
            "That is a plausible mechanism for the claim about non-decline. Practices that consist of "
            "doing something extra are the ones that lapse when conditions get difficult. Practices "
            "that consist of a limit on what is happening regardless are much harder to stop doing, "
            "because there is no occasion on which they are skipped &mdash; only occasions on which "
            "they are broken.",
            "The closing verse names what holds it together: <em>a mendicant who loves diligence, "
            "seeing fear in negligence</em>. <em>Appamāda</em>, diligence, is the collection&rsquo;s "
            "standing summary virtue, and here its content is four boundaries and nothing more "
            "exalted."]),
    ],
    terms=[
        ("aparihāniya",
         "&ldquo;not liable to decline&rdquo; &mdash; the title claim, paired with having drawn near "
         "to extinguishment."),
        ("indriyesu guttadvāra",
         "&ldquo;guarding the sense doors&rdquo; &mdash; the second quality, defined by the "
         "formula already used in AN 4.14."),
        ("bhojane mattaññutā",
         "&ldquo;moderation in eating&rdquo;, literally knowing the measure in food &mdash; with a "
         "reflection recited before meals across the Theravāda world."),
        ("jāgariyānuyoga",
         "&ldquo;dedication to wakefulness&rdquo; &mdash; a schedule, not an abstraction: roughly "
         "four hours of sleep in the middle watch."),
        ("sīhaseyya",
         "&ldquo;the lion&rsquo;s posture&rdquo; &mdash; on the right side, one foot on the other, "
         "mindful and aware, focused on the time of getting up."),
    ],
    text_intro=(
        "The discourse in full: the four qualities, each defined, and the verses. The ellipses are "
        "the Pāli&rsquo;s own abbreviation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four qualities"),
        ("p", "&sect;1", "an4.37:1.1-1.3"),
        ("h3", "Accomplished in ethics"),
        ("p", "&sect;2", "an4.37:2.1-2.3"),
        ("h3", "Guarding the sense doors"),
        ("p", "&sect;3", "an4.37:3.1-3.10"),
        ("h3", "Eating in moderation"),
        ("p", "&sect;4", "an4.37:4.1-4.4"),
        ("h3", "Dedicated to wakefulness"),
        ("p", "&sect;5", "an4.37:5.1-5.7"),
        ("h3", "The verses"),
        ("p", "&sect;6", "an4.37:6.1-7.4"),
        ("p", "&sect;7", "an4.37:8.1-8.4"),
    ],
    quiz=[
        {"q": "What are the four qualities?",
         "opts": [
             "Ethics, immersion, wisdom, and freedom",
             "Accomplished in ethics, guarding the sense doors, eating in moderation, and dedicated to wakefulness",
             "Faith, energy, mindfulness, and immersion",
             "Contentment, good will, mindfulness, and immersion"],
         "correct": 1,
         "expl": "Nothing on the list is an attainment."},
        {"q": "What two claims are attached to them?",
         "opts": [
             "Long life and good rebirth",
             "That the mendicant cannot decline, and has drawn near to extinguishment",
             "Merit and reputation",
             "Freedom from illness and from criticism"],
         "correct": 1,
         "expl": "One about stability, one about direction."},
        {"q": "Why does the guide call the earning of that claim surprising?",
         "opts": [
             "Because the qualities are difficult",
             "Because it is conduct, sense restraint, diet, and sleep &mdash; not insight or attainment",
             "Because the claim is unqualified",
             "Because the list is short"],
         "correct": 1,
         "expl": "An argument about what actually determines whether a practice holds."},
        {"q": "What four things is eating said not to be for?",
         "opts": [
             "Health, strength, beauty, and long life",
             "Fun, indulgence, adornment, and decoration",
             "Merit, honor, gain, and praise",
             "Pleasure, company, custom, and habit"],
         "correct": 1,
         "expl": "And three things it is for: to sustain the body, avoid harm, and support practice."},
        {"q": "What are the old and new discomforts?",
         "opts": [
             "Illness and injury",
             "Hunger, and what comes of eating too much",
             "Past and future kamma",
             "Craving and aversion"],
         "correct": 1,
         "expl": "Both under-eating and over-eating are treated as failures of the same kind."},
        {"q": "Why does the guide say the reflection is not ascetic?",
         "opts": [
             "Because it permits any food",
             "Because it asks for a comfortable abiding explicitly",
             "Because it is recited by lay people",
             "Because it mentions blamelessness"],
         "correct": 1,
         "expl": "Conditions of the body that would otherwise occupy the mind."},
        {"q": "What does dedication to wakefulness actually involve?",
         "opts": [
             "Not sleeping at all",
             "Walking and sitting meditation by day and in the first and last watches, with sleep in the middle watch in the lion&rsquo;s posture",
             "Sleeping only when tired",
             "Meditating through the night once a week"],
         "correct": 1,
         "expl": "Roughly four hours of sleep, taken in one block."},
        {"q": "What is notable about how the lying down is described?",
         "opts": [
             "It is called a lapse",
             "It is a posture with a form, entered mindful and aware, focused on the time of getting up",
             "It is forbidden to the diligent",
             "It is not described"],
         "correct": 1,
         "expl": "Sleep is scheduled and entered deliberately."},
        {"q": "What common shape does the guide find in the four?",
         "opts": [
             "Each is an added activity",
             "Each is a boundary placed on something that runs continuously &mdash; action, sense contact, eating, sleep",
             "Each requires a teacher",
             "Each is monastic only"],
         "correct": 1,
         "expl": "None of them is an activity added to the day."},
        {"q": "Why does that shape support the claim about non-decline?",
         "opts": [
             "Because limits are easier",
             "Because practices consisting of a limit on what happens regardless have no occasion on which they are skipped &mdash; only occasions on which they are broken",
             "Because they are done in private",
             "Because they produce merit"],
         "correct": 1,
         "expl": "Practices that consist of doing something extra lapse when conditions get difficult."},
    ],
    marginalia=[
        ("The four", [
            "ethics",
            "the sense doors",
            "moderation in eating",
            "wakefulness",
        ]),
        ("Not for", [
            "fun",
            "indulgence",
            "adornment",
            "decoration",
        ]),
        ("The night", [
            "first watch &middot; walking, sitting",
            "middle &middot; the lion&rsquo;s posture",
            "last &middot; walking, sitting",
        ]),
        ("Cross-references", [
            "AN 4.12 &middot; the ethics block",
            "AN 4.14 &middot; the sense-restraint block",
            "AN 4.38 &middot; next: withdrawn",
        ]),
    ],
    further=[
        '<a href="%s/an4.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.38.html">AN 4.38 &middot; Withdrawn</a> &mdash; next in this series.',
        '<a href="an-4.14.html">AN 4.14 &middot; Restraint</a> &mdash; where the sense-restraint '
        "formula is set out as one of the four efforts.",
        '<a href="an-4.12.html">AN 4.12 &middot; Ethics</a> &mdash; where the same ethical formula is '
        "followed by the question of what more there is to do.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.38 — Patilīnasutta
# --------------------------------------------------------------------------- #
page(
    38, "Patilīna", "Withdrawn",
    vagga=VAGGA_4,
    meta_title="AN 4.38 — Withdrawn | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Patilīnasutta — views cast "
        "aside, searching given up, the physical process stilled, and the conceit 'I am' cut off at "
        "the root. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_4),
        ("Speakers", SPEAKER),
        ("Form", "Four terms stated, then each defined, with three verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The <em>patilīna</em> set has counterparts in the Chinese Āgamas and "
                              "overlaps with MN material on the searches; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; four technical terms, each of "
                       "which repays being unpacked"),
    ],
    why=(
        "Four things put down: opinions about the big questions, the three searches, the movement of "
        "the body in the fourth absorption, and the conceit &lsquo;I am&rsquo;. The word for the "
        "result, <em>patilīna</em>, means drawn back or withdrawn &mdash; and the discourse defines "
        "withdrawal not as going away from anywhere but as the absence of the thing that was doing "
        "the going."),
    guide=[
        ("The teaching in one sentence", [
            "Withdrawal is the end of four movements: holding positions, searching, bodily agitation, "
            "and the assertion &lsquo;I am&rsquo;."]),
        ("The ten questions", [
            "The first item is casting aside <em>idiosyncratic interpretations of the truth</em>, and "
            "the discourse lists them: the cosmos is eternal or not; finite or infinite; the soul and "
            "body are the same or different; after death a realized one exists, does not exist, both, "
            "or neither.",
            "This is the standard list of the undeclared questions, which the canon returns to "
            "repeatedly and consistently refuses to settle. Note the form of the refusal here: the "
            "mendicant has <em>cast out, cast aside, thrown out, discarded, let go of, given up, and "
            "relinquished</em> them &mdash; seven verbs, all of putting down, and none of answering.",
            "The Pāli for what is put down is <em>paccekasacca</em>, individual or private truths "
            "&mdash; the positions each school takes as its own. Sujato&rsquo;s "
            "&lsquo;idiosyncratic&rsquo; catches the sense that these are not shared findings but "
            "party badges. What is abandoned is the holding of a position, not the pursuit of "
            "knowledge."]),
        ("The three searches", [
            "<em>Esanā</em>: the search for sensual pleasures, for continued existence, and for a "
            "spiritual path (<em>brahmacariyesanā</em>).",
            "The third is the one that catches attention, and it should. The search for a spiritual "
            "path is on the list of things given up. This is not a rejection of practice; it is the "
            "observation that seeking is itself a mode of lack, and that a person who has arrived is "
            "no longer looking &mdash; including no longer looking for the thing they have.",
            "It is worth pairing with AN 4.16 on subtlety, where the criterion was that the "
            "practitioner does not aim for anything finer. The same structure appears: the end of the "
            "path is marked by the cessation of a certain kind of seeking, not by an additional "
            "acquisition."]),
        ("Stilling the physical process", [
            "The definition is technical and specific: the fourth absorption, entered with the giving "
            "up of pleasure and pain and the disappearance of former happiness and sadness, with pure "
            "equanimity and mindfulness.",
            "The <em>kāyasaṅkhāra</em>, the physical process, is elsewhere identified with breathing, "
            "which in the fourth absorption is described as extremely subtle. The claim is not that "
            "the body has stopped but that the movement in it has quietened to the point of "
            "stillness.",
            "Its inclusion tells us this is not a discourse about attitude. Three of the four items "
            "are dispositional; this one requires an attainment, and the discourse does not offer an "
            "alternative route to it."]),
        ("The conceit &lsquo;I am&rsquo;", [
            "The fourth definition is the one the title actually names. A mendicant is withdrawn when "
            "they have given up the conceit &lsquo;I am&rsquo; &mdash; <em>asmimāna</em> &mdash; cut "
            "it off at the root, made it like a palm stump, obliterated it so it cannot arise.",
            "<em>Asmimāna</em> is not the view that there is a self, which is abandoned earlier on "
            "the path. It is the residual sense of being someone, which the tradition says survives "
            "the correction of the view and goes last. The palm-stump image &mdash; a palm cut at the "
            "crown cannot regrow &mdash; is the canon&rsquo;s standard figure for an irreversible "
            "removal.",
            "So <em>patilīna</em>, withdrawn, turns out to have no spatial content at all. One does "
            "not withdraw to anywhere. What is described is the absence of the thing that was "
            "positioned, searching, moving, and asserting."]),
        ("The four as one movement", [
            "Read in order the four are progressively more interior: opinions held about the world, "
            "searching conducted in it, the movement of one&rsquo;s own body, and finally the sense of "
            "being the one doing all of it.",
            "That ordering is the discourse&rsquo;s argument, made by arrangement rather than by "
            "statement. Each item is the engine of the one before. Positions are held because "
            "something is being sought; seeking is restless; restlessness is bodily; and the whole "
            "apparatus runs on there being someone it is for.",
            "The verses confirm the reading by naming the last item as the decisive one: "
            "<em>when they&rsquo;re awakened by comprehending conceit, they&rsquo;re called "
            "&lsquo;withdrawn&rsquo;</em>."]),
    ],
    terms=[
        ("patilīna",
         "&ldquo;withdrawn, drawn back&rdquo; &mdash; with no spatial content: not going away from "
         "anywhere, but the absence of what was going."),
        ("paccekasacca",
         "&ldquo;idiosyncratic interpretations of the truth&rdquo; &mdash; individual or private "
         "truths, the positions each school takes as its own."),
        ("brahmacariyesanā",
         "&ldquo;the search for a spiritual path&rdquo; &mdash; the third search, and the one on the "
         "list of things given up."),
        ("kāyasaṅkhāra",
         "&ldquo;the physical process&rdquo; &mdash; elsewhere identified with breathing, stilled in "
         "the fourth absorption."),
        ("asmimāna",
         "&ldquo;the conceit &lsquo;I am&rsquo;&rdquo; &mdash; not the view that there is a self, but "
         "the residual sense of being someone, which goes last."),
    ],
    text_intro=(
        "The discourse in full: the four terms and their definitions, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Casting aside interpretations"),
        ("p", "&sect;1", "an4.38:1.1-1.6"),
        ("h3", "Giving up searching"),
        ("p", "&sect;2", "an4.38:2.1-2.3"),
        ("h3", "Stilling the physical process"),
        ("p", "&sect;3", "an4.38:3.1-3.3"),
        ("h3", "Withdrawn"),
        ("p", "&sect;4", "an4.38:4.1-4.4"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.38:5.1-6.4"),
        ("p", "&sect;6", "an4.38:7.1-7.4"),
    ],
    quiz=[
        {"q": "What is the first of the four things put down?",
         "opts": [
             "Sensual desire",
             "Idiosyncratic interpretations of the truth &mdash; the undeclared questions about the cosmos, the soul, and a realized one after death",
             "The conceit &lsquo;I am&rsquo;",
             "Bodily movement"],
         "correct": 1,
         "expl": "Seven verbs of putting down, and none of answering."},
        {"q": "What does <em>paccekasacca</em> mean?",
         "opts": [
             "Ultimate truth",
             "Individual or private truths &mdash; the positions each school takes as its own",
             "Conventional truth",
             "Secret teachings"],
         "correct": 1,
         "expl": "Not shared findings but party badges."},
        {"q": "What is abandoned, on the guide&rsquo;s reading?",
         "opts": [
             "The pursuit of knowledge",
             "The holding of a position",
             "Debate itself",
             "All opinions whatever"],
         "correct": 1,
         "expl": "The refusal is by putting down rather than by answering."},
        {"q": "What are the three searches?",
         "opts": [
             "For gain, honor, and praise",
             "For sensual pleasures, for continued existence, and for a spiritual path",
             "For a teacher, a place, and a method",
             "For truth, peace, and freedom"],
         "correct": 1,
         "expl": "The third is the one that catches attention."},
        {"q": "How does the guide read the third search being given up?",
         "opts": [
             "As a rejection of practice",
             "As the observation that seeking is itself a mode of lack, and one who has arrived is no longer looking &mdash; including for the thing they have",
             "As a textual error",
             "As applying only to other schools"],
         "correct": 1,
         "expl": "Pairs with AN 4.16, where the practitioner does not aim for anything finer."},
        {"q": "How is stilling the physical process defined?",
         "opts": [
             "By stopping the breath",
             "By the fourth absorption &mdash; pleasure and pain given up, with pure equanimity and mindfulness",
             "By deep sleep",
             "By fasting"],
         "correct": 1,
         "expl": "The <em>kāyasaṅkhāra</em> is elsewhere identified with breathing."},
        {"q": "What does its inclusion tell us about the discourse?",
         "opts": [
             "That it is about attitude only",
             "That it is not &mdash; three items are dispositional, but this one requires an attainment, with no alternative route offered",
             "That the fourth absorption is optional",
             "That the body must be mortified"],
         "correct": 1,
         "expl": "The discourse does not offer another way to it."},
        {"q": "What is <em>asmimāna</em>?",
         "opts": [
             "The view that there is a self",
             "The residual sense of being someone, which survives the correction of the view and goes last",
             "Pride in attainment",
             "Comparison with others"],
         "correct": 1,
         "expl": "Cut off at the root and made like a palm stump."},
        {"q": "What does <em>patilīna</em> turn out to mean?",
         "opts": [
             "Living in seclusion",
             "Withdrawal with no spatial content &mdash; the absence of what was positioned, searching, moving, and asserting",
             "Silence",
             "Retreat from society"],
         "correct": 1,
         "expl": "One does not withdraw to anywhere."},
        {"q": "What argument does the ordering of the four make?",
         "opts": [
             "That they are equally important",
             "That each item is the engine of the one before &mdash; positions are held because something is sought, seeking is restless, restlessness is bodily, and the whole thing runs on there being someone it is for",
             "That they occur in that sequence in time",
             "That the first is hardest"],
         "correct": 1,
         "expl": "Made by arrangement rather than by statement, and confirmed in the verses."},
    ],
    marginalia=[
        ("Four put down", [
            "interpretations",
            "searching",
            "the physical process",
            "&ldquo;I am&rdquo;",
        ]),
        ("Three searches", [
            "sensual pleasures",
            "continued existence",
            "a spiritual path",
        ]),
        ("The last one", [
            "<span class=\"pali\">asmimāna</span>&ldquo;I am&rdquo;",
            "not the view",
            "&mdash; the sense that survives it",
        ]),
        ("Cross-references", [
            "AN 4.16 &middot; aiming for nothing finer",
            "AN 4.24 &middot; conceiving no knower",
            "AN 4.39 &middot; next: with Ujjaya",
        ]),
    ],
    further=[
        '<a href="%s/an4.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.39.html">AN 4.39 &middot; With Ujjaya</a> &mdash; next in this series.',
        '<a href="an-4.24.html">AN 4.24 &middot; At Kāḷaka&rsquo;s Monastery</a> &mdash; where not '
        "conceiving a knower is set out at length.",
        '<a href="an-4.16.html">AN 4.16 &middot; Subtlety</a> &mdash; on the end of a certain kind '
        "of seeking.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.39 — Ujjayasutta
# --------------------------------------------------------------------------- #
page(
    39, "Ujjaya", "With Ujjaya",
    vagga=VAGGA_4,
    meta_title="AN 4.39 — With Ujjaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ujjayasutta — asked whether "
        "he praises sacrifice, the Buddha distinguishes the violent kind from the non-violent, and "
        "names the great royal sacrifices as fruitless. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; Ujjaya the brahmin comes to the Buddha and the conversation begins "
                    "at once"),
        ("Speakers", "The Buddha and Ujjaya the brahmin"),
        ("Form", "A question, a distinction drawn in two halves, and four verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Discourses on non-violent sacrifice are well represented in the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clean distinction, made without "
                       "attacking the questioner&rsquo;s religion"),
    ],
    why=(
        "&ldquo;Does the worthy Gotama praise sacrifice?&rdquo; The answer is a model of how to "
        "disagree with a tradition without dismissing it: not all sacrifices, and not none. The "
        "line is drawn at whether animals are killed, and the reason given is not a doctrine about "
        "ritual but a fact about who attends."),
    guide=[
        ("The teaching in one sentence", [
            "Sacrifice is neither praised nor condemned as such; what is condemned is killing, and "
            "what marks the difference is that the accomplished will not come to a sacrifice where "
            "blood is shed."]),
        ("The question and its context", [
            "<em>Yañña</em>, sacrifice, was the central institution of brahminical religion and a "
            "major economic activity. Large royal sacrifices involved hundreds of animals, "
            "substantial expenditure, and the participation of the priestly class. Ujjaya, a brahmin, "
            "is asking whether this teacher is against the thing his profession exists to perform.",
            "The answer refuses the whole question in its either-or form &mdash; <em>I don&rsquo;t "
            "praise all sacrifices. Nor do I criticize all sacrifices</em> &mdash; and then supplies "
            "the criterion. That is the same move made with Vassakāra four discourses earlier, and it "
            "is worth noticing as a pattern in how these conversations go."]),
        ("The criterion", [
            "Cattle, goats, sheep, chickens, pigs, and various creatures slaughtered: criticized. Not "
            "slaughtered: praised. There is no further condition. Nothing is said about the "
            "sacrificer&rsquo;s caste, the correctness of the ritual, the deities addressed, or the "
            "metaphysics involved.",
            "That restraint is deliberate and effective. The discourse leaves brahminical religion "
            "entirely intact except at one point, which means the objection cannot be dismissed as "
            "sectarian hostility. A brahmin can accept the criterion without abandoning his "
            "tradition, and the canon records that some did."]),
        ("The reason given", [
            "<em>Because neither perfected ones nor those who are on the path to perfection will "
            "attend such a violent sacrifice.</em> That is the entire argument, and it is worth "
            "dwelling on what kind of argument it is.",
            "It is not: killing is wrong, therefore do not sacrifice. It is: the people whose "
            "presence would make a sacrifice worth performing will not be there. Given that the "
            "point of a sacrifice is its fruit, and that fruit in this framework depends on the "
            "worthiness of the recipients, a sacrifice the accomplished avoid is a sacrifice that "
            "cannot produce what it is for.",
            "The argument therefore works inside the questioner&rsquo;s own economy of merit rather "
            "than against it. It says the violent sacrifice fails on its own terms. That is a more "
            "persuasive move than a moral denunciation and the verses repeat it: these huge violent "
            "sacrifices <em>yield no great fruit</em>."]),
        ("The named sacrifices", [
            "The verse names four by their technical titles: the horse sacrifice "
            "(<em>assamedha</em>), the human sacrifice (<em>purisamedha</em>), the "
            "&lsquo;casting of the yoke-pin&rsquo; (<em>sammāpāsa</em>), and the &lsquo;royal soma "
            "drinking&rsquo; (<em>vājapeyya</em>), with the &lsquo;unbarred&rsquo; "
            "(<em>niraggaḷa</em>).",
            "These are real Vedic rites, the greatest and most expensive in the repertoire. The "
            "<em>aśvamedha</em> in particular was the imperial sacrifice, performed by kings "
            "asserting sovereignty. Naming these rather than small domestic offerings makes the "
            "criticism land at the top of the institution.",
            "Elsewhere in the canon these same names are reinterpreted &mdash; given moral meanings "
            "in place of ritual ones &mdash; but this discourse does not do that. Here they are named "
            "and rejected as what they are."]),
        ("What is praised", [
            "<em>Niccadāna anukulayañña</em>, rendered here &lsquo;a regular gift as a propitious "
            "sacrifice&rsquo;. The two terms are worth separating: <em>nicca</em>, constant or "
            "regular, and <em>anukula</em>, in keeping with the family, customary.",
            "So what replaces the great rite is the ordinary standing practice of giving &mdash; "
            "small, repeated, and continuous with what a household already does. That is "
            "characteristic of how this collection handles ritual: it is not abolished but "
            "redirected toward something that can be sustained and harms nobody.",
            "The closing verse adds the practical consequence: for a sponsor of such sacrifices, "
            "<em>things get better, not worse</em>. AN 4.40, the next discourse, gives the same "
            "teaching again to a different brahmin, which is the collection&rsquo;s usual sign that "
            "the material was considered worth having twice."]),
    ],
    terms=[
        ("yañña",
         "&ldquo;sacrifice&rdquo; &mdash; the central institution of brahminical religion and a major "
         "economic activity."),
        ("assamedha",
         "&ldquo;horse sacrifice&rdquo; &mdash; the imperial rite, performed by kings asserting "
         "sovereignty; named here among the fruitless."),
        ("arahanto arahattamaggaṁ vā samāpannā",
         "&ldquo;perfected ones and those on the path to perfection&rdquo; &mdash; whose attendance "
         "or absence is the whole of the argument."),
        ("niccadāna",
         "&ldquo;a regular gift&rdquo; &mdash; small, repeated, continuous with what a household "
         "already does; what replaces the great rite."),
        ("anukulayañña",
         "&ldquo;a propitious sacrifice&rdquo;, in keeping with the family &mdash; the customary "
         "offering, praised where the great rites are not."),
    ],
    text_intro=(
        "The discourse in full: the question, the distinction, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The violent sacrifice"),
        ("p", "&sect;1", "an4.39:1.1-1.9"),
        ("h3", "The non-violent sacrifice"),
        ("p", "&sect;2", "an4.39:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.39:3.1-4.4"),
        ("p", "&sect;4", "an4.39:5.1-6.6"),
    ],
    quiz=[
        {"q": "How does the Buddha answer &lsquo;do you praise sacrifice?&rsquo;",
         "opts": [
             "He praises all sacrifice",
             "He praises neither all nor none &mdash; he refuses the either-or and supplies a criterion",
             "He condemns all sacrifice",
             "He declines to answer"],
         "correct": 1,
         "expl": "The same move made with Vassakāra four discourses earlier."},
        {"q": "What is the criterion?",
         "opts": [
             "The caste of the sacrificer",
             "Whether animals are slaughtered",
             "The correctness of the ritual",
             "The deity addressed"],
         "correct": 1,
         "expl": "There is no further condition."},
        {"q": "Why does the guide call that restraint effective?",
         "opts": [
             "Because it is brief",
             "Because it leaves brahminical religion intact except at one point, so the objection cannot be dismissed as sectarian hostility",
             "Because it flatters brahmins",
             "Because it avoids doctrine"],
         "correct": 1,
         "expl": "A brahmin can accept the criterion without abandoning his tradition."},
        {"q": "What reason is given for criticizing the violent sacrifice?",
         "opts": [
             "That killing produces bad kamma",
             "That neither perfected ones nor those on the path to perfection will attend it",
             "That it is expensive",
             "That the gods reject it"],
         "correct": 1,
         "expl": "That is the entire argument."},
        {"q": "What kind of argument is that?",
         "opts": [
             "A moral denunciation",
             "One that works inside the questioner&rsquo;s own economy of merit &mdash; the sacrifice fails on its own terms because its fruit depends on the worthiness of those present",
             "An appeal to scripture",
             "An appeal to the king"],
         "correct": 1,
         "expl": "More persuasive than a denunciation, and the verses repeat it."},
        {"q": "Which sacrifices does the verse name?",
         "opts": [
             "Household offerings",
             "The horse sacrifice, the human sacrifice, the &lsquo;casting of the yoke-pin&rsquo;, the &lsquo;royal soma drinking&rsquo;, and the &lsquo;unbarred&rsquo;",
             "Fire offerings only",
             "Ancestral rites"],
         "correct": 1,
         "expl": "The greatest and most expensive rites in the Vedic repertoire."},
        {"q": "Why does naming those in particular matter?",
         "opts": [
             "They were the most common",
             "It makes the criticism land at the top of the institution &mdash; the <em>aśvamedha</em> was the imperial sacrifice",
             "They were already obsolete",
             "They involved no animals"],
         "correct": 1,
         "expl": "Rather than small domestic offerings."},
        {"q": "How does this discourse differ from other canonical treatments of those names?",
         "opts": [
             "It reinterprets them morally",
             "It does not reinterpret them &mdash; here they are named and rejected as what they are",
             "It omits them",
             "It praises them"],
         "correct": 1,
         "expl": "Elsewhere the same names are given moral meanings in place of ritual ones."},
        {"q": "What is praised in place of the great rite?",
         "opts": [
             "Meditation",
             "A regular gift as a propitious sacrifice &mdash; small, repeated, and continuous with what a household already does",
             "Ordination",
             "Silence"],
         "correct": 1,
         "expl": "Ritual is not abolished but redirected."},
        {"q": "What does the closing verse promise the sponsor?",
         "opts": [
             "Awakening",
             "That things get better, not worse",
             "Rebirth as a god",
             "Freedom from debt"],
         "correct": 1,
         "expl": "And AN 4.40 gives the same teaching again to a different brahmin."},
    ],
    marginalia=[
        ("The criterion", [
            "animals killed &rarr; criticized",
            "animals not killed &rarr; praised",
            "&mdash; and nothing else",
        ]),
        ("The argument", [
            "not: killing is wrong",
            "but: the accomplished",
            "will not attend",
        ]),
        ("Named and rejected", [
            "the horse sacrifice",
            "the human sacrifice",
            "the royal soma drinking",
        ]),
        ("Cross-references", [
            "AN 4.40 &middot; next: the same, to Udāyī",
            "AN 4.35 &middot; the same conversational move",
            "AN 4.34 &middot; the field of merit",
        ]),
    ],
    further=[
        '<a href="%s/an4.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.40.html">AN 4.40 &middot; With Udāyī</a> &mdash; next in this series, and the '
        "same teaching to a second brahmin.",
        '<a href="an-4.35.html">AN 4.35 &middot; With Vassakāra</a> &mdash; the other discourse in '
        "which the Buddha refuses the frame of a question.",
        '<a href="an-4.34.html">AN 4.34 &middot; The Best Kinds of Confidence</a> &mdash; on the '
        "field of merit whose worthiness the argument depends on.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.40 — Udāyīsutta
# --------------------------------------------------------------------------- #
page(
    40, "Udāyī", "With Udāyī",
    vagga=VAGGA_4,
    meta_title="AN 4.40 — With Udāyī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Udāyīsutta — the same "
        "question about sacrifice from a second brahmin, with five verses on the offering that is "
        "well-gotten and well-given. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; Udāyī the brahmin comes to the Buddha, with the approach itself "
                    "abbreviated in the Pāli"),
        ("Speakers", "The Buddha and Udāyī the brahmin"),
        ("Form", "AN 4.39 abbreviated, with a different and longer set of verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "As with AN 4.39; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the prose is a repeat and the "
                       "verses are where the new material is"),
    ],
    why=(
        "The same question, the same answer, a different brahmin &mdash; and a different set of "
        "verses. The prose is abbreviated almost to a stub, which is the compilers telling a reciter "
        "to supply AN 4.39 from memory. What is given in full is the verse section, and it moves the "
        "teaching from what to avoid to how to give: well-prepared, allowable, timely, and offered "
        "with a mind of letting go."),
    guide=[
        ("The teaching in one sentence", [
            "The same distinction as AN 4.39, with the emphasis moved from the sacrifice that fails "
            "to the offering that succeeds."]),
        ("A discourse that is mostly a pointer", [
            "The abbreviation here is heavier than anywhere else in the chapter. Even the approach is "
            "cut: <em>Then Udāyī the brahmin went up to the Buddha, &hellip; and asked him.</em> The "
            "greeting formula, the sitting to one side, the reasons for praising and criticizing "
            "&mdash; all elided.",
            "This is how the collection stores a variant. The prose exists to establish that the "
            "teaching was also given to Udāyī; the reciter fills it in from the discourse before. "
            "What is written out in full is only what is new, which is the verses.",
            "It is honest to say that this makes AN 4.40 a thin discourse on the page and a normal "
            "one in performance. A reader working through the Fours in order should read AN 4.39 and "
            "4.40 as a single sitting, which is how they were meant to arrive."]),
        ("Who Udāyī is", [
            "Simply <em>Udāyī brāhmaṇo</em>, a brahmin of that name, and nothing further is said "
            "about him. The name is common in the canon and attaches to several different figures, "
            "including monastics; there is no basis in this discourse for identifying him with any of "
            "them.",
            "That is worth stating rather than guessing at. The discourse needs only that he is a "
            "brahmin asking the standard brahmin question, and it supplies nothing else."]),
        ("Four qualities of a good sacrifice", [
            "The first verse names them: <em>well-prepared and non-violent, a sacrifice that&rsquo;s "
            "allowable and timely</em>. Prepared, harmless, allowable (<em>kappiya</em>, permissible "
            "under the training), and timely.",
            "Two of these are new relative to AN 4.39. Allowability introduces the question of "
            "whether what is offered may properly be received &mdash; a real concern in a tradition "
            "with detailed rules about what monastics may accept. Timeliness introduces the question "
            "of occasion.",
            "Together they shift the analysis from the recipient to the gift. AN 4.39 asked who would "
            "attend; this asks what may properly be given, which is the donor&rsquo;s side of the "
            "same transaction."]),
        ("Well-gotten, well-offered, well-sacrificed", [
            "<em>Suladdhaṁ suhutaṁ suyiṭṭhaṁ</em> &mdash; three adverbs covering the whole life of "
            "the gift: how it was obtained, how it was presented, how it was given.",
            "The first is the one usually left out of discussions of generosity and the one this "
            "collection returns to most. A gift made from what was wrongly acquired is not made good "
            "by the giving. The verse puts acquisition first in the sequence, before presentation and "
            "before the act itself.",
            "&lsquo;To those worthy of a religious donation&rsquo; then supplies the recipient "
            "condition, and the field image from AN 4.34 returns: <em>in the fertile field of "
            "spiritual practitioners</em>. Source, manner, occasion, and recipient &mdash; the verse "
            "has assembled a complete account of what makes an offering work."]),
        ("The mind of letting go", [
            "The last verse names the interior condition: <em>when an intelligent, faithful person "
            "sacrifices like this, with a mind of letting go</em> &mdash; <em>muttacāga</em>, with "
            "generosity released, an open hand.",
            "That is the item none of the external conditions can supply, and putting it last is "
            "right. A gift can be well-gotten, allowable, timely, and correctly directed and still be "
            "given tightly. The verse asks for the hand to be actually open.",
            "This closes the Cakkavagga, and it closes it on a lay note. The chapter opened with the "
            "four conditions for a prosperous life and ends with how to give away part of it. Between "
            "them it has held the lion&rsquo;s roar, the four bests, two brahmin conversations, and "
            "the discourse on non-decline &mdash; a chapter with unusually wide range, and one that "
            "returns at the end to the audience it began with."]),
    ],
    terms=[
        ("kappiya",
         "&ldquo;allowable&rdquo; &mdash; permissible under the training; whether what is offered may "
         "properly be received."),
        ("kālena",
         "&ldquo;timely&rdquo; &mdash; the question of occasion, new here relative to AN 4.39."),
        ("suladdha suhuta suyiṭṭha",
         "&ldquo;well-gotten, well-offered, well-sacrificed&rdquo; &mdash; three adverbs covering how "
         "a gift was obtained, presented, and given."),
        ("muttacāga",
         "&ldquo;with a mind of letting go&rdquo; &mdash; generosity released, an open hand; the "
         "condition no external requirement can supply."),
        ("khetta",
         "&ldquo;field&rdquo; &mdash; the fertile field of spiritual practitioners, the standing "
         "image for a recipient in whom a gift grows."),
    ],
    text_intro=(
        "The discourse in full: the abbreviated exchange and the five verses. The ellipses and gaps "
        "are the Pāli&rsquo;s own abbreviation, which expects AN 4.39 to be supplied from memory. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The question, abbreviated"),
        ("p", "&sect;1", "an4.40:1.1-1.8"),
        ("h3", "The non-violent sacrifice"),
        ("p", "&sect;2", "an4.40:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.40:3.1-4.4"),
        ("p", "&sect;4", "an4.40:5.1-6.4"),
        ("p", "&sect;5", "an4.40:7.1-7.4"),
    ],
    quiz=[
        {"q": "What is the relationship between AN 4.40 and AN 4.39?",
         "opts": [
             "They contradict each other",
             "The same question and answer to a different brahmin, with the prose abbreviated and a new set of verses given in full",
             "AN 4.40 refutes AN 4.39",
             "They are unrelated"],
         "correct": 1,
         "expl": "The prose exists to establish that the teaching was also given to Udāyī."},
        {"q": "How heavily is the prose abbreviated?",
         "opts": [
             "Lightly",
             "Even the approach is cut &mdash; the greeting, the sitting to one side, and the reasons are all elided",
             "Not at all",
             "Only the verses are cut"],
         "correct": 1,
         "expl": "The reciter fills it in from the discourse before."},
        {"q": "What does the guide recommend for a reader working through the Fours?",
         "opts": [
             "Skip AN 4.40",
             "Read AN 4.39 and 4.40 as a single sitting, which is how they were meant to arrive",
             "Read them out of order",
             "Read only the verses"],
         "correct": 1,
         "expl": "A thin discourse on the page and a normal one in performance."},
        {"q": "What does the discourse tell us about Udāyī?",
         "opts": [
             "That he was a senior monk",
             "Only that he is a brahmin of that name &mdash; the name attaches to several canonical figures and there is no basis here for identifying him",
             "That he became a disciple",
             "That he was a minister"],
         "correct": 1,
         "expl": "Worth stating rather than guessing at."},
        {"q": "What four qualities does the first verse give a good sacrifice?",
         "opts": [
             "Large, public, ancient, and correct",
             "Well-prepared, non-violent, allowable, and timely",
             "Cheap, quick, private, and frequent",
             "Vedic, royal, priestly, and seasonal"],
         "correct": 1,
         "expl": "Two of them are new relative to AN 4.39."},
        {"q": "What does <em>kappiya</em> introduce?",
         "opts": [
             "The question of cost",
             "Whether what is offered may properly be received &mdash; a real concern in a tradition with detailed rules about what monastics may accept",
             "The question of caste",
             "The question of season"],
         "correct": 1,
         "expl": "The donor&rsquo;s side of the transaction."},
        {"q": "What do the three adverbs <em>suladdha, suhuta, suyiṭṭha</em> cover?",
         "opts": [
             "Three kinds of gift",
             "How a gift was obtained, presented, and given",
             "Three recipients",
             "Three occasions"],
         "correct": 1,
         "expl": "The whole life of the gift."},
        {"q": "Which of the three does the guide single out?",
         "opts": [
             "How it was presented",
             "How it was obtained &mdash; a gift made from what was wrongly acquired is not made good by the giving",
             "How it was given",
             "None of them"],
         "correct": 1,
         "expl": "The verse puts acquisition first in the sequence."},
        {"q": "What is <em>muttacāga</em>?",
         "opts": [
             "A large donation",
             "A mind of letting go &mdash; generosity released, an open hand",
             "A regular gift",
             "A vow of giving"],
         "correct": 1,
         "expl": "A gift can meet every external condition and still be given tightly."},
        {"q": "How does the chapter close?",
         "opts": [
             "With a monastic instruction",
             "On a lay note &mdash; it opened with the conditions for a prosperous life and ends with how to give part of it away",
             "With a verse on rebirth",
             "With a debate"],
         "correct": 1,
         "expl": "A chapter of unusually wide range, returning at the end to the audience it began with."},
    ],
    marginalia=[
        ("Four qualities", [
            "well-prepared",
            "non-violent",
            "<span class=\"pali\">kappiya</span>allowable",
            "timely",
        ]),
        ("Three adverbs", [
            "well-gotten",
            "well-offered",
            "well-sacrificed",
        ]),
        ("The last condition", [
            "<span class=\"pali\">muttacāga</span>letting go",
            "no external rule supplies it",
            "&mdash; the hand actually open",
        ]),
        ("Cross-references", [
            "AN 4.39 &middot; the discourse this abbreviates",
            "AN 4.31 &middot; where the chapter opened",
            "AN 4.34 &middot; the field of merit",
        ]),
    ],
    further=[
        '<a href="%s/an4.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.39.html">AN 4.39 &middot; With Ujjaya</a> &mdash; the discourse this one '
        "abbreviates, and the one to read first.",
        '<a href="an-4.31.html">AN 4.31 &middot; Situations</a> &mdash; where this chapter opened, on '
        "the conditions of a prosperous life.",
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; further into the Fours, and the '
        "next published page after this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# Rohitassavagga — the fifth chapter of the Fours
# --------------------------------------------------------------------------- #
VAGGA_5 = "<em>Rohitassavagga</em> &mdash; the fifth chapter of the Fours"
SETTING_5 = ("None stated; the Rohitassavagga gives no location for this discourse, and it is "
             "addressed to the mendicants directly")


# --------------------------------------------------------------------------- #
# AN 4.41 — Samādhibhāvanāsutta
# --------------------------------------------------------------------------- #
page(
    41, "Samādhibhāvanā", "Ways of Developing Immersion Further",
    vagga=VAGGA_5,
    meta_title="AN 4.41 — Ways of Developing Immersion Further | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samādhibhāvanāsutta — four "
        "developments of immersion, leading to blissful meditation, to knowledge and vision, to "
        "mindfulness and awareness, and to the ending of defilements. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "Four developments named, each defined by its practice, closing with a quotation "
                 "from the Pārāyana"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The four <em>samādhibhāvanā</em> appear across the Chinese Āgamas and "
                              "at DN 33; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the most directly practical "
                       "discourse in the chapter"),
    ],
    why=(
        "Four things immersion can be developed <em>for</em>, each with a different practice and a "
        "different result: the absorptions for a blissful abiding, the perception of light for "
        "knowledge and vision, watching feelings arise and pass for mindfulness, and contemplating "
        "the five aggregates for the ending of defilements. Anyone who has wondered whether "
        "concentration practice and insight practice are the same thing has this discourse&rsquo;s "
        "answer: they are the same faculty developed four ways."),
    guide=[
        ("The teaching in one sentence", [
            "Immersion is not one practice with one result; it is a capacity that can be developed in "
            "four directions, and the direction is chosen by what one does with it."]),
        ("The first: a blissful abiding", [
            "The four absorptions, given in the standard formula. The result named is "
            "<em>diṭṭhadhammasukhavihāra</em>, a blissful meditation in this life &mdash; and that is "
            "all that is claimed for it.",
            "It is worth noticing how modest the claim is. The jhānas are not here said to produce "
            "insight, liberation, or knowledge. They produce a pleasant abiding now. The tradition "
            "values that and does not pretend it is more than it is, which is a useful corrective in "
            "both directions: against those who dismiss absorption as a detour, and against those who "
            "treat it as the goal."]),
        ("The second: the perception of light", [
            "<em>Ālokasaññā</em> &mdash; applying the mind to the perception of light, focusing on "
            "the perception of day, <em>as by day, so by night; as by night, so by day</em>, "
            "developing a mind full of radiance with an open and unenveloped heart.",
            "This is the least familiar of the four to most modern readers and the hardest to teach "
            "responsibly. It is a specific practice with a specific result &mdash; "
            "<em>ñāṇadassana</em>, knowledge and vision, which in this literature covers the divine "
            "eye and the perception of beings passing away and being reborn.",
            "Two honest notes. First, the practice is described in the canon as a remedy for "
            "drowsiness as well as a basis for these attainments, and both uses are attested. Second, "
            "the results it is aimed at are not required for liberation; the fourth development on "
            "this list is. A reader who finds this one obscure has lost nothing essential, and it "
            "would be a mistake to make a page about it either mystifying or dismissive."]),
        ("The third: mindfulness and awareness", [
            "<em>They know feelings as they arise, as they remain, and as they go away. They know "
            "perceptions &hellip; they know thoughts &hellip;</em>",
            "Three objects &mdash; feeling, perception, thought &mdash; and three moments for each: "
            "arising, standing, vanishing. That is a complete and compact instruction, and it is "
            "arguably the most usable sentence in the chapter.",
            "The choice of objects is worth remarking on. Not the body, not the breath, but the three "
            "mental events that most reliably feel like they are simply the case rather than like "
            "things that are happening. A feeling does not announce that it began. Watching for the "
            "arising and the going away is what converts it from a fact about the world into an event "
            "in the mind.",
            "<em>Sati-sampajañña</em>, mindfulness and awareness, is the named result. This is the "
            "development that produces the ordinary working equipment of practice rather than any "
            "particular attainment."]),
        ("The fourth: the ending of defilements", [
            "Observing rise and fall in the five grasping aggregates, with each of the five given its "
            "own line: such is form, such is its origin, such is its ending &mdash; and the same for "
            "feeling, perception, choices, and consciousness.",
            "This is the one that leads to <em>āsavakkhaya</em>, and it is the only one of the four "
            "that does. Note what distinguishes it: the object is the five aggregates as a set, and "
            "the mode is watching them originate and end. Not stilling them, not perceiving them "
            "brightly, and not merely noting them &mdash; seeing them arise and cease.",
            "Read against the third development the difference is precise. The third watches feeling, "
            "perception, and thought &mdash; three of the aggregates, and the ones nearest to hand. "
            "The fourth adds form and consciousness and completes the set. Between them they suggest "
            "that the third is the training and the fourth is the same skill applied to everything a "
            "person is made of."]),
        ("The quotation", [
            "The discourse closes by citing itself &mdash; or rather, by citing an older text. "
            "<em>And it was in this connection that I said in &lsquo;The Way to the Far Shore&rsquo;, "
            "in &lsquo;The Questions of Puṇṇaka&rsquo;</em>, followed by four lines about one who has "
            "appraised the world high and low and is disturbed by nothing in it.",
            "The Pārāyanavagga is a section of the Sutta Nipāta and one of the oldest strata of the "
            "canon; the Aṅguttara here treats it as an existing authority to be explained. That is "
            "unusual and worth pointing out to students, because it shows a text in the act of "
            "commenting on an earlier one within the canon itself.",
            "The verse quoted is not obviously about immersion, and the connection asserted is the "
            "discourse&rsquo;s own claim: the person described in the old verse is the one produced "
            "by the fourth development. Whether the original verse meant that is a separate question, "
            "and the discourse does not pretend to argue it."]),
    ],
    terms=[
        ("samādhibhāvanā",
         "&ldquo;development of immersion&rdquo; &mdash; not one practice but a capacity developed in "
         "four directions, chosen by what one does with it."),
        ("diṭṭhadhammasukhavihāra",
         "&ldquo;blissful meditation in this life&rdquo; &mdash; all that is claimed for the four "
         "absorptions here, and a deliberately modest claim."),
        ("ālokasaññā",
         "&ldquo;perception of light&rdquo; &mdash; as by day so by night; the practice leading to "
         "knowledge and vision, and elsewhere a remedy for drowsiness."),
        ("satisampajañña",
         "&ldquo;mindfulness and awareness&rdquo; &mdash; the result of watching feelings, "
         "perceptions, and thoughts arise, remain, and go away."),
        ("Pārāyana",
         "&ldquo;The Way to the Far Shore&rdquo; &mdash; a section of the Sutta Nipāta and one of the "
         "oldest strata of the canon, cited here as an existing authority."),
    ],
    text_intro=(
        "The discourse in full: the four developments, each with its practice and result, and the "
        "quotation from the Pārāyana. The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four developments"),
        ("p", "&sect;1", "an4.41:1.1-1.6"),
        ("h3", "A blissful abiding"),
        ("p", "&sect;2", "an4.41:2.1-2.3"),
        ("h3", "Knowledge and vision"),
        ("p", "&sect;3", "an4.41:3.1-3.5"),
        ("h3", "Mindfulness and awareness"),
        ("p", "&sect;4", "an4.41:4.1-4.4"),
        ("h3", "The ending of defilements"),
        ("p", "&sect;5", "an4.41:5.1-5.10"),
        ("p", "&sect;6", "an4.41:6.1-6.4"),
    ],
    quiz=[
        {"q": "What four results are the developments of immersion aimed at?",
         "opts": [
             "The four absorptions",
             "A blissful meditation in this life, knowledge and vision, mindfulness and awareness, and the ending of defilements",
             "Ethics, immersion, wisdom, and freedom",
             "The four noble truths"],
         "correct": 1,
         "expl": "The same faculty developed four ways."},
        {"q": "What is claimed for the four absorptions here?",
         "opts": [
             "Liberation",
             "A blissful abiding in this life &mdash; and nothing more",
             "Knowledge and vision",
             "The ending of defilements"],
         "correct": 1,
         "expl": "A deliberately modest claim, and a corrective in both directions."},
        {"q": "What is the practice for knowledge and vision?",
         "opts": [
             "The four absorptions",
             "The perception of light &mdash; as by day so by night, developing a mind full of radiance",
             "Contemplating the aggregates",
             "Watching the breath"],
         "correct": 1,
         "expl": "<em>Ālokasaññā</em>, the least familiar of the four."},
        {"q": "What two honest notes does the guide make about it?",
         "opts": [
             "That it is late, and that it is obscure",
             "That it is also attested as a remedy for drowsiness, and that its results are not required for liberation",
             "That it is Mahāyāna, and that it is optional",
             "That it is dangerous, and that it is rare"],
         "correct": 1,
         "expl": "A reader who finds it obscure has lost nothing essential."},
        {"q": "What three objects does the third development watch?",
         "opts": [
             "Body, feeling, and mind",
             "Feelings, perceptions, and thoughts",
             "Form, consciousness, and choices",
             "Sights, sounds, and ideas"],
         "correct": 1,
         "expl": "Each as it arises, remains, and goes away."},
        {"q": "Why does the guide remark on that choice of objects?",
         "opts": [
             "They are the easiest to watch",
             "They are the mental events that most reliably feel like they are simply the case rather than like things happening",
             "They are the only ones available in immersion",
             "They exclude the body"],
         "correct": 1,
         "expl": "Watching for arising and going away converts a feeling into an event in the mind."},
        {"q": "Which development leads to the ending of defilements?",
         "opts": [
             "The absorptions",
             "Observing rise and fall in the five grasping aggregates",
             "The perception of light",
             "Watching feelings and thoughts"],
         "correct": 1,
         "expl": "And it is the only one of the four that does."},
        {"q": "How does the fourth differ from the third?",
         "opts": [
             "It is done in absorption",
             "It adds form and consciousness, completing the set, and its mode is watching things originate and end",
             "It uses a different posture",
             "It requires a teacher"],
         "correct": 1,
         "expl": "The third is the training and the fourth is the same skill applied to everything a person is made of."},
        {"q": "What does the discourse quote at the end?",
         "opts": [
             "A commentary",
             "The Pārāyana &mdash; &lsquo;The Way to the Far Shore&rsquo;, from the Questions of Puṇṇaka",
             "The Dhammapada",
             "The Vinaya"],
         "correct": 1,
         "expl": "One of the oldest strata of the canon."},
        {"q": "Why does the guide say the quotation is worth pointing out?",
         "opts": [
             "Because it dates the discourse",
             "Because it shows a text in the act of commenting on an earlier one within the canon itself",
             "Because the verse is famous",
             "Because it names Puṇṇaka"],
         "correct": 1,
         "expl": "The connection asserted is the discourse&rsquo;s own claim, and it does not pretend to argue it."},
    ],
    marginalia=[
        ("Four results", [
            "a blissful abiding",
            "knowledge and vision",
            "mindfulness and awareness",
            "the end of defilements",
        ]),
        ("The third", [
            "feelings",
            "perceptions",
            "thoughts",
            "&mdash; arising, remaining, going",
        ]),
        ("The fourth", [
            "all five aggregates",
            "origin and ending of each",
            "&mdash; the only one that frees",
        ]),
        ("Cross-references", [
            "AN 4.42 &middot; next: four ways of answering",
            "AN 4.16 &middot; the four subtleties",
            "AN 4.38 &middot; the fourth absorption",
        ]),
    ],
    further=[
        '<a href="%s/an4.41/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.42.html">AN 4.42 &middot; Ways of Answering Questions</a> &mdash; next in this '
        "series.",
        '<a href="an-4.170.html">AN 4.170 &middot; In Conjunction</a> &mdash; further into the Fours, '
        "on serenity and insight developed together.",
        '<a href="an-4.16.html">AN 4.16 &middot; Subtlety</a> &mdash; on the refinement of the '
        "aggregates and where it ends.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.42 — Pañhabyākaraṇasutta
# --------------------------------------------------------------------------- #
page(
    42, "Pañhabyākaraṇa", "Ways of Answering Questions",
    vagga=VAGGA_5,
    meta_title="AN 4.42 — Ways of Answering Questions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Pañhabyākaraṇasutta — "
        "categorically, analytically, with a counter-question, or set aside: four ways a question "
        "should be answered. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of four, and four verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four <em>pañhabyākaraṇa</em> are standard across the Chinese "
                              "Āgamas and are elaborated at DN 33 and in the Milindapañha; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; four words that carry a great "
                       "deal of the canon&rsquo;s method"),
    ],
    why=(
        "Four ways to answer a question, and the fourth is not to answer it. Categorically, "
        "analytically, with a counter-question, or set aside &mdash; the list is bare here and "
        "elaborated elsewhere, and it is one of the most quietly consequential sets in the "
        "collection. Nearly everything distinctive about how the canon handles questions comes out "
        "of these four."),
    guide=[
        ("The teaching in one sentence", [
            "Not every question deserves a direct answer, and knowing which of four treatments a "
            "question needs is itself a skill."]),
        ("Categorically", [
            "<em>Ekaṁsabyākaraṇīya</em> &mdash; to be answered one-sidedly, without qualification. "
            "Is form impermanent? Yes. There is no case to distinguish and no counter-question "
            "needed.",
            "This is the mode most people assume is the only one, and the discourse&rsquo;s first "
            "point is that it is one of four. A tradition that answered everything categorically "
            "would be either dogmatic or wrong, since most interesting questions contain an "
            "ambiguity."]),
        ("Analytically", [
            "<em>Vibhajjabyākaraṇīya</em> &mdash; to be answered by dividing. Is such-and-such person "
            "to be praised? That depends: in this respect yes, in that respect no.",
            "This is the mode the Theravāda takes its old name from &mdash; <em>Vibhajjavāda</em>, "
            "the doctrine of analysis &mdash; and it is the characteristic move of the whole "
            "collection. The Aṅguttara is very largely a book of divisions: this fourfold, that "
            "threefold, these two kinds of person.",
            "The technique is not evasion. It concedes that the question is real and answers it "
            "completely, by first correcting the assumption that one answer will cover the cases."]),
        ("With a counter-question", [
            "<em>Paṭipucchābyākaraṇīya</em> &mdash; the answer is another question, asked in order to "
            "find out what was actually being asked or to make the questioner supply a term they had "
            "left undefined.",
            "The canon uses this constantly. A wanderer asks whether pleasure and pain are "
            "self-made; the reply asks what he means. The move assumes that many questions arrive "
            "malformed and that answering them as put would confirm a mistake embedded in the "
            "asking.",
            "It is worth teaching alongside the fourth mode, because the two are often confused. A "
            "counter-question is a way of proceeding. Setting aside is a way of stopping."]),
        ("Set aside", [
            "<em>Ṭhapanīya</em> &mdash; to be put aside, left standing. This is the treatment given "
            "to the undeclared questions listed in AN 4.38: whether the cosmos is eternal, whether a "
            "realized one exists after death, and the rest.",
            "The reason given elsewhere in the canon is consistently practical rather than "
            "epistemic: these questions are not connected with the goal, do not lead to "
            "disenchantment, dispassion, cessation, peace, insight, awakening, or extinguishment. "
            "The refusal is not a claim that the answers are unknowable; it is a claim that pursuing "
            "them does not help.",
            "It is honest to note that readers have disagreed for two thousand years about whether "
            "that is a satisfying position, and that the canon itself never elaborates it further "
            "than the practical grounds. A teaching guide should present the reason given rather "
            "than improve on it."]),
        ("What the verses claim", [
            "The mendicant who knows which mode each question needs is called <em>intimidating, hard "
            "to defeat, deep, and hard to crush</em>, and expert in <em>what the meaning is and what "
            "it isn&rsquo;t</em>.",
            "That vocabulary belongs to debate. These four are being presented as a competence in "
            "public disputation as much as a pedagogical method, which fits the setting: a teacher in "
            "this environment was regularly required to field questions from people trying to trap "
            "him.",
            "The closing verse shifts registers and gives the whole thing a criterion: "
            "<em>shunning what is not the meaning, an astute person grasps the meaning</em>. The four "
            "modes are in service of <em>attha</em>, the point &mdash; which is also what AN 4.6 said "
            "learning was for. The skill is not in answering well but in keeping the answer attached "
            "to what matters."]),
    ],
    terms=[
        ("ekaṁsabyākaraṇīya",
         "&ldquo;to be answered categorically&rdquo; &mdash; one-sidedly, without qualification; one "
         "of four modes rather than the default."),
        ("vibhajjabyākaraṇīya",
         "&ldquo;to be answered analytically&rdquo; &mdash; by dividing. The Theravāda&rsquo;s old "
         "name, <em>Vibhajjavāda</em>, comes from this word."),
        ("paṭipucchābyākaraṇīya",
         "&ldquo;to be answered with a counter-question&rdquo; &mdash; a way of proceeding, used when "
         "a question arrives malformed."),
        ("ṭhapanīya",
         "&ldquo;to be set aside&rdquo; &mdash; left standing; the treatment given to the undeclared "
         "questions, on practical rather than epistemic grounds."),
        ("attha",
         "&ldquo;meaning, point&rdquo; &mdash; what the four modes are in service of, and the "
         "criterion the closing verse supplies."),
    ],
    text_intro=(
        "The discourse in full: the four ways and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four ways of answering"),
        ("p", "&sect;1", "an4.42:1.1-1.7"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.42:2.1-2.4"),
        ("p", "&sect;3", "an4.42:3.1-3.4"),
        ("p", "&sect;4", "an4.42:4.1-4.4"),
        ("p", "&sect;5", "an4.42:5.1-5.4"),
    ],
    quiz=[
        {"q": "What are the four ways of answering questions?",
         "opts": [
             "Truthfully, kindly, timely, and beneficially",
             "Categorically, analytically, with a counter-question, and set aside",
             "In prose, in verse, by simile, and by silence",
             "To monastics, to lay people, to gods, and to wanderers"],
         "correct": 1,
         "expl": "And the fourth is not to answer."},
        {"q": "What is the guide&rsquo;s first point about the categorical mode?",
         "opts": [
             "That it is the best",
             "That it is one of four &mdash; a tradition answering everything categorically would be dogmatic or wrong",
             "That it is rarely used",
             "That it applies only to doctrine"],
         "correct": 1,
         "expl": "Most interesting questions contain an ambiguity."},
        {"q": "What old name of the Theravāda comes from the second mode?",
         "opts": [
             "Sthaviravāda",
             "Vibhajjavāda &mdash; the doctrine of analysis",
             "Sarvāstivāda",
             "Mahāvihāravāsin"],
         "correct": 1,
         "expl": "The characteristic move of the whole collection."},
        {"q": "Why is analysis not evasion?",
         "opts": [
             "Because it is quicker",
             "Because it concedes the question is real and answers it completely, after correcting the assumption that one answer covers the cases",
             "Because it is authorized",
             "Because it uses the questioner&rsquo;s terms"],
         "correct": 1,
         "expl": "The Aṅguttara is very largely a book of divisions."},
        {"q": "What does the counter-question assume?",
         "opts": [
             "That the questioner is hostile",
             "That many questions arrive malformed, and answering them as put would confirm a mistake embedded in the asking",
             "That the answer is unknown",
             "That the questioner already knows"],
         "correct": 1,
         "expl": "It finds out what was actually being asked."},
        {"q": "How does the guide distinguish the third mode from the fourth?",
         "opts": [
             "They are the same",
             "A counter-question is a way of proceeding; setting aside is a way of stopping",
             "One is for monastics, one for lay people",
             "One is polite, one is not"],
         "correct": 1,
         "expl": "The two are often confused."},
        {"q": "What kind of questions are set aside?",
         "opts": [
             "Questions about ethics",
             "The undeclared questions &mdash; whether the cosmos is eternal, whether a realized one exists after death, and the rest",
             "Questions from non-Buddhists",
             "Questions about the future"],
         "correct": 1,
         "expl": "The same list AN 4.38 gives."},
        {"q": "What reason does the canon give for setting them aside?",
         "opts": [
             "That they are unknowable",
             "A practical one &mdash; they are not connected with the goal and do not lead to disenchantment, dispassion, cessation, peace, insight, or awakening",
             "That they are forbidden",
             "That they were answered elsewhere"],
         "correct": 1,
         "expl": "Not a claim that the answers are unknowable, but that pursuing them does not help."},
        {"q": "How does the guide handle the adequacy of that reason?",
         "opts": [
             "It defends it at length",
             "It notes that readers have disagreed for two thousand years, and presents the reason given rather than improving on it",
             "It rejects it",
             "It does not raise the question"],
         "correct": 1,
         "expl": "The canon itself never elaborates further than the practical grounds."},
        {"q": "What criterion does the closing verse supply?",
         "opts": [
             "Speed of reply",
             "<em>Attha</em>, the meaning or point &mdash; shunning what is not the meaning and grasping what is",
             "Politeness",
             "Scriptural authority"],
         "correct": 1,
         "expl": "The skill is in keeping the answer attached to what matters."},
    ],
    marginalia=[
        ("Four modes", [
            "categorically",
            "analytically",
            "by counter-question",
            "set aside",
        ]),
        ("Proceeding vs stopping", [
            "counter-question &middot; go on",
            "set aside &middot; stop",
            "&mdash; often confused",
        ]),
        ("The criterion", [
            "<span class=\"pali\">attha</span>the point",
            "shun what is not",
            "grasp what is",
        ]),
        ("Cross-references", [
            "AN 4.38 &middot; the undeclared questions",
            "AN 4.6 &middot; getting the point of learning",
            "AN 4.43 &middot; next: valuing anger",
        ]),
    ],
    further=[
        '<a href="%s/an4.42/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.43.html">AN 4.43 &middot; Valuing Anger</a> &mdash; next in this series.',
        '<a href="an-4.38.html">AN 4.38 &middot; Withdrawn</a> &mdash; where the questions that are '
        "set aside are listed in full.",
        '<a href="an-4.6.html">AN 4.6 &middot; A Little Learning</a> &mdash; on <em>attha</em>, the '
        "point, as the measure of learning.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.43 — Paṭhamakodhagarusutta
# --------------------------------------------------------------------------- #
page(
    43, "Paṭhamakodhagaru", "Valuing Anger",
    vagga=VAGGA_5,
    meta_title="AN 4.43 — Valuing Anger | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamakodhagarusutta — "
        "four individuals who value anger, denigration, material things, or honor rather than the "
        "true teaching. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "Four individuals, their four mirrors, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The <em>kodhagaru</em> set appears in the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and built on one word "
                       "worth understanding"),
    ],
    why=(
        "Four people, sorted by what they hold more important than the teaching: anger, denigration, "
        "material things, or honor. The Pāli word is <em>garu</em>, weighty &mdash; the same root as "
        "the reverence of AN 4.21, whose absence was said to be a life of suffering. The discourse "
        "asks not what a person believes but what carries weight with them when something has to "
        "give."),
    guide=[
        ("The teaching in one sentence", [
            "What a person actually values is shown by what wins when it conflicts with the teaching, "
            "and four things commonly win."]),
        ("The word <em>garu</em>", [
            "<em>Kodhagaru</em>: one for whom anger is weighty. The suffix runs through all eight "
            "items, positive and negative, and the same root gives <em>gārava</em>, the reverence "
            "AN 4.21 said one cannot live well without, and <em>guru</em>, a teacher &mdash; one who "
            "is weighty.",
            "The image is of a scale. To value something is for it to weigh more than what it is set "
            "against, and the discourse always sets these four against <em>saddhamma</em>, the true "
            "teaching. Nobody in this discourse is described as rejecting the teaching. They are "
            "described as having something that outweighs it.",
            "That is a sharper diagnostic than a question about belief, because it produces a test. "
            "What has actually happened on the occasions when your anger and your practice pointed in "
            "different directions?"]),
        ("The four", [
            "Anger (<em>kodha</em>), denigration (<em>makkha</em>), material things "
            "(<em>lābha</em>), and honor (<em>sakkāra</em>).",
            "The pairing is instructive. The first two are hostile states and the second two are "
            "acquisitions; the first two make a person hold on to a grievance and the second two make "
            "them hold on to a position. Between them they cover the two ordinary reasons for setting "
            "a principle aside: because one is angry, and because one has something to lose.",
            "<em>Makkha</em> deserves a note. Usually translated denigration or disparagement, it "
            "names the specific move of belittling what someone else has done &mdash; and in the "
            "commentarial analysis, of refusing to acknowledge a benefit received. It is a colder "
            "fault than anger and it survives longer."]),
        ("Lābha and sakkāra", [
            "These two travel together throughout the canon, usually with <em>siloka</em>, "
            "popularity, as a third; AN 4.25 named the trio among the things the spiritual life is "
            "not lived for.",
            "Their appearance here as things that can outweigh the teaching is the sharper form of "
            "the same warning. AN 4.25 said the life is not <em>for</em> them; this says they can "
            "come to matter <em>more</em> than it. The second is the observable failure, and it can "
            "happen to someone who would sincerely affirm the first."]),
        ("The positive half", [
            "Four individuals who value the true teaching rather than anger, denigration, material "
            "things, or honor. The mirror is exact and adds no new content.",
            "The verses add one thing the prose does not: the metaphor of growth. Those who value the "
            "four <em>don&rsquo;t grow in the teaching that was taught by the perfected Buddha</em>; "
            "those who value the teaching <em>do grow</em>.",
            "That is the same verb AN 4.26 used of the deceivers and flatterers, and the diagnosis is "
            "the same shape. Nothing breaks. The practice simply does not develop, and the reason is "
            "that something else is being fed."]),
        ("Reading it as a pair with AN 4.44", [
            "The next discourse takes the identical four and reframes them: instead of four kinds of "
            "person, four things that <em>oppose</em> the true teaching. Same content, different "
            "grammatical subject.",
            "That is a smaller variation than the AN 4.17&ndash;4.19 group but the same phenomenon, "
            "and worth noticing for the same reason. The collection preserves a teaching in both its "
            "personal and its impersonal form, and the two are useful for different purposes: one "
            "sorts people, the other names forces."]),
    ],
    terms=[
        ("garu",
         "&ldquo;weighty&rdquo; &mdash; the suffix on all eight items. The same root gives "
         "<em>gārava</em>, reverence, and <em>guru</em>, teacher."),
        ("makkha",
         "&ldquo;denigration&rdquo; &mdash; belittling what someone else has done, and refusing to "
         "acknowledge a benefit received. Colder than anger, and longer-lasting."),
        ("lābha",
         "&ldquo;material things, gain&rdquo; &mdash; with honor, one of the pair that travels "
         "through the canon as the standing danger to a religious life."),
        ("sakkāra",
         "&ldquo;honor&rdquo; &mdash; the respect paid to a person; usually named with gain and "
         "popularity as a trio."),
        ("saddhamma",
         "&ldquo;the true teaching&rdquo; &mdash; what each of the four is weighed against. Nobody "
         "here rejects it; they have something that outweighs it."),
    ],
    text_intro=(
        "The discourse in full: the four individuals, their mirrors, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four who value otherwise"),
        ("p", "&sect;1", "an4.43:1.1-1.4"),
        ("h3", "Four who value the teaching"),
        ("p", "&sect;2", "an4.43:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.43:3.1-3.4"),
        ("p", "&sect;4", "an4.43:4.1-4.4"),
    ],
    quiz=[
        {"q": "What four things do the individuals value rather than the true teaching?",
         "opts": [
             "Wealth, family, health, and status",
             "Anger, denigration, material things, and honor",
             "Greed, hatred, delusion, and fear",
             "Gain, honor, praise, and pleasure"],
         "correct": 1,
         "expl": "Two hostile states and two acquisitions."},
        {"q": "What does <em>garu</em> mean, and what does the image suggest?",
         "opts": [
             "&lsquo;Dear&rsquo; &mdash; an image of affection",
             "&lsquo;Weighty&rsquo; &mdash; an image of a scale, where to value something is for it to outweigh what it is set against",
             "&lsquo;First&rsquo; &mdash; an image of order",
             "&lsquo;Strong&rsquo; &mdash; an image of force"],
         "correct": 1,
         "expl": "The same root gives <em>gārava</em>, reverence, and <em>guru</em>, teacher."},
        {"q": "What is notable about how the four are described?",
         "opts": [
             "They reject the teaching",
             "Nobody is described as rejecting the teaching &mdash; they have something that outweighs it",
             "They are all monastics",
             "They are unaware of the teaching"],
         "correct": 1,
         "expl": "A sharper diagnostic than a question about belief."},
        {"q": "What test does the guide draw from it?",
         "opts": [
             "What do you say you believe?",
             "What has actually happened on the occasions when your anger and your practice pointed in different directions?",
             "How much have you learned?",
             "How long have you practised?"],
         "correct": 1,
         "expl": "The word produces a test rather than a creed."},
        {"q": "What do the first two and the second two cover between them?",
         "opts": [
             "Monastic and lay faults",
             "The two ordinary reasons for setting a principle aside &mdash; because one is angry, and because one has something to lose",
             "Past and present faults",
             "Faults of speech and of mind"],
         "correct": 1,
         "expl": "Holding on to a grievance, and holding on to a position."},
        {"q": "What is <em>makkha</em>?",
         "opts": [
             "Anger",
             "Denigration &mdash; belittling what someone else has done, and refusing to acknowledge a benefit received",
             "Envy",
             "Conceit"],
         "correct": 1,
         "expl": "A colder fault than anger, and it survives longer."},
        {"q": "How does this discourse sharpen AN 4.25&rsquo;s warning about gain and honor?",
         "opts": [
             "It does not",
             "AN 4.25 said the life is not <em>for</em> them; this says they can come to matter <em>more</em> than it",
             "It permits them",
             "It adds popularity"],
         "correct": 1,
         "expl": "The second is the observable failure, and it can happen to someone who sincerely affirms the first."},
        {"q": "What do the verses add that the prose does not?",
         "opts": [
             "A simile of fire",
             "The metaphor of growth &mdash; these do or do not grow in the teaching",
             "A setting",
             "A fifth item"],
         "correct": 1,
         "expl": "The same verb AN 4.26 used of the deceivers."},
        {"q": "What diagnosis does that metaphor give?",
         "opts": [
             "That the practice collapses",
             "That nothing breaks &mdash; the practice simply does not develop, because something else is being fed",
             "That the person leaves the training",
             "That rebirth is unfavorable"],
         "correct": 1,
         "expl": "The same shape as AN 4.26."},
        {"q": "How does AN 4.44 reframe the same four?",
         "opts": [
             "As four faults of speech",
             "As four things that oppose the true teaching &mdash; the same content with a different grammatical subject",
             "As four stages",
             "As four assemblies"],
         "correct": 1,
         "expl": "One sorts people; the other names forces."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">kodha</span>anger",
            "<span class=\"pali\">makkha</span>denigration",
            "<span class=\"pali\">lābha</span>material things",
            "<span class=\"pali\">sakkāra</span>honor",
        ]),
        ("The word", [
            "<span class=\"pali\">garu</span>weighty",
            "also: <span class=\"pali\">gārava</span>reverence",
            "also: <span class=\"pali\">guru</span>teacher",
        ]),
        ("The diagnosis", [
            "nothing breaks",
            "nothing grows",
            "&mdash; something else is fed",
        ]),
        ("Cross-references", [
            "AN 4.44 &middot; next: the same, impersonally",
            "AN 4.25 &middot; not for gain and honor",
            "AN 4.21 &middot; reverence and its absence",
        ]),
    ],
    further=[
        '<a href="%s/an4.43/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.44.html">AN 4.44 &middot; Valuing Anger (2nd)</a> &mdash; next in this series, '
        "the same four stated impersonally.",
        '<a href="an-4.25.html">AN 4.25 &middot; The Spiritual Life</a> &mdash; on what the life is '
        "not lived for.",
        '<a href="an-4.26.html">AN 4.26 &middot; Deceivers</a> &mdash; the other discourse whose '
        "diagnosis is arrested growth.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.44 — Dutiyakodhagarusutta
# --------------------------------------------------------------------------- #
page(
    44, "Dutiyakodhagaru", "Valuing Anger (2nd)",
    vagga=VAGGA_5,
    meta_title="AN 4.44 — Valuing Anger (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyakodhagarusutta — the "
        "same four stated as things that oppose the true teaching, with the rotten seed in a good "
        "field. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "AN 4.43 restated impersonally, with two new similes in the verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 4.43; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a mirror discourse whose verses "
                       "carry the new material"),
    ],
    why=(
        "The same four as AN 4.43, said differently: not four kinds of person but four things that "
        "<em>oppose the true teaching</em>. And the verses replace the plain statement of growth "
        "with two agricultural images &mdash; a rotten seed in a good field, and well-watered herbs "
        "&mdash; which between them say something the prose of neither discourse says."),
    guide=[
        ("The teaching in one sentence", [
            "Anger, denigration, gain, and honor are not merely valued wrongly by some people; they "
            "stand against the teaching, and where they are present nothing grows."]),
        ("From persons to forces", [
            "AN 4.43 said: four individuals are found in the world. This says: four things oppose the "
            "true teaching, <em>asaddhammā</em>. The content is identical and the grammatical subject "
            "has changed.",
            "The shift is not cosmetic. A discourse about four kinds of person invites the listener "
            "to identify who they are; a discourse about four opposing forces invites them to notice "
            "what is operating. The first is a question of classification and the second of "
            "diagnosis, and most people find the second easier to apply honestly to themselves.",
            "The collection preserving both is the same pattern seen at AN 4.17&ndash;4.19 with the "
            "prejudices: a teaching kept in more than one grammatical form because the forms are "
            "useful on different occasions."]),
        ("&lsquo;These four things are the true teaching&rsquo;", [
            "The positive half is phrased more strongly than in AN 4.43, and the phrasing is worth "
            "noticing: valuing the true teaching rather than the four <em>is</em> the true teaching. "
            "Not leads to it, not accords with it. Is it.",
            "That is a small piece of real content. It says the teaching is not only a body of "
            "statements to be valued but also the valuing &mdash; that the orientation and the "
            "content are not separable. A person who holds the true teaching above their anger is not "
            "merely respecting the Dhamma; on this sentence, they are doing it."]),
        ("The rotten seed", [
            "<em>Like a rotten seed in a good field</em> &mdash; <em>pūtibījaṁva subhūmiyaṁ</em>. The "
            "field is good. Everything external is in order: the soil, presumably the water, the "
            "season. The failure is entirely in the seed.",
            "This is a pointed image for a monastic audience, and it should be read that way. The "
            "conditions of the training &mdash; teacher, community, requisites, instruction &mdash; "
            "are the good field. Someone can be placed in all of them and still not grow, and the "
            "simile locates the reason precisely where the discourse has been locating it: not in "
            "circumstances but in what is being valued.",
            "It also quietly answers a question the collection raises elsewhere. AN 4.31 said a "
            "suitable region and true companions are two of the four wheels a life runs on. This "
            "simile grants both and shows them to be insufficient."]),
        ("The well-watered herbs", [
            "<em>Like well-watered herbs</em> &mdash; and the positive image is deliberately ordinary. "
            "Not a great tree, not a lotus, not gold: herbs, small plants, the kind that grow quickly "
            "when they are given water.",
            "Read against the rotten seed, the pair says that growth is the normal outcome of "
            "adequate conditions and that failure to grow requires an explanation. The default is "
            "that a person in the training develops. The four things named are what accounts for the "
            "cases where that does not happen."]),
        ("Reading the pair", [
            "AN 4.43 and 4.44 should be read together in one sitting; each is under a minute. Taken "
            "as a unit they give the same material in personal and impersonal form, with the "
            "impersonal version carrying both similes.",
            "For teaching, the useful sequence is the reverse of the canonical one: start with the "
            "forces and the seed, then turn to the four kinds of person. Naming what is operating "
            "before naming who one is makes the second step considerably easier to take."]),
    ],
    terms=[
        ("asaddhamma",
         "&ldquo;what opposes the true teaching&rdquo; &mdash; the term that replaces &lsquo;four "
         "individuals&rsquo; and turns the list from a classification into a diagnosis."),
        ("saddhamma",
         "&ldquo;the true teaching&rdquo; &mdash; which valuing it, on this discourse&rsquo;s "
         "phrasing, does not merely accord with but <em>is</em>."),
        ("pūtibīja",
         "&ldquo;rotten seed&rdquo; &mdash; placed in a good field, where everything external is in "
         "order and the failure is entirely in the seed."),
        ("subhūmi",
         "&ldquo;good field, good ground&rdquo; &mdash; the conditions of the training: teacher, "
         "community, requisites, instruction."),
        ("osadhī",
         "&ldquo;herbs&rdquo; &mdash; small plants that grow quickly when watered; a deliberately "
         "ordinary image for what happens when nothing is in the way."),
    ],
    text_intro=(
        "The discourse in full: the four opposing things, their mirror, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four things that oppose"),
        ("p", "&sect;1", "an4.44:1.1-1.4"),
        ("h3", "Four things that are the teaching"),
        ("p", "&sect;2", "an4.44:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.44:3.1-3.4"),
        ("p", "&sect;4", "an4.44:4.1-4.4"),
    ],
    quiz=[
        {"q": "How does AN 4.44 differ from AN 4.43?",
         "opts": [
             "It names different faults",
             "It states the same four as things that oppose the true teaching rather than as four kinds of person",
             "It is longer",
             "It addresses lay people"],
         "correct": 1,
         "expl": "The content is identical and the grammatical subject has changed."},
        {"q": "Why does the guide say that shift is not cosmetic?",
         "opts": [
             "Because the Pāli differs",
             "Because a discourse about persons invites classification, while one about forces invites diagnosis &mdash; and most people apply the second more honestly to themselves",
             "Because it changes the ranking",
             "Because it adds a fifth item"],
         "correct": 1,
         "expl": "The same pattern as AN 4.17&ndash;4.19."},
        {"q": "How is the positive half phrased?",
         "opts": [
             "That valuing the teaching leads to it",
             "That valuing the true teaching rather than the four <em>is</em> the true teaching",
             "That it accords with it",
             "That it produces merit"],
         "correct": 1,
         "expl": "Not leads to, not accords with. Is."},
        {"q": "What does the guide draw from that phrasing?",
         "opts": [
             "That the Pāli is loose",
             "That the orientation and the content are not separable &mdash; a person who holds the teaching above their anger is doing it, not merely respecting it",
             "That the verse governs",
             "That the phrase is later"],
         "correct": 1,
         "expl": "A small piece of real content."},
        {"q": "What is the first simile?",
         "opts": [
             "A fire in a grass hut",
             "A rotten seed in a good field",
             "A linchpin",
             "A lotus in water"],
         "correct": 1,
         "expl": "Everything external is in order; the failure is entirely in the seed."},
        {"q": "What does the good field stand for?",
         "opts": [
             "Past merit",
             "The conditions of the training &mdash; teacher, community, requisites, instruction",
             "A suitable rebirth",
             "The Saṅgha as a field of merit"],
         "correct": 1,
         "expl": "Someone can be placed in all of them and still not grow."},
        {"q": "Which earlier discourse does the simile quietly answer?",
         "opts": [
             "AN 4.25",
             "AN 4.31 &mdash; a suitable region and true companions are two of the four wheels, and this grants both and shows them insufficient",
             "AN 4.42",
             "AN 4.1"],
         "correct": 1,
         "expl": "A useful qualification on the earlier list."},
        {"q": "What is the second simile, and why is it ordinary?",
         "opts": [
             "A great tree &mdash; to show scale",
             "Well-watered herbs &mdash; small plants that grow quickly when given water",
             "Gold &mdash; to show value",
             "A lotus &mdash; to show purity"],
         "correct": 1,
         "expl": "Not a great tree, not a lotus, not gold."},
        {"q": "What do the two similes say together?",
         "opts": [
             "That growth is rare",
             "That growth is the normal outcome of adequate conditions, and failure to grow requires an explanation",
             "That fields matter more than seeds",
             "That water is the decisive factor"],
         "correct": 1,
         "expl": "The four things named are what accounts for the cases where it does not happen."},
        {"q": "What teaching sequence does the guide recommend?",
         "opts": [
             "The canonical order",
             "The reverse &mdash; start with the forces and the seed, then turn to the four kinds of person",
             "Verses first",
             "AN 4.44 alone"],
         "correct": 1,
         "expl": "Naming what is operating before naming who one is makes the second step easier."},
    ],
    marginalia=[
        ("The shift", [
            "4.43 &middot; four persons",
            "4.44 &middot; four forces",
            "&mdash; classification, then diagnosis",
        ]),
        ("The seed", [
            "the field is good",
            "the seed is rotten",
            "&mdash; and nothing comes up",
        ]),
        ("The herbs", [
            "small plants",
            "well watered",
            "&mdash; growth is the default",
        ]),
        ("Cross-references", [
            "AN 4.43 &middot; the personal form",
            "AN 4.31 &middot; region and companions",
            "AN 4.45 &middot; next: with Rohitassa",
        ]),
    ],
    further=[
        '<a href="%s/an4.44/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.43.html">AN 4.43 &middot; Valuing Anger</a> &mdash; the personal form, to be '
        "read with this one.",
        '<a href="an-4.31.html">AN 4.31 &middot; Situations</a> &mdash; on the region and companions '
        "that the rotten-seed simile grants and finds insufficient.",
        '<a href="an-4.45.html">AN 4.45 &middot; With Rohitassa</a> &mdash; next in this series.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.45 — Rohitassasutta
# --------------------------------------------------------------------------- #
page(
    45, "Rohitassa", "With Rohitassa",
    vagga=VAGGA_5,
    meta_title="AN 4.45 — With Rohitassa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Rohitassasutta — a godling "
        "who once walked for a hundred years trying to reach the end of the world, and the "
        "fathom-long body in which the world is described. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery, late at "
                    "night"),
        ("Speakers", "The Buddha and the godling Rohitassa"),
        ("Form", "A question, a refusal, a first-person story, a qualification, and two verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The Rohitassa episode appears at SN 2.26 and across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; one of the most quoted discourses "
                       "in the canon, and usually quoted at half length"),
    ],
    why=(
        "A god arrives at night and asks whether one can reach the end of the world by walking. The "
        "answer is no, and the god knows it: he tried, at a stride spanning ocean to ocean, for a "
        "hundred years, and died on the way. Then comes the sentence the discourse is famous for "
        "&mdash; and the sentence before it, which is almost always dropped and which changes what "
        "the famous one means."),
    guide=[
        ("The teaching in one sentence", [
            "The end of the world cannot be walked to, and cannot be skipped either: it is to be "
            "reached in this body, because this body with its perception and mind is where the world "
            "is."]),
        ("The question", [
            "Rohitassa asks whether it is possible to know, see, or reach the end of the world "
            "<em>by traveling to a place where there&rsquo;s no being born, growing old, dying, "
            "passing away, or being reborn</em>.",
            "The question is precise and it is not naive. He is not asking about geography; he is "
            "asking whether there is a location exempt from birth and death, and whether it can be "
            "gone to. That is a reasonable question within his cosmology, which contains many "
            "realms of very different durations.",
            "The answer is a flat no, given twice, and the second time with the qualification that "
            "makes the discourse."]),
        ("The story", [
            "Rohitassa was a seer with psychic powers, a sky-walker, as fast as an arrow shot across "
            "the shadow of a palm tree by an expert archer, with a stride spanning the eastern ocean "
            "to the western.",
            "He walked for a full hundred-year lifespan, <em>pausing only to eat and drink, go to the "
            "toilet, and sleep to dispel weariness</em>, and died on the way without reaching the end "
            "of the world.",
            "The specificity of that list of pauses is what makes the story land. It is not a fable "
            "about a lazy attempt. He gave the whole of a life to it, at a speed no ordinary being "
            "could approach, and stopped only for what a body cannot avoid. The failure is not a "
            "failure of effort, and the discourse takes trouble to establish that before drawing its "
            "conclusion."]),
        ("The sentence that is usually dropped", [
            "<em>But I also say there&rsquo;s no making an end of suffering without reaching the end "
            "of the world.</em>",
            "This is the half of the answer that gets lost when the discourse is quoted, and without "
            "it the teaching is unrecognizable. The Buddha does not say the end of the world is a "
            "false goal. He says it is necessary and that walking is the wrong method.",
            "Read with this sentence in place, the famous line that follows is not a redefinition "
            "away from cosmology into psychology. It is an answer to the question &lsquo;where "
            "is it?&rsquo;, given to someone who has already accepted that he has to get there."]),
        ("The fathom-long carcass", [
            "<em>For it is in this fathom-long carcass with its perception and mind that I describe "
            "the world, its origin, its cessation, and the practice that leads to its cessation.</em>",
            "<em>Byāmamatta kaḷevara</em> &mdash; a body a fathom in length, the span of the "
            "outstretched arms. <em>Kaḷevara</em> is a blunt word, used of a corpse as readily as of "
            "a living body; Sujato&rsquo;s &lsquo;carcass&rsquo; keeps that edge, where softer "
            "renderings lose it.",
            "The four-truth structure returns, with the world in the first position, as at AN 4.23. "
            "What this discourse adds is the location. The world that is to be understood, whose "
            "origin is to be given up and whose cessation realized, is found here &mdash; and "
            "&lsquo;here&rsquo; is specified with a measurement and a qualifier: <em>with its "
            "perception and mind</em>.",
            "The qualifier matters. Not the body as a lump of matter, which contains no world at all, "
            "but the body as a perceiving and thinking thing. The claim is about experience having a "
            "location, not about the world being physically inside a person."]),
        ("What the discourse does and does not claim", [
            "It is worth being careful here, because this passage is regularly made to carry more "
            "than it says. It does not say there is no external world, that the world is a mental "
            "construct, or that cosmology is metaphor. It says that the world <em>as the four truths "
            "describe it</em> &mdash; the world that can be understood and brought to cessation "
            "&mdash; is described in this experiencing body.",
            "That is a claim about where the work is done, and it is enough to answer Rohitassa. He "
            "wanted a destination; he is told the destination is not a place because the thing to be "
            "escaped is not in a place.",
            "The closing verses put it plainly: the end of the world can never be reached by "
            "traveling, and without reaching it there is no release from suffering &mdash; so an "
            "intelligent person, <em>understanding the world</em>, has completed the journey and "
            "<em>gone to the end of the world</em>. The traveling vocabulary is kept and the "
            "traveling is not."]),
    ],
    terms=[
        ("lokanta",
         "&ldquo;the end of the world&rdquo; &mdash; not denied as a goal but relocated: necessary, "
         "and not reachable by walking."),
        ("byāmamatta kaḷevara",
         "&ldquo;this fathom-long carcass&rdquo; &mdash; the span of the outstretched arms; "
         "<em>kaḷevara</em> is used of a corpse as readily as a living body."),
        ("sasaññimhi samanake",
         "&ldquo;with its perception and mind&rdquo; &mdash; the qualifier that makes the claim about "
         "the experiencing body rather than about matter."),
        ("iddhimā",
         "&ldquo;possessed of psychic powers&rdquo; &mdash; what Rohitassa was as a seer, and the "
         "reason his failure is not a failure of effort."),
        ("devaputta",
         "&ldquo;godling&rdquo; &mdash; literally a son of the gods; the questioner&rsquo;s present "
         "rebirth, recalling his life as a human seer."),
    ],
    text_intro=(
        "The discourse in full: the question, the refusal, Rohitassa&rsquo;s story, the "
        "qualification, and the verses. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A visitor at night"),
        ("p", "&sect;1", "an4.45:1.1-1.2"),
        ("h3", "The question"),
        ("p", "&sect;2", "an4.45:2.1-2.2"),
        ("h3", "Rohitassa&rsquo;s story"),
        ("p", "&sect;3", "an4.45:3.1-3.2"),
        ("p", "&sect;4", "an4.45:4.1-4.6"),
        ("p", "&sect;5", "an4.45:5.1-5.2"),
        ("h3", "In this fathom-long body"),
        ("p", "&sect;6", "an4.45:6.1-6.3"),
        ("h3", "The verses"),
        ("p", "&sect;7", "an4.45:7.1-7.4"),
        ("p", "&sect;8", "an4.45:8.1-8.4"),
    ],
    quiz=[
        {"q": "What does Rohitassa ask?",
         "opts": [
             "How long the world lasts",
             "Whether one can know, see, or reach the end of the world by traveling to a place with no birth, aging, or death",
             "Whether the world is eternal",
             "Where the gods live"],
         "correct": 1,
         "expl": "Not a question about geography but about whether there is a location exempt from birth and death."},
        {"q": "What was Rohitassa in a former life?",
         "opts": [
             "A king",
             "A seer with psychic powers, a sky-walker with a stride from the eastern ocean to the western",
             "A brahmin priest",
             "A merchant"],
         "correct": 1,
         "expl": "As fast as an arrow shot across the shadow of a palm tree."},
        {"q": "What did he stop for during his hundred years of walking?",
         "opts": [
             "Nothing",
             "Only to eat and drink, go to the toilet, and sleep to dispel weariness",
             "To teach",
             "To rest each night"],
         "correct": 1,
         "expl": "The specificity of the list is what makes the story land."},
        {"q": "Why does the guide say that detail matters?",
         "opts": [
             "It shows he was disciplined",
             "It establishes that the failure is not a failure of effort, before the conclusion is drawn",
             "It dates the story",
             "It explains his rebirth"],
         "correct": 1,
         "expl": "Not a fable about a lazy attempt."},
        {"q": "What sentence is usually dropped when the discourse is quoted?",
         "opts": [
             "The description of his speed",
             "&lsquo;There&rsquo;s no making an end of suffering without reaching the end of the world&rsquo;",
             "The setting at Sāvatthī",
             "The closing verse"],
         "correct": 1,
         "expl": "Without it the teaching is unrecognizable."},
        {"q": "How does that sentence change the famous line?",
         "opts": [
             "It does not change it",
             "It makes the famous line an answer to &lsquo;where is it?&rsquo; rather than a redefinition away from cosmology &mdash; the end of the world is necessary, and walking is the wrong method",
             "It contradicts it",
             "It restricts it to monastics"],
         "correct": 1,
         "expl": "Given to someone who has already accepted that he has to get there."},
        {"q": "What does <em>kaḷevara</em> mean?",
         "opts": [
             "A living body only",
             "A body or carcass &mdash; used of a corpse as readily as of a living body",
             "A vehicle",
             "A dwelling"],
         "correct": 1,
         "expl": "Sujato&rsquo;s &lsquo;carcass&rsquo; keeps the edge that softer renderings lose."},
        {"q": "What qualifier is attached to the body in the famous sentence?",
         "opts": [
             "&lsquo;This impermanent body&rsquo;",
             "&lsquo;With its perception and mind&rsquo;",
             "&lsquo;This human body&rsquo;",
             "&lsquo;This body of four elements&rsquo;"],
         "correct": 1,
         "expl": "The claim is about the body as a perceiving and thinking thing."},
        {"q": "What does the guide say the passage does <em>not</em> claim?",
         "opts": [
             "That the world can be understood",
             "That there is no external world, that the world is a mental construct, or that cosmology is metaphor",
             "That suffering can end",
             "That travel is possible"],
         "correct": 1,
         "expl": "It is a claim about where the work is done."},
        {"q": "What do the closing verses do with the traveling vocabulary?",
         "opts": [
             "Drop it",
             "Keep it while dropping the traveling &mdash; one who understands the world has &lsquo;gone to the end of the world&rsquo;",
             "Reverse it",
             "Apply it to gods only"],
         "correct": 1,
         "expl": "The end can never be reached by traveling, and without reaching it there is no release."},
    ],
    marginalia=[
        ("The walker", [
            "a stride ocean to ocean",
            "a hundred years",
            "&mdash; and he died on the way",
        ]),
        ("The dropped half", [
            "&ldquo;no making an end of suffering",
            "without reaching",
            "the end of the world&rdquo;",
        ]),
        ("The location", [
            "<span class=\"pali\">byāmamatta</span>a fathom long",
            "<span class=\"pali\">kaḷevara</span>carcass",
            "with perception and mind",
        ]),
        ("Cross-references", [
            "AN 4.46 &middot; next: the same, retold",
            "AN 4.23 &middot; the world in four truths",
            "AN 4.24 &middot; what is known and not conceived",
        ]),
    ],
    further=[
        '<a href="%s/an4.45/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.46.html">AN 4.46 &middot; With Rohitassa (2nd)</a> &mdash; next in this '
        "series, the same events retold to the mendicants.",
        '<a href="an-4.23.html">AN 4.23 &middot; The World</a> &mdash; the same four-truth structure '
        "with the world in the first position.",
        '<a href="an-4.41.html">AN 4.41 &middot; Ways of Developing Immersion Further</a> &mdash; on '
        "the practice by which the world is actually understood.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.46 — Dutiyarohitassasutta
# --------------------------------------------------------------------------- #
page(
    46, "Dutiyarohitassa", "With Rohitassa (2nd)",
    vagga=VAGGA_5,
    meta_title="AN 4.46 — With Rohitassa (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyarohitassasutta — the "
        "Buddha reports the previous night's visit to the mendicants, and the collection preserves "
        "the retelling as its own discourse. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta&rsquo;s Grove, the morning after the events of AN 4.45"),
        ("Speakers", "The Buddha, reporting to the mendicants"),
        ("Form", "A frame and an opening line, with the entire body abbreviated to a reference"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "As with AN 4.45; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest page in the chapter, "
                       "and about why it is short"),
    ],
    why=(
        "The night visit of AN 4.45 happened without witnesses. This discourse is the Buddha "
        "telling the mendicants about it the next morning &mdash; and the Pāli abbreviates "
        "everything after the first exchange, because the reciter already has it. What survives on "
        "the page is a frame, and the frame is the interesting part: it is the collection showing "
        "how a private conversation became a public teaching."),
    guide=[
        ("The teaching in one sentence", [
            "The same teaching as AN 4.45, given the next morning to a human audience, and preserved "
            "as a separate discourse because the audience is what changed."]),
        ("What is actually on the page", [
            "<em>Then, when the night had passed, the Buddha addressed the mendicants: &lsquo;Tonight, "
            "the glorious godling Rohitassa, lighting up the entire Jeta&rsquo;s Grove, came to me, "
            "bowed, stood to one side, and said to me&hellip;&rsquo;</em> And there the text stops. "
            "The rest is marked as identical to AN 4.45.",
            "This is a more extreme abbreviation than AN 4.40&rsquo;s. There, at least the framing "
            "exchange and the verses were written out. Here everything after the opening question is "
            "a pointer, and Sujato&rsquo;s translation marks it as such rather than silently "
            "expanding it.",
            "The text on this page is therefore short by design and not by damage, and this guide "
            "gives the substance a page of its own rather than repeating AN 4.45. Anyone reading "
            "these in order should have AN 4.45 open alongside."]),
        ("Why the retelling was kept", [
            "The obvious question is why a verbatim repetition with a different audience is preserved "
            "as its own numbered discourse. Three answers are worth giving, and they are not "
            "exclusive.",
            "First, provenance. AN 4.45 records a conversation with nobody else present. Without "
            "AN 4.46 there is no account of how the community came to know about it. The retelling is "
            "the chain of transmission written into the canon.",
            "Second, audience. A teaching given to a god and a teaching given to mendicants are "
            "different events even when the words are identical, and the Aṅguttara consistently "
            "treats the recipient as part of what a discourse is.",
            "Third, recitation. A discourse that exists mainly as a pointer still occupies a slot in "
            "the sequence, and the slot is how a reciter keeps count. The Fours are organized in "
            "chapters of ten, and every chapter of this nipāta has exactly ten."]),
        ("The night visitor as a form", [
            "Visits from gods late at night, lighting up the grove, are a standard scene in the "
            "canon &mdash; the whole of the Devatāsaṁyutta is built from them. The pattern is "
            "consistent: the visitor arrives after dark, asks one question, receives a short answer, "
            "and departs.",
            "The form is efficient. It allows a single sharp question to be posed without the social "
            "apparatus of an approach, a greeting, and a discussion, and it allows the question to "
            "come from outside the human community entirely. Rohitassa&rsquo;s question &mdash; can "
            "one walk out of birth and death? &mdash; is exactly the sort a being with psychic powers "
            "and a long memory would ask, and no human questioner in the canon is placed to ask it "
            "with the same authority.",
            "A reader who does not take the gods literally loses nothing here. The scene functions as "
            "a way of putting the strongest possible version of a question, from the one being who "
            "has actually tested it."]),
        ("What the mendicants receive", [
            "The morning retelling delivers to a human audience the two things that make AN 4.45 "
            "matter: that a being of extraordinary power tried the method and it failed, and that the "
            "end of the world is nonetheless required and is located in this body.",
            "Delivered to mendicants, the emphasis shifts slightly. Rohitassa needed to be told that "
            "his approach was wrong. The mendicants are being told, in effect, that the work they are "
            "already doing is the only method there is &mdash; and that no amount of anything else, "
            "including the psychic attainments the tradition acknowledges as real, substitutes for "
            "it.",
            "That is a common function of the god-visit scene: the visitor&rsquo;s failure is the "
            "human audience&rsquo;s encouragement."]),
        ("Reading it honestly", [
            "It would be easy to write this page as though AN 4.46 contained new material. It does "
            "not, and a study guide that pretended otherwise would be teaching a reader to see "
            "content where there is a bookmark.",
            "What it does contain is evidence about how the collection works: how it records "
            "provenance, how it treats audience, and how it manages its own repetitions. That is "
            "worth one short page, and this is it."]),
    ],
    terms=[
        ("devaputta",
         "&ldquo;godling&rdquo; &mdash; literally a son of the gods; Rohitassa&rsquo;s present "
         "rebirth, from which he recalls his life as a seer."),
        ("Jetavana",
         "&ldquo;Jeta&rsquo;s Grove&rdquo; &mdash; Anāthapiṇḍika&rsquo;s monastery at Sāvatthī, lit "
         "up by the visitor&rsquo;s arrival."),
        ("peyyāla",
         "the abbreviation convention of the Pāli canon &mdash; a marked gap the reciter fills from "
         "an adjacent text, used here for almost the whole discourse."),
        ("lokanta",
         "&ldquo;the end of the world&rdquo; &mdash; the subject carried over unchanged from "
         "AN 4.45."),
        ("byāmamatta kaḷevara",
         "&ldquo;this fathom-long carcass&rdquo; &mdash; the location given in AN 4.45, and what the "
         "mendicants receive in this retelling."),
    ],
    text_intro=(
        "The discourse as the Pāli preserves it: the frame and the opening question, with the "
        "remainder marked as identical to AN 4.45. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The morning after"),
        ("p", "&sect;1", "an4.46:1.1-1.3"),
    ],
    quiz=[
        {"q": "What is AN 4.46?",
         "opts": [
             "A new teaching to the mendicants",
             "The Buddha reporting the previous night&rsquo;s visit from Rohitassa, with everything after the opening question abbreviated",
             "A commentary on AN 4.45",
             "A verse summary"],
         "correct": 1,
         "expl": "Short by design and not by damage."},
        {"q": "How does this abbreviation compare with AN 4.40&rsquo;s?",
         "opts": [
             "It is lighter",
             "It is more extreme &mdash; there the framing exchange and verses were written out; here everything after the opening question is a pointer",
             "They are the same",
             "AN 4.40 is not abbreviated"],
         "correct": 1,
         "expl": "Sujato marks it as such rather than silently expanding it."},
        {"q": "What is the first reason the guide gives for preserving the retelling?",
         "opts": [
             "Metrical variation",
             "Provenance &mdash; AN 4.45 records a conversation with nobody else present, and without this there is no account of how the community knew of it",
             "Doctrinal difference",
             "Length"],
         "correct": 1,
         "expl": "The chain of transmission written into the canon."},
        {"q": "What is the second?",
         "opts": [
             "The verses differ",
             "Audience &mdash; the Aṅguttara consistently treats the recipient as part of what a discourse is",
             "The setting differs",
             "It was taught twice by accident"],
         "correct": 1,
         "expl": "The same words to a god and to mendicants are different events."},
        {"q": "What is the third?",
         "opts": [
             "Scribal error",
             "Recitation &mdash; a pointer still occupies a slot, and every chapter of this nipāta has exactly ten",
             "Commentarial tradition",
             "Royal patronage"],
         "correct": 1,
         "expl": "The slot is how a reciter keeps count."},
        {"q": "What is the standard form of a night visit in the canon?",
         "opts": [
             "A long philosophical exchange",
             "The visitor arrives after dark, asks one question, receives a short answer, and departs",
             "A request for ordination",
             "An offering of alms"],
         "correct": 1,
         "expl": "The whole of the Devatāsaṁyutta is built from them."},
        {"q": "Why does the guide call the form efficient?",
         "opts": [
             "It is brief",
             "It poses a sharp question without the social apparatus of approach and greeting, and lets the question come from outside the human community",
             "It requires no setting",
             "It avoids verses"],
         "correct": 1,
         "expl": "No human questioner is placed to ask Rohitassa&rsquo;s question with the same authority."},
        {"q": "What does a reader who does not take the gods literally lose here?",
         "opts": [
             "The whole teaching",
             "Nothing &mdash; the scene functions as a way of putting the strongest version of a question, from the one being who has tested it",
             "The verses",
             "The setting"],
         "correct": 1,
         "expl": "The guide leaves the question open."},
        {"q": "How does the emphasis shift when the teaching is given to mendicants?",
         "opts": [
             "It does not shift",
             "They are told that the work they are already doing is the only method &mdash; and that not even the psychic attainments substitute for it",
             "They are told to travel",
             "They are told to question gods"],
         "correct": 1,
         "expl": "The visitor&rsquo;s failure is the human audience&rsquo;s encouragement."},
        {"q": "What does the guide say this page is for?",
         "opts": [
             "Repeating AN 4.45",
             "Evidence about how the collection works &mdash; how it records provenance, treats audience, and manages its repetitions",
             "Filling a gap in the index",
             "Correcting AN 4.45"],
         "correct": 1,
         "expl": "A guide that pretended otherwise would teach a reader to see content where there is a bookmark."},
    ],
    marginalia=[
        ("What survives", [
            "the frame",
            "the opening question",
            "&mdash; and a pointer",
        ]),
        ("Why it was kept", [
            "provenance",
            "audience",
            "a slot in the ten",
        ]),
        ("The night visit", [
            "arrives after dark",
            "one question",
            "&mdash; and departs",
        ]),
        ("Cross-references", [
            "AN 4.45 &middot; the discourse this points to",
            "AN 4.40 &middot; the other heavy abbreviation",
            "AN 4.19 &middot; a teaching kept in three forms",
        ]),
    ],
    further=[
        '<a href="%s/an4.46/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.45.html">AN 4.45 &middot; With Rohitassa</a> &mdash; the discourse this one '
        "points to, and the one to read first.",
        '<a href="an-4.19.html">AN 4.19 &middot; Prejudice (3rd)</a> &mdash; the other place in these '
        "chapters where the collection preserves a teaching in more than one arrangement.",
        '<a href="an-4.47.html">AN 4.47 &middot; Very Far Apart</a> &mdash; next in this series.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.47 — Suvidūrasutta
# --------------------------------------------------------------------------- #
page(
    47, "Suvidūra", "Very Far Apart",
    vagga=VAGGA_5,
    meta_title="AN 4.47 — Very Far Apart | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Suvidūrasutta — sky and "
        "earth, the two shores of the ocean, sunrise and sunset, and furthest of all, the teaching "
        "of the virtuous from that of the wicked. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "Four distances, three physical and one not, with two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four distances appear in the Chinese Āgamas and in the "
                              "Itivuttaka; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a simple rhetorical figure with "
                       "one thoughtful line in the second verse"),
    ],
    why=(
        "Three of the largest distances the ancient world could name &mdash; sky to earth, shore to "
        "shore, sunrise to sunset &mdash; and then a fourth that is said to exceed them: the "
        "teaching of the virtuous from the teaching of the wicked. The figure is simple. What is "
        "not simple is the reason the second verse gives for the gap, which is not about the content "
        "of the two teachings at all."),
    guide=[
        ("The teaching in one sentence", [
            "The distance between good and bad teaching is greater than any physical distance, and "
            "what makes it so is reliability rather than doctrine."]),
        ("The three physical distances", [
            "The firmament and the earth; the near and far shore of the ocean; where the sun rises "
            "and where it sets. These are the three greatest spans available to the imagination of "
            "the audience, and they are chosen with care.",
            "Each is a different kind of distance. Sky to earth is vertical and unbridgeable by "
            "walking. Shore to shore is horizontal and crossable, but only by a voyage. Sunrise to "
            "sunset is the whole width of the visible world and also a distance in time.",
            "Having established three incommensurable maxima, the discourse says the fourth exceeds "
            "all of them. That is a rhetorical structure rather than an argument, and it works "
            "because the three examples do not share a scale &mdash; there is no unit in which "
            "vertical, horizontal, and temporal distance can be compared, so the fourth term is not "
            "being measured against a number."]),
        ("The fourth", [
            "<em>Dhammo sataṁ</em> and <em>dhammo asataṁ</em> &mdash; the teaching, or the way, of "
            "the good and of the bad. <em>Sant</em> is the present participle of &lsquo;to be&rsquo; "
            "used to mean the good, the true, the real; <em>asant</em> is its negation.",
            "<em>Dhamma</em> here is broader than doctrine. It covers the way such people are, what "
            "they hold, and what they teach, and the discourse does not separate these. That "
            "breadth matters for the second verse, which locates the distance in behavior rather "
            "than in belief."]),
        ("Why the distance is so great", [
            "The second verse gives the reason, and it is not the one a reader expects. Not that the "
            "wicked teach falsehood, or lead people to hell, or contradict the truths. Rather: "
            "<em>The company of the virtuous is reliable; as long as it remains, it stays the same. "
            "But the company of the wicked is fickle.</em>",
            "The Pāli behind &lsquo;reliable&rsquo; and &lsquo;fickle&rsquo; contrasts what holds "
            "steady with what does not. The distinguishing mark of good teaching, on this account, "
            "is that it is the same tomorrow &mdash; and of bad teaching, that it changes.",
            "That is a striking criterion and it is worth pressing on. It is not a claim about "
            "truth-content; it is a claim about durability under time and pressure. A teaching that "
            "has to be revised when circumstances change, or that says one thing to one audience and "
            "another to the next, is by this measure on the far side of the largest distance in the "
            "world.",
            "It also connects to a theme running through the chapter and the one before it. AN 4.28 "
            "praised four traditions for being <em>uncorrupted, as they have been since the "
            "beginning</em>; AN 4.29 and 4.30 said the same of the four footprints. This verse gives "
            "the underlying principle: what is good keeps."]),
        ("&lsquo;Company&rsquo; and the ambiguity in it", [
            "Sujato renders the subject as <em>the company of the virtuous</em> and <em>the company "
            "of the wicked</em>, which keeps a useful ambiguity in the Pāli: the word can mean the "
            "association of such people among themselves, or the experience of associating with them.",
            "Both readings work and they reinforce each other. Good people are consistent with one "
            "another and consistent to be around; bad people are neither. The verse is as much about "
            "what it is like to depend on someone as about what they believe.",
            "This is the chapter&rsquo;s quietest practical teaching. AN 4.31 named relying on true "
            "persons as one of the four wheels a life runs on. This discourse supplies the test for "
            "identifying them, and the test is not what they say but whether it stays the same."]),
        ("Using it", [
            "As a short teaching this works best read backwards: give the second verse first, then "
            "the list of distances. Stated as a criterion &mdash; look for what holds steady &mdash; "
            "it is immediately usable. Stated as a hierarchy of distances it can sound merely "
            "emphatic.",
            "The reversal also protects against the obvious misreading, which is to hear the "
            "discourse as saying that good and bad people are irreconcilably separated as kinds. "
            "Nothing in it says that. What it says is that the two ways of proceeding do not "
            "converge, which is a claim about the ways rather than about the people."]),
    ],
    terms=[
        ("suvidūra",
         "&ldquo;very far apart&rdquo; &mdash; the title, and the figure the whole discourse is built "
         "on."),
        ("nabha",
         "&ldquo;the firmament, sky&rdquo; &mdash; the first of the three physical distances, and the "
         "one unbridgeable by walking."),
        ("sant / asant",
         "&ldquo;the good&rdquo; and &ldquo;the bad&rdquo; &mdash; from the present participle of "
         "&lsquo;to be&rsquo;: the true, the real, and its negation."),
        ("dhammo sataṁ",
         "&ldquo;the teaching of the virtuous&rdquo; &mdash; broader than doctrine: the way such "
         "people are, what they hold, and what they teach."),
        ("avaṭṭhita",
         "&ldquo;reliable, steady&rdquo; &mdash; what the company of the good is, and the "
         "verse&rsquo;s actual criterion: it stays the same."),
    ],
    text_intro=(
        "The discourse in full: the four distances and the two verses. The ellipses are the "
        "Pāli&rsquo;s own abbreviation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four things very far apart"),
        ("p", "&sect;1", "an4.47:1.1-1.11"),
        ("h3", "The verses"),
        ("p", "&sect;2", "an4.47:2.1-2.6"),
        ("p", "&sect;3", "an4.47:3.1-3.4"),
    ],
    quiz=[
        {"q": "What are the four things very far apart?",
         "opts": [
             "The four continents",
             "Sky and earth, the near and far shore of the ocean, sunrise and sunset, and the teaching of the virtuous from that of the wicked",
             "Birth, aging, sickness, and death",
             "The four directions"],
         "correct": 1,
         "expl": "Three physical distances and one that is not."},
        {"q": "Why does the guide say the three physical distances are chosen with care?",
         "opts": [
             "They are all measurable",
             "Each is a different kind of distance &mdash; vertical, horizontal, and the whole width of the visible world, which is also a distance in time",
             "They are all in the sky",
             "They were familiar to sailors"],
         "correct": 1,
         "expl": "Three incommensurable maxima."},
        {"q": "How does that make the fourth claim work?",
         "opts": [
             "By measuring it against a number",
             "The three examples do not share a scale, so the fourth term is not being measured against anything &mdash; it is a rhetorical structure rather than an argument",
             "By appeal to authority",
             "By simile"],
         "correct": 1,
         "expl": "There is no unit in which vertical, horizontal, and temporal distance can be compared."},
        {"q": "What does <em>sant</em> mean?",
         "opts": [
             "Learned",
             "The good, the true, the real &mdash; from the present participle of &lsquo;to be&rsquo;",
             "Ordained",
             "Ancient"],
         "correct": 1,
         "expl": "<em>Asant</em> is its negation."},
        {"q": "What reason does the second verse give for the distance?",
         "opts": [
             "That the wicked teach falsehood",
             "That the company of the virtuous is reliable and stays the same, while the company of the wicked is fickle",
             "That the wicked lead people to hell",
             "That they contradict the four truths"],
         "correct": 1,
         "expl": "Not the reason a reader expects."},
        {"q": "What kind of criterion is that?",
         "opts": [
             "A claim about truth-content",
             "A claim about durability under time and pressure",
             "A claim about intention",
             "A claim about lineage"],
         "correct": 1,
         "expl": "A teaching that says one thing to one audience and another to the next is on the far side of the largest distance in the world."},
        {"q": "Which earlier discourses does that principle connect to?",
         "opts": [
             "AN 4.17&ndash;4.19",
             "AN 4.28, 4.29, and 4.30 &mdash; the traditions and footprints praised for being uncorrupted since the beginning",
             "AN 4.35 and 4.36",
             "AN 4.43 and 4.44"],
         "correct": 1,
         "expl": "This verse gives the underlying principle: what is good keeps."},
        {"q": "What useful ambiguity does &lsquo;company&rsquo; preserve?",
         "opts": [
             "Between monastic and lay",
             "Between the association of such people among themselves and the experience of associating with them",
             "Between past and present",
             "Between teaching and practice"],
         "correct": 1,
         "expl": "Both readings work and reinforce each other."},
        {"q": "Which earlier discourse does this supply a test for?",
         "opts": [
             "AN 4.42, on answering questions",
             "AN 4.31 &mdash; relying on true persons as one of the four wheels; the test is not what they say but whether it stays the same",
             "AN 4.45, on the end of the world",
             "AN 4.41, on immersion"],
         "correct": 1,
         "expl": "The chapter&rsquo;s quietest practical teaching."},
        {"q": "What misreading does the guide warn against?",
         "opts": [
             "That the distances are literal",
             "Hearing the discourse as saying good and bad people are irreconcilably separated as kinds &mdash; the claim is about the ways, not the people",
             "That the verses are later",
             "That it applies only to monastics"],
         "correct": 1,
         "expl": "What it says is that the two ways of proceeding do not converge."},
    ],
    marginalia=[
        ("Three distances", [
            "sky to earth",
            "shore to shore",
            "sunrise to sunset",
        ]),
        ("And the fourth", [
            "<span class=\"pali\">dhammo sataṁ</span>the good",
            "<span class=\"pali\">dhammo asataṁ</span>the bad",
            "&mdash; further than all of them",
        ]),
        ("The reason", [
            "not falsehood",
            "not doctrine",
            "&mdash; the good keeps",
        ]),
        ("Cross-references", [
            "AN 4.31 &middot; relying on true persons",
            "AN 4.28 &middot; uncorrupted since the beginning",
            "AN 4.48 &middot; next: with Visākha",
        ]),
    ],
    further=[
        '<a href="%s/an4.47/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.48.html">AN 4.48 &middot; With Visākha, Pañcāli&rsquo;s Son</a> &mdash; next '
        "in this series.",
        '<a href="an-4.31.html">AN 4.31 &middot; Situations</a> &mdash; where relying on true persons '
        "is one of the four wheels.",
        '<a href="an-4.28.html">AN 4.28 &middot; The Noble Traditions</a> &mdash; on the practices '
        "that do not degrade.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.48 — Visākhasutta
# --------------------------------------------------------------------------- #
page(
    48, "Visākha", "With Visākha, Pañcāli&rsquo;s Son",
    vagga=VAGGA_5,
    meta_title="AN 4.48 — With Visākha, Pañcāli&rsquo;s Son | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Visākhasutta — the Buddha "
        "finds a monk teaching well in the assembly hall, praises him, and says that an astute "
        "person among fools is not known until he speaks. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery, in the "
                    "assembly hall"),
        ("Speakers", "The Buddha, the mendicants, and Venerable Visākha, Pañcāli&rsquo;s son"),
        ("Form", "A short narrative, a question, praise, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The banner-of-the-seers verse appears across the Chinese Āgamas and at "
                              "SN 21.7; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a small scene carrying one "
                       "memorable claim about speech"),
    ],
    why=(
        "The Buddha comes out of retreat, hears someone teaching well, asks who it was, and praises "
        "him. Then the verse: <em>Though an astute person is mixed up with fools, they don&rsquo;t "
        "know unless he speaks.</em> It is the counterweight to every discourse in this collection "
        "that warns about talk &mdash; and there are many &mdash; and it says that silence has a "
        "cost of its own."),
    guide=[
        ("The teaching in one sentence", [
            "Wisdom is invisible until it is spoken, so the person who has it should speak."]),
        ("The scene", [
            "Visākha, Pañcāli&rsquo;s son, is <em>educating, encouraging, firing up, and inspiring</em> "
            "the mendicants in the assembly hall. That four-verb formula is the canon&rsquo;s standard "
            "description of good Dhamma teaching and it appears hundreds of times; it is worth "
            "knowing on sight.",
            "The Buddha arrives in the late afternoon, sits, and asks who was teaching. He is told. He "
            "addresses Visākha directly with <em>sādhu sādhu</em> &mdash; good, good &mdash; and "
            "repeats the description of his speech back to him.",
            "The narrative is doing something specific: the praise is public, in the hall where the "
            "teaching happened, and it is given by repeating the qualities rather than by "
            "generalizing. That is a model of how to commend work, and the discourse spends most of "
            "its prose on it."]),
        ("The six qualities of the speech", [
            "<em>Polished, clear, articulate, expressing the meaning, comprehensive, and "
            "independent.</em> The Pāli is <em>poriyā vācāya vissaṭṭhāya anelagalāya "
            "atthassa viññāpaniyā anissitāya</em>.",
            "Two of these are worth unpacking. <em>Anelagala</em>, &lsquo;articulate&rsquo;, is "
            "literally without stammering or slurring &mdash; the physical clarity of the delivery, "
            "which the canon treats as part of teaching well rather than as an incidental. And "
            "<em>anissita</em>, &lsquo;independent&rsquo;, means not relying on, not leaning on "
            "&mdash; speech that does not depend on external support.",
            "The commentaries take <em>anissita</em> as speaking without depending on gain or "
            "reputation; it can also be read as speaking without leaning on authority, from one&rsquo;s "
            "own understanding. Both readings are defensible and both describe something a listener "
            "can detect."]),
        ("The verse about being unknown", [
            "<em>Though an astute person is mixed up with fools, they don&rsquo;t know unless he "
            "speaks. But when he speaks they know, he&rsquo;s teaching the state free of death.</em>",
            "The claim is epistemological and it modifies something the collection says elsewhere. "
            "AN 3.2 in the Threes said that a person is characterized by their deeds, for wisdom "
            "shines in its traces. This verse adds the necessary qualification: among people who are "
            "not looking, or not able to read the traces, the deeds are not enough. Speech is what "
            "makes wisdom legible in an ordinary room.",
            "That is a practical observation and not a flattering one about human company. The "
            "assumption behind it is that a wise person sitting quietly among fools is simply "
            "invisible, and that no amount of inner quality corrects for this."]),
        ("The banner", [
            "<em>He should speak and illustrate the teaching, holding up the banner of the seers. "
            "Words well spoken are the seers&rsquo; banner, for the teaching is the banner of the "
            "seers.</em>",
            "<em>Isīnaṁ dhajaṁ</em> &mdash; the banner or standard of the sages. A banner is how a "
            "body of people is identified at a distance, and in a military or processional context "
            "it is what marks whose side is present.",
            "The image makes speech a public act of identification rather than a private "
            "transmission. What is being said is that the Dhamma is visible in the world only when "
            "someone says it well, and that the person who says it well is holding up the standard on "
            "behalf of everyone who holds the same teaching."]),
        ("Against the collection&rsquo;s warnings about speech", [
            "This discourse should be read against the many that go the other way. AN 4.3 warned "
            "against speaking without examination. AN 4.22 defined a childish senior by untimely and "
            "meaningless talk. AN 4.26 disowned the flatterers. AN 4.25 said the life is not lived "
            "for winning debates.",
            "None of those is contradicted here, and the difference is precise: every one of them "
            "faults a <em>kind</em> of speech, and this one faults silence in someone who could speak "
            "well. Taken together the collection is not ambivalent about talking. It is demanding "
            "about it &mdash; and this discourse supplies the other half of the demand, which is that "
            "having met the conditions, one should actually speak.",
            "For a teacher this is the discourse to hold beside the warnings. The person most likely "
            "to take AN 4.3 and AN 4.26 to heart is the person least likely to need them, and AN 4.48 "
            "is addressed to exactly that person."]),
    ],
    terms=[
        ("sandasseti samādapeti samuttejeti sampahaṁseti",
         "&ldquo;educating, encouraging, firing up, and inspiring&rdquo; &mdash; the canon&rsquo;s "
         "standard four-verb description of good Dhamma teaching."),
        ("anelagala",
         "&ldquo;articulate&rdquo; &mdash; literally without stammering or slurring; physical clarity "
         "treated as part of teaching well."),
        ("anissita",
         "&ldquo;independent&rdquo; &mdash; not leaning on: read by the commentaries as free of "
         "dependence on gain or reputation, and also readable as speaking from one&rsquo;s own "
         "understanding."),
        ("amata",
         "&ldquo;the state free of death&rdquo; &mdash; the deathless; what the astute person is "
         "recognized as teaching once he speaks."),
        ("isīnaṁ dhaja",
         "&ldquo;the banner of the seers&rdquo; &mdash; how a body of people is identified at a "
         "distance; speech as a public act of identification."),
    ],
    text_intro=(
        "The discourse in full: the scene in the assembly hall, the praise, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "In the assembly hall"),
        ("p", "&sect;1", "an4.48:1.1-1.4"),
        ("h3", "Who was teaching?"),
        ("p", "&sect;2", "an4.48:2.1-2.2"),
        ("h3", "Good, good, Visākha"),
        ("p", "&sect;3", "an4.48:3.1-3.3"),
        ("h3", "The verses"),
        ("p", "&sect;4", "an4.48:4.1-4.4"),
        ("p", "&sect;5", "an4.48:5.1-5.4"),
    ],
    quiz=[
        {"q": "What was Visākha doing?",
         "opts": [
             "Reciting the monastic code",
             "Educating, encouraging, firing up, and inspiring the mendicants with a Dhamma talk",
             "Debating a wanderer",
             "Meditating in the hall"],
         "correct": 1,
         "expl": "The canon&rsquo;s standard four-verb description of good Dhamma teaching."},
        {"q": "How does the Buddha give the praise?",
         "opts": [
             "Privately, afterward",
             "Publicly, in the hall, by repeating the qualities of the speech back to him",
             "By a verse only",
             "Through another monk"],
         "correct": 1,
         "expl": "A model of how to commend work, and the discourse spends most of its prose on it."},
        {"q": "What does <em>anelagala</em> literally mean?",
         "opts": [
             "Beautiful",
             "Without stammering or slurring",
             "Loud",
             "Brief"],
         "correct": 1,
         "expl": "Physical clarity treated as part of teaching well rather than as incidental."},
        {"q": "What are the two readings of <em>anissita</em>?",
         "opts": [
             "Long and short",
             "Not depending on gain or reputation, and speaking from one&rsquo;s own understanding rather than leaning on authority",
             "Monastic and lay",
             "Prose and verse"],
         "correct": 1,
         "expl": "Both are defensible and both describe something a listener can detect."},
        {"q": "What does the first verse claim?",
         "opts": [
             "That fools cannot be taught",
             "That an astute person among fools is not known unless he speaks",
             "That speech is dangerous",
             "That teaching requires permission"],
         "correct": 1,
         "expl": "But when he speaks they know."},
        {"q": "How does that modify AN 3.2?",
         "opts": [
             "It contradicts it",
             "AN 3.2 said wisdom shines in its traces; this adds that among people not looking, deeds are not enough &mdash; speech makes wisdom legible in an ordinary room",
             "It replaces it",
             "It restricts it to monastics"],
         "correct": 1,
         "expl": "A practical observation, and not a flattering one about human company."},
        {"q": "What is the banner of the seers?",
         "opts": [
             "The robe",
             "Words well spoken &mdash; the teaching itself, held up so it can be identified at a distance",
             "The Saṅgha",
             "The alms bowl"],
         "correct": 1,
         "expl": "A banner marks whose side is present."},
        {"q": "What does that image make speech into?",
         "opts": [
             "A private transmission",
             "A public act of identification, on behalf of everyone who holds the same teaching",
             "A ritual",
             "A debate move"],
         "correct": 1,
         "expl": "The Dhamma is visible in the world only when someone says it well."},
        {"q": "How does this sit with the chapter&rsquo;s warnings about speech?",
         "opts": [
             "It contradicts them",
             "Every one of them faults a kind of speech; this faults silence in someone who could speak well",
             "It supersedes them",
             "It applies to a different audience"],
         "correct": 1,
         "expl": "The collection is not ambivalent about talking; it is demanding about it."},
        {"q": "Who does the guide say this discourse is addressed to?",
         "opts": [
             "The talkative",
             "The person most likely to have taken AN 4.3 and AN 4.26 to heart &mdash; who is least likely to need them",
             "Senior monks only",
             "Lay teachers"],
         "correct": 1,
         "expl": "The discourse to hold beside the warnings."},
    ],
    marginalia=[
        ("Six qualities", [
            "polished, clear",
            "articulate",
            "expressing the meaning",
            "comprehensive, independent",
        ]),
        ("The claim", [
            "among fools",
            "he is not known",
            "&mdash; unless he speaks",
        ]),
        ("The banner", [
            "<span class=\"pali\">isīnaṁ dhaja</span>",
            "how a side is identified",
            "&mdash; and it is words",
        ]),
        ("Cross-references", [
            "AN 4.3 &middot; speaking without examining",
            "AN 4.26 &middot; the flatterers",
            "AN 3.2 &middot; wisdom in its traces",
        ]),
    ],
    further=[
        '<a href="%s/an4.48/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.49.html">AN 4.49 &middot; Perversions</a> &mdash; next in this series.',
        '<a href="an-3.2.html">AN 3.2 &middot; Characteristics</a> &mdash; wisdom shines in its '
        "traces, which this discourse qualifies.",
        '<a href="an-4.3.html">AN 4.3 &middot; Broken (1st)</a> &mdash; the warning this discourse '
        "should be held beside.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.49 — Vipallāsasutta
# --------------------------------------------------------------------------- #
page(
    49, "Vipallāsa", "Perversions",
    vagga=VAGGA_5,
    meta_title="AN 4.49 — Perversions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vipallāsasutta — taking "
        "impermanence as permanence, suffering as happiness, not-self as self, and ugliness as "
        "beauty: four perversions of perception, thought, and view. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "Four perversions, their four corrections, and five verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The four <em>vipallāsa</em> are a standard set across the Chinese "
                              "Āgamas and later Abhidharma; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a famous set whose three levels "
                       "are usually collapsed into one"),
    ],
    why=(
        "Four things taken for their opposites: impermanence for permanence, suffering for "
        "happiness, not-self for self, ugliness for beauty. What makes this discourse worth a page "
        "rather than a footnote is that each perversion is said to occur at three levels &mdash; "
        "perception, thought, and view &mdash; and those three are not the same mistake made three "
        "times. They are three depths at which the same mistake is held."),
    guide=[
        ("The teaching in one sentence", [
            "Four inversions run through perception, thought, and view, and correcting them at the "
            "level of view does not by itself correct them at the level of perception."]),
        ("The three levels", [
            "<em>Saññāvipallāsa, cittavipallāsa, diṭṭhivipallāsa</em> &mdash; perversion of "
            "perception, of thought, and of view. The discourse names all three in the same breath "
            "for each of the four items and does not distinguish them further.",
            "The distinction is nonetheless real and it is the most useful thing on this page. "
            "<em>Saññā</em> is the immediate recognition that arrives before any deliberation: things "
            "simply look permanent. <em>Citta</em> is the thinking that follows and runs on that "
            "recognition. <em>Diṭṭhi</em> is the position one would defend if asked.",
            "Anyone who has understood impermanence intellectually and still flinches at loss knows "
            "the difference from the inside. The view has been corrected; the perception has not. The "
            "tradition&rsquo;s account of why practice takes time is largely contained in this "
            "distinction, and the later commentarial literature says explicitly that view goes first, "
            "thought next, and perception last."]),
        ("The four items", [
            "Impermanence taken as permanence; suffering as happiness; not-self as self; ugliness as "
            "beauty. The first three are the three characteristics, in their standard order. The "
            "fourth is not one of them.",
            "<em>Asubha</em>, rendered &lsquo;ugliness&rsquo;, is more precisely the unattractive or "
            "unlovely &mdash; the term used of the body-contemplations and the cemetery practices of "
            "AN 4.14. Its inclusion turns a doctrinal list into a practical one: three propositions "
            "about existence, and one about the body in particular.",
            "It is fair to note that the fourth sits slightly awkwardly with the other three, and "
            "that translations struggle with it. &lsquo;Ugliness&rsquo; can suggest a value judgment "
            "the Pāli does not quite make. What is being denied is that the body is <em>subha</em>, "
            "attractive in the way desire presents it as being."]),
        ("What perversion means", [
            "<em>Vipallāsa</em> is a turning-about, an inversion, a reversal. Not error in general, "
            "and not ignorance in the sense of not knowing: specifically taking a thing for its "
            "opposite.",
            "That precision matters for how the discourse should be used. It is not saying that "
            "beings lack information about impermanence. It is saying that the mind actively presents "
            "the reverse, which is a stronger and stranger claim. Correction therefore cannot consist "
            "of adding a fact.",
            "The corrections given are correspondingly minimal: taking impermanence as impermanence, "
            "suffering as suffering, and so on. There is nothing to be believed that was not already "
            "there. What changes is a reversal being removed."]),
        ("The verses on derangement", [
            "The language of the verses is unusually strong. Beings so perceiving are <em>ruined by "
            "wrong view, deranged, out of their minds</em> &mdash; and then <em>yoked by "
            "Māra&rsquo;s yoke, these people find no sanctuary from the yoke</em>.",
            "That is a deliberate echo of AN 4.10, which closed the first chapter of the Fours with "
            "the four yokes and the sanctuary from them. The perversions are being identified as what "
            "the yoking consists of.",
            "&lsquo;Out of their minds&rsquo; is not rhetorical excess in context. The claim is "
            "consistent: if the mind presents things as their opposites, then the ordinary "
            "unawakened condition is a disorder of perception rather than a shortage of information, "
            "and the vocabulary of derangement is the accurate one.",
            "The verses then say a wise person hearing the Buddhas <em>gets their mind back</em> "
            "&mdash; the same image, in reverse."]),
        ("Teaching it", [
            "The four items on their own are a list students will have met before. The three levels "
            "are what makes the discourse teachable, and the best use of this page is to give the "
            "levels first and the list second.",
            "Asked in order the levels produce an honest self-assessment. What do I hold as a "
            "position? What do my thoughts assume when I am not watching them? And what does the "
            "world look like before I think about it at all? Most practitioners find their answers "
            "differ, and the discourse says that is exactly what should be expected."]),
    ],
    terms=[
        ("vipallāsa",
         "&ldquo;perversion&rdquo; &mdash; a turning-about, an inversion; specifically taking a thing "
         "for its opposite rather than error in general."),
        ("saññāvipallāsa",
         "&ldquo;perversion of perception&rdquo; &mdash; the immediate recognition that arrives "
         "before deliberation, and the last of the three to be corrected."),
        ("diṭṭhivipallāsa",
         "&ldquo;perversion of view&rdquo; &mdash; the position one would defend if asked, and the "
         "first of the three to go."),
        ("asubha",
         "&ldquo;ugliness&rdquo; &mdash; more precisely the unattractive; the term of the "
         "body-contemplations, and the one item not among the three characteristics."),
        ("ummatta",
         "&ldquo;out of their minds, deranged&rdquo; &mdash; the verses&rsquo; word, accurate rather "
         "than rhetorical if the mind presents things as their opposites."),
    ],
    text_intro=(
        "The discourse in full: the four perversions, their corrections, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four perversions"),
        ("p", "&sect;1", "an4.49:1.1-1.7"),
        ("h3", "Four corrections"),
        ("p", "&sect;2", "an4.49:2.1-2.7"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.49:3.1-4.4"),
        ("p", "&sect;4", "an4.49:5.1-6.4"),
        ("p", "&sect;5", "an4.49:7.1-7.4"),
    ],
    quiz=[
        {"q": "What are the four perversions?",
         "opts": [
             "Greed, hatred, delusion, and fear",
             "Taking impermanence as permanence, suffering as happiness, not-self as self, and ugliness as beauty",
             "Wrong view, wrong intention, wrong speech, and wrong action",
             "The four floods"],
         "correct": 1,
         "expl": "Three of them are the three characteristics; the fourth is not."},
        {"q": "At what three levels does each occur?",
         "opts": [
             "Body, speech, and mind",
             "Perception, thought, and view",
             "Past, present, and future",
             "Coarse, medium, and subtle"],
         "correct": 1,
         "expl": "Three depths at which the same mistake is held."},
        {"q": "What distinguishes the three?",
         "opts": [
             "Their objects",
             "<em>Saññā</em> is the immediate recognition before deliberation, <em>citta</em> the thinking that runs on it, and <em>diṭṭhi</em> the position one would defend",
             "Their duration",
             "Their moral weight"],
         "correct": 1,
         "expl": "Anyone who understands impermanence intellectually and still flinches at loss knows the difference from the inside."},
        {"q": "In what order does the tradition say they are corrected?",
         "opts": [
             "Perception, thought, view",
             "View first, thought next, perception last",
             "All at once",
             "Thought, view, perception"],
         "correct": 1,
         "expl": "Which contains much of the tradition&rsquo;s account of why practice takes time."},
        {"q": "What is <em>asubha</em>, and why is it awkward here?",
         "opts": [
             "Impermanence &mdash; because it repeats the first item",
             "The unattractive &mdash; the term of the body-contemplations; it is the one item not among the three characteristics, and &lsquo;ugliness&rsquo; can suggest a value judgment the Pāli does not quite make",
             "Emptiness &mdash; because it is later",
             "Suffering &mdash; because it duplicates the second"],
         "correct": 1,
         "expl": "What is denied is that the body is attractive in the way desire presents it."},
        {"q": "What does <em>vipallāsa</em> specifically mean?",
         "opts": [
             "Ignorance",
             "A turning-about or inversion &mdash; taking a thing for its opposite",
             "Forgetting",
             "Doubt"],
         "correct": 1,
         "expl": "Not error in general."},
        {"q": "Why does that precision matter?",
         "opts": [
             "It dates the term",
             "It means the mind actively presents the reverse &mdash; so correction cannot consist of adding a fact",
             "It restricts the list to four",
             "It makes the list Abhidharmic"],
         "correct": 1,
         "expl": "Beings do not lack information about impermanence."},
        {"q": "How are the corrections phrased?",
         "opts": [
             "As new propositions to believe",
             "Minimally &mdash; taking impermanence as impermanence, suffering as suffering, and so on",
             "As practices",
             "As vows"],
         "correct": 1,
         "expl": "Nothing is added; a reversal is removed."},
        {"q": "Which earlier discourse do the verses echo?",
         "opts": [
             "AN 4.1",
             "AN 4.10 &mdash; Māra&rsquo;s yoke and no sanctuary from the yoke",
             "AN 4.23",
             "AN 4.45"],
         "correct": 1,
         "expl": "The perversions are identified as what the yoking consists of."},
        {"q": "Why does the guide say &lsquo;out of their minds&rsquo; is accurate rather than excessive?",
         "opts": [
             "Because the verse is old",
             "Because if the mind presents things as their opposites, the unawakened condition is a disorder of perception rather than a shortage of information",
             "Because Māra causes it",
             "Because it is a translation choice"],
         "correct": 1,
         "expl": "And the verses say a wise person hearing the Buddhas gets their mind back."},
    ],
    marginalia=[
        ("Four inversions", [
            "impermanent &rarr; permanent",
            "suffering &rarr; happiness",
            "not-self &rarr; self",
            "unlovely &rarr; beautiful",
        ]),
        ("Three levels", [
            "<span class=\"pali\">saññā</span>perception",
            "<span class=\"pali\">citta</span>thought",
            "<span class=\"pali\">diṭṭhi</span>view",
        ]),
        ("Corrected in reverse", [
            "view first",
            "thought next",
            "perception last",
        ]),
        ("Cross-references", [
            "AN 4.10 &middot; the yoke and its sanctuary",
            "AN 4.14 &middot; the body-contemplations",
            "AN 4.50 &middot; next: four corruptions",
        ]),
    ],
    further=[
        '<a href="%s/an4.49/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.50.html">AN 4.50 &middot; Corruptions</a> &mdash; next in this series, and the '
        "last discourse of the chapter.",
        '<a href="an-4.10.html">AN 4.10 &middot; Yokes</a> &mdash; where the yoke and the sanctuary '
        "from it are set out in full.",
        '<a href="an-4.41.html">AN 4.41 &middot; Ways of Developing Immersion Further</a> &mdash; on '
        "the practice that works at the level of perception.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.50 — Upakkilesasutta
# --------------------------------------------------------------------------- #
page(
    50, "Upakkilesa", "Corruptions",
    vagga=VAGGA_5,
    meta_title="AN 4.50 — Corruptions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Upakkilesasutta — four "
        "things obscure the sun and moon, and four corrupt ascetics and brahmins: drink, sex, gold "
        "and currency, and wrong livelihood. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_5),
        ("Speakers", SPEAKER),
        ("Form", "Four obscurations, four corruptions in parallel, and four verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The sun-and-moon simile with four obscurations is widespread in the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a plain simile and a blunt list, "
                       "closing the chapter"),
    ],
    why=(
        "Four things stop the sun and moon shining: stormclouds, fog, smoke, and an eclipse. And "
        "four things stop ascetics and brahmins shining: drink, sex, accepting gold and currency, "
        "and wrong livelihood. The simile does something specific that a plain list would not "
        "&mdash; it says the light is still there."),
    guide=[
        ("The teaching in one sentence", [
            "Four practices obscure a religious life the way weather obscures the sun: the radiance "
            "is not destroyed, it is prevented from reaching anyone."]),
        ("What the simile establishes", [
            "The sun and moon do not stop shining when a cloud passes; they stop <em>shining and "
            "glowing and radiating</em> from the point of view of anyone below. Nothing has happened "
            "to the source.",
            "Applied to a person, that is a claim worth noticing. The four corruptions are not said "
            "to destroy whatever the ascetic or brahmin has developed. They are said to prevent it "
            "reaching anyone. The failure is one of transmission rather than of substance.",
            "Note also that all four obscurations are external to the sun and temporary. The simile "
            "does not carry the implication that a corrupted practitioner is finished, and the "
            "collection generally does not either. What it says is that while these things are "
            "present, nothing gets through."]),
        ("The four obscurations", [
            "Stormclouds, fog, smoke, and an eclipse of Rāhu, lord of titans. Three are weather and "
            "one is a being.",
            "Rāhu returns from AN 4.15, where he held the record for size of body. Here he is doing "
            "the thing he is actually known for in Indian cosmology: swallowing the sun or moon and "
            "producing an eclipse. Placing him last, after three natural causes, gives the list a "
            "small escalation &mdash; the first three happen, and the fourth is done by someone.",
            "It is a nice touch that the discourse does not press this. The correspondence between "
            "the four obscurations and the four corruptions is not spelled out, and it would be "
            "overreading to assign each one a partner."]),
        ("The four corruptions", [
            "Drinking beer and wine; having sex; accepting gold and currency; making a living the "
            "wrong way. Each is stated in the same form: <em>there are some ascetics and brahmins "
            "who&hellip;, not refraining from&hellip;</em>",
            "The phrasing is worth attending to. The fault is not a single lapse but a settled "
            "practice &mdash; <em>not refraining</em>, <em>appaṭivirata</em>. What is described is a "
            "person who has stopped treating the thing as something to abstain from.",
            "The four are also not addressed to Buddhist monastics specifically. The subject "
            "throughout is <em>samaṇabrāhmaṇā</em>, ascetics and brahmins &mdash; religious "
            "professionals of any school. The discourse is making a claim about what discredits "
            "anyone who has taken up a religious life, not about breaches of a particular code."]),
        ("Gold and currency", [
            "The third item is the one that has had the longest institutional life. The rule against "
            "monastics accepting gold and money is among the most consequential in the Vinaya, and "
            "disagreement over it was a live issue at the second council and has remained one ever "
            "since.",
            "It is worth being straightforward that practice varies widely today and that the "
            "discourse takes a clear position. It also does not argue for it. Like the other three, "
            "it is simply listed among the things that stop a religious life from shining, and the "
            "reason must be inferred from the pattern: each of the four involves the practitioner "
            "acquiring or consuming something that ties them back into the ordinary economy of "
            "wanting.",
            "Wrong livelihood, the fourth, generalizes that. <em>Micchājīva</em> in this literature "
            "covers the ways a religious person can make a living dishonestly &mdash; fortune-telling, "
            "flattery, hinting, and the rest, several of which AN 4.26 named as the faults of the "
            "deceivers."]),
        ("The verses, and how the chapter ends", [
            "The verses are harsher than the prose and their register is worth naming. Ascetics and "
            "brahmins so corrupted are <em>impure, dirty creatures, shrouded in darkness, "
            "bondservants of craving, full of attachments</em>, who <em>swell the horrors of the "
            "charnel ground, taking up future lives</em>.",
            "That is condemnation rather than diagnosis, and it does not sit entirely comfortably "
            "with the simile that opens the discourse. A cloud passing over the sun is a temporary "
            "obstruction; a bondservant of craving swelling the charnel ground is a settled fate. The "
            "prose and the verses are pulling in different directions and the discourse does not "
            "reconcile them.",
            "A teaching guide should say which one it is standing on. The simile is the discourse&rsquo;s "
            "own framing, stated twice, and it is the more useful and the more accurate: these four "
            "are obstructions, they are present or absent, and while they are present nothing shines. "
            "The verses are the collection&rsquo;s acclamatory-and-denunciatory voice, which it also "
            "has.",
            "The Rohitassavagga closes here. It opened with four ways of developing immersion and "
            "four ways of answering a question, ran through the god who could not walk to the end of "
            "the world, and ends with the four things that stop a religious life being visible at "
            "all. Read as a whole it is the chapter of the Fours most concerned with what makes a "
            "practice work and what stops it &mdash; and its two best pages, AN 4.41 and AN 4.45, "
            "are worth returning to independently of the rest."]),
    ],
    terms=[
        ("upakkilesa",
         "&ldquo;corruption, obscuration&rdquo; &mdash; what stops something shining. The same word "
         "is used of what obscures the sun and what obscures a person."),
        ("Rāhu",
         "lord of titans &mdash; the eclipse figure, returning from AN 4.15; the one obscuration on "
         "the list that is done by someone."),
        ("appaṭivirata",
         "&ldquo;not refraining&rdquo; &mdash; the operative phrase: a settled practice rather than a "
         "single lapse."),
        ("jātarūparajata",
         "&ldquo;gold and currency&rdquo; &mdash; the third corruption, and the one with the longest "
         "institutional history of disagreement."),
        ("micchājīva",
         "&ldquo;wrong livelihood&rdquo; &mdash; the ways a religious person can make a living "
         "dishonestly, several of which AN 4.26 named."),
    ],
    text_intro=(
        "The discourse in full: the four obscurations, the four corruptions, and the verses. The "
        "ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "What obscures the sun and moon"),
        ("p", "&sect;1", "an4.50:1.1-4.2"),
        ("h3", "What corrupts ascetics and brahmins"),
        ("p", "&sect;2", "an4.50:5.1-8.3"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.50:9.1-10.6"),
        ("p", "&sect;4", "an4.50:11.1-12.4"),
    ],
    quiz=[
        {"q": "What four things obscure the sun and moon?",
         "opts": [
             "Night, cloud, rain, and wind",
             "Stormclouds, fog, smoke, and an eclipse of Rāhu",
             "Dust, mist, cloud, and darkness",
             "The four seasons"],
         "correct": 1,
         "expl": "Three are weather and one is a being."},
        {"q": "What does the simile establish?",
         "opts": [
             "That the light is destroyed",
             "That the light is still there &mdash; nothing has happened to the source, and the failure is one of transmission",
             "That the sun is impermanent",
             "That obstruction is permanent"],
         "correct": 1,
         "expl": "The four corruptions prevent what a person has developed from reaching anyone."},
        {"q": "What further implication does the guide draw from the obscurations being external and temporary?",
         "opts": [
             "That corruption is harmless",
             "That the simile does not imply a corrupted practitioner is finished &mdash; only that while these are present, nothing gets through",
             "That the four cannot be removed",
             "That weather is a poor image"],
         "correct": 1,
         "expl": "The collection generally does not treat such a person as finished either."},
        {"q": "Where has Rāhu appeared before in the Fours?",
         "opts": [
             "AN 4.33, with the lion",
             "AN 4.15, where he held the record for size of body",
             "AN 4.45, with Rohitassa",
             "AN 4.10, among the yokes"],
         "correct": 1,
         "expl": "Here he does the thing he is actually known for."},
        {"q": "What are the four corruptions?",
         "opts": [
             "Anger, denigration, gain, and honor",
             "Drinking beer and wine, having sex, accepting gold and currency, and wrong livelihood",
             "Killing, stealing, lying, and intoxication",
             "Deceit, flattery, insolence, and distraction"],
         "correct": 1,
         "expl": "Each stated as a settled practice, not a single lapse."},
        {"q": "What does <em>appaṭivirata</em> add?",
         "opts": [
             "That the act is repeated once",
             "That the person has stopped treating the thing as something to abstain from",
             "That it is done in public",
             "That it is done knowingly"],
         "correct": 1,
         "expl": "The fault is a settled practice."},
        {"q": "Who is the discourse addressed about?",
         "opts": [
             "Buddhist monastics only",
             "<em>Samaṇabrāhmaṇā</em> &mdash; religious professionals of any school",
             "Lay followers",
             "Kings and ministers"],
         "correct": 1,
         "expl": "A claim about what discredits anyone who has taken up a religious life."},
        {"q": "What pattern does the guide infer behind the four?",
         "opts": [
             "They are all Vinaya offenses",
             "Each involves acquiring or consuming something that ties the practitioner back into the ordinary economy of wanting",
             "They are all done in secret",
             "They all involve money"],
         "correct": 1,
         "expl": "The discourse itself does not argue for the list."},
        {"q": "What tension does the guide identify between the prose and the verses?",
         "opts": [
             "None",
             "The simile makes the four temporary obstructions; the verses describe a settled fate &mdash; condemnation rather than diagnosis",
             "The verses omit an item",
             "The verses address lay people"],
         "correct": 1,
         "expl": "The discourse does not reconcile them."},
        {"q": "Which does the guide stand on, and why?",
         "opts": [
             "The verses, because they are more vivid",
             "The simile, because it is the discourse&rsquo;s own framing, stated twice, and it is the more useful and accurate",
             "Neither",
             "Both equally"],
         "correct": 1,
         "expl": "The verses are the collection&rsquo;s denunciatory voice, which it also has."},
    ],
    marginalia=[
        ("Four obscurations", [
            "stormclouds",
            "fog",
            "smoke",
            "an eclipse",
        ]),
        ("Four corruptions", [
            "drink",
            "sex",
            "gold and currency",
            "wrong livelihood",
        ]),
        ("What the simile says", [
            "the source is unharmed",
            "nothing reaches below",
            "&mdash; and clouds pass",
        ]),
        ("Cross-references", [
            "AN 4.15 &middot; Rāhu, foremost in size",
            "AN 4.26 &middot; the faults of wrong livelihood",
            "AN 4.41 &middot; where this chapter began",
        ]),
    ],
    further=[
        '<a href="%s/an4.50/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.41.html">AN 4.41 &middot; Ways of Developing Immersion Further</a> &mdash; '
        "where this chapter began.",
        '<a href="an-4.45.html">AN 4.45 &middot; With Rohitassa</a> &mdash; the chapter&rsquo;s '
        "best-known discourse, and the one it is named for.",
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; the next published page in the '
        "Fours.",
    ],
)


# --------------------------------------------------------------------------- #
# Puññābhisandavagga — the sixth chapter of the Fours
# --------------------------------------------------------------------------- #
VAGGA_6 = "<em>Puññābhisandavagga</em> &mdash; the sixth chapter of the Fours"
SETTING_6 = ("None stated; the Puññābhisandavagga gives no location for this discourse, and it is "
             "addressed to the mendicants directly")


# --------------------------------------------------------------------------- #
# AN 4.51 — Paṭhamapuññābhisandasutta
# --------------------------------------------------------------------------- #
page(
    51, "Paṭhamapuññābhisanda", "Overflowing Merit",
    vagga=VAGGA_6,
    meta_title="AN 4.51 — Overflowing Merit | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamapuññābhisandasutta — a donor's merit is limitless when the recipient enters a "
        "limitless immersion, with the simile of the rivers reaching the sea. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī &mdash; the location given in a single word, without the usual full "
                    "formula"),
        ("Speakers", SPEAKER),
        ("Form", "Four overflowings, an ocean simile, and two verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The <em>puññābhisanda</em> set and the ocean simile appear across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a claim about giving whose "
                       "mechanism is easy to miss"),
    ],
    why=(
        "Four streams of merit, one for each of the four requisites &mdash; and the condition on "
        "all four is the same: the merit is limitless when the mendicant, <em>while using</em> the "
        "gift, enters a limitless immersion of heart. The donor&rsquo;s return is not fixed by the "
        "gift. It is fixed by what the recipient does with it, which makes this a discourse about a "
        "relationship rather than a transaction."),
    guide=[
        ("The teaching in one sentence", [
            "What a gift is worth to the giver depends on what the receiver does while using it."]),
        ("<em>Abhisanda</em>: the word for a flow", [
            "<em>Puññābhisanda</em> is a stream, flow, or overflowing of merit. The image is fluid "
            "from the start, and the discourse spends its second half developing it: the ocean, its "
            "incalculable water, and the rivers that reach it.",
            "That choice of image is not decorative. A stream is continuous, arrives from elsewhere, "
            "and accumulates. Merit on this account is not a set of discrete credits but something "
            "that keeps arriving, which is why the discourse can move from four occasions of giving "
            "to an immeasurable mass without any step of multiplication."]),
        ("The condition", [
            "Each of the four is stated the same way: when a mendicant enters and remains in a "
            "<em>limitless immersion of heart</em> (<em>appamāṇa cetosamādhi</em>) while using a "
            "robe, or eating almsfood, or using lodgings, or using medicines, the overflowing of "
            "merit for the donor is limitless.",
            "The mechanism is worth stating plainly because it is easy to read past. Nothing is said "
            "about the size of the gift, the wealth of the donor, or the intention behind it. The "
            "variable is the recipient&rsquo;s state, and specifically a state entered <em>while the "
            "gift is in use</em>.",
            "<em>Appamāṇa</em>, limitless or immeasurable, is the technical term used of the four "
            "immeasurables &mdash; loving-kindness, compassion, rejoicing, equanimity &mdash; "
            "radiated without boundary in all directions. The commentarial tradition reads the phrase "
            "that way here, and the reading fits: a limitless state produces a limitless result "
            "because the result takes its measure from the state.",
            "That is the logic of the whole discourse. The donor&rsquo;s merit is unbounded not "
            "because giving is inherently unbounded but because it has been attached to something "
            "that has no boundary."]),
        ("What follows for the giver", [
            "Two things, and they pull in opposite directions.",
            "The first is encouraging. An ordinary gift &mdash; a meal, a robe &mdash; can carry a "
            "result out of all proportion to its size, so poverty is no barrier to the practice. The "
            "collection says this repeatedly and this discourse gives the reason.",
            "The second is sobering, and it is the part usually left out. If the return depends on "
            "the recipient, then the donor does not control the outcome and cannot manufacture it by "
            "giving more. What the donor controls is who they give to, which is why the collection "
            "attends so closely to the worthiness of the recipient &mdash; the field of merit of "
            "AN 4.34.",
            "It is worth saying that this can be read uncharitably, as a system for directing lay "
            "wealth to monastics. The honest response is that the criterion cuts both ways: it makes "
            "the value of what the Saṅgha receives depend entirely on how its members actually "
            "practise, which is a demanding condition to have written into the economics of one&rsquo;s "
            "own support."]),
        ("The ocean", [
            "<em>It&rsquo;s not easy to say how many gallons, how many hundreds, thousands, hundreds "
            "of thousands of gallons there are.</em> The point of the simile is not that the ocean is "
            "large but that it is not countable in the units one would naturally reach for.",
            "That is a precise thing to say about merit, and more careful than &lsquo;very much&rsquo;. "
            "The claim is that the quantity is of the wrong kind for the question, which is also how "
            "the discourse describes the noble disciple&rsquo;s merit: <em>simply reckoned as an "
            "incalculable, immeasurable, great mass</em>.",
            "The verse then supplies the second half of the image. Rivers are many and are used by "
            "many people, and all of them reach the sea. Streams of merit reach the giver the way "
            "rivers reach the ocean &mdash; from many separate sources, continuously, and without any "
            "of them needing to be tracked."]),
        ("Where it sits in the chapter", [
            "The Puññābhisandavagga is the Fours&rsquo; lay chapter, and this discourse opens it. "
            "What follows is a sequence about householders: the four kinds of marriage in AN 4.53 and "
            "4.54, the equality of Nakula&rsquo;s parents in AN 4.55, Suppavāsā and Anāthapiṇḍika "
            "giving food, and finally the four things that constitute lay practice in AN 4.60.",
            "AN 4.52, immediately next, gives a different four &mdash; confidence in the Buddha, the "
            "teaching, and the Saṅgha, and ethical conduct &mdash; under the same heading of "
            "overflowing merit. Read together the pair says that merit flows both from what one gives "
            "and from what one is."]),
    ],
    terms=[
        ("puññābhisanda",
         "&ldquo;overflowing of merit&rdquo; &mdash; a stream or flow; something continuous that "
         "keeps arriving rather than a set of discrete credits."),
        ("appamāṇa cetosamādhi",
         "&ldquo;limitless immersion of heart&rdquo; &mdash; the technical term of the four "
         "immeasurables, radiated without boundary; the condition on all four overflowings."),
        ("cattāro paccayā",
         "the four requisites &mdash; robes, almsfood, lodgings, and medicines; one stream of merit "
         "for each."),
        ("asaṅkheyya appameyya",
         "&ldquo;incalculable, immeasurable&rdquo; &mdash; the description of both the ocean&rsquo;s "
         "water and the disciple&rsquo;s merit: of the wrong kind for the question."),
        ("puññakkhetta",
         "&ldquo;field of merit&rdquo; &mdash; not used here, but the concept this discourse supplies "
         "the reason for: the donor controls who they give to, not the size of the return."),
    ],
    text_intro=(
        "The discourse in full: the four overflowings, the ocean simile, and the verses. The "
        "ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four kinds of overflowing merit"),
        ("p", "&sect;1", "an4.51:1.1-1.4"),
        ("p", "&sect;2", "an4.51:2.1-4.2"),
        ("h3", "Incalculable"),
        ("p", "&sect;3", "an4.51:5.1"),
        ("p", "&sect;4", "an4.51:6.1-6.2"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.51:7.1-7.4"),
        ("p", "&sect;6", "an4.51:8.1-8.4"),
    ],
    quiz=[
        {"q": "What condition makes the donor&rsquo;s merit limitless?",
         "opts": [
             "The size of the gift",
             "The mendicant entering a limitless immersion of heart while using the gift",
             "The donor&rsquo;s intention",
             "Giving to many recipients"],
         "correct": 1,
         "expl": "The variable is the recipient&rsquo;s state, entered while the gift is in use."},
        {"q": "What does <em>abhisanda</em> mean, and why does the image matter?",
         "opts": [
             "&lsquo;Store&rsquo; &mdash; merit accumulates like treasure",
             "&lsquo;Stream, overflowing&rsquo; &mdash; something continuous that keeps arriving, not a set of discrete credits",
             "&lsquo;Seed&rsquo; &mdash; merit grows",
             "&lsquo;Debt&rsquo; &mdash; merit is owed"],
         "correct": 1,
         "expl": "Which is why the discourse can move to an immeasurable mass without multiplying."},
        {"q": "What is <em>appamāṇa cetosamādhi</em>?",
         "opts": [
             "The fourth absorption",
             "A limitless immersion of heart &mdash; the technical term of the four immeasurables, radiated without boundary",
             "Momentary concentration",
             "Insight into the aggregates"],
         "correct": 1,
         "expl": "A limitless state produces a limitless result because the result takes its measure from the state."},
        {"q": "What are the four occasions?",
         "opts": [
             "Morning, noon, evening, and night",
             "Using a robe, eating almsfood, using lodgings, and using medicines",
             "Giving, ethics, meditation, and wisdom",
             "The four assemblies"],
         "correct": 1,
         "expl": "One stream of merit for each of the four requisites."},
        {"q": "What is the encouraging consequence for a giver?",
         "opts": [
             "That giving more produces more",
             "That an ordinary gift can carry a result out of all proportion to its size, so poverty is no barrier",
             "That merit is guaranteed",
             "That the gift returns in this life"],
         "correct": 1,
         "expl": "The collection says this repeatedly, and this discourse gives the reason."},
        {"q": "What is the sobering consequence, usually left out?",
         "opts": [
             "That merit runs out",
             "That the donor does not control the outcome and cannot manufacture it by giving more &mdash; what they control is who they give to",
             "That giving is optional",
             "That merit cannot be shared"],
         "correct": 1,
         "expl": "Which is why the collection attends so closely to the worthiness of the recipient."},
        {"q": "How does the guide answer the uncharitable reading of the doctrine?",
         "opts": [
             "By denying it",
             "By noting the criterion cuts both ways &mdash; it makes the value of what the Saṅgha receives depend on how its members actually practise",
             "By citing the commentary",
             "By restricting it to monastics"],
         "correct": 1,
         "expl": "A demanding condition to have written into the economics of one&rsquo;s own support."},
        {"q": "What is the point of the ocean simile?",
         "opts": [
             "That the ocean is large",
             "That it is not countable in the units one would naturally reach for &mdash; the quantity is of the wrong kind for the question",
             "That water is precious",
             "That the sea is dangerous"],
         "correct": 1,
         "expl": "More careful than &lsquo;very much&rsquo;."},
        {"q": "What does the river verse add?",
         "opts": [
             "That merit can be lost",
             "That streams of merit reach the giver from many separate sources, continuously, without any of them needing to be tracked",
             "That rivers are impermanent",
             "That the ocean is the goal"],
         "correct": 1,
         "expl": "Rivers are many and are used by many, and all reach the sea."},
        {"q": "How does AN 4.52 complement this discourse?",
         "opts": [
             "It repeats it",
             "It gives a different four &mdash; confidence in the Buddha, teaching, and Saṅgha, and ethical conduct &mdash; under the same heading, so merit flows from what one is as well as what one gives",
             "It contradicts it",
             "It addresses monastics only"],
         "correct": 1,
         "expl": "The chapter is the Fours&rsquo; lay chapter, and this pair opens it."},
    ],
    marginalia=[
        ("Four occasions", [
            "a robe",
            "almsfood",
            "lodgings",
            "medicines",
        ]),
        ("The variable", [
            "not the gift",
            "not the giver",
            "&mdash; the recipient&rsquo;s state",
        ]),
        ("The ocean", [
            "not &lsquo;very much&rsquo;",
            "not countable in gallons",
            "&mdash; the wrong kind of quantity",
        ]),
        ("Cross-references", [
            "AN 4.52 &middot; next: merit from what one is",
            "AN 4.34 &middot; the supreme field of merit",
            "AN 4.60 &middot; what lay practice is",
        ]),
    ],
    further=[
        '<a href="%s/an4.51/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.52.html">AN 4.52 &middot; Overflowing Merit (2nd)</a> &mdash; next in this '
        "series, and the other half of the pair.",
        '<a href="an-4.34.html">AN 4.34 &middot; The Best Kinds of Confidence</a> &mdash; on the '
        "Saṅgha as the supreme field of merit.",
        '<a href="an-4.60.html">AN 4.60 &middot; Lay Practice</a> &mdash; where this chapter ends, '
        "with the four things a layperson does.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.52 — Dutiyapuññābhisandasutta
# --------------------------------------------------------------------------- #
page(
    52, "Dutiyapuññābhisanda", "Overflowing Merit (2nd)",
    vagga=VAGGA_6,
    meta_title="AN 4.52 — Overflowing Merit (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyapuññābhisandasutta — experiential confidence in the Buddha, the teaching, and the "
        "Saṅgha, and ethical conduct loved by the noble ones. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_6),
        ("Speakers", SPEAKER),
        ("Form", "Four items, each with its standard recollection formula, and three verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The four factors of stream-entry are widespread in the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; four familiar formulas whose "
                       "collective name is worth knowing"),
    ],
    why=(
        "The same heading as AN 4.51 &mdash; overflowing merit &mdash; with a completely different "
        "four. Not four occasions of giving but four possessions: confidence in the Buddha, in the "
        "teaching, in the Saṅgha, and ethical conduct that the noble ones love. This set is one of "
        "the most consequential in the canon, and it is worth reading here in its plainest form."),
    guide=[
        ("The teaching in one sentence", [
            "Merit flows continuously from four things a person <em>has</em>, without any occasion of "
            "giving being required."]),
        ("The four factors", [
            "This set is known throughout the tradition as the four factors of stream-entry &mdash; "
            "<em>sotāpattiyaṅga</em> &mdash; or the four <em>sotāpannassa aṅgāni</em>, the "
            "characteristics of a stream-enterer. Elsewhere in the canon they are the standard "
            "answer to how one knows one has entered the stream.",
            "That is not said here. This discourse gives them under a different heading, as sources "
            "of overflowing merit, and a reader meeting them for the first time should meet them that "
            "way. What is claimed in this discourse is that having these four is itself a continuous "
            "production of merit.",
            "The difference from AN 4.51 is the important structural point. There, merit arose on "
            "occasions and depended on someone else. Here it arises from a standing condition of the "
            "person and depends on nobody. Together the two discourses cover both ways the collection "
            "talks about merit."]),
        ("&lsquo;Experiential confidence&rsquo;", [
            "<em>Aveccappasāda</em> &mdash; Sujato&rsquo;s &lsquo;experiential confidence&rsquo;. "
            "<em>Avecca</em> is from a verb meaning to go into, to penetrate, to understand; "
            "<em>pasāda</em> is clarity, brightness, confidence.",
            "The compound is regularly translated &lsquo;unshakable&rsquo; or &lsquo;perfect&rsquo; "
            "faith. Sujato&rsquo;s rendering picks up the other element: this is confidence arrived "
            "at by having gone into the matter, not confidence held firmly. The two are different "
            "claims and the Pāli supports the second.",
            "That reading fits the third item in the Dhamma formula &mdash; <em>inviting "
            "inspection</em>, <em>ehipassika</em>, come-and-see. A tradition that describes its "
            "teaching as inviting inspection and its adherents&rsquo; confidence as arrived at by "
            "penetration is being consistent."]),
        ("The three recollection formulas", [
            "Each of the first three items is given with its standard formula, and these are among "
            "the most-recited passages in Theravāda practice, used daily as objects of recollection.",
            "The Buddha formula lists nine epithets, from <em>perfected</em> to <em>blessed</em>. The "
            "Dhamma formula gives six qualities, of which the middle four are the most useful to "
            "teach: apparent in the present life, immediately effective, inviting inspection, "
            "relevant &mdash; every one of them a claim about availability now rather than about "
            "truth. The Saṅgha formula defines the community as the four pairs and eight persons and "
            "calls it the supreme field of merit, exactly as AN 4.34 did.",
            "It is worth pointing out to students that these are liturgical texts as much as "
            "doctrinal ones. They are meant to be said, and their rhythm is part of how they work."]),
        ("The fourth item is not confidence", [
            "The fourth breaks the pattern: not confidence in something, but one&rsquo;s own ethical "
            "conduct &mdash; <em>loved by the noble ones, unbroken, impeccable, spotless, unmarred, "
            "liberating, praised by sensible people, not mistaken, and leading to immersion</em>.",
            "The list of nine adjectives is doing work. Four are negative (unbroken, impeccable, "
            "spotless, unmarred) and describe conduct with no gaps in it. Three concern how it is "
            "regarded. And two &mdash; <em>liberating</em> and <em>leading to immersion</em> &mdash; "
            "say what it does.",
            "That last pair is the reason the item belongs on this list. Ethics here is not a "
            "prerequisite or a moral achievement but something with a direction: it goes somewhere, "
            "and where it goes is immersion. The set as a whole therefore has three items of "
            "orientation and one of practice, and the practice item is the one that moves."]),
        ("The verses and what they substitute", [
            "The verses run through the four but replace the fourth with something else: faith in the "
            "Realized One, good ethical conduct, confidence in the Saṅgha, and <em>correct view</em> "
            "&mdash; <em>diṭṭhi ca yassa ujukā</em>, whose view is straight.",
            "So the verse gives faith, ethics, confidence, and right view, and the closing verse "
            "names four again: <em>faith, ethical behavior, confidence, and insight into the "
            "teaching</em>.",
            "This kind of slippage between prose and verse is common in the collection and is worth "
            "noticing rather than harmonizing. The prose set is fixed and technical; the verses reach "
            "for a related but looser group. A reader who learns the prose list will recognize the "
            "verses; a reader who learns only the verses will have a slightly different set."]),
    ],
    terms=[
        ("aveccappasāda",
         "&ldquo;experiential confidence&rdquo; &mdash; <em>avecca</em> is from a verb meaning to go "
         "into or penetrate: confidence arrived at, not confidence held firmly."),
        ("sotāpattiyaṅga",
         "&ldquo;factor of stream-entry&rdquo; &mdash; the name this set carries elsewhere in the "
         "canon, though this discourse gives it under a different heading."),
        ("ehipassika",
         "&ldquo;inviting inspection&rdquo;, literally come-and-see &mdash; one of the six qualities "
         "of the teaching, and consistent with the sense of <em>avecca</em>."),
        ("ariyakanta sīla",
         "&ldquo;ethical conduct loved by the noble ones&rdquo; &mdash; the fourth item, described by "
         "nine adjectives of which two say what it does."),
        ("samādhisaṁvattanika",
         "&ldquo;leading to immersion&rdquo; &mdash; the last of the nine, and the reason ethics "
         "belongs on a list otherwise made of orientations."),
    ],
    text_intro=(
        "The discourse in full: the four kinds of overflowing merit and the verses. The ellipses are "
        "the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Confidence in the Buddha"),
        ("p", "&sect;1", "an4.52:1.1-1.5"),
        ("h3", "Confidence in the teaching"),
        ("p", "&sect;2", "an4.52:2.1-2.3"),
        ("h3", "Confidence in the Saṅgha"),
        ("p", "&sect;3", "an4.52:3.1-3.3"),
        ("h3", "Ethical conduct"),
        ("p", "&sect;4", "an4.52:4.1-4.3"),
        ("h3", "The verses"),
        ("p", "&sect;5", "an4.52:5.1-6.4"),
        ("p", "&sect;6", "an4.52:7.1-7.4"),
    ],
    quiz=[
        {"q": "What are the four kinds of overflowing merit here?",
         "opts": [
             "Four occasions of giving",
             "Experiential confidence in the Buddha, the teaching, and the Saṅgha, and ethical conduct loved by the noble ones",
             "Ethics, immersion, wisdom, and freedom",
             "Faith, energy, mindfulness, and wisdom"],
         "correct": 1,
         "expl": "Four possessions rather than four occasions."},
        {"q": "What is this set known as elsewhere in the canon?",
         "opts": [
             "The four right efforts",
             "The four factors of stream-entry",
             "The four immeasurables",
             "The four bases of psychic power"],
         "correct": 1,
         "expl": "Though this discourse gives them under a different heading."},
        {"q": "How does this discourse differ structurally from AN 4.51?",
         "opts": [
             "It is longer",
             "There merit arose on occasions and depended on someone else; here it arises from a standing condition and depends on nobody",
             "It addresses monastics",
             "It uses no simile"],
         "correct": 1,
         "expl": "Together the two cover both ways the collection talks about merit."},
        {"q": "What does <em>avecca</em> contribute to <em>aveccappasāda</em>?",
         "opts": [
             "Firmness",
             "The sense of having gone into or penetrated the matter &mdash; confidence arrived at, not confidence held firmly",
             "Duration",
             "Purity"],
         "correct": 1,
         "expl": "Two different claims, and the Pāli supports the second."},
        {"q": "Which quality of the teaching does that reading fit?",
         "opts": [
             "Well explained",
             "<em>Ehipassika</em>, inviting inspection &mdash; come and see",
             "Immediately effective",
             "Relevant"],
         "correct": 1,
         "expl": "A tradition describing its teaching as inviting inspection is being consistent."},
        {"q": "What do the middle four qualities of the Dhamma formula have in common?",
         "opts": [
             "They concern the Buddha",
             "Every one is a claim about availability now rather than about truth",
             "They concern the Saṅgha",
             "They are negative"],
         "correct": 1,
         "expl": "Apparent in the present life, immediately effective, inviting inspection, relevant."},
        {"q": "How does the fourth item break the pattern?",
         "opts": [
             "It is shorter",
             "It is not confidence in something but one&rsquo;s own ethical conduct",
             "It concerns others",
             "It is in verse"],
         "correct": 1,
         "expl": "Described by nine adjectives."},
        {"q": "Which two of those nine explain why ethics belongs on the list?",
         "opts": [
             "Unbroken and spotless",
             "Liberating, and leading to immersion &mdash; the two that say what it does",
             "Praised and loved",
             "Impeccable and unmarred"],
         "correct": 1,
         "expl": "Ethics here is not a prerequisite but something with a direction."},
        {"q": "What does the verse substitute for the fourth item?",
         "opts": [
             "Generosity",
             "Correct view &mdash; and the closing verse names insight into the teaching",
             "Energy",
             "Learning"],
         "correct": 1,
         "expl": "The verses reach for a related but looser group."},
        {"q": "How does the guide recommend handling that slippage?",
         "opts": [
             "Harmonize the two lists",
             "Notice it rather than harmonize it &mdash; the prose set is fixed and technical, the verses are not",
             "Prefer the verses",
             "Treat the verses as spurious"],
         "correct": 1,
         "expl": "A reader who learns only the verses will have a slightly different set."},
    ],
    marginalia=[
        ("The four", [
            "confidence in the Buddha",
            "confidence in the teaching",
            "confidence in the Saṅgha",
            "ethical conduct",
        ]),
        ("The word", [
            "<span class=\"pali\">avecca</span>having gone into",
            "<span class=\"pali\">pasāda</span>clarity",
            "&mdash; arrived at, not held",
        ]),
        ("Nine adjectives", [
            "four say: no gaps",
            "three say: well regarded",
            "two say: it goes somewhere",
        ]),
        ("Cross-references", [
            "AN 4.51 &middot; merit from occasions",
            "AN 4.34 &middot; the same Saṅgha formula",
            "AN 4.53 &middot; next: four marriages",
        ]),
    ],
    further=[
        '<a href="%s/an4.52/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.53.html">AN 4.53 &middot; Living Together (1st)</a> &mdash; next in this '
        "series.",
        '<a href="an-4.51.html">AN 4.51 &middot; Overflowing Merit</a> &mdash; the other half of the '
        "pair, on merit that arises from occasions.",
        '<a href="an-4.34.html">AN 4.34 &middot; The Best Kinds of Confidence</a> &mdash; where the '
        "same Saṅgha formula appears.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.53 — Paṭhamasaṁvāsasutta
# --------------------------------------------------------------------------- #
page(
    53, "Paṭhamasaṁvāsa", "Living Together (1st)",
    vagga=VAGGA_6,
    meta_title="AN 4.53 — Living Together (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamasaṁvāsasutta — four "
        "kinds of marriage, sorted by the ethics of each partner: zombie with zombie, zombie with "
        "goddess, god with zombie, god with goddess. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "On the road between Madhurā and Verañjā, at the root of a tree, with "
                    "householders both women and men travelling the same way"),
        ("Speakers", "The Buddha, addressing householders"),
        ("Form", "A two-by-two grid of marriages, each defined by conduct, with six verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The four <em>saṁvāsa</em> appear in the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain in structure, with one "
                       "translation choice that needs explaining"),
    ],
    why=(
        "Four kinds of marriage, named by what each partner is: a corpse living with a corpse, a "
        "corpse with a goddess, a god with a corpse, a god with a goddess. The grid is symmetrical "
        "and the criterion is entirely ethical &mdash; the five precepts, stinginess, and how one "
        "treats ascetics and brahmins. It is one of the few discourses addressed to a mixed lay "
        "audience by the roadside, and the symmetry of its treatment of husband and wife is worth "
        "noticing."),
    guide=[
        ("The teaching in one sentence", [
            "A marriage is characterized by the ethical condition of each partner independently, and "
            "there are four possible combinations."]),
        ("&lsquo;Zombie&rsquo; and what it translates", [
            "The Pāli is <em>chava</em>, a corpse or carcass, used as a term of abuse &mdash; roughly "
            "&lsquo;wretch&rsquo; with the force of &lsquo;dead thing&rsquo;. Sujato&rsquo;s "
            "&lsquo;zombie&rsquo; is a deliberate and unusual choice; other translators have used "
            "&lsquo;wretch&rsquo;, &lsquo;corpse&rsquo;, or &lsquo;wretched man&rsquo;.",
            "The rendering is defensible and worth understanding rather than either adopting or "
            "dismissing. What <em>chava</em> conveys is a living person described as a dead one, "
            "which is exactly the modern sense of the word Sujato chose; &lsquo;corpse&rsquo; loses "
            "the fact that the person is walking around, and &lsquo;wretch&rsquo; loses the death.",
            "It is fair to say the English carries connotations from film that the Pāli does not, and "
            "a teacher may reasonably prefer to give both the Pāli and a plainer gloss. What should "
            "not be lost is the harshness. The discourse is not being gentle: it calls an unethical "
            "husband or wife a dead thing."]),
        ("The criterion", [
            "For each partner the description is the same and it has three parts: the five precepts "
            "(killing, stealing, sexual misconduct, lying, intoxicants); <em>living at home with the "
            "heart full of the stain of stinginess</em>; and <em>abusing and insulting ascetics and "
            "brahmins</em>.",
            "So: personal conduct, disposition toward one&rsquo;s own household, and behavior toward "
            "the religious. It is a lay standard, appropriate to the audience, and it is the same for "
            "both partners without a single word of difference.",
            "That symmetry is the discourse&rsquo;s quietest and strongest feature. Nothing in it "
            "assigns a different standard to husband and wife, and the four cells of the grid are "
            "given equal treatment: a good wife with a bad husband and a good husband with a bad wife "
            "each get their own cell, their own definition, and their own verse. For a text of its "
            "period this is worth pointing out."]),
        ("The verses and where the imbalance appears", [
            "The verses run the same four cases and here a small asymmetry does show. When the "
            "husband is unethical and the wife is not, <em>she&rsquo;s a goddess living with a zombie "
            "for a husband</em>. When the husband is ethical and the wife is not, <em>she&rsquo;s a "
            "zombie living with a god for a husband</em>.",
            "Both verses are told from the wife&rsquo;s position &mdash; she is the subject in each "
            "&mdash; whereas the prose named the husband first throughout. That is a difference of "
            "framing rather than of standard, and it is the kind of detail worth noticing without "
            "building much on it.",
            "The fourth verse is the one usually quoted: when both are faithful and bountiful, "
            "disciplined, living righteously, <em>then wife and husband say nice things to each "
            "other</em>. The Pāli is <em>piyaṁvadā</em>, speaking pleasantly &mdash; and it is "
            "notable that what the discourse names as the result of shared ethics is neither "
            "prosperity nor rebirth but how the two of them talk."]),
        ("The rest of the good outcome", [
            "The following verses do add the material results: needs amply satisfied, living at ease, "
            "enemies downhearted, and finally delight in the heavenly realm.",
            "<em>Their enemies are downhearted</em> is an unusual line and worth pausing on. The "
            "assumption is that a household has adversaries and that a well-ordered one disappoints "
            "them. This is a discourse for people with property, obligations, and rivals, and it does "
            "not pretend otherwise."]),
        ("The setting", [
            "The Buddha is travelling between Madhurā and Verañjā, leaves the road, and sits under a "
            "tree; householders travelling the same way see him and come over. The teaching is given "
            "on the roadside to whoever happened to be walking.",
            "That is worth registering because it explains the pitch. There is no request, no "
            "question, and no prior relationship. The discourse is what the Buddha says to a group of "
            "married lay people he has just met, and its content &mdash; a simple grid, a memorable "
            "and slightly rude image, verses that can be carried away &mdash; is shaped for exactly "
            "that.",
            "AN 4.54, immediately next, gives the same grid to mendicants with the ten courses of "
            "action in place of the five precepts. The pair shows the collection adapting one "
            "teaching to two audiences."]),
    ],
    terms=[
        ("chava",
         "&ldquo;zombie&rdquo; &mdash; literally a corpse, used as abuse. A living person described "
         "as a dead one; other translators use &lsquo;wretch&rsquo; or &lsquo;corpse&rsquo;."),
        ("devī",
         "&ldquo;goddess&rdquo; &mdash; the opposite term, with <em>deva</em> for the husband; the "
         "grid is built on this single pair."),
        ("saṁvāsa",
         "&ldquo;living together&rdquo; &mdash; the word for cohabitation and for marriage, and the "
         "title of both this discourse and the next."),
        ("maccheramala",
         "&ldquo;the stain of stinginess&rdquo; &mdash; the disposition named alongside the precepts, "
         "and the one that concerns the household itself."),
        ("piyaṁvadā",
         "&ldquo;saying nice things to each other&rdquo; &mdash; speaking pleasantly; what the "
         "discourse names as the first result of shared ethics."),
    ],
    text_intro=(
        "The discourse in full: the roadside setting, the four kinds of living together, and the "
        "verses. The ellipses are the Pāli&rsquo;s own abbreviation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "On the road"),
        ("p", "&sect;1", "an4.53:1.1-1.5"),
        ("h3", "Four ways of living together"),
        ("p", "&sect;2", "an4.53:2.1-2.6"),
        ("p", "&sect;3", "an4.53:3.1-3.4"),
        ("p", "&sect;4", "an4.53:4.1-4.4"),
        ("p", "&sect;5", "an4.53:5.1-5.4"),
        ("p", "&sect;6", "an4.53:6.1-6.5"),
        ("h3", "The verses"),
        ("p", "&sect;7", "an4.53:7.1-9.6"),
        ("p", "&sect;8", "an4.53:10.1-12.4"),
    ],
    quiz=[
        {"q": "What are the four ways of living together?",
         "opts": [
             "By age, wealth, caste, and region",
             "Zombie with zombie, zombie with goddess, god with zombie, and god with goddess",
             "By arrangement, love, duty, and convenience",
             "The four assemblies"],
         "correct": 1,
         "expl": "A two-by-two grid built on a single pair of terms."},
        {"q": "What does <em>chava</em> literally mean?",
         "opts": [
             "Fool",
             "A corpse or carcass, used as a term of abuse",
             "Slave",
             "Outcaste"],
         "correct": 1,
         "expl": "A living person described as a dead one."},
        {"q": "How does the guide assess Sujato&rsquo;s &lsquo;zombie&rsquo;?",
         "opts": [
             "As a mistranslation",
             "As defensible &mdash; &lsquo;corpse&rsquo; loses that the person is walking around and &lsquo;wretch&rsquo; loses the death &mdash; while noting the English carries film connotations the Pāli does not",
             "As too gentle",
             "As the only possible rendering"],
         "correct": 1,
         "expl": "What should not be lost is the harshness."},
        {"q": "What three parts make up the criterion for each partner?",
         "opts": [
             "Faith, generosity, and wisdom",
             "The five precepts, freedom from the stain of stinginess, and how one treats ascetics and brahmins",
             "Birth, conduct, and learning",
             "Wealth, health, and reputation"],
         "correct": 1,
         "expl": "Personal conduct, disposition toward one&rsquo;s household, and behavior toward the religious."},
        {"q": "What does the guide call the discourse&rsquo;s quietest and strongest feature?",
         "opts": [
             "The verses",
             "The symmetry &mdash; the same standard for both partners, with all four cells given equal treatment",
             "The roadside setting",
             "The heavenly result"],
         "correct": 1,
         "expl": "For a text of its period this is worth pointing out."},
        {"q": "What small asymmetry appears in the verses?",
         "opts": [
             "The wife is judged more harshly",
             "Both middle verses are told from the wife&rsquo;s position, whereas the prose named the husband first",
             "Only the husband is named",
             "The wife has no verse"],
         "correct": 1,
         "expl": "A difference of framing rather than of standard."},
        {"q": "What is named as the first result of shared ethics?",
         "opts": [
             "Wealth",
             "That wife and husband say nice things to each other",
             "Rebirth in heaven",
             "Long life"],
         "correct": 1,
         "expl": "<em>Piyaṁvadā</em> &mdash; neither prosperity nor rebirth but how the two of them talk."},
        {"q": "What is unusual about &lsquo;their enemies are downhearted&rsquo;?",
         "opts": [
             "Nothing",
             "It assumes a household has adversaries and that a well-ordered one disappoints them",
             "It contradicts the precepts",
             "It refers to Māra"],
         "correct": 1,
         "expl": "A discourse for people with property, obligations, and rivals."},
        {"q": "How did the teaching come to be given?",
         "opts": [
             "By invitation to a house",
             "On the roadside &mdash; householders travelling the same way saw the Buddha under a tree and came over",
             "At a festival",
             "In answer to a question"],
         "correct": 1,
         "expl": "No request, no question, and no prior relationship."},
        {"q": "How does AN 4.54 differ from this discourse?",
         "opts": [
             "It reverses the grid",
             "It gives the same grid to mendicants with the ten courses of action in place of the five precepts",
             "It omits the verses only",
             "It addresses only wives"],
         "correct": 1,
         "expl": "The pair shows one teaching adapted to two audiences."},
    ],
    marginalia=[
        ("The grid", [
            "zombie &amp; zombie",
            "zombie &amp; goddess",
            "god &amp; zombie",
            "god &amp; goddess",
        ]),
        ("The criterion", [
            "the five precepts",
            "the stain of stinginess",
            "ascetics and brahmins",
        ]),
        ("The first result", [
            "not wealth",
            "not heaven",
            "&mdash; they speak pleasantly",
        ]),
        ("Cross-references", [
            "AN 4.54 &middot; next: the same, to mendicants",
            "AN 4.55 &middot; Nakula&rsquo;s parents",
            "AN 4.51 &middot; where the lay chapter opened",
        ]),
    ],
    further=[
        '<a href="%s/an4.53/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.54.html">AN 4.54 &middot; Living Together (2nd)</a> &mdash; next in this '
        "series, the same grid with the ten courses of action.",
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; the couple who wanted to see '
        "each other in the next life, and the four things they were told to match.",
        '<a href="an-4.60.html">AN 4.60 &middot; Lay Practice</a> &mdash; where this chapter ends.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.54 — Dutiyasaṁvāsasutta
# --------------------------------------------------------------------------- #
page(
    54, "Dutiyasaṁvāsa", "Living Together (2nd)",
    vagga=VAGGA_6,
    next=("an-4.55.html", "AN 4.55 &middot; Equality"),
    meta_title="AN 4.54 — Living Together (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyasaṁvāsasutta — the "
        "same four kinds of marriage given to mendicants, with the ten courses of action in place of "
        "the five precepts. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_6),
        ("Speakers", SPEAKER),
        ("Form", "AN 4.53&rsquo;s grid restated to a monastic audience with a fuller ethical "
                 "standard; the verses are abbreviated away"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "As with AN 4.53; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a variant whose one change is the "
                       "whole of its content"),
    ],
    why=(
        "The same four marriages, the same terms, the same structure &mdash; and one substitution. "
        "Where AN 4.53 defined a partner by the five precepts, this defines them by the ten courses "
        "of action. The audience has also changed: the roadside householders are gone and the "
        "discourse is addressed to mendicants. The pair is a small, clear demonstration of how the "
        "collection adapts a teaching to who is listening."),
    guide=[
        ("The teaching in one sentence", [
            "The four kinds of marriage again, assessed by the full tenfold standard of action rather "
            "than the lay five."]),
        ("The ten courses of action", [
            "<em>Kammapatha</em>, courses of action: three bodily (killing, stealing, sexual "
            "misconduct), four verbal (false, backbiting, harsh, and nonsensical speech), and three "
            "mental (covetousness, malice, wrong view).",
            "Set against AN 4.53&rsquo;s five precepts the differences are exact. The tenfold list "
            "drops intoxicants, expands lying into four kinds of wrong speech, and adds three mental "
            "items that the lay list has no equivalent for.",
            "That third change is the substantial one. AN 4.53 assessed a spouse by what they did; "
            "this assesses them by what they do <em>and</em> by whether they are covetous, malicious, "
            "and of wrong view. The standard has moved inward.",
            "The dropping of intoxicants is also worth a note. It is not that drink has become "
            "permissible; the tenfold list is simply a different and older scheme, organized by body, "
            "speech, and mind rather than by the training rules a lay follower undertakes."]),
        ("Why give a discourse about marriage to mendicants", [
            "The obvious question, and there are two reasonable answers.",
            "The practical one is that mendicants advise lay people constantly, and a monk who is "
            "going to be asked about a household needs the teaching in a form he can use. The "
            "Aṅguttara contains a good deal of lay-facing material addressed to monastics for exactly "
            "this reason.",
            "The other is that the grid is not really about marriage. It is about what happens when "
            "two people of unlike ethical condition share a life, and monastic communities are also "
            "shared lives. Nothing in the tenfold assessment requires the two people to be married, "
            "and a reader in any close and ongoing arrangement will recognize the four cells."]),
        ("What is abbreviated", [
            "The verses are gone. The Pāli ends the prose with <em>&hellip;</em> and leaves the six "
            "verses of AN 4.53 to be supplied by the reciter, which is why this discourse is shorter "
            "than its predecessor despite having a longer ethical list.",
            "This is the same convention as AN 4.40 and AN 4.46, and by this point in the chapter a "
            "reader should recognize it on sight: where two adjacent discourses share material, the "
            "second one keeps only what is new."]),
        ("Reading the pair", [
            "AN 4.53 and 4.54 are best read in immediate succession, and the useful exercise is to "
            "hold the two standards side by side and ask which one is being applied when people "
            "assess a relationship in practice.",
            "The lay version is externally checkable: one can see whether someone kills, steals, "
            "lies, or drinks. The monastic version includes covetousness, malice, and wrong view, "
            "none of which is visible from outside and all of which the person themselves may not "
            "have looked at.",
            "That difference is not incidental to who each version is addressed to. A standard for "
            "assessing a household is necessarily one that can be applied by the people in it. A "
            "standard given to mendicants can afford to include what only self-examination reaches."]),
        ("The grid&rsquo;s durability", [
            "For all the harshness of its vocabulary, the four-cell structure is a genuinely useful "
            "instrument and it has outlived its setting. It refuses two comfortable simplifications: "
            "that a relationship has one moral character shared by both parties, and that the "
            "well-behaved partner in a bad match is thereby responsible for it.",
            "The two mixed cells are the point. The discourse says plainly that a good person can be "
            "living with a bad one, names the situation, and does not tell the good one that they "
            "must have failed somewhere. In a body of literature much concerned with how conduct "
            "produces consequences, that restraint is worth noticing."]),
    ],
    terms=[
        ("kammapatha",
         "&ldquo;course of action&rdquo; &mdash; the tenfold scheme of three bodily, four verbal, and "
         "three mental acts, organized by body, speech, and mind."),
        ("abhijjhālu",
         "&ldquo;covetous&rdquo; &mdash; one of the three mental items the tenfold list adds, and one "
         "of the reasons the standard here has moved inward."),
        ("byāpannacitta",
         "&ldquo;malicious&rdquo;, of ill-willed heart &mdash; the second mental item, invisible from "
         "outside."),
        ("micchādiṭṭhi",
         "&ldquo;wrong view&rdquo; &mdash; the third; its inclusion makes the assessment one only "
         "self-examination fully reaches."),
        ("saṁvāsa",
         "&ldquo;living together&rdquo; &mdash; the shared title of both discourses; nothing in the "
         "grid requires the two people to be married."),
    ],
    text_intro=(
        "The discourse in full: the four kinds of living together with the tenfold standard. The "
        "verses of AN 4.53 are abbreviated away in the Pāli. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four ways of living together"),
        ("p", "&sect;1", "an4.54:1.1-1.6"),
        ("h3", "Zombie with zombie"),
        ("p", "&sect;2", "an4.54:2.1-2.4"),
        ("h3", "Zombie with goddess"),
        ("p", "&sect;3", "an4.54:3.1-3.4"),
        ("h3", "God with zombie"),
        ("p", "&sect;4", "an4.54:4.1-4.4"),
        ("h3", "God with goddess"),
        ("p", "&sect;5", "an4.54:5.1-5.5"),
    ],
    quiz=[
        {"q": "What is the one substantive change from AN 4.53?",
         "opts": [
             "The four cells are renamed",
             "The five precepts are replaced by the ten courses of action",
             "The verses are longer",
             "Only wives are assessed"],
         "correct": 1,
         "expl": "And the audience has changed from householders to mendicants."},
        {"q": "How are the ten courses of action organized?",
         "opts": [
             "By severity",
             "Three bodily, four verbal, and three mental",
             "By frequency",
             "By who is harmed"],
         "correct": 1,
         "expl": "Organized by body, speech, and mind."},
        {"q": "What exactly differs between the five and the ten?",
         "opts": [
             "Nothing substantial",
             "The tenfold list drops intoxicants, expands lying into four kinds of wrong speech, and adds three mental items",
             "The ten omit killing",
             "The five include wrong view"],
         "correct": 1,
         "expl": "The third change is the substantial one."},
        {"q": "What does that third change accomplish?",
         "opts": [
             "It shortens the assessment",
             "It moves the standard inward &mdash; a spouse is now assessed by whether they are covetous, malicious, and of wrong view as well as by what they do",
             "It makes the list monastic",
             "It removes the precepts"],
         "correct": 1,
         "expl": "AN 4.53 assessed a spouse by what they did."},
        {"q": "Why is intoxicants dropped?",
         "opts": [
             "Because drink became permissible",
             "Because the tenfold list is a different and older scheme, organized by body, speech, and mind rather than by lay training rules",
             "Because monastics do not drink",
             "Because it is covered by wrong view"],
         "correct": 1,
         "expl": "Not a change in the ethical position."},
        {"q": "What is the practical reason for giving a marriage discourse to mendicants?",
         "opts": [
             "They are considering marriage",
             "They advise lay people constantly and need the teaching in a usable form",
             "The verses require it",
             "It is a mistake in transmission"],
         "correct": 1,
         "expl": "The Aṅguttara contains a good deal of lay-facing material addressed to monastics."},
        {"q": "What is the second reason the guide gives?",
         "opts": [
             "That marriage is a metaphor",
             "That the grid is about what happens when two people of unlike ethical condition share a life &mdash; and monastic communities are also shared lives",
             "That the ten courses apply only to monastics",
             "That the discourse is misplaced"],
         "correct": 1,
         "expl": "Nothing in the assessment requires the two people to be married."},
        {"q": "What is abbreviated away in this discourse?",
         "opts": [
             "The definitions",
             "The six verses of AN 4.53",
             "The setting",
             "The list of four"],
         "correct": 1,
         "expl": "The same convention as AN 4.40 and AN 4.46: the second discourse keeps only what is new."},
        {"q": "How do the two standards differ in what they can detect?",
         "opts": [
             "They detect the same things",
             "The lay version is externally checkable; the monastic version includes covetousness, malice, and wrong view, which are not visible from outside",
             "The monastic one is easier",
             "The lay one is stricter"],
         "correct": 1,
         "expl": "A standard for a household must be applicable by the people in it."},
        {"q": "What two simplifications does the four-cell grid refuse?",
         "opts": [
             "That marriage is permanent, and that it is voluntary",
             "That a relationship has one moral character shared by both parties, and that the well-behaved partner in a bad match is responsible for it",
             "That ethics can be measured, and that it matters",
             "That husbands and wives differ, and that both can be judged"],
         "correct": 1,
         "expl": "The discourse names the mixed cases and does not tell the good partner they must have failed somewhere."},
    ],
    marginalia=[
        ("Ten courses", [
            "three bodily",
            "four verbal",
            "three mental",
        ]),
        ("What is added", [
            "covetousness",
            "malice",
            "wrong view",
            "&mdash; none visible outside",
        ]),
        ("The two mixed cells", [
            "a good person",
            "living with a bad one",
            "&mdash; named, not blamed",
        ]),
        ("Cross-references", [
            "AN 4.53 &middot; the lay version",
            "AN 4.55 &middot; next: Nakula&rsquo;s parents",
            "AN 4.40 &middot; the same abbreviation convention",
        ]),
    ],
    further=[
        '<a href="%s/an4.54/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.53.html">AN 4.53 &middot; Living Together (1st)</a> &mdash; the lay version, '
        "with the verses this one abbreviates away.",
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; next in this chapter, and the '
        "positive case given a name and a couple.",
        '<a href="an-4.52.html">AN 4.52 &middot; Overflowing Merit (2nd)</a> &mdash; on ethical '
        "conduct as a standing source of merit.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.56 — Dutiyasamajīvīsutta
# --------------------------------------------------------------------------- #
page(
    56, "Dutiyasamajīvī", "Equality (2nd)",
    vagga=VAGGA_6,
    prev=("an-4.55.html", "AN 4.55 &middot; Equality"),
    meta_title="AN 4.56 — Equality (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyasamajīvīsutta — the "
        "instruction given to Nakula's parents, restated to the mendicants in a single sentence: "
        "equals in faith, ethics, generosity, and wisdom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_6),
        ("Speakers", SPEAKER),
        ("Form", "One sentence, with everything else abbreviated away"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "As with AN 4.55; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a single sentence, and the "
                       "shortest discourse of the chapter"),
    ],
    why=(
        "One sentence: if wife and husband want to see each other in this life and the next, they "
        "should be equals in faith, ethics, generosity, and wisdom. It is the core of AN 4.55 with "
        "the couple, the setting, and the verses stripped away &mdash; and stripped of them, it "
        "reads as what it is, which is a general instruction rather than personal advice."),
    guide=[
        ("The teaching in one sentence", [
            "A couple who want to remain together across lives should match in four things: faith, "
            "ethics, generosity, and wisdom."]),
        ("What AN 4.55 supplies", [
            "The preceding discourse, already published on this site, gives the occasion. The Buddha "
            "goes for alms to the house of Nakula&rsquo;s father in the land of the Bhaggas, and the "
            "householder and his wife each say the same thing: since they were married young, "
            "neither can recall betraying the other even in thought, and they want to see each other "
            "in this life and the next.",
            "The answer given there is the sentence that constitutes this discourse. Everything else "
            "in AN 4.56 &mdash; the couple, the request, the verses about speaking pleasantly and "
            "living at ease &mdash; is abbreviated away.",
            "So this page is not a substitute for AN 4.55 and does not try to be. What it can do is "
            "look at the instruction on its own, which the abbreviation makes possible."]),
        ("Four things to match", [
            "<em>Saddhā, sīla, cāga, paññā</em> &mdash; faith, ethics, generosity, wisdom. The set "
            "appears throughout the collection as a description of a well-formed lay life, and it is "
            "worth knowing independently of this context.",
            "Faith is orientation; ethics is conduct; generosity is what one does with what one has; "
            "wisdom is understanding. Between them they cover what a person believes, how they "
            "behave, how they hold their property, and what they see &mdash; which is close to an "
            "exhaustive description of the things two people sharing a household could differ about "
            "in ways that matter.",
            "Note that affection is not on the list, and neither is compatibility of temperament. "
            "Nakula&rsquo;s parents already had those; what they were told to attend to was "
            "something else."]),
        ("&lsquo;Equals&rsquo;", [
            "<em>Samasaddhā samasīlā samacāgā samapaññā</em> &mdash; of equal faith, equal ethics, "
            "equal generosity, equal wisdom. The word is <em>sama</em>, same or equal, prefixed to "
            "each item.",
            "The claim is about matching, not about level. The discourse does not say the couple must "
            "be highly developed in these four; it says they must be alike in them. That is a "
            "different and more interesting instruction, and it is consistent with the four-cell grid "
            "of AN 4.53 and 4.54, where the two problem cases were precisely the mismatched ones.",
            "Read together the three discourses make a coherent claim about shared life: what causes "
            "trouble is difference in these four, and what makes a marriage work as a spiritual "
            "arrangement is not that both partners are good but that they are the same."]),
        ("&lsquo;See each other in the next life&rsquo;", [
            "The stated goal is <em>aññamaññaṁ passitukāmā</em>, wanting to see one another &mdash; "
            "in this life and in the life to come. The mechanism assumed is that beings of similar "
            "faith, ethics, generosity, and wisdom are reborn in similar destinations.",
            "It is worth being clear that this is what the discourse says and that it is a claim "
            "about rebirth, not a metaphor. A reader who does not hold that framework can still take "
            "the instruction &mdash; matching in these four is good advice for a shared life on any "
            "view &mdash; but should not be told that the discourse means something other than what "
            "it says.",
            "It is also, in its way, a tender text. The request that prompted it was not for "
            "liberation or for merit but to stay together, and the answer takes the request seriously "
            "and answers it in its own terms."]),
        ("Why the abbreviated version was kept", [
            "The same three reasons that applied to AN 4.46 apply here: provenance is already "
            "established by AN 4.55, so what this adds is audience and a slot in the chapter of ten.",
            "There is one further point specific to this pair. AN 4.55 is a discourse to two named "
            "people about their own marriage. AN 4.56 is the same instruction addressed to mendicants "
            "with no couple in view, which converts it from advice into a general principle. The "
            "collection has kept both the case and the rule, and it is the rule that this discourse "
            "is."]),
    ],
    terms=[
        ("samajīvī",
         "&ldquo;living in equality, matched&rdquo; &mdash; the title of both discourses; the "
         "prefix <em>sama</em> means same or equal."),
        ("saddhā, sīla, cāga, paññā",
         "faith, ethics, generosity, wisdom &mdash; the four to be matched, and a standing "
         "description of a well-formed lay life."),
        ("cāga",
         "&ldquo;generosity&rdquo; &mdash; literally letting go or relinquishment; what one does with "
         "what one has."),
        ("aññamaññaṁ passitukāma",
         "&ldquo;wanting to see one another&rdquo; &mdash; the stated goal, in this life and the "
         "next; a claim about rebirth rather than a metaphor."),
        ("peyyāla",
         "the abbreviation convention that reduces this discourse to a single sentence, leaving "
         "AN 4.55 to supply the rest."),
    ],
    text_intro=(
        "The discourse as the Pāli preserves it: one sentence, with the occasion and verses of "
        "AN 4.55 abbreviated away. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Equals in four things"),
        ("p", "&sect;1", "an4.56:1.1"),
    ],
    quiz=[
        {"q": "What four things should a couple be equal in?",
         "opts": [
             "Age, wealth, birth, and beauty",
             "Faith, ethics, generosity, and wisdom",
             "Learning, energy, patience, and kindness",
             "The four requisites"],
         "correct": 1,
         "expl": "<em>Saddhā, sīla, cāga, paññā</em>."},
        {"q": "What does AN 4.55 supply that this discourse does not?",
         "opts": [
             "The four items",
             "The occasion &mdash; Nakula&rsquo;s parents, their request, and the verses",
             "The instruction",
             "The setting only"],
         "correct": 1,
         "expl": "Everything but the single sentence is abbreviated away."},
        {"q": "What did Nakula&rsquo;s parents ask for?",
         "opts": [
             "Liberation",
             "To see each other in this life and the next",
             "Merit for their household",
             "A teaching on generosity"],
         "correct": 1,
         "expl": "Neither could recall betraying the other even in thought."},
        {"q": "What do the four items cover between them?",
         "opts": [
             "Only religious matters",
             "What a person believes, how they behave, how they hold their property, and what they see",
             "Only conduct",
             "Only wealth and status"],
         "correct": 1,
         "expl": "Close to an exhaustive description of what two people sharing a household could differ about."},
        {"q": "What is notably absent from the list?",
         "opts": [
             "Ethics",
             "Affection and compatibility of temperament",
             "Wisdom",
             "Generosity"],
         "correct": 1,
         "expl": "Nakula&rsquo;s parents already had those."},
        {"q": "What does <em>sama</em> claim?",
         "opts": [
             "A high level in each",
             "Matching &mdash; that the two are alike in them, not that they are highly developed",
             "Superiority of one partner",
             "Growth over time"],
         "correct": 1,
         "expl": "A different and more interesting instruction."},
        {"q": "How does that fit AN 4.53 and 4.54?",
         "opts": [
             "It contradicts them",
             "Consistently &mdash; the two problem cells there were precisely the mismatched ones",
             "It replaces them",
             "It addresses a different question"],
         "correct": 1,
         "expl": "What causes trouble is difference in these four."},
        {"q": "What mechanism does the stated goal assume?",
         "opts": [
             "That love persists",
             "That beings of similar faith, ethics, generosity, and wisdom are reborn in similar destinations",
             "That merit is shared",
             "That memory carries over"],
         "correct": 1,
         "expl": "A claim about rebirth, not a metaphor."},
        {"q": "How does the guide treat a reader who does not hold that framework?",
         "opts": [
             "Tells them the discourse means something else",
             "Says they can still take the instruction, while not being told the discourse means other than what it says",
             "Excludes them",
             "Reinterprets the goal"],
         "correct": 1,
         "expl": "Matching in these four is good advice for a shared life on any view."},
        {"q": "What does this discourse add that AN 4.55 does not?",
         "opts": [
             "New content",
             "It converts a discourse to two named people about their own marriage into a general principle addressed to mendicants",
             "The verses",
             "The four items"],
         "correct": 1,
         "expl": "The collection has kept both the case and the rule."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">saddhā</span>faith",
            "<span class=\"pali\">sīla</span>ethics",
            "<span class=\"pali\">cāga</span>generosity",
            "<span class=\"pali\">paññā</span>wisdom",
        ]),
        ("The claim", [
            "<span class=\"pali\">sama</span>equal",
            "not high",
            "&mdash; alike",
        ]),
        ("Not on the list", [
            "affection",
            "temperament",
            "&mdash; they already had those",
        ]),
        ("Cross-references", [
            "AN 4.55 &middot; the case this states as a rule",
            "AN 4.53 &middot; the mismatched cells",
            "AN 4.57 &middot; next: Suppavāsā",
        ]),
    ],
    further=[
        '<a href="%s/an4.56/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.55.html">AN 4.55 &middot; Equality</a> &mdash; the discourse this one '
        "abbreviates, and the one to read first.",
        '<a href="an-4.53.html">AN 4.53 &middot; Living Together (1st)</a> &mdash; the four cells, of '
        "which two are mismatches.",
        '<a href="an-4.57.html">AN 4.57 &middot; Suppavāsā</a> &mdash; next in this series.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.57 — Suppavāsāsutta
# --------------------------------------------------------------------------- #
page(
    57, "Suppavāsā", "Suppavāsā",
    vagga=VAGGA_6,
    meta_title="AN 4.57 — Suppavāsā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Suppavāsāsutta — a woman "
        "serves the Buddha a meal and is told that a giver of food gives four things: long life, "
        "beauty, happiness, and strength. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The land of the Koliyans, at a town named Pajjanika, in Suppavāsā&rsquo;s own "
                    "home"),
        ("Speakers", "The Buddha, addressing Suppavāsā the Koliyan"),
        ("Form", "A meal, four things given, and two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The four gifts of a food-giver appear across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short and warm, with a neat "
                       "reciprocal structure"),
    ],
    why=(
        "Suppavāsā serves the Buddha a meal with her own hands, and he tells her what she has just "
        "given: not food but long life, beauty, happiness, and strength &mdash; and that she will "
        "have the same four. It is one of the collection&rsquo;s clearest statements of how giving "
        "is supposed to work, and it is given to a laywoman in her own house immediately after she "
        "has done it."),
    guide=[
        ("The teaching in one sentence", [
            "A person who gives food gives four things, and receives the same four."]),
        ("Who Suppavāsā was", [
            "A Koliyan laywoman, and one of the named lay figures of the canon: she is declared "
            "foremost among laywomen who give what is excellent, and she appears in the Udāna in "
            "connection with a long and difficult pregnancy.",
            "The Koliyans were the clan related by marriage to the Sakyans, the Buddha&rsquo;s own "
            "people. The discourse is set in their territory at a town called Pajjanika, and the "
            "Buddha comes to her house on almsround.",
            "The narrative detail is worth keeping: she serves and satisfies him <em>with her own "
            "hands</em>, and only after he has eaten and washed does she sit down to one side and "
            "receive the teaching. The order is not incidental. The teaching is about what she has "
            "just done, given while the doing is still in the room."]),
        ("The four things", [
            "<em>Āyu, vaṇṇa, sukha, bala</em> &mdash; long life, beauty, happiness, strength. These "
            "four are a standing set in the collection for what a lay person hopes for, and they are "
            "worth taking at face value: they are physical and worldly and the discourse does not "
            "apologize for them.",
            "The logic is that food produces exactly these in whoever eats it. A person who is fed "
            "lives longer, looks better, feels better, and is stronger than one who is not, and the "
            "discourse simply names those four effects and says the donor gave them.",
            "That is not a mystical claim. It is a redescription of what a meal does, and its whole "
            "force is in the redescription. What was handed over was rice; what was given was four "
            "conditions of a body."]),
        ("The reciprocity", [
            "Each of the four is then returned: <em>giving long life, she has long life as a god or "
            "human</em>, and so for the other three.",
            "The symmetry is exact and mechanical, and it is worth noticing that nothing else is "
            "promised. Not awakening, not merit in the abstract, not a favorable rebirth in general "
            "&mdash; specifically these four, returned in kind.",
            "The phrase <em>as a god or human</em> covers both possible destinations without "
            "choosing, which is characteristic of how the collection handles lay results. The "
            "consequence is stated for whichever life follows."]),
        ("The verses on what makes a gift fruitful", [
            "The first verse adds three conditions the prose did not state: the food is "
            "<em>well-prepared, pure, fine, and full of flavor</em>; the recipients are "
            "<em>sincere, of good conduct, and big-hearted</em>; and the offering therefore "
            "<em>joins merit to merit</em>.",
            "That first condition is the interesting one. The quality of the food matters, and the "
            "verse says so plainly. This is not a tradition in which the gesture is all that counts; "
            "care taken over what is given is part of the giving.",
            "The second verse turns to memory: <em>those who recall such sacrifices live in the world "
            "full of inspiration</em>. Recollection of one&rsquo;s own generosity is a recognized "
            "practice in this literature &mdash; <em>cāgānussati</em>, one of the standard "
            "recollections &mdash; and it is named here as producing gladness and driving out "
            "stinginess <em>root and all</em>."]),
        ("AN 4.57, 4.58, and 4.59", [
            "The next two discourses give the identical teaching to Anāthapiṇḍika and then to the "
            "mendicants in general, with the prose progressively abbreviated: AN 4.58 keeps the four "
            "and its own verses, and AN 4.59 is reduced to a single sentence.",
            "Three consecutive discourses on the same four things, to a laywoman, a layman, and the "
            "monastic community. The sequence is a small demonstration of how the collection "
            "generalizes: from a named person in her own house, to another named person, to the rule "
            "stated flatly with nobody in view."]),
    ],
    terms=[
        ("Suppavāsā",
         "a Koliyan laywoman, declared foremost among laywomen who give what is excellent, and known "
         "also from the Udāna."),
        ("āyu, vaṇṇa, sukha, bala",
         "long life, beauty, happiness, strength &mdash; a standing set for what a lay person hopes "
         "for, and what food actually produces."),
        ("Koliya",
         "the clan related by marriage to the Sakyans; their territory is where this discourse is "
         "set."),
        ("cāgānussati",
         "&ldquo;recollection of generosity&rdquo; &mdash; a standard recollection practice, named in "
         "the second verse as producing inspiration."),
        ("maccheramala",
         "&ldquo;the stain of stinginess&rdquo; &mdash; what the verse says such recollection drives "
         "out root and all."),
    ],
    text_intro=(
        "The discourse in full: the meal, the four things, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Suppavāsā&rsquo;s house"),
        ("p", "&sect;1", "an4.57:1.1-1.5"),
        ("h3", "Four things given"),
        ("p", "&sect;2", "an4.57:2.1-2.8"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.57:3.1-3.6"),
        ("p", "&sect;4", "an4.57:4.1-4.4"),
    ],
    quiz=[
        {"q": "What four things does a giver of food give?",
         "opts": [
             "Faith, ethics, generosity, and wisdom",
             "Long life, beauty, happiness, and strength",
             "Merit, honor, fame, and heaven",
             "Robes, almsfood, lodgings, and medicines"],
         "correct": 1,
         "expl": "<em>Āyu, vaṇṇa, sukha, bala</em>."},
        {"q": "Who was Suppavāsā?",
         "opts": [
             "A nun",
             "A Koliyan laywoman, declared foremost among laywomen who give what is excellent",
             "A queen",
             "A merchant&rsquo;s daughter of Sāvatthī"],
         "correct": 1,
         "expl": "She appears also in the Udāna."},
        {"q": "When is the teaching given?",
         "opts": [
             "Before the meal",
             "After he has eaten and washed, with the doing still in the room",
             "The following day",
             "In the assembly hall"],
         "correct": 1,
         "expl": "The teaching is about what she has just done."},
        {"q": "Why does the guide say the claim is not mystical?",
         "opts": [
             "Because it concerns gods",
             "Because a person who is fed lives longer, looks better, feels better, and is stronger &mdash; the discourse names what a meal does",
             "Because it is about merit",
             "Because it is a verse"],
         "correct": 1,
         "expl": "What was handed over was rice; what was given was four conditions of a body."},
        {"q": "What is returned to the giver?",
         "opts": [
             "Merit in general",
             "The same four, in kind &mdash; and nothing else is promised",
             "Awakening",
             "A favorable rebirth in general"],
         "correct": 1,
         "expl": "The symmetry is exact and mechanical."},
        {"q": "What does &lsquo;as a god or human&rsquo; do?",
         "opts": [
             "Restricts the result to heaven",
             "Covers both possible destinations without choosing, stating the consequence for whichever life follows",
             "Excludes human rebirth",
             "Names a specific realm"],
         "correct": 1,
         "expl": "Characteristic of how the collection handles lay results."},
        {"q": "What condition on the food does the first verse add?",
         "opts": [
             "That it be plentiful",
             "That it be well-prepared, pure, fine, and full of flavor",
             "That it be given early",
             "That it be homemade"],
         "correct": 1,
         "expl": "Care taken over what is given is part of the giving."},
        {"q": "What does the guide draw from that?",
         "opts": [
             "That poor gifts are worthless",
             "That this is not a tradition in which the gesture is all that counts",
             "That food must be expensive",
             "That donors should be wealthy"],
         "correct": 1,
         "expl": "The quality of the food matters, and the verse says so plainly."},
        {"q": "What practice does the second verse name?",
         "opts": [
             "Recollection of the Buddha",
             "Recollection of one&rsquo;s own generosity &mdash; <em>cāgānussati</em>",
             "Mindfulness of breathing",
             "Recollection of death"],
         "correct": 1,
         "expl": "Named as producing inspiration and driving out stinginess root and all."},
        {"q": "How do AN 4.57, 4.58, and 4.59 relate?",
         "opts": [
             "They give different teachings",
             "The same four to a laywoman, a layman, and the mendicants, with the prose progressively abbreviated",
             "They contradict each other",
             "Only the first is complete"],
         "correct": 1,
         "expl": "A small demonstration of how the collection generalizes."},
    ],
    marginalia=[
        ("The four", [
            "<span class=\"pali\">āyu</span>long life",
            "<span class=\"pali\">vaṇṇa</span>beauty",
            "<span class=\"pali\">sukha</span>happiness",
            "<span class=\"pali\">bala</span>strength",
        ]),
        ("The redescription", [
            "handed over: rice",
            "given: four conditions",
            "&mdash; of a body",
        ]),
        ("The verse condition", [
            "well-prepared",
            "pure, fine",
            "full of flavor",
        ]),
        ("Cross-references", [
            "AN 4.58 &middot; next: the same, to Anāthapiṇḍika",
            "AN 4.51 &middot; merit and the recipient&rsquo;s state",
            "AN 4.60 &middot; what lay practice is",
        ]),
    ],
    further=[
        '<a href="%s/an4.57/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.58.html">AN 4.58 &middot; Sudatta</a> &mdash; next in this series, the same '
        "teaching to Anāthapiṇḍika.",
        '<a href="an-4.51.html">AN 4.51 &middot; Overflowing Merit</a> &mdash; on what makes a '
        "donor&rsquo;s merit limitless.",
        '<a href="an-4.60.html">AN 4.60 &middot; Lay Practice</a> &mdash; the four things that '
        "constitute practice for a householder.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.58 — Sudattasutta
# --------------------------------------------------------------------------- #
page(
    58, "Sudatta", "Sudatta",
    vagga=VAGGA_6,
    meta_title="AN 4.58 — Sudatta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sudattasutta — the same "
        "four gifts of a food-giver, told to Anāthapiṇḍika, whose given name the discourse uses. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; Anāthapiṇḍika comes to the Buddha and the teaching begins at once"),
        ("Speakers", "The Buddha, addressing the householder Anāthapiṇḍika"),
        ("Form", "AN 4.57&rsquo;s teaching abbreviated, with two different verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 4.57; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a variant whose interest is its "
                       "title and its verses"),
    ],
    why=(
        "The same four gifts, this time to Anāthapiṇḍika &mdash; and the discourse is titled with "
        "his given name, Sudatta, which the canon almost never uses. The verses are new, and they "
        "add two conditions the previous discourse did not: giving <em>carefully</em>, and giving "
        "<em>at the right time</em>."),
    guide=[
        ("The teaching in one sentence", [
            "A giver of food gives long life, beauty, happiness, and strength &mdash; and receives "
            "them wherever they are reborn."]),
        ("Sudatta and Anāthapiṇḍika", [
            "The householder&rsquo;s name was Sudatta. <em>Anāthapiṇḍika</em> is an epithet meaning "
            "&lsquo;one who gives alms to the helpless&rsquo; &mdash; literally food for those "
            "without protection &mdash; and it is what he is called everywhere in the canon.",
            "This discourse is the exception: the title uses the given name, though the text itself "
            "still says Anāthapiṇḍika. That is a small piece of evidence about how these titles were "
            "assigned, apparently by someone with access to information the discourse text does not "
            "carry.",
            "He is the canon&rsquo;s principal lay donor, the purchaser of Jeta&rsquo;s Grove, and "
            "the person named in the setting formula of an enormous number of discourses. That a "
            "teaching about giving food is addressed to him is unsurprising; what is notable is how "
            "ordinary the teaching is. He receives the same four items as everyone else."]),
        ("The two new conditions", [
            "The verses add <em>kālena</em>, at the right time, and a word Sujato renders "
            "<em>carefully</em>. Neither appeared in AN 4.57.",
            "Timing matters concretely in this context: monastics may not eat after midday, so a "
            "meal offered late is not a gift at all but an embarrassment. The condition is practical "
            "before it is spiritual, and it generalizes &mdash; a gift that arrives when it cannot be "
            "used has not been given.",
            "&lsquo;Carefully&rsquo; picks up what AN 4.57&rsquo;s verse said about the food being "
            "well-prepared, pure, fine, and flavorful. Between the two discourses the conditions on a "
            "good gift are: prepared with care, of good quality, given at a usable time, and given to "
            "the disciplined."]),
        ("&lsquo;Eating only what others give&rsquo;", [
            "The recipients are described as <em>disciplined, eating only what others give</em>. That "
            "phrase names the structural fact that makes the whole exchange work.",
            "A mendicant on this model does not grow, buy, or store food. Whatever they eat came from "
            "someone, on the day it was eaten. The donor is therefore not supplementing a "
            "monastic&rsquo;s resources; they are supplying them entirely, and the four things the "
            "verse names really do depend on the giving.",
            "It is worth stating for lay readers that this is what makes the reciprocal claim more "
            "than sentiment. The dependence is real and total in one direction, and the discourse "
            "describes the return flowing in the other."]),
        ("What is promised", [
            "<em>Has long life and fame wherever they&rsquo;re reborn</em> &mdash; <em>yattha yattha "
            "upapajjati</em>, in whatever place they are reborn.",
            "That is slightly wider than AN 4.57&rsquo;s &lsquo;as a god or human&rsquo;. The formula "
            "does not specify a destination at all; it says the four travel with the giver wherever "
            "they go.",
            "It also adds fame (<em>yasa</em>) to the list, which the prose did not include. This "
            "kind of small drift between prose and verse recurs throughout the collection and is "
            "worth registering rather than reconciling."]),
        ("The sequence and its point", [
            "AN 4.57 gave this teaching to a laywoman in her own house, immediately after a meal. "
            "AN 4.58 gives it to a layman who has come to the Buddha, with the narrative reduced to "
            "one line. AN 4.59, next, gives it to the mendicants with no person in view at all and "
            "no verses.",
            "Read as a sequence the three show a teaching being lifted out of its occasion. The first "
            "is an event; the second is an instruction; the third is a rule. Nothing in the content "
            "changes, and the collection preserves all three stages.",
            "For a reader that is useful in a practical way. If the teaching is wanted as a story, "
            "read AN 4.57. If it is wanted as a statement, read AN 4.59. AN 4.58 sits between them "
            "and carries the conditions."]),
    ],
    terms=[
        ("Sudatta",
         "Anāthapiṇḍika&rsquo;s given name &mdash; used in this discourse&rsquo;s title and almost "
         "nowhere else in the canon."),
        ("Anāthapiṇḍika",
         "&ldquo;one who gives alms to the helpless&rdquo; &mdash; an epithet, and the name by which "
         "the canon&rsquo;s principal lay donor is otherwise always known."),
        ("kālena",
         "&ldquo;at the right time&rdquo; &mdash; a practical condition before a spiritual one: "
         "monastics may not eat after midday."),
        ("paradattūpajīvī",
         "&ldquo;eating only what others give&rdquo; &mdash; the structural fact that makes the "
         "exchange more than sentiment."),
        ("yasa",
         "&ldquo;fame&rdquo; &mdash; added by the verse to the four of the prose; a small drift worth "
         "registering rather than reconciling."),
    ],
    text_intro=(
        "The discourse in full: the approach, the four things, and the verses. The ellipses are the "
        "Pāli&rsquo;s own abbreviation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Anāthapiṇḍika comes"),
        ("p", "&sect;1", "an4.58:1.1"),
        ("h3", "Four things given"),
        ("p", "&sect;2", "an4.58:2.1-2.6"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.58:3.1-3.4"),
        ("p", "&sect;4", "an4.58:4.1-4.4"),
    ],
    quiz=[
        {"q": "Whose given name is Sudatta?",
         "opts": [
             "A Koliyan householder",
             "Anāthapiṇḍika&rsquo;s",
             "The Buddha&rsquo;s cousin",
             "A wanderer"],
         "correct": 1,
         "expl": "Used in this discourse&rsquo;s title and almost nowhere else in the canon."},
        {"q": "What does the epithet <em>Anāthapiṇḍika</em> mean?",
         "opts": [
             "&lsquo;Great giver&rsquo;",
             "&lsquo;One who gives alms to the helpless&rsquo; &mdash; food for those without protection",
             "&lsquo;Owner of the grove&rsquo;",
             "&lsquo;Chief householder&rsquo;"],
         "correct": 1,
         "expl": "The name by which he is otherwise always known."},
        {"q": "What does the guide draw from the title using the given name?",
         "opts": [
             "That the discourse is late",
             "A small piece of evidence about how titles were assigned &mdash; apparently by someone with information the discourse text does not carry",
             "That two people are confused",
             "That the title is wrong"],
         "correct": 1,
         "expl": "The text itself still says Anāthapiṇḍika."},
        {"q": "What two conditions do these verses add?",
         "opts": [
             "Generosity and faith",
             "Giving carefully, and giving at the right time",
             "Giving much, and giving often",
             "Giving in public, and giving anonymously"],
         "correct": 1,
         "expl": "Neither appeared in AN 4.57."},
        {"q": "Why does timing matter concretely?",
         "opts": [
             "Because donors are busy",
             "Because monastics may not eat after midday, so a meal offered late is not a gift but an embarrassment",
             "Because morning food is fresher",
             "Because of the season"],
         "correct": 1,
         "expl": "Practical before it is spiritual, and it generalizes."},
        {"q": "What do the two discourses together give as conditions on a good gift?",
         "opts": [
             "Size, frequency, publicity, and cost",
             "Prepared with care, of good quality, given at a usable time, and given to the disciplined",
             "Faith, ethics, generosity, and wisdom",
             "Long life, beauty, happiness, and strength"],
         "correct": 1,
         "expl": "Between AN 4.57&rsquo;s verse and this one."},
        {"q": "What does &lsquo;eating only what others give&rsquo; name?",
         "opts": [
             "A vow of poverty",
             "The structural fact that a mendicant does not grow, buy, or store food &mdash; whatever they eat came from someone, on the day it was eaten",
             "A monastic rule about leftovers",
             "A description of poverty"],
         "correct": 1,
         "expl": "The donor is not supplementing resources but supplying them entirely."},
        {"q": "Why does that make the reciprocal claim more than sentiment?",
         "opts": [
             "Because it is in verse",
             "Because the dependence is real and total in one direction, and the discourse describes the return flowing in the other",
             "Because the Buddha said it",
             "Because it is repeated"],
         "correct": 1,
         "expl": "Worth stating for lay readers."},
        {"q": "How does this discourse&rsquo;s promise differ from AN 4.57&rsquo;s?",
         "opts": [
             "It is narrower",
             "It says the four travel with the giver <em>wherever they are reborn</em>, without specifying a destination &mdash; and it adds fame",
             "It promises awakening",
             "It promises nothing"],
         "correct": 1,
         "expl": "AN 4.57 said &lsquo;as a god or human&rsquo;."},
        {"q": "What does the three-discourse sequence show?",
         "opts": [
             "Three different teachings",
             "A teaching being lifted out of its occasion &mdash; an event, then an instruction, then a rule",
             "A growing audience",
             "A change of doctrine"],
         "correct": 1,
         "expl": "Nothing in the content changes, and the collection preserves all three stages."},
    ],
    marginalia=[
        ("Two names", [
            "<span class=\"pali\">Sudatta</span>the given name",
            "<span class=\"pali\">Anāthapiṇḍika</span>the epithet",
            "&mdash; only the title uses the first",
        ]),
        ("New conditions", [
            "carefully",
            "at the right time",
            "&mdash; or it is not a gift",
        ]),
        ("The structural fact", [
            "does not grow food",
            "does not buy or store it",
            "&mdash; it came from someone today",
        ]),
        ("Cross-references", [
            "AN 4.57 &middot; the same, as an event",
            "AN 4.59 &middot; next: the same, as a rule",
            "AN 4.51 &middot; the four requisites and merit",
        ]),
    ],
    further=[
        '<a href="%s/an4.58/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.57.html">AN 4.57 &middot; Suppavāsā</a> &mdash; the same teaching as an event, '
        "in a laywoman&rsquo;s house.",
        '<a href="an-4.59.html">AN 4.59 &middot; Food</a> &mdash; next in this series, the same '
        "teaching reduced to a rule.",
        '<a href="an-4.60.html">AN 4.60 &middot; Lay Practice</a> &mdash; the other discourse of this '
        "chapter addressed to Anāthapiṇḍika.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.59 — Bhojanasutta
# --------------------------------------------------------------------------- #
page(
    59, "Bhojana", "Food",
    vagga=VAGGA_6,
    meta_title="AN 4.59 — Food | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bhojanasutta — the four "
        "gifts of a food-giver stated as a rule to the mendicants, in a single sentence. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_6),
        ("Speakers", SPEAKER),
        ("Form", "One sentence, with the definitions and verses abbreviated away"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "As with AN 4.57 and 4.58; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the bare rule, and the end of a "
                       "three-discourse sequence"),
    ],
    why=(
        "The third and last statement of the four gifts, and the shortest: when a donor gives food, "
        "they give the recipients long life, beauty, happiness, and strength. No person, no "
        "occasion, no verses. This is the teaching in the form the collection will store it in, and "
        "reading it after AN 4.57 and 4.58 is the point of having all three."),
    guide=[
        ("The teaching in one sentence", [
            "The rule, without occasion or elaboration: a giver of food gives four things."]),
        ("The word that changed", [
            "AN 4.57 and 4.58 both said <em>ariyasāvako</em>, a noble disciple, gives food. This "
            "discourse says <em>dāyako</em>, a donor.",
            "That is the only substantive difference and it is worth noticing. The two earlier "
            "discourses were addressed to people who were themselves noble disciples and described "
            "what such a person does. Stated as a general rule, the qualification drops away and the "
            "claim widens: <em>anyone</em> who gives food gives these four.",
            "Whether that widening is deliberate or an artifact of abbreviation cannot be settled "
            "from the text. What can be said is that the mechanism supports the wider version. The "
            "four things are what food does to a body, and food does that regardless of the "
            "giver&rsquo;s attainments."]),
        ("The three stages", [
            "The sequence is now complete. AN 4.57: Suppavāsā serves a meal in her own house and is "
            "told what she has given, with a narrative setting and two verses. AN 4.58: "
            "Anāthapiṇḍika comes and is told the same, with the narrative reduced to one line and "
            "different verses adding conditions. AN 4.59: the bare statement, addressed to nobody in "
            "particular.",
            "Twenty-six segments, then eighteen, then three. The collection has preserved a teaching "
            "at three degrees of abstraction and put them in descending order.",
            "That ordering is itself informative. The Aṅguttara does not begin with the principle and "
            "illustrate it; it begins with the occasion and works outward. A reader who wants to know "
            "what a teaching is <em>for</em> is generally better served by the first version in a "
            "sequence than the last."]),
        ("Why the bare form is useful", [
            "It would be easy to treat this discourse as the residue of the other two. It has a use "
            "of its own.",
            "A statement with no person in it can be applied to any person. The moment Suppavāsā is "
            "in the frame, a reader can wonder whether the teaching depends on her being who she was "
            "&mdash; foremost among laywomen who give what is excellent, serving the Buddha himself, "
            "with her own hands, in her own house. Every one of those particulars is a reason to "
            "think the case is special.",
            "AN 4.59 removes all of them. What is left is the mechanism, and the mechanism is what "
            "transfers."]),
        ("What is abbreviated", [
            "Everything after the list of four. In the fuller versions this would be the reciprocal "
            "statement &mdash; giving long life, one has long life as a god or human, and so for the "
            "other three &mdash; and then the verses.",
            "A reciter encountering this discourse would supply that expansion from AN 4.57. The "
            "written text preserves the head of the passage and marks the rest as understood, which "
            "is the same convention as AN 4.46, AN 4.54, and AN 4.56 in this chapter alone.",
            "By this point in the Fours the convention is running at a high density, and it is worth "
            "recognizing what that indicates: the chapter was compiled by people who expected its "
            "discourses to be known as a set rather than read individually."]),
        ("Closing the food sequence", [
            "One discourse remains in the chapter. AN 4.60 returns to Anāthapiṇḍika and gives the "
            "four requisites &mdash; robes, almsfood, lodgings, medicines &mdash; as the content of "
            "lay practice, which brings the chapter back to where AN 4.51 began.",
            "The Puññābhisandavagga is the most coherent chapter of the Fours so far. It opens with "
            "the four requisites as occasions of merit, runs through the four factors of "
            "stream-entry, the four kinds of marriage, the four things a couple should match in, and "
            "the four gifts in food, and closes with the four requisites again as the definition of "
            "lay practice. It is a chapter for householders, arranged as one."]),
    ],
    terms=[
        ("dāyaka",
         "&ldquo;donor&rdquo; &mdash; the word this discourse uses where AN 4.57 and 4.58 said "
         "&lsquo;noble disciple&rsquo;, widening the claim."),
        ("bhojana",
         "&ldquo;food&rdquo; &mdash; the title, and the whole of the subject; the discourse names no "
         "person and no occasion."),
        ("āyu, vaṇṇa, sukha, bala",
         "long life, beauty, happiness, strength &mdash; what food produces in whoever eats it, and "
         "therefore what the donor gives."),
        ("ariyasāvaka",
         "&ldquo;noble disciple&rdquo; &mdash; the qualification present in the two preceding "
         "discourses and absent here."),
        ("peyyāla",
         "the abbreviation convention &mdash; running at high density in this chapter, which "
         "indicates a compilation meant to be known as a set."),
    ],
    text_intro=(
        "The discourse as the Pāli preserves it: one sentence, with the reciprocal statement and the "
        "verses abbreviated away. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A donor gives four things"),
        ("p", "&sect;1", "an4.59:1.1-1.3"),
    ],
    quiz=[
        {"q": "What does this discourse state?",
         "opts": [
             "A new list of four",
             "That when a donor gives food, they give the recipients long life, beauty, happiness, and strength",
             "The four requisites",
             "The four factors of stream-entry"],
         "correct": 1,
         "expl": "The rule, without occasion or elaboration."},
        {"q": "What single word differs from AN 4.57 and 4.58?",
         "opts": [
             "&lsquo;Food&rsquo; for &lsquo;almsfood&rsquo;",
             "&lsquo;Donor&rsquo; for &lsquo;noble disciple&rsquo;",
             "&lsquo;Gives&rsquo; for &lsquo;serves&rsquo;",
             "&lsquo;Four&rsquo; for &lsquo;these four&rsquo;"],
         "correct": 1,
         "expl": "The only substantive difference."},
        {"q": "What effect does that have?",
         "opts": [
             "It narrows the claim",
             "It widens it &mdash; anyone who gives food gives these four, not only a noble disciple",
             "It changes the four items",
             "It makes it monastic"],
         "correct": 1,
         "expl": "The qualification drops away with the person."},
        {"q": "How does the guide assess whether the widening is deliberate?",
         "opts": [
             "It says the widening is certainly deliberate",
             "It says it cannot be settled from the text, but that the mechanism supports the wider version &mdash; food does what it does regardless of the giver&rsquo;s attainments",
             "It says it is an error",
             "It does not raise the question"],
         "correct": 1,
         "expl": "The four things are what food does to a body."},
        {"q": "What are the three stages of the sequence?",
         "opts": [
             "Three different teachings",
             "An event with a setting and verses, an instruction with conditions, and a bare statement",
             "Three audiences with three doctrines",
             "Prose, verse, and commentary"],
         "correct": 1,
         "expl": "Twenty-six segments, then eighteen, then three."},
        {"q": "What does the descending order indicate about the collection&rsquo;s method?",
         "opts": [
             "That the later versions are corrupt",
             "That it begins with the occasion and works outward rather than beginning with the principle and illustrating it",
             "That principles come first",
             "That the order is random"],
         "correct": 1,
         "expl": "A reader who wants to know what a teaching is for is better served by the first version in a sequence."},
        {"q": "What use does the bare form have of its own?",
         "opts": [
             "None; it is residue",
             "A statement with no person in it can be applied to any person &mdash; the particulars of Suppavāsā&rsquo;s case are all reasons to think it special",
             "It is easier to memorize",
             "It is more authoritative"],
         "correct": 1,
         "expl": "What is left is the mechanism, and the mechanism is what transfers."},
        {"q": "What is abbreviated away here?",
         "opts": [
             "The four items",
             "The reciprocal statement &mdash; giving long life one has long life, and so on &mdash; and the verses",
             "The setting only",
             "The audience"],
         "correct": 1,
         "expl": "A reciter would supply the expansion from AN 4.57."},
        {"q": "What does the high density of abbreviation in this chapter indicate?",
         "opts": [
             "Damage to the manuscripts",
             "That the chapter was compiled by people who expected its discourses to be known as a set rather than read individually",
             "Haste in composition",
             "A late date"],
         "correct": 1,
         "expl": "AN 4.46, 4.54, 4.56, and 4.59 in this chapter alone."},
        {"q": "How does the guide describe the Puññābhisandavagga as a whole?",
         "opts": [
             "A miscellany",
             "The most coherent chapter of the Fours so far &mdash; a chapter for householders, arranged as one, opening and closing with the four requisites",
             "A monastic chapter",
             "A set of unrelated variants"],
         "correct": 1,
         "expl": "Merit, stream-entry, marriage, matching, food, and lay practice."},
    ],
    marginalia=[
        ("The rule", [
            "a donor gives food",
            "&rarr; four things",
            "&mdash; and no more is said",
        ]),
        ("The widening", [
            "4.57, 4.58 &middot; a noble disciple",
            "4.59 &middot; a donor",
            "&mdash; anyone at all",
        ]),
        ("Three degrees", [
            "26 segments &middot; an event",
            "18 &middot; an instruction",
            "3 &middot; a rule",
        ]),
        ("Cross-references", [
            "AN 4.57 &middot; the event",
            "AN 4.58 &middot; the instruction",
            "AN 4.60 &middot; next: lay practice",
        ]),
    ],
    further=[
        '<a href="%s/an4.59/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.57.html">AN 4.57 &middot; Suppavāsā</a> &mdash; the fullest version, and the '
        "one to read for the occasion.",
        '<a href="an-4.58.html">AN 4.58 &middot; Sudatta</a> &mdash; the middle version, which '
        "carries the conditions.",
        '<a href="an-4.60.html">AN 4.60 &middot; Lay Practice</a> &mdash; next in this series, and '
        "the last discourse of the chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 4.60 — Gihisāmīcisutta
# --------------------------------------------------------------------------- #
page(
    60, "Gihisāmīci", "Lay Practice",
    vagga=VAGGA_6,
    meta_title="AN 4.60 — Lay Practice | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Gihisāmīcisutta — serving "
        "the Saṅgha with robes, almsfood, lodgings, and medicines: the four things that constitute "
        "appropriate practice for a layperson. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; Anāthapiṇḍika comes to the Buddha and the teaching begins at once"),
        ("Speakers", "The Buddha, addressing the householder Anāthapiṇḍika"),
        ("Form", "Four things named in a single clause, with two verses"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Statements of the layperson&rsquo;s proper practice appear across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and narrower than its "
                       "title suggests"),
    ],
    why=(
        "Four things, and they are the four requisites again: robes, almsfood, lodgings, medicines. "
        "Providing these to the Saṅgha is called <em>gihisāmīcipaṭipada</em>, the practice "
        "appropriate to a householder. The title makes a large promise and the content is "
        "deliberately narrow, and the gap between them is the thing to think about."),
    guide=[
        ("The teaching in one sentence", [
            "Supporting the Saṅgha with the four requisites is the practice proper to a layperson, "
            "and it brings fame and leads to heaven."]),
        ("<em>Sāmīci</em>: what is proper", [
            "<em>Sāmīcipaṭipada</em> is the practice that is fitting, proper, or correct &mdash; the "
            "same word used in the Saṅgha recollection formula, where the community practises "
            "&lsquo;the way that&rsquo;s good, direct, systematic, and proper&rsquo;. "
            "<em>Gihi</em> is a householder.",
            "So the phrase means the householder&rsquo;s version of the correct way. It is a formal "
            "designation rather than a description of everything a lay person might do, and reading "
            "it as a complete account of lay Buddhism would be a mistake the collection itself "
            "corrects several times over.",
            "AN 4.52, eight discourses earlier in this same chapter, gave a noble disciple four "
            "things that have nothing to do with giving: confidence in the Buddha, the teaching, the "
            "Saṅgha, and ethical conduct. AN 4.55 and 4.56 told a couple to match in faith, ethics, "
            "generosity, and wisdom &mdash; only one of which is generosity. This discourse is one "
            "answer among several and should be read as such."]),
        ("What is promised", [
            "<em>Yasassinī</em> and <em>saggasaṁvattanikā</em> &mdash; it brings fame, and it leads "
            "to heaven. Two results, one in this life and one after.",
            "The modesty of the promise is worth registering. Nothing is said about the path, "
            "stream-entry, or the ending of suffering, and this to Anāthapiṇḍika, who the canon "
            "elsewhere treats as a stream-enterer. Supporting the Saṅgha is being described as "
            "meritorious and appropriate, not as liberating.",
            "That is consistent throughout the collection and a teacher should not overclaim on its "
            "behalf. Giving is one of the three grounds of merit-making, alongside ethics and mental "
            "cultivation, and the collection is generally careful about which of the three does what."]),
        ("The verse and the growth of merit", [
            "<em>Their merit always grows by day and by night.</em> The claim is that the merit of "
            "supporting a practising community is continuous rather than momentary &mdash; it "
            "accrues while the donor is doing something else.",
            "That connects directly to AN 4.51, which opened this chapter. There the mechanism was "
            "given: the merit is limitless when the recipient enters a limitless immersion while "
            "using the gift. Here the consequence is stated without the mechanism.",
            "Reading the chapter as a unit, AN 4.51 explains AN 4.60. A robe given once produces "
            "merit for as long as it is worn by someone practising, which is why merit grows by day "
            "and by night without further action from the giver."]),
        ("&lsquo;Ethical and rightly comported&rsquo;", [
            "The verse specifies who is to be provided for: <em>those who are ethical and rightly "
            "comported</em>. That condition is not in the prose and it matters.",
            "Support is not owed to the Saṅgha as an institution regardless of its condition. The "
            "recipient condition runs through this entire chapter &mdash; AN 4.51&rsquo;s limitless "
            "immersion, AN 4.57&rsquo;s <em>sincere, of good conduct, big-hearted</em>, AN 4.58&rsquo;s "
            "<em>disciplined</em>, and here <em>ethical and rightly comported</em>.",
            "Four discourses in one chapter make the same qualification. Whatever else the "
            "collection&rsquo;s economics of giving amount to, they are not a blank endorsement of "
            "whoever is wearing the robe."]),
        ("Closing the chapter", [
            "The Puññābhisandavagga began with the four requisites as occasions of overflowing merit "
            "and ends with the four requisites as the definition of lay practice. Between those two "
            "points it has covered confidence and ethics as standing sources of merit, four kinds of "
            "marriage, the four things a couple should match in, and the four gifts contained in a "
            "meal.",
            "It is the chapter of the Fours addressed most consistently to householders, and it is "
            "worth reading straight through: about twelve minutes for the ten discourses, of which "
            "three are a single sentence each.",
            "The next chapter, the Pattakammavagga, continues in the same direction &mdash; AN 4.62, "
            "already published on this site, is its discourse on the four kinds of happiness "
            "available to a layperson, and it answers the question this one leaves open about what "
            "else a householder&rsquo;s life is for."]),
    ],
    terms=[
        ("gihisāmīcipaṭipada",
         "&ldquo;the practice appropriate to a householder&rdquo; &mdash; a formal designation, not a "
         "complete account of lay Buddhism."),
        ("sāmīci",
         "&ldquo;proper, fitting&rdquo; &mdash; the same word used of the Saṅgha&rsquo;s own practice "
         "in the recollection formula."),
        ("cattāro paccayā",
         "the four requisites &mdash; robes, almsfood, lodgings, and medicines and supplies for the "
         "sick; the content of the practice named here."),
        ("yasassinī",
         "&ldquo;bringing fame&rdquo; &mdash; the worldly half of the promise, alongside leading to "
         "heaven."),
        ("sīlavanta suppaṭipanna",
         "&ldquo;ethical and rightly comported&rdquo; &mdash; the verse&rsquo;s condition on the "
         "recipients, one of four such conditions in this chapter."),
    ],
    text_intro=(
        "The discourse in full: the four things, and the verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Anāthapiṇḍika comes"),
        ("p", "&sect;1", "an4.60:1.1"),
        ("h3", "Four things"),
        ("p", "&sect;2", "an4.60:2.1-2.4"),
        ("h3", "The verses"),
        ("p", "&sect;3", "an4.60:3.1-4.6"),
    ],
    quiz=[
        {"q": "What four things constitute lay practice here?",
         "opts": [
             "Faith, ethics, generosity, and wisdom",
             "Serving the Saṅgha with robes, almsfood, lodgings, and medicines",
             "The five precepts and the uposatha",
             "Long life, beauty, happiness, and strength"],
         "correct": 1,
         "expl": "The four requisites again."},
        {"q": "What does <em>sāmīci</em> mean?",
         "opts": [
             "Complete",
             "Proper, fitting, correct &mdash; the same word used of the Saṅgha&rsquo;s own practice",
             "Minimal",
             "Traditional"],
         "correct": 1,
         "expl": "So: the householder&rsquo;s version of the correct way."},
        {"q": "Why would reading this as a complete account of lay Buddhism be a mistake?",
         "opts": [
             "Because it is late",
             "Because the collection corrects it several times over &mdash; AN 4.52 gives four things with nothing to do with giving, and AN 4.55 makes generosity one of four",
             "Because it is addressed to one person",
             "Because the verses differ"],
         "correct": 1,
         "expl": "This discourse is one answer among several."},
        {"q": "What is promised?",
         "opts": [
             "Stream-entry",
             "Fame, and leading to heaven &mdash; one result in this life and one after",
             "The ending of suffering",
             "Rebirth as a god"],
         "correct": 1,
         "expl": "Nothing is said about the path."},
        {"q": "Why is that modesty worth registering?",
         "opts": [
             "Because the audience was poor",
             "Because it is said to Anāthapiṇḍika, whom the canon treats as a stream-enterer &mdash; supporting the Saṅgha is described as meritorious and appropriate, not as liberating",
             "Because heaven is temporary",
             "Because fame is a danger"],
         "correct": 1,
         "expl": "A teacher should not overclaim on the collection&rsquo;s behalf."},
        {"q": "What does the verse claim about merit?",
         "opts": [
             "That it is fixed at the moment of giving",
             "That it always grows, by day and by night",
             "That it can be transferred",
             "That it must be renewed"],
         "correct": 1,
         "expl": "Continuous rather than momentary."},
        {"q": "Which discourse explains that claim?",
         "opts": [
             "AN 4.57",
             "AN 4.51 &mdash; the merit is limitless when the recipient enters a limitless immersion while using the gift",
             "AN 4.52",
             "AN 4.55"],
         "correct": 1,
         "expl": "A robe produces merit for as long as it is worn by someone practising."},
        {"q": "What condition does the verse put on the recipients?",
         "opts": [
             "That they be senior",
             "That they be ethical and rightly comported",
             "That they be ordained",
             "That they be poor"],
         "correct": 1,
         "expl": "A condition not present in the prose."},
        {"q": "How many discourses in this chapter make a recipient condition?",
         "opts": [
             "One",
             "Four &mdash; AN 4.51, 4.57, 4.58, and this one",
             "Two",
             "None"],
         "correct": 1,
         "expl": "Not a blank endorsement of whoever is wearing the robe."},
        {"q": "How does the chapter frame itself?",
         "opts": [
             "By setting",
             "It begins with the four requisites as occasions of overflowing merit and ends with the four requisites as the definition of lay practice",
             "By speaker",
             "By length"],
         "correct": 1,
         "expl": "The chapter of the Fours addressed most consistently to householders."},
    ],
    marginalia=[
        ("The four", [
            "robes",
            "almsfood",
            "lodgings",
            "medicines",
        ]),
        ("The promise", [
            "fame &middot; now",
            "heaven &middot; after",
            "&mdash; and nothing further",
        ]),
        ("The condition", [
            "4.51 &middot; limitless immersion",
            "4.57 &middot; sincere, good conduct",
            "4.60 &middot; ethical, rightly comported",
        ]),
        ("Cross-references", [
            "AN 4.51 &middot; where the chapter began",
            "AN 4.52 &middot; lay practice without giving",
            "AN 4.62 &middot; the four lay happinesses",
        ]),
    ],
    further=[
        '<a href="%s/an4.60/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.51.html">AN 4.51 &middot; Overflowing Merit</a> &mdash; where the chapter '
        "began, and the mechanism behind this discourse&rsquo;s verse.",
        '<a href="an-4.52.html">AN 4.52 &middot; Overflowing Merit (2nd)</a> &mdash; the four things '
        "a noble disciple has that have nothing to do with giving.",
        '<a href="an-4.62.html">AN 4.62 &middot; Debtlessness</a> &mdash; the next chapter&rsquo;s '
        "discourse on the four kinds of happiness available to a layperson.",
    ],
)
