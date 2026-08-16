# -*- coding: utf-8 -*-
"""Catukka Nipāta — The Fours. One discourse per page, from AN 4.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Catukka Nipāta — The Fours"
# The Fours follow the Threes. AN 4.13, 4.55, 4.62 and 4.170 were published
# before this series began working in order; they are listed in the index by
# INDEX_EXTRA and are not generated here. HEAD points at the last page the
# Threes module has reached and moves as that module advances.
HEAD = ("an-3.20.html", "AN 3.20 &middot; A Shopkeeper (2nd)")
TAIL = ("an-4.13.html", "AN 4.13 &middot; Effort")
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
