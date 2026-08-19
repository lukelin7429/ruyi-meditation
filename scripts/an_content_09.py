# -*- coding: utf-8 -*-
"""Navaka Nipāta — The Nines. One discourse per page, from AN 9.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Navaka Nipāta — The Nines"
# HEAD points at the last page the Eights module reached. TAIL points at the
# nearest already-published page beyond the Nines -- an-10.60.html, from the
# earlier eighteen-page selection -- until the Tens module exists and TAIL
# can move to its own first page. an-9.20.html itself, also from that earlier
# selection, sits inside this module's own range (it closes ch.2,
# Sīhanādavagga) and is spliced in with explicit prev=/next= kwargs, per the
# an-6.16/an-6.63/an-7.6/an-8.30/an-8.53 precedent.
HEAD = ("an-8.148-627.html",
        "AN 8.148&ndash;627 &middot; Sixteen Defilements, Ten Verbs "
        "&mdash; Closing the Book of the Eights")
TAIL = ("an-10.60.html", "AN 10.60 &middot; With Girimānanda")
INDEX_EXTRA = [
    ("an-9.20", "Velāmasutta", "About Velāma"),
]

PAGES = []

VAGGA_1 = "<em>Sambodhivagga</em> &mdash; the first chapter of the Nines"
SETTING_SAVATTHI = "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery"
SETTING_NONE = "None stated in the source"
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Nines."""
    d = {
        "slug": "an-9.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an9/an9.%d" % num,
        "crumb": "AN 9.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 9.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 9.1 — Sambodhisutta
# --------------------------------------------------------------------------- #
page(
    1, "Sambodhi", "Awakening",
    vagga=VAGGA_1,
    meta_title="AN 9.1 — Awakening | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sambodhisutta, opening the Book of the Nines with five vital "
        "conditions for developing the qualities on the side of awakening, "
        "and a further four things grounded on them. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", SPEAKER),
        ("Form", "A rehearsed dialogue with outsiders, then five vital "
                 "conditions restated in full, then a further four things"),
        ("Length", "~2 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own name to the "
                               "chapter, <em>Sambodhivagga</em>, and opens "
                               "the entire new nipāta"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "familiar five-plus-four structure, formulaic once "
                       "seen"),
    ],
    why=(
        "The Book of the Nines opens by asking how a mendicant should "
        "answer outsiders who ask what supports the development of the "
        "qualities on the side of awakening: good friends, ethical conduct, "
        "encouraging talk, roused energy, and wisdom that sees arising and "
        "passing away &mdash; and, grounded on those five, four further "
        "things to develop toward extinguishment in this very life."),
    guide=[
        ("The teaching in one sentence", [
            "Five vital conditions support the development of the qualities "
            "on the side of awakening &mdash; good friends, ethical conduct, "
            "encouraging talk, roused energy, and wisdom into arising and "
            "passing away &mdash; and a mendicant grounded on these five "
            "should develop four further things: the perception of "
            "ugliness to give up greed, love to give up hate, mindfulness "
            "of breathing to cut off thinking, and the perception of "
            "impermanence to uproot the conceit &lsquo;I am&rsquo;."]),
        ("A new nipāta, and this chapter's own namesake", [
            "As with every new nipāta before it, the Book of the Nines "
            "opens with a discourse that lends its own subject &mdash; "
            "<em>sambodhi</em>, awakening &mdash; to the chapter's very "
            "name, <em>Sambodhivagga</em>."]),
        ("Rehearsed for outsiders, then stated in full", [
            "The discourse opens unusually: the Buddha first asks the "
            "mendicants how they would answer if wanderers of other "
            "religions questioned them, has them defer with the standard "
            "formula (&ldquo;our teachings are rooted in the "
            "Buddha&rdquo;), and only then states the five vital "
            "conditions himself, in full, for the mendicants to carry back "
            "out into such conversations."]),
        ("Five conditions, then four further things", [
            "The five vital conditions are social and ethical scaffolding "
            "&mdash; good friends, discipline, encouraging talk, energy, "
            "and insight into impermanence. Grounded on that base, four "
            "further practices target specific defilements one at a time: "
            "ugliness against greed, love against hate, breath-mindfulness "
            "against discursive thinking, and impermanence against the "
            "conceit &lsquo;I am&rsquo; &mdash; the same five-plus-four "
            "structure recurs almost verbatim at AN 9.3, addressed to a "
            "named disciple in a very different narrative setting."]),
    ],
    terms=[
        ("bodhipakkhikā dhammā",
         "&ldquo;the qualities on the same side as awakening&rdquo; "
         "&mdash; the discourse's own framing for what the five vital "
         "conditions support developing."),
        ("kalyāṇamitta, kalyāṇasahāya, kalyāṇasampavaṅka",
         "&ldquo;good friends, companions, and associates&rdquo; &mdash; "
         "the first of the five vital conditions, listed first and "
         "recurring at AN 9.3."),
        ("udayatthagāminiyā paññāya samannāgato ariyāya nibbedhikāya",
         "&ldquo;the wisdom of arising and passing away which is noble, "
         "penetrative&rdquo; &mdash; the fifth vital condition, insight "
         "into impermanence rather than mere learning."),
        ("asubhasaññā",
         "&ldquo;the perception of ugliness&rdquo; &mdash; the first of "
         "the four further things, developed to give up greed."),
        ("asmīti māno samugghātaṁ gacchati",
         "&ldquo;the conceit &lsquo;I am&rsquo; is uprooted&rdquo; "
         "&mdash; the outcome of perceiving impermanence, which stabilizes "
         "the perception of not-self."),
    ],
    text_intro=(
        "The discourse in full: a rehearsed answer for outsiders, five "
        "vital conditions, and four further things. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Rehearsing an answer for outsiders"),
        ("p", "&sect;1", "an9.1:1.1-1.3"),
        ("p", "&sect;2", "an9.1:2.1-3.3"),
        ("h3", "Five vital conditions, stated in full"),
        ("p", "&sect;3", "an9.1:4.1-4.2"),
        ("p", "&sect;4", "an9.1:5.1-5.2"),
        ("p", "&sect;5", "an9.1:6.1-6.2"),
        ("p", "&sect;6", "an9.1:7.1-7.2"),
        ("p", "&sect;7", "an9.1:8.1-8.2"),
        ("p", "&sect;8", "an9.1:9.1-9.2"),
        ("p", "&sect;9", "an9.1:10.1-13.2"),
        ("h3", "Four further things"),
        ("p", "&sect;10", "an9.1:14.1-14.4"),
    ],
    quiz=[
        {"q": "How does the discourse open, before stating the five vital "
              "conditions?",
         "opts": [
             "With a deity's visit", "With a rehearsed answer for how to "
             "respond if outsiders ask about the conditions for awakening",
             "With a dispute between two mendicants",
             "With a narrative about robes"],
         "correct": 1,
         "expl": "The mendicants first defer with the standard formula, "
                 "then the Buddha states the five conditions in full."},
        {"q": "What are the five vital conditions for developing the "
              "qualities on the side of awakening?",
         "opts": [
             "Wealth, fame, long life, health, and beauty",
             "Good friends, ethical conduct, encouraging talk, roused "
             "energy, and wisdom into arising and passing away",
             "The four right efforts plus one more",
             "The eight liberations"],
         "correct": 1,
         "expl": "Social and ethical scaffolding, ending in penetrative "
                 "wisdom."},
        {"q": "What four further things should a mendicant grounded on "
              "those five develop?",
         "opts": [
             "Four more kinds of ethical conduct",
             "The perception of ugliness, love, mindfulness of breathing, "
             "and the perception of impermanence, against greed, hate, "
             "thinking, and the conceit &lsquo;I am&rsquo; in turn",
             "Four kinds of almsfood",
             "Four monastic robes"],
         "correct": 1,
         "expl": "Four targeted practices, each aimed at a specific "
                 "defilement."},
        {"q": "According to the guide, where does this same five-plus-four "
              "structure recur almost verbatim?",
         "opts": [
             "Nowhere else in this nipāta", "At AN 9.3, addressed to the "
             "disciple Meghiya in a very different narrative setting",
             "Only in the Sevens", "At AN 9.9"],
         "correct": 1,
         "expl": "Same list, a different frame and setting."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular", "Its own subject, <em>sambodhi</em> "
             "(awakening), naming <em>Sambodhivagga</em>",
             "A disciple's name", "A place name"],
         "correct": 1,
         "expl": "As with every new nipāta's opener, the discourse names "
                 "its own chapter."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood", "Cālikā, on the mountain"],
         "correct": 1,
         "expl": "The standard opening setting for a new nipāta's first "
                 "discourse."},
    ],
    marginalia=[
        ("Five vital conditions", [
            "good friends, discipline,",
            "talk that opens the heart,",
            "energy, and insight",
        ]),
        ("Four further things", [
            "ugliness against greed,",
            "love against hate, breath",
            "against thought, change against &lsquo;I am&rsquo;",
        ]),
        ("A new nipāta's own namesake", [
            "sambodhi gives its name",
            "to Sambodhivagga &mdash;",
            "the chapter it opens",
        ]),
        ("Cross-references", [
            "AN 8.148&ndash;627 &middot; previous nipāta, closing the Eights",
            "AN 9.3 &middot; next but one, the same five-plus-four "
            "structure recurs",
        ]),
    ],
    further=[
        '<a href="%s/an9.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-8.148-627.html">AN 8.148&ndash;627</a> &mdash; previous, closing the '
        "Book of the Eights.",
        '<a href="an-9.2.html">AN 9.2 &middot; Supported</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.2 — Nissayasutta
# --------------------------------------------------------------------------- #
page(
    2, "Nissaya", "Supported",
    vagga=VAGGA_1,
    meta_title="AN 9.2 — Supported | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nissayasutta, defining what it means for a mendicant to be "
        "&ldquo;supported&rdquo; by five qualities, then to rely on four "
        "further things by way of appraisal. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.1"),
        ("Speakers", "A mendicant questioning the Buddha"),
        ("Form", "A question-and-answer dialogue, five supports followed by "
                 "four things relied on after appraisal"),
        ("Length", "~1 minute to read"),
        ("A term explained by use, not defined outright", "The mendicant "
         "asks what &ldquo;supported&rdquo; means; the Buddha answers by "
         "showing how each support functions, not with a bare definition"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and direct"),
    ],
    why=(
        "A mendicant asks what it means to be &ldquo;supported,&rdquo; and "
        "the Buddha answers with five qualities &mdash; faith, conscience, "
        "prudence, energy, and wisdom &mdash; each of which, when it "
        "supports giving up the unskillful and developing the skillful, "
        "actually accomplishes that giving up, and four further things a "
        "mendicant grounded on those five relies on only after appraisal."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant is &ldquo;supported&rdquo; when faith, conscience, "
            "prudence, energy, or wisdom actually accomplishes the giving "
            "up of the unskillful and the development of the skillful, and "
            "when, grounded on these five, they use some things, endure "
            "some things, avoid some things, and get rid of some things, "
            "all after appraisal."]),
        ("A question about a word", [
            "Unlike AN 9.1's rehearsed answer for outsiders, this "
            "discourse opens with a mendicant's direct question about "
            "terminology: what does it mean for a mendicant to be called "
            "&ldquo;supported&rdquo;? The Buddha's answer works by showing "
            "the term in action rather than defining it abstractly."]),
        ("Five supports, one shared test", [
            "Faith, conscience, prudence, energy, and wisdom are each "
            "tested the same way: does relying on this quality actually "
            "accomplish giving up the unskillful and developing the "
            "skillful? What has been given up counts as completely given "
            "up only when seen with noble wisdom &mdash; the fifth support "
            "closes and validates the other four."]),
        ("Four things, always after appraisal", [
            "The four things a supported mendicant relies on &mdash; "
            "using, enduring, avoiding, and getting rid of &mdash; are "
            "each qualified by the same phrase, &lsquo;after "
            "appraisal.&rsquo; This is the same reflective-use logic "
            "spelled out at length elsewhere for a mendicant's four "
            "requisites, compressed here into a single closing line."]),
    ],
    terms=[
        ("nissito",
         "&ldquo;supported&rdquo; &mdash; the term the questioning "
         "mendicant asks about, and the discourse's own title word."),
        ("saddhānissito",
         "&ldquo;supported by faith&rdquo; &mdash; the first of the five "
         "supports, tested by whether it accomplishes giving up the "
         "unskillful."),
        ("ariyāya paññāya passato",
         "&ldquo;seeing with noble wisdom&rdquo; &mdash; the standard by "
         "which what has been given up counts as completely given up."),
        ("paṭisaṅkhā yoniso",
         "&ldquo;after appraisal&rdquo; &mdash; the qualifier attached to "
         "each of the four things a supported mendicant relies on."),
        ("sevati, adhivāseti, parivajjeti, vinodeti",
         "&ldquo;uses, endures, avoids, and gets rid of&rdquo; &mdash; the "
         "four things relied on, a compressed echo of the fuller "
         "reflective-use teaching on a mendicant's requisites."),
    ],
    text_intro=(
        "The discourse in full: a question about what &ldquo;"
        "supported&rdquo; means, five supports, and four things relied on "
        "after appraisal. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A question about a word"),
        ("p", "&sect;1", "an9.2:1.1-1.3"),
        ("h3", "Five supports"),
        ("p", "&sect;2", "an9.2:1.4-1.9"),
        ("h3", "Four things, after appraisal"),
        ("p", "&sect;3", "an9.2:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse open?",
         "opts": [
             "With a deity's visit", "With a mendicant asking the Buddha "
             "what it means to be &ldquo;supported&rdquo;",
             "With a dispute between two mendicants",
             "With a narrative about robes"],
         "correct": 1,
         "expl": "A direct question about terminology opens this brief "
                 "discourse."},
        {"q": "What are the five supports named?",
         "opts": [
             "Faith, conscience, prudence, energy, and wisdom",
             "The five hindrances",
             "The five aggregates",
             "The five precepts"],
         "correct": 0,
         "expl": "Each tested by whether it actually accomplishes giving "
                 "up the unskillful."},
        {"q": "By what test is each of the five supports judged?",
         "opts": [
             "By how long it has been practiced",
             "By whether it actually accomplishes giving up the unskillful "
             "and developing the skillful",
             "By how it is described to outsiders",
             "By its popularity among mendicants"],
         "correct": 1,
         "expl": "A functional test, not a definition."},
        {"q": "What four things does a supported mendicant rely on, and "
              "how?",
         "opts": [
             "Four robes, worn in rotation",
             "Using, enduring, avoiding, and getting rid of things &mdash; "
             "each only after appraisal",
             "Four teachers, consulted in turn",
             "Four seasons of retreat"],
         "correct": 1,
         "expl": "Reflective use, echoing the fuller requisites teaching "
                 "found elsewhere."},
        {"q": "According to the guide, what validates the other four "
              "supports?",
         "opts": [
             "Energy", "Wisdom, since what is given up counts as "
             "completely given up only when seen with noble wisdom",
             "Faith alone", "Conscience alone"],
         "correct": 1,
         "expl": "The fifth support closes and validates the first four."},
        {"q": "How does the Buddha's answer approach the term "
              "&ldquo;supported&rdquo;?",
         "opts": [
             "With a bare dictionary definition",
             "By showing the term in action through five supports and "
             "four appraised reliances, rather than defining it abstractly",
             "By refusing to answer",
             "By quoting an earlier discourse verbatim"],
         "correct": 1,
         "expl": "Function over definition, as the guide notes."},
    ],
    marginalia=[
        ("Five supports, one test", [
            "faith, conscience, prudence,",
            "energy, wisdom &mdash;",
            "does it give up the unskillful?",
        ]),
        ("Four things, after appraisal", [
            "use, endure, avoid,",
            "get rid of &mdash;",
            "never without reflection",
        ]),
        ("A question about a word", [
            "&ldquo;supported,&rdquo; a mendicant asks &mdash;",
            "shown in action,",
            "not defined outright",
        ]),
        ("Cross-references", [
            "AN 9.1 &middot; previous, five conditions and four further "
            "things",
            "AN 9.3 &middot; next, With Meghiya",
        ]),
    ],
    further=[
        '<a href="%s/an9.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.1.html">AN 9.1 &middot; Awakening</a> &mdash; previous.',
        '<a href="an-9.3.html">AN 9.3 &middot; With Meghiya</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.3 — Meghiyasutta
# --------------------------------------------------------------------------- #
page(
    3, "Meghiya", "With Meghiya",
    vagga=VAGGA_1,
    meta_title="AN 9.3 — With Meghiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "famous Meghiyasutta, in which the Buddha's attendant insists on "
        "leaving to meditate alone, is beset by bad thoughts, and receives "
        "the same five-plus-four teaching given at AN 9.1. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Cālikā, on the Cālikā mountain"),
        ("Speakers", "Venerable Meghiya, the Buddha's attendant at the "
                     "time, and the Buddha"),
        ("Form", "An extended narrative &mdash; a threefold request, a "
                 "meditation attempt beset by bad thoughts, and a return "
                 "to the same five-plus-four teaching as AN 9.1"),
        ("Length", "~4 minutes to read"),
        ("A well-known parallel", "This discourse has a close parallel at "
                                  "Udāna 4.1, one of the most frequently "
                                  "cited episodes involving an attendant "
                                  "of the Buddha"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a rich "
                       "narrative wrapped around a teaching already met "
                       "at AN 9.1"),
    ],
    why=(
        "Meghiya begs the Buddha three times for permission to go meditate "
        "alone in a lovely mango grove, is granted it, and is promptly "
        "beset by sensual, malicious, and cruel thoughts &mdash; when he "
        "returns to report this, the Buddha explains that the heart's "
        "release, when not yet ripe, is ripened by the same five things "
        "named at AN 9.1, and grounded on those five, the same four "
        "further things."),
    guide=[
        ("The teaching in one sentence", [
            "When the heart's release is not yet ripe, five things help "
            "it ripen &mdash; good friends, ethical conduct, encouraging "
            "talk, roused energy, and wisdom into arising and passing "
            "away &mdash; and a mendicant grounded on these five should "
            "develop four further things: the perception of ugliness "
            "against greed, love against hate, mindfulness of breathing "
            "against thinking, and the perception of impermanence to "
            "uproot the conceit &lsquo;I am&rsquo;."]),
        ("Three requests, twice refused", [
            "Meghiya asks the Buddha's permission to go meditate alone in "
            "a mango grove he has found lovely and delightful. Twice the "
            "Buddha replies only &ldquo;we're alone, Meghiya, wait until "
            "another mendicant comes&rdquo; &mdash; and only on the third "
            "asking, when Meghiya frames it explicitly as striving in "
            "meditation, does the Buddha let him go."]),
        ("Solitude alone was not enough", [
            "Once alone under a tree, Meghiya is beset mostly by three "
            "kinds of bad, unskillful thoughts &mdash; sensual, "
            "malicious, and cruel &mdash; and is startled that thoughts "
            "like these still harass him despite having gone forth out of "
            "faith. Wanting solitude, on its own, did not protect him."]),
        ("The same five-plus-four teaching as AN 9.1", [
            "When Meghiya reports this, the Buddha's answer is, item for "
            "item, the same five vital conditions and four further "
            "practices given two discourses earlier at AN 9.1 &mdash; "
            "there framed as an answer for outsiders, here as medicine "
            "for an attendant's own beset meditation. The frame changes "
            "entirely; the list itself does not."]),
    ],
    terms=[
        ("kimikāḷāya nadiyā tīraṁ",
         "&ldquo;the shore of the Kimikālā river&rdquo; &mdash; where "
         "Meghiya finds the mango grove that draws him to ask for leave."),
        ("āgamehi tāva, meghiya",
         "&ldquo;wait a while, Meghiya&rdquo; &mdash; the Buddha's twice-"
         "repeated refusal, before granting leave on the third request."),
        ("kāmavitakko, byāpādavitakko, vihiṁsāvitakko",
         "&ldquo;sensual, malicious, and cruel thoughts&rdquo; &mdash; the "
         "three kinds of bad, unskillful thought that beset Meghiya alone "
         "in the mango grove."),
        ("aparipakkāya cetovimuttiyā",
         "&ldquo;when the heart's release is not yet ripe&rdquo; &mdash; "
         "this discourse's own framing for the same five things named at "
         "AN 9.1."),
        ("acchariyaṁ vata bho, abbhutaṁ vata bho",
         "&ldquo;oh lord, how incredible, how amazing&rdquo; &mdash; "
         "Meghiya's own exclamation on finding himself still harassed by "
         "bad thoughts despite having gone forth."),
    ],
    text_intro=(
        "The discourse in full: three requests, a meditation beset by bad "
        "thoughts, and the same five-plus-four teaching given at AN 9.1. "
        "Two short stretches here (Meghiya repeating his own story back to "
        "the Buddha) are written out in full in the Pali but left "
        "untranslated in the English, since they simply repeat what "
        "Meghiya has just said; the guide notes rather than fills that "
        "gap. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A lovely mango grove, and a threefold request"),
        ("p", "&sect;1", "an9.3:1.1-1.5"),
        ("p", "&sect;2", "an9.3:2.1-2.6"),
        ("p", "&sect;3", "an9.3:3.1-6.6"),
        ("h3", "Beset by bad thoughts"),
        ("p", "&sect;4", "an9.3:7.1-8.1"),
        ("h3", "Five things that ripen the heart's release"),
        ("p", "&sect;5", "an9.3:10.1-10.4"),
        ("p", "&sect;6", "an9.3:11.1-11.2"),
        ("p", "&sect;7", "an9.3:12.1-12.2"),
        ("p", "&sect;8", "an9.3:13.1-13.2"),
        ("p", "&sect;9", "an9.3:14.1-18.1"),
        ("h3", "Four further things"),
        ("p", "&sect;10", "an9.3:19.1-19.4"),
    ],
    quiz=[
        {"q": "How many times does Meghiya ask the Buddha's permission to "
              "go meditate alone, and what changes on the last time?",
         "opts": [
             "Once, and the Buddha refuses outright",
             "Three times; only on the third, when Meghiya frames it as "
             "striving in meditation, does the Buddha agree",
             "Twice, and a third mendicant decides for him",
             "Three times, and the Buddha never explains why he agrees"],
         "correct": 1,
         "expl": "Twice refused with &ldquo;wait a while,&rdquo; granted "
                 "on the third asking."},
        {"q": "What happens once Meghiya is alone in the mango grove?",
         "opts": [
             "He attains awakening immediately",
             "He is beset mostly by sensual, malicious, and cruel thoughts",
             "He falls asleep", "He is visited by a deity"],
         "correct": 1,
         "expl": "Solitude alone did not protect him from these three "
                 "kinds of thought."},
        {"q": "What five things does the Buddha say ripen the heart's "
              "release when it is not yet ripe?",
         "opts": [
             "Wealth, fame, long life, health, and beauty",
             "Good friends, ethical conduct, encouraging talk, roused "
             "energy, and wisdom into arising and passing away",
             "The four right efforts plus one more",
             "The eight liberations"],
         "correct": 1,
         "expl": "The same five vital conditions named at AN 9.1."},
        {"q": "According to the guide, how does this teaching relate to "
              "AN 9.1?",
         "opts": [
             "It is completely unrelated",
             "It is, item for item, the same five-plus-four list, given "
             "there as an answer for outsiders and here as medicine for "
             "Meghiya's beset meditation",
             "It reverses the order of the five conditions",
             "It adds a fifth further practice"],
         "correct": 1,
         "expl": "Same list, a different narrative frame."},
        {"q": "What does the guide note about two stretches of this "
              "discourse where Meghiya repeats his own story?",
         "opts": [
             "They are missing from the Pali entirely",
             "They are written out in full in the Pali but left "
             "untranslated in the English, since they simply repeat what "
             "was already said",
             "They contain a scribal error",
             "They were added by a later editor"],
         "correct": 1,
         "expl": "A translator's elision of verbatim repetition, not a "
                 "gap in the source."},
        {"q": "Where is this discourse set, and what well-known parallel "
              "does it have?",
         "opts": [
             "Sāvatthī; no known parallel",
             "Cālikā, on the Cālikā mountain; a close parallel at Udāna 4.1",
             "Rājagaha; a parallel at MN 2",
             "Vesālī; a parallel at DN 16"],
         "correct": 1,
         "expl": "One of the most frequently cited episodes involving an "
                 "attendant of the Buddha."},
    ],
    marginalia=[
        ("A threefold request", [
            "&ldquo;wait a while, Meghiya&rdquo; &mdash;",
            "twice refused, once granted &mdash;",
            "striving in meditation",
        ]),
        ("Beset in the mango grove", [
            "sensual, malicious,",
            "cruel thoughts still rise &mdash;",
            "solitude was not enough",
        ]),
        ("The same five, a new frame", [
            "friends, conduct, talk,",
            "energy, insight &mdash; ripening",
            "what outsiders were told",
        ]),
        ("Cross-references", [
            "AN 9.1 &middot; the same five-plus-four teaching, first given",
            "AN 9.4 &middot; next, With Nandaka",
        ]),
    ],
    further=[
        '<a href="%s/an9.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.1.html">AN 9.1 &middot; Awakening</a> &mdash; earlier, the same '
        "five-plus-four teaching in its original frame.",
        '<a href="an-9.2.html">AN 9.2 &middot; Supported</a> &mdash; previous.',
        '<a href="an-9.4.html">AN 9.4 &middot; With Nandaka</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.4 — Nandakasutta
# --------------------------------------------------------------------------- #
page(
    4, "Nandaka", "With Nandaka",
    vagga=VAGGA_1,
    meta_title="AN 9.4 — With Nandaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nandakasutta, in which the Buddha teases a mendicant about a long "
        "Dhamma talk, then teaches a four-statement progression toward "
        "completeness and five benefits of timely teaching. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s "
                    "monastery"),
        ("Speakers", "The Buddha, Venerable Nandaka, and the assembled "
                     "mendicants"),
        ("Form", "A narrative opening with gentle humor, a four-statement "
                 "progression with a simile, then Nandaka's own added "
                 "teaching on five benefits"),
        ("Length", "~5 minutes to read"),
        ("Two teachings, two teachers", "The Buddha gives the four-"
                                        "statement progression; Nandaka, "
                                        "repeating it to the mendicants, "
                                        "adds a further five benefits of "
                                        "his own"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "narrative frame carrying two distinct teachings"),
    ],
    why=(
        "The Buddha waits outside the door while Nandaka gives a long "
        "Dhamma talk, then teases him about his aching back before "
        "teaching a four-statement progression toward a spiritual practice "
        "&ldquo;entirely full and pure&rdquo; &mdash; faithful, then "
        "ethical, then internally serene, then wise &mdash; which Nandaka "
        "repeats to the mendicants and caps with five benefits of "
        "listening to and discussing the teachings at the right time."),
    guide=[
        ("The teaching in one sentence", [
            "A spiritual practice is entirely full and pure only once a "
            "mendicant is faithful and ethical, gets internal serenity of "
            "heart, and gets the higher wisdom of discernment of "
            "principles &mdash; each stage incomplete, like a lame four-"
            "footed animal, until the next is added."]),
        ("A backache, met with humor", [
            "The Buddha stands outside the assembly hall waiting for "
            "Nandaka's talk to end, then greets him not with a rebuke but "
            "with a wry complaint about his aching back &mdash; Nandaka's "
            "embarrassment, and the Buddha's immediate reassurance "
            "(&ldquo;good, good, Nandaka&rdquo;), frame the substantial "
            "teaching that follows."]),
        ("Four statements, one simile", [
            "The progression moves through four additions &mdash; faith "
            "and ethics, then internal serenity, then the higher wisdom "
            "of discernment of principles &mdash; each stage declared "
            "incomplete until the next is fulfilled, illustrated by a "
            "lame four-footed animal that remains disabled no matter how "
            "sound its other three legs."]),
        ("Nandaka adds his own five benefits", [
            "After the Buddha leaves, Nandaka repeats the four-statement "
            "teaching to the assembly and adds a teaching of his own: five "
            "benefits of listening to and discussing the teachings at the "
            "right time, ranging from becoming liked and respected by the "
            "Teacher to inspiring both trainees still striving and "
            "perfected ones already free."]),
    ],
    terms=[
        ("kevalaparipuṇṇaṁ parisuddhaṁ brahmacariyaṁ",
         "&ldquo;a spiritual practice that's entirely full and pure&rdquo; "
         "&mdash; what the four-statement progression builds toward."),
        ("catuppadaṁ jarasiṅgālaṁ",
         "the lame four-footed animal simile &mdash; illustrating "
         "incompleteness so long as any one of the four stages is missing."),
        ("ajjhattaṁ cetosamathaṁ",
         "&ldquo;internal serenity of heart&rdquo; &mdash; the third "
         "stage, following faith and ethics and preceding higher wisdom."),
        ("adhipaññādhammavipassanā",
         "&ldquo;the higher wisdom of discernment of principles&rdquo; "
         "&mdash; the fourth and final stage of the progression."),
        ("kālena dhammassavanassa, kālena dhammasākacchāya",
         "&ldquo;listening to the teachings at the right time... "
         "discussing the teachings at the right time&rdquo; &mdash; "
         "Nandaka's own added teaching, naming its five benefits."),
    ],
    text_intro=(
        "The discourse in full: a backache met with humor, a four-"
        "statement progression with its simile, and Nandaka's own five "
        "benefits of timely teaching. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A long talk, and an aching back"),
        ("p", "&sect;1", "an9.4:1.1-3.3"),
        ("h3", "Four statements, one simile"),
        ("p", "&sect;2", "an9.4:4.1-7.1"),
        ("p", "&sect;3", "an9.4:7.2-7.3"),
        ("h3", "Nandaka repeats it, and adds five benefits"),
        ("p", "&sect;4", "an9.4:8.1-8.18"),
        ("p", "&sect;5", "an9.4:9.1-9.5"),
        ("p", "&sect;6", "an9.4:10.1-10.3"),
        ("p", "&sect;7", "an9.4:11.1-11.3"),
        ("p", "&sect;8", "an9.4:12.1-12.4"),
        ("p", "&sect;9", "an9.4:13.1-13.5"),
    ],
    quiz=[
        {"q": "Why does the Buddha tease Nandaka about his back?",
         "opts": [
             "Nandaka fell asleep during a talk",
             "The Buddha stood outside the assembly hall door waiting for "
             "Nandaka's long Dhamma talk to end",
             "Nandaka refused to teach",
             "Nandaka gave a talk that contradicted the Buddha"],
         "correct": 1,
         "expl": "Gentle humor, met with immediate reassurance once "
                 "Nandaka is embarrassed."},
        {"q": "What four stages make up the progression toward a "
              "spiritual practice &ldquo;entirely full and pure&rdquo;?",
         "opts": [
             "Faith and ethics, internal serenity, and the higher wisdom "
             "of discernment of principles",
             "The four noble truths",
             "The four right efforts",
             "The four bases of psychic power"],
         "correct": 0,
         "expl": "Each stage incomplete until the next is added."},
        {"q": "What simile illustrates incompleteness in this progression?",
         "opts": [
             "A raft for crossing a flood",
             "A lame four-footed animal, disabled no matter how sound its "
             "other three legs",
             "A well-tuned lute",
             "A lotus rising above the water"],
         "correct": 1,
         "expl": "Missing any one stage leaves the whole practice "
                 "incomplete."},
        {"q": "Who adds the five benefits of timely teaching, and to whom?",
         "opts": [
             "The Buddha, to Nandaka alone",
             "Nandaka, repeating the four-statement teaching to the "
             "assembled mendicants and adding this teaching of his own",
             "A deity, to the whole assembly",
             "Sāriputta, in a separate discourse"],
         "correct": 1,
         "expl": "Two distinct teachings from two different teachers "
                 "within the same discourse."},
        {"q": "According to the five benefits, who is inspired by hearing "
              "timely teaching?",
         "opts": [
             "Only perfected mendicants",
             "Both trainees still striving toward the unattained and "
             "perfected ones who simply live happily",
             "Only lay supporters",
             "Only the Teacher"],
         "correct": 1,
         "expl": "The fifth benefit names both kinds of listener."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Cālikā, on the Cālikā mountain", "Vesālī"],
         "correct": 1,
         "expl": "The same setting as AN 9.1, though not explicitly "
                 "restated at AN 9.2 or 9.3."},
    ],
    marginalia=[
        ("A backache, met with humor", [
            "&ldquo;good, good, Nandaka&rdquo; &mdash;",
            "embarrassment turned",
            "to reassurance",
        ]),
        ("Four stages, one simile", [
            "faith, ethics, calm, wisdom &mdash;",
            "a lame animal",
            "until all four are sound",
        ]),
        ("Nandaka's own five benefits", [
            "liked by the Teacher,",
            "inspired by meaning &mdash;",
            "trainee and perfected alike",
        ]),
        ("Cross-references", [
            "AN 9.3 &middot; previous, With Meghiya",
            "AN 9.5 &middot; next, Powers",
        ]),
    ],
    further=[
        '<a href="%s/an9.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.3.html">AN 9.3 &middot; With Meghiya</a> &mdash; previous.',
        '<a href="an-9.5.html">AN 9.5 &middot; Powers</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.5 — Balasutta
# --------------------------------------------------------------------------- #
page(
    5, "Bala", "Powers",
    vagga=VAGGA_1,
    meta_title="AN 9.5 — Powers | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Balasutta, on the four powers of wisdom, energy, blamelessness, "
        "and inclusiveness, and the five fears a disciple who has them has "
        "gotten past. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Four powers defined in turn, the fourth expanded into a "
                 "well-known tetrad of its own, then five fears reflected "
                 "away one by one"),
        ("Length", "~3 minutes to read"),
        ("A tetrad within a tetrad", "The fourth power, inclusiveness, "
                                     "unpacks into the four standard means "
                                     "of inclusion &mdash; giving, kindly "
                                     "words, taking care, and equality "
                                     "&mdash; a tetrad well known elsewhere "
                                     "in the canon"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; two "
                       "layered lists, straightforward once distinguished"),
    ],
    why=(
        "Four powers &mdash; wisdom, energy, blamelessness, and "
        "inclusiveness &mdash; are defined in turn, with inclusiveness "
        "itself unpacking into the four standard means of inclusion, "
        "before the discourse turns to five fears a noble disciple who has "
        "these four powers has gotten past: livelihood, disrepute, "
        "insecurity in an assembly, death, and bad rebirth."),
    guide=[
        ("The teaching in one sentence", [
            "A noble disciple who has the four powers of wisdom, energy, "
            "blamelessness, and inclusiveness can reflect, for each of "
            "five common fears in turn, that only a witless, lazy, "
            "blameworthy, or exclusive person would have reason to fear "
            "it."]),
        ("Four powers, defined by function", [
            "Wisdom is clear-seeing that sorts qualities as skillful or "
            "not; energy is the effort to give up the unskillful and gain "
            "the skillful; blamelessness is blameless conduct by body, "
            "speech, and mind; inclusiveness is generosity toward "
            "others."]),
        ("A tetrad within a tetrad", [
            "Unpacking the fourth power, the discourse names the four "
            "standard means of inclusion &mdash; giving, kindly words, "
            "taking care, and equality &mdash; and for each names its "
            "best form: the gift of the teaching, repeated Dhamma talk to "
            "an engaged listener, grounding others in faith and virtue, "
            "and the equality of stream-enterers, once-returners, non-"
            "returners, and perfected ones with their own kind."]),
        ("Five fears, reflected away", [
            "For fear of livelihood, disrepute, insecurity in an "
            "assembly, death, and bad rebirth in turn, the discourse has "
            "the disciple run the same reflection: only someone witless, "
            "lazy, blameworthy in conduct, or exclusive of others has "
            "reason to fear this &mdash; and since none of those "
            "descriptions apply, the fear has no footing."]),
    ],
    terms=[
        ("paññābala, vīriyabala, anavajjabala, saṅgahabala",
         "&ldquo;the powers of wisdom, energy, blamelessness, and "
         "inclusiveness&rdquo; &mdash; the discourse's own four powers, "
         "named at the outset."),
        ("cattāri saṅgahavatthūni",
         "&ldquo;the four ways of being inclusive&rdquo; &mdash; giving, "
         "kindly words, taking care, and equality, a standard tetrad "
         "unpacked here from the fourth power."),
        ("dānānaṁ dhammadānaṁ",
         "&ldquo;the best of gifts is the gift of the teaching&rdquo; "
         "&mdash; the best form named for the first means of inclusion."),
        ("samānattatā",
         "&ldquo;equality&rdquo; &mdash; the fourth means of inclusion, "
         "its best form being solidarity among disciples at the same "
         "stage of awakening."),
        ("pañca bhayāni atikkanto",
         "&ldquo;has got past five fears&rdquo; &mdash; what a noble "
         "disciple with the four powers has accomplished, reflected on "
         "one fear at a time."),
    ],
    text_intro=(
        "The discourse in full: four powers, the fourth unpacked into its "
        "own tetrad, and five fears reflected away. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four powers"),
        ("p", "&sect;1", "an9.5:1.1-1.6"),
        ("p", "&sect;2", "an9.5:2.1-2.4"),
        ("p", "&sect;3", "an9.5:3.1-3.3"),
        ("h3", "Inclusiveness, unpacked"),
        ("p", "&sect;4", "an9.5:4.1-4.9"),
        ("h3", "Five fears, reflected away"),
        ("p", "&sect;5", "an9.5:5.1-5.24"),
    ],
    quiz=[
        {"q": "What are the four powers named at the outset of this "
              "discourse?",
         "opts": [
             "Faith, energy, mindfulness, and immersion",
             "Wisdom, energy, blamelessness, and inclusiveness",
             "The four noble truths",
             "The four right efforts"],
         "correct": 1,
         "expl": "Each power is then defined in turn by its function."},
        {"q": "What four means of inclusion are unpacked from the fourth "
              "power?",
         "opts": [
             "Giving, kindly words, taking care, and equality",
             "Ethics, immersion, wisdom, and freedom",
             "The four foundations of mindfulness",
             "The four bases of psychic power"],
         "correct": 0,
         "expl": "A standard tetrad well known elsewhere, unpacked here "
                 "from inclusiveness."},
        {"q": "What is named as the best form of giving, among the four "
              "means of inclusion?",
         "opts": [
             "The gift of material wealth",
             "The gift of the teaching",
             "The gift of shelter",
             "The gift of medicine"],
         "correct": 1,
         "expl": "The discourse names a best form for each of the four "
                 "means."},
        {"q": "What five fears has a disciple with the four powers gotten "
              "past?",
         "opts": [
             "Fear of the dark, of animals, of storms, of illness, and of "
             "old age",
             "Fear regarding livelihood, disrepute, feeling insecure in "
             "an assembly, death, and bad rebirth",
             "The five hindrances",
             "Fear of the five aggregates"],
         "correct": 1,
         "expl": "Each reflected away one at a time using the same "
                 "reasoning."},
        {"q": "What reflection does the disciple use to get past each "
              "fear?",
         "opts": [
             "That fear itself is an illusion",
             "That only someone witless, lazy, blameworthy, or exclusive "
             "of others has reason to fear it",
             "That fear can be bribed away",
             "That a teacher will always intervene"],
         "correct": 1,
         "expl": "The same fourfold reasoning, repeated for each fear in "
                 "turn."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, unlike the narrative discourses "
                 "immediately preceding it."},
    ],
    marginalia=[
        ("Four powers", [
            "wisdom, energy,",
            "blamelessness, and",
            "inclusiveness of others",
        ]),
        ("A tetrad within a tetrad", [
            "giving, kind words,",
            "care, and equality &mdash;",
            "the best form of each",
        ]),
        ("Five fears, reflected away", [
            "livelihood, disrepute,",
            "the assembly, death, rebirth &mdash;",
            "none has a footing",
        ]),
        ("Cross-references", [
            "AN 9.4 &middot; previous, With Nandaka",
            "AN 9.6 &middot; next, Association",
        ]),
    ],
    further=[
        '<a href="%s/an9.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.4.html">AN 9.4 &middot; With Nandaka</a> &mdash; previous.',
        '<a href="an-9.6.html">AN 9.6 &middot; Association</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.6 — Sevitabbasutta
# --------------------------------------------------------------------------- #
page(
    6, "Sevitabba", "Association",
    vagga=VAGGA_1,
    meta_title="AN 9.6 — Association | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sevitabbasutta, in which Sāriputta teaches how to distinguish six "
        "kinds of person, robe, food, lodging, village, and country by a "
        "shared test of what grows and what declines. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from the "
                    "chapter's opening"),
        ("Speakers", "Venerable Sāriputta, addressing the mendicants"),
        ("Form", "Six domains in turn, each split into two kinds by a "
                 "shared test, with individuals given a fuller three-"
                 "factor analysis the other five domains don't receive"),
        ("Length", "~4 minutes to read"),
        ("One test, six domains, one exception", "Robes, almsfood, "
         "lodging, villages, and countries are each judged by a single "
         "growth test; people alone get a fuller three-factor analysis"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "repetitive structure across six domains, worth "
                       "reading for where it varies"),
    ],
    why=(
        "Sāriputta teaches the mendicants to distinguish two kinds each of "
        "person, robe, almsfood, lodging, village or town, and country "
        "&mdash; those to associate with, wear, eat, frequent, or avoid "
        "&mdash; by whether unskillful qualities grow or decline in "
        "connection with each, with the test for people alone extended to "
        "weigh the ease of requisites and the ascetic goal itself."),
    guide=[
        ("The teaching in one sentence", [
            "Across six domains &mdash; people, robes, almsfood, lodging, "
            "villages and towns, and countries &mdash; distinguish the "
            "kind that should be associated with or used from the kind "
            "that shouldn't, by whether unskillful qualities grow or "
            "skillful qualities grow in connection with it."]),
        ("A shared refrain, six times", [
            "Sāriputta announces each distinction with the same refrain "
            "&mdash; &lsquo;you should distinguish two kinds of X: those "
            "you should Y, and those you shouldn't&rsquo; &mdash; then "
            "explains why he said it, then repeats the refrain to close "
            "the point, for people, robes, almsfood, lodging, villages, "
            "and countries in turn."]),
        ("People get a fuller test; the rest get one factor", [
            "For robes, almsfood, lodging, villages, and countries, the "
            "sole test is whether unskillful qualities grow or skillful "
            "qualities grow. For people alone, Sāriputta adds two further "
            "factors: whether a renunciate's requisites are easy or hard "
            "to come by around this person, and whether the ascetic goal "
            "itself is being fully developed &mdash; and the goal outweighs "
            "ease of requisites in every case."]),
        ("Follow even if sent away", [
            "The strongest instruction in the discourse is reserved for "
            "the one clearly beneficial kind of person: when unskillful "
            "qualities decline, skillful qualities grow, requisites are "
            "easy to come by, and the goal is being fully developed, a "
            "mendicant should follow that person and not leave them, "
            "&ldquo;even if they send you away.&rdquo;"]),
    ],
    terms=[
        ("sevitabbo puggalo, na sevitabbo puggalo",
         "&ldquo;an individual to be associated with, an individual not "
         "to be associated with&rdquo; &mdash; the discourse's own title "
         "distinction, applied first to people and then, by the same "
         "logic, to five further domains."),
        ("akusalā dhammā abhivaḍḍhanti, kusalā dhammā parihāyanti",
         "&ldquo;unskillful qualities grow, and skillful qualities "
         "decline&rdquo; &mdash; the shared test repeated across all six "
         "domains."),
        ("paccayā dullabhā, paccayā sulabhā",
         "&ldquo;requisites hard to come by, requisites easy to come "
         "by&rdquo; &mdash; the second factor added only for people, "
         "weighed against, and outweighed by, the ascetic goal."),
        ("sāmaññattho na paripūrati, sāmaññattho paripūrati",
         "&ldquo;the goal of the ascetic life is not being fully "
         "developed... is being fully developed&rdquo; &mdash; the third "
         "and decisive factor for people, overriding ease of requisites."),
        ("anapaloketvāpi pakkamitabbo",
         "&ldquo;should follow that person... even if they send you "
         "away&rdquo; &mdash; the discourse's strongest instruction, "
         "reserved for the one clearly beneficial kind of person."),
    ],
    text_intro=(
        "The discourse in full: six domains, each distinguished by a "
        "shared test, with people given a fuller three-factor analysis. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six domains announced"),
        ("p", "&sect;1", "an9.6:1.1-2.12"),
        ("h3", "People: a three-factor test"),
        ("p", "&sect;2", "an9.6:3.1-6.7"),
        ("h3", "Robes, almsfood, lodging, villages, countries: one test"),
        ("p", "&sect;3", "an9.6:7.1-11.10"),
    ],
    quiz=[
        {"q": "What six domains does Sāriputta teach the mendicants to "
              "distinguish two kinds of?",
         "opts": [
             "Robes, bowls, huts, rivers, mountains, and forests",
             "People, robes, almsfood, lodging, villages or towns, and "
             "countries",
             "The five aggregates plus consciousness",
             "Six kinds of meditation"],
         "correct": 1,
         "expl": "Each domain gets the same announce-explain-repeat "
                 "treatment."},
        {"q": "What single test decides which robes, almsfood, lodging, "
              "villages, or countries to use or frequent?",
         "opts": [
             "Their cost", "Whether unskillful qualities grow or skillful "
             "qualities grow in connection with them",
             "Their popularity", "Their distance from the monastery"],
         "correct": 1,
         "expl": "One growth test, applied identically to five of the six "
                 "domains."},
        {"q": "How does the test for people differ from the other five "
              "domains?",
         "opts": [
             "It doesn't differ at all",
             "It adds two further factors: ease of requisites, and "
             "whether the ascetic goal is being fully developed",
             "It uses an entirely unrelated test",
             "It is decided by seniority alone"],
         "correct": 1,
         "expl": "People alone get a fuller three-factor analysis."},
        {"q": "Between ease of requisites and the ascetic goal, which "
              "factor wins when they conflict?",
         "opts": [
             "Ease of requisites always wins",
             "The ascetic goal being fully developed always outweighs "
             "ease of requisites",
             "They are given equal weight",
             "Neither factor matters"],
         "correct": 1,
         "expl": "A mendicant should follow someone with hard-to-come-by "
                 "requisites if the goal is progressing, and leave someone "
                 "with easy requisites if it isn't."},
        {"q": "What is the discourse's strongest instruction, and for "
              "whom?",
         "opts": [
             "Leave everyone eventually",
             "Follow the one clearly beneficial kind of person and don't "
             "leave them, even if they send you away",
             "Never associate with anyone",
             "Follow only senior mendicants"],
         "correct": 1,
         "expl": "Reserved for the person combining all four favorable "
                 "conditions."},
        {"q": "Who teaches this discourse?",
         "opts": [
             "The Buddha", "Venerable Sāriputta",
             "Venerable Ānanda", "Venerable Nandaka"],
         "correct": 1,
         "expl": "One of the discourses in this nipāta given by a chief "
                 "disciple rather than the Buddha himself."},
    ],
    marginalia=[
        ("Six domains, one refrain", [
            "people, robes, food,",
            "lodging, village, country &mdash;",
            "&ldquo;this is why I said it&rdquo;",
        ]),
        ("People: a fuller test", [
            "growth of skill, ease",
            "of requisites, and the goal &mdash;",
            "the goal outweighs ease",
        ]),
        ("Follow, even sent away", [
            "when the goal is met",
            "and skill is growing &mdash;",
            "don't leave, whatever comes",
        ]),
        ("Cross-references", [
            "AN 9.5 &middot; previous, Powers",
            "AN 9.7 &middot; next, With Sutavā the Wanderer",
        ]),
    ],
    further=[
        '<a href="%s/an9.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.5.html">AN 9.5 &middot; Powers</a> &mdash; previous.',
        '<a href="an-9.7.html">AN 9.7 &middot; With Sutavā the Wanderer</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.7 — Sutavāsutta
# --------------------------------------------------------------------------- #
page(
    7, "Sutavā", "With Sutavā the Wanderer",
    vagga=VAGGA_1,
    meta_title="AN 9.7 — With Sutavā the Wanderer | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sutavāsutta, in which a wanderer confirms five things a "
        "perfected mendicant can't transgress, and the Buddha expands the "
        "list to nine. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain"),
        ("Speakers", "The wanderer Sutavā and the Buddha"),
        ("Form", "A wanderer recalls an earlier teaching in full, the "
                 "Buddha confirms it, then expands five items to nine"),
        ("Length", "~2 minutes to read"),
        ("Five confirmed, nine given", "Sutavā's memory of five items is "
         "verified as correct as far as it goes; the Buddha then adds four "
         "more the wanderer hadn't heard"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "close companion to AN 9.8, worth comparing item "
                       "by item"),
    ],
    why=(
        "The wanderer Sutavā recites back five things he once heard the "
        "Buddha say a mendicant with defilements ended can't transgress "
        "&mdash; killing, stealing, sex, lying, and hoarding &mdash; and "
        "the Buddha confirms he heard correctly, then says that in truth "
        "there are nine, adding four kinds of prejudiced decision a "
        "perfected mendicant likewise can't make."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who is perfected can't transgress in nine "
            "respects: the five Sutavā already knew &mdash; killing a "
            "living creature, stealing, sex, deliberate lying, and "
            "hoarding goods for personal enjoyment &mdash; plus four more, "
            "deciding out of favoritism, hostility, stupidity, or "
            "cowardice."]),
        ("A memory, verified rather than corrected", [
            "Sutavā doesn't ask a new question; he recites, word for "
            "word, a teaching he recalls hearing at this very location on "
            "an earlier occasion, and asks whether he heard, learned, and "
            "remembered it properly. The Buddha's answer is unambiguous "
            "confirmation, not correction: &ldquo;indeed, Sutavā, you "
            "properly heard.&rdquo;"]),
        ("Five becomes nine", [
            "Having confirmed the five, the Buddha states that &ldquo;in "
            "the past, as today,&rdquo; he has always taught nine: the "
            "same five behavioral prohibitions, plus four further ones "
            "concerning how a perfected mendicant makes decisions "
            "&mdash; never out of favoritism, hostility, stupidity, or "
            "cowardice."]),
        ("A companion discourse follows", [
            "AN 9.8, immediately next, repeats this exact frame with a "
            "different wanderer &mdash; but the four items added to reach "
            "nine are not the same. Read together, the pair shows that "
            "this expansion formula (five confirmed, four more added) is "
            "a template the source fills in two different ways."]),
    ],
    terms=[
        ("khīṇāsavo bhikkhu pañca ṭhānāni nābhabbo ajjhācarituṁ",
         "&ldquo;a mendicant with defilements ended can't transgress in "
         "five respects&rdquo; &mdash; what Sutavā recalls hearing "
         "before, verified word for word."),
        ("sannidhiṁ pi kātuṁ yathā pubbe gihibhūtassa",
         "&ldquo;store up goods for their own enjoyment like they did as "
         "a layperson&rdquo; &mdash; the fifth of the original five, "
         "prohibiting a return to lay-style hoarding."),
        ("chandāgatiṁ, dosāgatiṁ, mohāgatiṁ, bhayāgatiṁ",
         "&ldquo;favoritism, hostility, stupidity, and cowardice&rdquo; "
         "&mdash; the four wrong courses named here as the additional "
         "four, a standard tetrad found elsewhere describing biased "
         "decision-making."),
        ("bhūtapubbāhaṁ... etarahipi",
         "&ldquo;in the past, as today&rdquo; &mdash; the Buddha's own "
         "framing, insisting the nine-item teaching is not new, only "
         "fuller than what Sutavā happened to hear before."),
        ("nava ṭhānāni nābhabbo ajjhācarituṁ",
         "&ldquo;can't transgress in these nine respects&rdquo; &mdash; "
         "the discourse's closing formula, naming the expanded count."),
    ],
    text_intro=(
        "The discourse in full: a wanderer's recollection confirmed, then "
        "expanded from five items to nine. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "A memory, recited and confirmed"),
        ("p", "&sect;1", "an9.7:1.1-3.2"),
        ("h3", "Five becomes nine"),
        ("p", "&sect;2", "an9.7:3.3-3.6"),
    ],
    quiz=[
        {"q": "What does the wanderer Sutavā do at the start of this "
              "discourse?",
         "opts": [
             "He challenges the Buddha with a new question",
             "He recites, word for word, a five-item teaching he recalls "
             "hearing before and asks if he remembered it correctly",
             "He accuses a mendicant of an offense",
             "He asks to ordain"],
         "correct": 1,
         "expl": "A memory verified, not a new inquiry."},
        {"q": "What are the original five things a perfected mendicant "
              "can't transgress?",
         "opts": [
             "The five precepts as taught to laypeople",
             "Killing a living creature, stealing, sex, deliberate lying, "
             "and hoarding goods for personal enjoyment",
             "The five hindrances",
             "The five aggregates"],
         "correct": 1,
         "expl": "The five Sutavā already knew, confirmed correct as far "
                 "as they go."},
        {"q": "What four items does the Buddha add to reach nine?",
         "opts": [
             "Four more precepts identical in kind to the first five",
             "Deciding out of favoritism, hostility, stupidity, or "
             "cowardice",
             "Four kinds of wrong speech",
             "Four kinds of wrong livelihood"],
         "correct": 1,
         "expl": "Biased decision-making, a different category from the "
                 "first five behavioral prohibitions."},
        {"q": "How does the Buddha frame the expansion from five to nine?",
         "opts": [
             "As a correction of what Sutavā heard wrong",
             "As what he has always taught, &ldquo;in the past, as "
             "today&rdquo; &mdash; fuller than what Sutavā happened to "
             "hear before",
             "As a brand-new teaching never given before",
             "As optional, for advanced mendicants only"],
         "correct": 1,
         "expl": "Confirmation of the five, not correction, plus more "
                 "that Sutavā simply hadn't heard."},
        {"q": "According to the guide, what does the companion discourse "
              "AN 9.8 show when read alongside this one?",
         "opts": [
             "That the two discourses are identical in every respect",
             "That the five-confirmed-four-added template is filled in "
             "two different ways, with different additional four items",
             "That AN 9.8 contradicts this discourse",
             "That AN 9.7 is a later addition"],
         "correct": 1,
         "expl": "Same frame, same first five, different second four."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, on Vulture's Peak Mountain",
             "Cālikā, on the Cālikā mountain", "Vesālī"],
         "correct": 1,
         "expl": "The setting shared with its companion discourse, AN "
                 "9.8, immediately next."},
    ],
    marginalia=[
        ("A memory, confirmed", [
            "five things recalled &mdash;",
            "&ldquo;indeed, you properly",
            "heard,&rdquo; the Buddha says",
        ]),
        ("Five becomes nine", [
            "kill, steal, sex, lie,",
            "hoard &mdash; plus favoritism,",
            "hostility, folly, fear",
        ]),
        ("A template, filled in twice", [
            "the same five confirmed,",
            "but the added four differ &mdash;",
            "see AN 9.8 next",
        ]),
        ("Cross-references", [
            "AN 9.6 &middot; previous, Association",
            "AN 9.8 &middot; next, With the Wanderer Sajjha, the same "
            "template with a different four",
        ]),
    ],
    further=[
        '<a href="%s/an9.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.6.html">AN 9.6 &middot; Association</a> &mdash; previous.',
        '<a href="an-9.8.html">AN 9.8 &middot; With the Wanderer Sajjha</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.8 — Sajjhasutta
# --------------------------------------------------------------------------- #
page(
    8, "Sajjha", "With the Wanderer Sajjha",
    vagga=VAGGA_1,
    meta_title="AN 9.8 — With the Wanderer Sajjha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sajjhasutta, the near-twin of AN 9.7 — a different wanderer, the "
        "same five confirmed, but a different four added to reach nine. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain"),
        ("Speakers", "The wanderer Sajjha and the Buddha"),
        ("Form", "The same frame as AN 9.7, word for word, until the "
                 "final four items"),
        ("Length", "~2 minutes to read"),
        ("The trap this pair sets", "Read quickly, this discourse looks "
         "identical to AN 9.7; read closely, the four items added to "
         "reach nine are entirely different"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, "
                       "but easy to misread as a plain repeat of AN 9.7"),
    ],
    why=(
        "A different wanderer, Sajjha, recites back the identical five "
        "things a perfected mendicant can't transgress that Sutavā "
        "recited at AN 9.7, and the Buddha confirms them exactly as "
        "before &mdash; but this time expands to nine with four items "
        "that have nothing to do with biased decision-making: a "
        "perfected mendicant can't abandon the Buddha, the teaching, the "
        "Saṅgha, or the training."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who is perfected can't transgress in nine "
            "respects: the same five Sajjha already knew &mdash; "
            "killing, stealing, sex, lying, and hoarding &mdash; plus "
            "four more, abandoning the Buddha, the teaching, the Saṅgha, "
            "or the training."]),
        ("The same opening as AN 9.7, almost word for word", [
            "Down to the setting, the wanderer's phrasing, and the "
            "Buddha's reply, this discourse repeats AN 9.7 closely enough "
            "that a reader moving quickly could mistake it for the same "
            "discourse twice. Only the wanderer's name, Sajjha rather "
            "than Sutavā, signals a different occasion."]),
        ("Where it actually differs", [
            "The four items that expand five to nine are not the "
            "favoritism, hostility, stupidity, and cowardice of AN 9.7. "
            "Here they are refusals of a different kind entirely: a "
            "perfected mendicant cannot abandon the Buddha as teacher, "
            "the Dhamma as teaching, the Saṅgha as community, or the "
            "training itself &mdash; loyalty to the triple gem and its "
            "discipline, not freedom from bias."]),
        ("Why this pairing matters for reading the collection", [
            "Two wanderers, two near-identical dialogues, two different "
            "sets of four &mdash; this is the same &ldquo;same frame, "
            "different content&rdquo; pattern that recurs throughout this "
            "collection. The shared opening is not a scribal accident to "
            "smooth over; it is exactly what makes the difference in the "
            "closing four worth noticing."]),
    ],
    terms=[
        ("khīṇāsavo bhikkhu pañca ṭhānāni nābhabbo ajjhācarituṁ",
         "&ldquo;a mendicant with defilements ended can't transgress in "
         "five respects&rdquo; &mdash; the same formula Sajjha recites, "
         "identical to Sutavā's at AN 9.7."),
        ("buddhaṁ pi nābhabbo pajahituṁ",
         "&ldquo;can't abandon the Buddha&rdquo; &mdash; the first of "
         "this discourse's own additional four, distinct from AN 9.7's "
         "additional four."),
        ("dhammaṁ pi nābhabbo pajahituṁ",
         "&ldquo;can't abandon the teaching&rdquo; &mdash; the second "
         "addition, naming the Dhamma specifically."),
        ("saṅghaṁ pi nābhabbo pajahituṁ",
         "&ldquo;can't abandon the Saṅgha&rdquo; &mdash; the third "
         "addition, naming the community."),
        ("sikkhaṁ pi nābhabbo pajahituṁ",
         "&ldquo;can't abandon the training&rdquo; &mdash; the fourth and "
         "final addition, closing this discourse's own nine."),
    ],
    text_intro=(
        "The discourse in full: the same opening as AN 9.7, but a "
        "different four items closing the count at nine. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The same opening as AN 9.7"),
        ("p", "&sect;1", "an9.8:1.1-3.2"),
        ("h3", "Five becomes nine — a different four"),
        ("p", "&sect;2", "an9.8:3.3-3.6"),
    ],
    quiz=[
        {"q": "How does this discourse's opening compare to AN 9.7's?",
         "opts": [
             "Entirely unrelated",
             "The same frame almost word for word, differing chiefly in "
             "the wanderer's name (Sajjha rather than Sutavā)",
             "Set in a different location entirely",
             "Spoken by a different teacher"],
         "correct": 1,
         "expl": "Close enough to be mistaken for a repeat, until the "
                 "closing four."},
        {"q": "What are the original five items both wanderers recite?",
         "opts": [
             "The five hindrances",
             "Killing a living creature, stealing, sex, deliberate lying, "
             "and hoarding goods for personal enjoyment",
             "The five aggregates",
             "Five kinds of wrong speech"],
         "correct": 1,
         "expl": "Identical to AN 9.7's original five."},
        {"q": "What four items does the Buddha add here to reach nine?",
         "opts": [
             "Favoritism, hostility, stupidity, and cowardice",
             "Can't abandon the Buddha, the teaching, the Saṅgha, or the "
             "training",
             "Four more behavioral prohibitions identical to the first "
             "five",
             "Four kinds of wrong livelihood"],
         "correct": 1,
         "expl": "A different four from AN 9.7's biased-decision items — "
                 "loyalty to the triple gem instead."},
        {"q": "According to the guide, what is the point of this "
              "discourse's close resemblance to AN 9.7?",
         "opts": [
             "It is a scribal duplication to be smoothed over",
             "The shared opening is exactly what makes the different "
             "closing four worth noticing — a same-frame, different-"
             "content pattern recurring throughout the collection",
             "It proves one of the two discourses is spurious",
             "It has no significance"],
         "correct": 1,
         "expl": "The resemblance sets up the difference, rather than "
                 "erasing it."},
        {"q": "What single word in the opening actually signals a "
              "different occasion from AN 9.7?",
         "opts": [
             "The location",
             "The wanderer's name, Sajjha rather than Sutavā",
             "The time of day", "The number of mendicants present"],
         "correct": 1,
         "expl": "Everything else in the frame is shared."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, on Vulture's Peak Mountain",
             "Cālikā, on the Cālikā mountain", "Vesālī"],
         "correct": 1,
         "expl": "The same setting as its companion, AN 9.7."},
    ],
    marginalia=[
        ("The same opening, a new name", [
            "Sajjha, not Sutavā &mdash;",
            "otherwise word for word",
            "the same as AN 9.7",
        ]),
        ("Five becomes nine, differently", [
            "not bias this time, but",
            "Buddha, teaching, Saṅgha,",
            "training &mdash; never abandoned",
        ]),
        ("A pattern worth noticing", [
            "same frame, twice told,",
            "different content each time &mdash;",
            "read the pair together",
        ]),
        ("Cross-references", [
            "AN 9.7 &middot; previous, With Sutavā the Wanderer, the same "
            "template with a different four",
            "AN 9.9 &middot; next, Individuals",
        ]),
    ],
    further=[
        '<a href="%s/an9.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.7.html">AN 9.7 &middot; With Sutavā the Wanderer</a> &mdash; previous, '
        "the same template with a different four.",
        '<a href="an-9.9.html">AN 9.9 &middot; Individuals</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.9 — Puggalasutta
# --------------------------------------------------------------------------- #
page(
    9, "Puggala", "Individuals",
    vagga=VAGGA_1,
    meta_title="AN 9.9 — Individuals | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Puggalasutta, a bare nine-item classification of individuals "
        "found in the world — four pairs on the path to and fruit of "
        "awakening, plus the ordinary person. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list, no narrative and no similes"),
        ("Length", "~30 seconds to read"),
        ("Nine, not the usual eight", "The more familiar four-pairs "
         "formula names eight noble individuals; this discourse adds a "
         "ninth, the ordinary person, to reach nine"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the "
                       "shortest form in this chapter, a single "
                       "classification list"),
    ],
    why=(
        "Nine individuals are found in the world: four pairs, each "
        "naming someone who has realized a fruit of awakening and someone "
        "practicing to realize it &mdash; the perfected one, the non-"
        "returner, the once-returner, and the stream-enterer, each paired "
        "with the one still practicing for that fruit &mdash; plus, as a "
        "ninth, the ordinary person."),
    guide=[
        ("The teaching in one sentence", [
            "Nine individuals are found in the world: the perfected one "
            "and the one practicing for perfection, the non-returner and "
            "the one practicing to realize non-return, the once-returner "
            "and the one practicing to realize once-return, the stream-"
            "enterer and the one practicing to realize stream-entry, and "
            "the ordinary person."]),
        ("Eight familiar names, one familiar structure", [
            "The first eight names are the same four pairs that make up "
            "the well-known &ldquo;four pairs of persons, eight "
            "individuals&rdquo; formula describing the noble Saṅgha "
            "elsewhere in the canon: each of the four fruits &mdash; "
            "stream-entry, once-return, non-return, and perfection "
            "&mdash; paired with the practice that leads to it."]),
        ("A ninth added to reach nine", [
            "What makes this a discourse of the Nines rather than a "
            "restatement of the familiar eightfold formula is its ninth "
            "member: the ordinary person, <em>puthujjana</em>, someone "
            "who has not yet entered any of the four paths at all. Adding "
            "this ninth item is what lets the discourse belong to this "
            "nipāta's numerical scheme."]),
        ("A companion discourse follows immediately", [
            "AN 9.10, next, restates this same nine-item list almost "
            "exactly &mdash; but replaces the ordinary person with a "
            "different ninth member and reframes the whole list around "
            "worthiness of offerings, rather than simply being "
            "&ldquo;found in the world.&rdquo;"]),
    ],
    terms=[
        ("nava puggalā santo saṁvijjamānā lokasmiṁ",
         "&ldquo;these nine individuals are found in the world&rdquo; "
         "&mdash; the discourse's own bare framing, naming existence "
         "rather than worthiness."),
        ("arahā, arahattāya paṭipanno",
         "&ldquo;the perfected one and the one practicing for "
         "perfection&rdquo; &mdash; the first pair, naming the fruit and "
         "its path together."),
        ("anāgāmī, anāgāmiphalasacchikiriyāya paṭipanno",
         "&ldquo;the non-returner and the one practicing to realize the "
         "fruit of non-return&rdquo; &mdash; the second pair."),
        ("sotāpanno, sotāpattiphalasacchikiriyāya paṭipanno",
         "&ldquo;the stream-enterer and the one practicing to realize "
         "the fruit of stream-entry&rdquo; &mdash; the fourth pair, the "
         "entry point of the noble path."),
        ("puthujjano",
         "&ldquo;the ordinary person&rdquo; &mdash; the ninth member "
         "added here to the familiar eight, someone who has not yet "
         "entered any of the four paths."),
    ],
    text_intro=(
        "The discourse in full: nine individuals found in the world. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine individuals"),
        ("p", "&sect;1", "an9.9:1.1-1.4"),
    ],
    quiz=[
        {"q": "What are the nine individuals this discourse names?",
         "opts": [
             "Nine kinds of meditation teacher",
             "Four pairs on the path to and fruit of awakening (perfected "
             "one, non-returner, once-returner, stream-enterer, each "
             "paired with the one practicing toward it), plus the "
             "ordinary person",
             "Nine monastic ranks",
             "Nine kinds of layperson"],
         "correct": 1,
         "expl": "Eight familiar names plus one ninth to reach nine."},
        {"q": "What well-known formula do the first eight names belong "
              "to?",
         "opts": [
             "The five aggregates",
             "The &ldquo;four pairs of persons, eight individuals&rdquo; "
             "formula describing the noble Saṅgha",
             "The four right efforts",
             "The eight liberations"],
         "correct": 1,
         "expl": "Each of the four fruits paired with its path."},
        {"q": "What ninth member does this discourse add to reach nine?",
         "opts": [
             "A second perfected one",
             "The ordinary person, <em>puthujjana</em>",
             "A deity", "A wanderer of another religion"],
         "correct": 1,
         "expl": "Someone who has not yet entered any of the four paths."},
        {"q": "According to the guide, what does the companion discourse "
              "AN 9.10 change about this same list?",
         "opts": [
             "Nothing at all",
             "It replaces the ordinary person with a different ninth "
             "member and reframes the list around worthiness of "
             "offerings",
             "It removes the four pairs entirely",
             "It adds a tenth member"],
         "correct": 1,
         "expl": "Same eight, a different ninth, and a different "
                 "framing."},
        {"q": "How is this discourse's list framed?",
         "opts": [
             "As worthy of offerings and hospitality",
             "As simply &ldquo;found in the world&rdquo;",
             "As dangerous individuals to avoid",
             "As teachers to seek out"],
         "correct": 1,
         "expl": "A bare existence claim, not a worthiness claim."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "The shortest, barest form in this chapter."},
    ],
    marginalia=[
        ("Four pairs, familiar", [
            "perfected, non-returner,",
            "once-returner, stream-enterer &mdash;",
            "each paired with its path",
        ]),
        ("A ninth, to reach nine", [
            "the ordinary person",
            "added to the familiar eight &mdash;",
            "found in the world",
        ]),
        ("A companion discourse next", [
            "same eight, new ninth,",
            "worthy of offerings now &mdash;",
            "see AN 9.10",
        ]),
        ("Cross-references", [
            "AN 9.8 &middot; previous, With the Wanderer Sajjha",
            "AN 9.10 &middot; next, the same list reframed, closing this "
            "chapter",
        ]),
    ],
    further=[
        '<a href="%s/an9.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.8.html">AN 9.8 &middot; With the Wanderer Sajjha</a> &mdash; previous.',
        '<a href="an-9.10.html">AN 9.10 &middot; Worthy of Offerings Dedicated to the '
        "Gods</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.10 — Āhuneyyasutta — closes ch.1 Sambodhivagga
# --------------------------------------------------------------------------- #
page(
    10, "Āhuneyya", "Worthy of Offerings Dedicated to the Gods",
    vagga=VAGGA_1,
    meta_title=("AN 9.10 — Worthy of Offerings Dedicated to the Gods | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Āhuneyyasutta, closing this chapter with the same nine-item "
        "classification as AN 9.9, its ninth member replaced and reframed "
        "around worthiness of offerings. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same bare list as AN 9.9, with one member swapped "
                 "and a worthiness formula wrapped around it"),
        ("Length", "~30 seconds to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Sambodhivagga</em>, the first chapter of the Nines; "
         "the source's own untranslated closing verse names all ten "
         "discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "but easy to conflate with AN 9.9 without close "
                       "reading"),
    ],
    why=(
        "The same eight familiar names from AN 9.9 recur &mdash; the "
        "perfected one and the one practicing for perfection, the non-"
        "returner, the once-returner, and the stream-enterer, each "
        "paired with the one practicing toward that fruit &mdash; but the "
        "ninth member changes from the ordinary person to "
        "<em>gotrabhū</em>, and the whole list is now framed as worthy of "
        "offerings, hospitality, donations, and greeting, the supreme "
        "field of merit for the world."),
    guide=[
        ("The teaching in one sentence", [
            "Nine individuals are worthy of offerings dedicated to the "
            "gods, worthy of hospitality, worthy of a religious "
            "donation, worthy of greeting with cupped palms, and are the "
            "supreme field of merit for the world: the same four pairs "
            "as AN 9.9, plus <em>gotrabhū</em>, rendered here as "
            "&ldquo;a lamb of the flock,&rdquo; in place of the ordinary "
            "person."]),
        ("Same eight, a different ninth", [
            "This discourse repeats AN 9.9's four pairs exactly &mdash; "
            "perfected one, non-returner, once-returner, stream-enterer, "
            "each with the one practicing toward that fruit. Only the "
            "ninth member changes: not the ordinary person outright, but "
            "<em>gotrabhū</em>, one who stands at the very threshold of "
            "the noble path without having formally entered it."]),
        ("A distinctive translation choice", [
            "Sujato's English renders <em>gotrabhū</em> &mdash; literally "
            "someone who has &ldquo;become of the lineage&rdquo; of the "
            "noble ones &mdash; as &ldquo;a lamb of the flock,&rdquo; an "
            "idiomatic image of belonging to the fold rather than a "
            "literal translation of the Pāli term. It names someone "
            "closer to entering the path than the plain ordinary person "
            "of AN 9.9, without yet being a stream-enterer."]),
        ("Worthiness, and the chapter's own close", [
            "Where AN 9.9 simply says these nine are &ldquo;found in the "
            "world,&rdquo; this discourse wraps the list in the familiar "
            "worthy-of-offerings formula met repeatedly elsewhere in this "
            "project, naming the field of merit these nine represent for "
            "the world. With this discourse, <em>Sambodhivagga</em>, the "
            "first chapter of the Nines, closes; the source's own "
            "untranslated closing verse lists all ten discourses of the "
            "chapter by their opening words."]),
    ],
    terms=[
        ("āhuneyyā pāhuneyyā dakkhiṇeyyā añjalikaraṇīyā",
         "&ldquo;worthy of offerings dedicated to the gods, worthy of "
         "hospitality, worthy of a religious donation, worthy of "
         "greeting with cupped palms&rdquo; &mdash; the worthiness "
         "formula wrapped around this discourse's nine, distinguishing "
         "it from AN 9.9's bare framing."),
        ("anuttaraṁ puññakkhettaṁ lokassa",
         "&ldquo;the supreme field of merit for the world&rdquo; &mdash; "
         "the formula's closing phrase, naming what these nine represent "
         "for those who support them."),
        ("gotrabhū",
         "literally &ldquo;become of the lineage&rdquo; &mdash; this "
         "discourse's own ninth member, rendered here as &ldquo;a lamb "
         "of the flock,&rdquo; replacing AN 9.9's plain ordinary person."),
        ("puthujjano",
         "&ldquo;the ordinary person&rdquo; &mdash; AN 9.9's ninth "
         "member, absent here and replaced by <em>gotrabhū</em>."),
        ("sambodhivaggo paṭhamo",
         "&ldquo;the first chapter, Sambodhivagga, is finished&rdquo; "
         "&mdash; the source's own untranslated colophon closing this "
         "chapter, followed by an uddāna verse naming all ten discourses."),
    ],
    text_intro=(
        "The discourse in full: the same nine-item classification as AN "
        "9.9, its ninth member replaced and wrapped in the worthy-of-"
        "offerings formula. The source's own closing colophon and "
        "chapter-summary verse are untranslated in the English and are "
        "described rather than quoted here. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine worthy of offerings"),
        ("p", "&sect;1", "an9.10:1.1-1.4"),
    ],
    quiz=[
        {"q": "How do this discourse's nine individuals compare to AN "
              "9.9's?",
         "opts": [
             "Entirely different", "The same four pairs, with a different "
             "ninth member and a worthiness formula wrapped around the "
             "whole list",
             "Only the first pair is the same",
             "This discourse names ten individuals"],
         "correct": 1,
         "expl": "Same eight, one substitution, and a new frame."},
        {"q": "What ninth member replaces AN 9.9's ordinary person here?",
         "opts": [
             "A second perfected one",
             "<em>Gotrabhū</em>, rendered &ldquo;a lamb of the "
             "flock&rdquo;, one at the threshold of the noble path",
             "A wanderer of another religion",
             "A deity"],
         "correct": 1,
         "expl": "Closer to entering the path than a plain ordinary "
                 "person, without yet being a stream-enterer."},
        {"q": "How is this discourse's list framed, unlike AN 9.9's?",
         "opts": [
             "As simply &ldquo;found in the world&rdquo;",
             "As worthy of offerings, hospitality, donations, and "
             "greeting — the supreme field of merit for the world",
             "As dangerous and to be avoided",
             "As teachers of false doctrine"],
         "correct": 1,
         "expl": "The familiar worthy-of-offerings formula, met "
                 "repeatedly elsewhere in this project."},
        {"q": "What does this discourse close, and how does its own "
              "closing verse describe that?",
         "opts": [
             "Nothing; the chapter continues past it",
             "It closes <em>Sambodhivagga</em>, the first chapter, with "
             "an untranslated colophon and an uddāna verse naming all ten "
             "discourses by their opening words",
             "It closes the entire nipāta",
             "It closes only this discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "What English phrase does Sujato use for <em>gotrabhū</em>, "
              "and how literal is it?",
         "opts": [
             "&ldquo;Stream-enterer,&rdquo; a literal rendering",
             "&ldquo;A lamb of the flock,&rdquo; an idiomatic image "
             "rather than a literal translation of &ldquo;become of the "
             "lineage&rdquo;",
             "&ldquo;The awakened one,&rdquo; a literal rendering",
             "&ldquo;The novice,&rdquo; a literal rendering"],
         "correct": 1,
         "expl": "A distinctive, idiomatic translation choice worth "
                 "noting."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 9.9 immediately before it."},
    ],
    marginalia=[
        ("Same eight, a new ninth", [
            "perfected, non-returner,",
            "once-, stream-enterer &mdash;",
            "and a lamb of the flock",
        ]),
        ("Worthy of offerings", [
            "hospitality, donation,",
            "greeting with cupped palms &mdash;",
            "the field of merit",
        ]),
        ("Closing the first chapter", [
            "Sambodhivaggo",
            "paṭhamo, finished &mdash;",
            "ten discourses named",
        ]),
        ("Cross-references", [
            "AN 9.9 &middot; previous, the same list before its ninth "
            "member changes",
            "AN 9.11 &middot; next, opening ch.2, Sīhanādavagga",
        ]),
    ],
    further=[
        '<a href="%s/an9.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.9.html">AN 9.9 &middot; Individuals</a> &mdash; previous, the same '
        "list before its ninth member changes.",
    ],
)


# --------------------------------------------------------------------------- #
# ch.2 — Sīhanādavagga (AN 9.11-20). AN 9.20 itself was published before this
# series began working in order, in the earlier eighteen-page selection; it
# closes this chapter and is listed by INDEX_EXTRA rather than regenerated
# here. AN 9.19's page splices in with an explicit next= kwarg per the
# an-6.16/an-6.63/an-7.6/an-8.30/an-8.53 precedent, and an-9.20.html itself
# gets its prev link hand-edited once this chapter is built.
# --------------------------------------------------------------------------- #
VAGGA_2 = "<em>Sīhanādavagga</em> &mdash; the second chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.11 — Sāriputtasīhanādasutta
# --------------------------------------------------------------------------- #
page(
    11, "Sāriputtasīhanāda", "Sāriputta&rsquo;s Lion&rsquo;s Roar",
    vagga=VAGGA_2,
    meta_title="AN 9.11 — Sāriputta's Lion's Roar | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Sāriputta's Lion's Roar, opening this chapter with a false "
        "accusation and Sāriputta's own answer: ten similes on a heart "
        "like the earth, water, fire, wind, and more, free of enmity even "
        "when struck. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "A complaining mendicant, the Buddha, and Venerable "
                     "Sāriputta, summoned to answer the charge in the "
                     "Buddha's presence"),
        ("Form", "A narrative accusation, then ten similes answering it, "
                 "then the accuser's confession and Sāriputta's own "
                 "condition for forgiveness"),
        ("Length", "~6 minutes to read"),
        ("Chapter's namesake", "This discourse gives its own name to the "
                               "chapter, <em>Sīhanādavagga</em>, the "
                               "Chapter on the Lion's Roar"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a long "
                       "narrative with ten cumulative similes, worth "
                       "reading in full"),
    ],
    why=(
        "A mendicant falsely accuses Sāriputta, just departed for the "
        "countryside, of attacking him and leaving without apology; "
        "summoned back and told of the complaint, Sāriputta answers not "
        "with denial but with ten similes &mdash; a heart like the earth, "
        "water, fire, wind, a rag, a humble outcaste child, a gentle "
        "gelded bull &mdash; each showing that someone who had not "
        "established mindfulness of the body might well act this way, "
        "but he himself lives free of enmity and ill will."),
    guide=[
        ("The teaching in one sentence", [
            "Someone who had not established mindfulness of the body "
            "might well attack a companion and leave without apology, but "
            "Sāriputta lives with a heart like the earth, water, fire, "
            "wind, and a rag &mdash; unmoved whether clean or unclean "
            "things are thrown upon it &mdash; abundant, expansive, "
            "limitless, free of enmity and ill will."]),
        ("A false accusation, and a dramatic summons", [
            "The complaint is laid the moment Sāriputta has left for the "
            "countryside; the Buddha's terse instruction &mdash; "
            "&ldquo;the teacher summons him&rdquo; &mdash; and "
            "Moggallāna and Ānanda going from dwelling to dwelling "
            "calling the mendicants to come hear &ldquo;Sāriputta roar his "
            "lion's roar&rdquo; build real anticipation before Sāriputta "
            "has said a single word in his own defense."]),
        ("Ten similes, one repeated refrain", [
            "Rather than deny the accusation outright, Sāriputta answers "
            "with escalating images of imperturbability &mdash; earth, "
            "water, fire, wind, and a rag, each unmoved by both clean and "
            "unclean things; a humble outcaste child entering town; a "
            "gentle gelded bull harming no one; and, turning inward, his "
            "own disgust at his &ldquo;leaking and oozing&rdquo; body "
            "&mdash; each closed by the same refrain: someone without "
            "mindfulness of the body might well do this, but not him."]),
        ("A confession, and a condition for forgiveness", [
            "The accusing mendicant, moved by Sāriputta's answer, "
            "confesses his claim was &ldquo;incorrect, hollow, false, "
            "untruthful,&rdquo; and the Buddha warns his head will "
            "explode into seven pieces unless Sāriputta forgives him. "
            "Sāriputta's reply is neither refusal nor automatic pardon: he "
            "will forgive if the mendicant himself asks to be forgiven in "
            "turn &mdash; reconciliation offered, not simply granted."]),
    ],
    terms=[
        ("sīhanādaṁ nadatu",
         "&ldquo;roar his lion's roar&rdquo; &mdash; Moggallāna and "
         "Ānanda's own summons, giving this discourse and its chapter "
         "their name."),
        ("kāyagatāsati anupaṭṭhitā",
         "&ldquo;mindfulness of the body not established&rdquo; &mdash; "
         "the discourse's own refrain, naming what someone lacking "
         "might well do."),
        ("pathavisamena cetasā",
         "&ldquo;with a heart like the earth&rdquo; &mdash; the first of "
         "ten similes, unmoved whether clean or unclean things are "
         "thrown upon it."),
        ("caṇḍālakumārakena vā caṇḍālakumārikāya vā",
         "&ldquo;a boy or girl of a corpse-worker tribe&rdquo; &mdash; "
         "one of the ten similes, entering town with a humble mind, "
         "holding a pot and clad in rags."),
        ("sattadhā tassa muddhā phalatu",
         "&ldquo;his head will explode into seven pieces&rdquo; &mdash; "
         "the Buddha's warning to the accusing mendicant unless "
         "Sāriputta forgives him."),
    ],
    text_intro=(
        "The discourse in full: a false accusation, a dramatic summons, "
        "ten similes, and a confession answered with a condition for "
        "forgiveness. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A false accusation, and a summons"),
        ("p", "&sect;1", "an9.11:1.1-2.6"),
        ("h3", "Ten similes"),
        ("p", "&sect;2", "an9.11:3.1-4.3"),
        ("p", "&sect;3", "an9.11:5.1-5.3"),
        ("p", "&sect;4", "an9.11:6.1-6.3"),
        ("p", "&sect;5", "an9.11:7.1-7.3"),
        ("p", "&sect;6", "an9.11:8.1-8.3"),
        ("p", "&sect;7", "an9.11:9.1-9.3"),
        ("p", "&sect;8", "an9.11:10.1-10.3"),
        ("p", "&sect;9", "an9.11:11.1-11.3"),
        ("p", "&sect;10", "an9.11:12.1-12.3"),
        ("h3", "A confession, and a condition for forgiveness"),
        ("p", "&sect;11", "an9.11:13.1-14.4"),
    ],
    quiz=[
        {"q": "What complaint is laid against Sāriputta, and when?",
         "opts": [
             "That he stole almsfood, laid while he was still present",
             "That he attacked a mendicant and left without apologizing, "
             "laid just after he departed for the countryside",
             "That he broke a monastic rule about robes",
             "That he taught false doctrine"],
         "correct": 1,
         "expl": "The accusation prompts his dramatic summons back."},
        {"q": "How does Sāriputta answer the accusation?",
         "opts": [
             "By denying it outright and demanding proof",
             "With ten cumulative similes of imperturbability, each "
             "closing with the same refrain about mindfulness of the body",
             "By refusing to respond at all",
             "By accusing the mendicant in return"],
         "correct": 1,
         "expl": "Earth, water, fire, wind, a rag, and more, each unmoved "
                 "by clean or unclean things."},
        {"q": "What does the discourse's own refrain say about the "
              "accusation?",
         "opts": [
             "That it is certainly true",
             "That someone who had not established mindfulness of the "
             "body might well act this way — implying Sāriputta himself "
             "has",
             "That it is impossible for anyone to act this way",
             "That the Buddha alone can judge the matter"],
         "correct": 1,
         "expl": "A conditional, not a denial — establishing the standard "
                 "rather than simply asserting innocence."},
        {"q": "What does the accusing mendicant do once he hears "
              "Sāriputta's answer?",
         "opts": [
             "He storms off unconvinced",
             "He confesses his claim was incorrect, hollow, false, and "
             "untruthful, and asks forgiveness",
             "He challenges Sāriputta to a debate",
             "He leaves the monastic order"],
         "correct": 1,
         "expl": "A genuine confession, met by the Buddha's warning about "
                 "the consequences of an unforgiven wrong."},
        {"q": "On what condition does Sāriputta agree to forgive him?",
         "opts": [
             "Unconditionally, the moment the Buddha asks",
             "Only if the mendicant himself asks Sāriputta to pardon him "
             "in turn",
             "Never; he refuses to forgive",
             "Only after a period of monastic probation"],
         "correct": 1,
         "expl": "Reconciliation offered as an exchange, not simply "
                 "granted on request."},
        {"q": "What does this discourse lend to its chapter's name?",
         "opts": [
             "Nothing in particular", "Its own image, the &ldquo;lion's "
             "roar,&rdquo; naming <em>Sīhanādavagga</em>",
             "A place name", "A number"],
         "correct": 1,
         "expl": "Moggallāna and Ānanda's own summons gives the chapter "
                 "its name."},
    ],
    marginalia=[
        ("A false charge, a summons", [
            "&ldquo;the teacher summons him&rdquo; &mdash;",
            "&ldquo;come hear Sāriputta",
            "roar his lion's roar&rdquo;",
        ]),
        ("Ten similes of an unmoved heart", [
            "earth, water, fire, wind,",
            "a rag, a humble child,",
            "a gentle gelded bull",
        ]),
        ("Forgiveness, not automatic", [
            "&ldquo;I will pardon him",
            "if he asks me too&rdquo; &mdash;",
            "exchange, not simple grant",
        ]),
        ("Cross-references", [
            "AN 9.10 &middot; previous nipāta's chapter, closing "
            "Sambodhivagga",
            "AN 9.12 &middot; next, With Residue",
        ]),
    ],
    further=[
        '<a href="%s/an9.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.10.html">AN 9.10 &middot; Worthy of Offerings Dedicated to the '
        "Gods</a> &mdash; previous.",
        '<a href="an-9.12.html">AN 9.12 &middot; With Residue</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.12 — Sopādisesasutta
# --------------------------------------------------------------------------- #
page(
    12, "Sopādisesa", "With Residue",
    vagga=VAGGA_2,
    meta_title="AN 9.12 — With Residue | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sopādisesasutta, in which the Buddha corrects wanderers of other "
        "religions with a detailed nine-fold classification of stream-"
        "enterers, once-returners, and non-returners exempt from bad "
        "rebirth. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_SAVATTHI),
        ("Speakers", "Venerable Sāriputta and the Buddha"),
        ("Form", "A narrative frame — an overheard claim, deferred rather "
                 "than debated — then a detailed nine-fold classification"),
        ("Length", "~4 minutes to read"),
        ("Not the same nine as AN 9.9/9.10", "This nine-fold list is a "
         "far more granular breakdown of only three of the four noble "
         "fruits — non-return, once-return, and stream-entry — not the "
         "four-pairs-plus-one scheme met two discourses ago"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "technical classification worth reading slowly"),
    ],
    why=(
        "Overhearing wanderers of other religions claim that no-one who "
        "dies &lsquo;with residue&rsquo; escapes a bad rebirth, Sāriputta "
        "neither argues nor agrees but brings the question to the "
        "Buddha, who dismisses the wanderers as incompetent to judge such "
        "things and gives nine specific kinds of person who, dying with "
        "residue remaining, are exempt from hell, the animal realm, and "
        "the ghost realm."),
    guide=[
        ("The teaching in one sentence", [
            "Nine kinds of person, dying with residue still remaining, "
            "are exempt from a bad rebirth: five grades of non-returner, "
            "a once-returner, and three grades of stream-enterer, each "
            "defined by which fetters have ended and how much ethics, "
            "immersion, and wisdom have been fulfilled."]),
        ("Overheard, not argued", [
            "Sāriputta doesn't debate the wanderers' claim on the spot. "
            "He neither approves nor rejects it, quietly resolving "
            "instead to learn its truth from the Buddha himself &mdash; "
            "a model of restraint the discourse doesn't comment on "
            "directly but plainly commends by contrast with what follows."]),
        ("Five grades of non-returner, from one classification", [
            "The first five individuals are all non-returners, "
            "distinguished by how and when they attain final "
            "extinguishment after the five lower fetters end: between "
            "one life and the next, upon landing, without extra effort, "
            "with extra effort, or by heading upstream to the Akaniṭṭha "
            "realm &mdash; a finer subdivision of the same non-return "
            "already named as a single fruit at AN 9.9 and 9.10."]),
        ("A once-returner and three stream-enterers close the nine", [
            "The sixth individual is a once-returner. The final three are "
            "all stream-enterers, distinguished by how much further "
            "rebirth remains: a one-seeder reborn just once more, one who "
            "goes from family to family two or three times, and one with "
            "at most seven rebirths &mdash; and the Buddha adds that he "
            "has kept this detailed exposition largely unspoken, for fear "
            "listeners might grow negligent on hearing it."]),
    ],
    terms=[
        ("sopādiseso",
         "&ldquo;with residue&rdquo; &mdash; the discourse's own title "
         "term, meaning defilements not yet fully extinguished at death."),
        ("antarāparinibbāyī",
         "&ldquo;extinguished between one life and the next&rdquo; "
         "&mdash; the first of the five non-returner grades."),
        ("uddhaṁsoto akaniṭṭhagāmī",
         "&ldquo;heading upstream, going to the Akaniṭṭha realm&rdquo; "
         "&mdash; the fifth and most gradual of the non-returner grades."),
        ("ekabījī",
         "&ldquo;one-seeder&rdquo; &mdash; a stream-enterer reborn just "
         "one more time in a human existence before making an end of "
         "suffering."),
        ("na cāhaṁ, sāriputta, etāvatā aññāsiṁ pariyāyaṁ",
         "the Buddha's reason for rarely teaching this detailed "
         "exposition &mdash; not wanting listeners to grow negligent on "
         "hearing it, spoken here only to answer Sāriputta's question."),
    ],
    text_intro=(
        "The discourse in full: an overheard claim brought to the "
        "Buddha, and a detailed nine-fold classification of non-"
        "returners, a once-returner, and stream-enterers. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "An overheard claim, brought to the Buddha"),
        ("p", "&sect;1", "an9.12:1.1-2.6"),
        ("h3", "Nine individuals, exempt from bad rebirth"),
        ("p", "&sect;2", "an9.12:4.1-11.6"),
    ],
    quiz=[
        {"q": "What claim does Sāriputta overhear from wanderers of other "
              "religions?",
         "opts": [
             "That everyone who dies eventually attains awakening",
             "That no-one who dies with residue remaining is exempt from "
             "hell, the animal realm, or the ghost realm",
             "That rebirth doesn't exist",
             "That only monastics can be reborn well"],
         "correct": 1,
         "expl": "A claim Sāriputta neither approves nor rejects on the "
                 "spot."},
        {"q": "How does Sāriputta respond to the wanderers' claim in the "
              "moment?",
         "opts": [
             "He argues against it immediately",
             "He neither approves nor rejects it, and resolves to ask "
             "the Buddha instead",
             "He agrees with it publicly",
             "He reports them to the authorities"],
         "correct": 1,
         "expl": "Restraint, and deferring to the Buddha rather than "
                 "debating on the spot."},
        {"q": "What does the Buddha say about the wanderers' competence "
              "to judge this question?",
         "opts": [
             "That they are correct",
             "That they are foolish and incompetent to know whether "
             "someone has residue or not",
             "That the question is unanswerable",
             "That only Sāriputta can judge it"],
         "correct": 1,
         "expl": "A sharp dismissal before the Buddha gives his own "
                 "detailed answer."},
        {"q": "How does this nine-fold classification relate to the "
              "nine individuals at AN 9.9 and 9.10?",
         "opts": [
             "It is the identical list, restated",
             "It is a far more granular breakdown of only three of the "
             "four fruits — non-return, once-return, and stream-entry — "
             "not the four-pairs-plus-one scheme",
             "It replaces the earlier list entirely",
             "It adds the perfected one as a tenth grade"],
         "correct": 1,
         "expl": "A different, finer-grained nine, not a repeat of AN "
                 "9.9/9.10."},
        {"q": "Why does the Buddha say he has rarely taught this detailed "
              "exposition before?",
         "opts": [
             "It is a secret teaching for the ordained only",
             "He didn't want listeners to grow negligent on hearing it",
             "It had not yet been formulated",
             "It contradicts an earlier teaching"],
         "correct": 1,
         "expl": "Spoken here only because Sāriputta specifically asked."},
        {"q": "What closes the nine-fold list?",
         "opts": [
             "Five grades of non-returner only",
             "Five grades of non-returner, a once-returner, and three "
             "grades of stream-enterer",
             "Nine grades of stream-enterer",
             "The perfected one and eight lesser grades"],
         "correct": 1,
         "expl": "Three fruits, subdivided to nine individuals in total."},
    ],
    marginalia=[
        ("Overheard, not argued", [
            "neither approved",
            "nor rejected &mdash; Sāriputta",
            "asks the Buddha instead",
        ]),
        ("Five grades of non-return", [
            "between lives, on landing,",
            "with or without effort,",
            "or heading upstream",
        ]),
        ("A once-returner, three stream-enterers", [
            "one-seeder, family",
            "to family, seven rebirths",
            "at most &mdash; nine in all",
        ]),
        ("Cross-references", [
            "AN 9.9&ndash;10 &middot; a coarser four-pairs-plus-one "
            "classification, for comparison",
            "AN 9.11 &middot; previous, Sāriputta's Lion's Roar",
            "AN 9.13 &middot; next, With Koṭṭhita",
        ]),
    ],
    further=[
        '<a href="%s/an9.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.9.html">AN 9.9 &middot; Individuals</a> &mdash; a coarser '
        "classification, for comparison.",
        '<a href="an-9.11.html">AN 9.11 &middot; Sāriputta&rsquo;s Lion&rsquo;s Roar</a> '
        "&mdash; previous.",
        '<a href="an-9.13.html">AN 9.13 &middot; With Koṭṭhita</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.13 — Koṭṭhikasutta
# --------------------------------------------------------------------------- #
page(
    13, "Koṭṭhika", "With Koṭṭhita",
    vagga=VAGGA_2,
    meta_title="AN 9.13 — With Koṭṭhita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Koṭṭhikasutta, in which Mahākoṭṭhita questions Sāriputta with ten "
        "denials, ruling out a deterministic view of karma before "
        "Sāriputta names the real goal of the spiritual life. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue in the same "
                    "general setting as the chapter"),
        ("Speakers", "Venerable Mahākoṭṭhita questioning Venerable "
                     "Sāriputta"),
        ("Form", "Ten paired questions, each answered &lsquo;certainly "
                 "not,&rsquo; then a direct question and Sāriputta's own "
                 "answer"),
        ("Length", "~3 minutes to read"),
        ("A negative approach to a positive answer", "Ten denials clear "
         "away wrong reasons before the real goal — knowing the four "
         "noble truths — is finally named"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "repetitive but philosophically pointed, worth "
                       "reading for what it rules out"),
    ],
    why=(
        "Mahākoṭṭhita puts ten paired questions to Sāriputta, each asking "
        "whether the spiritual life is lived so that karmic results might "
        "be rearranged &mdash; experienced in a different life, felt as "
        "pleasant instead of painful, ripened early or late, felt more or "
        "less than their due, or avoided altogether &mdash; and Sāriputta "
        "answers &lsquo;certainly not&rsquo; to every one, before naming "
        "the real goal: to know, see, attain, realize, and comprehend the "
        "four noble truths."),
    guide=[
        ("The teaching in one sentence", [
            "The spiritual life is not lived to rearrange the results of "
            "past deeds in any way, but to know, see, attain, realize, "
            "and comprehend what is otherwise unknown, unseen, "
            "unattained, unrealized, and uncomprehended: the four noble "
            "truths."]),
        ("Ten ways of misunderstanding karma, ruled out", [
            "Mahākoṭṭhita's ten questions test five paired "
            "misconceptions: that deeds ripening now might instead ripen "
            "later or vice versa, that painful results might become "
            "pleasant or vice versa, that ripening might be sped up or "
            "delayed, that a large result might be reduced or a small one "
            "magnified, and that karmic results might be avoided "
            "altogether or invented from nothing. Sāriputta rejects every "
            "one without qualification."]),
        ("Clearing ground before building", [
            "The discourse's structure is deliberately negative before "
            "it is positive: only once all ten wrong reasons have been "
            "explicitly ruled out does Mahākoṭṭhita ask the direct "
            "question &mdash; what, then, is the goal? &mdash; and only "
            "then does Sāriputta answer."]),
        ("The four noble truths, named without being spelled out again", [
            "Sāriputta's answer names suffering, its origin, its "
            "cessation, and the practice leading to its cessation as "
            "&ldquo;the unknown, unseen, unattained, unrealized, and "
            "uncomprehended&rdquo; that the spiritual life exists to "
            "know, see, attain, realize, and comprehend &mdash; the same "
            "four truths spelled out in full at their most famous "
            "setting, the first sermon, here simply named in their "
            "standard four-part form."]),
    ],
    terms=[
        ("idha vuttavedanīyaṁ kammaṁ samparāye vuttavedanīyaṁ hoti",
         "&ldquo;deeds to be experienced in this life be experienced in "
         "lives to come&rdquo; &mdash; the first of ten misconceptions "
         "Mahākoṭṭhita tests and Sāriputta rejects."),
        ("ekantadukkhavedanīyaṁ kammaṁ",
         "&ldquo;deeds to be experienced as painful&rdquo; &mdash; part "
         "of the second pair of questions, testing whether painful "
         "results might become pleasant."),
        ("bahuṁ vā vedanīyaṁ kammaṁ appaṁ vedanīyaṁ",
         "&ldquo;deeds to be experienced a lot be experienced a "
         "little&rdquo; &mdash; the fourth pair, testing whether the "
         "scale of karmic results can be altered."),
        ("aññātassa aññātaṁ, adiṭṭhassa diṭṭhaṁ",
         "&ldquo;to know, see... that which is unknown, unseen&rdquo; "
         "&mdash; Sāriputta's own positive answer, naming the goal in "
         "place of the ten rejected misconceptions."),
        ("idaṁ dukkhanti... ayaṁ dukkhanirodhagāminī paṭipadāti",
         "the four noble truths, named in their standard form as what "
         "the spiritual life exists to know, see, attain, realize, and "
         "comprehend."),
    ],
    text_intro=(
        "The discourse in full: ten questions each answered &lsquo;"
        "certainly not,&rsquo; then Sāriputta's own answer naming the "
        "four noble truths as the real goal. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Ten questions, ten denials"),
        ("p", "&sect;1", "an9.13:1.1-10.2"),
        ("p", "&sect;2", "an9.13:11.1-20.2"),
        ("h3", "The real goal, named"),
        ("p", "&sect;3", "an9.13:21.1-21.9"),
    ],
    quiz=[
        {"q": "What does Mahākoṭṭhita's first pair of questions test?",
         "opts": [
             "Whether ethical conduct matters",
             "Whether the spiritual life is lived so deeds due in this "
             "life might instead ripen in future lives, or vice versa",
             "Whether meditation is necessary",
             "Whether the Buddha exists"],
         "correct": 1,
         "expl": "The first of five paired misconceptions about "
                 "rearranging karmic results."},
        {"q": "How does Sāriputta answer every one of the ten questions?",
         "opts": [
             "With a qualified &lsquo;sometimes&rsquo;",
             "With an unqualified &lsquo;certainly not&rsquo;",
             "By refusing to answer",
             "By asking a counter-question each time"],
         "correct": 1,
         "expl": "Every misconception about rearranging karma is flatly "
                 "rejected."},
        {"q": "What structural choice does the discourse make before "
              "revealing the real goal?",
         "opts": [
             "It states the goal first, then explains it",
             "It clears away ten wrong reasons before Mahākoṭṭhita asks "
             "directly what the goal actually is",
             "It never states a positive goal at all",
             "It leaves the goal for the reader to infer"],
         "correct": 1,
         "expl": "Negative clearing before the positive answer."},
        {"q": "What is the real goal Sāriputta names for the spiritual "
              "life?",
         "opts": [
             "Rearranging karmic results favorably",
             "To know, see, attain, realize, and comprehend the four "
             "noble truths",
             "Escaping karma altogether",
             "Accumulating merit for a better rebirth"],
         "correct": 1,
         "expl": "Named as &ldquo;the unknown, unseen, unattained&rdquo; "
                 "in their standard four-part form."},
        {"q": "According to the guide, where else are the four noble "
              "truths spelled out in their most famous setting?",
         "opts": [
             "Nowhere else in the canon",
             "The first sermon",
             "Only in this discourse",
             "In a later commentary only"],
         "correct": 1,
         "expl": "Named here in standard form rather than spelled out "
                 "afresh."},
        {"q": "Who questions whom in this discourse?",
         "opts": [
             "The Buddha questions Sāriputta",
             "Mahākoṭṭhita questions Sāriputta",
             "Sāriputta questions Mahākoṭṭhita",
             "Ānanda questions the Buddha"],
         "correct": 1,
         "expl": "One chief disciple questioning another, without the "
                 "Buddha present in the dialogue itself."},
    ],
    marginalia=[
        ("Ten questions, one answer", [
            "&ldquo;certainly not&rdquo; &mdash;",
            "ten ways karma might be",
            "rearranged, all ruled out",
        ]),
        ("Clearing ground first", [
            "not this, not that &mdash;",
            "only then the question:",
            "what, then, is the goal?",
        ]),
        ("The four truths, named", [
            "unknown, unseen, unattained &mdash;",
            "suffering and its ending,",
            "known here in brief",
        ]),
        ("Cross-references", [
            "AN 9.12 &middot; previous, With Residue",
            "AN 9.14 &middot; next, With Samiddhi",
        ]),
    ],
    further=[
        '<a href="%s/an9.13/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.12.html">AN 9.12 &middot; With Residue</a> &mdash; previous.',
        '<a href="an-9.14.html">AN 9.14 &middot; With Samiddhi</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.14 — Samiddhisutta
# --------------------------------------------------------------------------- #
page(
    14, "Samiddhi", "With Samiddhi",
    vagga=VAGGA_2,
    meta_title="AN 9.14 — With Samiddhi | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Samiddhisutta, a nine-question catechism tracing thoughts from "
        "name and form through contact, feeling, immersion, mindfulness, "
        "and wisdom to freedom from death. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue in the same "
                    "general setting as the chapter"),
        ("Speakers", "Venerable Sāriputta questioning Venerable Samiddhi"),
        ("Form", "Nine successive questions and answers, each building on "
                 "the last, closed by a caution against conceit"),
        ("Length", "~1 minute to read"),
        ("A chain, not a list", "Each answer becomes the ground for the "
         "next question, tracing thought from its basis to its final "
         "objective rather than naming nine parallel items"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief "
                       "but conceptually dense, best read slowly, term by "
                       "term"),
    ],
    why=(
        "Sāriputta questions Samiddhi in a nine-step chain &mdash; what "
        "grounds thoughts, where they diversify, what originates, meets, "
        "chiefs, rules, oversees, and cores them, and what their "
        "objective is &mdash; drawing out name and form, the elements, "
        "contact, feeling, immersion, mindfulness, wisdom, freedom, and "
        "finally freedom from death, then praises Samiddhi's answers "
        "while warning him not to grow conceited."),
    guide=[
        ("The teaching in one sentence", [
            "Thoughts arise based on name and form, diversify in the "
            "elements, originate from contact, meet in feeling, are "
            "chiefed by immersion, ruled by mindfulness, overseen by "
            "wisdom, cored by freedom, and aimed at freedom from death."]),
        ("Nine questions, one unbroken chain", [
            "Unlike the many nine-item lists elsewhere in this chapter, "
            "this discourse is not a list of nine parallel items but a "
            "single chain: each answer supplies the ground for the next "
            "question, moving from the most basic condition for thought "
            "to arise to its furthest and final objective."]),
        ("From name and form to freedom from death", [
            "The chain's two ends frame the whole spiritual project: it "
            "begins with name and form, the basic mind-and-body "
            "condition for any thought at all, and ends with freedom "
            "from death, the deathless, naming what all of it is finally "
            "for."]),
        ("Praise, and an immediate caution", [
            "Sāriputta confirms that Samiddhi has answered every question "
            "correctly, calling it &ldquo;good, good&rdquo; &mdash; but "
            "closes with a caution rather than unqualified praise: "
            "&ldquo;don't get conceited because of that,&rdquo; a brief "
            "reminder that correct answers are not themselves the "
            "attainment they describe."]),
    ],
    terms=[
        ("nāmarūpanissitā",
         "&ldquo;based on name and form&rdquo; &mdash; Samiddhi's first "
         "answer, the basic condition for thoughts to arise at all."),
        ("dhātusu vematteyya",
         "&ldquo;diversified in the elements&rdquo; &mdash; the second "
         "link, naming where thoughts take on their variety."),
        ("phassasamudayā",
         "&ldquo;contact is their origin&rdquo; &mdash; the third link in "
         "the chain."),
        ("samādhippamukhā",
         "&ldquo;immersion is their chief&rdquo; &mdash; the fifth link, "
         "naming what governs thought once it has met in feeling."),
        ("amatogadhā",
         "&ldquo;their objective is freedom from death&rdquo; &mdash; "
         "the chain's final link, naming the deathless as the whole "
         "sequence's ultimate aim."),
    ],
    text_intro=(
        "The discourse in full: nine questions tracing an unbroken chain "
        "from name and form to freedom from death. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine questions, one chain"),
        ("p", "&sect;1", "an9.14:1.1-10.2"),
        ("h3", "Praise, and a caution"),
        ("p", "&sect;2", "an9.14:11.1-11.11"),
    ],
    quiz=[
        {"q": "How does this discourse's structure differ from most other "
              "nine-item teachings in this chapter?",
         "opts": [
             "It has no structure at all",
             "It is a single unbroken chain, each answer grounding the "
             "next question, not a list of nine parallel items",
             "It repeats the same question nine times",
             "It is spoken entirely by the Buddha"],
         "correct": 1,
         "expl": "A chain from basis to objective, not a parallel list."},
        {"q": "What does Samiddhi name as the basis on which thoughts "
              "arise?",
         "opts": [
             "Contact", "Name and form", "Wisdom", "Immersion"],
         "correct": 1,
         "expl": "The chain's opening link, the basic mind-and-body "
                 "condition for thought."},
        {"q": "What does Samiddhi name as the chain's final objective?",
         "opts": [
             "Wealth and long life",
             "Freedom from death",
             "Rebirth in a heavenly realm",
             "Mastery of the elements"],
         "correct": 1,
         "expl": "The deathless, naming what the whole sequence is "
                 "finally for."},
        {"q": "What links immersion, mindfulness, and wisdom in the "
              "middle of the chain?",
         "opts": [
             "They are unrelated asides",
             "Each is named chief, ruler, and overseer of thought in "
             "turn, following from feeling",
             "They replace the earlier links entirely",
             "They are only mentioned once, together"],
         "correct": 1,
         "expl": "Three consecutive links, each naming a different kind "
                 "of governance over thought."},
        {"q": "How does Sāriputta respond to Samiddhi's answers?",
         "opts": [
             "With silence", "With praise, &lsquo;good, good,&rsquo; but "
             "also a caution not to grow conceited",
             "With correction of every answer",
             "By asking Samiddhi to repeat them"],
         "correct": 1,
         "expl": "Genuine praise paired with an immediate check against "
                 "pride."},
        {"q": "Who questions whom in this discourse?",
         "opts": [
             "The Buddha questions Samiddhi",
             "Sāriputta questions Samiddhi",
             "Samiddhi questions Sāriputta",
             "Mahākoṭṭhita questions Samiddhi"],
         "correct": 1,
         "expl": "A chief disciple examining a junior mendicant's "
                 "understanding."},
    ],
    marginalia=[
        ("A chain, not a list", [
            "name-and-form, elements,",
            "contact, feeling, immersion,",
            "mindfulness, wisdom, freedom",
        ]),
        ("From basis to objective", [
            "thought's first ground",
            "to its final aim &mdash;",
            "freedom from death",
        ]),
        ("Praise, with a caution", [
            "&ldquo;good, good, Samiddhi&rdquo; &mdash;",
            "but don't grow conceited",
            "over a right answer",
        ]),
        ("Cross-references", [
            "AN 9.13 &middot; previous, With Koṭṭhita",
            "AN 9.15 &middot; next, The Simile of the Boil",
        ]),
    ],
    further=[
        '<a href="%s/an9.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.13.html">AN 9.13 &middot; With Koṭṭhita</a> &mdash; previous.',
        '<a href="an-9.15.html">AN 9.15 &middot; The Simile of the Boil</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.15 — Gaṇḍasutta
# --------------------------------------------------------------------------- #
page(
    15, "Gaṇḍa", "The Simile of the Boil",
    vagga=VAGGA_2,
    meta_title="AN 9.15 — The Simile of the Boil | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Gaṇḍasutta, a brief and vivid simile comparing the body to an "
        "old boil with nine oozing orifices, closing with a call to have "
        "no illusion about it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single extended simile, stated once as an image and "
                 "once applied directly to the body"),
        ("Length", "~30 seconds to read"),
        ("The shortest kind of discourse in this chapter", "One image, "
         "stated and then applied, with no narrative frame and no "
         "further teaching attached"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and blunt, best read for its intended discomfort"),
    ],
    why=(
        "The body is compared to an old boil with nine orifices, each a "
        "continually open wound oozing and exuding what is filthy, "
        "stinking, and disgusting &mdash; a body produced by mother and "
        "father, built up from food, liable to impermanence and "
        "breaking up, of which mendicants are told to have no illusion."),
    guide=[
        ("The teaching in one sentence", [
            "&lsquo;Boil&rsquo; is a term for this body, made up of the "
            "four principal states, produced by mother and father, and "
            "built up from food; like an old boil with nine continually "
            "open, oozing orifices, it is filthy, stinking, and "
            "disgusting, and mendicants should have no illusion about "
            "it."]),
        ("An image, then its application", [
            "The discourse states its simile first in the abstract "
            "&mdash; a many-years-old boil with nine open, oozing "
            "orifices &mdash; then applies it directly: the body itself "
            "is the boil, its nine orifices are its own natural "
            "openings, and what oozes from them is, by the text's own "
            "plain word, filthy, stinking, and disgusting."]),
        ("Nine orifices, the body's own", [
            "The number nine names the body's own natural openings "
            "&mdash; the standard reckoning of two eyes, two ears, two "
            "nostrils, the mouth, and the two lower openings &mdash; "
            "reframed here not as neutral anatomy but as continually "
            "open wounds, tying this discourse's number to the "
            "collection it belongs to."]),
        ("A blunt close, without softening", [
            "The discourse draws no further conclusion and offers no "
            "consoling turn: it simply names the body a boil and "
            "instructs mendicants to have no illusion about it, trusting "
            "the image itself to do the teaching's work without further "
            "elaboration."]),
    ],
    terms=[
        ("gaṇḍo",
         "&ldquo;boil&rdquo; &mdash; the discourse's own title term and "
         "central image for the body."),
        ("navahi vaṇamukhehi",
         "&ldquo;nine orifices that were continually open wounds&rdquo; "
         "&mdash; the boil's nine openings, applied directly to the "
         "body's own natural orifices."),
        ("cātumahābhūtiko",
         "&ldquo;made up of the four principal states&rdquo; &mdash; "
         "the standard description of the body as earth, water, fire, "
         "and air, given here as part of the boil's own definition."),
        ("mātāpettikasambhavo",
         "&ldquo;produced by mother and father&rdquo; &mdash; naming the "
         "body's ordinary biological origin as part of its unglamorous "
         "reality."),
        ("mā ca imasmiṁ kāye apekkhaṁ akattha",
         "&ldquo;have no illusion about this body&rdquo; &mdash; the "
         "discourse's own closing instruction, its only explicit call to "
         "action."),
    ],
    text_intro=(
        "The discourse in full: a single simile, stated and then applied "
        "directly to the body. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "The image, and its application"),
        ("p", "&sect;1", "an9.15:1.1-2.7"),
    ],
    quiz=[
        {"q": "What image does this discourse use for the body?",
         "opts": [
             "A lotus rising above muddy water",
             "An old boil with nine continually open, oozing orifices",
             "A well-tuned lute",
             "A raft for crossing a flood"],
         "correct": 1,
         "expl": "A single blunt image, stated and then applied."},
        {"q": "What do the boil's nine orifices correspond to on the "
              "body?",
         "opts": [
             "Nine wounds from illness",
             "The body's own natural openings — eyes, ears, nostrils, "
             "mouth, and the two lower openings",
             "Nine meditation subjects",
             "Nine monastic robes"],
         "correct": 1,
         "expl": "Ordinary anatomy, reframed as continually open wounds."},
        {"q": "What three words describe what oozes from the boil's "
              "orifices?",
         "opts": [
             "Sweet, fragrant, pleasant",
             "Filthy, stinking, and disgusting",
             "Clear, pure, refreshing",
             "Warm, soft, gentle"],
         "correct": 1,
         "expl": "The discourse's own blunt, repeated description."},
        {"q": "What instruction closes the discourse?",
         "opts": [
             "Wash the body frequently",
             "Have no illusion about this body",
             "Avoid all physical contact",
             "Meditate only on beautiful objects"],
         "correct": 1,
         "expl": "A direct call to action, without further elaboration."},
        {"q": "How does the guide describe this discourse's overall "
              "approach?",
         "opts": [
             "Gentle and consoling",
             "Blunt, offering no softening turn and trusting the image "
             "itself to do the teaching's work",
             "Highly technical and abstract",
             "Framed entirely as a narrative"],
         "correct": 1,
         "expl": "One stark image, applied directly, with nothing added."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, the shortest form in this chapter."},
    ],
    marginalia=[
        ("An old boil", [
            "nine orifices,",
            "continually open wounds &mdash;",
            "filthy, oozing, foul",
        ]),
        ("The image applied", [
            "&lsquo;boil&rsquo; is a term",
            "for this very body &mdash;",
            "no illusion about it",
        ]),
        ("Nine, tied to this book", [
            "eyes, ears, nostrils,",
            "mouth, the lower two &mdash;",
            "nine, this chapter's own number",
        ]),
        ("Cross-references", [
            "AN 9.14 &middot; previous, With Samiddhi",
            "AN 9.16 &middot; next, Perceptions",
        ]),
    ],
    further=[
        '<a href="%s/an9.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.14.html">AN 9.14 &middot; With Samiddhi</a> &mdash; previous.',
        '<a href="an-9.16.html">AN 9.16 &middot; Perceptions</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.16 — Saññāsutta
# --------------------------------------------------------------------------- #
page(
    16, "Saññā", "Perceptions",
    vagga=VAGGA_2,
    meta_title="AN 9.16 — Perceptions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Saññāsutta, naming nine perceptions — from ugliness and death to "
        "fading away — whose culmination is freedom from death. This same "
        "list closes the entire Book of the Nines at AN 9.93. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list, no narrative and no similes"),
        ("Length", "~30 seconds to read"),
        ("A list that reappears at the end of the book", "This exact "
         "nine-item list of perceptions is the same list that closes the "
         "entire Book of the Nines, applied there to insight into greed "
         "at AN 9.93 and following"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "but worth remembering for later in this nipāta"),
    ],
    why=(
        "Nine perceptions &mdash; of ugliness, death, the repulsiveness "
        "of food, dissatisfaction with the whole world, impermanence, "
        "suffering in impermanence, not-self in suffering, giving up, "
        "and fading away &mdash; are named as very fruitful and "
        "beneficial when developed and cultivated, with freedom from "
        "death as their objective and culmination."),
    guide=[
        ("The teaching in one sentence", [
            "Nine perceptions &mdash; ugliness, death, the repulsiveness "
            "of food, dissatisfaction with the whole world, impermanence, "
            "suffering in impermanence, not-self in suffering, giving up, "
            "and fading away &mdash; are very fruitful and beneficial "
            "when developed and cultivated, with freedom from death as "
            "their objective and culmination."]),
        ("A bare list, stated once", [
            "Unlike the narrative discourses surrounding it in this "
            "chapter, this one offers no story and no simile &mdash; just "
            "the nine perceptions named in sequence, framed at the start "
            "and closed at the end by the same claim about their fruit "
            "and their final aim."]),
        ("A list already partly met, and one to be met again", [
            "A subset of four of these same nine perceptions has already "
            "appeared, transformed into active practices, in the four "
            "further things at AN 9.1 and AN 9.3: the perception of "
            "ugliness against greed, and the perception of impermanence "
            "to uproot the conceit &lsquo;I am,&rsquo; among them."]),
        ("The same nine, closing the entire book", [
            "This exact sequence of nine perceptions reappears verbatim "
            "far later in this nipāta, at AN 9.93, as one of the two "
            "foundational lists the entire Rāgapeyyāla &mdash; the great "
            "closing peyyāla that ends the Book of the Nines &mdash; is "
            "built from. Encountering it here, named plainly and in "
            "full, is worth remembering when it resurfaces there in "
            "compressed form."]),
    ],
    terms=[
        ("nava saññā",
         "&ldquo;nine perceptions&rdquo; &mdash; the discourse's own "
         "title list, later reused at AN 9.93 for insight into greed."),
        ("asubhasaññā, maraṇasaññā",
         "&ldquo;the perception of ugliness, the perception of "
         "death&rdquo; &mdash; the first two of the nine, both already "
         "familiar from the four further things at AN 9.1 and AN 9.3."),
        ("āhāre paṭikūlasaññā",
         "&ldquo;the perception of repulsiveness of food&rdquo; &mdash; "
         "the third perception, not previously met in this chapter."),
        ("sabbaloke anabhiratasaññā",
         "&ldquo;the perception of dissatisfaction with the whole "
         "world&rdquo; &mdash; the fourth perception, naming a "
         "comprehensive disenchantment rather than a narrower object."),
        ("amatogadhā amatapariyosānā",
         "&ldquo;their objective and culmination is freedom from "
         "death&rdquo; &mdash; the same closing formula that ended the "
         "chain of questions at AN 9.14."),
    ],
    text_intro=(
        "The discourse in full: nine perceptions named in sequence, "
        "framed by a single claim about their fruit. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine perceptions"),
        ("p", "&sect;1", "an9.16:1.1-1.4"),
    ],
    quiz=[
        {"q": "What nine perceptions does this discourse name?",
         "opts": [
             "The nine orifices of the body",
             "Ugliness, death, repulsiveness of food, dissatisfaction "
             "with the whole world, impermanence, suffering in "
             "impermanence, not-self in suffering, giving up, and fading "
             "away",
             "The nine individuals found in the world",
             "Nine kinds of wrong view"],
         "correct": 1,
         "expl": "A bare list, stated once at the discourse's start and "
                 "restated to close it."},
        {"q": "What is named as the objective and culmination of these "
              "nine perceptions?",
         "opts": [
             "Wealth and long life",
             "Freedom from death",
             "Rebirth as a deity",
             "Monastic ordination"],
         "correct": 1,
         "expl": "The same deathless objective named at the end of AN "
                 "9.14's chain of questions."},
        {"q": "According to the guide, where have four of these nine "
              "perceptions already appeared in this chapter?",
         "opts": [
             "Nowhere else in this nipāta",
             "As active practices in the four further things at AN 9.1 "
             "and AN 9.3",
             "Only in the closing colophon",
             "In AN 9.11's ten similes"],
         "correct": 1,
         "expl": "Ugliness and impermanence among them, already met as "
                 "targeted practices."},
        {"q": "Where does this exact same nine-item list reappear later "
              "in this nipāta?",
         "opts": [
             "It never reappears",
             "At AN 9.93, as one of the two foundational lists building "
             "the great closing peyyāla of the entire Book of the Nines",
             "At AN 9.20, the chapter's last page",
             "In every subsequent chapter"],
         "correct": 1,
         "expl": "Worth remembering when this list resurfaces in "
                 "compressed form far later in the nipāta."},
        {"q": "How is this discourse structured?",
         "opts": [
             "A long narrative with several characters",
             "A single bare list, with no story or simile attached",
             "A dialogue between two mendicants",
             "A series of similes"],
         "correct": 1,
         "expl": "The shortest and plainest form a teaching can take in "
                 "this collection."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, like AN 9.15 immediately before it."},
    ],
    marginalia=[
        ("Nine perceptions", [
            "ugliness, death, food's",
            "repulsiveness, the whole",
            "world's dissatisfaction",
        ]),
        ("Impermanence, and beyond", [
            "suffering, not-self,",
            "giving up, fading away &mdash;",
            "freedom from death, their aim",
        ]),
        ("A list to remember", [
            "these same nine perceptions",
            "close the entire book &mdash;",
            "see AN 9.93",
        ]),
        ("Cross-references", [
            "AN 9.1, AN 9.3 &middot; four of these nine, already met as "
            "active practices",
            "AN 9.15 &middot; previous, The Simile of the Boil",
            "AN 9.17 &middot; next, Families",
        ]),
    ],
    further=[
        '<a href="%s/an9.16/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.15.html">AN 9.15 &middot; The Simile of the Boil</a> &mdash; previous.',
        '<a href="an-9.17.html">AN 9.17 &middot; Families</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.17 — Kulasutta
# --------------------------------------------------------------------------- #
page(
    17, "Kula", "Families",
    vagga=VAGGA_2,
    meta_title="AN 9.17 — Families | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Kulasutta, naming nine factors that make a family not worth "
        "visiting and nine mirror-image factors that make one worth "
        "visiting. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two mirror-image nine-item lists, one negative and one "
                 "positive"),
        ("Length", "~1 minute to read"),
        ("A near neighbor to AN 9.19", "A very similar-sounding list of "
         "duties appears again at AN 9.19, spoken by deities rather than "
         "the Buddha, and does not match this list item for item"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; two "
                       "clean parallel lists, easy to follow"),
    ],
    why=(
        "Nine factors make visiting a family, or sitting down once "
        "arrived, not worthwhile &mdash; a cold welcome, hidden "
        "possessions, stinginess, carelessness in giving, and "
        "inattention to the teachings &mdash; and the same nine factors, "
        "reversed, make it worthwhile: a warm welcome, openness, "
        "generosity, care, and genuine attention."),
    guide=[
        ("The teaching in one sentence", [
            "A family that doesn't rise politely, hide what they have, "
            "give little even when they have much, give coarse things "
            "even when they have fine ones, give carelessly, or listen "
            "to the teachings is not worth visiting; a family that does "
            "the reverse in each respect is."]),
        ("Nine factors, then their mirror image", [
            "The discourse states the nine unworthy factors first, in a "
            "compact list running from a cold reception through hidden "
            "and grudging giving to inattention during teaching, then "
            "restates every one in reverse to name the worthy family: "
            "warm reception, openness, generosity proportionate to "
            "means, and genuine attentiveness."]),
        ("Practical hospitality and generosity, not doctrine", [
            "Unlike much of this chapter, this discourse concerns "
            "concrete social conduct &mdash; how a household receives a "
            "visiting mendicant, whether it shares what it has, and "
            "whether it actually listens when the teachings are spoken "
            "&mdash; rather than meditative attainment or philosophical "
            "argument."]),
        ("A near neighbor worth distinguishing from AN 9.19", [
            "AN 9.19, three discourses on, tells of deities recounting a "
            "similar-sounding graduated list of duties toward visiting "
            "renunciates &mdash; rising, bowing, offering a seat, sharing, "
            "and engaging with the teaching. The two lists overlap in "
            "their opening gestures but are not the same list; AN 9.19's "
            "is a narrative of deities' own past failures and successes, "
            "not this discourse's bare double list of family factors."]),
    ],
    terms=[
        ("nāsanaṁ kulaṁ upasaṅkamituṁ",
         "&ldquo;visiting a family... is not worthwhile&rdquo; &mdash; "
         "the discourse's own framing for the first, negative list."),
        ("na paṭisammodanti",
         "&ldquo;they don't politely rise&rdquo; &mdash; the first of "
         "the nine unworthy factors, an inhospitable reception."),
        ("paṭicchannena denti",
         "&ldquo;they give carelessly&rdquo; &mdash; naming grudging or "
         "inattentive giving as distinct from simply giving little."),
        ("sāsanaṁ upasaṅkamituṁ",
         "&ldquo;visiting a family... is worthwhile&rdquo; &mdash; the "
         "mirror-image framing for the second, positive list."),
        ("bhāsamānaṁ sussūsanti",
         "&ldquo;when you're speaking, they listen well&rdquo; &mdash; "
         "the ninth and final factor, closing both lists on genuine "
         "attentiveness."),
    ],
    text_intro=(
        "The discourse in full: nine factors that make a family not "
        "worth visiting, then the same nine reversed. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine factors: not worth visiting"),
        ("p", "&sect;1", "an9.17:1.1-1.4"),
        ("h3", "Nine factors, reversed: worth visiting"),
        ("p", "&sect;2", "an9.17:2.1-2.4"),
    ],
    quiz=[
        {"q": "What kind of family does this discourse say is not worth "
              "visiting?",
         "opts": [
             "A wealthy family only",
             "One with a cold reception, hidden possessions, stinginess, "
             "careless giving, and inattention to the teachings",
             "Any family with children",
             "A family that has never met a mendicant before"],
         "correct": 1,
         "expl": "Nine factors, all concerning hospitality, generosity, "
                 "and attentiveness."},
        {"q": "How is the second, positive list of nine factors "
              "constructed?",
         "opts": [
             "As an entirely new and unrelated list",
             "As the exact reverse of the first list, factor for factor",
             "As a shorter summary of the first list",
             "As a list of five factors, not nine"],
         "correct": 1,
         "expl": "A clean mirror image, negative to positive."},
        {"q": "What kind of concerns does this discourse address, "
              "compared to much of this chapter?",
         "opts": [
             "Advanced meditative attainments",
             "Concrete social conduct — hospitality, generosity, and "
             "attentiveness to teaching, not philosophical argument",
             "Monastic disciplinary rules",
             "Cosmology"],
         "correct": 1,
         "expl": "Practical household conduct toward visiting "
                 "mendicants."},
        {"q": "According to the guide, how does this discourse's list "
              "relate to the list of duties at AN 9.19?",
         "opts": [
             "They are the identical list, word for word",
             "They overlap in their opening gestures but are not the "
             "same list — AN 9.19 is a narrative of deities' own past "
             "conduct",
             "AN 9.19 replaces this discourse's list entirely",
             "There is no relationship between them"],
         "correct": 1,
         "expl": "Similar-sounding but distinct lists, worth "
                 "distinguishing carefully."},
        {"q": "What closes both the negative and positive lists?",
         "opts": [
             "Ethical conduct in general",
             "Whether the family listens well when the teachings are "
             "being spoken",
             "Wealth or poverty",
             "The number of children in the household"],
         "correct": 1,
         "expl": "Attentiveness to the teaching is the ninth and final "
                 "factor in both lists."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, like several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Nine factors, unworthy", [
            "no rising, no bowing,",
            "hidden wealth, coarse gifts,",
            "careless, and not listening",
        ]),
        ("The same nine, reversed", [
            "warm welcome, openness,",
            "generosity in kind,",
            "and genuine attention",
        ]),
        ("A near neighbor, not a twin", [
            "AN 9.19's deities",
            "recount a similar list &mdash;",
            "overlapping, not the same",
        ]),
        ("Cross-references", [
            "AN 9.16 &middot; previous, Perceptions",
            "AN 9.19 &middot; a similar-sounding but distinct list of "
            "duties",
            "AN 9.18 &middot; next, The Sabbath with Nine Factors",
        ]),
    ],
    further=[
        '<a href="%s/an9.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.16.html">AN 9.16 &middot; Perceptions</a> &mdash; previous.',
        '<a href="an-9.18.html">AN 9.18 &middot; The Sabbath with Nine Factors</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.18 — Navaṅgauposathasutta
# --------------------------------------------------------------------------- #
page(
    18, "Navaṅgauposatha", "The Sabbath with Nine Factors",
    vagga=VAGGA_2,
    meta_title="AN 9.18 — The Sabbath with Nine Factors | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Navaṅgauposathasutta, describing the sabbath observance built "
        "from the standard eight precepts plus a ninth factor: the "
        "meditation on love. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two factors given in full, the remaining six passed "
                 "over by the source's own peyyāla, then the ninth "
                 "factor given in full"),
        ("Length", "~1 minute to read what survives; the full nine-"
                   "factor observance is longer"),
        ("A well-known observance, one factor added", "Eight of the nine "
         "factors are the standard lay sabbath precepts found elsewhere "
         "in the canon; the ninth, meditation on love, is this "
         "discourse's own addition"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief "
                       "as it survives, but the guide fills in what the "
                       "source elides"),
    ],
    why=(
        "The sabbath observed with nine factors is very fruitful, "
        "beneficial, dazzling, and bountiful &mdash; a noble disciple "
        "reflects on living as the perfected ones do for a single day "
        "and night, beginning with giving up killing and, after passing "
        "through seven further factors the source itself abbreviates, "
        "ending with giving up luxurious beds and meditating on a heart "
        "full of love spread to the whole world."),
    guide=[
        ("The teaching in one sentence", [
            "A noble disciple who observes the sabbath with nine factors "
            "&mdash; the eight standard precepts of giving up killing, "
            "stealing, unchastity, lying, intoxicants, eating at the "
            "wrong time, entertainment and adornment, and luxurious "
            "beds, plus a heart of love spread to the whole world "
            "&mdash; produces something very fruitful, beneficial, "
            "dazzling, and bountiful."]),
        ("Eight familiar precepts, only two written out here", [
            "The source itself writes out only the first factor "
            "(renouncing killing) and the eighth (renouncing luxurious "
            "beds) in full, passing over the second through seventh with "
            "its own internal peyyāla. These middle six are the "
            "remaining standard lay sabbath precepts found in fuller form "
            "elsewhere in the canon: giving up stealing, unchastity, "
            "lying, intoxicants, eating after midday, and entertainment, "
            "garlands, and adornments."]),
        ("A ninth factor beyond the usual eight", [
            "What makes this observance &ldquo;the sabbath with nine "
            "factors&rdquo; rather than the more familiar eight-factor "
            "sabbath found elsewhere is this discourse's own addition: a "
            "ninth factor of meditation, spreading a heart full of love "
            "in all directions, to the whole world, abundant, expansive, "
            "limitless, free of enmity and ill will."]),
        ("Each factor modeled on the perfected ones", [
            "Every factor follows the same three-part pattern: first "
            "naming what the perfected ones do for as long as they "
            "live, then committing to do the same for this one day and "
            "night, then naming this as observing the sabbath &lsquo;by "
            "doing as the perfected ones do.&rsquo; The lay observance is "
            "framed throughout as temporary imitation of a permanent "
            "monastic standard."]),
    ],
    terms=[
        ("navaṅgena uposathena",
         "&ldquo;the sabbath with its nine factors&rdquo; &mdash; the "
         "discourse's own title phrase, distinguishing this observance "
         "from the more familiar eight-factor sabbath."),
        ("daṇḍaṁ nikkhipitvā satthaṁ nikkhipitvā",
         "&ldquo;renouncing the rod and the sword&rdquo; &mdash; part of "
         "the first factor, giving up killing living creatures."),
        ("uccāsayanamahāsayanaṁ",
         "&ldquo;high and luxurious beds&rdquo; &mdash; what the eighth "
         "factor gives up, sleeping instead on a cot or straw mat."),
        ("arahataṁ anukaromāno",
         "&ldquo;doing as the perfected ones do&rdquo; &mdash; the "
         "shared closing phrase for each factor, framing lay observance "
         "as imitation of monastic standards."),
        ("mettāsahagatena cetasā",
         "&ldquo;a heart full of love&rdquo; &mdash; the ninth and final "
         "factor, this discourse's own addition beyond the standard "
         "eight precepts."),
    ],
    text_intro=(
        "The discourse in full, as it survives in the source: the first "
        "and eighth factors given in full, the second through seventh "
        "passed over by the source's own internal peyyāla, and the ninth "
        "given in full. The guide names the six elided factors from the "
        "standard sabbath precepts found elsewhere in the canon. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first factor, in full"),
        ("p", "&sect;1", "an9.18:1.1-1.7"),
        ("h3", "The eighth factor (the source elides the second through "
               "seventh)"),
        ("p", "&sect;2", "an9.18:2.1-2.4"),
        ("h3", "The ninth factor: a heart of love"),
        ("p", "&sect;3", "an9.18:3.1-4.1"),
    ],
    quiz=[
        {"q": "How many of this observance's nine factors does the "
              "source write out in full, and which?",
         "opts": [
             "All nine, in full detail",
             "Only the first (giving up killing) and the eighth (giving "
             "up luxurious beds), with the second through seventh passed "
             "over by the source's own peyyāla",
             "Only the ninth factor",
             "None; the whole discourse is abbreviated"],
         "correct": 1,
         "expl": "The guide names the six elided middle factors from the "
                 "standard sabbath precepts found elsewhere."},
        {"q": "What are the six middle factors this discourse's source "
              "elides, according to the standard sabbath precepts?",
         "opts": [
             "Six more kinds of meditation",
             "Giving up stealing, unchastity, lying, intoxicants, eating "
             "after midday, and entertainment, garlands, and adornments",
             "Six monastic robes",
             "Six kinds of wrong view"],
         "correct": 1,
         "expl": "The remaining standard eight-precept sabbath factors, "
                 "found in fuller form elsewhere in the canon."},
        {"q": "What makes this &ldquo;the sabbath with nine factors&rdquo; "
              "rather than the more familiar eight-factor sabbath?",
         "opts": [
             "It has one fewer precept than usual",
             "A ninth factor: meditating on a heart full of love spread "
             "to the whole world",
             "It is observed twice as often",
             "It replaces all eight precepts with new ones"],
         "correct": 1,
         "expl": "This discourse's own addition beyond the standard "
                 "eight precepts."},
        {"q": "What three-part pattern does each factor follow?",
         "opts": [
             "A question, an answer, and a simile",
             "Naming what the perfected ones do for life, committing to "
             "the same for one day and night, and naming this as "
             "imitating the perfected ones",
             "A narrative, a teaching, and a verse",
             "A list, a warning, and a blessing"],
         "correct": 1,
         "expl": "Lay observance framed throughout as temporary "
                 "imitation of a permanent monastic standard."},
        {"q": "How is the result of this nine-factor observance "
              "described?",
         "opts": [
             "Modest but sufficient",
             "Very fruitful, beneficial, dazzling, and bountiful",
             "Uncertain and variable",
             "Only beneficial for monastics"],
         "correct": 1,
         "expl": "The discourse's own strong opening and closing claim."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, like several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight precepts, one day", [
            "no killing, stealing,",
            "unchastity, lying, drink,",
            "wrong times, shows, soft beds",
        ]),
        ("A ninth factor added", [
            "a heart full of love",
            "spread to every direction &mdash;",
            "beyond the usual eight",
        ]),
        ("Imitating the perfected", [
            "&ldquo;as they do for life,",
            "so I for a day and night&rdquo; &mdash;",
            "temporary, deliberate",
        ]),
        ("Cross-references", [
            "AN 9.17 &middot; previous, Families",
            "AN 9.19 &middot; next, A Deity",
        ]),
    ],
    further=[
        '<a href="%s/an9.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.17.html">AN 9.17 &middot; Families</a> &mdash; previous.',
        '<a href="an-9.19.html">AN 9.19 &middot; A Deity</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.19 — Devatāsutta — closes ch.2 Sīhanādavagga into AN 9.20, published
# earlier in this project's eighteen-page selection. Per the
# an-6.16/an-6.63/an-7.6/an-8.30/an-8.53 precedent, this page's next=
# splices straight into that existing page.
# --------------------------------------------------------------------------- #
page(
    19, "Devatā", "A Deity",
    vagga=VAGGA_2,
    next=("an-9.20.html", "AN 9.20 &middot; About Velāma"),
    meta_title="AN 9.19 — A Deity | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Devatāsutta, in which glorious deities recount to the Buddha, in "
        "graduated stages, their own past failures and eventual success "
        "in fulfilling their duty toward visiting renunciates. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Jeta&rsquo;s Grove, at night, visited by several "
                    "glorious deities lighting up the entire grove"),
        ("Speakers", "Several groups of deities, reporting to the Buddha "
                     "in turn"),
        ("Form", "Four successive reports from different groups of "
                 "deities, each stopping one step further along the same "
                 "graduated list of duties"),
        ("Length", "~3 minutes to read"),
        ("A near neighbor to AN 9.17, not its twin", "This discourse's "
         "graduated duties toward visiting renunciates overlap with AN "
         "9.17's family factors in their opening gestures, but form a "
         "different, more elaborate list"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "vivid nighttime visitation, worth reading for how "
                       "the stages build"),
    ],
    why=(
        "In the night, several groups of glorious deities visit the "
        "Buddha in turn, each recounting how, as humans, they fell short "
        "of their duty toward visiting renunciates by one further step "
        "&mdash; rising but not bowing, bowing but not offering a seat, "
        "offering a seat but not truly engaging with the teaching "
        "&mdash; and were reborn in a lesser realm, until a final group "
        "reports fulfilling every step and being reborn in a superior "
        "realm."),
    guide=[
        ("The teaching in one sentence", [
            "Deities who, as humans, fell short of fully receiving "
            "visiting renunciates &mdash; failing to rise, to bow, to "
            "offer a seat, to share, to listen to and engage with the "
            "teaching &mdash; report being reborn in a lesser realm out "
            "of remorse, while those who fulfilled every step of the "
            "duty were reborn in a superior one."]),
        ("Four reports, each one step further", [
            "The discourse structures its teaching through four "
            "successive groups of deities, not through a single "
            "abstract list: the first group failed at the very first "
            "gesture (rising but not bowing), the second failed one step "
            "later (bowing but not offering a seat), the third failed "
            "much further along (going through the physical courtesies "
            "but never truly engaging with the teaching itself), and the "
            "fourth succeeded at every step."]),
        ("From physical courtesy to genuine engagement", [
            "The full graduated sequence moves from bodily politeness "
            "&mdash; rising, bowing, offering a seat, sharing &mdash; "
            "into an entirely different register: sitting nearby to "
            "listen, actively listening, memorizing the teachings, "
            "examining their meaning, and finally practicing in line "
            "with what has been understood. Politeness alone, the "
            "discourse implies, is only the beginning."]),
        ("Overlapping with, but distinct from, AN 9.17", [
            "This graduated list of duties shares its opening gestures "
            "&mdash; rising, bowing, offering a seat &mdash; with AN "
            "9.17's nine factors for a family worth visiting, but is a "
            "longer and differently structured sequence, told here as "
            "deities' own testimony about their past lives rather than "
            "as a bare double list. The Buddha's closing exhortation "
            "&mdash; practice absorption, don't be negligent, don't "
            "regret it later like these deities &mdash; has no "
            "counterpart in AN 9.17 at all."]),
    ],
    terms=[
        ("obhāsayamānā kevalakappaṁ jetavanaṁ",
         "&ldquo;lighting up the entire Jeta's Grove&rdquo; &mdash; how "
         "the deities' arrival at night is described, marking their "
         "glorious status."),
        ("akatvā vata bho karaṇīyaṁ vippaṭisārino",
         "&ldquo;having not fulfilled our duty, full of remorse and "
         "regret&rdquo; &mdash; the shared refrain closing each group's "
         "report of falling short."),
        ("upanisīditvā dhammassavanāya",
         "&ldquo;sat nearby to listen to the teachings&rdquo; &mdash; "
         "the step at which the third group of deities fell short, "
         "having managed the physical courtesies but no further."),
        ("atthamaññāya dhammamaññāya dhammānudhammaṁ paṭipannā",
         "&ldquo;understanding the teaching and the meaning we practiced "
         "in line with the teaching&rdquo; &mdash; the final and highest "
         "step, achieved only by the fourth group."),
        ("rukkhamūlāni, suññāgārāni",
         "&ldquo;roots of trees... empty huts&rdquo; &mdash; the "
         "Buddha's own closing exhortation to the mendicants, pointing "
         "to available places for absorption after the deities' account."),
    ],
    text_intro=(
        "The discourse in full: four successive reports from groups of "
        "deities, each stopping one step further along the same "
        "graduated list of duties. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "The first group: rose, but did not bow"),
        ("p", "&sect;1", "an9.19:1.1-1.4"),
        ("h3", "The second group: bowed, but did not offer a seat"),
        ("p", "&sect;2", "an9.19:2.1-2.4"),
        ("h3", "The third group: courteous, but did not engage with the "
               "teaching"),
        ("p", "&sect;3", "an9.19:3.1-3.9"),
        ("h3", "The fourth group: fulfilled every step"),
        ("p", "&sect;4", "an9.19:4.1-4.5"),
    ],
    quiz=[
        {"q": "How does this discourse present its teaching about "
              "receiving visiting renunciates?",
         "opts": [
             "As a single bare list, with no narrative",
             "Through four successive groups of deities, each reporting "
             "how they fell short one step further along than the last",
             "As a debate between two deities",
             "As a monastic rule recited in full"],
         "correct": 1,
         "expl": "A graduated narrative, not an abstract list."},
        {"q": "At what step did the first group of deities fall short?",
         "opts": [
             "They never visited renunciates at all",
             "They politely rose but did not bow",
             "They offered a seat but did not share generously",
             "They listened but did not memorize the teachings"],
         "correct": 1,
         "expl": "The earliest possible failure, one gesture into the "
                 "sequence."},
        {"q": "What did the fourth group of deities do differently from "
              "the first three?",
         "opts": [
             "Nothing; all four groups received the same rebirth",
             "They fulfilled every step, from rising and bowing through "
             "practicing in line with the teaching, and were reborn in "
             "a superior realm",
             "They refused to visit renunciates at all",
             "They only bowed, nothing more"],
         "correct": 1,
         "expl": "Completing the full graduated sequence, unlike the "
                 "first three groups."},
        {"q": "According to the guide, what does the sequence's shift "
              "from physical courtesy to genuine engagement suggest?",
         "opts": [
             "That politeness alone is sufficient",
             "That physical courtesy is only the beginning; genuine "
             "engagement with the teaching itself is a further and "
             "higher step",
             "That listening to teachings is optional",
             "That the physical gestures don't matter at all"],
         "correct": 1,
         "expl": "The sequence moves from bodily politeness into "
                 "listening, memorizing, examining, and practicing."},
        {"q": "How does this discourse's list compare to AN 9.17's nine "
              "family factors?",
         "opts": [
             "They are word-for-word identical",
             "They overlap in their opening gestures but form a longer, "
             "differently structured sequence, told as deities' own "
             "testimony rather than a bare double list",
             "They have nothing in common",
             "AN 9.17 supersedes this discourse entirely"],
         "correct": 1,
         "expl": "A near neighbor, not a twin, as the guide notes."},
        {"q": "How does the Buddha close this discourse?",
         "opts": [
             "With a question for the mendicants",
             "With an exhortation to practice absorption, not be "
             "negligent, and not regret it later like these deities",
             "By dismissing the deities' account as unreliable",
             "By promising the mendicants a heavenly rebirth"],
         "correct": 1,
         "expl": "A direct call to action, unique to this discourse "
                 "among the two near-neighbor lists."},
    ],
    marginalia=[
        ("Four groups, one sequence", [
            "rose but did not bow;",
            "bowed but no seat offered;",
            "courteous, but no more",
        ]),
        ("From courtesy to engagement", [
            "listen, memorize,",
            "examine the meaning &mdash;",
            "practice what is understood",
        ]),
        ("Remorse, and its opposite", [
            "&ldquo;full of remorse, reborn",
            "in a lesser realm&rdquo; &mdash; or,",
            "fulfilled, a superior one",
        ]),
        ("Cross-references", [
            "AN 9.17 &middot; a similar-sounding but distinct list of "
            "duties",
            "AN 9.18 &middot; previous, The Sabbath with Nine Factors",
            "AN 9.20 &middot; next, About Velāma, closing this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an9.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.17.html">AN 9.17 &middot; Families</a> &mdash; a similar-sounding but '
        "distinct list of duties.",
        '<a href="an-9.18.html">AN 9.18 &middot; The Sabbath with Nine Factors</a> '
        "&mdash; previous.",
        '<a href="an-9.20.html">AN 9.20 &middot; About Velāma</a> &mdash; next, closing '
        "this chapter.",
    ],
)
