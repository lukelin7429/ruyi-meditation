# -*- coding: utf-8 -*-
"""Chakka Nipāta — The Sixes. One discourse per page, from AN 6.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Chakka Nipāta — The Sixes"
# an-6.16.html and an-6.63.html were published before this series began working
# in order, in the earlier eighteen-page selection; they are listed in the
# index by INDEX_EXTRA and are not generated here. HEAD points at the last
# page the Fives module reached. TAIL points at the nearest already-published
# page beyond the Sixes -- an-7.6.html, from the same earlier selection --
# until the Sevens module exists and TAIL can move to its own first page.
HEAD = ("an-5.308-1152.html", "AN 5.308&ndash;1152 &middot; Untitled Discourses on Greed, and So On")
TAIL = ("an-7.6.html", "AN 7.6 &middot; Wealth in Detail")
INDEX_EXTRA = [
    ("an-6.16", "Nakulapitā", "Nakula's Father"),
    ("an-6.63", "Nibbedhika", "Penetrative"),
]

PAGES = []

VAGGA_1 = "<em>Āhuneyyavagga</em> &mdash; the first chapter of the Sixes"
SETTING_1 = ("Sāvatthī, in Jeta’s Grove, Anāthapiṇḍika’s monastery; "
             "stated at the head of AN 6.1 and understood to hold across the chapter through AN 6.9")
SETTING_CONT = ("None stated; the discourse continues from AN 6.1, whose setting at Sāvatthī "
                 "in Jeta’s Grove is understood to hold")
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Sixes."""
    d = {
        "slug": "an-6.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an6/an6.%d" % num,
        "crumb": "AN 6.%d" % num,
        "number_line": "Aṅguttara Nikāya · Discourse 6.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 6.1 — Paṭhamaāhuneyyasutta
# --------------------------------------------------------------------------- #
page(
    1, "Paṭhamaāhuneyya", "Worthy of Offerings (1st)",
    meta_title="AN 6.1 — Worthy of Offerings (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamaāhuneyyasutta, "
        "the discourse that opens the Sixes: a mendicant equanimous at all six sense doors is "
        "worthy of offerings. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "A single formula: six qualities are named, and the fourfold worthiness "
                 "formula is attached to them"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The equanimity-at-the-six-senses formula recurs widely across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short, formulaic opening, "
                       "notable chiefly for what count of six it introduces the whole nipāta with"),
    ],
    why=(
        "The Sixes open, like the Fives before them, with a bare formula and no story. But where "
        "the Fives opened on five inward qualities of a trainee, the Sixes open on six doors: the "
        "senses. A mendicant who meets whatever arises at eye, ear, nose, tongue, body, and mind "
        "without being pulled into pleasure or displeasure &mdash; staying equanimous, mindful, and "
        "aware &mdash; is called worthy of offerings, worthy of hospitality, worthy of a religious "
        "donation, worthy of veneration with cupped palms, the supreme field of merit for the "
        "world. This fourfold worthiness formula will recur constantly through this chapter; AN "
        "6.1 is where it is first paired with the number six."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who meets sights, sounds, smells, tastes, touches, and mental "
            "phenomena at their six sense doors with neither happiness nor sadness, remaining "
            "<em>equanimous, mindful, and aware</em>, has the six qualities that make them "
            "&ldquo;worthy of offerings.&rdquo;"]),
        ("A formula named four ways", [
            "The Pāli gives four separate epithets in a row &mdash; "
            "<em>āhuneyyo pāhuneyyo dakkhiṇeyyo añjalikaraṇīyo</em> &mdash; each naming a "
            "different social occasion for giving: an oblation offered from a distance, a guest "
            "gift given to someone arriving, a donation given as an act of religious merit, and a "
            "simple gesture of raised palms. English collapses these into &ldquo;worthy of "
            "offerings dedicated to the gods, worthy of hospitality, worthy of a religious "
            "donation, worthy of veneration with cupped palms.&rdquo; The chapter takes its name, "
            "<em>Āhuneyyavagga</em>, from the first of the four."]),
        ("Six doors, not six qualities of mind", [
            "It would be easy to misread this as praising six separate mental qualities. It "
            "names one quality &mdash; equanimity paired with mindfulness and full awareness "
            "&mdash; and applies it across six occasions, one for each sense door. The "
            "&ldquo;six things&rdquo; of the title are the six doors the one quality is tested "
            "at, not six different virtues."]),
        ("Not withdrawal from the senses", [
            "The formula does not describe a mendicant who avoids sights and sounds, or who "
            "fails to notice them. It describes one who sees, hears, smells, tastes, touches, "
            "and cognizes exactly as anyone does, and simply does not tip into liking or "
            "disliking what arises. The senses keep functioning; what changes is what happens "
            "after contact."]),
        ("An opening formula the chapter will keep testing", [
            "AN 6.1 gives the fourfold worthiness formula its simplest possible attachment: "
            "equanimity at the six senses. The next several discourses attach the same formula "
            "to increasingly different sets of six qualities &mdash; the six kinds of "
            "superhuman knowledge at AN 6.2, the five spiritual faculties plus liberation at AN "
            "6.3 &mdash; testing how far a single closing refrain can stretch across different "
            "content."]),
    ],
    terms=[
        ("āhuneyya",
         "&ldquo;worthy of an oblation&rdquo; &mdash; the first of the sutta&rsquo;s four "
         "worthiness epithets, and the word the whole chapter is named for."),
        ("pāhuneyya",
         "&ldquo;worthy of hospitality&rdquo; &mdash; worthy of the gift given to a guest "
         "arriving from afar."),
        ("dakkhiṇeyya",
         "&ldquo;worthy of a religious donation&rdquo; &mdash; worthy of a gift given "
         "specifically as an act of merit-making."),
        ("añjalikaraṇīya",
         "&ldquo;worthy of being greeted with joined palms&rdquo; &mdash; worthy of the simple "
         "gesture of respect, without any material gift attached."),
        ("upekkhako viharati sato sampajāno",
         "&ldquo;remains equanimous, mindful, and aware&rdquo; &mdash; the three-part standing "
         "description of the response this discourse asks for at each of the six sense doors."),
    ],
    text_intro=(
        "The discourse in full: equanimity at the six sense doors, and the fourfold worthiness "
        "formula. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Sāvatthī"),
        ("p", "&sect;1", "an6.1:1.1-1.6"),
        ("h3", "Six qualities, one at each sense door"),
        ("p", "&sect;2", "an6.1:2.1-2.9"),
        ("h3", "The conclusion"),
        ("p", "&sect;3", "an6.1:3.1-3.2"),
    ],
    quiz=[
        {"q": "What six occasions does AN 6.1 attach the worthiness formula to?",
         "opts": [
             "Six virtues of generosity, ethics, and patience",
             "The six sense doors — eye, ear, nose, tongue, body, and mind",
             "Six stages of meditative absorption",
             "Six kinds of superhuman knowledge"],
         "correct": 1,
         "expl": "One quality, equanimity, tested at each of the six senses in turn."},
        {"q": "What is the one quality being tested at each sense door?",
         "opts": [
             "Complete withdrawal from sense contact",
             "Remaining equanimous, mindful, and aware — neither happy nor sad",
             "Actively suppressing every sensation",
             "Analyzing each sensation philosophically"],
         "correct": 1,
         "expl": "Upekkhako viharati sato sampajāno — the discourse's standing phrase."},
        {"q": "How many separate epithets make up the &lsquo;worthy of offerings&rsquo; formula?",
         "opts": ["Two", "Three", "Four", "Six"],
         "correct": 2,
         "expl": "Āhuneyyo, pāhuneyyo, dakkhiṇeyyo, añjalikaraṇīyo — four occasions for giving."},
        {"q": "What does the chapter title &lsquo;Āhuneyyavagga&rsquo; mean?",
         "opts": [
             "The Chapter on Enlightenment",
             "The Chapter on Worthy of Offerings",
             "The Chapter on the Senses",
             "The Chapter on Equanimity"],
         "correct": 1,
         "expl": "Taken from the first of the four worthiness epithets, āhuneyya."},
        {"q": "Does the formula describe a mendicant who avoids or fails to notice sense objects?",
         "opts": [
             "Yes — full sensory withdrawal is the point",
             "No — the senses keep functioning; what changes is the response after contact",
             "Only for sight and sound, not the other senses",
             "The text does not address this"],
         "correct": 1,
         "expl": "The formula is about response, not sensory absence."},
        {"q": "Where is AN 6.1 set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Kapilavatthu, among the Sakyans",
             "Vesālī, in the Great Wood"],
         "correct": 1,
         "expl": "The setting most Aṅguttara discourses default to when nothing more specific is named."},
        {"q": "How does the &lsquo;six things&rsquo; of the title relate to the one quality of "
              "equanimity?",
         "opts": [
             "They are six separate, unrelated virtues",
             "They are six doors the one quality of equanimity is tested at, not six different virtues",
             "The six things replace equanimity entirely",
             "Each door requires a completely different response"],
         "correct": 1,
         "expl": "One quality, applied at six occasions — not six different qualities."},
        {"q": "What happens to the fourfold worthiness formula across the rest of the chapter?",
         "opts": [
             "It never appears again after AN 6.1",
             "It recurs, attached to increasingly different sets of six qualities",
             "It is replaced by a different formula at AN 6.2",
             "It is only used for lay followers, not mendicants"],
         "correct": 1,
         "expl": "AN 6.2 attaches it to six kinds of superhuman knowledge, AN 6.3 to the five "
                 "faculties plus liberation, and so on."},
        {"q": "Who is speaking in AN 6.1?",
         "opts": [
             "A group of senior mendicants",
             "The Buddha alone, addressing the mendicants",
             "Mahānāma the Sakyan, questioning the Buddha",
             "Ānanda, reporting a teaching"],
         "correct": 1,
         "expl": "A direct address with no interlocutor — the Sixes' most common opening pattern."},
        {"q": "What is the relationship between AN 6.1 and AN 5.1, the opening of the previous "
              "nipāta?",
         "opts": [
             "They are identical in content",
             "Both open their nipāta with a bare formula and no story, but built from different "
             "material — five inward qualities of a trainee versus six sense doors",
             "AN 6.1 directly contradicts AN 5.1",
             "AN 6.1 is a word-for-word repetition of AN 5.1 with the number changed"],
         "correct": 1,
         "expl": "A shared opening strategy — terse, formulaic — applied to entirely different lists."},
    ],
    marginalia=[
        ("The four epithets", [
            "<span class=\"pali\">āhuneyya</span>oblation-worthy",
            "<span class=\"pali\">pāhuneyya</span>hospitality-worthy",
            "<span class=\"pali\">dakkhiṇeyya</span>donation-worthy",
            "<span class=\"pali\">añjalikaraṇīya</span>salutation-worthy",
        ]),
        ("Six doors", [
            "eye &middot; ear &middot; nose",
            "tongue &middot; body &middot; mind",
            "one response tested six times",
        ]),
        ("The standing response", [
            "<span class=\"pali\">upekkhako</span>equanimous",
            "<span class=\"pali\">sato</span>mindful",
            "<span class=\"pali\">sampajāno</span>aware",
        ]),
        ("Cross-references", [
            "AN 5.1 &middot; the Fives' own bare opening",
            "AN 6.2 &middot; next, the same formula stretched further",
        ]),
    ],
    further=[
        '<a href="%s/an6.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.2.html">AN 6.2 &middot; Worthy of Offerings (2nd)</a> &mdash; next, where '
        "the same worthiness formula is attached to the six kinds of superhuman knowledge.",
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; the Fives&rsquo; own bare, '
        "formulaic opening, for comparison.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.2 — Dutiyaāhuneyyasutta
# --------------------------------------------------------------------------- #
page(
    2, "Dutiyaāhuneyya", "Worthy of Offerings (2nd)",
    meta_title="AN 6.2 — Worthy of Offerings (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyaāhuneyyasutta, "
        "which attaches the worthiness formula to the six kinds of superhuman knowledge, from "
        "psychic power to the ending of defilements. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A single long formula: the six <em>abhiññā</em> spelled out in full, closed "
                 "by the worthiness refrain"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The six-fold abhijñā list has close counterparts across the "
                              "Chinese Āgamas and Abhidharma literature; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the content is standard and "
                       "recurs constantly elsewhere in the canon, but the list is long and "
                       "technical"),
    ],
    why=(
        "AN 6.1 attached the worthiness formula to equanimity at the six senses. AN 6.2 attaches "
        "the identical formula to something far larger: the six <em>abhiññā</em>, the "
        "&ldquo;superhuman knowledges&rdquo; that mark the furthest reach of the canon&rsquo;s "
        "meditative and liberating path. Five are attainments &mdash; psychic power, clairaudience, "
        "mind-reading, recollection of past lives, clairvoyance &mdash; and the sixth is the "
        "ending of defilements itself, the goal the other five all serve. Reading AN 6.1 and 6.2 "
        "side by side shows the same closing refrain doing very different work: at 6.1 it crowns a "
        "minimal, everyday equanimity; at 6.2 it crowns the highest attainments the tradition "
        "describes."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has the six superhuman knowledges &mdash; psychic power, "
            "clairaudience, mind-reading, recollection of past lives, clairvoyance, and the "
            "ending of defilements &mdash; is worthy of offerings, exactly as the equanimous "
            "mendicant of AN 6.1 was said to be."]),
        ("Five attainments and one culmination", [
            "The list is not six equal items. The first five &mdash; often grouped as the "
            "<em>pañca abhiññā</em>, the five mundane superhuman knowledges &mdash; are powers "
            "any sufficiently accomplished meditator might in principle develop, and the texts "
            "elsewhere note that they can be lost, or developed without full liberation. The "
            "sixth, the ending of defilements through freedom of heart and freedom by wisdom, is "
            "categorically different: it is full awakening itself, and it alone is irreversible."]),
        ("The five, briefly", [
            "Psychic power (<em>iddhividha</em>): multiplying the body, passing through solid "
            "matter, walking on water, flying, touching sun and moon. Clairaudience "
            "(<em>dibbasota</em>): hearing sounds human and heavenly, near and far. Mind-reading "
            "(<em>cetopariya</em>): knowing the state of another&rsquo;s mind &mdash; with or "
            "without greed, hate, delusion, and several further pairs. Recollection of past "
            "lives (<em>pubbenivāsānussati</em>): remembering former births in detail, across "
            "world-cycles. Clairvoyance (<em>dibbacakkhu</em>, here called the "
            "&ldquo;divine eye&rdquo;): seeing beings die and be reborn according to their deeds."]),
        ("The sixth as the reason for the other five", [
            "The passage&rsquo;s own structure makes a point often missed when the five worldly "
            "powers are discussed on their own: here they are listed only as a prelude to the "
            "sixth, the ending of defilements. Nothing in the discourse suggests the five are "
            "sought for their own sake, or that possessing them without the sixth would itself "
            "satisfy the worthiness formula. The passage names all six together as one bundle of "
            "qualities, but the weight falls on the last."]),
        ("Why this belongs beside AN 6.1", [
            "Placed second in the chapter, this discourse stretches the fourfold worthiness "
            "formula from its simplest possible application to one of its largest. The pairing "
            "is instructive about how these formulaic openings work across the Aṅguttara: the "
            "same closing refrain is portable across radically different content, and its "
            "repetition is not padding but the thread that ties a whole chapter&rsquo;s "
            "otherwise disparate material together."]),
    ],
    terms=[
        ("abhiññā",
         "&ldquo;superhuman knowledge,&rdquo; &ldquo;direct knowledge&rdquo; &mdash; the six "
         "attainments this discourse lists, ending in the destruction of defilements."),
        ("iddhividha",
         "&ldquo;kinds of psychic power&rdquo; &mdash; the first of the six, covering "
         "multiplying the body and passing unobstructed through solid matter."),
        ("dibbasota",
         "&ldquo;divine ear,&rdquo; clairaudience &mdash; the second knowledge, hearing sounds "
         "both human and heavenly."),
        ("cetopariyañāṇa",
         "knowledge of others&rsquo; minds &mdash; the third knowledge, reading another&rsquo;s "
         "mental state as with or without greed, hate, and delusion, and more."),
        ("āsavānaṁ khaya",
         "&ldquo;ending of defilements&rdquo; &mdash; the sixth and culminating knowledge, "
         "reached through freedom of heart and freedom by wisdom."),
    ],
    text_intro=(
        "The discourse in full: the six superhuman knowledges, and the worthiness formula. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The formula, and the first knowledge: psychic power"),
        ("p", "&sect;1", "an6.2:1.1-1.3"),
        ("h3", "The second: clairaudience"),
        ("p", "&sect;2", "an6.2:2.1"),
        ("h3", "The third: reading other minds"),
        ("p", "&sect;3", "an6.2:3.1-3.17"),
        ("h3", "The fourth: recollecting past lives"),
        ("p", "&sect;4", "an6.2:4.1"),
        ("h3", "The fifth: clairvoyance"),
        ("p", "&sect;5", "an6.2:5.1"),
        ("h3", "The sixth: the ending of defilements, and the conclusion"),
        ("p", "&sect;6", "an6.2:6.1-7.1"),
    ],
    quiz=[
        {"q": "What six qualities does AN 6.2 attach the worthiness formula to?",
         "opts": [
             "Equanimity at the six sense doors",
             "The six superhuman knowledges, ending in the ending of defilements",
             "The five faculties plus liberation",
             "Six topics for recollection"],
         "correct": 1,
         "expl": "Psychic power, clairaudience, mind-reading, past-life recollection, "
                 "clairvoyance, and the ending of defilements."},
        {"q": "How does the text itself structure the six knowledges?",
         "opts": [
             "As six equal, interchangeable items",
             "As five worldly attainments culminating in a sixth, categorically different one",
             "As six stages that must be attained in a fixed order over one lifetime",
             "As six alternative paths, only one of which need be followed"],
         "correct": 1,
         "expl": "The first five are mundane abhiññā; the sixth is full awakening itself."},
        {"q": "What distinguishes the sixth knowledge from the first five?",
         "opts": [
             "It requires no meditation at all",
             "It is irreversible, unlike the first five, which the texts elsewhere note can be lost",
             "It is available only to lay followers",
             "It has nothing to do with liberation"],
         "correct": 1,
         "expl": "The ending of defilements is full awakening; the other five are not."},
        {"q": "What is <em>iddhividha</em>, the first knowledge listed?",
         "opts": [
             "Reading the minds of others",
             "Various kinds of psychic power, such as passing through solid matter",
             "Hearing sounds both human and heavenly",
             "Recollecting one's own past lives"],
         "correct": 1,
         "expl": "Multiplying the body, walking on water, flying — the psychic-power group."},
        {"q": "What does <em>dibbasota</em> mean?",
         "opts": ["Divine eye", "Divine ear, or clairaudience", "Mind-reading", "Past-life recollection"],
         "correct": 1,
         "expl": "Hearing sounds human and heavenly, near and far."},
        {"q": "According to the discourse's own structure, why are the five worldly knowledges "
              "listed at all?",
         "opts": [
             "As ends in themselves, sought independently of liberation",
             "As a prelude to the sixth — the ending of defilements — with the weight falling on "
             "the last item",
             "As a warning against pursuing meditation too far",
             "As a description of what lay followers, not mendicants, should aim for"],
         "correct": 1,
         "expl": "Nothing in the passage suggests the five are valued apart from the sixth."},
        {"q": "How does AN 6.2 relate to AN 6.1?",
         "opts": [
             "It contradicts AN 6.1's teaching",
             "It attaches the identical worthiness formula to a far larger set of qualities than "
             "AN 6.1's simple equanimity",
             "It is unrelated in both form and content",
             "It replaces the worthiness formula with a new one"],
         "correct": 1,
         "expl": "Same closing refrain, stretched from a minimal to a maximal application."},
        {"q": "What kind of mental states does the mind-reading knowledge distinguish?",
         "opts": [
             "Only whether a mind is happy or sad",
             "Pairs such as mind with or without greed, hate, and delusion, constricted or "
             "expansive, and more",
             "Only the minds of enlightened beings",
             "The physical health of another person"],
         "correct": 1,
         "expl": "A long list of paired mental qualities, read directly in another's mind."},
        {"q": "What does the discourse say about clairvoyance (the fifth knowledge)?",
         "opts": [
             "It only shows a being's present appearance, not their future",
             "It shows beings passing away and being reborn according to their deeds",
             "It is identical to clairaudience",
             "It cannot distinguish good rebirths from bad ones"],
         "correct": 1,
         "expl": "Seeing how deeds by body, speech, and mind shape where beings are reborn."},
        {"q": "Is AN 6.2 set at a newly stated location?",
         "opts": [
             "Yes, at Rājagaha",
             "No — no setting is given; it continues from AN 6.1's setting at Sāvatthī",
             "Yes, at Kapilavatthu",
             "Yes, on Vulture's Peak"],
         "correct": 1,
         "expl": "A bare continuation, as is common through the rest of this chapter."},
    ],
    marginalia=[
        ("The six knowledges", [
            "1. psychic power",
            "2. clairaudience",
            "3. mind-reading",
            "4. past lives",
            "5. clairvoyance",
            "6. end of defilements",
        ]),
        ("Five and one", [
            "five mundane, losable",
            "one irreversible &mdash;",
            "full awakening itself",
        ]),
        ("Same refrain, new scale", [
            "AN 6.1: equanimity",
            "AN 6.2: the highest",
            "attainments described",
        ]),
        ("Cross-references", [
            "AN 6.1 &middot; the same formula, minimal case",
            "AN 6.3 &middot; next, the five faculties",
        ]),
    ],
    further=[
        '<a href="%s/an6.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.1.html">AN 6.1 &middot; Worthy of Offerings (1st)</a> &mdash; previous, '
        "where the same formula crowned a minimal, everyday equanimity.",
        '<a href="an-6.3.html">AN 6.3 &middot; Faculties</a> &mdash; next, where the formula is '
        "attached to the five spiritual faculties.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.3 — Indriyasutta
# --------------------------------------------------------------------------- #
page(
    3, "Indriya", "Faculties",
    meta_title="AN 6.3 — Faculties | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Indriyasutta, the "
        "discourse that gives the classic five spiritual faculties — faith, energy, mindfulness, "
        "immersion, wisdom — their own place in the Sixes. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The worthiness formula attached to the five faculties plus liberation, named "
                 "as one bundle of &lsquo;six&rsquo;"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The five-faculty list (<em>indriya</em>) recurs constantly across "
                              "the Chinese Āgamas and Abhidharma literature as part of the "
                              "thirty-seven aids to awakening; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short formula, but one "
                       "carrying real technical weight in the wider canon"),
    ],
    why=(
        "AN 5.1, at the head of the Fives, mentioned in passing that its own five-item list of a "
        "trainee&rsquo;s powers shares three terms &mdash; faith, energy, wisdom &mdash; with "
        "&ldquo;the much better known five faculties and five powers,&rdquo; without giving that "
        "better-known pair a discourse of its own. AN 6.3 is where that pair — faith, energy, "
        "mindfulness, immersion, wisdom, as <em>indriya</em>, faculties — finally gets named in "
        "full, folded into this chapter&rsquo;s worthiness formula as a bundle of six alongside "
        "liberation itself."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has the five faculties &mdash; faith, energy, mindfulness, "
            "immersion, and wisdom &mdash; and who has, through them, reached the ending of "
            "defilements and full liberation, is worthy of offerings."]),
        ("The list flagged three discourses back", [
            "AN 5.1&rsquo;s reading guide already anticipated this pair, warning readers not to "
            "confuse its own five powers of a trainee (faith, conscience, prudence, energy, "
            "wisdom) with the standard five faculties and five powers (faith, energy, "
            "mindfulness, immersion, wisdom). AN 6.3 is the discourse where that standard list, "
            "under the name <em>indriya</em>, receives its own dedicated statement in this "
            "series for the first time."]),
        ("Faculties, powers, and one further ingredient", [
            "The five terms named here &mdash; <em>saddhindriya, vīriyindriya, satindriya, "
            "samādhindriya, paññindriya</em> &mdash; are elsewhere in the canon paired with an "
            "identical five-item list called <em>bala</em>, powers, differing only in grammatical "
            "form and emphasis: a faculty is a capacity that can be developed or left "
            "undeveloped; a power is that same capacity once it has become unshakeable. AN 6.4, "
            "immediately following, states the power-version of this same list."]),
        ("Six qualities, five named plus liberation", [
            "The discourse is careful to count six qualities even though only five are named as "
            "<em>indriya</em>: the passage closes each of the five with &ldquo;and they realize "
            "the undefiled freedom of heart and freedom by wisdom &hellip; due to the ending of "
            "defilements&rdquo; &mdash; the same closing clause that ended the sixth superhuman "
            "knowledge at AN 6.2. Liberation itself is the sixth item, not merely a decorative "
            "flourish added to five faculties."]),
        ("Faculties as the root, not the crown", [
            "Where AN 6.2 crowned the worthiness formula with the most dramatic attainments the "
            "canon describes, AN 6.3 grounds it instead in five ordinary capacities every "
            "practitioner is asked to cultivate from the outset. Read together, the two "
            "discourses suggest that the same worthiness the tradition praises can be reached "
            "either by naming its most spectacular expression or by naming the plain faculties "
            "that make any progress toward it possible at all."]),
    ],
    terms=[
        ("indriya",
         "&ldquo;faculty&rdquo; &mdash; a capacity that governs and directs practice; the term "
         "this discourse uses for the five-item list, and the discourse&rsquo;s own title."),
        ("saddhindriya",
         "the faculty of faith (<em>saddhā</em> + <em>indriya</em>) &mdash; the first of the "
         "five, confidence directed toward the Buddha&rsquo;s awakening."),
        ("vīriyindriya",
         "the faculty of energy &mdash; sustained effort in practice, the second of the five."),
        ("samādhindriya",
         "the faculty of immersion &mdash; unification and steadiness of mind, the fourth of "
         "the five."),
        ("paññindriya",
         "the faculty of wisdom &mdash; discernment of things as they are, the fifth of the "
         "five and the one the whole set is said to culminate in."),
    ],
    text_intro=(
        "The discourse in full: the five faculties and liberation, closing the worthiness "
        "formula. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The formula, and the five faculties"),
        ("p", "&sect;1", "an6.3:1.1-1.4"),
    ],
    quiz=[
        {"q": "What five qualities does AN 6.3 name as <em>indriya</em>, faculties?",
         "opts": [
             "Faith, conscience, prudence, energy, and wisdom",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "Generosity, ethics, patience, energy, and wisdom",
             "The six sense doors"],
         "correct": 1,
         "expl": "Saddhindriya, vīriyindriya, satindriya, samādhindriya, paññindriya."},
        {"q": "How did AN 5.1's reading guide already anticipate this discourse?",
         "opts": [
             "It quoted AN 6.3 directly",
             "It warned readers not to confuse its own five powers of a trainee with the "
             "'much better known five faculties and five powers,' without yet giving that list "
             "its own discourse",
             "It claimed the two lists were identical",
             "It made no mention of any five-item list"],
         "correct": 1,
         "expl": "AN 6.3 is where that anticipated, better-known list finally gets its own page."},
        {"q": "How many qualities does AN 6.3 actually count toward the worthiness formula?",
         "opts": [
             "Five — only the faculties",
             "Six — the five faculties plus liberation itself",
             "Four — only faith, energy, and wisdom, doubled",
             "Ten"],
         "correct": 1,
         "expl": "The closing clause adds liberation as the sixth item, matching AN 6.2's structure."},
        {"q": "What is the relationship between a faculty (<em>indriya</em>) and a power "
              "(<em>bala</em>) in this same five-item list?",
         "opts": [
             "They are entirely unrelated lists",
             "The same five capacities, differing chiefly in whether they are still developing "
             "(faculty) or have become unshakeable (power)",
             "Powers are only for lay followers, faculties only for mendicants",
             "A power is weaker than a faculty"],
         "correct": 1,
         "expl": "AN 6.4, immediately following, restates the identical list as bala."},
        {"q": "Which faculty is said to be the one the whole set culminates in?",
         "opts": ["Faith", "Energy", "Immersion", "Wisdom"],
         "correct": 3,
         "expl": "Paññindriya, wisdom, closes the list and directs the other four."},
        {"q": "What does AN 6.3 ground the worthiness formula in, compared to AN 6.2?",
         "opts": [
             "The same spectacular attainments as AN 6.2",
             "Five ordinary capacities cultivated from the outset of practice, rather than the "
             "most dramatic attainments the canon describes",
             "A completely unrelated set of ethical precepts",
             "Nothing — AN 6.3 repeats AN 6.2 verbatim"],
         "correct": 1,
         "expl": "AN 6.2 crowns the formula with the highest attainments; AN 6.3 grounds it in "
                 "plain faculties."},
        {"q": "Is AN 6.3 set at a newly stated location?",
         "opts": [
             "Yes, at Kapilavatthu",
             "No — it continues from AN 6.1's setting at Sāvatthī",
             "Yes, at Rājagaha",
             "The setting is left deliberately ambiguous"],
         "correct": 1,
         "expl": "A bare continuation, as with AN 6.2."},
        {"q": "What does <em>vīriyindriya</em> mean?",
         "opts": ["The faculty of faith", "The faculty of energy", "The faculty of wisdom", "The faculty of immersion"],
         "correct": 1,
         "expl": "Vīriya, energy or sustained effort, plus indriya, faculty."},
        {"q": "How does AN 6.4 relate to AN 6.3?",
         "opts": [
             "It contradicts AN 6.3's list",
             "It restates the identical five items as bala, powers, rather than indriya, faculties",
             "It is unrelated in content",
             "It adds a sixth new faculty"],
         "correct": 1,
         "expl": "Same five terms, recast in the bala grammatical form — the next discourse."},
        {"q": "What broader canonical structure does this five-item list belong to?",
         "opts": [
             "It is unique to this discourse",
             "The thirty-seven aids to awakening, where indriya and bala form two of seven groups",
             "It belongs only to lay ethical teaching",
             "It is a Northern-tradition-only addition"],
         "correct": 1,
         "expl": "As AN 5.1's guide already noted, this is 'the much better known five faculties "
                 "and five powers.'"},
    ],
    marginalia=[
        ("The five faculties", [
            "<span class=\"pali\">saddhā</span>faith",
            "<span class=\"pali\">vīriya</span>energy",
            "<span class=\"pali\">sati</span>mindfulness",
            "<span class=\"pali\">samādhi</span>immersion",
            "<span class=\"pali\">paññā</span>wisdom",
        ]),
        ("Not AN 5.1's five", [
            "AN 5.1: faith, conscience,",
            "prudence, energy, wisdom",
            "— a different list, three",
            "terms shared with this one",
        ]),
        ("Faculty vs. power", [
            "<span class=\"pali\">indriya</span>developing capacity",
            "<span class=\"pali\">bala</span>unshakeable capacity",
            "same five terms, two forms",
        ]),
        ("Cross-references", [
            "AN 5.1 &middot; anticipated this list",
            "AN 6.2 &middot; the same six-count structure",
            "AN 6.4 &middot; next, the power-version",
        ]),
    ],
    further=[
        '<a href="%s/an6.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.4.html">AN 6.4 &middot; Powers</a> &mdash; next, restating the identical '
        "five qualities as bala.",
        '<a href="an-5.1.html">AN 5.1 &middot; In Brief</a> &mdash; where this better-known list '
        "was first flagged, though not yet given its own discourse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.4 — Balasutta
# --------------------------------------------------------------------------- #
page(
    4, "Bala", "Powers",
    meta_title="AN 6.4 — Powers | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Balasutta, which "
        "restates the five faculties of AN 6.3 as bala, powers — the same five capacities named "
        "as unshakeable rather than developing. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The worthiness formula attached to the five powers plus liberation — "
                 "identical in structure to AN 6.3, one grammatical form removed"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The five-power list (<em>bala</em>) recurs constantly across the "
                              "Chinese Āgamas and Abhidharma literature, paired everywhere with "
                              "the five faculties; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a near-repeat of AN 6.3, "
                       "worth reading for the single word that changes"),
    ],
    why=(
        "AN 6.4 is AN 6.3 with one change: <em>indriya</em>, faculty, becomes <em>bala</em>, "
        "power, in each of the five compound terms. Everything else &mdash; the six-count "
        "structure, the closing clause about liberation, the worthiness formula &mdash; is "
        "identical. Placed back to back, the two discourses let a reader see directly what the "
        "tradition means by pairing these two grammatical forms of the same five qualities: not "
        "two different lists, but the same capacities described first as still being cultivated, "
        "then as having become unshakeable."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who has the five powers &mdash; faith, energy, mindfulness, immersion, "
            "and wisdom &mdash; and who has, through them, reached the ending of defilements and "
            "full liberation, is worthy of offerings &mdash; word for word as AN 6.3, with "
            "<em>bala</em> in place of <em>indriya</em>."]),
        ("What changes, and what does not", [
            "Comparing the Pāli of the two discourses side by side: <em>saddhindriya</em> becomes "
            "<em>saddhābalena</em>, <em>vīriyindriya</em> becomes <em>vīriyabalena</em>, and so on "
            "through all five. The English translation renders both as &ldquo;the "
            "&hellip; of faith, energy, mindfulness, immersion, and wisdom&rdquo; with only "
            "&ldquo;faculties&rdquo; or &ldquo;powers&rdquo; distinguishing them &mdash; a case "
            "where the reading guide&rsquo;s caution from AN 5.1, to check the Pāli rather than "
            "judge by English wording alone, applies directly."]),
        ("A traditional distinction: strength against opposition", [
            "Commentarial tradition explains the difference this way: a faculty "
            "(<em>indriya</em>) exercises governance over its own domain &mdash; faith over "
            "confidence, energy over exertion, and so on &mdash; while a power (<em>bala</em>) is "
            "that same quality once it can no longer be shaken by its opposite. Faith as power "
            "is unmoved by doubt; energy as power is unmoved by laziness; wisdom as power is "
            "unmoved by ignorance. The Sixes place these two framings of one list back to back "
            "rather than merging them into a single ten-item set."]),
        ("Why two near-identical discourses, not one", [
            "A single combined discourse naming ten qualities would have been possible; the "
            "canon instead keeps <em>indriya</em> and <em>bala</em> as separate statements, each "
            "given its own worthiness formula. The repetition itself is the point: the same five "
            "capacities are worth affirming twice, once under each aspect, rather than being "
            "collapsed into one mention."]),
        ("Closing the chapter's first quarter", [
            "AN 6.1 through 6.4 form a loose unit: equanimity at the six senses, the six "
            "superhuman knowledges, the five faculties, the five powers &mdash; four different "
            "contents, one identical closing formula. The next three discourses turn from lists "
            "of qualities to a single extended simile, the thoroughbred horse."]),
    ],
    terms=[
        ("bala",
         "&ldquo;power&rdquo; &mdash; the five capacities named here, identical to AN 6.3&rsquo;s "
         "faculties but described as unshakeable by their opposites."),
        ("saddhābala",
         "the power of faith &mdash; confidence no longer moved by doubt."),
        ("vīriyabala",
         "the power of energy &mdash; sustained effort no longer moved by laziness."),
        ("samādhibala",
         "the power of immersion &mdash; steadiness of mind no longer moved by distraction."),
        ("paññābala",
         "the power of wisdom &mdash; discernment no longer moved by ignorance, closing the list "
         "as it did at AN 6.3."),
    ],
    text_intro=(
        "The discourse in full: the five powers and liberation, closing the worthiness formula. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The formula, and the five powers"),
        ("p", "&sect;1", "an6.4:1.1-1.4"),
    ],
    quiz=[
        {"q": "What is the single difference between AN 6.3 and AN 6.4?",
         "opts": [
             "AN 6.4 names six new qualities entirely",
             "AN 6.4 restates the same five qualities as bala, powers, rather than indriya, "
             "faculties",
             "AN 6.4 drops the worthiness formula",
             "AN 6.4 is set at a different location"],
         "correct": 1,
         "expl": "Saddhindriya becomes saddhābala, and so through all five terms — everything "
                 "else is identical."},
        {"q": "How does the commentarial tradition traditionally distinguish a faculty from a "
              "power, for the same quality?",
         "opts": [
             "A faculty is stronger than a power",
             "A faculty exercises governance over its own domain; a power is that same quality "
             "once unshakeable by its opposite",
             "They are entirely different capacities with no relation",
             "Only lay followers have faculties; only mendicants have powers"],
         "correct": 1,
         "expl": "Faith as power, for instance, is unmoved by doubt."},
        {"q": "What lesson from AN 5.1's reading guide does the indriya/bala comparison illustrate?",
         "opts": [
             "That Pāli terms are unimportant compared to English wording",
             "That formulas sounding alike in English translation may differ in ways worth "
             "checking against the Pāli directly",
             "That the five faculties and five powers are unrelated lists",
             "That translations by different scholars always disagree"],
         "correct": 1,
         "expl": "English renders both as similar phrasing; the Pāli distinguishes indriya from "
                 "bala precisely."},
        {"q": "Why does the canon keep faculties and powers as two separate discourses rather "
              "than merging them into one ten-item list?",
         "opts": [
             "It is simply an oversight in compilation",
             "The repetition is itself meaningful — the same five capacities affirmed twice, "
             "once under each aspect",
             "The two lists actually name different qualities",
             "Powers belong to a later historical layer and were never meant to be combined"],
         "correct": 1,
         "expl": "The discourse offers no combined ten-item version; each aspect gets its own "
                 "full statement."},
        {"q": "What example does the guide give of faith as a 'power' rather than a 'faculty'?",
         "opts": [
             "Faith that requires no testing",
             "Faith unmoved by doubt, as opposed to faith that is still developing",
             "Faith found only in advanced meditators",
             "Faith identical to blind belief"],
         "correct": 1,
         "expl": "Power names the point at which the quality can no longer be shaken by its "
                 "opposite."},
        {"q": "What do AN 6.1 through 6.4 have in common?",
         "opts": [
             "They are unrelated discourses grouped by chance",
             "Four different sets of qualities, each closed by the identical worthiness formula",
             "They all take place at Kapilavatthu",
             "They all involve a dialogue with a named questioner"],
         "correct": 1,
         "expl": "Equanimity, the six knowledges, the faculties, the powers — one refrain "
                 "throughout."},
        {"q": "What comes next in the chapter, after this loose four-discourse unit on qualities?",
         "opts": [
             "A discourse on generosity",
             "A three-part simile of the thoroughbred horse, at AN 6.5–6.7",
             "The end of the chapter",
             "A dialogue with a deity"],
         "correct": 1,
         "expl": "AN 6.5 through 6.7 turn from lists to an extended simile."},
        {"q": "How many qualities does AN 6.4 count toward the worthiness formula?",
         "opts": ["Five", "Six — the five powers plus liberation", "Four", "Ten"],
         "correct": 1,
         "expl": "Matching AN 6.3's structure exactly."},
        {"q": "Is AN 6.4 set at a newly stated location?",
         "opts": [
             "Yes, at Sāvatthī for the first time",
             "No — it continues from AN 6.1's setting, as with the discourses between them",
             "Yes, at Kapilavatthu",
             "The location is left unspecified on purpose, unlike any other discourse"],
         "correct": 1,
         "expl": "A bare continuation, matching the whole run from AN 6.2 through 6.9."},
        {"q": "What does <em>samādhibala</em> mean?",
         "opts": [
             "The power of faith",
             "The power of immersion, steadiness of mind unmoved by distraction",
             "The power of wisdom",
             "The power of energy"],
         "correct": 1,
         "expl": "Samādhi, immersion, plus bala, power."},
    ],
    marginalia=[
        ("The five powers", [
            "<span class=\"pali\">saddhābala</span>faith",
            "<span class=\"pali\">vīriyabala</span>energy",
            "<span class=\"pali\">satibala</span>mindfulness",
            "<span class=\"pali\">samādhibala</span>immersion",
            "<span class=\"pali\">paññābala</span>wisdom",
        ]),
        ("One word changes", [
            "AN 6.3: <span class=\"pali\">-indriya</span>",
            "AN 6.4: <span class=\"pali\">-bala</span>",
            "same five capacities",
        ]),
        ("Governance vs. unshakeable", [
            "faculty: governs its domain",
            "power: unmoved by its",
            "own opposite",
        ]),
        ("Cross-references", [
            "AN 6.3 &middot; the faculty-version",
            "AN 5.1 &middot; the caution on similar-sounding formulas",
        ]),
    ],
    further=[
        '<a href="%s/an6.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.3.html">AN 6.3 &middot; Faculties</a> &mdash; previous, the identical five '
        "qualities under their indriya form.",
        '<a href="an-6.5.html">AN 6.5 &middot; The Thoroughbred (1st)</a> &mdash; next, opening a '
        "three-part simile of the fine royal horse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.5 — Paṭhamaājānīyasutta
# --------------------------------------------------------------------------- #
page(
    5, "Paṭhamaājānīya", "The Thoroughbred (1st)",
    meta_title="AN 6.5 — The Thoroughbred (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamaājānīyasutta, "
        "which compares a mendicant able to endure the six senses to a fine royal thoroughbred "
        "that is, above all, beautiful. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A two-part simile: a fine royal thoroughbred's six qualities, then the parallel "
                 "mendicant's six"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Horse-similes for spiritual endurance recur elsewhere in the "
                              "canon and its Northern counterparts; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short, vivid simile, the "
                       "first of a three-part set"),
    ],
    why=(
        "After four discourses built on lists and closing formulas, AN 6.5 turns to a simile: a "
        "royal thoroughbred horse, prized for enduring sights, sounds, smells, tastes, and "
        "touches without breaking stride, and prized further for one additional quality that, "
        "this discourse says, completes what makes it fit to serve a king. A mendicant is "
        "compared directly: enduring the six sense objects, including thoughts, without being "
        "shaken. This is the first of three near-identical discourses, each naming a different "
        "sixth quality for the horse to be excellent."),
    guide=[
        ("The teaching in one sentence", [
            "As a fine royal thoroughbred is valued for enduring sights, sounds, smells, tastes, "
            "and touches, and for being <em>beautiful</em>, so a mendicant worthy of offerings "
            "endures sights, sounds, smells, tastes, touches, and thoughts without being shaken."]),
        ("A simile built in two matching halves", [
            "The discourse states the horse&rsquo;s six qualities first, then restates the "
            "mendicant&rsquo;s six qualities in matching order &mdash; but not in a perfectly "
            "parallel count. The horse&rsquo;s six are five kinds of endurance plus beauty; the "
            "mendicant&rsquo;s six are endurance across all six sense doors, sight through mind, "
            "with no separate sixth quality named beside endurance itself. The simile compares "
            "structure, not a term-for-term match."]),
        ("Why a horse, and why beauty", [
            "The thoroughbred simile draws on a stock image found across the canon for a being "
            "of exceptional quality: swift, strong, well-formed, and steady under provocation. "
            "This first version singles out beauty (<em>vaṇṇasampanna</em>) as what elevates mere "
            "endurance into something &ldquo;fit to serve a king.&rdquo; The two discourses that "
            "follow keep the same structure and swap in strength, then speed, as that "
            "distinguishing sixth quality &mdash; suggesting the simile is less about horses in "
            "particular than about naming, one at a time, the further qualities that make sheer "
            "endurance count for something."]),
        ("A note on what 'beauty' likely signals here", [
            "Applied to a mendicant, the parallel to the horse&rsquo;s beauty is left unstated "
            "&mdash; the mendicant side of the simile lists only the six-fold endurance across "
            "the senses, without an explicit sixth &ldquo;beauty&rdquo; quality of its own. A "
            "reader should not force an exact match where the text does not supply one; the "
            "simile&rsquo;s force lies in the shared image of endurance under trial, not in a "
            "one-to-one correspondence of every term."]),
        ("Part of a set of three", [
            "AN 6.5, 6.6, and 6.7 share an identical opening and an identical mendicant-side "
            "conclusion, differing only in the horse&rsquo;s named sixth quality: beauty here, "
            "strength at AN 6.6, speed at AN 6.7. Read as a set, they suggest three distinct "
            "ways a fine horse &mdash; and by extension a fine mendicant &mdash; might be praised "
            "beyond bare endurance alone."]),
    ],
    terms=[
        ("assājānīya",
         "&ldquo;thoroughbred horse&rdquo; &mdash; literally a horse &ldquo;of good breed,&rdquo; "
         "the discourse&rsquo;s central image."),
        ("khama",
         "&ldquo;able to endure&rdquo; &mdash; the quality both horse and mendicant share, "
         "applied to sights, sounds, smells, tastes, touches, and (for the mendicant) thoughts."),
        ("vaṇṇasampanna",
         "&ldquo;endowed with beauty&rdquo; &mdash; the horse&rsquo;s distinguishing sixth "
         "quality in this first version of the simile."),
        ("rājāraha",
         "&ldquo;worthy of a king,&rdquo; &ldquo;fit to serve a king&rdquo; &mdash; the horse's "
         "praise, paralleling the mendicant's worthiness of offerings."),
        ("rañño aṅga",
         "&ldquo;a factor of kingship&rdquo; &mdash; what a horse with these six qualities is "
         "reckoned to be, one of the resources befitting a king's household."),
    ],
    text_intro=(
        "The discourse in full: the thoroughbred's six qualities, and the parallel mendicant. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The thoroughbred horse"),
        ("p", "&sect;1", "an6.5:1.1-2.3"),
        ("h3", "The parallel: a mendicant"),
        ("p", "&sect;2", "an6.5:3.1-3.4"),
    ],
    quiz=[
        {"q": "What six qualities does AN 6.5 give the fine royal thoroughbred?",
         "opts": [
             "Speed, strength, and four kinds of intelligence",
             "Enduring sights, sounds, smells, tastes, and touches, plus being beautiful",
             "Six different colors of coat",
             "Obedience to six separate commands"],
         "correct": 1,
         "expl": "Five kinds of endurance plus vaṇṇasampanna, beauty."},
        {"q": "What are the mendicant's six matching qualities?",
         "opts": [
             "The same five kinds of endurance plus a stated sixth quality of beauty",
             "Enduring sights, sounds, smells, tastes, touches, and ideas — no separate sixth "
             "quality is named",
             "Six unrelated ethical precepts",
             "The five faculties plus liberation"],
         "correct": 1,
         "expl": "The mendicant side lists endurance across all six sense doors, sight through "
                 "mind, without an explicit added 'beauty' term."},
        {"q": "What is the discourse's own point about matching horse and mendicant term for term?",
         "opts": [
             "Every term must correspond exactly",
             "The simile compares structure and image, not a strict one-to-one term match — the "
             "reading guide cautions against forcing an exact correspondence",
             "The horse and mendicant qualities are identical in every detail",
             "The text explicitly denies any relationship between horse and mendicant"],
         "correct": 1,
         "expl": "The guide notes the mendicant side supplies no explicit parallel to 'beauty.'"},
        {"q": "What distinguishes AN 6.5, 6.6, and 6.7 from one another?",
         "opts": [
             "They are set in three different locations",
             "Each names a different sixth quality for the horse — beauty, then strength, then speed",
             "They feature three different questioners",
             "They use three unrelated similes entirely"],
         "correct": 1,
         "expl": "An identical structure with one term swapped each time."},
        {"q": "What does <em>khama</em> mean in this discourse?",
         "opts": ["Beautiful", "Able to endure", "Fast", "Strong"],
         "correct": 1,
         "expl": "The shared quality of enduring sense contact without breaking."},
        {"q": "What does <em>rañño aṅga</em> mean?",
         "opts": [
             "A gift given to a king",
             "A factor of kingship — one of the resources befitting a king's household",
             "A royal decree",
             "A type of horse breed"],
         "correct": 1,
         "expl": "What a horse with all six qualities is reckoned to be."},
        {"q": "How many sense doors does the mendicant's endurance cover, compared to the horse's?",
         "opts": [
             "The same five as the horse",
             "Six — the horse's five plus the mind, since the mendicant also endures ideas/thoughts",
             "Only three",
             "The text does not specify"],
         "correct": 1,
         "expl": "The horse endures five sensory domains; the mendicant additionally endures "
                 "mental phenomena."},
        {"q": "What image does this simile draw on?",
         "opts": [
             "A well-tended garden",
             "A stock canonical image of a being of exceptional quality: swift, strong, "
             "well-formed, steady under provocation",
             "A merchant's scale",
             "A burning house"],
         "correct": 1,
         "expl": "The thoroughbred horse, a common figure for excellence under trial."},
        {"q": "Is AN 6.5 set at a newly stated location?",
         "opts": [
             "Yes, at a royal stable",
             "No — it continues from AN 6.1's setting, as with the discourses before it",
             "Yes, at Kapilavatthu",
             "Yes, at Rājagaha"],
         "correct": 1,
         "expl": "The bare continuation pattern holds through AN 6.9."},
        {"q": "What quality does the horse's sixth term name in this first version of the simile?",
         "opts": ["Strength", "Speed", "Beauty", "Obedience"],
         "correct": 2,
         "expl": "Vaṇṇasampanna — AN 6.6 will name strength, AN 6.7 speed."},
    ],
    marginalia=[
        ("The horse's six", [
            "endures sights, sounds,",
            "smells, tastes, touches",
            "+ <span class=\"pali\">vaṇṇasampanna</span>beauty",
        ]),
        ("The mendicant's six", [
            "endures sights, sounds,",
            "smells, tastes, touches,",
            "and ideas — no stated sixth",
        ]),
        ("A set of three", [
            "AN 6.5: beauty",
            "AN 6.6: strength",
            "AN 6.7: speed",
        ]),
        ("Cross-references", [
            "AN 6.6 &middot; next, strength",
            "AN 6.7 &middot; third, speed",
        ]),
    ],
    further=[
        '<a href="%s/an6.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.6.html">AN 6.6 &middot; The Thoroughbred (2nd)</a> &mdash; next, the same '
        "simile with strength in place of beauty.",
        '<a href="an-6.4.html">AN 6.4 &middot; Powers</a> &mdash; previous, closing the '
        "chapter&rsquo;s opening run of list-formulas.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.6 — Dutiyaājānīyasutta
# --------------------------------------------------------------------------- #
page(
    6, "Dutiyaājānīya", "The Thoroughbred (2nd)",
    meta_title="AN 6.6 — The Thoroughbred (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyaājānīyasutta, "
        "the second of three thoroughbred-horse similes, naming strength as the horse's "
        "distinguishing sixth quality. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The same two-part simile as AN 6.5, with strength in place of beauty as the "
                 "horse's sixth quality"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 6.5, horse-similes for endurance recur elsewhere in "
                              "the canon and its Northern counterparts; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the second of three "
                       "near-identical discourses"),
    ],
    why=(
        "AN 6.6 repeats AN 6.5&rsquo;s simile of the thoroughbred horse almost word for word, "
        "changing only the horse&rsquo;s named sixth quality: <em>balava</em>, strong, in place "
        "of <em>vaṇṇasampanna</em>, beautiful. The mendicant side of the comparison is untouched. "
        "Read on its own this discourse might seem a mere variant; read as the middle term of a "
        "three-part set, it shows the tradition building a small series out of one fixed "
        "structure and a single changing element."),
    guide=[
        ("The teaching in one sentence", [
            "As a fine royal thoroughbred is valued for enduring sights, sounds, smells, tastes, "
            "and touches, and for being <em>strong</em>, so a mendicant worthy of offerings "
            "endures sights, sounds, smells, tastes, touches, and thoughts without being shaken."]),
        ("What changed from AN 6.5, and what did not", [
            "Every clause of AN 6.6 matches AN 6.5&rsquo;s wording exactly except one word: "
            "where AN 6.5 said the horse <em>vaṇṇasampanno ca hoti</em>, is possessed of beauty, "
            "AN 6.6 says <em>balavā ca hoti</em>, is possessed of strength. The mendicant-side "
            "conclusion, listing endurance across all six senses, is identical in both."]),
        ("Strength as a distinct praise from beauty", [
            "Where beauty at AN 6.5 named an outward, visible mark of excellence, strength names "
            "a capacity &mdash; what the horse can do, not merely how it appears. Placed second "
            "in the set, this shifts the register of what makes bare endurance count for "
            "something: not only handsome bearing, but real power in reserve."]),
        ("Reading the three as a single teaching, not three separate ones", [
            "Because AN 6.5, 6.6, and 6.7 differ by a single word each, they are best read "
            "together rather than as three independent teachings. Together they name three "
            "qualities &mdash; beauty, strength, speed &mdash; that a fine horse, and by "
            "extension an exemplary mendicant, might display beyond bare endurance, without "
            "claiming any one of the three is more essential than the others."]),
        ("A structural note on this series", [
            "This kind of tight, near-repeating triad, differing by a single term, recurs "
            "elsewhere across the Aṅguttara wherever a simile or list has more than one natural "
            "variant worth stating in full rather than compressing. It is a different technique "
            "from the peyyāla &mdash; abbreviated-text &mdash; passages this series will meet "
            "later in the Sixes, which compress rather than restate."]),
    ],
    terms=[
        ("balavā",
         "&ldquo;strong,&rdquo; &ldquo;possessed of strength&rdquo; &mdash; the horse's "
         "distinguishing sixth quality in this second version of the simile."),
        ("assājānīya",
         "&ldquo;thoroughbred horse&rdquo; &mdash; the same central image as AN 6.5."),
        ("khama",
         "&ldquo;able to endure&rdquo; &mdash; the shared quality of horse and mendicant, "
         "unchanged from AN 6.5."),
        ("rājāraha",
         "&ldquo;worthy of a king,&rdquo; &ldquo;fit to serve a king&rdquo; &mdash; the horse's "
         "praise, unchanged from AN 6.5."),
        ("rañño aṅga",
         "&ldquo;a factor of kingship&rdquo; &mdash; what a horse with these six qualities is "
         "reckoned to be, unchanged from AN 6.5."),
    ],
    text_intro=(
        "The discourse in full: the thoroughbred's six qualities, now including strength, and "
        "the parallel mendicant. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The thoroughbred horse"),
        ("p", "&sect;1", "an6.6:1.1-1.4"),
        ("h3", "The parallel: a mendicant"),
        ("p", "&sect;2", "an6.6:2.1-2.4"),
    ],
    quiz=[
        {"q": "What single word changes between AN 6.5 and AN 6.6?",
         "opts": [
             "The setting changes from Sāvatthī to Kapilavatthu",
             "The horse's named sixth quality changes from beauty to strength",
             "The number of sense doors changes from five to six",
             "The speaker changes from the Buddha to a mendicant"],
         "correct": 1,
         "expl": "Vaṇṇasampanna, beauty, becomes balavā, strong — everything else matches AN 6.5."},
        {"q": "Does the mendicant-side conclusion change between AN 6.5 and AN 6.6?",
         "opts": [
             "Yes, it also adds a strength quality",
             "No — it remains the same six-fold endurance across sights, sounds, smells, tastes, "
             "touches, and ideas",
             "Yes, it drops one of the six sense doors",
             "Yes, a new closing formula is used"],
         "correct": 1,
         "expl": "Only the horse's named sixth quality changes; the mendicant side is unchanged."},
        {"q": "How does the guide characterize the difference between 'beauty' and 'strength' as "
              "praise?",
         "opts": [
             "They are treated as exact synonyms",
             "Beauty names an outward, visible mark; strength names a capacity — what the horse "
             "can do, not merely how it appears",
             "Strength is dismissed as a lesser quality than beauty",
             "The text explicitly ranks strength above beauty"],
         "correct": 1,
         "expl": "A shift in register from appearance to capacity."},
        {"q": "How should AN 6.5, 6.6, and 6.7 best be read, according to the guide?",
         "opts": [
             "As three unrelated, independent teachings",
             "Together, as three ways a fine horse — and mendicant — might be praised beyond "
             "bare endurance, with no one term claimed as most essential",
             "As a strict ranking from least to most important quality",
             "As later interpolations unrelated to the original text"],
         "correct": 1,
         "expl": "A tight triad differing by one word each, meant to be read as a set."},
        {"q": "What technique does this triad use, compared to the peyyāla (abbreviated-text) "
              "passages met later in the Sixes?",
         "opts": [
             "The same technique — both compress repeated material",
             "A different technique — this triad restates the material in full each time rather "
             "than compressing it",
             "Peyyāla passages always restate material in full",
             "There is no difference between the two techniques"],
         "correct": 1,
         "expl": "This is full restatement with one changed term, not compression."},
        {"q": "What does <em>balavā</em> mean?",
         "opts": ["Beautiful", "Strong, possessed of strength", "Fast", "Wise"],
         "correct": 1,
         "expl": "The horse's sixth quality at AN 6.6."},
        {"q": "Is AN 6.6 set at a newly stated location?",
         "opts": [
             "Yes, at a different monastery",
             "No — it continues from AN 6.1's setting",
             "Yes, among the Sakyans",
             "Yes, at Rājagaha"],
         "correct": 1,
         "expl": "The bare continuation pattern holds through AN 6.9."},
        {"q": "What quality will AN 6.7, the third of this set, name as the horse's sixth quality?",
         "opts": ["Beauty again", "Strength again", "Speed", "Obedience"],
         "correct": 2,
         "expl": "Completing the set: beauty, strength, speed."},
        {"q": "What remains identical across all three thoroughbred discourses?",
         "opts": [
             "Nothing — each is a wholly separate teaching",
             "The five-fold sensory endurance and the mendicant-side six-fold endurance formula",
             "Only the setting",
             "Only the speaker"],
         "correct": 1,
         "expl": "The shared structural core across AN 6.5, 6.6, and 6.7."},
        {"q": "What kind of image does the thoroughbred simile draw on?",
         "opts": [
             "A merchant weighing goods",
             "A being of exceptional quality, steady under provocation — a stock canonical figure",
             "A farmer plowing a field",
             "A physician treating illness"],
         "correct": 1,
         "expl": "As already established at AN 6.5."},
    ],
    marginalia=[
        ("One word changes", [
            "AN 6.5: <span class=\"pali\">vaṇṇasampanna</span>",
            "AN 6.6: <span class=\"pali\">balavā</span>strong",
            "rest of the text unchanged",
        ]),
        ("Appearance vs. capacity", [
            "beauty: how it appears",
            "strength: what it can do",
        ]),
        ("The set of three", [
            "AN 6.5: beauty",
            "AN 6.6: strength &larr; here",
            "AN 6.7: speed",
        ]),
        ("Cross-references", [
            "AN 6.5 &middot; previous, beauty",
            "AN 6.7 &middot; next, speed",
        ]),
    ],
    further=[
        '<a href="%s/an6.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.5.html">AN 6.5 &middot; The Thoroughbred (1st)</a> &mdash; previous, the '
        "same simile with beauty as the horse's sixth quality.",
        '<a href="an-6.7.html">AN 6.7 &middot; The Thoroughbred (3rd)</a> &mdash; next, '
        "completing the set with speed.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.7 — Tatiyaājānīyasutta
# --------------------------------------------------------------------------- #
page(
    7, "Tatiyaājānīya", "The Thoroughbred (3rd)",
    meta_title="AN 6.7 — The Thoroughbred (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Tatiyaājānīyasutta, "
        "the third and last of the thoroughbred-horse similes, naming speed as the horse's "
        "distinguishing sixth quality. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "The same two-part simile as AN 6.5 and AN 6.6, with speed in place of beauty "
                 "or strength as the horse's sixth quality"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 6.5 and AN 6.6, horse-similes for endurance recur "
                              "elsewhere in the canon and its Northern counterparts; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the last of three "
                       "near-identical discourses, closing the set"),
    ],
    why=(
        "AN 6.7 completes the triad begun at AN 6.5: the same thoroughbred simile, the same "
        "mendicant-side conclusion, with <em>javana</em>, speed, now standing where beauty and "
        "then strength stood before. With this discourse the set is finished &mdash; three "
        "qualities named, one each, over three short discourses &mdash; and the chapter turns "
        "next to a different kind of teaching: a pair of six-item lists, unsurpassable "
        "attainments and subjects for recollection."),
    guide=[
        ("The teaching in one sentence", [
            "As a fine royal thoroughbred is valued for enduring sights, sounds, smells, tastes, "
            "and touches, and for being <em>fast</em>, so a mendicant worthy of offerings "
            "endures sights, sounds, smells, tastes, touches, and thoughts without being shaken."]),
        ("The third and final term", [
            "Where AN 6.5 gave the horse <em>vaṇṇasampanna</em>, beauty, and AN 6.6 gave it "
            "<em>balavā</em>, strength, AN 6.7 gives it <em>javana</em>, speed. The mendicant-side "
            "conclusion is, as in the two discourses before it, unchanged: the same six-fold "
            "endurance, with no explicit added &ldquo;speed&rdquo; quality named on the "
            "mendicant's side any more than beauty or strength were."]),
        ("What the completed triad suggests", [
            "Taken as a finished set, AN 6.5&ndash;6.7 name beauty, strength, and speed as three "
            "distinct further marks of an excellent horse beyond bare endurance &mdash; three "
            "things a king's stable might separately prize. None is presented as ranking above "
            "the others; the discourse does not argue that speed matters more than strength, or "
            "strength more than beauty. The three are offered as parallel, coordinate virtues."]),
        ("Why the mendicant side never gets its own matching sixth term", [
            "Across all three discourses, the horse gains a distinguishing sixth quality that "
            "the mendicant side never explicitly mirrors with a parallel virtue of its own; the "
            "mendicant's six qualities are simply endurance repeated across all six sense doors, "
            "sight through mind. The simile's work is done by the shared image of endurance "
            "itself, not by insisting every praised quality of the horse must find a named "
            "counterpart in the mendicant."]),
        ("Closing this chapter's second unit", [
            "With AN 6.5&ndash;6.7 complete, the Āhuneyyavagga has now given two internal units: "
            "AN 6.1&ndash;6.4, four list-formulas closed by the worthiness refrain, and "
            "AN 6.5&ndash;6.7, three variations on one simile. The chapter's final three "
            "discourses, AN 6.8&ndash;6.10, return to lists &mdash; unsurpassable things, "
            "subjects for recollection, and their expansion &mdash; closing the chapter."]),
    ],
    terms=[
        ("javana",
         "&ldquo;speed,&rdquo; &ldquo;swiftness&rdquo; &mdash; the horse's distinguishing sixth "
         "quality in this third and final version of the simile."),
        ("assājānīya",
         "&ldquo;thoroughbred horse&rdquo; &mdash; the same central image as AN 6.5 and AN 6.6."),
        ("khama",
         "&ldquo;able to endure&rdquo; &mdash; the shared quality of horse and mendicant across "
         "all three discourses."),
        ("rājāraha",
         "&ldquo;worthy of a king,&rdquo; &ldquo;fit to serve a king&rdquo; &mdash; the horse's "
         "praise, unchanged across the triad."),
        ("rañño aṅga",
         "&ldquo;a factor of kingship&rdquo; &mdash; what a horse with these six qualities is "
         "reckoned to be, unchanged across the triad."),
    ],
    text_intro=(
        "The discourse in full: the thoroughbred's six qualities, now including speed, and the "
        "parallel mendicant, closing the three-part simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The thoroughbred horse"),
        ("p", "&sect;1", "an6.7:1.1-1.4"),
        ("h3", "The parallel: a mendicant"),
        ("p", "&sect;2", "an6.7:2.1-2.4"),
    ],
    quiz=[
        {"q": "What is the horse's distinguishing sixth quality in AN 6.7?",
         "opts": ["Beauty", "Strength", "Speed", "Obedience"],
         "correct": 2,
         "expl": "Javana, speed — completing the set after beauty (AN 6.5) and strength (AN 6.6)."},
        {"q": "Does the mendicant-side conclusion in AN 6.7 add a matching 'speed' quality?",
         "opts": [
             "Yes, a new sixth virtue of swiftness is named",
             "No — as with beauty and strength before it, the mendicant side has no explicit "
             "matching sixth term, only the six-fold sensory endurance",
             "Yes, but only implicitly through a simile of a running deer",
             "The text is ambiguous on this point"],
         "correct": 1,
         "expl": "The mendicant's six qualities remain the same across all three discourses."},
        {"q": "How does the guide characterize the relationship among beauty, strength, and speed "
              "across the three discourses?",
         "opts": [
             "Speed is presented as more important than the other two",
             "The three are offered as parallel, coordinate virtues, with none ranked above the "
             "others",
             "Beauty is dismissed as unimportant compared to strength and speed",
             "Only one of the three actually appears in the text"],
         "correct": 1,
         "expl": "No ranking is argued for; three separate marks of excellence beyond endurance."},
        {"q": "What two internal units does the guide identify within the Āhuneyyavagga so far?",
         "opts": [
             "There are no internal units — the chapter is a single continuous teaching",
             "AN 6.1–6.4, four list-formulas with the worthiness refrain, and AN 6.5–6.7, three "
             "variations on the thoroughbred simile",
             "AN 6.1–6.5 and AN 6.6–6.10",
             "Odd-numbered and even-numbered discourses"],
         "correct": 1,
         "expl": "Two distinct techniques used within one ten-discourse chapter."},
        {"q": "What comes next in the chapter, after the thoroughbred triad closes?",
         "opts": [
             "A dialogue with a deity",
             "AN 6.8–6.10: unsurpassable things, subjects for recollection, and their expansion",
             "The chapter ends at AN 6.7",
             "A repeat of the six sense-door formula from AN 6.1"],
         "correct": 1,
         "expl": "The chapter's final three discourses return to list-teachings."},
        {"q": "What does <em>javana</em> mean?",
         "opts": ["Strength", "Beauty", "Speed, swiftness", "Endurance"],
         "correct": 2,
         "expl": "The horse's sixth quality in this final version of the simile."},
        {"q": "Is AN 6.7 set at a newly stated location?",
         "opts": [
             "Yes, at a royal stable",
             "No — it continues from AN 6.1's setting, as with the discourses before it",
             "Yes, among the Sakyans",
             "Yes, at Rājagaha"],
         "correct": 1,
         "expl": "The bare continuation pattern holds through AN 6.9."},
        {"q": "How many sense doors does the mendicant's endurance cover in this simile?",
         "opts": ["Five", "Six — sight, sound, smell, taste, touch, and mental phenomena", "Four", "Three"],
         "correct": 1,
         "expl": "Consistent across all three thoroughbred discourses."},
        {"q": "What does the guide say about forcing a term-for-term match between horse and "
              "mendicant?",
         "opts": [
             "It is essential to the simile's meaning",
             "It should not be forced — the simile's force lies in the shared image of endurance, "
             "not a strict correspondence of every praised term",
             "The text explicitly supplies a matching mendicant term for each horse quality",
             "There is no relationship between horse and mendicant at all"],
         "correct": 1,
         "expl": "A caution repeated from AN 6.5's own reading guide."},
        {"q": "What kind of teaching device is used across AN 6.5, 6.6, and 6.7?",
         "opts": [
             "A peyyāla, abbreviated-text compression",
             "A near-identical structure restated in full three times, with a single term changed "
             "each time",
             "Three unrelated parables",
             "A single discourse split across three pages for length"],
         "correct": 1,
         "expl": "Full restatement rather than compression — distinct from the peyyāla technique "
                 "met later in the Sixes."},
    ],
    marginalia=[
        ("The completed triad", [
            "AN 6.5: beauty",
            "AN 6.6: strength",
            "AN 6.7: speed &larr; here",
        ]),
        ("Still unchanged", [
            "mendicant's six: endures",
            "sights, sounds, smells,",
            "tastes, touches, ideas",
        ]),
        ("Three coordinate virtues", [
            "none ranked above",
            "the others in the text",
        ]),
        ("Cross-references", [
            "AN 6.6 &middot; previous, strength",
            "AN 6.8 &middot; next, unsurpassable things",
        ]),
    ],
    further=[
        '<a href="%s/an6.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.6.html">AN 6.6 &middot; The Thoroughbred (2nd)</a> &mdash; previous, the '
        "same simile with strength as the horse's sixth quality.",
        '<a href="an-6.8.html">AN 6.8 &middot; Unsurpassable</a> &mdash; next, a fresh six-item '
        "list closing the chapter's opening triad of similes.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.8 — Anuttariyasutta
# --------------------------------------------------------------------------- #
page(
    8, "Anuttariya", "Unsurpassable",
    meta_title="AN 6.8 — Unsurpassable | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anuttariyasutta, a "
        "bare list of six unsurpassable things — seeing, listening, acquisition, training, "
        "service, and recollection. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of six items, named once, with no elaboration and no worthiness "
                 "formula attached"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Lists of unsurpassable attainments recur in related forms across "
                              "the Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, but each of the six "
                       "terms names a substantial category left entirely unexplained here"),
    ],
    why=(
        "After three discourses built on one simile, AN 6.8 returns to bare listing, in the "
        "style of AN 5.1 at the head of the previous nipāta: six things are named "
        "&ldquo;unsurpassable,&rdquo; <em>anuttariya</em>, with no worthiness formula and no "
        "explanation of any one of them. The list gives this discourse its own name, "
        "<em>Anuttariyasutta</em>, and stands as the bare headline for six categories that "
        "elsewhere in the canon receive much fuller treatment."),
    guide=[
        ("The teaching in one sentence", [
            "Six things are called unsurpassable: unsurpassed seeing, unsurpassed listening, "
            "unsurpassed acquisition, unsurpassed training, unsurpassed service, and "
            "unsurpassed recollection."]),
        ("A list, not an argument", [
            "As with AN 5.1's five powers of a trainee, this discourse states its six items and "
            "stops. No simile explains them, no story motivates them, and no closing worthiness "
            "formula is attached &mdash; a departure from every discourse so far in this chapter, "
            "each of which closed on the fourfold āhuneyya refrain or the horse-simile's "
            "parallel structure. AN 6.8 is simply a naming."]),
        ("What the six terms are pointing toward", [
            "Elsewhere in the canon, most prominently at MN 30, this same six-item "
            "&ldquo;unsurpassable&rdquo; list is unpacked at length: unsurpassed seeing as "
            "witnessing something worth witnessing, unsurpassed listening as hearing a teaching "
            "worth hearing, unsurpassed acquisition as gaining faith, unsurpassed training as "
            "training in ethics, immersion, and wisdom, unsurpassed service as attending on "
            "someone worth serving, and unsurpassed recollection as recollecting a worthwhile "
            "state of mind. None of that expansion is present in this short text; the list is "
            "given here as a headline only."]),
        ("Why a bare list, in this position", [
            "Placed eighth in a ten-discourse chapter, after four list-formulas and three "
            "similes, this brief unadorned list offers a moment of compression before the "
            "chapter's two final discourses, which pair a similarly bare list of recollection "
            "topics (AN 6.9) with its full expansion (AN 6.10) &mdash; a brief-then-detailed "
            "structure this series has already met once, at AN 5.1 and 5.2."]),
        ("A caution on reading &lsquo;unsurpassable&rsquo; too literally", [
            "The term <em>anuttariya</em> does not claim these six are the only good things in "
            "the world, only that each names the best possible version of its own kind: the best "
            "kind of seeing, the best kind of listening, and so on. A reader should take the "
            "list as marking six categories at their highest pitch, not as a closed inventory of "
            "everything worth valuing."]),
    ],
    terms=[
        ("anuttariya",
         "&ldquo;unsurpassable,&rdquo; &ldquo;supreme&rdquo; &mdash; the quality named of each "
         "of the six items, and the discourse's own title."),
        ("dassanānuttariya",
         "unsurpassed seeing &mdash; the first of the six, elsewhere expanded as witnessing "
         "something truly worth witnessing."),
        ("savanānuttariya",
         "unsurpassed listening &mdash; the second, elsewhere expanded as hearing a teaching "
         "truly worth hearing."),
        ("sikkhānuttariya",
         "unsurpassed training &mdash; the fourth, elsewhere expanded as training in ethics, "
         "immersion, and wisdom."),
        ("anussatānuttariya",
         "unsurpassed recollection &mdash; the sixth and last, linking this discourse forward to "
         "AN 6.9's own list of recollection topics."),
    ],
    text_intro=(
        "The discourse in full: the six unsurpassable things, named without elaboration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six unsurpassable things"),
        ("p", "&sect;1", "an6.8:1.1-1.4"),
    ],
    quiz=[
        {"q": "What six things does AN 6.8 name as unsurpassable?",
         "opts": [
             "Seeing, listening, acquisition, training, service, and recollection",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "The six sense doors",
             "Generosity, ethics, patience, energy, and wisdom"],
         "correct": 0,
         "expl": "Dassana, savana, lābha, sikkhā, pāricariyā, anussati — anuttariya."},
        {"q": "How does AN 6.8's form differ from every discourse before it in this chapter?",
         "opts": [
             "It is the longest discourse in the chapter so far",
             "It is a bare list with no worthiness formula and no simile, unlike AN 6.1–6.7",
             "It introduces a new speaker for the first time",
             "It repeats AN 6.1 word for word"],
         "correct": 1,
         "expl": "A departure from the āhuneyya refrain and the horse-simile structure."},
        {"q": "According to the guide, where is this same six-item list unpacked at length "
              "elsewhere in the canon?",
         "opts": [
             "It is never expanded anywhere else",
             "Most prominently at MN 30",
             "Only in the Chinese Āgamas, never in Pāli",
             "At AN 6.9, immediately following"],
         "correct": 1,
         "expl": "AN 6.8 gives only the headline; the fuller unpacking is elsewhere."},
        {"q": "What does the guide caution against when reading the term 'unsurpassable'?",
         "opts": [
             "Taking it too figuratively",
             "Reading it as a closed inventory of everything worth valuing, rather than the best "
             "version of each of six specific categories",
             "Applying it to mendicants rather than lay followers",
             "Translating it at all"],
         "correct": 1,
         "expl": "Anuttariya marks the best of its own kind, not an exhaustive list of all good "
                 "things."},
        {"q": "What structural pairing does the guide anticipate for AN 6.9 and AN 6.10?",
         "opts": [
             "Two unrelated, independent teachings",
             "A brief-then-detailed pair, similar to AN 5.1 and AN 5.2",
             "A direct contradiction between the two",
             "AN 6.10 will repeat AN 6.8, not AN 6.9"],
         "correct": 1,
         "expl": "AN 6.9 gives a bare list of recollection topics; AN 6.10 expands them in full."},
        {"q": "What does <em>dassanānuttariya</em> mean, and how is it elsewhere expanded?",
         "opts": [
             "Unsurpassed listening, expanded as hearing music",
             "Unsurpassed seeing, elsewhere expanded as witnessing something truly worth "
             "witnessing",
             "Unsurpassed training, expanded as physical exercise",
             "Unsurpassed service, expanded as almsgiving"],
         "correct": 1,
         "expl": "The first of the six unsurpassable things."},
        {"q": "Which of the six items links forward to AN 6.9's own subject matter?",
         "opts": [
             "Unsurpassed seeing",
             "Unsurpassed acquisition",
             "Unsurpassed recollection (anussatānuttariya)",
             "Unsurpassed service"],
         "correct": 2,
         "expl": "AN 6.9 opens its own list of six recollection topics immediately after."},
        {"q": "Is AN 6.8 set at a newly stated location?",
         "opts": [
             "Yes, at a different monastery",
             "No — it continues from AN 6.1's setting",
             "Yes, among the Sakyans",
             "Yes, at Rājagaha"],
         "correct": 1,
         "expl": "The bare continuation pattern holds through AN 6.9."},
        {"q": "How does the guide describe the position of AN 6.8 within the chapter's structure?",
         "opts": [
             "As a random insertion with no relation to what surrounds it",
             "As a moment of compression between the thoroughbred triad and the final "
             "brief-then-detailed pair of AN 6.9–6.10",
             "As the chapter's climax and final discourse",
             "As an exact repetition of AN 6.1"],
         "correct": 1,
         "expl": "Eighth of ten discourses, bridging two different earlier units."},
        {"q": "What does <em>sikkhānuttariya</em> name, per its elsewhere-given expansion?",
         "opts": [
             "Training in only physical discipline",
             "Training in ethics, immersion, and wisdom",
             "Training in scholarship alone",
             "Training in psychic powers"],
         "correct": 1,
         "expl": "The fourth of the six unsurpassable things, the threefold training."},
    ],
    marginalia=[
        ("The six unsurpassable", [
            "1. seeing",
            "2. listening",
            "3. acquisition",
            "4. training",
            "5. service",
            "6. recollection",
        ]),
        ("A bare list, no formula", [
            "unlike AN 6.1–6.7,",
            "no āhuneyya refrain",
            "attached here",
        ]),
        ("Expanded elsewhere", [
            "see MN 30 for the",
            "full unpacking of",
            "all six terms",
        ]),
        ("Cross-references", [
            "AN 5.1 &middot; a similar bare opening",
            "AN 6.9 &middot; next, recollection topics",
        ]),
    ],
    further=[
        '<a href="%s/an6.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.9.html">AN 6.9 &middot; Topics for Recollection</a> &mdash; next, a '
        "matching bare list, itself expanded immediately after at AN 6.10.",
        '<a href="an-6.7.html">AN 6.7 &middot; The Thoroughbred (3rd)</a> &mdash; previous, '
        "closing the chapter's simile triad.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.9 — Anussatiṭṭhānasutta
# --------------------------------------------------------------------------- #
page(
    9, "Anussatiṭṭhāna", "Topics for Recollection",
    meta_title="AN 6.9 — Topics for Recollection | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anussatiṭṭhānasutta, a "
        "bare list of six topics for recollection — the Buddha, the teaching, the Saṅgha, "
        "ethics, generosity, and the deities. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_CONT),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of six items, named once, with no elaboration &mdash; the "
                 "companion to AN 6.8 and the seed of AN 6.10's full expansion"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The six recollections (<em>ṣaḍanusmṛti</em>) recur widely across "
                              "the Chinese Āgamas and later Mahāyāna devotional practice; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and easy to state, "
                       "though each item names a practice developed at length elsewhere"),
    ],
    why=(
        "AN 6.9 names, in one bare list, what will become one of the most widely practiced "
        "meditation frameworks in the tradition: the six recollections &mdash; of the Buddha, "
        "the teaching, the Saṅgha, ethics, generosity, and the deities. Nothing here explains "
        "how to practice any of the six or what results from doing so; that work is left "
        "entirely to the very next discourse, AN 6.10, where Mahānāma the Sakyan asks the "
        "Buddha directly what a noble disciple frequently practices, and receives this same list "
        "unpacked at length."),
    guide=[
        ("The teaching in one sentence", [
            "There are six topics for recollection: recollection of the Buddha, the teaching, "
            "the Saṅgha, ethics, generosity, and the deities."]),
        ("A companion to AN 6.8, not a repetition of it", [
            "AN 6.9 shares its bare, unadorned form with AN 6.8 &mdash; six items, named once, "
            "no elaboration &mdash; but an entirely different content. Where AN 6.8's "
            "&ldquo;unsurpassable&rdquo; list named six pinnacle achievements, AN 6.9's list "
            "names six concrete objects of meditation, each one something a practitioner can "
            "actually sit down and recollect."]),
        ("Three refuges, plus three more", [
            "The first three items &mdash; the Buddha, the teaching, the Saṅgha &mdash; are the "
            "same three objects named in the going-for-refuge formula familiar from lay and "
            "monastic practice alike. The list then adds three further topics not part of the "
            "refuge formula: one's own ethical conduct, one's own generosity, and the deities "
            "&mdash; extending recollection from what one takes refuge in outward to one's own "
            "conduct and, finally, to exemplary beings said to have reached their state through "
            "qualities any listener can also cultivate."]),
        ("Why this list, and not AN 5.57, gets the full expansion", [
            "This series has already published an earlier page on &ldquo;subjects for regular "
            "reviewing&rdquo; (AN 5.57), a different five-item list concerning aging, illness, "
            "death, separation, and one's own deeds. That list and this one share only the "
            "general theme of deliberate recollection; they are not the same teaching under two "
            "names, and a reader should not conflate the two before reaching AN 6.10, which "
            "expands only the present six-item list."]),
        ("A deliberately incomplete page", [
            "As with AN 6.8, this page does not attempt to supply the explanation the source "
            "text withholds. The reading guide for AN 6.10, immediately following, is where each "
            "of these six recollections receives its full description &mdash; what the "
            "practitioner brings to mind, and what is said to follow from doing so."]),
    ],
    terms=[
        ("anussati",
         "&ldquo;recollection,&rdquo; &ldquo;calling to mind&rdquo; &mdash; the practice named "
         "six times over in this discourse."),
        ("buddhānussati",
         "recollection of the Buddha &mdash; the first of the six, expanded in full at AN 6.10."),
        ("dhammānussati",
         "recollection of the teaching &mdash; the second of the six."),
        ("saṅghānussati",
         "recollection of the Saṅgha &mdash; the third of the six, completing the three items "
         "shared with the going-for-refuge formula."),
        ("devatānussati",
         "recollection of the deities &mdash; the sixth and last, recollecting beings said to "
         "have reached their state through faith, ethics, learning, generosity, and wisdom."),
    ],
    text_intro=(
        "The discourse in full: the six topics for recollection, named without elaboration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six topics for recollection"),
        ("p", "&sect;1", "an6.9:1.1-1.4"),
    ],
    quiz=[
        {"q": "What six topics does AN 6.9 name for recollection?",
         "opts": [
             "The Buddha, the teaching, the Saṅgha, ethics, generosity, and the deities",
             "Aging, illness, death, separation, and one's own deeds",
             "Seeing, listening, acquisition, training, service, and recollection",
             "The five faculties plus liberation"],
         "correct": 0,
         "expl": "Buddhānussati, dhammānussati, saṅghānussati, sīlānussati, cāgānussati, "
                 "devatānussati."},
        {"q": "How does AN 6.9's form compare to AN 6.8's?",
         "opts": [
             "Entirely different — AN 6.9 is a long narrative",
             "The same bare, unadorned form — six items named once, no elaboration — but "
             "different content",
             "AN 6.9 repeats AN 6.8's exact six items",
             "AN 6.9 attaches the worthiness formula, unlike AN 6.8"],
         "correct": 1,
         "expl": "A shared structure, a different list."},
        {"q": "Which three of the six items match the going-for-refuge formula?",
         "opts": [
             "Ethics, generosity, and the deities",
             "The Buddha, the teaching, and the Saṅgha",
             "All six match the refuge formula",
             "None of the six relate to the refuges"],
         "correct": 1,
         "expl": "The first three items of this list are the three refuges."},
        {"q": "What does the guide say about AN 5.57, a previously published page, in relation "
              "to this discourse?",
         "opts": [
             "AN 5.57 is the same teaching under a different name and should be read as identical",
             "AN 5.57 is a different five-item list (aging, illness, death, separation, one's own "
             "deeds) sharing only the general theme of recollection — not to be conflated with "
             "this six-item list",
             "AN 5.57 directly expands this discourse's list",
             "AN 5.57 has no connection whatsoever to recollection"],
         "correct": 1,
         "expl": "A caution against treating two different recollection-themed lists as the same "
                 "teaching."},
        {"q": "Where is this six-item list expanded in full?",
         "opts": [
             "It is never expanded anywhere in this series",
             "At AN 6.10, immediately following, in response to a question from Mahānāma the "
             "Sakyan",
             "At AN 5.57",
             "At AN 6.8"],
         "correct": 1,
         "expl": "AN 6.9 states the bare list; AN 6.10 unpacks each item at length."},
        {"q": "What three additional topics does this list add beyond the three refuges?",
         "opts": [
             "Wisdom, immersion, and mindfulness",
             "One's own ethical conduct, one's own generosity, and the deities",
             "Aging, illness, and death",
             "Seeing, listening, and service"],
         "correct": 1,
         "expl": "Sīlānussati, cāgānussati, and devatānussati extend the list beyond the refuges."},
        {"q": "What does <em>devatānussati</em> recollect, according to its later expansion at "
              "AN 6.10?",
         "opts": [
             "The physical appearance of various gods",
             "Beings said to have reached their state through faith, ethics, learning, "
             "generosity, and wisdom — qualities the listener can also cultivate",
             "The names of every deity in the Pāli canon",
             "A warning against believing in deities at all"],
         "correct": 1,
         "expl": "Recollection extends from what one reveres to qualities one can develop oneself."},
        {"q": "Is AN 6.9 set at a newly stated location?",
         "opts": [
             "Yes, at Kapilavatthu",
             "No — it continues from AN 6.1's setting",
             "Yes, at a different monastery",
             "Yes, at Rājagaha"],
         "correct": 1,
         "expl": "The last discourse in the chapter to use the bare continuation pattern — AN "
                 "6.10 states its own setting."},
        {"q": "What does this page deliberately leave unexplained?",
         "opts": [
             "Nothing — the page gives full detail on all six recollections",
             "How to practice any of the six, and what follows from doing so — left to AN 6.10",
             "The Pāli terms for each recollection",
             "The order of the six items"],
         "correct": 1,
         "expl": "As with AN 6.8, the full unpacking is left to the discourse that follows."},
        {"q": "What does <em>anussati</em> mean?",
         "opts": ["Meditation on emptiness", "Recollection, calling to mind", "Physical training", "Formal debate"],
         "correct": 1,
         "expl": "The practice named six times over across this discourse's list."},
    ],
    marginalia=[
        ("The six recollections", [
            "1. the Buddha",
            "2. the teaching",
            "3. the Saṅgha",
            "4. ethics",
            "5. generosity",
            "6. the deities",
        ]),
        ("Three refuges, three more", [
            "1&ndash;3: the refuge triad",
            "4&ndash;6: conduct, giving,",
            "exemplary beings",
        ]),
        ("Not AN 5.57", [
            "AN 5.57: aging, illness,",
            "death, separation, deeds",
            "&mdash; a different list",
        ]),
        ("Cross-references", [
            "AN 6.8 &middot; previous, unsurpassable things",
            "AN 6.10 &middot; next, the full expansion",
        ]),
    ],
    further=[
        '<a href="%s/an6.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.10.html">AN 6.10 &middot; With Mahānāma</a> &mdash; next, where each of '
        "these six recollections is unpacked in full.",
        '<a href="an-5.57.html">AN 5.57 &middot; Subjects for Regular Reviewing</a> &mdash; a '
        "different, earlier recollection-themed list, not to be conflated with this one.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.10 — Mahānāmasutta
# --------------------------------------------------------------------------- #
page(
    10, "Mahānāma", "With Mahānāma",
    meta_title="AN 6.10 — With Mahānāma | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahānāmasutta, closing "
        "the Āhuneyyavagga with Mahānāma the Sakyan's question and the Buddha's full expansion "
        "of the six recollections. From Ru-Yi Meditation Center."),
    vagga=VAGGA_1,
    glance=[
        ("Setting", "The land of the Sakyans, near Kapilavatthu, in the Banyan Tree Monastery"),
        ("Speakers", "The Buddha, replying to a question from Mahānāma the Sakyan"),
        ("Form", "A question and answer, followed by six matching expansions of the recollection "
                 "topics named in brief at AN 6.9"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "The six recollections (<em>ṣaḍanusmṛti</em>) recur widely across "
                              "the Chinese Āgamas and later Mahāyāna devotional and meditative "
                              "practice; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; long by this chapter's "
                       "standards, but built from six clearly repeated units"),
    ],
    why=(
        "AN 6.9 named six recollections and stopped. AN 6.10 is where they are unpacked, closing "
        "the Āhuneyyavagga with its only named interlocutor: Mahānāma the Sakyan, who asks what "
        "kind of meditation a noble disciple &ldquo;who has reached the fruit and understood the "
        "instructions&rdquo; frequently practices. The Buddha answers with all six recollections "
        "in turn, each following an identical pattern &mdash; recollect, find the mind free of "
        "greed, hate, and delusion, find inspiration and joy, and (for the first and last) trace "
        "the sequence through rapture, tranquility, bliss, and immersion. It is the longest "
        "discourse in the chapter so far, and the first since AN 6.1 to name its setting fresh."),
    guide=[
        ("The teaching in one sentence", [
            "A noble disciple who has already reached the fruit of practice frequently recollects "
            "the Buddha, the teaching, the Saṅgha, their own ethics, their own generosity, and "
            "the deities &mdash; and each recollection is said to clear the mind of greed, hate, "
            "and delusion and ground it, unswerving, in what is recollected."]),
        ("Who Mahānāma is, and why his question matters", [
            "Mahānāma the Sakyan appears elsewhere in the canon as a senior lay follower, a "
            "relative of the Buddha, sometimes shown worrying over how to practice amid the "
            "demands of household life. His question here is practical, not philosophical: not "
            "&ldquo;what is the goal,&rdquo; but what someone who has already made real progress "
            "&mdash; &ldquo;reached the fruit and understood the instructions&rdquo; &mdash; "
            "actually does, day to day. The answer he receives is a description of an ongoing "
            "practice, not a one-time attainment."]),
        ("The shared shape of the first recollection, in detail", [
            "The Buddha's account of recollecting the Buddha runs: call to mind a fixed formula "
            "of nine epithets (perfected, fully awakened, accomplished in knowledge and conduct, "
            "and so on); find that while doing so the mind is not full of greed, hate, and "
            "delusion; find the mind unswerving, based on the Realized One; find inspiration and "
            "joy connected with the teaching; and from that joy, rapture, tranquility, bliss, and "
            "finally immersion in samādhi arise in sequence. This five-step chain &mdash; joy, "
            "rapture, tranquility, bliss, immersion &mdash; is a standard description elsewhere "
            "in the canon of how calm and immersion develop from any wholesome mental state, not "
            "a mechanism unique to recollecting the Buddha."]),
        ("Four middle recollections, compressed by the source itself", [
            "The translation elides much of the repeated wording for the teaching, the Saṅgha, "
            "ethics, and generosity with an ellipsis, since each follows the identical "
            "&ldquo;mind not full of greed, hate, and delusion&rdquo; opening already spelled out "
            "in full for the Buddha. Only the specific formula recollected changes: the "
            "teaching's own four-part description (well explained, apparent in the present life, "
            "inviting inspection, and so on), the Saṅgha's own description (practicing well, "
            "worthy of offerings &mdash; echoing this very chapter's opening formula), one's own "
            "intact and unmarred ethical conduct, and one's own freedom from stinginess."]),
        ("The deities, and a needed clarification", [
            "The sixth recollection is not devotion to gods for their own sake. Its content is a "
            "reasoning: various classes of deities were reborn there because of their faith, "
            "ethics, learning, generosity, and wisdom; the practitioner recollects having &ldquo;"
            "the same kind of faith, ethics, learning, generosity, and wisdom&rdquo; already "
            "present in themselves. The deities function here as evidence that these five "
            "qualities lead somewhere, not as objects of petition or worship."]),
    ],
    terms=[
        ("khīṇāsavo",
         "not used here directly, but the target Mahānāma asks about &mdash; a disciple who has "
         "reached the fruit (<em>āgataphala</em>) and understood the instructions "
         "(<em>viññātasāsana</em>)."),
        ("iti pi so bhagavā",
         "&ldquo;that Blessed One is&hellip;&rdquo; &mdash; the opening formula of the "
         "Buddha-recollection, introducing the nine-epithet description recited here in full."),
        ("avecca-ppasāda",
         "not named directly in this discourse but the technical term elsewhere for the "
         "confirmed confidence this recollection is said to produce &mdash; unswerving faith "
         "based on direct experience, not belief alone."),
        ("pīti",
         "&ldquo;rapture&rdquo; &mdash; the third link in the five-step chain from joy to "
         "immersion, arising once the mind is inspired and joyful."),
        ("samādhi",
         "&ldquo;immersion,&rdquo; unification of mind &mdash; the final link in the chain, "
         "reached once the body has grown tranquil and the mind blissful."),
    ],
    text_intro=(
        "The discourse in full: Mahānāma's question, and the Buddha's expansion of the six "
        "recollections named at AN 6.9. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Kapilavatthu"),
        ("p", "&sect;1", "an6.10:1.1-1.3"),
        ("h3", "Recollection of the Buddha"),
        ("p", "&sect;2", "an6.10:2.1-2.9"),
        ("h3", "Recollection of the teaching"),
        ("p", "&sect;3", "an6.10:3.1-3.8"),
        ("h3", "Recollection of the Saṅgha"),
        ("p", "&sect;4", "an6.10:4.1-4.8"),
        ("h3", "Recollection of ethics"),
        ("p", "&sect;5", "an6.10:5.1-5.7"),
        ("h3", "Recollection of generosity"),
        ("p", "&sect;6", "an6.10:6.1-6.9"),
        ("h3", "Recollection of the deities"),
        ("p", "&sect;7", "an6.10:7.1-7.13"),
        ("h3", "The conclusion"),
        ("p", "&sect;8", "an6.10:8.1"),
    ],
    quiz=[
        {"q": "Who asks the Buddha the question that opens AN 6.10?",
         "opts": [
             "Ānanda", "Mahānāma the Sakyan", "Sāriputta", "A group of unnamed mendicants"],
         "correct": 1,
         "expl": "The chapter's only named interlocutor, and its first newly-stated setting "
                 "since AN 6.1."},
        {"q": "What does Mahānāma actually ask?",
         "opts": [
             "What is the ultimate goal of the path",
             "What kind of meditation a noble disciple who has reached the fruit and understood "
             "the instructions frequently practices",
             "How to become a mendicant",
             "Whether lay followers can attain awakening"],
         "correct": 1,
         "expl": "A practical question about an ongoing practice, not the goal itself."},
        {"q": "What five-step chain does the Buddha describe following each recollection (in "
              "full for the first and last)?",
         "opts": [
             "Faith, effort, mindfulness, immersion, wisdom",
             "Joy, rapture, tranquility, bliss, and immersion in samādhi",
             "Seeing, hearing, smelling, tasting, touching",
             "Generosity, ethics, patience, energy, wisdom"],
         "correct": 1,
         "expl": "A standard sequence elsewhere in the canon describing how calm develops from "
                 "any wholesome mental state."},
        {"q": "How does the source text handle the middle four recollections (teaching, Saṅgha, "
              "ethics, generosity)?",
         "opts": [
             "Each is given in exactly the same full detail as the Buddha-recollection",
             "Much of the repeated wording is elided with an ellipsis, since the opening pattern "
             "is already spelled out in full for the Buddha",
             "They are omitted from the discourse entirely",
             "They are combined into a single recollection"],
         "correct": 1,
         "expl": "Only the specific recollected content changes; the shared 'mind not full of "
                 "greed, hate, delusion' opening is elided after being stated once."},
        {"q": "What does the recollection of the Saṅgha's formula echo from earlier in this "
              "chapter?",
         "opts": [
             "The thoroughbred simile from AN 6.5-6.7",
             "The worthiness formula from AN 6.1 — worthy of offerings, worthy of hospitality, "
             "and so on",
             "The six superhuman knowledges from AN 6.2",
             "Nothing — it is unrelated to anything earlier in the chapter"],
         "correct": 1,
         "expl": "The Saṅgha is described as worthy of offerings, worthy of hospitality — the "
                 "exact fourfold formula that opened the chapter."},
        {"q": "What, according to the guide, is the actual content of the sixth recollection, of "
              "the deities?",
         "opts": [
             "Devotion to gods as objects of petition and worship",
             "A reasoning that deities were reborn there through faith, ethics, learning, "
             "generosity, and wisdom — qualities the practitioner recollects already having "
             "themselves",
             "A warning against believing in any deities",
             "A description of the physical realms where deities live"],
         "correct": 1,
         "expl": "The deities function as evidence these five qualities lead somewhere, not as "
                 "objects of worship."},
        {"q": "What is significant about AN 6.10's setting, compared to the discourses before it "
              "in this chapter?",
         "opts": [
             "It is the only discourse in the chapter with no stated setting at all",
             "It is the first discourse since AN 6.1 to state a fresh setting — the land of the "
             "Sakyans, near Kapilavatthu",
             "It repeats the exact same setting as AN 6.1",
             "Its setting is left deliberately ambiguous"],
         "correct": 1,
         "expl": "AN 6.2 through 6.9 all continued from AN 6.1's setting without restating it."},
        {"q": "How does AN 6.10 relate structurally to AN 6.9?",
         "opts": [
             "They are unrelated in content",
             "AN 6.10 expands, item by item, the same six recollections AN 6.9 named in brief",
             "AN 6.10 contradicts AN 6.9's list",
             "AN 6.10 replaces AN 6.9's list with a different one"],
         "correct": 1,
         "expl": "A brief-then-detailed pair, as this series already met once at AN 5.1 and 5.2."},
        {"q": "Who is Mahānāma, based on how he appears elsewhere in the canon?",
         "opts": [
             "A newly ordained mendicant",
             "A senior lay follower and relative of the Buddha, sometimes shown navigating the "
             "demands of household life",
             "A wandering ascetic hostile to the Buddha's teaching",
             "A king ruling over Kapilavatthu"],
         "correct": 1,
         "expl": "His practical question fits a lay practitioner's concerns, not a mendicant's."},
        {"q": "What does the nine-epithet formula for the Buddha include, as recollected here?",
         "opts": [
             "Only the single word 'awakened'",
             "A string of epithets including perfected, fully awakened, and accomplished in "
             "knowledge and conduct",
             "A physical description of the Buddha's appearance",
             "A list of the Buddha's past lives"],
         "correct": 1,
         "expl": "The standard nine-fold recollection-of-the-Buddha formula, recited here in full."},
    ],
    marginalia=[
        ("The six recollections, expanded", [
            "1. the Buddha (full)",
            "2. the teaching",
            "3. the Saṅgha",
            "4. ethics",
            "5. generosity",
            "6. the deities (full)",
        ]),
        ("The five-step chain", [
            "joy &rarr; rapture &rarr;",
            "tranquility &rarr; bliss &rarr;",
            "immersion",
        ]),
        ("Mahānāma's question", [
            "not ‘what is the goal’",
            "but ‘what does someone",
            "who has arrived do daily’",
        ]),
        ("Cross-references", [
            "AN 6.9 &middot; previous, the bare list",
            "AN 6.1 &middot; the Saṅgha formula echoed here",
        ]),
    ],
    further=[
        '<a href="%s/an6.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.9.html">AN 6.9 &middot; Topics for Recollection</a> &mdash; previous, the '
        "bare list this discourse expands.",
        '<a href="an-6.1.html">AN 6.1 &middot; Worthy of Offerings (1st)</a> &mdash; the '
        "chapter's opening, whose worthiness formula recurs in the Saṅgha recollection here.",
    ],
)
