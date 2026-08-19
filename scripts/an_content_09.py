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
