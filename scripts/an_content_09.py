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


# --------------------------------------------------------------------------- #
# ch.3 — Sattāvāsavagga (AN 9.21-31)
# --------------------------------------------------------------------------- #
VAGGA_3 = "<em>Sattāvāsavagga</em> &mdash; the third chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.21 — Tayodhammasutta
# --------------------------------------------------------------------------- #
page(
    21, "Tayodhamma", "In Three Particulars",
    vagga=VAGGA_3,
    prev=("an-9.20.html", "AN 9.20 &middot; About Velāma"),
    meta_title="AN 9.21 — In Three Particulars | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Tayodhammasutta, opening this chapter with a three-way "
        "cosmological comparison — Uttarakuru humans, the gods of the "
        "thirty-three, and the humans of this world, each surpassing the "
        "other two in three particulars. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Three parallel comparisons, each naming one group's own "
                 "three advantages over the other two"),
        ("Length", "~1 minute to read"),
        ("Nine by multiplication, not by a single list", "Three groups, "
         "each surpassing the others in three particulars, gives nine "
         "particulars total — this chapter's number reached by "
         "multiplication rather than one flat nine-item list"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "compact cosmological comparison, worth reading "
                       "for its final twist"),
    ],
    why=(
        "Three groups of beings each surpass the other two in three "
        "particulars of their own: the humans of Uttarakuru in "
        "selflessness, a fixed lifespan, and a distinctive nature; the "
        "gods of the thirty-three in heavenly lifespan, beauty, and "
        "happiness; and the humans of this world, the Black Plum Tree "
        "Land, in bravery, mindfulness, and the fact that the spiritual "
        "life is lived here."),
    guide=[
        ("The teaching in one sentence", [
            "Uttarakuru humans surpass the other two groups in "
            "selflessness, fixed lifespan, and distinctive nature; the "
            "gods of the thirty-three surpass them in heavenly lifespan, "
            "beauty, and happiness; and the humans of this world surpass "
            "both in bravery, mindfulness, and the fact that the "
            "spiritual life is lived here."]),
        ("Three comparisons, not one hierarchy", [
            "The discourse resists ranking these three groups on a single "
            "scale. Each of the three &mdash; a legendary northern human "
            "realm, the heaven of the thirty-three gods, and ordinary "
            "human life in this world &mdash; gets its own distinct set "
            "of three advantages the other two lack, with no group "
            "declared superior overall."]),
        ("Long life and beauty, set against something rarer", [
            "The gods' advantages &mdash; heavenly lifespan, beauty, "
            "happiness &mdash; read as the most enviable at first glance. "
            "But the discourse gives this world's ordinary humans their "
            "own equally real advantages, closing on the one that "
            "matters most for this whole collection's purpose."]),
        ("Why this world wins where it counts", [
            "The third particular named for this world's humans is not a "
            "worldly advantage at all: &lsquo;the spiritual life is lived "
            "here.&rsquo; Of the three groups compared, only ordinary "
            "human life in the Black Plum Tree Land offers the conditions "
            "for the very practice this entire collection is teaching "
            "&mdash; a quiet argument for the value of this life, however "
            "unglamorous next to Uttarakuru's ease or the gods' beauty."]),
    ],
    terms=[
        ("uttarakurukā manussā",
         "&ldquo;the humans of the land north of Kuru&rdquo; &mdash; a "
         "legendary human realm of ease and longevity, one of the three "
         "groups compared."),
        ("tāvatiṁsā devā",
         "&ldquo;the gods of the thirty-three&rdquo; &mdash; the second "
         "group, surpassing the others in heavenly lifespan, beauty, and "
         "happiness."),
        ("jambudīpakā manussā",
         "&ldquo;the humans of the Black Plum Tree Land&rdquo; &mdash; "
         "this discourse's own name for the human world of ordinary "
         "experience, the third group compared."),
        ("sūrā satimanto idha ca brahmacariyavāso",
         "&ldquo;bravery, mindfulness, and the spiritual life is lived "
         "here&rdquo; &mdash; the third group's own three advantages, "
         "closing on the discourse's real point."),
        ("brahmacariyavāso",
         "&ldquo;the spiritual life is lived&rdquo; &mdash; naming what "
         "only this human world, of the three compared, actually "
         "offers."),
    ],
    text_intro=(
        "The discourse in full: three groups, each surpassing the other "
        "two in three particulars of their own. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three groups, three particulars each"),
        ("p", "&sect;1", "an9.21:1.1-3.4"),
    ],
    quiz=[
        {"q": "What three groups does this discourse compare?",
         "opts": [
             "Three human kingdoms",
             "The humans of Uttarakuru, the gods of the thirty-three, and "
             "the humans of this world (the Black Plum Tree Land)",
             "Three kinds of deity only",
             "Three schools of wandering ascetics"],
         "correct": 1,
         "expl": "A legendary human realm, a heaven, and ordinary human "
                 "life, each with its own set of advantages."},
        {"q": "What three particulars belong to the gods of the thirty-"
              "three?",
         "opts": [
             "Selflessness, fixed lifespan, distinctive nature",
             "Heavenly lifespan, beauty, and happiness",
             "Bravery, mindfulness, and the spiritual life",
             "Wisdom, energy, and generosity"],
         "correct": 1,
         "expl": "The most conventionally enviable set, at first glance."},
        {"q": "What is the third and final particular named for this "
              "world's humans?",
         "opts": [
             "Wealth",
             "That the spiritual life is lived here",
             "Physical strength",
             "Political power"],
         "correct": 1,
         "expl": "Not a worldly advantage, but the condition for this "
                 "collection's own practice."},
        {"q": "How does the discourse structure its comparison?",
         "opts": [
             "As a single ranking from best to worst",
             "As three parallel comparisons, each group surpassing the "
             "other two in its own three particulars, with no overall "
             "winner declared",
             "As a debate between the three groups",
             "As a narrative journey between the three realms"],
         "correct": 1,
         "expl": "No single hierarchy — three distinct sets of "
                 "advantages."},
        {"q": "According to the guide, what does the final particular "
              "argue for?",
         "opts": [
             "The superiority of heavenly rebirth",
             "The value of this ordinary human life, however unglamorous "
             "next to Uttarakuru's ease or the gods' beauty, since only "
             "it offers the conditions for spiritual practice",
             "The need to seek rebirth in Uttarakuru",
             "That mindfulness is impossible for gods"],
         "correct": 1,
         "expl": "A quiet argument for practicing here and now."},
        {"q": "How does this chapter's number nine arise in this "
              "discourse?",
         "opts": [
             "From a single flat nine-item list",
             "By multiplication: three groups, each with three "
             "particulars of its own, totaling nine",
             "It doesn't relate to nine at all",
             "From nine named deities"],
         "correct": 1,
         "expl": "A structure this chapter reaches by multiplying three "
                 "by three, rather than a single nine-item list."},
    ],
    marginalia=[
        ("Three groups, three each", [
            "Uttarakuru's ease,",
            "the gods' long, beautiful lives,",
            "this world's own three gifts",
        ]),
        ("No single hierarchy", [
            "each surpasses the rest",
            "in its own particulars &mdash;",
            "no single winner named",
        ]),
        ("Why this life matters most", [
            "bravery, mindfulness,",
            "and the spiritual life",
            "lived only here",
        ]),
        ("Cross-references", [
            "AN 9.20 &middot; previous chapter's closing page, About "
            "Velāma",
            "AN 9.22 &middot; next, A Wild Colt",
        ]),
    ],
    further=[
        '<a href="%s/an9.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.20.html">AN 9.20 &middot; About Velāma</a> &mdash; previous.',
        '<a href="an-9.22.html">AN 9.22 &middot; A Wild Colt</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.22 — Khaḷuṅkasutta
# --------------------------------------------------------------------------- #
page(
    22, "Khaḷuṅka", "A Wild Colt",
    vagga=VAGGA_3,
    meta_title="AN 9.22 — A Wild Colt | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Khaḷuṅkasutta, mapping three grades of horse — wild colt, "
        "excellent horse, fine thoroughbred — each crossed against a "
        "quality of speed, beauty, and proportion, onto the path from "
        "stream-entry to arahantship. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A horse-training simile developed across three grades "
                 "of animal and person, each subdivided into three "
                 "qualities"),
        ("Length", "~4 minutes to read"),
        ("A three-by-three grid, not one list of nine", "Three grades of "
         "attainment (understanding the four noble truths, non-return, "
         "arahantship) each crossed against three qualities (fast, "
         "beautiful, well proportioned) produces this discourse's nine"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "layered simile worth tracking carefully across "
                       "its three grades"),
    ],
    why=(
        "Three wild colts, three excellent horses, and three fine "
        "thoroughbred horses are matched to three wild people, three "
        "excellent people, and three fine thoroughbred people, each "
        "grade defined by speed (spiritual attainment), beauty "
        "(answering questions about the teaching without faltering), and "
        "good proportion (receiving the four requisites) &mdash; moving "
        "from a mendicant who merely understands the four noble truths, "
        "through the non-returner, to the arahant."),
    guide=[
        ("The teaching in one sentence", [
            "Just as a horse may be fast alone, fast and beautiful, or "
            "fast, beautiful, and well proportioned, a mendicant's "
            "spiritual attainment &mdash; understanding the four noble "
            "truths, reaching non-return, or reaching arahantship "
            "&mdash; is likewise graded by whether it is joined by "
            "confident teaching and by material support from the "
            "community."]),
        ("Three grades of attainment, one shared template", [
            "Wild people understand the four noble truths; excellent "
            "people, with the five lower fetters ended, are reborn "
            "spontaneously and never return; fine thoroughbred people "
            "have realized the undefiled freedom of heart and wisdom "
            "&mdash; roughly stream-entry, non-return, and arahantship "
            "&mdash; but every grade is run through the identical "
            "three-part template of speed, beauty, and proportion."]),
        ("Speed alone is not the whole picture", [
            "Within each of the three attainment-grades, a further "
            "three-way split repeats: fast but not beautiful or well "
            "proportioned (attainment alone, without confident teaching "
            "or material support); fast and beautiful but not well "
            "proportioned (attainment plus confident teaching, but "
            "without support); and all three together. Inner attainment "
            "is necessary but, the simile insists, not by itself "
            "sufficient to complete the picture."]),
        ("A grid, not a ladder", [
            "Reading this discourse as one flat nine-item list obscures "
            "its real shape: it is a three-by-three grid, three grades "
            "of spiritual attainment each crossed against the same three "
            "qualities of speed, beauty, and proportion, giving nine "
            "combinations in total &mdash; the number this chapter is "
            "named for, reached here by multiplication rather than a "
            "single flat enumeration."]),
    ],
    terms=[
        ("khaḷuṅka",
         "&ldquo;wild colt&rdquo; &mdash; the discourse's own title "
         "image, the lowest of the three animal (and person) grades."),
        ("javena samannāgato, na vaṇṇena, na saṇṭhānena",
         "&ldquo;fast, but not beautiful or well proportioned&rdquo; "
         "&mdash; the first and most partial of the three qualities in "
         "each grade."),
        ("dhammavinayaṁ puṭṭho samāno na saṁsādeti",
         "&ldquo;when asked a question about the teaching or training, "
         "they answer without faltering&rdquo; &mdash; this discourse's "
         "own definition of &lsquo;beautiful&rsquo;."),
        ("cīvarapiṇḍapātasenāsanagilānappaccayabhesajjaparikkhāraṁ labhati",
         "&ldquo;they receive robes, almsfood, lodgings, and medicines "
         "and supplies for the sick&rdquo; &mdash; this discourse's own "
         "definition of &lsquo;well proportioned&rsquo;."),
        ("assājānīya, purisājānīya",
         "&ldquo;fine thoroughbred horse, fine thoroughbred person&rdquo; "
         "&mdash; the third and highest grade, mapped onto arahantship."),
    ],
    text_intro=(
        "The discourse in full: three grades of horse and person, each "
        "crossed against speed, beauty, and proportion. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Wild colts and wild people"),
        ("p", "&sect;1", "an9.22:1.1-2.5"),
        ("p", "&sect;2", "an9.22:3.1-4.8"),
        ("p", "&sect;3", "an9.22:5.1-6.9"),
        ("h3", "Excellent horses and excellent people"),
        ("p", "&sect;4", "an9.22:7.1-9.10"),
        ("h3", "Fine thoroughbred horses and fine thoroughbred people"),
        ("p", "&sect;5", "an9.22:10.1-12.10"),
    ],
    quiz=[
        {"q": "What three qualities does this discourse cross against "
              "each grade of horse and person?",
         "opts": [
             "Strength, endurance, and obedience",
             "Fast (spiritual attainment), beautiful (answering "
             "questions without faltering), and well proportioned "
             "(receiving the four requisites)",
             "Age, breed, and color",
             "Wealth, status, and popularity"],
         "correct": 1,
         "expl": "Attainment alone is not enough — confident teaching and "
                 "material support complete the picture."},
        {"q": "What three grades of spiritual attainment does the "
              "discourse map onto wild, excellent, and fine thoroughbred "
              "horses?",
         "opts": [
             "Three grades of monastic seniority",
             "Roughly stream-entry (understanding the four noble "
             "truths), non-return, and arahantship",
             "Three kinds of meditation posture",
             "Three levels of monastic ordination"],
         "correct": 1,
         "expl": "From understanding the truths, through non-return, to "
                 "full liberation."},
        {"q": "What does &lsquo;beautiful&rsquo; mean in this "
              "discourse's own terms?",
         "opts": [
             "Physical attractiveness",
             "Answering questions about the teaching or training without "
             "faltering",
             "Popularity among laypeople",
             "Fine robes"],
         "correct": 1,
         "expl": "Confident, capable teaching, not physical appearance."},
        {"q": "According to the guide, how should this discourse's "
              "structure actually be read?",
         "opts": [
             "As one flat list of nine unrelated items",
             "As a three-by-three grid: three grades of attainment, each "
             "crossed against the same three qualities",
             "As a single ladder with nine equal rungs",
             "As two unrelated similes stitched together"],
         "correct": 1,
         "expl": "Nine combinations reached by multiplication, not by a "
                 "single enumeration."},
        {"q": "What does the guide say the simile insists about inner "
              "attainment alone?",
         "opts": [
             "That it is entirely sufficient by itself",
             "That it is necessary but not by itself sufficient — "
             "confident teaching and material support complete the "
             "picture",
             "That it is irrelevant compared to material support",
             "That it cannot be combined with teaching ability"],
         "correct": 1,
         "expl": "A mendicant fast but not beautiful or well proportioned "
                 "still falls short of the full picture."},
        {"q": "What defines the highest grade, the fine thoroughbred "
              "person?",
         "opts": [
             "Wealth and fame",
             "Realizing the undefiled freedom of heart and wisdom, with "
             "defilements ended",
             "Physical beauty alone",
             "Seniority in the monastic order"],
         "correct": 1,
         "expl": "Full liberation, the highest of the three attainment "
                 "grades."},
    ],
    marginalia=[
        ("Three grades, one template", [
            "wild, excellent,",
            "fine thoroughbred &mdash; each crossed",
            "with speed, beauty, form",
        ]),
        ("Attainment is not enough", [
            "fast alone falls short &mdash;",
            "answer without faltering,",
            "and be well supported",
        ]),
        ("A grid, not a ladder", [
            "three times three grades &mdash;",
            "nine combinations, this",
            "chapter's own number",
        ]),
        ("Cross-references", [
            "AN 9.21 &middot; previous, In Three Particulars",
            "AN 9.23 &middot; next, Rooted in Craving",
        ]),
    ],
    further=[
        '<a href="%s/an9.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.21.html">AN 9.21 &middot; In Three Particulars</a> &mdash; previous.',
        '<a href="an-9.23.html">AN 9.23 &middot; Rooted in Craving</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.23 — Taṇhāmūlakasutta
# --------------------------------------------------------------------------- #
page(
    23, "Taṇhāmūlaka", "Rooted in Craving",
    vagga=VAGGA_3,
    meta_title="AN 9.23 — Rooted in Craving | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Taṇhāmūlakasutta, tracing nine things rooted in craving in an "
        "unbroken causal chain from searching through ownership and "
        "stinginess to violence and lies. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single unbroken causal chain of nine links, each "
                 "giving rise to the next"),
        ("Length", "~1 minute to read"),
        ("A chain, like AN 9.14, not a parallel list", "Each of the nine "
         "things gives rise to the next in sequence, the same chain-"
         "structure already met at AN 9.14, tracing craving's social and "
         "behavioral consequences rather than its subjective ones"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "compact but socially pointed causal sequence"),
    ],
    why=(
        "Craving gives rise to searching, searching to gaining material "
        "things, gaining to evaluation, evaluation to desire and lust, "
        "desire and lust to attachment, attachment to ownership, "
        "ownership to stinginess, and stinginess to safeguarding "
        "&mdash; and safeguarding in turn gives rise to violence, "
        "quarrels, disputes, accusations, backbiting, and lies."),
    guide=[
        ("The teaching in one sentence", [
            "Nine things rooted in craving unfold in an unbroken chain: "
            "craving gives rise to searching, then gaining, evaluation, "
            "desire and lust, attachment, ownership, stinginess, and "
            "safeguarding &mdash; and safeguarding gives rise to taking "
            "up the rod and the sword, quarrels, arguments, disputes, "
            "accusations, backbiting, and lies."]),
        ("A second chain, this time social", [
            "Like AN 9.14's chain from name and form to freedom from "
            "death, this discourse traces an unbroken sequence rather "
            "than a parallel list &mdash; but where AN 9.14 traced an "
            "individual's path toward liberation, this chain traces "
            "craving's outward, social consequences: possession, "
            "jealousy, and eventually open conflict."]),
        ("From an inner state to violence between people", [
            "The chain's middle links &mdash; evaluation, desire and "
            "lust, attachment, ownership &mdash; stay internal to the "
            "person doing the craving. But once ownership produces "
            "stinginess and stinginess produces safeguarding, the "
            "consequences turn outward and interpersonal: the discourse "
            "names the rod and the sword, quarrels, and outright lies as "
            "craving's final, fully socialized fruit."]),
        ("Nine links traced back to one root", [
            "Every one of the nine things named here, however far "
            "downstream from the original craving, is still described "
            "as &lsquo;rooted in craving&rsquo; &mdash; the discourse's "
            "own title and framing insist that even open violence and "
            "lying, several links removed, trace back to the same single "
            "root the discourse opens with."]),
    ],
    terms=[
        ("taṇhā pariyesanaṁ janeti",
         "&ldquo;craving gives rise to searching&rdquo; &mdash; the "
         "chain's opening link."),
        ("lābho vinicchayaṁ janeti",
         "&ldquo;gaining material things gives rise to evaluation&rdquo; "
         "&mdash; the third link, where acquisition begins producing "
         "judgment and comparison."),
        ("ajjhosānaṁ pariggahaṁ janeti",
         "&ldquo;attachment gives rise to ownership&rdquo; &mdash; the "
         "point where an internal state first becomes a claim."),
        ("macchariyaṁ ārakkhaṁ janeti",
         "&ldquo;stinginess gives rise to safeguarding&rdquo; &mdash; "
         "the eighth link, where craving's consequences turn outward "
         "and defensive."),
        ("daṇḍādānasatthādānaṁ",
         "&ldquo;taking up the rod and the sword&rdquo; &mdash; the "
         "first and most severe of safeguarding's own bad, unskillful "
         "consequences."),
    ],
    text_intro=(
        "The discourse in full: nine things rooted in craving, traced in "
        "an unbroken causal chain. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Nine things, one chain"),
        ("p", "&sect;1", "an9.23:1.1-1.4"),
    ],
    quiz=[
        {"q": "How is this discourse structured?",
         "opts": [
             "As nine parallel, unrelated items",
             "As a single unbroken causal chain, each link giving rise "
             "to the next",
             "As a debate between two disciples",
             "As three groups of three"],
         "correct": 1,
         "expl": "The same chain-structure already met at AN 9.14, "
                 "applied here to craving's social consequences."},
        {"q": "What does craving give rise to first in this chain?",
         "opts": [
             "Ownership", "Searching",
             "Stinginess", "Violence"],
         "correct": 1,
         "expl": "The chain's opening link."},
        {"q": "What does ownership give rise to, continuing the chain?",
         "opts": [
             "Generosity", "Stinginess",
             "Wisdom", "Contentment"],
         "correct": 1,
         "expl": "Possessiveness turning into guarding what is owned "
                 "against others."},
        {"q": "What final consequences does safeguarding give rise to?",
         "opts": [
             "Peace and contentment",
             "Taking up the rod and the sword, quarrels, disputes, "
             "accusations, backbiting, and lies",
             "Renunciation of all possessions",
             "A return to searching"],
         "correct": 1,
         "expl": "Craving's fully socialized, interpersonal fruit."},
        {"q": "According to the guide, how does this chain compare to AN "
              "9.14's chain?",
         "opts": [
             "They are identical in content",
             "Both are unbroken chains rather than parallel lists, but "
             "this one traces craving's social consequences rather than "
             "an individual's path toward liberation",
             "This chain has no relationship to AN 9.14",
             "AN 9.14 is a chain; this discourse is a simple list"],
         "correct": 1,
         "expl": "Same chain-structure, opposite direction and subject "
                 "matter."},
        {"q": "What does the discourse's own title and framing insist "
              "about all nine things named?",
         "opts": [
             "That they are unrelated to one another",
             "That every one, however far downstream, is still rooted "
             "in the same original craving",
             "That only the first three are rooted in craving",
             "That craving is irrelevant to the later links"],
         "correct": 1,
         "expl": "Even open violence and lying trace back to one root."},
    ],
    marginalia=[
        ("A chain, nine links", [
            "craving to searching,",
            "gain, evaluation, desire,",
            "attachment, ownership",
        ]),
        ("Outward, and dangerous", [
            "stinginess to guarding &mdash;",
            "guarding to the rod,",
            "the sword, and open lies",
        ]),
        ("One root, however far", [
            "every link downstream,",
            "however socialized,",
            "traced to craving still",
        ]),
        ("Cross-references", [
            "AN 9.14 &middot; the same chain-structure, a different "
            "subject and direction",
            "AN 9.22 &middot; previous, A Wild Colt",
            "AN 9.24 &middot; next, Abodes of Sentient Beings",
        ]),
    ],
    further=[
        '<a href="%s/an9.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.22.html">AN 9.22 &middot; A Wild Colt</a> &mdash; previous.',
        '<a href="an-9.24.html">AN 9.24 &middot; Abodes of Sentient Beings</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.24 — Sattāvāsasutta — this chapter's own namesake
# --------------------------------------------------------------------------- #
page(
    24, "Sattāvāsa", "Abodes of Sentient Beings",
    vagga=VAGGA_3,
    meta_title="AN 9.24 — Abodes of Sentient Beings | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sattāvāsasutta, this chapter's own namesake — a classic ninefold "
        "cosmology of body and perception, extending AN 7.44's seven "
        "stations of consciousness by two further abodes. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare cosmological list, nine abodes each named "
                 "with its own defining pair of qualities"),
        ("Length", "~2 minutes to read"),
        ("This chapter's own namesake, and a known extension", "This "
         "discourse names the entire chapter; its nine abodes extend AN "
         "7.44's seven stations of consciousness by two further items"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "dense cosmological catalogue, worth reading "
                       "alongside AN 7.44 for the comparison"),
    ],
    why=(
        "Nine abodes of sentient beings are catalogued by two crossed "
        "qualities, diversity or unity of body and of perception, moving "
        "from ordinary embodied beings through the beings of the "
        "absorptions to those non-percipient, then through the four "
        "formless dimensions ending at neither perception nor non-"
        "perception."),
    guide=[
        ("The teaching in one sentence", [
            "Sentient beings inhabit nine abodes: diverse in body and "
            "perception (humans and some gods); diverse in body, unified "
            "in perception; unified in body, diverse in perception; "
            "unified in both; non-percipient beings who experience "
            "nothing; and the four formless dimensions culminating in "
            "neither perception nor non-perception."]),
        ("This chapter's own namesake", [
            "As with every chapter opener elsewhere in this project, "
            "this discourse lends its own subject &mdash; "
            "<em>sattāvāsa</em>, abodes of sentient beings &mdash; to "
            "the chapter's name, <em>Sattāvāsavagga</em>, though it "
            "falls fourth rather than first within the chapter itself."]),
        ("Four abodes built from a crossed pair of qualities", [
            "The first four abodes are generated by crossing two "
            "binary qualities, diversity or unity of body and of "
            "perception: humans and some gods are diverse in both; the "
            "gods of the Divinity's host reborn through the first "
            "absorption are diverse in body but unified in perception; "
            "the gods of streaming radiance are unified in body but "
            "diverse in perception; and the gods of universal beauty are "
            "unified in both."]),
        ("Extending AN 7.44's seven stations by two", [
            "This discourse's first four abodes plus its final four "
            "formless dimensions match AN 7.44's seven stations of "
            "consciousness almost exactly &mdash; but AN 7.44 covered "
            "only seven, omitting the non-percipient beings and the "
            "dimension of neither perception nor non-perception. This "
            "discourse's ninefold scheme restores both, giving a fuller "
            "and more complete cosmological catalogue than the sevenfold "
            "version met earlier in this project."]),
    ],
    terms=[
        ("sattāvāsā",
         "&ldquo;abodes of sentient beings&rdquo; &mdash; this "
         "discourse's own title term and the name it lends to the "
         "entire chapter."),
        ("nānattakāyā nānattasaññino",
         "&ldquo;diverse in body and diverse in perception&rdquo; "
         "&mdash; the first abode, describing humans and some gods and "
         "beings in the underworld."),
        ("asaññasattā",
         "&ldquo;non-percipient beings&rdquo; &mdash; the fifth abode, "
         "beings who do not experience anything at all, one of the two "
         "items absent from AN 7.44's sevenfold version."),
        ("ākāsānañcāyatanūpagā devā",
         "&ldquo;reborn in the dimension of infinite space&rdquo; "
         "&mdash; the sixth abode, the first of the four formless "
         "dimensions."),
        ("nevasaññānāsaññāyatanūpagā",
         "&ldquo;the dimension of neither perception nor non-"
         "perception&rdquo; &mdash; the ninth and final abode, the other "
         "item absent from AN 7.44's sevenfold version."),
    ],
    text_intro=(
        "The discourse in full: nine abodes of sentient beings, "
        "catalogued by crossed qualities of body and perception. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine abodes"),
        ("p", "&sect;1", "an9.24:1.1-10.1"),
    ],
    quiz=[
        {"q": "What two qualities are crossed to generate this "
              "discourse's first four abodes?",
         "opts": [
             "Height and weight",
             "Diversity or unity of body, and diversity or unity of "
             "perception",
             "Wealth and poverty",
             "Age and lifespan"],
         "correct": 1,
         "expl": "Four combinations from two binary qualities."},
        {"q": "What does this discourse name its own chapter?",
         "opts": [
             "Nothing; it doesn't relate to the chapter title",
             "<em>Sattāvāsavagga</em>, though this discourse falls fourth "
             "in the chapter rather than first",
             "It names the chapter after Uttarakuru",
             "It names the chapter after craving"],
         "correct": 1,
         "expl": "This chapter's own namesake, unusually placed fourth "
                 "rather than as the opener."},
        {"q": "What are the fifth abode's beings like?",
         "opts": [
             "Beings of extraordinary beauty",
             "Non-percipient beings who do not experience anything at "
             "all",
             "Beings diverse in body only",
             "Beings unified in perception only"],
         "correct": 1,
         "expl": "One of the two items this ninefold scheme adds beyond "
                 "AN 7.44's sevenfold version."},
        {"q": "According to the guide, how does this discourse's ninefold "
              "scheme relate to AN 7.44's seven stations of "
              "consciousness?",
         "opts": [
             "They are entirely unrelated lists",
             "This scheme extends AN 7.44's seven stations by two "
             "further items: non-percipient beings and the dimension of "
             "neither perception nor non-perception",
             "This scheme is a shorter version of AN 7.44's list",
             "AN 7.44 has more items than this discourse"],
         "correct": 1,
         "expl": "A fuller, nine-item cosmological catalogue compared to "
                 "the earlier sevenfold version."},
        {"q": "What is the ninth and final abode named?",
         "opts": [
             "The dimension of infinite space",
             "The dimension of neither perception nor non-perception",
             "The dimension of nothingness",
             "The realm of universal beauty"],
         "correct": 1,
         "expl": "The most subtle of the four formless dimensions, "
                 "closing the ninefold list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare cosmological catalogue, without narrative "
                 "frame."},
    ],
    marginalia=[
        ("Four abodes, crossed qualities", [
            "diverse or unified &mdash;",
            "body and perception,",
            "crossed to make four kinds",
        ]),
        ("Non-percipient, and beyond", [
            "beings who feel nothing,",
            "then space, consciousness,",
            "nothingness, and neither",
        ]),
        ("Extending an earlier list", [
            "AN 7.44's seven",
            "stations, now made nine &mdash;",
            "two abodes restored",
        ]),
        ("Cross-references", [
            "AN 7.44 &middot; the earlier sevenfold version this "
            "discourse extends",
            "AN 9.23 &middot; previous, Rooted in Craving",
            "AN 9.25 &middot; next, Consolidated by Wisdom",
        ]),
    ],
    further=[
        '<a href="%s/an9.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.23.html">AN 9.23 &middot; Rooted in Craving</a> &mdash; previous.',
        '<a href="an-9.25.html">AN 9.25 &middot; Consolidated by Wisdom</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.25 — Paññāsutta
# --------------------------------------------------------------------------- #
page(
    25, "Paññā", "Consolidated by Wisdom",
    vagga=VAGGA_3,
    meta_title="AN 9.25 — Consolidated by Wisdom | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paññāsutta, naming nine kinds of self-knowledge that justify a "
        "mendicant's declaration of full awakening — the same nine "
        "framed by wisdom here and by heart at AN 9.26. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A declaration formula, then nine specific kinds of "
                 "self-knowledge that justify making it"),
        ("Length", "~1 minute to read"),
        ("The same nine as AN 9.26, framed differently", "This "
         "discourse's nine items of self-knowledge, framed here as a "
         "mind &lsquo;consolidated with wisdom,&rsquo; reappear at AN "
         "9.26 framed instead as a mind &lsquo;consolidated by "
         "heart&rsquo;"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "precise formula, best compared directly with AN "
                       "9.26"),
    ],
    why=(
        "A mendicant whose mind is well consolidated with wisdom may "
        "rightly declare themselves free of further rebirth, and this "
        "consolidation is defined by nine specific items of self-"
        "knowledge: freedom from greed, hate, and delusion; freedom from "
        "any tendency to return to them; and freedom from any tendency "
        "to be reborn in the sensual, form, or formless realms."),
    guide=[
        ("The teaching in one sentence", [
            "When a mendicant knows &lsquo;my mind is without greed, "
            "hate, delusion,&rsquo; &lsquo;my mind is not liable to "
            "become greedy, hateful, deluded,&rsquo; and &lsquo;my mind "
            "is not liable to return to rebirth in the sensual, form, or "
            "formless realm,&rsquo; their mind is well consolidated with "
            "wisdom, and it's appropriate for them to declare rebirth "
            "ended."]),
        ("Nine items, three groups of three", [
            "The nine items of self-knowledge fall into three clean "
            "groups: present freedom from the three roots (greed, hate, "
            "delusion); assurance against any future return of those "
            "same three roots; and assurance against rebirth in any of "
            "the three realms of existence &mdash; sensual, form, and "
            "formless."]),
        ("Present state and future assurance, not just one moment", [
            "The formula doesn't stop at describing the mind's current "
            "condition. The middle three items shift explicitly to the "
            "future tense &mdash; not liable to become greedy again, not "
            "liable to become hateful again &mdash; distinguishing a "
            "settled, permanent freedom from what might be only a "
            "temporary calm."]),
        ("Wisdom here; the same nine by heart at AN 9.26", [
            "This discourse frames its nine items as what makes a mind "
            "&lsquo;well consolidated with wisdom&rsquo; "
            "(paññāya suvimuttacittaṁ). The very next discourse, AN 9.26, "
            "gives the identical nine items but frames them instead as "
            "what makes a mind &lsquo;well consolidated by heart&rsquo; "
            "&mdash; the same content under two different framings, "
            "clarified there through a famous correction of a "
            "misquotation."]),
    ],
    terms=[
        ("khīṇā jāti, vusitaṁ brahmacariyaṁ",
         "&ldquo;rebirth is ended, the spiritual journey has been "
         "completed&rdquo; &mdash; the arahant's declaration formula "
         "this discourse's nine items justify making."),
        ("suparimuṭṭhacittaṁ paññāya",
         "&ldquo;well consolidated with wisdom&rdquo; &mdash; this "
         "discourse's own framing for the nine-item formula, contrasted "
         "with AN 9.26's &lsquo;consolidated by heart&rsquo;."),
        ("vītarāgaṁ me cittanti pajānāti",
         "&ldquo;my mind is without greed&rdquo; &mdash; the first of "
         "the nine items, naming present freedom from the first of the "
         "three roots."),
        ("na rāgadhammaṁ",
         "&ldquo;not liable to become greedy&rdquo; &mdash; the fourth "
         "item, shifting from present state to future assurance."),
        ("nāparaṁ itthattāyāti pajānāti",
         "&ldquo;there is nothing further for this place&rdquo; &mdash; "
         "the closing phrase of the declaration formula this discourse "
         "justifies."),
    ],
    text_intro=(
        "The discourse in full: the declaration formula, and nine items "
        "of self-knowledge that justify making it. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A declaration, and what justifies it"),
        ("p", "&sect;1", "an9.25:1.1-1.2"),
        ("h3", "Nine items of self-knowledge"),
        ("p", "&sect;2", "an9.25:2.1-2.12"),
    ],
    quiz=[
        {"q": "What declaration does this discourse's nine items justify "
              "making?",
         "opts": [
             "A vow of future practice",
             "&lsquo;Rebirth is ended, the spiritual journey has been "
             "completed, what had to be done has been done&rsquo;",
             "A confession of wrongdoing",
             "A request for ordination"],
         "correct": 1,
         "expl": "The standard arahant's declaration formula."},
        {"q": "How do the nine items of self-knowledge group together?",
         "opts": [
             "Nine unrelated, scattered claims",
             "Three groups of three: freedom from the three roots, "
             "assurance against their future return, and assurance "
             "against rebirth in the three realms",
             "One group of nine identical statements",
             "Five items, then four unrelated ones"],
         "correct": 1,
         "expl": "A cleanly structured formula, not a loose list."},
        {"q": "What shift happens in the formula's middle three items?",
         "opts": [
             "A shift to a different topic entirely",
             "A shift from describing the mind's present state to a "
             "future-tense assurance it won't return to greed, hate, or "
             "delusion",
             "A shift to a different speaker",
             "A shift to poetic verse"],
         "correct": 1,
         "expl": "Distinguishing settled freedom from merely temporary "
                 "calm."},
        {"q": "What three realms does the formula's final group of three "
              "items name assurance against?",
         "opts": [
             "Hell, the animal realm, and the ghost realm",
             "The sensual realm, the realm of luminous form, and the "
             "formless realm",
             "Three human kingdoms",
             "Three heavens only"],
         "correct": 1,
         "expl": "The three realms of existence in Buddhist cosmology."},
        {"q": "According to the guide, how does this discourse's "
              "framing compare to AN 9.26's?",
         "opts": [
             "They present entirely different content",
             "The identical nine items are framed here as a mind "
             "&lsquo;consolidated with wisdom&rsquo; and at AN 9.26 as "
             "&lsquo;consolidated by heart&rsquo;",
             "AN 9.26 has twice as many items",
             "This discourse has no connection to AN 9.26"],
         "correct": 1,
         "expl": "Same content, two different framings, worth reading "
                 "side by side."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, unlike AN 9.26 immediately after it."},
    ],
    marginalia=[
        ("Nine items, three groups", [
            "free of greed, hate,",
            "delusion; not liable",
            "to their return; nor to rebirth",
        ]),
        ("Present state, future assurance", [
            "&ldquo;my mind is without&rdquo; &mdash;",
            "then &ldquo;not liable to become&rdquo; &mdash;",
            "settled, not momentary",
        ]),
        ("Wisdom here, heart next", [
            "the same nine items,",
            "consolidated by wisdom &mdash;",
            "by heart, at AN 9.26",
        ]),
        ("Cross-references", [
            "AN 9.24 &middot; previous, Abodes of Sentient Beings",
            "AN 9.26 &middot; next, the same nine items framed by heart",
        ]),
    ],
    further=[
        '<a href="%s/an9.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.24.html">AN 9.24 &middot; Abodes of Sentient Beings</a> &mdash; previous.',
        '<a href="an-9.26.html">AN 9.26 &middot; The Simile of the Stone Post</a> '
        "&mdash; next, the same nine items framed by heart.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.26 — Indriyabhāvanāsutta / Silāyūpasutta (the Stone Post simile)
# --------------------------------------------------------------------------- #
page(
    26, "Silāyūpa", "The Simile of the Stone Post",
    vagga=VAGGA_3,
    meta_title="AN 9.26 — The Simile of the Stone Post | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Simile of the Stone Post, in which Sāriputta corrects a "
        "mendicant's threefold misquotation of Devadatta before giving "
        "the same nine items as AN 9.25, framed by heart, and a famous "
        "simile of an unshakeable mind. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, in the Bamboo Grove, the squirrels' "
                    "feeding ground"),
        ("Speakers", "Venerable Candikāputta, Venerable Sāriputta, and, "
                     "by report, Devadatta"),
        ("Form", "A threefold correction of a misquotation, then the "
                 "same nine-item formula as AN 9.25, then the stone-post "
                 "simile extended across all six sense doors"),
        ("Length", "~4 minutes to read"),
        ("A misquotation, corrected three times", "Candikāputta "
         "misreports Devadatta's own teaching by a single word, and is "
         "corrected identically three times before the full teaching is "
         "given"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "rich narrative wrapped around a precise formula "
                       "and a memorable simile"),
    ],
    why=(
        "Candikāputta reports Devadatta as teaching that a mind "
        "&lsquo;solidified by heart&rsquo; justifies the arahant's "
        "declaration; Sāriputta corrects him three times, insisting "
        "Devadatta actually says &lsquo;well consolidated by "
        "heart&rsquo; &mdash; then gives the same nine items of self-"
        "knowledge as AN 9.25, framed by heart rather than wisdom, and "
        "closes with the simile of a deeply embedded stone post, "
        "unmoved by storms from every direction."),
    guide=[
        ("The teaching in one sentence", [
            "A mind well consolidated by heart &mdash; knowing itself "
            "free of greed, hate, and delusion, and free of any tendency "
            "to return to them or to rebirth in any of the three realms "
            "&mdash; remains untainted, steady, and imperturbable even "
            "when compelling sights, sounds, smells, tastes, touches, or "
            "ideas come into its range, like a deeply embedded stone "
            "post unmoved by storms from every direction."]),
        ("A single word, corrected three times", [
            "Candikāputta reports Devadatta's teaching using the word "
            "&lsquo;solidified&rsquo; (a term suggesting rigidity); "
            "Sāriputta corrects him, insisting the actual word is "
            "&lsquo;well consolidated&rsquo; &mdash; and when "
            "Candikāputta repeats the same misquotation twice more, "
            "Sāriputta corrects him identically each time, a threefold "
            "insistence on precision echoing the threefold structure "
            "already met in Meghiya's threefold request at AN 9.3."]),
        ("The same nine items as AN 9.25, framed by heart", [
            "Once the correction is settled, Sāriputta gives the "
            "identical nine-item formula met at AN 9.25 &mdash; freedom "
            "from greed, hate, and delusion; assurance against their "
            "return; assurance against rebirth in the three realms "
            "&mdash; but frames it here as consolidation &lsquo;by "
            "heart&rsquo; (cetasā) rather than AN 9.25's "
            "&lsquo;with wisdom&rsquo; (paññāya), demonstrating that the "
            "same liberating self-knowledge can be described through "
            "either register."]),
        ("A stone post, and six sense doors", [
            "The discourse's famous close extends the formula's "
            "consequence into a concrete image: a stone post, sixteen "
            "feet long with half buried and half above ground, unmoved "
            "by violent storms from all four directions because of its "
            "deep foundation. The same imperturbability is then traced "
            "through all six sense doors in turn &mdash; sights, sounds, "
            "smells, tastes, touches, and ideas &mdash; none of which "
            "can occupy a mind rightly freed like this."]),
    ],
    terms=[
        ("ṭhitaṁ cittaṁ",
         "&ldquo;solidified mind&rdquo; &mdash; Candikāputta's own "
         "misquotation of Devadatta's teaching, corrected three times by "
         "Sāriputta."),
        ("suvimuttacittaṁ",
         "&ldquo;well consolidated mind&rdquo; &mdash; Sāriputta's "
         "insistent correction, the actual word he attributes to "
         "Devadatta."),
        ("cetasā suvimuttaṁ",
         "&ldquo;well consolidated by heart&rdquo; &mdash; this "
         "discourse's own framing for the nine-item formula, compared "
         "with AN 9.25's &lsquo;consolidated with wisdom&rsquo;."),
        ("asamphuṭṭhaṁyeva cittaṁ hoti",
         "&ldquo;they don't occupy their mind&rdquo; &mdash; what "
         "compelling sights, sounds, and other sense objects fail to do "
         "to a mind rightly freed."),
        ("silāyūpo soḷasakukkuko",
         "&ldquo;a stone post, sixteen feet long&rdquo; &mdash; the "
         "discourse's own title image, unmoved by storms from every "
         "direction because of its deep foundation."),
    ],
    text_intro=(
        "The discourse in full: a threefold correction of a "
        "misquotation, the nine-item formula framed by heart, and the "
        "stone-post simile extended across all six sense doors. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A misquotation, corrected three times"),
        ("p", "&sect;1", "an9.26:1.1-1.6"),
        ("p", "&sect;2", "an9.26:2.1-2.7"),
        ("p", "&sect;3", "an9.26:4.1-4.11"),
        ("h3", "Nine items, consolidated by heart"),
        ("p", "&sect;4", "an9.26:5.1-5.12"),
        ("h3", "The stone post, and six sense doors"),
        ("p", "&sect;5", "an9.26:6.1-6.10"),
        ("p", "&sect;6", "an9.26:7.1-7.6"),
    ],
    quiz=[
        {"q": "What single word does Candikāputta get wrong when "
              "reporting Devadatta's teaching?",
         "opts": [
             "He says &lsquo;solidified&rsquo; where Sāriputta insists "
             "on &lsquo;well consolidated&rsquo;",
             "He names the wrong teacher entirely",
             "He gets the number of items wrong",
             "He reports the opposite meaning entirely"],
         "correct": 0,
         "expl": "A single-word correction, insisted on three times."},
        {"q": "How many times does Sāriputta correct the same "
              "misquotation?",
         "opts": [
             "Once", "Twice", "Three times", "Four times"],
         "correct": 2,
         "expl": "A threefold structure echoing Meghiya's threefold "
                 "request at AN 9.3."},
        {"q": "How does this discourse's nine-item formula relate to AN "
              "9.25's?",
         "opts": [
             "It is an entirely different formula",
             "It is the identical nine items, framed here as "
             "consolidation &lsquo;by heart&rsquo; rather than AN 9.25's "
             "&lsquo;with wisdom&rsquo;",
             "It has only five items",
             "It adds four new items to AN 9.25's list"],
         "correct": 1,
         "expl": "Same content, a different framing register."},
        {"q": "What does the stone-post simile illustrate?",
         "opts": [
             "The impermanence of all things",
             "A mind rightly freed, remaining untainted, steady, and "
             "imperturbable when compelling sense objects come into its "
             "range, like a deeply embedded post unmoved by storms",
             "The importance of physical strength",
             "The dangers of pride"],
         "correct": 1,
         "expl": "A concrete image for the nine-item formula's practical "
                 "consequence."},
        {"q": "Across how many sense doors is the stone-post "
              "imperturbability traced?",
         "opts": [
             "Three", "Four", "Five", "Six (sights, sounds, smells, "
             "tastes, touches, and ideas)"],
         "correct": 3,
         "expl": "All six sense doors, extending the simile's reach "
                 "fully."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, in the Bamboo Grove, the squirrels' feeding "
             "ground",
             "Cālikā, on the Cālikā mountain",
             "Vesālī"],
         "correct": 1,
         "expl": "A different setting from most of this chapter's other "
                 "discourses."},
    ],
    marginalia=[
        ("A word, corrected thrice", [
            "not &lsquo;solidified&rsquo; &mdash;",
            "&lsquo;well consolidated&rsquo; &mdash;",
            "insisted three times",
        ]),
        ("The same nine, by heart", [
            "free of greed, hate,",
            "delusion, and their return &mdash;",
            "wisdom's twin, by heart",
        ]),
        ("A stone post, unmoved", [
            "eight feet buried, eight",
            "above &mdash; no storm from any",
            "direction shakes it",
        ]),
        ("Cross-references", [
            "AN 9.25 &middot; previous, the same nine items framed by "
            "wisdom",
            "AN 9.27 &middot; next, Fears and Enmities (1st)",
        ]),
    ],
    further=[
        '<a href="%s/an9.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.25.html">AN 9.25 &middot; Consolidated by Wisdom</a> &mdash; previous, '
        "the same nine items framed by wisdom.",
        '<a href="an-9.27.html">AN 9.27 &middot; Fears and Enmities (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.27 — Bhayasutta (1st)
# --------------------------------------------------------------------------- #
page(
    27, "Bhaya", "Fears and Enmities (1st)",
    vagga=VAGGA_3,
    meta_title="AN 9.27 — Fears and Enmities (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "first Bhayasutta, addressed personally to Anāthapiṇḍika — the "
        "classic stream-entry formula of five quelled fears and four "
        "factors of confidence, totaling this chapter's own nine. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue in the same "
                    "general setting as the chapter"),
        ("Speakers", "The Buddha, addressing the householder "
                     "Anāthapiṇḍika personally"),
        ("Form", "A declaration formula, then five quelled fears drawn "
                 "from the five precepts, then four factors of "
                 "confidence"),
        ("Length", "~3 minutes to read"),
        ("Five plus four equals this chapter's nine", "Five fears and "
         "enmities quelled through ethical restraint, plus four factors "
         "of confidence in the Buddha, teaching, Saṅgha, and ethics, "
         "totals the nine this chapter is named for"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; one "
                       "of the most famous formulas in the early "
                       "discourses, worth knowing well"),
    ],
    why=(
        "Addressing Anāthapiṇḍika by name, the Buddha explains that a "
        "noble disciple who has quelled five fears and enmities "
        "&mdash; by refraining from killing, stealing, sexual "
        "misconduct, lying, and intoxicants &mdash; and possesses four "
        "factors of stream-entry &mdash; confidence in the Buddha, the "
        "teaching, the Saṅgha, and their own ethical conduct &mdash; may "
        "rightly declare themselves a stream-enterer, assured and "
        "destined for awakening."),
    guide=[
        ("The teaching in one sentence", [
            "A noble disciple who has quelled the five fears and "
            "enmities that come from killing, stealing, sexual "
            "misconduct, lying, and intoxicants, and who possesses "
            "experiential confidence in the Buddha, the teaching, the "
            "Saṅgha, and their own unbroken ethical conduct, may rightly "
            "declare themselves a stream-enterer, finished with any "
            "further rebirth in a bad place."]),
        ("Five fears, quelled by the five precepts", [
            "Each of the five fears follows an identical logic: anyone "
            "who kills, steals, commits sexual misconduct, lies, or "
            "drinks intoxicants brims with fear and enmity, both now and "
            "in future lives, and suffers mental pain; anyone who "
            "refrains does not. The familiar five precepts are reframed "
            "here not as external rules but as the direct removal of a "
            "specific, nameable fear."]),
        ("Four factors, naming what a stream-enterer trusts", [
            "The four factors of stream-entry name experiential "
            "confidence, not mere belief, in the Buddha (recited through "
            "his standard qualities), the teaching (well explained, "
            "apparent, inviting inspection), and the Saṅgha (practicing "
            "well, worthy of offerings), plus a noble disciple's own "
            "ethical conduct, described as loved by the noble ones and "
            "leading to immersion."]),
        ("Nine total, and a personal address", [
            "Five quelled fears plus four factors of confidence gives "
            "exactly the nine this chapter is named for &mdash; but "
            "unlike most nine-item formulas in this nipāta, this "
            "discourse is addressed to a specific, named individual, "
            "Anāthapiṇḍika, the Buddha's most famous lay donor, rather "
            "than to the mendicants in general as at AN 9.28, its near-"
            "identical twin."]),
    ],
    terms=[
        ("pañca bhayāni verāni vūpasantāni",
         "&ldquo;five fears and enmities... quelled&rdquo; &mdash; the "
         "discourse's own title phrase, naming the consequence of "
         "ethical restraint."),
        ("cattāri ca sotāpattiyaṅgāni",
         "&ldquo;the four factors of stream-entry&rdquo; &mdash; the "
         "second half of this discourse's nine, naming confidence rather "
         "than restraint."),
        ("aveccappasāda",
         "&ldquo;experiential confidence&rdquo; &mdash; the quality of "
         "trust named for the Buddha, the teaching, and the Saṅgha, "
         "distinguished from mere belief."),
        ("cattāri pāripūrā, aṭṭha puggalā",
         "&ldquo;the four pairs, the eight individual persons&rdquo; "
         "&mdash; part of the confidence formula for the Saṅgha, the "
         "same eightfold classification met at AN 9.9."),
        ("khīṇanirayo... sotāpanno",
         "&ldquo;finished with rebirth in hell... I am a stream-"
         "enterer&rdquo; &mdash; the declaration this discourse's nine "
         "items justify making."),
    ],
    text_intro=(
        "The discourse in full: a declaration formula, five fears "
        "quelled through the five precepts, and four factors of "
        "confidence. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A declaration, addressed to Anāthapiṇḍika"),
        ("p", "&sect;1", "an9.27:1.1-2.2"),
        ("h3", "Five fears, quelled"),
        ("p", "&sect;2", "an9.27:3.1-5.1"),
        ("h3", "Four factors of confidence"),
        ("p", "&sect;3", "an9.27:6.1-10.2"),
    ],
    quiz=[
        {"q": "To whom is this discourse addressed, and how does that "
              "make it distinctive?",
         "opts": [
             "To the mendicants in general, like most discourses in this "
             "chapter",
             "Personally to the householder Anāthapiṇḍika, unlike its "
             "near-identical twin AN 9.28",
             "To a wanderer of another religion",
             "To a group of deities"],
         "correct": 1,
         "expl": "A personal address, distinguishing it from AN 9.28's "
                 "general one."},
        {"q": "What five fears does this discourse say are quelled by "
              "ethical restraint?",
         "opts": [
             "Fear of the dark, animals, storms, illness, old age",
             "Fears arising from killing, stealing, sexual misconduct, "
             "lying, and consuming intoxicants",
             "The five hindrances",
             "Fear of five specific deities"],
         "correct": 1,
         "expl": "The five precepts, reframed as direct removal of "
                 "nameable fears."},
        {"q": "What four factors of stream-entry does the discourse "
              "name?",
         "opts": [
             "Wisdom, energy, mindfulness, and immersion",
             "Experiential confidence in the Buddha, the teaching, the "
             "Saṅgha, and one's own ethical conduct",
             "The four noble truths",
             "The four right efforts"],
         "correct": 1,
         "expl": "Confidence and conduct, not meditative attainment."},
        {"q": "How does this discourse's nine items relate to the "
              "chapter's own number?",
         "opts": [
             "They have no connection to the number nine",
             "Five quelled fears plus four factors of confidence gives "
             "exactly nine",
             "There are only seven items total",
             "The nine items are unrelated to each other"],
         "correct": 1,
         "expl": "A clean five-plus-four structure reaching this "
                 "chapter's nine."},
        {"q": "What declaration may a noble disciple with these nine "
              "make?",
         "opts": [
             "A vow of silence",
             "That they are a stream-enterer, finished with rebirth in "
             "hell, the animal realm, and the ghost realm, and assured "
             "of awakening",
             "A request to become a monastic",
             "A claim to full awakening as an arahant"],
         "correct": 1,
         "expl": "Stream-entry specifically, not the higher fruits."},
        {"q": "What is named as part of the confidence in the Saṅgha?",
         "opts": [
             "Its wealth and buildings",
             "The four pairs, the eight individual persons — the same "
             "classification met at AN 9.9",
             "Its size and popularity",
             "Its age and history"],
         "correct": 1,
         "expl": "A cross-reference to the eightfold noble Saṅgha "
                 "formula met earlier in this nipāta."},
    ],
    marginalia=[
        ("Five fears, five precepts", [
            "no killing, stealing,",
            "misconduct, lying, drink &mdash;",
            "each fear quelled in turn",
        ]),
        ("Four factors of confidence", [
            "the Buddha, the teaching,",
            "the Saṅgha, and one's own",
            "unbroken ethical conduct",
        ]),
        ("Nine, and a named address", [
            "five plus four is nine &mdash;",
            "spoken to Anāthapiṇḍika",
            "himself, by name",
        ]),
        ("Cross-references", [
            "AN 9.9 &middot; the same &ldquo;four pairs, eight "
            "individuals&rdquo; Saṅgha formula",
            "AN 9.26 &middot; previous, The Simile of the Stone Post",
            "AN 9.28 &middot; next, the same formula addressed to "
            "mendicants in general",
        ]),
    ],
    further=[
        '<a href="%s/an9.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.26.html">AN 9.26 &middot; The Simile of the Stone Post</a> '
        "&mdash; previous.",
        '<a href="an-9.28.html">AN 9.28 &middot; Fears and Enmities (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.28 — Bhayasutta (2nd)
# --------------------------------------------------------------------------- #
page(
    28, "Bhaya", "Fears and Enmities (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 9.28 — Fears and Enmities (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "second Bhayasutta, the same five-fears-plus-four-factors "
        "stream-entry formula as AN 9.27, addressed here to the "
        "mendicants generally rather than to Anāthapiṇḍika by name. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical formula as AN 9.27, without the earlier "
                 "discourse's narrative frame"),
        ("Length", "~2 minutes to read"),
        ("A twin discourse, distinguished only by audience", "The "
         "content is identical to AN 9.27; the only real difference is "
         "that this version drops the personal address to Anāthapiṇḍika "
         "for a general teaching to the mendicants"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "straightforward restatement, best read as a pair "
                       "with AN 9.27"),
    ],
    why=(
        "The same nine-item stream-entry formula given to Anāthapiṇḍika "
        "at AN 9.27 &mdash; five fears and enmities quelled through the "
        "five precepts, and four factors of confidence in the Buddha, "
        "the teaching, the Saṅgha, and one's own ethical conduct "
        "&mdash; is repeated here as a general teaching to the "
        "mendicants, without the earlier discourse's narrative "
        "occasion."),
    guide=[
        ("The teaching in one sentence", [
            "A noble disciple who has quelled the same five fears and "
            "possesses the same four factors of confidence named at AN "
            "9.27 may, exactly as there, rightly declare themselves a "
            "stream-enterer, finished with rebirth in any bad place."]),
        ("A near-perfect twin", [
            "Word for word, this discourse's content matches AN 9.27's: "
            "the same five fears tied to the same five precepts, and the "
            "same four factors of confidence in the Buddha, the "
            "teaching, the Saṅgha, and ethical conduct, closing on the "
            "identical declaration formula."]),
        ("What actually changes: the audience, not the content", [
            "The one real difference between the two discourses is "
            "audience and occasion: AN 9.27 opens with Anāthapiṇḍika "
            "approaching the Buddha in person, while this discourse "
            "opens simply &lsquo;mendicants,&rsquo; addressed to the "
            "assembly in general with no narrative frame at all."]),
        ("Why a teaching would be given twice", [
            "This project has already met several paired discourses "
            "that repeat the same content under a different frame "
            "&mdash; AN 9.25 and AN 9.26's wisdom-versus-heart framing "
            "chief among them in this same chapter. This pairing is the "
            "simplest version of that pattern: identical content, "
            "distinguished by nothing but who is listening."]),
    ],
    terms=[
        ("bhikkhave",
         "&ldquo;mendicants&rdquo; &mdash; this discourse's own opening "
         "address, replacing AN 9.27's personal address to "
         "Anāthapiṇḍika."),
        ("pañca bhayāni verāni vūpasantāni",
         "&ldquo;five fears and enmities... quelled&rdquo; &mdash; the "
         "identical phrase and content as AN 9.27."),
        ("cattāri ca sotāpattiyaṅgāni",
         "&ldquo;the four factors of stream-entry&rdquo; &mdash; "
         "restated here without any change from AN 9.27's version."),
        ("suraṁerayamajjapamādaṭṭhānā paṭivirato",
         "&ldquo;refrains from consuming beer, wine, and liquor "
         "intoxicants&rdquo; &mdash; the fifth precept and fifth quelled "
         "fear, identical in both discourses."),
        ("khīṇanirayo... sotāpanno",
         "&ldquo;finished with rebirth in hell... I am a stream-"
         "enterer&rdquo; &mdash; the shared closing declaration, word "
         "for word the same as AN 9.27."),
    ],
    text_intro=(
        "The discourse in full: the identical nine-item formula as AN "
        "9.27, addressed here to the mendicants generally. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The same declaration, a general audience"),
        ("p", "&sect;1", "an9.28:1.1-2.3"),
        ("h3", "Five fears, quelled"),
        ("p", "&sect;2", "an9.28:3.1-3.4"),
        ("h3", "Four factors of confidence"),
        ("p", "&sect;3", "an9.28:4.1-5.2"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 9.27's?",
         "opts": [
             "Entirely different, with new items",
             "Word for word identical — the same five fears and four "
             "factors of confidence",
             "Half the length, with items removed",
             "Doubled, with additional items"],
         "correct": 1,
         "expl": "A near-perfect twin, differing only in audience."},
        {"q": "What is the one real difference between AN 9.27 and this "
              "discourse?",
         "opts": [
             "The number of items in the formula",
             "The audience and occasion — AN 9.27 addresses "
             "Anāthapiṇḍika personally, this discourse addresses the "
             "mendicants generally with no narrative frame",
             "The declaration each justifies",
             "The order of the nine items"],
         "correct": 1,
         "expl": "Content unchanged; only who is being addressed "
                 "differs."},
        {"q": "According to the guide, what other pairing in this "
              "chapter shows the same content repeated under a "
              "different frame?",
         "opts": [
             "AN 9.21 and AN 9.22",
             "AN 9.25 and AN 9.26, framed by wisdom and by heart",
             "AN 9.11 and AN 9.12",
             "There is no comparable pairing"],
         "correct": 1,
         "expl": "Though that pair changes framing register, not just "
                 "audience."},
        {"q": "What five precepts underlie the five quelled fears in "
              "this discourse?",
         "opts": [
             "Killing, stealing, sexual misconduct, lying, and "
             "intoxicants",
             "Five monastic rules about robes",
             "Five rules about almsfood",
             "Five rules about speech alone"],
         "correct": 0,
         "expl": "The same five precepts as AN 9.27, unchanged."},
        {"q": "What declaration closes this discourse?",
         "opts": [
             "A vow of future celibacy",
             "The identical stream-enterer's declaration as AN 9.27, "
             "word for word",
             "A request for the Buddha's blessing",
             "A confession of doubt"],
         "correct": 1,
         "expl": "The same closing formula, unchanged from its twin."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī, matching AN 9.27",
             "Yes, at Rājagaha",
             "No setting is stated in the source",
             "Yes, at Vesālī"],
         "correct": 2,
         "expl": "Unlike AN 9.27's personal narrative opening, this "
                 "version has no setting at all."},
    ],
    marginalia=[
        ("A near-perfect twin", [
            "the same five fears,",
            "the same four factors &mdash;",
            "word for word repeated",
        ]),
        ("What actually changes", [
            "not the content, but",
            "who is being addressed &mdash;",
            "one man, then the many",
        ]),
        ("Why repeat a teaching?", [
            "the same nine items,",
            "given twice over &mdash;",
            "worth hearing again",
        ]),
        ("Cross-references", [
            "AN 9.27 &middot; previous, the identical formula addressed "
            "to Anāthapiṇḍika by name",
            "AN 9.29 &middot; next, Grounds for Resentment",
        ]),
    ],
    further=[
        '<a href="%s/an9.28/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.27.html">AN 9.27 &middot; Fears and Enmities (1st)</a> &mdash; previous, '
        "the identical formula addressed to Anāthapiṇḍika by name.",
        '<a href="an-9.29.html">AN 9.29 &middot; Grounds for Resentment</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.29 — Āghātavatthusutta
# --------------------------------------------------------------------------- #
page(
    29, "Āghātavatthu", "Grounds for Resentment",
    vagga=VAGGA_3,
    meta_title="AN 9.29 — Grounds for Resentment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Āghātavatthusutta, naming nine grounds for resentment generated "
        "by crossing three time-tenses against three kinds of target — "
        "oneself, someone loved, and someone disliked. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single list of nine, generated by crossing three "
                 "tenses against three targets"),
        ("Length", "~1 minute to read"),
        ("A three-by-three grid, like AN 9.22", "Three tenses (past, "
         "present, future) crossed against three targets (myself, "
         "someone I love, someone I dislike) produces the nine grounds, "
         "the same multiplication logic already met at AN 9.22"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a "
                       "clear grid, worth reading alongside its direct "
                       "antidote at AN 9.30"),
    ],
    why=(
        "Nine grounds for resentment arise from crossing three "
        "time-tenses &mdash; they did, are doing, or will do wrong "
        "&mdash; against three targets: wrong done to oneself, wrong "
        "done to someone loved, and help given to someone disliked, each "
        "combination a distinct occasion on which resentment can take "
        "root."),
    guide=[
        ("The teaching in one sentence", [
            "Resentment is harbored on nine grounds: thinking someone "
            "did, is doing, or will do wrong to me; did, is doing, or "
            "will do wrong to someone I love; or helped, is helping, or "
            "will help someone I dislike."]),
        ("A grid, not a flat list", [
            "As with AN 9.22's horses and people, this discourse's nine "
            "items are not nine unrelated grievances but a clean "
            "three-by-three grid: three time-tenses (past, present, and "
            "future wrongdoing or favoritism) crossed against three "
            "targets (myself, someone I love, and someone I dislike)."]),
        ("Resentment extends beyond direct harm to oneself", [
            "Only the first three grounds concern wrong done directly "
            "to oneself. The middle three extend resentment to wrongs "
            "done to someone loved, and the final three extend it "
            "further still, to simple favor shown toward someone "
            "disliked &mdash; no direct harm required at all, only "
            "unwelcome kindness shown to the wrong person."]),
        ("A catalogue, without yet offering a remedy", [
            "This discourse is purely diagnostic: it names the nine "
            "grounds without commenting on whether resentment is "
            "justified or how to release it. That work is left "
            "entirely to its companion discourse immediately following, "
            "AN 9.30, which answers each of these same nine grounds with "
            "a specific way to let it go."]),
    ],
    terms=[
        ("āghāto",
         "&ldquo;resentment&rdquo; &mdash; the discourse's own title "
         "term, its nine grounds catalogued without comment here."),
        ("anatthaṁ me acari",
         "&ldquo;they did wrong to me&rdquo; &mdash; the first ground, "
         "opening the three-tense, three-target grid."),
        ("piyassa me manāpassa anatthaṁ acari",
         "&ldquo;they did wrong to someone I love&rdquo; &mdash; the "
         "fourth ground, extending resentment beyond direct harm to "
         "oneself."),
        ("appiyassa me amanāpassa atthaṁ acari",
         "&ldquo;they helped someone I dislike&rdquo; &mdash; the "
         "seventh ground, extending resentment to simple favor shown to "
         "an unwelcome party."),
        ("nava āghātavatthūni",
         "&ldquo;nine grounds for resentment&rdquo; &mdash; the "
         "discourse's own closing count, matched item for item by AN "
         "9.30's nine ways of letting it go."),
    ],
    text_intro=(
        "The discourse in full: nine grounds for resentment, generated "
        "by crossing three tenses against three targets. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine grounds for resentment"),
        ("p", "&sect;1", "an9.29:1.1-1.12"),
    ],
    quiz=[
        {"q": "How are this discourse's nine grounds for resentment "
              "generated?",
         "opts": [
             "As nine unrelated, scattered grievances",
             "By crossing three time-tenses (past, present, future) "
             "against three targets (myself, someone loved, someone "
             "disliked)",
             "As a single narrative sequence",
             "By listing nine named individuals"],
         "correct": 1,
         "expl": "A three-by-three grid, the same multiplication logic "
                 "already met at AN 9.22."},
        {"q": "What three targets does resentment extend across, "
              "according to this discourse?",
         "opts": [
             "Family, strangers, and enemies",
             "Wrong done to oneself, wrong done to someone loved, and "
             "help given to someone disliked",
             "Monastics, laypeople, and deities",
             "The past, present, and future only"],
         "correct": 1,
         "expl": "Resentment isn't limited to direct harm to oneself."},
        {"q": "What does the seventh ground for resentment involve?",
         "opts": [
             "Direct physical harm",
             "Simply helping someone I dislike — no direct harm required "
             "at all",
             "Theft of property",
             "A broken promise"],
         "correct": 1,
         "expl": "Unwelcome kindness shown to the wrong person, not harm "
                 "at all."},
        {"q": "What does this discourse do about the nine grounds it "
              "names?",
         "opts": [
             "It condemns resentment as always unjustified",
             "It purely catalogues them, without commenting on whether "
             "resentment is justified or how to release it",
             "It praises resentment as a virtue",
             "It offers a single universal remedy"],
         "correct": 1,
         "expl": "The remedy is left to its companion discourse, AN "
                 "9.30."},
        {"q": "How does AN 9.30 relate to this discourse?",
         "opts": [
             "It contradicts this discourse's list",
             "It answers each of these same nine grounds with a "
             "specific way of letting resentment go",
             "It has no relationship to this discourse",
             "It doubles the number of grounds"],
         "correct": 1,
         "expl": "A direct companion, matched item for item."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare diagnostic catalogue, like AN 9.30 immediately "
                 "after it."},
    ],
    marginalia=[
        ("A grid, three by three", [
            "did, is doing, will do &mdash;",
            "wrong to me, to one I love,",
            "or help to one I dislike",
        ]),
        ("Beyond direct harm", [
            "not just wrong to me &mdash;",
            "wrong to those I love, or",
            "kindness to a rival",
        ]),
        ("Diagnosis, not yet cure", [
            "nine grounds named plainly,",
            "no remedy offered yet &mdash;",
            "see AN 9.30 next",
        ]),
        ("Cross-references", [
            "AN 9.22 &middot; the same three-by-three grid logic",
            "AN 9.28 &middot; previous, Fears and Enmities (2nd)",
            "AN 9.30 &middot; next, the direct antidote to these same "
            "nine grounds",
        ]),
    ],
    further=[
        '<a href="%s/an9.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.28.html">AN 9.28 &middot; Fears and Enmities (2nd)</a> &mdash; previous.',
        '<a href="an-9.30.html">AN 9.30 &middot; Getting Rid of Resentment</a> &mdash; next, '
        "the direct antidote to these same nine grounds.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.30 — Āghātapaṭivinayasutta
# --------------------------------------------------------------------------- #
page(
    30, "Āghātapaṭivinaya", "Getting Rid of Resentment",
    vagga=VAGGA_3,
    meta_title="AN 9.30 — Getting Rid of Resentment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Āghātapaṭivinayasutta, answering AN 9.29's nine grounds for "
        "resentment with nine matching ways to let each one go, each "
        "closing on the same disarming question. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same three-by-three grid as AN 9.29, each item "
                 "closed by an identical disarming reflection"),
        ("Length", "~1 minute to read"),
        ("A direct answer to AN 9.29", "Every one of this discourse's "
         "nine ways to release resentment corresponds exactly to one of "
         "AN 9.29's nine grounds for holding it"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and practical, best read as a pair with AN "
                       "9.29"),
    ],
    why=(
        "For each of the same nine grounds named at AN 9.29 &mdash; "
        "wrong done to oneself, to someone loved, or favor shown to "
        "someone disliked, each across past, present, and future "
        "&mdash; resentment is released by the same disarming "
        "reflection: &lsquo;but what can I possibly do?&rsquo;"),
    guide=[
        ("The teaching in one sentence", [
            "Resentment is released on the same nine grounds named at "
            "AN 9.29 &mdash; harm done to me, to someone I love, or "
            "favor shown to someone I dislike, across past, present, and "
            "future &mdash; each time by the identical reflection: "
            "&lsquo;they harmed me (or are harming, or will harm), but "
            "what can I possibly do?&rsquo;"]),
        ("The same grid, now answered item for item", [
            "This discourse doesn't introduce a new structure; it takes "
            "AN 9.29's exact three-by-three grid of tenses and targets "
            "and answers every single cell with the same short "
            "reflection, making the pairing between the two discourses "
            "as tight as any in this collection."]),
        ("One reflection, not nine different techniques", [
            "Unlike teachings elsewhere that offer a distinct antidote "
            "for each item in a list, this discourse's remedy is "
            "strikingly uniform: the identical rhetorical question, "
            "&lsquo;but what can I possibly do?&rsquo;, applied without "
            "variation across all nine grounds, suggesting the release "
            "of resentment depends less on nine different insights than "
            "on repeating one disarming reflection consistently."]),
        ("Acceptance of limits, not denial of harm", [
            "The reflection doesn't deny that harm occurred, or that it "
            "might occur again; it simply notes the limits of what can "
            "actually be done about it now. This is a pragmatic release "
            "of resentment's grip rather than a claim that the "
            "resentment was never justified in the first place."]),
    ],
    terms=[
        ("āghātassa paṭivinayo",
         "&ldquo;getting rid of resentment&rdquo; &mdash; the "
         "discourse's own title phrase, framing release rather than "
         "diagnosis."),
        ("kiṁ hi tattha labbhā",
         "&ldquo;but what can I possibly do?&rdquo; &mdash; the single "
         "reflection applied without variation to all nine grounds for "
         "resentment."),
        ("upahaññi maṁ",
         "&ldquo;they harmed me&rdquo; &mdash; the first ground "
         "answered, matching AN 9.29's opening item exactly."),
        ("piyassa me manāpassa upahaññi",
         "&ldquo;they harmed someone I love&rdquo; &mdash; the fourth "
         "ground answered, matching AN 9.29's own fourth item."),
        ("appiyassa me amanāpassa atthaṁ acari",
         "&ldquo;they helped someone I dislike&rdquo; &mdash; the "
         "ninth and final ground answered, closing both discourses on "
         "the identical structure."),
    ],
    text_intro=(
        "The discourse in full: the same nine grounds as AN 9.29, each "
        "answered by the identical disarming reflection. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine ways to get rid of resentment"),
        ("p", "&sect;1", "an9.30:1.1-1.12"),
    ],
    quiz=[
        {"q": "How does this discourse's structure relate to AN 9.29's?",
         "opts": [
             "It introduces a completely different grid",
             "It uses the identical three-by-three grid of tenses and "
             "targets, answering every one of AN 9.29's nine grounds "
             "directly",
             "It only addresses three of the nine grounds",
             "It has no structural relationship to AN 9.29"],
         "correct": 1,
         "expl": "As tight a pairing as any two discourses in this "
                 "collection."},
        {"q": "What single reflection does this discourse apply across "
              "all nine grounds?",
         "opts": [
             "A different technique for each ground",
             "&lsquo;But what can I possibly do?&rsquo;, applied without "
             "variation to every ground",
             "A request for forgiveness",
             "A vow of retaliation"],
         "correct": 1,
         "expl": "Uniform repetition, not nine distinct antidotes."},
        {"q": "According to the guide, what does this uniformity "
              "suggest about releasing resentment?",
         "opts": [
             "That nine different insights are required",
             "That release depends less on varied insight than on "
             "repeating one disarming reflection consistently",
             "That resentment cannot actually be released",
             "That only monastics can release resentment"],
         "correct": 1,
         "expl": "One reflection, applied consistently across every "
                 "grievance."},
        {"q": "Does the reflection deny that harm occurred?",
         "opts": [
             "Yes, it claims the harm was imaginary",
             "No — it accepts the harm may have occurred and simply "
             "notes the limits of what can be done about it now",
             "Yes, it blames the person harboring resentment",
             "No, it promises the harm will be avenged"],
         "correct": 1,
         "expl": "Pragmatic release, not denial of the original harm."},
        {"q": "What is the ninth and final ground this discourse "
              "answers?",
         "opts": [
             "Wrong done to oneself in the present",
             "Help given to someone disliked, matching AN 9.29's own "
             "ninth item",
             "Wrong done to a stranger",
             "A broken monastic rule"],
         "correct": 1,
         "expl": "The pairing between the two discourses holds all the "
                 "way to the final item."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare practical formula, matching AN 9.29 immediately "
                 "before it."},
    ],
    marginalia=[
        ("The same grid, answered", [
            "past, present, future harm &mdash;",
            "to me, to one I love,",
            "or favor to a rival",
        ]),
        ("One reflection, repeated", [
            "&ldquo;but what can I",
            "possibly do?&rdquo; &mdash; the same",
            "answer, nine times over",
        ]),
        ("Acceptance, not denial", [
            "the harm isn't denied &mdash;",
            "only its grip released,",
            "by naming its limits",
        ]),
        ("Cross-references", [
            "AN 9.29 &middot; previous, the nine grounds this discourse "
            "answers item for item",
            "AN 9.31 &middot; next, Progressive Cessations, closing this "
            "chapter",
        ]),
    ],
    further=[
        '<a href="%s/an9.30/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.29.html">AN 9.29 &middot; Grounds for Resentment</a> &mdash; previous, '
        "the nine grounds this discourse answers item for item.",
        '<a href="an-9.31.html">AN 9.31 &middot; Progressive Cessations</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.31 — Anupubbanirodhasutta — closes ch.3 Sattāvāsavagga
# --------------------------------------------------------------------------- #
page(
    31, "Anupubbanirodha", "Progressive Cessations",
    vagga=VAGGA_3,
    meta_title="AN 9.31 — Progressive Cessations | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Anupubbanirodhasutta, closing this chapter with the classic "
        "nine progressive cessations across the four absorptions, the "
        "four formless dimensions, and the cessation of perception and "
        "feeling. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list of nine, each item naming what has "
                 "ceased at a specific meditative attainment"),
        ("Length", "~1 minute to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Sattāvāsavagga</em>, the third chapter of the "
         "Nines; the source's own untranslated closing verse names all "
         "eleven discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "precise meditative catalogue, best read alongside "
                       "AN 9.24's abodes"),
    ],
    why=(
        "Nine progressive cessations mark each successive meditative "
        "attainment: sensual perceptions cease at the first absorption, "
        "placing and keeping the mind connected cease at the second, "
        "rapture at the third, breathing at the fourth, and, through the "
        "four formless dimensions, perception of form, of infinite "
        "space, of infinite consciousness, and finally of nothingness, "
        "each cease in turn, ending with the total cessation of "
        "perception and feeling."),
    guide=[
        ("The teaching in one sentence", [
            "Nine things cease in progressive order across nine "
            "meditative attainments: sensual perceptions at the first "
            "absorption, placing and keeping the mind connected at the "
            "second, rapture at the third, breathing at the fourth, and "
            "then, through the four formless dimensions and the "
            "cessation of perception and feeling, each successively "
            "subtler perception in turn."]),
        ("Nine attainments, not nine practices", [
            "Unlike most nine-item lists in this chapter, this "
            "discourse's nine items are not nine parallel options to "
            "choose among but nine stages of a single deepening "
            "sequence, each attainment definitionally including "
            "everything that ceased at the stages before it."]),
        ("From the four absorptions through the formless dimensions", [
            "The first four cessations track the four form-absorptions "
            "familiar throughout this collection; the next four track "
            "the four formless dimensions already met in full at AN "
            "9.24's abodes of sentient beings, each one's perception "
            "replaced by a subtler one still. The ninth and final "
            "cessation, of perception and feeling itself, goes further "
            "than even the abodes catalogue in AN 9.24 reaches."]),
        ("Closing the third chapter", [
            "With this discourse, <em>Sattāvāsavagga</em>, the third "
            "chapter of the Nines, closes. The source's own untranslated "
            "colophon and chapter-summary verse name all eleven "
            "discourses of the chapter by their opening words, as with "
            "every chapter closer met so far in this collection."]),
    ],
    terms=[
        ("anupubbanirodhā",
         "&ldquo;progressive cessations&rdquo; &mdash; the discourse's "
         "own title term, naming nine successive stages rather than "
         "nine parallel options."),
        ("kāmasaññā niruddhā honti",
         "&ldquo;sensual perceptions have ceased&rdquo; &mdash; the "
         "first cessation, marking the first absorption."),
        ("assāsapassāsā niruddhā honti",
         "&ldquo;breathing has ceased&rdquo; &mdash; the fourth "
         "cessation, marking the fourth absorption."),
        ("ākiñcaññāyatanasaññā niruddhā honti",
         "&ldquo;the perception of the dimension of nothingness has "
         "ceased&rdquo; &mdash; the eighth cessation, marking the "
         "dimension of neither perception nor non-perception."),
        ("saññāvedayitanirodhaṁ samāpannassa saññā ca vedanā ca niruddhā honti",
         "&ldquo;for someone who has attained the cessation of "
         "perception and feeling, perception and feeling have "
         "ceased&rdquo; &mdash; the ninth and final cessation, closing "
         "the sequence and this chapter."),
    ],
    text_intro=(
        "The discourse in full: nine progressive cessations across the "
        "four absorptions, the four formless dimensions, and the "
        "cessation of perception and feeling. The source's own closing "
        "colophon and chapter-summary verse are untranslated in the "
        "English and are described rather than quoted here. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine progressive cessations"),
        ("p", "&sect;1", "an9.31:1.1-1.12"),
    ],
    quiz=[
        {"q": "How do this discourse's nine cessations differ in kind "
              "from most other nine-item lists in this chapter?",
         "opts": [
             "They are identical in structure to every other list",
             "They are nine stages of a single deepening sequence, not "
             "nine parallel options to choose among",
             "They have no relationship to meditative attainment",
             "They are nine unrelated similes"],
         "correct": 1,
         "expl": "Each attainment builds on and includes what ceased "
                 "before it."},
        {"q": "What ceases at the first absorption, according to this "
              "discourse?",
         "opts": [
             "Breathing", "Sensual perceptions",
             "Rapture", "The perception of form"],
         "correct": 1,
         "expl": "The first of nine progressive cessations."},
        {"q": "How do the fifth through eighth cessations relate to AN "
              "9.24?",
         "opts": [
             "They are entirely unrelated to AN 9.24",
             "They track the same four formless dimensions already met "
             "in full at AN 9.24's abodes of sentient beings",
             "They contradict AN 9.24's classification",
             "AN 9.24 covers ten formless dimensions, not four"],
         "correct": 1,
         "expl": "The same territory, reframed here as successive "
                 "cessation rather than as an abode."},
        {"q": "What is the ninth and final cessation, and how does it "
              "compare to AN 9.24's reach?",
         "opts": [
             "The cessation of breathing, matching AN 9.24 exactly",
             "The cessation of perception and feeling itself, going "
             "further than even AN 9.24's abodes catalogue reaches",
             "The cessation of rapture, a repeat of the third item",
             "There is no ninth cessation"],
         "correct": 1,
         "expl": "A stage beyond even the four formless dimensions "
                 "catalogued at AN 9.24."},
        {"q": "What does this discourse close?",
         "opts": [
             "Nothing; the chapter continues past it",
             "<em>Sattāvāsavagga</em>, the third chapter, with an "
             "untranslated colophon and uddāna verse naming all eleven "
             "discourses",
             "The entire nipāta",
             "Only this single discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare meditative catalogue, closing the chapter "
                 "without narrative frame."},
    ],
    marginalia=[
        ("Nine stages, one sequence", [
            "sensual perception,",
            "then placing thought, rapture,",
            "breathing, each in turn",
        ]),
        ("Through the formless, and beyond", [
            "space, consciousness,",
            "nothingness, then neither &mdash;",
            "then feeling itself stops",
        ]),
        ("Closing the third chapter", [
            "Sattāvāsavaggo",
            "finished &mdash; eleven discourses",
            "named in its own verse",
        ]),
        ("Cross-references", [
            "AN 9.24 &middot; the same formless dimensions, there as "
            "abodes rather than cessations",
            "AN 9.30 &middot; previous, Getting Rid of Resentment",
            "AN 9.32 &middot; next, opening ch.4, Mahāvagga",
        ]),
    ],
    further=[
        '<a href="%s/an9.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.24.html">AN 9.24 &middot; Abodes of Sentient Beings</a> &mdash; the '
        "same formless dimensions, there as abodes rather than cessations.",
        '<a href="an-9.30.html">AN 9.30 &middot; Getting Rid of Resentment</a> &mdash; previous.',
    ],
)


# --------------------------------------------------------------------------- #
# ch.4 — Mahāvagga (AN 9.32-41). Nearly every discourse in this chapter turns
# on the same nine progressive meditative attainments (anupubbavihāra) --
# the four absorptions, the four formless dimensions, and the cessation of
# perception and feeling -- already met piecemeal at AN 9.24 (as abodes) and
# AN 9.31 (as cessations). Each page's guide names its own distinctive angle
# rather than re-describing the shared nine-fold scaffold from scratch.
# --------------------------------------------------------------------------- #
VAGGA_4 = "<em>Mahāvagga</em> &mdash; the fourth chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.32 — Anupubbavihārasutta — this chapter's foundational catalogue
# --------------------------------------------------------------------------- #
page(
    32, "Anupubbavihāra", "Progressive Meditations",
    vagga=VAGGA_4,
    meta_title="AN 9.32 — Progressive Meditations | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Anupubbavihārasutta, opening this meditation-heavy chapter with "
        "the bare list of nine progressive attainments that nearly every "
        "other discourse here builds on. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single bare list, no narrative and no similes"),
        ("Length", "~30 seconds to read"),
        ("This chapter's real foundation", "Nearly every other discourse "
         "in this chapter builds on this exact nine-item list — the same "
         "content already met as &ldquo;cessations&rdquo; at AN 9.31"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "but essential scaffolding for the rest of this "
                       "chapter"),
    ],
    why=(
        "Nine progressive meditations are named in sequence: the four "
        "absorptions, the four formless dimensions, and the cessation of "
        "perception and feeling &mdash; the same nine attainments that, "
        "under different framings, structure nearly every other "
        "discourse in this chapter."),
    guide=[
        ("The teaching in one sentence", [
            "There are nine progressive meditations: the first, second, "
            "third, and fourth absorptions; the dimensions of infinite "
            "space, infinite consciousness, and nothingness; the "
            "dimension of neither perception nor non-perception; and the "
            "cessation of perception and feeling."]),
        ("A bare list, positively framed", [
            "Where AN 9.31 named this same nine-item sequence by what "
            "ceases at each stage, this discourse names the identical "
            "sequence positively, simply as meditations to be attained "
            "&mdash; the same content, its third framing in this nipāta "
            "after AN 9.24's abodes and AN 9.31's cessations."]),
        ("The scaffold for this entire chapter", [
            "Unlike most bare lists in this collection, this one is not "
            "an isolated teaching but this chapter's structural spine: "
            "AN 9.33 through AN 9.41 each return to this same nine-stage "
            "sequence, applying it to bliss, to skillful use as an "
            "insight-basis, to cosmology, to a mythic battle, to a "
            "wild elephant's solitude, and to the Buddha's own "
            "autobiography."]),
        ("Why the order matters", [
            "The sequence's progression &mdash; each dimension going "
            "&lsquo;totally beyond&rsquo; the one before it &mdash; is "
            "not incidental. Several of this chapter's later discourses "
            "make the ordering itself the whole point, whether through a "
            "gradualist simile of a cow that doesn't rush ahead, or "
            "through the Buddha's own insistence that only mastering all "
            "nine in both forward and reverse order preceded his "
            "awakening."]),
    ],
    terms=[
        ("anupubbavihārā",
         "&ldquo;progressive meditations&rdquo; &mdash; this "
         "discourse's own title term and the shared name for the nine-"
         "stage sequence structuring this entire chapter."),
        ("paṭhamaṁ jhānaṁ",
         "&ldquo;the first absorption&rdquo; &mdash; the sequence's "
         "opening stage."),
        ("ākāsānañcāyatanaṁ",
         "&ldquo;the dimension of infinite space&rdquo; &mdash; the "
         "fifth stage, the first of the four formless dimensions."),
        ("nevasaññānāsaññāyatanaṁ",
         "&ldquo;the dimension of neither perception nor non-"
         "perception&rdquo; &mdash; the eighth stage, the most subtle "
         "attainment with perception."),
        ("saññāvedayitanirodho",
         "&ldquo;the cessation of perception and feeling&rdquo; &mdash; "
         "the ninth and final stage, closing the sequence."),
    ],
    text_intro=(
        "The discourse in full: nine progressive meditations, named in "
        "sequence. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine progressive meditations"),
        ("p", "&sect;1", "an9.32:1.1-1.4"),
    ],
    quiz=[
        {"q": "What nine progressive meditations does this discourse "
              "name?",
         "opts": [
             "Nine kinds of loving-kindness practice",
             "The four absorptions, the four formless dimensions, and "
             "the cessation of perception and feeling",
             "The nine perceptions met at AN 9.16",
             "Nine monastic disciplinary rules"],
         "correct": 1,
         "expl": "The same nine-stage sequence structuring nearly this "
                 "whole chapter."},
        {"q": "How does this discourse's framing compare to AN 9.31's?",
         "opts": [
             "Entirely unrelated content",
             "The identical nine-item sequence, named here positively as "
             "meditations rather than by what ceases at each stage",
             "A shorter version with only five items",
             "A contradiction of AN 9.31's list"],
         "correct": 1,
         "expl": "The same nine attainments, a third framing after AN "
                 "9.24's abodes and AN 9.31's cessations."},
        {"q": "According to the guide, what role does this discourse "
              "play in the chapter?",
         "opts": [
             "An isolated teaching with no connection to what follows",
             "This chapter's structural spine, returned to by nearly "
             "every discourse that follows",
             "A closing summary of the whole chapter",
             "A teaching unrelated to meditation"],
         "correct": 1,
         "expl": "AN 9.33 through AN 9.41 each build on this same "
                 "sequence."},
        {"q": "What comes immediately after the four absorptions in this "
              "sequence?",
         "opts": [
             "The cessation of perception and feeling directly",
             "The four formless dimensions, beginning with infinite "
             "space",
             "A return to the first absorption",
             "The nine perceptions"],
         "correct": 1,
         "expl": "A clean progression from form-based to formless "
                 "attainments."},
        {"q": "Why does the guide say the sequence's order matters?",
         "opts": [
             "It doesn't matter; the nine items could occur in any order",
             "Several later discourses make the ordering itself central "
             "— including the Buddha's insistence on mastering all nine "
             "forward and reverse before his awakening",
             "The order is only relevant to monastics",
             "The order was added by a later editor"],
         "correct": 1,
         "expl": "A theme this chapter returns to explicitly at its "
                 "close, AN 9.41."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare foundational catalogue, opening this chapter."},
    ],
    marginalia=[
        ("Nine stages, named", [
            "four absorptions,",
            "four formless dimensions,",
            "then cessation itself",
        ]),
        ("A third framing", [
            "abodes, then cessations,",
            "now meditations &mdash;",
            "the same nine attainments",
        ]),
        ("This chapter's spine", [
            "nearly every discourse",
            "ahead returns to this list &mdash;",
            "bliss, insight, myth, self",
        ]),
        ("Cross-references", [
            "AN 9.24, AN 9.31 &middot; the same nine attainments under "
            "two earlier framings",
            "AN 9.31 &middot; previous chapter's closing page",
            "AN 9.33 &middot; next, the same nine elaborated in full",
        ]),
    ],
    further=[
        '<a href="%s/an9.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.31.html">AN 9.31 &middot; Progressive Cessations</a> &mdash; previous.',
        '<a href="an-9.33.html">AN 9.33 &middot; The Nine Progressive Meditative '
        "Attainments</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.33 — Anupubbanirodhasutta (Nava-anupubbavihārasamāpattisutta) — the
# nine attainments from AN 9.32, elaborated in full with a teaching dialogue.
# --------------------------------------------------------------------------- #
page(
    33, "Anupubbavihārasamāpatti", "The Nine Progressive Meditative Attainments",
    vagga=VAGGA_4,
    meta_title=("AN 9.33 — The Nine Progressive Meditative Attainments | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "elaborated companion to AN 9.32 — the same nine attainments, "
        "each unpacked with a full jhāna formula and a shared refrain "
        "about a non-deceitful listener's approval. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same nine-item sequence as AN 9.32, each stage "
                 "unpacked with a full formula and a shared closing "
                 "refrain"),
        ("Length", "~5 minutes to read"),
        ("AN 9.32, expanded rather than repeated", "Where AN 9.32 named "
         "the nine attainments in a single bare line each, this "
         "discourse gives each one a full teaching formula and an "
         "identical closing refrain"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "highly repetitive by design, worth reading for "
                       "its refrain's own logic"),
    ],
    why=(
        "For each of the nine progressive attainments in turn, this "
        "discourse names exactly where a specific quality ceases, gives "
        "the full formula for reaching that point, and closes with the "
        "claim that anyone not devious or deceitful would recognize and "
        "approve of the answer, bowing with cupped palms."),
    guide=[
        ("The teaching in one sentence", [
            "For each of the nine progressive attainments, a specific "
            "quality is said to cease there &mdash; sensual pleasures at "
            "the first absorption, the placing of the mind at the "
            "second, and so on through to the dimension of neither "
            "perception nor non-perception &mdash; and anyone honest "
            "would recognize and approve of this when the full formula "
            "for reaching it is explained."]),
        ("The same nine stages, now with full formulas", [
            "This discourse takes AN 9.32's bare nine-item list and "
            "gives each stage what that earlier discourse left out: the "
            "complete jhāna or formless-attainment formula, spelled out "
            "in full rather than merely named."]),
        ("A refrain testing honesty, not just doctrine", [
            "Every one of the nine stages closes with the identical "
            "claim: someone who is not devious or deceitful would "
            "approve and agree with the explanation, saying "
            "&lsquo;good!&rsquo; and paying homage with cupped palms. "
            "The refrain frames disagreement not as an intellectual "
            "difference of opinion but as a mark of deviousness &mdash; "
            "a rhetorically pointed move repeated nine times running."]),
        ("All nine stages fully unpacked, including the last", [
            "Unlike a flat list, each formula here names where the "
            "*previous* stage's perception ceases as the doorway into "
            "the next: the ninth and final formula names where the "
            "perception of neither perception nor non-perception ceases "
            "&mdash; namely, on entering the cessation of perception and "
            "feeling itself. Every one of the nine attainments, "
            "including this final and most subtle one, receives its own "
            "complete formula and refrain."]),
    ],
    terms=[
        ("nava anupubbavihārasamāpattiyo",
         "&ldquo;the nine progressive meditative attainments&rdquo; "
         "&mdash; this discourse's own fuller title for the same "
         "sequence named at AN 9.32."),
        ("kāmā nirujjhanti",
         "&ldquo;where sensual pleasures cease&rdquo; &mdash; the "
         "opening claim for the first absorption, unpacked with its "
         "full formula."),
        ("amāyāvī akuhako",
         "&ldquo;not devious or deceitful&rdquo; &mdash; the discourse's "
         "own description of someone who would recognize and approve of "
         "each formula, repeated as its shared refrain."),
        ("sādhūti bhāsissati, añjaliṁ paggahetvā namassissati",
         "&ldquo;they'd say &lsquo;good!&rsquo; and bowing down, they'd "
         "pay homage with cupped palms&rdquo; &mdash; the physical "
         "gesture closing the shared refrain nine times."),
        ("nevasaññānāsaññāyatanasaññā nirujjhanti",
         "&ldquo;where the perception of the dimension of neither "
         "perception nor non-perception ceases&rdquo; &mdash; the "
         "ninth and final formula, naming entry into the cessation of "
         "perception and feeling itself."),
    ],
    text_intro=(
        "The discourse in full: the same nine attainments as AN 9.32, "
        "each unpacked with a full formula and the shared refrain. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nine stages, each unpacked in full"),
        ("p", "&sect;1", "an9.33:1.1-1.9"),
        ("p", "&sect;2", "an9.33:2.1-2.7"),
        ("p", "&sect;3", "an9.33:3.1-3.7"),
        ("p", "&sect;4", "an9.33:4.1-4.7"),
        ("p", "&sect;5", "an9.33:5.1-5.7"),
        ("p", "&sect;6", "an9.33:6.1-6.7"),
        ("p", "&sect;7", "an9.33:7.1-7.7"),
        ("p", "&sect;8", "an9.33:8.1-8.7"),
        ("p", "&sect;9", "an9.33:9.1-10.1"),
    ],
    quiz=[
        {"q": "How does this discourse relate to AN 9.32?",
         "opts": [
             "It is an entirely unrelated teaching",
             "It takes the same nine-item list and gives each stage its "
             "full formula, where AN 9.32 only named each in a single "
             "line",
             "It shortens AN 9.32's list to five items",
             "It contradicts AN 9.32's sequence"],
         "correct": 1,
         "expl": "Expansion, not repetition or contradiction."},
        {"q": "What does this discourse claim ceases at the first "
              "absorption?",
         "opts": [
             "Breathing", "Sensual pleasures",
             "Rapture", "The perception of form"],
         "correct": 1,
         "expl": "The opening claim, unpacked with the first absorption's "
                 "full formula."},
        {"q": "What refrain closes each of the nine stages?",
         "opts": [
             "A warning about wrong view",
             "That someone not devious or deceitful would approve and "
             "agree, saying &lsquo;good!&rsquo; with cupped palms",
             "A request for further explanation",
             "A simile about a stone post"],
         "correct": 1,
         "expl": "Repeated identically nine times, framing agreement as "
                 "a mark of honesty."},
        {"q": "According to the guide, what does the refrain frame "
              "disagreement as?",
         "opts": [
             "A legitimate intellectual difference of opinion",
             "A mark of deviousness, not merely a different view",
             "An acceptable alternative position",
             "Irrelevant to the discourse's point"],
         "correct": 1,
         "expl": "A rhetorically pointed move, repeated nine times "
                 "running."},
        {"q": "How does the ninth and final formula name entry into the "
              "cessation of perception and feeling?",
         "opts": [
             "It is skipped entirely, with no formula given",
             "As where the perception of neither perception nor non-"
             "perception ceases — every one of the nine stages, "
             "including this last one, gets its own complete formula",
             "As identical to the very first formula",
             "Only in a footnote, not in the main text"],
         "correct": 1,
         "expl": "Each formula names the previous stage's cessation as "
                 "the doorway into the next, all the way through the "
                 "ninth."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, like AN 9.32 immediately before it."},
    ],
    marginalia=[
        ("Nine stages, unpacked", [
            "each formula spelled",
            "out in full, where AN 9.32",
            "gave only a name",
        ]),
        ("A refrain, nine times", [
            "&ldquo;good!&rdquo; with cupped palms &mdash;",
            "honesty itself the test",
            "of who would agree",
        ]),
        ("Nine formulas, none skipped", [
            "each names where the",
            "stage before it ceases &mdash;",
            "even the ninth, in full",
        ]),
        ("Cross-references", [
            "AN 9.32 &middot; previous, the same nine attainments named "
            "briefly",
            "AN 9.34 &middot; next, Extinguishment is Bliss",
        ]),
    ],
    further=[
        '<a href="%s/an9.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.32.html">AN 9.32 &middot; Progressive Meditations</a> &mdash; previous.',
        '<a href="an-9.34.html">AN 9.34 &middot; Extinguishment is Bliss</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.34 — Nibbānasukhasutta
# --------------------------------------------------------------------------- #
page(
    34, "Nibbānasukha", "Extinguishment is Bliss",
    vagga=VAGGA_4,
    meta_title="AN 9.34 — Extinguishment is Bliss | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "famous Nibbānasukhasutta, in which Sāriputta answers Udāyī's "
        "challenge — what's blissful about feeling nothing? — by tracing "
        "affliction's absence across all nine attainments. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, in the Bamboo Grove, the squirrels' "
                    "feeding ground"),
        ("Speakers", "Venerable Sāriputta and Venerable Udāyī"),
        ("Form", "A provocative declaration, a direct challenge, and a "
                 "reasoned answer traced across all nine attainments"),
        ("Length", "~4 minutes to read"),
        ("A famous paradox, resolved", "How can extinguishment be "
         "&lsquo;bliss&rsquo; if nothing is felt there? Sāriputta's "
         "answer inverts the question rather than dodging it"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "genuinely subtle philosophical move, worth "
                       "reading slowly"),
    ],
    why=(
        "Sāriputta declares twice, unprompted, that extinguishment is "
        "bliss; when Udāyī challenges him &mdash; what's blissful about "
        "it, since nothing is felt? &mdash; Sāriputta answers that the "
        "very absence of feeling is precisely what's blissful, then "
        "demonstrates this across each of the nine progressive "
        "attainments by showing how even their pleasant qualities are, "
        "on reflection, an affliction."),
    guide=[
        ("The teaching in one sentence", [
            "The fact that nothing is felt in extinguishment is "
            "precisely what makes it blissful: at every one of the nine "
            "progressive attainments, any perception and focus still "
            "tied to what has been left behind counts as an affliction, "
            "and affliction is suffering, so only the complete absence "
            "of feeling is free of it."]),
        ("A challenge met head-on, not dodged", [
            "Udāyī's question is genuinely sharp: ordinary bliss is a "
            "feeling, so calling a feelingless state &lsquo;bliss&rsquo; "
            "sounds like a contradiction. Sāriputta doesn't soften the "
            "claim or redefine &lsquo;bliss&rsquo; loosely; he answers "
            "with the very fact Udāyī raised as an objection &mdash; "
            "&lsquo;the fact that nothing is felt is precisely what's "
            "blissful about it.&rsquo;"]),
        ("Affliction as the yardstick, applied nine times", [
            "Sāriputta's demonstration runs the same test through every "
            "one of the nine progressive attainments in turn: even "
            "while absorbed in the first jhāna, if perception and focus "
            "tied to sensual pleasure still beset the mind, that "
            "counts as an affliction &mdash; like a happy person "
            "suddenly feeling pain &mdash; and affliction has been "
            "called suffering by the Buddha. The same logic runs through "
            "all eight remaining stages, each one's residual perception "
            "of what came before still counting against it."]),
        ("Only the ninth stage passes every test", [
            "By the time the sequence reaches the cessation of "
            "perception and feeling, there is nothing left for any "
            "residual perception to be tied to at all &mdash; the "
            "affliction test simply has nothing left to catch. This "
            "silent conclusion, more than any single line, is what makes "
            "Sāriputta's opening declaration finally make sense."]),
    ],
    terms=[
        ("nibbānaṁ sukhaṁ",
         "&ldquo;extinguishment is bliss&rdquo; &mdash; Sāriputta's own "
         "opening declaration, repeated twice before Udāyī's challenge."),
        ("kimhi panettha, āvuso sāriputta, sukhaṁ, yadettha natthi "
         "vedayitanti",
         "&ldquo;what's blissful about it, since nothing is felt&rdquo; "
         "&mdash; Udāyī's sharp challenge, met directly rather than "
         "deflected."),
        ("etadeva khvettha, āvuso, sukhaṁ yadettha natthi vedayitaṁ",
         "&ldquo;the fact that nothing is felt is precisely what's "
         "blissful about it&rdquo; &mdash; Sāriputta's inverting answer."),
        ("ābādho vuttoyaṁ bhagavatā",
         "&ldquo;affliction has been called suffering by the "
         "Buddha&rdquo; &mdash; the shared refrain closing each of the "
         "discourse's nine demonstrations."),
        ("saññāvedayitanirodhaṁ... āsavā parikkhīṇā honti",
         "&ldquo;the cessation of perception and feeling... their "
         "defilements come to an end&rdquo; &mdash; the ninth and final "
         "stage, where the affliction test has nothing left to catch."),
    ],
    text_intro=(
        "The discourse in full: a declaration, a challenge, and the "
        "same affliction-test traced across all nine progressive "
        "attainments. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A declaration, and a challenge"),
        ("p", "&sect;1", "an9.34:1.1-1.16"),
        ("h3", "Affliction, tested across nine attainments"),
        ("p", "&sect;2", "an9.34:2.1-2.6"),
        ("p", "&sect;3", "an9.34:3.1-3.6"),
        ("p", "&sect;4", "an9.34:4.1-4.6"),
        ("p", "&sect;5", "an9.34:5.1-5.6"),
        ("p", "&sect;6", "an9.34:6.1-6.6"),
        ("p", "&sect;7", "an9.34:7.1-7.6"),
        ("p", "&sect;8", "an9.34:8.1-8.6"),
        ("h3", "Only the ninth stage passes"),
        ("p", "&sect;9", "an9.34:9.1-11.1"),
    ],
    quiz=[
        {"q": "What challenge does Udāyī raise against Sāriputta's "
              "declaration?",
         "opts": [
             "That extinguishment doesn't exist",
             "That calling a feelingless state &lsquo;bliss&rsquo; seems "
             "contradictory, since nothing is felt there",
             "That the Buddha never taught this",
             "That Sāriputta lacks the authority to teach"],
         "correct": 1,
         "expl": "A genuinely sharp philosophical objection, met "
                 "directly."},
        {"q": "How does Sāriputta answer the challenge?",
         "opts": [
             "By redefining &lsquo;bliss&rsquo; to mean something "
             "looser",
             "By inverting the objection: the very fact that nothing is "
             "felt is precisely what's blissful about it",
             "By refusing to answer",
             "By denying that extinguishment involves no feeling"],
         "correct": 1,
         "expl": "The objection becomes the answer, rather than being "
                 "deflected."},
        {"q": "What test does Sāriputta apply across all nine "
              "attainments?",
         "opts": [
             "A test of physical comfort",
             "Whether residual perception and focus tied to what came "
             "before still besets the mind, counting as an affliction",
             "A test of how long each attainment lasts",
             "A test of popularity among mendicants"],
         "correct": 1,
         "expl": "Even the first jhāna's own rapture can still be an "
                 "affliction if sensual perception intrudes."},
        {"q": "What simile does Sāriputta use to illustrate "
              "&lsquo;affliction&rsquo;?",
         "opts": [
             "A wild elephant disturbed by its herd",
             "A happy person suddenly experiencing pain",
             "A cow that slips between footholds",
             "An archer practicing on a straw man"],
         "correct": 1,
         "expl": "The shared image applied at each of the nine stages "
                 "in turn."},
        {"q": "Why does only the ninth attainment, the cessation of "
              "perception and feeling, fully pass the test?",
         "opts": [
             "Because it is the longest-lasting attainment",
             "Because there is nothing left for any residual perception "
             "to be tied to, so the affliction test has nothing left to "
             "catch",
             "Because it involves the most physical comfort",
             "Because it is easiest to attain"],
         "correct": 1,
         "expl": "The silent conclusion that makes Sāriputta's opening "
                 "declaration make sense."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, in the Bamboo Grove, the squirrels' feeding "
             "ground",
             "Cālikā, on the Cālikā mountain",
             "Kosambī, in Ghosita's Monastery"],
         "correct": 1,
         "expl": "The same setting as AN 9.26's stone-post simile."},
    ],
    marginalia=[
        ("A declaration, challenged", [
            "&ldquo;extinguishment is bliss&rdquo; &mdash;",
            "&ldquo;but nothing is felt there&rdquo; &mdash;",
            "the challenge met head-on",
        ]),
        ("The objection, inverted", [
            "&ldquo;this is precisely",
            "what's blissful about it&rdquo; &mdash;",
            "feeling nothing, itself",
        ]),
        ("Nine tests, one standard", [
            "even rapture can still",
            "afflict, if tied to what",
            "came before it",
        ]),
        ("Cross-references", [
            "AN 9.32, AN 9.31 &middot; the same nine attainments under "
            "earlier framings",
            "AN 9.33 &middot; previous, The Nine Progressive Meditative "
            "Attainments",
            "AN 9.35 &middot; next, The Simile of the Cow",
        ]),
    ],
    further=[
        '<a href="%s/an9.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.33.html">AN 9.33 &middot; The Nine Progressive Meditative '
        "Attainments</a> &mdash; previous.",
        '<a href="an-9.35.html">AN 9.35 &middot; The Simile of the Cow</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.35 — Gāvīupamāsutta (Nāgitasutta)
# --------------------------------------------------------------------------- #
page(
    35, "Gāvīupamā", "The Simile of the Cow",
    vagga=VAGGA_4,
    meta_title="AN 9.35 — The Simile of the Cow | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Simile of the Cow, contrasting a foolish mountain cow who slips "
        "between footholds with a skillful one who stabilizes each step "
        "— then extending to the six higher knowledges a fully "
        "stabilized mind makes accessible. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A paired animal simile (foolish, then skillful cow), "
                 "applied to the nine attainments, then extended into "
                 "six higher knowledges"),
        ("Length", "~6 minutes to read"),
        ("Gradualism as the whole point", "Unlike most discourses in "
         "this chapter, this one's real teaching is about pacing — not "
         "charging ahead before a stage is stabilized"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "vivid simile followed by a dense catalogue of "
                       "psychic attainments"),
    ],
    why=(
        "A foolish mountain cow, lifting a hind-hoof before her fore-hoof "
        "is properly set, slips between unfamiliar ground and never "
        "returns safely; a skillful cow, moving one hoof at a time, "
        "reaches new pasture and returns home &mdash; and a mendicant "
        "who charges ahead through the nine attainments without "
        "stabilizing each one slips between them just as badly, while "
        "one who stabilizes each stage in turn gains a pliable mind "
        "capable of six further higher knowledges."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who charges ahead to the next absorption before "
            "properly stabilizing the one they're in slips and falls "
            "from both, like a foolish cow stuck between unfamiliar "
            "footholds; one who cultivates and stabilizes each "
            "attainment before advancing reaches all nine safely, "
            "gaining a pliable mind capable of realizing six further "
            "higher knowledges."]),
        ("Two cows, one on rugged mountains", [
            "The foolish cow lifts a hind-hoof before her fore-hoof is "
            "properly set, never reaches new pasture, and never returns "
            "safely home. The skillful cow moves one hoof at a time, "
            "reaches new ground, and returns safely &mdash; the same "
            "physical caution the discourse then maps directly onto a "
            "mendicant &lsquo;slipped and fallen from both sides,&rsquo; "
            "unable to remain in either the stage just left or the one "
            "not yet properly entered."]),
        ("Stabilization before advancement, nine times over", [
            "Each of the nine progressive attainments gets the identical "
            "instruction: cultivate, develop, and make much of this "
            "basis, ensuring it's properly stabilized, before thinking "
            "of moving to the next &mdash; and the discourse repeats, "
            "&lsquo;without charging at&rsquo; the following stage, at "
            "every single transition."]),
        ("A pliable mind, and six higher knowledges", [
            "Once a mendicant has entered and emerged from all nine "
            "attainments this way, the mind becomes pliable and "
            "workable, limitless in immersion, capable of realizing "
            "whatever can be realized by insight &mdash; the discourse "
            "then names all six higher knowledges this pliability makes "
            "accessible: psychic power, clairaudience, mind-reading, "
            "recollection of past lives, clairvoyance regarding others' "
            "rebirths, and the ending of one's own defilements."]),
    ],
    terms=[
        ("gāvī pabbateyyā bālā avyattā amaggakusalā gocarakusalā",
         "&ldquo;a mountain cow who was foolish, incompetent, unskillful, "
         "and lacked common sense&rdquo; &mdash; the first, negative "
         "half of the discourse's own title simile."),
        ("ubhato bhaṭṭho",
         "&ldquo;slipped and fallen from both sides&rdquo; &mdash; the "
         "discourse's own term for a mendicant stuck between two "
         "attainments, unable to remain in either."),
        ("anāgataṁ appattaṁ na sāhasā pakkhandati",
         "&ldquo;without charging at&rdquo; the next attainment &mdash; "
         "the phrase repeated at every transition, naming the "
         "discourse's real teaching about pacing."),
        ("mudubhūtaṁ kammaniyaṁ",
         "&ldquo;pliable and workable&rdquo; &mdash; the quality a "
         "properly stabilized mind gains after entering and emerging "
         "from all nine attainments."),
        ("iddhividhā, dibbasota, cetopariyañāṇa, pubbenivāsānussati, "
         "dibbacakkhu, āsavakkhaya",
         "the six higher knowledges named in sequence &mdash; psychic "
         "power, clairaudience, mind-reading, past-life recollection, "
         "clairvoyance, and the ending of defilements."),
    ],
    text_intro=(
        "The discourse in full: two cows, nine stabilized attainments, "
        "and six higher knowledges. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A foolish cow, slipped between footholds"),
        ("p", "&sect;1", "an9.35:1.1-2.7"),
        ("h3", "A skillful cow, and nine stabilized attainments"),
        ("p", "&sect;2", "an9.35:3.1-11.3"),
        ("h3", "A pliable mind, and six higher knowledges"),
        ("p", "&sect;3", "an9.35:12.1-15.18"),
        ("p", "&sect;4", "an9.35:16.1-18.2"),
    ],
    quiz=[
        {"q": "What mistake does the foolish mountain cow make?",
         "opts": [
             "She refuses to leave her pasture at all",
             "She lifts a hind-hoof before her fore-hoof is properly "
             "set, and slips between unfamiliar footholds",
             "She eats grass that isn't hers",
             "She wanders too slowly"],
         "correct": 1,
         "expl": "Moving before the previous step is stabilized, mapped "
                 "directly onto meditative practice."},
        {"q": "What does the discourse call a mendicant who charges "
              "ahead to the next absorption too soon?",
         "opts": [
             "Wise and skillful",
             "&ldquo;Slipped and fallen from both sides&rdquo; — unable "
             "to remain in either the previous or the next stage",
             "A fine thoroughbred person",
             "A perfected one"],
         "correct": 1,
         "expl": "Stuck between two attainments, like the foolish cow "
                 "between footholds."},
        {"q": "What instruction repeats at every transition between the "
              "nine attainments?",
         "opts": [
             "Move as quickly as possible",
             "Cultivate, develop, and stabilize the current basis before "
             "advancing, without charging at the next stage",
             "Skip stages that seem unnecessary",
             "Return to the first absorption before each new attempt"],
         "correct": 1,
         "expl": "The discourse's real teaching about pacing, repeated "
                 "nine times."},
        {"q": "What quality does a mind gain after entering and emerging "
              "from all nine attainments this way?",
         "opts": [
             "Rigidity and fixed concentration",
             "Pliability and workability, with limitless, well-developed "
             "immersion",
             "Complete cessation of all mental activity",
             "Immunity to all future rebirth automatically"],
         "correct": 1,
         "expl": "The condition for realizing the six higher knowledges "
                 "named next."},
        {"q": "What six higher knowledges does this pliable mind make "
              "accessible?",
         "opts": [
             "Six monastic disciplinary categories",
             "Psychic power, clairaudience, mind-reading, past-life "
             "recollection, clairvoyance, and the ending of defilements",
             "Six kinds of loving-kindness",
             "Six formless dimensions"],
         "correct": 1,
         "expl": "The classic sixfold higher knowledges (chaḷabhiññā), "
                 "closing this lengthy discourse."},
        {"q": "According to the guide, what is this discourse's real "
              "teaching, distinct from most of this chapter?",
         "opts": [
             "The content of each attainment individually",
             "Pacing — not charging ahead before a stage is properly "
             "stabilized",
             "The names of the six higher knowledges alone",
             "A comparison between cows and elephants"],
         "correct": 1,
         "expl": "Gradualism itself is the point, illustrated by the "
                 "paired cow simile."},
    ],
    marginalia=[
        ("Two cows, one lesson", [
            "lift too soon, and slip &mdash;",
            "stabilize each hoof,",
            "and reach new pasture safely",
        ]),
        ("Without charging ahead", [
            "cultivate, develop,",
            "stabilize each stage &mdash;",
            "nine times, the same caution",
        ]),
        ("A pliable mind, six powers", [
            "psychic power, hearing,",
            "reading minds, past lives, sight,",
            "and defilements ended",
        ]),
        ("Cross-references", [
            "AN 9.32, AN 9.33 &middot; the same nine attainments, here "
            "with an emphasis on pacing",
            "AN 9.34 &middot; previous, Extinguishment is Bliss",
            "AN 9.36 &middot; next, Depending on Absorption",
        ]),
    ],
    further=[
        '<a href="%s/an9.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.34.html">AN 9.34 &middot; Extinguishment is Bliss</a> &mdash; previous.',
        '<a href="an-9.36.html">AN 9.36 &middot; Depending on Absorption</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.36 — Jhānasutta
# --------------------------------------------------------------------------- #
page(
    36, "Jhāna", "Depending on Absorption",
    vagga=VAGGA_4,
    meta_title="AN 9.36 — Depending on Absorption | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Jhānasutta, showing how each absorption and lower formless "
        "attainment can itself become a basis for ending the "
        "defilements through insight — with an explicit limit on the "
        "top two stages. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Seven attainments each declared a basis for insight, "
                 "with a shared formula and an archer simile, closing on "
                 "an explicit limit"),
        ("Length", "~4 minutes to read"),
        ("Jhāna as insight-basis, not just calm", "This discourse's real "
         "claim is that absorption itself, contemplated rightly, can "
         "directly end the defilements — not merely prepare the mind "
         "for insight practiced elsewhere"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; a "
                       "doctrinally dense discourse, among the most "
                       "significant in this chapter"),
    ],
    why=(
        "Each of the four absorptions and the first three formless "
        "dimensions is declared a basis for ending the defilements: a "
        "mendicant contemplates the phenomena present in that very "
        "attainment as impermanent, suffering, and not-self, turns the "
        "mind from them toward the peace of freedom from death, and "
        "either ends the defilements directly or is reborn spontaneously "
        "&mdash; while the top two attainments, the discourse says, can "
        "only be properly explained by meditators already skilled in "
        "them."),
    guide=[
        ("The teaching in one sentence", [
            "Each of the first seven progressive attainments &mdash; the "
            "four absorptions and the dimensions of infinite space, "
            "infinite consciousness, and nothingness &mdash; is itself a "
            "basis for ending the defilements, when a mendicant "
            "contemplates whatever occurs there as impermanent, "
            "suffering, and not-self, then turns the mind toward the "
            "peace of freedom from death."]),
        ("Absorption as insight-basis, not only calm", [
            "This is a doctrinally significant claim: rather than "
            "treating jhāna purely as a calming preliminary to insight "
            "practiced afterward, this discourse says the very "
            "phenomena constituting an absorption &mdash; its form, "
            "feeling, perception, choices, and consciousness &mdash; can "
            "themselves become insight's own object, ended right there "
            "within the attainment."]),
        ("An archer's practice, and a shared refrain", [
            "For each attainment declared a basis, the discourse "
            "supplies the identical explanation: like an archer who "
            "first trains on a straw man before becoming a marksman who "
            "shatters large objects, a mendicant contemplates the "
            "attainment's own constituents, turns away from them toward "
            "freedom from death, and either ends the defilements "
            "outright or, short of that, is reborn spontaneously through "
            "the ending of the five lower fetters."]),
        ("An explicit limit on the top two stages", [
            "The discourse closes with an unusual admission of its own "
            "boundary: penetration to enlightenment through this method "
            "extends only as far as attainments that still involve "
            "perception. The dimension of neither perception nor non-"
            "perception and the cessation of perception and feeling "
            "&mdash; the two most subtle stages &mdash; are, by the "
            "discourse's own account, properly explained only by "
            "meditators already skilled in entering and emerging from "
            "them, rather than through the insight-method this "
            "discourse has just given for the first seven."]),
    ],
    terms=[
        ("āsavānaṁ khayāya paccayo",
         "&ldquo;a basis for ending the defilements&rdquo; &mdash; the "
         "discourse's own claim for each of the first seven attainments."),
        ("aniccato dukkhato rogato gaṇḍato sallato aghato ābādhato "
         "parato palokato suññato anattato samanupassati",
         "&ldquo;impermanent, suffering, diseased, a boil, a dart, "
         "gloom, an affliction, alien, breaking apart, empty, "
         "not-self&rdquo; &mdash; the eleven-fold contemplation applied "
         "to each attainment's own constituents."),
        ("etaṁ santaṁ etaṁ paṇītaṁ",
         "&ldquo;this is peaceful; this is sublime&rdquo; &mdash; the "
         "turn from contemplating the attainment's constituents toward "
         "freedom from death itself."),
        ("dīghadassī vā gaṇṭhikkhepī",
         "&ldquo;a marksman... who shatters large objects&rdquo; "
         "&mdash; the archer simile's own culmination, matching an "
         "insight practiced within absorption to trained skill."),
        ("saññāgatāva tattha paññāpanāya",
         "&ldquo;properly explained by meditators... skilled in these "
         "attainments&rdquo; &mdash; the discourse's own explicit "
         "boundary for the top two, subtlest stages."),
    ],
    text_intro=(
        "The discourse in full: seven attainments declared bases for "
        "insight, an archer simile, and an explicit limit on the final "
        "two stages. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven attainments, each a basis for insight"),
        ("p", "&sect;1", "an9.36:1.1-4.3"),
        ("p", "&sect;2", "an9.36:6.1-7.6"),
        ("p", "&sect;3", "an9.36:8.1-9.10"),
        ("h3", "An explicit limit"),
        ("p", "&sect;4", "an9.36:10.1-10.3"),
    ],
    quiz=[
        {"q": "What does this discourse claim about the first seven "
              "progressive attainments?",
         "opts": [
             "That they are merely preliminary calm, useless for insight",
             "That each one is itself a basis for ending the "
             "defilements, when its own constituents are contemplated "
             "rightly",
             "That only the first absorption can end defilements",
             "That they should be avoided entirely"],
         "correct": 1,
         "expl": "A doctrinally significant claim about jhāna as "
                 "insight-basis, not only calm."},
        {"q": "What does a mendicant contemplate within each attainment, "
              "according to this discourse?",
         "opts": [
             "Nothing; the attainment is simply enjoyed",
             "The attainment's own constituents — form, feeling, "
             "perception, choices, consciousness — as impermanent, "
             "suffering, and not-self",
             "Only physical sensations",
             "A separate object unrelated to the attainment"],
         "correct": 1,
         "expl": "Insight practiced on the attainment's own present "
                 "phenomena, not elsewhere."},
        {"q": "What simile illustrates the skill this insight requires?",
         "opts": [
             "The wild mountain cow of AN 9.35",
             "An archer who trains on a straw man before becoming a "
             "marksman who shatters large objects",
             "A stone post unmoved by storms",
             "A wild bull elephant seeking solitude"],
         "correct": 1,
         "expl": "Trained skill, developed progressively, matching the "
                 "insight practiced within absorption."},
        {"q": "What happens if a mendicant doesn't fully end the "
              "defilements while practicing this way?",
         "opts": [
             "They lose the attainment entirely",
             "With the ending of the five lower fetters, they're reborn "
             "spontaneously and are not liable to return from that world",
             "They must start over from the first absorption",
             "Nothing further is said about this case"],
         "correct": 1,
         "expl": "A fallback outcome — non-return — short of full "
                 "liberation."},
        {"q": "What explicit limit does this discourse name for the top "
              "two attainments?",
         "opts": [
             "They don't exist",
             "Penetration to enlightenment by this method extends only "
             "as far as attainments with perception; the top two are "
             "properly explained only by meditators already skilled in "
             "them",
             "They can only be reached by arahants",
             "They are identical to the first seven"],
         "correct": 1,
         "expl": "An explicit boundary the discourse admits for its own "
                 "insight-method."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, without narrative frame."},
    ],
    marginalia=[
        ("Insight within absorption", [
            "form, feeling, perception,",
            "choices, consciousness &mdash;",
            "seen as not-self, right there",
        ]),
        ("An archer's trained skill", [
            "straw man, then large game &mdash;",
            "insight practiced in jhāna",
            "sharpens the same way",
        ]),
        ("A limit, named outright", [
            "seven stages explained;",
            "the top two, only by",
            "those already skilled",
        ]),
        ("Cross-references", [
            "AN 9.35 &middot; previous, The Simile of the Cow",
            "AN 9.37 &middot; next, By Ānanda",
        ]),
    ],
    further=[
        '<a href="%s/an9.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.35.html">AN 9.35 &middot; The Simile of the Cow</a> &mdash; previous.',
        '<a href="an-9.37.html">AN 9.37 &middot; By Ānanda</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.37 — Ānandasutta
# --------------------------------------------------------------------------- #
page(
    37, "Ānanda", "By Ānanda",
    vagga=VAGGA_4,
    meta_title="AN 9.37 — By Ānanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ānandasutta, in which Ānanda explains how a mendicant can be "
        "percipient yet not experience a sense-field that is fully "
        "present, then recalls a nun's question about a distinct "
        "immersion. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kosambī, in Ghosita's Monastery"),
        ("Speakers", "Venerable Ānanda, Venerable Udāyī, and, by report, "
                     "the nun Jaṭilagāhikā"),
        ("Form", "A declaration on the sense fields, a direct challenge, "
                 "an answer through the formless dimensions, and a "
                 "recalled dialogue"),
        ("Length", "~3 minutes to read"),
        ("A different angle on the same territory", "Rather than the "
         "full nine-stage sequence, this discourse focuses narrowly on "
         "the first three formless dimensions and a further immersion "
         "not identified with any of the nine"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "subtle phenomenological puzzle about presence "
                       "and experience"),
    ],
    why=(
        "Ānanda declares it incredible that the Buddha has found an "
        "opening amid confinement: the eye and sights are both actually "
        "present, yet one need not experience that sense-field &mdash; "
        "and when Udāyī challenges whether such a person is percipient "
        "at all, Ānanda explains through the first three formless "
        "dimensions, then recalls a nun's own question about a further "
        "immersion whose fruit the Buddha named as enlightenment itself."),
    guide=[
        ("The teaching in one sentence", [
            "Though the eye and sights, the ear and sounds, and each "
            "sense faculty and its object remain actually present, a "
            "mendicant can go beyond experiencing that sense-field "
            "altogether by entering the formless dimensions &mdash; "
            "genuinely percipient throughout, not non-percipient, but "
            "perceiving something else entirely."]),
        ("An opening amid confinement", [
            "Ānanda's declaration is a striking image in its own right: "
            "ordinary experience is confinement, boxed in by the five "
            "physical senses and their objects, and what the Buddha "
            "found is a genuine opening within that confinement, not an "
            "escape from the body but a way of no longer being bound by "
            "what remains fully present to it."]),
        ("Percipient, but not non-percipient", [
            "Udāyī's challenge cuts to the heart of the matter: if "
            "someone doesn't experience a sense-field that's right "
            "there, are they percipient at all? Ānanda's answer is "
            "precise &mdash; not non-percipient, but perceiving in a "
            "specific, nameable way, through the dimension of infinite "
            "space, infinite consciousness, or nothingness in turn, each "
            "one crowding out ordinary sense experience with its own "
            "distinct perception."]),
        ("A recalled question, and a striking answer", [
            "Ānanda closes by recalling his own past encounter with the "
            "nun Jaṭilagāhikā, who asked what fruit the Buddha named for "
            "an immersion &lsquo;that does not lean forward or pull "
            "back, and is not held in place by forceful "
            "suppression&rsquo; &mdash; free, stable, content, and "
            "unanxious. The Buddha's answer, which Ānanda simply repeats "
            "here without further comment, names the fruit of that "
            "immersion as nothing less than enlightenment itself."]),
    ],
    terms=[
        ("sambādhe okāsādhigamo",
         "&ldquo;an opening amid confinement&rdquo; &mdash; Ānanda's own "
         "opening image for what the Buddha has found and taught."),
        ("taṁ āyatanaṁ na paṭisaṁvedeti",
         "&ldquo;one will not experience that sense-field&rdquo; "
         "&mdash; the puzzle Ānanda names for each of the five physical "
         "senses in turn."),
        ("saññī va so hoti, no asaññī",
         "&ldquo;actually percipient, not non-percipient&rdquo; "
         "&mdash; Ānanda's precise answer to Udāyī's challenge."),
        ("na cāpi anāyūhaṁ, no ca sasaṅkhāraniggayhavāritavato",
         "&ldquo;does not lean forward or pull back, and is not held in "
         "place by forceful suppression&rdquo; &mdash; the nun "
         "Jaṭilagāhikā's own description of the immersion she asks "
         "about."),
        ("aññā tissā samādhissa phalanti",
         "&ldquo;the fruit of this immersion is enlightenment&rdquo; "
         "&mdash; the Buddha's own answer, recalled and repeated by "
         "Ānanda without further elaboration."),
    ],
    text_intro=(
        "The discourse in full: a declaration on the sense fields, a "
        "challenge, an answer through the formless dimensions, and a "
        "recalled dialogue with a nun. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "An opening amid confinement"),
        ("p", "&sect;1", "an9.37:1.1-2.7"),
        ("h3", "Percipient, but not non-percipient"),
        ("p", "&sect;2", "an9.37:3.1-6.2"),
        ("h3", "A recalled question, and a striking answer"),
        ("p", "&sect;3", "an9.37:7.1-8.5"),
    ],
    quiz=[
        {"q": "What does Ānanda declare incredible about the Buddha's "
              "discovery?",
         "opts": [
             "That the Buddha can read minds",
             "That an opening amid confinement has been found — a "
             "sense-field can be actually present and yet not "
             "experienced",
             "That the Buddha never sleeps",
             "That the Buddha has ended all disease"],
         "correct": 1,
         "expl": "Ordinary sense experience as confinement, with a "
                 "genuine opening within it."},
        {"q": "What challenge does Udāyī raise?",
         "opts": [
             "Whether the Buddha's teaching is authentic",
             "Whether someone who doesn't experience a present sense-"
             "field is percipient at all, or not",
             "Whether Ānanda has the authority to teach",
             "Whether the formless dimensions actually exist"],
         "correct": 1,
         "expl": "A precise phenomenological question about awareness "
                 "itself."},
        {"q": "How does Ānanda answer Udāyī's challenge?",
         "opts": [
             "By admitting such a person is non-percipient",
             "That such a person is percipient, not non-percipient — "
             "perceiving through the formless dimensions instead of the "
             "ordinary senses",
             "By refusing to answer",
             "By changing the subject entirely"],
         "correct": 1,
         "expl": "A precise distinction: not absence of perception, but "
                 "a different object of perception."},
        {"q": "Who is Jaṭilagāhikā, and what does she ask Ānanda?",
         "opts": [
             "A queen asking about taxation",
             "A nun who asks what fruit the Buddha named for an "
             "immersion that doesn't lean forward, pull back, or rely "
             "on forceful suppression",
             "A wanderer challenging the five precepts",
             "A deity asking about rebirth"],
         "correct": 1,
         "expl": "A recalled past encounter, closing this discourse."},
        {"q": "What fruit does the Buddha name for the immersion "
              "Jaṭilagāhikā asks about?",
         "opts": [
             "Rebirth in a heavenly realm",
             "Enlightenment itself",
             "Long life", "Freedom from illness"],
         "correct": 1,
         "expl": "A striking, unelaborated answer that Ānanda simply "
                 "repeats."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, in the Bamboo Grove",
             "Kosambī, in Ghosita's Monastery",
             "Cālikā, on the Cālikā mountain"],
         "correct": 2,
         "expl": "A different setting from most of this chapter's other "
                 "discourses."},
    ],
    marginalia=[
        ("An opening amid confinement", [
            "eye and sights both present,",
            "yet not experienced &mdash;",
            "an opening within",
        ]),
        ("Percipient, differently", [
            "not non-percipient &mdash;",
            "space, consciousness,",
            "nothingness, instead",
        ]),
        ("A nun's question, recalled", [
            "not forced, not pulled back &mdash;",
            "its fruit, Ānanda says,",
            "is enlightenment itself",
        ]),
        ("Cross-references", [
            "AN 9.36 &middot; previous, Depending on Absorption",
            "AN 9.38 &middot; next, Brahmin Cosmologists",
        ]),
    ],
    further=[
        '<a href="%s/an9.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.36.html">AN 9.36 &middot; Depending on Absorption</a> &mdash; previous.',
        '<a href="an-9.38.html">AN 9.38 &middot; Brahmin Cosmologists</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.38 — Lokāyatikasutta
# --------------------------------------------------------------------------- #
page(
    38, "Lokāyatika", "Brahmin Cosmologists",
    vagga=VAGGA_4,
    meta_title="AN 9.38 — Brahmin Cosmologists | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Brahmin Cosmologists, in which the Buddha sidesteps a debate "
        "over whether the cosmos is finite or infinite, redefines "
        "&lsquo;the world&rsquo; as the five sensual stimulations, and "
        "maps the nine attainments as stages toward crossing it. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Two brahmin cosmologists and the Buddha"),
        ("Form", "A reported doctrinal dispute, a declined arbitration, "
                 "a simile of four impossibly fast runners, and the nine "
                 "attainments reframed as stages of crossing the world"),
        ("Length", "~4 minutes to read"),
        ("Redefining the question rather than answering it", "The "
         "brahmins ask whether the cosmos is finite or infinite; the "
         "Buddha declines to adjudicate and redefines &lsquo;the "
         "world&rsquo; entirely"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "philosophically sharp redirection, worth reading "
                       "for its own logic"),
    ],
    why=(
        "Two brahmin cosmologists ask the Buddha to arbitrate between "
        "Pūraṇa Kassapa's claim that the cosmos is infinite and the Jain "
        "ascetic's claim that it is finite; rather than taking a side, "
        "the Buddha tells of four impossibly fast runners who could "
        "never reach the world's end by traveling, then redefines "
        "&lsquo;the world&rsquo; as the five kinds of sensual "
        "stimulation, mapping each of the nine progressive attainments "
        "as a stage of meditating at, though not yet beyond, that "
        "world's end."),
    guide=[
        ("The teaching in one sentence", [
            "The five kinds of sensual stimulation are called "
            "&lsquo;the world&rsquo; in the training of the Noble One; a "
            "mendicant meditating in any of the first eight progressive "
            "attainments has gone to the end of that world but hasn't "
            "yet left it, and only the ninth, the cessation of "
            "perception and feeling, actually crosses over clinging to "
            "it."]),
        ("A dispute declined, not settled", [
            "Two brahmins report a genuine contradiction: one teacher "
            "claims infinite knowledge that the cosmos is infinite, "
            "another claims infinite knowledge that it is finite. The "
            "Buddha's response is not to pick a side or split the "
            "difference, but to set the entire question aside as the "
            "wrong question to be asking."]),
        ("Four runners who could never arrive", [
            "The simile is deliberately extravagant: four men, each as "
            "fast as a well-shot arrow, with strides spanning ocean to "
            "ocean, running for a full hundred-year lifespan, would still "
            "die along the way without reaching the end of the physical "
            "world. The point isn't that the cosmos is literally that "
            "vast, but that &lsquo;the end of the world&rsquo; was never "
            "a place reachable by traveling in the first place."]),
        ("A different world, reachable by a different method", [
            "The Buddha's redefinition is the discourse's real move: "
            "&lsquo;the world&rsquo; that actually matters for ending "
            "suffering is the five kinds of sensual stimulation, not "
            "physical cosmology. Each of the first eight progressive "
            "attainments is a way of meditating at this world's edge, "
            "though a mendicant there is still, by the Buddha's own "
            "admission, &lsquo;included in the world, and hasn't yet "
            "left it&rsquo; &mdash; only the ninth attainment actually "
            "crosses over."]),
    ],
    terms=[
        ("lokāyatikā brāhmaṇā",
         "&ldquo;brahmin cosmologists&rdquo; &mdash; this discourse's "
         "own title, naming the two questioners' area of doctrinal "
         "specialization."),
        ("anantavā loko... antavā loko",
         "&ldquo;the cosmos is infinite... the cosmos is finite&rdquo; "
         "&mdash; the two contradictory claims the brahmins ask the "
         "Buddha to arbitrate."),
        ("na ca kho ahaṁ, brāhmaṇā, appatvā lokassa antaṁ dukkhassa "
         "antakiriyaṁ vadāmi",
         "&ldquo;there's no making an end of suffering without reaching "
         "the end of the world&rdquo; &mdash; the Buddha's own pivot, "
         "before redefining what &lsquo;the world&rsquo; means."),
        ("pañca kāmaguṇā ariyassa vinaye loko vuccati",
         "&ldquo;these five kinds of sensual stimulation are called the "
         "world in the training of the Noble One&rdquo; &mdash; the "
         "discourse's own redefinition, replacing physical cosmology."),
        ("lokantagato lokante jhāyati... lokasmiṁ loke aniyyāto",
         "&ldquo;having gone to the end of the world, meditates at the "
         "end of the world... included in the world, and hasn't yet left "
         "the world&rdquo; &mdash; the discourse's own formula applied "
         "to each of the first eight attainments."),
    ],
    text_intro=(
        "The discourse in full: a declined dispute, four impossibly "
        "fast runners, and the nine attainments reframed as stages of "
        "crossing the world. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A dispute, declined"),
        ("p", "&sect;1", "an9.38:1.1-3.7"),
        ("h3", "Four runners who could never arrive"),
        ("p", "&sect;2", "an9.38:4.1-4.14"),
        ("h3", "A different world, crossed by a different method"),
        ("p", "&sect;3", "an9.38:5.1-6.6"),
        ("p", "&sect;4", "an9.38:7.1-10.2"),
    ],
    quiz=[
        {"q": "What contradictory claims do the two brahmins ask the "
              "Buddha to arbitrate?",
         "opts": [
             "Whether the self exists",
             "Whether the cosmos is infinite (Pūraṇa Kassapa's claim) or "
             "finite (the Jain ascetic's claim)",
             "Whether rebirth exists",
             "Whether ethics matters"],
         "correct": 1,
         "expl": "Two teachers, both claiming infinite knowledge, "
                 "directly contradicting each other."},
        {"q": "How does the Buddha respond to the brahmins' request for "
              "arbitration?",
         "opts": [
             "He sides with Pūraṇa Kassapa",
             "He sides with the Jain ascetic",
             "He declines to adjudicate and redirects the question "
             "entirely",
             "He refuses to speak with them at all"],
         "correct": 2,
         "expl": "Neither taking a side nor splitting the difference — "
                 "setting the question aside."},
        {"q": "What does the simile of the four fast runners "
              "illustrate?",
         "opts": [
             "That the cosmos is exactly as vast as described",
             "That &lsquo;the end of the world&rsquo; was never reachable "
             "by traveling in the first place",
             "That running is a form of meditation",
             "That the Buddha endorses physical exploration"],
         "correct": 1,
         "expl": "A deliberately extravagant image making a point about "
                 "method, not literal distance."},
        {"q": "What does the Buddha redefine &lsquo;the world&rsquo; as, "
              "in the training of the Noble One?",
         "opts": [
             "The physical cosmos in its entirety",
             "The five kinds of sensual stimulation",
             "The realm of the gods only",
             "The monastic community"],
         "correct": 1,
         "expl": "A redefinition that shifts the whole inquiry away from "
                 "cosmology."},
        {"q": "According to this discourse, what is true of a mendicant "
              "meditating in any of the first eight progressive "
              "attainments?",
         "opts": [
             "They have already fully left the world",
             "They have gone to the end of the world but haven't yet "
             "left it — still included in the world",
             "They have not made any progress at all",
             "They have attained full awakening"],
         "correct": 1,
         "expl": "Only the ninth attainment, per this discourse, "
                 "actually crosses over."},
        {"q": "What finally crosses over clinging to the world, "
              "according to this discourse?",
         "opts": [
             "The fourth absorption",
             "The dimension of nothingness",
             "The cessation of perception and feeling, the ninth "
             "attainment",
             "Simply believing the Buddha's teaching"],
         "correct": 2,
         "expl": "The same ninth attainment singled out across several "
                 "discourses in this chapter."},
    ],
    marginalia=[
        ("A dispute, declined", [
            "infinite or finite &mdash;",
            "the Buddha sets aside",
            "the whole question",
        ]),
        ("Four runners, no arrival", [
            "ocean-spanning strides,",
            "a hundred years running &mdash;",
            "never reaching the end",
        ]),
        ("A different world entirely", [
            "the five sense pleasures",
            "are &lsquo;the world&rsquo; that matters &mdash;",
            "crossed only at the ninth",
        ]),
        ("Cross-references", [
            "AN 9.32 &middot; the same nine attainments, here mapped as "
            "stages of crossing the world",
            "AN 9.37 &middot; previous, By Ānanda",
            "AN 9.39 &middot; next, The War Between the Gods and the "
            "Titans",
        ]),
    ],
    further=[
        '<a href="%s/an9.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.37.html">AN 9.37 &middot; By Ānanda</a> &mdash; previous.',
        '<a href="an-9.39.html">AN 9.39 &middot; The War Between the Gods and the Titans</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.39 — Devāsurasaṅgāmasutta
# --------------------------------------------------------------------------- #
page(
    39, "Devāsurasaṅgāma", "The War Between the Gods and the Titans",
    vagga=VAGGA_4,
    meta_title=("AN 9.39 — The War Between the Gods and the Titans | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The "
        "War Between the Gods and the Titans, a vivid mythic battle "
        "narrative — told twice, with reversed outcomes — mapped onto "
        "each absorption's temporary safety from Māra. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A mythic battle narrative told twice with reversed "
                 "outcomes, then mapped onto the nine attainments and "
                 "Māra"),
        ("Length", "~3 minutes to read"),
        ("The most mythic narrative in this chapter", "Unlike most of "
         "this chapter's meditation teachings, this discourse opens with "
         "an extended cosmic battle myth before turning to its "
         "meditative application"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "vivid, symmetrical narrative worth reading for "
                       "its own drama before its application"),
    ],
    why=(
        "The gods, defeated three times by the titans, retreat to the "
        "safety of their own castle and think themselves secure while "
        "the titans, unable to follow, think the same; the same battle "
        "is then told in reverse, the titans defeated and fleeing to "
        "their own citadel &mdash; and each of the four absorptions "
        "gives a mendicant this same temporary sense of security from "
        "Māra, while the formless attainments go further still, "
        "blinding Māra outright."),
    guide=[
        ("The teaching in one sentence", [
            "Just as gods and titans, whichever side wins three "
            "successive battles, each retreat to their own fortress "
            "believing themselves secure from a pursuer who now can't "
            "reach them, a mendicant absorbed in any of the four "
            "jhānas thinks &lsquo;Māra can't do anything to me,&rsquo; "
            "and Māra, unable to follow, thinks the same &mdash; while "
            "the formless attainments go further, blinding Māra "
            "outright."]),
        ("One myth, told twice in mirror image", [
            "The discourse's real narrative craft is its symmetry: the "
            "gods lose three battles running and flee north into their "
            "castle, and then, without missing a beat, the identical "
            "battle is retold with the titans losing three times and "
            "fleeing south into their own citadel. Neither side is the "
            "permanent winner; the pattern of temporary safety through "
            "retreat is what repeats."]),
        ("A stalemate, not a victory", [
            "What each side gains by retreating to its fortress is "
            "explicitly not triumph but mutual inaccessibility: the gods "
            "think the titans can't reach them, the titans think the "
            "same about the gods. This is the precise image the "
            "discourse maps onto absorption &mdash; not a defeat of "
            "Māra, but a temporary standoff where neither side can act "
            "on the other."]),
        ("From stalemate to genuinely blinding Māra", [
            "The four absorptions each produce only this stalemate: "
            "&lsquo;Māra can't do anything to me,&rsquo; matched by "
            "Māra's own equally accurate &lsquo;we can't do anything to "
            "the mendicant.&rsquo; The formless attainments mark a "
            "genuine escalation beyond stalemate: entering the dimension "
            "of infinite space, a mendicant is said to have "
            "&lsquo;blinded Māra, put out his eyes without a trace, and "
            "gone where the Wicked One cannot see&rsquo; &mdash; no "
            "longer a standoff, but total loss of Māra's own vision."]),
    ],
    terms=[
        ("devāsurasaṅgāmo",
         "&ldquo;the war between the gods and the titans&rdquo; &mdash; "
         "this discourse's own title, a battle told twice with reversed "
         "outcomes."),
        ("suraṭṭhaṁ devānaṁ pavisiṁsu",
         "&ldquo;fled right into the castle of the gods&rdquo; &mdash; "
         "the gods' retreat after three lost battles, mirrored later by "
         "the titans' own citadel."),
        ("na dāni amhākaṁ asurā kiñci karissantīti",
         "&ldquo;now the titans can't do anything to us&rdquo; &mdash; "
         "the gods' own thought inside their fortress, matched exactly "
         "by the titans' identical thought about the gods."),
        ("khemantabhūmiṁyeva pattoti maññati",
         "&ldquo;I'm in a secure location&rdquo; &mdash; the "
         "discourse's own phrase for a mendicant's thought while "
         "absorbed in any of the four jhānas."),
        ("andhamakāsi māraṁ apadaṁ vadhitvā cakkhumā",
         "&ldquo;blinded Māra, put out his eyes without a trace&rdquo; "
         "&mdash; the discourse's own escalation, marking entry into "
         "the formless dimensions as beyond mere stalemate."),
    ],
    text_intro=(
        "The discourse in full: the mythic battle told twice with "
        "reversed outcomes, then mapped onto the four absorptions and "
        "the formless dimensions. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "The gods lose three battles, and retreat"),
        ("p", "&sect;1", "an9.39:1.1-2.10"),
        ("h3", "The same battle, told in reverse"),
        ("p", "&sect;2", "an9.39:3.1-4.10"),
        ("h3", "From stalemate to blinding Māra"),
        ("p", "&sect;3", "an9.39:5.1-6.7"),
        ("p", "&sect;4", "an9.39:7.1-8.5"),
    ],
    quiz=[
        {"q": "How is the mythic battle between gods and titans "
              "structured in this discourse?",
         "opts": [
             "Told once, with the gods as permanent winners",
             "Told twice, in mirror image — first the gods losing three "
             "battles and retreating, then the titans losing three "
             "battles and retreating",
             "Told once, with no clear winner",
             "Told three separate times with three different outcomes"],
         "correct": 1,
         "expl": "A deliberately symmetrical narrative, neither side "
                 "permanently victorious."},
        {"q": "What do both the gods and the titans think once safely "
              "in their own fortress?",
         "opts": [
             "That they have permanently defeated the other side",
             "That they are now secure and the other side can't do "
             "anything to them — a thought both sides share equally",
             "That they should attack again immediately",
             "That the war is meaningless"],
         "correct": 1,
         "expl": "A mutual stalemate, not a one-sided triumph."},
        {"q": "What does each of the four absorptions produce, according "
              "to this discourse's application of the myth?",
         "opts": [
             "Permanent defeat of Māra",
             "The same kind of stalemate: the mendicant thinks Māra "
             "can't act on them, and Māra thinks the same",
             "No effect on Māra at all",
             "Māra's complete destruction"],
         "correct": 1,
         "expl": "Matching the gods' and titans' own mutual, temporary "
                 "safety."},
        {"q": "What happens once a mendicant enters the formless "
              "attainments, beginning with infinite space?",
         "opts": [
             "Nothing changes from the jhānas",
             "The mendicant is said to have blinded Māra outright, going "
             "where he cannot see — a genuine escalation beyond "
             "stalemate",
             "Māra gains greater power over the mendicant",
             "The mendicant returns to ordinary consciousness"],
         "correct": 1,
         "expl": "No longer a standoff, but total loss of Māra's vision."},
        {"q": "According to the guide, what makes this discourse "
              "distinctive within this chapter?",
         "opts": [
             "It contains no meditative application at all",
             "It opens with an extended cosmic battle myth before "
             "turning to its meditative application, unlike most other "
             "discourses here",
             "It is the shortest discourse in the chapter",
             "It rejects the nine-attainment framework entirely"],
         "correct": 1,
         "expl": "The most mythic narrative in this meditation-heavy "
                 "chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A mythic teaching narrative without a specific "
                 "historical setting."},
    ],
    marginalia=[
        ("A battle, told twice", [
            "gods flee north, defeated;",
            "then titans flee south &mdash;",
            "the same myth, reversed",
        ]),
        ("A mutual stalemate", [
            "&ldquo;now they can't reach us&rdquo; &mdash;",
            "both sides think the same,",
            "safe in their own walls",
        ]),
        ("From standoff to blindness", [
            "jhāna: a stalemate;",
            "formless: Māra blinded,",
            "eyes put out, gone where",
        ]),
        ("Cross-references", [
            "AN 9.32 &middot; the same nine attainments, here mapped "
            "onto safety from Māra",
            "AN 9.38 &middot; previous, Brahmin Cosmologists",
            "AN 9.40 &middot; next, The Simile of the Bull Elephant in "
            "the Forest",
        ]),
    ],
    further=[
        '<a href="%s/an9.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.38.html">AN 9.38 &middot; Brahmin Cosmologists</a> &mdash; previous.',
        '<a href="an-9.40.html">AN 9.40 &middot; The Simile of the Bull Elephant in the '
        "Forest</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.40 — Nāgasutta
# --------------------------------------------------------------------------- #
page(
    40, "Nāga", "The Simile of the Bull Elephant in the Forest",
    vagga=VAGGA_4,
    meta_title=("AN 9.40 — The Simile of the Bull Elephant in the Forest | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nāgasutta, mapping a wild bull elephant's withdrawal from a "
        "crowded herd onto a mendicant's solitary progress through the "
        "nine attainments, each marked by the same disarming refrain. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "An extended animal simile of withdrawal from a crowd, "
                 "mapped onto solitary practice through all nine "
                 "attainments"),
        ("Length", "~4 minutes to read"),
        ("An unusually physical, homely refrain", "Each attainment in "
         "this discourse closes not with a doctrinal claim but with the "
         "same disarming physical image: happily relieving an itch"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "vivid, relatable simile carrying a genuinely "
                       "substantial teaching"),
    ],
    why=(
        "A wild bull elephant, crowded by other elephants who trample "
        "his grass, eat his broken branches, muddy his pool, and bump "
        "into him, withdraws to live alone and finally scratches himself "
        "with a branch, happily relieving his itches &mdash; and a "
        "mendicant crowded by monastics and laypeople alike withdraws in "
        "just the same way to a secluded lodging, gives up the five "
        "hindrances, and progresses through all nine attainments, each "
        "one likewise a relief."),
    guide=[
        ("The teaching in one sentence", [
            "Just as a wild bull elephant, crowded and jostled by its "
            "herd, withdraws alone to eat untrampled grass and drink "
            "clear water, a mendicant crowded by the fourfold assembly "
            "and outsiders withdraws to a secluded lodging, gives up the "
            "five hindrances, and progresses through all nine "
            "attainments, each one described as happily relieving an "
            "itch."]),
        ("Four specific irritations, named in full", [
            "The elephant simile doesn't gesture vaguely at crowding; it "
            "names four concrete irritations in turn &mdash; trampled "
            "grass, stolen branches, muddied water, and female elephants "
            "bumping into him after his bath &mdash; each one a small, "
            "recognizable indignity rather than a single abstract "
            "complaint."]),
        ("From physical crowding to human crowding", [
            "The mapping onto human life is precise: a mendicant is "
            "crowded specifically by monks, nuns, laymen, laywomen, "
            "rulers and their ministers, and monastics of other "
            "religions &mdash; the full range of people who might press "
            "in on someone's attention, not merely a vague social "
            "burden."]),
        ("A disarming, physical refrain", [
            "Where most discourses in this chapter close each "
            "attainment with a doctrinal claim, this one closes every "
            "single stage &mdash; all nine, from the first absorption to "
            "the cessation of perception and feeling &mdash; with the "
            "same homely image: &lsquo;they happily relieve their "
            "itches,&rsquo; echoing the elephant's own branch-scratching "
            "at the simile's start and keeping the whole sequence "
            "grounded in something physically relatable rather than "
            "purely abstract."]),
    ],
    terms=[
        ("āraññako nāgo",
         "&ldquo;a wild bull elephant&rdquo; &mdash; the discourse's own "
         "title image, crowded by its herd before withdrawing alone."),
        ("ekaṁ vūpakaṭṭho vihareyyanti",
         "&ldquo;why don't I live alone, withdrawn from the herd&rdquo; "
         "&mdash; the elephant's own thought, echoed almost word for "
         "word by the mendicant in the application."),
        ("pañca nīvaraṇe pahāya",
         "&ldquo;giving up these five hindrances&rdquo; &mdash; the "
         "step a withdrawn mendicant takes before the nine attainments "
         "can properly begin."),
        ("kaṇḍūyamāno sukhaṁ seti",
         "&ldquo;happily relieving their itches&rdquo; &mdash; the "
         "shared refrain closing every one of the nine attainments in "
         "this discourse."),
        ("catūhi parisāhi rājūhi rājamahāmattehi",
         "&ldquo;monks, nuns, laymen, and laywomen; by rulers and their "
         "chief ministers&rdquo; &mdash; the specific range of people "
         "who crowd a mendicant, mapped from the elephant's own herd."),
    ],
    text_intro=(
        "The discourse in full: a wild elephant's withdrawal, mapped "
        "onto a mendicant's solitary progress through all nine "
        "attainments. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A crowded elephant, and four irritations"),
        ("p", "&sect;1", "an9.40:1.1-1.4"),
        ("h3", "Withdrawal, and relief"),
        ("p", "&sect;2", "an9.40:2.1-3.2"),
        ("h3", "The same withdrawal, applied to a mendicant"),
        ("p", "&sect;3", "an9.40:4.1-5.6"),
        ("h3", "Nine attainments, each a relief"),
        ("p", "&sect;4", "an9.40:5.7-6.7"),
    ],
    quiz=[
        {"q": "What four irritations does the crowded bull elephant "
              "experience?",
         "opts": [
             "Predators, disease, hunger, and thirst",
             "Trampled grass, stolen branches, muddied water, and female "
             "elephants bumping into him after his bath",
             "Loud noises, bright light, cold weather, and rough terrain",
             "Human hunters, forest fires, floods, and drought"],
         "correct": 1,
         "expl": "Four concrete, recognizable indignities of crowding, "
                 "not a single vague complaint."},
        {"q": "Who specifically crowds a mendicant, in the simile's "
              "human application?",
         "opts": [
             "Only other mendicants",
             "Monks, nuns, laymen, laywomen, rulers and their ministers, "
             "and monastics of other religions",
             "Only wild animals",
             "Only family members"],
         "correct": 1,
         "expl": "A precise mapping onto the full range of people who "
                 "might press in on someone's attention."},
        {"q": "What must a withdrawn mendicant give up before "
              "progressing through the nine attainments?",
         "opts": [
             "All monastic robes",
             "The five hindrances",
             "All forms of speech", "Contact with laypeople permanently"],
         "correct": 1,
         "expl": "The standard preliminary before absorption in this "
                 "and many other discourses."},
        {"q": "What refrain closes every one of the nine attainments in "
              "this discourse?",
         "opts": [
             "A doctrinal claim about impermanence",
             "&ldquo;They happily relieve their itches&rdquo;, echoing "
             "the elephant's own branch-scratching",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "An unusually homely, physical image, distinct from "
                 "most other discourses in this chapter."},
        {"q": "According to the guide, what does this physical refrain "
              "accomplish?",
         "opts": [
             "It trivializes the teaching",
             "It keeps the whole nine-stage sequence grounded in "
             "something physically relatable rather than purely "
             "abstract",
             "It replaces the need for the nine attainments entirely",
             "It contradicts the elephant simile"],
         "correct": 1,
         "expl": "Consistency between the opening simile and its "
                 "meditative application."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare simile-teaching, without narrative frame."},
    ],
    marginalia=[
        ("A crowded elephant", [
            "trampled grass, stolen",
            "branches, muddy water,",
            "jostled after his bath",
        ]),
        ("Withdrawal, and relief", [
            "alone at last, he",
            "scratches with a branch &mdash;",
            "happily relieving itches",
        ]),
        ("Nine stages, the same relief", [
            "crowded by the many,",
            "a mendicant withdraws too &mdash;",
            "each stage, an itch relieved",
        ]),
        ("Cross-references", [
            "AN 9.32 &middot; the same nine attainments, here closed by "
            "a physical refrain",
            "AN 9.39 &middot; previous, The War Between the Gods and the "
            "Titans",
            "AN 9.41 &middot; next, With the Householder Tapussa, closing "
            "this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an9.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.39.html">AN 9.39 &middot; The War Between the Gods and the Titans</a> '
        "&mdash; previous.",
        '<a href="an-9.41.html">AN 9.41 &middot; With the Householder Tapussa</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.41 — Tapussasutta — closes ch.4 Mahāvagga
# --------------------------------------------------------------------------- #
page(
    41, "Tapussa", "With the Householder Tapussa",
    vagga=VAGGA_4,
    meta_title="AN 9.41 — With the Householder Tapussa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Tapussasutta, closing this chapter with the Buddha's own "
        "autobiographical account of struggling through all nine "
        "attainments before his awakening, each requiring seeing a "
        "drawback and a benefit first. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The land of the Mallas, near Uruvelakappa"),
        ("Speakers", "The householder Tapussa, Venerable Ānanda, and the "
                     "Buddha, speaking autobiographically"),
        ("Form", "A layperson's question relayed by Ānanda, then an "
                 "extended first-person account repeating the same "
                 "structure nine times"),
        ("Length", "~9 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Mahāvagga</em>, the fourth chapter of the Nines; "
         "the source's own untranslated closing verse names all ten "
         "discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; long "
                       "and repetitive by design, but among the most "
                       "personal and revealing discourses in this "
                       "project"),
    ],
    why=(
        "The householder Tapussa tells Ānanda that renunciation seems "
        "like an abyss to laypeople who love sensual pleasure, yet young "
        "mendicants' minds leap forth into it readily; brought to the "
        "Buddha, this becomes the occasion for an extended first-person "
        "account of the Buddha's own pre-awakening struggle, in which "
        "his mind refused to settle into each successive attainment "
        "until he had first seen the drawback of the stage before it and "
        "the benefit of the one ahead."),
    guide=[
        ("The teaching in one sentence", [
            "Before his awakening, the Buddha's mind did not leap forth "
            "into any of the nine progressive attainments until he had "
            "first seen the drawback of the stage he was in and "
            "realized the benefit of the stage ahead &mdash; and only "
            "after mastering all nine in both forward and reverse order "
            "did he announce his supreme awakening."]),
        ("A layperson's honest observation", [
            "Tapussa's opening remark is refreshingly candid rather than "
            "merely rhetorical: laypeople who genuinely love sensual "
            "pleasures find renunciation abyss-like, yet somehow very "
            "young mendicants take to it with ease &mdash; a real puzzle "
            "he brings to Ānanda rather than a purely doctrinal question."]),
        ("Nine times, the same three-part struggle", [
            "The Buddha's answer reveals something rarely stated so "
            "plainly: even his own mind, before awakening, would not "
            "&lsquo;leap forth, gain confidence, settle down&rsquo; into "
            "a new attainment automatically. Each of the nine stages "
            "required first identifying why the mind was resisting "
            "(no benefit yet seen in the new stage, no drawback yet seen "
            "in the old one), then deliberately cultivating both before "
            "the mind was willing to move &mdash; and even once entered, "
            "the same affliction-logic met at AN 9.34 still applied, "
            "residual perception of the earlier stage counting against "
            "it."]),
        ("Mastery in both directions, before any declaration", [
            "The discourse's closing claim is exacting: it wasn't enough "
            "to enter all nine attainments once, moving only forward. "
            "The Buddha states plainly that he did not announce his "
            "awakening until he had entered into and withdrawn from all "
            "nine progressive attainments in both forward and reverse "
            "order &mdash; a standard of mastery this discourse alone in "
            "the chapter states explicitly, closing <em>Mahāvagga</em> "
            "on the Buddha's own most personal testimony."]),
    ],
    terms=[
        ("nekkhammaṁ papāto viya khāyati",
         "&ldquo;renunciation seems like an abyss&rdquo; &mdash; "
         "Tapussa's own candid description of how renunciation appears "
         "to laypeople who love sensual pleasure."),
        ("cittaṁ na pakkhandati nappasīdati na santiṭṭhati na "
         "vimuccati",
         "&ldquo;my mind did not leap forth, gain confidence, settle "
         "down, and become decided&rdquo; &mdash; the discourse's own "
         "shared refrain, repeated at every one of the nine stages "
         "before the Buddha's mind was willing to advance."),
        ("ādīnavaṁ adisvā, ānisaṁsaṁ ananubhavitvā",
         "&ldquo;I haven't seen the drawbacks... I haven't realized the "
         "benefits&rdquo; &mdash; the Buddha's own diagnosis for why his "
         "mind resisted each new stage, repeated nine times."),
        ("anulomapaṭilomaṁ samāpajjitvā vuṭṭhahitvā",
         "&ldquo;entered into and withdrawn from... in both forward and "
         "reverse order&rdquo; &mdash; the exacting standard of mastery "
         "the Buddha names as preceding his announcement of awakening."),
        ("akuppā me vimutti, ayamantimā jāti, natthi dāni punabbhavoti",
         "&ldquo;my freedom is unshakable; this is my last rebirth; now "
         "there'll be no more future lives&rdquo; &mdash; the "
         "discourse's closing knowledge, arising only after mastering "
         "all nine attainments in both directions."),
    ],
    text_intro=(
        "The discourse in full: Tapussa's question relayed by Ānanda, "
        "and the Buddha's own extended first-person account of "
        "struggling through all nine attainments before his awakening. "
        "The source's own closing colophon and chapter-summary verse "
        "are untranslated in the English and are described rather than "
        "quoted here. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A layperson's honest question"),
        ("p", "&sect;1", "an9.41:1.1-5.2"),
        ("h3", "&ldquo;That's so true, Ānanda!&rdquo;"),
        ("p", "&sect;2", "an9.41:7.1-7.18"),
        ("h3", "Nine times, the same struggle"),
        ("p", "&sect;3", "an9.41:8.1-8.16"),
        ("p", "&sect;4", "an9.41:9.1-9.16"),
        ("p", "&sect;5", "an9.41:10.1-10.16"),
        ("p", "&sect;6", "an9.41:11.1-11.16"),
        ("p", "&sect;7", "an9.41:12.1-12.16"),
        ("p", "&sect;8", "an9.41:13.1-13.16"),
        ("p", "&sect;9", "an9.41:14.1-14.16"),
        ("h3", "Mastery in both directions, then awakening"),
        ("p", "&sect;10", "an9.41:15.1-16.4"),
    ],
    quiz=[
        {"q": "What honest puzzle does the householder Tapussa raise "
              "with Ānanda?",
         "opts": [
             "Whether the Buddha's teachings are internally consistent",
             "That renunciation seems like an abyss to laypeople who "
             "love sensual pleasure, yet young mendicants take to it "
             "readily",
             "Whether laypeople can ever attain awakening",
             "Whether monastics should own property"],
         "correct": 1,
         "expl": "A genuine, candidly stated observation rather than a "
                 "purely doctrinal question."},
        {"q": "What refrain repeats at every one of the nine stages in "
              "the Buddha's own account?",
         "opts": [
             "A verse of praise",
             "That his mind did not leap forth, gain confidence, settle "
             "down, and become decided — until seeing both a drawback "
             "and a benefit",
             "A request for Ānanda's help",
             "A warning about Māra"],
         "correct": 1,
         "expl": "Even the Buddha's own pre-awakening mind resisted each "
                 "new stage until properly prepared."},
        {"q": "What two things does the Buddha say he needed to see "
              "before his mind would advance to each new stage?",
         "opts": [
             "Permission from a teacher and a favorable omen",
             "The drawback of the stage he was in and the benefit of "
             "the stage ahead",
             "A large donation and public recognition",
             "Physical strength and financial security"],
         "correct": 1,
         "expl": "Repeated as the diagnosis for resistance at every one "
                 "of the nine stages."},
        {"q": "What exacting standard does the Buddha name as preceding "
              "his announcement of awakening?",
         "opts": [
             "Simply entering all nine attainments once, moving forward",
             "Entering into and withdrawing from all nine attainments in "
             "both forward and reverse order",
             "Teaching the Dhamma for at least one year first",
             "Gaining the approval of five hundred mendicants"],
         "correct": 1,
         "expl": "A standard this discourse alone states explicitly in "
                 "this chapter."},
        {"q": "What does this discourse close?",
         "opts": [
             "Nothing; the chapter continues past it",
             "<em>Mahāvagga</em>, the fourth chapter, with an "
             "untranslated colophon and uddāna verse naming all ten "
             "discourses",
             "The entire nipāta",
             "Only this single discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, in the Bamboo Grove",
             "The land of the Mallas, near Uruvelakappa",
             "Kosambī, in Ghosita's Monastery"],
         "correct": 2,
         "expl": "A distinctive setting, closing this chapter on a "
                 "personal note."},
    ],
    marginalia=[
        ("A layperson's honest puzzle", [
            "renunciation, an abyss &mdash;",
            "yet the very young",
            "leap into it with ease",
        ]),
        ("Even the Buddha resisted", [
            "no leap, no confidence,",
            "until drawback and benefit",
            "were both first seen",
        ]),
        ("Mastery, both directions", [
            "forward, then reverse &mdash;",
            "only then, awakening",
            "announced to the world",
        ]),
        ("Cross-references", [
            "AN 9.34 &middot; the same affliction-logic applied within "
            "each stage",
            "AN 9.40 &middot; previous, The Simile of the Bull Elephant "
            "in the Forest",
            "AN 9.42 &middot; next, opening ch.5, Sāmaññavagga",
        ]),
    ],
    further=[
        '<a href="%s/an9.41/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.34.html">AN 9.34 &middot; Extinguishment is Bliss</a> &mdash; the same '
        "affliction-logic applied within each stage.",
        '<a href="an-9.40.html">AN 9.40 &middot; The Simile of the Bull Elephant in the '
        "Forest</a> &mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# ch.5 — Sāmaññavagga (AN 9.42-51), closing the First Fifty. Ten discourses,
# every one an Udāyī-to-Ānanda dialogue defining a different technical term
# by running the same nine attainments through a shared qualified-vs-
# definitive structure. The chapter's own name, "Similarity," names this
# structural sameness directly. AN 9.48-50 are the most minimal stubs met
# anywhere in this project so far -- literally one segment of English text
# each, an ordinal number, and nothing else, relying entirely on the shared
# template established at AN 9.42-47.
# --------------------------------------------------------------------------- #
VAGGA_5 = "<em>Sāmaññavagga</em> &mdash; the fifth chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.42 — Sambādhasutta — the template-setter for this whole chapter
# --------------------------------------------------------------------------- #
page(
    42, "Sambādha", "Cramped",
    vagga=VAGGA_5,
    meta_title="AN 9.42 — Cramped | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sambādhasutta, opening a chapter of near-identical dialogues by "
        "naming exactly what still confines a mendicant at each of the "
        "first eight attainments. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from Udāyī and "
                    "Ānanda's setting at Kosambī, Ghosita's Monastery"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, "
                     "quoting a godling's verse"),
        ("Form", "A quoted verse, a question, and nine attainments each "
                 "named as an opening &lsquo;in a qualified sense&rsquo; "
                 "&mdash; except the last, definitive"),
        ("Length", "~3 minutes to read"),
        ("This chapter's template-setter", "Nine more discourses follow "
         "this same qualified-versus-definitive structure, applied to a "
         "different technical term each time"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "most detailed discourse in this chapter, worth "
                       "reading closely before the rest"),
    ],
    why=(
        "Quoting a godling's verse praising the Buddha for discovering "
        "&lsquo;the opening amid confinement,&rsquo; Udāyī asks Ānanda "
        "what confinement actually is &mdash; and Ānanda answers that "
        "the five kinds of sensual stimulation are confinement, that "
        "each of the first eight attainments offers only a qualified "
        "opening because something specific still hasn't ceased there, "
        "and that only the ninth, the cessation of perception and "
        "feeling, is an opening in the fullest, definitive sense."),
    guide=[
        ("The teaching in one sentence", [
            "The five kinds of sensual stimulation are &lsquo;"
            "confinement&rsquo;; each of the first eight attainments "
            "opens a way out of confinement only in a qualified sense, "
            "since some specific remaining factor &mdash; unceased "
            "placing of the mind, rapture, form-perception, and so on "
            "&mdash; is itself still confinement there; only the "
            "cessation of perception and feeling opens it in a fully "
            "definitive sense."]),
        ("A quoted verse, taken seriously", [
            "Udāyī doesn't simply ask Ānanda to define a term in the "
            "abstract; he quotes a specific verse attributed to the "
            "godling Pañcālacaṇḍa praising the Buddha as &lsquo;the sage, "
            "the solitary boss bull&rsquo; who discovered this opening "
            "&mdash; grounding the whole technical discussion that "
            "follows in a devotional and poetic source, not just "
            "doctrine for its own sake."]),
        ("What specifically still confines, at each stage", [
            "Unlike most of this chapter's remaining discourses, this "
            "one doesn't merely repeat a bare formula at each "
            "attainment; it names the specific residual factor that "
            "still counts as confinement there &mdash; unceased placing "
            "of the mind at the first absorption, unceased rapture at "
            "the second, unceased bliss-with-equanimity at the third, "
            "and so on through unceased perception at each of the "
            "formless dimensions."]),
        ("This chapter's own template, set here first", [
            "The phrase this discourse repeats at each stage &mdash; "
            "&lsquo;to this extent the Buddha spoke of X in a qualified "
            "sense... but it is still confined... only at the ninth "
            "stage, in a definitive sense&rsquo; &mdash; is the exact "
            "structural template that AN 9.43 through AN 9.51 all reuse, "
            "substituting a different technical term for "
            "&lsquo;confinement&rsquo; each time. This chapter's own "
            "name, <em>Sāmaññavagga</em>, &ldquo;the Chapter on "
            "Similarity,&rdquo; names this structural sameness directly."]),
    ],
    terms=[
        ("sambādho",
         "&ldquo;confinement, cramped&rdquo; &mdash; this discourse's "
         "own title term, identified with the five kinds of sensual "
         "stimulation."),
        ("okāsādhigamo",
         "&ldquo;the opening amid confinement&rdquo; &mdash; the "
         "godling's own phrase, quoted by Udāyī, echoing Ānanda's "
         "identical language at AN 9.37."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; the discourse's own "
         "term for what the first eight attainments each offer, short of "
         "the full opening."),
        ("yo tattha vitakko avūpasanto, ayaṁ tattha sambādho",
         "&ldquo;whatever placing of the mind has not ceased is the "
         "confinement there&rdquo; &mdash; the specific residual factor "
         "named for the first absorption."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved solely "
         "for the ninth attainment, the cessation of perception and "
         "feeling."),
    ],
    text_intro=(
        "The discourse in full: a quoted verse, a question, and each of "
        "the nine attainments named as a qualified opening except the "
        "definitive ninth. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A quoted verse, and a question"),
        ("p", "&sect;1", "an9.42:1.1-3.1"),
        ("h3", "Confinement named, and what still confines"),
        ("p", "&sect;2", "an9.42:3.2-4.5"),
        ("p", "&sect;3", "an9.42:5.1-5.5"),
        ("p", "&sect;4", "an9.42:6.1-6.5"),
        ("p", "&sect;5", "an9.42:7.1-7.5"),
        ("p", "&sect;6", "an9.42:8.1-8.5"),
        ("p", "&sect;7", "an9.42:9.1-9.5"),
        ("p", "&sect;8", "an9.42:10.1-10.5"),
        ("p", "&sect;9", "an9.42:11.1-11.5"),
        ("h3", "The definitive opening"),
        ("p", "&sect;10", "an9.42:12.1-12.2"),
    ],
    quiz=[
        {"q": "What does Udāyī quote at the start of this discourse?",
         "opts": [
             "A rule from the monastic code",
             "A verse attributed to the godling Pañcālacaṇḍa praising "
             "the Buddha for discovering &lsquo;the opening amid "
             "confinement&rsquo;",
             "A parable about a cow",
             "A mathematical riddle"],
         "correct": 1,
         "expl": "Grounding the technical discussion in a devotional, "
                 "poetic source."},
        {"q": "What does Ānanda identify as &lsquo;confinement&rsquo;?",
         "opts": [
             "Physical illness",
             "The five kinds of sensual stimulation",
             "Monastic rules",
             "The nine attainments themselves"],
         "correct": 1,
         "expl": "The same five kāmaguṇā named as &lsquo;the "
                 "world&rsquo; at AN 9.38."},
        {"q": "How does this discourse describe the first eight "
              "attainments, unlike most of this chapter's other "
              "discourses?",
         "opts": [
             "As identical, with no distinguishing detail",
             "Each names the specific residual factor still counting as "
             "confinement there — unceased placing of the mind, rapture, "
             "and so on",
             "As entirely useless",
             "As already fully definitive"],
         "correct": 1,
         "expl": "Unique specific content per stage, unlike the bare "
                 "repeated formula found in most of the discourses that "
                 "follow."},
        {"q": "Which attainment alone offers the opening &lsquo;in a "
              "definitive sense&rsquo;?",
         "opts": [
             "The first absorption",
             "The fourth absorption",
             "The cessation of perception and feeling, the ninth "
             "attainment",
             "The dimension of nothingness"],
         "correct": 2,
         "expl": "The same ninth attainment singled out repeatedly "
                 "across this whole chapter."},
        {"q": "According to the guide, what does this discourse set up "
              "for the rest of the chapter?",
         "opts": [
             "Nothing; it stands alone",
             "The exact qualified-versus-definitive structural template "
             "that AN 9.43 through AN 9.51 all reuse with a different "
             "technical term",
             "A prohibition on discussing the formless attainments",
             "A contradiction of AN 9.32's list"],
         "correct": 1,
         "expl": "This chapter's own name, &ldquo;Similarity,&rdquo; "
                 "names this structural sameness directly."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same two speakers as AN 9.37, now with Udāyī "
                 "asking rather than challenging."},
    ],
    marginalia=[
        ("A godling's verse, quoted", [
            "&ldquo;the solitary boss bull&rdquo; &mdash;",
            "who found an opening",
            "amid confinement",
        ]),
        ("What confines at each stage", [
            "unceased thought, rapture,",
            "bliss, form, each dimension's",
            "own residual perception",
        ]),
        ("Qualified, then definitive", [
            "eight stages, partial;",
            "only the ninth, complete &mdash;",
            "this chapter's own template",
        ]),
        ("Cross-references", [
            "AN 9.37 &middot; the same &ldquo;opening amid "
            "confinement&rdquo; phrase, first introduced there",
            "AN 9.41 &middot; previous chapter's closing page",
            "AN 9.43 &middot; next, the same template applied to a new "
            "term",
        ]),
    ],
    further=[
        '<a href="%s/an9.42/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.41.html">AN 9.41 &middot; With the Householder Tapussa</a> &mdash; '
        "previous.",
        '<a href="an-9.43.html">AN 9.43 &middot; A Direct Witness</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.43 — Kāyasakkhīsutta
# --------------------------------------------------------------------------- #
page(
    43, "Kāyasakkhī", "A Direct Witness",
    vagga=VAGGA_5,
    meta_title="AN 9.43 — A Direct Witness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for A "
        "Direct Witness, applying AN 9.42's qualified-versus-definitive "
        "template to a new term — direct, personal experience of each "
        "attainment. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.42"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same qualified-versus-definitive template as AN "
                 "9.42, now with a single uniform formula at each stage"),
        ("Length", "~1 minute to read"),
        ("The template, now compressed", "Where AN 9.42 gave a distinct "
         "residual factor at each stage, this discourse applies one "
         "identical phrase to all nine attainments alike"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "once AN 9.42's structure is understood"),
    ],
    why=(
        "Udāyī asks what makes someone a &lsquo;direct witness,&rsquo; "
        "and Ānanda answers with the same nine-stage structure as AN "
        "9.42: a mendicant who directly experiences each attainment "
        "&lsquo;in every way&rsquo; is a direct witness in a qualified "
        "sense at each of the first eight stages, and in a definitive "
        "sense only at the ninth, the cessation of perception and "
        "feeling."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who meditates directly experiencing any of the "
            "nine progressive attainments &lsquo;in every way&rsquo; is "
            "called a direct witness in a qualified sense at each of the "
            "first eight stages, and in a definitive sense only upon "
            "reaching the cessation of perception and feeling."]),
        ("The same template, now uniform", [
            "Where AN 9.42 named a different specific residual factor "
            "at each of the eight qualified stages, this discourse uses "
            "the identical phrase &mdash; &lsquo;they meditate directly "
            "experiencing that dimension in every way&rsquo; &mdash; at "
            "every stage without variation, the compressed form this "
            "chapter's remaining discourses will mostly follow."]),
        ("Direct experience, not mere belief", [
            "&lsquo;Direct witness&rsquo; names a specific quality: "
            "personal, embodied experience of an attainment, not "
            "secondhand report or intellectual conviction. The term "
            "&lsquo;kāyasakkhī,&rsquo; literally &lsquo;body-"
            "witness,&rsquo; underscores that this experiential "
            "component is felt through the whole person, not reasoned "
            "out abstractly."]),
        ("Setting up a contrast with the next discourse", [
            "This discourse's single criterion &mdash; direct "
            "experience &mdash; sets up a deliberate contrast with AN "
            "9.44's criterion of wisdom-understanding, and both are then "
            "combined at AN 9.45's &lsquo;freed both ways,&rsquo; the "
            "traditional doctrinal category naming someone who has both "
            "qualities together."]),
    ],
    terms=[
        ("kāyasakkhī",
         "&ldquo;a direct witness&rdquo; &mdash; literally &ldquo;body-"
         "witness,&rdquo; this discourse's own title term for personal, "
         "embodied experience of an attainment."),
        ("kāyena phusitvā viharati",
         "&ldquo;meditate directly experiencing... in every way&rdquo; "
         "&mdash; the single uniform formula applied to all nine "
         "attainments in this discourse."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; the same term used "
         "at AN 9.42, marking each of the first eight stages as partial."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved, as "
         "always in this chapter, for the ninth attainment alone."),
        ("saññāvedayitanirodhaṁ upasampajja viharati, paññāya cassa "
         "disvā āsavā parikkhīṇā honti",
         "&ldquo;enters and remains in the cessation of perception and "
         "feeling... their defilements come to an end&rdquo; &mdash; "
         "the shared closing formula for the ninth stage, repeated "
         "throughout this chapter."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template as AN "
        "9.42, applied here to direct, personal experience. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A direct witness, at each of nine stages"),
        ("p", "&sect;1", "an9.43:1.1-2.3"),
        ("p", "&sect;2", "an9.43:3.1-4.3"),
        ("p", "&sect;3", "an9.43:5.1-5.3"),
    ],
    quiz=[
        {"q": "What term does this discourse define?",
         "opts": [
             "Confinement", "A direct witness (literally &ldquo;body-"
             "witness&rdquo;)",
             "Freedom by wisdom", "Extinguishment"],
         "correct": 1,
         "expl": "Personal, embodied experience of an attainment."},
        {"q": "How does this discourse's structure differ from AN "
              "9.42's?",
         "opts": [
             "It has only three stages instead of nine",
             "It uses one identical phrase at every stage, rather than a "
             "different residual factor named at each one",
             "It reverses the qualified-definitive order",
             "It contradicts AN 9.42 entirely"],
         "correct": 1,
         "expl": "The compressed, uniform version of the template AN "
                 "9.42 first set out with unique detail."},
        {"q": "What single criterion does this discourse apply to all "
              "nine attainments?",
         "opts": [
             "Understanding with wisdom",
             "Directly experiencing that dimension &lsquo;in every "
             "way&rsquo;",
             "Teaching it to others",
             "Physical strength"],
         "correct": 1,
         "expl": "Embodied, personal experience — not secondhand belief."},
        {"q": "According to the guide, what does this discourse set up "
              "for AN 9.44 and AN 9.45?",
         "opts": [
             "Nothing; they are unrelated",
             "A deliberate contrast with AN 9.44's wisdom-criterion, "
             "combined at AN 9.45 into the traditional &lsquo;freed both "
             "ways&rsquo; category",
             "A repetition with no new content",
             "A correction of an error in AN 9.42"],
         "correct": 1,
         "expl": "Direct experience and wisdom-understanding, paired "
                 "together at AN 9.45."},
        {"q": "At which stage alone does this discourse call someone a "
              "direct witness in the definitive sense?",
         "opts": [
             "The first absorption",
             "The dimension of nothingness",
             "The cessation of perception and feeling",
             "Every stage equally"],
         "correct": 2,
         "expl": "The ninth attainment, as throughout this chapter."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta and Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same speakers continuing from AN 9.42."},
    ],
    marginalia=[
        ("One phrase, nine stages", [
            "&ldquo;experiencing in",
            "every way&rdquo; &mdash; the same words",
            "repeated nine times",
        ]),
        ("Body-witness", [
            "kāyasakkhī &mdash;",
            "felt through the whole person,",
            "not reasoned abstractly",
        ]),
        ("Setting up a pairing", [
            "experience here; wisdom",
            "at AN 9.44 &mdash;",
            "combined at AN 9.45",
        ]),
        ("Cross-references", [
            "AN 9.42 &middot; previous, the template this discourse "
            "reuses in compressed form",
            "AN 9.44 &middot; next, Freed by Wisdom",
        ]),
    ],
    further=[
        '<a href="%s/an9.43/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.42.html">AN 9.42 &middot; Cramped</a> &mdash; previous, this '
        "chapter's own template.",
        '<a href="an-9.44.html">AN 9.44 &middot; Freed by Wisdom</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.44 — Paññāvimuttasutta
# --------------------------------------------------------------------------- #
page(
    44, "Paññāvimutta", "Freed by Wisdom",
    vagga=VAGGA_5,
    meta_title="AN 9.44 — Freed by Wisdom | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Freed by Wisdom, applying this chapter's shared template to "
        "understanding rather than direct experience — and quietly "
        "redefining a term that usually names a distinct category of "
        "practitioner. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.43"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same qualified-versus-definitive template, applied "
                 "here to understanding rather than experience"),
        ("Length", "~1 minute to read"),
        ("A term used differently here", "Elsewhere in the canon, "
         "&lsquo;freed by wisdom&rsquo; usually names a specific "
         "category of arahant; here it is redefined to apply, in a "
         "qualified sense, at every one of the nine stages"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, but worth noticing the terminological "
                       "shift"),
    ],
    why=(
        "Udāyī asks what makes someone &lsquo;freed by wisdom,&rsquo; "
        "and Ānanda answers with the same nine-stage structure again: a "
        "mendicant who understands each attainment with wisdom is freed "
        "by wisdom in a qualified sense at each of the first eight "
        "stages, and in a definitive sense only at the ninth."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who understands with wisdom whatever occurs in "
            "any of the nine progressive attainments is called freed by "
            "wisdom in a qualified sense at each of the first eight "
            "stages, and in a definitive sense only upon reaching the "
            "cessation of perception and feeling."]),
        ("The same template, a new criterion", [
            "Following directly on AN 9.43's pattern, this discourse "
            "swaps &lsquo;directly experiencing&rsquo; for "
            "&lsquo;understanding with wisdom&rsquo; as the single "
            "criterion applied uniformly across all nine stages, "
            "otherwise repeating the identical qualified-then-definitive "
            "structure."]),
        ("A familiar term, applied unusually", [
            "Elsewhere in the canon, &lsquo;paññāvimutta,&rsquo; freed "
            "by wisdom, typically names a specific category of arahant "
            "&mdash; one who has ended the defilements through insight "
            "without necessarily having mastered the formless "
            "attainments or direct witnessing. This discourse's usage is "
            "notably looser: it applies the phrase at every one of the "
            "nine stages, qualified or definitive, rather than reserving "
            "it for a single doctrinal category of person."]),
        ("Why this looseness matters for reading the chapter", [
            "This chapter's whole project is defining terms by running "
            "them through the same nine-stage grid, and readers "
            "expecting each term to retain its more familiar, narrower "
            "doctrinal sense from elsewhere in the canon should notice "
            "when, as here, the chapter's own usage is broader or "
            "different &mdash; a caution worth carrying into AN 9.45's "
            "combination of this discourse with AN 9.43's."]),
    ],
    terms=[
        ("paññāvimutto",
         "&ldquo;freed by wisdom&rdquo; &mdash; this discourse's own "
         "title term, elsewhere in the canon usually naming a distinct "
         "category of arahant."),
        ("paññāya ca naṁ pajānāti",
         "&ldquo;and they understand that with wisdom&rdquo; &mdash; "
         "the single criterion applied uniformly across all nine stages "
         "in this discourse."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; as at AN 9.42 and "
         "AN 9.43, marking each of the first eight stages as partial."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment alone, as throughout this chapter."),
        ("āsavā parikkhīṇā honti",
         "&ldquo;their defilements come to an end&rdquo; &mdash; the "
         "outcome marking the ninth and definitive stage, shared with "
         "every other discourse in this chapter."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template, applied "
        "here to understanding rather than direct experience. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Freed by wisdom, at each of nine stages"),
        ("p", "&sect;1", "an9.44:1.1-2.3"),
        ("p", "&sect;2", "an9.44:3.1-3.3"),
    ],
    quiz=[
        {"q": "What term does this discourse define?",
         "opts": [
             "A direct witness", "Freed by wisdom",
             "Confinement", "Full extinguishment"],
         "correct": 1,
         "expl": "Understanding with wisdom, applied across all nine "
                 "stages."},
        {"q": "What criterion replaces AN 9.43's &lsquo;directly "
              "experiencing&rsquo; in this discourse?",
         "opts": [
             "Physical strength",
             "Understanding with wisdom",
             "Teaching ability",
             "Length of monastic ordination"],
         "correct": 1,
         "expl": "The same nine-stage grid, a different single "
                 "criterion applied throughout."},
        {"q": "How does this discourse's usage of &lsquo;freed by "
              "wisdom&rsquo; differ from its more familiar sense "
              "elsewhere in the canon?",
         "opts": [
             "They are identical in every respect",
             "Elsewhere it usually names a specific category of "
             "arahant; here it applies more loosely, at every one of "
             "the nine stages",
             "This discourse never uses the term at all",
             "The canon elsewhere never uses this term"],
         "correct": 1,
         "expl": "A notable terminological broadening worth watching "
                 "for."},
        {"q": "According to the guide, what caution does this looser "
              "usage suggest for reading this chapter?",
         "opts": [
             "That the chapter is unreliable",
             "That readers should notice when a term's usage here is "
             "broader or different from its more familiar sense "
             "elsewhere in the canon",
             "That the term should be ignored entirely",
             "That translation itself is impossible"],
         "correct": 1,
         "expl": "A caution carried forward into AN 9.45's combination "
                 "of this discourse with AN 9.43's."},
        {"q": "At which stage alone is someone &lsquo;freed by "
              "wisdom&rsquo; in the definitive sense, according to this "
              "discourse?",
         "opts": [
             "The first absorption",
             "The dimension of infinite consciousness",
             "The cessation of perception and feeling",
             "All nine stages equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern across this whole "
                 "chapter."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same two speakers continuing through this "
                 "chapter."},
    ],
    marginalia=[
        ("A new criterion", [
            "not experience now,",
            "but understanding &mdash; the same",
            "nine stages, once more",
        ]),
        ("A term used loosely", [
            "elsewhere, one category;",
            "here, applied nine times over &mdash;",
            "watch the shift",
        ]),
        ("Toward a combination", [
            "experience, then wisdom &mdash;",
            "both together, next,",
            "at AN 9.45",
        ]),
        ("Cross-references", [
            "AN 9.43 &middot; previous, the same template applied to "
            "direct experience",
            "AN 9.45 &middot; next, combining both criteria",
        ]),
    ],
    further=[
        '<a href="%s/an9.44/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.43.html">AN 9.43 &middot; A Direct Witness</a> &mdash; previous.',
        '<a href="an-9.45.html">AN 9.45 &middot; Freed Both Ways</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.45 — Ubhatobhāgavimuttasutta
# --------------------------------------------------------------------------- #
page(
    45, "Ubhatobhāgavimutta", "Freed Both Ways",
    vagga=VAGGA_5,
    meta_title="AN 9.45 — Freed Both Ways | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Freed Both Ways, combining AN 9.43's direct experience with AN "
        "9.44's wisdom-understanding into the traditional doctrinal "
        "category naming both qualities together. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.44"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same template again, this time combining both of "
                 "the two previous discourses' criteria at every stage"),
        ("Length", "~1 minute to read"),
        ("A genuine combination, not just a third variant", "This "
         "discourse doesn't introduce a new criterion; it explicitly "
         "requires both AN 9.43's direct experience and AN 9.44's "
         "wisdom-understanding together"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief, and best read as the payoff of the "
                       "previous two discourses"),
    ],
    why=(
        "Udāyī asks what makes someone &lsquo;freed both ways,&rsquo; "
        "and Ānanda answers by combining the previous two discourses' "
        "criteria explicitly: a mendicant who both directly experiences "
        "an attainment and understands it with wisdom is freed both ways "
        "in a qualified sense at each of the first eight stages, and in "
        "a definitive sense only at the ninth."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who both meditates directly experiencing any "
            "of the nine attainments and understands it with wisdom is "
            "called freed both ways in a qualified sense at each of the "
            "first eight stages, and in a definitive sense only upon "
            "reaching the cessation of perception and feeling."]),
        ("A deliberate synthesis, not a third option", [
            "This discourse isn't a third independent variant sitting "
            "alongside AN 9.43 and AN 9.44; it names its own formula as "
            "the literal conjunction of both &mdash; direct experience "
            "and wisdom-understanding, together, at every one of the "
            "nine stages &mdash; making the three-discourse sequence "
            "read almost like a syllogism: criterion one, criterion two, "
            "both criteria combined."]),
        ("A category familiar from elsewhere in the canon", [
            "Unlike AN 9.44's somewhat looser use of &lsquo;freed by "
            "wisdom,&rsquo; &lsquo;ubhatobhāgavimutta&rsquo; is a well-"
            "established doctrinal category elsewhere in the canon, "
            "naming an arahant who has mastered both the formless "
            "attainments (or, in some accounts, all eight liberations) "
            "and full wisdom &mdash; here extended across all nine "
            "stages, qualified or definitive, following this chapter's "
            "consistent method."]),
        ("Three discourses, one deliberate progression", [
            "Read together, AN 9.43 through AN 9.45 form a small "
            "deliberate unit within this larger chapter: experience "
            "alone, wisdom alone, then both united &mdash; a "
            "progression this chapter's remaining discourses, defining "
            "further distinct terms, don't repeat again."]),
    ],
    terms=[
        ("ubhatobhāgavimutto",
         "&ldquo;freed both ways&rdquo; &mdash; this discourse's own "
         "title term, a well-established doctrinal category combining "
         "direct experience and wisdom."),
        ("kāyena ca phusitvā viharati, paññāya ca naṁ pajānāti",
         "&ldquo;they meditate directly experiencing... and they "
         "understand that with wisdom&rdquo; &mdash; the explicit "
         "combination of AN 9.43's and AN 9.44's separate criteria."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; as throughout this "
         "chapter, marking each of the first eight stages as partial."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment alone."),
        ("āsavā parikkhīṇā honti",
         "&ldquo;their defilements come to an end&rdquo; &mdash; the "
         "shared closing formula for the ninth and final stage."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template, combining "
        "AN 9.43's and AN 9.44's separate criteria. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Freed both ways, at each of nine stages"),
        ("p", "&sect;1", "an9.45:1.1-2.3"),
        ("p", "&sect;2", "an9.45:3.1-3.3"),
    ],
    quiz=[
        {"q": "What does this discourse's formula combine?",
         "opts": [
             "Two entirely new criteria not seen before",
             "AN 9.43's direct experience and AN 9.44's wisdom-"
             "understanding, together at every stage",
             "Only AN 9.42's confinement criterion, repeated",
             "Nothing; it introduces an unrelated new term"],
         "correct": 1,
         "expl": "A deliberate synthesis of the two preceding "
                 "discourses, not a third independent variant."},
        {"q": "How does &lsquo;ubhatobhāgavimutta&rsquo; compare to AN "
              "9.44's use of &lsquo;paññāvimutta&rsquo;?",
         "opts": [
             "Both are used equally loosely",
             "Unlike AN 9.44's looser usage, this term is a well-"
             "established doctrinal category elsewhere in the canon",
             "This term is never used elsewhere in the canon",
             "They are simply synonyms with no distinction"],
         "correct": 1,
         "expl": "A recognized category combining formless mastery and "
                 "wisdom, here extended across all nine stages."},
        {"q": "According to the guide, how do AN 9.43 through AN 9.45 "
              "read together?",
         "opts": [
             "As three unrelated, disconnected teachings",
             "Almost like a syllogism: criterion one, criterion two, "
             "both criteria combined",
             "As three contradictory definitions of the same term",
             "As a single discourse split into three pages by accident"],
         "correct": 1,
         "expl": "A small deliberate progression within the larger "
                 "chapter."},
        {"q": "At which stage alone is someone &lsquo;freed both "
              "ways&rsquo; in the definitive sense?",
         "opts": [
             "The first absorption",
             "The dimension of infinite space",
             "The cessation of perception and feeling",
             "Every stage equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern held throughout "
                 "this chapter."},
        {"q": "Does this chapter's remaining sequence of discourses "
              "repeat this three-part progression again?",
         "opts": [
             "Yes, exactly the same way for every remaining term",
             "No — the remaining discourses each define a further "
             "distinct term without repeating this specific three-part "
             "structure",
             "The chapter ends immediately after this discourse",
             "This is impossible to determine"],
         "correct": 1,
         "expl": "A unique small unit within the larger ten-discourse "
                 "chapter."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same two speakers continuing through this "
                 "chapter."},
    ],
    marginalia=[
        ("Two criteria, united", [
            "experience and wisdom &mdash;",
            "not either alone, but",
            "both together, at once",
        ]),
        ("A recognized category", [
            "unlike the looser term",
            "just before it &mdash; this one",
            "well-known elsewhere too",
        ]),
        ("A small progression, closed", [
            "one, then the other,",
            "then both combined &mdash; three",
            "discourses, one point",
        ]),
        ("Cross-references", [
            "AN 9.43, AN 9.44 &middot; the two separate criteria this "
            "discourse combines",
            "AN 9.46 &middot; next, In the Present Life",
        ]),
    ],
    further=[
        '<a href="%s/an9.45/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.44.html">AN 9.44 &middot; Freed by Wisdom</a> &mdash; previous.',
        '<a href="an-9.46.html">AN 9.46 &middot; In the Present Life</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.46 — Sandiṭṭhikadhammasutta
# --------------------------------------------------------------------------- #
page(
    46, "Sandiṭṭhikadhamma", "In the Present Life",
    vagga=VAGGA_5,
    meta_title="AN 9.46 — In the Present Life | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for In "
        "the Present Life, applying this chapter's shared template to a "
        "phrase usually reserved for the teaching as a whole — this time "
        "with no descriptive content added at any stage. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.45"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same template again, now at its most compressed: "
                 "no extra criterion or descriptive phrase at any stage"),
        ("Length", "~30 seconds to read"),
        ("The bare formula, stripped down further", "Where AN 9.43-45 "
         "each added a specific criterion, this discourse simply names "
         "each attainment itself as qualifiedly or definitively "
         "&lsquo;apparent in the present life&rsquo;"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the "
                       "briefest discourse in this chapter apart from "
                       "the fully elided stubs"),
    ],
    why=(
        "Udāyī asks in what way the Buddha spoke of &lsquo;a teaching "
        "apparent in the present life,&rsquo; and Ānanda answers with "
        "the bare nine-stage formula once more, this time with no "
        "further descriptive content: each of the first eight "
        "attainments is apparent in the present life in a qualified "
        "sense, and the ninth, definitively."),
    guide=[
        ("The teaching in one sentence", [
            "Reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;a teaching apparent in the "
            "present life&rsquo; &mdash; in a qualified sense at each of "
            "the first eight stages, and in a definitive sense only at "
            "the ninth, the cessation of perception and feeling."]),
        ("A familiar phrase, usually applied more broadly", [
            "&lsquo;Sandiṭṭhika,&rsquo; apparent or visible in the "
            "present life, is one of the standard qualities praising the "
            "Dhamma as a whole elsewhere in the canon &mdash; well "
            "explained, immediately effective, inviting inspection. Here "
            "it is applied narrowly to the nine meditative attainments "
            "specifically, in keeping with this whole chapter's project "
            "of running familiar terms through the same nine-stage grid."]),
        ("The template at its plainest", [
            "This discourse adds no descriptive content at any stage "
            "&mdash; no residual factor as at AN 9.42, no criterion of "
            "experience or wisdom as at AN 9.43 through AN 9.45. Simply "
            "reaching each attainment is what makes it &lsquo;apparent "
            "in the present life,&rsquo; qualifiedly or definitively, "
            "the plainest possible version of this chapter's shared "
            "structure."]),
        ("A bridge to the next discourse", [
            "This discourse's brevity sets up AN 9.47 directly: that "
            "next discourse simply adds &lsquo;extinguishment&rsquo; to "
            "this discourse's &lsquo;apparent in the present life,"
            "&rsquo; producing a compound term this chapter will "
            "continue exploring in variant forms through its remaining "
            "discourses."]),
    ],
    terms=[
        ("sandiṭṭhiko dhammo",
         "&ldquo;a teaching apparent in the present life&rdquo; &mdash; "
         "this discourse's own title phrase, elsewhere a standard "
         "quality praising the Dhamma as a whole."),
        ("ettāvatāpi kho... vuttaṁ bhagavatā pariyāyena",
         "&ldquo;to this extent the Buddha spoke of... in a qualified "
         "sense&rdquo; &mdash; the bare formula, repeated without added "
         "criteria at each of the first eight stages."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment, as throughout this chapter."),
        ("paṭhamaṁ jhānaṁ upasampajja viharati",
         "&ldquo;enters and remains in the first absorption&rdquo; "
         "&mdash; the opening stage, given here with no further "
         "descriptive addition."),
        ("saññāvedayitanirodhaṁ upasampajja viharati",
         "&ldquo;enters and remains in the cessation of perception and "
         "feeling&rdquo; &mdash; the ninth and definitive stage, closing "
         "this discourse's brief structure."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template at its "
        "plainest, with no descriptive content added at any stage. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Apparent in the present life, at each of nine stages"),
        ("p", "&sect;1", "an9.46:1.1-2.2"),
        ("p", "&sect;2", "an9.46:3.1-3.2"),
    ],
    quiz=[
        {"q": "What phrase does this discourse define?",
         "opts": [
             "Confinement",
             "A teaching apparent in the present life",
             "Freed both ways",
             "Full extinguishment"],
         "correct": 1,
         "expl": "Elsewhere in the canon, a standard quality praising "
                 "the Dhamma as a whole."},
        {"q": "How does this discourse's formula compare to AN 9.43 "
              "through AN 9.45?",
         "opts": [
             "It adds a new, more complex criterion",
             "It adds no descriptive content at any stage — the "
             "plainest possible version of this chapter's shared "
             "structure",
             "It contradicts the earlier discourses",
             "It has twice as many stages"],
         "correct": 1,
         "expl": "Simply reaching each attainment, with nothing further "
                 "specified."},
        {"q": "Where else in the canon does &lsquo;sandiṭṭhika&rsquo; "
              "commonly appear?",
         "opts": [
             "Nowhere else",
             "As one of the standard qualities praising the Dhamma as a "
             "whole",
             "Only in monastic disciplinary texts",
             "Only in cosmological discourses"],
         "correct": 1,
         "expl": "Applied here more narrowly, to the nine meditative "
                 "attainments specifically."},
        {"q": "According to the guide, what does this discourse set up "
              "for AN 9.47?",
         "opts": [
             "Nothing; they are unrelated",
             "AN 9.47 adds &lsquo;extinguishment&rsquo; to this "
             "discourse's &lsquo;apparent in the present life,&rsquo; "
             "forming a compound term",
             "AN 9.47 contradicts this discourse entirely",
             "AN 9.47 removes the nine-stage structure"],
         "correct": 1,
         "expl": "A compound term this chapter continues exploring in "
                 "variant forms."},
        {"q": "At which stage alone is a teaching apparent in the "
              "present life in a definitive sense?",
         "opts": [
             "The first absorption",
             "The dimension of nothingness",
             "The cessation of perception and feeling",
             "All nine stages equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern across this "
                 "chapter."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same two speakers continuing through this "
                 "chapter."},
    ],
    marginalia=[
        ("The template, plainest", [
            "no criterion added &mdash;",
            "just reaching each stage itself,",
            "qualified, then whole",
        ]),
        ("A familiar phrase, narrowed", [
            "elsewhere, the Dhamma",
            "as a whole; here, applied",
            "to nine stages alone",
        ]),
        ("A bridge ahead", [
            "&ldquo;apparent&rdquo; here;",
            "next, joined with extinguishment &mdash;",
            "a compound term begins",
        ]),
        ("Cross-references", [
            "AN 9.45 &middot; previous, Freed Both Ways",
            "AN 9.47 &middot; next, combining this term with "
            "extinguishment",
        ]),
    ],
    further=[
        '<a href="%s/an9.46/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.45.html">AN 9.45 &middot; Freed Both Ways</a> &mdash; previous.',
        '<a href="an-9.47.html">AN 9.47 &middot; Extinguishment Is Apparent in the Present '
        "Life</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.47 — Sandiṭṭhikanibbānasutta
# --------------------------------------------------------------------------- #
page(
    47, "Sandiṭṭhikanibbāna", "Extinguishment Is Apparent in the Present Life",
    vagga=VAGGA_5,
    meta_title=("AN 9.47 — Extinguishment Is Apparent in the Present Life | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Extinguishment Is Apparent in the Present Life, joining AN "
        "9.46's phrase to extinguishment itself and opening this "
        "chapter's run of four extinguishment-named discourses. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.46"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same bare template, now naming extinguishment "
                 "itself as what is qualifiedly or definitively apparent"),
        ("Length", "~30 seconds to read"),
        ("The first of four extinguishment-named discourses", "AN 9.47 "
         "through AN 9.51 each pair a different qualifier with "
         "&lsquo;extinguishment,&rsquo; and three of the four remaining "
         "ones are reduced in the source to a single elided line"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, the compound term worth noting for what "
                       "follows"),
    ],
    why=(
        "Udāyī asks in what way the Buddha said &lsquo;extinguishment is "
        "apparent in the present life,&rsquo; and Ānanda answers with "
        "the same bare nine-stage formula once more, joining AN 9.46's "
        "phrase directly to extinguishment itself &mdash; each of the "
        "first eight attainments qualifiedly, the ninth definitively."),
    guide=[
        ("The teaching in one sentence", [
            "Reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;extinguishment is apparent in "
            "the present life&rsquo; &mdash; in a qualified sense at "
            "each of the first eight stages, and in a definitive sense "
            "only at the ninth, the cessation of perception and "
            "feeling."]),
        ("A compound term, built from the previous discourse", [
            "This discourse doesn't introduce an unrelated new phrase; "
            "it takes AN 9.46's &lsquo;apparent in the present "
            "life&rsquo; and joins it directly to &lsquo;"
            "extinguishment,&rsquo; nibbāna, producing the compound term "
            "this title names &mdash; the same bare formula, now applied "
            "to the chapter's most central and weighty concept."]),
        ("Opening a run of four extinguishment-named discourses", [
            "This discourse opens a distinct sequence within the "
            "chapter: AN 9.47 through AN 9.51 all define some form of "
            "&lsquo;extinguishment,&rsquo; each with a different "
            "qualifier &mdash; apparent in the present life, bare "
            "extinguishment, full extinguishment, extinguishment in a "
            "certain respect, and extinguishment in this life."]),
        ("A run that becomes almost entirely elided", [
            "Of the four discourses following this one, three &mdash; "
            "AN 9.48, AN 9.49, and AN 9.50 &mdash; are reduced in the "
            "source to a single line each, no more than the opening "
            "question and an ellipsis, relying entirely on this "
            "discourse and its neighbors to supply the full nine-stage "
            "content by implication. Only the run's final discourse, AN "
            "9.51, is given in full again, closing not just this "
            "chapter but the entire First Fifty."]),
    ],
    terms=[
        ("sandiṭṭhikaṁ nibbānaṁ",
         "&ldquo;extinguishment is apparent in the present life&rdquo; "
         "&mdash; this discourse's own title compound, joining AN "
         "9.46's phrase to extinguishment itself."),
        ("ettāvatāpi kho... vuttaṁ bhagavatā pariyāyena",
         "&ldquo;to this extent the Buddha said... in a qualified "
         "sense&rdquo; &mdash; the bare formula, unchanged from AN "
         "9.46 apart from its new compound title term."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment, as throughout this chapter."),
        ("nibbānaṁ",
         "&ldquo;extinguishment&rdquo; &mdash; the term this discourse "
         "introduces into this chapter's compound titles, developed "
         "further across AN 9.48 through AN 9.51."),
        ("saññāvedayitanirodhaṁ upasampajja viharati, paññāya cassa "
         "disvā āsavā parikkhīṇā honti",
         "&ldquo;enters and remains in the cessation of perception and "
         "feeling... their defilements come to an end&rdquo; &mdash; "
         "the shared closing formula for the definitive ninth stage."),
    ],
    text_intro=(
        "The discourse in full: the same bare nine-stage template, now "
        "applied to extinguishment itself. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Extinguishment apparent in the present life"),
        ("p", "&sect;1", "an9.47:1.1-2.2"),
        ("p", "&sect;2", "an9.47:3.1-3.2"),
    ],
    quiz=[
        {"q": "What compound term does this discourse introduce?",
         "opts": [
             "Confinement and freedom",
             "Extinguishment is apparent in the present life, joining "
             "AN 9.46's phrase to extinguishment itself",
             "Freed both ways",
             "A direct witness"],
         "correct": 1,
         "expl": "The same bare formula from AN 9.46, now naming "
                 "extinguishment specifically."},
        {"q": "What sequence of discourses does this one open within "
              "the chapter?",
         "opts": [
             "A sequence about monastic discipline",
             "A run of four extinguishment-named discourses, AN 9.47 "
             "through AN 9.51, each with a different qualifier",
             "A sequence unrelated to the rest of the chapter",
             "The chapter's final two discourses only"],
         "correct": 1,
         "expl": "Apparent in the present life, bare extinguishment, "
                 "full extinguishment, in a certain respect, and in this "
                 "life."},
        {"q": "How are three of the four discourses following this one "
              "presented in the source?",
         "opts": [
             "In full detail, longer than this discourse",
             "Reduced to a single line each — just the opening question "
             "and an ellipsis",
             "Missing entirely, with no trace in the source",
             "Combined into one merged page"],
         "correct": 1,
         "expl": "AN 9.48, 9.49, and 9.50 rely on this discourse's "
                 "template to supply their full content by implication."},
        {"q": "Which discourse in this run is given in full again, and "
              "what does it close?",
         "opts": [
             "AN 9.48, closing nothing in particular",
             "AN 9.51, closing this chapter and the entire First Fifty",
             "AN 9.49, closing the whole nipāta",
             "This discourse itself closes the chapter"],
         "correct": 1,
         "expl": "The run's final discourse, given full treatment "
                 "again for this significant closing role."},
        {"q": "At which stage alone is extinguishment apparent in the "
              "present life in a definitive sense?",
         "opts": [
             "The first absorption",
             "The dimension of infinite consciousness",
             "The cessation of perception and feeling",
             "All nine stages equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern held throughout "
                 "this chapter."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same two speakers continuing through this "
                 "chapter."},
    ],
    marginalia=[
        ("A compound term begins", [
            "&ldquo;apparent&rdquo; joined now",
            "to extinguishment itself &mdash;",
            "a phrase built from two",
        ]),
        ("Four discourses, one theme", [
            "apparent, bare, full,",
            "a certain respect, this life &mdash;",
            "extinguishment, named four ways",
        ]),
        ("Toward near-total elision", [
            "three of the next four",
            "are a single line each &mdash;",
            "implied, not spelled out",
        ]),
        ("Cross-references", [
            "AN 9.46 &middot; previous, the phrase this discourse joins "
            "to extinguishment",
            "AN 9.48 &middot; next, Extinguishment",
        ]),
    ],
    further=[
        '<a href="%s/an9.47/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.46.html">AN 9.46 &middot; In the Present Life</a> &mdash; previous.',
        '<a href="an-9.48.html">AN 9.48 &middot; Extinguishment</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.48 — Nibbānasutta — the most minimal stub met anywhere in this
# project so far: one segment of English text, an ellipsis, and a bare
# ordinal number. The template it relies on is fully established at AN
# 9.42-47.
# --------------------------------------------------------------------------- #
page(
    48, "Nibbāna", "Extinguishment",
    vagga=VAGGA_5,
    meta_title="AN 9.48 — Extinguishment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Extinguishment, the "
        "most minimal discourse met anywhere in this project so far — a "
        "single line of English text, an ellipsis, and a bare ordinal "
        "number, relying entirely on AN 9.42-47's shared template. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.47"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis; nothing more "
                 "survives in the source"),
        ("Length", "A few seconds to read what exists"),
        ("The most minimal discourse in this project so far", "Where "
         "even the briefest earlier stubs kept a full first line, this "
         "one is reduced to the bare question and a source-side "
         "ellipsis, plus an ordinal number marking its place in the "
         "chapter"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, but worth understanding why it "
                       "is this short"),
    ],
    why=(
        "The source itself reduces this discourse to a single line "
        "&mdash; &lsquo;they speak of &ldquo;extinguishment&rdquo;&rsquo; "
        "&mdash; followed by an ellipsis and the bare marker "
        "&lsquo;seventh,&rsquo; relying entirely on the reader to supply "
        "the same nine-stage qualified-versus-definitive structure "
        "already given in full at AN 9.42 through AN 9.47."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at every discourse so far in "
            "this chapter, reaching any of the nine progressive "
            "attainments is what the Buddha meant by &lsquo;"
            "extinguishment&rsquo; &mdash; qualifiedly at each of the "
            "first eight stages, definitively only at the ninth &mdash; "
            "though the source itself no longer bothers to spell this "
            "out."]),
        ("A single line, and nothing more", [
            "Where AN 9.34's Meghiya narrative and AN 7.49's peyyāla "
            "each left only isolated stretches empty within an "
            "otherwise substantial discourse, this one is reduced in "
            "its entirety to one opening line, an ellipsis "
            "(&lsquo;&hellip;&rsquo;), and a bare ordinal &lsquo;"
            "seventh&rsquo; marking its numbered place among this "
            "chapter's ten discourses. Nothing else survives in the "
            "translated source."]),
        ("Reading by inference, not by content", [
            "This page's honest content is genuinely thin, and the "
            "guide does not fabricate what the source omits. What can "
            "be said with confidence comes entirely by inference from "
            "the five immediately preceding discourses, all sharing the "
            "identical structure: this discourse very likely ran "
            "through the same nine attainments, calling each of the "
            "first eight a qualified instance of &lsquo;"
            "extinguishment&rsquo; and the ninth a definitive one."]),
        ("Why the source compresses this far", [
            "By the sixth discourse in an unbroken run sharing one "
            "template, a reciter's tradition evidently judged further "
            "spelled-out repetition unnecessary &mdash; the ellipsis "
            "marks not a loss of content but a deliberate economy, "
            "trusting the listener to have already internalized the "
            "pattern from AN 9.42 through AN 9.47."]),
    ],
    terms=[
        ("nibbānaṁ",
         "&ldquo;extinguishment&rdquo; &mdash; this discourse's own "
         "title term and its only substantive word, standing in the "
         "source for the full nine-stage formula established earlier "
         "in this chapter."),
        ("…pe…",
         "the Pāli peyyāla marker itself, left untranslated here as an "
         "ellipsis &mdash; the source's own signal that the reciter "
         "should supply the omitted, already-familiar content."),
        ("sattamaṁ",
         "&ldquo;seventh&rdquo; &mdash; the bare ordinal closing this "
         "discourse, marking its numbered place among the chapter's ten "
         "discourses rather than offering any content of its own."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in this "
         "discourse's own surviving text, but supplied by inference from "
         "the identical structure at AN 9.42 through AN 9.47."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved throughout this chapter for the ninth "
         "attainment alone."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line, "
        "an ellipsis, and an ordinal number. Nothing has been added. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.48:1.1-1.1"),
    ],
    quiz=[
        {"q": "How much of this discourse survives in the translated "
              "source?",
         "opts": [
             "The full nine-stage formula, in complete detail",
             "A single opening line and an ellipsis — the most minimal "
             "discourse met anywhere in this project so far",
             "Only a title, with no text at all",
             "A shortened three-stage version"],
         "correct": 1,
         "expl": "Even briefer than earlier partial-ellipsis cases like "
                 "AN 9.3 or AN 7.49."},
        {"q": "What does the guide do about the missing content?",
         "opts": [
             "Fabricates the missing stages to fill out the page",
             "Honestly notes the omission and supplies what can be said "
             "by inference from the five immediately preceding "
             "discourses' shared structure",
             "Ignores the discourse entirely",
             "Claims the discourse has no meaningful content at all"],
         "correct": 1,
         "expl": "Consistent with this project's standing rule against "
                 "inventing text not in the source."},
        {"q": "According to the guide, why might the source compress "
              "this discourse so far?",
         "opts": [
             "A scribal accident with no explanation",
             "By the sixth discourse sharing one template, further "
             "spelled-out repetition was judged unnecessary — a "
             "deliberate economy, not a loss",
             "The discourse was considered unimportant",
             "It was added by a much later editor"],
         "correct": 1,
         "expl": "Trusting listeners to have internalized the pattern "
                 "from the discourses immediately before it."},
        {"q": "What term does this discourse's one surviving line "
              "define?",
         "opts": [
             "A direct witness",
             "Extinguishment",
             "Confinement",
             "Freed both ways"],
         "correct": 1,
         "expl": "The bare term this whole run of discourses, AN 9.47 "
                 "through AN 9.51, explores in variant forms."},
        {"q": "What does the bare ordinal &lsquo;seventh&rsquo; at the "
              "end of this discourse mark?",
         "opts": [
             "A count of the nine attainments",
             "This discourse's own numbered place among the chapter's "
             "ten discourses",
             "A monastic rank",
             "A count of the five precepts"],
         "correct": 1,
         "expl": "A structural marker, not substantive content."},
        {"q": "Which earlier discourse in this chapter supplies the "
              "full structure this one relies on?",
         "opts": [
             "AN 9.42 through AN 9.47",
             "AN 9.32 alone",
             "AN 9.11, unrelated to this chapter",
             "No earlier discourse is relevant"],
         "correct": 0,
         "expl": "The immediately preceding run of discourses, sharing "
                 "the identical qualified-versus-definitive template."},
    ],
    marginalia=[
        ("The most minimal page", [
            "one line, then &lsquo;&hellip;&rsquo;,",
            "then &lsquo;seventh&rsquo; &mdash; nothing more",
            "survives in the source",
        ]),
        ("No fabrication here", [
            "what can't be shown",
            "isn't invented &mdash; only",
            "named as missing",
        ]),
        ("A deliberate economy", [
            "six discourses deep",
            "in one template &mdash; the reciter",
            "trusts it's understood",
        ]),
        ("Cross-references", [
            "AN 9.42&ndash;47 &middot; the full template this stub "
            "relies on by inference",
            "AN 9.47 &middot; previous",
            "AN 9.49 &middot; next, Full Extinguishment",
        ]),
    ],
    further=[
        '<a href="%s/an9.48/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.47.html">AN 9.47 &middot; Extinguishment Is Apparent in the Present '
        "Life</a> &mdash; previous.",
        '<a href="an-9.49.html">AN 9.49 &middot; Full Extinguishment</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.49 — Parinibbānasutta — equally minimal
# --------------------------------------------------------------------------- #
page(
    49, "Parinibbāna", "Full Extinguishment",
    vagga=VAGGA_5,
    meta_title="AN 9.49 — Full Extinguishment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Full Extinguishment, "
        "equally minimal in the source as AN 9.48 — one line, an "
        "ellipsis, and an ordinal — this time naming the intensified "
        "form of extinguishment reserved for an arahant's death. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.48"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching AN "
                 "9.48's minimal survival exactly"),
        ("Length", "A few seconds to read what exists"),
        ("A distinct term, equally minimal treatment", "&lsquo;"
         "Parinibbāna&rsquo; usually names the final passing of an "
         "arahant, distinct from bare &lsquo;nibbāna&rsquo; — but the "
         "source treats this discourse exactly as tersely as AN 9.48"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, more interesting for the term "
                       "it names than for its own text"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;full extinguishment&rdquo;&rsquo; "
        "&mdash; followed by an ellipsis and the marker &lsquo;"
        "eighth,&rsquo; applying the same qualified-versus-definitive "
        "template established at AN 9.42 through AN 9.47 to a term that "
        "elsewhere in the canon usually names an arahant's final "
        "passing away, not merely the ending of defilements during "
        "life."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established throughout this chapter, "
            "reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;full extinguishment&rsquo; "
            "&mdash; qualifiedly at each of the first eight stages, "
            "definitively only at the ninth &mdash; though, as at AN "
            "9.48, the source no longer spells this out."]),
        ("A term that usually means something more final", [
            "Elsewhere in the canon, &lsquo;parinibbāna,&rsquo; full "
            "extinguishment, typically names an arahant's final passing "
            "away at death &mdash; the complete cessation of the five "
            "aggregates, distinct from the extinguishment of "
            "defilements an arahant already experiences while still "
            "alive. This chapter's series applies the term instead to "
            "the same nine meditative attainments as every other term "
            "here, a usage worth noticing as distinct from the more "
            "familiar sense."]),
        ("Equally minimal, despite the distinct meaning", [
            "Despite &lsquo;parinibbāna&rsquo; carrying a more specific "
            "and consequential meaning elsewhere, the source treats this "
            "discourse exactly as tersely as AN 9.48's bare "
            "&lsquo;nibbāna&rsquo; &mdash; one line, an ellipsis, and "
            "the ordinal &lsquo;eighth.&rsquo; The economy applies "
            "uniformly, regardless of how weighty the individual term "
            "might be."]),
        ("A run continuing toward its close", [
            "This is the second of three consecutive discourses reduced "
            "to a single line in this way; AN 9.50 follows identically, "
            "before AN 9.51 restores full treatment to close both this "
            "chapter and the entire First Fifty."]),
    ],
    terms=[
        ("parinibbānaṁ",
         "&ldquo;full extinguishment&rdquo; &mdash; elsewhere in the "
         "canon usually naming an arahant's final passing away at "
         "death, applied here to the nine meditative attainments like "
         "every other term in this chapter."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted, "
         "already-familiar content."),
        ("aṭṭhamaṁ",
         "&ldquo;eighth&rdquo; &mdash; the bare ordinal closing this "
         "discourse, marking its place among the chapter's ten "
         "discourses."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in this "
         "discourse's own text, supplied by inference from the pattern "
         "at AN 9.42 through AN 9.47."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this chapter."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line, "
        "an ellipsis, and an ordinal number. Nothing has been added. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.49:1.1-1.1"),
    ],
    quiz=[
        {"q": "What does &lsquo;parinibbāna&rsquo; usually name "
              "elsewhere in the canon?",
         "opts": [
             "A monastic ordination ceremony",
             "An arahant's final passing away at death, distinct from "
             "the ending of defilements during life",
             "A type of meditation posture",
             "A specific monastery"],
         "correct": 1,
         "expl": "A more final and specific meaning than bare "
                 "&lsquo;nibbāna&rsquo;."},
        {"q": "How does this discourse apply the term instead?",
         "opts": [
             "In its usual, more specific sense about death",
             "To the same nine meditative attainments as every other "
             "term in this chapter, by the shared qualified-versus-"
             "definitive template",
             "It doesn't use the term at all",
             "Only to describe the Buddha's own death"],
         "correct": 1,
         "expl": "This chapter's consistent method, applied here to a "
                 "usually more consequential term."},
        {"q": "How does the source's treatment of this discourse "
              "compare to AN 9.48's?",
         "opts": [
             "Much longer, given the term's weightier meaning",
             "Exactly as terse — one line, an ellipsis, and an ordinal, "
             "regardless of how consequential the individual term is",
             "Completely different in structure",
             "Missing from the source entirely"],
         "correct": 1,
         "expl": "The same minimal economy applied uniformly across "
                 "this stretch of the chapter."},
        {"q": "What is this discourse's place within the chapter's "
              "closing run?",
         "opts": [
             "The first of the fully elided stubs",
             "The second of three consecutive single-line discourses, "
             "before AN 9.51 restores full treatment",
             "The final discourse in the chapter",
             "Unrelated to the surrounding discourses"],
         "correct": 1,
         "expl": "AN 9.48 and AN 9.50 share this same minimal form; AN "
                 "9.51 closes the chapter and the First Fifty in full."},
        {"q": "What ordinal number marks this discourse's place?",
         "opts": [
             "Seventh", "Eighth", "Ninth", "Tenth"],
         "correct": 1,
         "expl": "Following AN 9.48's &lsquo;seventh&rsquo; in sequence."},
        {"q": "Where does the qualified-versus-definitive content this "
              "discourse implies come from?",
         "opts": [
             "Nowhere; it must be invented",
             "By inference from AN 9.42 through AN 9.47's shared, fully "
             "spelled-out template",
             "From a completely unrelated discourse",
             "It cannot be inferred at all"],
         "correct": 1,
         "expl": "The same source of inference used for AN 9.48."},
    ],
    marginalia=[
        ("A weightier term, elsewhere", [
            "parinibbāna usually",
            "means an arahant's death &mdash;",
            "not so, applied here",
        ]),
        ("Equally minimal", [
            "one line, &lsquo;&hellip;&rsquo;, &lsquo;eighth&rsquo; &mdash;",
            "the same economy",
            "regardless of weight",
        ]),
        ("Second of three, in a row", [
            "9.48, this, then",
            "9.50 the same way &mdash;",
            "before 9.51 restores",
        ]),
        ("Cross-references", [
            "AN 9.42&ndash;47 &middot; the full template this stub "
            "relies on by inference",
            "AN 9.48 &middot; previous",
            "AN 9.50 &middot; next, Extinguishment in a Certain Respect",
        ]),
    ],
    further=[
        '<a href="%s/an9.49/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.48.html">AN 9.48 &middot; Extinguishment</a> &mdash; previous.',
        '<a href="an-9.50.html">AN 9.50 &middot; Extinguishment in a Certain Respect</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.50 — Tadaṅganibbānasutta — equally minimal, third in the run
# --------------------------------------------------------------------------- #
page(
    50, "Tadaṅganibbāna", "Extinguishment in a Certain Respect",
    vagga=VAGGA_5,
    meta_title=("AN 9.50 — Extinguishment in a Certain Respect | "
                "Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide and self-check quiz for Extinguishment in a "
        "Certain Respect, the third and final minimal stub in this "
        "chapter's run, naming a technical category of temporary, "
        "partial extinguishment distinct from the complete kind. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.49"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, the third and "
                 "final discourse in this chapter reduced this far"),
        ("Length", "A few seconds to read what exists"),
        ("A genuinely technical distinction, minimally treated", "&lsquo;"
         "Tadaṅga-nibbāna&rsquo; names a real doctrinal category — "
         "temporary suppression of a specific defilement by its direct "
         "opposite — distinct from full and final extinguishment"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the "
                       "term itself carries more doctrinal weight than "
                       "its minimal treatment here suggests"),
    ],
    why=(
        "The source reduces this discourse, like AN 9.48 and AN 9.49 "
        "before it, to a single line &mdash; &lsquo;they speak of "
        "&ldquo;extinguishment in a certain respect&rdquo;&rsquo; "
        "&mdash; followed by an ellipsis and the marker &lsquo;"
        "ninth,&rsquo; applying the chapter's shared template to a term "
        "that elsewhere names a genuine technical category: the "
        "temporary suppression of one specific defilement by its "
        "direct opposite, short of complete and final extinguishment."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established throughout this chapter, "
            "reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;extinguishment in a certain "
            "respect&rsquo; &mdash; qualifiedly at each of the first "
            "eight stages, definitively only at the ninth &mdash; though "
            "the source, as at AN 9.48 and AN 9.49, no longer spells "
            "this out."]),
        ("A genuine technical category, named briefly", [
            "&lsquo;Tadaṅga-nibbāna,&rsquo; literally &lsquo;"
            "extinguishment by that factor,&rsquo; names a real "
            "doctrinal distinction found elsewhere in the tradition: the "
            "temporary suppression of one specific defilement by "
            "cultivating its direct opposite &mdash; hate suppressed by "
            "love, for instance &mdash; a genuine but partial and "
            "reversible achievement, distinct from full, final "
            "extinguishment."]),
        ("The third and last of this run's fully elided stubs", [
            "This is the third and final discourse in this chapter "
            "reduced to a single surviving line, closing out the run "
            "begun at AN 9.48. Where those two discourses named bare "
            "extinguishment and full extinguishment respectively, this "
            "one names the most technically specific of the three "
            "&mdash; and receives exactly the same minimal treatment "
            "regardless."]),
        ("What comes next restores the full picture", [
            "AN 9.51, immediately following, breaks this pattern of "
            "minimal treatment: it is given in full again, one final "
            "time, and closes not only this chapter but the entire "
            "First Fifty of the Book of the Nines &mdash; the run of "
            "compression this discourse belongs to giving way, at the "
            "chapter's very close, to full and deliberate elaboration "
            "once more."]),
    ],
    terms=[
        ("tadaṅganibbānaṁ",
         "&ldquo;extinguishment in a certain respect,&rdquo; literally "
         "&ldquo;extinguishment by that factor&rdquo; &mdash; a genuine "
         "technical category elsewhere naming temporary suppression of "
         "one defilement by its direct opposite."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("navamaṁ",
         "&ldquo;ninth&rdquo; &mdash; the bare ordinal closing this "
         "discourse, marking its place among the chapter's ten "
         "discourses (not to be confused with the ninth meditative "
         "attainment)."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in this "
         "discourse's own text, supplied by inference from AN 9.42 "
         "through AN 9.47's shared pattern."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this chapter."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line, "
        "an ellipsis, and an ordinal number. Nothing has been added. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.50:1.1-1.1"),
    ],
    quiz=[
        {"q": "What does &lsquo;tadaṅga-nibbāna&rsquo; name as a "
              "genuine technical category?",
         "opts": [
             "A monastic disciplinary offense",
             "The temporary suppression of one specific defilement by "
             "cultivating its direct opposite, short of complete "
             "extinguishment",
             "A type of meditation cushion",
             "A formal ordination procedure"],
         "correct": 1,
         "expl": "A real but partial and reversible achievement, "
                 "distinct from full and final extinguishment."},
        {"q": "How does this discourse's source-text treatment compare "
              "to AN 9.48 and AN 9.49's?",
         "opts": [
             "Much fuller, given its technical significance",
             "The same minimal treatment — one line, an ellipsis, and an "
             "ordinal, despite naming the most technically specific of "
             "the three terms",
             "Completely absent from the source",
             "Doubled in length"],
         "correct": 1,
         "expl": "The uniform economy applied across this whole "
                 "three-discourse run."},
        {"q": "What is this discourse's position within the chapter's "
              "run of minimal stubs?",
         "opts": [
             "The first of the run",
             "The third and final discourse in this chapter reduced to "
             "a single surviving line",
             "The only one of its kind in the chapter",
             "It falls outside the run entirely"],
         "correct": 1,
         "expl": "Closing out the run begun at AN 9.48 and continued at "
                 "AN 9.49."},
        {"q": "What happens immediately after this discourse, at AN "
              "9.51?",
         "opts": [
             "Another single-line stub, continuing the pattern",
             "Full treatment is restored, closing both this chapter and "
             "the entire First Fifty",
             "The chapter ends without further discourses",
             "The numbering restarts from AN 9.1"],
         "correct": 1,
         "expl": "The compression gives way to full elaboration at the "
                 "chapter's very close."},
        {"q": "What ordinal number marks this discourse's place?",
         "opts": [
             "Seventh", "Eighth", "Ninth", "Tenth"],
         "correct": 2,
         "expl": "Following AN 9.48's &lsquo;seventh&rsquo; and AN "
                 "9.49's &lsquo;eighth&rsquo; in sequence."},
        {"q": "Where does the qualified-versus-definitive content this "
              "discourse implies come from?",
         "opts": [
             "Nowhere; it must be invented",
             "By inference from AN 9.42 through AN 9.47's shared, fully "
             "spelled-out template",
             "From a completely unrelated discourse",
             "It cannot be inferred at all"],
         "correct": 1,
         "expl": "The same source of inference used for AN 9.48 and AN "
                 "9.49."},
    ],
    marginalia=[
        ("A technical term, briefly named", [
            "one defilement stilled",
            "by its own opposite &mdash;",
            "partial, not complete",
        ]),
        ("Third of three, minimal", [
            "one line, &lsquo;&hellip;&rsquo;, &lsquo;ninth&rsquo; &mdash;",
            "the same economy,",
            "closing out the run",
        ]),
        ("Full treatment restored next", [
            "compression gives way",
            "at the chapter's very close &mdash;",
            "see AN 9.51",
        ]),
        ("Cross-references", [
            "AN 9.42&ndash;47 &middot; the full template this stub "
            "relies on by inference",
            "AN 9.49 &middot; previous",
            "AN 9.51 &middot; next, closing this chapter and the entire "
            "First Fifty",
        ]),
    ],
    further=[
        '<a href="%s/an9.50/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.49.html">AN 9.49 &middot; Full Extinguishment</a> &mdash; previous.',
        '<a href="an-9.51.html">AN 9.51 &middot; Extinguishment in This Life</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.51 — Diṭṭhadhammanibbānasutta — closes ch.5 Sāmaññavagga AND the
# entire Paṭhamapaṇṇāsaka (First Fifty, AN 9.1-51).
# --------------------------------------------------------------------------- #
page(
    51, "Diṭṭhadhammanibbāna", "Extinguishment in This Life",
    vagga=VAGGA_5,
    meta_title="AN 9.51 — Extinguishment in This Life | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Extinguishment in This Life, restoring full treatment to close "
        "this chapter's run of near-identical discourses — and, with it, "
        "the entire First Fifty of the Book of the Nines. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.50"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same nine-stage template given in full one final "
                 "time, closing with an untranslated double colophon"),
        ("Length", "~1 minute to read"),
        ("Closing the chapter, and the First Fifty itself", "This "
         "discourse closes <em>Sāmaññavagga</em>, the fifth chapter, "
         "and, with it, the entire Paṭhamapaṇṇāsaka &mdash; the First "
         "Fifty of the Book of the Nines"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief in itself, but weighty for what it "
                       "closes"),
    ],
    why=(
        "Closing a run that grew progressively more compressed through "
        "AN 9.48, AN 9.49, and AN 9.50, this discourse restores full "
        "treatment one final time: a mendicant reaching any of the nine "
        "attainments has extinguishment in this life in a qualified "
        "sense, and only at the ninth, the cessation of perception and "
        "feeling, in a definitive sense &mdash; closing not only this "
        "chapter but the entire First Fifty of the Book of the Nines."),
    guide=[
        ("The teaching in one sentence", [
            "Reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;extinguishment in this "
            "life&rsquo; &mdash; in a qualified sense at each of the "
            "first eight stages, and in a definitive sense only upon "
            "reaching the cessation of perception and feeling, the same "
            "structure that has run through this entire chapter."]),
        ("Full treatment restored, after three minimal stubs", [
            "After AN 9.48, AN 9.49, and AN 9.50 each survived as no "
            "more than a single elided line, this discourse breaks the "
            "pattern of compression and is given full treatment once "
            "more &mdash; a deliberate choice by the tradition to close "
            "both the run and the chapter with complete elaboration "
            "rather than a fourth bare stub."]),
        ("A tenth term, closing a chapter about sameness", [
            "This is the tenth and final term this chapter's "
            "<em>Sāmaññavagga</em>, &ldquo;Chapter on Similarity,&rdquo; "
            "defines through its shared template: confinement, direct "
            "witnessing, freedom by wisdom, freedom both ways, apparent "
            "in the present life, and four variations on "
            "&lsquo;extinguishment&rsquo; &mdash; ten near-synonymous "
            "framings of the same underlying nine-stage progression, "
            "each illuminating it from a slightly different angle."]),
        ("Two colophons, closing two things at once", [
            "The source's own untranslated closing lines mark a double "
            "closure: first &lsquo;Sāmaññavaggo pañcamo&rsquo; "
            "(&ldquo;the fifth chapter, Sāmaññavagga, is finished&rdquo;), "
            "then, immediately after, &lsquo;paṭhamo paṇṇāsako "
            "samatto&rsquo; (&ldquo;the First Fifty is completed&rdquo;) "
            "&mdash; the same double-closing pattern met at the end of "
            "earlier nipātas' first-fifty sections, here marking the "
            "halfway point of the Book of the Nines itself, with the "
            "Second Fifty still ahead."]),
    ],
    terms=[
        ("diṭṭhadhammanibbānaṁ",
         "&ldquo;extinguishment in this life&rdquo; &mdash; this "
         "discourse's own title compound, closing the run of "
         "extinguishment-named discourses begun at AN 9.47."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; the shared term for "
         "each of the first eight attainments, running through this "
         "entire chapter."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment alone, as at every discourse in this chapter."),
        ("sāmaññavaggo pañcamo",
         "&ldquo;the fifth chapter, Sāmaññavagga, is finished&rdquo; "
         "&mdash; the source's own untranslated colophon closing this "
         "chapter."),
        ("paṭhamo paṇṇāsako samatto",
         "&ldquo;the First Fifty is completed&rdquo; &mdash; the "
         "source's own second untranslated colophon, marking the "
         "halfway point of the entire Book of the Nines."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template, given in "
        "complete detail one final time to close this chapter. The "
        "source's own double closing colophon is untranslated in the "
        "English and is described rather than quoted here. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Extinguishment in this life, at each of nine stages"),
        ("p", "&sect;1", "an9.51:1.1-2.2"),
        ("p", "&sect;2", "an9.51:3.1-3.2"),
    ],
    quiz=[
        {"q": "What term does this discourse define, closing the run "
              "begun at AN 9.47?",
         "opts": [
             "Confinement",
             "Extinguishment in this life",
             "A direct witness",
             "Freed both ways"],
         "correct": 1,
         "expl": "The final and fourth extinguishment-named term in "
                 "this chapter's closing sequence."},
        {"q": "How does this discourse's treatment compare to AN 9.48 "
              "through AN 9.50's?",
         "opts": [
             "Equally minimal, one line and an ellipsis",
             "Full treatment is restored, breaking the pattern of "
             "increasing compression",
             "Even more compressed than the three stubs before it",
             "Missing from the source entirely"],
         "correct": 1,
         "expl": "A deliberate choice to close both the run and the "
                 "chapter with complete elaboration."},
        {"q": "How many distinct terms does this chapter's shared "
              "template define in total, including this one?",
         "opts": [
             "Five", "Seven",
             "Ten", "Twelve"],
         "correct": 2,
         "expl": "Ten near-synonymous framings of the same underlying "
                 "nine-stage progression, one per discourse."},
        {"q": "What double closure does this discourse's untranslated "
              "colophon mark?",
         "opts": [
             "Only the end of this single discourse",
             "The end of <em>Sāmaññavagga</em>, the fifth chapter, and "
             "the end of the entire First Fifty of the Book of the "
             "Nines",
             "The end of the whole Book of the Nines",
             "The end of the Aṅguttara Nikāya itself"],
         "correct": 1,
         "expl": "Two separate closing lines, marking the chapter's end "
                 "and the halfway point of AN 9 together."},
        {"q": "What remains ahead after this discourse, according to "
              "the guide?",
         "opts": [
             "Nothing; the nipāta is complete",
             "The Second Fifty of the Book of the Nines",
             "A return to the First Fifty's opening chapter",
             "A separate, unrelated nipāta"],
         "correct": 1,
         "expl": "The halfway point of AN 9, not its end."},
        {"q": "At which stage alone is extinguishment in this life "
              "achieved in a definitive sense?",
         "opts": [
             "The first absorption",
             "The dimension of infinite consciousness",
             "The cessation of perception and feeling",
             "All nine stages equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern held throughout "
                 "this entire chapter."},
    ],
    marginalia=[
        ("Full treatment, restored", [
            "after three bare stubs,",
            "spelled out once more &mdash;",
            "a deliberate close",
        ]),
        ("Ten terms, one structure", [
            "confinement, witness,",
            "wisdom, both ways, apparent,",
            "extinguishment fourfold",
        ]),
        ("Two colophons at once", [
            "Sāmaññavaggo,",
            "then paṭhamo paṇṇāsako &mdash;",
            "chapter and half-book, closed",
        ]),
        ("Cross-references", [
            "AN 9.42&ndash;50 &middot; the nine earlier terms this "
            "discourse's tenth joins",
            "AN 9.50 &middot; previous",
            "AN 9.52 &middot; next, opening the Second Fifty",
        ]),
    ],
    further=[
        '<a href="%s/an9.51/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.50.html">AN 9.50 &middot; Extinguishment in a Certain Respect</a> '
        "&mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# ch.6 — Khemavagga (AN 9.52-62), opening the Second Fifty. This chapter
# continues ch.5's Udāyī-to-Ānanda template for its first ten discourses,
# defining five paired safety-related terms (bare and "reaching" forms) via
# the same nine-stage qualified-versus-definitive structure. Eight of these
# ten (AN 9.53-60) are reduced in the source to a single elided line each,
# the longest such run met anywhere in this project so far. AN 9.62 closes
# the chapter with an unrelated nine-defilement teaching.
# --------------------------------------------------------------------------- #
VAGGA_6 = "<em>Khemavagga</em> &mdash; the sixth chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.52 — Khemasutta — this chapter's own namesake
# --------------------------------------------------------------------------- #
page(
    52, "Khema", "A Safe Place",
    vagga=VAGGA_6,
    meta_title="AN 9.52 — A Safe Place | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for A "
        "Safe Place, this chapter's own namesake, opening a new run of "
        "the Udāyī-to-Ānanda template — nine safety-related terms "
        "structured through the same nine attainments. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from the "
                    "chapter's opening"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The same qualified-versus-definitive template met "
                 "throughout ch.5, opening a new ten-discourse run"),
        ("Length", "~1 minute to read"),
        ("Chapter's namesake, opening a new run of five paired terms",
         "This discourse names the chapter and opens five pairs of "
         "terms — safe/reaching safety, deathless/reaching it, "
         "fearless/reaching it, tranquility/progressive, cessation/"
         "progressive"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, opening a chapter that continues ch.5's "
                       "method almost without a break"),
    ],
    why=(
        "Udāyī asks in what way the Buddha spoke of &lsquo;a safe "
        "place,&rsquo; and Ānanda answers with the now-familiar nine-"
        "stage formula: each of the first eight attainments offers a "
        "safe place in a qualified sense, and only the ninth, the "
        "cessation of perception and feeling, in a definitive sense."),
    guide=[
        ("The teaching in one sentence", [
            "Reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;a safe place&rsquo; &mdash; in "
            "a qualified sense at each of the first eight stages, and "
            "in a definitive sense only upon reaching the cessation of "
            "perception and feeling."]),
        ("Continuing ch.5's method without a break", [
            "This discourse opens a new chapter, but not a new method: "
            "the identical Udāyī-to-Ānanda question-and-answer "
            "structure, the identical nine-stage grid, and the "
            "identical qualified-versus-definitive language carry "
            "straight over from <em>Sāmaññavagga</em>, now applied to a "
            "fresh cluster of terms grouped around safety."]),
        ("A chapter's namesake, and a new run of five pairs", [
            "This discourse's own term, khema, &ldquo;a safe place,"
            "&rdquo; names <em>Khemavagga</em> itself. It also opens a "
            "structured run of five term-pairs that will occupy this "
            "chapter's first ten discourses: safety and reaching "
            "safety, freedom from death and reaching it, freedom from "
            "fear and reaching it, tranquility and progressive "
            "tranquility, and cessation and progressive cessation."]),
        ("What follows: the longest run of minimal stubs so far", [
            "Of the nine discourses following this one, eight (AN 9.53 "
            "through AN 9.60) are reduced in the source to a single "
            "elided line each &mdash; the longest such run met anywhere "
            "in this project, surpassing even the three-discourse run "
            "at AN 9.48 through AN 9.50. Only AN 9.61, closing the run, "
            "is given full treatment again."]),
    ],
    terms=[
        ("khemaṁ",
         "&ldquo;a safe place&rdquo; &mdash; this discourse's own title "
         "term, naming the chapter and opening this run of five paired "
         "safety-related terms."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; the shared term "
         "for each of the first eight attainments, carried over "
         "directly from ch.5's method."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment alone, as throughout this whole stretch of "
         "the nipāta."),
        ("khemappatta",
         "&ldquo;reaching a safe place&rdquo; &mdash; the paired term "
         "explored next, at AN 9.53, the first of this chapter's "
         "minimal stubs."),
        ("saññāvedayitanirodhaṁ upasampajja viharati, paññāya cassa "
         "disvā āsavā parikkhīṇā honti",
         "&ldquo;enters and remains in the cessation of perception and "
         "feeling... their defilements come to an end&rdquo; &mdash; "
         "the shared closing formula for the definitive ninth stage."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template as "
        "ch.5, now applied to safety. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A safe place, at each of nine stages"),
        ("p", "&sect;1", "an9.52:1.1-2.2"),
        ("p", "&sect;2", "an9.52:3.1-3.2"),
    ],
    quiz=[
        {"q": "What term does this discourse define, and what chapter "
              "does it name?",
         "opts": [
             "Confinement, naming Sāmaññavagga",
             "A safe place (khema), naming this chapter, "
             "Khemavagga",
             "Cessation, naming no chapter",
             "Freedom from death, naming ch.7"],
         "correct": 1,
         "expl": "This chapter's own namesake, opening a fresh run of "
                 "paired terms."},
        {"q": "How does this discourse's method compare to ch.5's?",
         "opts": [
             "Entirely different, with a new speaker and structure",
             "Identical — the same Udāyī-to-Ānanda dialogue and nine-"
             "stage qualified-versus-definitive grid, applied to new "
             "terms",
             "Reversed, with Ānanda now asking Udāyī",
             "Shortened to only three stages"],
         "correct": 1,
         "expl": "A direct continuation of the method established "
                 "across ch.5."},
        {"q": "What five term-pairs does this discourse open a run of?",
         "opts": [
             "Five unrelated topics",
             "Safety/reaching safety, deathlessness/reaching it, "
             "fearlessness/reaching it, tranquility/progressive, "
             "cessation/progressive",
             "The five aggregates and their opposites",
             "Five monastic precepts"],
         "correct": 1,
         "expl": "A structured cluster of paired safety-related terms "
                 "occupying this chapter's first ten discourses."},
        {"q": "How many of the nine discourses following this one are "
              "reduced to a single elided line in the source?",
         "opts": [
             "None; all are given full treatment",
             "Eight — AN 9.53 through AN 9.60, the longest such run met "
             "anywhere in this project",
             "Only two",
             "All nine, with no exceptions"],
         "correct": 1,
         "expl": "Surpassing even the three-discourse run at AN 9.48 "
                 "through AN 9.50."},
        {"q": "Which discourse closes this run with full treatment "
              "restored?",
         "opts": [
             "AN 9.60", "AN 9.61", "AN 9.62", "AN 9.53"],
         "correct": 1,
         "expl": "Progressive cessation, given in full to close the "
                 "run, matching this chapter's opener."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same speakers carried over directly from ch.5."},
    ],
    marginalia=[
        ("A chapter's own name", [
            "khema, a safe place &mdash;",
            "naming Khemavagga,",
            "opening five pairs",
        ]),
        ("Continuing without a break", [
            "the same question, the",
            "same nine stages &mdash; ch.5's",
            "method, carried forward",
        ]),
        ("A long run of stubs ahead", [
            "eight discourses next,",
            "each just a single line &mdash;",
            "the longest run yet",
        ]),
        ("Cross-references", [
            "AN 9.42&ndash;51 &middot; ch.5's identical method, now "
            "continued here",
            "AN 9.51 &middot; previous chapter's closing page",
            "AN 9.53 &middot; next, Reaching a Safe Place",
        ]),
    ],
    further=[
        '<a href="%s/an9.52/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.51.html">AN 9.51 &middot; Extinguishment in This Life</a> &mdash; '
        "previous.",
        '<a href="an-9.53.html">AN 9.53 &middot; Reaching a Safe Place</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.53 — Khemappattasutta — first of this chapter's minimal stubs
# --------------------------------------------------------------------------- #
page(
    53, "Khemappatta", "Reaching a Safe Place",
    vagga=VAGGA_6,
    meta_title="AN 9.53 — Reaching a Safe Place | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Reaching a Safe Place, "
        "the first of this chapter's eight minimal stubs — pairing AN "
        "9.52's bare &lsquo;safe place&rsquo; with the achievement of "
        "actually arriving there. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.52"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, the first of "
                 "eight discourses in this chapter reduced this far"),
        ("Length", "A few seconds to read what exists"),
        ("A state versus its achievement", "Where AN 9.52 named safety "
         "itself, this discourse names the accomplishment of actually "
         "reaching it — the first of five such paired distinctions in "
         "this chapter"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, its interest lying in what it "
                       "pairs with"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;reaching a safe place&rdquo;&rsquo; "
        "&mdash; followed by an ellipsis, applying the same nine-stage "
        "template as AN 9.52 to the achievement of arriving at safety "
        "rather than to safety as a state."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;reaching a safe place&rsquo; &mdash; qualifiedly at "
            "each of the first eight stages, definitively only at the "
            "ninth &mdash; though the source no longer spells this out."]),
        ("A state, and its achievement", [
            "This discourse's relationship to AN 9.52 is not "
            "repetition but a grammatical shift: where khema names "
            "safety as a state or place, khemappatta names the "
            "accomplishment of a person who has actually arrived there "
            "&mdash; the first of five such state-versus-achievement "
            "pairs running through this chapter's first ten discourses."]),
        ("The same minimal treatment as the extinguishment-run", [
            "As with AN 9.48 through AN 9.50 in the previous chapter, "
            "this discourse's brevity is the source's own choice, not a "
            "gap this guide fills in with invented content. What can be "
            "said with confidence comes by inference from AN 9.52's "
            "fully spelled-out template."]),
        ("Opening the longest run of stubs in this project", [
            "This is the first of eight consecutive discourses (AN 9.53 "
            "through AN 9.60) reduced to a single surviving line, the "
            "longest such run met anywhere so far &mdash; four more "
            "paired terms will follow this same pattern before AN 9.61 "
            "restores full treatment."]),
    ],
    terms=[
        ("khemappattaṁ",
         "&ldquo;reaching a safe place&rdquo; &mdash; this discourse's "
         "own title term, naming the achievement of arriving at safety "
         "rather than safety as a bare state."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("khemaṁ",
         "&ldquo;a safe place&rdquo; &mdash; the paired term from AN "
         "9.52, this discourse's own state-versus-achievement "
         "counterpart."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.53:1.1-1.1"),
    ],
    quiz=[
        {"q": "How does this discourse's term relate grammatically to "
              "AN 9.52's &lsquo;khema&rsquo;?",
         "opts": [
             "It is an unrelated new term",
             "It names the achievement of arriving at safety, rather "
             "than safety itself as a bare state",
             "It contradicts AN 9.52's meaning",
             "It is simply a Pāli synonym with no distinction"],
         "correct": 1,
         "expl": "A state versus its achievement, the first of five "
                 "such pairs in this chapter."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "Only a title with no text",
             "A three-stage abbreviated version"],
         "correct": 1,
         "expl": "The first of eight discourses in this chapter reduced "
                 "this far."},
        {"q": "What does the guide do about the missing content?",
         "opts": [
             "Invents the missing stages",
             "Notes the omission honestly and supplies what can be said "
             "by inference from AN 9.52's fully spelled-out template",
             "Ignores the discourse",
             "Claims it has no meaning at all"],
         "correct": 1,
         "expl": "Consistent with this project's rule against inventing "
                 "text not in the source."},
        {"q": "How long is the run of minimal stubs this discourse "
              "opens?",
         "opts": [
             "Three discourses",
             "Eight discourses, AN 9.53 through AN 9.60",
             "Only this one discourse",
             "The rest of the entire nipāta"],
         "correct": 1,
         "expl": "The longest such run met anywhere in this project so "
                 "far."},
        {"q": "Which discourse restores full treatment, closing this "
              "run?",
         "opts": [
             "AN 9.55", "AN 9.58", "AN 9.61", "AN 9.53 itself"],
         "correct": 2,
         "expl": "Progressive cessation, matching AN 9.52's full "
                 "treatment at the run's start."},
        {"q": "Where does this discourse's implied nine-stage content "
              "come from?",
         "opts": [
             "It cannot be determined at all",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated discourse",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this "
                 "run of stubs."},
    ],
    marginalia=[
        ("A state, an achievement", [
            "khema, safety itself;",
            "khemappatta, one who's",
            "actually arrived",
        ]),
        ("One line, nothing more", [
            "the source's own choice &mdash;",
            "not invented, only",
            "honestly noted",
        ]),
        ("The longest run begins", [
            "eight discourses, each",
            "a single surviving line &mdash;",
            "four pairs, minimally told",
        ]),
        ("Cross-references", [
            "AN 9.52 &middot; the full template this stub relies on by "
            "inference",
            "AN 9.54 &middot; next, Freedom From Death",
        ]),
    ],
    further=[
        '<a href="%s/an9.53/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.52.html">AN 9.52 &middot; A Safe Place</a> &mdash; previous.',
        '<a href="an-9.54.html">AN 9.54 &middot; Freedom From Death</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.54 — Amatasutta
# --------------------------------------------------------------------------- #
page(
    54, "Amata", "Freedom From Death",
    vagga=VAGGA_6,
    meta_title="AN 9.54 — Freedom From Death | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Freedom From Death, "
        "the second of this chapter's minimal stubs, naming the "
        "deathless itself via the same nine-stage template applied "
        "throughout this run. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.53"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching AN "
                 "9.53's minimal survival"),
        ("Length", "A few seconds to read what exists"),
        ("A term already familiar from this chapter's neighbors", "The "
         "deathless (amata) already appeared as the shared closing "
         "formula at AN 9.16 and AN 9.34's own affliction-test; here it "
         "receives its own dedicated, if minimal, discourse"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, its interest lying in the term "
                       "itself"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;freedom from death&rdquo;&rsquo; "
        "&mdash; applying the same nine-stage template as AN 9.52 to "
        "amata, the deathless, a term already met repeatedly elsewhere "
        "in this nipāta as the culmination other teachings point toward."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;freedom from death&rsquo; &mdash; qualifiedly at "
            "each of the first eight stages, definitively only at the "
            "ninth."]),
        ("A term this nipāta has already used repeatedly", [
            "Unlike some of this chapter's other terms, amata isn't a "
            "new introduction: it closed AN 9.16's nine perceptions as "
            "their &lsquo;objective and culmination,&rsquo; and it "
            "closed AN 9.14's chain of questions the same way. This "
            "discourse gives the term its own dedicated treatment, "
            "however minimal, rather than using it only as a closing "
            "flourish for something else."]),
        ("Second of four remaining paired terms", [
            "Following AN 9.52-53's safe/reaching-safe pair, this "
            "discourse opens the second of this chapter's five term-"
            "pairs &mdash; deathless and reaching the deathless "
            "&mdash; continuing the same structural rhythm."]),
        ("The same honest minimalism", [
            "As throughout this run, the guide does not invent content "
            "the source omits. What can be said with confidence is "
            "supplied by inference from AN 9.52's fully spelled-out "
            "template, not from anything unique to this particular "
            "discourse's own surviving text."]),
    ],
    terms=[
        ("amataṁ",
         "&ldquo;freedom from death, the deathless&rdquo; &mdash; this "
         "discourse's own title term, already met as a closing formula "
         "at AN 9.14 and AN 9.16."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("amatogadhā amatapariyosānā",
         "&ldquo;their objective and culmination is freedom from "
         "death&rdquo; &mdash; AN 9.16's own use of this same term as a "
         "closing flourish, distinct from this discourse's dedicated "
         "treatment."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.54:1.1-1.1"),
    ],
    quiz=[
        {"q": "What term does this discourse define?",
         "opts": [
             "A safe place",
             "Freedom from death (amata, the deathless)",
             "Progressive tranquility",
             "Cessation"],
         "correct": 1,
         "expl": "A term already met elsewhere in this nipāta as a "
                 "closing formula."},
        {"q": "Where has this exact term already appeared earlier in "
              "this nipāta?",
         "opts": [
             "Nowhere before this discourse",
             "As the closing &lsquo;objective and culmination&rsquo; at "
             "AN 9.16, and closing AN 9.14's chain of questions",
             "Only in the very first discourse of AN 9",
             "It has never appeared before in the entire canon"],
         "correct": 1,
         "expl": "Used there as a closing flourish; here given its own "
                 "dedicated, if minimal, discourse."},
        {"q": "What pair of terms does this discourse open, continuing "
              "this chapter's structure?",
         "opts": [
             "Safety and reaching safety",
             "The deathless and reaching the deathless",
             "Tranquility and progressive tranquility",
             "Cessation and progressive cessation"],
         "correct": 1,
         "expl": "The second of this chapter's five term-pairs."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching AN 9.53's equally minimal survival."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
        {"q": "At which stage alone would freedom from death be "
              "achieved in a definitive sense, following this "
              "chapter's pattern?",
         "opts": [
             "The first absorption",
             "The dimension of nothingness",
             "The cessation of perception and feeling",
             "All nine stages equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern held throughout "
                 "this entire stretch of the nipāta."},
    ],
    marginalia=[
        ("A familiar term, dedicated", [
            "amata, already",
            "a closing flourish twice &mdash;",
            "now, its own discourse",
        ]),
        ("Second of five pairs", [
            "safe, then deathless &mdash;",
            "the same rhythm continues,",
            "minimally told",
        ]),
        ("Inference, not invention", [
            "one line surviving &mdash;",
            "the rest, drawn honestly",
            "from AN 9.52",
        ]),
        ("Cross-references", [
            "AN 9.14, AN 9.16 &middot; earlier uses of amata as a "
            "closing formula",
            "AN 9.53 &middot; previous",
            "AN 9.55 &middot; next, Reaching Freedom From Death",
        ]),
    ],
    further=[
        '<a href="%s/an9.54/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.53.html">AN 9.53 &middot; Reaching a Safe Place</a> &mdash; previous.',
        '<a href="an-9.55.html">AN 9.55 &middot; Reaching Freedom From Death</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.55 — Amatappattasutta
# --------------------------------------------------------------------------- #
page(
    55, "Amatappatta", "Reaching Freedom From Death",
    vagga=VAGGA_6,
    meta_title="AN 9.55 — Reaching Freedom From Death | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Reaching Freedom From "
        "Death, closing the deathless pair opened at AN 9.54 with the "
        "same minimal treatment applied throughout this run. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.54"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching this "
                 "chapter's other minimal stubs"),
        ("Length", "A few seconds to read what exists"),
        ("Closing the second pair", "This discourse pairs with AN 9.54 "
         "exactly as AN 9.53 paired with AN 9.52 — the achievement of "
         "arrival, following the bare state"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, its interest lying in its "
                       "pairing"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;reaching freedom from "
        "death&rdquo;&rsquo; &mdash; closing the deathless pair opened "
        "at AN 9.54 by naming the achievement of arrival rather than "
        "the state itself."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;reaching freedom from death&rsquo; &mdash; "
            "qualifiedly at each of the first eight stages, "
            "definitively only at the ninth."]),
        ("The same state-versus-achievement shift as AN 9.53", [
            "This discourse relates to AN 9.54 exactly as AN 9.53 "
            "related to AN 9.52: amatappatta names the accomplishment "
            "of a person who has actually reached the deathless, not "
            "the deathless as a bare state or object &mdash; the same "
            "grammatical pairing pattern this chapter applies "
            "consistently across all five of its term-pairs."]),
        ("Two pairs closed, three more discourses to go", [
            "With this discourse, the first two of this chapter's five "
            "term-pairs are complete: safety and reaching safety (AN "
            "9.52-53), and the deathless and reaching the deathless (AN "
            "9.54-55). Three further discourses in this run remain "
            "before AN 9.61 restores full treatment."]),
        ("Consistency across an entirely elided run", [
            "Nothing in this discourse's own surviving text "
            "distinguishes it structurally from AN 9.53 or AN 9.54; "
            "its interest lies entirely in what term it names and how "
            "that term relates to its pair, not in any unique content "
            "of its own, since none survives."]),
    ],
    terms=[
        ("amatappattaṁ",
         "&ldquo;reaching freedom from death&rdquo; &mdash; this "
         "discourse's own title term, naming the achievement of arrival "
         "rather than the deathless as a bare state."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("amataṁ",
         "&ldquo;freedom from death&rdquo; &mdash; the paired term from "
         "AN 9.54, this discourse's own state-versus-achievement "
         "counterpart."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.55:1.1-1.1"),
    ],
    quiz=[
        {"q": "How does this discourse's term relate to AN 9.54's "
              "&lsquo;amata&rsquo;?",
         "opts": [
             "It is an unrelated new term",
             "It names the achievement of actually reaching the "
             "deathless, rather than the deathless as a bare state",
             "It contradicts AN 9.54's meaning",
             "It is used only in a completely different context"],
         "correct": 1,
         "expl": "The same state-versus-achievement pairing pattern as "
                 "AN 9.52-53."},
        {"q": "How many of this chapter's five term-pairs are complete "
              "after this discourse?",
         "opts": [
             "None", "One", "Two", "All five"],
         "correct": 2,
         "expl": "Safety/reaching safety, and the deathless/reaching "
                 "the deathless."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching every other stub in this chapter's run."},
        {"q": "Where does this discourse's real interest lie, according "
              "to the guide?",
         "opts": [
             "In unique content found only in this discourse",
             "In what term it names and how that term pairs with AN "
             "9.54, not in any content unique to its own text",
             "In a narrative found nowhere else",
             "In a contradiction of the surrounding discourses"],
         "correct": 1,
         "expl": "Nothing distinguishes its own surviving text from any "
                 "other stub in this run."},
        {"q": "How many discourses in this run of stubs remain after "
              "this one, before full treatment is restored?",
         "opts": [
             "None; this is the last stub",
             "Three — AN 9.56 through AN 9.58, before AN 9.61 restores "
             "full treatment",
             "Ten more discourses",
             "It cannot be determined"],
         "correct": 1,
         "expl": "Fearless/reaching fearless and tranquility/progressive "
                 "tranquility remain, plus bare cessation."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
    ],
    marginalia=[
        ("Two pairs, now complete", [
            "safe, and reaching it;",
            "deathless, and reaching it &mdash;",
            "the same shift, twice",
        ]),
        ("Nothing unique to find", [
            "one line, like the rest &mdash;",
            "interest lies only",
            "in the pairing itself",
        ]),
        ("Three stubs still ahead", [
            "fearless, tranquility,",
            "bare cessation next &mdash;",
            "then 9.61 restores",
        ]),
        ("Cross-references", [
            "AN 9.54 &middot; the state this discourse's achievement "
            "pairs with",
            "AN 9.56 &middot; next, A Place Without Fear",
        ]),
    ],
    further=[
        '<a href="%s/an9.55/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.54.html">AN 9.54 &middot; Freedom From Death</a> &mdash; previous.',
        '<a href="an-9.56.html">AN 9.56 &middot; A Place Without Fear</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.56 — Abhayasutta
# --------------------------------------------------------------------------- #
page(
    56, "Abhaya", "A Place Without Fear",
    vagga=VAGGA_6,
    meta_title="AN 9.56 — A Place Without Fear | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for A Place Without Fear, "
        "opening this chapter's third term-pair with the same minimal "
        "treatment as its neighbors. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.55"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching this "
                 "chapter's other minimal stubs"),
        ("Length", "A few seconds to read what exists"),
        ("Opening the third pair", "Fearlessness (abhaya) and reaching "
         "it, the third of this chapter's five term-pairs, following "
         "safety and the deathless"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, its interest lying in the "
                       "term itself"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;a place without fear&rdquo;&rsquo; "
        "&mdash; applying the same nine-stage template once more, this "
        "time to fearlessness, opening this chapter's third term-pair."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;a place without fear&rsquo; &mdash; qualifiedly at "
            "each of the first eight stages, definitively only at the "
            "ninth."]),
        ("A third pair, following the same rhythm", [
            "After safety (AN 9.52-53) and the deathless (AN 9.54-55), "
            "this discourse opens the third of this chapter's five "
            "term-pairs: fearlessness and reaching fearlessness, "
            "continuing the identical structural pattern without "
            "variation."]),
        ("A term with real resonance elsewhere in this project", [
            "&lsquo;Abhaya,&rsquo; freedom from fear, echoes the five "
            "fears quelled by ethical restraint at AN 9.27 and AN 9.28 "
            "&mdash; though those discourses named specific, nameable "
            "worldly fears overcome by precepts and confidence, while "
            "this discourse applies the term instead to the nine "
            "meditative attainments, in keeping with this whole "
            "chapter's method."]),
        ("The same honest brevity", [
            "As throughout this run, nothing is invented to fill the "
            "gap the source leaves. What can be said with confidence "
            "about this discourse's likely content comes entirely by "
            "inference from AN 9.52's fully spelled-out template."]),
    ],
    terms=[
        ("abhayaṁ",
         "&ldquo;a place without fear&rdquo; &mdash; this discourse's "
         "own title term, opening this chapter's third pair."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("pañca bhayāni verāni vūpasantāni",
         "&ldquo;five fears and enmities... quelled&rdquo; &mdash; AN "
         "9.27 and AN 9.28's own, differently framed use of "
         "fearlessness, naming specific worldly fears rather than the "
         "nine attainments."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.56:1.1-1.1"),
    ],
    quiz=[
        {"q": "What term does this discourse open a new pair around?",
         "opts": [
             "Tranquility",
             "Fearlessness (abhaya), a place without fear",
             "Cessation",
             "Confinement"],
         "correct": 1,
         "expl": "The third of this chapter's five term-pairs, "
                 "following safety and the deathless."},
        {"q": "How does this discourse's use of &lsquo;fearlessness&rsquo; "
              "compare to AN 9.27 and AN 9.28's?",
         "opts": [
             "Identical in every respect",
             "Those discourses named specific worldly fears overcome by "
             "ethical restraint; this one applies the term to the nine "
             "meditative attainments instead",
             "This discourse contradicts those earlier ones",
             "There is no relationship between them"],
         "correct": 1,
         "expl": "A different application of a term with real resonance "
                 "earlier in this nipāta."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching every other stub in this chapter's run."},
        {"q": "What is this discourse's position among this chapter's "
              "five term-pairs?",
         "opts": [
             "The first pair",
             "The third pair, following safety and the deathless",
             "The fifth and final pair",
             "It doesn't belong to any pair"],
         "correct": 1,
         "expl": "Fearlessness and reaching fearlessness, continuing "
                 "the established rhythm."},
        {"q": "What does the guide avoid doing with this discourse's "
              "missing content?",
         "opts": [
             "Inventing plausible-sounding text to fill the gap",
             "Discussing the term at all",
             "Both of the above",
             "Neither; it fabricates freely"],
         "correct": 0,
         "expl": "Consistent with this project's standing rule against "
                 "inventing text not in the source."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
    ],
    marginalia=[
        ("A third pair opens", [
            "safe, deathless, now",
            "fearless &mdash; the same rhythm,",
            "the same brief treatment",
        ]),
        ("A term heard before", [
            "five fears quelled once,",
            "at AN 9.27 &mdash;",
            "here, a new frame",
        ]),
        ("Honest about the gap", [
            "one line surviving &mdash;",
            "nothing invented to",
            "fill what's not there",
        ]),
        ("Cross-references", [
            "AN 9.27, AN 9.28 &middot; an earlier, differently framed "
            "use of fearlessness",
            "AN 9.55 &middot; previous",
            "AN 9.57 &middot; next, Reaching a Place Without Fear",
        ]),
    ],
    further=[
        '<a href="%s/an9.56/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.55.html">AN 9.55 &middot; Reaching Freedom From Death</a> &mdash; '
        "previous.",
        '<a href="an-9.57.html">AN 9.57 &middot; Reaching a Place Without Fear</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.57 — Abhayappattasutta
# --------------------------------------------------------------------------- #
page(
    57, "Abhayappatta", "Reaching a Place Without Fear",
    vagga=VAGGA_6,
    meta_title="AN 9.57 — Reaching a Place Without Fear | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Reaching a Place "
        "Without Fear, closing the fearlessness pair opened at AN 9.56, "
        "with the same minimal treatment as this chapter's other "
        "stubs. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.56"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching this "
                 "chapter's other minimal stubs"),
        ("Length", "A few seconds to read what exists"),
        ("Closing the third pair", "Following the same state-versus-"
         "achievement shift as AN 9.53 and AN 9.55, closing this "
         "chapter's third term-pair"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, its interest lying in its "
                       "pairing"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;reaching a place without "
        "fear&rdquo;&rsquo; &mdash; closing the fearlessness pair opened "
        "at AN 9.56 by naming the achievement of arrival rather than "
        "the state itself."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;reaching a place without fear&rsquo; &mdash; "
            "qualifiedly at each of the first eight stages, "
            "definitively only at the ninth."]),
        ("The third state-versus-achievement pairing", [
            "This discourse relates to AN 9.56 exactly as AN 9.53 "
            "related to AN 9.52, and AN 9.55 to AN 9.54: "
            "abhayappatta names the accomplishment of a person who has "
            "actually reached fearlessness, not fearlessness as a bare "
            "state &mdash; the third instance of this chapter's "
            "consistent pairing pattern."]),
        ("Three pairs closed, two discourses left in the run", [
            "With this discourse, three of this chapter's five term-"
            "pairs are complete. Only tranquility and progressive "
            "tranquility (AN 9.58-59) and bare cessation (AN 9.60) "
            "remain before AN 9.61 restores full treatment, closing the "
            "whole run."]),
        ("A pattern reliable enough to predict, not merely observe", [
            "By this point in the run, the pairing pattern is reliable "
            "enough that a reader could predict this discourse's likely "
            "content before opening it &mdash; a useful check on "
            "whether the chapter's structure has actually been "
            "understood, not just described."]),
    ],
    terms=[
        ("abhayappattaṁ",
         "&ldquo;reaching a place without fear&rdquo; &mdash; this "
         "discourse's own title term, naming the achievement of arrival "
         "rather than fearlessness as a bare state."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("abhayaṁ",
         "&ldquo;a place without fear&rdquo; &mdash; the paired term "
         "from AN 9.56, this discourse's own state-versus-achievement "
         "counterpart."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.57:1.1-1.1"),
    ],
    quiz=[
        {"q": "How does this discourse's term relate to AN 9.56's "
              "&lsquo;abhaya&rsquo;?",
         "opts": [
             "It is an unrelated new term",
             "It names the achievement of actually reaching "
             "fearlessness, rather than fearlessness as a bare state",
             "It contradicts AN 9.56's meaning",
             "It is used only in a completely different context"],
         "correct": 1,
         "expl": "The third instance of this chapter's consistent "
                 "state-versus-achievement pairing pattern."},
        {"q": "How many of this chapter's five term-pairs are complete "
              "after this discourse?",
         "opts": [
             "One", "Two", "Three", "All five"],
         "correct": 2,
         "expl": "Safety, the deathless, and fearlessness, each with "
                 "their reaching-counterpart."},
        {"q": "According to the guide, what could a reader do by this "
              "point in the run?",
         "opts": [
             "Nothing useful; each discourse is unpredictable",
             "Predict this discourse's likely content before opening "
             "it, a check on whether the chapter's structure is "
             "actually understood",
             "Skip the remaining discourses entirely",
             "Assume the pattern has broken down"],
         "correct": 1,
         "expl": "The pairing pattern has become reliable enough to "
                 "anticipate."},
        {"q": "How many discourses remain in this run of stubs after "
              "this one?",
         "opts": [
             "None; the run ends here",
             "Three — AN 9.58, AN 9.59, and AN 9.60 — before AN 9.61 "
             "restores full treatment",
             "Ten more discourses",
             "It cannot be determined"],
         "correct": 1,
         "expl": "Tranquility, progressive tranquility, and bare "
                 "cessation remain."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching every other stub in this chapter's run."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
    ],
    marginalia=[
        ("Three pairs, now complete", [
            "safe, deathless, fearless &mdash;",
            "each with its own reaching,",
            "told the same brief way",
        ]),
        ("A predictable pattern", [
            "by now, a reader",
            "could guess before reading &mdash;",
            "the structure is clear",
        ]),
        ("Two more stubs remain", [
            "tranquility, then",
            "bare cessation &mdash; then",
            "9.61 restores",
        ]),
        ("Cross-references", [
            "AN 9.56 &middot; the state this discourse's achievement "
            "pairs with",
            "AN 9.58 &middot; next, Tranquility",
        ]),
    ],
    further=[
        '<a href="%s/an9.57/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.56.html">AN 9.56 &middot; A Place Without Fear</a> &mdash; previous.',
        '<a href="an-9.58.html">AN 9.58 &middot; Tranquility</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.58 — Passaddhisutta — shifts the pairing pattern from bare/reaching
# to bare/progressive
# --------------------------------------------------------------------------- #
page(
    58, "Passaddhi", "Tranquility",
    vagga=VAGGA_6,
    meta_title="AN 9.58 — Tranquility | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Tranquility, opening "
        "this chapter's fourth term-pair with a shift from the "
        "bare/reaching pattern to a bare/progressive pattern. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.57"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching this "
                 "chapter's other minimal stubs"),
        ("Length", "A few seconds to read what exists"),
        ("A shift in the pairing pattern", "The first three pairs "
         "contrasted a bare state with reaching it; this pair and the "
         "next instead contrast a bare state with a &lsquo;progressive"
         "&rsquo; version of the same state"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, worth noticing the structural "
                       "shift it introduces"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;tranquility&rdquo;&rsquo; &mdash; "
        "opening this chapter's fourth term-pair with a structural "
        "shift: rather than pairing with a &lsquo;reaching&rsquo; "
        "counterpart, tranquility pairs with a &lsquo;progressive"
        "&rsquo; one at AN 9.59."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;tranquility&rsquo; &mdash; qualifiedly at each of "
            "the first eight stages, definitively only at the ninth."]),
        ("A quiet shift in this chapter's pairing pattern", [
            "The first three pairs in this chapter &mdash; safety, the "
            "deathless, fearlessness &mdash; each paired a bare state "
            "with the achievement of &lsquo;reaching&rsquo; it "
            "(khema/khemappatta, and so on). This discourse breaks that "
            "pattern: rather than an "
            "&lsquo;-appatta&rsquo; counterpart, passaddhi pairs with "
            "&lsquo;anupubbapassaddhi,&rsquo; progressive tranquility, "
            "at AN 9.59."]),
        ("Tranquility, echoing earlier meditative vocabulary", [
            "Passaddhi, tranquility or calm, is standard vocabulary for "
            "the settling of bodily and mental activity that "
            "accompanies deepening absorption, related to but distinct "
            "from the samatha (stillness) more commonly paired with "
            "vipassanā (insight) elsewhere in the tradition."]),
        ("Fourth of five pairs, one more remaining", [
            "With this discourse, four of this chapter's five terms are "
            "underway; only cessation, the fifth and final pair (AN "
            "9.60-61), remains before this whole run of stubs closes "
            "and full treatment returns."]),
    ],
    terms=[
        ("passaddhi",
         "&ldquo;tranquility&rdquo; &mdash; this discourse's own title "
         "term, opening this chapter's fourth pair with a shift to a "
         "bare/progressive pairing pattern."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("anupubbapassaddhi",
         "&ldquo;progressive tranquility&rdquo; &mdash; the paired term "
         "explored next, at AN 9.59, this discourse's own counterpart."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.58:1.1-1.1"),
    ],
    quiz=[
        {"q": "What structural shift does this discourse introduce to "
              "this chapter's pairing pattern?",
         "opts": [
             "No shift at all; it continues identically",
             "Rather than pairing with a &lsquo;reaching&rsquo; "
             "counterpart, tranquility pairs with a &lsquo;"
             "progressive&rsquo; version at AN 9.59",
             "It abandons the pairing structure entirely",
             "It introduces a sixth term-pair"],
         "correct": 1,
         "expl": "The first three pairs used bare/reaching; this pair "
                 "and the next use bare/progressive."},
        {"q": "What does &lsquo;passaddhi&rsquo; refer to?",
         "opts": [
             "A monastic robe",
             "Tranquility or calm, the settling of bodily and mental "
             "activity accompanying deepening absorption",
             "A type of almsfood",
             "A geographic location"],
         "correct": 1,
         "expl": "Standard meditative vocabulary, related to but "
                 "distinct from samatha."},
        {"q": "How many of this chapter's five term-pairs are underway "
              "or complete after this discourse?",
         "opts": [
             "Two", "Three", "Four", "All five"],
         "correct": 2,
         "expl": "Safety, the deathless, fearlessness, and now "
                 "tranquility (opened, awaiting its pair at AN 9.59)."},
        {"q": "What remains after AN 9.58 and AN 9.59, before this run "
              "of stubs closes?",
         "opts": [
             "Nothing; the run ends here",
             "Bare cessation (AN 9.60), before AN 9.61 restores full "
             "treatment",
             "Five more term-pairs",
             "A return to the beginning of the chapter"],
         "correct": 1,
         "expl": "The fifth and final pair, cessation and progressive "
                 "cessation."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching every other stub in this chapter's run."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
    ],
    marginalia=[
        ("A pattern shifts", [
            "no longer &lsquo;reaching&rsquo; now,",
            "but &lsquo;progressive&rsquo; instead &mdash;",
            "a quiet structural turn",
        ]),
        ("A familiar meditative word", [
            "passaddhi, calm &mdash;",
            "settling of body and mind",
            "as absorption deepens",
        ]),
        ("One pair left", [
            "tranquility now;",
            "cessation still to come &mdash;",
            "the run nears its end",
        ]),
        ("Cross-references", [
            "AN 9.57 &middot; previous",
            "AN 9.59 &middot; next, Progressive Tranquility",
        ]),
    ],
    further=[
        '<a href="%s/an9.58/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.57.html">AN 9.57 &middot; Reaching a Place Without Fear</a> &mdash; '
        "previous.",
        '<a href="an-9.59.html">AN 9.59 &middot; Progressive Tranquility</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.59 — Anupubbapassaddhisutta
# --------------------------------------------------------------------------- #
page(
    59, "Anupubbapassaddhi", "Progressive Tranquility",
    vagga=VAGGA_6,
    meta_title="AN 9.59 — Progressive Tranquility | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Progressive "
        "Tranquility, closing the tranquility pair opened at AN 9.58 "
        "and echoing this project's earlier progressive-cessation and "
        "progressive-meditation discourses by name. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.58"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, matching this "
                 "chapter's other minimal stubs"),
        ("Length", "A few seconds to read what exists"),
        ("A title echoing two earlier discourses", "&lsquo;"
         "Anupubba&rsquo;, &ldquo;progressive,&rdquo; directly echoes "
         "the titles of AN 9.31 and AN 9.32, though this discourse's "
         "content and method are entirely this chapter's own"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, its interest lying in the "
                       "title's resonance"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;progressive tranquility&rdquo;"
        "&rsquo; &mdash; closing the tranquility pair opened at AN "
        "9.58, its title echoing &lsquo;anupubba,&rsquo; "
        "&ldquo;progressive,&rdquo; already met in the titles of AN "
        "9.31 and AN 9.32."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of the "
            "nine progressive attainments is what the Buddha meant by "
            "&lsquo;progressive tranquility&rsquo; &mdash; qualifiedly "
            "at each of the first eight stages, definitively only at "
            "the ninth."]),
        ("A title that echoes, without repeating content", [
            "&lsquo;Anupubba,&rsquo; progressive, is the same word "
            "opening the titles of AN 9.31 (&ldquo;Progressive "
            "Cessations&rdquo;) and AN 9.32 (&ldquo;Progressive "
            "Meditations&rdquo;), both foundational catalogues from "
            "ch.4. This discourse's title echoes that vocabulary, but "
            "its own content and method belong entirely to ch.6's "
            "Udāyī-to-Ānanda template, not to those earlier discourses' "
            "different framing."]),
        ("Closing the fourth pair", [
            "This discourse completes the tranquility pair, "
            "passaddhi and anupubbapassaddhi, the fourth of this "
            "chapter's five term-pairs &mdash; though unlike the first "
            "three pairs' bare/reaching structure, this one and the "
            "next instead contrast a bare state with its own "
            "&lsquo;progressive&rsquo; unfolding across the nine "
            "stages."]),
        ("One term-pair left before full treatment returns", [
            "Only bare cessation, nirodha, remains at AN 9.60 before "
            "its own progressive counterpart, anupubbanirodha at AN "
            "9.61, restores full treatment and closes this entire run "
            "of minimal stubs."]),
    ],
    terms=[
        ("anupubbapassaddhi",
         "&ldquo;progressive tranquility&rdquo; &mdash; this "
         "discourse's own title term, closing the pair opened at AN "
         "9.58."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("anupubbavihārā, anupubbanirodhā",
         "&ldquo;progressive meditations, progressive cessations&rdquo; "
         "&mdash; AN 9.32 and AN 9.31's own titles, sharing this "
         "discourse's opening word without sharing its content or "
         "method."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; not present in "
         "this discourse's own text, supplied by inference from AN "
         "9.52's template."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; likewise supplied "
         "by inference, reserved for the ninth attainment throughout "
         "this stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.59:1.1-1.1"),
    ],
    quiz=[
        {"q": "What two earlier discourses does this discourse's title "
              "echo?",
         "opts": [
             "AN 9.1 and AN 9.9",
             "AN 9.31 (&ldquo;Progressive Cessations&rdquo;) and AN "
             "9.32 (&ldquo;Progressive Meditations&rdquo;)",
             "AN 9.42 and AN 9.47",
             "AN 9.16 and AN 9.34"],
         "correct": 1,
         "expl": "Both share the word &lsquo;anupubba,&rsquo; "
                 "&ldquo;progressive.&rdquo;"},
        {"q": "Does this discourse share content or method with those "
              "two earlier discourses?",
         "opts": [
             "Yes, identical content",
             "No — only the title's opening word is shared; the content "
             "and method belong entirely to ch.6's own template",
             "It directly contradicts them",
             "It merges all three into one teaching"],
         "correct": 1,
         "expl": "A shared word, not shared content — an echo, not a "
                 "repetition."},
        {"q": "What pair does this discourse close?",
         "opts": [
             "Safety and reaching safety",
             "Tranquility and progressive tranquility, opened at AN "
             "9.58",
             "Fearlessness and reaching fearlessness",
             "Cessation and progressive cessation"],
         "correct": 1,
         "expl": "The fourth of this chapter's five term-pairs."},
        {"q": "What term-pair remains after this discourse, before full "
              "treatment returns?",
         "opts": [
             "None; this closes the run",
             "Cessation and progressive cessation, at AN 9.60-61",
             "A sixth, previously unmentioned pair",
             "A return to the safety pair"],
         "correct": 1,
         "expl": "The fifth and final pair, closing this whole run of "
                 "minimal stubs."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching every other stub in this chapter's run."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
    ],
    marginalia=[
        ("A word, echoed", [
            "&lsquo;progressive&rsquo; &mdash; the same",
            "word as 9.31, 9.32 &mdash;",
            "content, not shared",
        ]),
        ("Fourth pair, closed", [
            "tranquility, then",
            "its progressive form &mdash;",
            "the same brief telling",
        ]),
        ("One pair left", [
            "cessation still ahead,",
            "then its progressive form &mdash;",
            "the run nearly done",
        ]),
        ("Cross-references", [
            "AN 9.31, AN 9.32 &middot; the earlier discourses this "
            "title echoes without repeating",
            "AN 9.58 &middot; previous",
            "AN 9.60 &middot; next, Cessation",
        ]),
    ],
    further=[
        '<a href="%s/an9.59/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.58.html">AN 9.58 &middot; Tranquility</a> &mdash; previous.',
        '<a href="an-9.60.html">AN 9.60 &middot; Cessation</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.60 — Nirodhasutta — last of the eight minimal stubs
# --------------------------------------------------------------------------- #
page(
    60, "Nirodha", "Cessation",
    vagga=VAGGA_6,
    meta_title="AN 9.60 — Cessation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide and self-check quiz for Cessation, the last of "
        "this chapter's eight minimal stubs, opening the fifth and "
        "final term-pair before AN 9.61 restores full treatment. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.59"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda, by "
                     "implication"),
        ("Form", "A single opening line and an ellipsis, the last of "
                 "eight discourses in this chapter reduced this far"),
        ("Length", "A few seconds to read what exists"),
        ("The last stub in the run", "This discourse closes the eight-"
         "discourse run of minimal stubs begun at AN 9.53; its pair, AN "
         "9.61, restores full treatment"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read, marking a turning point in the "
                       "chapter"),
    ],
    why=(
        "The source reduces this discourse to a single line &mdash; "
        "&lsquo;they speak of &ldquo;cessation&rdquo;&rsquo; &mdash; "
        "opening this chapter's fifth and final term-pair, the last of "
        "eight consecutive discourses reduced to a single surviving "
        "line."),
    guide=[
        ("The teaching in one sentence", [
            "By the pattern established at AN 9.52, reaching any of "
            "the nine progressive attainments is what the Buddha meant "
            "by &lsquo;cessation&rsquo; &mdash; qualifiedly at each of "
            "the first eight stages, definitively only at the ninth."]),
        ("The last stub before full treatment returns", [
            "This discourse closes the longest run of minimal stubs "
            "met anywhere in this project: eight consecutive discourses "
            "(AN 9.53 through this one) surviving as no more than a "
            "single elided line each. Its pair, AN 9.61, breaks this "
            "pattern and restores full treatment."]),
        ("A term this project has met in fuller form before", [
            "&lsquo;Nirodha,&rsquo; cessation, is one of the most "
            "central terms in the whole tradition &mdash; the third "
            "noble truth, and the closing term of AN 9.31's fully "
            "elaborated &lsquo;progressive cessations.&rsquo; This "
            "discourse names the bare term itself, minimally, before "
            "its own progressive counterpart closes the run at AN 9.61."]),
        ("What follows: a return to full elaboration", [
            "AN 9.61, immediately next, is not simply the last item in "
            "this pattern; it breaks the pattern deliberately, spelling "
            "out the full nine-stage formula one more time to close "
            "both this run of paired terms and, two discourses later, "
            "this chapter itself."]),
    ],
    terms=[
        ("nirodho",
         "&ldquo;cessation&rdquo; &mdash; this discourse's own title "
         "term, opening this chapter's fifth and final pair."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; the source's own signal to supply the omitted content."),
        ("dukkhanirodho ariyasaccaṁ",
         "&ldquo;the noble truth of the cessation of suffering&rdquo; "
         "&mdash; the same root term's most famous doctrinal use, the "
         "third noble truth, distinct from this discourse's narrower "
         "meditative application."),
        ("anupubbanirodho",
         "&ldquo;progressive cessation&rdquo; &mdash; the paired term "
         "closing this run at AN 9.61, restoring full treatment."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; supplied by "
         "inference, reserved for the ninth attainment throughout this "
         "stretch of the nipāta."),
    ],
    text_intro=(
        "The discourse exactly as it survives in the source: one line "
        "and an ellipsis. Nothing has been added. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The discourse in full, as it survives"),
        ("p", "&sect;1", "an9.60:1.1-1.1"),
    ],
    quiz=[
        {"q": "What position does this discourse hold in this chapter's "
              "run of minimal stubs?",
         "opts": [
             "The first of the run",
             "The last of eight consecutive discourses reduced to a "
             "single surviving line",
             "The only stub in the chapter",
             "It falls outside the run entirely"],
         "correct": 1,
         "expl": "The longest such run met anywhere in this project, "
                 "closing here."},
        {"q": "What does this discourse's term, &lsquo;nirodha,&rsquo; "
              "name in its most famous doctrinal use elsewhere?",
         "opts": [
             "A monastic rule",
             "The third noble truth, the cessation of suffering",
             "A type of meditation posture",
             "A geographic location"],
         "correct": 1,
         "expl": "One of the most central terms in the whole tradition, "
                 "applied here more narrowly to the nine attainments."},
        {"q": "What happens at this discourse's pair, AN 9.61?",
         "opts": [
             "Another single-line stub, continuing the pattern",
             "Full treatment is restored, breaking the pattern of "
             "compression deliberately",
             "The chapter ends without further discourses",
             "The pairing pattern is abandoned entirely"],
         "correct": 1,
         "expl": "A deliberate return to complete elaboration, closing "
                 "both this run and setting up the chapter's own close."},
        {"q": "Where has this project already met &lsquo;nirodha&rsquo; "
              "in fuller, elaborated form?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.31's &ldquo;Progressive Cessations,&rdquo; closing "
             "with this same term",
             "Only in a completely different nipāta",
             "It has never appeared before in the canon"],
         "correct": 1,
         "expl": "The same root term, given full nine-stage treatment "
                 "earlier in this nipāta."},
        {"q": "How much of this discourse survives in the source?",
         "opts": [
             "The full nine-stage formula",
             "A single opening line and an ellipsis",
             "A three-stage summary",
             "Nothing at all"],
         "correct": 1,
         "expl": "Matching every other stub in this chapter's eight-"
                 "discourse run."},
        {"q": "Where does this discourse's implied content come from?",
         "opts": [
             "It cannot be inferred",
             "By inference from AN 9.52's fully spelled-out template",
             "From an unrelated chapter",
             "It must be invented"],
         "correct": 1,
         "expl": "The same source of inference used throughout this run "
                 "of stubs."},
    ],
    marginalia=[
        ("The last stub, closing", [
            "eight discourses, each",
            "a single line &mdash; this, the last",
            "before fullness returns",
        ]),
        ("A term met before, fuller", [
            "the third noble truth,",
            "and AN 9.31's own",
            "close, named again here",
        ]),
        ("What comes next breaks the pattern", [
            "not another stub &mdash;",
            "AN 9.61 spells",
            "the whole formula out",
        ]),
        ("Cross-references", [
            "AN 9.31 &middot; this same term, given full treatment "
            "earlier in this nipāta",
            "AN 9.59 &middot; previous",
            "AN 9.61 &middot; next, Progressive Cessation, restoring "
            "full treatment",
        ]),
    ],
    further=[
        '<a href="%s/an9.60/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.59.html">AN 9.59 &middot; Progressive Tranquility</a> &mdash; previous.',
        '<a href="an-9.61.html">AN 9.61 &middot; Progressive Cessation</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.61 — Anupubbanirodhasutta — restores full treatment, closing this
# chapter's run of five term-pairs
# --------------------------------------------------------------------------- #
page(
    61, "Anupubbanirodha", "Progressive Cessation",
    vagga=VAGGA_6,
    meta_title="AN 9.61 — Progressive Cessation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Progressive Cessation, restoring full treatment after eight "
        "minimal stubs and closing this chapter's run of five term-"
        "pairs. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Not restated; understood to continue from AN 9.60"),
        ("Speakers", "Venerable Udāyī questioning Venerable Ānanda"),
        ("Form", "The full nine-stage template spelled out again, after "
                 "eight discourses of minimal survival"),
        ("Length", "~1 minute to read"),
        ("Full treatment, restored deliberately", "This discourse "
         "breaks the run of minimal stubs begun at AN 9.53, matching "
         "AN 9.52's opening treatment to close the whole pattern"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief in itself, but marks a deliberate return "
                       "to full elaboration"),
    ],
    why=(
        "Closing the longest run of minimal stubs met anywhere in this "
        "project, Udāyī asks what &lsquo;progressive cessation&rsquo; "
        "means and Ānanda answers in full once more: each of the first "
        "eight attainments is progressive cessation in a qualified "
        "sense, and only the ninth, the cessation of perception and "
        "feeling, in a definitive sense."),
    guide=[
        ("The teaching in one sentence", [
            "Reaching any of the nine progressive attainments is what "
            "the Buddha meant by &lsquo;progressive cessation&rsquo; "
            "&mdash; in a qualified sense at each of the first eight "
            "stages, and in a definitive sense only upon reaching the "
            "cessation of perception and feeling."]),
        ("A deliberate bookend to eight stubs", [
            "This discourse's full treatment isn't an isolated event; "
            "it deliberately matches AN 9.52's opening treatment, "
            "framing the eight minimal stubs in between (AN 9.53 "
            "through AN 9.60) as a single compressed unit bracketed by "
            "two fully spelled-out discourses &mdash; the same "
            "structural bracketing this project has already met, for "
            "instance, in the peyyāla-opening pattern of full examples "
            "before compression sets in."]),
        ("The fifth and final pair, and this term's own history", [
            "This discourse closes the cessation pair opened at AN "
            "9.60 &mdash; the last of this chapter's five term-pairs "
            "&mdash; and its own title, &lsquo;anupubbanirodha,&rsquo; "
            "is identical to AN 9.31's title several chapters earlier, "
            "though the two discourses share only their name and "
            "underlying nine-stage content, not their surrounding "
            "method or dialogue frame."]),
        ("One discourse remains, closing the chapter differently", [
            "AN 9.62, immediately next, doesn't continue this chapter's "
            "Udāyī-to-Ānanda template at all; it closes "
            "<em>Khemavagga</em> with an entirely different kind of "
            "teaching, naming nine defilements that must be given up "
            "before perfection can be realized."]),
    ],
    terms=[
        ("anupubbanirodho",
         "&ldquo;progressive cessation&rdquo; &mdash; this discourse's "
         "own title term, identical to AN 9.31's title several chapters "
         "earlier, though the two share only their name."),
        ("pariyāyena",
         "&ldquo;in a qualified sense&rdquo; &mdash; the shared term "
         "for each of the first eight attainments, spelled out again "
         "here after eight stubs relied on inference alone."),
        ("nippariyāyena",
         "&ldquo;in a definitive sense&rdquo; &mdash; reserved for the "
         "ninth attainment, closing this discourse and this run of "
         "term-pairs alike."),
        ("nirodho",
         "&ldquo;cessation&rdquo; &mdash; the bare term from AN 9.60, "
         "this discourse's own state-versus-progressive counterpart."),
        ("saññāvedayitanirodhaṁ upasampajja viharati, paññāya cassa "
         "disvā āsavā parikkhīṇā honti",
         "&ldquo;enters and remains in the cessation of perception and "
         "feeling... their defilements come to an end&rdquo; &mdash; "
         "the shared closing formula for the definitive ninth stage."),
    ],
    text_intro=(
        "The discourse in full: the same nine-stage template, spelled "
        "out completely to close this chapter's run of five term-"
        "pairs. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Progressive cessation, at each of nine stages"),
        ("p", "&sect;1", "an9.61:1.1-2.2"),
        ("p", "&sect;2", "an9.61:3.1-3.2"),
    ],
    quiz=[
        {"q": "How does this discourse's treatment compare to the eight "
              "discourses immediately before it?",
         "opts": [
             "Equally minimal, one line and an ellipsis",
             "Full treatment is restored, deliberately matching AN "
             "9.52's opening treatment to bracket the eight stubs in "
             "between",
             "Even more compressed than the eight stubs",
             "Missing from the source entirely"],
         "correct": 1,
         "expl": "A deliberate bookend, framing the compressed run as "
                 "one structural unit."},
        {"q": "What pair does this discourse close?",
         "opts": [
             "Safety and reaching safety",
             "Cessation and progressive cessation, opened at AN 9.60",
             "The deathless and reaching the deathless",
             "Fearlessness and reaching fearlessness"],
         "correct": 1,
         "expl": "The fifth and final term-pair in this chapter's run."},
        {"q": "How does this discourse's title relate to AN 9.31's?",
         "opts": [
             "Entirely unrelated titles",
             "Identical titles, though the two discourses share only "
             "their name and underlying nine-stage content, not their "
             "method or dialogue frame",
             "AN 9.31 is a direct quotation of this discourse",
             "This discourse contradicts AN 9.31"],
         "correct": 1,
         "expl": "The same title reused across chapters, worth "
                 "distinguishing from genuine content overlap."},
        {"q": "What happens at AN 9.62, immediately following this "
              "discourse?",
         "opts": [
             "Another stub in the same Udāyī-to-Ānanda template",
             "A different kind of teaching entirely, closing the "
             "chapter with nine defilements to be given up before "
             "perfection can be realized",
             "The chapter simply ends without further discourses",
             "A return to the safety pair from the chapter's start"],
         "correct": 1,
         "expl": "A structural break from the template this whole "
                 "chapter has followed so far."},
        {"q": "At which stage alone is progressive cessation achieved "
              "in a definitive sense?",
         "opts": [
             "The first absorption",
             "The dimension of nothingness",
             "The cessation of perception and feeling",
             "All nine stages equally"],
         "correct": 2,
         "expl": "The consistent ninth-stage pattern held throughout "
                 "this entire chapter."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha alone",
             "Venerable Udāyī questioning Venerable Ānanda",
             "Sāriputta questioning Mahākoṭṭhita",
             "Two brahmin cosmologists"],
         "correct": 1,
         "expl": "The same two speakers continuing through this "
                 "chapter's entire run of ten discourses."},
    ],
    marginalia=[
        ("Full treatment, restored", [
            "eight stubs, bracketed",
            "by two full discourses &mdash;",
            "9.52, and this",
        ]),
        ("A title reused, elsewhere", [
            "the same words as",
            "AN 9.31 &mdash;",
            "name shared, not content",
        ]),
        ("A run of five pairs, closed", [
            "safe, deathless, fearless,",
            "tranquil, cessation &mdash;",
            "all five, complete",
        ]),
        ("Cross-references", [
            "AN 9.31 &middot; the same title, elsewhere in this nipāta",
            "AN 9.52 &middot; the matching full treatment that opened "
            "this run",
            "AN 9.62 &middot; next, closing this chapter differently",
        ]),
    ],
    further=[
        '<a href="%s/an9.61/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.60.html">AN 9.60 &middot; Cessation</a> &mdash; previous.',
        '<a href="an-9.62.html">AN 9.62 &middot; Impossible</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.62 — Abhabbasutta — closes ch.6 Khemavagga
# --------------------------------------------------------------------------- #
page(
    62, "Abhabba", "Impossible",
    vagga=VAGGA_6,
    meta_title="AN 9.62 — Impossible | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Impossible, closing this chapter with a nine-item defilement "
        "list drawn from the first half of the project's standard "
        "seventeen-item list. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two mirror-image statements — impossible without "
                 "giving up, possible after giving up — naming the same "
                 "nine defilements"),
        ("Length", "~1 minute to read"),
        ("A break from this chapter's template", "Unlike every "
         "discourse since AN 9.52, this one is not an Udāyī-to-Ānanda "
         "dialogue and does not use the qualified-versus-definitive "
         "nine-stage grid at all"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "straightforward, notable chiefly for the list it "
                       "shares with this project's largest peyyāla "
                       "closings"),
    ],
    why=(
        "Without giving up nine things &mdash; greed, hate, delusion, "
        "anger, acrimony, disdain, contempt, jealousy, and stinginess "
        "&mdash; perfection cannot be realized; giving them up, it can, "
        "closing this chapter with a return to plain doctrinal "
        "statement after ten discourses of the same recurring template."),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up nine defilements &mdash; greed, hate, "
            "delusion, anger, acrimony, disdain, contempt, jealousy, "
            "and stinginess &mdash; a mendicant cannot realize "
            "perfection; giving up these same nine, they can."]),
        ("A structural break, closing the chapter", [
            "After ten discourses running the Udāyī-to-Ānanda template "
            "&mdash; nine of them defining terms through the nine "
            "progressive attainments &mdash; this discourse abruptly "
            "returns to the Buddha's own plain voice, addressing the "
            "mendicants directly with no dialogue frame and no reference "
            "to the nine attainments at all."]),
        ("The first nine of this project's standard seventeen-item list", [
            "Readers of this project will recognize this list "
            "immediately: greed, hate, and delusion, followed by anger, "
            "acrimony, disdain, contempt, jealousy, and stinginess, are "
            "exactly the first nine items of the same seventeen-item "
            "defilement list (greed plus sixteen more) that has closed "
            "every nipāta's Rāgapeyyāla so far in this project &mdash; "
            "AN 3.183-352, AN 4.304-783, AN 6.170-649, AN 7.645-1124, "
            "and AN 8.148-627. Here, though, only the first nine are "
            "named, stopping before deceitfulness, deviousness, "
            "obstinacy, aggression, conceit, arrogance, vanity, and "
            "negligence."]),
        ("Two mirror statements, one list", [
            "The discourse's structure is simple and symmetrical: the "
            "same nine items are named twice, first as an obstacle "
            "(&lsquo;without giving up&rsquo;) and then as a condition "
            "met (&lsquo;after giving up&rsquo;), closing "
            "<em>Khemavagga</em> on a note of plain ethical urgency "
            "rather than another round of the chapter's meditative "
            "vocabulary game."]),
    ],
    terms=[
        ("abhabbo arahattaṁ sacchikātuṁ",
         "&ldquo;impossible to realize perfection&rdquo; &mdash; this "
         "discourse's own title phrase, naming what remains out of "
         "reach without giving up the nine items."),
        ("rāgaṁ, dosaṁ, mohaṁ",
         "&ldquo;greed, hate, delusion&rdquo; &mdash; the first three "
         "of this discourse's nine, the same three roots met throughout "
         "this nipāta."),
        ("kodhaṁ, upanāhaṁ, makkhaṁ, paḷāsaṁ, issaṁ, macchariyaṁ",
         "&ldquo;anger, acrimony, disdain, contempt, jealousy, and "
         "stinginess&rdquo; &mdash; the remaining six, exactly matching "
         "the first six items of the standard seventeen-item list that "
         "closes this project's largest peyyāla pages."),
        ("bhabbo arahattaṁ sacchikātuṁ",
         "&ldquo;possible to realize perfection&rdquo; &mdash; the "
         "discourse's mirror-image second statement, naming the same "
         "nine items as an obstacle removed."),
        ("khemavaggo",
         "&ldquo;Khemavagga&rdquo; &mdash; the chapter this discourse "
         "closes; the source's own colophon here numbers it "
         "&lsquo;paṭhamo&rsquo; (&ldquo;first&rdquo;), apparently "
         "restarting the count for the Second Fifty rather than "
         "continuing the running 1&ndash;10 numbering used in each "
         "discourse's own header."),
    ],
    text_intro=(
        "The discourse in full: two mirror-image statements naming the "
        "same nine defilements. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Impossible without giving up nine things"),
        ("p", "&sect;1", "an9.62:1.1-1.4"),
        ("h3", "Possible after giving them up"),
        ("p", "&sect;2", "an9.62:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse's form differ from every other "
              "discourse in this chapter since AN 9.52?",
         "opts": [
             "It is even more minimal than the eight stubs",
             "It breaks from the Udāyī-to-Ānanda dialogue and the nine-"
             "stage qualified-versus-definitive grid entirely",
             "It repeats AN 9.52 word for word",
             "It introduces a tenth term-pair"],
         "correct": 1,
         "expl": "A return to the Buddha's own plain voice, with no "
                 "dialogue frame."},
        {"q": "What nine items does this discourse name as obstacles to "
              "perfection?",
         "opts": [
             "The five hindrances plus four more",
             "Greed, hate, delusion, anger, acrimony, disdain, "
             "contempt, jealousy, and stinginess",
             "The nine progressive attainments themselves",
             "Nine kinds of wrong speech"],
         "correct": 1,
         "expl": "The same three roots plus six further defilements "
                 "familiar from elsewhere in this nipāta."},
        {"q": "How does this list relate to the standard seventeen-item "
              "list that closes this project's largest peyyāla pages?",
         "opts": [
             "It is entirely unrelated",
             "It matches exactly the first nine items of that same "
             "list (greed plus the first eight of sixteen further "
             "defilements)",
             "It reverses the order of that list completely",
             "It doubles that list's length"],
         "correct": 1,
         "expl": "A partial reuse, stopping before deceitfulness, "
                 "deviousness, and the remaining eight items."},
        {"q": "What structure do the discourse's two statements form?",
         "opts": [
             "Two unrelated teachings",
             "Mirror images: the same nine items named first as an "
             "obstacle, then as a condition removed",
             "A question and an unrelated answer",
             "A narrative followed by a simile"],
         "correct": 1,
         "expl": "Simple symmetry, closing the chapter with plain "
                 "ethical urgency."},
        {"q": "What curiosity does the source's own closing colophon "
              "show, according to the guide?",
         "opts": [
             "No colophon exists for this discourse",
             "It numbers the chapter &lsquo;paṭhamo&rsquo; "
             "(&ldquo;first&rdquo;), apparently restarting the count for "
             "the Second Fifty, unlike each discourse's own header using "
             "continuous 1&ndash;10 numbering",
             "It claims this is the final chapter of the whole nipāta",
             "It contradicts the discourse's own content"],
         "correct": 1,
         "expl": "An honestly noted inconsistency, not smoothed over."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal statement, closing this chapter "
                 "without narrative frame."},
    ],
    marginalia=[
        ("A template broken", [
            "no dialogue now &mdash;",
            "the Buddha speaks plainly,",
            "closing the chapter",
        ]),
        ("Nine of seventeen", [
            "greed, hate, delusion,",
            "then six more &mdash; the first half",
            "of a familiar list",
        ]),
        ("Two statements, mirrored", [
            "&ldquo;without, impossible&rdquo; &mdash;",
            "&ldquo;having given up, possible&rdquo; &mdash;",
            "the same nine, reversed",
        ]),
        ("Cross-references", [
            "AN 3.183-352, AN 4.304-783, AN 6.170-649, AN 7.645-1124, "
            "AN 8.148-627 &middot; the full seventeen-item list this "
            "discourse's nine partially match",
            "AN 9.61 &middot; previous",
        ]),
    ],
    further=[
        '<a href="%s/an9.62/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.61.html">AN 9.61 &middot; Progressive Cessation</a> &mdash; previous.',
    ],
)


# --------------------------------------------------------------------------- #
# ch.7 — Satipatthanavagga (AN 9.63-72). Ten discourses sharing one clean
# template: a different well-known set of five obstacles each time, always
# answered by the same remedy, the four kinds of mindfulness meditation.
# This chapter's own content is what AN 9.74-81 and AN 9.84-91 later point
# back to with "tell in full as in the chapter on mindfulness meditation."
# --------------------------------------------------------------------------- #
VAGGA_7 = "<em>Satipatthanavagga</em> &mdash; the seventh chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.63 — Sekhasutta — the template-setter for this whole chapter
# --------------------------------------------------------------------------- #
page(
    63, "Sekha", "Weaknesses in Training and Mindfulness Meditation",
    vagga=VAGGA_7,
    meta_title=("AN 9.63 — Weaknesses in Training and Mindfulness "
                "Meditation | Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the discourse opening this chapter's template — five "
        "weaknesses in training answered by the four kinds of "
        "mindfulness meditation, a pairing repeated with a new "
        "obstacle-list nine more times. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five weaknesses named, then the four satipaṭṭhāna "
                 "given in full as the remedy"),
        ("Length", "~1 minute to read"),
        ("This chapter's template-setter", "Nine more discourses follow, "
         "each swapping in a different well-known five-item list while "
         "keeping the same remedy"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and clean, the clearest chapter structure "
                       "in this nipāta"),
    ],
    why=(
        "The five weaknesses that undermine training &mdash; killing, "
        "stealing, sexual misconduct, lying, and intoxicants, the five "
        "precepts broken &mdash; are given up by developing the four "
        "kinds of mindfulness meditation: observing the body, feelings, "
        "the mind, and principles, each keen, aware, mindful, and rid "
        "of covetousness and displeasure for the world."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five weaknesses in training &mdash; "
            "killing, stealing, sexual misconduct, lying, and "
            "intoxicants &mdash; a mendicant should develop the four "
            "kinds of mindfulness meditation: observing the body, "
            "feelings, the mind, and principles."]),
        ("Five broken precepts, named as weaknesses", [
            "The five items named here are simply the five lay precepts "
            "stated as their own violation &mdash; not a new list, but "
            "a familiar one reframed as &lsquo;sekha,&rsquo; weaknesses "
            "that undermine a trainee's own progress rather than as "
            "external rules."]),
        ("The four satipaṭṭhāna, spelled out in full", [
            "Unlike most of the discourses that follow it in this "
            "chapter, this one gives the complete four-part formula: "
            "observing the body, feelings, the mind, and principles, "
            "each pursued keenly, with awareness and mindfulness, rid "
            "of covetousness and displeasure for the world &mdash; the "
            "standard four foundations of mindfulness in their full "
            "canonical wording."]),
        ("A template this whole chapter will repeat", [
            "This exact pairing &mdash; a named five-item list, "
            "followed by the instruction to develop the four kinds of "
            "mindfulness meditation to give it up &mdash; is the "
            "template AN 9.64 through AN 9.72 all reuse, substituting a "
            "different well-known obstacle-list each time. This "
            "chapter's own content is also what two later chapters, AN "
            "9.74-81 and AN 9.84-91, will point back to rather than "
            "repeat."]),
    ],
    terms=[
        ("sekhā pañca dhammā",
         "&ldquo;five weaknesses when you're training&rdquo; &mdash; "
         "this discourse's own framing of the five precepts as "
         "obstacles to a trainee's progress."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy this entire chapter applies to ten "
         "different obstacle-lists."),
        ("kāye kāyānupassī",
         "&ldquo;observing an aspect of the body&rdquo; &mdash; the "
         "first of the four foundations, given here in its full "
         "canonical wording."),
        ("ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṁ",
         "&ldquo;keen, aware, and mindful, rid of covetousness and "
         "displeasure for the world&rdquo; &mdash; the shared refrain "
         "closing each of the four foundations."),
        ("dhammesu dhammānupassī",
         "&ldquo;observing an aspect of principles&rdquo; &mdash; the "
         "fourth and final foundation, closing the formula."),
    ],
    text_intro=(
        "The discourse in full: five weaknesses, and the four kinds of "
        "mindfulness meditation given as their remedy. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five weaknesses in training"),
        ("p", "&sect;1", "an9.63:1.1-1.4"),
        ("h3", "Four kinds of mindfulness meditation"),
        ("p", "&sect;2", "an9.63:2.1-2.7"),
    ],
    quiz=[
        {"q": "What five weaknesses does this discourse name?",
         "opts": [
             "The five hindrances",
             "Killing, stealing, sexual misconduct, lying, and "
             "intoxicants — the five precepts stated as their own "
             "violation",
             "The five aggregates",
             "Five kinds of wrong view"],
         "correct": 1,
         "expl": "A familiar list, reframed as obstacles to a trainee's "
                 "own progress."},
        {"q": "What remedy does this discourse prescribe?",
         "opts": [
             "The four right efforts",
             "The four kinds of mindfulness meditation — body, "
             "feelings, mind, and principles",
             "The four noble truths",
             "The four bases of psychic power"],
         "correct": 1,
         "expl": "The shared remedy this whole chapter applies "
                 "repeatedly to different obstacle-lists."},
        {"q": "How does this discourse's treatment of the four "
              "foundations compare to most later discourses in this "
              "chapter?",
         "opts": [
             "Identical brevity throughout",
             "This one gives the complete formula in full; most later "
             "discourses elide it after the pattern is established",
             "This one omits the formula entirely",
             "Later discourses give a longer formula"],
         "correct": 1,
         "expl": "The template-setter, spelling out what later "
                 "discourses can then abbreviate."},
        {"q": "According to the guide, what do two later chapters point "
              "back to rather than repeat?",
         "opts": [
             "AN 9.32's nine attainments",
             "This chapter's own content, at AN 9.74-81 and AN 9.84-91",
             "AN 9.42's confinement discourse",
             "Nothing; no later chapter references this one"],
         "correct": 1,
         "expl": "A cross-chapter reference this project will meet "
                 "again later in AN 9."},
        {"q": "What is the shared refrain closing each of the four "
              "foundations?",
         "opts": [
             "A verse of praise",
             "&ldquo;Keen, aware, and mindful, rid of covetousness and "
             "displeasure for the world&rdquo;",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "The standard canonical closing formula for each "
                 "foundation."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, opening this chapter "
                 "without narrative frame."},
    ],
    marginalia=[
        ("Five precepts, reframed", [
            "not rules imposed, but",
            "weaknesses that undermine",
            "a trainee's own progress",
        ]),
        ("Four foundations, in full", [
            "body, feelings, mind,",
            "principles &mdash; keen, aware,",
            "mindful, free of craving",
        ]),
        ("A template, ten times over", [
            "a new five-item list,",
            "the same remedy each time &mdash;",
            "this chapter's own shape",
        ]),
        ("Cross-references", [
            "AN 9.62 &middot; previous chapter's closing page",
            "AN 9.74&ndash;81, AN 9.84&ndash;91 &middot; later chapters "
            "that point back to this one rather than repeat it",
            "AN 9.64 &middot; next, Hindrances",
        ]),
    ],
    further=[
        '<a href="%s/an9.63/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.62.html">AN 9.62 &middot; Impossible</a> &mdash; previous.',
        '<a href="an-9.64.html">AN 9.64 &middot; Hindrances</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.64 — Nīvaraṇasutta
# --------------------------------------------------------------------------- #
page(
    64, "Nīvaraṇa", "Hindrances",
    vagga=VAGGA_7,
    meta_title="AN 9.64 — Hindrances | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Hindrances, applying this chapter's template to the classic "
        "five hindrances that block meditative absorption. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same template as AN 9.63, given here in full a "
                 "second time"),
        ("Length", "~1 minute to read"),
        ("The most meditation-specific list in this run", "Where AN "
         "9.63's weaknesses concern ethical conduct broadly, the five "
         "hindrances are the standard obstacles named specifically "
         "within meditation practice itself"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, and highly familiar territory for anyone "
                       "who has read this project's earlier discourses"),
    ],
    why=(
        "The five hindrances &mdash; sensual desire, ill will, dullness "
        "and drowsiness, restlessness and remorse, and doubt &mdash; "
        "are given up the same way as AN 9.63's weaknesses: by "
        "developing the four kinds of mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five hindrances &mdash; sensual desire, ill "
            "will, dullness and drowsiness, restlessness and remorse, "
            "and doubt &mdash; a mendicant should develop the four "
            "kinds of mindfulness meditation, the same remedy given at "
            "AN 9.63."]),
        ("The most familiar list in this project so far", [
            "Of all the obstacle-lists this chapter cycles through, the "
            "five hindrances are the most frequently named elsewhere in "
            "the canon and in this project itself &mdash; already met, "
            "for instance, giving way before the four absorptions at AN "
            "9.40's wild elephant simile."]),
        ("A second full example, before compression begins", [
            "This discourse still gives the complete four-foundation "
            "formula in full, matching AN 9.63 rather than eliding it "
            "&mdash; the last discourse in this chapter to do so before "
            "AN 9.65 through AN 9.70 compress the remedy down to a bare "
            "ellipsis."]),
        ("Meditation obstacles, met with a meditative remedy", [
            "Unlike AN 9.63's ethically framed weaknesses, this "
            "discourse's obstacle-list belongs squarely to meditation "
            "practice itself &mdash; a tighter, more direct fit between "
            "problem and remedy than some of the other pairings this "
            "chapter will offer."]),
    ],
    terms=[
        ("pañca nīvaraṇā",
         "&ldquo;the five hindrances&rdquo; &mdash; this discourse's "
         "own title term, among the most familiar obstacle-lists in the "
         "entire canon."),
        ("kāmacchando, byāpādo",
         "&ldquo;sensual desire, ill will&rdquo; &mdash; the first two "
         "hindrances, already met giving way before absorption "
         "elsewhere in this project."),
        ("thinamiddhaṁ, uddhaccakukkuccaṁ, vicikicchā",
         "&ldquo;dullness and drowsiness, restlessness and remorse, "
         "and doubt&rdquo; &mdash; the remaining three hindrances, "
         "closing the standard list."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the same remedy as AN 9.63, given here in full for "
         "the last time before this chapter compresses it."),
        ("vineyya loke abhijjhādomanassaṁ",
         "&ldquo;rid of covetousness and displeasure for the "
         "world&rdquo; &mdash; the shared closing phrase for each of "
         "the four foundations."),
    ],
    text_intro=(
        "The discourse in full: the five hindrances, and the four "
        "kinds of mindfulness meditation given as their remedy. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five hindrances"),
        ("p", "&sect;1", "an9.64:1.1-1.4"),
        ("h3", "Four kinds of mindfulness meditation"),
        ("p", "&sect;2", "an9.64:2.1-2.7"),
    ],
    quiz=[
        {"q": "What five hindrances does this discourse name?",
         "opts": [
             "The five precepts",
             "Sensual desire, ill will, dullness and drowsiness, "
             "restlessness and remorse, and doubt",
             "The five aggregates",
             "The five higher fetters"],
         "correct": 1,
         "expl": "One of the most familiar obstacle-lists in the entire "
                 "canon."},
        {"q": "How does this discourse's obstacle-list differ in kind "
              "from AN 9.63's?",
         "opts": [
             "No difference at all",
             "AN 9.63's weaknesses concern ethical conduct broadly; "
             "this discourse's hindrances belong specifically to "
             "meditation practice",
             "This list is entirely unrelated to meditation",
             "This list is longer than AN 9.63's"],
         "correct": 1,
         "expl": "A tighter, more direct fit between the obstacle and "
                 "its meditative remedy."},
        {"q": "How does this discourse's treatment of the four "
              "foundations compare to AN 9.63's?",
         "opts": [
             "Already compressed to an ellipsis",
             "Given in full, matching AN 9.63 — the last discourse in "
             "this chapter to do so before compression begins",
             "Doubled in length",
             "Entirely different in structure"],
         "correct": 1,
         "expl": "The second and final full example before AN 9.65 "
                 "onward elide the remedy."},
        {"q": "Where has this project already met the five hindrances "
              "giving way before absorption?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.40's wild elephant simile",
             "Only in a completely different nipāta",
             "AN 9.1's opening discourse"],
         "correct": 1,
         "expl": "A familiar list this project has met before this "
                 "chapter."},
        {"q": "What remedy does this discourse prescribe, matching AN "
              "9.63?",
         "opts": [
             "The four right efforts",
             "The four kinds of mindfulness meditation",
             "The four noble truths",
             "The four bases of psychic power"],
         "correct": 1,
         "expl": "The shared remedy running through this entire "
                 "chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching AN 9.63 "
                 "immediately before it."},
    ],
    marginalia=[
        ("The most familiar five", [
            "desire, ill will, dullness,",
            "restlessness, doubt &mdash;",
            "met before, in this book",
        ]),
        ("A second full example", [
            "the last time this chapter",
            "spells the remedy out &mdash;",
            "compression starts next",
        ]),
        ("Obstacle meets remedy", [
            "meditation's own",
            "hindrances, met here by",
            "meditation itself",
        ]),
        ("Cross-references", [
            "AN 9.40 &middot; an earlier meeting with these same five "
            "hindrances",
            "AN 9.63 &middot; previous, this chapter's template-setter",
            "AN 9.65 &middot; next, Kinds of Sensual Stimulation",
        ]),
    ],
    further=[
        '<a href="%s/an9.64/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.63.html">AN 9.63 &middot; Weaknesses in Training and Mindfulness '
        "Meditation</a> &mdash; previous.",
        '<a href="an-9.65.html">AN 9.65 &middot; Kinds of Sensual Stimulation</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.65 — Kāmaguṇasutta — begins this chapter's compressed form
# --------------------------------------------------------------------------- #
page(
    65, "Kāmaguṇa", "Kinds of Sensual Stimulation",
    vagga=VAGGA_7,
    meta_title="AN 9.65 — Kinds of Sensual Stimulation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Kinds of Sensual Stimulation, the first discourse in this "
        "chapter to compress the four-foundation remedy to an "
        "ellipsis, applying the template to the standard five sense "
        "pleasures. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five sense pleasures named in full, then the four-"
                 "foundation remedy compressed to a single ellipsis"),
        ("Length", "~30 seconds to read"),
        ("Compression begins here", "This is the first discourse in "
         "this chapter where the mindfulness-meditation formula is no "
         "longer spelled out, relying on AN 9.63 and AN 9.64 instead"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, and a familiar list from elsewhere in "
                       "this nipāta"),
    ],
    why=(
        "The five kinds of sensual stimulation &mdash; likable, "
        "desirable sights, sounds, smells, tastes, and touches &mdash; "
        "are given up, like every obstacle in this chapter, by "
        "developing the four kinds of mindfulness meditation, though "
        "this discourse no longer spells the remedy out."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five kinds of sensual stimulation &mdash; "
            "pleasant sights, sounds, smells, tastes, and touches "
            "&mdash; a mendicant should develop the four kinds of "
            "mindfulness meditation, the same remedy given in full at "
            "AN 9.63 and AN 9.64."]),
        ("A term already familiar from this nipāta", [
            "The five kāmaguṇā named here are the identical five sense "
            "pleasures already met defining &lsquo;the world&rsquo; at "
            "AN 9.38 and &lsquo;confinement&rsquo; at AN 9.42 &mdash; "
            "the same content, applied here to a third distinct "
            "framing within this single nipāta."]),
        ("Where the chapter's compression begins", [
            "This is the first discourse in this chapter where the "
            "four-foundation formula is reduced to a bare ellipsis "
            "rather than spelled out. Having established the pattern "
            "twice in full at AN 9.63 and AN 9.64, the source now "
            "trusts the reader to supply it, a compression this chapter "
            "maintains through AN 9.70."]),
        ("A remedy that fits its obstacle directly", [
            "As with AN 9.64's hindrances, the pairing here is "
            "especially apt: the four foundations' own closing phrase, "
            "&lsquo;rid of covetousness and displeasure for the "
            "world,&rsquo; directly answers what sensory pleasure "
            "produces &mdash; craving for exactly the kind of pleasant "
            "stimulation this discourse names."]),
    ],
    terms=[
        ("pañca kāmaguṇā",
         "&ldquo;the five kinds of sensual stimulation&rdquo; &mdash; "
         "this discourse's own title term, already met at AN 9.38 and "
         "AN 9.42 under different framings."),
        ("cakkhuviññeyyā rūpā iṭṭhā kantā manāpā piyarūpā "
         "kāmūpasaṁhitā rajanīyā",
         "&ldquo;sights known by the eye, which are likable, desirable, "
         "agreeable, pleasant, sensual, and arousing&rdquo; &mdash; the "
         "first sense pleasure, given in its full standard description."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; marking where this chapter's four-foundation formula "
         "is first compressed after being spelled out twice in full."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, given by name here but not in full "
         "detail."),
        ("vineyya loke abhijjhādomanassaṁ",
         "&ldquo;rid of covetousness and displeasure for the "
         "world&rdquo; &mdash; the closing phrase from AN 9.63-64's "
         "full formula, directly answering this discourse's own "
         "obstacle."),
    ],
    text_intro=(
        "The discourse in full, as it survives: five sense pleasures "
        "given in full, then the remedy compressed to an ellipsis. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five kinds of sensual stimulation"),
        ("p", "&sect;1", "an9.65:1.1-1.8"),
        ("h3", "The remedy, compressed"),
        ("p", "&sect;2", "an9.65:2.1-2.1"),
    ],
    quiz=[
        {"q": "What five kinds of sensual stimulation does this "
              "discourse name?",
         "opts": [
             "The five hindrances",
             "Pleasant sights, sounds, smells, tastes, and touches",
             "The five aggregates",
             "Five precepts"],
         "correct": 1,
         "expl": "The standard five kāmaguṇā, already met defining "
                 "&lsquo;the world&rsquo; and &lsquo;confinement&rsquo; "
                 "earlier in this nipāta."},
        {"q": "Where has this exact five-item list already appeared "
              "earlier in AN 9?",
         "opts": [
             "Nowhere before this discourse",
             "Defining &lsquo;the world&rsquo; at AN 9.38 and "
             "&lsquo;confinement&rsquo; at AN 9.42",
             "Only in a completely unrelated nipāta",
             "Only in AN 9.63"],
         "correct": 1,
         "expl": "The same content under a third distinct framing "
                 "within this single nipāta."},
        {"q": "What happens to the four-foundation formula in this "
              "discourse, unlike AN 9.63 and AN 9.64?",
         "opts": [
             "It is given even more fully than before",
             "It is compressed to a bare ellipsis for the first time in "
             "this chapter",
             "It is replaced with a different remedy entirely",
             "It is omitted with no mention at all"],
         "correct": 1,
         "expl": "The pattern established, the source now trusts the "
                 "reader to supply the rest."},
        {"q": "According to the guide, why is the remedy especially apt "
              "here?",
         "opts": [
             "It isn't apt at all",
             "The formula's closing phrase, &lsquo;rid of covetousness "
             "and displeasure for the world,&rsquo; directly answers "
             "craving for pleasant sensory stimulation",
             "The remedy has nothing to do with the obstacle",
             "This discourse uses an entirely different remedy"],
         "correct": 1,
         "expl": "A tight fit between this specific obstacle and the "
                 "shared four-foundation cure."},
        {"q": "How long does this chapter's compressed form continue "
              "after this discourse?",
         "opts": [
             "It ends immediately",
             "Through AN 9.70, before AN 9.71 and AN 9.72 restore "
             "fuller detail",
             "For the rest of the entire nipāta",
             "It cannot be determined"],
         "correct": 1,
         "expl": "A sustained compression covering most of this "
                 "chapter's remaining discourses."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching this whole "
                 "chapter's method."},
    ],
    marginalia=[
        ("A familiar five, again", [
            "sights, sounds, smells, tastes,",
            "touches &mdash; the world's own",
            "pleasures, third framing",
        ]),
        ("Compression begins", [
            "the formula, spelled",
            "out twice, now trusted",
            "to memory instead",
        ]),
        ("A tight fit", [
            "craving for pleasure,",
            "met by freedom from",
            "covetousness itself",
        ]),
        ("Cross-references", [
            "AN 9.38, AN 9.42 &middot; the same five sense pleasures "
            "under two earlier framings",
            "AN 9.64 &middot; previous",
            "AN 9.66 &middot; next, Grasping Aggregates",
        ]),
    ],
    further=[
        '<a href="%s/an9.65/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.64.html">AN 9.64 &middot; Hindrances</a> &mdash; previous.',
        '<a href="an-9.66.html">AN 9.66 &middot; Grasping Aggregates</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.66 — Upādānakkhandhasutta
# --------------------------------------------------------------------------- #
page(
    66, "Upādānakkhandha", "Grasping Aggregates",
    vagga=VAGGA_7,
    meta_title="AN 9.66 — Grasping Aggregates | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Grasping Aggregates, applying this chapter's compressed "
        "template to the five aggregates subject to clinging — form, "
        "feeling, perception, choices, and consciousness. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five aggregates named in full, then the remedy "
                 "compressed to an ellipsis, matching AN 9.65"),
        ("Length", "~30 seconds to read"),
        ("The most foundational list in this chapter", "The five "
         "grasping aggregates are among the most basic analytical "
         "categories in the entire tradition, describing the whole of "
         "clung-to experience"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief in text, but naming a genuinely "
                       "foundational category"),
    ],
    why=(
        "The five grasping aggregates &mdash; form, feeling, "
        "perception, choices, and consciousness &mdash; are given up "
        "the same way as every obstacle in this chapter, by developing "
        "the four kinds of mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five grasping aggregates &mdash; form, "
            "feeling, perception, choices, and consciousness &mdash; a "
            "mendicant should develop the four kinds of mindfulness "
            "meditation, the same remedy given throughout this chapter."]),
        ("The most basic analytical category in the tradition", [
            "Where AN 9.63's weaknesses and AN 9.64's hindrances name "
            "specific obstacles to overcome, the five aggregates are "
            "something more fundamental still: the standard "
            "five-fold analysis of what a person actually is, the raw "
            "material any clinging whatsoever must cling to."]),
        ("Naming what is grasped, not merely what obstructs", [
            "This shift in kind is worth noticing: most of this "
            "chapter's other lists name specific unwholesome states "
            "&mdash; hindrances, fetters, stinginess &mdash; but the "
            "aggregates themselves are not inherently unwholesome. "
            "What must be given up is the grasping (upādāna) itself, "
            "not form, feeling, perception, choices, or consciousness "
            "as such."]),
        ("Continuing this chapter's compressed form", [
            "As at AN 9.65, the four-foundation remedy is here reduced "
            "to a bare ellipsis, relying on AN 9.63 and AN 9.64's full "
            "treatment to supply the missing detail."]),
    ],
    terms=[
        ("pañcupādānakkhandhā",
         "&ldquo;the five grasping aggregates&rdquo; &mdash; this "
         "discourse's own title term, one of the most foundational "
         "analytical categories in the tradition."),
        ("rūpupādānakkhandho, vedanupādānakkhandho",
         "&ldquo;the grasping aggregate of form, of feeling&rdquo; "
         "&mdash; the first two of the five, each named as an "
         "aggregate that can be clung to."),
        ("saññā, saṅkhārā, viññāṇa",
         "&ldquo;perception, choices, consciousness&rdquo; &mdash; the "
         "remaining three aggregates, closing the standard five-fold "
         "analysis."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; marking where the four-foundation formula is "
         "compressed, as at AN 9.65."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, named but not spelled out in this "
         "discourse."),
    ],
    text_intro=(
        "The discourse in full, as it survives: five grasping "
        "aggregates given in full, then the remedy compressed to an "
        "ellipsis. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five grasping aggregates"),
        ("p", "&sect;1", "an9.66:1.1-1.4"),
        ("h3", "The remedy, compressed"),
        ("p", "&sect;2", "an9.66:2.1-2.1"),
    ],
    quiz=[
        {"q": "What five grasping aggregates does this discourse name?",
         "opts": [
             "The five hindrances",
             "Form, feeling, perception, choices, and consciousness",
             "Five kinds of stinginess",
             "The five precepts"],
         "correct": 1,
         "expl": "The most foundational analytical category in the "
                 "tradition, describing the whole of clung-to "
                 "experience."},
        {"q": "How does this list differ in kind from most of this "
              "chapter's other obstacle-lists?",
         "opts": [
             "No difference at all",
             "The aggregates themselves are not inherently unwholesome "
             "— what must be given up is the grasping, not the "
             "aggregates as such",
             "The aggregates are a kind of precept",
             "This list has nothing to do with clinging"],
         "correct": 1,
         "expl": "A shift from naming specific unwholesome states to "
                 "naming the raw material of experience itself."},
        {"q": "How is the four-foundation remedy presented in this "
              "discourse?",
         "opts": [
             "Given in complete detail",
             "Compressed to a bare ellipsis, as at AN 9.65",
             "Replaced with a different remedy",
             "Omitted with no mention at all"],
         "correct": 1,
         "expl": "Continuing the compressed form begun at AN 9.65."},
        {"q": "What must be given up, according to the guide's "
              "reading of this discourse?",
         "opts": [
             "The aggregates themselves, entirely",
             "The grasping (upādāna) attached to the aggregates, not "
             "the aggregates as such",
             "Only the aggregate of form",
             "Nothing needs to be given up"],
         "correct": 1,
         "expl": "A precise distinction between the aggregates and the "
                 "clinging that makes them a problem."},
        {"q": "What remedy does this discourse prescribe, matching this "
              "whole chapter?",
         "opts": [
             "The four right efforts",
             "The four kinds of mindfulness meditation",
             "The four noble truths",
             "The six higher knowledges"],
         "correct": 1,
         "expl": "The shared remedy running through all ten discourses "
                 "in this chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching this whole "
                 "chapter's method."},
    ],
    marginalia=[
        ("The raw material itself", [
            "form, feeling, perception,",
            "choices, consciousness &mdash;",
            "not evil, but clung to",
        ]),
        ("Grasping, not the grasped", [
            "the aggregates aren't",
            "the problem &mdash; clinging",
            "to them is",
        ]),
        ("The same compressed form", [
            "one line, an ellipsis &mdash;",
            "the remedy trusted",
            "to memory again",
        ]),
        ("Cross-references", [
            "AN 9.65 &middot; previous",
            "AN 9.67 &middot; next, Lower Fetters",
        ]),
    ],
    further=[
        '<a href="%s/an9.66/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.65.html">AN 9.65 &middot; Kinds of Sensual Stimulation</a> &mdash; '
        "previous.",
        '<a href="an-9.67.html">AN 9.67 &middot; Lower Fetters</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.67 — Orambhāgiyasutta
# --------------------------------------------------------------------------- #
page(
    67, "Orambhāgiya", "Lower Fetters",
    vagga=VAGGA_7,
    meta_title="AN 9.67 — Lower Fetters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Lower Fetters, applying this chapter's compressed template to "
        "the five fetters ended by non-return, the same milestone met "
        "repeatedly elsewhere in this nipāta. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five fetters named in full, then the remedy "
                 "compressed to an ellipsis, matching AN 9.65-66"),
        ("Length", "~30 seconds to read"),
        ("The fetters this whole nipāta has tracked", "Ending these "
         "same five fetters is what produces a non-returner throughout "
         "this project, from AN 9.12's detailed classification onward"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief in text, naming a milestone this project "
                       "has returned to repeatedly"),
    ],
    why=(
        "The five lower fetters &mdash; substantialist view, doubt, "
        "misapprehension of precepts and observances, sensual desire, "
        "and ill will &mdash; are given up the same way as every "
        "obstacle in this chapter, by developing the four kinds of "
        "mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five lower fetters &mdash; substantialist "
            "view, doubt, misapprehension of precepts and observances, "
            "sensual desire, and ill will &mdash; a mendicant should "
            "develop the four kinds of mindfulness meditation, the "
            "same remedy given throughout this chapter."]),
        ("The milestone this whole nipāta measures by", [
            "Ending these exact five fetters is what this project has "
            "repeatedly identified as producing non-return: AN 9.12's "
            "detailed nine-fold classification graded non-returners "
            "precisely by how they attain final extinguishment after "
            "these same five fetters end, and AN 9.22's wild-colt "
            "simile used the identical ending as its middle grade of "
            "attainment."]),
        ("Naming the fetters plainly, without the classification's "
         "detail", [
            "Unlike AN 9.12's elaborate five-way subdivision of what "
            "happens after these fetters end, this discourse simply "
            "names the five fetters themselves and pairs them with the "
            "chapter's standard remedy &mdash; a plainer, more direct "
            "treatment of territory this nipāta has already explored "
            "in much greater depth."]),
        ("Continuing this chapter's compressed form", [
            "As at AN 9.65 and AN 9.66, the four-foundation formula is "
            "reduced here to a bare ellipsis, relying on AN 9.63 and AN "
            "9.64's earlier full treatment."]),
    ],
    terms=[
        ("pañcorambhāgiyāni saṁyojanāni",
         "&ldquo;the five lower fetters&rdquo; &mdash; this "
         "discourse's own title term, the same milestone marking "
         "non-return throughout this nipāta."),
        ("sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso",
         "&ldquo;substantialist view, doubt, misapprehension of "
         "precepts and observances&rdquo; &mdash; the first three "
         "fetters, shared with the standard four factors of stream-"
         "entry's own obstacles."),
        ("kāmacchando, byāpādo",
         "&ldquo;sensual desire, ill will&rdquo; &mdash; the remaining "
         "two fetters, the same first two hindrances named at AN 9.64."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; marking where the four-foundation formula is "
         "compressed, as at AN 9.65 and AN 9.66."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, named but not spelled out in this "
         "discourse."),
    ],
    text_intro=(
        "The discourse in full, as it survives: five lower fetters "
        "given in full, then the remedy compressed to an ellipsis. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five lower fetters"),
        ("p", "&sect;1", "an9.67:1.1-1.4"),
        ("h3", "The remedy, compressed"),
        ("p", "&sect;2", "an9.67:2.1-2.1"),
    ],
    quiz=[
        {"q": "What five lower fetters does this discourse name?",
         "opts": [
             "The five hindrances",
             "Substantialist view, doubt, misapprehension of precepts "
             "and observances, sensual desire, and ill will",
             "The five aggregates",
             "Five kinds of stinginess"],
         "correct": 1,
         "expl": "The same milestone this project has tracked "
                 "repeatedly as marking non-return."},
        {"q": "Where has this project already explored the ending of "
              "these same five fetters in greater depth?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.12's detailed nine-fold classification of non-"
             "returners, graded by how they attain final extinguishment",
             "Only in a completely unrelated nipāta",
             "AN 9.1's opening discourse"],
         "correct": 1,
         "expl": "A milestone examined with much finer granularity "
                 "earlier in this nipāta."},
        {"q": "How does this discourse's treatment compare to AN "
              "9.12's?",
         "opts": [
             "Identical in every detail",
             "Plainer and more direct — simply naming the five fetters "
             "and pairing them with the standard remedy, without AN "
             "9.12's elaborate subdivision",
             "This discourse contradicts AN 9.12",
             "This discourse is much longer"],
         "correct": 1,
         "expl": "The same territory, treated with far less "
                 "elaboration here."},
        {"q": "What two fetters does this list share with AN 9.64's "
              "five hindrances?",
         "opts": [
             "Doubt and misapprehension of precepts",
             "Sensual desire and ill will",
             "Substantialist view and doubt",
             "None; the lists share nothing"],
         "correct": 1,
         "expl": "An overlap worth noticing between two different "
                 "standard obstacle-lists."},
        {"q": "How is the four-foundation remedy presented in this "
              "discourse?",
         "opts": [
             "Given in complete detail",
             "Compressed to a bare ellipsis, continuing the pattern "
             "from AN 9.65 and AN 9.66",
             "Replaced with a different remedy",
             "Omitted with no mention at all"],
         "correct": 1,
         "expl": "Continuing this chapter's sustained compression."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching this whole "
                 "chapter's method."},
    ],
    marginalia=[
        ("A milestone, tracked before", [
            "view, doubt, rites clung to,",
            "desire, ill will &mdash; the same",
            "five as AN 9.12",
        ]),
        ("Plainer, this time", [
            "no nine-fold grading now &mdash;",
            "just the five fetters,",
            "named and answered",
        ]),
        ("An overlap noticed", [
            "desire, ill will &mdash;",
            "shared with the hindrances",
            "two discourses back",
        ]),
        ("Cross-references", [
            "AN 9.12 &middot; the same five fetters, explored in far "
            "greater depth",
            "AN 9.66 &middot; previous",
            "AN 9.68 &middot; next, Places of Rebirth",
        ]),
    ],
    further=[
        '<a href="%s/an9.67/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.66.html">AN 9.66 &middot; Grasping Aggregates</a> &mdash; previous.',
        '<a href="an-9.68.html">AN 9.68 &middot; Places of Rebirth</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.68 — Gatisutta
# --------------------------------------------------------------------------- #
page(
    68, "Gati", "Places of Rebirth",
    vagga=VAGGA_7,
    meta_title="AN 9.68 — Places of Rebirth | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Places of Rebirth, applying this chapter's compressed template "
        "to the five destinations of rebirth — the only list in this "
        "chapter naming destinations rather than obstacles. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five destinations named in full, then the remedy "
                 "compressed to an ellipsis, matching AN 9.65-67"),
        ("Length", "~30 seconds to read"),
        ("A different kind of list entirely", "Unlike every other "
         "obstacle-list in this chapter, the five destinations aren't "
         "unwholesome states to abandon but places one might be reborn "
         "— themselves what mindfulness meditation ultimately ends"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief in text, worth noticing how this list "
                       "differs from its neighbors"),
    ],
    why=(
        "The five destinations &mdash; hell, the animal realm, the "
        "ghost realm, humanity, and the gods &mdash; are given up the "
        "same way as every other obstacle in this chapter, by "
        "developing the four kinds of mindfulness meditation, though "
        "here it is rebirth itself, not a mental state, that must be "
        "given up."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five destinations &mdash; hell, the animal "
            "realm, the ghost realm, humanity, and the gods &mdash; a "
            "mendicant should develop the four kinds of mindfulness "
            "meditation, the same remedy given throughout this chapter."]),
        ("Not an obstacle, but a consequence", [
            "Every other list in this chapter names something a "
            "mendicant actively does or experiences &mdash; broken "
            "precepts, hindrances, sense-pleasures, clinging, fetters. "
            "The five destinations are different in kind: they are "
            "where continued rebirth leads, the consequence of not "
            "giving up the other obstacles rather than an obstacle "
            "themselves."]),
        ("Giving up rebirth altogether", [
            "Read this way, this discourse's real claim is more radical "
            "than its neighbors: developing the four foundations "
            "doesn't merely purify conduct or calm the mind, but ends "
            "the entire cycle these five destinations represent "
            "&mdash; a fitting way to describe what the culminating "
            "ninth attainment, the cessation of perception and feeling, "
            "accomplishes when reached in the definitive sense named "
            "throughout ch.5 and ch.6."]),
        ("Continuing this chapter's compressed form", [
            "As at AN 9.65 through AN 9.67, the four-foundation formula "
            "is reduced here to a bare ellipsis, relying on AN 9.63 and "
            "AN 9.64's earlier full treatment."]),
    ],
    terms=[
        ("pañca gatiyo",
         "&ldquo;the five destinations&rdquo; &mdash; this discourse's "
         "own title term, the only list in this chapter naming places "
         "of rebirth rather than obstacles to abandon."),
        ("nirayo, tiracchānayoni, pettivisayo",
         "&ldquo;hell, the animal realm, the ghost realm&rdquo; "
         "&mdash; the three lower destinations, named first."),
        ("manussā, devā",
         "&ldquo;humanity, the gods&rdquo; &mdash; the two higher "
         "destinations, closing the standard fivefold list."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; marking where the four-foundation formula is "
         "compressed, as at AN 9.65 through AN 9.67."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, here ending rebirth itself rather "
         "than a single mental obstacle."),
    ],
    text_intro=(
        "The discourse in full, as it survives: five destinations "
        "given in full, then the remedy compressed to an ellipsis. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five destinations"),
        ("p", "&sect;1", "an9.68:1.1-1.4"),
        ("h3", "The remedy, compressed"),
        ("p", "&sect;2", "an9.68:2.1-2.1"),
    ],
    quiz=[
        {"q": "What five destinations does this discourse name?",
         "opts": [
             "Five monastic ranks",
             "Hell, the animal realm, the ghost realm, humanity, and "
             "the gods",
             "Five kinds of stinginess",
             "The five aggregates"],
         "correct": 1,
         "expl": "The standard fivefold cosmology of rebirth "
                 "destinations."},
        {"q": "How does this list differ in kind from every other "
              "obstacle-list in this chapter?",
         "opts": [
             "No difference at all",
             "It names places one might be reborn, not a mental state "
             "or obstacle one actively holds",
             "It is longer than the other lists",
             "It contradicts the other lists"],
         "correct": 1,
         "expl": "A consequence of continued rebirth, not an obstacle "
                 "in itself."},
        {"q": "According to the guide, what more radical claim does "
              "this discourse make than its neighbors?",
         "opts": [
             "Nothing different; it makes the same claim",
             "That developing the four foundations ends the entire "
             "cycle of rebirth these five destinations represent, not "
             "merely purifying conduct or calming the mind",
             "That rebirth cannot actually be ended",
             "That only humans can practice mindfulness meditation"],
         "correct": 1,
         "expl": "A description fitting what the definitive ninth "
                 "attainment accomplishes elsewhere in this nipāta."},
        {"q": "How is the four-foundation remedy presented in this "
              "discourse?",
         "opts": [
             "Given in complete detail",
             "Compressed to a bare ellipsis, continuing the pattern "
             "from AN 9.65 through AN 9.67",
             "Replaced with a different remedy",
             "Omitted with no mention at all"],
         "correct": 1,
         "expl": "Continuing this chapter's sustained compression."},
        {"q": "What are the three lower destinations named first?",
         "opts": [
             "Humanity, the gods, and Brahmā",
             "Hell, the animal realm, and the ghost realm",
             "The formless realms",
             "Three kinds of heaven"],
         "correct": 1,
         "expl": "The first three of the standard fivefold list, "
                 "followed by humanity and the gods."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching this whole "
                 "chapter's method."},
    ],
    marginalia=[
        ("Not an obstacle, but a fate", [
            "hell, beast, ghost,",
            "human, god &mdash; where rebirth",
            "leads, not what causes it",
        ]),
        ("A more radical claim", [
            "not just calming mind,",
            "but ending the whole cycle",
            "these five represent",
        ]),
        ("The same compressed form", [
            "one line, an ellipsis &mdash;",
            "the remedy, as always,",
            "trusted to memory",
        ]),
        ("Cross-references", [
            "AN 9.67 &middot; previous",
            "AN 9.69 &middot; next, Stinginess",
        ]),
    ],
    further=[
        '<a href="%s/an9.68/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.67.html">AN 9.67 &middot; Lower Fetters</a> &mdash; previous.',
        '<a href="an-9.69.html">AN 9.69 &middot; Stinginess</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.69 — Macchariyasutta
# --------------------------------------------------------------------------- #
page(
    69, "Macchariya", "Stinginess",
    vagga=VAGGA_7,
    meta_title="AN 9.69 — Stinginess | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Stinginess, applying this chapter's compressed template to the "
        "five kinds of stinginess — the most concretely social "
        "obstacle-list in this chapter. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five kinds of stinginess named in full, then the "
                 "remedy compressed to an ellipsis, matching AN 9.65-68"),
        ("Length", "~30 seconds to read"),
        ("A term already met once in this nipāta", "One of these five "
         "kinds of stinginess, with the teaching, was already named as "
         "the seventh of nine things rooted in craving at AN 9.23"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, and among the most socially concrete "
                       "lists in this chapter"),
    ],
    why=(
        "The five kinds of stinginess &mdash; with dwellings, families, "
        "material things, praise, and the teaching &mdash; are given "
        "up the same way as every other obstacle in this chapter, by "
        "developing the four kinds of mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five kinds of stinginess &mdash; with "
            "dwellings, families, material things, praise, and the "
            "teaching &mdash; a mendicant should develop the four kinds "
            "of mindfulness meditation, the same remedy given "
            "throughout this chapter."]),
        ("Five domains of withholding", [
            "Unlike more abstract obstacle-lists elsewhere in this "
            "chapter, stinginess names five concrete, socially "
            "observable domains: a monastic's own lodging, their "
            "spiritual patrons or families, material possessions, "
            "credit or praise, and &mdash; distinctively &mdash; the "
            "teaching itself, withheld from those who might benefit "
            "from hearing it."]),
        ("Withholding the teaching, a stinginess unlike the rest", [
            "The fifth item, stinginess with the Dhamma, stands apart "
            "from the other four's more ordinary possessiveness: it "
            "names a specifically monastic failure, hoarding spiritual "
            "knowledge rather than material goods, and closes the list "
            "on its most consequential form."]),
        ("A term this nipāta has already touched once", [
            "Stinginess (macchariya) itself was already named as the "
            "seventh link in AN 9.23's nine-stage chain rooted in "
            "craving &mdash; ownership producing stinginess, stinginess "
            "producing safeguarding, and safeguarding eventually "
            "producing open conflict. This discourse doesn't repeat "
            "that chain but names the specific domains stinginess takes "
            "when it does arise."]),
    ],
    terms=[
        ("pañca macchariyāni",
         "&ldquo;the five kinds of stinginess&rdquo; &mdash; this "
         "discourse's own title term, naming five concrete domains of "
         "withholding."),
        ("āvāsamacchariyaṁ, kulamacchariyaṁ, lābhamacchariyaṁ",
         "&ldquo;stinginess with dwellings, families, material "
         "things&rdquo; &mdash; the first three, ordinary forms of "
         "monastic possessiveness."),
        ("vaṇṇamacchariyaṁ, dhammamacchariyaṁ",
         "&ldquo;stinginess with praise, and the teaching&rdquo; "
         "&mdash; the remaining two, the latter a distinctively "
         "monastic failure of withholding spiritual knowledge."),
        ("macchariyaṁ ārakkhaṁ janeti",
         "&ldquo;stinginess gives rise to safeguarding&rdquo; &mdash; "
         "AN 9.23's own use of this same term, as one link in a nine-"
         "stage chain rooted in craving."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, named but not spelled out in this "
         "discourse."),
    ],
    text_intro=(
        "The discourse in full, as it survives: five kinds of "
        "stinginess given in full, then the remedy compressed to an "
        "ellipsis. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five kinds of stinginess"),
        ("p", "&sect;1", "an9.69:1.1-1.4"),
        ("h3", "The remedy, compressed"),
        ("p", "&sect;2", "an9.69:2.1-2.1"),
    ],
    quiz=[
        {"q": "What five kinds of stinginess does this discourse name?",
         "opts": [
             "With food, robes, money, sleep, and speech",
             "With dwellings, families, material things, praise, and "
             "the teaching",
             "The five hindrances",
             "Five kinds of wrong view"],
         "correct": 1,
         "expl": "Five concrete, socially observable domains of "
                 "withholding."},
        {"q": "What makes the fifth item, stinginess with the teaching, "
              "distinctive among the five?",
         "opts": [
             "Nothing distinguishes it from the others",
             "It names a specifically monastic failure — hoarding "
             "spiritual knowledge rather than material goods",
             "It is the least serious of the five",
             "It doesn't actually belong on this list"],
         "correct": 1,
         "expl": "A withholding of benefit to others, distinct from "
                 "ordinary possessiveness."},
        {"q": "Where has this project already met the term "
              "&lsquo;stinginess&rsquo; (macchariya) earlier in this "
              "nipāta?",
         "opts": [
             "Nowhere before this discourse",
             "As the seventh link in AN 9.23's nine-stage chain rooted "
             "in craving",
             "Only in a completely unrelated nipāta",
             "At AN 9.1, the opening discourse"],
         "correct": 1,
         "expl": "A single step in a causal chain there, five concrete "
                 "domains here."},
        {"q": "How does this discourse relate to AN 9.23's chain?",
         "opts": [
             "It repeats the chain in full",
             "It doesn't repeat the chain, but names the specific "
             "domains stinginess takes when it does arise",
             "It contradicts AN 9.23 entirely",
             "It has no relationship to AN 9.23"],
         "correct": 1,
         "expl": "Complementary treatments of the same underlying "
                 "concept."},
        {"q": "How is the four-foundation remedy presented in this "
              "discourse?",
         "opts": [
             "Given in complete detail",
             "Compressed to a bare ellipsis, continuing the pattern "
             "from AN 9.65 through AN 9.68",
             "Replaced with a different remedy",
             "Omitted with no mention at all"],
         "correct": 1,
         "expl": "Continuing this chapter's sustained compression."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching this whole "
                 "chapter's method."},
    ],
    marginalia=[
        ("Five domains withheld", [
            "lodging, family, goods,",
            "praise, and &mdash; worst of all &mdash;",
            "the teaching itself",
        ]),
        ("A link, met before", [
            "stinginess, once a step",
            "in craving's own chain &mdash;",
            "now, named outright",
        ]),
        ("Withholding what helps others", [
            "hoarding the Dhamma",
            "closes the list &mdash; a failure",
            "worse than material greed",
        ]),
        ("Cross-references", [
            "AN 9.23 &middot; the same term, one link in an earlier "
            "causal chain",
            "AN 9.68 &middot; previous",
            "AN 9.70 &middot; next, Higher Fetters",
        ]),
    ],
    further=[
        '<a href="%s/an9.69/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.68.html">AN 9.68 &middot; Places of Rebirth</a> &mdash; previous.',
        '<a href="an-9.70.html">AN 9.70 &middot; Higher Fetters</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.70 — Uddhambhāgiyasutta — last of this chapter's compressed run
# --------------------------------------------------------------------------- #
page(
    70, "Uddhambhāgiya", "Higher Fetters",
    vagga=VAGGA_7,
    meta_title="AN 9.70 — Higher Fetters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Higher Fetters, closing this chapter's compressed run with "
        "the five fetters ended only by full awakening. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five higher fetters named in full, then the remedy "
                 "compressed to an ellipsis, the last discourse in this "
                 "chapter to do so"),
        ("Length", "~30 seconds to read"),
        ("The counterpart to AN 9.67's lower fetters", "Where ending "
         "the five lower fetters produces a non-returner, ending these "
         "five higher fetters is what full arahantship requires"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "brief in text, naming the final barrier to full "
                       "awakening"),
    ],
    why=(
        "The five higher fetters &mdash; desire for rebirth in the "
        "realm of luminous form, desire for rebirth in the formless "
        "realm, conceit, restlessness, and ignorance &mdash; are given "
        "up the same way as every obstacle in this chapter, by "
        "developing the four kinds of mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five higher fetters &mdash; desire for "
            "rebirth in the realm of luminous form, desire for rebirth "
            "in the formless realm, conceit, restlessness, and "
            "ignorance &mdash; a mendicant should develop the four "
            "kinds of mindfulness meditation, the same remedy given "
            "throughout this chapter."]),
        ("The counterpart to AN 9.67's lower fetters", [
            "This discourse completes a pair with AN 9.67 three "
            "discourses earlier: where ending the five lower fetters "
            "marks non-return, ending these five higher fetters is what "
            "full arahantship itself requires &mdash; the standard "
            "doctrinal division of the ten fetters into two sets of "
            "five, named here across two separate discourses in this "
            "same chapter."]),
        ("Subtler obstacles for a subtler stage", [
            "Where the lower fetters concern relatively coarse "
            "attachments &mdash; view, doubt, ritual, sensual desire, "
            "ill will &mdash; these higher fetters are correspondingly "
            "subtle: desire for the very meditative attainments this "
            "nipāta spends most of its length describing, along with "
            "conceit, restlessness, and the final residue of ignorance "
            "itself."]),
        ("The last discourse in this chapter's compressed run", [
            "This is the final discourse to use this chapter's "
            "compressed formula; AN 9.71 and AN 9.72, closing the "
            "chapter, both return to giving their obstacle-lists in "
            "considerably fuller detail than the ellipsis met "
            "throughout AN 9.65 to AN 9.70."]),
    ],
    terms=[
        ("pañcuddhambhāgiyāni saṁyojanāni",
         "&ldquo;the five higher fetters&rdquo; &mdash; this "
         "discourse's own title term, the counterpart to AN 9.67's "
         "lower fetters."),
        ("rūparāgo, arūparāgo",
         "&ldquo;desire for rebirth in the realm of luminous form, "
         "desire for rebirth in the formless realm&rdquo; &mdash; the "
         "first two higher fetters, naming attachment to the very "
         "attainments this nipāta describes at length."),
        ("māno, uddhaccaṁ, avijjā",
         "&ldquo;conceit, restlessness, and ignorance&rdquo; &mdash; "
         "the remaining three, closing the standard list of ten "
         "fetters' second half."),
        ("…pe…",
         "the Pāli peyyāla marker, left untranslated as an ellipsis "
         "&mdash; marking the last use of this chapter's compressed "
         "form before AN 9.71 restores fuller detail."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, here applied to the final barrier "
         "before full awakening."),
    ],
    text_intro=(
        "The discourse in full, as it survives: five higher fetters "
        "given in full, then the remedy compressed to an ellipsis. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The five higher fetters"),
        ("p", "&sect;1", "an9.70:1.1-1.4"),
        ("h3", "The remedy, compressed"),
        ("p", "&sect;2", "an9.70:2.1-2.1"),
    ],
    quiz=[
        {"q": "What five higher fetters does this discourse name?",
         "opts": [
             "The five hindrances",
             "Desire for rebirth in the realm of luminous form, desire "
             "for rebirth in the formless realm, conceit, "
             "restlessness, and ignorance",
             "The five aggregates",
             "Five kinds of stinginess"],
         "correct": 1,
         "expl": "The standard second half of the ten fetters, ended "
                 "only by full arahantship."},
        {"q": "How does this discourse's list relate to AN 9.67's lower "
              "fetters?",
         "opts": [
             "No relationship at all",
             "The two together form the standard division of the ten "
             "fetters into lower (ending in non-return) and higher "
             "(ending in arahantship)",
             "This list replaces AN 9.67's list entirely",
             "They name identical fetters"],
         "correct": 1,
         "expl": "A completing pair, named across two separate "
                 "discourses in this same chapter."},
        {"q": "What do the first two higher fetters concern?",
         "opts": [
             "Physical possessions",
             "Desire for the meditative attainments this nipāta "
             "spends most of its length describing",
             "Doubt about the teaching",
             "Sensual pleasure"],
         "correct": 1,
         "expl": "Even attachment to the formless attainments "
                 "themselves counts as a fetter to overcome."},
        {"q": "What is this discourse's position within this chapter's "
              "compressed run?",
         "opts": [
             "The first discourse to use the compressed form",
             "The last discourse to use the compressed form, before AN "
             "9.71 and AN 9.72 return to fuller detail",
             "It doesn't use the compressed form at all",
             "It falls outside the compressed run entirely"],
         "correct": 1,
         "expl": "Closing the run begun at AN 9.65."},
        {"q": "What happens at AN 9.71 and AN 9.72, closing this "
              "chapter?",
         "opts": [
             "Further compression, even briefer than this discourse",
             "A return to considerably fuller detail than the "
             "ellipsis used throughout AN 9.65 to AN 9.70",
             "The chapter simply ends without further discourses",
             "A repeat of AN 9.63's exact content"],
         "correct": 1,
         "expl": "The chapter's closing pair breaks from the "
                 "compressed pattern."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching this chapter's "
                 "compressed discourses."},
    ],
    marginalia=[
        ("A completing pair", [
            "lower fetters, non-return;",
            "higher fetters, full",
            "awakening required",
        ]),
        ("Subtler still", [
            "desire for form, formless,",
            "conceit, restlessness,",
            "and ignorance itself",
        ]),
        ("The last compressed page", [
            "one line, an ellipsis &mdash;",
            "the final time this chapter",
            "trusts memory alone",
        ]),
        ("Cross-references", [
            "AN 9.67 &middot; the lower fetters this discourse's higher "
            "fetters complete",
            "AN 9.69 &middot; previous",
            "AN 9.71 &middot; next, Hard-heartedness, restoring fuller "
            "detail",
        ]),
    ],
    further=[
        '<a href="%s/an9.70/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.69.html">AN 9.69 &middot; Stinginess</a> &mdash; previous.',
        '<a href="an-9.71.html">AN 9.71 &middot; Hard-heartedness</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.71 — Cetokhilasutta — restores full detail
# --------------------------------------------------------------------------- #
page(
    71, "Cetokhila", "Hard-heartedness",
    vagga=VAGGA_7,
    meta_title="AN 9.71 — Hard-heartedness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Hard-heartedness, restoring full detail to close this "
        "chapter's compressed run — five ways the mind refuses to "
        "incline toward practice. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five kinds of hard-heartedness, each given its own "
                 "explanation and shared refrain, restoring the fuller "
                 "detail last seen at AN 9.63-64"),
        ("Length", "~2 minutes to read"),
        ("Fuller detail restored", "Unlike AN 9.65 through AN 9.70, "
         "this discourse explains each item rather than merely naming "
         "it, and gives a psychological mechanism for why it obstructs "
         "practice"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "more substantial than its immediate "
                       "predecessors, worth reading for its "
                       "psychological precision"),
    ],
    why=(
        "Five kinds of hard-heartedness &mdash; doubt about the "
        "Teacher, the teaching, the Saṅgha, and the training, plus "
        "anger and resentment toward one's spiritual companions "
        "&mdash; each share the same mechanism: whenever present, the "
        "mind doesn't incline toward keenness, commitment, persistence, "
        "and striving, and are given up by developing the four kinds of "
        "mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "Five kinds of hard-heartedness &mdash; doubt about the "
            "Teacher, the teaching, the Saṅgha, and the training, and "
            "anger toward spiritual companions &mdash; each keep the "
            "mind from inclining toward keenness, commitment, "
            "persistence, and striving, and are given up by developing "
            "the four kinds of mindfulness meditation."]),
        ("A shift back to fuller explanation", [
            "After six discourses compressed to a bare list and an "
            "ellipsis, this discourse restores the kind of detail last "
            "seen at AN 9.63 and AN 9.64: each of the five items gets "
            "its own explanation, not just a name, and the shared "
            "mechanism connecting all five is spelled out explicitly "
            "rather than left implicit."]),
        ("A named mechanism, not just a list", [
            "What makes this discourse's five items cohere as one "
            "category isn't superficial similarity but a shared "
            "psychological consequence: each, when present, keeps the "
            "mind from &lsquo;inclining toward keenness, commitment, "
            "persistence, and striving&rsquo; &mdash; hard-heartedness "
            "named for what it does to motivation, not merely for what "
            "it is."]),
        ("Four doubts, then one interpersonal rupture", [
            "The first four items form a clean set &mdash; doubt about "
            "the Teacher, the teaching, the Saṅgha, and the training, "
            "the same four objects of confidence met throughout this "
            "nipāta's stream-entry formula, now viewed from their "
            "shadow side. The fifth breaks this pattern: not doubt "
            "about a doctrinal object at all, but anger and closed-off "
            "resentment toward one's own spiritual companions."]),
    ],
    terms=[
        ("cetokhilā",
         "&ldquo;hard-heartedness&rdquo; &mdash; this discourse's own "
         "title term, literally a barrenness or hardening of the heart "
         "that blocks inclination toward practice."),
        ("satthari kaṅkhati vicikicchati",
         "&ldquo;has doubts about the Teacher... uncertain, undecided, "
         "and lacking confidence&rdquo; &mdash; the first of the five, "
         "shadowing the first factor of stream-entry."),
        ("na namati ātappāya anuyogāya sātaccāya padhānāya",
         "&ldquo;their mind doesn't incline toward keenness, "
         "commitment, persistence, and striving&rdquo; &mdash; the "
         "shared mechanism naming what all five items have in common."),
        ("sabrahmacārīsu kupito hoti anattamano āhatacitto khilajāto",
         "&ldquo;angry and upset with their spiritual companions, "
         "resentful and closed off&rdquo; &mdash; the fifth item, "
         "breaking from the doubt-pattern of the first four."),
        ("cattāro satipaṭṭhānā",
         "&ldquo;the four kinds of mindfulness meditation&rdquo; "
         "&mdash; the shared remedy, once again named without full "
         "elaboration, but following a fuller explanation of the "
         "obstacle."),
    ],
    text_intro=(
        "The discourse in full: five kinds of hard-heartedness, each "
        "explained, and the shared mechanism connecting them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five kinds of hard-heartedness"),
        ("p", "&sect;1", "an9.71:1.1-2.6"),
        ("h3", "The remedy"),
        ("p", "&sect;2", "an9.71:3.1-3.1"),
    ],
    quiz=[
        {"q": "What shared mechanism connects all five kinds of hard-"
              "heartedness?",
         "opts": [
             "They each involve physical illness",
             "Each keeps the mind from inclining toward keenness, "
             "commitment, persistence, and striving",
             "They each involve breaking a specific precept",
             "They have no shared mechanism at all"],
         "correct": 1,
         "expl": "Named for their psychological consequence, not "
                 "merely their surface content."},
        {"q": "What do the first four kinds of hard-heartedness share?",
         "opts": [
             "They are all about physical possessions",
             "They are doubts about the Teacher, the teaching, the "
             "Saṅgha, and the training — the same four objects of "
             "confidence in the stream-entry formula",
             "They are all about sensual pleasure",
             "They are unrelated to each other"],
         "correct": 1,
         "expl": "The shadow side of the four factors of stream-entry "
                 "met earlier in this nipāta."},
        {"q": "How does the fifth kind of hard-heartedness break from "
              "the first four?",
         "opts": [
             "It doesn't break the pattern at all",
             "It isn't doubt about a doctrinal object, but anger and "
             "closed-off resentment toward one's own spiritual "
             "companions",
             "It is a repeat of the first item",
             "It concerns only physical health"],
         "correct": 1,
         "expl": "An interpersonal rupture, distinct from the four "
                 "doctrinal doubts before it."},
        {"q": "How does this discourse's level of detail compare to AN "
              "9.65 through AN 9.70?",
         "opts": [
             "Equally compressed, with a bare ellipsis",
             "Fuller — each item gets its own explanation, restoring "
             "the detail last seen at AN 9.63 and AN 9.64",
             "Even more compressed than those discourses",
             "Identical in every respect"],
         "correct": 1,
         "expl": "A deliberate return to fuller elaboration after six "
                 "compressed discourses."},
        {"q": "What remedy does this discourse prescribe, matching this "
              "whole chapter?",
         "opts": [
             "The four right efforts",
             "The four kinds of mindfulness meditation",
             "The four noble truths",
             "The six higher knowledges"],
         "correct": 1,
         "expl": "The shared remedy running through all ten discourses "
                 "in this chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, though fuller in detail "
                 "than its immediate predecessors."},
    ],
    marginalia=[
        ("A shared mechanism", [
            "not what each doubt is,",
            "but what it does &mdash; blocks",
            "keenness, striving, both",
        ]),
        ("Four doubts, one rupture", [
            "Teacher, teaching, Saṅgha,",
            "training doubted &mdash; then, anger",
            "at one's own companions",
        ]),
        ("Fuller detail returns", [
            "each item explained,",
            "not merely named &mdash;",
            "as at 9.63, 9.64",
        ]),
        ("Cross-references", [
            "AN 9.27 &middot; the same four objects of confidence, "
            "there as positive factors",
            "AN 9.70 &middot; previous",
            "AN 9.72 &middot; next, Shackles of the Heart, closing this "
            "chapter",
        ]),
    ],
    further=[
        '<a href="%s/an9.71/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.70.html">AN 9.70 &middot; Higher Fetters</a> &mdash; previous.',
        '<a href="an-9.72.html">AN 9.72 &middot; Shackles of the Heart</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.72 — Cetasovinibandhasutta — closes ch.7 Satipatthanavagga
# --------------------------------------------------------------------------- #
page(
    72, "Cetasovinibandha", "Shackles of the Heart",
    vagga=VAGGA_7,
    meta_title="AN 9.72 — Shackles of the Heart | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "Shackles of the Heart, closing this chapter with five ways "
        "attachment binds a mendicant's motivation, from bodily "
        "indulgence to seeking rebirth as a god through spiritual "
        "practice. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five shackles of the heart, each explained, then the "
                 "four kinds of mindfulness meditation given in full "
                 "one final time"),
        ("Length", "~2 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Satipatthanavagga</em>, the seventh chapter; the "
         "source's own untranslated closing verse names all ten "
         "discourses of the chapter by their opening words"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "substantial, closing this chapter with its most "
                       "pointed obstacle-list"),
    ],
    why=(
        "Five shackles of the heart &mdash; unresolved greed for "
        "sensual pleasures, for the body, for physical form, for "
        "comfort and sleep, and for rebirth among the gods sought "
        "through spiritual practice itself &mdash; each keep the mind "
        "from inclining toward keenness, commitment, persistence, and "
        "striving, and are given up, closing this chapter, by "
        "developing the four kinds of mindfulness meditation."),
    guide=[
        ("The teaching in one sentence", [
            "Five shackles of the heart &mdash; unresolved greed for "
            "sensual pleasures, for the body, for physical form, "
            "indulgence in comfort and sleep, and desire for rebirth "
            "among the gods pursued through one's own spiritual "
            "practice &mdash; each keep the mind from inclining toward "
            "keenness, commitment, persistence, and striving, and are "
            "given up by developing the four kinds of mindfulness "
            "meditation."]),
        ("The same mechanism as AN 9.71, a different content", [
            "This discourse shares its closing mechanism exactly with "
            "AN 9.71 &mdash; each shackle, like each kind of hard-"
            "heartedness, is defined by keeping the mind from "
            "&lsquo;inclining toward keenness, commitment, persistence, "
            "and striving&rsquo; &mdash; but where hard-heartedness "
            "named doubt and interpersonal rupture, these five shackles "
            "all concern unresolved attachment."]),
        ("A shackle turned against spiritual practice itself", [
            "The fifth and final shackle is the most pointed: a "
            "mendicant who leads the spiritual life hoping that "
            "precepts, observances, austerity, or practice will earn "
            "rebirth among the gods has turned the very tools of "
            "liberation into a subtler form of the same craving those "
            "tools exist to end &mdash; practice itself, corrupted by "
            "an ordinary worldly aim."]),
        ("Closing the chapter with full treatment restored", [
            "Unlike AN 9.71, this discourse gives the complete four-"
            "foundation formula one final time, matching AN 9.63 and AN "
            "9.64's opening treatment and closing "
            "<em>Satipatthanavagga</em> on the same full detail it "
            "began with. The source's own untranslated colophon and "
            "chapter-summary verse name all ten discourses of the "
            "chapter by their opening words."]),
    ],
    terms=[
        ("cetaso vinibandhā",
         "&ldquo;shackles of the heart&rdquo; &mdash; this discourse's "
         "own title term, naming five forms of unresolved attachment."),
        ("kāmesu avītarāgo hoti",
         "&ldquo;isn't free of greed... for sensual pleasures&rdquo; "
         "&mdash; the first shackle, echoing the same craving named "
         "&lsquo;confinement&rsquo; at AN 9.42 and &lsquo;the "
         "world&rsquo; at AN 9.38."),
        ("yāvadatthaṁ udarāvadehakaṁ bhuñjitvā seyyasukhaṁ "
         "passasukhaṁ middhasukhaṁ anuyutto viharati",
         "&ldquo;eat as much as they like until their belly is full, "
         "then indulge in the pleasures of sleeping, lying down, and "
         "drowsing&rdquo; &mdash; the fourth shackle, a vivid, concrete "
         "image among this discourse's otherwise abstract vocabulary."),
        ("iminā sīlena vā vatena vā tapena vā brahmacariyena vā "
         "devo vā bhavissāmi devaññataro vā",
         "&ldquo;by this precept or observance or fervent austerity or "
         "spiritual practice, may I become one of the gods&rdquo; "
         "&mdash; the fifth and final shackle, spiritual practice "
         "corrupted by a worldly aim."),
        ("satipaṭṭhānavaggo sattamo",
         "&ldquo;the seventh chapter, Satipaṭṭhānavagga, is "
         "finished&rdquo; &mdash; the source's own untranslated "
         "colophon closing this chapter."),
    ],
    text_intro=(
        "The discourse in full: five shackles of the heart, each "
        "explained, and the four kinds of mindfulness meditation given "
        "one final time. The source's own closing colophon and chapter-"
        "summary verse are untranslated in the English and are "
        "described rather than quoted here. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Five shackles of the heart"),
        ("p", "&sect;1", "an9.72:1.1-2.7"),
        ("h3", "Four kinds of mindfulness meditation"),
        ("p", "&sect;2", "an9.72:3.1-3.7"),
    ],
    quiz=[
        {"q": "What five shackles of the heart does this discourse "
              "name?",
         "opts": [
             "Five monastic disciplinary offenses",
             "Unresolved greed for sensual pleasures, the body, "
             "physical form, indulgence in comfort and sleep, and "
             "desire for rebirth among the gods through practice",
             "The five hindrances",
             "The five aggregates"],
         "correct": 1,
         "expl": "Five forms of unresolved attachment, closing this "
                 "chapter's obstacle-lists."},
        {"q": "What mechanism does this discourse share exactly with AN "
              "9.71?",
         "opts": [
             "No shared mechanism",
             "Each item, when present, keeps the mind from inclining "
             "toward keenness, commitment, persistence, and striving",
             "Both discourses name identical obstacles",
             "Both discourses use the compressed ellipsis form"],
         "correct": 1,
         "expl": "The same psychological consequence, applied here to "
                 "attachment rather than doubt."},
        {"q": "What makes the fifth shackle especially pointed?",
         "opts": [
             "It concerns only physical comfort",
             "It names spiritual practice itself turned into a subtler "
             "form of craving, seeking rebirth as a god through "
             "precepts and austerity",
             "It is identical to the first shackle",
             "It has nothing to do with practice"],
         "correct": 1,
         "expl": "The tools of liberation corrupted by an ordinary "
                 "worldly aim."},
        {"q": "How does this discourse's treatment of the four "
              "foundations compare to AN 9.71's?",
         "opts": [
             "Equally brief, just naming the remedy",
             "Full treatment is restored one final time, matching AN "
             "9.63 and AN 9.64's opening detail",
             "Even more compressed",
             "The remedy is entirely different here"],
         "correct": 1,
         "expl": "Closing the chapter on the same full detail it began "
                 "with."},
        {"q": "What does this discourse close, and how?",
         "opts": [
             "Nothing; the chapter continues past it",
             "<em>Satipatthanavagga</em>, the seventh chapter, with an "
             "untranslated colophon and uddāna verse naming all ten "
             "discourses",
             "The entire nipāta",
             "Only this single discourse, with no chapter-level effect"],
         "correct": 1,
         "expl": "The chapter's own closing colophon, left untranslated "
                 "in the English."},
        {"q": "Which shackle involves a vivid, concrete image distinct "
              "from this discourse's otherwise abstract vocabulary?",
         "opts": [
             "The first, greed for sensual pleasures",
             "The fourth, eating until full and indulging in sleep and "
             "drowsiness",
             "The second, greed for the body",
             "The fifth, seeking rebirth as a god"],
         "correct": 1,
         "expl": "A concrete bodily image amid the chapter's otherwise "
                 "abstract terminology."},
    ],
    marginalia=[
        ("Five shackles, unresolved", [
            "sensual pleasure, body,",
            "form, comfort, sleep &mdash; and rebirth",
            "as a god, sought wrongly",
        ]),
        ("Practice, corrupted", [
            "precepts, austerity,",
            "kept for a god's rebirth &mdash;",
            "craving in disguise",
        ]),
        ("Closing the chapter, in full", [
            "four foundations, spelled",
            "out once more &mdash; the same",
            "detail it began with",
        ]),
        ("Cross-references", [
            "AN 9.38, AN 9.42 &middot; the same craving named &lsquo;"
            "the world&rsquo; and &lsquo;confinement&rsquo; elsewhere",
            "AN 9.71 &middot; previous",
            "AN 9.73 &middot; next, opening ch.8, Sammappadhanavagga",
        ]),
    ],
    further=[
        '<a href="%s/an9.72/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.71.html">AN 9.71 &middot; Hard-heartedness</a> &mdash; previous.',
    ],
)


# --------------------------------------------------------------------------- #
# ch.8 — Sammappadhanavagga (AN 9.73-82). Reuses ch.7's exact ten obstacle-
# lists, swapping the remedy from the four kinds of mindfulness meditation
# to the four right efforts. Only the first (AN 9.73) and last (AN 9.82)
# discourses are given individually; AN 9.74-81 is a single merged page
# whose entire surviving text is "(Tell in full as in the chapter on
# mindfulness meditation.)" -- the first case in this project of a merged
# page pointing back to another chapter's own content rather than compressing
# via peyyāla or repeating a self-contained formula.
# --------------------------------------------------------------------------- #
VAGGA_8 = "<em>Sammappadhanavagga</em> &mdash; the eighth chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.73 — Sekhasutta (Right Efforts version)
# --------------------------------------------------------------------------- #
page(
    73, "Sekha", "Weaknesses in Training and Effort",
    vagga=VAGGA_8,
    meta_title="AN 9.73 — Weaknesses in Training and Effort | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the discourse opening this chapter — the identical obstacle-"
        "list as AN 9.63, now answered by the four right efforts rather "
        "than mindfulness meditation. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five weaknesses named, then the four right efforts "
                 "given in full as the remedy"),
        ("Length", "~1 minute to read"),
        ("Ch.7's obstacle, a new remedy", "The same five weaknesses "
         "opening ch.7 recur here, but the four right efforts replace "
         "the four kinds of mindfulness meditation as what overcomes "
         "them"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, opening a chapter that reuses ch.7's "
                       "structure with one substitution"),
    ],
    why=(
        "The same five weaknesses that open ch.7 &mdash; killing, "
        "stealing, sexual misconduct, lying, and intoxicants &mdash; "
        "recur here, but this time are given up by developing the four "
        "right efforts: generating enthusiasm and striving so that bad "
        "qualities don't arise or are given up, and skillful qualities "
        "arise or are developed further."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five weaknesses in training &mdash; "
            "killing, stealing, sexual misconduct, lying, and "
            "intoxicants &mdash; a mendicant should develop the four "
            "right efforts: striving to prevent, abandon, develop, and "
            "maintain skillful and unskillful qualities respectively."]),
        ("The identical obstacle, a substituted remedy", [
            "This discourse's five weaknesses are word-for-word "
            "identical to AN 9.63's opener several chapters back. What "
            "changes is entirely the remedy: where ch.7 answered every "
            "obstacle with the four kinds of mindfulness meditation, "
            "this chapter answers the identical ten obstacle-lists with "
            "the four right efforts instead."]),
        ("Four efforts, aimed in two directions each", [
            "The four right efforts split cleanly into prevention and "
            "cure for each of two categories: preventing unskillful "
            "qualities from arising, abandoning those that have "
            "arisen, developing skillful qualities not yet arisen, and "
            "maintaining and increasing those already present &mdash; "
            "an active, effort-driven complement to mindfulness "
            "meditation's more observational approach."]),
        ("A chapter built on substitution, not new content", [
            "This chapter's real interest lies less in its individual "
            "obstacle-lists, already fully explored in ch.7, than in "
            "what it reveals by substitution: the same ten problems "
            "this project has already named can each be answered by "
            "more than one canonical remedy, mindfulness meditation and "
            "right effort standing as parallel, not competing, "
            "approaches."]),
    ],
    terms=[
        ("sekhā pañca dhammā",
         "&ldquo;five weaknesses when you're training&rdquo; &mdash; "
         "the identical five precepts-as-weaknesses already met opening "
         "AN 9.63."),
        ("cattāro sammappadhānā",
         "&ldquo;the four right efforts&rdquo; &mdash; this chapter's "
         "own remedy, replacing ch.7's four kinds of mindfulness "
         "meditation."),
        ("anuppannānaṁ pāpakānaṁ akusalānaṁ dhammānaṁ anuppādāya",
         "&ldquo;so that bad, unskillful qualities don't arise&rdquo; "
         "&mdash; the first of the four efforts, prevention."),
        ("uppannānaṁ kusalānaṁ dhammānaṁ ṭhitiyā... bhāvanāya pāripūriyā",
         "&ldquo;that skillful qualities that have arisen remain... "
         "and are completed by development&rdquo; &mdash; the fourth "
         "and final effort, maintaining and perfecting what is already "
         "present."),
        ("chandaṁ janeti vāyamati vīriyaṁ ārabhati cittaṁ paggaṇhāti "
         "padahati",
         "&ldquo;generates enthusiasm, tries, makes an effort, exerts "
         "the mind, and strives&rdquo; &mdash; the shared active "
         "formula repeated for each of the four efforts."),
    ],
    text_intro=(
        "The discourse in full: five weaknesses, and the four right "
        "efforts given as their remedy. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Five weaknesses in training"),
        ("p", "&sect;1", "an9.73:1.1-1.4"),
        ("h3", "Four right efforts"),
        ("p", "&sect;2", "an9.73:2.1-2.7"),
    ],
    quiz=[
        {"q": "How does this discourse's obstacle-list compare to AN "
              "9.63's?",
         "opts": [
             "Entirely different content",
             "Word-for-word identical — the same five weaknesses "
             "opening ch.7",
             "A shortened version of AN 9.63's list",
             "A contradiction of AN 9.63"],
         "correct": 1,
         "expl": "The obstacle stays the same; only the remedy changes "
                 "across the two chapters."},
        {"q": "What remedy does this chapter substitute for ch.7's four "
              "kinds of mindfulness meditation?",
         "opts": [
             "The four noble truths",
             "The four right efforts",
             "The four bases of psychic power",
             "The six higher knowledges"],
         "correct": 1,
         "expl": "A different canonical remedy applied to the same ten "
                 "obstacle-lists."},
        {"q": "How do the four right efforts divide their aim?",
         "opts": [
             "All four aim at the same single goal",
             "Prevention and abandonment of unskillful qualities, and "
             "development and maintenance of skillful ones",
             "Three aim at unskillful qualities and one at skillful "
             "qualities",
             "They have no clear structure"],
         "correct": 1,
         "expl": "A clean two-by-two structure: two directions "
                 "(prevent/abandon vs. develop/maintain) crossed with "
                 "two categories (unskillful/skillful)."},
        {"q": "According to the guide, what does this chapter reveal by "
              "substitution?",
         "opts": [
             "That ch.7's remedy was mistaken",
             "That the same ten obstacle-lists can each be answered by "
             "more than one canonical remedy, standing as parallel "
             "approaches",
             "That right effort is superior to mindfulness meditation",
             "That the obstacle-lists themselves are unimportant"],
         "correct": 1,
         "expl": "Mindfulness meditation and right effort as "
                 "complementary, not competing, methods."},
        {"q": "What shared formula is repeated for each of the four "
              "efforts?",
         "opts": [
             "A verse of praise",
             "&ldquo;Generates enthusiasm, tries, makes an effort, "
             "exerts the mind, and strives&rdquo;",
             "A warning about pride",
             "A request for further teaching"],
         "correct": 1,
         "expl": "An active, effort-driven formula, distinct from "
                 "mindfulness meditation's more observational refrain."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, opening this chapter "
                 "without narrative frame."},
    ],
    marginalia=[
        ("The same five weaknesses", [
            "killing, stealing, lying,",
            "misconduct, drink &mdash; identical",
            "to AN 9.63",
        ]),
        ("A new remedy substituted", [
            "not mindfulness now,",
            "but effort &mdash; prevent, abandon,",
            "develop, maintain",
        ]),
        ("Two remedies, one obstacle", [
            "the same ten problems,",
            "answered by more than one",
            "canonical cure",
        ]),
        ("Cross-references", [
            "AN 9.63 &middot; the identical obstacle-list, there "
            "answered by mindfulness meditation",
            "AN 9.72 &middot; previous chapter's closing page",
            "AN 9.74&ndash;81 &middot; next, pointing back to ch.7's "
            "content",
        ]),
    ],
    further=[
        '<a href="%s/an9.73/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.63.html">AN 9.63 &middot; Weaknesses in Training and Mindfulness '
        "Meditation</a> &mdash; the identical obstacle-list, there answered by "
        "mindfulness meditation.",
        '<a href="an-9.72.html">AN 9.72 &middot; Shackles of the Heart</a> &mdash; previous.',
        '<a href="an-9.74-81.html">AN 9.74&ndash;81</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.74-81 — the first merged page in this project pointing back to
# another chapter's own content rather than compressing via peyyāla.
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-9.74-81",
    "index_pali": "(untitled)",
    "nav_title": "Hindrances, Etc.",
    "source": "an9/an9.74-81",
    "crumb": "AN 9.74&ndash;81",
    "meta_title": "AN 9.74–81 — Hindrances, Etc. | Ru-Yi Meditation Center",
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "this merged page — eight discourses whose entire surviving "
        "text points back to ch.7's own content rather than repeating "
        "or compressing it. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 9.74&ndash;81",
    "title": "Hindrances, Etc.",
    "subtitle": "<em>Untitled in the source</em> &mdash; %s, continued" % VAGGA_8,
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single instruction, pointing back to an entire "
                 "earlier chapter rather than giving any content of its "
                 "own"),
        ("Length", "A few seconds to read the instruction itself"),
        ("A new kind of compression for this project", "Not a peyyāla "
         "compressing many suttas' own repeated content, but a direct "
         "pointer to a different chapter's content entirely"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read the instruction, but worth "
                       "understanding what it actually implies"),
    ],
    "why": (
        "Standing for eight separate discourses (AN 9.74 through AN "
        "9.81), this single page's entire surviving content is one "
        "instruction: &lsquo;tell in full as in the chapter on "
        "mindfulness meditation&rsquo; &mdash; directing the reciter "
        "back to ch.7's own eight middle obstacle-lists, each now paired "
        "with the four right efforts instead of the four kinds of "
        "mindfulness meditation."),
    "guide": [
        ("The teaching in one sentence", [
            "The same eight obstacle-lists already given in full at AN "
            "9.64 through AN 9.71 &mdash; hindrances, sensual "
            "stimulation, grasping aggregates, lower fetters, "
            "destinations, stinginess, higher fetters, and hard-"
            "heartedness &mdash; are each given up by developing the "
            "four right efforts, exactly as AN 9.73 already showed for "
            "the first obstacle-list in both chapters."]),
        ("A genuinely new kind of compression", [
            "Every peyyāla merge met so far in this project &mdash; "
            "from AN 3.183-352 through AN 8.148-627 &mdash; compresses "
            "many suttas that share one self-contained repeated "
            "content. This page is different in kind: it points not to "
            "content repeated within its own range, but to an entirely "
            "separate chapter, ch.7, several discourses back, trusting "
            "the reciter to substitute &lsquo;four right efforts&rsquo; "
            "for &lsquo;four kinds of mindfulness meditation&rsquo; "
            "throughout."]),
        ("Eight discourses, reduced to one instruction", [
            "Following the same order as ch.7's own AN 9.64 through AN "
            "9.71, this page stands for: hindrances, sensual "
            "stimulation, grasping aggregates, lower fetters, "
            "destinations, stinginess, higher fetters, and hard-"
            "heartedness &mdash; the eight middle obstacle-lists "
            "sandwiched between the &lsquo;weaknesses&rsquo; opener and "
            "&lsquo;shackles of the heart&rsquo; closer both chapters "
            "share."]),
        ("Not fabricating what the instruction withholds", [
            "This guide does not reconstruct all eight discourses' full "
            "text under the four-right-efforts framing, since the "
            "source itself declines to write them out. Readers wanting "
            "the specific obstacle-lists in full should read them "
            "directly at AN 9.64 through AN 9.71, then mentally "
            "substitute this chapter's remedy for ch.7's."]),
    ],
    "terms": [
        ("tesaṁyeva vitthāro satipaṭṭhānavaggasadisova kātabbo",
         "&ldquo;tell in full as in the chapter on mindfulness "
         "meditation&rdquo; &mdash; this page's entire surviving "
         "instruction, pointing back to ch.7 rather than repeating its "
         "content."),
        ("cattāro sammappadhānā",
         "&ldquo;the four right efforts&rdquo; &mdash; the one "
         "substitution this instruction asks the reciter to make "
         "throughout."),
        ("nīvaraṇā, kāmaguṇā, upādānakkhandhā",
         "&ldquo;hindrances, sensual stimulation, grasping "
         "aggregates&rdquo; &mdash; the first three of the eight "
         "obstacle-lists this page stands for, given in full at AN "
         "9.64-66."),
        ("orambhāgiyāni saṁyojanāni, gatiyo, macchariyāni, "
         "uddhambhāgiyāni saṁyojanāni, cetokhilā",
         "&ldquo;lower fetters, destinations, stinginess, higher "
         "fetters, hard-heartedness&rdquo; &mdash; the remaining five "
         "obstacle-lists this page stands for, given in full at AN "
         "9.67-71."),
        ("sammappadhānavaggo",
         "&ldquo;Sammappadhānavagga&rdquo; &mdash; this chapter's own "
         "name, naming the remedy this whole chapter substitutes for "
         "ch.7's."),
    ],
    "text_intro": (
        "The discourse exactly as it survives in the source: a single "
        "instruction pointing back to ch.7's own content. Nothing has "
        "been added or reconstructed. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    "text": [
        ("h3", "The instruction, in full"),
        ("p", "&sect;1", "an9.74-81:1.1-1.1"),
    ],
    "quiz": [
        {"q": "What does this page's entire surviving text consist of?",
         "opts": [
             "The full text of eight discourses, spelled out completely",
             "A single instruction: &lsquo;tell in full as in the "
             "chapter on mindfulness meditation&rsquo;",
             "A peyyāla compression of repeated content within its own "
             "range",
             "Nothing; the page is entirely blank"],
         "correct": 1,
         "expl": "A direct pointer to ch.7's content, not a self-"
                 "contained repetition."},
        {"q": "How does this compression differ from every peyyāla "
              "merge met earlier in this project?",
         "opts": [
             "No difference at all",
             "Those compress content repeated within their own sutta "
             "range; this one points to an entirely separate chapter, "
             "ch.7, several discourses back",
             "This page has far more content than any peyyāla merge",
             "Peyyāla merges never occur elsewhere in this project"],
         "correct": 1,
         "expl": "A genuinely new kind of compression, first met at "
                 "this page."},
        {"q": "What eight obstacle-lists does this page stand for?",
         "opts": [
             "Eight entirely new lists never mentioned before",
             "The same eight given in full at AN 9.64 through AN "
             "9.71 — hindrances through hard-heartedness",
             "Only the five hindrances, repeated eight times",
             "Eight kinds of wrong view"],
         "correct": 1,
         "expl": "Ch.7's own eight middle obstacle-lists, sandwiched "
                 "between the shared opener and closer."},
        {"q": "What single substitution does the instruction ask the "
              "reciter to make?",
         "opts": [
             "Replace all five-item lists with nine-item lists",
             "Replace the four kinds of mindfulness meditation with the "
             "four right efforts",
             "Replace ch.7's speaker with a different one",
             "No substitution is needed"],
         "correct": 1,
         "expl": "The one variable that changes between the two "
                 "chapters' otherwise identical obstacle-lists."},
        {"q": "What does this page's guide avoid doing?",
         "opts": [
             "Explaining the instruction at all",
             "Reconstructing all eight discourses' full text, since the "
             "source itself declines to write them out",
             "Pointing readers to AN 9.64 through AN 9.71",
             "Naming the eight obstacle-lists"],
         "correct": 1,
         "expl": "Consistent with this project's rule against inventing "
                 "text not in the source."},
        {"q": "Where should a reader go for the full text of these "
              "eight obstacle-lists?",
         "opts": [
             "Nowhere; the content is permanently lost",
             "AN 9.64 through AN 9.71, then mentally substitute this "
             "chapter's remedy for ch.7's",
             "A completely different nipāta",
             "The Rāgapeyyāla closing this nipāta"],
         "correct": 1,
         "expl": "Ch.7's own full treatment of the identical obstacle-"
                 "lists."},
    ],
    "marginalia": [
        ("One instruction, eight discourses", [
            "&ldquo;tell it as in the",
            "mindfulness chapter&rdquo; &mdash;",
            "nothing more written",
        ]),
        ("A new kind of pointer", [
            "not repeated content,",
            "but another chapter,",
            "referenced whole",
        ]),
        ("One substitution asked", [
            "swap in right effort",
            "for mindfulness &mdash; the rest",
            "stays exactly the same",
        ]),
        ("Cross-references", [
            "AN 9.64&ndash;71 &middot; ch.7's full treatment of these "
            "same eight obstacle-lists",
            "AN 9.73 &middot; previous",
            "AN 9.82 &middot; next, Shackles of the Heart, closing this "
            "chapter",
        ]),
    ],
    "further": [
        '<a href="%s/an9.74-81/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.64.html">AN 9.64 &middot; Hindrances</a> &mdash; ch.7’s full '
        "treatment of the first obstacle-list this page stands for.",
        '<a href="an-9.73.html">AN 9.73 &middot; Weaknesses in Training and Effort</a> '
        "&mdash; previous.",
        '<a href="an-9.82.html">AN 9.82 &middot; Shackles of the Heart</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 9.82 — Cetasovinibandhasutta (Right Efforts version) — closes ch.8
# Sammappadhanavagga
# --------------------------------------------------------------------------- #
page(
    82, "Cetasovinibandha", "Shackles of the Heart",
    vagga=VAGGA_8,
    meta_title="AN 9.82 — Shackles of the Heart | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the discourse closing this chapter — the identical five "
        "shackles as AN 9.72, now answered by the four right efforts, "
        "closing both this chapter and its own colophon. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five shackles of the heart, then the four right "
                 "efforts given in full as the remedy"),
        ("Length", "~2 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse "
         "closes <em>Sammappadhanavagga</em>, the eighth chapter; the "
         "source's own colophon numbers it &lsquo;third&rsquo; within "
         "the Second Fifty, the same restarted numbering already met "
         "closing ch.6"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "substantial, closing this chapter on its most "
                       "pointed obstacle-list, as ch.7 did"),
    ],
    why=(
        "The same five shackles of the heart that closed ch.7 &mdash; "
        "unresolved greed for sensual pleasures, the body, physical "
        "form, comfort and sleep, and rebirth among the gods sought "
        "through spiritual practice &mdash; recur here, closing this "
        "chapter, given up instead by developing the four right efforts."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five shackles of the heart &mdash; "
            "unresolved greed for sensual pleasures, the body, "
            "physical form, comfort and sleep, and rebirth among the "
            "gods sought through spiritual practice &mdash; a "
            "mendicant should develop the four right efforts, the same "
            "remedy running through this entire chapter."]),
        ("The identical closer, a substituted remedy", [
            "As with AN 9.73's opener, this discourse's five shackles "
            "are word-for-word identical to AN 9.72's closer several "
            "chapters back. The two chapters share their opening and "
            "closing obstacle-lists precisely, differing only in the "
            "remedy applied throughout &mdash; mindfulness meditation "
            "in ch.7, right effort here."]),
        ("A shackle turned against practice, answered by effort", [
            "The fifth and most pointed shackle &mdash; spiritual "
            "practice pursued for the worldly aim of rebirth among the "
            "gods &mdash; receives a fitting counterpart in this "
            "chapter's remedy: right effort's own formula names "
            "striving toward skillful qualities for their own "
            "development, not for any further gain, a direct answer to "
            "practice corrupted by ulterior motive."]),
        ("Two chapters, one lesson about remedies", [
            "Read together, ch.7 and ch.8 make a point neither makes "
            "alone: identical obstacles, from ordinary broken precepts "
            "to the subtlest corruption of practice itself, can be met "
            "by more than one canonical approach. The source's own "
            "colophon closes this chapter, numbering it "
            "&lsquo;third&rsquo; within the Second Fifty &mdash; the "
            "same internally restarted numbering already met closing "
            "ch.6, distinct from the continuous 1&ndash;10 count used "
            "in each discourse's own header."]),
    ],
    terms=[
        ("cetaso vinibandhā",
         "&ldquo;shackles of the heart&rdquo; &mdash; the identical "
         "five items already met closing ch.7 at AN 9.72."),
        ("cattāro sammappadhānā",
         "&ldquo;the four right efforts&rdquo; &mdash; this chapter's "
         "remedy, closing it exactly as it opened at AN 9.73."),
        ("iminā sīlena vā vatena vā tapena vā brahmacariyena vā "
         "devo vā bhavissāmi devaññataro vā",
         "&ldquo;by this precept or observance or fervent austerity or "
         "spiritual practice, may I become one of the gods&rdquo; "
         "&mdash; the fifth shackle, practice corrupted by worldly "
         "aim, unchanged from AN 9.72."),
        ("dasamaṁ",
         "&ldquo;tenth&rdquo; &mdash; the bare ordinal closing this "
         "discourse, marking its place as the tenth and final discourse "
         "in this chapter."),
        ("sammappadhānavaggo tatiyo",
         "&ldquo;Sammappadhānavagga, third&rdquo; &mdash; the source's "
         "own colophon, restarting the chapter count for the Second "
         "Fifty rather than continuing the running 1&ndash;10 header "
         "numbering, the same pattern already noted closing ch.6."),
    ],
    text_intro=(
        "The discourse in full: the same five shackles of the heart as "
        "AN 9.72, now answered by the four right efforts. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five shackles of the heart"),
        ("p", "&sect;1", "an9.82:1.1-1.4"),
        ("h3", "Four right efforts"),
        ("p", "&sect;2", "an9.82:2.1-2.7"),
    ],
    quiz=[
        {"q": "How does this discourse's obstacle-list compare to AN "
              "9.72's?",
         "opts": [
             "Entirely different content",
             "Word-for-word identical — the same five shackles closing "
             "ch.7",
             "A shortened version",
             "A contradiction of AN 9.72"],
         "correct": 1,
         "expl": "The obstacle stays the same across both chapters; "
                 "only the remedy differs."},
        {"q": "What is the fifth and most pointed shackle?",
         "opts": [
             "Ordinary greed for food",
             "Spiritual practice pursued for the worldly aim of "
             "rebirth among the gods",
             "Fear of death",
             "Doubt about the teaching"],
         "correct": 1,
         "expl": "Practice itself corrupted by an ulterior motive, "
                 "unchanged from AN 9.72."},
        {"q": "According to the guide, how does right effort's formula "
              "specifically answer this fifth shackle?",
         "opts": [
             "It doesn't address it at all",
             "Right effort strives toward skillful qualities for their "
             "own development, not for further gain — a direct answer "
             "to practice pursued for worldly reward",
             "Right effort ignores spiritual motivation entirely",
             "Right effort only addresses physical obstacles"],
         "correct": 1,
         "expl": "A fitting counterpart between this specific obstacle "
                 "and this chapter's chosen remedy."},
        {"q": "What lesson do ch.7 and ch.8 make together, according to "
              "the guide?",
         "opts": [
             "That mindfulness meditation is inferior to right effort",
             "That identical obstacles can be met by more than one "
             "canonical approach",
             "That the obstacle-lists themselves were mistaken",
             "That right effort should replace mindfulness meditation "
             "entirely"],
         "correct": 1,
         "expl": "A lesson neither chapter makes alone, visible only "
                 "when read together."},
        {"q": "What does the source's own colophon number this chapter, "
              "and what pattern does this match?",
         "opts": [
             "Eighth, matching the continuous header numbering",
             "&lsquo;Third,&rsquo; restarting the count for the Second "
             "Fifty — the same pattern already noted closing ch.6",
             "First, contradicting all earlier chapters",
             "No colophon exists for this chapter"],
         "correct": 1,
         "expl": "An internally restarted numbering distinct from each "
                 "discourse's own continuous header count."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching AN 9.72's closing "
                 "of ch.7."},
    ],
    marginalia=[
        ("The same five shackles", [
            "sensual pleasure, body,",
            "form, comfort, sleep, and rebirth",
            "as a god &mdash; identical",
        ]),
        ("Effort answers motive", [
            "striving for its own",
            "sake, not for reward &mdash;",
            "a fitting counter",
        ]),
        ("Two remedies, one lesson", [
            "mindfulness, then effort &mdash;",
            "the same ten obstacles,",
            "met more than one way",
        ]),
        ("Cross-references", [
            "AN 9.72 &middot; the identical obstacle-list, there "
            "answered by mindfulness meditation",
            "AN 9.74&ndash;81 &middot; previous",
            "AN 9.83 &middot; next, opening ch.9, Iddhipadavagga",
        ]),
    ],
    further=[
        '<a href="%s/an9.82/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.72.html">AN 9.72 &middot; Shackles of the Heart</a> &mdash; the '
        "identical obstacle-list, there answered by mindfulness meditation.",
        '<a href="an-9.74-81.html">AN 9.74&ndash;81</a> &mdash; previous.',
    ],
)


# --------------------------------------------------------------------------- #
# ch.9 — Iddhipadavagga (AN 9.83-92). The third and final chapter in this
# three-chapter series (ch.7-9) reusing the identical ten obstacle-lists
# with a third substituted remedy, the four bases of psychic power. The
# source's own closing uddāna verse at AN 9.92 explicitly notes the parallel
# across all three chapters.
# --------------------------------------------------------------------------- #
VAGGA_9 = "<em>Iddhipadavagga</em> &mdash; the ninth chapter of the Nines"


# --------------------------------------------------------------------------- #
# AN 9.83 — Sekhasutta (Bases of Psychic Power version)
# --------------------------------------------------------------------------- #
page(
    83, "Sekha", "Weaknesses in Training and the Bases of Psychic Power",
    vagga=VAGGA_9,
    meta_title=("AN 9.83 — Weaknesses in Training and the Bases of "
                "Psychic Power | Ru-Yi Meditation Center"),
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the discourse opening this chapter — the third and final "
        "remedy substituted for ch.7's identical obstacle-lists, the "
        "four bases of psychic power. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same five weaknesses as AN 9.63 and AN 9.73, now "
                 "answered by the four bases of psychic power"),
        ("Length", "~1 minute to read"),
        ("A third and final remedy", "This chapter completes a three-"
         "part series (ch.7-9) applying three different canonical "
         "remedies to the identical ten obstacle-lists"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, opening the last chapter in this "
                       "project's clearest three-way structural "
                       "parallel"),
    ],
    why=(
        "The same five weaknesses opening ch.7 and ch.8 &mdash; "
        "killing, stealing, sexual misconduct, lying, and intoxicants "
        "&mdash; recur a third time, now given up by developing the "
        "four bases of psychic power: immersion born of enthusiasm, "
        "energy, mental development, and inquiry, each with active "
        "effort."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five weaknesses in training, a mendicant "
            "should develop the four bases of psychic power: immersion "
            "due to enthusiasm, energy, mental development, and "
            "inquiry, each accompanied by active effort."]),
        ("The third leg of a deliberate three-part series", [
            "With this discourse, this project meets the third and "
            "final remedy applied to the identical opening obstacle "
            "across three consecutive chapters: mindfulness meditation "
            "at AN 9.63, right effort at AN 9.73, and now the bases of "
            "psychic power &mdash; the same structural design confirmed "
            "explicitly by the source's own closing verse at AN 9.92, "
            "which names all three remedies together as intentionally "
            "parallel."]),
        ("Four bases, each pairing a quality with immersion", [
            "The four bases of psychic power name four distinct roads "
            "into the same immersion: enthusiasm (chanda), energy "
            "(vīriya), mental development or the mind itself (citta), "
            "and inquiry or investigation (vīmaṁsā), each producing "
            "immersion through active striving rather than through "
            "observation (as with mindfulness) or effort alone (as "
            "with right effort)."]),
        ("A remedy this project has met before, in a different role", [
            "The four bases of psychic power already appeared at AN "
            "9.35's culmination, among the six higher knowledges a "
            "pliable mind makes accessible after mastering all nine "
            "progressive attainments &mdash; there as an outcome of "
            "deep meditative mastery, here as a direct remedy for "
            "everyday ethical weakness, a striking range for the same "
            "fourfold practice."]),
    ],
    terms=[
        ("cattāro iddhipādā",
         "&ldquo;the four bases of psychic power&rdquo; &mdash; this "
         "chapter's own remedy, the third substituted for ch.7's four "
         "kinds of mindfulness meditation."),
        ("chandasamādhipadhānasaṅkhārasamannāgataṁ iddhipādaṁ",
         "&ldquo;the basis of psychic power that has immersion due to "
         "enthusiasm, and active effort&rdquo; &mdash; the first of the "
         "four bases."),
        ("vīriyasamādhi, cittasamādhi",
         "&ldquo;immersion due to energy... due to mental "
         "development&rdquo; &mdash; the second and third bases, each "
         "sharing the same active-effort structure as the first."),
        ("vīmaṁsāsamādhipadhānasaṅkhārasamannāgataṁ iddhipādaṁ",
         "&ldquo;the basis of psychic power that has immersion due to "
         "inquiry, and active effort&rdquo; &mdash; the fourth and "
         "final basis, closing the formula."),
        ("iddhividhā",
         "&ldquo;psychic power&rdquo; &mdash; the attainment these "
         "four bases lead toward, already named among the six higher "
         "knowledges at AN 9.35."),
    ],
    text_intro=(
        "The discourse in full: five weaknesses, and the four bases of "
        "psychic power given as their remedy. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Five weaknesses in training"),
        ("p", "&sect;1", "an9.83:1.1-1.4"),
        ("h3", "Four bases of psychic power"),
        ("p", "&sect;2", "an9.83:2.1-2.7"),
    ],
    quiz=[
        {"q": "How does this discourse's obstacle-list compare to AN "
              "9.63 and AN 9.73?",
         "opts": [
             "Entirely different content each time",
             "Identical across all three — the same five weaknesses, "
             "with a different remedy substituted each time",
             "This discourse has twice as many items",
             "This discourse contradicts the earlier two"],
         "correct": 1,
         "expl": "The third leg of a deliberate three-chapter parallel."},
        {"q": "What third remedy does this chapter apply?",
         "opts": [
             "The six higher knowledges",
             "The four bases of psychic power: enthusiasm, energy, "
             "mental development, and inquiry",
             "The four noble truths",
             "The nine progressive attainments"],
         "correct": 1,
         "expl": "Completing a series alongside mindfulness meditation "
                 "and right effort."},
        {"q": "According to the guide, how does the source itself "
              "confirm this three-chapter parallel is intentional?",
         "opts": [
             "It doesn't; the parallel is only the guide's own "
             "observation",
             "The closing verse at AN 9.92 names all three remedies "
             "together explicitly",
             "Each chapter contradicts the others",
             "The source never mentions the other two chapters"],
         "correct": 1,
         "expl": "A deliberate structural design, acknowledged in the "
                 "source's own closing uddāna."},
        {"q": "Where has this project already met the four bases of "
              "psychic power in a different role?",
         "opts": [
             "Nowhere before this discourse",
             "AN 9.35's culmination, among the six higher knowledges a "
             "pliable mind makes accessible",
             "Only in a completely unrelated nipāta",
             "At AN 9.1, the opening discourse"],
         "correct": 1,
         "expl": "There as an outcome of deep meditative mastery, here "
                 "as a remedy for everyday ethical weakness."},
        {"q": "What distinguishes each of the four bases from one "
              "another?",
         "opts": [
             "Nothing; they are identical",
             "Each pairs a different quality — enthusiasm, energy, "
             "mental development, inquiry — with the same immersion "
             "and active effort",
             "Each targets a different sense organ",
             "Each is aimed at a different obstacle-list"],
         "correct": 1,
         "expl": "Four distinct roads into the same underlying "
                 "immersion."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, opening this chapter "
                 "without narrative frame."},
    ],
    marginalia=[
        ("A third remedy, same obstacle", [
            "mindfulness, effort, now",
            "psychic power's four bases &mdash;",
            "the same five weaknesses",
        ]),
        ("Enthusiasm, energy, mind, inquiry", [
            "four roads to the same",
            "immersion, each paired",
            "with active effort",
        ]),
        ("A remedy in two roles", [
            "at AN 9.35, an outcome;",
            "here, applied directly",
            "to ordinary weakness",
        ]),
        ("Cross-references", [
            "AN 9.63, AN 9.73 &middot; the identical obstacle-list "
            "under two earlier remedies",
            "AN 9.35 &middot; the four bases of psychic power in a "
            "different role",
            "AN 9.82 &middot; previous chapter's closing page",
            "AN 9.84&ndash;91 &middot; next, pointing back to ch.7's "
            "content",
        ]),
    ],
    further=[
        '<a href="%s/an9.83/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.63.html">AN 9.63 &middot; Weaknesses in Training and Mindfulness '
        "Meditation</a> &mdash; the identical obstacle-list, under the first of "
        "three remedies.",
        '<a href="an-9.82.html">AN 9.82 &middot; Shackles of the Heart</a> &mdash; previous.',
        '<a href="an-9.84-91.html">AN 9.84&ndash;91</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 9.84-91 — the second merged page pointing back to ch.7's own content
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-9.84-91",
    "index_pali": "(untitled)",
    "nav_title": "Hindrances, Etc.",
    "source": "an9/an9.84-91",
    "crumb": "AN 9.84&ndash;91",
    "meta_title": "AN 9.84–91 — Hindrances, Etc. | Ru-Yi Meditation Center",
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for "
        "this merged page — the second in this project pointing back "
        "to ch.7's own content, this time with the four bases of "
        "psychic power substituted throughout. From Ru-Yi Meditation "
        "Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 9.84&ndash;91",
    "title": "Hindrances, Etc.",
    "subtitle": "<em>Untitled in the source</em> &mdash; %s, continued" % VAGGA_9,
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single instruction, identical in kind to AN 9.74-81, "
                 "pointing back to ch.7's own content"),
        ("Length", "A few seconds to read the instruction itself"),
        ("The second instance of this compression type", "The same "
         "&lsquo;tell in full as in the chapter on mindfulness "
         "meditation&rsquo; instruction already met at AN 9.74-81, now "
         "closing this project's third and final application of it"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "trivial to read the instruction itself"),
    ],
    "why": (
        "Standing for eight separate discourses (AN 9.84 through AN "
        "9.91), this page repeats AN 9.74-81's exact instruction "
        "&mdash; &lsquo;tell in full as in the chapter on mindfulness "
        "meditation&rsquo; &mdash; directing the reciter back to ch.7's "
        "eight middle obstacle-lists once more, this time paired with "
        "the four bases of psychic power."),
    "guide": [
        ("The teaching in one sentence", [
            "The same eight obstacle-lists given in full at AN 9.64 "
            "through AN 9.71 are each given up by developing the four "
            "bases of psychic power, exactly as AN 9.83 already showed "
            "for the first obstacle-list shared across all three "
            "chapters."]),
        ("The identical instruction, a second time", [
            "This page's own surviving text is word-for-word the same "
            "instruction already met at AN 9.74-81: &lsquo;tell in full "
            "as in the chapter on mindfulness meditation.&rsquo; The "
            "source doesn't even vary its own pointer between the two "
            "occasions, trusting the same substitution logic each time."]),
        ("Two merged pages, three chapters, one shared source", [
            "Both this page and AN 9.74-81 point to the identical "
            "eight discourses in ch.7 &mdash; neither points to the "
            "other, and neither reconstructs the content itself. Ch.7's "
            "AN 9.64 through AN 9.71 function as this project's sole "
            "on-record version of these eight obstacle-lists, now "
            "referenced twice over rather than written out three "
            "separate times."]),
        ("Closing in on the third chapter's own final discourse", [
            "With this page, only AN 9.92 remains to close ch.9 "
            "&mdash; the third and final &lsquo;shackles of the "
            "heart&rsquo; discourse in this three-chapter series, and "
            "the point at which the source's own closing verse "
            "explicitly names all three parallel chapters together."]),
    ],
    "terms": [
        ("tesaṁyeva vitthāro satipaṭṭhānavaggasadisova kātabbo",
         "&ldquo;tell in full as in the chapter on mindfulness "
         "meditation&rdquo; &mdash; the identical instruction already "
         "met at AN 9.74-81, repeated here without variation."),
        ("cattāro iddhipādā",
         "&ldquo;the four bases of psychic power&rdquo; &mdash; the "
         "one substitution this instruction asks the reciter to make "
         "throughout, in place of the four kinds of mindfulness "
         "meditation."),
        ("nīvaraṇā, kāmaguṇā, upādānakkhandhā",
         "&ldquo;hindrances, sensual stimulation, grasping "
         "aggregates&rdquo; &mdash; the first three of the eight "
         "obstacle-lists this page stands for, given in full at AN "
         "9.64-66."),
        ("orambhāgiyāni saṁyojanāni, gatiyo, macchariyāni, "
         "uddhambhāgiyāni saṁyojanāni, cetokhilā",
         "&ldquo;lower fetters, destinations, stinginess, higher "
         "fetters, hard-heartedness&rdquo; &mdash; the remaining five "
         "obstacle-lists this page stands for, given in full at AN "
         "9.67-71."),
        ("iddhipādavaggo",
         "&ldquo;Iddhipādavagga&rdquo; &mdash; this chapter's own "
         "name, naming the third and final remedy in this three-"
         "chapter series."),
    ],
    "text_intro": (
        "The discourse exactly as it survives in the source: the same "
        "instruction already met at AN 9.74-81, pointing back to ch.7's "
        "own content once more. Nothing has been added or "
        "reconstructed. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "The instruction, in full"),
        ("p", "&sect;1", "an9.84-91:1.1-1.1"),
    ],
    "quiz": [
        {"q": "How does this page's instruction compare to AN "
              "9.74-81's?",
         "opts": [
             "Entirely different wording",
             "Word-for-word identical: &lsquo;tell in full as in the "
             "chapter on mindfulness meditation&rsquo;",
             "This page gives full detail instead",
             "This page points to a different chapter"],
         "correct": 1,
         "expl": "The same pointer, repeated without variation for the "
                 "second time in this project."},
        {"q": "What remedy does this page's instruction imply, "
              "replacing ch.7's mindfulness meditation?",
         "opts": [
             "The four right efforts, as at AN 9.74-81",
             "The four bases of psychic power, this chapter's own "
             "remedy",
             "No remedy at all",
             "A completely new, unnamed remedy"],
         "correct": 1,
         "expl": "The substitution changes per chapter even though the "
                 "instruction's wording doesn't."},
        {"q": "How many times, across this project so far, do ch.7's "
              "eight middle obstacle-lists get written out in full?",
         "opts": [
             "Three times, once per chapter",
             "Once — at AN 9.64 through AN 9.71 — with both AN 9.74-81 "
             "and this page pointing back to that single source",
             "Never; the content is lost entirely",
             "Eight separate times"],
         "correct": 1,
         "expl": "Ch.7 functions as the sole on-record version, "
                 "referenced twice rather than repeated."},
        {"q": "What remains after this page, closing ch.9?",
         "opts": [
             "Nothing; the chapter ends here",
             "AN 9.92, the third and final &lsquo;shackles of the "
             "heart&rsquo; discourse in this three-chapter series",
             "A return to ch.7's opening discourse",
             "Ten further discourses"],
         "correct": 1,
         "expl": "The chapter's closer, where the source's own verse "
                 "names all three parallel chapters together."},
        {"q": "What does this page's guide avoid doing, consistent with "
              "AN 9.74-81?",
         "opts": [
             "Naming the obstacle-lists at all",
             "Reconstructing all eight discourses' full text under the "
             "new remedy, since the source itself declines to write "
             "them out",
             "Explaining the instruction",
             "Pointing readers to ch.7"],
         "correct": 1,
         "expl": "Consistent with this project's rule against inventing "
                 "text not in the source."},
        {"q": "What eight obstacle-lists does this page stand for?",
         "opts": [
             "Eight entirely new lists",
             "The same eight given in full at AN 9.64 through AN 9.71",
             "Only stinginess, repeated eight times",
             "Eight kinds of wrong view"],
         "correct": 1,
         "expl": "Identical to what AN 9.74-81 already pointed to, now "
                 "referenced a second time."},
    ],
    "marginalia": [
        ("The same pointer, again", [
            "&ldquo;tell it as in the",
            "mindfulness chapter&rdquo; &mdash;",
            "unchanged, a second time",
        ]),
        ("One source, twice referenced", [
            "ch.7's eight lists, written",
            "out only once &mdash;",
            "pointed to here and before",
        ]),
        ("Nearing the series' close", [
            "one discourse remains &mdash;",
            "where the source itself names",
            "all three chapters, paired",
        ]),
        ("Cross-references", [
            "AN 9.64&ndash;71 &middot; ch.7's full treatment of these "
            "same eight obstacle-lists",
            "AN 9.74&ndash;81 &middot; the identical instruction, first "
            "met in ch.8",
            "AN 9.83 &middot; previous",
            "AN 9.92 &middot; next, Shackles of the Heart, closing this "
            "chapter",
        ]),
    ],
    "further": [
        '<a href="%s/an9.84-91/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.64.html">AN 9.64 &middot; Hindrances</a> &mdash; ch.7’s full '
        "treatment of the first obstacle-list this page stands for.",
        '<a href="an-9.74-81.html">AN 9.74&ndash;81</a> &mdash; the identical instruction, '
        "first met in ch.8.",
        '<a href="an-9.83.html">AN 9.83 &middot; Weaknesses in Training and the Bases of '
        "Psychic Power</a> &mdash; previous.",
        '<a href="an-9.92.html">AN 9.92 &middot; Shackles of the Heart</a> &mdash; next.',
    ],
})


# --------------------------------------------------------------------------- #
# AN 9.92 — Cetasovinibandhasutta (Bases of Psychic Power version) — closes
# ch.9 Iddhipadavagga and the three-chapter ch.7-9 series
# --------------------------------------------------------------------------- #
page(
    92, "Cetasovinibandha", "Shackles of the Heart",
    vagga=VAGGA_9,
    meta_title="AN 9.92 — Shackles of the Heart | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the discourse closing this chapter and its three-chapter "
        "series — the identical five shackles, now answered by the "
        "four bases of psychic power, with the source's own verse "
        "naming all three parallel chapters together. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Five shackles of the heart, then the four bases of "
                 "psychic power given in full as the remedy"),
        ("Length", "~2 minutes to read"),
        ("Closing three chapters at once", "This discourse closes "
         "<em>Iddhipadavagga</em>, and the source's own uddāna verse "
         "explicitly names mindfulness meditation, right effort, and "
         "the bases of psychic power together as one deliberate series"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "substantial, closing this three-chapter series "
                       "on the most pointed shared obstacle-list"),
    ],
    why=(
        "The same five shackles of the heart that closed ch.7 and ch.8 "
        "&mdash; unresolved greed for sensual pleasures, the body, "
        "physical form, comfort and sleep, and rebirth among the gods "
        "sought through spiritual practice &mdash; recur a third and "
        "final time, given up by developing the four bases of psychic "
        "power, and the source's own closing verse confirms that all "
        "three chapters were meant to be read as one deliberate "
        "sequence."),
    guide=[
        ("The teaching in one sentence", [
            "To give up the five shackles of the heart, a mendicant "
            "should develop the four bases of psychic power: immersion "
            "due to enthusiasm, energy, mental development, and "
            "inquiry, each with active effort &mdash; the third and "
            "final remedy in a deliberate three-chapter series."]),
        ("The source's own confirmation of the pattern", [
            "Unlike the more inferential cross-referencing this project "
            "has drawn between other discourses, the parallel across "
            "ch.7, ch.8, and ch.9 is confirmed by the text itself: this "
            "discourse's own closing verse states, in effect, that "
            "&lsquo;just as the mindfulness meditations, so the [right] "
            "efforts, and likewise the four bases of psychic power "
            "should be combined&rsquo; with the same obstacle-lists "
            "&mdash; an explicit acknowledgment, rare in this "
            "collection, of a structural design spanning three separate "
            "chapters."]),
        ("Three chapters, one lesson made explicit", [
            "What earlier discourses in this project could only "
            "demonstrate through repetition, this closing verse states "
            "outright: the identical ten obstacles this project has "
            "traced across thirty discourses (AN 9.63 through AN 9.92) "
            "can each be met by mindfulness meditation, by right "
            "effort, or by the bases of psychic power, three genuinely "
            "different approaches converging on the same ten targets."]),
        ("Closing the chapter, and its own colophon", [
            "This discourse closes <em>Iddhipadavagga</em>, the ninth "
            "chapter; the source's own colophon numbers it "
            "&lsquo;fourth&rsquo; within the Second Fifty, continuing "
            "the restarted numbering already noted closing ch.6 and "
            "ch.8. One chapter remains before this nipāta's own great "
            "closing peyyāla begins."]),
    ],
    terms=[
        ("cetaso vinibandhā",
         "&ldquo;shackles of the heart&rdquo; &mdash; the identical "
         "five items already met closing ch.7 and ch.8."),
        ("cattāro iddhipādā",
         "&ldquo;the four bases of psychic power&rdquo; &mdash; the "
         "third and final remedy in this chapter series, closing it "
         "exactly as it opened at AN 9.83."),
        ("yatheva satipaṭṭhānā, padhānā caturopi ca, cattāro "
         "iddhipādā ca, tatheva sampayojaye",
         "&ldquo;just as the mindfulness meditations, so the efforts, "
         "and likewise the four bases of psychic power should be "
         "combined&rdquo; &mdash; the source's own closing verse, "
         "explicitly naming the three-chapter parallel."),
        ("dasamaṁ",
         "&ldquo;tenth&rdquo; &mdash; the bare ordinal closing this "
         "discourse, marking its place as the tenth and final "
         "discourse in this chapter."),
        ("iddhipādavaggo catuttho",
         "&ldquo;Iddhipādavagga, fourth&rdquo; &mdash; the source's "
         "own colophon, continuing the Second Fifty's restarted chapter "
         "numbering already noted closing ch.6 and ch.8."),
    ],
    text_intro=(
        "The discourse in full: the same five shackles of the heart as "
        "AN 9.72 and AN 9.82, now answered by the four bases of "
        "psychic power. The source's own closing colophon and uddāna "
        "verse are untranslated in the English and are described "
        "rather than quoted here. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "Five shackles of the heart"),
        ("p", "&sect;1", "an9.92:1.1-1.4"),
        ("h3", "Four bases of psychic power"),
        ("p", "&sect;2", "an9.92:2.1-2.7"),
    ],
    quiz=[
        {"q": "How does this discourse's obstacle-list compare to AN "
              "9.72 and AN 9.82's?",
         "opts": [
             "Entirely different content",
             "Word-for-word identical across all three — the same "
             "five shackles closing all three chapters",
             "A shortened version",
             "A contradiction of the earlier two"],
         "correct": 1,
         "expl": "The same obstacle-list closing all three chapters in "
                 "this deliberate series."},
        {"q": "How does this discourse's closing verse confirm the "
              "three-chapter parallel, unlike most cross-references in "
              "this project?",
         "opts": [
             "It doesn't confirm anything explicitly",
             "The source's own uddāna verse explicitly states that "
             "mindfulness meditation, effort, and the bases of psychic "
             "power should all be &lsquo;combined&rsquo; with the same "
             "obstacles",
             "It contradicts the parallel entirely",
             "It only mentions two of the three chapters"],
         "correct": 1,
         "expl": "A rare, explicit textual confirmation of a design "
                 "this project usually has to infer."},
        {"q": "How many discourses total does this three-chapter series "
              "span?",
         "opts": [
             "Ten discourses",
             "Thirty discourses, AN 9.63 through AN 9.92",
             "Five discourses",
             "The entire Second Fifty"],
         "correct": 1,
         "expl": "Three chapters of ten discourses each, sharing the "
                 "identical ten obstacle-lists."},
        {"q": "What does the source's own colophon number this "
              "chapter, continuing which pattern?",
         "opts": [
             "First, breaking the established pattern",
             "&lsquo;Fourth,&rsquo; continuing the Second Fifty's "
             "restarted chapter numbering already noted closing ch.6 "
             "and ch.8",
             "Ninth, matching the continuous header numbering",
             "No colophon exists for this discourse"],
         "correct": 1,
         "expl": "The same internally restarted numbering met at each "
                 "chapter's close in the Second Fifty."},
        {"q": "What remains after this chapter closes?",
         "opts": [
             "Nothing; AN 9 ends here",
             "One further chapter before this nipāta's own great "
             "closing peyyāla begins",
             "A return to the First Fifty",
             "Ten more chapters"],
         "correct": 1,
         "expl": "The final chapter, closing the entire Book of the "
                 "Nines."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare doctrinal teaching, matching AN 9.72 and AN "
                 "9.82's closings of the earlier two chapters."},
    ],
    marginalia=[
        ("The same five shackles, thrice", [
            "sensual pleasure, body,",
            "form, comfort, rebirth as a god &mdash;",
            "closing all three chapters",
        ]),
        ("The source names its own design", [
            "&ldquo;just as mindfulness,",
            "so effort, so the bases &mdash;",
            "combined the same way&rdquo;",
        ]),
        ("Thirty discourses, one lesson", [
            "ten obstacles, met by",
            "three different roads &mdash;",
            "converging as one",
        ]),
        ("Cross-references", [
            "AN 9.72, AN 9.82 &middot; the identical obstacle-list "
            "closing the two earlier chapters in this series",
            "AN 9.84&ndash;91 &middot; previous",
            "AN 9.93 &middot; next, opening ch.10, Rāgapeyyāla",
        ]),
    ],
    further=[
        '<a href="%s/an9.92/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-9.72.html">AN 9.72 &middot; Shackles of the Heart</a> &mdash; the '
        "identical obstacle-list, closing the first of three chapters.",
        '<a href="an-9.82.html">AN 9.82 &middot; Shackles of the Heart</a> &mdash; the '
        "identical obstacle-list, closing the second of three chapters.",
        '<a href="an-9.84-91.html">AN 9.84&ndash;91</a> &mdash; previous.',
    ],
)
