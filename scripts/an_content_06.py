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


# --------------------------------------------------------------------------- #
# Chapter 2 — Sāraṇīyavagga (AN 6.11–20)
# --------------------------------------------------------------------------- #
VAGGA_2 = "<em>Sāraṇīyavagga</em> &mdash; the second chapter of the Sixes"
SETTING_NONE = "None stated in the source"


# --------------------------------------------------------------------------- #
# AN 6.11 — Paṭhamasāraṇīyasutta
# --------------------------------------------------------------------------- #
page(
    11, "Paṭhamasāraṇīya", "Warm-hearted (1st)",
    vagga=VAGGA_2,
    meta_title="AN 6.11 — Warm-hearted (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamasāraṇīyasutta, "
        "opening the Sixes' second chapter with the six qualities that build warmth and cohesion "
        "in a spiritual community. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of six qualities, each closed with &lsquo;this is a warm-hearted "
                 "quality&rsquo;"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "This six-item list of communal virtues recurs at MN 48 and "
                              "elsewhere across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short, practical list about "
                       "communal life rather than solitary practice"),
    ],
    why=(
        "The Sixes' second chapter opens on a different register from the first: not "
        "attainments or similes, but the ordinary texture of living well among other "
        "practitioners. Six qualities are named <em>sāraṇīya</em>, warm-hearted or "
        "&ldquo;conducive to affection&rdquo; &mdash; kindness in body, speech, and mind toward "
        "one&rsquo;s spiritual companions, sharing material goods without holding back, and "
        "living by shared ethics and shared view. Nothing here concerns solitary meditation; "
        "everything concerns how a community of practitioners actually holds together."),
    guide=[
        ("The teaching in one sentence", [
            "Six things build warmth and belonging among spiritual companions: bodily kindness, "
            "verbal kindness, and mental kindness, both openly and privately; sharing material "
            "goods without holding anything back; living by shared ethical precepts; and living "
            "by a shared, liberating view."]),
        ("Three kindnesses, in every register", [
            "The first three items form a matched set &mdash; kindness of body, speech, and "
            "mind &mdash; each specified as holding &ldquo;both in public and in private,&rdquo; "
            "<em>āvi ceva raho ca</em>. The repetition of this phrase across all three items "
            "insists that warmth toward companions is not a performance for others to see; it "
            "must hold when no one is watching as much as when everyone is."]),
        ("A community's economy: sharing to the alms-bowl itself", [
            "The fourth item is startlingly concrete: sharing without reservation even "
            "&ldquo;the food placed in the alms-bowl.&rdquo; For a mendicant whose entire "
            "material life is a bowl of gathered food, this names the smallest and most "
            "immediate possible act of non-possessiveness, not an abstract principle about "
            "generosity in general."]),
        ("Ethics and view: the pair that closes the list", [
            "The fifth and sixth items shift from interpersonal conduct to shared standards: "
            "living by the same ethical precepts as one's companions, and holding the same "
            "&ldquo;noble and emancipating&rdquo; view that leads to the ending of suffering. A "
            "community held together only by mutual kindness, without a shared ethical and "
            "doctrinal foundation, is not quite what this list describes; both registers are "
            "named as necessary."]),
        ("A companion discourse follows immediately", [
            "AN 6.12, next, restates this identical list of six with one addition: an explicit "
            "closing formula naming what each quality produces &mdash; fondness, respect, "
            "inclusion, harmony, unity, freedom from dispute. Read together, the two discourses "
            "give first the bare list, then its social payoff, in the same brief-then-detailed "
            "pattern this series has already met at AN 5.1/5.2 and AN 6.9/6.10."]),
    ],
    terms=[
        ("sāraṇīya",
         "&ldquo;warm-hearted,&rdquo; &ldquo;conducive to affection&rdquo; &mdash; the quality "
         "named of each of the six items, and this chapter's own title."),
        ("mettaṁ kāyakammaṁ",
         "&ldquo;loving-kindness in bodily action&rdquo; &mdash; the first of the six, physical "
         "conduct rooted in <em>mettā</em>."),
        ("sabrahmacārī",
         "&ldquo;spiritual companion,&rdquo; &ldquo;fellow practitioner of the holy life&rdquo; "
         "&mdash; the community these six qualities are directed toward."),
        ("āvi ceva raho ca",
         "&ldquo;both openly and privately&rdquo; &mdash; the phrase repeated across the first "
         "three items, insisting warmth must hold whether or not one is observed."),
        ("diṭṭhi",
         "&ldquo;view&rdquo; &mdash; the sixth item, a shared understanding described as "
         "&ldquo;noble and emancipating,&rdquo; leading its holder to the ending of suffering."),
    ],
    text_intro=(
        "The discourse in full: the six warm-hearted qualities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six warm-hearted qualities"),
        ("p", "&sect;1", "an6.11:1.1-7.1"),
    ],
    quiz=[
        {"q": "What six qualities does AN 6.11 name as sāraṇīya, warm-hearted?",
         "opts": [
             "Bodily, verbal, and mental kindness; sharing material goods; shared ethics; and "
             "shared view",
             "The five faculties plus liberation",
             "Seeing, listening, acquisition, training, service, recollection",
             "Six kinds of meditative absorption"],
         "correct": 0,
         "expl": "Three kindnesses, communal sharing, and shared ethics and view."},
        {"q": "What phrase is repeated across the first three items (bodily, verbal, mental "
              "kindness)?",
         "opts": [
             "'For the ending of defilements'",
             "'Both in public and in private' (āvi ceva raho ca)",
             "'Worthy of offerings'",
             "'Neither happy nor sad'"],
         "correct": 1,
         "expl": "Insisting that warmth must hold whether or not one is observed."},
        {"q": "How concrete is the fourth item, about sharing material goods?",
         "opts": [
             "It speaks only in the abstract about generosity in general",
             "It specifies sharing even the food placed in the alms-bowl itself",
             "It applies only to money, not to food",
             "It is left undefined"],
         "correct": 1,
         "expl": "The smallest, most immediate possible act of non-possessiveness for a "
                 "mendicant."},
        {"q": "What do the fifth and sixth items add beyond the first four?",
         "opts": [
             "Nothing — they simply repeat the earlier items",
             "A shift from interpersonal conduct to shared standards: common ethical precepts and "
             "a shared, liberating view",
             "A requirement to live in physical isolation",
             "A rule against speaking to laypeople"],
         "correct": 1,
         "expl": "Both a communal-conduct register and a shared-standards register are named as "
                 "necessary."},
        {"q": "What does <em>sabrahmacārī</em> mean?",
         "opts": [
             "A senior teacher", "A spiritual companion, a fellow practitioner", "An enemy of "
             "the teaching", "A lay donor"],
         "correct": 1,
         "expl": "The community these six qualities of warmth are directed toward."},
        {"q": "How does AN 6.12, the next discourse, relate to AN 6.11?",
         "opts": [
             "It contradicts AN 6.11's list",
             "It restates the identical six-item list, adding an explicit closing formula naming "
             "what each quality produces",
             "It replaces the list with an entirely different set of six qualities",
             "It is unrelated in content"],
         "correct": 1,
         "expl": "A brief-then-detailed pair, as this series has already met more than once."},
        {"q": "What broader pattern does the AN 6.11/6.12 pairing match, according to the guide?",
         "opts": [
             "It is unprecedented in this series",
             "The same brief-then-detailed structure already seen at AN 5.1/5.2 and AN 6.9/6.10",
             "It matches only the thoroughbred simile at AN 6.5-6.7",
             "It matches the peyyāla compression technique"],
         "correct": 1,
         "expl": "A recurring compositional device across this whole series."},
        {"q": "Is a setting stated for AN 6.11?",
         "opts": [
             "Yes, at Sāvatthī",
             "No — none is stated in the source",
             "Yes, at Kapilavatthu",
             "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare list with no scene-setting clause, opening the chapter's second vagga."},
        {"q": "What does the sixth item's 'view' lead to, according to the text?",
         "opts": [
             "Rebirth as a deity",
             "The complete ending of suffering",
             "Material prosperity",
             "Fame among other mendicants"],
         "correct": 1,
         "expl": "Described as noble and emancipating, delivering its holder to the end of "
                 "suffering."},
        {"q": "What register does this discourse concern, compared to most of chapter 1?",
         "opts": [
             "Solitary meditative attainment, like chapter 1's opening discourses",
             "The ordinary, practical texture of living well within a community of practitioners",
             "Cosmology and the realms of rebirth",
             "Debate technique with wanderers of other sects"],
         "correct": 1,
         "expl": "A shift from attainments and similes to communal life."},
    ],
    marginalia=[
        ("The six warm-hearted qualities", [
            "1&ndash;3. bodily, verbal,",
            "mental kindness",
            "4. sharing goods",
            "5. shared ethics",
            "6. shared view",
        ]),
        ("Open and private", [
            "<span class=\"pali\">āvi ceva raho ca</span>",
            "repeated three times —",
            "warmth unwatched, too",
        ]),
        ("Down to the alms-bowl", [
            "sharing extends to",
            "the very food gathered",
            "that morning",
        ]),
        ("Cross-references", [
            "AN 6.12 &middot; next, the same list expanded",
        ]),
    ],
    further=[
        '<a href="%s/an6.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.12.html">AN 6.12 &middot; Warm-hearted (2nd)</a> &mdash; next, the same '
        "six qualities with their social effects made explicit.",
        '<a href="an-6.10.html">AN 6.10 &middot; With Mahānāma</a> &mdash; previous, closing the '
        "chapter's first unit.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.12 — Dutiyasāraṇīyasutta
# --------------------------------------------------------------------------- #
page(
    12, "Dutiyasāraṇīya", "Warm-hearted (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 6.12 — Warm-hearted (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyasāraṇīyasutta, "
        "restating the six warm-hearted qualities of AN 6.11 with their social effect made "
        "explicit: fondness, harmony, unity, and freedom from dispute. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same six-item list as AN 6.11, each item now closed with an explicit "
                 "statement of its social effect"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 6.11, this list recurs at MN 48 and elsewhere across "
                              "the Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a direct expansion of the "
                       "previous discourse"),
    ],
    why=(
        "AN 6.11 named six warm-hearted qualities and stopped. AN 6.12 states the identical six "
        "&mdash; the wording of each item is unchanged &mdash; but now closes each with a named "
        "consequence: the quality &ldquo;makes for fondness and respect, conducing to inclusion, "
        "harmony, and unity, without dispute.&rdquo; Nothing new is added to what the six "
        "qualities are; what changes is an explicit statement of what they are said to be "
        "for."),
    guide=[
        ("The teaching in one sentence", [
            "The same six warm-hearted qualities named at AN 6.11 &mdash; kindness in body, "
            "speech, and mind; sharing material goods; shared ethics; shared view &mdash; each "
            "&ldquo;make for fondness and respect, conducing to inclusion, harmony, and unity, "
            "without dispute.&rdquo;"]),
        ("What the closing formula adds", [
            "AN 6.11 left the payoff of these six qualities implicit, trusting the reader to "
            "infer that kindness and sharing build community. AN 6.12 states it outright, in a "
            "five-part formula &mdash; fondness, respect, inclusion, harmony, unity &mdash; that "
            "recurs elsewhere in the canon (notably at MN 48, the Kosambī discourse on "
            "communal harmony) as a fixed description of what holds a monastic community "
            "together without internal conflict."]),
        ("Naming outcomes changes the emphasis, not the content", [
            "It would be a misreading to treat AN 6.12 as a separate teaching from AN 6.11. "
            "Every one of the six qualities and its wording matches exactly; only the closing "
            "clause is added. The pairing works like AN 6.3 and 6.4's faculties-and-powers pair: "
            "one discourse states the material, the next restates it under a slightly different "
            "framing, without claiming to add new content."]),
        ("Harmony as a stated goal, not an accident", [
            "By naming &ldquo;without dispute&rdquo; as a direct consequence of these six "
            "qualities, the discourse implies the reverse as well, though it does not say so "
            "directly: a community lacking these qualities is at risk of the fondness, "
            "inclusion, and harmony they produce breaking down. The text stops short of drawing "
            "that inference explicitly, and this guide does not extend it further than the "
            "text itself warrants."]),
        ("Closing the chapter's opening pair", [
            "With AN 6.11 and 6.12 complete, the chapter turns from communal virtues to a "
            "different subject entirely: the six <em>nissāraṇīyā dhātuyo</em>, elements of "
            "escape, at AN 6.13 &mdash; a return to the solitary meditative register of "
            "chapter 1, now naming what liberates a mind from six specific afflictions."]),
    ],
    terms=[
        ("pemanīya",
         "&ldquo;conducive to fondness&rdquo; &mdash; the first outcome named for each of the "
         "six qualities."),
        ("garuka",
         "&ldquo;conducive to respect&rdquo; &mdash; the second outcome, paired with fondness "
         "throughout the formula."),
        ("saṅgahāya",
         "&ldquo;for inclusion,&rdquo; &ldquo;for being drawn together&rdquo; &mdash; the third "
         "outcome named."),
        ("sāmaggiyā",
         "&ldquo;for unity,&rdquo; &ldquo;for concord&rdquo; &mdash; the fifth outcome, closing "
         "the formula alongside freedom from dispute."),
        ("sāraṇīya",
         "&ldquo;warm-hearted&rdquo; &mdash; unchanged from AN 6.11, still naming each of the "
         "six qualities themselves."),
    ],
    text_intro=(
        "The discourse in full: the six warm-hearted qualities, now with their social effect "
        "stated explicitly. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six warm-hearted qualities, and their effect"),
        ("p", "&sect;1", "an6.12:1.1-7.1"),
    ],
    quiz=[
        {"q": "What does AN 6.12 add to AN 6.11's list of six qualities?",
         "opts": [
             "A seventh new quality",
             "An explicit closing formula naming each quality's social effect: fondness, "
             "respect, inclusion, harmony, and unity, without dispute",
             "A warning against practicing them incorrectly",
             "A restriction limiting them to senior mendicants only"],
         "correct": 1,
         "expl": "The six qualities themselves are worded identically to AN 6.11."},
        {"q": "Where else does this same five-part outcome formula recur in the canon, according "
              "to the guide?",
         "opts": [
             "Nowhere else — it is unique to this discourse",
             "Notably at MN 48, the Kosambī discourse on communal harmony",
             "Only in the Vinaya",
             "Only in later commentarial literature"],
         "correct": 1,
         "expl": "A fixed description recurring elsewhere for what holds a community together."},
        {"q": "How does the guide characterize the relationship between AN 6.11 and AN 6.12?",
         "opts": [
             "Two entirely unrelated teachings",
             "The same six qualities and wording, with an outcome clause added — not new "
             "content, a shift in framing, like the AN 6.3/6.4 faculties-and-powers pairing",
             "AN 6.12 contradicts AN 6.11",
             "AN 6.12 doubles the number of qualities named"],
         "correct": 1,
         "expl": "A restatement under a different framing, not a separate teaching."},
        {"q": "What inference does the guide explicitly decline to draw from the 'without "
              "dispute' outcome?",
         "opts": [
             "That the six qualities are unimportant",
             "That a community lacking these qualities risks the reverse — breakdown of "
             "fondness, inclusion, and harmony — though the text itself does not state this "
             "directly",
             "That mendicants who dispute should be expelled",
             "That the formula applies only to lay communities"],
         "correct": 1,
         "expl": "The guide is careful not to extend the text's claims further than stated."},
        {"q": "What comes next in the chapter, after this opening pair on communal virtues?",
         "opts": [
             "A return to the thoroughbred simile",
             "AN 6.13, the six elements of escape — a different subject, back in a solitary "
             "meditative register",
             "The chapter ends here",
             "A repeat of the worthiness formula"],
         "correct": 1,
         "expl": "A shift from communal life to what liberates the mind from specific afflictions."},
        {"q": "What does <em>sāmaggiyā</em> mean?",
         "opts": ["Fondness", "Respect", "Unity, concord", "Dispute"],
         "correct": 2,
         "expl": "The fifth outcome named in the closing formula, paired with freedom from "
                 "dispute."},
        {"q": "Is a setting stated for AN 6.12?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Kapilavatthu", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "Matching AN 6.11, no scene-setting clause is given."},
        {"q": "What does <em>pemanīya</em> mean?",
         "opts": ["Conducive to dispute", "Conducive to fondness", "Conducive to isolation", "Conducive to fear"],
         "correct": 1,
         "expl": "The first of the five named outcomes."},
        {"q": "Do the wordings of the six qualities themselves differ between AN 6.11 and AN "
              "6.12?",
         "opts": [
             "Yes, substantially",
             "No — they are worded identically; only the closing outcome clause is new",
             "Only the fourth quality differs",
             "AN 6.12 drops two of the six qualities"],
         "correct": 1,
         "expl": "A direct restatement, not a revision."},
        {"q": "What broader pattern does this pairing exemplify, according to the guide?",
         "opts": [
             "A unique, unprecedented structure in this series",
             "A discourse stating material plainly, followed by a companion restating it under a "
             "different framing — as with AN 6.3's faculties and AN 6.4's powers",
             "The peyyāla compression technique",
             "A contradiction requiring resolution"],
         "correct": 1,
         "expl": "A recurring compositional device in this collection."},
    ],
    marginalia=[
        ("The added outcomes", [
            "fondness &middot; respect",
            "inclusion &middot; harmony",
            "unity &middot; no dispute",
        ]),
        ("Same six qualities", [
            "wording unchanged",
            "from AN 6.11 —",
            "only the outcome is new",
        ]),
        ("A recurring pattern", [
            "AN 6.3/6.4: faculties,",
            "then powers — same",
            "restate-and-reframe move",
        ]),
        ("Cross-references", [
            "AN 6.11 &middot; previous, the bare list",
            "AN 6.13 &middot; next, elements of escape",
        ]),
    ],
    further=[
        '<a href="%s/an6.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.11.html">AN 6.11 &middot; Warm-hearted (1st)</a> &mdash; previous, the '
        "same six qualities without the outcome clause.",
        '<a href="an-6.13.html">AN 6.13 &middot; Elements of Escape</a> &mdash; next, a new '
        "six-item list on liberation from specific afflictions.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.13 — Nissāraṇīyasutta
# --------------------------------------------------------------------------- #
page(
    13, "Nissāraṇīya", "Elements of Escape",
    vagga=VAGGA_2,
    meta_title="AN 6.13 — Elements of Escape | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nissāraṇīyasutta, which "
        "insists that love, compassion, rejoicing, equanimity, the signless release, and the "
        "uprooting of self-conceit are each already complete escapes from their opposing "
        "affliction. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Six parallel scenarios: a mendicant's mistaken claim, a scripted correction, "
                 "and a stated principle of escape"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The four <em>brahmavihāra</em> and the two further liberations "
                              "named here recur widely in related forms across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a technical discourse "
                       "combining six distinct meditative liberations with a distinctive "
                       "argumentative form"),
    ],
    why=(
        "AN 6.13 has an unusual shape: six times, it scripts a mendicant's mistaken report "
        "&mdash; &ldquo;I&rsquo;ve developed this liberation fully, yet somehow the opposing "
        "affliction still occupies my mind&rdquo; &mdash; and six times gives the same scripted "
        "correction: that claim cannot be true, because it misrepresents the Buddha, and it is "
        "impossible for the affliction to remain once its stated escape has genuinely been "
        "developed. The discourse is less a description of six liberations than an argument "
        "about what &ldquo;fully developed&rdquo; must mean, if these liberations are what the "
        "canon says they are."),
    guide=[
        ("The teaching in one sentence", [
            "Six specific meditative liberations &mdash; love, compassion, rejoicing, "
            "equanimity, the signless release, and the uprooting of the conceit &ldquo;I "
            "am&rdquo; &mdash; are each declared the complete escape from one named affliction; "
            "if the affliction remains, the discourse insists, the liberation was not actually "
            "developed as claimed."]),
        ("Six pairs, one form repeated", [
            "Love (<em>mettā</em>) is escape from ill will. Compassion (<em>karuṇā</em>) is "
            "escape from the thought of harming. Rejoicing (<em>muditā</em>) is escape from "
            "discontent. Equanimity (<em>upekkhā</em>) is escape from desire. The signless "
            "release of the heart is escape from the mind's following after signs. And the "
            "uprooting of the conceit &ldquo;I am&rdquo; is escape from the dart of doubt and "
            "indecision. The first four are the standard <em>brahmavihāra</em>, the four "
            "&ldquo;divine abodes&rdquo;; the last two extend the list into subtler territory, "
            "concerning perception itself and the root sense of self."]),
        ("An argument about logical necessity, not just description", [
            "What makes this discourse distinctive is its form: rather than simply listing six "
            "liberations, it dramatizes a mendicant claiming success while still reporting the "
            "very affliction the practice is meant to end, then has that claim flatly refused. "
            "The refusal is not framed as encouragement to try harder; it is framed as a "
            "conceptual impossibility &mdash; &ldquo;it's impossible, it cannot happen&rdquo; "
            "&mdash; treating the relationship between cause and effect here as necessary, not "
            "merely probable."]),
        ("A caution this reading guide should itself observe", [
            "It would be easy to read this discourse as license to doubt one's own progress at "
            "the first sign of a lingering unwholesome thought. The text does not say that; its "
            "target is a mendicant's declarative claim of complete and settled development, not "
            "the ordinary, gradual experience of a quality growing stronger over time. A single "
            "arising of ill will does not, on this discourse's own terms, prove that love has "
            "not been cultivated at all &mdash; only that it has not yet reached the described "
            "completion."]),
        ("Why 'elements of escape', not simply 'liberations'", [
            "The term <em>nissāraṇīyā dhātuyo</em>, elements of escape, frames each of the six "
            "not as a state to rest in for its own sake but as a specific way out of a specific "
            "trap. Read this way, the four brahmavihāra function here less as devotional or "
            "purely ethical cultivations and more as precise antidotes, each aimed at one named "
            "obstruction."]),
    ],
    terms=[
        ("nissāraṇīyā dhātuyo",
         "&ldquo;elements of escape&rdquo; &mdash; the discourse's own title, framing each "
         "liberation as a way out of a specific affliction."),
        ("mettā cetovimutti",
         "&ldquo;the heart's release by love&rdquo; &mdash; the first of the six, declared the "
         "escape from ill will."),
        ("karuṇā cetovimutti",
         "&ldquo;the heart's release by compassion&rdquo; &mdash; the second, declared the "
         "escape from the thought of harming."),
        ("animittā cetovimutti",
         "&ldquo;the signless release of the heart&rdquo; &mdash; the fifth, declared the escape "
         "from the mind's following after signs."),
        ("asmimāna",
         "&ldquo;the conceit &lsquo;I am&rsquo;&rdquo; &mdash; whose uprooting is declared, "
         "sixth, the escape from the dart of doubt and indecision."),
    ],
    text_intro=(
        "The discourse in full: six scripted claims and corrections, naming each liberation as "
        "the escape from one affliction. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Love, as escape from ill will"),
        ("p", "&sect;1", "an6.13:1.1-1.9"),
        ("h3", "Compassion, as escape from the thought of harming"),
        ("p", "&sect;2", "an6.13:2.1-2.7"),
        ("h3", "Rejoicing, as escape from discontent"),
        ("p", "&sect;3", "an6.13:3.1-3.7"),
        ("h3", "Equanimity, as escape from desire"),
        ("p", "&sect;4", "an6.13:4.1-4.7"),
        ("h3", "The signless release, as escape from following signs"),
        ("p", "&sect;5", "an6.13:5.1-5.7"),
        ("h3", "Uprooting the conceit &lsquo;I am&rsquo;, as escape from doubt"),
        ("p", "&sect;6", "an6.13:6.1-7.1"),
    ],
    quiz=[
        {"q": "What is the discourse's scripted response when a mendicant claims to have fully "
              "developed love, yet reports ill will still occupying their mind?",
         "opts": [
             "That they should try a different meditation object",
             "That the claim is flatly rejected as impossible — genuine development of love "
             "cannot coexist with remaining ill will",
             "That some ill will is normal and acceptable",
             "That they should ask a senior mendicant for advice"],
         "correct": 1,
         "expl": "'It's impossible, reverend, it cannot happen' — a claim of logical necessity, "
                 "not mere encouragement."},
        {"q": "What are the first four of the six elements of escape?",
         "opts": [
             "The five faculties plus one power",
             "Love, compassion, rejoicing, and equanimity — the four brahmavihāra",
             "Faith, energy, mindfulness, and immersion",
             "Seeing, hearing, smelling, and tasting"],
         "correct": 1,
         "expl": "The standard four 'divine abodes', each paired with a specific affliction here."},
        {"q": "What are the fifth and sixth elements, extending beyond the four brahmavihāra?",
         "opts": [
             "Two more brahmavihāra not usually counted",
             "The signless release of the heart, and the uprooting of the conceit 'I am'",
             "Recollection of the Buddha and the Saṅgha",
             "The five faculties and five powers"],
         "correct": 1,
         "expl": "Extending the list into subtler territory concerning perception and the root "
                 "sense of self."},
        {"q": "According to the guide, what should this discourse NOT be read as licensing?",
         "opts": [
             "Practicing the four brahmavihāra at all",
             "Doubting one's own gradual progress at the first sign of a lingering unwholesome "
             "thought — the text targets a declarative claim of complete development, not "
             "ordinary gradual growth",
             "Ever claiming any spiritual attainment",
             "Teaching these liberations to others"],
         "correct": 1,
         "expl": "A single arising of ill will does not, on the text's own terms, prove love has "
                 "not been cultivated at all."},
        {"q": "What does the term <em>nissāraṇīyā dhātuyo</em>, 'elements of escape', frame each "
              "liberation as?",
         "opts": [
             "A state to rest in for its own sake, with no further purpose",
             "A precise antidote aimed at one named obstruction, a specific way out of a "
             "specific trap",
             "A purely devotional practice unrelated to liberation",
             "An optional supplement to the main path"],
         "correct": 1,
         "expl": "Framing the brahmavihāra here as targeted antidotes, not open-ended cultivations."},
        {"q": "What does compassion (karuṇā) serve as the escape from, per this discourse?",
         "opts": ["Discontent", "Desire", "The thought of harming", "Doubt and indecision"],
         "correct": 2,
         "expl": "The second of the six pairs."},
        {"q": "What is distinctive about this discourse's argumentative form, compared to a "
              "simple list?",
         "opts": [
             "It uses only similes, no direct statements",
             "It dramatizes a mistaken claim and a scripted refutation six times, treating the "
             "relationship between liberation and affliction as a logical necessity",
             "It is written entirely in verse",
             "It features a debate between two named mendicants"],
         "correct": 1,
         "expl": "Not mere description, but an argument about what 'fully developed' must mean."},
        {"q": "What is the sixth affliction named, and what escapes it?",
         "opts": [
             "Ill will, escaped by love",
             "The dart of doubt and indecision, escaped by uprooting the conceit 'I am'",
             "Desire, escaped by equanimity",
             "Discontent, escaped by rejoicing"],
         "correct": 1,
         "expl": "The final pair, extending past the four brahmavihāra and the signless release."},
        {"q": "Is a setting stated for AN 6.13?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Kapilavatthu", "Yes, among the Kosalans"],
         "correct": 1,
         "expl": "Matching AN 6.11 and 6.12, no scene-setting clause is given."},
        {"q": "What does the discourse say happens to a mendicant who makes such a mistaken "
              "claim, according to the scripted correction?",
         "opts": [
             "Nothing — the claim is simply accepted",
             "They are told the claim misrepresents the Buddha, and misrepresentation of the "
             "Buddha is not good",
             "They are expelled from the community",
             "They are praised for their honesty"],
         "correct": 1,
         "expl": "The correction frames the false claim as a misrepresentation of what the "
                 "Buddha actually taught, not merely a personal error."},
    ],
    marginalia=[
        ("The six escapes", [
            "love &rarr; ill will",
            "compassion &rarr; harming",
            "rejoicing &rarr; discontent",
            "equanimity &rarr; desire",
            "signless &rarr; signs",
            "no-self &rarr; doubt",
        ]),
        ("The scripted form", [
            "claim of full development",
            "+ lingering affliction",
            "= impossible, refused",
        ]),
        ("Not license to doubt", [
            "targets a declared claim,",
            "not ordinary gradual",
            "growth in practice",
        ]),
        ("Cross-references", [
            "AN 6.12 &middot; previous, communal warmth",
            "AN 6.14 &middot; next, a good death",
        ]),
    ],
    further=[
        '<a href="%s/an6.13/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.14.html">AN 6.14 &middot; A Good Death</a> &mdash; next, Sāriputta on what '
        "makes a mendicant's death good or otherwise.",
        '<a href="an-6.11.html">AN 6.11 &middot; Warm-hearted (1st)</a> &mdash; earlier in this '
        "chapter, a different register of six qualities.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.14 — Bhaddakasutta
# --------------------------------------------------------------------------- #
page(
    14, "Bhaddaka", "A Good Death",
    vagga=VAGGA_2,
    meta_title="AN 6.14 — A Good Death | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bhaddakasutta, in "
        "which Sāriputta names six things — work, talk, sleep, company, closeness, and "
        "proliferation — that determine whether a mendicant dies well. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Sāriputta, addressing the mendicants"),
        ("Form", "Two matched formulas &mdash; how life is lived so as not to have a good death, "
                 "and so as to have one &mdash; closed with four verse lines"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The theme of a death free of regret through non-attachment "
                              "recurs in related forms across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the central term, "
                       "<em>papañca</em>, carries real philosophical weight and resists a single "
                       "English word"),
    ],
    why=(
        "AN 6.14 is spoken by Sāriputta, not the Buddha &mdash; the first discourse in this "
        "chapter with a named speaker. His subject is blunt: what determines whether a "
        "mendicant has a &ldquo;good death,&rdquo; <em>bhaddaka maraṇa</em>. His answer turns on "
        "a single Pāli term, <em>papañca</em>, usually rendered &ldquo;proliferation&rdquo; "
        "&mdash; the mind's tendency to elaborate, embellish, and multiply itself around whatever "
        "it engages with. A mendicant who relishes six things, culminating in this "
        "proliferation, does not die well; one who does not relish them does."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who relishes work, talk, sleep, company, closeness, and proliferation "
            "does not have a good death; one who does not relish these six things does."]),
        ("Six items building toward one culmination", [
            "The list moves from concrete activities to something more abstract: work "
            "(<em>kamma</em>), talk (<em>bhassa</em>), sleep (<em>niddā</em>), company "
            "(<em>saṅgaṇikā</em>), closeness (<em>saṁsagga</em>), and finally "
            "<em>papañca</em>, proliferation. The first five are recognizable distractions from "
            "meditative life; the sixth names something subtler happening within the mind "
            "itself, and the discourse's own closing verse singles it out as the decisive term, "
            "not merely the sixth item in a list."]),
        ("What 'proliferation' names", [
            "<em>Papañca</em> is one of the canon's harder technical terms to render in "
            "English. It names the mind's tendency, once a perception has arisen, to spin "
            "outward into elaboration &mdash; associations, conceptual complications, and the "
            "sense of a self standing at the center of it all. Elsewhere in the canon (notably "
            "MN 18) it is explicitly linked to how ordinary perception generates the very "
            "concepts a person then becomes entangled in and fights over. Here, it is simply "
            "named as the last and most consequential of six things worth not relishing."]),
        ("Two labels for two ways of living", [
            "The discourse gives each way of living its own name: a mendicant who relishes "
            "these six is called one &ldquo;who enjoys substantial reality "
            "(<em>sakkāya</em>),&rdquo; who has not given it up &ldquo;to rightly make an end of "
            "suffering&rdquo;; one who does not relish them is called one &ldquo;who delights in "
            "extinguishment,&rdquo; who has given up substantial reality for that same end. "
            "<em>Sakkāya</em>, usually translated &ldquo;identity&rdquo; or "
            "&ldquo;substantial reality,&rdquo; is the same term at the root of "
            "<em>sakkāyadiṭṭhi</em>, identity view, one of the fetters binding beings to "
            "repeated existence."]),
        ("A death that is 'good' in a specific, technical sense", [
            "The discourse is not offering general advice about a peaceful passing in the "
            "ordinary sense. &ldquo;Good death&rdquo; here is inseparable from what has or has "
            "not been given up during life; it names whether one dies still entangled in "
            "proliferation and identity, or dies having already let them go. The closing verse "
            "makes this explicit, calling extinguishment &ldquo;the supreme sanctuary from the "
            "yoke,&rdquo; not a description of a serene final moment for its own sake."]),
    ],
    terms=[
        ("bhaddaka maraṇa",
         "&ldquo;a good death&rdquo; &mdash; the discourse's own title and subject, defined "
         "entirely in terms of what has been relinquished during life."),
        ("papañca",
         "&ldquo;proliferation&rdquo; &mdash; the mind's tendency to elaborate and multiply "
         "around what it perceives; the sixth and culminating item in this discourse's list."),
        ("sakkāya",
         "&ldquo;substantial reality,&rdquo; &ldquo;identity&rdquo; &mdash; what one who "
         "relishes the six listed things is said to enjoy and not give up."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; what one who does not relish the six things is "
         "said to delight in instead, named in the closing verse as the supreme sanctuary."),
        ("yogakkhema",
         "&ldquo;sanctuary from the yoke,&rdquo; &ldquo;security from bondage&rdquo; &mdash; the "
         "closing verse's description of what proliferation, given up, makes possible."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta on what makes a mendicant's death good or otherwise, "
        "closing in verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta addresses the mendicants"),
        ("p", "&sect;1", "an6.14:1.1-1.4"),
        ("h3", "Living so as not to have a good death"),
        ("p", "&sect;2", "an6.14:2.1-3.4"),
        ("h3", "Living so as to have a good death"),
        ("p", "&sect;3", "an6.14:4.1-5.4"),
        ("h3", "The closing verses"),
        ("p", "&sect;4", "an6.14:6.1-7.4"),
    ],
    quiz=[
        {"q": "Who speaks AN 6.14?",
         "opts": ["The Buddha", "Sāriputta, addressing the mendicants", "Mahānāma the Sakyan", "Ānanda"],
         "correct": 1,
         "expl": "The first discourse in this chapter with a named speaker other than the "
                 "Buddha."},
        {"q": "What six things does a mendicant who does not have a good death relish?",
         "opts": [
             "The six sense doors",
             "Work, talk, sleep, company, closeness, and proliferation",
             "The five faculties and one power",
             "Seeing, listening, acquisition, training, service, recollection"],
         "correct": 1,
         "expl": "Kamma, bhassa, niddā, saṅgaṇikā, saṁsagga, and papañca."},
        {"q": "What does the guide say about the sixth item, papañca, compared to the first five?",
         "opts": [
             "It is the least important of the six",
             "The closing verse singles it out as the decisive term, not merely the last item in "
             "a list — naming something subtler happening within the mind itself",
             "It is identical in meaning to 'sleep'",
             "It only applies to lay followers"],
         "correct": 1,
         "expl": "The first five are recognizable distractions; papañca names the mind's own "
                 "elaborating tendency."},
        {"q": "How does the guide describe what 'papañca' names?",
         "opts": [
             "Physical exhaustion from overwork",
             "The mind's tendency, once a perception arises, to spin outward into elaboration, "
             "association, and a sense of self at the center of it all",
             "A formal debate technique",
             "A type of unwholesome speech only"],
         "correct": 1,
         "expl": "Linked elsewhere in the canon (MN 18) to how ordinary perception generates the "
                 "concepts a person becomes entangled in."},
        {"q": "What is a mendicant who relishes these six things called?",
         "opts": [
             "One who delights in extinguishment",
             "One who enjoys substantial reality (sakkāya), who has not given it up to end "
             "suffering",
             "A stream-enterer",
             "A fully awakened Buddha"],
         "correct": 1,
         "expl": "Contrasted with one who does not relish them, called one who delights in "
                 "extinguishment."},
        {"q": "What does the guide clarify about the sense of 'good death' used here?",
         "opts": [
             "It means dying peacefully in the ordinary sense, regardless of one's practice",
             "It is inseparable from what has or has not been given up during life — whether one "
             "dies entangled in proliferation and identity, or having already let them go",
             "It refers only to the physical manner of death",
             "It has no relation to spiritual practice at all"],
         "correct": 1,
         "expl": "The closing verse calls extinguishment 'the supreme sanctuary from the yoke,' "
                 "not a description of a serene final moment alone."},
        {"q": "What does <em>sakkāya</em> relate to elsewhere in the canon?",
         "opts": [
             "It is unrelated to any other canonical term",
             "It is the root term in sakkāyadiṭṭhi, identity view, one of the fetters binding "
             "beings to repeated existence",
             "It refers only to physical possessions",
             "It names a type of meditative absorption"],
         "correct": 1,
         "expl": "A term with real technical weight beyond this single discourse."},
        {"q": "Is a setting stated for AN 6.14?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "Sāriputta 'addresses the mendicants' with no location given."},
        {"q": "What does <em>yogakkhema</em> mean?",
         "opts": [
             "A type of formal debate",
             "Sanctuary or security from the yoke — bondage",
             "A meditative posture",
             "A ceremonial offering"],
         "correct": 1,
         "expl": "The closing verse's term for what giving up proliferation makes possible."},
        {"q": "How does AN 6.15, the next discourse, relate to AN 6.14?",
         "opts": [
             "It is entirely unrelated in theme",
             "It restates a very similar teaching using the image of a 'bed one must lie in', "
             "framed around dying free of or tormented by regret",
             "It contradicts AN 6.14's teaching",
             "It is spoken by a different figure with no connection to Sāriputta's teaching here"],
         "correct": 1,
         "expl": "A closely related companion discourse, also on relishing versus not relishing "
                 "the same six things."},
    ],
    marginalia=[
        ("The six things", [
            "work &middot; talk &middot; sleep",
            "company &middot; closeness",
            "<span class=\"pali\">papañca</span>proliferation",
        ]),
        ("Two labels", [
            "relishes them: enjoys",
            "<span class=\"pali\">sakkāya</span>, substantial reality",
            "doesn't: delights in nibbāna",
        ]),
        ("A technical death", [
            "not a peaceful passing",
            "in the ordinary sense —",
            "defined by what's given up",
        ]),
        ("Cross-references", [
            "AN 6.13 &middot; previous, elements of escape",
            "AN 6.15 &middot; next, a close companion",
        ]),
    ],
    further=[
        '<a href="%s/an6.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.15.html">AN 6.15 &middot; Regret</a> &mdash; next, the same teaching '
        "recast around the image of the bed one must lie in.",
        '<a href="an-6.13.html">AN 6.13 &middot; Elements of Escape</a> &mdash; previous, a '
        "different discourse on liberation from affliction.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.15 — Anutappiyasutta
# --------------------------------------------------------------------------- #
page(
    15, "Anutappiya", "Regret",
    vagga=VAGGA_2,
    # an-6.16.html is an already-published page, not part of this module's
    # PAGES; chain() would otherwise skip straight from 6.15 to 6.17. Set the
    # hand-off explicitly here and mirror it with prev= on AN 6.17's page(),
    # matching the mid-run old-page splice used for AN 4.13.
    next=("an-6.16.html", "AN 6.16 &middot; Nakula&rsquo;s Father"),
    meta_title="AN 6.15 — Regret | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anutappiyasutta, "
        "Sāriputta's close companion to AN 6.14, recasting the same teaching around the image "
        "of the bed one must lie in. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Sāriputta, addressing the mendicants"),
        ("Form", "The same two matched formulas as AN 6.14, framed with the proverb-like image "
                 "of &lsquo;as you make your bed, so you must lie in it&rsquo;"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "As with AN 6.14, this theme recurs in related forms across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a direct companion to AN "
                       "6.14, sharing its central term <em>papañca</em>"),
    ],
    why=(
        "AN 6.15 restates AN 6.14 almost exactly &mdash; the same six things, the same two "
        "outcomes, the same closing verses &mdash; wrapped in a different opening image: "
        "&ldquo;as a mendicant makes their bed, so they must lie in it.&rdquo; Where AN 6.14 "
        "asked whether death is good or not, AN 6.15 asks whether it comes with regret or "
        "without. The two questions turn out, in this pairing, to be the same question asked "
        "twice."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who relishes work, talk, sleep, company, closeness, and proliferation "
            "makes a bed they must lie in, dying tormented by regret; one who does not relish "
            "these six things dies free of regret."]),
        ("A proverb doing the work of an argument", [
            "&ldquo;As you make your bed, so you must lie in it&rdquo; is a piece of ordinary "
            "proverbial wisdom, not a specialized Buddhist formula &mdash; its force depends on "
            "being instantly recognizable. Placed at the head of this discourse, it reframes "
            "AN 6.14's abstract terms (substantial reality, extinguishment) as something more "
            "immediate: the plain, almost folk-wisdom observation that how one lives determines "
            "how one ends up, without needing technical vocabulary to make the point land."]),
        ("What changes from AN 6.14, and what does not", [
            "Every one of the six items, both closing labels (&ldquo;enjoys substantial "
            "reality&rdquo; and &ldquo;delights in extinguishment&rdquo;), and all four lines of "
            "closing verse are shared word for word with AN 6.14. Only the frame differs: "
            "&ldquo;good death&rdquo; becomes &ldquo;free of regret,&rdquo; and the discourse "
            "opens on the bed-image rather than announcing its topic directly."]),
        ("Regret as the felt texture of an unexamined life", [
            "Where &ldquo;good death&rdquo; names a technical, almost clinical distinction "
            "&mdash; has substantial reality been given up or not &mdash; &ldquo;regret&rdquo; "
            "names how that same distinction is actually experienced by the person living, and "
            "dying, through it. The pairing suggests these are not two different consequences "
            "of relishing proliferation, but one consequence described twice: once from the "
            "outside, in terms of what has or has not been relinquished, and once from within, "
            "in terms of how it feels."]),
        ("Why the canon keeps two such close discourses", [
            "As with the thoroughbred triad at AN 6.5&ndash;6.7, restating near-identical "
            "material under a different frame is itself a technique this series has met "
            "repeatedly, not a redundancy to smooth over. A reader who has just absorbed AN "
            "6.14's more abstract framing meets the identical content again here in an "
            "immediately graspable proverb &mdash; two doors into the same room."]),
    ],
    terms=[
        ("anutappiya",
         "&ldquo;to be regretted,&rdquo; &ldquo;causing remorse&rdquo; &mdash; the discourse's "
         "own title, naming the felt consequence AN 6.14 described more abstractly."),
        ("yathā kataṁ tathā seyyaṁ",
         "&ldquo;as one has made [the bed], so one must lie [in it]&rdquo; &mdash; the "
         "proverbial image opening the discourse, reframing AN 6.14's teaching."),
        ("papañca",
         "&ldquo;proliferation&rdquo; &mdash; unchanged from AN 6.14, still the culminating and "
         "decisive item among the six."),
        ("sakkāya",
         "&ldquo;substantial reality,&rdquo; &ldquo;identity&rdquo; &mdash; unchanged from AN "
         "6.14, what one who relishes the six things is said to enjoy."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; unchanged from AN 6.14, named again in the shared "
         "closing verses as the supreme sanctuary from the yoke."),
    ],
    text_intro=(
        "The discourse in full: Sāriputta's bed-image companion to AN 6.14, sharing its closing "
        "verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sāriputta addresses the mendicants"),
        ("p", "&sect;1", "an6.15:1.1-1.3"),
        ("h3", "Making a bed that leads to regret"),
        ("p", "&sect;2", "an6.15:2.1-2.8"),
        ("h3", "Making a bed that leads to no regret"),
        ("p", "&sect;3", "an6.15:3.1-4.8"),
        ("h3", "The closing verses"),
        ("p", "&sect;4", "an6.15:5.1-6.4"),
    ],
    quiz=[
        {"q": "What proverbial image opens AN 6.15?",
         "opts": [
             "A ship navigating a storm",
             "As a mendicant makes their bed, so they must lie in it",
             "A tree bearing fruit according to its roots",
             "A river flowing to the sea"],
         "correct": 1,
         "expl": "An instantly recognizable piece of ordinary proverbial wisdom, not a "
                 "specialized formula."},
        {"q": "How much of AN 6.14's content is shared word for word with AN 6.15?",
         "opts": [
             "None — it is an entirely different teaching",
             "The six items, both closing labels, and all four lines of closing verse — only the "
             "opening frame differs",
             "Only the six items, with different closing verses",
             "Only the closing verses, with a different list of six items"],
         "correct": 1,
         "expl": "A near-total restatement with a changed frame: 'good death' becomes 'free of "
                 "regret.'"},
        {"q": "According to the guide, what is the relationship between 'good death' (AN 6.14) "
              "and 'free of regret' (AN 6.15)?",
         "opts": [
             "Two entirely separate and unrelated consequences",
             "Not two different consequences, but one consequence described twice — once "
             "externally, in terms of what's relinquished, and once from within, as how it feels",
             "'Free of regret' contradicts 'good death'",
             "They apply to different kinds of practitioners"],
         "correct": 1,
         "expl": "A technical distinction and its felt, experiential texture, given as one "
                 "teaching in two frames."},
        {"q": "What does the guide compare this AN 6.14/6.15 pairing to elsewhere in the chapter?",
         "opts": [
             "The worthiness formula of AN 6.1",
             "The thoroughbred triad at AN 6.5–6.7 — near-identical material restated under a "
             "different frame as a technique, not mere redundancy",
             "The six superhuman knowledges of AN 6.2",
             "It has no parallel elsewhere in the chapter"],
         "correct": 1,
         "expl": "A recurring compositional device: the same content through more than one door."},
        {"q": "Who speaks AN 6.15?",
         "opts": ["The Buddha", "Sāriputta, addressing the mendicants", "Mahānāma the Sakyan", "Ānanda"],
         "correct": 1,
         "expl": "Matching AN 6.14, its immediate companion."},
        {"q": "What does <em>anutappiya</em> mean?",
         "opts": [
             "Free from all suffering",
             "To be regretted, causing remorse",
             "Worthy of praise",
             "Impossible to achieve"],
         "correct": 1,
         "expl": "The discourse's own title, naming the felt consequence of an unexamined life."},
        {"q": "What remains the culminating, decisive item among the six things named, as in AN "
              "6.14?",
         "opts": ["Sleep", "Company", "Papañca, proliferation", "Talk"],
         "correct": 2,
         "expl": "Unchanged between the two companion discourses."},
        {"q": "Is a setting stated for AN 6.15?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "Matching AN 6.14, Sāriputta 'addresses the mendicants' with no location given."},
        {"q": "What comes immediately after AN 6.15 in the chapter's sequence?",
         "opts": [
             "AN 6.16, an already-published page not regenerated by this module",
             "The chapter ends at AN 6.15",
             "A return to the thoroughbred simile",
             "AN 6.20, skipping several discourses"],
         "correct": 0,
         "expl": "An-6.16.html, 'Nakula's Father', was published in this series' earlier "
                 "eighteen-page selection and is not rebuilt here."},
        {"q": "What does the guide say about reading these two discourses as separate teachings?",
         "opts": [
             "They should be read as unrelated, independent teachings",
             "They are best read as one teaching given twice — an abstract framing and an "
             "immediately graspable proverbial one, two doors into the same room",
             "AN 6.15 supersedes and replaces AN 6.14",
             "Only one of the two is considered authoritative"],
         "correct": 1,
         "expl": "A close companion pair, not a contradiction or redundancy to resolve."},
    ],
    marginalia=[
        ("The shared teaching", [
            "same six things",
            "same two outcomes",
            "same closing verses",
        ]),
        ("Only the frame changes", [
            "AN 6.14: good death",
            "AN 6.15: free of regret",
            "— one lesson, two doors",
        ]),
        ("A proverb's force", [
            "‘as you make your bed,",
            "so you must lie in it’ —",
            "instantly recognizable",
        ]),
        ("Cross-references", [
            "AN 6.14 &middot; previous, the companion",
            "AN 6.16 &middot; next, an earlier page",
        ]),
    ],
    further=[
        '<a href="%s/an6.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.14.html">AN 6.14 &middot; A Good Death</a> &mdash; previous, the same '
        "teaching under its more abstract framing.",
        '<a href="an-6.17.html">AN 6.17 &middot; Sleep</a> &mdash; further ahead, past the '
        "already-published AN 6.16.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.17 — Soppasutta
# --------------------------------------------------------------------------- #
page(
    17, "Soppa", "Sleep",
    vagga=VAGGA_2,
    prev=("an-6.16.html", "AN 6.16 &middot; Nakula&rsquo;s Father"),
    meta_title="AN 6.17 — Sleep | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Soppasutta, in which "
        "the Buddha finds junior mendicants sleeping late and asks whether any king, official, "
        "or ascetic ever gained lasting standing by indulging in sleep. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery — a fresh statement of "
                    "setting, the first since AN 6.10"),
        ("Speakers", "The Buddha, questioning the mendicants directly"),
        ("Form", "A narrated scene, a series of three parallel rhetorical questions, and a "
                 "closing injunction"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Narrative admonitions against oversleeping recur in related forms "
                              "across the Chinese Āgamas and Vinaya literature; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; an accessible narrative "
                       "discourse naming ten senior disciples by name"),
    ],
    why=(
        "AN 6.17 is a story, not a formula: senior disciples meditate through much of the "
        "night and retire; junior mendicants, newly gone forth, sleep until sunrise, snoring. "
        "The Buddha, seeing this with clairvoyance, asks the assembly three parallel questions "
        "&mdash; about a king, an official, and finally an ascetic or brahmin &mdash; each asking "
        "whether such a figure ever kept their position, or reached freedom, by indulging "
        "freely in sleep. The chapter's second discourse with a concrete narrative setting, it "
        "names ten of the Buddha's most senior disciples in a single roll call."),
    guide=[
        ("The teaching in one sentence", [
            "No king, official, or ascetic has ever kept their standing, or reached the ending "
            "of defilements, by indulging freely in sleep; mendicants should therefore guard "
            "their senses, eat moderately, and stay dedicated to wakefulness, especially in the "
            "hours the senior disciples had just used for meditation."]),
        ("A roll call of ten senior disciples", [
            "Sāriputta, Mahāmoggallāna, Mahākassapa, Mahākaccāna, Mahākoṭṭhita, Mahācunda, "
            "Mahākappina, Anuruddha, Revata, and Ānanda are named together, each simply "
            "understood to have &ldquo;done the same&rdquo; as Sāriputta: emerging from "
            "retreat, coming to the assembly hall, and later returning to meditate alone after "
            "the Buddha withdrew. The list functions as a marker of exemplary practice by name "
            "recognition &mdash; a reader familiar with these figures from elsewhere in the "
            "canon understands at once what kind of mendicant is being contrasted with the "
            "sleeping juniors."]),
        ("Three questions, one escalating structure", [
            "The Buddha's three rhetorical questions move from worldly power to spiritual "
            "attainment: first a king who rules his whole life while indulging in sleep, then "
            "a string of lesser officials down to a guild head who keeps his position the same "
            "way, and finally an ascetic or brahmin who reaches the ending of defilements while "
            "indulging in sleep, ungoverned senses, and overeating. Each question receives the "
            "same answer &mdash; &ldquo;No, sir&rdquo; &mdash; escalating from a claim about "
            "ordinary worldly success to a claim about the highest attainment the tradition "
            "describes, treating both as subject to the identical rule."]),
        ("Not a blanket condemnation of sleep", [
            "The discourse does not instruct mendicants to forgo sleep altogether; even the "
            "Buddha himself is described spending part of the night sitting in meditation "
            "before entering his own dwelling, implying rest afterward. What it targets is "
            "indulgence &mdash; sleeping &ldquo;as much as one likes,&rdquo; past the point rest "
            "requires, at the cost of the hours a serious practitioner would otherwise use."]),
        ("Why this discourse follows AN 6.14 and 6.15", [
            "Sleep was the third item named in both preceding discourses' list of six things "
            "not worth relishing. AN 6.17 can be read as a concrete illustration of that "
            "abstract item &mdash; not a list entry any longer, but a specific early-morning "
            "scene in which some mendicants relish it and others, by contrast, do not."]),
    ],
    terms=[
        ("soppa",
         "&ldquo;sleep&rdquo; &mdash; the discourse's own title, and the specific indulgence its "
         "narrative concerns."),
        ("dibbacakkhu",
         "&ldquo;clairvoyance,&rdquo; &ldquo;the divine eye&rdquo; &mdash; the faculty by which "
         "the Buddha is said to have seen the junior mendicants sleeping."),
        ("navā pabbajitā",
         "&ldquo;newly gone forth&rdquo; &mdash; how the discourse describes the sleeping "
         "mendicants, distinguishing them from the ten senior disciples named."),
        ("bodhipakkhiyā dhammā",
         "&ldquo;qualities on the side of awakening&rdquo; &mdash; what the closing injunction "
         "asks mendicants to develop in the evening and toward dawn, instead of sleeping."),
        ("indriyāni aguttāni",
         "&ldquo;sense doors unguarded&rdquo; &mdash; one of the conditions the Buddha lists as "
         "incompatible with reaching the ending of defilements while indulging in sleep."),
    ],
    text_intro=(
        "The discourse in full: the sleeping juniors, the Buddha's three questions, and his "
        "closing injunction. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The senior disciples meditate; the juniors sleep"),
        ("p", "&sect;1", "an6.17:1.1-1.18"),
        ("h3", "Where are the senior disciples?"),
        ("p", "&sect;2", "an6.17:2.1-2.19"),
        ("h3", "Three questions: king, official, ascetic"),
        ("p", "&sect;3", "an6.17:3.1-4.7"),
        ("h3", "The injunction"),
        ("p", "&sect;4", "an6.17:5.1-5.3"),
    ],
    quiz=[
        {"q": "What does the Buddha find when he checks on the mendicants after his own period "
              "of meditation?",
         "opts": [
             "All the mendicants have already gone to sleep",
             "Junior mendicants, newly gone forth, sleeping until sunrise and snoring, after the "
             "senior disciples had returned to their own dwellings",
             "The mendicants are all still meditating",
             "The mendicants have left the monastery"],
         "correct": 1,
         "expl": "Seen with his clairvoyance, contrasted with the ten senior disciples named "
                 "earlier."},
        {"q": "How many senior disciples are named in the roll call at the start of this "
              "discourse?",
         "opts": ["Five", "Ten", "Two", "Twenty"],
         "correct": 1,
         "expl": "Sāriputta, Mahāmoggallāna, Mahākassapa, Mahākaccāna, Mahākoṭṭhita, Mahācunda, "
                 "Mahākappina, Anuruddha, Revata, and Ānanda."},
        {"q": "What three figures does the Buddha ask about in his rhetorical questions?",
         "opts": [
             "A farmer, a merchant, and a scholar",
             "A king (and various officials down to a guild head), and finally an ascetic or "
             "brahmin",
             "Three different kings from different countries",
             "Three of his own senior disciples"],
         "correct": 1,
         "expl": "An escalation from worldly power to the highest spiritual attainment, each "
                 "receiving the same answer."},
        {"q": "What is the answer given to each of the three questions?",
         "opts": [
             "'Yes, sir' — such cases are common",
             "'No, sir' — no one has kept worldly standing or reached the ending of defilements "
             "by indulging freely in sleep",
             "The mendicants refuse to answer",
             "Different answers are given to each question"],
         "correct": 1,
         "expl": "The same negative answer applies whether the claim concerns worldly power or "
                 "the highest attainment."},
        {"q": "Does the discourse instruct mendicants to forgo sleep entirely?",
         "opts": [
             "Yes, sleep is condemned outright",
             "No — even the Buddha is shown resting after meditating; the target is indulgence, "
             "sleeping 'as much as one likes,' not rest itself",
             "Only senior disciples are permitted to sleep",
             "The text does not address this question at all"],
         "correct": 1,
         "expl": "A caution against excess, not a blanket prohibition."},
        {"q": "How does the guide connect AN 6.17 to AN 6.14 and 6.15?",
         "opts": [
             "There is no connection between them",
             "Sleep was the third item in both discourses' list of six things not worth "
             "relishing; AN 6.17 illustrates that abstract item with a concrete scene",
             "AN 6.17 contradicts the teaching of AN 6.14 and 6.15",
             "AN 6.17 replaces the six-item list with a new one"],
         "correct": 1,
         "expl": "A concrete narrative illustration following two more abstract, formula-based "
                 "discourses."},
        {"q": "What is significant about AN 6.17's setting, compared to the discourses "
              "immediately before it in this chapter?",
         "opts": [
             "It is the first discourse in the chapter to state a setting at all",
             "It restates the setting fresh at Sāvatthī, the first such restatement since AN 6.10",
             "It is set at an entirely new location never mentioned before",
             "Its setting is left deliberately unstated, like AN 6.11–6.15"],
         "correct": 1,
         "expl": "AN 6.11 through 6.15 gave no setting at all; AN 6.17 restates Sāvatthī "
                 "explicitly."},
        {"q": "What faculty does the Buddha use to see the sleeping junior mendicants?",
         "opts": ["Clairaudience", "Clairvoyance, the divine eye", "Mind-reading", "Recollection of past lives"],
         "correct": 1,
         "expl": "Dibbacakkhu, already named among the six superhuman knowledges at AN 6.2."},
        {"q": "What does the closing injunction ask mendicants to do?",
         "opts": [
             "Sleep even less than the junior mendicants already did",
             "Guard their sense doors, eat in moderation, be dedicated to wakefulness, and "
             "pursue the qualities on the side of awakening in the evening and toward dawn",
             "Report any mendicant seen sleeping to a senior disciple",
             "Meditate only during daylight hours"],
         "correct": 1,
         "expl": "A positive training instruction, not merely a prohibition."},
        {"q": "What does <em>navā pabbajitā</em> mean?",
         "opts": [
             "Senior disciples of long standing",
             "Newly gone forth — recently ordained mendicants",
             "Lay followers who have not yet ordained",
             "Mendicants who have left the community"],
         "correct": 1,
         "expl": "How the discourse describes the sleeping mendicants, distinct from the ten "
                 "named seniors."},
    ],
    marginalia=[
        ("Ten named seniors", [
            "Sāriputta &middot; Mahāmoggallāna",
            "Mahākassapa &middot; Mahākaccāna",
            "Mahākoṭṭhita &middot; Mahācunda",
            "Mahākappina &middot; Anuruddha",
            "Revata &middot; Ānanda",
        ]),
        ("Three questions", [
            "a king who indulges",
            "officials down to a guild head",
            "an ascetic reaching awakening",
        ]),
        ("Not against sleep itself", [
            "even the Buddha rests",
            "after meditating —",
            "the target is indulgence",
        ]),
        ("Cross-references", [
            "AN 6.14/6.15 &middot; sleep as one of six",
            "AN 6.2 &middot; clairvoyance defined",
        ]),
    ],
    further=[
        '<a href="%s/an6.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.18.html">AN 6.18 &middot; A Fish Dealer</a> &mdash; next, a difficult '
        "discourse on livelihood and intention.",
        '<a href="an-6.16.html">AN 6.16 &middot; Nakula&rsquo;s Father</a> &mdash; previous, an '
        "earlier-published page in this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.18 — Macchabandhasutta
# --------------------------------------------------------------------------- #
page(
    18, "Macchabandha", "A Fish Dealer",
    vagga=VAGGA_2,
    meta_title="AN 6.18 — A Fish Dealer | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Macchabandhasutta, in "
        "which the Buddha uses the sight of a fish dealer to argue that killing livelihoods "
        "never lead to prosperity, and extends the logic, briefly and starkly, to killing "
        "people. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "On the road in the land of the Kosalans, at the sight of a fish dealer "
                    "selling fish he had killed himself"),
        ("Speakers", "The Buddha, addressing the mendicants traveling with him"),
        ("Form", "A series of parallel rhetorical questions about killing-based livelihoods, "
                 "closing with an explicit and severe extension to killing human beings"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Teachings against killing-based livelihood recur widely across "
                              "the Chinese Āgamas and Vinaya literature; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short in length but harsh in "
                       "content, closing on a line about killing people that this guide will not "
                       "soften"),
    ],
    why=(
        "This discourse is one of the harder texts to read plainly in this series so far. The "
        "Buddha, seeing a fish dealer at work, asks whether killing-based trades ever produce "
        "real prosperity, and after each denial supplies the same explanation: because the "
        "practitioner regards the creature being led to slaughter with bad intentions. The "
        "final line extends this reasoning explicitly to a person who regards <em>human "
        "beings</em> brought to slaughter with the same bad intentions, naming that as grounds "
        "for a bad rebirth. This reading guide states what the text says without softening it, "
        "and without pretending the discourse settles every question a modern reader might "
        "bring to it."),
    guide=[
        ("The teaching in one sentence", [
            "Livelihoods built on killing &mdash; a fish dealer, a butcher of cattle, sheep, "
            "pigs, or poultry, a deer-hunter &mdash; have never, in the Buddha's own claimed "
            "experience, produced wealth, fine transport, or a large fortune, because the "
            "practitioner regards the beings led to slaughter with bad intentions; the "
            "discourse then states, starkly, that the same holds far worse for someone who "
            "regards human beings brought to slaughter the same way."]),
        ("What the discourse actually argues, and what it does not", [
            "The argument is not that killing-based work is poorly paid as an economic "
            "observation; it is a claim about karmic consequence, stated through a rhetorical "
            "pattern of denial (&ldquo;have you ever seen or heard&hellip; No, sir&rdquo;) "
            "repeated across five kinds of livelihood. The stated reason each time is identical: "
            "&ldquo;because when the [animals] are led to the slaughter he regards them with bad "
            "intentions.&rdquo; The discourse locates the harm in the killer's own state of "
            "mind at the moment of killing, not in some external judgment about the trade "
            "itself."]),
        ("The final line, read directly", [
            "The closing sentence &mdash; &ldquo;how much worse is someone who regards human "
            "beings brought to the slaughter with bad intentions&rdquo; &mdash; almost certainly "
            "refers to an executioner or a similar figure whose work is literally the killing "
            "of condemned people, a recognized occupation named elsewhere in the canon among "
            "livelihoods incompatible with the path. It is not a general statement about anger "
            "toward other people in ordinary life. Even read this narrowly, it remains a severe "
            "claim &mdash; that such a person is, on this discourse's own terms, reborn "
            "&ldquo;in a place of loss, a bad place, the underworld, hell&rdquo; &mdash; and this "
            "guide does not attempt to make that claim gentler than the text states it."]),
        ("A note on what this discourse does not settle", [
            "Readers today reasonably ask harder questions than this short text answers: what "
            "of livelihoods that cause death indirectly, or unintentionally, or at industrial "
            "scale and distance from any single killer's state of mind? The discourse is "
            "narrowly built around a specific, visible act &mdash; a person directly killing "
            "an animal or, in the closing line, a person &mdash; and its reasoning turns on the "
            "killer's own regard in that moment. Extending it to other, less direct cases is an "
            "inference a reader might draw, not a claim this short text makes explicitly."]),
        ("Continuing the chapter's turn toward mortality", [
            "Coming directly after AN 6.14, 6.15, and 6.17, all concerned in different ways with "
            "how a mendicant relates to death, AN 6.18 shifts the lens outward: not a "
            "mendicant's own dying, but the taking of life by others, witnessed on the road. The "
            "chapter's final two discourses, AN 6.19 and 6.20, return the lens fully inward, to "
            "a mendicant's own mindfulness of death."]),
    ],
    terms=[
        ("macchabandha",
         "&ldquo;fish dealer,&rdquo; literally &ldquo;fish binder/catcher&rdquo; &mdash; the "
         "figure whose trade opens the discourse and gives it its title."),
        ("vadhāya nīyamāne",
         "&ldquo;being led to slaughter&rdquo; &mdash; the discourse's recurring phrase, applied "
         "first to animals and then, in the closing line, to human beings."),
        ("pāpakaṁ cittaṁ paccupaṭṭhāpeti",
         "&ldquo;regards with bad intentions&rdquo; &mdash; the discourse's stated cause of harm "
         "in every case, locating the fault in the killer's mental state."),
        ("apāya",
         "&ldquo;place of loss&rdquo; &mdash; one of the terms in the fourfold description of "
         "the bad rebirth named at the discourse's close: place of loss, bad place, underworld, "
         "hell."),
        ("kosala",
         "the Kosalan lands &mdash; where the Buddha was wandering with a large Saṅgha when the "
         "encounter with the fish dealer occurred."),
    ],
    text_intro=(
        "The discourse in full, without abridgment: the fish dealer, the parallel questions "
        "about other killing trades, and the closing line about human beings. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The fish dealer on the road"),
        ("p", "&sect;1", "an6.18:1.1-1.6"),
        ("h3", "The fish dealer and the cattle butcher"),
        ("p", "&sect;2", "an6.18:2.1-3.9"),
        ("h3", "Sheep, pigs, poultry, deer — and the closing line"),
        ("p", "&sect;3", "an6.18:4.1-4.16"),
    ],
    quiz=[
        {"q": "What does the Buddha see that prompts this discourse?",
         "opts": [
             "A farmer plowing a field",
             "A fish dealer selling fish he had killed himself",
             "A group of mendicants arguing",
             "A merchant cheating a customer"],
         "correct": 1,
         "expl": "The sight leads the Buddha to leave the road and address the mendicants "
                 "traveling with him."},
        {"q": "What claim does the Buddha make about killing-based livelihoods?",
         "opts": [
             "That they are illegal and should be reported",
             "That he has never seen or heard of such a livelihood producing wealth, fine "
             "transport, or a large fortune",
             "That they are acceptable as long as performed skillfully",
             "That only fish dealers, not other killing trades, are affected"],
         "correct": 1,
         "expl": "Repeated across fish dealer, cattle butcher, and butchers of sheep, pigs, "
                 "poultry, and deer-hunters."},
        {"q": "What reason does the discourse give, each time, for why these livelihoods do not "
              "prosper?",
         "opts": [
             "Because society condemns such trades",
             "Because the practitioner regards the animals led to slaughter with bad intentions",
             "Because the work is physically exhausting",
             "No reason is given"],
         "correct": 1,
         "expl": "The discourse locates the harm in the killer's own state of mind at the moment "
                 "of killing."},
        {"q": "How does the guide interpret the discourse's closing line about human beings "
              "'brought to the slaughter'?",
         "opts": [
             "As a general statement about feeling anger toward other people in ordinary life",
             "As almost certainly referring to an executioner or similar figure whose work is "
             "literally killing condemned people — a recognized occupation named elsewhere in "
             "the canon, not a claim about ordinary interpersonal anger",
             "As a later scribal error that should be disregarded",
             "As referring to soldiers in battle specifically"],
         "correct": 1,
         "expl": "A narrow reading tied to the discourse's own logic, not stretched beyond what "
                 "the text states."},
        {"q": "What does the guide say this discourse does NOT settle?",
         "opts": [
             "Everything a modern reader might ask — the discourse is treated as fully "
             "comprehensive",
             "Harder questions about livelihoods that cause death indirectly, unintentionally, "
             "or at industrial scale and distance from any single killer's state of mind",
             "The discourse settles nothing at all and should be disregarded",
             "Whether killing is ever acceptable under any circumstances"],
         "correct": 1,
         "expl": "The guide is explicit that extending the text's narrow reasoning to other "
                 "cases is an inference, not a claim the text itself makes."},
        {"q": "What does the discourse say happens to someone who regards human beings brought "
              "to slaughter with bad intentions?",
         "opts": [
             "Nothing — the text stops short of any consequence",
             "They are reborn in a place of loss, a bad place, the underworld, hell",
             "They are simply advised to change professions",
             "They are praised for their honesty about their work"],
         "correct": 1,
         "expl": "A severe claim the guide states directly rather than softening."},
        {"q": "How does this discourse relate to the chapter's surrounding material on death?",
         "opts": [
             "It is entirely unrelated to any surrounding theme",
             "It shifts the chapter's lens outward — from a mendicant's own dying (AN 6.14, "
             "6.15) to the taking of life by others, before AN 6.19–20 return inward to a "
             "mendicant's own mindfulness of death",
             "It replaces the death theme with an economic argument only",
             "It directly continues AN 6.17's narrative about sleeping mendicants"],
         "correct": 1,
         "expl": "A pivot point within the chapter's broader concern with mortality."},
        {"q": "What five killing-trades are named before the closing line about human beings?",
         "opts": [
             "Farmer, merchant, blacksmith, potter, weaver",
             "Fish dealer, cattle butcher, sheep butcher, pig butcher, poultry butcher, and "
             "deer-hunter",
             "Soldier, executioner, jailer, tax collector, moneylender",
             "Only the fish dealer is named"],
         "correct": 1,
         "expl": "Six killing-based livelihoods in total, each receiving the identical "
                 "question-and-denial pattern."},
        {"q": "Where is AN 6.18 set?",
         "opts": [
             "At Sāvatthī, in Jeta's Grove",
             "On the road, while the Buddha was wandering in the land of the Kosalans with a "
             "large Saṅgha",
             "At Kapilavatthu, among the Sakyans",
             "At Ñātika, in the brick house"],
         "correct": 1,
         "expl": "A traveling scene, prompted directly by what the Buddha and the mendicants "
                 "encountered on the road."},
        {"q": "What does the guide say about its own approach to this discourse's harsh content?",
         "opts": [
             "It omits the difficult closing line entirely",
             "It states what the text says without softening it, while being explicit about what "
             "the text does and does not claim",
             "It argues the text is mistranslated and should be corrected",
             "It refuses to discuss the discourse's content at all"],
         "correct": 1,
         "expl": "A direct, honest reading rather than a smoothed-over paraphrase."},
    ],
    marginalia=[
        ("Six killing trades", [
            "fish dealer &middot; cattle",
            "sheep &middot; pigs &middot; poultry",
            "deer-hunter",
        ]),
        ("The stated cause", [
            "not the trade itself,",
            "but bad intentions at",
            "the moment of killing",
        ]),
        ("The closing line", [
            "extended, starkly, to",
            "one who kills people —",
            "likely an executioner",
        ]),
        ("What this text doesn't settle", [
            "indirect or distant",
            "causes of death —",
            "not addressed here",
        ]),
    ],
    further=[
        '<a href="%s/an6.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.19.html">AN 6.19 &middot; Mindfulness of Death (1st)</a> &mdash; next, '
        "returning to a mendicant's own relationship with mortality.",
        '<a href="an-6.17.html">AN 6.17 &middot; Sleep</a> &mdash; previous, a different '
        "narrative discourse from the same road-and-monastery setting.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.19 — Paṭhamamaraṇassatisutta
# --------------------------------------------------------------------------- #
page(
    19, "Paṭhamamaraṇassati", "Mindfulness of Death (1st)",
    vagga=VAGGA_2,
    meta_title="AN 6.19 — Mindfulness of Death (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamamaraṇassatisutta, "
        "in which seven mendicants each report their own practice of mindfulness of death, and "
        "the Buddha ranks their answers as negligent or diligent. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Ñātika, in the brick house — a fresh setting, shared with AN 6.20"),
        ("Speakers", "The Buddha and seven unnamed mendicants, in turn"),
        ("Form", "A question put to the assembly, seven individual answers, and the Buddha's "
                 "own ranking of them into two grades"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Mindfulness of death (maraṇasati/maraṇānusmṛti) is a widely "
                              "attested practice across the Chinese Āgamas and later Buddhist "
                              "literature; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a clear, escalating dialogue "
                       "structure, easy to follow despite its serious subject"),
    ],
    why=(
        "The Buddha asks the assembly directly whether they develop mindfulness of death, and "
        "seven mendicants answer in turn, each naming a shorter span of assumed remaining life: "
        "a day and a night, then a day, then the time to eat a meal, then four or five "
        "mouthfuls, then a single mouthful, then finally the time of one breath. All seven "
        "describe what sounds like the same practice at different scales &mdash; and the "
        "Buddha's verdict is that only the last two count as genuinely diligent. This discourse "
        "gives its own criterion for what makes mindfulness of death rigorous rather than "
        "merely notional."),
    guide=[
        ("The teaching in one sentence", [
            "Of seven mendicants who each report developing mindfulness of death by reflecting "
            "on how much they could accomplish if they had only some short remaining span of "
            "life, the Buddha calls the five who named a day and night down to a few mouthfuls "
            "negligent, and only the two who named a single mouthful or a single breath "
            "diligent."]),
        ("A single practice, tested at shrinking scales", [
            "Every one of the seven answers follows the identical form: &ldquo;Oh, if I'd only "
            "live for &hellip;, I'd focus on the Buddha's instructions and I could really "
            "achieve a lot.&rdquo; What varies is only the assumed remaining span &mdash; a day "
            "and night, a day, a meal, four or five mouthfuls, one mouthful, one breath. The "
            "discourse does not ask mendicants to imagine different content; it asks how short a "
            "span they are willing to take seriously as possibly their last."]),
        ("Where the Buddha draws the line, and why", [
            "The cutoff falls between &ldquo;four or five mouthfuls&rdquo; and &ldquo;a single "
            "mouthful&rdquo; &mdash; a distinction that might look arbitrary stated baldly, but "
            "the discourse's own logic is about the interval between successive checks. A "
            "mendicant who only reflects on death across the span of an entire meal has, within "
            "that meal, many moments where the reflection has gone stale; one who reflects at "
            "the scale of a single mouthful, or a single breath, is renewing the reflection "
            "continuously enough that negligence has no room to creep in between checks."]),
        ("Negligence, not the content of the reflection, is being judged", [
            "It would be a misreading to conclude the Buddha is dismissing the first five "
            "mendicants' sincerity or effort. He does not question whether they meant what they "
            "said; the discourse explicitly names their practice &ldquo;slack&rdquo; "
            "(<em>pamattā</em>) rather than false or insincere. The distinction drawn is about "
            "rigor of application, not honesty of intention."]),
        ("Setting up AN 6.20's fuller method", [
            "This discourse names a criterion &mdash; frequency of renewal &mdash; without "
            "describing what a mendicant actually reflects on beyond the bare formula of wishing "
            "for more time. AN 6.20, immediately following and sharing this discourse's setting "
            "at Ñātika, supplies that fuller content: a nightly and daily checklist of specific "
            "causes of death and unabandoned unskillful qualities, with its own simile of "
            "urgency, clothes or head on fire."]),
    ],
    terms=[
        ("maraṇassati",
         "&ldquo;mindfulness of death&rdquo; &mdash; the practice this discourse and its "
         "companion, AN 6.20, both concern."),
        ("amatogadha",
         "not named directly in this discourse but the term elsewhere for what mindfulness of "
         "death is said to have as its objective: &ldquo;freedom from death,&rdquo; here "
         "rendered simply as its stated culmination."),
        ("pamatta",
         "&ldquo;negligent,&rdquo; &ldquo;slack&rdquo; &mdash; the Buddha's verdict on the five "
         "mendicants whose reflection spans a day and night down to a few mouthfuls."),
        ("appamatta",
         "&ldquo;diligent,&rdquo; &ldquo;heedful&rdquo; &mdash; the verdict on the two "
         "mendicants whose reflection renews at the scale of a single mouthful or a single "
         "breath."),
        ("āsavānaṁ khayāya",
         "&ldquo;for the ending of defilements&rdquo; &mdash; the stated purpose toward which "
         "diligent mendicants are said to keenly develop mindfulness of death."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's question, seven mendicants' answers, and his "
        "ranking of them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Ñātika: the Buddha's question"),
        ("p", "&sect;1", "an6.19:1.1-1.7"),
        ("h3", "Seven mendicants answer in turn"),
        ("p", "&sect;2", "an6.19:2.1-7.6"),
        ("h3", "The Buddha's verdict: negligent and diligent"),
        ("p", "&sect;3", "an6.19:8.1-16.3"),
    ],
    quiz=[
        {"q": "What form do all seven mendicants' answers share?",
         "opts": [
             "Each names a completely different practice",
             "Each follows the identical form: wishing for a short remaining span of life in "
             "order to focus on the Buddha's instructions, varying only the length of that span",
             "Each recites a different verse",
             "Each describes a different meditative absorption"],
         "correct": 1,
         "expl": "A day and night, a day, a meal, several mouthfuls, one mouthful, one breath — "
                 "the same structure at shrinking scales."},
        {"q": "Where does the Buddha draw the line between negligent and diligent practice?",
         "opts": [
             "Between a day and night and a single day",
             "Between four or five mouthfuls and a single mouthful",
             "There is no line drawn — all seven are equally praised",
             "Between a single breath and a single mouthful"],
         "correct": 1,
         "expl": "The five longer spans are called negligent; the shortest two, single mouthful "
                 "and single breath, are called diligent."},
        {"q": "According to the guide, what is the actual logic behind where this line falls?",
         "opts": [
             "It is arbitrary and the text gives no reasoning",
             "It concerns the interval between successive checks — a longer span leaves room for "
             "the reflection to go stale before it's renewed",
             "It reflects seniority among the mendicants",
             "It is based on which mendicant spoke first"],
         "correct": 1,
         "expl": "Frequency of renewal, not merely sincerity, is what separates the two grades."},
        {"q": "Does the Buddha's verdict question the first five mendicants' sincerity?",
         "opts": [
             "Yes — he accuses them of lying",
             "No — the discourse explicitly calls their practice 'slack' rather than false or "
             "insincere; the distinction is about rigor, not honesty of intention",
             "The text does not address this question",
             "Yes — he expels them from the assembly"],
         "correct": 1,
         "expl": "A judgment about application, not about the mendicants' truthfulness."},
        {"q": "What does <em>pamatta</em> mean?",
         "opts": ["Diligent, heedful", "Negligent, slack", "Awakened", "Compassionate"],
         "correct": 1,
         "expl": "The Buddha's verdict on the five longer-span answers."},
        {"q": "Where is AN 6.19 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Ñātika, in the brick house",
             "Kapilavatthu, among the Sakyans",
             "On the road in the land of the Kosalans"],
         "correct": 1,
         "expl": "A fresh setting, shared with the discourse immediately following, AN 6.20."},
        {"q": "What does AN 6.20 add that AN 6.19 does not supply?",
         "opts": [
             "Nothing — the two discourses are identical",
             "A fuller method: specific causes of death and unabandoned unskillful qualities to "
             "check nightly and daily, with its own simile of urgency",
             "A contradiction of AN 6.19's criterion",
             "An entirely unrelated teaching on generosity"],
         "correct": 1,
         "expl": "AN 6.19 names a criterion (frequency); AN 6.20 supplies detailed content."},
        {"q": "What is mindfulness of death said to have as its objective and culmination?",
         "opts": [
             "Rebirth as a deity", "Freedom from death", "Material prosperity", "Fame among "
             "other mendicants"],
         "correct": 1,
         "expl": "Stated at the discourse's opening, before the seven mendicants answer."},
        {"q": "How many mendicants answer the Buddha's question in this discourse?",
         "opts": ["Three", "Five", "Seven", "Ten"],
         "correct": 2,
         "expl": "Seven separate answers, each at a shorter assumed span than the last."},
        {"q": "What is the shortest span named by any of the seven mendicants?",
         "opts": [
             "A single day",
             "The time it takes to breathe out after breathing in, or breathe in after breathing "
             "out",
             "A single mouthful of food",
             "An hour"],
         "correct": 1,
         "expl": "The seventh and final answer, paired with 'a single mouthful' as the two "
                 "diligent grades."},
    ],
    marginalia=[
        ("Seven spans named", [
            "day &amp; night &middot; a day",
            "one meal &middot; 4&ndash;5 bites",
            "one bite &middot; one breath",
        ]),
        ("The cutoff", [
            "negligent: day down to",
            "several mouthfuls",
            "diligent: one bite, one breath",
        ]),
        ("What's being judged", [
            "not sincerity —",
            "frequency of renewal,",
            "how long between checks",
        ]),
        ("Cross-references", [
            "AN 6.18 &middot; previous, a hard discourse",
            "AN 6.20 &middot; next, the fuller method",
        ]),
    ],
    further=[
        '<a href="%s/an6.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.20.html">AN 6.20 &middot; Mindfulness of Death (2nd)</a> &mdash; next, '
        "closing the chapter with the fuller method.",
        '<a href="an-6.18.html">AN 6.18 &middot; A Fish Dealer</a> &mdash; previous, a difficult '
        "discourse on livelihood and killing.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.20 — Dutiyamaraṇassatisutta
# --------------------------------------------------------------------------- #
page(
    20, "Dutiyamaraṇassati", "Mindfulness of Death (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 6.20 — Mindfulness of Death (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyamaraṇassatisutta, "
        "closing the Sāraṇīyavagga with the full method of mindfulness of death: a nightly and "
        "daily checklist, and the simile of clothes or head on fire. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Ñātika, in the brick house — restated fresh, matching AN 6.19"),
        ("Speakers", SPEAKER),
        ("Form", "A named method, given twice &mdash; once for evening, once for morning "
                 "&mdash; each with an identical simile of urgency"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "As with AN 6.19, mindfulness of death recurs widely across the "
                              "Chinese Āgamas and later literature; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a fuller, more procedural "
                       "teaching than AN 6.19, worth reading slowly for its structure"),
    ],
    why=(
        "AN 6.19 named a criterion &mdash; how frequently the reflection on death is renewed "
        "&mdash; without saying what, specifically, a mendicant should reflect on. AN 6.20, "
        "closing the chapter, supplies that content in full: as day turns to night, and again as "
        "night turns to day, a mendicant runs through the many ordinary ways death could arrive "
        "&mdash; snakebite, a fall, food poisoning, illness &mdash; and asks whether any "
        "unabandoned unskillful quality would obstruct their progress if death came before the "
        "next check. What follows from that question, in either direction, is stated with the "
        "same urgency twice: extraordinary effort if the answer is yes, sustained joyful "
        "practice if the answer is no."),
    guide=[
        ("The teaching in one sentence", [
            "Twice daily &mdash; as day passes into night, and as night passes into day &mdash; a "
            "mendicant should reflect on the many ordinary causes of death, check whether any "
            "unabandoned unskillful quality would be an obstacle if death came before the next "
            "check, and respond either with extraordinary urgency to give up such qualities or "
            "with rapture and joy in continued skillful training."]),
        ("A concrete, unglamorous list of causes", [
            "The discourse does not speak abstractly of mortality; it names specific, mundane "
            "hazards &mdash; snakebite, scorpion or centipede sting, stumbling off a cliff, food "
            "poisoning, disturbance of bile, phlegm, or the bodily &ldquo;winds&rdquo; &mdash; the "
            "kind of dangers any person, not only a mendicant, might reasonably imagine facing "
            "on an ordinary night or day. Death here is not a distant abstraction to be "
            "philosophized about but a near, mundane possibility to be checked against, twice "
            "within one day."]),
        ("The question that follows the reflection", [
            "Naming causes of death is only the first step; the discourse's actual instruction "
            "is the question that follows: &ldquo;Are there any bad, unskillful qualities that I "
            "haven't given up, which might be an obstacle to my progress if I die "
            "tonight?&rdquo; &mdash; or, in the morning version, &ldquo;today.&rdquo; Mindfulness "
            "of death, on this discourse's terms, is not primarily about dwelling on death "
            "itself; it is a device for surfacing exactly what remains unfinished in one's own "
            "practice, on a fixed and frequent schedule."]),
        ("The simile: clothes or head on fire", [
            "For a mendicant who finds unabandoned unskillful qualities upon checking, the "
            "discourse prescribes a response measured against a stock canonical image of "
            "maximum urgency: someone whose clothes or head have caught fire would apply "
            "&ldquo;extraordinary enthusiasm, effort, zeal, vigor, perseverance, mindfulness, "
            "and situational awareness&rdquo; to extinguish it, and giving up unskillful "
            "qualities should be met with the identical seven-part urgency."]),
        ("Closing the chapter on a doubled structure", [
            "AN 6.20 states its method twice &mdash; evening and morning &mdash; in nearly "
            "identical wording, closing the Sāraṇīyavagga on a note of sustained, twice-daily "
            "practice rather than a single teaching given once. The chapter that opened on "
            "warmth between spiritual companions closes, ten discourses later, on what a "
            "mendicant owes to their own unfinished practice, checked against the plain fact "
            "that today or tonight might be the last chance to address it."]),
    ],
    terms=[
        ("maraṇassati",
         "&ldquo;mindfulness of death&rdquo; &mdash; unchanged in name from AN 6.19, now given "
         "its full method."),
        ("antarāyika",
         "&ldquo;an obstacle,&rdquo; &ldquo;obstructive&rdquo; &mdash; what an unabandoned "
         "unskillful quality is said to be, to a mendicant's progress, if death arrived before "
         "it were given up."),
        ("ussukkaṁ āpajjeyya",
         "&ldquo;should apply extraordinary effort&rdquo; &mdash; the instruction following a "
         "positive check, paired with the fire simile."),
        ("pāmojja",
         "&ldquo;rapture and joy&rdquo; &mdash; what a mendicant who finds no unabandoned "
         "unskillful qualities is instructed to meditate with instead, training day and night in "
         "skillful qualities."),
        ("amatogadha",
         "&ldquo;freedom from death as its objective and culmination&rdquo; &mdash; the closing "
         "restatement, shared with AN 6.19, of what mindfulness of death is ultimately for."),
    ],
    text_intro=(
        "The discourse in full: the evening reflection and the morning reflection, each closing "
        "with the fire simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Ñātika: the question restated"),
        ("p", "&sect;1", "an6.20:1.1-1.4"),
        ("h3", "The evening reflection"),
        ("p", "&sect;2", "an6.20:2.1-4.2"),
        ("h3", "The morning reflection"),
        ("p", "&sect;3", "an6.20:5.1-7.2"),
        ("h3", "The conclusion"),
        ("p", "&sect;4", "an6.20:8.1"),
    ],
    quiz=[
        {"q": "How often does AN 6.20 instruct a mendicant to run through its reflection?",
         "opts": [
             "Once, at the start of practice",
             "Twice daily — as day passes into night, and as night passes into day",
             "Only on special observance days",
             "Once a week"],
         "correct": 1,
         "expl": "A doubled structure, evening and morning, in nearly identical wording."},
        {"q": "What kind of causes of death does the discourse name?",
         "opts": [
             "Abstract philosophical categories of impermanence",
             "Concrete, mundane hazards — snakebite, scorpion or centipede sting, a fall, food "
             "poisoning, bodily disturbances",
             "Only death by old age",
             "Only death in battle"],
         "correct": 1,
         "expl": "Ordinary dangers anyone might imagine facing on a given night or day."},
        {"q": "What is the actual question a mendicant is instructed to ask after naming these "
              "causes?",
         "opts": [
             "Whether they are afraid to die",
             "Whether there are any unabandoned unskillful qualities that would be an obstacle "
             "to their progress if death came before the next check",
             "Whether their meditation cushion needs replacing",
             "Whether other mendicants are more advanced than they are"],
         "correct": 1,
         "expl": "A device for surfacing what remains unfinished in one's own practice, checked "
                 "on a fixed schedule."},
        {"q": "What simile does the discourse use for the urgency required if unskillful "
              "qualities are found?",
         "opts": [
             "A boat crossing a flood",
             "Someone whose clothes or head have caught fire, applying extraordinary "
             "enthusiasm, effort, zeal, vigor, perseverance, mindfulness, and situational "
             "awareness to extinguish it",
             "A farmer plowing a field before the rains",
             "A physician diagnosing an illness"],
         "correct": 1,
         "expl": "A stock canonical image of maximum urgency, applied here to giving up "
                 "unskillful qualities."},
        {"q": "What should a mendicant do if the check finds no unabandoned unskillful "
              "qualities?",
         "opts": [
             "Stop practicing mindfulness of death entirely",
             "Meditate with rapture and joy, training day and night in skillful qualities",
             "Report their attainment to the Buddha immediately",
             "Begin teaching other mendicants"],
         "correct": 1,
         "expl": "A positive outcome met with sustained joyful practice, not complacency."},
        {"q": "According to the guide, what is mindfulness of death primarily about, on this "
              "discourse's terms?",
         "opts": [
             "Dwelling on death itself as an end in its own right",
             "A device for surfacing exactly what remains unfinished in one's own practice, on a "
             "fixed and frequent schedule",
             "Preparing funeral arrangements",
             "Convincing others of the inevitability of death"],
         "correct": 1,
         "expl": "Not morbid dwelling, but a practical checking device."},
        {"q": "Where is AN 6.20 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Ñātika, in the brick house — matching AN 6.19",
             "Kapilavatthu",
             "On the road among the Kosalans"],
         "correct": 1,
         "expl": "A fresh restatement of the same setting shared with AN 6.19."},
        {"q": "What relationship does the guide draw between AN 6.19 and AN 6.20?",
         "opts": [
             "They are unrelated teachings placed together by coincidence",
             "AN 6.19 names a criterion of frequency without content; AN 6.20 supplies the full "
             "method and content of what to actually reflect on",
             "AN 6.20 contradicts AN 6.19's ranking of negligent and diligent practice",
             "AN 6.20 is addressed only to lay followers, unlike AN 6.19"],
         "correct": 1,
         "expl": "A companion pair completing one teaching across two discourses."},
        {"q": "What does the guide say about how the chapter closes?",
         "opts": [
             "On an unrelated note, disconnected from its opening",
             "On a note of sustained, twice-daily practice — moving from the chapter's opening "
             "concern with warmth between companions to what a mendicant owes their own "
             "unfinished practice",
             "With a warning against ever practicing mindfulness of death",
             "By repeating the worthiness formula from AN 6.1"],
         "correct": 1,
         "expl": "A shift in register across the chapter's ten discourses, from communal warmth "
                 "to individual urgency."},
        {"q": "What does <em>antarāyika</em> mean?",
         "opts": ["Helpful, supportive", "An obstacle, obstructive", "Joyful", "Compassionate"],
         "correct": 1,
         "expl": "What an unabandoned unskillful quality is said to be to a mendicant's "
                 "progress."},
    ],
    marginalia=[
        ("Twice daily", [
            "evening: day into night",
            "morning: night into day",
            "same method, restated",
        ]),
        ("Mundane causes named", [
            "snakebite &middot; sting",
            "a fall &middot; food poisoning",
            "bodily disturbance",
        ]),
        ("The fire simile", [
            "clothes or head aflame —",
            "extraordinary urgency,",
            "applied to practice",
        ]),
        ("Cross-references", [
            "AN 6.19 &middot; previous, the criterion",
            "AN 6.11 &middot; the chapter's opening theme",
        ]),
    ],
    further=[
        '<a href="%s/an6.20/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.19.html">AN 6.19 &middot; Mindfulness of Death (1st)</a> &mdash; previous, '
        "the criterion this discourse fills out with full content.",
        '<a href="an-6.11.html">AN 6.11 &middot; Warm-hearted (1st)</a> &mdash; this '
        "chapter&rsquo;s opening, for contrast with where it closes.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 3 — Anuttariyavagga (AN 6.21–30)
# --------------------------------------------------------------------------- #
VAGGA_3 = "<em>Anuttariyavagga</em> &mdash; the third chapter of the Sixes"


# --------------------------------------------------------------------------- #
# AN 6.21 — Sāmakasutta
# --------------------------------------------------------------------------- #
page(
    21, "Sāmaka", "At Sāma Village",
    vagga=VAGGA_3,
    meta_title="AN 6.21 — At Sāma Village | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sāmakasutta, opening "
        "the Sixes' third chapter when a deity reports three causes of a mendicant's decline, "
        "and the Buddha adds three more. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "In the land of the Sakyans, near the little village of Sāma, by a lotus "
                    "pond"),
        ("Speakers", "A deity, reporting to the Buddha; then the Buddha, addressing the "
                     "mendicants"),
        ("Form", "A deity's nighttime visit and report, approved by the Buddha, followed by his "
                 "own addition of three further qualities"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Deity-visit narratives reporting on mendicant conduct recur "
                              "across the Saṁyutta and its Chinese counterparts; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short narrative opening a "
                       "chapter built mostly from formulaic material"),
    ],
    why=(
        "The Sixes' third chapter opens, unusually, with a deity rather than the Buddha "
        "speaking first: a glorious being, lighting up an entire lotus pond, reports three "
        "qualities that lead a mendicant to decline &mdash; relishing work, talk, and sleep, the "
        "same trio named in AN 6.14, 6.15, and 6.17. The Buddha approves what the deity said, "
        "and the next morning adds three further qualities of his own, completing the chapter's "
        "opening six."),
    guide=[
        ("The teaching in one sentence", [
            "Six qualities lead to a mendicant's decline: relishing work, talk, and sleep "
            "(reported by a deity), and enjoying company, being hard to admonish, and having bad "
            "friends (added by the Buddha)."]),
        ("A deity as the initial teacher", [
            "It is the deity, not the Buddha, who first names the three qualities of decline "
            "&mdash; a structure this series has not yet met. The Buddha's role in that first "
            "exchange is only to approve: &ldquo;that's what that deity said, and the teacher "
            "approved.&rdquo; Only afterward, addressing the mendicants directly, does he add "
            "content of his own, framing the deity's report as essentially correct but "
            "incomplete."]),
        ("A familiar trio, extended by three more", [
            "Work, talk, and sleep are exactly the three items opening the longer six-item list "
            "of AN 6.14 and 6.15 (work, talk, sleep, company, closeness, proliferation). Here "
            "the Buddha's three additions &mdash; enjoyment of company, being hard to admonish, "
            "and having bad friends &mdash; move from personal habits to relational ones, "
            "rounding the list out to six causes of decline that span both an individual's "
            "conduct and their choice of company."]),
        ("A stern opening line", [
            "The Buddha's response to the deity's report is notably blunt: &ldquo;It's "
            "unfortunate for those of you who even the deities know are declining in skillful "
            "qualities.&rdquo; The line implies these six qualities of decline were visible "
            "enough, in at least some of the assembled mendicants, for a passing deity to "
            "notice and report on &mdash; a rare moment in this series where an outside "
            "observer's judgment prompts the teaching, rather than a question or a bare "
            "formula."]),
        ("Setting up the chapter's second discourse", [
            "AN 6.22, immediately following, restates this same six-item structure in its "
            "positive form &mdash; not what causes decline, but what prevents it &mdash; without "
            "the narrative frame of a deity's visit. Read together, the two discourses form "
            "another brief pairing of stated-negative and stated-positive, a pattern with "
            "precedent already in AN 6.11/6.12."]),
    ],
    terms=[
        ("parihāna",
         "&ldquo;decline&rdquo; &mdash; what the six qualities named in this discourse are said "
         "to lead a mendicant toward."),
        ("devatā",
         "&ldquo;deity&rdquo; &mdash; the being who visits the Buddha at night and first names "
         "three of the six qualities."),
        ("dovacassatā",
         "&ldquo;being hard to admonish&rdquo; &mdash; the second of the Buddha's three added "
         "qualities."),
        ("pāpamittatā",
         "&ldquo;having bad friends&rdquo; &mdash; the third of the Buddha's additions, closing "
         "the six-item list."),
        ("satthā anumodi",
         "&ldquo;the teacher approved&rdquo; &mdash; the discourse's phrase for the Buddha's "
         "endorsement of the deity's report, before he adds his own three qualities."),
    ],
    text_intro=(
        "The discourse in full: the deity's nighttime report, and the Buddha's three additional "
        "qualities the next morning. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Sāma Village: a deity's visit"),
        ("p", "&sect;1", "an6.21:1.1-2.7"),
        ("h3", "The Buddha's three further qualities"),
        ("p", "&sect;2", "an6.21:3.1-5.1"),
    ],
    quiz=[
        {"q": "Who first names three qualities that lead to a mendicant's decline?",
         "opts": [
             "The Buddha alone", "A deity, visiting at night, whom the Buddha then approves", "Sāriputta", "Mahākaccāna"],
         "correct": 1,
         "expl": "An unusual structure for this series — a deity teaches first, and is approved."},
        {"q": "What three qualities does the deity report?",
         "opts": [
             "Enjoying company, being hard to admonish, having bad friends",
             "Relishing work, talk, and sleep",
             "Faith, energy, and wisdom",
             "The six sense doors"],
         "correct": 1,
         "expl": "The same three items opening the longer list at AN 6.14 and 6.15."},
        {"q": "What three qualities does the Buddha add the next morning?",
         "opts": [
             "Relishing work, talk, and sleep",
             "Enjoyment of company, being hard to admonish, and having bad friends",
             "The five faculties plus liberation",
             "Seeing, listening, and acquisition"],
         "correct": 1,
         "expl": "A shift from personal habits to relational ones, completing six causes of "
                 "decline."},
        {"q": "How does the guide characterize the Buddha's response to the deity's report?",
         "opts": [
             "Dismissive — he corrects the deity outright",
             "Approving but incomplete — he endorses what was said, then adds three qualities of "
             "his own",
             "He ignores the deity entirely",
             "He questions whether the deity is trustworthy"],
         "correct": 1,
         "expl": "'That's what that deity said, and the teacher approved' — then he supplements it."},
        {"q": "What does the Buddha's opening line to the mendicants imply?",
         "opts": [
             "That the six qualities of decline are purely hypothetical",
             "That these qualities were visible enough in at least some mendicants for a passing "
             "deity to notice and report on",
             "That the deity fabricated the report",
             "That decline is impossible for any mendicant"],
         "correct": 1,
         "expl": "'It's unfortunate for those of you who even the deities know are declining...'"},
        {"q": "How does AN 6.22 relate to AN 6.21?",
         "opts": [
             "It contradicts AN 6.21's list",
             "It restates the same six-item structure in positive form — what prevents decline, "
             "rather than what causes it",
             "It is entirely unrelated in content",
             "It replaces the six qualities with an unrelated new list"],
         "correct": 1,
         "expl": "A stated-negative and stated-positive pairing, with precedent at AN 6.11/6.12."},
        {"q": "Where is AN 6.21 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "In the land of the Sakyans, near the little village of Sāma, by a lotus pond",
             "Ñātika, in the brick house",
             "Kapilavatthu, in the Banyan Tree Monastery"],
         "correct": 1,
         "expl": "A fresh, specific setting opening the chapter's third vagga."},
        {"q": "What does <em>parihāna</em> mean?",
         "opts": ["Awakening", "Decline", "Generosity", "Recollection"],
         "correct": 1,
         "expl": "What the six named qualities are said to lead a mendicant toward."},
        {"q": "How many of the six causes of decline overlap with AN 6.14/6.15's longer list?",
         "opts": [
             "None", "All six", "Three — work, talk, and sleep, the first half of AN 6.14/6.15's "
             "list", "Only one"],
         "correct": 2,
         "expl": "The deity's three items match the opening of the longer six-item list "
                 "elsewhere in this chapter's predecessor."},
        {"q": "What role does the Buddha play in the first half of this discourse?",
         "opts": [
             "He teaches the deity directly",
             "He listens and approves what the deity says, without adding content until the next "
             "morning",
             "He refuses to engage with the deity at all",
             "He asks the deity further questions on the spot"],
         "correct": 1,
         "expl": "His own addition comes only afterward, addressing the mendicants."},
    ],
    marginalia=[
        ("The deity's three", [
            "work &middot; talk &middot; sleep",
        ]),
        ("The Buddha's three", [
            "enjoying company",
            "hard to admonish",
            "bad friends",
        ]),
        ("An unusual structure", [
            "a deity teaches first,",
            "the Buddha approves,",
            "then adds his own three",
        ]),
        ("Cross-references", [
            "AN 6.14/6.15 &middot; the same trio, extended",
            "AN 6.22 &middot; next, the positive form",
        ]),
    ],
    further=[
        '<a href="%s/an6.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.22.html">AN 6.22 &middot; Non-decline</a> &mdash; next, the same '
        "structure in positive form.",
        '<a href="an-6.14.html">AN 6.14 &middot; A Good Death</a> &mdash; earlier, where work, '
        "talk, and sleep first opened a longer six-item list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.22 — Aparihāniyasutta
# --------------------------------------------------------------------------- #
page(
    22, "Aparihāniya", "Non-decline",
    vagga=VAGGA_3,
    meta_title="AN 6.22 — Non-decline | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Aparihāniyasutta, "
        "restating AN 6.21's six causes of decline in their positive form as six principles "
        "that prevent it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of six qualities, each negated or reversed from AN 6.21's six "
                 "causes of decline"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 6.21, this theme recurs across the Saṁyutta and its "
                              "Chinese counterparts; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a direct mirror of the "
                       "preceding discourse"),
    ],
    why=(
        "AN 6.22 takes AN 6.21's six causes of decline and states their opposite: not relishing "
        "work, talk, sleep, or company; being easy to admonish; and having good friends. Where "
        "AN 6.21 arrived at its list through a deity's report and the Buddha's addition, AN 6.22 "
        "states the same material directly, without narrative frame, as six principles that "
        "prevent decline rather than cause it."),
    guide=[
        ("The teaching in one sentence", [
            "Six principles prevent a mendicant's decline: not relishing work, talk, sleep, and "
            "company, being easy to admonish, and having good friends."]),
        ("A precise mirror, not a new list", [
            "Each of AN 6.22's six items is the direct negation or reversal of one item from AN "
            "6.21: not relishing work/talk/sleep/company (reversing the first four), being easy "
            "to admonish (<em>sovacassatā</em>, reversing <em>dovacassatā</em>), and having good "
            "friends (<em>kalyāṇamittatā</em>, reversing <em>pāpamittatā</em>). Nothing new is "
            "introduced; the list is constructed entirely by inversion."]),
        ("Why state the inversion at all", [
            "It might seem redundant to state the reverse of an already-given list. But doing so "
            "makes explicit what is otherwise only implied: readers are not left to infer the "
            "positive form of AN 6.21's warning for themselves. The canon's preference for "
            "stating both a warning and its positive counterpart directly, rather than trusting "
            "an audience to invert it mentally, recurs across this collection."]),
        ("Losing the narrative frame", [
            "AN 6.21 was a story: a deity's nighttime visit, the Buddha's approval, his own "
            "addition the next morning. AN 6.22 strips all of that away, presenting the same "
            "six-item structure as a bare formula with no scene at all. The content survives the "
            "loss of its narrative wrapping intact &mdash; suggesting the story in AN 6.21 was "
            "occasion, not substance."]),
        ("A pattern already familiar from this chapter's predecessor", [
            "This positive-restatement move already appeared at AN 6.11/6.12 in the previous "
            "chapter, though there the second discourse added an outcome clause rather than "
            "simply inverting the first. Here the technique is starker: pure inversion, term for "
            "term, with no elaboration beyond the reversal itself."]),
    ],
    terms=[
        ("aparihāniya",
         "&ldquo;non-declining,&rdquo; &ldquo;conducive to non-decline&rdquo; &mdash; the "
         "discourse's own title, and the quality named of all six items together."),
        ("sovacassatā",
         "&ldquo;being easy to admonish&rdquo; &mdash; reversing AN 6.21's "
         "<em>dovacassatā</em>, hard to admonish."),
        ("kalyāṇamittatā",
         "&ldquo;having good friends&rdquo; &mdash; reversing AN 6.21's "
         "<em>pāpamittatā</em>, bad friends."),
        ("kammārāmatā",
         "&ldquo;relishing work&rdquo; &mdash; the quality negated as the first item here, "
         "matching AN 6.21's first cause of decline."),
        ("saṅgaṇikārāmatā",
         "&ldquo;relishing company&rdquo; &mdash; the fourth quality negated, closing the "
         "personal-habit half of the list before the two relational items."),
    ],
    text_intro=(
        "The discourse in full: the six principles that prevent decline. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six principles that prevent decline"),
        ("p", "&sect;1", "an6.22:1.1-2.1"),
    ],
    quiz=[
        {"q": "What six principles does AN 6.22 name as preventing decline?",
         "opts": [
             "Not relishing work, talk, sleep, and company; being easy to admonish; having good "
             "friends",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "The six sense doors",
             "Seeing, listening, acquisition, training, service, recollection"],
         "correct": 0,
         "expl": "The direct inversion of AN 6.21's six causes of decline."},
        {"q": "How is AN 6.22's list constructed, according to the guide?",
         "opts": [
             "As an entirely new set of qualities unrelated to AN 6.21",
             "Entirely by inversion — each item is the direct negation or reversal of one item "
             "from AN 6.21",
             "By adding three new items to AN 6.21's original three",
             "By removing half of AN 6.21's items"],
         "correct": 1,
         "expl": "Nothing new is introduced beyond the reversal itself."},
        {"q": "What does AN 6.22 lack, compared to AN 6.21?",
         "opts": [
             "A closing formula",
             "Any narrative frame — no deity, no scene, just a bare formula",
             "Six distinct qualities",
             "Any relation to decline at all"],
         "correct": 1,
         "expl": "The content survives the loss of its narrative wrapping intact."},
        {"q": "What does the guide suggest this implies about AN 6.21's deity narrative?",
         "opts": [
             "That the deity's report was false",
             "That the story was occasion, not substance — the teaching stands independently of "
             "its narrative frame",
             "That AN 6.22 should be read before AN 6.21",
             "That deities cannot actually teach the Dhamma"],
         "correct": 1,
         "expl": "The same six-item structure holds with or without the narrative wrapping."},
        {"q": "What earlier pairing in this chapter's predecessor does the guide compare this "
              "to?",
         "opts": [
             "AN 6.5-6.7's thoroughbred triad",
             "AN 6.11/6.12 — though there the second discourse added an outcome clause rather "
             "than simply inverting the first",
             "AN 6.1/6.2's worthiness formula",
             "AN 6.9/6.10's recollections"],
         "correct": 1,
         "expl": "A similar stated-negative/stated-positive move, though executed differently."},
        {"q": "What does <em>sovacassatā</em> mean?",
         "opts": ["Hard to admonish", "Easy to admonish", "Relishing sleep", "Having bad friends"],
         "correct": 1,
         "expl": "The direct reversal of AN 6.21's dovacassatā."},
        {"q": "Is a setting stated for AN 6.22?",
         "opts": ["Yes, near Sāma village", "No — none is stated", "Yes, at Isipatana", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare formula with no scene at all."},
        {"q": "What does <em>kalyāṇamittatā</em> mean?",
         "opts": ["Bad friendship", "Good friendship", "Solitary practice", "Hard to admonish"],
         "correct": 1,
         "expl": "The sixth and final item, reversing pāpamittatā."},
        {"q": "How many of the six items concern personal habits versus relational qualities?",
         "opts": [
             "All six concern personal habits",
             "Four personal-habit items (work, talk, sleep, company), followed by two relational "
             "items (easy to admonish, good friends)",
             "All six concern relationships with other people",
             "Three and three, evenly split"],
         "correct": 1,
         "expl": "Matching the structure of AN 6.21's six causes of decline."},
        {"q": "What comes next in the chapter, after this pair on decline and non-decline?",
         "opts": [
             "AN 6.23, on six terms describing the danger of sensual pleasures",
             "The chapter ends here",
             "A return to the thoroughbred simile",
             "AN 6.30, skipping ahead"],
         "correct": 0,
         "expl": "A shift to a different, more technical subject."},
    ],
    marginalia=[
        ("Six inversions", [
            "not relishing: work,",
            "talk, sleep, company",
            "+ easy to admonish,",
            "good friends",
        ]),
        ("Pure reversal", [
            "no new content —",
            "each item negates",
            "one from AN 6.21",
        ]),
        ("Frame stripped away", [
            "no deity, no scene,",
            "just the bare formula",
        ]),
        ("Cross-references", [
            "AN 6.21 &middot; previous, the causes",
            "AN 6.23 &middot; next, terms for danger",
        ]),
    ],
    further=[
        '<a href="%s/an6.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.21.html">AN 6.21 &middot; At Sāma Village</a> &mdash; previous, the same '
        "six qualities stated as causes of decline.",
        '<a href="an-6.23.html">AN 6.23 &middot; Dangers</a> &mdash; next, six terms for the '
        "danger of sensual pleasures.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.23 — Bhayasutta
# --------------------------------------------------------------------------- #
page(
    23, "Bhaya", "Dangers",
    vagga=VAGGA_3,
    meta_title="AN 6.23 — Dangers | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bhayasutta, which "
        "gives six terms — danger, suffering, disease, boil, chain, and bog — as synonyms for "
        "sensual pleasures, and explains why each name fits. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Six terms named in a row, a single explanation applied to all six, and a "
                 "closing pair of verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Synonym-lists for the danger of sensual pleasure recur across "
                              "the Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but each of the six "
                       "terms is doing real argumentative work, not simply piling up synonyms"),
    ],
    why=(
        "AN 6.23 is unusual among this chapter's six-item lists: rather than naming six "
        "qualities, practices, or occasions, it names six words &mdash; danger, suffering, "
        "disease, boil, chain, and bog &mdash; and argues that all six are legitimate terms for "
        "one thing, sensual pleasures. A single explanation, repeated for all six, does the "
        "argumentative work: someone caught by sensual greed is not freed from any of these six "
        "conditions, in this life or lives to come, and so all six names genuinely apply."),
    guide=[
        ("The teaching in one sentence", [
            "Danger, suffering, disease, boil, chain (or snare), and bog are all terms for "
            "sensual pleasures, because someone besotted by sensual greed and shackled by "
            "lustful desire is not freed from any of these six conditions, in this life or "
            "lives to come."]),
        ("Six words, one argument", [
            "The discourse does not explain each term separately with its own distinct "
            "rationale. It states all six terms, then gives a single explanation that covers "
            "all six at once: entanglement in sensual desire keeps a person unfree from danger, "
            "unfree from suffering, unfree from disease, and so on through the whole list. The "
            "six words function less as six separate insights than as six angles on one claim, "
            "repeated with variation for emphasis."]),
        ("Words chosen for their ordinary force", [
            "None of the six terms is a specialized doctrinal term coined for this discourse; "
            "each is a plain word for something anyone would want to avoid &mdash; a boil, a "
            "chain, a bog to be mired in. The argument's persuasive weight rests on this "
            "ordinariness: rather than asserting sensual pleasure is bad by definition, the "
            "discourse claims it deserves the same visceral aversion a listener already feels "
            "toward disease or a suppurating wound."]),
        ("A change of state, not a permanent verdict", [
            "The closing verses describe not a condemnation without exit but a contrast between "
            "two conditions: &ldquo;ordinary people&rdquo; remain attached to what these six "
            "words describe, while &ldquo;the unattached,&rdquo; seeing the danger in grasping, "
            "are freed with the ending of birth and death. The six terms describe a condition "
            "that can be left, not an unalterable feature of sensual experience itself."]),
        ("A different kind of six-item list", [
            "Compared to the qualities, practices, and occasions named elsewhere in this "
            "chapter, AN 6.23's list is unusual in being a list of words rather than a list of "
            "things to do or cultivate. Its place among the Sixes depends only on there being "
            "six terms offered, not on any six-fold structure in the underlying teaching about "
            "sensual pleasure itself."]),
    ],
    terms=[
        ("kāma",
         "&ldquo;sensual pleasure,&rdquo; &ldquo;sensuality&rdquo; &mdash; what all six terms in "
         "this discourse are said to name."),
        ("bhaya",
         "&ldquo;danger,&rdquo; &ldquo;fear&rdquo; &mdash; the first of the six terms, and the "
         "discourse's own title."),
        ("gaṇḍa",
         "&ldquo;boil&rdquo; &mdash; the fourth term, chosen for the visceral aversion a boil "
         "ordinarily provokes."),
        ("paṅka",
         "&ldquo;bog,&rdquo; &ldquo;mire&rdquo; &mdash; the sixth and final term, an image of "
         "being stuck and slowly sinking."),
        ("anupāya",
         "not itself a term from this discourse, but the state described in its closing verses "
         "as reached by &ldquo;the unattached,&rdquo; freed from grasping and its consequences."),
    ],
    text_intro=(
        "The discourse in full: the six terms, the shared explanation, and the closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six terms for sensual pleasures"),
        ("p", "&sect;1", "an6.23:1.1-1.6"),
        ("h3", "Why these terms apply"),
        ("p", "&sect;2", "an6.23:2.1-2.8"),
        ("h3", "The closing verses"),
        ("p", "&sect;3", "an6.23:3.1-5.4"),
    ],
    quiz=[
        {"q": "What six terms does AN 6.23 give as synonyms for sensual pleasures?",
         "opts": [
             "Danger, suffering, disease, boil, chain (snare), and bog",
             "Faith, energy, mindfulness, immersion, wisdom, and liberation",
             "Work, talk, sleep, company, closeness, and proliferation",
             "The six sense doors"],
         "correct": 0,
         "expl": "Bhaya, dukkha, roga, gaṇḍa, and so on."},
        {"q": "What single explanation does the discourse give for all six terms applying?",
         "opts": [
             "Each term has its own distinct, separately argued rationale",
             "One explanation covers all six: someone besotted by sensual greed is not freed "
             "from any of these six conditions, in this life or lives to come",
             "The terms are simply asserted with no explanation given",
             "Different deities gave different explanations for each term"],
         "correct": 1,
         "expl": "The six words function as six angles on one claim, not six separate insights."},
        {"q": "According to the guide, why were these six particular words chosen?",
         "opts": [
             "They are specialized doctrinal terms unique to this discourse",
             "They are plain, ordinary words for things anyone would want to avoid, drawing on "
             "visceral aversion already felt toward disease or a wound",
             "They were chosen at random to fill out the number six",
             "They are all synonyms for physical illness only"],
         "correct": 1,
         "expl": "The argument's force rests on the words' ordinariness, not technical precision."},
        {"q": "What do the closing verses describe, according to the guide?",
         "opts": [
             "A permanent, unalterable feature of sensual experience with no exit possible",
             "A contrast between two conditions — ordinary people remaining attached, and the "
             "unattached being freed with the ending of birth and death",
             "A condemnation of all pleasure of any kind",
             "A description only of monastic life, with no relevance to laypeople"],
         "correct": 1,
         "expl": "The six terms describe a condition that can be left, not a fixed verdict."},
        {"q": "How does the guide characterize this list compared to others in the chapter?",
         "opts": [
             "Identical in structure to every other six-item list in this chapter",
             "Unusual — a list of words rather than qualities, practices, or occasions; its "
             "place among the Sixes depends only on there being six terms offered",
             "It is not actually a list of six items at all",
             "It concerns meditation technique exclusively, like AN 6.24"],
         "correct": 1,
         "expl": "A different kind of six-fold structure from the rest of the chapter."},
        {"q": "What does <em>gaṇḍa</em> mean?",
         "opts": ["Chain", "Boil", "Bog", "Danger"],
         "correct": 1,
         "expl": "The fourth of the six terms, chosen for its visceral force."},
        {"q": "What does <em>paṅka</em> mean?",
         "opts": ["Disease", "Suffering", "Bog, mire", "Danger"],
         "correct": 2,
         "expl": "The sixth and final term, an image of being stuck and sinking."},
        {"q": "Is a setting stated for AN 6.23?",
         "opts": ["Yes, at Sāma village", "No — none is stated", "Yes, at Isipatana", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare formula continuing this chapter's pattern."},
        {"q": "What is <em>kāma</em>?",
         "opts": [
             "A specific meditative attainment",
             "Sensual pleasure, sensuality — what all six terms in this discourse name",
             "A synonym for the Saṅgha",
             "A type of monastic robe"],
         "correct": 1,
         "expl": "The single subject all six words are claimed to genuinely describe."},
        {"q": "What does the guide say about who is 'freed' according to the closing verses?",
         "opts": [
             "No one can ever be freed from what these six terms describe",
             "The unattached, who see the danger in grasping and are freed with the ending of "
             "birth and death",
             "Only deities are capable of such freedom",
             "Freedom is achieved automatically with age"],
         "correct": 1,
         "expl": "A stated path out of the condition the six terms describe, not a closed verdict."},
    ],
    marginalia=[
        ("The six terms", [
            "danger &middot; suffering",
            "disease &middot; boil",
            "chain &middot; bog",
        ]),
        ("One shared reason", [
            "besotted by desire,",
            "unfree from all six —",
            "in this life and beyond",
        ]),
        ("Ordinary words, chosen", [
            "not technical jargon —",
            "visceral, familiar",
            "aversion, redirected",
        ]),
        ("Cross-references", [
            "AN 6.22 &middot; previous, non-decline",
            "AN 6.24 &middot; next, immersion and Himalaya",
        ]),
    ],
    further=[
        '<a href="%s/an6.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.24.html">AN 6.24 &middot; The Himalaya</a> &mdash; next, six qualities of '
        "skill in immersion.",
        '<a href="an-6.22.html">AN 6.22 &middot; Non-decline</a> &mdash; previous, a different '
        "register of six-item list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.24 — Himavantasutta
# --------------------------------------------------------------------------- #
page(
    24, "Himavanta", "The Himalaya",
    vagga=VAGGA_3,
    meta_title="AN 6.24 — The Himalaya | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Himavantasutta, which "
        "names six kinds of skill in immersion powerful enough, the Buddha says, to shatter the "
        "Himalaya itself. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single hyperbolic claim, then a bare list of six technical skills"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The six kinds of skill in immersion (samādhi) named here recur "
                              "in related technical form across the Chinese Āgamas and "
                              "Abhidharma literature; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, but each of the six "
                       "terms names a distinct, specific meditative skill worth distinguishing "
                       "from the others"),
    ],
    why=(
        "AN 6.24 opens on hyperbole: a mendicant with six qualities could shatter the Himalaya, "
        "the king of mountains &mdash; and the discourse immediately undercuts the extravagance "
        "of that image with a dry aside, &ldquo;let alone this wretched ignorance,&rdquo; "
        "implying that dismantling ignorance is, if anything, the lesser task. What follows is a "
        "compact taxonomy of skill in immersion: not simply the ability to enter absorption, but "
        "six distinct competencies covering the whole arc of working with it."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant skilled in entering immersion, remaining in it, emerging from it, "
            "readying the mind for it, knowing its proper territory, and directing a mind "
            "purified by it toward a goal, could &mdash; the discourse claims &mdash; shatter "
            "the Himalaya itself, let alone something as comparatively minor as ignorance."]),
        ("Six competencies, not one ability", [
            "&ldquo;Skill in immersion&rdquo; might suggest a single capacity, but the "
            "discourse breaks it into six distinguishable skills: entering (<em>samāpatti"
            "</em>), remaining steady once in (<em>ṭhiti</em>), emerging cleanly "
            "(<em>vuṭṭhāna</em>), readiness or fitness for it (<em>kallita</em>), knowing its "
            "proper scope or territory (<em>gocara</em>), and directing a purified mind toward "
            "a chosen aim (<em>abhinīhāra</em>). A meditator might have some of these "
            "competencies without others &mdash; able to enter absorption easily, for instance, "
            "but not to emerge from it cleanly, or not to direct the resulting clarity toward a "
            "specific purpose."]),
        ("What the mountain-shattering claim is doing", [
            "This is not a literal claim about geology. The Himalaya functions here as the "
            "canon's stock image of maximum physical immovability &mdash; the largest, most "
            "fixed thing a listener could imagine &mdash; used precisely so the discourse can "
            "then deflate it: shattering something that solid is treated as a lesser feat than "
            "overturning ignorance, the actual target these six skills serve. The hyperbole "
            "exists to be undercut, not to be taken at face value."]),
        ("A technical vocabulary this series has not yet needed", [
            "Earlier discourses on immersion in this series (the faculties and powers at AN "
            "6.3&ndash;6.4, or immersion as one item within larger lists) treated it as a single "
            "named quality among others. AN 6.24 is the first discourse in this series to open "
            "immersion itself up into component skills, treating meditative competence as "
            "something with distinguishable parts rather than a single yes-or-no capacity."]),
        ("A short discourse with no closing formula", [
            "Unlike most of this chapter's list-discourses, AN 6.24 closes immediately after "
            "restating its opening claim, with no further explanation of the six terms, no "
            "quiz-friendly closing verse, and no attached worthiness formula. The six terms are "
            "left, deliberately or simply because the source text is this short, to stand as "
            "bare technical vocabulary for a reader to carry forward."]),
    ],
    terms=[
        ("samādhissa samāpattikusalo",
         "&ldquo;skilled in entering immersion&rdquo; &mdash; the first of the six, the ability "
         "to enter absorption."),
        ("samādhissa ṭhitikusalo",
         "&ldquo;skilled in remaining in immersion&rdquo; &mdash; the second, sustaining "
         "steadiness once absorbed."),
        ("samādhissa vuṭṭhānakusalo",
         "&ldquo;skilled in emerging from immersion&rdquo; &mdash; the third, the ability to "
         "come out of absorption cleanly and at will."),
        ("samādhissa gocarakusalo",
         "&ldquo;skilled in the territory of immersion&rdquo; &mdash; the fifth, knowing "
         "immersion's proper scope or domain."),
        ("samādhissa abhinīhārakusalo",
         "&ldquo;skilled in projecting the mind purified by immersion&rdquo; &mdash; the sixth "
         "and final skill, directing the resulting clarity toward a chosen aim."),
    ],
    text_intro=(
        "The discourse in full: the mountain-shattering claim, and the six skills in immersion. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Shattering the Himalaya"),
        ("p", "&sect;1", "an6.24:1.1-1.4"),
    ],
    quiz=[
        {"q": "What does the discourse claim a mendicant with six qualities could shatter?",
         "opts": [
             "A large boulder",
             "The Himalaya, the king of mountains — 'let alone this wretched ignorance'",
             "A city wall",
             "An iron chain"],
         "correct": 1,
         "expl": "Hyperbole used to deflate itself — ignorance is the actual, comparatively "
                 "lesser target."},
        {"q": "What six skills in immersion does the discourse name?",
         "opts": [
             "Entering, remaining, emerging, positivity/readiness, territory, and projecting the "
             "purified mind",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "Seeing, listening, acquisition, training, service, recollection",
             "The four brahmavihāra plus two further liberations"],
         "correct": 0,
         "expl": "Samāpatti, ṭhiti, vuṭṭhāna, kallita, gocara, abhinīhāra."},
        {"q": "According to the guide, why might a meditator have some of these six skills "
              "without others?",
         "opts": [
             "The six skills are identical and always develop together",
             "They are distinguishable competencies — one might enter absorption easily but not "
             "emerge cleanly, or not direct the resulting clarity toward a purpose",
             "Only fully awakened beings can have any of the six",
             "The discourse denies this is possible"],
         "correct": 1,
         "expl": "A taxonomy of distinct skills, not a single unified ability."},
        {"q": "What function does the Himalaya image serve, according to the guide?",
         "opts": [
             "A literal geological claim the discourse expects readers to believe",
             "The canon's stock image of maximum physical immovability, used precisely so it can "
             "be deflated by comparison to overturning ignorance",
             "A reference to an actual event in the Buddha's life",
             "A warning against mountain travel"],
         "correct": 1,
         "expl": "The hyperbole exists to be undercut, not taken at face value."},
        {"q": "How does AN 6.24 treat immersion differently from earlier discourses in this "
              "series?",
         "opts": [
             "It is the first discourse in this series to open immersion into distinguishable "
             "component skills, rather than treating it as one named quality among others",
             "It denies immersion has any value",
             "It treats immersion identically to how AN 6.3-6.4 treated it",
             "It replaces immersion with a different concept entirely"],
         "correct": 0,
         "expl": "A finer-grained taxonomy than the faculties/powers pairing earlier in this "
                 "chapter's predecessor."},
        {"q": "What does <em>vuṭṭhānakusalo</em> mean?",
         "opts": [
             "Skilled in entering immersion",
             "Skilled in emerging from immersion",
             "Skilled in the territory of immersion",
             "Skilled in remaining in immersion"],
         "correct": 1,
         "expl": "The third of the six skills, the ability to come out of absorption cleanly."},
        {"q": "What is notable about how AN 6.24 closes, compared to most of this chapter's "
              "discourses?",
         "opts": [
             "It ends with an elaborate closing verse",
             "It closes immediately after restating its opening claim, with no further "
             "explanation, quiz-friendly verse, or attached worthiness formula",
             "It ends with a dialogue between two mendicants",
             "It closes with the fourfold worthiness formula from AN 6.1"],
         "correct": 1,
         "expl": "A notably terse discourse, even by this chapter's standards."},
        {"q": "Is a setting stated for AN 6.24?",
         "opts": ["Yes, near Sāma village", "No — none is stated", "Yes, at Isipatana", "Yes, at Kapilavatthu"],
         "correct": 1,
         "expl": "Continuing this chapter's frequent bare-formula pattern."},
        {"q": "What does <em>abhinīhāra</em> mean in this context?",
         "opts": [
             "Entering absorption",
             "Directing a mind purified by immersion toward a chosen aim",
             "Remaining steady in absorption",
             "The territory or scope of immersion"],
         "correct": 1,
         "expl": "The sixth and final skill, closing the list."},
        {"q": "What is the discourse's actual target, despite its dramatic opening image?",
         "opts": [
             "Literal mountains", "Ignorance (avijjā)", "Sensual pleasure", "Physical illness"],
         "correct": 1,
         "expl": "'Let alone this wretched ignorance' names the real, comparatively lesser task."},
    ],
    marginalia=[
        ("Six skills in immersion", [
            "entering &middot; remaining",
            "emerging &middot; readiness",
            "territory &middot; projecting",
        ]),
        ("A deflated hyperbole", [
            "shatter the Himalaya —",
            "'let alone ignorance',",
            "the real, lesser target",
        ]),
        ("Distinct competencies", [
            "one skill without",
            "the others is possible —",
            "not a single ability",
        ]),
        ("Cross-references", [
            "AN 6.3/6.4 &middot; faculties and powers",
            "AN 6.25 &middot; next, recollection again",
        ]),
    ],
    further=[
        '<a href="%s/an6.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.25.html">AN 6.25 &middot; Topics for Recollection</a> &mdash; next, a '
        "third telling of the six recollections met earlier at AN 6.9-6.10.",
        '<a href="an-6.23.html">AN 6.23 &middot; Dangers</a> &mdash; previous, a different '
        "register of six-item teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.25 — Anussatiṭṭhānasutta
# --------------------------------------------------------------------------- #
page(
    25, "Anussatiṭṭhāna", "Topics for Recollection",
    vagga=VAGGA_3,
    meta_title="AN 6.25 — Topics for Recollection | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for this chapter's own "
        "Anussatiṭṭhānasutta, a third telling of the six recollections already met at AN "
        "6.9-6.10, self-contained and closing on how they purify a mind of greed. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The same six recollections as AN 6.9/6.10, stated here as one self-contained "
                 "discourse rather than split into a bare list and its expansion"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "As with AN 6.9/6.10, the six recollections recur widely across "
                              "the Chinese Āgamas and later Mahāyāna devotional practice; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; largely familiar material "
                       "from earlier in this nipāta, worth reading for what is added, not just "
                       "repeated"),
    ],
    why=(
        "This is the third time this series has encountered the six recollections &mdash; of "
        "the Buddha, the teaching, the Saṅgha, ethics, generosity, and the deities &mdash; after "
        "AN 6.9's bare list and AN 6.10's full expansion via Mahānāma's question. AN 6.25 gives "
        "them a third telling, this time as one self-contained discourse with no interlocutor "
        "and no bare-list companion of its own. It is not identical to AN 6.10, though "
        "&mdash; it closes each recollection differently, on how the practice purifies a mind "
        "of greed, rather than on the five-step chain from joy to immersion that closed AN "
        "6.10's account."),
    guide=[
        ("The teaching in one sentence", [
            "There are six topics for recollection &mdash; the Buddha, the teaching, the "
            "Saṅgha, one's own ethics, one's own generosity, and the deities &mdash; each of "
            "which, recollected, leaves the mind free of greed, hate, and delusion and unswerving, "
            "having left greed behind."]),
        ("What is genuinely the same as AN 6.9/6.10", [
            "The six topics themselves, their order, and the content of each formula &mdash; "
            "the nine-epithet description of the Buddha, the four-part description of the "
            "teaching, and so on &mdash; match AN 6.10 closely. A reader who has already read "
            "AN 6.10 will recognize this material immediately rather than encountering it fresh."]),
        ("What is genuinely different, checked directly against the Pāli", [
            "Unlike AN 6.10, which closed its account of Buddha- and deity-recollection with "
            "the five-step chain from joy through rapture, tranquility, and bliss to immersion, "
            "AN 6.25 closes each recollection instead with: &ldquo;their mind is quite "
            "unswerving. They've left behind greed; they're free of it and have risen above "
            "it. 'Greed' is a term for the five kinds of sensual stimulation. Relying on this, "
            "some sentient beings are purified in this way.&rdquo; This is a different closing "
            "formula, not a paraphrase of AN 6.10's, and this guide follows its own earlier "
            "caution against assuming similar-sounding formulas are identical without checking "
            "directly."]),
        ("A discourse complete in itself", [
            "Where AN 6.9 was deliberately a bare list awaiting AN 6.10's expansion, AN 6.25 "
            "needs no companion; it states the six topics and their effect fully, in a single "
            "self-contained teaching, with no named interlocutor prompting it and no second "
            "discourse required to complete it."]),
        ("A third telling still to come a fourth time", [
            "AN 6.26, immediately following, gives these same six recollections yet again "
            "&mdash; a fourth telling in this nipāta alone, this time spoken by Mahākaccāna as "
            "praise for the Buddha's teaching, with its own distinct addition not present here "
            "or at AN 6.9/6.10."]),
    ],
    terms=[
        ("anussatiṭṭhāna",
         "&ldquo;topic for recollection&rdquo; &mdash; the discourse's own title, shared with "
         "AN 6.9."),
        ("avecappasanna",
         "not directly named in this discourse's English but implicit in &ldquo;quite "
         "unswerving&rdquo; &mdash; confirmed confidence, based directly on what has been "
         "recollected."),
        ("kāmaguṇa",
         "&ldquo;kinds of sensual stimulation&rdquo; &mdash; what this discourse specifies "
         "&ldquo;greed&rdquo; is a term for, in its distinctive closing clause."),
        ("visujjhanti",
         "&ldquo;are purified&rdquo; &mdash; the verb closing this discourse's account of each "
         "recollection, not present in AN 6.10's closing formula."),
        ("buddhānussati",
         "recollection of the Buddha &mdash; the first of the six, its nine-epithet formula "
         "matching AN 6.10 closely."),
    ],
    text_intro=(
        "The discourse in full: the six recollections, each closing on how it purifies a mind "
        "of greed. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Recollection of the Buddha"),
        ("p", "&sect;1", "an6.25:1.1-1.8"),
        ("h3", "Recollection of the teaching"),
        ("p", "&sect;2", "an6.25:2.1-2.3"),
        ("h3", "Recollection of the Saṅgha"),
        ("p", "&sect;3", "an6.25:3.1-3.3"),
        ("h3", "Recollection of ethics"),
        ("p", "&sect;4", "an6.25:4.1-4.2"),
        ("h3", "Recollection of generosity"),
        ("p", "&sect;5", "an6.25:5.1-5.4"),
        ("h3", "Recollection of the deities, and the conclusion"),
        ("p", "&sect;6", "an6.25:6.1-8.1"),
    ],
    quiz=[
        {"q": "How many times has this series now encountered the six recollections, counting "
              "this discourse?",
         "opts": ["Once", "Twice", "A third time, after AN 6.9's bare list and AN 6.10's "
                  "expansion", "A fourth time"],
         "correct": 2,
         "expl": "AN 6.26, immediately following, will make it a fourth."},
        {"q": "What genuinely matches between this discourse and AN 6.10?",
         "opts": [
             "Nothing at all — they are unrelated lists",
             "The six topics themselves, their order, and the content of each recollection "
             "formula, such as the nine-epithet description of the Buddha",
             "Only the setting matches",
             "Only the closing clause matches"],
         "correct": 1,
         "expl": "A reader of AN 6.10 will recognize this core material immediately."},
        {"q": "What is genuinely different about this discourse's closing formula, checked "
              "directly against the source?",
         "opts": [
             "Nothing — it is a word-for-word repeat of AN 6.10's closing",
             "It closes on purification from greed and names greed 'a term for the five kinds of "
             "sensual stimulation,' rather than AN 6.10's five-step chain from joy to immersion",
             "It adds a sixth recollection not present in AN 6.10",
             "It removes the recollection of the deities entirely"],
         "correct": 1,
         "expl": "A distinct closing formula, verified directly rather than assumed from "
                 "surface similarity."},
        {"q": "What caution does the guide explicitly apply to itself here?",
         "opts": [
             "None — it assumes the two discourses are identical",
             "Its own earlier caution against assuming similar-sounding formulas are identical "
             "without checking directly against the Pāli",
             "A caution against ever comparing two discourses",
             "A caution that recollection practices are ineffective"],
         "correct": 1,
         "expl": "Consistent with the lesson already applied elsewhere in this series about "
                 "not conflating formulas that merely sound alike."},
        {"q": "Does AN 6.25 require a companion discourse to complete its teaching, unlike AN "
              "6.9?",
         "opts": [
             "Yes, it requires AN 6.26 to be complete",
             "No — it is a discourse complete in itself, stating the six topics and their "
             "effect fully with no named interlocutor",
             "Yes, it requires AN 6.10",
             "It is deliberately left incomplete"],
         "correct": 1,
         "expl": "Unlike AN 6.9's bare list awaiting AN 6.10's expansion."},
        {"q": "What does <em>kāmaguṇa</em> mean, as used in this discourse's closing clause?",
         "opts": [
             "A term for ethical precepts",
             "Kinds of sensual stimulation — what 'greed' is specified as a term for",
             "A term for the deities",
             "A meditative attainment"],
         "correct": 1,
         "expl": "Part of this discourse's distinctive closing formula, not found in AN 6.10's."},
        {"q": "Who speaks AN 6.25?",
         "opts": ["Sāriputta", "The Buddha", "Mahākaccāna", "Ānanda"],
         "correct": 1,
         "expl": "Unlike AN 6.26, immediately following, which is spoken by Mahākaccāna."},
        {"q": "Is a setting stated for AN 6.25?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Kapilavatthu", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "Continuing this chapter's bare-formula pattern."},
        {"q": "What comes immediately after AN 6.25?",
         "opts": [
             "AN 6.26, a fourth telling of the same six recollections, spoken by Mahākaccāna",
             "AN 6.30, skipping ahead",
             "The chapter ends here",
             "A return to the thoroughbred simile"],
         "correct": 0,
         "expl": "This nipāta returns to the six recollections yet again, with a new speaker and "
                 "a new addition."},
        {"q": "How many recollections does this discourse name in total?",
         "opts": ["Five", "Six", "Seven", "Ten"],
         "correct": 1,
         "expl": "The Buddha, the teaching, the Saṅgha, ethics, generosity, and the deities."},
    ],
    marginalia=[
        ("Same six topics", [
            "the Buddha &middot; the teaching",
            "the Saṅgha &middot; ethics",
            "generosity &middot; the deities",
        ]),
        ("A different closing", [
            "not AN 6.10's joy-to-",
            "immersion chain — instead,",
            "purification from greed",
        ]),
        ("Checked, not assumed", [
            "similar-sounding ≠",
            "identical — verified",
            "against the Pāli directly",
        ]),
        ("Cross-references", [
            "AN 6.9/6.10 &middot; the first telling",
            "AN 6.26 &middot; next, a fourth telling",
        ]),
    ],
    further=[
        '<a href="%s/an6.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.26.html">AN 6.26 &middot; With Mahākaccāna</a> &mdash; next, a fourth '
        "telling with its own distinct addition.",
        '<a href="an-6.10.html">AN 6.10 &middot; With Mahānāma</a> &mdash; the first full '
        "expansion of these six recollections, for direct comparison.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.26 — Mahākaccānasutta
# --------------------------------------------------------------------------- #
page(
    26, "Mahākaccāna", "With Mahākaccāna",
    vagga=VAGGA_3,
    meta_title="AN 6.26 — With Mahākaccāna | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahākaccānasutta, a "
        "fourth telling of the six recollections, framed by Mahākaccāna as praise for the "
        "Buddha and adding a space-like heart to two of the six. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Mahākaccāna, addressing the mendicants"),
        ("Form", "An opening exclamation of wonder, the six recollections restated, and a "
                 "closing repetition of the same exclamation"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "As with AN 6.9/6.10 and AN 6.25, the six recollections recur "
                              "widely across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the fourth appearance of "
                       "familiar material, worth reading for its distinctive framing and one "
                       "genuine addition"),
    ],
    why=(
        "This is the fourth time this series has met the six recollections in this nipāta "
        "alone, and its framing is the most distinctive yet: Mahākaccāna, not the Buddha, "
        "speaks, opening and closing with an exclamation of wonder at how the Buddha &ldquo;has "
        "found an opening amid confinement&rdquo; in these six practices. And unlike AN 6.9, "
        "6.10, or 6.25, this version adds one genuinely new element, checked directly against "
        "the text: for the recollections of the Buddha and of the deities, the practitioner is "
        "said to meditate &ldquo;with a heart just like space, abundant, expansive, limitless, "
        "free of enmity and ill will.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "Mahākaccāna praises the six recollections &mdash; of the Buddha, the teaching, the "
            "Saṅgha, ethics, generosity, and the deities &mdash; as an opening the Buddha found "
            "amid confinement, restating them with an added space-like quality of heart for two "
            "of the six."]),
        ("Praise, not instruction", [
            "Unlike every earlier telling of these six recollections, this discourse is framed "
            "as one senior disciple's declaration of wonder to his peers, not as teaching handed "
            "down from the Buddha in response to a question. Mahākaccāna's opening and closing "
            "lines &mdash; &ldquo;it's incredible, reverends, it's amazing&rdquo; &mdash; bracket "
            "the entire recitation, turning what elsewhere reads as instruction into testimony."]),
        ("&lsquo;An opening amid confinement&rsquo;", [
            "Mahākaccāna's own description of what these six recollections accomplish is worth "
            "pausing on: not merely useful practices, but something the Buddha &ldquo;found&rdquo; "
            "&mdash; an opening, a way out, discovered within what would otherwise be a closed "
            "and confining situation. This image is not present in AN 6.9, 6.10, or 6.25's "
            "framing of the same six topics, and it recasts recollection as a specific kind of "
            "discovery rather than a general-purpose calming technique."]),
        ("The one genuine addition, verified against the Pāli", [
            "For the recollections of the Buddha and of the deities &mdash; but not for the "
            "teaching, the Saṅgha, ethics, or generosity &mdash; this version adds: &ldquo;that "
            "noble disciple meditates with a heart just like space, abundant, expansive, "
            "limitless, free of enmity and ill will.&rdquo; This phrase does not appear in AN "
            "6.9, 6.10, or 6.25's accounts of these same recollections. Its selective placement, "
            "on the first and last of the six rather than all of them, mirrors AN 6.10's own "
            "structure, where only the Buddha- and deity-recollections received the full "
            "five-step chain while the middle four were elided."]),
        ("Four tellings, four different closings", [
            "Set beside AN 6.9's bare list, AN 6.10's five-step chain from joy to immersion, and "
            "AN 6.25's purification-from-greed formula, this fourth telling's space-like-heart "
            "addition makes clear that &ldquo;the six recollections&rdquo; in this nipāta is not "
            "one fixed text repeated four times, but one core list dressed in four distinct "
            "framings and closings across four separate discourses."]),
    ],
    terms=[
        ("ākāsasama",
         "&ldquo;just like space&rdquo; &mdash; this discourse's distinctive addition, "
         "describing the heart cultivated through Buddha- and deity-recollection here."),
        ("abbhokāsakato",
         "not a term from this discourse directly, but the general sense of "
         "&ldquo;opened out&rdquo; that Mahākaccāna's own image of &ldquo;an opening amid "
         "confinement&rdquo; evokes."),
        ("acchariyaṁ abbhutaṁ",
         "&ldquo;incredible, amazing&rdquo; &mdash; Mahākaccāna's opening and closing "
         "exclamation, bracketing the entire discourse."),
        ("okāsādhigamo",
         "&ldquo;found an opening&rdquo; &mdash; Mahākaccāna's description of what the Buddha "
         "achieved &ldquo;amid confinement&rdquo; through these six recollections."),
        ("anussatiṭṭhāna",
         "&ldquo;topic for recollection&rdquo; &mdash; the shared term across all four tellings "
         "of this list in this nipāta."),
    ],
    text_intro=(
        "The discourse in full: Mahākaccāna's praise, the six recollections with the space-like "
        "heart addition, and his closing exclamation repeated. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Mahākaccāna's opening exclamation"),
        ("p", "&sect;1", "an6.26:1.1-1.7"),
        ("h3", "Recollection of the Buddha"),
        ("p", "&sect;2", "an6.26:2.1-2.8"),
        ("h3", "Recollection of the teaching, the Saṅgha, ethics, and generosity"),
        ("p", "&sect;3", "an6.26:3.1-6.4"),
        ("h3", "Recollection of the deities, and the closing exclamation"),
        ("p", "&sect;4", "an6.26:7.1-8.2"),
    ],
    quiz=[
        {"q": "Who speaks AN 6.26?",
         "opts": ["The Buddha", "Mahākaccāna, addressing the mendicants", "Sāriputta", "Ānanda"],
         "correct": 1,
         "expl": "The fourth telling of the six recollections in this nipāta, and the first "
                 "framed as praise rather than instruction."},
        {"q": "How is this discourse framed, compared to AN 6.9, 6.10, and 6.25?",
         "opts": [
             "Identically, as direct teaching from the Buddha",
             "As one senior disciple's declaration of wonder to his peers, bracketed by "
             "'incredible... amazing', turning the recitation into testimony rather than "
             "instruction",
             "As a formal debate between two mendicants",
             "As a silent meditation with no spoken content"],
         "correct": 1,
         "expl": "A distinctive frame not present in the three earlier tellings."},
        {"q": "What does Mahākaccāna say the Buddha 'found' through these six recollections?",
         "opts": [
             "A new monastery site",
             "An opening amid confinement",
             "A cure for physical illness",
             "A new set of ethical precepts"],
         "correct": 1,
         "expl": "An image not present in the earlier framings of the same six topics."},
        {"q": "What genuine addition does this telling make to two of the six recollections, "
              "verified directly against the source?",
         "opts": [
             "A seventh recollection not found elsewhere",
             "For the Buddha- and deity-recollections specifically, meditating 'with a heart "
             "just like space, abundant, expansive, limitless, free of enmity and ill will'",
             "A requirement to fast before recollecting",
             "A warning against practicing more than one recollection per day"],
         "correct": 1,
         "expl": "Not present in AN 6.9, 6.10, or 6.25's accounts of the same recollections."},
        {"q": "Which recollections receive this space-like-heart addition?",
         "opts": [
             "All six equally",
             "Only the Buddha- and deity-recollections — the first and last of the six, not the "
             "middle four",
             "Only the middle four",
             "None — this is a misreading"],
         "correct": 1,
         "expl": "Mirroring AN 6.10's own structure, where only the first and last received full "
                 "treatment."},
        {"q": "What does the guide conclude about 'the six recollections' across these four "
              "discourses?",
         "opts": [
             "It is one fixed text, repeated identically four times",
             "It is one core list of six topics dressed in four distinct framings and closings "
             "across four separate discourses",
             "The four tellings actually name different topics entirely",
             "Only one of the four tellings is considered authentic"],
         "correct": 1,
         "expl": "A shared core, varied treatment — verified by direct comparison rather than "
                 "assumed."},
        {"q": "What does <em>acchariyaṁ abbhutaṁ</em> mean?",
         "opts": [
             "'It is forbidden'", "'Incredible, amazing'", "'Please explain further'", "'I "
             "disagree'"],
         "correct": 1,
         "expl": "Mahākaccāna's opening and closing exclamation, bracketing the whole discourse."},
        {"q": "Is a setting stated for AN 6.26?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Isipatana", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "Continuing this chapter's bare-formula pattern, though the speaker is named."},
        {"q": "How many times has this series now encountered the six recollections, counting "
              "this discourse?",
         "opts": ["Two", "Three", "Four — AN 6.9, 6.10, 6.25, and this discourse", "Five"],
         "correct": 2,
         "expl": "The most repeated single teaching so far in this nipāta."},
        {"q": "What comes next in the chapter, after this fourth telling?",
         "opts": [
             "AN 6.27, on the proper occasions for approaching an esteemed mendicant",
             "The chapter ends here",
             "A fifth telling of the six recollections",
             "A return to the thoroughbred simile"],
         "correct": 0,
         "expl": "A shift to a new subject after four consecutive tellings of one teaching."},
    ],
    marginalia=[
        ("Four tellings so far", [
            "AN 6.9: bare list",
            "AN 6.10: joy to immersion",
            "AN 6.25: purified of greed",
            "AN 6.26: space-like heart",
        ]),
        ("Praise, not instruction", [
            "Mahākaccāna's own",
            "wonder — 'an opening",
            "amid confinement'",
        ]),
        ("Where the addition falls", [
            "Buddha- and deity-",
            "recollection only —",
            "not the middle four",
        ]),
        ("Cross-references", [
            "AN 6.25 &middot; previous, the third telling",
            "AN 6.10 &middot; the first full expansion",
        ]),
    ],
    further=[
        '<a href="%s/an6.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.27.html">AN 6.27 &middot; Proper Occasions (1st)</a> &mdash; next, when '
        "to approach an esteemed mendicant for guidance.",
        '<a href="an-6.25.html">AN 6.25 &middot; Topics for Recollection</a> &mdash; previous, '
        "the third telling, for direct comparison.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.27 — Paṭhamasamayasutta
# --------------------------------------------------------------------------- #
page(
    27, "Paṭhamasamaya", "Proper Occasions (1st)",
    vagga=VAGGA_3,
    meta_title="AN 6.27 — Proper Occasions (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamasamayasutta, "
        "answering a mendicant's question about when to approach an esteemed senior for "
        "guidance: five hindrances and one further gap in understanding. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, answering a mendicant's question"),
        ("Form", "A question, and a list of six occasions, five following one template and the "
                 "sixth slightly different"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Guidance on when to seek out a senior teacher recurs across "
                              "monastic literature broadly, including the Chinese Āgamas and "
                              "Vinaya; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a clear, practically useful "
                       "list with an easily followed template"),
    ],
    why=(
        "A mendicant asks a direct, practical question: how many occasions are there for going "
        "to see an esteemed mendicant? The Buddha answers with six, five of them built from an "
        "identical template &mdash; naming one of the five hindrances (sensual desire, ill "
        "will, dullness and drowsiness, restlessness and remorse, doubt) as the specific "
        "obstruction that warrants a visit &mdash; and a sixth, structurally similar but "
        "concerning not an obstruction but a gap in understanding: not knowing what meditation "
        "subject to focus on."),
    guide=[
        ("The teaching in one sentence", [
            "There are six occasions for approaching an esteemed mendicant: when one's heart is "
            "overcome by each of the five hindrances in turn, and when one does not understand "
            "what meditation to focus on in order to end the defilements without delay."]),
        ("The five hindrances, as five of the six occasions", [
            "The discourse's first five occasions map directly onto the standard five "
            "hindrances (<em>nīvaraṇa</em>) named throughout the canon as obstacles to "
            "meditative progress: sensual desire, ill will, dullness and drowsiness, "
            "restlessness and remorse, and doubt. Each occasion follows the identical script: "
            "the mendicant reports being &ldquo;overcome and mired&rdquo; in the hindrance and "
            "not understanding &ldquo;the escape&rdquo; from it, asks for teaching, and receives "
            "it."]),
        ("A sixth occasion of a different kind", [
            "The sixth occasion breaks the pattern: it is not one of the five hindrances but a "
            "gap in direction &mdash; not knowing what specific meditation subject to take up "
            "&ldquo;in order to end the defilements without delay.&rdquo; Where the first five "
            "concern removing an active obstruction, the sixth concerns supplying a missing "
            "positive direction. The list moves, in its final item, from troubleshooting to "
            "guidance."]),
        ("What 'esteemed mendicant' implies about the community", [
            "The discourse assumes, without arguing for it, that some mendicants are recognized "
            "as worth seeking out specifically for this kind of help &mdash; "
            "<em>manobhāvanīya</em>, literally &ldquo;one who develops the mind,&rdquo; often "
            "rendered &ldquo;esteemed&rdquo; or &ldquo;inspiring.&rdquo; The list presupposes a "
            "community with recognized, approachable seniors, not simply peers of equal "
            "standing."]),
        ("Setting up a companion discourse on the same question", [
            "AN 6.28, immediately following, revisits this exact question &mdash; how many "
            "occasions are there for going to see an esteemed mendicant &mdash; but through a "
            "narrative in which several senior mendicants initially misunderstand the question "
            "entirely, debating the best <em>time of day</em> rather than the right "
            "<em>circumstance</em>, before Mahākaccāna corrects them with the very answer given "
            "here."]),
    ],
    terms=[
        ("manobhāvanīya",
         "&ldquo;esteemed,&rdquo; literally &ldquo;one who develops the mind&rdquo; &mdash; the "
         "discourse's term for the mendicant worth approaching for guidance."),
        ("nīvaraṇa",
         "&ldquo;hindrance&rdquo; &mdash; the standard canonical term for the five obstacles "
         "named across this discourse's first five occasions."),
        ("thinamiddha",
         "&ldquo;dullness and drowsiness&rdquo; &mdash; the third hindrance named, the occasion "
         "for the third visit."),
        ("uddhaccakukkucca",
         "&ldquo;restlessness and remorse&rdquo; &mdash; the fourth hindrance named, the "
         "occasion for the fourth visit."),
        ("kammaṭṭhāna",
         "not directly named in this English translation but the standard term for "
         "&ldquo;meditation subject&rdquo; &mdash; what the sixth occasion concerns not "
         "knowing."),
    ],
    text_intro=(
        "The discourse in full: a mendicant's question, and the Buddha's six occasions. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A mendicant's question"),
        ("p", "&sect;1", "an6.27:1.1-1.3"),
        ("h3", "The first occasion: sensual desire"),
        ("p", "&sect;2", "an6.27:2.1-2.6"),
        ("h3", "The sixth occasion: not knowing what to meditate on"),
        ("p", "&sect;3", "an6.27:7.1-8.1"),
    ],
    quiz=[
        {"q": "What question does a mendicant ask the Buddha at the start of this discourse?",
         "opts": [
             "How many topics for recollection are there",
             "How many occasions there are for going to see an esteemed mendicant",
             "How many kinds of psychic power exist",
             "How many chapters are in the Sixes"],
         "correct": 1,
         "expl": "A direct, practical question about seeking guidance."},
        {"q": "What do the first five occasions have in common?",
         "opts": [
             "They all concern financial matters",
             "Each names one of the five standard hindrances — sensual desire, ill will, "
             "dullness and drowsiness, restlessness and remorse, and doubt",
             "They all require traveling to a different monastery",
             "They apply only to newly ordained mendicants"],
         "correct": 1,
         "expl": "Following an identical template of being 'overcome and mired' in each "
                 "hindrance."},
        {"q": "How does the sixth occasion differ from the first five?",
         "opts": [
             "It is identical to the first occasion",
             "It concerns not knowing what meditation subject to focus on, rather than being "
             "actively obstructed by a hindrance — supplying missing direction rather than "
             "removing an obstruction",
             "It only applies to senior mendicants",
             "It does not involve seeking guidance at all"],
         "correct": 1,
         "expl": "A shift from troubleshooting an obstruction to seeking positive direction."},
        {"q": "What does <em>manobhāvanīya</em> mean?",
         "opts": [
             "A newly ordained mendicant",
             "'Esteemed,' literally 'one who develops the mind' — the kind of senior worth "
             "approaching for guidance",
             "A lay donor",
             "A wandering ascetic of another sect"],
         "correct": 1,
         "expl": "The discourse's term for the figure these six occasions concern approaching."},
        {"q": "What does the discourse assume about the community, according to the guide?",
         "opts": [
             "That all mendicants are of exactly equal standing with no recognized seniors",
             "That some mendicants are recognized as worth seeking out specifically for "
             "guidance — a community with approachable seniors, not simply peers",
             "That mendicants should never seek help from others",
             "That only the Buddha himself can give this kind of guidance"],
         "correct": 1,
         "expl": "The list presupposes recognized, approachable seniors within the community."},
        {"q": "What are the five hindrances named across this discourse's first five occasions?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Sensual desire, ill will, dullness and drowsiness, restlessness and remorse, doubt",
             "Danger, suffering, disease, boil, bog",
             "Work, talk, sleep, company, closeness"],
         "correct": 1,
         "expl": "The standard canonical list of nīvaraṇa."},
        {"q": "How does AN 6.28, the next discourse, relate to this one?",
         "opts": [
             "It is entirely unrelated",
             "It revisits the exact same question through a narrative where senior mendicants "
             "initially misunderstand it, before Mahākaccāna supplies this discourse's answer",
             "It contradicts this discourse's list of six occasions",
             "It replaces the question with a different one about meditation technique"],
         "correct": 1,
         "expl": "A companion discourse built around the same question, differently framed."},
        {"q": "Is a setting stated for AN 6.27?",
         "opts": ["Yes, at Isipatana", "No — none is stated", "Yes, near Sāma village", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare question-and-answer with no scene given."},
        {"q": "What is the stated goal of the sixth occasion's guidance?",
         "opts": [
             "To end the defilements without delay",
             "To gain worldly wealth",
             "To become a senior mendicant more quickly",
             "To avoid ever meditating on unpleasant subjects"],
         "correct": 0,
         "expl": "The specific aim named for seeking guidance on a meditation subject."},
        {"q": "What does <em>thinamiddha</em> mean?",
         "opts": ["Doubt", "Restlessness and remorse", "Dullness and drowsiness", "Ill will"],
         "correct": 2,
         "expl": "The third of the five hindrances, occasioning the third visit."},
    ],
    marginalia=[
        ("Six occasions", [
            "1&ndash;5. each hindrance:",
            "desire, ill will, dullness,",
            "restlessness, doubt",
            "6. no meditation subject",
        ]),
        ("Same script, five times", [
            "'overcome and mired' —",
            "ask, and receive",
            "the escape",
        ]),
        ("The sixth breaks the pattern", [
            "not removing an obstacle,",
            "but supplying missing",
            "positive direction",
        ]),
        ("Cross-references", [
            "AN 6.28 &middot; next, the narrative variant",
        ]),
    ],
    further=[
        '<a href="%s/an6.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.28.html">AN 6.28 &middot; Proper Occasions (2nd)</a> &mdash; next, the '
        "same six occasions reached through a debate among senior mendicants.",
        '<a href="an-6.26.html">AN 6.26 &middot; With Mahākaccāna</a> &mdash; previous, the same '
        "figure who resolves the companion discourse's debate.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.28 — Dutiyasamayasutta
# --------------------------------------------------------------------------- #
page(
    28, "Dutiyasamaya", "Proper Occasions (2nd)",
    vagga=VAGGA_3,
    meta_title="AN 6.28 — Proper Occasions (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyasamayasutta, in "
        "which senior mendicants debate the best time of day to visit a teacher, mistaking the "
        "question, until Mahākaccāna recites what the Buddha actually taught. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Near Varanasi, in the deer park at Isipatana"),
        ("Speakers", "Several unnamed senior mendicants, then Mahākaccāna"),
        ("Form", "A misdirected debate among peers, three proposed answers each rejected in "
                 "turn, and a correction citing the Buddha directly"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Narrative correctives of a misunderstood question recur in "
                              "related forms across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; an accessible narrative "
                       "whose real interest is in what the debate gets wrong, not merely what "
                       "the final answer is"),
    ],
    why=(
        "AN 6.27 gave the Buddha's own answer to a simple question. AN 6.28 dramatizes what "
        "happens when the same question circulates without him: a group of senior mendicants at "
        "Isipatana ask each other how many occasions there are for visiting an esteemed "
        "mendicant, and three of them answer in turn &mdash; each proposing a specific time of "
        "day, each rejected by the next speaker on practical grounds &mdash; before Mahākaccāna "
        "points out that they have all misread the question and recites, from memory, the "
        "six-occasion answer already given at AN 6.27."),
    guide=[
        ("The teaching in one sentence", [
            "Three senior mendicants each propose a specific time of day as the proper occasion "
            "for visiting an esteemed mendicant, each proposal rejected by the next speaker on "
            "practical grounds, until Mahākaccāna corrects the whole discussion by reciting the "
            "Buddha's actual six-occasion answer: not a time of day at all, but five hindrances "
            "and one gap in understanding."]),
        ("Three proposed times, three practical objections", [
            "The first mendicant proposes just after the midday meal, freshly returned from "
            "almsround; the second objects that fatigue from walking and eating has not yet "
            "faded, and proposes late afternoon instead; the third objects that the mind is "
            "still absorbed in the day's meditation subject at that hour, and proposes dawn. "
            "Each answer is plausible on its own practical terms, and each is overturned by an "
            "equally practical objection &mdash; the debate never resolves on its own footing."]),
        ("A shared misreading, not three competing answers", [
            "What the three mendicants share is not disagreement about content but a common "
            "misconstrual of the question itself: they treat &ldquo;occasion&rdquo; "
            "(<em>samaya</em>) as meaning a time of day, when the Buddha's own answer, cited "
            "moments later, treats it as meaning a circumstance &mdash; a specific inner state "
            "calling for guidance, regardless of what hour it occurs in. The debate is not "
            "wrong in its practical observations about fatigue and mental absorption; it is "
            "answering a question no one actually asked."]),
        ("Mahākaccāna's correction, cited as received teaching", [
            "Mahākaccāna does not argue against the three proposals directly, or offer a fourth "
            "time of day. He instead says, &ldquo;I have heard and learned this in the presence "
            "of the Buddha,&rdquo; and recites the identical six occasions given at AN 6.27 "
            "&mdash; word for word, checked directly against the source. His authority here "
            "rests entirely on accurate transmission, not on his own reasoning; he settles the "
            "debate by supplying what the Buddha actually said, not by out-arguing his peers."]),
        ("Why this pairing matters for how the canon transmits teaching", [
            "Read beside AN 6.27, this discourse dramatizes a real risk in oral transmission: "
            "even senior, well-intentioned practitioners can drift from a teaching's actual "
            "content toward a superficially similar but different question, simply by "
            "discussing it among themselves without a fixed reference. The corrective is not "
            "better reasoning but accurate memory of what was actually taught."]),
    ],
    terms=[
        ("samaya",
         "&ldquo;occasion,&rdquo; here at the center of the discourse's misunderstanding "
         "&mdash; mistaken for a time of day rather than a circumstance."),
        ("piṇḍapātapaṭikkanta",
         "&ldquo;returned from almsround&rdquo; &mdash; the first proposed occasion, rejected "
         "for the fatigue of the meal and the walk."),
        ("paṭisallānā vuṭṭhita",
         "&ldquo;come out of retreat&rdquo; &mdash; the late-afternoon proposal, rejected "
         "because the meditator is still absorbed in the day's subject."),
        ("kammaṭṭhāna",
         "&ldquo;meditation subject&rdquo; &mdash; what the second objection says still "
         "occupies the mind in late afternoon, making that hour unsuitable on the debaters' own "
         "terms."),
        ("sutaṁ me idaṁ, āvuso, bhagavato santike",
         "&ldquo;I have heard and learned this in the presence of the Buddha&rdquo; &mdash; "
         "Mahākaccāna's formula introducing his correction, grounding it in direct transmission."),
    ],
    text_intro=(
        "The discourse in full: the senior mendicants' misdirected debate, and Mahākaccāna's "
        "correction. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Isipatana: the question arises"),
        ("p", "&sect;1", "an6.28:1.1-1.3"),
        ("h3", "Three proposed times of day, each rejected"),
        ("p", "&sect;2", "an6.28:2.1-5.3"),
        ("h3", "Mahākaccāna's correction"),
        ("p", "&sect;3", "an6.28:6.1-6.3"),
        ("h3", "The six occasions, recited from memory"),
        ("p", "&sect;4", "an6.28:7.1-13.2"),
    ],
    quiz=[
        {"q": "What question do the senior mendicants at Isipatana discuss?",
         "opts": [
             "How many recollections there are",
             "How many occasions there are for going to see an esteemed mendicant — the same "
             "question already answered at AN 6.27",
             "How to enter the four absorptions",
             "How many hindrances there are"],
         "correct": 1,
         "expl": "Discussed independently, without reference back to the Buddha's own answer."},
        {"q": "What kind of answers do the first three mendicants propose?",
         "opts": [
             "Three different lists of hindrances",
             "Three different times of day — after the midday meal, late afternoon, and dawn — "
             "each rejected by the next speaker on practical grounds",
             "Three different locations to visit",
             "They all agree immediately on the same answer"],
         "correct": 1,
         "expl": "Each proposal plausible on its own terms, each overturned by a practical "
                 "objection."},
        {"q": "What do the three mendicants share, according to the guide, beneath their "
              "disagreement?",
         "opts": [
             "Nothing — they are answering entirely unrelated questions",
             "A common misconstrual of 'occasion' (samaya) as a time of day, rather than a "
             "circumstance or inner state calling for guidance",
             "All three are correct and Mahākaccāna is mistaken",
             "They are debating a completely different topic from AN 6.27"],
         "correct": 1,
         "expl": "Answering a question no one actually asked, however sound their individual "
                 "practical points."},
        {"q": "How does Mahākaccāna resolve the debate?",
         "opts": [
             "By proposing a fourth, better time of day",
             "By citing direct transmission — 'I have heard and learned this in the presence of "
             "the Buddha' — and reciting the six occasions from AN 6.27 word for word",
             "By declaring all three mendicants wrong without offering an alternative",
             "By asking the Buddha to intervene in person"],
         "correct": 1,
         "expl": "His authority rests on accurate memory of the actual teaching, not on winning "
                 "the argument."},
        {"q": "What broader point about oral transmission does this pairing illustrate, "
              "according to the guide?",
         "opts": [
             "That senior mendicants are infallible",
             "That even senior, well-intentioned practitioners can drift toward a superficially "
             "similar but different question when discussing a teaching without a fixed "
             "reference — the corrective is accurate memory, not better reasoning",
             "That debate among mendicants should never occur",
             "That written texts are more reliable than oral memory"],
         "correct": 1,
         "expl": "A dramatization of a real risk in how teachings circulate and drift."},
        {"q": "Where is AN 6.28 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Near Varanasi, in the deer park at Isipatana",
             "Near the little village of Sāma",
             "At Ñātika, in the brick house"],
         "correct": 1,
         "expl": "A fresh, specific setting for this narrative discourse."},
        {"q": "What objection is raised against the first proposed time (just after the midday "
              "meal)?",
         "opts": [
             "It is too early in the morning",
             "The fatigue from walking and eating has not yet faded away",
             "No mendicants are awake at that hour",
             "It violates monastic discipline"],
         "correct": 1,
         "expl": "A practical objection, not a claim that the question itself was misunderstood."},
        {"q": "What objection is raised against the late-afternoon proposal?",
         "opts": [
             "It is too dark to travel safely",
             "The meditator is still absorbed in the day's meditation subject at that hour",
             "It coincides with the meal time",
             "No objection is raised to this proposal"],
         "correct": 1,
         "expl": "Also a practical objection about mental state, still missing the deeper "
                 "misunderstanding Mahākaccāna later identifies."},
        {"q": "What does <em>samaya</em> mean in the context of this discourse's central "
              "confusion?",
         "opts": [
             "It unambiguously means 'time of day' throughout the canon",
             "'Occasion' — capable of meaning either a time of day or a circumstance, and the "
             "debate's error is assuming the former when the Buddha meant the latter",
             "A term exclusively for meditative absorption",
             "A synonym for 'esteemed mendicant'"],
         "correct": 1,
         "expl": "The word's ambiguity is exactly what drives the mendicants' shared "
                 "misunderstanding."},
        {"q": "How does this discourse relate to AN 6.27?",
         "opts": [
             "It contradicts AN 6.27's answer",
             "It dramatizes how the very question AN 6.27 answered can be misconstrued when "
             "discussed without reference back to the original teaching",
             "It is entirely unrelated to AN 6.27",
             "It replaces AN 6.27's six occasions with a new list of three"],
         "correct": 1,
         "expl": "A companion narrative built around the same underlying question and answer."},
    ],
    marginalia=[
        ("Three rejected proposals", [
            "after the meal —",
            "too fatigued",
            "late afternoon —",
            "still absorbed",
            "dawn — the one",
            "left unrejected, until",
        ]),
        ("The shared error", [
            "'occasion' mistaken",
            "for time of day,",
            "not circumstance",
        ]),
        ("Mahākaccāna's method", [
            "not better argument —",
            "accurate recitation",
            "of what was actually taught",
        ]),
        ("Cross-references", [
            "AN 6.27 &middot; the original answer",
        ]),
    ],
    further=[
        '<a href="%s/an6.28/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.29.html">AN 6.29 &middot; With Udāyī</a> &mdash; next, another discourse '
        "turning on a question misunderstood.",
        '<a href="an-6.27.html">AN 6.27 &middot; Proper Occasions (1st)</a> &mdash; previous, '
        "the Buddha's own original answer to this same question.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.29 — Udāyīsutta
# --------------------------------------------------------------------------- #
page(
    29, "Udāyī", "With Udāyī",
    vagga=VAGGA_3,
    meta_title="AN 6.29 — With Udāyī | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Udāyīsutta, where the "
        "same phrase 'topics for recollection' names an entirely different list — absorption, "
        "light, the body, the charnel ground, and mindful activity — not the six recollections "
        "met earlier in this chapter. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The Buddha, Udāyī, and Ānanda"),
        ("Form", "A repeated question, a silent and then mistaken answer, a correct answer from "
                 "Ānanda, and the Buddha's own addition"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Meditation-object lists of this kind recur widely across the "
                              "Chinese Āgamas and later meditation manuals; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; demanding both for its "
                       "technical content and for the terminological trap at its center"),
    ],
    why=(
        "This discourse uses the identical Pāli term, <em>anussatiṭṭhāna</em>, "
        "&ldquo;topic for recollection,&rdquo; that named the six recollections at AN 6.9, "
        "6.10, 6.25, and 6.26 &mdash; and then names a completely different list under that "
        "same term: not the Buddha, the teaching, the Saṅgha, ethics, generosity, and the "
        "deities, but the absorptions, the perception of light, contemplation of the body, "
        "contemplation of a corpse in decay, and mindful attention to ordinary activity. Two "
        "distinct six-item (here, five-plus-one) lists share one name. A reader who assumes "
        "&ldquo;topics for recollection&rdquo; always means the same content, on the strength of "
        "the shared term alone, will get this discourse wrong."),
    guide=[
        ("The teaching in one sentence", [
            "Asked how many topics for recollection there are, Udāyī answers wrongly with only "
            "one (recollection of past lives); Ānanda then correctly names five &mdash; the "
            "absorptions, the perception of light, contemplation of the body's parts, "
            "contemplation of a decaying corpse, and the fourth absorption &mdash; and the "
            "Buddha adds a sixth: mindful attention to ordinary activity."]),
        ("Why this list is not the six recollections met earlier", [
            "This is worth stating as plainly as possible, having checked the Pāli directly: "
            "the term <em>anussatiṭṭhāna</em> is shared with AN 6.9, 6.10, 6.25, and 6.26, but "
            "the content named here shares nothing with that list. Where the earlier four "
            "discourses concerned recollecting the Triple Gem, one's own ethics and generosity, "
            "and the deities, this discourse concerns meditative techniques &mdash; absorption "
            "states, a light-based perception practice, body contemplation, and charnel-ground "
            "reflection. The canon uses one general term, &ldquo;subject for recollection,&rdquo; "
            "for more than one specific enumerated list, and this discourse and AN 6.9/6.10/6.25/"
            "6.26 should not be read as variants of a single fixed teaching."]),
        ("Udāyī's mistake, and the Buddha's sharp response", [
            "Asked the question three times, Udāyī stays silent twice, then finally answers with "
            "only past-life recollection &mdash; itself a real recollection practice, but not "
            "what the Buddha's question was probing for, and offered as if it were a complete "
            "answer rather than one item among several. The Buddha's response is uncharacteristically "
            "blunt: he tells Ānanda directly, in Udāyī's hearing, that &ldquo;this futile man "
            "Udāyī is not committed to the higher mind,&rdquo; before turning to Ānanda for the "
            "actual answer."]),
        ("Ānanda's five, and the Buddha's addition of a sixth", [
            "Ānanda names five topics, each closing with a stated outcome: the first three "
            "absorptions, leading to blissful meditation in this life; the perception of light, "
            "leading to knowledge and vision; contemplation of the body's parts, leading to "
            "giving up sensual desire; contemplation of a corpse's stages of decay, leading to "
            "uprooting the conceit &ldquo;I am&rdquo;; and the fourth absorption, leading to "
            "penetration of the elements. The Buddha praises this answer and adds a sixth "
            "himself: mindfully going, returning, standing, sitting, lying down, and working, "
            "leading to mindfulness and situational awareness in ordinary activity."]),
        ("A caution this guide applies to itself, again", [
            "Encountering a discourse whose title and central term match earlier pages so "
            "closely, the temptation is to summarize it as &ldquo;another version of the six "
            "recollections&rdquo; and move on. Direct comparison of the actual content shows "
            "that would be wrong. This is the same caution already applied at AN 6.25, restated "
            "here because the resemblance in this case is closer &mdash; identical title, "
            "identical central term &mdash; and so the risk of conflating them without checking "
            "is correspondingly greater."]),
    ],
    terms=[
        ("anussatiṭṭhāna",
         "&ldquo;topic for recollection&rdquo; &mdash; the term shared with AN 6.9/6.10/6.25/"
         "6.26, here naming an entirely different five-plus-one item list."),
        ("dummedha",
         "&ldquo;futile,&rdquo; &ldquo;witless&rdquo; &mdash; the Buddha's blunt description of "
         "Udāyī, spoken to Ānanda in Udāyī's own hearing."),
        ("ālokasaññā",
         "&ldquo;perception of light&rdquo; &mdash; the second of Ānanda's five topics, said to "
         "lead to knowledge and vision."),
        ("asubhasaññā",
         "not named directly by this term in the translation but the standard canonical name "
         "for contemplation of the body's impurity, Ānanda's third topic."),
        ("satisampajañña",
         "&ldquo;mindfulness and situational awareness&rdquo; &mdash; what the Buddha's added "
         "sixth topic, mindful attention to ordinary activity, is said to lead to."),
    ],
    text_intro=(
        "The discourse in full: Udāyī's silence and mistaken answer, Ānanda's five topics, and "
        "the Buddha's addition of a sixth. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha's question, and Udāyī's silence"),
        ("p", "&sect;1", "an6.29:1.1-1.9"),
        ("h3", "Ānanda intervenes; Udāyī's mistaken answer"),
        ("p", "&sect;2", "an6.29:2.1-2.5"),
        ("h3", "The Buddha's rebuke, and Ānanda's five topics"),
        ("p", "&sect;3", "an6.29:3.1-10.3"),
        ("h3", "The Buddha adds a sixth"),
        ("p", "&sect;4", "an6.29:11.1-11.4"),
    ],
    quiz=[
        {"q": "What term does this discourse use, shared with AN 6.9, 6.10, 6.25, and 6.26?",
         "opts": [
             "Sāraṇīya, warm-hearted",
             "Anussatiṭṭhāna, topic for recollection",
             "Anuttariya, unsurpassable",
             "Nissāraṇīya, elements of escape"],
         "correct": 1,
         "expl": "The same term, but naming an entirely different list here."},
        {"q": "Does this discourse's list of 'topics for recollection' match the six "
              "recollections (Buddha, teaching, Saṅgha, ethics, generosity, deities) met at AN "
              "6.9/6.10/6.25/6.26?",
         "opts": [
             "Yes, it is the same list under a different framing",
             "No — checked directly against the Pāli, the content shares nothing with that "
             "list; this discourse names meditative techniques instead",
             "It is a partial overlap of three items",
             "The discourse does not actually name any topics"],
         "correct": 1,
         "expl": "One shared term, two genuinely different enumerated lists — not variants of "
                 "one teaching."},
        {"q": "How does Udāyī answer the Buddha's question, and why is it wrong?",
         "opts": [
             "He answers correctly with all six recollections",
             "After staying silent twice, he names only recollection of past lives — a real "
             "practice, but offered as a complete answer rather than one item among several",
             "He refuses to answer at all, even when pressed",
             "He gives an answer with ten items instead of six"],
         "correct": 1,
         "expl": "Incomplete and mistaking the scope of the actual question."},
        {"q": "How does the Buddha respond to Udāyī's answer?",
         "opts": [
             "He praises Udāyī's answer as correct",
             "He bluntly tells Ānanda, in Udāyī's hearing, that 'this futile man Udāyī is not "
             "committed to the higher mind,' then turns to Ānanda for the real answer",
             "He ignores the answer and changes the subject",
             "He asks Udāyī to elaborate further"],
         "correct": 1,
         "expl": "An uncharacteristically sharp rebuke in this series so far."},
        {"q": "What five topics does Ānanda name?",
         "opts": [
             "The Buddha, teaching, Saṅgha, ethics, and generosity",
             "The first three absorptions, the perception of light, contemplation of the body's "
             "parts, contemplation of a decaying corpse, and the fourth absorption",
             "The five faculties",
             "Seeing, listening, acquisition, training, and service"],
         "correct": 1,
         "expl": "Each closing with its own stated outcome, from blissful meditation to "
                 "uprooting the conceit 'I am'."},
        {"q": "What sixth topic does the Buddha add to Ānanda's five?",
         "opts": [
             "Recollection of the deities",
             "Mindfully going, returning, standing, sitting, lying down, and working — leading "
             "to mindfulness and situational awareness",
             "A seventh absorption",
             "Recollection of one's own past lives"],
         "correct": 1,
         "expl": "Extending ordinary daily activity itself into the domain of mindful practice."},
        {"q": "What caution does the guide apply to itself in reading this discourse?",
         "opts": [
             "None — it assumes the title alone settles the content",
             "The same caution applied at AN 6.25, restated here because the resemblance — "
             "identical title and central term — makes the risk of wrongly conflating the two "
             "lists greater",
             "A caution against ever comparing two discourses with similar titles",
             "A caution that Ānanda's answer should be doubted"],
         "correct": 1,
         "expl": "Direct comparison of content, not reliance on a shared label, is what settles "
                 "the question."},
        {"q": "What outcome does contemplation of a decaying corpse lead to, according to "
              "Ānanda?",
         "opts": [
             "Blissful meditation in this life",
             "Uprooting the conceit 'I am'",
             "Knowledge and vision",
             "Giving up sensual desire"],
         "correct": 1,
         "expl": "The fourth of Ānanda's five topics."},
        {"q": "Is a setting stated for AN 6.29?",
         "opts": ["Yes, at Isipatana", "No — none is stated", "Yes, near Sāma village", "Yes, at Kapilavatthu"],
         "correct": 1,
         "expl": "Continuing this chapter's frequent bare-formula pattern."},
        {"q": "What outcome does the perception of light lead to?",
         "opts": ["Uprooting the conceit 'I am'", "Knowledge and vision", "Blissful meditation", "Penetration of the elements"],
         "correct": 1,
         "expl": "The second of Ānanda's five topics, ālokasaññā."},
    ],
    marginalia=[
        ("Not the same list", [
            "same term as AN 6.9/",
            "6.10/6.25/6.26 —",
            "entirely different content",
        ]),
        ("Ānanda's five", [
            "1st&ndash;3rd absorption",
            "perception of light",
            "body &middot; corpse decay",
            "4th absorption",
        ]),
        ("The Buddha's sixth", [
            "mindful in every",
            "ordinary activity —",
            "going, sitting, working",
        ]),
        ("Cross-references", [
            "AN 6.9/6.10/6.25/6.26 &middot; the other list",
            "AN 6.30 &middot; next, unsurpassable expanded",
        ]),
    ],
    further=[
        '<a href="%s/an6.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.30.html">AN 6.30 &middot; Unsurpassable</a> &mdash; next, closing the '
        "chapter with the full expansion of AN 6.8's list.",
        '<a href="an-6.25.html">AN 6.25 &middot; Topics for Recollection</a> &mdash; for direct '
        "comparison with the six recollections this discourse does not repeat.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.30 — Anuttariyasutta
# --------------------------------------------------------------------------- #
page(
    30, "Anuttariya", "Unsurpassable",
    vagga=VAGGA_3,
    meta_title="AN 6.30 — Unsurpassable | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anuttariyasutta, "
        "closing the chapter with the full expansion of AN 6.8's bare list of six unsurpassable "
        "things, each contrasted with an ordinary counterpart. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Six matched contrasts, each naming an ordinary version of the item and then "
                 "its unsurpassable counterpart, closed with a summary verse"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "This same six-item unsurpassable list and its expansion recur at "
                              "MN 30 and across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; long by this chapter's "
                       "standards, but built from one repeated contrast pattern across all six "
                       "items"),
    ],
    why=(
        "AN 6.8, back in this nipāta's first chapter, named six unsurpassable things &mdash; "
        "seeing, listening, acquisition, training, service, recollection &mdash; and stopped, "
        "offering no explanation. AN 6.30, closing this chapter, is that explanation: for each "
        "of the six, an ordinary version is named and acknowledged as real (&ldquo;there is "
        "such a seeing, I don't deny it&rdquo;), then judged &ldquo;low, crude, ordinary, "
        "ignoble, and pointless,&rdquo; before the unsurpassable version is defined, in every "
        "case, as directed toward the Buddha or his disciples."),
    guide=[
        ("The teaching in one sentence", [
            "For each of six activities &mdash; seeing, hearing, acquiring, training, serving, "
            "and recollecting &mdash; there is an ordinary version aimed at worldly things, and "
            "an unsurpassable version aimed at a Realized One or his disciple; only the latter "
            "leads toward disillusionment, dispassion, and extinguishment."]),
        ("A repeated, six-fold contrast", [
            "Every item follows the same pattern: an ordinary object is named (an elephant or "
            "jewel to see, drums or singing to hear, a child or wealth to acquire, riding or "
            "archery to train in, an aristocrat or brahmin to serve, a child or wealth to "
            "recollect), acknowledged without denial, then judged pointless and incapable of "
            "leading to awakening; the unsurpassable counterpart replaces the worldly object "
            "with a Realized One or disciple in every single case."]),
        ("The one qualification worth noting", [
            "The ordinary version of each item is not condemned as false or nonexistent "
            "&mdash; &ldquo;there is such a seeing, I don't deny it&rdquo; is repeated for each "
            "&mdash; only as failing to accomplish what the unsurpassable version accomplishes. "
            "The discourse's target is not the existence of worldly seeing, hearing, or "
            "acquisition, but their insufficiency as a vehicle toward disillusionment and "
            "extinguishment."]),
        ("This is what AN 6.8 was withholding", [
            "This page can now say directly what AN 6.8's guide could only anticipate from "
            "elsewhere in the canon: AN 6.30, within this very nipāta, supplies the unpacking "
            "AN 6.8 left bare. The unsurpassable seeing is going, with settled faith, to see a "
            "Realized One or disciple; the unsurpassable hearing is going to hear their "
            "teaching; the unsurpassable acquisition is acquiring faith in them; the "
            "unsurpassable training is training in higher ethics, mind, and wisdom under their "
            "guidance; the unsurpassable service is serving them; and the unsurpassable "
            "recollection is recollecting them."]),
        ("Closing both this chapter and a long-open thread", [
            "AN 6.30 closes the Anuttariyavagga by returning to and completing its own chapter "
            "title's promise &mdash; and, at the same time, closes a thread left open since AN "
            "6.8 in the previous chapter. Few discourses in this nipāta so far have this "
            "double function, answering both their immediate chapter's material and an earlier "
            "chapter's unfinished list."]),
    ],
    terms=[
        ("anuttariya",
         "&ldquo;unsurpassable&rdquo; &mdash; unchanged from AN 6.8, now defined for each of "
         "the six items in turn."),
        ("hīna",
         "&ldquo;low,&rdquo; &ldquo;inferior&rdquo; &mdash; part of the fivefold judgment "
         "(&ldquo;low, crude, ordinary, ignoble, pointless&rdquo;) passed on each ordinary "
         "version."),
        ("pasādabahula",
         "not a single Pāli compound in this translation but the sense of &ldquo;settled faith "
         "and fondness&rdquo; that defines every unsurpassable version's approach to a Realized "
         "One or disciple."),
        ("adhisīla adhicitta adhipaññā",
         "&ldquo;higher ethics, the higher mind, and the higher wisdom&rdquo; &mdash; what the "
         "unsurpassable training specifically consists of."),
        ("nibbidā virāga nirodha",
         "&ldquo;disillusionment, dispassion, cessation&rdquo; &mdash; part of the sevenfold "
         "outcome the ordinary versions are said not to lead to, and the unsurpassable versions "
         "do."),
    ],
    text_intro=(
        "The discourse in full: the six unsurpassable things, each contrasted with its ordinary "
        "counterpart, closing in verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six unsurpassable things, named"),
        ("p", "&sect;1", "an6.30:1.1-1.3"),
        ("h3", "The unsurpassable seeing"),
        ("p", "&sect;2", "an6.30:2.1-2.7"),
        ("h3", "The unsurpassable hearing"),
        ("p", "&sect;3", "an6.30:3.1-3.7"),
        ("h3", "The unsurpassable acquisition"),
        ("p", "&sect;4", "an6.30:4.1-4.7"),
        ("h3", "The unsurpassable training"),
        ("p", "&sect;5", "an6.30:5.1-5.7"),
        ("h3", "The unsurpassable service"),
        ("p", "&sect;6", "an6.30:6.1-6.7"),
        ("h3", "The unsurpassable recollection, and the closing verses"),
        ("p", "&sect;7", "an6.30:7.1-11.4"),
    ],
    quiz=[
        {"q": "What relationship does AN 6.30 have to AN 6.8, in the previous chapter?",
         "opts": [
             "No relationship — a coincidental repeated title",
             "AN 6.30 supplies the full explanation AN 6.8 left as a bare, unexplained list",
             "AN 6.30 contradicts AN 6.8's list",
             "AN 6.30 replaces AN 6.8's six items with a different six"],
         "correct": 1,
         "expl": "The same six terms — seeing, listening, acquisition, training, service, "
                 "recollection — now defined in full."},
        {"q": "What pattern does every one of the six items follow?",
         "opts": [
             "A pure denial that the ordinary version exists at all",
             "The ordinary version is named and acknowledged as real, judged low and pointless, "
             "then the unsurpassable version is defined as directed toward a Realized One or "
             "disciple",
             "Each item is explained with a completely different structure",
             "Only the unsurpassable version is mentioned, with no ordinary counterpart"],
         "correct": 1,
         "expl": "'There is such a seeing, I don't deny it' — repeated for each of the six."},
        {"q": "What is the discourse's actual target, according to the guide?",
         "opts": [
             "The claim that worldly seeing, hearing, or acquisition don't exist",
             "Not the existence of the ordinary versions, but their insufficiency as a vehicle "
             "toward disillusionment and extinguishment",
             "A prohibition on ever seeing or hearing ordinary things",
             "A claim that only mendicants may see or hear anything at all"],
         "correct": 1,
         "expl": "The ordinary version is acknowledged, not denied — only judged inadequate for "
                 "the stated goal."},
        {"q": "What defines the unsurpassable version of each of the six items?",
         "opts": [
             "Greater intensity of the same ordinary activity",
             "In every single case, being directed toward a Realized One or his disciple, "
             "approached with settled faith and devotion",
             "Performing the activity in complete solitude",
             "Performing the activity only at dawn"],
         "correct": 1,
         "expl": "Seeing, hearing, acquiring, training, serving, and recollecting a Realized One "
                 "or disciple, specifically."},
        {"q": "What does the unsurpassable training specifically consist of?",
         "opts": [
             "Archery and swordsmanship at an elite level",
             "The higher ethics, the higher mind, and the higher wisdom, in the teaching and "
             "training proclaimed by a Realized One",
             "Elephant and horse riding",
             "Formal debate technique"],
         "correct": 1,
         "expl": "Contrasted with the ordinary training in worldly skills named earlier in the "
                 "same item."},
        {"q": "What double function does the guide attribute to AN 6.30?",
         "opts": [
             "It has no special function beyond closing this chapter",
             "It closes both this chapter's own material and completes a thread left open since "
             "AN 6.8 in the previous chapter — few discourses in this nipāta serve both roles",
             "It only relates to discourses outside this nipāta entirely",
             "It functions only as a repeat of AN 6.8 with no new content"],
         "correct": 1,
         "expl": "Answering both its immediate chapter and an earlier chapter's unfinished list."},
        {"q": "What is the ordinary version of 'unsurpassable acquisition'?",
         "opts": [
             "Acquiring faith in a Realized One",
             "Acquiring a child, a wife, wealth, or a diverse spectrum of things",
             "Acquiring the five faculties",
             "Acquiring merit through generosity alone"],
         "correct": 1,
         "expl": "The worldly counterpart, acknowledged but judged insufficient."},
        {"q": "Is a setting stated for AN 6.30?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Isipatana", "Yes, near Sāma village"],
         "correct": 1,
         "expl": "A bare formula closing this chapter, continuing its frequent pattern."},
        {"q": "What fivefold judgment does the discourse pass on each ordinary version?",
         "opts": [
             "'Excellent, valuable, rare, noble, and meaningful'",
             "'Low, crude, ordinary, ignoble, and pointless'",
             "'Dangerous, forbidden, unclean, shameful, and criminal'",
             "No judgment is passed on the ordinary versions"],
         "correct": 1,
         "expl": "Applied identically across the items where this fuller judgment is given."},
        {"q": "What canonical text elsewhere gives a closely related unpacking of this same "
              "six-item list, according to the guide?",
         "opts": [
             "The Vinaya Piṭaka", "MN 30", "The Dhammapada", "SN 5.2"],
         "correct": 1,
         "expl": "Named already in AN 6.8's own reading guide, before AN 6.30's in-nipāta "
                 "expansion was reached."},
    ],
    marginalia=[
        ("Six unsurpassable, expanded", [
            "seeing &middot; hearing",
            "acquisition &middot; training",
            "service &middot; recollection",
        ]),
        ("The repeated pattern", [
            "ordinary version: real,",
            "but low and pointless",
            "unsurpassable: toward",
            "a Realized One",
        ]),
        ("Closing a long thread", [
            "AN 6.8 left this bare —",
            "this page is what",
            "it was waiting for",
        ]),
        ("Cross-references", [
            "AN 6.8 &middot; the original bare list",
            "AN 6.21 &middot; this chapter's opening",
        ]),
    ],
    further=[
        '<a href="%s/an6.30/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.8.html">AN 6.8 &middot; Unsurpassable</a> &mdash; the original bare list, '
        "now fully explained.",
        '<a href="an-6.29.html">AN 6.29 &middot; With Udāyī</a> &mdash; previous, closing this '
        "chapter's run of recollection-themed discourses.",
    ],
)
