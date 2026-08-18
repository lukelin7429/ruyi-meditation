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


# --------------------------------------------------------------------------- #
# Chapter 3 — Vajjisattakavagga (AN 7.21–31)
# --------------------------------------------------------------------------- #
VAGGA_3 = "<em>Vajjisattakavagga</em> &mdash; the third chapter of the Sevens"
SETTING_VESALI = "Vesālī, at the Sārandada Shrine; stated at the head of AN 7.21"


# --------------------------------------------------------------------------- #
# AN 7.21 — Sārandadasutta
# --------------------------------------------------------------------------- #
page(
    21, "Sārandada", "At the Sārandada Shrine",
    vagga=VAGGA_3,
    meta_title="AN 7.21 — At the Sārandada Shrine | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sārandadasutta, in which the Buddha teaches the Licchavis of Vesālī the seven "
        "principles that prevent the Vajjian confederacy's decline — one of this "
        "collection's most historically significant discourses. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_VESALI),
        ("Speakers", "The Buddha, addressing several Licchavis of the Vajjian confederacy"),
        ("Form", "A full narrative frame opening a chapter, followed by seven political "
                 "and communal principles stated in sequence"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "This teaching's companion narrative recurs at the opening of "
                              "the Mahāparinibbāna-sutta tradition across both Pāli and "
                              "Chinese Āgama versions of the Buddha's final journey; this "
                              "reading guide does not assert a specific matching sutra "
                              "number for this particular discourse"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; historically and "
                       "politically significant content, addressed to a specific "
                       "confederacy rather than to mendicants"),
    ],
    why=(
        "AN 7.21 opens this chapter with one of this collection's most historically "
        "resonant teachings: seven principles that, as long as the Vajjis follow them, "
        "guarantee the confederacy's growth rather than decline &mdash; frequent "
        "assembly, harmony in meeting and acting, respect for established tradition and "
        "elders, protection of women from abduction, proper maintenance of shrines, and "
        "hospitality toward holy people. This same teaching, and its narrative "
        "consequences, opens the traditional account of the Buddha's final journey."),
    guide=[
        ("The teaching in one sentence", [
            "As long as the Vajjis meet frequently, act in harmony, uphold their ancient "
            "traditions, honor their elders, protect their women from abduction, maintain "
            "their shrines properly, and shelter holy people, they can expect growth, not "
            "decline."]),
        ("A political teaching, not a monastic one", [
            "Unlike almost every other discourse in this collection, this teaching is "
            "addressed not to mendicants but to the Licchavis, a ruling clan within the "
            "Vajjian confederacy &mdash; a rare instance of the Buddha offering direct "
            "counsel on the durability of a political community rather than a spiritual "
            "one."]),
        ("Seven principles spanning governance, tradition, and protection", [
            "The list moves through distinct registers: procedural (frequent, harmonious "
            "assembly), legal (not altering established decrees), social (honoring "
            "elders), specifically protective (not abducting women), religious (maintaining "
            "shrines and their offerings), and hospitable (sheltering perfected ones) "
            "&mdash; a comprehensive account of what holds a community together across "
            "several distinct dimensions at once."]),
        ("The narrative this teaching opens", [
            "This discourse's teaching becomes the pivot of a story continued at AN 7.22: "
            "King Ajātasattu of Magadha, planning to invade the Vajjis, sends his minister "
            "to learn whether they still follow these seven principles &mdash; the "
            "Buddha's answer determining, in the traditional account, whether that "
            "invasion could succeed by force alone."]),
    ],
    terms=[
        ("Licchavi",
         "one of the ruling clans of the Vajjian confederacy, centered at Vesālī, the "
         "discourse's addressees."),
        ("aparihāniyā dhammā",
         "&ldquo;principles that prevent decline&rdquo; &mdash; this teaching's own name "
         "for its seven items, recurring as this chapter's central organizing theme "
         "across several further discourses."),
        ("porāṇaṁ vajjidhammaṁ",
         "&ldquo;the ancient Vajjian tradition&rdquo; &mdash; what the third principle "
         "instructs the Vajjis to uphold without addition or removal."),
        ("vajjicetiyāni",
         "&ldquo;Vajjian shrines&rdquo; &mdash; both inner and outer, whose proper "
         "maintenance and traditional offerings the sixth principle addresses."),
        ("arahant",
         "&ldquo;perfected one&rdquo; &mdash; the holy people the seventh principle "
         "instructs the Vajjis to shelter and protect, so that more might come and those "
         "already present might live in comfort."),
    ],
    text_intro=(
        "The discourse in full: the seven principles that prevent the Vajjian "
        "confederacy's decline. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the Buddha's introduction"),
        ("p", "&sect;1", "an7.21:1.1-1.7"),
        ("h3", "The seven principles, in sequence"),
        ("p", "&sect;2", "an7.21:2.1-8.3"),
        ("h3", "The closing summary"),
        ("p", "&sect;3", "an7.21:9.1-9.2"),
    ],
    quiz=[
        {"q": "Who does the Buddha address this teaching to, unlike almost every other "
              "discourse in this collection?",
         "opts": [
             "A group of mendicants at Jeta's Grove",
             "The Licchavis, a ruling clan of the Vajjian confederacy",
             "A group of deities",
             "A single wealthy householder"],
         "correct": 1,
         "expl": "A rare instance of political rather than monastic counsel."},
        {"q": "What is the first of the seven principles named?",
         "opts": [
             "Not abducting women or girls",
             "Meeting frequently and having many meetings",
             "Maintaining shrines properly",
             "Sheltering perfected ones"],
         "correct": 1,
         "expl": "A procedural principle opening the list."},
        {"q": "What does the guide say the seven principles span, taken together?",
         "opts": [
             "Only religious ritual",
             "Several distinct registers — procedural, legal, social, protective, "
             "religious, and hospitable — a comprehensive account of communal durability",
             "Only military strategy",
             "Only economic policy"],
         "correct": 1,
         "expl": "A multi-dimensional account of what holds a community together."},
        {"q": "What narrative does this discourse's teaching open, according to the guide?",
         "opts": [
             "No further narrative connects to this discourse",
             "AN 7.22, where King Ajātasattu of Magadha, planning to invade the Vajjis, "
             "sends a minister to learn whether they still follow these principles",
             "A story about a different confederacy entirely",
             "A dispute among the mendicants"],
         "correct": 1,
         "expl": "The teaching's political stakes made explicit in the discourse "
                 "immediately following."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Sārandada Shrine",
             "Sāvatthī, in Jeta's Grove",
             "Kapilavatthu"],
         "correct": 1,
         "expl": "The setting stated at the head of this discourse and this chapter."},
        {"q": "What does the fifth principle specifically protect?",
         "opts": [
             "Property boundaries",
             "Women and girls of the clans, from forcible abduction",
             "Trade agreements",
             "Royal succession"],
         "correct": 1,
         "expl": "A specifically protective principle among the seven."},
    ],
    marginalia=[
        ("Seven principles of the Vajjis", [
            "frequent assembly &middot;",
            "harmony &middot; tradition &middot;",
            "elders &middot; protection &middot; shrines &middot; hospitality",
        ]),
        ("Political, not monastic", [
            "addressed to the",
            "Licchavis directly —",
            "rare in this collection",
        ]),
        ("Opening a famous narrative", [
            "the same teaching opens",
            "the traditional account",
            "of the Buddha's final journey",
        ]),
        ("Cross-references", [
            "AN 7.22 &middot; next, the political stakes made explicit",
        ]),
    ],
    further=[
        '<a href="%s/an7.21/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.20.html">AN 7.20 &middot; Qualifications for Graduation</a> &mdash; '
        "previous, closing the last chapter.",
        '<a href="an-7.22.html">AN 7.22 &middot; With Vassakāra</a> &mdash; next, this '
        "teaching's political stakes made explicit.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.22 — Vassakārasutta
# --------------------------------------------------------------------------- #
page(
    22, "Vassakāra", "With Vassakāra",
    vagga=VAGGA_3,
    meta_title="AN 7.22 — With Vassakāra | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Vassakārasutta, in which King Ajātasattu's minister questions the Buddha before "
        "an invasion of the Vajjis, and the Buddha confirms the seven principles of "
        "non-decline are still followed. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain; stated at the head of this "
                    "discourse, distinct from AN 7.21's setting at Vesālī"),
        ("Speakers", "King Ajātasattu of Magadha (reported), his minister Vassakāra, the "
                     "Buddha, and Venerable Ānanda, confirming each principle in turn"),
        ("Form", "A framed narrative: a king's declared intention to invade, a minister "
                 "sent to question the Buddha, and a question-and-answer confirmation of "
                 "AN 7.21's seven principles, restated in full"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "King Ajātasattu's planned invasion of the Vajjis and this "
                              "exchange with the Buddha recur at the opening of the "
                              "Mahāparinibbāna-sutta tradition across both Pāli and Chinese "
                              "Āgama versions; this reading guide does not assert a specific "
                              "matching sutra number for this particular discourse"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; this chapter's longest "
                       "and most narratively developed discourse, embedding real political "
                       "stakes in its restatement of AN 7.21's teaching"),
    ],
    why=(
        "AN 7.22 gives AN 7.21's teaching genuine dramatic stakes: King Ajātasattu of "
        "Magadha, declaring he will &ldquo;wipe out&rdquo; the Vajjis, sends his minister "
        "Vassakāra to the Buddha under cover of a courteous greeting. Rather than "
        "answering Vassakāra directly, the Buddha turns to Ānanda and asks, one by one, "
        "whether each of the seven principles is still being followed &mdash; and "
        "Vassakāra, overhearing, draws his own conclusion: the Vajjis cannot be defeated "
        "in open war."),
    guide=[
        ("The teaching in one sentence", [
            "As long as the Vajjis continue following the same seven principles already "
            "taught at AN 7.21, they can expect growth, not decline &mdash; and, as "
            "Vassakāra himself concludes, cannot be defeated by King Ajātasattu in open "
            "war."]),
        ("A king's intentions, reported rather than declared to the Buddha", [
            "Ajātasattu never appears before the Buddha directly. His threat &mdash; "
            "&ldquo;I shall wipe out these Vajjis... lay ruin and devastation upon "
            "them&rdquo; &mdash; reaches the Buddha only through Vassakāra's careful "
            "relay, opened by an elaborate show of courtesy that sits uneasily beside the "
            "violence of the message it precedes."]),
        ("An indirect answer, addressed to Ānanda rather than to Vassakāra", [
            "Rather than responding to Vassakāra's question directly, the Buddha turns to "
            "Ānanda, standing behind him fanning him, and asks seven times in sequence: "
            "&ldquo;Have you heard that the Vajjis...?&rdquo; Ānanda's simple confirmation "
            "&mdash; &ldquo;I have heard that, sir&rdquo; &mdash; becomes the actual "
            "vehicle for restating each principle, with Vassakāra left to draw his own "
            "conclusion from an exchange not addressed to him at all."]),
        ("Vassakāra's own political verdict", [
            "The discourse's final judgment comes not from the Buddha but from "
            "Vassakāra himself: &ldquo;If the Vajjis follow even a single one of these "
            "principles they can expect growth, not decline. How much more so all seven! "
            "King Ajātasattu cannot defeat the Vajjis in war, unless by bribery or by "
            "sowing dissension.&rdquo; The discourse ends without confirming whether that "
            "verdict held &mdash; a warning about the specific vulnerability (division "
            "from within) that the historical record suggests Magadha eventually "
            "exploited."]),
    ],
    terms=[
        ("Ajātasattu",
         "the king of Magadha whose declared intention to invade the Vajjis opens this "
         "discourse, never appearing before the Buddha himself."),
        ("Vassakāra",
         "the brahmin chief minister of Magadha, sent to question the Buddha under cover "
         "of a courteous royal greeting."),
        ("aparihāniyā dhammā",
         "&ldquo;principles that prevent decline&rdquo; &mdash; the same seven principles "
         "given in full at AN 7.21, restated here through Ānanda's confirmations."),
        ("mittabhedā vā upalāpanāya vā",
         "&ldquo;by bribery or by sowing dissension&rdquo; &mdash; Vassakāra's own named "
         "exception, the one path to victory he grants the king still remains open."),
        ("Sārandada",
         "the shrine near Vesālī where the Buddha names as having first taught this "
         "teaching, referring back explicitly to AN 7.21."),
    ],
    text_intro=(
        "The discourse in full: King Ajātasattu's declared intention, Vassakāra's "
        "mission, and the Buddha's sevenfold confirmation through Ānanda. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ajātasattu's declared intention"),
        ("p", "&sect;1", "an7.22:1.1-2.9"),
        ("h3", "Vassakāra delivers the message"),
        ("p", "&sect;2", "an7.22:3.1-4.5"),
        ("h3", "The Buddha's sevenfold confirmation through Ānanda"),
        ("p", "&sect;3", "an7.22:5.1-11.4"),
        ("h3", "Vassakāra's own conclusion"),
        ("p", "&sect;4", "an7.22:12.1-12.6"),
    ],
    quiz=[
        {"q": "Who does the Buddha address his sevenfold confirmation to, rather than "
              "answering Vassakāra directly?",
         "opts": [
             "King Ajātasattu himself, summoned to appear",
             "Venerable Ānanda, standing behind him fanning him",
             "The assembled Licchavis",
             "Vassakāra directly, in a formal address"],
         "correct": 1,
         "expl": "An indirect answer, leaving Vassakāra to draw his own conclusion."},
        {"q": "What does Ajātasattu declare his intention to do?",
         "opts": [
             "Form an alliance with the Vajjis",
             "'Wipe out' the Vajjis, laying 'ruin and devastation' upon them",
             "Send a gift to the Vajjian confederacy",
             "Study under the Buddha himself"],
         "correct": 1,
         "expl": "A stated threat of conquest, opening this discourse's political stakes."},
        {"q": "What conclusion does Vassakāra draw at the discourse's close?",
         "opts": [
             "That the Vajjis are already defeated",
             "That the Vajjis cannot be defeated in open war, only by bribery or sowing "
             "dissension",
             "That King Ajātasattu should abandon Magadha entirely",
             "That the Buddha has refused to answer at all"],
         "correct": 1,
         "expl": "A political verdict, with one specific vulnerability named as the "
                 "exception."},
        {"q": "How does this discourse's setting differ from AN 7.21's?",
         "opts": [
             "Identical setting, at Vesālī",
             "Rājagaha, on Vulture's Peak Mountain, distinct from AN 7.21's Vesālī setting",
             "No setting is given for either discourse",
             "Sāvatthī, in Jeta's Grove"],
         "correct": 1,
         "expl": "A different location, though the same teaching is recalled within it."},
        {"q": "What does the guide note about the tone of Vassakāra's approach to the "
              "Buddha?",
         "opts": [
             "Openly hostile from the start",
             "An elaborate show of courtesy sitting uneasily beside the violence of the "
             "message it precedes",
             "Complete indifference to protocol",
             "A direct challenge to a debate"],
         "correct": 1,
         "expl": "Courteous form carrying a genuinely threatening content."},
        {"q": "How many times does the Buddha ask Ānanda a version of 'have you heard "
              "that...'?",
         "opts": ["Once", "Three times", "Seven times, once for each principle", "Ten times"],
         "correct": 2,
         "expl": "One question for each of the seven principles from AN 7.21."},
    ],
    marginalia=[
        ("A king's threat, relayed", [
            "'I shall wipe out",
            "these Vajjis' —",
            "delivered through a minister",
        ]),
        ("An indirect confirmation", [
            "seven questions to Ānanda,",
            "not answers to",
            "Vassakāra directly",
        ]),
        ("One named vulnerability", [
            "'unless by bribery",
            "or by sowing dissension' —",
            "Vassakāra's own verdict",
        ]),
        ("Cross-references", [
            "AN 7.21 &middot; previous, the seven principles given in full",
        ]),
    ],
    further=[
        '<a href="%s/an7.22/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.21.html">AN 7.21 &middot; At the Sārandada Shrine</a> &mdash; '
        "previous, the seven principles given in full.",
        '<a href="an-7.23.html">AN 7.23 &middot; Non-Decline for Mendicants (1st)</a> '
        "&mdash; next, the same template adapted for the Saṅgha.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.23 — Paṭhamasattakasutta
# --------------------------------------------------------------------------- #
page(
    23, "Paṭhamasattaka", "Non-Decline for Mendicants (1st)",
    vagga=VAGGA_3,
    meta_title="AN 7.23 — Non-Decline for Mendicants (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamasattakasutta, adapting AN 7.21's Vajjian template of seven principles "
        "that prevent decline for the mendicant Saṅgha specifically. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain; stated at the head of this "
                    "discourse"),
        ("Speakers", "The Buddha, addressing the mendicants"),
        ("Form", "The identical seven-part template as AN 7.21, with items four through "
                 "seven substituted for the mendicant Saṅgha specifically"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The application of the Vajjian non-decline template to "
                              "monastic communal life recurs at the opening of the "
                              "Mahāparinibbāna-sutta tradition across both Pāli and Chinese "
                              "Āgama versions; this reading guide does not assert a specific "
                              "matching sutra number for this particular discourse"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the first of five "
                       "discourses in this chapter applying the non-decline template to "
                       "mendicants specifically, each with genuinely different content"),
    ],
    why=(
        "AN 7.23 takes AN 7.21's exact template &mdash; seven principles that prevent "
        "decline &mdash; and applies it for the first time to the mendicant Saṅgha "
        "specifically: the first three items (frequent harmonious assembly, not altering "
        "established rules) carry over almost unchanged, while the final four are "
        "substituted for concerns proper to monastic life: honoring senior mendicants, "
        "resisting craving for future lives, dwelling in wilderness, and individually "
        "established mindfulness."),
    guide=[
        ("The teaching in one sentence", [
            "As long as mendicants meet frequently, act in harmony, uphold the training "
            "rules, honor their seniors, resist craving for future lives, take care to "
            "dwell in wilderness, and individually establish mindfulness, they can expect "
            "growth, not decline."]),
        ("Three items carried over nearly unchanged", [
            "Frequent assembly, harmonious meeting and action, and not altering "
            "established rules &mdash; the first three items &mdash; transfer from the "
            "Vajjian confederacy to the Saṅgha with only the subject changed: "
            "&ldquo;training rules&rdquo; (sikkhāpada) replaces &ldquo;ancient Vajjian "
            "traditions,&rdquo; but the underlying structural concern for procedural "
            "continuity is identical."]),
        ("Four items substituted for monastic-specific concerns", [
            "Where AN 7.21 named honoring Vajjian elders, protecting women from abduction, "
            "maintaining shrines, and sheltering perfected ones, this discourse "
            "substitutes: honoring senior mendicants, resisting the sway of craving for "
            "future lives, taking care to dwell in wilderness lodgings, and individually "
            "establishing mindfulness so good-hearted companions may come and stay "
            "comfortably &mdash; concerns with no direct analogue in the political "
            "original."]),
        ("The first of five variations, not a single fixed list", [
            "This discourse is only the first of five discourses (AN 7.23&ndash;27) each "
            "offering a genuinely different seven-item list under the identical "
            "&ldquo;principles that prevent decline&rdquo; framing &mdash; a caution this "
            "series has now met repeatedly: the shared opening formula does not predict "
            "shared content in what follows it."]),
    ],
    terms=[
        ("sikkhāpada",
         "&ldquo;training rule&rdquo; &mdash; replacing AN 7.21's &ldquo;ancient Vajjian "
         "tradition&rdquo; in this discourse's third principle."),
        ("theravāda",
         "senior mendicants &ldquo;of long standing, long gone forth, fathers and leaders "
         "of the Saṅgha&rdquo; &mdash; replacing AN 7.21's Vajjian elders in the fourth "
         "principle."),
        ("āyatiṁ ponobbhavikāya taṇhāya",
         "&ldquo;craving for future lives&rdquo; &mdash; the fifth principle, resisting "
         "its sway, with no direct counterpart in AN 7.21's political list."),
        ("araññavanapatthāni pantāni senāsanāni",
         "&ldquo;wilderness lodgings&rdquo; &mdash; the sixth principle, a specifically "
         "monastic concern for dwelling place."),
        ("paccattaññeva satiṁ upaṭṭhāpenti",
         "&ldquo;individually establish mindfulness&rdquo; &mdash; the seventh and "
         "closing principle, echoing AN 7.21's concern for hospitality but reframed as an "
         "inward practice rather than an external provision."),
    ],
    text_intro=(
        "The discourse in full: the seven principles that prevent decline, adapted for "
        "the mendicant Saṅgha. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The introduction"),
        ("p", "&sect;1", "an7.23:1.1-1.7"),
        ("h3", "The seven principles for mendicants"),
        ("p", "&sect;2", "an7.23:2.1-9.1"),
    ],
    quiz=[
        {"q": "Which three items carry over from AN 7.21 nearly unchanged, according to "
              "the guide?",
         "opts": [
             "Protecting women, maintaining shrines, sheltering perfected ones",
             "Frequent assembly, harmonious meeting and action, and not altering "
             "established rules",
             "Honoring elders, resisting craving, dwelling in wilderness",
             "None — every item is substituted"],
         "correct": 1,
         "expl": "A procedural core transferring from confederacy to Saṅgha with only the "
                 "subject changed."},
        {"q": "What four items does this discourse substitute for AN 7.21's elder-honoring, "
              "women's protection, shrine-maintenance, and hospitality?",
         "opts": [
             "Faith, wisdom, generosity, and ethics",
             "Honoring senior mendicants, resisting craving for future lives, dwelling in "
             "wilderness, and individually establishing mindfulness",
             "The five hindrances plus two more",
             "The seven factors of awakening"],
         "correct": 1,
         "expl": "Concerns specific to monastic life, with no direct political analogue."},
        {"q": "What caution does the guide draw about this discourse's position among AN "
              "7.23–27?",
         "opts": [
             "That all five discourses share identical content",
             "That this is only the first of five discourses sharing the identical opening "
             "formula but offering genuinely different seven-item lists",
             "That only this discourse actually concerns non-decline",
             "That the other four discourses contradict this one"],
         "correct": 1,
         "expl": "A shared opening formula that does not predict shared specific content."},
        {"q": "What replaces 'ancient Vajjian tradition' in this discourse's third "
              "principle?",
         "opts": [
             "Nothing — the item is dropped entirely",
             "Sikkhāpada, training rules",
             "Shrine maintenance",
             "Royal decree"],
         "correct": 1,
         "expl": "The same structural concern for procedural continuity, differently "
                 "specified."},
        {"q": "Is a setting stated for AN 7.23?",
         "opts": ["Yes, at Rājagaha, on Vulture's Peak Mountain", "No — none is stated", "Yes, at Sāvatthī", "Yes, at Vesālī"],
         "correct": 0,
         "expl": "The same setting as AN 7.22 immediately before it."},
        {"q": "What does the seventh principle concern?",
         "opts": [
             "Maintaining shrines",
             "Individually establishing mindfulness, so good-hearted companions may come "
             "and stay comfortably",
             "Protecting women from abduction",
             "Royal succession"],
         "correct": 1,
         "expl": "An inward practice replacing AN 7.21's external hospitality provision."},
    ],
    marginalia=[
        ("Three items carried over", [
            "frequent assembly &middot;",
            "harmony &middot; unaltered",
            "training rules — near-identical to AN 7.21",
        ]),
        ("Four items substituted", [
            "honoring seniors &middot;",
            "resisting craving &middot;",
            "wilderness dwelling &middot; mindfulness",
        ]),
        ("First of five variations", [
            "AN 7.23–27 share one",
            "opening formula,",
            "each with genuinely different content",
        ]),
        ("Cross-references", [
            "AN 7.21 &middot; earlier, the template this discourse adapts",
            "AN 7.24 &middot; next, a second variant for mendicants",
        ]),
    ],
    further=[
        '<a href="%s/an7.23/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.21.html">AN 7.21 &middot; At the Sārandada Shrine</a> &mdash; '
        "earlier, the template this discourse adapts.",
        '<a href="an-7.24.html">AN 7.24 &middot; Non-Decline for Mendicants (2nd)</a> '
        "&mdash; next, a second, genuinely different variant.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.24 — Dutiyasattakasutta
# --------------------------------------------------------------------------- #
page(
    24, "Dutiyasattaka", "Non-Decline for Mendicants (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 7.24 — Non-Decline for Mendicants (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyasattakasutta, a second non-decline variant naming seven items closely "
        "matching this collection's familiar 'trainee decline' formula, plus two further "
        "items. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, sharing its opening four items with content "
                 "already met repeatedly in this collection"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of relishing work, talk, sleep, and company "
                              "with a mendicant's decline recurs throughout the Chinese "
                              "Āgamas' monastic-conduct material; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; opens with content "
                       "already familiar from earlier in this series, closing on three new "
                       "items"),
    ],
    why=(
        "AN 7.24 names seven principles opening with content already met repeatedly in "
        "this collection &mdash; not relishing work, talk, sleep, or company &mdash; the "
        "same core already spelled out at AN 6.31 and AN 6.117&ndash;118 in the previous "
        "nipāta, now joined by three further items: no corrupt wishes, no bad friends, "
        "and not stopping halfway after a trifling distinction."),
    guide=[
        ("The teaching in one sentence", [
            "As long as mendicants don't relish work, talk, sleep, or company, don't have "
            "corrupt wishes, don't keep bad friends, and don't stop halfway after some "
            "trifling attainment, they can expect growth, not decline."]),
        ("Four items already met, checked against their earlier appearances", [
            "Not relishing work, talk, sleep, and company is, checked term by term, the "
            "same core already named at AN 6.31 (there, a trainee's causes of decline) and "
            "AN 6.117&ndash;118 (there, blocking meditation on the foundations of "
            "mindfulness) &mdash; a third context in which this same four-item core "
            "appears, now under the Vajjian non-decline framing."]),
        ("Three further items, new to this recurring core", [
            "Corrupt wishes (pāpicchā), bad friendship (pāpamittatā), and stopping "
            "halfway after a trifling distinction extend the familiar four-item core into "
            "a full seven, adding concerns about aspiration, company, and premature "
            "satisfaction not present in either of the four-item core's earlier "
            "appearances."]),
        ("A warning against premature satisfaction, this discourse's own contribution", [
            "The seventh item &mdash; not stopping halfway after achieving some trifling "
            "distinction (oramattena visesādhigamena antarā vosānaṁ āpajjati) &mdash; "
            "names a danger specific to progress itself: mistaking an early or partial "
            "attainment for the completed goal, and settling there rather than continuing "
            "further."]),
    ],
    terms=[
        ("kammārāmatā, bhassārāmatā, niddārāmatā, saṅgaṇikārāmatā",
         "&ldquo;relishing work, talk, sleep, and company&rdquo; &mdash; the same core "
         "already met at AN 6.31 and AN 6.117–118, now appearing a third time under this "
         "chapter's non-decline framing."),
        ("pāpicchatā",
         "&ldquo;corrupt wishes&rdquo; &mdash; the fifth item, falling under their sway."),
        ("pāpamittatā",
         "&ldquo;bad friendship&rdquo; &mdash; the sixth item, echoing AN 7.10's own "
         "closing pair earlier in this book."),
        ("oramattena visesādhigamena antarā vosānaṁ āpajjati",
         "&ldquo;stops halfway after achieving some trifling distinction&rdquo; &mdash; "
         "the seventh and closing item, a warning against mistaking partial progress for "
         "completion."),
        ("aparihāniyā dhammā",
         "&ldquo;principles that prevent decline&rdquo; &mdash; this chapter's recurring "
         "framing, here applied to a list drawing on already-familiar content."),
    ],
    text_intro=(
        "The discourse in full: seven principles combining a familiar four-item core with "
        "three further items. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven principles"),
        ("p", "&sect;1", "an7.24:1.1-4.1"),
    ],
    quiz=[
        {"q": "What four-item core opens this discourse's list, and where has it already "
              "appeared in this collection?",
         "opts": [
             "The five hindrances, appearing nowhere else",
             "Not relishing work, talk, sleep, and company — already met at AN 6.31 and AN "
             "6.117–118 in the previous nipāta",
             "The three poisons, appearing only once before",
             "The seven fetters of AN 7.8"],
         "correct": 1,
         "expl": "A third context for this recurring four-item core, now under this "
                 "chapter's non-decline framing."},
        {"q": "What three items does this discourse add beyond the familiar four-item "
              "core?",
         "opts": [
             "Faith, wisdom, and energy",
             "No corrupt wishes, no bad friends, and not stopping halfway after a trifling "
             "distinction",
             "The three fetters",
             "The four foundations of mindfulness"],
         "correct": 1,
         "expl": "New concerns extending a familiar core into a full seven."},
        {"q": "What does the seventh item, 'stops halfway after achieving some trifling "
              "distinction,' warn against, according to the guide?",
         "opts": [
             "Working too hard toward the goal",
             "Mistaking an early or partial attainment for the completed goal, and settling "
             "there rather than continuing",
             "Talking too much about one's attainments",
             "Neglecting to eat enough"],
         "correct": 1,
         "expl": "A specific danger arising from progress itself, not from failure to "
                 "progress."},
        {"q": "Where else in this book has the sixth item, bad friendship, already "
              "appeared as a closing item?",
         "opts": [
             "Nowhere else in this book",
             "At AN 7.10, closing that discourse's own substituted pair",
             "At AN 7.5, among the seven kinds of wealth",
             "At AN 7.14, among the seven noble individuals"],
         "correct": 1,
         "expl": "A theme this book has already returned to once before."},
        {"q": "Is a setting stated for AN 7.24?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.23's fresh setting."},
        {"q": "What does <em>pāpamittatā</em> mean?",
         "opts": ["Corrupt wishes", "Bad friendship", "Wilderness dwelling", "Trifling distinction"],
         "correct": 1,
         "expl": "The sixth item on this discourse's seven-item list."},
    ],
    marginalia=[
        ("A familiar four-item core", [
            "work, talk, sleep,",
            "company — same as",
            "AN 6.31 and AN 6.117–118",
        ]),
        ("Three new items added", [
            "corrupt wishes &middot;",
            "bad friends &middot;",
            "stopping halfway too soon",
        ]),
        ("A warning against premature stop", [
            "mistaking partial progress",
            "for the completed goal —",
            "settling there instead of continuing",
        ]),
        ("Cross-references", [
            "AN 6.31/6.117–118 &middot; earlier nipāta, this same four-item core",
            "AN 7.10 &middot; earlier, bad friendship's earlier appearance in this book",
        ]),
    ],
    further=[
        '<a href="%s/an7.24/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.23.html">AN 7.23 &middot; Non-Decline for Mendicants (1st)</a> '
        "&mdash; previous, the first variant of this chapter's mendicant series.",
        '<a href="an-7.25.html">AN 7.25 &middot; Non-Decline for Mendicants (3rd)</a> '
        "&mdash; next, a third variant naming seven personal qualities.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.25 — Tatiyasattakasutta
# --------------------------------------------------------------------------- #
page(
    25, "Tatiyasattaka", "Non-Decline for Mendicants (3rd)",
    vagga=VAGGA_3,
    meta_title="AN 7.25 — Non-Decline for Mendicants (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Tatiyasattakasutta, a third non-decline variant naming seven personal qualities "
        "closely echoing AN 7.5's seven kinds of wealth. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list of personal qualities, the third variant in "
                 "this chapter's mendicant series"),
        ("Length", "under 30 seconds to read"),
        ("Northern parallel", "Faith, conscience, prudence, learning, energy, "
                              "mindfulness, and wisdom as a fixed positive set recur widely "
                              "across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, echoing but not "
                       "duplicating AN 7.5's seven kinds of wealth"),
    ],
    why=(
        "AN 7.25 names seven personal qualities &mdash; faithful, conscientious, prudent, "
        "learned, energetic, mindful, and wise &mdash; six of which match AN 7.5's seven "
        "kinds of wealth almost exactly, differing only in that this list drops "
        "generosity and ethics, replacing them with mindfulness, and reframes the "
        "remaining items as qualities of character rather than kinds of wealth."),
    guide=[
        ("The teaching in one sentence", [
            "As long as mendicants are faithful, conscientious, prudent, learned, "
            "energetic, mindful, and wise, they can expect growth, not decline."]),
        ("Close to, but not identical to, AN 7.5's seven kinds of wealth", [
            "Checked term by term against AN 7.5's list &mdash; faith, ethics, "
            "conscience, prudence, learning, generosity, wisdom &mdash; this discourse "
            "shares five items exactly (faith, conscience, prudence, learning, wisdom) but "
            "drops ethics and generosity, adding mindfulness and energy in their place: a "
            "close relative, not a restatement."]),
        ("Wealth reframed as character, and decline as its opposite", [
            "AN 7.5 framed these qualities as forms of wealth, prosperity a person "
            "possesses. This discourse instead frames the same core cluster as what "
            "prevents decline &mdash; the identical inward qualities read once as "
            "possession and once as protection, depending on which discourse's frame is "
            "applied."]),
        ("The third of five variants, continuing this chapter's pattern", [
            "Following AN 7.23's political-template adaptation and AN 7.24's familiar "
            "four-item-core expansion, this discourse offers yet a third distinct "
            "approach to the same &ldquo;principles that prevent decline&rdquo; framing "
            "&mdash; a set of personal virtues rather than communal procedures or specific "
            "conduct."]),
    ],
    terms=[
        ("saddha, hirimā, ottappī",
         "&ldquo;faithful, conscientious, prudent&rdquo; &mdash; the first three "
         "qualities, matching AN 7.5's wealth list exactly."),
        ("bahussuta",
         "&ldquo;learned&rdquo; &mdash; the fourth quality, matching AN 7.5's "
         "&ldquo;learning&rdquo; (suta)."),
        ("āraddhavīriya, satimā, paññavā",
         "&ldquo;energetic, mindful, wise&rdquo; &mdash; the fifth, sixth, and seventh "
         "qualities, with energy and mindfulness new to this list compared to AN 7.5."),
        ("sīla, cāga",
         "&ldquo;ethics, generosity&rdquo; &mdash; two of AN 7.5's seven kinds of wealth, "
         "absent from this discourse's version."),
        ("aparihāniyā dhammā",
         "&ldquo;principles that prevent decline&rdquo; &mdash; this discourse's own "
         "framing, distinct from AN 7.5's framing of the same core cluster as wealth."),
    ],
    text_intro=(
        "The discourse in full: seven personal qualities that prevent a mendicant's "
        "decline. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven qualities"),
        ("p", "&sect;1", "an7.25:1.1-3.1"),
    ],
    quiz=[
        {"q": "How many of this discourse's seven items match AN 7.5's seven kinds of "
              "wealth exactly?",
         "opts": [
             "All seven",
             "Five — faith, conscience, prudence, learning, and wisdom — with ethics and "
             "generosity dropped in favor of mindfulness and energy",
             "None",
             "Only two"],
         "correct": 1,
         "expl": "A close relative of AN 7.5's list, not a restatement."},
        {"q": "What two items does this discourse drop from AN 7.5's list, and what "
              "replaces them?",
         "opts": [
             "Faith and wisdom, replaced by nothing",
             "Ethics and generosity, replaced by mindfulness and energy",
             "Learning and prudence, replaced by faith and wisdom",
             "Nothing is dropped or replaced"],
         "correct": 1,
         "expl": "A genuine, checked difference despite the strong overlap."},
        {"q": "How does this discourse's framing differ from AN 7.5's, according to the "
              "guide?",
         "opts": [
             "No difference in framing at all",
             "AN 7.5 frames these qualities as wealth possessed; this discourse frames a "
             "closely related cluster as what prevents decline",
             "This discourse frames the qualities as physical health",
             "AN 7.5 frames the qualities negatively, this discourse positively"],
         "correct": 1,
         "expl": "Possession versus protection, two frames for closely related qualities."},
        {"q": "What position does this discourse occupy in this chapter's series of "
              "mendicant non-decline variants?",
         "opts": [
             "The first", "The third, following AN 7.23's political adaptation and AN "
             "7.24's expanded familiar core", "The fifth and final", "It does not belong "
             "to this series"],
         "correct": 1,
         "expl": "A third distinct approach to the shared 'non-decline' framing."},
        {"q": "Is a setting stated for AN 7.25?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.24 immediately before it."},
        {"q": "What does <em>bahussuta</em> mean?",
         "opts": ["Energetic", "Learned", "Mindful", "Wise"],
         "correct": 1,
         "expl": "The fourth quality, matching AN 7.5's 'learning' item exactly."},
    ],
    marginalia=[
        ("Seven personal qualities", [
            "faith &middot; conscience &middot;",
            "prudence &middot; learning &middot;",
            "energy &middot; mindfulness &middot; wisdom",
        ]),
        ("Close to AN 7.5, not identical", [
            "five items match exactly —",
            "ethics, generosity dropped;",
            "mindfulness, energy added",
        ]),
        ("Possession vs. protection", [
            "AN 7.5: wealth possessed —",
            "AN 7.25: what prevents",
            "decline — same core, two frames",
        ]),
        ("Cross-references", [
            "AN 7.5 &middot; earlier, the closely related seven kinds of wealth",
            "AN 7.24 &middot; previous, the second variant in this series",
        ]),
    ],
    further=[
        '<a href="%s/an7.25/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.5.html">AN 7.5 &middot; Wealth in Brief</a> &mdash; earlier, the '
        "closely related seven kinds of wealth.",
        '<a href="an-7.26.html">AN 7.26 &middot; Awakening Factors</a> &mdash; next, a '
        "fourth variant naming the seven factors of awakening.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.26 — Bojjhaṅgasutta
# --------------------------------------------------------------------------- #
page(
    26, "Bojjhaṅga", "Awakening Factors",
    vagga=VAGGA_3,
    meta_title="AN 7.26 — Awakening Factors | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Bojjhaṅgasutta, a fourth non-decline variant naming the seven factors of "
        "awakening — one of this literature's most fundamental fixed lists. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, the fourth variant in this chapter's "
                 "mendicant series, naming one of this literature's most standard "
                 "technical sets"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The seven factors of awakening (bojjhaṅga) as a fixed set "
                              "recur as one of the most standard technical lists across the "
                              "Chinese Āgamas and Abhidharma literature; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; names one of this "
                       "literature's most fundamental fixed lists, here folded into this "
                       "chapter's non-decline framing"),
    ],
    why=(
        "AN 7.26 names the seven factors of awakening &mdash; mindfulness, investigation "
        "of principles, energy, rapture, tranquility, immersion, and equanimity &mdash; "
        "as principles that prevent decline, folding one of this literature's most "
        "fundamental and widely recurring technical lists into this chapter's Vajjian-"
        "derived framing."),
    guide=[
        ("The teaching in one sentence", [
            "As long as mendicants develop the awakening factors of mindfulness, "
            "investigation of principles, energy, rapture, tranquility, immersion, and "
            "equanimity, they can expect growth, not decline."]),
        ("A standard set, given a new frame", [
            "The seven awakening factors (satta bojjhaṅgā) are among the most frequently "
            "recurring fixed lists in this literature, appearing across meditation "
            "instructions, analyses of the path, and accounts of realization. This "
            "discourse's contribution is not the list itself but its placement within "
            "this chapter's non-decline framing, alongside AN 7.21's political "
            "principles and AN 7.23&ndash;25's other mendicant variants."]),
        ("A developmental sequence, not seven independent items", [
            "Unlike several other seven-item lists in this chapter, the awakening "
            "factors are traditionally understood as unfolding in sequence: mindfulness "
            "grounds investigation, investigation fuels energy, energy gives rise to "
            "rapture, rapture leads to tranquility, tranquility supports immersion, and "
            "immersion matures into equanimity &mdash; each factor a precondition for the "
            "one following it."]),
        ("The fourth of five variants, still within reach of a shared root", [
            "Though the awakening factors are a fixed, independently well-known "
            "technical set, their appearance here as the fourth of five &ldquo;non-"
            "decline&rdquo; variants for mendicants keeps them within this chapter's "
            "broader argument: whatever specific content is named, following it "
            "consistently is what prevents decline, whether that content is political "
            "procedure, personal virtue, or the classic architecture of awakening "
            "itself."]),
    ],
    terms=[
        ("bojjhaṅga",
         "&ldquo;awakening factor&rdquo; &mdash; this discourse's own term for its "
         "seven-item list, one of the most standard technical sets in this literature."),
        ("sati sambojjhaṅga, dhammavicaya sambojjhaṅga",
         "&ldquo;the awakening factor of mindfulness, of investigation of "
         "principles&rdquo; &mdash; the first two factors, grounding the sequence that "
         "follows."),
        ("vīriya, pīti sambojjhaṅga",
         "&ldquo;energy, rapture&rdquo; &mdash; the third and fourth factors, arising in "
         "sequence from the first two."),
        ("passaddhi, samādhi sambojjhaṅga",
         "&ldquo;tranquility, immersion&rdquo; &mdash; the fifth and sixth factors, "
         "settling the energetic factors that precede them."),
        ("upekkhā sambojjhaṅga",
         "&ldquo;equanimity&rdquo; &mdash; the seventh and culminating factor, maturing "
         "from stable immersion."),
    ],
    text_intro=(
        "The discourse in full: the seven factors of awakening, as principles that "
        "prevent decline. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven awakening factors"),
        ("p", "&sect;1", "an7.26:1.1-3.1"),
    ],
    quiz=[
        {"q": "What seven factors does this discourse name?",
         "opts": [
             "The five hindrances plus two more",
             "Mindfulness, investigation of principles, energy, rapture, tranquility, "
             "immersion, and equanimity",
             "The seven fetters of AN 7.8",
             "The seven kinds of wealth of AN 7.5"],
         "correct": 1,
         "expl": "One of the most standard fixed lists in this entire literature."},
        {"q": "What does this discourse contribute, given that the seven awakening "
              "factors are already a well-known independent list, according to the "
              "guide?",
         "opts": [
             "An entirely new list unrelated to the standard bojjhaṅga",
             "Not the list itself, but its placement within this chapter's non-decline "
             "framing, alongside the political and personal-quality variants already met",
             "A denial that these seven factors are genuinely awakening factors",
             "Nothing — the discourse is entirely redundant"],
         "correct": 1,
         "expl": "A familiar list given a new organizing frame."},
        {"q": "How are the seven awakening factors traditionally understood to relate to "
              "each other, according to the guide?",
         "opts": [
             "As seven entirely independent, unordered items",
             "As a developmental sequence, each factor a precondition for the one "
             "following it",
             "As seven synonyms for the same single state",
             "As seven items that must all arise simultaneously"],
         "correct": 1,
         "expl": "Mindfulness grounding investigation, investigation fueling energy, and "
                 "so on through equanimity."},
        {"q": "What position does this discourse occupy in this chapter's mendicant "
              "non-decline series?",
         "opts": [
             "The first", "The fourth of five", "The last of five", "It does not belong "
             "to this series"],
         "correct": 1,
         "expl": "Following AN 7.23, 7.24, and 7.25, with one further variant still to "
                 "come."},
        {"q": "Is a setting stated for AN 7.26?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.25 immediately before it."},
        {"q": "What is the seventh and culminating awakening factor?",
         "opts": ["Rapture", "Tranquility", "Equanimity", "Investigation of principles"],
         "correct": 2,
         "expl": "Maturing from the stable immersion the sixth factor establishes."},
    ],
    marginalia=[
        ("The seven awakening factors", [
            "mindfulness &middot; investigation",
            "&middot; energy &middot; rapture &middot;",
            "tranquility &middot; immersion &middot; equanimity",
        ]),
        ("A standard list, new frame", [
            "already well-known —",
            "here folded into this",
            "chapter's non-decline argument",
        ]),
        ("A developmental sequence", [
            "each factor grounds",
            "the one that follows,",
            "not seven independent items",
        ]),
        ("Cross-references", [
            "AN 7.25 &middot; previous, the third variant naming personal qualities",
            "AN 7.27 &middot; next, the fifth and final variant naming perceptions",
        ]),
    ],
    further=[
        '<a href="%s/an7.26/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.25.html">AN 7.25 &middot; Non-Decline for Mendicants (3rd)</a> '
        "&mdash; previous, the third variant naming personal qualities.",
        '<a href="an-7.27.html">AN 7.27 &middot; Perceptions</a> &mdash; next, the fifth '
        "and final variant naming seven perceptions.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.27 — Saññāsutta
# --------------------------------------------------------------------------- #
page(
    27, "Saññā", "Perceptions",
    vagga=VAGGA_3,
    meta_title="AN 7.27 — Perceptions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saññāsutta, "
        "closing this chapter's mendicant non-decline series with seven perceptions "
        "related to, but distinct from, AN 6.142's six perceptions in the previous "
        "nipāta. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list of perceptions, closing this chapter's series "
                 "of five mendicant non-decline variants"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The graduated sequence of perceptions from impermanence "
                              "through cessation recurs widely across the Chinese Āgamas' "
                              "insight-meditation material; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; closes this chapter's "
                       "series, related to but distinct from AN 6.142's six perceptions in "
                       "the previous nipāta"),
    ],
    why=(
        "AN 7.27 closes this chapter's five-discourse mendicant series with seven "
        "perceptions &mdash; impermanence, not-self, ugliness, drawbacks, giving up, "
        "fading away, and cessation &mdash; a list checked against AN 6.142's six "
        "perceptions in the previous nipāta and found related but genuinely distinct, "
        "not a simple restatement with one item added."),
    guide=[
        ("The teaching in one sentence", [
            "As long as mendicants develop the perception of impermanence, not-self, "
            "ugliness, drawbacks, giving up, fading away, and cessation, they can expect "
            "growth, not decline."]),
        ("Checked against AN 6.142: related, not identical", [
            "AN 6.142's six perceptions were impermanence, suffering-in-impermanence, "
            "not-self-in-suffering, giving up, fading away, and cessation &mdash; an "
            "explicitly nested chain where each perception built on the one before it. "
            "This discourse's seven drop the nested suffering-in-impermanence and "
            "not-self-in-suffering structure, naming impermanence and not-self as flat, "
            "independent items instead, and add two new items, ugliness and drawbacks, "
            "not present in AN 6.142's version at all."]),
        ("Ugliness and drawbacks, new to this specific formula", [
            "Asubha (ugliness, the standard antidote to attraction already met at AN "
            "6.107) and ādīnava (drawbacks, seeing the danger or fault in something) "
            "extend the list into more concretely corrective territory, beyond the "
            "purely descriptive impermanence and not-self."]),
        ("Closing the chapter's series on insight rather than procedure", [
            "Where AN 7.21's original template concerned communal procedure and AN "
            "7.23&ndash;25 concerned conduct and character, this closing variant, like AN "
            "7.26 before it, concerns internal cultivation &mdash; ending this chapter's "
            "run of non-decline discourses on the register of meditative insight rather "
            "than external behavior."]),
    ],
    terms=[
        ("aniccasaññā, anattasaññā",
         "&ldquo;the perception of impermanence, of not-self&rdquo; &mdash; the first two "
         "items, named as flat independent perceptions here rather than AN 6.142's nested "
         "chain."),
        ("asubhasaññā",
         "&ldquo;the perception of ugliness&rdquo; &mdash; the third item, the same "
         "antidote to greed already met at AN 6.107, new to this specific formula."),
        ("ādīnavasaññā",
         "&ldquo;the perception of drawbacks&rdquo; &mdash; the fourth item, seeing the "
         "danger or fault in conditioned existence, likewise new to this formula."),
        ("pahānasaññā, virāgasaññā, nirodhasaññā",
         "&ldquo;the perception of giving up, of fading away, of cessation&rdquo; "
         "&mdash; the closing three items, matching AN 6.142's own closing three exactly."),
        ("aparihāniyā dhammā",
         "&ldquo;principles that prevent decline&rdquo; &mdash; this chapter's recurring "
         "framing, closing its mendicant series on this seventh and final variant."),
    ],
    text_intro=(
        "The discourse in full: seven perceptions that prevent a mendicant's decline. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven perceptions"),
        ("p", "&sect;1", "an7.27:1.1-3.1"),
    ],
    quiz=[
        {"q": "How does this discourse's seven perceptions compare to AN 6.142's six, "
              "checked term by term?",
         "opts": [
             "Identical, with one item simply added",
             "Related but distinct — this list drops AN 6.142's nested "
             "suffering-in-impermanence structure, names impermanence and not-self as flat "
             "items, and adds ugliness and drawbacks",
             "Entirely unrelated content",
             "This discourse has no perceptions in common with AN 6.142 at all"],
         "correct": 1,
         "expl": "A genuine variant, not a simple restatement with an item appended."},
        {"q": "What two items does this discourse add that were absent from AN 6.142's "
              "version?",
         "opts": [
             "Faith and wisdom",
             "Ugliness (asubha) and drawbacks (ādīnava)",
             "Suffering and self",
             "The three fetters"],
         "correct": 1,
         "expl": "New, more concretely corrective items extending beyond pure description."},
        {"q": "Which three closing items does this discourse share exactly with AN "
              "6.142?",
         "opts": [
             "Impermanence, not-self, ugliness",
             "Giving up, fading away, cessation",
             "Drawbacks, giving up, fading away",
             "None of the items are shared"],
         "correct": 1,
         "expl": "The final three items, matching AN 6.142's closing sequence exactly."},
        {"q": "How does the guide characterize this discourse's register compared to AN "
              "7.21 and AN 7.23–25?",
         "opts": [
             "Identical register throughout",
             "Internal cultivation and meditative insight, closing this chapter's series "
             "on a different note than the communal procedure or conduct of the earlier "
             "variants",
             "Purely political, like AN 7.21",
             "This discourse has no discernible register"],
         "correct": 1,
         "expl": "A close on meditative insight, following AN 7.26's similar register."},
        {"q": "Is a setting stated for AN 7.27?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, closing this chapter's five-discourse mendicant series."},
        {"q": "Where else has <em>asubhasaññā</em>, the perception of ugliness, already "
              "appeared in this collection?",
         "opts": [
             "Nowhere else",
             "At AN 6.107, as the antidote matched specifically to greed",
             "At AN 7.14, among the seven noble individuals",
             "At AN 7.5, among the seven kinds of wealth"],
         "correct": 1,
         "expl": "A term already established earlier in this series, applied here within a "
                 "new formula."},
    ],
    marginalia=[
        ("Seven perceptions", [
            "impermanence &middot; not-self",
            "&middot; ugliness &middot; drawbacks",
            "&middot; giving up &middot; fading away &middot; cessation",
        ]),
        ("Related, not identical, to AN 6.142", [
            "nested chain flattened,",
            "ugliness and drawbacks",
            "added — a genuine variant",
        ]),
        ("Closing on insight", [
            "AN 7.26/27 both",
            "concern cultivation,",
            "closing this series inward",
        ]),
        ("Cross-references", [
            "AN 6.142 &middot; earlier nipāta, the related six-item chain",
            "AN 7.26 &middot; previous, the fourth variant naming awakening factors",
        ]),
    ],
    further=[
        '<a href="%s/an7.27/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.26.html">AN 7.26 &middot; Awakening Factors</a> &mdash; previous, '
        "the fourth variant in this chapter's mendicant series.",
        '<a href="an-6.142.html">AN 6.142 &middot; Untitled Discourse on Greed (3rd)</a> '
        "&mdash; earlier nipāta, the related but distinct six-item perception chain.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.28 — Paṭhamaparihānisutta
# --------------------------------------------------------------------------- #
page(
    28, "Paṭhamaparihāni", "Non-decline for a Mendicant Trainee",
    vagga=VAGGA_3,
    meta_title="AN 7.28 — Non-decline for a Mendicant Trainee | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaparihānisutta, restating AN 6.31's familiar decline list with a new "
        "seventh item about deferring to senior mendicants on Saṅgha business. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "Two matched seven-item lists, cause and its direct reversal, opening "
                 "with content already met at AN 6.31 and this chapter's own AN 7.24"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of humility before senior monastics with a "
                              "trainee's stability recurs widely across the Chinese "
                              "Āgamas' monastic-conduct material; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a familiar six-item "
                       "core plus one new item, shifting this chapter's language from "
                       "'principles that prevent decline' back to a more familiar "
                       "blockage-and-reversal form"),
    ],
    why=(
        "AN 7.28 returns to Jeta's Grove and to this collection's familiar four-item core "
        "&mdash; relishing work, talk, sleep, and company &mdash; joined by not guarding "
        "the sense doors and eating too much, already met at AN 6.31 and this chapter's "
        "own AN 7.24, now closing on a new seventh item: getting involved in Saṅgha "
        "business a trainee should have deferred to their seniors."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant trainee who relishes work, talk, sleep, and company, doesn't "
            "guard the sense doors, eats too much, and involves themselves in Saṅgha "
            "business better left to senior mendicants declines; the seven reversals "
            "prevent that decline."]),
        ("Six items already familiar, checked against their earlier appearances", [
            "The first six items are, checked term by term, identical to AN 6.31's list "
            "of a trainee's causes of decline in the previous nipāta, and closely "
            "overlapping with AN 7.24's own four-item core earlier in this chapter &mdash; "
            "content this series has now met at least three times across two nipātas."]),
        ("A new seventh item: knowing when not to step in", [
            "The seventh and only new item concerns a specific failure of deference: "
            "when Saṅgha business arises, a trainee who fails to reflect that senior "
            "mendicants &ldquo;of long standing, long gone forth, responsible... will be "
            "known for taking care of this&rdquo; gets needlessly involved, rather than "
            "trusting the community's existing structure of responsibility."]),
        ("A return to blockage-and-reversal, after five 'non-decline' variants", [
            "Unlike AN 7.21 and 7.23&ndash;27's single positive list of principles that "
            "prevent decline, this discourse returns to the paired blockage/reversal "
            "structure familiar from the Sixes, stating both what leads to a trainee's "
            "decline and its direct opposite in full."]),
    ],
    terms=[
        ("sekha",
         "&ldquo;trainee&rdquo; &mdash; this discourse's specific subject, echoing AN "
         "6.31's identical population, already defined earlier in this series."),
        ("kammārāmatā, bhassārāmatā, niddārāmatā, saṅgaṇikārāmatā, indriyesu "
         "aguttadvāratā, bhojane amattaññutā",
         "the same six items already met at AN 6.31: relishing work, talk, sleep, and "
         "company, not guarding the sense doors, and eating too much."),
        ("saṅghakaraṇīya",
         "&ldquo;Saṅgha business&rdquo; &mdash; the occasion for this discourse's new "
         "seventh item, a trainee's failure to defer to responsible seniors."),
        ("cirapabbajita, saṅghapitaro, saṅghapariṇāyaka",
         "&ldquo;long gone forth, fathers and leaders of the Saṅgha&rdquo; &mdash; the "
         "senior mendicants a trainee should trust to handle communal responsibilities."),
        ("parihāni, aparihāni",
         "&ldquo;decline, non-decline&rdquo; &mdash; this discourse's own framing, a "
         "return to the paired form after this chapter's run of single positive lists."),
    ],
    text_intro=(
        "The discourse in full: seven things leading to a trainee's decline, and their "
        "reversal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven things that lead to a trainee's decline"),
        ("p", "&sect;1", "an7.28:1.1-1.8"),
        ("h3", "Seven things that don't"),
        ("p", "&sect;2", "an7.28:2.1-2.5"),
    ],
    quiz=[
        {"q": "How do this discourse's first six items compare to AN 6.31's list, checked "
              "term by term?",
         "opts": [
             "Entirely different content",
             "Identical — relishing work, talk, sleep, and company, not guarding the sense "
             "doors, and eating too much",
             "Only two items overlap",
             "No relationship between the two discourses"],
         "correct": 1,
         "expl": "Content this series has now met at least three times across two "
                 "nipātas."},
        {"q": "What does this discourse's new seventh item concern?",
         "opts": [
             "A specific meditation technique",
             "A trainee needlessly getting involved in Saṅgha business better left to "
             "responsible senior mendicants",
             "Eating too little food",
             "Refusing to speak with laypeople"],
         "correct": 1,
         "expl": "A failure of deference and trust in the community's existing "
                 "structure."},
        {"q": "How does this discourse's structure differ from AN 7.21 and 7.23–27's, "
              "according to the guide?",
         "opts": [
             "Identical structure throughout",
             "A return to the paired blockage/reversal form, after this chapter's run of "
             "single positive 'non-decline' lists",
             "This discourse has no reversal at all",
             "This discourse is a bare list with no elaboration"],
         "correct": 1,
         "expl": "The familiar Sixes-style structure returning after five single-list "
                 "variants."},
        {"q": "What senior mendicants is a trainee instructed to trust with Saṅgha "
              "business?",
         "opts": [
             "Only the most recently ordained",
             "Those of long standing, long gone forth, fathers and leaders of the Saṅgha",
             "Lay donors specifically",
             "No particular group is named"],
         "correct": 1,
         "expl": "An existing structure of communal responsibility the trainee should "
                 "trust rather than override."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Sārandada Shrine",
             "No setting is given"],
         "correct": 1,
         "expl": "A return to this book's opening setting, after this chapter's Rājagaha "
                 "and Vesālī discourses."},
        {"q": "Who is the specific subject of this discourse?",
         "opts": [
             "Lay followers generally",
             "A mendicant trainee (sekha) specifically",
             "Fully awakened arahants",
             "King Ajātasattu's ministers"],
         "correct": 1,
         "expl": "The same population already defined and addressed at AN 6.31."},
    ],
    marginalia=[
        ("Six familiar items", [
            "work, talk, sleep,",
            "company &middot; unguarded senses",
            "&middot; overeating — as AN 6.31",
        ]),
        ("A new seventh item", [
            "getting involved in",
            "Saṅgha business better",
            "left to responsible seniors",
        ]),
        ("Back to blockage/reversal", [
            "after five single-list",
            "'non-decline' variants —",
            "the familiar paired form returns",
        ]),
        ("Cross-references", [
            "AN 6.31 &middot; earlier nipāta, this discourse's six-item source",
            "AN 7.24 &middot; earlier, the same core within this chapter's own series",
        ]),
    ],
    further=[
        '<a href="%s/an7.28/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.27.html">AN 7.27 &middot; Perceptions</a> &mdash; previous, closing '
        "this chapter's mendicant non-decline series.",
        '<a href="an-6.31.html">AN 6.31 &middot; A Trainee</a> &mdash; earlier nipāta, this '
        "discourse's six-item source.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.29 — Dutiyaparihānisutta
# --------------------------------------------------------------------------- #
page(
    29, "Dutiyaparihāni", "Non-decline for a Lay Follower",
    vagga=VAGGA_3,
    meta_title="AN 7.29 — Non-decline for a Lay Follower | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaparihānisutta, opening a three-discourse family on a lay follower's "
        "decline, given in full prose and verse — the fullest of three near-identical "
        "treatments. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched seven-item lists plus a closing verse restatement, the "
                 "fullest of three discourses sharing this identical content"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The pairing of suspicion toward mendicants with a lay "
                              "follower's spiritual decline recurs widely across the "
                              "Chinese Āgamas' lay-conduct material; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; opens a three-"
                       "discourse family restating identical content under three "
                       "different titles"),
    ],
    why=(
        "AN 7.29 shifts this chapter's final attention from mendicants to lay followers: "
        "seven things that lead to a lay follower's decline &mdash; missing chances to "
        "see mendicants, neglecting the teaching, not training in higher ethics, "
        "suspicion toward mendicants, hostile listening, seeking donees outside the "
        "Buddhist community, and serving them first &mdash; given here in full prose and "
        "closing verse, the fullest of three discourses (AN 7.29&ndash;31) that will "
        "restate this identical content under three different titles."),
    guide=[
        ("The teaching in one sentence", [
            "A lay follower who misses seeing mendicants, neglects the teaching, doesn't "
            "train in higher ethics, is suspicious of mendicants, listens with a "
            "fault-finding mind, and serves those outside the Buddhist community first "
            "declines; the seven reversals prevent that decline."]),
        ("Seven items concerning the lay-mendicant relationship specifically", [
            "Unlike this chapter's mendicant-focused discourses, every item on this list "
            "concerns how a lay follower relates to mendicants and the wider Buddhist "
            "community &mdash; access, attentiveness, trust, and where support is "
            "directed &mdash; rather than any inward meditative quality."]),
        ("A closing verse restating the entire teaching", [
            "Unusually for this collection's shorter formulaic discourses, this one "
            "closes with a full verse restatement of both the decline and non-decline "
            "halves, ending each with the same refrain: a lay follower who practices the "
            "decline-causing seven &ldquo;falls away from the true teaching,&rdquo; while "
            "one who practices the reversal &ldquo;doesn't fall away.&rdquo;"]),
        ("The first of three near-identical discourses", [
            "AN 7.30 and 7.31, immediately following, restate this exact seven-item "
            "content under two further titles &mdash; &ldquo;failures&rdquo; and "
            "&ldquo;downfalls&rdquo; &mdash; a genre convention this series has now met "
            "repeatedly: the same content given more than one name, each presumably "
            "carrying slightly different connotations in the source tradition even where "
            "the underlying list is identical."]),
    ],
    terms=[
        ("upāsaka",
         "&ldquo;lay follower&rdquo; &mdash; this discourse's specific subject, a marked "
         "shift from this chapter's otherwise mendicant-focused non-decline series."),
        ("bhikkhūnaṁ dassanaṁ na labhati",
         "&ldquo;misses out on seeing the mendicants&rdquo; &mdash; the first item, an "
         "issue of access and opportunity rather than inward quality."),
        ("aññatra bāhirakā dakkhiṇeyyaṁ gavesati",
         "&ldquo;seeks outside of the Buddhist community for those worthy of religious "
         "donations&rdquo; &mdash; the sixth item, echoing similar concerns already met at "
         "AN 6.93 in the previous nipāta."),
        ("saddhammā parihāyati",
         "&ldquo;falls away from the true teaching&rdquo; &mdash; the closing verse's "
         "refrain, naming the ultimate stake of this discourse's seven items."),
        ("parihāni, aparihāni",
         "&ldquo;decline, non-decline&rdquo; &mdash; the same framing already met at AN "
         "7.28, now applied to lay followers rather than mendicant trainees."),
    ],
    text_intro=(
        "The discourse in full: seven things leading to a lay follower's decline, their "
        "reversal, and a closing verse restating both. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven things that lead to a lay follower's decline"),
        ("p", "&sect;1", "an7.29:1.1-2.12"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.29:3.1-10.4"),
    ],
    quiz=[
        {"q": "What population does this discourse concern, marking a shift from this "
              "chapter's earlier mendicant-focused discourses?",
         "opts": [
             "Senior mendicants specifically",
             "Lay followers (upāsaka)",
             "Deities",
             "Government ministers"],
         "correct": 1,
         "expl": "A shift in population, though the 'non-decline' framing continues."},
        {"q": "What do all seven items on this discourse's list concern, according to the "
              "guide?",
         "opts": [
             "Inward meditative states exclusively",
             "How a lay follower relates to mendicants and the wider Buddhist community — "
             "access, attentiveness, trust, and where support is directed",
             "Physical health and diet",
             "Political administration"],
         "correct": 1,
         "expl": "The lay-mendicant relationship specifically, not inward cultivation."},
        {"q": "What unusual feature does this discourse have, compared to many of this "
              "collection's shorter formulaic discourses?",
         "opts": [
             "No content beyond a bare list",
             "A closing verse restating the entire teaching, ending each half with a "
             "shared refrain about falling away from, or not falling away from, the true "
             "teaching",
             "A dialogue between two named individuals",
             "A dispute among the mendicants"],
         "correct": 1,
         "expl": "A fuller poetic restatement, unusual for this collection's briefer "
                 "list-form discourses."},
        {"q": "What does this discourse open, according to the guide?",
         "opts": [
             "An isolated, standalone teaching",
             "The first of three discourses (AN 7.29–31) restating this exact content "
             "under two further titles",
             "The chapter's final discourse",
             "A contradiction of AN 7.28's teaching"],
         "correct": 1,
         "expl": "A genre convention already met with this collection's other near-"
                 "identical discourse trios."},
        {"q": "Is a setting stated for AN 7.29?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.28's fresh setting."},
        {"q": "What does the sixth item, seeking donees outside the Buddhist community, "
              "echo from earlier in this series?",
         "opts": [
             "Nothing similar appears elsewhere",
             "A similar concern already met at AN 6.93 in the previous nipāta",
             "AN 7.14's classification of noble persons",
             "AN 7.5's seven kinds of wealth"],
         "correct": 1,
         "expl": "A theme this series has addressed before, in a different specific "
                 "context."},
    ],
    marginalia=[
        ("Seven items on lay decline", [
            "missing mendicants &middot;",
            "neglecting teaching &middot;",
            "no ethics training &middot; suspicion &middot; hostile listening &middot; "
            "wrong donees",
        ]),
        ("The lay-Saṅgha relationship", [
            "access, attentiveness,",
            "trust, and where",
            "support is actually directed",
        ]),
        ("A full verse restatement", [
            "unusual fullness —",
            "'falls away' /",
            "'doesn't fall away' as refrain",
        ]),
        ("Cross-references", [
            "AN 7.30/31 &middot; next, restating this same content under two further "
            "titles",
        ]),
    ],
    further=[
        '<a href="%s/an7.29/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.28.html">AN 7.28 &middot; Non-decline for a Mendicant Trainee</a> '
        "&mdash; previous, the same 'non-decline' framing applied to mendicant trainees.",
        '<a href="an-7.30.html">AN 7.30 &middot; Failures for a Lay Follower</a> &mdash; '
        "next, the identical content restated, heavily compressed.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.30 — Vipattisutta
# --------------------------------------------------------------------------- #
page(
    30, "Vipatti", "Failures for a Lay Follower",
    vagga=VAGGA_3,
    meta_title="AN 7.30 — Failures for a Lay Follower | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Vipattisutta, restating AN 7.29's identical seven-item content under a new "
        "title, compressed almost entirely via Pāli ellipsis. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical content as AN 7.29, compressed to a bare title-change via "
                 "Pāli ellipsis — the second of three near-identical discourses"),
        ("Length", "under 15 seconds to read"),
        ("Northern parallel", "The pairing of 'failure' (vipatti) and 'accomplishment' "
                              "(sampadā) as a technical vocabulary pair recurs across the "
                              "Chinese Āgamas' treatment of lay conduct; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; almost entirely "
                       "elided, pointing back to AN 7.29 for its full content"),
    ],
    why=(
        "AN 7.30 restates AN 7.29's identical seven-item content on a lay follower's "
        "spiritual condition, but under an entirely different technical vocabulary: "
        "vipatti, &ldquo;failure,&rdquo; and its reversal sampadā, "
        "&ldquo;accomplishment,&rdquo; rather than parihāni, &ldquo;decline,&rdquo; and "
        "aparihāni, &ldquo;non-decline.&rdquo; The source compresses the entire "
        "discourse to almost nothing, assuming AN 7.29's full content throughout."),
    guide=[
        ("The teaching in one sentence", [
            "There are seven failures for a lay follower, and seven accomplishments "
            "&mdash; the identical seven items already given in full at AN 7.29, now "
            "under different technical names."]),
        ("A vocabulary shift, not a content shift", [
            "Checked against AN 7.29, this discourse's content is unchanged; only the "
            "governing terms differ. Vipatti and sampadā are a standard paired "
            "vocabulary in this literature's ethical analysis, distinct from parihāni "
            "and aparihāni but describing, in this instance, exactly the same seven-item "
            "reality."]),
        ("Almost total compression", [
            "The source text gives only the bare announcement &mdash; &ldquo;these seven "
            "failures for a lay follower... these seven accomplishments for a lay "
            "follower&rdquo; &mdash; before eliding everything else with "
            "&ldquo;…,&rdquo; trusting a reader who has just read AN 7.29 to supply the "
            "entire remaining content without difficulty."]),
        ("The second of three, with one more restatement to come", [
            "AN 7.31, immediately following, will restate this identical content a third "
            "time under yet another title, this time spelled out again in full rather "
            "than elided &mdash; completing a genre pattern already met at AN 6.89&ndash;"
            "91 in the previous nipāta, where one identical list was restated three times "
            "under three different governing verbs or terms."]),
    ],
    terms=[
        ("vipatti",
         "&ldquo;failure&rdquo; &mdash; this discourse's own title term, replacing AN "
         "7.29's parihāni, decline, though naming the identical seven-item content."),
        ("sampadā",
         "&ldquo;accomplishment&rdquo; &mdash; the reversal's governing term, replacing "
         "AN 7.29's aparihāni, non-decline."),
        ("…pe…",
         "the Pāli ellipsis mark, standing in here for the entirety of AN 7.29's "
         "seven-item content on both sides, blocking and enabling."),
        ("upāsaka",
         "&ldquo;lay follower&rdquo; &mdash; the same subject as AN 7.29, unchanged "
         "across this vocabulary shift."),
        ("aparihāni",
         "&ldquo;non-decline&rdquo; &mdash; AN 7.29's own governing term for the same "
         "content this discourse instead calls sampadā."),
    ],
    text_intro=(
        "The formula exactly as the source compresses it: the identical content as AN "
        "7.29, under new technical names. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The compressed formula"),
        ("p", "&sect;1", "an7.30:1.1-1.2"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 7.29's, checked against "
              "the source?",
         "opts": [
             "Entirely different content",
             "Unchanged — the identical seven items, now governed by different technical "
             "terms (vipatti/sampadā rather than parihāni/aparihāni)",
             "Only half the items overlap",
             "This discourse has no content at all"],
         "correct": 1,
         "expl": "A vocabulary shift, not a content shift."},
        {"q": "What two terms govern this discourse's blocking and enabling halves?",
         "opts": [
             "Parihāni and aparihāni, identical to AN 7.29",
             "Vipatti (failure) and sampadā (accomplishment)",
             "Duccarita and sucarita",
             "Micchā and sammā"],
         "correct": 1,
         "expl": "A standard paired vocabulary distinct from AN 7.29's own terms."},
        {"q": "How compressed is this discourse's own text?",
         "opts": [
             "Fully spelled out, matching AN 7.29's length",
             "Almost total compression — only the bare announcement is given before '…' "
             "elides everything else",
             "Only the closing verse is given",
             "The discourse has no text at all"],
         "correct": 1,
         "expl": "A reader who has just read AN 7.29 can supply the entire remaining "
                 "content."},
        {"q": "What earlier discourse trio in this series does the guide compare this "
              "pattern to?",
         "opts": [
             "AN 6.65/6.66",
             "AN 6.89–91, one identical list restated three times under different "
             "governing terms",
             "AN 6.73/6.74",
             "AN 7.23–27"],
         "correct": 1,
         "expl": "A genre convention already met once before in the previous nipāta."},
        {"q": "Is a setting stated for AN 7.30?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, as compressed as the rest of this discourse."},
        {"q": "What comes next in this three-discourse family, according to the guide?",
         "opts": [
             "The family ends here",
             "AN 7.31, restating this identical content a third time under yet another "
             "title, spelled out again in full",
             "A return to mendicant-focused content",
             "A shift to an unrelated topic"],
         "correct": 1,
         "expl": "One further restatement completes this three-part family."},
    ],
    marginalia=[
        ("A vocabulary shift only", [
            "vipatti, sampadā —",
            "not parihāni, aparihāni —",
            "identical underlying content",
        ]),
        ("Near-total compression", [
            "bare announcement,",
            "then '…' for the",
            "entire remaining content",
        ]),
        ("Second of a three-part family", [
            "AN 7.29 (full),",
            "AN 7.30 (elided),",
            "AN 7.31 (full) — one more to come",
        ]),
        ("Cross-references", [
            "AN 7.29 &middot; previous, this discourse's full template",
            "AN 6.89–91 &middot; earlier nipāta, the same three-restatement pattern",
        ]),
    ],
    further=[
        '<a href="%s/an7.30/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.29.html">AN 7.29 &middot; Non-decline for a Lay Follower</a> '
        "&mdash; previous, this discourse's full template.",
        '<a href="an-7.31.html">AN 7.31 &middot; Downfalls for a Lay Follower</a> &mdash; '
        "next, the same content restated a third time, spelled out in full.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.31 — Parābhavasutta
# --------------------------------------------------------------------------- #
page(
    31, "Parābhava", "Downfalls for a Lay Follower",
    vagga=VAGGA_3,
    meta_title="AN 7.31 — Downfalls for a Lay Follower | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Parābhavasutta, closing this chapter and its lay-follower trilogy by restating "
        "AN 7.29's identical content a third time, spelled out in full under a new "
        "title. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical content as AN 7.29, spelled out in full a third time "
                 "under a new governing vocabulary — closing this chapter"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "'Ruin' or 'downfall' (parābhava) as a technical term for "
                              "spiritual failure recurs across the Chinese Āgamas, most "
                              "famously in verse-form discourses on decline; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; closes this chapter "
                       "and its lay-follower trilogy, spelled out in full for the third "
                       "and final time"),
    ],
    why=(
        "AN 7.31 closes this chapter by restating AN 7.29's identical seven-item content "
        "a third time, now under parābhava and its reversal, &ldquo;downfall&rdquo; and "
        "&ldquo;success&rdquo; &mdash; a third governing vocabulary (after AN 7.29's "
        "parihāni/aparihāni and AN 7.30's vipatti/sampadā) for the identical underlying "
        "seven-item reality, spelled out here in full, closing verses included, rather "
        "than elided as AN 7.30 was."),
    guide=[
        ("The teaching in one sentence", [
            "There are seven downfalls for a lay follower, and seven successes &mdash; "
            "the identical seven items already given at AN 7.29 and AN 7.30, now under a "
            "third governing vocabulary."]),
        ("A third name for one identical reality", [
            "Parābhava (downfall, ruin) and its reversal join parihāni/aparihāni (decline/"
            "non-decline) and vipatti/sampadā (failure/accomplishment) as a third paired "
            "vocabulary applied to this exact seven-item content &mdash; three genuinely "
            "different technical framings the tradition considered each worth stating in "
            "its own right, exactly the pattern already noted at AN 7.11/7.12's treatment "
            "of fetters and underlying tendencies earlier in this book."]),
        ("Spelled out fully, unlike AN 7.30", [
            "Where AN 7.30 compressed its entire content to a bare announcement, this "
            "discourse spells out all seven items, their reversal, and the same closing "
            "verse already met at AN 7.29 &mdash; the third statement in this trilogy "
            "given the fullest possible treatment alongside the first."]),
        ("Closing this chapter on lay practice, after opening on political ethics", [
            "Vajjisattakavagga opened at AN 7.21 with counsel for an entire confederacy's "
            "political survival and closes here with a single lay follower's spiritual "
            "condition &mdash; the same underlying concern, prevention of decline, "
            "scaled from an entire nation down to one person's relationship with the "
            "Buddhist community."]),
    ],
    terms=[
        ("parābhava",
         "&ldquo;downfall, ruin&rdquo; &mdash; this discourse's own title term, the third "
         "governing vocabulary applied to AN 7.29's identical seven-item content."),
        ("sampatti",
         "&ldquo;success&rdquo; &mdash; the reversal's governing term in this discourse, "
         "distinct from AN 7.29's aparihāni and AN 7.30's sampadā though naming the same "
         "underlying reversal."),
        ("bhikkhūnaṁ dassanaṁ na labhati, dhammassavanaṁ na labhati",
         "&ldquo;misses out on seeing the mendicants, misses out on hearing the "
         "teaching&rdquo; &mdash; the first two items, identical across all three "
         "discourses of this trilogy."),
        ("saddhammā parihāyati",
         "&ldquo;falls away from the true teaching&rdquo; &mdash; the closing verse's "
         "refrain, identical word for word to AN 7.29's own closing verse."),
        ("Vajjisattakavagga",
         "&ldquo;the Vajji Seven&rdquo; &mdash; this chapter's own title, closing here "
         "after moving from an entire confederacy's political survival to one lay "
         "follower's spiritual condition."),
    ],
    text_intro=(
        "The discourse in full: seven downfalls for a lay follower, seven successes, and "
        "the same closing verse already met at AN 7.29. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven downfalls, and seven successes"),
        ("p", "&sect;1", "an7.31:1.1-4.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.31:5.1-10.3"),
    ],
    quiz=[
        {"q": "How many different technical vocabularies has this exact seven-item "
              "content now been given, counting this discourse?",
         "opts": [
             "One", "Two", "Three — parihāni/aparihāni at AN 7.29, vipatti/sampadā at AN "
             "7.30, and parābhava/sampatti here", "Five"],
         "correct": 2,
         "expl": "The same content given three distinct technical framings, each "
                 "presumably worth its own statement to the tradition."},
        {"q": "How does this discourse's treatment compare to AN 7.30's, in terms of how "
              "fully it is spelled out?",
         "opts": [
             "Identical — both are heavily elided",
             "This discourse is spelled out fully, including the closing verse, unlike AN "
             "7.30's near-total compression",
             "This discourse is even more compressed than AN 7.30",
             "Neither discourse contains any content"],
         "correct": 1,
         "expl": "The third statement given the fullest possible treatment, matching AN "
                 "7.29's own fullness."},
        {"q": "What earlier discourse in this book does the guide compare this three-"
              "vocabulary pattern to?",
         "opts": [
             "AN 7.1/7.2",
             "AN 7.11/7.12, treating fetters and underlying tendencies as distinct "
             "technical categories for identical content",
             "AN 7.14",
             "AN 7.21"],
         "correct": 1,
         "expl": "A pattern already met once before within this same book."},
        {"q": "How does the guide describe this chapter's overall arc, from AN 7.21 to "
              "this closing discourse?",
         "opts": [
             "No discernible arc across the chapter",
             "From an entire confederacy's political survival (AN 7.21) to one lay "
             "follower's spiritual condition (this discourse) — the same underlying "
             "concern with preventing decline, at different scales",
             "A strictly chronological narrative with no thematic connection",
             "Every discourse in the chapter is identical"],
         "correct": 1,
         "expl": "One theme, prevention of decline, scaled from a nation to a single "
                 "person."},
        {"q": "Is a setting stated for AN 7.31?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching AN 7.29 and 7.30 before it."},
        {"q": "What does the closing verse's refrain state?",
         "opts": [
             "A lay follower who practices the seven items 'falls away from' or 'doesn't "
             "fall away from' the true teaching — identical word for word to AN 7.29's "
             "verse",
             "An entirely new refrain not found in AN 7.29",
             "No verse closes this discourse",
             "A refrain about mendicants specifically, not lay followers"],
         "correct": 0,
         "expl": "The same closing verse already met at AN 7.29, restated here word for "
                 "word."},
    ],
    marginalia=[
        ("A third vocabulary", [
            "parābhava, sampatti —",
            "after parihāni/aparihāni",
            "and vipatti/sampadā",
        ]),
        ("Spelled out fully, again", [
            "unlike AN 7.30's",
            "compression — matching",
            "AN 7.29's full treatment",
        ]),
        ("From nation to person", [
            "AN 7.21: an entire",
            "confederacy — AN 7.31:",
            "one lay follower's condition",
        ]),
        ("Cross-references", [
            "AN 7.29/7.30 &middot; earlier, this same content's first two statements",
            "AN 7.11/7.12 &middot; earlier, a similar three-name pattern",
        ]),
    ],
    further=[
        '<a href="%s/an7.31/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.30.html">AN 7.30 &middot; Failures for a Lay Follower</a> &mdash; '
        "previous, this same content's compressed second statement.",
        '<a href="an-7.21.html">AN 7.21 &middot; At the Sārandada Shrine</a> &mdash; back '
        "to this chapter&rsquo;s opening, for contrast with the chapter now closing.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 4 — Devatāvagga (AN 7.32–43)
# --------------------------------------------------------------------------- #
# Not to be confused with the two earlier chapters of this same name in the
# Sixes (AN 6.31-42 and AN 6.65-74). Unlike those two, THIS Devatāvagga opens
# with an actual deity at its very first discourse.
VAGGA_4 = "<em>Devatāvagga</em> &mdash; the fourth chapter of the Sevens"


# --------------------------------------------------------------------------- #
# AN 7.32 — Appamādagāravasutta
# --------------------------------------------------------------------------- #
page(
    32, "Appamādagārava", "Respect for Diligence",
    vagga=VAGGA_4,
    meta_title="AN 7.32 — Respect for Diligence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Appamādagāravasutta, opening this chapter with an actual deity — unlike the two "
        "earlier chapters of the same name in the Sixes — naming a seven-item respect "
        "formula. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", "A glorious deity, speaking to the Buddha at night; the Buddha, "
                     "retelling it to the mendicants the next morning, closing with verse"),
        ("Form", "A deity's nighttime visit, restated as a closing verse — the first of "
                 "four discourses in this chapter sharing a five-item core respect "
                 "formula"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Nighttime deity visitations delivering formulas of respect "
                              "to the Buddha recur widely across the Saṁyutta and its "
                              "Chinese Āgama parallels; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a formula already met "
                       "several times in this series, worth checking term by term rather "
                       "than assuming identity"),
    ],
    why=(
        "This chapter, Devatāvagga, is the third discourse-chapter of this exact name in "
        "this series &mdash; after two chapters of the same title in the Sixes, neither "
        "of which opened with an actual deity. This one does: a glorious deity visits the "
        "Buddha by night and names seven things that prevent a trainee's decline &mdash; "
        "respect for the Teacher, the teaching, the Saṅgha, the training, and immersion, "
        "plus diligence and hospitality &mdash; a five-item core already met four times in "
        "the Sixes, now extended by one further item and closing on two new terms."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, the training, and "
            "immersion, together with diligence and hospitality, prevents a mendicant "
            "trainee's decline."]),
        ("A fifth variant of a formula already met four times", [
            "This chapter's own reading guides will trace this &ldquo;respect&rdquo; "
            "formula's core &mdash; Teacher, teaching, Saṅgha, training &mdash; through "
            "four prior appearances at AN 6.32, 6.33, 6.40, and 6.69 in the previous "
            "nipāta, each with a different fifth-and-sixth pair. This discourse both "
            "extends the four-item core to five (adding immersion) and closes on a "
            "genuinely new pair: diligence (appamāda) and hospitality (pāricariyā), "
            "matching neither of the four Sixes variants."]),
        ("A five-item core, not four, in this nipāta", [
            "Where every appearance of this formula in the Sixes kept its core at four "
            "items (Teacher, teaching, Saṅgha, training), this discourse and its three "
            "companions in this chapter (AN 7.33&ndash;35) all extend that core to five by "
            "adding immersion &mdash; a structural shift specific to how this formula "
            "recurs in the Sevens."]),
        ("The deity's approval, and the Buddha's own added verse", [
            "As at AN 6.69, the deity's statement earns only the Buddha's silent approval "
            "before it departs; here the Buddha adds something AN 6.69 did not, closing "
            "his retelling to the mendicants with an original verse restating the same "
            "seven items and adding a further claim: a mendicant who respects all seven "
            "&ldquo;has drawn near to extinguishment.&rdquo;"]),
    ],
    terms=[
        ("satthugāravatā, dhammagāravatā, saṅghagāravatā, sikkhāgāravatā, samādhigāravatā",
         "&ldquo;respect for the Teacher, the teaching, the Saṅgha, the training, and "
         "immersion&rdquo; &mdash; this discourse's five-item core, one item larger than "
         "every appearance of this formula in the Sixes."),
        ("appamāda",
         "&ldquo;diligence&rdquo; &mdash; the sixth item, this discourse's own title term, "
         "new to this formula's several appearances."),
        ("pāricariyā",
         "&ldquo;hospitality&rdquo; &mdash; the seventh and closing item, likewise new to "
         "this formula compared to its four earlier variants."),
        ("nibbānassa santike",
         "&ldquo;drawn near to extinguishment&rdquo; &mdash; the Buddha's own added claim "
         "in his closing verse, absent from AN 6.69's otherwise similar structure."),
        ("sekha",
         "&ldquo;trainee&rdquo; &mdash; the population this formula protects from decline, "
         "consistent across all four variants of this formula met so far."),
    ],
    text_intro=(
        "The discourse in full: a deity's nighttime visit, and the Buddha's retelling "
        "with an added closing verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A deity's nighttime visit"),
        ("p", "&sect;1", "an7.32:1.1-2.7"),
        ("h3", "The Buddha's retelling, with a closing verse"),
        ("p", "&sect;2", "an7.32:3.1-5.4"),
    ],
    quiz=[
        {"q": "How many prior appearances has this 'respect' formula's core already had in "
              "this series, before this discourse?",
         "opts": [
             "None — this is the first appearance",
             "Four, at AN 6.32, 6.33, 6.40, and 6.69, each with a different fifth-and-"
             "sixth pair",
             "Only once, at AN 6.69",
             "Ten times"],
         "correct": 1,
         "expl": "A formula this series has now met and checked repeatedly across two "
                 "nipātas."},
        {"q": "How does this discourse's core differ structurally from every Sixes "
              "appearance of the same formula?",
         "opts": [
             "No structural difference at all",
             "This discourse extends the four-item Sixes core (Teacher, teaching, Saṅgha, "
             "training) to five items by adding immersion",
             "This discourse reduces the core to three items",
             "The core is entirely different content"],
         "correct": 1,
         "expl": "A shift specific to how this formula recurs in the Sevens."},
        {"q": "What two items close this discourse's list, distinguishing it from all four "
              "Sixes variants?",
         "opts": [
             "Conscience and prudence",
             "Diligence (appamāda) and hospitality (pāricariyā)",
             "Being easy to admonish and good friendship",
             "Diligence and hospitality applied to four assemblies"],
         "correct": 1,
         "expl": "A genuinely new pair, matching none of the four earlier variants."},
        {"q": "What does the guide say is unique about this discourse compared to AN "
              "6.69's otherwise similar structure?",
         "opts": [
             "Nothing is different",
             "The Buddha adds his own closing verse, including the claim that a mendicant "
             "who respects all seven 'has drawn near to extinguishment'",
             "This discourse has no deity at all",
             "The deity never departs in this discourse"],
         "correct": 1,
         "expl": "An added poetic claim absent from AN 6.69's version."},
        {"q": "What is notable about this chapter's title compared to the two earlier "
              "Devatāvagga chapters in the Sixes?",
         "opts": [
             "This chapter also opens without a deity, matching both earlier chapters",
             "This is the first Devatāvagga in this series to open with an actual deity "
             "at its very first discourse",
             "This chapter has an entirely different title",
             "Deities never appear anywhere in this chapter"],
         "correct": 1,
         "expl": "A departure from the pattern of both earlier same-named chapters."},
        {"q": "Is a setting stated for AN 7.32?",
         "opts": ["Yes, at Sāvatthī, in Jeta's Grove", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 0,
         "expl": "The book's standard opening setting, stated fresh here."},
    ],
    marginalia=[
        ("A five-item core", [
            "Teacher, teaching, Saṅgha,",
            "training, immersion —",
            "one item larger than the Sixes",
        ]),
        ("A new closing pair", [
            "diligence, hospitality —",
            "matching none of the",
            "four earlier variants",
        ]),
        ("A fifth occurrence, checked", [
            "AN 6.32, 33, 40, 69,",
            "and now this discourse —",
            "five distinct closing pairs",
        ]),
        ("Cross-references", [
            "AN 6.32/33/40/69 &middot; earlier nipāta, this formula's four prior "
            "appearances",
            "AN 7.33 &middot; next, a sixth variant",
        ]),
    ],
    further=[
        '<a href="%s/an7.32/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.69.html">AN 6.69 &middot; A God</a> &mdash; earlier nipāta, the '
        "closest structural precedent for this discourse.",
        '<a href="an-7.33.html">AN 7.33 &middot; Respect for Conscience</a> &mdash; next, '
        "a sixth variant of this same formula.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.33 — Hirigāravasutta
# --------------------------------------------------------------------------- #
page(
    33, "Hirigārava", "Respect for Conscience",
    vagga=VAGGA_4,
    meta_title="AN 7.33 — Respect for Conscience | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Hirigāravasutta, a sixth variant of this series' recurring respect formula, "
        "closing on conscience and prudence rather than AN 7.32's diligence and "
        "hospitality. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, retelling a deity's nighttime visit to the mendicants "
                     "the following day"),
        ("Form", "The identical five-item core as AN 7.32, closing on a different pair, "
                 "restated in verse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of conscience and prudence as a joint "
                              "safeguard against decline recurs widely across the Chinese "
                              "Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the same five-item "
                       "core as AN 7.32, closing on yet another distinct pair"),
    ],
    why=(
        "AN 7.33 repeats AN 7.32's five-item core &mdash; respect for the Teacher, the "
        "teaching, the Saṅgha, the training, and immersion &mdash; but closes on a "
        "different pair entirely: conscience (hiri, this discourse's own title term) and "
        "prudence, echoing AN 6.33's closing pair from the Sixes rather than AN 7.32's "
        "diligence and hospitality."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, the training, and "
            "immersion, together with conscience and prudence, prevents a mendicant "
            "trainee's decline."]),
        ("The same core, a different closing pair than its immediate predecessor", [
            "Checked term by term against AN 7.32, this discourse's first five items are "
            "identical; only the sixth and seventh change, from diligence and hospitality "
            "to conscience (hiri) and prudence (ottappa) &mdash; a substitution that "
            "matches AN 6.33's closing pair from the Sixes exactly, though applied here to "
            "the extended five-item core rather than the Sixes' four-item one."]),
        ("A sixth documented variant of this recurring formula", [
            "Counting AN 6.32, 6.33, 6.40, and 6.69 from the previous nipāta, plus AN "
            "7.32 immediately before this discourse, this is the sixth time this series "
            "has met some version of the &ldquo;respect&rdquo; formula, each requiring "
            "individual verification of its closing pair rather than assumption from the "
            "shared opening."]),
        ("No original closing verse this time", [
            "Unlike AN 7.32, which added an original closing verse with the phrase "
            "&ldquo;drawn near to extinguishment,&rdquo; this discourse's verse simply "
            "restates the seven items in poetic form without that additional claim, "
            "closing on &ldquo;it is impossible for them to decline; they have drawn near "
            "to extinguishment&rdquo; &mdash; in fact repeating the same phrase, but as "
            "part of the verse's direct restatement rather than an added original "
            "flourish."]),
    ],
    terms=[
        ("satthugāravatā, dhammagāravatā, saṅghagāravatā, sikkhāgāravatā, samādhigāravatā",
         "the same five-item core as AN 7.32: respect for the Teacher, the teaching, the "
         "Saṅgha, the training, and immersion."),
        ("hiri",
         "&ldquo;conscience&rdquo; &mdash; this discourse's own title term and sixth "
         "item, matching AN 6.33's closing pair from the Sixes."),
        ("ottappa",
         "&ldquo;prudence&rdquo; &mdash; the seventh and closing item, completing the "
         "pair already met at AN 6.33."),
        ("appamāda, pāricariyā",
         "&ldquo;diligence, hospitality&rdquo; &mdash; AN 7.32's own closing pair, absent "
         "from this discourse's version."),
        ("nibbānassa santike",
         "&ldquo;drawn near to extinguishment&rdquo; &mdash; the closing verse's phrase, "
         "shared with AN 7.32 though functioning here as direct restatement rather than "
         "an added claim."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's retelling of a deity's visit, closing on "
        "conscience and prudence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha retells the deity's visit"),
        ("p", "&sect;1", "an7.33:1.1-2.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.33:3.1-3.4"),
    ],
    quiz=[
        {"q": "How many of this discourse's seven items are identical to AN 7.32's, "
              "checked term by term?",
         "opts": [
             "None", "Five — only the sixth and seventh items differ", "All seven", "Only two"],
         "correct": 1,
         "expl": "The same five-item core, closing on a different pair."},
        {"q": "What pair closes this discourse's list, and where has it already appeared "
              "in this series?",
         "opts": [
             "Diligence and hospitality, new to this series",
             "Conscience (hiri) and prudence (ottappa), matching AN 6.33's closing pair "
             "from the Sixes",
             "Easy to admonish and good friendship, matching AN 6.69",
             "A pair not found anywhere else in this series"],
         "correct": 1,
         "expl": "A pair already documented once before, in the previous nipāta."},
        {"q": "How many total variants of this 'respect' formula has this series now met, "
              "counting this discourse?",
         "opts": [
             "Two", "Six — AN 6.32, 6.33, 6.40, 6.69, AN 7.32, and this discourse", "Three", "This is the only variant"],
         "correct": 1,
         "expl": "A formula requiring individual verification at every appearance, now "
                 "met six times."},
        {"q": "How does this discourse's closing verse compare to AN 7.32's, according to "
              "the guide?",
         "opts": [
             "Identical original content added by the Buddha in both cases",
             "This discourse's verse restates the seven items without AN 7.32's added "
             "original flourish, though it shares the same 'drawn near to extinguishment' "
             "phrase as part of its direct restatement",
             "This discourse has no closing verse at all",
             "The two verses share no language in common"],
         "correct": 1,
         "expl": "A shared phrase functioning differently in each discourse's structure."},
        {"q": "Is a setting stated for AN 7.33?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.32's fresh setting."},
        {"q": "What does <em>hiri</em> mean?",
         "opts": ["Prudence", "Conscience", "Diligence", "Hospitality"],
         "correct": 1,
         "expl": "This discourse's own title term, the sixth item on its list."},
    ],
    marginalia=[
        ("Five items shared with 7.32", [
            "Teacher, teaching, Saṅgha,",
            "training, immersion —",
            "identical core",
        ]),
        ("A different closing pair", [
            "conscience, prudence —",
            "matching AN 6.33's",
            "pair from the Sixes",
        ]),
        ("A sixth documented variant", [
            "AN 6.32, 33, 40, 69,",
            "AN 7.32, and now",
            "this discourse — six closing pairs",
        ]),
        ("Cross-references", [
            "AN 6.33 &middot; earlier nipāta, source of this discourse's closing pair",
            "AN 7.32 &middot; previous, sharing this discourse's five-item core",
        ]),
    ],
    further=[
        '<a href="%s/an7.33/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.33.html">AN 6.33 &middot; Non-decline (2nd)</a> &mdash; earlier '
        "nipāta, source of this discourse's closing pair.",
        '<a href="an-7.34.html">AN 7.34 &middot; Easy to Admonish (1st)</a> &mdash; next, '
        "a seventh variant of this formula.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.34 — Paṭhamasovacassatāsutta
# --------------------------------------------------------------------------- #
page(
    34, "Paṭhamasovacassatā", "Easy to Admonish (1st)",
    vagga=VAGGA_4,
    meta_title="AN 7.34 — Easy to Admonish (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamasovacassatāsutta, a seventh variant of this series' respect formula, "
        "closing on being easy to admonish and good friendship — the same pair already "
        "met at AN 6.69. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, retelling a deity's nighttime visit to the mendicants"),
        ("Form", "The identical five-item core as AN 7.32/33, closing on a pair already "
                 "met once before in this series"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Being easy to admonish paired with good friendship as a "
                              "joint safeguard recurs widely across the Chinese Āgamas' "
                              "monastic conduct material; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the same five-item "
                       "core as its two predecessors, closing on a pair this series has "
                       "specifically met once before, at AN 6.69"),
    ],
    why=(
        "AN 7.34 repeats AN 7.32/33's five-item core and closes on a pair this series has "
        "met once before, at AN 6.69 in the previous nipāta: being easy to admonish "
        "(sovacassatā, this discourse's own title term) and good friendship &mdash; the "
        "same closing pair, now applied to the extended five-item core rather than AN "
        "6.69's four-item one."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, the training, and "
            "immersion, together with being easy to admonish and good friendship, "
            "prevents a mendicant trainee's decline."]),
        ("A closing pair matching AN 6.69 exactly", [
            "Sovacassatā (being easy to admonish) and kalyāṇamittatā (good friendship) "
            "were already named together as the fifth and sixth items of AN 6.69's own "
            "respect formula in the Sixes. This discourse repeats that exact pair, making "
            "it the first of this series' several 'respect' variants to reuse a closing "
            "pair rather than introduce a new one."]),
        ("Seven appearances, now with a genuine repeat", [
            "Counting AN 6.32, 6.33, 6.40, 6.69, AN 7.32, and 7.33, this is the seventh "
            "time this series has met some version of the respect formula &mdash; and the "
            "first time a closing pair has repeated exactly rather than varying, "
            "confirming that this formula's closing items form a limited, recurring set "
            "rather than an inexhaustible supply of fresh substitutions."]),
        ("AN 7.35, immediately following, restates this exact same list", [
            "Unlike the pattern of AN 7.32/33 introducing new pairs, AN 7.35 will repeat "
            "this discourse's exact seven items again, differing only in how the teaching "
            "closes: with Sāriputta's detailed exposition rather than a summary verse."]),
    ],
    terms=[
        ("satthugāravatā, dhammagāravatā, saṅghagāravatā, sikkhāgāravatā, samādhigāravatā",
         "the same five-item core as AN 7.32 and 7.33: respect for the Teacher, the "
         "teaching, the Saṅgha, the training, and immersion."),
        ("sovacassatā",
         "&ldquo;being easy to admonish&rdquo; &mdash; this discourse's own title term "
         "and sixth item, matching AN 6.69's closing pair exactly."),
        ("kalyāṇamittatā",
         "&ldquo;good friendship&rdquo; &mdash; the seventh and closing item, likewise "
         "matching AN 6.69."),
        ("hiri, ottappa",
         "&ldquo;conscience, prudence&rdquo; &mdash; AN 7.33's own closing pair, absent "
         "from this discourse's version."),
        ("appamāda, pāricariyā",
         "&ldquo;diligence, hospitality&rdquo; &mdash; AN 7.32's closing pair, likewise "
         "absent here."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's retelling of a deity's visit, closing on "
        "being easy to admonish and good friendship. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha retells the deity's visit"),
        ("p", "&sect;1", "an7.34:1.1-2.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.34:3.1-3.4"),
    ],
    quiz=[
        {"q": "What closing pair does this discourse share exactly with an earlier "
              "discourse in this series?",
         "opts": [
             "Diligence and hospitality, matching AN 7.32",
             "Being easy to admonish and good friendship, matching AN 6.69 exactly",
             "Conscience and prudence, matching AN 6.33",
             "A pair unique to this discourse alone"],
         "correct": 1,
         "expl": "The first exact repeat of a closing pair among this series' respect "
                 "formula variants."},
        {"q": "What does the guide say this exact repeat confirms about this formula's "
              "closing items?",
         "opts": [
             "That every appearance must have a new, unique pair",
             "That the closing items form a limited, recurring set rather than an "
             "inexhaustible supply of fresh substitutions",
             "That this discourse is a copying error",
             "That only three closing pairs exist in the entire canon"],
         "correct": 1,
         "expl": "A finite pool of pairs the tradition draws from repeatedly."},
        {"q": "How many times has this series now met some version of the respect "
              "formula, counting this discourse?",
         "opts": [
             "Three", "Seven — AN 6.32, 6.33, 6.40, 6.69, AN 7.32, 7.33, and this discourse", "One", "Twelve"],
         "correct": 1,
         "expl": "A formula this series has tracked carefully across two nipātas."},
        {"q": "What does AN 7.35, immediately following, do with this discourse's exact "
              "content?",
         "opts": [
             "Introduces an entirely new list",
             "Restates the identical seven items, differing only in closing with "
             "Sāriputta's detailed exposition rather than a summary verse",
             "Contradicts this discourse's teaching",
             "Has no relationship to this discourse at all"],
         "correct": 1,
         "expl": "Same content, different closing treatment — echoing AN 6.69's own "
                 "structure."},
        {"q": "Is a setting stated for AN 7.34?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.33 immediately before it."},
        {"q": "What does <em>sovacassatā</em> mean?",
         "opts": ["Good friendship", "Being easy to admonish", "Diligence", "Conscience"],
         "correct": 1,
         "expl": "This discourse's own title term and sixth item."},
    ],
    marginalia=[
        ("Five items shared", [
            "Teacher, teaching, Saṅgha,",
            "training, immersion —",
            "identical to AN 7.32/33",
        ]),
        ("A repeated closing pair", [
            "easy to admonish,",
            "good friendship —",
            "exactly matching AN 6.69",
        ]),
        ("A finite pool, confirmed", [
            "the first exact repeat",
            "among this formula's",
            "several closing-pair variants",
        ]),
        ("Cross-references", [
            "AN 6.69 &middot; earlier nipāta, source of this discourse's exact closing "
            "pair",
            "AN 7.35 &middot; next, this exact content with a different closing treatment",
        ]),
    ],
    further=[
        '<a href="%s/an7.34/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.69.html">AN 6.69 &middot; A God</a> &mdash; earlier nipāta, source '
        "of this discourse's exact closing pair.",
        '<a href="an-7.35.html">AN 7.35 &middot; Easy to Admonish (2nd)</a> &mdash; next, '
        "this exact content closing with Sāriputta's exposition instead.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.35 — Dutiyasovacassatāsutta
# --------------------------------------------------------------------------- #
page(
    35, "Dutiyasovacassatā", "Easy to Admonish (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 7.35 — Easy to Admonish (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyasovacassatāsutta, restating AN 7.34's identical seven items and closing "
        "with Sāriputta's detailed exposition, confirmed word for word by the Buddha. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, retelling a deity's visit; Venerable Sāriputta, "
                     "supplying the detailed meaning; the Buddha, confirming it in full"),
        ("Form", "The identical content as AN 7.34, closing with a brief-statement/"
                 "detailed-explanation exchange rather than a verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Sāriputta expanding a brief statement into its detailed "
                              "meaning, confirmed word for word by the Buddha, recurs as a "
                              "recognizable genre across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the same content as "
                       "AN 7.34, given its fullest possible treatment through Sāriputta's "
                       "exposition"),
    ],
    why=(
        "AN 7.35 restates AN 7.34's identical seven items &mdash; the same five-item core "
        "plus being easy to admonish and good friendship &mdash; but closes not with a "
        "verse, as AN 7.34 did, but with the same brief-statement/detailed-explanation "
        "exchange already met at AN 6.69: Sāriputta supplies the meaning of the deity's "
        "brief report, and the Buddha confirms it word for word."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, the training, and "
            "immersion, together with being easy to admonish and good friendship, "
            "prevents a mendicant trainee's decline, each item fulfilled by personally "
            "holding it, encouraging others toward it, and praising those who have it."]),
        ("Identical content, a genuinely different closing structure", [
            "Checked term by term, this discourse's seven items are identical to AN "
            "7.34's. What differs entirely is what happens after the deity's report: "
            "rather than the Buddha adding a closing verse, Sāriputta steps forward to "
            "explain the brief statement's detailed meaning, exactly as he did at AN "
            "6.69."]),
        ("The three-part fulfillment formula, applied to seven items instead of six", [
            "Sāriputta's explanation gives each of the seven items the identical "
            "treatment already met at AN 6.69: personally holding it, praising it, "
            "encouraging others who lack it, and praising those who already have it "
            "&ldquo;at the right time, truthfully and correctly&rdquo; &mdash; the same "
            "three-part structure, now run across one more item than its Sixes "
            "precedent."]),
        ("The Buddha's confirmation, unchanged from AN 6.69's pattern", [
            "As at AN 6.69, the Buddha does not correct or add to Sāriputta's "
            "explanation; he repeats it in full and calls it &ldquo;good, good&rdquo; "
            "&mdash; the same structure of confirmation by exact echo, now completing "
            "this chapter's fourth and final respect-formula variant."]),
    ],
    terms=[
        ("satthugāravatā, dhammagāravatā, saṅghagāravatā, sikkhāgāravatā, "
         "samādhigāravatā, sovacassatā, kalyāṇamittatā",
         "the identical seven items already given at AN 7.34: the five-item respect "
         "core, being easy to admonish, and good friendship."),
        ("saṅkhittena bhāsitassa vitthārena attho",
         "&ldquo;the detailed meaning of what was stated in brief&rdquo; &mdash; the "
         "exact exchange already met at AN 6.69, here run across seven items instead of "
         "six."),
        ("attanā ca... vaṇṇavādī",
         "&ldquo;personally... and praises such&rdquo; &mdash; the first part of the "
         "three-part fulfillment formula applied to each of the seven items."),
        ("samādāpeti",
         "&ldquo;encourages&rdquo; &mdash; the second part, encouraging other mendicants "
         "who lack a given quality to develop it."),
        ("sādhu sādhu",
         "&ldquo;good, good&rdquo; &mdash; the Buddha's confirmation of Sāriputta's "
         "explanation, repeated in full rather than corrected."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's retelling, Sāriputta's detailed "
        "explanation, and the Buddha's confirmation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha retells the deity's visit"),
        ("p", "&sect;1", "an7.35:1.1-2.4"),
        ("h3", "Sāriputta's detailed explanation"),
        ("p", "&sect;2", "an7.35:2.5-2.14"),
        ("h3", "The Buddha's confirmation"),
        ("p", "&sect;3", "an7.35:3.1-3.14"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 7.34's, checked term by "
              "term?",
         "opts": [
             "Entirely different content",
             "Identical — the same seven items — but closing with a different structure",
             "Only five of seven items overlap",
             "No relationship between the two discourses"],
         "correct": 1,
         "expl": "Same content, differently closed."},
        {"q": "What closes this discourse, unlike AN 7.34's summary verse?",
         "opts": [
             "Nothing — the discourse simply ends",
             "The same brief-statement/detailed-explanation exchange already met at AN "
             "6.69, with Sāriputta supplying the meaning and the Buddha confirming it",
             "A dialogue with a different deity",
             "A dispute between two mendicants"],
         "correct": 1,
         "expl": "A recognizable genre already established once before in this series."},
        {"q": "What three-part treatment does Sāriputta give each of the seven items?",
         "opts": [
             "Only personal practice, with nothing further",
             "Personally holding it, encouraging others who lack it, and praising others "
             "who already have it",
             "Only teaching it publicly",
             "Renouncing it before taking it up again"],
         "correct": 1,
         "expl": "The identical three-part structure already met at AN 6.69, now applied "
                 "to seven items."},
        {"q": "How does the Buddha respond to Sāriputta's explanation?",
         "opts": [
             "He corrects several points",
             "He repeats it in full and calls it 'good, good' — confirmation by exact "
             "echo, unchanged from AN 6.69's pattern",
             "He rejects it entirely",
             "He remains silent"],
         "correct": 1,
         "expl": "The identical confirmation structure already established at AN 6.69."},
        {"q": "What does this discourse complete, according to the guide?",
         "opts": [
             "Nothing further — an isolated teaching",
             "This chapter's fourth and final respect-formula variant",
             "The entire chapter",
             "The entire Sevens collection"],
         "correct": 1,
         "expl": "The last of four respect-formula discourses opening this chapter."},
        {"q": "Is a setting stated for AN 7.35?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching AN 7.34 immediately before it."},
    ],
    marginalia=[
        ("Identical seven items", [
            "same five-item core",
            "plus easy to admonish,",
            "good friendship — as AN 7.34",
        ]),
        ("A different closing structure", [
            "not a summary verse —",
            "Sāriputta's detailed",
            "exposition, as at AN 6.69",
        ]),
        ("Confirmation by exact echo", [
            "'good, good, Sāriputta' —",
            "the Buddha repeats,",
            "not corrects, the explanation",
        ]),
        ("Cross-references", [
            "AN 7.34 &middot; previous, this discourse's identical content",
            "AN 6.69 &middot; earlier nipāta, this closing structure's precedent",
        ]),
    ],
    further=[
        '<a href="%s/an7.35/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.34.html">AN 7.34 &middot; Easy to Admonish (1st)</a> &mdash; '
        "previous, this discourse's identical content.",
        '<a href="an-6.69.html">AN 6.69 &middot; A God</a> &mdash; earlier nipāta, this '
        "closing structure's precedent.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.36 — Paṭhamamittasutta
# --------------------------------------------------------------------------- #
page(
    36, "Paṭhamamitta", "A Friend (1st)",
    vagga=VAGGA_4,
    meta_title="AN 7.36 — A Friend (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamamittasutta, naming seven qualities of a friend worth associating with, "
        "closing on verse. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, closing on verse — the first of two "
                 "genuinely different discourses on friendship in this chapter"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of giving what is hard to give with keeping "
                              "secrets as marks of true friendship recurs widely across "
                              "the Chinese Āgamas' ethical material; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and concrete, "
                       "naming qualities recognizable from ordinary experience rather "
                       "than technical categories"),
    ],
    why=(
        "AN 7.36 shifts this chapter's register entirely, from deity-delivered respect "
        "formulas to the ordinary, recognizable qualities of a true friend: giving what "
        "is hard to give, doing what is hard to do, enduring what is hard to endure, "
        "sharing and keeping secrets, and standing by someone in times of trouble or "
        "loss."),
    guide=[
        ("The teaching in one sentence", [
            "One should associate with a friend who gives what is hard to give, does "
            "what is hard to do, endures what is hard to endure, shares and keeps "
            "secrets, and doesn't abandon or look down on you in times of trouble or "
            "loss."]),
        ("Difficulty as the list's own organizing thread", [
            "The first three items are explicitly framed around what is hard "
            "(dukkara): giving what is hard to give, doing what is hard to do, enduring "
            "what is hard to endure &mdash; friendship tested against exactly the "
            "circumstances where lesser relationships would fail."]),
        ("Reciprocal trust, at the list's center", [
            "The fourth and fifth items concern secrets specifically: a true friend both "
            "reveals their own secrets to you and keeps the secrets you share with them "
            "&mdash; trust running in both directions, not a one-sided disclosure."]),
        ("Loyalty in decline, closing the list", [
            "The final two items name what a true friend does not do: abandon you in "
            "times of trouble, or look down on you in times of loss &mdash; naming "
            "friendship's real test as what happens precisely when a person has least to "
            "offer in return."]),
    ],
    terms=[
        ("dukkaraṁ dadāti, dukkaraṁ karoti, dukkaraṁ khamati",
         "&ldquo;gives what is hard to give, does what is hard to do, endures what is "
         "hard to endure&rdquo; &mdash; the first three items, explicitly framed around "
         "difficulty."),
        ("guyhamassa āvi karoti, guyhamassa pariguhati",
         "&ldquo;reveals their secrets to you, keeps your secrets&rdquo; &mdash; the "
         "fourth and fifth items, trust running in both directions."),
        ("āpadāsu na jahati",
         "&ldquo;doesn't abandon you in times of trouble&rdquo; &mdash; the sixth item."),
        ("khīṇena nātimaññati",
         "&ldquo;doesn't look down on you in times of loss&rdquo; &mdash; the seventh and "
         "closing item."),
        ("mitta",
         "&ldquo;friend&rdquo; &mdash; this discourse's own subject, defined here through "
         "seven concrete, recognizable qualities."),
    ],
    text_intro=(
        "The discourse in full: seven qualities of a friend worth associating with, "
        "closing on verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven qualities of a friend"),
        ("p", "&sect;1", "an7.36:1.1-1.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.36:2.1-4.4"),
    ],
    quiz=[
        {"q": "What organizes the first three items on this discourse's list, according "
              "to the guide?",
         "opts": [
             "Physical strength", "Difficulty (dukkara) — giving, doing, and enduring "
             "what is hard", "Wealth and status", "Scriptural learning"],
         "correct": 1,
         "expl": "Friendship tested against circumstances where lesser relationships "
                 "would fail."},
        {"q": "What do the fourth and fifth items concern?",
         "opts": [
             "Physical gifts only",
             "Secrets — a friend both reveals their own secrets and keeps yours, trust "
             "running in both directions",
             "Formal religious vows",
             "Public praise"],
         "correct": 1,
         "expl": "Reciprocal trust, not one-sided disclosure."},
        {"q": "What do the final two items name, according to the guide?",
         "opts": [
             "What a friend gains from the relationship",
             "What a true friend does not do — abandon you in trouble, or look down on "
             "you in loss — naming friendship's real test",
             "A friend's religious beliefs",
             "A friend's physical appearance"],
         "correct": 1,
         "expl": "The test of friendship precisely when a person has least to offer in "
                 "return."},
        {"q": "How does this discourse's register compare to this chapter's opening four "
              "discourses (AN 7.32–35)?",
         "opts": [
             "Identical register throughout",
             "A shift from deity-delivered respect formulas to ordinary, recognizable "
             "qualities of friendship",
             "This discourse also involves a deity",
             "No discernible difference in register"],
         "correct": 1,
         "expl": "Concrete, everyday qualities rather than technical or formulaic content."},
        {"q": "Is a setting stated for AN 7.36?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, despite its concrete, relatable subject matter."},
        {"q": "What does the discourse's closing verse do?",
         "opts": [
             "Introduces new content not in the prose list",
             "Restates the same seven qualities poetically, closing with an "
             "encouragement to keep company with such a friend",
             "Contradicts the prose list",
             "Concerns an entirely different topic"],
         "correct": 1,
         "expl": "A poetic restatement reinforcing the same seven qualities."},
    ],
    marginalia=[
        ("Seven marks of friendship", [
            "gives, does, endures",
            "what's hard &middot; shares, keeps",
            "secrets &middot; loyal in trouble, loss",
        ]),
        ("Tested by difficulty", [
            "not comfort — a friend",
            "proven by what's hard",
            "to give, do, and endure",
        ]),
        ("A register shift", [
            "from deity-delivered",
            "formulas to ordinary,",
            "recognizable human qualities",
        ]),
        ("Cross-references", [
            "AN 7.37 &middot; next, a second, genuinely different list on friendship",
        ]),
    ],
    further=[
        '<a href="%s/an7.36/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.35.html">AN 7.35 &middot; Easy to Admonish (2nd)</a> &mdash; '
        "previous, closing this chapter's respect-formula discourses.",
        '<a href="an-7.37.html">AN 7.37 &middot; A Friend (2nd)</a> &mdash; next, a '
        "genuinely different seven-item list on friendship.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.37 — Dutiyamittasutta
# --------------------------------------------------------------------------- #
page(
    37, "Dutiyamitta", "A Friend (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 7.37 — A Friend (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyamittasutta, a genuinely different seven-item list on friendship, worth "
        "staying close to even if they send you away. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, closing on verse — checked against AN 7.36 "
                 "and found genuinely distinct"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of a friend who admonishes with one who "
                              "accepts admonishment recurs widely across the Chinese "
                              "Āgamas' treatment of spiritual companionship; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; names qualities of "
                       "correction and honesty rather than AN 7.36's qualities of "
                       "loyalty and difficulty"),
    ],
    why=(
        "AN 7.37, sharing its title's shape with AN 7.36 (&lsquo;A Friend&rsquo;), names "
        "an entirely different seven-item list, checked term by term: a friend worth "
        "staying close to even if they drive you away is likable, respected, admonishes "
        "you and accepts admonishment, speaks on deep matters, and never urges you "
        "toward bad conduct."),
    guide=[
        ("The teaching in one sentence", [
            "A friend with seven qualities &mdash; likable, respected, an admonisher who "
            "accepts admonishment, one who speaks on deep matters, and one who never "
            "urges bad conduct &mdash; is worth associating with, even if they drive you "
            "away."]),
        ("Checked against AN 7.36: no shared items", [
            "Unlike several of this chapter's other same-titled pairs, this discourse "
            "and AN 7.36 share no items at all when checked term by term. Where AN "
            "7.36's list concerned loyalty tested by difficulty and secrecy, this "
            "discourse's list concerns honesty, correction, and depth of conversation "
            "&mdash; genuinely different criteria for the same underlying relationship."]),
        ("A friend worth keeping even when they push you away", [
            "The discourse's most striking claim is its opening qualifier: such a friend "
            "is worth staying close to &ldquo;even if they drive you away&rdquo; &mdash; "
            "suggesting that being pushed away by someone with these seven qualities is "
            "not itself evidence the friendship has failed, but potentially part of what "
            "makes them worth keeping."]),
        ("Mutual admonishment, not one-directional correction", [
            "The list's central pair &mdash; admonishing you and accepting "
            "admonishment &mdash; describes a friend capable of both giving and "
            "receiving correction, rather than someone who only points out others' faults "
            "while remaining above correction themselves."]),
    ],
    terms=[
        ("piya, garu",
         "&ldquo;likable, respected&rdquo; &mdash; the first two items, opening this "
         "discourse's list."),
        ("vattā ca hoti vacanakkhamo ca",
         "&ldquo;admonishes you and accepts admonishment&rdquo; &mdash; the discourse's "
         "central pair, describing mutual rather than one-directional correction."),
        ("gambhīrañca kathaṁ kattā",
         "&ldquo;speaks on deep matters&rdquo; &mdash; the sixth item, naming "
         "conversational depth as a mark of true friendship."),
        ("no ca aṭṭhāne niyojaye",
         "&ldquo;doesn't urge you to do bad things&rdquo; &mdash; the seventh and closing "
         "item."),
        ("api pabbājayamānena",
         "&ldquo;even if they drive you away&rdquo; &mdash; the discourse's opening "
         "qualifier, its most striking claim about this kind of friend's worth."),
    ],
    text_intro=(
        "The discourse in full: seven qualities of a friend worth staying close to even "
        "if they drive you away, closing on verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven qualities of a friend"),
        ("p", "&sect;1", "an7.37:1.1-1.4"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an7.37:2.1-3.6"),
    ],
    quiz=[
        {"q": "How does this discourse's seven-item list compare to AN 7.36's, checked "
              "term by term?",
         "opts": [
             "Identical content, just reworded",
             "No shared items at all — genuinely different criteria for the same "
             "underlying relationship",
             "Half the items overlap",
             "Only the closing item is shared"],
         "correct": 1,
         "expl": "Two same-titled discourses sharing no specific content, checked "
                 "carefully."},
        {"q": "What is the discourse's most striking claim, according to the guide?",
         "opts": [
             "That such a friend should never be trusted",
             "That such a friend is worth staying close to 'even if they drive you away' "
             "— being pushed away is not itself evidence the friendship has failed",
             "That such a friend will never disagree with you",
             "That friendship always ends badly"],
         "correct": 1,
         "expl": "A striking reframing of what being sent away might actually mean."},
        {"q": "What does the central pair, 'admonishes you and accepts admonishment,' "
              "describe?",
         "opts": [
             "A friend who only criticizes others",
             "Mutual correction — a friend capable of both giving and receiving "
             "admonishment, not someone who remains above correction themselves",
             "A friend who never speaks critically",
             "A formal teacher-student relationship only"],
         "correct": 1,
         "expl": "Correction flowing in both directions, not one-sided judgment."},
        {"q": "What does the seventh item concern?",
         "opts": [
             "Wealth and generosity",
             "Never urging you toward bad conduct",
             "Physical strength",
             "Formal religious training"],
         "correct": 1,
         "expl": "The closing item, protecting against a friend's harmful influence."},
        {"q": "Is a setting stated for AN 7.37?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.36 immediately before it."},
        {"q": "What does <em>gambhīrañca kathaṁ kattā</em> mean?",
         "opts": [
             "Speaks only casually", "Speaks on deep matters", "Never speaks at all", "Speaks only about wealth"],
         "correct": 1,
         "expl": "Conversational depth, named as a mark of true friendship."},
    ],
    marginalia=[
        ("Seven different qualities", [
            "likable, respected &middot;",
            "admonishes, accepts",
            "admonishment &middot; deep talk &middot; no bad urging",
        ]),
        ("No overlap with AN 7.36", [
            "checked term by term —",
            "genuinely different",
            "criteria for the same relationship",
        ]),
        ("Worth keeping, even when pushed away", [
            "'even if they",
            "drive you away' —",
            "a striking reframing",
        ]),
        ("Cross-references", [
            "AN 7.36 &middot; previous, a same-titled but content-distinct companion",
        ]),
    ],
    further=[
        '<a href="%s/an7.37/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.36.html">AN 7.36 &middot; A Friend (1st)</a> &mdash; previous, a '
        "same-titled but content-distinct companion.",
        '<a href="an-7.38.html">AN 7.38 &middot; Textual Analysis (1st)</a> &mdash; next, '
        "a shift to seven qualities for realizing textual analysis.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.38 — Paṭhamapaṭisambhidāsutta
# --------------------------------------------------------------------------- #
page(
    38, "Paṭhamapaṭisambhidā", "Textual Analysis (1st)",
    vagga=VAGGA_4,
    meta_title="AN 7.38 — Textual Analysis (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamapaṭisambhidāsutta, naming seven qualities of mental discernment that let "
        "a mendicant soon realize the four kinds of textual analysis. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list, stated once with no reversal, the first of a "
                 "brief/Sāriputta-example pair"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The four kinds of textual analysis (paṭisambhidā) as a "
                              "standard technical set recur throughout the Chinese Āgamas "
                              "and Abhidharma literature; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; names precise "
                       "technical distinctions in mental observation, denser than this "
                       "chapter's other discourses"),
    ],
    why=(
        "AN 7.38 names seven qualities of precise mental observation &mdash; recognizing "
        "sluggishness, an internally constricted mind, an externally scattered mind, "
        "watching feelings, perceptions, and thoughts arise and pass, and properly "
        "grasping the whole pattern of qualities encountered &mdash; that let a "
        "mendicant soon realize the four kinds of textual analysis through their own "
        "insight."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who recognizes sluggishness, an internally constricted mind, an "
            "externally scattered mind, and who watches feelings, perceptions, and "
            "thoughts arise and pass while properly grasping the whole pattern of "
            "qualities encountered, will soon realize the four kinds of textual "
            "analysis."]),
        ("Paṭisambhidā, a specific analytical attainment", [
            "The four kinds of textual analysis &mdash; of meaning, of the teaching, of "
            "language, and of eloquent expression &mdash; are a standard set of "
            "analytical capacities in this literature, treated here as reachable through "
            "sustained precise attention rather than through learning alone."]),
        ("Three named obstacles to attention, immediately followed by their remedy", [
            "The list's first three items each name a specific way attention can go "
            "wrong &mdash; sluggish, too internally constricted, or too externally "
            "scattered &mdash; framed as things to truly understand rather than simply "
            "avoid, implying accurate recognition of a distorted state is itself part of "
            "the practice."]),
        ("Watching three processes arise, remain, and pass", [
            "The middle three items apply an identical threefold observation &mdash; as "
            "they arise, as they remain, as they go away &mdash; to feelings, "
            "perceptions, and thoughts in turn, a repeated analytical structure applied "
            "across three different objects of experience."]),
    ],
    terms=[
        ("paṭisambhidā",
         "&ldquo;textual analysis&rdquo; &mdash; the fourfold analytical attainment "
         "(meaning, teaching, language, eloquent expression) this discourse's seven "
         "qualities are said to produce."),
        ("līnattaṁ cittassa",
         "&ldquo;mental sluggishness&rdquo; &mdash; the first quality, recognizing a "
         "specific way attention can go wrong."),
        ("ajjhattaṁ saṅkhittaṁ, bahiddhā vikkhittaṁ",
         "&ldquo;internally constricted mind, externally scattered mind&rdquo; &mdash; "
         "the second and third qualities, two further specific distortions."),
        ("uppādañca vayañca",
         "&ldquo;as they arise... as they go away&rdquo; &mdash; the threefold "
         "observation applied to feelings, perceptions, and thoughts in turn."),
        ("suggahitā... sumanasikatā... suppaṭividdhā paññāya",
         "&ldquo;properly grasped... borne in mind... penetrated with wisdom&rdquo; "
         "&mdash; the seventh and closing quality, a comprehensive grasp of the whole "
         "pattern of qualities encountered."),
    ],
    text_intro=(
        "The discourse in full: seven qualities of precise mental observation leading to "
        "textual analysis. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven qualities leading to textual analysis"),
        ("p", "&sect;1", "an7.38:1.1-1.10"),
    ],
    quiz=[
        {"q": "What does <em>paṭisambhidā</em> name, and what does this discourse claim "
              "produces it?",
         "opts": [
             "A physical healing power, produced by chanting",
             "The fourfold analytical attainment (meaning, teaching, language, eloquent "
             "expression), produced through sustained precise attention",
             "A form of psychic power unrelated to analysis",
             "A synonym for the four noble truths"],
         "correct": 1,
         "expl": "A specific technical set of analytical capacities."},
        {"q": "What do the first three items on this discourse's list have in common, "
              "according to the guide?",
         "opts": [
             "They are unrelated to attention entirely",
             "Each names a specific way attention can go wrong — sluggish, internally "
             "constricted, or externally scattered — framed as things to truly understand",
             "They describe three different physical postures",
             "They concern only sense-restraint"],
         "correct": 1,
         "expl": "Accurate recognition of distorted states, not merely their avoidance."},
        {"q": "What threefold observation applies to feelings, perceptions, and thoughts "
              "in the middle three items?",
         "opts": [
             "Whether they are wholesome or unwholesome",
             "As they arise, as they remain, and as they go away",
             "Whether they are strong or weak",
             "Whether they belong to oneself or another"],
         "correct": 1,
         "expl": "A repeated analytical structure applied across three objects of "
                 "experience."},
        {"q": "What does the discourse open a pair with, according to the guide?",
         "opts": [
             "No further discourse relates to this one",
             "AN 7.39, applying the identical seven-item list specifically to Sāriputta's "
             "own attainment",
             "A return to the respect formula",
             "A dispute among sectarians"],
         "correct": 1,
         "expl": "A brief/Sāriputta-example pair, a pattern this chapter will repeat."},
        {"q": "Is a setting stated for AN 7.38?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.37 immediately before it."},
        {"q": "What does the seventh and final quality involve?",
         "opts": [
             "Ignoring most encountered qualities",
             "Properly grasping, focusing on, bearing in mind, and penetrating with "
             "wisdom the whole pattern of qualities encountered",
             "Avoiding all mental qualities entirely",
             "Only memorizing scripture"],
         "correct": 1,
         "expl": "A comprehensive analytical grasp, closing the list."},
    ],
    marginalia=[
        ("Seven qualities of attention", [
            "recognizing sluggishness,",
            "constriction, scattering &middot;",
            "watching feelings, perceptions, thoughts",
        ]),
        ("A specific analytical goal", [
            "paṭisambhidā —",
            "fourfold textual analysis,",
            "meaning, teaching, language, expression",
        ]),
        ("Recognition, not just avoidance", [
            "distorted states named",
            "and understood, not",
            "simply pushed away",
        ]),
        ("Cross-references", [
            "AN 7.39 &middot; next, this same list applied to Sāriputta specifically",
        ]),
    ],
    further=[
        '<a href="%s/an7.38/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.37.html">AN 7.37 &middot; A Friend (2nd)</a> &mdash; previous, '
        "closing this chapter's two discourses on friendship.",
        '<a href="an-7.39.html">AN 7.39 &middot; Textual Analysis (2nd)</a> &mdash; next, '
        "this same list applied to Sāriputta specifically.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.39 — Dutiyapaṭisambhidāsutta
# --------------------------------------------------------------------------- #
page(
    39, "Dutiyapaṭisambhidā", "Textual Analysis (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 7.39 — Textual Analysis (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyapaṭisambhidāsutta, restating AN 7.38's identical seven qualities as "
        "Sāriputta's own personal attainment. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical seven-item list as AN 7.38, restated as one named "
                 "individual's personal attainment"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Naming a senior disciple's personal attainment of a "
                              "generally-taught quality recurs widely across the Chinese "
                              "Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the same content as "
                       "AN 7.38, made concrete through a specific named example"),
    ],
    why=(
        "AN 7.39 restates AN 7.38's identical seven qualities, but shifts from a general "
        "teaching addressed to mendicants to a specific claim about Venerable "
        "Sāriputta's own realization &mdash; the same analytical capacities named "
        "generally in the discourse before this one, now grounded in one named "
        "individual's demonstrated attainment."),
    guide=[
        ("The teaching in one sentence", [
            "Having the same seven qualities already named at AN 7.38, Sāriputta "
            "realized the four kinds of textual analysis and lives having achieved them "
            "with his own insight."]),
        ("Identical content, shifted from general to particular", [
            "Checked term by term, this discourse's seven qualities are the same "
            "recognizing sluggishness, constriction, scattering, and threefold "
            "observation of feelings, perceptions, and thoughts already given at AN "
            "7.38. The only change is grammatical: third-person singular past tense "
            "about Sāriputta, rather than a general present-tense teaching to "
            "mendicants."]),
        ("Sāriputta as a demonstrated case, not a new teaching", [
            "This discourse does not argue that Sāriputta's path to textual analysis "
            "differed from the general teaching; it instead offers him as confirmation "
            "that the general teaching actually works, grounding an abstract capacity in "
            "a concrete, already-attained example."]),
        ("A pattern repeated across this chapter", [
            "AN 7.40 and 7.41, immediately following, will repeat this exact "
            "general-teaching-then-Sāriputta-example structure for a different "
            "attainment: mastery of the mind through skill in immersion."]),
    ],
    terms=[
        ("Sāriputta",
         "one of the Buddha's chief disciples, named here as the concrete example of "
         "AN 7.38's general teaching successfully realized."),
        ("līnattaṁ cittassa, ajjhattaṁ saṅkhittaṁ, bahiddhā vikkhittaṁ",
         "the same three named distortions of attention already met at AN 7.38, "
         "restated here as qualities Sāriputta himself recognized."),
        ("vedanā, saññā, vitakka",
         "&ldquo;feelings, perceptions, thoughts&rdquo; &mdash; the same three objects "
         "of threefold observation already applied at AN 7.38."),
        ("sāmaṁ paccakkhāya",
         "&ldquo;with his own insight&rdquo; &mdash; the discourse's closing phrase, "
         "identical to AN 7.38's own closing claim, now applied specifically to "
         "Sāriputta."),
        ("paṭisambhidā",
         "&ldquo;textual analysis&rdquo; &mdash; the same fourfold attainment named at "
         "AN 7.38, here confirmed as something Sāriputta has actually realized."),
    ],
    text_intro=(
        "The discourse in full: the same seven qualities as AN 7.38, restated as "
        "Sāriputta's own attainment. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta's seven qualities"),
        ("p", "&sect;1", "an7.39:1.1-1.10"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 7.38's, checked term by "
              "term?",
         "opts": [
             "Entirely different content",
             "Identical seven qualities, shifted from a general teaching to a specific "
             "claim about Sāriputta's own realization",
             "Only half the items overlap",
             "This discourse names no qualities at all"],
         "correct": 1,
         "expl": "The same content, grounded in one named individual's attainment."},
        {"q": "What role does Sāriputta play in this discourse, according to the guide?",
         "opts": [
             "He rejects AN 7.38's teaching as incorrect",
             "He serves as a demonstrated case confirming AN 7.38's general teaching "
             "actually works, not a new or different teaching",
             "He teaches something entirely unrelated to AN 7.38",
             "He is only mentioned in passing, without further significance"],
         "correct": 1,
         "expl": "A concrete example grounding an abstract capacity."},
        {"q": "What pattern does this discourse establish, continued later in this "
              "chapter?",
         "opts": [
             "No further pattern follows",
             "AN 7.40 and 7.41 will repeat this same general-teaching-then-Sāriputta-"
             "example structure for a different attainment",
             "A return to the respect formula",
             "A shift to lay followers"],
         "correct": 1,
         "expl": "A structural device this chapter uses more than once."},
        {"q": "What three objects receive the identical threefold observation already met "
              "at AN 7.38?",
         "opts": [
             "Faith, energy, and wisdom",
             "Feelings, perceptions, and thoughts",
             "The Buddha, the teaching, the Saṅgha",
             "Body, speech, and mind"],
         "correct": 1,
         "expl": "The same three objects of experience already named in the general "
                 "teaching."},
        {"q": "Is a setting stated for AN 7.39?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.38 immediately before it."},
        {"q": "What is the only significant change between AN 7.38 and this discourse?",
         "opts": [
             "The entire content is different",
             "A grammatical shift from general present-tense teaching to third-person "
             "past tense about a specific named individual",
             "The number of qualities changes from seven to six",
             "The target attainment changes entirely"],
         "correct": 1,
         "expl": "The same content, differently grammatically framed."},
    ],
    marginalia=[
        ("The same seven qualities", [
            "recognizing sluggishness,",
            "constriction, scattering —",
            "identical to AN 7.38",
        ]),
        ("General teaching to example", [
            "AN 7.38: taught to",
            "mendicants generally —",
            "AN 7.39: Sāriputta's own case",
        ]),
        ("Confirmation, not new content", [
            "Sāriputta grounds",
            "the abstract teaching",
            "in a demonstrated attainment",
        ]),
        ("Cross-references", [
            "AN 7.38 &middot; previous, this discourse's identical general teaching",
            "AN 7.40/41 &middot; next, the same structure repeated for mastery of mind",
        ]),
    ],
    further=[
        '<a href="%s/an7.39/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.38.html">AN 7.38 &middot; Textual Analysis (1st)</a> &mdash; '
        "previous, this discourse's identical general teaching.",
        '<a href="an-7.40.html">AN 7.40 &middot; Mastery of the Mind (1st)</a> &mdash; '
        "next, the same general-teaching-then-example structure applied to immersion.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.40 — Paṭhamavasasutta
# --------------------------------------------------------------------------- #
page(
    40, "Paṭhamavasa", "Mastery of the Mind (1st)",
    vagga=VAGGA_4,
    meta_title="AN 7.40 — Mastery of the Mind (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamavasasutta, naming seven skills in immersion that let a mendicant master "
        "their own mind rather than be mastered by it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single seven-item list of immersion-related skills, stated once with "
                 "no reversal — the first of a brief/Sāriputta-example pair"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Skill across entering, remaining in, and emerging from "
                              "meditative absorption as a technical framework recurs "
                              "throughout the Chinese Āgamas' meditation instructions; "
                              "this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a dense technical "
                       "vocabulary of specific immersion-related skills"),
    ],
    why=(
        "AN 7.40 names seven skills specifically related to immersion &mdash; skilled at "
        "immersion generally, skilled in entering it, remaining in it, emerging from it, "
        "skilled in its positivity, its territory, and skilled in projecting a mind "
        "purified by it &mdash; that together let a mendicant master their own mind "
        "rather than be mastered by it."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant skilled at immersion, skilled in entering it, remaining in it, "
            "emerging from it, skilled in its positivity, its territory, and skilled in "
            "projecting a mind purified by it, masters their mind and is not mastered by "
            "it."]),
        ("An extension of AN 6.72's three immersion skills", [
            "AN 6.72 in the previous nipāta named three specific skills &mdash; entering, "
            "remaining in, emerging from immersion &mdash; as producing strength in "
            "immersion. This discourse names those same three skills as three of a "
            "larger seven, adding overall skill at immersion itself, plus skill in its "
            "positivity, territory, and purified projection."]),
        ("Mastering the mind, not merely developing immersion", [
            "The discourse's stated goal is broader than immersion for its own sake: "
            "&ldquo;masters their mind and is not mastered by it&rdquo; frames these "
            "seven skills as producing genuine control over one's own mental states, "
            "with immersion as the specific means rather than the final end in itself."]),
        ("Four new, more specialized skills beyond AN 6.72's three", [
            "Vasībhāva (overall mastery), abhirādhana (positivity or favorable "
            "development), gocara (the proper territory or range of immersion), and "
            "abhinīhāra (projecting a purified mind toward a chosen object) extend the "
            "three-skill core into a more comprehensive and specialized sevenfold "
            "mastery."]),
    ],
    terms=[
        ("samādhikusala",
         "&ldquo;skilled at immersion&rdquo; &mdash; the first, general item, before the "
         "list turns to more specific skills."),
        ("samāpattikusala, ṭhitikusala, vuṭṭhānakusala",
         "&ldquo;skilled in entering, remaining in, emerging from immersion&rdquo; "
         "&mdash; the same three skills already named at AN 6.72 in the previous nipāta, "
         "here forming three of seven rather than the entirety of the list."),
        ("abhirādhanākusala",
         "&ldquo;skilled in positivity for immersion&rdquo; &mdash; the fifth item, a "
         "term new to this discourse."),
        ("gocarakusala",
         "&ldquo;skilled in the territory of immersion&rdquo; &mdash; the sixth item, "
         "naming skill in immersion's proper range or scope."),
        ("abhinīhārakusala",
         "&ldquo;skilled in projecting the mind purified by immersion&rdquo; &mdash; the "
         "seventh and closing item."),
    ],
    text_intro=(
        "The discourse in full: seven skills in immersion that let a mendicant master "
        "their own mind. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven skills in immersion"),
        ("p", "&sect;1", "an7.40:1.1-1.4"),
    ],
    quiz=[
        {"q": "What three of this discourse's seven skills already appeared at AN 6.72 in "
              "the previous nipāta?",
         "opts": [
             "Skill in positivity, territory, and purified projection",
             "Skill in entering, remaining in, and emerging from immersion",
             "Skill at immersion generally, and two others",
             "None of the seven skills appeared before"],
         "correct": 1,
         "expl": "The same three skills AN 6.72 named as producing strength in "
                 "immersion."},
        {"q": "What is the discourse's stated goal, broader than immersion for its own "
              "sake?",
         "opts": [
             "Attaining the first absorption only",
             "Mastering one's own mind, rather than being mastered by it — immersion as "
             "the means, not the final end",
             "Achieving physical health",
             "Gaining a reputation as a skilled teacher"],
         "correct": 1,
         "expl": "Genuine control over mental states, with immersion as the specific "
                 "vehicle."},
        {"q": "What four skills does this discourse add beyond AN 6.72's three?",
         "opts": [
             "Faith, energy, mindfulness, and wisdom",
             "Overall skill at immersion, plus skill in its positivity, territory, and "
             "purified projection",
             "The four foundations of mindfulness",
             "Nothing further is added"],
         "correct": 1,
         "expl": "A more comprehensive and specialized sevenfold expansion."},
        {"q": "What does the discourse open a pair with, according to the guide?",
         "opts": [
             "No further discourse relates to this one",
             "AN 7.41, applying this identical list specifically to Sāriputta's own "
             "attainment",
             "A return to the respect formula",
             "A dispute among sectarians"],
         "correct": 1,
         "expl": "The same brief/Sāriputta-example pattern already met at AN 7.38/39."},
        {"q": "Is a setting stated for AN 7.40?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.39 immediately before it."},
        {"q": "What does <em>gocarakusala</em> mean?",
         "opts": [
             "Skilled in entering immersion",
             "Skilled in the territory of immersion",
             "Skilled at immersion generally",
             "Skilled in emerging from immersion"],
         "correct": 1,
         "expl": "The sixth item, naming skill in immersion's proper range."},
    ],
    marginalia=[
        ("Seven skills in immersion", [
            "overall skill &middot; entering,",
            "remaining, emerging &middot;",
            "positivity &middot; territory &middot; projection",
        ]),
        ("Extending AN 6.72's three", [
            "entering, remaining,",
            "emerging — now three",
            "of seven, not the whole list",
        ]),
        ("Mastery, not immersion alone", [
            "'masters their mind,",
            "not mastered by it' —",
            "immersion as means, not end",
        ]),
        ("Cross-references", [
            "AN 6.72 &middot; earlier nipāta, source of three of these seven skills",
            "AN 7.41 &middot; next, this same list applied to Sāriputta specifically",
        ]),
    ],
    further=[
        '<a href="%s/an7.40/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.72.html">AN 6.72 &middot; Strength</a> &mdash; earlier nipāta, '
        "source of three of these seven skills.",
        '<a href="an-7.41.html">AN 7.41 &middot; Mastery of the Mind (2nd)</a> &mdash; '
        "next, this same list applied to Sāriputta specifically.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.41 — Dutiyavasasutta
# --------------------------------------------------------------------------- #
page(
    41, "Dutiyavasa", "Mastery of the Mind (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 7.41 — Mastery of the Mind (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyavasasutta, restating AN 7.40's identical seven skills as Sāriputta's own "
        "personal mastery of mind. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical seven-item list as AN 7.40, restated as Sāriputta's own "
                 "personal attainment — matching AN 7.38/39's exact structural pattern"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Naming Sāriputta specifically as an exemplar of "
                              "meditative mastery recurs across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the same content as "
                       "AN 7.40, grounded in one named individual's attainment"),
    ],
    why=(
        "AN 7.41 completes this chapter's second general-teaching-then-Sāriputta-"
        "example pair, restating AN 7.40's identical seven immersion skills as "
        "Sāriputta's own demonstrated mastery &mdash; the same structural move already "
        "made once before at AN 7.38/39 for textual analysis, now repeated for mastery "
        "of the mind."),
    guide=[
        ("The teaching in one sentence", [
            "Having the same seven immersion skills already named at AN 7.40, Sāriputta "
            "has mastered his mind and is not mastered by it."]),
        ("A structural echo of AN 7.38/39, now for a different attainment", [
            "Checked side by side, this discourse and AN 7.38/39 share an identical "
            "compositional move: a general teaching to mendicants, followed immediately "
            "by the identical content restated as Sāriputta's own personal case, marking "
            "this as a deliberate pattern in how this chapter presents its content rather "
            "than a coincidence."]),
        ("Two attainments, one exemplar", [
            "Sāriputta now stands, within this single chapter, as the demonstrated "
            "example for two distinct attainments: the four kinds of textual analysis "
            "(AN 7.39) and mastery of the mind through immersion (this discourse) "
            "&mdash; a double role underscoring his standing as the paradigmatic senior "
            "disciple in this literature."]),
        ("Closing this chapter's paired-example discourses", [
            "With this discourse, this chapter's two general-teaching-then-example pairs "
            "(AN 7.38/39 and AN 7.40/41) are complete; AN 7.42 and 7.43, immediately "
            "following, will use named individuals differently &mdash; not as confirming "
            "examples of an already-stated teaching, but as questioners prompting a "
            "teaching not yet given."]),
    ],
    terms=[
        ("Sāriputta",
         "the same chief disciple already named at AN 7.39, here demonstrating a second "
         "distinct attainment within this chapter."),
        ("samādhikusala, samāpattikusala, ṭhitikusala, vuṭṭhānakusala",
         "the same first four skills already named at AN 7.40: skilled at immersion "
         "generally, and skilled in entering, remaining in, and emerging from it."),
        ("abhirādhanākusala, gocarakusala, abhinīhārakusala",
         "the same remaining three skills already named at AN 7.40: skilled in "
         "positivity, territory, and purified projection."),
        ("cittaṁ vasaṁ vatteti, na ca cittassa vasena vattati",
         "&ldquo;masters his mind and is not mastered by it&rdquo; &mdash; the "
         "discourse's closing claim, identical to AN 7.40's stated goal, now confirmed "
         "in Sāriputta's own case."),
        ("vasa",
         "&ldquo;mastery&rdquo; &mdash; this discourse's own title term, shared with AN "
         "7.40."),
    ],
    text_intro=(
        "The discourse in full: the same seven skills as AN 7.40, restated as "
        "Sāriputta's own mastery of mind. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta's seven skills"),
        ("p", "&sect;1", "an7.41:1.1-1.4"),
    ],
    quiz=[
        {"q": "What structural move does this discourse share with AN 7.38/39, according "
              "to the guide?",
         "opts": [
             "No relationship at all",
             "A general teaching followed immediately by the identical content restated "
             "as Sāriputta's own personal case — a deliberate pattern, not a coincidence",
             "Both discourses reject the general teaching",
             "Both discourses concern entirely different attainments with no shared "
             "structure"],
         "correct": 1,
         "expl": "The same compositional device used twice within this chapter."},
        {"q": "What two distinct attainments does Sāriputta demonstrate within this single "
              "chapter?",
         "opts": [
             "Only mastery of the mind",
             "The four kinds of textual analysis (AN 7.39) and mastery of the mind "
             "through immersion (this discourse)",
             "Only textual analysis",
             "Neither attainment is actually his own"],
         "correct": 1,
         "expl": "A double role underscoring his standing as the paradigmatic senior "
                 "disciple."},
        {"q": "What does this discourse complete, according to the guide?",
         "opts": [
             "Nothing further — an isolated teaching",
             "This chapter's two general-teaching-then-example pairs (AN 7.38/39 and AN "
             "7.40/41)",
             "The entire chapter",
             "The entire Sevens collection"],
         "correct": 1,
         "expl": "The second of two matched pairs using this identical structure."},
        {"q": "How will AN 7.42 and 7.43 use named individuals differently, according to "
              "the guide?",
         "opts": [
             "Identically to this discourse's pattern",
             "Not as confirming examples of an already-stated teaching, but as "
             "questioners prompting a teaching not yet given",
             "Named individuals do not appear in AN 7.42/43 at all",
             "As deities rather than mendicants"],
         "correct": 1,
         "expl": "A shift in how named individuals function within this chapter's "
                 "remaining discourses."},
        {"q": "Is a setting stated for AN 7.41?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, following AN 7.40 immediately before it."},
        {"q": "What does this discourse's closing claim state about Sāriputta?",
         "opts": [
             "That he has failed to master his mind",
             "That he masters his mind and is not mastered by it, identical to AN 7.40's "
             "stated goal",
             "That he has abandoned immersion practice",
             "Nothing specific is claimed about him"],
         "correct": 1,
         "expl": "The general teaching's goal, confirmed in one named individual's case."},
    ],
    marginalia=[
        ("The same seven skills", [
            "overall skill &middot; entering,",
            "remaining, emerging &middot;",
            "positivity, territory, projection",
        ]),
        ("Sāriputta's double role", [
            "textual analysis (7.39)",
            "and mastery of mind (7.41) —",
            "the paradigmatic disciple",
        ]),
        ("Closing two matched pairs", [
            "AN 7.38/39 and",
            "AN 7.40/41 — the same",
            "general-teaching-then-example device",
        ]),
        ("Cross-references", [
            "AN 7.40 &middot; previous, this discourse's identical general teaching",
            "AN 7.39 &middot; earlier, Sāriputta's other attainment within this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an7.41/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.40.html">AN 7.40 &middot; Mastery of the Mind (1st)</a> &mdash; '
        "previous, this discourse's identical general teaching.",
        '<a href="an-7.39.html">AN 7.39 &middot; Textual Analysis (2nd)</a> &mdash; '
        "earlier, Sāriputta's other attainment within this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.42 — Paṭhamaniddasasutta
# --------------------------------------------------------------------------- #
page(
    42, "Paṭhamaniddasa", "Graduation (1st)",
    vagga=VAGGA_4,
    meta_title="AN 7.42 — Graduation (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaniddasasutta, in which Sāriputta questions a sectarian claim about a "
        "twelve-year rule for graduation, and the Buddha rejects it in favor of "
        "AN 7.20's seven qualifications. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove; Sāriputta first visits a sectarian "
                    "hermitage before returning to question the Buddha"),
        ("Speakers", "Wanderers of other religions (reported), Venerable Sāriputta, and "
                     "the Buddha"),
        ("Form", "A narrated visit to a rival hermitage, a deliberately withheld "
                 "reaction, and a direct question brought back to the Buddha for "
                 "resolution"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Debates over whether spiritual attainment can be measured "
                              "by years of practice recur across the Chinese Āgamas' "
                              "polemic against rival ascetic traditions; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a narrative discourse "
                       "rejecting a fixed-year rule in favor of content already given in "
                       "full at AN 7.20"),
    ],
    why=(
        "AN 7.42 stages a direct confrontation between two accounts of spiritual "
        "maturity: wanderers of other religions claim that anyone who lives the "
        "spiritual life a full twelve years is qualified to be called a "
        "&ldquo;graduate.&rdquo; Sāriputta, hearing this, neither approves nor "
        "disputes it on the spot, but brings the question directly to the Buddha, who "
        "rejects the premise outright and restates the seven qualifications for "
        "graduation already given in full at AN 7.20."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant cannot be called a &ldquo;graduate&rdquo; solely for having "
            "completed a fixed number of years; the same seven qualifications for "
            "graduation already given at AN 7.20 are what actually qualify someone, "
            "whether that takes twelve, twenty-four, thirty-six, or forty-eight years."]),
        ("Deliberate restraint before an outside claim", [
            "Sāriputta's response to the wanderers' twelve-year rule is notably "
            "careful: he &ldquo;neither approved nor rejected&rdquo; the statement on "
            "the spot, choosing instead to verify it against the Buddha's own teaching "
            "before forming a judgment &mdash; a model of not reacting to an unfamiliar "
            "claim until its source has been properly checked."]),
        ("The Buddha's answer reuses AN 7.20's content exactly", [
            "Checked term by term, the seven qualifications the Buddha gives here are "
            "identical to AN 7.20's own list: keen enthusiasm sustained toward the "
            "training, examining the teachings, getting rid of desires, retreat, "
            "energy, mindfulness and alertness, and theoretical penetration, each "
            "qualified by not losing that enthusiasm in the future."]),
        ("Years as a possible outcome, never the qualifying cause", [
            "The Buddha's closing lines name several possible durations &mdash; twelve, "
            "twenty-four, thirty-six, or forty-eight years &mdash; explicitly as "
            "however long graduation might in fact take for a given individual, not as "
            "a fixed threshold anyone automatically crosses. Duration becomes a "
            "consequence of these seven qualities' presence, not their substitute."]),
    ],
    terms=[
        ("aññatitthiyā paribbājakā",
         "&ldquo;wanderers of other religions&rdquo; &mdash; the rival ascetic "
         "practitioners whose fixed-year claim Sāriputta hears and questions."),
        ("dvādasavassāni",
         "&ldquo;twelve years&rdquo; &mdash; the wanderers' claimed threshold for "
         "graduate status, rejected as a sufficient criterion on its own."),
        ("niddasavatthu",
         "&ldquo;qualifications for graduation&rdquo; &mdash; this discourse's own "
         "central term, identical to AN 7.20's, naming actual criteria rather than "
         "elapsed time."),
        ("sāmaṁ paccakkhāya",
         "&ldquo;after realizing them with my own insight&rdquo; &mdash; the Buddha's "
         "own stated basis for these seven qualifications, distinguishing them from an "
         "arbitrary convention like a fixed year-count."),
        ("dvādasa vā vassāni catucattārīsaṁ vā vassāni",
         "&ldquo;twelve years... or forty-eight years&rdquo; &mdash; the range of "
         "durations the Buddha names as possible outcomes, never as the qualifying "
         "cause itself."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta's visit to a sectarian hermitage, his question "
        "to the Buddha, and the Buddha's rejection of a fixed-year rule. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta hears the wanderers' claim"),
        ("p", "&sect;1", "an7.42:1.1-2.4"),
        ("h3", "Sāriputta questions the Buddha"),
        ("p", "&sect;2", "an7.42:3.1-4.2"),
        ("h3", "The Buddha's answer: seven qualifications, not a fixed year-count"),
        ("p", "&sect;3", "an7.42:5.1-5.6"),
    ],
    quiz=[
        {"q": "What claim do the wanderers of other religions make, that Sāriputta hears "
              "at their hermitage?",
         "opts": [
             "That no one can ever become a graduate",
             "That anyone who lives the spiritual life a full twelve years is qualified "
             "to be called a 'graduate'",
             "That only the Buddha himself can graduate",
             "That graduation requires exactly one hundred years"],
         "correct": 1,
         "expl": "A fixed-duration criterion the Buddha will go on to reject."},
        {"q": "How does Sāriputta respond to this claim on the spot, according to the "
              "guide?",
         "opts": [
             "He immediately agrees with it",
             "He neither approves nor rejects it, choosing to verify it against the "
             "Buddha's own teaching before forming a judgment",
             "He immediately and publicly refutes it",
             "He ignores the wanderers entirely and leaves without a word"],
         "correct": 1,
         "expl": "Deliberate restraint before an unfamiliar claim, verified rather than "
                 "reacted to."},
        {"q": "How does the Buddha's answer compare to AN 7.20's content, checked term by "
              "term?",
         "opts": [
             "Entirely different qualifications",
             "Identical — the same seven qualifications for graduation already given in "
             "full at AN 7.20",
             "Only three of seven items overlap",
             "The Buddha refuses to answer the question at all"],
         "correct": 1,
         "expl": "Content this series has already met once before, reused here to "
                 "answer a direct challenge."},
        {"q": "What role do the specific year-counts (twelve, twenty-four, thirty-six, "
              "forty-eight) play in the Buddha's answer, according to the guide?",
         "opts": [
             "They are the actual qualifying criteria",
             "Possible outcomes or durations, never the qualifying cause itself — a "
             "consequence of the seven qualities' presence, not their substitute",
             "They are dismissed as entirely irrelevant",
             "They apply only to lay followers"],
         "correct": 1,
         "expl": "Duration as a possible consequence, not a threshold anyone "
                 "automatically crosses."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kosambī, at Ghosita's Monastery",
             "Sāvatthī, in Jeta's Grove",
             "Vesālī, at the Sārandada Shrine",
             "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "This book's standard opening setting, distinct from AN 7.43's Kosambī "
                 "setting."},
        {"q": "What does <em>niddasavatthu</em> mean, and where else has it appeared in "
              "this book?",
         "opts": [
             "'Fixed duration' — a new term for this discourse",
             "'Qualifications for graduation' — the same term and content already given "
             "in full at AN 7.20",
             "A term unrelated to graduation",
             "'Sectarian claim' — describing only the wanderers' position"],
         "correct": 1,
         "expl": "This discourse's central term, reused word for word from AN 7.20."},
    ],
    marginalia=[
        ("A rival claim challenged", [
            "'twelve years qualifies",
            "anyone as a graduate' —",
            "the wanderers' fixed rule",
        ]),
        ("Restraint, then verification", [
            "Sāriputta neither",
            "approves nor rejects —",
            "checks with the Buddha first",
        ]),
        ("AN 7.20's content, reused", [
            "the same seven",
            "qualifications, now",
            "answering a direct challenge",
        ]),
        ("Cross-references", [
            "AN 7.20 &middot; earlier, this discourse's seven qualifications given in "
            "full",
            "AN 7.43 &middot; next, the same narrative structure, different content",
        ]),
    ],
    further=[
        '<a href="%s/an7.42/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.20.html">AN 7.20 &middot; Qualifications for Graduation</a> '
        "&mdash; earlier, this discourse's seven qualifications given in full.",
        '<a href="an-7.43.html">AN 7.43 &middot; Graduation (2nd)</a> &mdash; next, the '
        "same narrative structure with a genuinely different answer.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.43 — Dutiyaniddasasutta
# --------------------------------------------------------------------------- #
page(
    43, "Dutiyaniddasa", "Graduation (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 7.43 — Graduation (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaniddasasutta, closing this chapter as Ānanda repeats Sāriputta's "
        "question, but the Buddha answers with AN 7.25's seven qualities rather than AN "
        "7.20's list. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kosambī, at Ghosita's Monastery; Ānanda visits a sectarian "
                    "hermitage before returning to question the Buddha, echoing AN "
                    "7.42's narrative but in a different city"),
        ("Speakers", "Wanderers of other religions (reported), Venerable Ānanda, and the "
                     "Buddha"),
        ("Form", "The identical narrative structure as AN 7.42, with a different named "
                 "questioner, setting, and closing answer"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The repetition of a narrative structure with two "
                              "different senior disciples recurs across the Chinese "
                              "Āgamas' treatment of the same underlying question; this "
                              "reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the same narrative "
                       "shape as AN 7.42, worth checking whether the Buddha's actual "
                       "answer is identical or genuinely different"),
    ],
    why=(
        "AN 7.43 closes this chapter with a narrative matching AN 7.42's shape almost "
        "exactly &mdash; a senior disciple visits a sectarian hermitage, hears the same "
        "twelve-year claim, brings it to the Buddha &mdash; but checked term by term, "
        "the Buddha's actual answer here is not AN 7.42's seven qualifications from AN "
        "7.20. It is instead the seven personal qualities already met at AN 7.25: "
        "faithful, conscientious, prudent, learned, energetic, mindful, and wise."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant cannot be called a &ldquo;graduate&rdquo; solely for having "
            "completed a fixed number of years; being faithful, conscientious, "
            "prudent, learned, energetic, mindful, and wise is what actually "
            "qualifies someone, whether that takes twelve, twenty-four, thirty-six, or "
            "forty-eight years."]),
        ("The same frame, a genuinely different answer", [
            "Ānanda's visit to Ghosita's Monastery at Kosambī, his restraint before the "
            "wanderers' claim, and his question to the Buddha all mirror AN 7.42's "
            "structure precisely. What changes is the Buddha's actual answer: not the "
            "niddasavatthu list reused from AN 7.20, but the personal-quality list "
            "already met at AN 7.25 &mdash; a shared narrative shell around two "
            "genuinely different specific teachings."]),
        ("Two disciples, two settings, two answers", [
            "AN 7.42 features Sāriputta at Sāvatthī, answered with AN 7.20's content; "
            "this discourse features Ānanda at Kosambī, answered with AN 7.25's content "
            "&mdash; a matched pair distinguished by disciple, city, and answer alike, "
            "not merely a single detail changed."]),
        ("Closing this chapter, and this book's opening structural device", [
            "This discourse closes Devatāvagga on the same note AN 7.42 opened it with: "
            "a rejection of counting years as a substitute for actual qualities, "
            "restated with a second complete list, confirming that this book's several "
            "sevenfold formulas for graduation, wealth, power, and non-decline all "
            "circle back to closely related clusters of the same underlying virtues."]),
    ],
    terms=[
        ("Ānanda",
         "the Buddha's attendant, here playing the role Sāriputta played at AN 7.42, "
         "questioning the same sectarian claim in a different city."),
        ("Kosambī, Ghositārāma",
         "&ldquo;Kosambī, Ghosita's Monastery&rdquo; &mdash; this discourse's setting, "
         "distinct from AN 7.42's Sāvatthī."),
        ("saddha, hirimā, ottappī, bahussuta, āraddhavīriya, satimā, paññavā",
         "&ldquo;faithful, conscientious, prudent, learned, energetic, mindful, "
         "wise&rdquo; &mdash; the seven qualities the Buddha names here, identical to "
         "AN 7.25's own list rather than AN 7.42's niddasavatthu."),
        ("niddasavatthu",
         "&ldquo;qualifications for graduation&rdquo; &mdash; AN 7.42's own answer, "
         "notably absent from this discourse despite the shared narrative frame."),
        ("dvādasa vā vassāni... catucattārīsaṁ vā vassāni",
         "the same range of possible durations already named at AN 7.42, closing this "
         "discourse identically despite its different specific answer."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's visit to a sectarian hermitage, his question to "
        "the Buddha, and the Buddha's answer, drawing on a different seven-item list "
        "than AN 7.42's. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and Ānanda hears the wanderers' claim"),
        ("p", "&sect;1", "an7.43:1.1-2.2"),
        ("h3", "Ānanda questions the Buddha"),
        ("p", "&sect;2", "an7.43:3.1-6.2"),
        ("h3", "The Buddha's answer: seven qualities, not a fixed year-count"),
        ("p", "&sect;3", "an7.43:7.1-8.3"),
    ],
    quiz=[
        {"q": "How does this discourse's narrative shape compare to AN 7.42's?",
         "opts": [
             "Entirely different narrative",
             "Nearly identical — a senior disciple visits a sectarian hermitage, hears "
             "the same twelve-year claim, and brings it to the Buddha",
             "This discourse has no narrative frame at all",
             "The two discourses share no similarity whatsoever"],
         "correct": 1,
         "expl": "The same structural shell, with several specific details changed."},
        {"q": "What seven qualities does the Buddha actually name here, checked against "
              "AN 7.42's answer?",
         "opts": [
             "The identical niddasavatthu list from AN 7.20, reused word for word",
             "A genuinely different list — faithful, conscientious, prudent, learned, "
             "energetic, mindful, and wise — matching AN 7.25 instead",
             "No specific qualities are named at all",
             "The five spiritual faculties only"],
         "correct": 1,
         "expl": "A different specific teaching despite the shared narrative frame."},
        {"q": "What details distinguish this discourse from AN 7.42 beyond the Buddha's "
              "answer, according to the guide?",
         "opts": [
             "Nothing else differs",
             "The named disciple (Ānanda rather than Sāriputta) and the setting (Kosambī "
             "rather than Sāvatthī)",
             "Only the setting differs; the disciple is identical",
             "Only the disciple differs; the setting is identical"],
         "correct": 1,
         "expl": "A matched pair differing in disciple, city, and answer together."},
        {"q": "What does the guide say this discourse confirms about this book's several "
              "sevenfold formulas?",
         "opts": [
             "That they are all entirely unrelated to each other",
             "That formulas for graduation, wealth, power, and non-decline circle back "
             "to closely related clusters of the same underlying virtues",
             "That only one sevenfold formula is ever actually valid",
             "That this book contains no repeated themes at all"],
         "correct": 1,
         "expl": "A closing note connecting this chapter to this book's recurring "
                 "vocabulary of virtues."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Kosambī, at Ghosita's Monastery", "Vesālī, at the Sārandada Shrine", "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "A setting distinct from AN 7.42's Sāvatthī, in a discourse otherwise "
                 "matching its structure."},
        {"q": "What earlier discourse's content does the Buddha's answer here match "
              "exactly?",
         "opts": ["AN 7.20", "AN 7.25", "AN 7.5", "AN 7.36"],
         "correct": 1,
         "expl": "The seven personal qualities already given at AN 7.25 earlier in this "
                 "book."},
    ],
    marginalia=[
        ("The same challenge, again", [
            "Ānanda hears the",
            "wanderers' twelve-year",
            "claim, at Kosambī this time",
        ]),
        ("A different answer", [
            "not AN 7.20's list —",
            "AN 7.25's seven",
            "personal qualities instead",
        ]),
        ("A matched pair, three changes", [
            "different disciple,",
            "different city,",
            "different specific answer",
        ]),
        ("Cross-references", [
            "AN 7.42 &middot; previous, this discourse's near-identical narrative "
            "companion",
            "AN 7.25 &middot; earlier, source of this discourse's actual seven "
            "qualities",
        ]),
    ],
    further=[
        '<a href="%s/an7.43/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.42.html">AN 7.42 &middot; Graduation (1st)</a> &mdash; previous, '
        "this discourse's near-identical narrative companion.",
        '<a href="an-7.25.html">AN 7.25 &middot; Non-Decline for Mendicants (3rd)</a> '
        "&mdash; earlier, source of this discourse's actual seven qualities.",
    ],
)


# --------------------------------------------------------------------------- #
# The chapter's own title, Mahāyaññavagga ("A Great Sacrifice"), names AN
# 7.47's narrative rather than describing the chapter's actual span: only one
# discourse here involves a sacrifice. This chapter closes AN 7's First Fifty
# (Paṭhamapaṇṇāsaka, AN 7.1-53); the Second Fifty has not yet been mapped.
# --------------------------------------------------------------------------- #
VAGGA_5 = "<em>Mahāyaññavagga</em> &mdash; the fifth chapter of the Sevens, closing its First Fifty"


# --------------------------------------------------------------------------- #
# AN 7.44 — Sattaviññāṇaṭṭhitisutta
# --------------------------------------------------------------------------- #
page(
    44, "Sattaviññāṇaṭṭhiti", "Planes of Consciousness",
    vagga=VAGGA_5,
    meta_title="AN 7.44 — Planes of Consciousness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sattaviññāṇaṭṭhitisutta, the Buddha's bare list of seven planes of "
        "consciousness spanning the human realm up to the dimension of nothingness. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare doctrinal list, seven planes each defined by a pair of "
                 "terms &mdash; diversity or unity of body, diversity or unity of "
                 "perception &mdash; followed by three formless attainments"),
        ("Length", "~1 minute to read"),
        ("Wider canon", "The same seven planes reappear, folded into a larger list of "
                        "nine abodes of beings (navasattāvāsā), at DN 15 and DN 33; "
                        "this discourse gives only the seven that Ru-Yi's reading guide "
                        "for those texts would need on its own"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short but dense, "
                       "a cosmological map best read slowly, one plane at a time"),
    ],
    why=(
        "AN 7.44 opens this chapter with a cosmological map: seven planes of "
        "consciousness, sorted by whether the beings there share one body-type or many, "
        "one mode of perception or many, climbing from the human realm through three "
        "levels tied to the four absorptions and on to three of the four formless "
        "attainments."),
    guide=[
        ("The teaching in one sentence", [
            "Consciousness &mdash; not consciousness in general, but the specific "
            "settled conditions in which beings are reborn &mdash; sorts into seven "
            "planes, each named by whether its beings' bodies are diverse or uniform "
            "and whether their perceptions are diverse or uniform."]),
        ("The first four planes: body and perception, crossed two ways", [
            "The first plane covers beings diverse in both body and perception "
            "&mdash; humans, some gods, and some beings in the lower realms, the "
            "widest and most familiar plane. The second plane, diverse body but "
            "unified perception, names the gods of the Divinity's host reborn there "
            "through the first absorption. The third, unified body but diverse "
            "perception, names the gods of streaming radiance. The fourth, unified in "
            "both, names the gods of universal beauty &mdash; each pairing worked "
            "through systematically rather than left to the reader to infer."]),
        ("The last three planes: beyond form entirely", [
            "The fifth through seventh planes leave body out of the reckoning "
            "altogether, since these beings have gone totally beyond perceptions of "
            "form: the dimension of infinite space, the dimension of infinite "
            "consciousness, and the dimension of nothingness &mdash; three of the four "
            "formless attainments, each defined by what perception it has moved "
            "beyond rather than by any bodily comparison."]),
        ("What this list leaves out, and why it matters", [
            "The fuller doctrinal picture found elsewhere in the canon (DN 15, DN 33) "
            "adds two more abodes to make nine: non-percipient beings, who have no "
            "consciousness at all and so cannot count as a plane of consciousness by "
            "definition, and the dimension of neither perception nor non-perception, "
            "too subtle for even this fine-grained classification to pin down as "
            "clearly one thing or its opposite. This discourse's seven are exactly the "
            "planes that classification of this kind can actually reach."]),
    ],
    terms=[
        ("viññāṇaṭṭhiti",
         "&ldquo;plane&rdquo; or &ldquo;station&rdquo; of consciousness &mdash; a "
         "settled condition of rebirth classified by the character of body and "
         "perception shared there, not consciousness as a faculty in general."),
        ("nānattakāyā nānattasaññino",
         "&ldquo;diverse in body, diverse in perception&rdquo; &mdash; the first "
         "plane's defining pair, covering humans and much of the god and lower "
         "realms at once."),
        ("ekattakāyā ekattasaññino",
         "&ldquo;unified in body, unified in perception&rdquo; &mdash; the fourth "
         "plane, the gods of universal beauty (subhakiṇha), reborn through the third "
         "absorption."),
        ("ākāsānañcāyatana, viññāṇañcāyatana, ākiñcaññāyatana",
         "&ldquo;the dimension of infinite space, of infinite consciousness, of "
         "nothingness&rdquo; &mdash; the fifth through seventh planes, three of the "
         "four formless attainments named in sequence."),
        ("navasattāvāsā",
         "&ldquo;the nine abodes of beings&rdquo; &mdash; the larger classification "
         "at DN 15 and DN 33 that folds these seven planes in alongside two further "
         "abodes this discourse does not include."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's bare enumeration of the seven planes, "
        "with no dialogue frame. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven planes, announced"),
        ("p", "&sect;1", "an7.44:1.1-1.2"),
        ("h3", "Planes one through four: body and perception crossed two ways"),
        ("p", "&sect;2", "an7.44:1.3-4.2"),
        ("h3", "Planes five through seven: beyond form, into the formless"),
        ("p", "&sect;3", "an7.44:5.1-8.1"),
    ],
    quiz=[
        {"q": "What does this discourse classify as “planes of consciousness”?",
         "opts": [
             "Different types of meditation technique",
             "Settled conditions of rebirth, classified by whether beings there share "
             "one body-type or many, and one mode of perception or many",
             "The seven factors of awakening",
             "Seven stages of a single meditator's progress in one lifetime"],
         "correct": 1,
         "expl": "A cosmological classification of rebirth, not a meditation method."},
        {"q": "What defines the first, widest plane of consciousness?",
         "opts": [
             "Unified body, unified perception",
             "Diverse in body and diverse in perception — covering humans, some gods, "
             "and some beings in the lower realms at once",
             "Beings who have gone totally beyond perceptions of form",
             "Non-percipient beings with no consciousness at all"],
         "correct": 1,
         "expl": "The broadest plane, spanning much of the human, divine, and lower "
                 "realms together."},
        {"q": "What do the fifth through seventh planes have in common?",
         "opts": [
             "They are all named by comparing bodies",
             "They leave body out of the reckoning entirely, being three of the four "
             "formless attainments — infinite space, infinite consciousness, and "
             "nothingness",
             "They are all planes reached only through the first absorption",
             "They are identical to the first four planes"],
         "correct": 1,
         "expl": "Formless attainments defined by what perception has been left "
                 "behind, not by any bodily comparison."},
        {"q": "According to the guide, what does the fuller nine-abode list at DN 15 "
              "and DN 33 add that this discourse's seven leave out?",
         "opts": [
             "Nothing — the lists are identical",
             "Non-percipient beings, who have no consciousness at all, and the "
             "dimension of neither perception nor non-perception, too subtle to "
             "classify this way",
             "Three more formless attainments not mentioned here",
             "A tenth and eleventh plane of consciousness"],
         "correct": 1,
         "expl": "Two further abodes that fall outside what this particular "
                 "classification can pin down."},
        {"q": "Which gods does the guide name for the fourth plane, unified in both "
              "body and perception?",
         "opts": [
             "The gods of streaming radiance",
             "The gods of universal beauty, reborn through the third absorption",
             "The gods of the Divinity's host",
             "The gods of the Four Great Kings"],
         "correct": 1,
         "expl": "Subhakiṇha devas, the fourth plane's named example."},
        {"q": "How is this discourse delivered?",
         "opts": [
             "As a dialogue with a brahmin visitor",
             "As a bare doctrinal list, with no dialogue frame or narrative setting "
             "given",
             "As a story about a laywoman's attainments",
             "As a set of verses"],
         "correct": 1,
         "expl": "Direct address to the mendicants, opening this chapter without "
                 "narrative framing."},
    ],
    marginalia=[
        ("Seven planes, sorted", [
            "by diversity or unity",
            "of body, and of",
            "perception, in turn",
        ]),
        ("Four bodily, three formless", [
            "planes one through four span",
            "the four absorptions;",
            "five through seven leave form behind",
        ]),
        ("A map, not the whole map", [
            "two abodes elsewhere",
            "in the canon sit outside",
            "what this list reaches",
        ]),
        ("Cross-references", [
            "AN 6.142 &middot; earlier, the six perceptions building toward direct "
            "knowledge of greed",
            "DN 15, DN 33 &middot; outside this project, the fuller nine-abode "
            "classification",
        ]),
    ],
    further=[
        '<a href="%s/an7.44/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.142.html">AN 6.142 &middot; Direct Knowledge of Greed by Means '
        "of Perception</a> &mdash; earlier, this project's most recent extended "
        "treatment of a saññā list.",
        '<a href="an-7.43.html">AN 7.43 &middot; Graduation (2nd)</a> &mdash; closing '
        "the previous chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.45 — Samādhiparikkhārasutta
# --------------------------------------------------------------------------- #
page(
    45, "Samādhiparikkhāra", "Prerequisites for Immersion",
    vagga=VAGGA_5,
    meta_title="AN 7.45 — Prerequisites for Immersion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Samādhiparikkhārasutta, naming the noble eightfold path's first seven "
        "factors as the prerequisites that make right immersion itself possible. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single-sentence doctrinal definition, naming seven factors and "
                 "then defining what unifying the mind around them is called"),
        ("Length", "under 1 minute to read"),
        ("Wider canon", "The same definition of right immersion &ldquo;with its "
                        "vital conditions&rdquo; and &ldquo;with its "
                        "prerequisites&rdquo; recurs at MN 117, where it anchors that "
                        "discourse's account of the noble eightfold path as two "
                        "distinct tiers, mundane and transcendent"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief and "
                       "formulaic, worth reading against the eightfold path rather "
                       "than in isolation"),
    ],
    why=(
        "AN 7.45 takes the noble eightfold path's first seven factors &mdash; every "
        "one of them except right immersion itself &mdash; and names them as that "
        "path's own prerequisites: unifying the mind around all seven together is "
        "what &ldquo;noble right immersion&rdquo; actually means."),
    guide=[
        ("The teaching in one sentence", [
            "Right immersion is not a factor that stands alone; it is what results "
            "when a mind is unified around the other seven path factors together "
            "&mdash; right view, purpose, speech, action, livelihood, effort, and "
            "mindfulness &mdash; taken as its prerequisites."]),
        ("Seven factors, one list, no new content", [
            "The seven named here are not a new formula: they are the noble "
            "eightfold path itself, minus its own eighth factor. This discourse's "
            "entire content is the claim that these seven, taken together as "
            "conditions, are what right immersion is unified around &mdash; nothing "
            "is added to the path's usual eight factors, only a claim about how the "
            "eighth depends on the other seven."]),
        ("&ldquo;With its vital conditions&rdquo; and &ldquo;with its "
         "prerequisites&rdquo;", [
            "The discourse closes by giving this unification two names at once: "
            "noble right immersion &ldquo;with its vital condition&rdquo; "
            "(saupaniso) and &ldquo;with its prerequisite&rdquo; (saparikkhāro). "
            "Both phrases point to the same claim &mdash; that immersion of this "
            "kind cannot be isolated from the ethical and cognitive factors that "
            "precede and support it."]),
        ("Why this matters for how immersion is practiced", [
            "Read against the wider path, this discourse pushes back against "
            "treating meditative immersion as a free-standing technique separable "
            "from view, speech, action, and livelihood. The claim is structural: "
            "immersion that is genuinely noble is, by definition, immersion built on "
            "these seven conditions, not immersion achieved despite their absence."]),
    ],
    terms=[
        ("samādhiparikkhārā",
         "&ldquo;prerequisites for immersion&rdquo; &mdash; this discourse's own "
         "title, naming what the seven factors are called in relation to right "
         "immersion."),
        ("sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, sammāājīvo, "
         "sammāvāyāmo, sammāsati",
         "&ldquo;right view, right purpose, right speech, right action, right "
         "livelihood, right effort, right mindfulness&rdquo; &mdash; the noble "
         "eightfold path's first seven factors, named here as a set."),
        ("cittassekaggatā",
         "&ldquo;unification of mind&rdquo; &mdash; the discourse's own definition "
         "of what results when these seven factors converge as its prerequisites."),
        ("saupaniso, saparikkhāro",
         "&ldquo;with its vital condition&rdquo;, &ldquo;with its "
         "prerequisite&rdquo; &mdash; the two names this discourse gives to noble "
         "right immersion once its supporting seven factors are counted in."),
        ("ariyo sammāsamādhi",
         "&ldquo;noble right immersion&rdquo; &mdash; the eighth path factor, whose "
         "full definition this short discourse supplies by naming what precedes it."),
    ],
    text_intro=(
        "The discourse in full, a single compact definition. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven prerequisites, and what their unification is called"),
        ("p", "&sect;1", "an7.45:1.1-1.4"),
    ],
    quiz=[
        {"q": "What seven factors does this discourse name as prerequisites for "
              "immersion?",
         "opts": [
             "The seven factors of awakening",
             "Right view, right purpose, right speech, right action, right "
             "livelihood, right effort, and right mindfulness",
             "The seven planes of consciousness from the previous discourse",
             "Faith, energy, mindfulness, immersion, and wisdom, plus two more"],
         "correct": 1,
         "expl": "The noble eightfold path's first seven factors, named as a set."},
        {"q": "According to the guide, is this discourse introducing a new formula?",
         "opts": [
             "Yes, seven entirely new qualities not found elsewhere",
             "No — it is the noble eightfold path itself, minus its own eighth "
             "factor, with a claim added about how the eighth depends on the other "
             "seven",
             "Yes, a replacement for the eightfold path",
             "No, it simply repeats the seven planes of consciousness"],
         "correct": 1,
         "expl": "No new content — a structural claim about the path's existing "
                 "seven factors."},
        {"q": "What two names does the discourse give to right immersion once its "
              "seven prerequisites are counted in?",
         "opts": [
             "Mundane and transcendent",
             "&ldquo;With its vital conditions&rdquo; and &ldquo;with its "
             "prerequisites&rdquo;",
             "Weak and strong",
             "First and second absorption"],
         "correct": 1,
         "expl": "saupaniso and saparikkhāro, two phrases for the same claim."},
        {"q": "Where does this same definition of right immersion recur, according "
              "to the guide?",
         "opts": [
             "Nowhere else in the canon",
             "MN 117, anchoring that discourse's account of the eightfold path as "
             "mundane and transcendent tiers",
             "DN 15 only",
             "AN 6.31 only"],
         "correct": 1,
         "expl": "A cross-reference to the Mahācattarisaka's fuller treatment of the "
                 "same phrase."},
        {"q": "What does the guide say this discourse pushes back against?",
         "opts": [
             "Nothing in particular",
             "Treating meditative immersion as a free-standing technique separable "
             "from view, speech, action, and livelihood",
             "The value of meditation altogether",
             "The existence of the eightfold path"],
         "correct": 1,
         "expl": "A structural point about immersion depending on the other seven "
                 "factors, not standing apart from them."},
        {"q": "How long is this discourse?",
         "opts": [
             "A single compact definition, under a minute to read",
             "A lengthy narrative with multiple interlocutors",
             "A set of ten verses",
             "The longest discourse in this chapter"],
         "correct": 0,
         "expl": "One of the shortest discourses in the Sevens, a single-sentence "
                 "definition."},
    ],
    marginalia=[
        ("Seven, not eight", [
            "the path's first seven",
            "factors, named as what",
            "immersion depends on",
        ]),
        ("Two names, one claim", [
            "with its vital conditions,",
            "with its prerequisites —",
            "immersion cannot stand alone",
        ]),
        ("A structural claim", [
            "not a new technique,",
            "a definition of what",
            "noble immersion already means",
        ]),
        ("Cross-references", [
            "AN 7.44 &middot; previous, the seven planes of consciousness",
            "MN 117 &middot; outside this project, the fuller treatment of this same "
            "definition",
        ]),
    ],
    further=[
        '<a href="%s/an7.45/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.44.html">AN 7.44 &middot; Planes of Consciousness</a> '
        "&mdash; previous, opening this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.46 — Paṭhamaaggisutta
# --------------------------------------------------------------------------- #
page(
    46, "Paṭhamaaggi", "Fires (1st)",
    vagga=VAGGA_5,
    meta_title="AN 7.46 — Fires (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaaggisutta, the Buddha's bare list of seven fires — three to be "
        "abandoned, three to be tended, and one to be handled with plain "
        "practicality. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of seven fires, named without commentary or "
                 "explanation of any one of them"),
        ("Length", "under 1 minute to read"),
        ("Companion discourse", "AN 7.47 immediately following gives the same seven "
                                "fires in full narrative and doctrinal detail, in "
                                "the classic short-then-long pairing this book has "
                                "used repeatedly since AN 7.3/7.4"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a bare list, "
                       "meant to be read alongside its companion discourse rather "
                       "than puzzled over alone"),
    ],
    why=(
        "AN 7.46 names seven fires in a single breath &mdash; three inner fires to "
        "be abandoned, three outer fires (or rather, three relationships figured as "
        "fires) worth tending, and an actual wood fire needing nothing more than "
        "ordinary handling &mdash; setting up the fuller treatment AN 7.47 gives the "
        "same seven immediately afterward."),
    guide=[
        ("The teaching in one sentence", [
            "Of seven things this discourse calls fires, three are the fires of "
            "greed, hate, and delusion; three are figurative fires naming people "
            "worth tending like a sacred flame &mdash; parents, one's own household, "
            "and worthy ascetics; and the seventh is simply a wood fire, included to "
            "round out the list of seven rather than to make any doctrinal point."]),
        ("Three fires to abandon", [
            "The fires of greed, hate, and delusion head the list, matching this "
            "book's most familiar three-part diagnosis of what corrupts the mind, "
            "here given the specific image of something that burns rather than "
            "merely afflicts."]),
        ("Three fires to tend", [
            "The next three are fires only in a figurative sense: the fire of those "
            "worthy of offerings dedicated to the gods (one's parents), a "
            "householder's fire (one's dependents), and the fire of those worthy of "
            "a religious donation (ascetics and brahmins who live well). Naming a "
            "relationship a fire worth tending, rather than a duty to discharge, "
            "carries its own claim about how seriously these relationships deserve "
            "to be taken."]),
        ("One fire that is just a fire", [
            "The seventh, a plain wood fire, breaks the pattern entirely: it is not "
            "a metaphor for anything. AN 7.47's fuller version explains that this "
            "one alone should simply be fanned, watched over, extinguished, or set "
            "aside as the moment requires &mdash; the only item on the list that "
            "carries no ethical weight at all."]),
    ],
    terms=[
        ("aggi",
         "&ldquo;fire&rdquo; &mdash; this discourse's organizing image, applied "
         "across three registers: literal inner defilement, figurative worthy "
         "relationship, and literal household fire."),
        ("rāgaggi, dosaggi, mohaggi",
         "&ldquo;the fire of greed, the fire of hate, the fire of delusion&rdquo; "
         "&mdash; the three fires to be abandoned, this book's usual three root "
         "afflictions given a burning image."),
        ("āhuneyyaggi",
         "&ldquo;the fire of those worthy of offerings dedicated to the gods&rdquo; "
         "&mdash; AN 7.47 identifies this as one's own parents."),
        ("gahapataggi, dakkhiṇeyyaggi",
         "&ldquo;a householder's fire, the fire of those worthy of a religious "
         "donation&rdquo; &mdash; AN 7.47 identifies these as one's household "
         "and self-restrained ascetics and brahmins in turn."),
        ("kaṭṭhaggi",
         "&ldquo;a wood fire&rdquo; &mdash; the seventh and only literal, non-"
         "figurative fire on the list."),
    ],
    text_intro=(
        "The discourse in full, a single bare list. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven fires, named"),
        ("p", "&sect;1", "an7.46:1.1-1.4"),
    ],
    quiz=[
        {"q": "How many registers does this discourse's image of &ldquo;fire&rdquo; "
              "operate across, according to the guide?",
         "opts": [
             "One — all seven are the same kind of fire",
             "Three — literal inner defilement, figurative worthy relationship, and "
             "an actual household fire",
             "Two — only inner and outer fires",
             "Four — one for each of the four elements"],
         "correct": 1,
         "expl": "Greed/hate/delusion, three worthy relationships, and one plain "
                 "wood fire."},
        {"q": "Which three fires does this discourse say should be abandoned?",
         "opts": [
             "The fires of greed, hate, and delusion",
             "The fires of parents, household, and ascetics",
             "The seven planes of consciousness",
             "The four absorptions"],
         "correct": 0,
         "expl": "This book's familiar three root afflictions, given a burning "
                 "image."},
        {"q": "According to the guide, who does AN 7.47's fuller treatment identify "
              "as the &ldquo;fire of those worthy of offerings dedicated to the "
              "gods&rdquo;?",
         "opts": [
             "Ascetics and brahmins",
             "One's own parents",
             "The village elders",
             "The Buddha himself"],
         "correct": 1,
         "expl": "Āhuneyyaggi names one's parents, per AN 7.47's expansion."},
        {"q": "What is distinctive about the seventh fire, the wood fire, according "
              "to the guide?",
         "opts": [
             "It carries the heaviest ethical weight of all seven",
             "It is the only item on the list that is not a metaphor for anything, "
             "carrying no ethical weight at all",
             "It should be abandoned like the first three",
             "It represents the Buddha himself"],
         "correct": 1,
         "expl": "A literal fire needing only ordinary practical handling."},
        {"q": "What discourse immediately follows this one with the same seven "
              "fires in fuller detail?",
         "opts": ["AN 7.44", "AN 7.45", "AN 7.47", "AN 7.53"],
         "correct": 2,
         "expl": "The classic short-then-long pairing, as with AN 7.3/7.4 and AN "
                 "7.5/7.6 earlier in this book."},
        {"q": "How is this discourse delivered?",
         "opts": [
             "As a dialogue with a brahmin",
             "As a bare list with no commentary or explanation of any single fire",
             "As a set of verses",
             "As a story about a laywoman"],
         "correct": 1,
         "expl": "The Buddha states the list without elaborating; AN 7.47 supplies "
                 "the explanation."},
    ],
    marginalia=[
        ("Seven fires, three kinds", [
            "three to abandon,",
            "three to tend,",
            "one just a fire",
        ]),
        ("A relationship, called a fire", [
            "parents, household,",
            "worthy ascetics —",
            "each named worth tending",
        ]),
        ("The odd one out", [
            "a plain wood fire,",
            "no metaphor at all,",
            "just fan it or set it aside",
        ]),
        ("Cross-references", [
            "AN 7.47 &middot; next, the same seven fires in full narrative detail",
            "AN 7.45 &middot; earlier, this chapter's other single-sentence "
            "definition",
        ]),
    ],
    further=[
        '<a href="%s/an7.46/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.45.html">AN 7.45 &middot; Prerequisites for Immersion</a> '
        "&mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.47 — Dutiyaaggisutta
# --------------------------------------------------------------------------- #
page(
    47, "Dutiyaaggi", "Fires (2nd)",
    vagga=VAGGA_5,
    meta_title="AN 7.47 — Fires (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaaggisutta, in which the Buddha redirects a brahmin's animal "
        "sacrifice toward the seven fires of AN 7.46, ending with 2,500 animals "
        "set free. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near a great sacrifice the brahmin Uggatasarīra has prepared, "
                    "with 2,500 animals &mdash; five hundred each of bulls, "
                    "bullocks, heifers, goats, and rams &mdash; already led to the "
                    "sacrificial post"),
        ("Speakers", "The brahmin Uggatasarīra, Venerable Ānanda, and the Buddha"),
        ("Form", "A narrative dialogue expanding AN 7.46's bare list of seven "
                 "fires into full doctrinal and practical detail, closing with the "
                 "brahmin's own decision"),
        ("Length", "~5 minutes to read"),
        ("Companion discourse", "AN 7.46 immediately before gives the same seven "
                                "fires as a bare list, in the classic short-then-"
                                "long pairing this book has used since AN 7.3/7.4"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear "
                       "narrative arc, worth reading for both its doctrine and its "
                       "outcome"),
    ],
    why=(
        "AN 7.47 finds the Buddha at the site of an animal sacrifice already under "
        "way, and rather than simply condemning it, redirects the brahmin "
        "Uggatasarīra toward AN 7.46's seven fires &mdash; three to abandon, three "
        "to tend, one needing only practical care &mdash; ending with Uggatasarīra "
        "freeing all 2,500 animals with his own hands."),
    guide=[
        ("The teaching in one sentence", [
            "Before a single animal is slaughtered, the person preparing the "
            "sacrifice has already raised three unskillful knives &mdash; of body, "
            "speech, and mind &mdash; against themselves, and the fires genuinely "
            "worth honoring are not the sacrificial fire at all, but the fires of "
            "greed, hate, and delusion to be abandoned, and one's parents, "
            "household, and worthy ascetics to be tended instead."]),
        ("Ānanda's correction, before the Buddha speaks a word", [
            "Uggatasarīra opens by asking the Buddha to simply confirm what he has "
            "already heard &mdash; that kindling the sacrificial fire is very "
            "fruitful &mdash; three times over, and three times the Buddha only "
            "says he too has heard this, without endorsing it. It is Ānanda who "
            "intervenes, telling Uggatasarīra he is asking the wrong question "
            "entirely, and coaching him to ask for advice instead. Only then does "
            "the Buddha actually teach."]),
        ("Three unskillful knives, raised before the fire is even lit", [
            "The Buddha's first move is to name a cost that precedes the sacrifice "
            "itself: even before kindling the fire, one raises a mental knife in "
            "wishing for the animals' slaughter, a verbal knife in saying so aloud, "
            "and a bodily knife in personally undertaking the preparations &mdash; "
            "three unskillful knives, all self-inflicted, before a single animal "
            "has died."]),
        ("The seven fires of AN 7.46, now explained in full", [
            "The Buddha then works through AN 7.46's seven fires one by one: greed, "
            "hate, and delusion should be given up because a person ruled by them "
            "does bad by body, speech, and mind and is reborn badly as a result; "
            "one's parents (the fire of those worthy of offerings dedicated to the "
            "gods), one's household (a householder's fire), and self-restrained "
            "ascetics and brahmins (the fire of those worthy of a religious "
            "donation) should be honored and cared for; and the actual wood fire "
            "should simply be fanned, watched over, extinguished, or set aside as "
            "practical need requires &mdash; the only item on the list needing no "
            "ethical judgment at all."]),
        ("The outcome: 2,500 animals, set free", [
            "Uggatasarīra does not merely praise the teaching. He declares himself a "
            "lay follower for life and then, in his own words, sets free all five "
            "hundred each of bulls, bullocks, heifers, goats, and rams &mdash; 2,500 "
            "animals in total &mdash; wishing them grass to eat, cool water to "
            "drink, and a cool breeze, closing this discourse with an act rather "
            "than only a statement of faith."]),
    ],
    terms=[
        ("tīṇi akusalāni sattisatāni",
         "&ldquo;three unskillful knives&rdquo; &mdash; of body, speech, and mind, "
         "raised even before the sacrificial fire is kindled."),
        ("rāgaggi, dosaggi, mohaggi",
         "&ldquo;the fire of greed, hate, delusion&rdquo; &mdash; the three fires "
         "this discourse says should be given up and shunned, not cultivated."),
        ("āhuneyyaggi, gahapataggi, dakkhiṇeyyaggi",
         "&ldquo;the fire of those worthy of offerings dedicated to the gods, a "
         "householder's fire, the fire of those worthy of a religious donation"
         "&rdquo; &mdash; identified here in turn as parents, household, and "
         "self-restrained ascetics and brahmins."),
        ("kaṭṭhaggi",
         "&ldquo;a wood fire&rdquo; &mdash; to be fanned, watched over with "
         "equanimity, extinguished, or set aside, from time to time, as practical "
         "need requires."),
        ("Uggatasarīra",
         "the brahmin whose already-prepared animal sacrifice is this discourse's "
         "occasion, and who ends it by freeing every animal himself."),
    ],
    text_intro=(
        "The discourse in full: the sacrifice already under way, Ānanda's "
        "correction, the three unskillful knives, the seven fires explained, and "
        "Uggatasarīra's own act of releasing every animal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The sacrifice, and Uggatasarīra's opening question"),
        ("p", "&sect;1", "an7.47:1.1-2.7"),
        ("h3", "Ānanda's correction, and the Buddha's invitation to teach"),
        ("p", "&sect;2", "an7.47:3.1-4.4"),
        ("h3", "Three unskillful knives, raised before the fire is even lit"),
        ("p", "&sect;3", "an7.47:5.1-7.4"),
        ("h3", "Three fires to abandon, and why"),
        ("p", "&sect;4", "an7.47:8.1-11.5"),
        ("h3", "Three fires to tend, identified in turn"),
        ("p", "&sect;5", "an7.47:12.1-15.4"),
        ("h3", "The wood fire, and Uggatasarīra's own act of release"),
        ("p", "&sect;6", "an7.47:16.1-17.5"),
    ],
    quiz=[
        {"q": "How does the Buddha respond the first three times Uggatasarīra asks "
              "him to confirm that the sacrificial fire is fruitful?",
         "opts": [
             "He directly endorses the sacrifice",
             "He only says he too has heard this, without endorsing it — Ānanda has "
             "to intervene before real teaching begins",
             "He refuses to answer at all",
             "He immediately condemns Uggatasarīra"],
         "correct": 1,
         "expl": "A pointedly non-committal reply, until Ānanda redirects the "
                 "question."},
        {"q": "According to this discourse, when are the three unskillful knives "
              "first raised?",
         "opts": [
             "Only after the animals are actually slaughtered",
             "Even before kindling the sacrificial fire and raising the sacrificial "
             "post at all",
             "Only in a future rebirth",
             "They are never actually raised in this story"],
         "correct": 1,
         "expl": "The cost begins with the intention, before any animal is "
                 "touched."},
        {"q": "Who does the Buddha identify as the &ldquo;fire of those worthy of "
              "offerings dedicated to the gods&rdquo;?",
         "opts": [
             "Kings and rulers",
             "One's own mother and father",
             "The sacrificial animals themselves",
             "Wandering ascetics of any kind"],
         "correct": 1,
         "expl": "Parents, since it is from them one has been incubated and "
                 "produced."},
        {"q": "What does the Buddha say should be done with the actual wood fire, "
              "as distinct from the six figurative fires?",
         "opts": [
             "It should be abandoned entirely, like greed, hate, and delusion",
             "It should, from time to time, be fanned, watched over with equanimity, "
             "extinguished, or set aside",
             "It should be worshipped as a deity",
             "It should never be lit at all"],
         "correct": 1,
         "expl": "Plain practical handling, the only item on the list carrying no "
                 "ethical weight."},
        {"q": "How does this discourse actually end?",
         "opts": [
             "With the sacrifice proceeding as originally planned",
             "With Uggatasarīra declaring himself a lay follower and freeing all "
             "2,500 animals with his own hands",
             "With the Buddha refusing to speak further",
             "With no resolution given at all"],
         "correct": 1,
         "expl": "An act, not only a statement of faith — every animal set free."},
        {"q": "What earlier discourse gives these same seven fires as a bare list, "
              "without this narrative?",
         "opts": ["AN 7.44", "AN 7.45", "AN 7.46", "AN 7.20"],
         "correct": 2,
         "expl": "AN 7.46, the short half of this chapter's short-then-long pairing."},
    ],
    marginalia=[
        ("2,500 animals", [
            "already led to",
            "the sacrificial post",
            "when this discourse opens",
        ]),
        ("Three knives, before the fire", [
            "of body, speech, mind —",
            "raised in the intention",
            "before any animal dies",
        ]),
        ("Fires worth tending instead", [
            "parents, household,",
            "self-restrained ascetics —",
            "named fires worth honoring",
        ]),
        ("Cross-references", [
            "AN 7.46 &middot; previous, the same seven fires as a bare list",
            "AN 7.45 &middot; earlier, this chapter's other single-sentence "
            "definition",
        ]),
    ],
    further=[
        '<a href="%s/an7.47/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.46.html">AN 7.46 &middot; Fires (1st)</a> &mdash; previous, '
        "the same seven fires as a bare list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.48 — Paṭhamasaññāsutta
# --------------------------------------------------------------------------- #
page(
    48, "Paṭhamasaññā", "Perceptions in Brief",
    vagga=VAGGA_5,
    meta_title="AN 7.48 — Perceptions in Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamasaññāsutta, the Buddha's bare list of seven perceptions to "
        "develop, with freedom from death as their objective. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of seven perceptions, named without the extended "
                 "similes and self-checks AN 7.49 gives each one"),
        ("Length", "under 1 minute to read"),
        ("Companion discourse", "AN 7.49 immediately following works through the "
                                "same seven perceptions one at a time, with a simile "
                                "and a self-check for how to tell whether each has "
                                "been genuinely developed"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a bare list, "
                       "best read as a table of contents for its companion "
                       "discourse"),
    ],
    why=(
        "AN 7.48 names seven perceptions worth developing &mdash; from ugliness "
        "and death through to not-self in suffering &mdash; in a single breath, "
        "with freedom from death named as their shared objective and culmination, "
        "setting up AN 7.49's discourse-length treatment of the same seven."),
    guide=[
        ("The teaching in one sentence", [
            "Seven perceptions, developed and cultivated, are very fruitful and "
            "beneficial, with freedom from death as their objective and "
            "culmination: the perceptions of ugliness, death, the repulsiveness of "
            "food, dissatisfaction with the whole world, impermanence, suffering in "
            "impermanence, and not-self in suffering."]),
        ("A single sequence, moving from the concrete to the abstract", [
            "The seven move in a deliberate order: ugliness and death are the most "
            "concrete, aimed directly at the body; food's repulsiveness and the "
            "world's dissatisfying nature widen the frame outward; impermanence, "
            "suffering rooted in impermanence, and not-self rooted in suffering "
            "close the sequence with the three characteristics that, worked through "
            "in this order, build toward the discourse's stated goal of freedom "
            "from death."]),
        ("&ldquo;Freedom from death&rdquo; as a shared destination", [
            "Each of the seven is a different angle of approach, but this discourse "
            "names one destination for all of them together: amata, the deathless, "
            "named here as both the objective aimed at and the culmination reached "
            "when any of the seven is fully developed."]),
        ("Why this discourse stays this short", [
            "Nothing here is explained: no simile is given for any of the seven, "
            "and no self-check is offered for telling whether a perception has "
            "actually been developed. AN 7.49 supplies exactly that, working "
            "through the same list one perception at a time &mdash; this discourse "
            "is deliberately the bare list its companion expands."]),
    ],
    terms=[
        ("saññā",
         "&ldquo;perception&rdquo; &mdash; the mode of noticing and construing "
         "experience that each of these seven items trains, distinct from "
         "philosophical view or doctrinal belief."),
        ("asubhasaññā, maraṇasaññā",
         "&ldquo;the perception of ugliness, the perception of death&rdquo; "
         "&mdash; the first two and most body-directed of the seven."),
        ("āhāre paṭikūlasaññā, sabbaloke anabhiratasaññā",
         "&ldquo;the perception of the repulsiveness of food, the perception of "
         "dissatisfaction with the whole world&rdquo; &mdash; the third and fourth, "
         "widening the frame beyond the body."),
        ("aniccasaññā, anicce dukkhasaññā, dukkhe anattasaññā",
         "&ldquo;the perception of impermanence, of suffering in impermanence, of "
         "not-self in suffering&rdquo; &mdash; the closing three, building one "
         "characteristic on the last."),
        ("amatogadhā amatapariyosānā",
         "&ldquo;having freedom from death as their objective and "
         "culmination&rdquo; &mdash; the shared destination this discourse names "
         "for all seven perceptions together."),
    ],
    text_intro=(
        "The discourse in full, a single bare list. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven perceptions, named, with freedom from death as their goal"),
        ("p", "&sect;1", "an7.48:1.1-2.3"),
    ],
    quiz=[
        {"q": "What shared objective does this discourse name for all seven "
              "perceptions?",
         "opts": [
             "Rebirth as a god",
             "Freedom from death, as both objective and culmination",
             "Wealth and long life",
             "Skill in debate"],
         "correct": 1,
         "expl": "Amata, the deathless, named as the destination all seven aim at."},
        {"q": "According to the guide, how does the order of the seven perceptions "
              "move?",
         "opts": [
             "Randomly, with no discernible pattern",
             "From the most concrete, body-directed perceptions toward the most "
             "abstract closing three",
             "From most abstract to most concrete",
             "Alphabetically by Pali term"],
         "correct": 1,
         "expl": "Ugliness and death first, then wider dissatisfaction, then the "
                 "three characteristics closing the list."},
        {"q": "What does this discourse NOT provide for any of its seven "
              "perceptions, according to the guide?",
         "opts": [
             "Their names",
             "Any simile or self-check for whether each has actually been "
             "developed",
             "A stated objective",
             "A count of how many there are"],
         "correct": 1,
         "expl": "No explanation is given here — AN 7.49 supplies the similes and "
                 "self-checks."},
        {"q": "Which three perceptions close this discourse's list?",
         "opts": [
             "Ugliness, death, and food's repulsiveness",
             "Impermanence, suffering in impermanence, and not-self in suffering",
             "Faith, energy, and wisdom",
             "The four absorptions"],
         "correct": 1,
         "expl": "The three characteristics, each building on the last."},
        {"q": "What discourse immediately follows this one with the same seven "
              "perceptions worked through individually?",
         "opts": ["AN 7.47", "AN 7.49", "AN 7.50", "AN 7.44"],
         "correct": 1,
         "expl": "AN 7.49, the long half of this pairing."},
        {"q": "How is this discourse delivered?",
         "opts": [
             "As a dialogue with a brahmin",
             "As a bare list with no similes or explanations attached",
             "As a story about a laywoman",
             "As a set of verses"],
         "correct": 1,
         "expl": "A table of contents for AN 7.49's fuller treatment."},
    ],
    marginalia=[
        ("Seven perceptions, one goal", [
            "each a different angle,",
            "all aimed at",
            "freedom from death",
        ]),
        ("Concrete to abstract", [
            "ugliness and death first,",
            "then the world,",
            "then the three characteristics",
        ]),
        ("A table of contents", [
            "no similes here —",
            "just the bare list,",
            "expanded next",
        ]),
        ("Cross-references", [
            "AN 7.49 &middot; next, the same seven perceptions in full detail",
            "AN 6.142 &middot; earlier, a different saññā list building toward "
            "direct knowledge of greed",
        ]),
    ],
    further=[
        '<a href="%s/an7.48/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.47.html">AN 7.47 &middot; Fires (2nd)</a> &mdash; previous.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.49 — Dutiyasaññāsutta
#
# Unlike this book's usual short/long pairs, the source text itself abbreviates
# the middle five perceptions (death, food, world, impermanence, suffering-in-
# impermanence) with SuttaCentral's own peyyāla ellipsis, leaving most of their
# segments blank in translation-en-sujato.json; only perceptions 1 and 7 are
# given in full, each with its own distinct simile. This is not a multi-sutta
# merged page like an-3.183-352.html -- it is a single sutta whose own source
# file abbreviates itself -- so segments() over the ordinary per-perception
# spans handles it without any special casing; the blank segments simply
# contribute nothing to joined().
# --------------------------------------------------------------------------- #
page(
    49, "Dutiyasaññā", "Perceptions in Detail",
    vagga=VAGGA_5,
    meta_title="AN 7.49 — Perceptions in Detail | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyasaññāsutta, working through AN 7.48's seven perceptions one at a "
        "time, with a chicken-feather simile and a self-check for the first, and "
        "a distinct freedom-from-conceit description for the last. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same seven perceptions as AN 7.48, each introduced with "
                 "&ldquo;that's what I said, but why did I say it?&rdquo; and "
                 "answered in turn; the source text itself abbreviates five of the "
                 "seven answers with its own internal ellipsis"),
        ("Length", "~4 minutes to read"),
        ("Companion discourse", "AN 7.48 immediately before gives the same seven "
                                "perceptions as a bare list"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; only two of "
                       "the seven answers are given in full; the other five are "
                       "genuinely abbreviated in the source, not omitted by this "
                       "reading guide"),
    ],
    why=(
        "AN 7.49 takes AN 7.48's seven perceptions and asks, for each one in "
        "turn, why the Buddha said developing it is so fruitful &mdash; but the "
        "source text itself only answers the question in full for the first "
        "(ugliness) and the seventh (not-self in suffering), abbreviating the "
        "middle five with its own peyyāla ellipsis rather than repeating the "
        "same simile five more times."),
    guide=[
        ("The teaching in one sentence", [
            "Each of AN 7.48's seven perceptions is introduced with the same "
            "question &mdash; &ldquo;that's what I said, but why did I say "
            "it?&rdquo; &mdash; and answered by naming what craving or discomfort "
            "the mind draws back from once that perception is well developed, with "
            "a self-check for telling a genuinely developed perception from an "
            "undeveloped one."]),
        ("The perception of ugliness, given in full", [
            "The first perception gets the discourse's complete treatment: a "
            "mendicant who often meditates on ugliness finds their mind drawing "
            "back from sexual intercourse, compared to a chicken's feather or a "
            "scrap of sinew thrown into a fire, which shrivels and rolls up rather "
            "than stretching out. A two-sided self-check follows &mdash; if the "
            "mind is still drawn to intercourse rather than repulsed, the "
            "perception is undeveloped; if it draws back, development has been "
            "achieved."]),
        ("Five perceptions, genuinely abbreviated in the source itself", [
            "The next five &mdash; death, the repulsiveness of food, "
            "dissatisfaction with the whole world, impermanence, and suffering "
            "rooted in impermanence &mdash; each name what the mind draws back "
            "from (the desire to be reborn, craving for tastes, the world's shiny "
            "things, material things and honors and fame) but then abbreviate the "
            "chicken-feather simile and the two-sided self-check with an ellipsis, "
            "trusting the reader to supply what perception 1 already spelled out "
            "in full. This is the source text's own shorthand, not a gap in this "
            "reading guide."]),
        ("The perception of not-self in suffering, given in full again", [
            "The seventh and final perception breaks from the abbreviated middle "
            "five to receive its own complete description, and a different one: "
            "not a chicken-feather simile but a direct account of a heart rid of "
            "I-making, mine-making, and conceit, gone beyond discrimination, "
            "peaceful and well freed &mdash; the discourse's fullest statement of "
            "what full liberation from these seven perceptions actually looks "
            "like."]),
    ],
    terms=[
        ("kiñcetaṁ paṭicca vuttaṁ",
         "&ldquo;why did I say it?&rdquo; &mdash; the question repeated before "
         "each of the seven perceptions is explained in turn."),
        ("kukkuṭapattaṁ vā nhārudaddulaṁ vā aggimhi pakkhittaṁ",
         "&ldquo;a chicken's feather or a scrap of sinew thrown in a fire&rdquo; "
         "&mdash; the simile given in full for the perception of ugliness, and "
         "abbreviated by ellipsis for the five perceptions that follow it."),
        ("methunadhammasamāpatti",
         "&ldquo;sexual intercourse&rdquo; &mdash; what the mind reinforced with "
         "the perception of ugliness draws back from, this discourse's first and "
         "fullest example."),
        ("abhāvitā, subhāvitā",
         "&ldquo;undeveloped&rdquo;, &ldquo;well developed&rdquo; &mdash; the "
         "two-sided self-check's own verdict, repeated for the perception of "
         "ugliness and left to be supplied by the reader for the abbreviated five."),
        ("ahaṅkāramamaṅkāramānāpagataṁ",
         "&ldquo;rid of I-making, mine-making, and conceit&rdquo; &mdash; the "
         "distinct, non-abbreviated description given for the seventh perception, "
         "not-self in suffering."),
    ],
    text_intro=(
        "The discourse in full, including the source text's own abbreviation of "
        "five of the seven answers. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The seven perceptions, and their shared goal, restated"),
        ("p", "&sect;1", "an7.49:1.1-1.4"),
        ("h3", "The perception of ugliness, why it was said, in full"),
        ("p", "&sect;2", "an7.49:2.1-3.8"),
        ("h3", "The perception of death, in brief"),
        ("p", "&sect;3", "an7.49:4.1-5.8"),
        ("h3", "The perception of the repulsiveness of food, in brief"),
        ("p", "&sect;4", "an7.49:6.1-7.8"),
        ("h3", "The perception of dissatisfaction with the whole world, in brief"),
        ("p", "&sect;5", "an7.49:8.1-9.8"),
        ("h3", "The perception of impermanence, in brief"),
        ("p", "&sect;6", "an7.49:10.1-11.8"),
        ("h3", "The perception of suffering in impermanence, in brief"),
        ("p", "&sect;7", "an7.49:12.1-13.8"),
        ("h3", "The perception of not-self in suffering, why it was said, in full"),
        ("p", "&sect;8", "an7.49:14.1-16.5"),
        ("h3", "Closing"),
        ("p", "&sect;9", "an7.49:17.1"),
    ],
    quiz=[
        {"q": "What question does this discourse ask about each of AN 7.48's seven "
              "perceptions in turn?",
         "opts": [
             "How many people have developed it",
             "That's what I said, but why did I say it? — asking what the "
             "perception actually accomplishes",
             "How long it takes to develop",
             "Whether it is easier than the other six"],
         "correct": 1,
         "expl": "A recurring formula, repeated before each perception's answer."},
        {"q": "According to the guide, how many of the seven perceptions receive "
              "the discourse's complete, non-abbreviated treatment?",
         "opts": [
             "All seven, in full detail",
             "Only two — ugliness (the first) and not-self in suffering (the "
             "seventh) — with the middle five abbreviated by the source text's own "
             "ellipsis",
             "None; the whole discourse is abbreviated",
             "Only the last one"],
         "correct": 1,
         "expl": "The source text itself elides the middle five, not this reading "
                 "guide."},
        {"q": "What simile does this discourse give for the perception of "
              "ugliness?",
         "opts": [
             "A boat crossing a flood",
             "A chicken's feather or a scrap of sinew thrown into a fire, which "
             "shrivels and rolls up rather than stretching out",
             "A lotus rising above muddy water",
             "A raft, to be set down once the far shore is reached"],
         "correct": 1,
         "expl": "The discourse's one fully spelled-out simile, referenced by "
                 "ellipsis for the five perceptions that follow it."},
        {"q": "What two-sided self-check does the discourse offer for the "
              "perception of ugliness?",
         "opts": [
             "There is no self-check offered at all",
             "If the mind still draws to intercourse rather than repulsion, the "
             "perception is undeveloped; if it draws back, it is well developed",
             "A written examination administered by another mendicant",
             "Whether the mendicant can recite the perception from memory"],
         "correct": 1,
         "expl": "A first-person diagnostic, left implicit for the abbreviated "
                 "five that follow."},
        {"q": "How does the seventh perception, not-self in suffering, differ from "
              "the perception of ugliness in how it is described?",
         "opts": [
             "It uses the identical chicken-feather simile",
             "It uses a different, non-abbreviated description — a heart rid of "
             "I-making, mine-making, and conceit, gone beyond discrimination",
             "It is not described at all",
             "It is described only by a single word"],
         "correct": 1,
         "expl": "A distinct full treatment, not a repetition of perception 1's "
                 "simile."},
        {"q": "What earlier discourse in this chapter gives these same seven "
              "perceptions as a bare list?",
         "opts": ["AN 7.44", "AN 7.46", "AN 7.48", "AN 7.45"],
         "correct": 2,
         "expl": "AN 7.48, the short half of this pairing."},
    ],
    marginalia=[
        ("Two in full, five abbreviated", [
            "ugliness and not-self —",
            "the other five",
            "elided by the source itself",
        ]),
        ("A chicken's feather in fire", [
            "shrivels, rolls up,",
            "doesn't stretch out —",
            "the mind draws back the same way",
        ]),
        ("A different close", [
            "not-self in suffering",
            "gets its own account:",
            "rid of I-making entirely",
        ]),
        ("Cross-references", [
            "AN 7.48 &middot; previous, the same seven perceptions as a bare list",
            "AN 7.50 &middot; next, seven sexual yokes and their own drawing-back",
        ]),
    ],
    further=[
        '<a href="%s/an7.49/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.48.html">AN 7.48 &middot; Perceptions in Brief</a> '
        "&mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.50 — Methunasutta
# --------------------------------------------------------------------------- #
page(
    50, "Methuna", "Sex",
    vagga=VAGGA_5,
    meta_title="AN 7.50 — Sex | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Methunasutta, in which the Buddha answers a brahmin's blunt question "
        "about chastity by naming seven sexual yokes, from physical touch to the "
        "subtle wish to be reborn as a god. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "An unnamed location; the brahmin Jānussoṇi approaches the "
                    "Buddha directly, with no monastery named"),
        ("Speakers", "The brahmin Jānussoṇi and the Buddha"),
        ("Form", "A blunt question and answer, working through seven "
                 "progressively subtler ways chastity can be broken, tainted, or "
                 "marred, without ever involving actual intercourse"),
        ("Length", "~3 minutes to read"),
        ("Recurring interlocutor", "Jānussoṇi appears elsewhere across the "
                                   "canon questioning the Buddha; here the "
                                   "question is as direct as it gets, and the "
                                   "Buddha's claim to intact chastity is equally "
                                   "direct"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear, "
                       "escalating structure, worth reading alongside AN 7.51's "
                       "different angle on the same underlying subject"),
    ],
    why=(
        "AN 7.50 has the brahmin Jānussoṇi ask the Buddha, point-blank, whether "
        "he claims to be chaste, and the Buddha answers by naming seven ways "
        "chastity can be broken, tainted, or marred short of intercourse itself "
        "&mdash; from consenting to a massage, through gazing and recollection, to "
        "the subtlest yoke of all: practicing celibacy while wishing to be reborn "
        "among the gods."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant can avoid intercourse entirely and still be yoked by sex "
            "in seven possible ways, each one enjoyed and found rewarding even "
            "without physical union, and the Buddha declares he did not announce "
            "his own awakening until every one of the seven had been given up in "
            "him, without exception."]),
        ("A direct question, a direct claim", [
            "Jānussoṇi does not ease into his question: he asks outright whether "
            "the Buddha claims to be chaste, and the Buddha answers just as "
            "directly &mdash; intact, impeccable, spotless, unmarred, full and "
            "pure &mdash; before Jānussoṇi presses further, asking what would "
            "actually count as a break in that claim."]),
        ("Seven yokes, each one short of intercourse itself", [
            "The Buddha's answer moves through seven items in ascending "
            "subtlety: consenting to be anointed, massaged, bathed, or rubbed by "
            "a woman; giggling, playing, and having fun with women; gazing into a "
            "woman's eyes; listening through a wall to women laughing, chatting, "
            "singing, or crying; recalling past times spent laughing and having "
            "fun with women; and watching a householder or their child enjoying "
            "the five kinds of sensual stimulation. Each is described identically "
            "&mdash; enjoyed, liked, found rewarding &mdash; and each counts as a "
            "break, taint, stain, or mar in chastity, yoking one to sex without "
            "any actual sexual contact taking place."]),
        ("The seventh and subtlest yoke: aspiring to a god's pleasures", [
            "The seventh yoke is the most surprising: not seeing a householder "
            "enjoy sensual pleasure, but living the chaste life while wishing to "
            "be reborn among the gods through one's own precepts or austerities. "
            "Even this forward-looking wish for future pleasure, entirely absent "
            "any present sensual contact, still counts as being yoked by sex, "
            "since it is enjoyed and found rewarding in exactly the same way as "
            "the other six."]),
        ("Only when every yoke was given up", [
            "The discourse closes with the Buddha's own account of his path to "
            "awakening: as long as he saw even one of these seven sexual yokes "
            "still present in himself, he did not announce his supreme "
            "awakening; only once every one of the seven had been given up, "
            "without exception, did he make that announcement, followed "
            "immediately by the knowledge that his freedom was unshakable and "
            "this was his last rebirth."]),
    ],
    terms=[
        ("brahmacārī",
         "&ldquo;chaste&rdquo;, one living the chaste life &mdash; the claim "
         "Jānussoṇi asks the Buddha to confirm or deny at the discourse's opening."),
        ("methunasaṁyoga",
         "&ldquo;sexual yoke&rdquo; &mdash; this discourse's own title-word, "
         "naming each of the seven ways chastity can be broken short of actual "
         "intercourse."),
        ("khaṇḍaṁ, chiddaṁ, sabalaṁ, kammāsaṁ",
         "&ldquo;a break, taint, stain, or mar&rdquo; &mdash; the fourfold "
         "description repeated for each of the seven yokes in turn."),
        ("pañcahi kāmaguṇehi samappitaṁ samaṅgībhūtaṁ paricārayamānaṁ",
         "&ldquo;supplied and provided with the five kinds of sensual "
         "stimulation&rdquo; &mdash; what the sixth yoke watches a householder or "
         "their child enjoying."),
        ("iminā ahaṁ sīlena vā vatena vā tapena vā brahmacariyena vā devo vā "
         "bhavissāmi devaññataro vā",
         "&ldquo;by this precept or observance or fervent austerity or spiritual "
         "practice, may I become one of the gods!&rdquo; &mdash; the seventh and "
         "subtlest yoke, chastity practiced with an eye on future divine "
         "pleasure."),
    ],
    text_intro=(
        "The discourse in full: Jānussoṇi's question, the Buddha's claim, and "
        "the seven sexual yokes named one by one. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Jānussoṇi's question, and the Buddha's claim to intact chastity"),
        ("p", "&sect;1", "an7.50:1.1-1.7"),
        ("h3", "The first yoke: consenting to be touched"),
        ("p", "&sect;2", "an7.50:2.1-2.5"),
        ("h3", "The second: giggling and playing with women"),
        ("p", "&sect;3", "an7.50:3.1-3.2"),
        ("h3", "The third and fourth: gazing into eyes, listening through a wall"),
        ("p", "&sect;4", "an7.50:4.1-5.2"),
        ("h3", "The fifth and sixth: recalling past pleasure, watching another's "
               "enjoyment"),
        ("p", "&sect;5", "an7.50:6.1-7.2"),
        ("h3", "The seventh, subtlest yoke: chastity aimed at a god's pleasures"),
        ("p", "&sect;6", "an7.50:8.1-8.5"),
        ("h3", "Only once every yoke was given up"),
        ("p", "&sect;7", "an7.50:9.1-10.3"),
        ("h3", "Jānussoṇi's response"),
        ("p", "&sect;8", "an7.50:11.1-11.2"),
    ],
    quiz=[
        {"q": "What question does the brahmin Jānussoṇi ask the Buddha at the "
              "opening of this discourse?",
         "opts": [
             "Whether he approves of animal sacrifice",
             "Whether Mister Gotama claims to be chaste",
             "Whether the eightfold path has eight or seven factors",
             "Whether he has ever broken a precept"],
         "correct": 1,
         "expl": "A blunt, direct question, met with an equally direct answer."},
        {"q": "Does the Buddha's list of seven sexual yokes require actual "
              "intercourse to have taken place?",
         "opts": [
             "Yes, every one of the seven requires intercourse",
             "No — none of the seven involves actual intercourse; each is a "
             "subtler form of being yoked by sex",
             "Only the first yoke requires intercourse",
             "The discourse does not specify"],
         "correct": 1,
         "expl": "From consenting to touch through to a future-oriented wish, none "
                 "involves intercourse itself."},
        {"q": "What is the seventh and, according to the guide, most surprising "
              "yoke?",
         "opts": [
             "Actual sexual intercourse",
             "Living the chaste life while wishing, through one's own precepts or "
             "austerities, to be reborn among the gods",
             "Refusing to speak to women at all",
             "Eating food prepared by a woman"],
         "correct": 1,
         "expl": "A forward-looking wish for future pleasure, still counted as "
                 "being yoked by sex."},
        {"q": "According to the discourse's closing account, when did the Buddha "
              "announce his supreme awakening?",
         "opts": [
             "As soon as he began practicing austerities",
             "Only once every one of the seven sexual yokes had been given up in "
             "him, without exception",
             "Before he had given up any of the seven yokes",
             "He never made such an announcement"],
         "correct": 1,
         "expl": "A precondition stated without qualification — every one of the "
                 "seven, not most of them."},
        {"q": "What does the sixth yoke involve?",
         "opts": [
             "Reading scripture",
             "Watching a householder or their child enjoying the five kinds of "
             "sensual stimulation",
             "Teaching the Dhamma to laypeople",
             "Fasting for a full day"],
         "correct": 1,
         "expl": "A vicarious enjoyment, watching rather than directly "
                 "participating."},
        {"q": "How does Jānussoṇi respond after hearing the Buddha's answer?",
         "opts": [
             "He rejects the teaching outright",
             "He declares himself a lay follower who has gone for refuge for life",
             "He asks the Buddha to repeat the entire list",
             "He remains silent and leaves without comment"],
         "correct": 1,
         "expl": "The discourse's standard closing formula for a satisfied "
                 "questioner."},
    ],
    marginalia=[
        ("Seven yokes, no intercourse", [
            "from a massage's consent",
            "to a forward wish",
            "for a god's pleasures",
        ]),
        ("Not until all seven", [
            "were given up",
            "did the Buddha announce",
            "his own awakening",
        ]),
        ("The subtlest yoke", [
            "chastity practiced",
            "while still wishing",
            "for pleasure to come",
        ]),
        ("Cross-references", [
            "AN 7.51 &middot; next, a different angle on the same underlying "
            "subject",
            "AN 7.49 &middot; previous, the perception of ugliness drawing the "
            "mind back from intercourse",
        ]),
    ],
    further=[
        '<a href="%s/an7.50/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.49.html">AN 7.49 &middot; Perceptions in Detail</a> '
        "&mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.51 — Saṁyogasutta
#
# A thematic echo of AN 7.50, not a numbered Paṭhama/Dutiya pair with it: this
# discourse shares no narrative frame, no interlocutor, and no vocabulary with
# 7.50, only the underlying subject of what draws men and women toward each
# other. Worth flagging as a case where two discourses on the same theme sit
# adjacent without being a formal companion pair.
# --------------------------------------------------------------------------- #
page(
    51, "Saṁyoga", "Yoking and Unyoking",
    vagga=VAGGA_5,
    meta_title="AN 7.51 — Yoking and Unyoking | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Saṁyogasutta, an exposition on how women and men yoke themselves to "
        "each other by dwelling on their own femininity or masculinity, and how "
        "that yoke can be undone. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A symmetrical doctrinal exposition, working through a woman's "
                 "case and then a man's case in mirror-image structure, for both "
                 "yoking and unyoking"),
        ("Length", "~2 minutes to read"),
        ("Relation to AN 7.50", "A thematic echo, not a formal Paṭhama/Dutiya "
                                "pair — this discourse shares no narrative frame "
                                "or interlocutor with AN 7.50, only the same "
                                "underlying subject of attraction between women "
                                "and men"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clean "
                       "mirror structure, straightforward once the pattern is "
                       "seen"),
    ],
    why=(
        "AN 7.51 offers an exposition on yoking and unyoking that works entirely "
        "by a mirrored structure: a woman who dwells on her own femininity is "
        "drawn to a man's masculinity and desires to be yoked to him, and a man "
        "who dwells on his own masculinity is drawn to a woman's femininity in "
        "exactly the same way &mdash; with unyoking described as the same "
        "structure run in reverse."),
    guide=[
        ("The teaching in one sentence", [
            "Yoking between women and men begins inward, not outward: a woman "
            "who focuses on and takes pleasure in her own feminine qualities is "
            "thereby drawn to focus on and take pleasure in a man's masculine "
            "qualities, and desires to be yoked to him &mdash; and the same "
            "structure holds for a man focusing on his own masculinity."]),
        ("Six qualities, named for each side of the mirror", [
            "The discourse names six specific qualities for each side: moves, "
            "appearance, ways, desires, voice, and adornment &mdash; feminine for "
            "a woman's own self-focus and for the man she is drawn to describe by "
            "contrast, masculine for a man's own self-focus and for the woman he "
            "is drawn to. The same six-item list runs through all four cases "
            "&mdash; a woman's yoking, a man's yoking, a woman's unyoking, a "
            "man's unyoking &mdash; with only the direction of attention and its "
            "presence or absence changing."]),
        ("Yoking begins with the self, not the other", [
            "The order of the exposition is deliberate: a woman first focuses on "
            "her own femininity and is stimulated by it, and only then turns to "
            "focus on a man's masculinity. Attraction to another is presented as "
            "downstream of an already-established pleasure taken in one's own "
            "gendered qualities, not as an independent starting point."]),
        ("Unyoking as the identical structure, simply undone", [
            "The discourse's second half does not describe a different mechanism "
            "for freedom from this yoke; it restates the same structure with each "
            "step negated &mdash; not focusing on one's own qualities, not being "
            "stimulated, not focusing on the other's qualities, not desiring to "
            "be yoked &mdash; making the path out of the yoke exactly as "
            "structured as the path into it."]),
    ],
    terms=[
        ("saṁyogavisaṁyoga",
         "&ldquo;yoking and unyoking&rdquo; &mdash; this discourse's own title, "
         "naming the paired exposition it delivers."),
        ("itthatta, purisatta",
         "&ldquo;femininity&rdquo;, &ldquo;masculinity&rdquo; &mdash; the "
         "quality each side of the mirror focuses on in itself before being "
         "drawn to its counterpart in the other."),
        ("itthākappa, itthākāra, itthākhāya, itthicchandā, itthissara, itthālaṅkāra",
         "&ldquo;feminine moves, appearance, ways, desires, voice, and "
         "adornment&rdquo; &mdash; the six-item list applied to women throughout "
         "this discourse's four mirrored cases."),
        ("ye hi keci, bhikkhave, sattā itthiyā abhiratā, sabbe te purisassa "
         "saṁyuttā",
         "&ldquo;sentient beings who relish their femininity are yoked to "
         "men&rdquo; &mdash; the discourse's own stated conclusion for the "
         "yoking half of a woman's case."),
        ("nātivattati",
         "&ldquo;does not transcend&rdquo; &mdash; the verb marking a failure to "
         "move beyond one's own gendered self-focus, mirrored by "
         "&ldquo;transcends&rdquo; in the unyoking half."),
    ],
    text_intro=(
        "The discourse in full, its mirrored exposition of yoking and unyoking "
        "for both a woman's case and a man's case. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The teaching announced"),
        ("p", "&sect;1", "an7.51:1.1-1.3"),
        ("h3", "Yoking: a woman focused on her own femininity, desiring a man"),
        ("p", "&sect;2", "an7.51:2.1-2.10"),
        ("h3", "Yoking: a man focused on his own masculinity, desiring a woman"),
        ("p", "&sect;3", "an7.51:3.1-3.11"),
        ("h3", "Unyoking: a woman not focused on her own femininity"),
        ("p", "&sect;4", "an7.51:4.1-4.11"),
        ("h3", "Unyoking: a man not focused on his own masculinity"),
        ("p", "&sect;5", "an7.51:5.1-5.12"),
    ],
    quiz=[
        {"q": "According to this discourse, what does a woman's yoking to a man "
              "begin with?",
         "opts": [
             "Directly noticing a man's masculine qualities, with no self-focus "
             "involved",
             "Focusing on and taking pleasure in her own feminine qualities first, "
             "which then draws her to a man's masculine qualities",
             "A formal ceremony",
             "Nothing — the discourse says yoking has no discernible cause"],
         "correct": 1,
         "expl": "An inward starting point, with attraction to another presented "
                 "as downstream of it."},
        {"q": "How many specific qualities does the discourse name for each side "
              "of its mirror — feminine and masculine?",
         "opts": ["Three", "Four", "Six — moves, appearance, ways, desires, voice, "
                  "and adornment", "Eight"],
         "correct": 2,
         "expl": "A fixed six-item list, applied consistently across all four "
                 "cases."},
        {"q": "How does the discourse describe unyoking, according to the guide?",
         "opts": [
             "As an entirely different mechanism from yoking",
             "As the identical structure of yoking, with each step simply negated",
             "As something achieved only through a teacher's direct intervention",
             "The discourse does not describe unyoking at all"],
         "correct": 1,
         "expl": "Not focusing, not being stimulated, not desiring to be yoked — "
                 "the same steps, reversed."},
        {"q": "What is this discourse's relationship to AN 7.50, according to the "
              "guide?",
         "opts": [
             "A formal Paṭhama/Dutiya pair sharing the same narrative frame",
             "A thematic echo only — no shared narrative frame or interlocutor, "
             "just the same underlying subject",
             "A direct continuation of the same conversation",
             "An unrelated discourse on an entirely different topic"],
         "correct": 1,
         "expl": "Adjacent in theme, not a formally paired companion discourse."},
        {"q": "How is this discourse delivered?",
         "opts": [
             "As a dialogue with a brahmin",
             "As a direct doctrinal exposition to the mendicants, with no "
             "narrative frame",
             "As a story about a laywoman",
             "As a set of verses"],
         "correct": 1,
         "expl": "The Buddha announces the exposition and delivers it directly, "
                 "with no interlocutor named."},
        {"q": "What does the discourse conclude about sentient beings who relish "
              "their own femininity?",
         "opts": [
             "They are entirely free from any yoke",
             "They are yoked to men",
             "They are yoked to women",
             "The discourse draws no conclusion"],
         "correct": 1,
         "expl": "The discourse's own stated conclusion for the yoking half of a "
                 "woman's case."},
    ],
    marginalia=[
        ("Inward first, outward second", [
            "self-focus on one's own",
            "gender comes before",
            "attraction to the other",
        ]),
        ("Six qualities, four cases", [
            "moves, appearance, ways,",
            "desires, voice, adornment —",
            "run through yoking and unyoking alike",
        ]),
        ("The same steps, reversed", [
            "unyoking is not",
            "a different path —",
            "it is yoking's steps undone",
        ]),
        ("Cross-references", [
            "AN 7.50 &middot; previous, a thematic echo on the same underlying "
            "subject",
            "AN 7.52 &middot; next, seven kinds of motivation behind giving a "
            "gift",
        ]),
    ],
    further=[
        '<a href="%s/an7.51/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.50.html">AN 7.50 &middot; Sex</a> &mdash; previous, a '
        "thematic echo rather than a formal companion pair.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.52 — Dānamahapphalasutta
# --------------------------------------------------------------------------- #
page(
    52, "Dānamahapphala", "A Very Fruitful Gift",
    vagga=VAGGA_5,
    meta_title="AN 7.52 — A Very Fruitful Gift | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dānamahapphalasutta, in which the Buddha answers Sāriputta by naming "
        "seven motivations behind an identical gift, from self-interested "
        "investment to giving as an ornament for the mind. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Near Campā, on the banks of the Gaggarā Lotus Pond; lay "
                    "followers of Campā first approach Venerable Sāriputta, then "
                    "return with him on the next sabbath day to the Buddha"),
        ("Speakers", "Lay followers of Campā, Venerable Sāriputta, and the "
                     "Buddha"),
        ("Form", "A two-stage narrative frame leading into Sāriputta's question "
                 "and the Buddha's answer, which names seven motivations for "
                 "giving the identical gift, describing the outcome of the "
                 "first and seventh in full and abbreviating the middle five"),
        ("Length", "~4 minutes to read"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "question is simple, but tracking exactly which "
                       "motivation produces which outcome rewards a careful "
                       "read"),
    ],
    why=(
        "AN 7.52 has Sāriputta ask the Buddha why one person's gift might be "
        "unfruitful while another person's exactly identical gift is very "
        "fruitful, and the Buddha answers by naming seven different motivations "
        "behind giving &mdash; the same gift, given for reasons ranging from "
        "self-interested investment to using generosity as an ornament for the "
        "mind &mdash; each motivation producing a genuinely different result."),
    guide=[
        ("The teaching in one sentence", [
            "Two people can give the identical gift and receive entirely "
            "different fruits, because what actually determines a gift's fruit "
            "is not the gift itself but the state of mind behind it &mdash; and "
            "this discourse ranks seven such states of mind from least to most "
            "refined."]),
        ("A double approach, before the question is even asked", [
            "The lay followers of Campā first ask Sāriputta for a Dhamma talk, "
            "are told to return on the next sabbath, and only then does Sāriputta "
            "bring them to the Buddha and pose the question himself &mdash; a "
            "two-stage narrative that delays the actual teaching until an entire "
            "second scene."]),
        ("The first motivation: giving as an investment", [
            "The least refined motivation treats a gift as an investment, given "
            "with the mind tied to it, expecting to keep it and enjoy it in a "
            "future life. Someone who gives this way, the Buddha says, is reborn "
            "in the company of the gods of the Four Great Kings &mdash; and "
            "returns to this place once that result is spent."]),
        ("Five further motivations, named but not fully spelled out", [
            "Between the first and the seventh, the Buddha names five further "
            "motivations in ascending refinement &mdash; giving because it's good "
            "to give, because it continues a family tradition, out of simple "
            "reciprocity, in emulation of the ancient sages, or because giving "
            "itself makes the mind clear and joyful &mdash; each introduced with "
            "the same formula and then abbreviated by the source text's own "
            "ellipsis rather than given a separately spelled-out result."]),
        ("The seventh motivation: giving as an ornament for the mind", [
            "The most refined motivation gives no thought at all to the joy or "
            "clarity giving produces, but simply as an adornment and requisite "
            "for the mind &mdash; and this motivation alone, among all seven, "
            "leads to rebirth among the gods of the Divinity's host as a "
            "non-returner, someone who does not come back to this place at all."]),
    ],
    terms=[
        ("dānamahapphala",
         "&ldquo;a very fruitful gift&rdquo; &mdash; this discourse's own title, "
         "naming what distinguishes a fruitful gift from an unfruitful one."),
        ("sannidhipekkho... paṭiggahetvā paribhuñjissāmī&rsquo;ti dānaṁ deti",
         "&ldquo;gives a gift as an investment... [thinking] &lsquo;I'll enjoy "
         "this in my next life&rsquo;&rdquo; &mdash; the least refined of the "
         "seven motivations."),
        ("cittālaṅkāracittaparikkhāranti dānaṁ deti",
         "&ldquo;gives a gift thinking, &lsquo;this is an adornment and "
         "requisite for the mind&rsquo;&rdquo; &mdash; the most refined "
         "motivation, the only one leading to non-return."),
        ("cātumahārājikānaṁ devānaṁ sahabyataṁ",
         "&ldquo;the company of the gods of the Four Great Kings&rdquo; &mdash; "
         "the destination of the least refined motivation, a rebirth that is "
         "eventually spent and returned from."),
        ("brahmakāyikānaṁ devānaṁ sahabyataṁ... anāgāmī hoti",
         "&ldquo;among the gods of the Divinity's host... a non-returner&rdquo; "
         "&mdash; the destination of the most refined motivation, a rebirth not "
         "returned from."),
    ],
    text_intro=(
        "The discourse in full: the two-stage approach to the Buddha, "
        "Sāriputta's question, and all seven motivations for giving, from "
        "investment to mind-adornment. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting: lay followers of Campā ask for a teaching"),
        ("p", "&sect;1", "an7.52:1.1-1.7"),
        ("h3", "The next sabbath, and Sāriputta's question to the Buddha"),
        ("p", "&sect;2", "an7.52:2.1-3.6"),
        ("h3", "The first motivation: giving as an investment"),
        ("p", "&sect;3", "an7.52:4.1-4.4"),
        ("h3", "Its result: rebirth among the Four Great Kings, then return"),
        ("p", "&sect;4", "an7.52:5.1-5.3"),
        ("h3", "Five further motivations, in ascending refinement"),
        ("p", "&sect;5", "an7.52:6.1-10.3"),
        ("h3", "The seventh motivation: giving as an ornament for the mind"),
        ("p", "&sect;6", "an7.52:11.1-11.5"),
        ("h3", "Its result: rebirth among the Divinity's host, and no return"),
        ("p", "&sect;7", "an7.52:12.1-12.13"),
        ("h3", "Sāriputta's question, answered"),
        ("p", "&sect;8", "an7.52:13.1-13.2"),
    ],
    quiz=[
        {"q": "What question does Sāriputta ask the Buddha in this discourse?",
         "opts": [
             "Whether giving is ever worthwhile at all",
             "How the same gift, given by two different people, could be "
             "unfruitful in one case and very fruitful in the other",
             "Whether monks should accept gifts from laypeople",
             "How many kinds of gifts there are"],
         "correct": 1,
         "expl": "A question about what makes an identical gift's fruit differ."},
        {"q": "What does the least refined motivation, giving as an investment, "
              "lead to?",
         "opts": [
             "Rebirth among the gods of the Divinity's host as a non-returner",
             "Rebirth in the company of the gods of the Four Great Kings, with a "
             "return to this place once that result is spent",
             "Immediate awakening",
             "No result at all"],
         "correct": 1,
         "expl": "A temporary result, eventually spent and returned from."},
        {"q": "According to the guide, how are the five motivations between the "
              "first and the seventh treated in the source text?",
         "opts": [
             "Each is given its own fully spelled-out result, just like the first "
             "and seventh",
             "Each is named with the same introductory formula, then abbreviated "
             "by the source text's own ellipsis rather than given a separate "
             "result",
             "They are omitted from the discourse entirely",
             "They are given in reverse order of refinement"],
         "correct": 1,
         "expl": "Named but not separately spelled out, unlike the first and "
                 "seventh motivations."},
        {"q": "What is the seventh and most refined motivation for giving?",
         "opts": [
             "Giving out of family tradition",
             "Giving as an ornament and requisite for the mind, without regard for "
             "the joy or clarity it produces",
             "Giving expecting a future reward",
             "Giving only when asked directly"],
         "correct": 1,
         "expl": "The most refined motivation, and the only one leading to "
                 "non-return."},
        {"q": "What result does the seventh motivation lead to?",
         "opts": [
             "Rebirth in the human realm only",
             "Rebirth among the gods of the Divinity's host as a non-returner, who "
             "does not return to this place",
             "The same result as the first motivation",
             "No rebirth of any kind"],
         "correct": 1,
         "expl": "A rebirth not returned from, unlike the first motivation's "
                 "temporary result."},
        {"q": "How does the narrative reach the Buddha in this discourse?",
         "opts": [
             "The lay followers approach the Buddha directly with no intermediary",
             "In two stages: the lay followers first ask Sāriputta, are told to "
             "return on the next sabbath, and only then are brought to the Buddha",
             "The Buddha visits the lay followers uninvited",
             "There is no narrative frame at all"],
         "correct": 1,
         "expl": "A delayed, two-scene approach before the actual teaching begins."},
    ],
    marginalia=[
        ("Same gift, different fruit", [
            "what differs is not",
            "the gift itself,",
            "but the mind behind it",
        ]),
        ("Seven motivations, ranked", [
            "from self-interested",
            "investment up to",
            "an ornament for the mind",
        ]),
        ("One returns, one doesn't", [
            "the Four Great Kings' realm,",
            "then a return —",
            "or non-return, for the mind-adornment gift",
        ]),
        ("Cross-references", [
            "AN 7.51 &middot; previous, yoking and unyoking between women and men",
            "AN 7.53 &middot; next, closing this chapter's First Fifty with Nanda's "
            "Mother",
        ]),
    ],
    further=[
        '<a href="%s/an7.52/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.51.html">AN 7.51 &middot; Yoking and Unyoking</a> '
        "&mdash; previous.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 7.53 — Nandamātāsutta
#
# This closes both Mahāyaññavagga and AN 7's First Fifty (Paṭhamapaṇṇāsaka,
# AN 7.1-53). Per the lesson from AN 7.20 (see the note above ch.3): the
# `further` list below points only backward, never forward to AN 7.54, since
# the Second Fifty has not been mapped or written yet.
# --------------------------------------------------------------------------- #
page(
    53, "Nandamātā", "Nanda&rsquo;s Mother",
    vagga=VAGGA_5,
    meta_title="AN 7.53 — Nanda's Mother | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nandamātāsutta, closing AN 7's First Fifty with the laywoman Nanda's "
        "Mother revealing seven incredible qualities to Sāriputta, including "
        "the four absorptions at will and the five lower fetters already given "
        "up. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Veḷukaṇṭa, in the home of the laywoman Veḷukaṇṭakī, Nanda's "
                    "Mother, as Venerables Sāriputta and Mahāmoggallāna arrive "
                    "there wandering with a large Saṅgha through the Southern "
                    "Hills"),
        ("Speakers", "Nanda's Mother, the great king Vessavaṇa, and Venerable "
                     "Sāriputta"),
        ("Form", "A narrative opening with an overheard recitation and a deity's "
                 "request, followed by Sāriputta drawing out seven incredible "
                 "and amazing qualities from Nanda's Mother one at a time"),
        ("Length", "~6 minutes to read"),
        ("Closing this chapter, and AN 7's First Fifty", "The last discourse of "
                                                          "Mahāyaññavagga, and "
                                                          "the last of AN 7.1-53, "
                                                          "the Sevens' First "
                                                          "Fifty"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a warm, "
                       "clearly structured narrative, one of this book's most "
                       "vivid portraits of a named lay disciple"),
    ],
    why=(
        "AN 7.53 closes this chapter, and AN 7's entire First Fifty, with one of "
        "the canon's fullest portraits of a laywoman's attainment: Nanda's "
        "Mother is overheard reciting by a great king of the gods, hosts the "
        "Saṅgha the next day on his instruction, and then, questioned by "
        "Sāriputta, reveals seven incredible and amazing qualities culminating "
        "in the four absorptions at will and the five lower fetters already "
        "given up &mdash; the marks of a non-returner, still living as a "
        "householder."),
    guide=[
        ("The teaching in one sentence", [
            "A laywoman, without ever leaving her household, can attain what "
            "monastic teaching usually treats as the province of the ordained: "
            "the four absorptions at will and freedom from the five lower "
            "fetters, the very definition of a non-returner &mdash; and this "
            "discourse spells that out through seven successive qualities rather "
            "than a single statement."]),
        ("A deity overhears, and asks a favor", [
            "The discourse opens with Nanda's Mother reciting verses of &ldquo;"
            "The Way to the Far Shore&rdquo; at dawn, overheard by the great king "
            "Vessavaṇa passing by on business of his own. He applauds her, "
            "reveals himself as her brother in a manner of speaking, and asks a "
            "favor in return for the pleasure her recitation gave him: that when "
            "she serves the mendicant Saṅgha the next day, she dedicate the "
            "religious donation to him."]),
        ("Sāriputta's question, and the first incredible quality", [
            "When Sāriputta asks how she knew the Saṅgha was coming, her answer "
            "&mdash; recounting the conversation with Vessavaṇa in full &mdash; "
            "prompts his own comment that it is incredible and amazing she "
            "converses face to face with so mighty and illustrious a godling. "
            "This exchange itself supplies the first of the seven qualities, "
            "before she has claimed anything for herself."]),
        ("Six more qualities, each introduced the same way", [
            "Nanda's Mother then volunteers six further qualities, each opened "
            "with the same formula &mdash; &ldquo;this is not my only incredible "
            "and amazing quality; there is another&rdquo; &mdash; equanimity at "
            "her only son's execution, equanimity at her husband's posthumous "
            "revelation of his rebirth, unbroken fidelity to her husband even in "
            "thought since their marriage, never deliberately breaking a precept "
            "since declaring herself a lay follower, entering all four "
            "absorptions at will, and having given up every one of the five "
            "lower fetters."]),
        ("The seventh quality names what all the others point toward", [
            "The final quality &mdash; no trace remaining of the five lower "
            "fetters &mdash; is the technical definition of a non-returner, the "
            "third of the four stages of awakening. Read backward, the six "
            "qualities before it &mdash; equanimity through grief, unbroken "
            "fidelity and precepts, mastery of the four absorptions &mdash; are "
            "less a list of separate virtues than the visible signs of a mind "
            "that had, in fact, already reached that far."]),
        ("Closing this chapter, and AN 7's First Fifty", [
            "Sāriputta closes the discourse by teaching her further and taking "
            "his leave, and with that this chapter, Mahāyaññavagga, and AN 7's "
            "entire First Fifty &mdash; fifty-three discourses running from AN "
            "7.1 to AN 7.53 &mdash; come to an end. The Second Fifty has not yet "
            "been mapped or written."]),
    ],
    terms=[
        ("Nandamātā, Veḷukaṇṭakī",
         "&ldquo;Nanda's Mother&rdquo;, &ldquo;the woman of Veḷukaṇṭa&rdquo; "
         "&mdash; this discourse's central figure, named by her son and her "
         "town rather than by a personal name of her own."),
        ("Vessavaṇo mahārājā",
         "&ldquo;the great king Vessavaṇa&rdquo; &mdash; a deity who overhears "
         "her recitation and initiates the exchange that opens this discourse."),
        ("Pārāyanaṁ",
         "&ldquo;The Way to the Far Shore&rdquo; &mdash; the verses Nanda's "
         "Mother is reciting at dawn when Vessavaṇa passes by; a text also known "
         "independently elsewhere in the canon."),
        ("acchariyaṁ abbhutaṁ",
         "&ldquo;incredible, amazing&rdquo; &mdash; the phrase Sāriputta repeats "
         "after each of Nanda's Mother's seven qualities."),
        ("orambhāgiyāni saṁyojanāni",
         "&ldquo;the five lower fetters&rdquo; &mdash; identity view, doubt, "
         "attachment to precepts and observances, sensual desire, and ill will; "
         "their complete absence is this discourse's seventh and final quality, "
         "and the technical mark of a non-returner."),
    ],
    text_intro=(
        "The discourse in full: King Vessavaṇa's request, the meal for the "
        "Saṅgha, and all seven of Nanda's Mother's incredible and amazing "
        "qualities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting: two chief disciples travel through the Southern "
               "Hills"),
        ("p", "&sect;1", "an7.53:1.1-1.3"),
        ("h3", "King Vessavaṇa overhears her recitation, and makes a request"),
        ("p", "&sect;2", "an7.53:2.1-3.9"),
        ("h3", "Nanda's Mother prepares to receive the Saṅgha"),
        ("p", "&sect;3", "an7.53:4.1-4.9"),
        ("h3", "Sāriputta asks how she knew they were coming"),
        ("p", "&sect;4", "an7.53:5.1-6.10"),
        ("h3", "The first quality: conversing with a great king of the gods"),
        ("p", "&sect;5", "an7.53:7.1-7.2"),
        ("h3", "The second and third: equanimity at her son's death, her "
               "husband's rebirth"),
        ("p", "&sect;6", "an7.53:8.1-9.7"),
        ("h3", "The fourth and fifth: unbroken fidelity, unbroken precepts"),
        ("p", "&sect;7", "an7.53:10.1-11.4"),
        ("h3", "The sixth and seventh: the four absorptions at will, and the "
               "five lower fetters gone"),
        ("p", "&sect;8", "an7.53:12.1-13.4"),
        ("h3", "Sāriputta teaches her further, and departs"),
        ("p", "&sect;9", "an7.53:14.1"),
    ],
    quiz=[
        {"q": "What does the great king Vessavaṇa ask of Nanda's Mother, after "
              "overhearing her dawn recitation?",
         "opts": [
             "That she stop reciting the verses",
             "That when she serves the mendicant Saṅgha the next day, she "
             "dedicate the religious donation to him",
             "That she become his student",
             "That she leave Veḷukaṇṭa entirely"],
         "correct": 1,
         "expl": "A favor asked in return for the pleasure her recitation gave "
                 "him."},
        {"q": "How many incredible and amazing qualities does this discourse's "
              "narrative and Nanda's Mother's own testimony together establish, "
              "matching this book of Sevens?",
         "opts": ["Five", "Six", "Seven — one from the Vessavaṇa exchange itself, "
                  "and six she volunteers afterward", "Ten"],
         "correct": 2,
         "expl": "One quality established by the opening narrative, six more "
                 "self-declared, totaling seven."},
        {"q": "What does Nanda's Mother say about her reaction to her only son's "
              "execution?",
         "opts": [
             "She was devastated for years afterward",
             "She can't recall getting upset when he was arrested, imprisoned, "
             "or killed",
             "She does not mention her son at all",
             "She sought revenge against the rulers responsible"],
         "correct": 1,
         "expl": "Equanimity through the loss of her only son, the second of her "
                 "seven qualities."},
        {"q": "What is the seventh and final quality Nanda's Mother names?",
         "opts": [
             "Skill in reciting verses",
             "That she does not see any of the five lower fetters that she "
             "hasn't given up",
             "Wealth and social standing",
             "Knowledge of many languages"],
         "correct": 1,
         "expl": "The technical mark of a non-returner, the third of the four "
                 "stages of awakening."},
        {"q": "According to the guide, what does the seventh quality suggest "
              "about the six qualities that come before it?",
         "opts": [
             "They are unrelated to it",
             "They read as the visible signs of a mind that had already reached "
             "that far, rather than a list of separate, unrelated virtues",
             "They are more advanced than the seventh quality",
             "They contradict the seventh quality"],
         "correct": 1,
         "expl": "Equanimity, fidelity, precepts, and absorption read together as "
                 "signs of the same underlying attainment."},
        {"q": "What does this discourse close, according to the guide?",
         "opts": [
             "Only this individual discourse, with more chapters of the Sevens "
             "still ahead in an already-mapped sequence",
             "This chapter, Mahāyaññavagga, and AN 7's entire First Fifty (AN "
             "7.1 through 7.53) — with the Second Fifty not yet mapped or "
             "written",
             "The entire Aṅguttara Nikāya",
             "Nothing; it is a mid-chapter discourse"],
         "correct": 1,
         "expl": "The last discourse of the First Fifty, closing both the "
                 "chapter and that larger fifty-discourse span."},
    ],
    marginalia=[
        ("A deity overhears", [
            "Vessavaṇa, passing by,",
            "stops to hear her",
            "dawn recitation",
        ]),
        ("Seven qualities, in sequence", [
            "from conversing with a god",
            "to unbroken precepts",
            "to the four absorptions at will",
        ]),
        ("A householder, a non-returner", [
            "the five lower fetters",
            "already given up —",
            "without ever leaving home",
        ]),
        ("Cross-references", [
            "AN 7.52 &middot; previous, seven motivations behind an identical "
            "gift",
            "AN 7.1 &middot; earlier, opening this book's First Fifty, now closed "
            "here",
        ]),
    ],
    further=[
        '<a href="%s/an7.53/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.52.html">AN 7.52 &middot; A Very Fruitful Gift</a> '
        "&mdash; previous.",
        '<a href="an-7.1.html">AN 7.1 &middot; Pleasing (1st)</a> &mdash; '
        "earlier, opening this book's First Fifty, now closed here.",
    ],
)

