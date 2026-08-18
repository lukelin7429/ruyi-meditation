# -*- coding: utf-8 -*-
"""Sattaka Nipāta — The Sevens. One discourse per page, from AN 7.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Sattaka Nipāta — The Sevens"
# an-7.6.html was published before this series began working in order, in the
# earlier eighteen-page selection; it is listed in the index by INDEX_EXTRA
# and is not regenerated here. HEAD points at the last page the Sixes module
# reached. TAIL points at the nearest already-published page beyond the
# Sevens -- an-8.30.html, from the same earlier selection -- until the
# Eights module exists and TAIL can move to its own first page.
HEAD = ("an-6.170-649.html", "AN 6.170&ndash;649 &middot; Insight into Hate, and So On")
TAIL = ("an-8.30.html", "AN 8.30 &middot; Anuruddha and the Great Thoughts")
INDEX_EXTRA = [
    ("an-7.6", "Vitthatadhana", "Wealth in Detail"),
]

PAGES = []

VAGGA_1 = "<em>Dhanavagga</em> &mdash; the first chapter of the Sevens"
SETTING_1 = ("Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery; "
             "stated at the head of AN 7.1 and understood to hold across the chapter "
             "unless a fresh setting is given")
SETTING_NONE = "None stated in the source"
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Sevens."""
    d = {
        "slug": "an-7.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an7/an7.%d" % num,
        "crumb": "AN 7.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 7.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 7.1 — Paṭhamapiyasutta
# --------------------------------------------------------------------------- #
page(
    1, "Paṭhamapiya", "Pleasing (1st)",
    vagga=VAGGA_1,
    meta_title="AN 7.1 — Pleasing (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamapiyasutta, opening the Book of the Sevens with seven qualities that make "
        "a mendicant disliked or liked by their spiritual companions. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "Two matched seven-item lists, cause and its direct reversal, opening a new "
                 "nipāta with a full narrative frame"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of material desire and ethical shame as decisive "
                              "for a mendicant's standing recurs widely across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "opening the Sevens with the collection's now-familiar full narrative "
                       "opening formula"),
    ],
    why=(
        "The Book of the Sevens opens exactly as the Sixes did: a full narrative frame "
        "&mdash; &ldquo;So I have heard&rdquo; &mdash; at Sāvatthī, in Jeta&rsquo;s Grove, "
        "before the Buddha addresses the mendicants directly. What follows is a bare pair of "
        "seven-item lists: desiring material things, honor, and status, lacking conscience "
        "and prudence, and having corrupt wishes and wrong view make a mendicant disliked; "
        "their seven reversals make one liked."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who desires material things, honor, and status, lacks conscience "
            "and prudence, and has corrupt wishes and wrong view is disliked by their "
            "spiritual companions; the seven direct opposites make a mendicant liked."]),
        ("A new nipāta, opening with its full formula", [
            "Where individual chapters within the Sixes often opened straight into a bare "
            "teaching, this discourse gives the complete traditional frame &mdash; the "
            "narrator's own '&ldquo;so I have heard,&rdquo;' the setting, and the address to "
            "the mendicants &mdash; the standard way a new nipāta's very first discourse is "
            "presented in this literature, matching how the Sixes themselves opened at AN "
            "6.1."]),
        ("Seven items, not six", [
            "The core structure &mdash; a blocking list matched by its direct reversal "
            "&mdash; will be familiar from the entire Sixes collection just completed. What "
            "changes with this new nipāta is only the count: seven items instead of six, "
            "the numerical theme this entire book will develop discourse after discourse."]),
        ("Desire for status, before any conduct is named", [
            "The list opens not with an action but with a disposition: wanting material "
            "things, honor, and status. Only after naming this underlying desire does the "
            "list turn to conscience, prudence, and finally view &mdash; suggesting the "
            "chain of what makes a mendicant disliked begins in craving before it shows up "
            "in judgment or belief."]),
    ],
    terms=[
        ("lābhakāma, sakkārakāma, anavaññattikāma",
         "&ldquo;desiring material things, honor, and status&rdquo; &mdash; the first three "
         "blocking items, an underlying disposition rather than an action."),
        ("ahirika, anottappa",
         "&ldquo;lacking conscience, lacking prudence&rdquo; &mdash; the fourth and fifth "
         "items, terms already familiar from the Sixes."),
        ("pāpiccha, micchādiṭṭhi",
         "&ldquo;corrupt wishes, wrong view&rdquo; &mdash; the sixth and seventh items, "
         "closing the blocking list."),
        ("piya",
         "&ldquo;pleasing, dear&rdquo; &mdash; this discourse's own title term, the state "
         "its seven reversed qualities are said to produce."),
        ("sattaka",
         "&ldquo;a set of seven&rdquo; &mdash; the numerical theme of this entire nipāta, "
         "Sattaka Nipāta, the Book of the Sevens."),
    ],
    text_intro=(
        "The discourse in full: seven qualities that make a mendicant disliked, and their "
        "seven reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "an7.1:1.1-1.6"),
        ("h3", "Seven qualities that make a mendicant disliked"),
        ("p", "&sect;2", "an7.1:2.1-2.4"),
        ("h3", "Seven qualities that make a mendicant liked"),
        ("p", "&sect;3", "an7.1:3.1-3.4"),
    ],
    quiz=[
        {"q": "How does this discourse open, compared to many individual discourses within "
              "the Sixes?",
         "opts": [
             "With a bare formula and no setting, like most Sixes discourses",
             "With the full traditional frame — 'so I have heard,' the setting at Sāvatthī, "
             "and the address to the mendicants — matching how the Sixes themselves opened "
             "at AN 6.1",
             "With a dialogue between two mendicants",
             "With a deity's visit"],
         "correct": 1,
         "expl": "The standard way a new nipāta's first discourse is presented."},
        {"q": "What seven qualities make a mendicant disliked by their spiritual companions?",
         "opts": [
             "The five hindrances plus doubt and restlessness",
             "Desiring material things, honor, and status; lacking conscience and prudence; "
             "having corrupt wishes and wrong view",
             "The three poisons plus four more items",
             "The seven factors of awakening, negated"],
         "correct": 1,
         "expl": "Seven items, the numerical theme of this entire new book."},
        {"q": "What does the guide say opens the blocking list, before any conduct is named?",
         "opts": [
             "An act of physical violence",
             "An underlying disposition — desiring material things, honor, and status",
             "A specific broken precept",
             "A wrong meditative technique"],
         "correct": 1,
         "expl": "The chain of what makes a mendicant disliked begins in craving, before "
                 "judgment or belief."},
        {"q": "How does this discourse's core structure compare to the Sixes collection just "
              "completed?",
         "opts": [
             "Entirely different in form",
             "The same blocking-list-plus-reversal structure, familiar from the Sixes, only "
             "with seven items instead of six",
             "No structure at all — a narrative only",
             "A chain argument, unlike anything in the Sixes"],
         "correct": 1,
         "expl": "A familiar shape carried into a new numerical count."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "No setting is given"],
         "correct": 1,
         "expl": "The standard opening setting for this literature's collections."},
        {"q": "What does <em>piya</em>, this discourse's own title term, mean?",
         "opts": ["Disliked", "Pleasing, dear", "Powerful", "Wealthy"],
         "correct": 1,
         "expl": "The state the seven reversed qualities are said to produce."},
    ],
    marginalia=[
        ("Seven qualities disliked", [
            "desiring things, honor,",
            "status &middot; no conscience,",
            "prudence &middot; corrupt wishes, wrong view",
        ]),
        ("A new book begins", [
            "full narrative frame —",
            "'so I have heard' —",
            "matching AN 6.1's own opening",
        ]),
        ("Seven, not six", [
            "the same blocking/reversal",
            "shape as the Sixes,",
            "now with one more item each",
        ]),
        ("Cross-references", [
            "AN 6.170-649 &middot; previous nipāta, closing the Sixes",
            "AN 7.2 &middot; next, the same theme restated",
        ]),
    ],
    further=[
        '<a href="%s/an7.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.170-649.html">AN 6.170&ndash;649 &middot; Insight into Hate, and So '
        "On</a> &mdash; previous, closing the Sixes.",
        '<a href="an-7.2.html">AN 7.2 &middot; Pleasing (2nd)</a> &mdash; next, the same '
        "theme with a different closing pair of items.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.2 — Dutiyapiyasutta
# --------------------------------------------------------------------------- #
page(
    2, "Dutiyapiya", "Pleasing (2nd)",
    vagga=VAGGA_1,
    meta_title="AN 7.2 — Pleasing (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyapiyasutta, restating AN 7.1's first five items but closing on jealousy and "
        "stinginess rather than corrupt wishes and wrong view. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched seven-item lists, cause and its direct reversal, sharing five "
                 "of seven items with AN 7.1"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of jealousy and stinginess as a joint obstacle to "
                              "being liked recurs in related forms across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "sharing most of its content with AN 7.1 immediately before it"),
    ],
    why=(
        "AN 7.2 repeats AN 7.1's first five items exactly &mdash; desiring material things, "
        "honor, and status, lacking conscience and prudence &mdash; but closes on a "
        "different pair: jealousy and stinginess, rather than corrupt wishes and wrong "
        "view. A reader who assumes this is simply AN 7.1 restated would be missing the "
        "one deliberate substitution that gives this discourse its own content."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who desires material things, honor, and status, lacks conscience "
            "and prudence, and is jealous and stingy is disliked by their spiritual "
            "companions; the seven direct opposites make a mendicant liked."]),
        ("Five items shared, two substituted", [
            "Checked term by term against AN 7.1, this discourse's first five items are "
            "identical. Only the sixth and seventh change: jealousy (issā) and stinginess "
            "(macchariya) replace AN 7.1's corrupt wishes and wrong view &mdash; the same "
            "'shared frame, substituted closing pair' technique already met repeatedly "
            "across the Sixes, now carried into this new nipāta's very second discourse."]),
        ("From doctrinal error to interpersonal fault", [
            "AN 7.1's closing pair concerned corrupt wishes and wrong view &mdash; internal "
            "distortions of desire and belief. This discourse's closing pair, jealousy and "
            "stinginess, concerns something more immediately social: how a mendicant "
            "relates to what others have, and what they themselves are willing to share."]),
        ("A brief/elaborated pair itself, within Dhanavagga", [
            "AN 7.1 and 7.2 together form this chapter's own small pair of near-duplicate "
            "discourses, echoed by the two further near-duplicate pairs immediately "
            "following: AN 7.3/7.4 on the seven powers, and AN 7.5/7.6 on the seven kinds "
            "of wealth."]),
    ],
    terms=[
        ("lābhakāma, sakkārakāma, anavaññattikāma, ahirika, anottappa",
         "the same first five items as AN 7.1: desiring material things, honor, and status, "
         "and lacking conscience and prudence."),
        ("issā",
         "&ldquo;jealousy&rdquo; &mdash; the sixth item, replacing AN 7.1's corrupt "
         "wishes."),
        ("macchariya",
         "&ldquo;stinginess&rdquo; &mdash; the seventh and closing item, replacing AN 7.1's "
         "wrong view."),
        ("anissuka, amaccharī",
         "&ldquo;not jealous, not stingy&rdquo; &mdash; the reversal's sixth and seventh "
         "items."),
        ("piya",
         "&ldquo;pleasing, dear&rdquo; &mdash; this discourse's shared title term with AN "
         "7.1, the state its seven reversed qualities produce."),
    ],
    text_intro=(
        "The discourse in full: seven qualities that make a mendicant disliked, closing on "
        "jealousy and stinginess, and their reversal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven qualities that make a mendicant disliked"),
        ("p", "&sect;1", "an7.2:1.1-1.4"),
        ("h3", "Seven qualities that make a mendicant liked"),
        ("p", "&sect;2", "an7.2:2.1-2.4"),
    ],
    quiz=[
        {"q": "How many of this discourse's seven items are identical to AN 7.1's, checked "
              "term by term?",
         "opts": [
             "None — entirely different content",
             "Five — only the sixth and seventh items differ",
             "All seven are identical",
             "Only two items overlap"],
         "correct": 1,
         "expl": "The same shared-frame, substituted-closing-pair technique already "
                 "established across the Sixes."},
        {"q": "What two items close this discourse's blocking list, replacing AN 7.1's "
              "corrupt wishes and wrong view?",
         "opts": [
             "Laziness and negligence",
             "Jealousy and stinginess",
             "Doubt and restlessness",
             "The five hindrances"],
         "correct": 1,
         "expl": "A shift from doctrinal distortion to interpersonal fault."},
        {"q": "Is this discourse a repeat of AN 7.1, according to the guide?",
         "opts": [
             "Yes, word for word identical",
             "No — five items are shared, but the substituted sixth and seventh items give "
             "this discourse its own distinct content",
             "No — the two discourses share nothing at all",
             "Yes, except for the setting"],
         "correct": 1,
         "expl": "A deliberate substitution, not an accidental duplicate."},
        {"q": "What further near-duplicate pairs does this chapter contain, according to the "
              "guide?",
         "opts": [
             "None — AN 7.1/7.2 is the only such pair",
             "AN 7.3/7.4 on the seven powers, and AN 7.5/7.6 on the seven kinds of wealth",
             "Only pairs found later in the Second Fifty",
             "AN 7.8/7.9 only"],
         "correct": 1,
         "expl": "A chapter built partly from brief/elaborated or near-duplicate discourse "
                 "pairs."},
        {"q": "Is a setting stated for AN 7.2?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, unlike AN 7.1's full narrative opening."},
        {"q": "What does <em>macchariya</em> mean?",
         "opts": ["Jealousy", "Stinginess", "Wrong view", "Corrupt wishes"],
         "correct": 1,
         "expl": "The seventh and closing item on this discourse's blocking list."},
    ],
    marginalia=[
        ("Five items shared with 7.1", [
            "desiring things, honor,",
            "status &middot; no conscience,",
            "prudence — identical to AN 7.1",
        ]),
        ("Two items substituted", [
            "not corrupt wishes,",
            "wrong view — instead:",
            "jealousy and stinginess",
        ]),
        ("A social, not doctrinal, close", [
            "how a mendicant relates",
            "to others' possessions",
            "and their own willingness to share",
        ]),
        ("Cross-references", [
            "AN 7.1 &middot; previous, this discourse's near-duplicate companion",
            "AN 7.3 &middot; next, a shift to the seven powers",
        ]),
    ],
    further=[
        '<a href="%s/an7.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.1.html">AN 7.1 &middot; Pleasing (1st)</a> &mdash; previous, this '
        "discourse's near-duplicate companion.",
        '<a href="an-7.3.html">AN 7.3 &middot; Powers in Brief</a> &mdash; next, a shift to '
        "the seven powers, in brief.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.3 — Saṁkhittabalasutta
# --------------------------------------------------------------------------- #
page(
    3, "Saṁkhittabala", "Powers in Brief",
    vagga=VAGGA_1,
    meta_title="AN 7.3 — Powers in Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Saṁkhittabalasutta, naming the seven powers in brief, with a closing verse "
        "matched word for word by AN 7.4's elaborated version. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, named briefly, closing on verse — the shorter "
                 "half of a brief/elaborated pair with AN 7.4"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The seven powers (bala) as a standard set closely paralleling "
                              "the five spiritual faculties plus two further items recur "
                              "throughout the Chinese Āgamas and Abhidharma literature; this "
                              "reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, naming seven "
                       "terms without elaboration, closing on a memorable verse"),
    ],
    why=(
        "AN 7.3 names seven powers &mdash; faith, energy, conscience, prudence, "
        "mindfulness, immersion, and wisdom &mdash; bare, with no explanation of any one "
        "term, closing on a verse that restates the list in poetic form and ends on the "
        "striking image of &ldquo;liberation of the heart... like a lamp going out.&rdquo; "
        "AN 7.4, immediately following, will spell out every term this discourse leaves "
        "unexplained."),
    guide=[
        ("The teaching in one sentence", [
            "There are seven powers: faith, energy, conscience, prudence, mindfulness, "
            "immersion, and wisdom, empowering an astute mendicant to live happily and "
            "examine the teaching with wisdom."]),
        ("A brief half, deliberately withholding explanation", [
            "Unlike AN 7.4's fuller treatment, this discourse offers no definition for any "
            "of its seven terms &mdash; simply naming them, restating them in verse, and "
            "trusting the reader either to already know their meaning or to encounter the "
            "elaboration at the very next discourse."]),
        ("Five familiar terms, plus two shared with the five faculties", [
            "Saddhā (faith), viriya (energy), sati (mindfulness), samādhi (immersion), and "
            "paññā (wisdom) are five of the standard five spiritual faculties (indriya) "
            "already met throughout this series; this list replaces the faculties' own "
            "internal completeness with two further items, hiri (conscience) and ottappa "
            "(prudence), producing seven powers rather than five faculties."]),
        ("A closing image already familiar from this series", [
            "The verse's closing line, comparing the heart's liberation to &ldquo;a lamp "
            "going out&rdquo; (padīpasseva nibbānaṁ), uses the same root image, nibbāna as "
            "an extinguished flame, that has run throughout this collection's treatment of "
            "extinguishment since the Sixes."]),
    ],
    terms=[
        ("bala",
         "&ldquo;power&rdquo; &mdash; this discourse's own term for its seven-item list, "
         "closely related to but distinct from the five spiritual faculties (indriya)."),
        ("saddhā, vīriya, sati, samādhi, paññā",
         "&ldquo;faith, energy, mindfulness, immersion, wisdom&rdquo; &mdash; five of this "
         "list's seven items, matching the standard five spiritual faculties by name."),
        ("hiri, ottappa",
         "&ldquo;conscience, prudence&rdquo; &mdash; the two further items distinguishing "
         "this seven-item list from the five-item faculties."),
        ("padīpasseva nibbānaṁ",
         "&ldquo;like a lamp going out&rdquo; &mdash; the verse's closing image for the "
         "heart's liberation, the same extinguished-flame image recurring throughout this "
         "collection's treatment of nibbāna."),
        ("saṁkhitta, vitthata",
         "&ldquo;in brief, in detail&rdquo; &mdash; the terms distinguishing this discourse "
         "from AN 7.4, its elaborated companion."),
    ],
    text_intro=(
        "The discourse in full: the seven powers named in brief, closing on verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "an7.3:1.1-1.6"),
        ("h3", "The seven powers, named in brief"),
        ("p", "&sect;2", "an7.3:2.1-2.6"),
        ("h3", "The closing verse"),
        ("p", "&sect;3", "an7.3:3.1-3.4"),
    ],
    quiz=[
        {"q": "What seven powers does this discourse name?",
         "opts": [
             "The five hindrances plus two more",
             "Faith, energy, conscience, prudence, mindfulness, immersion, and wisdom",
             "The seven factors of awakening",
             "The three poisons plus four more"],
         "correct": 1,
         "expl": "Seven powers, five of which match the standard five spiritual faculties by "
                 "name."},
        {"q": "How does this discourse treat its seven terms, unlike AN 7.4?",
         "opts": [
             "With full definitions for each term",
             "Bare — no explanation of any term is offered, unlike AN 7.4's fuller treatment "
             "immediately following",
             "With only three of the seven terms defined",
             "Identically to AN 7.4 in every respect"],
         "correct": 1,
         "expl": "The shorter half of a brief/elaborated pair."},
        {"q": "How does this seven-item list relate to the five spiritual faculties "
              "(indriya)?",
         "opts": [
             "No relationship at all",
             "Five of the seven terms — faith, energy, mindfulness, immersion, wisdom — "
             "match the five faculties by name, with conscience and prudence added",
             "All seven terms are entirely different from the five faculties",
             "The five faculties are a subset unrelated to powers"],
         "correct": 1,
         "expl": "A closely related but numerically distinct set."},
        {"q": "What image closes this discourse's verse?",
         "opts": [
             "A mountain unmoved by storms",
             "The heart's liberation compared to a lamp going out",
             "A river flowing to the sea",
             "A bird returning to a ship"],
         "correct": 1,
         "expl": "The same extinguished-flame image for nibbāna recurring throughout this "
                 "collection."},
        {"q": "Is a setting stated for AN 7.3?",
         "opts": ["Yes, at Sāvatthī, with the full narrative frame", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 0,
         "expl": "A fresh full setting, restated after AN 7.2's bare formula."},
        {"q": "What does <em>hiri</em> mean?",
         "opts": ["Prudence", "Conscience", "Energy", "Immersion"],
         "correct": 1,
         "expl": "One of the two items distinguishing this seven-item list from the five "
                 "faculties."},
    ],
    marginalia=[
        ("The seven powers", [
            "faith &middot; energy &middot;",
            "conscience &middot; prudence &middot;",
            "mindfulness &middot; immersion &middot; wisdom",
        ]),
        ("Brief, withholding explanation", [
            "no definitions given —",
            "AN 7.4 will spell out",
            "every term left bare here",
        ]),
        ("Five faculties, plus two", [
            "faith, energy, mindfulness,",
            "immersion, wisdom — plus",
            "conscience and prudence",
        ]),
        ("Cross-references", [
            "AN 7.4 &middot; next, this discourse's elaborated companion",
        ]),
    ],
    further=[
        '<a href="%s/an7.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.2.html">AN 7.2 &middot; Pleasing (2nd)</a> &mdash; previous, closing '
        "this chapter's first near-duplicate pair.",
        '<a href="an-7.4.html">AN 7.4 &middot; Powers in Detail</a> &mdash; next, this '
        "discourse's elaborated companion.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.4 — Vitthatabalasutta
# --------------------------------------------------------------------------- #
page(
    4, "Vitthatabala", "Powers in Detail",
    vagga=VAGGA_1,
    meta_title="AN 7.4 — Powers in Detail | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Vitthatabalasutta, defining each of the seven powers AN 7.3 named in brief, "
        "including the four absorptions in full under the power of immersion. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical seven-item list as AN 7.3, each term now given a full "
                 "definition — the elaborated half of this pair"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Definitional treatments of faith, energy, and the four "
                              "absorptions in sequence recur throughout the Chinese Āgamas' "
                              "systematic expositions; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the fullest definitional "
                       "discourse so far in this new nipāta, including all four absorptions "
                       "under a single power"),
    ],
    why=(
        "AN 7.4 defines every term AN 7.3 left bare: faith as confidence in the Buddha's "
        "awakening, energy as roused effort against unskillful qualities, conscience and "
        "prudence as shame and fear of wrongdoing, mindfulness as the capacity to recall "
        "what was said and done long ago, immersion as all four absorptions in sequence, "
        "and wisdom as insight into arising and passing away."),
    guide=[
        ("The teaching in one sentence", [
            "The seven powers &mdash; faith, energy, conscience, prudence, mindfulness, "
            "immersion, and wisdom &mdash; are each defined in turn, with immersion alone "
            "requiring all four absorptions to state in full."]),
        ("Faith as confidence in a specific, quoted formula", [
            "The power of faith is defined not as a vague trust but as confidence in a "
            "specific epithet formula for the Buddha &mdash; &ldquo;perfected, a fully "
            "awakened Buddha, accomplished in knowledge and conduct...&rdquo; &mdash; the "
            "same standard nine-part formula recurring throughout this literature wherever "
            "the Buddha's qualities are invoked in full."]),
        ("Immersion alone requires the entire fourfold jhāna sequence", [
            "Where the other six powers each receive one or two sentences of definition, "
            "the power of immersion is defined by naming all four absorptions in "
            "sequence, from the first (with applied and sustained thought, rapture, and "
            "bliss) through the fourth (with pure equanimity and mindfulness) &mdash; by far "
            "the longest single definition on this page."]),
        ("Wisdom, defined narrowly as insight into arising and passing away", [
            "Where paññā, wisdom, is sometimes treated broadly elsewhere in this "
            "literature, this discourse defines the power of wisdom specifically as "
            "&ldquo;the wisdom of arising and passing away which is noble, penetrative, and "
            "leads to the complete ending of suffering&rdquo; &mdash; a narrower, "
            "impermanence-focused definition rather than a general claim about "
            "intelligence or learning."]),
    ],
    terms=[
        ("saddhābala",
         "&ldquo;the power of faith&rdquo; &mdash; defined as confidence in the standard "
         "nine-part formula for the Buddha's qualities."),
        ("vīriyabala",
         "&ldquo;the power of energy&rdquo; &mdash; defined as roused effort for giving up "
         "unskillful qualities and embracing skillful ones."),
        ("hiribala, ottappabala",
         "&ldquo;the power of conscience, the power of prudence&rdquo; &mdash; defined as "
         "shame and fear specifically regarding bad conduct of body, speech, and mind."),
        ("samādhibala",
         "&ldquo;the power of immersion&rdquo; &mdash; defined by naming all four "
         "absorptions in full sequence, the longest single definition in this discourse."),
        ("paññābala",
         "&ldquo;the power of wisdom&rdquo; &mdash; defined narrowly as insight into "
         "arising and passing away, rather than a general claim about intelligence."),
    ],
    text_intro=(
        "The discourse in full: each of the seven powers defined in turn, closing on the "
        "same verse as AN 7.3. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven powers named"),
        ("p", "&sect;1", "an7.4:1.1-1.3"),
        ("h3", "Faith, energy, conscience, and prudence, defined"),
        ("p", "&sect;2", "an7.4:2.1-5.3"),
        ("h3", "Mindfulness, defined"),
        ("p", "&sect;3", "an7.4:6.1-6.3"),
        ("h3", "Immersion, defined through all four absorptions"),
        ("p", "&sect;4", "an7.4:7.1-9.1"),
        ("h3", "Wisdom, defined, and the closing verse"),
        ("p", "&sect;5", "an7.4:10.1-11.4"),
    ],
    quiz=[
        {"q": "How is the power of faith specifically defined in this discourse?",
         "opts": [
             "As a vague, unspecified trust",
             "As confidence in a specific nine-part formula naming the Buddha's qualities",
             "As faith in one's own judgment alone",
             "As agreement with a teacher's opinions"],
         "correct": 1,
         "expl": "A concrete, quoted formula rather than an undefined feeling."},
        {"q": "Why does the power of immersion require the longest definition on this page, "
              "according to the guide?",
         "opts": [
             "It does not — all seven powers receive equal-length definitions",
             "Because it is defined by naming all four absorptions in sequence, from the "
             "first through the fourth",
             "Because immersion is considered less important and needs more explanation",
             "Because the source text is corrupted at this point"],
         "correct": 1,
         "expl": "The only power requiring the full fourfold jhāna sequence to state."},
        {"q": "How is the power of wisdom defined in this discourse?",
         "opts": [
             "As general intelligence and broad learning",
             "Narrowly, as insight into arising and passing away, noble and penetrative, "
             "leading to the ending of suffering",
             "As skill in debate",
             "As memorization of scripture"],
         "correct": 1,
         "expl": "A specific, impermanence-focused definition rather than a general claim."},
        {"q": "How do conscience and prudence get defined in this discourse?",
         "opts": [
             "As unrelated to conduct entirely",
             "As shame and fear specifically regarding bad conduct of body, speech, and "
             "mind",
             "As synonyms for wisdom",
             "As physical sensations"],
         "correct": 1,
         "expl": "Terms already familiar from this series, defined with specific reference to "
                 "conduct."},
        {"q": "What does this discourse do that AN 7.3 did not?",
         "opts": [
             "Nothing — the two discourses are identical",
             "Define each of the seven powers in full, where AN 7.3 named them bare",
             "Add an eighth power",
             "Remove several powers from the list"],
         "correct": 1,
         "expl": "The elaborated half completing the brief/elaborated pair."},
        {"q": "Is a setting stated for AN 7.4?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.3's fresh full setting."},
    ],
    marginalia=[
        ("Seven powers, defined", [
            "faith: confidence in",
            "the Buddha's nine qualities —",
            "wisdom: insight into arising, passing",
        ]),
        ("Immersion: the longest entry", [
            "all four absorptions",
            "named in full sequence —",
            "far exceeding the other six",
        ]),
        ("A narrow definition of wisdom", [
            "not general intelligence —",
            "specifically, insight into",
            "arising and passing away",
        ]),
        ("Cross-references", [
            "AN 7.3 &middot; previous, this discourse's brief companion",
            "AN 7.5 &middot; next, a shift to the seven kinds of wealth",
        ]),
    ],
    further=[
        '<a href="%s/an7.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.3.html">AN 7.3 &middot; Powers in Brief</a> &mdash; previous, the '
        "brief companion this discourse elaborates on.",
        '<a href="an-7.5.html">AN 7.5 &middot; Wealth in Brief</a> &mdash; next, a shift to '
        "the seven kinds of wealth, in brief.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.5 — Saṁkhittadhanasutta
# --------------------------------------------------------------------------- #
page(
    5, "Saṁkhittadhana", "Wealth in Brief",
    vagga=VAGGA_1,
    next=("an-7.6.html", "AN 7.6 &middot; Wealth in Detail"),
    meta_title="AN 7.5 — Wealth in Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Saṁkhittadhanasutta, naming the seven kinds of wealth in brief — the chapter's own "
        "namesake theme, and the shorter half of a pair completed at the already-published "
        "AN 7.6. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, named briefly, closing on verse — this chapter's "
                 "own namesake theme"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The seven kinds of wealth (dhana) as a standard set recur "
                              "throughout the Chinese Āgamas' treatment of spiritual versus "
                              "material riches; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, naming this "
                       "chapter's own titular theme for the first time"),
    ],
    why=(
        "Dhanavagga, &lsquo;Wealth,&rsquo; finally names its own titular term directly: "
        "seven kinds of wealth &mdash; faith, ethics, conscience, prudence, learning, "
        "generosity, and wisdom &mdash; that this discourse's verse insists make anyone who "
        "has them prosperous, their life not lived in vain. AN 7.6, the chapter's own "
        "elaborated companion to this brief statement, is already published on this site "
        "from an earlier selection."),
    guide=[
        ("The teaching in one sentence", [
            "There are seven kinds of wealth: faith, ethics, conscience, prudence, "
            "learning, generosity, and wisdom, and whoever has them is truly prosperous, "
            "their life not lived in vain."]),
        ("This chapter's title, finally earned", [
            "AN 7.1 and 7.2 concerned being liked; AN 7.3 and 7.4 concerned powers; only "
            "with this discourse does the chapter titled 'Wealth' actually name wealth as "
            "its subject &mdash; a chapter title, like several already met across this "
            "series, describing later content more than its opening."]),
        ("Wealth reframed entirely as inward qualities", [
            "None of the seven items named &mdash; faith, ethics, conscience, prudence, "
            "learning, generosity, wisdom &mdash; is a material possession. The discourse's "
            "verse makes the reframing explicit: these seven inward qualities are what "
            "actually constitutes being &ldquo;prosperous,&rdquo; not any accumulation of "
            "coin or property."]),
        ("A brief half whose elaboration is already on this site", [
            "AN 7.6, this discourse's elaborated companion, was already published in this "
            "site's earlier eighteen-page selection before this systematic build-out began "
            "&mdash; matching the same pattern already met with AN 6.16 and AN 6.63 within "
            "the Sixes, an already-existing page this build simply threads around."]),
    ],
    terms=[
        ("dhana",
         "&ldquo;wealth&rdquo; &mdash; this chapter's own title term, finally named "
         "directly at this, its fifth discourse."),
        ("saddhā, sīla",
         "&ldquo;faith, ethics&rdquo; &mdash; the first two of the seven kinds of wealth "
         "named."),
        ("hiri, ottappa, suta",
         "&ldquo;conscience, prudence, learning&rdquo; &mdash; the third, fourth, and fifth "
         "items."),
        ("cāga, paññā",
         "&ldquo;generosity, wisdom&rdquo; &mdash; the sixth and seventh, closing items, "
         "wisdom named as &ldquo;the seventh kind of wealth&rdquo; in the closing verse."),
        ("saṁkhitta",
         "&ldquo;in brief&rdquo; &mdash; this discourse's own qualifier, distinguishing it "
         "from AN 7.6's <em>vitthata</em>, &ldquo;in detail.&rdquo;"),
    ],
    text_intro=(
        "The discourse in full: the seven kinds of wealth, named in brief, closing on "
        "verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven kinds of wealth"),
        ("p", "&sect;1", "an7.5:1.1-1.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.5:2.1-4.4"),
    ],
    quiz=[
        {"q": "What seven kinds of wealth does this discourse name?",
         "opts": [
             "Gold, silver, land, cattle, servants, grain, and jewels",
             "Faith, ethics, conscience, prudence, learning, generosity, and wisdom",
             "The seven powers of AN 7.3",
             "The five spiritual faculties plus two more"],
         "correct": 1,
         "expl": "Seven inward qualities, none of them a material possession."},
        {"q": "What is notable about this discourse's relationship to its chapter's title, "
              "'Wealth' (Dhanavagga)?",
         "opts": [
             "No relationship — the chapter title is unrelated to any discourse in it",
             "This is the first discourse in the chapter to actually name wealth as its "
             "subject, after AN 7.1/7.2 on being liked and AN 7.3/7.4 on powers",
             "Every discourse in the chapter concerns wealth equally",
             "This discourse contradicts the chapter's title"],
         "correct": 1,
         "expl": "A chapter title describing later content more than its opening, a pattern "
                 "already met across this series."},
        {"q": "How does the discourse's verse reframe the concept of wealth?",
         "opts": [
             "By adding material possessions to the list",
             "By insisting these seven inward qualities are what actually constitutes being "
             "prosperous, with no material item named at all",
             "By denying that anyone can truly be wealthy",
             "By equating wealth entirely with generosity alone"],
         "correct": 1,
         "expl": "Wealth defined entirely in terms of inward qualities."},
        {"q": "Where is this discourse's elaborated companion, AN 7.6, found?",
         "opts": [
             "It has not yet been written",
             "Already published on this site from an earlier selection, before this "
             "systematic build-out began — the same pattern already met with AN 6.16 and AN "
             "6.63",
             "It does not exist anywhere",
             "It was written later in this same session"],
         "correct": 1,
         "expl": "An already-existing page this build threads around, not a gap to fill."},
        {"q": "Is a setting stated for AN 7.5?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.4 immediately before it."},
        {"q": "What does <em>cāga</em> mean?",
         "opts": ["Learning", "Generosity", "Ethics", "Wisdom"],
         "correct": 1,
         "expl": "The sixth of the seven kinds of wealth named in this discourse."},
    ],
    marginalia=[
        ("The seven kinds of wealth", [
            "faith &middot; ethics &middot;",
            "conscience &middot; prudence &middot;",
            "learning &middot; generosity &middot; wisdom",
        ]),
        ("The chapter's title, at last", [
            "'Wealth' finally named —",
            "after two pairs on being",
            "liked, and on the seven powers",
        ]),
        ("Wealth entirely reframed", [
            "no material item —",
            "seven inward qualities",
            "define true prosperity",
        ]),
        ("Cross-references", [
            "AN 7.6 &middot; next, this discourse's already-published elaborated companion",
        ]),
    ],
    further=[
        '<a href="%s/an7.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.4.html">AN 7.4 &middot; Powers in Detail</a> &mdash; previous, the '
        "seven powers defined in full.",
        '<a href="an-7.6.html">AN 7.6 &middot; Wealth in Detail</a> &mdash; next, this '
        "discourse's already-published elaborated companion.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.7 — Uggasutta
# --------------------------------------------------------------------------- #
# an-7.6.html was published before this series began working in order, in
# the earlier eighteen-page selection; it sits between AN 7.5 and AN 7.7 in
# the traditional numbering, so this page's prev is set explicitly to splice
# around it. See HEAD/TAIL comment and INDEX_EXTRA at the top of this module.
page(
    7, "Ugga", "With Ugga",
    vagga=VAGGA_1,
    prev=("an-7.6.html", "AN 7.6 &middot; Wealth in Detail"),
    meta_title="AN 7.7 — With Ugga | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Uggasutta, in "
        "which the Buddha tells a government minister that even the richest man's fortune "
        "is vulnerable, unlike the seven kinds of spiritual wealth. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Unspecified, implied to continue from wherever the previous discourse "
                    "left off; Ugga the government chief minister approaches the Buddha "
                    "directly"),
        ("Speakers", "Ugga the government chief minister, and the Buddha, in dialogue"),
        ("Form", "A narrated exchange opening on a minister's amazement at another man's "
                 "wealth, turning to the same seven-item list already given at AN 7.5"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The contrast between material wealth vulnerable to fire, "
                              "water, and thieves and a spiritual wealth immune to all three "
                              "recurs widely across the Chinese Āgamas' teachings to lay "
                              "audiences; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a narrative dialogue "
                       "rather than a bare formula, naming a specific sum of material wealth "
                       "before pivoting to its spiritual counterpart"),
    ],
    why=(
        "AN 7.7 is this chapter's first genuine narrative since AN 7.1: Ugga, a government "
        "chief minister, marvels to the Buddha at Migāra of Rohaṇa's fortune, &ldquo;a "
        "hundred thousand gold coins, not to mention the silver.&rdquo; The Buddha does not "
        "dispute the sum, but immediately names its vulnerability &mdash; fire, water, "
        "rulers, thieves, and unloved heirs can all take a share &mdash; before naming the "
        "same seven kinds of wealth already given at AN 7.5, this time as what none of "
        "those five threats can touch."),
    guide=[
        ("The teaching in one sentence", [
            "Material wealth, however vast, can be taken by fire, water, rulers, thieves, "
            "or unloved heirs; the seven kinds of spiritual wealth &mdash; faith, ethics, "
            "conscience, prudence, learning, generosity, and wisdom &mdash; cannot be taken "
            "by any of them."]),
        ("The Buddha grants the premise before reframing it", [
            "Asked to marvel at another man's riches, the Buddha does not deny or minimize "
            "the sum Ugga names &mdash; &ldquo;that is wealth, I can't deny it&rdquo; "
            "&mdash; before immediately naming five specific threats material wealth "
            "remains exposed to. The reframing works by acknowledging the premise fully, "
            "not by dismissing it."]),
        ("The identical seven-item list as AN 7.5, in a new context", [
            "Checked term by term against AN 7.5, this discourse's seven kinds of wealth "
            "&mdash; faith, ethics, conscience, prudence, learning, generosity, wisdom "
            "&mdash; and its closing verse are identical. What is new is the narrative "
            "frame: a specific interlocutor, a specific named rich man, and a specific "
            "sum, giving abstract content concrete stakes."]),
        ("Five named threats, not a vague warning", [
            "Fire, water, rulers, thieves, and unloved heirs (aggi, udaka, rājāno, corā, "
            "appiyā dāyādā) are named specifically rather than left as a general caution "
            "&mdash; four external forces and, notably, one internal to the family itself, "
            "an heir who does not love the one whose wealth they inherit."]),
    ],
    terms=[
        ("Ugga",
         "the government chief minister (mahāmatta) who opens this discourse, marveling at "
         "another man's fortune."),
        ("Migāra of Rohaṇa",
         "the wealthy man whose &ldquo;hundred thousand gold coins&rdquo; opens this "
         "discourse's dialogue, never appearing directly himself."),
        ("aggi, udaka, rājāno, corā, appiyā dāyādā",
         "&ldquo;fire, water, rulers, thieves, unloved heirs&rdquo; &mdash; the five named "
         "threats material wealth remains exposed to."),
        ("saddhā, sīla, hiri, ottappa, suta, cāga, paññā",
         "the same seven kinds of wealth already given at AN 7.5: faith, ethics, "
         "conscience, prudence, learning, generosity, and wisdom."),
        ("dhana",
         "&ldquo;wealth&rdquo; &mdash; this chapter's own title term, now given a concrete "
         "narrative stake through Ugga's specific question."),
    ],
    text_intro=(
        "The discourse in full: Ugga's amazement at another man's fortune, and the "
        "Buddha's reframing toward the seven kinds of wealth no threat can take. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ugga marvels at Migāra's fortune"),
        ("p", "&sect;1", "an7.7:1.1-1.1"),
        ("h3", "Wealth, and what threatens it"),
        ("p", "&sect;2", "an7.7:2.1-2.10"),
        ("h3", "The seven kinds of wealth no threat can take"),
        ("p", "&sect;3", "an7.7:3.1-5.4"),
    ],
    quiz=[
        {"q": "What does Ugga marvel at, opening this discourse?",
         "opts": [
             "The Buddha's own teaching ability",
             "Migāra of Rohaṇa's fortune — a hundred thousand gold coins, not counting "
             "silver",
             "A deity's visit",
             "A mendicant's meditative attainment"],
         "correct": 1,
         "expl": "A specific, named sum opening this discourse's narrative frame."},
        {"q": "How does the Buddha initially respond to Ugga's report of this wealth?",
         "opts": [
             "By denying it counts as real wealth at all",
             "By granting the premise fully — 'that is wealth, I can't deny it' — before "
             "naming its vulnerability",
             "By ignoring the question entirely",
             "By condemning Migāra for his wealth"],
         "correct": 1,
         "expl": "The reframing works by acknowledging the premise, not dismissing it."},
        {"q": "What five threats does the Buddha name as able to take a share of material "
              "wealth?",
         "opts": [
             "The five hindrances",
             "Fire, water, rulers, thieves, and unloved heirs",
             "Old age, sickness, death, loss, and separation",
             "The four elements"],
         "correct": 1,
         "expl": "Four external forces and one internal to the family itself."},
        {"q": "How does this discourse's seven-item list compare to AN 7.5's, checked term "
              "by term?",
         "opts": [
             "Entirely different content",
             "Identical — the same seven kinds of wealth and closing verse, now given a "
             "concrete narrative frame",
             "Only three items overlap",
             "No relationship between the two discourses"],
         "correct": 1,
         "expl": "The same abstract content given concrete stakes through Ugga's specific "
                 "question."},
        {"q": "What page comes immediately before this one in the traditional numbering, "
              "already published on this site from an earlier selection?",
         "opts": [
             "AN 7.5", "AN 7.6, Wealth in Detail", "AN 7.1", "There is no earlier page"],
         "correct": 1,
         "expl": "This page's own navigation splices around that already-published page."},
        {"q": "Who does the Buddha address in this discourse?",
         "opts": [
             "The mendicants generally", "Ugga, the government chief minister, directly", "Migāra of Rohaṇa himself", "A group of deities"],
         "correct": 1,
         "expl": "A direct dialogue with a specific lay official, not a general address."},
    ],
    marginalia=[
        ("A specific fortune named", [
            "a hundred thousand",
            "gold coins — Migāra's",
            "wealth, marveled at by Ugga",
        ]),
        ("Five named threats", [
            "fire &middot; water &middot; rulers",
            "&middot; thieves &middot; unloved heirs —",
            "all can take a share",
        ]),
        ("The same seven kinds, again", [
            "faith, ethics, conscience,",
            "prudence, learning,",
            "generosity, wisdom — as AN 7.5",
        ]),
        ("Cross-references", [
            "AN 7.5 &middot; earlier, source of this discourse's seven-item list",
            "AN 7.6 &middot; the already-published page this navigation splices around",
        ]),
    ],
    further=[
        '<a href="%s/an7.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.5.html">AN 7.5 &middot; Wealth in Brief</a> &mdash; earlier, source '
        "of this discourse's seven-item list.",
        '<a href="an-7.8.html">AN 7.8 &middot; Fetters</a> &mdash; next, a shift to the '
        "seven fetters.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.8 — Saṁyojanasutta
# --------------------------------------------------------------------------- #
page(
    8, "Saṁyojana", "Fetters",
    vagga=VAGGA_1,
    meta_title="AN 7.8 — Fetters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṁyojanasutta, "
        "naming seven fetters — closing on desire for continued existence and ignorance — "
        "the first of a three-discourse family on this theme. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, stated bare with no reversal — opening a "
                 "three-discourse family on the fetters"),
        ("Length", "under 30 seconds to read"),
        ("Northern parallel", "The sevenfold division of fetters, distinct from the "
                              "more commonly cited ten fetters (saṁyojana) elsewhere in this "
                              "literature, recurs across the Chinese Āgamas' Abhidharma-"
                              "adjacent material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the briefest discourse "
                       "in this chapter so far, a single bare list"),
    ],
    why=(
        "AN 7.8 names seven fetters &mdash; attraction, aversion, views, doubt, conceit, "
        "desire for continued existence, and ignorance &mdash; with no elaboration, no "
        "reversal, and no further teaching, opening a three-discourse family that AN 7.9 "
        "and 7.10 will each treat differently: one by stating the fetters' purpose and "
        "full removal, the other by substituting its final two items entirely."),
    guide=[
        ("The teaching in one sentence", [
            "There are seven fetters: attraction, aversion, views, doubt, conceit, desire "
            "for continued existence, and ignorance."]),
        ("A sevenfold list, distinct from the more familiar ten fetters", [
            "This literature elsewhere more commonly names ten fetters (dasa saṁyojanāni) "
            "removed progressively across the four stages of awakening. This discourse's "
            "seven-item list overlaps with several of those ten &mdash; views, doubt, "
            "conceit, and ignorance recur in both &mdash; but is not identical to it, "
            "reflecting this chapter's own numerical theme of seven rather than the more "
            "commonly cited count."]),
        ("Attraction and aversion, opening the list", [
            "Anurodha (compliance, attraction) and virodha (repulsion, aversion) open this "
            "list as a matched pair &mdash; being drawn toward what is pleasant and pushed "
            "away from what is unpleasant &mdash; before the list turns to more specifically "
            "doctrinal fetters: views, doubt, and conceit."]),
        ("The first of three discourses on this exact theme", [
            "AN 7.9, immediately following, states this identical list's purpose and its "
            "complete removal in far fuller language; AN 7.10 restates the list's first "
            "five items but substitutes its own final two, jealousy and stinginess, for "
            "this discourse's desire for continued existence and ignorance."]),
    ],
    terms=[
        ("anurodha, virodha",
         "&ldquo;attraction, aversion&rdquo; &mdash; the opening pair of this discourse's "
         "seven fetters, being drawn toward the pleasant and pushed from the unpleasant."),
        ("diṭṭhi, vicikicchā, māna",
         "&ldquo;views, doubt, conceit&rdquo; &mdash; the third, fourth, and fifth items, "
         "each also named among the more commonly cited ten fetters elsewhere in this "
         "literature."),
        ("bhavarāga",
         "&ldquo;desire for continued existence&rdquo; &mdash; the sixth item, closing this "
         "particular version of the list."),
        ("avijjā",
         "&ldquo;ignorance&rdquo; &mdash; the seventh and final item, the last fetter "
         "removed at full awakening in this literature's broader account."),
        ("saṁyojana",
         "&ldquo;fetter&rdquo; &mdash; this discourse's own title term, here counted "
         "sevenfold rather than the more familiar tenfold division."),
    ],
    text_intro=(
        "The discourse in full: seven fetters, named bare. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven fetters"),
        ("p", "&sect;1", "an7.8:1.1-1.4"),
    ],
    quiz=[
        {"q": "What seven fetters does this discourse name?",
         "opts": [
             "The five hindrances plus two more",
             "Attraction, aversion, views, doubt, conceit, desire for continued existence, "
             "and ignorance",
             "The three poisons plus four more",
             "The seven powers of AN 7.3"],
         "correct": 1,
         "expl": "A sevenfold list distinct from, though overlapping with, the more "
                 "commonly cited ten fetters."},
        {"q": "How does this list relate to the more commonly cited ten fetters elsewhere in "
              "this literature, according to the guide?",
         "opts": [
             "Identical in every respect",
             "Overlapping but not identical — views, doubt, conceit, and ignorance recur in "
             "both, but this is a distinct sevenfold count matching this chapter's own "
             "numerical theme",
             "Entirely unrelated concepts",
             "This list has twelve items, not seven"],
         "correct": 1,
         "expl": "A count shaped by this book's own numerical theme, not a simple subset."},
        {"q": "What pair opens this discourse's list?",
         "opts": [
             "Faith and wisdom",
             "Attraction and aversion — being drawn toward the pleasant and pushed from the "
             "unpleasant",
             "Views and doubt",
             "The two poisons"],
         "correct": 1,
         "expl": "A matched pair before the list turns to more doctrinal items."},
        {"q": "What does this discourse open, according to the guide?",
         "opts": [
             "An isolated, standalone teaching",
             "A three-discourse family — AN 7.9 elaborates on this exact list, and AN 7.10 "
             "substitutes its final two items",
             "The chapter's final discourse",
             "A return to material already covered"],
         "correct": 1,
         "expl": "The first of three related but distinct treatments of this theme."},
        {"q": "Is a setting stated for AN 7.8?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, the briefest discourse in this chapter so far."},
        {"q": "What does <em>avijjā</em> mean?",
         "opts": ["Wisdom", "Ignorance", "Conceit", "Doubt"],
         "correct": 1,
         "expl": "The seventh and final fetter named, the last removed at full awakening in "
                 "this literature's broader account."},
    ],
    marginalia=[
        ("Seven fetters", [
            "attraction &middot; aversion",
            "&middot; views &middot; doubt &middot; conceit",
            "&middot; desire for existence &middot; ignorance",
        ]),
        ("Not the more familiar ten", [
            "overlapping but distinct —",
            "this chapter's own",
            "sevenfold numerical theme",
        ]),
        ("Opening a three-part family", [
            "AN 7.9 elaborates;",
            "AN 7.10 substitutes",
            "the final two items",
        ]),
        ("Cross-references", [
            "AN 7.9 &middot; next, this list's purpose and full removal",
        ]),
    ],
    further=[
        '<a href="%s/an7.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.7.html">AN 7.7 &middot; With Ugga</a> &mdash; previous, the seven '
        "kinds of wealth given concrete stakes.",
        '<a href="an-7.9.html">AN 7.9 &middot; Giving Up</a> &mdash; next, this identical '
        "list's purpose and full removal.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.9 — Pahānasutta
# --------------------------------------------------------------------------- #
page(
    9, "Pahāna", "Giving Up",
    vagga=VAGGA_1,
    meta_title="AN 7.9 — Giving Up | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Pahānasutta, "
        "restating AN 7.8's identical seven fetters and stating the entire purpose of the "
        "spiritual life as their complete removal. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical seven-item list as AN 7.8, elaborated with a statement of "
                 "purpose and a closing formula already met in the Sixes"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The image of a fetter cut off 'at the root, like a palm "
                              "stump' recurs widely across the Chinese Āgamas' descriptions "
                              "of complete abandonment; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; restates AN 7.8's bare "
                       "list with the fullest statement of purpose in this chapter so far"),
    ],
    why=(
        "AN 7.9 restates AN 7.8's identical seven fetters, but where that discourse simply "
        "named them, this one states outright that &ldquo;the spiritual life is lived to "
        "give up and cut out these seven fetters,&rdquo; then closes with the same formula "
        "already met at AN 6.105 and 6.106 in the previous nipāta: &ldquo;cut off craving, "
        "cast off the fetters, and by rightly comprehending conceit has made an end of "
        "suffering.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "The entire spiritual life is lived to give up and cut out the seven fetters "
            "&mdash; attraction, aversion, views, doubt, conceit, desire to be reborn, and "
            "ignorance &mdash; cutting them off at the root so they can never arise again."]),
        ("A stated purpose, not merely a list", [
            "AN 7.8 named these seven items with no further comment. This discourse opens "
            "by stating their removal as nothing less than the entire point of the "
            "spiritual life (brahmacariya) &mdash; the highest possible framing this "
            "literature gives to any single teaching."]),
        ("'Cut off at the root, like a palm stump'", [
            "The discourse's central image for complete removal &mdash; &ldquo;cut them off "
            "at the root, made them like a palm stump, obliterated them, so they are unable "
            "to arise in the future&rdquo; &mdash; describes not weakening or suppressing a "
            "fetter but its total, irreversible elimination, a palm stump being unable to "
            "regrow once properly cut."]),
        ("A closing formula carried over from the previous nipāta", [
            "This discourse's closing line &mdash; &ldquo;cut off craving, cast off the "
            "fetters, and by rightly comprehending conceit has made an end of "
            "suffering&rdquo; &mdash; is word for word the same formula already met closing "
            "both AN 6.105 and AN 6.106, applied there to a different pair of specific "
            "3+3 lists and here to this discourse's own seven fetters."]),
    ],
    terms=[
        ("brahmacariya",
         "&ldquo;the spiritual life&rdquo; &mdash; this discourse's framing for the entire "
         "purpose the seven fetters' removal serves."),
        ("mūlaghacca",
         "&ldquo;cut off at the root&rdquo; &mdash; part of this discourse's central image "
         "for complete, irreversible removal."),
        ("tālāvatthukata",
         "&ldquo;made like a palm stump&rdquo; &mdash; the same image, describing a "
         "removal so total that regrowth becomes impossible."),
        ("anurodha, virodha, diṭṭhi, vicikicchā, māna, bhavarāga, avijjā",
         "identical to AN 7.8's seven fetters: attraction, aversion, views, doubt, "
         "conceit, desire to be reborn, and ignorance."),
        ("taṇhacchida, mānābhisamayā antamakāsi dukkhassa",
         "&ldquo;one who has cut off craving... by rightly comprehending conceit, made an "
         "end of suffering&rdquo; &mdash; the closing formula shared word for word with AN "
         "6.105 and AN 6.106 in the previous nipāta."),
    ],
    text_intro=(
        "The discourse in full: the purpose and complete removal of the seven fetters. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The purpose of the spiritual life"),
        ("p", "&sect;1", "an7.9:1.1-1.17"),
    ],
    quiz=[
        {"q": "How does AN 7.9's treatment of the seven fetters differ from AN 7.8's, "
              "checked term by term?",
         "opts": [
             "Entirely different content",
             "The identical seven fetters, but stated here as the purpose of the entire "
             "spiritual life, rather than simply named bare",
             "Only three of seven items overlap",
             "No relationship between the two discourses"],
         "correct": 1,
         "expl": "Same list, elevated to the highest possible framing this literature gives "
                 "a teaching."},
        {"q": "What does the image of a fetter 'cut off at the root, like a palm stump' "
              "describe, according to the guide?",
         "opts": [
             "A temporary weakening of a fetter",
             "Total, irreversible elimination — a palm stump being unable to regrow once "
             "properly cut",
             "A fetter that will return after some time",
             "A metaphor unrelated to removal"],
         "correct": 1,
         "expl": "Complete removal, not suppression or gradual weakening."},
        {"q": "Where else in this series has this discourse's closing formula already "
              "appeared?",
         "opts": [
             "Nowhere else",
             "At AN 6.105 and AN 6.106, closing the previous nipāta, applied there to "
             "different specific 3+3 lists",
             "Only at AN 7.8, immediately before this discourse",
             "At AN 7.1, opening this chapter"],
         "correct": 1,
         "expl": "An identical closing formula carried across the boundary between two "
                 "nipātas."},
        {"q": "What does <em>brahmacariya</em> mean, and what role does it play in this "
              "discourse?",
         "opts": [
             "'Wisdom' — a synonym for insight",
             "'The spiritual life' — this discourse frames the seven fetters' removal as "
             "nothing less than its entire purpose",
             "'Fetter' — a synonym for saṁyojana",
             "A term unrelated to this discourse's teaching"],
         "correct": 1,
         "expl": "The highest possible framing this literature gives to a single teaching."},
        {"q": "Is a setting stated for AN 7.9?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching AN 7.8 immediately before it."},
        {"q": "What are the seven fetters named in this discourse?",
         "opts": [
             "The five hindrances plus two more",
             "Attraction, aversion, views, doubt, conceit, desire to be reborn, and "
             "ignorance — identical to AN 7.8",
             "An entirely new list not matching AN 7.8",
             "The seven powers of AN 7.3"],
         "correct": 1,
         "expl": "The same list as AN 7.8, now elaborated with purpose and closing formula."},
    ],
    marginalia=[
        ("The same seven fetters", [
            "attraction &middot; aversion",
            "&middot; views &middot; doubt &middot; conceit",
            "&middot; desire to be reborn &middot; ignorance",
        ]),
        ("The entire point of practice", [
            "'the spiritual life",
            "is lived to give up",
            "and cut out these seven fetters'",
        ]),
        ("A formula from the Sixes", [
            "'cut off craving,",
            "cast off fetters' —",
            "identical to AN 6.105/106",
        ]),
        ("Cross-references", [
            "AN 7.8 &middot; previous, the bare version of this same list",
            "AN 6.105/106 &middot; earlier nipāta, source of this closing formula",
        ]),
    ],
    further=[
        '<a href="%s/an7.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.8.html">AN 7.8 &middot; Fetters</a> &mdash; previous, the bare '
        "version of this same list.",
        '<a href="an-7.10.html">AN 7.10 &middot; Stinginess</a> &mdash; next, closing this '
        "chapter with two substituted items.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.10 — Macchariyasutta
# --------------------------------------------------------------------------- #
page(
    10, "Macchariya", "Stinginess",
    vagga=VAGGA_1,
    meta_title="AN 7.10 — Stinginess | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Macchariyasutta, "
        "closing this chapter with AN 7.8's first five fetters but substituting jealousy "
        "and stinginess for its final two items. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, sharing five items with AN 7.8 but closing on "
                 "two substituted items — closing this chapter"),
        ("Length", "under 30 seconds to read"),
        ("Northern parallel", "The pairing of jealousy and stinginess as a joint fetter "
                              "recurs in related forms across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, closing this "
                       "chapter with a now-familiar substitution technique"),
    ],
    why=(
        "AN 7.10 closes this chapter by repeating AN 7.8's first five fetters exactly "
        "&mdash; attraction, aversion, views, doubt, conceit &mdash; but substituting "
        "jealousy and stinginess for that discourse's desire for continued existence and "
        "ignorance, the same shared-frame, substituted-closing-pair technique already met "
        "repeatedly across the Sixes and, within this very chapter, at AN 7.1/7.2."),
    guide=[
        ("The teaching in one sentence", [
            "There are seven fetters: attraction, aversion, views, doubt, conceit, "
            "jealousy, and stinginess."]),
        ("Five items shared, two substituted, again", [
            "Checked term by term against AN 7.8, this discourse's first five items are "
            "identical. Only the sixth and seventh change: issā (jealousy) and macchariya "
            "(stinginess, this discourse's own title term) replace bhavarāga (desire for "
            "continued existence) and avijjā (ignorance)."]),
        ("The same substituted pair as AN 7.2, on different first five items", [
            "Jealousy and stinginess already closed AN 7.2's blocking list, substituted "
            "there for corrupt wishes and wrong view against a different first five items "
            "concerning material desire and conscience. Here the same substituted pair "
            "closes a list concerning attraction, aversion, views, doubt, and conceit "
            "instead &mdash; the identical closing substitution reused against a different "
            "base list within the same chapter."]),
        ("A chapter closing on the theme it opened with", [
            "This chapter opened at AN 7.1 with jealousy and stinginess's near-relatives "
            "(corrupt wishes, wrong view) as one closing pair among several possibilities, "
            "and closes here with jealousy and stinginess themselves &mdash; the exact pair "
            "AN 7.2 already used &mdash; now applied to the fetters rather than to what "
            "makes a mendicant liked or disliked."]),
    ],
    terms=[
        ("anurodha, virodha, diṭṭhi, vicikicchā, māna",
         "the first five fetters, identical to AN 7.8: attraction, aversion, views, doubt, "
         "conceit."),
        ("issā",
         "&ldquo;jealousy&rdquo; &mdash; the sixth item, replacing AN 7.8's desire for "
         "continued existence, and identical to AN 7.2's own sixth item."),
        ("macchariya",
         "&ldquo;stinginess&rdquo; &mdash; the seventh and closing item, this discourse's "
         "own title term, replacing AN 7.8's ignorance."),
        ("bhavarāga, avijjā",
         "&ldquo;desire for continued existence, ignorance&rdquo; &mdash; AN 7.8's original "
         "sixth and seventh items, absent from this discourse's version."),
        ("saṁyojana",
         "&ldquo;fetter&rdquo; &mdash; the shared term across all three discourses of this "
         "chapter's fetters family, AN 7.8&ndash;10."),
    ],
    text_intro=(
        "The discourse in full: seven fetters, closing on jealousy and stinginess. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven fetters"),
        ("p", "&sect;1", "an7.10:1.1-1.4"),
    ],
    quiz=[
        {"q": "How many of this discourse's seven items are identical to AN 7.8's, checked "
              "term by term?",
         "opts": [
             "None", "Five — only the sixth and seventh items differ", "All seven", "Only two"],
         "correct": 1,
         "expl": "The same substitution technique already met repeatedly across this "
                 "series."},
        {"q": "What two items replace AN 7.8's desire for continued existence and "
              "ignorance?",
         "opts": [
             "Laziness and negligence",
             "Jealousy and stinginess",
             "Doubt and restlessness",
             "Faith and wisdom"],
         "correct": 1,
         "expl": "This discourse's own title term, stinginess, closes the substituted pair."},
        {"q": "Where else in this same chapter has this exact substituted pair, jealousy "
              "and stinginess, already appeared?",
         "opts": [
             "Nowhere else in this chapter",
             "At AN 7.2, closing a different base list concerning material desire and "
             "conscience",
             "At AN 7.5, among the seven kinds of wealth",
             "At AN 7.9, restating AN 7.8's exact list"],
         "correct": 1,
         "expl": "The identical closing substitution reused against a different base list "
                 "within one chapter."},
        {"q": "How does the guide describe this chapter's overall arc, from AN 7.1 to this "
              "closing discourse?",
         "opts": [
             "No discernible arc across the chapter",
             "The chapter opens with jealousy and stinginess's near-relatives as one "
             "closing pair, and closes with jealousy and stinginess themselves, now applied "
             "to the fetters",
             "The chapter never mentions jealousy or stinginess before this discourse",
             "Every discourse in the chapter is identical"],
         "correct": 1,
         "expl": "A closing echo of themes already introduced earlier in the chapter."},
        {"q": "Is a setting stated for AN 7.10?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, closing this chapter's fetters family and Dhanavagga "
                 "itself."},
        {"q": "What connects AN 7.9 and AN 7.10, both following AN 7.8?",
         "opts": [
             "Nothing — they are unrelated discourses",
             "Both restate AN 7.8's fetters theme, one elaborating the identical list in "
             "full, the other substituting its final two items",
             "Both are identical to each other",
             "Neither discourse mentions fetters"],
         "correct": 1,
         "expl": "Two different treatments completing a three-discourse family opened at AN "
                 "7.8."},
    ],
    marginalia=[
        ("Five items shared with 7.8", [
            "attraction &middot; aversion",
            "&middot; views &middot; doubt &middot;",
            "conceit — identical to AN 7.8",
        ]),
        ("The same pair as AN 7.2", [
            "jealousy, stinginess —",
            "reused here against",
            "a different base list",
        ]),
        ("Closing the chapter's arc", [
            "opened with near-relatives",
            "of this pair at AN 7.1,",
            "closes with the pair itself",
        ]),
        ("Cross-references", [
            "AN 7.8/7.9 &middot; earlier, this chapter's fetters family",
            "AN 7.2 &middot; earlier, source of this discourse's substituted pair",
        ]),
    ],
    further=[
        '<a href="%s/an7.10/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.9.html">AN 7.9 &middot; Giving Up</a> &mdash; previous, the full '
        "elaboration of AN 7.8's identical list.",
        '<a href="an-7.2.html">AN 7.2 &middot; Pleasing (2nd)</a> &mdash; earlier, source of '
        "this discourse's substituted closing pair.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 2 — Anusayavagga (AN 7.11–20)
# --------------------------------------------------------------------------- #
VAGGA_2 = "<em>Anusayavagga</em> &mdash; the second chapter of the Sevens"


# --------------------------------------------------------------------------- #
# AN 7.11 — Paṭhamaanusayasutta
# --------------------------------------------------------------------------- #
page(
    11, "Paṭhamaanusaya", "Underlying Tendencies (1st)",
    vagga=VAGGA_2,
    meta_title="AN 7.11 — Underlying Tendencies (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaanusayasutta, naming seven underlying tendencies identical in content to "
        "AN 7.8's fetters but classified under a different technical category. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, stated bare — opening this chapter with content "
                 "already met once in this book under a different name"),
        ("Length", "under 30 seconds to read"),
        ("Northern parallel", "The sevenfold underlying tendencies (anusaya) as a distinct "
                              "technical category from the fetters recurs throughout the "
                              "Chinese Āgamas' Abhidharma-adjacent material; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; content already met at "
                       "AN 7.8, now presented under a genuinely different technical term"),
    ],
    why=(
        "Anusayavagga, &lsquo;Tendencies,&rsquo; opens with a list checked term by term "
        "against AN 7.8's seven fetters from the previous chapter: sensual desire, "
        "aversion, views, doubt, conceit, desire for continued existence, and ignorance "
        "&mdash; the identical seven items, now named anusaya, &ldquo;underlying "
        "tendencies,&rdquo; rather than saṁyojana, &ldquo;fetters.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "There are seven underlying tendencies: sensual desire, aversion, views, "
            "doubt, conceit, desire for continued existence, and ignorance."]),
        ("The same seven items, a different technical category", [
            "Fetter (saṁyojana) and underlying tendency (anusaya) are distinct technical "
            "terms in this literature's broader Abhidhamma-adjacent vocabulary: a fetter "
            "binds a being to the cycle of rebirth, while an underlying tendency describes "
            "a defilement's latent, dormant potential to arise even when not currently "
            "active. That this discourse applies the identical seven-item content to both "
            "categories suggests the two terms describe the same underlying defilements "
            "from two different angles &mdash; as bonds, and as latent potentials &mdash; "
            "rather than naming two different sets of things."]),
        ("A chapter title matching its content directly", [
            "Unlike several chapter titles already met across this series that describe "
            "later content more than their opening discourse, Anusayavagga names its own "
            "subject directly at this, its very first discourse."]),
        ("Opening a pair matching AN 7.8/7.9's exact shape", [
            "AN 7.12, immediately following, will do for this discourse's anusaya list "
            "exactly what AN 7.9 already did for AN 7.8's saṁyojana list: state its "
            "purpose and complete removal, closing on the identical formula already met "
            "twice in this series."]),
    ],
    terms=[
        ("anusaya",
         "&ldquo;underlying tendency&rdquo; &mdash; this chapter's own title term, "
         "describing a defilement's latent, dormant potential to arise."),
        ("kāmarāga, paṭigha",
         "&ldquo;sensual desire, aversion&rdquo; &mdash; the first two items, matching AN "
         "7.8's first two fetters in substance though named slightly differently in Pāli."),
        ("diṭṭhi, vicikicchā, māna",
         "&ldquo;views, doubt, conceit&rdquo; &mdash; the third, fourth, and fifth items, "
         "identical in wording to AN 7.8's fetters."),
        ("bhavarāga, avijjā",
         "&ldquo;desire for continued existence, ignorance&rdquo; &mdash; the sixth and "
         "seventh items, closing this list exactly as they closed AN 7.8's."),
        ("saṁyojana",
         "&ldquo;fetter&rdquo; &mdash; the distinct technical category AN 7.8 in the "
         "previous chapter applied to this identical seven-item content."),
    ],
    text_intro=(
        "The discourse in full: the seven underlying tendencies, named bare. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven underlying tendencies"),
        ("p", "&sect;1", "an7.11:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this discourse's seven-item list compare to AN 7.8's fetters, "
              "checked term by term?",
         "opts": [
             "Entirely different content",
             "Identical — the same seven items, now classified as underlying tendencies "
             "(anusaya) rather than fetters (saṁyojana)",
             "Only three items overlap",
             "No relationship between the two lists"],
         "correct": 1,
         "expl": "The same defilements, described under a different technical category."},
        {"q": "What does the guide say distinguishes 'fetter' from 'underlying tendency' as "
              "technical terms?",
         "opts": [
             "They are complete synonyms with no distinction",
             "A fetter binds a being to rebirth, while an underlying tendency describes a "
             "defilement's latent, dormant potential to arise — two angles on the same "
             "content",
             "They refer to two entirely unrelated sets of defilements",
             "Only underlying tendencies are ever actually removed"],
         "correct": 1,
         "expl": "Two different technical angles on what may be the same underlying "
                 "defilements."},
        {"q": "How does this discourse's relationship to its chapter's title compare to "
              "several earlier chapter titles in this series?",
         "opts": [
             "Identical pattern — the title describes later content, not this opening "
             "discourse",
             "This chapter's title, Anusayavagga, matches its own subject directly at this "
             "very first discourse, unlike several earlier chapters",
             "The chapter has no relationship to any of its own discourses",
             "This chapter has no title at all"],
         "correct": 1,
         "expl": "A direct match, rather than the delayed-title pattern already met "
                 "elsewhere."},
        {"q": "What does this discourse open a pair with, according to the guide?",
         "opts": [
             "Nothing further — an isolated teaching",
             "AN 7.12, which will do for this list exactly what AN 7.9 already did for AN "
             "7.8's fetters — state its purpose and complete removal",
             "A return to the seven kinds of wealth",
             "The chapter's final discourse"],
         "correct": 1,
         "expl": "A pair matching AN 7.8/7.9's exact shape, now applied to a different "
                 "technical category."},
        {"q": "Is a setting stated for AN 7.11?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, opening this new chapter."},
        {"q": "What does <em>bhavarāga</em> mean?",
         "opts": ["Sensual desire", "Desire for continued existence", "Ignorance", "Conceit"],
         "correct": 1,
         "expl": "The sixth item, closing this list exactly as it closed AN 7.8's fetters."},
    ],
    marginalia=[
        ("Seven underlying tendencies", [
            "sensual desire &middot;",
            "aversion &middot; views &middot; doubt",
            "&middot; conceit &middot; desire for existence &middot; ignorance",
        ]),
        ("Identical to AN 7.8's fetters", [
            "same seven items —",
            "a different technical",
            "category, not different content",
        ]),
        ("Two angles, one content", [
            "fetter: what binds",
            "to rebirth — tendency:",
            "latent potential to arise",
        ]),
        ("Cross-references", [
            "AN 7.8/7.9 &middot; earlier, this same content as fetters",
            "AN 7.12 &middot; next, this list's purpose and full removal",
        ]),
    ],
    further=[
        '<a href="%s/an7.11/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.8.html">AN 7.8 &middot; Fetters</a> &mdash; earlier, this same '
        "content classified as fetters.",
        '<a href="an-7.12.html">AN 7.12 &middot; Underlying Tendencies (2nd)</a> &mdash; '
        "next, this list's purpose and complete removal.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.12 — Dutiyaanusayasutta
# --------------------------------------------------------------------------- #
page(
    12, "Dutiyaanusaya", "Underlying Tendencies (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 7.12 — Underlying Tendencies (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaanusayasutta, stating the purpose and complete removal of AN 7.11's seven "
        "underlying tendencies, closing on the same formula already met twice before. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical seven-item list as AN 7.11, elaborated with a statement of "
                 "purpose and the same closing formula already met twice in this series"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The image of an underlying tendency cut off 'at the root, "
                              "like a palm stump' recurs widely across the Chinese Āgamas' "
                              "descriptions of complete abandonment; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; restates AN 7.11's bare "
                       "list with the fullest statement of purpose in this chapter so far"),
    ],
    why=(
        "AN 7.12 does for AN 7.11's seven underlying tendencies exactly what AN 7.9 "
        "already did for AN 7.8's seven fetters: states their removal as the entire "
        "purpose of the spiritual life, uses the identical &ldquo;cut off at the root, "
        "like a palm stump&rdquo; image for complete elimination, and closes on the same "
        "formula &mdash; now met a third time in this series."),
    guide=[
        ("The teaching in one sentence", [
            "The entire spiritual life is lived to give up and cut out the seven "
            "underlying tendencies &mdash; sensual desire, aversion, views, doubt, conceit, "
            "desire to be reborn, and ignorance &mdash; cutting them off at the root so "
            "they can never arise again."]),
        ("A structural twin of AN 7.9, applied to a different category", [
            "Checked side by side, this discourse and AN 7.9 share their entire "
            "structure &mdash; the statement of purpose, the palm-stump image, the closing "
            "formula &mdash; differing only in whether the seven items being removed are "
            "named as fetters or as underlying tendencies."]),
        ("A third appearance of this closing formula", [
            "&ldquo;Cut off craving, cast off the fetters, and by rightly comprehending "
            "conceit has made an end of suffering&rdquo; now closes AN 6.105, AN 6.106, and "
            "AN 7.9 in the previous nipāta and chapter, and this discourse makes a fourth "
            "appearance &mdash; the same formula applied across four discourses with "
            "different specific content in every case, spanning two nipātas."]),
        ("Why fetters and tendencies each get their own pair", [
            "That this chapter gives underlying tendencies the identical bare-list-plus-"
            "elaboration treatment the previous chapter already gave fetters, rather than "
            "simply noting the overlap and moving on, suggests the tradition considered "
            "each technical category worth stating fully in its own right, even where the "
            "specific content named is identical."]),
    ],
    terms=[
        ("brahmacariya",
         "&ldquo;the spiritual life&rdquo; &mdash; this discourse's framing for the entire "
         "purpose the seven underlying tendencies' removal serves, identical to AN 7.9's "
         "framing."),
        ("mūlaghacca, tālāvatthukata",
         "&ldquo;cut off at the root, made like a palm stump&rdquo; &mdash; the same image "
         "for complete, irreversible removal already met at AN 7.9."),
        ("kāmarāga, paṭigha, diṭṭhi, vicikicchā, māna, bhavarāga, avijjā",
         "identical to AN 7.11's seven underlying tendencies: sensual desire, aversion, "
         "views, doubt, conceit, desire to be reborn, and ignorance."),
        ("taṇhacchida, mānābhisamayā antamakāsi dukkhassa",
         "&ldquo;one who has cut off craving... by rightly comprehending conceit, made an "
         "end of suffering&rdquo; &mdash; the closing formula's fourth appearance in this "
         "series, after AN 6.105, AN 6.106, and AN 7.9."),
        ("anusaya",
         "&ldquo;underlying tendency&rdquo; &mdash; the technical category this discourse "
         "addresses, structurally paired with AN 7.9's treatment of fetters."),
    ],
    text_intro=(
        "The discourse in full: the purpose and complete removal of the seven underlying "
        "tendencies. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The purpose of the spiritual life"),
        ("p", "&sect;1", "an7.12:1.1-1.9"),
        ("h3", "Complete removal, and the closing formula"),
        ("p", "&sect;2", "an7.12:2.1-2.8"),
    ],
    quiz=[
        {"q": "How does this discourse's structure compare to AN 7.9's, checked side by "
              "side?",
         "opts": [
             "Entirely different structure",
             "The identical structure — statement of purpose, palm-stump image, closing "
             "formula — differing only in whether the seven items are named as fetters or "
             "underlying tendencies",
             "Only the closing formula is shared",
             "No relationship between the two discourses"],
         "correct": 1,
         "expl": "A structural twin of AN 7.9, applied to a different technical category."},
        {"q": "How many times has this discourse's closing formula now appeared in this "
              "series, counting this discourse?",
         "opts": [
             "Once", "Twice", "A fourth appearance, after AN 6.105, AN 6.106, and AN 7.9", "Never before"],
         "correct": 2,
         "expl": "The same formula spanning two nipātas and four discourses with different "
                 "specific content each time."},
        {"q": "According to the guide, why might fetters and underlying tendencies each get "
              "their own bare-list-plus-elaboration pair, despite identical content?",
         "opts": [
             "It is simply a copying error",
             "The tradition may have considered each technical category worth stating "
             "fully in its own right, even where the specific content named is identical",
             "The two pairs actually have entirely different content",
             "Only one of the two pairs is authentic"],
         "correct": 1,
         "expl": "A deliberate choice to treat each category on its own terms."},
        {"q": "What image describes complete removal in this discourse?",
         "opts": [
             "A river reaching the sea",
             "Cut off at the root, made like a palm stump — unable to arise again",
             "A flower blooming and fading",
             "A bird returning to a ship"],
         "correct": 1,
         "expl": "The same image already met at AN 7.9, describing total, irreversible "
                 "elimination."},
        {"q": "Is a setting stated for AN 7.12?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching AN 7.11 immediately before it."},
        {"q": "What is the entire purpose the spiritual life is said to serve, according to "
              "this discourse?",
         "opts": [
             "Acquiring merit for a good rebirth",
             "Giving up and cutting out the seven underlying tendencies",
             "Gaining a reputation as a skilled teacher",
             "Accumulating scriptural knowledge"],
         "correct": 1,
         "expl": "The highest possible framing this literature gives to a single teaching."},
    ],
    marginalia=[
        ("A structural twin of AN 7.9", [
            "same purpose statement,",
            "same palm-stump image,",
            "same closing formula",
        ]),
        ("The formula's fourth appearance", [
            "AN 6.105, AN 6.106,",
            "AN 7.9, and now",
            "this discourse — two nipātas",
        ]),
        ("Each category, fully stated", [
            "fetters and tendencies",
            "both get their own pair,",
            "despite identical content",
        ]),
        ("Cross-references", [
            "AN 7.11 &middot; previous, the bare version of this same list",
            "AN 7.9 &middot; earlier, this discourse's structural twin",
        ]),
    ],
    further=[
        '<a href="%s/an7.12/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.11.html">AN 7.11 &middot; Underlying Tendencies (1st)</a> &mdash; '
        "previous, the bare version of this same list.",
        '<a href="an-7.13.html">AN 7.13 &middot; A Family</a> &mdash; next, a shift to '
        "practical conduct toward lay households.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.13 — Kulasutta
# --------------------------------------------------------------------------- #
page(
    13, "Kula", "A Family",
    vagga=VAGGA_2,
    meta_title="AN 7.13 — A Family | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kulasutta, naming "
        "seven factors that make visiting a lay household worthwhile or not, a shift from "
        "doctrinal categories to everyday practical conduct. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched seven-item lists, cause and its direct reversal, addressing "
                 "practical etiquette rather than doctrinal categories"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Guidance on which lay households are worth a mendicant's "
                              "visit recurs widely across the Chinese Āgamas' monastic "
                              "conduct material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a concrete, practical "
                       "list, a clear register shift after this chapter's two doctrinal "
                       "discourses"),
    ],
    why=(
        "AN 7.13 shifts abruptly from AN 7.11 and 7.12's underlying tendencies to something "
        "entirely practical: seven factors of hospitality &mdash; whether a family rises "
        "politely, bows, offers a seat, shares openly, gives generously, offers fine "
        "things, and gives carefully &mdash; that determine whether visiting, or even "
        "sitting down once arrived, is worthwhile at all."),
    guide=[
        ("The teaching in one sentence", [
            "Visiting a family that doesn't rise politely, hides what they have, gives "
            "little even when they have much, gives coarse things even when they have "
            "fine things, and gives carelessly is not worthwhile; a family with the seven "
            "direct opposites is worth visiting."]),
        ("A sharp register shift within this chapter", [
            "Where AN 7.11 and 7.12 concerned abstract underlying tendencies removed only "
            "at advanced stages of practice, this discourse concerns the concrete, everyday "
            "question of hospitality &mdash; whether a family rises to greet a visitor, "
            "what quality of goods they offer, and how carefully they give. This chapter's "
            "'Tendencies' title, like several others already met in this series, does not "
            "describe every discourse within it equally."]),
        ("Not merely material generosity, but its manner", [
            "The list's final three items concern not whether a family gives at all, but "
            "how: giving little despite having much, giving coarse things despite having "
            "fine things, and giving carelessly rather than carefully. The discourse's "
            "concern is the quality and attentiveness of generosity, not simply its "
            "occurrence."]),
        ("'Worthwhile' as the discourse's own practical stake", [
            "The discourse frames its stakes not in terms of merit, karma, or spiritual "
            "attainment, but simply worth (na... alaṁ) &mdash; whether a visit, or even "
            "remaining seated once arrived, is a good use of a mendicant's time, a "
            "strikingly pragmatic framing for this collection."]),
    ],
    terms=[
        ("kula",
         "&ldquo;family, household&rdquo; &mdash; this discourse's own subject, the lay "
         "household a mendicant might visit."),
        ("paccuṭṭhāti, abhivādeti, āsanaṁ dadāti",
         "&ldquo;rises, bows, offers a seat&rdquo; &mdash; the first three factors of "
         "hospitality named."),
        ("santaṁ pi na denti",
         "&ldquo;even when they have much they give little&rdquo; &mdash; one of the "
         "discourse's items concerning the manner, not mere occurrence, of generosity."),
        ("sakkaccaṁ deti, asakkaccaṁ na deti",
         "&ldquo;gives carefully, not carelessly&rdquo; &mdash; the seventh and closing "
         "item, on attentiveness in giving."),
        ("alaṁ",
         "&ldquo;worthwhile, enough&rdquo; &mdash; the discourse's own practical framing "
         "for its stakes, distinct from the doctrinal framing of the two discourses before "
         "it."),
    ],
    text_intro=(
        "The discourse in full: seven factors of hospitality determining whether visiting "
        "a family is worthwhile, and their reversal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven factors that make a family not worth visiting"),
        ("p", "&sect;1", "an7.13:1.1-1.4"),
        ("h3", "Seven factors that make a family worth visiting"),
        ("p", "&sect;2", "an7.13:2.1-2.4"),
    ],
    quiz=[
        {"q": "What kind of content does this discourse address, unlike AN 7.11 and 7.12 "
              "immediately before it?",
         "opts": [
             "Abstract underlying tendencies, identical to the two before it",
             "Concrete, practical hospitality — whether a family rises politely, shares "
             "openly, and gives carefully",
             "The four noble truths",
             "A doctrinal dispute between two mendicants"],
         "correct": 1,
         "expl": "A sharp register shift from doctrinal category to everyday etiquette."},
        {"q": "What do the list's final three items concern, according to the guide?",
         "opts": [
             "Whether a family gives at all",
             "The manner of giving — quantity relative to means, quality of goods offered, "
             "and attentiveness — not merely whether generosity occurs",
             "A family's religious beliefs",
             "The family's physical dwelling"],
         "correct": 1,
         "expl": "Quality and care in generosity, not simply its bare occurrence."},
        {"q": "How does this discourse frame its own stakes, according to the guide?",
         "opts": [
             "In terms of merit and karma specifically",
             "Pragmatically, in terms of worth (alaṁ) — whether a visit is a good use of a "
             "mendicant's time",
             "In terms of eventual rebirth destination",
             "The discourse states no particular stakes"],
         "correct": 1,
         "expl": "A strikingly practical framing distinct from this discourse's doctrinal "
                 "neighbors."},
        {"q": "What does the guide say about this chapter's title, 'Tendencies,' in light of "
              "this discourse?",
         "opts": [
             "The title perfectly describes every discourse in the chapter equally",
             "Like several chapter titles already met in this series, it does not describe "
             "every discourse within it equally — this one concerns hospitality, not "
             "underlying tendencies",
             "This discourse actually belongs to a different chapter",
             "The chapter has no discernible title"],
         "correct": 1,
         "expl": "A pattern of chapter titles not uniformly matching every discourse, "
                 "already met elsewhere in this series."},
        {"q": "Is a setting stated for AN 7.13?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, despite its concrete practical subject matter."},
        {"q": "What are the first three factors of hospitality named in this discourse?",
         "opts": [
             "Faith, wisdom, and generosity",
             "Rising politely, bowing, and offering a seat",
             "Giving food, water, and shelter",
             "Reciting scripture, chanting, and meditating"],
         "correct": 1,
         "expl": "Basic courtesies opening the list, before it turns to the manner of "
                 "material generosity."},
    ],
    marginalia=[
        ("Seven factors of hospitality", [
            "rising, bowing, offering",
            "a seat &middot; sharing openly",
            "&middot; giving generously, carefully",
        ]),
        ("A sharp register shift", [
            "abstract tendencies (7.11/12)",
            "to concrete etiquette —",
            "'Tendencies' doesn't describe everything",
        ]),
        ("The manner, not just occurrence", [
            "not whether a family",
            "gives, but how much,",
            "how fine, how carefully",
        ]),
        ("Cross-references", [
            "AN 7.11/7.12 &middot; previous, this chapter's doctrinal opening pair",
        ]),
    ],
    further=[
        '<a href="%s/an7.13/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.12.html">AN 7.12 &middot; Underlying Tendencies (2nd)</a> &mdash; '
        "previous, this chapter's doctrinal opening pair.",
        '<a href="an-7.14.html">AN 7.14 &middot; Individuals</a> &mdash; next, seven types '
        "of noble persons worthy of offerings.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.14 — Puggalasutta
# --------------------------------------------------------------------------- #
page(
    14, "Puggala", "Individuals",
    vagga=VAGGA_2,
    meta_title="AN 7.14 — Individuals | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Puggalasutta, "
        "naming seven types of noble persons classified by their path and liberation, "
        "worthy of offerings and veneration. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list of person-types, stated once with no reversal"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The sevenfold classification of noble persons by mode of "
                              "liberation and stage of practice recurs throughout the "
                              "Chinese Āgamas and Abhidharma literature; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the first of a "
                       "recurring blurb family in this chapter — four further discourses "
                       "share this exact summary phrase but not this exact list"),
    ],
    why=(
        "AN 7.14 opens the first of five discourses in this chapter sharing the identical "
        "summary phrase, &ldquo;worthy of offerings... the supreme field of merit for the "
        "world&rdquo; &mdash; but this discourse's own seven-item list is genuinely its "
        "own: seven classifications of noble persons by mode of liberation and stage of "
        "practice, from the one freed both ways down to the follower by faith."),
    guide=[
        ("The teaching in one sentence", [
            "Seven individuals are worthy of offerings and veneration, the supreme field "
            "of merit for the world: the one freed both ways, the one freed by wisdom, the "
            "direct witness, the one attained to view, the one freed by faith, the "
            "follower of teachings, and the follower by faith."]),
        ("A checked caution for this chapter's remaining pages", [
            "AN 7.16, 7.17, 7.18, and 7.19, later in this chapter, all share this exact "
            "summary phrase &mdash; but checked term by term, none of their seven-item "
            "lists matches this discourse's classification by mode of liberation. Each "
            "shares only the concluding formula, not the specific content, a pattern this "
            "series has met repeatedly and must verify rather than assume here."]),
        ("Seven positions on a spectrum, not seven unrelated types", [
            "The list moves from the most complete attainment (ubhatobhāgavimutta, freed "
            "both ways, combining the deepest concentration with wisdom) down through "
            "progressively less complete combinations of the same underlying qualities "
            "&mdash; faith, wisdom, direct experience &mdash; ending with saddhānusārī, the "
            "follower by faith, who has not yet directly verified the teaching for "
            "themselves but proceeds on trust."]),
        ("Worthy regardless of stage, not only the most advanced", [
            "That all seven, from the fully liberated down to the faith-follower still "
            "early in the path, are named together as equally worthy of offerings "
            "suggests worthiness here is not reserved for the highest attainment alone, "
            "but extends across a genuine spectrum of genuine progress."]),
    ],
    terms=[
        ("ubhatobhāgavimutta",
         "&ldquo;freed both ways&rdquo; &mdash; the first and most complete of the seven, "
         "combining the deepest immersion attainments with liberating wisdom."),
        ("paññāvimutta, kāyasakkhī",
         "&ldquo;freed by wisdom, the direct witness&rdquo; &mdash; the second and third "
         "classifications, each combining wisdom and direct experience differently."),
        ("diṭṭhippatta, saddhāvimutta",
         "&ldquo;attained to view, freed by faith&rdquo; &mdash; the fourth and fifth "
         "classifications."),
        ("dhammānusārī, saddhānusārī",
         "&ldquo;the follower of teachings, the follower by faith&rdquo; &mdash; the sixth "
         "and seventh, least advanced classifications, proceeding by inference or trust "
         "rather than direct verification."),
        ("dakkhiṇeyya, āhuneyya",
         "&ldquo;worthy of a religious donation, worthy of offerings&rdquo; &mdash; two of "
         "several honorific terms this discourse's summary phrase applies to all seven "
         "classifications."),
    ],
    text_intro=(
        "The discourse in full: seven types of noble persons, classified by mode of "
        "liberation and stage of practice. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven individuals worthy of offerings"),
        ("p", "&sect;1", "an7.14:1.1-1.4"),
    ],
    quiz=[
        {"q": "What seven classifications does this discourse name?",
         "opts": [
             "The seven fetters of AN 7.8",
             "Seven types of noble persons by mode of liberation: freed both ways, freed "
             "by wisdom, direct witness, attained to view, freed by faith, follower of "
             "teachings, follower by faith",
             "The seven kinds of wealth of AN 7.5",
             "The seven powers of AN 7.3"],
         "correct": 1,
         "expl": "A spectrum of noble attainment, from most to least complete."},
        {"q": "What caution does the guide draw regarding this chapter's later discourses?",
         "opts": [
             "That every discourse sharing this summary phrase shares identical content",
             "That AN 7.16, 17, 18, and 19 all share this discourse's exact summary phrase "
             "but, checked term by term, name genuinely different seven-item lists",
             "That no other discourse in this chapter shares any similar phrasing",
             "That this discourse's list is repeated word for word later in the chapter"],
         "correct": 1,
         "expl": "A shared closing formula does not guarantee shared specific content, a "
                 "pattern requiring individual verification."},
        {"q": "How does the guide describe the movement across this discourse's seven "
              "classifications?",
         "opts": [
             "Seven entirely unrelated, unrankable types",
             "A spectrum from the most complete attainment (freed both ways) down through "
             "progressively less complete combinations, ending with the follower by faith",
             "A strictly chronological life story of one person",
             "Seven types with no relationship to liberation at all"],
         "correct": 1,
         "expl": "A graduated spectrum, not seven independent categories."},
        {"q": "What does the discourse suggest by naming all seven, from most to least "
              "advanced, as equally worthy of offerings?",
         "opts": [
             "That only the most advanced type is actually worthy",
             "That worthiness extends across a genuine spectrum of progress, not reserved "
             "for the highest attainment alone",
             "That the list is purely theoretical with no practical bearing",
             "That the least advanced type is actually the most worthy"],
         "correct": 1,
         "expl": "Worthiness spanning the whole spectrum of genuine practice."},
        {"q": "Is a setting stated for AN 7.14?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other list-form discourses."},
        {"q": "What does <em>saddhānusārī</em> mean?",
         "opts": ["Freed both ways", "The follower by faith", "The direct witness", "Freed by wisdom"],
         "correct": 1,
         "expl": "The seventh and least advanced classification, proceeding on trust rather "
                 "than direct verification."},
    ],
    marginalia=[
        ("Seven noble persons", [
            "freed both ways &middot;",
            "by wisdom &middot; direct witness",
            "&middot; view-attained &middot; faith-freed &middot; two followers",
        ]),
        ("A spectrum, not seven types", [
            "most to least complete",
            "attainment — faith, wisdom,",
            "direct experience combined variably",
        ]),
        ("A shared phrase, watch for later", [
            "AN 7.16/17/18/19 share",
            "this exact summary —",
            "check each list individually",
        ]),
        ("Cross-references", [
            "AN 7.16 &middot; later this chapter, a genuinely different list sharing this "
            "phrase",
        ]),
    ],
    further=[
        '<a href="%s/an7.14/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.13.html">AN 7.13 &middot; A Family</a> &mdash; previous, practical '
        "conduct toward lay households.",
        '<a href="an-7.15.html">AN 7.15 &middot; A Simile With Water</a> &mdash; next, a '
        "different sevenfold classification of persons entirely.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.15 — Udakūpamāsutta
# --------------------------------------------------------------------------- #
page(
    15, "Udakūpamā", "A Simile With Water",
    vagga=VAGGA_2,
    meta_title="AN 7.15 — A Simile With Water | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Udakūpamāsutta, mapping seven types of people onto seven stages of drowning and "
        "swimming — from the worldling who sinks and stays under to the arahant standing "
        "on solid ground. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "An extended simile: seven types of people in water, each explained in "
                 "turn and mapped onto a specific stage of spiritual progress"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The water simile for stages of spiritual progress, from "
                              "complete submersion to standing on the far shore, recurs "
                              "widely across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; this chapter's longest "
                       "and most fully developed discourse, mapping a memorable image onto "
                       "the entire path from worldling to arahant"),
    ],
    why=(
        "AN 7.15 is a genuinely different sevenfold classification from AN 7.14's, despite "
        "both concerning seven types of people: here, seven people are compared to seven "
        "positions in water &mdash; sinking and staying under, rising then sinking, rising "
        "then staying put, rising then seeing and discerning, rising then crossing over, "
        "rising then finding a foothold, and finally standing on solid ground on the far "
        "shore &mdash; each explicitly mapped onto a specific stage from complete "
        "unwholesomeness through full awakening."),
    guide=[
        ("The teaching in one sentence", [
            "Seven people are like seven positions in water: one sinks and stays under "
            "(exclusively unwholesome), one rises then sinks (fleeting faith that "
            "dwindles), one rises then stays put (stable but undeveloped faith), one rises "
            "then sees and discerns (stream-entry), one rises then crosses over "
            "(once-return), one rises then finds a foothold (non-return), and one has "
            "risen, crossed over, and stands on solid ground on the far shore (full "
            "awakening)."]),
        ("A genuinely different list from AN 7.14, sharing only the number seven", [
            "Checked term by term, this discourse's seven water-positions have nothing in "
            "common with AN 7.14's seven modes of liberation beyond both classifying "
            "spiritual progress into seven stages. Where AN 7.14 named technical "
            "categories (freed both ways, freed by wisdom, and so on), this discourse uses "
            "an extended, unified image, tracking one continuous scene of rising, sinking, "
            "and swimming rather than naming discrete types."]),
        ("The middle five stages, defined by faith's fate", [
            "Types two through six all begin identically: &ldquo;rising up,&rdquo; the "
            "person thinks, &ldquo;it's good to have faith, conscience, prudence, energy, "
            "and wisdom regarding skillful qualities.&rdquo; What distinguishes each stage "
            "is what happens to that faith afterward &mdash; whether it dwindles away "
            "(type 2), merely holds steady (type 3), or becomes the basis for progressively "
            "ending fetters through stream-entry, once-return, and non-return (types 4 "
            "through 6)."]),
        ("Types 6 and 7, the closing pair", [
            "Type 6, ending the five lower fetters, describes the non-returner, reborn "
            "spontaneously and never returning to this world. Type 7, the discourse's "
            "final and most complete image, describes one who has &ldquo;risen up, crossed "
            "over, and gone to the far shore, a brahmin who stands on solid ground&rdquo; "
            "&mdash; realizing the undefiled freedom of heart and wisdom, the arahant's "
            "full awakening."]),
    ],
    terms=[
        ("udakūpamā",
         "&ldquo;simile with water&rdquo; &mdash; this discourse's own title, its unifying "
         "extended image."),
        ("sakiṁ nimujjitvā nimuggova tiṭṭhati",
         "&ldquo;sinks under once and stays under&rdquo; &mdash; the first and lowest "
         "type, exclusively dark, unskillful qualities."),
        ("ummujjitvā apāraṅgato pāraṅgato tiṭṭhati thale titthaṁ brāhmaṇo",
         "&ldquo;has risen up, crossed over, gone to the far shore, a brahmin who stands "
         "on solid ground&rdquo; &mdash; the seventh and final type, the arahant's full "
         "awakening."),
        ("saddhā, hiri, ottappa, vīriya, paññā",
         "&ldquo;faith, conscience, prudence, energy, wisdom&rdquo; &mdash; the five "
         "qualities each of types two through six reflects on gaining, distinguished by "
         "what happens to them afterward."),
        ("sotāpanna, sakadāgāmī, anāgāmī",
         "&ldquo;stream-enterer, once-returner, non-returner&rdquo; &mdash; the three "
         "noble stages types four, five, and six are explicitly identified with."),
    ],
    text_intro=(
        "The discourse in full: seven people compared to seven positions in water, each "
        "explained and mapped onto a stage of spiritual progress. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven types, introduced"),
        ("p", "&sect;1", "an7.15:1.1-1.9"),
        ("h3", "Type 1: sinks under once and stays under"),
        ("p", "&sect;2", "an7.15:2.1-2.3"),
        ("h3", "Type 2: rises then sinks under"),
        ("p", "&sect;3", "an7.15:3.1-3.10"),
        ("h3", "Type 3: rises then stays put"),
        ("p", "&sect;4", "an7.15:4.1-4.11"),
        ("h3", "Type 4: rises then sees and discerns (stream-entry)"),
        ("p", "&sect;5", "an7.15:5.1-5.7"),
        ("h3", "Type 5: rises then crosses over (once-return)"),
        ("p", "&sect;6", "an7.15:6.1-6.7"),
        ("h3", "Type 6: rises then finds a foothold (non-return)"),
        ("p", "&sect;7", "an7.15:7.1-7.7"),
        ("h3", "Type 7: crosses to the far shore (full awakening)"),
        ("p", "&sect;8", "an7.15:8.1-9.1"),
    ],
    quiz=[
        {"q": "How does this discourse's classification compare to AN 7.14's, both naming "
              "seven types of people?",
         "opts": [
             "Identical content, just reworded",
             "Genuinely different — this discourse uses an extended water image tracking "
             "one continuous scene, rather than naming discrete technical categories as AN "
             "7.14 did",
             "This discourse has no actual classification at all",
             "Only the number seven differs between the two"],
         "correct": 1,
         "expl": "Two distinct sevenfold classifications sharing only the number seven."},
        {"q": "What distinguishes types two through six from each other, according to the "
              "guide?",
         "opts": [
             "Nothing — they are identical",
             "What happens to the same initial faith afterward — whether it dwindles, "
             "merely holds steady, or becomes the basis for progressively ending fetters",
             "The order in which they appear in the discourse only",
             "Which specific deity they encounter"],
         "correct": 1,
         "expl": "A single starting reflection, diverging by what follows it."},
        {"q": "What does type 1, sinking and staying under, represent?",
         "opts": [
             "A stream-enterer",
             "Someone with exclusively dark, unskillful qualities",
             "An arahant",
             "A once-returner"],
         "correct": 1,
         "expl": "The lowest position in this discourse's water simile."},
        {"q": "What does type 7, the discourse's final image, represent?",
         "opts": [
             "A stream-enterer only",
             "Full awakening — one who has risen, crossed over, and stands on solid ground "
             "on the far shore, realizing undefiled freedom of heart and wisdom",
             "A worldling with no spiritual progress",
             "A non-returner, not yet fully awakened"],
         "correct": 1,
         "expl": "The arahant, the discourse's most complete image."},
        {"q": "What three noble stages are types 4, 5, and 6 explicitly identified with?",
         "opts": [
             "The three fetters of AN 7.8",
             "Stream-entry, once-return, and non-return",
             "The three poisons",
             "Faith, wisdom, and energy"],
         "correct": 1,
         "expl": "A direct mapping onto three of the four traditional stages of "
                 "awakening."},
        {"q": "Is a setting stated for AN 7.15?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, despite this discourse's extended narrative simile."},
        {"q": "What happens to type 2's faith, distinguishing it from type 3?",
         "opts": [
             "It grows stronger over time, unlike type 3's",
             "It dwindles away, where type 3's faith merely holds steady, neither "
             "dwindling nor growing",
             "Both types' faith is identical in every respect",
             "Type 2 has no faith at all"],
         "correct": 1,
         "expl": "A fine distinction between fleeting and merely stable, still-undeveloped "
                 "faith."},
    ],
    marginalia=[
        ("Seven positions in water", [
            "sinks &middot; rises-sinks",
            "&middot; stays put &middot; sees, discerns",
            "&middot; crosses &middot; finds foothold &middot; far shore",
        ]),
        ("Mapped onto the path", [
            "worldling &middot; fading faith",
            "&middot; stable faith &middot; stream-enterer",
            "&middot; once-returner &middot; non-returner &middot; arahant",
        ]),
        ("One reflection, five outcomes", [
            "'good to have faith,",
            "conscience...' — then",
            "diverging by what follows",
        ]),
        ("Cross-references", [
            "AN 7.14 &middot; previous, a genuinely different sevenfold classification",
        ]),
    ],
    further=[
        '<a href="%s/an7.15/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.14.html">AN 7.14 &middot; Individuals</a> &mdash; previous, a '
        "genuinely different sevenfold classification.",
        '<a href="an-7.16.html">AN 7.16 &middot; Observing Impermanence</a> &mdash; next, '
        "sharing AN 7.14's summary phrase but not its content.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.16 — Aniccānupassīsutta
# --------------------------------------------------------------------------- #
page(
    16, "Aniccānupassī", "Observing Impermanence",
    vagga=VAGGA_2,
    meta_title="AN 7.16 — Observing Impermanence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Aniccānupassīsutta, opening a tetrad of discourses classifying seven types of "
        "people who meditate on impermanence, by how and when their defilements finally "
        "end. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Seven types of meditators on impermanence, classified by the manner and "
                 "timing of their final liberation — opening a tetrad sharing AN 7.14's "
                 "summary phrase with genuinely different content"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The sevenfold classification of non-returners by manner of "
                              "final attainment (antarā-parinibbāyī and its companions) "
                              "recurs throughout the Chinese Āgamas and Abhidharma "
                              "literature; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a third, genuinely "
                       "distinct sevenfold classification in this chapter, worth checking "
                       "against AN 7.14 rather than assuming identity from the shared "
                       "closing phrase"),
    ],
    why=(
        "AN 7.16 shares AN 7.14's exact closing phrase &mdash; &ldquo;worthy of "
        "offerings... the supreme field of merit for the world&rdquo; &mdash; but names a "
        "third, genuinely distinct sevenfold classification: seven types of people who "
        "meditate observing impermanence in all conditions, distinguished by exactly how "
        "and when their defilements come to a final end, from full arahantship in this "
        "very life through six further variations on non-return."),
    guide=[
        ("The teaching in one sentence", [
            "Seven people meditate observing impermanence in all conditions, distinguished "
            "by how their defilements finally end: the first realizes full awakening in "
            "this very life; the second ends defilements and life at the same moment; the "
            "remaining five, having ended the five lower fetters, are extinguished in one "
            "of five different specific ways."]),
        ("Checked against AN 7.14: a genuinely different list", [
            "AN 7.14 classified seven persons by mode of liberation (freed both ways, "
            "freed by wisdom, and so on) without reference to any specific meditation "
            "practice. This discourse instead specifies one meditation object, "
            "impermanence, and classifies seven outcomes by the precise manner and timing "
            "of final liberation &mdash; a different organizing principle entirely, "
            "despite the identical closing formula."]),
        ("Two full types, then five compressed variations", [
            "This discourse spells out its first two types in some detail &mdash; full "
            "awakening in this life, and awakening simultaneous with death &mdash; then "
            "compresses the remaining five types, all sharing the ending of the five "
            "lower fetters, into a single dense passage naming five specific manners of "
            "the non-returner's extinguishment: between one life and the next, upon "
            "landing, without extra effort, with extra effort, and heading upstream to the "
            "Akaniṭṭha realm."]),
        ("Opening a tetrad, not a lone discourse", [
            "AN 7.17, 7.18, and 7.19, immediately following, will each repeat this exact "
            "sevenfold structure &mdash; two full types plus five compressed variations "
            "&mdash; changing only the meditation object: suffering, not-self, and finally "
            "the happiness of extinguishment itself."]),
    ],
    terms=[
        ("aniccānupassī",
         "&ldquo;observing impermanence&rdquo; &mdash; this discourse's own title and "
         "meditation object, the first of four such objects this tetrad will use."),
        ("diṭṭheva dhamme aññā",
         "&ldquo;realizing the undefiled freedom... in this very life&rdquo; &mdash; the "
         "first type, full arahantship attained before death."),
        ("upapajjavedanīye āsavā parikkhīṇā",
         "&ldquo;defilements and life come to an end at exactly the same time&rdquo; "
         "&mdash; the second type, an ending simultaneous with death itself."),
        ("antarāparinibbāyī, upahaccaparinibbāyī, asaṅkhāraparinibbāyī, "
         "sasaṅkhāraparinibbāyī, uddhaṁsota akaniṭṭhagāmī",
         "the five specific manners of the non-returner's extinguishment named for types "
         "three through seven: between lives, upon landing, without extra effort, with "
         "extra effort, and heading upstream to the Akaniṭṭha realm."),
        ("āhuneyyā... anuttaraṁ puññakkhettaṁ lokassa",
         "&ldquo;worthy of offerings... the supreme field of merit for the world&rdquo; "
         "&mdash; the closing formula shared word for word with AN 7.14, despite this "
         "discourse's entirely different seven-item content."),
    ],
    text_intro=(
        "The discourse in full: seven types of meditators on impermanence, classified by "
        "how and when their defilements end. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first individual: full awakening in this life"),
        ("p", "&sect;1", "an7.16:1.1-1.5"),
        ("h3", "The second individual: ending simultaneous with death"),
        ("p", "&sect;2", "an7.16:2.1-2.3"),
        ("h3", "The third through seventh individuals: five manners of non-return"),
        ("p", "&sect;3", "an7.16:3.1-3.8"),
    ],
    quiz=[
        {"q": "How does this discourse's classification compare to AN 7.14's, despite "
              "sharing its exact closing phrase?",
         "opts": [
             "Identical content, just reworded",
             "A genuinely different organizing principle — classifying seven outcomes by "
             "the manner and timing of final liberation through impermanence-meditation, "
             "rather than AN 7.14's modes of liberation",
             "This discourse has no actual seven-item list",
             "The two discourses concern entirely unrelated topics with no overlap "
             "whatsoever"],
         "correct": 1,
         "expl": "A shared closing formula, genuinely different specific content."},
        {"q": "What distinguishes the first two types in this discourse?",
         "opts": [
             "Nothing — they are identical",
             "The first realizes full awakening in this very life; the second ends "
             "defilements and life simultaneously",
             "The first is a stream-enterer, the second a once-returner",
             "Both types describe the same non-returner"],
         "correct": 1,
         "expl": "Two distinct timings of the highest attainment relative to death."},
        {"q": "What do types three through seven all share in common?",
         "opts": [
             "None have ended any fetters",
             "All have ended the five lower fetters, differing only in the specific manner "
             "of their extinguishment",
             "All are full arahants already",
             "All are worldlings with no attainment"],
         "correct": 1,
         "expl": "Five variations on the non-returner's mode of final extinguishment."},
        {"q": "What does this discourse open, according to the guide?",
         "opts": [
             "An isolated, standalone teaching",
             "A tetrad — AN 7.17, 7.18, and 7.19 will repeat this exact structure with "
             "different meditation objects: suffering, not-self, and the happiness of "
             "extinguishment",
             "A return to AN 7.14's exact content",
             "The chapter's final discourse"],
         "correct": 1,
         "expl": "The template for three further discourses sharing this same sevenfold "
                 "structure."},
        {"q": "Is a setting stated for AN 7.16?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other list-form discourses."},
        {"q": "What meditation object does this discourse specify, unlike AN 7.14?",
         "opts": [
             "Suffering", "Impermanence", "Not-self", "The happiness of extinguishment"],
         "correct": 1,
         "expl": "The first of four meditation objects this tetrad will use in turn."},
    ],
    marginalia=[
        ("Seven outcomes of one practice", [
            "meditating on impermanence —",
            "arahant in this life,",
            "or death-simultaneous, or 5 modes of non-return",
        ]),
        ("Same phrase, different list", [
            "shares AN 7.14's exact",
            "closing formula —",
            "a genuinely distinct classification",
        ]),
        ("Opening a tetrad", [
            "AN 7.17, 18, 19",
            "repeat this structure —",
            "suffering, not-self, extinguishment",
        ]),
        ("Cross-references", [
            "AN 7.14 &middot; earlier, sharing this exact closing phrase, different content",
            "AN 7.17 &middot; next, the same structure applied to suffering",
        ]),
    ],
    further=[
        '<a href="%s/an7.16/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.14.html">AN 7.14 &middot; Individuals</a> &mdash; earlier, sharing '
        "this discourse's exact closing phrase over different content.",
        '<a href="an-7.17.html">AN 7.17 &middot; Observing Suffering</a> &mdash; next, the '
        "identical structure applied to suffering.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.17 — Dukkhānupassīsutta
# --------------------------------------------------------------------------- #
page(
    17, "Dukkhānupassī", "Observing Suffering",
    vagga=VAGGA_2,
    meta_title="AN 7.17 — Observing Suffering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dukkhānupassīsutta, restating AN 7.16's exact sevenfold structure with suffering "
        "as the meditation object, compressed almost entirely via Pāli ellipsis. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical sevenfold structure as AN 7.16, compressed to a single "
                 "changed opening clause via Pāli ellipsis"),
        ("Length", "under 30 seconds to read"),
        ("Northern parallel", "The application of the same liberation-classification "
                              "structure to multiple meditation objects in sequence recurs "
                              "across the Chinese Āgamas' abbreviation series; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; almost entirely elided, "
                       "pointing back to AN 7.16 for its full content"),
    ],
    why=(
        "AN 7.17 restates AN 7.16's entire sevenfold structure &mdash; two full types plus "
        "five compressed variations of non-return &mdash; changing only the meditation "
        "object from impermanence to suffering, and compresses the entire discourse to "
        "barely more than its opening clause via the Pāli ellipsis &ldquo;…pe…&rdquo;."),
    guide=[
        ("The teaching in one sentence", [
            "The same seven outcomes already detailed at AN 7.16 for impermanence-"
            "meditation apply identically to suffering-meditation: full awakening in this "
            "life, ending simultaneous with death, or one of five manners of non-return."]),
        ("Almost total compression", [
            "Where AN 7.16 spelled out its content across three sections, this discourse's "
            "source text gives only the opening clause &mdash; &ldquo;meditates observing "
            "suffering in all conditions&rdquo; &mdash; before eliding everything else with "
            "&ldquo;…pe….&rdquo; A reader who has read AN 7.16 can supply the entire "
            "remaining content without difficulty."]),
        ("Suffering as the second of four objects", [
            "This tetrad, opened at AN 7.16 with impermanence, continues here with "
            "suffering, the second of the three characteristics already met together at "
            "AN 6.98&ndash;101 and AN 6.142 in the previous nipāta, now applied "
            "individually to this chapter's sevenfold liberation-classification."]),
        ("The same care required, despite the brevity", [
            "Though this discourse's own text is nearly empty of content, the underlying "
            "teaching it represents is the full sevenfold classification already detailed "
            "at AN 7.16 &mdash; brevity here reflects compression, not a genuinely "
            "different or lesser teaching."]),
    ],
    terms=[
        ("dukkhānupassī",
         "&ldquo;observing suffering&rdquo; &mdash; this discourse's own title and "
         "meditation object, replacing AN 7.16's impermanence."),
        ("…pe…",
         "the Pāli ellipsis mark, standing in here for nearly the entirety of AN 7.16's "
         "sevenfold structure, unchanged beyond the opening clause."),
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; the second of the three characteristics, "
         "following impermanence at AN 7.16 and preceding not-self at AN 7.18."),
        ("sattamaṁ",
         "&ldquo;the seventh&rdquo; &mdash; the source colophon's ordinal marking this "
         "discourse's position within its chapter."),
        ("āhuneyyā... anuttaraṁ puññakkhettaṁ lokassa",
         "the same closing formula shared across AN 7.14 and this entire tetrad, assumed "
         "here without being spelled out."),
    ],
    text_intro=(
        "The formula exactly as the source compresses it: the same sevenfold structure as "
        "AN 7.16, applied to suffering. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The compressed formula"),
        ("p", "&sect;1", "an7.17:1.1-1.3"),
    ],
    quiz=[
        {"q": "What does this discourse's content represent?",
         "opts": [
             "An entirely new sevenfold classification",
             "The identical sevenfold structure as AN 7.16, with suffering replacing "
             "impermanence as the meditation object",
             "A four-item list unrelated to AN 7.16",
             "A repeat of AN 7.14's content"],
         "correct": 1,
         "expl": "The same seven outcomes, compressed to a changed opening clause."},
        {"q": "How compressed is this discourse's own text?",
         "opts": [
             "Fully spelled out, matching AN 7.16's length",
             "Almost total compression — only the opening clause is given before '…pe…' "
             "elides the rest",
             "Only the closing formula is given",
             "The discourse has no text at all"],
         "correct": 1,
         "expl": "A reader who has read AN 7.16 can supply the entire remaining content."},
        {"q": "What position does suffering occupy within this tetrad's four meditation "
              "objects?",
         "opts": [
             "First, opening the tetrad",
             "Second, following impermanence at AN 7.16 and preceding not-self at AN 7.18",
             "Third",
             "Fourth and final"],
         "correct": 1,
         "expl": "The second of four objects this tetrad applies to the same sevenfold "
                 "structure."},
        {"q": "Does this discourse's brevity indicate a lesser or different teaching, "
              "according to the guide?",
         "opts": [
             "Yes, a significantly reduced teaching",
             "No — brevity here reflects compression alone; the underlying teaching is the "
             "full sevenfold classification already detailed at AN 7.16",
             "Yes, this discourse contradicts AN 7.16",
             "The discourse has no relationship to AN 7.16 at all"],
         "correct": 1,
         "expl": "Compression, not reduction — the same content, differently presented."},
        {"q": "Is a setting stated for AN 7.17?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, as compressed as the rest of this discourse's content."},
        {"q": "What does <em>dukkhānupassī</em> mean?",
         "opts": ["Observing impermanence", "Observing suffering", "Observing not-self", "Observing happiness"],
         "correct": 1,
         "expl": "This discourse's own title and meditation object."},
    ],
    marginalia=[
        ("Nearly total elision", [
            "only the opening clause",
            "spelled out — '…pe…'",
            "for the rest of AN 7.16's structure",
        ]),
        ("Suffering, the second object", [
            "impermanence (7.16),",
            "suffering (7.17),",
            "not-self and happiness to follow",
        ]),
        ("Compression, not reduction", [
            "the full sevenfold",
            "classification still applies —",
            "only the presentation is brief",
        ]),
        ("Cross-references", [
            "AN 7.16 &middot; previous, this discourse's full template",
            "AN 7.18 &middot; next, the same structure applied to not-self",
        ]),
    ],
    further=[
        '<a href="%s/an7.17/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.16.html">AN 7.16 &middot; Observing Impermanence</a> &mdash; '
        "previous, this discourse's full template.",
        '<a href="an-7.18.html">AN 7.18 &middot; Observing Not-self</a> &mdash; next, the '
        "same structure applied to not-self.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.18 — Anattānupassīsutta
# --------------------------------------------------------------------------- #
page(
    18, "Anattānupassī", "Observing Not-self",
    vagga=VAGGA_2,
    meta_title="AN 7.18 — Observing Not-self | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Anattānupassīsutta, the most compressed discourse in this collection so far — a "
        "single elided clause applying AN 7.16's sevenfold structure to not-self. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical sevenfold structure as AN 7.16, compressed to a single "
                 "elided line"),
        ("Length", "under 15 seconds to read"),
        ("Northern parallel", "The extension of a liberation-classification structure "
                              "across the three characteristics recurs across the Chinese "
                              "Āgamas' abbreviation series; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the single most "
                       "compressed discourse in this collection to date, one elided line "
                       "and an ordinal"),
    ],
    why=(
        "AN 7.18 compresses even further than AN 7.17: a single line, &ldquo;meditates "
        "observing not-self in all things,&rdquo; followed immediately by &ldquo;…pe….&rdquo; "
        "and the source's own ordinal marker. This is the briefest discourse in this "
        "collection so far, shorter even than AN 6.90 within the previous nipāta."),
    guide=[
        ("The teaching in one sentence", [
            "The same seven outcomes already detailed at AN 7.16 apply identically to "
            "not-self meditation: full awakening in this life, ending simultaneous with "
            "death, or one of five manners of non-return."]),
        ("The briefest discourse in this collection to date", [
            "AN 6.90, within the previous nipāta, held the record for this collection's "
            "shortest discourse: one sentence beyond title and setting. This discourse is "
            "shorter still &mdash; a single clause naming its meditation object, followed "
            "by the ellipsis marking everything else as already given."]),
        ("Not-self, completing the three characteristics", [
            "With impermanence (AN 7.16) and suffering (AN 7.17) already applied to this "
            "sevenfold structure, this discourse completes the standard three "
            "characteristics with not-self &mdash; the same trio already treated together "
            "in the previous nipāta at AN 6.98&ndash;101 and individually at AN 6.142, now "
            "each given their own discourse within this chapter's tetrad."]),
        ("One object remains", [
            "AN 7.19, immediately following, will complete this tetrad with a fourth "
            "object beyond the three characteristics: the happiness of extinguishment "
            "itself, applied to the identical sevenfold structure one final time."]),
    ],
    terms=[
        ("anattānupassī",
         "&ldquo;observing not-self&rdquo; &mdash; this discourse's own title and "
         "meditation object, completing the three characteristics within this tetrad."),
        ("…pe…",
         "the Pāli ellipsis mark, here standing in for nearly this entire discourse's "
         "content beyond its single opening clause."),
        ("aṭṭhamaṁ",
         "&ldquo;the eighth&rdquo; &mdash; the source colophon's ordinal, this "
         "discourse's own entire second line."),
        ("anicca, dukkha, anatta",
         "&ldquo;impermanent, suffering, not-self&rdquo; &mdash; the three characteristics, "
         "now individually applied across AN 7.16, 7.17, and this discourse."),
        ("āhuneyyā... anuttaraṁ puññakkhettaṁ lokassa",
         "the same closing formula shared across this entire tetrad and AN 7.14, assumed "
         "here without being spelled out at all."),
    ],
    text_intro=(
        "The formula exactly as the source compresses it: the same sevenfold structure as "
        "AN 7.16, applied to not-self, in a single elided line. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The compressed formula"),
        ("p", "&sect;1", "an7.18:1.1-1.1"),
    ],
    quiz=[
        {"q": "How does this discourse's length compare to the rest of this collection, "
              "according to the guide?",
         "opts": [
             "Average length for this collection",
             "The single most compressed discourse to date, shorter even than AN 6.90 in "
             "the previous nipāta",
             "The longest discourse in this chapter",
             "Identical in length to AN 7.15"],
         "correct": 1,
         "expl": "A new record for brevity within this series."},
        {"q": "What does this discourse's content represent?",
         "opts": [
             "An entirely new classification unrelated to AN 7.16",
             "The identical sevenfold structure as AN 7.16, with not-self replacing "
             "impermanence as the meditation object",
             "A four-item list",
             "A repeat of AN 7.13's content"],
         "correct": 1,
         "expl": "The same seven outcomes, compressed to a single elided line."},
        {"q": "What does this discourse complete, according to the guide?",
         "opts": [
             "Nothing — an isolated compression",
             "The three characteristics (impermanence, suffering, not-self) individually "
             "applied across AN 7.16, 7.17, and this discourse",
             "The entire chapter",
             "The entire Sevens collection"],
         "correct": 1,
         "expl": "The third of three characteristics already treated together in the "
                 "previous nipāta."},
        {"q": "What comes next in this tetrad, according to the guide?",
         "opts": [
             "The tetrad ends here",
             "AN 7.19, applying the identical structure to a fourth object beyond the "
             "three characteristics: the happiness of extinguishment",
             "A return to AN 7.14's content",
             "A shift to an unrelated topic"],
         "correct": 1,
         "expl": "One further discourse completes this four-part tetrad."},
        {"q": "Is a setting stated for AN 7.18?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, as compressed as the rest of this discourse."},
        {"q": "What does <em>anattānupassī</em> mean?",
         "opts": ["Observing impermanence", "Observing suffering", "Observing not-self", "Observing happiness"],
         "correct": 2,
         "expl": "This discourse's own title and meditation object."},
    ],
    marginalia=[
        ("This collection's briefest yet", [
            "one clause, then '…pe…' —",
            "shorter even than",
            "AN 6.90's single sentence",
        ]),
        ("Completing the three characteristics", [
            "impermanence (7.16),",
            "suffering (7.17),",
            "not-self (7.18) — all applied",
        ]),
        ("One object remains", [
            "AN 7.19 will close",
            "this tetrad with",
            "the happiness of extinguishment",
        ]),
        ("Cross-references", [
            "AN 7.16 &middot; earlier, this discourse's full template",
            "AN 6.98–101 &middot; earlier nipāta, the three characteristics treated "
            "together",
        ]),
    ],
    further=[
        '<a href="%s/an7.18/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.16.html">AN 7.16 &middot; Observing Impermanence</a> &mdash; '
        "earlier, this discourse's full template.",
        '<a href="an-7.19.html">AN 7.19 &middot; Extinguishment</a> &mdash; next, closing '
        "this tetrad with a fourth meditation object.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.19 — Nibbānasutta
# --------------------------------------------------------------------------- #
page(
    19, "Nibbāna", "Extinguishment",
    vagga=VAGGA_2,
    meta_title="AN 7.19 — Extinguishment | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nibbānasutta, "
        "closing this tetrad by applying AN 7.16's sevenfold structure to the happiness of "
        "extinguishment, spelled out in full rather than elided. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical sevenfold structure as AN 7.16, spelled out in full rather "
                 "than elided — closing this tetrad on a fourth, distinct meditation "
                 "object"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Meditating on the happiness, rather than the peace, of "
                              "extinguishment recurs in related forms across the Chinese "
                              "Āgamas' treatment of nibbāna; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; closes this tetrad with "
                       "a fourth object departing from the three characteristics, spelled "
                       "out fully like AN 7.16"),
    ],
    why=(
        "AN 7.19 closes this tetrad with a genuine departure from AN 7.16&ndash;18's "
        "pattern: rather than a fourth characteristic of conditioned existence, this "
        "discourse's meditation object is extinguishment itself, observed specifically as "
        "happiness &mdash; and, like AN 7.16 but unlike AN 7.17 and 7.18, the source "
        "spells this discourse out in full rather than eliding it."),
    guide=[
        ("The teaching in one sentence", [
            "The same seven outcomes already detailed at AN 7.16 apply to meditation on "
            "the happiness of extinguishment: full awakening in this life, ending "
            "simultaneous with death, or one of five manners of non-return."]),
        ("Extinguishment, not a fourth characteristic", [
            "Impermanence, suffering, and not-self (AN 7.16&ndash;18) are all "
            "characteristics of conditioned existence; extinguishment is this literature's "
            "term for the unconditioned. This discourse's object is thus not a fourth item "
            "in the same series as the first three, but a genuine category shift, echoing "
            "the same move already made at AN 6.101 within the previous nipāta, where "
            "regarding extinguishment specifically required its own full treatment rather "
            "than simple elision."]),
        ("Happiness, not merely peace", [
            "This discourse specifies observing sukha, happiness, in extinguishment, "
            "rather than the more commonly emphasized santi, peace, or the simple absence "
            "of suffering &mdash; framing the unconditioned in explicitly positive, felt "
            "terms rather than only as a cessation."]),
        ("Why this discourse is spelled out, like AN 7.16", [
            "Just as AN 6.101's shift to the unconditioned required full text rather than "
            "elision, this discourse's shift from characteristics of conditioned existence "
            "to extinguishment itself is significant enough that the source gives its "
            "entire sevenfold structure in full, rather than compressing it as it did for "
            "AN 7.17 and 7.18's more straightforward continuations of the same "
            "characteristic-based series."]),
    ],
    terms=[
        ("nibbāne sukhānupassī",
         "&ldquo;observing the happiness in extinguishment&rdquo; &mdash; this discourse's "
         "own meditation object, framing the unconditioned in positive, felt terms."),
        ("sukha",
         "&ldquo;happiness&rdquo; &mdash; the specific quality this discourse observes in "
         "extinguishment, distinct from the more commonly emphasized peace."),
        ("saṅkhata, asaṅkhata",
         "&ldquo;conditioned, unconditioned&rdquo; &mdash; the underlying distinction "
         "behind this discourse's category shift, echoing the identical move already made "
         "at AN 6.101 in the previous nipāta."),
        ("antarāparinibbāyī, upahaccaparinibbāyī, asaṅkhāraparinibbāyī, "
         "sasaṅkhāraparinibbāyī, uddhaṁsota akaniṭṭhagāmī",
         "the same five manners of non-return already named at AN 7.16, restated here in "
         "full for types three through seven."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; this discourse's own title term and "
         "meditation object, closing this tetrad on the unconditioned rather than a fourth "
         "characteristic."),
    ],
    text_intro=(
        "The discourse in full: seven types of meditators on the happiness of "
        "extinguishment, classified by how and when their defilements end. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first individual: full awakening in this life"),
        ("p", "&sect;1", "an7.19:1.1-1.3"),
        ("h3", "The second individual: ending simultaneous with death"),
        ("p", "&sect;2", "an7.19:2.1-2.3"),
        ("h3", "The third through seventh individuals: five manners of non-return"),
        ("p", "&sect;3", "an7.19:3.1-3.8"),
    ],
    quiz=[
        {"q": "How does this discourse's meditation object differ from AN 7.16–18's, "
              "according to the guide?",
         "opts": [
             "No difference — it is a fourth characteristic in the same series",
             "A genuine category shift — extinguishment is the unconditioned, not a fourth "
             "characteristic of conditioned existence like impermanence, suffering, and "
             "not-self",
             "This discourse names no meditation object at all",
             "It is identical to AN 7.16's impermanence"],
         "correct": 1,
         "expl": "A shift from conditioned characteristics to the unconditioned itself."},
        {"q": "What specific quality does this discourse observe in extinguishment, rather "
              "than the more commonly emphasized peace?",
         "opts": [
             "Emptiness", "Happiness (sukha)", "Silence", "Distance"],
         "correct": 1,
         "expl": "A positive, felt framing of the unconditioned."},
        {"q": "Why is this discourse spelled out in full, unlike AN 7.17 and 7.18, "
              "according to the guide?",
         "opts": [
             "For no particular reason — the source is simply inconsistent",
             "Its shift to the unconditioned is significant enough to require full text, "
             "echoing the same move already made at AN 6.101 in the previous nipāta",
             "Because it is the tetrad's first discourse",
             "Because it contradicts AN 7.16's teaching"],
         "correct": 1,
         "expl": "A structural echo of AN 6.101's earlier shift to the unconditioned."},
        {"q": "What connects this discourse's structure to AN 7.16's?",
         "opts": [
             "No connection at all",
             "The identical sevenfold classification by manner and timing of final "
             "liberation, now applied to extinguishment as the meditation object",
             "Only the setting is shared",
             "This discourse reverses AN 7.16's teaching entirely"],
         "correct": 1,
         "expl": "The same seven outcomes, applied to a fourth and category-shifting "
                 "object."},
        {"q": "Is a setting stated for AN 7.19?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching this tetrad's other discourses."},
        {"q": "What does this discourse close, according to the guide?",
         "opts": [
             "Nothing — further discourses in this exact tetrad follow",
             "The four-discourse tetrad begun at AN 7.16, having now applied the identical "
             "sevenfold structure to impermanence, suffering, not-self, and extinguishment",
             "The entire chapter",
             "The entire Sevens collection"],
         "correct": 1,
         "expl": "The tetrad's fourth and final meditation object."},
    ],
    marginalia=[
        ("A category shift", [
            "not a fourth characteristic —",
            "extinguishment itself,",
            "the unconditioned",
        ]),
        ("Happiness, not merely peace", [
            "sukha specifically —",
            "a positive, felt framing",
            "of the unconditioned",
        ]),
        ("Spelled out, like AN 7.16", [
            "significant enough",
            "for full text, echoing",
            "AN 6.101's earlier shift",
        ]),
        ("Cross-references", [
            "AN 7.16–18 &middot; earlier, this tetrad's three characteristic-based "
            "discourses",
            "AN 6.101 &middot; earlier nipāta, the same structural shift to the "
            "unconditioned",
        ]),
    ],
    further=[
        '<a href="%s/an7.19/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.18.html">AN 7.18 &middot; Observing Not-self</a> &mdash; previous, '
        "closing this tetrad's three characteristic-based discourses.",
        '<a href="an-7.20.html">AN 7.20 &middot; Qualifications for Graduation</a> &mdash; '
        "next, closing this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.20 — Niddasavatthusutta
# --------------------------------------------------------------------------- #
page(
    20, "Niddasavatthu", "Qualifications for Graduation",
    vagga=VAGGA_2,
    meta_title="AN 7.20 — Qualifications for Graduation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Niddasavatthusutta, closing this chapter with seven qualities of sustained keen "
        "enthusiasm that qualify a mendicant to graduate from training. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list of sustained enthusiasms, closing this chapter"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The image of graduating from a training already completed "
                              "recurs widely across the Chinese Āgamas' descriptions of the "
                              "arahant's finished task; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "closing this chapter with a compact seven-item list"),
    ],
    why=(
        "AN 7.20 closes this chapter with seven qualifications for graduation "
        "(niddasavatthu) &mdash; keen enthusiasm sustained toward undertaking the "
        "training, examining the teachings, getting rid of desires, retreat, rousing "
        "energy, mindfulness and alertness, and theoretical penetration &mdash; each "
        "qualified by the same closing clause: &ldquo;and they don't lose these desires "
        "in the future.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant qualifies for graduation through seven keen enthusiasms sustained "
            "without loss into the future: for undertaking the training, examining the "
            "teachings, getting rid of desires, retreat, energy, mindfulness and "
            "alertness, and theoretical penetration."]),
        ("Graduation as a specific technical image", [
            "Niddasavatthu, literally &ldquo;grounds for being ten-less&rdquo; or having "
            "completed schooling, names the point at which a mendicant no longer needs "
            "the guidance of a teacher for a fixed number of years &mdash; not a claim "
            "about age but about training having reached its completion."]),
        ("Sustained, not merely momentary", [
            "Each of the seven items is qualified by the identical closing clause, "
            "&ldquo;and they don't lose these desires in the future&rdquo; &mdash; the "
            "discourse's concern is not whether a mendicant has ever shown enthusiasm for "
            "these seven things, but whether that enthusiasm persists without falling "
            "away."]),
        ("Closing this chapter on a forward-looking note", [
            "Where this chapter's earlier discourses classified persons by attainment "
            "already reached (AN 7.14&ndash;19) or by conduct already shown (AN "
            "7.11&ndash;13), this closing discourse frames its seven qualities "
            "prospectively &mdash; enthusiasms that must continue, not simply have "
            "occurred, ending the chapter on a note of ongoing practice rather than a "
            "fixed classification."]),
    ],
    terms=[
        ("niddasavatthu",
         "&ldquo;grounds for graduation&rdquo; &mdash; this discourse's own title, naming "
         "the point training reaches completion without requiring further oversight."),
        ("sikkhāsamādāne tibbacchando",
         "&ldquo;keen enthusiasm to undertake the training&rdquo; &mdash; the first of "
         "seven qualifications, each with an identical grammatical structure."),
        ("dhammanisantiyā, nekkhamme, pavivekāya",
         "&ldquo;examining the teachings, getting rid of desires, for retreat&rdquo; "
         "&mdash; the second, third, and fourth qualifications."),
        ("vīriyārambhe, satisampajaññe, diṭṭhipaṭivedhāya",
         "&ldquo;rousing energy, mindfulness and alertness, theoretical penetration&rdquo; "
         "&mdash; the fifth, sixth, and seventh qualifications, closing the list."),
        ("na cāyatiṁ taṁ chandaṁ vinodenti",
         "&ldquo;and they don't lose these desires in the future&rdquo; &mdash; the "
         "identical closing clause qualifying all seven items, emphasizing persistence "
         "over mere occurrence."),
    ],
    text_intro=(
        "The discourse in full: seven sustained enthusiasms that qualify a mendicant for "
        "graduation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven qualifications for graduation"),
        ("p", "&sect;1", "an7.20:1.1-1.12"),
    ],
    quiz=[
        {"q": "What does <em>niddasavatthu</em>, this discourse's own title, name?",
         "opts": [
             "A specific meditation posture",
             "The point at which a mendicant's training has reached completion, no longer "
             "requiring a teacher's fixed-term guidance",
             "A synonym for the five hindrances",
             "The fourth fruit of the path specifically"],
         "correct": 1,
         "expl": "Not a claim about age, but about training reaching completion."},
        {"q": "What clause qualifies all seven items on this discourse's list?",
         "opts": [
             "No qualifying clause is given",
             "'And they don't lose these desires in the future' — emphasizing sustained "
             "persistence, not merely having once shown enthusiasm",
             "'And they teach this to others'",
             "'And they abandon this eventually'"],
         "correct": 1,
         "expl": "A concern with ongoing persistence, not a one-time occurrence."},
        {"q": "What are the first three of the seven qualifications named?",
         "opts": [
             "Faith, wisdom, and generosity",
             "Keen enthusiasm to undertake the training, to examine the teachings, and to "
             "get rid of desires",
             "The three poisons",
             "The three fetters of AN 7.8"],
         "correct": 1,
         "expl": "The opening three of seven sustained enthusiasms."},
        {"q": "How does this discourse's framing compare to this chapter's earlier "
              "discourses, according to the guide?",
         "opts": [
             "Identical framing throughout the chapter",
             "This discourse frames its qualities prospectively — enthusiasms that must "
             "continue — where earlier discourses classified persons by attainment already "
             "reached or conduct already shown",
             "This discourse has no relationship to the rest of the chapter",
             "This discourse only concerns past conduct"],
         "correct": 1,
         "expl": "A forward-looking close to a chapter otherwise concerned with existing "
                 "classifications."},
        {"q": "Is a setting stated for AN 7.20?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, closing this chapter."},
        {"q": "What are the final two qualifications named in this discourse?",
         "opts": [
             "Faith and wisdom",
             "Mindfulness and alertness, and theoretical penetration",
             "Generosity and ethics",
             "The two poisons"],
         "correct": 1,
         "expl": "The sixth and seventh items closing this discourse's list."},
    ],
    marginalia=[
        ("Seven sustained enthusiasms", [
            "training &middot; examining",
            "teachings &middot; renunciation",
            "&middot; retreat &middot; energy &middot; mindfulness &middot; penetration",
        ]),
        ("Sustained, not momentary", [
            "'don't lose these desires",
            "in the future' —",
            "every one of the seven items",
        ]),
        ("Graduation, a specific image", [
            "niddasavatthu —",
            "training complete,",
            "no further fixed-term guidance needed",
        ]),
        ("Cross-references", [
            "AN 7.14–19 &middot; earlier, classifications by attainment or conduct already "
            "shown",
        ]),
    ],
    further=[
        '<a href="%s/an7.20/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.19.html">AN 7.19 &middot; Extinguishment</a> &mdash; previous, '
        "closing this chapter's tetrad.",
        '<a href="an-7.16.html">AN 7.16 &middot; Observing Impermanence</a> &mdash; back to '
        "this chapter&rsquo;s tetrad, for contrast with this closing discourse&rsquo;s "
        "forward-looking framing.",
    ],
)

