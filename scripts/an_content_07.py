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

