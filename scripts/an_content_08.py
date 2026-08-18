# -*- coding: utf-8 -*-
"""Aṭṭhaka Nipāta — The Eights. One discourse per page, from AN 8.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Aṭṭhaka Nipāta — The Eights"
# an-8.30.html and an-8.53.html were published before this series began working
# in order, in the earlier eighteen-page selection; they are listed in the
# index by INDEX_EXTRA and are not regenerated here. Pages built around them
# splice in with explicit prev=/next= kwargs, per the an-6.16/an-6.63/an-7.6
# precedent -- and the two static pages themselves get their own prev/next
# hand-edited once the pages on both sides of each exist. HEAD points at the
# last page the Sevens module reached. TAIL points at the nearest
# already-published page beyond the Eights -- an-9.20.html, from the same
# earlier selection -- until the Nines module exists and TAIL can move to its
# own first page.
HEAD = ("an-7.645-1124.html", "AN 7.645&ndash;1124 &middot; Untitled Discourses on Hate, Etc.")
TAIL = ("an-9.20.html", "AN 9.20 &middot; About Velāma")
INDEX_EXTRA = [
    ("an-8.30", "Anuruddhamahāvitakkasutta", "Anuruddha and the Great Thoughts"),
    ("an-8.53", "Gotamīsutta", "Brief Advice to Gotamī"),
]

PAGES = []

VAGGA_1 = "<em>Mettāvagga</em> &mdash; the first chapter of the Eights"
SETTING_1 = ("Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery; "
             "stated at the head of AN 8.1 and understood to hold across the chapter "
             "unless a fresh setting is given")
SETTING_NONE = "None stated in the source"
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Eights."""
    d = {
        "slug": "an-8.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an8/an8.%d" % num,
        "crumb": "AN 8.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 8.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 8.1 — Mettāsutta
# --------------------------------------------------------------------------- #
page(
    1, "Mettā", "The Benefits of Love",
    vagga=VAGGA_1,
    meta_title="AN 8.1 — The Benefits of Love | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Mettāsutta, opening the Book of the Eights with eight benefits of "
        "cultivating the heart's release by love. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item list of benefits, followed by five verses that "
                 "widen from personal safety to a comparison with royal sacrifice"),
        ("Length", "~1 minute to read"),
        ("Chapter's namesake", "This discourse gives its own name to the chapter, "
                               "<em>Mettāvagga</em>, and to the practice &mdash; "
                               "<em>mettā</em>, love or loving-kindness &mdash; that "
                               "opens the entire new nipāta"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "formulaic, opening the Eights with the collection's now-"
                       "familiar full narrative opening formula"),
    ],
    why=(
        "The Book of the Eights opens exactly as the Sevens did: the full "
        "narrative frame at Sāvatthī, then a bare eight-item list &mdash; you "
        "sleep at ease, wake happily, don't have bad dreams, are loved by humans "
        "and non-humans, are protected by deities, can't be harmed by fire, "
        "poison, or blade, and are reborn in a realm of divinity if you don't "
        "reach anything higher &mdash; followed by verses that rate a mind "
        "developed with love above even the greatest royal sacrifices."),
    guide=[
        ("The teaching in one sentence", [
            "Eight benefits can be expected when the heart's release by love has "
            "been cultivated, developed, and practiced: untroubled sleep and "
            "waking, freedom from nightmares, the love of humans and non-humans, "
            "the protection of deities, immunity to fire, poison, and blade, and "
            "&mdash; short of anything higher &mdash; rebirth in a realm of "
            "divinity."]),
        ("A new nipāta, and this chapter's own namesake", [
            "As with the Sixes and Sevens before it, the Book of the Eights opens "
            "with the traditional full frame. But this discourse does something "
            "the openers of the Sixes and Sevens didn't: it lends its own subject, "
            "<em>mettā</em>, to the chapter's very name, <em>Mettāvagga</em>, the "
            "Chapter on Love."]),
        ("Eight items, not seven", [
            "The count grows by one again, continuing this book's inherited "
            "numerical logic. But unlike the blocking-and-reversal lists that "
            "opened the Sixes and Sevens, this list is entirely positive: eight "
            "benefits, with no negative counterpart given."]),
        ("From safety to comparison with kings", [
            "The prose list of eight benefits is practical and personal &mdash; "
            "sleep, dreams, the goodwill of beings seen and unseen, physical "
            "safety, and a favorable rebirth. The verses that follow widen the "
            "lens dramatically, rating a mind developed with love as worth "
            "sixteen times more than even the greatest royal sacrifices a "
            "conquering king could sponsor."]),
    ],
    terms=[
        ("mettā",
         "&ldquo;love, loving-kindness&rdquo; &mdash; the practice this "
         "discourse and its chapter are named for, described here as a "
         "&ldquo;heart's release&rdquo; (<em>cetovimutti</em>) to be cultivated."),
        ("cetovimutti",
         "&ldquo;heart's release&rdquo; &mdash; the meditative attainment "
         "produced by love when it is &ldquo;cultivated, developed, and "
         "practiced, made a vehicle and a basis, kept up, consolidated, and "
         "properly implemented.&rdquo;"),
        ("na sakkā aggisā vā visena vā satthena vā pāpetuṁ",
         "&ldquo;can't be harmed by fire, poison, or blade&rdquo; &mdash; one "
         "of the eight benefits, and the most vivid of the list's several "
         "physical-safety claims."),
        ("assamedha, purisamedha",
         "&ldquo;horse sacrifice, human sacrifice&rdquo; &mdash; two of the "
         "grand royal sacrifices the closing verses set against a mind "
         "developed with love, and find wanting."),
        ("soḷasiṁ kalaṁ nāgghanti",
         "&ldquo;not worth a sixteenth part&rdquo; &mdash; the verses' own "
         "measure of how far love outweighs even a conquering king's greatest "
         "sacrifices, echoed by the moon-versus-stars simile that follows it."),
    ],
    text_intro=(
        "The discourse in full: eight benefits of a heart developed with love, "
        "and five verses on love's incomparable worth. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and eight benefits"),
        ("p", "&sect;1", "an8.1:1.1-1.6"),
        ("p", "&sect;2", "an8.1:2.1-2.4"),
        ("h3", "Verses: a mind developed with love"),
        ("p", "&sect;3", "an8.1:3.1-3.4"),
        ("p", "&sect;4", "an8.1:4.1-4.4"),
        ("p", "&sect;5", "an8.1:5.1-5.4"),
        ("p", "&sect;6", "an8.1:6.1-6.4"),
        ("p", "&sect;7", "an8.1:7.1-7.4"),
    ],
    quiz=[
        {"q": "How does this discourse open, and what does it lend to its "
              "chapter?",
         "opts": [
             "With a bare formula and no setting, unlike the chapter it opens",
             "With the full traditional frame at Sāvatthī, and it lends its own "
             "subject — love (mettā) — to the chapter's name, Mettāvagga",
             "With a dialogue between two mendicants",
             "With a deity's visit"],
         "correct": 1,
         "expl": "The full opening formula, and this chapter's own namesake."},
        {"q": "What eight benefits follow from a heart's release cultivated by "
              "love?",
         "opts": [
             "Wealth, fame, long life, and four more worldly gains",
             "Untroubled sleep and waking, no bad dreams, the love of humans "
             "and non-humans, protection by deities, immunity to fire, poison, "
             "and blade, and rebirth in a realm of divinity",
             "The seven factors of awakening plus one more",
             "Freedom from all five hindrances"],
         "correct": 1,
         "expl": "A list of practical and personal benefits, entirely positive."},
        {"q": "According to the guide, how does this discourse's eight-item "
              "list differ in shape from the Sixes' and Sevens' opening lists?",
         "opts": [
             "It has no numbered list at all",
             "It is entirely positive, with no blocking list and reversal — "
             "unlike the paired lists that opened the Sixes and Sevens",
             "It is identical in every respect",
             "It lists eight kinds of wrong view"],
         "correct": 1,
         "expl": "A single positive list, not a blocking-and-reversal pair."},
        {"q": "What do the closing verses compare a mind developed with love "
              "to?",
         "opts": [
             "A lotus rising above the water",
             "A conquering king's greatest royal sacrifices — found worth less "
             "than a sixteenth part",
             "A raft for crossing a flood",
             "A well-tuned lute"],
         "correct": 1,
         "expl": "Royal sacrifice, and the moon-versus-stars simile that follows it."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "No setting is given"],
         "correct": 1,
         "expl": "The standard opening setting for a new nipāta's first discourse."},
        {"q": "What is <em>cetovimutti</em>, the attainment this discourse "
              "describes love as producing?",
         "opts": ["A physical posture", "A heart's release", "A monastic robe",
                   "A type of alms bowl"],
         "correct": 1,
         "expl": "The meditative attainment love is said to produce when fully "
                 "cultivated."},
    ],
    marginalia=[
        ("Eight benefits of love", [
            "ease in sleep, waking —",
            "loved by seen and unseen —",
            "safe from fire, poison, blade",
        ]),
        ("This chapter's own name", [
            "mettā gives its name",
            "to Mettāvagga —",
            "the chapter it opens"],
        ),
        ("Worth more than royal sacrifice", [
            "not a sixteenth part",
            "of a mind grown in love —",
            "as stars to the moon's light",
        ]),
        ("Cross-references", [
            "AN 7.645&ndash;1124 &middot; previous nipāta, closing the Sevens",
            "AN 8.2 &middot; next, wisdom's own eight causes",
        ]),
    ],
    further=[
        '<a href="%s/an8.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-7.645-1124.html">AN 7.645&ndash;1124 &middot; Untitled Discourses on '
        "Hate, Etc.</a> &mdash; previous, closing the Sevens.",
        '<a href="an-8.2.html">AN 8.2 &middot; Wisdom</a> &mdash; next, eight causes for '
        "acquiring wisdom.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.2 — Paññāsutta
# --------------------------------------------------------------------------- #
page(
    2, "Paññā", "Wisdom",
    vagga=VAGGA_1,
    meta_title="AN 8.2 — Wisdom | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paññāsutta, on the eight causes and reasons that lead to acquiring "
        "the wisdom fundamental to the spiritual life. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "An eight-item list of causes, then the same eight repeated as "
                 "reasons spiritual companions come to esteem the one who keeps "
                 "them, the second half compressed by internal peyyāla"),
        ("Length", "~2 minutes to read"),
        ("An internal peyyāla", "Items 2 and 8 of the second half are compressed "
                                "with an ellipsis in the source rather than "
                                "restated in full &mdash; the same self-"
                                "abbreviation pattern already met at AN 7.49 and "
                                "AN 7.52, handled the same simple way: the spec "
                                "range is cut normally and the empty segments "
                                "render as nothing extra"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear "
                       "eight-item list, doubled by a second half that mostly "
                       "just re-praises the same eight"),
    ],
    why=(
        "AN 8.2 names eight causes and reasons for acquiring the wisdom "
        "fundamental to the spiritual life &mdash; relying on a teacher, asking "
        "questions, withdrawing body and mind, ethical conduct, deep learning, "
        "roused energy, right speech in the Saṅgha, and meditating on the rise "
        "and fall of the five grasping aggregates &mdash; then shows how each of "
        "these same eight also wins a mendicant their companions' fondness, "
        "respect, and esteem."),
    guide=[
        ("The teaching in one sentence", [
            "Eight causes and reasons lead to acquiring, and then to increasing "
            "and fully developing, the wisdom fundamental to the spiritual "
            "life &mdash; and each of these same eight causes also leads to "
            "fondness, respect, esteem, harmony, and unity among one's "
            "spiritual companions."]),
        ("The eight causes of wisdom", [
            "Relying on a teacher or senior companion with conscience and "
            "respect; asking that teacher questions; perfecting withdrawal of "
            "body and mind after hearing the teaching; ethical restraint under "
            "the monastic code; deep learning of the teachings; roused energy "
            "for abandoning the unskillful and cultivating the skillful; "
            "speaking only Dhamma or keeping noble silence in the Saṅgha; and "
            "meditating on the rise and fall of the five grasping aggregates."]),
        ("The same eight, restated as reasons for esteem", [
            "Having listed the eight causes of wisdom in full, the discourse "
            "then runs through all eight again, this time framed as what "
            "spiritual companions say in praise of the one who keeps them: "
            "&ldquo;clearly this venerable knows and sees.&rdquo; Two of the "
            "eight restatements are compressed by the source's own internal "
            "ellipsis rather than spelled out a second time."]),
        ("Wisdom and belonging, tied to the same causes", [
            "The discourse's structure makes a quiet claim: the very causes "
            "that build the wisdom fundamental to the spiritual life are not "
            "separate from what earns a mendicant their companions' respect "
            "and harmony. The two outcomes &mdash; inner development and "
            "social standing &mdash; grow from an identical eightfold root."]),
    ],
    terms=[
        ("paññā mūlikā brahmacariyikā",
         "&ldquo;the wisdom fundamental to the spiritual life&rdquo; &mdash; "
         "this discourse's own subject and title."),
        ("satthari vā viharati sabrahmacārīsu vā garuṭṭhāniye",
         "&ldquo;lives relying on the Teacher or a spiritual companion in a "
         "teacher's role&rdquo; &mdash; the first and most repeated of the "
         "eight causes, anchoring the rest."),
        ("kaṅkhāṭhāniyesu dhammesu kaṅkhaṁ paṭivinodenti",
         "&ldquo;dispel doubt regarding the many doubtful matters&rdquo; "
         "&mdash; part of the second cause, what a teacher does when asked."),
        ("udayabbayānupassī pañcasu upādānakkhandhesu",
         "&ldquo;meditate observing rise and fall in the five grasping "
         "aggregates&rdquo; &mdash; the eighth and final cause, closing the "
         "list with direct insight practice."),
        ("pemanīyo hoti garu bhāvanīyo saṅgahako samaggakaraṇo",
         "&ldquo;leads to fondness, respect, esteem, harmony, and unity&rdquo; "
         "&mdash; the closing refrain attached to each of the eight when "
         "restated as reasons for a spiritual companion's esteem."),
    ],
    text_intro=(
        "The discourse in full: eight causes of wisdom, then the same eight "
        "restated as reasons for a spiritual companion's esteem. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first four causes"),
        ("p", "&sect;1", "an8.2:1.1-4.2"),
        ("h3", "The fifth through eighth causes"),
        ("p", "&sect;2", "an8.2:5.1-8.7"),
        ("h3", "The same eight, restated as reasons for esteem"),
        ("p", "&sect;3", "an8.2:9.1-17.1"),
    ],
    quiz=[
        {"q": "What is this discourse's subject, named in its own title?",
         "opts": [
             "Generosity", "The wisdom fundamental to the spiritual life",
             "Right speech", "Monastic discipline alone"],
         "correct": 1,
         "expl": "Paññā mūlikā brahmacariyikā, this discourse's title-phrase."},
        {"q": "What is the first of the eight causes for acquiring this "
              "wisdom?",
         "opts": [
             "Living alone in the forest",
             "Living relying on the Teacher or a spiritual companion in a "
             "teacher's role, with conscience and respect for them",
             "Fasting for long periods",
             "Memorizing the entire monastic code"],
         "correct": 1,
         "expl": "The first cause, anchoring the seven that follow."},
        {"q": "What does the discourse do with the same eight causes in its "
              "second half?",
         "opts": [
             "Discards them and lists eight new ones",
             "Restates each as a reason spiritual companions come to esteem "
             "the one who keeps it — 'clearly this venerable knows and sees'",
             "Contradicts the first list entirely",
             "Turns them into a set of prohibitions"],
         "correct": 1,
         "expl": "The identical eight, reframed as grounds for a companion's "
                 "esteem."},
        {"q": "What happens to two of the eight restatements in the source "
              "text's second half?",
         "opts": [
             "They are expanded with new detail",
             "They are compressed by an internal ellipsis rather than spelled "
             "out again in full — the same pattern met before at AN 7.49",
             "They are removed entirely",
             "They are moved to a separate discourse"],
         "correct": 1,
         "expl": "An internal peyyāla, handled the same simple way as before."},
        {"q": "What is the eighth and final cause of wisdom?",
         "opts": [
             "Giving generously to the Saṅgha",
             "Meditating observing rise and fall in the five grasping "
             "aggregates",
             "Reciting the monastic code twice monthly",
             "Traveling to holy sites"],
         "correct": 1,
         "expl": "Direct insight practice, closing the list of eight causes."},
        {"q": "According to the guide, what quiet claim does this discourse's "
              "structure make?",
         "opts": [
             "Wisdom and social standing are unrelated",
             "The same eight causes that build fundamental wisdom also earn a "
             "mendicant their companions' respect and harmony",
             "Only ordained teachers can develop wisdom",
             "Wisdom requires isolation from all companions"],
         "correct": 1,
         "expl": "Inner development and social standing, grown from an "
                 "identical eightfold root."},
    ],
    marginalia=[
        ("Eight causes of wisdom", [
            "relying on a teacher —",
            "learning, energy, restraint —",
            "watching the aggregates rise and fall",
        ]),
        ("The same eight, twice", [
            "praised a second time",
            "as what earns esteem —",
            "two items cut by ellipsis",
        ]),
        ("Wisdom and belonging", [
            "one eightfold root grows",
            "both insight and standing —",
            "not two separate paths",
        ]),
        ("Cross-references", [
            "AN 8.1 &middot; previous, love's own eight benefits",
            "AN 8.3 &middot; next, what makes a mendicant liked or disliked",
        ]),
    ],
    further=[
        '<a href="%s/an8.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.1.html">AN 8.1 &middot; The Benefits of Love</a> &mdash; previous.',
        '<a href="an-8.3.html">AN 8.3 &middot; Disliked (1st)</a> &mdash; next, an eightfold '
        "return to the blocking-and-reversal shape.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.3 — Paṭhamaappiyasutta
# --------------------------------------------------------------------------- #
page(
    3, "Paṭhamaappiya", "Disliked (1st)",
    vagga=VAGGA_1,
    meta_title="AN 8.3 — Disliked (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaappiyasutta, an eight-item blocking list and its direct "
        "reversal on what makes a mendicant disliked or liked by their "
        "spiritual companions. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched eight-item lists, cause and its direct reversal, in "
                 "the bare formula familiar from AN 7.1"),
        ("Length", "under 1 minute to read"),
        ("The same shape, one item longer", "AN 7.1 opened the Sevens with an "
                                            "identical structure at seven items; "
                                            "this discourse runs the same "
                                            "blocking-and-reversal shape at eight, "
                                            "the Eights' own numerical theme"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "formulaic, no setting given"),
    ],
    why=(
        "AN 8.3 gives eight qualities that make a mendicant disliked by their "
        "spiritual companions &mdash; praising the disliked, criticizing the "
        "liked, desiring material things and honor, lacking conscience and "
        "prudence, and having corrupt wishes and wrong view &mdash; and their "
        "eight direct reversals, which make one liked."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who praises the disliked and criticizes the liked, "
            "desires material things and honor, lacks conscience and prudence, "
            "and has corrupt wishes and wrong view is disliked by their "
            "spiritual companions; the eight direct opposites make a mendicant "
            "liked."]),
        ("AN 7.1's shape, now at eight", [
            "This discourse reruns the exact structure that opened the Sevens "
            "at AN 7.1: a bare blocking list matched by its point-for-point "
            "reversal, no setting given. What changes is only the count, now "
            "eight items instead of seven, this book's own numerical theme."]),
        ("Praise and blame toward others, named first", [
            "Where AN 7.1's blocking list opened with desire for material "
            "things, this one opens with something more social still: praising "
            "whoever is disliked and criticizing whoever is liked &mdash; "
            "a contrarian reflex named before desire, conscience, or view are "
            "even mentioned."]),
        ("Eight items in four matched pairs", [
            "The Pāli names eight distinct terms, falling into four natural "
            "pairs: praising-the-disliked and criticizing-the-liked; desiring "
            "material things and desiring honor; lacking conscience and "
            "lacking prudence; corrupt wishes and wrong view. Each pair reverses "
            "cleanly in the second list."]),
    ],
    terms=[
        ("appiyapasaṁsī, piyagarahī",
         "&ldquo;praises the disliked, criticizes the liked&rdquo; &mdash; the "
         "first pair of the blocking list, a contrarian reflex named before "
         "any of the other seven items."),
        ("lābhakāmo, sakkārakāmo",
         "&ldquo;desires material things, desires honor&rdquo; &mdash; the "
         "second pair, echoing (but not fully repeating) the three-item "
         "opening of AN 7.1's own blocking list."),
        ("ahiriko, anottappī",
         "&ldquo;lacks conscience, lacks prudence&rdquo; &mdash; the third "
         "pair, terms already familiar from the Sixes and Sevens."),
        ("pāpiccho, micchādiṭṭhi",
         "&ldquo;corrupt wishes, wrong view&rdquo; &mdash; the fourth and "
         "final pair, closing the blocking list exactly as it closed AN 7.1's."),
        ("appiyo, piyo",
         "&ldquo;disliked, liked&rdquo; &mdash; this discourse's own title "
         "term and its reversal, the outcome the two eight-item lists are said "
         "to produce."),
    ],
    text_intro=(
        "The discourse in full: eight qualities that make a mendicant disliked, "
        "and their eight reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight qualities that make a mendicant disliked"),
        ("p", "&sect;1", "an8.3:1.1-1.4"),
        ("h3", "Eight qualities that make a mendicant liked"),
        ("p", "&sect;2", "an8.3:2.1-2.4"),
    ],
    quiz=[
        {"q": "What structure does this discourse share with AN 7.1, the "
              "opening discourse of the Sevens?",
         "opts": [
             "No relation at all",
             "The same bare blocking-list-and-reversal shape, now run at eight "
             "items instead of seven",
             "Both are set at Rājagaha",
             "Both feature a deity's visit"],
         "correct": 1,
         "expl": "The identical shape, one item longer, matching this book's "
                 "numerical theme."},
        {"q": "What is named first in this discourse's blocking list, before "
              "desire, conscience, or view?",
         "opts": [
             "Physical violence",
             "Praising whoever is disliked and criticizing whoever is liked",
             "Breaking a specific precept",
             "Refusing to teach"],
         "correct": 1,
         "expl": "A contrarian social reflex, named before the other seven "
                 "items."},
        {"q": "How do the eight items fall, according to the guide?",
         "opts": [
             "Eight unrelated items with no grouping",
             "Four matched pairs: praise/blame, material desire, lack of "
             "conscience/prudence, and corrupt wishes/wrong view",
             "Two groups of four unrelated items",
             "A single continuous list with no internal structure"],
         "correct": 1,
         "expl": "Four natural pairs, each reversing cleanly in the second "
                 "list."},
        {"q": "What quality closes both the blocking list and its reversal?",
         "opts": [
             "Wealth and poverty", "Corrupt wishes and wrong view, reversed to "
                                    "few desires and right view",
             "Physical strength", "Skill in debate"],
         "correct": 1,
         "expl": "The same closing pair AN 7.1 used, now in an eight-item list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, in the Himalayas"],
         "correct": 2,
         "expl": "A bare formula, matching AN 7.1's own lack of a restated "
                 "setting."},
        {"q": "What does this discourse's own title term, <em>appiyo</em>, "
              "mean?",
         "opts": ["Liked", "Disliked", "Wealthy", "Ordained"],
         "correct": 1,
         "expl": "The outcome the first eight-item list is said to produce; "
                 "its reversal, piyo, closes the second."},
    ],
    marginalia=[
        ("Eight qualities disliked", [
            "praising the disliked,",
            "blaming the liked — desire,",
            "no conscience, corrupt wishes, wrong view",
        ]),
        ("AN 7.1's shape, at eight", [
            "the same bare formula",
            "that opened the Sevens,",
            "now one item longer",
        ]),
        ("Four matched pairs", [
            "praise/blame, desire,",
            "conscience/prudence, wishes/view —",
            "each reversing cleanly",
        ]),
        ("Cross-references", [
            "AN 8.2 &middot; previous, wisdom's eight causes",
            "AN 8.4 &middot; next, a second disliked/liked pair with different "
            "items",
        ]),
    ],
    further=[
        '<a href="%s/an8.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.2.html">AN 8.2 &middot; Wisdom</a> &mdash; previous.',
        '<a href="an-8.4.html">AN 8.4 &middot; Disliked (2nd)</a> &mdash; next, the same '
        "theme with a different eight items.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.4 — Dutiyaappiyasutta
# --------------------------------------------------------------------------- #
page(
    4, "Dutiyaappiya", "Disliked (2nd)",
    vagga=VAGGA_1,
    meta_title="AN 8.4 — Disliked (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaappiyasutta, a second eight-item blocking list and its reversal "
        "on what makes a mendicant disliked or liked, sharing its opening "
        "three items with AN 7.1. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A second matched pair of eight-item lists, same bare formula as "
                 "AN 8.3, different items"),
        ("Length", "under 1 minute to read"),
        ("A callback to AN 7.1", "This list's own opening three items &mdash; "
                                 "desiring material things, honor, and status "
                                 "&mdash; are the identical Pāli terms that "
                                 "opened AN 7.1's blocking list a full nipāta "
                                 "earlier, though the five items that follow are "
                                 "entirely different"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "formulaic, no setting given"),
    ],
    why=(
        "AN 8.4 gives a second eight-item list of what makes a mendicant "
        "disliked &mdash; desiring material things, honor, and status, not "
        "knowing moderation or the proper time, impure conduct, talking too "
        "much, and insulting one's companions &mdash; and its direct reversal, "
        "sharing its opening three terms with the very first discourse of the "
        "Sevens."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who desires material things, honor, and status, knows "
            "neither moderation nor the proper time, has impure conduct, talks "
            "a lot, and insults and abuses their spiritual companions is "
            "disliked; the eight direct opposites make a mendicant liked."]),
        ("A paired discourse, not a repeat", [
            "This is the second of a Paṭhama/Dutiya pair with AN 8.3, following "
            "a pattern this project has met many times before: the same bare "
            "formula and structure, but a genuinely different eight items, not "
            "a restatement of the first discourse's list."]),
        ("The same three opening terms as AN 7.1", [
            "This list's first three items &mdash; <em>lābhakāmo, sakkārakāmo, "
            "anavaññattikāmo</em>, desiring material things, honor, and status "
            "&mdash; are word-for-word the same three that opened the very "
            "first discourse of the Sevens. What follows them here is entirely "
            "different: not conscience, prudence, wishes, and view, but "
            "moderation, timing, purity of conduct, restraint in speech, and "
            "abstaining from insult."]),
        ("A more social, less doctrinal list than AN 8.3's", [
            "Where AN 8.3's blocking list leaned toward inner disposition "
            "&mdash; conscience, wishes, view &mdash; this one leans toward "
            "observable conduct in community: knowing when and how much, "
            "keeping bodily and verbal conduct clean, and not talking too much "
            "or abusing one's companions."]),
    ],
    terms=[
        ("lābhakāmo, sakkārakāmo, anavaññattikāmo",
         "&ldquo;desires material things, honor, and status&rdquo; &mdash; the "
         "first three items, identical in Pāli to the opening of AN 7.1's own "
         "blocking list."),
        ("akālaññū, amattaññū",
         "&ldquo;knows neither the proper time nor moderation&rdquo; &mdash; "
         "the fourth and fifth items, naming a failure of social and practical "
         "judgment."),
        ("asuci",
         "&ldquo;impure&rdquo; &mdash; the sixth item, describing conduct "
         "rather than an inner state."),
        ("bahubhāṇī",
         "&ldquo;talks a lot&rdquo; &mdash; the seventh item, a fault of "
         "excess in speech."),
        ("akkosakaparibhāsako sabrahmacārīnaṁ",
         "&ldquo;insults and abuses their spiritual companions&rdquo; &mdash; "
         "the eighth and closing item, the most directly harmful of the eight."),
    ],
    text_intro=(
        "The discourse in full: a second eight-item list of what makes a "
        "mendicant disliked, and its reversal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight qualities that make a mendicant disliked"),
        ("p", "&sect;1", "an8.4:1.1-1.4"),
        ("h3", "Eight qualities that make a mendicant liked"),
        ("p", "&sect;2", "an8.4:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse relate to AN 8.3, the discourse before "
              "it?",
         "opts": [
             "It repeats AN 8.3's list word for word",
             "It is the second of a Paṭhama/Dutiya pair — the same bare formula "
             "and structure, but a genuinely different eight items",
             "It contradicts AN 8.3 entirely",
             "It has no relation to AN 8.3"],
         "correct": 1,
         "expl": "A familiar paired-discourse pattern, not a restatement."},
        {"q": "What do this list's opening three items share with AN 7.1, the "
              "first discourse of the Sevens?",
         "opts": [
             "Nothing — they are entirely different",
             "They are the identical Pāli terms — desiring material things, "
             "honor, and status",
             "Only the general theme, not the exact wording",
             "AN 7.1 has no opening items at all"],
         "correct": 1,
         "expl": "A word-for-word callback across two different nipātas."},
        {"q": "According to the guide, how does this list's character differ "
              "from AN 8.3's?",
         "opts": [
             "They are identical in every respect",
             "AN 8.4 leans toward observable conduct in community — timing, "
             "purity, speech — where AN 8.3 leaned toward inner disposition",
             "AN 8.4 has no reversal list at all",
             "AN 8.3 is entirely about physical conduct"],
         "correct": 1,
         "expl": "A more social, less doctrinal list than its predecessor."},
        {"q": "What is the eighth and closing item of this blocking list?",
         "opts": [
             "Wrong view", "Insulting and abusing one's spiritual companions",
             "Excessive fasting", "Refusing all almsfood"],
         "correct": 1,
         "expl": "The most directly harmful of the eight, closing the list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Campā",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.3's own lack of a restated "
                 "setting."},
        {"q": "What does <em>akālaññū, amattaññū</em> mean?",
         "opts": [
             "Physically strong and healthy",
             "Knows neither the proper time nor moderation",
             "Wealthy and well-connected", "Skilled in debate"],
         "correct": 1,
         "expl": "The fourth and fifth items, naming a failure of practical "
                 "judgment."},
    ],
    marginalia=[
        ("Eight qualities disliked, again", [
            "desire, no timing,",
            "impure, talks too much —",
            "insults their own companions",
        ]),
        ("AN 7.1's opening, reused", [
            "the same three Pāli words",
            "that began the Sevens —",
            "then eight new items follow",
        ]),
        ("Conduct, not disposition", [
            "a more social list",
            "than AN 8.3's own —",
            "timing, purity, speech",
        ]),
        ("Cross-references", [
            "AN 8.3 &middot; previous, the first disliked/liked pair",
            "AN 8.5 &middot; next, the eight worldly conditions",
        ]),
    ],
    further=[
        '<a href="%s/an8.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.3.html">AN 8.3 &middot; Disliked (1st)</a> &mdash; previous.',
        '<a href="an-8.5.html">AN 8.5 &middot; Worldly Conditions (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.5 — Paṭhamalokadhammasutta
# --------------------------------------------------------------------------- #
page(
    5, "Paṭhamalokadhamma", "Worldly Conditions (1st)",
    vagga=VAGGA_1,
    meta_title="AN 8.5 — Worldly Conditions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamalokadhammasutta, the brief version of one of the tradition's "
        "best-known teachings: the eight worldly winds of gain and loss, fame "
        "and disgrace, blame and praise, pleasure and pain. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item list in four opposed pairs, followed by two "
                 "verses on how a wise person meets them"),
        ("Length", "under 1 minute to read"),
        ("One of the tradition's best-known teachings", "The eight worldly "
                                                         "conditions (<em>aṭṭha "
                                                         "lokadhammā</em>) named "
                                                         "here are among the most "
                                                         "widely cited teachings "
                                                         "in this literature, "
                                                         "recurring across many "
                                                         "genres and settings "
                                                         "beyond this pair of "
                                                         "discourses"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "purely descriptive, no blocking-and-reversal shape this "
                       "time"),
    ],
    why=(
        "AN 8.5 names the eight worldly conditions that revolve around the "
        "world &mdash; gain and loss, fame and disgrace, blame and praise, "
        "pleasure and pain &mdash; as impermanent and perishable, then closes "
        "with two verses on how an intelligent, mindful person meets them "
        "without being disturbed by the desirable or repelled by the "
        "undesirable."),
    guide=[
        ("The teaching in one sentence", [
            "The eight worldly conditions &mdash; gain and loss, fame and "
            "disgrace, blame and praise, pleasure and pain &mdash; revolve "
            "around the world just as the world revolves around them; they are "
            "impermanent and perishable, and the wise meet them without being "
            "disturbed."]),
        ("Four pairs, not a blocking-and-reversal list", [
            "Unlike most of this chapter's discourses so far, this one is not "
            "structured as a blocking list matched by its reversal. It simply "
            "names four pairs of opposites &mdash; gain/loss, fame/disgrace, "
            "blame/praise, pleasure/pain &mdash; as the fixed conditions every "
            "being in the world encounters."]),
        ("Encountered by everyone, met differently", [
            "The discourse doesn't claim the eight worldly conditions can be "
            "avoided. Its closing verses instead describe how a person who "
            "understands their impermanent, perishable nature meets them: "
            "undisturbed by what's desirable, unrepelled by what's "
            "undesirable, with both favoring and opposing cleared away."]),
        ("The brief half of a matched pair", [
            "This is the first of two discourses on the same eight "
            "conditions, following this chapter's established Paṭhama/Dutiya "
            "pattern. AN 8.6, immediately following, expands the same "
            "material with a full dialogue and detailed contrast between "
            "learned and unlearned responses."]),
    ],
    terms=[
        ("aṭṭha lokadhammā",
         "&ldquo;the eight worldly conditions&rdquo; &mdash; this discourse's "
         "own title-phrase, and one of the most widely cited short lists in "
         "the tradition."),
        ("lābho ca alābho ca, yaso ca ayaso ca",
         "&ldquo;gain and loss, fame and disgrace&rdquo; &mdash; the first two "
         "of the four opposed pairs."),
        ("nindā ca pasaṁsā ca, sukhañca dukkhañca",
         "&ldquo;blame and praise, pleasure and pain&rdquo; &mdash; the third "
         "and fourth pairs, closing the list of eight."),
        ("aniccā, addhuvā, vipariṇāmadhammā",
         "&ldquo;impermanent, transient, and perishable&rdquo; &mdash; the "
         "verses' own description of all eight conditions, the basis for how "
         "a wise person is said to meet them."),
        ("nābhijjhā na paṭighā",
         "&ldquo;not disturbed by the desirable, nor repelled by the "
         "undesirable&rdquo; &mdash; the intelligent, mindful person's "
         "response, described in the closing verses."),
    ],
    text_intro=(
        "The discourse in full: the eight worldly conditions, and two verses "
        "on how the wise meet them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The eight worldly conditions"),
        ("p", "&sect;1", "an8.5:1.1-1.4"),
        ("h3", "Verses: impermanent, and met by the wise"),
        ("p", "&sect;2", "an8.5:2.1-2.4"),
        ("p", "&sect;3", "an8.5:3.1-3.4"),
        ("p", "&sect;4", "an8.5:4.1-4.4"),
    ],
    quiz=[
        {"q": "What are the eight worldly conditions named in this discourse?",
         "opts": [
             "The five hindrances plus three more",
             "Gain and loss, fame and disgrace, blame and praise, pleasure and "
             "pain",
             "The seven factors of awakening plus one",
             "Birth, aging, illness, and death, doubled"],
         "correct": 1,
         "expl": "Four opposed pairs, among the tradition's most widely cited "
                 "short lists."},
        {"q": "How is this discourse structured, compared to most of this "
              "chapter's earlier discourses?",
         "opts": [
             "As a blocking list matched by its exact reversal",
             "As a bare naming of four pairs of opposites, not a "
             "blocking-and-reversal structure",
             "As a long narrative with multiple characters",
             "As a set of monastic rules"],
         "correct": 1,
         "expl": "Four fixed pairs every being encounters, not a blocking list."},
        {"q": "According to the closing verses, how does an intelligent, "
              "mindful person meet the eight worldly conditions?",
         "opts": [
             "By avoiding them entirely",
             "Undisturbed by the desirable, unrepelled by the undesirable, "
             "with favoring and opposing both cleared away",
             "By actively pursuing gain, fame, and praise",
             "By ignoring the teaching altogether"],
         "correct": 1,
         "expl": "Not avoidance, but an undisturbed relationship to conditions "
                 "everyone encounters."},
        {"q": "What quality do the verses attribute to all eight worldly "
              "conditions?",
         "opts": [
             "They are permanent and unchanging",
             "They are impermanent, transient, and perishable",
             "They apply only to monastics",
             "They can be permanently escaped through ritual"],
         "correct": 1,
         "expl": "Their impermanent nature is the basis for the wise person's "
                 "undisturbed response."},
        {"q": "How does this discourse relate to AN 8.6, which follows it?",
         "opts": [
             "No relation at all",
             "It is the brief half of a matched pair — AN 8.6 expands the "
             "same eight conditions with a full dialogue",
             "AN 8.6 contradicts this discourse",
             "AN 8.6 is set centuries later"],
         "correct": 1,
         "expl": "A Paṭhama/Dutiya pair, brief followed by detailed."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, like several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("The eight worldly winds", [
            "gain, loss · fame, shame ·",
            "blame, praise · pleasure, pain —",
            "impermanent, all of them",
        ]),
        ("Not blocking and reversal", [
            "four pairs simply named,",
            "not a list to overcome —",
            "conditions everyone meets",
        ]),
        ("Undisturbed, not escaping", [
            "not avoiding gain or loss",
            "but meeting both unmoved —",
            "favoring and opposing cleared",
        ]),
        ("Cross-references", [
            "AN 8.4 &middot; previous, a second disliked/liked pair",
            "AN 8.6 &middot; next, the same eight conditions in full dialogue",
        ]),
    ],
    further=[
        '<a href="%s/an8.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.4.html">AN 8.4 &middot; Disliked (2nd)</a> &mdash; previous.',
        '<a href="an-8.6.html">AN 8.6 &middot; Worldly Conditions (2nd)</a> &mdash; next, the '
        "same eight conditions, expanded.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.6 — Dutiyalokadhammasutta
# --------------------------------------------------------------------------- #
page(
    6, "Dutiyalokadhamma", "Worldly Conditions (2nd)",
    vagga=VAGGA_1,
    meta_title="AN 8.6 — Worldly Conditions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyalokadhammasutta, the expanded version of the eight worldly "
        "conditions, contrasting how a learned noble disciple and an "
        "unlearned ordinary person each encounter gain, loss, fame, disgrace, "
        "blame, praise, pleasure, and pain. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, prompted by the mendicants' own request for "
                     "clarification"),
        ("Form", "A dialogue opening, then a doubled explanation running the "
                 "same eight conditions once for the unlearned ordinary person "
                 "and once for the learned noble disciple, closing with the "
                 "same two verses as AN 8.5"),
        ("Length", "~3 minutes to read"),
        ("Not a repeat of AN 8.5", "This discourse names the identical eight "
                                   "worldly conditions as AN 8.5, but its real "
                                   "content is new: a full explanation of what "
                                   "actually distinguishes a learned response "
                                   "from an unlearned one"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; longer than "
                       "its brief companion, but the doubled structure repeats "
                       "predictably once its shape is seen"),
    ],
    why=(
        "AN 8.6 expands AN 8.5's bare list of the eight worldly conditions "
        "into a full teaching: an unlearned ordinary person encounters gain, "
        "loss, fame, disgrace, blame, praise, pleasure, and pain without "
        "reflecting on their impermanent, perishable nature, so favoring and "
        "opposing occupy their mind and they remain unfree from suffering; a "
        "learned noble disciple reflects on each as it arises, and is freed."),
    guide=[
        ("The teaching in one sentence", [
            "The difference between a learned noble disciple and an unlearned "
            "ordinary person facing the same eight worldly conditions is not "
            "whether they encounter gain, loss, fame, disgrace, blame, praise, "
            "pleasure, and pain &mdash; both do &mdash; but whether they "
            "reflect on each as impermanent, suffering, and perishable when it "
            "arises."]),
        ("A question the mendicants themselves ask", [
            "Unusually for this chapter, the discourse opens with the Buddha "
            "posing a question directly to the mendicants &mdash; both kinds "
            "of person encounter the same eight conditions, so what "
            "distinguishes them? &mdash; and the mendicants formally request "
            "him to explain, invoking their own teachings as rooted in the "
            "Buddha."]),
        ("The unlearned response: no reflection, and its cost", [
            "The ordinary person encounters each of the eight without "
            "reflecting: &ldquo;I've encountered this gain (or pain); it's "
            "impermanent, suffering, and perishable.&rdquo; Left unreflected "
            "on, the eight conditions occupy their mind, and they favor the "
            "desirable half of each pair while opposing its undesirable "
            "counterpart &mdash; leaving them, the discourse says, unfree "
            "from suffering."]),
        ("The learned response: the identical formula, reflected on", [
            "The learned noble disciple meets the same eight conditions with "
            "exactly the same reflection each time it arises. Because the "
            "conditions no longer occupy an unreflective mind, favoring and "
            "opposing don't take hold, and the discourse says such a person is "
            "freed from suffering. The closing verses are word-for-word "
            "identical to AN 8.5's."]),
    ],
    terms=[
        ("assutavā puthujjano",
         "&ldquo;an unlearned ordinary person&rdquo; &mdash; one pole of this "
         "discourse's central contrast, who meets the eight conditions "
         "without reflection."),
        ("sutavā ariyasāvako",
         "&ldquo;a learned noble disciple&rdquo; &mdash; the other pole, who "
         "reflects on each condition as it arises."),
        ("&lsquo;laddhaṁ kho myāyaṁ lābho, so ca kho anicco dukkho "
         "vipariṇāmadhammo&rsquo;ti yathābhūtaṁ nappajānāti",
         "&ldquo;they don't truly understand: &lsquo;I've encountered this "
         "gain; it's impermanent, suffering, and perishable&rsquo;&rdquo; "
         "&mdash; the unlearned person's failure, repeated across all eight "
         "conditions in the source's own internal ellipsis."),
        ("anurujjhati, paṭivirujjhati",
         "&ldquo;favors, opposes&rdquo; &mdash; the pair of reactions that "
         "occupy an unreflective mind, and that the learned disciple's "
         "reflection prevents from taking hold."),
        ("parimuccati dukkhasmāti vadāmi",
         "&ldquo;they are freed from suffering, I say&rdquo; &mdash; the "
         "Buddha's own closing claim about the learned noble disciple, "
         "mirrored by its negative about the unlearned ordinary person."),
    ],
    text_intro=(
        "The discourse in full: a question about the eight worldly conditions, "
        "and the doubled explanation that answers it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The question, and the request to explain it"),
        ("p", "&sect;1", "an8.6:1.1-3.3"),
        ("h3", "The unlearned ordinary person"),
        ("p", "&sect;2", "an8.6:3.4-4.7"),
        ("h3", "The learned noble disciple"),
        ("p", "&sect;3", "an8.6:5.1-6.8"),
        ("h3", "Verses: impermanent, and met by the wise"),
        ("p", "&sect;4", "an8.6:7.1-7.4"),
        ("p", "&sect;5", "an8.6:8.1-8.4"),
        ("p", "&sect;6", "an8.6:9.1-9.4"),
    ],
    quiz=[
        {"q": "According to this discourse, what actually distinguishes a "
              "learned noble disciple from an unlearned ordinary person?",
         "opts": [
             "The noble disciple never encounters the eight worldly "
             "conditions at all",
             "Both encounter the same eight conditions, but the noble "
             "disciple reflects on each as impermanent, suffering, and "
             "perishable as it arises",
             "The noble disciple is wealthier",
             "There is no real difference between them"],
         "correct": 1,
         "expl": "Reflection on impermanence, not escape from the conditions "
                 "themselves."},
        {"q": "How does this discourse open, compared to most discourses in "
              "this chapter?",
         "opts": [
             "With a bare formula and no dialogue",
             "With the Buddha posing a question directly, and the mendicants "
             "formally requesting him to explain it",
             "With a deity's visit",
             "With a narrative about Devadatta"],
         "correct": 1,
         "expl": "An unusually dialogic opening for this chapter."},
        {"q": "What happens to the unlearned ordinary person who doesn't "
              "reflect on the eight conditions?",
         "opts": [
             "Nothing; the conditions have no effect either way",
             "The conditions occupy their mind — they favor the desirable "
             "half of each pair and oppose the undesirable, remaining unfree "
             "from suffering",
             "They immediately attain awakening",
             "They become a noble disciple automatically"],
         "correct": 1,
         "expl": "Unreflected-on conditions drive favoring and opposing, and "
                 "leave suffering unresolved."},
        {"q": "How do this discourse's closing verses compare to AN 8.5's?",
         "opts": [
             "Completely different verses",
             "Word-for-word identical",
             "AN 8.5 has no verses at all",
             "Only the first line matches"],
         "correct": 1,
         "expl": "The same closing verses, shared by both discourses in this "
                 "pair."},
        {"q": "What are the eight worldly conditions named in both this "
              "discourse and AN 8.5?",
         "opts": [
             "The five hindrances plus three more",
             "Gain and loss, fame and disgrace, blame and praise, pleasure "
             "and pain",
             "The seven factors of awakening plus one",
             "The four noble truths, doubled"],
         "correct": 1,
         "expl": "The identical eight conditions as AN 8.5's brief version."},
        {"q": "What does the reflection <em>'it's impermanent, suffering, "
              "and perishable'</em> apply to, in this discourse?",
         "opts": [
             "Only pleasant conditions like gain and praise",
             "Each of the eight worldly conditions individually, as it arises",
             "Only unpleasant conditions like loss and blame",
             "The Buddha's teaching itself"],
         "correct": 1,
         "expl": "Applied uniformly to all eight, whether desirable or "
                 "undesirable."},
    ],
    marginalia=[
        ("Same eight, doubled response", [
            "unlearned: no reflection,",
            "favoring, opposing, bound —",
            "learned: reflects, and is freed",
        ]),
        ("A question, formally asked", [
            "the mendicants themselves",
            "request the explanation —",
            "an unusually dialogic open",
        ]),
        ("Identical closing verses", [
            "the same two verses",
            "as AN 8.5's brief version —",
            "now earned through fuller explanation",
        ]),
        ("Cross-references", [
            "AN 8.5 &middot; previous, the brief version of the same eight "
            "conditions",
            "AN 8.7 &middot; next, Devadatta's own failure to overcome them",
        ]),
    ],
    further=[
        '<a href="%s/an8.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.5.html">AN 8.5 &middot; Worldly Conditions (1st)</a> &mdash; previous.',
        '<a href="an-8.7.html">AN 8.7 &middot; Devadatta&rsquo;s Failure</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.7 — Devadattavipattisutta
# --------------------------------------------------------------------------- #
page(
    7, "Devadattavipatti", "Devadatta&rsquo;s Failure",
    vagga=VAGGA_1,
    meta_title="AN 8.7 — Devadatta's Failure | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Devadattavipattisutta, spoken not long after Devadatta's attempt to "
        "split the Saṅgha, naming eight things that overcame him and the "
        "advantage of overcoming them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain, not long after "
                    "Devadatta had left &mdash; a fresh, specific setting, "
                    "distinct from this chapter's opening frame"),
        ("Speakers", "The Buddha, speaking to the mendicants about Devadatta"),
        ("Form", "A narrative opening naming a real historical rupture, then an "
                 "eight-item list of what overcame Devadatta, followed by "
                 "internal peyyāla on the advantage of overcoming the same "
                 "eight"),
        ("Length", "~2 minutes to read"),
        ("A real crisis in the community", "Devadatta's attempt to split the "
                                           "Saṅgha is one of the tradition's "
                                           "best-known ruptures; this discourse "
                                           "is dated explicitly to just after "
                                           "it, giving his fall a doctrinal "
                                           "diagnosis in the same eightfold "
                                           "form used throughout this chapter"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a named, "
                       "consequential setting; the closing sections are "
                       "compressed by the source's own internal ellipsis"),
    ],
    why=(
        "Speaking not long after Devadatta had left the community, the Buddha "
        "names eight things &mdash; gain, loss, fame, disgrace, honor, "
        "dishonor, corrupt wishes, and bad friendship &mdash; that overcame "
        "and overwhelmed Devadatta, sending him to hell for an eon, "
        "irredeemable, and urges the mendicants to overcome the same eight "
        "themselves."),
    guide=[
        ("The teaching in one sentence", [
            "Overcome and overwhelmed by eight things that oppose the true "
            "teaching &mdash; gain, loss, fame, disgrace, honor, dishonor, "
            "corrupt wishes, and bad friendship &mdash; Devadatta is going to "
            "hell for an eon, irredeemable; mendicants should train to "
            "overcome the same eight whenever they encounter them."]),
        ("A real crisis, given a doctrinal diagnosis", [
            "Unlike most of this chapter's bare formulas, this discourse opens "
            "with a specific, consequential setting: Vulture's Peak, "
            "immediately after Devadatta's departure from the community. The "
            "eightfold list that follows functions as the Buddha's own "
            "diagnosis of what led to that rupture."]),
        ("Checking one's own failings and successes", [
            "Before naming Devadatta's eight failings, the Buddha opens with a "
            "more general principle: it's good for a mendicant to check their "
            "own failings and successes, and the failings and successes of "
            "others, from time to time &mdash; framing what follows as a case "
            "study rather than gossip about a fallen rival."]),
        ("Bad friendship, closing a list of worldly conditions", [
            "The first six of the eight items are variations on gain, loss, "
            "fame, disgrace, honor, and dishonor &mdash; close cousins of the "
            "eight worldly conditions from AN 8.5&ndash;6. The list then adds "
            "two items beyond that set: corrupt wishes and, closing the list, "
            "bad friendship &mdash; the sole social cause named among seven "
            "conditions and dispositions."]),
    ],
    terms=[
        ("devadatto āpāyiko nerayiko kappaṭṭho atekiccho",
         "&ldquo;Devadatta is going to a place of loss, to hell, there to "
         "remain for an eon, irredeemable&rdquo; &mdash; the discourse's own "
         "verdict, repeated after both the opening statement and the full "
         "eight-item list."),
        ("lābho, alābho, yaso, ayaso",
         "&ldquo;gain, loss, fame, disgrace&rdquo; &mdash; the first four of "
         "the eight things that overcame Devadatta, echoing the eight worldly "
         "conditions of AN 8.5&ndash;6."),
        ("sakkāro, asakkāro",
         "&ldquo;honor, dishonor&rdquo; &mdash; the fifth and sixth items, "
         "close cousins of fame and disgrace but named separately."),
        ("pāpicchatā, pāpamittatā",
         "&ldquo;corrupt wishes, bad friendship&rdquo; &mdash; the seventh "
         "and eighth items, the only two not drawn from the worldly-"
         "conditions set, with bad friendship closing the list."),
        ("attanāva attano vipattiṁ paccavekkhituṁ",
         "&ldquo;to check their own failings&rdquo; &mdash; part of the "
         "discourse's opening general principle, framing the case study that "
         "follows."),
    ],
    text_intro=(
        "The discourse in full: the general principle of checking one's own "
        "failings, then the eight things that overcame Devadatta. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and a general principle"),
        ("p", "&sect;1", "an8.7:1.1-1.7"),
        ("h3", "The eight things that overcame Devadatta"),
        ("p", "&sect;2", "an8.7:2.1-2.10"),
        ("h3", "Overcoming the same eight, and its advantage"),
        ("p", "&sect;3", "an8.7:3.1-3.8"),
        ("p", "&sect;4", "an8.7:4.1-4.8"),
        ("p", "&sect;5", "an8.7:5.1-5.16"),
        ("h3", "The training"),
        ("p", "&sect;6", "an8.7:6.1-6.10"),
    ],
    quiz=[
        {"q": "When and where is this discourse set?",
         "opts": [
             "At Sāvatthī, at the start of the rains retreat",
             "At Rājagaha, on Vulture's Peak Mountain, not long after "
             "Devadatta had left the community",
             "At Vesālī, decades after the Buddha's passing",
             "No setting is given"],
         "correct": 1,
         "expl": "A specific, consequential setting, unlike most of this "
                 "chapter's bare formulas."},
        {"q": "What eight things overcame and overwhelmed Devadatta, according "
              "to this discourse?",
         "opts": [
             "The five hindrances plus three more",
             "Gain, loss, fame, disgrace, honor, dishonor, corrupt wishes, and "
             "bad friendship",
             "The seven factors of awakening, negated",
             "Only physical illnesses"],
         "correct": 1,
         "expl": "Six variants on worldly conditions, plus corrupt wishes and "
                 "bad friendship."},
        {"q": "What general principle does the Buddha state before naming "
              "Devadatta's specific failings?",
         "opts": [
             "That failure is inevitable for everyone",
             "It's good for a mendicant to check their own failings and "
             "successes, and the failings and successes of others, from time "
             "to time",
             "That Devadatta should be publicly shamed",
             "That no one should ever discuss another's conduct"],
         "correct": 1,
         "expl": "A framing principle that turns the account into a case "
                 "study, not gossip."},
        {"q": "According to the guide, how do six of the eight items relate to "
              "AN 8.5–6?",
         "opts": [
             "They are unrelated to those discourses",
             "They are close cousins of the eight worldly conditions — gain, "
             "loss, fame, disgrace, honor, and dishonor",
             "They directly contradict AN 8.5–6",
             "They only appear in this discourse"],
         "correct": 1,
         "expl": "A partial overlap with the worldly-conditions list, plus two "
                 "further items."},
        {"q": "What is the eighth and closing item of the list, the only "
              "purely social cause named?",
         "opts": [
             "Wrong view", "Bad friendship", "Excessive fasting",
             "Refusing to teach"],
         "correct": 1,
         "expl": "Pāpamittatā, closing a list otherwise made of worldly "
                 "conditions and corrupt wishes."},
        {"q": "What happens to the source's own description of the advantage "
              "of overcoming these eight things?",
         "opts": [
             "It is stated in full detail for each of the eight",
             "It is compressed by the source's own internal ellipsis, the "
             "same self-abbreviation pattern met at AN 8.2",
             "It is omitted from the discourse entirely",
             "It is replaced with a different list"],
         "correct": 1,
         "expl": "An internal peyyāla, another instance of this book's "
                 "recurring self-abbreviation pattern."},
    ],
    marginalia=[
        ("Eight things that overcame him", [
            "gain, loss, fame, disgrace,",
            "honor, dishonor, corrupt wishes —",
            "bad friendship closing the list",
        ]),
        ("A named, consequential setting", [
            "Vulture's Peak, just after",
            "Devadatta had left —",
            "a real rupture, given diagnosis",
        ]),
        ("Check yourself, not just others", [
            "the general principle first:",
            "examine your own failings",
            "before naming another's",
        ]),
        ("Cross-references", [
            "AN 8.6 &middot; previous, the eight worldly conditions in full",
            "AN 8.8 &middot; next, Uttara restates this very teaching",
        ]),
    ],
    further=[
        '<a href="%s/an8.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.6.html">AN 8.6 &middot; Worldly Conditions (2nd)</a> &mdash; previous.',
        '<a href="an-8.8.html">AN 8.8 &middot; Uttara on Failure</a> &mdash; next, the same '
        "teaching restated through Uttara, Vessavaṇa, and Sakka.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.8 — Uttaravipattisutta
# --------------------------------------------------------------------------- #
page(
    8, "Uttaravipatti", "Uttara on Failure",
    vagga=VAGGA_1,
    meta_title="AN 8.8 — Uttara on Failure | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Uttaravipattisutta, in which the mendicant Uttara teaches AN 8.7's "
        "own words on Devadatta's failure, the god-king Vessavaṇa carries the "
        "report to Sakka, and Sakka comes in person to ask Uttara where the "
        "teaching came from. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Saṅkheyyaka Mountain in the Mahisa region near "
                    "Dhavajālikā &mdash; a location unique to this discourse"),
        ("Speakers", "Venerable Uttara, Vessavaṇa (a great king of the gods), "
                     "and Sakka, lord of the gods, in a three-part relay"),
        ("Form", "A narrative in three stages — Uttara teaches, Vessavaṇa "
                 "overhears and reports upward, Sakka descends to ask Uttara "
                 "directly — closing with the grain-heap simile and a full "
                 "quotation of AN 8.7 within Sakka's own reply"),
        ("Length", "~4 minutes to read"),
        ("A chain of overhearing, not a repeat", "This discourse does not "
                                                  "simply restate AN 8.7's "
                                                  "teaching; its real subject is "
                                                  "how that teaching travels — "
                                                  "overheard by a passing deity, "
                                                  "relayed to its king, and "
                                                  "finally verified in person"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "longest discourse in this chapter so far, with three "
                       "named speakers and an embedded quotation of another "
                       "full discourse"),
    ],
    why=(
        "Venerable Uttara teaches the mendicants the same general principle "
        "that opened AN 8.7 &mdash; checking one's own and others' failings "
        "and successes &mdash; and the god-king Vessavaṇa, passing by, "
        "overhears him and carries the report to Sakka, who descends in "
        "person to ask whether the teaching is Uttara's own or the Buddha's, "
        "and receives in reply a grain-heap simile and the full text of AN "
        "8.7 itself."),
    guide=[
        ("The teaching in one sentence", [
            "Whatever is well spoken is spoken by the Buddha, and both Uttara "
            "and others who speak well rely completely on that source &mdash; "
            "illustrated when Uttara, questioned by Sakka about the origin of "
            "his own teaching, answers with a simile and then the complete "
            "text of AN 8.7, the Buddha's own words about Devadatta."]),
        ("A relay of overhearing, not a solo teaching", [
            "The discourse tracks a teaching's journey through three parties: "
            "Uttara teaches the mendicants on a mountain; Vessavaṇa, a great "
            "king of the gods traveling on business, overhears and carries "
            "the report to the Thirty-Three gods; Sakka, lord of the gods, "
            "descends in person to verify it with Uttara directly."]),
        ("The grain-heap simile", [
            "Asked whether his teaching came from his own inspiration or from "
            "the Buddha, Uttara answers with a simile: a large heap of grain "
            "near a village, from which a crowd draws grain by many different "
            "means &mdash; carrying poles, baskets, cupped hands. Asked where "
            "they got the grain, the crowd would rightly say the heap. "
            "Likewise, whatever is well spoken traces back to the Buddha, and "
            "Uttara and others who speak well rely completely on that source."]),
        ("AN 8.7, quoted in full within this discourse", [
            "Having explained the simile, Uttara does not merely summarize "
            "the Buddha's teaching about Devadatta &mdash; he recites AN 8.7 "
            "in its entirety, word for word, as his answer to Sakka. Sakka "
            "responds that this teaching should be learned, memorized, and "
            "remembered, since it isn't yet established anywhere among the "
            "four assemblies."]),
    ],
    terms=[
        ("vessavaṇo mahārājā",
         "&ldquo;the great king Vessavaṇa&rdquo; &mdash; one of the four "
         "great kings of the gods, here traveling on business and overhearing "
         "Uttara's teaching by chance."),
        ("sakko devānamindo",
         "&ldquo;Sakka, lord of the gods&rdquo; &mdash; ruler of the gods of "
         "the Thirty-Three, who descends in person to question Uttara "
         "directly rather than relying on Vessavaṇa's secondhand report."),
        ("yaṁ kiñci subhāsitaṁ sabbaṁ taṁ tassa bhagavato vacanaṁ",
         "&ldquo;whatever is well spoken is spoken by the Blessed One&rdquo; "
         "&mdash; Uttara's own summary of the grain-heap simile, and the "
         "discourse's central claim."),
        ("mahā dhaññarāsi",
         "&ldquo;a large heap of grain&rdquo; &mdash; the simile's central "
         "image, illustrating how many different speakers can draw from one "
         "source."),
        ("na cāyaṁ, bhante uttara, dhammapariyāyo catūsu parisāsu "
         "paṭṭhāsi",
         "&ldquo;this exposition of the teaching is not established anywhere "
         "in the four assemblies&rdquo; &mdash; Sakka's own closing remark, "
         "the reason he urges Uttara to learn, memorize, and remember it."),
    ],
    text_intro=(
        "The discourse in full: Uttara's teaching, Vessavaṇa's report to "
        "Sakka, and Sakka's visit, including a full restatement of AN 8.7. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Uttara teaches, and Vessavaṇa overhears"),
        ("p", "&sect;1", "an8.8:1.1-2.2"),
        ("h3", "Vessavaṇa reports to Sakka"),
        ("p", "&sect;2", "an8.8:3.1-3.8"),
        ("h3", "Sakka questions Uttara directly"),
        ("p", "&sect;3", "an8.8:4.1-5.9"),
        ("h3", "The grain-heap simile"),
        ("p", "&sect;4", "an8.8:6.1-6.8"),
        ("h3", "Sakka's response, and AN 8.7 restated in full"),
        ("p", "&sect;5", "an8.8:7.1-13.7"),
    ],
    quiz=[
        {"q": "What is this discourse really about, according to the guide?",
         "opts": [
             "A simple repeat of AN 8.7 with no new content",
             "How a teaching travels — overheard by a passing deity, relayed "
             "to its king, and finally verified in person with the original "
             "speaker",
             "A dispute between Uttara and Sakka",
             "A new teaching unrelated to AN 8.7"],
         "correct": 1,
         "expl": "A relay of overhearing across three parties, not a solo "
                 "restatement."},
        {"q": "Who overhears Uttara's teaching first, and how?",
         "opts": [
             "Sakka, who was meditating nearby",
             "Vessavaṇa, a great king of the gods, passing by on unrelated "
             "business",
             "A group of local villagers",
             "No one overhears it; Uttara reports it himself"],
         "correct": 1,
         "expl": "A chance overhearing during travel, not a planned visit."},
        {"q": "What does the grain-heap simile illustrate?",
         "opts": [
             "That teachings should never be shared with others",
             "That whatever is well spoken traces back to the Buddha, just as "
             "grain drawn by many different means all traces back to one heap",
             "That Uttara invented his own original doctrine",
             "That grain offerings are the highest form of generosity"],
         "correct": 1,
         "expl": "A single source, drawn from by many different speakers."},
        {"q": "What does Uttara do when Sakka asks where his teaching came "
              "from?",
         "opts": [
             "He refuses to answer",
             "He gives the grain-heap simile, then recites the full text of "
             "AN 8.7 word for word",
             "He claims it as his own original insight",
             "He sends Sakka to ask the Buddha directly"],
         "correct": 1,
         "expl": "A simile followed by a complete quotation of another "
                 "discourse, embedded within this one."},
        {"q": "Why does Sakka urge Uttara to learn, memorize, and remember "
              "this exposition of the teaching?",
         "opts": [
             "Because it is about to be lost forever",
             "Because it is not yet established anywhere among the four "
             "assemblies",
             "Because Sakka plans to teach it himself instead",
             "Because it contradicts the Buddha's own teaching"],
         "correct": 1,
         "expl": "Sakka's own stated reason, closing the discourse."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Saṅkheyyaka Mountain in the Mahisa region near Dhavajālikā",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A location unique to this discourse, not reused elsewhere in "
                 "this chapter."},
    ],
    marginalia=[
        ("A teaching relayed upward", [
            "Uttara teaches — Vessavaṇa",
            "overhears, reports to Sakka —",
            "who comes himself to verify",
        ]),
        ("The grain-heap simile", [
            "many hands draw grain",
            "by pole, basket, cupped hands —",
            "all from one and the same heap",
        ]),
        ("AN 8.7, quoted whole", [
            "not summarized but recited",
            "word for word as answer —",
            "Devadatta's own eight things",
        ]),
        ("Cross-references", [
            "AN 8.7 &middot; previous, and quoted in full within this "
            "discourse",
            "AN 8.9 &middot; next, a very different register: the monk Nanda",
        ]),
    ],
    further=[
        '<a href="%s/an8.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.7.html">AN 8.7 &middot; Devadatta&rsquo;s Failure</a> &mdash; previous, '
        "and quoted here in full.",
        '<a href="an-8.9.html">AN 8.9 &middot; Nanda</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.9 — Nandasutta
# --------------------------------------------------------------------------- #
page(
    9, "Nanda", "Nanda",
    vagga=VAGGA_1,
    meta_title="AN 8.9 — Nanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nandasutta, on how the Buddha's own half-brother Nanda — called "
        "gentleman, strong, lovely, and lustful — lives the full spiritual "
        "life by guarding the sense doors, eating in moderation, dedication "
        "to wakefulness, and mindful awareness. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Four epithets for Nanda, then four practices explained in "
                 "turn, each opening and closing with the same refrain"),
        ("Length", "~2 minutes to read"),
        ("No stated eight, unlike most of this chapter", "This discourse never "
                                                          "uses the "
                                                          "&ldquo;aṭṭhahi&rdquo; "
                                                          "(&ldquo;by "
                                                          "eight&rdquo;) formula "
                                                          "that opens most "
                                                          "discourses in this "
                                                          "chapter; its four "
                                                          "epithets plus four "
                                                          "practices can be read "
                                                          "as an implicit eight, "
                                                          "but the text itself "
                                                          "never counts them"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "well-known figure and a clear fourfold practice "
                       "structure, easier to follow than to summarize in one "
                       "line"),
    ],
    why=(
        "The Buddha names his own half-brother Nanda &mdash; rightly called "
        "gentleman, strong, lovely, and lustful &mdash; and asks how such a "
        "person could live the full and pure spiritual life without guarding "
        "the sense doors, eating in moderation, dedicating himself to "
        "wakefulness, and maintaining mindfulness and situational awareness, "
        "then explains each of the four practices in turn."),
    guide=[
        ("The teaching in one sentence", [
            "Nanda &mdash; a gentleman, strong, lovely, and by his own nature "
            "lustful &mdash; is able to live the full and pure spiritual life "
            "only because he guards the sense doors, eats in moderation, is "
            "dedicated to wakefulness, and maintains mindfulness and "
            "situational awareness."]),
        ("An implicit eight, never counted", [
            "Unlike almost every other discourse in this chapter, this one "
            "never says &ldquo;eight qualities&rdquo; or asks &ldquo;what "
            "eight?&rdquo; Its four epithets for Nanda and four explained "
            "practices could be read together as this chapter's numerical "
            "theme, but the text itself leaves that combination implicit "
            "rather than stated."]),
        ("Guarding the sense doors, direction by direction", [
            "The first practice is explained through Nanda's own method: "
            "before looking in any direction &mdash; east, west, north, "
            "south, up, down, or the intermediate directions &mdash; he "
            "wholeheartedly concentrates first, resolving that covetousness "
            "and displeasure will not overwhelm him for having looked."]),
        ("Eating, wakefulness, and mindfulness, each with its own formula", [
            "Nanda reflects rationally on food eaten only to sustain the body, "
            "not for fun or adornment. He practices walking and sitting "
            "meditation through the day and both the first and last watches "
            "of the night, sleeping mindfully in the lion's posture only "
            "during the middle watch. And he knows feelings, perceptions, and "
            "thoughts as they arise, remain, and pass away."]),
    ],
    terms=[
        ("kulaputto, balavā, pāsādiko, tibbarāgo",
         "&ldquo;gentleman, strong, lovely, and lustful&rdquo; &mdash; the "
         "four epithets rightly applied to Nanda, naming both his standing "
         "and his own inherited disposition toward desire."),
        ("indriyesu guttadvāro",
         "&ldquo;guards the sense doors&rdquo; &mdash; the first of the four "
         "practices, illustrated through Nanda's own method of concentrating "
         "before looking in any direction."),
        ("bhojane mattaññū",
         "&ldquo;eats in moderation&rdquo; &mdash; the second practice, "
         "explained through rational reflection on the purpose of food."),
        ("jāgariyaṁ anuyutto",
         "&ldquo;dedicated to wakefulness&rdquo; &mdash; the third practice, "
         "a specific schedule of walking and sitting meditation through the "
         "day and most of the night."),
        ("satisampajaññena samannāgato",
         "&ldquo;has mindfulness and situational awareness&rdquo; &mdash; the "
         "fourth and final practice, knowing feelings, perceptions, and "
         "thoughts as they arise, remain, and pass away."),
    ],
    text_intro=(
        "The discourse in full: Nanda's four epithets, and the four practices "
        "that let him live the full spiritual life. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Nanda, named by four epithets"),
        ("p", "&sect;1", "an8.9:1.1-1.9"),
        ("h3", "Guarding the sense doors, direction by direction"),
        ("p", "&sect;2", "an8.9:2.1-2.9"),
        ("h3", "Eating in moderation"),
        ("p", "&sect;3", "an8.9:3.1-3.4"),
        ("h3", "Dedication to wakefulness"),
        ("p", "&sect;4", "an8.9:4.1-4.6"),
        ("h3", "Mindfulness and situational awareness"),
        ("p", "&sect;5", "an8.9:5.1-6.1"),
    ],
    quiz=[
        {"q": "What four epithets does the Buddha apply to his half-brother "
              "Nanda?",
         "opts": [
             "Wise, patient, humble, and generous",
             "Gentleman, strong, lovely, and lustful",
             "Weak, plain, cowardly, and dull",
             "Rich, famous, powerful, and proud"],
         "correct": 1,
         "expl": "Including tibbarāgo, 'lustful' — named plainly, not "
                 "euphemized."},
        {"q": "According to the guide, what is unusual about this discourse "
              "compared to most others in this chapter?",
         "opts": [
             "It is the longest discourse in the chapter",
             "It never uses the chapter's usual 'by eight, what eight?' "
             "formula, though four epithets plus four practices could be read "
             "as an implicit eight",
             "It has no named speaker",
             "It is set in a foreign country"],
         "correct": 1,
         "expl": "An implicit eight, left uncounted by the text itself."},
        {"q": "How does Nanda guard the sense doors, according to this "
              "discourse?",
         "opts": [
             "By never leaving his dwelling",
             "By wholeheartedly concentrating before looking in any "
             "direction, resolving that covetousness and displeasure won't "
             "overwhelm him",
             "By closing his eyes at all times",
             "By avoiding all human contact"],
         "correct": 1,
         "expl": "A direction-by-direction method of concentrating before "
                 "looking."},
        {"q": "Why does Nanda eat, according to his own reflection?",
         "opts": [
             "For fun, indulgence, and adornment",
             "Only to sustain the body, avoid harm, and support spiritual "
             "practice",
             "To gain physical strength for combat",
             "As a social obligation only"],
         "correct": 1,
         "expl": "Rational reflection on food's purpose, the second of the "
                 "four practices."},
        {"q": "During which watch of the night does Nanda sleep, and how?",
         "opts": [
             "He never sleeps at all",
             "Only the middle watch, lying in the lion's posture, mindful and "
             "aware, focused on the time of getting up",
             "The entire night, without any meditation",
             "Only briefly at dawn"],
         "correct": 1,
         "expl": "Walking and sitting meditation fill the first and last "
                 "watches; only the middle watch is for sleep."},
        {"q": "What does the fourth practice, mindfulness and situational "
              "awareness, consist of?",
         "opts": [
             "Reciting scripture continuously",
             "Knowing feelings, perceptions, and thoughts as they arise, "
             "remain, and pass away",
             "Avoiding all thought entirely",
             "Memorizing the monastic code"],
         "correct": 1,
         "expl": "Direct awareness of the arising, presence, and passing of "
                 "mental factors."},
    ],
    marginalia=[
        ("Four epithets for Nanda", [
            "gentleman, strong, lovely —",
            "and lustful, named plainly —",
            "his own brother, not spared candor",
        ]),
        ("An eight left uncounted", [
            "four names, four practices —",
            "never called 'the eight' outright,",
            "unlike most of this chapter",
        ]),
        ("Guarding every direction", [
            "east, west, up, down —",
            "concentrating before looking,",
            "so desire finds no opening",
        ]),
        ("Cross-references", [
            "AN 8.8 &middot; previous, Uttara's teaching relayed through gods",
            "AN 8.10 &middot; next, closing this chapter with a warning about "
            "corrupt companions",
        ]),
    ],
    further=[
        '<a href="%s/an8.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.8.html">AN 8.8 &middot; Uttara on Failure</a> &mdash; previous.',
        '<a href="an-8.10.html">AN 8.10 &middot; Trash</a> &mdash; next, closing this '
        "chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.10 — Kāraṇḍavasutta — closes ch.1 Mettāvagga
# --------------------------------------------------------------------------- #
page(
    10, "Kāraṇḍava", "Trash",
    vagga=VAGGA_1,
    meta_title="AN 8.10 — Trash | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Kāraṇḍavasutta, closing this chapter with the Buddha's call to "
        "expel a corrupt mendicant from the community, illustrated by four "
        "similes of bad barley, chaff, rotten wood, and useless trash. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Campā, on the banks of the Gaggarā Lotus Pond &mdash; a "
                    "location this discourse does not share with any earlier "
                    "one in this chapter"),
        ("Speakers", "The Buddha, prompted by mendicants accusing one of their "
                     "own of an offense"),
        ("Form", "A narrative opening, then four similes on the same theme "
                 "&mdash; bad barley, winnowed chaff, rotten wood, and the "
                 "discourse's own title-image, trash &mdash; closing with "
                 "verses"),
        ("Length", "~3 minutes to read"),
        ("Closing the chapter, and its own colophon", "This discourse closes "
                                                       "<em>Mettāvagga</em>, "
                                                       "the first chapter of "
                                                       "the Eights; the "
                                                       "source's own untranslated "
                                                       "closing verse names all "
                                                       "ten discourses of the "
                                                       "chapter by their opening "
                                                       "words"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; four "
                       "concrete similes built on one shared point, "
                       "straightforward once the pattern is seen"),
    ],
    why=(
        "When mendicants accuse a fellow mendicant of an offense and he "
        "dodges the issue with irrelevant points and open hostility, the "
        "Buddha calls for his expulsion, comparing him in turn to bad barley "
        "hidden among healthy grain, chaff blown aside in winnowing, and "
        "rotten wood that sounds hollow when struck &mdash; each recognized "
        "only once its true nature is exposed."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who, when accused of an offense, dodges the issue, "
            "distracts with irrelevant points, and shows annoyance, hate, and "
            "bitterness should be expelled from the community &mdash; not out "
            "of vindictiveness, but so that such a person doesn't corrupt "
            "good-natured mendicants, just as bad barley, chaff, and rotten "
            "wood are separated from what is sound."]),
        ("An accusation that goes badly", [
            "The discourse opens with a concrete incident: mendicants accuse "
            "one of their own of an offense, and rather than responding "
            "honestly, he dodges the issue, distracts with irrelevant points, "
            "and displays annoyance, hate, and bitterness &mdash; the "
            "Buddha's response is immediate and blunt: throw this individual "
            "out."]),
        ("Four similes, one recurring point", [
            "The Buddha develops the same point through four images: a "
            "corrupt mendicant looks identical to good-natured ones until "
            "their offense is noticed, just as bad barley looks like healthy "
            "barley until its head appears, chaff looks like grain until "
            "winnowed, and a rotten tree sounds like a sound one until "
            "struck with an axe. In every case, recognition &mdash; not "
            "appearance &mdash; is what triggers separation."]),
        ("Not vindictiveness, but protecting the community", [
            "Each simile closes with the same refrain: this is done so that "
            "the corrupt individual doesn't spoil what is sound. The "
            "discourse's title-image &mdash; trash, useless refuse &mdash; "
            "names what the corrupt mendicant becomes once recognized, and "
            "the closing verses call directly for throwing out the trash and "
            "sweeping away the scraps, dwelling in communion only with the "
            "pure."]),
    ],
    terms=[
        ("kāraṇḍavo",
         "&ldquo;trash, useless refuse&rdquo; &mdash; this discourse's own "
         "title term, applied to a corrupt mendicant once their offense is "
         "recognized."),
        ("apehi ayaṁ puggalo",
         "&ldquo;throw this individual out&rdquo; &mdash; the Buddha's blunt "
         "opening response to the accused mendicant's dodging and hostility."),
        ("nirujjhamānā yaṭṭhi kaṇṭako",
         "the bad-barley simile's own turning point &mdash; &ldquo;so long as "
         "the head doesn't appear&rdquo; &mdash; describing how a corrupt "
         "individual passes unnoticed until the decisive sign is seen."),
        ("thusaṁ vā palālaṁ vā",
         "&ldquo;chaff or straw&rdquo; &mdash; part of the third simile, "
         "winnowed grain, where the flimsy and insubstantial are blown aside "
         "and swept further away."),
        ("pūtimūlaṁ pūtikandaṁ",
         "&ldquo;rotten inside, decomposing and decayed&rdquo; &mdash; the "
         "fourth simile's own image, a tree that sounds hollow when struck, "
         "unlike the sound cracking of healthy wood."),
    ],
    text_intro=(
        "The discourse in full: an accusation, four similes on recognizing "
        "and removing corruption, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The accusation, and the Buddha's response"),
        ("p", "&sect;1", "an8.10:1.1-2.12"),
        ("h3", "The simile of bad barley"),
        ("p", "&sect;2", "an8.10:3.1-4.7"),
        ("h3", "The simile of winnowed chaff"),
        ("p", "&sect;3", "an8.10:5.1-5.11"),
        ("h3", "The simile of rotten wood"),
        ("p", "&sect;4", "an8.10:6.1-6.11"),
        ("h3", "Closing verses"),
        ("p", "&sect;5", "an8.10:7.1-11.6"),
    ],
    quiz=[
        {"q": "What incident opens this discourse?",
         "opts": [
             "A dispute over almsfood",
             "Mendicants accuse a fellow mendicant of an offense, and he "
             "dodges the issue with irrelevant points and open hostility",
             "A visiting king asks for teaching",
             "A natural disaster near the monastery"],
         "correct": 1,
         "expl": "A concrete accusation, met with evasion and hostility, "
                 "prompting the Buddha's response."},
        {"q": "What does the Buddha immediately call for, in response?",
         "opts": [
             "A formal debate to settle the matter",
             "Expelling the individual — 'throw this individual out'",
             "Ignoring the accusation entirely",
             "A period of silent meditation for everyone"],
         "correct": 1,
         "expl": "A blunt, immediate response, developed through the similes "
                 "that follow."},
        {"q": "What do the four similes in this discourse share?",
         "opts": [
             "Nothing; they illustrate four unrelated points",
             "The same recurring point — recognition, not appearance, is "
             "what triggers separation from what is sound",
             "They all involve water",
             "They all describe monastic robes"],
         "correct": 1,
         "expl": "Bad barley, chaff, rotten wood, and trash — one point "
                 "developed four ways."},
        {"q": "According to the guide, why does the discourse call for "
              "removing a corrupt mendicant?",
         "opts": [
             "Out of vindictiveness toward the individual",
             "So that the corrupt individual doesn't corrupt or spoil the "
             "good-natured mendicants around them",
             "To punish them for a specific crime",
             "There is no reason given"],
         "correct": 1,
         "expl": "Protection of the community, stated explicitly after each "
                 "simile."},
        {"q": "What does this discourse's own title term, kāraṇḍavo, mean?",
         "opts": [
             "A type of monastic robe", "Trash, useless refuse",
             "A meditation posture", "A ceremonial offering"],
         "correct": 1,
         "expl": "What a corrupt mendicant becomes once recognized, echoed in "
                 "the closing verses."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Rājagaha, on Vulture's Peak",
             "Campā, on the banks of the Gaggarā Lotus Pond",
             "Vesālī, at the Great Wood"],
         "correct": 2,
         "expl": "A location unique to this discourse within the chapter."},
    ],
    marginalia=[
        ("Four similes, one point", [
            "bad barley · winnowed chaff ·",
            "rotten wood · trash itself —",
            "hidden until recognized",
        ]),
        ("Not vindictiveness", [
            "expelled so the corrupt",
            "doesn't spoil the sound —",
            "protection, not punishment",
        ]),
        ("Closing the first chapter", [
            "ten discourses complete",
            "Mettāvagga, chapter one —",
            "love opened it, trash closes it",
        ]),
        ("Cross-references", [
            "AN 8.9 &middot; previous, Nanda's own four practices",
            "AN 8.1 &middot; earlier, opening this same chapter with love's "
            "eight benefits",
        ]),
    ],
    further=[
        '<a href="%s/an8.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.9.html">AN 8.9 &middot; Nanda</a> &mdash; previous.',
        '<a href="an-8.1.html">AN 8.1 &middot; The Benefits of Love</a> &mdash; earlier, '
        "opening this same chapter.",
    ],
)


VAGGA_2 = "<em>Mahāvagga</em> &mdash; the second chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.11 — Verañjasutta — opens ch.2 Mahāvagga
# --------------------------------------------------------------------------- #
page(
    11, "Verañja", "At Verañjā",
    vagga=VAGGA_2,
    meta_title="AN 8.11 — At Verañjā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Verañjasutta, opening this chapter with the brahmin Verañja's eight "
        "hostile epithets for the Buddha, each accepted and reinterpreted, "
        "followed by the Buddha's own first-person account of his awakening. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Verañjā, at the root of a neem tree dedicated to Naḷeru "
                    "&mdash; a location unique to this discourse and the next"),
        ("Speakers", "The brahmin Verañja and the Buddha, in direct dialogue"),
        ("Form", "Eight hostile epithets, each accepted in a reinterpreted "
                 "sense and then set aside, followed by the chicken-and-egg "
                 "simile and the Buddha's own first-person account of the "
                 "three knowledges of his awakening night"),
        ("Length", "~6 minutes to read"),
        ("A famous, substantial discourse", "This opens the chapter's own "
                                            "title theme, and is among the "
                                            "tradition's most-cited first-"
                                            "person accounts of the Buddha's "
                                            "own awakening"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; long, with "
                       "eight repeated exchanges and then a sustained "
                       "first-person narrative of deep meditative attainment"),
    ],
    why=(
        "The brahmin Verañja confronts the Buddha with eight hostile "
        "epithets &mdash; that he lacks taste, is indelicate, teaches "
        "inaction, teaches annihilation, is disgusted, is an exterminator, is "
        "a mortifier, and is immature &mdash; and the Buddha accepts each one "
        "in a sense of his own choosing, entirely different from what Verañja "
        "meant, before giving a chicken-and-egg simile and his own first-"
        "person account of the three knowledges that broke him free of "
        "ignorance."),
    guide=[
        ("The teaching in one sentence", [
            "Each of Verañja's eight hostile epithets can rightly be said of "
            "the Buddha &mdash; but only in a sense of the Buddha's own "
            "choosing, always about abandoning what is unskillful, never in "
            "the accusatory sense Verañja intended; and the Buddha's own "
            "claim to be the eldest and first in the world rests on his "
            "direct account of the three knowledges realized on the night of "
            "his awakening."]),
        ("Eight epithets, eight reinterpretations", [
            "Verañja calls the Buddha, in turn: lacking taste, indelicate, a "
            "teacher of inaction, a teacher of annihilation, disgusted, an "
            "exterminator, a mortifier, and immature. Each time, the Buddha "
            "agrees &mdash; but redefines the term around abandoning craving, "
            "delight, or unskillful conduct, cut off at the root like a palm "
            "stump, then closes with the same refrain: &ldquo;but that's not "
            "what you're talking about.&rdquo;"]),
        ("The chicken-and-egg simile, and a claim to be eldest", [
            "Having set aside all eight accusations, the Buddha turns the "
            "conversation with a simile: of many eggs incubated together, the "
            "chick that breaks out first is rightly called the eldest, not "
            "the youngest. In a population lost in ignorance, swaddled in "
            "their shells, the Buddha claims to be the one who broke the egg "
            "of ignorance first, making him the eldest and first in the "
            "world."]),
        ("Three knowledges, told in the Buddha's own words", [
            "The Buddha then narrates, in first person, the four "
            "absorptions and the three knowledges of his awakening night: "
            "recollection of his own past lives in the first watch, the "
            "death and rebirth of other beings according to their deeds in "
            "the middle watch, and the ending of the defilements in the last "
            "watch &mdash; each called a &ldquo;breaking out,&rdquo; like a "
            "chick from its shell. Verañja, persuaded, goes for refuge as a "
            "lay follower for life."]),
    ],
    terms=[
        ("rasapaṭisaṁvedī, arasarūpo",
         "&ldquo;lacks taste, indelicate&rdquo; &mdash; the first two of "
         "Verañja's eight epithets, each reinterpreted around the Buddha's "
         "own abandonment of taste and delight for sense objects."),
        ("akiriyavādo, ucchedavādo",
         "&ldquo;teacher of inaction, teacher of annihilationism&rdquo; "
         "&mdash; the third and fourth epithets, redefined around the "
         "cessation of unskillful qualities and defilements, not doctrine "
         "denying moral consequence."),
        ("jegucchī, venayiko, tapassī, apagabbho",
         "&ldquo;disgusted, exterminator, mortifier, immature&rdquo; &mdash; "
         "the remaining four epithets, each reinterpreted the same way, "
         "closing with the recurring refrain that this isn't what Verañja "
         "meant."),
        ("jeṭṭho seṭṭho lokassa",
         "&ldquo;the eldest and first in the world&rdquo; &mdash; the "
         "Buddha's own claim, following the chicken-and-egg simile, to have "
         "been the first to break out of ignorance."),
        ("tisso vijjā",
         "&ldquo;the three knowledges&rdquo; &mdash; recollection of past "
         "lives, the death and rebirth of beings, and the ending of "
         "defilements, the three &ldquo;breakings-out&rdquo; of the "
         "awakening night, told here in the Buddha's own first-person voice."),
    ],
    text_intro=(
        "The discourse in full: Verañja's eight epithets, the chicken-and-egg "
        "simile, and the Buddha's own account of his awakening. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and Verañja's opening accusation"),
        ("p", "&sect;1", "an8.11:1.1-2.7"),
        ("h3", "Eight epithets, each reinterpreted"),
        ("p", "&sect;2", "an8.11:3.1-10.7"),
        ("h3", "The chicken-and-egg simile"),
        ("p", "&sect;3", "an8.11:11.1-12.2"),
        ("h3", "The four absorptions"),
        ("p", "&sect;4", "an8.11:13.1-13.5"),
        ("h3", "The three knowledges"),
        ("p", "&sect;5", "an8.11:14.1-19.3"),
        ("h3", "Verañja goes for refuge"),
        ("p", "&sect;6", "an8.11:20.1-20.6"),
    ],
    quiz=[
        {"q": "How does the Buddha respond to each of Verañja's eight hostile "
              "epithets?",
         "opts": [
             "By denying every one of them",
             "By accepting each one, but only in a sense of his own choosing "
             "— always about abandoning what is unskillful, never what "
             "Verañja meant",
             "By ignoring the accusations entirely",
             "By becoming angry and ending the conversation"],
         "correct": 1,
         "expl": "Acceptance with reinterpretation, closing each with 'but "
                 "that's not what you're talking about.'"},
        {"q": "What does the chicken-and-egg simile illustrate?",
         "opts": [
             "That age should always be respected",
             "That the chick first to break out of its shell is rightly "
             "called the eldest — as the Buddha claims to be, breaking the "
             "egg of ignorance first",
             "That eggs should never be disturbed",
             "That Verañja himself is the eldest"],
         "correct": 1,
         "expl": "A claim to priority based on who broke free first, not on "
                 "chronological birth order."},
        {"q": "What are the three knowledges the Buddha describes realizing "
              "on his awakening night?",
         "opts": [
             "The four noble truths, the eightfold path, and dependent "
             "origination",
             "Recollection of his own past lives, the death and rebirth of "
             "other beings according to their deeds, and the ending of the "
             "defilements",
             "The five aggregates, the six senses, and the seven awakening "
             "factors",
             "Three kinds of miraculous power"],
         "correct": 1,
         "expl": "One knowledge per watch of the night, each called a "
                 "'breaking out.'"},
        {"q": "What happens at the end of this discourse?",
         "opts": [
             "Verañja leaves unconvinced",
             "Verañja goes for refuge to the Buddha, the teaching, and the "
             "Saṅgha as a lay follower for life",
             "Verañja challenges the Buddha to a debate",
             "The discourse ends without resolution"],
         "correct": 1,
         "expl": "A full conversion, closing the dialogue."},
        {"q": "According to the guide, what does the Buddha's response to "
              "each epithet consistently reinterpret it around?",
         "opts": [
             "Physical strength and endurance",
             "Abandoning craving, delight, or unskillful conduct — cut off "
             "at the root like a palm stump",
             "Wealth and social status",
             "Skill in public debate"],
         "correct": 1,
         "expl": "A consistent redefinition around inner abandonment, not "
                 "the accusatory sense intended."},
        {"q": "What does 'teacher of annihilationism' come to mean, in the "
              "Buddha's own reinterpretation?",
         "opts": [
             "Denying any afterlife or moral consequence",
             "Teaching the annihilation of greed, hate, and delusion",
             "Teaching that the self is annihilated at death",
             "Advocating for the destruction of property"],
         "correct": 1,
         "expl": "Not metaphysical annihilationism, but the ending of "
                 "defilements."},
    ],
    marginalia=[
        ("Eight epithets, reclaimed", [
            "lacks taste, indelicate,",
            "teacher of inaction, annihilation —",
            "each redefined, each set aside",
        ]),
        ("The chick that breaks out first", [
            "not born first, but freed first —",
            "the egg of ignorance broken —",
            "'I am the eldest in the world'",
        ]),
        ("Three knowledges, one night", [
            "past lives · beings' rebirth ·",
            "the ending of defilements —",
            "three watches, three breakings-out",
        ]),
        ("Cross-references", [
            "AN 8.10 &middot; earlier, closing the previous chapter",
            "AN 8.12 &middot; next, the same eight epithets echoed for "
            "General Sīha",
        ]),
    ],
    further=[
        '<a href="%s/an8.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.10.html">AN 8.10 &middot; Trash</a> &mdash; earlier, closing the '
        "previous chapter.",
        '<a href="an-8.12.html">AN 8.12 &middot; With Sīha</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.12 — Sīhasutta
# --------------------------------------------------------------------------- #
page(
    12, "Sīha", "With Sīha",
    vagga=VAGGA_2,
    meta_title="AN 8.12 — With Sīha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sīhasutta, in which the Jain general Sīha overcomes his teachers' "
        "warnings to visit the Buddha, hears eight epithets reinterpreted "
        "once again, converts, and weathers a Jain smear campaign over a "
        "meal of meat. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with the peaked "
                    "roof, then General Sīha's own home"),
        ("Speakers", "General Sīha, the Jain ascetic of the Ñātika clan, and "
                     "the Buddha"),
        ("Form", "A three-part narrative — Sīha's twice-thwarted resolve to "
                 "visit the Buddha, eight epithets reinterpreted as in AN "
                 "8.11 but with a different eighth term, and a conversion "
                 "narrative including a public smear over a meal of meat"),
        ("Length", "~7 minutes to read"),
        ("A named historical convert, not an anonymous inquirer", "General "
                                                                   "Sīha is a "
                                                                   "known "
                                                                   "figure in "
                                                                   "the "
                                                                   "tradition, "
                                                                   "and this "
                                                                   "discourse "
                                                                   "is among "
                                                                   "the fuller "
                                                                   "narrative "
                                                                   "conversion "
                                                                   "accounts "
                                                                   "in the "
                                                                   "canon"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the "
                       "longest discourse in this chapter, with several named "
                       "characters and a complete step-by-step conversion "
                       "narrative"),
    ],
    why=(
        "General Sīha, a Jain disciple, is twice talked out of visiting the "
        "Buddha by his own teacher's warning that the Buddha teaches "
        "inaction, but on the third occasion goes anyway, hears the same "
        "eight reinterpreted epithets met at AN 8.11 (with ambition replacing "
        "the first two), converts after a graduated teaching culminating in "
        "the vision of the Dhamma, and hosts the Buddha for a meal that Jain "
        "ascetics falsely claim involved a specially slaughtered calf."),
    guide=[
        ("The teaching in one sentence", [
            "General Sīha, overcoming his own teacher's repeated warning "
            "that the Buddha teaches only inaction, hears from the Buddha "
            "himself that each of eight labels &mdash; inaction, action, "
            "annihilationism, disgust, extermination, mortification, "
            "immaturity, and ambition &mdash; can rightly be said of him, but "
            "each in a specific reinterpreted sense, and converts after a "
            "graduated teaching."]),
        ("Thwarted twice, then going anyway", [
            "Twice, hearing prominent Licchavis praise the Buddha, Sīha "
            "resolves to visit him, and twice his own Jain teacher warns him "
            "off with the claim that the Buddha teaches a doctrine of "
            "inaction. On the third occasion, Sīha reasons that the Jains "
            "can do nothing to him either way, and goes without even taking "
            "leave of his teacher."]),
        ("The same eight epithets, with different substitutions", [
            "Sīha asks directly whether the reports that the Buddha teaches "
            "inaction are accurate. The Buddha answers with the same "
            "structure as AN 8.11 &mdash; each label true in a "
            "reinterpreted sense &mdash; but this list swaps AN 8.11's "
            "opening pair (lacking taste, indelicate) for action as a "
            "positive counterpart to inaction, and closes not with "
            "immaturity but with ambition, reinterpreted as ambition for "
            "the highest solace."]),
        ("Conversion, and a public smear survived", [
            "Taught step by step &mdash; generosity, ethics, heaven, the "
            "drawbacks of sensuality, and finally the four noble truths "
            "&mdash; Sīha attains the vision of the Dhamma and goes for "
            "refuge three times, undeterred even when the Buddha "
            "unexpectedly urges him to keep supporting the Jain ascetics too. "
            "When Jain ascetics later spread a false rumor that Sīha "
            "slaughtered an animal specially for the Buddha's meal, Sīha "
            "dismisses it outright, and the meal proceeds."]),
    ],
    terms=[
        ("akiriyavādo, kiriyavādo",
         "&ldquo;doctrine of inaction, doctrine of action&rdquo; &mdash; the "
         "accusation that first stops Sīha from visiting the Buddha, and the "
         "first pair of epithets the Buddha addresses directly."),
        ("dhammadesanāya cittaṁ pasādesi",
         "the step-by-step teaching that inspires Sīha's mind &mdash; "
         "generosity, ethical conduct, and heaven, then the drawbacks of "
         "sensual pleasure, then the four noble truths."),
        ("virajaṁ vītamalaṁ dhammacakkhuṁ udapādi",
         "&ldquo;the stainless, immaculate vision of the Dhamma arose&rdquo; "
         "&mdash; Sīha's own moment of stream-entry, compared to a clean "
         "cloth properly absorbing dye."),
        ("appekacce niggaṇhitabbaṁ maññanti",
         "part of the Jain ascetics' false public claim about the meal, "
         "&ldquo;a fat calf slaughtered specially&rdquo; &mdash; a smear "
         "Sīha dismisses without hesitation."),
        ("ussāhī, ussoḷhī",
         "&ldquo;ambitious&rdquo; &mdash; the eighth and final epithet in "
         "this discourse's list, reinterpreted as ambition for offering "
         "solace, replacing AN 8.11's closing term, immaturity."),
    ],
    text_intro=(
        "The discourse in full: Sīha's twice-thwarted resolve, his question "
        "and the Buddha's eight-part answer, and his conversion. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sīha's resolve, twice thwarted"),
        ("p", "&sect;1", "an8.12:1.1-6.5"),
        ("h3", "Sīha visits the Buddha, and asks directly"),
        ("p", "&sect;2", "an8.12:7.1-8.4"),
        ("h3", "Eight labels, named"),
        ("p", "&sect;3", "an8.12:9.1-16.2"),
        ("h3", "Eight labels, explained"),
        ("p", "&sect;4", "an8.12:17.1-24.4"),
        ("h3", "Sīha goes for refuge, three times"),
        ("p", "&sect;5", "an8.12:25.1-27.12"),
        ("h3", "Conversion, and the meal"),
        ("p", "&sect;6", "an8.12:28.1-33.3"),
    ],
    quiz=[
        {"q": "What twice stops General Sīha from visiting the Buddha?",
         "opts": [
             "Illness", "His own Jain teacher's warning that the Buddha "
                        "teaches only a doctrine of inaction",
             "Bad weather", "A direct order from the king"],
         "correct": 1,
         "expl": "A repeated warning, overcome only on the third occasion."},
        {"q": "How does this discourse's list of eight labels differ from AN "
              "8.11's list for the same accusation pattern?",
         "opts": [
             "It is completely different, sharing nothing with AN 8.11",
             "It swaps AN 8.11's opening pair for 'action' and closes with "
             "'ambition' instead of 'immaturity'",
             "It has only four items instead of eight",
             "It is word-for-word identical"],
         "correct": 1,
         "expl": "The same structure and most terms, with specific "
                 "substitutions."},
        {"q": "What teaching sequence leads to Sīha's vision of the Dhamma?",
         "opts": [
             "A single abrupt statement with no preparation",
             "A graduated teaching — generosity, ethics, and heaven, the "
             "drawbacks of sensuality, then the four noble truths",
             "Silent meditation with no verbal teaching at all",
             "A debate Sīha must first win"],
         "correct": 1,
         "expl": "The standard graduated teaching, compared to a clean cloth "
                 "absorbing dye."},
        {"q": "What does the Buddha unexpectedly urge Sīha to do, even after "
              "his conversion?",
         "opts": [
             "Abandon his family",
             "Continue supporting the Jain ascetics his family has long "
             "sponsored",
             "Give up all his wealth immediately",
             "Never speak to a Jain again"],
         "correct": 1,
         "expl": "A counterintuitive instruction that further deepens Sīha's "
                 "confidence in the Buddha."},
        {"q": "What false claim do Jain ascetics spread about Sīha's meal for "
              "the Buddha?",
         "opts": [
             "That the food was poisoned",
             "That Sīha slaughtered a fat calf specially for the Buddha's "
             "meal",
             "That the meal was never actually served",
             "That the Buddha refused to eat it"],
         "correct": 1,
         "expl": "A smear campaign Sīha dismisses immediately as untruthful."},
        {"q": "What moment is compared to a clean cloth properly absorbing "
              "dye?",
         "opts": [
             "Sīha's initial resolve to visit the Buddha",
             "The arising of Sīha's stainless, immaculate vision of the "
             "Dhamma",
             "The preparation of the meal",
             "The Jain ascetics' announcement"],
         "correct": 1,
         "expl": "Sīha's own moment of stream-entry, at the end of the "
                 "graduated teaching."},
    ],
    marginalia=[
        ("Thwarted twice, then going", [
            "warned off by his own teacher —",
            "twice turned back, then reasons:",
            "'what can they do to me?'",
        ]),
        ("Eight labels, one swapped", [
            "inaction, action, disgust,",
            "extermination, mortification —",
            "ambition closes it this time",
        ]),
        ("A smear, dismissed outright", [
            "'a calf slaughtered specially' —",
            "false, hollow, untruthful —",
            "Sīha doesn't flinch",
        ]),
        ("Cross-references", [
            "AN 8.11 &middot; previous, the same eight-epithet structure for "
            "Verañja",
            "AN 8.13 &middot; next, a very different register: a royal "
            "thoroughbred",
        ]),
    ],
    further=[
        '<a href="%s/an8.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.11.html">AN 8.11 &middot; At Verañjā</a> &mdash; previous, the same '
        "eight-epithet structure.",
        '<a href="an-8.13.html">AN 8.13 &middot; A Thoroughbred</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.13 — Assājānīyasutta
# --------------------------------------------------------------------------- #
page(
    13, "Assājānīya", "A Thoroughbred",
    vagga=VAGGA_2,
    meta_title="AN 8.13 — A Thoroughbred | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Assājānīyasutta, mapping eight factors that make a royal "
        "thoroughbred worthy of a king onto eight parallel qualities that "
        "make a mendicant the supreme field of merit for the world. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "An eight-factor simile — the fine royal thoroughbred "
                 "&mdash; mapped point for point onto eight qualities of a "
                 "mendicant worthy of offerings"),
        ("Length", "~2 minutes to read"),
        ("The noble eightfold path, embedded mid-list", "The seventh factor, "
                                                         "&ldquo;always walks "
                                                         "in a straight "
                                                         "path,&rdquo; is "
                                                         "explicitly glossed "
                                                         "as the noble "
                                                         "eightfold path "
                                                         "itself, an eight-"
                                                         "item structure "
                                                         "nested inside this "
                                                         "chapter's own "
                                                         "eight-item simile"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear "
                       "point-for-point simile, easy to follow once the "
                       "horse-to-mendicant mapping is seen"),
    ],
    why=(
        "AN 8.13 lists eight factors that make a fine royal thoroughbred "
        "worthy of a king &mdash; good breeding, good origin, careful "
        "eating, disgust at filth, gentleness, showing his tricks openly, "
        "reliably carrying his load, walking a straight path, and enduring "
        "strength &mdash; then maps each, point for point, onto eight "
        "qualities that make a mendicant the supreme field of merit for the "
        "world."),
    guide=[
        ("The teaching in one sentence", [
            "Just as a fine royal thoroughbred with eight factors is worthy "
            "of a king, a mendicant with eight parallel qualities &mdash; "
            "ethical restraint, careful eating, disgust at bad conduct, "
            "gentleness, openness about their own faults, reliable training, "
            "walking the noble eightfold path, and energetic endurance "
            "&mdash; is worthy of offerings and the supreme field of merit "
            "for the world."]),
        ("Eight factors of a fine horse", [
            "Good birth on both sides, bred in the right region, careful "
            "eating without mess, disgust at soiling himself, gentleness "
            "with other horses, openly showing his trainer his tricks and "
            "feints so they can be corrected, reliably carrying his load "
            "regardless of what others do, walking a straight path, and "
            "remaining strong even to the point of death."]),
        ("The same eight, mapped to a mendicant", [
            "Each equine factor becomes a monastic parallel: good breeding "
            "becomes ethical restraint; careful eating becomes eating "
            "without complaint whether the food is coarse or fine; disgust "
            "at filth becomes disgust at bad conduct; showing tricks to a "
            "trainer becomes openly showing one's own faults to sensible "
            "companions so they can be corrected; and reliable strength "
            "becomes an explicit vow to keep trying even at the cost of "
            "skin, sinew, bone, blood, and flesh."]),
        ("A straight path, glossed as the eightfold path itself", [
            "Where the horse simply walks in a straight line, the mendicant "
            "parallel names exactly what that straight path is: right view, "
            "right purpose, right speech, right action, right livelihood, "
            "right effort, right mindfulness, and right immersion &mdash; "
            "the noble eightfold path, embedded as a second eight-item "
            "structure inside this discourse's own eightfold simile."]),
    ],
    terms=[
        ("ājānīyo",
         "&ldquo;thoroughbred&rdquo; &mdash; this discourse's own title "
         "term, a horse of proven fine breeding, matched against a "
         "mendicant's own worthiness."),
        ("ubhato sujāto hoti mātito ca pitito ca",
         "&ldquo;well born on both the mother's and the father's "
         "sides&rdquo; &mdash; the horse's first factor, paralleled by the "
         "mendicant's own ethical restraint rather than literal ancestry."),
        ("bhinnesu sikkhāpadesu tikicchaṁ dasseti sāraṇīyehi "
         "sabrahmacārīhi",
         "&ldquo;openly shows their tricks, bluffs, ruses, and feints to "
         "their sensible spiritual companions&rdquo; &mdash; the "
         "seventh-factor parallel, honesty about one's own faults rather "
         "than concealment."),
        ("ujuṁyeva maggaṁ gacchati",
         "&ldquo;always walks in a straight path&rdquo; &mdash; the eighth "
         "factor, explicitly glossed for the mendicant as the noble "
         "eightfold path itself."),
        ("āhuneyyo pāhuneyyo dakkhiṇeyyo añjalikaraṇīyo anuttaraṁ "
         "puññakkhettaṁ lokassa",
         "&ldquo;worthy of offerings dedicated to the gods... the supreme "
         "field of merit for the world&rdquo; &mdash; the standing "
         "description this book has already applied elsewhere, here earned "
         "through the eight-factor thoroughbred simile."),
    ],
    text_intro=(
        "The discourse in full: the eight factors of a fine thoroughbred, and "
        "their eight mendicant parallels. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight factors of a fine royal thoroughbred"),
        ("p", "&sect;1", "an8.13:1.1-1.17"),
        ("h3", "The same eight, mapped to a mendicant"),
        ("p", "&sect;2", "an8.13:2.1-2.19"),
    ],
    quiz=[
        {"q": "What does this discourse compare a mendicant worthy of "
              "offerings to?",
         "opts": [
             "A well-tuned lute", "A fine royal thoroughbred with eight "
                                   "factors",
             "A lotus flower", "A ship crossing the ocean"],
         "correct": 1,
         "expl": "A point-for-point equine simile, mapped onto eight "
                 "monastic qualities."},
        {"q": "What does the horse's factor of 'openly showing tricks to a "
              "trainer' become in the mendicant parallel?",
         "opts": [
             "Concealing one's faults from others",
             "Openly showing one's own faults to sensible spiritual "
             "companions so they can be corrected",
             "Refusing all correction",
             "Publicly shaming other mendicants"],
         "correct": 1,
         "expl": "Honesty about one's own faults, not concealment."},
        {"q": "What is the horse's eighth factor, 'always walks in a "
              "straight path,' explicitly glossed as for the mendicant?",
         "opts": [
             "Walking meditation practice",
             "The noble eightfold path — right view through right "
             "immersion",
             "A literal straight road to the monastery",
             "Avoiding all travel"],
         "correct": 1,
         "expl": "An eight-item structure nested inside this discourse's own "
                 "eightfold simile."},
        {"q": "What does the mendicant parallel to the horse's 'enduring "
              "strength even to death' consist of?",
         "opts": [
             "Physical exercise routines",
             "An explicit vow to keep trying until success, even at the "
             "cost of skin, sinew, bone, blood, and flesh",
             "Fasting for extended periods",
             "Competing with other mendicants"],
         "correct": 1,
         "expl": "Energetic determination, stated in the mendicant's own "
                 "words."},
        {"q": "What closing description does this discourse apply to a "
              "mendicant with all eight qualities?",
         "opts": [
             "Wealthy and well-connected",
             "Worthy of offerings, hospitality, and religious donation — the "
             "supreme field of merit for the world",
             "Physically the strongest in the Saṅgha",
             "Guaranteed a favorable rebirth only"],
         "correct": 1,
         "expl": "The standing description this book has applied to worthy "
                 "individuals elsewhere."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Vesālī",
             "No setting is stated in the source", "Yes, at Campā"],
         "correct": 2,
         "expl": "A bare formula, like several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight factors of a fine horse", [
            "well bred, careful eating,",
            "disgusted by filth, gentle,",
            "open, reliable, straight, strong",
        ]),
        ("Mapped to a mendicant", [
            "breeding becomes ethics,",
            "tricks shown become honesty —",
            "point for point, horse to monk",
        ]),
        ("An eightfold path within eight", [
            "'walks a straight path' becomes",
            "right view through right immersion —",
            "one eight nested in another",
        ]),
        ("Cross-references", [
            "AN 8.12 &middot; previous, General Sīha's conversion",
            "AN 8.14 &middot; next, a very different horse simile — this "
            "time about failure",
        ]),
    ],
    further=[
        '<a href="%s/an8.13/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.12.html">AN 8.12 &middot; With Sīha</a> &mdash; previous.',
        '<a href="an-8.14.html">AN 8.14 &middot; A Wild Colt</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.14 — Assakhaḷuṅkasutta
# --------------------------------------------------------------------------- #
page(
    14, "Assakhaḷuṅka", "A Wild Colt",
    vagga=VAGGA_2,
    meta_title="AN 8.14 — A Wild Colt | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Assakhaḷuṅkasutta, mapping eight defects in an untrained horse onto "
        "eight distinct ways a mendicant can respond badly when accused of "
        "an offense, related to but structurally different from AN 8.10's "
        "trash simile. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight named defects in an untrained horse, each mapped one "
                 "for one onto eight distinct bad responses to an "
                 "accusation of a monastic offense"),
        ("Length", "~3 minutes to read"),
        ("Not AN 8.10's trash simile", "AN 8.10 gave a single type of "
                                       "corrupt individual through four "
                                       "different similes; this discourse "
                                       "gives eight genuinely distinct "
                                       "behavioral patterns, each mapped "
                                       "one for one to a specific horse "
                                       "defect, not four similes for one "
                                       "type"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; eight "
                       "parallel structures, repetitive but each pairing "
                       "distinct once read closely"),
    ],
    why=(
        "AN 8.14 names eight defects in wild, untrained colts &mdash; "
        "backing up, wrecking the chariot, shaking off the pole, veering off "
        "track, rearing up, ignoring the trainer, standing stock still, and "
        "sitting down &mdash; and maps each, one for one, onto eight "
        "distinct ways a mendicant accused of an offense can respond badly, "
        "from claiming not to remember to resigning the training in a huff."),
    guide=[
        ("The teaching in one sentence", [
            "Just as eight kinds of wild, untrained colt resist a trainer's "
            "command in eight distinct ways, a mendicant accused of an "
            "offense can respond badly in eight distinct ways &mdash; from "
            "evasive forgetting to hostile counter-accusation to abrupt "
            "resignation &mdash; each compared to a specific horse defect."]),
        ("Eight defects, eight distinct responses", [
            "Unlike a repeated refrain applied to one behavior, this "
            "discourse pairs eight genuinely different horse defects with "
            "eight genuinely different human responses: backing up pairs "
            "with claiming not to remember the offense; wrecking the hub "
            "pairs with insulting the accuser's competence; shaking off the "
            "pole pairs with counter-accusing the accuser of their own "
            "offense; veering off track pairs with the same evasive "
            "distraction tactic met at AN 8.10."]),
        ("Not AN 8.10's single corrupt type, restructured", [
            "AN 8.10 built four similes &mdash; bad barley, winnowed chaff, "
            "rotten wood, trash &mdash; around one recurring type of corrupt "
            "individual, recognized only once exposed. This discourse takes "
            "a different structural approach entirely: eight distinct "
            "behavioral patterns, each earning its own horse-defect "
            "comparison, not four variations on a single portrait."]),
        ("From gesticulating to resignation", [
            "The remaining pairings: rearing up pairs with gesticulating "
            "wildly while speaking before the Saṅgha; ignoring the trainer "
            "pairs with a guilty mendicant simply going wherever they want; "
            "standing stock still pairs with frustrating the Saṅgha through "
            "silence; and sitting down pairs with abruptly resigning the "
            "training and taunting, &ldquo;are you happy now?&rdquo;"]),
    ],
    terms=[
        ("assakhaḷuṅko",
         "&ldquo;wild colt&rdquo; &mdash; this discourse's own title term, "
         "an untrained horse resistant to its trainer's commands."),
        ("codito codito āpattiṁ apassanto assati paṭicarati",
         "&ldquo;evades it by saying they don't remember&rdquo; &mdash; the "
         "first of the eight bad responses, paired with a colt that backs "
         "up and spins the chariot."),
        ("codakaññeva paccāropeti",
         "&ldquo;retorts to the accuser: you've fallen into such-and-such an "
         "offense&rdquo; &mdash; a counter-accusation, paired with a colt "
         "that shakes off the draft-pole and tramples it."),
        ("aññenaññaṁ paṭicarati, bahiddhā kathaṁ apanāmeti, kopañca "
         "dosañca appaccayañca pātukaroti",
         "&ldquo;dodges the issue, distracts the discussion with irrelevant "
         "points, and displays annoyance, hate, and bitterness&rdquo; "
         "&mdash; the same evasive tactic named in AN 8.10, here paired with "
         "a colt veering off track."),
        ("sikkhaṁ paccakkhāya hīnāyāvattissāmi",
         "&ldquo;I'll resign the training and return to a lesser life&rdquo; "
         "&mdash; the eighth and final bad response, an abrupt resignation "
         "paired with a colt that simply sits down."),
    ],
    text_intro=(
        "The discourse in full: eight defects in wild colts, and their eight "
        "distinct human parallels. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight defects in wild colts"),
        ("p", "&sect;1", "an8.14:1.1-9.4"),
        ("h3", "Eight defects in people, matched one for one"),
        ("p", "&sect;2", "an8.14:10.1-17.10"),
    ],
    quiz=[
        {"q": "How does this discourse's structure differ from AN 8.10's "
              "trash simile, according to the guide?",
         "opts": [
             "They are structurally identical",
             "AN 8.10 gives four similes for one recurring corrupt type; "
             "this discourse gives eight genuinely distinct behaviors, each "
             "mapped one for one to a specific horse defect",
             "This discourse has no similes at all",
             "AN 8.10 involves horses instead of barley"],
         "correct": 1,
         "expl": "One type through four similes, versus eight distinct "
                 "types through eight parallel pairings."},
        {"q": "What is the first of the eight bad responses to an "
              "accusation, and its matching horse defect?",
         "opts": [
             "Immediate confession, paired with a well-trained horse",
             "Evading by claiming not to remember, paired with a colt that "
             "backs up and spins the chariot",
             "Silent agreement, paired with a resting horse",
             "Public apology, paired with a galloping horse"],
         "correct": 1,
         "expl": "The first of eight distinct pairings, not a repeated "
                 "refrain."},
        {"q": "What evasive tactic does this discourse share with AN 8.10?",
         "opts": [
             "No shared tactic at all",
             "Dodging the issue, distracting with irrelevant points, and "
             "displaying annoyance, hate, and bitterness",
             "Both involve accusations of theft",
             "Both are set at the same location"],
         "correct": 1,
         "expl": "The identical evasive phrase, paired here with a colt "
                 "veering off track."},
        {"q": "What is the eighth and final bad response?",
         "opts": [
             "Formally apologizing to the Saṅgha",
             "Abruptly resigning the training and taunting, 'are you happy "
             "now?'",
             "Requesting a formal hearing",
             "Reporting the accuser to outside authorities"],
         "correct": 1,
         "expl": "Paired with a colt that simply sits down, refusing to "
                 "move at all."},
        {"q": "What does gesticulating wildly while speaking before the "
              "Saṅgha get compared to?",
         "opts": [
             "A calm, well-trained horse", "A colt that rears up and "
                                            "strikes out with its fore-legs",
             "A horse standing still", "A horse carrying a heavy load"],
         "correct": 1,
         "expl": "One of the eight distinct pairings in this discourse's "
                 "structure."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Campā"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight colts, eight defects", [
            "backs up · wrecks the hub ·",
            "shakes off the pole · veers off ·",
            "rears · ignores · stands · sits",
        ]),
        ("Eight distinct responses, not four similes", [
            "unlike AN 8.10's",
            "one type through four images —",
            "here, eight genuinely different",
        ]),
        ("From forgetting to resignation", [
            "'I don't remember' —",
            "to 'are you happy now?' —",
            "eight ways to respond badly",
        ]),
        ("Cross-references", [
            "AN 8.13 &middot; previous, a thoroughbred's eight virtues",
            "AN 8.10 &middot; earlier, the trash simile this discourse "
            "relates to but structurally differs from",
        ]),
    ],
    further=[
        '<a href="%s/an8.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.13.html">AN 8.13 &middot; A Thoroughbred</a> &mdash; previous.',
        '<a href="an-8.15.html">AN 8.15 &middot; Stains</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.15 — Malasutta
# --------------------------------------------------------------------------- #
page(
    15, "Mala", "Stains",
    vagga=VAGGA_2,
    meta_title="AN 8.15 — Stains | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Malasutta, a short, pithy list of eight everyday stains — of "
        "hymns, houses, beauty, guards, women, givers, and the world itself "
        "— crowned by ignorance as the worst stain of all. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item prose list, immediately restated in verse "
                 "with minor rephrasing"),
        ("Length", "under 1 minute to read"),
        ("A domestic, everyday register", "Unlike this chapter's grander "
                                          "similes and narratives, this "
                                          "discourse draws its seven "
                                          "ordinary stains from daily life "
                                          "&mdash; hymns, houses, beauty, "
                                          "guards, women, givers &mdash; "
                                          "before naming ignorance as worse "
                                          "than all of them combined"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "aphoristic, easy to read but each pairing rewards a "
                       "second look"),
    ],
    why=(
        "AN 8.15 names eight stains &mdash; failing to rehearse spoils "
        "hymns, neglect spoils houses, laziness spoils beauty, negligence "
        "spoils a guard, misconduct spoils a woman, stinginess spoils a "
        "giver, and bad unskillful qualities are a stain on this world and "
        "the next &mdash; then names a stain worse than all seven "
        "combined: ignorance."),
    guide=[
        ("The teaching in one sentence", [
            "Seven everyday things each have their own particular stain "
            "&mdash; unrehearsed hymns, neglected houses, lazy beauty, a "
            "negligent guard, a misbehaving woman, a stingy giver, and bad "
            "qualities staining this world and the next &mdash; but "
            "ignorance is worse than all of them, the worst stain of all."]),
        ("Seven domestic stains, each specific to its object", [
            "Each of the first seven pairings names a stain that belongs "
            "specifically to one thing: a hymn is stained by not being "
            "rehearsed, a house by neglect, beauty by laziness, a guard's "
            "post by negligence, a woman's standing by misconduct, and a "
            "giver's generosity by stinginess &mdash; each stain the "
            "specific failure that spoils that specific thing's own "
            "purpose."]),
        ("The seventh item widens the frame", [
            "Where the first six stains are narrow and domestic, the "
            "seventh breaks the pattern's scale: bad, unskillful qualities "
            "generally are named as a stain not on any one object but on "
            "this world and the next world both &mdash; a bridge from small "
            "household failures to something with consequences beyond a "
            "single lifetime."]),
        ("Ignorance, worse than the rest combined", [
            "The list's climax names an eighth stain that isn't simply "
            "another item alongside the first seven, but is explicitly "
            "ranked above them: worse than any of these, ignorance is "
            "called the worst stain of all &mdash; the discourse's own "
            "verse repeats this ranking word for word."]),
    ],
    terms=[
        ("malaṁ",
         "&ldquo;stain&rdquo; &mdash; this discourse's own title term, "
         "applied to seven specific objects and then, worst of all, to "
         "ignorance itself."),
        ("asajjhāyamalā mantā",
         "&ldquo;not rehearsing is the stain of hymns&rdquo; &mdash; the "
         "first pairing, a specific failure of practice spoiling a specific "
         "skill."),
        ("anuṭṭhānamalā gharā",
         "&ldquo;neglect is the stain of houses&rdquo; &mdash; the second "
         "pairing, extending the same logic from spoken skill to physical "
         "upkeep."),
        ("pāpo dhammo ubhayattha malaṁ",
         "&ldquo;bad, unskillful qualities are a stain in this world and "
         "the next&rdquo; &mdash; the seventh item, widening the list's "
         "scale from domestic objects to consequences beyond a single "
         "life."),
        ("tato malā malataraṁ avijjā paramaṁ malaṁ",
         "&ldquo;worse than any of these is ignorance, the worst stain of "
         "all&rdquo; &mdash; the discourse's own climactic ranking, repeated "
         "word for word in both the prose list and the closing verse."),
    ],
    text_intro=(
        "The discourse in full: eight stains in prose, then restated in "
        "verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight stains, in prose"),
        ("p", "&sect;1", "an8.15:1.1-1.11"),
        ("h3", "The same eight, in verse"),
        ("p", "&sect;2", "an8.15:2.1-2.4"),
        ("p", "&sect;3", "an8.15:3.1-3.6"),
    ],
    quiz=[
        {"q": "What stains a hymn, according to this discourse?",
         "opts": [
             "Speaking too loudly", "Not rehearsing it",
             "Learning it from an unqualified teacher", "Reciting it too "
                                                          "often"],
         "correct": 1,
         "expl": "The first of seven specific, domestic stains."},
        {"q": "How does the guide describe the seventh item in this list, "
              "compared to the first six?",
         "opts": [
             "It is identical in scale to the first six",
             "It widens the frame — bad unskillful qualities stain not one "
             "object but this world and the next",
             "It is unrelated to the rest of the list",
             "It only applies to monastics"],
         "correct": 1,
         "expl": "A bridge from small domestic failures to consequences "
                 "beyond one lifetime."},
        {"q": "What is named as worse than all seven other stains combined?",
         "opts": [
             "Poverty", "Ignorance, the worst stain of all",
             "Old age", "Physical illness"],
         "correct": 1,
         "expl": "The discourse's climactic ranking, repeated word for word "
                 "in the closing verse."},
        {"q": "What stains a giver, according to this discourse?",
         "opts": [
             "Giving too much", "Stinginess",
             "Giving to the wrong recipient", "Giving in public"],
         "correct": 1,
         "expl": "The sixth of seven specific pairings, each naming a "
                 "particular failure."},
        {"q": "How is the eight-item list structured?",
         "opts": [
             "As a blocking list matched by its reversal",
             "As a bare prose list, immediately restated in verse with "
             "minor rephrasing",
             "As a dialogue between two characters",
             "As a long narrative"],
         "correct": 1,
         "expl": "Brief and aphoristic, prose followed by verse."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Vesālī",
             "No setting is stated in the source", "Yes, at Rājagaha"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Seven domestic stains", [
            "unrehearsed hymns, neglected",
            "houses, lazy beauty,",
            "a negligent guard, a stingy giver",
        ]),
        ("From household to two worlds", [
            "the seventh item widens:",
            "bad qualities stain not one thing",
            "but this world and the next",
        ]),
        ("Ignorance, worst of all", [
            "worse than the other seven —",
            "the climax of the list,",
            "repeated once more in verse",
        ]),
        ("Cross-references", [
            "AN 8.14 &middot; previous, eight ways to respond badly to an "
            "accusation",
            "AN 8.16 &middot; next, the qualities that make a mendicant "
            "worthy of going on a mission",
        ]),
    ],
    further=[
        '<a href="%s/an8.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.14.html">AN 8.14 &middot; A Wild Colt</a> &mdash; previous.',
        '<a href="an-8.16.html">AN 8.16 &middot; Going on a Mission</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.16 — Dūteyyasutta
# --------------------------------------------------------------------------- #
page(
    16, "Dūteyya", "Going on a Mission",
    vagga=VAGGA_2,
    meta_title="AN 8.16 — Going on a Mission | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dūteyyasutta, naming five qualities that make a mendicant fit to "
        "serve as an envoy, then holding up Venerable Sāriputta by name as "
        "someone who embodies them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A general list of qualities stated once, then restated as a "
                 "portrait of a single named individual, closing with three "
                 "summary verses"),
        ("Length", "under 1 minute to read"),
        ("A count worth checking closely", "The source's own list names five "
                                            "qualities in prose &mdash; "
                                            "learning and educating, "
                                            "memorizing, understanding, "
                                            "skill at what's on topic, and "
                                            "not causing quarrels &mdash; "
                                            "not eight discrete items, "
                                            "despite this discourse's place "
                                            "in the Book of the Eights"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "naming a real disciple by name rather than staying "
                       "purely abstract"),
    ],
    why=(
        "AN 8.16 names the qualities that make a mendicant worthy of going "
        "on a mission &mdash; learning and teaching well, remembering "
        "accurately, understanding and helping others understand, staying "
        "on topic, and not causing quarrels &mdash; and then says Venerable "
        "Sāriputta has exactly these qualities, naming him directly as the "
        "model."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant worthy of going on a mission learns and teaches "
            "well, remembers accurately, understands and helps others "
            "understand, stays skillfully on topic, and doesn't cause "
            "quarrels &mdash; and Venerable Sāriputta is named directly as "
            "someone who has exactly these qualities."]),
        ("A general principle, then a named embodiment", [
            "Unlike most of this chapter's discourses, which stay entirely "
            "abstract, this one follows its general statement with a "
            "second, nearly identical restatement naming Sāriputta by name "
            "&mdash; the Buddha's own foremost disciple in wisdom &mdash; as "
            "someone who actually has these qualities, not merely a "
            "hypothetical mendicant who might."]),
        ("A count that doesn't cleanly reach eight", [
            "Despite its place in the Book of the Eights, the source's own "
            "list of qualities for a worthy envoy numbers five in the "
            "prose, not eight: learns and educates others, memorizes and "
            "remembers, understands and helps others understand, is skilled "
            "at what's on and off topic, and doesn't cause quarrels. This "
            "discourse belongs to this nipāta by placement, not by "
            "presenting a clean eightfold list."]),
        ("Composure under pressure, added in verse", [
            "The closing verses add a further dimension beyond the prose "
            "list: such a mendicant doesn't tremble arriving at an assembly "
            "of fierce debaters, doesn't miss out words or conceal "
            "instructions, and their words aren't poisoned even when "
            "questioned closely &mdash; composure and precision under "
            "pressure, not just competence in calm conditions."]),
    ],
    terms=[
        ("dūteyyaṁ gantuṁ",
         "&ldquo;going on a mission&rdquo; &mdash; this discourse's own "
         "title-phrase, the role a qualified mendicant is fit to serve."),
        ("sussūsati saussūsāpeti",
         "&ldquo;learns and educates others&rdquo; &mdash; the first "
         "quality named, both receiving and transmitting the teaching."),
        ("ṭhānāṭhānakusalo",
         "&ldquo;skilled at knowing what's on topic and what isn't&rdquo; "
         "&mdash; the fourth quality, discernment about relevance in "
         "discussion."),
        ("na ca bhaṇḍanakārako",
         "&ldquo;doesn't cause quarrels&rdquo; &mdash; the fifth and final "
         "quality named in the prose list."),
        ("sāriputto",
         "Venerable Sāriputta, named directly as embodying all the "
         "qualities of a mendicant worthy of going on a mission."),
    ],
    text_intro=(
        "The discourse in full: the qualities of a worthy envoy, restated for "
        "Sāriputta, and three closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The qualities, general and then named for Sāriputta"),
        ("p", "&sect;1", "an8.16:1.1-1.8"),
        ("h3", "Closing verses: composure under pressure"),
        ("p", "&sect;2", "an8.16:2.1-2.4"),
        ("p", "&sect;3", "an8.16:3.1-3.4"),
    ],
    quiz=[
        {"q": "What does this discourse do after stating its general list of "
              "qualities?",
         "opts": [
             "Nothing further; the discourse ends there",
             "It restates the same qualities, this time naming Venerable "
             "Sāriputta directly as someone who has them",
             "It contradicts the general list",
             "It lists eight additional qualities"],
         "correct": 1,
         "expl": "A general principle followed by a named embodiment, "
                 "unusual for this chapter."},
        {"q": "According to the guide, how many qualities does the source's "
              "own prose list actually name?",
         "opts": [
             "Exactly eight, matching this chapter's usual theme",
             "Five — despite this discourse's place in the Book of the "
             "Eights",
             "Three", "Twelve"],
         "correct": 1,
         "expl": "A discourse included by placement, not by presenting a "
                 "clean eightfold list."},
        {"q": "What do the closing verses add beyond the prose list?",
         "opts": [
             "A warning against ever going on a mission",
             "Composure under pressure — not trembling before fierce "
             "debaters, and speaking without poisoned words even when "
             "questioned closely",
             "A description of the envoy's clothing",
             "A list of forbidden topics"],
         "correct": 1,
         "expl": "Precision and composure under difficult conditions, not "
                 "just competence when calm."},
        {"q": "Who is named directly as embodying these qualities?",
         "opts": [
             "Venerable Ānanda", "Venerable Sāriputta",
             "Venerable Mahāmoggallāna", "General Sīha"],
         "correct": 1,
         "expl": "The Buddha's own foremost disciple in wisdom, named by "
                 "name."},
        {"q": "What is the fifth quality named in the prose list?",
         "opts": [
             "Physical strength", "Not causing quarrels",
             "Wealth", "Skill in debate alone"],
         "correct": 1,
         "expl": "Closing the list of five qualities named for a worthy "
                 "envoy."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Five qualities, named twice", [
            "learns, remembers,",
            "understands, stays on topic,",
            "doesn't cause quarrels",
        ]),
        ("Not abstract — Sāriputta", [
            "the general principle",
            "restated with a real name —",
            "the Buddha's own foremost disciple",
        ]),
        ("A count that doesn't reach eight", [
            "five qualities in prose,",
            "not eight — included here",
            "by placement, not by count",
        ]),
        ("Cross-references", [
            "AN 8.15 &middot; previous, eight everyday stains",
            "AN 8.17 &middot; next, a very different subject: how a woman "
            "catches a man",
        ]),
    ],
    further=[
        '<a href="%s/an8.16/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.15.html">AN 8.15 &middot; Stains</a> &mdash; previous.',
        '<a href="an-8.17.html">AN 8.17 &middot; Catching (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.17 — Paṭhamabandhanasutta
# --------------------------------------------------------------------------- #
page(
    17, "Paṭhamabandhana", "Catching (1st)",
    vagga=VAGGA_2,
    meta_title="AN 8.17 — Catching (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamabandhanasutta, an eight-item list of the features a woman "
        "uses to catch a man, closing with the claim that touch is the "
        "surest catch of all. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item list, closing with a single ranking "
                 "statement"),
        ("Length", "under 1 minute to read"),
        ("The first half of a gender-mirrored pair", "This discourse and AN "
                                                      "8.18 immediately "
                                                      "following present the "
                                                      "identical eight "
                                                      "features and identical "
                                                      "closing claim, with "
                                                      "only the subject and "
                                                      "object of "
                                                      "&ldquo;catching&rdquo; "
                                                      "reversed"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "direct; this reading guide presents the content "
                       "honestly without softening its frank treatment of "
                       "attraction"),
    ],
    why=(
        "AN 8.17 names eight features &mdash; weeping, laughing, speaking, "
        "appearance, gifts of wildflowers, scents, tastes, and touches "
        "&mdash; that a woman uses to catch a man, closing with the claim "
        "that of all eight, being caught by touch is the surest catch of "
        "all."),
    guide=[
        ("The teaching in one sentence", [
            "A woman catches a man using eight features &mdash; weeping, "
            "laughing, speaking, appearance, gifts of wildflowers, scents, "
            "tastes, and touches &mdash; but of all eight, those caught by "
            "touch are said to be the most thoroughly caught."]),
        ("A frank, unsentimental catalog", [
            "This discourse doesn't moralize or instruct; it simply "
            "catalogs eight means of attraction and capture, from "
            "expressive behavior (weeping, laughing, speaking) through "
            "physical presentation (appearance) to direct sensory "
            "offering (flowers, scents, tastes, touches), without editorial "
            "comment on any of the eight."]),
        ("Touch, singled out as strongest", [
            "The discourse's only evaluative move is its closing line: "
            "among all eight means of catching, being caught by touch is "
            "called being &ldquo;well and truly caught.&rdquo; The list "
            "moves from the least physically direct (weeping, laughing) "
            "toward the most direct (touch), and the closing line confirms "
            "that gradient by naming the final item as strongest."]),
        ("Paired with AN 8.18, the mirror image", [
            "This is the first half of a matched pair. AN 8.18, immediately "
            "following, presents the identical eight features and identical "
            "closing claim, with only the subject and object reversed: a "
            "man catching a woman rather than a woman catching a man &mdash; "
            "a symmetrical treatment, not a one-sided portrait of either "
            "gender."]),
    ],
    terms=[
        ("bandhati",
         "&ldquo;catches, binds&rdquo; &mdash; the discourse's own key "
         "verb, and the root of its Pāli title, Paṭhamabandhanasutta, "
         "&ldquo;the first discourse on binding.&rdquo;"),
        ("rodanena, hasanena, bhaṇitena",
         "&ldquo;with weeping, laughing, speaking&rdquo; &mdash; the first "
         "three of the eight features, all expressive behaviors rather than "
         "physical gifts."),
        ("vanabhaṅgena",
         "&ldquo;gifts of wildflowers&rdquo; &mdash; the fifth feature, "
         "opening the list's shift from behavior toward direct sensory "
         "offering."),
        ("gandhena, rasena, phoṭṭhabbena",
         "&ldquo;with scents, tastes, and touches&rdquo; &mdash; the final "
         "three features, closing the list at its most physically direct."),
        ("phassabandhanā ye baddhā, susaṅkhātā tesaṁ bandhanā",
         "&ldquo;those beings who are caught by touch are well and truly "
         "caught&rdquo; &mdash; the discourse's own closing ranking, singling "
         "out touch as the strongest of the eight."),
    ],
    text_intro=(
        "The discourse in full: eight features that catch, and touch named "
        "strongest of all. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight features that catch"),
        ("p", "&sect;1", "an8.17:1.1-1.12"),
    ],
    quiz=[
        {"q": "What eight features does this discourse name?",
         "opts": [
             "The five hindrances plus three more",
             "Weeping, laughing, speaking, appearance, gifts of "
             "wildflowers, scents, tastes, and touches",
             "The seven factors of awakening plus one",
             "Eight monastic requisites"],
         "correct": 1,
         "expl": "A catalog moving from expressive behavior to direct "
                 "sensory offering."},
        {"q": "Which of the eight features is singled out as strongest?",
         "opts": [
             "Weeping", "Touch — those caught by it are 'well and truly "
                         "caught'",
             "Appearance", "Speaking"],
         "correct": 1,
         "expl": "The discourse's only evaluative move, closing the list."},
        {"q": "How does this discourse relate to AN 8.18, immediately "
              "following it?",
         "opts": [
             "No relation at all",
             "AN 8.18 presents the identical eight features and closing "
             "claim, with the subject and object of 'catching' reversed",
             "AN 8.18 contradicts this discourse entirely",
             "AN 8.18 is set centuries later"],
         "correct": 1,
         "expl": "A symmetrical, gender-mirrored pair, not a one-sided "
                 "portrait."},
        {"q": "How does the guide characterize this discourse's approach to "
              "its subject?",
         "opts": [
             "Heavily moralizing and instructive",
             "A frank, unsentimental catalog without editorial comment, "
             "apart from the closing ranking",
             "Entirely metaphorical, not about literal attraction",
             "Addressed only to laypeople"],
         "correct": 1,
         "expl": "Presented without softening, as this reading guide notes "
                 "explicitly."},
        {"q": "What is the discourse's own Pāli title term, and what does it "
              "mean?",
         "opts": [
             "Mettā, 'love'", "Bandhana, 'binding, catching'",
             "Paññā, 'wisdom'", "Sīla, 'ethics'"],
         "correct": 1,
         "expl": "The root of this discourse's Pāli title, "
                 "Paṭhamabandhanasutta."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Vesālī",
             "No setting is stated in the source", "Yes, at Rājagaha"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight features that catch", [
            "weeping, laughing, speaking,",
            "appearance, flowers, scents,",
            "tastes, and touches",
        ]),
        ("Touch, named strongest", [
            "of all eight means of catching,",
            "the discourse's only ranking:",
            "touch catches most thoroughly",
        ]),
        ("A mirrored pair follows", [
            "the identical eight features,",
            "the identical closing line —",
            "next, reversed: man catching woman",
        ]),
        ("Cross-references", [
            "AN 8.16 &middot; previous, the qualities of a worthy envoy",
            "AN 8.18 &middot; next, the mirror image of this same list",
        ]),
    ],
    further=[
        '<a href="%s/an8.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.16.html">AN 8.16 &middot; Going on a Mission</a> &mdash; previous.',
        '<a href="an-8.18.html">AN 8.18 &middot; Catching (2nd)</a> &mdash; next, the mirror '
        "image of this same list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.18 — Dutiyabandhanasutta
# --------------------------------------------------------------------------- #
page(
    18, "Dutiyabandhana", "Catching (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 8.18 — Catching (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyabandhanasutta, the mirror image of AN 8.17: the identical "
        "eight features a man uses to catch a woman, closing with the same "
        "ranking of touch as the surest catch. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical eight-item list and closing ranking as AN "
                 "8.17, with subject and object reversed"),
        ("Length", "under 1 minute to read"),
        ("A deliberate mirror, not a variant", "Every one of the eight "
                                               "features and the closing "
                                               "line match AN 8.17 word for "
                                               "word; only 'a woman catches "
                                               "a man' becomes 'a man "
                                               "catches a woman,' a "
                                               "symmetry this reading guide "
                                               "treats as the discourse's "
                                               "own point"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; identical "
                       "in structure to AN 8.17, read together as a pair"),
    ],
    why=(
        "AN 8.18 restates AN 8.17's eight features &mdash; weeping, "
        "laughing, speaking, appearance, gifts of wildflowers, scents, "
        "tastes, and touches &mdash; and its closing claim that touch is "
        "the surest catch, with only the direction of &ldquo;catching&rdquo; "
        "reversed: a man catching a woman, rather than a woman catching a "
        "man."),
    guide=[
        ("The teaching in one sentence", [
            "A man catches a woman using the same eight features named in "
            "AN 8.17 &mdash; weeping, laughing, speaking, appearance, gifts "
            "of wildflowers, scents, tastes, and touches &mdash; and, as in "
            "AN 8.17, those caught by touch are said to be the most "
            "thoroughly caught."]),
        ("A deliberate, exact mirror", [
            "Nothing in this discourse's content differs from AN 8.17 "
            "except the direction of the verb: where AN 8.17 says a woman "
            "catches a man, this discourse says a man catches a woman. "
            "Every one of the eight features and the closing evaluative "
            "line are otherwise identical, word for word."]),
        ("Symmetry as the discourse's own point", [
            "Read as a pair, AN 8.17 and AN 8.18 make a claim through their "
            "very structure: attraction and capture by these eight means "
            "run in both directions equally, not as a fault attributed to "
            "one gender and a vulnerability attributed to the other. "
            "Neither discourse singles out women or men as the sole agent "
            "or the sole target."]),
        ("Touch, ranked strongest again", [
            "As in AN 8.17, the discourse's only evaluative move comes at "
            "the close: of the eight features, touch is named the surest "
            "catch, &ldquo;those beings who are caught by touch are well "
            "and truly caught&rdquo; &mdash; the identical closing line, "
            "unchanged by the reversal of subject and object."]),
    ],
    terms=[
        ("bandhati",
         "&ldquo;catches, binds&rdquo; &mdash; the same key verb as AN "
         "8.17, and the root of this discourse's own Pāli title, "
         "Dutiyabandhanasutta, &ldquo;the second discourse on binding.&rdquo;"),
        ("rodanena, hasanena, bhaṇitena",
         "&ldquo;with weeping, laughing, speaking&rdquo; &mdash; the "
         "identical first three features named in AN 8.17, unchanged here."),
        ("ākappena",
         "&ldquo;appearance&rdquo; &mdash; the fourth feature, physical "
         "presentation, identical in both discourses of this pair."),
        ("gandhena, rasena, phoṭṭhabbena",
         "&ldquo;with scents, tastes, and touches&rdquo; &mdash; the final "
         "three features, closing this list exactly as they closed AN "
         "8.17's."),
        ("phassabandhanā ye baddhā, susaṅkhātā tesaṁ bandhanā",
         "&ldquo;those beings who are caught by touch are well and truly "
         "caught&rdquo; &mdash; the identical closing ranking as AN 8.17, "
         "unchanged by the reversal of who catches whom."),
    ],
    text_intro=(
        "The discourse in full: the same eight features as AN 8.17, with a "
        "man catching a woman. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight features that catch"),
        ("p", "&sect;1", "an8.18:1.1-1.12"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 8.17's?",
         "opts": [
             "Entirely different content",
             "Identical in every feature and the closing line, except that "
             "the direction of catching is reversed — a man catches a woman "
             "rather than a woman catching a man",
             "This discourse has ten features instead of eight",
             "This discourse has no closing ranking"],
         "correct": 1,
         "expl": "A deliberate, exact mirror, not an independent variant."},
        {"q": "According to the guide, what claim does the pairing of AN "
              "8.17 and AN 8.18 make through its very structure?",
         "opts": [
             "That only women can catch men",
             "That attraction and capture by these eight means run in both "
             "directions equally, not as a fault attributed to one gender "
             "alone",
             "That only men can catch women",
             "That neither gender can be caught at all"],
         "correct": 1,
         "expl": "A symmetrical treatment, neither discourse singling out "
                 "one gender as sole agent or target."},
        {"q": "Which feature is again ranked as the surest catch?",
         "opts": [
             "Appearance", "Touch",
             "Weeping", "Gifts of wildflowers"],
         "correct": 1,
         "expl": "The identical closing line as AN 8.17, unchanged by the "
                 "reversal."},
        {"q": "What does this discourse's own Pāli title mean?",
         "opts": [
             "'The discourse on wisdom'",
             "'The second discourse on binding'",
             "'The discourse on the ocean'",
             "'The discourse on stains'"],
         "correct": 1,
         "expl": "Dutiyabandhanasutta, paired with AN 8.17's "
                 "Paṭhamabandhanasutta."},
        {"q": "How many of the eight features differ from AN 8.17's list?",
         "opts": [
             "All eight are different",
             "None — all eight are identical, word for word",
             "Four are different",
             "Only the first feature differs"],
         "correct": 1,
         "expl": "A complete, word-for-word match apart from the reversed "
                 "subject and object."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Vesālī",
             "No setting is stated in the source", "Yes, at Campā"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.17's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("The identical eight, reversed", [
            "weeping, laughing, speaking,",
            "appearance, flowers, scents,",
            "tastes, and touches — man to woman now",
        ]),
        ("Symmetry as the point", [
            "not one gender's fault —",
            "the pairing itself argues:",
            "both directions, equally",
        ]),
        ("Touch, ranked strongest again", [
            "the same closing line",
            "as AN 8.17's own —",
            "unchanged by the reversal",
        ]),
        ("Cross-references", [
            "AN 8.17 &middot; previous, the mirror image of this same list",
            "AN 8.19 &middot; next, a very different register: the ocean's "
            "eight wonders",
        ]),
    ],
    further=[
        '<a href="%s/an8.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.17.html">AN 8.17 &middot; Catching (1st)</a> &mdash; previous, the '
        "mirror image of this same list.",
        '<a href="an-8.19.html">AN 8.19 &middot; With Pahārāda</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.19 — Pahārādasutta
# --------------------------------------------------------------------------- #
page(
    19, "Pahārāda", "With Pahārāda",
    vagga=VAGGA_2,
    meta_title="AN 8.19 — With Pahārāda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Pahārādasutta, one of the tradition's most famous similes: eight "
        "incredible things the titans love about the ocean, matched point "
        "for point against eight incredible things mendicants love about "
        "the teaching and training. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Verañjā, at the root of the same neem tree named in AN "
                    "8.11, this time with the titan-lord Pahārāda as "
                    "interlocutor"),
        ("Speakers", "Pahārāda, lord of titans, and the Buddha"),
        ("Form", "A question-and-answer exchange, eight qualities of the "
                 "ocean matched point for point against eight qualities of "
                 "the Buddha's own teaching and training"),
        ("Length", "~5 minutes to read"),
        ("One of the tradition's best-known similes", "This ocean-and-"
                                                       "Dhamma comparison is "
                                                       "among the most widely "
                                                       "cited extended "
                                                       "similes in the "
                                                       "canon, recurring in "
                                                       "the Vinaya's own "
                                                       "account of the "
                                                       "uposatha and echoed "
                                                       "again at AN 8.20, "
                                                       "immediately following"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; eight "
                       "parallel points, each requiring its own comparison "
                       "to be held in mind"),
    ],
    why=(
        "Asked why the titans love the ocean, Pahārāda names eight "
        "incredible and amazing features &mdash; its gradual slope, its "
        "steady shoreline, its rejection of carcasses, how great rivers "
        "lose their names on entering it, its constant volume, its single "
        "taste of salt, its many treasures, and the great beings that live "
        "in it &mdash; and the Buddha matches each, point for point, against "
        "an equally incredible feature of his own teaching and training."),
    guide=[
        ("The teaching in one sentence", [
            "Just as the ocean has eight incredible and amazing qualities "
            "that make the titans love it, the Buddha's own teaching and "
            "training has eight parallel qualities &mdash; gradual "
            "training, unbreakable rules, expelling the corrupt, erasing "
            "caste distinctions, a single taste of freedom, spiritual "
            "treasures, and noble beings within it &mdash; that make the "
            "mendicants love it."]),
        ("The ocean's eight qualities", [
            "A gradual slope with no sudden precipice; a consistent "
            "shoreline that never overflows its bounds; refusing to "
            "accommodate a corpse, carrying it quickly to shore; great "
            "rivers losing their separate names and clans on entering it; "
            "never emptying or overfilling despite every stream and "
            "rainfall; a single uniform taste of salt; abundant treasures "
            "such as pearls and gems; and enormous life-forms living "
            "within it."]),
        ("Each quality, matched to the teaching", [
            "Gradual slope becomes gradual training toward awakening, not "
            "sudden penetration. An unbreaking shoreline becomes training "
            "rules disciples won't break even at the cost of their own "
            "life. Rejecting a corpse becomes the Saṅgha's swift expulsion "
            "of the corrupt. Rivers losing their names becomes people of "
            "all four classes losing their former caste on going forth, "
            "becoming simply &ldquo;ascetics who follow the Sakyan.&rdquo;"]),
        ("From constant volume to noble beings within", [
            "Never emptying or filling becomes the element of "
            "extinguishment neither shrinking nor swelling no matter how "
            "many attain it. A single taste of salt becomes a single taste "
            "of freedom. The ocean's treasures become the mindfulness "
            "meditations, right efforts, and other factors of awakening. "
            "And the ocean's great life-forms become the four pairs of "
            "noble persons, from stream-enterer to the perfected one, "
            "living within the teaching itself."]),
    ],
    terms=[
        ("acchariyo abbhuto dhammo",
         "&ldquo;incredible and amazing thing&rdquo; &mdash; the standing "
         "description applied to all eight qualities of both the ocean and "
         "the teaching."),
        ("anupubbasikkhā anupubbakiriyā anupubbapaṭipadā",
         "&ldquo;gradual training, progress, and practice&rdquo; &mdash; the "
         "teaching's own first parallel, matched against the ocean's "
         "gradual slope without abrupt precipice."),
        ("na kuṇapaṁ mahāsamuddo vasati",
         "&ldquo;the ocean doesn't accommodate a carcass&rdquo; &mdash; the "
         "third ocean quality, matched against the Saṅgha's swift expulsion "
         "of a corrupt individual, even one sitting in its very midst."),
        ("samuddo ... ekaraso loṇaraso",
         "&ldquo;the ocean has just one taste, the taste of salt&rdquo; "
         "&mdash; the sixth quality, matched against the teaching's own "
         "&ldquo;one taste, the taste of freedom&rdquo; (vimuttiraso)."),
        ("sotāpanno ca sotāpattiphalasacchikiriyāya paṭipanno",
         "the four pairs of noble persons &mdash; stream-enterer through the "
         "perfected one &mdash; matched against the ocean's own great "
         "life-forms, some hundreds of leagues long."),
    ],
    text_intro=(
        "The discourse in full: Pahārāda's eight qualities of the ocean, and "
        "the Buddha's eight parallel qualities of the teaching. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The question, and the ocean's eight qualities"),
        ("p", "&sect;1", "an8.19:1.1-9.4"),
        ("h3", "The teaching's eight parallel qualities"),
        ("p", "&sect;2", "an8.19:10.1-19.1"),
    ],
    quiz=[
        {"q": "What eight qualities does Pahārāda name as reasons the "
              "titans love the ocean?",
         "opts": [
             "Its color, temperature, depth, and four more physical traits",
             "Gradual slope, steady shoreline, rejecting carcasses, rivers "
             "losing their names, constant volume, one taste, treasures, "
             "and great beings",
             "Its size alone",
             "Eight named sea gods"],
         "correct": 1,
         "expl": "Eight incredible and amazing features, each matched to a "
                 "quality of the teaching."},
        {"q": "What does the ocean's refusal to accommodate a carcass match "
              "in the teaching?",
         "opts": [
             "Funeral rites for deceased mendicants",
             "The Saṅgha's swift expulsion of a corrupt individual, even one "
             "sitting in its very midst",
             "A prohibition against eating meat",
             "Cremation practices"],
         "correct": 1,
         "expl": "A quick, decisive removal, matched point for point to the "
                 "ocean's own behavior."},
        {"q": "What does rivers losing their names on entering the ocean "
              "match in the teaching?",
         "opts": [
             "Nothing; this quality has no parallel",
             "People of all four classes losing their former caste "
             "identities on going forth, becoming simply 'ascetics who "
             "follow the Sakyan'",
             "Rivers are mentioned only metaphorically with no application",
             "The renaming of monasteries"],
         "correct": 1,
         "expl": "A dissolution of caste distinction upon entering the "
                 "monastic life."},
        {"q": "What is the ocean's 'single taste,' and what does it match?",
         "opts": [
             "The taste of sweetness, matching the taste of generosity",
             "The taste of salt, matching the teaching's single taste of "
             "freedom",
             "The taste of bitterness, matching the taste of renunciation",
             "No taste is mentioned"],
         "correct": 1,
         "expl": "Ekaraso loṇaraso matched against vimuttiraso, one taste "
                 "of freedom."},
        {"q": "What do the ocean's great life-forms match in the teaching?",
         "opts": [
             "Nothing; this quality is purely descriptive",
             "The four pairs of noble persons, from the stream-enterer "
             "through the perfected one",
             "The Buddha's own physical appearance",
             "Wealthy lay donors"],
         "correct": 1,
         "expl": "Noble beings living within the teaching, paralleling "
                 "enormous beings living within the ocean."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Verañjā, at the same neem tree "
                                          "named in AN 8.11",
             "Rājagaha, on Vulture's Peak", "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "The same location as AN 8.11, this time with the "
                 "titan-lord Pahārāda."},
    ],
    marginalia=[
        ("Eight wonders of the ocean", [
            "gradual slope, steady shore,",
            "no carcass, rivers renamed,",
            "one taste, treasures, great beings",
        ]),
        ("Matched point for point", [
            "the ocean's own eight",
            "become eight of the teaching —",
            "gradual training, one taste of freedom",
        ]),
        ("Caste dissolved on entering", [
            "as rivers lose their names",
            "in the ocean's single body —",
            "so castes dissolve, going forth",
        ]),
        ("Cross-references", [
            "AN 8.18 &middot; previous, the mirror image of catching",
            "AN 8.20 &middot; next, this same eightfold ocean simile, "
            "reused in a very different setting",
        ]),
    ],
    further=[
        '<a href="%s/an8.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.18.html">AN 8.18 &middot; Catching (2nd)</a> &mdash; previous.',
        '<a href="an-8.20.html">AN 8.20 &middot; Sabbath</a> &mdash; next, closing this '
        "chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.20 — Uposathasutta — closes ch.2 Mahāvagga
# --------------------------------------------------------------------------- #
page(
    20, "Uposatha", "Sabbath",
    vagga=VAGGA_2,
    meta_title="AN 8.20 — Sabbath | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Uposathasutta, closing this chapter with the Buddha's refusal to "
        "recite the monastic code before an impure assembly, Mahāmoggallāna "
        "ejecting the offender by force, and the same eight ocean wonders "
        "met at AN 8.19 recalled by explicit cross-reference. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in the stilt longhouse of Migāra's mother in "
                    "the Eastern Monastery, on the sabbath night"),
        ("Speakers", "Venerable Ānanda, the Buddha, and Venerable "
                     "Mahāmoggallāna"),
        ("Form", "A narrative in three watches of the night, then the same "
                 "eight ocean qualities as AN 8.19, this time compressed by "
                 "an explicit textual cross-reference rather than restated "
                 "in full"),
        ("Length", "~4 minutes to read"),
        ("A named cross-reference, not a generic peyyāla", "Where this "
                                                            "project has met "
                                                            "many peyyāla "
                                                            "compressions "
                                                            "using ellipsis, "
                                                            "this discourse's "
                                                            "own source text "
                                                            "explicitly says "
                                                            "&ldquo;tell in "
                                                            "full as in the "
                                                            "previous "
                                                            "discourse&rdquo; "
                                                            "&mdash; a direct "
                                                            "citation of AN "
                                                            "8.19 by name, "
                                                            "not a generic "
                                                            "abbreviation "
                                                            "formula"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a vivid "
                       "narrative core, with a compressed doctrinal close "
                       "that rewards having just read AN 8.19"),
    ],
    why=(
        "Three times Ānanda asks the Buddha to recite the monastic code to "
        "the assembled monks on the sabbath night, and three times the "
        "Buddha stays silent, until he reveals the assembly is impure; "
        "Mahāmoggallāna scans the Saṅgha's minds, finds the offender, and "
        "physically ejects him when he refuses to leave, after which the "
        "Buddha declares he will never again recite the code himself, and "
        "recalls the same eight ocean wonders met at AN 8.19 by name."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha refuses three times to recite the monastic code "
            "while an unethical, corrupt individual sits undetected within "
            "the assembly; once Mahāmoggallāna physically ejects that "
            "person, the Buddha declares he will never personally recite "
            "the code again, since it's impossible for a Realized One to "
            "recite it in an impure assembly &mdash; itself an instance of "
            "the ocean's refusal to accommodate a corpse, the very quality "
            "named at AN 8.19."]),
        ("Three requests, three silences", [
            "In each of the night's three watches, Ānanda formally requests "
            "the recitation, describing the lateness of the hour with "
            "escalating detail. Each time the Buddha simply stays silent, "
            "building tension until, on the third request, he finally "
            "names the problem: the assembly itself is not pure."]),
        ("Mahāmoggallāna scans, confronts, and ejects", [
            "Rather than the Buddha naming the offender directly, "
            "Mahāmoggallāna uses his own power to encompass the minds of "
            "everyone present, locates the unethical individual sitting in "
            "the Saṅgha's very midst, and asks him to leave three times. "
            "When the man stays silent all three times, Mahāmoggallāna "
            "takes him by the arm and physically ejects him, bolting the "
            "door behind him."]),
        ("The ocean simile recalled by explicit citation", [
            "Having declared he will never again personally recite the "
            "code, the Buddha explains why by returning to the same eight "
            "wonders of the ocean and the teaching met at AN 8.19 &mdash; "
            "but this time the source text itself abbreviates by instructing "
            "the reciter to &ldquo;tell in full as in the previous "
            "discourse,&rdquo; a direct, named citation rather than a "
            "generic ellipsis, giving only the first and eighth items in "
            "full here."]),
    ],
    terms=[
        ("uposatho",
         "&ldquo;sabbath&rdquo; &mdash; this discourse's own title term, "
         "the observance day on which the monastic code is recited before "
         "the assembled Saṅgha."),
        ("na parisuddhā, ānanda, parisā",
         "&ldquo;Ānanda, the assembly is not pure&rdquo; &mdash; the "
         "Buddha's own terse revelation, breaking his third silence."),
        ("cetasā cetoparivitakkamaññāya",
         "&ldquo;encompassing the minds of everyone in the Saṅgha&rdquo; "
         "&mdash; Mahāmoggallāna's own method for locating the offender the "
         "Buddha had detected but not named."),
        ("bāhāyaṁ gahetvā bahi dvārakoṭṭhakā nikkhāmetvā "
         "sūcighaṭikaṁ daṁsetvā",
         "&ldquo;took that individual by the arm, ejected him out the gate, "
         "and bolted the door&rdquo; &mdash; Mahāmoggallāna's own decisive, "
         "physical resolution after three silent refusals to leave."),
        ("vitthārena purimasuttantasadisaṁ kātabbaṁ",
         "&ldquo;tell in full as in the previous discourse&rdquo; &mdash; "
         "the source text's own explicit cross-reference to AN 8.19, a "
         "named citation rather than a generic peyyāla ellipsis."),
    ],
    text_intro=(
        "The discourse in full: three requests and silences, "
        "Mahāmoggallāna's ejection of the offender, and the ocean simile "
        "recalled by citation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three requests, three silences"),
        ("p", "&sect;1", "an8.20:1.1-2.10"),
        ("h3", "Mahāmoggallāna finds and ejects the offender"),
        ("p", "&sect;2", "an8.20:3.1-5.6"),
        ("h3", "The Buddha's declaration, and the ocean simile recalled"),
        ("p", "&sect;3", "an8.20:6.1-9.11"),
    ],
    quiz=[
        {"q": "What happens each time Ānanda asks the Buddha to recite the "
              "monastic code, for the first two of three requests?",
         "opts": [
             "The Buddha immediately agrees",
             "The Buddha stays silent, without explanation",
             "The Buddha refuses angrily",
             "The Buddha asks Ānanda to recite it instead"],
         "correct": 1,
         "expl": "Silence, building tension until the third request finally "
                 "gets an answer."},
        {"q": "How does Mahāmoggallāna locate the offender the Buddha had "
              "detected but not named?",
         "opts": [
             "By asking each monk individually",
             "By encompassing the minds of everyone in the Saṅgha with his "
             "own power",
             "By waiting for the offender to confess",
             "By consulting the monastic register"],
         "correct": 1,
         "expl": "A direct use of Mahāmoggallāna's own mind-reading ability."},
        {"q": "What does the Buddha declare after the offender is ejected?",
         "opts": [
             "That the sabbath observance should be abolished",
             "That he will never again personally recite the monastic "
             "code, since a Realized One cannot recite it in an impure "
             "assembly",
             "That Mahāmoggallāna should be punished for using force",
             "That the offender should be readmitted"],
         "correct": 1,
         "expl": "A lasting policy change, framed as an instance of the "
                 "ocean's own refusal to accommodate a corpse."},
        {"q": "How does this discourse's source text handle the eight ocean "
              "qualities, compared to a generic peyyāla ellipsis?",
         "opts": [
             "By restating all eight in full a second time",
             "By explicitly instructing the reciter to 'tell in full as in "
             "the previous discourse' — a direct, named citation of AN 8.19",
             "By omitting the ocean simile entirely",
             "By replacing it with an unrelated teaching"],
         "correct": 1,
         "expl": "A named cross-reference, distinct from this project's more "
                 "common generic abbreviation formulas."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Verañjā, at the neem tree",
             "Sāvatthī, in the stilt longhouse of Migāra's mother in the "
             "Eastern Monastery",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A specific setting on the sabbath night, distinct from AN "
                 "8.19's own location."},
        {"q": "How many times does Mahāmoggallāna ask the offender to leave "
              "before physically ejecting him?",
         "opts": [
             "Once", "Three times, met each time with silence",
             "Five times", "He never asks; he ejects him immediately"],
         "correct": 1,
         "expl": "Three silent refusals, echoing the discourse's own "
                 "pattern of threes."},
    ],
    marginalia=[
        ("Three requests, three silences", [
            "each watch of the night,",
            "Ānanda asks — silence,",
            "until: 'the assembly is not pure'",
        ]),
        ("Mahāmoggallāna acts decisively", [
            "scans every mind present,",
            "asks three times, then ejects —",
            "by the arm, out the gate, bolted",
        ]),
        ("Closing this chapter, by citation", [
            "the ocean's eight wonders",
            "recalled, not restated —",
            "'tell in full as before'",
        ]),
        ("Cross-references", [
            "AN 8.19 &middot; previous, and cited here by name",
            "AN 8.11 &middot; earlier, opening this chapter at the same "
            "neem tree Pahārāda's discourse named",
        ]),
    ],
    further=[
        '<a href="%s/an8.20/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.19.html">AN 8.19 &middot; With Pahārāda</a> &mdash; previous, and cited '
        "here by name.",
        '<a href="an-8.11.html">AN 8.11 &middot; At Verañjā</a> &mdash; earlier, opening this '
        "same chapter.",
    ],
)
