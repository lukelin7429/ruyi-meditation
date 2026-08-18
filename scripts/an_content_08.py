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
