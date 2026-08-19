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


VAGGA_3 = "<em>Gahapativagga</em> &mdash; the third chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.21 — Uggasutta (Vesālī) — opens ch.3 Gahapativagga
# --------------------------------------------------------------------------- #
page(
    21, "Ugga", "With Ugga of Vesālī",
    vagga=VAGGA_3,
    meta_title="AN 8.21 — With Ugga of Vesālī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Uggasutta, opening a new chapter of lay-follower portraits: the "
        "householder Ugga of Vesālī describes, in his own words, the eight "
        "amazing qualities the Buddha praised him for. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with the peaked "
                    "roof"),
        ("Speakers", "The Buddha, an unnamed mendicant, and the householder "
                     "Ugga of Vesālī, relayed through a messenger structure"),
        ("Form", "The Buddha names a praise without explaining it, a "
                 "mendicant investigates, and the householder himself "
                 "supplies and numbers his own eight qualities in first "
                 "person"),
        ("Length", "~4 minutes to read"),
        ("A new chapter, a new register", "This opens Gahapativagga, the "
                                          "Chapter on Householders, "
                                          "beginning a run of discourses "
                                          "praising named lay disciples "
                                          "rather than teaching doctrine "
                                          "directly to mendicants"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "relay narrative with a first-person list embedded "
                       "inside it"),
    ],
    why=(
        "The Buddha tells the mendicants that the householder Ugga of "
        "Vesālī has eight amazing qualities, without saying what they are, "
        "then leaves; a mendicant goes to ask Ugga directly, and Ugga "
        "&mdash; not knowing what the Buddha meant either &mdash; supplies "
        "his own list: being inspired at first sight of the Buddha, "
        "stream-entry, giving away a beloved wife without regret, "
        "unreserved generosity, careful reverence, attentive listening, "
        "composure around visiting deities, and having already given up "
        "the five lower fetters."),
    guide=[
        ("The teaching in one sentence", [
            "Ugga of Vesālī's eight amazing qualities &mdash; inspired at "
            "first sight, converted through the graduated teaching, giving "
            "away a beloved wife without regret, unreserved generosity, "
            "careful homage and listening, composure before visiting "
            "deities, and freedom from the five lower fetters &mdash; turn "
            "out to be exactly what Ugga himself lists, unprompted, when "
            "asked what the Buddha might have meant."]),
        ("A relay, not a direct teaching", [
            "The Buddha names Ugga's praiseworthy qualities but withholds "
            "their content and immediately withdraws. It falls to an "
            "unnamed mendicant, and then to Ugga himself, to fill in what "
            "the Buddha left unsaid &mdash; a structure this chapter will "
            "repeat with other named householders."]),
        ("Freedom that doesn't announce itself", [
            "The eighth and final quality Ugga names is striking for its "
            "confidence: of the five lower fetters, he says, he doesn't see "
            "any that he hasn't given up &mdash; a direct claim to the "
            "attainment of non-return, stated plainly by a layperson still "
            "living a full householder's life."]),
        ("Composure before both people and deities", [
            "Two of Ugga's eight qualities describe emotional evenness under "
            "circumstances that might unsettle most people: giving away a "
            "cherished young wife without any recorded upset, and receiving "
            "visits from deities who confirm the Buddha's teaching without "
            "being swept up in the excitement of the visit itself."]),
    ],
    terms=[
        ("acchariyabbhutadhammā",
         "&ldquo;amazing and incredible qualities&rdquo; &mdash; the "
         "standing phrase applied to Ugga and to every householder praised "
         "in this new chapter."),
        ("virajaṁ vītamalaṁ dhammacakkhuṁ udapādi",
         "&ldquo;the stainless, immaculate vision of the Dhamma arose&rdquo; "
         "&mdash; Ugga's own moment of stream-entry, following the same "
         "graduated teaching met at AN 8.12 for General Sīha."),
        ("pañcasu orambhāgiyesu saṁyojanesu",
         "&ldquo;of the five lower fetters&rdquo; &mdash; the set Ugga "
         "claims to have entirely given up, the mark of a non-returner."),
        ("kalyāṇakāmo",
         "part of Ugga's own generosity, shared &ldquo;without "
         "reserve&rdquo; with people of good, ethical character &mdash; "
         "generosity aimed specifically, not indiscriminately."),
        ("sādhu sādhu, bhikkhu",
         "&ldquo;good, good, mendicant!&rdquo; &mdash; the Buddha's own "
         "confirmation, closing the discourse by verifying that Ugga's self-"
         "report matches exactly what he had in mind."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's unexplained praise, and Ugga's "
        "own account of his eight qualities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha's unexplained praise"),
        ("p", "&sect;1", "an8.21:1.1-2.2"),
        ("h3", "Ugga names his own eight qualities"),
        ("p", "&sect;2", "an8.21:3.1-10.2"),
        ("h3", "The Buddha confirms Ugga's own account"),
        ("p", "&sect;3", "an8.21:11.1-13.3"),
    ],
    quiz=[
        {"q": "How does this discourse's structure work?",
         "opts": [
             "The Buddha teaches the eight qualities directly to the "
             "mendicants",
             "The Buddha names a praise without explaining it, and Ugga "
             "himself supplies and numbers his own eight qualities when "
             "asked",
             "Ugga refuses to discuss his own qualities",
             "The mendicant invents the list himself"],
         "correct": 1,
         "expl": "A relay structure, with the householder's own first-person "
                 "account filling in what the Buddha left unsaid."},
        {"q": "What does Ugga claim about the five lower fetters?",
         "opts": [
             "That he has never heard of them",
             "That he doesn't see any that he hasn't given up",
             "That he plans to give them up eventually",
             "That only monastics can give them up"],
         "correct": 1,
         "expl": "A direct claim to non-return, stated by a layperson still "
                 "living a householder's life."},
        {"q": "What does Ugga do when his eldest wife asks to be given to "
              "another man?",
         "opts": [
             "He refuses her request",
             "He arranges it himself, and doesn't recall getting upset "
             "while doing so",
             "He becomes angry and disowns her",
             "He asks the Buddha to intervene"],
         "correct": 1,
         "expl": "One of the eight qualities: emotional evenness under "
                 "circumstances that might unsettle most people."},
        {"q": "What confirms that Ugga's own list matches what the Buddha "
              "had in mind?",
         "opts": [
             "Nothing; the discourse leaves it unresolved",
             "The Buddha's closing statement, verifying the mendicant's "
             "report matches exactly",
             "A vote among the mendicants",
             "Ugga's own guess, later proven wrong"],
         "correct": 1,
         "expl": "'Good, good, mendicant!' — direct confirmation closing the "
                 "discourse."},
        {"q": "What chapter does this discourse open, and what does it "
              "shift toward?",
         "opts": [
             "Devatāvagga, shifting toward deity visits",
             "Gahapativagga, the Chapter on Householders, shifting toward "
             "portraits of named lay disciples",
             "Rāgapeyyāla, shifting toward abbreviated formulas",
             "No chapter shift occurs"],
         "correct": 1,
         "expl": "A new register: praising named lay disciples rather than "
                 "teaching doctrine directly to mendicants."},
        {"q": "How does Ugga describe his own generosity?",
         "opts": [
             "Given only to his immediate family",
             "Shared without reserve with ethical people of good character",
             "Given only once a year",
             "Kept entirely private"],
         "correct": 1,
         "expl": "The fourth of his eight self-described qualities."},
    ],
    marginalia=[
        ("Eight qualities, self-reported", [
            "inspired at first sight,",
            "stream-entry, a wife given",
            "without regret, generosity",
        ]),
        ("A relay, not a direct teaching", [
            "the Buddha names, withholds —",
            "a mendicant asks, and Ugga",
            "supplies his own account",
        ]),
        ("Freedom, plainly claimed", [
            "no lower fetter remains —",
            "a householder's direct claim",
            "to the fruit of non-return",
        ]),
        ("Cross-references", [
            "AN 8.20 &middot; earlier, closing the previous chapter",
            "AN 8.22 &middot; next, the same relay structure for a "
            "different householder",
        ]),
    ],
    further=[
        '<a href="%s/an8.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.20.html">AN 8.20 &middot; Sabbath</a> &mdash; earlier, closing the '
        "previous chapter.",
        '<a href="an-8.22.html">AN 8.22 &middot; With Uggata of Elephant Village</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.22 — Uggasutta (Hatthigāma)
# --------------------------------------------------------------------------- #
page(
    22, "Uggata", "With Uggata of Elephant Village",
    vagga=VAGGA_3,
    meta_title="AN 8.22 — With Uggata of Elephant Village | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "second Ugga-pattern discourse, in which the householder Uggata of "
        "Elephant Village lists his own eight amazing qualities, sharing "
        "most items with AN 8.21 but diverging in tone and confidence "
        "toward the close. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Elephant Village, in the land of the Vajjis"),
        ("Speakers", "The Buddha, an unnamed mendicant, and the householder "
                     "Uggata of Elephant Village"),
        ("Form", "The identical relay structure as AN 8.21, with five nearly "
                 "identical opening qualities and three that diverge"),
        ("Length", "~4 minutes to read"),
        ("A paired discourse, not a repeat", "This shares its narrative "
                                             "frame and five of its eight "
                                             "qualities word for word with "
                                             "AN 8.21, but items six through "
                                             "eight genuinely differ, and "
                                             "Uggata's own opening detail "
                                             "&mdash; sobering up mid-party "
                                             "at first sight of the Buddha "
                                             "&mdash; is unique to him"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; best read "
                       "alongside AN 8.21 to see exactly where the two "
                       "portraits diverge"),
    ],
    why=(
        "Following the same relay structure as AN 8.21, the householder "
        "Uggata of Elephant Village lists his own eight amazing qualities "
        "&mdash; sobering up at first sight of the Buddha mid-celebration, "
        "stream-entry, giving away a wife without regret, unreserved "
        "generosity, careful reverence and reciprocal teaching, impartial "
        "giving to the Saṅgha regardless of individual monks' reported "
        "attainments, composure before deities, and a modest, conditional "
        "claim about his own likely destination after death."),
    guide=[
        ("The teaching in one sentence", [
            "Uggata of Elephant Village's eight qualities largely match "
            "Ugga of Vesālī's from AN 8.21, but diverge from item six "
            "onward: impartial generosity toward mendicants regardless of "
            "their reported spiritual rank, and a hedged, conditional claim "
            "about non-return rather than Ugga's flat assertion."]),
        ("A vivid, unique opening detail", [
            "Unlike Ugga's plain first sight of the Buddha, Uggata's own "
            "account adds a specific circumstance: he was partying in the "
            "Dragon's Park when he first saw the Buddha at a distance, and "
            "sobered up on the spot &mdash; a detail found nowhere in AN "
            "8.21, individualizing this otherwise closely parallel "
            "portrait."]),
        ("Impartial giving, a genuinely new sixth quality", [
            "Where Ugga's sixth quality was about listening carefully and "
            "teaching back if untaught, Uggata's sixth is about something "
            "AN 8.21 doesn't mention at all: even when deities tell him "
            "which visiting mendicants have attained which specific "
            "spiritual ranks, he doesn't let that knowledge skew his "
            "giving, offering to the Saṅgha impartially rather than "
            "favoring the more advanced."]),
        ("A hedged claim, not a flat one", [
            "Where Ugga states outright that he has given up all five lower "
            "fetters, Uggata's eighth quality is phrased far more "
            "cautiously: if he dies before the Buddha, it would be &ldquo;no "
            "wonder&rdquo; if the Buddha declared him free of any fetter "
            "binding him to this world &mdash; a conditional, deferential "
            "way of pointing at the same attainment Ugga claims directly."]),
    ],
    terms=[
        ("nāgavanuyyāne kīḷamāno",
         "&ldquo;partying in the Dragon's Park&rdquo; &mdash; Uggata's own "
         "circumstance at first sight of the Buddha, unique to this "
         "discourse among the Ugga-pattern pair."),
        ("ubhatobhāgavimutto",
         "&ldquo;freed both ways&rdquo; &mdash; one of several technical "
         "terms deities are said to report about individual visiting "
         "mendicants, the discrimination Uggata's sixth quality resists "
         "acting on."),
        ("samacittataṁ",
         "&ldquo;impartially&rdquo; &mdash; the manner of Uggata's own "
         "giving to the Saṅgha, regardless of what deities report about "
         "individual recipients' attainments."),
        ("na me ambhāgiyaṁ saṁyojanaṁ siyā",
         "&ldquo;bound by no fetter that might return him to this "
         "world&rdquo; &mdash; the Buddha's hypothetical declaration Uggata "
         "invokes conditionally, rather than claiming the attainment "
         "outright as Ugga does."),
        ("acchariyabbhutadhammā",
         "&ldquo;amazing and incredible qualities&rdquo; &mdash; the same "
         "standing phrase applied throughout this chapter's householder "
         "portraits."),
    ],
    text_intro=(
        "The discourse in full: Uggata's own account of his eight "
        "qualities, diverging from Ugga's from item six onward. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha's unexplained praise"),
        ("p", "&sect;1", "an8.22:1.1-2.2"),
        ("h3", "Uggata names his own eight qualities"),
        ("p", "&sect;2", "an8.22:3.1-10.3"),
        ("h3", "The Buddha confirms Uggata's own account"),
        ("p", "&sect;3", "an8.22:11.1-13.3"),
    ],
    quiz=[
        {"q": "What unique detail opens Uggata's own account of his first "
              "quality, not found in Ugga's version at AN 8.21?",
         "opts": [
             "He was meditating alone in a forest",
             "He was partying in the Dragon's Park and sobered up at first "
             "sight of the Buddha",
             "He was traveling on business",
             "He was asleep and dreamed of the Buddha"],
         "correct": 1,
         "expl": "A vivid, individualizing detail unique to this discourse."},
        {"q": "How does Uggata's sixth quality differ from Ugga's?",
         "opts": [
             "They are identical",
             "Uggata's is about giving impartially to mendicants regardless "
             "of their reported spiritual rank, a quality Ugga's account "
             "doesn't include",
             "Uggata has no sixth quality at all",
             "Uggata's sixth quality is about physical strength"],
         "correct": 1,
         "expl": "A genuinely new element, not present in AN 8.21's "
                 "parallel list."},
        {"q": "How does Uggata's eighth quality differ from Ugga's flat "
              "claim to have given up all five lower fetters?",
         "opts": [
             "Uggata makes the identical flat claim",
             "Uggata phrases it conditionally — 'no wonder' if the Buddha "
             "declared him free of any binding fetter after his death",
             "Uggata denies having attained anything",
             "Uggata claims a higher attainment than Ugga"],
         "correct": 1,
         "expl": "A hedged, deferential claim rather than a direct "
                 "assertion."},
        {"q": "How many of the eight qualities are shared nearly word for "
              "word between this discourse and AN 8.21?",
         "opts": [
             "None", "About five, before the two accounts diverge",
             "All eight, with no differences", "Only one"],
         "correct": 1,
         "expl": "A paired discourse, not a repeat — shared frame, "
                 "diverging content from item six onward."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Vesālī, at the Great Wood", "Elephant Village, in the land of "
                                          "the Vajjis",
             "Sāvatthī, in Jeta's Grove", "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "A different location from AN 8.21's Vesālī setting."},
        {"q": "What confirms Uggata's own account matches what the Buddha "
              "had in mind?",
         "opts": [
             "Nothing; the discourse leaves it unresolved",
             "The Buddha's closing statement, the same confirmation pattern "
             "as AN 8.21",
             "A public vote", "Uggata's own uncertainty, never resolved"],
         "correct": 1,
         "expl": "The identical confirmation structure as the previous "
                 "discourse."},
    ],
    marginalia=[
        ("A party, then sobered", [
            "in the Dragon's Park, at first sight —",
            "unique among the Ugga pair,",
            "individualizing this portrait",
        ]),
        ("Impartial giving, added", [
            "regardless of deities' reports",
            "on visiting monks' attainments —",
            "a quality Ugga's list lacks",
        ]),
        ("A hedged claim, not a flat one", [
            "'no wonder,' Uggata says —",
            "conditional, deferential,",
            "unlike Ugga's direct assertion",
        ]),
        ("Cross-references", [
            "AN 8.21 &middot; previous, the same relay structure for a "
            "different householder",
            "AN 8.23 &middot; next, a third householder — this time judged "
            "by what he doesn't want known",
        ]),
    ],
    further=[
        '<a href="%s/an8.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.21.html">AN 8.21 &middot; With Ugga of Vesālī</a> &mdash; previous.',
        '<a href="an-8.23.html">AN 8.23 &middot; With Hatthaka (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.23 — Paṭhamahatthakasutta
# --------------------------------------------------------------------------- #
page(
    23, "Paṭhamahatthaka", "With Hatthaka (1st)",
    vagga=VAGGA_3,
    meta_title="AN 8.23 — With Hatthaka (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamahatthakasutta, in which the Buddha names seven qualities of "
        "the householder Hatthaka of Āḷavī, and Hatthaka's own reluctance "
        "to have them confirmed publicly becomes the eighth quality itself. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Āḷavī, at Āḷavī's premier shrine"),
        ("Speakers", "The Buddha, an unnamed mendicant, and the householder "
                     "Hatthaka of Āḷavī"),
        ("Form", "Seven qualities named directly by the Buddha, confirmed "
                 "word for word by a visiting mendicant, and an eighth "
                 "quality that emerges only from Hatthaka's own reluctance"),
        ("Length", "~2 minutes to read"),
        ("The eighth quality is the withholding itself", "Unlike AN 8.21 "
                                                          "and 8.22, where "
                                                          "the householder "
                                                          "supplies his own "
                                                          "full list, here "
                                                          "the Buddha names "
                                                          "only seven "
                                                          "qualities outright "
                                                          "&mdash; the eighth "
                                                          "is revealed only "
                                                          "because Hatthaka "
                                                          "doesn't want it "
                                                          "known"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, "
                       "with an elegant structural twist in its closing "
                       "lines"),
    ],
    why=(
        "The Buddha names seven qualities of the householder Hatthaka of "
        "Āḷavī &mdash; faithful, ethical, conscientious, prudent, learned, "
        "generous, and wise &mdash; and when a mendicant confirms the list "
        "with Hatthaka directly, Hatthaka's first concern is only whether "
        "any lay people were present to overhear it; the Buddha then names "
        "this very reluctance itself as the eighth quality, fewness of "
        "wishes."),
    guide=[
        ("The teaching in one sentence", [
            "Hatthaka of Āḷavī has seven named qualities &mdash; faith, "
            "ethics, conscience, prudence, learning, generosity, and wisdom "
            "&mdash; and an eighth that isn't named directly at all: his "
            "own reluctance to have his good qualities made known to "
            "others, which the Buddha identifies as fewness of wishes, the "
            "eighth quality itself."]),
        ("Seven qualities, stated and confirmed", [
            "Unlike the Ugga-pattern discourses just before it, this one "
            "opens with the Buddha naming all seven qualities directly and "
            "in full, which the visiting mendicant then repeats back to "
            "Hatthaka word for word, and Hatthaka confirms without "
            "elaboration."]),
        ("A question that reveals the eighth quality", [
            "Hatthaka's only response to hearing his own seven qualities "
            "confirmed is to ask whether any lay people were present when "
            "the Buddha named them &mdash; relieved to learn none were. "
            "This single question, not any positive statement, is what "
            "reveals the quality the Buddha completes the list with."]),
        ("Fewness of wishes, demonstrated rather than described", [
            "Rather than defining appicchatā, fewness of wishes, "
            "abstractly, this discourse lets Hatthaka demonstrate it "
            "directly: he doesn't want his own good qualities publicized, "
            "and that very not-wanting is what earns him the eighth and "
            "final place on a list the Buddha had originally left "
            "incomplete."]),
    ],
    terms=[
        ("saddho, sīlavā, hirimā, ottappī, bahussuto, cāgavā, paññavā",
         "&ldquo;faithful, ethical, conscientious, prudent, learned, "
         "generous, and wise&rdquo; &mdash; the seven qualities the Buddha "
         "names outright, stated once and confirmed once without variation."),
        ("api nu kho, bhante, na koci odātavasano upāsako sammukhā ahosī",
         "&ldquo;I trust that no white-clothed lay people were present?"
         "&rdquo; &mdash; Hatthaka's own question, the moment that reveals "
         "his reluctance rather than any positive statement."),
        ("appicchova samāno na icchati attano guṇaṁ paresaṁ vidito",
         "&ldquo;that gentleman has few wishes; he doesn't want his own "
         "good qualities to be made known to others&rdquo; &mdash; the "
         "Buddha's own explanation of the eighth quality, drawn directly "
         "from Hatthaka's question."),
        ("appicchatā",
         "&ldquo;fewness of wishes&rdquo; &mdash; the eighth and final "
         "quality named, demonstrated through Hatthaka's own reluctance "
         "rather than defined abstractly."),
        ("acchariyabbhutadhammā",
         "&ldquo;amazing and incredible qualities&rdquo; &mdash; the "
         "standing phrase this chapter applies to each of its named "
         "householders."),
    ],
    text_intro=(
        "The discourse in full: seven named qualities, and an eighth "
        "revealed through Hatthaka's own reluctance. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Seven qualities, named by the Buddha"),
        ("p", "&sect;1", "an8.23:1.1-1.14"),
        ("h3", "A mendicant confirms the list with Hatthaka"),
        ("p", "&sect;2", "an8.23:2.1-4.2"),
        ("h3", "The eighth quality, revealed"),
        ("p", "&sect;3", "an8.23:7.1-7.4"),
    ],
    quiz=[
        {"q": "How does this discourse's structure differ from AN 8.21 and "
              "8.22?",
         "opts": [
             "It is structurally identical to both",
             "The Buddha names the qualities directly here, rather than "
             "leaving the householder to supply his own full list",
             "Hatthaka refuses to participate at all",
             "There is no mendicant intermediary"],
         "correct": 1,
         "expl": "Seven stated directly and confirmed, unlike the earlier "
                 "relay-and-self-report structure."},
        {"q": "What is Hatthaka's only response upon hearing his seven "
              "qualities confirmed?",
         "opts": [
             "He immediately lists an eighth quality himself",
             "He asks whether any lay people were present to overhear it",
             "He denies having any of the seven qualities",
             "He asks for a ninth quality to be added"],
         "correct": 1,
         "expl": "A single question, not a positive statement, that reveals "
                 "the eighth quality."},
        {"q": "What does the Buddha name as Hatthaka's eighth quality?",
         "opts": [
             "Physical strength", "Fewness of wishes — not wanting his own "
                                   "good qualities made known to others",
             "Wealth", "Skill in debate"],
         "correct": 1,
         "expl": "Demonstrated through Hatthaka's own reluctance, not stated "
                 "as an abstract virtue."},
        {"q": "What are the seven qualities the Buddha names directly?",
         "opts": [
             "The five precepts plus two more",
             "Faithful, ethical, conscientious, prudent, learned, generous, "
             "and wise",
             "The seven factors of awakening",
             "Physical beauty, wealth, and social standing"],
         "correct": 1,
         "expl": "Stated once by the Buddha, then confirmed word for word by "
                 "the visiting mendicant."},
        {"q": "According to the guide, how does this discourse demonstrate "
              "fewness of wishes rather than merely define it?",
         "opts": [
             "By giving a long abstract explanation",
             "By letting Hatthaka's own not-wanting-to-be-known stand as "
             "the demonstration itself",
             "By contrasting it with wealth",
             "It doesn't demonstrate it at all"],
         "correct": 1,
         "expl": "The reluctance itself, not a description of it, earns "
                 "Hatthaka the eighth quality."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Vesālī, at the Great Wood", "Āḷavī, at Āḷavī's premier shrine",
             "Sāvatthī, in Jeta's Grove", "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "The same location this discourse shares with AN 8.24, "
                 "immediately following."},
    ],
    marginalia=[
        ("Seven, named directly", [
            "faithful, ethical, conscientious,",
            "prudent, learned, generous,",
            "and wise — stated, then confirmed",
        ]),
        ("A question reveals the eighth", [
            "'were any lay people there?' —",
            "not a claim, but a worry —",
            "that worry becomes the answer",
        ]),
        ("Fewness of wishes, demonstrated", [
            "not defined, but shown:",
            "not wanting one's own virtue known",
            "is the very virtue itself",
        ]),
        ("Cross-references", [
            "AN 8.22 &middot; previous, the second Ugga-pattern householder",
            "AN 8.24 &middot; next, the same Hatthaka, now with all eight "
            "qualities named together",
        ]),
    ],
    further=[
        '<a href="%s/an8.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.22.html">AN 8.22 &middot; With Uggata of Elephant Village</a> &mdash; '
        "previous.",
        '<a href="an-8.24.html">AN 8.24 &middot; With Hatthaka (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.24 — Dutiyahatthakasutta
# --------------------------------------------------------------------------- #
page(
    24, "Dutiyahatthaka", "With Hatthaka (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 8.24 — With Hatthaka (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyahatthakasutta, in which Hatthaka explains how the four ways "
        "of being inclusive let him gather a congregation of five hundred, "
        "and the Buddha then names his full eight qualities together for "
        "the first time, folding in the fewness of wishes met at AN 8.23. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Āḷavī, at Āḷavī's premier shrine, the same location as "
                    "AN 8.23"),
        ("Speakers", "Hatthaka of Āḷavī, escorted by around five hundred lay "
                     "followers, and the Buddha"),
        ("Form", "A question about leadership answered with a fourfold "
                 "teaching, followed by the Buddha's own summary naming "
                 "Hatthaka's full eight qualities in a single list"),
        ("Length", "~2 minutes to read"),
        ("The eighth quality, now stated outright", "AN 8.23 revealed "
                                                     "fewness of wishes only "
                                                     "obliquely, through "
                                                     "Hatthaka's own "
                                                     "reluctance; this "
                                                     "discourse folds it "
                                                     "directly into a "
                                                     "single eight-item list, "
                                                     "confirming what the "
                                                     "earlier discourse only "
                                                     "implied"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "with a practical teaching on leadership followed by "
                       "a summary list"),
    ],
    why=(
        "Arriving with roughly five hundred lay followers, Hatthaka "
        "explains to the Buddha that he gathers such a large congregation "
        "using the four ways of being inclusive &mdash; giving, kindly "
        "words, taking care of people, and treating them equally &mdash; "
        "though he adds candidly that his own family's wealth helps too; "
        "after Hatthaka leaves, the Buddha names his full eight qualities "
        "together, this time explicitly including fewness of wishes as the "
        "eighth."),
    guide=[
        ("The teaching in one sentence", [
            "Hatthaka gathers his large congregation through the four ways "
            "of being inclusive &mdash; giving, kindly speech, caring for "
            "people, and treating them equally &mdash; a method the Buddha "
            "confirms as universal across past, present, and future; "
            "afterward, the Buddha names Hatthaka's full eight qualities "
            "together, now explicitly including fewness of wishes."]),
        ("The four ways of being inclusive, applied practically", [
            "Asked directly how he brings together such a large following, "
            "Hatthaka doesn't describe an abstract virtue but a practical "
            "method: reading what each person responds to &mdash; a gift, "
            "kind words, being cared for, or equal treatment &mdash; and "
            "giving each what draws them in."]),
        ("An honest caveat about wealth", [
            "Hatthaka doesn't let his answer stand as purely idealistic. He "
            "adds, unprompted, that his family's wealth also plays a role: "
            "people wouldn't give a poor person the same hearing they give "
            "him &mdash; a candid acknowledgment the Buddha doesn't correct "
            "or soften."]),
        ("Eight qualities, finally listed as one", [
            "Where AN 8.23 revealed the eighth quality only through "
            "Hatthaka's own reluctance to be praised, this discourse closes "
            "by having the Buddha state all eight together in a single "
            "list &mdash; faithful, ethical, conscientious, prudent, "
            "learned, generous, wise, and having few wishes &mdash; "
            "confirming directly what the earlier discourse only implied."]),
    ],
    terms=[
        ("cattārime saṅgahavatthū",
         "&ldquo;the four ways of being inclusive&rdquo; &mdash; dāna "
         "(giving), peyyavajja (kindly words), atthacariyā (taking care of "
         "people), and samānattatā (treating people equally), the method "
         "Hatthaka credits for his large congregation."),
        ("dānena saṅgaṇhāmi",
         "&ldquo;I include them by giving a gift&rdquo; &mdash; the first "
         "of the four ways, matched to whichever people respond to "
         "material generosity."),
        ("aḍḍhā kho pana me, bhante, kulāni",
         "&ldquo;my family is wealthy&rdquo; &mdash; Hatthaka's own candid "
         "addition, acknowledging a factor beyond the four ways of being "
         "inclusive."),
        ("yepi te, bhikkhave, ahesuṁ atītamaddhānaṁ mahantaṁ parisaṁ "
         "saṅgaṇhiṁsu",
         "&ldquo;whether in the past, future, or present, all those who "
         "have brought together a large congregation&rdquo; &mdash; the "
         "Buddha's own confirmation that Hatthaka's method is universal, "
         "not particular to him."),
        ("appicchatā",
         "&ldquo;fewness of wishes&rdquo; &mdash; the eighth quality, here "
         "stated directly as part of a single eight-item list, confirming "
         "what AN 8.23 only demonstrated obliquely."),
    ],
    text_intro=(
        "The discourse in full: the four ways of being inclusive, and "
        "Hatthaka's full eight qualities named together. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "How Hatthaka gathers a large congregation"),
        ("p", "&sect;1", "an8.24:1.1-1.18"),
        ("h3", "The Buddha names Hatthaka's full eight qualities"),
        ("p", "&sect;2", "an8.24:2.1-2.13"),
    ],
    quiz=[
        {"q": "What method does Hatthaka credit for gathering roughly five "
              "hundred lay followers?",
         "opts": [
             "Wealth alone",
             "The four ways of being inclusive — giving, kindly words, "
             "taking care of people, and treating them equally",
             "Strict discipline and punishment",
             "Public debate and argument"],
         "correct": 1,
         "expl": "A practical method matched to what draws each person in."},
        {"q": "What candid addition does Hatthaka make to his own answer?",
         "opts": [
             "That he actually dislikes leading a congregation",
             "That his family's wealth also plays a role, since people "
             "wouldn't give a poor person the same hearing",
             "That the method never actually works",
             "That he learned it from a rival teacher"],
         "correct": 1,
         "expl": "An honest caveat the Buddha doesn't correct or soften."},
        {"q": "How does the Buddha respond to Hatthaka's explanation of the "
              "four ways of being inclusive?",
         "opts": [
             "He rejects it as insufficient",
             "He confirms it as universal — used by all who have gathered "
             "large congregations across past, present, and future",
             "He says only wealthy people can use this method",
             "He changes the subject entirely"],
         "correct": 1,
         "expl": "A general confirmation, not limited to Hatthaka's own "
                 "case."},
        {"q": "How does this discourse's closing list of eight qualities "
              "relate to AN 8.23?",
         "opts": [
             "It contradicts AN 8.23 entirely",
             "It states all eight together directly, including fewness of "
             "wishes, confirming what AN 8.23 only revealed obliquely",
             "It omits fewness of wishes entirely",
             "It has no relation to AN 8.23"],
         "correct": 1,
         "expl": "A direct statement of what the earlier discourse "
                 "demonstrated through Hatthaka's own reluctance."},
        {"q": "What are the four ways of being inclusive?",
         "opts": [
             "Generosity, ethics, patience, and wisdom",
             "Giving, kindly words, taking care of people, and treating "
             "them equally",
             "Faith, effort, mindfulness, and immersion",
             "The four noble truths"],
         "correct": 1,
         "expl": "Dāna, peyyavajja, atthacariyā, and samānattatā, named "
                 "directly by Hatthaka."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Vesālī, at the Great Wood", "Āḷavī, at Āḷavī's premier "
                                          "shrine, the same location as AN "
                                          "8.23",
             "Sāvatthī, in Jeta's Grove", "Elephant Village"],
         "correct": 1,
         "expl": "The same setting shared with the previous discourse."},
    ],
    marginalia=[
        ("Four ways of being inclusive", [
            "giving, kindly words,",
            "taking care, treating equally —",
            "matched to what draws each person",
        ]),
        ("An honest caveat", [
            "'my family is wealthy too' —",
            "Hatthaka doesn't overclaim,",
            "and the Buddha doesn't correct him",
        ]),
        ("Eight, finally stated together", [
            "faithful through wise, then:",
            "'and has few wishes' — the eighth",
            "now named outright, not implied",
        ]),
        ("Cross-references", [
            "AN 8.23 &middot; previous, where fewness of wishes was only "
            "revealed obliquely",
            "AN 8.25 &middot; next, a very different question: how is a lay "
            "follower even defined?",
        ]),
    ],
    further=[
        '<a href="%s/an8.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.23.html">AN 8.23 &middot; With Hatthaka (1st)</a> &mdash; previous.',
        '<a href="an-8.25.html">AN 8.25 &middot; With Mahānāma</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.25 — Mahānāmasutta
# --------------------------------------------------------------------------- #
page(
    25, "Mahānāma", "With Mahānāma",
    vagga=VAGGA_3,
    meta_title="AN 8.25 — With Mahānāma | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Mahānāmasutta, in which the Sakyan Mahānāma asks the Buddha to "
        "define a lay follower in four increasingly demanding senses, from "
        "bare refuge to practicing for the benefit of both oneself and "
        "others. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kapilavatthu, in the land of the Sakyans, at the "
                    "Banyan Tree Monastery"),
        ("Speakers", "Mahānāma the Sakyan and the Buddha, in direct "
                     "question-and-answer"),
        ("Form", "Four successive questions, each answer built by adding a "
                 "further condition onto the one before it"),
        ("Length", "~2 minutes to read"),
        ("A ladder of definitions, not a single one", "This discourse "
                                                       "doesn't give one "
                                                       "definition of a lay "
                                                       "follower but four, "
                                                       "each stricter than "
                                                       "the last, ending "
                                                       "with an eightfold "
                                                       "list of qualities "
                                                       "held and actively "
                                                       "encouraged in others"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clean, "
                       "escalating structure, easy to follow across its four "
                       "stages"),
    ],
    why=(
        "Mahānāma asks the Buddha, in four successive questions, how a lay "
        "follower is defined at all, then what makes one ethical, then what "
        "distinguishes a lay follower practicing only for their own "
        "benefit from one practicing for the benefit of both themselves and "
        "others &mdash; the answer to the fourth turning on eight qualities, "
        "each one held and actively encouraged in other people too."),
    guide=[
        ("The teaching in one sentence", [
            "A lay follower is simply someone who has gone for refuge to "
            "the Buddha, the teaching, and the Saṅgha; an ethical lay "
            "follower additionally keeps the five precepts; but a lay "
            "follower practicing for the benefit of both themselves and "
            "others holds eight further qualities and actively encourages "
            "other people to develop the same eight."]),
        ("Four questions, each stricter than the last", [
            "Mahānāma's four questions build a ladder: first, what makes "
            "someone a lay follower at all (refuge alone); second, what "
            "makes that lay follower ethical (the five precepts); third, "
            "what does self-benefiting-only practice look like; and fourth, "
            "what does practice benefiting both oneself and others look "
            "like."]),
        ("The same eight qualities, with and without encouraging others", [
            "The third and fourth answers share an identical eightfold "
            "list &mdash; accomplishment in faith, ethical conduct, "
            "generosity, liking to see mendicants, liking to hear the true "
            "teaching, readily memorizing what's heard, examining its "
            "meaning, and practicing in line with the teaching &mdash; "
            "differing only in whether the lay follower also encourages "
            "other people to develop each one."]),
        ("The single variable that changes everything", [
            "Structurally, this discourse makes a precise point: the "
            "content of one's own practice can be identical in both cases "
            "&mdash; same eight qualities, equally accomplished &mdash; and "
            "still differ entirely in whether it counts as benefiting only "
            "oneself or benefiting both oneself and others, depending "
            "purely on the single added factor of encouraging others."]),
    ],
    terms=[
        ("upāsako",
         "&ldquo;lay follower&rdquo; &mdash; this discourse's own subject, "
         "defined in the most minimal sense as simply someone who has gone "
         "for refuge."),
        ("sīlavā upāsako",
         "&ldquo;an ethical lay follower&rdquo; &mdash; the second, "
         "stricter definition, adding the five precepts to bare refuge."),
        ("attahitāya paṭipanno no parahitāya",
         "&ldquo;practicing to benefit themselves, not others&rdquo; "
         "&mdash; the third definition, an eightfold list held privately, "
         "without encouraging others to develop the same qualities."),
        ("attahitāya ca paṭipanno parahitāya ca",
         "&ldquo;practicing to benefit both themselves and others&rdquo; "
         "&mdash; the fourth and final definition, the identical eightfold "
         "list, now actively encouraged in other people too."),
        ("saddhāsampanno, sīlasampanno, cāgasampanno",
         "&ldquo;accomplished in faith, ethical conduct, and "
         "generosity&rdquo; &mdash; the first three of the eight shared "
         "qualities running through both the third and fourth definitions."),
    ],
    text_intro=(
        "The discourse in full: four successive questions, each answer "
        "building on the one before it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "What defines a lay follower?"),
        ("p", "&sect;1", "an8.25:1.1-1.5"),
        ("h3", "What defines an ethical lay follower?"),
        ("p", "&sect;2", "an8.25:2.1-2.3"),
        ("h3", "Practicing for one's own benefit only"),
        ("p", "&sect;3", "an8.25:3.1-3.10"),
        ("h3", "Practicing for the benefit of both oneself and others"),
        ("p", "&sect;4", "an8.25:4.1-4.10"),
    ],
    quiz=[
        {"q": "How does the Buddha define a lay follower in the most basic "
              "sense?",
         "opts": [
             "Someone who has taken monastic ordination",
             "Someone who has gone for refuge to the Buddha, the teaching, "
             "and the Saṅgha",
             "Someone who has kept the five precepts for a full year",
             "Someone born into a Buddhist family"],
         "correct": 1,
         "expl": "The most minimal definition, refuge alone."},
        {"q": "What distinguishes an 'ethical lay follower' from a bare lay "
              "follower?",
         "opts": [
             "Nothing further is required",
             "Keeping the five precepts — not killing, stealing, sexual "
             "misconduct, lying, or intoxicants",
             "Taking full monastic vows",
             "Donating a specific amount of wealth"],
         "correct": 1,
         "expl": "The second, stricter definition in this discourse's "
                 "ladder."},
        {"q": "What is the single factor that distinguishes 'practicing for "
              "one's own benefit only' from 'practicing for the benefit of "
              "both oneself and others'?",
         "opts": [
             "An entirely different set of qualities",
             "The identical eight qualities, but whether the lay follower "
             "also actively encourages others to develop the same eight",
             "Wealth alone",
             "Physical location"],
         "correct": 1,
         "expl": "A single added variable — encouraging others — not a "
                 "different content of practice."},
        {"q": "What are among the eight shared qualities named in both the "
              "third and fourth definitions?",
         "opts": [
             "Physical strength and endurance",
             "Faith, ethical conduct, generosity, liking to see mendicants "
             "and hear the teaching, memorizing and examining it, and "
             "practicing in line with it",
             "Wealth, status, and family lineage",
             "Skill in debate and public speaking"],
         "correct": 1,
         "expl": "An eightfold list running through both the third and "
                 "fourth definitions."},
        {"q": "How many successive questions does Mahānāma ask in this "
              "discourse?",
         "opts": [
             "One", "Four, each building a stricter definition than the last",
             "Eight", "Two"],
         "correct": 1,
         "expl": "A ladder of four increasingly demanding definitions."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Kapilavatthu, in the land of the "
                                          "Sakyans, at the Banyan Tree "
                                          "Monastery",
             "Rājagaha, on Vulture's Peak", "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "Mahānāma's own homeland, among his fellow Sakyans."},
    ],
    marginalia=[
        ("Four questions, four rungs", [
            "refuge alone · then ethics ·",
            "then self-benefit only ·",
            "then benefit for self and others",
        ]),
        ("The same eight, twice", [
            "faith, ethics, generosity,",
            "hearing and examining the teaching —",
            "identical in both definitions",
        ]),
        ("One variable changes everything", [
            "not a different practice,",
            "but whether it's encouraged",
            "in others too",
        ]),
        ("Cross-references", [
            "AN 8.24 &middot; previous, Hatthaka's full eight qualities "
            "named together",
            "AN 8.26 &middot; next, the same four questions asked again, "
            "this time by Jīvaka",
        ]),
    ],
    further=[
        '<a href="%s/an8.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.24.html">AN 8.24 &middot; With Hatthaka (2nd)</a> &mdash; previous.',
        '<a href="an-8.26.html">AN 8.26 &middot; With Jīvaka</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.26 — Jīvakasutta
# --------------------------------------------------------------------------- #
page(
    26, "Jīvaka", "With Jīvaka",
    vagga=VAGGA_3,
    meta_title="AN 8.26 — With Jīvaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Jīvakasutta, in which the royal physician Jīvaka Komārabhacca asks "
        "the Buddha the identical four questions Mahānāma asked at AN 8.25, "
        "receiving the same ladder of definitions for a lay follower. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, in Jīvaka's own Mango Grove"),
        ("Speakers", "Jīvaka Komārabhacca and the Buddha"),
        ("Form", "The identical four-question structure as AN 8.25, "
                 "compressed in its own source text by an internal "
                 "ellipsis across the middle two questions"),
        ("Length", "~2 minutes to read"),
        ("The same teaching, a different asker", "Jīvaka Komārabhacca, the "
                                                  "physician credited with "
                                                  "treating the Buddha "
                                                  "himself, receives the "
                                                  "identical four-part "
                                                  "answer Mahānāma received "
                                                  "at AN 8.25, in his own "
                                                  "mango grove near Rājagaha"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "best read as a direct companion to AN 8.25"),
    ],
    why=(
        "Jīvaka Komārabhacca, the physician, asks the Buddha the same four "
        "questions Mahānāma asked at AN 8.25 &mdash; how a lay follower is "
        "defined, what makes one ethical, and what distinguishes practicing "
        "only for oneself from practicing for both oneself and others "
        "&mdash; and receives word for word the same answers."),
    guide=[
        ("The teaching in one sentence", [
            "Jīvaka receives the identical four-part definition of a lay "
            "follower that Mahānāma received at AN 8.25: refuge alone, "
            "refuge plus the five precepts, an eightfold list of qualities "
            "held privately, and the same eight actively encouraged in "
            "others as well."]),
        ("A different asker, the same teaching", [
            "Where AN 8.25 features Mahānāma the Sakyan, a member of the "
            "Buddha's own extended clan, this discourse features Jīvaka "
            "Komārabhacca, the renowned physician associated elsewhere in "
            "the tradition with treating the Buddha's own ailments &mdash; "
            "a different social position, the same four questions, the "
            "same four answers."]),
        ("Compressed by the source's own ellipsis", [
            "Unlike AN 8.25, which spells out all four answers in full, "
            "this discourse's own source text compresses the middle two "
            "answers &mdash; the definition of an ethical lay follower and "
            "much of the third definition &mdash; using an internal "
            "ellipsis, trusting the reader to supply what AN 8.25 already "
            "gave in full."]),
        ("Why the same teaching recurs with a new name", [
            "This discourse doesn't add new content to AN 8.25's teaching; "
            "its interest lies in who receives it. A physician known for "
            "treating bodies receives the same graduated ladder toward "
            "benefiting both oneself and others that a Sakyan nobleman "
            "received &mdash; the same path, open regardless of "
            "profession or social standing."]),
    ],
    terms=[
        ("upāsako",
         "&ldquo;lay follower&rdquo; &mdash; the identical subject and "
         "identical first definition as AN 8.25: refuge to the Buddha, the "
         "teaching, and the Saṅgha."),
        ("jīvako komārabhacco",
         "Jīvaka Komārabhacca, the royal physician who asks these "
         "questions in his own mango grove, a figure elsewhere in the "
         "tradition associated with the Buddha's own medical care."),
        ("attahitāya paṭipanno no parahitāya",
         "&ldquo;practicing to benefit themselves, not others&rdquo; "
         "&mdash; the same eightfold private list as AN 8.25, here "
         "compressed by the source's own internal ellipsis."),
        ("attahitāya ca paṭipanno parahitāya ca",
         "&ldquo;practicing to benefit both themselves and others&rdquo; "
         "&mdash; the same eightfold list, spelled out in full for this "
         "discourse's own closing answer."),
        ("saddhāsampanno ... sīlasampanno ... cāgasampanno",
         "&ldquo;accomplished in faith ... ethical conduct ... "
         "generosity&rdquo; &mdash; the shared eight qualities running "
         "through both this discourse and AN 8.25 alike."),
    ],
    text_intro=(
        "The discourse in full: the same four questions Mahānāma asked, this "
        "time from the physician Jīvaka. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "What defines a lay follower?"),
        ("p", "&sect;1", "an8.26:1.1-1.5"),
        ("h3", "What defines an ethical lay follower?"),
        ("p", "&sect;2", "an8.26:2.1-2.3"),
        ("h3", "Practicing for one's own benefit only"),
        ("p", "&sect;3", "an8.26:3.1-3.4"),
        ("h3", "Practicing for the benefit of both oneself and others"),
        ("p", "&sect;4", "an8.26:4.1-4.10"),
    ],
    quiz=[
        {"q": "How does this discourse relate to AN 8.25?",
         "opts": [
             "It contradicts AN 8.25's teaching entirely",
             "It presents the identical four questions and answers, asked "
             "this time by the physician Jīvaka rather than Mahānāma",
             "It has no relation to AN 8.25",
             "It only covers the first of the four questions"],
         "correct": 1,
         "expl": "The same teaching, given to a different asker in a "
                 "different setting."},
        {"q": "Who is Jīvaka Komārabhacca?",
         "opts": [
             "A member of the Buddha's own Sakyan clan",
             "A physician, associated elsewhere in the tradition with "
             "treating the Buddha's own ailments",
             "A rival ascetic teacher", "A king's general"],
         "correct": 1,
         "expl": "A renowned physician, asking in his own mango grove."},
        {"q": "How does this discourse's source text handle the middle two "
              "answers, compared to AN 8.25?",
         "opts": [
             "It expands them with new detail",
             "It compresses them using an internal ellipsis, trusting the "
             "reader to supply what AN 8.25 already gave in full",
             "It omits them entirely",
             "It replaces them with unrelated content"],
         "correct": 1,
         "expl": "A self-abbreviation, relying on the fuller text just "
                 "given at AN 8.25."},
        {"q": "According to the guide, what is this discourse's real point "
              "in repeating AN 8.25's teaching?",
         "opts": [
             "To correct an error in AN 8.25",
             "That the same graduated path is open regardless of "
             "profession or social standing — a physician receives it just "
             "as a nobleman did",
             "To test whether Jīvaka understood the first discourse",
             "There is no particular point; it is a simple duplicate"],
         "correct": 1,
         "expl": "The interest lies in who receives the teaching, not in "
                 "new content."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kapilavatthu, at the Banyan Tree Monastery",
             "Rājagaha, in Jīvaka's own Mango Grove",
             "Sāvatthī, in Jeta's Grove", "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A location named for Jīvaka himself, distinct from AN "
                 "8.25's setting."},
        {"q": "What is the single factor distinguishing the third and "
              "fourth definitions, as in AN 8.25?",
         "opts": [
             "An entirely different set of qualities",
             "Whether the lay follower also actively encourages others to "
             "develop the same eight qualities",
             "Wealth alone",
             "Physical location"],
         "correct": 1,
         "expl": "The identical single variable met at AN 8.25."},
    ],
    marginalia=[
        ("The same four questions", [
            "refuge · then ethics ·",
            "self-benefit only ·",
            "benefit for self and others",
        ]),
        ("A different asker", [
            "not a Sakyan nobleman —",
            "a physician, in his own",
            "mango grove near Rājagaha",
        ]),
        ("Compressed by its own ellipsis", [
            "trusting the reader",
            "to recall AN 8.25's answer —",
            "the middle two questions abbreviated",
        ]),
        ("Cross-references", [
            "AN 8.25 &middot; previous, the same four questions in full, "
            "asked by Mahānāma",
            "AN 8.27 &middot; next, a very different register: proverbial "
            "'powers' of different beings",
        ]),
    ],
    further=[
        '<a href="%s/an8.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.25.html">AN 8.25 &middot; With Mahānāma</a> &mdash; previous.',
        '<a href="an-8.27.html">AN 8.27 &middot; Powers (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.27 — Paṭhamabalasutta
# --------------------------------------------------------------------------- #
page(
    27, "Paṭhamabala", "Powers (1st)",
    vagga=VAGGA_3,
    meta_title="AN 8.27 — Powers (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamabalasutta, a proverbial list of eight different 'powers' "
        "belonging to eight different kinds of being, from a baby's crying "
        "to an ascetic's patience — unrelated in content to AN 8.28 despite "
        "sharing its title numbering. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item proverbial list, one power matched to "
                 "one kind of being, with no further explanation"),
        ("Length", "under 1 minute to read"),
        ("A title pair with unrelated content", "AN 8.27 and 8.28 share "
                                                 "only their Paṭhama/Dutiya "
                                                 "title numbering and the "
                                                 "word &ldquo;power&rdquo; "
                                                 "&mdash; this discourse is a "
                                                 "folk-wisdom catalog of "
                                                 "social types, while AN "
                                                 "8.28 is Sāriputta's own "
                                                 "technical account of an "
                                                 "arahant's inner powers, "
                                                 "with no shared content "
                                                 "between them"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and proverbial, more social observation than "
                       "meditative instruction"),
    ],
    why=(
        "AN 8.27 names eight different &ldquo;powers&rdquo; belonging to "
        "eight different kinds of being &mdash; crying is the power of "
        "babies, anger the power of ladies, weapons the power of bandits, "
        "authority the power of rulers, complaining the power of fools, "
        "reason the power of the astute, reflection the power of the "
        "learned, and patience the power of ascetics and brahmins &mdash; "
        "without further comment or moral evaluation."),
    guide=[
        ("The teaching in one sentence", [
            "Eight different kinds of being each rely on a characteristic "
            "&ldquo;power&rdquo; distinct to their situation: babies on "
            "crying, ladies on anger, bandits on weapons, rulers on "
            "authority, fools on complaining, the astute on reason, the "
            "learned on reflection, and ascetics and brahmins on patience."]),
        ("A proverb, not a teaching with commentary", [
            "Unlike most discourses in this book, AN 8.27 offers no "
            "explanation, no praise, and no criticism of any of the eight "
            "pairings. It simply states them, in the manner of a folk "
            "proverb observing how different kinds of people or beings get "
            "what they want."]),
        ("A title pair that shares nothing but a number", [
            "AN 8.27 and AN 8.28, immediately following, are titled "
            "&ldquo;Powers (1st)&rdquo; and &ldquo;Powers (2nd)&rdquo; as "
            "though they were a matched pair like AN 8.17/8.18 or 8.23/8.24 "
            "&mdash; but their content shares nothing beyond the word "
            "&ldquo;power&rdquo; itself. This is worth noticing explicitly: "
            "not every Paṭhama/Dutiya title pair in this collection carries "
            "paired content."]),
        ("Patience, closing the list at its highest register", [
            "The list moves through a rough social hierarchy &mdash; from "
            "an infant's helpless crying through a ruler's institutional "
            "authority to reasoning and reflection &mdash; and closes with "
            "patience as the characteristic power of ascetics and "
            "brahmins, placing spiritual endurance at the top of this "
            "particular proverbial ladder."]),
    ],
    terms=[
        ("balāni",
         "&ldquo;powers&rdquo; &mdash; this discourse's own title term, "
         "used here in a loose, proverbial sense rather than the technical "
         "sense met at AN 8.28."),
        ("rodanaṁ bālassa balaṁ",
         "&ldquo;crying is the power of babies&rdquo; &mdash; the first "
         "pairing, opening the list at its most helpless register."),
        ("āyudhaṁ corānaṁ balaṁ",
         "&ldquo;weapons are the power of bandits&rdquo; &mdash; the third "
         "pairing, naming a power that is coercive rather than social or "
         "reflective."),
        ("upanijjhāyanā paṇḍitassa balaṁ",
         "&ldquo;reflection is the power of the learned&rdquo; &mdash; the "
         "seventh pairing, distinguished from the sixth item's bare "
         "reason by its more deliberate, considered quality."),
        ("khantībalaṁ samaṇabrāhmaṇānaṁ",
         "&ldquo;patience is the power of ascetics and brahmins&rdquo; "
         "&mdash; the eighth and closing pairing, placing spiritual "
         "endurance at the top of the list's rough hierarchy."),
    ],
    text_intro=(
        "The discourse in full: eight powers, matched to eight kinds of "
        "being. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight powers, eight kinds of being"),
        ("p", "&sect;1", "an8.27:1.1-1.4"),
    ],
    quiz=[
        {"q": "What are the eight 'powers' this discourse names?",
         "opts": [
             "The five spiritual faculties plus three more",
             "Crying (babies), anger (ladies), weapons (bandits), "
             "authority (rulers), complaining (fools), reason (astute), "
             "reflection (learned), and patience (ascetics and brahmins)",
             "The seven factors of awakening plus one",
             "Eight monastic requisites"],
         "correct": 1,
         "expl": "A proverbial catalog matching one power to one kind of "
                 "being."},
        {"q": "How does this discourse present its eight pairings?",
         "opts": [
             "With extensive doctrinal commentary on each",
             "Without explanation, praise, or criticism — stated plainly, "
             "in the manner of a folk proverb",
             "As a set of instructions to be followed",
             "As a warning against each of the eight"],
         "correct": 1,
         "expl": "A bare observational list, not a teaching with "
                 "commentary."},
        {"q": "According to the guide, how does this discourse relate to AN "
              "8.28, despite sharing its title numbering?",
         "opts": [
             "They share identical content",
             "They share only the word 'power' and the Paṭhama/Dutiya "
             "numbering — the actual content is unrelated",
             "AN 8.28 directly contradicts this discourse",
             "AN 8.28 is a longer version of this same list"],
         "correct": 1,
         "expl": "A rare title pair without paired content, worth noticing "
                 "explicitly."},
        {"q": "What is named as the power of ascetics and brahmins, closing "
              "the list?",
         "opts": [
             "Wealth", "Patience",
             "Physical strength", "Political influence"],
         "correct": 1,
         "expl": "The eighth and final pairing, placing spiritual endurance "
                 "at the top of the list's rough hierarchy."},
        {"q": "What is named as the power of bandits?",
         "opts": [
             "Cunning alone", "Weapons",
             "Wealth", "Speed"],
         "correct": 1,
         "expl": "A coercive power, distinct from the social or reflective "
                 "powers named elsewhere in the list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight powers, eight beings", [
            "crying · anger · weapons ·",
            "authority · complaining ·",
            "reason · reflection · patience",
        ]),
        ("A proverb, not a teaching", [
            "no praise, no criticism —",
            "stated plainly, the way",
            "an old saying simply is",
        ]),
        ("A title pair, unrelated content", [
            "'Powers (1st)' and '(2nd)' —",
            "the same word, different subjects —",
            "worth not assuming they match",
        ]),
        ("Cross-references", [
            "AN 8.26 &middot; previous, Jīvaka's own four questions",
            "AN 8.28 &middot; next, a genuinely different 'powers' — an "
            "arahant's own, named by Sāriputta",
        ]),
    ],
    further=[
        '<a href="%s/an8.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.26.html">AN 8.26 &middot; With Jīvaka</a> &mdash; previous.',
        '<a href="an-8.28.html">AN 8.28 &middot; Powers (2nd)</a> &mdash; next, unrelated in '
        "content despite the shared title.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.28 — Dutiyabalasutta
# --------------------------------------------------------------------------- #
page(
    28, "Dutiyabala", "Powers (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 8.28 — Powers (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyabalasutta, in which Venerable Sāriputta answers the Buddha's "
        "own question by naming eight powers that qualify a mendicant who "
        "has ended the defilements to claim arahantship. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, questioning, and Venerable Sāriputta, "
                     "answering"),
        ("Form", "A direct question from the Buddha, answered by Sāriputta "
                 "with an eight-item list, the last four compressed by "
                 "internal ellipsis into a single unbroken group"),
        ("Length", "~2 minutes to read"),
        ("A technical 'powers,' not a proverbial one", "Unlike AN 8.27's "
                                                        "folk catalog, this "
                                                        "discourse's "
                                                        "&ldquo;powers&rdquo; "
                                                        "are specific "
                                                        "meditative insights "
                                                        "and factors of the "
                                                        "path that ground an "
                                                        "arahant's own claim "
                                                        "to complete freedom"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "final four items compress several major doctrinal "
                       "categories rapidly, worth reading closely"),
    ],
    why=(
        "Asked by the Buddha how many powers qualify a mendicant who has "
        "ended the defilements to claim arahantship, Sāriputta names eight: "
        "clear insight into impermanence, seeing sensual pleasures as a pit "
        "of glowing coals, a mind inclined to seclusion, and the "
        "cultivation of the four kinds of mindfulness meditation, the four "
        "bases of psychic power, the five faculties, the seven awakening "
        "factors, and the noble eightfold path."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has ended the defilements has eight powers "
            "that qualify the claim &ldquo;my defilements have ended&rdquo;: "
            "clearly seeing all conditions as impermanent, seeing sensual "
            "pleasures as a pit of glowing coals, a mind inclined to "
            "seclusion, and the full development of the four kinds of "
            "mindfulness meditation, the four bases of psychic power, the "
            "five faculties, the seven awakening factors, and the noble "
            "eightfold path."]),
        ("Sāriputta answers a direct question from the Buddha", [
            "Rather than the Buddha teaching this list to the mendicants "
            "directly, the Buddha poses the question to Sāriputta by name, "
            "and it is Sāriputta's own answer that constitutes the entire "
            "discourse &mdash; one of several places in this book where the "
            "Buddha's foremost disciple in wisdom speaks in his own voice."]),
        ("Three insights, then five factor-groups", [
            "The first three powers are individual insights: seeing "
            "impermanence clearly, seeing sensuality as dangerous as glowing "
            "coals, and a mind that naturally inclines toward seclusion. "
            "The remaining five powers are not individual insights but "
            "entire groups of practice factors, compressed by the source's "
            "own internal ellipsis into a single flowing list."]),
        ("The full architecture of practice, named in one breath", [
            "The final five powers name, in sequence, the four kinds of "
            "mindfulness meditation, the four bases of psychic power, the "
            "five faculties, the seven awakening factors, and the noble "
            "eightfold path &mdash; the same major groupings this project "
            "has already met named together at AN 7.71 as the full "
            "thirty-seven factors of awakening, here folded into a single "
            "power among eight."]),
    ],
    terms=[
        ("khīṇāsavo",
         "&ldquo;a mendicant who has ended the defilements&rdquo; &mdash; "
         "an arahant, the subject of Sāriputta's entire answer."),
        ("sabbe saṅkhārā aniccato yathābhūtaṁ sammappaññāya sudiṭṭhā "
         "honti",
         "&ldquo;has clearly seen with right wisdom all conditions as truly "
         "impermanent&rdquo; &mdash; the first power, an insight into "
         "impermanence itself."),
        ("aṅgārakāsūpamā kāmā yathābhūtaṁ sammappaññāya sudiṭṭhā "
         "honti",
         "&ldquo;has clearly seen with right wisdom that sensual pleasures "
         "are truly like a pit of glowing coals&rdquo; &mdash; the second "
         "power, a vivid simile for the danger of sensuality."),
        ("vivekaninnaṁ cittaṁ hoti vivekapoṇaṁ vivekapabbhāraṁ",
         "&ldquo;the mind slants, slopes, and inclines to seclusion&rdquo; "
         "&mdash; the third power, describing a settled orientation rather "
         "than an occasional state."),
        ("cattāro satipaṭṭhānā ... cattāro iddhipādā ... "
         "pañcindriyāni ... satta bojjhaṅgā ... ariyo aṭṭhaṅgiko "
         "maggo",
         "the four kinds of mindfulness meditation, the four bases of "
         "psychic power, the five faculties, the seven awakening factors, "
         "and the noble eightfold path &mdash; the remaining five powers, "
         "together spanning the full thirty-seven factors of awakening."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's question, and Sāriputta's own "
        "eight-power answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha's question to Sāriputta"),
        ("p", "&sect;1", "an8.28:1.1-2.1"),
        ("h3", "Three insights"),
        ("p", "&sect;2", "an8.28:2.2-4.3"),
        ("h3", "Five factor-groups, in one breath"),
        ("p", "&sect;3", "an8.28:5.1-7.2"),
    ],
    quiz=[
        {"q": "Who answers the Buddha's question in this discourse?",
         "opts": [
             "The Buddha answers his own question",
             "Venerable Sāriputta, speaking in his own voice",
             "Venerable Ānanda", "General Sīha"],
         "correct": 1,
         "expl": "One of several discourses where Sāriputta's own answer "
                 "constitutes the entire teaching."},
        {"q": "What is the second power Sāriputta names?",
         "opts": [
             "Skill in debate",
             "Clearly seeing with right wisdom that sensual pleasures are "
             "truly like a pit of glowing coals",
             "Physical endurance",
             "Wealth given up entirely"],
         "correct": 1,
         "expl": "A vivid simile for the danger of sensuality, the second "
                 "of three individual insights."},
        {"q": "How does the guide describe the difference between this "
              "discourse's 'powers' and AN 8.27's?",
         "opts": [
             "They are identical in every respect",
             "This discourse's powers are specific meditative insights and "
             "path factors grounding an arahant's claim, unlike AN 8.27's "
             "proverbial social catalog",
             "AN 8.27 also concerns arahantship",
             "There is no difference at all"],
         "correct": 1,
         "expl": "A technical, doctrinal sense of 'power,' distinct from AN "
                 "8.27's folk-proverb register."},
        {"q": "What do the final five powers name together?",
         "opts": [
             "Five unrelated miscellaneous qualities",
             "The four kinds of mindfulness meditation, the four bases of "
             "psychic power, the five faculties, the seven awakening "
             "factors, and the noble eightfold path — spanning the full "
             "thirty-seven factors of awakening",
             "Five different meditation postures",
             "Five monastic requisites"],
         "correct": 1,
         "expl": "The major groupings already met assembled together at AN "
                 "7.71, here folded into a single power."},
        {"q": "What claim do these eight powers qualify a mendicant to "
              "make?",
         "opts": [
             "'I am the wisest in the Saṅgha'",
             "'My defilements have ended'",
             "'I will become a Buddha'",
             "'I have never made a mistake'"],
         "correct": 1,
         "expl": "The Buddha's own opening question, answered fully by "
                 "Sāriputta's eight powers."},
        {"q": "What is the third power, describing the arahant's mind?",
         "opts": [
             "A mind fixed on wealth",
             "A mind that slants, slopes, and inclines toward seclusion",
             "A mind focused on debate",
             "A mind seeking fame"],
         "correct": 1,
         "expl": "A settled orientation toward seclusion, not an occasional "
                 "state."},
    ],
    marginalia=[
        ("Three insights, named first", [
            "impermanence, seen clearly —",
            "sensuality like glowing coals —",
            "a mind inclined to seclusion",
        ]),
        ("Five factor-groups, in one breath", [
            "mindfulness, psychic power,",
            "faculties, awakening factors,",
            "the noble eightfold path",
        ]),
        ("Sāriputta answers directly", [
            "not the Buddha teaching outright —",
            "his foremost disciple in wisdom",
            "speaks the entire discourse",
        ]),
        ("Cross-references", [
            "AN 8.27 &middot; previous, a proverbial 'powers' unrelated in "
            "content",
            "AN 8.29 &middot; next, the eight lost opportunities for "
            "spiritual practice",
        ]),
    ],
    further=[
        '<a href="%s/an8.28/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.27.html">AN 8.27 &middot; Powers (1st)</a> &mdash; previous, unrelated '
        "in content despite the shared title.",
        '<a href="an-8.29.html">AN 8.29 &middot; Lost Opportunities</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.29 — Akkhaṇasutta — closes new content for ch.3 Gahapativagga.
# an-8.30.html already exists (earlier eighteen-page selection); splice in
# with an explicit next=, per the an-6.16/an-6.63/an-7.6/an-7.5 precedent.
# --------------------------------------------------------------------------- #
page(
    29, "Akkhaṇa", "Lost Opportunities",
    vagga=VAGGA_3,
    meta_title="AN 8.29 — Lost Opportunities | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Akkhaṇasutta, naming eight wasted circumstances for spiritual "
        "practice and the single narrow opportunity that isn't wasted, "
        "closing with verses on the rarity of a Buddha's arising. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight wasted circumstances, each pairing a Buddha's "
                 "arising with an obstacle that squanders it, followed by "
                 "the single circumstance that isn't wasted and ten closing "
                 "verses"),
        ("Length", "~4 minutes to read"),
        ("Closing this chapter's new content", "This is the last discourse "
                                               "newly built for this "
                                               "chapter; AN 8.30, "
                                               "immediately following, "
                                               "already exists from this "
                                               "site's earlier eighteen-page "
                                               "selection and closes the "
                                               "chapter itself"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; eight "
                       "parallel structures followed by a sustained closing "
                       "verse sequence"),
    ],
    why=(
        "AN 8.29 names eight circumstances in which a Realized One's "
        "arising in the world is wasted &mdash; rebirth in hell, as an "
        "animal, as a ghost, among long-lived gods, in the borderlands, or "
        "as a human with wrong view or with dullness even in a central "
        "country, and even a Buddha's non-arising when someone is otherwise "
        "perfectly positioned &mdash; against the single narrow window in "
        "which the opportunity is not wasted at all."),
    guide=[
        ("The teaching in one sentence", [
            "Of eight circumstances that waste the rare opportunity of a "
            "Realized One's arising in the world &mdash; four unfortunate "
            "rebirths, life in the borderlands, wrong view, dullness, or a "
            "Buddha's own non-arising &mdash; only one narrow window "
            "combines every necessary condition: a Buddha has arisen, a "
            "person is reborn in a central country, and that person is "
            "wise enough to distinguish good teaching from bad."]),
        ("Seven wasted rebirths, and an eighth wasted circumstance", [
            "The first seven lost opportunities all begin the same way "
            "&mdash; a Realized One has arisen in the world &mdash; and "
            "then name a circumstance that squanders that arising: rebirth "
            "in hell, as an animal, as a ghost, among long-lived gods "
            "unable to hear teaching, in remote borderlands teaching never "
            "reaches, or as a human in a central country who either holds "
            "wrong view or is simply too dull to tell good teaching from "
            "bad."]),
        ("The eighth lost opportunity inverts the pattern", [
            "Where the first seven all begin with a Buddha having arisen, "
            "the eighth reverses the condition entirely: a person is born "
            "wise, bright, and capable in a central country, but no "
            "Realized One has arisen in the world at all &mdash; showing "
            "that even ideal personal readiness is wasted without the "
            "teaching itself being available."]),
        ("One narrow window, and verses on its rarity", [
            "Only one combination avoids every obstacle: a Buddha has "
            "arisen, teaching in a way that leads to peace and awakening, "
            "and a person is reborn in a central country with the wisdom "
            "to distinguish well-spoken teaching from poorly spoken "
            "teaching. The closing verses press the urgency of this rare "
            "coincidence, warning that missing it invites long regret, "
            "&ldquo;like the merchant in the story of the past.&rdquo;"]),
    ],
    terms=[
        ("akkhaṇo",
         "&ldquo;lost opportunity, wrong time&rdquo; &mdash; this "
         "discourse's own title term, a circumstance in which spiritual "
         "practice cannot take root even when a Buddha has arisen."),
        ("majjhimesu janapadesu paccājāto hoti",
         "&ldquo;reborn in a central country&rdquo; &mdash; a necessary but "
         "not sufficient condition, required alongside a Buddha's arising "
         "and personal wisdom for the one opportunity that isn't wasted."),
        ("micchādiṭṭhiko hoti viparītadassano",
         "&ldquo;has wrong view and distorted perspective&rdquo; &mdash; "
         "the sixth lost opportunity, denying moral consequence and the "
         "afterlife even while born in a favorable location."),
        ("duppañño hoti eḷamūgo",
         "&ldquo;witless, dull, idiotic&rdquo; &mdash; the seventh lost "
         "opportunity, unable to distinguish good teaching from bad even "
         "under otherwise favorable conditions."),
        ("khaṇo yathā bhaddaṁ tathā vadanti",
         "part of the closing verses' warning &mdash; that only rare "
         "occasions see a Realized One arise, and missing the moment "
         "brings regret &ldquo;like the merchant in the story of the "
         "past.&rdquo;"),
    ],
    text_intro=(
        "The discourse in full: eight lost opportunities, the one "
        "opportunity that isn't wasted, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four wasted rebirths"),
        ("p", "&sect;1", "an8.29:1.1-4.2"),
        ("h3", "Borderlands, wrong view, and dullness"),
        ("p", "&sect;2", "an8.29:5.1-7.3"),
        ("h3", "The eighth lost opportunity, inverted"),
        ("p", "&sect;3", "an8.29:8.1-9.1"),
        ("h3", "The one opportunity that isn't wasted"),
        ("p", "&sect;4", "an8.29:10.1-10.5"),
        ("h3", "Closing verses"),
        ("p", "&sect;5", "an8.29:11.1-20.4"),
    ],
    quiz=[
        {"q": "What do the first seven lost opportunities all share as a "
              "starting condition?",
         "opts": [
             "A person's own choice to reject the teaching",
             "A Realized One has arisen in the world",
             "A famine or natural disaster",
             "The absence of any teacher at all"],
         "correct": 1,
         "expl": "Each of the first seven pairs a Buddha's arising with a "
                 "circumstance that wastes it."},
        {"q": "How does the eighth lost opportunity differ in structure from "
              "the first seven?",
         "opts": [
             "It is identical in structure to the others",
             "It reverses the condition — a person is born wise and "
             "well-placed, but no Realized One has arisen at all",
             "It doesn't involve rebirth in any form",
             "It is the only opportunity that isn't actually wasted"],
         "correct": 1,
         "expl": "Even ideal personal readiness is wasted without the "
                 "teaching being available at all."},
        {"q": "What three conditions together make up the single "
              "opportunity that isn't wasted?",
         "opts": [
             "Wealth, health, and a long life",
             "A Buddha has arisen and teaches, a person is reborn in a "
             "central country, and that person is wise enough to tell good "
             "teaching from bad",
             "Physical strength, courage, and patience",
             "Royal birth, education, and fame"],
         "correct": 1,
         "expl": "A narrow window combining every necessary condition at "
                 "once."},
        {"q": "What does the sixth lost opportunity name, for someone born "
              "in a central country?",
         "opts": [
             "Physical illness",
             "Wrong view and a distorted perspective, denying moral "
             "consequence and the afterlife",
             "Poverty", "Old age"],
         "correct": 1,
         "expl": "Favorable birth alone doesn't guarantee the view needed "
                 "to benefit from a Buddha's teaching."},
        {"q": "What do the closing verses warn happens to someone who misses "
              "this rare opportunity?",
         "opts": [
             "Nothing of consequence",
             "Long regret, compared to a merchant in a story of the past, "
             "and continued transmigration through birth and death",
             "Immediate awakening regardless",
             "A second chance guaranteed in the same lifetime"],
         "correct": 1,
         "expl": "The verses press the urgency of a coincidence the "
                 "discourse calls rare."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Seven wasted rebirths", [
            "hell, animal, ghost realm,",
            "long-lived gods, borderlands,",
            "wrong view, or simple dullness",
        ]),
        ("The eighth, inverted", [
            "wise, well-placed, ready —",
            "but no Buddha has arisen —",
            "readiness alone isn't enough",
        ]),
        ("One narrow window", [
            "a Buddha teaching, a person",
            "born well, and wise enough",
            "to tell good teaching from bad",
        ]),
        ("Cross-references", [
            "AN 8.28 &middot; previous, Sāriputta's own eight powers",
            "AN 8.21 &middot; earlier, opening this chapter's run of "
            "householder portraits",
        ]),
    ],
    further=[
        '<a href="%s/an8.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.28.html">AN 8.28 &middot; Powers (2nd)</a> &mdash; previous.',
        '<a href="an-8.21.html">AN 8.21 &middot; With Ugga of Vesālī</a> &mdash; earlier, '
        "opening this chapter's run of householder portraits.",
    ],
    next=("an-8.30.html", "AN 8.30 &middot; Anuruddha and the Great Thoughts"),
)


VAGGA_4 = "<em>Dānavagga</em> &mdash; the fourth chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.31 — Paṭhamadānasutta — opens ch.4 Dānavagga. an-8.30.html (existing)
# sits before this chapter; its own next= stays pointed at an-8.53.html for
# now (nearest already-published page) until ch.6 splices that page in too.
# --------------------------------------------------------------------------- #
page(
    31, "Paṭhamadāna", "Giving (1st)",
    vagga=VAGGA_4,
    meta_title="AN 8.31 — Giving (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamadānasutta, opening a new chapter with eight different "
        "motives behind a gift, ranging from insult and fear through "
        "reciprocity and reputation to giving as an adornment of the mind. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item list of motives, with no evaluative "
                 "ranking or commentary attached to any of them"),
        ("Length", "under 1 minute to read"),
        ("A new chapter on giving, opening without judgment", "This opens "
                                                               "Dānavagga, "
                                                               "the Chapter "
                                                               "on Giving, "
                                                               "but its own "
                                                               "first "
                                                               "discourse "
                                                               "simply "
                                                               "catalogs "
                                                               "motives "
                                                               "without "
                                                               "ranking them "
                                                               "from worst to "
                                                               "best"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and "
                       "purely descriptive, though several of its eight "
                       "motives are unflattering"),
    ],
    why=(
        "AN 8.31 opens a new chapter by naming eight different motives that "
        "lead someone to give a gift &mdash; after insulting the recipient, "
        "out of fear, out of reciprocity already received or expected, "
        "because giving is simply thought good, out of social obligation, "
        "for reputation, or as an adornment for the mind &mdash; without "
        "ranking any of the eight as better or worse than the others."),
    guide=[
        ("The teaching in one sentence", [
            "People give gifts for eight different reasons &mdash; after "
            "insulting the recipient, out of fear, out of reciprocity "
            "already received or hoped for, because giving is simply "
            "thought good, out of a sense of social obligation, for "
            "reputation, or to adorn and equip the mind &mdash; and this "
            "discourse simply names all eight without ranking them."]),
        ("From hostile to reflective, without commentary", [
            "The list moves, roughly, from the least admirable motive "
            "(giving while insulting the recipient, or out of plain fear) "
            "through transactional motives (reciprocity given or expected) "
            "to more reflective ones (thinking giving is simply good, "
            "honoring family obligation, seeking reputation, or treating "
            "giving as equipment for the mind) &mdash; but the discourse "
            "itself offers no verdict on any of them."]),
        ("A catalog opening a chapter, not a conclusion", [
            "Rather than closing this chapter's exploration of giving with "
            "a final judgment, this discourse opens it by simply mapping "
            "the range of motives that actually drive people to give, "
            "setting up the more evaluative discourses on giving that "
            "follow later in this same chapter."]),
        ("The final motive: giving as equipment for the mind", [
            "The list's last item stands apart from the rest: giving "
            "&ldquo;as an adornment and requisite for the mind&rdquo; "
            "treats generosity itself as a form of inner cultivation, not "
            "a means to any external end &mdash; reputation, reciprocity, "
            "or obligation &mdash; that the other seven motives all still "
            "point toward."]),
    ],
    terms=[
        ("dānāni",
         "&ldquo;gifts&rdquo; &mdash; this discourse's own title term, here "
         "distinguished by the motive behind each of the eight, not by "
         "size or recipient."),
        ("sāsaṅkena vā deti",
         "&ldquo;gives out of fear&rdquo; &mdash; the second motive, giving "
         "under a sense of threat or obligation rather than free choice."),
        ("adāsi me'ti deti, dassati me'ti deti",
         "&ldquo;gives thinking, &lsquo;they gave to me&rsquo; ... "
         "&lsquo;they'll give to me&rsquo;&rdquo; &mdash; the third and "
         "fourth motives, both forms of reciprocity, past and anticipated."),
        ("sādhu dānan'ti deti",
         "&ldquo;gives thinking, &lsquo;it's good to give&rsquo;&rdquo; "
         "&mdash; the fifth motive, a general moral conviction rather than "
         "any personal transaction."),
        ("cittālaṅkāraparikkhāranti deti",
         "&ldquo;gives thinking, &lsquo;this is an adornment and requisite "
         "for the mind&rsquo;&rdquo; &mdash; the eighth and final motive, "
         "treating generosity as inner cultivation rather than a means to "
         "an external end."),
    ],
    text_intro=(
        "The discourse in full: eight motives behind a gift, named without "
        "ranking. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight motives behind a gift"),
        ("p", "&sect;1", "an8.31:1.1-1.11"),
    ],
    quiz=[
        {"q": "What does this discourse do with its eight motives for "
              "giving?",
         "opts": [
             "Ranks them clearly from worst to best",
             "Simply names all eight without ranking or evaluating any of "
             "them",
             "Condemns all eight as equally wrong",
             "Praises only the first motive"],
         "correct": 1,
         "expl": "A bare catalog, opening this chapter without a verdict."},
        {"q": "What are two of the more transactional motives named?",
         "opts": [
             "Giving purely at random",
             "Giving because 'they gave to me' or because 'they'll give to "
             "me'",
             "Giving only to family members",
             "Giving only on religious holidays"],
         "correct": 1,
         "expl": "Reciprocity already received and reciprocity anticipated, "
                 "the third and fourth motives."},
        {"q": "What is the eighth and final motive named?",
         "opts": [
             "Giving purely for tax benefit",
             "Giving thinking 'this is an adornment and requisite for the "
             "mind'",
             "Giving only under legal compulsion",
             "Giving to win a public contest"],
         "correct": 1,
         "expl": "Giving treated as inner cultivation, not a means to an "
                 "external end."},
        {"q": "What chapter does this discourse open?",
         "opts": [
             "Gahapativagga, the Chapter on Householders",
             "Dānavagga, the Chapter on Giving",
             "Mahāvagga, the Great Chapter",
             "Rāgapeyyāla"],
         "correct": 1,
         "expl": "A new chapter, opened with a motive catalog rather than a "
                 "final judgment."},
        {"q": "According to the guide, how does the list's rough order "
              "move?",
         "opts": [
             "Randomly, with no discernible pattern",
             "Roughly from less admirable motives (insult, fear) through "
             "transactional ones to more reflective ones",
             "From best to worst",
             "Alphabetically by motive name"],
         "correct": 1,
         "expl": "A loose gradient, though the discourse itself offers no "
                 "explicit ranking."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "book."},
    ],
    marginalia=[
        ("Eight motives, unranked", [
            "after insult, out of fear,",
            "reciprocity, obligation,",
            "reputation, or mind's adornment",
        ]),
        ("Opening, not concluding", [
            "no verdict given here —",
            "a map of real motives,",
            "setting up what follows",
        ]),
        ("The mind's own equipment", [
            "the eighth motive stands apart:",
            "giving as inner cultivation,",
            "not a means to any external end",
        ]),
        ("Cross-references", [
            "AN 8.30 &middot; earlier, closing the previous chapter",
            "AN 8.32 &middot; next, the same theme in four lines of verse",
        ]),
    ],
    further=[
        '<a href="%s/an8.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.30.html">AN 8.30 &middot; Anuruddha and the Great Thoughts</a> '
        "&mdash; earlier, closing the previous chapter.",
        '<a href="an-8.32.html">AN 8.32 &middot; Giving (2nd)</a> &mdash; next.',
    ],
    prev=("an-8.30.html", "AN 8.30 &middot; Anuruddha and the Great Thoughts"),
)


# --------------------------------------------------------------------------- #
# AN 8.32 — Dutiyadānasutta
# --------------------------------------------------------------------------- #
page(
    32, "Dutiyadāna", "Giving (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 8.32 — Giving (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyadānasutta, a single four-line verse naming faith, "
        "conscience, and skillful giving as the path true persons follow "
        "toward the heavenly realm — the shortest discourse in this "
        "chapter so far. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single four-line verse, with no prose framing at all"),
        ("Length", "a few seconds to read"),
        ("The shortest discourse in this chapter", "Unlike AN 8.31's "
                                                    "eight-item prose "
                                                    "catalog, this "
                                                    "discourse's entire "
                                                    "content is four lines "
                                                    "of verse naming only "
                                                    "three qualities, not "
                                                    "eight, despite sharing "
                                                    "AN 8.31's title "
                                                    "numbering"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "enough to read in seconds"),
    ],
    why=(
        "AN 8.32 names, in a single verse, the qualities true persons "
        "follow &mdash; faith, conscience, and skillful giving &mdash; as "
        "the path of the gods leading to the heavenly realm."),
    guide=[
        ("The teaching in one sentence", [
            "Faith, conscience, and skillful giving are the qualities that "
            "true persons follow, said to constitute the path of the gods "
            "leading to the heavenly realm."]),
        ("Three qualities, not eight", [
            "Despite carrying the &ldquo;2nd&rdquo; in a title pair with AN "
            "8.31, this discourse's actual content names only three "
            "qualities &mdash; faith, conscience, and skillful giving "
            "&mdash; not eight. Like AN 8.16 and AN 8.36 elsewhere in this "
            "book, it belongs to the Book of the Eights by collection "
            "placement, not by presenting an eightfold list."]),
        ("A verse without prose framing", [
            "Where nearly every other discourse in this book opens with at "
            "least a brief prose setting or address to the mendicants, this "
            "one is entirely verse, with no narrative frame at all &mdash; "
            "the shortest and most condensed discourse met in this chapter "
            "so far."]),
        ("The path of the gods", [
            "The verse's closing image, &ldquo;the path of the gods, which "
            "leads to the heavenly realm,&rdquo; names a specific "
            "destination rather than describing awakening itself &mdash; a "
            "modest, this-worldly goal appropriate to a verse about "
            "ordinary virtues like faith, conscience, and giving."]),
    ],
    terms=[
        ("saddhā, hiri, dānañca",
         "&ldquo;faith, conscience, and giving&rdquo; &mdash; the three "
         "qualities this brief verse names, sharing the second and third "
         "terms with values met throughout this book's blocking-and-"
         "reversal lists."),
        ("sappurisā",
         "&ldquo;true persons&rdquo; &mdash; those who follow these three "
         "qualities, a term this book applies elsewhere to figures like "
         "Hatthaka of Āḷavī."),
        ("devayānaṁ",
         "&ldquo;the path of the gods&rdquo; &mdash; the verse's own name "
         "for the destination these three qualities lead to."),
        ("saggagāmī",
         "&ldquo;leads to the heavenly realm&rdquo; &mdash; the verse's "
         "closing destination, a modest, this-worldly goal rather than "
         "final awakening."),
        ("dānāni",
         "&ldquo;gifts&rdquo; &mdash; the shared title root linking this "
         "discourse to AN 8.31, despite their otherwise unrelated content "
         "and scale."),
    ],
    text_intro=(
        "The discourse in full: a single four-line verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The verse"),
        ("p", "&sect;1", "an8.32:1.1-1.4"),
    ],
    quiz=[
        {"q": "How many qualities does this discourse's verse actually "
              "name?",
         "opts": [
             "Eight, matching this book's numerical theme",
             "Three — faith, conscience, and skillful giving",
             "Five", "None; it is purely descriptive"],
         "correct": 1,
         "expl": "A discourse included by collection placement, not by "
                 "presenting a clean eightfold list, like AN 8.16 and AN "
                 "8.36 elsewhere in this book."},
        {"q": "What form does this entire discourse take?",
         "opts": [
             "A long prose narrative",
             "A single four-line verse, with no prose framing at all",
             "A dialogue between two characters",
             "A list of monastic rules"],
         "correct": 1,
         "expl": "The shortest and most condensed discourse in this chapter "
                 "so far."},
        {"q": "What destination does the verse name for those who follow "
              "faith, conscience, and giving?",
         "opts": [
             "Final awakening in this very life",
             "The path of the gods, leading to the heavenly realm",
             "Rebirth as a wealthy human",
             "No destination is named"],
         "correct": 1,
         "expl": "A modest, this-worldly goal, appropriate to a verse about "
                 "ordinary virtues."},
        {"q": "How does this discourse relate to AN 8.31, which it is "
              "titled as a pair with?",
         "opts": [
             "Identical content, just condensed",
             "Sharing only the title root 'giving' — otherwise unrelated in "
             "content and scale",
             "A direct contradiction of AN 8.31",
             "An expanded version of AN 8.31"],
         "correct": 1,
         "expl": "A shared title, but genuinely different content, like AN "
                 "8.27/8.28's 'Powers' pair."},
        {"q": "Who is said to follow these three qualities?",
         "opts": [
             "Only ordained monastics", "True persons (sappurisā)",
             "Only kings and nobles", "Only the very wealthy"],
         "correct": 1,
         "expl": "A term this book applies elsewhere to lay figures like "
                 "Hatthaka of Āḷavī."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare verse with no narrative frame at all."},
    ],
    marginalia=[
        ("Three qualities, one verse", [
            "faith, conscience,",
            "and skillful giving —",
            "the path true persons follow",
        ]),
        ("Not eight, despite the title", [
            "'Giving (2nd)' in name,",
            "but only three qualities named —",
            "placement, not a matching count",
        ]),
        ("A modest, this-worldly goal", [
            "not awakening itself,",
            "but the path of the gods —",
            "the heavenly realm ahead",
        ]),
        ("Cross-references", [
            "AN 8.31 &middot; previous, eight unranked motives for giving",
            "AN 8.33 &middot; next, a different eightfold list of reasons "
            "to give",
        ]),
    ],
    further=[
        '<a href="%s/an8.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.31.html">AN 8.31 &middot; Giving (1st)</a> &mdash; previous.',
        '<a href="an-8.33.html">AN 8.33 &middot; Reasons to Give</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.33 — Dānavatthusutta
# --------------------------------------------------------------------------- #
page(
    33, "Dānavatthu", "Reasons to Give",
    vagga=VAGGA_4,
    meta_title="AN 8.33 — Reasons to Give | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dānavatthusutta, an eight-item list of grounds for giving that "
        "overlaps only partially with AN 8.31's own eight motives, ranging "
        "from bias and cowardice through family tradition to giving as "
        "equipment for the mind. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item list of grounds for giving, unranked, "
                 "structurally similar to AN 8.31 but only partially "
                 "overlapping in content"),
        ("Length", "under 1 minute to read"),
        ("Not a repeat of AN 8.31", "Both discourses list eight unranked "
                                    "grounds for giving, but this list "
                                    "opens with the four biases "
                                    "(favoritism, hostility, stupidity, "
                                    "cowardice) that AN 8.31 doesn't "
                                    "mention at all, sharing only family "
                                    "tradition and the closing item, giving "
                                    "as equipment for the mind"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and descriptive, best read alongside AN 8.31 to see "
                       "where the two lists genuinely overlap"),
    ],
    why=(
        "AN 8.33 names eight grounds for giving &mdash; out of favoritism, "
        "hostility, stupidity, or cowardice, out of family tradition, in "
        "hope of a heavenly rebirth, for the mental clarity and joy giving "
        "itself produces, or as equipment for the mind &mdash; overlapping "
        "with AN 8.31's own eight motives in only a couple of places."),
    guide=[
        ("The teaching in one sentence", [
            "People give for eight different grounds &mdash; the four "
            "biases of favoritism, hostility, stupidity, and cowardice; "
            "family tradition; hope of heavenly rebirth; the mental clarity "
            "and joy giving produces; or as equipment for the mind &mdash; "
            "named here without ranking, much as AN 8.31 named its own "
            "different eight."]),
        ("Four biases, opening a different list", [
            "This discourse's own first four grounds &mdash; favoritism "
            "(chanda), hostility (dosa), stupidity (moha), and cowardice "
            "(bhaya) &mdash; are the four classic biases (agati) that "
            "corrupt judgment elsewhere in this literature, applied here "
            "specifically to the decision of whether and what to give, a "
            "starting point AN 8.31's list doesn't share at all."]),
        ("Where the two lists genuinely converge", [
            "Despite their different openings, this discourse and AN 8.31 "
            "converge on two points: both name family or social obligation "
            "as a motive (framed here as honoring one's father and "
            "grandfather's own practice of giving), and both close with the "
            "identical final item, giving as &ldquo;an adornment and "
            "requisite for the mind.&rdquo;"]),
        ("Two lists, one honest catalog of human motive", [
            "Read together, AN 8.31 and AN 8.33 don't contradict each "
            "other; they simply survey the same broad territory &mdash; why "
            "people actually give &mdash; from two different angles, "
            "neither claiming to be exhaustive, both landing on the same "
            "final, most reflective motive."]),
    ],
    terms=[
        ("chandā, dosā, mohā, bhayā",
         "&ldquo;out of favoritism, hostility, stupidity, or "
         "cowardice&rdquo; &mdash; this discourse's own opening four "
         "grounds, the four classic biases (agati) applied here to giving."),
        ("pitupitāmahaṁ",
         "&ldquo;my father and my father's father&rdquo; &mdash; the "
         "family-tradition ground, framed here as inherited practice "
         "rather than personal conviction."),
        ("cittaṁ pasīdati, attamano hoti",
         "&ldquo;my mind becomes clear, and I become happy and "
         "joyful&rdquo; &mdash; a ground focused on the immediate inner "
         "effect of giving itself, distinct from any external outcome."),
        ("cittālaṅkāraparikkhāranti",
         "&ldquo;this is an adornment and requisite for the mind&rdquo; "
         "&mdash; the eighth and closing ground, identical in wording to AN "
         "8.31's own final item."),
        ("dānavatthūni",
         "&ldquo;grounds for giving&rdquo; &mdash; this discourse's own "
         "title term, distinct from AN 8.31's simple dānāni, 'gifts.'"),
    ],
    text_intro=(
        "The discourse in full: eight grounds for giving, overlapping only "
        "partly with AN 8.31's own eight. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight grounds for giving"),
        ("p", "&sect;1", "an8.33:1.1-1.4"),
    ],
    quiz=[
        {"q": "What four grounds open this discourse's list?",
         "opts": [
             "Wealth, status, education, and health",
             "Favoritism, hostility, stupidity, and cowardice — the four "
             "classic biases applied here to giving",
             "Faith, effort, mindfulness, and wisdom",
             "The four noble truths"],
         "correct": 1,
         "expl": "The agati, biases that corrupt judgment elsewhere in this "
                 "literature, here applied to the decision to give."},
        {"q": "According to the guide, where do this discourse and AN 8.31 "
              "genuinely converge?",
         "opts": [
             "They share every single item",
             "They converge on family/social obligation and the identical "
             "closing item, giving as equipment for the mind",
             "They share nothing at all",
             "They converge only on the opening item"],
         "correct": 1,
         "expl": "Two overlapping points, despite otherwise different "
                 "openings."},
        {"q": "What ground focuses on the immediate inner effect of giving "
              "itself?",
         "opts": [
             "Giving for public recognition",
             "Giving because the mind becomes clear, happy, and joyful in "
             "the act itself",
             "Giving only to avoid punishment",
             "Giving to settle a debt"],
         "correct": 1,
         "expl": "A ground distinct from any external outcome like "
                 "reputation or rebirth."},
        {"q": "How does the guide characterize the relationship between AN "
              "8.31 and AN 8.33?",
         "opts": [
             "AN 8.33 corrects an error in AN 8.31",
             "They survey the same broad territory of human motive from two "
             "different angles, neither claiming to be exhaustive",
             "They are strictly contradictory",
             "AN 8.33 is simply a shorter summary of AN 8.31"],
         "correct": 1,
         "expl": "Two honest, non-exhaustive catalogs converging on the "
                 "same reflective closing motive."},
        {"q": "What is this discourse's own Pāli title term, and how does "
              "it differ from AN 8.31's?",
         "opts": [
             "Identical titles",
             "Dānavatthūni, 'grounds for giving,' distinct from AN 8.31's "
             "simple dānāni, 'gifts'",
             "This discourse has no Pāli title",
             "The title means 'reasons to refuse giving'"],
         "correct": 1,
         "expl": "A related but distinct title, matching the related but "
                 "distinct content."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.31 and 8.32's own lack of a "
                 "stated setting."},
    ],
    marginalia=[
        ("Four biases, first", [
            "favoritism, hostility,",
            "stupidity, cowardice —",
            "applied here to giving itself",
        ]),
        ("Where the two lists meet", [
            "family tradition, and",
            "'an adornment for the mind' —",
            "the only points AN 8.31 shares",
        ]),
        ("Two honest surveys", [
            "not contradicting each other,",
            "just different angles on",
            "why people actually give",
        ]),
        ("Cross-references", [
            "AN 8.32 &middot; previous, three qualities in a single verse",
            "AN 8.34 &middot; next, a field simile for what makes a gift "
            "fruitful",
        ]),
    ],
    further=[
        '<a href="%s/an8.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.32.html">AN 8.32 &middot; Giving (2nd)</a> &mdash; previous.',
        '<a href="an-8.34.html">AN 8.34 &middot; A Field</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.34 — Khettasutta
# --------------------------------------------------------------------------- #
page(
    34, "Khetta", "A Field",
    vagga=VAGGA_4,
    meta_title="AN 8.34 — A Field | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Khettasutta, mapping eight defects in a poor field and eight "
        "virtues of a good one onto the noble eightfold path, reversed and "
        "upright, as what makes a gift unfruitful or bountiful. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two paired similes — a poor field and a good one, each "
                 "with eight factors — mapped onto the eightfold path "
                 "reversed and upright, closing with an extended series of "
                 "verses built on the word 'excellent'"),
        ("Length", "~3 minutes to read"),
        ("The eightfold path, mapped both ways", "This discourse gives the "
                                                  "noble eightfold path in "
                                                  "its wrong-view form as "
                                                  "what makes a recipient "
                                                  "unfruitful, and in its "
                                                  "right-view form as what "
                                                  "makes a recipient "
                                                  "bountiful — a rare case "
                                                  "of the same eightfold "
                                                  "structure given both "
                                                  "inverted and upright in a "
                                                  "single discourse"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear "
                       "double simile, followed by a verse sequence built "
                       "almost entirely on repetitions of one word"),
    ],
    why=(
        "AN 8.34 compares a poor field &mdash; full of mounds, ditches, "
        "stones, and salt, without deep furrows or irrigation &mdash; to an "
        "ascetic or brahmin with the eight wrong factors of the path, and a "
        "good field &mdash; free of those defects, well irrigated and "
        "bounded &mdash; to one with the eight right factors, closing with "
        "verses that build an entire teaching on generosity around the "
        "single word &ldquo;excellent.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "Just as a field marred by mounds, ditches, stones, salt, "
            "shallow furrows, and poor irrigation yields little from any "
            "seed sown in it, a gift given to someone with wrong view, "
            "purpose, speech, action, livelihood, effort, mindfulness, and "
            "immersion is not very fruitful &mdash; while the same gift "
            "given to someone with the eightfold path's right factors is "
            "highly fruitful, like a well-tended field."]),
        ("Eight defects, eight virtues, in the field itself", [
            "The poor field has mounds and ditches, stones and gravel, "
            "salinity, and shallow furrows, and lacks water inlets, "
            "outlets, irrigation channels, and boundaries. The good field "
            "simply lacks every one of those defects and has every one of "
            "those provisions &mdash; the same eight factors, inverted."]),
        ("The eightfold path, given both wrong and right", [
            "The simile's real weight falls on its application: the "
            "unfruitful recipient has wrong view, wrong purpose, wrong "
            "speech, wrong action, wrong livelihood, wrong effort, wrong "
            "mindfulness, and wrong immersion &mdash; the noble eightfold "
            "path's own eight factors, each inverted &mdash; while the "
            "fruitful recipient has the identical eight factors in their "
            "upright, right form."]),
        ("A closing verse sequence built on one word", [
            "The discourse closes with an extended run of verses that "
            "repeat the word &ldquo;excellent&rdquo; (bhaddaka) again and "
            "again &mdash; excellent field, excellent seed, excellent "
            "rainfall, excellent growth, excellent food, excellent ethics "
            "&mdash; building toward &ldquo;the excellence of "
            "extinguishment&rdquo; as the culmination of the entire "
            "sequence."]),
    ],
    terms=[
        ("khettaṁ",
         "&ldquo;field&rdquo; &mdash; this discourse's own title term and "
         "central image, mapped onto a gift's recipient."),
        ("micchādiṭṭhi, micchāsaṅkappo, micchāvācā, micchākammanto, "
         "micchāājīvo, micchāvāyāmo, micchāsati, micchāsamādhi",
         "the eight factors of the noble eightfold path, each inverted, "
         "describing the recipient in whom a gift bears little fruit."),
        ("sammādiṭṭhi ... sammāsamādhi",
         "the same eight factors of the noble eightfold path, in their "
         "upright form, describing the recipient in whom a gift is "
         "highly fruitful and bountiful."),
        ("khettasampadā ca bījasampadā ca vuṭṭhisampadā ca",
         "&ldquo;an excellent field, an excellent seed, and excellent "
         "rainfall&rdquo; &mdash; the three conditions the closing verses "
         "name as jointly producing an excellent harvest."),
        ("nibbānasampadā",
         "&ldquo;the excellence of extinguishment&rdquo; &mdash; the "
         "closing verses' own culmination, the final &ldquo;excellent&rdquo; "
         "in a sequence that builds from agricultural imagery to complete "
         "freedom."),
    ],
    text_intro=(
        "The discourse in full: a poor field and a good one, mapped onto "
        "the eightfold path reversed and upright, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A poor field, and an unfruitful recipient"),
        ("p", "&sect;1", "an8.34:1.1-2.4"),
        ("h3", "A good field, and a bountiful recipient"),
        ("p", "&sect;2", "an8.34:3.1-4.4"),
        ("h3", "Closing verses: a sequence of 'excellent'"),
        ("p", "&sect;3", "an8.34:5.1-11.4"),
    ],
    quiz=[
        {"q": "What eight factors describe the recipient in whom a gift "
              "bears little fruit?",
         "opts": [
             "The five hindrances plus three more",
             "The noble eightfold path's own eight factors, each inverted "
             "— wrong view through wrong immersion",
             "Poverty, illness, and six other misfortunes",
             "The seven factors of awakening, negated"],
         "correct": 1,
         "expl": "A simile whose real weight falls on mapping the "
                 "eightfold path onto the recipient, inverted."},
        {"q": "What describes the recipient in whom a gift is highly "
              "fruitful and bountiful?",
         "opts": [
             "Wealth and social standing alone",
             "The identical eight factors of the noble eightfold path, in "
             "their upright, right form",
             "Physical beauty",
             "A completely different set of eight qualities"],
         "correct": 1,
         "expl": "The same eightfold structure as the unfruitful case, now "
                 "given upright."},
        {"q": "What eight defects mark the poor field in this discourse's "
              "opening simile?",
         "opts": [
             "Drought, flooding, and six other weather problems",
             "Mounds and ditches, stones and gravel, salinity, shallow "
             "furrows, and lacking irrigation provisions and boundaries",
             "Wrong crop selection alone",
             "Poor soil color"],
         "correct": 1,
         "expl": "Eight physical defects, mapped point for point onto the "
                 "eightfold path's own wrong factors."},
        {"q": "What word do the closing verses repeat throughout their "
              "sequence?",
         "opts": [
             "'Impermanent'", "'Excellent' (bhaddaka)",
             "'Suffering'", "'Empty'"],
         "correct": 1,
         "expl": "A word repeated across field, seed, rainfall, ethics, and "
                 "finally extinguishment itself."},
        {"q": "What does the verse sequence culminate in?",
         "opts": [
             "A description of a bountiful harvest alone",
             "'The excellence of extinguishment' — nibbānasampadā",
             "A warning against generosity",
             "A description of royal wealth"],
         "correct": 1,
         "expl": "The final 'excellent' in a sequence building from "
                 "agriculture to complete freedom."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight defects, eight virtues", [
            "mounds, ditches, stones, salt —",
            "or none of these, well irrigated —",
            "the same eight, inverted",
        ]),
        ("The eightfold path, both ways", [
            "wrong view through wrong immersion —",
            "or right view through right immersion —",
            "the same structure, reversed and upright",
        ]),
        ("A sequence built on one word", [
            "excellent field, seed, rainfall —",
            "excellent ethics, excellent gift —",
            "culminating in extinguishment itself",
        ]),
        ("Cross-references", [
            "AN 8.33 &middot; previous, eight grounds for giving",
            "AN 8.35 &middot; next, eight rebirths a gift can lead to",
        ]),
    ],
    further=[
        '<a href="%s/an8.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.33.html">AN 8.33 &middot; Reasons to Give</a> &mdash; previous.',
        '<a href="an-8.35.html">AN 8.35 &middot; Rebirth by Giving</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.35 — Dānūpapattisutta
# --------------------------------------------------------------------------- #
page(
    35, "Dānūpapatti", "Rebirth by Giving",
    vagga=VAGGA_4,
    meta_title="AN 8.35 — Rebirth by Giving | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dānūpapattisutta, on eight rebirth destinies a gift-giver's own "
        "closing wish can produce, from favored human company up through "
        "successive heavens, and why only ethical people can succeed at "
        "any of them. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight parallel cases, each pairing generosity expecting "
                 "something back with a specific rebirth wish, compressed "
                 "in the middle by the source's own internal ellipsis"),
        ("Length", "~2 minutes to read"),
        ("Eight destinies from one shared mechanism", "Despite naming eight "
                                                       "different rebirth "
                                                       "outcomes, every "
                                                       "single one runs "
                                                       "through the "
                                                       "identical "
                                                       "mechanism: giving "
                                                       "while expecting "
                                                       "something back, "
                                                       "then settling on, "
                                                       "stabilizing, and "
                                                       "developing a "
                                                       "specific rebirth "
                                                       "wish"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "repeating structure across eight tiers, with a "
                       "notable added condition at the very top"),
    ],
    why=(
        "AN 8.35 traces eight destinies a gift-giver's own mental wish can "
        "produce &mdash; rebirth among favored humans, then successively "
        "among six tiers of gods culminating in the Divinity's host "
        "&mdash; each following the identical mechanism of giving while "
        "expecting something back and then fixing the mind on a specific "
        "destination, though only for those of ethical conduct, and the "
        "highest tier requiring freedom from desire as well."),
    guide=[
        ("The teaching in one sentence", [
            "A gift given while expecting something back, combined with a "
            "settled, stabilized, developed wish for a specific rebirth, "
            "produces that very rebirth &mdash; running through eight "
            "successive tiers from favored human company up through six "
            "levels of gods to the Divinity's host &mdash; but only for "
            "the ethical, and the highest tier only for those free of "
            "desire as well."]),
        ("One mechanism, repeated eight times", [
            "Every one of the eight cases follows an identical three-step "
            "pattern: give expecting something back, hear of or see a "
            "particular kind of favorable existence, then settle on, "
            "stabilize, and develop the wish to be reborn there &mdash; the "
            "wish itself, not merely the gift, is what the discourse "
            "credits with producing the specific rebirth."]),
        ("Eight tiers, ascending", [
            "The destinies climb in sequence: favored human company first, "
            "then the gods of the four great kings, the gods of the "
            "thirty-three, the gods of Yama, the joyful gods, the gods who "
            "love to create, the gods who control what is created by "
            "others, and finally the Divinity's host &mdash; the same "
            "sequence of heavens this book has already met by name at AN "
            "8.36."]),
        ("A recurring refrain, and one added condition at the top", [
            "Each of the first seven cases closes with the identical "
            "refrain: this succeeds only for the ethical, not the "
            "unethical, because the heart's wish of an ethical person "
            "succeeds through their own purity. The eighth and highest "
            "case adds a further requirement found nowhere else in the "
            "list: success here belongs only to those free of desire, not "
            "those still governed by it."]),
    ],
    terms=[
        ("sāpekho dānaṁ deti",
         "&ldquo;gives expecting something back&rdquo; &mdash; the shared "
         "starting condition of all eight cases, distinguishing this "
         "discourse's giving from the disinterested motive named elsewhere "
         "in this chapter."),
        ("taṁ cittaṁ adhiṭṭhāti, taṁ cittaṁ vaḍḍheti",
         "&ldquo;they settle on that thought, stabilize it, and develop "
         "it&rdquo; &mdash; the mechanism the discourse credits with "
         "actually producing the specific rebirth wished for."),
        ("sīlavato taṁ hoti, no dussīlassa",
         "&ldquo;this is only for those of ethical conduct, not for the "
         "unethical&rdquo; &mdash; the refrain closing each of the first "
         "seven cases, a necessary condition throughout."),
        ("vītarāgassa, no sarāgassa",
         "&ldquo;for those free of desire, not those with desire&rdquo; "
         "&mdash; the additional condition attached only to the eighth and "
         "highest destination, the Divinity's host."),
        ("brahmakāyikānaṁ devānaṁ",
         "&ldquo;the gods of the Divinity's host&rdquo; &mdash; the "
         "eighth and highest destiny named, requiring both ethical purity "
         "and freedom from desire."),
    ],
    text_intro=(
        "The discourse in full: eight rebirth destinies, each following the "
        "same mechanism of a gift-giver's own settled wish. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Rebirth among favored humans"),
        ("p", "&sect;1", "an8.35:1.1-1.12"),
        ("h3", "Rebirth among the gods of the four great kings"),
        ("p", "&sect;2", "an8.35:2.1-2.9"),
        ("h3", "Rebirth among five further tiers of gods"),
        ("p", "&sect;3", "an8.35:3.1-3.13"),
        ("h3", "Rebirth among the Divinity's host"),
        ("p", "&sect;4", "an8.35:4.1-4.13"),
    ],
    quiz=[
        {"q": "What three-step mechanism runs through all eight cases in "
              "this discourse?",
         "opts": [
             "Giving anonymously, then forgetting about it entirely",
             "Giving while expecting something back, then settling on, "
             "stabilizing, and developing a wish for a specific rebirth",
             "Giving only to monastics, never to laypeople",
             "Giving once and never giving again"],
         "correct": 1,
         "expl": "The identical pattern repeated across all eight rebirth "
                 "tiers."},
        {"q": "What condition applies to all eight destinies alike?",
         "opts": [
             "Wealth is required in addition to giving",
             "Success belongs only to those of ethical conduct, not the "
             "unethical",
             "Only monastics can achieve any of the eight destinies",
             "No condition applies; the wish alone suffices"],
         "correct": 1,
         "expl": "A recurring refrain: the heart's wish of an ethical "
                 "person succeeds through their own purity."},
        {"q": "What additional condition applies only to the eighth and "
              "highest destination?",
         "opts": [
             "Extreme wealth", "Freedom from desire, not merely ethical "
                                "conduct",
             "Royal birth", "Advanced age"],
         "correct": 1,
         "expl": "The Divinity's host requires vītarāga, freedom from "
                 "desire, beyond the ethical purity required for the other "
                 "seven."},
        {"q": "What is the first of the eight destinies named?",
         "opts": [
             "The gods of the four great kings",
             "Rebirth among favored, well-to-do humans",
             "The Divinity's host directly",
             "The animal realm"],
         "correct": 1,
         "expl": "The lowest and first tier, before the sequence ascends "
                 "through six levels of gods."},
        {"q": "How does this discourse's list of heavens relate to AN 8.36, "
              "elsewhere in this chapter?",
         "opts": [
             "No relation at all",
             "It names the same sequence of heavenly tiers this book meets "
             "again by name at AN 8.36",
             "It directly contradicts AN 8.36",
             "AN 8.36 uses an entirely different cosmology"],
         "correct": 1,
         "expl": "The identical ascending sequence of heavens, met twice in "
                 "this chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("One mechanism, eight tiers", [
            "give expecting return,",
            "settle and stabilize the wish —",
            "the wish itself produces the rebirth",
        ]),
        ("Ascending through the heavens", [
            "humans, then four great kings,",
            "thirty-three, Yama, joyful,",
            "creating, controlling, and Brahmā's host",
        ]),
        ("Purity, and at the top, desirelessness", [
            "ethical conduct required",
            "throughout — but the highest tier",
            "demands freedom from desire too",
        ]),
        ("Cross-references", [
            "AN 8.34 &middot; previous, a field simile for fruitful giving",
            "AN 8.36 &middot; next, the same heavenly sequence named again "
            "through giving, ethics, and meditation together",
        ]),
    ],
    further=[
        '<a href="%s/an8.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.34.html">AN 8.34 &middot; A Field</a> &mdash; previous.',
        '<a href="an-8.36.html">AN 8.36 &middot; Grounds for Making Merit</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.36 — Puññakiriyavatthusutta
# --------------------------------------------------------------------------- #
page(
    36, "Puññakiriyavatthu", "Grounds for Making Merit",
    vagga=VAGGA_4,
    meta_title="AN 8.36 — Grounds for Making Merit | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Puññakiriyavatthusutta, on three grounds for making merit — "
        "giving, ethics, and meditation — and how varying degrees of the "
        "first two alone determine rebirth across seven ascending tiers, "
        "each ruled by a god who surpasses the rest in ten respects. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Three grounds named at the outset, then a graduated "
                 "sequence of degrees of practice mapped onto seven "
                 "successive rebirth tiers, compressed by internal "
                 "ellipsis across most of the middle tiers"),
        ("Length", "~2 minutes to read"),
        ("Three grounds, not eight", "Despite its place in the Book of the "
                                     "Eights, this discourse names only "
                                     "three grounds for making merit; the "
                                     "sevenfold tier structure that follows "
                                     "is a different count again, neither "
                                     "matching this book's numerical theme "
                                     "directly"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "repeating structure across seven tiers, with named "
                       "ruling gods worth tracking individually"),
    ],
    why=(
        "AN 8.36 names three grounds for making merit &mdash; giving, "
        "ethical conduct, and meditation &mdash; and traces what happens "
        "when someone practices only the first two, at varying degrees of "
        "intensity: a little produces rebirth among disadvantaged humans, a "
        "moderate amount among well-off humans, and an extraordinary "
        "degree among six successive tiers of gods, each tier ruled by a "
        "named deity who surpasses the others in ten respects."),
    guide=[
        ("The teaching in one sentence", [
            "Giving, ethical conduct, and meditation are the three grounds "
            "for making merit, and someone who practices only the first "
            "two &mdash; without reaching meditation &mdash; is reborn "
            "according to the degree of their practice: a little among "
            "disadvantaged humans, moderately among well-off humans, and "
            "at an extraordinary degree among any of six successive tiers "
            "of gods, ruled respectively by the four great kings, Sakka, "
            "Suyāma, Santusita, Sunimmita, and Vasavattī."]),
        ("What's conspicuously missing from every case", [
            "Every single rebirth this discourse describes &mdash; from "
            "disadvantaged human through the Divinity's near approach "
            "&mdash; shares one explicit qualifier: the person has not "
            "reached meditation as a ground for making merit. The "
            "discourse implicitly leaves open, without stating, what "
            "becomes possible once meditation is added to giving and "
            "ethics."]),
        ("Six god-kings, each surpassing their own realm", [
            "At the extraordinary-degree tier, the discourse names six "
            "named ruling gods in turn &mdash; the four great kings "
            "themselves, Sakka, the godling Suyāma, the godling Santusita, "
            "the godling Sunimmita, and the godling Vasavattī &mdash; each "
            "said to have practiced giving and ethical conduct to a "
            "greater degree than the other gods in their own realm, and "
            "each surpassing their fellow gods in the same ten respects: "
            "lifespan, beauty, happiness, glory, sovereignty, and the five "
            "sense objects."]),
        ("Compressed by the source's own internal ellipsis", [
            "Having spelled out the first ruling god's ten-respect "
            "superiority in full, the source text compresses the same "
            "formula for the remaining five gods &mdash; Sakka, Suyāma, "
            "Santusita, Sunimmita, and Vasavattī &mdash; trusting the "
            "reader to supply the identical ten respects each time."]),
    ],
    terms=[
        ("puññakiriyavatthūni",
         "&ldquo;grounds for making merit&rdquo; &mdash; this discourse's "
         "own title-phrase and its three named grounds: dāna, sīla, and "
         "bhāvanā."),
        ("dānamayaṁ puññakiriyavatthu, sīlamayaṁ puññakiriyavatthu",
         "&ldquo;giving as a ground for making merit, ethical conduct as a "
         "ground for making merit&rdquo; &mdash; the two grounds every "
         "rebirth in this discourse is based on, without the third, "
         "meditation."),
        ("dasahi ṭhānehi adhiggahetvā",
         "&ldquo;surpasses them in ten respects&rdquo; &mdash; the "
         "standing formula applied to each of the six named ruling gods, "
         "spelled out in full for the first and compressed for the "
         "remaining five."),
        ("āyunā vaṇṇena sukhena yasena ādhipateyyena",
         "&ldquo;lifespan, beauty, happiness, glory, sovereignty&rdquo; "
         "&mdash; the first five of the ten respects a ruling god surpasses "
         "others in, the second five being the five sense objects."),
        ("sakko devānamindo",
         "Sakka, lord of the gods, named here as the ruling deity of the "
         "gods of the thirty-three, the second of six named gods in this "
         "discourse's ascending sequence."),
    ],
    text_intro=(
        "The discourse in full: three grounds for making merit, and seven "
        "ascending rebirth tiers from giving and ethics alone. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three grounds for making merit"),
        ("p", "&sect;1", "an8.36:1.1-1.3"),
        ("h3", "Human rebirths, by degree of practice"),
        ("p", "&sect;2", "an8.36:2.1-3.2"),
        ("h3", "Six tiers of gods, each ruled by a named deity"),
        ("p", "&sect;3", "an8.36:4.1-9.5"),
    ],
    quiz=[
        {"q": "What three grounds for making merit does this discourse "
              "name?",
         "opts": [
             "Faith, wisdom, and effort",
             "Giving, ethical conduct, and meditation",
             "Study, devotion, and renunciation",
             "The five precepts alone"],
         "correct": 1,
         "expl": "Dāna, sīla, and bhāvanā — three grounds, not eight, "
                 "despite this discourse's place in the Book of the Eights."},
        {"q": "What is conspicuously absent from every rebirth this "
              "discourse describes?",
         "opts": [
             "Wealth", "Reaching meditation as a ground for making merit",
             "Family support", "Physical health"],
         "correct": 1,
         "expl": "Every case explicitly notes the person hasn't gotten as "
                 "far as meditation."},
        {"q": "What determines whether someone practicing only giving and "
              "ethics is reborn among disadvantaged humans, well-off "
              "humans, or among the gods?",
         "opts": [
             "Random chance",
             "The degree of their practice — a little, a moderate amount, "
             "or an extraordinary degree",
             "Their family's wealth alone",
             "The specific god they pray to"],
         "correct": 1,
         "expl": "A graduated scale, mapped onto ascending rebirth tiers."},
        {"q": "What do the six named ruling gods have in common?",
         "opts": [
             "Nothing in particular",
             "Each has practiced giving and ethical conduct to a greater "
             "degree than other gods in their realm, surpassing them in ten "
             "respects",
             "They are all enemies of each other",
             "They rule over hell realms"],
         "correct": 1,
         "expl": "The same ten-respect formula, spelled out once and "
                 "compressed for the remaining five gods."},
        {"q": "How does the source text handle the ten-respect formula "
              "after the first ruling god?",
         "opts": [
             "It restates it in full for every god",
             "It compresses it by internal ellipsis, trusting the reader to "
             "supply the same ten respects each time",
             "It omits it entirely for the remaining gods",
             "It replaces it with a different formula each time"],
         "correct": 1,
         "expl": "A self-abbreviation this project has met in similar form "
                 "elsewhere."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Three grounds, not eight", [
            "giving, ethics, meditation —",
            "only the first two here reach",
            "the various rebirth tiers described",
        ]),
        ("What's missing every time", [
            "'hasn't gotten as far as",
            "meditation' — repeated",
            "at every single tier",
        ]),
        ("Six god-kings, ten respects each", [
            "four kings, Sakka, Suyāma,",
            "Santusita, Sunimmita, Vasavattī —",
            "lifespan, beauty, glory, and more",
        ]),
        ("Cross-references", [
            "AN 8.35 &middot; previous, the same heavenly sequence reached "
            "through a giver's own settled wish",
            "AN 8.37 &middot; next, the eight gifts of a true person",
        ]),
    ],
    further=[
        '<a href="%s/an8.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.35.html">AN 8.35 &middot; Rebirth by Giving</a> &mdash; previous.',
        '<a href="an-8.37.html">AN 8.37 &middot; Gifts of a True Person</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.37 — Sappurisadānasutta
# --------------------------------------------------------------------------- #
page(
    37, "Sappurisadāna", "Gifts of a True Person",
    vagga=VAGGA_4,
    meta_title="AN 8.37 — Gifts of a True Person | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sappurisadānasutta, an eight-item list of qualities that mark a "
        "true person's own gift-giving, from purity and timeliness through "
        "confidence while giving and uplift afterward. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item prose list, immediately restated in "
                 "three verses"),
        ("Length", "under 1 minute to read"),
        ("Qualities of the act, not of the motive", "Unlike AN 8.31 and AN "
                                                     "8.33's catalogs of why "
                                                     "someone gives, this "
                                                     "discourse's eight "
                                                     "items describe how "
                                                     "the gift itself is "
                                                     "given and received "
                                                     "internally, including "
                                                     "two items about the "
                                                     "giver's own inner "
                                                     "state during and after "
                                                     "the act"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "prose followed by verse restatement"),
    ],
    why=(
        "AN 8.37 names eight qualities of a true person's gift &mdash; "
        "pure, good quality, timely, appropriate, intelligent, and "
        "regular, given with a confident heart, and followed by feeling "
        "uplifted afterward &mdash; describing the manner of giving and the "
        "giver's own inner state, not merely the motive behind it."),
    guide=[
        ("The teaching in one sentence", [
            "A true person's gift has eight qualities: it is pure, good "
            "quality, timely, appropriate, intelligent, and regular, given "
            "with a confident heart, and the giver feels uplifted "
            "afterward &mdash; six qualities of the gift itself and two of "
            "the giver's own inner state."]),
        ("Six qualities of the gift, two of the giver", [
            "The first six items in this list describe the gift as an "
            "object and an act &mdash; its purity, quality, timing, "
            "appropriateness to the recipient, thoughtfulness, and "
            "regularity. The final two shift entirely to the giver's own "
            "experience: confidence while giving, and feeling uplifted "
            "once the gift is given."]),
        ("A shift this chapter's other lists don't make", [
            "AN 8.31 and AN 8.33 both catalog motives &mdash; why someone "
            "gives. This discourse instead describes the texture of the "
            "giving itself and its emotional aftermath, a genuinely "
            "different axis of description than either of the earlier "
            "motive-catalogs in this chapter."]),
        ("Verses that restate the list without softening it", [
            "The closing verses don't add new content but compress the "
            "same eight qualities into poetic form, adding one further "
            "note: such giving is never regretted, and &ldquo;discerning "
            "people praise giving such gifts&rdquo; &mdash; a social as "
            "well as personal endorsement of the pattern just described."]),
    ],
    terms=[
        ("suci",
         "&ldquo;pure&rdquo; &mdash; the first quality named, describing "
         "the gift's own ethical or physical cleanliness."),
        ("kālena deti",
         "&ldquo;timely&rdquo; &mdash; the third quality, giving at the "
         "right moment rather than whenever convenient."),
        ("kappiyaṁ deti",
         "&ldquo;appropriate&rdquo; &mdash; the fourth quality, suited to "
         "the recipient rather than given without regard for fit."),
        ("pasannacitto deti",
         "&ldquo;while giving their heart is confident&rdquo; &mdash; the "
         "seventh quality, describing the giver's own inner state during "
         "the act itself, not merely its outward form."),
        ("datvā attamano hoti",
         "&ldquo;afterwards they're uplifted&rdquo; &mdash; the eighth and "
         "final quality, the giver's emotional aftermath once the gift has "
         "been made."),
    ],
    text_intro=(
        "The discourse in full: eight qualities of a true person's gift, in "
        "prose and then verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight qualities of a true person's gift"),
        ("p", "&sect;1", "an8.37:1.1-1.4"),
        ("h3", "The same eight, in verse"),
        ("p", "&sect;2", "an8.37:2.1-2.4"),
        ("p", "&sect;3", "an8.37:3.1-3.4"),
        ("p", "&sect;4", "an8.37:4.1-4.4"),
    ],
    quiz=[
        {"q": "How do this discourse's eight qualities differ from AN "
              "8.31's and AN 8.33's own eight-item lists?",
         "opts": [
             "They are identical lists",
             "This discourse describes the manner of giving and the "
             "giver's inner state, not the motive behind giving",
             "This discourse only describes wrong ways to give",
             "There is no meaningful difference"],
         "correct": 1,
         "expl": "A genuinely different axis of description than the "
                 "earlier motive-catalogs in this chapter."},
        {"q": "Which two qualities describe the giver's own inner state, "
              "rather than the gift itself?",
         "opts": [
             "Purity and good quality",
             "A confident heart while giving, and feeling uplifted "
             "afterward",
             "Timeliness and appropriateness",
             "Regularity and intelligence"],
         "correct": 1,
         "expl": "The seventh and eighth items, shifting from the object "
                 "given to the giver's own experience."},
        {"q": "What do the closing verses add beyond restating the eight "
              "qualities?",
         "opts": [
             "A warning against generosity",
             "That such giving is never regretted, and discerning people "
             "praise it",
             "A list of forbidden gifts",
             "Nothing further"],
         "correct": 1,
         "expl": "A social as well as personal endorsement of the pattern "
                 "described."},
        {"q": "What is the fourth quality named?",
         "opts": [
             "Wealth", "Appropriate — suited to the recipient",
             "Secrecy", "Publicity"],
         "correct": 1,
         "expl": "One of six qualities describing the gift itself, before "
                 "the list shifts to the giver's inner state."},
        {"q": "How is this discourse structured?",
         "opts": [
             "As a dialogue between two characters",
             "A bare prose list, immediately restated in verse",
             "As a long narrative", "As a set of monastic rules"],
         "correct": 1,
         "expl": "Prose followed by poetic restatement, similar in form to "
                 "AN 8.15's stains."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Six qualities of the gift", [
            "pure, good quality, timely,",
            "appropriate, intelligent,",
            "and given regularly",
        ]),
        ("Two of the giver's own heart", [
            "confident while giving —",
            "and uplifted afterward —",
            "the act's inner texture",
        ]),
        ("A different axis entirely", [
            "not why one gives,",
            "as AN 8.31, 8.33 asked,",
            "but how the giving itself feels",
        ]),
        ("Cross-references", [
            "AN 8.36 &middot; previous, three grounds for making merit and "
            "seven rebirth tiers",
            "AN 8.38 &middot; next, why a true person is born into a "
            "family at all",
        ]),
    ],
    further=[
        '<a href="%s/an8.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.36.html">AN 8.36 &middot; Grounds for Making Merit</a> &mdash; '
        "previous.",
        '<a href="an-8.38.html">AN 8.38 &middot; A True Person</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.38 — Sappurisasutta
# --------------------------------------------------------------------------- #
page(
    38, "Sappurisa", "A True Person",
    vagga=VAGGA_4,
    meta_title="AN 8.38 — A True Person | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sappurisasutta, comparing a true person born into a family to a "
        "great rain cloud that nourishes all crops, benefiting eight "
        "named groups from parents through ascetics and deities. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single extended simile — a true person compared to a "
                 "rain cloud — naming eight groups of beneficiaries, closing "
                 "in verse"),
        ("Length", "under 1 minute to read"),
        ("Eight beneficiaries, not eight qualities", "Where most of this "
                                                      "chapter's eight-item "
                                                      "lists name qualities "
                                                      "or motives, this "
                                                      "discourse's eight "
                                                      "items name who "
                                                      "benefits from a true "
                                                      "person's presence in "
                                                      "a family, a "
                                                      "different kind of "
                                                      "eightfold list"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "built around one clear image"),
    ],
    why=(
        "AN 8.38 compares a true person born into a family to a great rain "
        "cloud that nourishes every crop without distinction, naming eight "
        "groups who benefit from that person's presence: parents, children "
        "and partners, bondservants and staff, friends and colleagues, "
        "departed ancestors, the king, the deities, and ascetics and "
        "brahmins."),
    guide=[
        ("The teaching in one sentence", [
            "A true person is born into a family for the benefit, "
            "welfare, and happiness of eight groups of people &mdash; "
            "parents, children and partners, bondservants and staff, "
            "friends and colleagues, departed ancestors, the king, the "
            "deities, and ascetics and brahmins &mdash; just as a great "
            "rain cloud nourishes every crop for the benefit of all people."]),
        ("Eight beneficiaries, not eight qualities of the person", [
            "This discourse's eightfold structure works differently than "
            "most of this chapter's lists: rather than naming eight traits "
            "the true person has, it names eight distinct groups who "
            "receive benefit from that person's presence, radiating "
            "outward from the immediate family to servants, colleagues, the "
            "dead, the state, the divine, and the renunciate community."]),
        ("A rain cloud that doesn't discriminate", [
            "The simile's force lies in its indiscriminate reach: a great "
            "rain cloud nourishes every crop it falls on, not only the "
            "ones a farmer favors. A true person's benefit to their family "
            "and community is presented the same way &mdash; not targeted "
            "narrowly, but spread across every relationship the household "
            "touches."]),
        ("From the domestic to the cosmic, in one list", [
            "The eight beneficiaries move outward in scale: household "
            "relationships first (parents, children, partners, staff), "
            "then social relationships (friends, colleagues), then "
            "relationships that reach beyond the visible and the living "
            "entirely (departed ancestors, the king representing the "
            "state, the deities, and the ascetic and brahmin community)."]),
    ],
    terms=[
        ("sappuriso",
         "&ldquo;a true person&rdquo; &mdash; this discourse's own "
         "subject, the same term this chapter has already applied to "
         "figures like Hatthaka of Āḷavī."),
        ("mahāmegho",
         "&ldquo;a great rain cloud&rdquo; &mdash; the discourse's central "
         "simile, nourishing every crop without discrimination."),
        ("mātāpitūnaṁ, puttadārassa, dāsakammakaraporisassa",
         "&ldquo;mother and father; children and partners; bondservants, "
         "workers, and staff&rdquo; &mdash; the first three of the eight "
         "beneficiaries, the household's own immediate members."),
        ("petānaṁ, rañño, devatānaṁ",
         "&ldquo;departed ancestors; the king; the deities&rdquo; &mdash; "
         "three beneficiaries reaching beyond the living household into the "
         "dead, the state, and the divine."),
        ("samaṇabrāhmaṇānaṁ",
         "&ldquo;ascetics and brahmins&rdquo; &mdash; the eighth and final "
         "beneficiary named, closing the list with the renunciate and "
         "religious community."),
    ],
    text_intro=(
        "The discourse in full: a true person compared to a rain cloud, and "
        "the eight groups who benefit. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A true person, and eight beneficiaries"),
        ("p", "&sect;1", "an8.38:1.1-1.2"),
        ("h3", "The rain cloud simile"),
        ("p", "&sect;2", "an8.38:2.1-2.2"),
        ("h3", "Closing verses"),
        ("p", "&sect;3", "an8.38:3.1-6.4"),
    ],
    quiz=[
        {"q": "What does this discourse compare a true person born into a "
              "family to?",
         "opts": [
             "A well-tuned lute", "A great rain cloud that nourishes all "
                                   "crops",
             "A ship crossing the ocean", "A lamp in the dark"],
         "correct": 1,
         "expl": "An indiscriminate benefit, reaching every crop it falls "
                 "on."},
        {"q": "How does this discourse's eightfold structure differ from "
              "most of this chapter's other lists?",
         "opts": [
             "It is identical in structure to the others",
             "It names eight groups who benefit from the person's "
             "presence, rather than eight qualities that person has",
             "It has no eightfold structure at all",
             "It names eight ways to become wealthy"],
         "correct": 1,
         "expl": "A different kind of eightfold list — beneficiaries, not "
                 "traits."},
        {"q": "What three beneficiaries reach beyond the living household "
              "into the dead, the state, and the divine?",
         "opts": [
             "Wealth, fame, and status",
             "Departed ancestors, the king, and the deities",
             "Foreign kingdoms, rival clans, and enemies",
             "None; all eight beneficiaries are living household members"],
         "correct": 1,
         "expl": "Three of the eight beneficiaries reaching beyond the "
                 "visible and the living entirely."},
        {"q": "What closes the list of eight beneficiaries?",
         "opts": [
             "Wealthy merchants", "Ascetics and brahmins",
             "Foreign dignitaries", "Royal soldiers"],
         "correct": 1,
         "expl": "The renunciate and religious community, closing a list "
                 "that moves from domestic to cosmic scale."},
        {"q": "What quality of the rain cloud does the guide emphasize?",
         "opts": [
             "Its destructive power",
             "Its indiscriminate reach — nourishing every crop, not only "
             "favored ones",
             "Its rarity", "Its unpredictability"],
         "correct": 1,
         "expl": "The simile's force lies in benefit spread without "
                 "narrow targeting."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight who benefit", [
            "parents, children, partners,",
            "staff, friends, ancestors,",
            "the king, deities, ascetics",
        ]),
        ("A cloud that doesn't discriminate", [
            "nourishing every crop,",
            "not only the favored ones —",
            "benefit spread without narrowing",
        ]),
        ("From household to cosmic", [
            "immediate family first,",
            "then friends, then the dead,",
            "the state, the divine, the renunciate",
        ]),
        ("Cross-references", [
            "AN 8.37 &middot; previous, the eight qualities of a true "
            "person's own gift",
            "AN 8.39 &middot; next, eight kinds of overflowing merit",
        ]),
    ],
    further=[
        '<a href="%s/an8.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.37.html">AN 8.37 &middot; Gifts of a True Person</a> &mdash; previous.',
        '<a href="an-8.39.html">AN 8.39 &middot; Overflowing Merit</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.39 — Abhisandasutta
# --------------------------------------------------------------------------- #
page(
    39, "Abhisanda", "Overflowing Merit",
    vagga=VAGGA_4,
    meta_title="AN 8.39 — Overflowing Merit | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Abhisandasutta, on eight kinds of overflowing merit — three "
        "refuges plus the five precepts, each precept doubling as one of "
        "the five great, uncorrupted gifts. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Three refuges named first, then the five precepts, each "
                 "one doubly numbered as both a kind of overflowing merit "
                 "and one of five great, ancient gifts"),
        ("Length", "~2 minutes to read"),
        ("A double numbering, not an error", "The five precepts are each "
                                             "labeled twice within this "
                                             "single discourse — once as "
                                             "the fourth through eighth "
                                             "kinds of overflowing merit, "
                                             "and once, separately, as the "
                                             "first through fifth of five "
                                             "great gifts — an internal "
                                             "structure worth tracking "
                                             "rather than a textual "
                                             "inconsistency"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; two "
                       "numbering systems running simultaneously through "
                       "the same five items"),
    ],
    why=(
        "AN 8.39 names eight kinds of overflowing merit that nurture "
        "happiness and lead to heaven: going for refuge to the Buddha, the "
        "teaching, and the Saṅgha, and giving up killing, stealing, sexual "
        "misconduct, lying, and intoxicants &mdash; with each of the five "
        "precepts doubling as one of five great, primordial, uncorrupted "
        "gifts of freedom from fear to all beings."),
    guide=[
        ("The teaching in one sentence", [
            "Eight kinds of overflowing merit &mdash; refuge in the "
            "Buddha, the teaching, and the Saṅgha, and abstaining from "
            "killing, stealing, sexual misconduct, lying, and intoxicants "
            "&mdash; nurture happiness and lead to heaven, and each of the "
            "five precepts is also, in its own right, one of five great, "
            "primordial gifts of freedom from fear given to every sentient "
            "being."]),
        ("Three refuges, then five precepts", [
            "The first three kinds of overflowing merit are simply the "
            "three refuges, named individually rather than as a single "
            "combined act. The remaining five are the five precepts, each "
            "introduced with the same formula: a noble disciple gives up a "
            "specific form of harm."]),
        ("Two numbering systems in one discourse", [
            "Within the discourse's own text, each precept carries two "
            "separate labels: its place among the eight kinds of "
            "overflowing merit (fourth through eighth) and, independently, "
            "its place among five great gifts (first through fifth) that "
            "are &ldquo;primordial, long-standing, traditional, and "
            "ancient&rdquo; and that &ldquo;sensible ascetics and "
            "brahmins don't look down on&rdquo; &mdash; two different "
            "counts running through the identical five items."]),
        ("A gift given to every being, not just the recipient", [
            "What makes each precept a &ldquo;gift&rdquo; in this "
            "discourse's own terms is unusual: giving up killing, for "
            "instance, gives &ldquo;to countless sentient beings the gift "
            "of freedom from fear, enmity, and ill will&rdquo; &mdash; a "
            "gift not directed at any one recipient, but extended "
            "automatically to every being by the very act of restraint."]),
    ],
    terms=[
        ("puññābhisandā kusalābhisandā",
         "&ldquo;overflowing merit, overflowing goodness&rdquo; &mdash; "
         "this discourse's own title-phrase, describing merit that nurtures "
         "happiness and leads to heaven."),
        ("buddhe aveccappasādena samannāgato",
         "&ldquo;gone for refuge to the Buddha&rdquo; &mdash; the first of "
         "the eight kinds of overflowing merit, named individually rather "
         "than folded into a single triple-refuge act."),
        ("mahādānāni",
         "&ldquo;great gifts&rdquo; &mdash; the five precepts' own second "
         "identity within this discourse, described as primordial, "
         "long-standing, and never corrupted."),
        ("abhayaṁ dadāti averaṁ dadāti abyāpajjaṁ dadāti",
         "&ldquo;gives the gift of freedom from fear, enmity, and ill "
         "will&rdquo; &mdash; what each precept is said to give to "
         "countless sentient beings, not merely to withhold harm from any "
         "one recipient."),
        ("suramerayamajjapamādaṭṭhānā paṭivirato",
         "&ldquo;gives up beer, wine, and liquor intoxicants&rdquo; "
         "&mdash; the fifth precept and eighth kind of overflowing merit, "
         "closing both numbering systems in this discourse at once."),
    ],
    text_intro=(
        "The discourse in full: three refuges and five precepts, each "
        "precept doubly numbered as merit and as a great gift. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three refuges"),
        ("p", "&sect;1", "an8.39:1.1-3.2"),
        ("h3", "Giving up killing: merit and gift together"),
        ("p", "&sect;2", "an8.39:3.3-3.9"),
        ("h3", "Three further precepts, by internal ellipsis"),
        ("p", "&sect;3", "an8.39:4.1-6.2"),
        ("h3", "Giving up intoxicants, closing both numbering systems"),
        ("p", "&sect;4", "an8.39:7.1-8.1"),
    ],
    quiz=[
        {"q": "What are the first three kinds of overflowing merit named in "
              "this discourse?",
         "opts": [
             "The three poisons, negated",
             "The three refuges, named individually — Buddha, teaching, "
             "and Saṅgha",
             "Three types of meditation",
             "Three monastic robes"],
         "correct": 1,
         "expl": "Each refuge counted separately rather than as one "
                 "combined act."},
        {"q": "What double numbering does each of the five precepts carry "
              "within this discourse?",
         "opts": [
             "No double numbering; there is only one count",
             "A place among the eight kinds of overflowing merit (fourth "
             "through eighth), and separately, a place among five great "
             "gifts (first through fifth)",
             "Each precept is numbered three separate times",
             "The numbering is inconsistent and should be treated as an "
             "error"],
         "correct": 1,
         "expl": "Two distinct, deliberate numbering systems running "
                 "through the identical five items."},
        {"q": "What makes giving up killing a 'gift,' in this discourse's "
              "own terms?",
         "opts": [
             "It earns the giver material wealth",
             "It gives to countless sentient beings the gift of freedom "
             "from fear, enmity, and ill will — not directed at one "
             "recipient",
             "It is only a gift if performed publicly",
             "It isn't actually described as a gift"],
         "correct": 1,
         "expl": "A gift extended automatically to every being through the "
                 "act of restraint itself."},
        {"q": "How are the five great gifts described, distinct from being "
              "kinds of merit?",
         "opts": [
             "As modern innovations",
             "As primordial, long-standing, traditional, and ancient, never "
             "corrupted, and not looked down on by sensible ascetics and "
             "brahmins",
             "As optional and easily abandoned",
             "As applicable only to monastics"],
         "correct": 1,
         "expl": "A standing description distinguishing the 'great gift' "
                 "framing from the 'overflowing merit' framing."},
        {"q": "What is the eighth and final kind of overflowing merit?",
         "opts": [
             "Refuge in the Saṅgha", "Giving up beer, wine, and liquor "
                                      "intoxicants",
             "Giving up lying", "Giving up stealing"],
         "correct": 1,
         "expl": "The fifth precept, closing both numbering systems at "
                 "once."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in this "
                 "chapter."},
    ],
    marginalia=[
        ("Three refuges, five precepts", [
            "Buddha, teaching, Saṅgha —",
            "then abstaining from killing,",
            "stealing, misconduct, lying, drink",
        ]),
        ("Two counts, one list", [
            "fourth through eighth as merit —",
            "first through fifth as great gifts —",
            "the same five items, doubly numbered",
        ]),
        ("A gift to every being at once", [
            "not one recipient chosen,",
            "but freedom from fear given",
            "to countless beings by restraint alone",
        ]),
        ("Cross-references", [
            "AN 8.38 &middot; previous, a true person compared to a rain "
            "cloud",
            "AN 8.40 &middot; next, the results of misconduct, this "
            "discourse's own reversal",
        ]),
    ],
    further=[
        '<a href="%s/an8.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.38.html">AN 8.38 &middot; A True Person</a> &mdash; previous.',
        '<a href="an-8.40.html">AN 8.40 &middot; The Results of Misconduct</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.40 — Duccaritavipākasutta — closes ch.4 Dānavagga
# --------------------------------------------------------------------------- #
page(
    40, "Duccaritavipāka", "The Results of Misconduct",
    vagga=VAGGA_4,
    meta_title="AN 8.40 — The Results of Misconduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Duccaritavipākasutta, closing this chapter with eight kinds of "
        "misconduct, each leading to a bad rebirth at worst and a specific, "
        "pointed human consequence at minimum — AN 8.39's mirror image. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight parallel structures, each pairing a form of "
                 "misconduct with a bad-realm consequence and a distinct "
                 "minimum human consequence"),
        ("Length", "~2 minutes to read"),
        ("This chapter's reversal of AN 8.39", "Where AN 8.39 named five "
                                               "precepts as great gifts of "
                                               "fearlessness, this "
                                               "discourse closing the "
                                               "chapter names eight forms of "
                                               "misconduct — the same five "
                                               "precepts broken, plus three "
                                               "further verbal faults — each "
                                               "with its own specific, "
                                               "pointed consequence"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "repeating structure across eight items, each with a "
                       "distinct, specific human consequence worth reading "
                       "individually"),
    ],
    why=(
        "AN 8.40 closes this chapter by naming eight kinds of misconduct "
        "&mdash; killing, stealing, sexual misconduct, lying, backbiting, "
        "harsh speech, talking nonsense, and drinking alcohol &mdash; each "
        "leading at worst to hell, the animal realm, or the ghost realm, "
        "and at minimum to a specific, pointed human consequence distinct "
        "from all the others."),
    guide=[
        ("The teaching in one sentence", [
            "Each of eight kinds of misconduct, when cultivated, developed, "
            "and practiced, leads at worst to hell, the animal realm, or "
            "the ghost realm, and at minimum &mdash; even for someone "
            "reborn human &mdash; to a specific consequence distinct to "
            "that particular misconduct."]),
        ("Eight items, not the traditional ten", [
            "This list draws on the ten standard courses of unskillful "
            "action but reshapes them: it keeps seven bodily and verbal "
            "items &mdash; killing, stealing, sexual misconduct, lying, "
            "backbiting, harsh speech, and talking nonsense &mdash; and "
            "replaces the traditional three purely mental items "
            "(covetousness, ill will, wrong view) entirely with a single "
            "eighth item, drinking alcohol."]),
        ("A distinct minimum consequence for each", [
            "What distinguishes this discourse from a simple list is its "
            "specificity: killing's minimum human consequence is a short "
            "lifespan; stealing's is loss of wealth; sexual misconduct's is "
            "rivalry and enmity; lying's is false accusations; "
            "backbiting's is being divided against friends; harsh "
            "speech's is hearing disagreeable things; nonsense talk's is "
            "that no one takes what you say seriously; and drinking's is "
            "madness."]),
        ("A precise, almost poetic justice", [
            "Each pairing has an internal logic that isn't arbitrary: harsh "
            "speech returns as disagreeable things heard, nonsense talk "
            "returns as being disbelieved, backbiting returns as division "
            "from one's own friends &mdash; the consequence in each case "
            "mirrors the shape of the original misconduct rather than "
            "being a generic punishment."]),
    ],
    terms=[
        ("pāṇātipāto",
         "&ldquo;killing living creatures&rdquo; &mdash; the first "
         "misconduct named, whose minimum human consequence is a short "
         "lifespan."),
        ("pisuṇā vācā",
         "&ldquo;backbiting&rdquo; &mdash; the fifth item, whose minimum "
         "consequence, being divided against friends, mirrors the "
         "divisive nature of the original speech."),
        ("pharusā vācā",
         "&ldquo;harsh speech&rdquo; &mdash; the sixth item, whose minimum "
         "consequence is hearing disagreeable things oneself."),
        ("samphappalāpo",
         "&ldquo;talking nonsense&rdquo; &mdash; the seventh item, whose "
         "minimum consequence is that no one takes what you say seriously."),
        ("surāmerayapānaṁ",
         "&ldquo;drinking beer and wine&rdquo; &mdash; the eighth and "
         "closing item, replacing the traditional three mental unskillful "
         "actions, with madness as its minimum consequence."),
    ],
    text_intro=(
        "The discourse in full: eight kinds of misconduct, each with a "
        "distinct minimum human consequence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Killing, stealing, and sexual misconduct"),
        ("p", "&sect;1", "an8.40:1.1-3.2"),
        ("h3", "Lying, backbiting, and harsh speech"),
        ("p", "&sect;2", "an8.40:4.1-6.2"),
        ("h3", "Nonsense talk and drinking, closing this chapter"),
        ("p", "&sect;3", "an8.40:7.1-8.2"),
    ],
    quiz=[
        {"q": "How does this discourse's list of eight relate to the "
              "traditional ten courses of unskillful action?",
         "opts": [
             "It is identical to the traditional ten",
             "It keeps seven bodily and verbal items and replaces the three "
             "mental items entirely with a single eighth item, drinking "
             "alcohol",
             "It has nothing to do with the traditional ten",
             "It adds three new items to the traditional ten"],
         "correct": 1,
         "expl": "A reshaping that fits this book's eightfold theme rather "
                 "than the traditional count of ten."},
        {"q": "What is the minimum human consequence of backbiting, "
              "according to this discourse?",
         "opts": [
             "Physical illness",
             "Being divided against friends — mirroring the divisive "
             "nature of the original speech",
             "Loss of wealth",
             "A short lifespan"],
         "correct": 1,
         "expl": "A consequence that mirrors the shape of the original "
                 "misconduct, not a generic punishment."},
        {"q": "What is the minimum human consequence of talking nonsense?",
         "opts": [
             "Hearing disagreeable things",
             "That no one takes what you say seriously",
             "A short lifespan",
             "Rivalry and enmity"],
         "correct": 1,
         "expl": "A fittingly ironic consequence for habitual nonsense "
                 "talk."},
        {"q": "What does every one of the eight misconducts lead to at "
              "worst?",
         "opts": [
             "Nothing; only the minimum consequence applies",
             "Hell, the animal realm, or the ghost realm",
             "A short period of bad luck",
             "Social embarrassment only"],
         "correct": 1,
         "expl": "The severe end of the range, with the specific human "
                 "consequence as the minimum, not the worst case."},
        {"q": "How does this discourse relate to AN 8.39, immediately "
              "preceding it in this chapter?",
         "opts": [
             "No relation at all",
             "It functions as AN 8.39's mirror image — misconduct instead "
             "of the great gifts of restraint",
             "It repeats AN 8.39 word for word",
             "It contradicts AN 8.39's teaching entirely"],
         "correct": 1,
         "expl": "The same core precepts, viewed from their broken rather "
                 "than kept side, closing this chapter."},
        {"q": "What is the minimum human consequence of drinking alcohol, "
              "the eighth item?",
         "opts": [
             "Loss of wealth", "Madness",
             "False accusations", "Short lifespan"],
         "correct": 1,
         "expl": "The consequence closing both this discourse and this "
                 "chapter."},
    ],
    marginalia=[
        ("Eight misconducts, eight consequences", [
            "killing → short life,",
            "stealing → lost wealth,",
            "backbiting → divided friends",
        ]),
        ("A precise, mirrored justice", [
            "harsh speech returns as",
            "disagreeable things heard —",
            "nonsense talk, as disbelief",
        ]),
        ("This chapter's mirror image", [
            "AN 8.39's five great gifts,",
            "now shown from their broken side —",
            "plus three further verbal faults",
        ]),
        ("Cross-references", [
            "AN 8.39 &middot; previous, the five precepts as great gifts of "
            "fearlessness",
            "AN 8.31 &middot; earlier, opening this chapter's exploration "
            "of giving",
        ]),
    ],
    further=[
        '<a href="%s/an8.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.39.html">AN 8.39 &middot; Overflowing Merit</a> &mdash; previous.',
        '<a href="an-8.31.html">AN 8.31 &middot; Giving (1st)</a> &mdash; earlier, opening '
        "this chapter's exploration of giving.",
    ],
)


VAGGA_5 = "<em>Uposathavagga</em> &mdash; the fifth chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.41 — Saṅkhittūposathasutta — opens ch.5 Uposathavagga
# --------------------------------------------------------------------------- #
page(
    41, "Saṅkhittūposatha", "The Sabbath With Eight Factors, In Brief",
    vagga=VAGGA_5,
    meta_title="AN 8.41 — The Sabbath With Eight Factors, In Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Saṅkhittūposathasutta, opening a new chapter with the brief form "
        "of the lay eight-factored sabbath observance, each factor framed "
        "as a temporary vow to live for one day and night as the perfected "
        "ones live always. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "Eight factors, each given the identical three-part "
                 "reflection: how the perfected ones live permanently, how "
                 "the reflector will live for one day and night, and the "
                 "resolve that constitutes observing the sabbath"),
        ("Length", "~2 minutes to read"),
        ("A new chapter on lay observance", "This opens Uposathavagga, the "
                                            "Chapter on the Sabbath, giving "
                                            "the eight-factored lay "
                                            "observance in its shortest "
                                            "form before AN 8.42 expands it "
                                            "with an extended simile"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "clear, repeating structure across eight factors"),
    ],
    why=(
        "AN 8.41 gives the brief form of the eight-factored lay sabbath: a "
        "noble disciple reflects on how the perfected ones live permanently "
        "&mdash; giving up killing, stealing, unchastity, lying, "
        "intoxicants, eating after midday, entertainment and adornment, and "
        "luxurious beds &mdash; and resolves to live the same way for a "
        "single day and night, undertaking each factor as a temporary "
        "training."),
    guide=[
        ("The teaching in one sentence", [
            "The eight-factored sabbath, observed by reflecting on how the "
            "perfected ones live permanently and resolving to live the same "
            "way for a single day and night &mdash; giving up killing, "
            "stealing, unchastity, lying, intoxicants, eating after midday, "
            "entertainment and adornment, and luxurious beds &mdash; is "
            "very fruitful, beneficial, dazzling, and bountiful."]),
        ("A temporary vow modeled on a permanent one", [
            "Each of the eight factors follows an identical three-part "
            "pattern: first, how perfected ones live as long as they live; "
            "second, a personal resolve to live the same way, but only for "
            "this one day and night; third, the explicit naming of this as "
            "how the sabbath is observed with respect to that factor. The "
            "temporary vow is explicitly modeled on a permanent monastic "
            "standard, not invented separately for lay practice."]),
        ("Eight factors, in two registers", [
            "The first five factors overlap closely with the five "
            "precepts already met throughout this book, with the fifth "
            "precept's usual wording slightly adjusted. The remaining "
            "three &mdash; eating only before midday, giving up "
            "entertainment and adornment, and giving up luxurious beds "
            "&mdash; extend further into the register of monastic "
            "discipline, temporarily adopted by a layperson for a single "
            "day."]),
        ("Opening a new chapter with lay practice", [
            "Where the previous chapter explored giving, this new chapter "
            "turns to the sabbath observance itself &mdash; a periodic "
            "intensification of lay discipline that this chapter will "
            "explore from several angles: its brief form here, its "
            "detailed form and cosmic scale next, and its application to "
            "several named lay disciples in the discourses that follow."]),
    ],
    terms=[
        ("aṭṭhaṅgasamannāgato uposatho",
         "&ldquo;the sabbath with its eight factors&rdquo; &mdash; this "
         "discourse's own title-phrase and central subject."),
        ("yāvajīvaṁ arahanto",
         "&ldquo;as long as they live, the perfected ones&rdquo; &mdash; "
         "the opening formula of each factor's reflection, the permanent "
         "standard the temporary lay vow is modeled on."),
        ("imañca rattindivaṁ",
         "&ldquo;for this day and night&rdquo; &mdash; the temporal scope "
         "of the lay observance, distinguishing it explicitly from the "
         "permanent monastic standard it imitates."),
        ("vikālabhojanā paṭivirato",
         "&ldquo;abstaining from food at the wrong time&rdquo; &mdash; the "
         "sixth factor, eating only in one part of the day, extending "
         "beyond the five precepts into monastic-style discipline."),
        ("uccāsayanamahāsayanā paṭivirato",
         "&ldquo;giving up high and luxurious beds&rdquo; &mdash; the "
         "eighth and final factor, sleeping in a low place, a cot or "
         "straw mat."),
    ],
    text_intro=(
        "The discourse in full: the eight factors of the lay sabbath, each "
        "framed as a temporary vow. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the first factor"),
        ("p", "&sect;1", "an8.41:1.1-2.7"),
        ("h3", "The second through fourth factors"),
        ("p", "&sect;2", "an8.41:3.1-5.4"),
        ("h3", "The fifth and sixth factors"),
        ("p", "&sect;3", "an8.41:6.1-7.4"),
        ("h3", "The seventh and eighth factors"),
        ("p", "&sect;4", "an8.41:8.1-10.1"),
    ],
    quiz=[
        {"q": "What three-part pattern does each of the eight factors "
              "follow?",
         "opts": [
             "A prohibition, a punishment, and a warning",
             "How the perfected ones live permanently, a resolve to live "
             "the same way for one day and night, and naming this as the "
             "sabbath observance",
             "A story, a moral, and a summary",
             "A question, an answer, and a verse"],
         "correct": 1,
         "expl": "A temporary vow explicitly modeled on a permanent "
                 "monastic standard."},
        {"q": "How do the first five factors relate to material already met "
              "in this book?",
         "opts": [
             "They are entirely unrelated to anything met before",
             "They overlap closely with the five precepts, with the fifth "
             "slightly adjusted in wording",
             "They contradict the five precepts",
             "They apply only to monastics, never to laypeople"],
         "correct": 1,
         "expl": "A familiar ethical foundation, extended by three further "
                 "factors."},
        {"q": "What do the sixth, seventh, and eighth factors add beyond "
              "the five precepts?",
         "opts": [
             "Nothing further", "Eating only before midday, giving up "
                                 "entertainment and adornment, and giving "
                                 "up luxurious beds",
             "A vow of silence", "A vow never to travel"],
         "correct": 1,
         "expl": "Factors extending into monastic-style discipline, "
                 "temporarily adopted for a single day."},
        {"q": "How long is the sabbath vow undertaken for, in this "
              "discourse's own framing?",
         "opts": [
             "Permanently, for the rest of one's life",
             "For a single day and night",
             "For one month", "For one year"],
         "correct": 1,
         "expl": "A temporary practice, explicitly distinguished from the "
                 "permanent standard it's modeled on."},
        {"q": "What chapter does this discourse open?",
         "opts": [
             "Dānavagga, the Chapter on Giving",
             "Uposathavagga, the Chapter on the Sabbath",
             "Gahapativagga, the Chapter on Householders",
             "Rāgapeyyāla"],
         "correct": 1,
         "expl": "A new chapter turning from giving to periodic lay "
                 "discipline."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Vesālī, at the Great Wood",
             "Kapilavatthu, at the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "The standard opening setting, with the full narrative "
                 "frame."},
    ],
    marginalia=[
        ("Eight factors, one pattern", [
            "how perfected ones live always,",
            "a vow for one day and night,",
            "and the naming of the sabbath itself",
        ]),
        ("Five precepts, then three more", [
            "the familiar ethical base,",
            "extended into monastic register:",
            "midday eating, no adornment, low beds",
        ]),
        ("A new chapter opens", [
            "from giving to periodic",
            "intensification of practice —",
            "the sabbath, in its briefest form",
        ]),
        ("Cross-references", [
            "AN 8.40 &middot; earlier, closing the previous chapter",
            "AN 8.42 &middot; next, the same eight factors in full detail",
        ]),
    ],
    further=[
        '<a href="%s/an8.41/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.40.html">AN 8.40 &middot; The Results of Misconduct</a> &mdash; '
        "earlier, closing the previous chapter.",
        '<a href="an-8.42.html">AN 8.42 &middot; The Sabbath With Eight Factors, In '
        "Detail</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.42 — Vitthatūposathasutta
# --------------------------------------------------------------------------- #
page(
    42, "Vitthatūposatha", "The Sabbath With Eight Factors, In Detail",
    vagga=VAGGA_5,
    meta_title="AN 8.42 — The Sabbath With Eight Factors, In Detail | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Vitthatūposathasutta, expanding AN 8.41's brief sabbath with an "
        "extended comparison to a sixteen-kingdom empire, six ascending "
        "tiers of heavenly lifespan, and closing verses. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "AN 8.41's same eight factors, compressed by internal "
                 "ellipsis, followed by an extended comparison to imperial "
                 "wealth and six tiers of heavenly lifespan, closing in "
                 "verse"),
        ("Length", "~4 minutes to read"),
        ("The same six heavens, a fourth time in this nipāta", "This "
                                                                "discourse's "
                                                                "six-tier "
                                                                "heavenly "
                                                                "sequence "
                                                                "&mdash; "
                                                                "four great "
                                                                "kings, "
                                                                "thirty-"
                                                                "three, "
                                                                "Yama, "
                                                                "joyful, "
                                                                "creating, "
                                                                "controlling "
                                                                "&mdash; is "
                                                                "the same "
                                                                "sequence "
                                                                "already met "
                                                                "at AN 8.35 "
                                                                "and AN "
                                                                "8.36, now "
                                                                "with each "
                                                                "tier's "
                                                                "specific "
                                                                "heavenly "
                                                                "lifespan "
                                                                "given for "
                                                                "the first "
                                                                "time"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the "
                       "cosmological arithmetic in the middle section "
                       "rewards reading slowly"),
    ],
    why=(
        "AN 8.42 takes AN 8.41's eight-factored sabbath and, after "
        "compressing the factors themselves by ellipsis, expands their "
        "value dramatically: ruling all sixteen great countries with the "
        "seven kinds of precious things wouldn't be worth a sixteenth part "
        "of the sabbath, and the discourse then works through six "
        "successive tiers of gods, giving each tier's specific ratio of "
        "human to heavenly time and its total heavenly lifespan."),
    guide=[
        ("The teaching in one sentence", [
            "The eight-factored sabbath observed in full is worth more "
            "than ruling all sixteen great countries of the Buddha's world "
            "combined with all their wealth, because it can lead to "
            "rebirth among gods whose lifespans, measured in human years, "
            "reach into the tens of thousands."]),
        ("An empire, found wanting", [
            "The discourse names all sixteen great countries of its "
            "world by name &mdash; from Aṅga and Magadha through Gandhāra "
            "and Kamboja &mdash; and imagines ruling over every one of "
            "them, full of the seven kinds of precious things, only to "
            "declare this entire imperial wealth not worth a sixteenth "
            "part of the eight-factored sabbath."]),
        ("Six heavens, each with its own arithmetic", [
            "The discourse then works through six tiers of gods in "
            "ascending order, giving each one a specific conversion rate "
            "between human and heavenly time (fifty years to one divine "
            "day for the four great kings' realm, doubling at each "
            "successive tier up to sixteen hundred years for the highest) "
            "and a total heavenly lifespan calculated from that rate, from "
            "five hundred heavenly years up to sixteen thousand."]),
        ("The same six heavens, now with lifespans attached", [
            "This is the fourth time this nipāta has named this identical "
            "sequence of six heavenly tiers &mdash; after AN 8.35's giver's "
            "settled wish and AN 8.36's degrees of giving and ethics "
            "&mdash; but the first time their specific lifespans and time-"
            "ratios are given, turning what was elsewhere a bare "
            "sequence of names into a fully worked cosmology."]),
    ],
    terms=[
        ("soḷasannaṁ mahājanapadānaṁ",
         "&ldquo;these sixteen great countries&rdquo; &mdash; named in "
         "full, from Aṅga and Magadha through Gandhāra and Kamboja, the "
         "imperial scale the sabbath is measured against and found to "
         "exceed."),
        ("sattaratanasampannānaṁ",
         "&ldquo;full of the seven kinds of precious things&rdquo; "
         "&mdash; the wealth attributed to the imagined sixteen-country "
         "empire, still found wanting."),
        ("cātumahārājikānaṁ devānaṁ pañcasatāni dibbāni vassāni "
         "āyuppamāṇaṁ",
         "&ldquo;the lifespan of the gods of the four great kings is five "
         "hundred of these heavenly years&rdquo; &mdash; the first and "
         "lowest of six lifespan calculations given in ascending order."),
        ("paranimmitavasavattīnaṁ devānaṁ soḷasa vassasahassāni "
         "āyuppamāṇaṁ",
         "&ldquo;the life span of the gods who control what is created by "
         "others is sixteen thousand of these heavenly years&rdquo; "
         "&mdash; the sixth and highest lifespan given, closing the "
         "ascending sequence."),
        ("appakasmiṁ hi rajje mānussake",
         "&ldquo;human kingship is a poor thing&rdquo; &mdash; the "
         "discourse's own refrain, repeated after each of the six "
         "heavenly calculations, comparing human political power "
         "unfavorably to divine happiness."),
    ],
    text_intro=(
        "The discourse in full: the eight factors compressed, an imperial "
        "comparison, six heavenly lifespans, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The eight factors, and an empire found wanting"),
        ("p", "&sect;1", "an8.42:1.1-3.5"),
        ("h3", "Six heavens, each with its own arithmetic"),
        ("p", "&sect;2", "an8.42:4.1-9.7"),
        ("h3", "Closing verses"),
        ("p", "&sect;3", "an8.42:10.1-15.4"),
    ],
    quiz=[
        {"q": "What imperial comparison does this discourse make to "
              "measure the sabbath's worth?",
         "opts": [
             "Ruling a single small village",
             "Ruling all sixteen great countries of the Buddha's world, "
             "full of the seven kinds of precious things, still not worth "
             "a sixteenth part of the sabbath",
             "Owning a single precious gem",
             "No comparison is made"],
         "correct": 1,
         "expl": "The largest political and material scale this book "
                 "offers, still found wanting."},
        {"q": "How many tiers of gods does this discourse's cosmological "
              "sequence cover?",
         "opts": [
             "Three", "Six, from the four great kings up to the gods who "
                       "control what is created by others",
             "Twelve", "One"],
         "correct": 1,
         "expl": "The same six-tier sequence already met at AN 8.35 and AN "
                 "8.36, now with lifespans attached."},
        {"q": "What is given for each of the six heavenly tiers, for the "
              "first time in this nipāta?",
         "opts": [
             "Their location on a map",
             "A specific ratio of human to heavenly time and a total "
             "heavenly lifespan",
             "Their names alone, with no further detail",
             "A description of their physical appearance"],
         "correct": 1,
         "expl": "Bare sequence names elsewhere become a fully worked "
                 "cosmology here."},
        {"q": "What refrain repeats after each of the six heavenly "
              "calculations?",
         "opts": [
             "'This is impossible to verify'",
             "'Human kingship is a poor thing compared to the happiness of "
             "the gods'",
             "'This applies only to monastics'",
             "'None of this can be trusted'"],
         "correct": 1,
         "expl": "A comparison unfavorable to human political power, "
                 "repeated six times."},
        {"q": "How does this discourse handle AN 8.41's eight factors "
              "themselves?",
         "opts": [
             "It restates them in full a second time",
             "It compresses them by internal ellipsis before moving to the "
             "extended comparison",
             "It omits them entirely",
             "It replaces them with a different set of factors"],
         "correct": 1,
         "expl": "A self-abbreviation, trusting the reader to recall AN "
                 "8.41's fuller statement."},
        {"q": "What is the lifespan given for the highest of the six "
              "heavenly tiers?",
         "opts": [
             "Five hundred heavenly years",
             "Sixteen thousand heavenly years",
             "One thousand heavenly years",
             "Two thousand heavenly years"],
         "correct": 1,
         "expl": "The gods who control what is created by others, closing "
                 "the ascending sequence."},
    ],
    marginalia=[
        ("An empire, still found wanting", [
            "sixteen great countries,",
            "full of the seven treasures —",
            "not a sixteenth part of the sabbath",
        ]),
        ("Six heavens, worked in full", [
            "four kings, thirty-three, Yama,",
            "joyful, creating, controlling —",
            "now with lifespans, for the first time",
        ]),
        ("The fourth appearance of this sequence", [
            "after AN 8.35's settled wish,",
            "AN 8.36's degrees of practice —",
            "now the arithmetic itself",
        ]),
        ("Cross-references", [
            "AN 8.41 &middot; previous, the same eight factors in brief",
            "AN 8.43 &middot; next, the same detailed sabbath addressed to "
            "Visākhā",
        ]),
    ],
    further=[
        '<a href="%s/an8.42/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.41.html">AN 8.41 &middot; The Sabbath With Eight Factors, In '
        "Brief</a> &mdash; previous.",
        '<a href="an-8.43.html">AN 8.43 &middot; With Visākhā on the Sabbath</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.43 — Visākhūposathasutta
# --------------------------------------------------------------------------- #
page(
    43, "Visākhūposatha", "With Visākhā on the Sabbath",
    vagga=VAGGA_5,
    meta_title="AN 8.43 — With Visākhā on the Sabbath | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Visākhūposathasutta, addressing AN 8.42's detailed eight-factored "
        "sabbath directly to the great laywoman patron Visākhā, in her own "
        "residence, the stilt longhouse of Migāra's mother. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in the stilt longhouse of Migāra's mother in "
                    "the Eastern Monastery — Visākhā's own donated "
                    "residence"),
        ("Speakers", "The Buddha, addressing Visākhā directly"),
        ("Form", "The identical content as AN 8.42, addressed to a named "
                 "individual rather than to the mendicants generally"),
        ("Length", "~4 minutes to read"),
        ("Visākhā, this book's most prominent laywoman", "Visākhā, "
                                                          "Migāra's mother, "
                                                          "is one of the "
                                                          "tradition's most "
                                                          "celebrated lay "
                                                          "donors, and this "
                                                          "chapter will "
                                                          "return to her by "
                                                          "name in three "
                                                          "further "
                                                          "discourses"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to AN 8.42, best read as a "
                       "direct address rather than new material"),
    ],
    why=(
        "The Buddha addresses Visākhā, Migāra's mother, directly with the "
        "same detailed eight-factored sabbath and its cosmic-scale "
        "comparisons met at AN 8.42, personalizing a teaching already given "
        "generally to the mendicants."),
    guide=[
        ("The teaching in one sentence", [
            "Visākhā receives, addressed to her personally, the same "
            "eight-factored sabbath teaching AN 8.42 gave in general terms: "
            "an empire's wealth found wanting beside the sabbath, and six "
            "tiers of heavenly lifespan reachable through its observance."]),
        ("A teaching personalized, not altered", [
            "Nothing in the content changes between AN 8.42 and this "
            "discourse &mdash; the same sixteen countries, the same seven "
            "precious things, the same six heavens with the same "
            "lifespans. What changes is only the audience: a named "
            "individual, in her own residence, rather than the mendicants "
            "in general."]),
        ("Visākhā's own place in this book", [
            "This is the first of four discourses in this chapter "
            "addressed to Visākhā by name &mdash; here, and again at AN "
            "8.47 and AN 8.49, with AN 8.44 and AN 8.45 addressed to other "
            "named lay figures using closely related material. Her "
            "prominence in this cluster of discourses reflects her "
            "standing as one of the tradition's most celebrated lay "
            "donors."]),
        ("Setting as its own detail", [
            "The setting itself carries meaning: the stilt longhouse of "
            "Migāra's mother in the Eastern Monastery was Visākhā's own "
            "donation to the Saṅgha, so the Buddha teaches her this "
            "discourse on the eight-factored sabbath inside a building she "
            "herself provided."]),
    ],
    terms=[
        ("visākhā migāramātā",
         "Visākhā, Migāra's mother, the discourse's addressee and one of "
         "the tradition's most celebrated lay donors."),
        ("pubbārāme migāramātupāsāde",
         "&ldquo;the stilt longhouse of Migāra's mother in the Eastern "
         "Monastery&rdquo; &mdash; the setting, itself Visākhā's own gift "
         "to the Saṅgha."),
        ("aṭṭhaṅgasamannāgato uposatho",
         "&ldquo;the sabbath with its eight factors&rdquo; &mdash; the "
         "identical subject as AN 8.42, now addressed directly."),
        ("soḷasannaṁ mahājanapadānaṁ",
         "&ldquo;these sixteen great countries&rdquo; &mdash; the same "
         "imperial comparison met at AN 8.42, unchanged in this "
         "personalized address."),
        ("cātumahārājikānaṁ ... paranimmitavasavattīnaṁ",
         "the same six named tiers of gods, from the four great kings "
         "through the gods who control what is created by others, "
         "unchanged from AN 8.42."),
    ],
    text_intro=(
        "The discourse in full: the same detailed sabbath teaching as AN "
        "8.42, addressed directly to Visākhā. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the eight factors"),
        ("p", "&sect;1", "an8.43:1.1-3.5"),
        ("h3", "Six heavens, each with its own arithmetic"),
        ("p", "&sect;2", "an8.43:4.1-6.10"),
        ("h3", "Closing verses"),
        ("p", "&sect;3", "an8.43:7.1-12.4"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 8.42's?",
         "opts": [
             "Entirely different content",
             "Identical content, addressed directly to Visākhā rather than "
             "to the mendicants generally",
             "A shortened summary of AN 8.42",
             "An expanded version with new material"],
         "correct": 1,
         "expl": "A teaching personalized in audience, not altered in "
                 "content."},
        {"q": "Who is Visākhā, addressed in this discourse?",
         "opts": [
             "A queen ruling one of the sixteen great countries",
             "One of the tradition's most celebrated lay donors, Migāra's "
             "mother",
             "A rival ascetic teacher",
             "A member of the monastic Saṅgha"],
         "correct": 1,
         "expl": "A prominent laywoman this chapter addresses by name in "
                 "several further discourses."},
        {"q": "What is significant about this discourse's setting, "
              "according to the guide?",
         "opts": [
             "It has no particular significance",
             "The stilt longhouse of Migāra's mother was Visākhā's own "
             "donation to the Saṅgha",
             "It is the same location as AN 8.7's Devadatta discourse",
             "It is Visākhā's birthplace"],
         "correct": 1,
         "expl": "The Buddha teaches Visākhā inside a building she herself "
                 "provided."},
        {"q": "How many discourses in this chapter address Visākhā by "
              "name?",
         "opts": [
             "None besides this one",
             "Four, including this one, at AN 8.43, 8.47, and 8.49",
             "Ten", "One hundred"],
         "correct": 1,
         "expl": "A recurring addressee across this chapter, reflecting her "
                 "prominence."},
        {"q": "What imperial comparison appears in this discourse, "
              "unchanged from AN 8.42?",
         "opts": [
             "A single small village",
             "Ruling all sixteen great countries, full of the seven "
             "precious things, still not worth a sixteenth part of the "
             "sabbath",
             "A single precious gem",
             "No comparison appears"],
         "correct": 1,
         "expl": "The identical comparison, now addressed to Visākhā "
                 "personally."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in the stilt longhouse of Migāra's mother in the "
             "Eastern Monastery",
             "Vesālī, at the Great Wood",
             "Kapilavatthu, at the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "Visākhā's own donated residence."},
    ],
    marginalia=[
        ("The same teaching, personalized", [
            "identical content as 8.42 —",
            "addressed now to Visākhā",
            "by name, in her own residence",
        ]),
        ("A gift returned as teaching", [
            "the longhouse she donated",
            "becomes the very place",
            "she receives this discourse",
        ]),
        ("A recurring addressee", [
            "Visākhā appears again",
            "at 8.47, 8.49 —",
            "this chapter's most-named laywoman",
        ]),
        ("Cross-references", [
            "AN 8.42 &middot; previous, the same teaching addressed "
            "generally",
            "AN 8.44 &middot; next, the layman Vāseṭṭha's own reflection "
            "on this same sabbath",
        ]),
    ],
    further=[
        '<a href="%s/an8.43/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.42.html">AN 8.42 &middot; The Sabbath With Eight Factors, In '
        "Detail</a> &mdash; previous.",
        '<a href="an-8.44.html">AN 8.44 &middot; With Vāseṭṭha on the Sabbath</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.44 — Vāseṭṭhūposathasutta
# --------------------------------------------------------------------------- #
page(
    44, "Vāseṭṭhūposatha", "With Vāseṭṭha on the Sabbath",
    vagga=VAGGA_5,
    meta_title="AN 8.44 — With Vāseṭṭha on the Sabbath | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Vāseṭṭhūposathasutta, in which the layman Vāseṭṭha's own response "
        "to the sabbath teaching escalates from his family to all four "
        "castes to the entire world, with the Buddha extending it even "
        "further to sentient trees. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with the peaked "
                    "roof"),
        ("Speakers", "The layman Vāseṭṭha and the Buddha"),
        ("Form", "The sabbath teaching heavily compressed by ellipsis, "
                 "followed by Vāseṭṭha's own escalating reflection and the "
                 "Buddha's confirmation, extended even further"),
        ("Length", "~1 minute to read"),
        ("The shortest of this chapter's sabbath discourses", "Where AN "
                                                               "8.42 and AN "
                                                               "8.43 spell "
                                                               "out the full "
                                                               "sabbath "
                                                               "teaching, "
                                                               "this "
                                                               "discourse "
                                                               "compresses "
                                                               "nearly all "
                                                               "of it, "
                                                               "giving its "
                                                               "real "
                                                               "attention "
                                                               "instead to "
                                                               "Vāseṭṭha's "
                                                               "own "
                                                               "escalating "
                                                               "response"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "with a memorable escalating structure in its second "
                       "half"),
    ],
    why=(
        "After the Buddha gives the eight-factored sabbath teaching to the "
        "layman Vāseṭṭha in heavily compressed form, Vāseṭṭha responds by "
        "wishing it first for his own relatives, then for all four castes, "
        "prompting the Buddha to confirm and extend the wish even further "
        "&mdash; to the whole world with its gods and humans, and even, "
        "hypothetically, to sentient trees."),
    guide=[
        ("The teaching in one sentence", [
            "If Vāseṭṭha's relatives observed the eight-factored sabbath "
            "it would be for their lasting welfare and happiness; the "
            "Buddha confirms this and extends it further, to all castes, "
            "to the whole world of gods and humans, and even, "
            "hypothetically, to sentient trees."]),
        ("The sabbath teaching itself, barely stated", [
            "Unusually for this cluster of sabbath discourses, this one "
            "compresses the actual eight-factored teaching almost "
            "entirely, jumping straight from the Buddha's opening "
            "statement to its closing line via ellipsis. The discourse's "
            "real interest lies not in restating the factors again but in "
            "what happens next."]),
        ("An escalation, moving outward from family", [
            "Vāseṭṭha's own response builds in three steps: first his "
            "immediate relatives and kin, then all four castes &mdash; "
            "aristocrats, brahmins, peasants, and menials &mdash; named "
            "explicitly rather than left implicit. Each step widens the "
            "circle of who might benefit from the sabbath's observance."]),
        ("The Buddha's confirmation, and a striking extension", [
            "Rather than simply agreeing, the Buddha extends Vāseṭṭha's "
            "own escalation even further: to the whole world with its "
            "gods, Māras, and divinities, and then &mdash; in a "
            "deliberately impossible hypothetical &mdash; even to the "
            "great sal trees themselves, if they were sentient, closing "
            "with the a fortiori conclusion: how much more, then, a human "
            "being."]),
    ],
    terms=[
        ("vāseṭṭho gahapati",
         "the layman Vāseṭṭha, whose own reflection on the sabbath "
         "teaching's reach is this discourse's real subject."),
        ("ñātisālohitā",
         "&ldquo;relatives and kin&rdquo; &mdash; the first and narrowest "
         "circle Vāseṭṭha wishes the sabbath's benefit for."),
        ("khattiyā ... brāhmaṇā ... vessā ... suddā",
         "&ldquo;aristocrats, brahmins, peasants, and menials&rdquo; "
         "&mdash; the four traditional castes, named explicitly as the "
         "second and wider circle of Vāseṭṭha's wish."),
        ("sadevako loko samārako sabrahmako sassamaṇabrāhmaṇī pajā "
         "sadevamanussā",
         "&ldquo;the whole world&mdash;with its gods, Māras, and "
         "divinities, this population with its ascetics and brahmins, "
         "gods and humans&rdquo; &mdash; the Buddha's own further "
         "extension, beyond even Vāseṭṭha's four castes."),
        ("sace sattā abhavissaṁsu",
         "&ldquo;if they were sentient&rdquo; &mdash; the deliberately "
         "impossible hypothetical applied to the great sal trees, closing "
         "the discourse's escalation with an a fortiori argument for "
         "human beings."),
    ],
    text_intro=(
        "The discourse in full: the sabbath teaching compressed, and "
        "Vāseṭṭha's own escalating reflection. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the sabbath teaching, compressed"),
        ("p", "&sect;1", "an8.44:1.1-1.4"),
        ("h3", "Vāseṭṭha's escalating reflection, and the Buddha's answer"),
        ("p", "&sect;2", "an8.44:2.1-3.5"),
    ],
    quiz=[
        {"q": "How does this discourse treat the actual eight-factored "
              "sabbath teaching, compared to AN 8.42 and AN 8.43?",
         "opts": [
             "It restates the teaching in even greater detail",
             "It compresses the teaching almost entirely by ellipsis, "
             "focusing instead on what follows",
             "It omits the teaching entirely with no mention",
             "It contradicts the earlier teaching"],
         "correct": 1,
         "expl": "The shortest of this chapter's sabbath discourses, with "
                 "its real attention elsewhere."},
        {"q": "What three steps does Vāseṭṭha's own reflection move "
              "through?",
         "opts": [
             "Himself alone, then his village, then the entire universe",
             "His relatives and kin, then all four castes explicitly "
             "named, prompting the Buddha's further extension",
             "Only his immediate family, with no further extension",
             "A single step with no escalation at all"],
         "correct": 1,
         "expl": "A widening circle, extended even further by the Buddha's "
                 "own response."},
        {"q": "How far does the Buddha's own extension of Vāseṭṭha's wish "
              "reach?",
         "opts": [
             "No further than the four castes",
             "The whole world with its gods and humans, and even, "
             "hypothetically, the great sal trees, if they were sentient",
             "Only to the mendicant Saṅgha",
             "Only to Vāseṭṭha's own household"],
         "correct": 1,
         "expl": "An a fortiori argument, closing with 'how much more then "
                 "a human being.'"},
        {"q": "What four castes does Vāseṭṭha name explicitly?",
         "opts": [
             "Farmers, merchants, soldiers, and priests",
             "Aristocrats, brahmins, peasants, and menials",
             "Kings, queens, princes, and princesses",
             "Ascetics, brahmins, laymen, and laywomen"],
         "correct": 1,
         "expl": "The traditional fourfold caste division, named as the "
                 "second, wider circle of his wish."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in the stilt longhouse of Migāra's mother",
             "Vesālī, at the Great Wood, in the hall with the peaked roof",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, at the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "A setting shared with several other discourses in this "
                 "book, including AN 8.12."},
        {"q": "What rhetorical device closes the discourse?",
         "opts": [
             "A simple restatement",
             "An a fortiori argument — if even hypothetically sentient "
             "trees would benefit, how much more a human being",
             "A direct contradiction of Vāseṭṭha",
             "A refusal to answer"],
         "correct": 1,
         "expl": "The Buddha's own rhetorical extension, closing the "
                 "discourse."},
    ],
    marginalia=[
        ("The teaching barely stated", [
            "compressed almost entirely —",
            "this discourse's real interest",
            "lies in what comes after",
        ]),
        ("An escalation outward", [
            "relatives, then all castes,",
            "then the whole world of beings,",
            "then even sentient trees",
        ]),
        ("How much more, a human being", [
            "if trees, hypothetically,",
            "would benefit from the sabbath —",
            "the Buddha's own closing argument",
        ]),
        ("Cross-references", [
            "AN 8.43 &middot; previous, the full sabbath teaching addressed "
            "to Visākhā",
            "AN 8.45 &middot; next, the same teaching addressed to the "
            "laywoman Bojjhā",
        ]),
    ],
    further=[
        '<a href="%s/an8.44/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.43.html">AN 8.43 &middot; With Visākhā on the Sabbath</a> &mdash; '
        "previous.",
        '<a href="an-8.45.html">AN 8.45 &middot; With Bojjhā on the Sabbath</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.45 — Bojjhūposathasutta
# --------------------------------------------------------------------------- #
page(
    45, "Bojjhūposatha", "With Bojjhā on the Sabbath",
    vagga=VAGGA_5,
    meta_title="AN 8.45 — With Bojjhā on the Sabbath | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Bojjhūposathasutta, the detailed sabbath teaching addressed to "
        "the laywoman Bojjhā, closing with a line whose English translation "
        "diverges from the identical Pāli given at AN 8.42 and 8.43 — "
        "noted honestly rather than silently corrected. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery"),
        ("Speakers", "The Buddha, addressing the laywoman Bojjhā directly"),
        ("Form", "The same detailed sabbath teaching as AN 8.42 and 8.43, "
                 "addressed to a third named individual"),
        ("Length", "~4 minutes to read"),
        ("A translation discrepancy, noted honestly", "This discourse's "
                                                       "closing verse "
                                                       "compares the "
                                                       "sabbath's worth to "
                                                       "royal wealth in "
                                                       "Pāli identical to "
                                                       "AN 8.42 and 8.43, "
                                                       "but the English "
                                                       "translation in the "
                                                       "source data reads "
                                                       "&ldquo;the mind "
                                                       "developed with "
                                                       "love&rdquo; instead "
                                                       "&mdash; almost "
                                                       "certainly carried "
                                                       "over from AN 8.1's "
                                                       "own verse, and "
                                                       "presented here as "
                                                       "found rather than "
                                                       "silently corrected"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to AN 8.42 and 8.43, worth "
                       "reading for its one genuine textual anomaly"),
    ],
    why=(
        "The Buddha addresses the laywoman Bojjhā with the same detailed "
        "eight-factored sabbath teaching given to Visākhā at AN 8.43, "
        "though the closing verses in this discourse's English translation "
        "contain a small, apparently inherited discrepancy worth noting "
        "rather than silently smoothing over."),
    guide=[
        ("The teaching in one sentence", [
            "Bojjhā receives the same detailed sabbath teaching as "
            "Visākhā at AN 8.43 &mdash; the sixteen-country comparison and "
            "the six ascending tiers of heavenly lifespan &mdash; word for "
            "word, in Pāli, even where the English translation of one "
            "closing line appears to diverge."]),
        ("A third named laywoman", [
            "Where AN 8.43 addressed Visākhā and AN 8.44 addressed the "
            "layman Vāseṭṭha, this discourse turns to a third figure, the "
            "laywoman Bojjhā, otherwise little known elsewhere in this "
            "collection, receiving the identical detailed teaching in the "
            "familiar setting of Jeta's Grove."]),
        ("A line that doesn't quite match its own source", [
            "Checking the root Pāli against the English translation "
            "reveals something worth flagging honestly: the line "
            "translated elsewhere (AN 8.42, AN 8.43) as &ldquo;not worth a "
            "sixteenth part of the sabbath with its eight factors&rdquo; "
            "appears in this discourse's English rendering as &ldquo;not "
            "worth a sixteenth part of the mind developed with love&rdquo; "
            "&mdash; even though the underlying Pāli line is word-for-word "
            "identical to AN 8.42 and 8.43's own."]),
        ("Presented as found, not silently corrected", [
            "This project pulls its text directly from the source "
            "translation data without hand-editing, and this small "
            "discrepancy is presented the same way: as an observed "
            "anomaly, almost certainly an accidental carryover from AN "
            "8.1's own verse about a mind developed with love, rather than "
            "a deliberate variant reading, but reported honestly rather "
            "than quietly fixed."]),
    ],
    terms=[
        ("bojjhā upāsikā",
         "the laywoman Bojjhā, this discourse's addressee, otherwise "
         "little known elsewhere in this collection."),
        ("aṭṭhaṅgasamannāgato uposatho",
         "&ldquo;the sabbath with its eight factors&rdquo; &mdash; the "
         "same subject as AN 8.42 and 8.43, unchanged in content here."),
        ("kalampi te nānubhavanti soḷasiṁ",
         "&ldquo;they're not worth a sixteenth part&rdquo; &mdash; the "
         "Pāli line identical across AN 8.42, 8.43, and this discourse, "
         "though its English translation here reads differently."),
        ("mettāya cittaṁ bhāvitaṁ",
         "&ldquo;a mind developed with love&rdquo; &mdash; the phrase this "
         "discourse's own English translation supplies at the point where "
         "AN 8.42 and 8.43 both read &ldquo;the sabbath with its eight "
         "factors,&rdquo; an apparent carryover from AN 8.1."),
        ("cātumahārājikānaṁ ... paranimmitavasavattīnaṁ",
         "the same six named tiers of gods met at AN 8.42 and 8.43, "
         "unchanged in this discourse."),
    ],
    text_intro=(
        "The discourse in full: the same detailed sabbath teaching as AN "
        "8.42 and 8.43, addressed to Bojjhā, with one closing line "
        "presented as found in the source translation. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the eight factors"),
        ("p", "&sect;1", "an8.45:1.1-4.5"),
        ("h3", "Six heavens, each with its own arithmetic"),
        ("p", "&sect;2", "an8.45:5.1-6.11"),
        ("h3", "Closing verses"),
        ("p", "&sect;3", "an8.45:7.1-12.4"),
    ],
    quiz=[
        {"q": "Who is addressed in this discourse?",
         "opts": [
             "Visākhā, Migāra's mother", "The laywoman Bojjhā",
             "The layman Vāseṭṭha", "Venerable Anuruddha"],
         "correct": 1,
         "expl": "A third named lay figure in this chapter's sabbath "
                 "cluster."},
        {"q": "What discrepancy does the guide flag in this discourse's "
              "closing verses?",
         "opts": [
             "A missing paragraph",
             "The English translation reads 'the mind developed with love' "
             "at a point where the identical Pāli matches AN 8.42 and "
             "8.43's 'the sabbath with its eight factors'",
             "A different setting than stated",
             "A missing quiz question"],
         "correct": 1,
         "expl": "A small, apparently inherited discrepancy in the source "
                 "translation data."},
        {"q": "How does the guide handle this discrepancy?",
         "opts": [
             "By silently correcting the translation to match AN 8.42",
             "By noting it honestly as an observed anomaly, likely carried "
             "over from AN 8.1, without silently fixing it",
             "By ignoring it entirely",
             "By claiming it as a deliberate variant reading with certainty"],
         "correct": 1,
         "expl": "Presented as found, consistent with this project's "
                 "practice of not hand-editing source text."},
        {"q": "How does the rest of this discourse's content compare to AN "
              "8.43?",
         "opts": [
             "Entirely different",
             "The same detailed sabbath teaching — sixteen countries, six "
             "heavenly tiers — addressed to a different named individual",
             "A much shorter summary",
             "Contradictory in its core teaching"],
         "correct": 1,
         "expl": "Identical core content, personalized to a third "
                 "addressee."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Vesālī, at the Great Wood",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Rājagaha, on Vulture's Peak",
             "Kapilavatthu, at the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "The familiar opening setting shared with many discourses "
                 "in this book."},
        {"q": "What is likely the true source of the discrepant line, "
              "according to the guide?",
         "opts": [
             "A deliberate doctrinal revision",
             "An accidental carryover from AN 8.1's own verse about a mind "
             "developed with love",
             "A scribal error unique to this discourse with no clear "
             "origin",
             "An intentional cross-reference"],
         "correct": 1,
         "expl": "A plausible but not certain explanation, offered "
                 "honestly rather than asserted as fact."},
    ],
    marginalia=[
        ("A third named laywoman", [
            "after Visākhā, Vāseṭṭha —",
            "Bojjhā receives the same",
            "detailed sabbath teaching",
        ]),
        ("A line that doesn't quite match", [
            "identical Pāli, but the English",
            "reads 'mind developed with love' —",
            "likely carried over from AN 8.1",
        ]),
        ("Reported, not corrected", [
            "this project pulls text as found —",
            "the anomaly noted honestly,",
            "not silently smoothed over",
        ]),
        ("Cross-references", [
            "AN 8.44 &middot; previous, Vāseṭṭha's own escalating "
            "reflection",
            "AN 8.1 &middot; earlier, the likely source of this "
            "discourse's discrepant closing line",
        ]),
    ],
    further=[
        '<a href="%s/an8.45/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.44.html">AN 8.44 &middot; With Vāseṭṭha on the Sabbath</a> &mdash; '
        "previous.",
        '<a href="an-8.1.html">AN 8.1 &middot; The Benefits of Love</a> &mdash; earlier, the '
        "likely source of this discourse's discrepant line.",
        '<a href="an-8.46.html">AN 8.46 &middot; Anuruddha and the Agreeable Deities</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.46 — Anuruddhasutta -- note: this is a DIFFERENT discourse from
# an-8.30.html's own Pāli title (Anuruddhamahāvitakkasutta names AN 8.30's
# "great thoughts" discourse); this discourse's own Pāli title is the
# shorter Anuruddhasutta. Content here is a candid, patriarchal-household
# teaching on a wife's duties; presented honestly per this project's
# AN4.80/AN7.63 precedent, without softening or endorsing.
# --------------------------------------------------------------------------- #
page(
    46, "Anuruddha", "Anuruddha and the Agreeable Deities",
    vagga=VAGGA_5,
    meta_title="AN 8.46 — Anuruddha and the Agreeable Deities | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Anuruddhasutta, opening with deities displaying their powers "
        "to Venerable Anuruddha and vanishing in embarrassment when he "
        "stays unmoved, then turning to eight qualities the source "
        "attributes to a wife securing rebirth among those very gods — "
        "presented honestly, without softening its patriarchal framing. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Kosambī, in Ghosita's Monastery"),
        ("Speakers", "Deities of the Agreeable Host, Venerable Anuruddha, "
                     "and the Buddha"),
        ("Form", "A narrative of deities displaying psychic power and "
                 "vanishing in embarrassment, followed by the Buddha's own "
                 "answer to Anuruddha's resulting question, in prose and "
                 "verse"),
        ("Length", "~3 minutes to read"),
        ("Candid, patriarchal household content", "The eight qualities "
                                                   "named here describe a "
                                                   "wife's deference and "
                                                   "duty toward her "
                                                   "husband within an "
                                                   "ancient household "
                                                   "structure; this reading "
                                                   "guide presents the text "
                                                   "as it stands, following "
                                                   "this project's practice "
                                                   "elsewhere (AN 4.80, AN "
                                                   "7.63) of not softening "
                                                   "or endorsing difficult "
                                                   "historical material"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "charming narrative opening, followed by content "
                       "that asks careful, honest reading"),
    ],
    why=(
        "Deities of the Agreeable Host visit Venerable Anuruddha in "
        "meditation, showing off their power to change color, voice, and "
        "pleasure at will, and perform music and dance for him &mdash; but "
        "vanish in embarrassment when he stays unmoved; asking the Buddha "
        "afterward what leads women to be reborn among such gods, "
        "Anuruddha receives an answer built entirely around eight qualities "
        "of deference and duty within marriage."),
    guide=[
        ("The teaching in one sentence", [
            "According to this discourse, a wife who honors her husband's "
            "wishes in household management, defers to those he respects, "
            "safeguards his wealth, and adds faith, ethics, and generosity "
            "of her own is, on this account, reborn among the Agreeable "
            "Host of gods &mdash; the very deities who visited Anuruddha at "
            "this discourse's opening."]),
        ("A narrative of unmoved equanimity", [
            "The discourse opens with something genuinely striking: "
            "deities who can turn any color, produce any voice, and "
            "conjure any pleasure at will perform an irresistible show for "
            "Anuruddha, described as graceful, tantalizing, and "
            "intoxicating &mdash; and he simply averts his senses. Finding "
            "themselves unable to move him, the deities vanish in what the "
            "text frames as embarrassment."]),
        ("Eight qualities, read honestly", [
            "Anuruddha's resulting question to the Buddha &mdash; what "
            "leads women to be reborn among these gods &mdash; receives an "
            "answer built around eight qualities: deference to a husband's "
            "schedule and wishes, honoring whoever he honors, skill and "
            "diligence in domestic management, fair oversight of "
            "household staff, careful guarding of his income, and three "
            "further qualities &mdash; refuge, ethical conduct, and "
            "generosity &mdash; shared with the ethical ideals taught "
            "elsewhere in this book to men and women alike. This reading "
            "guide states the content plainly rather than reframing it as "
            "timeless or universal advice."]),
        ("A pattern this book doesn't apply symmetrically", [
            "Unlike AN 8.17/8.18's deliberately mirrored pair on catching, "
            "this discourse and its companions (AN 8.47, 8.48) have no "
            "reversed counterpart addressed to husbands. The asymmetry is "
            "itself worth noticing: this cluster of teachings, addressed "
            "to and about women, doesn't receive the same paired treatment "
            "this book gives some of its other gendered material."]),
    ],
    terms=[
        ("manāpakāyikā devā",
         "&ldquo;the Agreeable Host,&rdquo; or &ldquo;deities called "
         "&lsquo;Agreeable&rsquo;&rdquo; &mdash; this discourse's own "
         "title-figures, wielding control over color, voice, and pleasure."),
        ("mātāpitaro dadanti atthakāmā hitesino anukampakā",
         "&ldquo;her mother and father give her to a husband wanting "
         "what's best for her, out of kindness and sympathy&rdquo; &mdash; "
         "the discourse's own framing of marriage, presented here without "
         "further comment."),
        ("orundhati sāmikassa bhaṇḍaṁ",
         "&ldquo;guards and protects any income her husband earns&rdquo; "
         "&mdash; one of the eight qualities, financial stewardship on the "
         "husband's behalf."),
        ("upāsikā hoti, sīlavatī hoti, cāgavatī hoti",
         "&ldquo;a lay follower who has gone for refuge... ethical... "
         "generous&rdquo; &mdash; the final three of the eight qualities, "
         "shared in substance with ideals taught to men elsewhere in this "
         "book."),
        ("cattāri ṭhānāni adhigayha",
         "part of the phrase describing the deities' threefold power over "
         "color, voice, and pleasure, displayed and then withdrawn once "
         "Anuruddha shows no interest."),
    ],
    text_intro=(
        "The discourse in full: deities performing for Anuruddha, then his "
        "question and the Buddha's answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Deities of the Agreeable Host"),
        ("p", "&sect;1", "an8.46:1.1-1.8"),
        ("h3", "A performance, and unmoved equanimity"),
        ("p", "&sect;2", "an8.46:2.1-5.2"),
        ("h3", "Anuruddha's question"),
        ("p", "&sect;3", "an8.46:9.2-9.2"),
        ("h3", "Eight qualities"),
        ("p", "&sect;4", "an8.46:10.1-18.1"),
        ("h3", "Closing verses"),
        ("p", "&sect;5", "an8.46:19.1-22.4"),
    ],
    quiz=[
        {"q": "What happens when the Agreeable deities perform music and "
              "dance for Anuruddha?",
         "opts": [
             "He is delighted and asks for more",
             "He averts his senses and stays unmoved, so the deities "
             "vanish in what the text frames as embarrassment",
             "He immediately falls asleep",
             "He joins in the performance himself"],
         "correct": 1,
         "expl": "A striking demonstration of equanimity, prompting the "
                 "deities' own reaction."},
        {"q": "What question does Anuruddha bring to the Buddha afterward?",
         "opts": [
             "How to gain the same psychic powers himself",
             "What leads women to be reborn among the Agreeable Host of "
             "gods",
             "Whether the deities were lying",
             "How to summon deities at will"],
         "correct": 1,
         "expl": "The question that prompts the Buddha's eightfold answer."},
        {"q": "How does the guide characterize the eight qualities named in "
              "the Buddha's answer?",
         "opts": [
             "As timeless, universally applicable advice for everyone",
             "As candid content reflecting an ancient patriarchal household "
             "structure, presented honestly rather than softened",
             "As entirely metaphorical, not about literal marriage",
             "As irrelevant to understanding this discourse"],
         "correct": 1,
         "expl": "Stated plainly, following this project's practice with "
                 "other difficult historical material."},
        {"q": "What asymmetry does the guide point out about this cluster "
              "of discourses?",
         "opts": [
             "None; it is perfectly symmetrical with a matching discourse "
             "for husbands",
             "Unlike AN 8.17/8.18's mirrored pair, this cluster addressed "
             "to and about women has no reversed counterpart for husbands",
             "It is addressed only to monastics",
             "It applies equally and identically to all genders"],
         "correct": 1,
         "expl": "Worth noticing explicitly, unlike the deliberate mirror "
                 "structure met elsewhere in this book."},
        {"q": "What three of the eight qualities are shared in substance "
              "with ideals taught to men elsewhere in this book?",
         "opts": [
             "Physical strength, courage, and wealth",
             "Refuge in the triple gem, ethical conduct, and generosity",
             "Skill in debate, patience, and wisdom",
             "None of the eight qualities are shared with material "
             "elsewhere"],
         "correct": 1,
         "expl": "The final three qualities, echoing broader ethical ideals "
                 "in this collection."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Kosambī, in Ghosita's Monastery",
             "Vesālī, at the Great Wood", "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "A location distinct from the sabbath cluster's usual "
                 "settings."},
    ],
    marginalia=[
        ("Unmoved by an irresistible show", [
            "any color, any voice,",
            "any pleasure at will —",
            "Anuruddha simply looks away",
        ]),
        ("Eight qualities, read plainly", [
            "deference, household duty,",
            "guarding income, honoring",
            "whoever the husband honors",
        ]),
        ("An asymmetry worth noting", [
            "no mirrored discourse exists",
            "addressed the other way —",
            "unlike this book's paired discourses elsewhere",
        ]),
        ("Cross-references", [
            "AN 8.45 &middot; previous, closing the sabbath teaching's "
            "detailed form",
            "AN 8.47 &middot; next, the same eight qualities addressed to "
            "Visākhā",
        ]),
    ],
    further=[
        '<a href="%s/an8.46/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.45.html">AN 8.45 &middot; With Bojjhā on the Sabbath</a> &mdash; '
        "previous.",
        '<a href="an-8.47.html">AN 8.47 &middot; With Visākhā on the Agreeable Gods</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.47 — Visākhāsutta
# --------------------------------------------------------------------------- #
page(
    47, "Visākhā", "With Visākhā on the Agreeable Gods",
    vagga=VAGGA_5,
    meta_title="AN 8.47 — With Visākhā on the Agreeable Gods | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Visākhāsutta, addressing AN 8.46's eight wifely qualities directly "
        "to Visākhā without the deity narrative that opened it — presented "
        "honestly, without softening its patriarchal framing. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in the stilt longhouse of Migāra's mother in "
                    "the Eastern Monastery"),
        ("Speakers", "The Buddha, addressing Visākhā directly"),
        ("Form", "The same eight qualities as AN 8.46, addressed directly "
                 "without Anuruddha's deity narrative, compressed in the "
                 "middle by internal ellipsis"),
        ("Length", "~2 minutes to read"),
        ("The narrative frame dropped, the content kept", "Where AN 8.46 "
                                                           "reached its "
                                                           "eight qualities "
                                                           "through "
                                                           "Anuruddha's own "
                                                           "encounter with "
                                                           "deities, this "
                                                           "discourse "
                                                           "states them "
                                                           "directly to "
                                                           "Visākhā with no "
                                                           "narrative "
                                                           "framing at all"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, "
                       "best read alongside AN 8.46 for its narrative "
                       "context"),
    ],
    why=(
        "The Buddha states directly to Visākhā the same eight qualities AN "
        "8.46 attributed to a wife securing rebirth among the Agreeable "
        "Host of gods, dropping Anuruddha's deity narrative entirely and "
        "delivering the teaching without any framing story."),
    guide=[
        ("The teaching in one sentence", [
            "The same eight qualities named at AN 8.46 &mdash; deference "
            "to a husband's schedule and wishes, honoring whoever he "
            "honors, household diligence, fair management of staff, "
            "guarding his income, and refuge, ethics, and generosity "
            "&mdash; are stated here directly to Visākhā, without the "
            "deity narrative that framed them before."]),
        ("A direct address, no narrative needed", [
            "This discourse strips away everything AN 8.46 used to "
            "arrive at its eight qualities &mdash; the deities' display of "
            "power, their performance, their vanishing, Anuruddha's "
            "question &mdash; and simply states the content to Visākhā as "
            "a direct teaching, opening with the same standard visit "
            "formula met throughout this chapter's Visākhā discourses."]),
        ("The same content, the same honest presentation", [
            "This reading guide continues to present the eight qualities "
            "as they stand in the source, without softening their "
            "patriarchal household framing or claiming they represent "
            "universal or timeless advice &mdash; the same approach taken "
            "at AN 8.46, applied here to the identical content."]),
        ("A pattern of repetition across this chapter", [
            "This is now the fourth discourse in this chapter that repeats "
            "substantially the same content across different addressees "
            "&mdash; following AN 8.42/8.43/8.45's detailed sabbath "
            "teaching &mdash; suggesting this book's compilers valued "
            "recording which named individuals received which teachings "
            "as much as recording the teachings' content itself."]),
    ],
    terms=[
        ("visākhā migāramātā",
         "Visākhā, Migāra's mother, addressed here without any "
         "intervening narrative, unlike AN 8.46's deity encounter."),
        ("aṭṭha dhammā samannāgatā",
         "&ldquo;when they have eight qualities&rdquo; &mdash; the "
         "discourse's own opening formula, identical to AN 8.46's."),
        ("manāpakāyikānaṁ devānaṁ sahabyataṁ upapajjanti",
         "&ldquo;reborn in company with the Gods of the Agreeable "
         "Host&rdquo; &mdash; the same destination named at AN 8.46, now "
         "reached without any narrative framing."),
        ("sīlavatī hoti, cāgavatī hoti",
         "&ldquo;ethical... generous&rdquo; &mdash; two of the final three "
         "qualities, shared in substance with broader ethical ideals in "
         "this book."),
        ("anukampakena atthakāmena bhattu vasaṁ vattamānā",
         "part of the discourse's own framing of a household relationship, "
         "presented here as found rather than reinterpreted."),
    ],
    text_intro=(
        "The discourse in full: the same eight qualities as AN 8.46, "
        "addressed directly to Visākhā. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the eight qualities"),
        ("p", "&sect;1", "an8.47:1.1-3.3"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.47:4.1-7.4"),
    ],
    quiz=[
        {"q": "How does this discourse's content relate to AN 8.46's?",
         "opts": [
             "Entirely unrelated content",
             "The identical eight qualities, without the deity narrative "
             "that framed them at AN 8.46",
             "A contradicting set of eight qualities",
             "An expanded version with new content"],
         "correct": 1,
         "expl": "The narrative dropped, the teaching kept, addressed "
                 "directly to Visākhā."},
        {"q": "What does this discourse omit that AN 8.46 included?",
         "opts": [
             "The eight qualities themselves",
             "The deities' display of power, their performance, and "
             "Anuruddha's resulting question",
             "The rebirth destination named",
             "Nothing is omitted"],
         "correct": 1,
         "expl": "A direct statement, without the narrative that led to "
                 "the teaching in AN 8.46."},
        {"q": "According to the guide, what does this discourse's "
              "repetition suggest about this chapter's compilers?",
         "opts": [
             "That they made an editing error",
             "That recording which named individuals received which "
             "teachings mattered as much as the content itself",
             "That they had run out of new material",
             "Nothing in particular"],
         "correct": 1,
         "expl": "A pattern of repetition across named addressees, seen "
                 "also in the sabbath cluster."},
        {"q": "How does this reading guide handle the eight qualities' "
              "content?",
         "opts": [
             "By reframing them as universal, timeless advice",
             "By presenting them honestly as they stand, without "
             "softening their patriarchal household framing",
             "By omitting them from the discussion entirely",
             "By declaring them entirely irrelevant today"],
         "correct": 1,
         "expl": "The same honest approach taken at AN 8.46, applied to "
                 "identical content."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kosambī, in Ghosita's Monastery",
             "Sāvatthī, in the stilt longhouse of Migāra's mother in the "
             "Eastern Monastery",
             "Vesālī, at the Great Wood",
             "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "Visākhā's own donated residence, distinct from AN 8.46's "
                 "Kosambī setting."},
        {"q": "What destination do the eight qualities lead to, as in AN "
              "8.46?",
         "opts": [
             "The Divinity's host",
             "Rebirth in company with the Gods of the Agreeable Host",
             "The gods of the four great kings",
             "No specific destination is named"],
         "correct": 1,
         "expl": "The identical destination as AN 8.46, unchanged in this "
                 "direct address."},
    ],
    marginalia=[
        ("The narrative dropped", [
            "no deities, no performance —",
            "the same eight qualities",
            "stated directly to Visākhā",
        ]),
        ("Read the same way, honestly", [
            "no softening applied here",
            "any more than at AN 8.46 —",
            "the content presented as it stands",
        ]),
        ("A pattern across this chapter", [
            "the fourth repeated teaching",
            "to a different named addressee —",
            "who received what seems to matter here",
        ]),
        ("Cross-references", [
            "AN 8.46 &middot; previous, the same eight qualities with "
            "Anuruddha's deity narrative",
            "AN 8.48 &middot; next, the same teaching addressed to "
            "Nakula's mother",
        ]),
    ],
    further=[
        '<a href="%s/an8.47/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.46.html">AN 8.46 &middot; Anuruddha and the Agreeable Deities</a> '
        "&mdash; previous.",
        '<a href="an-8.48.html">AN 8.48 &middot; With Nakula&rsquo;s Mother on the '
        "Agreeable Gods</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.48 — Nakulamātusutta
# --------------------------------------------------------------------------- #
page(
    48, "Nakulamātu", "With Nakula&rsquo;s Mother on the Agreeable Gods",
    vagga=VAGGA_5,
    meta_title="AN 8.48 — With Nakula's Mother on the Agreeable Gods | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nakulamātusutta, the same eight qualities restated in full for "
        "the laywoman Nakula's mother, one half of this tradition's most "
        "celebrated devoted couple. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The land of the Bhaggas, at Crocodile's Bellow, in the "
                    "deer park at Bhesakaḷā's Wood"),
        ("Speakers", "The Buddha, addressing the housewife Nakula's mother "
                     "directly"),
        ("Form", "The same eight qualities as AN 8.46 and 8.47, this time "
                 "spelled out in full without internal ellipsis"),
        ("Length", "~2 minutes to read"),
        ("A third named addressee, in full detail", "Where AN 8.47 "
                                                     "compressed the middle "
                                                     "qualities by "
                                                     "ellipsis, this "
                                                     "discourse restates "
                                                     "every one of the "
                                                     "eight qualities in "
                                                     "full for Nakula's "
                                                     "mother, one half of a "
                                                     "couple this tradition "
                                                     "elsewhere celebrates "
                                                     "for their devotion"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to AN 8.46 and 8.47, given here "
                       "in its fullest, most detailed form"),
    ],
    why=(
        "The Buddha restates the same eight qualities met at AN 8.46 and "
        "8.47 in full, this time for Nakula's mother, a laywoman elsewhere "
        "in the tradition celebrated together with her husband Nakula's "
        "father as an exemplary devoted couple."),
    guide=[
        ("The teaching in one sentence", [
            "Nakula's mother receives the same eight qualities as Visākhā "
            "at AN 8.47 and the answer given to Anuruddha at AN 8.46, "
            "spelled out here in their fullest form without any "
            "compressing ellipsis."]),
        ("A third address, now given in full", [
            "This is the third time this cluster of discourses states the "
            "same eight qualities, and the first since AN 8.46 to spell "
            "every one of them out in complete detail rather than "
            "compressing the middle sections &mdash; deference to the "
            "husband's schedule, honoring whoever he honors, household "
            "diligence, staff management, income guarding, refuge, "
            "ethics, and generosity, each given its full description."]),
        ("Nakula's mother, elsewhere a celebrated figure", [
            "Nakula's mother and her husband, Nakula's father, are "
            "remembered elsewhere in this literature as an exemplary "
            "devoted couple, addressed together by the Buddha in other "
            "discourses on aging and companionship across a shared "
            "spiritual life &mdash; a context this particular discourse "
            "doesn't itself reference, focused instead on the same eight "
            "qualities met twice already in this chapter."]),
        ("Continuing this project's honest presentation", [
            "As with AN 8.46 and 8.47, this reading guide states the "
            "content as it stands in the source rather than reframing it "
            "as universal counsel, maintaining the same practice across "
            "all three discourses in this chapter's wifely-duty cluster."]),
    ],
    terms=[
        ("nakulamātā gahapatānī",
         "the housewife Nakula's mother, this discourse's addressee, "
         "elsewhere celebrated together with her husband as a devoted "
         "couple."),
        ("bhagganaṁ susumāragire bhesakaḷāvane migadāye",
         "&ldquo;the land of the Bhaggas at Crocodile's Bellow, in the "
         "deer park at Bhesakaḷā's Wood&rdquo; &mdash; this discourse's "
         "own distinct setting, different from AN 8.46's Kosambī and AN "
         "8.47's Sāvatthī."),
        ("dakkho hoti analasā tattha upāyāya",
         "&ldquo;deft and tireless&rdquo; &mdash; part of the third "
         "quality, household diligence, spelled out here without "
         "compression."),
        ("na atimaññati, na acchati, na avamaññati",
         "part of the discourse's description of proper deference within "
         "the marriage, given in full in this particular restatement."),
        ("manāpakāyikānaṁ devānaṁ sahabyataṁ upapajjanti",
         "&ldquo;reborn in company with the Gods of the Agreeable "
         "Host&rdquo; &mdash; the same destination named at AN 8.46 and "
         "8.47, unchanged in this fuller restatement."),
    ],
    text_intro=(
        "The discourse in full: the same eight qualities as AN 8.46 and "
        "8.47, spelled out in complete detail for Nakula's mother. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and the eight qualities in full"),
        ("p", "&sect;1", "an8.48:1.1-10.1"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.48:11.1-14.4"),
    ],
    quiz=[
        {"q": "How does this discourse's presentation differ from AN "
              "8.47's?",
         "opts": [
             "It has entirely different content",
             "It spells out every one of the eight qualities in full, "
             "without the compressing ellipsis AN 8.47 used",
             "It has fewer qualities than AN 8.47",
             "It contradicts AN 8.47's teaching"],
         "correct": 1,
         "expl": "The fullest, most detailed restatement of this "
                 "cluster's shared content."},
        {"q": "Who is Nakula's mother, addressed in this discourse?",
         "opts": [
             "A member of the Buddha's own Sakyan clan",
             "A laywoman elsewhere in the tradition celebrated together "
             "with her husband as an exemplary devoted couple",
             "A rival ascetic teacher",
             "A queen ruling one of the sixteen great countries"],
         "correct": 1,
         "expl": "A figure with a broader context this particular "
                 "discourse doesn't itself reference."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kosambī, in Ghosita's Monastery",
             "The land of the Bhaggas at Crocodile's Bellow, in the deer "
             "park at Bhesakaḷā's Wood",
             "Sāvatthī, in the stilt longhouse of Migāra's mother",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A distinct setting from both AN 8.46 and AN 8.47."},
        {"q": "How many times has this cluster of discourses now stated the "
              "same eight qualities?",
         "opts": [
             "Once", "Three times — at AN 8.46, 8.47, and this discourse",
             "Ten times", "This is the only statement of these qualities"],
         "correct": 1,
         "expl": "A recurring pattern of restating the same content for "
                 "different named addressees."},
        {"q": "How does this reading guide continue to handle the eight "
              "qualities' content?",
         "opts": [
             "By reframing them as universal advice for this discourse "
             "specifically",
             "By continuing the same honest presentation as AN 8.46 and "
             "8.47, without softening",
             "By omitting discussion of the content entirely",
             "By contradicting its own earlier treatment"],
         "correct": 1,
         "expl": "A consistent approach maintained across all three "
                 "discourses in this cluster."},
        {"q": "What destination do the eight qualities lead to?",
         "opts": [
             "The Divinity's host",
             "Rebirth in company with the Gods of the Agreeable Host",
             "The gods of the thirty-three",
             "No destination is named"],
         "correct": 1,
         "expl": "The identical destination named across all three "
                 "discourses in this cluster."},
    ],
    marginalia=[
        ("The fullest restatement", [
            "every one of the eight",
            "spelled out without ellipsis —",
            "the third time in this chapter",
        ]),
        ("A celebrated couple, elsewhere", [
            "Nakula's mother and father",
            "remembered for their devotion —",
            "a context this discourse doesn't reference",
        ]),
        ("The same honest presentation", [
            "no reframing as universal —",
            "the content stated as it stands,",
            "consistent across all three discourses",
        ]),
        ("Cross-references", [
            "AN 8.47 &middot; previous, the same eight qualities addressed "
            "to Visākhā",
            "AN 8.49 &middot; next, a related but restructured teaching: "
            "four qualities for this life, four for the next",
        ]),
    ],
    further=[
        '<a href="%s/an8.48/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.47.html">AN 8.47 &middot; With Visākhā on the Agreeable Gods</a> '
        "&mdash; previous.",
        '<a href="an-8.49.html">AN 8.49 &middot; Winning in This Life (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.49 — Paṭhamaidhalokikasutta -- restructures this cluster's eight qualities
# into 4+4 (this-life / next-life), addressed to Visākhā.
# --------------------------------------------------------------------------- #
page(
    49, "Paṭhamaidhalokika", "Winning in This Life (1st)",
    vagga=VAGGA_5,
    meta_title="AN 8.49 — Winning in This Life (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaidhalokikasutta, restructuring the wifely-duty material met at "
        "AN 8.46-48 into four qualities for succeeding in this life and "
        "four for succeeding in the next — addressed to Visākhā, presented "
        "honestly. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in the stilt longhouse of Migāra's mother in "
                    "the Eastern Monastery"),
        ("Speakers", "The Buddha, addressing Visākhā directly"),
        ("Form", "Four qualities for worldly success, then four for "
                 "spiritual success, each of the eight explained in turn, "
                 "closing in verse"),
        ("Length", "~3 minutes to read"),
        ("The same territory, restructured", "Where AN 8.46-48 named eight "
                                             "qualities as a single set "
                                             "leading to one rebirth "
                                             "destination, this discourse "
                                             "reorganizes overlapping "
                                             "material into two distinct "
                                             "fours — this life and the "
                                             "next — with the closing "
                                             "verses referring to "
                                             "&ldquo;sixteen respects&rdquo; "
                                             "worth noting rather than "
                                             "fully resolving"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "clear fourfold-plus-fourfold structure, with one "
                       "numerical detail in the closing verse worth reading "
                       "carefully"),
    ],
    why=(
        "The Buddha tells Visākhā that a woman with four qualities "
        "&mdash; well-organized at work, managing domestic help, acting "
        "lovingly toward her husband, and preserving his earnings &mdash; "
        "succeeds at winning in this life, and a woman with four further "
        "qualities &mdash; faith, ethics, generosity, and wisdom &mdash; "
        "succeeds at winning in the next, restructuring material "
        "overlapping with AN 8.46-48 into two distinct fourfold sets."),
    guide=[
        ("The teaching in one sentence", [
            "Four qualities &mdash; organization at work, managing "
            "domestic help, loving devotion to her husband, and guarding "
            "his earnings &mdash; let a woman succeed in this life, and "
            "four further qualities &mdash; faith, ethical conduct, "
            "generosity, and wisdom &mdash; let her succeed in the next, "
            "together forming a differently organized eight from the "
            "single set met at AN 8.46-48."]),
        ("This life: overlapping material, reorganized", [
            "The first four qualities substantially overlap with items "
            "already met in AN 8.46-48's own eight, but reorganized "
            "explicitly under the heading of worldly rather than "
            "spiritual success: work organization, staff management, "
            "devotion to her husband framed as never transgressing his "
            "wishes even at the cost of her own life, and financial "
            "guardianship."]),
        ("The next life: a genuinely different fourth quality", [
            "The second four qualities &mdash; faith, ethics, generosity, "
            "and wisdom &mdash; are the same fourfold accomplishment "
            "pattern (saddhāsampadā, sīlasampadā, cāgasampadā, "
            "paññāsampadā) already met in this book's discourses to men, "
            "here applied without alteration to a woman's own path to "
            "spiritual success, including the wisdom of arising and "
            "passing away explicitly credited as leading to the ending of "
            "suffering."]),
        ("An unresolved number in the closing verse", [
            "The closing verse describes a woman with these eight "
            "qualities as &ldquo;accomplished in sixteen respects, "
            "complete with the eight factors&rdquo; &mdash; a number this "
            "reading guide notes rather than fully resolves, since the "
            "verse doesn't itself specify what the second eight respects "
            "consist of beyond the eight qualities already named."]),
    ],
    terms=[
        ("diṭṭhadhammikatthavijayāya paṭipannā",
         "&ldquo;practicing to win in this life&rdquo; &mdash; the "
         "framing for the first four qualities, distinct from the "
         "spiritual, next-life framing of the second four."),
        ("saṁparāyikatthavijayāya paṭipannā",
         "&ldquo;practicing to win in the next life&rdquo; &mdash; the "
         "framing for the second four qualities, faith through wisdom."),
        ("anaññamanā pana bhattu",
         "&ldquo;would not transgress in any way that her husband would "
         "not consider agreeable, even for the sake of her own life&rdquo; "
         "&mdash; the discourse's own definition of loving devotion, "
         "stated here without further comment."),
        ("udayatthagāminiyā paññāya samannāgatā",
         "&ldquo;the wisdom of arising and passing away&rdquo; &mdash; "
         "the fourth and final quality for next-life success, explicitly "
         "called noble, penetrative, and leading to the complete ending of "
         "suffering."),
        ("soḷasahi ṭhānehi samannāgatā, aṭṭhaṅgasusamāhitā",
         "&ldquo;accomplished in sixteen respects, complete with the "
         "eight factors&rdquo; &mdash; the closing verse's own numerical "
         "claim, noted here rather than fully resolved."),
    ],
    text_intro=(
        "The discourse in full: four qualities for this-life success, four "
        "for next-life success, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting, and four qualities for this life"),
        ("p", "&sect;1", "an8.49:1.1-3.3"),
        ("h3", "Four qualities explained"),
        ("p", "&sect;2", "an8.49:4.1-6.4"),
        ("h3", "Four qualities for the next life"),
        ("p", "&sect;3", "an8.49:7.1-12.1"),
        ("h3", "Closing verses"),
        ("p", "&sect;4", "an8.49:13.1-16.4"),
    ],
    quiz=[
        {"q": "How does this discourse structure its eight qualities, "
              "compared to AN 8.46-48's single set of eight?",
         "opts": [
             "Identically, with no reorganization",
             "As two distinct fourfold sets — four for this-life success, "
             "four for next-life success",
             "As a single set of sixteen items",
             "As eight entirely unrelated qualities"],
         "correct": 1,
         "expl": "A restructuring of overlapping material into two "
                 "explicitly separate fours."},
        {"q": "What are the four qualities for succeeding in the next "
              "life?",
         "opts": [
             "Wealth, status, education, and beauty",
             "Faith, ethical conduct, generosity, and wisdom",
             "Physical strength, courage, patience, and skill",
             "The five precepts alone"],
         "correct": 1,
         "expl": "The same fourfold accomplishment pattern met elsewhere "
                 "in this book, here applied to a woman's own path."},
        {"q": "What numerical detail in the closing verse does the guide "
              "note rather than fully resolve?",
         "opts": [
             "A miscounted list of five items",
             "The claim of being 'accomplished in sixteen respects,' which "
             "the verse doesn't itself explain beyond the eight qualities "
             "named",
             "A contradiction with AN 8.46's eight qualities",
             "A missing quality entirely"],
         "correct": 1,
         "expl": "An honest acknowledgment of an unresolved detail, rather "
                 "than a forced explanation."},
        {"q": "How is loving devotion to her husband defined in this "
              "discourse?",
         "opts": [
             "Agreeing with everything he says publicly",
             "Not transgressing in any way he wouldn't consider agreeable, "
             "even for the sake of her own life",
             "Managing all family finances independently",
             "Living separately for part of the year"],
         "correct": 1,
         "expl": "The discourse's own definition, stated plainly."},
        {"q": "Who is addressed in this discourse?",
         "opts": [
             "Nakula's mother", "Visākhā, Migāra's mother",
             "Bojjhā", "The layman Vāseṭṭha"],
         "correct": 1,
         "expl": "The fourth discourse in this chapter addressed to "
                 "Visākhā by name."},
        {"q": "What is the fourth quality for succeeding in the next life?",
         "opts": [
             "Physical beauty",
             "The wisdom of arising and passing away, leading to the "
             "complete ending of suffering",
             "Political influence",
             "Skill in household management"],
         "correct": 1,
         "expl": "The final and highest of the four next-life qualities."},
    ],
    marginalia=[
        ("Two fours, not one eight", [
            "this life: work, staff,",
            "devotion, guarded wealth —",
            "next life: faith, ethics, giving, wisdom",
        ]),
        ("Wisdom, closing the higher four", [
            "arising and passing away —",
            "noble, penetrative,",
            "leading to suffering's end",
        ]),
        ("Sixteen respects, unresolved", [
            "the verse claims sixteen —",
            "but names only eight outright —",
            "noted here, not forced to fit",
        ]),
        ("Cross-references", [
            "AN 8.48 &middot; previous, the same wifely-duty material as a "
            "single set of eight",
            "AN 8.50 &middot; next, the same restructured teaching stated "
            "impersonally, closing this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an8.49/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.48.html">AN 8.48 &middot; With Nakula&rsquo;s Mother on the Agreeable '
        "Gods</a> &mdash; previous.",
        '<a href="an-8.50.html">AN 8.50 &middot; Winning in This Life (2nd)</a> &mdash; next, '
        "closing this chapter and the First Fifty.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.50 — Dutiyaidhalokikasutta — closes ch.5 Uposathavagga and the First Fifty
# (Paṭhamapaṇṇāsaka, AN 8.1-50).
# --------------------------------------------------------------------------- #
page(
    50, "Dutiyaidhalokika", "Winning in This Life (2nd)",
    vagga=VAGGA_5,
    meta_title="AN 8.50 — Winning in This Life (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaidhalokikasutta, restating AN 8.49's eight qualities impersonally "
        "to the mendicants rather than to Visākhā, closing this chapter and "
        "the First Fifty of the Book of the Eights. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "AN 8.49's same eight qualities, restated to the "
                 "mendicants generally rather than to Visākhā, compressed "
                 "throughout by internal ellipsis"),
        ("Length", "~2 minutes to read"),
        ("Closing this chapter and the First Fifty", "This discourse "
                                                      "closes both "
                                                      "Uposathavagga and "
                                                      "the First Fifty of "
                                                      "the Book of the "
                                                      "Eights (AN 8.1&ndash;"
                                                      "50); the Second "
                                                      "Fifty begins at AN "
                                                      "8.51"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to AN 8.49, heavily compressed "
                       "here"),
    ],
    why=(
        "AN 8.50 restates the same eight qualities met at AN 8.49 &mdash; "
        "four for succeeding in this life, four for succeeding in the "
        "next &mdash; this time addressed impersonally to the mendicants "
        "rather than to Visākhā by name, closing both this chapter and the "
        "First Fifty of the Book of the Eights."),
    guide=[
        ("The teaching in one sentence", [
            "The same eight qualities as AN 8.49 &mdash; work "
            "organization, staff management, loving devotion, and "
            "financial guardianship for this-life success; faith, ethics, "
            "generosity, and wisdom for next-life success &mdash; are "
            "restated here to the mendicants generally, closing this "
            "chapter and the First Fifty."]),
        ("From personal address to general teaching", [
            "Where AN 8.49 spoke to Visākhā directly, this discourse opens "
            "with the standard address to the mendicants, &ldquo;Mendicants, "
            "a lady who has four qualities...&rdquo; &mdash; the same "
            "content, delivered now as general instruction rather than "
            "personal counsel to a specific laywoman."]),
        ("Heavy compression, trusting what came before", [
            "This discourse compresses far more than AN 8.49 did, cutting "
            "explanatory detail from nearly every quality via internal "
            "ellipsis and trusting the reader to recall the fuller "
            "explanations just given &mdash; a fitting way to close a "
            "chapter that has repeated this material across several "
            "addressees already."]),
        ("Closing a chapter, and the First Fifty itself", [
            "This discourse's significance extends beyond its own content: "
            "it is the last discourse of Uposathavagga, and with it, the "
            "First Fifty (Paṭhamapaṇṇāsaka) of the Book of the Eights "
            "comes to a close. The Second Fifty, beginning at AN 8.51, "
            "opens a new sequence of chapters."]),
    ],
    terms=[
        ("diṭṭhadhammikatthavijayāya paṭipannā ... saṁparāyikatthavijayāya "
         "paṭipannā",
         "&ldquo;practicing to win in this life... practicing to win in "
         "the next life&rdquo; &mdash; the identical fourfold-plus-fourfold "
         "framing as AN 8.49, restated here impersonally."),
        ("saddhāsampadāya samannāgatā ... paññāsampadāya samannāgatā",
         "&ldquo;accomplished in faith... accomplished in wisdom&rdquo; "
         "&mdash; the four next-life qualities, compressed here by "
         "ellipsis but identical to AN 8.49's fuller statement."),
        ("paṭhamapaṇṇāsakaṁ",
         "&ldquo;the First Fifty&rdquo; &mdash; the structural division "
         "this discourse closes, spanning AN 8.1 through AN 8.50."),
        ("dutiyapaṇṇāsakaṁ",
         "&ldquo;the Second Fifty&rdquo; &mdash; the division beginning "
         "immediately after this discourse, at AN 8.51."),
        ("udayatthagāminiyā paññāya samannāgatā",
         "&ldquo;the wisdom of arising and passing away&rdquo; &mdash; "
         "the same closing quality named at AN 8.49, unchanged here."),
    ],
    text_intro=(
        "The discourse in full: the same eight qualities as AN 8.49, "
        "restated to the mendicants, closing this chapter and the First "
        "Fifty. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four qualities for this life"),
        ("p", "&sect;1", "an8.50:1.1-5.4"),
        ("h3", "Four qualities for the next life"),
        ("p", "&sect;2", "an8.50:6.1-10.4"),
        ("h3", "Closing verses"),
        ("p", "&sect;3", "an8.50:11.1-14.4"),
    ],
    quiz=[
        {"q": "How does this discourse's opening address differ from AN "
              "8.49's?",
         "opts": [
             "No difference; both address Visākhā directly",
             "This discourse opens with the standard address to the "
             "mendicants generally, rather than speaking to Visākhā by "
             "name",
             "This discourse addresses Nakula's mother instead",
             "This discourse has no opening address at all"],
         "correct": 1,
         "expl": "The same content, delivered as general instruction "
                 "rather than personal counsel."},
        {"q": "How does this discourse handle the explanatory detail AN "
              "8.49 gave for each quality?",
         "opts": [
             "It expands the detail further",
             "It compresses most of it by internal ellipsis, trusting the "
             "reader to recall AN 8.49's fuller explanations",
             "It omits the qualities themselves entirely",
             "It replaces the explanations with new ones"],
         "correct": 1,
         "expl": "Heavier compression than AN 8.49, fitting for a chapter "
                 "closing on repeated material."},
        {"q": "What structural division does this discourse close?",
         "opts": [
             "Nothing in particular",
             "Both Uposathavagga and the First Fifty (Paṭhamapaṇṇāsaka) "
             "of the Book of the Eights",
             "The entire Book of the Eights",
             "Only a single paragraph"],
         "correct": 1,
         "expl": "AN 8.1 through AN 8.50 complete; the Second Fifty begins "
                 "at AN 8.51."},
        {"q": "What are the four qualities for succeeding in this life, as "
              "in AN 8.49?",
         "opts": [
             "Faith, ethics, generosity, and wisdom",
             "Work organization, staff management, loving devotion, and "
             "financial guardianship",
             "Physical strength, courage, patience, and skill",
             "Wealth, status, education, and beauty"],
         "correct": 1,
         "expl": "The identical four qualities as AN 8.49, here "
                 "compressed."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī, in the stilt longhouse of Migāra's mother",
             "No setting is stated in the source",
             "Yes, at Kosambī, in Ghosita's Monastery",
             "Yes, at Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A bare formula, distinct from AN 8.49's personal address "
                 "to Visākhā in her own residence."},
        {"q": "What quality closes the four next-life qualities, as in AN "
              "8.49?",
         "opts": [
             "Physical beauty",
             "The wisdom of arising and passing away",
             "Political influence",
             "Skill in debate"],
         "correct": 1,
         "expl": "The same closing quality named at AN 8.49, unchanged "
                 "here."},
    ],
    marginalia=[
        ("From Visākhā to the mendicants", [
            "the same eight qualities,",
            "no longer personal counsel —",
            "general instruction instead",
        ]),
        ("Compressed, trusting what came before", [
            "most detail cut by ellipsis —",
            "fitting for a chapter",
            "closing on repeated ground",
        ]),
        ("The First Fifty, complete", [
            "AN 8.1 through 8.50 —",
            "Uposathavagga closes here —",
            "the Second Fifty begins next",
        ]),
        ("Cross-references", [
            "AN 8.49 &middot; previous, the same eight qualities addressed "
            "personally to Visākhā",
            "AN 8.41 &middot; earlier, opening this chapter with the "
            "sabbath's own eight factors",
        ]),
    ],
    further=[
        '<a href="%s/an8.50/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.49.html">AN 8.49 &middot; Winning in This Life (1st)</a> &mdash; '
        "previous.",
        '<a href="an-8.41.html">AN 8.41 &middot; The Sabbath With Eight Factors, In Brief'
        "</a> &mdash; earlier, opening this chapter.",
    ],
)


VAGGA_6 = "<em>Gotamīvagga</em> &mdash; the sixth chapter of the Eights, opening the Second Fifty"


# --------------------------------------------------------------------------- #
# AN 8.51 — Gotamīsutta -- opens ch.6 Gotamīvagga and the Second Fifty. This
# is one of the most historically significant and most debated discourses in
# the canon: the founding of the bhikkhunī order and the eight garudhammā.
# Presented factually, noting the scholarly debate over the decline
# prophecy and the garudhammā's authenticity without asserting a conclusion
# beyond the textual evidence -- per this project's established practice
# with difficult material (AN 4.80, AN 7.63, AN 8.46-48).
# --------------------------------------------------------------------------- #
page(
    51, "Gotamī", "With Gotamī",
    vagga=VAGGA_6,
    meta_title="AN 8.51 — With Gotamī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Gotamīsutta — the founding of the bhikkhunī order, the eight "
        "garudhamma, and the Buddha's prediction that the true teaching's "
        "lifespan would be halved — one of the canon's most historically "
        "significant and most debated discourses, presented factually with "
        "the scholarly debate noted honestly. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Kapilavatthu, at the Banyan Tree Monastery, then "
                    "Vesālī, at the Great Wood"),
        ("Speakers", "Mahāpajāpati Gotamī, Venerable Ānanda, and the Buddha"),
        ("Form", "A narrative in three refused requests, a journey on foot, "
                 "Ānanda's intervention, the eight principles of respect, "
                 "and the Buddha's own closing prediction and similes"),
        ("Length", "~5 minutes to read"),
        ("One of the canon's most debated discourses", "This account of "
                                                        "the bhikkhunī "
                                                        "order's founding, "
                                                        "including the "
                                                        "eight garudhamma "
                                                        "and the halved-"
                                                        "lifespan "
                                                        "prediction, is "
                                                        "widely discussed "
                                                        "in modern "
                                                        "Buddhist "
                                                        "scholarship, "
                                                        "including by this "
                                                        "translation's own "
                                                        "translator, over "
                                                        "whether these "
                                                        "specific elements "
                                                        "reflect later "
                                                        "monastic-political "
                                                        "additions rather "
                                                        "than the earliest "
                                                        "layer of the "
                                                        "account"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "historically and doctrinally weighty; this reading "
                       "guide states the content plainly and notes the "
                       "scholarly debate without resolving it"),
    ],
    why=(
        "Mahāpajāpati Gotamī, the Buddha's aunt and foster mother, asks "
        "three times for women to be allowed to go forth and is refused "
        "each time; after she and several Sakyan women walk to Vesālī on "
        "foot and Ānanda intervenes on their behalf, the Buddha agrees on "
        "the condition that Gotamī accept eight principles of respect "
        "subordinating nuns to monks, then predicts that the true "
        "teaching's lifespan will be halved as a result."),
    guide=[
        ("The teaching in one sentence", [
            "After Mahāpajāpati Gotamī's request for women's ordination is "
            "refused three times, Ānanda secures the Buddha's agreement by "
            "asking directly whether women are capable of realizing the "
            "same four fruits of the path as men and reminding the Buddha "
            "of Gotamī's own care for him as an infant; the Buddha agrees "
            "on condition that Gotamī accept eight principles of respect, "
            "then predicts the true teaching's lifespan is halved as a "
            "result, illustrated by three similes of vulnerability."]),
        ("Three refusals, a journey on foot, and Ānanda's argument", [
            "Gotamī's own three direct requests, made in person, are each "
            "met with the same refusal. Rather than giving up, she has her "
            "head shaved, dons ocher robes, and walks with several Sakyan "
            "women from Kapilavatthu to Vesālī &mdash; her feet swollen, "
            "her limbs covered in dust &mdash; where Ānanda finds her "
            "weeping outside the gate and takes up her cause. Ānanda's own "
            "argument turns not on repeating her request but on asking "
            "whether women are capable of the same four fruits of the "
            "path, and reminding the Buddha that Gotamī nursed him at her "
            "own breast after his birth mother's death."]),
        ("The eight garudhamma", [
            "The Buddha's consent comes bound to eight principles of "
            "respect (garudhamma): a nun of a hundred years must bow to a "
            "monk ordained that very day; nuns can't spend the rains "
            "retreat where there are no monks; nuns depend on the monks' "
            "community for the sabbath date and for teaching; nuns "
            "confess offenses to both communities; a nun's grave offense "
            "requires penance before both communities; full ordination "
            "for a trainee nun requires both communities' involvement; "
            "nuns may never abuse or insult a monk; and monks may "
            "criticize nuns, but nuns may never criticize monks. Gotamī "
            "accepts all eight as her own ordination, compared to a young "
            "person delighted to receive a garland of flowers."]),
        ("A prediction, three similes, and an unresolved scholarly debate", [
            "The Buddha's closing prediction &mdash; that the true "
            "teaching, which would otherwise have lasted a thousand "
            "years, will now last only five hundred because of women's "
            "ordination &mdash; is illustrated by three similes of "
            "vulnerability: a household with many women and few men, "
            "inviting bandits; a rice field struck by disease; a "
            "sugarcane field struck by blight. This reading guide states "
            "these elements as the text presents them, while noting that "
            "modern scholarship, including from this very translation's "
            "own translator, has raised serious questions about whether "
            "the garudhamma and the decline prediction represent the "
            "earliest layer of this account or later additions reflecting "
            "later institutional concerns &mdash; a live scholarly "
            "question this guide does not attempt to resolve."]),
    ],
    terms=[
        ("mahāpajāpatī gotamī",
         "Mahāpajāpati Gotamī, the Buddha's maternal aunt, who raised him "
         "after his mother's death and here becomes the first woman to "
         "seek ordination."),
        ("aṭṭha garudhammā",
         "&ldquo;the eight principles of respect&rdquo; &mdash; the "
         "conditions the Buddha attaches to women's ordination, "
         "structurally subordinating nuns to monks."),
        ("alaṁ, ānanda, mā te rucci mātugāmassa",
         "&ldquo;enough, Ānanda; don't endorse it&rdquo; &mdash; the "
         "Buddha's own refrain, repeated identically across all three of "
         "Gotamī's own requests and Ānanda's first attempts."),
        ("sotāpattiphalaṁ vā sakadāgāmiphalaṁ vā anāgāmiphalaṁ vā "
         "arahattaṁ vā sacchikātuṁ",
         "&ldquo;realize the fruits of stream-entry, once-return, non-"
         "return, and perfection&rdquo; &mdash; the question Ānanda "
         "reframes the debate around, securing the Buddha's affirmation "
         "of women's spiritual capacity before the ordination itself is "
         "granted."),
        ("addhā, ānanda, na cireva brahmacariyaṁ ṭhassati",
         "&ldquo;the spiritual life will not last long&rdquo; &mdash; the "
         "Buddha's own closing prediction, at the center of ongoing "
         "scholarly discussion about this passage's textual history."),
    ],
    text_intro=(
        "The discourse in full: three refused requests, the journey to "
        "Vesālī, Ānanda's intervention, the eight principles of respect, "
        "and the Buddha's closing prediction. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three requests, three refusals"),
        ("p", "&sect;1", "an8.51:1.1-4.1"),
        ("h3", "The journey to Vesālī"),
        ("p", "&sect;2", "an8.51:5.1-6.5"),
        ("h3", "Ānanda's intervention"),
        ("p", "&sect;3", "an8.51:7.1-9.10"),
        ("h3", "The eight principles of respect"),
        ("p", "&sect;4", "an8.51:10.1-19.1"),
        ("h3", "Gotamī accepts"),
        ("p", "&sect;5", "an8.51:20.1-24.2"),
        ("h3", "The Buddha's prediction, and three similes"),
        ("p", "&sect;6", "an8.51:25.1-30.2"),
    ],
    quiz=[
        {"q": "How many times does Gotamī herself directly request the "
              "going forth for women, and how is each request met?",
         "opts": [
             "Once, and it is granted immediately",
             "Three times, each met with the identical refusal, 'Enough, "
             "Gotamī. Don't endorse it'",
             "Twice, with the second request granted",
             "She never asks directly; only Ānanda asks"],
         "correct": 1,
         "expl": "A repeated formula of refusal before Gotamī takes further "
                 "action herself."},
        {"q": "What does Gotamī do after her three requests are refused?",
         "opts": [
             "She abandons the effort entirely",
             "She has her head shaved, dons ocher robes, and walks with "
             "several Sakyan women from Kapilavatthu to Vesālī",
             "She appeals directly to the king",
             "She waits several years before trying again"],
         "correct": 1,
         "expl": "A physically demanding journey on foot, arriving with "
                 "swollen feet and dust-covered limbs."},
        {"q": "What argument does Ānanda make that succeeds where the "
              "direct requests failed?",
         "opts": [
             "He threatens to leave the Saṅgha himself",
             "He asks whether women are capable of the same four fruits of "
             "the path as men, and reminds the Buddha that Gotamī nursed "
             "him after his mother's death",
             "He simply repeats Gotamī's own request word for word",
             "He bribes the Buddha's attendants"],
         "correct": 1,
         "expl": "A reframing of the question around spiritual capacity, "
                 "plus a personal appeal to gratitude."},
        {"q": "What condition does the Buddha attach to granting women's "
              "ordination?",
         "opts": [
             "No condition at all",
             "Gotamī's acceptance of eight principles of respect "
             "(garudhamma) structurally subordinating nuns to monks",
             "A vow of complete silence for life",
             "Payment of a specific sum to the Saṅgha"],
         "correct": 1,
         "expl": "Eight conditions Gotamī accepts, compared by her to "
                 "receiving a garland of flowers."},
        {"q": "What does the Buddha predict will result from women's "
              "ordination, and how does the guide handle this claim?",
         "opts": [
             "That the true teaching's lifespan will be halved, from a "
             "thousand years to five hundred — presented factually, with "
             "the guide noting ongoing scholarly debate over whether this "
             "reflects the earliest layer of the text",
             "That the true teaching will last forever regardless",
             "Nothing is predicted; the discourse ends without comment",
             "That women's ordination will have no effect either way"],
         "correct": 0,
         "expl": "A significant, debated claim, stated here as the text "
                 "presents it, with scholarly context offered rather than "
                 "resolved."},
        {"q": "What three similes illustrate the Buddha's prediction?",
         "opts": [
             "A lotus, a lamp, and a raft",
             "A household with many women and few men easily robbed, a "
             "rice field struck by disease, and a sugarcane field struck "
             "by blight",
             "A mountain, a river, and the ocean",
             "A chariot, a horse, and a rider"],
         "correct": 1,
         "expl": "Three images of vulnerability, closing the discourse."},
    ],
    marginalia=[
        ("Three requests, three refusals", [
            "'Enough, Gotamī' — repeated,",
            "then she walks to Vesālī herself,",
            "feet swollen, robed in ocher",
        ]),
        ("Ānanda reframes the question", [
            "not repeating the request,",
            "but asking: can women realize",
            "the same four fruits as men?",
        ]),
        ("Eight conditions, and a prediction", [
            "garudhamma accepted like a garland —",
            "then: the teaching's span halved —",
            "a claim modern scholarship still debates",
        ]),
        ("Cross-references", [
            "AN 8.50 &middot; earlier, closing the First Fifty",
            "AN 8.52 &middot; next, the qualities of a monk fit to advise "
            "nuns",
        ]),
    ],
    further=[
        '<a href="%s/an8.51/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.50.html">AN 8.50 &middot; Winning in This Life (2nd)</a> &mdash; '
        "earlier, closing the First Fifty.",
        '<a href="an-8.52.html">AN 8.52 &middot; An Adviser for Nuns</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.52 — Ovādasutta
# --------------------------------------------------------------------------- #
page(
    52, "Ovāda", "An Adviser for Nuns",
    vagga=VAGGA_6,
    meta_title="AN 8.52 — An Adviser for Nuns | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ovādasutta, on eight qualities a monk must have to be deemed fit "
        "to advise the community of nuns, including an explicit disciplinary "
        "requirement and a twenty-year ordination minimum. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, in the hall with the "
                    "peaked roof — the same location as AN 8.51's own "
                    "closing scene"),
        ("Speakers", "Venerable Ānanda, asking, and the Buddha, answering"),
        ("Form", "A direct question from Ānanda, answered with an "
                 "eight-item list of qualifications"),
        ("Length", "under 1 minute to read"),
        ("A structural follow-on to AN 8.51", "Coming immediately after "
                                              "the bhikkhunī order's "
                                              "founding, this discourse "
                                              "addresses a practical "
                                              "question the previous "
                                              "discourse's eight garudhamma "
                                              "made newly urgent: who is "
                                              "actually qualified to serve "
                                              "in the advisory role those "
                                              "principles establish"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and direct, worth reading alongside AN 8.51"),
    ],
    why=(
        "Asked by Ānanda how many qualities a monk needs to be deemed an "
        "adviser for nuns, the Buddha names eight: ethical conduct, deep "
        "learning, mastery of both monastic codes, articulate speech, the "
        "ability to inspire the community of nuns, being well liked by "
        "most of them, a clean record with no prior sexual harassment of "
        "any nun, and at least twenty years of ordination."),
    guide=[
        ("The teaching in one sentence", [
            "A monk qualified to advise nuns must be ethical, learned in "
            "the teachings, thoroughly versed in both monastic codes, an "
            "articulate and inspiring speaker, well liked by most nuns, "
            "free of any history of sexually harassing a nun, and ordained "
            "for at least twenty years."]),
        ("A question this discourse's placement makes urgent", [
            "Following directly after AN 8.51's account of the bhikkhunī "
            "order's founding and its eight garudhamma &mdash; several of "
            "which require nuns to depend on the monks' community for "
            "guidance, the sabbath date, and instruction &mdash; this "
            "discourse's question isn't abstract: it asks who is actually "
            "fit to fill that dependent role responsibly."]),
        ("An explicit disciplinary safeguard", [
            "Among the eight qualities, one stands out for its specificity "
            "and its plain acknowledgment of a real risk: a monk qualified "
            "to advise nuns must never have previously sexually harassed "
            "any woman who has gone forth in the Buddha's name. This "
            "reading guide notes the requirement as the text states it, "
            "without softening its implication that this was a known, "
            "named concern."]),
        ("Seniority as a floor, not a substitute", [
            "The eighth and final requirement, twenty years of ordination, "
            "functions as a floor rather than a sufficient qualification "
            "on its own &mdash; it closes a list where ethical conduct, "
            "learning, communication skill, and a clean disciplinary "
            "record all come first, suggesting seniority alone was not "
            "considered adequate grounds for this responsibility."]),
    ],
    terms=[
        ("bhikkhunovādako",
         "&ldquo;an adviser for nuns&rdquo; &mdash; this discourse's own "
         "title-role, the qualification Ānanda's question concerns."),
        ("ubhayāni kho panassa pātimokkhāni vitthārena svāgatāni honti",
         "&ldquo;both monastic codes have been passed down to them in "
         "detail&rdquo; &mdash; the third quality, requiring mastery of "
         "both the monks' and the nuns' own codes of discipline."),
        ("bhikkhunisaṅghassa piyo hoti manāpo",
         "&ldquo;likable and agreeable to most of the nuns&rdquo; &mdash; "
         "the sixth quality, requiring the community's own regard, not "
         "merely formal qualification."),
        ("na ca pubbe ocarakaṁ katvā gahitapubbo hoti kāsāyavatthavasanāya",
         "&ldquo;never previously sexually harassed any woman wearing the "
         "ocher robe who has gone forth&rdquo; &mdash; the seventh and "
         "most specific quality, an explicit disciplinary requirement."),
        ("vīsativassavāsī vā atirekavīsativassavāsī vā",
         "&ldquo;ordained for twenty years or more&rdquo; &mdash; the "
         "eighth and final requirement, a seniority floor closing the "
         "list."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's question and the eight "
        "qualifications the Buddha names in answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda's question, and eight qualifications"),
        ("p", "&sect;1", "an8.52:1.1-2.11"),
    ],
    quiz=[
        {"q": "What question does Ānanda bring to the Buddha in this "
              "discourse?",
         "opts": [
             "How many nuns should be ordained at once",
             "How many qualities a monk needs to be deemed an adviser for "
             "nuns",
             "Whether nuns should be allowed to travel alone",
             "How the sabbath should be observed"],
         "correct": 1,
         "expl": "A practical question following directly from AN 8.51's "
                 "account of the order's founding."},
        {"q": "Why does the guide describe this discourse's question as "
              "urgent given its placement after AN 8.51?",
         "opts": [
             "There is no particular connection between the two",
             "AN 8.51's own garudhamma make nuns dependent on the monks' "
             "community for guidance, so who fills that role responsibly "
             "becomes a real practical question",
             "AN 8.51 is unrelated to monastic advising",
             "This discourse contradicts AN 8.51 entirely"],
         "correct": 1,
         "expl": "A structural follow-on addressing a concrete "
                 "implication of the previous discourse."},
        {"q": "What explicit disciplinary requirement appears among the "
              "eight qualities?",
         "opts": [
             "A vow of poverty",
             "Never having previously sexually harassed any woman who has "
             "gone forth in the Buddha's name",
             "Never having traveled outside the local region",
             "Never having taught a layperson"],
         "correct": 1,
         "expl": "A specific safeguard, stated plainly rather than "
                 "softened."},
        {"q": "What is the eighth and final requirement?",
         "opts": [
             "Physical strength", "Ordination for twenty years or more",
             "Wealth given to the Saṅgha", "Royal endorsement"],
         "correct": 1,
         "expl": "A seniority floor, closing a list where several other "
                 "qualities come first."},
        {"q": "According to the guide, what does the ordering of the eight "
              "qualities suggest about seniority alone?",
         "opts": [
             "That seniority alone was sufficient qualification",
             "That seniority functions as a floor, not a substitute for "
             "ethical conduct, learning, and a clean disciplinary record",
             "That seniority was irrelevant to the role",
             "That younger monks were preferred"],
         "correct": 1,
         "expl": "Twenty years closes the list, after several other "
                 "requirements come first."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kapilavatthu, at the Banyan Tree Monastery",
             "Vesālī, at the Great Wood, in the hall with the peaked roof",
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, on Vulture's Peak"],
         "correct": 1,
         "expl": "The same location as AN 8.51's own closing scene."},
    ],
    marginalia=[
        ("Eight qualifications", [
            "ethical, learned, versed",
            "in both monastic codes,",
            "articulate, well liked, senior",
        ]),
        ("A follow-on to AN 8.51", [
            "the garudhamma make nuns",
            "dependent on the monks' community —",
            "so who is fit to serve that role?",
        ]),
        ("A safeguard stated plainly", [
            "never having harassed",
            "any woman who has gone forth —",
            "a named, specific requirement",
        ]),
        ("Cross-references", [
            "AN 8.51 &middot; previous, the bhikkhunī order's own founding",
            "AN 8.53 &middot; next, from the earlier eighteen-page "
            "selection",
        ]),
    ],
    further=[
        '<a href="%s/an8.52/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.51.html">AN 8.51 &middot; With Gotamī</a> &mdash; previous.',
    ],
    next=("an-8.53.html", "AN 8.53 &middot; Brief Advice to Gotamī"),
)


# --------------------------------------------------------------------------- #
# AN 8.54 — Dīghajāṇusutta (Byagghapajjasutta). an-8.53.html (existing) sits
# before this discourse; splice in with explicit prev=, per the
# an-6.16/an-6.63/an-7.6 precedent.
# --------------------------------------------------------------------------- #
page(
    54, "Dīghajāṇu", "With Dīghajāṇu",
    vagga=VAGGA_6,
    meta_title="AN 8.54 — With Dīghajāṇu | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dīghajāṇusutta, one of the canon's most widely taught lay-ethics "
        "discourses: four qualities for worldly welfare — initiative, "
        "protection, good friendship, balanced finances — and four for "
        "welfare in future lives. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The land of the Koliyans, at a town named "
                    "Kakkarapatta"),
        ("Speakers", "Dīghajāṇu the Koliyan and the Buddha"),
        ("Form", "A direct request for practical lay teaching, answered "
                 "with two sets of four qualities, each explained with its "
                 "own simile, closing in verse"),
        ("Length", "~3 minutes to read"),
        ("One of the most widely taught lay discourses", "This teaching "
                                                          "on practical "
                                                          "livelihood and "
                                                          "ethics is among "
                                                          "the most "
                                                          "frequently cited "
                                                          "lay-ethics "
                                                          "discourses in "
                                                          "the modern "
                                                          "tradition, often "
                                                          "referenced in "
                                                          "discussions of "
                                                          "Buddhist "
                                                          "economics"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "practical and concrete, with two vivid similes "
                       "(the reservoir, the appraiser's scale)"),
    ],
    why=(
        "Dīghajāṇu, a layperson who enjoys sensual pleasures and household "
        "life, asks directly for teaching leading to welfare in this life "
        "and the next; the Buddha answers with four qualities for worldly "
        "success &mdash; initiative, protection of wealth, good "
        "friendship, and balanced finances &mdash; and four for spiritual "
        "success &mdash; faith, ethics, generosity, and wisdom."),
    guide=[
        ("The teaching in one sentence", [
            "Four qualities &mdash; earning a living through legitimate "
            "effort, protecting what's earned, keeping good company, and "
            "balancing income against expenditure &mdash; lead to welfare "
            "in this life, while four further qualities &mdash; faith, "
            "ethics, generosity, and wisdom &mdash; lead to welfare in "
            "future lives."]),
        ("A layperson's own honest self-description", [
            "Dīghajāṇu doesn't ask for monastic teaching; he opens by "
            "plainly describing his own life &mdash; enjoying sensual "
            "pleasures, living at home with children, wearing garlands "
            "and fragrance, accepting gold and currency &mdash; and asks "
            "for a Dhamma suited to exactly that life, not one that "
            "requires leaving it behind."]),
        ("Four this-life qualities, each with its own simile", [
            "Initiative means understanding one's own trade well enough to "
            "organize it competently. Protection means safeguarding "
            "legitimate wealth from rulers, bandits, fire, flood, and "
            "unloved heirs. Good friendship means associating with mature, "
            "accomplished people and emulating them. Balanced finances, "
            "illustrated by an appraiser's scale, means neither living "
            "beyond one's income like a &ldquo;fig-eater&rdquo; nor "
            "starving oneself through excessive frugality."]),
        ("A reservoir with four inlets and four drains", [
            "The discourse's central image compares wealth to a large "
            "reservoir: womanizing, drinking, gambling, and bad "
            "companionship are its four drains, while their opposites are "
            "its four inlets. The same four items appear as both threat "
            "and safeguard, framed entirely around whether the drains are "
            "open or closed. The four spiritual qualities that follow "
            "&mdash; faith, ethics, generosity, and wisdom &mdash; are the "
            "identical fourfold pattern already met at AN 8.49-50, applied "
            "here to a male householder rather than a woman."]),
    ],
    terms=[
        ("byagghapajja",
         "&ldquo;Byagghapajja&rdquo; &mdash; the name (or clan-name) the "
         "Buddha uses to address Dīghajāṇu, giving this discourse its "
         "alternate title, Byagghapajjasutta."),
        ("uṭṭhānasampadā, ārakkhasampadā, kalyāṇamittatā, "
         "samajīvitā",
         "&ldquo;accomplishment in initiative, protection, good "
         "friendship, and balanced finances&rdquo; &mdash; the four "
         "qualities for this-life welfare."),
        ("cattāri apāyamukhāni",
         "&ldquo;four drains&rdquo; on wealth &mdash; womanizing, "
         "drinking, gambling, and bad companionship &mdash; illustrated by "
         "a reservoir losing water faster than rain can replenish it."),
        ("nāccogāḷhaṁ nātihīnaṁ",
         "&ldquo;neither too extravagant nor too frugal&rdquo; &mdash; "
         "the standard for balanced finances, illustrated by an "
         "appraiser's scale."),
        ("saddhāsampadā, sīlasampadā, cāgasampadā, paññāsampadā",
         "&ldquo;accomplishment in faith, ethics, generosity, and "
         "wisdom&rdquo; &mdash; the four qualities for future-life "
         "welfare, the identical fourfold pattern met at AN 8.49-50."),
    ],
    text_intro=(
        "The discourse in full: Dīghajāṇu's request, four qualities for "
        "this life, four for future lives, and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Dīghajāṇu's request"),
        ("p", "&sect;1", "an8.54:1.1-1.4"),
        ("h3", "Four qualities for this life"),
        ("p", "&sect;2", "an8.54:2.1-5.8"),
        ("h3", "Four drains, and four inlets"),
        ("p", "&sect;3", "an8.54:6.1-8.1"),
        ("h3", "Four qualities for future lives"),
        ("p", "&sect;4", "an8.54:9.1-14.1"),
        ("h3", "Closing verses"),
        ("p", "&sect;5", "an8.54:15.1-18.4"),
    ],
    quiz=[
        {"q": "What does Dīghajāṇu ask for, and how does he frame his own "
              "life first?",
         "opts": [
             "He asks how to become a monk, describing his desire to "
             "renounce",
             "He asks for teaching suited to welfare in this life and the "
             "next, first plainly describing his own life of sensual "
             "enjoyment and household duties",
             "He asks for a magical charm",
             "He asks the Buddha to settle a legal dispute"],
         "correct": 1,
         "expl": "A request for a Dhamma suited to lay life, not one "
                 "requiring its abandonment."},
        {"q": "What are the four qualities for this-life welfare?",
         "opts": [
             "Wealth, status, education, and beauty",
             "Initiative, protection, good friendship, and balanced "
             "finances",
             "Faith, ethics, generosity, and wisdom",
             "Physical strength, courage, patience, and skill"],
         "correct": 1,
         "expl": "Practical qualities for livelihood and household "
                 "management."},
        {"q": "What four items function as both 'drains' and, in their "
              "opposite form, 'inlets' for wealth?",
         "opts": [
             "The five precepts",
             "Womanizing, drinking, gambling, and bad companionship — or "
             "their opposites",
             "Taxes, tithes, gifts, and loans",
             "The four noble truths"],
         "correct": 1,
         "expl": "A single fourfold item functioning as threat or "
                 "safeguard depending on direction."},
        {"q": "What image illustrates balanced finances?",
         "opts": [
             "A ship navigating a storm",
             "An appraiser's scale, showing whether something is 'low by "
             "this much or high by this much'",
             "A garden being watered",
             "A fire being tended"],
         "correct": 1,
         "expl": "Neither extravagant nor frugal, measured like weights on "
                 "a scale."},
        {"q": "How do the four future-life qualities relate to AN 8.49-50?",
         "opts": [
             "They are entirely unrelated",
             "They are the identical fourfold pattern — faith, ethics, "
             "generosity, wisdom — applied here to a male householder "
             "rather than a woman",
             "They contradict AN 8.49-50's teaching",
             "AN 8.49-50 has no comparable fourfold pattern"],
         "correct": 1,
         "expl": "The same saddhā/sīla/cāga/paññā-sampadā pattern, now "
                 "addressed to a man."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Kapilavatthu, at the Banyan Tree Monastery",
             "The land of the Koliyans, at a town named Kakkarapatta",
             "Vesālī, at the Great Wood",
             "Sāvatthī, in Jeta's Grove"],
         "correct": 1,
         "expl": "A location distinct from this chapter's earlier "
                 "discourses."},
    ],
    marginalia=[
        ("A life described plainly first", [
            "sensual pleasures, household,",
            "garlands, gold and currency —",
            "a Dhamma suited to exactly that",
        ]),
        ("Four qualities, four similes", [
            "initiative, protection,",
            "good friendship, balance —",
            "the appraiser's scale for finances",
        ]),
        ("A reservoir, drained or filled", [
            "womanizing, drink, gambling,",
            "bad company — the same four,",
            "as drains or, reversed, as inlets",
        ]),
        ("Cross-references", [
            "AN 8.53 &middot; previous, from the earlier eighteen-page "
            "selection",
            "AN 8.55 &middot; next, the same teaching addressed to a "
            "different brahmin",
        ]),
    ],
    further=[
        '<a href="%s/an8.54/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.53.html">AN 8.53 &middot; Brief Advice to Gotamī</a> &mdash; previous.',
        '<a href="an-8.55.html">AN 8.55 &middot; With Ujjaya</a> &mdash; next.',
    ],
    prev=("an-8.53.html", "AN 8.53 &middot; Brief Advice to Gotamī"),
)


# --------------------------------------------------------------------------- #
# AN 8.55 — Ujjayasutta
# --------------------------------------------------------------------------- #
page(
    55, "Ujjaya", "With Ujjaya",
    vagga=VAGGA_6,
    meta_title="AN 8.55 — With Ujjaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ujjayasutta, restating AN 8.54's eight qualities for welfare in "
        "this life and the next, this time for the brahmin Ujjaya as he "
        "prepares to travel abroad. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Ujjaya the brahmin and the Buddha"),
        ("Form", "The identical eight qualities as AN 8.54, addressed to a "
                 "different questioner with a different stated reason for "
                 "asking"),
        ("Length", "~3 minutes to read"),
        ("A traveler's question, not a householder's", "Where Dīghajāṇu "
                                                        "asked as someone "
                                                        "settled in "
                                                        "household life, "
                                                        "Ujjaya asks "
                                                        "because he is "
                                                        "about to travel "
                                                        "abroad — a "
                                                        "different "
                                                        "motivation "
                                                        "receiving the "
                                                        "identical answer"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical content to AN 8.54, best read as a "
                       "companion rather than new material"),
    ],
    why=(
        "The brahmin Ujjaya, preparing to travel abroad, asks the Buddha "
        "for the same teaching on welfare in this life and the next that "
        "Dīghajāṇu received at AN 8.54, and receives it word for word: "
        "four qualities for worldly welfare and four for welfare in future "
        "lives."),
    guide=[
        ("The teaching in one sentence", [
            "Ujjaya receives the identical eight qualities given to "
            "Dīghajāṇu at AN 8.54 &mdash; initiative, protection, good "
            "friendship, and balanced finances for this life; faith, "
            "ethics, generosity, and wisdom for future lives &mdash; "
            "prompted by his own upcoming journey abroad rather than a "
            "settled household life."]),
        ("A different stated reason, an identical answer", [
            "Ujjaya doesn't describe his lifestyle the way Dīghajāṇu did; "
            "instead, he states a specific practical reason for asking: "
            "&ldquo;we wish to travel abroad.&rdquo; The Buddha's answer "
            "doesn't adjust for this different circumstance at all "
            "&mdash; the same eight qualities apply whether one is "
            "settling into household life or setting out on a journey."]),
        ("No setting given, unlike AN 8.54", [
            "Where AN 8.54 opens with a specific location, the land of "
            "the Koliyans at Kakkarapatta, this discourse gives no "
            "setting at all, opening directly with Ujjaya's approach and "
            "question &mdash; one of several small differences in framing "
            "that don't affect the substance of the shared teaching."]),
        ("A teaching stable across different life circumstances", [
            "Read together, AN 8.54 and AN 8.55 make an implicit claim "
            "through repetition: these eight qualities aren't tailored to "
            "one particular life situation &mdash; settled household life, "
            "or travel and change &mdash; but hold as a stable foundation "
            "across different circumstances a layperson might actually "
            "face."]),
    ],
    terms=[
        ("ujjayo brāhmaṇo",
         "the brahmin Ujjaya, this discourse's own questioner, distinct "
         "from Dīghajāṇu the Koliyan at AN 8.54."),
        ("bāhirā gantukāmā",
         "&ldquo;we wish to travel abroad&rdquo; &mdash; Ujjaya's own "
         "stated reason for asking, absent from AN 8.54's version of the "
         "same request."),
        ("uṭṭhānasampadā, ārakkhasampadā, kalyāṇamittatā, "
         "samajīvitā",
         "the identical four this-life qualities named at AN 8.54, "
         "unchanged here."),
        ("cattāri apāyamukhāni",
         "the same four drains on wealth met at AN 8.54 &mdash; "
         "womanizing, drinking, gambling, and bad companionship &mdash; "
         "restated here without alteration."),
        ("saddhāsampadā, sīlasampadā, cāgasampadā, paññāsampadā",
         "the identical four future-life qualities as AN 8.54, closing "
         "this discourse's teaching unchanged."),
    ],
    text_intro=(
        "The discourse in full: the same eight qualities as AN 8.54, "
        "given to Ujjaya as he prepares to travel abroad. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ujjaya's request"),
        ("p", "&sect;1", "an8.55:1.1-1.4"),
        ("h3", "Four qualities for this life"),
        ("p", "&sect;2", "an8.55:2.1-6.8"),
        ("h3", "Four drains, and four inlets"),
        ("p", "&sect;3", "an8.55:7.1-9.1"),
        ("h3", "Four qualities for future lives"),
        ("p", "&sect;4", "an8.55:10.1-14.1"),
        ("h3", "Closing verses"),
        ("p", "&sect;5", "an8.55:15.1-18.4"),
    ],
    quiz=[
        {"q": "How does Ujjaya's stated reason for asking differ from "
              "Dīghajāṇu's at AN 8.54?",
         "opts": [
             "They are identical",
             "Ujjaya states a specific practical reason — he is about to "
             "travel abroad — where Dīghajāṇu described his settled "
             "household life",
             "Ujjaya doesn't give any reason at all",
             "Ujjaya asks a completely different question"],
         "correct": 1,
         "expl": "Different circumstances, prompting the same underlying "
                 "request."},
        {"q": "How does the Buddha's answer to Ujjaya compare to his "
              "answer to Dīghajāṇu?",
         "opts": [
             "Entirely different, adjusted for travel",
             "Word for word identical — the same eight qualities apply "
             "regardless of the specific life circumstance",
             "Shorter, omitting several qualities",
             "Contradictory in its core content"],
         "correct": 1,
         "expl": "A teaching that doesn't adjust for the different stated "
                 "motivation."},
        {"q": "What does this discourse omit that AN 8.54 includes?",
         "opts": [
             "The eight qualities themselves",
             "A stated setting — this discourse gives no location at all",
             "The closing verses",
             "The reservoir simile"],
         "correct": 1,
         "expl": "A bare opening with no location given, unlike AN 8.54's "
                 "named setting."},
        {"q": "According to the guide, what claim does the pairing of AN "
              "8.54 and AN 8.55 make through repetition?",
         "opts": [
             "That the teaching only applies to travelers",
             "That these eight qualities hold as a stable foundation "
             "across different life circumstances, not tailored to one "
             "particular situation",
             "That the two discourses actually contradict each other",
             "That only brahmins can benefit from this teaching"],
         "correct": 1,
         "expl": "A teaching whose stability across circumstances is the "
                 "pairing's implicit point."},
        {"q": "What are the four drains on wealth, restated here unchanged "
              "from AN 8.54?",
         "opts": [
             "Taxes, tithes, gifts, and loans",
             "Womanizing, drinking, gambling, and bad companionship",
             "Wealth, status, education, and beauty",
             "The four noble truths"],
         "correct": 1,
         "expl": "Identical to AN 8.54's own reservoir simile."},
        {"q": "Who asks the question in this discourse?",
         "opts": [
             "Dīghajāṇu the Koliyan", "The brahmin Ujjaya",
             "Mahāpajāpati Gotamī", "Venerable Ānanda"],
         "correct": 1,
         "expl": "A different questioner receiving the identical teaching."},
    ],
    marginalia=[
        ("A traveler's question", [
            "'we wish to travel abroad' —",
            "a different reason for asking,",
            "the identical eight qualities given",
        ]),
        ("No setting, unlike AN 8.54", [
            "no named location here —",
            "opening straight into",
            "Ujjaya's own request",
        ]),
        ("Stable across circumstances", [
            "settled household, or travel —",
            "the same eight qualities hold,",
            "not tailored to one situation",
        ]),
        ("Cross-references", [
            "AN 8.54 &middot; previous, the identical teaching for "
            "Dīghajāṇu",
            "AN 8.56 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an8.55/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.54.html">AN 8.54 &middot; With Dīghajāṇu</a> &mdash; previous.',
        '<a href="an-8.56.html">AN 8.56 &middot; Danger</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.56 — Ādīnavasutta
# --------------------------------------------------------------------------- #
page(
    56, "Ādīnava", "Danger",
    vagga=VAGGA_6,
    meta_title="AN 8.56 — Danger | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ādīnavasutta, eight terms for sensual pleasures — danger, "
        "suffering, disease, boil, dart, chain, bog, and womb — each "
        "explained through the ordinary person's continued bondage to "
        "rebirth. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight terms for sensual pleasures, each briefly "
                 "explained, closing in verse"),
        ("Length", "~1 minute to read"),
        ("A single register, eight synonyms", "Unlike this chapter's other "
                                              "eight-item lists, which name "
                                              "eight distinct factors or "
                                              "qualities, this discourse "
                                              "names eight different words "
                                              "for a single thing, each "
                                              "capturing a different facet "
                                              "of the same danger"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and image-rich, easy to read but worth sitting "
                       "with each term individually"),
    ],
    why=(
        "AN 8.56 names eight terms for sensual pleasures &mdash; danger, "
        "suffering, disease, boil, dart, chain, bog, and womb &mdash; "
        "explaining that someone besotted by sensual greed is not freed "
        "from these dangers, or from further rebirth, in this life or "
        "lives to come."),
    guide=[
        ("The teaching in one sentence", [
            "Danger, suffering, disease, boil, dart, chain, bog, and womb "
            "are all terms for sensual pleasures, because someone "
            "besotted by sensual greed and shackled by lustful desire is "
            "not freed from danger &mdash; or from further wombs, further "
            "rebirths &mdash; in this life or lives to come."]),
        ("Eight words, not eight separate things", [
            "Where most of this book's eight-item lists name eight "
            "distinct factors, qualities, or individuals, this discourse "
            "takes a different approach: eight different words applied to "
            "a single subject, sensual pleasure, each word illuminating a "
            "different aspect of why it's dangerous &mdash; acute pain "
            "(dart), chronic affliction (disease), entrapment (chain), "
            "and the cycle of rebirth itself (womb)."]),
        ("Womb, the term the discourse dwells on longest", [
            "Though all eight terms receive the identical explanatory "
            "formula, the discourse's own text singles out "
            "&ldquo;womb&rdquo; for explicit restatement, tying sensual "
            "greed directly to continued rebirth &mdash; not simply an "
            "unpleasant state to be endured, but the very mechanism that "
            "keeps the cycle of birth and death turning."]),
        ("A mendicant who transcends the swamp", [
            "The closing verses shift from diagnosis to contrast: where "
            "ordinary people remain swamped by what merely seems pleasant, "
            "a mendicant who is keen and doesn't forget awareness "
            "transcends this &ldquo;grueling swamp&rdquo; entirely, "
            "watching from outside as the wider population flounders in "
            "rebirth and old age."]),
    ],
    terms=[
        ("ādīnavo",
         "&ldquo;danger&rdquo; &mdash; this discourse's own title term "
         "and the first of the eight, explained through continued "
         "bondage to danger in this life and future lives."),
        ("gaṇḍo, sallaṁ",
         "&ldquo;boil, dart&rdquo; &mdash; two of the more viscerally "
         "physical terms in the list, images of festering affliction and "
         "acute, piercing pain."),
        ("palipo",
         "&ldquo;bog&rdquo; &mdash; a term evoking entrapment that "
         "worsens with struggle, a swamp one sinks deeper into by "
         "resisting incorrectly."),
        ("yoni",
         "&ldquo;womb&rdquo; &mdash; the eighth and final term, singled "
         "out by the discourse's own text for explicit restatement, tying "
         "sensual greed directly to the mechanism of continued rebirth."),
        ("taṁ padumaṁ atikkamma",
         "part of the closing verses' description of the mendicant who "
         "transcends &ldquo;this grueling swamp,&rdquo; watching the "
         "wider population flounder in rebirth and old age."),
    ],
    text_intro=(
        "The discourse in full: eight terms for sensual pleasures, and "
        "closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight terms for sensual pleasures"),
        ("p", "&sect;1", "an8.56:1.1-1.18"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.56:2.1-4.4"),
    ],
    quiz=[
        {"q": "What are the eight terms this discourse applies to sensual "
              "pleasures?",
         "opts": [
             "The five hindrances plus three more",
             "Danger, suffering, disease, boil, dart, chain, bog, and womb",
             "The seven factors of awakening plus one",
             "Eight kinds of physical illness"],
         "correct": 1,
         "expl": "Eight different words illuminating different facets of "
                 "the same underlying danger."},
        {"q": "How does this discourse's eightfold structure differ from "
              "most others in this book?",
         "opts": [
             "It is structurally identical to the rest",
             "It names eight different words for a single subject, rather "
             "than eight distinct factors or individuals",
             "It has no eightfold structure at all",
             "It lists eight unrelated topics"],
         "correct": 1,
         "expl": "Eight synonyms, not eight separate items."},
        {"q": "Which term does the discourse's own text single out for "
              "explicit restatement?",
         "opts": [
             "Disease", "Womb — tying sensual greed directly to continued "
                         "rebirth",
             "Boil", "Chain"],
         "correct": 1,
         "expl": "The mechanism keeping the cycle of birth and death "
                 "turning, not merely an unpleasant state."},
        {"q": "What happens to a mendicant who is keen and doesn't forget "
              "awareness, according to the closing verses?",
         "opts": [
             "They remain swamped like everyone else",
             "They transcend the 'grueling swamp' entirely, watching the "
             "wider population flounder in rebirth and old age",
             "They are punished for their effort",
             "Nothing changes for them"],
         "correct": 1,
         "expl": "A contrast between ordinary bondage and a mendicant's "
                 "own transcendence."},
        {"q": "Why is 'danger' explained as a term for sensual pleasures?",
         "opts": [
             "Because sensual pleasures are physically painful to enjoy",
             "Because someone besotted by sensual greed is not freed from "
             "dangers in this life or lives to come",
             "Because sensual pleasures are illegal",
             "No explanation is given"],
         "correct": 1,
         "expl": "The same explanatory formula applied to each of the "
                 "eight terms in turn."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Vesālī",
             "No setting is stated in the source", "Yes, at Rājagaha"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this book."},
    ],
    marginalia=[
        ("Eight words, one danger", [
            "danger, suffering, disease,",
            "boil, dart, chain, bog, womb —",
            "each a different facet",
        ]),
        ("Womb, singled out", [
            "the mechanism itself —",
            "sensual greed tied directly",
            "to the wheel of rebirth",
        ]),
        ("A mendicant transcends the swamp", [
            "keen, never forgetting awareness —",
            "watching from outside",
            "as the population flounders",
        ]),
        ("Cross-references", [
            "AN 8.55 &middot; previous, the same welfare teaching for a "
            "traveler",
            "AN 8.57 &middot; next, eight qualities worthy of offerings",
        ]),
    ],
    further=[
        '<a href="%s/an8.56/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.55.html">AN 8.55 &middot; With Ujjaya</a> &mdash; previous.',
        '<a href="an-8.57.html">AN 8.57 &middot; Worthy of Offerings Dedicated to the '
        "Gods (1st)</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.57 — Paṭhamaāhuneyyasutta
# --------------------------------------------------------------------------- #
page(
    57, "Paṭhamaāhuneyya", "Worthy of Offerings Dedicated to the Gods (1st)",
    vagga=VAGGA_6,
    meta_title="AN 8.57 — Worthy of Offerings Dedicated to the Gods (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaāhuneyyasutta, an eight-quality composite of the ethical, "
        "learned, well-connected mendicant crowned with the three "
        "knowledges of the awakening night, worthy of the highest offerings. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare eight-item list combining ethical, social, and "
                 "meditative qualities, closing with the three knowledges"),
        ("Length", "under 1 minute to read"),
        ("A composite built from earlier material", "Several of these "
                                                     "eight qualities "
                                                     "recombine elements "
                                                     "already met "
                                                     "separately elsewhere "
                                                     "in this book — the "
                                                     "arahant's three "
                                                     "knowledges echo AN "
                                                     "8.11's own first-"
                                                     "person account of "
                                                     "the awakening night"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "clear list, worth comparing closely with AN 8.58's "
                       "own different eight items"),
    ],
    why=(
        "AN 8.57 names eight qualities that make a mendicant worthy of the "
        "highest offerings &mdash; ethical restraint, deep learning, good "
        "friendship, right view, the four absorptions on demand, "
        "recollection of past lives, clairvoyant knowledge of other "
        "beings' rebirth, and the freedom of heart and wisdom that comes "
        "from ending the defilements."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant worthy of offerings dedicated to the gods "
            "combines ethical restraint, deep learning, good companionship, "
            "and right view with the four absorptions available at will, "
            "recollection of past lives, clairvoyant insight into other "
            "beings' rebirth, and complete freedom through the ending of "
            "defilements."]),
        ("Ethics and learning, this book's familiar foundation", [
            "The first two qualities &mdash; ethical restraint down to the "
            "slightest fault, and deep, well-retained learning of the "
            "teachings &mdash; are the same foundational pair this book "
            "has met repeatedly, here forming the base of a list that "
            "builds upward toward full awakening."]),
        ("Two social and doctrinal qualities, before the meditative core", [
            "Between the ethical foundation and the meditative "
            "attainments, this list inserts two qualities not always "
            "paired together elsewhere: good friends, companions, and "
            "associates, and right view with a right perspective &mdash; "
            "social and doctrinal grounding, positioned deliberately "
            "before the list turns to meditation."]),
        ("Three knowledges, echoing AN 8.11's own account", [
            "The final three items &mdash; the four absorptions, "
            "recollection of past lives, and clairvoyant knowledge of "
            "other beings' rebirth according to their deeds &mdash; "
            "together with the closing freedom through ending the "
            "defilements, recombine the same three knowledges the Buddha "
            "described in his own first-person voice at AN 8.11, now "
            "given as a general qualification rather than a personal "
            "account."]),
    ],
    terms=[
        ("kalyāṇamitto",
         "&ldquo;has good friends&rdquo; &mdash; the third quality, "
         "social grounding positioned between ethical foundation and "
         "meditative attainment."),
        ("sammādiṭṭhi hoti ujuppaṭipanno",
         "&ldquo;has right view, possessing right perspective&rdquo; "
         "&mdash; the fourth quality, doctrinal orientation preceding the "
         "list's meditative core."),
        ("catunnaṁ jhānānaṁ ābhicetasikānaṁ diṭṭhadhammasukhavihārānaṁ "
         "nikāmalābhī",
         "&ldquo;gets the four absorptions... when they want, without "
         "trouble or difficulty&rdquo; &mdash; the fifth quality, "
         "meditative mastery available on demand."),
        ("anekavihitaṁ pubbenivāsaṁ anussarati",
         "&ldquo;recollects many kinds of past lives&rdquo; &mdash; the "
         "sixth quality, the first of the three knowledges echoing AN "
         "8.11's own account."),
        ("āsavānaṁ khayā anāsavaṁ cetovimuttiṁ paññāvimuttiṁ",
         "&ldquo;the undefiled freedom of heart and freedom by "
         "wisdom&rdquo; through the ending of defilements &mdash; the "
         "eighth and closing quality."),
    ],
    text_intro=(
        "The discourse in full: eight qualities of a mendicant worthy of "
        "offerings dedicated to the gods. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight qualities worthy of the highest offerings"),
        ("p", "&sect;1", "an8.57:1.1-1.11"),
    ],
    quiz=[
        {"q": "What are the first two qualities in this discourse's list?",
         "opts": [
             "Wealth and social status",
             "Ethical restraint down to the slightest fault, and deep, "
             "well-retained learning of the teachings",
             "Physical strength and courage",
             "Skill in debate and public speaking"],
         "correct": 1,
         "expl": "This book's familiar foundational pair, met repeatedly "
                 "elsewhere."},
        {"q": "What two qualities does this list insert between the "
              "ethical foundation and the meditative attainments?",
         "opts": [
             "Wealth and fame", "Good friendship and right view",
             "Physical beauty and eloquence", "Royal connections and "
                                               "political influence"],
         "correct": 1,
         "expl": "Social and doctrinal grounding, positioned deliberately "
                 "before the meditative core."},
        {"q": "What do the final three items of this list echo?",
         "opts": [
             "Nothing from elsewhere in this book",
             "The same three knowledges the Buddha described in his own "
             "first-person account at AN 8.11",
             "AN 8.5's eight worldly conditions",
             "AN 8.15's eight stains"],
         "correct": 1,
         "expl": "A recombination of the awakening-night knowledges, now "
                 "given as a general qualification."},
        {"q": "What does the fifth quality describe?",
         "opts": [
             "Physical endurance",
             "Getting the four absorptions when wanted, without trouble "
             "or difficulty",
             "Wealth accumulation",
             "Skill in argument"],
         "correct": 1,
         "expl": "Meditative mastery available on demand, not merely "
                 "occasional attainment."},
        {"q": "What closes the list of eight qualities?",
         "opts": [
             "Wealth and generosity",
             "The undefiled freedom of heart and wisdom through the "
             "ending of defilements",
             "Physical beauty",
             "Royal endorsement"],
         "correct": 1,
         "expl": "Complete freedom, the culmination of the eight "
                 "qualities."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this book."},
    ],
    marginalia=[
        ("Ethics and learning, first", [
            "the same foundational pair",
            "this book has met before —",
            "the base of a list building upward",
        ]),
        ("Friendship and view, between", [
            "social and doctrinal grounding,",
            "positioned deliberately",
            "before the meditative core",
        ]),
        ("Three knowledges, recombined", [
            "past lives, others' rebirth,",
            "freedom through ending defilements —",
            "echoing AN 8.11's own account",
        ]),
        ("Cross-references", [
            "AN 8.56 &middot; previous, eight terms for sensual pleasures",
            "AN 8.58 &middot; next, a different eight qualities for the "
            "same worthiness",
        ]),
    ],
    further=[
        '<a href="%s/an8.57/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.56.html">AN 8.56 &middot; Danger</a> &mdash; previous.',
        '<a href="an-8.58.html">AN 8.58 &middot; Worthy of Offerings Dedicated to the '
        "Gods (2nd)</a> &mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.58 — Dutiyaāhuneyyasutta
# --------------------------------------------------------------------------- #
page(
    58, "Dutiyaāhuneyya", "Worthy of Offerings Dedicated to the Gods (2nd)",
    vagga=VAGGA_6,
    meta_title="AN 8.58 — Worthy of Offerings Dedicated to the Gods (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaāhuneyyasutta, a second, more forest-ascetic set of eight "
        "qualities worthy of the highest offerings — energy, wilderness "
        "dwelling, and mastery of fear — sharing only its opening and "
        "closing items with AN 8.57. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A second eight-item list for the same worthiness, "
                 "sharing its ethical and meditative bookends with AN 8.57 "
                 "but replacing the middle four qualities entirely"),
        ("Length", "under 1 minute to read"),
        ("A different register from AN 8.57", "Where AN 8.57 built toward "
                                              "worthiness through "
                                              "friendship, view, and the "
                                              "three knowledges, this "
                                              "discourse builds toward it "
                                              "through energy, solitary "
                                              "forest dwelling, and "
                                              "mastery over desire and "
                                              "fear — a forest-ascetic "
                                              "register rather than a "
                                              "socially and doctrinally "
                                              "grounded one"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; best "
                       "read directly alongside AN 8.57 to see exactly "
                       "which items change"),
    ],
    why=(
        "AN 8.58 names a second set of eight qualities for the same "
        "worthiness described at AN 8.57 &mdash; ethical restraint and "
        "deep learning as before, but now roused energy, wilderness "
        "dwelling, mastery over desire and discontent, mastery over fear "
        "and dread, the four absorptions, and freedom through ending the "
        "defilements."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant worthy of offerings dedicated to the gods can "
            "also be described through a different eight qualities: "
            "ethical restraint and deep learning as before, then roused "
            "energy, wilderness dwelling, mastery over desire and "
            "discontent, mastery over fear and dread, the four "
            "absorptions on demand, and freedom through ending the "
            "defilements."]),
        ("The same bookends, a different middle", [
            "This discourse shares its first two qualities (ethical "
            "restraint, deep learning) and its meditative bookend items "
            "(the four absorptions, final freedom) with AN 8.57 nearly "
            "word for word. What changes entirely is the middle: where AN "
            "8.57 inserted friendship, right view, and two of the three "
            "knowledges, this discourse inserts energy, solitude, and "
            "mastery over two specific internal obstacles."]),
        ("A forest-ascetic profile", [
            "Wilderness dwelling in remote lodgings, mastery over desire "
            "and discontent, and mastery over fear and dread together "
            "sketch a recognizably different figure than AN 8.57's "
            "socially embedded, doctrinally grounded mendicant &mdash; "
            "someone whose worthiness comes through solitary struggle "
            "with specific internal obstacles rather than through "
            "companionship and view."]),
        ("Two paths to the same worthiness, not a contradiction", [
            "Read together, AN 8.57 and AN 8.58 don't compete for which "
            "eight qualities are the &ldquo;real&rdquo; requirement; they "
            "offer two different composite profiles &mdash; one social "
            "and doctrinal, one solitary and ascetic &mdash; both landing "
            "on the identical worthiness through different combinations "
            "of qualities."]),
    ],
    terms=[
        ("āraddhavīriyo",
         "&ldquo;lives with energy roused up&rdquo; &mdash; the third "
         "quality in this discourse's own version, replacing AN 8.57's "
         "good friendship at the same position."),
        ("araññavanapatthāni pantāni senāsanāni paṭisevati",
         "&ldquo;lives in the wilderness, in remote lodgings&rdquo; "
         "&mdash; the fourth quality, physical solitude replacing AN "
         "8.57's right view."),
        ("chandaṁ abhibhuyya viharati, na chandena abhibhūyati",
         "&ldquo;prevails over desire and discontent&rdquo; &mdash; the "
         "fifth quality, mastery over an internal obstacle rather than an "
         "external social or doctrinal grounding."),
        ("bhayabheravaṁ abhibhuyya viharati",
         "&ldquo;prevails over fear and dread&rdquo; &mdash; the sixth "
         "quality, a second internal mastery distinctive to this "
         "discourse's own list."),
        ("catunnaṁ jhānānaṁ ābhicetasikānaṁ",
         "the four absorptions, shared word for word with AN 8.57 at the "
         "same position in both lists."),
    ],
    text_intro=(
        "The discourse in full: a second set of eight qualities worthy of "
        "the highest offerings. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight qualities worthy of the highest offerings"),
        ("p", "&sect;1", "an8.58:1.1-1.11"),
    ],
    quiz=[
        {"q": "Which two qualities does this discourse share nearly word "
              "for word with AN 8.57?",
         "opts": [
             "Right view and good friendship",
             "Ethical restraint and deep learning, at the opening",
             "Wilderness dwelling and mastery of fear",
             "Nothing is shared between the two discourses"],
         "correct": 1,
         "expl": "The same foundational pair opening both discourses' "
                 "lists."},
        {"q": "What replaces AN 8.57's 'good friendship' and 'right view' "
              "at the same positions in this discourse's list?",
         "opts": [
             "Wealth and social status",
             "Roused energy and wilderness dwelling in remote lodgings",
             "Physical beauty and eloquence",
             "Royal patronage and political influence"],
         "correct": 1,
         "expl": "A shift from social/doctrinal grounding to energy and "
                 "solitude."},
        {"q": "What two internal obstacles does this discourse's fifth and "
              "sixth quality describe mastering?",
         "opts": [
             "Hunger and thirst",
             "Desire and discontent, then fear and dread",
             "Anger and pride",
             "Doubt and restlessness"],
         "correct": 1,
         "expl": "Qualities distinctive to this discourse's own forest-"
                 "ascetic profile."},
        {"q": "According to the guide, how should AN 8.57 and AN 8.58 be "
              "understood together?",
         "opts": [
             "As contradicting each other about the 'real' requirement",
             "As two different composite profiles — social/doctrinal and "
             "solitary/ascetic — both landing on the identical worthiness",
             "As the same discourse repeated without variation",
             "As entirely unrelated teachings"],
         "correct": 1,
         "expl": "Two paths to the same worthiness, not competing claims."},
        {"q": "What do this discourse and AN 8.57 share at their closing "
              "position?",
         "opts": [
             "Nothing; the endings are entirely different",
             "The four absorptions and freedom through ending the "
             "defilements",
             "A description of physical appearance",
             "A list of monastic requisites"],
         "correct": 1,
         "expl": "The same meditative bookend, word for word, closing both "
                 "lists."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.57's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("Same bookends, different middle", [
            "ethics, learning — shared —",
            "then energy, solitude,",
            "mastery of desire and fear",
        ]),
        ("A forest-ascetic profile", [
            "remote lodgings, roused energy,",
            "prevailing over fear and dread —",
            "a different figure than AN 8.57's",
        ]),
        ("Two paths, one worthiness", [
            "social and doctrinal, or",
            "solitary and ascetic —",
            "both reaching the same field of merit",
        ]),
        ("Cross-references", [
            "AN 8.57 &middot; previous, the first set of eight qualities "
            "for this worthiness",
            "AN 8.59 &middot; next, the eight individuals of the noble "
            "Saṅgha",
        ]),
    ],
    further=[
        '<a href="%s/an8.58/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.57.html">AN 8.57 &middot; Worthy of Offerings Dedicated to the '
        "Gods (1st)</a> &mdash; previous.",
        '<a href="an-8.59.html">AN 8.59 &middot; Eight Individuals (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.59 — Paṭhamapuggalasutta
# --------------------------------------------------------------------------- #
page(
    59, "Paṭhamapuggala", "Eight Individuals (1st)",
    vagga=VAGGA_6,
    meta_title="AN 8.59 — Eight Individuals (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamapuggalasutta, naming the eight individuals of the noble "
        "Saṅgha — four pairs, path and fruit, from stream-enterer through "
        "the perfected one — worthy of the highest offerings. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare naming of eight individuals in four pairs, "
                 "closing in two verses"),
        ("Length", "under 1 minute to read"),
        ("Individuals, not qualities", "Unlike AN 8.57 and 8.58's "
                                       "composite lists of qualities in a "
                                       "single mendicant, this discourse "
                                       "names eight distinct kinds of "
                                       "person, forming the traditional "
                                       "eightfold noble Saṅgha"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and structurally clear, a foundational list in "
                       "this tradition"),
    ],
    why=(
        "AN 8.59 names the eight individuals of the noble Saṅgha, worthy "
        "of the highest offerings: the stream-enterer and the one "
        "practicing to realize that fruit, the once-returner and the one "
        "practicing toward it, the non-returner and the one practicing "
        "toward it, and the perfected one and the one practicing for "
        "perfection."),
    guide=[
        ("The teaching in one sentence", [
            "The eight individuals worthy of the highest offerings are "
            "four pairs &mdash; each combining someone who has realized a "
            "fruit of the path with someone practicing to realize that "
            "same fruit &mdash; spanning from stream-entry through "
            "complete perfection, together forming the traditional "
            "eightfold noble Saṅgha."]),
        ("Four fruits, doubled into eight", [
            "Rather than naming four attainments, this discourse doubles "
            "each one: the stream-enterer themselves, and separately, the "
            "one still practicing to realize stream-entry; likewise for "
            "once-return, non-return, and full perfection. The doubling "
            "recognizes practice itself, not only its completion, as part "
            "of what makes the Saṅgha worthy."]),
        ("A community defined by attainment, not institution", [
            "This eightfold classification cuts across any formal "
            "monastic hierarchy or seniority &mdash; it sorts people by "
            "what they have realized or are actively realizing on the "
            "path, not by ordination date, robe color, or administrative "
            "role, a genuinely different axis of organization than most "
            "of this book's other lists."]),
        ("Closing verses: the upright Saṅgha", [
            "The closing verses name this eightfold group directly as "
            "&ldquo;the upright Saṅgha, with wisdom, ethics, and "
            "immersion,&rdquo; and declare that whatever merit-seeking "
            "humans offer to this Saṅgha specifically is very fruitful "
            "&mdash; grounding the whole discourse's practical purpose in "
            "identifying who is worth giving to."]),
    ],
    terms=[
        ("aṭṭha puggalā",
         "&ldquo;eight individuals&rdquo; &mdash; this discourse's own "
         "title-phrase, the traditional eightfold classification of the "
         "noble Saṅgha."),
        ("sotāpanno, sotāpattiphalasacchikiriyāya paṭipanno",
         "&ldquo;the stream-enterer and the one practicing to realize the "
         "fruit of stream-entry&rdquo; &mdash; the first pair, combining "
         "attainment and active practice."),
        ("anāgāmī, anāgāmiphalasacchikiriyāya paṭipanno",
         "&ldquo;the non-returner and the one practicing to realize the "
         "fruit of non-return&rdquo; &mdash; the third pair in the "
         "ascending sequence."),
        ("arahā, arahattāya paṭipanno",
         "&ldquo;the perfected one, and the one practicing for "
         "perfection&rdquo; &mdash; the fourth and highest pair, closing "
         "the eightfold sequence."),
        ("ujubhūtaṁ sāṅghaṁ, paññāsīlasamāhitaṁ",
         "&ldquo;the upright Saṅgha, with wisdom, ethics, and "
         "immersion&rdquo; &mdash; the closing verses' own name for this "
         "eightfold community of individuals."),
    ],
    text_intro=(
        "The discourse in full: the eight individuals of the noble Saṅgha, "
        "and closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight individuals, four pairs"),
        ("p", "&sect;1", "an8.59:1.1-1.4"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.59:2.1-3.4"),
    ],
    quiz=[
        {"q": "How does this discourse structure its eight individuals?",
         "opts": [
             "As eight unrelated types with no pairing",
             "As four pairs — each combining someone who has realized a "
             "fruit with someone practicing to realize that same fruit",
             "As a single continuous hierarchy with no grouping",
             "As eight qualities in one mendicant"],
         "correct": 1,
         "expl": "A doubling of four fruits into eight, recognizing "
                 "practice as well as attainment."},
        {"q": "How does this discourse's approach differ from AN 8.57 and "
              "8.58?",
         "opts": [
             "It is structurally identical to both",
             "It names eight distinct individuals rather than eight "
             "qualities combined in a single mendicant",
             "It has no eightfold structure at all",
             "It contradicts AN 8.57 and 8.58's teaching"],
         "correct": 1,
         "expl": "A different axis of organization: individuals, not "
                 "composite qualities."},
        {"q": "According to the guide, what axis does this eightfold "
              "classification sort people by?",
         "opts": [
             "Ordination date and seniority",
             "What they have realized or are actively realizing on the "
             "path, cutting across formal monastic hierarchy",
             "Robe color and administrative role",
             "Physical location within the monastery"],
         "correct": 1,
         "expl": "A community defined by attainment, not institutional "
                 "position."},
        {"q": "What do the closing verses call this eightfold group?",
         "opts": [
             "The wandering ascetics",
             "The upright Saṅgha, with wisdom, ethics, and immersion",
             "The royal court", "The merchant guild"],
         "correct": 1,
         "expl": "A direct naming, grounding the discourse's practical "
                 "purpose."},
        {"q": "What is the fourth and highest pair in the sequence?",
         "opts": [
             "The stream-enterer and the one practicing toward it",
             "The perfected one, and the one practicing for perfection",
             "The once-returner and the one practicing toward it",
             "The non-returner and the one practicing toward it"],
         "correct": 1,
         "expl": "Closing the ascending sequence of four pairs."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this book."},
    ],
    marginalia=[
        ("Four fruits, doubled to eight", [
            "stream-entry, once-return,",
            "non-return, perfection —",
            "each paired with active practice",
        ]),
        ("Attainment, not institution", [
            "not sorted by ordination date",
            "or robe color or role —",
            "but by what's realized on the path",
        ]),
        ("The upright Saṅgha", [
            "wisdom, ethics, immersion —",
            "what's given here is very fruitful,",
            "the closing verses declare",
        ]),
        ("Cross-references", [
            "AN 8.58 &middot; previous, a second composite of qualities "
            "for the same worthiness",
            "AN 8.60 &middot; next, the same eight individuals restated, "
            "closing this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an8.59/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.58.html">AN 8.58 &middot; Worthy of Offerings Dedicated to the '
        "Gods (2nd)</a> &mdash; previous.",
        '<a href="an-8.60.html">AN 8.60 &middot; Eight Individuals (2nd)</a> &mdash; next, '
        "closing this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.60 — Dutiyapuggalasutta — closes ch.6 Gotamīvagga
# --------------------------------------------------------------------------- #
page(
    60, "Dutiyapuggala", "Eight Individuals (2nd)",
    vagga=VAGGA_6,
    meta_title="AN 8.60 — Eight Individuals (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyapuggalasutta, restating AN 8.59's eight individuals with a "
        "small change in the closing verses — 'the exalted Saṅgha' rather "
        "than 'the upright Saṅgha' — closing this chapter. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical eight individuals as AN 8.59, with a "
                 "small variation in the closing verses"),
        ("Length", "under 1 minute to read"),
        ("A small but genuine variation", "Where AN 8.59's verses call "
                                          "this group &ldquo;the upright "
                                          "Saṅgha,&rdquo; this discourse "
                                          "calls it &ldquo;the exalted "
                                          "Saṅgha, the eight individuals "
                                          "among sentient beings&rdquo; "
                                          "&mdash; a genuine, if minor, "
                                          "difference worth noticing rather "
                                          "than assuming the two "
                                          "discourses are identical in "
                                          "every word"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, "
                       "best read directly alongside AN 8.59"),
    ],
    why=(
        "AN 8.60 restates the same eight individuals of the noble Saṅgha "
        "met at AN 8.59, closing this chapter with verses that call the "
        "same group &ldquo;the exalted Saṅgha&rdquo; rather than "
        "&ldquo;the upright Saṅgha,&rdquo; a small but genuine variation "
        "worth reading closely rather than assuming away."),
    guide=[
        ("The teaching in one sentence", [
            "The same eight individuals as AN 8.59 &mdash; four pairs "
            "spanning stream-entry through perfection, each combining "
            "attainment with active practice &mdash; are restated here, "
            "closing this chapter with a slightly different closing "
            "verse."]),
        ("The prose, identical", [
            "The prose portion of this discourse matches AN 8.59 word for "
            "word: the same four pairs, the same standing description of "
            "worthiness, the same closing statement naming all eight "
            "together as worthy of offerings, hospitality, religious "
            "donation, and veneration."]),
        ("The verses, genuinely different", [
            "Where AN 8.59's closing verse calls this group &ldquo;the "
            "upright Saṅgha, with wisdom, ethics, and immersion,&rdquo; "
            "this discourse's verse instead calls it &ldquo;the exalted "
            "Saṅgha, the eight individuals among sentient beings&rdquo; "
            "&mdash; a real variation in wording and emphasis, not simply "
            "a repeated line."]),
        ("Closing this chapter on a note of worthiness", [
            "This discourse closes Gotamīvagga on a discourse type this "
            "chapter has returned to twice already (AN 8.57, 8.58): "
            "identifying who or what is worthy of the highest offerings "
            "&mdash; here landing on the noble Saṅgha itself as a "
            "collective, rather than on any single mendicant's composite "
            "qualities."]),
    ],
    terms=[
        ("aṭṭha puggalā",
         "&ldquo;eight individuals&rdquo; &mdash; the identical subject "
         "as AN 8.59, unchanged in this discourse's own prose."),
        ("sotāpanno ... arahattāya paṭipanno",
         "the same four pairs as AN 8.59, from the stream-enterer through "
         "the one practicing for perfection, restated word for word."),
        ("ujubhūtaṁ sāṅghaṁ",
         "&ldquo;the upright Saṅgha&rdquo; &mdash; AN 8.59's own closing "
         "phrase, the point of comparison for this discourse's own "
         "variation."),
        ("uttamaṁ sāṅghaṁ, aṭṭha ca puggalā dhammadasā",
         "&ldquo;the exalted Saṅgha, the eight individuals among sentient "
         "beings&rdquo; &mdash; this discourse's own closing phrase, "
         "genuinely different from AN 8.59's wording."),
        ("Dutiyapaṇṇāsakaṁ",
         "&ldquo;the Second Fifty&rdquo; &mdash; the division this "
         "discourse belongs to, having opened at AN 8.51, now closing its "
         "first chapter, Gotamīvagga."),
    ],
    text_intro=(
        "The discourse in full: the same eight individuals as AN 8.59, "
        "with a genuinely different closing verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight individuals, four pairs"),
        ("p", "&sect;1", "an8.60:1.1-1.4"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.60:2.1-3.4"),
    ],
    quiz=[
        {"q": "How does this discourse's prose compare to AN 8.59's?",
         "opts": [
             "Entirely different content",
             "Word for word identical — the same four pairs and the same "
             "standing description of worthiness",
             "A shortened summary",
             "Contradictory in its core claims"],
         "correct": 1,
         "expl": "An exact match in prose, with the variation appearing "
                 "only in the closing verses."},
        {"q": "What does AN 8.59's closing verse call the eightfold group, "
              "compared to this discourse's own verse?",
         "opts": [
             "Both use identical wording",
             "AN 8.59 calls it 'the upright Saṅgha'; this discourse calls "
             "it 'the exalted Saṅgha, the eight individuals among "
             "sentient beings'",
             "AN 8.59 doesn't name the group at all",
             "This discourse omits any closing verse"],
         "correct": 1,
         "expl": "A genuine, if minor, variation worth noticing rather "
                 "than assuming away."},
        {"q": "What does this discourse close?",
         "opts": [
             "Nothing in particular",
             "Gotamīvagga, this chapter of the Second Fifty",
             "The entire Book of the Eights",
             "Only a single paragraph"],
         "correct": 1,
         "expl": "The sixth chapter of the Eights, opened at AN 8.51."},
        {"q": "How many times has this chapter addressed the theme of who "
              "is worthy of the highest offerings?",
         "opts": [
             "Once, only in this discourse",
             "Three times — AN 8.57, 8.58, and this discourse, each with a "
             "different approach",
             "Never; this is unrelated to that theme",
             "Ten times"],
         "correct": 1,
         "expl": "A recurring theme in this chapter, approached through "
                 "composite qualities and then individual attainment."},
        {"q": "What is the fourth pair in the sequence, shared with AN "
              "8.59?",
         "opts": [
             "The stream-enterer and the one practicing toward it",
             "The perfected one, and the one practicing for perfection",
             "The once-returner and the one practicing toward it",
             "The non-returner and the one practicing toward it"],
         "correct": 1,
         "expl": "The identical closing pair as AN 8.59's own sequence."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.59's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("Identical prose", [
            "the same four pairs,",
            "word for word as AN 8.59 —",
            "the variation comes later",
        ]),
        ("A different closing verse", [
            "'the upright Saṅgha' becomes",
            "'the exalted Saṅgha' here —",
            "a real, if small, variation",
        ]),
        ("Closing this chapter", [
            "a third return to worthiness —",
            "after AN 8.57, 8.58 —",
            "now the noble Saṅgha as a whole",
        ]),
        ("Cross-references", [
            "AN 8.59 &middot; previous, the same eight individuals with a "
            "different closing verse",
            "AN 8.51 &middot; earlier, opening this chapter with the "
            "bhikkhunī order's own founding",
        ]),
    ],
    further=[
        '<a href="%s/an8.60/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.59.html">AN 8.59 &middot; Eight Individuals (1st)</a> &mdash; previous.',
        '<a href="an-8.51.html">AN 8.51 &middot; With Gotamī</a> &mdash; earlier, opening '
        "this chapter.",
    ],
)


VAGGA_7 = "<em>Bhūmicālavagga</em> &mdash; the seventh chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.61 — Icchāsutta -- opens ch.7 Bhūmicālavagga
# --------------------------------------------------------------------------- #
page(
    61, "Icchā", "Desire",
    vagga=VAGGA_7,
    meta_title="AN 8.61 — Desire | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Icchāsutta, opening a new chapter with eight individuals sorted "
        "by a combinatorial matrix — trying or not for material things, "
        "getting or not getting them, reacting badly or well — only the "
        "reaction itself deciding who has fallen from the true teaching. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A combinatorial matrix of eight individuals, crossing "
                 "effort, outcome, and reaction, each spelled out in full "
                 "despite the repeating pattern"),
        ("Length", "~3 minutes to read"),
        ("Reaction is the only variable that matters", "Of the three axes "
                                                        "crossed in this "
                                                        "matrix — whether "
                                                        "one tries, "
                                                        "whether one gets, "
                                                        "and how one "
                                                        "reacts — only the "
                                                        "third actually "
                                                        "determines "
                                                        "whether someone "
                                                        "has fallen from "
                                                        "the true teaching"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "repetitive by design; the combinatorial structure "
                       "rewards mapping out all eight cases explicitly"),
    ],
    why=(
        "AN 8.61 opens a new chapter by naming eight individuals found in "
        "the world, sorted by crossing whether a secluded mendicant tries "
        "for material things, whether those things actually come, and "
        "whether the mendicant then reacts with sorrow or indulgence "
        "&mdash; with only the reaction itself, not the trying or the "
        "getting, determining whether that individual has fallen from the "
        "true teaching."),
    guide=[
        ("The teaching in one sentence", [
            "Whether a secluded mendicant tries for material things or "
            "not, and whether those things come or not, doesn't itself "
            "decide whether they've fallen from the true teaching &mdash; "
            "only their reaction does: sorrow at not getting, or "
            "indulgent negligence at getting, marks a fall, while equanimity "
            "in either outcome does not."]),
        ("A matrix, not a simple list", [
            "This discourse crosses three variables &mdash; trying or not "
            "trying, getting or not getting, reacting badly or well "
            "&mdash; producing eight individuals rather than eight "
            "independent qualities. The first four combinations all react "
            "badly (sorrow when unsuccessful, indulgence when successful) "
            "and are declared fallen; the identical four combinations of "
            "trying and getting, but reacting with equanimity instead, "
            "are declared not fallen."]),
        ("Trying and getting turn out not to matter", [
            "The discourse's real point emerges only once all eight cases "
            "are laid out side by side: whether someone tries hard for "
            "material things, and whether those things actually arrive, "
            "make no difference at all to whether they've fallen from the "
            "true teaching. A mendicant who tries and fails but stays "
            "equanimous hasn't fallen; a mendicant who never even tries "
            "but sorrows anyway when nothing comes has."]),
        ("Reaction as the single load-bearing variable", [
            "Read as a complete set, these eight cases isolate reaction "
            "&mdash; sorrow and indulgence versus equanimity &mdash; as "
            "the only variable that actually determines spiritual "
            "standing. Effort and outcome are real, and both are named "
            "explicitly in every one of the eight cases, but neither one "
            "is what the discourse is actually testing for."]),
    ],
    terms=[
        ("paṭisallīno viharanto",
         "&ldquo;stays secluded, living independently&rdquo; &mdash; the "
         "shared starting condition of all eight individuals, before their "
         "differing effort, outcome, and reaction."),
        ("vāyamati, ussahati, vāyamaṁ karoti",
         "&ldquo;tries hard, strives, and makes an effort&rdquo; &mdash; "
         "the first variable crossed in this discourse's matrix."),
        ("socati kilamati paridevati, urattāḷiṁ kandati, sammohaṁ "
         "āpajjati",
         "&ldquo;sorrows and wails and laments, beating their breast and "
         "falling into confusion&rdquo; &mdash; one of the two reaction "
         "types, marking a fall from the true teaching whenever it occurs."),
        ("mucchito pamādamāpajjati",
         "&ldquo;becomes indulgent and falls into negligence&rdquo; "
         "&mdash; the other bad reaction, occurring only when material "
         "things actually arrive."),
        ("cuto ariyassa dhammavinayā",
         "&ldquo;fallen from the true teaching&rdquo; &mdash; the "
         "discourse's own verdict, determined entirely by reaction rather "
         "than by effort or outcome."),
    ],
    text_intro=(
        "The discourse in full: eight individuals crossing effort, "
        "outcome, and reaction. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four individuals who have fallen from the true teaching"),
        ("p", "&sect;1", "an8.61:1.1-4.6"),
        ("h3", "Four individuals who have not fallen"),
        ("p", "&sect;2", "an8.61:5.1-9.1"),
    ],
    quiz=[
        {"q": "What three variables does this discourse's matrix cross to "
              "produce eight individuals?",
         "opts": [
             "Wealth, status, and education",
             "Whether one tries for material things, whether those things "
             "come, and how one reacts",
             "Age, gender, and location",
             "Physical strength, courage, and patience"],
         "correct": 1,
         "expl": "A combinatorial structure, not eight independent "
                 "qualities."},
        {"q": "According to the guide, which variable actually determines "
              "whether someone has fallen from the true teaching?",
         "opts": [
             "Whether they tried hard for material things",
             "Only their reaction — sorrow or indulgence versus "
             "equanimity — regardless of effort or outcome",
             "Whether they succeeded in getting material things",
             "Their social status"],
         "correct": 1,
         "expl": "Effort and outcome are named in every case but turn out "
                 "not to be what the discourse tests for."},
        {"q": "What happens to a mendicant who tries hard, fails to get "
              "material things, but doesn't sorrow?",
         "opts": [
             "They are declared fallen from the true teaching",
             "They are declared not fallen, since equanimity is what "
             "matters, not the failed effort",
             "The discourse doesn't address this case",
             "They must try again immediately"],
         "correct": 1,
         "expl": "One of the four cases in the 'not fallen' half of the "
                 "matrix."},
        {"q": "What marks the first four individuals as 'fallen from the "
              "true teaching'?",
         "opts": [
             "Their social class",
             "Reacting with sorrow when unsuccessful, or indulgent "
             "negligence when successful",
             "Living in seclusion at all",
             "Desiring material things in the first place"],
         "correct": 1,
         "expl": "The bad-reaction half of the matrix, regardless of "
                 "effort or outcome."},
        {"q": "How many individuals does this discourse name in total?",
         "opts": [
             "Four", "Eight, crossing three variables",
             "Two", "Sixteen"],
         "correct": 1,
         "expl": "A complete matrix of eight, not a partial list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this book."},
    ],
    marginalia=[
        ("Three variables, eight individuals", [
            "trying or not, getting or not,",
            "reacting with sorrow, indulgence,",
            "or equanimity — the matrix crossed",
        ]),
        ("Effort and outcome don't matter", [
            "both named in every case,",
            "but neither decides the verdict —",
            "only the reaction does",
        ]),
        ("A new chapter opens", [
            "Bhūmicālavagga begins",
            "with a combinatorial teaching,",
            "not a simple eightfold list",
        ]),
        ("Cross-references", [
            "AN 8.60 &middot; earlier, closing the previous chapter",
            "AN 8.62 &middot; next, a related combinatorial teaching about "
            "self- and other-benefit",
        ]),
    ],
    further=[
        '<a href="%s/an8.61/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.60.html">AN 8.60 &middot; Eight Individuals (2nd)</a> &mdash; '
        "earlier, closing the previous chapter.",
        '<a href="an-8.62.html">AN 8.62 &middot; Good Enough</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.62 — Alaṁsutta
# --------------------------------------------------------------------------- #
page(
    62, "Alaṁ", "Good Enough",
    vagga=VAGGA_7,
    meta_title="AN 8.62 — Good Enough | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Alaṁsutta, an eight-case logical teaching on which combinations "
        "of six qualities — quick-wittedness, memory, comprehension, "
        "practice, eloquence, and inspiring others — suffice for one's own "
        "benefit, others' benefit, both, or neither. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight logical cases, each naming a different subset of "
                 "six underlying qualities, cascading from six qualities "
                 "down through two"),
        ("Length", "~3 minutes to read"),
        ("Eight cases, not eight qualities", "Unlike most of this book's "
                                             "eightfold lists, this "
                                             "discourse's underlying "
                                             "material is six qualities, "
                                             "not eight — the &ldquo;eight"
                                             "&rdquo; here counts logical "
                                             "cases built from different "
                                             "combinations of those six"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the "
                       "most logically intricate discourse in this book so "
                       "far, rewarding a careful case-by-case comparison"),
    ],
    why=(
        "AN 8.62 works through eight combinations of six underlying "
        "qualities &mdash; quick-wittedness, memory, comprehension of "
        "meaning, practicing accordingly, eloquent speech, and inspiring "
        "one's companions &mdash; showing which combinations make a "
        "mendicant good enough for their own benefit, for others' "
        "benefit, for both, or for neither."),
    guide=[
        ("The teaching in one sentence", [
            "Six underlying qualities combine in eight different ways "
            "across this discourse's cases, and which subset a mendicant "
            "has determines whether they are good enough for themselves "
            "alone, for others alone, or for both &mdash; with "
            "comprehension-and-practice serving one function and "
            "eloquence-and-inspiration serving the other."]),
        ("Six qualities, not eight, underlying eight cases", [
            "The material this discourse works with is six qualities: "
            "quick-wittedness, ready memory, examining meaning, practicing "
            "in line with understanding, eloquent speech, and the ability "
            "to inspire companions. The &ldquo;eight&rdquo; in this "
            "chapter's theme counts the cases the discourse builds from "
            "different combinations of these six, not the qualities "
            "themselves."]),
        ("A pattern emerges: comprehension for self, eloquence for others", [
            "Working through all eight cases reveals a consistent split: "
            "memory, examining meaning, and practicing accordingly serve "
            "one's own benefit, while eloquent speech and the ability to "
            "inspire serve others' benefit. Quick-wittedness turns out to "
            "be optional in every single case &mdash; its presence or "
            "absence never changes which verdict a case reaches."]),
        ("Not every combination is possible", [
            "The discourse doesn't test all mathematically possible "
            "subsets of six qualities; it selects eight specific "
            "combinations that actually occur, revealing through their "
            "particular pairings (comprehension without eloquence; "
            "eloquence without comprehension; both; neither) that "
            "self-benefit and other-benefit are functionally independent "
            "outcomes, not two names for the same underlying "
            "accomplishment."]),
    ],
    terms=[
        ("alaṁ attano, alaṁ parassa",
         "&ldquo;good enough for themselves... good enough for "
         "others&rdquo; &mdash; the discourse's own two independent "
         "verdicts, this discourse's own title term."),
        ("khippanisanti dhammesu",
         "&ldquo;quick-witted when it comes to skillful teachings&rdquo; "
         "&mdash; the one quality whose presence or absence never changes "
         "any case's verdict, appearing and disappearing without effect."),
        ("atthaṁ upaparikkhati",
         "&ldquo;examines the meaning of teachings they've "
         "memorized&rdquo; &mdash; one of the qualities this discourse "
         "consistently ties to self-benefit rather than benefiting others."),
        ("sāvake ovadati anusāsati",
         "&ldquo;educates, encourages, fires up, and inspires their "
         "spiritual companions&rdquo; &mdash; one of the qualities this "
         "discourse consistently ties to benefiting others."),
        ("cha dhammehi samannāgato, pañcahi dhammehi samannāgato",
         "&ldquo;with six qualities... with five qualities&rdquo; &mdash; "
         "the discourse's own cascading count, descending from six "
         "qualities through five, four, three, and two across its eight "
         "cases."),
    ],
    text_intro=(
        "The discourse in full: eight cases built from six underlying "
        "qualities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six and five qualities: good enough for both"),
        ("p", "&sect;1", "an8.62:1.1-2.9"),
        ("h3", "Four qualities, split two ways"),
        ("p", "&sect;2", "an8.62:3.1-4.9"),
        ("h3", "Three qualities, split two ways"),
        ("p", "&sect;3", "an8.62:5.1-6.9"),
        ("h3", "Two qualities, split two ways"),
        ("p", "&sect;4", "an8.62:7.1-8.9"),
    ],
    quiz=[
        {"q": "How many underlying qualities does this discourse's "
              "material actually consist of, despite its place in the "
              "Book of the Eights?",
         "opts": [
             "Eight qualities directly", "Six qualities, combined into "
                                          "eight different logical cases",
             "Four qualities", "Twelve qualities"],
         "correct": 1,
         "expl": "The 'eight' counts cases built from combinations of six "
                 "underlying qualities, not the qualities themselves."},
        {"q": "According to the guide, what consistent pattern emerges "
              "across the eight cases?",
         "opts": [
             "No pattern at all; the cases are random",
             "Comprehension, memory, and practice serve self-benefit; "
             "eloquence and inspiring others serve other-benefit",
             "Only wealth determines the outcome",
             "Physical strength determines both verdicts"],
         "correct": 1,
         "expl": "A functional split between qualities serving different "
                 "verdicts."},
        {"q": "What role does quick-wittedness play across all eight "
              "cases?",
         "opts": [
             "It is the single most important quality",
             "Its presence or absence never changes any case's verdict",
             "It alone determines other-benefit",
             "It is required for every single case"],
         "correct": 1,
         "expl": "An optional quality whose presence turns out not to be "
                 "load-bearing."},
        {"q": "What two independent verdicts does this discourse assess?",
         "opts": [
             "Wealth and poverty",
             "Being good enough for oneself, and being good enough for "
             "others — shown to be functionally independent",
             "Ordination and lay status",
             "Youth and old age"],
         "correct": 1,
         "expl": "Two separate outcomes, not two names for the same "
                 "accomplishment."},
        {"q": "How does this discourse select its eight cases?",
         "opts": [
             "By testing every mathematically possible combination of six "
             "qualities",
             "By selecting eight specific combinations that actually "
             "occur and reveal the underlying pattern",
             "Randomly, with no logical structure",
             "By listing only positive combinations"],
         "correct": 1,
         "expl": "A deliberately chosen set, not an exhaustive combinatorial "
                 "listing."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.61's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("Six qualities, eight cases", [
            "quick wit, memory, comprehension,",
            "practice, eloquence, inspiring —",
            "combined into eight logical tests",
        ]),
        ("A consistent split emerges", [
            "comprehension serves the self,",
            "eloquence serves others —",
            "two independent verdicts",
        ]),
        ("One quality that never matters", [
            "quick-wittedness comes and goes",
            "across all eight cases —",
            "never changing the outcome",
        ]),
        ("Cross-references", [
            "AN 8.61 &middot; previous, a related combinatorial matrix of "
            "eight individuals",
            "AN 8.63 &middot; next, a request for a teaching in brief",
        ]),
    ],
    further=[
        '<a href="%s/an8.62/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.61.html">AN 8.61 &middot; Desire</a> &mdash; previous.',
        '<a href="an-8.63.html">AN 8.63 &middot; A Teaching in Brief</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.63 — Saṅkhittasutta
# --------------------------------------------------------------------------- #
page(
    63, "Saṅkhitta", "A Teaching in Brief",
    vagga=VAGGA_7,
    meta_title="AN 8.63 — A Teaching in Brief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Saṅkhittasutta, a mendicant's request for brief teaching met "
        "first with suspicion, then answered with a graduated path from "
        "steadying the mind through the four immeasurables to the four "
        "kinds of mindfulness meditation, ending in arahantship. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "An unnamed mendicant and the Buddha"),
        ("Form", "A request rebuffed, then granted, followed by a "
                 "graduated meditation instruction and a narrative close "
                 "reporting the mendicant's own awakening"),
        ("Length", "~3 minutes to read"),
        ("A count that doesn't reach eight explicitly", "Neither the four "
                                                         "immeasurables nor "
                                                         "the four kinds "
                                                         "of mindfulness "
                                                         "meditation named "
                                                         "here total eight "
                                                         "on their own; "
                                                         "this discourse "
                                                         "belongs to the "
                                                         "Book of the "
                                                         "Eights by "
                                                         "placement rather "
                                                         "than by naming an "
                                                         "explicit eightfold "
                                                         "list"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "compressed but complete meditation manual, worth "
                       "reading slowly"),
    ],
    why=(
        "A mendicant asks for brief teaching so he can go meditate alone, "
        "and the Buddha first suspects him of merely wanting an excuse to "
        "follow him around; once reassured, the Buddha gives a graduated "
        "sequence &mdash; steadying the mind, then the four immeasurables, "
        "then the four kinds of mindfulness meditation &mdash; and the "
        "mendicant, practicing accordingly, soon becomes an arahant."),
    guide=[
        ("The teaching in one sentence", [
            "Starting from a steady, settled mind free of unskillful "
            "qualities, a mendicant should develop each of the four "
            "immeasurable states &mdash; love, compassion, rejoicing, and "
            "equanimity &mdash; through seven modes of increasing "
            "refinement, then apply the same graduated development to the "
            "four kinds of mindfulness meditation, arriving at complete "
            "comfort in walking, standing, sitting, and lying down."]),
        ("A rebuff, then a sincere renewal", [
            "The Buddha's first response to the mendicant's request isn't "
            "teaching at all, but a pointed accusation: some people ask "
            "for brief teaching only to use it as an excuse to keep "
            "following him around rather than actually practicing. Only "
            "after the mendicant repeats his request with visible "
            "sincerity &mdash; hoping to understand the meaning and become "
            "an heir of the teaching &mdash; does the Buddha actually "
            "answer."]),
        ("A count that doesn't reach eight explicitly", [
            "Despite this discourse's place in the Book of the Eights, "
            "neither the four immeasurables nor the four kinds of "
            "mindfulness meditation is itself an eightfold list; this "
            "discourse, like several others in this collection, belongs "
            "here by placement in the source anthology rather than by "
            "presenting a clean count of eight."]),
        ("Seven modes, applied twice over", [
            "Both the four immeasurables and the four kinds of "
            "mindfulness meditation are developed through the identical "
            "seven-mode formula: with placing the mind and keeping it "
            "connected, without placing but keeping connected, without "
            "either, with rapture, without rapture, with pleasure, and "
            "with equanimity &mdash; the same refinement sequence applied "
            "twice to two different objects of meditation."]),
    ],
    terms=[
        ("santaṁ vata me cittaṁ bhavissati susaṇṭhitaṁ ajjhattaṁ",
         "&ldquo;my mind will be steady and well settled internally"
         "&rdquo; &mdash; the discourse's own starting point, before any "
         "of the four immeasurables are developed."),
        ("mettāya cetovimuttiṁ bhāvessāmi",
         "&ldquo;I will develop the heart's release by love&rdquo; "
         "&mdash; the first of the four immeasurables, developed with the "
         "same seven-mode refinement applied to each of the others."),
        ("savitakkampi savicāraṁ bhāveyya, avitakkampi vicāramattaṁ "
         "bhāveyya, avitakkampi avicāraṁ bhāveyya",
         "the seven-mode refinement sequence, applied identically to each "
         "of the four immeasurables and again to the four kinds of "
         "mindfulness meditation."),
        ("kāye kāyānupassī vihareyya ātāpī sampajāno satimā, vineyya "
         "loke abhijjhādomanassaṁ",
         "&ldquo;meditate observing an aspect of the body&mdash;keen, "
         "aware, and mindful, rid of covetousness and displeasure&rdquo; "
         "&mdash; the first of the four kinds of mindfulness meditation, "
         "developed the same way as the immeasurables before it."),
        ("etadeva bahulamakāsi",
         "the aftermath in which the mendicant, given this graduated "
         "advice, practices it thoroughly and soon realizes arahantship."),
    ],
    text_intro=(
        "The discourse in full: a rebuffed and renewed request, a "
        "graduated meditation instruction, and the mendicant's own "
        "awakening. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A request, rebuffed and renewed"),
        ("p", "&sect;1", "an8.63:1.1-1.6"),
        ("h3", "A steady mind, then love"),
        ("p", "&sect;2", "an8.63:1.7-3.1"),
        ("h3", "Compassion, rejoicing, and equanimity"),
        ("p", "&sect;3", "an8.63:4.1-5.1"),
        ("h3", "The four kinds of mindfulness meditation"),
        ("p", "&sect;4", "an8.63:6.1-9.1"),
        ("h3", "Comfort in every posture, and the mendicant's awakening"),
        ("p", "&sect;5", "an8.63:10.1-11.4"),
    ],
    quiz=[
        {"q": "How does the Buddha first respond to the mendicant's "
              "request for brief teaching?",
         "opts": [
             "He grants it immediately",
             "He suspects the mendicant of merely wanting an excuse to "
             "follow him around rather than actually practicing",
             "He refuses to speak at all",
             "He asks the mendicant to teach him instead"],
         "correct": 1,
         "expl": "A pointed accusation, answered only after the mendicant "
                 "renews his request sincerely."},
        {"q": "What is the graduated sequence the Buddha eventually gives?",
         "opts": [
             "A single instruction with no further development",
             "Steadying the mind, then the four immeasurables, then the "
             "four kinds of mindfulness meditation",
             "A list of monastic rules",
             "Instructions for building a shrine"],
         "correct": 1,
         "expl": "A complete graduated path from settling the mind to "
                 "full mindfulness practice."},
        {"q": "According to the guide, does this discourse's actual content "
              "total eight of anything explicitly?",
         "opts": [
             "Yes, exactly eight immeasurables",
             "No — neither the four immeasurables nor the four kinds of "
             "mindfulness meditation is itself an eightfold list",
             "Yes, eight kinds of mindfulness",
             "The discourse doesn't discuss any numbered lists"],
         "correct": 1,
         "expl": "A discourse included by placement, like several others "
                 "in this collection."},
        {"q": "What seven-mode formula is applied to both the "
              "immeasurables and the mindfulness meditations?",
         "opts": [
             "A count of breaths",
             "Placing/keeping connected, without placing, without either, "
             "with rapture, without rapture, with pleasure, with "
             "equanimity",
             "A recitation of precepts",
             "A physical posture sequence"],
         "correct": 1,
         "expl": "The same refinement sequence applied twice, to two "
                 "different meditation objects."},
        {"q": "What happens to the mendicant after receiving this advice?",
         "opts": [
             "Nothing further is recorded",
             "He practices it thoroughly and soon realizes arahantship",
             "He rejects the teaching",
             "He asks for a different teaching instead"],
         "correct": 1,
         "expl": "The narrative frame closes with the mendicant's own "
                 "successful practice."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Suspicion, then sincerity", [
            "'some ask just to follow me' —",
            "the request renewed, sincere —",
            "then the Buddha actually answers",
        ]),
        ("A graduated sequence", [
            "steady mind, then love,",
            "compassion, joy, equanimity —",
            "then the four mindfulnesses",
        ]),
        ("Seven modes, applied twice", [
            "placing and connecting the mind,",
            "rapture, pleasure, equanimity —",
            "the same refinement, two objects",
        ]),
        ("Cross-references", [
            "AN 8.62 &middot; previous, a logical teaching on self- and "
            "other-benefit",
            "AN 8.64 &middot; next, the Buddha's own account of purifying "
            "his knowledge of deities",
        ]),
    ],
    further=[
        '<a href="%s/an8.63/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.62.html">AN 8.62 &middot; Good Enough</a> &mdash; previous.',
        '<a href="an-8.64.html">AN 8.64 &middot; At Gayā Head</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.64 — Gayāsīsasutta -- a major autobiographical account of the
# pre-awakening period, complementary to AN 8.11's three-knowledges account.
# --------------------------------------------------------------------------- #
page(
    64, "Gayāsīsa", "At Gayā Head",
    vagga=VAGGA_7,
    meta_title="AN 8.64 — At Gayā Head | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Gayāsīsasutta, the Buddha's own first-person account of "
        "purifying his knowledge of deities through eight escalating "
        "rounds before he would announce his awakening — complementary to "
        "AN 8.11's three-knowledges account. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Gayā, on Gayā Head"),
        ("Speakers", "The Buddha, in first-person autobiographical account"),
        ("Form", "Eight escalating rounds, each adding one further "
                 "refinement to a single ongoing process of purification"),
        ("Length", "~3 minutes to read"),
        ("Complementary to AN 8.11", "Where AN 8.11 gave the Buddha's own "
                                     "account of the three knowledges of "
                                     "his awakening night, this discourse "
                                     "gives a parallel first-person "
                                     "account focused specifically on "
                                     "deities, structured as eight "
                                     "explicit rounds rather than three "
                                     "watches"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "cumulative, escalating structure where each round "
                       "adds exactly one further refinement to the last"),
    ],
    why=(
        "The Buddha describes, in his own first-person voice, purifying "
        "his &ldquo;knowledge and vision&rdquo; about deities through "
        "eight escalating rounds &mdash; from merely perceiving light, "
        "through seeing forms, conversing with deities, learning their "
        "origin, their karma, their food and feelings, their lifespan, "
        "and finally whether he had previously lived among them &mdash; "
        "declaring that he did not announce his awakening until all "
        "eight were fully purified."),
    guide=[
        ("The teaching in one sentence", [
            "Before his awakening, the Buddha purified his knowledge and "
            "vision of deities through eight cumulative rounds, each "
            "adding exactly one further refinement to what he already "
            "knew, and declared that he would not announce his "
            "supreme awakening to the world until this eightfold "
            "knowledge was completely purified."]),
        ("An escalating structure, one refinement at a time", [
            "Each round in this account follows an identical pattern: the "
            "Buddha notices what his current knowledge lacks, reflects "
            "that resolving it would further purify his knowledge and "
            "vision, then achieves it after further diligent practice "
            "&mdash; from perceiving light without seeing forms, to "
            "seeing forms without engaging the deities behind them, to "
            "conversing without knowing their origin, and onward through "
            "knowledge of their karma, their food and feelings, their "
            "lifespan, and finally whether he had lived among them "
            "before."]),
        ("Complementary to AN 8.11, not a repeat", [
            "This discourse doesn't restate AN 8.11's three knowledges "
            "&mdash; past lives, other beings' rebirth according to their "
            "deeds, and the ending of defilements &mdash; but offers a "
            "parallel first-person account focused specifically and only "
            "on deities, structured around eight explicit rounds rather "
            "than three watches of the awakening night, giving a "
            "different, more granular window into the same pre-awakening "
            "period."]),
        ("Knowledge withheld until fully purified", [
            "The discourse's own framing carries real weight: the Buddha "
            "states plainly that he did not announce his awakening to the "
            "world &mdash; with its gods, Māras, and divinities &mdash; "
            "until every one of the eight rounds concerning deities was "
            "complete, treating this specific knowledge as a genuine "
            "precondition for the announcement, not a minor detail."]),
    ],
    terms=[
        ("obhāsañceva sañjānāmi, na ca rūpāni passāmi",
         "&ldquo;I perceived light but did not see forms&rdquo; &mdash; "
         "the Buddha's own starting point, before the first of the eight "
         "rounds is completed."),
        ("ñāṇadassanaṁ visujjheyya",
         "&ldquo;my knowledge and vision would become even more "
         "purified&rdquo; &mdash; the refrain closing each stage of "
         "reflection, before the next round is achieved through further "
         "practice."),
        ("kismiṁ nu kho devanikāye ito cutā upapannā",
         "part of the third round, learning which specific orders of "
         "gods particular deities belong to, once mere conversation with "
         "them was no longer enough."),
        ("ahosiṁ nu kho ahaṁ tehi devehi saddhiṁ",
         "&ldquo;whether or not I had previously lived together with "
         "those deities&rdquo; &mdash; the eighth and final round, "
         "closing the entire sequence."),
        ("na tāvāhaṁ ... anuttaraṁ sammāsambodhiṁ abhisambuddhoti "
         "paccaññāsiṁ",
         "&ldquo;I didn't announce my supreme perfect awakening&rdquo; "
         "&mdash; the Buddha's own statement that this eightfold "
         "knowledge was a genuine precondition, not withheld arbitrarily."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's own first-person account of "
        "eight escalating rounds of purified knowledge about deities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first two rounds: light, then forms"),
        ("p", "&sect;1", "an8.64:1.1-3.2"),
        ("h3", "The third and fourth rounds: conversation, then origin"),
        ("p", "&sect;2", "an8.64:4.1-7.6"),
        ("h3", "The fifth through eighth rounds"),
        ("p", "&sect;3", "an8.64:7.7-9.5"),
        ("h3", "The announcement, once fully purified"),
        ("p", "&sect;4", "an8.64:10.1-10.4"),
    ],
    quiz=[
        {"q": "What is the Buddha's own starting point in this account, "
              "before any of the eight rounds is completed?",
         "opts": [
             "He already sees deities clearly",
             "He perceives light but doesn't see forms",
             "He knows nothing about deities at all",
             "He has already completed the first round"],
         "correct": 1,
         "expl": "The account's own opening condition, refined "
                 "progressively through eight rounds."},
        {"q": "What pattern does each of the eight rounds follow?",
         "opts": [
             "A random, unstructured sequence",
             "Noticing a lack, reflecting that resolving it would purify "
             "knowledge further, then achieving it through diligent "
             "practice",
             "A single instantaneous realization with no development",
             "A dialogue with another person"],
         "correct": 1,
         "expl": "An identical cumulative structure repeated across all "
                 "eight rounds."},
        {"q": "How does this discourse relate to AN 8.11's own account of "
              "the awakening?",
         "opts": [
             "It simply repeats AN 8.11's three knowledges",
             "It is complementary — a parallel first-person account "
             "focused specifically on deities, structured around eight "
             "rounds rather than three watches",
             "It contradicts AN 8.11 entirely",
             "It has no relation to AN 8.11"],
         "correct": 1,
         "expl": "A different, more granular window into the same "
                 "pre-awakening period."},
        {"q": "What is the eighth and final round of knowledge purified?",
         "opts": [
             "The deities' names",
             "Whether the Buddha had previously lived together with those "
             "deities",
             "The deities' physical appearance",
             "The deities' language"],
         "correct": 1,
         "expl": "The closing round, completing the eightfold sequence."},
        {"q": "What does the Buddha say about announcing his awakening "
              "before this eightfold knowledge was purified?",
         "opts": [
             "He announced it immediately regardless",
             "He did not announce his supreme awakening until this "
             "eightfold knowledge concerning deities was fully purified",
             "The discourse doesn't address the announcement at all",
             "He announced it before purifying any of the eight rounds"],
         "correct": 1,
         "expl": "A genuine precondition, stated plainly in the "
                 "discourse's own closing lines."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Gayā, on Gayā Head",
             "Rājagaha, on Vulture's Peak", "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A location distinct from most of this book's other "
                 "settings."},
    ],
    marginalia=[
        ("Eight rounds, cumulative", [
            "light, then forms, then speech,",
            "origin, karma, food and feeling,",
            "lifespan, then shared past lives",
        ]),
        ("Complementary to AN 8.11", [
            "not a repeat, but a parallel —",
            "eight rounds on deities alone,",
            "not the three knowledges' full sweep",
        ]),
        ("Withheld until complete", [
            "no announcement made",
            "until all eight were purified —",
            "a genuine precondition, not a detail",
        ]),
        ("Cross-references", [
            "AN 8.63 &middot; previous, a mendicant's own graduated path "
            "to awakening",
            "AN 8.11 &middot; earlier, the Buddha's own account of the "
            "three knowledges",
        ]),
    ],
    further=[
        '<a href="%s/an8.64/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.63.html">AN 8.63 &middot; A Teaching in Brief</a> &mdash; previous.',
        '<a href="an-8.11.html">AN 8.11 &middot; At Verañjā</a> &mdash; earlier, the '
        "Buddha's own account of the three knowledges.",
        '<a href="an-8.65.html">AN 8.65 &middot; Dimensions of Mastery</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.65 — Abhibhāyatanasutta
# --------------------------------------------------------------------------- #
page(
    65, "Abhibhāyatana", "Dimensions of Mastery",
    vagga=VAGGA_7,
    meta_title="AN 8.65 — Dimensions of Mastery | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Abhibhāyatanasutta, a classic list of eight meditative dimensions "
        "of mastery over perceived form, moving from limited and "
        "limitless external forms through the four color kasinas. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight dimensions, each following the identical "
                 "'perceiving/not perceiving... mastering them, they "
                 "perceive: I know and see' formula"),
        ("Length", "~1 minute to read"),
        ("A foundational, widely referenced meditation topic", "The eight "
                                                                "dimensions "
                                                                "of mastery "
                                                                "are a "
                                                                "classic "
                                                                "topic in "
                                                                "this "
                                                                "literature's "
                                                                "meditation "
                                                                "typology, "
                                                                "closely "
                                                                "related to "
                                                                "the eight "
                                                                "liberations "
                                                                "at AN "
                                                                "8.66, "
                                                                "immediately "
                                                                "following"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "terse and technical, best understood by tracking "
                       "the pattern's own internal variables"),
    ],
    why=(
        "AN 8.65 names eight dimensions of meditative mastery over "
        "perceived form &mdash; internal perception with limited or "
        "limitless external forms, no internal perception with limited or "
        "limitless external forms, and finally no internal perception "
        "with each of four external colors, blue, yellow, red, and white."),
    guide=[
        ("The teaching in one sentence", [
            "Eight dimensions of mastery progress through combinations of "
            "internal versus absent internal form-perception, limited "
            "versus limitless external forms, and finally four specific "
            "colors &mdash; blue, yellow, red, white &mdash; each "
            "dimension marked by the meditator's own confident "
            "declaration, &ldquo;I know and see.&rdquo;"]),
        ("Two variables, crossed across the first four dimensions", [
            "The first four dimensions cross two variables: whether form "
            "is perceived internally at all, and whether the external "
            "forms seen are limited or limitless in scope. All four "
            "dimensions include both pretty and ugly forms within their "
            "scope, testing whether the meditator's mastery holds across "
            "that entire aesthetic range."]),
        ("Four colors, closing the sequence", [
            "The final four dimensions drop the internal/external "
            "distinction of the first four and instead specify four pure "
            "colors in turn &mdash; blue, yellow, red, white &mdash; each "
            "described identically apart from its color, forming the "
            "basis for what later tradition develops into the color "
            "kasina meditations."]),
        ("Mastery, not mere perception", [
            "Every one of the eight dimensions closes with the identical "
            "phrase, &ldquo;mastering them, they perceive: 'I know and "
            "see,'&rdquo; distinguishing this practice from simply "
            "perceiving forms passively &mdash; the discourse's own "
            "emphasis falls on active mastery over what's perceived, not "
            "merely on the perception itself."]),
    ],
    terms=[
        ("abhibhāyatanāni",
         "&ldquo;dimensions of mastery&rdquo; &mdash; this discourse's "
         "own title term, active control over what's perceived rather "
         "than passive perception."),
        ("ajjhattaṁ rūpasaññī",
         "&ldquo;perceiving form internally&rdquo; &mdash; the variable "
         "distinguishing the first two dimensions from the third and "
         "fourth."),
        ("parittāni suvaṇṇadubbaṇṇāni, appamāṇāni suvaṇṇadubbaṇṇāni",
         "&ldquo;limited, both pretty and ugly&rdquo; and &ldquo;limitless, "
         "both pretty and ugly&rdquo; &mdash; the scope variable crossed "
         "against internal perception in the first four dimensions."),
        ("nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni",
         "&ldquo;blue, with blue color and blue appearance&rdquo; "
         "&mdash; the fifth dimension, the first of four pure-color "
         "dimensions closing the sequence."),
        ("abhibhuyya jānāmi passāmī'ti saññī hoti",
         "&ldquo;mastering them, they perceive: 'I know and see'&rdquo; "
         "&mdash; the identical closing declaration for all eight "
         "dimensions, emphasizing active mastery."),
    ],
    text_intro=(
        "The discourse in full: eight dimensions of mastery over perceived "
        "form. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first four dimensions: internal perception crossed "
               "with scope"),
        ("p", "&sect;1", "an8.65:1.1-4.3"),
        ("h3", "The final four dimensions: four pure colors"),
        ("p", "&sect;2", "an8.65:5.1-8.4"),
    ],
    quiz=[
        {"q": "What two variables are crossed across the first four "
              "dimensions of mastery?",
         "opts": [
             "Wealth and poverty",
             "Whether form is perceived internally, and whether external "
             "forms seen are limited or limitless",
             "Age and gender",
             "Physical strength and endurance"],
         "correct": 1,
         "expl": "A combinatorial structure similar to other 'crossed "
                 "variable' teachings in this book."},
        {"q": "What do the final four dimensions specify, replacing the "
              "internal/external distinction?",
         "opts": [
             "Four specific sounds",
             "Four pure colors — blue, yellow, red, and white",
             "Four physical postures",
             "Four monastic robes"],
         "correct": 1,
         "expl": "The basis for what later tradition develops into the "
                 "color kasina meditations."},
        {"q": "What phrase closes every one of the eight dimensions "
              "identically?",
         "opts": [
             "'This is impermanent'",
             "'Mastering them, they perceive: I know and see'",
             "'This is not mine'",
             "'This leads to suffering'"],
         "correct": 1,
         "expl": "Emphasizing active mastery over what's perceived, not "
                 "passive perception."},
        {"q": "According to the guide, what does this discourse emphasize "
              "over mere perception?",
         "opts": [
             "Speed of perception",
             "Active mastery over what's perceived",
             "The number of forms perceived",
             "The meditator's physical location"],
         "correct": 1,
         "expl": "The discourse's own repeated closing phrase makes this "
                 "emphasis explicit."},
        {"q": "What range of forms does each of the first four dimensions "
              "cover?",
         "opts": [
             "Only pretty forms",
             "Both pretty and ugly forms, testing whether mastery holds "
             "across the entire aesthetic range",
             "Only ugly forms",
             "No specific range is mentioned"],
         "correct": 1,
         "expl": "A deliberately full aesthetic range, not a filtered "
                 "selection."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Two variables, four dimensions", [
            "internal or not, limited",
            "or limitless — both pretty",
            "and ugly forms, mastered",
        ]),
        ("Four colors, closing", [
            "blue, yellow, red, white —",
            "each identically described,",
            "the seed of the color kasinas",
        ]),
        ("Mastery, not mere seeing", [
            "'I know and see' — active",
            "control over the perceived,",
            "not passive observation",
        ]),
        ("Cross-references", [
            "AN 8.64 &middot; previous, the Buddha's own eight rounds of "
            "purified knowledge",
            "AN 8.66 &middot; next, the closely related eight liberations",
        ]),
    ],
    further=[
        '<a href="%s/an8.65/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.64.html">AN 8.64 &middot; At Gayā Head</a> &mdash; previous.',
        '<a href="an-8.66.html">AN 8.66 &middot; Liberations</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.66 — Vimokkhasutta
# --------------------------------------------------------------------------- #
page(
    66, "Vimokkha", "Liberations",
    vagga=VAGGA_7,
    meta_title="AN 8.66 — Liberations | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Vimokkhasutta, the eight classic liberations, ascending from "
        "ordinary form-perception through the four formless dimensions to "
        "the cessation of perception and feeling. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight liberations in strict ascending sequence, the "
                 "first three named briefly, the remaining five each "
                 "explicitly building on 'going totally beyond' the one "
                 "before it"),
        ("Length", "under 1 minute to read"),
        ("A companion list to AN 8.65", "The eight liberations and the "
                                        "eight dimensions of mastery at AN "
                                        "8.65 are closely related "
                                        "meditation topics in this "
                                        "literature's own typology, often "
                                        "discussed together as related but "
                                        "distinct sequences"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; terse "
                       "and technical, an ascending sequence worth tracing "
                       "step by step"),
    ],
    why=(
        "AN 8.66 names the eight liberations in ascending sequence: seeing "
        "forms while having physical form, seeing external forms without "
        "perceiving form internally, focusing only on beauty, then the "
        "four formless dimensions &mdash; infinite space, infinite "
        "consciousness, nothingness, neither perception nor non-perception "
        "&mdash; and finally the cessation of perception and feeling."),
    guide=[
        ("The teaching in one sentence", [
            "The eight liberations ascend from ordinary embodied "
            "perception of form, through progressively more refined "
            "states of form-perception and pure aesthetic focus, into the "
            "four formless meditative dimensions, culminating in the "
            "complete cessation of perception and feeling itself."]),
        ("Three form-based liberations, briefly stated", [
            "The first three liberations are each named in a single "
            "terse line: having physical form and seeing forms; not "
            "perceiving form internally while seeing forms externally; "
            "and being focused only on beauty. Unlike the eight "
            "dimensions of mastery at AN 8.65, these opening liberations "
            "receive no elaboration on scope or aesthetic range."]),
        ("Four formless dimensions, each explicitly transcending the last", [
            "From the fourth liberation onward, the discourse's own "
            "language makes the ascending structure explicit: each "
            "formless dimension is reached by &ldquo;going totally "
            "beyond&rdquo; perceptions of the one before it &mdash; "
            "beyond form to infinite space, beyond infinite space to "
            "infinite consciousness, beyond that to nothingness, and "
            "beyond that to neither perception nor non-perception."]),
        ("The eighth liberation, beyond perception itself", [
            "The sequence's final step goes further than any refinement "
            "of perception: the eighth liberation is the cessation of "
            "perception and feeling entirely, not a subtler object to be "
            "perceived but the ending of the perceiving-and-feeling "
            "process itself, closing a sequence that has moved "
            "consistently toward less and less content, not more."]),
    ],
    terms=[
        ("vimokkhā",
         "&ldquo;liberations&rdquo; &mdash; this discourse's own title "
         "term, an ascending sequence of meditative states rather than a "
         "single moment of release."),
        ("rūpī rūpāni passati",
         "&ldquo;having physical form, they see forms&rdquo; &mdash; the "
         "first liberation, ordinary embodied perception of form."),
        ("subhanteva adhimutto hoti",
         "&ldquo;they're focused only on beauty&rdquo; &mdash; the third "
         "liberation, a pure aesthetic focus preceding the formless "
         "dimensions."),
        ("sabbaso rūpasaññānaṁ samatikkamā ... ākāsānañcāyatanaṁ "
         "upasampajja viharati",
         "&ldquo;going totally beyond perceptions of form... they enter "
         "and remain in the dimension of infinite space&rdquo; &mdash; "
         "the fourth liberation, the first of the four formless "
         "dimensions."),
        ("saññāvedayitanirodhaṁ upasampajja viharati",
         "&ldquo;they enter and remain in the cessation of perception and "
         "feeling&rdquo; &mdash; the eighth and final liberation, going "
         "beyond perception itself rather than refining it further."),
    ],
    text_intro=(
        "The discourse in full: the eight liberations in ascending "
        "sequence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three form-based liberations"),
        ("p", "&sect;1", "an8.66:1.1-3.2"),
        ("h3", "Four formless dimensions, each beyond the last"),
        ("p", "&sect;2", "an8.66:4.1-7.2"),
        ("h3", "The cessation of perception and feeling"),
        ("p", "&sect;3", "an8.66:8.1-8.3"),
    ],
    quiz=[
        {"q": "What are the first three liberations, briefly stated?",
         "opts": [
             "The five hindrances, negated",
             "Having physical form and seeing forms; not perceiving form "
             "internally while seeing forms externally; and being "
             "focused only on beauty",
             "The seven factors of awakening",
             "The four noble truths"],
         "correct": 1,
         "expl": "Three terse form-based liberations, opening the "
                 "ascending sequence."},
        {"q": "What language makes the ascending structure explicit from "
              "the fourth liberation onward?",
         "opts": [
             "No particular language marks the progression",
             "Each formless dimension is reached by 'going totally "
             "beyond' perceptions of the one before it",
             "A count of breaths",
             "A description of physical posture"],
         "correct": 1,
         "expl": "An explicit transcendence formula linking each formless "
                 "dimension to the one preceding it."},
        {"q": "What are the four formless dimensions in this sequence?",
         "opts": [
             "The four elements: earth, water, fire, air",
             "Infinite space, infinite consciousness, nothingness, and "
             "neither perception nor non-perception",
             "The four noble truths",
             "The four kinds of mindfulness meditation"],
         "correct": 1,
         "expl": "Four progressively more refined formless meditative "
                 "states."},
        {"q": "What is the eighth and final liberation?",
         "opts": [
             "An even more refined perception",
             "The cessation of perception and feeling entirely",
             "A return to ordinary form-perception",
             "Physical death"],
         "correct": 1,
         "expl": "Not a subtler object to perceive, but the ending of the "
                 "perceiving-and-feeling process itself."},
        {"q": "How does this discourse relate to AN 8.65's eight "
              "dimensions of mastery?",
         "opts": [
             "They are unrelated topics",
             "They are closely related meditation topics in this "
             "literature's typology, often discussed together as related "
             "but distinct sequences",
             "They directly contradict each other",
             "This discourse simply repeats AN 8.65"],
         "correct": 1,
         "expl": "Companion lists, immediately adjacent in this chapter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.65's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("Three form-based liberations", [
            "seeing forms with form,",
            "seeing without internal form,",
            "focused only on beauty",
        ]),
        ("Four formless, each beyond the last", [
            "infinite space, infinite mind,",
            "nothingness, neither-nor —",
            "each explicitly transcending the one before",
        ]),
        ("Cessation, not further refinement", [
            "the eighth goes beyond",
            "perception itself entirely —",
            "less content, not more",
        ]),
        ("Cross-references", [
            "AN 8.65 &middot; previous, the closely related eight "
            "dimensions of mastery",
            "AN 8.67 &middot; next, eight ignoble expressions",
        ]),
    ],
    further=[
        '<a href="%s/an8.66/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.65.html">AN 8.65 &middot; Dimensions of Mastery</a> &mdash; previous.',
        '<a href="an-8.67.html">AN 8.67 &middot; Ignoble Expressions</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.67 — Anariyavohārasutta
# --------------------------------------------------------------------------- #
page(
    67, "Anariyavohāra", "Ignoble Expressions",
    vagga=VAGGA_7,
    meta_title="AN 8.67 — Ignoble Expressions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Anariyavohārasutta, eight ignoble expressions built from a "
        "simple 4×2 structure: claiming to have or not have seen, heard, "
        "thought, or known something, falsely. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A compact 4×2 combinatorial structure, stated in a "
                 "single sentence"),
        ("Length", "a few seconds to read"),
        ("The most compact discourse in this chapter", "Where several "
                                                        "discourses in "
                                                        "this book take "
                                                        "paragraphs to "
                                                        "enumerate eight "
                                                        "items, this one "
                                                        "compresses all "
                                                        "eight into a "
                                                        "single sentence "
                                                        "crossing four "
                                                        "categories with "
                                                        "two directions of "
                                                        "falsehood"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and logically clean, best read alongside AN 8.68's "
                       "own mirror-image structure"),
    ],
    why=(
        "AN 8.67 names eight ignoble expressions, built from a single "
        "compact structure: falsely claiming to have seen, heard, thought, "
        "or known something you haven't, and falsely claiming not to have "
        "seen, heard, thought, or known something you have."),
    guide=[
        ("The teaching in one sentence", [
            "Eight ignoble expressions arise from crossing four "
            "categories of experience &mdash; seeing, hearing, thinking, "
            "and knowing &mdash; against two directions of falsehood: "
            "claiming something happened when it didn't, and claiming "
            "something didn't happen when it did."]),
        ("A 4×2 structure, not eight separate lies", [
            "Rather than naming eight unrelated falsehoods, this "
            "discourse crosses four categories of experience against two "
            "directions of misrepresentation, producing exactly eight "
            "combinations from a structure that could be stated in a "
            "single short sentence."]),
        ("Four categories spanning all channels of knowing", [
            "Seeing, hearing, thinking, and knowing together cover the "
            "full range of how a person comes to claim awareness of "
            "something &mdash; direct sensory experience (seeing, "
            "hearing), and internal cognitive processes (thinking, "
            "knowing) &mdash; leaving no channel of claimed experience "
            "untouched by the discourse's own scope."]),
        ("Two directions, both equally ignoble", [
            "The discourse treats false claiming and false denying as "
            "equally ignoble, not weighting one direction as worse than "
            "the other &mdash; overclaiming experience one doesn't have "
            "and underclaiming experience one does have are named "
            "together as the same category of falsehood."]),
    ],
    terms=[
        ("anariyā vohārā",
         "&ldquo;ignoble expressions&rdquo; &mdash; this discourse's own "
         "title term, contrasted directly with AN 8.68's noble "
         "expressions immediately following."),
        ("adiṭṭhe diṭṭhavāditā",
         "&ldquo;saying you've seen something, but you haven't&rdquo; "
         "&mdash; the overclaiming direction, applied to the first of the "
         "four categories."),
        ("diṭṭhe adiṭṭhavāditā",
         "&ldquo;saying you haven't seen something, and you have&rdquo; "
         "&mdash; the underclaiming direction, the mirror image of the "
         "first."),
        ("suta, muta, viññāta",
         "&ldquo;heard, thought, known&rdquo; &mdash; the remaining three "
         "categories, each crossed against the same two directions of "
         "falsehood as seeing."),
        ("vohārā",
         "&ldquo;expressions&rdquo; &mdash; a term for speech acts or "
         "verbal claims, the discourse's own subject matter throughout."),
    ],
    text_intro=(
        "The discourse in full: eight ignoble expressions, crossing four "
        "categories against two directions of falsehood. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight ignoble expressions"),
        ("p", "&sect;1", "an8.67:1.1-1.4"),
    ],
    quiz=[
        {"q": "What structure produces this discourse's eight ignoble "
              "expressions?",
         "opts": [
             "Eight entirely separate, unrelated falsehoods",
             "Four categories of experience (seeing, hearing, thinking, "
             "knowing) crossed against two directions of falsehood",
             "A random list with no underlying structure",
             "Eight different social classes"],
         "correct": 1,
         "expl": "A compact 4x2 combinatorial structure, not eight "
                 "independent items."},
        {"q": "What are the four categories of experience named?",
         "opts": [
             "Wealth, status, education, and beauty",
             "Seeing, hearing, thinking, and knowing",
             "Faith, ethics, generosity, and wisdom",
             "Birth, aging, illness, and death"],
         "correct": 1,
         "expl": "Together spanning direct sensory experience and "
                 "internal cognitive processes."},
        {"q": "What two directions of falsehood does the discourse treat "
              "as equally ignoble?",
         "opts": [
             "Only overclaiming, since underclaiming is harmless",
             "Falsely claiming something happened, and falsely claiming "
             "something didn't happen",
             "Only underclaiming, since overclaiming is harmless",
             "Neither direction is actually addressed"],
         "correct": 1,
         "expl": "Overclaiming and underclaiming named together as the "
                 "same category of falsehood."},
        {"q": "How does this discourse compare in length to most others in "
              "this chapter?",
         "opts": [
             "It is the longest discourse in the chapter",
             "It is among the most compact, stating all eight in a single "
             "short sentence",
             "It is of average length",
             "It has no measurable length difference"],
         "correct": 1,
         "expl": "A structure compact enough to state very briefly."},
        {"q": "How does this discourse relate to AN 8.68, immediately "
              "following it?",
         "opts": [
             "No relation at all",
             "AN 8.68 presents the mirror-image structure: noble "
             "expressions, truthfully claiming or denying",
             "AN 8.68 contradicts this discourse's teaching",
             "AN 8.68 is unrelated to truth-telling"],
         "correct": 1,
         "expl": "A deliberately paired contrast, false versus truthful "
                 "claims."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Four categories, two directions", [
            "seeing, hearing, thinking, knowing —",
            "falsely claimed, or falsely denied —",
            "eight from one compact structure",
        ]),
        ("Both directions, equally ignoble", [
            "overclaiming what didn't happen,",
            "underclaiming what did —",
            "named together, not ranked",
        ]),
        ("This chapter's most compact teaching", [
            "all eight in one sentence —",
            "a structure, not a list",
            "to be memorized item by item",
        ]),
        ("Cross-references", [
            "AN 8.66 &middot; previous, the eight liberations",
            "AN 8.68 &middot; next, the mirror-image noble expressions",
        ]),
    ],
    further=[
        '<a href="%s/an8.67/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.66.html">AN 8.66 &middot; Liberations</a> &mdash; previous.',
        '<a href="an-8.68.html">AN 8.68 &middot; Noble Expressions</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.68 — Ariyavohārasutta
# --------------------------------------------------------------------------- #
page(
    68, "Ariyavohāra", "Noble Expressions",
    vagga=VAGGA_7,
    meta_title="AN 8.68 — Noble Expressions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Ariyavohārasutta, the exact mirror image of AN 8.67: eight noble "
        "expressions built from truthfully claiming or denying having "
        "seen, heard, thought, or known something. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical 4×2 structure as AN 8.67, with truthful "
                 "rather than false claims"),
        ("Length", "a few seconds to read"),
        ("A deliberate mirror, not a variant", "Every category and every "
                                               "direction in this "
                                               "discourse matches AN "
                                               "8.67's structure exactly; "
                                               "only truthfulness replaces "
                                               "falsehood, a symmetry this "
                                               "reading guide treats as "
                                               "the pairing's own point"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "identical in structure to AN 8.67, best read "
                       "immediately after it"),
    ],
    why=(
        "AN 8.68 names eight noble expressions, the exact structural "
        "mirror of AN 8.67's ignoble ones: truthfully claiming not to "
        "have seen, heard, thought, or known something when you haven't, "
        "and truthfully claiming to have when you have."),
    guide=[
        ("The teaching in one sentence", [
            "Eight noble expressions arise from the same 4x2 structure as "
            "AN 8.67's ignoble ones &mdash; four categories of experience "
            "crossed against two directions of claim &mdash; but here "
            "every claim matches the actual facts: denying what didn't "
            "happen, and affirming what did."]),
        ("An exact structural mirror", [
            "This discourse changes nothing about AN 8.67's underlying "
            "structure &mdash; the same four categories (seeing, hearing, "
            "thinking, knowing), the same two directions of claim "
            "(affirming, denying). The only change is that every claim "
            "now accurately tracks reality rather than misrepresenting it."]),
        ("Truthfulness as simple correspondence", [
            "Nothing in this discourse frames noble speech as requiring "
            "eloquence, tact, or diplomatic softening &mdash; the entire "
            "content of &ldquo;noble expression&rdquo; here is simple "
            "correspondence between what one claims and what actually "
            "happened, in either direction, across all four categories of "
            "experience."]),
        ("A pair that makes truthfulness structurally visible", [
            "Read together, AN 8.67 and AN 8.68 make truthfulness "
            "visible as a structural property rather than a vague virtue: "
            "the identical eight-slot grid can be filled with lies or "
            "with truth, and nothing about the grid itself changes "
            "&mdash; only whether each claim actually matches what "
            "happened."]),
    ],
    terms=[
        ("ariyā vohārā",
         "&ldquo;noble expressions&rdquo; &mdash; this discourse's own "
         "title term, the exact structural mirror of AN 8.67's ignoble "
         "expressions."),
        ("adiṭṭhe adiṭṭhavāditā",
         "&ldquo;saying you haven't seen something, and you haven't&rdquo; "
         "&mdash; the first noble expression, truthful denial matching "
         "AN 8.67's first ignoble expression's false affirmation."),
        ("diṭṭhe diṭṭhavāditā",
         "&ldquo;saying you've seen something, and you have&rdquo; "
         "&mdash; the mirror truthful affirmation, completing the first "
         "pair."),
        ("suta, muta, viññāta",
         "&ldquo;heard, thought, known&rdquo; &mdash; the same three "
         "remaining categories as AN 8.67, each crossed against truthful "
         "affirmation and truthful denial."),
        ("vohārā",
         "&ldquo;expressions&rdquo; &mdash; the identical subject term as "
         "AN 8.67, now applied to accurate rather than false claims."),
    ],
    text_intro=(
        "The discourse in full: eight noble expressions, the mirror image "
        "of AN 8.67. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight noble expressions"),
        ("p", "&sect;1", "an8.68:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this discourse's structure compare to AN 8.67's?",
         "opts": [
             "Entirely different",
             "The identical 4x2 structure — four categories crossed "
             "against two directions of claim — with truthfulness "
             "replacing falsehood",
             "This discourse has only four expressions, not eight",
             "The two discourses share nothing"],
         "correct": 1,
         "expl": "An exact structural mirror, changing only whether "
                 "claims match reality."},
        {"q": "What does this discourse's framing of 'noble expression' "
              "consist of?",
         "opts": [
             "Eloquent, diplomatically softened speech",
             "Simple correspondence between what one claims and what "
             "actually happened, in either direction",
             "Speech that avoids all difficult topics",
             "Speech given only by monastics"],
         "correct": 1,
         "expl": "Truthfulness as accurate correspondence, not as tact or "
                 "eloquence."},
        {"q": "What four categories does this discourse share with AN "
              "8.67?",
         "opts": [
             "Wealth, status, education, and beauty",
             "Seeing, hearing, thinking, and knowing",
             "Faith, ethics, generosity, and wisdom",
             "The four noble truths"],
         "correct": 1,
         "expl": "The identical four categories, now crossed against "
                 "truthful rather than false claims."},
        {"q": "According to the guide, what does reading AN 8.67 and AN "
              "8.68 together make visible?",
         "opts": [
             "That truthfulness is an arbitrary social convention",
             "That truthfulness is a structural property — the same "
             "eight-slot grid filled with lies or with truth",
             "That the two discourses contradict each other",
             "That only some categories require truthfulness"],
         "correct": 1,
         "expl": "A structural, not merely moralistic, way of "
                 "understanding truthful versus false speech."},
        {"q": "What is the first noble expression named?",
         "opts": [
             "Saying you've seen something you haven't",
             "Saying you haven't seen something, and you haven't",
             "Refusing to speak at all",
             "Speaking only in riddles"],
         "correct": 1,
         "expl": "A truthful denial, mirroring AN 8.67's first ignoble "
                 "expression."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.67's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("The identical grid, truthfully filled", [
            "seeing, hearing, thinking, knowing —",
            "affirmed or denied, but now",
            "matching what actually happened",
        ]),
        ("Truthfulness as correspondence", [
            "not eloquence, not tact —",
            "simply: does the claim match",
            "what actually occurred?",
        ]),
        ("A pair making truth structural", [
            "the same eight-slot grid",
            "filled with lies, or with truth —",
            "only the correspondence changes",
        ]),
        ("Cross-references", [
            "AN 8.67 &middot; previous, the mirror-image ignoble "
            "expressions",
            "AN 8.69 &middot; next, the eight assemblies the Buddha "
            "recalls approaching",
        ]),
    ],
    further=[
        '<a href="%s/an8.68/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.67.html">AN 8.67 &middot; Ignoble Expressions</a> &mdash; previous.',
        '<a href="an-8.69.html">AN 8.69 &middot; Assemblies</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.69 — Parisāsutta
# --------------------------------------------------------------------------- #
page(
    69, "Parisā", "Assemblies",
    vagga=VAGGA_7,
    meta_title="AN 8.69 — Assemblies | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Parisāsutta, the Buddha's own account of approaching eight kinds "
        "of assembly — from aristocrats to Māras to divinities — matching "
        "his appearance and voice to each while teaching, then vanishing "
        "leaving them uncertain whether he was god or human. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, in first-person autobiographical "
                     "account"),
        ("Form", "Eight assemblies named, then a single episode described "
                 "in full for the first and compressed by ellipsis for the "
                 "remaining seven"),
        ("Length", "~2 minutes to read"),
        ("Related to AN 8.64's own deity account", "This discourse "
                                                    "extends the Buddha's "
                                                    "own first-person "
                                                    "account of "
                                                    "interacting with "
                                                    "beings beyond the "
                                                    "human realm, met "
                                                    "already at AN 8.64, "
                                                    "now widened to eight "
                                                    "kinds of assembly "
                                                    "spanning both human "
                                                    "society and several "
                                                    "orders of gods and "
                                                    "Māras"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "vivid account, notable for what it says about "
                       "adaptability and for the deliberate ambiguity the "
                       "Buddha leaves behind him"),
    ],
    why=(
        "The Buddha recalls approaching eight kinds of assembly &mdash; "
        "aristocrats, brahmins, householders, ascetics, the gods of the "
        "four great kings, the gods of the thirty-three, Māras, and "
        "divinities &mdash; in each case sitting, conversing, and "
        "teaching until his own appearance and voice matched theirs, then "
        "vanishing afterward so thoroughly that none of them ever knew "
        "whether they'd been speaking with a god or a human."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha recalls approaching eight distinct kinds of "
            "assembly &mdash; four human and four divine or demonic "
            "&mdash; and in every single case, his own appearance and "
            "voice became just like theirs while he taught, and he "
            "vanished afterward leaving each assembly permanently unsure "
            "whether they had been addressed by a god or a human."]),
        ("Eight assemblies, spanning human and beyond", [
            "The eight named assemblies move outward from ordinary human "
            "society &mdash; aristocrats, brahmins, householders, "
            "ascetics &mdash; into progressively less familiar company: "
            "the gods of the four great kings, the gods of the "
            "thirty-three, Māras, and finally divinities (the Brahmā "
            "realm), together spanning the full range of beings this "
            "literature recognizes as capable of receiving a Dhamma talk."]),
        ("Matching appearance and voice, in every single case", [
            "The identical detail recurs across all eight assemblies: the "
            "Buddha's own appearance and voice became just like those of "
            "whichever assembly he addressed &mdash; a capacity for "
            "adaptation the discourse states plainly and without further "
            "explanation, applied uniformly whether the audience was "
            "human, divine, or demonic."]),
        ("Vanishing into deliberate ambiguity", [
            "The discourse's own emphasis falls less on the teaching "
            "given than on what happened after: in every one of the eight "
            "cases, once the Buddha finished speaking and vanished, the "
            "assembly was left permanently unable to determine whether "
            "they had just been taught by a god or a human &mdash; an "
            "ambiguity the account presents as consistent and "
            "intentional, not accidental."]),
    ],
    terms=[
        ("khattiyaparisā, brāhmaṇaparisā, gahapatiparisā, "
         "samaṇaparisā",
         "&ldquo;the assemblies of aristocrats, brahmins, householders, "
         "and ascetics&rdquo; &mdash; the four human assemblies opening "
         "the list."),
        ("cātumahārājikaparisā, tāvatiṁsaparisā, māraparisā, "
         "brahmaparisā",
         "&ldquo;an assembly of the gods of the four great kings... the "
         "thirty-three... Māras... divinities&rdquo; &mdash; the four "
         "non-human assemblies closing the list."),
        ("tādisova me vaṇṇo hoti, tādisī me byappathi",
         "&ldquo;my appearance and voice became just like theirs&rdquo; "
         "&mdash; the identical adaptive detail recurring across all "
         "eight assemblies."),
        ("ko nu kho ayaṁ bhāsati devo vā manusso vā",
         "&ldquo;who is this that speaks? Is it a god or a human?&rdquo; "
         "&mdash; the question each assembly is left with, unresolved, "
         "after the Buddha vanishes."),
        ("antaradhāyāmi",
         "&ldquo;I vanished&rdquo; &mdash; the Buddha's own action "
         "closing each of the eight encounters, leaving the deliberate "
         "ambiguity behind him."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's own account of approaching "
        "eight kinds of assembly. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight assemblies, named"),
        ("p", "&sect;1", "an8.69:1.1-1.3"),
        ("h3", "The first assembly, in full"),
        ("p", "&sect;2", "an8.69:1.4-1.12"),
        ("h3", "The remaining seven assemblies"),
        ("p", "&sect;3", "an8.69:2.1-2.16"),
    ],
    quiz=[
        {"q": "What eight assemblies does the Buddha recall approaching?",
         "opts": [
             "Eight different human kingdoms",
             "Aristocrats, brahmins, householders, ascetics, the gods of "
             "the four great kings, the gods of the thirty-three, Māras, "
             "and divinities",
             "The eight individuals of the noble Saṅgha",
             "Eight different meditation teachers"],
         "correct": 1,
         "expl": "Four human assemblies and four non-human ones, spanning "
                 "the full range of possible audiences."},
        {"q": "What detail recurs identically across all eight assemblies?",
         "opts": [
             "The Buddha always remained silent",
             "His own appearance and voice became just like theirs while "
             "he taught",
             "He always refused to teach",
             "He always brought gifts"],
         "correct": 1,
         "expl": "A capacity for adaptation stated plainly across every "
                 "single encounter."},
        {"q": "What happens after the Buddha finishes teaching and "
              "vanishes, in every case?",
         "opts": [
             "The assembly immediately recognizes him as the Buddha",
             "The assembly is left permanently unable to determine "
             "whether they'd been addressed by a god or a human",
             "The assembly becomes angry",
             "Nothing further is recorded"],
         "correct": 1,
         "expl": "A deliberate ambiguity the account presents as "
                 "consistent, not accidental."},
        {"q": "How does this discourse relate to AN 8.64, earlier in this "
              "chapter?",
         "opts": [
             "No relation at all",
             "It extends the Buddha's own first-person account of "
             "interacting with non-human beings, now widened to eight "
             "kinds of assembly",
             "It directly contradicts AN 8.64",
             "AN 8.64 doesn't mention deities at all"],
         "correct": 1,
         "expl": "A related first-person account, widening the earlier "
                 "discourse's focus on deities specifically."},
        {"q": "How does the source text handle the seven assemblies after "
              "the first?",
         "opts": [
             "Each is described in full, identical detail",
             "They are compressed by internal ellipsis, trusting the "
             "reader to apply the same details described for the first",
             "They are omitted entirely",
             "They are described with entirely different details"],
         "correct": 1,
         "expl": "A self-abbreviation pattern met elsewhere in this book."},
        {"q": "What question is each assembly left with?",
         "opts": [
             "'What is the meaning of suffering?'",
             "'Who is this that speaks? Is it a god or a human?'",
             "'Where did he come from?'",
             "'When will he return?'"],
         "correct": 1,
         "expl": "The unresolved question closing each of the eight "
                 "encounters."},
    ],
    marginalia=[
        ("Eight assemblies, human and beyond", [
            "aristocrats, brahmins,",
            "householders, ascetics —",
            "four kings' gods, thirty-three, Māras, Brahmā",
        ]),
        ("Matching appearance and voice", [
            "the same detail, eight times —",
            "adapted to whoever listens,",
            "human, divine, or demonic",
        ]),
        ("Vanishing into ambiguity", [
            "'was it a god or a human?' —",
            "left unresolved every time,",
            "deliberately, not by accident",
        ]),
        ("Cross-references", [
            "AN 8.68 &middot; previous, noble expressions",
            "AN 8.64 &middot; earlier, the Buddha's own account of "
            "purifying his knowledge of deities",
            "AN 8.70 &middot; next, closing this chapter with the great "
            "earthquake",
        ]),
    ],
    further=[
        '<a href="%s/an8.69/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.68.html">AN 8.68 &middot; Noble Expressions</a> &mdash; previous.',
        '<a href="an-8.64.html">AN 8.64 &middot; At Gayā Head</a> &mdash; earlier, the '
        "Buddha's own account of purifying his knowledge of deities.",
        '<a href="an-8.70.html">AN 8.70 &middot; Earthquakes</a> &mdash; next, closing this '
        "chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.70 — Bhūmicālasutta — closes ch.7 Bhūmicālavagga, its own namesake.
# One of the canon's most significant narrative discourses: the Buddha's
# decision to relinquish the life force, closely paralleling DN 16
# (Mahāparinibbānasutta). Presented with the full weight this moment
# carries, without sentimentalizing it.
# --------------------------------------------------------------------------- #
page(
    70, "Bhūmicāla", "Earthquakes",
    vagga=VAGGA_7,
    meta_title="AN 8.70 — Earthquakes | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Bhūmicālasutta, this chapter's own namesake: the Buddha's "
        "decision to relinquish the life force after Ānanda misses three "
        "clear hints, Māra's request, the great earthquake, and the eight "
        "causes and reasons for such earthquakes — closely paralleling DN "
        "16. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Vesālī, at the Great Wood, then the Cāpāla Shrine"),
        ("Speakers", "The Buddha, Venerable Ānanda, and Māra the Wicked"),
        ("Form", "A narrative in five movements — three missed hints, "
                 "Ānanda's dismissal, Māra's request, the Buddha's "
                 "decision and the earthquake, and finally the eight "
                 "causes of earthquakes generally"),
        ("Length", "~6 minutes to read"),
        ("This chapter's own namesake, and a major turning point", "This "
                                                                   "discourse "
                                                                   "gives "
                                                                   "the "
                                                                   "chapter, "
                                                                   "Bhūmicāla"
                                                                   "vagga, "
                                                                   "its "
                                                                   "name, and "
                                                                   "closely "
                                                                   "parallels "
                                                                   "the "
                                                                   "opening "
                                                                   "of DN 16, "
                                                                   "the "
                                                                   "Mahāparini"
                                                                   "bbāna "
                                                                   "Sutta, "
                                                                   "recounting "
                                                                   "the same "
                                                                   "pivotal "
                                                                   "moment "
                                                                   "from a "
                                                                   "different "
                                                                   "collection"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "emotionally and doctrinally weighty; this reading "
                       "guide presents the narrative with the full weight "
                       "it carries, without sentimentalizing it"),
    ],
    why=(
        "Three times the Buddha drops an unmistakable hint that he could, "
        "if asked, choose to live out a full lifespan, and three times "
        "Ānanda &mdash; his mind as if possessed by Māra &mdash; fails to "
        "ask; once Ānanda leaves, Māra himself asks the Buddha to become "
        "fully extinguished, and the Buddha, judging that his fourfold "
        "community of disciples is now established, agrees to die in "
        "three months, at which point the earth shakes with a great "
        "earthquake, prompting the Buddha to name the eight causes and "
        "reasons for such earthquakes in general."),
    guide=[
        ("The teaching in one sentence", [
            "After Ānanda fails three times to ask the Buddha to remain "
            "for a full lifespan despite an unmistakable hint each time, "
            "Māra himself asks the Buddha to become fully extinguished, "
            "and the Buddha &mdash; judging his fourfold community of "
            "disciples now well established and his teaching successfully "
            "spread &mdash; agrees to die in three months, an act that "
            "triggers a great earthquake, occasioning the Buddha's own "
            "explanation of the eight general causes of such earthquakes."]),
        ("Three missed hints, and a mind possessed by Māra", [
            "Three times the Buddha tells Ānanda, almost in passing, that "
            "whoever has developed the four bases of psychic power could "
            "choose to live out a full lifespan &mdash; and that he "
            "himself has developed them. Three times Ānanda fails to "
            "grasp what's being offered and doesn't beg him to remain, "
            "the text stating plainly that his mind was &ldquo;as if "
            "possessed by Māra&rdquo; &mdash; not a personal failing "
            "softened or excused, but named directly."]),
        ("Māra's request, and a decision already ready to be made", [
            "Once Ānanda has left, Māra approaches directly and asks the "
            "Buddha to die now, citing the Buddha's own earlier statement "
            "that he would not do so until he had competent, established "
            "monk, nun, layman, and laywoman disciples, and until his "
            "spiritual path was successful and widespread &mdash; "
            "conditions Māra argues, and the Buddha does not dispute, are "
            "now fully met."]),
        ("Surrendering the life force, and eight causes of earthquakes", [
            "The Buddha's own response to Māra is measured, not "
            "urgent: &ldquo;the full extinguishment of the Realized One "
            "will be soon... three months from now.&rdquo; At the moment "
            "he mindfully surrenders the life force itself, a great "
            "earthquake occurs; when Ānanda later asks the cause, the "
            "Buddha answers not narrowly about this one earthquake but "
            "generally, naming eight causes and reasons for great "
            "earthquakes &mdash; physical, meditative, and marking the "
            "major turning points of a Buddha's own life, from conception "
            "through final extinguishment."]),
    ],
    terms=[
        ("iddhipādā",
         "&ldquo;the bases of psychic power&rdquo; &mdash; the meditative "
         "development the Buddha names as what would let him choose to "
         "live out a full lifespan, the hint Ānanda fails three times to "
         "grasp."),
        ("māravasaṁvattiko viya",
         "&ldquo;as if possessed by Māra&rdquo; &mdash; the text's own "
         "description of Ānanda's mind at each of the three missed hints, "
         "stated directly rather than softened."),
        ("āyusaṅkhāraṁ ossajji",
         "&ldquo;surrendered the life force&rdquo; &mdash; the Buddha's "
         "own decisive act, at the Cāpāla Shrine, the moment that "
         "triggers the great earthquake."),
        ("ito tiṇṇaṁ māsānaṁ accayena tathāgato parinibbāyissati",
         "&ldquo;three months from now the Realized One will be fully "
         "extinguished&rdquo; &mdash; the Buddha's own measured answer to "
         "Māra, setting the timeframe for what follows."),
        ("aṭṭha imāni ... bhūmicālassa hetū paccayā",
         "&ldquo;these eight causes and reasons for a great "
         "earthquake&rdquo; &mdash; the Buddha's own generalizing answer "
         "to Ānanda, moving from this one earthquake to the full "
         "typology, closing both this discourse and the chapter it names."),
    ],
    text_intro=(
        "The discourse in full: three missed hints, Māra's request, the "
        "Buddha's decision and the earthquake, and the eight general "
        "causes of earthquakes. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three missed hints"),
        ("p", "&sect;1", "an8.70:1.1-4.8"),
        ("h3", "Māra's request"),
        ("p", "&sect;2", "an8.70:5.1-9.1"),
        ("h3", "The Buddha's decision, and the earthquake"),
        ("p", "&sect;3", "an8.70:9.2-10.7"),
        ("h3", "Ānanda asks the cause"),
        ("p", "&sect;4", "an8.70:11.1-13.4"),
        ("h3", "Eight causes and reasons for a great earthquake"),
        ("p", "&sect;5", "an8.70:14.1-21.3"),
    ],
    quiz=[
        {"q": "What hint does the Buddha give Ānanda three times, and how "
              "does Ānanda respond?",
         "opts": [
             "That he wants to travel; Ānanda immediately begs him not to",
             "That whoever has developed the four bases of psychic power "
             "could live out a full lifespan, and that he himself has "
             "developed them; Ānanda fails to grasp the hint each time",
             "That he is unwell; Ānanda calls for a physician",
             "That he wants Ānanda to succeed him; Ānanda refuses"],
         "correct": 1,
         "expl": "An unmistakable hint, missed three times, with the text "
                 "explicitly naming Ānanda's mind as 'possessed by Māra.'"},
        {"q": "What does Māra ask the Buddha to do, and on what grounds?",
         "opts": [
             "To ordain more monks",
             "To become fully extinguished now, since the Buddha's own "
             "earlier conditions for doing so — established disciples, a "
             "successful and widespread teaching — are now met",
             "To travel to a new country",
             "To silence Ānanda"],
         "correct": 1,
         "expl": "A request the Buddha does not dispute the factual basis "
                 "of, though he sets his own timeframe."},
        {"q": "What is the Buddha's own response to Māra's request?",
         "opts": [
             "He refuses outright",
             "He agrees, setting the timeframe himself: three months from "
             "now",
             "He asks Māra to leave without answering",
             "He defers the decision to Ānanda"],
         "correct": 1,
         "expl": "A measured, deliberate answer, not an immediate or "
                 "urgent one."},
        {"q": "What happens at the moment the Buddha surrenders the life "
              "force?",
         "opts": [
             "Nothing observable occurs",
             "A great earthquake, awe-inspiring and hair-raising, with "
             "thunder cracking the sky",
             "A rainstorm begins",
             "Ānanda immediately understands and objects"],
         "correct": 1,
         "expl": "A dramatic physical sign accompanying the decisive "
                 "moment."},
        {"q": "How does the Buddha answer Ānanda's question about the "
              "earthquake's cause?",
         "opts": [
             "He refuses to explain",
             "He generalizes beyond this one earthquake, naming eight "
             "causes and reasons for great earthquakes overall, including "
             "physical causes and the major turning points of a Buddha's "
             "life",
             "He blames Māra entirely",
             "He says earthquakes have no cause"],
         "correct": 1,
         "expl": "A move from the particular event to a general typology, "
                 "closing this chapter."},
        {"q": "What does this discourse's title give to the chapter it "
              "closes, and what does it parallel elsewhere in the canon?",
         "opts": [
             "Nothing in particular; there is no parallel",
             "It gives Bhūmicālavagga its own name, and closely parallels "
             "the opening of DN 16, the Mahāparinibbāna Sutta",
             "It parallels the Dhammapada",
             "It has no connection to any other text"],
         "correct": 1,
         "expl": "A pivotal narrative recounted in more than one "
                 "collection."},
    ],
    marginalia=[
        ("Three hints, missed", [
            "'I could live a full lifespan' —",
            "said three times, unheard three times —",
            "'his mind as if possessed by Māra'",
        ]),
        ("Māra asks, the Buddha answers", [
            "'now is the time' — Māra says —",
            "the Buddha doesn't dispute it,",
            "but sets his own three months",
        ]),
        ("The life force surrendered", [
            "mindful, aware — then the earth",
            "shakes, awe-inspiring, hair-raising —",
            "thunder cracking the sky",
        ]),
        ("Cross-references", [
            "AN 8.69 &middot; previous, the eight assemblies",
            "AN 8.61 &middot; earlier, opening this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an8.70/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.69.html">AN 8.69 &middot; Assemblies</a> &mdash; previous.',
        '<a href="an-8.61.html">AN 8.61 &middot; Desire</a> &mdash; earlier, opening this '
        "chapter.",
    ],
)


VAGGA_8 = "<em>Yamakavagga</em> &mdash; the eighth chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.71 — Paṭhamaparisāvacarasutta -- opens ch.8 Yamakavagga
# --------------------------------------------------------------------------- #
page(
    71, "Paṭhamaparisāvacara", "Inspiring All Around (1st)",
    vagga=VAGGA_8,
    meta_title="AN 8.71 — Inspiring All Around (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamaparisāvacarasutta, opening a new chapter with a completion "
        "ladder — faith, ethics, learning, teaching skill, and finally the "
        "four absorptions and freedom — each rung named as incomplete "
        "until the next is added. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A cumulative ladder of eight qualities, each stage named "
                 "explicitly as 'incomplete' until the next quality is "
                 "added, closing with a single complete mendicant"),
        ("Length", "~2 minutes to read"),
        ("Completion, not mere accumulation", "This discourse doesn't "
                                              "simply list eight qualities "
                                              "side by side; it names each "
                                              "partial combination as "
                                              "explicitly incomplete, "
                                              "framing the whole sequence "
                                              "as a self-assessment "
                                              "exercise rather than a "
                                              "static checklist"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "clear cumulative structure, worth comparing "
                       "against AN 8.72's own slightly different seventh "
                       "rung"),
    ],
    why=(
        "AN 8.71 opens a new chapter with a cumulative ladder: a mendicant "
        "who is faithful but not ethical is incomplete and should become "
        "ethical too; faithful and ethical but not learned is still "
        "incomplete; and so the ladder continues through becoming a "
        "Dhamma speaker, frequenting assemblies, teaching with assurance, "
        "gaining the four absorptions at will, and finally realizing "
        "complete freedom through ending the defilements."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has only some of eight qualities &mdash; "
            "faith, ethics, learning, skill as a Dhamma speaker, comfort "
            "frequenting assemblies, confidence teaching there, the four "
            "absorptions at will, and freedom through ending the "
            "defilements &mdash; is incomplete in that respect and should "
            "actively work to fulfill what's missing, one rung at a time."]),
        ("Each rung named as explicitly incomplete", [
            "Rather than simply listing eight qualities, this discourse "
            "structures itself as a sequence of self-diagnoses: faithful "
            "but not ethical is incomplete; faithful and ethical but not "
            "learned is incomplete; and so on, each partial state given "
            "its own explicit verdict and its own explicit resolution "
            "&mdash; &ldquo;how can I become...&rdquo; &mdash; before the "
            "ladder proceeds to the next rung."]),
        ("A ladder building toward complete impressiveness", [
            "The sequence climbs from foundational virtues (faith, "
            "ethics) through intellectual and social capacities (learning, "
            "Dhamma-speaking, frequenting assemblies, teaching with "
            "confidence) to meditative and liberating attainments (the "
            "four absorptions, freedom through ending defilements) "
            "&mdash; only the mendicant who has climbed every rung is "
            "declared &ldquo;impressive all around... complete in every "
            "respect.&rdquo;"]),
        ("Two versions, differing at the seventh rung", [
            "AN 8.72, immediately following, restates this identical "
            "ladder with one variation: where this discourse's seventh "
            "rung is gaining the four absorptions at will, AN 8.72's "
            "seventh rung is direct meditative experience of the formless "
            "liberations instead &mdash; two different meditative "
            "attainments filling the identical structural position."]),
    ],
    terms=[
        ("aparipūro tasmiṁ aṅge",
         "&ldquo;incomplete in that respect&rdquo; &mdash; the "
         "discourse's own recurring verdict, applied to every partial "
         "combination of qualities before the ladder's next rung is "
         "added."),
        ("dhammakathiko",
         "&ldquo;a Dhamma speaker&rdquo; &mdash; the fourth rung, the "
         "first quality in the ladder concerned with actively "
         "communicating the teaching rather than simply holding it."),
        ("visārado dhammaṁ deseti parisāya",
         "&ldquo;teaches Dhamma to the assembly with assurance&rdquo; "
         "&mdash; the sixth rung, confidence added to the mere presence "
         "in assemblies established at the fifth."),
        ("catunnaṁ jhānānaṁ ābhicetasikānaṁ nikāmalābhī",
         "&ldquo;gets the four absorptions... when they want, without "
         "trouble or difficulty&rdquo; &mdash; the seventh rung in this "
         "discourse's own version, differing from AN 8.72's parallel "
         "seventh rung."),
        ("sabbākāraparipūro",
         "&ldquo;complete in every respect&rdquo; &mdash; the discourse's "
         "own closing verdict, reserved for the mendicant who has climbed "
         "every one of the eight rungs."),
    ],
    text_intro=(
        "The discourse in full: a cumulative eight-rung ladder from faith "
        "to complete freedom. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first two rungs: faith and ethics"),
        ("p", "&sect;1", "an8.71:1.1-2.6"),
        ("h3", "The remaining six rungs, to complete freedom"),
        ("p", "&sect;2", "an8.71:3.1-4.3"),
    ],
    quiz=[
        {"q": "How does this discourse structure its eight qualities, "
              "compared to a simple list?",
         "opts": [
             "As eight unrelated, independent items",
             "As a cumulative ladder, each partial combination explicitly "
             "named 'incomplete' before the next rung is added",
             "As eight mutually exclusive alternatives",
             "As a random, unordered collection"],
         "correct": 1,
         "expl": "A self-assessment sequence, not a static checklist."},
        {"q": "What is the fourth rung in this ladder?",
         "opts": [
             "Wealth", "Being a Dhamma speaker",
             "Physical strength", "Royal favor"],
         "correct": 1,
         "expl": "The first quality concerned with actively communicating "
                 "the teaching, following faith, ethics, and learning."},
        {"q": "What verdict does the discourse give a mendicant who has "
              "climbed every rung of the ladder?",
         "opts": [
             "Still incomplete, since perfection is impossible",
             "'Impressive all around... complete in every respect'",
             "No verdict is given",
             "Warned against pride"],
         "correct": 1,
         "expl": "The discourse's own closing declaration, reserved for "
                 "the full eight rungs."},
        {"q": "How does AN 8.72, immediately following, differ from this "
              "discourse?",
         "opts": [
             "It is entirely unrelated",
             "It restates the identical ladder but with a different "
             "seventh rung — the formless liberations instead of the four "
             "absorptions",
             "It has only four rungs instead of eight",
             "It contradicts this discourse's teaching"],
         "correct": 1,
         "expl": "A near-identical pairing differing at one specific "
                 "position."},
        {"q": "What are the first two rungs of the ladder?",
         "opts": [
             "Wealth and status",
             "Faith and ethics",
             "Physical strength and courage",
             "Skill in debate and eloquence"],
         "correct": 1,
         "expl": "The foundational virtues opening this cumulative "
                 "sequence."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this book."},
    ],
    marginalia=[
        ("A cumulative ladder", [
            "faithful but not ethical:",
            "incomplete — then add ethics,",
            "then learning, speech, and more",
        ]),
        ("Each rung, explicitly named", [
            "not a static checklist —",
            "each partial state diagnosed,",
            "each resolution stated outright",
        ]),
        ("Complete in every respect", [
            "the ladder's own final verdict —",
            "reserved for all eight rungs,",
            "not any partial climb",
        ]),
        ("Cross-references", [
            "AN 8.70 &middot; earlier, closing the previous chapter",
            "AN 8.72 &middot; next, the same ladder with a different "
            "seventh rung",
        ]),
    ],
    further=[
        '<a href="%s/an8.71/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.70.html">AN 8.70 &middot; Earthquakes</a> &mdash; earlier, closing '
        "the previous chapter.",
        '<a href="an-8.72.html">AN 8.72 &middot; Inspiring All Around (2nd)</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.72 — Dutiyaparisāvacarasutta
# --------------------------------------------------------------------------- #
page(
    72, "Dutiyaparisāvacara", "Inspiring All Around (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 8.72 — Inspiring All Around (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyaparisāvacarasutta, restating AN 8.71's completion ladder "
        "with the formless liberations replacing the four absorptions at "
        "the seventh rung. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The identical cumulative ladder as AN 8.71, differing "
                 "only at the seventh rung"),
        ("Length", "~2 minutes to read"),
        ("One rung swapped, the rest identical", "Six of the eight rungs "
                                                 "and the closing verdict "
                                                 "match AN 8.71 word for "
                                                 "word; only the seventh "
                                                 "rung changes, from the "
                                                 "four absorptions to the "
                                                 "formless liberations"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; best "
                       "read directly alongside AN 8.71 to isolate exactly "
                       "what changes"),
    ],
    why=(
        "AN 8.72 restates AN 8.71's identical completion ladder &mdash; "
        "faith, ethics, learning, Dhamma-speaking, frequenting assemblies, "
        "teaching with assurance &mdash; but swaps the seventh rung: "
        "rather than the four absorptions, this discourse's seventh "
        "quality is direct meditative experience of the formless "
        "liberations, transcending form entirely."),
    guide=[
        ("The teaching in one sentence", [
            "The same eight-rung completion ladder as AN 8.71 holds here "
            "too, with one substitution: where AN 8.71's seventh rung is "
            "gaining the four absorptions at will, this discourse's "
            "seventh rung is direct meditative experience of the peaceful "
            "formless liberations, transcending form."]),
        ("Six rungs and the closing verdict, unchanged", [
            "Faith, ethics, learning, being a Dhamma speaker, frequenting "
            "assemblies, and teaching with assurance all match AN 8.71 "
            "word for word, as does the closing verdict for the mendicant "
            "who completes every rung: &ldquo;impressive all around... "
            "complete in every respect.&rdquo;"]),
        ("Formless liberations, not the four absorptions", [
            "The substitution at the seventh rung is meaningful, not "
            "arbitrary: the four absorptions (met at AN 8.71) are "
            "form-based meditative attainments, while the formless "
            "liberations named here &mdash; the same territory covered by "
            "the eight liberations at AN 8.66 &mdash; move beyond form "
            "entirely, a different and more advanced meditative register "
            "filling the identical structural position."]),
        ("Two complete paths to the same completeness", [
            "Rather than treating one version as more authoritative than "
            "the other, this pairing suggests two viable routes through "
            "the same seven preceding rungs to the same final "
            "completeness &mdash; a mendicant might complete the ladder "
            "through form-based absorption or through formless "
            "liberation, both counting as full completion once paired "
            "with the shared eighth rung of freedom through ending "
            "defilements."]),
    ],
    terms=[
        ("santā vimokkhā atikkamma rūpe āruppā",
         "&ldquo;the peaceful liberations that are formless, transcending "
         "form&rdquo; &mdash; this discourse's own seventh rung, replacing "
         "AN 8.71's four absorptions at the same structural position."),
        ("aparipūro tasmiṁ aṅge",
         "&ldquo;incomplete in that respect&rdquo; &mdash; the identical "
         "recurring verdict as AN 8.71, applied to every partial "
         "combination before the ladder's completion."),
        ("dhammakathiko, parisāvacaro, visārado",
         "the shared middle rungs &mdash; Dhamma speaker, one who "
         "frequents assemblies, one who teaches with assurance &mdash; "
         "identical in both this discourse and AN 8.71."),
        ("āsavānaṁ khayā anāsavaṁ cetovimuttiṁ",
         "&ldquo;the undefiled freedom of heart... through the ending of "
         "defilements&rdquo; &mdash; the shared eighth and final rung, "
         "identical in both versions of this ladder."),
        ("sabbākāraparipūro",
         "&ldquo;complete in every respect&rdquo; &mdash; the identical "
         "closing verdict as AN 8.71, reached here by a slightly "
         "different path."),
    ],
    text_intro=(
        "The discourse in full: the same completion ladder as AN 8.71, "
        "with the formless liberations replacing the four absorptions. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first two rungs: faith and ethics"),
        ("p", "&sect;1", "an8.72:1.1-2.1"),
        ("h3", "The remaining six rungs, to complete freedom"),
        ("p", "&sect;2", "an8.72:2.2-3.3"),
    ],
    quiz=[
        {"q": "What single change distinguishes this discourse from AN "
              "8.71?",
         "opts": [
             "Every rung is entirely different",
             "Only the seventh rung changes — the formless liberations "
             "replace the four absorptions, everything else matches word "
             "for word",
             "This discourse has only four rungs",
             "The closing verdict is different"],
         "correct": 1,
         "expl": "A single, meaningful substitution within an otherwise "
                 "identical ladder."},
        {"q": "According to the guide, why is the substitution at the "
              "seventh rung meaningful rather than arbitrary?",
         "opts": [
             "It isn't meaningful; it's a random variation",
             "The four absorptions are form-based, while the formless "
             "liberations move beyond form entirely — a different, more "
             "advanced meditative register",
             "The formless liberations are easier to attain",
             "There is no actual difference between the two"],
         "correct": 1,
         "expl": "Two genuinely different meditative attainments filling "
                 "the same structural position."},
        {"q": "How does this discourse's seventh rung relate to AN 8.66?",
         "opts": [
             "No relation at all",
             "It covers the same territory as the eight liberations named "
             "at AN 8.66",
             "It directly contradicts AN 8.66",
             "AN 8.66 is about something entirely unrelated"],
         "correct": 1,
         "expl": "A connection to the classic liberation typology met "
                 "earlier in this chapter."},
        {"q": "According to the guide, what does this pairing (AN 8.71 and "
              "8.72) suggest?",
         "opts": [
             "That one version is more authoritative than the other",
             "Two viable routes through the same preceding rungs to the "
             "same final completeness",
             "That the two discourses contradict each other",
             "That only monastics can achieve either path"],
         "correct": 1,
         "expl": "Two complete paths, not a correction of one by the "
                 "other."},
        {"q": "What are the shared, unchanged rungs between this discourse "
              "and AN 8.71?",
         "opts": [
             "Only the first rung",
             "Faith, ethics, learning, being a Dhamma speaker, frequenting "
             "assemblies, teaching with assurance, and the final freedom "
             "through ending defilements",
             "None; every rung differs",
             "Only the closing verdict"],
         "correct": 1,
         "expl": "Seven of the eight rungs, unchanged word for word."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.71's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("One rung swapped", [
            "the seventh becomes formless —",
            "beyond form entirely,",
            "not the four absorptions",
        ]),
        ("Six rungs, unchanged", [
            "faith, ethics, learning,",
            "speaking, assemblies, assurance —",
            "identical to AN 8.71",
        ]),
        ("Two paths, one completeness", [
            "form-based or formless —",
            "either route reaches",
            "the same final freedom",
        ]),
        ("Cross-references", [
            "AN 8.71 &middot; previous, the same ladder with the four "
            "absorptions at the seventh rung",
            "AN 8.73 &middot; next, the famous mindfulness-of-death "
            "teaching",
        ]),
    ],
    further=[
        '<a href="%s/an8.72/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.71.html">AN 8.71 &middot; Inspiring All Around (1st)</a> &mdash; '
        "previous.",
        '<a href="an-8.73.html">AN 8.73 &middot; Mindfulness of Death (1st)</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.73 — Paṭhamamaraṇassatisutta -- famous discourse on urgency in
# meditation.
# --------------------------------------------------------------------------- #
page(
    73, "Paṭhamamaraṇassati", "Mindfulness of Death (1st)",
    vagga=VAGGA_8,
    meta_title="AN 8.73 — Mindfulness of Death (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamamaraṇassatisutta, a famous discourse in which mendicants "
        "confess eight escalating degrees of imagined remaining lifespan "
        "— from a day and night down to a single breath — and the Buddha "
        "judges only the shortest two truly diligent. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Ñātika, at the brick house"),
        ("Speakers", "The Buddha and several unnamed mendicants, one after "
                     "another"),
        ("Form", "A direct question, eight sequential confessions each "
                 "shortening the imagined remaining lifespan, and the "
                 "Buddha's own verdict sorting them into diligent and "
                 "negligent"),
        ("Length", "~2 minutes to read"),
        ("A famous teaching on urgency", "This discourse's escalating "
                                         "structure — imagining "
                                         "successively shorter remaining "
                                         "lifespans down to a single "
                                         "breath — is among the most "
                                         "widely cited teachings on "
                                         "spiritual urgency in this "
                                         "literature"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "vivid and accessible, with a sharp, unsentimental "
                       "verdict at its close"),
    ],
    why=(
        "Asked whether they develop mindfulness of death, one mendicant "
        "after another confesses to the Buddha a progressively shorter "
        "imagined remaining lifespan &mdash; a day and night, a day, half "
        "a day, an almsmeal, half an almsmeal, several mouthfuls, a "
        "single mouthful, a single breath &mdash; and the Buddha declares "
        "only the final two, developed with the urgency of a single "
        "mouthful or a single breath, count as genuinely diligent."),
    guide=[
        ("The teaching in one sentence", [
            "Eight mendicants each describe developing mindfulness of "
            "death by imagining a progressively shorter remaining "
            "lifespan &mdash; from a full day and night down to the time "
            "it takes to breathe out after breathing in &mdash; and the "
            "Buddha judges only the final two, the single mouthful and "
            "the single breath, as genuinely diligent practice; the "
            "other six, however sincerely meant, he calls negligent."]),
        ("Eight confessions, each shorter than the last", [
            "One mendicant after another volunteers their own practice: "
            "wishing to live another day and night, then a day, then half "
            "a day, then the time to eat an almsmeal, then half an "
            "almsmeal, then four or five mouthfuls, then a single "
            "mouthful, then finally a single breath &mdash; each reciting "
            "the identical framing, that with this much time they could "
            "focus on the Buddha's instructions and achieve a great deal."]),
        ("A sharp verdict, not an equal validation", [
            "Rather than praising all eight mendicants equally for their "
            "sincerity, the Buddha draws a clear line: the six who "
            "measure their urgency in days, half-days, or meals are "
            "called negligent, living carelessly, developing mindfulness "
            "of death only slackly &mdash; only the two who measure it in "
            "a single mouthful or a single breath are called diligent."]),
        ("Urgency measured in breaths, not days", [
            "The discourse's real teaching lies in where it draws this "
            "line: even wishing for a full day and night of remaining "
            "life, which sounds urgent by ordinary standards, is judged "
            "insufficiently urgent here. Only awareness pitched to the "
            "scale of a single mouthful or breath meets the Buddha's own "
            "standard for genuine diligence."]),
    ],
    terms=[
        ("maraṇassati",
         "&ldquo;mindfulness of death&rdquo; &mdash; this discourse's own "
         "subject, said to have freedom from death itself as its "
         "objective and culmination."),
        ("rattindivaṁ jīveyyaṁ",
         "&ldquo;if I'd only live for another day and night&rdquo; "
         "&mdash; the first and least urgent of the eight confessions."),
        ("ekaṁ ālopaṁ saṅkhāditvā ajjhoharaṇamattaṁ jīveyyaṁ",
         "&ldquo;if I'd only live as long as it takes to chew and swallow "
         "a single mouthful&rdquo; &mdash; the seventh confession, one of "
         "the two the Buddha calls diligent."),
        ("assasitvā vā passasati, passasitvā vā assasati",
         "&ldquo;to breathe out after breathing in, or to breathe in "
         "after breathing out&rdquo; &mdash; the eighth and shortest "
         "confession, the most urgent measure of remaining life named in "
         "this discourse."),
        ("pamattā viharanti, dandhaṁ maraṇassatiṁ bhāventi",
         "&ldquo;live negligently... slackly develop mindfulness of "
         "death&rdquo; &mdash; the Buddha's own verdict on the first six "
         "mendicants, despite their evident sincerity."),
    ],
    text_intro=(
        "The discourse in full: eight mendicants' confessions and the "
        "Buddha's own verdict sorting them into diligent and negligent. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha's question"),
        ("p", "&sect;1", "an8.73:1.1-1.7"),
        ("h3", "Eight confessions, each shorter than the last"),
        ("p", "&sect;2", "an8.73:2.1-9.6"),
        ("h3", "The Buddha's verdict"),
        ("p", "&sect;3", "an8.73:10.1-12.3"),
    ],
    quiz=[
        {"q": "What do the eight mendicants each confess to the Buddha?",
         "opts": [
             "Eight different meditation postures",
             "A progressively shorter imagined remaining lifespan, from a "
             "day and night down to a single breath",
             "Eight different monastic offenses",
             "Eight different reasons for joining the Saṅgha"],
         "correct": 1,
         "expl": "An escalating sequence of decreasing time-scales for "
                 "urgency."},
        {"q": "How does the Buddha judge the first six mendicants' "
              "practice, despite their evident sincerity?",
         "opts": [
             "As equally excellent to the last two",
             "As negligent — living carelessly, developing mindfulness of "
             "death only slackly",
             "As harmful and to be avoided",
             "As irrelevant to spiritual practice"],
         "correct": 1,
         "expl": "A sharp, unsentimental verdict, not an equal validation "
                 "of every sincere effort."},
        {"q": "Which two confessions does the Buddha call genuinely "
              "diligent?",
         "opts": [
             "A day and night, and a day",
             "A single mouthful, and a single breath",
             "Half a day, and an almsmeal",
             "None of the eight are called diligent"],
         "correct": 1,
         "expl": "The two shortest, most urgent time-scales named in the "
                 "sequence."},
        {"q": "According to the guide, where does the discourse's real "
              "teaching lie?",
         "opts": [
             "In praising all eight mendicants equally",
             "In where it draws the line — even a full day and night of "
             "imagined remaining life is judged insufficiently urgent",
             "In condemning meditation on death entirely",
             "In requiring literal starvation"],
         "correct": 1,
         "expl": "A standard for urgency pitched far higher than ordinary "
                 "expectations."},
        {"q": "What framing does each mendicant repeat identically in "
              "their confession?",
         "opts": [
             "A request for more food",
             "That with this much remaining time, they could focus on the "
             "Buddha's instructions and achieve a great deal",
             "A complaint about monastic life",
             "A request to leave the Saṅgha"],
         "correct": 1,
         "expl": "The shared framing across all eight confessions, "
                 "varying only in the timeframe."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove", "Ñātika, at the brick house",
             "Rājagaha, on Vulture's Peak", "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A setting shared with AN 8.74, immediately following."},
    ],
    marginalia=[
        ("Eight confessions, shrinking", [
            "a day and night, a day,",
            "half a day, an almsmeal —",
            "down to a single breath",
        ]),
        ("A sharp line drawn", [
            "not all eight praised equally —",
            "six called negligent,",
            "only the last two, diligent",
        ]),
        ("Urgency measured in breaths", [
            "even a full day and night",
            "judged insufficiently urgent —",
            "the standard set far higher",
        ]),
        ("Cross-references", [
            "AN 8.72 &middot; previous, the second completion ladder",
            "AN 8.74 &middot; next, the practical method behind this same "
            "urgency",
        ]),
    ],
    further=[
        '<a href="%s/an8.73/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.72.html">AN 8.72 &middot; Inspiring All Around (2nd)</a> &mdash; '
        "previous.",
        '<a href="an-8.74.html">AN 8.74 &middot; Mindfulness of Death (2nd)</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.74 — Dutiyamaraṇassatisutta
# --------------------------------------------------------------------------- #
page(
    74, "Dutiyamaraṇassati", "Mindfulness of Death (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 8.74 — Mindfulness of Death (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyamaraṇassatisutta, the practical method behind AN 8.73's "
        "urgency: reflecting each morning and evening on the causes that "
        "could kill you, then treating any unabandoned unskillful quality "
        "like a fire on your own head. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Ñātika, at the brick house, the same setting as AN "
                    "8.73"),
        ("Speakers", SPEAKER),
        ("Form", "A single method described once for evening reflection "
                 "and once for morning reflection, each branching into two "
                 "outcomes depending on what the self-check reveals"),
        ("Length", "~2 minutes to read"),
        ("The method behind AN 8.73's standard", "Where AN 8.73 sorted "
                                                  "eight mendicants' "
                                                  "practices into diligent "
                                                  "and negligent without "
                                                  "explaining the method "
                                                  "itself, this discourse "
                                                  "supplies the actual "
                                                  "procedure: a concrete "
                                                  "self-check performed "
                                                  "twice daily"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "practical, repeatable method rather than an "
                       "abstract standard"),
    ],
    why=(
        "AN 8.74 supplies the practical method behind AN 8.73's standard "
        "of urgency: as day turns to night, and again as night turns to "
        "day, a mendicant reflects on the many causes &mdash; snakebite, "
        "stumbling, illness, attack &mdash; that could kill them, then "
        "checks whether any unabandoned unskillful quality would obstruct "
        "their progress if they died that very night or day, applying the "
        "urgency of extinguishing a fire on their own head if so."),
    guide=[
        ("The teaching in one sentence", [
            "Twice daily, as day turns to night and as night turns to "
            "day, a mendicant should reflect on the many ordinary causes "
            "of death, then check whether any unabandoned unskillful "
            "quality would obstruct their progress if they died that very "
            "night or day &mdash; and if so, apply the same urgency "
            "they'd use to extinguish a fire on their own head."]),
        ("A concrete list of ordinary dangers", [
            "Rather than treating death abstractly, the discourse names "
            "specific, ordinary causes: snakebite, scorpion or centipede "
            "sting, stumbling off a cliff, food poisoning, disturbances of "
            "bile, phlegm, or wind, and attack by humans or non-humans "
            "&mdash; the same everyday vulnerabilities anyone might face, "
            "not exotic or remote dangers."]),
        ("A check with two branches, applied twice daily", [
            "The reflection isn't an end in itself; it leads to a "
            "concrete self-check &mdash; are there unabandoned "
            "unskillful qualities that would obstruct progress if death "
            "came tonight or today? If yes, extraordinary urgency is "
            "called for. If no, the mendicant should instead meditate with "
            "rapture and joy, training day and night in skillful "
            "qualities &mdash; the same reflection performed each evening "
            "and again each morning."]),
        ("Fire on the head, not a metaphor softened", [
            "The discourse's own simile for the urgency required is "
            "unambiguous: exactly the effort someone would apply to "
            "extinguish their own clothes or head if it were on fire "
            "&mdash; enthusiasm, effort, zeal, vigor, perseverance, "
            "mindfulness, and situational awareness, all at once, "
            "immediately, not gradually worked toward."]),
    ],
    terms=[
        ("divase nikkhante rattiyā patihitāya",
         "&ldquo;as day passes by and night draws close&rdquo; &mdash; "
         "the timing of the first of the two daily reflections this "
         "discourse describes."),
        ("bahūhipi kho maraṇassa hetūhi mareyyaṁ",
         "&ldquo;I might die of many causes&rdquo; &mdash; the reflection "
         "opening each check, naming snakebite, stumbling, illness, and "
         "attack among the causes."),
        ("antarāyāya me assā'ti",
         "&ldquo;it would be an obstacle to my progress&rdquo; &mdash; "
         "the discourse's own framing of why any unabandoned unskillful "
         "quality matters, tied directly to the possibility of dying "
         "before it's given up."),
        ("ādittacelo vā ādittasīso vā",
         "&ldquo;your clothes or head were on fire&rdquo; &mdash; the "
         "discourse's own simile for the level of urgency called for when "
         "the self-check reveals something unabandoned."),
        ("pāmojjabahulo vihareyya kusalesu dhammesu ahorattānusikkhī",
         "&ldquo;meditate with rapture and joy, training day and night in "
         "skillful qualities&rdquo; &mdash; the alternative outcome, when "
         "the self-check finds nothing left to abandon."),
    ],
    text_intro=(
        "The discourse in full: the twice-daily reflection and self-check "
        "behind AN 8.73's standard of urgency. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Evening reflection, and its two outcomes"),
        ("p", "&sect;1", "an8.74:1.1-5.2"),
        ("h3", "Morning reflection, and closing"),
        ("p", "&sect;2", "an8.74:6.1-9.3"),
    ],
    quiz=[
        {"q": "How does this discourse relate to AN 8.73?",
         "opts": [
             "No relation at all",
             "It supplies the actual method behind AN 8.73's standard of "
             "urgency — a concrete twice-daily self-check",
             "It contradicts AN 8.73's teaching",
             "It repeats AN 8.73 word for word"],
         "correct": 1,
         "expl": "A practical procedure explaining how the urgency in AN "
                 "8.73 is actually cultivated."},
        {"q": "What ordinary causes of death does this discourse name?",
         "opts": [
             "Only old age",
             "Snakebite, scorpion or centipede sting, stumbling off a "
             "cliff, food poisoning, illness, and attack",
             "Only warfare",
             "Only accidents while traveling"],
         "correct": 1,
         "expl": "Concrete, everyday vulnerabilities, not exotic or "
                 "remote dangers."},
        {"q": "What two outcomes does the self-check branch into?",
         "opts": [
             "Both outcomes require the same response",
             "If unabandoned unskillful qualities are found, apply "
             "extraordinary urgency; if none are found, meditate with "
             "rapture and joy",
             "Only one outcome is possible",
             "The self-check has no practical outcome"],
         "correct": 1,
         "expl": "A genuine branch depending on what the reflection "
                 "actually reveals."},
        {"q": "What simile does the discourse use for the required "
              "urgency?",
         "opts": [
             "A slow, gradual climb up a mountain",
             "Extinguishing a fire on one's own clothes or head",
             "Planting and tending a garden",
             "Waiting patiently for rain"],
         "correct": 1,
         "expl": "An unambiguous image of immediate, total effort, not "
                 "gradual improvement."},
        {"q": "How often is this reflection performed, according to the "
              "discourse?",
         "opts": [
             "Once a year", "Twice daily — as day turns to night, and as "
                             "night turns to day",
             "Only once, at ordination", "Only when illness strikes"],
         "correct": 1,
         "expl": "A regular, twice-daily practice, not a one-time "
                 "exercise."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Ñātika, at the brick house, the same setting as AN 8.73",
             "Rājagaha, on Vulture's Peak", "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "The identical setting as the preceding discourse."},
    ],
    marginalia=[
        ("Ordinary dangers, named plainly", [
            "snakebite, stumbling,",
            "illness, attack — not exotic,",
            "but everyday vulnerabilities",
        ]),
        ("A twice-daily check", [
            "evening and morning both —",
            "anything left unabandoned",
            "that would obstruct my progress?",
        ]),
        ("Fire on the head", [
            "not a softened metaphor —",
            "the exact urgency you'd bring",
            "to your own burning clothes",
        ]),
        ("Cross-references", [
            "AN 8.73 &middot; previous, the eight confessions this "
            "discourse's method underlies",
            "AN 8.75 &middot; next, a condensed restatement of the "
            "Dīghajāṇu teaching",
        ]),
    ],
    further=[
        '<a href="%s/an8.74/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.73.html">AN 8.73 &middot; Mindfulness of Death (1st)</a> &mdash; '
        "previous.",
        '<a href="an-8.75.html">AN 8.75 &middot; Accomplishments (1st)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.75 — Paṭhamasampadāsutta
# --------------------------------------------------------------------------- #
page(
    75, "Paṭhamasampadā", "Accomplishments (1st)",
    vagga=VAGGA_8,
    meta_title="AN 8.75 — Accomplishments (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭhamasampadāsutta, a condensed restatement of AN 8.54's lay "
        "ethics teaching as a bare eight-item list and verse, without the "
        "narrative frame or Dīghajāṇu's own request. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same eight accomplishments as AN 8.54, given as a "
                 "bare list and verse with no explanatory prose at all"),
        ("Length", "under 1 minute to read"),
        ("The third appearance of this teaching", "The same eightfold "
                                                   "pattern — initiative, "
                                                   "protection, good "
                                                   "friendship, balanced "
                                                   "finances, faith, "
                                                   "ethics, generosity, "
                                                   "wisdom — has now "
                                                   "appeared at AN 8.54 "
                                                   "(Dīghajāṇu), AN 8.55 "
                                                   "(Ujjaya), and here, "
                                                   "stripped down to its "
                                                   "barest form"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and condensed, best understood by comparing "
                       "against its fuller statement at AN 8.54"),
    ],
    why=(
        "AN 8.75 restates the same eight accomplishments taught in full "
        "at AN 8.54 and AN 8.55 &mdash; initiative, protection, good "
        "friendship, balanced finances, faith, ethics, generosity, and "
        "wisdom &mdash; but strips away every trace of narrative frame, "
        "questioner, and explanatory prose, presenting only the bare list "
        "and its closing verses."),
    guide=[
        ("The teaching in one sentence", [
            "The eight accomplishments &mdash; initiative, protection, "
            "good friendship, and balanced finances for this life; faith, "
            "ethics, generosity, and wisdom for future lives &mdash; are "
            "named here in their barest form, without Dīghajāṇu's request "
            "or any of AN 8.54's explanatory prose defining each term."]),
        ("A third appearance, stripped to its essentials", [
            "This is the third time this exact eightfold pattern appears "
            "in this book: fully explained with a narrative frame at AN "
            "8.54 (Dīghajāṇu), restated for a different questioner at AN "
            "8.55 (Ujjaya), and now given here with no narrative at all "
            "&mdash; just the bare naming of all eight accomplishments "
            "followed directly by the closing verses."]),
        ("What's lost, and what's kept, in condensation", [
            "Missing entirely from this version: Dīghajāṇu's own "
            "self-description as a layperson who enjoys sensual pleasures, "
            "the appraiser's-scale simile for balanced finances, and the "
            "reservoir simile for the four drains and four inlets on "
            "wealth. What survives is the bare eightfold structure and "
            "the identical closing verses met at AN 8.54."]),
        ("A teaching treated as stable enough to condense", [
            "That this book is willing to present the same eight "
            "accomplishments with progressively less framing &mdash; full "
            "narrative, then bare list &mdash; suggests the underlying "
            "content was considered stable and well-established enough to "
            "stand without repeated justification or narrative "
            "reinforcement."]),
    ],
    terms=[
        ("aṭṭha sampadā",
         "&ldquo;eight accomplishments&rdquo; &mdash; this discourse's "
         "own title-phrase, naming the identical eightfold content met in "
         "fuller form at AN 8.54."),
        ("uṭṭhānasampadā, ārakkhasampadā, kalyāṇamittatā, "
         "samajīvitā",
         "the four this-life accomplishments, named here without any of "
         "AN 8.54's defining explanations."),
        ("saddhāsampadā, sīlasampadā, cāgasampadā, paññāsampadā",
         "the four future-life accomplishments, identical to AN 8.54, "
         "8.55, and the earlier lay-follower discourses at AN 8.49-50."),
        ("uṭṭhātā kammadheyyesu",
         "&ldquo;enterprising in the workplace&rdquo; &mdash; the "
         "opening line of the closing verses, identical to AN 8.54's own "
         "verse."),
        ("dānena vaḍḍhate puñño",
         "&ldquo;merit grows by generosity&rdquo; &mdash; the discourse's "
         "own closing line, identical to AN 8.54's."),
    ],
    text_intro=(
        "The discourse in full: the eight accomplishments, stated bare and "
        "in verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight accomplishments, named"),
        ("p", "&sect;1", "an8.75:1.1-1.4"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.75:2.1-5.4"),
    ],
    quiz=[
        {"q": "How does this discourse's content relate to AN 8.54's?",
         "opts": [
             "Entirely unrelated content",
             "The identical eight accomplishments, stripped of Dīghajāṇu's "
             "narrative frame and all explanatory prose",
             "A contradicting set of eight accomplishments",
             "An expanded version with new material"],
         "correct": 1,
         "expl": "The third appearance of this exact pattern, now in its "
                 "barest form."},
        {"q": "What is missing from this version that AN 8.54 includes?",
         "opts": [
             "Nothing is missing",
             "Dīghajāṇu's self-description, the appraiser's-scale simile, "
             "and the reservoir simile for wealth",
             "The closing verses",
             "The eight accomplishments themselves"],
         "correct": 1,
         "expl": "All narrative and illustrative material removed, "
                 "leaving only the bare structure and verses."},
        {"q": "According to the guide, what does this progressive "
              "condensation suggest about the teaching?",
         "opts": [
             "That it was considered unimportant",
             "That it was considered stable and well-established enough "
             "to stand without repeated narrative reinforcement",
             "That it was a later corruption of the original teaching",
             "That it contradicts the fuller version"],
         "correct": 1,
         "expl": "A teaching trusted to work in condensed form, not "
                 "diminished by the condensation."},
        {"q": "What are the four this-life accomplishments?",
         "opts": [
             "Faith, ethics, generosity, and wisdom",
             "Initiative, protection, good friendship, and balanced "
             "finances",
             "Physical strength, courage, patience, and skill",
             "Wealth, status, education, and beauty"],
         "correct": 1,
         "expl": "The same four qualities met at AN 8.54 and 8.55."},
        {"q": "How many times has this exact eightfold pattern now "
              "appeared in this book?",
         "opts": [
             "Once, only here", "Three times — AN 8.54, 8.55, and this "
                                 "discourse",
             "Ten times", "This is a completely new pattern"],
         "correct": 1,
         "expl": "A recurring pattern, given progressively less framing "
                 "with each restatement."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Kakkarapatta",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, unlike AN 8.54's specific named "
                 "location."},
    ],
    marginalia=[
        ("The same eight, a third time", [
            "initiative, protection,",
            "friendship, balance — then",
            "faith, ethics, generosity, wisdom",
        ]),
        ("Stripped to its essentials", [
            "no Dīghajāṇu, no request,",
            "no reservoir or scale simile —",
            "just the bare structure and verse",
        ]),
        ("Trusted to stand alone", [
            "condensed, not diminished —",
            "a teaching stable enough",
            "to need no repeated framing",
        ]),
        ("Cross-references", [
            "AN 8.74 &middot; previous, the mindfulness-of-death method",
            "AN 8.54 &middot; earlier, this same teaching in its fullest "
            "form",
            "AN 8.76 &middot; next, this same teaching restated once more, "
            "with full explanations",
        ]),
    ],
    further=[
        '<a href="%s/an8.75/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.74.html">AN 8.74 &middot; Mindfulness of Death (2nd)</a> &mdash; '
        "previous.",
        '<a href="an-8.54.html">AN 8.54 &middot; With Dīghajāṇu</a> &mdash; earlier, this '
        "same teaching in its fullest form.",
        '<a href="an-8.76.html">AN 8.76 &middot; Accomplishments (2nd)</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.76 — Dutiyasampadāsutta
# --------------------------------------------------------------------------- #
page(
    76, "Dutiyasampadā", "Accomplishments (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 8.76 — Accomplishments (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Dutiyasampadāsutta, restoring full explanations to AN 8.75's "
        "bare eight accomplishments — matching AN 8.54's content almost "
        "word for word, but with no narrative frame or questioner at all. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same eight accomplishments as AN 8.75, now with "
                 "full explanations restored for each, but still no "
                 "narrative frame"),
        ("Length", "~2 minutes to read"),
        ("Full content, no narrative", "This discourse restores every "
                                       "explanation AN 8.75 stripped away "
                                       "— matching AN 8.54's substance "
                                       "almost word for word — while "
                                       "still omitting Dīghajāṇu, his "
                                       "self-description, and any "
                                       "questioner at all"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the "
                       "fullest explanatory content in this pattern's "
                       "fourth appearance, worth comparing against AN "
                       "8.54's own narrative version"),
    ],
    why=(
        "AN 8.76 restores full explanations to each of the eight "
        "accomplishments AN 8.75 gave only as a bare list &mdash; "
        "matching AN 8.54's explanatory content almost word for word, "
        "including the appraiser's-scale simile &mdash; but still opens "
        "with no narrative frame at all, addressed to the mendicants in "
        "general."),
    guide=[
        ("The teaching in one sentence", [
            "The eight accomplishments &mdash; initiative, protection, "
            "good friendship, balanced finances, faith, ethics, "
            "generosity, and wisdom &mdash; are explained here in full, "
            "matching AN 8.54's own definitions almost word for word, but "
            "with no narrative frame, no Dīghajāṇu, and no questioner at "
            "all."]),
        ("Explanations restored, narrative still absent", [
            "Where AN 8.75 gave only the bare naming of all eight "
            "accomplishments, this discourse restores the full "
            "&ldquo;and what is accomplishment in...&rdquo; explanatory "
            "formula for each one, including the appraiser's-scale simile "
            "for balanced finances &mdash; but the narrative scaffolding "
            "of AN 8.54 (Dīghajāṇu's self-description, his direct "
            "request) never returns."]),
        ("A fourth appearance, isolating content from context", [
            "Across four appearances of this eightfold pattern &mdash; AN "
            "8.54's full narrative, AN 8.55's different questioner, AN "
            "8.75's bare list, and now this discourse's full content "
            "without narrative &mdash; this book effectively runs an "
            "experiment in separating a teaching's substance from the "
            "story that originally carried it."]),
        ("What the reservoir simile alone is missing here", [
            "One detail from AN 8.54 does not reappear even in this "
            "fuller restatement: the reservoir simile for the four drains "
            "and four inlets on wealth (womanizing, drinking, gambling, "
            "bad friends versus their opposites) is absent from this "
            "discourse, marking it as fuller than AN 8.75 but still not a "
            "complete match for AN 8.54's full content."]),
    ],
    terms=[
        ("uṭṭhānasampadā",
         "&ldquo;accomplishment in initiative&rdquo; &mdash; the first "
         "quality, explained here in full, matching AN 8.54's own "
         "definition."),
        ("ārakkhasampadā",
         "&ldquo;accomplishment in protection&rdquo; &mdash; the second "
         "quality, its explanation restored here after AN 8.75's bare "
         "naming."),
        ("nāccogāḷhaṁ nātihīnaṁ",
         "&ldquo;neither too extravagant nor too frugal&rdquo; &mdash; "
         "part of the balanced-finances explanation, including the "
         "appraiser's-scale simile restored from AN 8.54."),
        ("saddhāsampadā, sīlasampadā, cāgasampadā, paññāsampadā",
         "the four future-life accomplishments, explained in full, "
         "identical in substance to AN 8.54, 8.55, and the AN 8.49-50 "
         "lay-follower discourses."),
        ("dānena vaḍḍhate puñño",
         "&ldquo;merit grows by generosity&rdquo; &mdash; the closing "
         "line shared across every appearance of this eightfold pattern "
         "in this book."),
    ],
    text_intro=(
        "The discourse in full: the eight accomplishments, fully "
        "explained, with no narrative frame. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four accomplishments for this life, explained"),
        ("p", "&sect;1", "an8.76:1.1-4.8"),
        ("h3", "Four accomplishments for future lives, explained"),
        ("p", "&sect;2", "an8.76:5.1-9.1"),
        ("h3", "Closing verses"),
        ("p", "&sect;3", "an8.76:10.1-13.4"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 8.75's?",
         "opts": [
             "Identical, still a bare list",
             "It restores full explanations for each of the eight "
             "accomplishments, matching AN 8.54's own definitions almost "
             "word for word",
             "It has fewer accomplishments than AN 8.75",
             "It contradicts AN 8.75's teaching"],
         "correct": 1,
         "expl": "Full content restored, but still without AN 8.54's "
                 "narrative frame."},
        {"q": "What narrative element does this discourse still omit, "
              "despite restoring full explanations?",
         "opts": [
             "The eight accomplishments themselves",
             "Dīghajāṇu, his self-description, and any questioner at all",
             "The closing verses",
             "The definition of balanced finances"],
         "correct": 1,
         "expl": "Full content, but addressed to the mendicants generally "
                 "rather than through a narrative request."},
        {"q": "What detail from AN 8.54 remains absent even in this "
              "fuller restatement?",
         "opts": [
             "The appraiser's-scale simile",
             "The reservoir simile for the four drains and four inlets on "
             "wealth",
             "The four future-life accomplishments",
             "The closing verses"],
         "correct": 1,
         "expl": "A detail marking this discourse as fuller than AN 8.75 "
                 "but not a complete match for AN 8.54."},
        {"q": "According to the guide, what experiment does this book run "
              "across four appearances of this pattern?",
         "opts": [
             "No pattern; each appearance is unrelated",
             "Separating a teaching's substance from the story that "
             "originally carried it, across progressively different "
             "combinations of narrative and content",
             "Testing whether readers notice repetition",
             "Correcting errors in earlier versions"],
         "correct": 1,
         "expl": "A deliberate variation in how much narrative framing "
                 "accompanies the same underlying content."},
        {"q": "What simile is restored for balanced finances in this "
              "discourse?",
         "opts": [
             "The reservoir with four inlets and drains",
             "The appraiser's scale, showing whether income is 'low by "
             "this much or high by this much'",
             "A ship navigating a storm",
             "A garden being watered"],
         "correct": 1,
         "expl": "One simile restored from AN 8.54, though not the "
                 "reservoir simile."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Kakkarapatta",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, like AN 8.75, unlike AN 8.54's named "
                 "location."},
    ],
    marginalia=[
        ("Full explanations, restored", [
            "each accomplishment defined",
            "in full, matching AN 8.54 —",
            "the appraiser's scale returns",
        ]),
        ("Still no narrative", [
            "no Dīghajāṇu, no request —",
            "content restored, but the story",
            "that carried it stays absent",
        ]),
        ("One simile still missing", [
            "the reservoir, four drains,",
            "four inlets — not here either —",
            "fuller than 8.75, not complete",
        ]),
        ("Cross-references", [
            "AN 8.75 &middot; previous, the bare version of this same "
            "teaching",
            "AN 8.77 &middot; next, the eight individuals of AN 8.61, now "
            "taught by Sāriputta",
        ]),
    ],
    further=[
        '<a href="%s/an8.76/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.75.html">AN 8.75 &middot; Accomplishments (1st)</a> &mdash; previous.',
        '<a href="an-8.77.html">AN 8.77 &middot; Desires</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.77 — Icchāsutta (Sāriputta version) -- word-for-word the same
# content as AN 8.61, but taught independently by Sāriputta rather than
# the Buddha.
# --------------------------------------------------------------------------- #
page(
    77, "Icchā", "Desires",
    vagga=VAGGA_8,
    meta_title="AN 8.77 — Desires | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Icchāsutta, in which Sāriputta teaches the mendicants word for "
        "word the same eight individuals AN 8.61 attributed to the "
        "Buddha, crossing effort, outcome, and reaction. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Sāriputta, addressing the mendicants "
                     "directly"),
        ("Form", "The identical combinatorial matrix of eight individuals "
                 "as AN 8.61, now delivered by Sāriputta rather than the "
                 "Buddha"),
        ("Length", "~3 minutes to read"),
        ("The same content, an independent voice", "Every word of this "
                                                    "discourse's eight "
                                                    "individuals matches "
                                                    "AN 8.61, but the "
                                                    "speaker has changed "
                                                    "entirely — Sāriputta "
                                                    "teaches this content "
                                                    "on his own authority, "
                                                    "not relaying the "
                                                    "Buddha's own words in "
                                                    "this instance"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical in content to AN 8.61, notable chiefly "
                       "for its change of speaker"),
    ],
    why=(
        "Sāriputta addresses the mendicants directly and teaches, word "
        "for word, the same eight individuals AN 8.61 attributed to the "
        "Buddha &mdash; crossing whether a secluded mendicant tries for "
        "material things, whether those things come, and whether the "
        "reaction is sorrow, indulgence, or equanimity."),
    guide=[
        ("The teaching in one sentence", [
            "Sāriputta teaches the identical eight individuals as AN "
            "8.61, in the Buddha's absence and on his own authority: only "
            "reaction &mdash; sorrow or indulgence versus equanimity "
            "&mdash; determines whether a mendicant desiring material "
            "things has fallen from the true teaching, regardless of "
            "whether they tried for those things or received them."]),
        ("A word-for-word match, differing only in speaker", [
            "Every one of the eight cases, every phrase describing effort, "
            "outcome, and reaction, and the closing summary all match AN "
            "8.61 precisely. The only substantive change across the two "
            "discourses is who is speaking: the Buddha at AN 8.61, "
            "Sāriputta here, addressing his fellow mendicants directly as "
            "&ldquo;reverends.&rdquo;"]),
        ("A senior disciple teaching independently", [
            "This discourse belongs to a small group in this book where "
            "Sāriputta, the Buddha's foremost disciple in wisdom, teaches "
            "content elsewhere attributed to the Buddha himself, without "
            "any indication that he is merely relaying or repeating a "
            "teaching he received &mdash; a marker of the kind of "
            "independent teaching authority senior disciples are shown "
            "exercising in this literature."]),
        ("Why repetition without variation still matters", [
            "Unlike most paired discourses in this book, which vary some "
            "detail between repetitions, this pairing varies nothing in "
            "content at all &mdash; making the discourse's real interest "
            "not what is taught, already covered fully at AN 8.61, but "
            "that it can be taught this precisely by someone other than "
            "the Buddha."]),
    ],
    terms=[
        ("sāriputto",
         "Venerable Sāriputta, this discourse's own speaker, addressing "
         "his fellow mendicants as &ldquo;reverends&rdquo; rather than "
         "the Buddha's own &ldquo;mendicants.&rdquo;"),
        ("āvuso, bhikkhave",
         "&ldquo;reverends, mendicants&rdquo; &mdash; Sāriputta's own "
         "form of address, distinct from the Buddha's own opening formula "
         "at AN 8.61."),
        ("aṭṭha puggalā santo saṁvijjamānā lokasmiṁ",
         "&ldquo;these eight individuals are found in the world&rdquo; "
         "&mdash; the identical opening formula as AN 8.61, now spoken by "
         "Sāriputta."),
        ("socati kilamati paridevati",
         "&ldquo;sorrows and wails and laments&rdquo; &mdash; the same "
         "bad-reaction phrase as AN 8.61, unchanged across every one of "
         "its four occurrences in this discourse."),
        ("cuto ariyassa dhammavinayā",
         "&ldquo;fallen from the true teaching&rdquo; &mdash; the "
         "identical verdict as AN 8.61, applied to the same four "
         "combinations of effort and outcome paired with bad reaction."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta's own teaching of the same eight "
        "individuals as AN 8.61. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta addresses the mendicants"),
        ("p", "&sect;1", "an8.77:1.1-2.2"),
        ("h3", "Four individuals who have fallen from the true teaching"),
        ("p", "&sect;2", "an8.77:2.3-5.5"),
        ("h3", "Four individuals who have not fallen"),
        ("p", "&sect;3", "an8.77:6.1-9.6"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 8.61's?",
         "opts": [
             "Entirely different content",
             "Word for word identical, including all eight individuals "
             "and the closing summary",
             "A shortened summary of AN 8.61",
             "A contradicting version of the same teaching"],
         "correct": 1,
         "expl": "The only substantive change across the two discourses "
                 "is the speaker."},
        {"q": "Who teaches this discourse's content, unlike AN 8.61?",
         "opts": [
             "Venerable Ānanda", "Venerable Sāriputta, addressing the "
                                  "mendicants on his own authority",
             "Mahāpajāpati Gotamī", "General Sīha"],
         "correct": 1,
         "expl": "A senior disciple teaching independently, not relaying "
                 "the Buddha's words as a report."},
        {"q": "What form of address does Sāriputta use, distinct from the "
              "Buddha's own?",
         "opts": [
             "'Householders'", "'Reverends' (āvuso), rather than the "
                                "Buddha's 'mendicants'",
             "'Your majesty'", "No address is used at all"],
         "correct": 1,
         "expl": "A marker of a fellow-mendicant speaking to peers, "
                 "distinct from the Buddha's own opening formula."},
        {"q": "According to the guide, what makes this discourse's real "
              "interest, given the identical content?",
         "opts": [
             "The content itself, since it's genuinely new",
             "That the identical teaching can be delivered this precisely "
             "by someone other than the Buddha",
             "A hidden contradiction with AN 8.61",
             "Nothing of interest; it's a pure duplicate"],
         "correct": 1,
         "expl": "A marker of independent teaching authority, not new "
                 "content."},
        {"q": "What determines whether a mendicant in this discourse has "
              "fallen from the true teaching?",
         "opts": [
             "Whether they tried hard for material things",
             "Only their reaction — sorrow or indulgence versus "
             "equanimity",
             "Whether they succeeded in getting material things",
             "Their seniority in the Saṅgha"],
         "correct": 1,
         "expl": "The identical determining variable as AN 8.61."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.61's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("Identical content, new speaker", [
            "every word matches AN 8.61 —",
            "only the speaker changes:",
            "Sāriputta, not the Buddha",
        ]),
        ("'Reverends,' not 'mendicants'", [
            "a fellow disciple's address,",
            "not the Buddha's own opening —",
            "peer to peer, not teacher to student",
        ]),
        ("Independent teaching authority", [
            "not relaying, not reporting —",
            "Sāriputta teaches on his own,",
            "the identical eightfold matrix",
        ]),
        ("Cross-references", [
            "AN 8.76 &middot; previous, the fullest version of the "
            "accomplishments teaching",
            "AN 8.61 &middot; earlier, the Buddha's own original teaching "
            "of this identical content",
            "AN 8.78 &middot; next, Sāriputta's own version of the "
            "'good enough' teaching",
        ]),
    ],
    further=[
        '<a href="%s/an8.77/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.76.html">AN 8.76 &middot; Accomplishments (2nd)</a> &mdash; previous.',
        '<a href="an-8.61.html">AN 8.61 &middot; Desire</a> &mdash; earlier, the '
        "Buddha&rsquo;s own original teaching of this identical content.",
        '<a href="an-8.78.html">AN 8.78 &middot; Good Enough</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.78 — Alaṁsutta (Sāriputta version) -- word-for-word the same content
# as AN 8.62, taught independently by Sāriputta.
# --------------------------------------------------------------------------- #
page(
    78, "Alaṁ", "Good Enough",
    vagga=VAGGA_8,
    meta_title="AN 8.78 — Good Enough | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Alaṁsutta, in which Sāriputta teaches word for word the same "
        "eight logical cases AN 8.62 attributed to the Buddha, on which "
        "combinations of six qualities suffice for self- and "
        "other-benefit. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Sāriputta, addressing the mendicants "
                     "directly"),
        ("Form", "The identical eight logical cases as AN 8.62, now "
                 "delivered by Sāriputta"),
        ("Length", "~3 minutes to read"),
        ("The second Sāriputta-Buddha pair in this chapter", "Following "
                                                              "AN 8.77's "
                                                              "identical "
                                                              "relationship "
                                                              "to AN 8.61, "
                                                              "this "
                                                              "discourse "
                                                              "does the "
                                                              "same for AN "
                                                              "8.62 — "
                                                              "Sāriputta "
                                                              "teaching "
                                                              "content "
                                                              "word for "
                                                              "word "
                                                              "identical to "
                                                              "an earlier "
                                                              "discourse "
                                                              "attributed "
                                                              "to the "
                                                              "Buddha"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the "
                       "same logically intricate content as AN 8.62, now "
                       "worth comparing for its change of speaker rather "
                       "than its logical structure"),
    ],
    why=(
        "Sāriputta teaches the mendicants, word for word, the same eight "
        "logical cases AN 8.62 attributed to the Buddha: which "
        "combinations of six underlying qualities &mdash; quick-"
        "wittedness, memory, comprehension, practice, eloquence, and "
        "inspiring others &mdash; make a mendicant good enough for "
        "themselves, for others, for both, or for neither."),
    guide=[
        ("The teaching in one sentence", [
            "Sāriputta delivers the identical eight-case logical teaching "
            "as AN 8.62 on his own authority: comprehension, memory, and "
            "practice serve self-benefit, eloquence and inspiring others "
            "serve other-benefit, and quick-wittedness never changes any "
            "case's verdict."]),
        ("A second matched pair in this chapter", [
            "This discourse and AN 8.77 together form a small set within "
            "this chapter: two discourses whose content is word-for-word "
            "identical to earlier discourses in this same book (AN 8.61 "
            "and AN 8.62 respectively), differing only in that Sāriputta, "
            "not the Buddha, is the speaker."]),
        ("The same logical structure, unchanged", [
            "Every element of AN 8.62's intricate cascading structure "
            "&mdash; six qualities down through five, four, three, and "
            "two, each combination assigned its own verdict for self- and "
            "other-benefit &mdash; appears here exactly as before, with "
            "Sāriputta's own opening address to &ldquo;reverends&rdquo; "
            "the only textual marker distinguishing this discourse from "
            "its earlier counterpart."]),
        ("Why this pairing pattern recurs exactly twice", [
            "That this book pairs exactly two of Sāriputta's own teachings "
            "with exactly two earlier Buddha-attributed discourses (AN "
            "8.61/8.77 and AN 8.62/8.78) &mdash; rather than one, or many "
            "&mdash; suggests a deliberate, bounded demonstration of "
            "Sāriputta's capacity to teach precisely, not an open-ended "
            "pattern extending indefinitely through this chapter."]),
    ],
    terms=[
        ("sāriputto",
         "Venerable Sāriputta, this discourse's own speaker, as at AN "
         "8.77 immediately preceding it."),
        ("khippanisanti dhammesu",
         "&ldquo;quick-witted when it comes to skillful teachings&rdquo; "
         "&mdash; the one quality whose presence or absence never changes "
         "any case's verdict, identical to AN 8.62's own finding."),
        ("alaṁ attano, alaṁ parassa",
         "&ldquo;good enough for themselves... good enough for "
         "others&rdquo; &mdash; the identical dual verdict as AN 8.62, "
         "unchanged in this discourse."),
        ("cha dhammehi samannāgato",
         "&ldquo;with six qualities&rdquo; &mdash; the discourse's own "
         "opening case, cascading down through five, four, three, and two "
         "as at AN 8.62."),
        ("āvuso, bhikkhave",
         "&ldquo;reverends, mendicants&rdquo; &mdash; Sāriputta's own "
         "address, the clearest textual marker distinguishing this "
         "discourse from AN 8.62."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta's own teaching of the same eight "
        "cases as AN 8.62. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six and five qualities: good enough for both"),
        ("p", "&sect;1", "an8.78:1.1-2.9"),
        ("h3", "Four qualities, split two ways"),
        ("p", "&sect;2", "an8.78:3.1-4.9"),
        ("h3", "Three qualities, split two ways"),
        ("p", "&sect;3", "an8.78:5.1-6.9"),
        ("h3", "Two qualities, split two ways"),
        ("p", "&sect;4", "an8.78:7.1-8.9"),
    ],
    quiz=[
        {"q": "How does this discourse's content compare to AN 8.62's?",
         "opts": [
             "Entirely different content",
             "Word for word identical, including the full cascading "
             "eight-case structure",
             "A simplified summary",
             "A contradicting version"],
         "correct": 1,
         "expl": "The second of this chapter's two Sāriputta/Buddha "
                 "content pairs."},
        {"q": "What pattern does this discourse and AN 8.77 together "
              "establish in this chapter?",
         "opts": [
             "No particular pattern",
             "Exactly two discourses where Sāriputta teaches content "
             "word-for-word identical to earlier Buddha-attributed "
             "discourses",
             "A pattern extending through the entire chapter",
             "A pattern found nowhere else in this book"],
         "correct": 1,
         "expl": "A bounded, deliberate demonstration rather than an "
                 "open-ended repetition."},
        {"q": "What quality's presence or absence never changes any "
              "case's verdict, matching AN 8.62's own finding?",
         "opts": [
             "Memory", "Quick-wittedness",
             "Eloquence", "Practice"],
         "correct": 1,
         "expl": "The identical optional quality found in AN 8.62's "
                 "structure."},
        {"q": "What is the only textual marker distinguishing this "
              "discourse from AN 8.62?",
         "opts": [
             "A different set of six qualities",
             "Sāriputta's own opening address to 'reverends,' rather than "
             "the Buddha addressing 'mendicants'",
             "A different number of cases",
             "A contradicting verdict in one case"],
         "correct": 1,
         "expl": "The speaker's own address formula, not any change in "
                 "content."},
        {"q": "What two qualities does the guide identify as serving "
              "self-benefit and other-benefit respectively?",
         "opts": [
             "Wealth for self-benefit, fame for other-benefit",
             "Comprehension/memory/practice for self-benefit, "
             "eloquence/inspiring others for other-benefit",
             "Physical strength for both",
             "Neither quality serves either benefit"],
         "correct": 1,
         "expl": "The same functional split identified at AN 8.62."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.62's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("Identical content, again", [
            "the same cascading structure —",
            "six qualities down through two,",
            "now taught by Sāriputta",
        ]),
        ("A bounded pattern, exactly twice", [
            "AN 8.61/8.77, and",
            "AN 8.62/8.78 —",
            "not extended further in this chapter",
        ]),
        ("One marker of change", [
            "'reverends,' not 'mendicants' —",
            "the address alone reveals",
            "a different speaker entirely",
        ]),
        ("Cross-references", [
            "AN 8.77 &middot; previous, the first of this chapter's "
            "Sāriputta/Buddha content pairs",
            "AN 8.62 &middot; earlier, the Buddha's own original teaching "
            "of this identical content",
            "AN 8.79 &middot; next, eight things that lead to a trainee's "
            "decline",
        ]),
    ],
    further=[
        '<a href="%s/an8.78/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.77.html">AN 8.77 &middot; Desires</a> &mdash; previous.',
        '<a href="an-8.62.html">AN 8.62 &middot; Good Enough</a> &mdash; earlier, the '
        "Buddha&rsquo;s own original teaching of this identical content.",
        '<a href="an-8.79.html">AN 8.79 &middot; Decline</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.79 — Parihānasutta
# --------------------------------------------------------------------------- #
page(
    79, "Parihāna", "Decline",
    vagga=VAGGA_8,
    meta_title="AN 8.79 — Decline | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Parihānasutta, a compact blocking-and-reversal pair on what "
        "leads a trainee mendicant to decline — relishing work, talk, "
        "sleep, and company — and its eight exact opposites. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight things that cause decline, then their eight exact "
                 "reversals, stated in two compact sentences"),
        ("Length", "under 1 minute to read"),
        ("A return to this book's founding shape", "This discourse "
                                                    "returns to the bare "
                                                    "blocking-list-and-"
                                                    "reversal structure "
                                                    "that opened the very "
                                                    "first discourse of "
                                                    "this book at AN 8.3, "
                                                    "now applied "
                                                    "specifically to a "
                                                    "trainee's risk of "
                                                    "decline"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief "
                       "and direct, easy to hold in mind as a single "
                       "compact pair"),
    ],
    why=(
        "AN 8.79 names eight things that lead to the decline of a "
        "mendicant trainee &mdash; relishing work, talk, sleep, and "
        "company, not guarding the sense doors, eating too much, and "
        "relishing closeness and proliferation &mdash; and their exact "
        "reversals, which don't lead to decline."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant trainee declines by relishing work, talk, sleep, "
            "and company, failing to guard the sense doors, eating too "
            "much, and relishing closeness and proliferation &mdash; and "
            "avoids decline by relishing none of these and guarding the "
            "sense doors instead."]),
        ("A trainee-specific list, not a general one", [
            "Unlike many of this book's blocking-and-reversal pairs, "
            "which apply broadly to any mendicant, this discourse names "
            "its subject explicitly as a &ldquo;trainee&rdquo; "
            "(sekha) &mdash; someone still actively progressing on the "
            "path rather than having completed it, for whom these eight "
            "risks and their reversals carry particular weight."]),
        ("Four ordinary indulgences, and four more specific risks", [
            "The first four items &mdash; work, talk, sleep, company "
            "&mdash; name broadly recognizable everyday indulgences. The "
            "remaining four are more specific to meditative training: "
            "failing to guard the sense doors, eating to excess, "
            "relishing closeness (saṅgaṇika, social entanglement), and "
            "relishing proliferation (papañca, the mind's own tendency to "
            "elaborate and complicate)."]),
        ("The book's founding shape, returned to near its close", [
            "This chapter has moved through combinatorial matrices, "
            "cumulative ladders, autobiographical accounts, and paired "
            "content taught by different speakers; this discourse's "
            "return to the simple blocking-list-and-reversal structure "
            "that opened the entire book at AN 8.3 offers a moment of "
            "structural simplicity late in this chapter."]),
    ],
    terms=[
        ("sekhassa bhikkhuno parihānāya",
         "&ldquo;the decline of a mendicant trainee&rdquo; &mdash; this "
         "discourse's own subject, naming its audience specifically as "
         "still-training mendicants rather than mendicants generally."),
        ("kammārāmatā, bhassārāmatā, niddārāmatā, saṅgaṇikārāmatā",
         "&ldquo;relish work, talk, sleep, and company&rdquo; &mdash; the "
         "first four items, broadly recognizable everyday indulgences."),
        ("indriyesu aguttadvāratā",
         "&ldquo;not guarding the sense doors&rdquo; &mdash; the fifth "
         "item, a specifically meditative failure rather than an "
         "ordinary indulgence."),
        ("bhojane amattaññutā",
         "&ldquo;eating too much&rdquo; &mdash; the sixth item, lacking "
         "moderation specifically around food."),
        ("papañcārāmatā",
         "&ldquo;relishing proliferation&rdquo; &mdash; the eighth and "
         "final item, the mind's own tendency to elaborate and complicate "
         "experience rather than meeting it directly."),
    ],
    text_intro=(
        "The discourse in full: eight things that cause a trainee's "
        "decline, and their eight reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight things that lead to a trainee's decline"),
        ("p", "&sect;1", "an8.79:1.1-1.4"),
        ("h3", "Eight things that don't lead to decline"),
        ("p", "&sect;2", "an8.79:2.1-2.4"),
    ],
    quiz=[
        {"q": "Who is the specific audience this discourse names, unlike "
              "many of this book's other blocking-list pairs?",
         "opts": [
             "Wealthy laypeople",
             "A mendicant trainee (sekha) — someone still actively "
             "progressing on the path",
             "Only fully awakened arahants",
             "Only newly ordained novices under age twenty"],
         "correct": 1,
         "expl": "A discourse specifically addressed to those still in "
                 "active training."},
        {"q": "What are the first four things that lead to a trainee's "
              "decline?",
         "opts": [
             "The five hindrances",
             "Relishing work, talk, sleep, and company",
             "Wealth, status, education, and beauty",
             "Fear, doubt, anger, and pride"],
         "correct": 1,
         "expl": "Broadly recognizable everyday indulgences, opening the "
                 "list."},
        {"q": "What does 'relishing proliferation' (papañca) refer to?",
         "opts": [
             "Excessive wealth accumulation",
             "The mind's own tendency to elaborate and complicate "
             "experience rather than meeting it directly",
             "Overeating specifically",
             "Excessive physical exercise"],
         "correct": 1,
         "expl": "A specifically meditative concern, the eighth and final "
                 "item in the list."},
        {"q": "How does this discourse's structure compare to AN 8.3, "
              "which opened this book?",
         "opts": [
             "Entirely unrelated structures",
             "It returns to the same bare blocking-list-and-reversal "
             "structure that opened the entire book",
             "This discourse has no reversal list at all",
             "AN 8.3 has a completely different structure"],
         "correct": 1,
         "expl": "A moment of structural simplicity, echoing the book's "
                 "own opening shape."},
        {"q": "How are the eight things that don't lead to decline "
              "presented?",
         "opts": [
             "As an entirely different, unrelated list",
             "As the exact reversal of the first eight items",
             "As only four items, not eight",
             "They are not presented at all"],
         "correct": 1,
         "expl": "A clean, point-for-point reversal of the decline-causing "
                 "list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Four ordinary indulgences", [
            "relishing work, talk,",
            "sleep, and company —",
            "broadly recognizable risks",
        ]),
        ("Four more specific risks", [
            "unguarded senses, overeating,",
            "relishing closeness,",
            "relishing proliferation itself",
        ]),
        ("A return to the book's own shape", [
            "the same bare blocking list",
            "and reversal that opened",
            "this entire book at AN 8.3",
        ]),
        ("Cross-references", [
            "AN 8.78 &middot; previous, Sāriputta's second matched "
            "teaching",
            "AN 8.80 &middot; next, closing this chapter with the same "
            "circumstances rationalized two opposite ways",
        ]),
    ],
    further=[
        '<a href="%s/an8.79/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.78.html">AN 8.78 &middot; Good Enough</a> &mdash; previous.',
        '<a href="an-8.80.html">AN 8.80 &middot; Grounds for Laziness and Arousing '
        "Energy</a> &mdash; next, closing this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.80 — Kusītārambhavatthusutta — closes ch.8 Yamakavagga
# --------------------------------------------------------------------------- #
page(
    80, "Kusītārambhavatthu", "Grounds for Laziness and Arousing Energy",
    vagga=VAGGA_8,
    meta_title="AN 8.80 — Grounds for Laziness and Arousing Energy | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Kusītārambhavatthusutta, closing this chapter with eight "
        "identical circumstances — work, travel, hunger, fullness, "
        "illness, recovery — rationalized once toward lying down and once "
        "toward rousing energy, the same facts read two opposite ways. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight circumstances rationalized toward laziness, then "
                 "the identical eight circumstances rationalized toward "
                 "energy, each pair sharing the same factual premise but "
                 "opposite reasoning"),
        ("Length", "~3 minutes to read"),
        ("The same eight facts, opposite interpretations", "This is a "
                                                            "psychologically "
                                                            "sharp closing "
                                                            "discourse: "
                                                            "the sixteen "
                                                            "items aren't "
                                                            "sixteen "
                                                            "different "
                                                            "circumstances "
                                                            "but eight "
                                                            "identical ones, "
                                                            "each capable "
                                                            "of justifying "
                                                            "either "
                                                            "laziness or "
                                                            "energy "
                                                            "depending "
                                                            "entirely on "
                                                            "how the "
                                                            "mendicant "
                                                            "frames it"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "closely paired structure, best read by comparing "
                       "each circumstance's two opposite rationalizations "
                       "side by side"),
    ],
    why=(
        "AN 8.80 closes this chapter by naming eight circumstances "
        "&mdash; having work to do or done, a journey ahead or completed, "
        "insufficient or plentiful almsfood, minor illness, or recent "
        "recovery &mdash; each one capable of rationalizing either "
        "laziness (&ldquo;my body will get tired, I'd better lie "
        "down&rdquo;) or energetic effort (&ldquo;I'd better rouse "
        "energy now, before it's too late&rdquo;), depending entirely on "
        "how the mendicant chooses to interpret it."),
    guide=[
        ("The teaching in one sentence", [
            "The same eight circumstances &mdash; work ahead or behind, "
            "travel ahead or behind, too little or too much almsfood, "
            "minor illness or recent recovery &mdash; can rationalize "
            "either lying down in laziness or rousing energy "
            "preemptively, and the discourse shows exactly how the "
            "identical fact pattern supports both conclusions depending "
            "purely on how it's framed."]),
        ("Eight facts, sixteen rationalizations", [
            "This discourse's real structure isn't sixteen independent "
            "items but eight circumstances, each given two opposite "
            "internal monologues: work not yet done becomes either "
            "&ldquo;my body will get tired, I'd better lie down&rdquo; or "
            "&ldquo;it's not easy to focus while working, I'd better "
            "rouse energy first&rdquo; &mdash; the same anticipated "
            "tiredness read as an excuse in one case and a warning in "
            "the other."]),
        ("Even opposite physical states rationalize the same way", [
            "The discourse's sharpest move comes with almsfood: "
            "insufficient food becomes either an excuse (&ldquo;my body "
            "is tired and unfit for work&rdquo;) or a spur (&ldquo;my "
            "body is light and fit for work&rdquo;), while abundant food "
            "becomes either an excuse (&ldquo;my body is heavy, like "
            "I've just eaten a load of beans&rdquo;) or a spur "
            "(&ldquo;my body is strong and fit for work&rdquo;) &mdash; "
            "demonstrating that even physically opposite states can each "
            "be rationalized in either direction."]),
        ("Closing this chapter on the mind's own responsibility", [
            "Rather than external circumstance determining a mendicant's "
            "diligence or laziness, this discourse's closing position "
            "places the deciding factor entirely in how the mind "
            "interprets whatever circumstance arises &mdash; a fitting "
            "close to a chapter that has repeatedly examined how "
            "reaction, framing, and interpretation, not raw fact, "
            "determine spiritual outcome."]),
    ],
    terms=[
        ("kusītavatthūni",
         "&ldquo;grounds for laziness&rdquo; &mdash; the first half of "
         "this discourse's own title-phrase and its opening eight "
         "circumstances."),
        ("ārambhavatthūni",
         "&ldquo;grounds for arousing energy&rdquo; &mdash; the second "
         "half of the title, the identical eight circumstances "
         "rationalized in the opposite direction."),
        ("kilanto bhavissāmi, handāhaṁ nipajjāmī'ti",
         "&ldquo;my body will get tired, I'd better have a lie down&rdquo; "
         "&mdash; the recurring laziness rationalization, repeated across "
         "each of the eight circumstances with only the specific "
         "situation changed."),
        ("appattassa pattiyā, anadhigatassa adhigamāya, "
         "asacchikatassa sacchikiriyāya vīriyaṁ ārabhissāmī'ti",
         "&ldquo;I'd better preemptively rouse up energy for attaining "
         "the unattained, achieving the unachieved, and realizing the "
         "unrealized&rdquo; &mdash; the recurring energy rationalization, "
         "the exact structural counterpart to the laziness formula."),
        ("bhabbo pāpiyo assā'ti",
         "&ldquo;it's possible this illness will worsen&rdquo; &mdash; "
         "part of the seventh circumstance's energetic rationalization, "
         "reading minor illness as a spur rather than an excuse."),
    ],
    text_intro=(
        "The discourse in full: eight circumstances, each rationalized "
        "once toward laziness and once toward energy, closing this "
        "chapter. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight grounds for laziness"),
        ("p", "&sect;1", "an8.80:1.1-8.6"),
        ("h3", "The same eight circumstances, grounds for arousing "
               "energy"),
        ("p", "&sect;2", "an8.80:9.1-17.1"),
    ],
    quiz=[
        {"q": "How many distinct circumstances does this discourse "
              "actually name, despite giving sixteen numbered items?",
         "opts": [
             "Sixteen entirely independent circumstances",
             "Eight — each one given two opposite rationalizations, "
             "toward laziness and toward energy",
             "Four", "Two"],
         "correct": 1,
         "expl": "The same eight facts, each read two opposite ways, not "
                 "sixteen separate situations."},
        {"q": "What happens to insufficient almsfood in this discourse's "
              "two rationalizations?",
         "opts": [
             "It only ever justifies laziness",
             "It becomes an excuse ('my body is tired') in one "
             "rationalization and a spur ('my body is light and fit for "
             "work') in the other",
             "It only ever justifies energy",
             "It isn't addressed in this discourse"],
         "correct": 1,
         "expl": "The same physical state, framed in opposite directions "
                 "depending on the mendicant's own interpretation."},
        {"q": "According to the guide, what does this discourse's closing "
              "position emphasize?",
         "opts": [
             "That external circumstance alone determines diligence or "
             "laziness",
             "That the deciding factor lies entirely in how the mind "
             "interprets whatever circumstance arises, not raw fact "
             "itself",
             "That laziness is always justified",
             "That energy should never be roused preemptively"],
         "correct": 1,
         "expl": "A fitting close to a chapter examining reaction and "
                 "interpretation over raw circumstance."},
        {"q": "What happens with abundant almsfood in this discourse's two "
              "rationalizations?",
         "opts": [
             "It only justifies laziness",
             "It becomes 'heavy, like I've just eaten a load of beans' in "
             "one version and 'strong and fit for work' in the other",
             "It is treated identically in both versions",
             "It only justifies energy"],
         "correct": 1,
         "expl": "Even the same physically full state supports opposite "
                 "conclusions depending on framing."},
        {"q": "What structural pattern repeats across all eight "
              "circumstances in the 'laziness' half?",
         "opts": [
             "A different excuse each time with no common thread",
             "'My body will get tired, I'd better have a lie down' — the "
             "identical formula applied to each specific situation",
             "A request for permission from a senior monk",
             "A recitation of the monastic code"],
         "correct": 1,
         "expl": "A consistent recurring rationalization, only the "
                 "specific circumstance changing."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Eight facts, sixteen readings", [
            "work, travel, hunger, fullness,",
            "illness, recovery — each one",
            "argued two opposite ways",
        ]),
        ("The same tiredness, both ways", [
            "'I'd better lie down' — or",
            "'I'd better rouse energy first' —",
            "the fact unchanged, the framing everything",
        ]),
        ("Closing on the mind's own choice", [
            "not circumstance, but interpretation —",
            "a fitting close to a chapter",
            "built on reaction over raw fact",
        ]),
        ("Cross-references", [
            "AN 8.79 &middot; previous, eight things that lead to a "
            "trainee's decline",
            "AN 8.61 &middot; earlier, opening this chapter with the same "
            "insight about reaction over circumstance",
        ]),
    ],
    further=[
        '<a href="%s/an8.80/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.79.html">AN 8.79 &middot; Decline</a> &mdash; previous.',
        '<a href="an-8.61.html">AN 8.61 &middot; Desire</a> &mdash; earlier, opening this '
        "chapter.",
    ],
)


VAGGA_9 = "<em>Sativagga</em> &mdash; the ninth chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.81 — Ariyavaṁsasutta -- opens ch.9 Sativagga. Root name differs from
# common English title; SC catalogs it under the mindfulness/situational-
# awareness theme, an upanisā-style supporting-condition chain like SN 12.23.
# --------------------------------------------------------------------------- #
page(
    81, "Sati", "Mindfulness and Situational Awareness",
    vagga=VAGGA_9,
    meta_title="AN 8.81 — Mindfulness and Situational Awareness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "discourse opening a new chapter with an eight-link chain of "
        "supporting conditions — from mindfulness through conscience, "
        "restraint, ethics, and immersion to knowledge and freedom — "
        "illustrated by a tree needing branches and foliage to grow to "
        "fullness. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "An eight-link upstream chain of supporting conditions, "
                 "stated first as destruction (each missing link "
                 "undermining the next) and then as fulfillment, both "
                 "illustrated by a tree simile"),
        ("Length", "~2 minutes to read"),
        ("A chain, not a checklist", "This discourse doesn't name eight "
                                     "independent qualities but eight "
                                     "links in a single dependency chain, "
                                     "each one explicitly named as the "
                                     "supporting condition for the next, "
                                     "structurally similar to the "
                                     "&ldquo;upstream conditions&rdquo; "
                                     "logic met at AN 7.65"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a "
                       "clear chain, worth tracing link by link in both "
                       "directions"),
    ],
    why=(
        "AN 8.81 opens a new chapter with an eight-link chain: without "
        "mindfulness and situational awareness, conscience and prudence "
        "are undermined; without those, sense restraint; without that, "
        "ethical conduct; without that, right immersion; without that, "
        "true knowledge and vision; without that, disillusionment and "
        "dispassion; without that, knowledge and vision of freedom itself "
        "&mdash; and the identical chain holds in reverse when each link "
        "is fulfilled instead."),
    guide=[
        ("The teaching in one sentence", [
            "Mindfulness and situational awareness support conscience and "
            "prudence, which support sense restraint, which supports "
            "ethical conduct, which supports right immersion, which "
            "supports true knowledge and vision, which supports "
            "disillusionment and dispassion, which supports knowledge and "
            "vision of freedom &mdash; a single chain that collapses from "
            "the bottom up when any link is missing, and builds from the "
            "bottom up when each link is fulfilled."]),
        ("Eight links, not eight independent qualities", [
            "Every item in this discourse is explicitly framed as a "
            "&ldquo;vital condition&rdquo; (upanisā) for the next, not as "
            "a free-standing virtue listed alongside seven others. The "
            "structure demands the chain be read in sequence, each link's "
            "presence or absence rippling forward to affect everything "
            "that depends on it."]),
        ("A tree that can't grow without branches and foliage", [
            "The discourse illustrates both directions of the chain with "
            "the same image: a tree lacking branches and foliage can't "
            "grow its shoots, bark, softwood, and heartwood to fullness, "
            "while a tree complete with branches and foliage grows fully "
            "&mdash; the visible, outer structure supporting the "
            "development of what lies within, exactly as mindfulness and "
            "situational awareness support everything built on top of "
            "them."]),
        ("A structural cousin to AN 7.65's own chain", [
            "This discourse's upstream-conditions logic &mdash; each "
            "factor explicitly enabling the next rather than simply "
            "co-occurring with it &mdash; closely resembles the chain met "
            "earlier in this project at AN 7.65, though the two chains "
            "name different links and neither one is a mere restatement "
            "of the other."]),
    ],
    terms=[
        ("upanisā",
         "&ldquo;vital condition&rdquo; &mdash; the discourse's own "
         "recurring term for how each link in the chain supports the "
         "next, the structural key to the whole teaching."),
        ("hirottappa",
         "&ldquo;conscience and prudence&rdquo; &mdash; the second link, "
         "directly dependent on mindfulness and situational awareness "
         "according to this discourse's own chain."),
        ("indriyasaṁvaro",
         "&ldquo;sense restraint&rdquo; &mdash; the third link, "
         "dependent on conscience and prudence and itself a support for "
         "ethical conduct."),
        ("sammāsamādhi",
         "&ldquo;right immersion&rdquo; &mdash; the fifth link, the "
         "point where ethical foundation gives way to meditative "
         "development in this chain."),
        ("nibbidāvirāgo, vimuttiñāṇadassanaṁ",
         "&ldquo;disillusionment and dispassion... knowledge and vision "
         "of freedom&rdquo; &mdash; the seventh and eighth links, closing "
         "the chain at complete liberation."),
    ],
    text_intro=(
        "The discourse in full: the eight-link chain, stated first as "
        "collapse and then as fulfillment. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The chain of collapse"),
        ("p", "&sect;1", "an8.81:1.1-1.11"),
        ("h3", "The chain of fulfillment"),
        ("p", "&sect;2", "an8.81:2.1-2.11"),
    ],
    quiz=[
        {"q": "How does this discourse structure its eight items, "
              "compared to a simple checklist?",
         "opts": [
             "As eight independent, free-standing virtues",
             "As a chain, each item explicitly framed as a 'vital "
             "condition' (upanisā) for the next",
             "As eight mutually exclusive alternatives",
             "As a random, unordered collection"],
         "correct": 1,
         "expl": "A sequential dependency chain, not a list of "
                 "independent qualities."},
        {"q": "What is the first link in this discourse's chain?",
         "opts": [
             "Wealth", "Mindfulness and situational awareness",
             "Physical strength", "Royal favor"],
         "correct": 1,
         "expl": "The foundation the entire rest of the chain depends on."},
        {"q": "What image illustrates both directions of the chain?",
         "opts": [
             "A river flowing to the sea",
             "A tree that can't grow shoots, bark, softwood, and "
             "heartwood without branches and foliage — or grows fully "
             "when complete with them",
             "A lamp being lit in darkness",
             "A ship crossing a flood"],
         "correct": 1,
         "expl": "The same image used for both collapse and fulfillment "
                 "of the chain."},
        {"q": "What are the final two links, closing the chain?",
         "opts": [
             "Wealth and status",
             "Disillusionment and dispassion, then knowledge and vision "
             "of freedom",
             "Physical strength and courage",
             "Fame and popularity"],
         "correct": 1,
         "expl": "The chain's culmination at complete liberation."},
        {"q": "How does this discourse's structure relate to AN 7.65?",
         "opts": [
             "No relation at all",
             "It closely resembles AN 7.65's own upstream-conditions "
             "logic, though naming different specific links",
             "It directly contradicts AN 7.65",
             "It is a word-for-word repeat of AN 7.65"],
         "correct": 1,
         "expl": "A structural cousin, not a restatement, of an earlier "
                 "chain teaching."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this book."},
    ],
    marginalia=[
        ("An eight-link chain", [
            "mindfulness, then conscience,",
            "restraint, ethics, immersion,",
            "knowledge, dispassion, freedom",
        ]),
        ("A tree without branches", [
            "can't grow shoots or heartwood —",
            "the same image, reversed,",
            "for a tree complete and thriving",
        ]),
        ("Support, not mere listing", [
            "each link a 'vital condition'",
            "for what follows it —",
            "collapse or fulfillment ripples through",
        ]),
        ("Cross-references", [
            "AN 8.80 &middot; earlier, closing the previous chapter",
            "AN 7.65 &middot; earlier, a structurally related chain of "
            "upstream conditions",
        ]),
    ],
    further=[
        '<a href="%s/an8.81/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.80.html">AN 8.80 &middot; Grounds for Laziness and Arousing '
        "Energy</a> &mdash; earlier, closing the previous chapter.",
        '<a href="an-8.82.html">AN 8.82 &middot; With Puṇṇiya</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.82 — Puṇṇiyasutta
# --------------------------------------------------------------------------- #
page(
    82, "Puṇṇiya", "With Puṇṇiya",
    vagga=VAGGA_9,
    meta_title="AN 8.82 — With Puṇṇiya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Puṇṇiyasutta, in which the Buddha answers why he sometimes feels "
        "inspired to teach and sometimes doesn't: an eight-step chain of "
        "genuine receptivity, from approaching in faith through practicing "
        "in line with what's understood. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Puṇṇiya and the Buddha"),
        ("Form", "A direct question, answered with an eight-step chain of "
                 "receptivity, each step's absence explicitly blocking "
                 "the Buddha's own inspiration to teach"),
        ("Length", "~2 minutes to read"),
        ("Teaching as a two-way responsiveness, not one-way delivery", "This "
                                                                        "discourse "
                                                                        "frames "
                                                                        "the "
                                                                        "Buddha's "
                                                                        "own "
                                                                        "inspiration "
                                                                        "to "
                                                                        "teach "
                                                                        "as "
                                                                        "genuinely "
                                                                        "responsive "
                                                                        "to "
                                                                        "the "
                                                                        "listener's "
                                                                        "own "
                                                                        "receptivity, "
                                                                        "not "
                                                                        "something "
                                                                        "automatically "
                                                                        "available "
                                                                        "regardless "
                                                                        "of "
                                                                        "the "
                                                                        "audience"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a "
                       "clear eight-step chain, worth comparing against AN "
                       "8.81's own upstream-conditions structure"),
    ],
    why=(
        "Puṇṇiya asks the Buddha directly why he sometimes feels inspired "
        "to teach and other times not, and the Buddha answers with an "
        "eight-step chain: a mendicant must have faith, approach, pay "
        "homage, ask questions, actively listen, remember what's heard, "
        "examine its meaning, and practice accordingly &mdash; and only "
        "when every step is present does the Buddha feel fully inspired "
        "to teach."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha's own inspiration to teach depends entirely on "
            "whether a mendicant completes an eight-step chain of genuine "
            "receptivity &mdash; faith, approaching, paying homage, "
            "asking questions, actively listening, remembering, examining "
            "meaning, and practicing accordingly &mdash; with any missing "
            "step leaving him uninspired to teach."]),
        ("An unusually direct, personal question", [
            "Puṇṇiya's question isn't about doctrine but about the "
            "Buddha's own psychology as a teacher: what determines "
            "whether he feels inspired to teach at all. The Buddha's "
            "answer treats this as a legitimate, answerable question "
            "rather than deflecting it, revealing something about "
            "teaching itself as a responsive act rather than an automatic "
            "delivery."]),
        ("Eight steps, each one a genuine gate", [
            "The chain moves from an inner disposition (faith) through "
            "physical action (approaching, paying homage) to active "
            "engagement (asking questions, listening) and finally to "
            "cognitive and practical follow-through (remembering, "
            "examining meaning, practicing accordingly). Each step is "
            "explicitly presented as necessary: faith without approaching "
            "isn't enough, approaching without paying homage isn't "
            "enough, and so on through all eight."]),
        ("A cousin to AN 8.81's chain, in a different register", [
            "Like AN 8.81 immediately preceding it, this discourse builds "
            "its eight items as a sequential chain rather than a flat "
            "list &mdash; but where AN 8.81 traces conditions internal to "
            "a practitioner's own development, this discourse traces the "
            "conditions of a specific relationship: what a listener must "
            "bring for a teacher to feel moved to teach."]),
    ],
    terms=[
        ("kena nu kho, bhante, hetunā kena paccayena",
         "&ldquo;what is the cause, what is the reason&rdquo; &mdash; "
         "Puṇṇiya's own opening question, asking directly about the "
         "Buddha's variable inspiration to teach."),
        ("saddho hoti, no ca upasaṅkamati",
         "&ldquo;has faith but doesn't approach&rdquo; &mdash; the first "
         "broken link in the chain, faith alone proving insufficient."),
        ("payirupāsati, no ca dhammaṁ suṇāti",
         "&ldquo;pays homage, but doesn't actively listen to the "
         "teaching&rdquo; &mdash; a later link, showing that even "
         "physical presence and respect aren't sufficient without active "
         "engagement."),
        ("atthamaññāya dhammamaññāya dhammānudhammaṁ paṭipajjati",
         "&ldquo;understood the meaning and the teaching, they practice "
         "in line with the principle of the teaching&rdquo; &mdash; the "
         "eighth and final step, completing the chain."),
        ("tathāgato dhammadesanāya cittaṁ na namati",
         "&ldquo;the Realized One doesn't feel inspired to teach&rdquo; "
         "&mdash; the discourse's own recurring verdict, repeated for "
         "each incomplete version of the chain."),
    ],
    text_intro=(
        "The discourse in full: Puṇṇiya's question and the Buddha's "
        "eight-step answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Puṇṇiya's question"),
        ("p", "&sect;1", "an8.82:1.1-1.2"),
        ("h3", "Seven incomplete chains, each insufficient"),
        ("p", "&sect;2", "an8.82:1.3-1.13"),
        ("h3", "The complete chain"),
        ("p", "&sect;3", "an8.82:2.1-2.3"),
    ],
    quiz=[
        {"q": "What question does Puṇṇiya ask the Buddha directly?",
         "opts": [
             "How to attain awakening",
             "What causes the Buddha to sometimes feel inspired to teach, "
             "and other times not",
             "How to become a monastic",
             "What the Buddha ate for breakfast"],
         "correct": 1,
         "expl": "An unusually direct, personal question about the "
                 "Buddha's own teaching psychology."},
        {"q": "What is the first step in the Buddha's eight-step answer?",
         "opts": [
             "Wealth", "Faith",
             "Physical strength", "Royal favor"],
         "correct": 1,
         "expl": "The chain's opening inner disposition, insufficient "
                 "alone without the steps that follow."},
        {"q": "What happens if a mendicant completes faith and approaching "
              "but doesn't pay homage?",
         "opts": [
             "The Buddha still feels fully inspired to teach",
             "The chain remains broken; the Buddha doesn't feel inspired "
             "to teach",
             "The Buddha teaches anyway out of obligation",
             "This case is not addressed in the discourse"],
         "correct": 1,
         "expl": "Every one of the eight steps is presented as "
                 "necessary, not merely helpful."},
        {"q": "What is the eighth and final step, completing the chain?",
         "opts": [
             "Giving generously to the Saṅgha",
             "Practicing in line with the principle of the teaching, "
             "having understood its meaning",
             "Building a monastery",
             "Reciting the monastic code"],
         "correct": 1,
         "expl": "Practical follow-through, closing the chain of genuine "
                 "receptivity."},
        {"q": "How does this discourse's structure compare to AN 8.81's?",
         "opts": [
             "Entirely unrelated structures",
             "Both build their eight items as a sequential chain, though "
             "AN 8.81 traces internal development while this discourse "
             "traces a teacher-listener relationship",
             "This discourse has no chain structure at all",
             "AN 8.81 is a flat list, unlike this discourse"],
         "correct": 1,
         "expl": "Structural cousins applying the chain logic to "
                 "different subject matter."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.81's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("An eight-step chain of receptivity", [
            "faith, approach, homage,",
            "questions, listening, memory,",
            "examining meaning, practice",
        ]),
        ("A personal question, answered directly", [
            "not deflected as inappropriate —",
            "the Buddha's own inspiration",
            "genuinely responsive, not automatic",
        ]),
        ("Every step, genuinely necessary", [
            "faith alone insufficient,",
            "homage alone insufficient —",
            "the whole chain required",
        ]),
        ("Cross-references", [
            "AN 8.81 &middot; previous, a structurally related chain of "
            "supporting conditions",
            "AN 8.83 &middot; next, the famous eightfold root-questions "
            "catechism",
        ]),
    ],
    further=[
        '<a href="%s/an8.82/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.81.html">AN 8.81 &middot; Mindfulness and Situational Awareness</a> '
        "&mdash; previous.",
        '<a href="an-8.83.html">AN 8.83 &middot; Rooted</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.83 — Mūlakasutta -- the famous eightfold root-questions catechism.
# --------------------------------------------------------------------------- #
page(
    83, "Mūlaka", "Rooted",
    vagga=VAGGA_9,
    meta_title="AN 8.83 — Rooted | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Mūlakasutta, a widely cited eightfold catechism answering eight "
        "questions any outsider might ask about the root, origin, and "
        "core of all things — desire, contact, immersion, freedom, and "
        "more. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The mendicants, deferring to the Buddha, and the "
                     "Buddha himself"),
        ("Form", "A hypothetical challenge from outsiders, an initial "
                 "deferral, then the Buddha's own eight-part catechism "
                 "answering eight distinct questions"),
        ("Length", "under 1 minute to read"),
        ("A widely cited philosophical formula", "This eightfold answer "
                                                  "to eight questions "
                                                  "about the nature of "
                                                  "&ldquo;all "
                                                  "things&rdquo; is among "
                                                  "the more frequently "
                                                  "cited compact "
                                                  "philosophical formulas "
                                                  "in this literature"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "terse and dense, eight distinct technical terms "
                       "answering eight distinct questions"),
    ],
    why=(
        "Anticipating that wanderers of other religions might ask what "
        "roots, produces, originates, and gathers all things, the Buddha "
        "supplies the mendicants with a compact eight-part answer: all "
        "things are rooted in desire, produced by attention, originated "
        "by contact, gathered by feeling, chiefed by immersion, ruled by "
        "mindfulness, overseen by wisdom, and cored by freedom."),
    guide=[
        ("The teaching in one sentence", [
            "Asked what roots, produces, originates, gathers, chiefs, "
            "rules, oversees, and cores all things, the correct answer is: "
            "desire, attention, contact, feeling, immersion, mindfulness, "
            "wisdom, and freedom, respectively &mdash; eight distinct "
            "questions, each with its own distinct technical answer."]),
        ("A hypothetical challenge, deferred first to the Buddha", [
            "Rather than answering an outsider's question immediately "
            "themselves, the mendicants' first response &mdash; when the "
            "Buddha poses the hypothetical &mdash; is to defer entirely: "
            "&ldquo;our teachings are rooted in the Buddha... may the "
            "Buddha himself please clarify.&rdquo; Only then does the "
            "Buddha supply the actual eight-part answer for the "
            "mendicants to use themselves in the future."]),
        ("Eight questions, eight distinct technical answers", [
            "Each of the eight questions targets a genuinely different "
            "aspect of how experience arises and unfolds: what's at the "
            "root (desire, chanda), what produces (attention, "
            "manasikāra), what's the origin (contact, phassa), what's the "
            "meeting place (feeling, vedanā), what's chief (immersion, "
            "samādhi), what rules (mindfulness, sati), what oversees "
            "(wisdom, paññā), and what's the core (freedom, vimutti)."]),
        ("From desire to freedom, a compressed map of the path", [
            "Read in sequence, the eight answers trace a compact "
            "trajectory: starting from desire, the very thing driving "
            "experience, and ending at freedom, its complete resolution "
            "&mdash; with attention, contact, and feeling describing how "
            "experience actually arises, and immersion, mindfulness, and "
            "wisdom describing what governs a skillful response to it."]),
    ],
    terms=[
        ("chandamūlakā sabbe dhammā",
         "&ldquo;all things are rooted in desire&rdquo; &mdash; the "
         "first and foundational answer, chanda naming the root from "
         "which everything else in the list follows."),
        ("manasikārasambhavā",
         "&ldquo;produced by application of mind&rdquo; &mdash; the "
         "second answer, attention as what actually brings things into "
         "being from their root."),
        ("phassasamudayā",
         "&ldquo;contact is their origin&rdquo; &mdash; the third "
         "answer, the point of sensory or mental contact where "
         "experience actually begins."),
        ("vedanāsamosaraṇā",
         "&ldquo;feeling is their meeting place&rdquo; &mdash; the "
         "fourth answer, where the results of contact converge."),
        ("vimuttisārā",
         "&ldquo;freedom is their core&rdquo; &mdash; the eighth and "
         "final answer, the innermost essence toward which the whole "
         "sequence points."),
    ],
    text_intro=(
        "The discourse in full: the hypothetical challenge and the "
        "Buddha's eight-part answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A hypothetical challenge, deferred to the Buddha"),
        ("p", "&sect;1", "an8.83:1.1-1.3"),
        ("h3", "The eight-part answer"),
        ("p", "&sect;2", "an8.83:2.1-2.9"),
    ],
    quiz=[
        {"q": "What do the mendicants do first when the Buddha poses the "
              "hypothetical outsider question?",
         "opts": [
             "They answer immediately themselves",
             "They defer entirely to the Buddha, asking him to clarify "
             "the meaning himself",
             "They refuse to engage with the question",
             "They ask the outsiders to leave"],
         "correct": 1,
         "expl": "A formal deferral before the Buddha supplies the actual "
                 "answer."},
        {"q": "What is all things' root, according to the Buddha's answer?",
         "opts": [
             "Ignorance", "Desire (chanda)",
             "Wealth", "Fear"],
         "correct": 1,
         "expl": "The first and foundational term in the eight-part "
                 "answer."},
        {"q": "What is named as all things' core, closing the sequence?",
         "opts": [
             "Wisdom", "Freedom (vimutti)",
             "Immersion", "Mindfulness"],
         "correct": 1,
         "expl": "The innermost essence the whole eight-part sequence "
                 "points toward."},
        {"q": "What is named as the 'meeting place' of all things?",
         "opts": [
             "Contact", "Feeling (vedanā)",
             "Attention", "Immersion"],
         "correct": 1,
         "expl": "The fourth of the eight distinct technical answers."},
        {"q": "According to the guide, what trajectory do the eight "
              "answers trace when read in sequence?",
         "opts": [
             "A random, unordered list",
             "A compressed map from desire (what drives experience) to "
             "freedom (its complete resolution)",
             "A description of physical cosmology",
             "A list of monastic requisites"],
         "correct": 1,
         "expl": "A trajectory from the root of experience to its final "
                 "resolution."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Eight questions, eight answers", [
            "rooted in desire, produced",
            "by attention, contact's origin,",
            "feeling's meeting, immersion's chief",
        ]),
        ("Deferred first, then answered", [
            "'our teachings are rooted",
            "in the Buddha' — then he himself",
            "supplies the actual formula",
        ]),
        ("A compressed map of the path", [
            "from desire, what drives it all,",
            "to freedom, its resolution —",
            "eight terms, one trajectory",
        ]),
        ("Cross-references", [
            "AN 8.82 &middot; previous, the Buddha's own eight-step "
            "receptivity chain",
            "AN 8.84 &middot; next, a very different register: a master "
            "thief's eight factors",
        ]),
    ],
    further=[
        '<a href="%s/an8.83/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.82.html">AN 8.82 &middot; With Puṇṇiya</a> &mdash; previous.',
        '<a href="an-8.84.html">AN 8.84 &middot; A Master Thief</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.84 — Corasutta -- literally a thief simile with no explicit monastic
# parallel drawn in the text itself; presented as found, noting the implied
# reading rather than asserting an unstated textual mapping.
# --------------------------------------------------------------------------- #
page(
    84, "Cora", "A Master Thief",
    vagga=VAGGA_9,
    meta_title="AN 8.84 — A Master Thief | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Corasutta, eight factors that get a master thief quickly "
        "executed and their eight opposites that let him live long — "
        "presented as a purely worldly teaching, with no explicit "
        "monastic parallel drawn in the text itself. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare blocking-and-reversal pair, unusually literal in "
                 "subject matter, with no allegorical mapping stated in "
                 "the text"),
        ("Length", "under 1 minute to read"),
        ("No stated spiritual parallel", "Unlike most simile-based "
                                         "discourses in this book, which "
                                         "explicitly map their image back "
                                         "onto monastic life (as at AN "
                                         "8.13's thoroughbred or AN 8.34's "
                                         "field), this discourse never "
                                         "draws such a connection itself "
                                         "— it reads, on its own terms, "
                                         "purely as worldly criminal "
                                         "advice"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief "
                       "and blunt; this reading guide presents its "
                       "content plainly rather than supplying an "
                       "interpretation the text doesn't state"),
    ],
    why=(
        "AN 8.84 names eight factors &mdash; unprovoked attacks, "
        "indiscriminate theft, killing women, raping girls, robbing "
        "monks, robbing the royal treasury, working close to home, and "
        "poor concealment &mdash; that get a master thief quickly "
        "executed, and their eight opposites, which let him live a long "
        "life, without ever stating an explicit parallel to monastic "
        "conduct."),
    guide=[
        ("The teaching in one sentence", [
            "A master thief who attacks unprovoked, steals "
            "indiscriminately, kills women, rapes girls, robs monks and "
            "the royal treasury, works close to home, and hides his loot "
            "poorly is soon executed; the same thief avoiding all eight "
            "behaviors lives a long life &mdash; stated here as literal "
            "criminal advice, with no allegorical reading supplied by the "
            "text itself."]),
        ("A blunt, unusually literal discourse", [
            "Where most of this book's blocking-and-reversal pairs "
            "concern virtues and vices directly relevant to spiritual "
            "practice, this discourse reads as exactly what it says: "
            "practical, cynical observations about which criminal "
            "behaviors invite swift capital punishment and which allow a "
            "thief to survive."]),
        ("No stated parallel, unlike this book's other similes", [
            "This is worth noting explicitly: discourses like AN 8.13's "
            "thoroughbred or AN 8.34's field always draw their comparison "
            "back to monastic life within the text itself, saying "
            "outright &ldquo;in the same way, a mendicant...&rdquo; This "
            "discourse never does. Whatever cautionary reading a listener "
            "might draw about restraint, discretion, or consequence is "
            "left for them to construct, not handed to them by the "
            "source."]),
        ("Content presented plainly, not smoothed into allegory", [
            "Rather than supplying an unstated spiritual interpretation "
            "on the text's behalf, this reading guide presents the "
            "discourse's content as it actually stands &mdash; a "
            "candid, unflinching piece of worldly observation, including "
            "its disturbing specifics about violence against women, "
            "without either softening it or inventing a monastic moral "
            "the source doesn't supply."]),
    ],
    terms=[
        ("coro mahānubhāvo",
         "&ldquo;a master thief&rdquo; &mdash; this discourse's own "
         "title-figure, and its literal, unallegorized subject."),
        ("asāhasaṁ karoti",
         "&ldquo;attacks unprovoked&rdquo; &mdash; the first factor, "
         "gratuitous violence beyond what theft itself requires."),
        ("sabbaharaṁ harati",
         "&ldquo;steals everything without exception&rdquo; &mdash; the "
         "second factor, indiscriminate rather than selective theft."),
        ("chatte lambati",
         "part of the description of &ldquo;working close to home,&rdquo; "
         "one of the eight factors, exposing the thief to easy "
         "recognition."),
        ("nikhipituṁ na kusalo hoti",
         "&ldquo;not skilled at hiding his booty&rdquo; &mdash; the "
         "eighth factor, the discourse's own closing point about poor "
         "concealment leading to swift capture."),
    ],
    text_intro=(
        "The discourse in full: eight factors leading to a thief's swift "
        "execution, and their eight opposites. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight factors leading to swift execution"),
        ("p", "&sect;1", "an8.84:1.1-1.4"),
        ("h3", "Eight factors that let him live long"),
        ("p", "&sect;2", "an8.84:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does this discourse name as leading to a master "
              "thief's quick execution?",
         "opts": [
             "Poverty alone",
             "Unprovoked attacks, indiscriminate theft, killing women, "
             "raping girls, robbing monks and the treasury, working close "
             "to home, and poor concealment",
             "Only theft from the wealthy",
             "Refusing to work with accomplices"],
         "correct": 1,
         "expl": "Eight specific factors, stated bluntly and literally."},
        {"q": "According to the guide, what makes this discourse "
              "unusual compared to most of this book's other similes?",
         "opts": [
             "It is identical in structure to every other simile",
             "It never draws an explicit parallel back to monastic life "
             "within the text itself, unlike AN 8.13 or AN 8.34",
             "It has no reversal list at all",
             "It is set at a specific, named location"],
         "correct": 1,
         "expl": "An unusually literal discourse, with no stated "
                 "allegorical mapping."},
        {"q": "How does this reading guide handle the discourse's content?",
         "opts": [
             "By inventing a monastic moral the text doesn't state",
             "By presenting the content plainly as it stands, without "
             "supplying an unstated interpretation",
             "By omitting the disturbing specifics entirely",
             "By declaring the discourse irrelevant to this collection"],
         "correct": 1,
         "expl": "Candid presentation, neither softened nor allegorized "
                 "beyond what the text itself supports."},
        {"q": "What is the eighth factor named?",
         "opts": [
             "Working far from home",
             "Not being skilled at hiding his booty",
             "Refusing to steal from monks",
             "Being too cautious"],
         "correct": 1,
         "expl": "The discourse's own closing point about poor "
                 "concealment."},
        {"q": "What contrast does the guide draw with AN 8.13 and AN "
              "8.34?",
         "opts": [
             "No contrast is drawn",
             "Both of those discourses explicitly say 'in the same way, a "
             "mendicant...' — this discourse never makes that move",
             "AN 8.13 and AN 8.34 also lack any stated parallel",
             "This discourse explicitly states a monastic parallel too"],
         "correct": 1,
         "expl": "A genuine structural difference from this book's more "
                 "typical simile discourses."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Eight factors, swift execution", [
            "unprovoked attack, indiscriminate theft,",
            "violence against women,",
            "robbing monks, poor concealment",
        ]),
        ("No stated parallel", [
            "unlike AN 8.13, AN 8.34 —",
            "no 'in the same way, a mendicant' —",
            "read purely on its own terms",
        ]),
        ("Presented plainly, not softened", [
            "the disturbing specifics kept,",
            "no invented monastic moral,",
            "no allegory supplied unasked",
        ]),
        ("Cross-references", [
            "AN 8.83 &middot; previous, the eightfold root-questions "
            "catechism",
            "AN 8.85 &middot; next, eight terms for the Realized One",
        ]),
    ],
    further=[
        '<a href="%s/an8.84/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.83.html">AN 8.83 &middot; Rooted</a> &mdash; previous.',
        '<a href="an-8.85.html">AN 8.85 &middot; Terms for the Realized One</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.85 — Samaṇasutta
# --------------------------------------------------------------------------- #
page(
    85, "Samaṇa", "Terms for the Realized One",
    vagga=VAGGA_9,
    meta_title="AN 8.85 — Terms for the Realized One | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Samaṇasutta, eight titles for the Buddha — ascetic, brahmin, "
        "knowledge master, healer, unstained, immaculate, knower, freed — "
        "closing with a defiant victory verse. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight titles applied to the Buddha, then verses "
                 "restating them and closing with a first-person "
                 "declaration of victory"),
        ("Length", "under 1 minute to read"),
        ("Titles reclaimed, not merely listed", "Several of these eight "
                                                "terms — ascetic, "
                                                "brahmin — were contested "
                                                "titles other religious "
                                                "movements also claimed "
                                                "for themselves, echoing "
                                                "the reinterpretation "
                                                "pattern already met at AN "
                                                "8.11's eight epithets"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, closing this chapter's philosophical run "
                       "with a burst of declarative confidence"),
    ],
    why=(
        "AN 8.85 names eight terms for the Realized One &mdash; ascetic, "
        "brahmin, knowledge master, healer, unstained, immaculate, "
        "knower, and freed &mdash; then closes with verses declaring, in "
        "the Buddha's own first-person voice, victory in battle and "
        "complete quenching."),
    guide=[
        ("The teaching in one sentence", [
            "Eight terms &mdash; ascetic, brahmin, knowledge master, "
            "healer, unstained, immaculate, knower, and freed &mdash; all "
            "apply to the Realized One, each naming a different facet of "
            "the same complete attainment, closing with a defiant "
            "first-person verse of victory."]),
        ("Titles other traditions also claimed", [
            "Several of these eight terms, especially &ldquo;ascetic&rdquo; "
            "(samaṇa) and &ldquo;brahmin&rdquo; (brāhmaṇa), were live, "
            "contested titles other religious movements of the time also "
            "claimed for their own teachers &mdash; this discourse "
            "applies them to the Buddha not as unique inventions but as "
            "titles genuinely earned and reclaimed, echoing the "
            "reinterpretation pattern already met at AN 8.11's eight "
            "epithets."]),
        ("Eight facets of one complete attainment", [
            "Rather than eight separate achievements, the eight titles "
            "function as eight lenses on a single state: healer "
            "(bhisakka) emphasizes practical remedy, unstained and "
            "immaculate emphasize purity, knower and knowledge master "
            "emphasize direct understanding, and freed names the "
            "underlying liberation all the other titles point toward."]),
        ("A verse of unabashed victory", [
            "The closing verses shift register entirely, from measured "
            "listing to first-person declaration: &ldquo;I am victorious "
            "in battle... I am a dragon completely tamed, an adept, I am "
            "quenched&rdquo; &mdash; a rare moment in this book where the "
            "Buddha's own voice claims triumph directly and without "
            "qualification."]),
    ],
    terms=[
        ("samaṇo",
         "&ldquo;ascetic&rdquo; &mdash; the first term, a title also "
         "claimed by rival religious movements of the time, applied here "
         "to the Buddha as genuinely earned."),
        ("brāhmaṇo",
         "&ldquo;brahmin&rdquo; &mdash; the second term, likewise a "
         "contested title, reclaimed here around spiritual attainment "
         "rather than birth."),
        ("vedagū",
         "&ldquo;knowledge master&rdquo; &mdash; one of the eight terms, "
         "naming direct mastery of understanding."),
        ("bhisakko",
         "&ldquo;healer&rdquo; &mdash; a term emphasizing practical "
         "remedy, distinct in flavor from the more purity- or knowledge-"
         "focused terms surrounding it."),
        ("sammadaññā vimutto",
         "&ldquo;freed&rdquo; &mdash; the eighth and final term, naming "
         "the underlying liberation the other seven titles each point "
         "toward from a different angle."),
    ],
    text_intro=(
        "The discourse in full: eight terms for the Realized One, and a "
        "closing verse of victory. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight terms for the Realized One"),
        ("p", "&sect;1", "an8.85:1.1-1.8"),
        ("h3", "Closing verses"),
        ("p", "&sect;2", "an8.85:2.1-4.4"),
    ],
    quiz=[
        {"q": "What are the eight terms this discourse applies to the "
              "Realized One?",
         "opts": [
             "The five hindrances plus three more",
             "Ascetic, brahmin, knowledge master, healer, unstained, "
             "immaculate, knower, and freed",
             "The seven factors of awakening plus one",
             "Eight monastic titles"],
         "correct": 1,
         "expl": "Eight facets of a single complete attainment."},
        {"q": "According to the guide, why are 'ascetic' and 'brahmin' "
              "particularly notable among the eight terms?",
         "opts": [
             "They are the least important terms",
             "They were contested titles other religious movements of the "
             "time also claimed for their own teachers",
             "They apply only to laypeople",
             "They have no parallel elsewhere in this book"],
         "correct": 1,
         "expl": "Titles reclaimed rather than uniquely invented, echoing "
                 "AN 8.11's own reinterpretation pattern."},
        {"q": "What does the guide say about how the eight titles relate "
              "to each other?",
         "opts": [
             "They name eight completely separate achievements",
             "They function as eight lenses on a single complete "
             "attainment, each emphasizing a different facet",
             "Only one of the eight is actually accurate",
             "They contradict each other"],
         "correct": 1,
         "expl": "Different angles on one underlying state, not eight "
                 "independent accomplishments."},
        {"q": "How do the closing verses shift in register?",
         "opts": [
             "They continue the same measured listing",
             "They shift to first-person declaration of victory — 'I am "
             "victorious in battle... I am quenched'",
             "They become a question rather than a statement",
             "They shift to addressing a specific individual by name"],
         "correct": 1,
         "expl": "A rare moment of direct, unqualified triumph in the "
                 "Buddha's own voice."},
        {"q": "What does 'healer' (bhisakko) emphasize, distinct from the "
              "purity-focused terms around it?",
         "opts": [
             "Physical strength",
             "Practical remedy",
             "Wealth", "Royal status"],
         "correct": 1,
         "expl": "A different flavor of attainment than the purity- or "
                 "knowledge-focused terms nearby."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("Eight titles, one attainment", [
            "ascetic, brahmin, knower,",
            "healer, unstained, immaculate,",
            "knowledge master, freed",
        ]),
        ("Contested titles, reclaimed", [
            "not unique inventions —",
            "rival movements claimed these too —",
            "earned here, not merely asserted",
        ]),
        ("A verse of unabashed victory", [
            "'I am victorious in battle' —",
            "a rare moment of direct",
            "first-person triumph, unqualified",
        ]),
        ("Cross-references", [
            "AN 8.84 &middot; previous, a master thief's eight factors",
            "AN 8.11 &middot; earlier, the same reinterpretation pattern "
            "applied to eight hostile epithets",
        ]),
    ],
    further=[
        '<a href="%s/an8.85/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.84.html">AN 8.84 &middot; A Master Thief</a> &mdash; previous.',
        '<a href="an-8.11.html">AN 8.11 &middot; At Verañjā</a> &mdash; earlier, the same '
        "reinterpretation pattern applied to eight hostile epithets.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.86 — Nāgitasutta -- a vivid, highly personal narrative; not
# organized around an eightfold list at all, unusual for this book.
# --------------------------------------------------------------------------- #
page(
    86, "Nāgita", "With Nāgita",
    vagga=VAGGA_9,
    meta_title="AN 8.86 — With Nāgita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Nāgitasutta, a vivid, unusually personal narrative in which the "
        "Buddha refuses a noisy crowd's offering, declares he never wants "
        "fame, and gives his attendant Nāgita a candid, sometimes "
        "surprising account of what pleases and displeases him about "
        "mendicant conduct. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "A forest near Icchānaṅgala, a village of Kosalan "
                    "brahmins"),
        ("Speakers", "The Buddha and Venerable Nāgita, his attendant"),
        ("Form", "A narrative opening with a noisy crowd, then an extended "
                 "personal account by the Buddha of what he approves and "
                 "disapproves of, closing with an unexpectedly mundane "
                 "personal detail"),
        ("Length", "~4 minutes to read"),
        ("Not organized around an eightfold list at all", "Unlike almost "
                                                           "every other "
                                                           "discourse in "
                                                           "this book, "
                                                           "this one names "
                                                           "no explicit "
                                                           "count of eight "
                                                           "— it belongs "
                                                           "here by "
                                                           "placement, its "
                                                           "real content a "
                                                           "free-flowing, "
                                                           "highly "
                                                           "personal "
                                                           "account"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "narratively rich and unusually candid, worth "
                       "reading for its portrait of the Buddha's own "
                       "temperament as much as its explicit content"),
    ],
    why=(
        "When a crowd of brahmins and householders arrives making a "
        "&ldquo;colossal racket&rdquo; wanting to honor him specially, "
        "the Buddha tells his attendant Nāgita that he never wants fame, "
        "preferring the pleasure of seclusion any ordinary person can't "
        "access &mdash; and goes on to give a candid, sometimes "
        "surprising account of exactly what pleases and displeases him "
        "about how mendicants actually live."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha declares he never wants fame, since the "
            "&ldquo;filthy, lazy pleasure&rdquo; of possessions, honor, "
            "and popularity can't compare to the pleasure of renunciation "
            "and seclusion he can access at will, then tells Nāgita in "
            "detail what specifically pleases and displeases him about "
            "how mendicants conduct themselves, in the village and in the "
            "wilderness alike."]),
        ("A noisy crowd, and a blunt refusal of fame", [
            "The discourse opens with genuine comic energy: a crowd makes "
            "such a racket outside the gate that the Buddha compares it "
            "to fishermen hauling in a catch, and when told they've come "
            "bearing food specifically to honor him, his response isn't "
            "gratitude but a flat declaration that he never wants fame at "
            "all &mdash; repeated even after Nāgita's own respectful "
            "objection that the Buddha's influence naturally draws people "
            "&ldquo;like water flowing downhill.&rdquo;"]),
        ("Surprisingly candid judgments about mendicant behavior", [
            "The Buddha's account of what displeases him is unusually "
            "specific and personal: mendicants poking each other and "
            "giggling together, or eating until full and then indulging "
            "in sleep, both genuinely disappoint him. His preference "
            "between village and wilderness dwelling isn't absolute "
            "either &mdash; he's displeased by a village mendicant sitting "
            "immersed in samādhi (fearing they'll be disturbed) but "
            "pleased by a wilderness mendicant even when nodding off in "
            "meditation, reasoning that at least they'll wake to an "
            "environment supporting further practice."]),
        ("A closing detail almost startling in its ordinariness", [
            "The discourse ends not with a grand doctrinal statement but "
            "with the Buddha admitting, with disarming candor, that "
            "walking a road alone &mdash; seeing no one ahead or behind "
            "&mdash; feels relaxing to him, even for something as mundane "
            "as needing to urinate or defecate. This closing detail, "
            "unusual in this book's typical register, humanizes the "
            "entire discourse's underlying preference for solitude over "
            "crowds."]),
    ],
    terms=[
        ("mā maṁ yaso āgamā, mā ca yasaṁ āgamiṁ",
         "&ldquo;may I never become famous. May fame not come to "
         "me&rdquo; &mdash; the Buddha's own blunt, repeated declaration, "
         "the discourse's central refrain."),
        ("kilesikaṁ kasiraṁ lābhasakkārasilokasukhaṁ",
         "&ldquo;the filthy, lazy pleasure of possessions, honor, and "
         "popularity&rdquo; &mdash; the Buddha's own dismissive "
         "description of what fame actually offers, contrasted with "
         "renunciation's pleasure."),
        ("aṅgulipatodakena aññamaññaṁ",
         "&ldquo;poking each other with their fingers, giggling and "
         "playing together&rdquo; &mdash; one of the specific behaviors "
         "the Buddha names as displeasing him, a candid, almost "
         "parental-sounding complaint."),
        ("araññe pana bhikkhuṁ passāmi pacalāyamānaṁ nisinnaṁ",
         "&ldquo;a mendicant in the wilderness who I see sitting nodding "
         "in meditation&rdquo; &mdash; a case the Buddha says pleases "
         "him despite the apparent lapse, reasoning that the wilderness "
         "itself supports recovery."),
        ("appossukko sukhaṁ vighāsaṁ karomi",
         "part of the discourse's closing admission about the ordinary "
         "relief of walking a road with no one ahead or behind, even for "
         "mundane bodily needs."),
    ],
    text_intro=(
        "The discourse in full: a noisy crowd, the Buddha's refusal of "
        "fame, and his candid account of what pleases and displeases him "
        "about mendicant conduct. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A noisy crowd, and the Buddha's refusal of fame"),
        ("p", "&sect;1", "an8.86:1.1-4.3"),
        ("h3", "What displeases him: company, giggling, overeating"),
        ("p", "&sect;2", "an8.86:5.1-7.4"),
        ("h3", "Village and wilderness, judged case by case"),
        ("p", "&sect;3", "an8.86:8.1-13.3"),
        ("h3", "A closing, unexpectedly ordinary detail"),
        ("p", "&sect;4", "an8.86:14.1-14.1"),
    ],
    quiz=[
        {"q": "How does the Buddha respond when told a crowd has come "
              "bearing food specifically to honor him?",
         "opts": [
             "With gratitude and immediate acceptance",
             "With a flat declaration that he never wants fame at all",
             "By asking Nāgita to accept it on his behalf",
             "By ignoring the crowd entirely"],
         "correct": 1,
         "expl": "A blunt refusal, repeated even after Nāgita's own "
                 "respectful objection."},
        {"q": "What specific mendicant behaviors does the Buddha say "
              "displease him?",
         "opts": [
             "Meditating too much",
             "Poking each other and giggling together, and eating until "
             "full then indulging in sleep",
             "Traveling too far from the monastery",
             "Speaking too formally"],
         "correct": 1,
         "expl": "Candid, almost parental-sounding complaints about "
                 "specific observed conduct."},
        {"q": "How does the Buddha judge a village mendicant sitting "
              "immersed in samādhi, versus a wilderness mendicant nodding "
              "off in meditation?",
         "opts": [
             "He approves of both equally",
             "He's displeased by the village case (fearing disturbance) "
             "but pleased by the wilderness case (trusting the "
             "environment supports recovery)",
             "He disapproves of both equally",
             "He never comments on either case"],
         "correct": 1,
         "expl": "A nuanced, situation-specific judgment rather than a "
                 "simple rule."},
        {"q": "What does the discourse's closing detail reveal?",
         "opts": [
             "A grand doctrinal statement",
             "The Buddha's candid admission that walking alone feels "
             "relaxing to him, even for mundane bodily needs",
             "A prediction about the future of the Saṅgha",
             "A warning about a specific mendicant"],
         "correct": 1,
         "expl": "An unusually ordinary, humanizing detail closing the "
                 "discourse."},
        {"q": "According to the guide, how is this discourse structured, "
              "unlike almost every other discourse in this book?",
         "opts": [
             "Around a clean eightfold list",
             "With no explicit count of eight at all — a free-flowing, "
             "highly personal narrative belonging here by placement",
             "As a bare blocking-and-reversal pair",
             "As a formal legal procedure"],
         "correct": 1,
         "expl": "An outlier in structure, its content unusually personal "
                 "and narrative."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "A forest near Icchānaṅgala, a village of Kosalan brahmins",
             "Rājagaha, on Vulture's Peak",
             "Vesālī, at the Great Wood"],
         "correct": 1,
         "expl": "A specific named location, distinct from this book's "
                 "more common settings."},
    ],
    marginalia=[
        ("A racket like fishermen hauling a catch", [
            "a crowd comes bearing food —",
            "the Buddha's answer: 'may I",
            "never become famous'",
        ]),
        ("Candid, almost parental judgments", [
            "displeased by giggling, poking —",
            "displeased by eating full",
            "then indulging in sleep",
        ]),
        ("Nuanced, not absolute", [
            "village samādhi worries him —",
            "wilderness drowsiness doesn't —",
            "judged case by case, not by rule",
        ]),
        ("Cross-references", [
            "AN 8.85 &middot; earlier, eight terms for the Realized One",
            "AN 8.87 &middot; next, formal Saṅgha procedures toward "
            "difficult lay supporters",
        ]),
    ],
    further=[
        '<a href="%s/an8.86/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.85.html">AN 8.85 &middot; Terms for the Realized One</a> &mdash; '
        "previous.",
        '<a href="an-8.87.html">AN 8.87 &middot; Turning the Bowl Upside Down</a> &mdash; '
        "next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.87 — Pattanikkujjanasutta -- first of four Vinaya-procedural
# discourses closing this chapter.
# --------------------------------------------------------------------------- #
page(
    87, "Pattanikkujjana", "Turning the Bowl Upside Down",
    vagga=VAGGA_9,
    meta_title="AN 8.87 — Turning the Bowl Upside Down | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Pattanikkujjanasutta, the formal grounds on which the Saṅgha may "
        "collectively boycott a hostile lay supporter — and the grounds "
        "for reversing that boycott. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A formal procedural statement: eight grounds for the "
                 "Saṅgha's collective boycott, then their eight reversals"),
        ("Length", "under 1 minute to read"),
        ("The first of four Vinaya-adjacent discourses", "This discourse "
                                                          "opens a "
                                                          "distinct "
                                                          "closing run in "
                                                          "this chapter: "
                                                          "four "
                                                          "discourses "
                                                          "(AN 8.87–90) "
                                                          "concerned with "
                                                          "formal "
                                                          "institutional "
                                                          "procedures "
                                                          "governing "
                                                          "Saṅgha-lay "
                                                          "relations and "
                                                          "monastic "
                                                          "discipline"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "formal and procedural in register, a shift from "
                       "this chapter's earlier narrative and "
                       "philosophical material"),
    ],
    why=(
        "AN 8.87 names eight grounds on which the Saṅgha may, if it "
        "wishes, collectively refuse a lay follower's offerings &mdash; "
        "obstructing mendicants' material support, harming them, driving "
        "them from a monastery, insulting them, dividing them against "
        "each other, or criticizing the Buddha, teaching, or Saṅgha "
        "&mdash; and their eight reversals, restoring the relationship."),
    guide=[
        ("The teaching in one sentence", [
            "The Saṅgha may collectively boycott a lay follower &mdash; "
            "&ldquo;turning the bowl upside down&rdquo; to refuse their "
            "offerings &mdash; on eight grounds of active hostility "
            "toward mendicants, and may reverse that boycott once the lay "
            "follower stops behaving in these eight ways."]),
        ("A vivid image for a formal act", [
            "&ldquo;Turning the bowl upside down&rdquo; names a concrete, "
            "visible gesture: an alms bowl normally held open to receive "
            "food is instead inverted, signaling refusal. The Saṅgha's "
            "formal collective response to hostile lay conduct is "
            "expressed through this same physical, unmistakable act "
            "rather than an abstract declaration."]),
        ("Eight grounds, all concerning active hostility", [
            "Every one of the eight grounds describes deliberate hostile "
            "action toward the mendicant community: obstructing material "
            "support, causing harm, driving mendicants away, insulting "
            "them, sowing division among them, or criticizing the three "
            "refuges directly &mdash; not disagreement or criticism in "
            "general, but active, targeted hostility."]),
        ("A reversible, not permanent, procedure", [
            "The discourse's second half matters as much as its first: "
            "the boycott is explicitly reversible, restored once the lay "
            "follower's conduct changes &mdash; framing this formal act "
            "as a corrective response to specific behavior, not a "
            "permanent severing of relationship."]),
    ],
    terms=[
        ("pattaṁ nikkujjeyya",
         "&ldquo;turn the bowl upside down&rdquo; &mdash; this "
         "discourse's own title-phrase and central image, a visible "
         "gesture of collective refusal."),
        ("lābhaṁ pariyesati",
         "&ldquo;material things&rdquo; &mdash; what the first ground "
         "concerns, a lay follower obstructing mendicants' basic "
         "material support."),
        ("anatthaṁ pariyesati",
         "&ldquo;tries to harm&rdquo; &mdash; the second ground, direct "
         "hostility beyond merely withholding support."),
        ("saṅghabhedāya parakkamati",
         "&ldquo;divides mendicants against each other&rdquo; &mdash; "
         "one of the eight grounds, targeting the Saṅgha's own internal "
         "unity rather than any individual mendicant."),
        ("pattaṁ ukkujjeyya",
         "&ldquo;turn the bowl upright&rdquo; &mdash; the discourse's own "
         "term for reversing the boycott, restoring the relationship once "
         "the eight grounds no longer apply."),
    ],
    text_intro=(
        "The discourse in full: eight grounds for the Saṅgha's boycott, "
        "and eight grounds for reversing it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight grounds for turning the bowl upside down"),
        ("p", "&sect;1", "an8.87:1.1-1.4"),
        ("h3", "Eight grounds for turning it upright again"),
        ("p", "&sect;2", "an8.87:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does 'turning the bowl upside down' refer to?",
         "opts": [
             "A meditation posture",
             "A visible, concrete gesture of the Saṅgha's collective "
             "refusal of a lay follower's offerings",
             "A monastic building repair",
             "A method of alms distribution"],
         "correct": 1,
         "expl": "A formal boycott expressed through a physical, "
                 "unmistakable act."},
        {"q": "What kind of conduct do the eight grounds for this boycott "
              "concern?",
         "opts": [
             "Simple disagreement or criticism in general",
             "Active, targeted hostility — obstructing support, causing "
             "harm, driving mendicants away, insulting them, dividing "
             "them, or criticizing the three refuges",
             "Failure to attend religious festivals",
             "Minor social awkwardness"],
         "correct": 1,
         "expl": "Deliberate hostile action, not mere disagreement."},
        {"q": "Is the boycott described as permanent?",
         "opts": [
             "Yes, once imposed it can never be reversed",
             "No — it is explicitly reversible once the lay follower's "
             "conduct changes",
             "The discourse doesn't address reversal",
             "It automatically expires after a fixed time"],
         "correct": 1,
         "expl": "A corrective response to specific behavior, not a "
                 "permanent severing."},
        {"q": "How does the guide characterize this discourse's place in "
              "the chapter?",
         "opts": [
             "A continuation of the narrative register of AN 8.86",
             "The first of four Vinaya-adjacent discourses closing this "
             "chapter with formal institutional procedures",
             "A return to philosophical material",
             "Unrelated to the rest of the chapter"],
         "correct": 1,
         "expl": "A shift in register, opening a distinct closing run of "
                 "procedural discourses."},
        {"q": "What is one of the eight grounds for the boycott?",
         "opts": [
             "Disagreeing publicly with a monastic teaching",
             "Trying to divide mendicants against each other",
             "Being too generous with offerings",
             "Asking too many questions"],
         "correct": 1,
         "expl": "One of six named grounds, all concerning active "
                 "hostility toward the mendicant community."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching several other discourses in "
                 "this chapter."},
    ],
    marginalia=[
        ("A visible gesture of refusal", [
            "the alms bowl, inverted —",
            "a concrete, physical signal,",
            "not an abstract declaration",
        ]),
        ("Active hostility, not disagreement", [
            "obstructing support, causing harm,",
            "driving mendicants away,",
            "dividing them, insulting the refuges",
        ]),
        ("Reversible, not permanent", [
            "the bowl turned upright again",
            "once conduct changes —",
            "a corrective response, not a severing",
        ]),
        ("Cross-references", [
            "AN 8.86 &middot; previous, the Buddha's candid account of "
            "what pleases and displeases him",
            "AN 8.88 &middot; next, the mirror procedure from the "
            "laypeople's own side",
        ]),
    ],
    further=[
        '<a href="%s/an8.87/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.86.html">AN 8.86 &middot; With Nāgita</a> &mdash; previous.',
        '<a href="an-8.88.html">AN 8.88 &middot; A Proclamation of No Confidence</a> '
        "&mdash; next.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.88 — Appasādasutta
# --------------------------------------------------------------------------- #
page(
    88, "Appasāda", "A Proclamation of No Confidence",
    vagga=VAGGA_9,
    meta_title="AN 8.88 — A Proclamation of No Confidence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Appasādasutta, the mirror procedure to AN 8.87 from the "
        "laypeople's own side: the grounds on which they may formally "
        "declare no confidence in a hostile mendicant, and its reversal. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight grounds for a formal lay proclamation of no "
                 "confidence in a mendicant, then eight grounds for its "
                 "reversal"),
        ("Length", "under 1 minute to read"),
        ("The mirror of AN 8.87, from the other direction", "Where AN "
                                                             "8.87 gave "
                                                             "the "
                                                             "Saṅgha's "
                                                             "own formal "
                                                             "power to "
                                                             "boycott a "
                                                             "hostile "
                                                             "layperson, "
                                                             "this "
                                                             "discourse "
                                                             "gives "
                                                             "laypeople "
                                                             "the "
                                                             "parallel "
                                                             "power to "
                                                             "formally "
                                                             "declare no "
                                                             "confidence "
                                                             "in a "
                                                             "hostile "
                                                             "mendicant"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "formal and procedural, best read directly "
                       "alongside AN 8.87 for the reciprocal structure"),
    ],
    why=(
        "AN 8.88 names eight grounds on which laypeople may formally "
        "declare no confidence in a mendicant &mdash; obstructing their "
        "material support, harming them, insulting them, dividing them "
        "against each other, criticizing the Buddha, teaching, or "
        "Saṅgha, or begging in inappropriate places &mdash; and their "
        "eight reversals, restoring lay confidence."),
    guide=[
        ("The teaching in one sentence", [
            "Laypeople may formally proclaim no confidence in a "
            "mendicant who obstructs their material support, harms or "
            "insults them, divides them against each other, criticizes "
            "the three refuges, or begs in an inappropriate place "
            "&mdash; and may restore confidence once the mendicant stops "
            "behaving in these eight ways."]),
        ("A power granted to laypeople, mirroring AN 8.87", [
            "This discourse and AN 8.87, immediately preceding it, form a "
            "deliberate reciprocal pair: the Saṅgha can formally withdraw "
            "from a hostile layperson, and laypeople can formally "
            "withdraw their confidence from a hostile mendicant &mdash; "
            "neither side holds unilateral, unchecked authority over the "
            "relationship."]),
        ("Overlapping grounds, one genuinely new item", [
            "Six of the eight grounds closely parallel AN 8.87's own "
            "list &mdash; obstructing material support, causing harm, "
            "insulting, dividing, and criticizing the three refuges "
            "&mdash; but this discourse adds one item with no equivalent "
            "in AN 8.87: being seen begging for alms at an inappropriate "
            "place, a specifically monastic-conduct concern that wouldn't "
            "apply to a layperson."]),
        ("Confidence as something earned continuously, not assumed", [
            "By naming specific, concrete grounds for withdrawing and "
            "restoring confidence, this discourse frames a mendicant's "
            "standing with the lay community as something maintained "
            "through ongoing conduct, not a status granted once at "
            "ordination and held automatically thereafter."]),
    ],
    terms=[
        ("appasādaṁ pakāseyyuṁ",
         "&ldquo;make a proclamation of no confidence&rdquo; &mdash; "
         "this discourse's own title-phrase, the formal lay declaration "
         "concerning a mendicant."),
        ("agocare āpādesi",
         "&ldquo;seen at an inappropriate place for collecting "
         "alms&rdquo; &mdash; the item unique to this discourse's list, "
         "with no equivalent in AN 8.87's grounds for the Saṅgha's own "
         "boycott."),
        ("saṅghabhedāya parakkamati",
         "&ldquo;divides laypeople against each other&rdquo; &mdash; "
         "one of the shared grounds, here concerning division within the "
         "lay community rather than within the Saṅgha."),
        ("pasādaṁ pakāseyyuṁ",
         "&ldquo;make a proclamation of confidence&rdquo; &mdash; the "
         "discourse's own term for restoring standing, once the eight "
         "grounds no longer apply."),
        ("upāsakā",
         "&ldquo;lay followers&rdquo; &mdash; the discourse's own "
         "subject, holding a formal, named power over a mendicant's "
         "standing, mirroring the Saṅgha's own power at AN 8.87."),
    ],
    text_intro=(
        "The discourse in full: eight grounds for a lay proclamation of "
        "no confidence, and eight grounds for its reversal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight grounds for a proclamation of no confidence"),
        ("p", "&sect;1", "an8.88:1.1-1.4"),
        ("h3", "Eight grounds for a proclamation of confidence"),
        ("p", "&sect;2", "an8.88:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse relate to AN 8.87?",
         "opts": [
             "No relation at all",
             "A deliberate reciprocal pair — where AN 8.87 gives the "
             "Saṅgha power over a hostile layperson, this discourse gives "
             "laypeople parallel power over a hostile mendicant",
             "This discourse contradicts AN 8.87's teaching",
             "It repeats AN 8.87 word for word"],
         "correct": 1,
         "expl": "Neither side holds unilateral authority over the "
                 "relationship."},
        {"q": "What item appears in this discourse's list with no "
              "equivalent in AN 8.87?",
         "opts": [
             "Obstructing material support",
             "Being seen begging for alms at an inappropriate place",
             "Insulting laypeople",
             "Criticizing the three refuges"],
         "correct": 1,
         "expl": "A specifically monastic-conduct concern, not applicable "
                 "to a layperson's own behavior."},
        {"q": "According to the guide, what does this discourse's "
              "structure suggest about a mendicant's standing with the lay "
              "community?",
         "opts": [
             "That it is granted once at ordination and held automatically "
             "thereafter",
             "That it is maintained through ongoing conduct, not assumed "
             "as a permanent status",
             "That laypeople have no say in the matter",
             "That only senior monks are subject to this scrutiny"],
         "correct": 1,
         "expl": "A relationship earned continuously, with named grounds "
                 "for both withdrawal and restoration."},
        {"q": "What is this discourse's own title-phrase?",
         "opts": [
             "Turning the bowl upside down",
             "A proclamation of no confidence (appasāda)",
             "An act of reconciliation",
             "A period of penance"],
         "correct": 1,
         "expl": "The formal lay declaration this discourse describes."},
        {"q": "How many of the eight grounds closely parallel AN 8.87's "
              "own list?",
         "opts": [
             "None", "Six, with one genuinely new item added",
             "All eight are entirely different", "Only one"],
         "correct": 1,
         "expl": "Substantial overlap, with one item specific to "
                 "monastic alms-conduct."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.87's own lack of a stated "
                 "setting."},
    ],
    marginalia=[
        ("A reciprocal power", [
            "Saṅgha can boycott laypeople —",
            "laypeople can withdraw confidence —",
            "neither side holds it alone",
        ]),
        ("One new item added", [
            "begging in the wrong place —",
            "a monastic-specific concern",
            "with no equivalent in AN 8.87",
        ]),
        ("Standing, earned continuously", [
            "not granted once and held forever —",
            "named grounds for withdrawal",
            "and for restoration alike",
        ]),
        ("Cross-references", [
            "AN 8.87 &middot; previous, the Saṅgha's own mirror procedure",
            "AN 8.89 &middot; next, a formal act requiring reconciliation",
        ]),
    ],
    further=[
        '<a href="%s/an8.88/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.87.html">AN 8.87 &middot; Turning the Bowl Upside Down</a> &mdash; '
        "previous.",
        '<a href="an-8.89.html">AN 8.89 &middot; Reconciliation</a> &mdash; next.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.89 — Paṭisāraṇīyasutta
# --------------------------------------------------------------------------- #
page(
    89, "Paṭisāraṇīya", "Reconciliation",
    vagga=VAGGA_9,
    meta_title="AN 8.89 — Reconciliation | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Paṭisāraṇīyasutta, the formal act by which the Saṅgha may compel "
        "a mendicant to seek reconciliation with a wronged layperson, and "
        "the grounds for revoking it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Eight grounds for the Saṅgha's formal act requiring "
                 "reconciliation, then eight grounds for revoking that "
                 "act"),
        ("Length", "under 1 minute to read"),
        ("A formal remedy, not just a sanction", "Unlike AN 8.87 and AN "
                                                  "8.88's boycott and no-"
                                                  "confidence procedures, "
                                                  "this discourse's "
                                                  "formal act doesn't "
                                                  "simply withdraw "
                                                  "support — it actively "
                                                  "requires the mendicant "
                                                  "to pursue "
                                                  "reconciliation with "
                                                  "the specific wronged "
                                                  "layperson"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "formal and procedural, best read as the third of "
                       "this chapter's four institutional-procedure "
                       "discourses"),
    ],
    why=(
        "AN 8.89 names eight grounds on which the Saṅgha may formally "
        "require a mendicant to pursue reconciliation with a layperson "
        "&mdash; obstructing their material support, harming them, "
        "insulting them, dividing them, criticizing the three refuges, or "
        "breaking a legitimate promise made to them &mdash; and the "
        "grounds for revoking that requirement once satisfied."),
    guide=[
        ("The teaching in one sentence", [
            "When a mendicant obstructs a layperson's material support, "
            "harms or insults them, divides laypeople against each "
            "other, criticizes the three refuges, or breaks a legitimate "
            "promise made to a layperson, the Saṅgha may formally require "
            "that mendicant to pursue reconciliation, revoking the "
            "requirement once they keep their promise and stop the "
            "offending conduct."]),
        ("A remedy aimed at repair, not merely withdrawal", [
            "Where AN 8.87 and AN 8.88 both describe forms of formal "
            "withdrawal &mdash; the Saṅgha boycotting a layperson, "
            "laypeople withdrawing confidence in a mendicant &mdash; this "
            "discourse's formal act moves in the opposite direction: it "
            "actively compels the mendicant to go and repair a specific "
            "relationship, not simply to stop the offending behavior."]),
        ("A new item: keeping legitimate promises", [
            "This discourse adds a ground not found in either AN 8.87 or "
            "AN 8.88: not keeping a legitimate promise made to a "
            "layperson. This item shifts the register slightly from pure "
            "hostility toward a breach of trust and reliability, a "
            "distinct kind of harm to the lay relationship."]),
        ("The third of four related procedural discourses", [
            "Read alongside AN 8.87, 8.88, and AN 8.90 immediately "
            "following, this discourse forms part of a deliberate cluster "
            "closing this chapter with concrete institutional machinery "
            "&mdash; different formal responses (boycott, withdrawn "
            "confidence, compelled reconciliation, and restricted "
            "standing) matched to different situations in the "
            "relationship between the Saṅgha and its lay supporters."]),
    ],
    terms=[
        ("paṭisāraṇīyaṁ kammaṁ",
         "&ldquo;an act requiring... reconciliation&rdquo; &mdash; this "
         "discourse's own title-phrase, a formal Saṅgha procedure "
         "compelling active repair rather than mere withdrawal."),
        ("saccaṁ paṭiññaṁ na karoti",
         "&ldquo;doesn't keep a legitimate promise made to a "
         "layperson&rdquo; &mdash; the item unique to this discourse's "
         "list, concerning broken trust rather than direct hostility."),
        ("kammaṁ paṭippassambheyya",
         "&ldquo;revoke the act&rdquo; &mdash; the discourse's own term "
         "for lifting the reconciliation requirement, once its eight "
         "grounds no longer apply."),
        ("lābhaṁ pariyesati, anatthaṁ pariyesati",
         "&ldquo;tries to prevent laypeople from getting material "
         "things... tries to harm laypeople&rdquo; &mdash; two shared "
         "grounds echoing AN 8.87 and AN 8.88's own lists."),
        ("saṅghabhedāya parakkamati",
         "&ldquo;divides laypeople against each other&rdquo; &mdash; a "
         "shared ground with AN 8.88, concerning harm to lay unity."),
    ],
    text_intro=(
        "The discourse in full: eight grounds for requiring "
        "reconciliation, and eight grounds for revoking that requirement. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight grounds for requiring reconciliation"),
        ("p", "&sect;1", "an8.89:1.1-1.4"),
        ("h3", "Eight grounds for revoking the requirement"),
        ("p", "&sect;2", "an8.89:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse's formal act differ from AN 8.87 "
              "and AN 8.88's procedures?",
         "opts": [
             "It is identical to both",
             "It actively compels the mendicant to pursue reconciliation "
             "with a specific wronged layperson, rather than simply "
             "withdrawing support or confidence",
             "It applies only to laypeople, not mendicants",
             "It has no practical effect at all"],
         "correct": 1,
         "expl": "A remedy aimed at repair, not merely a form of "
                 "withdrawal."},
        {"q": "What ground appears in this discourse's list that isn't "
              "found in AN 8.87 or AN 8.88?",
         "opts": [
             "Obstructing material support",
             "Not keeping a legitimate promise made to a layperson",
             "Insulting laypeople",
             "Criticizing the three refuges"],
         "correct": 1,
         "expl": "A shift toward broken trust and reliability, distinct "
                 "from direct hostility."},
        {"q": "According to the guide, what does this discourse's place in "
              "the chapter's closing cluster represent?",
         "opts": [
             "An isolated, unrelated procedure",
             "One of four different formal responses matched to different "
             "situations in the Saṅgha-lay relationship",
             "A contradiction of AN 8.87 and AN 8.88",
             "A repeat of AN 8.90's own content"],
         "correct": 1,
         "expl": "Part of a deliberate cluster of institutional machinery "
                 "closing this chapter."},
        {"q": "What happens once the mendicant keeps their promise and "
              "stops the offending conduct?",
         "opts": [
             "Nothing changes; the act is permanent",
             "The Saṅgha may revoke the act requiring reconciliation",
             "The layperson must formally forgive them in a separate "
             "ceremony",
             "The mendicant is expelled regardless"],
         "correct": 1,
         "expl": "A reversible procedure, like AN 8.87 and AN 8.88's own "
                 "reversible acts."},
        {"q": "What kind of harm does the new promise-breaking item "
              "represent, distinct from the other grounds?",
         "opts": [
             "Physical violence",
             "A breach of trust and reliability, rather than direct "
             "hostility",
             "Financial fraud specifically",
             "Public embarrassment"],
         "correct": 1,
         "expl": "A distinct kind of relational harm, added to this "
                 "discourse's own list."},
        {"q": "Is a setting given for this discourse?",
         "opts": [
             "Yes, at Sāvatthī", "Yes, at Rājagaha",
             "No setting is stated in the source", "Yes, at Vesālī"],
         "correct": 2,
         "expl": "A bare formula, matching AN 8.87 and AN 8.88's own lack "
                 "of a stated setting."},
    ],
    marginalia=[
        ("Repair, not just withdrawal", [
            "not a boycott or lost confidence —",
            "an active requirement",
            "to seek out reconciliation",
        ]),
        ("A new kind of harm named", [
            "breaking a legitimate promise —",
            "not hostility, but broken trust,",
            "a distinct relational wound",
        ]),
        ("Third of four related procedures", [
            "boycott, no confidence,",
            "reconciliation, restricted standing —",
            "different remedies, different situations",
        ]),
        ("Cross-references", [
            "AN 8.88 &middot; previous, the lay proclamation of no "
            "confidence",
            "AN 8.90 &middot; next, closing this chapter with restricted "
            "standing after aggravated misconduct",
        ]),
    ],
    further=[
        '<a href="%s/an8.89/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.88.html">AN 8.88 &middot; A Proclamation of No Confidence</a> '
        "&mdash; previous.",
        '<a href="an-8.90.html">AN 8.90 &middot; Proper Behavior in a Case of Aggravated '
        "Misconduct</a> &mdash; next, closing this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 8.90 — Ādibrahmacariyakasutta -- closes ch.9 Sativagga with the fourth
# of this chapter's Vinaya-procedural discourses.
# --------------------------------------------------------------------------- #
page(
    90, "Ādibrahmacariyaka", "Proper Behavior in a Case of Aggravated Misconduct",
    vagga=VAGGA_9,
    meta_title="AN 8.90 — Proper Behavior in a Case of Aggravated Misconduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "closing discourse of this chapter, naming eight specific "
        "restrictions a mendicant convicted of aggravated misconduct must "
        "observe — barred from ordaining others, holding seniority, or "
        "resolving others of similar offenses. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single, unreversed list of eight specific behavioral "
                 "restrictions, with no reversal pair this time"),
        ("Length", "under 1 minute to read"),
        ("Closing this chapter's procedural run without reversal", "Unlike "
                                                                    "AN "
                                                                    "8.87, "
                                                                    "8.88, "
                                                                    "and "
                                                                    "8.89, "
                                                                    "each "
                                                                    "of "
                                                                    "which "
                                                                    "paired "
                                                                    "its "
                                                                    "formal "
                                                                    "act "
                                                                    "with "
                                                                    "explicit "
                                                                    "grounds "
                                                                    "for "
                                                                    "reversal, "
                                                                    "this "
                                                                    "discourse "
                                                                    "states "
                                                                    "only "
                                                                    "the "
                                                                    "eight "
                                                                    "restrictions "
                                                                    "themselves, "
                                                                    "with "
                                                                    "no "
                                                                    "parallel "
                                                                    "list "
                                                                    "for "
                                                                    "lifting "
                                                                    "them"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "formal and specific, closing this chapter on "
                       "institutional detail rather than doctrine or "
                       "narrative"),
    ],
    why=(
        "AN 8.90 closes this chapter by naming eight specific "
        "restrictions a mendicant convicted of aggravated misconduct must "
        "observe: barred from performing ordinations, giving dependence, "
        "supervising novices, advising nuns, accepting Saṅgha "
        "appointments, holding seniority, or excusing others from "
        "offenses similar to their own."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant convicted of aggravated misconduct must observe "
            "eight specific restrictions on their monastic role: no "
            "ordaining others, no giving dependence or supervising a "
            "novice, no serving or being appointed as adviser for nuns, "
            "no accepting any Saṅgha appointment, no position of "
            "seniority, and no resolving others from offenses similar to "
            "their own."]),
        ("Restrictions targeting authority, not participation", [
            "Every one of the eight restrictions concerns positions of "
            "authority, responsibility, or influence over others "
            "&mdash; ordaining, supervising, advising, holding seniority "
            "&mdash; rather than barring the convicted mendicant from "
            "monastic life itself. The restriction is specifically on "
            "exercising authority while under this status, not on "
            "remaining part of the community."]),
        ("A pointed final restriction", [
            "The eighth and final restriction carries particular weight: "
            "such a mendicant must not resolve others from any offense "
            "similar to the one they themselves committed &mdash; a "
            "direct acknowledgment that someone under this status lacks "
            "the standing to judge others on the very matter they "
            "themselves are answering for."]),
        ("No reversal list, closing this chapter differently", [
            "Where the three preceding discourses in this chapter's "
            "procedural cluster each paired their formal act with "
            "explicit grounds for reversal, this discourse names only "
            "the restrictions themselves, with no parallel list "
            "describing when or how they lift &mdash; closing this "
            "chapter's run of institutional-procedure discourses on a "
            "single, unreversed statement of what aggravated misconduct "
            "costs a mendicant in standing."]),
    ],
    terms=[
        ("garukāya āpattiyā parivutthaparivāso",
         "part of this discourse's own framing, a mendicant convicted of "
         "&ldquo;aggravated misconduct&rdquo; and undergoing the "
         "associated probation."),
        ("na upasampādetabbaṁ",
         "&ldquo;must not perform an ordination&rdquo; &mdash; the first "
         "restriction, barring the convicted mendicant from bringing "
         "others into full ordination."),
        ("bhikkhunovādako na sammannitabbo",
         "&ldquo;must not consent to being appointed as adviser for "
         "nuns&rdquo; &mdash; connecting this discourse back to the "
         "specific qualification named at AN 8.52 earlier in this book."),
        ("na therāsane nisīditabbaṁ",
         "&ldquo;must not be put in a position of seniority&rdquo; "
         "&mdash; one of the eight restrictions, barring the elevated "
         "standing seniority would otherwise confer."),
        ("na tādisikāya āpattiyā aññaṁ vuṭṭhāpetabbaṁ",
         "&ldquo;must not resolve others from any offense similar to "
         "that which they have transgressed&rdquo; &mdash; the eighth "
         "and final restriction, closing the list and this chapter."),
    ],
    text_intro=(
        "The discourse in full: eight restrictions on a mendicant "
        "convicted of aggravated misconduct, closing this chapter. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Eight restrictions for a mendicant convicted of "
               "aggravated misconduct"),
        ("p", "&sect;1", "an8.90:1.1-1.3"),
    ],
    quiz=[
        {"q": "What kind of restrictions does this discourse's eight items "
              "concern?",
         "opts": [
             "Dietary restrictions",
             "Positions of authority, responsibility, or influence over "
             "others — ordaining, supervising, advising, holding seniority",
             "Restrictions on speech entirely",
             "Restrictions on physical movement"],
         "correct": 1,
         "expl": "Authority and standing, not exclusion from the "
                 "community itself."},
        {"q": "What does the eighth and final restriction specifically "
              "address?",
         "opts": [
             "Financial matters",
             "Not being allowed to resolve others from an offense similar "
             "to their own transgression",
             "Travel restrictions",
             "Dietary requirements"],
         "correct": 1,
         "expl": "An acknowledgment that the convicted mendicant lacks "
                 "standing to judge others on the matter they themselves "
                 "are answering for."},
        {"q": "How does this discourse differ structurally from AN 8.87, "
              "8.88, and 8.89?",
         "opts": [
             "It is identical in structure to all three",
             "It names only the restrictions themselves, with no parallel "
             "list of grounds for reversal",
             "It has twice as many items", "It applies only to laypeople"],
         "correct": 1,
         "expl": "A single, unreversed statement, unlike the three "
                 "preceding paired procedures."},
        {"q": "What connection does this discourse have to AN 8.52, "
              "earlier in this book?",
         "opts": [
             "No connection at all",
             "One of the eight restrictions bars serving as adviser for "
             "nuns, the same role AN 8.52 named qualifications for",
             "AN 8.52 describes the same misconduct",
             "This discourse contradicts AN 8.52"],
         "correct": 1,
         "expl": "A restriction tied directly to a role this book already "
                 "examined the qualifications for."},
        {"q": "What does the guide say about whether this discourse bars "
              "the convicted mendicant from monastic life itself?",
         "opts": [
             "Yes, it results in complete expulsion",
             "No — the restrictions target specific positions of "
             "authority, not participation in the community itself",
             "The discourse doesn't address this question",
             "It applies only to newly ordained monks"],
         "correct": 1,
         "expl": "A targeted restriction on authority, not a total "
                 "exclusion."},
        {"q": "What chapter does this discourse close?",
         "opts": [
             "Gotamīvagga", "Sativagga, the ninth chapter of the Eights",
             "Yamakavagga", "Bhūmicālavagga"],
         "correct": 1,
         "expl": "The final discourse of this chapter, opened at AN 8.81."},
    ],
    marginalia=[
        ("Eight restrictions on authority", [
            "no ordaining, no supervising,",
            "no advising nuns, no seniority,",
            "no Saṅgha appointment",
        ]),
        ("A pointed final restriction", [
            "can't resolve others' offenses",
            "similar to their own —",
            "no standing to judge that matter",
        ]),
        ("No reversal named this time", [
            "unlike the three procedures before it —",
            "only the restrictions stated,",
            "closing this chapter unreversed",
        ]),
        ("Cross-references", [
            "AN 8.89 &middot; previous, the formal act requiring "
            "reconciliation",
            "AN 8.81 &middot; earlier, opening this chapter with the "
            "eight-link chain of supporting conditions",
        ]),
    ],
    further=[
        '<a href="%s/an8.90/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-8.89.html">AN 8.89 &middot; Reconciliation</a> &mdash; previous.',
        '<a href="an-8.81.html">AN 8.81 &middot; Mindfulness and Situational Awareness</a> '
        "&mdash; earlier, opening this chapter.",
    ],
)


VAGGA_10 = "<em>Sāmaññavagga</em> &mdash; the tenth chapter of the Eights"


# --------------------------------------------------------------------------- #
# AN 8.91-117 — closing ch.10 Sāmaññavagga. bilara-data holds this entire
# 27-sutta range as a single merged peyyāla file (an8.91-117), consisting
# of nothing but a chain of 27 names -- the eight-factored sabbath teaching
# already given in full at AN 8.41-45, 47-49 is peyyāla-compressed away
# entirely, leaving only the addressee list. Per the an5.308-1152/
# an6.170-649/an6.120-139/an7.96-614 precedent: PAGES.append({...}) with a
# plain dict, since the slug is not purely numeric.
#
# The source's own colophon here reads "Dutiyo paṇṇāsako samatto" ("the
# Second Fifty is finished") immediately after this vagga -- even though
# Rāgapeyyāla (AN 8.118-627) still follows numerically. This structural
# quirk is noted honestly in the guide below rather than resolved; it
# suggests the traditional "Second Fifty" label was applied to AN 8.51-117
# specifically, with the Rāgapeyyāla appended afterward as a separate
# closing section, distinct from how AN 6 and AN 7's own Rāgapeyyāla
# sections closed their nipātas directly.
# --------------------------------------------------------------------------- #
PAGES.append({
    "slug": "an-8.91-117",
    "index_pali": "Sāmañña",
    "nav_title": "Twenty-Seven Laywomen on the Sabbath",
    "source": "an8/an8.91-117",
    "crumb": "AN 8.91&ndash;117",
    "meta_title": "AN 8.91–117 — Twenty-Seven Laywomen on the Sabbath | Ru-Yi Meditation Center",
    "meta_desc": (
        "A reading guide, full English text, and self-check quiz for this chapter's "
        "closing peyyāla: the eight-factored sabbath teaching, already given in full "
        "earlier in this book, compressed here into a single chain of twenty-seven "
        "named laywomen. From Ru-Yi Meditation Center."),
    "number_line": "Aṅguttara Nikāya &middot; Discourses 8.91&ndash;117",
    "title": "Twenty-Seven Laywomen on the Sabbath",
    "subtitle": "<em>Sāmaññavagga</em> &mdash; the tenth chapter of the Eights, closing "
                "with an entire chapter's teaching reduced to a list of names",
    "glance": [
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single peyyāla-compressed line naming twenty-seven laywomen in "
                 "turn, each receiving (by implication) the identical eight-factored "
                 "sabbath teaching already spelled out in full earlier in this book"),
        ("Length", "a few seconds to read the compressed text; the underlying "
                   "teaching it stands for takes several minutes, as at AN 8.42"),
        ("An entire chapter reduced to a name list", "This chapter's own name, "
                                                      "Sāmaññavagga (&ldquo;the "
                                                      "Chapter on Similarity&rdquo;), "
                                                      "names exactly what's "
                                                      "happening structurally: "
                                                      "twenty-seven otherwise "
                                                      "separate discourses, "
                                                      "similar enough in content "
                                                      "to be compressed into one"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the compressed "
                       "text itself is trivial to read; its significance lies "
                       "entirely in what it stands for"),
    ],
    "why": (
        "AN 8.91&ndash;117 compresses twenty-seven separate discourses &mdash; each "
        "one, by implication, an instance of the eight-factored sabbath teaching "
        "already given in full at AN 8.41&ndash;45 and 47&ndash;49 &mdash; into a "
        "single line naming twenty-seven laywomen in turn, from Bojjhā through "
        "Nakula's mother, several of them well known elsewhere in this tradition."),
    "guide": [
        ("The teaching in one sentence", [
            "The same eight-factored sabbath already taught in full to Visākhā, "
            "Bojjhā, and others earlier in this book was, according to this "
            "peyyāla, taught identically to twenty-seven named laywomen in all, "
            "the source compressing all twenty-seven repetitions into a single "
            "chain of names rather than restating the teaching twenty-seven "
            "times over."]),
        ("A chapter named for what it does structurally", [
            "This chapter's own title, Sāmaññavagga, means &ldquo;the Chapter on "
            "Similarity&rdquo; &mdash; and that title describes its own "
            "compression method as much as its content: twenty-seven discourses "
            "similar enough to each other that bilara-data's source itself "
            "holds them as a single merged file, the entire content peyyāla-"
            "compressed to nothing but the addressee list."]),
        ("Twenty-seven names, some famous, most otherwise unrecorded", [
            "The list moves from largely unknown figures &mdash; Sirīmā, Padumā, "
            "Sutanā, Manujā, and many more &mdash; to several names this "
            "tradition remembers well: Visākhā, Migāra's mother, already met "
            "repeatedly earlier in this book; Khujjuttarā, celebrated elsewhere "
            "as a formerly enslaved woman who became a renowned Dhamma teacher; "
            "Sāmāvatī, a queen; Suppavāsā the Koliyan, known elsewhere for an "
            "unusually long pregnancy; and Nakula's mother, already met at AN "
            "8.48."]),
        ("A colophon that closes the Second Fifty here, not after the "
         "Rāgapeyyāla that follows", [
            "The source's own closing line after this chapter reads "
            "&ldquo;the Second Fifty is finished&rdquo; &mdash; even though AN "
            "8.118&ndash;627, the Rāgapeyyāla, still follows numerically. This "
            "is worth noting honestly rather than smoothed over: it suggests the "
            "traditional &ldquo;Second Fifty&rdquo; label applies specifically "
            "to AN 8.51&ndash;117, with the enormous Rāgapeyyāla appended "
            "afterward as its own closing section &mdash; a different structural "
            "pattern than AN 6 and AN 7, where the Rāgapeyyāla's own colophon "
            "closed the entire nipāta directly."]),
    ],
    "terms": [
        ("sāmaññavaggo",
         "&ldquo;the Chapter on Similarity&rdquo; &mdash; this chapter's own "
         "title, naming its structural method as much as any shared content."),
        ("bojjhā upāsikā ... nakulamātā gahapatānī",
         "the compressed chain of twenty-seven names opening with the "
         "laywoman Bojjhā, whose own sabbath teaching was already given in "
         "full at AN 8.45, and closing with the housewife Nakula's mother, "
         "already met earlier in this book at AN 8.48 (a different teaching, "
         "on the eight wifely qualities leading to rebirth among the "
         "Agreeable Gods)."),
        ("khujjuttarā upāsikā",
         "the laywoman Khujjuttarā, remembered elsewhere in this tradition as "
         "a formerly enslaved woman who became a celebrated Dhamma teacher in "
         "her own right."),
        ("suppavāsā koliyadhītā",
         "&ldquo;Suppavāsā the Koliyan&rdquo; &mdash; remembered elsewhere for "
         "an unusually extended pregnancy, one of several named figures in "
         "this list with a fuller story told in other discourses."),
        ("dutiyo paṇṇāsako samatto",
         "&ldquo;the Second Fifty is finished&rdquo; &mdash; the source's own "
         "closing colophon after this chapter, despite the Rāgapeyyāla still "
         "following at AN 8.118&ndash;627."),
    ],
    "text_intro": (
        "The discourse in full: the compressed chain of twenty-seven "
        "laywomen's names, standing for twenty-seven repetitions of the "
        "eight-factored sabbath teaching given in full earlier in this book. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    "text": [
        ("h3", "Twenty-seven laywomen, compressed to a single line"),
        ("p", "&sect;1", "an8.91-117:1.1-1.1"),
    ],
    "quiz": [
        {"q": "What does this peyyāla-compressed text stand for, according to "
              "the guide?",
         "opts": [
             "A new, previously unstated teaching",
             "Twenty-seven repetitions of the eight-factored sabbath teaching "
             "already given in full earlier in this book",
             "A list of monastic rules",
             "A genealogy of the Buddha's own family"],
         "correct": 1,
         "expl": "The identical sabbath teaching, applied to twenty-seven "
                 "named laywomen in turn."},
        {"q": "What does this chapter's own title, Sāmaññavagga, mean, and "
              "what does it describe?",
         "opts": [
             "'The Chapter on Wisdom' — describing doctrinal content",
             "'The Chapter on Similarity' — describing its own compression "
             "method, twenty-seven discourses similar enough to merge",
             "'The Chapter on Kings' — describing royal patrons",
             "'The Chapter on Silence' — describing a vow of quietude"],
         "correct": 1,
         "expl": "A title naming the chapter's structural method as much as "
                 "any shared content."},
        {"q": "Which named figure in this list is remembered elsewhere as a "
              "formerly enslaved woman who became a celebrated Dhamma teacher?",
         "opts": [
             "Visākhā", "Khujjuttarā",
             "Sāmāvatī", "Nakula's mother"],
         "correct": 1,
         "expl": "One of several figures in this compressed list with a "
                 "fuller story told elsewhere in the tradition."},
        {"q": "What structural quirk does the guide note about the source's "
              "own colophon after this chapter?",
         "opts": [
             "There is no colophon at all",
             "It declares 'the Second Fifty is finished' even though the "
             "Rāgapeyyāla (AN 8.118-627) still follows numerically",
             "It contradicts the sabbath teaching entirely",
             "It renumbers all twenty-seven discourses"],
         "correct": 1,
         "expl": "A genuine structural oddity, noted honestly rather than "
                 "smoothed over or forced to resolve."},
        {"q": "How many laywomen are named in this compressed chain?",
         "opts": [
             "Ten", "Twenty-seven",
             "Fifty", "One hundred"],
         "correct": 1,
         "expl": "Matching the range AN 8.91 through AN 8.117, twenty-seven "
                 "discourses in all."},
        {"q": "How does the guide characterize the relationship between AN "
              "6 and AN 7's own Rāgapeyyāla closings and this chapter's own "
              "colophon placement?",
         "opts": [
             "They are identical in structure",
             "AN 6 and AN 7's Rāgapeyyāla colophons closed their entire "
             "nipātas directly, unlike this chapter's earlier 'Second Fifty "
             "finished' declaration",
             "AN 6 and AN 7 have no Rāgapeyyāla sections at all",
             "There is no meaningful difference to note"],
         "correct": 1,
         "expl": "A different structural pattern from the precedent set in "
                 "earlier nipātas."},
    ],
    "marginalia": [
        ("Twenty-seven names, one line", [
            "Bojjhā, Sirīmā, Padumā —",
            "through Suppiyā, Nakula's mother —",
            "the same teaching, twenty-seven times",
        ]),
        ("A title naming its own method", [
            "Sāmaññavagga — 'Similarity' —",
            "twenty-seven discourses merged",
            "because they're similar enough",
        ]),
        ("Famous names among the unknown", [
            "Visākhā, Khujjuttarā the teacher,",
            "Sāmāvatī the queen,",
            "Suppavāsā's long pregnancy",
        ]),
        ("Cross-references", [
            "AN 8.90 &middot; previous, closing the previous chapter",
            "AN 8.45 &middot; earlier, Bojjhā's own sabbath teaching in full",
            "AN 8.48 &middot; earlier, Nakula's mother's own sabbath teaching "
            "in full",
        ]),
    ],
    "further": [
        '<a href="%s/an8.91-117/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="an-8.90.html">AN 8.90 &middot; Proper Behavior in a Case of Aggravated '
        "Misconduct</a> &mdash; previous, closing the previous chapter.",
        '<a href="an-8.45.html">AN 8.45 &middot; With Bojjhā on the Sabbath</a> &mdash; '
        "earlier, this same teaching given in full.",
        '<a href="an-8.48.html">AN 8.48 &middot; With Nakula&rsquo;s Mother on the '
        "Agreeable Gods</a> &mdash; earlier, another laywoman from this list, met "
        "elsewhere in this book through a different teaching.",
    ],
})
